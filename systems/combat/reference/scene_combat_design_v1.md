# Scene Combat Envelope — Design (scene-combat WS-7, Phase 2)

**Status:** DESIGN-ONLY (Phase 2, not built). Resolving the build of this layer is **ED-911** — a Jordan call
flagged in workplan v5. This doc specifies the multi-combatant envelope so it can be ratified before code.

## What it is

The canonical engine (`designs/scene/combat_engine_v1/wrapper.py`) resolves **one 1-vs-1 bout**. A "scene" is
usually more than two fighters. The envelope is a thin outer layer that turns N-vs-M participants into a resolved
encounter emitting a single `scene.combat_resolved` Key — **wrapping `engagement()` as a black box, never
forking it**. It is `fight()`-shaped (a second outer loop), not `engagement()`-shaped.

## Architectural stance: wrap, never fork

`engagement(A, B, first, cfg, rng)` is pure: two `Combatant` objects in, the felled one or `None` out; it mutates
persistent wound state on the objects and recovers nothing itself. The envelope is a **second outer loop parallel
to `fight()`** that calls `engagement()` for many pairs. New directory `designs/scene/scene_combat_v1/` keeps the
ratified engine pristine. Proposed files (design-only): `scene.py` (`resolve_scene(roster, cfg, rng)`),
`pairing.py` (pure target-selection policy), `scene_state_graph.py`.

## Scene state graph (reuses the WS-1 integrity machine)

```
SceneInit  -> RoundInit
RoundInit  -> Pairing            (refresh standing/engaged, recompute outnumber pressure)
Pairing    -> BoutResolution     (assign each engaged pair; queue extra bouts for the outnumbered)
BoutResolution -> BoutResolution (next pair this round — each is one engagement() call)
BoutResolution -> Attrition      (all this round's bouts resolved)
Attrition  -> RoundEnd           (remove felled; resolve flee checks; admit reinforcements)
RoundEnd   -> RoundInit          (each side still has >=1 standing fighter)
RoundEnd   -> SceneResolved [terminal]  (one side eliminated/routed/withdrawn, or round cap)
SceneResolved -> emit scene.combat_resolved
```

Crucially, this graph is authored in the **same declarative idiom as `state_graph.py`** (the WS-1 graph-as-data),
so the *same* integrity test (`test_combat_state_graph.py`'s closure/reachability/coverage) and the dynamic
coverage harness validate the scene graph for free. One integrity machine, two graphs.

## What it reuses (unchanged) vs new state

**Reused, untouched:** `engagement()` (one scene bout = one call); `Combatant` + `WoundTracker` + `apply_wound`
+ `felled` (wounds persist across bouts within the scene by construction); `_init_live` (seed per participant at
scene start); the whole subsystem layer; the inter-turn recovery formula and first-mover coin-flip lifted from
`fight()` (do **not** call `fight()` — reuse the formula in `Attrition`).

**New scene-only state (minimal):** `roster` (per-actor `{combatant, side, status ∈ {standing,felled,fled,reserve},
engaged_with}`); `sides` (membership + standing-count, drives outnumber + the terminal check); `round` counter
with a `SCENE_ROUND_CAP` (the scene analog of `max_bouts=12`); `focus_counts` (enemies targeting each actor this
round — the outnumber lever); `pairing` (this round's `(A,B)` assignments + the extra-bout queue).

## Composition

**Pairing (`pairing.py`, pure policy).** Each `RoundInit`, match every standing actor to an enemy: an actor
already `engaged_with` an enemy stays paired (continuity → ongoing Vor/poise matters); an unengaged actor picks a
target (default: the lowest-Health reachable enemy → **focus-fire** emerges). **Outnumbering falls out of the
arithmetic**: if side A has 3 standing and B has 1, B is the target of 3 pairings → B fights **3 bouts this round**
(one per attacker) while each A-fighter fights one; B's wounds/stamina/initiative accumulate across those bouts
against the same persistent `Combatant` — no special case, just more `engagement()` calls. **Sequencing within a
round** is initiative-ordered (reuse the engine's `initiative` Vor state) so an actor felled early is removed
before later-queued bouts fire. A `reserve`/late actor enters as unengaged at `RoundInit` — identical to any other
unengaged actor.

## The one new lever: outnumber pressure (Jordan call — ED-911 (b))

Outnumbering already produces churn via extra-bouts arithmetic. Two candidate knobs:
1. **Extra-bout economy only** (purest no-fork): the outnumbered fighter simply eats N bouts/round; churn comes
   from accumulated state. Zero engine change.
2. **Extra-bout + a documented transient init seed**: when actor B is focus-fired by k attackers, each attacker's
   bout passes `first=attacker` and B starts that bout with a small `initiative` deficit ∝ `focus_counts[B]` — a
   *scene-set initial condition on an existing engine input* (modulates, doesn't unlock), making being swarmed
   visibly worse beyond raw bout-count (historically correct, a churn amplifier).

Either rule lives in a `SCENE_CFG` dict (Class-C, Jordan-vetoable), consistent with how the engine treats every
coefficient — and is **ablation-gated** (WS-8 §6) if it adds any term.

## Entry / exit

- **Felled removal:** `engagement()` returns the felled object → mark `status=felled` at `Attrition`, emit
  `scene.combat_felled` (`actor_id`, `by_actor`), drop from next round's pairing.
- **Fleeing:** a `flee` check at `Attrition` (policy: low-Health/routed-side actors roll to withdraw) → `status=fled`,
  a non-casualty contributing to `outcome=withdrawal`. (The `disengage`/contested-withdrawal contact-axis access
  from WS-5 can feed a contested version.)
- **Reinforcements:** a `reserve` actor's admission round is part of the scene spec; it flips to `standing` at the
  chosen `RoundInit` — a scripted "second wave," a churn-positive turning point.

## Roll-up into the `scene.combat_resolved` Key

Match `key_type_registry_v30.md scene.combat_resolved` verbatim (the registry already anticipated this layer):
`required: scene_id, outcome, participants`; `optional: casualties, wounds_inflicted`. Roll-up:
`outcome ∈ {attacker_win, defender_win, draw, rout, withdrawal}` from the terminal; `participants` = all actor_ids
ever standing; `casualties` = `status=felled` ids (accumulated from per-bout `scene.combat_felled`); `wounds_inflicted`
= `{actor_id: final wt.wounds}` read off each `Combatant` at `SceneResolved` (the engine already tracks it).
Per-bout `scene.combat_strike/_hit/_felled` Keys emit en route — the Godot `combat_engine.gd`
`resolve_round`/`_active_fights` skeleton is already shaped for this multi-participant roll-up.

## Contract closure (`references/module_contracts.yaml`)

Add a `combat.scene` module row to the `personal_combat` entry — the IN→resolver→OUT contract (the
module-adjudicator Key-closure pattern):
`{id: "combat.scene", resolver: state_reader, status: PENDING, in: ["scene.combat_strike","scene.combat_hit",
"scene.combat_felled"], out: ["scene.combat_resolved"]}`. No new Key *types* — the registry's scene-family covers
it; `scene.combat_resolved`'s declared consumers (npc_behavior, faction_layer, articulation) are the combat→world
ripple.

## Churn-positivity (the design axiom)

Every scene decision branches narrative state: target selection → who-killed-whom (`by_actor`) → NPC grudges;
outnumber → emergent swarm lethality ("dragged down by three"); flee/reinforce → turning points (`rout` vs
`withdrawal`) → faction ripples; persistent wounds → scars carried into the next scene. Any scene mechanic that
produces no distinguishable Key/state delta is suspect — the WS-1 coverage harness (extended to the scene graph)
catches an inert scene transition.

## Open decisions (Jordan) — gate the build

- **ED-911 (decision pending):** retain group combat on the old `combat_v30` dice chassis (a), or build this
  scene engine out for groups (b)? This doc assumes (b); confirm before building.
- The outnumber lever (extra-bout-only vs + transient init seed).
- Simultaneity (initiative-ordered sequential [recommended] vs discrete simultaneous rounds).
- `designs/scene/scene_combat_v1/` location (sibling, recommended) vs inside `combat_engine_v1/`.
