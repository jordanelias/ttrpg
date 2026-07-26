# Structure register — architecture layers (G_code + L2)

Deterministic, working-tree only. **Measures; does not gate** (pytest + import-smoke gate). Provenance: L2 is built on `module_contracts.yaml`, which carries 13 `[ASSUMPTION]` markers and 9 `doc:null` modules — findings on those are bucketed as lower-confidence.

**Code roots scanned:** engine, systems, tools, tests/sim/mass_battle.

**Scorecard:** code-modules=248, import-edges=336, import-cycles=4, code-cut-vertices=21, code-orphans=142; l2-modules=27, wiring-edges=99 raw (43 simple/deduped — the cycle/cut-vertex/locality metrics run on the simple graph), l2-cycles=2, l2-contract↔code-correspondence=UNVERIFIED(6/27 name-map), phantom-producers=0(+0 notional), dangling-emits=4, cross-scale-fraction=0.512.

## L2 Key-closure — relationship to the module-adjudicator (§8 disclosure)

The two closure findings below (phantom-producer, dangling-emit) overlap `valoria-module-adjudicator`’s **A3 consume-closure** and **A4 orphan emission** — and the honest §8 accounting (corrected after the Fable-5 2026-07-14 audit called out an earlier over-claim) is: this is **NOT the same rule, and the two are NOT equivalent.** `contract_adjudicator.adjudicate()` already runs A1–A12 **corpus-wide** in one call (it is not per-module — the earlier version of this note wrongly implied it was), against the Key registry, and — critically — it does **family-wildcard inhabitance** checking for wildcard consumes like `scene.*` (`_wild_registered`/`_pat_overlap`). This layer’s `build_l2()` deliberately does **less**: it `continue`s past every wildcard consume (`ktype == "*"` or a family pattern) rather than resolving it, so it detects only the exact-type phantom/dangling cases. It is therefore a **strict-subset, registry-unaware, corpus-wide MEASURE**, not a re-implementation of A3/A4 and not a second gate. The adjudicator is the authoritative registry-aware gate; where the two disagree the adjudicator wins, and this layer will MISS any closure defect that only a wildcard-family resolution would surface. A row here is a pointer to inspect, not a ruling. (True single-sourcing — importing `adjudicate()` here — is the right end-state; it is tracked, not yet done, because that function returns prose verdicts rather than the structured edge list this graph layer needs.)

## L2 phantom producers — a consume names a source that does NOT emit that Key (canon-grade; the mass_battle `scene_outcome.battle_concluded` class)
(none)

## L2 dangling emits — a non-terminal Key emitted but consumed nowhere (canon-grade)

- `mass_battle` emits `scene_outcome.battle_concluded` — no consumer
- `peninsular_strain` emits `env.crisis` — no consumer
- `personal_combat` emits `scene.combat_felled` — no consumer
- `personal_combat` emits `scene.combat_resolved` — no consumer

## Import cycles (SCC > 1) in sim/ + tools/

- engine.autoload.game_state ↔ systems.world.sim.npe
- systems.mass_battle.sim.massbattle ↔ systems.mass_battle.sim.units
- systems.social_contest.sim.contest ↔ systems.social_contest.sim.contest.appraise ↔ systems.social_contest.sim.contest.armature ↔ systems.social_contest.sim.contest.dictionaries ↔ systems.social_contest.sim.contest.faction ↔ systems.social_contest.sim.contest.modes …
- tests.sim.mass_battle.core.exchange ↔ tests.sim.mass_battle.geometry ↔ tests.sim.mass_battle.hierarchy.units ↔ tests.sim.mass_battle.percell ↔ tests.sim.mass_battle.resolution

## Code cut-vertices — single points of failure (removal disconnects the import graph)

- `engine.autoload.game_state` (in 10, out 9)
- `tools.sim_harness.adapters` (in 1, out 17)
- `tests.sim.mass_battle.engine` (in 5, out 11)
- `tests.sim.mass_battle.hierarchy.units` (in 7, out 8)
- `tests.sim.mass_battle.orchestration` (in 3, out 10)
- `tools.sim_harness.adapters.pr119_governance.pr119_integrated_campaign` (in 3, out 8)
- `systems.factions.sim.faction_action` (in 1, out 9)
- `engine.cross_scale.scene_dispatch` (in 1, out 7)
- `systems.social_contest.sim.parliamentary_vote` (in 4, out 4)
- `tests.sim.mass_battle.workbench.server` (in 0, out 8)
- `engine.cross_scale.echo_transport` (in 3, out 4)
- `tools.sim_harness.harness` (in 0, out 7)
- `systems.settlements.sim.registry` (in 5, out 1)
- `tests.sim.mass_battle.troop_types.registry` (in 4, out 2)
- `systems.settlements.sim.infrastructure` (in 4, out 0)
- `systems.mass_battle.sim.massbattle` (in 2, out 1)
- `systems.mass_battle.sim.units` (in 1, out 2)
- `systems.overview.sim.ms_track` (in 3, out 0)
- `systems.overview.sim.season` (in 1, out 2)
- `tests.sim.mass_battle.equipment` (in 1, out 2)
- … 1 more (see `data/structure_metrics.json`)

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

Nothing in the observatory joins L2's 27 `module_contracts.yaml` modules to G_code's 248 real code modules, so a fictional / unimplemented contract entry would surface as canon-grade wiring unchallenged. This gap is **named, not measured**: the contract→code mapping is NOT name-based (a plain name match finds only 6/27 — the code uses `massbattle` for the `mass_battle` contract, folds `faction_state` into `faction_action.py`, etc.), so any name-heuristic cross-check would cry wolf at ~78% and is deliberately NOT shipped as a finding. Closing this honestly needs the `registers/mechanics_index.yaml` `sim_module:` join (a contract↔mechanic↔file map) — a deferred WS task. Until then: **contract↔code correspondence is UNVERIFIED by this layer.**

## Import orphans — internal module nothing imports (dead-ish; verify before removal)

- `engine`
- `engine.autoload.npc_ai`
- `engine.autoload.registry`
- `engine.cross_scale.articulation`
- `engine.cross_scale.handoff_rules`
- `engine.mc_v18`
- `systems`
- `systems.characters`
- `systems.characters.sim`
- `systems.characters.sim.companion`
- `systems.combat`
- `systems.combat.combat_engine_v1.ability_primitives`
- `systems.combat.combat_engine_v1.capabilities`
- `systems.combat.combat_engine_v1.combat_systems`
- `systems.combat.combat_engine_v1.combatant`
- `systems.combat.combat_engine_v1.config`
- `systems.combat.combat_engine_v1.contact`
- `systems.combat.combat_engine_v1.core`
- `systems.combat.combat_engine_v1.geometry`
- `systems.combat.combat_engine_v1.state_graph`
- … 122 more (see `data/structure_metrics.json`)

## Code import hubs (highest total degree — change-impact)

- `engine.autoload.game_state` (in 10, out 9)
- `systems.social_contest.sim.contest` (in 6, out 13)
- `tools.sim_harness.adapter` (in 17, out 1)
- `tools.sim_harness.adapters` (in 1, out 17)
- `tools.sim_harness.depth` (in 18, out 0)
- `tests.sim.mass_battle.engine` (in 5, out 11)
- `engine.autoload.dice_engine` (in 15, out 0)
- `systems.social_contest.sim.contest._kernel_tests` (in 0, out 15)
- `tests.sim.mass_battle.hierarchy.units` (in 7, out 8)
- `systems.social_contest.sim.contest.wrapper` (in 3, out 10)
- `tests.sim.mass_battle.orchestration` (in 3, out 10)
- `tools.sim_harness.adapters.pr119_governance.goldenfurt_fixture` (in 12, out 1)

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
