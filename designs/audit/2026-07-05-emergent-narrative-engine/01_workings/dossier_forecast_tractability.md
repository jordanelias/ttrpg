# Dossier — FORECAST Tractability (Churn Engine v2 forward-probability layer)

## Status: working record
## Date: 2026-07-05 · Lane: IN · Branch: `claude/ners-audit-fable5-9cpfdz`

**Scope.** Whether the v2 FORECAST layer — compute, each Accounting, the forward probability
field over the strategic state graph via (a) analytic threshold-hitting horizons and (b) a seeded
ensemble rollout (N≈32–128 × k≈4 seasons) that **reuses the live resolver code paths** — is
tractable, and in what shape. Grounded in the working tree (sim/, params/, designs/, canon/).
Cites `file:line`. Charter constraints: `00_grounding/00_engine_charter.md` C1 (no runtime LLM,
deterministic), C3 (book venues, never own resolution), plus the §4 replay-determinism contract of
`narrative_engine_design_v1.md` and its s4 substrate spec. Port↔oracle discipline: CLAUDE.md §7.

**Note on prior art.** No `Churn Engine` / `FORECAST` doc exists in the corpus yet
(`grep -rln "Churn Engine\|forward probability\|ensemble rollout"` → empty). This dossier is
green-field tractability analysis against the existing sim + resolver substrate.

---

## VERDICT

**Tractable — as a TWO-LAYER forecast, not a single ensemble.**

- **Layer A (analytic, near-free): the clock/echo horizon layer.** Every *continuous* state
  variable (faction stats, clocks, tracks) advances each season by a step whose distribution is
  **closed-form** — the two resolver families both expose extractable degree distributions, and
  Domain Echo maps degree→±1/±2 by a zero-RNG table (`sim/cross_scale/domain_echo.py:27-33`). So
  per-step expected drift and variance are computable in closed form, and threshold-hitting
  horizons for drift-like clocks reduce to a Normal first-passage estimate — no sampling.
- **Layer B (seeded ensemble, cheap at strategic cadence): the structural-branch layer.** The
  sources EV-mode *cannot* cleanly collapse — discrete AI action choice, event-deck card draws,
  insurgency emergence, target selection — must be **sampled through the live code**
  (`sim.mc_v18.run_campaign`), which is exactly the port↔oracle-safe path (same functions, seeded
  RNG). 64×4 rollouts per Accounting is comfortably desktop-affordable **provided scenes are never
  rolled** (strategic cadence only).

The binding risks are not compute: they are (1) ~19 sim stubs (`npc_ai`, `ip_track`, `rs_track`,
several provincial actions) and the event deck existing only as a PROPOSAL, so several branch
sources cannot be rolled today; and (2) the absence of a balance regression oracle (CLAUDE.md §7 —
a seeded batch already yields a degenerate ~87%/0%/0% win-share that nothing flags), which means
the ensemble's *outputs* have no trusted baseline yet.

---

## Q1 — BRANCH-SOURCE CENSUS

For each source: transition dynamics, and whether one-step transition is **analytic**
(drift+threshold → hitting time / closed-form EV) or needs **sampling**.

| # | Source | Where (file:line / doc) | One-step dynamics | Analytic or sample? |
|---|---|---|---|---|
| 1a | **Pure-drift clocks** — MS baseline −1/in-game-year; CI passive +1/season (PP-402) | `params/core.md:96-101` (MS); `params/factions/stats_1_7_scale.md:107-108` (CI); `sim/peninsular/accounting.py:53-58` | Deterministic linear drift | **Analytic** — hitting time = (threshold − x₀)/rate exactly |
| 1b | **Accounting-perturbed clocks** — CI *generation* (PP-412 5-step), IP, Turmoil, Accord | `sim/peninsular/ci_track.py apply_seasonal_ci`; `clock_registry_v30.md:16-19` | Deterministic base + state-dependent delta; some stochastic (insurgency-driven) | **Analytic if per-season delta distribution known** (usually a small closed-form); else sample |
| 2 | **Faction stat deltas via Domain Echo** — degree→stat | `domain_echo.py:27-33,79-124`; `params/scale_transitions.md:31-34`; `params/core.md` echo cap ±2 | degree map is a **zero-RNG table**; only the *degree* is stochastic | **Analytic EV**: E[Δstat] = Σ P(deg)·amount, cap ±2 |
| 3 | **NPC/faction priority trees (GD-2)** | `canon/02_canon_constraints.md:39` (GD-2 def); `sim/provincial/faction_action.py:48-77` | **NOT fully deterministic.** GD-2 mandates only that a *deterministic mandatory threat-response pass PRECEDES* stochastic selection. Candidate selection is stochastic: `faction_action.py:55 roll = rng.random()` picks unique/conquest/muster/govern; `:159 target = rng.choice(targets)` | **Sample** (discrete branch — see Q3 limitation). *Corrects the task's "deterministic per GD-2" premise.* |
| 4a | **Scene/contest/combat draws — dice** | `params/core.md:58-80` (Decision-E continuous engine); `sim/autoload/sigma_leverage.py:234-250 p_success`, `dice_engine.continuous_engine_sample` | `net ~ Normal(μ·N, σ·√N)`; P(success)=Φ((μN−(Ob−0.5))/(σ√N)) | **Analytic** — degree probs are Φ at each band boundary |
| 4b | **Faction bare-stat draws — domain resolver** | `params/factions/stats_1_7_scale.md:64-84`; spec `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md:26-40` | `P_success=clamp(0.5+0.1·M, .05,.90)`; `P_ovw`, `P_partial` bands explicit | **Analytic** — the four degree probabilities ARE the closed form |
| 5 | **Event decks** — settlement governance deck; Π homeostat | `designs/territory/governance_play_redesign_v1.md:91-104,147` — draw `1+⌊Π/3⌋` cards, weighted/filtered by predicate | Π recompute deterministic; **card draw is stochastic categorical** | **Sample** (categorical); EV = weighted expectation over eligible cards. ⚠️ PROPOSAL only — not in sim |
| 6 | **Ambition / project graphs** | `designs/npcs/npc_behavior_v30.md` §Projects; `sim/autoload/npc_ai.py:22-27` | **STUB** — `select_action`/`evaluate_priority_stack` raise NotImplementedError | Cannot roll today. NPE stance-drift (`sim/world/npe.py`, Volatility roll) is a partial proxy — **sample** |
| 7 | **Insurgency pipeline (GD-3)** | `sim/world/insurgency_pipeline.py`; `accounting.py:60-73` | Deterministic threshold triggers (2+ contiguous Uncontrolled, streaks) + promotion checks | **Analytic** emergence (threshold on settled state); promotion partly deterministic |

**Census gist.** The *continuous* layer (1a, 2, 4a, 4b, and the deterministic parts of 1b/7) is
fully analytic — this is the majority of the strategic state's motion and it needs **no sampling**.
The *discrete/structural* layer (3 AI action & target choice, 5 deck draws, 6 ambitions) is
irreducibly stochastic and must be sampled through the live code. #6 is blocked on stubs; #5 is
blocked on the deck being a PROPOSAL.

---

## Q2 — REUSABLE MACHINERY

Concrete modules + entry points the ensemble can reuse. Runnable-headless-today unless flagged.

**Reuse AS-IS (the ensemble spine):**
- `sim/mc_v18.py:86 run_campaign(seed, max_seasons, params) -> CampaignResult` and
  `:140 run_batch(n, base_seed, params)` — **the seeded campaign runner.** Each forecast future =
  `run_campaign(seed=derived, max_seasons=k)`. `run_batch` already loops N seeded campaigns
  (`:146 seed=base_seed+i`). This is the ensemble entry point, verbatim.
- `sim/peninsular/season.py:48 run_season(world, action_callback)` — one season step; the
  `action_callback` seam (`mc_v18._faction_actions_callback:62`) is exactly where a forecast
  injects "no-intervention" vs "player-lever" policies.
- `sim/peninsular/accounting.py:37 run_accounting(world)` — the deterministic Accounting pass (CI,
  MS, insurgency, NPE). Runnable headless today.
- `sim/autoload/game_state.py:189 create_world(seed)` + `serialize_world` — snapshot/restore for
  branching from the live state at the Accounting boundary.
- `sim/cross_scale/domain_echo.py:79 compute_domain_echo(degree, scope_met, ...)` — degree→delta,
  **table lookup, zero RNG** (`s4_substrate.md:454` confirms "zero RNG"). Reusable as the EV-delta
  kernel.
- `sim/autoload/victory.py check_all_factions` — GD-1 termination check per rolled future.
- `sim/world/insurgency_pipeline.py` (`check_insurgency_triggers`, `check_insurgency_promotion`) +
  `sim/world/npe.py simulate_npc_actions` — both invoked from accounting today.

**Reuse AS-IS (the EV-mode primitives — already exist):**
- `sim/autoload/sigma_leverage.py:229 _phi` (Φ via `math.erf`) and `:234 p_success(base_ob, pool,
  net_sigma, tn)` → `1 − Φ(z)`. **This is the closed-form EV primitive the analytic layer needs.**
- `sim/autoload/dice_engine.py:77 continuous_engine_sample`, `:94 degree_from_net` — sampled-mode
  draw + degree binning.
- `sim/personal/contest/resolver.py:24` imports `effective_ob, degree, net_boost` from
  `sigma_leverage` — single-sourced σ-kernel (no parallel model).

**Reuse WITH thin wrapper:**
- `sim/provincial/faction_action.py:48 faction_take_action(faction, world, rng)` — the faction AI
  step; sampled-mode reuses verbatim. For EV-mode it needs a branch-enumeration wrapper (the
  `roll<0.30/0.65/0.85` cascade is a fixed categorical → enumerable).
- `tests/sim/mass_battle/engine.py:354 resolve_battle` — mass-battle resolver, separate but works;
  only needed if forecast rolls battles (recommend EV-summarize instead).

**STUBS — cannot roll today** (NotImplementedError; CLAUDE.md §7's ~19):
- `sim/autoload/npc_ai.py:22-27` (priority trees / ambitions — **source #6**)
- `sim/peninsular/ip_track.py:22,26` and `sim/peninsular/rs_track.py:21` (IP/RS track deltas)
- `sim/personal/contest/resolver.py:51` (`WinCondition.resolve` base — but subclasses work),
  `modes.py`, `wrapper.py`, `dictionaries.py`
- provincial actions: `varfell_territorial_acquisition`, `treaty`, `charter_liberties`,
  `home_sanctuary`, `infrastructure_reclamation`, `altonian_reinforcements`, `hafenmark_equipment`,
  `varfell_mandate_action` (all NotImplementedError)
- `sim/world/restoration_movement.py`, `sim/world/miraculous_event.py`, `sim/thread/rendering.py`,
  `sim/cross_scale/articulation.py`, `sim/personal/{fieldwork,companion,investigation,tribunal}.py`
- **Event deck (source #5): no implementation at all** — `governance_play_redesign_v1.md` is a
  2026-06-22 PROPOSAL.

---

## Q3 — SHARED-CODE FEASIBILITY (EV-mode vs sampled-mode)

**(b) Sampled mode — YES, trivially and safely.** `run_campaign` already draws through the true
functions with `world.rng`. A forecast future is `run_campaign(seed=derived_seed, max_seasons=k)`.
This is the canonical port↔oracle path (CLAUDE.md §7) — no parallel model, by construction.

**(a) EV mode — YES for every CONTINUOUS resolver; NO (cleanly) for DISCRETE structural branches.**

EV-mode feasibility **per resolver family**:

| Resolver family | Extractable P/degree distribution? | EV-mode requires |
|---|---|---|
| **Dice continuous engine** (combat, social contest, thread, fieldwork, aggregated mass-battle) | **Yes** — Normal(μN, σ√N); degree probs = Φ at Ob, 2·Ob boundaries with the −0.5 continuity term (`params/core.md:80`) | thin wrapper over existing `p_success` (`sigma_leverage.py:234`) returning P(Failure/Partial/Success/Overwhelming) from the same μ/σ, then E[Δ]=Σ P·echo_amount |
| **Domain-action resolver** (all faction bare-stat: Assert/Suppress/Govern/Treaty/Royal Decree/Excommunication…) | **Yes** — the clamp bands ARE the probabilities (`stats_1_7_scale.md:73-75`) | pure arithmetic: `P_ovw, P_succ−P_ovw, P_partial−P_succ, 1−P_partial` → E[Δ] |
| **Domain Echo map** | Deterministic given degree (`domain_echo.py:27-33`) | table lookup — no work |
| **Faction AI action selection** (`faction_action.py:55`) | Discrete categorical over *which action / which target* | **structurally hard** — see below |
| **Event-deck draw** | Discrete categorical over *which card* | same limitation as AI selection |

**Where EV-mode is structurally impossible/misleading: DISCRETE STRUCTURAL BRANCHES.** Averaging is
sound for a *continuous* stat delta (E[Δstat] is a real intermediate value the game can occupy).
It is **not** sound for a branch that changes *which* resolver fires or *which* target is hit:
EV-averaging "attack Territory A" and "attack Territory B" yields a phantom half-attack on each —
an off-manifold state that never occurs and that mis-propagates downstream. So:
- **Continuous deltas** (stat drift, clock advance, Domain Echo, meaningfulness accumulation) →
  EV-mode is exact and cheap. Use it for Layer A (the analytic horizons).
- **Discrete branches** (faction action choice + target `:159`, deck card, insurgency
  emergence-or-not) → EV collapses the mixture and lies. **Must sample** (Layer B). A middle option
  for small branch factors: enumerate the categorical and carry a *weighted particle set* (mixture)
  rather than a mean — tractable only for the ~4-way action cascade, explosive across k seasons, so
  sampling is the honest default.

**Recommendation:** hybrid. Layer A analytic EV for all continuous motion (gives smooth
threshold-hitting horizons per stake). Layer B seeded ensemble for structural branches, with each
rolled scene *summarized by its EV degree distribution* rather than played (Q4). Per-lever
conditioning (`P(cross | player lever L)`) is injected as a **stat/odds shift on the analytic
layer + a policy change in the `action_callback`**, never as a rolled player scene.

---

## Q4 — COST ENVELOPE

**Live strategic-scale state size (order of magnitude):**

| Component | Count | Vars each | Subtotal |
|---|---|---|---|
| Factions (`mc_v18.py:152` = Crown/Church/Hafenmark/Varfell; charter says 4–6) | 4–6 | ~6 stats + loyalty/autonomy tracks | ~40–60 |
| Settlements (canon **35** — `data_serialization_spec.md:5`) | 35 | Prosperity/Defense/Order + derived + Guild Favour + Π | ~210 |
| Territories (`ALL_PLAYABLE_15`, `game_state.py:23`) | 15 | Accord, PT, Fort, Prosperity | ~60 |
| Shared clocks (MS, CI, IP, Turmoil) + faction tracks | — | — | ~20 |
| Named-NPC roster (`character_canon_v30.md`) | ~20–40 | Disposition, concern, ambition, project | ~100–200 |
| **Total live strategic state** | | | **≈ 400–550 vars → O(500)** |

**Ops per season-step at Accounting cadence (EV-mode, no scenes):** `run_accounting` = CI 5-step +
MS + insurgency scan (over 15 territories) + NPE (pairwise-ish over ~30 NPCs, bounded) + faction
actions (4–6 factions × few candidate evals) + per-settlement deck/Π eval (35). Dominant terms are
the per-settlement and NPC loops. Ballpark **~10³–10⁴ arithmetic ops / season-step**.

**Rollout budget:** N=64 × k=4 = **256 season-steps per Accounting**.
- EV-mode: 256 × ~10⁴ ≈ **2.6×10⁶ ops/Accounting** → sub-10 ms on desktop. Negligible.
- Sampled-mode (real resolver draws, ~5–10× overhead): ~10⁷ ops → **<100 ms**. Fine.
- **64×4 is plausible; 128×4 (~5×10⁶–2×10⁷) is still fine.** Accounting cadence is seasonal, so
  even 100 ms is invisible.

**Where the real cost would be — and why we skip it.** Scene-level resolution (personal
contest/combat kernels: `sim/personal/contest/`, `combat.py`) runs *hundreds of rounds* per scene.
Rolling scenes inside every future would multiply cost by ~10²–10³ and blow the budget. **Forecast
runs strategic cadence only** and models each scene by its EV degree distribution (Q3).

**Fidelity lost by never rolling scenes in forecast (flag):** the forecast cannot see
player-participated scene *outcomes* — it treats "player engages venue X" at its *unconditional*
odds, losing player build/skill, Momentum/Resource spend, tactical choices, and contest-specific
dynamics (Composure/Concentration attrition). This is acceptable for a *strategic pressure-field*
forecast (which is what the horizons are) but means: (i) per-lever conditioning must inject the
lever as an odds/stat shift, not a played scene; (ii) the forecast will systematically
under-represent a skilled player's ability to beat the odds at a specific venue — surface horizons
as *field pressure under average play*, never as a promise.

---

## Q5 — DETERMINISM HAZARDS (design already pre-empts most in s4)

The v1 s4 substrate spec (`spec_sections/s4_substrate.md`) already fought and documented this exact
class of hazard for the detector; the forecast INHERITS those fixes and adds a new float surface.

1. **Iteration order over live arc-vectors / stakes / factions / settlements.**
   `world.factions` is keyed from a **`frozenset` (`game_state.py:23 ALL_PLAYABLE_15`) — frozenset
   iteration order is hash-seeded** → nondeterministic across processes. `faction_action.py:148-159`
   already carries a "[hash-seed fix 2026-05-20] sort before rng.choice" for exactly this. s4
   generalizes it: R7 mandates order-preserving containers, **no `set()`**, sorted-before-emit
   (`s4_substrate.md:140-146`, flagging `convergence_fired_set` as a *second* ORD-2 violation).
   **Mitigation:** iterate every aggregation (marginal accumulation, stake enumeration, per-faction
   drift) in a **fixed sorted key order**; forbid `set()`/frozenset iteration in the marginal path.

2. **Float accumulation in marginals.** Summing per-future probabilities as float is order- and
   platform-sensitive. **s4 already mandates the fix** — integer basis-points with total-order
   tiebreak (`narrative_engine_design_v1.md §4:96-98`; `s4_substrate.md:114-130`: "integer product,
   compare integers"). **Integer basis-points (P as 0–10000) is viable and recommended** for every
   marginal, horizon probability, and convergence co-spike score. This also dodges most of hazard 4.

3. **Key-log-hash seed derivation, stable across save/load.** `propagation_spec_v1` O.8 +
   `00_engine_charter.md:143`: identical seed+choices → identical KEY_LOG hash (V4 replay,
   PP-687 §6). The forecast evaluates at the **Accounting boundary over SETTLED state** (L2's design,
   `narrative_engine_design_v1.md:32`), which sidesteps ORD-3 mid-cascade nondeterminism
   (`s4_substrate.md:73-77`). **Mitigation:** derive rollout seeds as a pure function
   `seed_i = hash(canonical_serialized_key_log, accounting_index, future_index)` — save/load-stable
   iff the Key-log is serialized in canonical order (V4 already requires this). Do **not** seed from
   wall-clock (`mc_v18.py:89-90` falls back to `time.time()` — the forecast must always pass an
   explicit derived seed, never the fallback).

4. **Cross-platform float (Godot vs Python oracle).** The forecast adds a NEW float surface — the
   whole probability field, including Φ. `_phi` uses Python `math.erf` (`sigma_leverage.py:229-231`);
   GDScript has no identical `erf`. s4 already flags "two float comparisons cross the replay
   boundary … the ED-1050 `adef_threshold` class" and routes them to the **key-log parity harness**
   (`s4_substrate.md:114-126`; CLAUDE.md §6 ED-1050). The existing typed-export/parity discipline
   covers the *resolver draws*; it does **not** yet cover a bespoke Φ. **Mitigation:** compute EV-mode
   Φ from a **shared, agreed erf implementation (polynomial or precomputed lookup) identical on both
   platforms**, and carry marginals in integer basis-points (hazard 2) so the only float is the
   per-step Φ, pinned by the parity harness. Sampled-mode must draw through the **Gate-0 RNG service**
   (CLAUDE.md §6 — not yet built) so Godot and the Python oracle share one stream.

**Top 3 hazards + mitigations:**
1. **frozenset/dict iteration order in state aggregation** → sort by stable key everywhere;
   forbid `set()`/frozenset in the marginal path (reuse the `faction_action.py:148` sort discipline;
   satisfy s4 R7).
2. **Cross-platform Φ/erf + Normal-RNG divergence** → shared erf (lookup/poly) + integer
   basis-point marginals + the Gate-0 shared RNG service; pin via the ED-1050 key-log parity harness.
3. **Seed stability across save/load** → derive `hash(canonical_key_log, accounting_index,
   future_index)` at the Accounting boundary over settled state; never fall back to `time.time()`.

---

## Residual blockers (not compute)

- **~19 stubs** gate the sampled layer: `npc_ai` (ambitions #6), `ip_track`, `rs_track`, ~8
  provincial actions, several world/thread/personal modules. Layer A (analytic) works today; Layer B
  is only as complete as the sim.
- **Event deck (#5) has no code** — `governance_play_redesign_v1.md` is a PROPOSAL. Forecasting
  settlement Π-driven branches waits on it.
- **No balance regression oracle** (CLAUDE.md §7): a seeded batch already gives a degenerate
  ~87%/0%/0% win-share that nothing flags. The ensemble's *outputs* have no trusted baseline —
  **add a deterministic seeded smoke assertion before trusting any horizon.** (`sim/tests/` has a
  seeded regression scaffold to extend: `test_mc_v18_regression.py`, `test_sigma_leverage_parity.py`.)
