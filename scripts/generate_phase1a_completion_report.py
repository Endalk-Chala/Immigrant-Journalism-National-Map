#!/usr/bin/env python3
"""Generate the short Phase 1A completion report from final analytical outputs."""

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
CORE = ROOT / "data" / "analysis" / "national_core_outlets_v1.csv"
CONTROLLED = ROOT / "data" / "analysis" / "national_controlled_coding_v1.csv"
REL = ROOT / "data" / "analysis" / "audits" / "relationship_validation_summary_v1.csv"
REPORT = ROOT / "docs" / "PHASE_1A_COMPLETION_REPORT.md"


def read(path):
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

registry = read(REGISTRY)
core = read(CORE)
controlled = read(CONTROLLED)
rel_rows = read(REL)
rel = {r["metric"]: r["value"] for r in rel_rows}

jurisdictions = len({r.get("jurisdiction", "") for r in registry if r.get("jurisdiction")})
analysis_tier = Counter(r.get("analysis_tier", "") for r in registry)
status = Counter(r.get("core_population_role", "") for r in controlled)
community = Counter(r.get("community_orientation", "") for r in controlled)
relationship = Counter(r.get("institutional_relationship", "") for r in controlled)
ownership = Counter(r.get("ownership_or_governance_form", "") for r in controlled)

text = f"""# Phase 1A Completion Report

## National Immigrant Journalism Map v1.0 — Phase 1A

Phase 1A is complete and frozen as a national institutional sampling frame for immigrant-serving journalism in the United States. The mapping covers **{jurisdictions} jurisdictions (50 states plus the District of Columbia)** and contains **{len(registry)} verified/assessed records**, including **{len(core)} core verified outlets or journalism products**.

## Final frame

- Total assessed records: **{len(registry)}**
- Core verified outlets/products: **{len(core)}**
- Core population role: **{status.get('core_outlet_or_product', 0)} core**, **{status.get('pending_verification', 0)} pending**, **{status.get('boundary_case', 0)} boundary**, **{status.get('contextual_infrastructure', 0)} contextual infrastructure**, **{status.get('market_context_only', 0)} market-context records**, **{status.get('historical_context_only', 0)} historical-context records**
- Relationship review: **{rel.get('review_pairs_resolved', '0')} of {rel.get('review_pairs_total', '0')} priority pairs resolved**, with **{rel.get('review_pairs_pending', '0')} remaining pending**
- Organization IDs assigned during priority relationship review: **{rel.get('organization_ids_assigned', '0')}**, covering **{rel.get('records_with_organization_id', '0')} records**

## Community-orientation validation

The final bounded Phase 1A review separates publishing language from community identity. Explicit Latino/Hispanic/AAHPI/other ethnic-racial audience evidence is coded in `community_orientation`, while language remains independently represented in `language_model`.

Current community-orientation counts after reviewed corrections include:

- diaspora / national-origin: **{community.get('diaspora_national_origin', 0)}**
- language community: **{community.get('language_community', 0)}**
- ethnic / racial community: **{community.get('ethnic_or_racial_community', 0)}**
- immigrant general: **{community.get('immigrant_general', 0)}**
- refugee general: **{community.get('refugee_general', 0)}**
- mixed orientation: **{community.get('mixed_orientation', 0)}**
- multicultural / multiethnic: **{community.get('multicultural_multiethnic', 0)}**
- unclear: **{community.get('unclear', 0)}**

## Known unresolved cases and limitations

Phase 1A intentionally stops before eliminating every `unclear` value. Remaining uncertainty is preserved rather than inferred from weak evidence. The main limitations are:

1. **Ownership/governance disclosure is incomplete.** `ownership_or_governance_form` remains unclear for **{ownership.get('unclear', 0)}** records because public-facing evidence often does not disclose ownership or governance structure.
2. **Some institutional relationships remain unresolved.** `institutional_relationship` remains unclear for **{relationship.get('unclear', 0)}** records, and the priority similar-name review retains **{rel.get('review_pairs_pending', '0')}** unresolved pairs rather than merging them without evidence.
3. **Community orientation is not forced where evidence is weak.** **{community.get('unclear', 0)}** records remain unclear after the bounded validation pass.
4. **The map is a reproducible sampling frame, not a census claim.** Phase 1A used directory discovery, institutional verification, targeted community/language searches, and first-pass saturation; it does not claim that no additional outlets exist.
5. **Public-site silence is treated as missing evidence, not absence.** Missing ownership, staffing, funding, safety, or legal-support information should not be interpreted as proof that these resources do not exist.
6. **Multistate and hosted records are preserved intentionally.** A single organization may appear in more than one jurisdiction, while distinct hosted language products may share a parent organization. Organization IDs and relationship fields prevent these cases from being treated as simple duplicates.

## Stopping rule

Phase 1A stops here because national jurisdiction coverage is complete, the core/non-core boundary is stable enough for sampling, the highest-risk duplicate and multistate relationships have been reviewed, and the principal structural/interpretive variables are usable with uncertainty explicitly retained. Further resolution of every unclear field would produce diminishing returns and is deferred unless a specific Phase 2 sampling decision requires it.

## Transition to Phase 2

Phase 2 should use this frozen frame to select and study organizations in greater depth. Appropriate next-stage variables include staffing, funding/revenue, founder and organizational history, legal resources, safety/security capacity, platform dependence, publishing cadence, language capacity, and other dimensions of institutional risk ecology. The Phase 1A snapshot should remain unchanged; later corrections or discoveries should be versioned separately.
"""

REPORT.write_text(text, encoding="utf-8")
print(REPORT)
