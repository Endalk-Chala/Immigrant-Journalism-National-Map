# Methodology Note
## A National Institutional Map of Immigrant Journalism and Its Risk Ecologies in the United States

**Working project title:** A National Institutional Map of Immigrant Journalism and Its Risk Ecologies in the United States

**Current phase:** Phase 1 — national institutional mapping and sampling-frame construction

**Date of methodology note:** 21 September 2026

## 1. Purpose

This project begins by constructing a national, state-by-state institutional database of immigrant and immigrant-serving journalism organizations in the United States. The database is intended first as a **sampling frame**, not as a census and not as a risk-scoring system.

The first research task is descriptive and institutional:

> What immigrant and immigrant-serving journalism organizations can be identified across the United States, where are they located, whom do they serve, and what publicly visible institutional infrastructure do they have?

A later phase will use the sampling frame to select a smaller number of theoretically contrasting outlets for qualitative research on risk ecologies.

## 2. Relationship to the accepted study

The accepted Digital Journalism proposal examines how financial, legal, digital, physical, professional, and transnational risks interact within immigrant and immigrant-serving U.S. news organizations. It also asks how newsroom size, funding models, platform dependence, community embeddedness, and intermediary support shape the concentration or redistribution of risk.

The national institutional map strengthens that design by creating a systematic sampling frame before the interview phase. It allows case selection to be based on observable institutional variation rather than convenience alone.

## 3. Unit of analysis

The primary unit is the **news outlet or journalism-producing media organization**.

A secondary institutional unit may be used where appropriate for a **host organization**. This is necessary for media programs that are embedded inside larger institutions, such as a language-specific radio program hosted by a nonprofit community radio station.

The database may therefore use linked identifiers such as:

- `outlet_id`
- `host_organization_id`

## 4. Inclusion principle

An outlet is eligible when it:

1. is based in, or substantially serves audiences in, the United States;
2. currently produces journalism, news, or public-affairs reporting on a sustained basis;
3. substantially serves an immigrant, refugee, diaspora, language, ethnic, or immigrant-origin community; and
4. is more than a general-interest outlet that only occasionally covers immigration.

The study distinguishes media that report **for or with immigrant communities** from outlets that merely report **about immigration**.

## 5. Exclusion principle

Exclude or flag for exclusion:

- inactive or clearly defunct outlets;
- entertainment-only or promotional platforms without sustained journalism;
- community organizations that publish announcements but do not produce journalism;
- general-interest outlets with only occasional immigration stories;
- social-media pages with no identifiable journalistic operation;
- historical outlets unless they are being retained in a separate archival registry.

Borderline cases remain in the candidate registry until manually reviewed.

## 6. Sampling-frame strategy

The project uses a **state-by-state discovery and verification workflow**.

The national database is not intended to prove exhaustive census coverage. Instead, it aims to produce a systematic, transparent, and sufficiently broad sampling frame from which institutionally diverse cases can later be selected.

Initial pilot states:

- Minnesota
- Wisconsin
- Illinois
- Washington
- North Carolina
- Ohio

Planned next expansion:

- California
- Oregon
- Washington (deeper pass)
- Texas
- Alabama

Expansion will proceed in manageable regional or multi-state batches.

## 7. Discovery workflow

For each state:

### Step 1: Broad discovery
Search multiple discovery sources, including:

- national immigrant/ethnic media directories;
- state and municipal ethnic-media directories;
- journalism associations and newsroom networks;
- community-radio schedules;
- local nonprofit-news directories;
- targeted web searches by community and language;
- existing outlet websites;
- credible secondary reporting.

### Step 2: Candidate registry
Every plausible outlet is entered into a candidate registry with minimal fields:

- outlet name
- state
- city
- website
- discovery source
- screening status

At this stage, inclusion is provisional.

### Step 3: Eligibility screening
Visit the current outlet website and determine:

- whether it is active;
- whether it produces journalism on a sustained basis;
- whether immigrant/refugee/diaspora or immigrant-origin communities are a sustained part of its audience, mission, language, or editorial identity.

### Step 4: Institutional verification
For eligible outlets, collect a limited set of publicly verifiable institutional attributes.

### Step 5: State gap search
Before closing a first-pass state search, conduct targeted searches for major immigrant and language communities that may have been missed by directories.

### Step 6: First-pass saturation
A state reaches first-pass saturation when:

- major available directories have been searched;
- targeted searches have been conducted for major immigrant-language communities;
- a follow-up search produces few or no substantively new outlet types or communities.

This does not imply census completeness.

## 8. Minimum institutional variables

The first national pass should remain intentionally compact.

Core variables:

- `outlet_id`
- `outlet_name`
- `state`
- `city`
- `website`
- `website_active`
- `community_served`
- `languages`
- `media_format`
- `geographic_scope`
- `ownership_type`
- `nonprofit_status`
- `parent_or_host_organization`
- `network_affiliation`
- `staff_information_available`
- `approx_public_staff_count`
- `funding_information_available`
- `legal_support_publicly_disclosed`
- `safety_or_security_support_publicly_disclosed`
- `source_directory`
- `verification_url`
- `last_verified`
- `eligibility_status`
- `notes`

## 9. Institutional variation

The sampling frame should preserve variation rather than force all outlets into one media category.

Important dimensions include:

- nonprofit / commercial / fiscally sponsored / hosted;
- founder-led / small-team / larger staffed newsroom;
- independent / network-affiliated;
- local / metro / statewide / regional / national / transnational;
- English-dominant / bilingual / multilingual / primarily non-English;
- print / digital / radio / television / newsletter / social-first / mixed;
- stand-alone outlet / program embedded in a larger host institution;
- visible versus non-visible legal, technical, fundraising, governance, and safety infrastructure.

Institutional variation is central because it will later inform purposive selection for the risk-ecology phase.

## 10. Evidence rules

All substantive coded fields should be supported by a public source where possible.

Preferred evidence order:

1. outlet or organization website;
2. public tax or governance documents;
3. official directory or institutional source;
4. journalism association or professional organization;
5. credible secondary reporting.

For each claim, preserve:

- source URL;
- source type;
- access/verification date;
- short evidence note where useful.

## 11. Missing-data rule

A critical methodological rule:

> Website silence is not evidence of institutional absence.

Use controlled values such as:

- `explicitly_disclosed`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

Do not code “no legal support,” “no security support,” or similar claims simply because an outlet does not disclose them online.

## 12. Semi-automated website collection

The project may use a conservative scraper to assist with public institutional data collection.

The scraper may:

- visit a supplied outlet domain;
- inspect a small set of likely pages such as About, Staff, Team, Board, Funding, Support, Policies, Privacy, and Contact;
- extract visible text;
- flag terms related to nonprofit status, staff, funding, board structure, legal support, safety/security support, and policies;
- preserve source URLs and surrounding text snippets.

The scraper must **not** make final eligibility or substantive coding decisions.

Automated signals are reviewed manually before entering the verified sampling frame.

## 13. Scraping ethics and constraints

The collection workflow should:

- use publicly accessible pages only;
- respect `robots.txt`;
- crawl at a low request rate;
- avoid logins, paywalls, or technical circumvention;
- avoid scraping private social-media information;
- avoid collecting personal phone numbers, home addresses, immigration status, family information, or other sensitive personal data;
- focus on institutions rather than creating dossiers on individual journalists.

## 14. Public and restricted data layers

The project should separate public research data from sensitive research-management information.

### Public/reproducible layer
May include:

- outlet name;
- city/state;
- website;
- community served;
- language;
- media format;
- ownership/nonprofit structure;
- host/network affiliation;
- visible institutional characteristics;
- evidence URLs;
- codebook and methods;
- scripts.

### Restricted layer
Should include:

- recruitment notes;
- private contact information;
- interview participation status;
- confidential observations;
- interview transcripts;
- identifiable critical incidents not already public;
- any sensitive personal or security information.

Restricted data should never be uploaded to the public GitHub repository.

## 15. Risk ecology comes later

The national database is Phase 1.

The project sequence is:

### Phase 1 — National institutional map
Identify and verify outlets and their publicly visible institutional characteristics.

### Phase 2 — Case selection
Select a smaller sample that maximizes institutional and geographic variation.

### Phase 3 — Risk-ecology research
Conduct interviews and deeper documentary research on financial, legal, digital, physical, professional, and transnational risks.

### Phase 4 — Relational analysis
Examine how risks trigger, amplify, buffer, transfer, or compound one another.

No outlet should be labeled “high risk,” “weak,” or “vulnerable” solely from website evidence.

## 16. Publicly documented exposure variables

A later database layer may record publicly documented institutional exposure such as:

- legal threats or litigation;
- harassment or intimidation;
- physical-safety incidents;
- digital/cyber incidents;
- platform disruption;
- government or political pressure;
- transnational pressure;
- organizational disruption.

These variables measure **publicly documented exposure**, not true incidence or severity.

They should remain separate from the core sampling-frame database until the national institutional map is stable.

## 17. Pilot logic and scalability

The project deliberately begins with a manageable pilot rather than all 50 states at once.

Current pilot work demonstrates that public institutional information can be collected across multiple organizational forms, including:

- nonprofit digital newsrooms;
- commercial ethnic newspapers;
- community radio;
- television and digital networks;
- diaspora publications;
- media programs hosted by larger nonprofit institutions.

The pilot will be used to determine:

- average candidate yield per state;
- average verification workload;
- which variables are consistently observable;
- which variables should be removed or simplified;
- how many outlets are feasible for the national sampling frame.

Only after the pilot should the national codebook be frozen.

## 18. Representativeness

The goal is not statistical representativeness in the survey-sampling sense. The project aims for **institutional, geographic, linguistic, and community breadth** sufficient to construct a credible national sampling frame.

Later qualitative sampling will be purposive and comparative, seeking variation across:

- U.S. region;
- community/language;
- newsroom size;
- nonprofit/commercial form;
- hosted/independent structure;
- network affiliation;
- platform dependence;
- local/transnational orientation;
- visible institutional support capacity.

## 19. Reproducibility

The project should maintain:

- a candidate registry;
- a verified sampling frame;
- a state search log;
- a codebook;
- scraper/source code;
- evidence/source URLs;
- dates of verification;
- versioned releases of datasets.

GitHub can serve as the public reproducibility repository once the pilot structure is stable.

## 20. Current methodological principle

The working principle for the project is:

> **Broad discovery, narrow verification, deeper coding only where analytically useful.**

This keeps the national project ambitious but manageable, protects against overinterpretation, and ensures that the eventual risk-ecology study is built on a transparent and defensible sampling frame.
