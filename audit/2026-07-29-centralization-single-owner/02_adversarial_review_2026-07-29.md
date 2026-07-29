# Adversarial review — centralization & single-ownership plan v1

## Status: REVIEW RECORD (read-only; rules nothing) — ED-IN-0103, 2026-07-29

**Method.** The plan was drafted by a Fable-tier planner from four read-only reconnaissance lanes,
then attacked by **two structurally independent `valoria-critic` agents** (Opus tier, `Read/Grep/Glob`
only — no write tools by construction, per CLAUDE.md §10's structural-independence rule). Neither
critic saw the planner's reasoning; each received only the artifact. Lenses were disjoint and assigned
in advance:

- **Critic A — factual correctness against HEAD.** Every number, path and line-cite treated as a
  hypothesis until re-derived. 17 findings.
- **Critic B — directive coverage, structure, cross-program collision.** Explicitly instructed that
  the most likely failure of a plan like this is quietly narrowing its own mandate. 17 findings.

**34 findings, 10 of them P1.** The orchestrator independently re-verified the three highest-impact
claims before accepting them. All are reconciled into `01_orchestration_plan_v1.md`.

---

## The findings that changed the plan

| # | Finding | Disposition |
|---|---|---|
| **A-F1** | The dup detector's "expected: the `compute_degree` byte-identical **pair**" is wrong by an order of magnitude — **26 definitions exist**, 24 in the frozen `tests/sim/sim_mb_06_v5…v25.py` snapshot corpus. The plan's own stop-rule ("count ≫ census halts the wave") would have **aborted Wave 2 on its own wrong prediction** | **Orchestrator-verified** (`grep -c "def compute_degree"` → 26). Corpus scope promoted from a detail to the detector's design: `tests/sim/**` + `tests/sim_framework/**` are a declared frozen-harness allowlist, excluded from `dup.count`, **printed as excluded-with-count** per §8's no-silent-caps rule. §2.3 rewritten |
| **A-F2** | The §0 carve-out (`systems/combat/**`, `tests/sim/mass_battle/**`) does not cover where the duplication actually lives — the forks are under `tests/sim/` but **not** `tests/sim/mass_battle/`, so they were in-scope for detection, out-of-scope for MB routing, and unprotected by the W5 no-touch assertion | Both trees named explicitly with a stated disposition |
| **A-F3** | Size-cap single-sourcing is not mechanical: **≥5 divergences**, not one (`arc_register` 20k/5k, `values_master` 40k/50k, `patch_register_index` 20k/6k, `names_index` 8k/generic-10k, `propagation_map` 15k/10k); **12 of 26 checker paths have no policy entry at all**; and `propagation_map.md` has **two contradictory policy blocks** (10000 and 5000) where the loader returns on first hit | Stage retiered sonnet/low → **sonnet/high + opus adjudication**; §6 row 6 widened from 1 fork to the whole set |
| **B-F1** | **FORMULAS — a named clause of the directive — have no owner, no wave, no falsifier, and are not even deferred to §6.** The category is absent. The plan touches `ci_formula_prose_check.py` for an unrelated reason and never asks whether formulas have one owner | **The single largest coverage gap.** New §1 predicate 8, new §2.0, new W1 stage 1, new signal `formula.drift` |
| **B-F2** | **`ci_formula_prose_check.py` is silently dead at HEAD.** `DEFAULT_CENSUS` (lines 86–88) points into the retired `designs/` tree; `load_census` returns `[]` without raising; the tool prints `0 findings across 0 formula-bearing quantities` and exits 0. **Neither in-flight program's dead-root list contains it** | **Orchestrator-verified by running it.** The §0.1-point-2 defect class exactly — an assertion that cannot observe the failure it excludes. Repoint + `rows > 0` guard is W1 stage 1; added to both programs' scope by routing row |
| **B-F3** | Inbound routing as "PR-body + docket lines" **regresses a landed convention.** ED-IN-0091 established routing is *physical*: items are appended to `MB §12` / `PC §15` INBOUND sections, which exist on disk, so "a dedicated session reading only its own plan misses nothing." A PR body is not a section of the MB plan | W3 stage 4 rewritten to append to the existing INBOUND sections. "Never lane-handoff writes" retained for `HANDOFF_MB.md`, where it is correct |
| **B-F4** | Directive (2) satisfied only for the plan itself; **6 other live plans left pointer-less**, and §6 row 7's default said "revisit if a plan lands pointer-less **again**" — asserting a clean current state that is false for all 7 | W0 stage 3 backfills **all 8** pointer files; §6 row 7's premise corrected |
| **B-F5** | `workplans/README.md` rules the **opposite** convention and nothing owned the edit — a live contradiction would have shipped, and the next session would read every pointer as misplaced | README rewritten in the same commit as the pointers |
| **B-F6** | The **ED-IN-0073** character-decision program is never mentioned, yet its Phase 1 relocates `systems/characters/`, repoints `descriptor_registry` + `module_contracts`, and writes `values_master.yaml` — **a lane table cannot be authored against paths about to move** | §0.1 interlock 4; two pointer files carry the sequencing warning |
| **B-F13** | "Ordering is convention, not enforcement" is not an acceptable mitigation for the one race that **silently destroys work** — if ED-IN-0091 W4 item 5 retires `tools/registry.py` first, the ED-1082 grep-then-move precedent finds no consumers *precisely because* W1 has not run | Promoted to a **hard interlock** using ED-IN-0091 §4's existing binding stop-condition mechanism |

## Corrections to numbers (critic A)

| Claim as drafted | Measured |
|---|---|
| 46 dead lane prefixes | **44** — 41 `designs/` + **3 `sim/`**, a second retired tree the predicate did not name |
| ~26 files parse `module_contracts.yaml` | **19–21** parse-sites (38 files merely *mention* it) — **plus `wiring_map_check.py:45`, which parses by REGEX** and needs a `module_ids()` accessor, not a `safe_load` swap |
| 5 live `references/registry/*` citations | **3 in-scope** + 1 handoff mention; the rest are append-only ledger and frozen-audit rows that **must not be repointed** |
| `structure_audit.py:379` / `build_graph.py:335` | `:378` / `:334-336` (the "inlined exactly twice in production" claim was attacked repo-wide and **holds**) |

## Claims attacked that survived

`ci_names_consistency.py:45` and `quantity_registry.py:66` re-parses (exact) · 26 thresholds / 2
single-sourced (exact) · `build_decisions.MARKERS` = 13 patterns (exact) · `ci_claude_workflow_paths.py`
declares the fold verbatim at `:14-15` · `SIM-CALIBRATE`/`FIAT` have zero machine readers · the scale
vocabularies and the `peninsular`/`peninsula` divergence · `SCHEMA_VERSION` is a genuine false positive
(3 unrelated schemas) · `build_decisions.py:230` contradicts CLAUDE.md on `systems/overview/` ·
**no lane checker, no duplication detector, and no `contracts_store` equivalent exists** — §2.2/§2.3/§2.4
are not re-implementations · the prose-path fold does **not** collide with ED-IN-0091 W4 item 3
(`ci_common.sim_reference_roots()` owns *where the sim reference lives*; `RETIRED_TREES` owns *which
trees are retired* — different questions, both single-owned) · every §1 predicate has an instrument and
no §3.6 row is unowned · Fable placement complies with §10 · agent counts reconcile.

## Orchestrator corrections to the reconnaissance

- **`tools/registry.py` importers.** A scout named `tests/sim/territory_registry/test_registry_ledger.py`
  and `tests/sim/mass_battle/workbench/server.py` as consumers. **Wrong** — those import unrelated
  modules that happen to be named `registry` (`sim.territory.registry`,
  `mass_battle.troop_types.registry`). Re-derived: the facade's **only importer anywhere is its own
  unit test**. The truth is stronger than the claim, and it matters — completing WS1 has no read-side
  migration cost.
- **`apparatus_registry.yaml:950` already reports `orphaned: false`** for that same module, because the
  generator counts a unit-test import as an invoker (critic A-F7). The plan's original acceptance
  instrument would have measured a flag that reads `false` before *and* after. §2.6 added.
- **A `## Status:` line is not a liveness signal.** The orchestrator initially reported that live plans
  are exactly those lacking one. The full triage refuted it in both directions: 3 of 7 live plans carry
  one; 7 of the 10 files that carry one are dead. Pointer files therefore carry an **explicit**
  `liveness:` field.

## Disagreements recorded, not resolved

1. `HANDOFF_MB.md` labels the live MB plan "v1 (superseded)" — the bullet predates PR #250's in-place
   v2 correction. Recorded in the MB pointer; **not** silently reconciled (that file is the MB
   session's to write).
2. `valoria_master_workplan_v6.md`'s MB row still calls `05_redesign_workplan.md` "the governing plan."
3. `ED-IN-0066` remains `status: open` though its execution surface was absorbed into ED-IN-0091.
4. Two MB plans classified SUPERSEDED at ~80% confidence carry no supersession banner — the softest
   calls in the triage, flagged as such.

## Limits of this review

Critic A had no Bash by construction, so `git log --all` was unavailable to it; the "`references/registry/`
never existed" half was verified separately by the orchestrator. Neither critic executed the corpus —
both reasoned from reading. The A18 formula-drift magnitude is **unknown at plan time** because the
detector has been dead; W1 stage 1's first real measurement could be 0 rows or 200, and §9 risk 4
states that rather than smoothing it.
