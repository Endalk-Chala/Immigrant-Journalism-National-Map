# Immigrant Journalism National Map

## Research repository for *Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem*

This repository contains the public research infrastructure for a manuscript in preparation for *Digital Journalism*'s special issue **“Epistemic Disorder: Journalism amid Democratic Decline and Media Insecurity.”**

### Authors

**Endalkachew H. Chala, Ph.D.**  
Fellow, Center for an Informed Public, University of Washington, USA  
Corresponding author: endalk2006@gmail.com

**Tewodros (Teddy) Workneh, Ph.D.**  
Associate Professor of Global Communication, School of Communication Studies, Kent State University, USA  
Email: tworkneh@kent.edu

---

## What this project asks

Immigrant-serving journalism is important to the U.S. information environment but remains difficult to study as a national institutional field. These outlets operate across languages, ownership forms, platforms, local markets, and transnational communities. Existing scholarship has examined ethnic and immigrant media, local news, platform dependence, and journalist safety, but these literatures do not by themselves provide a national organizational frame for comparing how differently resourced outlets encounter and respond to risk.

The project therefore asks a simple but consequential question:

> **How do the institutional conditions of immigrant-serving news organizations shape their exposure to risk, their capacity to respond, and their ability to sustain community-relevant knowledge?**

We use **epistemic precarity** to describe the condition in which the production, verification, distribution, or protection of community-relevant knowledge depends on fragile or uneven organizational resources, legal and safety support, funding, platform access, linguistic capacity, and community relationships.

---

## Intellectual foundations

Research on ethnic and immigrant media shows that these outlets do more than represent identity. They provide culturally and linguistically specific information, connect communities to public institutions, and mediate local and transnational forms of civic life (Lin & Song, 2006; Matsaganis, Katz, & Ball-Rokeach, 2010; Shumow, 2012, 2014).

Journalist-safety scholarship provides a second foundation. Holton et al. (2021) show that online harassment can produce fatigue, anxiety, and professional withdrawal while news organizations often leave journalists to manage these harms individually. Westlund, Krøvel, and Orgeret (2022) broaden the analysis through **Newsafety**, treating safety as a sociotechnical problem involving infrastructures, practices, and consequences. Slavtcheva-Petkova et al. (2023) formalize journalist safety as physical, psychological, digital, and financial, with risk operating across societal, organizational, and individual levels. Bélair-Gagnon et al. (2024) then frame attacks on journalism as an **occupational hazard**, making the case for institutional rather than purely individual responses. This line of work directs attention to the organizational and infrastructural conditions that shape exposure, coping, and consequence.

This project extends that trajectory through **risk ecology**. Chala's earlier study of journalist exposure in Ethiopia argues that risk is relational rather than additive: political environment, professional orientation, visibility, organizational mediation, and platform dynamics interact to shape exposure and survival. The present project changes the unit and scale of analysis. It asks how **organizationally heterogeneous immigrant-serving news outlets occupy different risk ecologies within the same national media system**.

The core analytical relationship is:

> **institutional capacity → structural exposure → documented event → organizational response → consequence**

The study does **not** combine these dimensions into a single risk score.

---

## How the research is organized

### 1. Build the national map

We first identify and verify immigrant and immigrant-serving journalism outlets across all 50 states and the District of Columbia. The map distinguishes journalism **for or with immigrant communities** from general-interest journalism that only reports **about immigration**.

The completed national frame contains **531 assessed records**, including **301 core verified outlets or journalism products** across **51 jurisdictions**. These figures are documented in the project completion report and frozen release. 

### 2. Enrich the verified outlets

We then collect public evidence about institutional conditions such as organizational form, staffing, governance, funding, legal and safety support, professional networks, platform dependence, and owned-audience infrastructure.

A central rule is:

> **Public silence is not evidence of institutional absence.**

If an outlet does not publicly disclose legal support, for example, it is coded as **not publicly disclosed**, not as **no legal support**.

### 3. Document risk events separately

We maintain a separate event-level dataset for publicly documented harms and disruptions, including detention, physical assault, harassment, legal pressure, immigration-enforcement exposure, staffing disruption, source-safety concerns, funding shocks, access restrictions, and platform-related disruptions.

Sector-wide conditions, such as declining referral traffic or philanthropic contraction, are treated as **structural exposures** unless there is outlet-specific evidence of impact.

### 4. Use the map for qualitative interviews

The national map and enrichment data will support purposive sampling for interviews across meaningful institutional contrasts. Interview and other human-subject data will remain separate from this public repository and will be handled under applicable IRB requirements.

---

## What is distinctive about this project

The project brings together four areas that are usually studied separately: immigrant and ethnic media, local-news institutions, platform dependence, and journalist safety.

Its main contribution is organizational. Rather than asking only whether journalists face threats, the study asks **why similar threats can produce different consequences across differently resourced news organizations**.

That distinction matters because safety is not only an individual condition. It can affect whether a newsroom can continue reporting, protect sources, maintain multilingual coverage, keep staff, withstand legal pressure, preserve audience access, or sustain publication.

This is where **epistemic precarity** becomes analytically useful: risk matters not only because it harms journalists, but because it can alter what communities are able to know.

---

## Current status

The national mapping stage is complete and frozen. Institutional enrichment and the parallel risk-event scan are ongoing.

The frozen national release is stored in:

`releases/national-immigrant-journalism-map-v1.0-phase1a/`

Key methodological documentation is in:

- `docs/PHASE_1A_COMPLETION_REPORT.md`
- `docs/PHASE_1B_INSTITUTIONAL_ENRICHMENT_CODEBOOK.md`
- `docs/PHASE_1B_RISK_ECOLOGY_METHODOLOGICAL_NOTE.md`
- `docs/JOURNALIST_SAFETY_AND_RISK_ECOLOGY_FRAMEWORK.md`
- `docs/NATIONAL_DATASET_README.md`

Key data locations are:

- `data/verification/` — reviewed state/DC source files
- `data/analysis/` — generated national analytical files
- `data/phase1b/institutional_enrichment_v1.csv` — institutional enrichment table
- `data/phase1b/enrichment_batches/` — evidence-backed enrichment batches
- `data/phase1b/risk_events_v1.csv` — documented risk-event records

---

## Reproducibility and data quality

This repository is designed as a versioned, auditable research record. Generated analytical files are rebuilt from source and review files rather than hand-edited. The project preserves source URLs, evidence notes, coding rules, review decisions, scripts, workflow files, Git history, and SHA-256 checksums for the frozen national release.

The public dataset is a **sampling frame, not a census**. Uncertainty is retained when evidence is weak, and missing disclosure is not converted into a negative finding.

Public-facing counts and claims in this README are cross-checked against the repository's completion report and source documentation. More detailed methodological and coding decisions are kept in the `docs/` directory rather than repeated here.

---

## Selected references

Bélair-Gagnon, V., Searles, K., Vraga, E., Holton, A. E., & Tandoc, E. C. Jr. (2024). Attacks on journalism as an occupational hazard. *International Journal of Communication, 18*, 4603–4622.

Chala, E. H. (2026). From multidimensional safety to risk ecologies: A four-coordinate analysis of journalist exposure in Ethiopia, 1992–2024. *Journalism Practice*. https://doi.org/10.1080/17512786.2026.2637127

Holton, A. E., Bélair-Gagnon, V., Bossio, D., & Molyneux, L. (2021). “Not Their Fault, but Their Problem”: Organizational responses to the online harassment of journalists. *Journalism Practice, 17*(4), 859–874. https://doi.org/10.1080/17512786.2021.1946417

Lin, W.-Y., & Song, H. (2006). Geo-ethnic storytelling: An examination of ethnic media content in contemporary immigrant communities. *Journalism, 7*(3), 362–388. https://doi.org/10.1177/1464884906065518

Matsaganis, M. D., Katz, V. S., & Ball-Rokeach, S. J. (2010). *Understanding Ethnic Media: Producers, Consumers, and Societies*. SAGE.

Shumow, M. (2012). Immigrant journalism, ideology and the production of transnational media spaces. *Media, Culture & Society, 34*(7).

Shumow, M. (2014). Media production in a transnational setting: Three models of immigrant journalism. *Journalism, 15*(8).

Slavtcheva-Petkova, V., Ramaprasad, J., Springer, N., Hughes, S., Hanitzsch, T., Hamada, B., Hoxha, A., & Steindl, N. (2023). Conceptualizing journalists' safety around the globe. *Digital Journalism, 11*(7), 1211–1229. https://doi.org/10.1080/21670811.2022.2162429

Westlund, O., Krøvel, R., & Orgeret, K. S. (2022). Newsafety: Infrastructures, practices and consequences. *Journalism Practice, 16*(9), 1811–1828. https://doi.org/10.1080/17512786.2022.2130818

---

## Manuscript status

This repository supports an ongoing manuscript and should not yet be cited as a published *Digital Journalism* article.

**Working manuscript citation:**

Chala, Endalkachew H., and Tewodros (Teddy) Workneh. “Epistemic Precarity: Risk Ecologies of Immigrant Journalism in the Emerging U.S. Local News Ecosystem.” Manuscript in preparation for *Digital Journalism*, special issue “Epistemic Disorder: Journalism amid Democratic Decline and Media Insecurity.”
