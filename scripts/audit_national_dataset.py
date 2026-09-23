#!/usr/bin/env python3
"""Audit the national immigrant-journalism registry without changing source records.

This script produces review queues for likely duplicates/shared hosts, raw coding
variation, and classification inconsistencies. It never automatically merges or
recodes outlets. Human review remains authoritative.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "analysis" / "national_verified_registry_v1.csv"
OUTDIR = ROOT / "data" / "analysis" / "audits"

GENERIC_NAME_WORDS = {
    "news", "media", "radio", "tv", "television", "newspaper", "magazine",
    "journal", "weekly", "daily", "the", "of", "and", "online", "network",
}


def read_rows() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(name: str, rows: list[dict[str, str]], fields: list[str]) -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / name
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm_text(value: str) -> str:
    value = (value or "").casefold()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def norm_name(value: str) -> str:
    words = [w for w in norm_text(value).split() if w not in GENERIC_NAME_WORDS]
    return " ".join(words)


def website_host(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    if "://" not in value:
        value = "https://" + value
    host = urlparse(value).netloc.casefold()
    if host.startswith("www."):
        host = host[4:]
    return host


def shared_website_groups(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        host = website_host(row.get("website", ""))
        if host:
            groups[host].append(row)

    out = []
    for host, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        names = " | ".join(r["outlet_name"] for r in members)
        ids = " | ".join(r["outlet_id"] for r in members)
        jurisdictions = " | ".join(sorted({r["jurisdiction"] for r in members}))
        statuses = " | ".join(sorted({r["eligibility_status"] for r in members}))
        forms = " | ".join(sorted({r["institutional_form"] for r in members}))
        out.append({
            "website_host": host,
            "n_records": str(len(members)),
            "outlet_ids": ids,
            "outlet_names": names,
            "jurisdictions": jurisdictions,
            "eligibility_statuses": statuses,
            "institutional_forms": forms,
            "review_type": "shared_host_or_possible_duplicate",
            "review_instruction": "Do not auto-merge. Determine parent/program/shared-operation/multistate/true-duplicate relationship.",
        })
    return out


def similar_name_pairs(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    prepared = [(r, norm_name(r["outlet_name"])) for r in rows]
    out = []
    for i, (a, an) in enumerate(prepared):
        if len(an) < 4:
            continue
        for b, bn in prepared[i + 1:]:
            if len(bn) < 4:
                continue
            score = SequenceMatcher(None, an, bn).ratio()
            same_host = website_host(a.get("website", "")) and website_host(a.get("website", "")) == website_host(b.get("website", ""))
            if score >= 0.88 or (score >= 0.76 and same_host):
                out.append({
                    "outlet_id_a": a["outlet_id"],
                    "outlet_name_a": a["outlet_name"],
                    "jurisdiction_a": a["jurisdiction"],
                    "outlet_id_b": b["outlet_id"],
                    "outlet_name_b": b["outlet_name"],
                    "jurisdiction_b": b["jurisdiction"],
                    "name_similarity": f"{score:.3f}",
                    "same_website_host": "yes" if same_host else "no",
                    "review_type": "possible_name_duplicate_or_related_product",
                })
    out.sort(key=lambda r: (-float(r["name_similarity"]), r["outlet_name_a"], r["outlet_name_b"]))
    return out


def value_frequency(rows: list[dict[str, str]], field: str) -> list[dict[str, str]]:
    counts = Counter((r.get(field) or "[blank]").strip() or "[blank]" for r in rows)
    return [{field: value, "n": str(n)} for value, n in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]


def classification_flags(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out = []
    for r in rows:
        status = norm_text(r.get("eligibility_status", ""))
        form = norm_text(r.get("institutional_form", ""))
        notes = norm_text(r.get("verification_notes", ""))
        active = norm_text(r.get("website_active", ""))
        core = r.get("core_inclusion") == "yes"
        reasons = []

        if core and any(token in active for token in ("inactive", "no current", "closed")):
            reasons.append("core_but_inactive_signal")
        if core and any(token in status for token in ("pending", "exclude", "hold", "historical")):
            reasons.append("core_status_conflict")
        if core and "pending" in notes:
            reasons.append("core_but_notes_say_pending")
        if "hosted" in status and not any(token in form for token in ("within", "host", "product", "program", "affiliate")):
            reasons.append("hosted_status_form_mismatch")
        if any(token in status for token in ("multistate", "market case")) and core:
            reasons.append("multistate_context_but_core")
        if not r.get("primary_evidence_url", "").strip() and core:
            reasons.append("core_missing_primary_evidence_url")
        if not r.get("institutional_form", "").strip():
            reasons.append("missing_institutional_form")

        if reasons:
            out.append({
                "outlet_id": r["outlet_id"],
                "outlet_name": r["outlet_name"],
                "jurisdiction": r["jurisdiction"],
                "eligibility_status": r["eligibility_status"],
                "analysis_tier": r["analysis_tier"],
                "core_inclusion": r["core_inclusion"],
                "website_active": r["website_active"],
                "institutional_form": r["institutional_form"],
                "flag_reasons": " | ".join(reasons),
                "source_file": r["source_file"],
                "source_row_number": r["source_row_number"],
            })
    return out


def jurisdiction_status_matrix(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    statuses = sorted({r["analysis_tier"] for r in rows})
    grouped: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        grouped[r["jurisdiction"]][r["analysis_tier"]] += 1
    out = []
    for jurisdiction in sorted(grouped):
        row = {"jurisdiction": jurisdiction}
        row.update({status: str(grouped[jurisdiction][status]) for status in statuses})
        row["total"] = str(sum(grouped[jurisdiction].values()))
        out.append(row)
    return out


def audit_summary(rows: list[dict[str, str]], host_groups, name_pairs, flags) -> list[dict[str, str]]:
    metrics = [
        ("records_audited", len(rows)),
        ("core_records", sum(r["core_inclusion"] == "yes" for r in rows)),
        ("shared_website_host_groups", len(host_groups)),
        ("possible_similar_name_pairs", len(name_pairs)),
        ("classification_flagged_records", len(flags)),
        ("distinct_institutional_form_strings", len({r["institutional_form"] for r in rows})),
        ("distinct_eligibility_status_strings", len({r["eligibility_status"] for r in rows})),
        ("distinct_website_active_strings", len({r["website_active"] for r in rows})),
    ]
    return [{"metric": k, "value": str(v)} for k, v in metrics]


def main() -> None:
    rows = read_rows()
    host_groups = shared_website_groups(rows)
    name_pairs = similar_name_pairs(rows)
    flags = classification_flags(rows)

    write_csv("shared_website_host_review_v1.csv", host_groups, [
        "website_host", "n_records", "outlet_ids", "outlet_names", "jurisdictions",
        "eligibility_statuses", "institutional_forms", "review_type", "review_instruction",
    ])
    write_csv("similar_name_review_v1.csv", name_pairs, [
        "outlet_id_a", "outlet_name_a", "jurisdiction_a", "outlet_id_b", "outlet_name_b",
        "jurisdiction_b", "name_similarity", "same_website_host", "review_type",
    ])
    write_csv("classification_flags_v1.csv", flags, [
        "outlet_id", "outlet_name", "jurisdiction", "eligibility_status", "analysis_tier",
        "core_inclusion", "website_active", "institutional_form", "flag_reasons",
        "source_file", "source_row_number",
    ])
    write_csv("institutional_form_frequency_v1.csv", value_frequency(rows, "institutional_form"), ["institutional_form", "n"])
    write_csv("website_active_frequency_v1.csv", value_frequency(rows, "website_active"), ["website_active", "n"])
    write_csv("eligibility_status_frequency_v1.csv", value_frequency(rows, "eligibility_status"), ["eligibility_status", "n"])

    matrix = jurisdiction_status_matrix(rows)
    matrix_fields = ["jurisdiction"] + sorted({r["analysis_tier"] for r in rows}) + ["total"]
    write_csv("jurisdiction_status_matrix_v1.csv", matrix, matrix_fields)
    write_csv("audit_summary_v1.csv", audit_summary(rows, host_groups, name_pairs, flags), ["metric", "value"])

    print(f"Records audited: {len(rows)}")
    print(f"Shared-host review groups: {len(host_groups)}")
    print(f"Similar-name review pairs: {len(name_pairs)}")
    print(f"Classification flags: {len(flags)}")
    print(f"Audit outputs: {OUTDIR}")


if __name__ == "__main__":
    main()
