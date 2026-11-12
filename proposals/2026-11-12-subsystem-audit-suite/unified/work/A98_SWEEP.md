# A-98 · the vocabulary sweep: files edited and counts

## Status: REFERENCE (the A-98 lane's record of one sweep round, 2026-11-12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree, 2026-11-12. Lane: A-98 vocabulary sweep. Ruling: `unified/DECISIONS_ANSWERED.md` A-98. Companions: `A98_DERIVED_SCORES.md` (the derived-score inventory), `A98_LAYER1_WORDS.md` (Layer 1, listed not edited).

**Method.** The glossary (`U1_GLOSSARY.md` §A–§B, §C *resolve*, §H), `U1_OWNERS_AND_VOCABULARY.md` (D-U1-11p, D-U1-11q
superseded; C-02, C-12, D-U1-04) and `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (§2, new §2a, §3–§4, §8–§10) were
rewritten by hand (Edit). The rest was one scripted pass over `proposals/`, `master/` and `unified/`, dry-run first
with every changed line listed and reviewed (513 lines), then applied; then 52 exact-string rewordings by sense
(each asserted to match once) and a handful of Edit calls; then one `Reconciled:` clause per edited file (a new
`Reconciled:` line in the eight files that had none). `python tools/ci_naming_check.py` after each write: no new use
of a deprecated name.

**The scripted rules, by sense.** Applied only to prose: never inside backticks or fenced code (code comments
excepted), never inside double-quoted or italic-quoted text, never on a `Reconciled:`/`Folded:` line or a
blockquote. *capability(ies)* → *skill(s)*, except as an identifier (any `_`, `.`, `-`, `` ` `` or `:` neighbour) and in
document and batch names ("capability (authoring) architecture", "capability-authoring", "capability authoring
surface", "capability axiom map", "capability home", "capability batch", "capability Part"); *trained score/rank* →
*skill score* (and "trained `x` score" → "`x` skill score"); *talent* → *governing attribute* / *attribute* by
phrase ("talent as levels" → "the governing attribute as levels", "talent rows" → "attribute rows", "rank 5 with
talent 2" → "attribute 2", …); *training* only where it meant the rank ("training gives dice", "the roller's
training", "the pool is training only") → *skill score*. Proposed identifiers that carried the retired word
(none is in the tree) were renamed: `talent_level` → `attribute_level`, `pool.py::talent` →
`pool.py::governing_attribute`, three proposed test names.

**Rewordings by sense** (the last column below): the retired kinds in schema blocks and tables (`kinds: [skill]`;
`insight` and the `keen_eye` example are skills; the `moved_by_*` rows and the `unmoved` example move to the trait
roster, U1 §2a); "a trait is a capability row of kind `trait`" (`05_SC_capability_surface.md`); where *capability*
had meant Thread Sensitivity (the one `gate`: now "the one held value", since Thread Sensitivity is a practitioner's
stat, not a skill: architecture §3 item 5 and §8, `U5a_capability_home…`, `U5_CONFLICTS_U5a.md`,
`U3_CONFLICT_LEDGER.md`); line-wrapped "trained / score"; `10_DICE_capability_axiom_map.md`'s `resource` row ("a pool
that drains" → "a reserve that drains (a derived score …)", `A98_DERIVED_SCORES.md` mislabel 1).

## Counts

| word | occurrences changed | files |
|---|---|---|
| *capability* in prose → skill | 371 scripted, plus the glossary, OWNERS and architecture rewrites | 81 scripted; 3 rewritten by hand |
| *trained score / trained rank / trained skill* → skill score | 137 (124 scripted, 13 by hand) | 64 scripted; 9 by hand |
| *talent* → attribute / governing attribute | 75 (61 scripted, 14 by hand), plus 15 in the architecture and OWNERS | 41 scripted; 7 by hand, 2 rewritten |
| *training* meaning the rank → skill score | 24 (17 scripted, 7 by hand) | 11 scripted; 6 by hand |
| *aptitude* (the attribute or the kind) | 10 by hand, plus the glossary, OWNERS and architecture | 6 by hand; 3 rewritten |
| *prowess* of a person → martial skill | 1 (`29_DICE` table row), plus the glossary row; no other live use found | 2 |
| proposed identifiers renamed | 35 | 12 |
| traits apart, Thread Sensitivity not a skill | 8 by hand, plus `02_CHAR_which_ground_moves_whom.md` edits 1 and 4 | 9 |

**Files edited: 115** (101 in `proposals/`, 13 in `unified/`, 1 in `master/`), listed below. Columns: capability,
trained, talent, training (scripted), identifiers (scripted), rewordings by hand.

| file | capability | trained | talent | training | identifiers | by hand |
|---|---|---|---|---|---|---|
| `master/HOLISTIC_AUDIT_part3.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/01_CORE_capability_authoring_surface.md` | 24 | 0 | 3 | 0 | 0 | 5 |
| `proposals/01_CORE_tests_shipped_world_falsifiers.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/02_CHAR_capability_definitions.md` | 9 | 0 | 0 | 0 | 0 | 2 |
| `proposals/02_CHAR_capability_uses_table.md` | 11 | 0 | 0 | 0 | 0 | 1 |
| `proposals/02_CHAR_offer_what_can_be_done.md` | 4 | 0 | 0 | 0 | 0 | 0 |
| `proposals/02_CHAR_voices_and_the_room.md` | 4 | 0 | 0 | 0 | 0 | 0 |
| `proposals/02_CHAR_what_an_act_risks.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/02_CHAR_which_ground_moves_whom.md` | 1 | 0 | 0 | 1 | 0 | 4 |
| `proposals/03_PC_duel_round_and_approach.md` | 1 | 0 | 0 | 0 | 1 | 0 |
| `proposals/03_PC_exits_withdrawal_recovery.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `proposals/03_PC_loadout_and_carry.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/03_PC_person_inputs_content.md` | 2 | 1 | 0 | 1 | 1 | 1 |
| `proposals/04_MB_campaign_party_economy.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/04_MB_manager_battle_one_resolver.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/04_MB_squad_grid_of_named_characters.md` | 5 | 0 | 0 | 0 | 0 | 0 |
| `proposals/04_MB_typed_outcome_and_one_path.md` | 3 | 1 | 0 | 0 | 0 | 0 |
| `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/05_SC_capability_surface.md` | 7 | 0 | 0 | 0 | 0 | 2 |
| `proposals/05_SC_hearing_capabilities.md` | 12 | 0 | 0 | 1 | 0 | 1 |
| `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md` | 0 | 1 | 0 | 0 | 1 | 0 |
| `proposals/05_SC_opposed_obstacle_parity.md` | 0 | 4 | 0 | 0 | 0 | 0 |
| `proposals/05_SC_playable_hearing_B.md` | 1 | 2 | 0 | 0 | 0 | 0 |
| `proposals/06_FA_office_capabilities.md` | 25 | 0 | 0 | 0 | 0 | 0 |
| `proposals/07_SE_capability_and_chooser_surface.md` | 9 | 0 | 0 | 0 | 0 | 0 |
| `proposals/07_SE_capability_rate_B.md` | 18 | 1 | 0 | 0 | 0 | 0 |
| `proposals/10_DICE_advantage_sources_for_the_arcs.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/10_DICE_believed_odds_have_a_prior.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `proposals/10_DICE_capability_axiom_map.md` | 28 | 5 | 0 | 2 | 1 | 5 |
| `proposals/10_DICE_one_score_two_roles.md` | 10 | 1 | 0 | 0 | 1 | 3 |
| `proposals/11_GO_design_reference_disposition.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/11_GO_player_surface_contract_B.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/11_GO_pointer_and_stale_text_resolutions.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/12_ARCS_case_on_the_realm.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/13_SC_calibration.md` | 0 | 1 | 0 | 0 | 0 | 1 |
| `proposals/13_SC_draw_for_unrolled_contests.md` | 0 | 2 | 0 | 0 | 0 | 0 |
| `proposals/13_SC_tuning_tables.md` | 2 | 2 | 0 | 0 | 0 | 2 |
| `proposals/14_VERBS_BINDING_A_formation.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_BINDING_B_sittings.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_BINDING_C_turnover.md` | 2 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_BINDING_D_orders.md` | 0 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_BINDING_E_war_seats.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MATERIAL_A_mending.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MATERIAL_B_stores.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MATERIAL_C_works.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MATERIAL_D_paper.md` | 0 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MATERIAL_E_knowledge.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MILITARY_A_movement.md` | 2 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MILITARY_B_train.md` | 9 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MILITARY_C_the_muster.md` | 1 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | 1 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | 1 | 0 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` | 0 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_PHYSICAL_C_looking.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_PHYSICAL_D_thread_read.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL1_B_documents_and_obedience.md` | 2 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | 11 | 2 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | 4 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL2_C_case_question_confession.md` | 1 | 3 | 1 | 0 | 0 | 0 |
| `proposals/14_VERBS_SOCIAL2_D_tie.md` | 0 | 2 | 1 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md` | 1 | 2 | 0 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` | 1 | 4 | 1 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_COLONIAL_B_distance.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_SYNTHESIS_E_implementation_plan.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_VENICE_A_obligation_and_the_ask.md` | 0 | 1 | 1 | 0 | 0 | 0 |
| `proposals/15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md` | 0 | 1 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` | 1 | 0 | 2 | 0 | 0 | 1 |
| `proposals/16_PESSIMIST_DICE_task_difficulty_and_throughput.md` | 0 | 2 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` | 0 | 0 | 0 | 1 | 0 | 0 |
| `proposals/16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_MB_partition_and_the_pair_rule.md` | 0 | 1 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_MB_rout_has_two_exits.md` | 0 | 1 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_PC_A_the_yield_is_a_draw.md` | 1 | 1 | 1 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_PC_B_the_commit_window.md` | 0 | 1 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md` | 0 | 3 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md` | 0 | 0 | 0 | 0 | 0 | 0 |
| `proposals/16_PESSIMIST_WR_A_the_road_is_drawn.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/17_CENSUS_C1A_01_deletion_batches.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/17_CENSUS_REST_2_wiring.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/18_DETERMINISM_notice_is_a_draw.md` | 2 | 1 | 2 | 0 | 0 | 0 |
| `proposals/18_DETERMINISM_rival_acts_in_one_fold.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md` | 3 | 0 | 0 | 0 | 0 | 0 |
| `proposals/21_PROCEDURAL_B_cast_and_seats.md` | 5 | 0 | 0 | 0 | 0 | 0 |
| `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `proposals/23_STORY_B_a_house_continues.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/26_MASS_BATTLE_maneuver_orders.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/27_MB_A_command_and_the_obedience_draw.md` | 10 | 3 | 5 | 1 | 4 | 2 |
| `proposals/28_CORE_scene_access_B_appointments.md` | 1 | 0 | 0 | 0 | 0 | 0 |
| `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` | 3 | 12 | 2 | 3 | 2 | 6 |
| `proposals/31_WR_B_the_revival_gathers.md` | 0 | 0 | 0 | 1 | 0 | 1 |
| `proposals/U5a_CHAR_self_knowledge_is_a_belief.md` | 2 | 0 | 0 | 0 | 0 | 1 |
| `proposals/U5a_capability_home_and_two_inputs.md` | 5 | 5 | 5 | 0 | 8 | 1 |
| `proposals/U5b_PC_residue.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `proposals/U5b_PC_rulings_in_the_fight.md` | 0 | 4 | 6 | 1 | 1 | 2 |
| `proposals/U5b_VERBS_military_physical_residue.md` | 2 | 1 | 1 | 0 | 0 | 0 |
| `proposals/U5c_SC_one_obstacle_form.md` | 9 | 2 | 0 | 0 | 0 | 0 |
| `unified/OWED_TO_UNIFICATION.md` | 1 | 2 | 0 | 0 | 0 | 0 |
| `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` | 19 | 4 | 3 | 0 | 10 | 25 |
| `unified/U1_GLOSSARY.md` | 0 | 0 | 0 | 0 | 0 | 24 |
| `unified/U1_JORDAN_CALLS.md` | 1 | 0 | 1 | 0 | 0 | 0 |
| `unified/U1_OWNERS_AND_VOCABULARY.md` | 23 | 6 | 1 | 4 | 3 | 13 |
| `unified/U2_LAYER1_CONFORMANCE.md` | 17 | 1 | 0 | 1 | 2 | 1 |
| `unified/U3_CONFLICT_LEDGER.md` | 4 | 5 | 1 | 0 | 0 | 3 |
| `unified/U3_LAYER1_AMENDMENTS.md` | 0 | 1 | 0 | 0 | 0 | 0 |
| `unified/U4_DOCUMENT_STATUS.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `unified/U4_FACT_CHECK.md` | 0 | 0 | 0 | 0 | 0 | 1 |
| `unified/U5_CONFLICTS_U5a.md` | 8 | 1 | 0 | 0 | 0 | 4 |
| `unified/U5_CONFLICTS_U5c.md` | 2 | 0 | 0 | 0 | 0 | 0 |
| `unified/U6_VERDICT_AND_REPAIRS.md` | 1 | 0 | 0 | 0 | 0 | 0 |
