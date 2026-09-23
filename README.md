# Immigrant Journalism National Map

A national institutional sampling frame of immigrant and immigrant-serving journalism outlets and media products in the United States.

## Current stage

**Phase 1A national first-pass mapping is complete for all 50 states plus the District of Columbia.**

The project identifies and verifies journalism organizations and media products that substantially serve immigrant, refugee, diaspora, language, ethnic, or immigrant-origin communities. The national map is designed as a transparent sampling frame for later qualitative and event-level research on risk ecologies.

The project is now moving from state-by-state discovery to a **reproducible national analytical dataset**.

## Repository structure

- `data/candidates/` — broad state-by-state candidate registries; records are provisional at discovery stage
- `data/verification/` — manually reviewed state/DC verification files; source layer for the national dataset
- `data/analysis/` — generated national analytical files; do not hand-edit
- `data/logs/` — state search logs and national progress tracker
- `docs/METHODOLOGY_NOTE.md` — Phase 1A methodology
- `docs/NATIONAL_DATASET_README.md` — national dataset architecture, external-data boundaries, and reproducibility rules
- `docs/DATA_DICTIONARY.md` — source and derived variable definitions
- `docs/PHASE_1B_METHOD_AND_SAMPLING_MEMO.md` — documented-risk-event layer
- `scripts/build_national_dataset.py` — reproducible national dataset builder
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
- `data/analysis/state_summary_v1.csv` — state/DC counts by analytical tier
- `data/analysis/eligibility_status_summary_v1.csv` — detailed verification-status counts

Every generated national row carries `source_file` and `source_row_number` provenance fields.

## Methodological principle

> **Broad discovery, narrow verification, deeper coding only where analytically useful.**

The database is a **sampling frame, not a census and not a risk score**. Missing public information must not be interpreted as evidence that an institution lacks a resource, capacity, or exposure.

## How this dataset differs from existing resources

This project does not reproduce or silently merge external databases.

- **CUNY Center for Community Media** is used as a possible discovery/comparison resource. Its community-media directories do not define this project's population.
- **Medill State of Local News** is a broader local-news ecosystem resource. This project specifically centers immigrant-serving journalism and preserves hosted, diaspora, language-specific, and transnational institutional forms.
- **U.S. Press Freedom Tracker** is an event-level resource, not an outlet registry. It belongs in the separate Phase 1B risk-event layer.
- **Census ACS** is demographic context. It should be linked through geography for population/language analyses rather than treated as outlet data.

External records must pass the project's own discovery and verification workflow before they can enter the core outlet registry. Future crosswalks to CUNY/Medill and enrichment with ACS/Press Freedom Tracker data should remain in separate relational tables.

See `docs/NATIONAL_DATASET_README.md` for the full boundary rules.

## Public-data boundary

This repository contains only public, non-sensitive research infrastructure. It must not contain private contact information, recruitment records, interview participation status, consent records, interview transcripts, confidential notes, or other human-subjects data.

## Reproducibility rule

Generated analytical files should not be hand-edited. Corrections belong in the state/DC source verification files, after which the national dataset should be rebuilt. This keeps the analytical dataset fully traceable to public verification evidence and documented classification rules.
