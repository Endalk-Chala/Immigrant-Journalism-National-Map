# Data Dictionary

This dictionary distinguishes **source verification fields** from **derived analytical fields**. Source fields are coded during manual Phase 1A verification. Derived fields are created by `scripts/build_national_dataset.py` and should not be hand-edited.

## Source verification fields

| Field | Meaning | Notes |
|---|---|---|
| `outlet_id` | Stable project identifier for the outlet/media product | State/DC prefix plus sequence number; used for relational linkage |
| `outlet_name` | Public name of outlet or media product | Preserve public-facing name |
| `state` or `state_or_market` | Source-file geography field | Phase 1A files used both headers; the national build preserves the value as `state_or_market` |
| `city_or_scope` | City, metro, statewide, regional, or other geographic scope | Early files may use `city`; normalized during build |
| `website` | Primary public website | Blank when no reliable current site was identified |
| `website_active` | Publicly observed website/activity status | Controlled language evolved during Phase 1A; preserve original value |
| `sustained_journalism` | Evidence assessment of sustained journalism/news/public-affairs production | Do not reduce nuanced values to yes/no without a documented recode |
| `immigrant_or_diaspora_serving` | Evidence assessment that immigrant/refugee/diaspora/language/immigrant-origin communities are substantially served | Preserves nuanced source coding |
| `institutional_form` | Publicly visible organizational/media form | Examples: nonprofit newsroom, commercial newspaper, hosted program, community radio product |
| `public_institutional_signals` | Short evidence note about visible institutional characteristics | Descriptive, not a score |
| `eligibility_status` | Detailed project decision/status after manual review | Primary field for inclusion/boundary interpretation |
| `primary_evidence_url` | Main public source supporting verification | Some early/borderline records may be blank |
| `verification_notes` | Short methodological/evidence note | Used to preserve uncertainty and decision rationale |

## Derived analytical fields

| Field | Meaning | Derivation |
|---|---|---|
| `jurisdiction` | State/DC Phase 1A search frame | Derived from the verification filename, not from the outlet's market field |
| `state_or_market` | Verbatim outlet geography/market value from source verification row | Normalizes source `state_or_market` or `state` without redefining it |
| `analysis_tier` | Broad analytical grouping for reproducible filtering | Derived from `eligibility_status` by the build script |
| `core_inclusion` | Conservative flag for the core analytical subset | `yes` only when status begins with `verified_include` or `verified_core` |
| `dataset_origin` | Identifies records as originating in this project's Phase 1A verification process | Constant value in the national analytical files |
| `source_file` | Verification CSV from which the row came | Added automatically for provenance |
| `source_row_number` | Original 1-based CSV line number including header offset | Added automatically for provenance |

### Why `jurisdiction` and `state_or_market` are separate

The distinction is methodological. `jurisdiction` answers **where the Phase 1A search was conducted**. `state_or_market` preserves **how the outlet itself was geographically coded**, including regional and multistate markets. State-level counts must use `jurisdiction`; outlet-market analysis may use `state_or_market`.

This prevents a multistate outlet from becoming a false extra "state" in summary tables and prevents early schema variation from creating blank-state records.

## Analytical tiers

`analysis_tier` intentionally simplifies detailed statuses only for high-level filtering. The original `eligibility_status` must always be retained.

- `core_verified` — status begins with `verified_include` or `verified_core`
- `pending_verification` — further verification required
- `hold_for_review` — unresolved or borderline record retained for review
- `contextual_noncore` — comparison, infrastructure, historical, or multistate contextual case
- `other_review_status` — detailed status not captured by the broad groups
- `missing_status` — no detailed eligibility status present; requires review

## Important coding rules

1. **Do not infer institutional absence from website silence.** `not_publicly_disclosed`, `unclear`, and comparable values are different from `no`.
2. **Do not treat the core subset as the complete project archive.** Boundary cases are analytically meaningful and remain in the full registry.
3. **Do not overwrite detailed source coding with simplified analytical tiers.** Recode in analysis scripts or separate derived tables.
4. **Do not insert external-directory rows directly into the master verification registry.** CUNY/Medill records first enter the discovery layer and must pass the project's own verification rules.
5. **Keep event and demographic data relational.** Press Freedom Tracker and Phase 1B event records link to outlets; ACS data link by geography. They are not outlet attributes by default.
6. **Use `jurisdiction` for state/DC sampling-frame summaries.** Do not use `state_or_market` as a substitute.

## External comparison layer

External sources are stored separately from the national analytical registry. The comparison table should use fields such as:

- `outlet_id`
- `external_source`
- `external_match_status`
- `external_record_id_or_url`
- `match_method`
- `match_confidence`
- `match_review_note`

Recommended controlled values for `external_source` include `CUNY_CCM` and `MEDILL_SOLN`.

A match indicates overlap or discoverability in an external resource. It does **not** mean the external resource defines inclusion in this project's population.

Likewise, demographic and risk-event enrichment should use separate tables keyed by geography or `outlet_id`. Keeping these layers separate prevents external resources from silently redefining the project's population.

## Build diagnostics

`data/analysis/build_diagnostics_v1.csv` is generated automatically and reports basic integrity checks including jurisdiction count, blank jurisdiction records, blank outlet IDs, and duplicate outlet-ID extra rows. These diagnostics should be reviewed whenever the analytical dataset is rebuilt.
