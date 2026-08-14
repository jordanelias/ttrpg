# Valoria — Engine Atlas (generated)

> **GENERATED** by `tools/build_engine_atlas.py`. Do not hand-edit — a hand-edit is silently discarded on the next build.
>
> This is the **countable** half of the atlas. The reading guide, the campaign spine and the open-decision set are authored in [`systems/_architecture/engine_atlas_v1.md`](../systems/_architecture/engine_atlas_v1.md); the per-subsystem flow is authored in each `systems/<x>/<x>_flow_skeleton_v1.md`. Nothing here ratifies anything.

**15 subsystems** · sources: `module_contracts.yaml`, `key_graph.json`, `execution_map.json`, `execution_trace.json`, and the authored flow skeletons.

---

## 0. This document's own coverage

⚠ The generator reconciles the **filesystem** (what exists) against the **roster** (what is declared) and its inputs. These did not line up, and are reported rather than silently resolved — a generated atlas that quietly drops a new subsystem is worse than no atlas.

| reconciliation | items |
|---|---|
| Module contract mapping to no subsystem folder | `audit`, `campaign_architecture`, `clock_registry`, `domain_actions`, `scenario_authoring`, `scene_slate`, `scene_timer` |
| Execution-trace bucket matching no subsystem (engine-level paths are expected here) | `engine/autoload`, `engine/cross_scale`, `engine/substrate` |

---

## 1. Subsystem atlas

`reached` is measured from ONE seeded campaign (`references/execution_trace.json`). "not in trace" means that run did not call it — not that it is unreachable; the authored skeleton rules on reachability in principle.

| subsystem | lane | .py | contracts | reached | emits keys | gaps | flow skeleton |
|---|---|---|---|---|---|---|---|
| `_architecture` | IN | 0 | [`engine_clock`](CONTRACT_INDEX.md#engine_clock) | no code | 2 | 16 | [skeleton](../systems/_architecture/_architecture_flow_skeleton_v1.md) |
| `articulation` | IN | 0 | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) | no code | 1 | 9 | [skeleton](../systems/articulation/articulation_flow_skeleton_v1.md) |
| `characters` | PC | 3 | [`piety_track`](CONTRACT_INDEX.md#piety_track) | not in trace | 1 | 6 | [skeleton](../systems/characters/characters_flow_skeleton_v1.md) |
| `combat` | PC | 27 | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) | not in trace | 3 | 5 | [skeleton](../systems/combat/combat_flow_skeleton_v1.md) |
| `factions` | FA | 16 | [`ci_political`](CONTRACT_INDEX.md#ci_political), [`faction_politics`](CONTRACT_INDEX.md#faction_politics), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) | **yes** (1,346 calls) | 18 | 14 | [skeleton](../systems/factions/factions_flow_skeleton_v1.md) |
| `fieldwork` | FI | 3 | [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots) | not in trace | 4 | 9 | [skeleton](../systems/fieldwork/fieldwork_flow_skeleton_v1.md) |
| `mass_battle` | MB | 4 | [`mass_battle`](CONTRACT_INDEX.md#mass_battle) | **yes** (481,653 calls) | 1 | 9 | [skeleton](../systems/mass_battle/mass_battle_flow_skeleton_v1.md) |
| `npcs` | WR | 0 | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`npc_memory`](CONTRACT_INDEX.md#npc_memory) | no code | 11 | 9 | [skeleton](../systems/npcs/npcs_flow_skeleton_v1.md) |
| `overview` | IN | 6 | [`game_director`](CONTRACT_INDEX.md#game_director), [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain), [`territorial_piety`](CONTRACT_INDEX.md#territorial_piety) | not in trace | 8 | 17 | [skeleton](../systems/overview/overview_flow_skeleton_v1.md) |
| `settlements` | SE | 6 | [`settlement_economy`](CONTRACT_INDEX.md#settlement_economy), [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) | **yes** (1,983 calls) | 3 | 11 | [skeleton](../systems/settlements/settlements_flow_skeleton_v1.md) |
| `social_contest` | SC | 17 | [`social_contest`](CONTRACT_INDEX.md#social_contest) | **yes** (276 calls) | 4 | 15 | [skeleton](../systems/social_contest/social_contest_flow_skeleton_v1.md) |
| `threadwork` | WR | 7 | [`threadwork`](CONTRACT_INDEX.md#threadwork) | not in trace | 2 | 10 | [skeleton](../systems/threadwork/threadwork_flow_skeleton_v1.md) |
| `ui` | IN | 0 | — | no code | — | 8 | [skeleton](../systems/ui/ui_flow_skeleton_v1.md) |
| `victory` | IN | 0 | [`victory`](CONTRACT_INDEX.md#victory) | no code | 2 | 6 | [skeleton](../systems/victory/victory_flow_skeleton_v1.md) |
| `world` | WR | 4 | [`miraculous_event`](CONTRACT_INDEX.md#miraculous_event) | **yes** (108 calls) | 1 | 9 | [skeleton](../systems/world/world_flow_skeleton_v1.md) |

## 2. Declared vs executed

Each contract's declared `build`/`executes` status beside what the trace measured. A disagreement here is a finding, not noise: it means the status field and the run disagree about the same module.

| contract | subsystem | declared build | declared executes | trace |
|---|---|---|---|---|
| `engine_clock` | `_architecture` | design | False | no code |
| `articulation_layer` | `articulation` | stub | False | no code |
| `piety_track` | `characters` | deferred | False | not in trace |
| `personal_combat` | `combat` | unwired | False | not in trace |
| `ci_political` | `factions` | deferred | False | **yes** (1,346 calls) |
| `faction_politics` | `factions` | deferred | False | **yes** (1,346 calls) |
| `faction_state` | `factions` | deferred | False | **yes** (1,346 calls) |
| `npc_behavior` | `factions` | design | False | **yes** (1,346 calls) |
| `fieldwork_knots` | `fieldwork` | stub | False | not in trace |
| `mass_battle` | `mass_battle` | live | True | **yes** (481,653 calls) |
| `npc_behavior` | `npcs` | design | False | no code |
| `npc_memory` | `npcs` | design | False | no code |
| `game_director` | `overview` | deferred | False | not in trace |
| `peninsular_strain` | `overview` | deferred | False | not in trace |
| `territorial_piety` | `overview` | deferred | False | not in trace |
| `settlement_economy` | `settlements` | design | False | **yes** (1,983 calls) |
| `settlement_layer` | `settlements` | design | False | **yes** (1,983 calls) |
| `social_contest` | `social_contest` | gated | True | **yes** (276 calls) |
| `threadwork` | `threadwork` | unwired | False | not in trace |
| `victory` | `victory` | live | True | no code |
| `miraculous_event` | `world` | stub | False | **yes** (108 calls) |

## 3. Authored-coverage check

Public top-level callables in each subsystem folder that its authored skeleton never names, found by AST. **These are candidates, not defects** — a flow skeleton lists what an outside caller can enter through, which is narrower than every public def, so a helper legitimately never appears. The list matters because this is exactly where hand-tracing drops things, and recomputing it is free.

| subsystem | public callables | not named in skeleton |
|---|---|---|
| `_architecture` | 0 | 0 |
| `articulation` | 0 | 0 |
| `characters` | 16 | 0 |
| `combat` | 201 | 148 |
| `factions` | 46 | 25 |
| `fieldwork` | 15 | 0 |
| `mass_battle` | 42 | 16 |
| `npcs` | 0 | 0 |
| `overview` | 11 | 0 |
| `settlements` | 30 | 6 |
| `social_contest` | 150 | 101 |
| `threadwork` | 32 | 5 |
| `ui` | 0 | 0 |
| `victory` | 0 | 0 |
| `world` | 16 | 0 |

<details><summary><b>combat</b> — 148 unnamed</summary>

| callable | at |
|---|---|
| `ability_bonus` | `systems/combat/combat_engine_v1/ability_primitives.py:129` |
| `ability_factor` | `systems/combat/combat_engine_v1/ability_primitives.py:140` |
| `eff_cw` | `systems/combat/combat_engine_v1/ability_primitives.py:154` |
| `kit` | `systems/combat/combat_engine_v1/ability_primitives.py:83` |
| `allowed` | `systems/combat/combat_engine_v1/capabilities.py:67` |
| `capability_table` | `systems/combat/combat_engine_v1/capabilities.py:72` |
| `markdown_table` | `systems/combat/combat_engine_v1/capabilities.py:78` |
| `wound_impairment` | `systems/combat/combat_engine_v1/combat_systems.py:1037` |
| `clamp_initiative` | `systems/combat/combat_engine_v1/combat_systems.py:1163` |
| `init_steal_factor` | `systems/combat/combat_engine_v1/combat_systems.py:1171` |
| `init_hold_decay` | `systems/combat/combat_engine_v1/combat_systems.py:1182` |
| `init_overcommit_loss` | `systems/combat/combat_engine_v1/combat_systems.py:1188` |
| `poise_factor` | `systems/combat/combat_engine_v1/combat_systems.py:1194` |
| `clamp_poise` | `systems/combat/combat_engine_v1/combat_systems.py:1201` |
| `percussion_stagger` | `systems/combat/combat_engine_v1/combat_systems.py:1205` |
| `rear_clearance` | `systems/combat/combat_engine_v1/combat_systems.py:123` |
| `true_time_edge` | `systems/combat/combat_engine_v1/combat_systems.py:1278` |
| `choke_counterbalance` | `systems/combat/combat_engine_v1/combat_systems.py:129` |
| `stophit_sigma` | `systems/combat/combat_engine_v1/combat_systems.py:1297` |
| `pursuit_sigma` | `systems/combat/combat_engine_v1/combat_systems.py:1344` |
| `close_rate` | `systems/combat/combat_engine_v1/combat_systems.py:1367` |
| `arrest_impulse` | `systems/combat/combat_engine_v1/combat_systems.py:1381` |
| `lever_log_edge` | `systems/combat/combat_engine_v1/combat_systems.py:14` |
| `init_emphasis_sigma` | `systems/combat/combat_engine_v1/combat_systems.py:1415` |
| `consistency` | `systems/combat/combat_engine_v1/combat_systems.py:1422` |
| `mental_fatigue` | `systems/combat/combat_engine_v1/combat_systems.py:1426` |
| `poise_regen` | `systems/combat/combat_engine_v1/combat_systems.py:1432` |
| `act_cost` | `systems/combat/combat_engine_v1/combat_systems.py:165` |
| `reading` | `systems/combat/combat_engine_v1/combat_systems.py:171` |
| `reflex` | `systems/combat/combat_engine_v1/combat_systems.py:172` |
| `str_demand` | `systems/combat/combat_engine_v1/combat_systems.py:175` |
| `handling_penalty` | `systems/combat/combat_engine_v1/combat_systems.py:178` |
| `disp_lean` | `systems/combat/combat_engine_v1/combat_systems.py:181` |
| `balance_eff` | `systems/combat/combat_engine_v1/combat_systems.py:184` |
| `anti_overcommit` | `systems/combat/combat_engine_v1/combat_systems.py:189` |
| `recoverability_factor` | `systems/combat/combat_engine_v1/combat_systems.py:232` |
| `close_unwieldiness` | `systems/combat/combat_engine_v1/combat_systems.py:257` |
| `can_choke` | `systems/combat/combat_engine_v1/combat_systems.py:287` |
| `grip_target` | `systems/combat/combat_engine_v1/combat_systems.py:291` |
| `stance_stability` | `systems/combat/combat_engine_v1/combat_systems.py:320` |
| `mode_sigma` | `systems/combat/combat_engine_v1/combat_systems.py:329` |
| `adef_cap` | `systems/combat/combat_engine_v1/combat_systems.py:358` |
| `close_efficacy` | `systems/combat/combat_engine_v1/combat_systems.py:367` |
| `facing_target` | `systems/combat/combat_engine_v1/combat_systems.py:414` |
| `range_utilization` | `systems/combat/combat_engine_v1/combat_systems.py:425` |
| `element_afforded` | `systems/combat/combat_engine_v1/combat_systems.py:545` |
| `afforded_heads` | `systems/combat/combat_engine_v1/combat_systems.py:627` |
| `forward_extent` | `systems/combat/combat_engine_v1/combat_systems.py:64` |
| `reach_threat` | `systems/combat/combat_engine_v1/combat_systems.py:756` |
| `wield_heft` | `systems/combat/combat_engine_v1/combat_systems.py:78` |
| `affords_halfsword` | `systems/combat/combat_engine_v1/combat_systems.py:861` |
| `reach_sigma` | `systems/combat/combat_engine_v1/combat_systems.py:897` |
| `legibility` | `systems/combat/combat_engine_v1/combat_systems.py:914` |
| `approach_displace` | `systems/combat/combat_engine_v1/combat_systems.py:949` |
| `contact_moment_edge` | `systems/combat/combat_engine_v1/combat_systems.py:999` |
| `max_wounds` | `systems/combat/combat_engine_v1/combatant.py:30` |
| `wound_interval` | `systems/combat/combat_engine_v1/combatant.py:35` |
| `health_full` | `systems/combat/combat_engine_v1/combatant.py:40` |
| `stamina_max` | `systems/combat/combat_engine_v1/combatant.py:45` |
| `grab_sigma` | `systems/combat/combat_engine_v1/contact.py:41` |
| `thrust_authority` | `systems/combat/combat_engine_v1/core.py:328` |
| `cut_thrust_arm` | `systems/combat/combat_engine_v1/core.py:333` |
| `logistic` | `systems/combat/combat_engine_v1/core.py:34` |
| `coupling` | `systems/combat/combat_engine_v1/core.py:363` |
| `adef_cap` | `systems/combat/combat_engine_v1/core.py:425` |
| `roll_net` | `systems/combat/combat_engine_v1/core.py:56` |
| `heft_resp` | `systems/combat/combat_engine_v1/core.py:86` |
| `gap_precision` | `systems/combat/combat_engine_v1/geometry.py:28` |
| `thrust_factor` | `systems/combat/combat_engine_v1/geometry.py:37` |
| `cut_factor` | `systems/combat/combat_engine_v1/geometry.py:50` |
| `percussion_concentration` | `systems/combat/combat_engine_v1/geometry.py:60` |
| `can_halfsword_thrust` | `systems/combat/combat_engine_v1/geometry.py:65` |
| `bake` | `systems/combat/combat_engine_v1/geometry.py:70` |
| `injection_markdown` | `systems/combat/combat_engine_v1/state_graph.py:109` |
| `reachable_from` | `systems/combat/combat_engine_v1/state_graph.py:121` |
| `fired_states_from_events` | `systems/combat/combat_engine_v1/state_graph.py:133` |
| `separation_reasons_from_events` | `systems/combat/combat_engine_v1/state_graph.py:160` |
| `familiarity` | `systems/combat/combat_engine_v1/traditions.py:47` |
| `grip_swing_ratio` | `systems/combat/combat_engine_v1/weapon_physics.py:248` |
| `phi_grip` | `systems/combat/combat_engine_v1/weapon_physics.py:257` |
| `phi_room_percussion` | `systems/combat/combat_engine_v1/weapon_physics.py:278` |
| `hilt_assembly_mass` | `systems/combat/combat_engine_v1/weapon_physics.py:287` |
| `reversed_grip_percussion` | `systems/combat/combat_engine_v1/weapon_physics.py:318` |
| `delivered_strike` | `systems/combat/combat_engine_v1/weapon_physics.py:353` |
| `strike_point_lever` | `systems/combat/combat_engine_v1/weapon_physics.py:397` |
| `percussion_authority` | `systems/combat/combat_engine_v1/weapon_physics.py:442` |
| `puncture_pressure` | `systems/combat/combat_engine_v1/weapon_physics.py:493` |
| `percussion_element_authority` | `systems/combat/combat_engine_v1/weapon_physics.py:501` |
| `armour_defeat_mode` | `systems/combat/combat_engine_v1/weapon_physics.py:554` |
| `agility` | `systems/combat/combat_engine_v1/weapon_physics.py:566` |
| `defense_affinities` | `systems/combat/combat_engine_v1/weapon_physics.py:596` |
| `hand_guard` | `systems/combat/combat_engine_v1/weapon_physics.py:654` |
| `blade_guard` | `systems/combat/combat_engine_v1/weapon_physics.py:661` |
| `distraction` | `systems/combat/combat_engine_v1/weapon_physics.py:679` |
| `facing_pref` | `systems/combat/combat_engine_v1/weapon_physics.py:695` |
| `edge_vibration` | `systems/combat/combat_engine_v1/weapon_physics.py:705` |
| `edge_lines` | `systems/combat/combat_engine_v1/weapon_physics.py:730` |
| `grab_hazard` | `systems/combat/combat_engine_v1/weapon_physics.py:754` |
| `heft` | `systems/combat/combat_engine_v1/weapon_physics.py:809` |
| `handling` | `systems/combat/combat_engine_v1/weapon_physics.py:856` |
| `grip_travel_max` | `systems/combat/combat_engine_v1/weapon_physics.py:889` |
| `grip_choke_max` | `systems/combat/combat_engine_v1/weapon_physics.py:893` |
| `at_circumstance` | `systems/combat/combat_engine_v1/weapon_physics.py:907` |
| `energy_credit` | `systems/combat/combat_engine_v1/weapon_physics.py:92` |
| `at_grip` | `systems/combat/combat_engine_v1/weapon_physics.py:942` |
| `strike_profile` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:117` |
| `tier_table` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:164` |
| `reference_table` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:205` |
| `write_reference` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:238` |
| `capability` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:57` |
| `participation` | `systems/combat/combat_engine_v1/workbench/armour_participation.py:89` |
| `tradition_field_table` | `systems/combat/combat_engine_v1/workbench/balance.py:106` |
| `tradition_context_matrix` | `systems/combat/combat_engine_v1/workbench/balance.py:121` |
| `weapon_armour_matrix` | `systems/combat/combat_engine_v1/workbench/balance.py:155` |
| `winrate` | `systems/combat/combat_engine_v1/workbench/balance.py:56` |
| `abilities` | `systems/combat/combat_engine_v1/workbench/build_levers.py:121` |
| `armour` | `systems/combat/combat_engine_v1/workbench/build_levers.py:156` |
| `familiarity` | `systems/combat/combat_engine_v1/workbench/build_levers.py:172` |
| `archetypes` | `systems/combat/combat_engine_v1/workbench/build_levers.py:185` |
| `build` | `systems/combat/combat_engine_v1/workbench/build_levers.py:52` |
| `duel` | `systems/combat/combat_engine_v1/workbench/build_levers.py:63` |
| `values` | `systems/combat/combat_engine_v1/workbench/catalogue.py:171` |
| `coupling_matrix` | `systems/combat/combat_engine_v1/workbench/catalogue.py:188` |
| `constants` | `systems/combat/combat_engine_v1/workbench/catalogue.py:242` |
| `header` | `systems/combat/combat_engine_v1/workbench/catalogue.py:266` |
| `roster` | `systems/combat/combat_engine_v1/workbench/catalogue.py:49` |
| `render_text` | `systems/combat/combat_engine_v1/workbench/commentary.py:176` |
| `commentate` | `systems/combat/combat_engine_v1/workbench/commentary.py:47` |
| `render` | `systems/combat/combat_engine_v1/workbench/narrate.py:29` |
| `param_surface` | `systems/combat/combat_engine_v1/workbench/presets.py:31` |
| `effective_cfg` | `systems/combat/combat_engine_v1/workbench/presets.py:59` |
| `save_scratch` | `systems/combat/combat_engine_v1/workbench/presets.py:74` |
| `load_scratch` | `systems/combat/combat_engine_v1/workbench/presets.py:82` |
| `promote_diff` | `systems/combat/combat_engine_v1/workbench/presets.py:90` |
| `node_distribution` | `systems/combat/combat_engine_v1/workbench/probabilities.py:105` |
| `degree_distribution` | `systems/combat/combat_engine_v1/workbench/probabilities.py:25` |
| `read_win_p` | `systems/combat/combat_engine_v1/workbench/probabilities.py:49` |
| `outcome_distribution` | `systems/combat/combat_engine_v1/workbench/probabilities.py:54` |
| `beta_band_probs` | `systems/combat/combat_engine_v1/workbench/probabilities.py:91` |
| `do_trace` | `systems/combat/combat_engine_v1/workbench/server.py:49` |
| `do_montecarlo` | `systems/combat/combat_engine_v1/workbench/server.py:65` |
| `Handler` | `systems/combat/combat_engine_v1/workbench/server.py:93` |
| `exported_keys` | `systems/combat/combat_engine_v1/workbench/structure_scan.py:202` |
| `dead_exported_keys` | `systems/combat/combat_engine_v1/workbench/structure_scan.py:209` |
| `report` | `systems/combat/combat_engine_v1/workbench/structure_scan.py:217` |
| `zero_caller_functions` | `systems/combat/combat_engine_v1/workbench/structure_scan.py:65` |
| `run_traced_fight` | `systems/combat/combat_engine_v1/workbench/trace.py:14` |
| `ActionResult` | `systems/combat/sim/combat.py:100` |

</details>

<details><summary><b>factions</b> — 25 unnamed</summary>

| callable | at |
|---|---|
| `AbsolutionResult` | `systems/factions/sim/absolution.py:38` |
| `attempt_absolution` | `systems/factions/sim/absolution.py:50` |
| `select_absolution_target` | `systems/factions/sim/absolution.py:91` |
| `council_ob` | `systems/factions/sim/council_solmund.py:30` |
| `CouncilResult` | `systems/factions/sim/council_solmund.py:37` |
| `attempt_council` | `systems/factions/sim/council_solmund.py:49` |
| `attempt_great_work` | `systems/factions/sim/crown_initiative.py:131` |
| `coronation_renewal_ob` | `systems/factions/sim/crown_initiative.py:188` |
| `attempt_coronation_renewal` | `systems/factions/sim/crown_initiative.py:211` |
| `InitiativeResult` | `systems/factions/sim/crown_initiative.py:278` |
| `royal_progress_ob` | `systems/factions/sim/crown_initiative.py:45` |
| `attempt_royal_progress` | `systems/factions/sim/crown_initiative.py:61` |
| `ExcommResult` | `systems/factions/sim/excommunication.py:63` |
| `attempt_excommunication` | `systems/factions/sim/excommunication.py:78` |
| `is_available` | `systems/factions/sim/mass_seizure.py:300` |
| `SeizureDeclaration` | `systems/factions/sim/mass_seizure.py:85` |
| `SeizureResult` | `systems/factions/sim/mass_seizure.py:95` |
| `select_censure_target` | `systems/factions/sim/parliamentary_action.py:63` |
| `TransferResult` | `systems/factions/sim/parliamentary_transfer.py:80` |
| `get_active_treaties` | `systems/factions/sim/treaty.py:157` |
| `reset_registry` | `systems/factions/sim/treaty.py:162` |
| `TreatyResult` | `systems/factions/sim/treaty.py:86` |
| `ExpirationResult` | `systems/factions/sim/treaty.py:93` |
| `TribunalResult` | `systems/factions/sim/tribunal.py:60` |
| `formal_grounds_check` | `systems/factions/sim/tribunal.py:73` |

</details>

<details><summary><b>mass_battle</b> — 16 unnamed</summary>

| callable | at |
|---|---|
| `freed_attacker_damage` | `systems/mass_battle/sim/massbattle.py:1500` |
| `arrowhead_cells` | `systems/mass_battle/sim/massbattle.py:369` |
| `line_cells` | `systems/mass_battle/sim/massbattle.py:379` |
| `horseshoe_cells` | `systems/mass_battle/sim/massbattle.py:384` |
| `gapped_line_cells` | `systems/mass_battle/sim/massbattle.py:398` |
| `refused_flank_cells` | `systems/mass_battle/sim/massbattle.py:411` |
| `oriented_pattern` | `systems/mass_battle/sim/massbattle.py:432` |
| `cell_facing` | `systems/mass_battle/sim/massbattle.py:439` |
| `octagon_angle` | `systems/mass_battle/sim/massbattle.py:451` |
| `atom_max_width` | `systems/mass_battle/sim/massbattle.py:480` |
| `cells_to_orig_coords` | `systems/mass_battle/sim/massbattle.py:489` |
| `support_engage_frac` | `systems/mass_battle/sim/massbattle.py:503` |
| `cell_speed` | `systems/mass_battle/sim/massbattle.py:591` |
| `roll_pool` | `systems/mass_battle/sim/massbattle.py:627` |
| `compute_degree` | `systems/mass_battle/sim/massbattle.py:640` |
| `count_engagements_per_atom` | `systems/mass_battle/sim/massbattle.py:804` |

</details>

<details><summary><b>settlements</b> — 6 unnamed</summary>

| callable | at |
|---|---|
| `BuildResult` | `systems/settlements/sim/infrastructure.py:103` |
| `reset_infrastructure` | `systems/settlements/sim/infrastructure.py:257` |
| `reset_registry` | `systems/settlements/sim/registry.py:210` |
| `SettlementState` | `systems/settlements/sim/settlement.py:45` |
| `ProvinceState` | `systems/settlements/sim/settlement.py:65` |
| `reset_drift` | `systems/settlements/sim/temperaments.py:168` |

</details>

<details><summary><b>social_contest</b> — 101 unnamed</summary>

| callable | at |
|---|---|
| `evrate` | `systems/social_contest/sim/contest/_kernel_tests.py:122` |
| `prate` | `systems/social_contest/sim/contest/_kernel_tests.py:146` |
| `ck` | `systems/social_contest/sim/contest/_kernel_tests.py:18` |
| `rate` | `systems/social_contest/sim/contest/_kernel_tests.py:22` |
| `bad` | `systems/social_contest/sim/contest/_kernel_tests.py:417` |
| `HarnessState` | `systems/social_contest/sim/contest/agon_harness.py:141` |
| `ask_choice` | `systems/social_contest/sim/contest/agon_harness.py:159` |
| `setup_contest` | `systems/social_contest/sim/contest/agon_harness.py:190` |
| `print_setup_screen` | `systems/social_contest/sim/contest/agon_harness.py:218` |
| `print_appraise` | `systems/social_contest/sim/contest/agon_harness.py:252` |
| `print_bars` | `systems/social_contest/sim/contest/agon_harness.py:280` |
| `human_turn` | `systems/social_contest/sim/contest/agon_harness.py:312` |
| `ai_turn` | `systems/social_contest/sim/contest/agon_harness.py:369` |
| `print_move_result` | `systems/social_contest/sim/contest/agon_harness.py:378` |
| `run_contest_interactive` | `systems/social_contest/sim/contest/agon_harness.py:418` |
| `appraise_armature` | `systems/social_contest/sim/contest/appraise.py:140` |
| `ArmatureAxis` | `systems/social_contest/sim/contest/armature.py:191` |
| `ArmaturePosition` | `systems/social_contest/sim/contest/armature.py:262` |
| `style_axis_alignment` | `systems/social_contest/sim/contest/armature.py:346` |
| `style_axis_dsigma` | `systems/social_contest/sim/contest/armature.py:357` |
| `position_of` | `systems/social_contest/sim/contest/armature.py:374` |
| `Adjudicator` | `systems/social_contest/sim/contest/contract.py:25` |
| `Pressure` | `systems/social_contest/sim/contest/contract.py:70` |
| `InteractionType` | `systems/social_contest/sim/contest/dictionaries.py:270` |
| `derive_interaction` | `systems/social_contest/sim/contest/dictionaries.py:310` |
| `AdjudicatorType` | `systems/social_contest/sim/contest/dictionaries.py:337` |
| `FactionBoost` | `systems/social_contest/sim/contest/dictionaries.py:387` |
| `guilds_boost_for` | `systems/social_contest/sim/contest/dictionaries.py:473` |
| `Proceeding` | `systems/social_contest/sim/contest/dictionaries.py:503` |
| `Genre` | `systems/social_contest/sim/contest/dictionaries.py:60` |
| `Orientation` | `systems/social_contest/sim/contest/dictionaries.py:67` |
| `Style` | `systems/social_contest/sim/contest/dictionaries.py:76` |
| `succession_rate` | `systems/social_contest/sim/contest/faction.py:120` |
| `coalition_rate` | `systems/social_contest/sim/contest/faction.py:150` |
| `rate` | `systems/social_contest/sim/contest/faction.py:59` |
| `band_of` | `systems/social_contest/sim/contest/faction.py:68` |
| `rate_banded` | `systems/social_contest/sim/contest/faction.py:76` |
| `fused_arbiter_venue` | `systems/social_contest/sim/contest/modes.py:121` |
| `deliberative_body_venue` | `systems/social_contest/sim/contest/modes.py:127` |
| `scholastic_disputation_venue` | `systems/social_contest/sim/contest/modes.py:137` |
| `single_arbiter_mode` | `systems/social_contest/sim/contest/modes.py:142` |
| `deliberative_body_mode` | `systems/social_contest/sim/contest/modes.py:144` |
| `scholastic_disputation_mode` | `systems/social_contest/sim/contest/modes.py:147` |
| `public_oration_venue` | `systems/social_contest/sim/contest/modes.py:166` |
| `excommunication_court_venue` | `systems/social_contest/sim/contest/modes.py:200` |
| `imperial_petition_venue` | `systems/social_contest/sim/contest/modes.py:219` |
| `secret_council_venue` | `systems/social_contest/sim/contest/modes.py:241` |
| `memorial_remonstrance_venue` | `systems/social_contest/sim/contest/modes.py:258` |
| `public_oration_mode` | `systems/social_contest/sim/contest/modes.py:282` |
| `inquisition_mode` | `systems/social_contest/sim/contest/modes.py:285` |
| `imperial_petition_mode` | `systems/social_contest/sim/contest/modes.py:298` |
| `secret_council_mode` | `systems/social_contest/sim/contest/modes.py:304` |
| `memorial_remonstrance_mode` | `systems/social_contest/sim/contest/modes.py:311` |
| `DyadicMode` | `systems/social_contest/sim/contest/modes.py:333` |
| `NegotiationMode` | `systems/social_contest/sim/contest/modes.py:342` |
| `CeremonialMode` | `systems/social_contest/sim/contest/modes.py:351` |
| `expert_judge` | `systems/social_contest/sim/contest/modes.py:433` |
| `crowd` | `systems/social_contest/sim/contest/modes.py:440` |
| `no_adjudicator` | `systems/social_contest/sim/contest/modes.py:449` |
| `proceeding_mode` | `systems/social_contest/sim/contest/modes.py:569` |
| `court_venue` | `systems/social_contest/sim/contest/modes.py:66` |
| `disputation_venue` | `systems/social_contest/sim/contest/modes.py:70` |
| `assembly_venue` | `systems/social_contest/sim/contest/modes.py:73` |
| `appeal_venue` | `systems/social_contest/sim/contest/modes.py:77` |
| `courtier` | `systems/social_contest/sim/contest/policy.py:12` |
| `build_then_close` | `systems/social_contest/sim/contest/policy.py:15` |
| `exploiter` | `systems/social_contest/sim/contest/policy.py:20` |
| `fallback_ladder` | `systems/social_contest/sim/contest/policy.py:25` |
| `off_ground_chancer` | `systems/social_contest/sim/contest/policy.py:32` |
| `advocate` | `systems/social_contest/sim/contest/policy.py:37` |
| `overreacher` | `systems/social_contest/sim/contest/policy.py:43` |
| `staller` | `systems/social_contest/sim/contest/policy.py:44` |
| `counterpuncher` | `systems/social_contest/sim/contest/policy.py:45` |
| `logos_spammer` | `systems/social_contest/sim/contest/policy.py:6` |
| `demagogue` | `systems/social_contest/sim/contest/policy.py:9` |
| `FaceScale` | `systems/social_contest/sim/contest/primitives.py:132` |
| `RhetoricalWeights` | `systems/social_contest/sim/contest/primitives.py:185` |
| `Pool` | `systems/social_contest/sim/contest/primitives.py:208` |
| `Leverage` | `systems/social_contest/sim/contest/primitives.py:222` |
| `Resonance` | `systems/social_contest/sim/contest/primitives.py:238` |
| `Readiness` | `systems/social_contest/sim/contest/primitives.py:253` |
| `DefeatCatalogue` | `systems/social_contest/sim/contest/primitives.py:262` |
| `Appeal` | `systems/social_contest/sim/contest/primitives.py:27` |
| `WinCondition` | `systems/social_contest/sim/contest/resolver.py:50` |
| `ThresholdRace` | `systems/social_contest/sim/contest/resolver.py:52` |
| `TallyAtClose` | `systems/social_contest/sim/contest/resolver.py:60` |
| `ProofBar` | `systems/social_contest/sim/contest/resolver.py:65` |
| `GraceThreshold` | `systems/social_contest/sim/contest/resolver.py:72` |
| `genre_of_ground` | `systems/social_contest/sim/contest/rhetoric.py:101` |
| `primary_genre_for` | `systems/social_contest/sim/contest/rhetoric.py:160` |
| `is_pre_merits` | `systems/social_contest/sim/contest/rhetoric.py:172` |
| `is_higher_order_reframe` | `systems/social_contest/sim/contest/rhetoric.py:178` |
| `genre_of_style` | `systems/social_contest/sim/contest/rhetoric.py:209` |
| `primary_genre_pool_bonus` | `systems/social_contest/sim/contest/rhetoric.py:221` |
| `orientation_channel` | `systems/social_contest/sim/contest/rhetoric.py:399` |
| `cr5_self_backfire` | `systems/social_contest/sim/contest/rhetoric.py:413` |
| `build_argue_pool` | `systems/social_contest/sim/contest_legacy_stub.py:111` |
| `resolve_exchange` | `systems/social_contest/sim/contest_legacy_stub.py:132` |
| `ExchangeResult` | `systems/social_contest/sim/contest_legacy_stub.py:84` |
| `ContestResult` | `systems/social_contest/sim/contest_legacy_stub.py:99` |
| `VoteResult` | `systems/social_contest/sim/parliamentary_vote.py:96` |

</details>

<details><summary><b>threadwork</b> — 5 unnamed</summary>

| callable | at |
|---|---|
| `reset_deck` | `systems/threadwork/sim/co_movement.py:155` |
| `ZeroTransitionResult` | `systems/threadwork/sim/coherence.py:105` |
| `reset_all` | `systems/threadwork/sim/coherence.py:193` |
| `CoherenceLogEntry` | `systems/threadwork/sim/coherence.py:66` |
| `reset_threadcut` | `systems/threadwork/sim/threadcut.py:198` |

</details>

**Corpus coverage:** 258 of 559 public callables (46.2%) are named by an authored skeleton.

## 4. Attribution provenance

How each contract was attributed to its subsystem. `declared` is a package-level `VALORIA_CONTRACTS` metakey — the only source that survives a file move; the rest are inferred. Adoption is voluntary, so this line is the adoption meter, not a failure: **0 of 15** subsystems declare.

| contract | subsystem | attributed by |
|---|---|---|
| `engine_clock` | `_architecture` | `authored` |
| `articulation_layer` | `articulation` | `authored` |
| `piety_track` | `characters` | `authored`, `code`, `graph` |
| `personal_combat` | `combat` | `authored`, `code`, `graph` |
| `ci_political` | `factions` | `authored` |
| `faction_politics` | `factions` | `authored` |
| `faction_state` | `factions` | `authored` |
| `npc_behavior` | `factions` | `authored` |
| `fieldwork_knots` | `fieldwork` | `authored`, `code`, `graph` |
| `mass_battle` | `mass_battle` | `authored` |
| `npc_behavior` | `npcs` | `authored` |
| `npc_memory` | `npcs` | `authored` |
| `game_director` | `overview` | `authored` |
| `peninsular_strain` | `overview` | `authored`, `code`, `graph` |
| `territorial_piety` | `overview` | `authored`, `code`, `graph` |
| `settlement_economy` | `settlements` | `authored` |
| `settlement_layer` | `settlements` | `authored`, `code`, `graph` |
| `social_contest` | `social_contest` | `authored`, `code`, `graph` |
| `threadwork` | `threadwork` | `authored`, `code`, `graph` |
| `victory` | `victory` | `authored` |
| `miraculous_event` | `world` | `authored`, `code`, `graph` |

## 5. Nomenclature — can a canonical name be found by searching for it?

A canonical identifier is only a usable handle if searching for it returns its references and little else. **Key types satisfy this by construction** — dotted and distinctive, median 27 occurrence(s). **Contract names largely do not**: several are ordinary English words, so the count below is dominated by unrelated prose and identifiers (median 129). This is evidence for a naming rule, not the rule itself — nothing is enforced here.

`qualified` counts uses of a namespaced form (`contract:<name>`), the convention `_identifier_census.yaml` already uses with `key:`/`py:`. A name with a high raw count and zero qualified uses cannot be located by search today.

| contract | bare occurrences | qualified uses |
|---|---|---|
| `mass_battle` | 2494 | 0 |
| `threadwork` | 2237 | 0 |
| `audit` | 2235 | 0 |
| `social_contest` | 2173 | 0 |
| `victory` | 2101 | 0 |
| `npc_behavior` | 649 | 0 |
| `settlement_layer` | 346 | 0 |
| `faction_state` | 342 | 0 |
| `articulation_layer` | 319 | 0 |
| `scene_slate` | 197 | 0 |
| `peninsular_strain` | 175 | 0 |
| `piety_track` | 152 | 0 |

