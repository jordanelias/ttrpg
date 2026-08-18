# Culling plan v1 — remove the apparatus that audits the apparatus

## Status: RATIFIED AS PLAN OF RECORD (Jordan, 2026-08-18) — waves execute individually; §5 gates are hard

## Date: 2026-08-18 · Lane: IN (cross-cutting) · ED: ED-IN-0194

**No new ED was allocated.** `registers/editorial_ledger_in.jsonl` has **108 tokens of headroom**
under a blocking cap (ED-IN-0185 Q5, overdue). Allocating a row would block the commit. The plan's
thesis, arriving on schedule.

**The governing rule (Jordan, 2026-08-18):**

> *If the script/tool/whatever is recursive — guardrails for guardrails, audit prose about audit
> prose about audit prose — then that is worthless. If it doesn't directly concern the code base or
> design documents or the first layer of compliance and organization, ie if it isn't a primary
> guardrail, then it's likely useless.*

Supporting direction, same session: *"We need as little as possible"* · *"keep the actual code shape
and data management as simple and lean as possible with the actual code itself holding complexity as
required"* · *"a sharply cut and explicit centralized system where all terms, glossary definitions,
values, etc are stored in single locations."*

---

## 1. The decision procedure

Stated as an algorithm so a later session reaches the same verdict without re-litigating it.

For any artifact **A**, ask in order:

1. **What is A's SUBJECT?** Not what A does — what A is *about*.
   - the game engine, or a design document → **layer 1**
   - a layer-1 artifact → **layer 2**
   - a layer-2 artifact or higher → **layer 3+**
2. **Verdict by layer.**
   - **Layer 1 → P (PRIMARY).** Keep. A defect here is a defect in the game.
   - **Layer 2 → O or R.** Keep **only** if it is the *first and only* layer-2 artifact for its
     rule — the first layer of compliance and organization. A second layer-2 artifact enforcing the
     same rule is a **merge target**, not a keeper (CLAUDE.md §8: every rule lives once).
   - **Layer 3+ → R (RECURSIVE).** Delete. Worthless regardless of build quality, test coverage, or
     how recently it was written.
3. **Zero callers, or subject retired → D (DEAD).** Delete regardless of layer.

**Two corollaries that decide most hard cases:**

- **A tool that cannot fail is not a guardrail.** `ci_supersession_check` returns 0 on every path
  and its own registry row says so. It is R by construction.
- **A tool whose only consumers are R-tier tools is R**, transitively. This is what makes the waves
  ordered: deleting the consumer first turns the producer into D, which is a cheaper deletion.

**One thing the rule deliberately does not protect:** build quality. `test_wf_harness.py` is
mutation-verified, 13/13 mutants killed — and it guards the prelude of the scripts that run audits.
Layer 4. It dies. Excellence at layer 4 is the most expensive kind of waste, because it is the
hardest to argue with.

---

## 2. Measured shape (working tree, 2026-08-18)

| surface | lines | note |
|---|---:|---|
| **Game engine** `engine/` + `systems/*/sim/` | **29,570** | the thing |
| **Design docs + canon** `systems/**.md`, `canon/` | **57,732** | the thing |
| `audit/` | 179,002 | 98,763 machine JSON; 339 files, ~50 units |
| generated + tracked in `references/` | 100,830 | every one regenerable |
| `tools/observability/` | 36,262 | prose about process prose |
| `deprecated/` | 11,280 | retired 2026-08-05 |
| `registers/handoffs/` + root | 7,230 | `HANDOFF_IN.md` = 3,485 |
| `tools/sim_harness/` | 4,220 | 28 files, **zero callers** |
| apparatus tests in `tests/valoria/` | 9,981 | 41 files |

**87,302 lines are the game. ~338,000 are about the game — a 3.9:1 inversion.**
`tests/valoria` splits **81 files game / 81 files apparatus**; by authored test functions,
**852 tooling vs 573 game.**

**Two files are 46% of `audit/`:** `2026-07-26-mass-battle-vector-audit` (57,772) and
`2026-08-06-vector-audit` (24,999). Both are machine lens-output, not prose anyone reads.

---

## 3. The recursion chains — evidence for the verdicts

Depth measured. Layer 1 = checks the game or a design doc.

**Chain 1 — the test-register stack, depth 5.**
`game code` → `tests/valoria` game tests **(L1)** → `build_test_register.py` writes
`references/test_register.json`, a registry *of* the tests **(L2)** → `--check` gates the registry's
freshness in CI and locally **(L3)** → `test_test_register.py` tests the register tool **(L4)** →
`ci_gate_coverage.py` verifies the `--check` line is present in the workflow, and
`test_gate_coverage.py` tests that **(L5)**. Four layers exist so a JSON nobody plays the game with
stays fresh. **12,514 lines of tracked JSON at the base of it.**

**Chain 2 — the apparatus inventory, depth 4.**
checkers **(L1/L2)** → `build_apparatus_registry.py` inventories them **(L3)** →
`test_compile_is_not_invocation.py` + `test_oi12_orphan_census.py` test the inventory's orphan
semantics **(L4)** → `audit-refresh.yml` regenerates it weekly and `test_audit_refresh_coverage.py`
tests that the workflow regenerates it **(L4)**.

**Chain 3 — the ratchet stack, depth 4.**
checkers emit signals **(L2)** → `review_core.py` grades them against `review_baseline.yaml` **(L3)**
→ `dashboard_data.py` renders the grade; `test_status_reader_one_owner.py` tests that the dashboard
reads status through one owner **(L4)**. Parallel: `scope_ratchet.py` meters *counts of process
artifacts* (open EDs, proposals) — a meter of the ledger of the process **(L3–4)**.

**Chain 4 — wiring verification, depth 4.**
validators **(L1/L2)** → `ci_hooks_verifier.py` checks they are wired **(L3)** →
`ci_gate_coverage.py` checks the workflow ran them **(L3)** → `test_gate_coverage.py` and
`test_blocking_tier_is_honest.py` — *a test that the blocking tier's membership is honest* **(L4)**.

**Chain 5 — orchestration guardrails, depth 4, entirely off-game.**
`.claude/wf_*.js` run audits **(L2)** → `tools/wf_harness.js` is the copied prelude **(L3)** →
`ci_wf_harness_check.py` verifies the copy is byte-identical **(L3)** → `test_wf_harness.py` (23
defs, executed under node) + `test_wf_harness_check.py` (20 defs) **(L4)**. **43 tests guarding the
guardrail of the scripts that orchestrate the audits.**

**Chain 6 — the digest stack.**
ledgers (process prose) → `build_decisions` / `build_proposals` / `build_incompleteness` /
`build_graph` / `build_lexicon` generate `DECISIONS.md` / `PROPOSALS.md` / `INCOMPLETENESS.md` /
console — prose about process prose **(L3)** → `audit-refresh.yml` regenerates weekly and opens PRs
about it → `dashboard.yml` regenerates again → `audit_staleness.py` reports when the digests are
stale **(L4)**, and the workflow's own comment concedes it "will keep reporting stale. That is
honest." **A tool whose steady state is reporting that other reports are old.**

**Chain 7 — the retirement stack.** `evacuation_plan.py` classifies files for an operation that
**completed 2026-08-05** → `test_evacuation_plan.py` (18 defs) → `single_owner_check.py` checks that
tools import owner modules **(L3)** → `test_single_owner_check.py` **(L4)**. Plus `build_fork.py`,
`join_audit_workings.py` — one-shot migration tools, still tested.

**Chain 8 — pure mirror.** CLAUDE.md §10's tier table → `tools/model_router.html` mirrors it **(L2)**
→ `test_model_router_ids.py` tests that the mirror matches **(L3)**.

---

## 4. The waves

Ordered so that each wave's deletions turn the next wave's targets from R into D. **Every caller is
edited in the same commit as its target.** After each wave: `pytest tests/valoria engine/tests`, the
surviving `valoria_local.py` list, and push — one wave per PR.

### Wave 1 — leaves (nothing outside the set consumes them) · ~45,000 lines

**Targets.** `tools/observability/` (36,262 — all 6 generators + every committed feed, `.md`, `.json`,
`_data.js`, html, `guide/`) · `dashboard/` + `tools/dashboard_data.py` + `tools/m1_acceptance.py` ·
`.github/workflows/dashboard.yml` · `.github/workflows/audit-refresh.yml` · `tools/sim_harness/`
(4,220, 28 files, **0 callers** — CLAUDE.md §3 already measured this) · `tools/dead_primitive_census.py`
(0 callers — *a census of dead apparatus*) · `tools/editorial_review/` (jsx, 0 callers) ·
`tools/model_router.html` · `tools/tag_normalizer.py`, `tools/valoria_rename.py` (0 callers) ·
skills `valoria-arc-generator` (subject `arcs/` evacuated), `valoria-simulator` (subject `sim/`
retired), `valoria-workplan-navigator` · every committed `__pycache__/*.pyc`.

**Tests deleted with them.** `test_build_proposals` · `test_build_glossary` · `test_observability_core`
· `test_status_reader_one_owner` · `test_model_router_ids` · `test_audit_refresh_coverage` ·
`test_compile_is_not_invocation` · `test_oi12_orphan_census`.

**Other same-commit edits.** Remove their rows from `references/ci_checks_registry.yaml`; CLAUDE.md
§3 (`dashboard/` row), §8 (observability paragraph), §9 (routing rows).

**Verify.** `grep -rl "observability\|dashboard_data\|sim_harness" .github .githooks tools/valoria_local.py`
returns nothing outside the deleted set.

**Rollback.** Single revert; nothing else depends on it.

### Wave 2 — meta-gates, now orphaned by wave 1 · ~8,000 lines

**Targets, with the caller line to edit.**

| target | callers |
|---|---|
| `build_apparatus_registry.py` + `references/apparatus_registry.{yaml,md}` (2,322) | wave-1 workflow gone; `ci_hooks_verifier:93`, `audit_staleness:128`, `dead_primitive_census:9` — all dying |
| `audit_staleness.py` | `session_open_work:18`, `dashboard_data:219` (gone), `ci_common:106` shim |
| `audit_registry.py` + `ci_audit_registry_check.py` | CI `validators-report`, `valoria_local:173` |
| `review_core.py` + `registers/review_baseline.yaml` | CI `compliance-check:411`, `.claude/settings.json` Stop hook, CLAUDE.md §9 |
| `scope_ratchet.py` + `registers/scope_baseline.yaml` | CI:191, `valoria_local:210` |
| `build_test_register.py` + `references/test_register.json` (12,514) | CI:111, `valoria_local:171` |
| `ci_supersession_check.py` (**cannot fail**) | CI:173, `valoria_local:163` |
| `wiring_map_check.py` + `references/wiring_manifest.yaml` | CI:183, `valoria_local:174` — fold the manifest into `module_contracts.yaml` first |
| `ci_program_claim_check.py`, `ci_vacuous_assertion_check.py`†, `ci_workplan_pointer_check.py` | CI:192–193, 182; `valoria_local:193` |
| `ci_register_size_check.py` | CI:100, `valoria_local:160` — **after** the §6 merge into `compliance_check` |
| `workplans/POINTER_*.md` (11 files, 5 already pointing at deleted dirs) | `ci_workplan_pointer_check`, dying with them |

† see §5.6 — `ci_vacuous_assertion_check` is held pending the §0.1 ruling.

**Tests deleted.** `test_test_register` · `test_ci_supersession_check` · `test_scope_ratchet` ·
`test_program_claim_check` · `test_vacuous_assertion_check`† · `test_wiring_map_check` ·
`test_known_red_register` **(⚠ NO — see §5.4)**.

**Verify.** `review_core --check` is removed from `compliance-check` *before* the tool is deleted, or
CI reds on a missing file.

### Wave 3 — wiring-checkers · ~5,000 lines

Must run **after** wave 2, or these red on subjects that no longer exist.

**Targets.** `ci_gate_coverage.py` — first rewrite `valoria_local.py` to drop `--ci` (lines 23–143)
and sever `broken_dependency_checker.py:33`'s import · `ci_hooks_verifier.py` — **only after §5.3** ·
`ci_wf_harness_check.py` + `tools/wf_harness.js` + `ci_claude_workflow_paths.py` + `.claude/wf_*.js`
+ `.claude/agents/valoria-critic.md` · `single_owner_check.py`.

**Tests deleted.** `test_gate_coverage` · `test_blocking_tier_is_honest` · `test_wf_harness` ·
`test_wf_harness_check` · `test_single_owner_check` · `test_handoff_structure` ·
`test_handoff_dispatch_validity` · `test_retired_tree_apparatus` (29 defs) · `test_retired_tree_scanner`
· `test_session_open_work`.

**Also in this wave** (session/process machinery): `session_status.py`, `session_handoff_reminder.py`,
`session_open_work.py`, `handoff_atomize.py`, `workplan_status.py` — edit `.claude/settings.json`
hooks in the same commit.

⚠ **Deleting `.claude/wf_*.js` and `valoria-critic` ends structurally-independent adversarial
review.** That is the mechanism that caught four errors in this session's own work. It is a real
capability, it is layer 4 by the rule, and the trade is Jordan's — see §5.7.

### Wave 4 — `audit/` → fork ref · ~172,000 lines

**Precondition, and the only expensive step in the plan: EXTRACT FIRST.** ~33 of ~50 units are
game-subject working papers. Their *surviving conclusions* belong in `systems/` heads or
`proposals/`; the workings do not.

**Extract before deleting** (non-exhaustive, verify each against `CURRENT.md` and the ledgers):
`2026-07-22-mass-battle-stress-test/{octagon_damage_model,rotation_model_v1,geometric_contact_proposal_v1,ratified_but_unbuilt_backlog}.md`
· `2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (**RATIFIED and
CURRENT.md-referenced — this one must move, not fork**) · the contest gate packets ·
`2026-08-08-world-churn-audit` (backs 9 open Jordan decisions) · `2026-08-14-degree-reband-consumer-cost/reband_delta.py`
· `2026-08-12-degree-vocabulary-census`.

**Delete outright, no extraction** — the 17 repository-subject units:
`2026-07-08-fable5-four-modes-review` · `2026-07-08-open-items-jordan-decision-docket` ·
`2026-07-12-pr119-harness-verification` · `2026-07-13-multi-agent-audit` (an audit *of the audit
apparatus*) · `2026-07-21-repo-state-vector-audit` · `2026-07-30-mb-session-retrospective` (pure
session narrative) · `2026-08-05-repo-analysis-sweep` · `2026-08-06-vector-audit` (24,999, machine
output) · `2026-07-26-mass-battle-vector-audit` (57,772, machine output) ·
`2026-08-10-subsystem-atlas-verification` · `2026-08-11-code-leanness` · `2026-08-11-consolidation-sweep`
· `2026-08-11-divergence-audit` · `2026-08-11-systems-python-architecture-audit` ·
`2026-08-12-alias-index-consolidation` · `2026-08-13-fork-divergence-harness` ·
`2026-08-14-five-lens-repo-assessment` · `2026-08-17-weekly-review` (**this session's own**).

**Nesting depth 3 confirmed:** `2026-08-17-weekly-review/vector_audit/03_validation_report.md` is a
validation report *of* that unit's own weakness register, inside a review whose subjects include
prior audits.

**Method.** Fork ref, matching the 2026-08-05 precedent (`c451bcb`): tag, push the tag, delete from
`main`, add `FORK:` rows to `references/restructure_ledger.md` so citations resolve. **Nothing is
destroyed.**

**Verify before deleting.** `grep -rl "audit/2026-" --include=*.py tests/ tools/ engine/ systems/` —
`test_fork_divergence.py` imports `audit/2026-08-13-fork-divergence-harness/fork_divergence.py` and
`tests/sim/v32-combat-balance/` is a frozen parity oracle. Both must be resolved first.

### Wave 5 — untrack generated data · ~101,000 lines

**Targets** (generator in brackets; all verified present):
`references/glossary/` — `glossary.json` 68,469 + 20 views 6,838 [`build_glossary.py`] ·
`test_register.json` 12,514 [gone in wave 2] · `key_graph.json` 2,840 [`build_key_graph.py`] ·
`execution_map.json` 2,551 + `EXECUTION_MAP.md` + `execution_trace.json` [`build_execution_map.py`,
`trace_execution_phases.py`] · `engine_atlas.json` 1,983 + `ENGINE_ATLAS.md` 487
[`build_engine_atlas.py`] · `CONTRACT_INDEX.md` 1,464 + `KEY_INDEX.md` 1,185
[`build_contract_index.py`] · `definitions/definitions.yaml` 888 [`definitions_store.py`] · the 4
vocab views 1,069 [`vocab_store.py`] · `identifier_census.json` 99 · the 4 regenerable
`engine/engine_params/*.json`.

**The gate flip this requires.** Several freshness checks work by diffing the *committed* copy
against a fresh build (`vocab_store --check`, `definitions_store --check`, `test_engine_atlas`,
`test_test_register`, `test_build_glossary`). Untracking means flipping each to *build in CI, do not
diff a committed copy*. **One deliberate pass — not a silent `git rm`.**

**Standing proof this is right:** two sibling branches collided on 18 files "over nothing," every
conflict a generated file, zero in source (`HANDOFF_IN.md`). And three times in one session an edit
to *prose* staled `engine_atlas.json` and failed a blocking gate — once because the word "audit"
appeared one more time in a comment.

### Wave 6 — data consolidation · ~18,000 lines

**6a. `deprecated/` → fork** (11,280). **Blocked on 6b** — see §5.2.

**6b. Ledgers: 1,232 rows → ~260 open + one tombstone file.**
Verified: `validate_ed_citations.py:240-245,295` builds its known-ID map from `(id, status)` **only**;
no other field of a closed row is read by anything. So `registers/ed_tombstones.yaml` — one
`ED-XXXX: resolved` line each, ~1,150 entries — fully substitutes for every closed row **and** for
the `deprecated/archives/editorial*` files the checker currently keeps alive. Delete the 4 archive
`.jsonl` files and the 239 closed rows still sitting in live lane files. Rehome
`test_evacuation_plan.py`'s keep-pin into `test_ed_citation_integrity.py` in the same commit.

**6c. Handoffs: 7,230 → ~1,000.** ≥75% of `HANDOFF_IN.md` (3,485 lines) is narrative about completed
work — seven dated session retrospectives, `[DONE]`/`[RULED]` sections. Continuity is `git log`'s
job. New shape, one bullet per open item: `ED-ID — state — next action — blocked-on`. **Cap 100 lines
per lane**, enforced by the surviving size gate. Delete `HANDOFF_archive.md` (an archive of diaries).

**6d. Vocabulary → one file.** Fold `glossary.md` (305), `names_index.yaml` (294),
`descriptor_registry.yaml` (230), `proper_noun_registry.yaml` (481), `name_collision_database.yaml`
(508), `placeholder_names.yaml` (217), `action_vocabulary.yaml` (60), `scope_vocabulary.md` (48) into
`references/definitions/vocab_source.yaml` — which already declares itself the single source and
already has a fold mechanism (`vocab_store.py`). Views become untracked build products.
⚠ **Two blockers:** `restructure_ledger.md:1065-1067` records a standing Jordan ruling that folding
`name_collision_database.yaml` is "architecturally backwards" — needs re-ruling, not silent override.
And `names_index.yaml` is the enforcement source for the naming gate: repoint `ci_naming_check.py` /
`ci_names_consistency.py` in the same commit.

**6e. Contracts.** Fold `wiring_manifest.yaml` (132) into `module_contracts.yaml`.

**6f. Prose meta-registers → fork:** `references/{throughlines_meta*,id_reservations_history,canonical_sources_notes,canonical_sources_provenance}.md`,
`registers/{patch_register_index.md,editorial_ledger_migration_2026-05-28.md}`,
`references/splits/params_board_game_split.yaml` (maps the evacuated `engine/params/` tree),
`godot/{scene_tree_architecture,gm_to_engine_conversion,data_serialization_spec,implementation_sequence}.md`
(banner-stale since ED-1054, ship wrong schemas). Move `throughlines_complete.md` (377, a design
artifact) to `systems/_architecture/`.

---

## 5. Hard gates — verify before the wave that touches them

1. **`engine/engine_params/params_tables.yaml` is NOT regenerable.** Its 43 source docs were
   evacuated and `export_params_constants.py` exists nowhere in the tree — verified by grep across
   the whole repo including `deprecated/`. It is now a **source, not an artifact**. **KEEP TRACKED.**
   Excluded from wave 5. It is the only file in this state; every other generator was located.
2. **`deprecated/archives/editorial*` is read by `validate_ed_citations.py`.** Delete it before 6b's
   tombstone list lands and **every valid `ED-` citation reads as fabricated**. 6b gates 6a.
3. **`ci_hooks_verifier` Check 6 enforces CLAUDE.md §11** (no self-scheduling — a measured 116
   wake-ups / ~2.7M-token bleed). Before deleting, confirm `tests/valoria/test_no_polling_triggers.py`
   independently asserts all seven deny-list primitives. **Keep that test regardless.**
4. **`tests/sim/mass_battle/` is the canon engine, not a test suite** (Jordan ruling J2, 11,269 lines).
   **Never sweep it with tooling tests.** Likewise `test_degree_ladder_single_owner.py` matches
   apparatus name-patterns but is a **primary** guardrail on game dice logic — and
   `test_known_red_register.py` pins the 9 mass-battle known-reds. **Both keep.**
5. **`build_identifier_census`** — `validate_ed_citations.py:368` reads the census. Detach or confirm
   it degrades safely before deleting.
6. **`ci_claim_provenance_check` and `ci_vacuous_assertion_check` are literal encodings of CLAUDE.md
   §0.1 points 3 and 2.** By the rule in this plan's header they are recursive: they audit ledger
   prose and test code, not the game. Two independent lenses flagged them; neither would rule. **If
   they go, §0.1 must be struck in the same commit** rather than left pointing at deleted guards.
   **Jordan's call — held.**
7. **Wave 3 ends structurally-independent adversarial review.** `.claude/wf_*.js` + `valoria-critic`
   are the mechanism that caught four errors in this session's own work, including a refuted headline
   claim. Layer 4 by the rule; a real capability in fact. **Jordan's call — the rule says delete, the
   evidence says it works.**

---

## 6. Merges — one owner per rule (CLAUDE.md §8)

| survivor | absorbs | why |
|---|---|---|
| `ci_naming_check` | `ci_names_check`, `ci_names_consistency` | all three read `names_index.yaml`; survivor is the blocking one |
| `compliance_check` | `ci_register_size_check` | the cap is already single-sourced from `atomization_rules.yaml`; two bodies for one rule *is* the §8 violation |
| `currency_consistency_check` | `ci_generation_consistency`, `canon_coverage_check` | all three answer "is every canonical doc present, statused, current" |
| `broken_dependency_checker` | `freshness_gate` | both walk `canonical_sources.yaml`; §1 already rules the SHA pins advisory |
| `registry.py` | `vocab_store`, `definitions_store` readers | one owner for "what does this term mean" — the §4 ruling |

---

## 7. Keep

**Primary guardrails (P).** The 81 game files in `tests/valoria` · `engine/tests/` whole (the port
oracle) · `ci_golden_modes_check` (byte-exact shipped goldens) · `lanchester_signature` ·
`export_engine_params` / `export_key_types` / `export_sim_params` `--check` round-trips ·
`gen_sigma_parity_goldens` · `ci_sim_fabrication_check` (anti-fabrication on game numbers) ·
`ci_module_shape_check` · `contract_adjudicator`.

**First-layer organisation (O).** `validate_ed_citations` · `ci_pp_frozen_check` · `ci_naming_check`
+ `names.py` + `hook_naming_guard` · `ci_editorial_checker` · `ci_co_file_checker` ·
`currency_consistency_check` · `broken_dependency_checker` · `mechanics_index_gen` ·
`ci_quantity_vocabulary_check` + `registry.py` + `quantity_registry` + `descriptor_registry` ·
`compliance_check` · `valoria_local.py` (static list only) + `.githooks/pre-commit` · `ci_common.py`
· `pathres.py` · `build_key_graph`.

**Skills (9 of 13).** `valoria-dice-model` · `valoria-canon-guard` · `valoria-mechanic-audit` ·
`valoria-module-adjudicator` · `valoria-resolution-diagnostic` · `prose-writer` ·
`valoria-editorial-register` · `valoria-chunker` · `valoria-compiler`.
⚠ `valoria-vector-audit` (9,324 lines, the largest skill) survives **only** as an on-demand
instrument — its 183 tests and its observability feed do not.

**Data (single owner each).** `references/definitions/vocab_source.yaml` (terms) ·
`engine/engine_params/` (values, code-generated; `params_tables.yaml` frozen) ·
`references/module_contracts.yaml` (structure) · `references/canonical_sources.yaml` ·
`references/restructure_ledger.md` (load-bearing for every old citation) ·
`registers/mechanics_index.yaml` · `registers/{patch_register_active,supersession_register}.yaml` ·
`references/id_reservations.yaml` · `references/npc_registry.yaml` (canonical character data) ·
`CURRENT.md` · slim `HANDOFF.md` + lane files · `workplans/valoria_master_workplan_v6.md` + board ·
`CLAUDE.md`.

**CI after the cull:** `syntax-check` · `validators` · `validators-report` · `unit-tests` ·
`sim-regression` · `field-goldens` · `lanchester-signature` · `contract-conformance` ·
`compliance-check` · `ci-summary`. `dashboard.yml` and `audit-refresh.yml` gone.

---

## 8. Targets

| metric | now | after | Δ |
|---|---:|---:|---:|
| tracked non-code lines | ~490,000 | ~72,000 | **−85%** |
| `tools/` modules | 107 | ~24 | −78% |
| skills | 13 | 9 | −31% |
| workflows | 3 | 1 | −67% |
| `tests/valoria` files | 162 | ~90 | −44% |
| apparatus : game ratio | 3.9 : 1 | **0.5 : 1** | inverted |
| deepest recursion chain | 5 layers | **2** | |
| homes for a term | 14 | **1** | |

**Resulting repo:** ~29,600 lines of engine · ~58,000 of design and canon · ~10–14k of hand-authored
data in single-owner files · ~1,500 of continuity.

---

## 9. Risk register

| risk | likelihood | mitigation |
|---|---|---|
| A deleted tool was load-bearing in a way grep missed (dynamic import, subprocess by string) | medium | one wave per PR; full `pytest tests/valoria engine/tests` after each; fork ref makes every deletion recoverable |
| Extraction in wave 4 misses a live design artifact | **high** — the expensive risk | do wave 4 **last**; cross-check every unit against `CURRENT.md`, `mechanics_index.yaml` and open ledger rows before forking |
| Untracking wave 5 breaks a drift gate silently | medium | flip each gate in the same commit as its file; CI must be green *before* the `git rm --cached` |
| §0.1 left pointing at deleted guards | high if §5.6 is skipped | strike doctrine and tool in one commit, or keep both |
| Loss of adversarial review capability (§5.7) | certain if wave 3 runs in full | Jordan's call; can be held back without blocking any other wave |
| Ledger cap blocks the work that fixes the ledger cap | **already true** — 108 tokens | 6b is unblocked and execution-only; do it first, out of order, if any wave needs a ledger row |

---

## 10. Sequencing

```
6b (tombstones) ──────────► 6a (deprecated → fork)
      │
Wave 1 (leaves) ──► Wave 2 (meta-gates) ──► Wave 3 (wiring-checkers)
                          │                        │
                          └──► Wave 5 (untrack) ◄──┘
                                     │
                          Wave 4 (audit/ → fork, LAST)
                                     │
                          6c/6d/6e/6f (consolidation)
```

**Start at 6b** — it is execution-only, already ruled, unblocks `deprecated/`, and lifts the cap that
currently blocks every lane's next ledger entry. Then wave 1, which is pure leaves.
