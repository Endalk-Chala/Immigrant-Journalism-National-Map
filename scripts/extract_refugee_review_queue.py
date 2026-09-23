#!/usr/bin/env python3
"""Extract explicit refugee-signal cases into a compact manual-review queue."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "analysis" / "audits" / "community_orientation_validation_candidates_v1.csv"
OUT = ROOT / "data" / "analysis" / "audits" / "refugee_orientation_review_queue_v1.csv"

FIELDS = [
    "outlet_id", "outlet_name", "jurisdiction", "current_orientation",
    "suggested_review_value", "evidence_excerpt", "institutional_form",
    "eligibility_status", "primary_evidence_url",
]

with SRC.open("r", encoding="utf-8-sig", newline="") as fh:
    rows = [r for r in csv.DictReader(fh) if r.get("signal_type") == "explicit_refugee_signal"]

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=FIELDS)
    writer.writeheader()
    for r in rows:
        writer.writerow({k: r.get(k, "") for k in FIELDS})

print(f"Explicit refugee-signal records: {len(rows)}")
print(OUT)
