# C1 · top-level functions and classes the game code never names outside their own file (leads)

Name-based and conservative: dynamic dispatch by string, `getattr`, registry `target:` strings and YAML composition rows are searched (YAML hits excluded here); a flagged symbol may still be reached by a string built at runtime. Columns: file:line · name · lines · uses in own file besides the def · uses in tests · uses in tools · reading.

| file:line | name | lines | own | tests | tools | reading |
|---|---|---|---|---|---|---|
| `engine/season/harness/soak.py:256` | `_run_world` | 180 | 1 | 1 | 0 | file-local only |
| `systems/threadwork/sim/opposing.py:102` | `resolve_opposing_operations` | 168 | 3 | 7 | 0 | file-local only |
| `systems/threadwork/sim/collective.py:71` | `attempt_collective_operation` | 159 | 3 | 7 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:222` | `analyze` | 133 | 5 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1965` | `a5` | 104 | 0 | 7 | 0 | unreferenced anywhere in game code |
| `systems/mass_battle/sim/stress.py:182` | `analyse` | 95 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:114` | `resolve_threadcut_interaction` | 82 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:66` | `run_cell` | 81 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1415` | `f10` | 79 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/social_contest/sim/contest/agon_harness.py:419` | `run_contest_interactive` | 78 | 3 | 0 | 0 | file-local only |
| `engine/season/data/arrangements.py:156` | `_load_arrangement` | 75 | 1 | 3 | 0 | file-local only |
| `engine/season/harness/aperture.py:357` | `wrong_kind` | 73 | 12 | 14 | 0 | file-local only |
| `engine/season/harness/register.py:631` | `check_requirements` | 71 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:248` | `_trajectory` | 69 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:374` | `build_processes` | 66 | 2 | 5 | 0 | file-local only |
| `engine/season/harness/obligee_report.py:98` | `read_obligee_reports` | 64 | 1 | 11 | 0 | file-local only |
| `engine/season/harness/probes.py:666` | `p15` | 61 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/core/contact.py:417` | `_find_contacts_standoff` | 60 | 1 | 2 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/commentary.py:115` | `_beat` | 60 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/conviction_spread.py:68` | `_eigenvalues` | 58 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:4943` | `_StrifeReading` | 57 | 21 | 2 | 0 | file-local only |
| `systems/mass_battle/sim/bat.py:662` | `_mode_key` | 56 | 1 | 0 | 1 | file-local only |
| `engine/season/state/world.py:279` | `_encode_into` | 55 | 8 | 1 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:313` | `human_turn` | 55 | 2 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:160` | `_object` | 51 | 1 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:414` | `_goal_stages` | 50 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:793` | `pool_worlds` | 50 | 2 | 2 | 0 | file-local only |
| `engine/season/harness/strife_data.py:37` | `load_moves` | 49 | 1 | 5 | 0 | file-local only |
| `engine/season/harness/probes.py:758` | `p18` | 48 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/queries/world_q.py:2900` | `current_stage` | 47 | 5 | 22 | 0 | file-local only |
| `engine/season/data/affiliations.py:84` | `_load_incompatibility` | 46 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:2817` | `a31c` | 46 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2867` | `a39` | 46 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/corpus_run.py:367` | `_check_cast` | 45 | 6 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:315` | `read_persons` | 44 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/register.py:315` | `rule_G13` | 44 | 1 | 4 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:118` | `strike_profile` | 44 | 2 | 0 | 0 | file-local only |
| `engine/season/data/rosters.py:1448` | `_load_endings` | 43 | 1 | 2 | 0 | file-local only |
| `engine/season/data/requires.py:247` | `Requirement` | 42 | 10 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1989` | `_check_alignment_density` | 42 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:389` | `strands_block` | 42 | 2 | 3 | 0 | file-local only |
| `modules/combat/weapon_physics.py:367` | `delivered_strike` | 42 | 7 | 0 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:2444` | `_relax_bodies` | 42 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:2182` | `a14` | 41 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `modules/mass_battle/orchestration.py:561` | `_compute_atom_sides` | 41 | 3 | 1 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:70` | `zero_caller_functions` | 41 | 2 | 0 | 0 | file-local only |
| `systems/threadwork/sim/co_movement.py:94` | `draw_comovement_card` | 41 | 1 | 0 | 0 | file-local only |
| `engine/season/decision/options.py:1364` | `_person_bags` | 40 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:2485` | `a31b` | 39 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:480` | `grade_mix` | 39 | 4 | 9 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:82` | `_worker` | 39 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:864` | `p22` | 38 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/characters/sim/conviction.py:120` | `ConvictionState` | 38 | 7 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:277` | `v_reform` | 38 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:391` | `read_decisions` | 37 | 2 | 4 | 0 | file-local only |
| `engine/season/harness/probes.py:2399` | `a28` | 37 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/storybar.py:406` | `draw_seed_arm` | 37 | 4 | 7 | 0 | file-local only |
| `modules/mass_battle/geometry.py:62` | `_build_shape_n` | 37 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:202` | `_pair_toi_scale` | 37 | 3 | 1 | 0 | file-local only |
| `engine/season/harness/register.py:277` | `rule_G8` | 36 | 1 | 6 | 0 | file-local only |
| `modules/mass_battle/percell.py:107` | `_apply_with_spill` | 36 | 5 | 1 | 0 | file-local only |
| `engine/season/harness/aperture.py:941` | `pooled_report` | 35 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1140` | `p36` | 35 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:316` | `flow_profile` | 35 | 3 | 2 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:114` | `target_points` | 35 | 1 | 7 | 0 | file-local only |
| `engine/season/harness/interactions.py:330` | `act_rows` | 34 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:395` | `p2y` | 34 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:978` | `p28` | 34 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/data/goals.py:379` | `_stages` | 33 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1511` | `f12` | 33 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/manifest/registry.py:238` | `_check_step_declares` | 32 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/core/contact.py:479` | `_find_contacts_field` | 32 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1400` | `_load_projection` | 31 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:845` | `_wrong_kind_blocks` | 31 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:2609` | `p37` | 31 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/aperture.py:666` | `_refusal_blocks` | 30 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1688` | `_seed_near_floor` | 30 | 5 | 0 | 0 | file-local only |
| `engine/season/harness/register.py:245` | `rule_G12` | 30 | 1 | 3 | 0 | file-local only |
| `engine/season/harness/soak.py:146` | `_act_row` | 30 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2868` | `_goal_referents` | 30 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/equipment/_base.py:15` | `EquipmentRecord` | 30 | 4 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:678` | `_compute_front_fixers` | 30 | 4 | 5 | 0 | file-local only |
| `systems/combat/combat_engine_v1/state_graph.py:155` | `fired_states_from_events` | 30 | 5 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:190` | `coupling_matrix` | 30 | 1 | 0 | 0 | file-local only |
| `engine/season/data/rosters.py:1392` | `_load_modules` | 29 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1039` | `p31` | 29 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5002` | `_move_referents` | 29 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/interactions.py:117` | `office_relation` | 28 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:353` | `link_lines` | 28 | 1 | 2 | 0 | file-local only |
| `engine/season/queries/world_q.py:1375` | `_larder_parts` | 28 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/orderofbattle.py:142` | `_spec_for` | 28 | 1 | 1 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:348` | `check_law_exponents` | 28 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/conviction_spread.py:200` | `_report` | 27 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/populated.py:226` | `_institutions` | 27 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:228` | `p1` | 27 | 0 | 54 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1283` | `f5` | 27 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2929` | `p42` | 27 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/queries/world_q.py:372` | `docketed_by` | 27 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/arms.py:160` | `_resolve_arm` | 26 | 2 | 5 | 0 | file-local only |
| `engine/season/harness/probes.py:2755` | `a37` | 26 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2786` | `a38` | 26 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:542` | `grade_run` | 26 | 1 | 3 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:1503` | `_obscuring_probe` | 26 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:191` | `setup_contest` | 26 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:253` | `print_appraise` | 26 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:281` | `print_bars` | 26 | 4 | 0 | 0 | file-local only |
| `systems/threadwork/sim/coherence.py:166` | `CoherenceLogEntry` | 26 | 4 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:376` | `ContainPath` | 25 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/arms.py:188` | `run_arm` | 25 | 2 | 3 | 0 | file-local only |
| `engine/season/harness/military_menu.py:46` | `MilitaryMenu` | 25 | 9 | 1 | 0 | file-local only |
| `engine/season/harness/probes.py:835` | `p21` | 25 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1598` | `f16` | 25 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2092` | `a8` | 25 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/combat/combat_engine_v1/workbench/server.py:65` | `do_montecarlo` | 25 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:160` | `ask_choice` | 25 | 8 | 0 | 0 | file-local only |
| `engine/season/data/rosters.py:1119` | `_load_strife_kinds` | 24 | 1 | 4 | 0 | file-local only |
| `engine/season/harness/aperture.py:895` | `_answered_blocks` | 24 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/arms.py:215` | `two_proportion_z` | 24 | 3 | 5 | 0 | file-local only |
| `engine/season/harness/probes.py:549` | `p10` | 24 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:598` | `p12` | 24 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:579` | `_parse_args` | 24 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2675` | `_ending_edges` | 24 | 2 | 15 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:279` | `fight_one` | 24 | 1 | 1 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:219` | `print_setup_screen` | 24 | 2 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:904` | `_check_known_person_claim` | 23 | 1 | 4 | 0 | file-local only |
| `engine/season/harness/aperture.py:595` | `measure_world` | 23 | 3 | 2 | 0 | file-local only |
| `engine/season/harness/invariants.py:53` | `_entities` | 23 | 2 | 7 | 1 | file-local only |
| `engine/season/harness/loops.py:214` | `_simple_cycles` | 23 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:639` | `p14` | 23 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:919` | `p24` | 23 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1370` | `f8` | 23 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/seam/wrappers/mass_battle.py:192` | `_order_of_battle` | 23 | 3 | 1 | 0 | file-local only |
| `modules/combat/weapon_physics.py:156` | `_all_parts` | 23 | 5 | 1 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/build_levers.py:186` | `archetypes` | 23 | 4 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:323` | `_best_exponent` | 23 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/degree_extension.py:60` | `PoolDesaturation` | 23 | 1 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:966` | `_check_shortfall_stem` | 22 | 2 | 4 | 0 | file-local only |
| `engine/season/harness/invariants.py:249` | `carrier_census` | 22 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/populated.py:589` | `acquaintance_pairs` | 22 | 2 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:4410` | `PersonProjection` | 22 | 3 | 2 | 0 | file-local only |
| `engine/season/seam/contest.py:94` | `_returned` | 22 | 5 | 0 | 0 | file-local only |
| `engine/season/state/gate.py:657` | `check_revocation_disposal` | 22 | 2 | 7 | 0 | file-local only |
| `engine/season/state/gate.py:705` | `check_filled_by` | 22 | 1 | 4 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:654` | `_expire_charger_latches` | 22 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:239` | `write_reference` | 22 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:155` | `weapon_armour_matrix` | 22 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:258` | `memorial_remonstrance_venue` | 22 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/coherence.py:411` | `check_coherence_failure_transition` | 22 | 2 | 3 | 0 | file-local only |
| `engine/season/gaps.py:87` | `Ineligible` | 21 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/arc.py:142` | `validate_roster` | 21 | 9 | 5 | 0 | file-local only |
| `engine/season/harness/obligee_report.py:71` | `ObligeeReading` | 21 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1548` | `f13` | 21 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2460` | `a31` | 21 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/storybar.py:154` | `_depths` | 21 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:318` | `run_seed` | 21 | 1 | 1 | 0 | file-local only |
| `engine/season/loop/effects_information.py:127` | `_content_of` | 21 | 4 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5045` | `_Chain` | 21 | 8 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:331` | `_fed` | 21 | 4 | 1 | 0 | file-local only |
| `modules/combat/core.py:303` | `_transmit` | 21 | 9 | 5 | 0 | file-local only |
| `systems/characters/sim/conviction.py:245` | `check_conviction_threshold` | 21 | 3 | 2 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:254` | `v_envelop` | 21 | 3 | 4 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:219` | `imperial_petition_venue` | 21 | 1 | 0 | 0 | file-local only |
| `engine/season/data/arrangements.py:134` | `_load_speech_kind` | 20 | 1 | 2 | 0 | file-local only |
| `engine/season/data/requires.py:144` | `_Unknown` | 20 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:268` | `kind_census` | 20 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/aperture.py:432` | `death_census` | 20 | 2 | 4 | 0 | file-local only |
| `engine/season/harness/probes.py:2528` | `a32` | 20 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2724` | `f21` | 20 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/storybar.py:233` | `executed_summary` | 20 | 5 | 1 | 0 | file-local only |
| `engine/season/harness/storybar.py:451` | `_print_draw_seeds` | 20 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:294` | `link_profile` | 20 | 2 | 5 | 0 | file-local only |
| `engine/season/loop/effects_combat.py:686` | `_siege` | 20 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:1080` | `own_purview` | 20 | 3 | 4 | 0 | file-local only |
| `engine/season/queries/world_q.py:3765` | `stage_referents` | 20 | 3 | 15 | 0 | file-local only |
| `engine/season/queries/world_q.py:5233` | `_eras` | 20 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:2169` | `freed_attacker_damage` | 20 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:46` | `_convex_hull` | 20 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:121` | `tradition_context_matrix` | 20 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:195` | `build_page` | 20 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:592` | `_mend_own_configuration` | 20 | 1 | 0 | 0 | file-local only |
| `engine/season/data/cast.py:87` | `_rows` | 19 | 3 | 23 | 1 | file-local only |
| `engine/season/data/goals.py:139` | `_org` | 19 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1445` | `_load_role_template_pursuits` | 19 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/chronicle.py:86` | `deepest_chain` | 19 | 4 | 3 | 0 | file-local only |
| `engine/season/harness/heir_hears.py:57` | `HeirSpy` | 19 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/interactions.py:397` | `print_summary` | 19 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/populated.py:802` | `goals_missing` | 19 | 3 | 3 | 0 | file-local only |
| `engine/season/harness/probes.py:1722` | `w1` | 19 | 0 | 34 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:448` | `grade_cost` | 19 | 4 | 7 | 0 | file-local only |
| `engine/season/queries/world_q.py:4820` | `check_strife_openers` | 19 | 2 | 5 | 0 | file-local only |
| `engine/season/queries/world_q.py:5487` | `open_referents_known` | 19 | 4 | 3 | 0 | file-local only |
| `engine/season/state/attribution.py:156` | `_cover_for` | 19 | 2 | 1 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:2423` | `_pairs_within` | 19 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:604` | `_cell_damage_weights` | 19 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/dictionaries.py:583` | `_build_proceedings_table` | 19 | 1 | 0 | 0 | file-local only |
| `engine/season/data/fixtures.py:143` | `_check_keyed_on_site_kinds` | 18 | 2 | 0 | 0 | file-local only |
| `engine/season/decision/options.py:1005` | `holds_own_document` | 18 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:758` | `pools_lines` | 18 | 1 | 4 | 0 | file-local only |
| `engine/season/harness/heir_hears.py:100` | `seeded_reading` | 18 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:174` | `stance_row_shape` | 18 | 5 | 1 | 1 | file-local only |
| `engine/season/harness/loops.py:239` | `derive_cycles` | 18 | 3 | 4 | 0 | file-local only |
| `engine/season/harness/loops.py:286` | `check_bounds` | 18 | 3 | 5 | 0 | file-local only |
| `engine/season/harness/soak.py:178` | `_canary_h156` | 18 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/faction_q.py:225` | `_check_sheet_keys` | 18 | 2 | 3 | 0 | file-local only |
| `modules/combat/ability_primitives.py:112` | `_generics` | 18 | 2 | 0 | 0 | file-local only |
| `modules/combat/wrapper.py:57` | `_carry` | 18 | 4 | 12 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:86` | `_sweep` | 18 | 3 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:142` | `v_fixing` | 18 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:400` | `v_sweep` | 18 | 2 | 4 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:60` | `_snap_unit` | 18 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:181` | `inquisition_hearing_venue` | 18 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:200` | `excommunication_court_venue` | 18 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:397` | `attempt_past_pulling` | 18 | 1 | 1 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:72` | `ThreadcutState` | 18 | 4 | 0 | 0 | file-local only |
| `engine/season/data/matrix.py:119` | `MatrixRow` | 17 | 5 | 0 | 0 | file-local only |
| `engine/season/decision/sheet.py:116` | `DevelopmentSheet` | 17 | 6 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:182` | `read_label` | 17 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:317` | `_referent` | 17 | 4 | 2 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:509` | `print_persons` | 17 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:528` | `p9` | 17 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1655` | `f18` | 17 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:165` | `part_b_defects` | 17 | 2 | 1 | 0 | file-local only |
| `engine/season/loop/effects_founding.py:26` | `_works_named` | 17 | 6 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/sigma.py:331` | `_estimated` | 17 | 2 | 1 | 0 | file-local only |
| `modules/mass_battle/percell.py:195` | `_erode_cell_morale_from_damage` | 17 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/terrain.py:77` | `_point_in_polygon` | 17 | 1 | 6 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:165` | `tier_table` | 17 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/commentary.py:177` | `render_text` | 17 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:162` | `v_shock` | 17 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:181` | `v_brace` | 17 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:355` | `v_archer` | 17 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/wrapper.py:91` | `_as_contestant` | 17 | 2 | 0 | 0 | file-local only |
| `engine/season/data/arrangements.py:89` | `_refuse_not_in` | 16 | 6 | 1 | 0 | file-local only |
| `engine/season/data/verbs.py:1898` | `_derive_rung_remit_acts` | 16 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:317` | `deaths_of` | 16 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:704` | `verb_counts` | 16 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/arc.py:173` | `ambition_thrusts` | 16 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/conviction_spread.py:50` | `_covariance` | 16 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:891` | `degrees_by_verb` | 16 | 3 | 5 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:926` | `emits_and_writes_nothing` | 16 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:245` | `tally_split` | 16 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:108` | `tenure_referent` | 16 | 3 | 3 | 0 | file-local only |
| `engine/season/harness/probes.py:1808` | `w7` | 16 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1828` | `w8` | 16 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2306` | `a22` | 16 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:439` | `_cite_norm` | 16 | 6 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2701` | `_opened_by_acts` | 16 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5068` | `_links` | 16 | 6 | 0 | 0 | file-local only |
| `engine/season/state/attribution.py:220` | `_a_stage_unmatured` | 16 | 3 | 0 | 0 | file-local only |
| `engine/season/state/gate.py:1119` | `_closes` | 16 | 8 | 0 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:256` | `to_order_of_battle` | 16 | 3 | 6 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:169` | `_effective_reach` | 16 | 1 | 2 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:71` | `_duel` | 16 | 3 | 1 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:106` | `_attacker_retained` | 16 | 12 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:124` | `v_cannae` | 16 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:200` | `_attacker_envelop` | 16 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:218` | `_set_movement_path` | 16 | 5 | 10 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:236` | `_envelop_reach` | 16 | 4 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:337` | `_archer_far_loss` | 16 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:382` | `_sweep_disp` | 16 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:379` | `print_move_result` | 16 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:401` | `_describe_verdict` | 16 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:241` | `secret_council_venue` | 16 | 1 | 0 | 0 | file-local only |
| `engine/dice_engine/sigma_leverage.py:299` | `_net_counts` | 15 | 1 | 1 | 0 | file-local only |
| `engine/season/data/arrangements.py:117` | `_parse_floor` | 15 | 1 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:213` | `_pursuits` | 15 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:878` | `_death_blocks` | 15 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/arc.py:196` | `ArcReading` | 15 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:832` | `foreign_kinds` | 15 | 0 | 6 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/decision_spread.py:145` | `apply_control` | 15 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/interactions.py:418` | `print_audit` | 15 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:78` | `_all_tenures` | 15 | 5 | 1 | 0 | file-local only |
| `engine/season/harness/probes.py:433` | `p3` | 15 | 0 | 23 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:495` | `p7` | 15 | 0 | 5 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1636` | `f17` | 15 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2353` | `a25` | 15 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2573` | `a36` | 15 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:188` | `rule_R0` | 15 | 1 | 3 | 0 | file-local only |
| `engine/season/manifest/registry.py:387` | `check_estimate_providers` | 15 | 1 | 2 | 0 | file-local only |
| `engine/season/manifest/registry.py:534` | `_graded_verb_emits_it` | 15 | 3 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:5438` | `check_restraint_kinds` | 15 | 2 | 5 | 0 | file-local only |
| `engine/season/state/world.py:174` | `_TenureSnap` | 15 | 6 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:625` | `_accum_cell_damage` | 15 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:320` | `_archer_pair` | 15 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:141` | `_print_table` | 15 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/wrapper.py:220` | `_stub` | 15 | 3 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:417` | `attempt_locking` | 15 | 1 | 2 | 0 | file-local only |
| `engine/season/data/goals.py:236` | `_thrust_axes` | 14 | 2 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:331` | `_ancestors` | 14 | 2 | 0 | 0 | file-local only |
| `engine/season/data/rosters.py:753` | `check_logged_kinds` | 14 | 1 | 4 | 0 | file-local only |
| `engine/season/harness/chronicle.py:177` | `consequence_chains` | 14 | 2 | 12 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:131` | `_exercise_docs` | 14 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/interactions.py:147` | `known_via` | 14 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:147` | `claim_not_from_the_future` | 14 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/probes.py:1397` | `f9` | 14 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1946` | `a4` | 14 | 0 | 14 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2705` | `f20` | 14 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:470` | `_rows_text_excluding` | 14 | 1 | 0 | 0 | file-local only |
| `engine/season/manifest/registry.py:518` | `_bound_verb_contests_it` | 14 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:3013` | `engaged_poles` | 14 | 2 | 5 | 0 | file-local only |
| `engine/season/queries/world_q.py:5094` | `_attach` | 14 | 4 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5508` | `concluded_known` | 14 | 5 | 6 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:187` | `_read_sites` | 14 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:166` | `public_oration_venue` | 14 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:521` | `_use_tracker` | 14 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1599` | `_derive_holding_record_kinds` | 13 | 2 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1672` | `_load_vocation_sourced` | 13 | 1 | 2 | 0 | file-local only |
| `engine/season/data/verbs.py:1703` | `_load_choice_sourced` | 13 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1863` | `_load_violence_contexts` | 13 | 1 | 2 | 0 | file-local only |
| `engine/season/decision/options.py:457` | `_crime_context` | 13 | 0 | 1 | 0 | unreferenced anywhere in game code |
| `engine/season/epistemic.py:152` | `_tenure_by_id` | 13 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:469` | `scene_sources` | 13 | 2 | 4 | 0 | file-local only |
| `engine/season/harness/interactions.py:217` | `_question` | 13 | 1 | 9 | 0 | file-local only |
| `engine/season/harness/loops.py:359` | `_exists_reads` | 13 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:188` | `_one_pass` | 13 | 7 | 6 | 0 | file-local only |
| `engine/season/harness/probes.py:478` | `p6` | 13 | 0 | 4 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:103` | `_require_out_dir` | 13 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:118` | `_require_clean_engine` | 13 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:209` | `_person_row` | 13 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:221` | `terminal_for` | 13 | 2 | 3 | 0 | file-local only |
| `engine/season/harness/strife.py:236` | `_single_code_runs` | 13 | 2 | 0 | 0 | file-local only |
| `modules/combat/core.py:595` | `strike_impact` | 13 | 5 | 23 | 0 | file-local only |
| `modules/combat/weapon_physics.py:42` | `_ltr_sum` | 13 | 9 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:479` | `_merge_intervals` | 13 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:187` | `_reach_throttle` | 13 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `modules/mass_battle/hierarchy/units.py:2400` | `_ToiCell` | 13 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/massbattle.py:106` | `_round_half_up` | 13 | 4 | 0 | 0 | file-local only |
| `modules/mass_battle/massbattle.py:242` | `_retreat_orders` | 13 | 6 | 6 | 0 | file-local only |
| `modules/mass_battle/massbattle.py:358` | `_oob_unit` | 13 | 2 | 4 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:1560` | `_volley_density_mult` | 13 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/capabilities.py:80` | `markdown_table` | 13 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:106` | `tradition_field_table` | 13 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:1415` | `_cr4_church_tribunal_adv` | 13 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:1647` | `_armature_track` | 13 | 3 | 0 | 0 | file-local only |
| `systems/threadwork/sim/collective.py:47` | `CollectiveResult` | 13 | 5 | 0 | 0 | file-local only |
| `systems/threadwork/sim/opposing.py:87` | `_degree_label` | 13 | 2 | 2 | 0 | file-local only |
| `engine/dice_engine/dice_engine.py:191` | `_require_tn7` | 12 | 2 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:271` | `_axis` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:48` | `_check_operand_subset` | 12 | 4 | 2 | 0 | file-local only |
| `engine/season/data/rosters.py:775` | `_check_scale_of_rung` | 12 | 2 | 7 | 0 | file-local only |
| `engine/season/data/verbs.py:1495` | `_check_deed_kinds` | 12 | 2 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1750` | `_load_own_stance_declines` | 12 | 1 | 2 | 0 | file-local only |
| `engine/season/data/verbs.py:1771` | `_load_lie_verbs` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1796` | `_load_own_hold_declines` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1820` | `_load_own_title_declines` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/decision/sheet.py:74` | `CreationRow` | 12 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:722` | `pool_verb_counts` | 12 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/aperture.py:927` | `seed_row` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:551` | `print_season` | 12 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:579` | `run_arms` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/populated.py:133` | `_index_anchor` | 12 | 8 | 4 | 0 | file-local only |
| `engine/season/harness/populated.py:255` | `institution_of` | 12 | 5 | 0 | 1 | file-local only |
| `engine/season/harness/populated.py:284` | `surname_index` | 12 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1113` | `p34` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2132` | `a10` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2165` | `a13` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2336` | `a24` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2659` | `p39` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2675` | `p40` | 12 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/strife.py:170` | `opening_routes` | 12 | 4 | 1 | 0 | file-local only |
| `engine/season/queries/person_q.py:288` | `_kind_engages` | 12 | 2 | 0 | 0 | file-local only |
| `modules/combat/combat_systems.py:65` | `forward_extent` | 12 | 7 | 0 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:84` | `by_type` | 12 | 3 | 10 | 0 | file-local only |
| `modules/mass_battle/geometry.py:379` | `_normalize_heading` | 12 | 4 | 2 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:162` | `approach_alignment` | 12 | 0 | 4 | 0 | unreferenced anywhere in game code |
| `systems/combat/combat_engine_v1/workbench/balance.py:179` | `_md_weapon_armour` | 12 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:106` | `_place_line` | 12 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:68` | `_multi_subunit_row_ids` | 12 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/degree_extension.py:90` | `owner_overwhelming_margin` | 12 | 1 | 1 | 0 | file-local only |
| `engine/season/data/verbs.py:1213` | `_check_duel_terms` | 11 | 1 | 3 | 0 | file-local only |
| `engine/season/data/verbs.py:1726` | `_load_held_document_declines` | 11 | 1 | 2 | 0 | file-local only |
| `engine/season/data/verbs.py:1842` | `_load_held_edge_declines` | 11 | 1 | 3 | 0 | file-local only |
| `engine/season/harness/aperture.py:163` | `_Replay` | 11 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:738` | `_span_status` | 11 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:528` | `print_decisions` | 11 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/exercises.py:155` | `orphan_cases` | 11 | 1 | 3 | 0 | file-local only |
| `engine/season/harness/interactions.py:194` | `person_targets` | 11 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:95` | `tenure_interval` | 11 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/invariants.py:228` | `office_singly_held` | 11 | 4 | 1 | 1 | file-local only |
| `engine/season/harness/probes.py:452` | `p4` | 11 | 0 | 10 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:820` | `p20` | 11 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1848` | `w9` | 11 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:457` | `_contains` | 11 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:529` | `load_series` | 11 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/soak.py:605` | `_require_fresh_world_dir` | 11 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/cache.py:86` | `_build_tenure_index` | 11 | 1 | 0 | 0 | file-local only |
| `modules/combat/combat_systems.py:488` | `_element_mass_x` | 11 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/terrain.py:96` | `_polygon_area` | 11 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:1363` | `_cr4_choice_adv` | 11 | 2 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:375` | `attempt_weaving` | 11 | 2 | 6 | 0 | file-local only |
| `engine/season/data/files.py:236` | `decision_modules` | 10 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `engine/season/data/verbs.py:1567` | `_asks_subject_held` | 10 | 4 | 2 | 0 | file-local only |
| `engine/season/harness/arms.py:255` | `_pool_arm` | 10 | 4 | 1 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:298` | `profile_key` | 10 | 2 | 2 | 0 | file-local only |
| `engine/season/harness/probes.py:514` | `p8` | 10 | 0 | 3 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:744` | `p17` | 10 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1025` | `p30` | 10 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2282` | `a20` | 10 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2385` | `a27` | 10 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2691` | `p41` | 10 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:91` | `_require_pinned_hashseed` | 10 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:198` | `_reachable_codes` | 10 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:282` | `_instances` | 10 | 3 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:3172` | `_heir_title_holders` | 10 | 1 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:3512` | `_top_arms` | 10 | 2 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:3753` | `open_stages` | 10 | 6 | 5 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:642` | `_merge_cell_damage` | 10 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/capabilities.py:23` | `_affords_point` | 10 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/state_graph.py:143` | `reachable_from` | 10 | 3 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:94` | `attribute_parity_table` | 10 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:143` | `_md_context` | 10 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:106` | `check_linear` | 10 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:94` | `_attacker` | 10 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:123` | `_run_one` | 10 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:750` | `_golden_trace` | 10 | 11 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:148` | `_raw_input` | 10 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/policy.py:45` | `counterpuncher` | 10 | 2 | 0 | 0 | file-local only |
| `engine/season/data/cast.py:118` | `name_of` | 9 | 0 | 2 | 3 | unreferenced anywhere in game code |
| `engine/season/data/verbs.py:1884` | `_derive_violent_verbs` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:201` | `_replayed` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:306` | `_events_by_act` | 9 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:335` | `_exists_zero_on` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:346` | `_lives_in` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:778` | `_verb_total_line` | 9 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:172` | `null_alignment` | 9 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/invariants.py:126` | `log_ids_unique` | 9 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/invariants.py:163` | `body_in_range` | 9 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/probes.py:626` | `p13` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:731` | `p16` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:906` | `p23` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:965` | `p27` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1269` | `f4` | 9 | 0 | 1 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1498` | `f11` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1585` | `f15` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1883` | `w12` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2249` | `a17` | 9 | 0 | 1 | 1 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2372` | `a26` | 9 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:374` | `_source_bucket` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:469` | `_tv_distance` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:192` | `summarise` | 9 | 7 | 1 | 0 | file-local only |
| `engine/season/harness/strife_data.py:26` | `declared_kinds` | 9 | 1 | 1 | 0 | file-local only |
| `engine/season/loop/effects_army.py:34` | `_army` | 9 | 2 | 34 | 0 | file-local only |
| `engine/season/queries/world_q.py:1755` | `lives_in` | 9 | 3 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:4798` | `_petitioned_matter` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/state/world.py:260` | `_object_head` | 9 | 1 | 1 | 0 | file-local only |
| `modules/combat/combat_systems.py:452` | `_commit_range_factor` | 9 | 2 | 3 | 0 | file-local only |
| `modules/combat/fight.py:44` | `_attr_kw` | 9 | 2 | 0 | 0 | file-local only |
| `modules/combat/weapon_physics.py:657` | `_guard_catch_raw` | 9 | 2 | 0 | 0 | file-local only |
| `modules/combat/wrapper.py:531` | `_terms_yielder` | 9 | 2 | 3 | 0 | file-local only |
| `modules/mass_battle/geometry.py:11` | `arrowhead_cells` | 9 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:393` | `_cascade_depth_key` | 9 | 5 | 4 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:1699` | `_cell_snapshot` | 9 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:151` | `nearest_target` | 9 | 1 | 3 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:177` | `_docstring_nodes` | 9 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:83` | `_defender` | 9 | 5 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:423` | `run_all` | 9 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:127` | `deliberative_body_venue` | 9 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:342` | `NegotiationMode` | 9 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:351` | `CeremonialMode` | 9 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/coherence.py:154` | `_displacement_band` | 9 | 1 | 0 | 0 | file-local only |
| `engine/season/data/arrangements.py:107` | `_refuse_any_not_in` | 8 | 5 | 1 | 0 | file-local only |
| `engine/season/data/goals.py:116` | `_through` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/data/rosters.py:1432` | `EndingRow` | 8 | 3 | 2 | 0 | file-local only |
| `engine/season/decision/choose.py:144` | `_odds_arm` | 8 | 3 | 0 | 0 | file-local only |
| `engine/season/decision/choose.py:224` | `_npc_effort_arm` | 8 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:909` | `bands_that_differ` | 8 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:127` | `realm_mean_pursuits` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:288` | `territory_of` | 8 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:541` | `print_split` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:137` | `log_not_from_the_future` | 8 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/populated.py:216` | `_mentions` | 8 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:380` | `p2x` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1573` | `f14` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1775` | `w4` | 8 | 0 | 14 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1796` | `w6` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2237` | `a16` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2440` | `a29` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:149` | `section_exists` | 8 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/scarce.py:171` | `shortfall_question` | 8 | 1 | 12 | 0 | file-local only |
| `engine/season/harness/strife.py:66` | `Readers` | 8 | 6 | 1 | 0 | file-local only |
| `engine/season/harness/strife.py:160` | `opening_producers` | 8 | 1 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:362` | `_docketing_ref` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2609` | `EndingReached` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2949` | `_aim_held_by_org_member` | 8 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:4364` | `_person_or_refuse` | 8 | 2 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/combat.py:187` | `_cause_record` | 8 | 4 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/sigma.py:250` | `_odds_of_input` | 8 | 2 | 5 | 0 | file-local only |
| `modules/combat/contact.py:18` | `_short_reach_exempt` | 8 | 1 | 0 | 0 | file-local only |
| `modules/combat/weapon_physics.py:262` | `grip_swing_ratio` | 8 | 1 | 3 | 0 | file-local only |
| `modules/combat/weapon_physics.py:292` | `phi_room_percussion` | 8 | 2 | 1 | 0 | file-local only |
| `modules/combat/weapon_physics.py:822` | `_arm_lever` | 8 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:104` | `_vertex_interior_angle` | 8 | 1 | 0 | 0 | file-local only |
| `systems/characters/sim/conviction.py:161` | `ConvictionThresholdState` | 8 | 2 | 0 | 0 | file-local only |
| `systems/characters/sim/conviction.py:268` | `mark_belief_revision_pending` | 8 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/combat/combat_engine_v1/workbench/balance.py:84` | `weapon_matchup_table` | 8 | 3 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:186` | `wilson_wins` | 8 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:141` | `check_no_annihilation` | 8 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:84` | `_prep` | 8 | 5 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:50` | `_subs` | 8 | 2 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:114` | `_collapse` | 8 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:185` | `_summary` | 8 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/server.py:117` | `do_roster_options` | 8 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:206` | `_adv` | 8 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:221` | `_adv_ev` | 8 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:478` | `_d3_paired` | 8 | 2 | 0 | 0 | file-local only |
| `systems/threadwork/sim/co_movement.py:84` | `_shuffle_deck` | 8 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/coherence.py:280` | `CoherenceFailureResult` | 8 | 3 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:225` | `_compute_degree` | 8 | 1 | 7 | 0 | file-local only |
| `engine/dice_engine/dice_engine.py:142` | `RollResult` | 7 | 4 | 0 | 0 | file-local only |
| `engine/season/data/arrangements.py:80` | `_refuse_unknown` | 7 | 2 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1617` | `_derive_declared_classes` | 7 | 1 | 0 | 0 | file-local only |
| `engine/season/decision/options.py:440` | `_context` | 7 | 4 | 3 | 0 | file-local only |
| `engine/season/decision/options.py:482` | `_defence_context` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/aperture.py:749` | `persons_separated` | 7 | 1 | 6 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:685` | `_register_sites` | 7 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:263` | `split_figures` | 7 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/invariants.py:299` | `_declared_for` | 7 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:455` | `_bound_arg` | 7 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:203` | `_run_d` | 7 | 8 | 20 | 0 | file-local only |
| `engine/season/harness/probes.py:467` | `p5` | 7 | 0 | 5 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:946` | `p25` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1872` | `w11` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1934` | `a3` | 7 | 0 | 27 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2121` | `a9` | 7 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2562` | `a34` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2597` | `w13` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2917` | `p43` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:229` | `_innermost_season_frame` | 7 | 3 | 0 | 0 | file-local only |
| `engine/season/loop/effects_combat.py:52` | `_yielder` | 7 | 4 | 0 | 0 | file-local only |
| `engine/season/loop/effects_combat.py:262` | `raised_capability` | 7 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:1746` | `_refuse_two_residences` | 7 | 3 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2965` | `_aim_rule` | 7 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:2974` | `check_aim_rules` | 7 | 4 | 2 | 0 | file-local only |
| `engine/season/queries/world_q.py:4789` | `_claimed_seat` | 7 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5158` | `_concluded` | 7 | 4 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:289` | `_seat_treasury` | 7 | 2 | 1 | 0 | file-local only |
| `engine/season/state/gate.py:464` | `_ground_reaches` | 7 | 3 | 3 | 0 | file-local only |
| `modules/combat/weapon_physics.py:735` | `_blade_edges` | 7 | 3 | 0 | 0 | file-local only |
| `modules/combat/weapon_physics.py:925` | `_geom_slide_max` | 7 | 1 | 0 | 0 | file-local only |
| `modules/combat/wrapper.py:49` | `_select` | 7 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:27` | `column_cells` | 7 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/state_graph.py:131` | `injection_markdown` | 7 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:207` | `_md_trad` | 7 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:213` | `_job` | 7 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:60` | `_safe` | 7 | 3 | 0 | 0 | file-local only |
| `systems/fieldwork/sim/knots.py:146` | `KnotState` | 7 | 11 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:168` | `_nodes` | 7 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:370` | `ai_turn` | 7 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/appraise.py:110` | `_dominant_axis` | 7 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/appraise.py:119` | `_strength_band` | 7 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:291` | `excommunication_mode` | 7 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:304` | `secret_council_mode` | 7 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/narrative.py:103` | `_per_exchange` | 7 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/policy.py:25` | `fallback_ladder` | 7 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/co_movement.py:63` | `CoMovementCard` | 7 | 4 | 0 | 0 | file-local only |
| `systems/threadwork/sim/collective.py:62` | `_helper_contribution` | 7 | 2 | 0 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:388` | `attempt_pulling` | 7 | 2 | 1 | 0 | file-local only |
| `systems/threadwork/sim/operations.py:434` | `attempt_dissolution` | 7 | 1 | 1 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:105` | `perception_band` | 7 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/dice_engine/sigma_leverage.py:316` | `_split_margin` | 6 | 3 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:79` | `GoalStages` | 6 | 2 | 1 | 0 | file-local only |
| `engine/season/data/matrix.py:208` | `_retirement` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/decision/options.py:473` | `_duel_context` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/aperture.py:129` | `seat_gated` | 6 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/aperture.py:650` | `_control_line` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:658` | `exists_zero` | 6 | 1 | 3 | 0 | file-local only |
| `engine/season/harness/aperture.py:736` | `_verb_line` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/army_presets.py:58` | `plan_for` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:217` | `_partition_cast` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:137` | `realm_mean_conviction` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:383` | `formed_set` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/populated.py:565` | `_first_holder` | 6 | 4 | 1 | 0 | file-local only |
| `engine/season/harness/probes.py:810` | `p19` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1103` | `p33` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1130` | `p35` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1314` | `f6` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1676` | `f19` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1765` | `w3` | 6 | 0 | 25 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2073` | `a6` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2227` | `a15` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2262` | `a18` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2296` | `a21` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2326` | `a23` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2552` | `a33` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2644` | `p38` | 6 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/soak.py:244` | `_record_escape` | 6 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:521` | `_read_jsonl` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:203` | `per_season` | 6 | 7 | 3 | 0 | file-local only |
| `engine/season/harness/storybar.py:255` | `executed_per_season` | 6 | 6 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:484` | `_fmt_exec` | 6 | 5 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:274` | `_by_pair` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/manifest/registry.py:54` | `_contracts` | 6 | 1 | 7 | 0 | file-local only |
| `engine/season/queries/person_q.py:746` | `_affiliations_violated_by` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:1208` | `_site_rungs` | 6 | 3 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:1590` | `_creating_act` | 6 | 1 | 2 | 0 | file-local only |
| `engine/season/queries/world_q.py:5120` | `_strand_of` | 6 | 3 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:217` | `_standing_order` | 6 | 3 | 2 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:298` | `_defender_treasury` | 6 | 2 | 1 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:323` | `_fielded_by` | 6 | 2 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/sigma.py:242` | `_composed_obstacle` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/state/gate.py:370` | `_seat_grants` | 6 | 5 | 0 | 0 | file-local only |
| `engine/season/state/world.py:271` | `_encode_object` | 6 | 2 | 0 | 0 | file-local only |
| `modules/combat/core.py:518` | `_puncture_adef` | 6 | 2 | 0 | 0 | file-local only |
| `modules/combat/weapon_physics.py:908` | `_gather_len` | 6 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:215` | `atom_max_width` | 6 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:421` | `_dist_point_to_segment` | 6 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:435` | `body_overlap` | 6 | 2 | 16 | 0 | file-local only |
| `modules/mass_battle/orderofbattle.py:172` | `_rows_of` | 6 | 2 | 16 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:164` | `_groups` | 6 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:207` | `exported_keys` | 6 | 2 | 1 | 0 | file-local only |
| `systems/fieldwork/sim/knots.py:392` | `reset_knots` | 6 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `systems/mass_battle/sim/stress.py:94` | `_depth` | 6 | 3 | 5 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:374` | `_attacker_sweep` | 6 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/walkthrough.py:42` | `_oob` | 6 | 2 | 8 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:161` | `_bands` | 6 | 2 | 17 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:240` | `_barred_out` | 6 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:269` | `_shapes` | 6 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/faction.py:41` | `_one_vote` | 6 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:77` | `appeal_venue` | 6 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:285` | `inquisition_mode` | 6 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:298` | `imperial_petition_mode` | 6 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:311` | `memorial_remonstrance_mode` | 6 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/opposing.py:79` | `opposing_engagement_modifier` | 6 | 3 | 0 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:92` | `mark_threadcut` | 6 | 1 | 0 | 0 | file-local only |
| `engine/season/data/goals.py:132` | `_text` | 5 | 2 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1916` | `_remit_acts_of_class` | 5 | 3 | 0 | 0 | file-local only |
| `engine/season/data/verbs.py:1923` | `_remit_acts_of` | 5 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:147` | `seat_depth` | 5 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/chronicle.py:170` | `chain_ends` | 5 | 6 | 17 | 0 | file-local only |
| `engine/season/harness/chronicle.py:193` | `render_chains` | 5 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:751` | `_emission_id` | 5 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:919` | `deposit_only_rulings` | 5 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:276` | `_cosine` | 5 | 2 | 3 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:565` | `_decider_total` | 5 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:572` | `_build` | 5 | 3 | 43 | 0 | file-local only |
| `engine/season/harness/interactions.py:104` | `same_faction` | 5 | 5 | 5 | 0 | file-local only |
| `engine/season/harness/loops.py:352` | `_leaves` | 5 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:1016` | `p29` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1745` | `w1x` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1787` | `w5` | 5 | 0 | 14 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2083` | `a7` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2156` | `a12` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2273` | `a19` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:232` | `rule_R3` | 5 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/run_cases.py:318` | `_probe_view` | 5 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/soak.py:202` | `_claim_row` | 5 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/storybar.py:226` | `executed_items` | 5 | 4 | 1 | 0 | file-local only |
| `engine/season/harness/strife.py:148` | `routeless_terminals` | 5 | 1 | 2 | 0 | file-local only |
| `engine/season/loop/matter.py:204` | `_HeldBefore` | 5 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/cache.py:71` | `TenureIndex` | 5 | 4 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:3184` | `_sworn_retainers` | 5 | 1 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:4896` | `flow_capacity` | 5 | 2 | 2 | 0 | file-local only |
| `engine/season/queries/world_q.py:5033` | `_content_matter` | 5 | 3 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5128` | `default_terminal` | 5 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5260` | `slot_rank` | 5 | 2 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:5458` | `_ledger_in_order` | 5 | 2 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/mass_battle.py:282` | `_causing_act` | 5 | 1 | 0 | 0 | file-local only |
| `engine/season/state/gate.py:1062` | `_committed_to` | 5 | 3 | 0 | 0 | file-local only |
| `engine/season/state/world.py:336` | `_canonical` | 5 | 12 | 43 | 0 | file-local only |
| `engine/substrate/stubwire.py:80` | `reset_invocations` | 5 | 1 | 3 | 1 | file-local only |
| `modules/combat/core.py:366` | `_shear_yield` | 5 | 1 | 1 | 0 | file-local only |
| `modules/combat/weapon_physics.py:108` | `energy_credit` | 5 | 4 | 3 | 0 | file-local only |
| `modules/combat/wrapper.py:36` | `_emit_outcome` | 5 | 4 | 2 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:50` | `_type` | 5 | 6 | 0 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:122` | `_sf_index` | 5 | 4 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:393` | `_rotate90` | 5 | 2 | 2 | 0 | file-local only |
| `modules/mass_battle/geometry.py:443` | `_reach_body_overlap` | 5 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:494` | `_interval_union_length` | 5 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:250` | `_subunit_depth` | 5 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:1709` | `_subunit_snapshot` | 5 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/perimeter.py:31` | `TargetPoint` | 5 | 6 | 0 | 0 | file-local only |
| `modules/mass_battle/resolution.py:164` | `_depth_prep` | 5 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/terrain.py:202` | `_on_segment` | 5 | 3 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:206` | `reference_table` | 5 | 2 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:193` | `_md_weapon` | 5 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/balance.py:200` | `_md_attr` | 5 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/probabilities.py:83` | `_beta_pdf` | 5 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/server.py:32` | `_make_fighter` | 5 | 4 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:214` | `dead_exported_keys` | 5 | 2 | 1 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:878` | `_raises` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/social_contest/sim/contest/_kernel_tests.py:1689` | `_same_off` | 5 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:115` | `_default_panel` | 5 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:121` | `fused_arbiter_venue` | 5 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/policy.py:32` | `off_ground_chancer` | 5 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/co_movement.py:137` | `reset_deck` | 5 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/threadwork/sim/operations.py:456` | `MendingPrice` | 5 | 3 | 0 | 0 | file-local only |
| `engine/dice_engine/sigma_leverage.py:292` | `_dice_dealt` | 4 | 2 | 0 | 0 | file-local only |
| `engine/reference/degree-sweep/sweep_core.py:132` | `contested_verbs` | 4 | 1 | 0 | 0 | file-local only |
| `engine/season/data/files.py:201` | `loop_source` | 4 | 0 | 2 | 0 | unreferenced anywhere in game code |
| `engine/season/data/goals.py:230` | `_is_orientation` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:689` | `_observe` | 4 | 8 | 1 | 0 | file-local only |
| `engine/season/data/verbs.py:1170` | `_produced_pairs` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/decision/options.py:450` | `_war_context` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/decision/options.py:973` | `_held_objects` | 4 | 3 | 0 | 0 | file-local only |
| `engine/season/decision/sheet.py:166` | `take_ranked` | 4 | 0 | 6 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/aperture.py:176` | `_observed_of` | 4 | 4 | 2 | 0 | file-local only |
| `engine/season/harness/aperture.py:454` | `source_key` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:644` | `_control_same` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:921` | `cr14_blocks` | 4 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/army_presets.py:52` | `_commander` | 4 | 1 | 7 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:377` | `decision_question` | 4 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/heir_hears.py:94` | `one_season` | 4 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/interactions.py:111` | `faction_heads` | 4 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/interactions.py:207` | `is_hostile` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/interactions.py:439` | `write_jsonl` | 4 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:188` | `_mul` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/probes.py:957` | `p26` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1628` | `f16b` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:1863` | `w10` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2148` | `a11` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/probes.py:2452` | `a30` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/harness/register.py:239` | `rule_G6` | 4 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/soak.py:238` | `_append_jsonl` | 4 | 4 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:445` | `chain_difference` | 4 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/strife.py:383` | `opened_on` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/loop/effects_army.py:45` | `_payload` | 4 | 6 | 2 | 0 | file-local only |
| `engine/season/loop/effects_founding.py:45` | `_made_by` | 4 | 6 | 0 | 0 | file-local only |
| `engine/season/loop/effects_migration.py:74` | `_arrival_only` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/loop/predicates.py:260` | `founded_office_id` | 4 | 2 | 3 | 0 | file-local only |
| `engine/season/manifest/registry.py:404` | `_takes_module_entry` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/person_q.py:380` | `_paired_weight` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:1433` | `_draw_dict` | 4 | 2 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:1439` | `_draw_record` | 4 | 1 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5344` | `_strains` | 4 | 2 | 0 | 0 | file-local only |
| `engine/season/seam/wrappers/pool.py:54` | `_held_attribute` | 4 | 2 | 0 | 0 | file-local only |
| `modules/combat/combatant.py:200` | `_attribute_property` | 4 | 1 | 0 | 0 | file-local only |
| `modules/combat/fight.py:32` | `_kit_kw` | 4 | 2 | 0 | 0 | file-local only |
| `modules/combat/fight.py:38` | `_faculty_kw` | 4 | 2 | 0 | 0 | file-local only |
| `modules/combat/geometry.py:60` | `percussion_concentration` | 4 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:57` | `_pos` | 4 | 7 | 0 | 0 | file-local only |
| `modules/mass_battle/armyrecord.py:129` | `_replace_sf` | 4 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/equipment/armour.py:50` | `dr_vs_piercing` | 4 | 7 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:21` | `line_cells` | 4 | 5 | 0 | 0 | file-local only |
| `modules/mass_battle/geometry.py:473` | `_project_interval` | 4 | 3 | 3 | 0 | file-local only |
| `modules/mass_battle/hierarchy/units.py:127` | `standoff_from_reach` | 4 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/terrain.py:196` | `_orient` | 4 | 4 | 0 | 0 | file-local only |
| `modules/mass_battle/troop_types/recruitment.py:72` | `training_site_for` | 4 | 2 | 1 | 0 | file-local only |
| `systems/combat/combat_engine_v1/capabilities.py:74` | `capability_table` | 4 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/build_levers.py:85` | `_hdr` | 4 | 7 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:180` | `newcombe` | 4 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/fieldwork/sim/knots.py:168` | `_count_knots_for_actor` | 4 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:162` | `_penetration` | 4 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/validators.py:71` | `_line` | 4 | 8 | 21 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:135` | `_row_passes_win_band` | 4 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/server.py:102` | `do_mode` | 4 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:18` | `ck` | 4 | 372 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:125` | `evrate` | 4 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:149` | `prate` | 4 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:307` | `_same` | 4 | 1 | 5 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:327` | `_reb` | 4 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:1544` | `_face_after_failed_obscuring` | 4 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:142` | `HarnessState` | 4 | 8 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:137` | `scholastic_disputation_venue` | 4 | 1 | 0 | 0 | file-local only |
| `engine/season/data/affiliations.py:79` | `_true_pairs` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/aperture.py:744` | `verb_totals` | 3 | 2 | 1 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:240` | `new_split` | 3 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:283` | `projected_vector` | 3 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/decision_spread.py:310` | `_pair_cosines` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/delta.py:62` | `_cases` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/interactions.py:99` | `held_offices` | 3 | 4 | 2 | 0 | file-local only |
| `engine/season/harness/invariants.py:342` | `carrier_census_keys` | 3 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/loops.py:306` | `row_quantities` | 3 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:442` | `loop_rows` | 3 | 7 | 1 | 0 | file-local only |
| `engine/season/harness/register.py:205` | `rule_R1` | 3 | 1 | 2 | 0 | file-local only |
| `engine/season/harness/soak.py:570` | `_fmt_grade` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/harness/storybar.py:492` | `_fmt_est` | 3 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/strife.py:143` | `terminal_codes` | 3 | 5 | 2 | 0 | file-local only |
| `engine/season/harness/strife.py:155` | `opening_kinds` | 3 | 1 | 1 | 0 | file-local only |
| `engine/season/harness/strife.py:184` | `routeless_pairs` | 3 | 3 | 1 | 0 | file-local only |
| `engine/season/manifest/registry.py:325` | `_as_list` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:256` | `_is_person_id` | 3 | 4 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:4938` | `Flows` | 3 | 4 | 1 | 0 | file-local only |
| `engine/season/queries/world_q.py:5040` | `_parents` | 3 | 5 | 0 | 3 | file-local only |
| `engine/season/queries/world_q.py:5115` | `_move_place` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/queries/world_q.py:5255` | `open_era` | 3 | 1 | 7 | 0 | file-local only |
| `engine/season/seam/wrappers/combat.py:124` | `load_error` | 3 | 2 | 15 | 0 | file-local only |
| `engine/season/state/gate.py:732` | `filled_by` | 3 | 4 | 0 | 0 | file-local only |
| `engine/season/state/world.py:169` | `_snapshot_fields` | 3 | 3 | 0 | 0 | file-local only |
| `engine/season/state/world.py:191` | `_payload_holders` | 3 | 2 | 0 | 0 | file-local only |
| `engine/season/state/world.py:255` | `_str_bytes` | 3 | 6 | 2 | 0 | file-local only |
| `modules/combat/combat_systems.py:88` | `_heft_of` | 3 | 2 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:271` | `rally_check` | 3 | 3 | 0 | 0 | file-local only |
| `modules/mass_battle/orchestration.py:316` | `threadwork_check` | 3 | 3 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:44` | `teaching_tradition` | 3 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/commentary.py:42` | `_who` | 3 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/narrate.py:21` | `_dist` | 3 | 3 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/bat.py:657` | `_cfg_mod` | 3 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/stress.py:79` | `_layout` | 3 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:190` | `_commfrac` | 3 | 4 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:282` | `_bt` | 3 | 26 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:504` | `_rawres` | 3 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:612` | `_rejects_opt_in` | 3 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:683` | `_bc_rejects` | 3 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/faction.py:37` | `_adj` | 3 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:70` | `disputation_venue` | 3 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/modes.py:282` | `public_oration_mode` | 3 | 1 | 0 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:100` | `is_threadcut` | 3 | 5 | 0 | 0 | file-local only |
| `systems/threadwork/sim/threadcut.py:198` | `reset_threadcut` | 3 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `engine/season/data/goals.py:108` | `_where` | 2 | 3 | 0 | 0 | file-local only |
| `engine/season/data/requires.py:213` | `_bound` | 2 | 11 | 0 | 0 | file-local only |
| `engine/season/decision/sheet.py:65` | `_frozen` | 2 | 12 | 0 | 0 | file-local only |
| `engine/season/harness/arc.py:112` | `ArcRosterRefused` | 2 | 6 | 3 | 0 | file-local only |
| `engine/season/harness/corpus_run.py:213` | `_waits_on_player` | 2 | 3 | 0 | 0 | file-local only |
| `engine/season/harness/interactions.py:435` | `_rows_by_i` | 2 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:311` | `_ledger_max` | 2 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/loops.py:315` | `_confidence_max` | 2 | 1 | 0 | 0 | file-local only |
| `engine/season/harness/obligee_report.py:94` | `_live_at` | 2 | 4 | 3 | 0 | file-local only |
| `engine/season/harness/probes.py:142` | `NOCHOOSE` | 2 | 6 | 9 | 0 | file-local only |
| `engine/season/harness/soak.py:198` | `_tenure_row` | 2 | 1 | 0 | 0 | file-local only |
| `engine/season/state/gate.py:1808` | `_nothing` | 2 | 1 | 0 | 0 | file-local only |
| `modules/combat/wrapper.py:528` | `_terms_met` | 2 | 4 | 1 | 0 | file-local only |
| `modules/mass_battle/equipment/weapons.py:63` | `with_keyword` | 2 | 1 | 0 | 0 | file-local only |
| `modules/mass_battle/troop_types/registry.py:147` | `support_ranks_for` | 2 | 2 | 6 | 0 | file-local only |
| `systems/combat/combat_engine_v1/state_graph.py:187` | `separation_reasons_from_events` | 2 | 4 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:62` | `cell_seed` | 2 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:56` | `_fighter` | 2 | 2 | 12 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/commentary.py:27` | `_commit_band` | 2 | 1 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/narrate.py:17` | `_pct` | 2 | 3 | 0 | 0 | file-local only |
| `systems/combat/combat_engine_v1/workbench/narrate.py:26` | `_sig` | 2 | 1 | 18 | 0 | file-local only |
| `systems/fieldwork/sim/knots.py:384` | `get_knot` | 2 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/fieldwork/sim/knots.py:388` | `get_active_knots` | 2 | 0 | 0 | 0 | unreferenced anywhere in game code |
| `systems/mass_battle/sim/altonian_reinforcements.py:20` | `invoke_altonian_reinforcements` | 2 | 1 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/lanchester_signature.py:319` | `_new_diag` | 2 | 3 | 0 | 0 | file-local only |
| `systems/mass_battle/sim/workbench/trace.py:33` | `_anchor_for` | 2 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:233` | `_bth` | 2 | 1 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:249` | `_awin` | 2 | 2 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/_kernel_tests.py:453` | `_d3` | 2 | 3 | 0 | 0 | file-local only |
| `systems/social_contest/sim/contest/agon_harness.py:249` | `_band_name` | 2 | 1 | 0 | 0 | file-local only |
| `modules/combat/weapons.py:845` | `_E` | 1 | 65 | 4 | 0 | file-local only |
| `systems/social_contest/sim/contest/policy.py:5` | `_low` | 1 | 8 | 0 | 0 | file-local only |
