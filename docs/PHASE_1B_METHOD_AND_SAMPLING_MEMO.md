# Methodological Memo: Phase 1B — Publicly Documented Risk Events

**Project:** Immigrant Journalism National Map  
**Phase:** 1B — Publicly Documented Risk Events  
**Purpose:** To identify and systematically document publicly verifiable legal, political, digital, physical, and institutional pressure events involving immigrant-serving journalism organizations included in the national institutional map.

## 1. Purpose of Phase 1B

Phase 1A maps the institutional landscape of immigrant and immigrant-serving journalism in the United States. Phase 1B adds a second analytical layer by identifying **publicly documented risk events involving those institutions**.

The goal is not to determine which outlet is “most vulnerable” or to estimate the true prevalence of risk. Rather, Phase 1B documents observable events that entered the public record and examines how those events intersect with different institutional forms of immigrant journalism.

The central methodological principle is:

> **Documented exposure is not equivalent to total exposure.**

An outlet for which no event is found should therefore be coded as `not_identified`, not as having experienced no risk.

## 2. Phase 1B Research Questions

**RQ1B.1:** What kinds of publicly documented legal, political, digital, physical, and institutional pressures have involved immigrant-serving journalism organizations in the United States?

**RQ1B.2:** How are documented risk events distributed across different institutional forms, including nonprofit, commercial, founder-led, network-affiliated, hosted, multilingual, and diaspora-oriented outlets?

**RQ1B.3:** What publicly documented consequences follow these events, including litigation, newsroom disruption, changes to reporting practices, safety measures, financial costs, or organizational responses?

**RQ1B.4:** What forms of institutional support or intermediary infrastructure are publicly visible when immigrant-serving media encounter such events?

These questions remain descriptive and relational. They do not require assigning risk scores to individual outlets.

## 3. Unit of Analysis

The primary unit of analysis is the **documented event**, not the outlet.

One outlet may therefore have:

- zero publicly identified events;
- one event;
- multiple events across different years;
- multiple event types associated with the same episode.

The institutional outlet database and the event database should remain separate and be connected through `outlet_id`.

This produces a relational structure:

`outlet → documented event → actor → institutional response → consequence → source`

## 4. Proposed Event Categories

### A. Legal exposure

Possible subtypes:

- defamation or libel lawsuit
- privacy lawsuit
- copyright lawsuit
- subpoena
- compelled disclosure
- source-identification dispute
- contempt proceedings
- records-access litigation
- employment litigation related to journalism activity
- SLAPP or anti-SLAPP dispute
- other civil litigation

A lawsuit should not automatically be treated as political pressure or a press-freedom violation. Record what happened without inferring motive.

### B. Government or political pressure

Possible subtypes:

- elected-official pressure
- government criticism directed at outlet
- access restriction
- press credential restriction
- exclusion from public event
- regulatory investigation
- official demand for removal or correction
- immigration-enforcement interaction involving journalists
- government surveillance allegation supported by credible evidence

Political disagreement with reporting by itself should not automatically qualify. There should be some identifiable action, threat, restriction, investigation, or institutional pressure.

### C. Harassment and intimidation

Possible subtypes:

- threats
- doxxing
- swatting
- coordinated harassment
- intimidation
- racist or xenophobic targeting
- threats directed at family members
- harassment tied to specific coverage

### D. Physical safety

Possible subtypes:

- assault
- physical obstruction
- injury while reporting
- detention
- arrest
- equipment seizure
- property damage

### E. Digital and cybersecurity pressure

Possible subtypes:

- account takeover
- hacking
- DDoS attack
- phishing
- impersonation
- doxxing
- coordinated online abuse
- website disruption
- unauthorized content removal

### F. Platform-related disruption

Possible subtypes:

- account suspension
- demonetization
- content removal
- algorithmic visibility disruption
- advertising restriction
- platform-policy enforcement affecting publication

These should only be included when sufficiently documented rather than inferred from changes in engagement.

### G. Transnational pressure

Especially relevant for diaspora journalism.

Possible subtypes:

- foreign-government threats
- surveillance allegations
- pressure on relatives abroad
- diplomatic intimidation
- transnational harassment
- foreign legal action
- threats from political or armed groups abroad

### H. Organizational disruption

Possible subtypes:

- newsroom closure after documented pressure
- staff departure linked publicly to threats
- cancellation of event
- reduction of coverage
- suspension of reporting
- relocation
- security changes
- legal-cost burden

This category should generally represent a consequence rather than an initial pressure event.

## 5. Inclusion Criteria

Include an event when all of the following are true:

1. The event involves an outlet already contained in the institutional sampling frame, or clearly involves a journalist acting in an identifiable professional capacity for that outlet.
2. The event is supported by at least one identifiable public source.
3. The event involves a legal, political, digital, physical, organizational, or other pressure relevant to journalistic practice.
4. There is enough information to establish at minimum:
   - the outlet or journalist;
   - approximate date;
   - type of event;
   - public source.
5. The event can be described without relying on speculation.

## 6. Exclusion Criteria

Do not include:

- ordinary negative comments about an outlet;
- routine corrections;
- general criticism without pressure or threat;
- disputes unsupported by identifiable sources;
- rumors;
- unattributed social-media allegations;
- normal commercial disputes with no meaningful connection to journalistic operation, unless the research design intentionally includes general legal exposure;
- crimes affecting a journalist that have no documented connection to professional activity;
- purely historical incidents involving organizations outside the active sample unless retained in a separate historical layer.

Some legal cases may be recorded but classified as `legal_exposure_non_press_specific` where appropriate.

## 7. Evidence Hierarchy

The event dataset should preserve source type rather than collapse everything into a single reliability score.

Suggested `source_type` values:

- `court_or_public_record`
- `outlet_self_report`
- `press_freedom_organization`
- `professional_association`
- `credible_news_report`
- `academic_or_research_source`
- `government_record`
- `other`

Suggested `evidence_quality` values:

- `primary_documentary`
- `primary_self_report`
- `corroborated_secondary`
- `credible_secondary`
- `unverified_lead`

Only the first four should enter the verified event dataset.

`unverified_lead` can remain in a discovery file.

## 8. Event Dataset Structure

Recommended file:

`data/risk_events/public_risk_events.csv`

Suggested fields:

```text
event_id
outlet_id
outlet_name
state
event_date
event_year
event_category
event_subtype
target_type
actor_type
event_summary
legal_case_name
court_or_agency
case_number
case_status
direct_or_contextual
source_type
source_title
source_publisher
source_date
source_url
evidence_quality
documented_consequence
institutional_response
verification_status
verification_notes
last_verified
```

### Useful controlled values

`target_type`

```text
outlet
journalist
editor
publisher
multiple_staff
event_or_forum
newsroom_property
```

`actor_type`

```text
government
law_enforcement
elected_official
court_litigant
private_individual
organized_group
foreign_government
political_group
platform
unknown
other
```

`direct_or_contextual`

```text
direct
state_context
ecosystem_context
```

`verification_status`

```text
verified
pending_second_source
unclear
exclude
```

## 9. Consequence Coding

Possible consequences:

```text
coverage_changed
event_cancelled
comments_disabled
reporting_suspended
staff_security_measures
legal_costs
court_judgment
settlement
case_dismissed
access_restricted
journalist_injured
journalist_detained
staff_departure
organizational_relocation
no_public_consequence_identified
unclear
```

Multiple consequences can be recorded either as semicolon-separated values or, if the dataset grows, in a separate relational table.

## 10. Search Procedure

For every verified outlet, conduct the same basic search protocol.

Search combinations such as:

```text
"[outlet name]" lawsuit
"[outlet name]" defamation
"[outlet name]" libel
"[outlet name]" court
"[outlet name]" subpoena
"[outlet name]" arrested journalist
"[outlet name]" threatened
"[outlet name]" harassment
"[outlet name]" doxxing
"[outlet name]" swatting
"[outlet name]" attack
"[outlet name]" police
"[outlet name]" government
"[outlet name]" mayor
"[outlet name]" censorship
"[outlet name]" press freedom
"[outlet name]" hacking
"[outlet name]" cyberattack
"[outlet name]" suspended
"[outlet name]" immigration enforcement
```

Then search dedicated sources such as:

- U.S. Press Freedom Tracker
- Committee to Protect Journalists
- Reporters Committee for Freedom of the Press
- PEN America where relevant
- CourtListener / RECAP
- Justia
- Google Scholar case law
- federal and state court records where accessible
- credible local and national news
- the outlet's own public statements

## 11. State-Level Context Layer

Recommended file:

`data/risk_context/state_press_environment.csv`

This is separate from outlet-specific risk.

Possible fields:

```text
state
context_event_id
event_date
context_category
event_summary
journalism_relevance
source_type
source_url
evidence_quality
notes
```

Examples could include statewide reporter-shield litigation, police treatment of journalists, state anti-SLAPP law changes, government access restrictions, or major court rulings affecting journalism.

The presence of a state-level event should **not** be assigned to every outlet in the state.

# Sampling Memo for Phase 1B

## Sampling Strategy

Phase 1B will use a **nested purposive sample derived from the Phase 1A institutional sampling frame**.

The first pilot should not begin with all outlets nationally.

Instead, sample states that provide meaningful variation in:

- immigrant population and linguistic diversity;
- density of immigrant-serving journalism;
- institutional form;
- nonprofit versus commercial structure;
- large versus small media markets;
- network-affiliated versus independent outlets;
- geographic region.

## Recommended Pilot

Start with approximately five states:

- **Minnesota**
- **Michigan**
- **New York**
- **California**
- **Illinois**

These provide substantial institutional variation:

- Minnesota: nonprofit, Somali, Hmong, Korean, Latino and community-radio ecosystem.
- Michigan: Arab, Yemeni, Chaldean, Korean, Latino, Polish and African-diaspora media.
- New York: very dense multilingual immigrant-media ecosystem.
- California: large and institutionally diverse immigrant-media environment.
- Illinois: strong Chicago immigrant/diaspora ecosystem with both new nonprofit newsrooms and longstanding ethnic presses.

This is **not** intended as a representative sample of the United States.

It is a methodological pilot designed to determine whether publicly documented event data can be collected consistently enough to scale the procedure nationally.

## Pilot Sample Size

For the first test, do not search every outlet.

Select roughly:

**5 states × 8–12 outlets per state = approximately 40–60 outlets.**

Purposefully vary the outlets within each state, including:

- independent nonprofit newsroom
- commercial ethnic newspaper
- diaspora newspaper
- multilingual outlet
- hosted/community-radio program
- network-affiliated Spanish-language newsroom
- small founder-led outlet
- large longstanding outlet

If the search yields useful event data and reasonable source consistency, then scale Phase 1B to the full verified national frame.

## Pilot Success Criteria

After the first 40–60 outlets, assess:

1. What percentage produce at least one documented event?
2. Which event categories actually appear?
3. Which sources generate the most usable evidence?
4. How much time does each outlet require?
5. Are legal databases productive enough to justify systematic searching?
6. Are there large visibility biases favoring prominent outlets?
7. Can we reliably distinguish absence of evidence from actual absence?
8. Do the events generate meaningful links to institutional form and organizational response?

If the answer to those questions is generally yes, Phase 1B becomes national.

## Analytical Logic

The eventual analysis should avoid:

> “Outlet X is more risky than Outlet Y.”

Instead, ask:

> What types of documented pressures become publicly visible across different forms of immigrant journalism?

Then:

> What institutional resources appear around those events?

And eventually, through interviews:

> What forms of pressure never entered the public record, and how do journalists themselves understand their relationship to organizational capacity, editorial autonomy, and knowledge production?

This creates a clean methodological progression:

**Phase 1A — Institutional Map**  
↓  
**Phase 1B — Publicly Documented Risk Events**  
↓  
**Phase 2 — Purposive Interviews and Critical Incidents**  
↓  
**Relational Risk-Ecology Analysis**

The key methodological payoff is that **Phase 1B does not replace the interviews**. It provides observable institutional evidence against which interview accounts can later be interpreted.
