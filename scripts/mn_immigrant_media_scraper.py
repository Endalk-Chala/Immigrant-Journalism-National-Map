#!/usr/bin/env python3
"""
Minnesota immigrant-media institutional collector (pilot).

Purpose
-------
Take a manually reviewed candidate list and collect a small amount of publicly
available institutional information from each outlet's website.

This script is intentionally conservative:
- respects robots.txt
- crawls only the supplied outlet domain
- uses a delay between requests
- limits pages per site
- does not log in, bypass paywalls, or scrape social platforms
- does not classify "risk"
- preserves source URLs and text snippets for manual verification
- treats missing disclosure as unknown, not as absence

Input
-----
CSV with columns:
outlet_id,outlet_name,state,city,website,discovery_source

Outputs
-------
1. outlet_page_extracts.jsonl
   One record per crawled page with title, URL, text, links, and keyword hits.

2. outlet_review_queue.csv
   One row per outlet with candidate institutional signals for human review.

Usage
-----
python mn_immigrant_media_scraper.py \
    --input mn_candidates_seed.csv \
    --output-dir output

Dependencies
------------
pip install requests beautifulsoup4
"""

import argparse
import csv
import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

USER_AGENT = "ImmigrantJournalismResearchBot/0.1 (academic research; public web only)"
REQUEST_TIMEOUT = 20
DEFAULT_DELAY = 2.0
DEFAULT_MAX_PAGES = 10

# We crawl only a small set of likely institutional pages.
PATH_HINTS = [
    "", "about", "about-us", "who-we-are", "team", "staff", "our-team",
    "board", "leadership", "mission", "support", "donate", "funders",
    "funding", "sponsors", "partners", "advertise", "advertising",
    "annual-report", "reports", "financials", "transparency",
    "policies", "editorial-policy", "ethics", "corrections",
    "privacy", "terms", "contact"
]

KEYWORDS = {
    "nonprofit": [
        r"\bnon[- ]?profit\b", r"\b501\s*\(c\)\s*\(3\)\b", r"\b501c3\b"
    ],
    "ownership": [
        r"\bowned by\b", r"\bpublisher\b", r"\bfounded by\b",
        r"\bparent organization\b", r"\bparent organisation\b",
        r"\bLLC\b", r"\bincorporated\b"
    ],
    "staff": [
        r"\bstaff\b", r"\bteam\b", r"\beditor\b", r"\breporter\b",
        r"\bproducer\b", r"\bpublisher\b", r"\bdirector\b"
    ],
    "board": [
        r"\bboard of directors\b", r"\bboard member\b", r"\btrustee\b"
    ],
    "funding": [
        r"\bfunder\b", r"\bfunding\b", r"\bgrant\b", r"\bdonor\b",
        r"\bdonation\b", r"\bmember support\b", r"\badvertis"
    ],
    "network_or_host": [
        r"\bfiscal sponsor\b", r"\bmember of\b", r"\bnetwork\b",
        r"\bprogram of\b", r"\bprogramme of\b", r"\bproject of\b"
    ],
    "legal_support": [
        r"\blegal counsel\b", r"\blegal adviser\b", r"\blegal advisor\b",
        r"\battorney\b", r"\blawyer\b", r"\blaw firm\b", r"\blegal services\b"
    ],
    "safety_security": [
        r"\bdigital security\b", r"\bcybersecurity\b", r"\bsecurity vendor\b",
        r"\bsafety policy\b", r"\bsafety training\b", r"\bsecurity training\b"
    ],
    "policies": [
        r"\beditorial policy\b", r"\bethics policy\b", r"\bcorrections policy\b",
        r"\bprivacy policy\b", r"\bconflict of interest\b"
    ],
}

def normalize_base_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"

def same_domain(a: str, b: str) -> bool:
    return urlparse(a).netloc.lower().replace("www.", "") == urlparse(b).netloc.lower().replace("www.", "")

def robots_allowed(base_url: str, target_url: str) -> bool:
    robots_url = urljoin(base_url, "/robots.txt")
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch(USER_AGENT, target_url)
    except Exception:
        return True

def fetch_page(session, url):
    try:
        r = session.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        r.raise_for_status()
        ctype = r.headers.get("content-type", "")
        if "text/html" not in ctype:
            return None
        return r
    except requests.RequestException:
        return None

def extract_page(url, html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])
        label = re.sub(r"\s+", " ", a.get_text(" ", strip=True))
        links.append({"url": href, "label": label})

    hits = {}
    for category, patterns in KEYWORDS.items():
        snippets = []
        for pat in patterns:
            for m in re.finditer(pat, text, flags=re.I):
                start = max(0, m.start() - 180)
                end = min(len(text), m.end() + 220)
                snippet = text[start:end].strip()
                if snippet not in snippets:
                    snippets.append(snippet)
                if len(snippets) >= 5:
                    break
            if len(snippets) >= 5:
                break
        hits[category] = snippets

    return {
        "url": url,
        "title": title,
        "text": text,
        "links": links,
        "keyword_hits": hits,
    }

def candidate_urls(base_url, homepage_extract):
    urls = [base_url]
    for hint in PATH_HINTS[1:]:
        urls.append(urljoin(base_url + "/", hint))

    if homepage_extract:
        marker = re.compile(
            r"(about|team|staff|board|leadership|fund|support|donat|partner|"
            r"advertis|policy|ethic|correct|privacy|contact|annual|report)",
            re.I,
        )
        for link in homepage_extract["links"]:
            if same_domain(base_url, link["url"]) and marker.search(link["url"] + " " + link["label"]):
                urls.append(link["url"])

    seen = set()
    out = []
    for u in urls:
        u = u.split("#")[0]
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out

def summarize_for_review(outlet, extracts):
    categories = list(KEYWORDS.keys())
    row = dict(outlet)
    row["pages_crawled"] = len(extracts)
    row["homepage_title"] = extracts[0]["title"] if extracts else ""

    for cat in categories:
        evidence = []
        for ex in extracts:
            for snip in ex["keyword_hits"].get(cat, []):
                evidence.append(f"{ex['url']} :: {snip}")
                if len(evidence) >= 3:
                    break
            if len(evidence) >= 3:
                break
        row[f"{cat}_signal"] = "yes" if evidence else "not_identified_by_scraper"
        row[f"{cat}_evidence"] = " || ".join(evidence)

    row["manual_review_status"] = "pending"
    row["eligibility_status"] = "pending_manual_review"
    row["review_notes"] = ""
    return row

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--delay", type=float, default=DEFAULT_DELAY)
    ap.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    args = ap.parse_args()

    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    with open(args.input, newline="", encoding="utf-8-sig") as f:
        outlets = list(csv.DictReader(f))

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    page_records = []
    review_rows = []

    for outlet in outlets:
        base_url = normalize_base_url(outlet["website"])
        homepage_resp = fetch_page(session, base_url)

        homepage_extract = None
        if homepage_resp is not None:
            homepage_extract = extract_page(homepage_resp.url, homepage_resp.text)

        urls = candidate_urls(base_url, homepage_extract)
        extracts = []

        for url in urls[:args.max_pages]:
            if not same_domain(base_url, url):
                continue
            if not robots_allowed(base_url, url):
                continue
            resp = fetch_page(session, url)
            if resp is None:
                continue
            ex = extract_page(resp.url, resp.text)
            ex["outlet_id"] = outlet["outlet_id"]
            ex["outlet_name"] = outlet["outlet_name"]
            extracts.append(ex)
            page_records.append(ex)
            time.sleep(args.delay)

        review_rows.append(summarize_for_review(outlet, extracts))

    jsonl_path = outdir / "outlet_page_extracts.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for record in page_records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    review_path = outdir / "outlet_review_queue.csv"
    if review_rows:
        fields = list(review_rows[0].keys())
        with open(review_path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(review_rows)

    print(f"Wrote {jsonl_path}")
    print(f"Wrote {review_path}")
    print("Important: scraper signals are candidates for manual verification, not final coded values.")

if __name__ == "__main__":
    main()
