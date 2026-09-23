#!/usr/bin/env python3
"""Code interpretive controlled variables conservatively.

This pass adds:
- community_orientation
- journalism_intensity

It reads the verified national registry plus the structural controlled-coding file,
updates only these two fields (and the aggregate coding confidence), and emits a
separate interpretive-review queue. Ambiguous cases remain `unclear`.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
REVIEW = ROOT / "data" / "analysis" / "audits" / "interpretive_coding_manual_review_v1.csv"
SUMMARY = ROOT / "data" / "analysis" / "audits" / "controlled_coding_summary_v1.csv"
RULE_VERSION = "v1.0-pass4"

REVIEW_FIELDS = [
    "outlet_id", "outlet_name", "jurisdiction", "field", "proposed_value",
    "reason", "source_value", "institutional_form", "eligibility_status",
    "verification_notes",
]


def norm(value: str) -> str:
    value = (value or "").casefold()
    value = re.sub(r"[_/\-]+", " ", value)
    value = re.sub(r"[^a-z0-9\s]+", " ", value)
    return " ".join(value.split())


def contains_any(text: str, tokens: tuple[str, ...]) -> bool:
    return any(token in text for token in tokens)


def combined_text(row: dict[str, str]) -> str:
    return " ".join(
        norm(row.get(field, ""))
        for field in (
            "outlet_name", "city_or_scope", "state_or_market", "institutional_form",
            "public_institutional_signals", "eligibility_status", "verification_notes",
            "immigrant_or_diaspora_serving",
        )
    )


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def code_community_orientation(row: dict[str, str], controlled: dict[str, str]) -> tuple[str, str, str | None]:
    text = combined_text(row)
    language_model = controlled.get("language_model", "")

    # Explicitly broad multicultural/multiethnic missions take precedence over a single-language clue.
    if contains_any(text, ("multicultural", "multiethnic", "multi ethnic", "diverse communities", "communities of color")):
        return "multicultural_multiethnic", "high", None

    if contains_any(text, ("refugee community", "refugees", "refugee serving", "newly arrived refugees")):
        if contains_any(text, ("immigrant", "diaspora", "ethnic")):
            return "mixed_orientation", "medium", "refugee orientation coexists with another explicit community orientation"
        return "refugee_general", "high", None

    if contains_any(text, ("diaspora", "national origin", "ethiopian", "somali", "hmong", "korean", "filipino", "vietnamese", "haitian", "ukrainian", "russian", "marshallese", "nepali", "burmese", "afghan", "iranian", "arab", "arab american", "mexican", "brazilian", "indian american", "pakistani", "bangladeshi", "chinese american", "japanese american")):
        # Only use diaspora/national-origin when the descriptive evidence signals an identified people/community, not just a language.
        if contains_any(text, ("community", "diaspora", "american", "immigrant", "origin", "audience")):
            return "diaspora_national_origin", "medium", "specific national-origin/diaspora community signal detected"

    if contains_any(text, ("latino community", "latina community", "hispanic community", "asian american", "aapi", "black immigrant", "african community", "ethnic community", "racial community")):
        return "ethnic_or_racial_community", "high", None

    if contains_any(text, ("immigrant serving", "immigrant community", "immigrants", "new americans", "migrant neighbors", "migrant community")):
        return "immigrant_general", "high", None

    if contains_any(text, ("cross border", "border community", "arizona sonora", "regional transborder", "transborder")):
        return "regional_or_cross_border_community", "high", None

    # Language-community is a fallback only when language structure is explicit but no narrower identity was established.
    if language_model in {"single_non_english", "language_specific_product_within_host"} and contains_any(text, ("language", "serves", "audience", "community", "news")):
        return "language_community", "medium", "language-serving function explicit but narrower community orientation not established"

    if contains_any(text, ("immigrant", "refugee", "diaspora", "ethnic", "language community")):
        return "mixed_orientation", "requires_manual_review", "multiple or insufficiently specific community signals detected"

    return "unclear", "requires_manual_review", "community orientation not explicit enough for deterministic coding"


def code_journalism_intensity(row: dict[str, str], controlled: dict[str, str]) -> tuple[str, str, str | None]:
    raw = norm(row.get("sustained_journalism", ""))
    form = norm(row.get("institutional_form", ""))
    signals = norm(row.get("public_institutional_signals", ""))
    notes = norm(row.get("verification_notes", ""))
    status = norm(row.get("eligibility_status", ""))
    record_type = controlled.get("record_type", "")
    text = " ".join((raw, form, signals, notes, status))

    if record_type == "information_infrastructure" or contains_any(status, ("information infrastructure", "host infrastructure", "intermediary host")):
        return "not_independent_journalism", "high", None

    if record_type == "historical_or_inactive" or contains_any(raw, ("historically yes", "historical")):
        return "historical_journalism", "high", None

    if contains_any(raw, ("yes mixed", "mixed with music", "mixed format", "mixed magazine", "mixed content")) or contains_any(text, ("music and news", "news and entertainment", "culture business and current events", "events and news", "service information and news")):
        return "journalism_substantial_mixed_content", "high", None

    if raw == "yes" or raw.startswith("yes ") or contains_any(raw, ("sustained", "daily reporting", "weekly reporting")):
        if contains_any(text, ("mixed", "music", "entertainment", "events", "promotional")):
            return "journalism_substantial_mixed_content", "medium", "sustained journalism coexists with substantial non-journalism content"
        return "journalism_primary", "high", None

    if contains_any(raw, ("unclear", "limited", "likely yes", "not confirmed")):
        return "journalism_limited_or_unclear", "medium", None

    if contains_any(raw, ("no as single outlet", "no independent", "no")):
        return "not_independent_journalism", "medium", None

    if row.get("core_inclusion") == "yes" and contains_any(text, ("newspaper", "newsroom", "news outlet", "news publication", "journalism", "reporting")):
        return "journalism_primary", "medium", "core inclusion plus explicit newsroom/news-publication evidence"

    return "unclear", "requires_manual_review", "journalism centrality not explicit enough for deterministic coding"


def review_row(source: dict[str, str], field: str, value: str, reason: str) -> dict[str, str]:
    source_map = {
        "community_orientation": " | ".join(filter(None, (source.get("immigrant_or_diaspora_serving", ""), source.get("institutional_form", ""), source.get("public_institutional_signals", "")))),
        "journalism_intensity": " | ".join(filter(None, (source.get("sustained_journalism", ""), source.get("institutional_form", ""), source.get("public_institutional_signals", "")))),
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


def recompute_confidence(row: dict[str, str], community_conf: str, journalism_conf: str) -> str:
    # Preserve a prior manual-review requirement; otherwise fold in this pass.
    if row.get("coding_confidence") == "requires_manual_review":
        return "requires_manual_review"
    if "requires_manual_review" in {community_conf, journalism_conf}:
        return "requires_manual_review"
    if "low" in {row.get("coding_confidence"), community_conf, journalism_conf}:
        return "low"
    if "medium" in {row.get("coding_confidence"), community_conf, journalism_conf}:
        return "medium"
    return "high"


def write_summary(rows: list[dict[str, str]]) -> None:
    tracked = [
        "record_type", "ownership_or_governance_form", "media_format", "language_model",
        "community_orientation", "geographic_scope", "institutional_relationship",
        "newsroom_independence_form", "activity_status", "journalism_intensity",
        "core_population_role", "coding_confidence",
    ]
    output = []
    for field in tracked:
        counts = Counter(row.get(field, "") for row in rows)
        for value, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            output.append({"field": field, "value": value, "n": str(n)})
    with SUMMARY.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["field", "value", "n"])
        writer.writeheader()
        writer.writerows(output)


def main() -> None:
    registry_rows = read_csv(REGISTRY)
    controlled_rows = read_csv(CONTROLLED)
    registry = {r["outlet_id"]: r for r in registry_rows}
    review = []

    for controlled in controlled_rows:
        source = registry[controlled["outlet_id"]]
        community, cc, cr = code_community_orientation(source, controlled)
        journalism, jc, jr = code_journalism_intensity(source, controlled)
        controlled["community_orientation"] = community
        controlled["journalism_intensity"] = journalism
        controlled["coding_confidence"] = recompute_confidence(controlled, cc, jc)
        controlled["coding_rule_version"] = RULE_VERSION

        for field, value, confidence, reason in (
            ("community_orientation", community, cc, cr),
            ("journalism_intensity", journalism, jc, jr),
        ):
            if confidence == "requires_manual_review" or reason:
                review.append(review_row(source, field, value, reason or "manual review requested"))

    with CONTROLLED.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=controlled_rows[0].keys())
        writer.writeheader()
        writer.writerows(controlled_rows)

    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    with REVIEW.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=REVIEW_FIELDS)
        writer.writeheader()
        writer.writerows(review)

    write_summary(controlled_rows)

    print(f"Records interpretively coded: {len(controlled_rows)}")
    print(f"Interpretive review flags: {len(review)}")
    print(f"Controlled file updated: {CONTROLLED}")
    print(f"Interpretive review queue: {REVIEW}")


if __name__ == "__main__":
    main()
