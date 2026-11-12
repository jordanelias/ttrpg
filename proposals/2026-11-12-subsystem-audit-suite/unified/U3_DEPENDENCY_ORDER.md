# U3 — the single dependency order: every proposal and implementation lane A, in batches, acyclic

## Status: WORK LEDGER (unification wave 2, lane U3; the input to workplan v12, `STAGES.md` step 6; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

## Read at: the working tree of branch `ccr-62958c70-0kjhsw`, HEAD `181548b`, 2026-11-12. Producer: Opus lane U3. Companion: `unified/U3_CONFLICT_LEDGER.md` (the decisions this order applies, cited `C3-…`).

Reconciled: 2026-11-12, U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*); "knockout" → "removal test" (glossary *removal test*; file names keep their words).

## 0. How this order was built, and what it is not

**Source of the edges.** The five read lanes' §5 tables (`unified/work/R1_READ.md` to `R5_READ.md`): one row per
proposal, its dependencies marked EXISTS-IN-TREE / PROPOSED / MISSING, the files it edits, its declared hash
movers, its lane tag, whether a gate and a cost class are named. This lane parsed those 300 rows by script
(scratch, not committed), resolved every proposal name and abbreviation (`OBS`, `VRES`, `RES-V`, `CAP`, `PB`,
`UPR`, `UMR`, `SC-B`, `18-A`, `FA-P1`…`FA-B4`, `BIND_A`…`VEN_E`, `SC-P1`…`SC-P8`) to its file, and read the
proposals' own landing orders where they state one (`U5a_DICE_owed_edits.md` §1 Order;
`U5a_capability_home_and_two_inputs.md` Order; `U5c_SC_one_obstacle_form.md` §4; `29_DICE_one_opposed_rule_form_and_tuning.md`
Dependencies; `U5b_PC_rulings_in_the_fight.md` §5; `U5b_MB_rulings_in_the_field.md` §6; `27_MB_A` Dependencies).

**What the raw graph is.** 300 proposal nodes (every file under `proposals/`, each in exactly one read lane),
790 proposal-to-proposal edges, one strongly connected component of 119 nodes, six smaller ones, 58 mutual
pairs. The read lanes' "depends on" records citation in both directions (a proposal names the file that amends
it, re-points it or supersedes it), so the raw graph is not a landing order. **This order makes it one** by
(1) assigning every proposal to one batch, (2) keeping every edge that points from a later batch to an earlier
one or inside a batch, and (3) removing every edge that points forward, each with a stated category and reason
(§4.1: 91 edges; SPLIT 59, REV 12, LATER 12, SUP 7, LANDED 1; row 91, LATER, added by U6 R-A). The batch graph that
remains is acyclic (checked by script: every kept edge points to a batch of lower order). **Inside a batch** the
order was not checked at first; §1.2 checks it, §1.3 checks that each gate's instrument exists by its batch, and
§1.4 places the Layer 1 amendments as gate nodes (U6 R-A).

**What decides the grouping.** STAGES.md step 6's rules: owners and hash-equal work first, the batches every
requirement stands on (the one roll, the keyed draw, the capability home) first by dependency; hash movers
co-batched so a seeded re-pin happens once per batch; the families' own landing orders kept where they exist;
items linked by a mutual dependency in one batch; cross-lane batches only where a dependency forces it (B12).

**What this is not.** It is not v12: it carries no requirement map, no per-batch runtime, no context sets and
no `methodology-execute` boundary rows. v12's author takes §1 (the ordered list), §2 (the batch table, the waves
and the lane schedule), §5 (the file census) and §6 (tests owed) as given and adds those. Positions of workplan
v11 that a proposal names as a dependency (CR-, CP-T-, IN-, B10- ids, marked PL/PLAN/W in the read lanes) are
plan items, not code and not proposals; STAGES.md step 5 dispositions them, and this order treats each as
MISSING until that evaluation carries or retires it.

**Handles.** `B00` to `B41`; `B13` is unused (merged into `B12`, C3-D6). A handle is one batch with one close
(RULED 2026-11-06). Lane tags are the nine-lane roster of `tools/ci_common.py`; CHAR, CORE, DICE and tests
work is IN.

---

## 1. The ordered list (consume in this order; each batch's gate is an execution artifact read at its close)

Internal order is "→". "(part)" is a section of a proposal whose other sections land elsewhere (§4.1 names
which). Every batch: covering test files mid-batch (`python tools/tests_for_diff.py`), the full suite once at
its close (CLAUDE.md §0.4), `python -m engine.season.harness.register --check` and `--requirements` read and
recorded in the close, one re-pin at its last item where it declares movers (said plainly as a re-pin,
CLAUDE.md §7).

1. **B00 ids (IN).** No proposal. Allocate, on the working tree head and before any batch cites a number: a
   block of lane-tagged ED ids per batch from `references/id_reservations.yaml` `next_free` (bumped, co-committed);
   a block of hole-register ids beginning at the register's next free id (`H-363` at this read; the file has no
   H key, `U3_CONFLICT_LEDGER.md` T-4), split into per-batch sub-blocks, recorded in the close. Gate: `register --check` green; the bump is on the base every later batch starts from.
2. **B01 lane A (IN).** Rebase `e5d6ab9` and `c5bf18a` (branch `worktree-agent-a737f996de1fa4752`) onto the head
   after B00; resolve the 33 shared files toward the working tree (T-2); renumber the B11-A row from `H-275`
   (C3-A1). Lands `03_PC_duel_chain_reach.md`. Precondition: Jordan's word to push the branch
   (`U3_JORDAN_CALLS.md`, P-1). Gate: lane A's own: `aperture 2 s`, s = 0, 1, 2, before and after (`challenge`
   executed above 0; `exists:Person`, `dispute=False`, `exists:challenge` at 0 at formation), the planted-dispute
   run fires and its revert does not; same seed twice, same hash. Mover: every realm pin, re-recorded once.
3. **B02 tests (IN, hash EQUAL).** `01_CORE_tests_one_golden_owner` → `01_CORE_tests_delete_what_cannot_fail` →
   `U5a_tests_digest_additions` → `01_CORE_requirements_reading_record` (§1; §2 withdrawn, C-U5a-01) →
   `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` (R-01/R-02 `measure:`, C3-K5) →
   `16_PESSIMIST_GAME_consequence_reading` (a chronicle reading only) → `01_CORE_tests_shipped_world_falsifiers`
   (its R-09 row lands in B05). Gate: every pinned hash unchanged; each golden has one owner (`_realm_goldens.py`).
4. **B03 hygiene (IN, hash EQUAL).** `17_CENSUS_C1A_01` D1–D3 → `17_CENSUS_C1B_01`
   (its SC05-kernel item in B24) → `17_CENSUS_C1B_03` → `17_CENSUS_REST_1` (D2 in B11) →
   `16_PESSIMIST_CORE_no_stored_plan` → `09_WR_B_pointer_text_for_the_orchestrator` → `11_GO_pointer_and_stale_text_resolutions`
   (item 5 in B06) → `11_GO_design_reference_disposition` → `17_CENSUS_REST_3` (after the pointer file, whose row 8 it
   does not repeat; U6 R-A) → `06_FA_hygiene` (item 4 withdrawn: no mover; item 3 keeps `faction_q.holdings`, C3-V3) →
   `U5a_CORE_owed_edits` §A–C, E, F, I → `09_WR_threadwork_module` edit 3. Gate: content hash equal on every
   pinned world (`06_FA_hygiene`'s two movers left with its withdrawn item 4; U6 R-A); `tools/export_composition.py --check`; the deletions' greps.
5. **B04 capability home (IN, hash EQUAL).** Precondition: U1's capability architecture
   (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`, and U1's owner ledger when written). `U5a_capability_home_and_two_inputs`
   Part A → `01_CORE_capability_authoring_surface` → `02_CHAR_capability_definitions` → `02_CHAR_capability_uses_table`
   → `10_DICE_capability_axiom_map` (part one) → `05_SC_capability_surface` → `05_SC_hearing_capabilities`
   (definition rows; `hearing_moves` in B24) → `06_FA_office_capabilities` (ships none) → `29_DICE` row 1
   (`opposed_ob`, a function with no caller). *(U6 R-A, C3-V1: `10_DICE_one_score_two_roles` moved whole to B05, a
   declared mover in a hash-EQUAL batch.)* Gate: `tools/export_descriptors.py --check`;
   the NPC-088 headless hash equal to its post-B01 reading; `corpus_run` tallies unchanged.
6. **B05 one roll (IN, with SC, PC and MB edits; the calibrated landing; every seeded result re-pinned once).**
   `U5a_DICE_owed_edits` §1 rows 1–9 (row 4 is the field's sampler, `U5b_MB_rulings_in_the_field` §1, C3-D2; the
   margin quantised, C3-L1) → §2 (the wound as a level) → §3 → `10_DICE_one_roller_one_fraction_rule` (Edit C as
   designed with MB) → `10_DICE_exported_face_rule_and_band_edges` (A, D) → CAP Part B (lane A's `c5bf18a`
   folded, C3-A3) with `10_DICE_one_score_two_roles` edits A–C (OBS step 0; Edit A is CAP row B1, Edit B is row B4;
   C3-V1) → OBS step 1a carrying `05_SC_obstacle_difficulty_and_modifiers_B` → `16_PESSIMIST_SC_A` (1b) →
   `05_SC_contest_record_on_event` (2, with `U5c_SC_proceedings_residue` §1) → `13_SC_tuning_tables` commit 1 (3) →
   `13_SC_calibration` test, read red (4) → T13 commit 2, CAL green (5; the bench seats' `modifier:` held null until
   `L1-A12`, §1.4) → `05_SC_opposed_obstacle_parity` (0.4) →
   `16_PESSIMIST_DICE_soft_ceiling` → `16_PESSIMIST_DICE_task_difficulty_and_throughput` (code part) → `29_DICE`
   rows 2–4 and 8 → `U5b_PC_rulings_in_the_fight` §2–§3 (UPR §5 row 4) → `10_DICE_advantage_sources_for_the_arcs`
   → `10_DICE_believed_odds_have_a_prior` → `01_CORE_tests_shipped_world_falsifiers` R-09 row. Gate:
   `U5a_DICE_owed_edits` §1 gates (1)–(5); OBS's six gates; `13_SC_calibration` C1–C8 green (C1 at rank 7, C3-N6);
   `29_DICE` gates 2–4; CAP Part B's gate (equal opponents meet `plain` at 0.50 ± 0.005); the R-09 conjunct.
7. **B06 keyed draw (IN/GO; one re-pin).** `11_GO_float_contract` Part A (`fmath`, the leaf `draw.py` imports;
   U6 R-A) → `11_GO_one_draw_owner` with `16_PESSIMIST_GO_keyed_draw_no_recorder` (one commit pair: `H2` and `Draw.u`
   in `draw.py`, C3-V2 → `draw_factory` returns `seeded` → the two outside generators and the four fallbacks) →
   `11_GO_float_contract` Part B as C3-L3 (vectors) and Part C's text (owed, `L1-A29`) → `U5d_GO_owed_edits` →
   `11_GO_pointer…` item 5. Gate: same seed twice, same hash; `engine/tests/test_draw.py` (the scan with its three
   named harness controls, the `(key, n) → u` and sampler vectors held in the test) and `engine/tests/test_fmath.py`;
   the vectors' **export** round-trip moves to B41, which builds the exporter (§1.3).
8. **B07 task draw (IN; one re-pin).** `18_DETERMINISM_task_draw_for_uncontested_verbs` (the two loader refusals
   edited first, `25` G-01; item 4's shapes) → `U5c_VERBS_residue_and_governance_owner` §1–§2 →
   `U5b_VERBS_military_physical_residue` §1 → `13_SC_draw_for_unrolled_contests` (surviving rows). Gate: 18-A's
   five readings, the throughput reading among them (C-U5a-07); the loader accepts shapes (a) and (b) and refuses
   a band-keyed route row (planted).
9. **B08 scene order (IN; one re-pin).** `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` edits 1–4 (edit 5 is
   Layer 1 text owed; the live arm waits on `L1-A9`, §1.4) → `18_DETERMINISM_rival_acts_in_one_fold`. Gate: `interactions_per_scene = 1` equal; the
   four readings.
10. **B09 memory (IN).** `01_CORE_claim_fade_as_read` → `16_PESSIMIST_CORE_a_refusal_is_remembered` with
    `U5a_DICE_owed_edits` §4 and VRES §3 → `16_PESSIMIST_SC_B_one_reader_of_a_ledger` →
    `16_PESSIMIST_CORE_the_record_holds_what_changed` (`scar.taken` only) → `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`
    → `02_CHAR_reason_trail_and_small_edits` (Part A, the `watch` hook; B1 deleted, C3-L8) → `01_CORE_reason_trail_in_the_act_store`
    (reads Part A; U6 R-A) →
    `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` → `01_CORE_predicates_name_their_clause`. Gate: each
    file's readings; `refusal_memory = 0.0` equal.
11. **B10 character (IN).** `U5a_CHAR_owed_amendments` §2 (`stance_scale`, which the scar cap reads; U6 R-A) and its
    §4, §5, §7, §8 → `02_CHAR_scar_cap_and_regard_unit` with `02_CHAR_scar_is_a_wound` (one fixture) →
    `16_PESSIMIST_CHAR_A` (signature C3-K2) → `_CHAR_B` → `_CHAR_C` →
    `02_CHAR_resolve_and_temper` → `02_CHAR_goal_lean_on_its_own_question` → `02_CHAR_what_an_act_risks` →
    `02_CHAR_voices_and_the_room` (C3-D7) → `02_CHAR_choice_alignment` → `02_CHAR_offer_what_can_be_done` →
    `02_CHAR_relations_have_a_ground` → `U5a_CHAR_self_knowledge_is_a_belief` → `17_CENSUS_C1A_02` W3, W4 →
    `01_CORE_unmet_need_is_attended_first` → `12_ARCS_arcs_as_staged_goals` with `U5a_CHAR_owed_amendments` §3. Gate:
    each file's; `crisis_draw: off` equal.
12. **B11 FI readers (FI).** `U5c_FI_residue` → `08_FI_01` → `08_FI_02` (with VRES §6 and `audience_of`) → `08_FI_04`
    (with `17_CENSUS_REST_1` D2) → `08_FI_06` → `16_PESSIMIST_FI_A` → `16_PESSIMIST_SC_E` (C3-K1) →
    `16_PESSIMIST_FI_C` (`covert_kinds` members, C3-K6) → `18_DETERMINISM_notice_is_a_draw` → `14_VERBS_SOCIAL1_A`
    → `08_FI_03` → `08_FI_07` → `19_LACUNA_conclusion_is_a_committed_assertion`. Gate: each file's; planted worlds for notice.
13. **B12 world motion and ground (SE and WR together, C3-D6; re-ordered by U6 R-A, C3-V4, edges in §1.2).**
    `20_NARRATIVE_E` edit 1 (the year, C3-K11) → `09_WR_strand_conclusion` edits 1–3 (was missing from this list) →
    `09_WR_world_motion` edits 1–3 (the wound row and switch, the unheld seizure, the settled selector) →
    `09_WR_B_draws_not_thresholds` edits 1–3 (drawn wear and drawn endings on that row and selector) →
    `07_SE_kernel_repairs` → `07_SE_ground_and_granaries` with `07_SE_treasury_granary_B` →
    `16_PESSIMIST_GAME_the_world_draws` → `16_PESSIMIST_WR_B` edits 1–2 with `U5d_WR_owed_edits` §2 (a), §3, §4 →
    `09_WR_world_motion` edit 1's `lattice_coupling` flip (its own commit) → `09_WR_B_weather_with_memory_and_the_year`
    (year and spell) → `16_PESSIMIST_WR_A_the_road_is_drawn` → `09_WR_provided_arcs` → `07_SE_arc_needs` →
    `16_PESSIMIST_SE_B` → `U5d_SE_owed_edits` → `07_SE_population_census` (thinning at MATTER, C3-C3) with
    `07_SE_population_regrowth_B` → `16_PESSIMIST_SE_A` → `14_VERBS_MATERIAL_A` (owner of `tend`) → `_MATERIAL_B` →
    `_MATERIAL_C` → `07_SE_capability_rate_B` (C3-C2) → `07_SE_capability_and_chooser_surface` §5–§6 →
    `07_SE_valley_scenario`. Gate: controls equal; each flip its own declared mover; the valley loader test.
14. **B14 PC outcome (PC).** `03_PC_typed_outcome_one_door` (C3-L5) → `03_PC_weapon_records_in_the_export` →
    `03_PC_weapon_form_at_round_start` → `16_PESSIMIST_PC_C` → `U5b_PC_residue` §7–§8 → `14_VERBS_PHYSICAL_A` A4.
    Gate: `tools/export_engine_params.py --check`; two declared movers (`standing`, `fell_to`).
15. **B15 PC calibration (PC; one re-record of combat goldens, the armour reference and the export).** UPR §4 (the
    scale) → `16_PESSIMIST_PC_B` → `16_PESSIMIST_PC_D` → `14_VERBS_PHYSICAL_A` A3 (in `modules/combat/`, C3-C8;
    `22_HAPPENINGS_A` edit 3's `mortal_terms` lands here; moved ahead of the two files that depend on it, U6 R-A,
    UPR §5 row 5 edited to match) → `18_DETERMINISM_no_certain_matchup` → `16_PESSIMIST_PC_A` → UPR §3's flip;
    `29_DICE` rows 5–7, 9. Gate: `29_DICE` gates (a)–(c); each step's own gate read before the next.
16. **B16 PC round (PC).** `03_PC_duel_round_and_approach_B` steps 1–2 (round keys, A-30) → 3a, 3b, 3e, 3c at 0 →
    step 4 with `03_PC_exits_withdrawal_recovery` Part A; `03_PC_duel_round_and_approach` marked superseded.
    Gate: PB's per-step gates and the added R-6 gate.
17. **B17 MB scale (MB).** `04_MB_headcount_grade_and_scale` (the `Drawn` re-homing, A-67 to A-70) →
    `04_MB_typed_outcome_and_one_path` §1, §2, §4 with `U5b_MB_residue` §1 → `04_MB_unit_loadout_and_weapon_in_hand_B`
    stages 1–2 (creates `references/troops.yaml` and `tools/export_troops.py`; `04_MB_unit_loadout_and_weapon_in_hand`
    superseded) → `04_MB_typed_outcome_and_one_path` §3 (moves table content into the troop file; it needs the file
    and its exporter, U6 R-A). Gate: the troop exporter's `--check`; seed 2's pin moved and re-recorded.
18. **B18 PC content (PC).** `U5b_PC_residue` §3 census → `03_PC_person_inputs_content` Parts B–D → `03_PC_loadout_and_carry`.
19. **B19 MB field calibration (MB; one re-record).** `26_MASS_BATTLE_calibration_targets`' T-rows written first as
    the batch's tests (§6.1 rule; 27C reads its "results" block) → `27_MB_A` 27A-1 to 27A-4 with `27_MB_C` 27C-1 (the
    named draws, UMR §6 row 4) → `16_PESSIMIST_MB_one_stamina_ledger` 1–2 →
    `04_MB_cr12_linear_law` 1–3 with `16_PESSIMIST_MB_partition_and_the_pair_rule` 2–4 → `04_MB_cell_hierarchy_as_data`
    with `26_MASS_BATTLE_cell_scale_and_time` → `27_MB_A`'s window and lull actions (on cell-scale §3; U6 R-A) →
    `26_MASS_BATTLE_rout_pursuit_and_giving_ground` with `16_PESSIMIST_MB_rout_has_two_exits` → UMR §4–§6 → 27C-2's
    table and 27C-3 (the multiplier; zero if the first arm passes, A-77; 27C-3 (h) edits the LINEAR band, C3-C6) in
    the one re-record → `26_MASS_BATTLE_calibration_targets` read last. Gate:
    `26_MASS_BATTLE_calibration_targets` T-rows; twice the men win; `lanchester_signature.py` as edited.
20. **B20 MB orders (MB).** `04_MB_manager_battle_one_resolver` §2–§6 with `26_MASS_BATTLE_maneuver_orders` →
    `04_MB_playable_field_scenario` A, C, D → `27_MB_D` → `17_CENSUS_REST_2` W1.
21. **B21 FA governance (FA).** The order of C3-D5, with three moves by U6 R-A (edges in §1.2): `06_FA_seat_terms_and_turnover`
    → `06_FA_remit_grant_by_row` → `06_FA_seat_terms_by_body_B` → `14_VERBS_BINDING_A` → `U5d_FA_owed_edits` §2
    (custody) → `14_VERBS_BINDING_C` at control (its `revoke`/`succeed` draws, `rank_step` 0 until `L1-A12`) →
    `22_HAPPENINGS_B` edits 1–2 (moved after BIND_C: it "binds on" BIND_C's `succeed` draw, `22_HAPPENINGS_B…:8`, `:19`)
    → `06_FA_decree_binds` edits 1–2 → `16_PESSIMIST_FA_C` (the command predicate) → `06_FA_decree_binds` edit 3 (who
    is bound reads the predicate, A-22) → `16_PESSIMIST_FA_A` (after HAP_B, C3-K9) → `14_VERBS_BINDING_D` →
    `06_FA_war_lives_in_seats_B` edits 1–3 → `06_FA_levy_through_the_seat_B` → `16_PESSIMIST_FA_B` → the rest of
    `U5d_FA_owed_edits` → `06_FA_playable_scenario` → `14_VERBS_BINDING_C`'s flip (moved after the scenario its
    Depends line names) → `06_FA_shortest_loop_B`.
22. **B22 MB armies (MB).** `27_MB_E` (C3-L11; the loss ledger MILITARY_A, _C and _D read, moved first by U6 R-A) →
    `14_VERBS_MILITARY_A` → `_MILITARY_B` → `07_SE_campaign_supply_and_muster` with `U5b_MB_residue`'s realm item
    (moved ahead of the muster that names it) → `_MILITARY_C` (e6 per C3-L11) → `_MILITARY_D` →
    `14_VERBS_PHYSICAL_B` → `04_MB_playable_field_scenario` §E → RES-V §4 → `17_CENSUS_C1A_02` W2 rows for these verbs.
23. **B23 land (FA).** `06_FA_war_lives_in_seats_B` edit 6 → `U5d_FA_land_and_seats_pass_on_a_won_march` (C3-L7,
    C3-L12) → `14_VERBS_MATERIAL_D` §6 (`seize`) → `26_MASS_BATTLE_aggression_and_land` → RES-V §2–§3 → UMR §2 →
    `14_VERBS_BINDING_E`. Gate: the land proposal's arms a–i; a won march followed by `seize` moves the land and
    its anchored seats; a draw re-homes both armies; a won march with no `seize` moves no title.
24. **B24 SC hearing (SC).** `05_SC_playable_hearing_B` → `19_LACUNA_admission_rides_the_citing_draw` →
    `05_SC_evidence_and_rebuttal_B` (C3-C1) → `08_FI_05_evidence-interface_B` → `05_SC_hearing_capabilities`
    `hearing_moves` → `05_SC_negotiation_scene` → `05_SC_sc05_kernel_disposition_B` with `17_CENSUS_C1B_01`'s kernel
    item → `12_ARCS_cited_evidence` → `02_CHAR_which_ground_moves_whom` → VRES §2 hearing rows → `17_CENSUS_REST_2`
    W2; the three superseded SC/FI files marked. Gate: `build_hearing`; `sitting_exchanges` leaves 0.
25. **B25 FI questioning (FI).** `14_VERBS_SOCIAL2_A` → `_B` → `_C` → `_A` edit 2 (and `14_VERBS_MATERIAL_C`'s
    `research` pair) → `08_FI_08_knots-season-form` §2–§3 → `_D` (`tie`, the verb roster 67 → 68; after FI_08 §3 as its
    own Lands line says, U6 R-A). Gate: the roster
    count read by command, not typed.
26. **B26 FI inquiry (FI).** `19_LACUNA_questioning_has_an_approach_and_a_cost` → `16_PESSIMIST_FI_B` →
    `16_PESSIMIST_FI_D` → `14_VERBS_MATERIAL_D` (not §6) → `_MATERIAL_E` → `14_VERBS_PHYSICAL_C`.
27. **B27 SC proceedings (SC).** `05_SC_acquittal` → `05_SC_arrangement_rows_that_bind` → `16_PESSIMIST_SC_C` →
    `16_PESSIMIST_SC_D` → `U5c_SC_proceedings_residue`'s remaining sections (its own Depends line names SC_C and SC_D;
    §1 landed in B05, §2 and §6 in B24; §3 and §8 part 2 stay design-first, unscheduled, per its Lands line; U6 R-A) → `19_LACUNA_verdict_ladder_and_reversal` (its chronicle line in B36).
28. **B28 social verbs (SC).** `14_VERBS_SOCIAL1_B` → `_SOCIAL1_D` (the challenge spent, C3-A4) → `_SOCIAL1_C` (after
    `_D`, as its own Lands line says; U6 R-A) →
    `28_CORE_scene_access_A` (the person key at control, C3-K8) → `28_CORE_scene_access_B`. Gate: 28A's twelve rows
    with their named tests (§6.1 lists them as owed).
29. **B29 PC custody (PC).** `14_VERBS_PHYSICAL_A` A1–A2 (custody, capture, arrest).
30. **B30 MB nested (MB).** UPR §1 (the nested entry, cap 1, A-72) → PB step 5 → `04_MB_manager_battle_one_resolver`
    §7 → `04_MB_squad_grid_of_named_characters` → UMR §3 → `29_DICE` item 29-5 (`DuelRoundInput` from PB,
    `HearingInput` and `Speaker` from HEAR_B now exist).
31. **B31 MB loadout and economy (MB).** `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4 →
    `26_MASS_BATTLE_movement_and_fatigue_as_data` → stamina step 3 → `04_MB_campaign_party_economy` with UMR §5 → `27_MB_B`.
32. **B32 institutions kit (FA).** `15_INSTITUTIONS_COLONIAL_A` → `_SYNTHESIS_A` → `_SYNTHESIS_B` (the ledger reader;
    prehistory in B39) → `22_HAPPENINGS_B` edit 3 → `_BYZANTINE_A` → `_BYZANTINE_E` → `_PAPACY_A` → `_PAPACY_B`
    (two electors) → `14_VERBS_BINDING_B` → `_VENICE_C` with `16_PESSIMIST_FA_B`'s `may_seat` edit →
    `17_CENSUS_REST_2` W5 → `U5d_FA_owed_edits`'s papacy section.
33. **B33 institutions economy and hands (FA).** `_BYZANTINE_B` → `_C` → `_D` → `_COLONIAL_B` → `_C` → `_D` →
    `_PAPACY_C` → `_D` → `_E` (item 5 deleted, A-36) → `_VENICE_A` → `_B` → `_D` → `_SYNTHESIS_C`.
34. **B34 GO surface (GO).** `11_GO_player_surface_contract_B` (C3-L4) → `11_GO_player_surface_contract` (superseded;
    §2 `explain` kept live) → `11_GO_fidelity_and_campaign_modes` → `16_PESSIMIST_GO_the_offer_names_what_is_held` →
    `01_CORE_one_scene_contract` → `U5a_CORE_owed_edits`' GO-B §8 item → `17_CENSUS_C1A_02` W1.
35. **B35 WR thread (WR).** `09_WR_B_threadwork_session_and_practitioner` → `14_VERBS_PHYSICAL_D` with
    `17_CENSUS_REST_2` W3 → `08_FI_08` §1, §4 → `U5d_WR_zero_coherence_unknowable` → `12_ARCS_substrate_as_ground`
    (C3-C14; it names the zero-coherence file among its Depends, U6 R-A).
36. **B36 WR story instruments (WR).** `09_WR_story_instruments_that_can_fail` → `09_WR_B_readings_of_closure_and_tension`
    with `09_WR_B_chronicle_that_tells` (and the verdict ladder's chronicle line) → `16_PESSIMIST_WR_D` →
    `20_NARRATIVE_F` (its `stands_for` clause in B38) → `23_STORY_D` → `17_CENSUS_C1B_02` (not W-2). `harness/storybar.py` serially (C3-K7).
37. **B37 happenings (IN).** `22_HAPPENINGS_A` (ages, the bout; `mortal_terms` already in B15) with
    `16_PESSIMIST_WR_C` reduced (C3-K4) and `U5d_WR_owed_edits` §2 (c) → `22_HAPPENINGS_C` with UPR §6 →
    `22_HAPPENINGS_D`.
38. **B38 narrative and regimes (WR).** `20_NARRATIVE_A` (with `20_NARRATIVE_F`'s clause; flips CHAR_A's `reading`) →
    `20_NARRATIVE_C` (moved first of the three: NARR_B and 28C each say it "lands first"; U6 R-A) → `20_NARRATIVE_B`
    (carrying `30_WR_D` commit 1) → `28_CORE_scene_access_C` (C3-D8) → `20_NARRATIVE_D` commit 1 → `20_NARRATIVE_E`
    (not edit 1) → `30_WR_B` → `30_WR_G` → `31_WR_A` (its commit 4, the `creed:` values) → `20_NARRATIVE_D`'s later
    commits → `31_WR_B` (C3-L6; `sway_gain` 0 until `L1-A92`) → `30_WR_A` (with `09_WR_B_draws` edit 4 and the
    weather's era part) → `30_WR_C` → `23_STORY_A` (C3-L14) → `30_WR_D` → `30_WR_E` → `30_GO_F` → `31_WR_C` (moved
    after `30_GO_F`, which its Depends names; U6 R-A) → `U5d_SE_cohort_heavy_moves_and_caste`.
39. **B39 procedural generation and cases (WR).** `21_PROCEDURAL_A` → `_B` → `_E` → `21_PROCEDURAL_C` (the prologue and
    its year) → `01_CORE_case_setup_and_beats` (the base `12_ARCS_case_on_the_realm.md:7` names) → `12_ARCS_case_on_the_realm`
    (U6 R-A: the three were "with", now ordered by `12_ARCS`'s own Depends line) → `_D` → `U5d_STORY_owed_edits` → `23_STORY_B` →
    `23_STORY_C` → `23_STORY_E`; the split parts of `15_INSTITUTIONS_SYNTHESIS_B`, `_COLONIAL_D`,
    `17_CENSUS_C1B_02` W-2, `U5d_FA_owed_edits` and `30_WR_A` that need these.
40. **B40 institutions scenarios (FA).** `15_INSTITUTIONS_SYNTHESIS_D` → `_BYZANTINE_F` → `_COLONIAL_E` →
    `_PAPACY_F` (each with A-80's entrenched-world arm, C3-C12) → the four grounding files in the order
    `_BYZANTINE_grounding` → `_VENICE_grounding_E` → `_COLONIAL_grounding_F` (which names VENICE_grounding_E edits 1
    and 3 among its Depends; U6 R-A) → `_PAPACY_grounding` → `_SYNTHESIS_E`.
41. **B41 GO port gate (GO; after `L1-A29` and `L1-A30`, §1.4).** `16_PESSIMIST_GO_surface_pins` (GO-08 builds
    `tools/export_oracle_pins.py` and `harness/port_oracle.py`) → `11_GO_port_gate_order_and_coverage`. Gate: the
    pins and vectors it names, **including the B06 `fmath` and `(key, n) → u` vectors' export round-trip moved here**
    (`export_oracle_pins.py --check` reds on an edited vector; §1.3); no draw or float log (C3-L3).

### 1.1 Rules for running batches at once (STAGES.md "Parallel sessions", applied to this graph)

- **One open batch per lane.** The IN lane holds B00 to B10 and B37, so the spine is serial whatever the waves
  say; parallelism begins at B14 (PC) beside B06 (§2.3).
- **Hash movers.** Almost every batch moves seeded pins. Two batches open at once that both move pins merge in
  handle order; the later rebases on the earlier's merge and re-pins once, quoting the earlier's after-reading as
  its baseline (`reading @<sha>`). Hash-equal batches (B02, B03 except its two movers, B04) need no re-pin.
- **The hot files.** Sixteen files are edited by twenty or more proposals (§5.1; the first ten: `rosters.yaml` 130,
  `fixtures.py` 91, `world_q.py` 81, `verb_table.yaml` 66, `person_q.py` 53, `effects_information.py` 32,
  `options.py` 31, `inputs.py`, `populated.py` and `sigma.py` 29 each). Two open batches may edit one of them only in different
  top-level keys or functions; the merge keeps both edits by hand in handle order and never regenerates the file.
  An append-only register (`hole_register.yaml`, `requirements.yaml`) takes each batch's rows from its pre-allocated
  block (B00).
- **Serial instrument files.** `harness/storybar.py` (C3-K7), `loop/resolve.py::_canonical_order` (C3-K8),
  `decision/choose.py::_stance_arm` (C3-K3) and `loop/witness.py::_told_value` (C3-K1) are edited by one batch
  at a time, in the order named in the ledger.

### 1.2 Intra-batch order and every within-batch edge (U6 repair lane R-A)

The batch graph of §2 was checked acyclic between batches only (`U6_VERDICT_AND_REPAIRS.md` finding 2). This
section checks inside each batch. **Source:** every edge of §3.1 whose two ends sit in one batch and that §4.1 does
not cut, extracted by script from §3.1 (scratch, not committed) and laid against the order of §1 as edited by this
lane. **Reading:** each batch lists its items in landing order (a split node appears where its part lands); after an
item, each of its within-batch dependencies is marked ✓ (lands earlier) or carries its disposition. Dispositions:
**two-way citation** (the read lanes recorded both directions, §0; the pair co-lands in this order); **met by an earlier
part** (the needed part landed in an earlier batch or an earlier step); **split** (only a later part of the dependent
waits, placed after the target); **same step**, **co-land**; **cut CITE** (the dependent names the target without
needing it to land first, quoted); **cut REV** (the target composes on the dependent, quoted); **cut LATER** (the
dependent's own Lands line puts it first and the target only widens it). Moves made by this lane, each with its
reason, are marked "U6 R-A" in §1. **Not seen by this check:** a dependency a proposal's own `Depends on` line names
but the read lane's §3.1 row omits (one found and added: `27_MB_C` 27C-1 on `04_MB_manager_battle_one_resolver` §6,
§4.1 row 91); a proposal's internal part order.

- **B02.** 1. `01_CORE_tests_one…` · 2. `01_CORE_tests_delete…` · 3. `U5a_tests_digest…` · 4. `01_CORE_requirements…` · 5. `16_PESSIMIST_CORE_the_nine…`: needs `01_CORE_requirements…` ✓ · 6. `16_PESSIMIST_GAME_consequence…`: needs `01_CORE_requirements…` ✓ · 7. `01_CORE_tests_shipped…`: needs `01_CORE_requirements…` ✓
- **B03.** 1. `17_CENSUS_C1A_01…`: needs `06_FA_hygiene` (cut CITE: C1A_01 names the hygiene item only to exclude it from its own list (`:112`)) · 2. `17_CENSUS_C1B_01…`: needs `09_WR_threadwork…` (cut CITE: a co-landing text correction (C1B_01 `:7`), no landing dependency) · 3. `17_CENSUS_C1B_03…` · 4. `17_CENSUS_REST_1…`: needs `17_CENSUS_C1B_01…` ✓ · 5. `16_PESSIMIST_CORE_no…` · 6. `09_WR_B_pointer…` · 7. `11_GO_pointer…` · 8. `11_GO_design…`: needs `11_GO_pointer…` ✓ · 9. `17_CENSUS_REST_3…`: needs `11_GO_pointer…` ✓ · 10. `06_FA_hygiene` · 11. `U5a_CORE_owed…` · 12. `09_WR_threadwork…`
- **B04.** 1. `U5a_capability_home…` · 2. `01_CORE_capability…`: needs `10_DICE_capability…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `02_CHAR_capability_definitions` · 4. `02_CHAR_capability_uses…` · 5. `10_DICE_capability…`: needs `U5a_capability_home…` ✓; `01_CORE_capability…` ✓; `02_CHAR_capability_uses…` ✓ · 6. `05_SC_capability…` · 7. `05_SC_hearing…` · 8. `06_FA_office…`: needs `U5a_capability_home…` ✓; `05_SC_hearing…` ✓ · 9. `29_DICE_one…`
- **B05.** 1. `U5a_DICE_owed…` · 2. `U5b_MB_rulings…` · 3. `10_DICE_one_roller…`: needs `U5a_DICE_owed…` ✓ · 4. `10_DICE_exported…`: needs `U5a_DICE_owed…` ✓ · 5. `U5a_capability_home…` · 6. `10_DICE_one_score…`: needs `U5c_SC_one…` (same step: these edits ARE OBS §4 step 0); `29_DICE_one…` (met by item 29-1 in B04) · 7. `U5c_SC_one…`: needs `05_SC_contest…` (OBS is the step frame: SC-P1 is its step 2); `13_SC_tuning…` (OBS is the step frame: T13 is its steps 3 and 5); `29_DICE_one…` (met by item 29-1 in B04; rows 2–4 after CAL) · 8. `05_SC_obstacle…`: needs `U5c_SC_one…` ✓ · 9. `16_PESSIMIST_SC_A…`: needs `05_SC_obstacle…` ✓; `13_SC_tuning…` (cut LATER: SC_A's own Lands line (`:15`) and OBS §4 put it at step 1b, T13 at step 3 with members at 0) · 10. `05_SC_contest…`: needs `U5c_SC_one…` ✓ · 11. `13_SC_tuning…`: needs `U5c_SC_one…` ✓ · 12. `13_SC_calibration`: needs `U5c_SC_one…` ✓; `13_SC_tuning…` ✓; `29_DICE_one…` (met by item 29-1 in B04 (mutual; 29_DICE rows 2–4 read CAL)) · 13. `05_SC_opposed…`: needs `U5c_SC_one…` ✓; `29_DICE_one…` (met by item 29-1 in B04) · 14. `16_PESSIMIST_DICE_soft…`: needs `U5a_DICE_owed…` ✓; `05_SC_obstacle…` ✓ · 15. `16_PESSIMIST_DICE_task…`: needs `05_SC_obstacle…` ✓; `13_SC_tuning…` ✓ · 16. `29_DICE_one…`: needs `U5c_SC_one…` ✓; `13_SC_calibration` ✓ · 17. `U5b_PC_rulings…` · 18. `10_DICE_advantage…` · 19. `10_DICE_believed…` · 20. `01_CORE_tests_shipped…`
- **B06.** 1. `11_GO_float…` · 2. `11_GO_one…`: needs `11_GO_float…` ✓; `16_PESSIMIST_GO_keyed…` (one commit pair (C3-Y10): `H2` and `Draw.u` first) · 3. `16_PESSIMIST_GO_keyed…`: needs `11_GO_one…` ✓ · 4. `U5d_GO_owed…`: needs `11_GO_float…` ✓; `16_PESSIMIST_GO_keyed…` ✓ · 5. `11_GO_pointer…`
- **B07.** 1. `18_DETERMINISM_task…` · 2. `U5c_VERBS_residue…`: needs `18_DETERMINISM_task…` ✓ · 3. `U5b_VERBS_military…`: needs `18_DETERMINISM_task…` ✓; `U5c_VERBS_residue…` ✓ · 4. `13_SC_draw…`
- **B08.** 1. `16_PESSIMIST_CORE_a_scene…`: needs `18_DETERMINISM_rival…` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `18_DETERMINISM_rival…`: needs `16_PESSIMIST_CORE_a_scene…` ✓
- **B09.** 1. `01_CORE_claim…` · 2. `16_PESSIMIST_CORE_a_refusal…`: needs `01_CORE_claim…` ✓ · 3. `16_PESSIMIST_SC_B…`: needs `01_CORE_claim…` ✓ · 4. `16_PESSIMIST_CORE_the_record…` · 5. `16_PESSIMIST_GAME_standing…`: needs `01_CORE_reason…` (cut CITE: "compatible and independent" (GAME `:130`)) · 6. `02_CHAR_reason…` · 7. `01_CORE_reason…`: needs `02_CHAR_reason…` ✓ · 8. `16_PESSIMIST_GO_a…` · 9. `01_CORE_predicates…`
- **B10.** 1. `U5a_CHAR_owed…`: needs `12_ARCS_arcs…` (co-land: U5a_CHAR §3 lands with 12_ARCS at the batch end) · 2. `02_CHAR_scar_cap…`: needs `U5a_CHAR_owed…` ✓; `02_CHAR_scar_is…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `02_CHAR_scar_is…`: needs `02_CHAR_scar_cap…` ✓ · 4. `16_PESSIMIST_CHAR_A…`: needs `02_CHAR_scar_cap…` ✓; `02_CHAR_scar_is…` ✓ · 5. `16_PESSIMIST_CHAR_B…`: needs `U5a_CHAR_owed…` ✓ · 6. `16_PESSIMIST_CHAR_C…`: needs `U5a_CHAR_owed…` ✓; `16_PESSIMIST_CHAR_B…` ✓ · 7. `02_CHAR_resolve…`: needs `U5a_CHAR_owed…` ✓ · 8. `02_CHAR_goal…` · 9. `02_CHAR_what…` · 10. `02_CHAR_voices…` · 11. `02_CHAR_choice…` · 12. `02_CHAR_offer…` · 13. `02_CHAR_relations…`: needs `U5a_CHAR_owed…` ✓ · 14. `U5a_CHAR_self…` · 15. `17_CENSUS_C1A_02…`: needs `U5a_CHAR_owed…` ✓; `02_CHAR_scar_cap…` ✓ · 16. `01_CORE_unmet…`: needs `02_CHAR_goal…` ✓ · 17. `12_ARCS_arcs…`
- **B11.** 1. `U5c_FI_residue` · 2. `08_FI_01…` · 3. `08_FI_02…`: needs `U5c_FI_residue` ✓ · 4. `08_FI_04…` · 5. `08_FI_06…` · 6. `16_PESSIMIST_FI_A…`: needs `08_FI_02…` ✓; `08_FI_06…` ✓ · 7. `16_PESSIMIST_SC_E…` · 8. `16_PESSIMIST_FI_C…`: needs `08_FI_01…` ✓; `08_FI_02…` ✓ · 9. `18_DETERMINISM_notice…` · 10. `14_VERBS_SOCIAL1_A…`: needs `08_FI_02…` ✓ · 11. `08_FI_03…`: needs `U5c_FI_residue` ✓ · 12. `08_FI_07…`: needs `08_FI_06…` ✓; `08_FI_03…` ✓ · 13. `19_LACUNA_conclusion…`: needs `U5c_FI_residue` ✓; `08_FI_03…` ✓
- **B12.** 1. `20_NARRATIVE_E…` · 2. `09_WR_strand…` · 3. `09_WR_world…`: needs `09_WR_B_draws…` (cut REV: the draws file re-mechanises world_motion edits 1 and 3 on their row and selector (draws `:21-24`); world_motion first); `16_PESSIMIST_WR_B…` (split: only edit 1's `lattice_coupling` flip waits; it lands after WR_B edits 1–2) · 4. `09_WR_B_draws…`: needs `09_WR_strand…` ✓; `09_WR_world…` ✓ · 5. `07_SE_kernel…` · 6. `07_SE_ground…`: needs `07_SE_treasury…` (two-way citation: co-lands in this order, the reverse edge kept) · 7. `07_SE_treasury…`: needs `07_SE_ground…` ✓ · 8. `16_PESSIMIST_GAME_the…`: needs `09_WR_B_draws…` ✓; `07_SE_ground…` ✓ · 9. `16_PESSIMIST_WR_B…`: needs `09_WR_world…` ✓; `16_PESSIMIST_GAME_the…` ✓; `U5d_WR_owed…` (two-way citation: co-lands in this order, the reverse edge kept) · 10. `U5d_WR_owed…`: needs `16_PESSIMIST_WR_B…` ✓ · 11. `09_WR_B_weather…` · 12. `16_PESSIMIST_WR_A…`: needs `07_SE_kernel…` ✓; `09_WR_B_weather…` ✓ · 13. `09_WR_provided…` · 14. `07_SE_arc…` · 15. `16_PESSIMIST_SE_B…`: needs `09_WR_B_draws…` ✓; `07_SE_treasury…` ✓ · 16. `U5d_SE_owed…`: needs `16_PESSIMIST_SE_B…` ✓ · 17. `07_SE_population_census`: needs `09_WR_B_draws…` ✓; `07_SE_population_regrowth…` (two-way citation: co-lands in this order, the reverse edge kept) · 18. `07_SE_population_regrowth…`: needs `07_SE_population_census` ✓ · 19. `16_PESSIMIST_SE_A…`: needs `07_SE_ground…` ✓; `07_SE_treasury…` ✓; `16_PESSIMIST_GAME_the…` ✓; `07_SE_population_census` ✓ · 20. `14_VERBS_MATERIAL_A…`: needs `07_SE_kernel…` ✓ · 21. `14_VERBS_MATERIAL_B…`: needs `07_SE_kernel…` ✓; `07_SE_treasury…` ✓; `07_SE_arc…` ✓; `14_VERBS_MATERIAL_A…` ✓ · 22. `14_VERBS_MATERIAL_C…`: needs `14_VERBS_MATERIAL_A…` ✓ · 23. `07_SE_capability_rate…` · 24. `07_SE_capability_and…`: needs `07_SE_capability_rate…` ✓ · 25. `07_SE_valley…`
- **B14.** 1. `03_PC_typed…` · 2. `03_PC_weapon_records…` · 3. `03_PC_weapon_form…` · 4. `16_PESSIMIST_PC_C…`: needs `03_PC_typed…` ✓ · 5. `U5b_PC_residue` · 6. `14_VERBS_PHYSICAL_A…`
- **B15.** 1. `U5b_PC_rulings…`: needs `14_VERBS_PHYSICAL_A…` (split: UPR §3's flip (after A3) is the part that reads A3; §4 heads the batch) · 2. `16_PESSIMIST_PC_B…` · 3. `16_PESSIMIST_PC_D…`: needs `18_DETERMINISM_no…` (cut REV: PC_D's Lands line (`:14`) orders it before the riposte; its Depends names only `draw.py` and the A-31 scale) · 4. `14_VERBS_PHYSICAL_A…` · 5. `22_HAPPENINGS_A…` · 6. `18_DETERMINISM_no…`: needs `14_VERBS_PHYSICAL_A…` ✓ · 7. `16_PESSIMIST_PC_A…`: needs `14_VERBS_PHYSICAL_A…` ✓ · 8. `29_DICE_one…`
- **B16.** 1. `03_PC_duel_round_and_approach_B`: needs `03_PC_duel_round_and_approach` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `03_PC_exits…` · 3. `03_PC_duel_round_and_approach`: needs `03_PC_duel_round_and_approach_B` ✓
- **B17.** 1. `04_MB_headcount…` · 2. `04_MB_typed…`: needs `04_MB_headcount…` ✓ · 3. `U5b_MB_residue` · 4. `04_MB_unit_loadout_and_weapon_in_hand_B` · 5. `04_MB_unit_loadout_and_weapon_in_hand`
- **B18.** 1. `U5b_PC_residue` · 2. `03_PC_person…` · 3. `03_PC_loadout…`
- **B19.** 1. `26_MASS_BATTLE_calibration…` · 2. `27_MB_A…`: needs `26_MASS_BATTLE_cell…` (split: 27A-1–4 need nothing; the window and lull actions land after cell-scale §3 (27_MB_A `:5`)) · 3. `27_MB_C…`: needs `26_MASS_BATTLE_calibration…` ✓; `27_MB_A…` ✓; `U5b_MB_rulings…` (met by UMR §1 (B05) for 27C-1; 27C-2/27C-3 land after UMR §4–§6) · 4. `16_PESSIMIST_MB_one…` · 5. `04_MB_cr12…`: needs `16_PESSIMIST_MB_partition…` (two-way citation: co-lands in this order, the reverse edge kept); `U5b_MB_rulings…` (met by UMR §1 in B05 (the one sampler, C3-D2)) · 6. `16_PESSIMIST_MB_partition…`: needs `04_MB_cr12…` ✓; `U5b_MB_rulings…` (met by UMR §1 in B05 (the one sampler, C3-D2)) · 7. `04_MB_cell…`: needs `16_PESSIMIST_MB_partition…` ✓ · 8. `26_MASS_BATTLE_cell…`: needs `04_MB_cell…` ✓ · 9. `26_MASS_BATTLE_rout…`: needs `16_PESSIMIST_MB_rout…` (two-way citation: co-lands in this order, the reverse edge kept) · 10. `16_PESSIMIST_MB_rout…`: needs `27_MB_A…` ✓; `26_MASS_BATTLE_rout…` ✓ · 11. `U5b_MB_rulings…`
- **B20.** 1. `04_MB_manager…` · 2. `26_MASS_BATTLE_maneuver…`: needs `04_MB_manager…` ✓ · 3. `04_MB_playable…` · 4. `27_MB_D…`: needs `04_MB_manager…` ✓ · 5. `17_CENSUS_REST_2…`
- **B21.** 1. `06_FA_seat_terms_and…` · 2. `06_FA_remit…`: needs `22_HAPPENINGS_B…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `06_FA_seat_terms_by…`: needs `06_FA_seat_terms_and…` ✓; `06_FA_remit…` ✓ · 4. `14_VERBS_BINDING_A…` · 5. `U5d_FA_owed…`: needs `14_VERBS_BINDING_C…` (split: §2 (custody) early per C3-D5; the other sections after FA_B [ASSUMPTION: §2 reads neither BIND_C nor BIND_D — basis: C3-D5 placed it before both]); `22_HAPPENINGS_B…` (split, as the row above); `14_VERBS_BINDING_D…` (split, as the row above) · 6. `14_VERBS_BINDING_C…`: needs `06_FA_seat_terms_and…` ✓; `06_FA_remit…` ✓; `14_VERBS_BINDING_A…` ✓; `06_FA_decree…` (two-way citation: co-lands in this order, the reverse edge kept); `06_FA_playable…` (split: BIND_C's flip moves after the scenario [ASSUMPTION: the scenario is BIND_C's gate world — basis: BIND_C `:11` Depends and `:18` sources; no BIND_C edit names a symbol the scenario creates]) · 7. `22_HAPPENINGS_B…`: needs `06_FA_remit…` ✓; `14_VERBS_BINDING_C…` ✓; `16_PESSIMIST_FA_A…` (two-way citation: co-lands in this order, the reverse edge kept) · 8. `06_FA_decree…`: needs `U5d_FA_owed…` ✓; `14_VERBS_BINDING_C…` ✓; `16_PESSIMIST_FA_C…` (split: decree edits 1–2 before FA_C, edit 3 (who is bound, A-22) after it) · 9. `16_PESSIMIST_FA_C…`: needs `06_FA_decree…` ✓; `14_VERBS_BINDING_D…` (cut REV: FA_C owns the command predicate and lands before BIND_D, which composes on it (FA_C `:10-12`, `:22`)); `06_FA_levy…` (cut REV: the levy reads FA_C's two predicates (FA_C `:30`)) · 10. `16_PESSIMIST_FA_A…`: needs `06_FA_seat_terms_and…` ✓; `14_VERBS_BINDING_C…` ✓; `22_HAPPENINGS_B…` ✓; `06_FA_decree…` ✓ · 11. `14_VERBS_BINDING_D…`: needs `06_FA_remit…` ✓; `06_FA_decree…` ✓ · 12. `06_FA_war…` · 13. `06_FA_levy…` · 14. `16_PESSIMIST_FA_B…`: needs `06_FA_remit…` ✓; `14_VERBS_BINDING_C…` ✓ · 15. `06_FA_playable…`: needs `06_FA_seat_terms_and…` ✓; `22_HAPPENINGS_B…` ✓; `06_FA_decree…` ✓ · 16. `06_FA_shortest…`: needs `06_FA_decree…` ✓; `06_FA_playable…` ✓
- **B22.** 1. `27_MB_E…` · 2. `14_VERBS_MILITARY_A…`: needs `27_MB_E…` ✓ · 3. `14_VERBS_MILITARY_B…`: needs `14_VERBS_MILITARY_A…` ✓ · 4. `07_SE_campaign…` · 5. `U5b_MB_residue` · 6. `14_VERBS_MILITARY_C…`: needs `27_MB_E…` ✓; `14_VERBS_MILITARY_A…` ✓; `07_SE_campaign…` ✓ · 7. `14_VERBS_MILITARY_D…`: needs `27_MB_E…` ✓; `14_VERBS_MILITARY_C…` ✓ · 8. `14_VERBS_PHYSICAL_B…` · 9. `04_MB_playable…` · 10. `U5b_VERBS_military…` · 11. `17_CENSUS_C1A_02…`
- **B23.** 1. `06_FA_war…`: needs `U5d_FA_land…` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `U5d_FA_land…`: needs `06_FA_war…` ✓; `26_MASS_BATTLE_aggression…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `14_VERBS_MATERIAL_D…` · 4. `26_MASS_BATTLE_aggression…`: needs `U5d_FA_land…` ✓ · 5. `U5b_VERBS_military…` · 6. `U5b_MB_rulings…` · 7. `14_VERBS_BINDING_E…`: needs `U5d_FA_land…` ✓
- **B24.** 1. `05_SC_playable_hearing_B`: needs `05_SC_evidence_and_rebuttal_B` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `19_LACUNA_admission…`: needs `05_SC_evidence_and_rebuttal_B` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `05_SC_evidence_and_rebuttal_B`: needs `05_SC_playable_hearing_B` ✓; `19_LACUNA_admission…` ✓; `08_FI_05_evidence-interface_B` (two-way citation: co-lands in this order, the reverse edge kept) · 4. `08_FI_05_evidence-interface_B`: needs `05_SC_playable_hearing_B` ✓; `19_LACUNA_admission…` ✓; `05_SC_evidence_and_rebuttal_B` ✓ · 5. `05_SC_hearing…` · 6. `05_SC_negotiation…`: needs `05_SC_playable_hearing_B` ✓ · 7. `05_SC_sc05_kernel_disposition…`: needs `05_SC_playable_hearing_B` ✓ · 8. `17_CENSUS_C1B_01…` · 9. `12_ARCS_cited…`: needs `19_LACUNA_admission…` ✓; `05_SC_evidence_and_rebuttal_B` ✓ · 10. `02_CHAR_which…`: needs `05_SC_evidence_and_rebuttal_B` ✓ · 11. `U5c_VERBS_residue…` · 12. `17_CENSUS_REST_2…` · 13. `05_SC_playable_hearing` · 14. `05_SC_evidence_and_rebuttal` · 15. `08_FI_05_evidence-interface` · 16. `05_SC_sc05_kernel_retirement`
- **B25.** 1. `14_VERBS_SOCIAL2_A…`: needs `14_VERBS_SOCIAL2_B…` (two-way citation: co-lands in this order, the reverse edge kept); `14_VERBS_SOCIAL2_C…` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `14_VERBS_SOCIAL2_B…`: needs `14_VERBS_SOCIAL2_A…` ✓ · 3. `14_VERBS_SOCIAL2_C…`: needs `14_VERBS_SOCIAL2_A…` ✓ · 4. `14_VERBS_MATERIAL_C…` · 5. `08_FI_08…` · 6. `14_VERBS_SOCIAL2_D…`: needs `08_FI_08…` ✓
- **B26.** 1. `19_LACUNA_questioning…` · 2. `16_PESSIMIST_FI_B…` · 3. `16_PESSIMIST_FI_D…` · 4. `14_VERBS_MATERIAL_D…` · 5. `14_VERBS_MATERIAL_E…`: needs `14_VERBS_MATERIAL_D…` ✓ · 6. `14_VERBS_PHYSICAL_C…`
- **B27.** 1. `05_SC_acquittal` · 2. `05_SC_arrangement…` · 3. `16_PESSIMIST_SC_C…`: needs `05_SC_acquittal` ✓ · 4. `16_PESSIMIST_SC_D…` · 5. `U5c_SC_proceedings…`: needs `16_PESSIMIST_SC_C…` ✓; `16_PESSIMIST_SC_D…` ✓ · 6. `19_LACUNA_verdict…`: needs `05_SC_acquittal` ✓
- **B28.** 1. `14_VERBS_SOCIAL1_B…` · 2. `14_VERBS_SOCIAL1_D…`: needs `14_VERBS_SOCIAL1_B…` ✓ · 3. `14_VERBS_SOCIAL1_C…`: needs `14_VERBS_SOCIAL1_D…` ✓ · 4. `28_CORE_scene_access_A…` · 5. `28_CORE_scene_access_B…`: needs `28_CORE_scene_access_A…` ✓
- **B29.** 1. `14_VERBS_PHYSICAL_A…`
- **B30.** 1. `U5b_PC_rulings…` · 2. `03_PC_duel_round_and_approach_B` · 3. `04_MB_manager…` · 4. `04_MB_squad…` · 5. `U5b_MB_rulings…` · 6. `29_DICE_one…`
- **B31.** 1. `04_MB_unit_loadout_and_weapon_in_hand_B` · 2. `26_MASS_BATTLE_movement…` · 3. `16_PESSIMIST_MB_one…` · 4. `04_MB_campaign…` · 5. `U5b_MB_rulings…` · 6. `27_MB_B…`
- **B32.** 1. `15_INSTITUTIONS_COLONIAL_A…` · 2. `15_INSTITUTIONS_SYNTHESIS_A…`: needs `15_INSTITUTIONS_COLONIAL_A…` ✓; `15_INSTITUTIONS_SYNTHESIS_B…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `15_INSTITUTIONS_SYNTHESIS_B…`: needs `15_INSTITUTIONS_SYNTHESIS_A…` ✓ · 4. `22_HAPPENINGS_B…` · 5. `15_INSTITUTIONS_BYZANTINE_A…` · 6. `15_INSTITUTIONS_BYZANTINE_E…`: needs `15_INSTITUTIONS_BYZANTINE_A…` ✓ · 7. `15_INSTITUTIONS_PAPACY_A…` · 8. `15_INSTITUTIONS_PAPACY_B…` · 9. `14_VERBS_BINDING_B…` · 10. `15_INSTITUTIONS_VENICE_C…`: needs `14_VERBS_BINDING_B…` ✓ · 11. `16_PESSIMIST_FA_B…` · 12. `17_CENSUS_REST_2…`: needs `15_INSTITUTIONS_PAPACY_B…` ✓ · 13. `U5d_FA_owed…`
- **B33.** 1. `15_INSTITUTIONS_BYZANTINE_B…` · 2. `15_INSTITUTIONS_BYZANTINE_C…` · 3. `15_INSTITUTIONS_BYZANTINE_D…`: needs `15_INSTITUTIONS_BYZANTINE_C…` ✓ · 4. `15_INSTITUTIONS_COLONIAL_B…` · 5. `15_INSTITUTIONS_COLONIAL_C…` · 6. `15_INSTITUTIONS_COLONIAL_D…` · 7. `15_INSTITUTIONS_PAPACY_C…` · 8. `15_INSTITUTIONS_PAPACY_D…` · 9. `15_INSTITUTIONS_PAPACY_E…` · 10. `15_INSTITUTIONS_VENICE_A…` · 11. `15_INSTITUTIONS_VENICE_B…`: needs `15_INSTITUTIONS_VENICE_A…` ✓ · 12. `15_INSTITUTIONS_VENICE_D…`: needs `15_INSTITUTIONS_VENICE_A…` ✓; `15_INSTITUTIONS_VENICE_B…` ✓ · 13. `15_INSTITUTIONS_SYNTHESIS_C…`: needs `15_INSTITUTIONS_PAPACY_D…` ✓; `15_INSTITUTIONS_VENICE_A…` ✓; `15_INSTITUTIONS_VENICE_B…` ✓
- **B34.** 1. `11_GO_player_surface_contract_B` · 2. `11_GO_player_surface_contract` · 3. `11_GO_fidelity…`: needs `11_GO_player_surface_contract_B` ✓ · 4. `16_PESSIMIST_GO_the…`: needs `11_GO_player_surface_contract_B` ✓ · 5. `01_CORE_one…`: needs `11_GO_player_surface_contract_B` ✓ · 6. `U5a_CORE_owed…` · 7. `17_CENSUS_C1A_02…`
- **B35.** 1. `09_WR_B_threadwork…` · 2. `14_VERBS_PHYSICAL_D…` · 3. `17_CENSUS_REST_2…` · 4. `08_FI_08…` · 5. `U5d_WR_zero…` · 6. `12_ARCS_substrate…`: needs `U5d_WR_zero…` ✓
- **B36.** 1. `09_WR_story…` · 2. `09_WR_B_readings…`: needs `09_WR_B_chronicle…` (two-way citation: co-lands in this order, the reverse edge kept) · 3. `09_WR_B_chronicle…`: needs `09_WR_B_readings…` ✓ · 4. `19_LACUNA_verdict…` · 5. `16_PESSIMIST_WR_D…`: needs `09_WR_B_readings…` ✓ · 6. `20_NARRATIVE_F…`: needs `09_WR_story…` ✓; `09_WR_B_readings…` ✓; `09_WR_B_chronicle…` ✓ · 7. `23_STORY_D…`: needs `09_WR_story…` ✓; `20_NARRATIVE_F…` ✓ · 8. `17_CENSUS_C1B_02…`: needs `09_WR_B_readings…` ✓
- **B37.** 1. `22_HAPPENINGS_A…`: needs `16_PESSIMIST_WR_C…` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `16_PESSIMIST_WR_C…`: needs `22_HAPPENINGS_A…` ✓ · 3. `U5d_WR_owed…` · 4. `22_HAPPENINGS_C…` · 5. `U5b_PC_rulings…` · 6. `22_HAPPENINGS_D…`
- **B38.** 1. `20_NARRATIVE_A…`: needs `30_WR_B…` (two-way citation: co-lands in this order, the reverse edge kept); `30_WR_G…` (two-way citation: co-lands in this order, the reverse edge kept); `31_WR_A…` (two-way citation: co-lands in this order, the reverse edge kept) · 2. `20_NARRATIVE_F…` · 3. `20_NARRATIVE_C…`: needs `30_WR_A…` (two-way citation: co-lands in this order, the reverse edge kept); `30_GO_F…` (two-way citation: co-lands in this order, the reverse edge kept) · 4. `20_NARRATIVE_B…`: needs `20_NARRATIVE_C…` ✓; `28_CORE_scene_access_C…` (two-way citation: co-lands in this order, the reverse edge kept); `30_WR_D…` (two-way citation: co-lands in this order, the reverse edge kept) · 5. `28_CORE_scene_access_C…`: needs `20_NARRATIVE_C…` ✓; `20_NARRATIVE_B…` ✓ · 6. `20_NARRATIVE_D…`: needs `20_NARRATIVE_A…` ✓; `20_NARRATIVE_C…` ✓; `31_WR_A…` (split: NARR_D commit 1 before; its later commits after 31_WR_A commit 4 (NARR_D `:9`)); `30_WR_D…` (two-way citation: co-lands in this order, the reverse edge kept) · 7. `20_NARRATIVE_E…` · 8. `30_WR_B…`: needs `20_NARRATIVE_A…` ✓; `20_NARRATIVE_D…` ✓; `20_NARRATIVE_E…` ✓ · 9. `30_WR_G…`: needs `20_NARRATIVE_A…` ✓; `30_WR_B…` ✓; `31_WR_A…` (two-way citation: co-lands in this order, the reverse edge kept) · 10. `31_WR_A…`: needs `20_NARRATIVE_A…` ✓; `30_WR_B…` ✓; `30_WR_G…` ✓ · 11. `31_WR_B…`: needs `30_WR_G…` ✓; `31_WR_A…` ✓ · 12. `30_WR_A…`: needs `20_NARRATIVE_C…` ✓ · 13. `09_WR_B_draws…` · 14. `09_WR_B_weather…` · 15. `30_WR_C…`: needs `20_NARRATIVE_A…` ✓; `20_NARRATIVE_B…` ✓; `28_CORE_scene_access_C…` ✓ · 16. `23_STORY_A…`: needs `30_WR_D…` (two-way citation: co-lands in this order, the reverse edge kept) · 17. `30_WR_D…`: needs `20_NARRATIVE_A…` ✓; `20_NARRATIVE_C…` ✓; `20_NARRATIVE_B…` ✓; `28_CORE_scene_access_C…` ✓; `20_NARRATIVE_D…` ✓; `20_NARRATIVE_E…` ✓; `23_STORY_A…` ✓ · 18. `30_WR_E…`: needs `30_WR_B…` ✓; `30_WR_A…` ✓; `30_WR_C…` ✓; `30_WR_D…` ✓ · 19. `30_GO_F…`: needs `20_NARRATIVE_C…` ✓; `20_NARRATIVE_E…` ✓; `30_WR_G…` ✓; `30_WR_A…` ✓; `30_WR_C…` ✓ · 20. `31_WR_C…`: needs `20_NARRATIVE_D…` ✓; `31_WR_A…` ✓; `30_GO_F…` ✓ · 21. `U5d_SE_cohort…`: needs `31_WR_A…` ✓; `31_WR_B…` ✓; `31_WR_C…` ✓
- **B39.** 1. `21_PROCEDURAL_A…` · 2. `21_PROCEDURAL_B…`: needs `21_PROCEDURAL_A…` ✓ · 3. `21_PROCEDURAL_E…`: needs `21_PROCEDURAL_B…` ✓ · 4. `21_PROCEDURAL_C…`: needs `21_PROCEDURAL_A…` ✓ · 5. `01_CORE_case…`: needs `12_ARCS_case…` (cut REV: 12_ARCS `:7` names CORE as "this file's base") · 6. `12_ARCS_case…`: needs `21_PROCEDURAL_C…` ✓ · 7. `21_PROCEDURAL_D…`: needs `21_PROCEDURAL_A…` ✓; `01_CORE_case…` ✓; `12_ARCS_case…` ✓ · 8. `U5d_STORY_owed…` · 9. `23_STORY_B…`: needs `21_PROCEDURAL_B…` ✓ · 10. `23_STORY_C…` · 11. `23_STORY_E…`: needs `12_ARCS_case…` ✓ · 12. `15_INSTITUTIONS_SYNTHESIS_B…` · 13. `15_INSTITUTIONS_COLONIAL_D…` · 14. `17_CENSUS_C1B_02…` · 15. `U5d_FA_owed…` · 16. `30_WR_A…`
- **B40.** 1. `15_INSTITUTIONS_SYNTHESIS_D…` · 2. `15_INSTITUTIONS_BYZANTINE_F…` · 3. `15_INSTITUTIONS_COLONIAL_E…` · 4. `15_INSTITUTIONS_PAPACY_F…` · 5. `15_INSTITUTIONS_BYZANTINE_grounding…`: needs `15_INSTITUTIONS_BYZANTINE_F…` ✓ · 6. `15_INSTITUTIONS_VENICE_grounding…` · 7. `15_INSTITUTIONS_COLONIAL_grounding…`: needs `15_INSTITUTIONS_COLONIAL_E…` ✓; `15_INSTITUTIONS_VENICE_grounding…` ✓ · 8. `15_INSTITUTIONS_PAPACY_grounding…` · 9. `15_INSTITUTIONS_SYNTHESIS_E…`
- **B41.** 1. `16_PESSIMIST_GO_surface…` · 2. `11_GO_port…`: needs `16_PESSIMIST_GO_surface…` ✓

**What changed against the first order** (each also in §1): B03 (`17_CENSUS_REST_3` after the GO pointer file);
B04/B05 (`10_DICE_one_score_two_roles` moved to B05, C3-V1); B05 (SC-B placed at OBS step 1a, which carries it);
B06 (`fmath` first; `draw.py` imports it, the edge §3.1 lacked); B09 (`02_CHAR_reason_trail` Part A before the CORE
reason trail); B10 (`U5a_CHAR` §2 before the scar pair); B12 (`09_WR_strand_conclusion` added; `09_WR_world_motion`
edits 1–3 before the draws file, C3-V4; the SE readers after what they read); B15 (A3 before the riposte and the
yield); B17 (`04_MB_typed_outcome` §3 after the troop file exists); B19 (calibration T-rows first; 27C split); B21
(HAP_B after BIND_C's control; the decree split around FA_C; BIND_C's flip after the scenario); B22 (`27_MB_E` and the
SE supply file before the muster); B25, B28 (each to its own Lands line); B27 (the SC residue after SC_C/SC_D); B35;
B38 (NARR_C first; `31_WR_C` after `30_GO_F`); B39; B40.

### 1.3 Gate instrument exists by this batch

Each batch's gate names an instrument: a tool, a test file, a harness command or a probe. An instrument a batch reads
must exist on that batch's base or be written inside it before the reading (§6.1, §6.2). "Tree" means present at this
read (`ls tools/`, `ls engine/season/harness/`, `git ls-files` run by this lane). The test files of §6.1 are written
as their batch's first commit; the scratch probes of §6.2 are restated as named tests first; neither is repeated here.

| batch | gate instrument | exists by | verdict |
|---|---|---|---|
| B00 | `python -m engine.season.harness.register --check` | tree (`harness/register.py`) | ok |
| B01 | `harness/aperture.py`; the planted-dispute run | tree; lane A's branch | ok |
| B02 | pinned hashes through `engine/season/tests/_realm_goldens.py`; `test_realm_requirements.py` | B02 (`01_CORE_tests_one_golden_owner` A, first item; §6.1) | ok (created inside, before the reading) |
| B03 | content hashes; `tools/export_composition.py --check`; the deletions' greps; `test_cr30_heritage.py` | tree | ok |
| B04 | `tools/export_descriptors.py --check`; `harness/headless.py --case NPC-088`; `harness/corpus_run.py` | tree | ok |
| B05 | `test_sc01_provider.py`, `test_sc01_obstacle_ceiling.py`; `test_sc_calibration_targets.py`, `test_opposed_ob.py`, `test_combat_opposed_rule_shape.py` | tree; B05 first commit (§6.1) | ok |
| B06 | `engine/tests/test_draw.py`, `engine/tests/test_fmath.py`, `tests/valoria/test_fmath_one_owner.py` | B06 (written first, C3-V2) | ok |
| B06 | **`tools/export_oracle_pins.py --check`** (the draw and `fmath` vectors' export) | **B41** (`16_PESSIMIST_GO_surface_pins`, GO-08) | **was late: the gate moves to B41** (the vectors are held in B06's tests and reproduced there; their export round-trip is read in B41). Moving the exporter's creation earlier would pull GO-08 and its `surface` block, which needs B34, into B06 |
| B07 | the loader's planted band-keyed row; 18-A's five readings | B07 (18-A item 4's loader edit, first) | ok |
| B08 | `interactions_per_scene` readings | B08 | ok |
| B12 | `test_cr08_census_weight.py`, `test_endowment.py`, `test_travel.py`; the valley loader test | B12 first commit; `07_SE_valley_scenario` (B12, last item, creates `harness/valley.py`) | ok |
| B14, B15 | `tools/export_engine_params.py --check`; the armour reference re-derived | tree | ok |
| B17 | `tools/export_troops.py --check`, `tests/valoria/test_export_troops.py`; `test_field_golden_pins.py`; `tools/ci_golden_modes_check.py` | B17 (`04_MB_unit_loadout_and_weapon_in_hand_B` stage 1); tree | **was late inside the batch**: `04_MB_typed_outcome` §3 read the troop file before stage 1 created it; §3 moved after stages 1–2 (§1 item 17) |
| B19 | `26_MASS_BATTLE_calibration_targets` T-rows; `systems/mass_battle/sim/lanchester_signature.py` | B19 (T-rows moved first); tree | **was late inside the batch** (27C read the targets' results block before the targets landed); fixed by order |
| B20 | `harness/field_scene.py` | B20 (`04_MB_playable_field_scenario`) | ok |
| B21 | `test_fa01_head_seats.py`; `engine/season/tests/test_vb_c_turnover.py` | B21 first commit; B21 (`14_VERBS_BINDING_C`) | ok |
| B22 | `test_standing_ration.py` | B22 first commit | ok |
| B24 | `harness/governance_spine.py::build_hearing` | B24 (`05_SC_playable_hearing_B` edit 9, first item) | ok |
| B28 | `test_scene_access_occupancy.py`, `_precedence.py`, `_appointments.py`; `world_q.office_rank` | B28 first commit; B28 (`28_CORE_scene_access_A`) | ok |
| B32, B33, B40 | `test_instruments.py`; `test_accomplishment.py`, `test_audit_and_charter.py`, `test_remove.py` | B32; B33 first commit | ok |
| B36 | `harness/storybar.py`; `test_referent_class_stamps.py` | tree; B36 first commit | ok |
| B38, B39 | `test_custom.py`, `test_narrative_dues.py`, `test_sway.py`, `test_scene_access_waiting.py`; `test_worldgen_switch.py` | each batch's first commit | ok |
| B41 | `tools/export_oracle_pins.py --check`, `harness/port_oracle.py` | B41 (GO-08, first item) | ok; also reads B06's vectors (above) |

Batches not listed (B09 to B11, B16, B18, B23, B25 to B27, B29 to B31, B34, B35, B37) gate on each file's own readings,
which name existing harness commands or §6.1/§6.2 instruments written inside the batch; none names a tool another
batch creates.

### 1.4 Layer 1 amendments as gate nodes (Jordan's act; text drafted in `unified/U3_LAYER1_AMENDMENTS.md`)

A node `L1-…` is Jordan applying one drafted amendment (both halves, PART B/C and PART D). It has no predecessor in the
batch graph, so it adds no cycle. Each batch lands at the dormant form the amendments table names; only the arm named
here waits on the node.

| node | the arm that waits on it (batch) | dormant form that lands without it |
|---|---|---|
| `L1-A3` | the host grading the field by its end state; B23's land rules on `Won` (B17, B23) | `FieldOutcome` carries the end-state flags beside the margin; the ladder grades the margin `[ASSUMPTION]` |
| `L1-A4` | any new person-supplied callable across a seam: B20's field decider, B30's `duel` (B20, B30) | the built `decide=host.decide` (`seam/wrappers/combat.py:395`), as built |
| `L1-A72` | B30's wrapper handing `duel` into the field (B30) | the `contest_nesting_cap` fixture and `nested_entry` with no caller |
| `L1-A9` | `interactions_per_scene` above 1; the rival-acts draw over scenes (B08) | B08 edits 1–4 at `interactions_per_scene = 1` |
| `L1-A64` | `precedence_level` set (B28) | the person key at control (`precedence_level` `None`) |
| `L1-A12` | any non-null seat `modifier:` (OBS step 5's bench die, B05; B19; B32–B33); `rank_step` above 0 (B21) | the column loaded null; `rank_step` 0 |
| `L1-A13` | any authored `passes_through`, `hand_term`, `audit_at_exit` (B32, B33) | the keys accepted and absent |
| `L1-A20` | `at_war` narrowed to seat holders that may muster (B21) | `may_wage` built; `at_war` as today |
| `L1-A29` | B41's reading of step 13's done-when (B41) | B06 whole (hash EQUAL) |
| `L1-A30` | B41's port draw (B41) | B06 whole, under R-C's reading that `n` is part of the key |
| `L1-A92` | `sway_gain` above 0 (the calibration batch after B38) | the RESOLVE-side sway at `sway_gain` 0 (B10 host, B38) |
| `L1-A62` | none (A-62: build nothing) | — |

`L1-A22`, `L1-A24`, `L1-A77`, `L1-A85` are ledger rows co-committed with B21, B10, B19 and B23/B38; `L1-A17`, `L1-A60`
and `L1-A84` are reference text. None of them is a gate.


## 2. The batch graph

### 2.1 Batch table (the input to v12; one close per batch)

| # | handle | lane | wave | after (batches) | members (proposal files, without `.md`) | declared hash movers among members | split parts landing here from another node (earlier or later; extended by U6 R-A) |
|---|---|---|---|---|---|---|---|
| 0 | B00-ids | IN | W0 | — | (none; see split parts) | 0 of 0 | — |
| 1 | B01-laneA | IN | W1 | B00 | `03_PC_duel_chain_reach`; lane A `e5d6ab9` + `c5bf18a`, rebased (C3-A2) | 1 of 1 | — |
| 2 | B02-tests | IN | W2 | B00, B01 | `01_CORE_requirements_reading_record`; `01_CORE_tests_delete_what_cannot_fail`; `01_CORE_tests_one_golden_owner`; `01_CORE_tests_shipped_world_falsifiers`; `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading`; `16_PESSIMIST_GAME_consequence_reading`; `U5a_tests_digest_additions` | 0 of 7 | — |
| 3 | B03-hygiene | IN | W3 | B00, B01, B02 | `06_FA_hygiene`; `09_WR_B_pointer_text_for_the_orchestrator`; `09_WR_threadwork_module`; `11_GO_design_reference_disposition`; `11_GO_pointer_and_stale_text_resolutions`; `16_PESSIMIST_CORE_no_stored_plan`; `17_CENSUS_C1A_01_deletion_batches`; `17_CENSUS_C1B_01_deletions`; `17_CENSUS_C1B_03_corrections`; `17_CENSUS_REST_1_deletions`; `17_CENSUS_REST_3_corrections`; `U5a_CORE_owed_edits` | 1 of 12 | — |
| 4 | B04-capability-home | IN | W3 | B00, B01, B02 | `01_CORE_capability_authoring_surface`; `02_CHAR_capability_definitions`; `02_CHAR_capability_uses_table`; `05_SC_capability_surface`; `05_SC_hearing_capabilities`; `06_FA_office_capabilities`; `10_DICE_capability_axiom_map`; `U5a_capability_home_and_two_inputs` | 3 of 8 | `29_DICE_one_opposed_rule_form_and_tuning` (part: row 1, `opposed_ob`) |
| 5 | B05-one-roll | IN | W4 | B00, B01, B02, B04 | `05_SC_contest_record_on_event`; `05_SC_obstacle_difficulty_and_modifiers_B`; `05_SC_opposed_obstacle_parity`; `10_DICE_advantage_sources_for_the_arcs`; `10_DICE_believed_odds_have_a_prior`; `10_DICE_exported_face_rule_and_band_edges`; `10_DICE_one_roller_one_fraction_rule`; `10_DICE_one_score_two_roles`; `13_SC_calibration`; `13_SC_tuning_tables`; `16_PESSIMIST_DICE_soft_ceiling`; `16_PESSIMIST_DICE_task_difficulty_and_throughput`; `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage`; `29_DICE_one_opposed_rule_form_and_tuning`; `U5a_DICE_owed_edits`; `U5c_SC_one_obstacle_form` | 11 of 16 | `U5a_capability_home_and_two_inputs` (part), `U5b_MB_rulings_in_the_field` (part: §1), `U5b_PC_rulings_in_the_fight` (part: §2–§3), `U5c_SC_proceedings_residue` (part: §1), `01_CORE_tests_shipped_world_falsifiers` (part: the R-09 row) |
| 6 | B06-keyed-draw | IN | W5 | B00, B01, B02, B03, B05 | `11_GO_float_contract`; `11_GO_one_draw_owner`; `16_PESSIMIST_GO_keyed_draw_no_recorder`; `U5d_GO_owed_edits` | 2 of 4 | `11_GO_pointer_and_stale_text_resolutions` (part) |
| 7 | B07-task-draw | IN | W6 | B00, B01, B02, B05, B06 | `13_SC_draw_for_unrolled_contests`; `18_DETERMINISM_task_draw_for_uncontested_verbs`; `U5b_VERBS_military_physical_residue`; `U5c_VERBS_residue_and_governance_owner` | 3 of 4 | `16_PESSIMIST_DICE_task_difficulty_and_throughput` (part) |
| 8 | B08-scene-order | IN | W3 | B00, B01, B02 | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order`; `18_DETERMINISM_rival_acts_in_one_fold` | 2 of 2 | — |
| 9 | B09-memory | IN | W7 | B00, B01, B02, B05, B07 | `01_CORE_claim_fade_as_read`; `01_CORE_predicates_name_their_clause`; `01_CORE_reason_trail_in_the_act_store`; `02_CHAR_reason_trail_and_small_edits`; `16_PESSIMIST_CORE_a_refusal_is_remembered`; `16_PESSIMIST_CORE_the_record_holds_what_changed`; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`; `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds`; `16_PESSIMIST_SC_B_one_reader_of_a_ledger` | 8 of 9 | `U5a_DICE_owed_edits` (part), `U5c_VERBS_residue_and_governance_owner` (part) |
| 10 | B10-character | IN | W8 | B00, B01, B02, B04, B05, B09 | `01_CORE_unmet_need_is_attended_first`; `02_CHAR_choice_alignment`; `02_CHAR_goal_lean_on_its_own_question`; `02_CHAR_offer_what_can_be_done`; `02_CHAR_relations_have_a_ground`; `02_CHAR_resolve_and_temper`; `02_CHAR_scar_cap_and_regard_unit`; `02_CHAR_scar_is_a_wound`; `02_CHAR_voices_and_the_room`; `02_CHAR_what_an_act_risks`; `12_ARCS_arcs_as_staged_goals`; `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told`; `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says`; `16_PESSIMIST_CHAR_C_the_stop_is_the_mans`; `17_CENSUS_C1A_02_wires_and_corrections`; `U5a_CHAR_owed_amendments`; `U5a_CHAR_self_knowledge_is_a_belief` | 13 of 17 | — |
| 11 | B11-fi-readers | FI | W9 | B00, B01, B02, B03, B04, B07, B10 | `08_FI_01_claim-sourced-referents`; `08_FI_02_rumour-that-travels`; `08_FI_03_playable-inquiry`; `08_FI_04_small-edits`; `08_FI_06_testimony-names-a-hand`; `08_FI_07_shortest-playable-case`; `14_VERBS_SOCIAL1_A_formation`; `16_PESSIMIST_FI_A_what_a_rumour_can_garble`; `16_PESSIMIST_FI_C_what_a_deed_leaves_behind`; `16_PESSIMIST_SC_E_an_honest_teller_is_not_marked`; `18_DETERMINISM_notice_is_a_draw`; `19_LACUNA_conclusion_is_a_committed_assertion`; `U5c_FI_residue` | 13 of 13 | `17_CENSUS_REST_1_deletions` (part), `U5c_VERBS_residue_and_governance_owner` (part) |
| 12 | B12-world-motion-and-ground | SE+WR | W10 | B00, B01, B02, B04, B05, B07, B10, B11 | `07_SE_arc_needs`; `07_SE_capability_and_chooser_surface`; `07_SE_capability_rate_B`; `07_SE_ground_and_granaries`; `07_SE_kernel_repairs`; `07_SE_population_census`; `07_SE_population_regrowth_B`; `07_SE_treasury_granary_B`; `07_SE_valley_scenario`; `09_WR_B_draws_not_thresholds`; `09_WR_B_weather_with_memory_and_the_year`; `09_WR_provided_arcs`; `09_WR_strand_conclusion`; `09_WR_world_motion`; `14_VERBS_MATERIAL_A_mending`; `14_VERBS_MATERIAL_B_stores`; `14_VERBS_MATERIAL_C_works`; `16_PESSIMIST_GAME_the_world_draws`; `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted`; `16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate`; `16_PESSIMIST_WR_A_the_road_is_drawn`; `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks`; `U5d_SE_owed_edits`; `U5d_WR_owed_edits` | 19 of 24 | `17_CENSUS_C1A_02_wires_and_corrections` (part), `20_NARRATIVE_E_the_year_and_the_reason` (part: edit 1) |
| 13 | B14-pc-outcome | PC | W5 | B00, B01, B02, B05 | `03_PC_typed_outcome_one_door`; `03_PC_weapon_form_at_round_start`; `03_PC_weapon_records_in_the_export`; `16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight`; `U5b_PC_residue` | 4 of 5 | `14_VERBS_PHYSICAL_A_custody_and_force` (part: A4) |
| 14 | B15-pc-calibration | PC | W9 | B00, B01, B02, B04, B05, B10, B14 | `14_VERBS_PHYSICAL_A_custody_and_force`; `16_PESSIMIST_PC_A_the_yield_is_a_draw`; `16_PESSIMIST_PC_B_the_commit_window`; `16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw`; `18_DETERMINISM_no_certain_matchup`; `U5b_PC_rulings_in_the_fight` | 6 of 6 | `29_DICE_one_opposed_rule_form_and_tuning` (part), `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` (part: edit 3, `mortal_terms`) |
| 15 | B16-pc-round | PC | W10 | B00, B01, B02, B06, B07, B10, B15 | `03_PC_duel_round_and_approach`; `03_PC_duel_round_and_approach_B`; `03_PC_exits_withdrawal_recovery` | 3 of 3 | — |
| 16 | B17-mb-scale | MB | W6 | B00, B01, B02, B05, B14 | `04_MB_headcount_grade_and_scale`; `04_MB_typed_outcome_and_one_path`; `04_MB_unit_loadout_and_weapon_in_hand`; `04_MB_unit_loadout_and_weapon_in_hand_B`; `U5b_MB_residue` | 3 of 5 | — |
| 17 | B18-pc-content | PC | W11 | B00, B01, B02, B14, B16, B17 | `03_PC_loadout_and_carry`; `03_PC_person_inputs_content` | 2 of 2 | `U5b_PC_residue` (part: §3) |
| 18 | B19-mb-field-calibration | MB | W10 | B00, B01, B02, B04, B05, B06, B15, B17 | `04_MB_cell_hierarchy_as_data`; `04_MB_cr12_linear_law`; `16_PESSIMIST_MB_one_stamina_ledger`; `16_PESSIMIST_MB_partition_and_the_pair_rule`; `16_PESSIMIST_MB_rout_has_two_exits`; `26_MASS_BATTLE_calibration_targets`; `26_MASS_BATTLE_cell_scale_and_time`; `26_MASS_BATTLE_rout_pursuit_and_giving_ground`; `27_MB_A_command_and_the_obedience_draw`; `27_MB_C_dynamic_strength_and_the_residual_chance`; `U5b_MB_rulings_in_the_field` | 9 of 11 | — |
| 19 | B20-mb-orders | MB | W11 | B00, B01, B02, B05, B15, B16, B17, B19 | `04_MB_manager_battle_one_resolver`; `04_MB_playable_field_scenario`; `26_MASS_BATTLE_maneuver_orders`; `27_MB_D_the_commander_as_chooser` | 2 of 4 | `17_CENSUS_REST_2_wiring` (part: W1) |
| 20 | B21-fa-governance | FA | W9 | B00, B01, B02, B05, B07, B10 | `06_FA_decree_binds`; `06_FA_levy_through_the_seat_B`; `06_FA_playable_scenario`; `06_FA_remit_grant_by_row`; `06_FA_seat_terms_and_turnover`; `06_FA_seat_terms_by_body_B`; `06_FA_shortest_loop_B`; `14_VERBS_BINDING_A_formation`; `14_VERBS_BINDING_C_turnover`; `14_VERBS_BINDING_D_orders`; `16_PESSIMIST_FA_A_dismissal_survives_the_king`; `16_PESSIMIST_FA_B_who_may_sit_join_and_declare`; `16_PESSIMIST_FA_C_under_the_seat`; `22_HAPPENINGS_B_the_throne_is_never_stranded`; `U5d_FA_owed_edits` | 11 of 15 | `14_VERBS_PHYSICAL_B_field_and_ruin` (part), `17_CENSUS_C1A_02_wires_and_corrections` (part), `06_FA_war_lives_in_seats_B` (part: edits 1–3) |
| 21 | B22-mb-armies | MB | W12 | B00, B01, B02, B04, B05, B07, B10, B12, B17, B19, B20, B21 | `07_SE_campaign_supply_and_muster`; `14_VERBS_MILITARY_A_movement`; `14_VERBS_MILITARY_B_train`; `14_VERBS_MILITARY_C_the_muster`; `14_VERBS_MILITARY_D_the_order_of_battle`; `14_VERBS_PHYSICAL_B_field_and_ruin`; `27_MB_E_what_an_army_carries_back` | 6 of 7 | `04_MB_playable_field_scenario` (part), `17_CENSUS_C1A_02_wires_and_corrections` (part), `U5b_MB_residue` (part), `U5b_VERBS_military_physical_residue` (part: §4) |
| 22 | B23-land | FA | W13 | B00, B01, B02, B07, B12, B17, B19, B20, B21, B22 | `06_FA_war_lives_in_seats_B`; `14_VERBS_BINDING_E_war_seats`; `26_MASS_BATTLE_aggression_and_land`; `U5d_FA_land_and_seats_pass_on_a_won_march` | 3 of 4 | `U5b_MB_rulings_in_the_field` (part), `U5b_VERBS_military_physical_residue` (part), `14_VERBS_MATERIAL_D_paper` (part: §6, `seize`) |
| 23 | B24-sc-hearing | SC | W10 | B00, B01, B02, B03, B04, B07, B10, B11 | `02_CHAR_which_ground_moves_whom`; `05_SC_evidence_and_rebuttal`; `05_SC_evidence_and_rebuttal_B`; `05_SC_negotiation_scene`; `05_SC_playable_hearing`; `05_SC_playable_hearing_B`; `05_SC_sc05_kernel_disposition_B`; `05_SC_sc05_kernel_retirement`; `08_FI_05_evidence-interface`; `08_FI_05_evidence-interface_B`; `12_ARCS_cited_evidence`; `19_LACUNA_admission_rides_the_citing_draw` | 7 of 12 | `05_SC_hearing_capabilities` (part), `17_CENSUS_C1A_02_wires_and_corrections` (part), `17_CENSUS_C1B_01_deletions` (part), `U5c_VERBS_residue_and_governance_owner` (part), `17_CENSUS_REST_2_wiring` (part: W2), `U5c_SC_proceedings_residue` (part: §2, §6) |
| 24 | B25-fi-questioning | FI | W11 | B00, B01, B02, B11, B12, B24 | `08_FI_08_knots-season-form`; `14_VERBS_SOCIAL2_A_formation_on_what_is_known`; `14_VERBS_SOCIAL2_B_a_word_with_content`; `14_VERBS_SOCIAL2_C_case_question_confession`; `14_VERBS_SOCIAL2_D_tie` | 4 of 5 | `14_VERBS_MATERIAL_C_works` (part) |
| 25 | B26-fi-inquiry | FI | W12 | B00, B01, B02, B10, B11, B12, B24, B25 | `14_VERBS_MATERIAL_D_paper`; `14_VERBS_MATERIAL_E_knowledge`; `14_VERBS_PHYSICAL_C_looking`; `16_PESSIMIST_FI_B_a_paper_is_about_something`; `16_PESSIMIST_FI_D_withhold_what_has_no_product`; `19_LACUNA_questioning_has_an_approach_and_a_cost` | 5 of 6 | — |
| 26 | B27-sc-proceedings | SC | W11 | B00, B01, B02, B11, B24 | `05_SC_acquittal`; `05_SC_arrangement_rows_that_bind`; `16_PESSIMIST_SC_C_a_verdict_names_its_party`; `16_PESSIMIST_SC_D_an_argument_moves_someone`; `19_LACUNA_verdict_ladder_and_reversal`; `U5c_SC_proceedings_residue` | 6 of 6 | — |
| 27 | B28-social-verbs | SC | W12 | B00, B01, B02, B05, B07, B08, B11, B15, B21, B25 | `14_VERBS_SOCIAL1_B_documents_and_obedience`; `14_VERBS_SOCIAL1_C_persuasion_and_deceit`; `14_VERBS_SOCIAL1_D_grievance_and_settlement`; `28_CORE_scene_access_A_occupancy_and_precedence`; `28_CORE_scene_access_B_appointments` | 5 of 5 | — |
| 28 | B29-pc-custody | PC | W11 | B00, B01, B02, B15, B16, B21 | (none; see split parts) | 0 of 0 | `14_VERBS_PHYSICAL_A_custody_and_force` (part) |
| 29 | B30-mb-nested | MB | W12 | B00, B01, B02, B05, B15, B16, B20, B24 | `04_MB_squad_grid_of_named_characters` | 1 of 1 | `29_DICE_one_opposed_rule_form_and_tuning` (part), `U5b_PC_rulings_in_the_fight` (part: §1), `03_PC_duel_round_and_approach_B` (part: step 5), `04_MB_manager_battle_one_resolver` (part: §7), `U5b_MB_rulings_in_the_field` (part: §3) |
| 30 | B31-mb-loadout-economy | MB | W12 | B00, B01, B02, B17, B18, B19 | `04_MB_campaign_party_economy`; `26_MASS_BATTLE_movement_and_fatigue_as_data`; `27_MB_B_unit_prowess_on_the_row` | 2 of 3 | `04_MB_unit_loadout_and_weapon_in_hand_B` (part), `16_PESSIMIST_MB_one_stamina_ledger` (part), `U5b_MB_rulings_in_the_field` (part: §5, as §1 item 31 places it) |
| 31 | B32-inst-kit | FA | W12 | B00, B01, B02, B04, B05, B07, B20, B21, B24, B25, B27 | `14_VERBS_BINDING_B_sittings`; `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll`; `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd`; `15_INSTITUTIONS_COLONIAL_A_instruments`; `15_INSTITUTIONS_PAPACY_A_ground`; `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline`; `15_INSTITUTIONS_SYNTHESIS_A_one_kit`; `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger`; `15_INSTITUTIONS_VENICE_C_roll_lot_ballot`; `17_CENSUS_REST_2_wiring` | 7 of 10 | `16_PESSIMIST_FA_B_who_may_sit_join_and_declare` (part), `22_HAPPENINGS_B_the_throne_is_never_stranded` (part), `U5d_FA_owed_edits` (part) |
| 32 | B33-inst-economy-hands | FA | W13 | B00, B01, B02, B04, B05, B07, B12, B21, B24, B25, B26, B27, B28, B32 | `15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc`; `15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain`; `15_INSTITUTIONS_BYZANTINE_D_the_empire_at_a_distance`; `15_INSTITUTIONS_COLONIAL_B_distance`; `15_INSTITUTIONS_COLONIAL_C_audit_and_charter`; `15_INSTITUTIONS_COLONIAL_D_accomplishment`; `15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger`; `15_INSTITUTIONS_PAPACY_D_sanction_and_absolution`; `15_INSTITUTIONS_PAPACY_E_sees_tithe_orders_legates_council`; `15_INSTITUTIONS_SYNTHESIS_C_crossings`; `15_INSTITUTIONS_VENICE_A_obligation_and_the_ask`; `15_INSTITUTIONS_VENICE_B_debt_instrument`; `15_INSTITUTIONS_VENICE_D_houses_charters_and_content` | 9 of 13 | — |
| 33 | B34-go-surface | GO | W11 | B00, B01, B02, B03, B10, B24 | `01_CORE_one_scene_contract`; `11_GO_fidelity_and_campaign_modes`; `11_GO_player_surface_contract`; `11_GO_player_surface_contract_B`; `16_PESSIMIST_GO_the_offer_names_what_is_held` | 1 of 5 | `17_CENSUS_C1A_02_wires_and_corrections` (part), `U5a_CORE_owed_edits` (part) |
| 34 | B35-wr-thread | WR | W13 | B00, B01, B02, B03, B05, B09, B11, B12, B32, B34 | `09_WR_B_threadwork_session_and_practitioner`; `12_ARCS_substrate_as_ground`; `14_VERBS_PHYSICAL_D_thread_read`; `U5d_WR_zero_coherence_unknowable` | 2 of 4 | `17_CENSUS_REST_2_wiring` (part), `08_FI_08_knots-season-form` (part: §1, §4) |
| 35 | B36-wr-story-instruments | WR | W14 | B00, B01, B02, B03, B09, B12, B27, B34, B35 | `09_WR_B_chronicle_that_tells`; `09_WR_B_readings_of_closure_and_tension`; `09_WR_story_instruments_that_can_fail`; `16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings`; `17_CENSUS_C1B_02_wires`; `20_NARRATIVE_F_story_inventory_and_gate`; `23_STORY_D_story_census_and_gate` | 0 of 7 | `19_LACUNA_verdict_ladder_and_reversal` (part) |
| 36 | B37-happenings | IN | W11 | B00, B01, B02, B05, B10, B11, B12, B15, B16, B21 | `16_PESSIMIST_WR_C_illness_on_the_body_ladder`; `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn`; `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits`; `22_HAPPENINGS_D_batches_and_added_gates` | 4 of 4 | `U5b_PC_rulings_in_the_fight` (part), `U5d_WR_owed_edits` (part) |
| 37 | B38-narrative-regimes | WR | W15 | B00, B01, B02, B05, B07, B09, B10, B11, B12, B21, B22, B23, B27, B28, B32, B34, B36 | `20_NARRATIVE_A_stands_for`; `20_NARRATIVE_B_what_he_was_owed`; `20_NARRATIVE_C_who_holds_what`; `20_NARRATIVE_D_his_own_side`; `20_NARRATIVE_E_the_year_and_the_reason`; `23_STORY_A_what_a_roll_leaves`; `28_CORE_scene_access_C_the_petition_that_waits`; `30_GO_F_the_plot_as_the_player_is_shown_it`; `30_WR_A_the_era_is_a_named_period`; `30_WR_B_regimes_who_believes_whom`; `30_WR_C_strands_open_grow_join_conclude`; `30_WR_D_momentum_and_its_brakes`; `30_WR_E_cascade_chains_and_the_census`; `30_WR_G_regime_opinions_and_the_pull_of_ones_own`; `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes`; `31_WR_B_the_revival_gathers`; `31_WR_C_what_the_stances_feed`; `U5d_SE_cohort_heavy_moves_and_caste` | 12 of 18 | `09_WR_B_draws_not_thresholds` (part), `09_WR_B_weather_with_memory_and_the_year` (part), `20_NARRATIVE_F_story_inventory_and_gate` (part) |
| 38 | B39-procgen-and-cases | WR | W16 | B00, B01, B02, B04, B06, B07, B10, B11, B12, B15, B21, B22, B24, B25, B26, B27, B32, B33, B36, B37, B38 | `01_CORE_case_setup_and_beats`; `12_ARCS_case_on_the_realm`; `21_PROCEDURAL_A_worldgen_tables_and_ground`; `21_PROCEDURAL_B_cast_and_seats`; `21_PROCEDURAL_C_prologue_and_case_seeds`; `21_PROCEDURAL_D_world_cards_and_churn`; `21_PROCEDURAL_E_names_and_texts`; `23_STORY_B_a_house_continues`; `23_STORY_C_a_founded_place_can_fail`; `23_STORY_E_first_playable_the_lean_year`; `U5d_STORY_owed_edits` | 7 of 11 | `15_INSTITUTIONS_COLONIAL_D_accomplishment` (part), `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger` (part), `17_CENSUS_C1B_02_wires` (part), `30_WR_A_the_era_is_a_named_period` (part), `U5d_FA_owed_edits` (part) |
| 39 | B40-inst-scenarios | FA | W17 | B00, B01, B02, B12, B21, B32, B33, B39 | `15_INSTITUTIONS_BYZANTINE_F_playable_scenarios_and_reading`; `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms`; `15_INSTITUTIONS_COLONIAL_E_scenario`; `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds`; `15_INSTITUTIONS_PAPACY_F_playable_vacant_chair`; `15_INSTITUTIONS_PAPACY_grounding_mechanisms`; `15_INSTITUTIONS_SYNTHESIS_D_first_playable`; `15_INSTITUTIONS_SYNTHESIS_E_implementation_plan`; `15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds` | 0 of 9 | — |
| 40 | B41-go-port-gate | GO | W12 | B00, B01, B02, B06, B34 | `11_GO_port_gate_order_and_coverage`; `16_PESSIMIST_GO_surface_pins` | 0 of 2 | — |

### 2.2 Waves (dependency levels) and the critical path

| wave | batches (may run at once only under §2.4 rules) |
|---|---|
| W0 | B00-ids |
| W1 | B01-laneA |
| W2 | B02-tests |
| W3 | B03-hygiene, B04-capability-home, B08-scene-order |
| W4 | B05-one-roll |
| W5 | B06-keyed-draw, B14-pc-outcome |
| W6 | B07-task-draw, B17-mb-scale |
| W7 | B09-memory |
| W8 | B10-character |
| W9 | B11-fi-readers, B15-pc-calibration, B21-fa-governance |
| W10 | B12-world-motion-and-ground, B16-pc-round, B19-mb-field-calibration, B24-sc-hearing |
| W11 | B18-pc-content, B20-mb-orders, B25-fi-questioning, B27-sc-proceedings, B29-pc-custody, B34-go-surface, B37-happenings |
| W12 | B22-mb-armies, B26-fi-inquiry, B28-social-verbs, B30-mb-nested, B31-mb-loadout-economy, B32-inst-kit, B41-go-port-gate |
| W13 | B23-land, B33-inst-economy-hands, B35-wr-thread |
| W14 | B36-wr-story-instruments |
| W15 | B38-narrative-regimes |
| W16 | B39-procgen-and-cases |
| W17 | B40-inst-scenarios |

**Critical path (longest chain of batch dependencies, 18 batches):** B00-ids → B01-laneA → B02-tests → B04-capability-home → B05-one-roll → B06-keyed-draw → B07-task-draw → B09-memory → B10-character → B11-fi-readers → B24-sc-hearing → B27-sc-proceedings → B32-inst-kit → B35-wr-thread → B36-wr-story-instruments → B38-narrative-regimes → B39-procgen-and-cases → B40-inst-scenarios.


### 2.3 One schedule that obeys the lane rule (one open batch per lane), unit time per batch [estimate]

| step | batches open at once (each in its own lane and worktree) |
|---|---|
| S0 | B00-ids (IN) |
| S1 | B01-laneA (IN) |
| S2 | B02-tests (IN) |
| S3 | B03-hygiene (IN) |
| S4 | B04-capability-home (IN) |
| S5 | B05-one-roll (IN) |
| S6 | B06-keyed-draw (IN), B14-pc-outcome (PC) |
| S7 | B07-task-draw (IN), B17-mb-scale (MB) |
| S8 | B08-scene-order (IN) |
| S9 | B09-memory (IN) |
| S10 | B10-character (IN) |
| S11 | B11-fi-readers (FI), B15-pc-calibration (PC), B21-fa-governance (FA) |
| S12 | B12-world-motion-and-ground (SE+WR), B16-pc-round (PC), B19-mb-field-calibration (MB), B24-sc-hearing (SC) |
| S13 | B18-pc-content (PC), B20-mb-orders (MB), B25-fi-questioning (FI), B27-sc-proceedings (SC), B34-go-surface (GO), B37-happenings (IN) |
| S14 | B22-mb-armies (MB), B26-fi-inquiry (FI), B28-social-verbs (SC), B29-pc-custody (PC), B32-inst-kit (FA), B41-go-port-gate (GO) |
| S15 | B23-land (FA), B30-mb-nested (MB), B35-wr-thread (WR) |
| S16 | B31-mb-loadout-economy (MB), B33-inst-economy-hands (FA), B36-wr-story-instruments (WR) |
| S17 | B38-narrative-regimes (WR) |
| S18 | B39-procgen-and-cases (WR) |
| S19 | B40-inst-scenarios (FA) |

Makespan under this rule: 20 steps for 41 batches (a batch handle is one close; B13 is unused, merged into B12). [ASSUMPTION: every batch costs one unit — basis: no batch has a measured runtime yet; v12 replaces the unit by each batch's estimate (`STAGES.md` step 6, efficiency rule 5).]


## 3. Every proposal

### 3.1 Node table: every proposal

Status codes inside "depends on": every proposal named is PROPOSED (P) and carries its batch; EXISTS-IN-TREE and MISSING items are the read lane's own marks in the row cited in the last column (T/E/EX = exists, M/MS = missing, PL/PLAN/W = a v11 plan position). "cut" marks an edge removed by §4.

| proposal | batch | lane (read lane) | depends on: proposals (batch) | MISSING named in the read lane's row | hash movers declared (read lane) | gate named | cost / tier | read-lane row |
|---|---|---|---|---|---|---|---|---|
| `03_PC_duel_chain_reach` | B01 | PC (CORE file) | 14_VERBS_PHYSICAL_A_custody_and_force (B15, cut) | — | yes: formation of `challenge`/`accept` | yes (`aperture 2 s` before/after) | cost yes / tier no | R1:371 |
| `01_CORE_requirements_reading_record` | B02 | IN | — | — | none | yes | cost yes; tier no | R2:315 |
| `01_CORE_tests_delete_what_cannot_fail` | B02 | IN | — | — | none | yes | cost yes; tier no | R2:316 |
| `01_CORE_tests_one_golden_owner` | B02 | IN | — | — | none | yes | cost yes; tier no | R2:317 |
| `01_CORE_tests_shipped_world_falsifiers` | B02 | IN | 01_CORE_requirements_reading_record (B02) | — | none | yes | cost yes; tier no | R2:318 |
| `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` | B02 | IN (CORE) | 01_CORE_requirements_reading_record (B02) | `req_forge.py` | none | yes (`req_forge.py` re-run: not in repo  | class yes (Edit, small build); tier no | R5:505 |
| `16_PESSIMIST_GAME_consequence_reading` | B02 | IN | 01_CORE_requirements_reading_record (B02) | — | none | yes (`chronicle --propagation --seeds 0  | class yes (Edit); tier no | R5:521 |
| `U5a_tests_digest_additions` | B02 | IN | — | — | none | yes | cost yes; tier no | R2:337 |
| `06_FA_hygiene` | B03 | FA (+IN) | — | — | rename = 2 movers | yes | edit, six commits / none | R3:224 |
| `09_WR_B_pointer_text_for_the_orchestrator` | B03 | WR (IN) | — | — | none | yes | edit (text) / none | R3:249 |
| `09_WR_threadwork_module` | B03 | WR | — | — | EQUAL | yes | small build / none | R3:256 |
| `11_GO_design_reference_disposition` | B03 | GO | 11_GO_pointer_and_stale_text_resolutions (B03) | — | none | yes | yes / no | R1:413 |
| `11_GO_pointer_and_stale_text_resolutions` | B03 | GO | 11_GO_one_draw_owner (B06, cut) | — | none | yes | yes / no | R1:419 |
| `16_PESSIMIST_CORE_no_stored_plan` | B03 | IN (CORE) | — | — | none (falsifier: any pinned hash moves) | yes: realm and headless hashes unchanged | class yes (Edit, a deletion); tier no | R5:504 |
| `17_CENSUS_C1A_01_deletion_batches` | B03 | IN | 02_CHAR_voices_and_the_room (B10, cut); 06_FA_hygiene (B03); 09_WR_B_chronicle_that_tells (B36, cut); 09_WR_B_threadwork_session_and_practitio (B35, cut); 11_GO_player_surface_contract_B (B34, cut); 19_LACUNA_verdict_ladder_and_reversal (B27, cut) | — | none (content hash equal) | yes (import probe; `test_cr30_heritage.p | class yes (Edit, three commits); tier no | R5:546 |
| `17_CENSUS_C1B_01_deletions` | B03 | IN (cross-lane: MB, WR, PC) | 01_CORE_tests_delete_what_cannot_fail (B02); 04_MB_unit_loadout_and_weapon_in_hand (B17, cut); 05_SC_sc05_kernel_disposition_B (B24, cut); 09_WR_threadwork_module (B03) | — | none (hash equal) | yes (4 items) | class yes (Edit; small build for D3); ti | R5:548 |
| `17_CENSUS_C1B_03_corrections` | B03 | IN | — | — | none | yes (greps) | class yes (Edit); tier no | R5:550 |
| `17_CENSUS_REST_1_deletions` | B03 | IN | 08_FI_04_small-edits (B11, cut); 10_DICE_one_roller_one_fraction_rule (B05, cut); 17_CENSUS_C1B_01_deletions (B03); U5a_DICE_owed_edits (B05, cut) | — | none | yes | class yes (Edit, three batches); tier no | R5:551 |
| `17_CENSUS_REST_3_corrections` | B03 | IN | 11_GO_pointer_and_stale_text_resolutions (B03) | — | none | yes (register `--check`, `--verify-citat | class yes (Edit, one `[cleanup]` commit) | R5:553 |
| `U5a_CORE_owed_edits` | B03 | IN | 01_CORE_tests_one_golden_owner (B02); 11_GO_player_surface_contract_B (B34, cut) | — | none | yes (per section) | cost yes; tier no (lands-by line: an IN  | R2:335 |
| `01_CORE_capability_authoring_surface` | B04 | IN | 10_DICE_capability_axiom_map (B04); U1 | — | Part one none; Edit 8 and 9 each | yes (`export_descriptors --check`, hash  | cost yes; tier no | R2:309 |
| `02_CHAR_capability_definitions` | B04 | IN | U1 | — | build-hash once after Edit 4 deletions | yes | cost yes; tier no | R2:320 |
| `02_CHAR_capability_uses_table` | B04 | IN | U1 | — | none | yes | cost yes; tier no | R2:321 |
| `05_SC_capability_surface` | B04 | SC | U1 | — | none | yes (`test_sc01_provider.py`) | cost yes; tier no | R2:340 |
| `05_SC_hearing_capabilities` | B04 | SC | 05_SC_playable_hearing_B (B24, cut); U1 | — | none for the cast as shipped | yes | cost yes; tier no | R2:344 |
| `06_FA_office_capabilities` | B04 | FA (CHAR) | 05_SC_hearing_capabilities (B04); U5a_capability_home_and_two_inputs (B04) | `None`, `[UNVERIFIED]` | none at ship; `confer_fit_weight` flip | yes | small build / none | R3:226 |
| `10_DICE_capability_axiom_map` | B04 | IN (CHAR, SC, PC, MB, SE) | 01_CORE_capability_authoring_surface (B04); 02_CHAR_capability_uses_table (B04); U1; U5a_capability_home_and_two_inputs (B04) | — | part one hash equal | yes | yes / no | R1:407 |
| `U5a_capability_home_and_two_inputs` | B04 | IN + SC + PC | 05_SC_obstacle_difficulty_and_modifiers_ (B05, cut); 05_SC_opposed_obstacle_parity (B05, cut); 16_PESSIMIST_DICE_soft_ceiling (B05, cut); U1; U5a_DICE_owed_edits (B05, cut) | — | Part B every graded world; Part C build hash | yes (hash, equal opponents, R-09 conjunc | cost yes; tier no | R2:336 |
| `05_SC_contest_record_on_event` | B05 | SC | U5c_SC_one_obstacle_form (B05) | — | once | yes (`test_sc01_provider.py`) | cost yes; tier no | R2:341 |
| `05_SC_obstacle_difficulty_and_modifiers_B` | B05 | SC | U5c_SC_one_obstacle_form (B05) | — | — | (OBS's) | — | R2:346 |
| `05_SC_opposed_obstacle_parity` | B05 | SC | 29_DICE_one_opposed_rule_form_and_tuning (B05); U5c_SC_one_obstacle_form (B05) | — | at the joint calibration step | yes (`test_sc01_obstacle_ceiling.py`) | cost yes; tier no | R2:347 |
| `10_DICE_advantage_sources_for_the_arcs` | B05 | IN (PC, SC, FA) | — | `engine/season/tests/test_effort.py` | mover for a wounded person | yes | yes / no | R1:405 |
| `10_DICE_believed_odds_have_a_prior` | B05 | IN (CHAR, CORE) | — | — | declared mover | yes | yes / no | R1:406 |
| `10_DICE_exported_face_rule_and_band_edges` | B05 | IN (GO) | U5a_DICE_owed_edits (B05) | — | none | yes | yes / no | R1:408 |
| `10_DICE_one_roller_one_fraction_rule` | B05 | IN (MB) | U5a_DICE_owed_edits (B05); U5b_MB_rulings_in_the_field (B19, cut) | — | one declared re-pin (head) | yes (stale wording) | yes / no | R1:409 |
| `10_DICE_one_score_two_roles` | B05 | IN (CHAR) | 29_DICE_one_opposed_rule_form_and_tuning (B05); U5a_capability_home_and_two_inputs (B04); U5c_SC_one_obstacle_form (B05) | — | declared mover | yes | yes / no | R1:410 |
| `13_SC_calibration` | B05 | SC | 13_SC_tuning_tables (B05); 29_DICE_one_opposed_rule_form_and_tuning (B05); U5c_SC_one_obstacle_form (B05) | — | none | yes | cost yes; tier no | R2:352 |
| `13_SC_tuning_tables` | B05 | SC | U5c_SC_one_obstacle_form (B05) | — | commit 2 | yes | cost yes; tier no | R2:354 |
| `16_PESSIMIST_DICE_soft_ceiling` | B05 | IN (DICE) / SC | 05_SC_obstacle_difficulty_and_modifiers_ (B05); U5a_DICE_owed_edits (B05) | — | every world where a rolled act composes above the fixed ceiling | yes (4) | class yes (Edit); tier no | R5:512 |
| `16_PESSIMIST_DICE_task_difficulty_and_throughput` | B05 | IN (DICE) / SC | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 13_SC_tuning_tables (B05); 18_DETERMINISM_task_draw_for_uncontested (B07, cut) | — | none until SC-B and 18-A land | yes (4) | class yes (Edit to proposals); tier no | R5:513 |
| `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage` | B05 | SC | 05_SC_evidence_and_rebuttal_B (B24, cut); 05_SC_obstacle_difficulty_and_modifiers_ (B05); 13_SC_tuning_tables (B05); 19_LACUNA_admission_rides_the_citing_dra (B24, cut) | — | any world with a `speak` rolled with proofs or reception (7 rolls in 4 | yes | class yes; tier no | R5:535 |
| `29_DICE_one_opposed_rule_form_and_tuning` | B05 | IN (DICE, SC, PC) | 13_SC_calibration (B05); U5a_capability_home_and_two_inputs (B04); U5b_PC_rulings_in_the_fight (B15, cut); U5c_SC_one_obstacle_form (B05) | `DuelRoundInput`, `HearingInput`, `Speaker` | none at control; live in the two batches | yes | yes / yes | R1:412 |
| `U5a_DICE_owed_edits` | B05 | IN | 01_CORE_claim_fade_as_read (B09, cut); 16_PESSIMIST_CORE_a_refusal_is_remembere (B09, cut) | — | every graded draw | yes | yes / no | R1:411 |
| `U5c_SC_one_obstacle_form` | B05 | SC | 05_SC_contest_record_on_event (B05); 05_SC_evidence_and_rebuttal_B (B24, cut); 13_SC_tuning_tables (B05); 29_DICE_one_opposed_rule_form_and_tuning (B05); U1 | — | steps 1b, 2, 5, each later step | yes (6 gates) | cost yes; tier no (lanes named) | R2:355 |
| `11_GO_float_contract` | B06 | GO (IN, PC, MB) | — | — | hash EQUAL on 3.11 | yes | yes / no | R1:415 |
| `11_GO_one_draw_owner` | B06 | GO (IN) | 16_PESSIMIST_GO_keyed_draw_no_recorder (B06); 11_GO_float_contract (B06; added by U6 R-A: `draw.py` imports `fmath`, `11_GO_one_draw_owner.md:9`, `:49`) | — | one declared re-pin | yes | yes / no | R1:416 |
| `16_PESSIMIST_GO_keyed_draw_no_recorder` | B06 | GO / IN (PC, MB, DICE draw sit | 11_GO_one_draw_owner (B06) | `Draw`, `engine/dice_engine/draw.py` | every seeded hash and golden moves once (with `11_GO_one_draw_owner.md | yes (4) | class yes (Small build + one re-pin); ti | R5:526 |
| `U5d_GO_owed_edits` | B06 | GO | 11_GO_float_contract (B06); 16_PESSIMIST_GO_keyed_draw_no_recorder (B06) | — | none | yes | yes / no | R1:422 |
| `13_SC_draw_for_unrolled_contests` | B07 | SC | — | — | yes (for the surviving rows) | yes | cost yes; tier no | R2:353 |
| `18_DETERMINISM_task_draw_for_uncontested_verbs` | B07 | IN | 13_SC_tuning_tables (B05); 16_PESSIMIST_DICE_task_difficulty_and_th (B05); U1 | — | every realm, spine and case world where a converted verb executes (all | yes (5) | class yes (Medium build); tier no | R5:557 |
| `U5b_VERBS_military_physical_residue` | B07 | MB [R4] | 18_DETERMINISM_task_draw_for_uncontested (B07); 26_MASS_BATTLE_aggression_and_land (B23, cut); U5c_VERBS_residue_and_governance_owner (B07); U5d_FA_land_and_seats_pass_on_a_won_marc (B23, cut) | `world_q.passage_granted` | none by shape; formation | Y | edit / small; no tier | R4:447 |
| `U5c_VERBS_residue_and_governance_owner` | B07 | IN [R4] | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 05_SC_playable_hearing_B (B24, cut); 08_FI_01_claim-sourced-referents (B11, cut); 08_FI_02_rumour-that-travels (B11, cut); 16_PESSIMIST_CORE_a_refusal_is_remembere (B09, cut); 18_DETERMINISM_task_draw_for_uncontested (B07); U5c_SC_one_obstacle_form (B05) | — | §3, §4 declared | Y | edit / small; no tier | R4:446 |
| `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` | B08 | IN (CORE) | 18_DETERMINISM_rival_acts_in_one_fold (B08); 28_CORE_scene_access_A_occupancy_and_pre (B28, cut) | — | every fixture with >1 interaction per scene; control `interactions_per | yes (4 readings) | class yes (design-first then small build | R5:508 |
| `18_DETERMINISM_rival_acts_in_one_fold` | B08 | IN | 16_PESSIMIST_CORE_a_scene_runs_in_its_ow (B08); 28_CORE_scene_access_A_occupancy_and_pre (B28, cut) | — | only worlds with a rivalry group | yes (4) | class yes (Small build); tier no | R5:556 |
| `01_CORE_claim_fade_as_read` | B09 | IN | 01_CORE_tests_one_golden_owner (B02) | `decision/options.py`, `loop/witness.py` | yes (log and `Claim.confidence`) | yes (`probe_growth.py` — a scratch scrip | cost yes; tier no | R2:311 |
| `01_CORE_predicates_name_their_clause` | B09 | IN (FA content) | — | — | step two yes | yes (`probe_predicates.py` — scratch) | cost yes; tier no | R2:313 |
| `01_CORE_reason_trail_in_the_act_store` | B09 | IN | 02_CHAR_reason_trail_and_small_edits (B09) | — | none if the store is not hashed | yes (`probe_reason.py` — scratch) | cost yes; tier no | R2:314 |
| `02_CHAR_reason_trail_and_small_edits` | B09 | IN | — | — | B1 yes | yes | cost yes; tier no | R2:325 |
| `16_PESSIMIST_CORE_a_refusal_is_remembered` | B09 | IN (CORE) | 01_CORE_claim_fade_as_read (B09); U5a_DICE_owed_edits (B05) | — | control `refusal_memory=0.0` equals today's; any non-control value re- | yes (five readings) | class yes (small build); tier no | R5:506 |
| `16_PESSIMIST_CORE_the_record_holds_what_changed` | B09 | IN (CORE) | 16_PESSIMIST_CHAR_A_a_crisis_of_faith_is (B10, cut) | — | every content hash moves once | yes (6 readings) | class yes (small build, one golden re-re | R5:507 |
| `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` | B09 | IN | 01_CORE_reason_trail_in_the_act_store (B09) | — | declared (an Event's `causes` is hashed); control reproduces | yes (named test files; control arm) | class yes (Edit); tier no | R5:522 |
| `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` | B09 | IN / CHAR | — | — | control equal; declared when chance raised | yes (5 rows) | class yes; tier no | R5:525 |
| `16_PESSIMIST_SC_B_one_reader_of_a_ledger` | B09 | SC (IN, FI) | 01_CORE_claim_fade_as_read (B09) | — | wherever a person holds two values for one cell | yes | class yes (Small build); tier no | R5:536 |
| `01_CORE_unmet_need_is_attended_first` | B10 | IN | 02_CHAR_goal_lean_on_its_own_question (B10) | — | yes | yes (`scarce` unassisted arm) | cost yes; tier no | R2:319 |
| `02_CHAR_choice_alignment` | B10 | IN | — | — | once a cell is authored | yes | cost yes; tier no | R2:322 |
| `02_CHAR_goal_lean_on_its_own_question` | B10 | IN | — | — | when `aim_gain` flips | yes | cost yes; tier no | R2:323 |
| `02_CHAR_offer_what_can_be_done` | B10 | IN | — | — | yes | yes (`aperture 2 0`) | cost yes; tier no | R2:324 |
| `02_CHAR_relations_have_a_ground` | B10 | IN (CHAR) | U5a_CHAR_owed_amendments (B10) | — | once content lands | yes (`probe_foils.py` — scratch) | cost yes; tier no | R2:326 |
| `02_CHAR_resolve_and_temper` | B10 | IN | U5a_CHAR_owed_amendments (B10) | — | none at control | yes | cost yes; tier no | R2:327 |
| `02_CHAR_scar_cap_and_regard_unit` | B10 | IN | 02_CHAR_scar_is_a_wound (B10); U5a_CHAR_owed_amendments (B10) | — | each flip | yes | cost yes; tier no | R2:328 |
| `02_CHAR_scar_is_a_wound` | B10 | IN | 02_CHAR_scar_cap_and_regard_unit (B10); 16_PESSIMIST_CORE_the_record_holds_what_ (B09) | — | each flip | yes (probe scratch) | cost yes; tier no | R2:329 |
| `02_CHAR_voices_and_the_room` | B10 | IN / GO surface | 02_CHAR_reason_trail_and_small_edits (B09) | — | none (observer) | yes | cost yes; tier no | R2:330 |
| `02_CHAR_what_an_act_risks` | B10 | IN | 02_CHAR_capability_uses_table (B04); 10_DICE_believed_odds_have_a_prior (B05) | — | when `risk_gain` flips | yes | cost yes; tier no | R2:331 |
| `12_ARCS_arcs_as_staged_goals` | B10 | WR/IN | — | — | none with no stage rows | yes (ARC-47, three arms) | cost yes; tier no | R2:367 |
| `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told` | B10 | IN (CHAR) | 02_CHAR_capability_definitions (B04); 02_CHAR_scar_cap_and_regard_unit (B10); 02_CHAR_scar_is_a_wound (B10); 16_PESSIMIST_CORE_the_record_holds_what_ (B09); U1 | — | every run in which a crisis fires re-records; control `crisis_draw: of | yes (4 readings; seeded run, no named te | class yes (small build); tier no | R5:509 |
| `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says` | B10 | IN (CHAR) | U5a_CHAR_owed_amendments (B10) | — | step 2 re-records every golden that plays a season; step 1 none | yes (3 readings) | class yes; tier no | R5:510 |
| `16_PESSIMIST_CHAR_C_the_stop_is_the_mans` | B10 | IN (CHAR) | 01_CORE_reason_trail_in_the_act_store (B09); 16_PESSIMIST_CHAR_B_a_pursuit_does_what_ (B10); U5a_CHAR_owed_amendments (B10) | — | none unarmed; armed re-records | yes (5 readings) | class yes; tier no | R5:511 |
| `17_CENSUS_C1A_02_wires_and_corrections` | B10 | IN | 02_CHAR_scar_cap_and_regard_unit (B10); 02_CHAR_which_ground_moves_whom (B24, cut); 11_GO_player_surface_contract_B (B34, cut); 14_VERBS_BINDING_A_formation (B21, cut); 14_VERBS_MATERIAL_C_works (B12, cut); 14_VERBS_MILITARY_A_movement (B22, cut); 14_VERBS_MILITARY_C_the_muster (B22, cut); 14_VERBS_MILITARY_D_the_order_of_battle (B22, cut); U5a_CHAR_owed_amendments (B10) | — | W4 none at control | yes | class yes (Edit / small build); tier no | R5:547 |
| `U5a_CHAR_owed_amendments` | B10 | IN | 12_ARCS_arcs_as_staged_goals (B10) | — | §2, §4, §7, §8, §3 at their flips | yes | cost yes; tier no | R2:333 |
| `U5a_CHAR_self_knowledge_is_a_belief` | B10 | IN | 02_CHAR_capability_uses_table (B04); U5c_SC_one_obstacle_form (B05) | — | build hash once at seeding | yes | cost yes; tier no | R2:334 |
| `08_FI_01_claim-sourced-referents` | B11 | FI | — | — | every realm world | yes (`r08_probe.py` — scratch) | cost yes; tier no | R2:358 |
| `08_FI_02_rumour-that-travels` | B11 | FI | U5c_FI_residue (B11) | — | each arm | yes (`dynamics.py` — scratch) | cost yes; tier no | R2:359 |
| `08_FI_03_playable-inquiry` | B11 | FI | U5c_FI_residue (B11) | — | §2 onward | yes | cost yes; tier no | R2:360 |
| `08_FI_04_small-edits` | B11 | FI | — | — | §1–§4 | yes | cost yes; tier no | R2:361 |
| `08_FI_06_testimony-names-a-hand` | B11 | FI | — | — | `told_pairing` on | yes | cost yes; tier no | R2:364 |
| `08_FI_07_shortest-playable-case` | B11 | FI | 08_FI_03_playable-inquiry (B11); 08_FI_06_testimony-names-a-hand (B11) | — | §2 | yes | cost yes; tier no | R2:365 |
| `14_VERBS_SOCIAL1_A_formation` | B11 | SC | 02_CHAR_offer_what_can_be_done (B10); 08_FI_02_rumour-that-travels (B11) | `present_persons` | declared | Y | edit; no tier | R4:476 |
| `16_PESSIMIST_FI_A_what_a_rumour_can_garble` | B11 | FI | 08_FI_02_rumour-that-travels (B11); 08_FI_06_testimony-names-a-hand (B11) | — | every world with a Partial telling or a lie on an existence reading (3 | yes (`p2_proxy.py`, `told_dump.py`, `p1c | class yes; tier no | R5:517 |
| `16_PESSIMIST_FI_C_what_a_deed_leaves_behind` | B11 | FI (IN for edit 4) | 08_FI_01_claim-sourced-referents (B11); 08_FI_02_rumour-that-travels (B11) | — | declared hash mover | yes (6 probe rows + `test_fi03_trail.py` | class yes; tier no | R5:519 |
| `16_PESSIMIST_SC_E_an_honest_teller_is_not_marked` | B11 | SC (FI, IN) | — | — | partial `tell`/`lie` of a number reaching a firsthand holder | yes | class yes (Edit); tier no | R5:539 |
| `18_DETERMINISM_notice_is_a_draw` | B11 | FI (IN) | 05_SC_hearing_capabilities (B04); 18_DETERMINISM_task_draw_for_uncontested (B07); U1 | — | every world with a deed and a non-party witness at `on` | yes (3; planted worlds) | class yes (Small build); tier no | R5:554 |
| `19_LACUNA_conclusion_is_a_committed_assertion` | B11 | FI | 08_FI_03_playable-inquiry (B11); U5c_FI_residue (B11) | — | when `reconstruct` folds | yes | cost yes; tier no | R2:372 |
| `U5c_FI_residue` | B11 | FI | — | — | §6 to §8 | yes | cost yes; tier no | R2:357 |
| `07_SE_arc_needs` | B12 | SE | — | — | amount flip | yes | small build / none | R3:233 |
| `07_SE_capability_and_chooser_surface` | B12 | SE | 07_SE_capability_rate_B (B12) | — | none | yes (superseded) | edit / none | R3:235 |
| `07_SE_capability_rate_B` | B12 | SE (CORE/CHAR) | 01_CORE_capability_authoring_surface (B04); 02_CHAR_capability_uses_table (B04); 18_DETERMINISM_task_draw_for_uncontested (B07); U5a_capability_home_and_two_inputs (B04) | — | none while no rate row; `effect_rate_gain` | yes | edit, after CORE and CHAR / none | R3:236 |
| `07_SE_ground_and_granaries` | B12 | SE | 07_SE_treasury_granary_B (B12); 21_PROCEDURAL_D_world_cards_and_churn (B39, cut) | — | three flips | yes | small build / none | R3:237 |
| `07_SE_kernel_repairs` | B12 | SE | — | — | B, C, D | yes | edit / none | R3:238 |
| `07_SE_population_census` | B12 | SE | 07_SE_population_regrowth_B (B12); 09_WR_B_draws_not_thresholds (B12) | — | `hunger_loss`, `famine_loss` flips | yes | small build / none | R3:239 |
| `07_SE_population_regrowth_B` | B12 | SE | 07_SE_population_census (B12); 20_NARRATIVE_E_the_year_and_the_reason (B38, cut) | — | flip | yes | small build / none | R3:240 |
| `07_SE_treasury_granary_B` | B12 | SE | 07_SE_ground_and_granaries (B12) | — | part of `ground` flip | yes | edit / none | R3:241 |
| `07_SE_valley_scenario` | B12 | SE | — | — | none | yes | small build / none | R3:242 |
| `09_WR_B_draws_not_thresholds` | B12 | WR | 09_WR_strand_conclusion (B12); 09_WR_world_motion (B12); 30_WR_A_the_era_is_a_named_period (B38, cut) | — | e1, e2 with control | yes | small build / edit / none | R3:248 |
| `09_WR_B_weather_with_memory_and_the_year` | B12 | WR | 30_WR_A_the_era_is_a_named_period (B38, cut) | — | none at shipped | yes | edit / small build / none | R3:252 |
| `09_WR_provided_arcs` | B12 | WR | 12_ARCS_arcs_as_staged_goals (B10) | — | e1, e2 with control | yes | small build / edit / none | R3:253 |
| `09_WR_strand_conclusion` | B12 | WR | — | — | e1 EQUAL; e2, e3 movers | yes | edit / small build / none | R3:255 |
| `09_WR_world_motion` | B12 | WR | 09_WR_B_draws_not_thresholds (B12, cut REV by U6 R-A: the draws file builds on this one, C3-V4); 16_PESSIMIST_WR_B_the_calamity_strains_a (B12; edit 1's flip only) | — | per edit with control | yes | small build / edit / none | R3:257 |
| `14_VERBS_MATERIAL_A_mending` | B12 | SE | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 07_SE_kernel_repairs (B12); 08_FI_01_claim-sourced-referents (B11); 18_DETERMINISM_task_draw_for_uncontested (B07); U5c_SC_one_obstacle_form (B05); U5c_VERBS_residue_and_governance_owner (B07) | `holders_named` | 4 commits | Y | small; no tier | R4:458 |
| `14_VERBS_MATERIAL_B_stores` | B12 | SE | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 07_SE_arc_needs (B12); 07_SE_kernel_repairs (B12); 07_SE_treasury_granary_B (B12); 14_VERBS_MATERIAL_A_mending (B12) | — | 3 | Y | small; no tier | R4:459 |
| `14_VERBS_MATERIAL_C_works` | B12 | SE | 08_FI_04_small-edits (B11); 14_VERBS_MATERIAL_A_mending (B12); 14_VERBS_SOCIAL2_A_formation_on_what_is_ (B25, cut) | — | declared | Y | small; no tier | R4:460 |
| `16_PESSIMIST_GAME_the_world_draws` | B12 | IN | 07_SE_ground_and_granaries (B12); 09_WR_B_draws_not_thresholds (B12) | — | control `()` reproduces; shipped moves | yes (test + `x3_famine.py` falsifier, no | class yes (Edit); tier no | R5:523 |
| `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted` | B12 | SE (edit 4 PC) | 03_PC_exits_withdrawal_recovery (B16, cut); 07_SE_ground_and_granaries (B12); 07_SE_population_census (B12); 07_SE_treasury_granary_B (B12); 16_PESSIMIST_GAME_the_world_draws (B12) | — | edit 3 every hash with a hunger fall; edit 4 realm season 1; edit 2 se | yes (6; test files named) | class yes ("Small"); tier no | R5:540 |
| `16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate` | B12 | SE (edit 3 consumer MB) | 07_SE_treasury_granary_B (B12); 09_WR_B_draws_not_thresholds (B12) | — | yield receipts move hashes; walls none at one garrison | yes (4) | class yes ("Small"); tier no | R5:541 |
| `16_PESSIMIST_WR_A_the_road_is_drawn` | B12 | WR | 07_SE_kernel_repairs (B12); 09_WR_B_weather_with_memory_and_the_year (B12) | — | when `road_hazard` flips (own commit); off = base | yes | class yes (Small build); tier no | R5:542 |
| `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks` | B12 | WR | 09_WR_B_threadwork_session_and_practitio (B35, cut); 09_WR_world_motion (B12); 16_PESSIMIST_GAME_the_world_draws (B12); U5d_WR_owed_edits (B12) | — | none while `lattice_coupling` = 0; the flip is a mover | yes | class yes; tier no | R5:543 |
| `U5d_SE_owed_edits` | B12 | SE | 16_PESSIMIST_SE_B_harvest_walls_and_the_ (B12) | — | per section | yes | edits / small build / none | R3:244 |
| `U5d_WR_owed_edits` | B12 | WR | 16_PESSIMIST_WR_B_the_calamity_strains_a (B12); 16_PESSIMIST_WR_C_illness_on_the_body_la (B37, cut); 22_HAPPENINGS_A_a_death_is_rare_caused_a (B37, cut) | — | §3 | yes | edits / none | R3:267 |
| `03_PC_typed_outcome_one_door` | B14 | PC | 18_DETERMINISM_no_certain_matchup (B15, cut); U5a_DICE_owed_edits (B05) | — | two declared (`standing`, `fell_to`) | yes | yes / no | R1:377 |
| `03_PC_weapon_form_at_round_start` | B14 | PC | — | — | armour reference only | yes | yes / no | R1:378 |
| `03_PC_weapon_records_in_the_export` | B14 | PC (+GO) | — | — | none | yes | yes / no | R1:379 |
| `16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight` | B14 | PC | 03_PC_typed_outcome_one_door (B14) | — | every log with a fight (`Event.observed` is hashed) | yes (4) | class yes; tier no | R5:533 |
| `U5b_PC_residue` | B14 | PC | 10_DICE_believed_odds_have_a_prior (B05) | — | §7, §8 | yes per section | yes / no | R1:381 |
| `14_VERBS_PHYSICAL_A_custody_and_force` | B15 | PC | 03_PC_duel_chain_reach (B01); 03_PC_duel_round_and_approach_B (B16, cut); 03_PC_exits_withdrawal_recovery (B16, cut); 06_FA_remit_grant_by_row (B21, cut); LANE-A | — | declared re-records | Y (four test files, unnamed) | build; no tier | R4:467 |
| `16_PESSIMIST_PC_A_the_yield_is_a_draw` | B15 | PC | 02_CHAR_resolve_and_temper (B10); 03_PC_exits_withdrawal_recovery (B16, cut); 14_VERBS_PHYSICAL_A_custody_and_force (B15) | — | every world with a fight | yes (5; probes `pB_yield.py` not in repo | class yes (Small build); tier no | R5:531 |
| `16_PESSIMIST_PC_B_the_commit_window` | B15 | PC | 03_PC_duel_round_and_approach_B (B16, cut) | — | every world with a fight | yes (4) | class yes; tier no | R5:532 |
| `16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw` | B15 | PC | 03_PC_duel_round_and_approach_B (B16, cut); 18_DETERMINISM_no_certain_matchup (B15) | — | every world with a fight | yes (4) | class yes; tier no | R5:534 |
| `18_DETERMINISM_no_certain_matchup` | B15 | PC | 03_PC_duel_round_and_approach_B (B16, cut); 03_PC_typed_outcome_one_door (B14); 14_VERBS_PHYSICAL_A_custody_and_force (B15) | — | every world with a decided season fight | yes (3) | class yes (Small edit + re-pin); tier no | R5:555 |
| `U5b_PC_rulings_in_the_fight` | B15 | PC (+MB) | 14_VERBS_PHYSICAL_A_custody_and_force (B15); 22_HAPPENINGS_C_a_killing_is_a_crime_som (B37, cut); U5a_DICE_owed_edits (B05); U5a_capability_home_and_two_inputs (B04) | — | per section | yes per section | yes / no | R1:380 |
| `03_PC_duel_round_and_approach` | B16 | PC | 03_PC_duel_round_and_approach_B (B16) | — | step 2 re-seeds every fight | yes | yes / no | R1:372 |
| `03_PC_duel_round_and_approach_B` | B16 | PC | 02_CHAR_choice_alignment (B10); 03_PC_duel_round_and_approach (B16); 11_GO_one_draw_owner (B06); 16_PESSIMIST_PC_A_the_yield_is_a_draw (B15); 18_DETERMINISM_no_certain_matchup (B15); U5b_PC_rulings_in_the_fight (B15) | `PersonInterior` | steps 2, 3e (none in season), 4, 5 | yes per step | yes / no | R1:373 |
| `03_PC_exits_withdrawal_recovery` | B16 | PC | 14_VERBS_PHYSICAL_A_custody_and_force (B15); 18_DETERMINISM_task_draw_for_uncontested (B07) | — | Part B (if ruled), Part C live | yes | yes / no | R1:374 |
| `04_MB_headcount_grade_and_scale` | B17 | MB (IN seam) | U5d_FA_land_and_seats_pass_on_a_won_marc (B23, cut) | — | yes | yes | yes / no | R1:385 |
| `04_MB_typed_outcome_and_one_path` | B17 | MB (IN) | 04_MB_headcount_grade_and_scale (B17) | — | gate row 5 only | yes | yes / no | R1:389 |
| `04_MB_unit_loadout_and_weapon_in_hand` | B17 | MB | — | — | — | (n/a) | yes / no | R1:390 |
| `04_MB_unit_loadout_and_weapon_in_hand_B` | B17 | MB | 03_PC_loadout_and_carry (B18, cut); 03_PC_weapon_records_in_the_export (B14) | — | stage 4 | yes per stage | yes / no | R1:391 |
| `U5b_MB_residue` | B17 | MB | 07_SE_campaign_supply_and_muster (B22, cut); 10_DICE_believed_odds_have_a_prior (B05) | — | none | yes | yes / no | R1:404 |
| `03_PC_loadout_and_carry` | B18 | PC (+MB) | 03_PC_duel_round_and_approach_B (B16); 03_PC_weapon_records_in_the_export (B14); 04_MB_unit_loadout_and_weapon_in_hand_B (B17) | — | only persons with a secondary | yes | yes / no | R1:375 |
| `03_PC_person_inputs_content` | B18 | PC | U1; U5b_PC_residue (B14) | — | yes (Part B/D) | yes | yes / no | R1:376 |
| `04_MB_cell_hierarchy_as_data` | B19 | MB | 04_MB_headcount_grade_and_scale (B17); 04_MB_unit_loadout_and_weapon_in_hand_B (B17); 16_PESSIMIST_MB_partition_and_the_pair_r (B19) | — | `arm: grid` flip | yes | yes / no | R1:383 |
| `04_MB_cr12_linear_law` | B19 | MB | 16_PESSIMIST_MB_partition_and_the_pair_r (B19); U5b_MB_rulings_in_the_field (B19) | — | yes (step 3) | yes | yes / no | R1:384 |
| `16_PESSIMIST_MB_one_stamina_ledger` | B19 | MB (input IN) | 04_MB_unit_loadout_and_weapon_in_hand_B (B17); 26_MASS_BATTLE_movement_and_fatigue_as_d (B31, cut); 27_MB_E_what_an_army_carries_back (B22, cut) | — | steps 1-2 none; step 3 default equal | yes (one test, unnamed) | class yes; tier no | R5:529 |
| `16_PESSIMIST_MB_partition_and_the_pair_rule` | B19 | MB | 04_MB_cr12_linear_law (B19); 04_MB_headcount_grade_and_scale (B17); U5b_MB_rulings_in_the_field (B19) | — | every fought field; goldens under `engine/tests/` re-recorded once | yes (6 rows; tests "in the file that cov | class yes (Design-first); tier no | R5:528 |
| `16_PESSIMIST_MB_rout_has_two_exits` | B19 | MB | 04_MB_typed_outcome_and_one_path (B17); 14_VERBS_PHYSICAL_A_custody_and_force (B15); 26_MASS_BATTLE_rout_pursuit_and_giving_g (B19); 27_MB_A_command_and_the_obedience_draw (B19) | — | every field ending in a rout | yes (4 rows; test unnamed) | class yes (Small build); tier no | R5:530 |
| `26_MASS_BATTLE_calibration_targets` | B19 | MB | — | — | none (instrument) | yes | yes / no | R1:393 |
| `26_MASS_BATTLE_cell_scale_and_time` | B19 | MB | 04_MB_cell_hierarchy_as_data (B19); 04_MB_headcount_grade_and_scale (B17); 04_MB_manager_battle_one_resolver (B20, cut); 04_MB_typed_outcome_and_one_path (B17) | — | three flips | yes | yes / no | R1:394 |
| `26_MASS_BATTLE_rout_pursuit_and_giving_ground` | B19 | MB | 04_MB_manager_battle_one_resolver (B20, cut); 04_MB_typed_outcome_and_one_path (B17); 16_PESSIMIST_MB_rout_has_two_exits (B19) | — | `stand_draw` flip | yes | yes / no | R1:397 |
| `27_MB_A_command_and_the_obedience_draw` | B19 | MB (IN, CORE) | 04_MB_manager_battle_one_resolver (B20, cut); 26_MASS_BATTLE_cell_scale_and_time (B19); U5a_capability_home_and_two_inputs (B04) | — | none at `obey: off` | yes | yes / yes (sonnet, opus critique) | R1:398 |
| `27_MB_C_dynamic_strength_and_the_residual_chance` | B19 | MB | 26_MASS_BATTLE_calibration_targets (B19); 27_MB_A_command_and_the_obedience_draw (B19); U5b_MB_rulings_in_the_field (B19) | — | yes (27C-1, 27C-3) | yes | yes / yes (sonnet; opus judgment node) | R1:400 |
| `U5b_MB_rulings_in_the_field` | B19 | MB (IN) | U5a_DICE_owed_edits (B05); U5d_FA_land_and_seats_pass_on_a_won_marc (B23, cut) | — | every fought field (re-pin) | yes | yes / no | R1:403 |
| `04_MB_manager_battle_one_resolver` | B20 | MB | 03_PC_duel_round_and_approach_B (B16); 04_MB_headcount_grade_and_scale (B17); 04_MB_typed_outcome_and_one_path (B17); U5b_PC_rulings_in_the_fight (B15) | — | none with no orders | yes | yes / no | R1:386 |
| `04_MB_playable_field_scenario` | B20 | MB (+IN, FA) | 04_MB_headcount_grade_and_scale (B17); 04_MB_typed_outcome_and_one_path (B17); 14_VERBS_MILITARY_C_the_muster (B22, cut); 14_VERBS_MILITARY_D_the_order_of_battle (B22, cut) | — | declared flips | yes | yes / no | R1:387 |
| `26_MASS_BATTLE_maneuver_orders` | B20 | MB | 04_MB_manager_battle_one_resolver (B20); 26_MASS_BATTLE_cell_scale_and_time (B19); 27_MB_A_command_and_the_obedience_draw (B19) | — | with orders | yes | yes / no | R1:395 |
| `27_MB_D_the_commander_as_chooser` | B20 | MB (CHAR) | 04_MB_manager_battle_one_resolver (B20); 10_DICE_believed_odds_have_a_prior (B05); 27_MB_A_command_and_the_obedience_draw (B19) | — | none with no decider | yes | yes / yes (27D-4 INCOMPLETE) | R1:401 |
| `06_FA_decree_binds` | B21 | FA | 14_VERBS_BINDING_C_turnover (B21); 16_PESSIMIST_FA_C_under_the_seat (B21); U5d_FA_owed_edits (B21) | — | each of the 5 edits, own revert | yes (`fa_probe`/`aperture`) | small build / none | R3:223 |
| `06_FA_levy_through_the_seat_B` | B21 | FA (cross MB) | 06_FA_war_lives_in_seats_B (B23, cut) | — | none computed | yes | small build / none | R3:225 |
| `06_FA_playable_scenario` | B21 | FA | 06_FA_decree_binds (B21); 06_FA_seat_terms_and_turnover (B21); 22_HAPPENINGS_B_the_throne_is_never_stra (B21) | — | spine build hash | yes | small build / none | R3:227 |
| `06_FA_remit_grant_by_row` | B21 | FA | 22_HAPPENINGS_B_the_throne_is_never_stra (B21) | — | realm hash | yes | edit / none | R3:228 |
| `06_FA_seat_terms_and_turnover` | B21 | FA | — | — | steps 1-5 EQUAL; row authoring, ban scope movers | yes | small build / none | R3:229 |
| `06_FA_seat_terms_by_body_B` | B21 | FA | 06_FA_remit_grant_by_row (B21); 06_FA_seat_terms_and_turnover (B21) | — | 2 | yes | edit (data) / none | R3:230 |
| `06_FA_shortest_loop_B` | B21 | FA | 06_FA_decree_binds (B21); 06_FA_playable_scenario (B21) | — | none | yes | small build (harness) / none | R3:231 |
| `14_VERBS_BINDING_A_formation` | B21 | FA | 05_SC_obstacle_difficulty_and_modifiers_ (B05); U5c_SC_one_obstacle_form (B05); U5c_VERBS_residue_and_governance_owner (B07) | — | 3 commits, each declared | Y (`aperture 2 0/2 1`) | small; no tier | R4:448 |
| `14_VERBS_BINDING_C_turnover` | B21 | FA | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 06_FA_decree_binds (B21); 06_FA_playable_scenario (B21); 06_FA_remit_grant_by_row (B21); 06_FA_seat_terms_and_turnover (B21); 14_VERBS_BINDING_A_formation (B21) | — | C2..C4 movers | Y | medium; no tier | R4:450 |
| `14_VERBS_BINDING_D_orders` | B21 | FA | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 06_FA_decree_binds (B21); 06_FA_remit_grant_by_row (B21) | `dispatch` | D1..D4 | Y | medium; no tier | R4:451 |
| `16_PESSIMIST_FA_A_dismissal_survives_the_king` | B21 | FA | 06_FA_decree_binds (B21); 06_FA_seat_terms_and_turnover (B21); 14_VERBS_BINDING_C_turnover (B21); 22_HAPPENINGS_B_the_throne_is_never_stra (B21) | — | none at build (falsifier ran in memory: `pf6_fixcheck.py`, not in repo | yes (G1-G4 + tests `test_in31_revocation | class yes (Edit, data); tier no | R5:514 |
| `16_PESSIMIST_FA_B_who_may_sit_join_and_declare` | B21 | FA | 06_FA_remit_grant_by_row (B21); 06_FA_war_lives_in_seats_B (B23, cut); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_VENICE_C_roll_lot_ballot (B32, cut) | — | (3) every run in which a person commits to a faction Proposition he is | yes (G1-G4) | class yes (Edit; small build for edit 3) | R5:515 |
| `16_PESSIMIST_FA_C_under_the_seat` | B21 | FA | 06_FA_decree_binds (B21); 06_FA_levy_through_the_seat_B (B21); 14_VERBS_BINDING_D_orders (B21); 15_INSTITUTIONS_COLONIAL_B_distance (B33, cut) | — | issue widens, dispatch narrows (FA E-3: 12 executed `dispatch` in two  | yes (G1-G3, probe `pf2_premise.py` not i | class yes (Small build); tier no | R5:516 |
| `22_HAPPENINGS_B_the_throne_is_never_stranded` | B21 | FA | 06_FA_remit_grant_by_row (B21); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_BYZANTINE_E_accession_re (B32, cut); 15_INSTITUTIONS_SYNTHESIS_B_the_deed_led (B32, cut); 16_PESSIMIST_FA_A_dismissal_survives_the (B21) | — | none at build; after a royal death | yes (G1-G3 in `test_in61_heir_hears_vaca | class yes (Edit + small build); tier no | R5:570 |
| `U5d_FA_owed_edits` | B21 | FA | 14_VERBS_BINDING_C_turnover (B21); 14_VERBS_BINDING_D_orders (B21); 15_INSTITUTIONS_PAPACY_B_patronage_elect (B32, cut); 21_PROCEDURAL_B_cast_and_seats (B39, cut); 22_HAPPENINGS_B_the_throne_is_never_stra (B21) | `[unverified]`, `via` | per section | yes | edits / small builds / design-first / no | R3:246 |
| `07_SE_campaign_supply_and_muster` | B22 | SE (cross MB) | 07_SE_ground_and_granaries (B12) | `[UNVERIFIED]`, `under_arms` | each flip | yes | small build, split / none | R3:234 |
| `14_VERBS_MILITARY_A_movement` | B22 | MB | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 16_PESSIMIST_MB_one_stamina_ledger (B19); 18_DETERMINISM_task_draw_for_uncontested (B07); 26_MASS_BATTLE_movement_and_fatigue_as_d (B31, cut); 27_MB_E_what_an_army_carries_back (B22); U1; U5c_VERBS_residue_and_governance_owner (B07) | — | 6 | Y | small; no tier | R4:463 |
| `14_VERBS_MILITARY_B_train` | B22 | MB | 01_CORE_capability_authoring_surface (B04); 05_SC_obstacle_difficulty_and_modifiers_ (B05); 14_VERBS_MILITARY_A_movement (B22); U1 | — | formation + execution | Y | small; no tier | R4:464 |
| `14_VERBS_MILITARY_C_the_muster` | B22 | MB | 06_FA_levy_through_the_seat_B (B21); 07_SE_campaign_supply_and_muster (B22); 14_VERBS_MILITARY_A_movement (B22); 27_MB_A_command_and_the_obedience_draw (B19); 27_MB_E_what_an_army_carries_back (B22) | `may_wage`, `state/gate.py::may_levy`, `world_q.py:2186`, `world_q.raisable_by` | 1 mover at shipped fixtures | Y | small, 3 owners; no tier | R4:465 |
| `14_VERBS_MILITARY_D_the_order_of_battle` | B22 | MB | 04_MB_headcount_grade_and_scale (B17); 14_VERBS_MILITARY_C_the_muster (B22); 26_MASS_BATTLE_maneuver_orders (B20); 27_MB_A_command_and_the_obedience_draw (B19); 27_MB_B_unit_prowess_on_the_row (B31, cut); 27_MB_E_what_an_army_carries_back (B22) | — | none at shipped | Y | small; no tier | R4:466 |
| `14_VERBS_PHYSICAL_B_field_and_ruin` | B22 | MB | 04_MB_headcount_grade_and_scale (B17); 06_FA_remit_grant_by_row (B21); 06_FA_war_lives_in_seats_B (B23, cut); U5b_VERBS_military_physical_residue (B07) | — | all realm pins with `march`/`raze` | Y | build; no tier | R4:468 |
| `27_MB_E_what_an_army_carries_back` | B22 | MB (WR, SE) | 04_MB_typed_outcome_and_one_path (B17); 16_PESSIMIST_MB_one_stamina_ledger (B19); 16_PESSIMIST_MB_rout_has_two_exits (B19); 26_MASS_BATTLE_rout_pursuit_and_giving_g (B19) | — | `recuperation: on`, `carry: on` | yes | yes / yes | R1:402 |
| `06_FA_war_lives_in_seats_B` | B23 | FA | U5d_FA_land_and_seats_pass_on_a_won_marc (B23) | — | one test | yes | edit, ruled / none | R3:232 |
| `14_VERBS_BINDING_E_war_seats` | B23 | FA | 04_MB_playable_field_scenario (B20); 06_FA_levy_through_the_seat_B (B21); 06_FA_remit_grant_by_row (B21); 14_VERBS_PHYSICAL_B_field_and_ruin (B22); U5d_FA_land_and_seats_pass_on_a_won_marc (B23) | — | E2, E3 each | Y | small; no tier | R4:452 |
| `26_MASS_BATTLE_aggression_and_land` | B23 | MB | 04_MB_headcount_grade_and_scale (B17); 04_MB_manager_battle_one_resolver (B20); U5d_FA_land_and_seats_pass_on_a_won_marc (B23) | — | none of its own | yes | yes / no | R1:392 |
| `U5d_FA_land_and_seats_pass_on_a_won_march` | B23 | FA | 06_FA_remit_grant_by_row (B21); 06_FA_war_lives_in_seats_B (B23); 09_WR_strand_conclusion (B12); 14_VERBS_MATERIAL_D_paper (B26, cut); 16_PESSIMIST_FA_B_who_may_sit_join_and_d (B21); 26_MASS_BATTLE_aggression_and_land (B23) | `[unverified]`, `passage_granted` | per commit | yes (arms a-i) | small build; design-first levels / none | R3:245 |
| `02_CHAR_which_ground_moves_whom` | B24 | IN | 05_SC_evidence_and_rebuttal_B (B24) | — | on the 18 hearers | yes | cost yes; tier no | R2:332 |
| `05_SC_evidence_and_rebuttal` | B24 | SC | — | — | — | — | — | R2:342 |
| `05_SC_evidence_and_rebuttal_B` | B24 | SC | 05_SC_playable_hearing_B (B24); 08_FI_05_evidence-interface_B (B24); 19_LACUNA_admission_rides_the_citing_dra (B24) | — | when `cites` is on | yes (`build_hearing`) | cost yes; tier no | R2:343 |
| `05_SC_negotiation_scene` | B24 | SC | 05_SC_playable_hearing_B (B24) | `exchange` | when built | yes | cost yes (design-first); tier no | R2:345 |
| `05_SC_playable_hearing` | B24 | SC | — | — | — | — | — | R2:348 |
| `05_SC_playable_hearing_B` | B24 | SC | 05_SC_evidence_and_rebuttal_B (B24) | — | when `sitting_exchanges` leaves 0 | yes | cost yes; tier no | R2:349 |
| `05_SC_sc05_kernel_disposition_B` | B24 | SC | 05_SC_playable_hearing_B (B24) | — | none | yes | cost yes; tier no | R2:350 |
| `05_SC_sc05_kernel_retirement` | B24 | SC | — | — | — | — | — | R2:351 |
| `08_FI_05_evidence-interface` | B24 | FI | — | — | — | — | — | R2:362 |
| `08_FI_05_evidence-interface_B` | B24 | FI | 05_SC_evidence_and_rebuttal_B (B24); 05_SC_playable_hearing_B (B24); 08_FI_06_testimony-names-a-hand (B11); 08_FI_07_shortest-playable-case (B11); 19_LACUNA_admission_rides_the_citing_dra (B24) | — | nothing until SC builds | yes | cost yes; tier no | R2:363 |
| `12_ARCS_cited_evidence` | B24 | SC | 05_SC_evidence_and_rebuttal_B (B24); 19_LACUNA_admission_rides_the_citing_dra (B24) | — | at the control none | yes | cost yes; tier no | R2:369 |
| `19_LACUNA_admission_rides_the_citing_draw` | B24 | SC / FI | 05_SC_evidence_and_rebuttal_B (B24) | — | when built | yes | cost yes; tier no | R2:371 |
| `08_FI_08_knots-season-form` | B25 | FI | 08_FI_02_rumour-that-travels (B11) | — | none now | yes | cost yes; tier no | R2:366 |
| `14_VERBS_SOCIAL2_A_formation_on_what_is_known` | B25 | FI | 08_FI_02_rumour-that-travels (B11); 14_VERBS_SOCIAL2_B_a_word_with_content (B25); 14_VERBS_SOCIAL2_C_case_question_confess (B25) | — | declared (every world) | Y | edit + small; no tier | R4:480 |
| `14_VERBS_SOCIAL2_B_a_word_with_content` | B25 | SC | 08_FI_01_claim-sourced-referents (B11); 08_FI_05_evidence-interface_B (B24); 14_VERBS_SOCIAL2_A_formation_on_what_is_ (B25) | — | declared at the shipped arm | Y | small; no tier | R4:481 |
| `14_VERBS_SOCIAL2_C_case_question_confession` | B25 | SC | 05_SC_evidence_and_rebuttal_B (B24); 05_SC_playable_hearing_B (B24); 08_FI_02_rumour-that-travels (B11); 08_FI_06_testimony-names-a-hand (B11); 14_VERBS_SOCIAL2_A_formation_on_what_is_ (B25) | — | declared | Y | small each | R4:482 |
| `14_VERBS_SOCIAL2_D_tie` | B25 | FI | 08_FI_02_rumour-that-travels (B11); 08_FI_08_knots-season-form (B25) | `53ed995d` | verb count 67 -> 68 | Y | small; no tier | R4:483 |
| `14_VERBS_MATERIAL_D_paper` | B26 | FI | 02_CHAR_offer_what_can_be_done (B10); 08_FI_01_claim-sourced-referents (B11); 08_FI_02_rumour-that-travels (B11); 08_FI_05_evidence-interface_B (B24); 14_VERBS_MATERIAL_A_mending (B12) | — | 5 | Y | small, 5 movers; no tier | R4:461 |
| `14_VERBS_MATERIAL_E_knowledge` | B26 | FI | 08_FI_03_playable-inquiry (B11); 08_FI_04_small-edits (B11); 08_FI_06_testimony-names-a-hand (B11); 14_VERBS_MATERIAL_A_mending (B12); 14_VERBS_MATERIAL_D_paper (B26); 19_LACUNA_conclusion_is_a_committed_asse (B11) | — | declared | Y | small; no tier | R4:462 |
| `14_VERBS_PHYSICAL_C_looking` | B26 | FI | 08_FI_03_playable-inquiry (B11); 08_FI_04_small-edits (B11) | — | declared re-records | Y | edit + small build; no tier | R4:469 |
| `16_PESSIMIST_FI_B_a_paper_is_about_something` | B26 | FI | 08_FI_05_evidence-interface_B (B24); 18_DETERMINISM_notice_is_a_draw (B11); 19_LACUNA_admission_rides_the_citing_dra (B24) | — | none for edits 1-3 (no holder doubts a held paper at seeds 0-2); edit  | yes (`p3b_knows.py`, `p3_forgery.py`: no | class yes (Edit); tier no | R5:518 |
| `16_PESSIMIST_FI_D_withhold_what_has_no_product` | B26 | FI (fixture IN) | 08_FI_03_playable-inquiry (B11); 19_LACUNA_conclusion_is_a_committed_asse (B11) | — | declared hash mover for every seeded realm (157 of 1,394 acts) | yes (`fi_arms.py`: not in repo) | class yes (Edit); tier no | R5:520 |
| `19_LACUNA_questioning_has_an_approach_and_a_cost` | B26 | FI | 14_VERBS_SOCIAL2_C_case_question_confess (B25) | — | when `interview`/`interrogate` fold | yes | cost yes; tier no | R2:373 |
| `05_SC_acquittal` | B27 | SC | — | — | yes | yes (`test_u7_remit.py` §10) | cost yes; tier no | R2:338 |
| `05_SC_arrangement_rows_that_bind` | B27 | SC | — | — | when a row is re-authored | yes (`test_arrangements.py`) | cost yes; tier no | R2:339 |
| `16_PESSIMIST_SC_C_a_verdict_names_its_party` | B27 | SC (IN, CHAR) | 05_SC_acquittal (B27); 08_FI_06_testimony-names-a-hand (B11) | — | worlds with `matter.determined` or `arrest.made` | yes | class yes; tier no | R5:537 |
| `16_PESSIMIST_SC_D_an_argument_moves_someone` | B27 | SC | 02_CHAR_which_ground_moves_whom (B24); 08_FI_04_small-edits (B11) | — | every world where an `argue` is rolled | yes (probes not in repo; `harness/convic | class yes; tier no | R5:538 |
| `19_LACUNA_verdict_ladder_and_reversal` | B27 | SC | 05_SC_acquittal (B27); 05_SC_evidence_and_rebuttal_B (B24); 09_WR_B_chronicle_that_tells (B36, cut) | — | mistrial, reversal | yes | cost yes; tier no | R2:374 |
| `U5c_SC_proceedings_residue` | B27 | SC | 16_PESSIMIST_SC_C_a_verdict_names_its_pa (B27); 16_PESSIMIST_SC_D_an_argument_moves_some (B27) | — | §4 to §7 | yes | cost yes; tier no | R2:356 |
| `14_VERBS_SOCIAL1_B_documents_and_obedience` | B28 | SC | 06_FA_decree_binds (B21); 14_VERBS_SOCIAL1_A_formation (B11); LANE-A; U5c_VERBS_residue_and_governance_owner (B07) | — | declared | Y | small; no tier | R4:477 |
| `14_VERBS_SOCIAL1_C_persuasion_and_deceit` | B28 | SC | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 14_VERBS_SOCIAL1_D_grievance_and_settlem (B28); LANE-A | — | declared | Y | small | R4:478 |
| `14_VERBS_SOCIAL1_D_grievance_and_settlement` | B28 | SC | 14_VERBS_PHYSICAL_A_custody_and_force (B15); 14_VERBS_SOCIAL1_B_documents_and_obedien (B28); LANE-A | — | declared | Y | small-medium; no tier | R4:479 |
| `28_CORE_scene_access_A_occupancy_and_precedence` | B28 | IN | 14_VERBS_SOCIAL1_A_formation (B11); 16_PESSIMIST_CORE_a_scene_runs_in_its_ow (B08); 18_DETERMINISM_rival_acts_in_one_fold (B08); U5c_SC_one_obstacle_form (B05) | — | `occupancy` off the control; levels off `None` | yes (12 rows, with named tests) | **cost yes; tier yes** (`valoria-author` | R2:375 |
| `28_CORE_scene_access_B_appointments` | B28 | IN | 14_VERBS_SOCIAL2_B_a_word_with_content (B25); 28_CORE_scene_access_A_occupancy_and_pre (B28) | — | `appointments: on` | yes | cost yes; tier yes | R2:376 |
| `04_MB_squad_grid_of_named_characters` | B30 | MB | 03_PC_duel_round_and_approach_B (B16) | — | squad fields | yes | yes / no | R1:388 |
| `04_MB_campaign_party_economy` | B31 | MB | 04_MB_typed_outcome_and_one_path (B17); 04_MB_unit_loadout_and_weapon_in_hand_B (B17) | — | yes (veterancy on; arrears) | yes | yes / no | R1:382 |
| `26_MASS_BATTLE_movement_and_fatigue_as_data` | B31 | MB | 04_MB_unit_loadout_and_weapon_in_hand_B (B17); 16_PESSIMIST_MB_one_stamina_ledger (B19) | — | three flips | yes | yes / no | R1:396 |
| `27_MB_B_unit_prowess_on_the_row` | B31 | MB | 04_MB_cr12_linear_law (B19); 04_MB_unit_loadout_and_weapon_in_hand_B (B17) | — | none | yes | yes / yes (sonnet) | R1:399 |
| `14_VERBS_BINDING_B_sittings` | B32 | FA | 05_SC_acquittal (B27); 05_SC_arrangement_rows_that_bind (B27); 05_SC_obstacle_difficulty_and_modifiers_ (B05); 05_SC_playable_hearing_B (B24) | — | B1..B4 each | Y | small; no tier | R4:449 |
| `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll` | B32 | FA | 06_FA_office_capabilities (B04); 06_FA_remit_grant_by_row (B21); 14_VERBS_BINDING_C_turnover (B21) | — | build | Y | small | R4:494 |
| `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd` | B32 | FA | 05_SC_arrangement_rows_that_bind (B27); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_BYZANTINE_A_dignities_an (B32) | — | any `succeed`/`revoke` | Y | small | R4:498 |
| `15_INSTITUTIONS_COLONIAL_A_instruments` | B32 | FA | 06_FA_decree_binds (B21) | — | EQUAL empty | Y (`test_instruments.py`) | small | R4:501 |
| `15_INSTITUTIONS_PAPACY_A_ground` | B32 | FA | 06_FA_remit_grant_by_row (B21) | — | build (one person) | Y | edit | R4:507 |
| `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline` | B32 | FA | 13_SC_draw_for_unrolled_contests (B07); 14_VERBS_BINDING_C_turnover (B21) | — | declared | Y | small | R4:508 |
| `15_INSTITUTIONS_SYNTHESIS_A_one_kit` | B32 | FA | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 14_VERBS_BINDING_D_orders (B21); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_SYNTHESIS_B_the_deed_led (B32); U5c_SC_one_obstacle_form (B05) | — | EQUAL until used | Y | edit + small; no tier | R4:489 |
| `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger` | B32 | FA | 05_SC_evidence_and_rebuttal_B (B24); 12_ARCS_case_on_the_realm (B39, cut); 14_VERBS_BINDING_C_turnover (B21); 14_VERBS_SOCIAL2_B_a_word_with_content (B25); 15_INSTITUTIONS_SYNTHESIS_A_one_kit (B32) | — | declared build mover | Y | small; no tier | R4:490 |
| `15_INSTITUTIONS_VENICE_C_roll_lot_ballot` | B32 | FA | 06_FA_seat_terms_and_turnover (B21); 06_FA_seat_terms_by_body_B (B21); 13_SC_draw_for_unrolled_contests (B07); 14_VERBS_BINDING_B_sittings (B32) | — | EQUAL with keys null | Y | small + design-first (e8) | R4:516 |
| `17_CENSUS_REST_2_wiring` | B32 | MB (W1), SC (W2), WR (W3), FA  | 04_MB_manager_battle_one_resolver (B20); 05_SC_playable_hearing_B (B24); 14_VERBS_PHYSICAL_D_thread_read (B35, cut); 15_INSTITUTIONS_PAPACY_B_patronage_elect (B32); U1 | — | W3 a declared mover of every pin where a sensitive person tells such a | yes | class yes (Edit / small build); tier no | R5:552 |
| `15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc` | B33 | FA | 07_SE_treasury_granary_B (B12); 14_VERBS_MATERIAL_B_stores (B12); 15_INSTITUTIONS_BYZANTINE_A_dignities_an (B32) | — | any `requisition` | Y | small | R4:495 |
| `15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain` | B33 | FA | 06_FA_decree_binds (B21); 13_SC_draw_for_unrolled_contests (B07); 14_VERBS_BINDING_D_orders (B21); 14_VERBS_SOCIAL1_D_grievance_and_settlem (B28) | — | any seat with `passes_through` | Y | small | R4:496 |
| `15_INSTITUTIONS_BYZANTINE_D_the_empire_at_a_distance` | B33 | FA | 15_INSTITUTIONS_BYZANTINE_C_the_hands_of (B33) | — | foreign-arm build | Y | edit + small | R4:497 |
| `15_INSTITUTIONS_COLONIAL_B_distance` | B33 | FA | 05_SC_obstacle_difficulty_and_modifiers_ (B05); 06_FA_office_capabilities (B04); 14_VERBS_BINDING_D_orders (B21); 14_VERBS_MATERIAL_B_stores (B12); 14_VERBS_MATERIAL_D_paper (B26); U5c_SC_one_obstacle_form (B05) | `world_q.root_of` | declared | Y (`test_remove.py`) | small | R4:502 |
| `15_INSTITUTIONS_COLONIAL_C_audit_and_charter` | B33 | FA | 05_SC_acquittal (B27); 05_SC_arrangement_rows_that_bind (B27); 05_SC_obstacle_difficulty_and_modifiers_ (B05); 06_FA_seat_terms_and_turnover (B21) | — | EQUAL until docketed | Y (`test_audit_and_charter.py`) | edit + small | R4:503 |
| `15_INSTITUTIONS_COLONIAL_D_accomplishment` | B33 | FA | 12_ARCS_case_on_the_realm (B39, cut); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_SYNTHESIS_B_the_deed_led (B32) | — | build mover | Y (`test_accomplishment.py`, stale) | small | R4:504 |
| `15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger` | B33 | FA | 05_SC_evidence_and_rebuttal_B (B24); 12_ARCS_cited_evidence (B24); 14_VERBS_SOCIAL2_B_a_word_with_content (B25) | — | build | Y | small | R4:509 |
| `15_INSTITUTIONS_PAPACY_D_sanction_and_absolution` | B33 | FA | 05_SC_acquittal (B27); 05_SC_arrangement_rows_that_bind (B27); 06_FA_decree_binds (B21); 14_VERBS_BINDING_B_sittings (B32); 14_VERBS_BINDING_D_orders (B21) | — | declared | Y | small | R4:510 |
| `15_INSTITUTIONS_PAPACY_E_sees_tithe_orders_legates_council` | B33 | FA | 06_FA_decree_binds (B21); 06_FA_remit_grant_by_row (B21); 06_FA_seat_terms_and_turnover (B21); 14_VERBS_BINDING_A_formation (B21); 15_INSTITUTIONS_PAPACY_B_patronage_elect (B32) | — | build (three Offices) | Y | edit | R4:511 |
| `15_INSTITUTIONS_SYNTHESIS_C_crossings` | B33 | FA | 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_PAPACY_D_sanction_and_ab (B33); 15_INSTITUTIONS_SYNTHESIS_A_one_kit (B32); 15_INSTITUTIONS_VENICE_A_obligation_and_ (B33); 15_INSTITUTIONS_VENICE_B_debt_instrument (B33) | — | none until used | Y | small | R4:491 |
| `15_INSTITUTIONS_VENICE_A_obligation_and_the_ask` | B33 | FA | 05_SC_contest_record_on_event (B05); 05_SC_obstacle_difficulty_and_modifiers_ (B05); U5c_SC_one_obstacle_form (B05) | — | EQUAL at ship | Y | small | R4:514 |
| `15_INSTITUTIONS_VENICE_B_debt_instrument` | B33 | FA | 05_SC_acquittal (B27); 05_SC_arrangement_rows_that_bind (B27); 07_SE_treasury_granary_B (B12); 15_INSTITUTIONS_VENICE_A_obligation_and_ (B33) | — | EQUAL when no act names `kind` and `amount` | Y | small | R4:515 |
| `15_INSTITUTIONS_VENICE_D_houses_charters_and_content` | B33 | FA | 06_FA_office_capabilities (B04); 06_FA_remit_grant_by_row (B21); 14_VERBS_MATERIAL_B_stores (B12); 15_INSTITUTIONS_VENICE_A_obligation_and_ (B33); 15_INSTITUTIONS_VENICE_B_debt_instrument (B33); 15_INSTITUTIONS_VENICE_C_roll_lot_ballot (B32) | — | each row | Y | edit + small | R4:517 |
| `01_CORE_one_scene_contract` | B34 | IN | 05_SC_playable_hearing_B (B24); 11_GO_player_surface_contract_B (B34) | — | none with no host; edit 5 moves nothing | yes (echo control, no-host hash) | cost yes; tier no | R2:312 |
| `11_GO_fidelity_and_campaign_modes` | B34 | GO (IN) | 11_GO_player_surface_contract_B (B34) | — | none in automated run | yes | yes / no | R1:414 |
| `11_GO_player_surface_contract` | B34 | GO | — | — | — | (n/a) | yes / no | R1:417 |
| `11_GO_player_surface_contract_B` | B34 | GO (IN, CHAR) | 08_FI_05_evidence-interface_B (B24) | `PersonInterior` | none in automated run | yes | yes / no | R1:418 |
| `16_PESSIMIST_GO_the_offer_names_what_is_held` | B34 | IN / CHAR | 11_GO_player_surface_contract_B (B34) | — | ledgers at build and questions formed from them | yes (5) | class yes (Edit + small build); tier no | R5:527 |
| `09_WR_B_threadwork_session_and_practitioner` | B35 | WR | 09_WR_threadwork_module (B03); 17_CENSUS_C1B_01_deletions (B03) | `modules/threadwork/`, `seam/wrappers/threadwork.py` | none (EQUAL) | yes | small build / edit / design-first / none | R3:251 |
| `12_ARCS_substrate_as_ground` | B35 | WR | 16_PESSIMIST_WR_B_the_calamity_strains_a (B12); U5d_WR_zero_coherence_unknowable (B35) | — | yes | yes | cost yes (design-first); tier no | R2:370 |
| `14_VERBS_PHYSICAL_D_thread_read` | B35 | WR | 08_FI_03_playable-inquiry (B11); 09_WR_threadwork_module (B03) | `_eff_thread_read` | realm pins (4 sensitive persons) | Y | edit / small build; no tier | R4:470 |
| `U5d_WR_zero_coherence_unknowable` | B35 | WR | 01_CORE_reason_trail_in_the_act_store (B09); 10_DICE_believed_odds_have_a_prior (B05); 11_GO_player_surface_contract_B (B34) | `Person.coherence` | none until a writer | yes | design-first / none | R3:268 |
| `09_WR_B_chronicle_that_tells` | B36 | WR | 09_WR_B_readings_of_closure_and_tension (B36); 11_GO_player_surface_contract_B (B34); 17_CENSUS_C1A_01_deletion_batches (B03) | `telling.yaml` | none (EQUAL) | yes | small build / none | R3:247 |
| `09_WR_B_readings_of_closure_and_tension` | B36 | WR | 09_WR_B_chronicle_that_tells (B36) | — | none | yes | small build / none | R3:250 |
| `09_WR_story_instruments_that_can_fail` | B36 | WR | — | — | none | yes | edit / small build / none | R3:254 |
| `16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings` | B36 | WR | 09_WR_B_readings_of_closure_and_tension (B36); 09_WR_B_threadwork_session_and_practitio (B35); 16_PESSIMIST_WR_B_the_calamity_strains_a (B12) | — | none expected (asserted) | yes | class yes; tier no | R5:545 |
| `17_CENSUS_C1B_02_wires` | B36 | IN | 09_WR_B_readings_of_closure_and_tension (B36); 09_WR_B_threadwork_session_and_practitio (B35); 09_WR_threadwork_module (B03); 12_ARCS_case_on_the_realm (B39, cut) | — | none | yes (run output named) | class yes; tier no | R5:549 |
| `20_NARRATIVE_F_story_inventory_and_gate` | B36 | WR (IN) | 09_WR_B_chronicle_that_tells (B36); 09_WR_B_readings_of_closure_and_tension (B36); 09_WR_story_instruments_that_can_fail (B36); 09_WR_strand_conclusion (B12); 20_NARRATIVE_A_stands_for (B38, cut) | — | none | yes (a 5-command bar that fails today) | class yes (Small build); tier no | R5:563 |
| `23_STORY_D_story_census_and_gate` | B36 | WR (IN) | 07_SE_valley_scenario (B12); 09_WR_story_instruments_that_can_fail (B36); 16_PESSIMIST_CORE_the_record_holds_what_ (B09); 16_PESSIMIST_GAME_standing_occasions_car (B09); 20_NARRATIVE_F_story_inventory_and_gate (B36) | — | none | yes (4 commands; "the bar failing on tod | class yes (Small build); tier no | R5:576 |
| `16_PESSIMIST_WR_C_illness_on_the_body_ladder` | B37 | WR | 09_WR_B_draws_not_thresholds (B12); 22_HAPPENINGS_A_a_death_is_rare_caused_a (B37); U5d_WR_owed_edits (B12) | — | one re-pin when the rate leaves zero | yes (file found by `grep -rl body_hazard | class yes; tier no | R5:544 |
| `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` | B37 | IN | 03_PC_exits_withdrawal_recovery (B16); 09_WR_world_motion (B12); 10_DICE_one_roller_one_fraction_rule (B05); 14_VERBS_PHYSICAL_A_custody_and_force (B15); 16_PESSIMIST_WR_C_illness_on_the_body_la (B37); 21_PROCEDURAL_B_cast_and_seats (B39, cut) | — | `Person.born` at the control (every world hash); on: one re-pin | yes (3 arms in `test_in34_bodies_clock.p | class yes (small build); tier no | R5:569 |
| `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits` | B37 | PC (FI) | 02_CHAR_relations_have_a_ground (B10); 08_FI_06_testimony-names-a-hand (B11); 08_FI_07_shortest-playable-case (B11); 14_VERBS_PHYSICAL_A_custody_and_force (B15); 16_PESSIMIST_CHAR_C_the_stop_is_the_mans (B10); 18_DETERMINISM_notice_is_a_draw (B11); 22_HAPPENINGS_B_the_throne_is_never_stra (B21) | — | wherever the context is met (none at build, unverified) | yes (formation, 200-attempt access arm,  | class yes (design-first then small build | R5:571 |
| `22_HAPPENINGS_D_batches_and_added_gates` | B37 | IN | 16_PESSIMIST_FA_A_dismissal_survives_the (B21) | — | the five-line edit moves every world hash (co-location) | yes (probe of off-ground seat-holds: cou | class: ordering text plus one data edit; | R5:572 |
| `20_NARRATIVE_A_stands_for` | B38 | WR (CHAR) | 02_CHAR_scar_is_a_wound (B10); 08_FI_02_rumour-that-travels (B11); 09_WR_story_instruments_that_can_fail (B36); 09_WR_strand_conclusion (B12); 30_WR_B_regimes_who_believes_whom (B38); 30_WR_G_regime_opinions_and_the_pull_of_ (B38); 31_WR_A_house_cores_and_the_cast_on_the_ (B38) | — | `held_reading: stands` (commit 2) every realm season with a told claim | yes (5) | class yes (Edit); tier no | R5:558 |
| `20_NARRATIVE_B_what_he_was_owed` | B38 | WR (FA, CHAR) | 20_NARRATIVE_C_who_holds_what (B38); 28_CORE_scene_access_C_the_petition_that (B38); 30_WR_D_momentum_and_its_brakes (B38); U5c_SC_proceedings_residue (B27) | — | `dues_valence` live | yes (5; two worlds) | class yes; tier no | R5:559 |
| `20_NARRATIVE_C_who_holds_what` | B38 | WR (FA) | 06_FA_seat_terms_and_turnover (B21); 06_FA_seat_terms_by_body_B (B21); 06_FA_war_lives_in_seats_B (B23); 18_DETERMINISM_notice_is_a_draw (B11); 30_GO_F_the_plot_as_the_player_is_shown_ (B38); 30_WR_A_the_era_is_a_named_period (B38) | — | three commits, each a declared mover with a control | yes (6) | class yes (Small build); tier no | R5:560 |
| `20_NARRATIVE_D_his_own_side` | B38 | WR / FA | 20_NARRATIVE_A_stands_for (B38); 20_NARRATIVE_C_who_holds_what (B38); 30_WR_D_momentum_and_its_brakes (B38); 31_WR_A_house_cores_and_the_cast_on_the_ (B38) | — | commit 2 (4 rows) and `stamp_own_side True` | yes (5) | class yes (Edit); tier no | R5:561 |
| `20_NARRATIVE_E_the_year_and_the_reason` | B38 | WR | 01_CORE_reason_trail_in_the_act_store (B09); 06_FA_seat_terms_by_body_B (B21); 09_WR_B_chronicle_that_tells (B36); 09_WR_B_weather_with_memory_and_the_year (B12); 09_WR_story_instruments_that_can_fail (B36); 16_PESSIMIST_CHAR_A_a_crisis_of_faith_is (B10) | — | edit 1, 2 none; edit 3 superseded | yes (3) | class yes (Edit; small build for 3); tie | R5:562 |
| `23_STORY_A_what_a_roll_leaves` | B38 | IN | 02_CHAR_relations_have_a_ground (B10); 02_CHAR_what_an_act_risks (B10); 05_SC_contest_record_on_event (B05); 08_FI_06_testimony-names-a-hand (B11); 10_DICE_exported_face_rule_and_band_edge (B05); 16_PESSIMIST_CORE_the_record_holds_what_ (B09); 18_DETERMINISM_task_draw_for_uncontested (B07); 30_WR_D_momentum_and_its_brakes (B38) | — | none at ship (`shortfall_scale: off`); declared per executing staked r | yes (5 + a planted test) | class yes (Small build); tier no | R5:573 |
| `28_CORE_scene_access_C_the_petition_that_waits` | B38 | IN | 14_VERBS_SOCIAL1_D_grievance_and_settlem (B28); 20_NARRATIVE_B_what_he_was_owed (B38); 20_NARRATIVE_C_who_holds_what (B38); 23_STORY_D_story_census_and_gate (B36); 28_CORE_scene_access_A_occupancy_and_pre (B28); 28_CORE_scene_access_B_appointments (B28); U5c_SC_one_obstacle_form (B05) | — | fixtures off controls | yes | cost yes; tier yes | R2:377 |
| `30_GO_F_the_plot_as_the_player_is_shown_it` | B38 | GO (IN, CHAR) | 11_GO_player_surface_contract_B (B34); 20_NARRATIVE_C_who_holds_what (B38); 20_NARRATIVE_E_the_year_and_the_reason (B38); 23_STORY_D_story_census_and_gate (B36); 30_WR_A_the_era_is_a_named_period (B38); 30_WR_C_strands_open_grow_join_conclude (B38); 30_WR_G_regime_opinions_and_the_pull_of_ (B38) | — | none (EQUAL) | yes | yes / yes (sonnet) | R1:421 |
| `30_WR_A_the_era_is_a_named_period` | B38 | WR | 06_FA_war_lives_in_seats_B (B23); 09_WR_strand_conclusion (B12); 12_ARCS_arcs_as_staged_goals (B10); 20_NARRATIVE_C_who_holds_what (B38); 22_HAPPENINGS_B_the_throne_is_never_stra (B21); 23_STORY_B_a_house_continues (B39, cut); U5d_FA_land_and_seats_pass_on_a_won_marc (B23) | — | c3 | yes | small build; sonnet + opus critic | R3:258 |
| `30_WR_B_regimes_who_believes_whom` | B38 | WR | 16_PESSIMIST_CHAR_A_a_crisis_of_faith_is (B10); 20_NARRATIVE_A_stands_for (B38); 20_NARRATIVE_D_his_own_side (B38); 20_NARRATIVE_E_the_year_and_the_reason (B38) | — | none | yes | small build; sonnet | R3:259 |
| `30_WR_C_strands_open_grow_join_conclude` | B38 | WR | 09_WR_B_draws_not_thresholds (B12); 09_WR_strand_conclusion (B12); 20_NARRATIVE_A_stands_for (B38); 20_NARRATIVE_B_what_he_was_owed (B38); 28_CORE_scene_access_C_the_petition_that (B38) | — | 1b | yes | small build; opus (1a) + sonnet critic | R3:260 |
| `30_WR_D_momentum_and_its_brakes` | B38 | WR (IN) | 20_NARRATIVE_A_stands_for (B38); 20_NARRATIVE_B_what_he_was_owed (B38); 20_NARRATIVE_C_who_holds_what (B38); 20_NARRATIVE_D_his_own_side (B38); 20_NARRATIVE_E_the_year_and_the_reason (B38); 23_STORY_A_what_a_roll_leaves (B38); 27_MB_E_what_an_army_carries_back (B22); 28_CORE_scene_access_A_occupancy_and_pre (B28); 28_CORE_scene_access_B_appointments (B28); 28_CORE_scene_access_C_the_petition_that (B38) | — | none | yes | edit; sonnet | R3:261 |
| `30_WR_E_cascade_chains_and_the_census` | B38 | WR | 09_WR_story_instruments_that_can_fail (B36); 20_NARRATIVE_F_story_inventory_and_gate (B36); 23_STORY_D_story_census_and_gate (B36); 30_WR_A_the_era_is_a_named_period (B38); 30_WR_B_regimes_who_believes_whom (B38); 30_WR_C_strands_open_grow_join_conclude (B38); 30_WR_D_momentum_and_its_brakes (B38) | — | none | yes | small build; sonnet + critic | R3:262 |
| `30_WR_G_regime_opinions_and_the_pull_of_ones_own` | B38 | WR (CHAR) | 20_NARRATIVE_A_stands_for (B38); 30_WR_B_regimes_who_believes_whom (B38); 31_WR_A_house_cores_and_the_cast_on_the_ (B38) | — | c2 build; c4 `accord`; c5 | yes | edit/small build; sonnet + opus (c4, c5) | R3:263 |
| `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes` | B38 | WR (CHAR) | 20_NARRATIVE_A_stands_for (B38); 30_WR_B_regimes_who_believes_whom (B38); 30_WR_G_regime_opinions_and_the_pull_of_ (B38) | — | c2 build | yes | edit / authoring / small build; sonnet,  | R3:264 |
| `31_WR_B_the_revival_gathers` | B38 | WR (CHAR) | 02_CHAR_resolve_and_temper (B10); 16_PESSIMIST_CHAR_A_a_crisis_of_faith_is (B10); 30_WR_G_regime_opinions_and_the_pull_of_ (B38); 31_WR_A_house_cores_and_the_cast_on_the_ (B38) | — | c1 above 0; c2 | yes | small build; opus (c1) + sonnet critic | R3:265 |
| `31_WR_C_what_the_stances_feed` | B38 | WR (FA, GO) | 15_INSTITUTIONS_SYNTHESIS_B_the_deed_led (B32); 20_NARRATIVE_D_his_own_side (B38); 30_GO_F_the_plot_as_the_player_is_shown_ (B38); 31_WR_A_house_cores_and_the_cast_on_the_ (B38); U5d_FA_owed_edits (B21) | `BYZANTINE_E`, `None`, `VENICE_C`, `axis:` | none (EQUAL) | yes | edit / small build; sonnet | R3:266 |
| `U5d_SE_cohort_heavy_moves_and_caste` | B38 | SE | 16_PESSIMIST_SE_A_the_granary_shares_and (B12); 31_WR_A_house_cores_and_the_cast_on_the_ (B38); 31_WR_B_the_revival_gathers (B38); 31_WR_C_what_the_stances_feed (B38); U5d_FA_owed_edits (B21) | — | (1) every realm run | yes | edit / design-first / data+build, no tie | R3:243 |
| `01_CORE_case_setup_and_beats` | B39 | IN | 12_ARCS_case_on_the_realm (B39) | — | none for un-authored cases | yes (beats matched, off-arm) | cost yes; tier no | R2:310 |
| `12_ARCS_case_on_the_realm` | B39 | WR/IN | 21_PROCEDURAL_C_prologue_and_case_seeds (B39) | — | none | yes | cost yes; tier no | R2:368 |
| `21_PROCEDURAL_A_worldgen_tables_and_ground` | B39 | WR / SE | 07_SE_ground_and_granaries (B12); 07_SE_population_census (B12); 09_WR_B_draws_not_thresholds (B12); 09_WR_B_weather_with_memory_and_the_year (B12) | — | off = base hash; PG-1 flips are declared movers | yes (PG-0: 4 tests; PG-1: `--range 20` r | class yes (small build each); tier no | R5:564 |
| `21_PROCEDURAL_B_cast_and_seats` | B39 | WR / CHAR / FA | 01_CORE_capability_authoring_surface (B04); 02_CHAR_capability_definitions (B04); 02_CHAR_relations_have_a_ground (B10); 06_FA_seat_terms_and_turnover (B21); 06_FA_seat_terms_by_body_B (B21); 07_SE_population_census (B12); 08_FI_01_claim-sourced-referents (B11); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_BYZANTINE_A_dignities_an (B32); 15_INSTITUTIONS_COLONIAL_D_accomplishmen (B33); 15_INSTITUTIONS_VENICE_B_debt_instrument (B33); 21_PROCEDURAL_A_worldgen_tables_and_grou (B39); 22_HAPPENINGS_A_a_death_is_rare_caused_a (B37); U1; U5d_SE_cohort_heavy_moves_and_caste (B38) | — | `cast_quota: {}` = PG-1 hash; on: every world | yes (PG-2 and PG-3 gates) | class yes (design-first D-1 answered; sm | R5:565 |
| `21_PROCEDURAL_C_prologue_and_case_seeds` | B39 | WR / FI | 08_FI_05_evidence-interface_B (B24); 08_FI_06_testimony-names-a-hand (B11); 08_FI_07_shortest-playable-case (B11); 12_ARCS_cited_evidence (B24); 14_VERBS_PHYSICAL_A_custody_and_force (B15); 14_VERBS_PHYSICAL_C_looking (B26); 14_VERBS_SOCIAL2_C_case_question_confess (B25); 19_LACUNA_conclusion_is_a_committed_asse (B11); 19_LACUNA_verdict_ladder_and_reversal (B27); 20_NARRATIVE_E_the_year_and_the_reason (B38); 21_PROCEDURAL_A_worldgen_tables_and_grou (B39); U5d_GO_owed_edits (B06) | `scenes_per_season` | PG-4 with a prologue every hash; PG-5 case cards on | yes (PG-4; PG-5 a-e; PG-5a fallback name | class yes (small build; design-first for | R5:566 |
| `21_PROCEDURAL_D_world_cards_and_churn` | B39 | WR / FA | 01_CORE_case_setup_and_beats (B39); 02_CHAR_goal_lean_on_its_own_question (B10); 12_ARCS_arcs_as_staged_goals (B10); 12_ARCS_case_on_the_realm (B39); 14_VERBS_BINDING_B_sittings (B32); 21_PROCEDURAL_A_worldgen_tables_and_grou (B39) | — | empty pools = base hash | yes (PG-6, PG-7; docket if released) | class yes (small build; docket design-fi | R5:567 |
| `21_PROCEDURAL_E_names_and_texts` | B39 | WR | 21_PROCEDURAL_B_cast_and_seats (B39) | — | names enter the world hash; colour does not | yes (import-time enumeration; `--names 1 | class yes (Edit once lists authored); ti | R5:568 |
| `23_STORY_B_a_house_continues` | B39 | SE / FA | 07_SE_population_regrowth_B (B12); 13_SC_draw_for_unrolled_contests (B07); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_SYNTHESIS_A_one_kit (B32); 20_NARRATIVE_E_the_year_and_the_reason (B38); 21_PROCEDURAL_B_cast_and_seats (B39); 22_HAPPENINGS_A_a_death_is_rare_caused_a (B37); 22_HAPPENINGS_B_the_throne_is_never_stra (B21); 23_STORY_A_what_a_roll_leaves (B38) | — | none at ship (`birth_rate` 0, `majority_age` 0); live: A-75 | yes (5 + planted) | class yes (Small build; edit 2-3 design- | R5:574 |
| `23_STORY_C_a_founded_place_can_fail` | B39 | SE | 07_SE_population_regrowth_B (B12); 14_VERBS_MATERIAL_A_mending (B12); 14_VERBS_MATERIAL_C_works (B12); 14_VERBS_MILITARY_A_movement (B22); 18_DETERMINISM_task_draw_for_uncontested (B07); 23_STORY_A_what_a_roll_leaves (B38) | — | only worlds that hold such a rung; dark at control | yes (5 + planted) | class yes (Small build; the matrix cell  | R5:575 |
| `23_STORY_E_first_playable_the_lean_year` | B39 | SE (all lanes meet) | 05_SC_playable_hearing_B (B24); 07_SE_valley_scenario (B12); 08_FI_07_shortest-playable-case (B11); 12_ARCS_case_on_the_realm (B39); 14_VERBS_BINDING_C_turnover (B21); 22_HAPPENINGS_A_a_death_is_rare_caused_a (B37); 23_STORY_D_story_census_and_gate (B36); 30_GO_F_the_plot_as_the_player_is_shown_ (B38) | `harness/valley.py`, `valley.yaml` | none (no other world's hash moves) | yes (5 readings; plus the loader test) | class yes (Edit + small build, one sessi | R5:577 |
| `U5d_STORY_owed_edits` | B39 | WR (+SE, MB, PC) | 07_SE_ground_and_granaries (B12); 09_WR_B_draws_not_thresholds (B12); 14_VERBS_MATERIAL_A_mending (B12); 16_PESSIMIST_FI_C_what_a_deed_leaves_beh (B11); 18_DETERMINISM_notice_is_a_draw (B11); 22_HAPPENINGS_C_a_killing_is_a_crime_som (B37) | `[unverified]`, `besiege` | each declared | yes | edits / small build / none | R3:269 |
| `15_INSTITUTIONS_BYZANTINE_F_playable_scenarios_and_reading` | B40 | FA | 06_FA_playable_scenario (B21); 15_INSTITUTIONS_BYZANTINE_A_dignities_an (B32); 15_INSTITUTIONS_BYZANTINE_B_the_roga_and (B33); 15_INSTITUTIONS_BYZANTINE_C_the_hands_of (B33) | — | none | Y | small | R4:499 |
| `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms` | B40 | FA | 15_INSTITUTIONS_BYZANTINE_A_dignities_an (B32); 15_INSTITUTIONS_BYZANTINE_B_the_roga_and (B33); 15_INSTITUTIONS_BYZANTINE_C_the_hands_of (B33); 15_INSTITUTIONS_BYZANTINE_D_the_empire_a (B33); 15_INSTITUTIONS_BYZANTINE_E_accession_re (B32); 15_INSTITUTIONS_BYZANTINE_F_playable_sce (B40); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_COLONIAL_C_audit_and_cha (B33); 15_INSTITUTIONS_VENICE_C_roll_lot_ballot (B32) | — | EQUAL with rows absent | Y | edit | R4:500 |
| `15_INSTITUTIONS_COLONIAL_E_scenario` | B40 | FA | 06_FA_playable_scenario (B21); 07_SE_valley_scenario (B12); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_COLONIAL_B_distance (B33); 15_INSTITUTIONS_COLONIAL_C_audit_and_cha (B33); 15_INSTITUTIONS_COLONIAL_D_accomplishmen (B33) | — | none | Y | small | R4:505 |
| `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds` | B40 | FA | 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_COLONIAL_B_distance (B33); 15_INSTITUTIONS_COLONIAL_C_audit_and_cha (B33); 15_INSTITUTIONS_COLONIAL_D_accomplishmen (B33); 15_INSTITUTIONS_COLONIAL_E_scenario (B40); 15_INSTITUTIONS_VENICE_grounding_E_what_ (B40) | — | EQUAL absent | Y | small | R4:506 |
| `15_INSTITUTIONS_PAPACY_F_playable_vacant_chair` | B40 | FA | 06_FA_playable_scenario (B21); 14_VERBS_BINDING_C_turnover (B21); 15_INSTITUTIONS_PAPACY_A_ground (B32); 15_INSTITUTIONS_PAPACY_B_patronage_elect (B32) | — | none | Y | small | R4:512 |
| `15_INSTITUTIONS_PAPACY_grounding_mechanisms` | B40 | FA | 15_INSTITUTIONS_PAPACY_B_patronage_elect (B32); 15_INSTITUTIONS_PAPACY_D_sanction_and_ab (B33); 15_INSTITUTIONS_PAPACY_E_sees_tithe_orde (B33) | — | EQUAL absent | Y | small | R4:513 |
| `15_INSTITUTIONS_SYNTHESIS_D_first_playable` | B40 | FA | 06_FA_playable_scenario (B21); 12_ARCS_case_on_the_realm (B39) | — | none (harness) | Y | small; no tier | R4:492 |
| `15_INSTITUTIONS_SYNTHESIS_E_implementation_plan` | B40 | IN | — | — | — | Y (SYN_D) | none; no tier | R4:493 |
| `15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds` | B40 | FA | 06_FA_remit_grant_by_row (B21); 15_INSTITUTIONS_COLONIAL_A_instruments (B32); 15_INSTITUTIONS_COLONIAL_C_audit_and_cha (B33); 15_INSTITUTIONS_SYNTHESIS_A_one_kit (B32); 15_INSTITUTIONS_VENICE_B_debt_instrument (B33); 15_INSTITUTIONS_VENICE_D_houses_charters (B33) | — | EQUAL absent | Y | edit + small | R4:518 |
| `11_GO_port_gate_order_and_coverage` | B41 | GO (IN) | 16_PESSIMIST_GO_surface_pins (B41) | `tools/export_oracle_pins.py` | none in loop; 91 env reads -> literals (hash EQUAL) | yes | yes / no | R1:420 |
| `16_PESSIMIST_GO_surface_pins` | B41 | GO / IN | — | `harness/port_oracle.py`, `tools/export_oracle_pins.py` | none | yes (3 rows; `probe.py trunc` not in rep | class yes (Small build + ~150 strings);  | R5:524 |

## 4. Edges removed (the cycle breaks)

### 4.1 Every edge removed to make the graph acyclic

Categories: **SPLIT** the dependent part lands in the named later batch; **REV** the read lane recorded the reverse relation (the target depends on, or is re-pointed by, the source); **SUP** the dependency is on an item a decision superseded; **LATER** the source works at its control and the target only widens its reach; **LANDED** already built by lane A.

| # | from (batch) | to (batch) | category | reason |
|---|---|---|---|---|
| 0 | `03_PC_duel_chain_reach` (B01) | `14_VERBS_PHYSICAL_A_custody_and_force` (B15) | LANDED | lane A's e5d6ab9 already built the reach; `14_VERBS_PHYSICAL_A` A4 then A3 follow it (`U5b_PC_rulings_in_the_fight.md` §5 rows 2 and 5) |
| 1 | `11_GO_pointer_and_stale_text_resolutions` (B03) | `11_GO_one_draw_owner` (B06) | SPLIT | item 5 (the GO-16/draw row) lands in B06 with the draw owner; items 1-4, 6-11 are hash-equal text |
| 2 | `17_CENSUS_C1A_01_deletion_batches` (B03) | `02_CHAR_voices_and_the_room` (B10) | REV | C-U5a-15: D2 deletes caller-less `world_q.projection`/`witnessed`; the four files are re-pointed to `account` and depend on D2, not the reverse |
| 3 | `17_CENSUS_C1A_01_deletion_batches` (B03) | `19_LACUNA_verdict_ladder_and_reversal` (B27) | REV | as row 2 (C-U5a-15) |
| 4 | `17_CENSUS_C1A_01_deletion_batches` (B03) | `11_GO_player_surface_contract_B` (B34) | REV | as row 2 (C-U5a-15); GO-B builds `account`, the reading the re-pointed files use |
| 5 | `17_CENSUS_C1A_01_deletion_batches` (B03) | `09_WR_B_threadwork_session_and_practitioner` (B35) | REV | as row 2 (C-U5a-15) |
| 6 | `17_CENSUS_C1A_01_deletion_batches` (B03) | `09_WR_B_chronicle_that_tells` (B36) | REV | as row 2 (C-U5a-15) |
| 7 | `17_CENSUS_C1B_01_deletions` (B03) | `04_MB_unit_loadout_and_weapon_in_hand` (B17) | SUP | the edge is to the superseded first loadout file (`04_MB_unit_loadout_and_weapon_in_hand.md`, retracted by `_B`); the deletion of `ARMOURY`/`ARSENAL` merge text has no reader |
| 8 | `17_CENSUS_C1B_01_deletions` (B03) | `05_SC_sc05_kernel_disposition_B` (B24) | SPLIT | the C1B item that touches the SC05 kernel lands in B24 after `05_SC_playable_hearing_B` (the kernel disposition's own order: HEAR_B first) |
| 9 | `17_CENSUS_REST_1_deletions` (B03) | `10_DICE_one_roller_one_fraction_rule` (B05) | SUP | C-U5a-18: D1 row 1 stands whatever the dice proposals do (no reader of `pool_size` is gained under A-5) |
| 10 | `17_CENSUS_REST_1_deletions` (B03) | `U5a_DICE_owed_edits` (B05) | SUP | as row 9 (C-U5a-18) |
| 11 | `17_CENSUS_REST_1_deletions` (B03) | `08_FI_04_small-edits` (B11) | SPLIT | the D-row that needs `08_FI_04` lands in B11 with it |
| 12 | `U5a_CORE_owed_edits` (B03) | `11_GO_player_surface_contract_B` (B34) | SPLIT | the item of `U5a_CORE_owed_edits.md` that cites GO-B §8 lands in B34; sections A-C, E, F, I are hash-equal and land in B03 |
| 13 | `05_SC_hearing_capabilities` (B04) | `05_SC_playable_hearing_B` (B24) | SPLIT | definition rows (`law`, `insight`, `deception`) land in B04; the `hearing_moves` rows land in B24 with HEAR_B |
| 14 | `U5a_capability_home_and_two_inputs` (B04) | `05_SC_obstacle_difficulty_and_modifiers_B` (B05) | SPLIT | CAP Part A (hash EQUAL) lands in B04; Part B lands in B05 with SC-B, the parity file, the soft ceiling and U5a_DICE §1 (CAP's own Order section) |
| 15 | `U5a_capability_home_and_two_inputs` (B04) | `05_SC_opposed_obstacle_parity` (B05) | SPLIT | as row 14 |
| 16 | `U5a_capability_home_and_two_inputs` (B04) | `16_PESSIMIST_DICE_soft_ceiling` (B05) | SPLIT | as row 14 |
| 17 | `U5a_capability_home_and_two_inputs` (B04) | `U5a_DICE_owed_edits` (B05) | SPLIT | as row 14 |
| 18 | `10_DICE_one_roller_one_fraction_rule` (B05) | `U5b_MB_rulings_in_the_field` (B19) | SPLIT | U3 decision C3-D2: `U5b_MB_rulings_in_the_field.md` §1 (the field's one sampler) lands in B05 with U5a_DICE §1 row 4, not at the head of the field batch |
| 19 | `16_PESSIMIST_DICE_task_difficulty_and_throughput` (B05) | `18_DETERMINISM_task_draw_for_uncontested_verbs` (B07) | SPLIT | the pessimist's text amendments to 18-A land with 18-A in B07 (C-U5a-07 already folded them); its T13/SC-B code lands in B05 |
| 20 | `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage` (B05) | `05_SC_evidence_and_rebuttal_B` (B24) | LATER | OBS §4 step 1b lands SC_A at the rate in force reading today's `world_q.proofs` (EX); EVID_B re-sources the proofs in B24 |
| 21 | `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage` (B05) | `19_LACUNA_admission_rides_the_citing_draw` (B24) | LATER | as row 20 (ADM sets entry in B24) |
| 22 | `29_DICE_one_opposed_rule_form_and_tuning` (B05) | `U5b_PC_rulings_in_the_fight` (B15) | SPLIT | 29_DICE rows 5-7 and 9 land with `U5b_PC_rulings_in_the_fight.md` §5 rows 4-5 in B15 (29_DICE's own Dependencies section); item 29-5 in B30 |
| 23 | `U5a_DICE_owed_edits` (B05) | `01_CORE_claim_fade_as_read` (B09) | SPLIT | U5a_DICE §4 (a failed search is remembered) lands in B09 with the refusal and fading owners; §1-§3 in B05 |
| 24 | `U5a_DICE_owed_edits` (B05) | `16_PESSIMIST_CORE_a_refusal_is_remembered` (B09) | SPLIT | as row 23 |
| 25 | `U5c_SC_one_obstacle_form` (B05) | `05_SC_evidence_and_rebuttal_B` (B24) | LATER | OBS composes the evidence member when EVID_B lands (B24); OBS §2-§5 need nothing from EVID_B; the proof unit is U1's (U3 ledger §11) |
| 26 | `U5b_VERBS_military_physical_residue` (B07) | `26_MASS_BATTLE_aggression_and_land` (B23) | SPLIT | RES-V §2-§3 (march under the land rulings; raze/seize) land in B23; §1 (shape) in B07; §4 (`mustered` excludes the restrained) in B22 |
| 27 | `U5b_VERBS_military_physical_residue` (B07) | `U5d_FA_land_and_seats_pass_on_a_won_march` (B23) | SPLIT | as row 26 |
| 28 | `U5c_VERBS_residue_and_governance_owner` (B07) | `16_PESSIMIST_CORE_a_refusal_is_remembered` (B09) | SPLIT | VRES §3 (a refusal teaches the actor) lands in B09 with the refusal owner |
| 29 | `U5c_VERBS_residue_and_governance_owner` (B07) | `08_FI_01_claim-sourced-referents` (B11) | SPLIT | VRES §6 and the `audience_of` reader that names `present_persons`/`holders_named` land in B11 after FI-01/FI-02 build them; §1-§2 in B07 |
| 30 | `U5c_VERBS_residue_and_governance_owner` (B07) | `08_FI_02_rumour-that-travels` (B11) | SPLIT | as row 29 |
| 31 | `U5c_VERBS_residue_and_governance_owner` (B07) | `05_SC_playable_hearing_B` (B24) | SPLIT | the hearing rows of VRES §2's prize roster (the `heard_by` audience for a hearing) land in B24 with HEAR_B |
| 32 | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` (B08) | `28_CORE_scene_access_A_occupancy_and_precedence` (B28) | REV | 28A depends on the scene order (A-9) and composes on it; the person key of `_canonical_order` is 28A's own edit (collision C3-K8) |
| 33 | `18_DETERMINISM_rival_acts_in_one_fold` (B08) | `28_CORE_scene_access_A_occupancy_and_precedence` (B28) | REV | as row 32 |
| 34 | `16_PESSIMIST_CORE_the_record_holds_what_changed` (B09) | `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told` (B10) | SUP | C-U5a-09: the record proposal emits `scar.taken` only; `conviction.moved` is CHAR_A's, so the record proposal does not depend on CHAR_A |
| 35 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `14_VERBS_MATERIAL_C_works` (B12) | SPLIT | C1A_02 W2's closing gate for each verb wire rides with that verb's batch (B12, B21, B22); W3 lands in B10 |
| 36 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `14_VERBS_BINDING_A_formation` (B21) | SPLIT | as row 35 |
| 37 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `14_VERBS_MILITARY_A_movement` (B22) | SPLIT | as row 35 |
| 38 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `14_VERBS_MILITARY_C_the_muster` (B22) | SPLIT | as row 35 |
| 39 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `14_VERBS_MILITARY_D_the_order_of_battle` (B22) | SPLIT | as row 35 |
| 40 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `02_CHAR_which_ground_moves_whom` (B24) | SPLIT | C-U5a-16: W4 is one term with the scar-cap Addendum (B10); its `which_ground` half lands in B24 |
| 41 | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | `11_GO_player_surface_contract_B` (B34) | SPLIT | W1 lands in B34 with GO-B |
| 42 | `07_SE_ground_and_granaries` (B12) | `21_PROCEDURAL_D_world_cards_and_churn` (B39) | LATER | a bounded drawn starting state (A-50) arrives with world cards (B39); the ground and granaries run at their control without it |
| 43 | `07_SE_population_regrowth_B` (B12) | `20_NARRATIVE_E_the_year_and_the_reason` (B38) | SPLIT | U3 decision C3-K11: `20_NARRATIVE_E` edit 1 (the declared year) lands at the head of B12; the rest of NARR_E in B38 |
| 44 | `09_WR_B_draws_not_thresholds` (B12) | `30_WR_A_the_era_is_a_named_period` (B38) | SPLIT | edit 4 (the strand-conclusion draw keyed to the era) lands in B38 with `30_WR_A`; edits 1-3 in B12 |
| 45 | `09_WR_B_weather_with_memory_and_the_year` (B12) | `30_WR_A_the_era_is_a_named_period` (B38) | SPLIT | the era reading of the weather proposal (`30_WR_A` c4) lands in B38; the year and the spell in B12 |
| 46 | `14_VERBS_MATERIAL_C_works` (B12) | `14_VERBS_SOCIAL2_A_formation_on_what_is_known` (B25) | SPLIT | C-28: the `_stamped` pair for `research` lands with `14_VERBS_SOCIAL2_A` edit 2 in B25; the works rows in B12 |
| 47 | `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted` (B12) | `03_PC_exits_withdrawal_recovery` (B16) | SUP | C-32: `tend` is owned by `14_VERBS_MATERIAL_A_mending.md` §6 (B12), not by the PC exits file; the SE pessimist's edit 4 composes on MAT_A |
| 48 | `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks` (B12) | `09_WR_B_threadwork_session_and_practitioner` (B35) | LATER | the calamity ships with `lattice_coupling` 0; the thread coupling arrives with B35 |
| 49 | `U5d_WR_owed_edits` (B12) | `16_PESSIMIST_WR_C_illness_on_the_body_ladder` (B37) | SPLIT | `U5d_WR_owed_edits.md` §2 (c) (illness on the body ladder) lands in B37 with HAP_A; §2 (a), §3, §4 in B12 |
| 50 | `U5d_WR_owed_edits` (B12) | `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` (B37) | SPLIT | as row 49 |
| 51 | `03_PC_typed_outcome_one_door` (B14) | `18_DETERMINISM_no_certain_matchup` (B15) | SUP | C-U5b-12: R-PC-03 is superseded by `18_DETERMINISM_no_certain_matchup.md`; the typed outcome does not wait for it |
| 52 | `14_VERBS_PHYSICAL_A_custody_and_force` (B15) | `03_PC_duel_round_and_approach_B` (B16) | SPLIT | PHY_A A3 (the mortal-wound draw) lands in B15 (UPR §5 row 5); A4 in B14 (UPR row 2); A1-A2 (custody, capture, arrest) in B29 after B16 and B21 |
| 53 | `14_VERBS_PHYSICAL_A_custody_and_force` (B15) | `03_PC_exits_withdrawal_recovery` (B16) | SPLIT | as row 52 |
| 54 | `14_VERBS_PHYSICAL_A_custody_and_force` (B15) | `06_FA_remit_grant_by_row` (B21) | SPLIT | as row 52 |
| 55 | `16_PESSIMIST_PC_A_the_yield_is_a_draw` (B15) | `03_PC_exits_withdrawal_recovery` (B16) | SUP | the exits file's Part B (the yield) is superseded by `16_PESSIMIST_PC_A_the_yield_is_a_draw.md` (A-24: the yield is a draw) |
| 56 | `16_PESSIMIST_PC_B_the_commit_window` (B15) | `03_PC_duel_round_and_approach_B` (B16) | REV | UPR §5 orders the calibration batch (row 5: PC_B, PC_D, the riposte, PC_A) before the round (row 6, PB steps 1-2): the family's own landing order, step 4 |
| 57 | `16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw` (B15) | `03_PC_duel_round_and_approach_B` (B16) | REV | as row 56 |
| 58 | `18_DETERMINISM_no_certain_matchup` (B15) | `03_PC_duel_round_and_approach_B` (B16) | REV | as row 56 |
| 59 | `U5b_PC_rulings_in_the_fight` (B15) | `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits` (B37) | SPLIT | UPR §6 (the opener's first-exchange edge, D-41 after A-16) lands in B37 with HAP_C |
| 60 | `04_MB_headcount_grade_and_scale` (B17) | `U5d_FA_land_and_seats_pass_on_a_won_march` (B23) | REV | UMR §6 row 7 (the land) depends on row 1 (the `Drawn` band); the headcount file depends on nothing (UMR row 1) |
| 61 | `04_MB_unit_loadout_and_weapon_in_hand_B` (B17) | `03_PC_loadout_and_carry` (B18) | SPLIT | loadout_B stages 1-2 (the troop file as data) land in B17; stages 3-4 in B31 after `03_PC_loadout_and_carry` (UMR §6 rows 3 and 9) |
| 62 | `U5b_MB_residue` (B17) | `07_SE_campaign_supply_and_muster` (B22) | SPLIT | the residue's realm-data item for the muster lands in B22 with the SE supply file |
| 63 | `16_PESSIMIST_MB_one_stamina_ledger` (B19) | `27_MB_E_what_an_army_carries_back` (B22) | REV | 27_MB_E reads the one stamina ledger; the ledger's steps 1-2 need nothing from 27_MB_E |
| 64 | `16_PESSIMIST_MB_one_stamina_ledger` (B19) | `26_MASS_BATTLE_movement_and_fatigue_as_data` (B31) | SPLIT | stamina step 3 lands in B31 with the movement-and-fatigue file (UMR §6 row 9) |
| 65 | `26_MASS_BATTLE_cell_scale_and_time` (B19) | `04_MB_manager_battle_one_resolver` (B20) | LATER | UMR §6 row 4 precedes row 5; the window and lull actions reach the drawn order only when the manager's §4 lands (`27_MB_A` Dependencies) |
| 66 | `26_MASS_BATTLE_rout_pursuit_and_giving_ground` (B19) | `04_MB_manager_battle_one_resolver` (B20) | LATER | as row 65 |
| 67 | `27_MB_A_command_and_the_obedience_draw` (B19) | `04_MB_manager_battle_one_resolver` (B20) | LATER | as row 65 (`27_MB_A` 27A-1 to 27A-4 need none) |
| 68 | `U5b_MB_rulings_in_the_field` (B19) | `U5d_FA_land_and_seats_pass_on_a_won_march` (B23) | SPLIT | UMR §2 (what a field returns, and the land) lands in B23; §1 in B05; §3 in B30; §4-§6 in B19 |
| 69 | `04_MB_playable_field_scenario` (B20) | `14_VERBS_MILITARY_C_the_muster` (B22) | SPLIT | the playable field scenario's §E (armies at build) lands in B22 (UMR §6 row 6, C-U5b-05); A, C, D in B20 |
| 70 | `04_MB_playable_field_scenario` (B20) | `14_VERBS_MILITARY_D_the_order_of_battle` (B22) | SPLIT | as row 69 |
| 71 | `06_FA_levy_through_the_seat_B` (B21) | `06_FA_war_lives_in_seats_B` (B23) | SPLIT | R3 cycle (4) broken: `06_FA_war_lives_in_seats_B` edits 1-3 (`may_wage`, no dependency on the taking) land in B21; edit 6 lands with the land plan in B23 |
| 72 | `16_PESSIMIST_FA_B_who_may_sit_join_and_declare` (B21) | `06_FA_war_lives_in_seats_B` (B23) | SPLIT | as row 71 |
| 73 | `16_PESSIMIST_FA_B_who_may_sit_join_and_declare` (B21) | `15_INSTITUTIONS_VENICE_C_roll_lot_ballot` (B32) | SPLIT | the FA_B edit that reads `may_seat` lands in B32 with `15_INSTITUTIONS_VENICE_C` |
| 74 | `16_PESSIMIST_FA_C_under_the_seat` (B21) | `15_INSTITUTIONS_COLONIAL_B_distance` (B33) | LATER | the command predicate (A-22) stands without the distance term; COL_B adds `distance` (one member, F-R4-08) in B33 |
| 75 | `22_HAPPENINGS_B_the_throne_is_never_stranded` (B21) | `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd` (B32) | SPLIT | HAP_B edits 1-2 (the rows, the set-of-titles `successions`) land in B21; edit 3 (the deed race's odds, A-19) lands in B32 with BYZ_E and SYN_B's deed ledger |
| 76 | `22_HAPPENINGS_B_the_throne_is_never_stranded` (B21) | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger` (B32) | SPLIT | as row 75 |
| 77 | `U5d_FA_owed_edits` (B21) | `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline` (B32) | SPLIT | the section of `U5d_FA_owed_edits.md` that cites `15_INSTITUTIONS_PAPACY_B` lands in B32 |
| 78 | `U5d_FA_owed_edits` (B21) | `21_PROCEDURAL_B_cast_and_seats` (B39) | SPLIT | the section that cites `21_PROCEDURAL_B` lands in B39 |
| 79 | `14_VERBS_MILITARY_A_movement` (B22) | `26_MASS_BATTLE_movement_and_fatigue_as_data` (B31) | LATER | the march reads today's pace and fatigue constants until `26_MASS_BATTLE_movement_and_fatigue_as_data.md` exports them (B31) |
| 80 | `14_VERBS_MILITARY_D_the_order_of_battle` (B22) | `27_MB_B_unit_prowess_on_the_row` (B31) | LATER | 27_MB_B ships with no behaviour at its control arm (UMR §6 row 10); the order of battle reads it when it lands |
| 81 | `14_VERBS_PHYSICAL_B_field_and_ruin` (B22) | `06_FA_war_lives_in_seats_B` (B23) | SPLIT | as row 71 (`may_wage` lands in B21) |
| 82 | `U5d_FA_land_and_seats_pass_on_a_won_march` (B23) | `14_VERBS_MATERIAL_D_paper` (B26) | SPLIT | U3 decision C3-L12 (C-R4-3): `14_VERBS_MATERIAL_D_paper.md` §6 (the `seize` act's Rung half) lands in B23 as the carrier of the aggressor's chosen seizure; the paper rows in B26 |
| 83 | `19_LACUNA_verdict_ladder_and_reversal` (B27) | `09_WR_B_chronicle_that_tells` (B36) | SPLIT | the verdict ladder's chronicle line (R-19-09, re-pointed to `account`) lands in B36 with the chronicle |
| 84 | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger` (B32) | `12_ARCS_case_on_the_realm` (B39) | SPLIT | SYN_B's prehistory (build-time ROOT-caused told claims, A-51) lands in B39 with `12_ARCS_case_on_the_realm`; the ledger reader in B32 |
| 85 | `17_CENSUS_REST_2_wiring` (B32) | `14_VERBS_PHYSICAL_D_thread_read` (B35) | SPLIT | REST_2 W3 lands in B35 with `14_VERBS_PHYSICAL_D`; W1 in B20, W2 in B24, W5 in B32 |
| 86 | `15_INSTITUTIONS_COLONIAL_D_accomplishment` (B33) | `12_ARCS_case_on_the_realm` (B39) | SPLIT | COL_D's founders-as-prehistory item lands in B39; its ledger reading in B33 |
| 87 | `17_CENSUS_C1B_02_wires` (B36) | `12_ARCS_case_on_the_realm` (B39) | SPLIT | the `arc.py` build-on-case item (W-2) lands in B39 |
| 88 | `20_NARRATIVE_F_story_inventory_and_gate` (B36) | `20_NARRATIVE_A_stands_for` (B38) | SPLIT | NARR_F's `stands_for` clause lands in B38 with `20_NARRATIVE_A`; the bar and its other clauses in B36 |
| 89 | `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` (B37) | `21_PROCEDURAL_B_cast_and_seats` (B39) | LATER | HAP_A reads the authored ages of the 46 (A-15) through its own `npcs.yaml` `age:` key; PROC_B's `age_bands` for the generated cast arrive in B39 |
| 90 | `30_WR_A_the_era_is_a_named_period` (B38) | `23_STORY_B_a_house_continues` (B39) | SPLIT | the era-ending row that reads STORY_B's events (a house continues) lands in B39 |
| 91 | `27_MB_C_dynamic_strength_and_the_residual_chance` (B19) | `04_MB_manager_battle_one_resolver` (B20) | LATER | *(found by U6 R-A's intra-batch check: in the file's own Depends line, `27_MB_C…:9`, absent from its §3.1 row)* 27C-1 traces the module's existing draw sites (`core/contact.py::obey`, `orchestration.py::stand_draw` and kin, `27_MB_C…:277`) into `FieldOutcome.report` (B17); the commanded battle's draws reach the report when manager §6 lands in B20, as rows 65–67 |

## 5. File census

### 5.1 File census: every file two or more proposals edit (serial edges)

Normalised from the read lanes' "files it edits" columns by file name; a name shared by two modules carries its module, and "?" marks a module inferred from the lane. Order inside a cell is landing order; a file listed in two or more batches is a **serial edge**: those batches never edit it concurrently, and each edits it once, in batch order.

| file | proposals | batches (serial order) |
|---|---|---|
| `rosters.yaml` | 130 proposals (see §3.1) | B01 → B03 → B04 → B05 → B07 → B09 → B10 → B11 → B12 → B14 → B15 → B16 → B17 → B18 → B19 → B21 → B22 → B23 → B24 → B25 → B26 → B27 → B28 → B30 → B31 → B32 → B33 → B35 → B37 → B38 → B39 → B40 |
| `fixtures.py` | 91 proposals (see §3.1) | B04 → B05 → B07 → B08 → B09 → B10 → B11 → B12 → B15 → B16 → B17 → B19 → B21 → B22 → B23 → B24 → B26 → B27 → B28 → B32 → B33 → B34 → B35 → B37 → B38 → B39 |
| `world_q.py` | 81 proposals (see §3.1) | B03 → B05 → B07 → B09 → B10 → B11 → B12 → B15 → B18 → B21 → B22 → B23 → B24 → B25 → B26 → B27 → B28 → B32 → B33 → B34 → B37 → B38 → B40 |
| `verb_table.yaml` | 66 proposals (see §3.1) | B01 → B03 → B04 → B07 → B09 → B10 → B11 → B12 → B15 → B17 → B21 → B22 → B23 → B24 → B25 → B26 → B27 → B28 → B32 → B33 → B35 → B36 → B37 → B38 → B39 → B40 |
| `person_q.py` | 53 proposals (see §3.1) | B03 → B04 → B09 → B10 → B11 → B14 → B21 → B24 → B25 → B26 → B27 → B28 → B32 → B33 → B34 → B35 → B38 → B39 → B40 |
| `effects_information.py` | 32 proposals (see §3.1) | B07 → B11 → B12 → B15 → B21 → B22 → B23 → B24 → B25 → B26 → B27 → B28 → B32 → B33 → B38 → B40 |
| `options.py` | 31 proposals (see §3.1) | B01 → B04 → B09 → B10 → B11 → B12 → B15 → B21 → B22 → B24 → B25 → B26 → B28 → B33 → B37 → B38 → B39 |
| `inputs.py` | 29 proposals (see §3.1) | B05 → B12 → B14 → B15 → B16 → B17 → B19 → B22 → B24 → B34 → B35 |
| `populated.py` | 29 proposals (see §3.1) | B04 → B10 → B11 → B12 → B20 → B21 → B22 → B25 → B32 → B33 → B34 → B37 → B38 → B39 |
| `sigma.py` | 29 proposals (see §3.1) | B04 → B05 → B06 → B07 → B12 → B21 → B22 → B23 → B24 → B25 → B26 → B28 → B32 → B33 |
| `offices.yaml` | 24 proposals (see §3.1) | B04 → B21 → B32 → B33 → B40 |
| `matter.py` | 23 proposals (see §3.1) | B03 → B09 → B12 → B22 → B27 → B28 → B32 → B33 → B37 → B39 |
| `hole_register.yaml` | 22 proposals (see §3.1) | B03 → B05 → B10 → B11 → B14 → B17 → B19 → B34 → B37 → B38 |
| `rosters.py` | 21 proposals (see §3.1) | B04 → B07 → B10 → B12 → B21 → B32 → B33 → B38 |
| `verbs.py` | 21 proposals (see §3.1) | B04 → B07 → B09 → B10 → B11 → B12 → B20 → B21 → B22 → B23 → B25 → B26 → B28 → B32 → B38 |
| `witness.py` | 20 proposals (see §3.1) | B05 → B11 → B21 → B24 → B25 → B26 → B28 → B32 → B35 → B38 |
| `arrangements.yaml` | 17 proposals (see §3.1) | B05 → B24 → B27 → B28 → B32 → B33 → B40 |
| `choose.py` | 17 proposals (see §3.1) | B04 → B08 → B09 → B10 → B16 → B28 → B38 |
| `effects_combat.py` | 15 proposals (see §3.1) | B04 → B12 → B14 → B16 → B17 → B19 → B20 → B22 → B23 → B31 |
| `gate.py` | 15 proposals (see §3.1) | B21 → B23 → B27 → B28 → B32 → B33 |
| `resolve.py` | 15 proposals (see §3.1) | B05 → B07 → B08 → B09 → B10 → B26 → B27 → B28 → B38 |
| `carriers.py` | 14 proposals (see §3.1) | B03 → B05 → B08 → B09 → B10 → B11 → B21 → B32 → B38 |
| `chronicle.py` | 16_PESSIMIST_GAME_consequence_reading; 05_SC_contest_record_on_event; 01_CORE_reason_trail_in_the_act_store; 16_PESSIMIST_PC_C_what_the_world_keeps_of_a_; 19_LACUNA_verdict_ladder_and_reversal; 28_CORE_scene_access_B_appointments; 09_WR_B_chronicle_that_tells; 09_WR_story_instruments_that_can_fail; 23_STORY_A_what_a_roll_leaves; 28_CORE_scene_access_C_the_petition_that_wai; 30_GO_F_the_plot_as_the_player_is_shown_it; 31_WR_C_what_the_stances_feed | B02 → B05 → B09 → B14 → B27 → B28 → B36 → B38 |
| `module_contracts.yaml` | 11_GO_pointer_and_stale_text_resolutions; 17_CENSUS_REST_1_deletions; 17_CENSUS_REST_3_corrections; 10_DICE_capability_axiom_map; U5a_DICE_owed_edits; 16_PESSIMIST_WR_A_the_road_is_drawn; 03_PC_duel_round_and_approach; U5b_MB_rulings_in_the_field; 05_SC_evidence_and_rebuttal_B; 05_SC_playable_hearing_B; 05_SC_sc05_kernel_disposition_B; 09_WR_B_threadwork_session_and_practitioner | B03 → B04 → B05 → B12 → B16 → B19 → B24 → B35 |
| `seam/wrappers/mass_battle.py` | 04_MB_headcount_grade_and_scale; 16_PESSIMIST_MB_one_stamina_ledger; 26_MASS_BATTLE_cell_scale_and_time; 27_MB_A_command_and_the_obedience_draw; U5b_MB_rulings_in_the_field; 04_MB_manager_battle_one_resolver; 04_MB_playable_field_scenario; 27_MB_D_the_commander_as_chooser; 27_MB_E_what_an_army_carries_back; 26_MASS_BATTLE_aggression_and_land; 04_MB_squad_grid_of_named_characters; 26_MASS_BATTLE_movement_and_fatigue_as_data | B17 → B19 → B20 → B22 → B23 → B30 → B31 |
| `effects_governance.py` | 06_FA_decree_binds; 06_FA_seat_terms_and_turnover; 14_VERBS_BINDING_A_formation; 22_HAPPENINGS_B_the_throne_is_never_stranded; U5d_FA_owed_edits; 14_VERBS_SOCIAL1_B_documents_and_obedience; 14_VERBS_BINDING_B_sittings; 15_INSTITUTIONS_BYZANTINE_A_dignities_and_th; 15_INSTITUTIONS_VENICE_C_roll_lot_ballot; 15_INSTITUTIONS_PAPACY_D_sanction_and_absolu; 23_STORY_B_a_house_continues | B21 → B28 → B32 → B33 → B39 |
| `sheet.py` | 01_CORE_capability_authoring_surface; 02_CHAR_capability_definitions; 02_CHAR_reason_trail_and_small_edits; 16_PESSIMIST_GO_a_witness_may_connect_what_h; 16_PESSIMIST_SC_B_one_reader_of_a_ledger; U5a_CHAR_self_knowledge_is_a_belief; 01_CORE_one_scene_contract; 11_GO_fidelity_and_campaign_modes; 11_GO_player_surface_contract_B; 16_PESSIMIST_GO_the_offer_names_what_is_held; 30_GO_F_the_plot_as_the_player_is_shown_it | B04 → B09 → B10 → B34 → B38 |
| `troops.yaml` | 04_MB_unit_loadout_and_weapon_in_hand_B; 04_MB_cell_hierarchy_as_data; 26_MASS_BATTLE_cell_scale_and_time; 26_MASS_BATTLE_rout_pursuit_and_giving_groun; 26_MASS_BATTLE_maneuver_orders; 27_MB_D_the_commander_as_chooser; 27_MB_E_what_an_army_carries_back; 04_MB_squad_grid_of_named_characters; 04_MB_campaign_party_economy; 26_MASS_BATTLE_movement_and_fatigue_as_data; 27_MB_B_unit_prowess_on_the_row | B17 → B19 → B20 → B22 → B30 → B31 |
| `massbattle.py` | 04_MB_headcount_grade_and_scale; 04_MB_typed_outcome_and_one_path; 04_MB_cell_hierarchy_as_data; 16_PESSIMIST_MB_rout_has_two_exits; 04_MB_manager_battle_one_resolver; 04_MB_playable_field_scenario; 26_MASS_BATTLE_maneuver_orders; 27_MB_D_the_commander_as_chooser; 26_MASS_BATTLE_movement_and_fatigue_as_data; 27_MB_B_unit_prowess_on_the_row | B17 → B19 → B20 → B31 |
| `predicates.py` | 06_FA_office_capabilities; 01_CORE_predicates_name_their_clause; 06_FA_decree_binds; 06_FA_seat_terms_and_turnover; 14_VERBS_BINDING_A_formation; 16_PESSIMIST_FA_B_who_may_sit_join_and_decla; 16_PESSIMIST_FA_C_under_the_seat; 14_VERBS_SOCIAL2_C_case_question_confession; 15_INSTITUTIONS_BYZANTINE_A_dignities_and_th; 15_INSTITUTIONS_VENICE_C_roll_lot_ballot | B04 → B09 → B21 → B25 → B32 |
| `roll.py` | 10_DICE_capability_axiom_map; U5a_capability_home_and_two_inputs; 05_SC_opposed_obstacle_parity; 16_PESSIMIST_DICE_soft_ceiling; 16_PESSIMIST_DICE_task_difficulty_and_throug; 16_PESSIMIST_SC_A_what_the_speaker_brings_is; 29_DICE_one_opposed_rule_form_and_tuning; U5a_DICE_owed_edits; U5c_SC_one_obstacle_form; 15_INSTITUTIONS_VENICE_A_obligation_and_the_ | B04 → B05 → B33 |
| `storybar.py` | 16_PESSIMIST_CORE_the_nine_gate_and_a_knocko; 09_WR_B_readings_of_closure_and_tension; 09_WR_story_instruments_that_can_fail; 16_PESSIMIST_WR_D_small_clock_repairs_and_tw; 20_NARRATIVE_F_story_inventory_and_gate; 23_STORY_D_story_census_and_gate; 28_CORE_scene_access_C_the_petition_that_wai; 30_WR_B_regimes_who_believes_whom; 30_WR_C_strands_open_grow_join_conclude; 30_WR_E_cascade_chains_and_the_census | B02 → B36 → B38 |
| `cast.py` | 17_CENSUS_C1A_01_deletion_batches; 01_CORE_capability_authoring_surface; 02_CHAR_capability_definitions; 02_CHAR_relations_have_a_ground; 17_CENSUS_C1A_02_wires_and_corrections; U5a_CHAR_self_knowledge_is_a_belief; 02_CHAR_which_ground_moves_whom; 16_PESSIMIST_WR_C_illness_on_the_body_ladder; 22_HAPPENINGS_A_a_death_is_rare_caused_and_d | B03 → B04 → B10 → B24 → B37 |
| `npc_registry.yaml` | 02_CHAR_capability_definitions; 02_CHAR_relations_have_a_ground; U5a_CHAR_owed_amendments; U5a_CHAR_self_knowledge_is_a_belief; 15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger; 15_INSTITUTIONS_BYZANTINE_D_the_empire_at_a_; 15_INSTITUTIONS_COLONIAL_B_distance; 16_PESSIMIST_WR_C_illness_on_the_body_ladder; 31_WR_A_house_cores_and_the_cast_on_the_opin | B04 → B10 → B32 → B33 → B37 → B38 |
| `requirements.yaml` | 01_CORE_requirements_reading_record; 01_CORE_tests_delete_what_cannot_fail; 16_PESSIMIST_CORE_the_nine_gate_and_a_knocko; 16_PESSIMIST_GAME_consequence_reading; 09_WR_B_pointer_text_for_the_orchestrator; 01_CORE_claim_fade_as_read; 08_FI_01_claim-sourced-referents; U5b_MB_residue; 16_PESSIMIST_FI_D_withhold_what_has_no_produ | B02 → B03 → B09 → B11 → B17 → B26 |
| `requires.py` | 02_CHAR_offer_what_can_be_done; 14_VERBS_BINDING_D_orders; 16_PESSIMIST_FA_C_under_the_seat; 14_VERBS_MILITARY_A_movement; 14_VERBS_MILITARY_C_the_muster; 14_VERBS_MILITARY_D_the_order_of_battle; 15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the; 09_WR_B_threadwork_session_and_practitioner; 14_VERBS_PHYSICAL_D_thread_read | B10 → B21 → B22 → B33 → B35 |
| `write_matrix.yaml` | 17_CENSUS_REST_3_corrections; 01_CORE_claim_fade_as_read; 16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_dra; 07_SE_population_regrowth_B; 16_PESSIMIST_WR_A_the_road_is_drawn; 16_PESSIMIST_WR_B_the_calamity_strains_and_b; 12_ARCS_substrate_as_ground; 31_WR_B_the_revival_gathers; 23_STORY_C_a_founded_place_can_fail | B03 → B09 → B10 → B12 → B35 → B38 → B39 |
| `armyrecord.py` | 04_MB_cell_hierarchy_as_data; 27_MB_A_command_and_the_obedience_draw; 04_MB_manager_battle_one_resolver; 27_MB_D_the_commander_as_chooser; 14_VERBS_MILITARY_C_the_muster; 14_VERBS_MILITARY_D_the_order_of_battle; 27_MB_E_what_an_army_carries_back; 04_MB_campaign_party_economy | B19 → B20 → B22 → B31 |
| `battle_loop.py` | U5b_PC_rulings_in_the_fight; 04_MB_typed_outcome_and_one_path; 16_PESSIMIST_MB_rout_has_two_exits; 26_MASS_BATTLE_rout_pursuit_and_giving_groun; 27_MB_C_dynamic_strength_and_the_residual_ch; U5b_MB_rulings_in_the_field; 04_MB_manager_battle_one_resolver; 04_MB_playable_field_scenario | B15 → B17 → B19 → B20 |
| `descriptor_registry.yaml` | 01_CORE_capability_authoring_surface; 02_CHAR_capability_definitions; 06_FA_office_capabilities; 10_DICE_capability_axiom_map; 27_MB_A_command_and_the_obedience_draw; 30_WR_G_regime_opinions_and_the_pull_of_ones; 31_WR_A_house_cores_and_the_cast_on_the_opin; 31_WR_C_what_the_stances_feed | B04 → B19 → B38 |
| `epistemic.py` | 01_CORE_reason_trail_in_the_act_store; 16_PESSIMIST_GO_a_witness_may_connect_what_h; 18_DETERMINISM_notice_is_a_draw; 08_FI_08_knots-season-form; 16_PESSIMIST_SC_C_a_verdict_names_its_party; 28_CORE_scene_access_A_occupancy_and_precede; 15_INSTITUTIONS_COLONIAL_B_distance; 20_NARRATIVE_C_who_holds_what | B09 → B11 → B25 → B27 → B28 → B33 → B38 |
| `instruments.yaml` | 15_INSTITUTIONS_COLONIAL_A_instruments; 15_INSTITUTIONS_SYNTHESIS_A_one_kit; 15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger; 15_INSTITUTIONS_PAPACY_C_consecration_and_de; 15_INSTITUTIONS_SYNTHESIS_C_crossings; 23_STORY_B_a_house_continues; 15_INSTITUTIONS_COLONIAL_grounding_F_what_th; 15_INSTITUTIONS_VENICE_grounding_E_what_the_ | B32 → B33 → B39 → B40 |
| `orderofbattle.py` | 04_MB_unit_loadout_and_weapon_in_hand_B; 04_MB_cell_hierarchy_as_data; 26_MASS_BATTLE_cell_scale_and_time; 04_MB_manager_battle_one_resolver; 14_VERBS_MILITARY_D_the_order_of_battle; 04_MB_campaign_party_economy; 27_MB_B_unit_prowess_on_the_row; 17_CENSUS_REST_2_wiring | B17 → B19 → B20 → B22 → B31 → B32 |
| `arrangements.py` | 12_ARCS_cited_evidence; 05_SC_arrangement_rows_that_bind; U5c_SC_proceedings_residue; 14_VERBS_SOCIAL1_D_grievance_and_settlement; 15_INSTITUTIONS_PAPACY_B_patronage_election_; 17_CENSUS_REST_2_wiring; 15_INSTITUTIONS_PAPACY_grounding_mechanisms | B24 → B27 → B28 → B32 → B40 |
| `play_surface.py` | 08_FI_03_playable-inquiry; 08_FI_07_shortest-playable-case; 01_CORE_one_scene_contract; 11_GO_player_surface_contract_B; 30_GO_F_the_plot_as_the_player_is_shown_it; 21_PROCEDURAL_C_prologue_and_case_seeds; 16_PESSIMIST_GO_surface_pins | B11 → B34 → B38 → B39 → B41 |
| `pool.py` | 01_CORE_capability_authoring_surface; 10_DICE_capability_axiom_map; U5a_capability_home_and_two_inputs; 10_DICE_one_score_two_roles; 13_SC_tuning_tables; 29_DICE_one_opposed_rule_form_and_tuning; 07_SE_capability_rate_B | B04 → B05 → B12 |
| `corpus_run.py` | 01_CORE_claim_fade_as_read; 07_SE_arc_needs; 09_WR_provided_arcs; 23_STORY_A_what_a_roll_leaves; 01_CORE_case_setup_and_beats; 12_ARCS_case_on_the_realm | B09 → B12 → B38 → B39 |
| `governance_spine.py` | 06_FA_playable_scenario; 06_FA_shortest_loop_B; 05_SC_playable_hearing_B; 15_INSTITUTIONS_BYZANTINE_F_playable_scenari; 15_INSTITUTIONS_PAPACY_F_playable_vacant_cha; 15_INSTITUTIONS_SYNTHESIS_D_first_playable | B21 → B24 → B40 |
| `modules/combat/wrapper.py?` | 03_PC_weapon_form_at_round_start; 16_PESSIMIST_PC_A_the_yield_is_a_draw; 16_PESSIMIST_PC_B_the_commit_window; 16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_; 03_PC_duel_round_and_approach; 03_PC_exits_withdrawal_recovery | B14 → B15 → B16 |
| `world.py` | 17_CENSUS_C1A_01_deletion_batches; 17_CENSUS_REST_1_deletions; U5d_GO_owed_edits; 16_PESSIMIST_CORE_the_record_holds_what_chan; 16_PESSIMIST_SE_B_harvest_walls_and_the_supp; 16_PESSIMIST_GO_surface_pins | B03 → B06 → B09 → B12 → B41 |
| `dice_engine.py` | 17_CENSUS_REST_1_deletions; 10_DICE_exported_face_rule_and_band_edges; 10_DICE_one_roller_one_fraction_rule; U5a_DICE_owed_edits; 11_GO_one_draw_owner | B03 → B05 → B06 |
| `driver.py` | 16_PESSIMIST_CORE_no_stored_plan; 01_CORE_reason_trail_in_the_act_store; 09_WR_B_weather_with_memory_and_the_year; 28_CORE_scene_access_A_occupancy_and_precede; 09_WR_B_threadwork_session_and_practitioner | B03 → B09 → B12 → B28 → B35 |
| `effects_army.py` | 04_MB_manager_battle_one_resolver; 06_FA_levy_through_the_seat_B; 14_VERBS_MILITARY_C_the_muster; 14_VERBS_MILITARY_D_the_order_of_battle; 27_MB_E_what_an_army_carries_back | B20 → B21 → B22 |
| `effects_economy.py` | 07_SE_capability_rate_B; 14_VERBS_MATERIAL_A_mending; 16_PESSIMIST_WR_B_the_calamity_strains_and_b; 15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the; 15_INSTITUTIONS_VENICE_B_debt_instrument | B12 → B33 |
| `goals.yaml` | 12_ARCS_arcs_as_staged_goals; 15_INSTITUTIONS_COLONIAL_B_distance; 15_INSTITUTIONS_PAPACY_C_consecration_and_de; 15_INSTITUTIONS_PAPACY_E_sees_tithe_orders_l; 15_INSTITUTIONS_BYZANTINE_grounding_mechanis | B10 → B33 → B40 |
| `modules/mass_battle/config.py?` | 04_MB_typed_outcome_and_one_path; U5b_MB_residue; 04_MB_cr12_linear_law; 27_MB_C_dynamic_strength_and_the_residual_ch; 26_MASS_BATTLE_movement_and_fatigue_as_data | B17 → B19 → B31 |
| `modules/mass_battle/orchestration.py?` | 04_MB_unit_loadout_and_weapon_in_hand_B; 26_MASS_BATTLE_rout_pursuit_and_giving_groun; 27_MB_A_command_and_the_obedience_draw; 27_MB_C_dynamic_strength_and_the_residual_ch; 26_MASS_BATTLE_maneuver_orders | B17 → B19 → B20 |
| `seam/wrappers/combat.py` | 01_CORE_capability_authoring_surface; 11_GO_one_draw_owner; 03_PC_typed_outcome_one_door; 16_PESSIMIST_PC_C_what_the_world_keeps_of_a_; 14_VERBS_PHYSICAL_A_custody_and_force | B04 → B06 → B14 → B15 |
| `sigma_leverage.py` | 10_DICE_capability_axiom_map; 10_DICE_exported_face_rule_and_band_edges; 16_PESSIMIST_DICE_soft_ceiling; 29_DICE_one_opposed_rule_form_and_tuning; U5a_DICE_owed_edits | B04 → B05 |
| `strife.py` | U5d_WR_owed_edits; 15_INSTITUTIONS_PAPACY_A_ground; 09_WR_story_instruments_that_can_fail; 30_WR_A_the_era_is_a_named_period; 30_WR_C_strands_open_grow_join_conclude | B12 → B32 → B36 → B38 |
| `subsist.py` | 07_SE_ground_and_granaries; 07_SE_population_census; 16_PESSIMIST_GAME_the_world_draws; 16_PESSIMIST_SE_A_the_granary_shares_and_the; U5d_STORY_owed_edits | B12 → B39 |
| `arc.py` | 09_WR_B_readings_of_closure_and_tension; 17_CENSUS_C1B_02_wires; 01_CORE_case_setup_and_beats; 12_ARCS_case_on_the_realm | B36 → B39 |
| `battle_orders.json` | 27_MB_A_command_and_the_obedience_draw; 04_MB_manager_battle_one_resolver; 26_MASS_BATTLE_maneuver_orders; 04_MB_squad_grid_of_named_characters | B19 → B20 → B30 |
| `census.py` | 07_SE_population_census; 21_PROCEDURAL_B_cast_and_seats; 21_PROCEDURAL_D_world_cards_and_churn; 23_STORY_B_a_house_continues | B12 → B39 |
| `combat_systems.py` | 03_PC_weapon_form_at_round_start; 16_PESSIMIST_PC_B_the_commit_window; U5b_PC_rulings_in_the_fight; 03_PC_loadout_and_carry | B14 → B15 → B18 |
| `decision_spread.py` | 01_CORE_tests_shipped_world_falsifiers; 02_CHAR_goal_lean_on_its_own_question; 02_CHAR_resolve_and_temper; U5a_CHAR_owed_amendments | B02 → B10 |
| `effects_shared.py` | 14_VERBS_MATERIAL_A_mending; 14_VERBS_BINDING_C_turnover; 28_CORE_scene_access_B_appointments; 23_STORY_A_what_a_roll_leaves | B12 → B21 → B28 → B38 |
| `modules/combat/config.py?` | 03_PC_typed_outcome_one_door; 03_PC_weapon_records_in_the_export; 18_DETERMINISM_no_certain_matchup; 03_PC_loadout_and_carry | B14 → B15 → B18 |
| `modules/combat/core.py?` | 10_DICE_capability_axiom_map; U5a_capability_home_and_two_inputs; 29_DICE_one_opposed_rule_form_and_tuning; U5b_PC_rulings_in_the_fight | B04 → B05 → B15 |
| `test_storybar.py` | 16_PESSIMIST_WR_D_small_clock_repairs_and_tw; 20_NARRATIVE_F_story_inventory_and_gate; 23_STORY_D_story_census_and_gate; 23_STORY_A_what_a_roll_leaves | B36 → B38 |
| `worldgen.py` | 21_PROCEDURAL_A_worldgen_tables_and_ground; 21_PROCEDURAL_B_cast_and_seats; 21_PROCEDURAL_C_prologue_and_case_seeds; 21_PROCEDURAL_E_names_and_texts | B39 |
| `combat_kit.py` | 03_PC_weapon_records_in_the_export; 03_PC_loadout_and_carry; 03_PC_person_inputs_content | B14 → B18 |
| `conviction.py` | 17_CENSUS_C1B_01_deletions; 17_CENSUS_C1B_03_corrections; 17_CENSUS_REST_1_deletions | B03 |
| `core/exchange.py` | 04_MB_cr12_linear_law; 27_MB_C_dynamic_strength_and_the_residual_ch; 27_MB_B_unit_prowess_on_the_row | B19 → B31 |
| `deliberate.py` | 16_PESSIMIST_CORE_no_stored_plan; 01_CORE_reason_trail_in_the_act_store; 28_CORE_scene_access_A_occupancy_and_precede | B03 → B09 → B28 |
| `effects_founding.py` | 14_VERBS_MATERIAL_C_works; 14_VERBS_PHYSICAL_B_field_and_ruin; 23_STORY_C_a_founded_place_can_fail | B12 → B22 → B39 |
| `evidence.py` | 05_SC_evidence_and_rebuttal_B; 19_LACUNA_admission_rides_the_citing_draw; 19_LACUNA_verdict_ladder_and_reversal | B24 → B27 |
| `export_troops.py` | 04_MB_unit_loadout_and_weapon_in_hand_B; 04_MB_cell_hierarchy_as_data; 26_MASS_BATTLE_movement_and_fatigue_as_data | B17 → B19 → B31 |
| `files.py` | 17_CENSUS_C1A_01_deletion_batches; 07_SE_valley_scenario; 15_INSTITUTIONS_COLONIAL_A_instruments | B03 → B12 → B32 |
| `hierarchy/units.py` | 04_MB_unit_loadout_and_weapon_in_hand_B; 16_PESSIMIST_MB_rout_has_two_exits; 26_MASS_BATTLE_maneuver_orders | B17 → B19 → B20 |
| `instruments.py` | 15_INSTITUTIONS_COLONIAL_A_instruments; 15_INSTITUTIONS_SYNTHESIS_A_one_kit; 15_INSTITUTIONS_COLONIAL_grounding_F_what_th | B32 → B40 |
| `lanchester_signature.py` | 04_MB_cr12_linear_law; 16_PESSIMIST_MB_partition_and_the_pair_rule; 27_MB_C_dynamic_strength_and_the_residual_ch | B19 |
| `military_menu.py` | 04_MB_manager_battle_one_resolver; 27_MB_D_the_commander_as_chooser; 06_FA_levy_through_the_seat_B | B20 → B21 |
| `modules/mass_battle/hierarchy/units.py` | 17_CENSUS_C1B_01_deletions; 17_CENSUS_REST_1_deletions; 17_CENSUS_REST_2_wiring | B03 → B32 |
| `modules/mass_battle/units.py?` | 27_MB_A_command_and_the_obedience_draw; 26_MASS_BATTLE_movement_and_fatigue_as_data; 27_MB_B_unit_prowess_on_the_row | B19 → B31 |
| `npcs.yaml` | 15_INSTITUTIONS_PAPACY_A_ground; 22_HAPPENINGS_A_a_death_is_rare_caused_and_d; 22_HAPPENINGS_D_batches_and_added_gates | B32 → B37 |
| `test_season_shape.py` | 01_CORE_tests_delete_what_cannot_fail; 08_FI_01_claim-sourced-referents; 09_WR_provided_arcs | B02 → B11 → B12 |
| `worldgen.yaml` | 21_PROCEDURAL_A_worldgen_tables_and_ground; 21_PROCEDURAL_B_cast_and_seats; 21_PROCEDURAL_C_prologue_and_case_seeds | B39 |
| `*.yaml` | 01_CORE_case_setup_and_beats; 12_ARCS_case_on_the_realm | B39 |
| `CURRENT.md` | 09_WR_B_pointer_text_for_the_orchestrator; 11_GO_pointer_and_stale_text_resolutions | B03 |
| `README.md` | 11_GO_design_reference_disposition; 11_GO_pointer_and_stale_text_resolutions | B03 |
| `aperture.py` | 17_CENSUS_C1B_02_wires; 22_HAPPENINGS_A_a_death_is_rare_caused_and_d | B36 → B37 |
| `budget.py` | 02_CHAR_reason_trail_and_small_edits; 09_WR_B_weather_with_memory_and_the_year | B09 → B12 |
| `combat_engine_v1.json` | 03_PC_weapon_records_in_the_export; 16_PESSIMIST_PC_A_the_yield_is_a_draw | B14 → B15 |
| `core/contact.py` | 26_MASS_BATTLE_maneuver_orders; 17_CENSUS_REST_2_wiring | B20 → B32 |
| `descriptors.py` | 01_CORE_capability_authoring_surface; 02_CHAR_capability_uses_table | B04 |
| `draw.py` | 11_GO_one_draw_owner; 16_PESSIMIST_GO_keyed_draw_no_recorder | B06 |
| `effects_migration.py` | 16_PESSIMIST_WR_A_the_road_is_drawn; 14_VERBS_MILITARY_A_movement | B12 → B22 |
| `export_oracle_pins.py` | 11_GO_port_gate_order_and_coverage; 16_PESSIMIST_GO_surface_pins | B41 |
| `goals.py` | 12_ARCS_arcs_as_staged_goals; 31_WR_C_what_the_stances_feed | B10 → B38 |
| `governance_spine.yaml` | 06_FA_playable_scenario; 15_INSTITUTIONS_VENICE_D_houses_charters_and | B21 → B33 |
| `hearing.py` | 05_SC_negotiation_scene; 05_SC_playable_hearing_B | B24 |
| `ids.py` | 11_GO_one_draw_owner; 16_PESSIMIST_GO_keyed_draw_no_recorder | B06 |
| `institution.py` | 15_INSTITUTIONS_COLONIAL_E_scenario; 15_INSTITUTIONS_SYNTHESIS_D_first_playable | B40 |
| `knots.py` | 17_CENSUS_C1B_01_deletions; 08_FI_08_knots-season-form | B03 → B25 |
| `ladder.py` | 04_MB_headcount_grade_and_scale; 26_MASS_BATTLE_aggression_and_land | B17 → B23 |
| `larder.py` | 07_SE_ground_and_granaries; 16_PESSIMIST_SE_A_the_granary_shares_and_the | B12 |
| `mechanics_index.yaml` | 17_CENSUS_C1B_01_deletions; 17_CENSUS_C1B_03_corrections | B03 |
| `modules/combat/config.py` | 16_PESSIMIST_PC_A_the_yield_is_a_draw; 16_PESSIMIST_PC_B_the_commit_window | B15 |
| `modules/combat/fight.py` | 16_PESSIMIST_PC_C_what_the_world_keeps_of_a_; 03_PC_duel_round_and_approach | B14 → B16 |
| `modules/combat/fight.py?` | 03_PC_typed_outcome_one_door; 16_PESSIMIST_PC_A_the_yield_is_a_draw | B14 → B15 |
| `modules/mass_battle/contact.py?` | 27_MB_A_command_and_the_obedience_draw; 27_MB_D_the_commander_as_chooser | B19 → B20 |
| `modules/mass_battle/table.py?` | 26_MASS_BATTLE_movement_and_fatigue_as_data; 27_MB_B_unit_prowess_on_the_row | B31 |
| `names_index.yaml` | 06_FA_hygiene; 16_PESSIMIST_GO_surface_pins | B03 → B41 |
| `percell.py` | 04_MB_unit_loadout_and_weapon_in_hand_B; 26_MASS_BATTLE_movement_and_fatigue_as_data | B17 → B31 |
| `register.py` | 01_CORE_requirements_reading_record; 16_PESSIMIST_CORE_the_nine_gate_and_a_knocko | B02 |
| `restructure_ledger.md` | 01_CORE_tests_delete_what_cannot_fail; 17_CENSUS_C1B_01_deletions | B02 → B03 |
| `scenarios.py` | 08_FI_03_playable-inquiry; 08_FI_07_shortest-playable-case | B11 |
| `sim_params.json` | 27_MB_C_dynamic_strength_and_the_residual_ch; 05_SC_sc05_kernel_disposition_B | B19 → B24 |
| `squad.py` | U5b_MB_rulings_in_the_field; 04_MB_squad_grid_of_named_characters | B19 → B30 |
| `strife_moves.yaml` | 15_INSTITUTIONS_PAPACY_A_ground; 15_INSTITUTIONS_PAPACY_D_sanction_and_absolu | B32 → B33 |
| `test_go07_canonical_digest.py` | 11_GO_pointer_and_stale_text_resolutions; U5d_GO_owed_edits | B03 → B06 |
| `valley.py` | 07_SE_valley_scenario; 23_STORY_E_first_playable_the_lean_year | B12 → B39 |
| `valley.yaml` | 07_SE_valley_scenario; 23_STORY_E_first_playable_the_lean_year | B12 → B39 |
| `voices.py` | 02_CHAR_voices_and_the_room; U5a_CHAR_self_knowledge_is_a_belief | B10 |
| `world_cards.yaml` | 21_PROCEDURAL_C_prologue_and_case_seeds; 21_PROCEDURAL_D_world_cards_and_churn | B39 |

## 6. Tests and probes a gate names that are not in the tree

### 6.1 Test files a gate names that do not exist in the tree

| test file | named by (batch) | status | the batch that lands it must first |
|---|---|---|---|
| `test_accomplishment.py` | `15_INSTITUTIONS_COLONIAL_D_accomplishment` (B33) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_audit_and_charter.py` | `15_INSTITUTIONS_COLONIAL_C_audit_and_charter` (B33) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_combat_opposed_rule_shape.py` | `29_DICE_one_opposed_rule_form_and_tuning` (B05) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_cr08_census_weight.py` | `07_SE_population_census` (B12) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_custom.py` | `30_WR_G_regime_opinions_and_the_pull_of_ones_own` (B38) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_effort.py` | `10_DICE_advantage_sources_for_the_arcs` (B05) | MISSING | rename the citation to `engine/season/tests/test_cp_t01_05_npc_effort.py` (exists; `R1_READ.md:367`) |
| `test_endowment.py` | `07_SE_ground_and_granaries` (B12) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_fa01_head_seats.py` | `06_FA_remit_grant_by_row` (B21) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_instruments.py` | `15_INSTITUTIONS_COLONIAL_A_instruments` (B32); `15_INSTITUTIONS_SYNTHESIS_E_implementation_plan` (B40) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_narrative_dues.py` | `30_WR_D_momentum_and_its_brakes` (B38) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_obligees.py` | `17_CENSUS_C1A_02_wires_and_corrections` (B10) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_opposed_ob.py` | `29_DICE_one_opposed_rule_form_and_tuning` (B05) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_realm_requirements.py` | `01_CORE_tests_shipped_world_falsifiers` (B02) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_referent_class_stamps.py` | `16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings` (B36) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_remove.py` | `15_INSTITUTIONS_COLONIAL_B_distance` (B33) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_sc_calibration_targets.py` | `13_SC_calibration` (B05); `29_DICE_one_opposed_rule_form_and_tuning` (B05) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_scene_access_appointments.py` | `28_CORE_scene_access_B_appointments` (B28) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_scene_access_occupancy.py` | `28_CORE_scene_access_A_occupancy_and_precedence` (B28) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_scene_access_precedence.py` | `28_CORE_scene_access_A_occupancy_and_precedence` (B28) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_scene_access_waiting.py` | `28_CORE_scene_access_C_the_petition_that_waits` (B38) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_standing_ration.py` | `07_SE_campaign_supply_and_muster` (B22) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_sway.py` | `31_WR_B_the_revival_gathers` (B38) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_travel.py` | `16_PESSIMIST_WR_A_the_road_is_drawn` (B12) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |
| `test_worldgen_switch.py` | `21_PROCEDURAL_A_worldgen_tables_and_ground` (B39) | MISSING | write it as the batch's first commit (red against the control where the claim is a defect; green at control and red with the edit reverted where the claim is a new behaviour) |

### 6.2 Scratch probes a gate names that are not in the repository

Each is a script a producing lane ran and did not commit. A gate may not rest on it (CLAUDE.md §0.1 pt 3: check the run happened): before the batch lands, the probe's reading is restated as a named test or a committed harness reading (an existing instrument: `aperture`, `storybar`, `chronicle`, `corpus_run`, `register`), and the batch writes that first. New modules a proposal creates (`fmath.py`, `draw.py`, `squad.py`, `table.py`, `port_oracle.py`, `export_oracle_draws.py` (struck by C3-L3), `export_oracle_pins.py`) are not probes and are excluded.

| proposal (batch) | scripts named and absent |
|---|---|
| `01_CORE_tests_one_golden_owner` (B02) | `probe_realm_gates.py`, `probe_realm_sweep.py` |
| `01_CORE_tests_shipped_world_falsifiers` (B02) | `probe_r01_control.py`, `probe_realm_gates.py`, `probe_realm_sweep.py`, `probe_vacuity.py` |
| `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` (B02) | `knock2.py`, `req_forge.py` |
| `16_PESSIMIST_GAME_consequence_reading` (B02) | `x2_death.py` |
| `11_GO_pointer_and_stale_text_resolutions` (B03) | `seam.py` |
| `16_PESSIMIST_CORE_no_stored_plan` (B03) | `knock.py`, `qreuse_small.py` |
| `13_SC_calibration` (B05) | `realm_tap.py` |
| `13_SC_tuning_tables` (B05) | `calibrate.py`, `planted_grid.py` |
| `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage` (B05) | `n1_favour_two_ladders.py`, `p1_petitioner.py` |
| `29_DICE_one_opposed_rule_form_and_tuning` (B05) | `p1_grid.py`, `p7_scale.py` |
| `13_SC_draw_for_unrolled_contests` (B07) | `realm_tap.py` |
| `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` (B08) | `ordp.py` |
| `01_CORE_claim_fade_as_read` (B09) | `probe_growth.py` |
| `01_CORE_predicates_name_their_clause` (B09) | `probe_predicates.py` |
| `01_CORE_reason_trail_in_the_act_store` (B09) | `probe_reason.py` |
| `16_PESSIMIST_CORE_a_refusal_is_remembered` (B09) | `an1.py`, `refclaim.py` |
| `16_PESSIMIST_CORE_the_record_holds_what_changed` (B09) | `ordp.py`, `p34.py` |
| `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` (B09) | `x2_death.py` |
| `16_PESSIMIST_SC_B_one_reader_of_a_ledger` (B09) | `p2b_lie_extremes.py`, `p2c_two_readers.py`, `p2d_stale_sighting.py` |
| `02_CHAR_goal_lean_on_its_own_question` (B10) | `probe3.py` |
| `02_CHAR_offer_what_can_be_done` (B10) | `probe2.py` |
| `02_CHAR_relations_have_a_ground` (B10) | `probe_foils.py` |
| `02_CHAR_resolve_and_temper` (B10) | `probe1.py` |
| `02_CHAR_scar_cap_and_regard_unit` (B10) | `probe2.py`, `probe3.py` |
| `02_CHAR_scar_is_a_wound` (B10) | `probe_scar_stock.py` |
| `02_CHAR_voices_and_the_room` (B10) | `probe_voices.py` |
| `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told` (B10) | `a0_words.py`, `b1_season.py`, `c1_two_men.py`, `d1_cuts.py`, `d1_read.py`, `x1_extremes.py` |
| `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says` (B10) | `a0_words.py`, `a1_norms.py`, `a2_sig.py`, `c1_two_men.py`, `d1_cuts.py` |
| `16_PESSIMIST_CHAR_C_the_stop_is_the_mans` (B10) | `c2_stopped.py` |
| `U5a_CHAR_owed_amendments` (B10) | `b2_done_to_him.py`, `c1_two_men.py`, `x1_extremes.py` |
| `08_FI_01_claim-sourced-referents` (B11) | `dynamics.py`, `r08_probe.py` |
| `08_FI_02_rumour-that-travels` (B11) | `dynamics.py` |
| `08_FI_06_testimony-names-a-hand` (B11) | `hearsay_doer_probe.py` |
| `16_PESSIMIST_FI_A_what_a_rumour_can_garble` (B11) | `p1c_exists.py`, `p2_proxy.py` |
| `16_PESSIMIST_FI_C_what_a_deed_leaves_behind` (B11) | `p1_belief.py`, `p1c_exists.py`, `p1d_where.py`, `p4_detective.py`, `p5_crime.py` |
| `16_PESSIMIST_SC_E_an_honest_teller_is_not_marked` (B11) | `p2_lie.py`, `p2b_lie_extremes.py`, `realm_sc.py` |
| `U5c_FI_residue` (B11) | `fi_arms.py`, `p1_belief.py`, `p1d_where.py` |
| `07_SE_ground_and_granaries` (B12) | `se_ground.py`, `se_probe.py` |
| `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted` (B12) | `kernel.py`, `pes_play.py` |
| `16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate` (B12) | `kernel.py`, `pes_supply.py` |
| `03_PC_weapon_form_at_round_start` (B14) | `probe_round_state.py` |
| `16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight` (B14) | `pS2.py`, `pS_season.py` |
| `U5b_PC_residue` (B14) | `fight_trace.py`, `pD_skill.py`, `pS_season.py`, `scan_tests.py` |
| `16_PESSIMIST_PC_A_the_yield_is_a_draw` (B15) | `pB_yield.py`, `pM_yield_draw.py` |
| `16_PESSIMIST_PC_B_the_commit_window` (B15) | `pF_story.py`, `pP_window.py` |
| `16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw` (B15) | `pC_armour.py`, `pQ2_gap.py`, `pQ_knee.py` |
| `U5b_PC_rulings_in_the_fight` (B15) | `pF_story.py`, `pK_scale2.py`, `pL_misc.py` |
| `03_PC_duel_round_and_approach_B` (B16) | `pI_approach2.py` |
| `U5b_MB_residue` (B17) | `p10_edges.py`, `p11_extremes.py` |
| `16_PESSIMIST_MB_one_stamina_ledger` (B19) | `p5_tired.py` |
| `16_PESSIMIST_MB_partition_and_the_pair_rule` (B19) | `p10_edges.py`, `p12_proxy3.py`, `p13_same_cells.py`, `p15_shape.py`, `p15b_shape_proxy.py`, `p1_size.py`, `p2_flank.py`, `p9_proxy.py` |
| `16_PESSIMIST_MB_rout_has_two_exits` (B19) | `p6_rout.py` |
| `06_FA_levy_through_the_seat_B` (B21) | `levy_probe.py` |
| `06_FA_seat_terms_by_body_B` (B21) | `build_probe.py` |
| `16_PESSIMIST_FA_A_dismissal_survives_the_king` (B21) | `pf1_static.py`, `pf2_premise.py`, `pf2b_followup.py`, `pf6_fixcheck.py` |
| `16_PESSIMIST_FA_B_who_may_sit_join_and_declare` (B21) | `pf2_premise.py`, `pf2b_followup.py` |
| `16_PESSIMIST_FA_C_under_the_seat` (B21) | `pf2_premise.py`, `pf2b_followup.py` |
| `U5d_FA_owed_edits` (B21) | `pf1_static.py`, `pf5_heads.py` |
| `16_PESSIMIST_FI_B_a_paper_is_about_something` (B26) | `p3_forgery.py`, `p3b_knows.py` |
| `16_PESSIMIST_FI_D_withhold_what_has_no_product` (B26) | `p5_crime.py` |
| `16_PESSIMIST_SC_C_a_verdict_names_its_party` (B27) | `p3_hearing_ends.py`, `p4_verdict.py`, `realm_sc.py` |
| `16_PESSIMIST_SC_D_an_argument_moves_someone` (B27) | `d_projection.py`, `p5_argue.py`, `realm_sc.py` |
| `U5c_SC_proceedings_residue` (B27) | `p5_argue.py` |
| `28_CORE_scene_access_A_occupancy_and_precedence` (B28) | `face.py`, `occ.py`, `ordp.py` |
| `15_INSTITUTIONS_PAPACY_A_ground` (B32) | `probe_reach.py` |
| `15_INSTITUTIONS_VENICE_D_houses_charters_and_content` (B33) | `counting_house.py` |
| `09_WR_B_threadwork_session_and_practitioner` (B35) | `working.py` |
| `20_NARRATIVE_F_story_inventory_and_gate` (B36) | `narr_probe.py` |
| `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` (B37) | `bout_calc2.py` |
| `20_NARRATIVE_A_stands_for` (B38) | `narr_probe.py` |
| `15_INSTITUTIONS_SYNTHESIS_D_first_playable` (B40) | `counting_house.py` |

### 6.3 Symbols and files a proposal depends on that exist in neither the tree nor (as its own edit) the dependent proposal

Consolidated from the read lanes' MISSING lists (`R1_READ.md:367`, `:424`; `R2_READ.md:305`, `:379`;
`R3_READ.md` §5 M marks; `R4_READ.md:740`; `R5_READ.md` §5). "Created by" names the proposal whose own edit
builds it and the batch; the dependent batch is ordered after it in §2. **No carrier** means nothing in the suite
builds it: v12 must place it (from a v11 position that STAGES.md step 5 carries) or the dependent part waits.

| missing symbol or file | needed by | created by (batch) |
|---|---|---|
| `references/troops.yaml`, `tools/export_troops.py`, `modules/mass_battle/troop_types/table.py` | the MB family | `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 1–2 (B17) |
| `engine/season/harness/field_scene.py` | `04_MB_playable_field_scenario.md` | itself (B20) |
| `tools/export_oracle_pins.py`, `harness/port_oracle.py` | the port gate; and the export round-trip of B06's `fmath` and draw vectors, which B06's gates named and which therefore moves to B41 (U6 R-A, §1.3) | `16_PESSIMIST_GO_surface_pins.md` (B41) |
| `engine/dice_engine/draw.py` (`Draw`), the A-30 key function | every keyed draw | `16_PESSIMIST_GO_keyed_draw_no_recorder.md` with `11_GO_one_draw_owner.md` (B06) |
| `engine/dice_engine/fmath.py` | float parity | `11_GO_float_contract.md` Part A (B06) |
| `tools/export_oracle_draws.py` | `11_GO_float_contract.md` Part B | struck (C3-L3) |
| `PersonInterior` as a typed class | every `decision/` signature in GO and PC | `U5a_CORE_owed_edits.md` §E (a frozen `PersonInterior`, B03) |
| `explain` / `Derivation` | the player surface | `11_GO_player_surface_contract.md` §2, the one live section of a superseded file (B34) |
| `DuelRoundInput`; `HearingInput`, `Speaker` | `29_DICE` item 29-5 | `03_PC_duel_round_and_approach_B.md` (B16); `05_SC_playable_hearing_B.md` (B24); 29-5 lands in B30 |
| the `entry:` kind for `combat.round`; the nested entry | the nested duel | `U5b_PC_rulings_in_the_fight.md` §1 (B30) |
| the seat row's `modifier:` | `27_MB_A` gate 7, the `office` source | U1 D-U1-01 (its column lands with OBS §3, B05; behind its revert until A-12's text is applied) |
| `person_q.present_persons`, `person_q.holders_named` | VRES §2, SOCIAL1/2, MATERIAL | `08_FI_02_rumour-that-travels.md` edit 5, `08_FI_01_claim-sourced-referents.md` edit 1 (B11) |
| `world_q.hearing` | the evidence interface | `08_FI_05_evidence-interface_B.md` (B24) |
| `world_q.office_rank` | precedence | `28_CORE_scene_access_A_occupancy_and_precedence.md` (B28) |
| `ActStore.add_scene` / `scene_of` | the reason trail | `01_CORE_reason_trail_in_the_act_store.md` (B09) |
| `decision/voices.py`; `modules/social_contest/hearing.py`, `evidence.py`; `harness/scene.py`, `access.py`, `scenarios.py` | their families | `02_CHAR_voices_and_the_room.md` (B10); `05_SC_playable_hearing_B.md`, `05_SC_evidence_and_rebuttal_B.md` (B24); `01_CORE_one_scene_contract.md` (B34); `28_CORE_scene_access_A` (B28); `08_FI_03_playable-inquiry.md` (B11) |
| `state/gate.py::may_levy`, `::may_wage`, `::commands` | MILITARY, PHYSICAL_B, BINDING_D | `06_FA_levy_through_the_seat_B.md`, `06_FA_war_lives_in_seats_B.md` edits 1–3, `14_VERBS_BINDING_D_orders.md` D2 (all B21) |
| `world_q.passage_granted` | RES-V, the land | `U5d_FA_land_and_seats_pass_on_a_won_march.md` decision 5 (B23) |
| `world_q.root_of` | `15_INSTITUTIONS_COLONIAL_B_distance.md` | itself (B33) |
| `engine/season/instruments.yaml`, `data/instruments.py` | the institutions kit, `23_STORY_B` | `15_INSTITUTIONS_COLONIAL_A_instruments.md` (B32) |
| `engine/season/valley.yaml`, `harness/valley.py` | `23_STORY_E`, `15_INSTITUTIONS_COLONIAL_E` | `07_SE_valley_scenario.md` (B12) |
| `engine/season/telling.yaml` | `09_WR_B_chronicle_that_tells.md` (uses it "once that table exists") | `30_GO_F_the_plot_as_the_player_is_shown_it.md` (B38); the chronicle runs without it until then (a later reach) |
| `modules/threadwork/`, `seam/wrappers/threadwork.py` | `14_VERBS_PHYSICAL_D` stage 2, the thread | `09_WR_B_threadwork_session_and_practitioner.md` (B35) |
| `scenes_per_season` | `21_PROCEDURAL_C` PG-5 `fade` | struck (C3-K6) |
| the WR motion-step symbol for an army's unprompted recovery | `27_MB_E` | not needed: computed when read (C3-L11) |
| `_eff_dispatch` (a `dispatch` that sends) | `14_VERBS_BINDING_D` D4, `15_INSTITUTIONS_BYZANTINE_C`/`_D` abroad | **no carrier** in the suite (v11 CP-T09-08); D4 and the hands abroad wait |
| a writer of `Person.coherence` | `U5d_WR_zero_coherence_unknowable.md`, `14_VERBS_PHYSICAL_D` | **no carrier** in the suite (v11 CP-T07-02, H-47); the readers ship and read nothing until it exists |
| the Court Parliament's working state | A-68's "parliament functional" | **no carrier** (H-90, unbuilt); A-76's stand-in (a working realm bench, switchable) ships in B23 |
| `req_forge.py` | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md`'s re-run line | **no carrier**: a scratch script; B02 replaces the line by the removal-test arm's `storybar` reading (§6.2 rule) |
| a goal row carrying `axis:` | `31_WR_C_what_the_stances_feed.md` (all 38 goal rows print `None`) | **no carrier**: authored content; `31_WR_C` ships at its control until the rows are authored |

---

## 7. Limits of this order (stated once)

- The edges are the read lanes' extraction; this lane resolved names by script and checked the resolution by the
  zero-unresolved count (two unresolved tokens are tree files: `02_P1_templates.md` and
  `08_decks_and_template_in_engine_form.md`, both EXISTS per `R5_READ.md:567`). A dependency a read lane did not
  record is not in the graph.
- "MISSING" in §3.1 is the read lane's mark, extracted from its row; an item the read lane marked missing inside a
  longer sentence may be shown under-collected. The read-lane row cited in the last column is authoritative.
- The file census normalises by file name; the names `config.py`, `core.py`, `table.py`, `units.py`, `wrapper.py`
  and kin are kept with their module where the read lane gave it and inferred from the lane where it did not
  (marked `?`).
- The unit-time schedule (§2.3) is an estimate; no batch runtime was measured.
- §6.1 checks test-file names against `git ls-files` (and lane A's branch); a test named only by function, or a gate
  that names no file, is not listed there (the read lanes' §7 lists them as INCOMPLETE).
