# Consolidation Execution Log — 2026-07-01

## Status: FROZEN at PR open (2026-07-01)

Step → commit → result record for the month-overview + architecture-consolidation session.
The decision queue is `decision_queue.md`; stale-truth fixes are itemized in
`02_truth_reconciliation_log.md`; the ingested workflow spec is under `inputs/`.

| Step | Scope | Commit(s) | Result |
|---|---|---|---|
| 1 | LB-21 ID re-block: `verified_live_max.ED` 1042→1080; ED 1081-1087 allocated from block D; Round-3 block E provisioned (id_reservations v3) | `75dedcc` | done |
| 2 | Month-overview artifact skeleton (this folder) | `999c5dd` | done |
| 3 | Revive `broken_dependency_checker` (.jsonl path; live-status scope; restructure-ledger resolution) + `.githooks/pre-commit` tracked mode 100644→100755 (ED-1081) | `9039334` | done — 0 broken, 8 INFO legacy paths |
| 4 | Truth reconciliation: CLAUDE.md §6 two falsified claims, CURRENT.md, HANDOFF.md, patch-register header (+ propagation_map Class-E note per co-file rule) (ED-1082) | `650dda6` | done |
| 5 | Workflow-spec ingest (verbatim, `inputs/`) + `designs/architecture/holonic_container_doctrine_v1.md` PROPOSED (ED-1083) | `25e9216` | done — doctrine awaits Jordan |
| 6a | Cleanup: orchestrator maintenance pointers repointed; session-log machinery → `deprecated/session_machinery/`; size-check entries dropped; lane_assignments annotated (ED-1084) | `e8b232c` | done — post-move dependency check clean |
| 6b | Centralization: Combat Pool collapsed to `max(5, History+6)` across every live stale site; 4 Revision-2 compilations banner-flagged (2 docs × 2 duplicate homes — queued); values_master QUARANTINED; names_index v2 proper-noun fold (mirror 23→83 names) (ED-1084, ED-1052) | `87df2cf` | done |
| 7a | Container de-leak: engine runtime numpy-free; σ-kernel via `sim.autoload.sigma_leverage`; combat-state kernel relocated verbatim into `combatant.py`; RNG contract → stdlib (ED-1085) | `d4b1463` | done — deterministic probes byte-identical; 400-fight batch within 2.5·SE; 854 tests green |
| 7b | `tools/ci_module_shape_check.py` + CI report-only + 5 unit tests (ED-1085) | `bef96e0` | done — 0 violations, 26 INFO constants |
| 8 | `tools/export_engine_params.py` → `references/engine_params/combat_engine_v1.json` (schema v1, 176 keys); **blocking** round-trip CI; CURRENT.md + module_contracts `typed_params` (advances ED-1052) | `46e6236` | done — idempotent |
| 9 | `contract-conformance` CI job (report-only; ~21 violations = ED-1051 backlog surfaced per-PR); CLAUDE.md §10 fable tier + relay patterns; workplan v5 **J-38** propagation-spec docket (ED-1086) | `d8d74db` | done |
| 10 | `tools/currency_consistency_check.py` (6 checks) + CI report-only + SessionStart banner + valoria_local + 7 unit tests (ED-1087) | `2e70ebc` | done — first run caught 12 (3 real, 9 → documented TZ grace) |
| 11 | Finalize: artifacts frozen; HANDOFF repointed; CURRENT re-stamped; `verified_live_max` → 1087; freshness `--update` + blocking flip; full gates; PR | _(final commits)_ | done |

## Deviations from the approved plan (all documented in ledger entries)

1. **Byte-identical whole-fight gate (step 7a)** — impossible by construction: the sanctioned
   Stage-1a single-source deliberately replaced the numpy RNG stream with stdlib (D0-2
   numpy-free mandate), so identical seeds draw different streams. The gate split:
   deterministic kernel functions byte-identical (verified) + distributional equivalence on
   the stochastic path (same Normal(μ·N, σ·√N), identical TN tables, 400-fight aggregate
   within 2.5·SE). The plan's revert clause targeted behavioral divergence, which this is not.
2. **Ledger live-entry paths (step 3)** — the plan's B1 triage anticipated fixing broken refs
   in the ledger; the append-only audit-trail discipline makes rewriting live entries a
   Jordan canon edit instead. The checker resolves legacy paths through
   `references/restructure_ledger.md` (INFO, not violations); the 7 affected entries are
   queued (decision_queue #23).
3. **Combat Pool sites** — the sweep found more live sites than planned (params/fieldwork.md
   PP-615 note, companion spec, EXECUTIVE_GUIDE, and the four duplicated Revision-2
   compilations); all fixed/bannered, and the duplicate-home question queued (#22).
4. **names_index attribute mirror** — already existed (exploration overstated the gap); the
   fold-in delivered the proper-noun corpus instead, per the file's own MIGRATION note.
