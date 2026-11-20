# W3 · seams by string: composition roles, their call sites, and what a run calls (M3)

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12).

## The 16 composition rows (`engine/engine_params/composition.json`, cooked from `references/module_contracts.yaml` `composition_roles:` by `tools/export_composition.py`)

| role | target | entry | verb | calls in the one-season realm run (seed 0) | entered in either longer run (seed 0 x3, seed 2 x4) |
|---|---|---|---|---|---|
| `combat.fight` | `modules.combat.fight:fight` | verb_call | fight | 0 | yes |
| `fieldwork.find` | `modules.fieldwork.find:find` | step_call | None | 62 | yes |
| `mass_battle.army` | `modules.mass_battle.armyrecord:apply` | query | None | 0 | no |
| `mass_battle.army_options` | `modules.mass_battle.armyrecord:options` | query | None | 0 | no |
| `mass_battle.army_order` | `modules.mass_battle.armyrecord:fielded` | query | None | 0 | no |
| `mass_battle.army_preset` | `modules.mass_battle.troop_types.presets:plan` | query | None | 0 | no |
| `mass_battle.resolve_field` | `modules.mass_battle.massbattle:resolve_field` | verb_call | march | 0 | yes |
| `settlements.drawn_under` | `modules.settlements.larder:drawn_under` | query | None | 0 | no |
| `settlements.fabric` | `modules.settlements.fabric:fabric` | query | None | 0 | no |
| `settlements.fortification` | `modules.settlements.fortification:fortification` | query | None | 0 | yes |
| `settlements.housing` | `modules.settlements.housing:housing` | query | None | 79 | yes |
| `settlements.larder_draw` | `modules.settlements.larder:larder_draw` | query | None | 1 | yes |
| `settlements.produce` | `modules.settlements.produce:produce` | step_call | None | 1 | yes |
| `settlements.provision` | `modules.settlements.provision:provision` | query | None | 0 | yes |
| `settlements.subsist` | `modules.settlements.subsist:subsist` | step_call | None | 1 | yes |
| `social_contest.roll` | `modules.social_contest.roll:roll` | verb_call | tell | 48 | yes |

## Call sites of `composition.require` outside the registrar (`grep -rn "require(" engine/season modules`, resolved by reading each line; tests excluded)

| site | role constant | what it reaches |
|---|---|---|
| `engine/season/manifest/registrar.py:115` `register_module_entries` | every row with `entry:` | fills `MODULE_ENTRIES` at `SeasonDriver.__init__` |
| `engine/season/queries/world_q.py:1358` `_entry` | `LARDER_DRAW`, `DRAWN_UNDER`, `HOUSING`, `FABRIC`, `FORTIFICATION` | the settlements queries, driverless callers included (the docstring says why it is not `MODULE_ENTRIES`) |
| `engine/season/loop/effects_army.py:57` | `world_q.ARMY` | `modules.mass_battle.armyrecord:apply` |
| `engine/season/loop/effects_information.py:119` | `ARMY` | `armyrecord:apply` with op `validate` |
| `engine/season/seam/wrappers/mass_battle.py:214` | `world_q.ARMY_ORDER` | `armyrecord:fielded` |
| `engine/season/seam/wrappers/mass_battle.py:343` | `world_q.PROVISION` | `modules.settlements.provision:provision` |
| `engine/season/seam/wrappers/sigma.py:246` `_composed_obstacle` | `_ROLL_ROLE` = `social_contest.roll` | **not the row's target**: `importlib.import_module(composition.require(role).__module__).obstacle(inp)`, the module attribute `obstacle`, which no composition row names |
| `engine/season/harness/army_presets.py:61` | `world_q.ARMY_PRESET` | `troop_types.presets:plan` |
| `engine/season/harness/military_menu.py:101` | `world_q.ARMY_OPTIONS` | `armyrecord:options` |

The four provider adapters (`seam/wrappers/{combat,mass_battle,fieldwork,sigma}.py`) look their entry up in `MODULE_ENTRIES` through `seam/wrappers/_entry.py::entry_for`; the nine sites above look the same rows up through `composition.require` and its `_CACHE`. Both return the callable `composition.require(role)` resolved.

## Providers registered in code (`@provider(role, module)`; `grep -n "@provider" engine/season/seam/wrappers/*.py`)

- `engine/season/seam/wrappers/combat.py:286:@provider("estimate", _PROVIDER)`
- `engine/season/seam/wrappers/combat.py:324:@provider("contest", _PROVIDER)`
- `engine/season/seam/wrappers/fieldwork.py:63:@provider("inquiry", _PROVIDER)`
- `engine/season/seam/wrappers/mass_battle.py:354:@provider("contest", _PROVIDER)`
- `engine/season/seam/wrappers/mass_battle.py:509:@provider("estimate", _PROVIDER)`
- `engine/season/seam/wrappers/sigma.py:451:@provider("contest", _PROVIDER)`

## Runtime calls that enter `modules/`, `engine/dice_engine/`, `engine/substrate/` from another area (one-season realm run, seed 0; from `W4`)

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

