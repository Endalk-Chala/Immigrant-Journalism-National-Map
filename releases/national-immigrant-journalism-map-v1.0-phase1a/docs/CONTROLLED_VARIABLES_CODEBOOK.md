# Controlled Analytical Variables Codebook

## Purpose

This codebook defines the **derived controlled variables** used for national analysis of the Immigrant Journalism National Map.

These variables do **not** replace the original Phase 1A verification fields. The source fields in `data/verification/` remain the evidentiary record. Controlled variables are a reproducible analytical layer designed to make national comparison possible while preserving uncertainty, hosted structures, multistate relationships, and institutional diversity.

## General coding principles

1. **Source evidence remains authoritative.** Controlled variables are derived from `institutional_form`, `city_or_scope`, `state_or_market`, `eligibility_status`, `verification_notes`, and other public evidence fields.
2. **Do not infer absence from silence.** If public evidence does not establish a category, code `unclear`, not `no`.
3. **Prefer one primary category per analytical dimension.** Use `mixed` only when no single category reasonably captures the record.
4. **Do not collapse organizational relationships.** A hosted language product and its host newsroom may both remain separate records when analytically meaningful.
5. **Do not use language, ethnicity, or ownership as interchangeable concepts.** They are distinct dimensions.
6. **Do not automatically deduplicate shared websites or similar names.** Relationship review must distinguish shared parent, shared operation, market appearance, and true duplicate.
7. **External datasets do not determine coding.** CUNY, Medill, Press Freedom Tracker, and ACS may inform discovery/comparison/enrichment but do not define these variables.
8. **Controlled coding should be reproducible.** Automated rules may assign high-confidence cases; ambiguous cases must be flagged for human review.

---

# 1. `record_type`

## Question
What kind of record is this in the project database?

## Controlled values

- `standalone_outlet` — independently identifiable journalism outlet/newsroom/publication/station.
- `hosted_program` — recurring journalism/public-affairs program operating within another organization.
- `hosted_language_product` — language-specific or translated journalism product inside a broader newsroom/organization.
- `network_affiliate_or_local_station` — local affiliate/station operating within a larger broadcast or media network.
- `shared_operation_distinct_product` — editorial product that remains distinct but shares operations/ownership with another mapped product.
- `market_appearance` — record retained to document service/circulation in a jurisdiction although the newsroom is based elsewhere.
- `information_infrastructure` — directory, service organization, community information hub, host, intermediary, or non-news infrastructure retained for context.
- `historical_or_inactive` — formerly relevant outlet retained for ecosystem history but not active core sampling.
- `unclear` — evidence insufficient for classification.

## Rules

Use `market_appearance` when the same underlying outlet is represented because it serves a second jurisdiction but has no distinct newsroom/product there.

Use `hosted_language_product` only when the language product itself has sustained journalism/public-affairs output; simple occasional translations should remain contextual/noncore.

Use `shared_operation_distinct_product` when two named products share ownership/operations but retain distinct editorial identities, editions, schedules, or audiences.

---

# 2. `ownership_or_governance_form`

## Question
What publicly visible organizational/governance form best describes the outlet or host?

## Controlled values

- `nonprofit`
- `for_profit_private`
- `public_media`
- `university_or_school_based`
- `community_or_civic_organization_based`
- `religious_organization_based`
- `government_or_public_agency_based`
- `fiscally_sponsored`
- `cooperative_or_collective`
- `mixed_or_hybrid`
- `unclear`

## Rules

Code institutional form, not editorial orientation.

If an outlet is a program inside a nonprofit community organization, code the host's governance form here and preserve `hosted_program` in `record_type`.

Do not infer `nonprofit` merely because an outlet accepts donations or has a community mission.

Do not infer `for_profit_private` merely because advertising is present.

---

# 3. `media_format`

## Question
What is the outlet/product's primary publishing/broadcast format?

## Controlled values

- `digital`
- `print`
- `radio`
- `television`
- `newsletter`
- `podcast`
- `social_first`
- `mixed_platform`
- `unclear`

## Rules

Use `mixed_platform` when two or more formats are institutionally central, not merely when a print outlet also has a website.

A print newspaper with a routine companion website remains `print` unless digital publishing is clearly a co-primary operation.

A television station with a substantial current news website remains `television` unless the organization explicitly operates as a genuinely integrated multi-platform newsroom.

---

# 4. `language_model`

## Question
How is language organized in the outlet/product?

## Controlled values

- `english_dominant`
- `single_non_english`
- `bilingual`
- `multilingual`
- `language_specific_product_within_host`
- `unclear`

## Rules

`bilingual` requires sustained publication/broadcast in two languages, not occasional translation.

`multilingual` requires sustained output in three or more languages or an explicitly multilingual program structure.

Use `language_specific_product_within_host` when the mapped record is itself one language product within a multilingual/general host operation.

Language classification should describe output, not presumed audience ethnicity.

---

# 5. `community_orientation`

## Question
What community relationship most directly explains inclusion in this project?

## Controlled values

- `immigrant_general`
- `refugee_general`
- `diaspora_national_origin`
- `ethnic_or_racial_community`
- `language_community`
- `regional_or_cross_border_community`
- `multicultural_multiethnic`
- `mixed_orientation`
- `unclear`

## Rules

Use the most institutionally explicit orientation in mission, audience description, publication identity, or sustained coverage practice.

`diaspora_national_origin` includes outlets organized around a specific national-origin or transnational diaspora community.

`language_community` is appropriate when the institution is primarily organized around a language-serving function and no narrower community identity is dominant.

Use `mixed_orientation` when two orientations are equally central and analytically inseparable.

Do not infer community orientation from language alone where contrary evidence exists.

---

# 6. `geographic_scope`

## Question
What is the outlet/product's principal service geography?

## Controlled values

- `neighborhood_or_city`
- `metro`
- `statewide`
- `multistate_or_regional`
- `national_us`
- `transnational_or_diaspora`
- `mixed_scope`
- `unclear`

## Rules

Code audience/service scope, not merely headquarters location.

A locally headquartered diaspora outlet with explicit U.S.-wide or homeland-diaspora reach may be `national_us` or `transnational_or_diaspora`.

Use `multistate_or_regional` when the core service area regularly crosses state boundaries but is not national.

---

# 7. `institutional_relationship`

## Question
How does this record relate structurally to a larger organization or other mapped records?

## Controlled values

- `standalone`
- `hosted`
- `subsidiary_or_parent_owned`
- `network_affiliate`
- `shared_operation`
- `same_outlet_multijurisdiction`
- `successor_or_predecessor`
- `unclear`

## Rules

This variable is relational and should eventually be paired with `organization_id` and, where relevant, `related_outlet_id`.

Use `same_outlet_multijurisdiction` only after manual relationship review confirms the records represent the same underlying outlet rather than distinct local editions/products.

Use `shared_operation` when records share staff/ownership/production systems but preserve distinct editorial identities.

---

# 8. `newsroom_independence_form`

## Question
How institutionally independent is the mapped journalism operation from its host/parent?

## Controlled values

- `independent_newsroom`
- `editorially_distinct_within_parent`
- `hosted_program_or_product`
- `network_local_newsroom`
- `information_project_not_newsroom`
- `unclear`

## Rules

This is **not** an editorial-independence score and should not imply freedom from owner/host influence.

It only describes organizational separateness visible in public evidence.

---

# 9. `activity_status`

## Question
What is the best standardized interpretation of current operational status?

## Controlled values

- `active`
- `active_with_limited_or_uncertain_cadence`
- `temporarily_disrupted`
- `inactive_or_closed`
- `historical_only`
- `unclear`

## Rules

This field standardizes the many raw `website_active` formulations without deleting them.

A broken or missing website does not by itself justify `inactive_or_closed`.

`temporarily_disrupted` is appropriate where current evidence documents interruption with an effort or expectation to resume.

---

# 10. `journalism_intensity`

## Question
How central is sustained journalism/public-affairs production to the mapped record?

## Controlled values

- `journalism_primary`
- `journalism_substantial_mixed_content`
- `journalism_limited_or_unclear`
- `not_independent_journalism`
- `historical_journalism`
- `unclear`

## Rules

This is a structural content-role category, **not a quality score**.

Music, events, cultural programming, service information, advocacy, or promotional content may coexist with journalism. Use `journalism_substantial_mixed_content` where journalism is sustained but not the sole or dominant function.

---

# 11. `core_population_role`

## Question
How should the record be used analytically in the national sampling frame?

## Controlled values

- `core_outlet_or_product`
- `boundary_case`
- `contextual_infrastructure`
- `market_context_only`
- `historical_context_only`
- `pending_verification`

## Rules

This variable translates detailed Phase 1A statuses into a substantively meaningful population-role field.

It should be derived from `eligibility_status`, `analysis_tier`, and relationship review, not used to overwrite them.

---

# 12. `coding_confidence`

## Question
How strong is the evidence for the controlled-variable coding on this record?

## Controlled values

- `high`
- `medium`
- `low`
- `requires_manual_review`

## Rules

`high` — coding follows explicit first-party or strong institutional evidence.

`medium` — coding is well supported but partly inferred from reliable secondary evidence or multiple descriptive fields.

`low` — evidence is limited, old, indirect, or ambiguous.

`requires_manual_review` — automated rules produce conflicts or cannot safely distinguish among categories.

This is confidence in **our classification**, not confidence in the outlet's journalism or credibility.

---

# Relational identifiers to add

These are identifiers rather than substantive categories.

## `organization_id`
Stable project identifier for the underlying parent organization/operation. Multiple outlet/product records may share one `organization_id`.

Recommended format: `ORG0001`, `ORG0002`, etc. Assign only after relationship review.

## `related_outlet_id`
Optional reference to another mapped record where a direct structural relationship matters, such as predecessor/successor, host/product, or shared operation.

## `relationship_note`
Short human-readable explanation of the relationship decision.

---

# Variables intentionally NOT collapsed into the controlled layer

The following source information should remain descriptive unless a separate research question requires additional coding:

- legal/safety/security resources
- staffing size
- revenue/funding model
- ownership identity or founder demographics
- political orientation
- journalistic quality
- credibility
- audience size
- risk level

These either require deeper evidence, are outside Phase 1A, or could create misleading inferences if coded from sparse public information.

---

# Coding workflow

1. Preserve source verification row unchanged.
2. Apply high-confidence deterministic coding rules.
3. Assign `coding_confidence`.
4. Send conflicts and ambiguous cases to a manual-review queue.
5. Resolve shared-host/similar-name relationships before assigning `organization_id`.
6. Rebuild controlled analytical file from source + reviewed overrides.
7. Never hand-edit generated analytical outputs.

# Recommended analytical file

Create a separate generated file:

`data/analysis/national_controlled_coding_v1.csv`

with one row per Phase 1A record and these fields:

`outlet_id,record_type,ownership_or_governance_form,media_format,language_model,community_orientation,geographic_scope,institutional_relationship,newsroom_independence_form,activity_status,journalism_intensity,core_population_role,coding_confidence,organization_id,related_outlet_id,relationship_note,coding_rule_version`

The controlled-coding file should join to `national_verified_registry_v1.csv` through `outlet_id` rather than duplicating the entire source registry.

# Versioning

Initial controlled-variable schema: `v1.0`.

Increment the major version only when categories or conceptual definitions change in a way that could alter interpretation. Routine record-level corrections or new reviewed overrides do not require a major schema version change.
