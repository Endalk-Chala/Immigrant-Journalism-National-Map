#!/usr/bin/env python3
"""
Multi-state immigrant-media institutional collector.

This is a conservative public-web collector for a manually assembled
candidate list. It is designed to support a national sampling frame,
not to make automated eligibility or risk judgments.

Key principles:
- respects robots.txt
- stays on the supplied outlet domain
- throttles requests
- limits pages per outlet
- does not log in, bypass paywalls, or scrape social platforms
- flags institutional signals for manual review
- preserves URLs and text snippets
- treats missing disclosure as unknown, not absence
"""

import argparse, csv, json, re, time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

USER_AGENT = "ImmigrantJournalismResearchBot/0.2 (academic research; public web only)"
REQUEST_TIMEOUT = 20
DEFAULT_DELAY = 2.0
DEFAULT_MAX_PAGES = 10

PATH_HINTS = [
    "", "about", "about-us", "who-we-are", "team", "staff", "our-team",
    "board", "leadership", "mission", "support", "donate", "funders",
    "funding", "sponsors", "partners", "advertise", "advertising",
    "annual-report", "reports", "financials", "transparency",
    "policies", "editorial-policy", "ethics", "corrections",
    "privacy", "terms", "contact"
]

KEYWORDS = {
    "nonprofit": [r"\bnon[- ]?profit\b", r"\b501\s*\(c\)\s*\(3\)\b", r"\b501c3\b"],
    "ownership": [r"\bowned by\b", r"\bpublisher\b", r"\bfounded by\b", r"\bparent organi[sz]ation\b", r"\bLLC\b", r"\bincorporated\b"],
    "staff": [r"\bstaff\b", r"\bteam\b", r"\beditor\b", r"\breporter\b", r"\bproducer\b", r"\bpublisher\b", r"\bdirector\b"],
    "board": [r"\bboard of directors\b", r"\bboard member\b", r"\btrustee\b"],
    "funding": [r"\bfunder\b", r"\bfunding\b", r"\bgrant\b", r"\bdonor\b", r"\bdonation\b", r"\bmember support\b", r"\badvertis"],
    "network_or_host": [r"\bfiscal sponsor\b", r"\bmember of\b", r"\bnetwork\b", r"\bprogram of\b", r"\bprogramme of\b", r"\bproject of\b"],
    "legal_support": [r"\blegal counsel\b", r"\blegal adviser\b", r"\blegal advisor\b", r"\battorney\b", r"\blawyer\b", r"\blaw firm\b", r"\blegal services\b"],
    "safety_security": [r"\bdigital security\b", r"\bcybersecurity\b", r"\bsecurity vendor\b", r"\bsafety policy\b", r"\bsafety training\b", r"\bsecurity training\b"],
    "policies": [r"\beditorial policy\b", r"\bethics policy\b", r"\bcorrections policy\b", r"\bprivacy policy\b", r"\bconflict of interest\b"],
}

def normalize_base_url(url):
    if not url:
        return ""
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"

def same_domain(a,b):
    return urlparse(a).netloc.lower().replace("www.","") == urlparse(b).netloc.lower().replace("www.","")

def robots_allowed(base_url,target_url):
    rp = RobotFileParser()
    rp.set_url(urljoin(base_url,"/robots.txt"))
    try:
        rp.read()
        return rp.can_fetch(USER_AGENT,target_url)
    except Exception:
        return True

def fetch_page(session,url):
    try:
        r=session.get(url,timeout=REQUEST_TIMEOUT,allow_redirects=True)
        r.raise_for_status()
        if "text/html" not in r.headers.get("content-type",""):
            return None
        return r
    except requests.RequestException:
        return None

def extract_page(url,html):
    soup=BeautifulSoup(html,"html.parser")
    for tag in soup(["script","style","noscript","svg"]):
        tag.decompose()
    title=soup.title.get_text(" ",strip=True) if soup.title else ""
    text=re.sub(r"\s+"," ",soup.get_text(" ",strip=True))
    links=[]
    for a in soup.find_all("a",href=True):
        links.append({"url":urljoin(url,a["href"]), "label":re.sub(r"\s+"," ",a.get_text(" ",strip=True))})
    hits={}
    for category,patterns in KEYWORDS.items():
        snippets=[]
        for pat in patterns:
            for m in re.finditer(pat,text,flags=re.I):
                start=max(0,m.start()-180); end=min(len(text),m.end()+220)
                s=text[start:end].strip()
                if s not in snippets: snippets.append(s)
                if len(snippets)>=5: break
            if len(snippets)>=5: break
        hits[category]=snippets
    return {"url":url,"title":title,"text":text,"links":links,"keyword_hits":hits}

def candidate_urls(base_url,homepage_extract):
    urls=[base_url]
    for hint in PATH_HINTS[1:]:
        urls.append(urljoin(base_url+"/",hint))
    if homepage_extract:
        marker=re.compile(r"(about|team|staff|board|leadership|fund|support|donat|partner|advertis|policy|ethic|correct|privacy|contact|annual|report)",re.I)
        for link in homepage_extract["links"]:
            if same_domain(base_url,link["url"]) and marker.search(link["url"]+" "+link["label"]):
                urls.append(link["url"])
    seen=set(); out=[]
    for u in urls:
        u=u.split("#")[0]
        if u not in seen:
            seen.add(u); out.append(u)
    return out

def summarize(outlet,extracts):
    row=dict(outlet)
    row["pages_crawled"]=len(extracts)
    row["homepage_title"]=extracts[0]["title"] if extracts else ""
    for cat in KEYWORDS:
        evidence=[]
        for ex in extracts:
            for snip in ex["keyword_hits"].get(cat,[]):
                evidence.append(f"{ex['url']} :: {snip}")
                if len(evidence)>=3: break
            if len(evidence)>=3: break
        row[f"{cat}_signal"]="yes" if evidence else "not_identified_by_scraper"
        row[f"{cat}_evidence"]=" || ".join(evidence)
    row["manual_review_status"]="pending"
    row["eligibility_status"]="pending_manual_review"
    row["review_notes"]=""
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--output-dir",required=True)
    ap.add_argument("--delay",type=float,default=DEFAULT_DELAY)
    ap.add_argument("--max-pages",type=int,default=DEFAULT_MAX_PAGES)
    ap.add_argument("--state",default=None,help="Optional exact state filter")
    args=ap.parse_args()

    outdir=Path(args.output_dir); outdir.mkdir(parents=True,exist_ok=True)
    with open(args.input,newline="",encoding="utf-8-sig") as f:
        outlets=list(csv.DictReader(f))
    if args.state:
        outlets=[o for o in outlets if o.get("state")==args.state]

    session=requests.Session(); session.headers.update({"User-Agent":USER_AGENT})
    page_records=[]; review_rows=[]

    for outlet in outlets:
        if not outlet.get("website"):
            review_rows.append(summarize(outlet,[]))
            continue
        base=normalize_base_url(outlet["website"])
        homepage=fetch_page(session,base)
        home_ex=extract_page(homepage.url,homepage.text) if homepage else None
        extracts=[]
        for url in candidate_urls(base,home_ex)[:args.max_pages]:
            if not same_domain(base,url) or not robots_allowed(base,url): continue
            resp=fetch_page(session,url)
            if not resp: continue
            ex=extract_page(resp.url,resp.text)
            ex.update({"outlet_id":outlet["outlet_id"],"outlet_name":outlet["outlet_name"],"state":outlet["state"]})
            extracts.append(ex); page_records.append(ex)
            time.sleep(args.delay)
        review_rows.append(summarize(outlet,extracts))

    with open(outdir/"outlet_page_extracts.jsonl","w",encoding="utf-8") as f:
        for rec in page_records: f.write(json.dumps(rec,ensure_ascii=False)+"\n")
    if review_rows:
        with open(outdir/"outlet_review_queue.csv","w",newline="",encoding="utf-8-sig") as f:
            w=csv.DictWriter(f,fieldnames=list(review_rows[0].keys()))
            w.writeheader(); w.writerows(review_rows)
    print(f"Processed {len(outlets)} outlets")
    print("Automated signals require manual verification.")

if __name__=="__main__":
    main()
