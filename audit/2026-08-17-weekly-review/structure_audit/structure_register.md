# Structure register — architecture layers (G_code + L2)

Deterministic, working-tree only. **Measures; does not gate** (pytest + import-smoke gate). Provenance: L2 is built on `module_contracts.yaml`, which carries 13 `[ASSUMPTION]` markers and 9 `doc:null` modules — findings on those are bucketed as lower-confidence.

**Code roots scanned:** engine, systems, tools, tests/sim/mass_battle.

**Scorecard:** code-modules=273, import-edges=419, import-cycles=3, code-cut-vertices=20, code-orphans=63, cli-entries=91, stub-wired=24; l2-modules=27, wiring-edges=103 raw (45 simple/deduped — the cycle/cut-vertex/locality metrics run on the simple graph), l2-cycles=2, l2-contract↔code-correspondence=JOINED(13 joined, 13 none, 0 unresolvable, 1 undeclared / 27), phantom-producers=0(+0 notional), dangling-emits=1, cross-scale-fraction=0.511.

## L2 Key-closure — relationship to the module-adjudicator (§8 disclosure)

The two closure findings below (phantom-producer, dangling-emit) overlap `valoria-module-adjudicator`’s **A3 consume-closure** and **A4 orphan emission** — and the honest §8 accounting (corrected after the Fable-5 2026-07-14 audit called out an earlier over-claim) is: this is **NOT the same rule, and the two are NOT equivalent.** `contract_adjudicator.adjudicate()` already runs A1–A12 **corpus-wide** in one call (it is not per-module — the earlier version of this note wrongly implied it was), against the Key registry, and — critically — it does **family-wildcard inhabitance** checking for wildcard consumes like `scene.*` (`_wild_registered`/`_pat_overlap`). This layer’s `build_l2()` deliberately does **less**: it `continue`s past every wildcard consume (`ktype == "*"` or a family pattern) rather than resolving it, so it detects only the exact-type phantom/dangling cases. It is therefore a **strict-subset, registry-unaware, corpus-wide MEASURE**, not a re-implementation of A3/A4 and not a second gate. The adjudicator is the authoritative registry-aware gate; where the two disagree the adjudicator wins, and this layer will MISS any closure defect that only a wildcard-family resolution would surface. A row here is a pointer to inspect, not a ruling. (True single-sourcing — importing `adjudicate()` here — is the right end-state; it is tracked, not yet done, because that function returns prose verdicts rather than the structured edge list this graph layer needs.)

## L2 phantom producers — a consume names a source that does NOT emit that Key (canon-grade; the mass_battle `scene_outcome.battle_concluded` class)
(none)

## L2 dangling emits — a non-terminal Key emitted but consumed nowhere (canon-grade)

- `peninsular_strain` emits `env.crisis` — no consumer

## Import cycles (SCC > 1) in sim/ + tools/

- systems.mass_battle.sim.massbattle ↔ systems.mass_battle.sim.units
- systems.social_contest.sim.contest ↔ systems.social_contest.sim.contest.appraise ↔ systems.social_contest.sim.contest.armature ↔ systems.social_contest.sim.contest.dictionaries ↔ systems.social_contest.sim.contest.faction ↔ systems.social_contest.sim.contest.modes …
- tests.sim.mass_battle.core.exchange ↔ tests.sim.mass_battle.geometry ↔ tests.sim.mass_battle.hierarchy.units ↔ tests.sim.mass_battle.percell ↔ tests.sim.mass_battle.resolution

## Code cut-vertices — single points of failure (removal disconnects the import graph)

- `engine.autoload.game_state` (in 10, out 11)
- `tools.sim_harness.adapters` (in 1, out 17)
- `engine.cross_scale.scene_dispatch` (in 1, out 14)
- `tests.sim.mass_battle.hierarchy.units` (in 7, out 8)
- `engine.mc_v18` (in 1, out 13)
- `tests.sim.mass_battle.orchestration` (in 3, out 10)
- `engine.cross_scale.echo_transport` (in 3, out 8)
- `tools.sim_harness.adapters.pr119_governance.pr119_integrated_campaign` (in 3, out 8)
- `systems.settlements.sim.registry` (in 8, out 1)
- `systems.social_contest.sim.parliamentary_vote` (in 4, out 4)
- `tests.sim.mass_battle.workbench.server` (in 0, out 8)
- `tools.sim_harness.harness` (in 0, out 7)
- `tests.sim.mass_battle.troop_types.registry` (in 4, out 2)
- `systems.mass_battle.sim.massbattle` (in 2, out 3)
- `engine.substrate.keys` (in 4, out 0)
- `systems.mass_battle.sim.units` (in 1, out 2)
- `systems.overview.sim.ms_track` (in 3, out 0)
- `systems.overview.sim.season` (in 1, out 2)
- `tests.sim.mass_battle.equipment` (in 1, out 2)
- `tools.trace_execution_phases` (in 0, out 2)

## L2 module cut-vertices — wiring fragility points

- `npc_behavior` (in 13, out 4, canon)
- `faction_state` (in 14, out 2, canon)
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

## Contract↔code correspondence — JOIN-VERIFIED (OI-54, ED-IN-0097, was capstone #7's DISCLOSED BLACK-HOLE, ED-IN-0056)

Every one of L2's 27 `module_contracts.yaml` modules now carries an explicit `sim_module:` field, resolved here against G_code's 273 real code modules — a file path checked for an exact relpath match, a directory path checked as a prefix of >=1 scanned file (the `combat`/`social_contest` convention `mechanics_index.yaml` already used), and the literal `none` accepted as a disclosed absence. A plain NAME match — kept below as `l2_contract_without_code()`, unmodified, for its own pinned test — still finds only 6/27 (the code uses `massbattle` for the `mass_battle` contract, folds `faction_state`'s state into `game_state.py`, etc.); the join below is what actually closes the gap that heuristic could only disclose. Result: **13 joined, 13 explicitly none, 0 unresolvable, 1 undeclared** — `unresolvable` is the fictional-contract case this join exists to catch and should read 0 on a clean tree; `undeclared` should always read 0 now that all 27 modules carry the field (a nonzero value here is itself a regression, not a pre-existing gap).

## L2 contract↔code UNRESOLVABLE — sim_module: names neither a real file nor a real directory prefix in G_code (canon-grade: a fictional or stale code-home claim)
(none)

## L2 contract↔code UNDECLARED — no sim_module: field at all (regression watch: should be empty now that all 27 module_contracts.yaml entries carry the field)

- `mass_battle`

## Import orphans — internal module nothing imports (dead-ish; verify before removal)

- `engine.autoload.npc_ai`
- `systems`
- `systems.characters`
- `systems.characters.sim`
- `systems.characters.sim.companion`
- `systems.combat`
- `systems.combat.combat_engine_v1.ability_primitives`
- `systems.combat.combat_engine_v1.combat_systems`
- `systems.combat.combat_engine_v1.combatant`
- `systems.combat.combat_engine_v1.config`
- `systems.combat.combat_engine_v1.contact`
- `systems.combat.combat_engine_v1.core`
- `systems.combat.combat_engine_v1.geometry`
- `systems.combat.combat_engine_v1.tradition`
- `systems.combat.combat_engine_v1.traditions`
- `systems.combat.combat_engine_v1.vocabulary`
- `systems.combat.combat_engine_v1.weapons`
- `systems.combat.combat_engine_v1.workbench.trace`
- `systems.combat.combat_engine_v1.wrapper`
- `systems.combat.sim`
- … 43 more (see `data/structure_metrics.json`)

## CLI entry points — modules with an `if __name__ == '__main__':` guard and zero importers: runnable as scripts, NOT verified as invoked (a module whose only `__main__` is a self-test still lands here) — excluded from Import orphans above (OI-55/ED-IN-0092); cross-check `references/apparatus_registry.md`'s Invoked-by column before trusting any row

- `systems.combat.combat_engine_v1.capabilities`
- `systems.combat.combat_engine_v1.state_graph`
- `systems.combat.combat_engine_v1.weapon_physics`
- `systems.combat.combat_engine_v1.workbench.armour_participation`
- `systems.combat.combat_engine_v1.workbench.balance`
- `systems.combat.combat_engine_v1.workbench.build_levers`
- `systems.combat.combat_engine_v1.workbench.catalogue`
- `systems.combat.combat_engine_v1.workbench.commentary`
- `systems.combat.combat_engine_v1.workbench.narrate`
- `systems.combat.combat_engine_v1.workbench.presets`
- `systems.combat.combat_engine_v1.workbench.probabilities`
- `systems.combat.combat_engine_v1.workbench.server`
- `systems.combat.combat_engine_v1.workbench.structure_scan`
- `systems.social_contest.sim.contest.agon_harness`
- `tests.sim.mass_battle.bat`
- `tests.sim.mass_battle.lanchester_signature`
- `tests.sim.mass_battle.test_persubunit_stress`
- `tests.sim.mass_battle.validators`
- `tests.sim.mass_battle.workbench.server`
- `tests.sim.mass_battle.workbench.trace`
- … 71 more (see `data/structure_metrics.json`)

## Stub-wired — modules that import `engine.substrate.stubwire` (P1 primitive §2.1, ED-IN-0091: an explicitly-flagged not-built call site, never a silent raise or a fabricated value)

- `engine.autoload.npc_ai`
- `engine.cross_scale.articulation`
- `engine.cross_scale.scene_dispatch`
- `engine.mc_v18`
- `systems.characters.sim.companion`
- `systems.factions.sim.charter_liberties`
- `systems.factions.sim.hafenmark_equipment`
- `systems.factions.sim.home_sanctuary`
- `systems.factions.sim.infrastructure_reclamation`
- `systems.factions.sim.treaty`
- `systems.factions.sim.tribunal`
- `systems.factions.sim.varfell_mandate_action`
- `systems.factions.sim.varfell_territorial_acquisition`
- `systems.fieldwork.sim.fieldwork`
- `systems.fieldwork.sim.investigation`
- `systems.overview.sim.ip_track`
- `systems.overview.sim.rs_track`
- `systems.social_contest.sim.contest._kernel_tests`
- `systems.social_contest.sim.contest.dictionaries`
- `systems.social_contest.sim.contest.modes`
- … 4 more (see `data/structure_metrics.json`)

## Code import hubs (highest total degree — change-impact)

- `engine.substrate` (in 24, out 1)
- `engine.substrate.stubwire` (in 24, out 0)
- `engine.autoload.game_state` (in 10, out 11)
- `engine.autoload` (in 19, out 0)
- `systems.social_contest.sim.contest` (in 6, out 13)
- `tools.sim_harness.adapter` (in 17, out 1)
- `tools.sim_harness.adapters` (in 1, out 17)
- `tools.sim_harness.depth` (in 18, out 0)
- `engine.autoload.dice_engine` (in 17, out 0)
- `systems.social_contest.sim.contest._kernel_tests` (in 0, out 16)
- `tests.sim.mass_battle.engine` (in 5, out 11)
- `engine.cross_scale.scene_dispatch` (in 1, out 14)

## L2 wiring hubs (highest total degree)

- `npc_behavior` (in 13, out 4)
- `faction_state` (in 14, out 2)
- `piety_track` (in 7, out 2)
- `personal_combat` (in 2, out 3)
- `domain_actions` (in 0, out 4)
- `peninsular_strain` (in 0, out 4)
- `scene_slate` (in 0, out 4)
- `settlement_layer` (in 2, out 2)
- `social_contest` (in 1, out 3)
- `fieldwork_knots` (in 0, out 3)
- `mass_battle` (in 0, out 3)
- `settlement_economy` (in 3, out 0)

## Cross-scale locality (NS3 — does the wiring cluster by scale?)
22 intra-scale vs 23 cross-scale edges (51% cross). Lower is better-clustered.

> **EXPLORATORY, not authoritative (capstone #8, ED-IN-0056):** this metric keys on each module's `scales:` field, whose vocabulary is NOT yet reconciled (that is WS2 — the four divergent scale vocabularies are an open workstream), so the intra/cross split can shift when the vocabulary lands. Unlike the phantom-producer / dangling-emit findings above, this one does NOT split notional (`doc:null`/`[ASSUMPTION]`) modules into a lower-confidence bucket — a notional module's declared `scales:` is weighted the same as a canon module's. Read it as a directional signal, not a gate.
