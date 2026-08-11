# Appendix — per-module scorecard

All 115 Python files under `systems/`; trivial `__init__.py` shims (<20 LOC) omitted.
`tested` = referenced by any file under `tests/` or `engine/tests/` (dotted path or bare-import name).
`stubwire` = count of governed `stub_resolve()` calls (a designed no-op, not a defect).

| module | LOC | fns | pyflakes | dead fn/const | stubwire | tested | notes |
|---|--:|--:|--:|--:|--:|:--:|---|
| `characters/sim/beliefs.py` | 245 | 9 | 0 | 4/1 | 0 | **N** |  |
| `characters/sim/companion.py` | 33 | 1 | 0 | 0/0 | 1 | Y |  |
| `characters/sim/conviction.py` | 270 | 11 | 0 | 2/1 | 0 | **N** | dup-group |
| `combat/combat_engine_v1/ability_primitives.py` | 159 | 5 | 0 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/capabilities.py` | 171 | 4 | 0 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/combat_systems.py` | 1451 | 80 | 0 | 0/0 | 0 | Y | sys.path, GAP×3 |
| `combat/combat_engine_v1/combatant.py` | 156 | 17 | 3 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/config.py` | 318 | 0 | 0 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/contact.py` | 78 | 4 | 0 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/core.py` | 583 | 15 | 0 | 0/0 | 0 | Y | sys.path, GAP×8 |
| `combat/combat_engine_v1/geometry.py` | 96 | 6 | 0 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/state_graph.py` | 231 | 4 | 1 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/tradition.py` | 19 | 0 | 11 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/traditions.py` | 61 | 1 | 0 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/vocabulary.py` | 107 | 0 | 0 | 0/2 | 0 | Y |  |
| `combat/combat_engine_v1/weapon_physics.py` | 971 | 39 | 0 | 0/1 | 0 | Y | GAP×1 |
| `combat/combat_engine_v1/weapons.py` | 921 | 1 | 0 | 0/0 | 0 | Y |  |
| `combat/combat_engine_v1/workbench/armour_participation.py` | 286 | 10 | 0 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/workbench/balance.py` | 238 | 15 | 2 | 0/0 | 0 | Y | sys.path, dup-group |
| `combat/combat_engine_v1/workbench/build_levers.py` | 229 | 13 | 0 | 0/0 | 0 | Y | sys.path, dup-group |
| `combat/combat_engine_v1/workbench/catalogue.py` | 299 | 11 | 0 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/workbench/commentary.py` | 208 | 6 | 0 | 0/0 | 0 | **N** | sys.path |
| `combat/combat_engine_v1/workbench/narrate.py` | 115 | 5 | 3 | 0/0 | 0 | **N** | sys.path |
| `combat/combat_engine_v1/workbench/presets.py` | 113 | 5 | 0 | 1/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/workbench/probabilities.py` | 131 | 7 | 0 | 1/0 | 0 | **N** | sys.path |
| `combat/combat_engine_v1/workbench/server.py` | 144 | 9 | 3 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/workbench/structure_scan.py` | 265 | 6 | 5 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/workbench/trace.py` | 26 | 1 | 1 | 0/0 | 0 | Y | sys.path |
| `combat/combat_engine_v1/wrapper.py` | 496 | 5 | 1 | 0/0 | 0 | Y | sys.path |
| `combat/sim/combat.py` | 305 | 8 | 0 | 0/0 | 0 | Y | DEPRECATED×2 |
| `factions/sim/absolution.py` | 106 | 2 | 1 | 0/0 | 0 | **N** |  |
| `factions/sim/charter_liberties.py` | 32 | 1 | 1 | 0/0 | 1 | Y |  |
| `factions/sim/council_solmund.py` | 92 | 2 | 0 | 0/0 | 0 | **N** |  |
| `factions/sim/crown_initiative.py` | 316 | 7 | 2 | 0/0 | 0 | **N** |  |
| `factions/sim/excommunication.py` | 214 | 2 | 1 | 0/1 | 0 | **N** |  |
| `factions/sim/faction_action.py` | 550 | 13 | 2 | 0/0 | 0 | Y | GAP×1 |
| `factions/sim/hafenmark_equipment.py` | 35 | 1 | 0 | 0/0 | 1 | Y |  |
| `factions/sim/home_sanctuary.py` | 42 | 2 | 2 | 1/0 | 2 | Y |  |
| `factions/sim/infrastructure_reclamation.py` | 34 | 1 | 1 | 0/0 | 1 | Y |  |
| `factions/sim/mass_seizure.py` | 307 | 7 | 4 | 3/0 | 0 | **N** | dup-group |
| `factions/sim/parliamentary_action.py` | 177 | 2 | 0 | 0/0 | 0 | Y | TODO×2 |
| `factions/sim/parliamentary_transfer.py` | 318 | 4 | 0 | 0/0 | 0 | Y |  |
| `factions/sim/treaty.py` | 164 | 8 | 1 | 3/1 | 1 | Y |  |
| `factions/sim/tribunal.py` | 162 | 3 | 0 | 0/3 | 1 | Y |  |
| `factions/sim/varfell_mandate_action.py` | 46 | 1 | 1 | 0/0 | 1 | Y |  |
| `factions/sim/varfell_territorial_acquisition.py` | 48 | 1 | 1 | 0/0 | 1 | Y |  |
| `fieldwork/sim/fieldwork.py` | 59 | 3 | 1 | 2/0 | 3 | Y |  |
| `fieldwork/sim/investigation.py` | 51 | 3 | 1 | 2/0 | 3 | **N** |  |
| `fieldwork/sim/knots.py` | 385 | 11 | 1 | 2/2 | 0 | Y |  |
| `mass_battle/sim/altonian_reinforcements.py` | 21 | 1 | 1 | 0/0 | 0 | Y |  |
| `mass_battle/sim/massbattle.py` | 1905 | 54 | 17 | 1/3 | 0 | Y | GAP×4 |
| `mass_battle/sim/tactic_cards.py` | 33 | 0 | 0 | 0/0 | 0 | **N** |  |
| `mass_battle/sim/units.py` | 415 | 15 | 2 | 0/0 | 0 | Y |  |
| `overview/sim/accounting.py` | 142 | 2 | 0 | 0/0 | 0 | Y |  |
| `overview/sim/ci_track.py` | 189 | 4 | 1 | 0/0 | 0 | **N** | dup-group |
| `overview/sim/ip_track.py` | 42 | 2 | 2 | 1/0 | 2 | Y |  |
| `overview/sim/ms_track.py` | 91 | 3 | 0 | 0/0 | 0 | **N** |  |
| `overview/sim/rs_track.py` | 33 | 1 | 1 | 0/0 | 1 | Y |  |
| `overview/sim/season.py` | 78 | 1 | 1 | 0/0 | 0 | Y |  |
| `settlements/sim/adjacency.py` | 26 | 0 | 0 | 0/0 | 0 | **N** |  |
| `settlements/sim/infrastructure.py` | 259 | 8 | 1 | 0/10 | 0 | **N** |  |
| `settlements/sim/ledger.py` | 75 | 5 | 0 | 0/0 | 0 | Y |  |
| `settlements/sim/registry.py` | 266 | 15 | 0 | 0/0 | 0 | Y |  |
| `settlements/sim/settlement.py` | 204 | 3 | 0 | 1/0 | 0 | Y |  |
| `settlements/sim/temperaments.py` | 170 | 6 | 1 | 4/0 | 0 | Y |  |
| `social_contest/sim/contest/__init__.py` | 135 | 0 | 1 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/_kernel_tests.py` | 1650 | 31 | 13 | 1/0 | 0 | Y |  |
| `social_contest/sim/contest/agon_harness.py` | 521 | 13 | 5 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/appraise.py` | 177 | 3 | 1 | 0/1 | 0 | **N** |  |
| `social_contest/sim/contest/armature.py` | 451 | 10 | 4 | 0/0 | 0 | Y |  |
| `social_contest/sim/contest/contract.py` | 77 | 6 | 0 | 0/0 | 0 | Y |  |
| `social_contest/sim/contest/dictionaries.py` | 765 | 6 | 1 | 3/0 | 1 | Y |  |
| `social_contest/sim/contest/faction.py` | 154 | 11 | 1 | 1/0 | 0 | Y |  |
| `social_contest/sim/contest/modes.py` | 577 | 35 | 0 | 0/0 | 3 | Y | GAP×1 |
| `social_contest/sim/contest/narrative.py` | 170 | 6 | 0 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/policy.py` | 60 | 12 | 1 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/primitives.py` | 310 | 33 | 0 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/resolver.py` | 450 | 35 | 3 | 0/0 | 0 | Y |  |
| `social_contest/sim/contest/rhetoric.py` | 524 | 8 | 2 | 0/0 | 0 | **N** |  |
| `social_contest/sim/contest/wrapper.py` | 429 | 13 | 8 | 0/0 | 1 | Y |  |
| `social_contest/sim/contest_legacy_stub.py` | 268 | 3 | 0 | 0/0 | 0 | **N** | DEPRECATED×3 |
| `social_contest/sim/parliamentary_stay.py` | 106 | 2 | 1 | 2/0 | 0 | Y |  |
| `social_contest/sim/parliamentary_vote.py` | 219 | 3 | 0 | 0/1 | 0 | Y |  |
| `threadwork/sim/co_movement.py` | 159 | 5 | 2 | 3/0 | 0 | Y |  |
| `threadwork/sim/coherence.py` | 196 | 11 | 0 | 1/0 | 0 | **N** |  |
| `threadwork/sim/collective.py` | 201 | 2 | 7 | 1/0 | 0 | Y |  |
| `threadwork/sim/operations.py` | 334 | 10 | 2 | 4/4 | 0 | Y |  |
| `threadwork/sim/opposing.py` | 258 | 3 | 2 | 1/2 | 0 | Y |  |
| `threadwork/sim/rendering.py` | 42 | 2 | 2 | 1/0 | 2 | Y |  |
| `threadwork/sim/threadcut.py` | 200 | 8 | 0 | 4/1 | 0 | **N** | dup-group |
| `world/sim/insurgency_pipeline.py` | 266 | 9 | 1 | 1/1 | 0 | **N** |  |
| `world/sim/miraculous_event.py` | 33 | 1 | 1 | 0/0 | 1 | Y |  |
| `world/sim/npe.py` | 386 | 9 | 1 | 3/4 | 0 | Y |  |
| `world/sim/restoration_movement.py` | 43 | 2 | 2 | 1/0 | 2 | Y |  |
