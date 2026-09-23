#!/usr/bin/env python3
"""Populate controlled analytical variables from the verified national registry.

Pass 2 codes six comparatively high-confidence dimensions:
- record_type
- ownership_or_governance_form
- media_format
- language_model
- geographic_scope
- activity_status

The script preserves ambiguity by assigning `unclear` and producing a field-level
manual-review queue rather than forcing classifications. It never modifies the
Phase 1A verification source files.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
OUTPUT = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
REVIEW = ROOT / "data" / "analysis" / "audits" / "controlled_coding_manual_review_v1.csv"
SUMMARY = ROOT / "data" / "analysis" / "audits" / "controlled_coding_summary_v1.csv"
RULE_VERSION = "v1.0-pass2"

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

NON_ENGLISH_LANGUAGES = (
    "spanish", "portuguese", "korean", "chinese", "mandarin", "cantonese",
    "vietnamese", "arabic", "somali", "hmong", "amharic", "oromo", "afar",
    "tigrinya", "french", "haitian creole", "creole", "russian", "ukrainian",
    "polish", "tagalog", "filipino", "marshallese", "chuukese", "nepali",
    "burmese", "karen", "swahili", "urdu", "hindi", "punjabi", "bengali",
    "bangla", "gujarati", "japanese", "lao", "khmer", "thai", "farsi",
    "persian", "dari", "pashto", "bosnian", "serbian", "croatian",
    "romanian", "greek", "hebrew", "armenian", "albanian", "turkish",
)


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


def combined_text(row: dict[str, str]) -> str:
    return " ".join(
        norm(row.get(field, ""))
        for field in (
            "outlet_name", "city_or_scope", "state_or_market", "institutional_form",
            "public_institutional_signals", "eligibility_status", "verification_notes",
        )
    )


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
        return "network_affiliate_or_local_station", "medium", "parent/network wording should be relationship-reviewed"
    if row.get("core_inclusion") == "yes":
        return "standalone_outlet", "medium", None
    if contains_any(status, ("pending", "hold", "borderline")):
        return "unclear", "requires_manual_review", "boundary/pending record requires manual record-type decision"
    return "unclear", "requires_manual_review", "no deterministic record-type rule matched"


def code_ownership(row: dict[str, str]) -> tuple[str, str, str | None]:
    text = combined_text(row)

    explicit_rules = [
        ("fiscally_sponsored", ("fiscally sponsored", "fiscal sponsor")),
        ("university_or_school_based", ("university", "college", "school based", "student media")),
        ("government_or_public_agency_based", ("government agency", "public agency", "city government", "county government", "state agency")),
        ("religious_organization_based", ("church", "mosque", "synagogue", "religious organization", "faith based")),
        ("cooperative_or_collective", ("cooperative", "worker owned", "collective newsroom", "media collective")),
        ("public_media", ("public media", "public radio", "public television", "pbs", "npr member")),
        ("nonprofit", ("nonprofit", "non profit", "501 c 3", "501c3", "501 c3")),
        ("community_or_civic_organization_based", ("community organization", "civic association", "community center", "immigrant organization", "refugee organization", "published by asian american civic association")),
        ("for_profit_private", (" llc", "inc ", "corporation", "privately owned", "commercial newspaper", "commercial radio", "for profit", "media company", "entertainment inc")),
    ]

    matches = []
    for value, tokens in explicit_rules:
        if contains_any(f" {text} ", tokens):
            matches.append(value)

    matches = list(dict.fromkeys(matches))
    if not matches:
        return "unclear", "requires_manual_review", "no explicit governance/ownership signal found"
    if len(matches) == 1:
        return matches[0], "high", None

    # Fiscal sponsorship is a specific governance condition and can coexist with nonprofit language.
    if "fiscally_sponsored" in matches and set(matches).issubset({"fiscally_sponsored", "nonprofit"}):
        return "fiscally_sponsored", "high", None

    # Hosted programs in community organizations should preserve the host form rather than be forced to nonprofit.
    if "community_or_civic_organization_based" in matches and "nonprofit" in matches and "for_profit_private" not in matches:
        return "community_or_civic_organization_based", "medium", "community/civic host also described as nonprofit"

    return "mixed_or_hybrid", "requires_manual_review", "multiple governance signals detected: " + ", ".join(matches)


def code_media_format(row: dict[str, str]) -> tuple[str, str, str | None]:
    form = norm(row.get("institutional_form", ""))
    signals = norm(row.get("public_institutional_signals", ""))
    name = norm(row.get("outlet_name", ""))
    text = " ".join((form, signals, name))

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
        if set(unique) == {"print", "digital"} and contains_any(form, ("newspaper", "magazine", "print")):
            return "print", "medium", "print plus companion digital presence; verify whether digital is co-primary"
        return "mixed_platform", "medium", "multiple central formats detected; manual check recommended"

    return "unclear", "requires_manual_review", "no clear primary format found"


def code_language(row: dict[str, str], record_type: str) -> tuple[str, str, str | None]:
    text = combined_text(row)

    if record_type == "hosted_language_product" or "language product" in text:
        return "language_specific_product_within_host", "high", None
    if contains_any(text, ("multilingual", "multi lingual", "multiple languages", "three languages", "four languages")):
        return "multilingual", "high", None
    if contains_any(text, ("bilingual", "bi lingual")):
        return "bilingual", "high", None

    # Explicit pairs such as Arabic-English or Korean-English often normalize into two language names.
    languages_found = sorted({lang for lang in NON_ENGLISH_LANGUAGES if lang in text})
    has_english = "english" in text
    if has_english and languages_found:
        if len(languages_found) == 1:
            return "bilingual", "medium", "English plus one non-English language detected from descriptive fields"
        return "multilingual", "medium", "English plus multiple non-English languages detected"
    if len(languages_found) >= 3:
        return "multilingual", "medium", "three or more non-English languages detected"
    if len(languages_found) == 2:
        return "bilingual", "medium", "two non-English languages detected; verify sustained dual-language output"

    # Require explicit language-serving wording for a single-language classification.
    if len(languages_found) == 1 and contains_any(text, ("language newspaper", "language weekly", "language outlet", "language radio", "language television", "language digital", "language publication", "language news", "spanish language", "portuguese language", "korean language", "chinese language", "vietnamese language", "arabic language", "somali language", "hmong language", "french language", "russian language", "ukrainian language", "tagalog language", "filipino language")):
        return "single_non_english", "high", None

    # English-dominant should be conservative: only explicit wording counts.
    if contains_any(text, ("english language outlet", "english dominant", "publishes primarily in english", "english only")):
        return "english_dominant", "high", None

    return "unclear", "requires_manual_review", "language output structure not explicit enough for deterministic coding"


def code_geographic_scope(row: dict[str, str], record_type: str) -> tuple[str, str, str | None]:
    scope = norm(row.get("city_or_scope", ""))
    market = norm(row.get("state_or_market", ""))
    notes = norm(row.get("verification_notes", ""))
    signals = norm(row.get("public_institutional_signals", ""))
    text = " ".join((scope, market, notes, signals))

    if contains_any(text, ("transnational", "diaspora", "homeland", "cross border", "central pacific", "u s and", "us and")) and contains_any(text, ("national", "diaspora", "cross border", "central pacific", "homeland")):
        return "transnational_or_diaspora", "medium", "transnational/diaspora reach indicated; verify principal service geography"
    if contains_any(text, ("national scope", "nationwide", "u s wide", "us wide", "across the united states", "national audience", "national us")):
        return "national_us", "high", None
    if record_type == "market_appearance" or contains_any(text, ("multistate", "multi state", "regional", "two state", "three state", "six markets")):
        return "multistate_or_regional", "high" if record_type == "market_appearance" else "medium", None
    if contains_any(scope, ("statewide", "state wide")):
        return "statewide", "high", None
    if contains_any(scope, ("metro", "metropolitan", "twin cities", "greater ")):
        return "metro", "high", None
    if contains_any(scope, ("neighborhood", "city", "local")):
        return "neighborhood_or_city", "high", None

    # A city name alone is common in this field. Slash-separated city/statewide scope is not safe to reduce.
    if scope and not contains_any(scope, ("statewide", "regional", "national", "diaspora", "multi", " / ")):
        if len(scope.split()) <= 5:
            return "neighborhood_or_city", "medium", "city/local scope inferred from concise city_or_scope field"

    return "unclear", "requires_manual_review", "service geography not explicit enough for deterministic coding"


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
        "ownership_or_governance_form": source.get("institutional_form", ""),
        "media_format": source.get("institutional_form", ""),
        "language_model": " | ".join(filter(None, (source.get("institutional_form", ""), source.get("public_institutional_signals", "")))),
        "geographic_scope": " | ".join(filter(None, (source.get("city_or_scope", ""), source.get("state_or_market", "")))),
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


def write_summary(coded: list[dict[str, str]]) -> None:
    tracked = [
        "record_type", "ownership_or_governance_form", "media_format",
        "language_model", "geographic_scope", "activity_status",
        "core_population_role", "coding_confidence",
    ]
    rows = []
    for field in tracked:
        counts = Counter(row[field] for row in coded)
        for value, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            rows.append({"field": field, "value": value, "n": str(n)})
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["field", "value", "n"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = read_rows()
    coded: list[dict[str, str]] = []
    review: list[dict[str, str]] = []

    for source in rows:
        out = blank_controlled_row(source["outlet_id"])
        rt, rtc, rtr = code_record_type(source)
        own, ownc, ownr = code_ownership(source)
        mf, mfc, mfr = code_media_format(source)
        lang, langc, langr = code_language(source, rt)
        geo, geoc, geor = code_geographic_scope(source, rt)
        ac, acc, acr = code_activity(source)

        out["record_type"] = rt
        out["ownership_or_governance_form"] = own
        out["media_format"] = mf
        out["language_model"] = lang
        out["geographic_scope"] = geo
        out["activity_status"] = ac
        out["coding_confidence"] = aggregate_confidence([rtc, ownc, mfc, langc, geoc, acc])

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

        assignments = (
            ("record_type", rt, rtc, rtr),
            ("ownership_or_governance_form", own, ownc, ownr),
            ("media_format", mf, mfc, mfr),
            ("language_model", lang, langc, langr),
            ("geographic_scope", geo, geoc, geor),
            ("activity_status", ac, acc, acr),
        )
        for field, value, confidence, reason in assignments:
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

    write_summary(coded)

    print(f"Records coded: {len(coded)}")
    print(f"Manual-review flags: {len(review)}")
    print(f"Controlled file: {OUTPUT}")
    print(f"Review queue: {REVIEW}")
    print(f"Controlled summary: {SUMMARY}")


if __name__ == "__main__":
    main()
