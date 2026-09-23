#!/usr/bin/env python3
"""Audit community-orientation coding for high-priority validation cases.

This script does not change classifications. It creates reproducible review files for:
1. records currently coded unclear;
2. records with explicit refugee signals;
3. language-community records that also contain explicit ethnic/racial audience signals;
4. records where explicit immigrant/refugee/ethnic/multicultural evidence may justify review.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
OUT = ROOT / "data" / "analysis" / "audits" / "community_orientation_validation_candidates_v1.csv"
SUMMARY = ROOT / "data" / "analysis" / "audits" / "community_orientation_validation_summary_v1.csv"

FIELDS = [
    "outlet_id", "outlet_name", "jurisdiction", "current_orientation", "priority",
    "signal_type", "suggested_review_value", "evidence_excerpt", "institutional_form",
    "eligibility_status", "primary_evidence_url",
]


def norm(value: str) -> str:
    value = (value or "").casefold()
    value = re.sub(r"[_/\-]+", " ", value)
    value = re.sub(r"[^a-z0-9\s]+", " ", value)
    return " ".join(value.split())


def read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def text(row: dict[str, str]) -> str:
    return " | ".join(filter(None, (
        row.get("immigrant_or_diaspora_serving", ""),
        row.get("institutional_form", ""),
        row.get("public_institutional_signals", ""),
        row.get("verification_notes", ""),
    )))


def has(t: str, tokens: tuple[str, ...]) -> bool:
    return any(tok in t for tok in tokens)


def main() -> None:
    registry = {r["outlet_id"]: r for r in read(REGISTRY)}
    controlled = read(CONTROLLED)
    out: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(crow: dict[str, str], signal_type: str, suggested: str, priority: str) -> None:
        key = (crow["outlet_id"], signal_type)
        if key in seen:
            return
        seen.add(key)
        src = registry[crow["outlet_id"]]
        ev = text(src)
        out.append({
            "outlet_id": crow["outlet_id"],
            "outlet_name": src.get("outlet_name", ""),
            "jurisdiction": src.get("jurisdiction", ""),
            "current_orientation": crow.get("community_orientation", ""),
            "priority": priority,
            "signal_type": signal_type,
            "suggested_review_value": suggested,
            "evidence_excerpt": ev[:700],
            "institutional_form": src.get("institutional_form", ""),
            "eligibility_status": src.get("eligibility_status", ""),
            "primary_evidence_url": src.get("primary_evidence_url", ""),
        })

    ethnic_tokens = (
        "latino", "latina", "hispanic", "aahpi", "asian american", "aapi",
        "african american", "black community", "arab american", "indigenous community",
        "native hawaiian", "pacific islander",
    )
    refugee_tokens = (
        "refugee", "refugees", "refugee serving", "refugee community", "resettled",
        "resettlement",
    )
    immigrant_tokens = (
        "immigrant community", "immigrant serving", "immigrants", "new americans",
        "newcomer community", "migrant community", "migrant neighbors",
    )
    multi_tokens = (
        "multicultural", "multiethnic", "multi ethnic", "diverse communities",
        "multiple immigrant communities", "multiple language communities",
    )

    for crow in controlled:
        src = registry[crow["outlet_id"]]
        t = norm(text(src))
        current = crow.get("community_orientation", "")

        if current == "unclear":
            add(crow, "currently_unclear", "manual_review", "high")

        if has(t, refugee_tokens):
            suggested = "refugee_general"
            if has(t, immigrant_tokens + ethnic_tokens):
                suggested = "mixed_orientation"
            add(crow, "explicit_refugee_signal", suggested, "highest")

        if current == "language_community" and has(t, ethnic_tokens):
            add(crow, "language_vs_explicit_ethnic_signal", "ethnic_or_racial_community", "highest")

        if current in {"unclear", "language_community"} and has(t, immigrant_tokens):
            suggested = "immigrant_general"
            if has(t, ethnic_tokens + refugee_tokens):
                suggested = "mixed_orientation"
            add(crow, "explicit_immigrant_signal", suggested, "high")

        if current in {"unclear", "language_community", "mixed_orientation"} and has(t, multi_tokens):
            add(crow, "explicit_multicultural_signal", "multicultural_multiethnic", "high")

    priority_rank = {"highest": 0, "high": 1, "medium": 2}
    out.sort(key=lambda r: (priority_rank.get(r["priority"], 9), r["jurisdiction"], r["outlet_name"], r["signal_type"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(out)

    counts = Counter((r["signal_type"], r["suggested_review_value"]) for r in out)
    with SUMMARY.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["signal_type", "suggested_review_value", "n"])
        writer.writeheader()
        for (signal, value), n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            writer.writerow({"signal_type": signal, "suggested_review_value": value, "n": n})

    print(f"Community validation candidates: {len(out)}")
    print(f"Candidate file: {OUT}")
    print(f"Summary file: {SUMMARY}")


if __name__ == "__main__":
    main()
