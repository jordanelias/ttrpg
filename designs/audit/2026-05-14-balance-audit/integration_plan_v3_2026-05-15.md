# Valoria Integration Plan v3 — 2026-05-15

**Supersedes:** `integration_plan_2026-05-15.md` (v1), `integration_plan_v2_2026-05-15.md` (v2).
**Reason:** v2 self-audit against framework + logic/code review surfaced Phase 1a premise error (VFIVE ≠ binomial), Phase 4 sequencing error (research reads must precede implementation), Phase 5 F6 gate demotion, and six code procedure gaps. v3 bakes corrections into structure.

**Changelog v2→v3:**
- Phase 1a corrected: VFIVE mean=0.4/var=0.64 per die; target p_hit=0.4 φ≈2.67 (was: "find φ matching v12c binomial" — wrong, v12c is not binomial)
- Phase 4 split: 4-read (before Phase 2) and 4-write (after Phase 2)
- Phase 5 F6 demoted from gate to limitation
- Phase 2 unit-movement gap surfaced as Jordan decision
- Code discipline: sim_fabrication_check citations, sweep-all-to-JSONL, Wilson CI balance test, context_gate in sweep loop, safe_session_close per phase, ED filing before propagation commits
- Sequencing graph redrawn

---

## §1 Executive Summary

Five active workstreams in `jordanelias/ttrpg` over 2026-05-10..15 (281 commits):

| # | Workstream | Head | Status |
|---|---|---|---|
| A | Strategic faction balance sim | `a5ee7402` (v15) | Regressed from v12c 25/25/25/25 to 46/53/1/0 |
| B | Tactical mass-battle sim | `f8f2390` (v25) | 3/11 battery in band |
| C | Personal combat (weapon v2) | `4d89cbb` (PP-718 revert) | Post-revert; needs ratification check |
| D | Settlement management | `6c9cdd3` (Module 13 FINAL) | Structurally complete |
| E | Pre-firearms research | `8c51f23` + Chunks 0-5 | Research complete; integration pending |

**Critical regression:** v12c (`42aa952`) achieved 25/25/25/25 at N=1000. v13→v14→v15 dropped Restoration Movement world process + Altonian Reinforcements + tuned params (consent 0.28, lapse 0.90, victory 11/15) while improving sim architecture. Recovery is Phase 1.

**v12c dice are VFIVE, not binomial.** `VFIVE = [-1,0,0,0,0,0,1,1,1,2]` per `mc_v4.py`. Mean 0.4/die, variance 0.64/die, range [-1,2]. v15 quasibinomial at p=0.5 φ=1.0 has mean 0.5/die, variance 0.25/die. Phase 1a calibrates quasibinomial to match VFIVE distribution (p_hit=0.4, φ≈2.67), not merely "match variance."

---

## §2 Workstream State — Filepath Inventory

### §2.1 Workstream A — Strategic faction balance sim

**Sim chain** (`designs/audit/2026-05-14-balance-audit/sim/`):
- `mc_v4.py` — VFIVE dice, `roll_pool()`, `resolve_degree()`, canonical territories, Faction/Territory classes
- `mc_v5.py` — `pool_and_ob_v5()`, `score_action_v5()`
- `mc_v6.py` — `apply_outcome_v6()`, parameterized consent/appease/acquisition gating
- `mc_v8.py` — `reset_seasonal_v8()`; Vaynard's Hall + Charter of Liberties introduced
- `mc_v12c.py` ← **balanced reference** (commit `42aa952`); imports v4/v5/v6/v8
- `mc_v15.py` ← current head (`a5ee7402`); self-contained quasibinomial architecture

**Design chain** (`designs/audit/2026-05-14-balance-audit/`):
- `README.md` — 13-part audit overview
- `comprehensive_audit_all_directions_2026-05-14.md` (37k) — NERS-rated all-directions
- `part6_bottom_up_v3sim_2026-05-14.md` — bottom-up methodology
- `part7_canonical_v5sim_2026-05-14.md` — canonical v5 baseline
- `part8_sensitivity_synthesis_2026-05-14.md` — Q-1/Q-3/Q-4 leverage ranking
- `part9_character_decoupling_2026-05-14.md` — Almud vs Crown
- `part10_crown_initiative_design_2026-05-14.md` (21k) — Crown Initiative 3 modes (Royal Progress / Great Work / Coronation Renewal)
- `part11_throughline_meta_audit_2026-05-14.md` — PP-674 framework audit
- `part12_v8_refutation_2026-05-14.md` — symmetric-analog-cards hypothesis refuted
- `part13_integrated_balance_solution_2026-05-14.md` — RC-v1 ratification slate
- `part16_v15_quasibinomial_checkpoint.md` — v15 architecture checkpoint
- `faction_balance_convergence_v12c_2026-05-14.md` ← **operative balance spec**
- `mechanical_log_specification_2026-05-14.md` — JSONL log schema
- `handoff_2026-05-15_v15.md` — v15 handoff (SUPERSEDED by this plan)

**Canonical design docs needing propagation FROM audit thread:**
- `designs/provincial/victory_v30.md` — does not yet reflect Einhir Revival, Parliamentary Transfer, Altonian Reinforcements, RM, Crown Initiative, 11/15 threshold
- `designs/provincial/peninsular_strain_v30.md` — §5.4 still labels Cultural Reformation STRUCK without naming Einhir Revival as replacement
- `designs/provincial/faction_layer_v30.md` — Charter of Liberties, Altonian Reinforcements, Parliamentary Transfer not documented
- `designs/provincial/faction_state_authoring_v30.md` — `primary_objective` fields still reference struck paths
- `designs/provincial/faction_canon_v30.md` — Stage 1 Crown+Church only; Hafenmark+Varfell sheets pending
- `designs/provincial/ci_political_v30.md` — current

### §2.2 Workstream B — Tactical mass-battle sim

**Sim chain** (`tests/sim/`):
- `sim_mb_06_v8.py` through `sim_mb_06_v25.py` (18 versions)
- `sim_mb_06_v25.py` ← current head (`f8f2390`): 41×42 geometry, sightline, dynamic wide-wing pathing
- `HANDOFF_v22.md` — 4 priorities resolved (BIAS-1, GEO-1, D-3, D-5)
- `coverage_matrix.md` — battery state by version
- `instrument_battle.py` — instrumentation tool

**Canonical doc:**
- `designs/provincial/mass_battle_v30.md` — §A.3b geometry committed `c695921`
- `params/mass_combat.md` — unit stats + tactic cards

**Open from v25 handoff:** ANGLE_DMG_MULT unwired, 17-row vertical gap, arrowhead tip H2/H9 out of band, battery 3/11

### §2.3 Workstream C — Personal combat

**Post-PP-718 revert state:**
- `params/combat.md` — canonical pool/Health/MW/crit/three-axis weapons
- `designs/scene/derived_stats_v30.md` — PP-718 revert (`4d89cbb`)
- `designs/scene/combat_v30.md` — round structure, phases
- `tests/sim/duel_architecture_stress_01/` — sim chain through v9 final

### §2.4 Workstream D — Settlement management

**Complete:**
- `tests/sim/settlement_mgmt_stress_01/` — 13/13 modules, 500-seed batch (`e1553ed`)
- Canonical: `designs/territory/settlement_layer_v30.md`, `settlement_adjacency_v30.md`, `valoria_geography_v30.yaml`, `territory_temperaments_v30.md`
- Open: F6 geography YAML rebuild (blocks Mode-C, does NOT block integration runner)

### §2.5 Workstream E — Pre-firearms research

**Research** (`research/pre_firearms_formations/`): 17 files, ~6000 lines; `14_methodology_audit.md` + `15_methodology_resolutions_handoff.md` + `16_historical_research_vs_game_design_critical_comparison.md`

**Comparative audit** (`designs/audit/2026-05-15-mass-battle-comparative/`):
- `chunk_0_framing.md` (`6d2fdf2`)
- `chunk_1_scale_geometry_phase.md` (`6d2fdf2`)
- `chunk_2_unit_primitives_formation_taxonomy.md` (`74c1972`)
- `chunk_3_resolution_mechanics_command_timing.md` (`eadd582`)
- `chunk_4_cohesion_rout_pursuit_pipeline.md` (`90a4e95`)
- `chunk_5_environment_terrain.md` (`dc4d40d`)

**NERS layer:** `tests/audit/all_directions_ners_v27.md` (`8c51f23`)

---

## §3 Regression Forensic

### §3.1 What v12c had that v15 dropped

| # | Mechanic / parameter | v12c spec (convergence §4) | In v15? |
|---|---|---|---|
| 1 | Einhir Revival (Varfell) | §4.1: pool I+1, Ob max(1, 1+PT×weight), no Sta penalty on Failure | ✓ (verify small differences) |
| 2 | Restoration Movement world process | §4.2: per arc; P(PT−1) = min(0.8, chance × (base + growth×(arc−1))) per non-Church non-Inquisitor territory | ✗ DROPPED |
| 3 | Altonian Reinforcements (Hafenmark) | §4.3: auto arc boundary; gate I≥5; pool I, Ob 3; OW only → Mil+1 permanent | ✗ DROPPED |
| 4 | Parliamentary Territory Transfer | §4.4: 1/arc; pool I, Ob Holder.L + bonus; consumes CB; Failure → Sta−1 + Holder L+1 | ✓ (verify CB sources match) |
| 5 | Treaty Expiration 90%/arc lapse | §4.5 | ✓ but tuned to 0.7, not 0.90 |
| 6 | EA throttle every-arc | §4.6 | ⚠ verify `ea_arc_used` semantics |
| 7 | Tuned params | consent 0.28, lapse 0.90, RM decay 0.35, Altonian I-gate 5, victory 11/15 | ✗ v15: consent 0.4, lapse 0.7, 15/15 |

### §3.2 Dice distribution mismatch

v12c: `VFIVE = [-1,0,0,0,0,0,1,1,1,2]` sampled via `random.choice`, integer pools.
v15: `quasibinomial_successes(pool, p_hit=0.5, dispersion=1.0)` with fractional pools.

| | VFIVE (per die) | Quasibinomial (p=0.5, φ=1) |
|---|---|---|
| Mean | 0.40 | 0.50 |
| Variance | 0.64 | 0.25 |
| Range | [-1, +2] | [0, pool] clamped |
| Negative results | Yes (−1 face) | No (clamped ≥ 0) |

To match VFIVE in quasibinomial framework: set `p_hit = 0.4`, `φ = 0.64 / (0.4 × 0.6) ≈ 2.67`.

Remaining mismatch: VFIVE can produce negative per-die outcomes (−1 face); quasibinomial clamps at 0. At pool 4 Ob 4, VFIVE E[sum]=1.6 with non-negligible P(sum<0); quasibinomial at p=0.4 E[sum]=1.6 but floor 0. This asymmetry affects Failure-vs-deep-Failure rates specifically. **For balance purposes** (win% over N=1000 campaigns, not degree distribution), this is likely second-order — verify empirically in Phase 1a.

### §3.3 v12c result vs v15 result

| Faction | v12c (N=1000) | v15 (N=100) |
|---|---|---|
| Crown | 24.7% | 46% |
| Church | 28.6% | 1% |
| Hafenmark | 24.2% | 53% |
| Varfell | 22.5% | 0% |
| Spread | 6.1pp | 53pp |

---

## §4 Integration Architecture

```
                  Workstream A (strategic sim, arc-scale)
                            ↓ Military Conquest action
                  Workstream B (tactical sim, battle-scale)
                            ↓ when PC present (mass_battle §B.5)
                  Workstream C (personal combat, tick-scale)

   Workstream D (settlement state) ─── underpins ── A, B
   Workstream E (research) ──────── informs ──── B canon
```

**Boundaries:**

| Boundary | Current | Target | Risk |
|---|---|---|---|
| A → B | pool faction.Mil vs Ob 4, single roll | A invokes B BG resolution sequence (§B.3 6-step) with unit roster + terrain + tactic cards | Variance + state expansion |
| B → C | Specified in §B.5 | TTRPG rules for PC actions during PC-present battle | C ratification stability |
| D → A | Settlement M1 REGISTRY readable | Settlement events feed arc-boundary territory state | F6 limits Mode-C but doesn't block |
| E → B | Research findings inform canon | Per-chunk propagation to `mass_battle_v30.md` | Authored-emergence risk |

---

## §5 Phased Plan

### Phase 1a — Dice distribution calibration

**Goal:** configure v15 quasibinomial to match v12c VFIVE distribution.

**Method:**
1. Compute v12c VFIVE analytical distribution at key matchups: pool 4 Ob 4, pool 4 Ob 2, pool 5 Ob 3, pool 6 Ob 4
2. Compute quasibinomial at p_hit=0.4, φ=2.67 for same matchups
3. Compare: P(Failure), P(Partial), P(Success), P(Overwhelming) per matchup
4. If ≤2pp deviation across all matchups at these params: accept p=0.4 φ=2.67
5. If >2pp deviation: test whether the clamping floor (no negative outcomes) is the cause; if so, implement signed quasibinomial (allow negative net successes) as variant
6. If quasibinomial fundamentally cannot match VFIVE: fallback to VFIVE sampling in v15 architecture with probabilistic rounding for fractional pools (`floor(pool) + Bernoulli(pool - floor(pool))` extra die)

**Deliverable:** `designs/audit/2026-05-14-balance-audit/variance_calibration_v16_2026-05-15.md` documenting: chosen sampling parameters, per-matchup comparison tables, decision rationale.

**Duration:** <1 session (analytical + small validation runs).

### Phase 1b — Balance parameter discovery

**Goal:** restore 25/25/25/25 ± 5pp on v15 architecture with calibrated dice and all v12c mechanics.

**Mechanics to port from `mc_v12c.py` → new `mc_v16.py`:**

| Mechanic | Source function/section in v12c | Action |
|---|---|---|
| Restoration Movement | v12c lines TBD (world process in seasonal loop) | Port entirely; not in v15 |
| Altonian Reinforcements | v12c arc-boundary block | Port entirely; not in v15 |
| Einhir Revival | v15 lines 265-272, 396-402, 457-458, 623-635 | Verify match with v12c §4.1; reconcile differences |
| Parliamentary Transfer | v15 lines 279-283, 410-412, 463-465, 652-664 | Verify CB source chain matches v12c §4.4.1 |
| Treaty Expiration rate | v15 line 467 (0.7) | Change to 0.90 per v12c §4.5 |
| EA throttle | v15 `ea_arc_used` | Verify = every-arc per v12c §4.6 |
| Victory threshold | v15 (15/15) | Change to 11/15 per v12c §5.1 |
| Consent rate | v15 best config (0.4) | Change to 0.28 per v12c §5.1 |
| Dice | v15 quasibinomial p=0.5 φ=1 | Apply Phase 1a calibration (p=0.4 φ=2.67 or VFIVE fallback) |

**Parameter sweep:**
- Sweep: CONSENT_RATE (0.25, 0.28, 0.30, 0.33) × TREATY_LAPSE_RATE (0.85, 0.90, 0.95) × RM_PT_DECAY_CHANCE (0.30, 0.35, 0.40) × VICTORY_THRESHOLD (11) = 36 configs at N=1000 each
- Record ALL configs to `designs/audit/2026-05-14-balance-audit/data/sweep_v16_results.jsonl`
- Success criterion: Wilson score 95% CI for all four factions overlaps [20%, 30%]
- Sensitivity table output analogous to `part8_sensitivity_synthesis`

**Code discipline:**
- All mechanical constants annotated `# [canonical: convergence_v12c §4.N]` or `# [PROVISIONAL: pending canonization — PROP-NN]`
- `h.context_gate()` every 10 configs in sweep loop
- `sim_fabrication_check` ledger entries for: RM_PT_DECAY_CHANCE, RM_BASE_STRENGTH, RM_GROWTH_PER_ARC, ALTONIAN_I_GATE, CONSENT_RATE, TREATY_LAPSE_RATE, VICTORY_THRESHOLD

**Commit:** `mc_v16.py` + `variance_calibration_v16_2026-05-15.md` + `sweep_v16_results.jsonl` via `h.safe_commit()`. Message: `[simulation] v16 — restore v12c balance (RM, Altonian, calibrated dice p=0.4 φ=2.67, 11/15) on v15 quasibinomial architecture`.

**Duration:** 1-2 sessions.

### Phase 4-read — Research chunk intake (BEFORE Phase 2)

**Goal:** read Chunks 0-5 + research methodology to inform Phase 2 implementation. No commits — read-only.

**Files to read:**
- `designs/audit/2026-05-15-mass-battle-comparative/chunk_0_framing.md`
- `chunk_1_scale_geometry_phase.md`
- `chunk_2_unit_primitives_formation_taxonomy.md`
- `chunk_3_resolution_mechanics_command_timing.md`
- `chunk_4_cohesion_rout_pursuit_pipeline.md`
- `chunk_5_environment_terrain.md`
- `research/pre_firearms_formations/14_methodology_audit.md`
- `research/pre_firearms_formations/15_methodology_resolutions_handoff.md`

**Per-chunk emergence verification:** for each proposed rule, test: does it produce emergence (terrain × unit × tactic → outcome) or does it script an outcome? If scripted: flag for redesign. Failure Lexicon "authored emergence" — Μ-β violation.

**Deliverable:** reading notes with per-chunk: (a) rules that inform Phase 2 BG resolution API, (b) rules that inform Phase 4-write canonization, (c) emergence flags.

**Duration:** 1 session (read-only, no commits).

### Phase 2 — Mass-battle integration + Workstream C prerequisite

**Prerequisite — Workstream C ratification.**
- Confirm `4d89cbb` (PP-718 revert) is Jordan-ratified stable
- If volatile: block Phase 2 until ratified
- If ratified: tag in `canon/patch_register_active.yaml`

**Step 2a — Workstream C API surface.**

Define entry points for B→C during PC-present mass battle per `mass_battle §B.5`:
- `resolve_pc_action(pc_state, action, target, environment)` — single PC action
- Returns: result, pool/Ob used, damage, stamina/wound delta
- Source: `designs/scene/combat_v30.md` action set, `params/combat.md` stats

Filepaths: `tests/sim/duel_architecture_stress_01/`, `designs/scene/combat_v30.md`, `params/combat.md`

**Step 2b — Workstream B API surface.**

Define `sim_mb_06.resolve_battle()` per `mass_battle §B.3` 6-step BG resolution sequence — NOT "single opposed roll":
1. Tactic card declaration (attacker, defender)
2. Disposition table lookup → Ob modifier
3. Attacker pool: Σ(engaged unit Martial) + floor(faction.Mil / 2); Defender pool: same + Fort dice
4. Both roll (TN 7 per §B.3, or calibrated from Phase 1a); net = attacker − defender
5. Margin: ≥+2 attacker wins, ≤1 either direction partial, ≥+2 defender wins
6. Outcome application: territory transfer (if attacker wins), unit losses, Accord, Stability triggers

Inputs: `attacker_faction, defender_faction, attacker_units: dict[unit_class, int], defender_units, terrain_type, fort_level, tactic_card_attacker, tactic_card_defender, pc_present: bool`

Branch: `pc_present=False` → BG resolution sequence (Steps 1-6); `pc_present=True` → full tick sim with C invocation for PC actions

Outputs: `BattleResult(winner, attacker_losses, defender_losses, territory_transferred, accord_outcome, stability_triggers)`

**Step 2c — Unit-token state in Workstream A.**

Add to `mc_v16.py` → `mc_v17.py`:
```python
from collections import defaultdict
# Schema-complete (9 classes per mass_battle §B.2), semantics-partial (3 initially)
self.units = defaultdict(lambda: defaultdict(int))
# Active classes: 'Levy', 'LightInf', 'HeavyInf'
# Reserved: 'Cavalry', 'Archer', 'Crossbow', 'Sling', 'Artillery', 'KnightsTemplar'
```

Serialization: `json.dumps({k: dict(v) for k, v in faction.units.items()})` — defaultdict doesn't serialize directly.

Muster action: mints Levy tokens in territory (expandable to per-faction recruitment doctrine later).
Conquest action: commits tokens from territory to battle.

**`[GAP: unit movement model — Jordan decision required]`**

How do units reach the target territory for Conquest?
- **(a)** Commit from any controlled territory (simplest; loses March strategic cost)
- **(b)** Commit from adjacent-to-target only (closer to canon; adds March prerequisite)
- **(c)** Floating "army" pool not per-territory (closest to current v15 faction.Mil architecture)

Recommend (b) for canon fidelity, with March as implicit (no separate March action; adjacency requirement models it). But this is Jordan's decision.

**Step 2d — Integration + balance verification.**
- N=1000 balance battery with v16 parameters + mass battle → v17
- Wilson CI check: all factions [20%, 30%] at 95%
- N=100 PC-present scenarios for C invocation end-to-end
- Performance profile: target <20 min for N=1000 BG-resolution-only campaigns

**Code discipline:**
- `sim_fabrication_check`: cite `mass_battle_v30.md §B.3` for resolution constants; cite `mass_battle_v30.md §B.2` for unit Martial/Endurance/Discipline stats; ANGLE_DMG_MULT and FLANKED_BONUS marked `[PROVISIONAL: pending Phase 4-write canonization]`
- `h.context_gate()` in battle-resolution loop
- `h.safe_commit()` for v17

**Commit:** `mc_v17.py` + `sim_mb_06_v26.py` (with `resolve_battle()` API) + `sim_mb_06_api_v1.md` via `h.safe_commit()`.

**Duration:** 3 sessions.

### Phase 3 — Documentation propagation

Split into 3a (pure propagation) and 3b (ratification request). Can run in parallel with Phase 1b.

**Pre-commit requirement:** file EDs in `canon/editorial_ledger.yaml` for each PROP item BEFORE propagation commits. PROP-05 is 3b, not 3a.

**Phase 3a — Pure propagation** (mechanics already Jordan-ratified via RC-v1 / v12c convergence):

| ID | Mechanic | From (audit thread) | To (canonical doc) | Action |
|---|---|---|---|---|
| PROP-01 | Einhir Revival | `convergence §4.1` | `peninsular_strain_v30.md §5.4` | Replace STRUCK Cultural Reformation with Einhir Revival spec |
| PROP-02 | Restoration Movement (world process) | `convergence §4.2` | `peninsular_strain_v30.md` new §4.5 or `victory_v30.md §8` extension | RM as autonomous world process (distinct from RM-as-faction) |
| PROP-03 | Altonian Reinforcements | `convergence §4.3` | `faction_layer_v30.md §3 Treaty Mechanics` | Trigger, pool, Ob, OW-only Mil gain |
| PROP-04 | Parliamentary Territory Transfer | `convergence §4.4` | `faction_layer_v30.md §5 Parliamentary Mechanics` | CB sources, four modes, last-territory protection |
| PROP-06 | EA throttle every-arc | `convergence §4.6` | `faction_canon_v30.md §Church EA` | Throttle spec |
| PROP-07 | Victory threshold 11/15 | `convergence §5.1` | `victory_v30.md §0` + `peninsular_strain_v30.md §6.1` | Replace 15/15 throughout |
| PROP-08 | Crown Initiative 3 modes | `part10_crown_initiative_design` | `victory_v30.md §3.1` + `faction_canon_v30.md §Crown` | Royal Progress / Great Work / Coronation Renewal |
| PROP-09 | Vaynard's Settlement + Vaynard's Hall | sim source | `peninsular_strain_v30.md §5` Varfell + `faction_canon_v30.md` Varfell sheet | Both action specs |
| PROP-10 | Charter of Liberties | sim source | `faction_canon_v30.md §Hafenmark` | Wealth-cost action spec |

**Faction sheet completion:**
- Hafenmark sheet — new in `faction_canon_v30.md`
- Varfell sheet — new in `faction_canon_v30.md`
- Crown + Church Stage 1 sheets — update with Crown Initiative / EA throttle / Mass Seizure

**P2 cleanup:**
- `faction_state_authoring_v30.md §§2-7` — rewrite `primary_objective` to `victory.peninsular_sovereignty`
- `peninsular_strain_v30.md §5.2` — rename "Graduated Seizure" to "Mass Seizure (one-shot)"
- `designs/audit/2026-05-14-balance-audit/README.md` — update §asymmetric balance hypothesis (Jordan-rejected per v12c §1)
- Mark v15 handoff SUPERSEDED

**Code discipline:** each commit via `h.safe_commit()` with co-file rules (SHA update in `canonical_sources.yaml` where applicable), Solmund grep, editorial markers `[ED-NNN]`.

**Phase 3b — Ratification request (PROP-05):**

| ID | Mechanic | Status |
|---|---|---|
| PROP-05 | Treaty Expiration 4-season → 90% per-arc | Jordan-implicit via RC-v1; `victory §3.1` canonical text still says 4-season. Request explicit ratification before propagating. |

**Duration:** 1-2 sessions (parallelizable with Phase 1b).

### Phase 4-write — Research canonization (AFTER Phase 2)

**Goal:** propagate Chunk 0-5 findings (vetted in Phase 4-read) into canonical docs.

**Per-chunk targets:**

| Chunk | Target file | Section |
|---|---|---|
| 1 (scale/geometry/phase) | `mass_battle_v30.md §A.3 / §A.3b` | Verify + extend |
| 2 (unit primitives / formation) | `mass_battle_v30.md §B.2` + `params/mass_combat.md` | Unit roster |
| 3 (resolution / command / timing) | `mass_battle_v30.md §B.3` | Resolution refinements |
| 4 (cohesion / rout / pursuit) | `mass_battle_v30.md §A.12` + new sections | Cohesion-rout-pursuit pipeline |
| 5 (environment / terrain) | `mass_battle_v30.md §A.9` | Environmental modifiers |

**Per-rule emergence check:** must produce emergence, not script outcomes. Failure Lexicon "authored emergence" = Μ-β violation → redesign or reject.

**Code discipline:** cite Phase 4-write canonized sections in v26/v17 sim constants, removing `[PROVISIONAL]` flags.

**Duration:** 2-3 sessions.

### Phase 5 — Settlement state integration

**F6 geography YAML status:** demoted from gate to limitation. F6 blocks Mode-C YAML scenarios but does NOT block integration runner — `module_13_FINAL` reads from M1 REGISTRY (canonical settlement IDs). Phase 5 can proceed; Mode-C scenarios deferred until F6 closes.

**Steps:**
1. Confirm `module_13_FINAL_integration_runner.py` exports invocable library interface
2. Define settlement → territory aggregation: settlement state → per-territory Accord/PT/infrastructure
3. Replace v17 territory state initialization with settlement-aggregate from M1 REGISTRY
4. At arc boundary: feed settlement events (revolts, famines, Domain Echoes) into territory state
5. Verify RM growth matches `convergence §4.2` expectations when settlement-driven instability feeds territory-level Accord

**Balance check:** N=1000 with settlement integration → expect 25/25/25/25 ± 5pp preserved. Wilson CI.

**Duration:** 1-2 sessions.

---

## §6 Pre-Execution Discipline

Before each phase begins:

| Check | What | Failure response |
|---|---|---|
| **T-coverage** | Enumerate throughlines touched; classify as extend/preserve/break | Cannot proceed until enumerated |
| **Emergence check** | Per new rule: produces emergence or scripts outcome? | If scripted → redesign or reject |
| **Variance check** | Does this phase change dice distribution or pool/Ob ranges? | Document expected impact; verify empirically |
| **Prereq verification** | Phase-specific prerequisites met? | Block if not |
| **Bootstrap fresh** | `h.assert_bootstrap()` + `h.task_gate()` | Stop if fails |
| **Last 5 commits + audit-dir READMEs** | Read before fetching task files | Prevents v1-class blind spots |
| **`h.context_gate()`** | Every ~10 tool calls or ~10 sweep configs | Hard stop at 90% |
| **`g.safe_session_close()`** | At phase completion | Prevents session log staleness |

---

## §7 Sequencing + Dependency Graph

```
Phase 1a (dice calibration)
    │
    ▼
Phase 1b (parameter sweep + v16 commit)
    │
    ├──────────────────────────┐
    ▼                          ▼
Phase 4-read (research intake) Phase 3a (doc propagation, parallelizable)
    │                          │
    ▼                          ▼
Phase 2 prereq (C ratif.)     Phase 3b (PROP-05 ratification request)
    │
    ▼
Phase 2 (mass battle + C + v17 commit)
    │
    ├──────────────────────────┐
    ▼                          ▼
Phase 4-write (canon chunks)  Phase 5 (settlement integration)
    │                          │
    └──────────┬───────────────┘
               ▼
          Phase 6+ horizon
```

**Critical path:** 1a → 1b → 4-read → 2-prereq → 2 → 5. ~7-9 sessions.

**Parallelizable:** Phase 3a with Phase 1b; Phase 4-write with Phase 5.

**Blocked:** Phase 2 by C ratification + Phase 4-read. Phase 5 limited (not blocked) by F6.

---

## §8 Horizon — Phase 6+ Candidates

After Phase 5, trajectory shifts from closure to compounding-forward:

| ID | Candidate | Ω loading | Trigger |
|---|---|---|---|
| 6a | Threadwork-transition campaign arc (`research §15`) | Ω-a + Ω-b (high) | Phase 4-write complete; Jordan interest confirmed |
| 6b | Faction sheet completion (Hafenmark + Varfell in `faction_canon_v30.md`) | ○ (doc) | Phase 3a complete |
| 6c | Workstream C continued: D6 shield, group combat, Fibonacci scaling | Ω-b | Phase 2 ratification stable + Jordan direction |
| 6d | Settlement audit follow-on: 24 NERS probes, Mode-D search, F6 close | Ω-c | Phase 5 complete |
| 6e | Workstream B calibration: ANGLE_DMG_MULT, arrowhead tip, battery 11/11 | ○ (tactical) | Phase 4-write complete |
| 6f | Asymmetric balance reconsideration | Ω-d | If Jordan re-ratifies asymmetric in §9 Q1 |

---

## §9 Open Questions for Jordan

1. **Balance target.** v12c convergence §1 says symmetric 25% ± 5pp (Jordan rejected asymmetric). Confirm final. If asymmetric re-ratified, T-18 coverage restores but Phase 1b success criterion changes.

2. **Workstream C ratification.** Is `4d89cbb` (PP-718 revert — canonical pool/Health/MW/crit/three-axis weapons) ratified stable? Blocks Phase 2.

3. **PROP-05 Treaty Expiration.** 4-season fixed (current canon) vs 90% per-arc (v12c balanced). Explicit ratification needed.

4. **Phase 1a dice fallback.** If quasibinomial at p=0.4 φ=2.67 cannot match VFIVE within 2pp per matchup, approve VFIVE sampling fallback in v15 architecture (with probabilistic rounding for fractional pools)?

5. **Unit movement model.** (a) any controlled territory, (b) adjacent-to-target only, (c) floating army pool. Recommend (b). Jordan decides.

6. **Per-workstream session logs.** Should bootstrap report per-workstream status?

---

## §10 Risk Register

| ID | Risk | Severity | Phase | Mitigation |
|---|---|---|---|---|
| R-01 | p=0.4 φ=2.67 quasibinomial doesn't match VFIVE within 2pp | Med | 1a | Fallback: VFIVE sampling + probabilistic rounding (Q4) |
| R-02 | v16 sweep doesn't converge to 25/25/25/25 | High | 1b | 36 configs × N=1000; all recorded to JSONL; sensitivity surface reveals bottleneck |
| R-03 | Mass-battle integration breaks v16 balance | High | 2d | BEFORE/AFTER battery; rollback on >5pp drift |
| R-04 | Workstream C still volatile | Med | 2-prereq | Block Phase 2; surface to Jordan |
| R-05 | N=1000 × mass-battle performance intractable | Med | 2d | Profile early; BG resolution sequence (~ms per battle) is fast; full tick sim only PC-present |
| R-06 | Authored emergence in research-derived rules | Med | 4-read | Per-rule verification structural (§6) |
| R-07 | Phase 3a/1b parallel creates canonical divergence before hooks catch it | Med | 3a | Commit 3a propagation AFTER v16 committed; verify no spec drift between sim constants and canon text |
| R-08 | My prior audit defects recur | High (history) | all | §6 discipline codifies missing checks; bootstrap reads last 5 commits + audit-dir READMEs |
| R-09 | sim_fabrication_check blocks commit on uncited constants | Med | 1b, 2 | Annotate all constants with `[canonical:]` or `[PROVISIONAL:]` inline; file ledger entries pre-commit |
| R-10 | Multiple workstreams diverge during execution | Med | all | Per-workstream commit tagging; `g.safe_session_close()` per phase |

---

## §11 Framework Alignment Summary

| Phase | N | Ω served | Μ modes | М ratings | Q-N | Q-R | Q-S | Q-E |
|---|---|---|---|---|---|---|---|---|
| 1a+1b | ✓ | Ω-d (no dominance) | Μ-α Μ-β Μ-δ | M-1+ M-3✓ M-5+ M-6+ | ✓ | ✓ | ✓ (calibrated) | ✓ |
| 4-read | ✓ | refines Ω | read-only | read-only | — | — | — | — |
| 2 | ✓ | Ω-a/b/c/d (full) | Μ-β Μ-δ | M-5+ M-2✓ M-7+ | ✓ | ⚠ perf | ✓ (§B.3 6-step) | ⚠ unit state |
| 3a | ✓ | ○ (doc) | ○ | ○ | ✓ | ✓ | ✓ | ✓ |
| 4-write | ✓ | refines Ω | Μ-α Μ-δ | M-1+ M-2+ M-10+ | ✓ | ✓ | ✓ | ✓ (emergence checked) |
| 5 | ✓ | Ω-a Ω-c | Μ-β Μ-δ | M-5+ M-7+ | ✓ | ✓ | ✓ (F6 limits, not blocks) | ✓ |

All Ω clauses served. No silent failures. Momentum shifts from closure (Phases 1-3) to compounding-forward (Phases 4-6+) by design.
