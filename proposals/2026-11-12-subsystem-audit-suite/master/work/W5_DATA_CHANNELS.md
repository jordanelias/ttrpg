# W5 · data channels: the registries code reads, what is in them, and who reads them (M2)

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12).

## 1. The season registries: bytes that are values and bytes that are prose

Method: `yaml.safe_load` each file; sum the length of every string leaf by the name of its key; whole-line `#` comments summed apart. `*_note` and `note` leaves are annotations the loaders skip by rule (`engine/season/data/rosters.py:1402`, `:1462`; `engine/season/data/verbs.py:616-627`), except `requires_typed_note`, `effect_decline_note` and `requires_decline_note`, whose **presence** the verb loader checks (`data/verbs.py:662-667`, `:759-762`).

| file | bytes | comment bytes | string-leaf bytes | the largest string keys |
|---|---|---|---|---|
| `engine/season/rosters.yaml` | 359,435 | 48,638 | 237,839 | `note` 183,132; `source` 27,617; `ground` 6,112; `cite` 3,099 |
| `engine/season/verb_table.yaml` | 353,681 | 31,431 | 283,535 | `requires_typed_note` 67,126; `referent_class_note` 49,561; `writes_note` 38,648; `refusal_note` 19,236; `emits_note` 12,880; `source` 10,701; `requires_note` 10,666 |
| `engine/season/requirements.yaml` | 165,722 | 6,054 | 147,810 | `measured` 135,348; `note` 7,435; `measure` 2,063; `statement` 790 |
| `engine/season/write_matrix.yaml` | 37,077 | 14,608 | 16,831 | `by` 10,958; `reason` 2,096 |
| `engine/season/offices.yaml` | 36,887 | 15,381 | 11,416 | `note` 5,431; `source` 2,780 |
| `engine/season/goals.yaml` | 33,373 | 6,777 | 19,803 | `source` 13,914; `text` 3,176 |
| `engine/season/arrangements.yaml` | 20,020 | 13,936 | 964 | (values) |
| `engine/season/npcs.yaml` | 19,238 | 1,585 | 13,762 | `want` 11,205 (content) |
| `engine/season/venues.yaml` | 14,680 | 7,760 | 2,663 | (values) |
| `engine/season/cohorts.yaml` | 14,109 | 10,745 | 417 | (values) |
| `engine/season/governance_spine.yaml` | 9,218 | 7,879 | 508 | (values) |
| `engine/season/hole_register.yaml` | 1,315,682 | not weighed | not weighed | read by the corpus grader, not the loop (CLAUDE.md §3) |

`rosters.yaml`: two top-level keys, `rosters:` (119 named rosters, lines 99 to 3506) and `tables:` (8 tables, lines 3507 to 4548); 4,548 lines. Roster field shapes: 27 rosters carry `(note, source, values)`, 22 `(note, open, source, values)`, 12 `(cite, note, source, values)`, the rest twelve other shapes. One roster key is named by no non-test `.py` as a quoted string (`knowledge_kinds`; `audits/25_GROUNDING_ENGINE.md` V-17 records the same) and one by tests only (`witness_channel_predicates`); a key read through a derived name would be missed by this match.

`verb_table.yaml`: one key `verbs:`, a list of 67 rows; 10 columns on every row (`verb, stratum, eligibility, beneficiary, requires, writes, emits, emits_on_refusal, grade, source`), 41 further column names of which 31 end in `_note`.

## 2. The typed exports under `engine/engine_params/`

| artifact | bytes | written by | read at runtime by | read by the port |
|---|---|---|---|---|
| `composition.json` | 15,051 | `tools/export_composition.py` (from `references/module_contracts.yaml`) | `engine/substrate/composition.py` | not stated |
| `descriptors.json` | 5,126 | `tools/export_descriptors.py` (from `references/descriptor_registry.yaml`) | `engine/substrate/descriptors.py` | not stated |
| `names.json` | 8,971 | `tools/export_names.py` (from `references/names_index.yaml`) | `engine/substrate/names.py` | not stated |
| `combat_engine_v1.json` | 10,275 | `tools/export_engine_params.py` (from `modules/combat/*.py`) | `engine/substrate/combat_kit.py` (`sections.kit`) | its `_generated` line says the port validates against it |
| `battle_orders.json` | small | `tools/export_battle_orders.py` (from `modules/mass_battle/massbattle.py`) | `engine/substrate/battle_orders.py` | not stated |
| `sim_params.json` | 123,333 | `tools/export_sim_params.py` (AST literals at module scope) | **nothing under `engine/` or `modules/`**; `tools/export_game_constants.py`, `tools/link_values_pointers.py` | through `game_constants.json` |
| `game_constants.json` | 5,506 | `tools/export_game_constants.py` | nothing here | `valoria-game/tools/check_constants_parity.py` (its `_generated` line); 5 constants, 2 collisions, 3 divergences |
| `value_pointer_links.json` | 23,151 | `tools/link_values_pointers.py` | **nothing** but its own test (`tests/valoria/test_link_values_pointers.py`) | not stated |

`sim_params.json` holds 283 constants: `mass_battle` 164, `threadwork` 36, `social_contest` 31, `engine.season` 21, `fieldwork` 15, `engine.dice_engine` 6, `characters` 5, `overview` 5; 125 of 283 carry a citation. `python tools/export_sim_params.py --check` prints `[SIM-PARAMS] current` (run by this lane).

## 3. The season's own numbers: `Fixtures`

`engine/season/data/fixtures.py`: 1,170 lines, of which 219 code, 861 whole-line comment, 62 docstring. `DEFAULT_FIXTURES = Fixtures(...)` (`:213`) passes **101 keyword arguments**: 40 `int`, 22 `float`, 20 `str` (selectors such as `fan_out_mode='all_five'`, `scene_packing_rule='greedy'`, `wound_harm_model='scene_fraction'`, `field_casualty_model='scaled_by_degree'`), 7 `bool`, 4 tuples, 3 `None`, 5 names of tables loaded in the same file. Read through `Fixtures.get(name)` (`:44`), which raises on an unregistered name and counts reads; 218 `.get(` read sites in non-test `engine/season` and `modules/`, over 99 distinct names. **These 101 values are call arguments, not module-scope constants, so `tools/export_sim_params.py` does not see them** (its `engine.season` block holds 21 constants).

## 4. Other data the engine reads from outside `engine/`

`engine/season/data/files.py`: `GEOGRAPHY_YAML = systems/settlements/valoria_geography_v30.yaml` (`:147`), `MODULE_CONTRACTS_YAML = references/module_contracts.yaml` (`:149`), `NPC_REGISTRY_YAML = references/npc_registry.yaml` (`:158`), `CLAUDE_MD` (`:150`), `ARCH_PLAN_MD = architecture/PLAN.md` (`:92`).
