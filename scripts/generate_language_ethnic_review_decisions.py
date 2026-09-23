#!/usr/bin/env python3
"""Generate the bounded final review set for explicit language-vs-ethnic audience cases.

The community-orientation validation audit already restricts this set to records
currently coded language_community that also contain explicit ethnic/racial
audience signals (e.g., Latino/Hispanic/AAHPI). Phase 1A accepts these explicit
cases as ethnic_or_racial_community. This script writes the decisions as a
separate auditable layer; it does not broaden the rule beyond this 36-case set.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data" / "analysis" / "audits" / "community_orientation_validation_candidates_v1.csv"
OUT = ROOT / "data" / "analysis" / "community_orientation_language_ethnic_decisions_v1.csv"

FIELDS = [
    "review_id", "outlet_id", "review_scope", "previous_value", "reviewed_value",
    "resolution_status", "evidence_url", "review_note",
]

with CANDIDATES.open("r", encoding="utf-8-sig", newline="") as fh:
    rows = [
        r for r in csv.DictReader(fh)
        if r.get("signal_type") == "language_vs_explicit_ethnic_signal"
    ]

rows.sort(key=lambda r: (r.get("jurisdiction", ""), r.get("outlet_name", ""), r.get("outlet_id", "")))

if len(rows) != 36:
    raise SystemExit(f"Expected bounded Phase 1A set of 36 cases; found {len(rows)}. Review audit before proceeding.")

with OUT.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=FIELDS)
    writer.writeheader()
    for i, r in enumerate(rows, start=15):
        writer.writerow({
            "review_id": f"CO{i:03d}",
            "outlet_id": r["outlet_id"],
            "review_scope": "language_vs_explicit_ethnic_signal",
            "previous_value": r.get("current_orientation", "language_community"),
            "reviewed_value": "ethnic_or_racial_community",
            "resolution_status": "resolved",
            "evidence_url": r.get("primary_evidence_url", ""),
            "review_note": (
                "Phase 1A bounded review: the verification evidence explicitly identifies an ethnic/racial audience "
                "(for example Latino, Hispanic, AAHPI, or another named ethnic/racial community). Language remains "
                "captured separately in language_model, so community_orientation is coded ethnic_or_racial_community."
            ),
        })

print(f"Language-vs-ethnic reviewed decisions written: {len(rows)}")
print(OUT)
