# Phase 1B External Support Infrastructure Addendum

## Purpose

This addendum extends the institutional-enrichment framework to capture forms of **external or networked organizational capacity** available to immigrant-serving news organizations.

The study's working theoretical proposition is that small immigrant-serving news organizations may rely on external professional, legal, safety, fiscal, technical, funding, and field-building organizations for capacities that larger newsrooms often maintain internally. The study therefore asks whether these relationships function as forms of **distributed organizational capacity** that buffer, mediate, or otherwise shape risk.

This is a proposition to be tested, not a finding assumed in advance.

The data architecture must distinguish three analytically different levels:

1. **Affiliation or connection** — whether an outlet has a documented relationship with a support organization;
2. **Potentially available support** — what resources or services the support organization publicly makes available through that relationship;
3. **Documented mobilization or use** — evidence that the outlet actually accessed or used those resources.

Membership or directory presence must never be treated as evidence that support was used.

---

## Why a separate relationship table is required

Support infrastructure is many-to-many:

- one outlet may be connected to INN, LION, Tiny News Collective, a fiscal sponsor, a university, a legal organization, and a local collaborative;
- one support organization may serve many outlets.

These relationships should therefore be stored separately from the 301-row outlet-level enrichment file.

Recommended file:

`data/phase1b/support_infrastructure_relationships_v1.csv`

One row = one documented relationship between one mapped outlet and one support organization or support program.

---

## Core fields

### `relationship_id`
Stable identifier: `SUP000001`, etc.

### `outlet_id`
Phase 1A outlet identifier.

### `organization_id`
Parent/organization identifier where known.

### `support_organization`
Name of the external organization, network, sponsor, collaborative, legal organization, funder, or field-building institution.

Examples may include:

- Institute for Nonprofit News (INN)
- LION Publishers
- Tiny News Collective
- Center for Community Media at CUNY/Newmark J-School
- Reporters Committee for Freedom of the Press
- Lawyers for Reporters
- Committee to Protect Journalists
- International Women's Media Foundation
- fiscal sponsors
- local journalism collaboratives
- university-based journalism programs
- journalism-support funders or emergency-assistance programs

This list is illustrative, not exhaustive.

### `support_organization_type`
Controlled values:

- `professional_membership_network`
- `field_building_institution`
- `legal_support_organization`
- `journalist_safety_organization`
- `fiscal_sponsor_or_host`
- `funding_or_grantmaking_organization`
- `technology_or_security_support`
- `journalism_collaborative`
- `university_or_training_partner`
- `identity_or_community_media_network`
- `other`

### `relationship_type`
Controlled values:

- `formal_member`
- `fiscal_sponsorship`
- `hosted_program`
- `program_participant`
- `grantee`
- `training_participant`
- `legal_support_relationship`
- `safety_support_relationship`
- `collaborative_partner`
- `technical_support_relationship`
- `directory_listing_only`
- `other`
- `unclear`

A directory listing must not be upgraded to membership or support participation without separate evidence.

### `relationship_status`

- `explicitly_verified`
- `externally_documented`
- `historical`
- `unclear`
- `not_publicly_disclosed`

### `support_functions_available`
Semicolon-separated controlled values where public evidence establishes that the relevant organization/program makes the support available:

- `legal_support`
- `media_liability_insurance`
- `physical_safety`
- `digital_security`
- `online_harassment_support`
- `emergency_assistance`
- `fiscal_sponsorship`
- `technology`
- `funding`
- `business_or_operational_support`
- `training`
- `peer_support`
- `research_or_field_building`
- `audience_or_distribution_support`
- `policy_or_advocacy_support`
- `other`

This field describes potential capacity available through the relationship; it does not prove outlet use.

### `support_access_status`

- `verified_access_through_relationship`
- `general_eligibility_only`
- `affiliation_only_support_unclear`
- `unclear`
- `not_publicly_disclosed`

### `documented_support_used`

- `yes`
- `no_public_evidence_of_use`
- `unclear`
- `not_publicly_disclosed`

`no_public_evidence_of_use` does not mean the outlet did not use the resource.

### `support_use_type`
Semicolon-separated from the same controlled function list when actual use is documented.

### `support_use_description`
Short factual description of what was used, by whom at the organizational level, and under what circumstances. Avoid sensitive personal details unless already publicly documented and necessary.

### `relationship_evidence_url`
Source establishing the relationship.

### `support_service_evidence_url`
Source establishing the support functions available through the organization/program.

### `support_use_evidence_url`
Source establishing actual use, if publicly documented.

### `evidence_date`
Date of the relationship/service evidence when available.

### `date_checked`
Date checked by the research team.

### `coding_confidence`

- `high`
- `medium`
- `low`
- `requires_manual_review`

### `notes`
Short coding note for ambiguity, time period, program limits, historical membership, or distinctions between affiliation and service use.

---

## Coding rules

1. **Do not equate directory presence with institutional support.** A CUNY CCM directory listing, for example, may help validate that an outlet exists but does not by itself establish program participation or access to CCM support.
2. **Do not equate membership with resource use.** INN, LION, or Tiny News Collective membership may establish eligibility or access to resources; actual mobilization requires separate evidence.
3. **Do not code the absence of public evidence as absence of support.** Use `not_publicly_disclosed` or `no_public_evidence_of_use` as appropriate.
4. **Distinguish organization-wide services from outlet-specific use.** A support organization's website can establish what it offers; the outlet's website, public reporting, program records, or interviews may establish actual use.
5. **Preserve time.** Historical membership or a one-time grant should not automatically be treated as current support.
6. **Treat confidential or non-public legal/safety assistance conservatively.** Do not infer or seek private client relationships from silence. Interviews may establish support use subject to IRB and participant consent.
7. **Support infrastructure is not itself a risk score.** Network embeddedness may buffer risk, increase capacity, or have little practical effect; the empirical analysis must determine the relationship.

---

## Relation to existing Phase 1B variables

Existing outlet-level variables remain useful:

- `network_memberships`
- `network_membership_status`
- `collaborative_partnerships_public`
- `parent_resource_relationship`
- `legal_support_status`
- `safety_support_status`

They should function as summary fields at the outlet level.

The new relationship table is the source-level relational layer that records **which organization**, **what relationship**, **what support is potentially available**, and **whether actual use is documented**.

Later, the relationship table may be summarized into derived outlet-level variables such as:

- `external_support_relationship_count`
- `external_support_function_count`
- `legal_support_network_access`
- `safety_support_network_access`
- `fiscal_or_operational_support_access`
- `documented_external_support_use`
- `network_embeddedness_sampling_category`

These derived variables should be created only after systematic collection and should not be interpreted as quality or safety scores.

---

## Relation to sampling and IRB

External support infrastructure is a purposive-sampling dimension for the interview study.

The sampling matrix should seek variation among:

- highly networked outlets with multiple documented institutional relationships;
- outlets with one or two specialized support relationships;
- fiscally sponsored or hosted outlets;
- outlets connected to legal or safety-support organizations;
- outlets connected primarily through field-building or community-media institutions;
- outlets with little publicly identifiable external support.

Interviews can then examine the difference between **nominal affiliation** and **functional support** by asking where newsrooms turn when they face legal, physical, digital, financial, platform, or other serious challenges and whether those relationships altered organizational response or consequence.

---

## Working analytical proposition

Small immigrant-serving news organizations may rely on external professional and field-building organizations for capacities that larger newsrooms traditionally internalized. The study therefore examines whether network membership, fiscal sponsorship, legal-support relationships, safety programs, peer networks, and other external institutional connections function as forms of distributed organizational capacity that buffer or mediate risk.
