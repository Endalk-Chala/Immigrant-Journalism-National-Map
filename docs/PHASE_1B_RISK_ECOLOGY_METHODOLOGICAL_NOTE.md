# Phase 1B Methodological Note: Institutional Capacity, Risk Events, and Reproducibility

## Project
**A National Institutional Map of Immigrant Journalism and Its Risk Ecologies in the United States**

## Purpose

This note documents the methodological transition from the frozen Phase 1A national sampling frame to Phase 1B institutional enrichment and risk-event collection. It is designed to support the *Digital Journalism* manuscript, IRB documentation, and public reproducibility of the research workflow.

The central methodological principle is to keep three analytically distinct forms of evidence separate:

1. **Institutional capacity** — what an outlet or host publicly appears to have in terms of staffing, governance, funding, legal support, safety infrastructure, network ties, audience infrastructure, and platform dependence.
2. **Documented risk events** — what has happened to an outlet, newsroom, journalist, source community, or organizational operation, such as detention, assault, harassment, staffing disruption, legal threats, funding loss, or platform restrictions.
3. **Structural exposure** — wider conditions that may shape organizational vulnerability, including platform referral decline, demonetization systems, changes in search or social distribution, philanthropic contraction, immigration-enforcement environments, and other sector-wide pressures.

These layers are linked analytically but are not collapsed into a single risk score.

---

## 1. Phase 1A as the frozen sampling frame

Phase 1A created a national institutional sampling frame covering all 50 U.S. states and the District of Columbia. Candidate outlets were discovered through multiple directories, professional associations, community-media sources, targeted language/community searches, outlet websites, and credible secondary sources. Each candidate was screened using a common inclusion rule: the outlet had to be U.S.-based or substantially U.S.-serving, produce sustained journalism or public-affairs content, and substantially serve immigrant, refugee, diaspora, language, ethnic, or immigrant-origin communities.

The Phase 1A frame contains 531 assessed records, of which 301 were classified as core verified outlets or journalism products. The Phase 1A release is frozen and is not modified by Phase 1B enrichment. This separation ensures that later discoveries about staffing, funding, safety, or risk do not retroactively alter the original sampling frame.

Phase 1A is therefore the population from which Phase 1B enrichment and later purposive interview sampling proceed.

---

## 2. Why Phase 1B precedes interview sampling

The study does not select interviewees directly from the national map based only on convenience or visibility. Instead, Phase 1B first enriches the 301 core outlets with publicly verifiable institutional information. This allows the later interview sample to capture meaningful organizational contrasts, such as:

- nonprofit versus commercial;
- independent versus hosted or parent-supported;
- very small versus larger newsroom capacity;
- local versus statewide, national, or transnational reach;
- English-dominant, bilingual, multilingual, or non-English operations;
- print, digital, radio, television, newsletter, or mixed-platform outlets;
- diversified versus concentrated funding structures;
- publicly visible versus non-visible legal and safety support;
- strong owned-audience infrastructure versus heavier platform dependence;
- outlets with documented risk events versus outlets without publicly documented incidents.

This sequencing supports purposive, theoretically informed selection for Phase 2 interviews.

---

## 3. Institutional enrichment layer

Phase 1B creates a separate outlet-level dataset joined to the frozen Phase 1A frame through `outlet_id`.

The enrichment layer records publicly verifiable information on:

### Organizational structure
- founding year and institutional history;
- legal organizational form;
- parent, host, or fiscal sponsor;
- ownership/governance structure;
- public board/governance information.

### Staffing and newsroom capacity
- publicly listed staff count;
- staff-size band;
- editorial leadership;
- visible employment model, where disclosed;
- staff-directory source and evidence basis.

### Financial capacity
- revenue model;
- publicly disclosed revenue sources;
- annual revenue where verifiable;
- revenue band;
- named funders;
- grant dependence where public evidence supports classification;
- revenue concentration where public evidence supports classification.

### Institutional support
- journalism/network memberships;
- collaborative partnerships;
- parent/host resource relationships;
- publicly visible legal support;
- publicly visible safety/security support.

### Editorial and accountability infrastructure
- corrections policies;
- ethics policies;
- editorial policies;
- privacy/source-protection policies where public.

### Distribution and platform infrastructure
- publishing cadence;
- platform presence;
- platform dependence;
- direct or indirect platform monetization;
- referral dependence;
- owned-audience channels such as newsletters, SMS, WhatsApp, print, direct web, radio, television, apps, and events;
- publicly documented exposure to demonetization, algorithmic visibility loss, referral decline, or platform-policy changes.

### Recruitment readiness
- public organizational contact routes;
- publicly listed professional/editorial contacts;
- source URLs supporting professional roles.

No private personal information is required for Phase 1B institutional enrichment.

---

## 4. Missingness and non-disclosure

A central rule is:

> **Public silence is not evidence of institutional absence.**

For fields such as legal support, safety support, funding structure, or platform monetization, the study distinguishes among:

- `explicitly_disclosed`
- `externally_documented`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`
- `not_applicable`

For example, an outlet is not coded as having "no legal team" simply because no lawyer appears on its website. Instead, the field is coded `not_publicly_disclosed` if relevant public sources were searched and no disclosure was found.

This rule is intended to reduce false negative inferences from uneven website transparency.

---

## 5. Source hierarchy

Phase 1B uses a consistent evidence hierarchy:

1. outlet or organization website;
2. parent or host organization website;
3. annual reports, IRS filings, audited financials, and official governance documents;
4. funder or grant-maker announcements;
5. official membership/network directories;
6. journalism associations and professional organizations;
7. press-freedom organizations and incident trackers;
8. credible secondary journalism or industry reporting;
9. other public secondary sources used cautiously.

Each substantive coded value should preserve, where applicable:

- source URL;
- source type;
- evidence date;
- date checked;
- short evidence note;
- coding confidence.

---

## 6. Risk-event layer

Documented risk events are stored separately from outlet-level institutional characteristics. This prevents an event from becoming a permanent label attached to an organization and allows multiple events per outlet.

The risk-event table includes fields such as:

- `event_id`
- `outlet_id`
- `outlet_name`
- `event_date_start`
- `event_date_end`
- `jurisdiction`
- `event_scope`
- `risk_domain`
- `risk_subtype`
- `event_status`
- `event_summary`
- `actor_or_source_of_risk`
- primary and secondary evidence URLs;
- source type;
- coding confidence;
- documented consequence;
- financial consequence where publicly documented;
- organizational response.

Risk domains may include:

- physical safety;
- arrest/detention or immigration-enforcement exposure;
- harassment or threats;
- legal pressure;
- cyber/digital security;
- source or audience safety;
- staffing/capacity disruption;
- financial-security shock;
- platform-governance or monetization shock;
- access restriction;
- other documented organizational disruptions.

---

## 7. Outlet-specific events versus structural exposure

The study distinguishes outlet-specific events from sector-wide conditions.

An assault, detention, lawsuit, layoff, staffing collapse, or demonetization event involving a specific outlet can be linked to that outlet through `outlet_id` when evidence supports the connection.

By contrast, sector-wide developments such as declining Facebook referral traffic, philanthropic contraction, or changes in platform monetization policies are coded as structural exposures. These are **not** automatically assigned to every outlet.

An outlet is treated as exposed to a structural condition only when the institutional enrichment layer provides evidence that the outlet depends on the relevant funding, referral, distribution, or platform system.

This prevents ecological inference from sector-level trends to individual organizations.

---

## 8. Platform monetization and financial security

Financial security is treated as broader than annual revenue.

The study distinguishes:

- direct platform monetization;
- indirect platform-related revenue;
- platform referral dependence;
- search/social distribution dependence;
- owned-audience infrastructure;
- grant dependence;
- donor/funder concentration;
- advertising dependence;
- government-advertising dependence where applicable;
- documented funding losses;
- demonetization or platform-policy restrictions;
- algorithmic visibility and referral changes.

Platform presence is not treated as equivalent to platform dependence, and platform dependence is not treated as equivalent to platform monetization.

For example, an outlet may use WhatsApp heavily for distribution without earning platform revenue, or may receive YouTube advertising revenue while remaining primarily grant-funded.

---

## 9. No composite risk score

The project does not convert staffing, revenue, legal support, documented incidents, or platform dependence into a single numerical risk score.

A small outlet is not assumed to be high risk, and a larger or better-funded outlet is not assumed to be protected from harm. Instead, the design preserves the empirical relationship among:

**institutional capacity → exposure → documented event → organizational response → consequence**

This allows the study to examine how resources may redistribute, mitigate, or sometimes create different forms of risk without presupposing a linear relationship between organizational size and vulnerability.

---

## 10. Comparison cases

The risk-event scan may identify relevant immigrant, ethnic, language, independent, or community journalists/outlets that were not present in the frozen Phase 1A core frame.

These are retained as `comparison_case = yes` rather than being retroactively inserted into Phase 1A. If a later crosswalk establishes that a comparison case corresponds to an existing Phase 1A organization, the relationship can be documented without altering the frozen release.

This preserves temporal integrity of the original sampling frame while allowing the risk-event corpus to capture relevant events beyond it.

---

## 11. Reproducibility and public availability

The research repository is public and is designed to support reconstruction of the data workflow.

The repository preserves:

- candidate and verification records;
- the frozen Phase 1A release;
- data dictionaries and controlled-variable codebooks;
- relationship-review and community-orientation decisions;
- scripts used to build and validate analytical datasets;
- GitHub Actions workflows;
- Phase 1B enrichment codebooks;
- platform/financial-security coding rules;
- the Phase 1B enrichment template;
- evidence-backed enrichment batches;
- the risk-event table;
- source URLs and evidence notes;
- version history through Git commits.

The frozen Phase 1A release includes SHA-256 checksums so researchers can verify that archived files have not changed.

Phase 1B is versioned separately from Phase 1A. New enrichment records are added in evidence-backed batches rather than modifying the frozen sampling-frame release.

A researcher can therefore reproduce the study at two levels:

### Computational reconstruction
Using the archived Phase 1A files, controlled coding files, Python scripts, and GitHub Actions workflow to rebuild the analytical frame.

### Procedural replication
Using the published inclusion criteria, source hierarchy, enrichment codebook, missing-data rules, and event-coding protocol to repeat the public-source collection process.

An independent replication may not yield an identical set of current webpages or institutional characteristics because organizations change, staff move, websites disappear, funding changes, and new incidents occur. The project therefore treats reproducibility as **transparent reconstruction of a time-bounded research process**, rather than an expectation that a dynamic media ecosystem will remain unchanged.

---

## 12. Public versus restricted research data

The public repository should contain institutional and event information that is already publicly available and appropriate for scholarly replication.

Public data may include:

- outlet-level institutional characteristics;
- organizational contacts already publicly listed in professional roles;
- public funding and governance information;
- publicly reported incidents;
- source URLs;
- coding decisions and confidence.

Future interview data should remain separate from the public institutional dataset. Interview transcripts, consent records, private contact information, immigration-status information, or other sensitive human-subject data should be handled according to IRB requirements and should not be included in the public replication dataset unless explicitly permitted by consent and ethics review.

---

## 13. Transition to Phase 2 interviews

The Phase 1A sampling frame and Phase 1B enrichment layer jointly provide the basis for purposive interview sampling.

Interviewees can be selected to capture contrasts in:

- organizational form;
- newsroom size;
- language model;
- media format;
- geographic scope;
- funding model;
- platform dependence;
- legal/safety support;
- documented risk exposure;
- organizational responses to risk.

The interview phase can then investigate dimensions that public sources cannot establish reliably, including informal safety practices, experienced threats, legal chilling, source-protection decisions, immigration-related concerns, platform dependence, self-censorship, financial insecurity, internal decision-making, and organizational adaptation.

---

## 14. Core methodological contribution

The methodological contribution is not simply a directory of immigrant-serving news organizations or a list of press-freedom incidents. It is the linkage of a verified institutional sampling frame with separately coded organizational-capacity and risk-event layers.

This design makes it possible to study risk ecologies relationally: not only whether journalists experience threats, but how institutional form, financial structure, platform dependence, legal and safety resources, and organizational support shape the distribution and management of those risks across the immigrant-journalism ecosystem.
