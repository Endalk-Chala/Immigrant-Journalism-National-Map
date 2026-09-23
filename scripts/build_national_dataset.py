#!/usr/bin/env python3
"""Build reproducible national analytical datasets from Phase 1A verification files.

Inputs are the project's own manually verified state/DC CSV files in
``data/verification``. External datasets (CUNY, Medill, Press Freedom Tracker,
ACS, etc.) are deliberately NOT merged here. They belong in separate comparison
or enrichment layers so the project's original sampling frame remains auditable.

Standard-library only; no third-party dependencies required.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFICATION_DIR = ROOT / "data" / "verification"
OUTPUT_DIR = ROOT / "data" / "analysis"

MASTER_COLUMNS = [
    "outlet_id",
    "outlet_name",
    "state",
    "city_or_scope",
    "website",
    "website_active",
    "sustained_journalism",
    "immigrant_or_diaspora_serving",
    "institutional_form",
    "public_institutional_signals",
    "eligibility_status",
    "primary_evidence_url",
    "verification_notes",
    "analysis_tier",
    "core_inclusion",
    "source_file",
    "source_row_number",
]

CORE_STATUS_PREFIXES = (
    "verified_include",
    "verified_core",
)

CONTEXTUAL_STATUS_TOKENS = (
    "comparison",
    "infrastructure",
    "not_outlet",
    "multistate_market_case",
    "market_case",
    "historical",
)


def normalize_row(row: dict[str, str], source_file: str, source_row: int) -> dict[str, str]:
    """Normalize minor schema differences while preserving source-language coding."""
    normalized = {k: (v or "").strip() for k, v in row.items() if k is not None}

    # Minnesota batch used `city`; most later files use `city_or_scope`.
    city_or_scope = normalized.get("city_or_scope") or normalized.get("city", "")
    status = normalized.get("eligibility_status", "").strip()
    status_l = status.lower()

    if any(status_l.startswith(prefix) for prefix in CORE_STATUS_PREFIXES):
        analysis_tier = "core_verified"
        core_inclusion = "yes"
    elif "pending" in status_l:
        analysis_tier = "pending_verification"
        core_inclusion = "no"
    elif "hold" in status_l or "unresolved" in status_l:
        analysis_tier = "hold_for_review"
        core_inclusion = "no"
    elif any(token in status_l for token in CONTEXTUAL_STATUS_TOKENS):
        analysis_tier = "contextual_noncore"
        core_inclusion = "no"
    elif status_l:
        analysis_tier = "other_review_status"
        core_inclusion = "no"
    else:
        analysis_tier = "missing_status"
        core_inclusion = "no"

    return {
        "outlet_id": normalized.get("outlet_id", ""),
        "outlet_name": normalized.get("outlet_name", ""),
        "state": normalized.get("state", ""),
        "city_or_scope": city_or_scope,
        "website": normalized.get("website", ""),
        "website_active": normalized.get("website_active", ""),
        "sustained_journalism": normalized.get("sustained_journalism", ""),
        "immigrant_or_diaspora_serving": normalized.get("immigrant_or_diaspora_serving", ""),
        "institutional_form": normalized.get("institutional_form", ""),
        "public_institutional_signals": normalized.get("public_institutional_signals", ""),
        "eligibility_status": status,
        "primary_evidence_url": normalized.get("primary_evidence_url", ""),
        "verification_notes": normalized.get("verification_notes", ""),
        "analysis_tier": analysis_tier,
        "core_inclusion": core_inclusion,
        "source_file": source_file,
        "source_row_number": str(source_row),
    }


def input_files() -> list[Path]:
    files = sorted(VERIFICATION_DIR.glob("*.csv"))
    if not files:
        raise SystemExit(f"No verification CSVs found in {VERIFICATION_DIR}")
    return files


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in input_files():
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            for row_number, row in enumerate(reader, start=2):
                rows.append(normalize_row(row, str(path.relative_to(ROOT)), row_number))

    rows.sort(key=lambda r: (r["state"], r["outlet_name"].casefold(), r["outlet_id"]))
    return rows


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def build_state_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_state: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_state[row["state"]].append(row)

    summary = []
    for state in sorted(by_state):
        state_rows = by_state[state]
        tiers = Counter(r["analysis_tier"] for r in state_rows)
        summary.append(
            {
                "state": state,
                "verified_records": str(len(state_rows)),
                "core_verified": str(tiers["core_verified"]),
                "pending_verification": str(tiers["pending_verification"]),
                "hold_for_review": str(tiers["hold_for_review"]),
                "contextual_noncore": str(tiers["contextual_noncore"]),
                "other_review_status": str(tiers["other_review_status"] + tiers["missing_status"]),
            }
        )
    return summary


def build_status_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    counts = Counter(r["eligibility_status"] or "[blank]" for r in rows)
    return [
        {"eligibility_status": status, "n": str(n)}
        for status, n in sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    ]


def main() -> None:
    rows = build_rows()
    core_rows = [r for r in rows if r["core_inclusion"] == "yes"]

    write_csv(OUTPUT_DIR / "national_verified_registry_v1.csv", rows, MASTER_COLUMNS)
    write_csv(OUTPUT_DIR / "national_core_outlets_v1.csv", core_rows, MASTER_COLUMNS)

    state_columns = [
        "state",
        "verified_records",
        "core_verified",
        "pending_verification",
        "hold_for_review",
        "contextual_noncore",
        "other_review_status",
    ]
    write_csv(OUTPUT_DIR / "state_summary_v1.csv", build_state_summary(rows), state_columns)
    write_csv(
        OUTPUT_DIR / "eligibility_status_summary_v1.csv",
        build_status_summary(rows),
        ["eligibility_status", "n"],
    )

    print(f"Verification files: {len(input_files())}")
    print(f"National verified records: {len(rows)}")
    print(f"Core verified outlets/products: {len(core_rows)}")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
