# Phase 1B Threat, Risk, and Structural Exposure Coding Protocol

## Purpose

This protocol creates a separate event/exposure layer linked to the frozen Phase 1A outlet frame. It is intended to capture publicly documented threats, attacks, legal pressures, platform disruptions, and financial shocks affecting mapped outlets and comparable immigrant/ethnic/community media.

Do **not** collapse these events into the institutional enrichment row. One outlet may experience multiple events over time, and some structural risks operate at sector or platform level rather than at a single outlet.

Recommended file:

`data/phase1b/risk_events_v1.csv`

---

# Unit of analysis

One row = one documented event, episode, or structural exposure.

The event may be:
- outlet-specific;
- journalist-specific but institutionally linked;
- multi-outlet;
- sector-wide;
- platform-wide or policy-wide.

Where the affected outlet is in the Phase 1A map, link through `outlet_id`. Otherwise retain an external comparison record with `outlet_id` blank and `comparison_case=yes`.

---

# Core event fields

`event_id`
Stable identifier: `RISK0001`, etc.

`outlet_id`
Phase 1A outlet ID where applicable.

`outlet_name`
Outlet name at time of event.

`organization_id`
Where known.

`comparison_case`
- `yes`
- `no`

`event_date_start`
ISO date where known.

`event_date_end`
For continuing/multi-day events.

`jurisdiction`
Primary U.S. state/territory or national/sector-level.

`event_scope`
- `individual_journalist`
- `single_outlet`
- `multiple_outlets`
- `sector_wide`
- `platform_wide`

---

# Risk domain

`risk_domain`
One primary domain:
- `physical_safety`
- `legal_or_regulatory`
- `immigration_or_border_enforcement`
- `digital_security`
- `online_harassment_or_doxxing`
- `platform_governance`
- `financial_security`
- `labor_or_employment`
- `source_or_audience_safety`
- `political_or_state_pressure`
- `other`

`risk_subtype`
Semicolon-separated where relevant:
- `arrest_or_detention`
- `physical_assault`
- `threat_of_violence`
- `harassment`
- `doxxing`
- `surveillance`
- `subpoena_or_court_order`
- `lawsuit_or_legal_threat`
- `access_restriction`
- `equipment_seizure_or_damage`
- `account_suspension`
- `demonetization`
- `algorithmic_visibility_loss`
- `referral_traffic_loss`
- `content_removal`
- `copyright_claim`
- `funding_cut_or_grant_loss`
- `advertising_loss`
- `layoff_or_staff_reduction`
- `closure_or_suspension_risk`
- `emergency_fundraising`
- `other`

---

# Evidence and attribution

`event_status`
- `confirmed_publicly_documented`
- `reported_by_outlet`
- `reported_by_credible_secondary_source`
- `alleged_or_disputed`
- `unclear`

`event_summary`
Brief factual summary. Attribute allegations and disputed claims explicitly.

`actor_or_source_of_risk`
Named institution/actor where publicly documented, e.g. law enforcement agency, litigant, platform, funder, advertiser, unknown actor.

Do not infer motive.

`source_url_primary`
Best evidence URL.

`source_url_secondary`
Optional corroboration.

`source_type_primary`
- `outlet_self_report`
- `press_freedom_tracker`
- `court_or_government_record`
- `journalism_association`
- `credible_news_report`
- `platform_policy_or_notice`
- `funder_or_grantmaker`
- `other`

`date_checked`
Research check date.

`coding_confidence`
- `high`
- `medium`
- `low`
- `requires_manual_review`

---

# Consequence fields

`documented_consequence`
Semicolon-separated where supported:
- `injury`
- `detention`
- `legal_cost`
- `reporting_interruption`
- `loss_of_access`
- `content_loss`
- `traffic_loss`
- `revenue_loss`
- `staff_reduction`
- `publication_reduction`
- `temporary_shutdown`
- `closure`
- `security_changes`
- `emergency_fundraising`
- `no_consequence_publicly_documented`
- `unclear`

`financial_consequence_amount`
Numeric only if publicly documented.

`organizational_response`
Brief descriptive text on legal challenge, safety changes, fundraising, platform appeal, staffing changes, collaboration, etc.

---

# Structural exposure records

Some risks are not discrete attacks on one newsroom but structural changes affecting many outlets. These should still be recorded, with `event_scope=sector_wide` or `platform_wide`.

Examples include:
- major platform reductions in news referrals;
- changes to platform monetization programs;
- government or philanthropic funding contraction;
- advertising-market shocks;
- legal/regulatory changes affecting newsgathering or immigrant communities;
- search/AI changes that reduce publisher click-through.

For these rows, `outlet_id` may be blank. Later analysis can link structural exposures to outlets according to their documented dependence on affected revenue/distribution channels.

Important: do not assume every outlet experienced the same effect. A sector-level exposure means a plausible external condition existed; outlet-level impact requires separate evidence.

---

# Search strategy

For each mapped outlet, use combinations of outlet name with terms such as:

`threat`, `harassment`, `attack`, `assault`, `detained`, `arrested`, `ICE`, `police`, `lawsuit`, `subpoena`, `legal threat`, `doxxed`, `cyberattack`, `hacked`, `demonetized`, `suspended`, `Facebook`, `YouTube`, `TikTok`, `Google`, `algorithm`, `funding cut`, `grant loss`, `layoff`, `closure`, `financial crisis`, `emergency fundraiser`.

Also search by sector/community terms because some incidents may be reported without the outlet name in the headline:

`immigrant media`, `ethnic media`, `Latino media`, `Asian American media`, `Arab American media`, `Somali media`, `refugee media`, `Spanish-language newsroom`, `community media`.

---

# Source priority for risk events

1. U.S. Press Freedom Tracker or comparable documented press-freedom incident database;
2. court/government records for legal proceedings;
3. outlet's own detailed account;
4. journalism associations / press-freedom organizations;
5. high-quality local or national reporting;
6. platform/funder announcements for structural financial/platform events.

Use more than one source when an event is contested or consequences are material.

---

# Analytical rule

Do not create a single composite "risk score" during collection.

The project should preserve three distinct concepts:

1. **institutional capacity** — resources the organization has;
2. **documented events** — things that happened to the outlet/journalist;
3. **structural exposure** — external conditions that may create vulnerability.

Phase 2 interviews can then test how these interact rather than assuming that a low-resource outlet necessarily experiences more incidents or that a documented incident necessarily means weak institutional capacity.
