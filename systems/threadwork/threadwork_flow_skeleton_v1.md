# Threadwork — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/threadwork/` · **Lane:** `WR` · **Contracts:** `threadwork`
**Code roots traced:** `systems/threadwork/sim/{__init__,operations,coherence,collective,opposing,co_movement,rendering,threadcut}.py`, `engine/autoload/game_state.py`, `engine/cross_scale/handoff_rules.py`, `engine/cross_scale/scene_dispatch.py`, `engine/mc_v18.py`, `systems/fieldwork/sim/knots.py`, `systems/overview/sim/{rs_track,ms_track}.py`, `systems/world/sim/miraculous_event.py`, `systems/mass_battle/sim/massbattle.py`, `engine/tests/test_pipeline_reach.py`, `engine/tests/test_thread_mending_ed871.py`
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `attempt_leap(actor, target_state, world, rng)` | `systems/threadwork/sim/operations.py:224 attempt_leap` | `systems/threadwork/sim/collective.py:93 attempt_leap` (internal, lateral) — no cross-subsystem or production caller found |
| `attempt_weaving(actor, target, world, rng)` | `systems/threadwork/sim/operations.py:248 attempt_weaving` | `engine/tests/test_thread_mending_ed871.py:26 attempt_weaving` (test only) |
| `attempt_pulling(actor, target, world, rng)` | `systems/threadwork/sim/operations.py:261 attempt_pulling` | — none found |
| `attempt_past_pulling(actor, target_moment, world, rng)` | `systems/threadwork/sim/operations.py:270 attempt_past_pulling` | — none found |
| `attempt_locking(actor, target, world, rng)` | `systems/threadwork/sim/operations.py:290 attempt_locking` | — none found |
| `attempt_dissolution(actor, target, world, rng)` | `systems/threadwork/sim/operations.py:307 attempt_dissolution` | — none found |
| `attempt_mending(actor, target, world, rng)` | `systems/threadwork/sim/operations.py:316 attempt_mending` | `engine/tests/test_thread_mending_ed871.py:26 attempt_mending` (test only) |
| `attempt_collective_operation(actors, op_type, target, world, rng)` | `systems/threadwork/sim/collective.py:66 attempt_collective_operation` | — none found |
| `resolve_opposing_operations(actor_a, actor_b, op_type, target, world, rng, a_knot_id, b_knot_id)` | `systems/threadwork/sim/opposing.py:103 resolve_opposing_operations` | — none found |
| `opposing_engagement_modifier(opponent_tps)` | `systems/threadwork/sim/opposing.py:79 opposing_engagement_modifier` | — none found |
| `apply_coherence_delta(actor, delta, source, world)` | `systems/threadwork/sim/coherence.py:138 apply_coherence_delta` | `systems/threadwork/sim/operations.py:194 apply_coherence_delta` (internal); `systems/threadwork/sim/collective.py:179 apply_coherence_delta` (internal); `systems/threadwork/sim/opposing.py:228 apply_coherence_delta` (internal); `systems/fieldwork/sim/knots.py:364 apply_coherence_delta` (cross-subsystem, lateral, on Knot rupture — the only cross-subsystem production call site found) |
| `check_coherence_zero_transition(actor, world)` | `systems/threadwork/sim/coherence.py:161 check_coherence_zero_transition` | — none found |
| `get_state(actor, world)` | `systems/threadwork/sim/coherence.py:186 get_state` | — none found |
| `draw_comovement_card(op_type, depth, world, rng)` | `systems/threadwork/sim/co_movement.py:87 draw_comovement_card` | — none found |
| `apply_comovement_effects(card, op_result, world)` | `systems/threadwork/sim/co_movement.py:130 apply_comovement_effects` | — none found |
| `apply_rs_strain(delta, source, world)` | `systems/threadwork/sim/rendering.py:29 apply_rs_strain` | `engine/tests/test_pipeline_reach.py:761 apply_rs_strain` (stub-wired conformance probe only) |
| `check_calamity_threshold(world)` | `systems/threadwork/sim/rendering.py:37 check_calamity_threshold` | — none found |
| `is_threadcut(being_id, world)` | `systems/threadwork/sim/threadcut.py:100 is_threadcut` | `systems/threadwork/sim/threadcut.py:133 is_threadcut` (internal, self) |
| `mark_threadcut(being_id, world)` | `systems/threadwork/sim/threadcut.py:92 mark_threadcut` | — none found |
| `perception_band(observer_ts)` | `systems/threadwork/sim/threadcut.py:105 perception_band` | — none found |
| `resolve_threadcut_interaction(actor, threadcut_target_id, op_type, rendering_threshold, world)` | `systems/threadwork/sim/threadcut.py:114 resolve_threadcut_interaction` | — none found |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `actor` (duck-typed practitioner: `.spirit`, `.ts`, `.history`, `.actor_id`) | `arg` | caller-supplied; no World practitioner-stat schema exists | `systems/threadwork/sim/operations.py:15-19` (module docstring ASSUMPTION) |
| `target` / `target_state` / `target_moment` dict (`scale`, `recency`, ...) | `arg` | caller-supplied | `systems/threadwork/sim/operations.py:224 target_state`, `:248 target` |
| `world.practitioners` (Coherence store) | `world-state` | `engine/autoload/game_state.py` `World` dataclass | `engine/autoload/game_state.py:204 practitioners` |
| `world.threadcut_beings` | `world-state` | `engine/autoload/game_state.py` `World` dataclass | `engine/autoload/game_state.py:222 threadcut_beings` |
| `world.comovement_deck` | `world-state` | `engine/autoload/game_state.py` `World` dataclass | `engine/autoload/game_state.py:223 comovement_deck` |
| `world.clocks['MS']` (Mending Stability) | `world-state` | `engine/autoload/game_state.py:246` `create_world` clock init | `engine/autoload/game_state.py:266 clocks` |
| `world.rng` | `world-state` | fallback rng source when no `rng` arg given | `systems/threadwork/sim/operations.py:172 world.rng` |
| Snapshot dict on load | `file` | `engine/autoload/game_state.py` snapshot restore | `engine/autoload/game_state.py:387 CoherenceState`, `:405 ThreadcutState` |
| TN/Ob/Coherence-cost tables (`TN_STANDARD`, `DEPTH_OB`, `MENDING_OB`, `COHERENCE_COST_BY_SCALE`, ...) | `param` | module-level constants | `systems/threadwork/sim/operations.py:47-117` |
| `CO_MOVEMENT_CARDS` (15-card table) | `param` | module-level constant | `systems/threadwork/sim/co_movement.py:35 CO_MOVEMENT_CARDS` |
| `a_knot_id` / `b_knot_id` | `arg` | caller-supplied, optional | `systems/threadwork/sim/opposing.py:105 a_knot_id` |

## 3. Flow

**S1. [gate] Leap — Personal → Thread scale entry.** `attempt_leap` checks the TS eligibility gate; on failure returns a Failure `OperationResult` with no roll. `systems/threadwork/sim/operations.py:224-245 attempt_leap`

- S1.1 [branch] Below the TS eligibility gate → immediate Failure, no Coherence cost. `systems/threadwork/sim/operations.py:233-239`
- S1.2 [branch] At/above the TS eligibility gate → Ob set by the Leap Ob TS-band gate, routed into the shared resolver `_resolve_operation`. `systems/threadwork/sim/operations.py:241-245`

**S2. [gate] Shared single-actor operation resolution.** `_resolve_operation` computes the actor's pool (`_actor_pool`), rolls via `engine.autoload.dice_engine.roll_pool`, derives a degree, applies a Coherence delta, and (for Weaving/Pulling/Locking/Dissolution) a Mending Stability delta. `systems/threadwork/sim/operations.py:160-221 _resolve_operation`

- S2.1 `_actor_pool` reads `.spirit`, `.ts`, `.history` off the actor. `systems/threadwork/sim/operations.py:145-157 _actor_pool`
- S2.2 [branch] pool > 0 → roll; else net_successes = 0. `systems/threadwork/sim/operations.py:176`
- S2.3 `_compute_degree` maps net successes vs Ob to Failure/Partial/Success/Overwhelming. `systems/threadwork/sim/operations.py:134-142 _compute_degree`
- S2.4 [branch] Partial/Failure on any op except Mending → additional −1 Coherence (ED-871 exemption). `systems/threadwork/sim/operations.py:189-191`
- S2.5 [write] Coherence delta applied via `coherence.apply_coherence_delta` when nonzero. `systems/threadwork/sim/operations.py:193-194`
- S2.6 [branch] Weaving/Pulling degree-driven MS delta; Locking/Dissolution flat −1 MS. `systems/threadwork/sim/operations.py:197-209`

**S3. [emit] Per-operation entry points build on S2** with operation-specific Ob/TN/Coherence-cost lookups: `attempt_weaving`/`attempt_pulling` (Depth Ob, standard TN), `attempt_past_pulling` (recency-banded Ob, TN_POP, extra −1 Coherence), `attempt_locking`/`attempt_dissolution` (Depth Ob, TN_BINDING, FR surcharge), `attempt_mending` (Mending Ob table, 0 Coherence at every degree per ED-871). `systems/threadwork/sim/operations.py:248-334`

**S4. [gate][branch][loop] Collective operation.** `attempt_collective_operation` ranks actors by TS descending (Anchor = highest); all actors Leap independently (S1) in the same round. `systems/threadwork/sim/collective.py:66-96 attempt_collective_operation`

- S4.1 [branch] Anchor's Leap fails → no lattice forms, return early. `systems/threadwork/sim/collective.py:98-105`
- S4.2 [branch] Anchor succeeds → pool sums Anchor's solo pool + successful helpers' `_helper_contribution` (floor(Cognition/2)); lattice fracture (+1 Ob) computed by comparing remaining pool to expected pool. `systems/threadwork/sim/collective.py:107-137`
- S4.3 [loop][write] pooled roll resolved directly (own degree table, not `_resolve_operation`); Coherence applied per successful-Leap participant. `systems/threadwork/sim/collective.py:163-179`

**S5. [gate][branch] Opposing operation.** `resolve_opposing_operations` computes an Ob modifier for each side from the opponent's TPS (`opposing_engagement_modifier`, floor(TPS/2) floored by the `OPPOSING_OB_MODIFIER_MIN` gate), rolls both actors' pools independently, and looks up outcome/consequences in a 3×3 (Meets/Partial/Failure) table. `systems/threadwork/sim/opposing.py:103-224 resolve_opposing_operations`

- S5.1 [write] Coherence deltas applied to both actors per the resolved cell. `systems/threadwork/sim/opposing.py:227-232`
- S5.2 [branch][write] `world.clocks['MS']` present → MS delta routed through `systems.overview.sim.ms_track.apply_ms_delta`. `systems/threadwork/sim/opposing.py:235-239`
- S5.3 [branch][write] `a_knot_id`/`b_knot_id` supplied → strain applied to the Knot(s) via `systems.fieldwork.sim.knots.sustain_knot`, swallowing `ImportError`/`AttributeError`. `systems/threadwork/sim/opposing.py:243-256`

**S6. [gate][emit] Co-Movement card draw**, one per Thread operation: `draw_comovement_card` reshuffles the 15-card deck when exhausted, pops one card, and returns actualized vs unactualized effect profile gated on scale (Object/Personal = unactualized). `systems/threadwork/sim/co_movement.py:87-127 draw_comovement_card`

- S6.1 [write] `apply_comovement_effects` routes the card's MS delta through `ms_track.apply_ms_delta`. `systems/threadwork/sim/co_movement.py:130-152`

**S7. [gate][branch] Threadcut interaction.** `resolve_threadcut_interaction` requires actor-or-target to already be registered threadcut (via `mark_threadcut`); else returns an error dict. `systems/threadwork/sim/threadcut.py:114-140 resolve_threadcut_interaction`

- S7.1 [branch][write] actor is threadcut → +1 Rendering Strain to its registry entry. `systems/threadwork/sim/threadcut.py:153-158`
- S7.2 [gate][branch] Rendering Strain ≥ health OR wounds ≥ rendering_threshold → De-Actualisation round advances, capped by the deactualisation-round-cap gate. `systems/threadwork/sim/threadcut.py:160-187`

**S8. [gate] Rendering Stability world-track — stub-wired, not implemented.** `apply_rs_strain` and `check_calamity_threshold` both return `stubwire.stub_resolve(...)` unconditionally; no Part-5 logic executes. `systems/threadwork/sim/rendering.py:29-42`

**S9. [branch][gap] Cross-scale handoff into/out of Thread scale is a descriptor lookup only.** `engine.cross_scale.handoff_rules.apply_handoff` matches `(SCALE_PERSONAL, SCALE_THREAD)` and `(SCALE_THREAD, SCALE_FACTION)`/`(SCALE_THREAD, SCALE_MASS)` and returns a `HandoffResult` naming a procedure in prose strings; it does not call any `systems.threadwork.sim.*` function. `engine/cross_scale/handoff_rules.py:102-114 apply_handoff`, `:153-183`

**S10. [gate][gap] Production scene dispatch never derives a Thread-scale scene.** `engine.cross_scale.scene_dispatch._resolve_slot` branches on `scene_type` ∈ `{"combat", "contest", "fieldwork", "investigation"}` plus a catch-all `stubwire.stub_resolve` fallback; no `"thread"` branch exists, and `_HANDOFF_SCALE_PAIR_BY_SCENE_TYPE` maps only `"combat"`/`"contest"` → `(Scene, Faction)`. `engine/cross_scale/scene_dispatch.py:157-160 _HANDOFF_SCALE_PAIR_BY_SCENE_TYPE`, `:216-224 _resolve_slot`, `:360-371` catch-all

**S11. [gap] Campaign season driver never imports threadwork.** `engine/mc_v18.py`'s `run_campaign` imports `game_state`, `victory`, `scene_slate`, `stubwire`, `faction_action`, `season`, `scene_dispatch` — no `systems.threadwork` import anywhere in the file. `engine/mc_v18.py:35-39`

**S12. [gap][branch] Mass-battle phase-boundary hook is a declared, empty no-op.** `massbattle.py`'s canonical phase-boundary order names `threadwork` last; `threadwork_check(unit_a, unit_b, phase_idx)` is `pass`-bodied and is called from `phase_boundary` every phase, but performs no threadwork call. `systems/mass_battle/sim/massbattle.py:194`, `:301-303 threadwork_check`, `:314 phase_boundary`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `OperationResult` (degree, net_successes, pool, coherence_delta, mending_stability_delta) | return value | caller (test only in practice) | `systems/threadwork/sim/operations.py:120-131 OperationResult` |
| `CollectiveResult` | return value | caller (no found caller) | `systems/threadwork/sim/collective.py:44-54 CollectiveResult` |
| `OpposingResult` | return value | caller (no found caller) | `systems/threadwork/sim/opposing.py:62-76 OpposingResult` |
| `CoherenceState` (per-practitioner track) | `world-state write` | `world.practitioners`, read back by `engine/autoload/game_state.py` snapshot restore | `systems/threadwork/sim/coherence.py:83-95 CoherenceState`; `engine/autoload/game_state.py:367-369` |
| `CoMovementCard` | return value | caller of `apply_comovement_effects` (no found production caller) | `systems/threadwork/sim/co_movement.py:55-62 CoMovementCard` |
| MS clock delta (`world.clocks['MS']`) | `world-state write` | `systems.overview.sim.ms_track` (shared MS surface) | `systems/threadwork/sim/opposing.py:238-239`; `systems/threadwork/sim/co_movement.py:142-143` |
| Knot strain (`sustain_knot`) | cross-subsystem call | `systems.fieldwork.sim.knots` | `systems/threadwork/sim/opposing.py:245-254` |
| `ThreadcutState` (rendering_strain, deactualisation_round) | `world-state write` | `world.threadcut_beings`, read back by snapshot restore | `systems/threadwork/sim/threadcut.py:71-82 ThreadcutState`; `engine/autoload/game_state.py:407-409` |
| `StubResult` (rendering.py) | return value | `engine/tests/test_pipeline_reach.py` conformance probe only | `systems/threadwork/sim/rendering.py:30-34`; `engine/tests/test_pipeline_reach.py:761` |
| `scene.thread_operation`, `meta.thread_woven` (declared Key types) | `key` | **none — declared in contract, never constructed anywhere in the tree** | `references/module_contracts.yaml:354-355`; see §7 |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `world.practitioners[actor_id]` (`CoherenceState`) | RW | `systems/threadwork/sim/coherence.py` | `systems/threadwork/sim/coherence.py:57-62 _store`, `:130-135 _get_or_create` |
| `_practitioner_state` (module-level fallback) | RW | `systems/threadwork/sim/coherence.py` | `systems/threadwork/sim/coherence.py:54 _practitioner_state` |
| `world.threadcut_beings[being_id]` (`ThreadcutState`) | RW | `systems/threadwork/sim/threadcut.py` | `systems/threadwork/sim/threadcut.py:63-68 _store` |
| `_threadcut_registry` (module-level fallback) | RW | `systems/threadwork/sim/threadcut.py` | `systems/threadwork/sim/threadcut.py:60 _threadcut_registry` |
| `world.comovement_deck['remaining'/'discard']` | RW | `systems/threadwork/sim/co_movement.py` | `systems/threadwork/sim/co_movement.py:69-74 _store` |
| `_deck_state` (module-level fallback) | RW | `systems/threadwork/sim/co_movement.py` | `systems/threadwork/sim/co_movement.py:66 _deck_state` |
| `world.clocks['MS']` | W (via `ms_track.apply_ms_delta`) | `systems.overview.sim.ms_track` (peer module, not owned here) | `systems/threadwork/sim/opposing.py:238-239`; `systems/threadwork/sim/co_movement.py:142-143` |
| Knot strain state | W (via `knots.sustain_knot`) | `systems.fieldwork.sim.knots` (peer module, not owned here) | `systems/threadwork/sim/opposing.py:245-254` |
| `Thread Fatigue` (contract-declared clock) | — (unimplemented) | none — declared in contract only, no owning module | `references/module_contracts.yaml:358`; see §7 |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| down (import) | `engine.autoload.dice_engine` | `roll_pool` for all dice resolution | `systems/threadwork/sim/operations.py:40 roll_pool`; `systems/threadwork/sim/opposing.py:36 roll_pool` |
| out (write) | `systems.overview.sim.ms_track` | `apply_ms_delta` — shared Mending Stability arithmetic surface | `systems/threadwork/sim/opposing.py:238 apply_ms_delta`; `systems/threadwork/sim/co_movement.py:142 apply_ms_delta` |
| out (write) | `systems.fieldwork.sim.knots` | `sustain_knot` — Knot strain on opposing-operation outcome | `systems/threadwork/sim/opposing.py:245 sustain_knot` |
| in (call) | `systems.fieldwork.sim.knots` | `apply_coherence_delta` — the only cross-subsystem caller into threadwork found | `systems/fieldwork/sim/knots.py:363-364 apply_coherence_delta` |
| up (declared, not wired) | `engine.cross_scale.handoff_rules` | `SCALE_PERSONAL↔SCALE_THREAD`, `SCALE_THREAD↔SCALE_FACTION`, `SCALE_THREAD↔SCALE_MASS` procedure descriptors — returns prose steps, calls no threadwork function | `engine/cross_scale/handoff_rules.py:102-114`, `:153-183` |
| up (declared, not wired) | `engine.cross_scale.scene_dispatch` | no `"thread"` `scene_type` branch exists; Thread-scale scenes cannot be produced by the live dispatcher | `engine/cross_scale/scene_dispatch.py:216-224`, `:360-371` |
| lateral (declared, not wired) | `systems.mass_battle.sim.massbattle` | `threadwork_check` phase-boundary hook is a named, called, empty no-op | `systems/mass_battle/sim/massbattle.py:194`, `:301-303`, `:314` |
| lateral (declared, not wired) | `systems.overview.sim.rs_track` | shares the Part-5 Rendering Stability canon source; both `rendering.apply_rs_strain` and `rs_track`'s own entry point are separately stub-wired, no call between them found | `systems/overview/sim/rs_track.py:4-9`, `:29-33` |
| lateral (declared, not wired) | `systems.world.sim.miraculous_event` | docstring names `systems/threadwork/sim/rendering` as a dependency; no import found in the module body | `systems/world/sim/miraculous_event.py:9` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| **No Key type is ever emitted.** The contract declares `scene.thread_operation` and `meta.thread_woven` as this module's emits, but no `.py` file anywhere in the tree constructs either string as part of a Key/emit call — a repo-wide grep for both literals returns zero hits outside the contract file itself. | `references/module_contracts.yaml:354-355`; confirmed absent via repo-wide search of all `.py` files (no results) |
| **No production caller reaches any threadwork sim entry point.** Every `attempt_*`/`resolve_opposing_operations`/`draw_comovement_card`/threadcut function has either zero callers repo-wide, or its only caller is a test (`engine/tests/test_thread_mending_ed871.py`) or a stub-conformance probe (`engine/tests/test_pipeline_reach.py`). The one live cross-subsystem call into threadwork is `knots.py`'s `apply_coherence_delta` on Knot rupture — a write into Coherence, not an invocation of any operation resolver. | §1 table "Called-by" column, all rows; `systems/fieldwork/sim/knots.py:364-365` |
| **The campaign season loop never reaches Thread scale.** `engine/mc_v18.py` (`run_campaign`) imports no `systems.threadwork` module. The vertical dispatcher `engine/cross_scale/scene_dispatch.py` has no `"thread"` `scene_type` branch — only `combat`/`contest`/`fieldwork`/`investigation` are live, everything else falls through to a generic `stubwire.stub_resolve`. `handoff_rules.apply_handoff`'s `(Personal, Thread)` branch (§3.1) returns a procedure-descriptor string only and is invoked only from `tests/valoria/test_handoff_dispatch_validity.py`, never from `scene_dispatch` or `mc_v18`. | `engine/mc_v18.py:35-39`; `engine/cross_scale/scene_dispatch.py:157-160`, `engine/cross_scale/scene_dispatch.py:216-224`, `engine/cross_scale/scene_dispatch.py:360-371`; `engine/cross_scale/handoff_rules.py:102-114` |
| **Rendering (Part 5) is entirely stub-wired.** Both `apply_rs_strain` and `check_calamity_threshold` are unconditional `stubwire.stub_resolve(...)` calls with no Part-5 logic behind them; `systems.overview.sim.rs_track` (the world-track peer sharing the same canon Part 5) is independently stub-wired too, with no call between the two modules found. | `systems/threadwork/sim/rendering.py:29-42`; `systems/overview/sim/rs_track.py:29-33` |
| **Mass Battle's `threadwork_check` phase hook is a named, wired, empty no-op.** It is called every phase boundary by `phase_boundary`, but its body is `pass` — the Thread→Mass handoff described in `handoff_rules.py`'s `RULE_THREAD_TO_MASS` (§3.6) has no execution path from the mass-battle sim side. | `systems/mass_battle/sim/massbattle.py:194`; `:301-303`; `:314` |
| **A known unresolved defect (C-TW-3) sits in the shared resolver, not fixed by the ED-871 exemption.** `_resolve_operation`'s docstring records that the blanket Partial/Failure −1 Coherence penalty also mis-hits Leap against Leap's own "Failure does NOT cost Coherence" contract, and that this is deliberately not fixed here. | `systems/threadwork/sim/operations.py:186-188`; corroborated by `engine/tests/test_thread_mending_ed871.py:14-16` |
| **Practitioner/Threadcut/Co-Movement state is module-level-fallback dual-stored; the schema migration these fallbacks were pending on has already landed, and three module docstrings are stale in saying otherwise.** `engine/autoload/game_state.py`'s `World` dataclass declares `practitioners`, `convictions`, `beliefs`, `knots`/`knot_id_counter`, `threadcut_beings`, and `comovement_deck` under "Schema migration #1/#2 — 2026-05-19", with full `serialize_world`/`restore_world` round-tripping (this skeleton's own §2 IN table cites the same `game_state.py` fields as live World state, so §2 and this row previously contradicted each other). All three stores (`coherence.py`, `threadcut.py`, `co_movement.py`) still route through a `_store(world)` helper with a module-level-dict fallback for the `world is None` case (legacy callers/tests) — that fallback is real and current, but each module's own docstring claims the World field itself is missing, which is no longer true. | World fields: `engine/autoload/game_state.py:184`, `engine/autoload/game_state.py:196-199`, `engine/autoload/game_state.py:202-203`; round-trip: `engine/autoload/game_state.py:294-295` (practitioners serialize), `engine/autoload/game_state.py:366-369` (practitioners restore), `engine/autoload/game_state.py:321-322` (threadcut_beings serialize), `engine/autoload/game_state.py:406-409` (threadcut_beings restore), `engine/autoload/game_state.py:324-327` (comovement_deck serialize), `engine/autoload/game_state.py:410-415` (comovement_deck restore); stale docstrings: `systems/threadwork/sim/coherence.py:13-14`, `systems/threadwork/sim/co_movement.py:11-12`, `systems/threadwork/sim/threadcut.py:15`; `_store(world)` fallback still live: `systems/threadwork/sim/coherence.py:49-62`, `systems/threadwork/sim/threadcut.py:59-68`, `systems/threadwork/sim/co_movement.py:65-74` |
| **`collective.py`'s lattice-fracture arithmetic is self-flagged uncertain in-line.** The module computes `lattice_fractured` once, comments through a re-derivation of the canon condition, then recomputes and overwrites it — both computations and the surrounding commentary are left in the file. | `systems/threadwork/sim/collective.py:117-137` |
| **Thread Fatigue (contract clock) has no implementation.** The contract declares a second writable state field for this module, Thread Fatigue (bucket: clock), alongside Coherence — but no `.py` under `systems/threadwork/` implements, reads, or writes it; a case-insensitive repo grep of `systems/threadwork/` for "fatigue" returns hits only in the two prose docs (`threadwork_v30.md`, `threadwork_v30_index.md`), zero in `sim/`. | `references/module_contracts.yaml:358`; case-insensitive grep of `systems/threadwork/` (zero `.py` hits) |
| **The declared Three-Axis Ob (Depth + Breadth + Distance) is dead outside the Depth axis.** `operations.py`'s module docstring claims the module implements "the Three-Axis Ob lookup (Depth + Breadth + Distance)", and the file defines `BREADTH_OB` and `DISTANCE_OB` tables alongside `DEPTH_TS_MINIMUM` — but no function body anywhere in the tree references any of the three; every operation computes Ob from `DEPTH_OB` alone. | `systems/threadwork/sim/operations.py:7-8` (docstring claim), `:71-78 DEPTH_TS_MINIMUM`, `:81-87 BREADTH_OB`, `:90-95 DISTANCE_OB`; confirmed via repo-wide grep for each symbol — no reference outside its own definition |
| **`attempt_leap`'s own docstring claims a `target_state['ts_minimum']` eligibility read that the body never performs.** The docstring says eligibility is gated on `target_state`'s optional `ts_minimum` field; the body (§3 S1) never reads `target_state` at all — eligibility is computed from `actor.ts` only. The parameter is accepted and unread. | `systems/threadwork/sim/operations.py:227` (docstring claim), `:231-245 attempt_leap` (body — no `target_state` reference) |
