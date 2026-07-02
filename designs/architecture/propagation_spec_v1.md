# Cross-Scale Propagation Spec — v1

## Status: PROPOSED (Jordan-vetoable throughout) — filed 2026-07-02, ED-1089

Per the merge-ratifies-by-default convention (ED-1088): merging the PR that carries this
document ratifies it — no separate step required. Ratification covers this document's text
exactly as written, including its own honest scope markers: it PROVES per-tick and
per-cascade termination; it does NOT prove cross-tick convergence; it PROPOSES two cited
amendments to `key_substrate_v30.md` §4.1 step 4/5 (OF-7, OF-B1) as proposals recorded here,
not as edits already applied to that file; several items (D.6 double-count, `decay()`,
cap constants, ORD-3/ORD-4) are explicitly left open within the document itself. Canonizing
this document canonizes those distinctions along with everything else — it does not resolve
them.

**What this is.** Workplan v5 §3 docket item **J-38**: the cross-scale propagation contract the
holonic container doctrine (`holonic_container_doctrine_v1.md`, ED-1083, CANONICAL) named as
"the highest-value unauthored canon" and explicitly declined to author itself. This document
supplies the aggregate-up transform, the distribute-down transform, the ordering/determinism
spine (doubling as `engine_clock`'s missing home doc, ED-1051), and a termination guarantee —
closing conversion register #1 (downward Key delivery, ED-1006) and retiring `engine_clock`'s
`doc: null` / `[ASSUMPTION]` grade.

**Authorship discipline.** Every mechanical claim below is grounded in cited canon or code —
`key_substrate_v30.md`, `scale_transitions_v30.md`, the conversion strategy's IV.2 directional
laws, `module_contracts.yaml`, and the live `sim/` temporal/cross-scale code. Two amendments are
genuinely new and are marked **PROPOSED** rather than restated as already-true (OF-7, OF-B1).
Everything else is discipline over what already exists — no bespoke delivery channel is added
(§12.2 compliance verified), no aggregate is ever written directly (F1/IV.2-law-2 compliance
verified). This draft went through one full adversarial round: three independent critics found
real fatal/major holes in the first pass (a field doing two incompatible jobs, an uncapped
accounting-phase cascade, a live-vs-deferred echo-timing contradiction); a repair pass closed
all of them; two independent re-verification passes confirmed the repair holds. Nothing here is
first-draft.

---

# 1. Ordering & Determinism (engine_clock)

> This section formalizes existing ruled canon and doubles as engine_clock's home doc, retiring its doc:null/[ASSUMPTION] grade. Most of it restates ruled canon or states ordering rules the tick structure already implies (SSI-1..4, ORD-1..4); the tick-scoped scheduler itself (O.2's "tick scheduler" state, `cascade_depth`) is genuinely new engine apparatus — legitimized by §4's OF-B1 amendment, not by this section alone.

## O.1 The clock model: season is the tick

There is no sub-season fixed timestep today. The season is the tick. `run_season` composes exactly three steps in order (season.py:57-72): SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY, the last itself a fixed five-step composition (accounting.py:37-79). engine_clock owns this composition and is the only module that may advance the season counter.

| Named phase | Registry phase id | What it does | Code binding |
|---|---|---|---|
| SEASON_TICK | season_tick | Advance season counter; detect arc boundary; engine_clock emits mechanical.season_change | season_manager.advance_season, called at season.py:64 |
| ACTION | (unregistered — Open Flag O-1) | Faction actions in stable dict-insertion order, then scene_dispatch distributes DOWN and resolves | mc_v18._faction_actions_callback (:62-83), invoked at season.py:65 |
| ACCOUNTING_BOUNDARY | accounting_boundary | CI calc; MS year-end decay (gated); insurgency triggers/promotion; NPC ecology; engine_clock emits mechanical.accounting | accounting.run_accounting, called at season.py:66 |

Arc vs year cadence: SEASONS_PER_ARC and SEASONS_PER_YEAR are both 4, but new_arc fires on season%4==1 (start) while year-end decay fires on season%4==0 (end) — a real one-tick offset, not a bug, named here so it isn't "fixed" into alignment later.

**Both phases emit, both drain the same way.** ACTION-phase and ACCOUNTING_BOUNDARY-phase emissions are BOTH routed through engine_clock's single cascade_depth-capped drain (§4.1/§4.2 below). Accounting is not a raw side-effect call: its own emissions (mechanical.accounting, insurgency triggers/promotion, NPC ecology) re-enter the same guarded drain path. The termination cap is tick-wide, not action-phase-only.

## O.2 engine_clock module contract (retires doc:null/[ASSUMPTION])

```yaml
module: engine_clock
scales: [provincial]
resolver: clock_advance
consumes: []   # root-of-causality module: actuated by the campaign runner's for-loop, never by another system's emission
emits:
  # NOTE: `phase:` is NOT part of module_contracts.yaml schema-2's {type, terminal} emit shape —
  # it is prose-level phase binding for this doc's exposition, not a proposed schema-2 field
  # extension. Do not treat it as ratified schema when porting this block into module_contracts.yaml.
  - {type: mechanical.season_change, terminal: false, phase: SEASON_TICK}
  - {type: mechanical.accounting,    terminal: false, phase: ACCOUNTING_BOUNDARY}
state:
  - {name: "season counter", bucket: clock, writable: true, owner: engine_clock}
  - {name: "tick scheduler",  bucket: clock, writable: true, owner: engine_clock}  # tick-scoped: cascade_depth-bearing emission queue (§4.2/§4.6); NOT a Key field
accounting_phase: [season_tick, accounting_boundary]
```

mechanical.season_change requires a categorical new_season (spring|summer|autumn|winter) label that NO code in sim/ currently computes — Open Flag O-2.

**Scheduler entry point is engine-internal routing, not an inbound Key subscription.** engine_clock's scheduling primitive (`engine_clock.schedule_emission()`, NOT a Key-envelope-mutating `defer()` verb) is an ENGINE-INTERNAL routing mechanism over the SAME §4.1 `emit()` path (key_substrate_v30.md). It is NOT a new cross-scale delivery channel (§12.2 compliance: no bespoke channel is added) and NOT a Key-type subscription. `consumes: []` therefore stays empty and correct: engine_clock does not subscribe to any Key type; the scheduler primitive is an ordering/routing over the existing emit path, and does not contradict engine_clock's "root of causality" framing.

## O.3 Within-tick ordering discipline

ACTION sub-steps: faction-action loop over world.factions.items() (dict insertion order) → scene_dispatch.run_scene_phase (evaluate_triggers → queue_triggered_scenes → dispatch_scenes, drains scene_slate in stable priority order). Note (see §4 Theorem A): run_scene_phase runs AFTER the faction-action loop, still inside the ACTION phase, and is called exactly once per tick.

**Normative rules:**
- ORD-1: dict iteration order is load-bearing and safe only because Python 3.7+/GDScript Dictionary guarantee insertion order.
- ORD-2: no set() may gate emission/mutation order anywhere in the tick (generalizes the game_state.py hash-seed fix).

## O.4 sub_step_index — assignment rule

key_substrate_v30.md §2.1 defines sub_step_index as ordering Keys within a season, tiebreak by emission order. Nothing in sim/ currently assigns it.

- SSI-1: sub_step_index is assigned by KEY_LOG.append (§4.1 step 2), NOT by the emitting system. One monotonic counter per campaign/World, reset to 0 at every SEASON_TICK, scoped to season_index.
- SSI-2: because phases run strictly sequentially within a tick, sub_step_index ranges are phase-ordered for free.
- SSI-3: this makes (season_index, sub_step_index) a total order over the Key log by construction.
- **SSI-4: sub_step_index is an APPEND-ORDER / total-order tiebreak field ONLY (its §2.1 meaning), used for ordering and the §4.7/§6.2 stable-sort tiebreak. It is NOT a cascade-depth meter.** The termination guard's re-entrancy bound uses a SEPARATE `cascade_depth` counter that lives on engine_clock's tick-scoped scheduler (§4 below), is never written onto the immutable logged Key, and is never assigned parent+1 into `sub_step_index`.

## O.5 RNG threading — a contract, not a convention

One seeded random.Random lives on World.rng, seeded once at create_world. Threading beyond that is explicit-parameter-passing with no enforcement, and two fallback paths leak (dice_engine, scene_dispatch both instantiate a fresh unseeded Random() if none passed).

- RNG-1: no resolver reachable from the ACTION phase may default to an unseeded random.Random(); the fallback is a determinism bug to retire.
- RNG-2: exactly one World.rng stream per campaign, threaded by explicit passing only.
- RNG-3: each Key emission should record a monotonic rng_draw_index in payload metadata for per-Key replay isolation — proposed mechanism, not a ruling (Open Flag O-3).

**Collision, not silently disposed (Open Flag RNG-MODEL-COLLISION).** `key_substrate_v30.md` §6.1 already rules a DIFFERENT RNG contract: *"Every random draw is seeded per Key emission, not engine-globally... No engine-wide global RNG state contributes to Key payload."* RNG-1/RNG-2 above formalize the sim's CURRENT practice (one global `World.rng` stream) into a contract without disposing of this conflict; RNG-3's draw-index is one plausible reconciliation (recording stream position approximates a per-emission seed without literally reseeding per Key) but is not shown equivalent to §6.1's per-emission-seed model, and the conversion strategy (V.2) separately proposes a THIRD model — a named-draw injected RNG service. This section does not resolve which of the three governs; it names the collision so it isn't inherited silently. Do not treat RNG-1..3 as settling §6 determinism without disposing of this flag first.

## O.6 compute_observers — a live ORD-2 violation in the substrate's own reference pseudocode

key_substrate_v30.md §4.2 specifies compute_observers returning a Python set(), string-actor-id-keyed — exactly the ORD-2-forbidden pattern.

- ORD-3: compute_observers must return an order-preserving collection, seeded deterministically (source_actor first, then targets[] in array order, then actors_in_scale sorted by actor_id, then semi/private observers, de-duplicated). Flagged for Jordan/an ED ticket since this section cannot itself edit key_substrate_v30.md (Open Flag O-4). **This is load-bearing for the termination guard's determinism:** the order in which re-entrant children are enqueued during a drain (§4.2 below) inherits observer order, so until ORD-3 lands, per-cascade drain order — and therefore whether a marginal emission trips EMISSIONS_PER_TICK_MAX — would be hash-seed-dependent. The termination guarantee's determinism is stated as CONDITIONAL on ORD-3/ORD-4 landing.

## O.7 scene_slate._queue — module-global isolation hazard

scene_slate.py declares _queue at MODULE scope, not on World. Masked today by run_campaign's explicit clear() call for sequential runs; a hazard under future parallel batch execution.

- ORD-4: scene-queue state belongs on World, not module scope. Whether this fix is in J-38's scope or a separate sim/ hygiene ticket is Open Flag O-5. Until it lands, the termination guarantee's determinism holds only under SEQUENTIAL execution (parallel batch runs would share module-global queue state).

## O.8 Save / replay / verification

save = (initial_state, KEY_LOG); replay re-executes on_key_emitted() over KEY_LOG from initial_state → identical state; V4 = same seed+choices → identical KEY_LOG hash. O.1's fixed phase order + O.3's ORD-1/ORD-2 + O.4's SSI-1..4 + O.5's RNG-1..3 + O.6's ORD-3 together are the complete determinism precondition set. (Runtime-only guard state — the scheduler's `cascade_depth` — is not part of the save; re-entrant parentage is recorded in each child Key's `causes[]` so cascade depth is reconstructable on replay — §4.4 below.)

## O.9 Out of scope — cross-reference only

The cascade-termination gap is not resolved by this section; that is §4's job.

**Open flags:** O-1 (ACTION phase has no registered phase id) · O-2 (new_season label has no computing code) · O-3 (per-Key seed recording mechanism undecided) · O-4 (compute_observers bare set() is a live ORD-2 violation, out of this section's authority to fix; termination determinism conditional on it) · O-5 (scene_slate._queue module-global fix scope undecided; termination determinism holds only under sequential execution until it lands) · **RNG-MODEL-COLLISION (O.5 — this section's single-stream contract vs key_substrate_v30.md §6.1's per-emission-seed contract, not yet disposed of).**

---

# 2. Aggregate-Up Transform — Domain Echo → Substrate → Re-Derive

## Scope

This section formalizes the **upward** half of the cross-scale propagation contract named by IV.2 law 2 (`godot_conversion_strategy_v1.md:127`): *"Scene outcomes reach higher scales by writing the substrate the aggregate derives from... never the aggregate itself — the F1 rule."* It binds Domain Echo (`scale_transitions_v30.md` §5) to the faction-stat inversion register #3/R6 (`godot_conversion_strategy_v1.md:200,211`) and closes the concrete wiring seam between `sim/cross_scale/domain_echo.py` (implemented, canonical amount tables) and `sim/cross_scale/scene_dispatch.py` (live dispatch, but "side-effect-free on strategic state by construction" by its own docstring, `scene_dispatch.py:16-27`). It ratifies nothing: every mechanism named below already exists in cited canon or code; this section names the correspondence, gives it one emission shape, and states the invariant precisely. **One exception is flagged, not asserted:** AU-5 proposes a cited extension to §4.1's step-4 semantics (a deferred-apply target) to reconcile live echo emission with §5.5 / this doc's §4 termination section — that extension is marked OF-7 for Jordan, not treated as already-canonical.

## AU-1 — The rule: no aggregate is ever written

IV.2 law 1 (`godot_conversion_strategy_v1.md:126`) establishes downward derivation as read-only — "No system writes a derived value... getters only, no setters." IV.2 law 2 (`:127`) is the upward corollary: the aggregate (`faction_stat[s]`) is never a write target, in either direction. Combined with the faction-stat inversion (register #3/R6, `godot_conversion_strategy_v1.md:200,211` — an **OPEN** register item, carried from the consolidation master, gating only the write-side port, not ratified by this section):

```
faction_stat[s]  =  AGGREGATE_s( settlement/territory stats over holdings )
                 ⊕  Σ_k  national_event_modifier_k     (decaying Key-ledger contributions)
```

`faction_stat[s]` has **no setter**. Every write in this section terminates at one of two leaves: a settlement/territory substrate cell, or an entry in the Key log that the aggregation function reads at derivation time (AU-4). This is the corollary of IV.2 law 1 applied to the write side, not a new rule.

**Consequence for the current implementation.** `domain_echo.compute_domain_echo()` (`sim/cross_scale/domain_echo.py:79-124`) returns a `DomainEchoResult{affected_faction, affected_stat, delta}` — exactly the pre-inversion "Layer 4" scalar-delta shape IV.2 law 2 names as the F1 defect. The amount/cap tables inside it (`ECHO_AMOUNT_BY_DEGREE`, `ECHO_STAT_CAP`, `PP_329_ECHO_PER_SCENE_PER_FACTION` — `domain_echo.py:30-43`, citing `scale_transitions_v30.md` §5.2:179-187) are canonical and reusable as-is; only the *destination* of the computed delta must change — from a direct write to `faction.stat[s]` to one of the two channels in AU-2.

## AU-2 — The two write channels

| Channel | What it writes | Grounding |
|---|---|---|
| (i) Substrate-locus write | The settlement/territory stat cell at the scene's locus (e.g. ΔOrder, ΔL, ΔPS at the settlement where the scene occurred) | `scale_transitions_v30.md` §5.5 "Settlement targeting (AUD-SET-02)" (`:208`) already establishes locus-targeting for Accord Echo; IV.2 law 2 names the general form "Domain Echo → settlement ΔL/ΔPS → re-aggregate" |
| (ii) National-event modifier Key | A decaying contribution appended to the Key log, read by `AGGREGATE_s(...) ⊕ Σ_k` at derivation time (AU-4) | register #3/R6: "treaties/decrees/campaigns/Domain-Echoes routed HERE instead of writing the stat; contributions decay" |

A given echo may use (i), (ii), or both — the grounding fact's "and/or." A governance scene at a named settlement can write that settlement's Order directly (i) and may also register a modifier if the outcome has national-scale symbolic weight (ii); a scene with no resolvable settlement locus can only use (ii). **Which stats have a clean settlement/territory aggregate basis and which are national-ledger-dominant is not established by the citations available to this section** — register #3/R6 flags the qualification without enumerating it in ratified canon (OF-1, below).

**Timing (see AU-5).** For channel (i), the settlement-level `stat_deltas` write is NOT applied live during scene resolution; it is a **deferred-apply target** executed at the ACCOUNTING_BOUNDARY, consistent with `scale_transitions_v30.md` §5.5 (AUD-SET-02: Accord/faction consequences "queued to next Accounting") and §4's A1 (ECHO-DEFERRAL). Channel (ii)'s modifier contribution is likewise read at the next derivation, not applied to any aggregate live.

## AU-3 — Emission shape: one Key per echo

Every fired Domain Echo — from `compute_domain_echo`, `compute_accord_echo`, or `compute_thread_echo` (`domain_echo.py:79/128/178`) — emits **exactly one Key**, run through the single update rule verbatim (`key_substrate_v30.md` §4.1:184-220), so it is logged, cause-linked, and replayable per §6 (`:385-399`). The Key is **appended to KEY_LOG at scene-end** (preserving `causes[]` provenance and replayability); what is deferred is only the *application* of its settlement-level `stat_deltas` (AU-3.2 / AU-5), not the log append.

### AU-3.1 — Why `stat_deltas` must stay empty on the faction target

§4.1 step 4 (`key_substrate_v30.md:196-201`) applies `key.stat_deltas` **generically to every observer**: `observer.apply_state_changes(interpretation, key.stat_deltas)`. The schema does not itself distinguish "this observer is a faction whose stats are a pure derivation" from "this observer is a personal actor whose stats are legitimately direct-written" — that distinction is external to the substrate. **This section therefore states AU-1 as a standing authoring discipline, not a self-enforcing schema property**: any Key naming a faction in `targets[]` MUST carry `stat_deltas: {}` for that target; the magnitude rides only in `payload`, read at derivation time (AU-4) by the registered consumer, and is never applied by the generic per-observer write path.

### AU-3.2 — Deferred-apply target for the settlement-locus write (PROPOSED, OF-7)

The channel-(i) settlement-locus `stat_deltas` must NOT be applied at §4.1 step 4 during the ACTION phase, because §4's A1 and §5.5 both require echo consequences to land at the ACCOUNTING_BOUNDARY. To reconcile "one Key, logged live" with "applied at accounting," this section **proposes** a cited extension to §4.1's step-4 semantics: **a Key MAY declare a deferred-apply target** — a target whose `stat_deltas` are collected at emission but whose `apply_state_changes` is executed for that target only at the ACCOUNTING_BOUNDARY, replayed by engine_clock from the already-logged Key. This is a real amendment to §4.1's step-4 wording (which today applies to every observer immediately), not a restatement, and is flagged **OF-7** for Jordan / an ED ticket. It is grounded in `scale_transitions_v30.md` §5.5 (AUD-SET-02, "queued to next Accounting") and §4's A1; it is proposed, cited, and not smuggled in as already-ratified.

**Why not the cheaper alternative — hold the Key in the substrate's existing "Drafted" lifecycle state (§4.8) and emit it whole at the boundary, avoiding a step-4 amendment entirely?** That alternative was considered and rejected: (1) `key_substrate_v30.md` §2.3 invariant 3 restricts `causes[]` to Keys **already in the log** — a deferred-*emission* echo would be invisible to `causes[]` on any later same-tick scene, breaking same-tick causal chaining (a scene at settlement B, resolved after the echo-triggering scene at A but in the same tick's slate, could not cite the still-unemitted echo as a cause). (2) Observer memory forms at §4.1 step 4, scene-resolution time; a deferred-emission Key means witnesses to the *triggering* scene never form memory of the echo at all — deferred-apply preserves this (the Key is logged and observers resolved live; only the settlement-target's state write is delayed). (3) `emitted_at` records when the event happened, not when accounting settles it; deferred emission would misdate the Key. OF-7's "log live, apply late" is the minimal amendment that preserves all three properties; a bigger deferred-emission change would cost more and fix less.

## AU-4 — Re-derivation: getters only, and the ledger *is* the log

`AGGREGATE_s(...)` reads the settlement/territory substrate directly (an existing read per IV.2 law 1). `Σ_k national_event_modifier_k` is defined as a **query over `KEY_LOG`**, not a separate mutable ledger structure — "decaying **Key-ledger** contributions" (register #3/R6) names the log itself as the ledger. This keeps the ledger append-only and consistent with §4.1 step 2 — no second mutable aggregate is introduced that could itself become an F1-style write target. The only unspecified term is `decay()`; whatever function is chosen must be a pure function of `key.emitted_at` (no RNG, no hidden state) to preserve §6 determinism — that constraint is stated here; the function itself is not (OF-3). **Note (cross-ref §4.3):** cross-tick convergence of the up/down loop is *conditional* on `decay()` being strictly contractive; that is not proven here and is §4's honestly-open guarantee, not something AU-4 delivers.

## AU-5 — Wiring contract: closing the domain_echo.py ↔ scene_dispatch.py seam

`domain_echo.py` fully implements §5's amount tables but is unwired: `_resolve_slot` (`sim/cross_scale/scene_dispatch.py:83-119`) computes a resolver result and then calls `zoom_in_out.zoom_out({}, world)` — an **empty dict**, never populated from the resolver result. This is the "OUTCOME→ECHO MAPPING GAP" the module's own docstring names and explicitly declines to fabricate.

**The wiring contract this section specifies** (interface only): the resolver outcome is interpreted (resolver-specific, NOT authored here — flagged OF-5), `domain_echo.compute_domain_echo` is called, and if it fires, an echo Key is **appended to the log at scene-end** with its `causes[]` chain intact. Its settlement-level `stat_deltas` (channel (i)) are marked as a **deferred-apply target** (AU-3.2) and are applied **only at the ACCOUNTING_BOUNDARY**, per §4's A1 and §5.5 — NOT live at §4.1 step 4 during ACTION. The Key is logged live (replayable, cause-linked) but its consequence lands at the accounting boundary. **Explicitly out of scope**: the CONTEXT-DERIVATION BRIDGE stays a flagged prerequisite.

## AU-6 — Ordering and determinism

Domain Echo computation itself (table lookup by degree, zero RNG draws) introduces no new randomness. Ordering follows the existing dispatch order: `scene_slate` drains in stable priority order, and each echo Key's `sub_step_index` is assigned at emission by `KEY_LOG.append` (append order; §1's O.4 / SSI-1), so multiple echoes within one scene-dispatch phase inherit the stable-sort tiebreak for free. **`sub_step_index` is an append-order tiebreak field only** — it is NOT the cascade-depth meter used by the termination guard; that meter (`cascade_depth`) lives on engine_clock's tick-scoped scheduler, never on the Key (§4.2). The two must not be conflated.

## AU-7 — Boundary: what this section does not claim

The PP-329 caps bound the magnitude of one echo's Key — they do not bound accumulation across seasons, nor whether a down-transform landing on an adjacent scene can re-trigger Sufficient Scope. That cross-tick convergence question belongs to §4 (which proves per-tick/per-cascade termination but explicitly does NOT prove cross-tick convergence), not authored here.

**Open flags:** OF-1 (per-stat locus-basis classification unestablished in ratified canon) · OF-2 (no key_type_registry_v30.md entry exists yet for the Domain Echo Key type) · OF-3 (decay() unspecified; cross-tick convergence conditional on it being strictly contractive — see §4.3) · OF-4 (whether apply_state_changes should be engine-hardened against non-empty stat_deltas on faction-typed observers is undecided) · OF-5 (interpret_resolver_outcome is resolver-specific, not authored here) · OF-6 (whether settlements are addressable as targets[].actor_id the same way factions/territories are is assumed, not confirmed) · **OF-7 (PROPOSED cited amendment — extending §4.1 step-4 semantics for a deferred-apply target; needs Jordan / an ED ticket to ratify)**.

---

# 3. Distribute-Down Transform (§12 discipline, seam closure)

### D.0 What this section does and does not do

Direction is already ruled. J-1 (Jordan, 2026-06-19) settled it, recorded as `scale_transitions_v30.md` §12: top-down Key delivery is canonical, engine-mediated Key delivery is the sole cross-scale channel in every direction (§12.2) — "a bespoke top-down delivery channel is not to be authored." This section records §12.3's authoring discipline as the standing distribute-down transform, sharpens the Law-1-vs-§12 distinction, and closes the §12.4 worklist including the down-half of faction-stat inversion. (Adversarially confirmed COMPLIANT with §12.2: distribute_down is authoring-time discipline over the same `emit()`, no second channel added.)

### D.1 The transform, stated once

**Rule (restates scale_transitions_v30.md §12.3, :323-329).** A strategic/environmental Key reaching a sub-scale actor MUST, at emission, set targets[] (one entry per affected actor, with role/impact_vector/stat_deltas), scale_signature[] (include the sub-scale), and per-target stat_deltas/impact_vector.

```
for sub_actor in consequence.affected_sub_scale_actors:
    key.targets.append({actor_id: sub_actor.id, role: ..., impact_vector: {...}, stat_deltas: {...}})
    key.scale_signature |= {sub_actor.scale}
emit(key)   # §4.1, unchanged
```

**Fan-out is one Key, not N Keys.** A single strategic Key affecting N sub-scale actors carries all N in its `targets[]` array (already how §2.1 Keys support multiple targets) and is emitted **once**. This is a single emission, not N re-entrant emissions: the termination guard's `cascade_depth` counter increments only on RE-ENTRANT emission (a consumer emitting a NEW Key in response to observing this one), NEVER on a single Key's target-array width. Wide legitimate fan-out therefore does not trip the cascade-depth cap (cross-ref §4.2/§4.5).

### D.2 Two downward paths — do not conflate them

| | Law 1 — derivation (READ) | §12 — distribute-down (EVENT) |
|---|---|---|
| What moves | nothing written; computed on read | a Key is emitted, stat_deltas applied to named sub-scale actors' own state |
| Failure mode | a setter on Mandate/Accord/Treasury | sparse targets[] — "delivers blind" |

### D.3 Worked example — env.peninsular_strain_shock

The registry entry exists with consuming_systems [faction_layer, npc_behavior, articulation, settlement_layer], but compute_observers never reads payload — only targets[]/scale_signature. Per D.1, peninsular_strain must populate targets[]/scale_signature/stat_deltas for each affected_territories entry. Where one strain event touches many territories, it is ONE Key with a many-entry `targets[]` array (D.1 fan-out rule), not one Key per territory.

### D.4 The eight down-seams — closure worklist

| # | Emitter → consumer(s) | Band |
|---|---|---|
| 1 | domain_actions → npc_behavior (×3) | provincial → personal |
| 2 | domain_actions → piety_track (×2) | provincial → personal |
| 3 | domain_actions → settlement_economy (×1) | provincial → settlement |
| 4 | faction_politics → npc_behavior (×4) | provincial → personal |
| 5 | peninsular_strain → npc_behavior (×1) | peninsula → personal |
| 6 | peninsular_strain → settlement_economy (×1) | peninsula → settlement |
| 7 | peninsular_strain → settlement_layer (×2) | peninsula → settlement |
| 8 | scenario_authoring → settlement_layer (×1) | authored → settlement |

### D.5 The down-half of faction-stat inversion

The down-half — how national_event_modifier_k reshapes constituent settlements — is D.1 applied to this node: the emitter appends the modifier's contribution to Σ_k AND, in the same emission, populates targets[] with the constituent settlement/territory actor_ids, so npc_behavior/settlement_economy at those settlements observe and react. No second channel: the modifier Key's targets[] carries the down-reach; its Σ_k contribution carries the up-reach.

**One Key, N targets — not N Keys.** A large faction's `national_event_modifier` touching N constituent settlements is emitted as a **single Key** whose `targets[]` array holds all N entries (per D.1). It is NOT N separate child emissions. This matters for termination: a wide down-half on a large map is one emission at one `cascade_depth`, so legitimate wide fan-out does not trip the `cascade_depth` / `EMISSIONS_PER_TICK_MAX` guard that exists to catch genuine re-entrant runaway. `cascade_depth` increments only when a consumer of this Key emits a *new* Key in response — never on the width of this Key's `targets[]`. (Cross-ref §4.2/§4.5.)

### D.6 Open flags for Jordan

- Constituent-settlement selection rule for a modifier's targets[] is undefined.
- **Double-count risk (HIGH PRIORITY — needs a Jordan ruling, do NOT resolve here):** the modifier's down-targeted settlement `stat_deltas` may overlap the very settlement stats that `AGGREGATE_s` reads to derive `faction_stat[s]`. If they overlap, the same scene outcome is counted twice — once as the down-write to the settlement (which then feeds AGGREGATE_s on re-derivation) and once as the up-side Σ_k modifier contribution. **Ruling needed:** are the down-targeted settlement `stat_deltas` **disjoint** from what `AGGREGATE_s` reads, or is the modifier term explicitly defined as the *complement* of the settlement-write (so the two partition, not overlap)? This is an F1-adjacent hazard (IV.2 law 2) and a confirmed driver of non-convergence in adversarial review. Per anti-fabrication discipline it is NOT resolved here. §4's termination guarantee is explicitly CONDITIONAL on this being ruled disjoint (see §4.3): if it is NOT disjoint, the up/down loop double-counts every hop and can sustain a bounded-magnitude oscillation that `decay()` may not damp.
- Decay coupling unspecified.
- Sequencing of the eight D.4 seams unassigned.
- The FACTION-STAT INVERSION formula's primary source document could not be located verbatim in the working tree.

---

# 4. Termination Guarantee (per-tick & per-cascade) — Cross-Tick Convergence NOT Proven

> Status: PROPOSED. Proves why cross-scale propagation TERMINATES within any single tick and within any single cascade under the existing phase structure, and adds the one runtime guard the substrate currently lacks (Level B). **Scope honesty:** this section proves TERMINATION (per-tick, per-cascade finiteness). It does NOT prove cross-tick CONVERGENCE. Cross-tick convergence is CONDITIONAL on `decay()` being strictly contractive (unspecified — OF-3) AND on the D.6 double-count being ruled disjoint (§3, D.6); both are open. See §4.3.

## 4.0 The gap this section closes

The causes[] DAG cycle-check (§4.6 of key_substrate_v30.md) guards only authored provenance. It says nothing about runtime side-effect cascades: C1 (inter-scale macro loop: up-echo → §12.3 down-delivery → adjacent scene → Sufficient Scope → new up-event) and C2 (intra-tick micro re-entrancy: §4.1 step 5/7 triggering a new emission that synchronously re-enters the Single Update Rule). Level A bounds C1 WITHIN a tick (per-tick fixpoint). Level B bounds C2 WITHIN a cascade (per-cascade depth). **Neither bounds C1 ACROSS ticks** — that is the honestly-unproven part (§4.3).

## 4.1 Level A — Inter-scale / macro bound (phase separation)

**A1 — ECHO-DEFERRAL.** Within a tick, up-echoes are COLLECTED. The echo Key is APPENDED to KEY_LOG at scene-end (preserving causes[] provenance and replayability — §2's AU-3/AU-5), but its settlement-level `stat_deltas` are a DEFERRED-APPLY TARGET (AU-3.2): applied exactly once, at the ACCOUNTING_BOUNDARY, not live at §4.1 step 4 during ACTION. This is consistent with `scale_transitions_v30.md` §5.5 (AUD-SET-02: Accord/faction consequences "queued to next Accounting").

**A2 — SLATE-FREEZE.** The scene slate is generated exactly ONCE per tick, by `scene_dispatch.run_scene_phase`. Scene resolution MUST NOT append to the current tick's slate; re-evaluation happens only at the next SEASON_TICK.

```
def run_tick(state, season_index):
    # --- SEASON_TICK ---
    advance_season(state, season_index)               # engine_clock emits mechanical.season_change

    # --- ACTION phase ---
    for key in faction_action_keys(state):            # mc_v18 faction-action loop, dict-insertion order
        drain_emission_queue(state, key)              # capped drain (Level B)
    slate = run_scene_phase(state)                    # generated ONCE, AFTER the faction loop, still in ACTION
                                                      # (= evaluate_triggers -> queue_triggered_scenes -> dispatch_scenes)
    for slot in drain(slate):                         # stable priority order
        outcome = resolve(slot)
        for echo in collect_echoes(outcome):
            append_echo_key(state, echo)              # AU-3: Key APPENDED to log at scene-end (causes[] intact)
                                                      # its settlement stat_deltas = DEFERRED-APPLY target (A1)

    # --- ACCOUNTING_BOUNDARY --- (Level B cap applies HERE TOO, not action-phase-only)
    for key in deferred_echo_apply_keys(state) + accounting_seed_keys(state):
        drain_emission_queue(state, key)              # deferred echo stat_deltas applied here, AND all
                                                      # accounting emissions (mechanical.accounting, insurgency
                                                      # triggers/promotion, NPC ecology) routed through the SAME
                                                      # cascade_depth-capped drain — not a raw run_accounting call
```

**Note (accounting is capped).** An earlier draft called `run_accounting(state)` RAW, outside the drain. That was unbounded: accounting itself emits Keys that re-derive state and re-emit. Here, ALL accounting-phase emissions are seeded into the SAME `drain_emission_queue` as action-phase emissions. **Level B's cap applies tick-wide, both phases.**

**Theorem A (per-tick fixpoint).** No scene resolved in tick N can cause another scene to resolve in tick N. *Proof.* `scene_dispatch.run_scene_phase` (`evaluate_triggers → queue_triggered_scenes → dispatch_scenes`) is called EXACTLY ONCE per tick, and it runs AFTER the mc_v18 faction-action loop, inside the ACTION phase. Because it is called once and the slate it produces is frozen (A2), no scene resolved during `dispatch_scenes` can append to the slate being drained; new triggers evaluate only at the next tick's `run_scene_phase`. Up-echo consequences are deferred to ACCOUNTING (A1), after all scene resolution, so they cannot feed a same-tick scene. Depth within a tick is bounded to exactly 1-down (distribute) + 1-up (echo, deferred). ∎ Note this bounds per-tick DEPTH, not the total COUNT of echoes: intra-slate coupling can produce many echoes in one tick — that fan-out is bounded by EMISSIONS_PER_TICK_MAX (§4.2), not by Theorem A.

## 4.2 Level B — Intra-tick / micro bound (emission re-entrancy)

**The re-entrancy meter is `cascade_depth`, a SEPARATE counter from `sub_step_index`.** `sub_step_index` keeps its §1 O.4/SSI meaning (append-order total-order tiebreak, assigned by KEY_LOG.append, never re-written). `cascade_depth` is engine_clock-scheduler-internal: it lives on the tick-scoped scheduler queue, is NOT a field on the immutable logged Key, and is NOT part of the §2.1 Key shape. Level B bounds `cascade_depth`.

**B1 — NO SYNCHRONOUS RE-ENTRY (PROPOSED AMENDMENT to §4.1 step 5).** A consume() or awareness-watcher that would emit a new Key MUST route it through `engine_clock.schedule_emission()` (enqueue onto the tick-scoped scheduler at `cascade_depth = parent.cascade_depth + 1`), and MUST NOT call the Single Update Rule synchronously. **This is a real tightening of existing canon:** §4.1 step 5 today reads "MUST be O(1) OR async." B1 forbids ALL synchronous re-entry and requires deferral instead. That is a change to §4.1's wording, NOT a restatement — recorded here as a PROPOSED, ledger-tracked amendment for Jordan / an ED ticket (OF-B1), not silently asserted as already-true.

**B1a — Two re-entry paths, kept distinct.** §4.1 sanctions two paths and they must not be conflated:
- **Genuinely-async consumer path:** decoupled from the parent's stack frame AND tick. It MUST land in tick N+1's ACTION phase, gets its OWN fresh `cascade_depth = 0` seed there, and MUST carry the triggering Key in its `causes[]`. It cannot honor `parent.cascade_depth + 1` (different stack, different tick) and does not try to — it re-enters the cap fresh next tick. An async emission may NOT land unstamped in the current tick.
- **O(1)-deferred synchronous-but-queued re-entry:** same tick, enqueued via `schedule_emission()` at `parent.cascade_depth + 1`, drained under the cap below.

Stating both explicitly prevents an async emission from silently evading the depth cap by landing unstamped in the wrong tick.

**B2 — CASCADE-DEPTH CAP.** A hard `CASCADE_DEPTH_MAX` caps re-entrant depth; a hard `EMISSIONS_PER_TICK_MAX` caps total per-tick emission count. Breaching either is fail-closed. **`cascade_depth` increments ONLY on RE-ENTRANT emission** (a consumer emitting a NEW Key in response to observing a drained Key) — NEVER on a single Key's `targets[]` array width. A strategic Key with N targets (§3, D.5) is ONE emission at ONE depth, so legitimate wide fan-out on a large map does NOT trip the cap. Both cap constants are UNBACKED integers with no cited canonical_source — OF-CAP.

```
def drain_emission_queue(state, seed_key):
    sched = state.engine_clock.scheduler          # tick-scoped, engine-owned; holds (key, cascade_depth) pairs
    sched.enqueue(seed_key, cascade_depth=0)
    while not sched.empty():
        key, depth = sched.pop_next()             # deterministic order: enqueue order under ORD-3 (O.6)
        assert depth <= CASCADE_DEPTH_MAX          # fail-closed on re-entrant depth
        assert sched.total_emitted <= EMISSIONS_PER_TICK_MAX
        on_key_emitted(key)                        # §4.1 Single Update Rule, UNCHANGED (same emit path)
        for child in sched.reentrant_children_of(key):   # NEW Keys consumers enqueued via schedule_emission()
            # child is a normal §2.1 Key: its sub_step_index is assigned by KEY_LOG.append (SSI-1),
            # NOT re-written here; its runtime parent is recorded in child.causes[] for replay-checkability.
            sched.enqueue(child, cascade_depth=depth + 1)
```

**No mutation of the logged Key.** The drain does NOT read `key.deferred_emissions` (not a §2.1 field) and does NOT write `child.emitted_at.sub_step_index` post-append. Deferred children are held in engine_clock-owned tick-scoped scheduler state (the `cascade_depth`-bearing queue), never as a mutable field on the Key. The Key stays EXACTLY the §2.1 shape; all scheduling metadata (`cascade_depth`, queue position) lives OUTSIDE the Key, on the scheduler. `sub_step_index` is still assigned once, by KEY_LOG.append (O.4/SSI-1), and never re-written.

**Theorem B (intra-tick / per-cascade termination).** `drain_emission_queue` halts. *Proof.* Every re-entrant child enqueued during a drain has `cascade_depth = parent.cascade_depth + 1`. The `assert depth <= CASCADE_DEPTH_MAX` fails-closed once depth would exceed the cap, and no path enqueues at a depth ≤ an already-drained parent's depth, so `cascade_depth` is strictly increasing along any re-entrancy chain and bounded above by `CASCADE_DEPTH_MAX`. Total emissions are independently bounded by `EMISSIONS_PER_TICK_MAX`. A queue that only accepts finitely-many strictly-increasing-depth items below a fixed bound, with a hard total-count cap, drains in finite steps. ∎ (Determinism of WHICH marginal emission trips the count cap is CONDITIONAL on ORD-3/ORD-4 landing — O.6/O.7 — else enqueue order is hash-seed-dependent.)

## 4.3 Convergence / fixpoint condition — what IS and is NOT proven

- **PROVEN — per-tick fixpoint (Level A):** depth bounded to 1-down + 1-up within a tick (Theorem A).
- **PROVEN — per-cascade termination (Level B):** every drain halts under `CASCADE_DEPTH_MAX` / `EMISSIONS_PER_TICK_MAX` (Theorem B), tick-wide (both ACTION and ACCOUNTING phases).
- **PROVEN — the C1 macro loop's MAGNITUDE is bounded, even though its persistence is not (new — a free strengthening at zero fabrication cost).** Every hop through the loop is individually capped: PP-329 permits at most one Domain Echo per faction per scene, and `ECHO_STAT_CAP` (`domain_echo.py:30-43`, citing `scale_transitions_v30.md` §5.2) bounds each echo's magnitude to ±2 per stat. Combined with finite stat ranges (IV.2's directional laws presuppose bounded state), C1 cannot diverge — it can at most fail to *settle*, oscillating at bounded amplitude, never growing unboundedly. This closes the doctrine's named "scariest runtime risk" (a runaway magnitude cascade) independently of `decay()` or the D.6 ruling; only the weaker, still-open question — does the oscillation eventually settle — remains conditional (next bullet).
- **NOT PROVEN — cross-tick convergence (C1):** the macro loop up-echo → §12.3 down-target → adjacent scene → Sufficient Scope → new up-echo next tick is bounded ONLY by the campaign's outer season for-loop, NOT by any proven decay/convergence. It can persist at bounded, non-decaying amplitude for the entire campaign. Genuine convergence requires `decay()` to be STRICTLY CONTRACTIVE (dominate per-tick replenishment) — and `decay()` is UNSPECIFIED (OF-3). Until `decay()` is specified and shown contractive, the guarantee is TERMINATION-ONLY, not convergence. Do not oversell it.
- **CONDITIONAL on the D.6 disjointness ruling:** cross-tick convergence additionally requires that a modifier's down-targeted settlement `stat_deltas` be DISJOINT from what `AGGREGATE_s` reads (§3, D.6). If they overlap (not yet ruled — HIGH-PRIORITY open flag for Jordan), every up/down hop double-counts the same outcome, sustaining a double-counted oscillation that no bounded `decay()` short of over-damping can settle. **If D.6 is ruled non-disjoint, the convergence story breaks even with a contractive decay().**

**Named behavior — the level-triggered perpetual-scene RISK is bounded by canon; the sim doesn't yet comply with it.** A level-triggered Sufficient Scope condition combined with a persistent/indelible Key COULD drive a scene every tick indefinitely — but for the flagship exemplar this is not an open design question. `scale_transitions_v30.md` §4.3.2 already rules Stability Crisis with **hysteresis (ED-749)**: *"Trigger fires once per Stab ≤ 2 entry. Re-arms only after Stab ≥ 3 maintained for 2 consecutive Accountings"* — edge-triggered with a cooldown, for the **player's** faction only. The sim's current implementation (`sim/cross_scale/scene_dispatch.py:49-61`) does not comply: it re-evaluates FRESH every tick with no hysteresis state (level-triggered, matching neither ED-749's edge/re-arm rule) and iterates **all** factions, not just the player's. **This is a sim canon-compliance bug, not a spec gap** — the ruling already exists; the code needs to catch up (track `stab_crisis_armed` per faction, gate re-fire on the 2-consecutive-Accounting recovery, scope to the player). This document does not fix the sim (out of scope), but the decision-queue item this section previously raised is retired: no Jordan ruling is needed for Stability Crisis. The narrower residual: other level-conditioned §4.3.2 triggers (e.g. Settlement Revolt at Order 0, ED-750) may lack an ED-749-style hysteresis rule of their own — auditing the full §4.3.2 table for hysteresis coverage is a hygiene item, not a propagation-spec decision (OF-HYSTERESIS-AUDIT).

## 4.4 Checkable termination invariants

```
# Runtime (scheduler-observable) guard state — checked DURING the drain, not from the save:
assert scheduler.max_cascade_depth <= CASCADE_DEPTH_MAX
assert scheduler.total_emitted    <= EMISSIONS_PER_TICK_MAX
assert scheduler.substep_queue.empty()   # drained below cap at tick end

# Log-derivable (post-hoc replay) invariants:
for k in TICK_KEYS:
    for c in same_tick_causes(k):
        assert k.emitted_at.sub_step_index > c.emitted_at.sub_step_index   # append-order monotonicity (ORDERING, not depth)
assert no_scene_appended_to_slate_after_generation(N)
assert deferred_echo_stat_deltas_applied_at_accounting_only(N)
```

**Note on checkability.** `cascade_depth` is RUNTIME scheduler state, not a saved Key field, so the depth cap is a runtime guard — it is enforced during the drain, not reconstructed from `save = (initial_state, KEY_LOG)`. To keep the runtime cascade REPLAY-checkable, every re-entrant child records its runtime parent Key in `causes[]`; a replay can then reconstruct the re-entrancy tree and its depth from the log. **Known residual ambiguity (flagged in re-verification, low severity):** `causes[]` now carries both authored provenance (used by the §4.6 cycle-check) and runtime re-entrancy parentage, without a specified way to distinguish the two edge types on replay — depth reconstruction is therefore ambiguous until this is resolved. The `sub_step_index`-monotonicity assert is explicitly an ORDERING check (satisfied by append monotonicity for any Key) and is NOT claimed to detect cascade depth — that separation is the whole point of splitting the two counters.

## 4.5 No scripting-drift escape hatch

`CASCADE_DEPTH_MAX`, `EMISSIONS_PER_TICK_MAX`, and B1 are global and entity-agnostic. Termination MUST NOT be achieved by special-casing any actor/faction/scene/outcome, and the cap MUST NOT be tuned per-entity to make a specific cascade fit. Fan-out width (`targets[]` length) is explicitly NOT a depth signal (B2), so a legitimately wide down-half is not special-cased around the guard — it simply is not re-entrancy.

## 4.6 Home & binding

This machinery is the temporal spine's responsibility: engine_clock owns the tick-scoped scheduler, the `schedule_emission()` primitive, the `cascade_depth` counter, and the caps. **`engine_clock.schedule_emission()` is an ENGINE-INTERNAL routing/ordering primitive over the SAME §4.1 `emit()` path** — it is NOT a new cross-scale delivery channel (§12.2: no bespoke channel is added) and NOT a Key-type subscription. engine_clock's `consumes: []` stays empty and its "root of causality" framing stands: the scheduler primitive does not make engine_clock a consumer of any Key type; it routes emissions that still flow through the ordinary Single Update Rule. engine_clock's ownership of this state assumes ED-1051 lands it there (OF-OWN).

**Open flags:** OF-CAP (CASCADE_DEPTH_MAX / EMISSIONS_PER_TICK_MAX unbacked — no cited canonical_source, assign from calibration before ratifying) · **OF-B1 (§4.1 step-5 tightening is a PROPOSED canon amendment needing a ledger/ED ticket)** · OF-3 (decay() unspecified — cross-tick CONVERGENCE proven only if decay() is strictly contractive; termination-only until then) · OF-D6 (cross-tick convergence CONDITIONAL on the D.6 double-count being ruled disjoint — HIGH PRIORITY, Jordan) · OF-HYSTERESIS-AUDIT (the flagship perpetual-scene risk, Stability Crisis, is already ruled by ED-749 hysteresis — a sim compliance bug, not an open decision; auditing the rest of §4.3.2's triggers for hysteresis coverage is a hygiene item, not a Jordan ruling) · OF-OWN (engine_clock ownership of the scheduler assumes ED-1051) · causes[]-overload ambiguity (§4.4, low severity — runtime-reentrancy vs authored-provenance edges not yet distinguished) · intra-drain determinism CONDITIONAL on ORD-3/ORD-4 (§1 O.6/O.7) landing; sequential-execution-only until ORD-4 · step-7 awareness-watcher synchronous-emit audit still needed · **RNG-MODEL-COLLISION (§1 O.5, new) — the single-stream contract here is not reconciled against key_substrate_v30.md §6.1's per-emission-seed contract; needs disposal before O.5/RNG-3 can be treated as settled.**

---

## 5. Consolidated decision queue (this document contributes to decision_queue.md item 18)

Nothing below is decided by this document. Ranked roughly by how much downstream work each unblocks:

1. **OF-7 / OF-B1 (PROPOSED canon amendments)** — extend §4.1 step-4 to allow a deferred-apply target; tighten §4.1 step-5 to forbid synchronous re-entry. Both cited, both needed for this spec's own mechanism to be soundly ratifiable. Natural first ruling: without these two, the termination guarantee has no legal footing in the substrate as currently worded.
2. **D.6 double-count (HIGH PRIORITY)** — are down-targeted settlement `stat_deltas` disjoint from `AGGREGATE_s`'s basis? Confirmed live driver of non-convergence by adversarial review; blocks the convergence story even once `decay()` is specified.
3. **OF-3 — decay() specification** — needed for any cross-tick convergence claim; must be a pure function of `key.emitted_at`, calibration-grade, not fabricated here.
4. **~~OF-PERPETUAL~~ — RETIRED, not a Jordan decision.** `scale_transitions_v30.md` §4.3.2 already rules Stability Crisis's perpetual-scene risk via ED-749 hysteresis (edge-triggered, 2-Accounting re-arm, player's faction only); `sim/cross_scale/scene_dispatch.py:49-61` doesn't yet comply (level-triggered, no hysteresis state, all factions). This is a sim bug to fix, not a ruling to make. Residual: **OF-HYSTERESIS-AUDIT** — do the *other* level-conditioned §4.3.2 triggers (e.g. Settlement Revolt, ED-750) have an ED-749-equivalent hysteresis rule? A hygiene audit, not this spec's decision.
5. **RNG-MODEL-COLLISION (§1, O.5, new)** — this spec's single-global-stream RNG contract (RNG-1/2/3) is not reconciled against `key_substrate_v30.md` §6.1's per-emission-seed contract, nor against the conversion strategy's named-draw-service proposal. Three RNG models currently coexist unreconciled in the corpus; disposing of this is a precondition for treating §1's determinism claims as settled.
6. **OF-CAP** — CASCADE_DEPTH_MAX / EMISSIONS_PER_TICK_MAX numeric values, from calibration.
7. **ORD-3 / ORD-4 (§1, O.4/O.5/O.6/O.7)** — compute_observers order-preservation and scene_slate._queue's module-global fix. Both are determinism preconditions this spec's own guarantee depends on but cannot itself rule (out of authority to edit key_substrate_v30.md / decide sim/ hygiene scope).
8. **OF-1, OF-2, OF-4, OF-5, OF-6 (§2)** and **the D.4/D.5 residuals (§3)** — smaller, non-blocking authoring/registry decisions.

---

## Relationship to other canonical surfaces

- `designs/architecture/holonic_container_doctrine_v1.md` (ED-1083, CANONICAL) — names this document as the propagation-spec transform it explicitly deferred authoring. This document does not re-litigate the doctrine's cross-map; it fills the one cell the doctrine left open.
- `designs/architecture/key_substrate_v30.md` — remains the canonical substrate spec. This document proposes two cited amendments to it (OF-7, OF-B1) rather than silently diverging; until ratified, treat §4.1 step 4/5 in `key_substrate_v30.md` as authoritative and this document's amendments as pending.
- `designs/architecture/scale_transitions_v30.md` §12 (J-1/ED-1038) — the downward-delivery ruling this document builds on, not reopens.
- `references/module_contracts.yaml` — the `engine_clock` entry (ED-1051, open — awaiting Jordan) carries a gap_notes pointer at this document as the candidate home doc; `doc: null` stays unflipped until Jordan resolves ED-1051.
- `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md` — conversion register #1 (downward Key delivery, ED-1006) and the IV.2 directional laws this document formalizes.
- `CURRENT.md` — indexes this doc under Architecture once ratified.
