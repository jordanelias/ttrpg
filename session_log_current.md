session_id: faction_stability_military_tc_redesign
session_close: 2026-04-14
phase: COMPLETE
status: CLOSED
last_stage: sim_validated_20_20_tests
next_action:
  skill: confirm_with_jordan
design_docs_produced:
  - faction_layer_v30.md
  - faction_layer_v30_infill.md
  - military_layer_v30.md
  - tc_political_redesign_v30.md
sim_file: /home/claude/valoria_sim.py
sim_tests: 20/20_passing
sim_results_bg: TC_THEOCRACY_53pct CROWN_TREATY_14pct TIMEOUT_32pct avg_13.3y
sim_results_hybrid: TC_THEOCRACY_45pct CROWN_TREATY_16pct TIMEOUT_39pct avg_14.5y
crown_collapse_rate: 3.4pct
hafenmark_collapse_rate: 27.8pct
patches_proposed:
  - PP_402_REPEALED
  - PP_403_REPEALED_except_Suppress_exception
  - TC_runs_0_to_100_no_freeze
  - unit_cap_Military_times_2_plus_3
  - BG_battle_pool_sum_Martial_plus_commander_bonus
  - Spiritual_Weight_per_territory
  - Conditional_TC_passive
  - Church_TC_political_legitimacy_bonus
gaps_next_session:
  - territory_Prosperity_not_seeded
  - Lowenritter_post_coup_AI
  - Varfell_VTM_path
  - Parish_Cathedral_upgrades
  - Hafenmark_RDT_TD_tracks
  - ED_NEW_TC_10_church_victory_threshold
  - ED_NEW_TC_11_seizure_ob_post_milestone
  - all_docs_pending_PP_numbers
blockers: []
