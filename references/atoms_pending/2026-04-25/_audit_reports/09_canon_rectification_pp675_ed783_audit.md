# Audit Report — `09_canon_rectification_pp675_ed783`

**Topic:** Canon Rectification PP-675 / ED-783 (consolidated)
**Atoms audited:** 18
**Audit date:** 2026-04-25
**Method:** programmatic ID-presence + path-reference + drift-detection + targeted content scan; substantive-content claims flagged MANUAL-REVIEW.

## Recommendation: **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)**

## Checklist results

| status | check | detail |
|---|---|---|
| **MANUAL-REVIEW** | PP-675 final spec matches whatever landed in canon/patch_register_active.yaml. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | ED-783 statement matches canon/editorial_ledger.yaml. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Outstanding Work (§10) cross-checked against current next_action queue. | Requires substantive content reading; programmatic audit cannot conclude. |
| **MANUAL-REVIEW** | Censured Vocabulary list (§2) is the authoritative one. | Requires substantive content reading; programmatic audit cannot conclude. |

## ID-presence verification

| kind | known in canon | unknown (new) | unknown IDs |
|---|---|---|---|
| ED | 6 | 1 | ED-783 |
| M | 1 | 0 |  |
| PP | 0 | 1 | PP-675 |
| T | 4 | 0 |  |

**2 canonical IDs referenced in atoms are NOT in the fetched canon registers.** Caveat: PP archive chunks were not accessible (canon/ has no archive subdir; index references "Archive chunks: 9" but they aren't at expected paths). Some "unknown" PP IDs may exist in unfetched archives. ED, T, M sets are believed complete (active + archive fetched).

## Path-reference audit

- Total path references in atoms: 70
- Unique paths referenced: 32
- Paths NOT verified against canon corpus: 22
- Sample unverified (require manual GH check):
  - `canon/02_canon_constraints.md` (referenced 7x)
  - `canon/00_philosophical_foundations_rules.md` (referenced 5x)
  - `canon/01_foundations_amendment_self_rendering.md` (referenced 6x)
  - `references/censured_vocabulary.yaml` (referenced 2x)
  - `canon/editorial_ledger_summary.yaml` (referenced 2x)
  - `references/file_index_summary.md` (referenced 1x)
  - `canon/README.md` (referenced 2x)
  - `canon/editorial_ledger_index.md` (referenced 2x)

## Intra-source drift (same source, multiple atoms per ID)

Multiple atoms within a single source discuss the same canonical ID. May indicate the source itself contains drift — review during ingestion.

| source | id | atom count | atoms |
|---|---|---|---|
| valoria_session_2026_04_25_master_consol | ED-783 | 5 | preamble, 1-scope, 9-verification-sta, 10-outstanding-wor, 14-references |
| valoria_session_2026_04_25_master_consol | PP-675 | 3 | preamble, 9-verification-sta, 14-references |
| valoria_session_master_2026-04-25.md | ED-667 | 2 | context-window-3-e, status |
| valoria_session_master_2026-04-25.md | ED-717 | 2 | context-window-3-e, status |
| valoria_session_master_2026-04-25.md | PP-675 | 2 | context-window-3-e, status |
| valoria_session_master_2026-04-25.md | M-4 | 2 | context-window-3-e, status |

## Topic-specific findings

**key_id_status:**

```yaml
PP-675_in_canon_active: false
ED-783_in_canon: false
```

## Provenance

- Consolidated doc: `references/atoms_pending/2026-04-25/_consolidated/09_canon_rectification_pp675_ed783.md`
- Topic decomposition: `references/atoms_pending/2026-04-25/_topic_decomposition.yaml`
- Canon registers fetched: editorial_ledger.yaml + archive, patch_register_active.yaml + index, throughlines_meta.md + infill
