# REPO RESTRUCTURE LEDGER
# Generated: 2026-04-18
# Status: ECOSYSTEM FILES UPDATED — file moves pending
#
# This ledger tracks every path change for the restructure.
# Phase 1: Ecosystem file path updates (this commit)
# Phase 2: File moves (subsequent commits)
#
# Ecosystem files updated in Phase 1:
#   references/canonical_sources.yaml — 47 path replacements
#   references/design_registry.yaml — 61 path replacements
#   references/atomization_rules.yaml — pattern replacements
#   references/splits/params_board_game_split.yaml — 18 path replacements
#   references/propagation_map.md — pattern replacements
#   skills/valoria-orchestrator/scripts/github_ops.py — session_log_archive → archives/session/
#   skills/valoria-orchestrator/scripts/valoria_hooks.py — CANON_DIRS, test paths
#   tools/ci_co_file_checker.py — test paths, params paths
#   tools/ci_editorial_checker.py — setting→world, gm_ref path
#   tools/patch_propagation_checker.py — params paths
#   skills/valoria-arc-generator/SKILL.md — params, gm_ref paths
#   skills/valoria-atomizer/SKILL.md — design doc paths
#   skills/valoria-combat-simulator/SKILL.md — params paths
#   skills/valoria-dice-model/SKILL.md — params paths
#   skills/valoria-orchestrator/SKILL.md — params paths
#   skills/valoria-simulator/SKILL.md — params, design paths

## MOVES (470 files)

| Old Path | New Path | Status |
|----------|----------|--------|
| `canon/audit_threadwork_v24_deprecated.md` | `tests/audit/audit_threadwork_v24_deprecated.md` | PENDING |
| `canon/audit_threadwork_v25.md` | `tests/audit/audit_threadwork_v25.md` | PENDING |
| `canon/editorial_ledger_archive_001_200.yaml` | `archives/editorials/editorial_ledger_archive_001_200.yaml` | PENDING |
| `canon/editorial_ledger_archive_1001_1200.yaml` | `archives/editorials/editorial_ledger_archive_1001_1200.yaml` | PENDING |
| `canon/editorial_ledger_archive_201_400.yaml` | `archives/editorials/editorial_ledger_archive_201_400.yaml` | PENDING |
| `canon/editorial_ledger_archive_401_600.yaml` | `archives/editorials/editorial_ledger_archive_401_600.yaml` | PENDING |
| `canon/editorial_ledger_archive_601_800.yaml` | `archives/editorials/editorial_ledger_archive_601_800.yaml` | PENDING |
| `canon/editorial_ledger_archive_801_1000.yaml` | `archives/editorials/editorial_ledger_archive_801_1000.yaml` | PENDING |
| `canon/patch_register_archive_001_200.yaml` | `archives/patches/patch_register_archive_001_200.yaml` | PENDING |
| `canon/patch_register_archive_1001_1200.yaml` | `archives/patches/patch_register_archive_1001_1200.yaml` | PENDING |
| `canon/patch_register_archive_1201_1400.yaml` | `archives/patches/patch_register_archive_1201_1400.yaml` | PENDING |
| `canon/patch_register_archive_1401_1600.yaml` | `archives/patches/patch_register_archive_1401_1600.yaml` | PENDING |
| `canon/patch_register_archive_1601_1800.yaml` | `archives/patches/patch_register_archive_1601_1800.yaml` | PENDING |
| `canon/patch_register_archive_201_400.yaml` | `archives/patches/patch_register_archive_201_400.yaml` | PENDING |
| `canon/patch_register_archive_401_600.yaml` | `archives/patches/patch_register_archive_401_600.yaml` | PENDING |
| `canon/patch_register_archive_601_800.yaml` | `archives/patches/patch_register_archive_601_800.yaml` | PENDING |
| `canon/patch_register_archive_801_1000.yaml` | `archives/patches/patch_register_archive_801_1000.yaml` | PENDING |
| `canon/patch_register_index_archive.md` | `archives/patches/patch_register_index_archive.md` | PENDING |
| `compilation/README.md` | `deprecated/compilation/README.md` | PENDING |
| `compilation/v0.14/README.md` | `deprecated/compilation/v0.14/README.md` | PENDING |
| `compilation/v0.14/stage10_advancement_deprecated.md` | `deprecated/compilation/v0.14/stage10_advancement_deprecated.md` | PENDING |
| `compilation/v0.14/stage11_scale_transitions_deprecated.md` | `deprecated/compilation/v0.14/stage11_scale_transitions_deprecated.md` | PENDING |
| `compilation/v0.14/stage12_campaign_modes_deprecated.md` | `deprecated/compilation/v0.14/stage12_campaign_modes_deprecated.md` | PENDING |
| `compilation/v0.14/stage13_npcs_deprecated.md` | `deprecated/compilation/v0.14/stage13_npcs_deprecated.md` | PENDING |
| `compilation/v0.14/stage14_gm_tools_deprecated.md` | `deprecated/compilation/v0.14/stage14_gm_tools_deprecated.md` | PENDING |
| `compilation/v0.14/stage15_spell_catalog_deprecated.md` | `deprecated/compilation/v0.14/stage15_spell_catalog_deprecated.md` | PENDING |
| `compilation/v0.14/stage16_reference_deprecated.md` | `deprecated/compilation/v0.14/stage16_reference_deprecated.md` | PENDING |
| `compilation/v0.14/stage17_canon_guard_deprecated.md` | `deprecated/compilation/v0.14/stage17_canon_guard_deprecated.md` | PENDING |
| `compilation/v0.14/stage1_core_engine_deprecated.md` | `deprecated/compilation/v0.14/stage1_core_engine_deprecated.md` | PENDING |
| `compilation/v0.14/stage2_characters_deprecated.md` | `deprecated/compilation/v0.14/stage2_characters_deprecated.md` | PENDING |
| `compilation/v0.14/stage3_compilation_report_deprecated.md` | `deprecated/compilation/v0.14/stage3_compilation_report_deprecated.md` | PENDING |
| `compilation/v0.14/stage3_thread_operations_deprecated.md` | `deprecated/compilation/v0.14/stage3_thread_operations_deprecated.md` | PENDING |
| `compilation/v0.14/stage4_southernmost_deprecated.md` | `deprecated/compilation/v0.14/stage4_southernmost_deprecated.md` | PENDING |
| `compilation/v0.14/stage5_clocks_deprecated.md` | `deprecated/compilation/v0.14/stage5_clocks_deprecated.md` | PENDING |
| `compilation/v0.14/stage6_factions_deprecated.md` | `deprecated/compilation/v0.14/stage6_factions_deprecated.md` | PENDING |
| `compilation/v0.14/stage7_territories_deprecated.md` | `deprecated/compilation/v0.14/stage7_territories_deprecated.md` | PENDING |
| `compilation/v0.14/stage8_combat_deprecated.md` | `deprecated/compilation/v0.14/stage8_combat_deprecated.md` | PENDING |
| `compilation/v0.14/stage9_social_deprecated.md` | `deprecated/compilation/v0.14/stage9_social_deprecated.md` | PENDING |
| `compilation/v0.14/stage_bg_board_game_mode_deprecated.md` | `deprecated/compilation/v0.14/stage_bg_board_game_mode_deprecated.md` | PENDING |
| `compilation/v0.14/valoria_ruleset_v0.14_deprecated.md` | `deprecated/compilation/v0.14/valoria_ruleset_v0.14_deprecated.md` | PENDING |
| `designs/audit/bridge_part1_revisions_2026-04-16.md` | `designs/audit/bridge_part1_revisions.md` | PENDING |
| `designs/board_game/board_game_v30.md` | `designs/provincial/strategic_layer_v30.md` | PENDING |
| `designs/board_game/board_game_v30_infill.md` | `designs/provincial/strategic_layer_v30_infill.md` | PENDING |
| `designs/board_game/board_game_v30_skeleton.md` | `designs/provincial/strategic_layer_v30_skeleton.md` | PENDING |
| `designs/board_game/faction_layer_v30.md` | `designs/provincial/faction_layer_v30.md` | PENDING |
| `designs/board_game/faction_layer_v30_infill.md` | `designs/provincial/faction_layer_v30_infill.md` | PENDING |
| `designs/board_game/faction_layer_v30_skeleton.md` | `designs/provincial/faction_layer_v30_skeleton.md` | PENDING |
| `designs/board_game/fail_forward_pp177_2026-04-02.md` | `designs/provincial/fail_forward_pp177.md` | PENDING |
| `designs/board_game/military_layer_v30.md` | `deprecated/designs/board_game/military_layer_v30.md` | PENDING |
| `designs/board_game/peninsular_strain_v1.md` | `designs/provincial/peninsular_strain_v30.md` | PENDING |
| `designs/board_game/peninsular_strain_v1_skeleton.md` | `designs/provincial/peninsular_strain_v30_skeleton.md` | PENDING |
| `designs/board_game/tc_political_redesign_v30.md` | `deprecated/designs/board_game/tc_political_redesign_v30.md` | PENDING |
| `designs/board_game/valoria_map_v2.svg` | `designs/provincial/valoria_map_v2.svg` | PENDING |
| `designs/board_game/varfell_path_b_v30.md` | `designs/provincial/varfell_path_b_v30.md` | PENDING |
| `designs/board_game/varfell_path_b_v30_infill.md` | `designs/provincial/varfell_path_b_v30_infill.md` | PENDING |
| `designs/board_game/victory_v30.md` | `designs/provincial/victory_v30.md` | PENDING |
| `designs/board_game/victory_v30_infill.md` | `designs/provincial/victory_v30_infill.md` | PENDING |
| `designs/board_game/victory_v30_skeleton.md` | `designs/provincial/victory_v30_skeleton.md` | PENDING |
| `designs/characters/character_histories_v30.md` | `systems/world/character_histories_v30.md` | PENDING |
| `designs/characters/character_histories_v30_infill.md` | `systems/world/character_histories_v30_infill.md` | PENDING |
| `designs/characters/character_histories_v30_skeleton.md` | `systems/world/character_histories_v30_skeleton.md` | PENDING |
| `designs/combat/combat_design_v1.md` | `designs/scene/combat_design_v1.md` | PENDING |
| `designs/combat/combat_design_v1_skeleton.md` | `designs/scene/combat_design_v1_skeleton.md` | PENDING |
| `designs/combat/combat_v30.md` | `designs/scene/combat_v30.md` | PENDING |
| `designs/combat/combat_v30_infill.md` | `designs/scene/combat_v30_infill.md` | PENDING |
| `designs/combat/combat_v30_skeleton.md` | `designs/scene/combat_v30_skeleton.md` | PENDING |
| `designs/contest/social_contest_system_v2.md` | `designs/scene/social_contest_system_v2.md` | PENDING |
| `designs/contest/social_contest_system_v2_skeleton.md` | `designs/scene/social_contest_system_v2_skeleton.md` | PENDING |
| `designs/contest/social_contest_v30.md` | `designs/scene/social_contest_v30.md` | PENDING |
| `designs/contest/social_contest_v30_infill.md` | `designs/scene/social_contest_v30_infill.md` | PENDING |
| `designs/contest/social_contest_v30_skeleton.md` | `designs/scene/social_contest_v30_skeleton.md` | PENDING |
| `designs/conviction_track/conviction_track_v30.md` | `designs/scene/conviction_track_v30.md` | PENDING |
| `designs/conviction_track/conviction_track_v30_infill.md` | `designs/scene/conviction_track_v30_infill.md` | PENDING |
| `designs/conviction_track/conviction_track_v30_skeleton.md` | `designs/scene/conviction_track_v30_skeleton.md` | PENDING |
| `designs/fieldwork/fieldwork_bg_v30.md` | `systems/fieldwork/fieldwork_bg_v30.md` | PENDING |
| `designs/fieldwork/fieldwork_bg_v30_infill.md` | `systems/fieldwork/fieldwork_bg_v30_infill.md` | PENDING |
| `designs/fieldwork/fieldwork_editorial.md` | `systems/fieldwork/fieldwork_editorial.md` | PENDING |
| `designs/fieldwork/fieldwork_exploration.md` | `systems/fieldwork/fieldwork_exploration.md` | PENDING |
| `designs/fieldwork/fieldwork_exposure.md` | `systems/fieldwork/fieldwork_exposure.md` | PENDING |
| `designs/fieldwork/fieldwork_godot.md` | `systems/fieldwork/fieldwork_godot.md` | PENDING |
| `designs/fieldwork/fieldwork_hybrid_v30.md` | `systems/fieldwork/fieldwork_hybrid_v30.md` | PENDING |
| `designs/fieldwork/fieldwork_hybrid_v30_infill.md` | `systems/fieldwork/fieldwork_hybrid_v30_infill.md` | PENDING |
| `designs/fieldwork/fieldwork_investigation.md` | `systems/fieldwork/fieldwork_investigation.md` | PENDING |
| `designs/fieldwork/fieldwork_rationale.md` | `systems/fieldwork/fieldwork_rationale.md` | PENDING |
| `designs/fieldwork/fieldwork_socializing.md` | `systems/fieldwork/fieldwork_socializing.md` | PENDING |
| `designs/fieldwork/fieldwork_summary.md` | `systems/fieldwork/fieldwork_summary.md` | PENDING |
| `designs/fieldwork/fieldwork_v30.md` | `systems/fieldwork/fieldwork_v30.md` | PENDING |
| `designs/fieldwork/fieldwork_v30_infill.md` | `systems/fieldwork/fieldwork_v30_infill.md` | PENDING |
| `designs/fieldwork/fieldwork_v30_skeleton.md` | `designs/scene/fieldwork_v30_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/README.md` | `designs/arcs/README.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_16_19_faction_domain_echoes.md` | `designs/arcs/arcs_16_19.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_16_19_faction_domain_echoes_skeleton.md` | `designs/arcs/arcs_16_19_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_20_23_branching.md` | `designs/arcs/arcs_20_23.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_20_23_branching_skeleton.md` | `designs/arcs/arcs_20_23_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_24_27_branching.md` | `designs/arcs/arcs_24_27.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_24_27_branching_skeleton.md` | `designs/arcs/arcs_24_27_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_28_30_coherence_zero.md` | `designs/arcs/arcs_28_30.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_28_30_coherence_zero_skeleton.md` | `designs/arcs/arcs_28_30_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md` | `designs/arcs/arcs_31_35.md` | PENDING |
| `designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems_skeleton.md` | `designs/arcs/arcs_31_35_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/valoria_emergent_arcs_experimental.md` | `designs/arcs/emergent_arcs_experimental.md` | PENDING |
| `designs/gm_ref_cp14/arcs/valoria_emergent_arcs_experimental_skeleton.md` | `designs/arcs/emergent_arcs_experimental_skeleton.md` | PENDING |
| `designs/gm_ref_cp14/arcs/valoria_emergent_campaign_arcs.md` | `designs/arcs/emergent_campaign_arcs.md` | PENDING |
| `designs/hybrid/hybrid_gaps_v30.md` | `systems/_architecture/hybrid_gaps_v30.md` | PENDING |
| `designs/hybrid/hybrid_gaps_v30_infill.md` | `systems/_architecture/hybrid_gaps_v30_infill.md` | PENDING |
| `designs/hybrid/scale_transitions_v30.md` | `systems/_architecture/scale_transitions_v30.md` | PENDING |
| `designs/hybrid/scale_transitions_v30_infill.md` | `systems/_architecture/scale_transitions_v30_infill.md` | PENDING |
| `designs/hybrid/scale_transitions_v30_skeleton.md` | `systems/_architecture/scale_transitions_v30_skeleton.md` | PENDING |
| `designs/mass_combat/mass_battle_v30.md` | `designs/provincial/mass_battle_v30.md` | PENDING |
| `designs/mass_combat/mass_battle_v30_infill.md` | `designs/provincial/mass_battle_v30_infill.md` | PENDING |
| `designs/mass_combat/mass_battle_v30_skeleton.md` | `designs/provincial/mass_battle_v30_skeleton.md` | PENDING |
| `designs/mechanics/baralta_crown_claim_v30.md` | `designs/provincial/baralta_crown_claim_v30.md` | PENDING |
| `designs/mechanics/baralta_crown_claim_v30_infill.md` | `designs/provincial/baralta_crown_claim_v30_infill.md` | PENDING |
| `designs/setting/adjacency_map.jsx` | `systems/world/adjacency_map.jsx` | PENDING |
| `designs/setting/calamity_radiation_v30.md` | `systems/world/calamity_radiation_v30.md` | PENDING |
| `designs/setting/calamity_radiation_v30_infill.md` | `systems/world/calamity_radiation_v30_infill.md` | PENDING |
| `designs/setting/geography_v30.md` | `systems/world/geography_v30.md` | PENDING |
| `designs/setting/geography_v30_infill.md` | `systems/world/geography_v30_infill.md` | PENDING |
| `designs/setting/southernmost_v30.md` | `systems/world/southernmost_v30.md` | PENDING |
| `designs/setting/southernmost_v30_infill.md` | `systems/world/southernmost_v30_infill.md` | PENDING |
| `designs/systems/arc_expansion_v1_2026-04-16.md` | `designs/arcs/arc_expansion_v30.md` | PENDING |
| `designs/systems/arc_expansion_v1_2026-04-16_skeleton.md` | `designs/arcs/arc_expansion_v30_skeleton.md` | PENDING |
| `designs/systems/campaign_architecture_v1.md` | `systems/_architecture/campaign_architecture_v30.md` | PENDING |
| `designs/systems/campaign_modes_v30.md` | `systems/_architecture/campaign_modes_v30.md` | PENDING |
| `designs/systems/campaign_modes_v30_infill.md` | `systems/_architecture/campaign_modes_v30_infill.md` | PENDING |
| `designs/systems/canonical_registry_r2_2026-04-15.md` | `systems/_architecture/canonical_registry.md` | PENDING |
| `designs/systems/clock_registry_v30.md` | `designs/provincial/clock_registry_v30.md` | PENDING |
| `designs/systems/clock_registry_v30_infill.md` | `designs/provincial/clock_registry_v30_infill.md` | PENDING |
| `designs/systems/cogload_moderate_target.md` | `systems/_architecture/cogload_moderate_target.md` | PENDING |
| `designs/systems/companion_app_design_note_2026-04-04.md` | `systems/_architecture/companion_app_design_note.md` | PENDING |
| `designs/systems/companion_specification_v30.md` | `systems/npcs/companion_specification_v30.md` | PENDING |
| `designs/systems/complete_systems_reference_r2_2026-04-15.md` | `systems/_architecture/complete_systems_reference.md` | PENDING |
| `designs/systems/derived_stats_v1.md` | `designs/scene/derived_stats_v30.md` | PENDING |
| `designs/systems/derived_stats_v1_skeleton.md` | `designs/scene/derived_stats_v30_skeleton.md` | PENDING |
| `designs/systems/faction_politics_expanded_v1.md` | `designs/provincial/faction_politics_v30.md` | DONE (2026-07-08, ED-IN-0016 — file move already complete, old path long gone; citation-repointing half executed this pass across the live corpus) |
| `designs/systems/faction_politics_expanded_v1_skeleton.md` | `designs/provincial/faction_politics_v30_skeleton.md` | N/A (2026-07-08, ED-IN-0016 — not executed: `faction_politics_v30.md` was promoted as a single monolithic doc; no index/skeleton split was ever authored for it, confirmed no such file exists) |
| `designs/systems/integration_proposal_2026-04-15.md` | `systems/_architecture/integration_proposal_v30.md` | PENDING |
| `designs/systems/integration_proposal_2026-04-15_skeleton.md` | `systems/_architecture/integration_proposal_v30_skeleton.md` | PENDING |
| `designs/systems/investigation_systems_proposal_2026-04-15.md` | `systems/fieldwork/investigation_systems_v30.md` | PENDING |
| `designs/systems/investigation_systems_proposal_2026-04-15_skeleton.md` | `designs/scene/investigation_systems_v30_skeleton.md` | PENDING |
| `designs/systems/military_layer_v30.md` | `designs/provincial/military_layer_v30.md` | PENDING |
| `designs/systems/military_layer_v30_skeleton.md` | `designs/provincial/military_layer_v30_skeleton.md` | PENDING |
| `designs/systems/npc_behavior_system_v1.md` | `systems/npcs/npc_behavior_system_v1.md` | PENDING |
| `designs/systems/npc_behavior_system_v1_skeleton.md` | `systems/npcs/npc_behavior_system_v1_skeleton.md` | PENDING |
| `designs/systems/npc_behavior_v30.md` | `systems/npcs/npc_behavior_v30.md` | PENDING |
| `designs/systems/npc_behavior_v30_infill.md` | `systems/npcs/npc_behavior_v30_infill.md` | PENDING |
| `designs/systems/npc_behavior_v30_skeleton.md` | `systems/npcs/npc_behavior_v30_skeleton.md` | PENDING |
| `designs/systems/player_agency_v30.md` | `systems/_architecture/player_agency_v30.md` | PENDING |
| `designs/systems/player_agency_v30_skeleton.md` | `systems/_architecture/player_agency_v30_skeleton.md` | PENDING |
| `designs/systems/settlement_layer_v30.md` | `systems/settlements/settlement_layer_v30.md` | PENDING |
| `designs/systems/settlement_layer_v30_skeleton.md` | `systems/settlements/settlement_layer_v30_skeleton.md` | PENDING |
| `designs/systems/tc_political_redesign_v30.md` | `designs/provincial/tc_political_v30.md` | PENDING |
| `designs/systems/tc_political_redesign_v30_skeleton.md` | `designs/provincial/tc_political_v30_skeleton.md` | PENDING |
| `designs/systems/thread_horizontal_integration_spec.md` | `systems/threadwork/thread_horizontal_integration_spec.md` | PENDING |
| `designs/systems/throughline_resolutions_v1.md` | `designs/arcs/throughline_resolutions_v30.md` | PENDING |
| `designs/systems/throughline_resolutions_v1_skeleton.md` | `designs/arcs/throughline_resolutions_v30_skeleton.md` | PENDING |
| `designs/ttrpg/edeyja_npc.md` | `systems/npcs/edeyja_npc.md` | PENDING |
| `designs/ttrpg/factions_ttrpg_v30.md` | `designs/provincial/factions_personal_v30.md` | PENDING |
| `designs/ttrpg/factions_ttrpg_v30_infill.md` | `designs/provincial/factions_personal_v30_infill.md` | PENDING |
| `designs/ttrpg/factions_ttrpg_v30_skeleton.md` | `designs/provincial/factions_personal_v30_skeleton.md` | PENDING |
| `designs/ttrpg/threadwork_philosophical_reference_v30.md` | `systems/threadwork/threadwork_philosophical_reference_v30.md` | PENDING |
| `designs/ttrpg/threadwork_philosophical_reference_v30_infill.md` | `systems/threadwork/threadwork_philosophical_reference_v30_infill.md` | PENDING |
| `designs/ttrpg/threadwork_redesign_v25.md` | `systems/threadwork/threadwork_v25_historical.md` | PENDING |
| `designs/ttrpg/threadwork_redesign_v25_skeleton.md` | `systems/threadwork/threadwork_v25_historical_skeleton.md` | PENDING |
| `designs/ttrpg/threadwork_v30.md` | `systems/threadwork/threadwork_v30.md` | PENDING |
| `designs/ttrpg/threadwork_v30_infill.md` | `systems/threadwork/threadwork_v30_infill.md` | PENDING |
| `designs/ttrpg/threadwork_v30_skeleton.md` | `systems/threadwork/threadwork_v30_skeleton.md` | PENDING |
| `designs/ttrpg/valoria_emergent_scenarios.md` | `designs/arcs/emergent_scenarios.md` | PENDING |
| `designs/ttrpg/valoria_emergent_scenarios_skeleton.md` | `designs/arcs/emergent_scenarios_skeleton.md` | PENDING |
| `designs/ttrpg/valoria_narrative_scenario_chains.md` | `designs/arcs/narrative_scenario_chains.md` | PENDING |
| `designs/ttrpg/valoria_narrative_scenario_chains_skeleton.md` | `designs/arcs/narrative_scenario_chains_skeleton.md` | PENDING |
| `designs/worldbuilding/worldbuilding_canon_audit_v30.md` | `systems/world/worldbuilding_canon_audit_v30.md` | PENDING |
| `designs/worldbuilding/worldbuilding_canon_audit_v30_infill.md` | `systems/world/worldbuilding_canon_audit_v30_infill.md` | PENDING |
| `designs/worldbuilding/worldbuilding_v30.md` | `systems/world/worldbuilding_v30.md` | PENDING |
| `designs/worldbuilding/worldbuilding_v30_infill.md` | `systems/world/worldbuilding_v30_infill.md` | PENDING |
| `gm_ref/README.md` | `designs/arcs/gm_ref/README.md` | PENDING |
| `gm_ref/arc_narrative_analysis.md` | `designs/arcs/gm_ref/arc_narrative_analysis.md` | PENDING |
| `gm_ref/arcs_01_04_nongreedy.md` | `designs/arcs/gm_ref/arcs_01_04.md` | PENDING |
| `gm_ref/arcs_05_09_batch02.md` | `designs/arcs/gm_ref/arcs_05_09.md` | PENDING |
| `gm_ref/arcs_10_18_consolidated.md` | `designs/arcs/gm_ref/arcs_10_18.md` | PENDING |
| `gm_ref/arcs_36_40_interdependent.md` | `designs/arcs/gm_ref/arcs_36_40.md` | PENDING |
| `gm_ref/arcs_41_45_interdependent.md` | `designs/arcs/gm_ref/arcs_41_45.md` | PENDING |
| `gm_ref/arcs_46_55_consolidated.md` | `designs/arcs/gm_ref/arcs_46_55.md` | PENDING |
| `gm_ref/arcs_46_55_resolved.md` | `designs/arcs/gm_ref/arcs_46_55_resolved.md` | PENDING |
| `references/audit/throughlines_transitions_hierarchy_2026-04-18.md` | `designs/audit/throughlines_transitions_hierarchy.md` | PENDING |
| `references/audit/valoria_complete_system_audit_2026-04-18.md` | `designs/audit/valoria_complete_system_audit.md` | PENDING |
| `references/audit/valoria_workplan_final_2026-04-18.md` | `designs/audit/valoria_workplan_final.md` | PENDING |
| `references/historical_precedents_analysis.md` | `references/historical/precedents_analysis.md` | PENDING |
| `references/historical_precedents_warfare.md` | `references/historical/precedents_warfare.md` | PENDING |
| `references/params_bg_clocks.md` | `params/bg/clocks.md` | PENDING |
| `references/params_bg_core.md` | `params/bg/core.md` | PENDING |
| `references/params_bg_ed_resolutions.md` | `params/bg/ed_resolutions.md` | PENDING |
| `references/params_bg_faction_actions.md` | `params/bg/faction_actions.md` | PENDING |
| `references/params_bg_geography.md` | `params/bg/geography.md` | PENDING |
| `references/params_bg_institutions.md` | `params/bg/institutions.md` | PENDING |
| `references/params_bg_military.md` | `params/bg/military.md` | PENDING |
| `references/params_bg_ministry.md` | `params/bg/ministry.md` | PENDING |
| `references/params_bg_npc_priority_trees.md` | `params/bg/npc_priority_trees.md` | PENDING |
| `references/params_bg_npcs_special.md` | `params/bg/npcs_special.md` | PENDING |
| `references/params_bg_parliament.md` | `params/bg/parliament.md` | PENDING |
| `references/params_bg_phases.md` | `params/bg/phases.md` | PENDING |
| `references/params_bg_stress_patches.md` | `params/bg/stress_patches.md` | PENDING |
| `references/params_bg_tc_seizure.md` | `params/bg/tc_seizure.md` | PENDING |
| `references/params_bg_tracks.md` | `params/bg/tracks.md` | PENDING |
| `references/params_bg_victory.md` | `params/bg/victory.md` | PENDING |
| `references/params_board_game.md` | `params/board_game.md` | PENDING |
| `references/params_board_game_history.md` | `params/history/board_game.md` | PENDING |
| `references/params_board_game_misc.md` | `params/board_game_misc.md` | PENDING |
| `references/params_campaign_modes.md` | `params/campaign_modes.md` | PENDING |
| `references/params_campaign_modes_history.md` | `params/history/campaign_modes.md` | PENDING |
| `references/params_combat.md` | `params/combat.md` | PENDING |
| `references/params_combat_history.md` | `params/history/combat.md` | PENDING |
| `references/params_contest.md` | `params/contest.md` | PENDING |
| `references/params_core.md` | `params/core.md` | PENDING |
| `references/params_core_history.md` | `params/history/core.md` | PENDING |
| `references/params_factions.md` | `params/factions.md` | PENDING |
| `references/params_factions_ed_006_resolution_pp_287_riskbreakers_identity_fla.md` | `params/factions/riskbreakers_identity.md` | PENDING |
| `references/params_factions_npc_stance_triangles_pp_new_from_npc_behavior_syst.md` | `params/factions/npc_stance_triangles.md` | PENDING |
| `references/params_factions_stats_1_7_scale.md` | `params/factions/stats_1_7_scale.md` | PENDING |
| `references/params_factions_ttrpg.md` | `params/factions_personal.md` | PENDING |
| `references/params_factions_ttrpg_history.md` | `params/history/factions_personal.md` | PENDING |
| `references/params_fieldwork.md` | `params/fieldwork.md` | PENDING |
| `references/params_mass_combat.md` | `params/mass_combat.md` | PENDING |
| `references/params_mass_combat_history.md` | `params/history/mass_combat.md` | PENDING |
| `references/params_scale_transitions.md` | `params/scale_transitions.md` | PENDING |
| `references/params_southernmost.md` | `params/southernmost.md` | PENDING |
| `references/params_southernmost_history.md` | `params/history/southernmost.md` | PENDING |
| `references/params_threadwork.md` | `params/threadwork.md` | PENDING |
| `references/params_threadwork_history.md` | `params/history/threadwork.md` | PENDING |
| `references/params_threadwork_superseded.md` | `params/threadwork_superseded.md` | PENDING |
| `references/sim_decision_protocols.md` | `tests/sim/sim_decision_protocols.md` | PENDING |
| `references/videogame_mode_spec.md` | `systems/_architecture/videogame_mode_spec.md` | PENDING |
| `session_log_archive_part_1.md` | `archives/session/session_log_archive_part_1.md` | PENDING |
| `session_log_archive_part_2.md` | `archives/session/session_log_archive_part_2.md` | PENDING |
| `session_log_archive_part_3.md` | `archives/session/session_log_archive_part_3.md` | PENDING |
| `session_log_archive_part_4.md` | `archives/session/session_log_archive_part_4.md` | PENDING |
| `session_log_archive_part_5.md` | `archives/session/session_log_archive_part_5.md` | PENDING |
| `session_log_archive_part_6.md` | `archives/session/session_log_archive_part_6.md` | PENDING |
| `session_log_archive_part_7.md` | `archives/session/session_log_archive_part_7.md` | PENDING |
| `tests/arc_branch_simulation.md` | `tests/sim/arc_branch_simulation.md` | PENDING |
| `tests/aud_bg_01.md` | `tests/audit/aud_bg_01.md` | PENDING |
| `tests/aud_bg_02_03.md` | `tests/audit/aud_bg_02_03.md` | PENDING |
| `tests/aud_ttrpg_01.md` | `tests/audit/aud_ttrpg_01.md` | PENDING |
| `tests/aud_tw_001_threadwork_audit.md` | `tests/audit/aud_tw_001_threadwork_audit.md` | PENDING |
| `tests/audit_combat_2026-04-02.md` | `tests/audit/audit_combat_2026-04-02.md` | PENDING |
| `tests/audit_cross_system_2026_04_06.md` | `tests/audit/audit_cross_system_2026_04_06.md` | PENDING |
| `tests/audit_d02_sim_d05.md` | `tests/audit/audit_d02_sim_d05.md` | PENDING |
| `tests/audit_debate_a_g.md` | `tests/audit/audit_debate_a_g.md` | PENDING |
| `tests/audit_graduated_seizure_AUDIT-GS-01.md` | `tests/audit/audit_graduated_seizure_AUDIT-GS-01.md` | PENDING |
| `tests/audit_hybrid_01.md` | `tests/audit/audit_hybrid_01.md` | PENDING |
| `tests/audit_npc_behavior_system.md` | `tests/audit/audit_npc_behavior_system.md` | PENDING |
| `tests/audit_phase1_params_crosssystem.md` | `tests/audit/audit_phase1_params_crosssystem.md` | PENDING |
| `tests/audit_phase2_canonical_docs.md` | `tests/audit/audit_phase2_canonical_docs.md` | PENDING |
| `tests/audit_phase3_crossmode_cogload.md` | `tests/audit/audit_phase3_crossmode_cogload.md` | PENDING |
| `tests/audit_phase3_remaining_systems.md` | `tests/audit/audit_phase3_remaining_systems.md` | PENDING |
| `tests/audit_sim_social_contest.md` | `tests/audit/audit_sim_social_contest.md` | PENDING |
| `tests/audit_victory_architecture_v1.md` | `tests/audit/audit_victory_architecture_v1.md` | PENDING |
| `tests/bal_bg_02.md` | `tests/sim/bal_bg_02.md` | PENDING |
| `tests/commit_test.md` | `tests/misc/commit_test.md` | PENDING |
| `tests/delay_vs_preclusion_evaluation.md` | `tests/audit/delay_vs_preclusion_evaluation.md` | PENDING |
| `tests/editorial_resolution_pass.md` | `tests/audit/editorial_resolution_pass.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch2.md` | `tests/stress/emergent_arc_2026-04-17_batch2.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch3_with_audit.md` | `tests/stress/emergent_arc_2026-04-17_batch3_with_audit.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch4.md` | `tests/stress/emergent_arc_2026-04-17_batch4.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch5.md` | `tests/stress/emergent_arc_2026-04-17_batch5.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch6.md` | `tests/stress/emergent_arc_2026-04-17_batch6.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch7.md` | `tests/stress/emergent_arc_2026-04-17_batch7.md` | PENDING |
| `tests/emergent_arc_skeleton_test_2026-04-17_batch8_counterfactual.md` | `tests/stress/emergent_arc_2026-04-17_batch8_counterfactual.md` | PENDING |
| `tests/hook_test.md` | `tests/misc/hook_test.md` | PENDING |
| `tests/session_critical_review_2026-04-04.md` | `tests/audit/session_critical_review.md` | PENDING |
| `tests/sim_alternate_branches2_2026-04-17.md` | `tests/sim/sim_alternate_branches2_2026-04-17.md` | PENDING |
| `tests/sim_alternate_branches_2026-04-17.md` | `tests/sim/sim_alternate_branches_2026-04-17.md` | PENDING |
| `tests/sim_arc_01_irrational_player_arcs.md` | `tests/sim/sim_arc_01_irrational_player_arcs.md` | PENDING |
| `tests/sim_arc_02_nongreedy_player_arcs.md` | `tests/sim/sim_arc_02_nongreedy_player_arcs.md` | PENDING |
| `tests/sim_arc_03_new_nongreedy_arcs.md` | `tests/sim/sim_arc_03_new_nongreedy_arcs.md` | PENDING |
| `tests/sim_arc_04_structural_misreaders.md` | `tests/sim/sim_arc_04_structural_misreaders.md` | PENDING |
| `tests/sim_arc_a01_baralta_programme.md` | `tests/sim/sim_arc_a01_baralta_programme.md` | PENDING |
| `tests/sim_arc_b01_tc_fracture.md` | `tests/sim/sim_arc_b01_tc_fracture.md` | PENDING |
| `tests/sim_arc_b02_season8_constraint.md` | `tests/sim/sim_arc_b02_season8_constraint.md` | PENDING |
| `tests/sim_arc_c01_vaynard_unchecked.md` | `tests/sim/sim_arc_c01_vaynard_unchecked.md` | PENDING |
| `tests/sim_arc_d01_southern_corridor.md` | `tests/sim/sim_arc_d01_southern_corridor.md` | PENDING |
| `tests/sim_arc_e01_rm_pressure.md` | `tests/sim/sim_arc_e01_rm_pressure.md` | PENDING |
| `tests/sim_arc_f01_economic_web.md` | `tests/sim/sim_arc_f01_economic_web.md` | PENDING |
| `tests/sim_arc_g01_g05_capitals.md` | `tests/sim/sim_arc_g01_g05_capitals.md` | PENDING |
| `tests/sim_arcs_36_45_batch.md` | `tests/sim/sim_arcs_36_45_batch.md` | PENDING |
| `tests/sim_batch_3_2026-04-16.md` | `tests/sim/sim_batch_3_2026-04-16.md` | PENDING |
| `tests/sim_batch_4_2026-04-16.md` | `tests/sim/sim_batch_4_2026-04-16.md` | PENDING |
| `tests/sim_batch_5_2026-04-16.md` | `tests/sim/sim_batch_5_2026-04-16.md` | PENDING |
| `tests/sim_batch_6_2026-04-16.md` | `tests/sim/sim_batch_6_2026-04-16.md` | PENDING |
| `tests/sim_batch_7_2026-04-16.md` | `tests/sim/sim_batch_7_2026-04-16.md` | PENDING |
| `tests/sim_batch_8_2026-04-17.md` | `tests/sim/sim_batch_8_2026-04-17.md` | PENDING |
| `tests/sim_bg_01.md` | `tests/sim/sim_bg_01.md` | PENDING |
| `tests/sim_bg_balance_01.md` | `tests/sim/sim_bg_balance_01.md` | PENDING |
| `tests/sim_bg_battle_thread_2026_04_08.md` | `tests/sim/sim_bg_battle_thread_2026_04_08.md` | PENDING |
| `tests/sim_bg_ff_01.md` | `tests/sim/sim_bg_ff_01.md` | PENDING |
| `tests/sim_bg_remaining_2026_04_08.md` | `tests/sim/sim_bg_remaining_2026_04_08.md` | PENDING |
| `tests/sim_cascade_01.md` | `tests/sim/sim_cascade_01.md` | PENDING |
| `tests/sim_combat_004.md` | `tests/sim/sim_combat_004.md` | PENDING |
| `tests/sim_combat_batch_11.md` | `tests/sim/sim_combat_batch_11.md` | PENDING |
| `tests/sim_combat_exhaustive.py` | `tests/sim/sim_combat_exhaustive.py` | PENDING |
| `tests/sim_combat_group.py` | `tests/sim/sim_combat_group.py` | PENDING |
| `tests/sim_combat_rescue.py` | `tests/sim/sim_combat_rescue.py` | PENDING |
| `tests/sim_combat_tieup.py` | `tests/sim/sim_combat_tieup.py` | PENDING |
| `tests/sim_combat_v11.py` | `tests/sim/sim_combat_v11.py` | PENDING |
| `tests/sim_comp01_season8.md` | `tests/sim/sim_comp01_season8.md` | PENDING |
| `tests/sim_comp02_season9.md` | `tests/sim/sim_comp02_season9.md` | PENDING |
| `tests/sim_companions_2026-04-16.md` | `tests/sim/sim_companions_2026-04-16.md` | PENDING |
| `tests/sim_comprehensive_batch_2026_04_10.md` | `tests/sim/sim_comprehensive_batch_2026_04_10.md` | PENDING |
| `tests/sim_comprehensive_multisystem_2026_04_07.md` | `tests/sim/sim_comprehensive_multisystem_2026_04_07.md` | PENDING |
| `tests/sim_d05_debate_resim.md` | `tests/sim/sim_d05_debate_resim.md` | PENDING |
| `tests/sim_d06_social_contest_stress.md` | `tests/sim/sim_d06_social_contest_stress.md` | PENDING |
| `tests/sim_d_01_debate_stress_test.md` | `tests/sim/sim_d_01_debate_stress_test.md` | PENDING |
| `tests/sim_d_02_debate_scenario_c.md` | `tests/sim/sim_d_02_debate_scenario_c.md` | PENDING |
| `tests/sim_d_03_subsystem_k.md` | `tests/sim/sim_d_03_subsystem_k.md` | PENDING |
| `tests/sim_d_04_gap_fill_stress.md` | `tests/sim/sim_d_04_gap_fill_stress.md` | PENDING |
| `tests/sim_debate_stress_01.md` | `tests/sim/sim_debate_stress_01.md` | PENDING |
| `tests/sim_debt_03_04_contest_baselines.md` | `tests/sim/sim_debt_03_04_contest_baselines.md` | PENDING |
| `tests/sim_diplomacy_audit_patch.md` | `tests/sim/sim_diplomacy_audit_patch.md` | PENDING |
| `tests/sim_diplomacy_batch2.md` | `tests/sim/sim_diplomacy_batch2.md` | PENDING |
| `tests/sim_econ_01.md` | `tests/sim/sim_econ_01.md` | PENDING |
| `tests/sim_extended_threadwork.md` | `tests/sim/sim_extended_threadwork.md` | PENDING |
| `tests/sim_faction_ambition_2026-04-16.md` | `tests/sim/sim_faction_ambition_2026-04-16.md` | PENDING |
| `tests/sim_factions_stress_2026_04_13.md` | `tests/sim/sim_factions_stress_2026_04_13.md` | PENDING |
| `tests/sim_feint_rescue_mandate_batch.md` | `tests/sim/sim_feint_rescue_mandate_batch.md` | PENDING |
| `tests/sim_fieldwork_npc_char_2026_04_13.md` | `tests/sim/sim_fieldwork_npc_char_2026_04_13.md` | PENDING |
| `tests/sim_fieldwork_transitions.md` | `tests/sim/sim_fieldwork_transitions.md` | PENDING |
| `tests/sim_graduated_seizure_SIM-GS-01.md` | `tests/sim/sim_graduated_seizure_SIM-GS-01.md` | PENDING |
| `tests/sim_h01_hybrid_season6.md` | `tests/sim/sim_h01_hybrid_season6.md` | PENDING |
| `tests/sim_h01_to_h07_resolution_and_audit.md` | `tests/sim/sim_h01_to_h07_resolution_and_audit.md` | PENDING |
| `tests/sim_h08_to_h13_nongreedy_batch.md` | `tests/sim/sim_h08_to_h13_nongreedy_batch.md` | PENDING |
| `tests/sim_hyb_01_templar_crossing.md` | `tests/sim/sim_hyb_01_templar_crossing.md` | PENDING |
| `tests/sim_intensive_01.md` | `tests/sim/sim_intensive_01.md` | PENDING |
| `tests/sim_ixc_01_02_03.md` | `tests/sim/sim_ixc_01_02_03.md` | PENDING |
| `tests/sim_ixc_05_06_07.md` | `tests/sim/sim_ixc_05_06_07.md` | PENDING |
| `tests/sim_mass_battle_SIM-MB-01.md` | `tests/sim/sim_mass_battle_SIM-MB-01.md` | PENDING |
| `tests/sim_mass_battle_SIM-MB-02.md` | `tests/sim/sim_mass_battle_SIM-MB-02.md` | PENDING |
| `tests/sim_mass_battle_SIM-MB-03.md` | `tests/sim/sim_mass_battle_SIM-MB-03.md` | PENDING |
| `tests/sim_mass_battle_batch_11.md` | `tests/sim/sim_mass_battle_batch_11.md` | PENDING |
| `tests/sim_mass_combat_005.md` | `tests/sim/sim_mass_combat_005.md` | PENDING |
| `tests/sim_mending_coherence_2026-04-17.md` | `tests/sim/sim_mending_coherence_2026-04-17.md` | PENDING |
| `tests/sim_negotiations_alliances_treaties.md` | `tests/sim/sim_negotiations_alliances_treaties.md` | PENDING |
| `tests/sim_new_01_conviction_yield.md` | `tests/sim/sim_new_01_conviction_yield.md` | PENDING |
| `tests/sim_new_02_partition.md` | `tests/sim/sim_new_02_partition.md` | PENDING |
| `tests/sim_new_03_ip_crisis.md` | `tests/sim/sim_new_03_ip_crisis.md` | PENDING |
| `tests/sim_new_04_resistance_decay.md` | `tests/sim/sim_new_04_resistance_decay.md` | PENDING |
| `tests/sim_new_05_patience_protocol.md` | `tests/sim/sim_new_05_patience_protocol.md` | PENDING |
| `tests/sim_new_06_cultural_uprising.md` | `tests/sim/sim_new_06_cultural_uprising.md` | PENDING |
| `tests/sim_npc_01.py` | `tests/sim/sim_npc_01.py` | PENDING |
| `tests/sim_npc_01_results.md` | `tests/sim/sim_npc_01_results.md` | PENDING |
| `tests/sim_npc_as_player_2026-04-16.md` | `tests/sim/sim_npc_as_player_2026-04-16.md` | PENDING |
| `tests/sim_npc_player_batch2_2026-04-16.md` | `tests/sim/sim_npc_player_batch2_2026-04-16.md` | PENDING |
| `tests/sim_npc_player_batch3_2026-04-17.md` | `tests/sim/sim_npc_player_batch3_2026-04-17.md` | PENDING |
| `tests/sim_npc_player_batch4_2026-04-17.md` | `tests/sim/sim_npc_player_batch4_2026-04-17.md` | PENDING |
| `tests/sim_npc_player_batch5_2026-04-17.md` | `tests/sim/sim_npc_player_batch5_2026-04-17.md` | PENDING |
| `tests/sim_open_items_2026-04-16.md` | `tests/sim/sim_open_items_2026-04-16.md` | PENDING |
| `tests/sim_opposing_threadwork_final.md` | `tests/sim/sim_opposing_threadwork_final.md` | PENDING |
| `tests/sim_pp431_cor_retest.md` | `tests/sim/sim_pp431_cor_retest.md` | PENDING |
| `tests/sim_pp441_cor_retest.md` | `tests/sim/sim_pp441_cor_retest.md` | PENDING |
| `tests/sim_pp476_498.md` | `tests/sim/sim_pp476_498.md` | PENDING |
| `tests/sim_proj_01_projectile_categories.md` | `tests/sim/sim_proj_01_projectile_categories.md` | PENDING |
| `tests/sim_ranged_001.md` | `tests/sim/sim_ranged_001.md` | PENDING |
| `tests/sim_ranged_002_003.md` | `tests/sim/sim_ranged_002_003.md` | PENDING |
| `tests/sim_ranged_004_005_006.md` | `tests/sim/sim_ranged_004_005_006.md` | PENDING |
| `tests/sim_rescue_feint_partial_commit.md` | `tests/sim/sim_rescue_feint_partial_commit.md` | PENDING |
| `tests/sim_rescue_interconnected.md` | `tests/sim/sim_rescue_interconnected.md` | PENDING |
| `tests/sim_run22_brackets.md` | `tests/sim/sim_run22_brackets.md` | PENDING |
| `tests/sim_run22_report.md` | `tests/sim/sim_run22_report.md` | PENDING |
| `tests/sim_soc_01.md` | `tests/sim/sim_soc_01.md` | PENDING |
| `tests/sim_soc_debt_2026_04_13.md` | `tests/sim/sim_soc_debt_2026_04_13.md` | PENDING |
| `tests/sim_social_contest_stress.md` | `tests/sim/sim_social_contest_stress.md` | PENDING |
| `tests/sim_social_contest_stress_v1.md` | `tests/sim/sim_social_contest_stress_v1.md` | PENDING |
| `tests/sim_southernmost_stress_2026_04_13.md` | `tests/sim/sim_southernmost_stress_2026_04_13.md` | PENDING |
| `tests/sim_spoiler_bg_01.md` | `tests/sim/sim_spoiler_bg_01.md` | PENDING |
| `tests/sim_spoiler_hybrid_01.md` | `tests/sim/sim_spoiler_hybrid_01.md` | PENDING |
| `tests/sim_str_pp476_498_2026_04_08.md` | `tests/sim/sim_str_pp476_498_2026_04_08.md` | PENDING |
| `tests/sim_stress_01.md` | `tests/sim/sim_stress_01.md` | PENDING |
| `tests/sim_stress_03.md` | `tests/sim/sim_stress_03.md` | PENDING |
| `tests/sim_stress_04.md` | `tests/sim/sim_stress_04.md` | PENDING |
| `tests/sim_stress_05.md` | `tests/sim/sim_stress_05.md` | PENDING |
| `tests/sim_stress_06.md` | `tests/sim/sim_stress_06.md` | PENDING |
| `tests/sim_stress_batch_2_2026-04-16.md` | `tests/sim/sim_stress_batch_2_2026-04-16.md` | PENDING |
| `tests/sim_stress_bg_2026_04_08.md` | `tests/sim/sim_stress_bg_2026_04_08.md` | PENDING |
| `tests/sim_territory_ops_2_SIM-TERR-02.md` | `tests/sim/sim_territory_ops_2_SIM-TERR-02.md` | PENDING |
| `tests/sim_territory_ops_SIM-TERR-01.md` | `tests/sim/sim_territory_ops_SIM-TERR-01.md` | PENDING |
| `tests/sim_thread_01.md` | `tests/sim/sim_thread_01.md` | PENDING |
| `tests/sim_thread_batch_01.md` | `tests/sim/sim_thread_batch_01.md` | PENDING |
| `tests/sim_thread_batch_02.md` | `tests/sim/sim_thread_batch_02.md` | PENDING |
| `tests/sim_thread_batch_03.md` | `tests/sim/sim_thread_batch_03.md` | PENDING |
| `tests/sim_thread_batch_04.md` | `tests/sim/sim_thread_batch_04.md` | PENDING |
| `tests/sim_thread_batch_05.md` | `tests/sim/sim_thread_batch_05.md` | PENDING |
| `tests/sim_thread_batch_06.md` | `tests/sim/sim_thread_batch_06.md` | PENDING |
| `tests/sim_thread_batch_07.md` | `tests/sim/sim_thread_batch_07.md` | PENDING |
| `tests/sim_thread_batch_08.md` | `tests/sim/sim_thread_batch_08.md` | PENDING |
| `tests/sim_thread_combat_comprehensive.md` | `tests/sim/sim_thread_combat_comprehensive.md` | PENDING |
| `tests/sim_thread_combat_extreme.md` | `tests/sim/sim_thread_combat_extreme.md` | PENDING |
| `tests/sim_thread_combat_matrix_v2.md` | `tests/sim/sim_thread_combat_matrix_v2.md` | PENDING |
| `tests/sim_thread_combat_narrative.md` | `tests/sim/sim_thread_combat_narrative.md` | PENDING |
| `tests/sim_threadwork_fieldwork.md` | `tests/sim/sim_threadwork_fieldwork.md` | PENDING |
| `tests/sim_threadwork_ontological.md` | `tests/sim/sim_threadwork_ontological.md` | PENDING |
| `tests/sim_ttrpg_batch_02.md` | `tests/sim/sim_ttrpg_batch_02.md` | PENDING |
| `tests/sim_ttrpg_batch_03.md` | `tests/sim/sim_ttrpg_batch_03.md` | PENDING |
| `tests/sim_ttrpg_batch_04.md` | `tests/sim/sim_ttrpg_batch_04.md` | PENDING |
| `tests/sim_ttrpg_batch_05.md` | `tests/sim/sim_ttrpg_batch_05.md` | PENDING |
| `tests/sim_ttrpg_batch_05b.md` | `tests/sim/sim_ttrpg_batch_05b.md` | PENDING |
| `tests/sim_ttrpg_batch_06.md` | `tests/sim/sim_ttrpg_batch_06.md` | PENDING |
| `tests/sim_ttrpg_batch_07.md` | `tests/sim/sim_ttrpg_batch_07.md` | PENDING |
| `tests/sim_ttrpg_batch_08.md` | `tests/sim/sim_ttrpg_batch_08.md` | PENDING |
| `tests/sim_ttrpg_batch_09.md` | `tests/sim/sim_ttrpg_batch_09.md` | PENDING |
| `tests/sim_ttrpg_batch_10.md` | `tests/sim/sim_ttrpg_batch_10.md` | PENDING |
| `tests/sim_ttrpg_batch_legacy_02.md` | `tests/sim/sim_ttrpg_batch_legacy_02.md` | PENDING |
| `tests/sim_ttrpg_batch_legacy_03.md` | `tests/sim/sim_ttrpg_batch_legacy_03.md` | PENDING |
| `tests/sim_ttrpg_batch_legacy_04.md` | `tests/sim/sim_ttrpg_batch_legacy_04.md` | PENDING |
| `tests/sim_ttrpg_batch_r01.md` | `tests/sim/sim_ttrpg_batch_r01.md` | PENDING |
| `tests/sim_ttrpg_batch_r02.md` | `tests/sim/sim_ttrpg_batch_r02.md` | PENDING |
| `tests/sim_ttrpg_batch_r03.md` | `tests/sim/sim_ttrpg_batch_r03.md` | PENDING |
| `tests/sim_ttrpg_batch_r05a.md` | `tests/sim/sim_ttrpg_batch_r05a.md` | PENDING |
| `tests/sim_ttrpg_batch_r05b.md` | `tests/sim/sim_ttrpg_batch_r05b.md` | PENDING |
| `tests/sim_ttrpg_batch_r06a.md` | `tests/sim/sim_ttrpg_batch_r06a.md` | PENDING |
| `tests/sim_ttrpg_batch_r06b.md` | `tests/sim/sim_ttrpg_batch_r06b.md` | PENDING |
| `tests/sim_ttrpg_batch_r07.md` | `tests/sim/sim_ttrpg_batch_r07.md` | PENDING |
| `tests/sim_ttrpg_batch_sonnet46.md` | `tests/sim/sim_ttrpg_batch_sonnet46.md` | PENDING |
| `tests/sim_tw_01.md` | `tests/sim/sim_tw_01.md` | PENDING |
| `tests/sim_var_01_rm.md` | `tests/sim/sim_var_01_rm.md` | PENDING |
| `tests/sim_var_02_rs_crisis.md` | `tests/sim/sim_var_02_rs_crisis.md` | PENDING |
| `tests/sim_var_03_debate_clash.md` | `tests/sim/sim_var_03_debate_clash.md` | PENDING |
| `tests/sim_var_04_lowenritter.md` | `tests/sim/sim_var_04_lowenritter.md` | PENDING |
| `tests/sim_var_05_hybrid_crown.md` | `tests/sim/sim_var_05_hybrid_crown.md` | PENDING |
| `tests/sim_var_06_mass_combat_wounds.md` | `tests/sim/sim_var_06_mass_combat_wounds.md` | PENDING |
| `tests/sim_x26_x27_x28_cross_mode.md` | `tests/sim/sim_x26_x27_x28_cross_mode.md` | PENDING |
| `tests/sim_x26r_personal_combat_protocol.md` | `tests/sim/sim_x26r_personal_combat_protocol.md` | PENDING |
| `tests/sim_x27r_hybrid_domain_protocol.md` | `tests/sim/sim_x27r_hybrid_domain_protocol.md` | PENDING |
| `tests/sim_x28r_bg_multifaction_protocol.md` | `tests/sim/sim_x28r_bg_multifaction_protocol.md` | PENDING |
| `tests/sim_x29_x30_x31_x32_cross_mode_b.md` | `tests/sim/sim_x29_x30_x31_x32_cross_mode_b.md` | PENDING |
| `tests/sim_x33_x34_x35_x36_batch_c.md` | `tests/sim/sim_x33_x34_x35_x36_batch_c.md` | PENDING |
| `tests/sim_x_01_combat_thread.md` | `tests/sim/sim_x_01_combat_thread.md` | PENDING |
| `tests/sim_x_02_debate_thread.md` | `tests/sim/sim_x_02_debate_thread.md` | PENDING |
| `tests/sim_x_03_massbattle_thread.md` | `tests/sim/sim_x_03_massbattle_thread.md` | PENDING |
| `tests/sim_x_04_massbattle_personal.md` | `tests/sim/sim_x_04_massbattle_personal.md` | PENDING |
| `tests/sim_x_05_debate_thread_npcs.md` | `tests/sim/sim_x_05_debate_thread_npcs.md` | PENDING |
| `tests/sim_x_06_combat_wounds_npcs.md` | `tests/sim/sim_x_06_combat_wounds_npcs.md` | PENDING |
| `tests/sim_x_07_massbattle_npcs_thread.md` | `tests/sim/sim_x_07_massbattle_npcs_thread.md` | PENDING |
| `tests/sim_x_08_seasonal_cascade.md` | `tests/sim/sim_x_08_seasonal_cascade.md` | PENDING |
| `tests/sim_x_09_vaynard_almud_zoom.md` | `tests/sim/sim_x_09_vaynard_almud_zoom.md` | PENDING |
| `tests/sim_x_10_doctrine_evidence_tc.md` | `tests/sim/sim_x_10_doctrine_evidence_tc.md` | PENDING |
| `tests/sim_x_11_maret_infiltration_zoom.md` | `tests/sim/sim_x_11_maret_infiltration_zoom.md` | PENDING |
| `tests/sim_x_12_three_season_cascade.md` | `tests/sim/sim_x_12_three_season_cascade.md` | PENDING |
| `tests/sim_x_13_pulling_dissolution.md` | `tests/sim/sim_x_13_pulling_dissolution.md` | PENDING |
| `tests/sim_x_14_mode2_entity_political.md` | `tests/sim/sim_x_14_mode2_entity_political.md` | PENDING |
| `tests/sim_x_15_knot_crisis_klapp.md` | `tests/sim/sim_x_15_knot_crisis_klapp.md` | PENDING |
| `tests/sim_x_16_collective_weave.md` | `tests/sim/sim_x_16_collective_weave.md` | PENDING |
| `tests/sim_x_17_paradox_window.md` | `tests/sim/sim_x_17_paradox_window.md` | PENDING |
| `tests/sim_x_18_rendering_crisis_arc.md` | `tests/sim/sim_x_18_rendering_crisis_arc.md` | PENDING |
| `tests/sim_x_19_mass_battle_rs_multiplier.md` | `tests/sim/sim_x_19_mass_battle_rs_multiplier.md` | PENDING |
| `tests/sim_x_20_hybrid_coherence_campaign.md` | `tests/sim/sim_x_20_hybrid_coherence_campaign.md` | PENDING |
| `tests/sim_x_21_collective_weaving_brittleness.md` | `tests/sim/sim_x_21_collective_weaving_brittleness.md` | PENDING |
| `tests/sim_x_22_combat_massbattle_threadwork_temporal.md` | `tests/sim/sim_x_22_combat_massbattle_threadwork_temporal.md` | PENDING |
| `tests/simulation_report_arcs_31_33.md` | `tests/sim/simulation_report_arcs_31_33.md` | PENDING |
| `tests/stale_scan_bg_01.md` | `tests/audit/stale_scan_bg_01.md` | PENDING |
| `tests/thread_stress/threadwork_audit_register.md` | `tests/stress/thread/threadwork_audit_register.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test.md` | `tests/stress/thread/threadwork_stress_test.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch2.md` | `tests/stress/thread/threadwork_stress_test_batch2.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch3.md` | `tests/stress/thread/threadwork_stress_test_batch3.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch4.md` | `tests/stress/thread/threadwork_stress_test_batch4.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch5.md` | `tests/stress/thread/threadwork_stress_test_batch5.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch6.md` | `tests/stress/thread/threadwork_stress_test_batch6.md` | PENDING |
| `tests/thread_stress/threadwork_stress_test_batch7.md` | `tests/stress/thread/threadwork_stress_test_batch7.md` | PENDING |
| `tests/thread_stress/throughlines_2026-04-17.md` | `tests/stress/thread/throughlines_2026-04-17.md` | PENDING |
| `tests/threadwork_decision_point_analysis.md` | `tests/stress/threadwork_decision_point_analysis.md` | PENDING |
| `tests/throughline_analysis_2026-04-17.md` | `tests/audit/throughline_analysis.md` | PENDING |
| `tests/valoria_throughline_synthesis_holistic_audit.md` | `tests/audit/throughline_synthesis_holistic.md` | PENDING |

## DELETES (4 files)

| Path | Status |
|------|--------|
| `designs/board_game/military_layer_v30_skeleton.md` | PENDING |
| `designs/board_game/tc_political_redesign_v30_skeleton.md` | PENDING |
| `path` | PENDING |
| `session_log_archive.md` | PENDING |


## 2026-07-16 — Registers out of canon/ (ED-IN-0071 P0)

| old path | new path |
|---|---|
| `canon/editorial_ledger.jsonl` | `registers/editorial_ledger.jsonl` |
| `canon/editorial_ledger_archive.jsonl` | `registers/editorial_ledger_archive.jsonl` |
| `canon/editorial_ledger_fa.jsonl` | `registers/editorial_ledger_fa.jsonl` |
| `canon/editorial_ledger_fi.jsonl` | `registers/editorial_ledger_fi.jsonl` |
| `canon/editorial_ledger_in.jsonl` | `registers/editorial_ledger_in.jsonl` |
| `canon/editorial_ledger_mb.jsonl` | `registers/editorial_ledger_mb.jsonl` |
| `canon/editorial_ledger_migration_2026-05-28.md` | `registers/editorial_ledger_migration_2026-05-28.md` |
| `canon/editorial_ledger_pc.jsonl` | `registers/editorial_ledger_pc.jsonl` |
| `canon/editorial_ledger_sc.jsonl` | `registers/editorial_ledger_sc.jsonl` |
| `canon/editorial_ledger_se.jsonl` | `registers/editorial_ledger_se.jsonl` |
| `canon/editorial_ledger_wr.jsonl` | `registers/editorial_ledger_wr.jsonl` |
| `canon/mechanics_index.yaml` | `registers/mechanics_index.yaml` |
| `canon/patch_register_active.yaml` | `registers/patch_register_active.yaml` |
| `canon/patch_register_index.md` | `registers/patch_register_index.md` |
| `canon/placeholder_names.yaml` | `registers/placeholder_names.yaml` |
| `canon/supersession_register.yaml` | `registers/supersession_register.yaml` |


## 2026-07-16 — designs/proposals -> proposals (ED-IN-0071 P1)

| old path | new path |
|---|---|
| `designs/proposals/2026-05-16-PC-4.4-unified-success-stress.md` | `proposals/2026-05-16-PC-4.4-unified-success-stress.md` |
| `designs/proposals/2026-05-16-faction-audit-followup-plan.md` | `proposals/2026-05-16-faction-audit-followup-plan.md` |
| `designs/proposals/2026-05-25-mechanics-integration-v3_1.md` | `proposals/2026-05-25-mechanics-integration-v3_1.md` |
| `designs/proposals/mass_battle_fighting_withdrawal_v1.md` | `proposals/mass_battle_fighting_withdrawal_v1.md` |
| `designs/proposals/mass_battle_shape_echelon_revamp.md` | `proposals/mass_battle_shape_echelon_revamp.md` |
| `designs/proposals/multiunit_envelopment_plan.md` | `proposals/multiunit_envelopment_plan.md` |
| `designs/proposals/pc_formation_system.md` | `proposals/pc_formation_system.md` |
| `designs/proposals/repo-reorganization-v1.md` | `proposals/repo-reorganization-v1.md` |
| `designs/proposals/stub_infill_plan.md` | `proposals/stub_infill_plan.md` |
| `designs/proposals/weapon_physics_and_concentration_model.md` | `proposals/weapon_physics_and_concentration_model.md` |

## 2026-07-16 — primary promotions batch (research/dashboard/workplans, ED-IN-0071 P1)

| old path | new path |
|---|---|
| `references/historical/mass_battle_gauge_grounding.md` | `research/historical/mass_battle_gauge_grounding.md` |
| `references/historical/precedents_analysis.md` | `research/historical/precedents_analysis.md` |
| `references/historical/precedents_warfare.md` | `research/historical/precedents_warfare.md` |
| `docs/dashboard/data.json` | `dashboard/data.json` |
| `docs/dashboard/icon.svg` | `dashboard/icon.svg` |
| `docs/dashboard/index.html` | `dashboard/index.html` |
| `docs/dashboard/manifest.json` | `dashboard/manifest.json` |
| `designs/workplans/README.md` | `workplans/README.md` |
| `designs/workplans/valoria_master_workplan_v6.md` | `workplans/valoria_master_workplan_v6.md` |
| `designs/workplans/workplan_v6_progress.yaml` | `workplans/workplan_v6_progress.yaml` |


## 2026-07-16 — Godot three-home collapse -> godot/ (ED-IN-0071 P2)

| old path | new path |
|---|---|
| `designs/godot/` | `godot/` |
| `designs/videogame/` | `godot/` |
| `designs/audit/2026-06-10-godot-conversion-strategy/` | `godot/` |
| `designs/audit/2026-06-10-godot-conversion-strategy/README.md` | `godot/README.md` |
| `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md` | `godot/godot_conversion_strategy_v1.md` |
| `designs/godot/data_serialization_spec.md` | `godot/data_serialization_spec.md` |
| `designs/godot/gm_to_engine_conversion.md` | `godot/gm_to_engine_conversion.md` |
| `designs/godot/implementation_sequence.md` | `godot/implementation_sequence.md` |
| `designs/godot/scene_tree_architecture.md` | `godot/scene_tree_architecture.md` |
| `designs/godot/skeleton/core/engine_manifest.gd` | `godot/skeleton/core/engine_manifest.gd` |
| `designs/godot/skeleton/core/key_type_resource.gd` | `godot/skeleton/core/key_type_resource.gd` |
| `designs/godot/skeleton/data/combat_config.tres` | `godot/skeleton/data/combat_config.tres` |
| `designs/godot/skeleton/data/engines/combat/combat.tres` | `godot/skeleton/data/engines/combat/combat.tres` |
| `designs/godot/skeleton/data/engines/combat/strike.tres` | `godot/skeleton/data/engines/combat/strike.tres` |
| `designs/godot/skeleton/data/engines/combat/wound.tres` | `godot/skeleton/data/engines/combat/wound.tres` |
| `designs/godot/skeleton/data/key_types/scene_combat_felled.tres` | `godot/skeleton/data/key_types/scene_combat_felled.tres` |
| `designs/godot/skeleton/data/key_types/scene_combat_hit.tres` | `godot/skeleton/data/key_types/scene_combat_hit.tres` |
| `designs/godot/skeleton/data/key_types/scene_combat_resolved.tres` | `godot/skeleton/data/key_types/scene_combat_resolved.tres` |
| `designs/godot/skeleton/data/key_types/scene_combat_strike.tres` | `godot/skeleton/data/key_types/scene_combat_strike.tres` |
| `designs/godot/skeleton/data/traditions/german.tres` | `godot/skeleton/data/traditions/german.tres` |
| `designs/godot/skeleton/data/traditions/none.tres` | `godot/skeleton/data/traditions/none.tres` |
| `designs/godot/skeleton/data/weapons/arming.tres` | `godot/skeleton/data/weapons/arming.tres` |
| `designs/godot/skeleton/data/weapons/longsword.tres` | `godot/skeleton/data/weapons/longsword.tres` |
| `designs/godot/skeleton/engines/combat/combat_engine.gd` | `godot/skeleton/engines/combat/combat_engine.gd` |
| `designs/godot/skeleton/engines/combat/modules/strike_module.gd` | `godot/skeleton/engines/combat/modules/strike_module.gd` |
| `designs/godot/skeleton/engines/combat/modules/wound_module.gd` | `godot/skeleton/engines/combat/modules/wound_module.gd` |
| `designs/godot/skeleton/engines/combat/resources/combat_config.gd` | `godot/skeleton/engines/combat/resources/combat_config.gd` |
| `designs/godot/skeleton/engines/combat/resources/tradition_resource.gd` | `godot/skeleton/engines/combat/resources/tradition_resource.gd` |
| `designs/godot/skeleton/engines/combat/resources/weapon_resource.gd` | `godot/skeleton/engines/combat/resources/weapon_resource.gd` |
| `designs/videogame/godot_architecture_specification.md` | `godot/godot_architecture_specification.md` |


## 2026-07-16 — arcs primary promotion -> arcs/ (+ arcs/registers/) (ED-IN-0071 P1-class)

| old path | new path |
|---|---|
| `designs/arcs/` | `arcs/` |
| `references/arcs/` | `arcs/registers/` |
| `references/arc_register.md` | `arcs/registers/arc_register.md` |
| `references/arc_register_infill.md` | `arcs/registers/arc_register_infill.md` |
| `designs/arcs/README.md` | `arcs/README.md` |
| `designs/arcs/arc_expansion_v30.md` | `arcs/arc_expansion_v30.md` |
| `designs/arcs/arc_expansion_v30_index.md` | `arcs/arc_expansion_v30_index.md` |
| `designs/arcs/arcs_16_19.md` | `arcs/simulated/arcs_16_19.md` |
| `designs/arcs/arcs_16_19_index.md` | `arcs/simulated/arcs_16_19_index.md` |
| `designs/arcs/arcs_20_23.md` | `arcs/simulated/arcs_20_23.md` |
| `designs/arcs/arcs_20_23_index.md` | `arcs/simulated/arcs_20_23_index.md` |
| `designs/arcs/arcs_24_27.md` | `arcs/simulated/arcs_24_27.md` |
| `designs/arcs/arcs_24_27_index.md` | `arcs/simulated/arcs_24_27_index.md` |
| `designs/arcs/arcs_28_30.md` | `arcs/simulated/arcs_28_30.md` |
| `designs/arcs/arcs_28_30_index.md` | `arcs/simulated/arcs_28_30_index.md` |
| `designs/arcs/arcs_31_35.md` | `arcs/simulated/arcs_31_35.md` |
| `designs/arcs/arcs_31_35_index.md` | `arcs/simulated/arcs_31_35_index.md` |
| `designs/arcs/emergent_arcs_experimental.md` | `arcs/emergent_arcs_experimental.md` |
| `designs/arcs/emergent_arcs_experimental_index.md` | `arcs/emergent_arcs_experimental_index.md` |
| `designs/arcs/emergent_campaign_arcs.md` | `arcs/emergent_campaign_arcs.md` |
| `designs/arcs/emergent_scenarios.md` | `arcs/emergent_scenarios.md` |
| `designs/arcs/emergent_scenarios_index.md` | `arcs/emergent_scenarios_index.md` |
| `designs/arcs/gm_ref/README.md` | `arcs/simulated/README.md` |
| `designs/arcs/gm_ref/arc_narrative_analysis.md` | `arcs/simulated/arc_narrative_analysis.md` |
| `designs/arcs/gm_ref/arc_narrative_analysis_index.md` | `arcs/simulated/arc_narrative_analysis_index.md` |
| `designs/arcs/gm_ref/arcs_01_04.md` | `arcs/simulated/arcs_01_04.md` |
| `designs/arcs/gm_ref/arcs_01_04_index.md` | `arcs/simulated/arcs_01_04_index.md` |
| `designs/arcs/gm_ref/arcs_05_09.md` | `arcs/simulated/arcs_05_09.md` |
| `designs/arcs/gm_ref/arcs_05_09_index.md` | `arcs/simulated/arcs_05_09_index.md` |
| `designs/arcs/gm_ref/arcs_10_18.md` | `arcs/simulated/arcs_10_18.md` |
| `designs/arcs/gm_ref/arcs_10_18_index.md` | `arcs/simulated/arcs_10_18_index.md` |
| `designs/arcs/gm_ref/arcs_36_40.md` | `arcs/simulated/arcs_36_40.md` |
| `designs/arcs/gm_ref/arcs_36_40_index.md` | `arcs/simulated/arcs_36_40_index.md` |
| `designs/arcs/gm_ref/arcs_41_45.md` | `arcs/simulated/arcs_41_45.md` |
| `designs/arcs/gm_ref/arcs_41_45_index.md` | `arcs/simulated/arcs_41_45_index.md` |
| `designs/arcs/gm_ref/arcs_46_55.md` | `arcs/simulated/arcs_46_55.md` |
| `designs/arcs/gm_ref/arcs_46_55_index.md` | `arcs/simulated/arcs_46_55_index.md` |
| `designs/arcs/gm_ref/arcs_46_55_resolved.md` | `arcs/simulated/arcs_46_55_resolved.md` |
| `designs/arcs/gm_ref/arcs_46_55_resolved_index.md` | `arcs/simulated/arcs_46_55_resolved_index.md` |
| `designs/arcs/narrative_scenario_chains.md` | `arcs/narrative_scenario_chains.md` |
| `designs/arcs/narrative_scenario_chains_index.md` | `arcs/narrative_scenario_chains_index.md` |
| `designs/arcs/throughline_resolutions_v30.md` | `arcs/throughline_resolutions_v30.md` |
| `designs/arcs/throughline_resolutions_v30_index.md` | `arcs/throughline_resolutions_v30_index.md` |
| `references/arc_register.md` | `arcs/registers/arc_register.md` |
| `references/arc_register_infill.md` | `arcs/registers/arc_register_infill.md` |
| `references/arcs/arc_register_clocks.md` | `arcs/registers/arc_register_clocks.md` |
| `references/arcs/arc_register_events.md` | `arcs/registers/arc_register_events.md` |
| `references/arcs/arc_register_factions.md` | `arcs/registers/arc_register_factions.md` |
| `references/arcs/arc_register_territory.md` | `arcs/registers/arc_register_territory.md` |
| `references/arcs/arc_register_threads.md` | `arcs/registers/arc_register_threads.md` |


## 2026-07-16 — arcs/gm_ref -> simulated + root arc-batches pulled in (ED-IN-0071 follow-up)

| old path | new path |
|---|---|
| `arcs/gm_ref/` | `arcs/simulated/` |
| `arcs/arcs_16_19.md` | `arcs/simulated/arcs_16_19.md` |
| `arcs/arcs_16_19_index.md` | `arcs/simulated/arcs_16_19_index.md` |
| `arcs/arcs_20_23.md` | `arcs/simulated/arcs_20_23.md` |
| `arcs/arcs_20_23_index.md` | `arcs/simulated/arcs_20_23_index.md` |
| `arcs/arcs_24_27.md` | `arcs/simulated/arcs_24_27.md` |
| `arcs/arcs_24_27_index.md` | `arcs/simulated/arcs_24_27_index.md` |
| `arcs/arcs_28_30.md` | `arcs/simulated/arcs_28_30.md` |
| `arcs/arcs_28_30_index.md` | `arcs/simulated/arcs_28_30_index.md` |
| `arcs/arcs_31_35.md` | `arcs/simulated/arcs_31_35.md` |
| `arcs/arcs_31_35_index.md` | `arcs/simulated/arcs_31_35_index.md` |


## 2026-07-16 — handoffs/ -> registers/handoffs/ (ED-IN-0071 P0b, part 1)

| old path | new path |
|---|---|
| `handoffs/` | `registers/handoffs/` |
| `handoffs/HANDOFF_FA.md` | `registers/handoffs/HANDOFF_FA.md` |
| `handoffs/HANDOFF_FI.md` | `registers/handoffs/HANDOFF_FI.md` |
| `handoffs/HANDOFF_GO.md` | `registers/handoffs/HANDOFF_GO.md` |
| `handoffs/HANDOFF_IN.md` | `registers/handoffs/HANDOFF_IN.md` |
| `handoffs/HANDOFF_MB.md` | `registers/handoffs/HANDOFF_MB.md` |
| `handoffs/HANDOFF_PC.md` | `registers/handoffs/HANDOFF_PC.md` |
| `handoffs/HANDOFF_SC.md` | `registers/handoffs/HANDOFF_SC.md` |
| `handoffs/HANDOFF_SE.md` | `registers/handoffs/HANDOFF_SE.md` |
| `handoffs/HANDOFF_WR.md` | `registers/handoffs/HANDOFF_WR.md` |
| `handoffs/HANDOFF_archive.md` | `registers/handoffs/HANDOFF_archive.md` |


## 2026-07-16 — archives/ -> deprecated/archives/ (merge graveyards, ED-IN-0071 P5, fork #1)

| old path | new path |
|---|---|
| `archives/` | `deprecated/archives/` |
| `archives/audit/` | `deprecated/archives/audit/` |
| `archives/editorial/` | `deprecated/archives/editorial/` |
| `archives/editorials/` | `deprecated/archives/editorials/` |
| `archives/handoffs/` | `deprecated/archives/handoffs/` |
| `archives/patches/` | `deprecated/archives/patches/` |
| `archives/propagation/` | `deprecated/archives/propagation/` |
| `archives/session/` | `deprecated/archives/session/` |
| `archives/workplans/` | `deprecated/archives/workplans/` |


## 2026-07-16 — references/engine_params -> engine/engine_params (ED-IN-0071 P3 seed)

| old path | new path |
|---|---|
| `references/engine_params/` | `engine/engine_params/` |
| `references/engine_params/combat_engine_v1.json` | `engine/engine_params/combat_engine_v1.json` |


## 2026-07-16 — params/ -> engine/params/ (ED-IN-0071 P3; pointers for prose refs)

| old path | new path |
|---|---|
| `params/` | `engine/params/` |
| `params/bg/ci_seizure.md` | `engine/params/bg/ci_seizure.md` |
| `params/bg/clocks.md` | `engine/params/bg/clocks.md` |
| `params/bg/core.md` | `engine/params/bg/core.md` |
| `params/bg/ed_resolutions.md` | `engine/params/bg/ed_resolutions.md` |
| `params/bg/faction_actions.md` | `engine/params/bg/faction_actions.md` |
| `params/bg/geography.md` | `engine/params/bg/geography.md` |
| `params/bg/institutions.md` | `engine/params/bg/institutions.md` |
| `params/bg/military.md` | `engine/params/bg/military.md` |
| `params/bg/ministry.md` | `engine/params/bg/ministry.md` |
| `params/bg/npc_priority_trees.md` | `engine/params/bg/npc_priority_trees.md` |
| `params/bg/npcs_special.md` | `engine/params/bg/npcs_special.md` |
| `params/bg/parliament.md` | `engine/params/bg/parliament.md` |
| `params/bg/phases.md` | `engine/params/bg/phases.md` |
| `params/bg/royal_assassination.md` | `engine/params/bg/royal_assassination.md` |
| `params/bg/stress_patches.md` | `engine/params/bg/stress_patches.md` |
| `params/bg/tensions_deck.md` | `engine/params/bg/tensions_deck.md` |
| `params/bg/tracks.md` | `engine/params/bg/tracks.md` |
| `params/bg/victory.md` | `engine/params/bg/victory.md` |
| `params/board_game.md` | `engine/params/board_game.md` |
| `params/board_game_misc.md` | `engine/params/board_game_misc.md` |
| `params/campaign_modes.md` | `engine/params/campaign_modes.md` |
| `params/contest.md` | `engine/params/contest.md` |
| `params/contest_extensions.md` | `engine/params/contest_extensions.md` |
| `params/core.md` | `engine/params/core.md` |
| `params/factions.md` | `engine/params/factions.md` |
| `params/factions/npc_stance_triangles.md` | `engine/params/factions/npc_stance_triangles.md` |
| `params/factions/riskbreakers_identity.md` | `engine/params/factions/riskbreakers_identity.md` |
| `params/factions/stats_1_7_scale.md` | `engine/params/factions/stats_1_7_scale.md` |
| `params/factions_personal.md` | `engine/params/factions_personal.md` |
| `params/fieldwork.md` | `engine/params/fieldwork.md` |
| `params/history/board_game.md` | `engine/params/history/board_game.md` |
| `params/history/campaign_modes.md` | `engine/params/history/campaign_modes.md` |
| `params/history/combat.md` | `engine/params/history/combat.md` |
| `params/history/core.md` | `engine/params/history/core.md` |
| `params/history/factions_personal.md` | `engine/params/history/factions_personal.md` |
| `params/history/mass_combat.md` | `engine/params/history/mass_combat.md` |
| `params/history/southernmost.md` | `engine/params/history/southernmost.md` |
| `params/history/threadwork.md` | `engine/params/history/threadwork.md` |
| `params/mass_combat.md` | `engine/params/mass_combat.md` |
| `params/scale_transitions.md` | `engine/params/scale_transitions.md` |
| `params/southernmost.md` | `engine/params/southernmost.md` |
| `params/threadwork.md` | `engine/params/threadwork.md` |
| `params/threadwork_superseded.md` | `engine/params/threadwork_superseded.md` |


## 2026-07-16 — sim/ engine core -> engine/ (ED-IN-0071 P3 Phase A)

| old path | new path |
|---|---|
| `sim/substrate/` | `engine/substrate/` |
| `sim/autoload/` | `engine/autoload/` |
| `sim/cross_scale/` | `engine/cross_scale/` |
| `sim/mc_v18.py` | `engine/mc_v18.py` |


## 2026-07-17 — designs/ -> systems/ P4 slice 1 (doc-only clean subsystems, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/npcs/` | `systems/npcs/` |
| `designs/articulation/` | `systems/articulation/` |
| `designs/ui/` | `systems/ui/` |


## 2026-07-17 — threadwork designs/ + sim/ -> systems/ (P4 slice 2, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/threadwork/` | `systems/threadwork/` |
| `sim/thread/` | `systems/threadwork/sim/` |


## 2026-07-17 — designs/architecture/ -> systems/_architecture/ (P4 slice 3, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/architecture/` | `systems/_architecture/` |


## 2026-07-17 — world designs/ + sim/ -> systems/ (P4 slice 4, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/world/` | `systems/world/` |
| `sim/world/` | `systems/world/sim/` |


## 2026-07-17 — settlements designs/territory + sim/territory -> systems/settlements/ (P4 slice 5, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/territory/` | `systems/settlements/` |
| `sim/territory/` | `systems/settlements/sim/` |


## 2026-07-17 — fieldwork cross-subdir extraction -> systems/fieldwork/ (P4 slice 6, ED-IN-0071)

| old path | new path |
|---|---|
| `designs/scene/fieldwork_bg_v30.md` | `systems/fieldwork/fieldwork_bg_v30.md` |
| `designs/scene/fieldwork_bg_v30_infill.md` | `systems/fieldwork/fieldwork_bg_v30_infill.md` |
| `designs/scene/fieldwork_editorial.md` | `systems/fieldwork/fieldwork_editorial.md` |
| `designs/scene/fieldwork_exploration.md` | `systems/fieldwork/fieldwork_exploration.md` |
| `designs/scene/fieldwork_exposure.md` | `systems/fieldwork/fieldwork_exposure.md` |
| `designs/scene/fieldwork_godot.md` | `systems/fieldwork/fieldwork_godot.md` |
| `designs/scene/fieldwork_hybrid_v30.md` | `systems/fieldwork/fieldwork_hybrid_v30.md` |
| `designs/scene/fieldwork_hybrid_v30_infill.md` | `systems/fieldwork/fieldwork_hybrid_v30_infill.md` |
| `designs/scene/fieldwork_investigation.md` | `systems/fieldwork/fieldwork_investigation.md` |
| `designs/scene/fieldwork_rationale.md` | `systems/fieldwork/fieldwork_rationale.md` |
| `designs/scene/fieldwork_socializing.md` | `systems/fieldwork/fieldwork_socializing.md` |
| `designs/scene/fieldwork_summary.md` | `systems/fieldwork/fieldwork_summary.md` |
| `designs/scene/fieldwork_v30.md` | `systems/fieldwork/fieldwork_v30.md` |
| `designs/scene/fieldwork_v30_index.md` | `systems/fieldwork/fieldwork_v30_index.md` |
| `designs/scene/fieldwork_v30_infill.md` | `systems/fieldwork/fieldwork_v30_infill.md` |
| `designs/scene/investigation_systems_v30.md` | `systems/fieldwork/investigation_systems_v30.md` |
| `designs/scene/investigation_systems_v30_index.md` | `systems/fieldwork/investigation_systems_v30_index.md` |
| `designs/personal/knots_v30.md` | `systems/fieldwork/knots_v30.md` |
| `sim/personal/fieldwork.py` | `systems/fieldwork/sim/fieldwork.py` |
| `sim/personal/investigation.py` | `systems/fieldwork/sim/investigation.py` |
| `sim/personal/knots.py` | `systems/fieldwork/sim/knots.py` |
| `sim/personal/fieldwork` | `systems/fieldwork/sim/fieldwork` |
| `sim/personal/investigation` | `systems/fieldwork/sim/investigation` |
| `sim/personal/knots` | `systems/fieldwork/sim/knots` |
