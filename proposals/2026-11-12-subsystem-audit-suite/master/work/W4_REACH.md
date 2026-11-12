# W4 · reach: which functions a seeded realm run enters (M4)

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12). Built by a throwaway `ast` or seeded-run probe in the session scratchpad; nothing here is a judgment.

Method A (`runs/HOLISTIC/reach_all.py`): `sys.setprofile` from before the first engine import; `build_realm(0)`, the shipped chooser, one season; content hash `5ab73af282d0779646c38839fbab85d8`, 13,379 Events (equal to `audits/25_GROUNDING_ENGINE.md` L-18, so the run is the world other lanes read). Headless: `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0`, hash `5405522c36b0399247f83fd9f6d29494`.

| area | function defs | called in realm (import+build+1 season, seed 0) | called in headless NPC-088 x2 | called in either | share of def lines never entered |
|---|---|---|---|---|---|
| engine.dice_engine | 30 | 15 | 14 | 15 | 42% |
| engine.reference | 33 | 0 | 0 | 0 | 100% |
| engine.season.<top> | 42 | 35 | 34 | 35 | 8% |
| engine.season.data | 249 | 208 | 90 | 208 | 9% |
| engine.season.decision | 85 | 74 | 66 | 74 | 7% |
| engine.season.harness | 568 | 38 | 5 | 41 | 82% |
| engine.season.loop | 212 | 114 | 56 | 114 | 29% |
| engine.season.manifest | 25 | 23 | 21 | 23 | 3% |
| engine.season.queries | 287 | 174 | 116 | 174 | 31% |
| engine.season.seam | 71 | 32 | 22 | 32 | 43% |
| engine.season.state | 166 | 120 | 95 | 120 | 21% |
| engine.substrate | 10 | 6 | 2 | 6 | 44% |
| modules.combat | 195 | 0 | 0 | 0 | 100% |
| modules.fieldwork | 1 | 1 | 1 | 1 | 0% |
| modules.mass_battle | 339 | 6 | 6 | 6 | 100% |
| modules.settlements | 8 | 4 | 3 | 4 | 24% |
| modules.social_contest | 4 | 4 | 4 | 4 | 0% |
| systems.characters | 11 | 0 | 0 | 0 | 100% |
| systems.combat | 114 | 0 | 0 | 0 | 100% |
| systems.fieldwork | 11 | 0 | 0 | 0 | 100% |
| systems.mass_battle | 119 | 0 | 0 | 0 | 100% |
| systems.overview | 3 | 0 | 0 | 0 | 100% |
| systems.social_contest | 228 | 0 | 0 | 0 | 100% |
| systems.threadwork | 53 | 0 | 0 | 0 | 100% |

## runtime calls entering modules/, engine/dice_engine, engine/substrate, systems/ from another area (realm run)

| caller | callee | calls |
|---|---|---|
| `engine/season/data/rosters.py:<module>` | `engine/dice_engine/__init__.py:<module>` | 1 |
| `engine/season/data/rosters.py:<module>` | `engine/dice_engine/dice_engine.py:<module>` | 1 |
| `engine/season/seam/ladder.py:degree_of` | `engine/dice_engine/dice_engine.py:degree_from_net` | 48 |
| `engine/season/seam/wrappers/sigma.py:<module>` | `engine/dice_engine/sigma_leverage.py:<module>` | 1 |
| `modules/social_contest/roll.py:chance` | `engine/dice_engine/sigma_leverage.py:band_odds` | 4 |
| `modules/social_contest/roll.py:_chance_floor_cap` | `engine/dice_engine/sigma_leverage.py:band_odds` | 1 |
| `engine/season/seam/wrappers/sigma.py:advantage_sigma` | `engine/dice_engine/sigma_leverage.py:levels_to_net_sigma` | 150 |
| `modules/social_contest/roll.py:roll` | `engine/dice_engine/sigma_leverage.py:net_boost` | 48 |
| `engine/season/seam/wrappers/sigma.py:_odds_of_input` | `engine/dice_engine/sigma_leverage.py:record_odds` | 102 |
| `modules/social_contest/roll.py:roll` | `engine/dice_engine/sigma_leverage.py:roll_net` | 48 |
| `engine/season/seam/wrappers/sigma.py:resolve` | `engine/dice_engine/sigma_leverage.py:settle_record` | 48 |
| `engine/season/data/rosters.py:roster` | `engine/substrate/__init__.py:<module>` | 1 |
| `engine/season/data/rosters.py:roster` | `engine/substrate/battle_orders.py:<module>` | 1 |
| `engine/season/data/rosters.py:<module>` | `engine/substrate/combat_kit.py:<module>` | 1 |
| `engine/season/queries/world_q.py:<module>` | `engine/substrate/composition.py:<module>` | 1 |
| `engine/season/seam/wrappers/sigma.py:_composed_obstacle` | `engine/substrate/composition.py:require` | 102 |
| `engine/season/queries/world_q.py:_entry` | `engine/substrate/composition.py:require` | 79 |
| `engine/season/manifest/registrar.py:register_module_entries` | `engine/substrate/composition.py:require` | 16 |
| `engine/season/data/rosters.py:_load_vocation_attribute` | `engine/substrate/descriptors.py:<module>` | 1 |
| `engine/season/decision/options.py:<module>` | `engine/substrate/descriptors.py:attribute_key` | 1 |
| `engine/season/seam/wrappers/combat.py:<module>` | `engine/substrate/descriptors.py:attribute_key` | 1 |
| `engine/season/data/rosters.py:roster` | `engine/substrate/descriptors.py:block` | 2 |
| `engine/season/data/pursuits.py:pursuit` | `engine/substrate/descriptors.py:resolve_pursuit` | 1837 |
| `engine/season/data/rosters.py:roster` | `engine/substrate/names.py:<module>` | 1 |
| `engine/season/data/rosters.py:roster` | `engine/substrate/names.py:of_class` | 1 |
| `modules/combat/fight.py:<module>` | `engine/substrate/pc_engine.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/__init__.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/combat/fight.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/fieldwork/__init__.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/fieldwork/find.py:<module>` | 1 |
| `engine/season/seam/wrappers/fieldwork.py:find` | `modules/fieldwork/find.py:find` | 62 |
| `engine/substrate/composition.py:require` | `modules/mass_battle/__init__.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/mass_battle/armyrecord.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/mass_battle/massbattle.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/mass_battle/troop_types/presets.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/__init__.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/fabric.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/fortification.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/housing.py:<module>` | 1 |
| `engine/season/queries/world_q.py:capacity` | `modules/settlements/housing.py:housing` | 58 |
| `engine/season/queries/world_q.py:population` | `modules/settlements/housing.py:housing` | 21 |
| `engine/substrate/composition.py:require` | `modules/settlements/larder.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/produce.py:<module>` | 1 |
| `engine/season/loop/matter.py:matter` | `modules/settlements/produce.py:produce` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/provision.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/settlements/subsist.py:<module>` | 1 |
| `engine/season/loop/matter.py:matter` | `modules/settlements/subsist.py:subsist` | 1 |
| `engine/substrate/composition.py:require` | `modules/social_contest/__init__.py:<module>` | 1 |
| `engine/substrate/composition.py:require` | `modules/social_contest/roll.py:<module>` | 1 |
| `engine/season/seam/wrappers/sigma.py:_composed_obstacle` | `modules/social_contest/roll.py:obstacle` | 102 |
| `engine/season/seam/wrappers/sigma.py:resolve` | `modules/social_contest/roll.py:roll` | 48 |


Method B (`runs/HOLISTIC/reach_mon.py`): `sys.monitoring` `PY_START`, each code object recorded once; seed 0 for three seasons (hash `52ff67bc45c5b956cd99215f6ba3097f`) and seed 2 for four seasons (hash `b4bae063f33476988db678b5aae62a28`, equal to `audits/25_GROUNDING_ENGINE.md` L-18). Per-season marks, functions of `modules/combat` and `modules/mass_battle` entered so far (module-level class bodies excluded):

```
{'season': 0, 'secs': 7.9, 'log': 13379, 'combat_fns': 0, 'mb_fns': 18}
{'season': 1, 'secs': 24.1, 'log': 37646, 'combat_fns': 0, 'mb_fns': 18}
{'season': 2, 'secs': 54.6, 'log': 74510, 'combat_fns': 0, 'mb_fns': 152}
hash 52ff67bc45c5b956cd99215f6ba3097f code objects 1693
{'season': 0, 'secs': 7.4, 'log': 11208, 'combat_fns': 155, 'mb_fns': 149}
{'season': 1, 'secs': 23.4, 'log': 34430, 'combat_fns': 155, 'mb_fns': 149}
{'season': 2, 'secs': 55.5, 'log': 73470, 'combat_fns': 155, 'mb_fns': 153}
{'season': 3, 'secs': 120.0, 'log': 126691, 'combat_fns': 161, 'mb_fns': 153}
hash b4bae063f33476988db678b5aae62a28 code objects 1976
```

| area | function defs | entered (union of the two runs, import and build included) | not entered | share of function lines never entered |
|---|---|---|---|---|
| engine.dice_engine | 30 | 18 | 12 | 28% |
| engine.reference | 33 | 0 | 33 | 100% |
| engine.season.<top> | 42 | 37 | 5 | 4% |
| engine.season.data | 249 | 208 | 41 | 9% |
| engine.season.decision | 85 | 74 | 11 | 7% |
| engine.season.harness | 568 | 38 | 530 | 83% |
| engine.season.loop | 212 | 151 | 61 | 16% |
| engine.season.manifest | 25 | 23 | 2 | 3% |
| engine.season.queries | 287 | 206 | 81 | 24% |
| engine.season.seam | 71 | 58 | 13 | 10% |
| engine.season.state | 166 | 135 | 31 | 10% |
| engine.substrate | 10 | 7 | 3 | 36% |
| modules.combat | 195 | 158 | 37 | 17% |
| modules.fieldwork | 1 | 1 | 0 | 0% |
| modules.mass_battle | 339 | 141 | 198 | 40% |
| modules.settlements | 8 | 6 | 2 | 14% |
| modules.social_contest | 4 | 4 | 0 | 0% |
| systems.characters | 11 | 0 | 11 | 100% |
| systems.combat | 114 | 0 | 114 | 100% |
| systems.fieldwork | 11 | 0 | 11 | 100% |
| systems.mass_battle | 119 | 0 | 119 | 100% |
| systems.overview | 3 | 0 | 3 | 100% |
| systems.social_contest | 228 | 0 | 228 | 100% |
| systems.threadwork | 53 | 0 | 53 | 100% |

Per file, the resolver modules, the seam and the loop (functions entered / defined; function lines entered / defined):

| file | functions | lines |
|---|---|---|
| `engine/dice_engine/dice_engine.py` | 5/9 | 119/150 |
| `engine/dice_engine/sigma_leverage.py` | 13/21 | 178/265 |
| `engine/season/loop/calendar.py` | 2/2 | 79/79 |
| `engine/season/loop/census.py` | 1/2 | 67/73 |
| `engine/season/loop/deliberate.py` | 7/7 | 490/490 |
| `engine/season/loop/driver.py` | 5/5 | 437/437 |
| `engine/season/loop/effects_army.py` | 0/10 | 0/69 |
| `engine/season/loop/effects_combat.py` | 22/28 | 766/816 |
| `engine/season/loop/effects_economy.py` | 5/10 | 178/356 |
| `engine/season/loop/effects_founding.py` | 1/9 | 52/277 |
| `engine/season/loop/effects_governance.py` | 11/18 | 299/504 |
| `engine/season/loop/effects_information.py` | 30/45 | 769/1177 |
| `engine/season/loop/effects_migration.py` | 5/6 | 186/202 |
| `engine/season/loop/effects_shared.py` | 10/10 | 112/112 |
| `engine/season/loop/encounter.py` | 1/1 | 42/42 |
| `engine/season/loop/matter.py` | 6/7 | 815/830 |
| `engine/season/loop/predicates.py` | 14/16 | 482/531 |
| `engine/season/loop/resolve.py` | 20/22 | 1182/1222 |
| `engine/season/loop/sides.py` | 2/2 | 129/129 |
| `engine/season/loop/witness.py` | 9/12 | 885/967 |
| `engine/season/seam/contest.py` | 5/9 | 215/223 |
| `engine/season/seam/ladder.py` | 5/6 | 149/152 |
| `engine/season/seam/wrappers/_entry.py` | 1/1 | 15/15 |
| `engine/season/seam/wrappers/_estimate.py` | 0/2 | 0/12 |
| `engine/season/seam/wrappers/combat.py` | 10/13 | 225/287 |
| `engine/season/seam/wrappers/fieldwork.py` | 2/2 | 29/29 |
| `engine/season/seam/wrappers/mass_battle.py` | 16/18 | 325/375 |
| `engine/season/seam/wrappers/pool.py` | 6/6 | 59/59 |
| `engine/season/seam/wrappers/sigma.py` | 13/14 | 367/384 |
| `engine/substrate/composition.py` | 1/1 | 27/27 |
| `engine/substrate/descriptors.py` | 4/4 | 42/42 |
| `engine/substrate/names.py` | 1/2 | 4/32 |
| `engine/substrate/pc_engine.py` | 1/1 | 10/10 |
| `engine/substrate/stubwire.py` | 0/2 | 0/19 |
| `modules/combat/ability_primitives.py` | 6/6 | 75/75 |
| `modules/combat/combat_systems.py` | 60/79 | 927/1206 |
| `modules/combat/combatant.py` | 17/19 | 115/123 |
| `modules/combat/contact.py` | 4/4 | 48/48 |
| `modules/combat/core.py` | 16/20 | 362/391 |
| `modules/combat/fight.py` | 5/5 | 90/90 |
| `modules/combat/geometry.py` | 6/6 | 64/64 |
| `modules/combat/traditions.py` | 1/1 | 9/9 |
| `modules/combat/weapon_physics.py` | 32/42 | 432/644 |
| `modules/combat/weapons.py` | 1/1 | 1/1 |
| `modules/combat/wrapper.py` | 10/12 | 528/548 |
| `modules/fieldwork/find.py` | 1/1 | 7/7 |
| `modules/mass_battle/armies.py` | 0/4 | 0/307 |
| `modules/mass_battle/armyrecord.py` | 0/23 | 0/299 |
| `modules/mass_battle/battle_loop.py` | 2/3 | 471/482 |
| `modules/mass_battle/config.py` | 1/1 | 6/6 |
| `modules/mass_battle/core/attrition.py` | 1/1 | 32/32 |
| `modules/mass_battle/core/contact.py` | 7/11 | 417/529 |
| `modules/mass_battle/core/exchange.py` | 4/7 | 150/177 |
| `modules/mass_battle/core/state.py` | 0/5 | 0/211 |
| `modules/mass_battle/equipment/__init__.py` | 0/1 | 0/8 |
| `modules/mass_battle/equipment/_base.py` | 4/18 | 13/65 |
| `modules/mass_battle/equipment/armour.py` | 1/4 | 9/17 |
| `modules/mass_battle/equipment/weapons.py` | 1/5 | 16/24 |
| `modules/mass_battle/geometry.py` | 19/28 | 301/385 |
| `modules/mass_battle/hierarchy/units.py` | 47/100 | 1459/2498 |
| `modules/mass_battle/massbattle.py` | 8/13 | 323/377 |
| `modules/mass_battle/orchestration.py` | 21/48 | 1576/2360 |
| `modules/mass_battle/orderofbattle.py` | 0/6 | 0/128 |
| `modules/mass_battle/percell.py` | 12/14 | 255/274 |
| `modules/mass_battle/perimeter.py` | 0/9 | 0/116 |
| `modules/mass_battle/resolution.py` | 7/16 | 86/165 |
| `modules/mass_battle/rngsource.py` | 2/2 | 14/14 |
| `modules/mass_battle/terrain.py` | 2/6 | 139/176 |
| `modules/mass_battle/troop_types/presets.py` | 0/3 | 0/68 |
| `modules/mass_battle/troop_types/recruitment.py` | 0/3 | 0/35 |
| `modules/mass_battle/troop_types/registry.py` | 2/8 | 12/45 |
| `modules/settlements/fabric.py` | 0/1 | 0/10 |
| `modules/settlements/fortification.py` | 1/1 | 5/5 |
| `modules/settlements/housing.py` | 1/1 | 10/10 |
| `modules/settlements/larder.py` | 1/2 | 32/43 |
| `modules/settlements/produce.py` | 1/1 | 23/23 |
| `modules/settlements/provision.py` | 1/1 | 10/10 |
| `modules/settlements/subsist.py` | 1/1 | 48/48 |
| `modules/social_contest/roll.py` | 4/4 | 100/100 |

Limits: two seeds, at most four seasons, the realm builder only; a function no run entered is **unobserved**, not dead (`valoria-simplify` C5). The harness is an instrument package and is entered only where a run calls into it.
