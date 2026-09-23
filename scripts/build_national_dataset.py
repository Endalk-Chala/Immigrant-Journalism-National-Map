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
DATASET_ORIGIN = "National Immigrant Journalism Map Phase 1A"

MASTER_COLUMNS = [
    "outlet_id",
    "outlet_name",
    "jurisdiction",
    "state_or_market",
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
    "dataset_origin",
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


def jurisdiction_from_path(path: Path) -> str:
    """Derive the Phase 1A search jurisdiction from the verification filename."""
    suffix = "_verification_v1"
    stem = path.stem
    slug = stem[:-len(suffix)] if stem.endswith(suffix) else stem
    label = slug.replace("_", " ").title()
    if label == "District Of Columbia":
        return "District of Columbia"
    return label


def normalize_row(
    row: dict[str, str], source_file: str, source_row: int, jurisdiction: str
) -> dict[str, str]:
    """Normalize minor schema differences while preserving source-language coding."""
    normalized = {k: (v or "").strip() for k, v in row.items() if k is not None}

    # Early files used `city`; files also varied between `state` and
    # `state_or_market`. Preserve outlet geography separately from the search frame.
    city_or_scope = normalized.get("city_or_scope") or normalized.get("city", "")
    state_or_market = normalized.get("state_or_market") or normalized.get("state", "")
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
        "jurisdiction": jurisdiction,
        "state_or_market": state_or_market,
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
        "dataset_origin": DATASET_ORIGIN,
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
        jurisdiction = jurisdiction_from_path(path)
        source_file = str(path.relative_to(ROOT))
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            for row_number, row in enumerate(reader, start=2):
                rows.append(normalize_row(row, source_file, row_number, jurisdiction))

    rows.sort(
        key=lambda r: (
            r["jurisdiction"],
            r["outlet_name"].casefold(),
            r["outlet_id"],
        )
    )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def build_jurisdiction_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_jurisdiction: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_jurisdiction[row["jurisdiction"]].append(row)

    summary = []
    for jurisdiction in sorted(by_jurisdiction):
        jurisdiction_rows = by_jurisdiction[jurisdiction]
        tiers = Counter(r["analysis_tier"] for r in jurisdiction_rows)
        summary.append(
            {
                "jurisdiction": jurisdiction,
                "verified_records": str(len(jurisdiction_rows)),
                "core_verified": str(tiers["core_verified"]),
                "pending_verification": str(tiers["pending_verification"]),
                "hold_for_review": str(tiers["hold_for_review"]),
                "contextual_noncore": str(tiers["contextual_noncore"]),
                "other_review_status": str(
                    tiers["other_review_status"] + tiers["missing_status"]
                ),
            }
        )
    return summary


def build_status_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    counts = Counter(r["eligibility_status"] or "[blank]" for r in rows)
    return [
        {"eligibility_status": status, "n": str(n)}
        for status, n in sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    ]


def build_diagnostics(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    outlet_ids = [r["outlet_id"] for r in rows if r["outlet_id"]]
    duplicate_ids = sum(n - 1 for n in Counter(outlet_ids).values() if n > 1)
    metrics = [
        ("verification_files", len(input_files())),
        ("jurisdictions", len({r["jurisdiction"] for r in rows if r["jurisdiction"]})),
        ("national_verified_records", len(rows)),
        ("core_verified_records", sum(r["core_inclusion"] == "yes" for r in rows)),
        ("blank_jurisdiction_records", sum(not r["jurisdiction"] for r in rows)),
        ("blank_outlet_id_records", sum(not r["outlet_id"] for r in rows)),
        ("duplicate_outlet_id_extra_rows", duplicate_ids),
    ]
    return [{"metric": metric, "value": str(value)} for metric, value in metrics]


def main() -> None:
    rows = build_rows()
    core_rows = [r for r in rows if r["core_inclusion"] == "yes"]

    write_csv(OUTPUT_DIR / "national_verified_registry_v1.csv", rows, MASTER_COLUMNS)
    write_csv(OUTPUT_DIR / "national_core_outlets_v1.csv", core_rows, MASTER_COLUMNS)

    summary_columns = [
        "jurisdiction",
        "verified_records",
        "core_verified",
        "pending_verification",
        "hold_for_review",
        "contextual_noncore",
        "other_review_status",
    ]
    write_csv(
        OUTPUT_DIR / "state_summary_v1.csv",
        build_jurisdiction_summary(rows),
        summary_columns,
    )
    write_csv(
        OUTPUT_DIR / "eligibility_status_summary_v1.csv",
        build_status_summary(rows),
        ["eligibility_status", "n"],
    )
    write_csv(
        OUTPUT_DIR / "build_diagnostics_v1.csv",
        build_diagnostics(rows),
        ["metric", "value"],
    )

    print(f"Verification files: {len(input_files())}")
    print(f"Jurisdictions: {len({r['jurisdiction'] for r in rows})}")
    print(f"National verified records: {len(rows)}")
    print(f"Core verified outlets/products: {len(core_rows)}")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
