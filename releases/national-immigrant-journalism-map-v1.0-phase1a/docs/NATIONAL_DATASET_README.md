# National Analytical Dataset

## Purpose

This repository contains a reproducible national analytical layer built from the project's Phase 1A state-by-state verification files.

The national dataset is **not a copy, subset, or repackaging of CUNY Center for Community Media, Medill State of Local News, the U.S. Press Freedom Tracker, or Census ACS data**. Those resources may be used as discovery, comparison, validation, demographic-context, or event-enrichment sources. They remain analytically separate from the project's core outlet registry.

## What makes this dataset distinct

The project defines and verifies an institutional population centered on **immigrant, refugee, diaspora, language, ethnic, and immigrant-origin journalism in the United States**.

Its distinctive features are:

1. **Project-defined inclusion criteria.** Records are screened against a common immigrant-serving journalism definition rather than imported because they appear in another directory.
2. **State-by-state discovery and gap searching.** Each jurisdiction was searched separately, including targeted searches for language and immigrant communities that directories could miss.
3. **Manual eligibility verification.** Candidate discovery and eligibility verification are stored separately.
4. **Institutional-form sensitivity.** The project preserves distinctions among standalone newsrooms, hosted programs, translated/language products, multistate market cases, information infrastructure, and unresolved leads.
5. **Evidence-linked status coding.** Each verification record preserves an eligibility status, evidence URL where available, and verification note.
6. **No inference from silence.** Lack of publicly disclosed legal, safety, staffing, funding, or governance information is not coded as institutional absence.
7. **Relational design for later risk analysis.** The outlet registry remains separate from Phase 1B documented-event data and from demographic/contextual datasets.
8. **Traceable national construction.** Every analytical record is generated from a state/DC verification file and retains source-file and source-row provenance.

## Data architecture

### 1. Discovery layer

- `data/candidates/` — broad state-by-state candidate registries. These are intentionally inclusive and contain provisional leads.

A record appearing here is **not automatically part of the analytical population**.

### 2. Verification source layer

- `data/verification/` — manually reviewed state/DC records. This is the authoritative source layer for national analytical builds.
- `data/logs/` — search logs and national progress documentation.

Corrections to outlet eligibility or evidence should be made here, not in generated national files.

### 3. Generated national analytical layer

The script `scripts/build_national_dataset.py` creates:

- `data/analysis/national_verified_registry_v1.csv` — full verified registry including core, pending, contextual, and held cases.
- `data/analysis/national_core_outlets_v1.csv` — conservative subset whose status begins with `verified_include` or `verified_core`.
- `data/analysis/state_summary_v1.csv` — counts by Phase 1A search jurisdiction and analytical tier.
- `data/analysis/eligibility_status_summary_v1.csv` — counts of the original detailed eligibility-status values.
- `data/analysis/build_diagnostics_v1.csv` — build-integrity checks such as jurisdiction count, blank IDs, and duplicate IDs.

Generated files must not be hand-edited.

### 4. External comparison layer

- `data/external_crosswalks/external_outlet_crosswalk_template.csv` — schema for matching project outlets to external resources without inserting external records into the core registry.

A future populated crosswalk can record whether a project outlet appears in CUNY or Medill, how the match was made, and how confident the match is. The crosswalk does not determine project eligibility.

### 5. Context and risk layers

Later data should remain relational rather than being treated as outlet attributes by default:

- Census ACS — demographic/geographic context
- U.S. Press Freedom Tracker — documented press-freedom incidents
- Phase 1B project event data — documented risk events

These layers can connect through `outlet_id` or carefully specified geographic keys.

## Analytical geography

The national analytical files distinguish two different geographic concepts:

- `jurisdiction` — the state or District of Columbia search frame in which the record was identified and reviewed. It is derived reproducibly from the verification filename.
- `state_or_market` — the source verification row's own geography or market description. It may be a state, regional market, or multistate service area.

State/DC summary statistics use `jurisdiction`, not `state_or_market`.

This distinction prevents multistate market descriptions from becoming false states in national summaries and resolves schema variation among early Phase 1A files.

## Core versus full registry

The full verified registry should be treated as the audit-friendly analytical universe. It retains uncertainty and boundary cases.

The core file is a conservative subset for analyses that require a clearly verified immigrant-serving journalism population.

A record excluded from the core file is **not automatically an excluded or invalid organization**. It may be pending verification, a hosted/infrastructure case, a comparison case, a multistate case, or a record requiring deeper review.

## Relationship to external datasets

### CUNY Center for Community Media

Use as a **discovery and comparison source**. CUNY maps multiple community-media populations and directories. The National Immigrant Journalism Map applies its own inclusion/verification workflow and preserves institutional categories needed for immigrant-journalism and risk-ecology research.

A CUNY record is never imported directly into the core national dataset simply because it appears in CUNY.

### Medill State of Local News

Use as a **local-news ecosystem comparison source**. Medill's population is broader and oriented toward local-news availability and news deserts. This project centers immigrant-serving journalism as the population of interest and includes transnational, hosted, language-specific, and diaspora-oriented institutional forms that may not map neatly onto general local-news categories.

A Medill match is evidence of overlap between sampling frames, not a project inclusion decision.

### U.S. Press Freedom Tracker

Use as a **separate event-level enrichment source**. Its unit of analysis is a press-freedom incident, not an outlet registry. Phase 1B can link documented incidents to outlets through `outlet_id` or carefully documented entity matching without turning absence from the Tracker into evidence of no risk.

### Census ACS

Use as a **separate demographic-context layer**. ACS variables can support analyses of foreign-born population, language use, geography, and institutional media density. ACS data should not be merged into the core outlet file as if demographic variables were outlet characteristics; use geographic keys and derived analytical tables instead.

## Reproducibility

Run from the repository root:

```bash
python scripts/build_national_dataset.py
```

The build uses only Python's standard library. It:

1. reads every CSV in `data/verification/`;
2. derives a standardized `jurisdiction` from each state/DC verification filename;
3. preserves the source geography as `state_or_market`;
4. normalizes minor early schema differences such as `city` versus `city_or_scope`;
5. preserves detailed verification coding;
6. derives broad analytical tiers and the conservative core flag;
7. adds dataset-origin and row-level provenance fields;
8. writes deterministic national CSV outputs and build diagnostics.

A GitHub Actions workflow also rebuilds the analytical files when the build script or verification source data change.

## Provenance

Every generated national row contains:

- `dataset_origin`
- `source_file`
- `source_row_number`

This makes each analytical row traceable to the project's own Phase 1A verification record.

External comparison data use separate crosswalk tables with explicit source labels rather than being silently copied into the master registry.

## Versioning rule

- Do not hand-edit generated files in `data/analysis/`.
- Correct source records in `data/verification/` and rerun the build.
- Preserve detailed eligibility statuses in the source verification files.
- Increment the analytical dataset version for substantive schema or classification-rule changes, not routine evidence corrections.
- Preserve external source names and matching decisions in the external crosswalk layer.

## Research-use caution

This is a systematic national **sampling frame**, not a claim of census completeness. Counts reflect outlets and media products identified and verified under this methodology at the time of collection. Sparse states should not be interpreted as proof that no additional immigrant-serving media exist.
