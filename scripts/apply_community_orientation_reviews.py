#!/usr/bin/env python3
"""Apply reviewed community-orientation decisions to the controlled dataset."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
DECISIONS = ROOT / "data" / "analysis" / "community_orientation_review_decisions_v1.csv"
SUMMARY = ROOT / "data" / "analysis" / "audits" / "community_orientation_review_application_summary_v1.csv"

with CONTROLLED.open("r", encoding="utf-8-sig", newline="") as fh:
    rows = list(csv.DictReader(fh))
    fieldnames = fh.seek(0) or None

with DECISIONS.open("r", encoding="utf-8-sig", newline="") as fh:
    decisions = list(csv.DictReader(fh))

decision_map = {d["outlet_id"]: d for d in decisions}
updated = 0
matched = 0
for row in rows:
    d = decision_map.get(row["outlet_id"])
    if not d:
        continue
    matched += 1
    reviewed = d.get("reviewed_value", "").strip()
    if reviewed and row.get("community_orientation") != reviewed:
        row["community_orientation"] = reviewed
        updated += 1
    note = d.get("review_note", "").strip()
    if note:
        existing = row.get("relationship_note", "").strip()
        marker = f"Community review: {note}"
        row["relationship_note"] = f"{existing} | {marker}" if existing else marker
    row["coding_rule_version"] = "v1.0-pass4-reviewed-community"

with CONTROLLED.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

SUMMARY.parent.mkdir(parents=True, exist_ok=True)
with SUMMARY.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=["metric", "value"])
    writer.writeheader()
    writer.writerows([
        {"metric": "review_decisions_total", "value": len(decisions)},
        {"metric": "review_decisions_matched", "value": matched},
        {"metric": "records_value_changed", "value": updated},
        {"metric": "resolved", "value": sum(d.get("resolution_status") == "resolved" for d in decisions)},
        {"metric": "pending_operational_verification", "value": sum(d.get("resolution_status") == "pending_operational_verification" for d in decisions)},
    ])

print(f"Community decisions matched: {matched}/{len(decisions)}")
print(f"Community orientation values changed: {updated}")
