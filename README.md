# Immigrant Journalism National Map

## Research repository for *Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem*

This repository contains the public research infrastructure, reproducible data workflow, institutional sampling frame, enrichment data, and documented risk-event materials developed for the research project:

> **Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem**

The project is being developed as a full manuscript for *Digital Journalism*'s special issue **“Epistemic Disorder: Journalism amid Democratic Decline and Media Insecurity,”** following an invitation to submit a full manuscript after selection of the project abstract for further consideration.

## Authors

**Endalkachew H. Chala, Ph.D.**  
Fellow, Center for an Informed Public  
University of Washington, USA  
Corresponding author: endalk2006@gmail.com

**Tewodros (Teddy) Workneh, Ph.D.**  
Associate Professor of Global Communication  
School of Communication Studies, Kent State University, USA  
Email: tworkneh@kent.edu

---

## Project summary

Immigrant-serving news organizations occupy an increasingly important but unevenly resourced part of the U.S. local news ecosystem. They often serve communities navigating immigration enforcement, multilingual information needs, political uncertainty, platform dependence, and limited access to legal, financial, and safety infrastructure. Yet these outlets are difficult to study systematically because they are dispersed across languages, organizational forms, platforms, and local markets, and because existing media directories, local-news databases, and press-freedom trackers capture different parts of the ecosystem.

This project addresses that gap through a sequential, multi-layered research design. First, it constructs a national institutional sampling frame of immigrant and immigrant-serving journalism outlets across all 50 states and the District of Columbia. Second, it enriches the verified outlet population with publicly available evidence about organizational form, staffing, governance, funding, legal and safety support, network membership, platform dependence, monetization, and audience infrastructure. Third, it builds a separate event-level dataset of publicly documented risks and organizational disruptions, including detention, physical assault, harassment, legal pressure, immigration-enforcement exposure, staffing loss, funding shocks, source-safety concerns, and platform-related disruptions. Sector-wide conditions such as philanthropic contraction or declining platform referral traffic are coded separately as structural exposures rather than automatically attributed to individual outlets.

The study does not collapse these dimensions into a single risk score. Instead, it examines the relationship among **institutional capacity, structural exposure, documented events, organizational responses, and consequences**. The resulting national map and enrichment layers provide the sampling infrastructure for a later qualitative interview phase focused on how immigrant-serving news organizations experience, interpret, and respond to risk. The public repository is designed to make the institutional and event-level components of the study transparent, versioned, and reproducible while keeping future human-subjects data separate and protected.

---

## Project overview

The study examines the institutional conditions under which immigrant-serving journalism operates in the United States and how financial, legal, digital, physical, professional, organizational, platform-related, and transnational risks interact across news organizations.

Rather than beginning with a small convenience sample of journalists or newsrooms, the project first constructs a national institutional sampling frame and then enriches that frame with public evidence about organizational capacity, funding, staffing, legal and safety support, platform dependence, and documented risk events.

The core methodological design separates three forms of evidence:

1. **Institutional capacity** — what an outlet or host publicly appears to have in terms of staffing, governance, funding, legal support, safety infrastructure, network ties, audience infrastructure, and platform dependence.
2. **Documented risk events** — what has happened to an outlet, newsroom, journalist, source community, or organizational operation, such as detention, assault, harassment, staffing disruption, legal pressure, funding loss, or platform restrictions.
3. **Structural exposure** — wider conditions that may shape vulnerability, including platform referral decline, demonetization systems, changes in search or social distribution, philanthropic contraction, immigration-enforcement environments, and other sector-wide pressures.

These layers are analyzed relationally but are **not collapsed into a single risk score**.

The analytical logic is:

> **institutional capacity → exposure → documented event → organizational response → consequence**

This allows the project to examine how resources may mitigate, redistribute, or sometimes generate different forms of risk without assuming that small organizations are necessarily more vulnerable or that larger organizations are necessarily protected.

---

## Research phases

### Phase 1A — National institutional sampling frame

Phase 1A identifies and verifies immigrant and immigrant-serving journalism outlets and media products across all 50 U.S. states and the District of Columbia.

The project distinguishes journalism **for or with immigrant communities** from general-interest journalism that merely reports **about immigration**.

Phase 1A is complete and frozen.

Current Phase 1A totals:

- **531 assessed records**
- **301 core verified outlets/products**
- all 50 states plus the District of Columbia represented

The frozen release is stored at:

`releases/national-immigrant-journalism-map-v1.0-phase1a/`

It includes SHA-256 checksums so that archived files can be verified against later changes.

### Phase 1B — Institutional enrichment

Phase 1B enriches the 301 core outlets using publicly available institutional evidence while leaving the frozen Phase 1A frame unchanged.

The enrichment layer records, where publicly verifiable:

- organizational and legal form;
- parent, host, or fiscal-sponsor relationships;
- staffing and newsroom capacity;
- funding and revenue structure;
- named funders and network affiliations;
- legal-support capacity;
- safety and security support;
- editorial and accountability infrastructure;
- publishing cadence and platform presence;
- platform dependence and platform monetization;
- referral dependence and owned-audience infrastructure;
- publicly documented financial-security conditions;
- public professional contact routes for later recruitment planning.

A central coding rule is:

> **Public silence is not evidence of institutional absence.**

For example, an outlet is not coded as having “no legal support” merely because no attorney appears on its website. Relevant fields distinguish between explicitly disclosed, externally documented, not publicly disclosed, unclear, not searched, and not applicable.

### Parallel risk-event layer

Documented risk events are stored separately from institutional characteristics. This allows multiple events to be linked to the same outlet without permanently labeling the outlet itself as “high risk.”

The risk-event layer includes publicly documented events such as:

- physical assault;
- arrest or detention;
- immigration-enforcement exposure;
- harassment or threats;
- legal pressure;
- cyber or digital-security incidents;
- source or audience safety concerns;
- staffing or organizational-capacity disruption;
- funding loss or financial shock;
- platform restrictions, demonetization, or visibility changes;
- access restrictions;
- other documented organizational disruptions.

Sector-wide conditions such as declining social-media referrals, philanthropic contraction, or platform-policy changes are coded as **structural exposures** rather than automatically assigned to every outlet.

### Phase 2 — Qualitative interviews

The enriched national frame will support purposive interview sampling across meaningful institutional contrasts, including organizational form, staffing capacity, language model, media format, geographic scope, funding structure, platform dependence, legal and safety support, and documented risk exposure.

Interview data will remain separate from the public institutional dataset and will be handled according to applicable IRB and human-subjects requirements.

---

## Current stage

**Phase 1A is complete and frozen. Phase 1B institutional enrichment and the parallel risk-event scan are in progress.**

The project currently has:

- a frozen national Phase 1A sampling frame;
- a reproducible national analytical dataset;
- controlled coding and review layers;
- a 301-record Phase 1B enrichment template;
- evidence-backed enrichment batches;
- a separate risk-event dataset;
- a platform monetization and financial-security coding framework;
- public methodology and reproducibility documentation;
- separate GitHub Actions workflows for Phase 1A and Phase 1B.

---

## Repository structure

- `data/candidates/` — broad state-by-state candidate registries; records are provisional at discovery stage
- `data/verification/` — manually reviewed state/DC verification files; authoritative source layer for the national dataset
- `data/analysis/` — generated national analytical files; do not hand-edit
- `data/analysis/audits/` — generated review queues and coding-consistency audits
- `data/external_crosswalks/` — relational layer for comparison with CUNY, Medill, and other external datasets
- `data/logs/` — state search logs and national progress tracking
- `data/phase1b/institutional_enrichment_v1.csv` — 301-record Phase 1B institutional-enrichment table
- `data/phase1b/enrichment_batches/` — evidence-backed Phase 1B coding batches
- `data/phase1b/risk_events_v1.csv` — outlet-specific, comparison-case, and structural risk-event records
- `docs/METHODOLOGY_NOTE.md` — Phase 1A methodology
- `docs/PHASE_1B_INSTITUTIONAL_ENRICHMENT_CODEBOOK.md` — Phase 1B variables and coding rules
- `docs/PHASE_1B_PLATFORM_FINANCIAL_SECURITY_ADDENDUM.md` — platform monetization, referral dependence, and financial-security coding
- `docs/PHASE_1B_RISK_ECOLOGY_METHODOLOGICAL_NOTE.md` — integrated institutional-capacity/risk-event methodology and reproducibility design
- `docs/NATIONAL_DATASET_README.md` — national dataset architecture and reproducibility rules
- `docs/DATA_DICTIONARY.md` — source and derived variable definitions
- `docs/CONTROLLED_VARIABLES_CODEBOOK.md` — controlled analytical variables and coding rules
- `scripts/build_national_dataset.py` — reproducible national dataset builder and diagnostics
- `scripts/audit_national_dataset.py` — reproducible duplicate/relationship and classification audit
- `scripts/build_phase1b_enrichment_template.py` — creates the Phase 1B enrichment table from the frozen core frame
- `.github/workflows/build-national-dataset.yml` — automated Phase 1A analytical rebuild and audit
- `.github/workflows/build-phase1b-enrichment.yml` — separate Phase 1B template build and validation workflow
- `releases/national-immigrant-journalism-map-v1.0-phase1a/` — frozen Phase 1A release

---

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

The controlled coding schema is relational: controlled variables join back to the verified registry through `outlet_id` rather than replacing source evidence.

Every generated national registry row carries provenance fields identifying its dataset origin, source file, and source row number.

---

## Geography rule

The analytical dataset deliberately separates:

- `jurisdiction` — the state/DC Phase 1A search frame, derived from the source verification filename
- `state_or_market` — the outlet's source-coded state, region, or market description

State-level national summaries use `jurisdiction`. This prevents multistate market descriptions and earlier header variation from distorting state counts.

---

## Methodological principle

> **Broad discovery, narrow verification, deeper coding only where analytically useful.**

The national database is a **sampling frame, not a census and not a risk score**.

The project preserves institutional variation rather than forcing all immigrant-serving outlets into a single organizational category. Important dimensions include nonprofit/commercial/fiscally sponsored/hosted forms, independent/networked operations, small and larger newsrooms, multiple language models, local and transnational reach, and print/digital/radio/television/social/mixed publishing systems.

---

## How this dataset differs from existing resources

This project does not reproduce or silently merge external databases.

- **CUNY Center for Community Media** is used as a discovery and comparison resource; its directories do not define this project's population.
- **Medill State of Local News** provides broader local-news ecosystem context.
- **U.S. Press Freedom Tracker** provides event-level evidence rather than an outlet registry and therefore belongs in the separate risk-event layer.
- **Census ACS** provides demographic context and can be linked through geography rather than treated as outlet-level data.

External records do not enter the core outlet registry simply because they appear in an external directory. Comparison and overlap work is kept in explicit crosswalks with source labels, match methods, confidence levels, and review notes.

---

## Reproducibility and public availability

This repository is intended to make the public-source research workflow transparent and reproducible.

It preserves:

- candidate and verification records;
- the frozen Phase 1A release;
- codebooks and controlled-variable definitions;
- review and adjudication decisions;
- Python scripts used to build analytical datasets;
- GitHub Actions workflows;
- Phase 1B enrichment rules;
- evidence-backed enrichment batches;
- the risk-event dataset;
- source URLs and evidence notes;
- version history through Git commits;
- SHA-256 checksums for the frozen Phase 1A release.

Reproducibility operates at two levels:

### Computational reconstruction

Researchers can use the archived source files, coding files, scripts, and workflows to rebuild the analytical sampling frame.

### Procedural replication

Researchers can apply the published discovery rules, inclusion criteria, source hierarchy, missing-data rules, enrichment codebook, and event-coding protocol to repeat the public-source collection process.

Because news organizations, staff, funding, websites, platform systems, and risk events change over time, a later replication may not produce an identical contemporary dataset. The project therefore treats reproducibility as the transparent reconstruction of a **time-bounded and versioned research process**.

---

## Public-data boundary

This repository contains public, non-sensitive research infrastructure and public-source institutional/event data appropriate for scholarly replication.

It must not contain private recruitment records, interview participation status, consent records, private contact information, interview transcripts, confidential field notes, immigration-status information, or other sensitive human-subject data.

Future interview and human-subject materials will be stored separately and governed by applicable IRB requirements.

---

## Citation and manuscript status

This repository supports an ongoing manuscript project and should not yet be cited as a published *Digital Journalism* article.

**Working manuscript citation:**

Chala, Endalkachew H., and Tewodros (Teddy) Workneh. “Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem.” Manuscript in preparation for *Digital Journalism*, special issue “Epistemic Disorder: Journalism amid Democratic Decline and Media Insecurity.”

For questions about the research repository, contact the corresponding author: **endalk2006@gmail.com**.
