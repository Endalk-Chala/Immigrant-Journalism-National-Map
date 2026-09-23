#!/usr/bin/env python3
"""Build the Phase 1B institutional-enrichment template from frozen Phase 1A core outlets.

The script never edits Phase 1A source files. It creates a separate Phase 1B table,
populates identifiers and stable descriptive fields from the frozen core frame, and
initializes enrichment variables to not_searched / blank as appropriate.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "data" / "analysis" / "national_core_outlets_v1.csv"
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
OUT = ROOT / "data" / "phase1b" / "institutional_enrichment_v1.csv"

FIELDS = [
    "outlet_id","organization_id","outlet_name","jurisdiction","state_or_market","city_or_scope","website",
    "record_type","ownership_or_governance_form_phase1a","media_format","language_model","community_orientation","geographic_scope",
    "founding_year","founding_status","founder_or_origin_note","parent_or_host_name","parent_resource_relationship",
    "legal_organizational_form","ownership_structure","governing_board_public","board_or_governance_url",
    "public_staff_count","staff_size_band","staff_count_basis","editorial_leadership_public","public_editorial_roles","employment_model_public",
    "revenue_model","revenue_sources_public","annual_revenue_amount","annual_revenue_year","revenue_band","funders_publicly_named","named_funders","funding_source_url",
    "network_memberships","network_membership_status","collaborative_partnerships_public","partnership_note",
    "legal_support_status","legal_support_scope","legal_support_provider","legal_support_source_url","legal_support_disclosure_status",
    "safety_support_status","safety_support_types","safety_policy_public","safety_source_url",
    "editorial_policy_public","corrections_policy_public","ethics_policy_public","privacy_or_source_policy_public",
    "publishing_cadence","platform_presence","platform_dependence_public_signal",
    "platform_monetization_status","monetized_platforms","platform_monetization_model","platform_revenue_dependency","platform_revenue_share_or_amount","platform_revenue_evidence_url",
    "referral_dependency_status","major_referral_sources","owned_audience_channels","owned_audience_strength_public_signal",
    "platform_policy_financial_exposure","documented_demonetization_or_restriction_event","platform_risk_source_url",
    "revenue_concentration_public_signal","grant_dependency_public_signal","government_advertising_dependency_public_signal","major_funding_loss_event_public","financial_security_note",
    "public_contact_available","public_contact_type","editor_or_leader_name_public","editor_or_leader_role_public","recruitment_source_url",
    "primary_enrichment_source_url","secondary_enrichment_source_url","source_type","evidence_date","date_checked","enrichment_confidence","enrichment_notes","enrichment_version"
]

NOT_SEARCHED_FIELDS = {
    "founding_status","parent_resource_relationship","legal_organizational_form","ownership_structure","governing_board_public",
    "staff_size_band","staff_count_basis","editorial_leadership_public","employment_model_public",
    "revenue_model","revenue_band","funders_publicly_named","network_membership_status","collaborative_partnerships_public",
    "legal_support_status","legal_support_disclosure_status","safety_support_status","safety_policy_public",
    "editorial_policy_public","corrections_policy_public","ethics_policy_public","privacy_or_source_policy_public",
    "publishing_cadence","platform_dependence_public_signal","platform_monetization_status","platform_revenue_dependency",
    "referral_dependency_status","owned_audience_strength_public_signal","documented_demonetization_or_restriction_event",
    "revenue_concentration_public_signal","grant_dependency_public_signal","government_advertising_dependency_public_signal",
    "major_funding_loss_event_public","public_contact_available","enrichment_confidence"
}

with CORE.open("r", encoding="utf-8-sig", newline="") as fh:
    core_rows = list(csv.DictReader(fh))

with CONTROLLED.open("r", encoding="utf-8-sig", newline="") as fh:
    controlled = {r["outlet_id"]: r for r in csv.DictReader(fh)}

if len(core_rows) != 301:
    raise SystemExit(f"Expected 301 frozen Phase 1A core records; found {len(core_rows)}")

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=FIELDS)
    writer.writeheader()
    for src in core_rows:
        c = controlled.get(src["outlet_id"], {})
        row = {f: "" for f in FIELDS}
        row.update({
            "outlet_id": src.get("outlet_id", ""),
            "organization_id": c.get("organization_id", ""),
            "outlet_name": src.get("outlet_name", ""),
            "jurisdiction": src.get("jurisdiction", ""),
            "state_or_market": src.get("state_or_market", ""),
            "city_or_scope": src.get("city_or_scope", ""),
            "website": src.get("website", ""),
            "record_type": c.get("record_type", ""),
            "ownership_or_governance_form_phase1a": c.get("ownership_or_governance_form", ""),
            "media_format": c.get("media_format", ""),
            "language_model": c.get("language_model", ""),
            "community_orientation": c.get("community_orientation", ""),
            "geographic_scope": c.get("geographic_scope", ""),
            "primary_enrichment_source_url": src.get("primary_evidence_url", ""),
            "enrichment_version": "phase1b-v1.0",
        })
        for f in NOT_SEARCHED_FIELDS:
            if not row[f]:
                row[f] = "not_searched"
        writer.writerow(row)

print(f"Phase 1B template rows written: {len(core_rows)}")
print(OUT)
