# Minnesota immigrant-journalism sampling-frame pilot

This is a **data-collection pilot**, not a risk-scoring system.

## Files

- `mn_candidates_seed.csv` — manually assembled seed candidates.
- `mn_immigrant_media_scraper.py` — conservative public-web collector.
- Script output:
  - `outlet_page_extracts.jsonl`
  - `outlet_review_queue.csv`

## Workflow

1. Discover candidate outlets through directories and targeted searches.
2. Add candidates to the seed registry.
3. Run the scraper against verified public websites.
4. Manually review every flagged institutional signal.
5. Move only eligible, active outlets into the national sampling frame.
6. Preserve source URLs and access dates.

## What the scraper looks for

It searches a small number of likely institutional pages (About, Staff, Board,
Funders, Policies, Privacy, etc.) and flags public text associated with:

- nonprofit status
- ownership
- staff
- board
- funding
- host/network relationships
- legal support
- safety/security support
- policies

A scraper hit is **not** a coded fact. It is evidence for human review.

## Missing-data rule

`not_identified_by_scraper` does **not** mean the institution lacks the resource.
It means the automated pass did not identify it on the pages crawled.

## Ethical limits

The collector:
- uses public pages only;
- respects robots.txt;
- does not log in or bypass paywalls;
- does not crawl social-media profiles;
- does not collect personal vulnerability information;
- is intended to map organizations, not build dossiers on journalists.

## Suggested first test

Run the script on the seven Minnesota seed outlets, inspect the review queue,
and then adjust the fields before scaling to Wisconsin or another state.
