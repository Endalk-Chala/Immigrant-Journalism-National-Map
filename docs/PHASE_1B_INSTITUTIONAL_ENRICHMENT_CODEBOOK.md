# Phase 1B Institutional Enrichment Codebook

## Purpose

Phase 1B deepens the frozen Phase 1A national sampling frame using publicly available institutional evidence. It does **not** reopen Phase 1A inclusion decisions. Its purpose is to describe the organizational resources, structures, and capacities of the 301 core verified outlets/products so that Phase 2 interview sampling can be purposive and analytically defensible.

Phase 1B asks: **What can be established from public evidence about the institutional capacity and organizational conditions of the outlets already identified in Phase 1A?**

The enriched dataset should be joined to the frozen Phase 1A frame by `outlet_id`. Phase 1A files remain unchanged.

---

# General coding principles

1. **Public evidence only.** Phase 1B uses publicly available institutional information, not private or inferred personal information.
2. **Silence is not absence.** If a website does not mention a resource, code `not_publicly_disclosed`, not `no`.
3. **Do not infer internal capacity from organizational size alone.** A small outlet may have external legal or safety support; a large outlet may not publicly disclose it.
4. **Distinguish outlet-level from parent-level evidence.** If a hosted product inherits resources from a parent or host, record that relationship explicitly.
5. **Prefer direct evidence.** First-party organizational pages, staff pages, annual reports, IRS filings, grant announcements, funder pages, membership directories, and official network listings outrank secondary profiles.
6. **Preserve source URLs and evidence dates.** Every substantive coded field should be traceable to at least one source.
7. **Do not convert missing disclosure into a risk score.** Phase 1B describes public institutional capacity; risk interpretation belongs to later analysis.
8. **Use controlled values where comparison matters and descriptive text where nuance matters.**
9. **Do not infer protected or sensitive characteristics of individual staff.** Community orientation and language service are institutional variables, not personal demographic classifications.
10. **Phase 1B is enrichment, not eligibility screening.** A weakly resourced core outlet remains in the Phase 1A population.

---

# Missingness / disclosure status

For fields where public disclosure may be incomplete, use the following controlled values:

- `explicitly_disclosed` — first-party or strong institutional evidence directly confirms the information.
- `externally_documented` — reliable external institutional evidence confirms it, but the outlet does not clearly disclose it itself.
- `not_publicly_disclosed` — searched relevant public sources and did not find disclosure.
- `unclear` — evidence exists but is ambiguous or conflicting.
- `not_searched` — field has not yet been researched.
- `not_applicable` — field genuinely does not apply to the organizational form.

These values should be stored in field-specific status columns when useful.

---

# Source hierarchy

Preferred evidence order:

1. outlet/organization official website;
2. parent/host organization official website;
3. annual reports, IRS Form 990, audited financials, official corporate/nonprofit filings;
4. funder/grant-maker announcements;
5. official membership/network directories;
6. professional associations and public-media/network pages;
7. credible journalism-industry or local-news reporting;
8. other secondary sources used cautiously.

Record `source_url`, `source_type`, and `evidence_date` wherever possible.

---

# A. Organizational identity and history

## 1. `founding_year`
Year the outlet/product began operating.

Values: four-digit year; `unclear`; `not_publicly_disclosed`.

Rule: distinguish founding of the outlet/product from founding of a parent organization.

## 2. `founding_status`
- `explicitly_disclosed`
- `externally_documented`
- `not_publicly_disclosed`
- `unclear`

## 3. `founder_or_origin_note`
Short descriptive text on institutional origin, merger, community initiative, newsroom spinout, hosted launch, etc.

Do not code founder demographic identity unless explicitly institutionally relevant and ethically justified.

## 4. `parent_or_host_name`
Name of parent, host, fiscal sponsor, chain, network, or umbrella organization where applicable.

## 5. `parent_resource_relationship`
- `resources_primarily_outlet_level`
- `resources_shared_with_parent`
- `resources_primarily_parent_level`
- `unclear`
- `not_applicable`

---

# B. Ownership and governance

## 6. `legal_organizational_form`
- `nonprofit_501c3`
- `other_nonprofit`
- `for_profit_corporation_or_llc`
- `sole_proprietorship_or_individual_business`
- `public_media_or_public_entity`
- `university_or_school_based`
- `community_or_civic_host`
- `religious_organization_host`
- `fiscally_sponsored_project`
- `cooperative_or_collective`
- `mixed_or_hybrid`
- `unclear`
- `not_publicly_disclosed`

This is a Phase 1B refinement of the broader Phase 1A governance category.

## 7. `ownership_structure`
- `independent_owner_operated`
- `family_owned`
- `founder_led`
- `employee_or_worker_owned`
- `chain_or_group_owned`
- `nonprofit_board_governed`
- `parent_organization_owned`
- `public_or_university_governed`
- `mixed_or_other`
- `unclear`
- `not_publicly_disclosed`

Do not infer `family_owned` or `founder_led` from names alone.

## 8. `governing_board_public`
- `yes`
- `no_public_board_identified`
- `not_applicable`
- `unclear`
- `not_searched`

`no_public_board_identified` means no board was found publicly; it does not prove no board exists.

## 9. `board_or_governance_url`
Primary evidence URL for governance structure.

---

# C. Staffing and newsroom capacity

## 10. `public_staff_count`
Numeric count of publicly listed current staff where reasonably ascertainable.

Do not treat this automatically as total employment.

## 11. `staff_size_band`
- `1_person`
- `2_5`
- `6_10`
- `11_25`
- `26_50`
- `51_plus`
- `unclear`
- `not_publicly_disclosed`

Use the narrowest defensible band from public evidence.

## 12. `staff_count_basis`
- `official_staff_directory`
- `annual_report_or_financial_document`
- `official_about_page`
- `credible_external_profile`
- `other`
- `unclear`

## 13. `editorial_leadership_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`

## 14. `public_editorial_roles`
Semicolon-separated roles only, such as `editor_in_chief;publisher;managing_editor;news_director`.

## 15. `employment_model_public`
- `mostly_staff`
- `staff_plus_freelancers`
- `mostly_freelance_or_contributor`
- `volunteer_heavy`
- `mixed`
- `unclear`
- `not_publicly_disclosed`

Do not infer from byline counts alone.

---

# D. Revenue and funding model

## 16. `revenue_model`
- `advertising_primary`
- `subscription_or_membership_primary`
- `philanthropy_or_grants_primary`
- `donations_primary`
- `public_funding_primary`
- `sponsorship_primary`
- `mixed_revenue`
- `host_supported`
- `unclear`
- `not_publicly_disclosed`

Use only when the dominant model is explicit enough to support coding.

## 17. `revenue_sources_public`
Semicolon-separated controlled indicators:
- `advertising`
- `subscriptions`
- `memberships`
- `individual_donations`
- `foundation_grants`
- `government_grants`
- `public_media_funding`
- `sponsorships`
- `events`
- `services_or_contracts`
- `parent_or_host_support`
- `other`

## 18. `annual_revenue_amount`
Most recent publicly documented annual revenue, numeric USD where available.

## 19. `annual_revenue_year`
Fiscal/calendar year associated with the amount.

## 20. `revenue_band`
- `under_100k`
- `100k_499k`
- `500k_999k`
- `1m_4_99m`
- `5m_9_99m`
- `10m_plus`
- `unclear`
- `not_publicly_disclosed`

## 21. `funders_publicly_named`
- `yes`
- `not_publicly_disclosed`
- `not_applicable`
- `unclear`

## 22. `named_funders`
Semicolon-separated institutional funders only when publicly disclosed.

Do not infer ongoing support from a single historical grant; capture dates where possible.

## 23. `funding_source_url`
Primary evidence URL for revenue/funding coding.

---

# E. Network and institutional support

## 24. `network_memberships`
Semicolon-separated verified memberships or formal affiliations, e.g. INN, LION, public-media networks, ethnic/community media associations, local collaborative networks.

## 25. `network_membership_status`
- `verified_member`
- `public_affiliation_not_formal_membership`
- `none_found_publicly`
- `unclear`
- `not_searched`

`none_found_publicly` is not equivalent to no membership.

## 26. `collaborative_partnerships_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`

## 27. `partnership_note`
Short description of relevant journalism, community, university, public-media, legal, or funding partnerships.

---

# F. Legal capacity and support

## 28. `legal_support_status`
- `in_house_legal_team_disclosed`
- `named_outside_counsel_disclosed`
- `pro_bono_or_legal_partner_disclosed`
- `legal_support_via_parent_or_network`
- `multiple_forms_disclosed`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

This field does **not** contain a simple yes/no value.

## 29. `legal_support_scope`
Semicolon-separated if explicit:
- `general_counsel`
- `prepublication_review`
- `defamation_or_media_law`
- `FOIA_or_records`
- `immigration_related`
- `employment`
- `copyright`
- `digital_or_privacy`
- `other`
- `unclear`

## 30. `legal_support_provider`
Name of publicly disclosed law firm, attorney, parent legal unit, nonprofit legal organization, insurance/legal hotline, or membership-based support provider.

## 31. `legal_support_source_url`
Evidence URL.

## 32. `legal_support_disclosure_status`
- `explicitly_disclosed`
- `externally_documented`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

---

# G. Safety and security capacity

## 33. `safety_support_status`
- `formal_internal_program_disclosed`
- `external_partner_or_network_support_disclosed`
- `training_or_guidance_disclosed`
- `multiple_forms_disclosed`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## 34. `safety_support_types`
Semicolon-separated if explicit:
- `physical_safety`
- `digital_security`
- `online_harassment`
- `source_protection`
- `field_reporting_protocols`
- `trauma_or_wellbeing_support`
- `emergency_or_crisis_protocol`
- `insurance_or_security_service`
- `other`

## 35. `safety_policy_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## 36. `safety_source_url`
Evidence URL.

Important: `not_publicly_disclosed` must never be interpreted as evidence that the outlet lacks safety practices.

---

# H. Editorial and accountability infrastructure

## 37. `editorial_policy_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## 38. `corrections_policy_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## 39. `ethics_policy_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## 40. `privacy_or_source_policy_public`
- `yes`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

These are indicators of publicly visible institutional infrastructure, not measures of journalism quality.

---

# I. Publishing and platform infrastructure

## 41. `publishing_cadence`
- `multiple_times_daily`
- `daily`
- `multiple_times_weekly`
- `weekly`
- `biweekly`
- `monthly`
- `irregular_but_active`
- `broadcast_schedule_based`
- `unclear`

## 42. `platform_presence`
Semicolon-separated:
- `website`
- `print`
- `radio`
- `television`
- `newsletter`
- `podcast`
- `youtube`
- `facebook`
- `instagram`
- `tiktok`
- `x`
- `whatsapp`
- `other`

## 43. `platform_dependence_public_signal`
- `platform_central`
- `platform_substantial`
- `platform_supplementary`
- `unclear`
- `not_searched`

Use only when public evidence supports an institutional publishing dependence. Do not infer dependence solely from follower counts.

---

# J. Contact and Phase 2 recruitment readiness

## 44. `public_contact_available`
- `yes_general`
- `yes_editorial`
- `yes_named_leadership`
- `multiple_contact_routes`
- `no_public_contact_found`
- `unclear`
- `not_searched`

## 45. `public_contact_type`
Semicolon-separated: `email;contact_form;phone;mailing_address;social_dm;other`.

## 46. `editor_or_leader_name_public`
Publicly listed professional contact relevant to possible recruitment.

## 47. `editor_or_leader_role_public`
Professional role only.

## 48. `recruitment_source_url`
Public page supporting the contact/role information.

These fields support later recruitment planning but do **not** constitute human-subject enrollment.

---

# K. Evidence and coding metadata

## 49. `primary_enrichment_source_url`
Primary institutional source for the row.

## 50. `secondary_enrichment_source_url`
Optional corroborating source.

## 51. `source_type`
- `official_outlet_site`
- `official_parent_or_host_site`
- `annual_report_or_financial_document`
- `government_or_tax_record`
- `funder_or_grantmaker`
- `membership_directory`
- `professional_association`
- `credible_secondary_reporting`
- `other`

## 52. `evidence_date`
Date the evidence was published or last updated, where available.

## 53. `date_checked`
Date the researcher checked the source.

## 54. `enrichment_confidence`
- `high`
- `medium`
- `low`
- `requires_manual_review`

Confidence applies to the Phase 1B enrichment record, not the credibility or quality of the outlet.

## 55. `enrichment_notes`
Short human-readable notes for ambiguity, changes over time, shared resources, or unresolved evidence.

## 56. `enrichment_version`
Initial value: `phase1b-v1.0`.

---

# Recommended Phase 1B data structure

Create a new file rather than modifying the frozen Phase 1A dataset:

`data/phase1b/institutional_enrichment_v1.csv`

Recommended key fields:

`outlet_id,organization_id,outlet_name,jurisdiction,founding_year,parent_or_host_name,parent_resource_relationship,legal_organizational_form,ownership_structure,governing_board_public,public_staff_count,staff_size_band,staff_count_basis,editorial_leadership_public,public_editorial_roles,employment_model_public,revenue_model,revenue_sources_public,annual_revenue_amount,annual_revenue_year,revenue_band,funders_publicly_named,named_funders,network_memberships,network_membership_status,collaborative_partnerships_public,legal_support_status,legal_support_scope,legal_support_provider,legal_support_disclosure_status,safety_support_status,safety_support_types,safety_policy_public,editorial_policy_public,corrections_policy_public,ethics_policy_public,privacy_or_source_policy_public,publishing_cadence,platform_presence,platform_dependence_public_signal,public_contact_available,public_contact_type,editor_or_leader_name_public,editor_or_leader_role_public,primary_enrichment_source_url,secondary_enrichment_source_url,source_type,evidence_date,date_checked,enrichment_confidence,enrichment_notes,enrichment_version`

---

# Phase 1B stopping rule

Phase 1B is complete when:

1. every Phase 1A core outlet/product has been searched using the same source hierarchy;
2. each high-priority enrichment dimension is coded or explicitly marked `not_publicly_disclosed`/`unclear`;
3. evidence URLs and check dates are preserved;
4. records requiring manual review are separated from straightforward cases;
5. enough variation is visible to construct the Phase 2 purposive interview sample.

Phase 1B does **not** require eliminating every missing value. The objective is systematic institutional enrichment, not exhaustive disclosure reconstruction.

---

# Phase 2 transition

The enriched Phase 1B dataset will support purposive interview sampling across meaningful institutional contrasts, including organizational form, staff capacity, funding model, legal/safety support, language model, media format, geography, hosted/standalone status, and community orientation.

Interview questions should then investigate what public evidence cannot reliably establish: experienced threats, informal safety practices, internal decision-making, self-censorship or chilling effects, source protection, legal vulnerability, platform dependence, immigration-related concerns, financial precarity, and organizational responses to risk.
