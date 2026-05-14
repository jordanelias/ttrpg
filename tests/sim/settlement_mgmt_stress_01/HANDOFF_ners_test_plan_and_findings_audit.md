# HANDOFF — NERS Empirical Test Plan + Mechanical Findings Log

**Document:** `tests/sim/settlement_mgmt_stress_01/HANDOFF_ners_test_plan_and_findings_audit.md`
**Date:** 2026-05-14
**Author session:** Mode G post-completion (after M13 STRUCTURALLY COMPLETE commit `6c9cdd35`)
**Status:** Open for execution
**Reader:** Jordan (project owner) + any reviewer Jordan designates

---

## 0 — Scope and what this document is

`settlement_mgmt_stress_01` is **structurally complete** as of commit `6c9cdd35` (M13 FINAL). The M13 audit produced a 24-cell NERS grid by **subjective assessment** — rationale strings written from the implementer's vantage. This handoff promotes each cell into an **empirical probe**: a concrete experiment with a mechanical artifact, pass/partial/fail criteria, and reproducible execution.

Parallel section: the cumulative findings register (18 findings across M1-M12) is restated as an **audit-grade log** with dependency graph and evidence pointers, suitable for an external reviewer to verify without re-reading every module report.

**This is a handoff, not a runner.** No code executes here. Each probe specifies what to run and how to interpret the output. Execution belongs in the next session(s), after Jordan decides priority.

**Prerequisites for execution:**
- `gh api` access to `jordanelias/ttrpg`
- `/home/claude` working dir with `github_ops.py` + `valoria_hooks.py` from session bootstrap
- M1-M13 modules already on GitHub at `tests/sim/settlement_mgmt_stress_01/module_NN_*.py`

---

## 1 — Why empirical NERS matters

The PI `<canon_terms>` definitions:

- **Necessary:** unable to be removed without worsening gameplay
- **Robust:** strategic thinking, customization, emergent narrative; mechanics fully formed, error-free, complete
- **Smooth:** integrates cleanly without friction across scales
- **Elegant:** logically simple, clear approach, no unnecessary overhead

These are **operational** definitions: they admit empirical test. "Unable to be removed without worsening gameplay" is testable by removing the mechanic and observing whether downstream tests break or canonical numbers diverge. "Integrates cleanly without friction" is testable by counting fallback-path invocations or off-canonical-type rejection rates.

The M13 self-assessment rationales are the implementer's *priors*. An audit reviewer should not accept implementer priors at face value. Each probe below is the experiment that converts a prior into evidence.

---

## 2 — NERS Empirical Test Plan (24 probes)

Format per probe:
- **Probe ID:** `NERS-{property}-{direction}` for indexing
- **Hypothesis:** what the probe is testing (the M13 prior, restated as a falsifiable claim)
- **Mechanical artifact:** which file / function / data structure to inspect
- **Procedure:** the concrete experiment
- **PASS criterion:** what counts as confirming the hypothesis
- **partial criterion:** what counts as ambiguous evidence
- **FAIL criterion:** what counts as falsifying
- **Dependencies:** which other probes / unblocks are prerequisites
- **Execution cost:** rough minutes of work

### 2.1 NECESSARY × 6 directions (6 probes)

#### NERS-N-TopDown
- **Hypothesis:** Province Accord is undefined without settlement-level Order; removing M2 `province_accord_from_settlements` breaks province-level mechanics.
- **Artifact:** `module_01_primitives.py::province_accord_from_settlements`; downstream consumers in M11 Domain Echo + §8.1 S07 Victory binding.
- **Procedure:** Run `grep -rn "province_accord_from_settlements" tests/sim/settlement_mgmt_stress_01/` to enumerate callers. For each caller, comment out the call and run that module's isolation tests. Count test failures.
- **PASS:** ≥3 downstream consumers break (settlement-to-province is structurally load-bearing).
- **partial:** 1-2 consumers break (load-bearing but narrow).
- **FAIL:** 0 consumers break (the function is dead code; necessity is illusory).
- **Dependencies:** none.
- **Cost:** 15 min.

#### NERS-N-BottomUp
- **Hypothesis:** The 8 emergent cross-module chains (T43, T41, T35, T27, T30, T38, T40, M13-T23) require atomic predicate composition; replacing any one predicate with a hardcoded constant breaks the chain.
- **Artifact:** Tests T43 (M6), T41 (M7), T35 (M9), T27 (M10), T30 (M11), T38/T40 (M12), T23 (M13).
- **Procedure:** For each chain test, identify the most atomic predicate it consumes (e.g. M6 `predicate_local_revolt`, M9 `tick_ms_decay`). Replace each with `lambda *a, **kw: True` or a constant and re-run the chain test. Count chains that still pass.
- **PASS:** All 8 chains fail when their constituent predicate is stubbed (chain emergence is genuine, not coincidental).
- **partial:** 6-7 chains fail.
- **FAIL:** ≤5 chains fail (some chains may be coincidentally aligned, not emergent).
- **Dependencies:** none.
- **Cost:** 45 min (8 chains × ~5 min each).

#### NERS-N-Vertical
- **Hypothesis:** The Stature ladder (M8) + Stage transitions (M8) + Faction integration (M12) form an irreducible vertical progression — removing any tier produces a player who cannot reach National Actor scope.
- **Artifact:** `module_08_progression.py` (StatureScope, EmergenceStage); `module_12_faction_integration.py` (FactionStats).
- **Procedure:** Construct a synthetic player StatureState with Renown=10 + 5 controlled provinces. Verify they reach Stage 5 HEGEMON. Then independently disable each of (M8 stage_from_renown, M8 can_transition_4_to_5, M12 FactionStats) and re-run. Check whether the path remains traversable.
- **PASS:** All 3 disablements break the path.
- **partial:** 2 disablements break (one tier is redundant).
- **FAIL:** ≤1 breaks (tiers are decorative, not load-bearing).
- **Dependencies:** none.
- **Cost:** 30 min.

#### NERS-N-Diagonal
- **Hypothesis:** The Domain Echo chain dampening by province count (M11 `domain_echo_province_to_national`) is non-trivially necessary — removing it makes multi-province factions over-reactive at national scale.
- **Artifact:** `module_11_provincial_authority.py::domain_echo_province_to_national`; T20 + T22 tests.
- **Procedure:** Replace the `province_magnitude // controlled_provinces_count` dampening with `province_magnitude` (no dampening). Run a 30-year integrated simulation with Crown holding 5 provinces, one REVOLT per year. Compare final national-stability impact magnitude with vs. without dampening.
- **PASS:** Without dampening, national-stability change ≥3× larger (over-reactive); with dampening, magnitude scales sub-linearly with province count.
- **partial:** Without dampening, change is 1.5-3× larger (dampening matters but is not dominant).
- **FAIL:** Without dampening, change is <1.5× larger (dampening is decorative).
- **Dependencies:** none.
- **Cost:** 30 min.

#### NERS-N-Lateral
- **Hypothesis:** The adjacency graph M2 EDGES provides settlement-to-settlement lateral coupling that province-scope mechanics cannot substitute; removing edges collapses settlements within a province to mechanical equivalence.
- **Artifact:** `module_02_hierarchy.py::EDGES`, `neighbors()`; M7 invasion sequencing (`can_jump_to_settlement`).
- **Procedure:** Replace EDGES with a complete graph (every settlement adjacent to every other in the same province). Run M7 invasion-sequencing tests + adjacency §2.2 terrain-modifier tests. Count tests that change outcome.
- **PASS:** ≥10 outcomes change (terrain mods + chokepoint dynamics + bypass eligibility shift).
- **partial:** 5-9 outcomes change.
- **FAIL:** <5 outcomes change.
- **Dependencies:** none.
- **Cost:** 25 min.

#### NERS-N-Horizontal
- **Hypothesis:** `per_season_accounting()` (M9) is the single canonical horizontal time-coupling layer — removing any of its 5 clock ticks (MS, CI, IP, Turmoil, GS) breaks at least one primary throughline binding.
- **Artifact:** `module_09_timeline.py::per_season_accounting` + 5 tick functions.
- **Procedure:** Independently no-op each of `tick_ms_decay`, `tick_ci_accumulation`, `tick_ip_accumulation`, `tick_turmoil`, `tick_generational_shift`. Run M13 T23 (30-year canonical) and verify which canonical numbers diverge from §7.1 expected values (MS=42, IP=80, GS=6).
- **PASS:** Every no-op breaks at least one canonical number (5 primary throughline bindings are individually load-bearing).
- **partial:** 4 of 5 break.
- **FAIL:** ≤3 break.
- **Dependencies:** none.
- **Cost:** 20 min.

### 2.2 ROBUST × 6 directions (6 probes)

#### NERS-R-TopDown
- **Hypothesis:** The two-tier authority model + tension index produces actual strategic gameplay variation — a PA with hostile disposition toward Governor produces measurably different season outcomes than aligned PA.
- **Artifact:** `module_11_provincial_authority.py::accumulate_tension_per_season`, `authority_alignment`.
- **Procedure:** Run two parallel 20-season simulations: (A) PA-Governor disposition +3 throughout; (B) disposition −3 throughout. Compare frequency of governance-transition events fired (M6) + settlement Order trajectory.
- **PASS:** Run B produces ≥2× more governance-transition events AND lower mean Order.
- **partial:** Run B produces 1.5-2× events.
- **FAIL:** <1.5× difference (tension is decorative).
- **Dependencies:** none.
- **Cost:** 25 min.

#### NERS-R-BottomUp
- **Hypothesis:** M6 §4.5 Local Actor recruitment + M10 dissolution emergence (black markets / intel brokers / thread sites) provide bottom-up narrative hooks without player involvement — running an "idle" 30-year simulation produces ≥5 emergent narrative events per simulation.
- **Artifact:** Integrated runner with all player-action handlers stubbed (no improvement/maintenance/problem-solve actions).
- **Procedure:** Run `integrated_season_tick` for 120 seasons with zero player actions. Count fired events (M6 events + M10 black-market emergences + M10 intel-broker placements).
- **PASS:** ≥5 distinct event-firings per simulation, ≥3 distinct event types represented.
- **partial:** 3-4 events of ≥2 types.
- **FAIL:** ≤2 events OR all events same type.
- **Dependencies:** none.
- **Cost:** 30 min.

#### NERS-R-Vertical
- **Hypothesis:** The 5 EmergenceStages + ED-790 founded-faction starting stats give distinct starting positions; faction emergence outcome at Stage 4 varies meaningfully with Renown at declaration.
- **Artifact:** `module_08_progression.py::founded_faction_starting_stats`.
- **Procedure:** Sweep Renown at declaration from 7 to 10 in steps of 1. For each, compute starting stats. Compute Euclidean distance in stat-space between adjacent stat-vectors.
- **PASS:** Mean inter-Renown distance ≥1.5; max distance ≥3 (Renown 7 → 10 produces meaningfully different founded factions).
- **partial:** Mean 1.0-1.5.
- **FAIL:** Mean <1.0 (stat differences are noise).
- **Dependencies:** none.
- **Cost:** 15 min.

#### NERS-R-Diagonal
- **Hypothesis:** The 7 subnational-faction management-effect variants (Church Piety, Guilds Trade, Ministry Order-decay, Löwenritter Defense, RM CV-Einhir, Wardens Thread-monitoring, Niflhel Intel) produce 7 distinct diagonal paths through settlement-to-faction integration.
- **Artifact:** `module_05_governance.py::MANAGEMENT_EFFECTS`.
- **Procedure:** For each subnational, run a 10-season simulation of a settlement under that subnational's management. Record (Prosperity, Defense, Order, faction_renown) trajectory. Compute pairwise trajectory-distance across the 7 subnationals.
- **PASS:** All 7 trajectories are pairwise distinct (no two subnationals produce identical outcomes); mean pairwise distance ≥2.
- **partial:** 5-6 distinct trajectories (some collapse).
- **FAIL:** ≤4 distinct trajectories (most subnationals are mechanically equivalent).
- **Dependencies:** none.
- **Cost:** 35 min.

#### NERS-R-Lateral (M13 marked PARTIAL — verify)
- **Hypothesis:** Lateral coupling exists via adjacency edges (M2) + §2.2 settlement-type modifiers (M7); the F15 City omission produces a measurable gap.
- **Artifact:** `module_07_military.py::SETTLEMENT_TYPE_MODIFIER_BY_TYPE` (City row uses provisional zero modifier).
- **Procedure:** Construct two parallel siege scenarios — one against a Town, one against a City — with otherwise-identical attacker/defender stats. Resolve siege via M7 assault chain. Compare outcomes.
- **PASS for partial finding:** Town and City siege outcomes are mechanically identical (confirming F15: City has no canonical modifier and falls back to Town's). This means the partial rating is **correctly identified**.
- **FAIL for partial finding:** Outcomes differ even without a canonical City modifier (would indicate the fallback path itself is broken).
- **Dependencies:** none.
- **Cost:** 15 min.

#### NERS-R-Horizontal
- **Hypothesis:** Per-season events compose freely without contradicting — running a stress-loaded settlement (Famine + Local Revolt + Governance Transition simultaneously) produces all three events without state corruption.
- **Artifact:** `module_06_events.py::sweep_season_events`.
- **Procedure:** Construct a settlement with stats deliberately set to fire all three predicates simultaneously (Prosperity 0, Order 0, governance transition in progress). Run sweep. Verify all 3 fire AND post-sweep state is consistent (all stats in valid range, no None values).
- **PASS:** All 3 fire; post-sweep state passes invariant check.
- **partial:** 2 of 3 fire (some predicates mutually exclusive — investigate why).
- **FAIL:** Post-sweep state inconsistent (cascade corrupts state).
- **Dependencies:** none.
- **Cost:** 15 min.

### 2.3 SMOOTH × 6 directions (6 probes)

#### NERS-S-TopDown
- **Hypothesis:** Domain Echo chain propagates settlement events upward to province then national without contradiction; the dampening prevents discontinuity at multi-province factions.
- **Artifact:** `module_11_provincial_authority.py::domain_echo_chain`.
- **Procedure:** Sweep `controlled_provinces_count` from 1 to 8 for each canonical SettlementEvent. For each (event, province_count) pair, verify the chain returns either an empty list, a 1-step chain, or a 2-step chain — never a malformed chain.
- **PASS:** All 5 events × 8 province counts = 40 cases produce well-formed chains.
- **partial:** 36-39 well-formed.
- **FAIL:** ≤35 well-formed (smoothness genuinely broken at some scale boundary).
- **Dependencies:** none.
- **Cost:** 20 min.

#### NERS-S-BottomUp
- **Hypothesis:** The M3-M12 ActionResult signals bind canonically via `apply_renown_delta` (M8) and `bind_faction_standing_delta` (M12) without friction; no signal magnitude is "stranded" between layers.
- **Artifact:** `module_08_progression.py::apply_renown_delta`, `module_12_faction_integration.py::bind_faction_standing_delta`.
- **Procedure:** Enumerate every `renown_delta` and `faction_standing_delta` value produced by any ActionResult in M3-M11 (grep the codebase for `renown_delta=`, `faction_standing_delta=`). For each value, run it through the binding function. Verify every value produces a non-trivial canonical delta.
- **PASS:** Every emitted signal magnitude has a canonical binding (no signal produces zero downstream effect when its source intended impact).
- **partial:** 1-2 signal magnitudes produce silent zero-bindings.
- **FAIL:** ≥3 silent zero-bindings.
- **Dependencies:** none.
- **Cost:** 30 min.

#### NERS-S-Vertical (M13 marked PARTIAL — verify)
- **Hypothesis:** Type-taxonomy drift family (F1, F7, F10, F11, F12, F14, F18) creates measurable vertical friction — synthetic settlements with extra types (Village / Fortress-City / Cathedral-City) hit fallback paths in multiple modules.
- **Artifact:** Fallback handlers in M3 (capacity), M5 (governor eligibility), M5 (subnational alignment), M6 (Local Actor count), M10 (POI template).
- **Procedure:** Construct a Village settlement and route it through M3 `expand_institutional_capacity`, M5 standing-tier checks, M6 local-actor count, M10 POI template. Count fallback-path invocations (where the module falls back to Town/Outpost semantics or returns None).
- **PASS for partial finding:** ≥3 fallback invocations confirm vertical friction (F1/F7/F10/F11/F12/F14/F18 are real and provisional).
- **FAIL for partial finding:** 0 fallback invocations (drift is theoretical, not mechanical).
- **Dependencies:** none.
- **Cost:** 25 min.

#### NERS-S-Diagonal
- **Hypothesis:** Cross-scale transitions (Settlement Governor → Multi-Settlement → Provincial Authority → National Actor) are mechanically smooth; no scope-boundary produces double-counted or stranded effects.
- **Artifact:** M5 + M8 + M11 scope-transition logic.
- **Procedure:** Drive a player StatureState across all 4 scope-tier boundaries via canonical Renown gains. At each boundary crossing, snapshot ActionResult effects in the same season. Compare to a control run where the player remains within one tier.
- **PASS:** Boundary crossings produce monotonic Renown progression with no duplicate or lost effects.
- **partial:** 1 boundary has minor anomaly.
- **FAIL:** ≥2 boundaries produce stranded effects.
- **Dependencies:** none.
- **Cost:** 25 min.

#### NERS-S-Lateral
- **Hypothesis:** Adjacency edge types (road / river / mountain_pass / coastal / sea / thread_witnessed) integrate cleanly with M7 assault mechanics; provisional sea + thread_witnessed are flagged but don't break composition.
- **Artifact:** `module_07_military.py::TERRAIN_MODIFIER_BY_EDGE_TYPE`.
- **Procedure:** For each edge type, run an assault scenario where the attacker traverses that edge. Verify M7 `resolve_assault` returns a well-formed result for all 6 edge types (including the 2 provisional).
- **PASS:** All 6 edge types produce well-formed assault results.
- **partial:** 5 of 6 well-formed.
- **FAIL:** ≤4 well-formed.
- **Dependencies:** none.
- **Cost:** 15 min.

#### NERS-S-Horizontal (M13 marked PARTIAL — verify)
- **Hypothesis:** Documentation drift family (F2, F13, F16, F17) creates horizontal friction at audit time but doesn't break runtime composition.
- **Artifact:** Per-finding evidence in design docs.
- **Procedure:** Run M13 `integrated_season_tick` for 120 seasons. Verify zero exceptions thrown. Then separately: for each documentation-drift finding, identify what an external reviewer would have to cross-check between design doc and sim implementation.
- **PASS for partial finding:** Runtime composition unaffected; cross-check reveals ≥4 documentation gaps for reviewer.
- **FAIL for partial finding:** Runtime breaks OR <2 documentation gaps (drift overstated).
- **Dependencies:** none.
- **Cost:** 30 min.

### 2.4 ELEGANT × 6 directions (6 probes)

Elegance probes are **static analysis** rather than dynamic experiment — they measure code-shape properties.

#### NERS-E-TopDown
- **Hypothesis:** Province Accord derivation is irreducibly simple (single floor-average expression with one tiebreaker).
- **Artifact:** `module_01_primitives.py::province_accord_from_settlements`.
- **Procedure:** Inspect the function. Count: lines of code (excluding docstring/comments), number of conditionals, number of dependencies on other module functions.
- **PASS:** ≤10 LOC, ≤2 conditionals, ≤1 cross-module dependency.
- **partial:** ≤15 LOC.
- **FAIL:** >15 LOC OR >3 conditionals.
- **Dependencies:** none.
- **Cost:** 5 min.

#### NERS-E-BottomUp
- **Hypothesis:** Atomic predicates compose via shared state without controller objects or inheritance hierarchies.
- **Artifact:** `module_06_events.py` (predicates), `module_10_dissolution.py` (predicates), `module_07_military.py` (predicates).
- **Procedure:** `grep -c "^class.*Controller\|^class.*Manager\|^class.*Orchestrator"` across all module files. Count base classes in dataclass inheritance trees.
- **PASS:** Zero Controller / Manager / Orchestrator classes; zero non-trivial inheritance.
- **partial:** Up to 1 controller-like class.
- **FAIL:** ≥2 controller-like classes OR inheritance hierarchies >1 level deep.
- **Dependencies:** none.
- **Cost:** 10 min.

#### NERS-E-Vertical
- **Hypothesis:** Stature ladder uses a single Renown integer 0-10 to unlock all governance scope; no parallel tracking required.
- **Artifact:** `module_08_progression.py::StatureScope`, `stature_scope_from_renown`.
- **Procedure:** Inspect the StatureState dataclass. Count fields involved in scope determination (should be `renown` alone). Verify `stature_scope_from_renown` is a pure function of Renown.
- **PASS:** Scope is purely a function of Renown.
- **partial:** Scope depends on Renown + 1 other field.
- **FAIL:** Scope requires 3+ fields.
- **Dependencies:** none.
- **Cost:** 5 min.

#### NERS-E-Diagonal
- **Hypothesis:** Domain Echo chain is two function compositions with no intermediate machinery.
- **Artifact:** `module_11_provincial_authority.py::domain_echo_chain`.
- **Procedure:** Inspect the function. Count LOC, number of intermediate variables, number of helper functions called.
- **PASS:** ≤15 LOC; ≤2 helper calls (settlement→province, province→national).
- **partial:** ≤25 LOC.
- **FAIL:** >25 LOC OR >4 helper calls.
- **Dependencies:** none.
- **Cost:** 5 min.

#### NERS-E-Lateral
- **Hypothesis:** Adjacency queries use a single `neighbors()` function with no region/zone abstractions or precomputed pathfinding tables.
- **Artifact:** `module_02_hierarchy.py::neighbors`, EDGES.
- **Procedure:** Inspect M2. Verify EDGES is a single flat data structure (not nested abstractions). Verify `neighbors()` is ≤10 LOC.
- **PASS:** EDGES is a flat collection; `neighbors()` is ≤10 LOC.
- **partial:** Slightly more than 10 LOC but clearly single-purpose.
- **FAIL:** EDGES is nested/hierarchical OR `neighbors()` is >20 LOC.
- **Dependencies:** none.
- **Cost:** 5 min.

#### NERS-E-Horizontal
- **Hypothesis:** `per_season_accounting()` is a single function composing 6 modules' per-season effects in canonical sequence; no scheduler, no event queue.
- **Artifact:** `module_09_timeline.py::per_season_accounting`.
- **Procedure:** Inspect the function. Count: LOC, presence of queue/scheduler structures, presence of dynamic event dispatch.
- **PASS:** Linear sequence of function calls; no `queue.`, `deque`, `dispatch_event`, or similar; ≤80 LOC.
- **partial:** ≤120 LOC.
- **FAIL:** >120 LOC OR scheduler/queue present.
- **Dependencies:** none.
- **Cost:** 10 min.

### 2.5 Execution sequencing

| Probe batch | Probes | Total cost | Prerequisites |
|---|---|---|---|
| Quick static analysis | NERS-E-* (6) | ~40 min | none |
| Single-experiment dynamic | NERS-N-TopDown, R-TopDown, R-Vertical, R-Lateral, R-Horizontal, S-Lateral | ~110 min | none |
| Multi-experiment dynamic | NERS-N-BottomUp, N-Diagonal, N-Lateral, N-Horizontal, R-BottomUp, R-Diagonal | ~195 min | none |
| Drift-verification | NERS-S-Vertical, S-Horizontal | ~55 min | none |
| Cross-scale composition | NERS-N-Vertical, S-TopDown, S-BottomUp, S-Diagonal | ~110 min | none |

**Total execution: ~8.5 hours of probe work, fully parallelizable across sessions.** All probes are independent — no dependency chains. Recommend running quick static analysis first (validates the cheap-to-confirm Elegant priors) before committing to dynamic experiments.

### 2.6 Probe-result aggregation format

Per-probe output for audit review:

```yaml
probe_id: NERS-N-BottomUp
prior_rating: pass
empirical_rating: pass | partial | fail
evidence_summary: |
  8 chain tests run with constituent predicates stubbed.
  All 8 broke as predicted. Chain emergence is genuine.
artifacts_inspected:
  - tests/sim/.../module_06_events.py::predicate_local_revolt
  - tests/sim/.../module_07_military.py::resolve_siege_tick
  - ...
findings_surfaced:  []   # any NEW findings the probe uncovered
recommendation: confirm prior | downgrade to partial | escalate to FAIL | escalate finding
```

Aggregate output: `tests/sim/settlement_mgmt_stress_01/audits/ners_empirical_audit_YYYY-MM-DD.md` with one section per probe + summary table.

---

## 3 — Mechanical Findings Log (audit-grade)

Cumulative findings register from M1-M12 with audit metadata. **18 total findings: 1 resolved, 1 partial, 16 open.**

### 3.1 Findings register — full

| ID | Title | Family | Status | Surfacing | Evidence file:section | Closure path | Blocks | Blocked-by |
|---|---|---|---|---|---|---|---|---|
| F1 | Settlement type-taxonomy drift §1.2 vs §2.1 | type-tax-drift | open | M1 | `settlement_layer_v30.md` §1.2 vs §2.1 | Editorial P1 | F7, F10, F11, F12, F14, F18 | — |
| F2 | Settlement stats schema documentation gap | doc-drift | open | M1 | `settlement_layer_v30.md` §1.3 implicit Prosperity/Defense/Order schema | Editorial P2 | — | — |
| F3 | PP-726 §2.1 registry rebuild propagation | isolated | RESOLVED | M2 | resolved at M2 commit `b5545aa5` | — | — | — |
| F4 | §1.3 vs §2.1 granularity | isolated | PARTIAL | M2 | `valoria_geography_v30.yaml` settlements: block | Editorial P3 (closes with F6) | — | F6 |
| F5 | Edge-count math discrepancy | isolated | open | M2 | `settlement_adjacency_v30.md` adjacency totals | Editorial P4 | — | — |
| F6 | Pre-PP-726 S-ID granularity drift in geography YAML | **mode-c-blocker** | open | M2 | `valoria_geography_v30.yaml` settlements: block | Editorial P3 (geography YAML rebuild) | F4, Mode-C, Mode-D, batch | — |
| F7 | §1.4.1 facility matrix omits extras | type-tax-drift | open | M3 | `settlement_layer_v30.md` §1.4.1 capacity table | Editorial P1 (closes with F1) | — | F1 |
| F8 | §1.5/§1.6 effect-timing asymmetry | isolated | open (info) | M4 | `settlement_layer_v30.md` §1.5/§1.6 | Editorial P4 (doc only) | — | — |
| F9 | §3.2 Pacify floor()-redundancy | isolated | open (info) | M5 | `settlement_layer_v30.md` §3.2 Pacify formula | Editorial P4 (doc only) | — | — |
| F10 | §3.2 governor eligibility omits extras | type-tax-drift | open | M5 | `settlement_layer_v30.md` §3.2 | Editorial P1 (closes with F1) | — | F1 |
| F11 | §3.3 subnational alignment + Guilds Market ref | type-tax-drift | open | M5 | `settlement_layer_v30.md` §3.3 | Editorial P1 (closes with F1) | — | F1 |
| F12 | §4.5 Local Actor counts omit extras | type-tax-drift | open | M6 | `settlement_layer_v30.md` §4.5 | Editorial P1 (closes with F1) | — | F1 |
| F13 | §4.5 prose pre-rebuild | doc-drift | open | M6 | `settlement_layer_v30.md` §4.5 prose | Editorial P2 | — | — |
| F14 | §5.1 + adjacency §3 stale S-IDs | type-tax-drift / doc-drift overlap | open | M7 | `settlement_layer_v30.md` §5.1; `settlement_adjacency_v30.md` §3 examples | Editorial P1 (S-ID refresh component) | — | F1 |
| F15 | §2.2 settlement-type modifier omits City | isolated | open | M7 | `settlement_adjacency_v30.md` §2.2 | Editorial P4 (add City row) | — | — |
| F16 | §4.5/§4.6 stale Throughline-T-NN parentheticals | doc-drift | open (info) | M8 | `settlement_layer_v30.md` §4.5 `(Throughline T7)` and §4.6 `(Throughline T3)` | Editorial P2 (T-NN refresh to post-ED-738) | — | — |
| F17 | clock_registry vs §7.1 IP rate doc gap | doc-drift | open (info) | M9 | `clock_registry_v30.md` IP row; `settlement_layer_v30.md` §7.1 recalibration | Editorial P2 (annotate §7.1 governs) | — | — |
| F18 | §4.6 POI templates omit extras | type-tax-drift | open | M10 | `settlement_layer_v30.md` §4.6 POI template table | Editorial P1 (closes with F1) | — | F1 |

### 3.2 Family aggregate

| Family | Count | Members | Closure |
|---|---|---|---|
| **type-tax-drift** | 7 | F1, F7, F10, F11, F12, F14, F18 | **Editorial P1 — ONE pass closes all 7** |
| **doc-drift** | 4 | F2, F13, F16, F17 (F14 dual-classified to type-tax) | **Editorial P2 — ONE pass closes all 4** |
| isolated | 6 | F3 (resolved), F4 (partial), F5, F8, F9, F15 | Editorial P3 (F4) + P4 (F5, F8, F9, F15) |
| **mode-c-blocker** | 1 | F6 | **Editorial P3 — closes F4 as side effect; unblocks Mode-C/D** |

### 3.3 Dependency graph (Mermaid)

```
F1 ──┬→ F7
     ├→ F10
     ├→ F11
     ├→ F12
     ├→ F14
     └→ F18

F6 ──→ F4 (partial → resolved)
     └→ Mode-C unblock
        └→ Mode-D systematic search
            └→ 50-seed batch validation

(F2, F5, F8, F9, F13, F15, F16, F17 are independent)
```

**Critical observation:** F1 is the structural root of the type-taxonomy drift family. Closing F1 with the canonical §1.2 / §2.1 reconciliation cascades to closing 6 other findings.

### 3.4 Editorial sequence — operational order

| Priority | Pass name | Closes | Cost estimate | Unblocks |
|---|---|---|---|---|
| **P1** | Type-taxonomy reconciliation | F1, F7, F10, F11, F12, F14, F18 (7) | ~2 hours | NERS-S-Vertical confirmation; reduces audit-noise floor |
| **P2** | Documentation refresh | F2, F13, F16, F17 (4) | ~1 hour | NERS-S-Horizontal confirmation |
| **P3** | F6 Mode-C unblock | F6, F4 (2) | ~3 hours (YAML rebuild) | Mode-C, Mode-D, 50-seed batch |
| **P4** | Isolated cleanup | F5, F8, F9, F15 (4) | ~1 hour | NERS-R-Lateral confirmation (F15) |

**Total editorial cleanup: ~7 hours. Cleanest sequence is P1 → P2 → P3 → P4.**

---

## 4 — Audit Reviewer Checklist

For an external reviewer (or Jordan acting as reviewer) to verify the M1-M13 work and the NERS probe results. Each item is a single yes/no question with a pointer to the artifact answering it.

### 4.1 Architectural commitments
1. ☐ Are there any Controller / Manager / Orchestrator classes anywhere in M1-M13? *Run NERS-E-BottomUp probe.*
2. ☐ Is `per_season_accounting()` a linear sequence of function calls without scheduler/queue structures? *Run NERS-E-Horizontal probe.*
3. ☐ Are all cross-module emergent chains genuine (atomic predicate composition) rather than coincidental? *Run NERS-N-BottomUp probe.*
4. ☐ Does the 30-year integrated simulation produce §7.1 worked values to the integer? *Run M13 T23 — already validated in commit `6c9cdd35`.*

### 4.2 Canonical-source compliance
5. ☐ Is every numeric constant in M1-M13 cited to a canonical source via `sim_verification_ledger.json`? *Verify ledger entry count = 245.*
6. ☐ Did sim_gate pass on every commit M1-M13? *Verify commit log — every commit message ends with safe_commit OID.*
7. ☐ Does the fab pre-check show zero genuine fab issues in any module? *Run `h._extract_uncited_constants` against each module file and verify no value falls outside the ledger.*

### 4.3 Throughline coverage
8. ☐ Are all 7 primary meta-throughlines (М-1 through М-7) primary-bound? *Inspect `META_THROUGHLINE_FINAL_TALLY` in M13.*
9. ☐ Are the 4 character-layer T-NNs (T-12, T-13, T-14, T-17) correctly out-of-scope? *Inspect M13 `CHARACTER_LAYER_T_NNS`.*
10. ☐ Is T-16 (Knot Propagation) appropriately unbound (threadwork-sim scope, not settlement-mgmt)? *Inspect M13 throughline audit.*

### 4.4 NERS audit
11. ☐ Does the M13 NERS grid match empirical probe results? *Run all 24 NERS probes per section 2 above.*
12. ☐ Are both partial cells (Smooth-Vertical, Smooth-Horizontal) confirmed as documentation-only drift (no mechanical drift)? *Run NERS-S-Vertical + NERS-S-Horizontal probes.*
13. ☐ Is the Robust-Lateral partial (F15 City omission) confirmed as a single canonical-completeness gap rather than mechanical failure? *Run NERS-R-Lateral probe.*

### 4.5 Findings register
14. ☐ Does the findings register total exactly 18 with classification (1 resolved, 1 partial, 16 open)? *Inspect §3.1 above.*
15. ☐ Is F6 correctly identified as Mode-C blocker (not Mode-A/B blocker)? *Verify Mode A and B are both "complete" in M13 mode progression audit.*
16. ☐ Does the dependency graph (§3.3) match the closure-path field for each finding? *Cross-check.*

### 4.6 Mode progression
17. ☐ Is Mode A complete (377 isolation tests M1-M12 + 26 M13 = 403)? *Verify via test execution.*
18. ☐ Is Mode B complete (8 cross-module emergent chains validated)? *Cross-check M13 T21-T25 + prior chain tests T43, T41, T35, T27, T30, T38, T40, M13-T23.*
19. ☐ Is Mode C blocked by F6 (not by anything else)? *Verify F6 is the only mode-c-blocker family finding.*
20. ☐ Is Mode D deferred pending Mode-C unblock? *Verify the 9-category systematic search has not been run.*

### 4.7 Bottom-up emergent architecture
21. ☐ Do all 8 emergent cross-module chains pass without authored coupling? *Re-run M6 T43, M7 T41, M9 T35, M10 T27, M11 T30, M12 T38, M12 T40, M13 T23.*
22. ☐ Is the strongest end-to-end emergence proof (M13 T23 30-year canonical) reproducible? *Run M13 isolation tests; verify T23 PASS.*

### 4.8 Editorial readiness
23. ☐ Is the P1 type-taxonomy reconciliation pass scoped correctly to close exactly 7 findings? *Verify F1+F7+F10+F11+F12+F14+F18 listed.*
24. ☐ Are the editorial priorities (P1-P4) independent enough to execute in any order? *F4 closes with P3 only; otherwise independent.*
25. ☐ Does completing P1-P4 leave only Mode-D systematic search + 50-seed batch as outstanding work? *Verify against current state.*

---

## 5 — Logging notes (per PI tags)

- `[ASSUMPTION: M13 NERS grid prior ratings are accurate self-assessments — basis: implementer prior. Empirical probes in §2 above will verify or falsify.]`
- `[ASSUMPTION: F4 status will move from partial to resolved when F6 closes — basis: F4 cause is the same geography YAML drift F6 names.]`
- `[GAP: Companions §8.1 system impact is "unrealized" — no dedicated mechanic; deferred. Decision needed on whether to address in a separate sim or amend §8.1 to mark Companions as deferred.]`
- `[GAP: T-16 Knot Propagation remains unbound — appropriate for settlement-mgmt sim scope but Module 13 audit should explicitly note threadwork-sim is the canonical binding location.]`
- `[CONFIDENCE: high — all 18 findings have explicit evidence pointers; editorial closure paths are mechanically determined, not interpretive.]`

---

## 6 — Handoff completion criteria

This handoff is complete when:
1. ☐ All 24 NERS empirical probes have been executed and results aggregated
2. ☐ Editorial P1 + P2 are complete (closes 11 findings)
3. ☐ Editorial P3 (F6 geography YAML rebuild) is complete (unblocks Mode-C/D)
4. ☐ Mode-D systematic 9-category exhaustive search is complete
5. ☐ 50-seed batch validation is complete
6. ☐ Audit reviewer checklist §4 above shows 25/25 confirmed
7. ☐ Editorial P4 isolated cleanup is complete (closes 4 findings)

**Estimated total work: ~16 hours across the remaining sessions.** ~8.5 hours NERS probes + ~7 hours editorial + remainder for Mode-D + batch.

---

## 7 — Reading order for next session

For someone resuming this work cold:

1. **Read first:** This document end-to-end.
2. **Read second:** `module_13_report.md` — the synthesis the empirical probes will be testing against.
3. **Read third:** `module_manifest.md` — the per-module verification status.
4. **Spot-check:** Run M13's `run_isolation_tests()` to confirm sim is still functional.
5. **Start work:** Begin with NERS-E-* probes (quick static analysis, ~40 min, validates the cheap Elegant priors).

**Mode G simulation `settlement_mgmt_stress_01` is structurally complete. This handoff is the bridge from "structurally complete" to "audit-confirmed and Mode-C/D unblocked."**
