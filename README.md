# Immigrant Journalism National Map

A national institutional sampling frame of immigrant and immigrant-serving journalism outlets and media products in the United States.

## Current stage

**Phase 1A national first-pass mapping is complete for all 50 states plus the District of Columbia.**

The project identifies and verifies journalism organizations and media products that substantially serve immigrant, refugee, diaspora, language, ethnic, or immigrant-origin communities. The national map is designed as a transparent sampling frame for later qualitative and event-level research on risk ecologies.

The project now has a **reproducible national analytical dataset** generated from the state/DC verification files.

## Repository structure

- `data/candidates/` — broad state-by-state candidate registries; records are provisional at discovery stage
- `data/verification/` — manually reviewed state/DC verification files; authoritative source layer for the national dataset
- `data/analysis/` — generated national analytical files; do not hand-edit
- `data/external_crosswalks/` — separate relational layer for comparison with CUNY, Medill, or other external outlet datasets
- `data/logs/` — state search logs and national progress tracker
- `docs/METHODOLOGY_NOTE.md` — Phase 1A methodology
- `docs/NATIONAL_DATASET_README.md` — national dataset architecture, external-data boundaries, and reproducibility rules
- `docs/DATA_DICTIONARY.md` — source and derived variable definitions
- `docs/PHASE_1B_METHOD_AND_SAMPLING_MEMO.md` — documented-risk-event layer
- `scripts/build_national_dataset.py` — reproducible national dataset builder and diagnostics
- `scripts/` — public-web collection and supporting scripts
- `.github/workflows/build-national-dataset.yml` — automated national dataset rebuild

## Generated national files

Running:

```bash
python scripts/build_national_dataset.py
```

creates:

- `data/analysis/national_verified_registry_v1.csv` — full verified registry including uncertainty and boundary cases
- `data/analysis/national_core_outlets_v1.csv` — conservative core subset of clearly verified immigrant-serving journalism outlets/products
- `data/analysis/state_summary_v1.csv` — state/DC search-jurisdiction counts by analytical tier
- `data/analysis/eligibility_status_summary_v1.csv` — detailed verification-status counts
- `data/analysis/build_diagnostics_v1.csv` — reproducibility and integrity checks

Every generated national row carries `dataset_origin`, `source_file`, and `source_row_number` provenance fields.

## Geography rule

The analytical dataset deliberately separates:

- `jurisdiction` — the state/DC Phase 1A search frame, derived from the source verification filename
- `state_or_market` — the outlet's source-coded state, region, or market description

State-level national summaries use `jurisdiction`. This prevents multistate market descriptions and earlier header variation from distorting state counts.

## Methodological principle

> **Broad discovery, narrow verification, deeper coding only where analytically useful.**

The database is a **sampling frame, not a census and not a risk score**. Missing public information must not be interpreted as evidence that an institution lacks a resource, capacity, or exposure.

## How this dataset differs from existing resources

This project does not reproduce or silently merge external databases.

- **CUNY Center for Community Media** is a discovery/comparison resource. Its community-media directories do not define this project's population.
- **Medill State of Local News** is a broader local-news ecosystem resource. This project specifically centers immigrant-serving journalism and preserves hosted, diaspora, language-specific, and transnational institutional forms.
- **U.S. Press Freedom Tracker** is an event-level resource, not an outlet registry. It belongs in the separate risk-event layer.
- **Census ACS** is demographic context. It should be linked through geography for population/language analyses rather than treated as outlet data.

External records do not enter the core outlet registry simply because they appear in CUNY, Medill, or another directory. Future overlap analysis is stored in `data/external_crosswalks/` using explicit source labels, match methods, confidence, and review notes.

## Reproducibility and auditability

Generated analytical files should not be hand-edited. Corrections belong in the state/DC source verification files, after which the national dataset is rebuilt.

The public build script:

1. reads the project verification files;
2. standardizes analytical geography without erasing source geography;
3. preserves detailed eligibility statuses;
4. derives broad analytical tiers and a conservative core subset;
5. adds row-level provenance;
6. generates integrity diagnostics; and
7. writes deterministic national outputs.

The GitHub Actions workflow runs the same public script when relevant source data or build logic change.

## Public-data boundary

This repository contains only public, non-sensitive research infrastructure. It must not contain private contact information, recruitment records, interview participation status, consent records, interview transcripts, confidential notes, or other human-subjects data.

See `docs/NATIONAL_DATASET_README.md` and `docs/DATA_DICTIONARY.md` for the full architecture and coding rules.
