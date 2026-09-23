#!/usr/bin/env python3
"""Populate high-confidence controlled analytical variables.

This first-pass coder focuses on record_type, media_format, and activity_status.
It preserves ambiguity by assigning `unclear` and creating a manual-review queue
rather than forcing low-confidence classifications.

The script reads `data/analysis/national_verified_registry_v1.csv` and writes a
relational controlled-coding file keyed by `outlet_id`. It does not modify the
Phase 1A verification source files.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
OUTPUT = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
REVIEW = ROOT / "data" / "analysis" / "audits" / "controlled_coding_manual_review_v1.csv"
RULE_VERSION = "v1.0-pass1"

FIELDS = [
    "outlet_id",
    "record_type",
    "ownership_or_governance_form",
    "media_format",
    "language_model",
    "community_orientation",
    "geographic_scope",
    "institutional_relationship",
    "newsroom_independence_form",
    "activity_status",
    "journalism_intensity",
    "core_population_role",
    "coding_confidence",
    "organization_id",
    "related_outlet_id",
    "relationship_note",
    "coding_rule_version",
]

REVIEW_FIELDS = [
    "outlet_id",
    "outlet_name",
    "jurisdiction",
    "field",
    "proposed_value",
    "reason",
    "source_value",
    "institutional_form",
    "eligibility_status",
    "verification_notes",
]


def norm(value: str) -> str:
    value = (value or "").casefold()
    value = re.sub(r"[_/\-]+", " ", value)
    value = re.sub(r"[^a-z0-9\s]+", " ", value)
    return " ".join(value.split())


def contains_any(text: str, tokens: tuple[str, ...]) -> bool:
    return any(token in text for token in tokens)


def read_rows() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def code_record_type(row: dict[str, str]) -> tuple[str, str, str | None]:
    status = norm(row.get("eligibility_status", ""))
    form = norm(row.get("institutional_form", ""))
    notes = norm(row.get("verification_notes", ""))
    text = " ".join((status, form, notes))

    if contains_any(status, ("exclude inactive", "inactive archive", "historical")) or contains_any(form, ("former newsroom", "historic ")):
        return "historical_or_inactive", "high", None
    if contains_any(status, ("classify information infrastructure", "classify host infrastructure", "classify intermediary host", "hosted information project", "comparison or media infrastructure")):
        return "information_infrastructure", "high", None
    if "multistate market case" in status or "market case" in status:
        return "market_appearance", "high", None
    if "shared operation" in status or "shared operation" in text:
        return "shared_operation_distinct_product", "high", None
    if "hosted language product" in status:
        return "hosted_language_product", "high", None
    if "hosted program" in status:
        return "hosted_program", "high", None
    if contains_any(form, ("network affiliate", "local television newsroom", "local tv newsroom", "radio station within", "television station within")):
        return "network_affiliate_or_local_station", "medium", "format/parent wording may require review"
    if row.get("core_inclusion") == "yes":
        return "standalone_outlet", "medium", None
    if contains_any(status, ("pending", "hold", "borderline")):
        return "unclear", "requires_manual_review", "boundary/pending record requires manual record-type decision"
    return "unclear", "requires_manual_review", "no deterministic record-type rule matched"


def code_media_format(row: dict[str, str]) -> tuple[str, str, str | None]:
    form = norm(row.get("institutional_form", ""))
    signals = norm(row.get("public_institutional_signals", ""))
    name = norm(row.get("outlet_name", ""))
    text = " ".join((form, signals, name))

    # Strong explicit mixed-platform wording first.
    if contains_any(text, ("multi platform", "multiplatform", "print radio tv", "newspaper radio tv", "radio tv network", "print digital radio", "television and digital newsroom", "radio and digital media operation")):
        return "mixed_platform", "high", None

    explicit = []
    checks = [
        ("radio", ("radio", "fm station", "am station")),
        ("television", ("television", " tv ", "tv station", "broadcasting company")),
        ("print", ("newspaper", "print publication", "weekly newspaper", "monthly magazine", "magazine", "print digital community publication")),
        ("newsletter", ("newsletter",)),
        ("podcast", ("podcast",)),
        ("social_first", ("social first", "facebook only", "instagram only", "social media outlet")),
        ("digital", ("digital newsroom", "digital outlet", "online newspaper", "online news", "digital publication", "news website")),
    ]
    for value, tokens in checks:
        if contains_any(f" {text} ", tokens):
            explicit.append(value)

    unique = list(dict.fromkeys(explicit))
    if len(unique) == 1:
        return unique[0], "high", None
    if len(unique) >= 2:
        # Print+digital companion wording is common and should not automatically mean mixed.
        if set(unique) == {"print", "digital"} and contains_any(form, ("newspaper", "magazine", "print")):
            return "print", "medium", "print plus companion digital presence; verify whether digital is co-primary"
        return "mixed_platform", "medium", "multiple central formats detected; manual check recommended"

    return "unclear", "requires_manual_review", "no clear primary format found"


def code_activity(row: dict[str, str]) -> tuple[str, str, str | None]:
    raw = norm(row.get("website_active", ""))
    notes = norm(row.get("verification_notes", ""))
    status = norm(row.get("eligibility_status", ""))
    text = " ".join((raw, notes, status))

    if contains_any(text, ("operationally disrupted", "temporarily disrupted", "tower loss", "suspended temporarily", "interruption")):
        return "temporarily_disrupted", "high", None
    if contains_any(status, ("exclude inactive", "inactive archive")) or contains_any(raw, ("inactive", "closed", "no current operation", "defunct")):
        return "inactive_or_closed", "high", None
    if contains_any(text, ("historical only", "historically yes", "historic")) and not contains_any(raw, ("yes", "active")):
        return "historical_only", "medium", None
    if raw in {"yes", "active", "current", "yes current"} or raw.startswith("yes ") or raw.startswith("active "):
        if contains_any(raw, ("uncertain", "limited", "via parent", "resource", "station")):
            return "active_with_limited_or_uncertain_cadence", "medium", None
        return "active", "high", None
    if contains_any(raw, ("unclear", "unknown", "not confirmed", "uncertain")):
        return "unclear", "requires_manual_review", "source activity value is explicitly uncertain"
    if not raw:
        return "unclear", "requires_manual_review", "source activity value is blank"

    return "active_with_limited_or_uncertain_cadence", "medium", "nonstandard activity wording requires review"


def blank_controlled_row(outlet_id: str) -> dict[str, str]:
    row = {field: "" for field in FIELDS}
    row["outlet_id"] = outlet_id
    row.update({
        "ownership_or_governance_form": "unclear",
        "language_model": "unclear",
        "community_orientation": "unclear",
        "geographic_scope": "unclear",
        "institutional_relationship": "unclear",
        "newsroom_independence_form": "unclear",
        "journalism_intensity": "unclear",
        "core_population_role": "pending_verification",
        "coding_rule_version": RULE_VERSION,
    })
    return row


def aggregate_confidence(values: list[str]) -> str:
    rank = {
        "high": 0,
        "medium": 1,
        "low": 2,
        "requires_manual_review": 3,
    }
    return max(values, key=lambda v: rank.get(v, 3))


def review_row(source: dict[str, str], field: str, value: str, reason: str) -> dict[str, str]:
    source_map = {
        "record_type": source.get("eligibility_status", ""),
        "media_format": source.get("institutional_form", ""),
        "activity_status": source.get("website_active", ""),
    }
    return {
        "outlet_id": source["outlet_id"],
        "outlet_name": source["outlet_name"],
        "jurisdiction": source["jurisdiction"],
        "field": field,
        "proposed_value": value,
        "reason": reason,
        "source_value": source_map.get(field, ""),
        "institutional_form": source.get("institutional_form", ""),
        "eligibility_status": source.get("eligibility_status", ""),
        "verification_notes": source.get("verification_notes", ""),
    }


def main() -> None:
    rows = read_rows()
    coded: list[dict[str, str]] = []
    review: list[dict[str, str]] = []

    for source in rows:
        out = blank_controlled_row(source["outlet_id"])
        rt, rtc, rtr = code_record_type(source)
        mf, mfc, mfr = code_media_format(source)
        ac, acc, acr = code_activity(source)

        out["record_type"] = rt
        out["media_format"] = mf
        out["activity_status"] = ac
        out["coding_confidence"] = aggregate_confidence([rtc, mfc, acc])

        if source.get("core_inclusion") == "yes":
            out["core_population_role"] = "core_outlet_or_product"
        elif source.get("analysis_tier") == "contextual_noncore":
            if rt == "information_infrastructure":
                out["core_population_role"] = "contextual_infrastructure"
            elif rt == "market_appearance":
                out["core_population_role"] = "market_context_only"
            elif rt == "historical_or_inactive":
                out["core_population_role"] = "historical_context_only"
            else:
                out["core_population_role"] = "boundary_case"
        elif source.get("analysis_tier") in {"pending_verification", "hold_for_review"}:
            out["core_population_role"] = "pending_verification"
        else:
            out["core_population_role"] = "boundary_case"

        for field, value, confidence, reason in (
            ("record_type", rt, rtc, rtr),
            ("media_format", mf, mfc, mfr),
            ("activity_status", ac, acc, acr),
        ):
            if confidence == "requires_manual_review" or reason:
                review.append(review_row(source, field, value, reason or "manual review requested"))

        coded.append(out)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(coded)

    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    with REVIEW.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=REVIEW_FIELDS)
        writer.writeheader()
        writer.writerows(review)

    print(f"Records coded: {len(coded)}")
    print(f"Manual-review flags: {len(review)}")
    print(f"Controlled file: {OUTPUT}")
    print(f"Review queue: {REVIEW}")


if __name__ == "__main__":
    main()
