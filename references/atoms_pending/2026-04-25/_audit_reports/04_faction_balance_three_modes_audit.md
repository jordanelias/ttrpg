# Audit Report — `04_faction_balance_three_modes`

**Topic:** Faction Balance & Three-Mode Architecture (consolidated)
**Atoms audited:** 50
**Audit date:** 2026-04-25
**Method:** programmatic ID-presence + path-reference + drift-detection + targeted content scan; substantive-content claims flagged MANUAL-REVIEW.

## Recommendation: **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)**

## Checklist results

| status | check | detail |
|---|---|---|
| **MANUAL-REVIEW** | Three-mode architecture is described once authoritatively. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Simulation methodology and result claims are reproducible (params/inputs documen | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | §6.5 framework propagation gaps are real gaps, not artifacts of partial source v | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Companion-deliverable references (`faction_balance_audit_2026-04-25.md`, `balanc | Requires substantive content reading; programmatic audit cannot conclude. |

## ID-presence verification

| kind | known in canon | unknown (new) | unknown IDs |
|---|---|---|---|
| ED | 1 | 1 | ED-706 |
| PP | 1 | 2 | PP-540, PP-541 |

**3 canonical IDs referenced in atoms are NOT in the fetched canon registers.** Caveat: PP archive chunks were not accessible (canon/ has no archive subdir; index references "Archive chunks: 9" but they aren't at expected paths). Some "unknown" PP IDs may exist in unfetched archives. ED, T, M sets are believed complete (active + archive fetched).

## Path-reference audit

- Total path references in atoms: 4
- Unique paths referenced: 1
- Paths NOT verified against canon corpus: 1
- Sample unverified (require manual GH check):
  - `params/bg/victory.md` (referenced 4x)

## Intra-source drift (same source, multiple atoms per ID)

Multiple atoms within a single source discuss the same canonical ID. May indicate the source itself contains drift — review during ingestion.

| source | id | atom count | atoms |
|---|---|---|---|
| master_document_2026-04-25.md | PP-540 | 7 | 2-1-initial-factio, 2-2-monte-carlo-si, p1-essential-for-m, p3-designer-hygien, 6-2-strategic-laye, 6-5-framework-prop, 8-9-faction-balanc |
| master_document_2026-04-25.md | PP-541 | 6 | 2-2-monte-carlo-si, p1-essential-for-m, p3-designer-hygien, 6-2-strategic-laye, 6-5-framework-prop, 8-9-faction-balanc |

## Topic-specific findings

**simulation_coverage:**

```yaml
pp_540_refs: 7
pp_541_refs: 6
three_mode_mentions: 34
monte_carlo: 7
```

## Provenance

- Consolidated doc: `references/atoms_pending/2026-04-25/_consolidated/04_faction_balance_three_modes.md`
- Topic decomposition: `references/atoms_pending/2026-04-25/_topic_decomposition.yaml`
- Canon registers fetched: editorial_ledger.yaml + archive, patch_register_active.yaml + index, throughlines_meta.md + infill
