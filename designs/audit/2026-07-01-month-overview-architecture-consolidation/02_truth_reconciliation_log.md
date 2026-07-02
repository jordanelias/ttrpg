# Truth Reconciliation Log — 2026-07-01

## Status: FROZEN at PR open (2026-07-01) — all 14 rows executed; see 01_consolidation_execution.md for commits

Every stale/falsified claim found by the month-overview exploration, with its fix. All were
verified against the working tree before fixing (never from memory or a filename).

| # | Stale claim | Where | Reality (verified) | Fix (step) |
|---|---|---|---|---|
| 1 | "The four `designs/godot/*.md` docs have no supersession banner" | CLAUDE.md §6 | All four carry `⚠️ STALE / PARTIALLY SUPERSEDED` banners since 2026-06-30 (ED-1054) | 4 |
| 2 | "`combat_config.gd` hand-edits `adef_threshold` away from the oracle … parity cannot go green" | CLAUDE.md §6 | ED-1050 resolved (Jordan, 2026-06-30, PR #40): oracle re-swept monotone, port re-exported — they match. Parity still red, but only because RESIST/GAP_EXPOSURE are not yet re-exported | 4 |
| 3 | "Last reconciled: 2026-06-28" while row 29 was edited 07-01; combat merge + contest_rebuild absent | CURRENT.md | PR #40/#47 merged 06-30→07-01; contest_rebuild Gate 0 ratified 06-30 (ED 1055-1079 / PP 800-809 reserved) | 4, re-stamp 11 |
| 4 | "ED ceiling 1042" in Next-actions header | HANDOFF.md | Ledger max ED-1080; block D had 1081-1099 free; round-3 blocks now provisioned | 4 (after step 1) |
| 5 | "validate_ed_citations still needs its blocking flip (315 violations)" | HANDOFF.md LB-23 bullet | Blocking since 2026-06-29 with 0 genuine violations (valoria-ci.yml:273-276) | 4 |
| 6 | `# Next PP number: 724` | canon/patch_register_active.yaml:3 | Body contains PP-724/725/726 → next is 727 | 4 |
| 7 | `check_editorial_ledger()` reads `canon/editorial_ledger.yaml` | tools/broken_dependency_checker.py:88 | File doesn't exist (real: `.jsonl`); check silently returned `[],[]` since inception — dead gate | 3 (ED-1081) |
| 8 | `.githooks/pre-commit` assumed active once `core.hooksPath` is set | CLAUDE.md §8 / .githooks | Tracked mode 100644 (non-executable): git ignores it on every fresh clone — local advisory tier silently dead | 3 (ED-1081) |
| 9 | `verified_live_max.ED: 1042` "verified this session" | references/id_reservations.yaml | Same file's block D showed next_free 1081; ledger max 1080 — internal contradiction | 1 (LB-21) |
| 10 | "Maintained by: valoria-orchestrator skill" | references/glossary.md (header + footer), designs/provincial/clock_registry_v30.md:116, params/history/{combat,threadwork,board_game}.md:3 | Skill retired to deprecated/skills/ 2026-06-28 (LB-22) — maintenance mechanism no longer exists | 6 |
| 11 | ~70 values indexed under `params/combat.md`; 8 under `params/threadwork_superseded.md`; STRUCK pool formula presented live | references/values_master.yaml | `params/combat.md` does not exist; superseded file feeding "master" registry; generator `extract_values.py` dead (legacy imports) | 6 (quarantine, ED-1052) |
| 12 | Combat Pool `(Agility × 2) + History + 3` presented as current | params/core.md:161; skills/valoria-combat-simulator/references/combat_params.md:27; designs/scene/combat_design_v1.md + combat_v30_infill.md; analogy cites in social_contest_v30.md / social_contest_system_v2.md | Canonical since 2026-05-29 R1 (ED-901, re-ratified ED-900/904): `pool = max(5, History + 6)`, Agility-independent | 6 (ED-1052/ED-1084) |
| 13 | "All modules are stubs" | sim/README.md | 66 modules, 19 stubbed; mc_v18 runs full campaigns (both README and CLAUDE.md §7 flag their own staleness in place) | noted; README self-caveat already present — text corrected in step 4's CLAUDE.md pass only where load-bearing |
| 14 | 12 stale `canonical_sha__` pins | references/canonical_sources.yaml | Real content drift surfaced by the now-local freshness gate (ED-1053 residual) | 11 (`--update` + blocking flip) |
