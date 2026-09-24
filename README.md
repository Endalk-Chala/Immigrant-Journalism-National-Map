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

Immigrant-serving journalism occupies a consequential but poorly mapped position in the U.S. information environment. Scholarship on ethnic and immigrant media has long shown that these outlets do more than represent identity: they produce culturally and linguistically specific information, connect communities to local institutions, mediate between homeland and host-country politics, and sustain forms of civic visibility often weakly supplied by mainstream news organizations (Matsaganis, Katz, & Ball-Rokeach, 2010; Lin & Song, 2006; Shumow, 2012, 2014). Recent work further demonstrates that geo-ethnic journalism can shape trust, political information access, and participation precisely because it is embedded in the social worlds of the communities it serves (Zonszein, 2025; Moon et al., 2026).

Yet immigrant-serving journalism remains analytically fragmented across several literatures. Ethnic-media research has often emphasized identity, community formation, and transnationalism; local-news scholarship has focused on institutional decline, market failure, and “news deserts”; platformization research has examined publishers' growing dependencies on large technology firms; and press-freedom datasets typically record discrete incidents rather than the organizational conditions that make harms more or less consequential. These literatures identify important pieces of the problem, but they rarely provide a common institutional frame for asking why similar threats produce different consequences across differently resourced news organizations. Critical work on local news also cautions against treating the mere presence or absence of an outlet as an adequate measure of information provision, while platformization research shows that dependence on distribution infrastructures varies with organizational resources and context (Usher, 2023; Hartley et al., 2023).

This project addresses that gap by treating immigrant-serving news organizations as **epistemic institutions embedded in unequal risk ecologies**. “Epistemic precarity” refers here not simply to unstable employment or financial insecurity, but to the condition in which a newsroom's capacity to produce, verify, distribute, and protect community-relevant knowledge depends on fragile combinations of organizational resources, legal and safety infrastructure, platform access, funding, linguistic capacity, and relationships with the communities it serves. The project therefore asks not only whether immigrant-serving journalists encounter threats, but **how institutional form conditions exposure, response, and consequence**.

Methodologically, the project uses a sequential, multi-layered design. Phase 1A constructs a national institutional sampling frame of immigrant and immigrant-serving journalism outlets across all 50 states and the District of Columbia. Phase 1B enriches the verified outlet population with publicly available evidence about organizational form, staffing, governance, funding, legal and safety support, network membership, platform dependence, monetization, referral structure, and owned-audience infrastructure. A separate risk-event layer records publicly documented incidents and disruptions, including detention, physical assault, harassment, legal pressure, immigration-enforcement exposure, staffing loss, funding shocks, source-safety concerns, and platform-related disruptions. Sector-wide conditions such as philanthropic contraction or declining platform referral traffic are coded separately as structural exposures rather than automatically attributed to individual outlets.

The study does **not** collapse these dimensions into a composite risk score. Instead, it preserves the relationship among:

> **institutional capacity → structural exposure → documented event → organizational response → consequence**

This design makes it possible to examine how resources may buffer some harms, redistribute others, or create new dependencies. It also avoids assuming that small outlets are necessarily more vulnerable, that larger outlets are necessarily more secure, or that absence of a publicly documented incident is evidence of safety.

The resulting national map and enrichment layers provide the sampling infrastructure for a later qualitative interview phase focused on how immigrant-serving news organizations experience, interpret, and respond to risk. The public repository is designed to make the institutional and event-level components of the study transparent, versioned, and reproducible while keeping future human-subjects data separate and protected.

---

## Research questions guiding the project

The broader study is organized around four linked questions:

1. **What is the institutional landscape of immigrant-serving journalism in the United States?**
2. **How are financial, legal, digital, physical, professional, organizational, platform-related, and transnational risks distributed across different kinds of immigrant-serving news organizations?**
3. **How do organizational resources and dependencies shape whether a threat becomes a manageable disruption, a chilling constraint, or an existential risk?**
4. **How do journalists and news organizations themselves interpret, negotiate, and respond to these interacting risks?**

The first three questions structure the public mapping and enrichment work in this repository. The fourth will be addressed primarily through the later qualitative interview phase.

---

## Conceptual contribution

The project brings together four bodies of scholarship that are often treated separately:

- **Ethnic and immigrant media studies**, which show how community media support identity, local information needs, representation, and transnational connection (Matsaganis et al., 2010; Lin & Song, 2006; Shumow, 2012, 2014).
- **Local-news and information-ecosystem scholarship**, which treats journalism as institutional infrastructure while also warning against overly simple “news desert” measures that ignore place, power, and uneven information provision (Usher, 2023; Barclay et al., 2025).
- **Platformization research**, which emphasizes that news organizations experience digital platforms through unequal configurations of autonomy and dependence shaped by organizational resources and market context (Hartley et al., 2023).
- **Journalism-precarity and safety research**, which demonstrates that vulnerability is shaped not only by discrete threats but by institutional, labor, and contextual conditions that affect journalists' capacity to absorb and respond to harm.

The project's intervention is to operationalize these insights at the **organizational level**. Instead of treating risk as an individual journalist characteristic or as a count of incidents, it examines how risk is produced relationally through the interaction of organizational capacity, external exposure, and institutional response.

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

## Selected scholarly references

Barclay, S., Barnett, S., Moore, M., & Townend, J. (2025). Local news as political institution and the repercussions of “news deserts”: A qualitative study of seven UK local areas. *Journalism, 26*(9). https://doi.org/10.1177/14648849241272255

Hartley, J. M., Petre, C., Bengtsson, M., & Kammer, A. (2023). Autonomies and dependencies: Shifting configurations of power in the platformization of news. *Digital Journalism, 11*(8), 1375–1390. https://doi.org/10.1080/21670811.2023.2257759

Lin, W.-Y., & Song, H. (2006). Geo-ethnic storytelling: An examination of ethnic media content in contemporary immigrant communities. *Journalism, 7*(3), 362–388. https://doi.org/10.1177/1464884906065518

Matsaganis, M. D., Katz, V. S., & Ball-Rokeach, S. J. (2010). *Understanding Ethnic Media: Producers, Consumers, and Societies*. SAGE.

Moon, Y. E., Hays, C., Xu, Z., Roschke, K., & Kwon, K. H. (2026). Contextualizing trust: Geo-ethnic media, relatable storytelling, and audience trust. *Journalism & Mass Communication Quarterly*. https://doi.org/10.1177/10776990261416899

Shumow, M. (2012). Immigrant journalism, ideology and the production of transnational media spaces. *Media, Culture & Society, 34*(7). https://doi.org/10.1177/0163443712452770

Shumow, M. (2014). Media production in a transnational setting: Three models of immigrant journalism. *Journalism, 15*(8). https://doi.org/10.1177/1464884914521581

Usher, N. (2023). The real problems with the problem of news deserts: Toward rooting place, precision, and positionality in scholarship on local news and democracy. *Political Communication, 40*(2), 238–253. https://doi.org/10.1080/10584609.2023.2175399

Zonszein, S. (2025). Turn on, tune in, turn out: Ethnic radio and immigrants' political engagement. *American Journal of Political Science*. https://doi.org/10.1111/ajps.12911

---

## Citation and manuscript status

This repository supports an ongoing manuscript project and should not yet be cited as a published *Digital Journalism* article.

**Working manuscript citation:**

Chala, Endalkachew H., and Tewodros (Teddy) Workneh. “Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem.” Manuscript in preparation for *Digital Journalism*, special issue “Epistemic Disorder: Journalism amid Democratic Decline and Media Insecurity.”

For questions about the research repository, contact the corresponding author: **endalk2006@gmail.com**.
