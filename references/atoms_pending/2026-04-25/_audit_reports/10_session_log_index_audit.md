# Audit Report — `10_session_log_index`

**Topic:** Session Log Index 2026-04-25 (consolidated)
**Atoms audited:** 10
**Audit date:** 2026-04-25
**Method:** programmatic ID-presence + path-reference + drift-detection + targeted content scan; substantive-content claims flagged MANUAL-REVIEW.

## Recommendation: **INDEX-ONLY (verify ID presence; no canon ingestion expected)**

## Checklist results

| status | check | detail |
|---|---|---|
| **MANUAL-REVIEW** | Every ED listed in commit-manifest atoms exists in canon/editorial_ledger.yaml. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Every PP listed exists in canon/patch_register_active.yaml or an archive. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Stress-test results (Section 4) referenced from session-log atoms point at simul | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | P1 resolutions claimed are reflected in current p1_blocker_count. | Requires substantive content reading; programmatic audit cannot conclude. |

## ID-presence verification

| kind | known in canon | unknown (new) | unknown IDs |
|---|---|---|---|
| ED | 47 | 0 |  |
| PP | 1 | 2 | PP-195, PP-197 |

**2 canonical IDs referenced in atoms are NOT in the fetched canon registers.** Caveat: PP archive chunks were not accessible (canon/ has no archive subdir; index references "Archive chunks: 9" but they aren't at expected paths). Some "unknown" PP IDs may exist in unfetched archives. ED, T, M sets are believed complete (active + archive fetched).

## Path-reference audit

- Total path references in atoms: 14
- Unique paths referenced: 11
- Paths NOT verified against canon corpus: 6
- Sample unverified (require manual GH check):
  - `designs/architecture/conflict_architecture_proposal.md` (referenced 1x)
  - `params/bg/victory.md` (referenced 1x)
  - `designs/provincial/baralta_crown_claim_v30.md` (referenced 1x)
  - `params/bg/tensions_deck.md` (referenced 1x)
  - `params/bg/royal_assassination.md` (referenced 1x)
  - `params/bg/phases.md` (referenced 1x)

## Provenance

- Consolidated doc: `references/atoms_pending/2026-04-25/_consolidated/10_session_log_index.md`
- Topic decomposition: `references/atoms_pending/2026-04-25/_topic_decomposition.yaml`
- Canon registers fetched: editorial_ledger.yaml + archive, patch_register_active.yaml + index, throughlines_meta.md + infill
