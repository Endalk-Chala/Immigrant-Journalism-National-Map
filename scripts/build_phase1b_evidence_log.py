#!/usr/bin/env python3
"""Build the canonical Phase 1B evidence log from legacy enrichment batches.

The legacy batch CSVs contain some unquoted commas in free-text values/notes.
This script therefore does not rely on fixed CSV column positions after `field`.
It locates the first http(s) URL token, treats preceding tokens as the coded
value, and treats following tokens as the evidence note.

The script does not invent missing evidence dates, check dates, organization
IDs, or confidence judgments. Migrated rows remain `requires_manual_review`
until they are audited.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = ROOT / "data" / "phase1b" / "enrichment_batches"
OUTPUT = ROOT / "data" / "phase1b" / "enrichment_evidence_v1.csv"

OUTPUT_FIELDS = [
    "evidence_id",
    "outlet_id",
    "organization_id",
    "field_name",
    "coded_value",
    "evidence_text",
    "source_url",
    "source_type",
    "evidence_date",
    "date_checked",
    "coding_confidence",
    "notes",
    "source_batch",
    "source_row",
]

OFFICIAL_PARENT_DOMAINS = {"accionlatina.org"}
CREDIBLE_SECONDARY_DOMAINS = {"missionlocal.org", "poynter.org"}
TAX_RECORD_DOMAINS = {"projects.propublica.org"}

MIGRATION_NOTE = (
    "Migrated from legacy enrichment batch without inventing missing "
    "evidence-date/check-date metadata; review before canonical analytical merge."
)


def classify_source(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    if host in OFFICIAL_PARENT_DOMAINS:
        return "official_parent_or_host_site"
    if host in CREDIBLE_SECONDARY_DOMAINS:
        return "credible_secondary_reporting"
    if host in TAX_RECORD_DOMAINS:
        return "government_or_tax_record"
    return "official_outlet_site"


def evidence_date_from_url(url: str) -> str:
    """Extract YYYY-MM-DD only when the URL explicitly encodes the full date."""
    match = re.search(r"/((?:19|20)\d{2})/(\d{2})/(\d{2})/", url)
    return "-".join(match.groups()) if match else ""


def repair_batch_row(parts: list[str], source_row: int) -> dict[str, str]:
    """Recover a legacy batch row even when free text contains unquoted commas."""
    if len(parts) < 5:
        raise ValueError(f"Row {source_row}: too few columns: {parts!r}")

    url_index = next(
        (
            i
            for i, value in enumerate(parts)
            if value.startswith("https://") or value.startswith("http://")
        ),
        None,
    )
    if url_index is None or url_index < 3:
        raise ValueError(f"Row {source_row}: could not locate evidence URL: {parts!r}")

    return {
        "outlet_id": parts[0].strip(),
        "field_name": parts[1].strip(),
        "coded_value": ",".join(parts[2:url_index]).strip(),
        "source_url": parts[url_index].strip(),
        "evidence_text": ",".join(parts[url_index + 1 :]).strip(),
    }


def read_batch(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        expected = ["outlet_id", "field", "value", "evidence_url", "evidence_note"]
        if header != expected:
            raise ValueError(f"{path}: unexpected header {header!r}")
        for source_row, parts in enumerate(reader, start=2):
            if not parts or not any(part.strip() for part in parts):
                continue
            row = repair_batch_row(parts, source_row)
            row["source_batch"] = path.name
            row["source_row"] = str(source_row)
            rows.append(row)
    return rows


def build() -> list[dict[str, str]]:
    legacy_rows: list[dict[str, str]] = []
    for path in sorted(BATCH_DIR.glob("priority_batch*.csv")):
        legacy_rows.extend(read_batch(path))

    evidence_rows: list[dict[str, str]] = []
    for index, row in enumerate(legacy_rows, start=1):
        evidence_rows.append(
            {
                "evidence_id": f"EVID{index:06d}",
                "outlet_id": row["outlet_id"],
                "organization_id": "",
                "field_name": row["field_name"],
                "coded_value": row["coded_value"],
                "evidence_text": row["evidence_text"],
                "source_url": row["source_url"],
                "source_type": classify_source(row["source_url"]),
                "evidence_date": evidence_date_from_url(row["source_url"]),
                "date_checked": "",
                "coding_confidence": "requires_manual_review",
                "notes": MIGRATION_NOTE,
                "source_batch": row["source_batch"],
                "source_row": row["source_row"],
            }
        )
    return evidence_rows


def validate(rows: list[dict[str, str]]) -> None:
    ids = [row["evidence_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate evidence_id detected")

    for row in rows:
        if not row["outlet_id"]:
            raise ValueError(f"{row['evidence_id']}: missing outlet_id")
        if not row["field_name"]:
            raise ValueError(f"{row['evidence_id']}: missing field_name")
        if not row["source_url"].startswith(("https://", "http://")):
            raise ValueError(f"{row['evidence_id']}: invalid source_url")


def main() -> None:
    rows = build()
    validate(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} evidence rows to {OUTPUT}")


if __name__ == "__main__":
    main()
