# National Analytical Dataset

## Purpose

This repository now contains a reproducible national analytical layer built from the project's Phase 1A state-by-state verification files.

The national dataset is **not a copy, subset, or repackaging of CUNY Center for Community Media, Medill State of Local News, the U.S. Press Freedom Tracker, or Census ACS data**. Those resources may be used later as discovery, comparison, validation, demographic-context, or event-enrichment sources. They remain analytically separate from the project's core outlet registry.

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

## Data architecture

### Source layers

- `data/candidates/` — broad discovery registries. These are intentionally inclusive and contain provisional leads.
- `data/verification/` — manually reviewed state/DC records. This is the source layer for national analytical builds.
- `data/logs/` — search and progress documentation.

### Generated analytical layer

The script `scripts/build_national_dataset.py` creates:

- `data/analysis/national_verified_registry_v1.csv` — all verification records, including core, pending, contextual, and held cases.
- `data/analysis/national_core_outlets_v1.csv` — records whose verification status begins with `verified_include` or `verified_core`.
- `data/analysis/state_summary_v1.csv` — counts by jurisdiction and analytical tier.
- `data/analysis/eligibility_status_summary_v1.csv` — counts of the original detailed eligibility-status values.

The generated registry adds provenance fields so every row can be traced back to a source file and row number.

## Core versus full registry

The full verified registry should be treated as the audit-friendly analytical universe. It retains uncertainty and boundary cases.

The core file is a conservative subset for analyses that require a clearly verified immigrant-serving journalism population.

A record excluded from the core file is **not automatically an excluded or invalid organization**. It may be pending verification, a hosted/infrastructure case, a comparison case, a multistate case, or a record requiring deeper review.

## Relationship to external datasets

### CUNY Center for Community Media

Use as a **discovery and comparison source**. CUNY maps multiple community-media populations and directories. The National Immigrant Journalism Map applies its own inclusion/verification workflow and preserves institutional categories needed for immigrant-journalism and risk-ecology research.

### Medill State of Local News

Use as a **local-news ecosystem comparison source**. Medill's population is broader and oriented toward local-news availability and news deserts. This project centers immigrant-serving journalism as the population of interest and includes transnational, hosted, language-specific, and diaspora-oriented institutional forms that may not map neatly onto general local-news categories.

### U.S. Press Freedom Tracker

Use as a **separate event-level enrichment source**. Its unit of analysis is a press-freedom incident, not an outlet registry. Phase 1B can link documented incidents to outlets through `outlet_id` or carefully documented entity matching without turning absence from the Tracker into evidence of no risk.

### Census ACS

Use as a **separate demographic-context layer**. ACS variables can support analyses of foreign-born population, language use, geography, and institutional media density. ACS data should not be merged into the core outlet file as if demographic variables were outlet attributes; use geographic keys and derived analytical tables instead.

## Reproducibility

Run from the repository root:

```bash
python scripts/build_national_dataset.py
```

The build uses only Python's standard library. It reads all CSV files in `data/verification/`, normalizes the early Minnesota `city` field to `city_or_scope`, preserves the original verification variables, adds analytical/provenance fields, and writes deterministic CSV outputs.

A GitHub Actions workflow also rebuilds the analytical files when the build script or a verification file changes.

## Versioning rule

- Do not hand-edit generated files in `data/analysis/`.
- Correct source records in `data/verification/` and rerun the build.
- Preserve detailed eligibility statuses in the source verification files.
- Increment the analytical dataset version only for a substantive schema or classification-rule change, not for routine source-row corrections.

## Research-use caution

This is a systematic national **sampling frame**, not a claim of census completeness. Counts reflect outlets and media products identified and verified under this methodology at the time of collection. Sparse states should not be interpreted as proof that no additional immigrant-serving media exist.
