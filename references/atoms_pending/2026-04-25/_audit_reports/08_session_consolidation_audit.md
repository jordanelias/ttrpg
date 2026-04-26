# Audit Report — `08_session_consolidation`

**Topic:** Session Consolidation 2026-04-25 (consolidated)
**Atoms audited:** 19
**Audit date:** 2026-04-25
**Method:** programmatic ID-presence + path-reference + drift-detection + targeted content scan; substantive-content claims flagged MANUAL-REVIEW.

## Recommendation: **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)**

## Checklist results

| status | check | detail |
|---|---|---|
| **MANUAL-REVIEW** | Phase narrative (assessment → critique → ...) is coherent. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Recent canonical strikes (§2.4) cross-checked against actual commits. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Bridge-work claims (§2.1) cross-checked against current state. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Scale Transitions Zoom-In trigger families (§2.2) match current designs/. | Requires substantive content reading; programmatic audit cannot conclude. |

## ID-presence verification

| kind | known in canon | unknown (new) | unknown IDs |
|---|---|---|---|
| ED | 1 | 6 | ED-539, ED-545, ED-547, ED-577, ED-588, ED-663 |
| PP | 0 | 1 | PP-508 |

**7 canonical IDs referenced in atoms are NOT in the fetched canon registers.** Caveat: PP archive chunks were not accessible (canon/ has no archive subdir; index references "Archive chunks: 9" but they aren't at expected paths). Some "unknown" PP IDs may exist in unfetched archives. ED, T, M sets are believed complete (active + archive fetched).

## Path-reference audit

- Total path references in atoms: 1
- Unique paths referenced: 1
- Paths NOT verified against canon corpus: 1
- Sample unverified (require manual GH check):
  - `designs/architecture/core_experiential_moments.md` (referenced 1x)

## Provenance

- Consolidated doc: `references/atoms_pending/2026-04-25/_consolidated/08_session_consolidation.md`
- Topic decomposition: `references/atoms_pending/2026-04-25/_topic_decomposition.yaml`
- Canon registers fetched: editorial_ledger.yaml + archive, patch_register_active.yaml + index, throughlines_meta.md + infill
