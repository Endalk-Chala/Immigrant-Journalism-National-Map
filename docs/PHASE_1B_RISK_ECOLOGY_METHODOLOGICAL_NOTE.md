# Phase 1B Methodological Note: Institutional Capacity, Support Infrastructure, Risk Events, and Reproducibility

## Project
**A National Institutional Map of Immigrant Journalism and Its Risk Ecologies in the United States**

## Purpose

This note documents the methodological transition from the frozen Phase 1A national sampling frame to Phase 1B institutional enrichment, external support-infrastructure mapping, and risk-event collection. It is designed to support the *Digital Journalism* manuscript, IRB documentation, and public reproducibility of the research workflow.

The study uses four linked but analytically distinct data layers:

1. **National sampling frame** — the independently constructed and verified population of immigrant-serving journalism outlets/products from which later enrichment and purposive interview sampling proceed.
2. **Internal institutional capacity** — publicly documented organizational characteristics such as staffing, governance, funding, legal and safety resources, audience infrastructure, and platform dependence.
3. **External support infrastructure** — documented relationships with professional networks, fiscal sponsors, field-building institutions, legal and safety organizations, funders, training programs, collaboratives, and other organizations that may provide capacities outside the newsroom itself.
4. **Risk events and structural exposure** — documented events, anticipatory responses, and wider political, legal, physical, economic, informational, platform, funding, or enforcement conditions that may affect outlets and journalists.

These layers are linked analytically but are not collapsed into a single risk score. The design allows the study to examine both **internal capacity** and **networked or distributed capacity** when assessing how organizations encounter, respond to, and absorb risk.

---

## 1. Phase 1A as the frozen sampling frame

Phase 1A created a national institutional sampling frame covering all 50 U.S. states and the District of Columbia. Candidate outlets were discovered through multiple directories, professional associations, community-media sources, targeted language/community searches, outlet websites, and credible secondary sources. Each candidate was screened using a common inclusion rule: the outlet had to be U.S.-based or substantially U.S.-serving, produce sustained journalism or public-affairs content, and substantially serve immigrant, refugee, diaspora, language, ethnic, or immigrant-origin communities.

The Phase 1A frame contains 531 assessed records, of which 301 were classified as core verified outlets or journalism products. The Phase 1A release is frozen and is not modified by Phase 1B enrichment. This separation ensures that later discoveries about staffing, funding, support networks, safety, or risk do not retroactively alter the original sampling frame.

Phase 1A is therefore the population from which Phase 1B enrichment and later purposive interview sampling proceed.

---

## 2. Why enrichment precedes interview sampling

The study does not select interviewees directly from the national map based only on convenience or visibility. Public-source enrichment first documents meaningful organizational and infrastructural differences across the 301 core outlets. This allows later interview sampling to capture contrasts such as:

- nonprofit versus commercial;
- independent versus hosted, fiscally sponsored, or parent-supported;
- very small versus larger newsroom capacity;
- local versus statewide, national, or transnational reach;
- English-dominant, bilingual, multilingual, or non-English operations;
- print, digital, radio, television, newsletter, or mixed-platform outlets;
- diversified versus concentrated funding structures;
- strong owned-audience infrastructure versus heavier platform dependence;
- internally resourced versus externally networked legal, safety, technical, or operational capacity;
- highly networked versus relatively institutionally isolated outlets;
- outlets with documented risk events, anticipatory adaptations, or only structural exposure;
- outlets without publicly documented incidents, retained as analytically important comparison cases.

This sequencing supports purposive, theoretically informed selection for the interview phase.

---

## 3. Internal institutional-enrichment layer

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

### Institutional support summaries
- journalism/network memberships;
- collaborative partnerships;
- parent/host resource relationships;
- publicly visible legal support;
- publicly visible safety/security support.

These outlet-level fields provide summary indicators. Detailed many-to-many relationships with external support organizations are stored in a separate support-infrastructure table described below.

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

No private personal information is required for this public institutional-enrichment layer.

---

## 4. External support-infrastructure layer

The study separately maps external relationships that may provide organizational capacity outside the newsroom itself. This layer is motivated by the working proposition that small immigrant-serving news organizations may rely on professional and field-building organizations for capacities that larger newsrooms have historically maintained internally.

Relevant relationships may include professional membership networks, fiscal sponsors, field-building institutions, legal-support organizations, journalist-safety organizations, funding and grant-making organizations, technology or cybersecurity programs, journalism collaboratives, university or training partners, and identity- or community-media networks.

Examples include, where evidence supports an outlet-specific relationship, organizations such as the Institute for Nonprofit News, LION Publishers, Tiny News Collective, the Center for Community Media at CUNY/Newmark J-School, the Reporters Committee for Freedom of the Press, Lawyers for Reporters, the Committee to Protect Journalists, the International Women's Media Foundation, fiscal sponsors, local journalism collaboratives, and other support institutions.

The unit of analysis is **one outlet-to-support-organization relationship**, stored in `data/phase1b/support_infrastructure_relationships_v1.csv`.

The coding distinguishes three levels:

1. **Affiliation or connection** — whether a documented relationship exists;
2. **Potentially available support** — what resources or services the organization makes available through that relationship;
3. **Documented mobilization or use** — whether public evidence shows that the outlet actually accessed or used those resources.

Possible support functions include legal assistance, media-liability insurance, physical safety, digital security, online-harassment support, emergency assistance, fiscal sponsorship, technology, funding, business or operational support, training, peer support, research or field building, audience/distribution assistance, and policy or advocacy support.

Two distinctions are methodologically essential. First, **directory presence is not membership**: appearing in an external directory may help validate an outlet's existence but does not establish participation in that institution's programs. Second, **membership is not use**: formal membership may establish eligibility or access to resources, but actual mobilization requires separate evidence.

Public-source data may establish affiliation and potentially available support. Actual use may be undocumented publicly and can therefore become a question for the interview phase. Absence of public evidence of support use is not coded as evidence that no support was used.

This layer permits the study to examine whether external relationships function as forms of **distributed organizational capacity** and whether network embeddedness appears to buffer, mediate, or otherwise shape organizational responses to risk.

---

## 5. Missingness and non-disclosure

A central rule is:

> **Public silence is not evidence of institutional absence.**

For fields such as legal support, safety support, funding structure, platform monetization, or external support use, the study distinguishes among:

- `explicitly_disclosed`
- `externally_documented`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`
- `not_applicable`

For example, an outlet is not coded as having "no legal team" simply because no lawyer appears on its website. Similarly, lack of public evidence that an outlet used a professional network's legal or safety service does not establish that the resource was never used.

This rule is intended to reduce false negative inferences from uneven public disclosure.

---

## 6. Source hierarchy

Phase 1B uses a consistent evidence hierarchy:

1. outlet or organization website;
2. parent, host, fiscal sponsor, or support-organization website;
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

## 7. Risk-event and structural-exposure layer

Documented risk events are stored separately from outlet-level institutional characteristics. This prevents an event from becoming a permanent label attached to an organization and allows multiple events or related episodes per outlet.

The reconciled event schema distinguishes:

- `documented_event`
- `anticipatory_response`
- `structural_exposure`
- `legal_or_administrative_outcome`

The canonical top-level risk domains are:

- `legal`
- `physical`
- `political`
- `economic`
- `informational`

More specific phenomena such as immigration enforcement, online harassment, platform action, funding loss, staffing disruption, or source intimidation are represented through separate fields for mechanism, actor, target, coercion type, consequence, and organizational response rather than treated as competing top-level domains.

The event table includes fields such as:

- `event_id`
- `episode_id`
- `compounds_with`
- `outlet_id`
- `record_type`
- event dates and date precision;
- event state/city and scope;
- target type and role;
- primary and secondary domain;
- mechanism;
- actor class and named actor;
- coercion type;
- severity and reversibility;
- event status and summary;
- outcome and documented consequence;
- verification level;
- source URLs and source type;
- coding confidence;
- organizational response.

The event schema is documented in `docs/RISK_SCHEMA_RECONCILIATION_V1.md`, and the normalized table is stored in `data/phase1b/risk_events_v2.csv`.

---

## 8. Outlet-specific events versus structural exposure

The study distinguishes outlet-specific events from sector-wide conditions.

An assault, detention, lawsuit, staffing loss, access restriction, platform action, or other documented event involving a specific outlet can be linked to that outlet through `outlet_id` when evidence supports the connection.

By contrast, sector-wide developments such as declining platform referral traffic, philanthropic contraction, emergency press-safety conditions, changes in platform monetization policies, or enforcement environments are coded as structural exposures. These are **not** automatically assigned to every outlet.

An outlet is treated as specifically exposed to a structural condition only when the institutional-enrichment or support-infrastructure layer provides evidence linking the outlet to the relevant funding, referral, distribution, legal, safety, or institutional system.

This prevents ecological inference from sector-level trends to individual organizations.

---

## 9. Platform monetization and financial security

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

## 10. No composite risk score

The project does not convert staffing, revenue, legal support, network relationships, documented incidents, or platform dependence into a single numerical risk score.

A small outlet is not assumed to be high risk, and a larger, better-funded, or highly networked outlet is not assumed to be protected from harm. Instead, the design preserves the empirical relationship among:

**internal capacity + external/networked capacity → structural exposure → documented event or anticipatory response → organizational response → consequence**

This allows the study to examine how resources may redistribute, mitigate, or sometimes fail to mitigate risk without presupposing a linear relationship between organizational size, network embeddedness, and vulnerability.

---

## 11. Comparison cases

The risk-event scan may identify relevant immigrant, ethnic, language, independent, or community journalists/outlets that were not present in the frozen Phase 1A core frame.

These are retained as `comparison_case = yes` rather than being retroactively inserted into Phase 1A. If a later crosswalk establishes that a comparison case corresponds to an existing Phase 1A organization, the relationship can be documented without altering the frozen release.

This preserves temporal integrity of the original sampling frame while allowing the risk-event corpus to capture relevant events beyond it.

---

## 12. Reproducibility and public availability

The research repository is public and is designed to support reconstruction of the data workflow.

The repository preserves:

- candidate and verification records;
- the frozen Phase 1A release;
- data dictionaries and controlled-variable codebooks;
- relationship-review and community-orientation decisions;
- scripts used to build and validate analytical datasets;
- GitHub Actions workflows;
- Phase 1B enrichment codebooks;
- the external support-infrastructure coding addendum;
- the platform/financial-security coding rules;
- the canonical enrichment evidence log and audit decisions;
- evidence-backed enrichment batches;
- the normalized risk-event table and schema-reconciliation note;
- the external support-infrastructure relationship table;
- source URLs and evidence notes;
- version history through Git commits.

The frozen Phase 1A release includes SHA-256 checksums so researchers can verify that archived files have not changed.

Phase 1B is versioned separately from Phase 1A. New enrichment records are added through evidence-backed and auditable layers rather than modifying the frozen sampling-frame release.

A researcher can therefore reproduce the study at two levels:

### Computational reconstruction
Using the archived Phase 1A files, controlled coding files, Python scripts, and GitHub Actions workflow to rebuild the analytical frame.

### Procedural replication
Using the published inclusion criteria, source hierarchy, enrichment codebook, support-infrastructure addendum, missing-data rules, and event-coding protocol to repeat the public-source collection process.

An independent replication may not yield an identical set of current webpages or institutional characteristics because organizations change, staff move, websites disappear, memberships change, funding changes, and new incidents occur. The project therefore treats reproducibility as **transparent reconstruction of a time-bounded research process**, rather than an expectation that a dynamic media ecosystem will remain unchanged.

---

## 13. Public versus restricted research data

The public repository should contain institutional, relational, and event information that is already publicly available and appropriate for scholarly replication.

Public data may include:

- outlet-level institutional characteristics;
- publicly documented support-network relationships;
- organizational contacts already publicly listed in professional roles;
- public funding and governance information;
- publicly reported incidents;
- source URLs;
- coding decisions and confidence.

Future interview data should remain separate from the public institutional dataset. Interview transcripts, consent records, private contact information, immigration-status information, confidential legal or safety assistance, or other sensitive human-subject data should be handled according to IRB requirements and should not be included in the public replication dataset unless explicitly permitted by consent and ethics review.

---

## 14. Transition to interview sampling and IRB

The frozen national sampling frame and the public enrichment layers jointly provide the basis for purposive interview sampling.

Interview cases can be selected to capture contrasts in:

- organizational form;
- newsroom size and internal capacity;
- language/community model;
- media format;
- geographic scope;
- funding model;
- platform dependence;
- internal legal/safety resources;
- external support infrastructure and degree/type of network embeddedness;
- documented risk exposure;
- anticipatory organizational adaptations;
- organizational responses to documented events.

External support infrastructure is therefore a sampling dimension rather than simply a descriptive variable. The interview sample should include variation among highly networked outlets, outlets with one or two specialized support relationships, fiscally sponsored or hosted outlets, outlets connected to legal or safety organizations, outlets connected primarily through field-building/community-media institutions, and outlets with little publicly identifiable external support.

The interview phase can then investigate dimensions that public sources cannot establish reliably, including whether nominal affiliations provide usable support; whether newsrooms actually mobilize legal, safety, technical, financial, or peer resources during crises; informal safety practices; experienced threats; legal chilling; source-protection decisions; immigration-related concerns; platform dependence; self-censorship; financial insecurity; internal decision-making; and organizational adaptation.

The public 301-outlet frame is the organizational sampling frame. Human subjects enter the study only through recruitment and interviews, which will proceed under applicable IRB approval and consent procedures.

---

## 15. Core methodological contribution

The methodological contribution is not simply a directory of immigrant-serving news organizations or a list of press-freedom incidents. It is the linkage of a verified national sampling frame with separately coded layers of **internal organizational capacity, external support infrastructure, and risk events/structural exposure**.

This design makes it possible to study risk ecologies relationally: not only whether journalists and news organizations experience threats, but how institutional form, financial structure, platform dependence, internal resources, and networked external support shape the distribution, management, and consequences of those risks across the immigrant-journalism ecosystem.
