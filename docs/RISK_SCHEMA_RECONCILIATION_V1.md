# Risk-event schema reconciliation v1

## Purpose

This note reconciles the original GitHub risk-event protocol with the richer *Journalist Risk Ecology* workbook developed on 23 September 2026. The goal is to establish one canonical schema before additional risk-event collection continues.

The reconciliation preserves the project's central distinction among:

1. **institutional capacity** — resources and organizational conditions;
2. **documented events** — actions, harms, disruptions, or anticipatory changes linked to a target;
3. **structural exposure** — sector-, policy-, platform-, funding-, or enforcement-level conditions that may affect many outlets but cannot be attributed to an individual outlet without evidence.

No composite risk score is created.

---

## Core decision 1: use five top-level risk domains

The canonical top-level domains are:

- `legal`
- `physical`
- `political`
- `economic`
- `informational`

This replaces the earlier GitHub list of parallel domains such as `immigration_or_border_enforcement`, `online_harassment_or_doxxing`, `platform_governance`, `financial_security`, `labor_or_employment`, and `source_or_audience_safety`.

Those earlier categories remain analytically important, but they describe **actors, mechanisms, targets, or contexts**, not equivalent top-level domains.

Examples:

- ICE detention → `primary_domain=legal`, `mechanism=immigration_detention`, `actor_class=federal`.
- Pepper spray by federal agents → `primary_domain=physical`, `mechanism=assault_by_state_actor`, `actor_class=federal`.
- Doxxing or coordinated online abuse → `primary_domain=informational`, with the appropriate mechanism.
- Platform referral loss → usually `primary_domain=economic`, `secondary_domain=informational`, with `actor_class=market_or_funder`.
- Staff loss or closure pressure → `primary_domain=economic`, `mechanism=staff_loss_or_closure`.
- Source intimidation → `primary_domain=political` where pressure operates through fear/access, with `target_type=source_or_community` when appropriate.

A `secondary_domain` may be used where an event clearly spans two domains.

---

## Core decision 2: separate domain from mechanism

One row should identify the principal action or exposure through a controlled `mechanism` field.

Canonical mechanisms include the workbook values:

### Legal
`arrest_or_charge`; `immigration_detention`; `deportation_or_removal`; `visa_revocation_or_denial`; `border_stop_or_device_search`; `subpoena_or_legal_order`; `civil_suit_or_slapp`; `registration_demand`; `prior_restraint`; `records_denial`.

### Physical
`assault_by_state_actor`; `assault_by_private_actor`; `equipment_damage_or_seizure`; `premises_attack`; `detention_conditions_harm`.

### Political
`access_denial`; `credential_revocation`; `chilling_statement`; `regulatory_pressure`; `legislative_threat`; `source_intimidation`.

### Economic
`public_funding_withdrawal`; `philanthropic_withdrawal`; `advertiser_withdrawal`; `distribution_loss`; `staff_loss_or_closure`.

### Informational
`state_surveillance`; `spyware_or_intrusion`; `doxxing_or_swatting`; `coordinated_harassment`; `platform_action`; `transnational_digital_threat`; `anticipatory_self_censorship`.

Two additional mechanisms are added because existing project cases require them without forcing misleading labels:

- `anticipatory_risk_mitigation` — an outlet changes or cancels reporting, source, staffing, or field practices in anticipation of a plausible threat, without implying that the change is necessarily self-censorship;
- `structural_platform_or_market_shift` — a sector-level platform, referral, advertising, or funding change that creates exposure but is not itself an outlet-specific incident.

If a future case cannot fit a mechanism without distortion, add a new mechanism only after defining it in the codebook.

---

## Core decision 3: retain episode structure

The workbook's `episode_id` and `compounds_with` fields are adopted.

- `event_id` identifies one coded row.
- `episode_id` links multiple actions in the same sequence.
- `compounds_with` links an event to an earlier event whose effects it compounds.

This is preferable to placing arrest, detention, deportation, legal outcome, and organizational response into one undifferentiated row.

Existing broad GitHub rows may remain temporarily intact during migration, but new coding should favor one principal mechanism per row whenever the evidence permits.

---

## Core decision 4: distinguish record type from event scope

Add `record_type`:

- `documented_event`
- `anticipatory_response`
- `structural_exposure`
- `legal_or_administrative_outcome`

Retain `event_scope`, but normalize it to:

- `individual_journalist`
- `single_outlet`
- `multiple_outlets`
- `sector_wide`
- `platform_wide`

Values such as `statewide_sector` and `multi_state_assignment` are not scope categories.

- `statewide_sector` → `event_scope=sector_wide`, with state recorded in `event_state`.
- `multi_state_assignment` → normally `event_scope=single_outlet`; outlet home location comes from the outlet table, while the planned/actual event location is recorded separately.

---

## Core decision 5: adopt target, actor, and coercion fields

The following workbook fields become canonical:

### Target
- `target_type`: `organisation`; `individual`; `both`; `source_or_community`
- `target_name`
- `target_role`
- `target_status`

`target_status` is used only when publicly stated and analytically necessary. Never infer immigration status.

### Actor
- `actor_class`: `federal`; `state_local`; `nonstate_domestic`; `home_country`; `market_or_funder`; `unknown`
- `actor_named`

### Coercion
- `coercion_type`: `direct`; `indirect`; `anticipatory`

These fields allow immigration enforcement, home-country pressure, platforms, funders, and non-state harassment to be represented without turning each into a separate top-level risk domain.

---

## Core decision 6: adopt severity and reversibility, but not a risk score

The workbook's descriptive severity scale is retained:

- `1` — chilling/environmental change without a discrete action against a specific target;
- `2` — obstruction of reporting or access;
- `3` — coercive cost such as arrest, detention, litigation, funding loss, or major staff loss;
- `4` — grave harm such as removal from the country, significant injury, imprisonment, or outlet closure.

`reversibility`:

- `reversible`
- `partly_reversible`
- `irreversible`
- `unknown`

Severity is an event descriptor. It must **not** be summed with institutional variables into an outlet-level risk score.

---

## Core decision 7: preserve consequences and organizational response

The original GitHub distinction between event and consequence is retained.

`documented_consequence` remains a semicolon-separated field using controlled values where possible. Existing off-schema values should be normalized to broader outcomes rather than proliferating near-duplicates.

Examples:

- `physical_contact` → `injury` only if injury is documented; otherwise describe contact in `outcome` and use `reporting_interruption` if documented.
- `staff_loss` / `reduced_editorial_capacity` → `staff_reduction`; add `publication_reduction` only when reduced publishing is documented.
- `reporting_assignment_cancelled` / `coverage_constraint` → `reporting_interruption` with the precise decision described in `organizational_response` or `outcome`.
- `safety_risk` alone is not a consequence; it is an exposure condition.

`organizational_response` remains descriptive because legal challenges, safety planning, paired reporting, remote reporting, emergency fundraising, and other adaptations are analytically important.

---

## Core decision 8: distinguish event location from outlet jurisdiction

The event table should use:

- `event_state`
- `event_city`

The outlet's home jurisdiction should be obtained by joining through `outlet_id` or `organization_id` rather than duplicated ambiguously in the event record.

This resolves cases such as a New York newsroom cancelling a planned Colorado assignment.

---

## Core decision 9: strengthen evidence metadata

Canonical evidence fields:

- `event_status`
- `verification_level`
- `source_url_primary`
- `source_url_secondary`
- `source_type_primary`
- `legal_case_number`
- `pft_incident_url`
- `external_dataset_id`
- `date_checked`
- `coding_confidence`
- `notes`

`verification_level` follows the workbook logic:

- `1` — single source or self-report;
- `2` — two independent sources or one established tracker;
- `3` — documentary record or tracker entry supported by case/document identifiers.

The prior `event_status` field is retained because it captures whether a claim is confirmed, outlet-reported, secondary-source-reported, disputed, or unclear. It serves a different purpose from verification level.

---

## Canonical field order

The reconciled event table should use:

`event_id,episode_id,compounds_with,outlet_id,outlet_name,organization_id,comparison_case,record_type,event_date_start,event_date_end,date_precision,event_state,event_city,event_scope,target_type,target_name,target_role,target_status,primary_domain,secondary_domain,mechanism,actor_class,actor_named,coercion_type,severity,reversibility,event_status,event_summary,outcome,chilling_reported,legal_case_number,pft_incident_url,external_dataset_id,verification_level,source_url_primary,source_url_secondary,source_type_primary,date_checked,coding_confidence,documented_consequence,financial_consequence_amount,organizational_response,notes`

---

## Treatment of the existing GitHub risk rows

The current `risk_events_v1.csv` is preserved as a historical collection file. A normalized `risk_events_v2.csv` should be created rather than rewriting the v1 evidence history.

Known v1 normalizations include:

- `immigration_or_border_enforcement` → usually `legal`, `physical`, or `political` depending on the mechanism; immigration enforcement becomes actor/context.
- `platform_governance` → `economic` and/or `informational` depending on mechanism.
- `financial_security`, `labor_or_employment`, `organizational_capacity` → generally `economic` with an explicit mechanism.
- `source_or_audience_safety` → represented through `target_type=source_or_community`, domain, mechanism, and response.
- `statewide_sector` → `sector_wide` plus event state.
- `multi_state_assignment` → `single_outlet` plus event location.
- `assignment_cancellation;legal_support_constraint` → `anticipatory_risk_mitigation` rather than creating two incompatible subtypes.

The existing records should be migrated conservatively. If the current source does not support severity, target status, actor, or reversibility, use `unknown` rather than infer.

---

## Collection rule going forward

Before adding new risk records:

1. identify whether the record is a documented event, anticipatory response, structural exposure, or legal/administrative outcome;
2. code one primary domain and, when necessary, one secondary domain;
3. identify the principal mechanism;
4. identify target and actor separately;
5. distinguish direct, indirect, and anticipatory coercion;
6. preserve event consequence and organizational response separately;
7. use episode linkage for sequences of related actions;
8. never treat the absence of a tracker record as evidence of safety;
9. never attribute a sector-level exposure to an individual outlet without outlet-specific evidence;
10. do not calculate a composite risk score during collection.
