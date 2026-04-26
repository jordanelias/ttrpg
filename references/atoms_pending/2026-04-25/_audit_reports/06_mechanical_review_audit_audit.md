# Audit Report — `06_mechanical_review_audit`

**Topic:** Mechanical Review & Audit Record (consolidated)
**Atoms audited:** 83
**Audit date:** 2026-04-25
**Method:** programmatic ID-presence + path-reference + drift-detection + targeted content scan; substantive-content claims flagged MANUAL-REVIEW.

## Recommendation: **SUB-DECOMPOSE-RECOMMENDED (83 atoms; sub-split by section family before canon decisions)**

## Checklist results

| status | check | detail |
|---|---|---|
| **MANUAL-REVIEW** | Sections are non-overlapping or overlap is justified. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Mechanical specs match existing designs/ where applicable; new specs are flagged | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | No internal contradictions across sections. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Open Decisions Requiring Jordan (II.2) listed as decision points, not as resolve | Requires substantive content reading; programmatic audit cannot conclude. |

## ID-presence verification

| kind | known in canon | unknown (new) | unknown IDs |
|---|---|---|---|
| ED | 1 | 8 | ED-129, ED-131, ED-200, ED-295, ED-297, ED-618, ED-670, ED-694 |
| PP | 1 | 18 | PP-233, PP-238, PP-239, PP-246, PP-251, PP-285, PP-294, PP-402, PP-508, PP-512 (+8 more) |
| TC | 0 | 1 | TC-01 |

**27 canonical IDs referenced in atoms are NOT in the fetched canon registers.** Caveat: PP archive chunks were not accessible (canon/ has no archive subdir; index references "Archive chunks: 9" but they aren't at expected paths). Some "unknown" PP IDs may exist in unfetched archives. ED, T, M sets are believed complete (active + archive fetched).

## Path-reference audit

- Total path references in atoms: 4
- Unique paths referenced: 4
- Paths NOT verified against canon corpus: 3
- Sample unverified (require manual GH check):
  - `params/core.md` (referenced 1x)
  - `params/combat.md` (referenced 1x)
  - `designs/architecture/derived_stats_v30.md` (referenced 1x)

## Provenance

- Consolidated doc: `references/atoms_pending/2026-04-25/_consolidated/06_mechanical_review_audit.md`
- Topic decomposition: `references/atoms_pending/2026-04-25/_topic_decomposition.yaml`
- Canon registers fetched: editorial_ledger.yaml + archive, patch_register_active.yaml + index, throughlines_meta.md + infill
