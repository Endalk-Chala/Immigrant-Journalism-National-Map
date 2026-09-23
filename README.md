# Immigrant Journalism National Map

A national institutional sampling frame of immigrant and immigrant-serving journalism outlets and media products in the United States.

## Current stage

**Phase 1A national first-pass mapping is complete for all 50 states plus the District of Columbia.**

The project identifies and verifies journalism organizations and media products that substantially serve immigrant, refugee, diaspora, language, ethnic, or immigrant-origin communities. The national map is designed as a transparent sampling frame for later qualitative and event-level research on risk ecologies.

The project now has a **reproducible national analytical dataset** generated from the state/DC verification files and is moving into a controlled coding layer for national comparison.

## Repository structure

- `data/candidates/` — broad state-by-state candidate registries; records are provisional at discovery stage
- `data/verification/` — manually reviewed state/DC verification files; authoritative source layer for the national dataset
- `data/analysis/` — generated national analytical files; do not hand-edit
- `data/analysis/audits/` — generated review queues and coding-consistency audits
- `data/external_crosswalks/` — separate relational layer for comparison with CUNY, Medill, or other external outlet datasets
- `data/logs/` — state search logs and national progress tracker
- `docs/METHODOLOGY_NOTE.md` — Phase 1A methodology
- `docs/NATIONAL_DATASET_README.md` — national dataset architecture, external-data boundaries, and reproducibility rules
- `docs/DATA_DICTIONARY.md` — source and derived variable definitions
- `docs/CONTROLLED_VARIABLES_CODEBOOK.md` — controlled analytical variables and coding rules
- `docs/PHASE_1B_METHOD_AND_SAMPLING_MEMO.md` — documented-risk-event layer
- `scripts/build_national_dataset.py` — reproducible national dataset builder and diagnostics
- `scripts/audit_national_dataset.py` — reproducible duplicate/relationship and classification audit
- `scripts/` — public-web collection and supporting scripts
- `.github/workflows/build-national-dataset.yml` — automated national dataset rebuild and audit

## Generated national files

Running:

```bash
python scripts/build_national_dataset.py
python scripts/audit_national_dataset.py
```

creates or refreshes:

- `data/analysis/national_verified_registry_v1.csv` — full verified registry including uncertainty and boundary cases
- `data/analysis/national_core_outlets_v1.csv` — conservative core subset of clearly verified immigrant-serving journalism outlets/products
- `data/analysis/state_summary_v1.csv` — state/DC search-jurisdiction counts by analytical tier
- `data/analysis/eligibility_status_summary_v1.csv` — detailed verification-status counts
- `data/analysis/build_diagnostics_v1.csv` — reproducibility and integrity checks
- `data/analysis/audits/` — relationship-review queues and coding-variation summaries

The controlled coding schema is defined in `data/analysis/national_controlled_coding_v1.csv` and `docs/CONTROLLED_VARIABLES_CODEBOOK.md`. It is relational: controlled variables join back to the verified registry through `outlet_id` rather than replacing source evidence.

Every generated national registry row carries `dataset_origin`, `source_file`, and `source_row_number` provenance fields.

## Geography rule

The analytical dataset deliberately separates:

- `jurisdiction` — the state/DC Phase 1A search frame, derived from the source verification filename
- `state_or_market` — the outlet's source-coded state, region, or market description

State-level national summaries use `jurisdiction`. This prevents multistate market descriptions and earlier header variation from distorting state counts.

## Methodological principle

> **Broad discovery, narrow verification, deeper coding only where analytically useful.**

The database is a **sampling frame, not a census and not a risk score**. Missing public information must not be interpreted as evidence that an institution lacks a resource, capacity, or exposure.

## Controlled analytical layer

The controlled coding layer standardizes a limited set of dimensions for national analysis while preserving all raw Phase 1A evidence. Initial variables include:

- record type
- ownership/governance form
- media format
- language model
- community orientation
- geographic scope
- institutional relationship
- newsroom organizational form
- activity status
- journalism intensity
- core population role
- coding confidence

Relationship identifiers such as `organization_id` will be assigned only after manual review of shared-host, multijurisdiction, and similar-name cases. The project does not automatically merge records merely because they share a website, name, owner, or host.

## How this dataset differs from existing resources

This project does not reproduce or silently merge external databases.

- **CUNY Center for Community Media** is a discovery/comparison resource. Its community-media directories do not define this project's population.
- **Medill State of Local News** is a broader local-news ecosystem resource. This project specifically centers immigrant-serving journalism and preserves hosted, diaspora, language-specific, and transnational institutional forms.
- **U.S. Press Freedom Tracker** is an event-level resource, not an outlet registry. It belongs in the separate risk-event layer.
- **Census ACS** is demographic context. It should be linked through geography for population/language analyses rather than treated as outlet data.

External records do not enter the core outlet registry simply because they appear in CUNY, Medill, or another directory. Future overlap analysis is stored in `data/external_crosswalks/` using explicit source labels, match methods, confidence, and review notes.

## Reproducibility and auditability

Generated analytical files should not be hand-edited. Corrections belong in the state/DC source verification files or in documented reviewed-override tables, after which analytical files are rebuilt.

The public scripts:

1. read the project verification files;
2. standardize analytical geography without erasing source geography;
3. preserve detailed eligibility statuses;
4. derive broad analytical tiers and a conservative core subset;
5. add row-level provenance;
6. generate integrity diagnostics and review queues; and
7. write deterministic national outputs.

The GitHub Actions workflow runs the same public scripts when relevant source data or build logic change.

## Public-data boundary

This repository contains only public, non-sensitive research infrastructure. It must not contain private contact information, recruitment records, interview participation status, consent records, interview transcripts, confidential notes, or other human-subjects data.

See `docs/NATIONAL_DATASET_README.md`, `docs/DATA_DICTIONARY.md`, and `docs/CONTROLLED_VARIABLES_CODEBOOK.md` for the full architecture and coding rules.
