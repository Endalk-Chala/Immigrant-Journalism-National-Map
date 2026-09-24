# Phase 1B Canonical Evidence Log

## Purpose

`data/phase1b/enrichment_evidence_v1.csv` is the canonical evidence-level table for public institutional enrichment.

The three `priority_batch*.csv` files are retained as historical staging inputs. They should not be treated as the canonical analytical evidence layer.

## Unit of analysis

One row = one public source supporting one coded field for one outlet.

Multiple rows may support the same outlet/field combination. This is intentional.

## Fields

- `evidence_id` — stable evidence-row identifier.
- `outlet_id` — joins to the frozen national outlet frame.
- `organization_id` — optional parent/organization identifier; blank where not yet established.
- `field_name` — Phase 1B enrichment variable.
- `coded_value` — value supported by the evidence row.
- `evidence_text` — concise human-readable statement of what the source supports.
- `source_url` — public source.
- `source_type` — source category from the Phase 1B source hierarchy.
- `evidence_date` — publication/update date only when actually established.
- `date_checked` — date the source was checked; blank for migrated legacy rows where the batch did not preserve this metadata.
- `coding_confidence` — `high`, `medium`, `low`, or `requires_manual_review`.
- `notes` — ambiguity, migration, or adjudication note.
- `source_batch` / `source_row` — provenance back to the original staging file.

## Migration rule

Legacy batches contained some unquoted commas in free-text cells. The builder locates the evidence URL and reconstructs the coded value and evidence note rather than trusting fixed comma positions.

No missing evidence date, source-check date, organization ID, or confidence judgment is invented during migration.

All migrated rows begin as `requires_manual_review`. Step 2 of the data-collection workflow audits and adjudicates these records before they are used to update the canonical outlet-level enrichment table.

## Canonical workflow

1. collect or migrate source-level evidence;
2. store it in `enrichment_evidence_v1.csv`;
3. audit controlled values and source interpretation;
4. mark confidence and evidence/check dates;
5. use approved evidence to populate `institutional_enrichment_v1.csv`.

The frozen national mapping dataset remains unchanged.
