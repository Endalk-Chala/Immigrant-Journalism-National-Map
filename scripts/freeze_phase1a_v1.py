#!/usr/bin/env python3
"""Freeze National Immigrant Journalism Map v1.0 — Phase 1A.

Copies the principal Phase 1A analytical files and documentation into an immutable-style
versioned directory and writes SHA-256 checksums. Later work should create a new version
rather than edit this snapshot.
"""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "releases" / "national-immigrant-journalism-map-v1.0-phase1a"

FILES = [
    "data/analysis/national_verified_registry_v1.csv",
    "data/analysis/national_core_outlets_v1.csv",
    "data/analysis/national_controlled_coding_v1.csv",
    "data/analysis/state_summary_v1.csv",
    "data/analysis/relationship_review_decisions_v1.csv",
    "data/analysis/community_orientation_review_decisions_v1.csv",
    "data/analysis/community_orientation_language_ethnic_decisions_v1.csv",
    "data/analysis/audits/controlled_coding_summary_v1.csv",
    "data/analysis/audits/relationship_validation_summary_v1.csv",
    "data/analysis/audits/community_orientation_review_application_summary_v1.csv",
    "data/analysis/audits/language_ethnic_review_application_summary_v1.csv",
    "docs/NATIONAL_DATASET_README.md",
    "docs/DATA_DICTIONARY.md",
    "docs/CONTROLLED_VARIABLES_CODEBOOK.md",
    "docs/PHASE_1A_COMPLETION_REPORT.md",
]

SNAP.mkdir(parents=True, exist_ok=True)
checksums = []
for rel in FILES:
    src = ROOT / rel
    if not src.exists():
        raise SystemExit(f"Cannot freeze Phase 1A; missing required file: {rel}")
    dest = SNAP / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    checksums.append((digest, rel))

manifest = "# National Immigrant Journalism Map v1.0 — Phase 1A\n\n"
manifest += "Frozen Phase 1A analytical snapshot. Do not edit files in this directory in place. " \
            "Subsequent corrections, discoveries, or Phase 2 work should use a new version.\n\n"
manifest += "## Included files\n\n" + "\n".join(f"- `{rel}`" for _, rel in checksums) + "\n"
(SNAP / "README.md").write_text(manifest, encoding="utf-8")

checksum_text = "".join(f"{digest}  {rel}\n" for digest, rel in checksums)
(SNAP / "SHA256SUMS.txt").write_text(checksum_text, encoding="utf-8")

version = ROOT / "VERSION_PHASE1A.md"
version.write_text(
    "# National Immigrant Journalism Map v1.0 — Phase 1A\n\n"
    "Status: **FROZEN**\n\n"
    "Frozen snapshot path: `releases/national-immigrant-journalism-map-v1.0-phase1a/`\n\n"
    "Phase 2 work must not overwrite the v1.0 Phase 1A snapshot. New discoveries or corrections should be versioned separately.\n",
    encoding="utf-8",
)

print(f"Frozen files: {len(checksums)}")
print(SNAP)
