# Phase 1A Completion Report

## National Immigrant Journalism Map v1.0 — Phase 1A

Phase 1A is complete and frozen as a national institutional sampling frame for immigrant-serving journalism in the United States. The mapping covers **51 jurisdictions (50 states plus the District of Columbia)** and contains **531 verified/assessed records**, including **301 core verified outlets or journalism products**.

## Final frame

- Total assessed records: **531**
- Core verified outlets/products: **301**
- Core population role: **301 core**, **125 pending**, **79 boundary**, **10 contextual infrastructure**, **14 market-context records**, **2 historical-context records**
- Relationship review: **13 of 16 priority pairs resolved**, with **3 remaining pending**
- Organization IDs assigned during priority relationship review: **8**, covering **18 records**

## Community-orientation validation

The final bounded Phase 1A review separates publishing language from community identity. Explicit Latino/Hispanic/AAHPI/other ethnic-racial audience evidence is coded in `community_orientation`, while language remains independently represented in `language_model`.

Current community-orientation counts after reviewed corrections include:

- diaspora / national-origin: **157**
- language community: **120**
- ethnic / racial community: **94**
- immigrant general: **33**
- refugee general: **1**
- mixed orientation: **31**
- multicultural / multiethnic: **8**
- unclear: **86**

## Known unresolved cases and limitations

Phase 1A intentionally stops before eliminating every `unclear` value. Remaining uncertainty is preserved rather than inferred from weak evidence. The main limitations are:

1. **Ownership/governance disclosure is incomplete.** `ownership_or_governance_form` remains unclear for **447** records because public-facing evidence often does not disclose ownership or governance structure.
2. **Some institutional relationships remain unresolved.** `institutional_relationship` remains unclear for **236** records, and the priority similar-name review retains **3** unresolved pairs rather than merging them without evidence.
3. **Community orientation is not forced where evidence is weak.** **86** records remain unclear after the bounded validation pass.
4. **The map is a reproducible sampling frame, not a census claim.** Phase 1A used directory discovery, institutional verification, targeted community/language searches, and first-pass saturation; it does not claim that no additional outlets exist.
5. **Public-site silence is treated as missing evidence, not absence.** Missing ownership, staffing, funding, safety, or legal-support information should not be interpreted as proof that these resources do not exist.
6. **Multistate and hosted records are preserved intentionally.** A single organization may appear in more than one jurisdiction, while distinct hosted language products may share a parent organization. Organization IDs and relationship fields prevent these cases from being treated as simple duplicates.

## Stopping rule

Phase 1A stops here because national jurisdiction coverage is complete, the core/non-core boundary is stable enough for sampling, the highest-risk duplicate and multistate relationships have been reviewed, and the principal structural/interpretive variables are usable with uncertainty explicitly retained. Further resolution of every unclear field would produce diminishing returns and is deferred unless a specific Phase 2 sampling decision requires it.

## Transition to Phase 2

Phase 2 should use this frozen frame to select and study organizations in greater depth. Appropriate next-stage variables include staffing, funding/revenue, founder and organizational history, legal resources, safety/security capacity, platform dependence, publishing cadence, language capacity, and other dimensions of institutional risk ecology. The Phase 1A snapshot should remain unchanged; later corrections or discoveries should be versioned separately.
