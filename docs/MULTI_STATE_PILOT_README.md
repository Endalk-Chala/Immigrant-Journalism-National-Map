# Five-state immigrant journalism sampling-frame pilot

## Pilot states
- Minnesota
- Wisconsin
- Illinois
- Washington
- North Carolina

The purpose is to test whether a state-by-state national institutional map is
feasible before scaling to all 50 states and Washington, D.C.

## Files
- `multi_state_candidates_seed.csv` — seed candidate registry
- `multi_state_immigrant_media_scraper.py` — generic conservative website collector
- `state_search_log_template.csv` — documents discovery work state by state

## Design
1. Discovery
2. Candidate registry
3. Eligibility screening
4. Website extraction
5. Manual institutional verification
6. State saturation review

The scraper does not determine eligibility and does not code risk. It only
surfaces public institutional signals for human review.

## First-pass target
Aim for roughly 10–20 verified outlets per pilot state where available.
Do not force an arbitrary quota if a state yields fewer qualifying outlets.

## Minimum institutional fields
- outlet name
- state/city
- website and activity status
- community served
- languages
- media format
- geographic scope
- ownership/nonprofit/host structure
- network affiliation
- staff information
- approximate public staff count
- funding information
- publicly disclosed legal/support infrastructure
- source URL
- last verified date
- eligibility status

## Missing-data principle
Website silence is not evidence of institutional absence.
Use `not publicly disclosed`, `unclear`, or `not identified by scraper`.

## Scaling decision
Only after all five states complete a first pass should the codebook be frozen
and the project expanded in regional batches.
