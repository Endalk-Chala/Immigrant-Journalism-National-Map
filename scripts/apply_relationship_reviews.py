#!/usr/bin/env python3
"""Apply reviewed relationship decisions to the generated controlled-coding layer.

This script never edits Phase 1A verification files. It reads the reviewed pair
file and applies only rows with resolution_status=resolved to the controlled
analytical file. Multijurisdiction appearances share organization_id but retain
separate outlet records. Distinct hosted products may also share organization_id
without being deduplicated.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
DECISIONS = ROOT / "data" / "analysis" / "relationship_review_decisions_v1.csv"
VALIDATION = ROOT / "data" / "analysis" / "audits" / "relationship_validation_summary_v1.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    rows = read_csv(CONTROLLED)
    decisions = read_csv(DECISIONS)
    by_id = {row["outlet_id"]: row for row in rows}
    related = defaultdict(set)
    notes = defaultdict(list)

    resolved = [d for d in decisions if d.get("resolution_status") == "resolved"]
    for d in resolved:
        a, b = d["outlet_id_a"], d["outlet_id_b"]
        if a not in by_id or b not in by_id:
            continue
        for oid, other in ((a, b), (b, a)):
            row = by_id[oid]
            if d.get("organization_id"):
                row["organization_id"] = d["organization_id"]
            if d.get("relationship_value"):
                row["institutional_relationship"] = d["relationship_value"]
            if d.get("newsroom_independence_value"):
                row["newsroom_independence_form"] = d["newsroom_independence_value"]
            related[oid].add(other)
            notes[oid].append(d["review_note"])

    for oid, row in by_id.items():
        if related[oid]:
            row["related_outlet_id"] = ";".join(sorted(related[oid]))
        if notes[oid]:
            row["relationship_note"] = " | ".join(dict.fromkeys(notes[oid]))

    with CONTROLLED.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    status_counts = Counter(d.get("resolution_status", "") for d in decisions)
    decision_counts = Counter(d.get("decision", "") for d in decisions)
    org_members = defaultdict(set)
    for row in rows:
        if row.get("organization_id"):
            org_members[row["organization_id"]].add(row["outlet_id"])

    summary = [
        {"metric": "review_pairs_total", "value": str(len(decisions))},
        {"metric": "review_pairs_resolved", "value": str(status_counts.get("resolved", 0) + status_counts.get("resolved_nonmatch", 0))},
        {"metric": "review_pairs_pending", "value": str(status_counts.get("pending", 0))},
        {"metric": "organization_ids_assigned", "value": str(len(org_members))},
        {"metric": "records_with_organization_id", "value": str(sum(len(v) for v in org_members.values()))},
    ]
    for decision, n in sorted(decision_counts.items()):
        summary.append({"metric": f"decision::{decision}", "value": str(n)})

    VALIDATION.parent.mkdir(parents=True, exist_ok=True)
    with VALIDATION.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["metric", "value"])
        writer.writeheader()
        writer.writerows(summary)

    print(f"Reviewed pairs: {len(decisions)}")
    print(f"Resolved relationship rows applied: {len(resolved)}")
    print(f"Organization IDs assigned: {len(org_members)}")
    print(f"Validation summary: {VALIDATION}")


if __name__ == "__main__":
    main()
