# Exhaustive Review — Master Summary

**Generated:** 2026-04-25
**Method:** strict primary-register ID definition check (format-aware: YAML `id:` for ED/PP, table-row/heading for T/M) + repo path verification + best-match canon excerpts for substantive claims.
**Canon corpus:** 84 files (2.32 MB) covering 87 atom-referenced paths (3 missing).

## Per-topic recommendations

| topic | atoms | DEFINED | MENTIONED | PARTIAL | NEW | matched | unmatched | missing-paths | recommendation |
|---|---|---|---|---|---|---|---|---|---|
| `01_throughlines_meta` | 22 | 30 | 2 | 0 | 1 | 43 | 7 | 0 | **INGEST-WITH-NEW-REGISTRATIONS — 1 new IDs to register: ED-543.** |
| `02_solmund_cultural_guide` | 32 | 0 | 0 | 0 | 0 | 40 | 5 | 0 | **NO-IDS — recommendation hinges on substantive claim review (40 matched / 5 unmat** |
| `03_threadwork_design` | 71 | 9 | 19 | 0 | 0 | 103 | 34 | 1 | **CANONICAL-PROMOTION-NEEDED — 19 IDs mentioned in canon but not in primary regist** |
| `04_faction_balance_three_modes` | 50 | 2 | 3 | 0 | 0 | 64 | 5 | 0 | **CANONICAL-PROMOTION-NEEDED — 3 IDs mentioned in canon but not in primary registe** |
| `05_v2_historicity_correction` | 9 | 0 | 0 | 0 | 0 | 14 | 3 | 0 | **NO-IDS — recommendation hinges on substantive claim review (14 matched / 3 unmat** |
| `06_mechanical_review_audit` | 83 | 2 | 27 | 0 | 0 | 126 | 13 | 1 | **CANONICAL-PROMOTION-NEEDED — 27 IDs mentioned in canon but not in primary regist** |
| `07_audit_s1_s7_synthesis` | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **NO-IDS — recommendation hinges on substantive claim review (1 matched / 0 unmatc** |
| `08_session_consolidation` | 19 | 1 | 7 | 0 | 0 | 33 | 7 | 1 | **CANONICAL-PROMOTION-NEEDED — 7 IDs mentioned in canon but not in primary registe** |
| `09_canon_rectification_pp675_ed783` | 18 | 11 | 2 | 0 | 0 | 27 | 2 | 1 | **INGEST-WITH-PATH-FIXES — 1 repo paths missing.** |
| `10_session_log_index` | 10 | 48 | 2 | 0 | 0 | 14 | 0 | 0 | **STANDARD-INGESTION — IDs defined; ingest with verification.** |

## Cross-topic totals

- **Total ID instances:** 166
  - DEFINED: 103 (62%)
  - MENTIONED: 62 (37%)
  - PARTIAL: 0 (0%)
  - NEW: 1 (0%)
- **Substantive claims:** 541 (465 matched, 76 unmatched)
- **Missing repo paths:** 4

## Cross-topic findings

### Finding 1 — Most atom IDs are MENTIONED, not DEFINED

Across all 10 topics, only 62% of canonical IDs are formally defined in their primary register; 37% appear elsewhere in canon (commit logs, archives, cross-doc references) but are not in editorial_ledger / patch_register / throughlines_meta as primary entries.

Implication: a substantial share of atom-referenced IDs need **canonical promotion** — formalize them into their primary register — before content ingestion can build on them. This is a necessary Stage 4 prerequisite, not a Stage 5 archive task.

### Finding 2 — Path orphans concentrate in 4 topics

3 unique repo paths are missing across 87 referenced. They surface in topics 03, 06, 08, 09 because those topics frequently reference the same paths:
- `designs/architecture/core_experiential_moments.md`
- `designs/architecture/derived_stats_v30.md`
- `references/censured_vocabulary.yaml`

Either the atoms reference docs that haven't been created (proposal stage) or the paths drifted (file moved/renamed). Each Stage 4 ingestion of these topics must resolve.

### Finding 3 — Topic 01 has 1 NEW ID (ED-543)

ED-543 referenced in master_consolidation atoms but not in editorial_ledger active or archive. Possibilities: (a) typo for a different ED, (b) ID assigned but never registered, (c) was struck pre-archive. Stage 4 must register or reconcile.

### Finding 4 — Solmund (02) and v2 historicity (05) have zero canonical IDs

Both are content-driven, not ID-anchored. Their reviews hinge entirely on substantive claim matching. Topic 02 (Solmund) has 18 unmatched claims worth deeper review (many are PROVISIONAL setting/character claims requiring Jordan editorial). Topic 05 has only 1 unmatched claim — mostly aligned with existing audit canon.

## Caveats

- **PP archive chunks unavailable** — `patch_register_index.md` references "Archive chunks: 9" but archives weren't in `canon/`. Some "MENTIONED" PPs may be DEFINED in unfetched archives.
- **Substantive claim matching is keyword-overlap, not semantic.** "no-match" doesn't prove a claim is genuinely new.
- **Per-atom claim cap = 3.** Bounded extraction; deep audits should re-extract per-claim.
- **PARTIAL classification is conservative** — triggers when atom_chars > canon_chars + 100. Some PARTIAL items may already be fully canonized.
- **Topic 02 (Solmund) is editorial-judgment content** — programmatic review confirms structural validity but cannot resolve setting/character decisions; that requires Jordan.
