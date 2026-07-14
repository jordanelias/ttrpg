# Structure register — architecture layers (G_code + L2)

Deterministic, working-tree only. **Measures; does not gate** (pytest + import-smoke gate). Provenance: L2 is built on `module_contracts.yaml`, which carries 13 `[ASSUMPTION]` markers and 9 `doc:null` modules — findings on those are bucketed as lower-confidence.

**Scorecard:** code-modules=173, import-edges=268, import-cycles=3, code-cut-vertices=14, code-orphans=87; l2-modules=27, wiring-edges=99 raw (43 simple/deduped — the cycle/cut-vertex/locality metrics run on the simple graph), l2-cycles=2, l2-contract↔code-correspondence=UNVERIFIED(3/27 name-map), phantom-producers=0(+0 notional), dangling-emits=4, cross-scale-fraction=0.512.

## L2 Key-closure — relationship to the module-adjudicator (§8 disclosure)

The two closure findings below (phantom-producer, dangling-emit) cover the same ground as `valoria-module-adjudicator`’s **A3 consume-closure** and **A4 orphan emission** — NOT a second implementation of them (§8 "every rule lives once"). The adjudicator is the **authoritative per-module gate**: it runs A1–A12 against the Key registry with wildcard-family inhabitance and emits the CLOSED/OPEN verdict. This layer instead computes closure **corpus-wide as a measure** (a producer/consumer index over all 27 contracts at once) to surface the graph-level pattern — a consume whose named source emits nothing, a non-terminal emit with zero consumers anywhere. It **measures; it does not gate** (the observatory never gates — pytest + the adjudicator do). Where the two disagree, the adjudicator’s registry-aware verdict wins; a row here is a pointer to inspect, not a ruling.

## L2 phantom producers — a consume names a source that does NOT emit that Key (canon-grade; the mass_battle `scene_outcome.battle_concluded` class)
(none)

## L2 dangling emits — a non-terminal Key emitted but consumed nowhere (canon-grade)

- `mass_battle` emits `scene_outcome.battle_concluded` — no consumer
- `peninsular_strain` emits `env.crisis` — no consumer
- `personal_combat` emits `scene.combat_felled` — no consumer
- `personal_combat` emits `scene.combat_resolved` — no consumer

## Import cycles (SCC > 1) in sim/ + tools/

- sim.autoload.game_state ↔ sim.world.npe
- sim.personal.contest ↔ sim.personal.contest.appraise ↔ sim.personal.contest.armature ↔ sim.personal.contest.dictionaries ↔ sim.personal.contest.faction ↔ sim.personal.contest.modes …
- sim.provincial.massbattle ↔ sim.provincial.units

## Code cut-vertices — single points of failure (removal disconnects the import graph)

- `sim.autoload.game_state` (in 10, out 9)
- `tools.sim_harness.adapters` (in 1, out 17)
- `tools.sim_harness.adapters.pr119_governance.pr119_integrated_campaign` (in 3, out 8)
- `sim.provincial.faction_action` (in 1, out 9)
- `sim.cross_scale.scene_dispatch` (in 1, out 7)
- `sim.personal.parliamentary_vote` (in 4, out 4)
- `sim.cross_scale.echo_transport` (in 3, out 4)
- `tools.sim_harness.harness` (in 0, out 7)
- `sim.territory.registry` (in 5, out 1)
- `sim.provincial.excommunication` (in 1, out 4)
- `sim.territory.infrastructure` (in 4, out 0)
- `sim.peninsular.ms_track` (in 3, out 0)
- `sim.peninsular.season` (in 1, out 2)
- `sim.substrate` (in 1, out 1)

## L2 module cut-vertices — wiring fragility points

- `npc_behavior` (in 12, out 4, canon)
- `faction_state` (in 13, out 2, canon)
- `scene_slate` (in 0, out 4, notional)
- `game_director` (in 0, out 2, notional)

## doc:null modules — registered contract, no home design doc (unimplementable spec)

- `audit`
- `domain_actions`
- `engine_clock`
- `game_director`
- `npc_memory`
- `scenario_authoring`
- `scene_slate`
- `scene_timer`
- `settlement_economy`

## Contract↔code correspondence — a DISCLOSED BLACK-HOLE (capstone #7, ED-IN-0056)

Nothing in the observatory joins L2's 27 `module_contracts.yaml` modules to G_code's 173 real code modules, so a fictional / unimplemented contract entry would surface as canon-grade wiring unchallenged. This gap is **named, not measured**: the contract→code mapping is NOT name-based (a plain name match finds only 3/27 — the code uses `massbattle` for the `mass_battle` contract, folds `faction_state` into `faction_action.py`, etc.), so any name-heuristic cross-check would cry wolf at ~89% and is deliberately NOT shipped as a finding. Closing this honestly needs the `canon/mechanics_index.yaml` `sim_module:` join (a contract↔mechanic↔file map) — a deferred WS task. Until then: **contract↔code correspondence is UNVERIFIED by this layer.**

## Import orphans — internal module nothing imports (dead-ish; verify before removal)

- `sim`
- `sim.autoload.npc_ai`
- `sim.autoload.registry`
- `sim.cross_scale.articulation`
- `sim.cross_scale.handoff_rules`
- `sim.mc_v18`
- `sim.peninsular`
- `sim.peninsular.ip_track`
- `sim.peninsular.rs_track`
- `sim.personal.companion`
- `sim.personal.contest.agon_harness`
- `sim.personal.fieldwork`
- `sim.personal.investigation`
- `sim.personal.parliamentary_stay`
- `sim.provincial.altonian_reinforcements`
- `sim.provincial.charter_liberties`
- `sim.provincial.hafenmark_equipment`
- `sim.provincial.home_sanctuary`
- `sim.provincial.infrastructure_reclamation`
- `sim.provincial.mass_seizure`

## Code import hubs (highest total degree — change-impact)

- `sim.autoload.game_state` (in 10, out 9)
- `sim.personal.contest` (in 6, out 13)
- `tools.sim_harness.adapter` (in 17, out 1)
- `tools.sim_harness.adapters` (in 1, out 17)
- `tools.sim_harness.depth` (in 18, out 0)
- `sim.autoload.dice_engine` (in 15, out 0)
- `sim.personal.contest._kernel_tests` (in 0, out 15)
- `sim.personal.contest.wrapper` (in 3, out 10)
- `tools.sim_harness.adapters.pr119_governance.goldenfurt_fixture` (in 12, out 1)
- `sim.personal.contest.primitives` (in 10, out 2)
- `sim.personal.contest.resolver` (in 7, out 5)
- `sim.personal.contest.contract` (in 11, out 0)

## L2 wiring hubs (highest total degree)

- `npc_behavior` (in 12, out 4)
- `faction_state` (in 13, out 2)
- `piety_track` (in 7, out 2)
- `domain_actions` (in 0, out 4)
- `peninsular_strain` (in 0, out 4)
- `scene_slate` (in 0, out 4)
- `settlement_layer` (in 2, out 2)
- `social_contest` (in 1, out 3)
- `fieldwork_knots` (in 0, out 3)
- `mass_battle` (in 0, out 3)
- `personal_combat` (in 2, out 1)
- `settlement_economy` (in 3, out 0)

## Cross-scale locality (NS3 — does the wiring cluster by scale?)
21 intra-scale vs 22 cross-scale edges (51% cross). Lower is better-clustered.

> **EXPLORATORY, not authoritative (capstone #8, ED-IN-0056):** this metric keys on each module's `scales:` field, whose vocabulary is NOT yet reconciled (that is WS2 — the four divergent scale vocabularies are an open workstream), so the intra/cross split can shift when the vocabulary lands. Unlike the phantom-producer / dangling-emit findings above, this one does NOT split notional (`doc:null`/`[ASSUMPTION]`) modules into a lower-confidence bucket — a notional module's declared `scales:` is weighted the same as a canon module's. Read it as a directional signal, not a gate.
