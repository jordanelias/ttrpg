# W3-1 rewrite lane (R1 set: PC, MB, DICE, GO): progress

## Status: WORK FILE (progress record for `unified/WAVE3_REWRITE_ORDER.md` lane W3-1; resolves nothing at runtime; deleted when the stage closes)

Lane run family by family (PC; MB `04_*`; MB `26_*` + `U5b_MB_*`; MB `27_*`; DICE; GO) by one producer (no agent tool was available, so no sub-agents). Each family's ordered list of finished files (file; rows applied; rows not applied and why) is appended below as it closes.

## PC (11 files) — finished

Note: the lane had no agent-spawning tool; it ran as one lane, family by family (0 sub-agents).

| # | file | rows applied | rows not applied, and why |
|---|---|---|---|
| 1 | `03_PC_duel_chain_reach.md` | R1 §1.1 (V-13 settles `[UNVERIFIED]`), 7b-1, 7b-19; U3 B01, §4.1 row 0, C3-A1/A2 | 7b-1's call-site sentence corrected at the tree (production caller `decision/choose.py:541`, not `play_surface.py`) |
| 2 | `03_PC_duel_round_and_approach.md` | R1 §2 A-30 (key), §2 YIELD_HEALTH_FRAC (A-24), §6.1 (d), §7 (superseded in part → PB); D-U1-11b; U1 P-03; C3-N4; U3 B16 | R1 7b-12 Option A (delete `nested_entry`): U1 §2 keeps `nested_entry` |
| 3 | `03_PC_duel_round_and_approach_B.md` | R1 §1.1 (key; `PersonInterior`; snapshot closure; view list closed, Option B; `approach_responses` refusal), 7b-2, 7b-3/D-U1-08, D-U1-11b, C3-N4/§6.1 (a), 7b-4 (`form` comment); probe → workbench file; U3 B16/B30 | 7b-12 (as above) |
| 4 | `03_PC_exits_withdrawal_recovery.md` | R1 §1.1 Part B history removed, §2 A-8/A-24/A-31/A-81, 7b-14; C3-C8, C3-C11; U3 §4.1 rows 47, 55; C-32/U1 P-12; A-30; D-U1-08 | 7b-14's new test file replaced by the existing `test_cp_t03_08_tend_on_the_wounded.py` |
| 5 | `03_PC_loadout_and_carry.md` | D-U1-11d (rule in `combat_kit.py`, host hands shortfall raw), §6.1 (c), 7b-4, glossary *unit*; tests, call sites; U3 B18, §4.1 row 61 | R1 7b-5 [DECISION] (a `combat.carry_demand` role): U1 D-U1-11d decided otherwise |
| 6 | `03_PC_person_inputs_content.md` | R1 §2 A-71/A-79; D-U1-08; glossary *skill* → `axis`; V-18 settles `rung_kinds`; Part D pointer → PB; tests; U3 B18 | — |
| 7 | `03_PC_typed_outcome_one_door.md` | D-U1-11a (`prevailed`), D-U1-06/C3-L5 (`observation_terms`, docstring), D-U1-08, glossary (`axes`), R1 §1.1 (not a Margin), A-81/C3-C11; order, tests; U3 B14, §4.1 row 51 | — |
| 8 | `03_PC_weapon_form_at_round_start.md` | 7b-4 (`form` kept), probe written as workbench file (rule 4 overrides 7b-4's commit-body choice); tests; U3 B14 | — |
| 9 | `03_PC_weapon_records_in_the_export.md` | C3-N17, C3-N18 (re-counted at the tree: six of ten ARSENAL classes, `siege` omitted before), parity probe → workbench file; tests; U3 B14 | — |
| 10 | `U5b_PC_residue.md` | R1 §1.1 §4 edit 2 (raise → no-default signature; callers grepped), §7/§8 keyed (A-30), U1 R-27, glossary *axis*, `[grep at landing]` sites (§2 none; §6 five importers, not three); U3 B14/B15/B18 | §10 left INCOMPLETE: `scan_tests.py` not in the tree, the ten loops not identified |
| 11 | `U5b_PC_rulings_in_the_fight.md` | D-U1-11b + U1 §2 (`nested_entry` homed in `seam/contest.py` [ASSUMPTION], typed refusal = `ContestError` at the tree), D-U1-08, U1 P-02 (1.07 decided), U1 C-07 (`reader:` cell), D-U1-11a; R1 §1.1 (keyed window draw; `expected_by(PersonInterior)`); C3-N3, C3-D4; probes → workbench files | 7b-12 Option A (U1 wins) |

Row corrected at the tree: D-U1-11b names `Refusal(depth_cap)`; the tree's typed refusal is `seam/contest.py::ContestError("max_depth reached", …)` (`:28-36`, `:238`); written as both.

## MB `04_*` (10 files) — finished

| # | file | rows applied | rows not applied, and why |
|---|---|---|---|
| 12 | `04_MB_campaign_party_economy.md` | R1 §1.2; A-30 (veterancy key); H-158 functions located at the tree; tests; U3 B31 | `U1_GLOSSARY` *arm* → `branch` for this file: wrong at the file (`veterancy: {arm: off|steps}` is a switch, the glossary's own sense) — corrected, not applied |
| 13 | `04_MB_cell_hierarchy_as_data.md` | C3-N11; R1 §7 ranks seeds (sourced 2/4/2, missile 2 [ASSUMPTION]); D-U1-11o; glossary *band*→`layers`, *approach*→`opening_rows`, *body*→block, *post*; probes → files; tests; U3 B19 | — |
| 14 | `04_MB_cr12_linear_law.md` | C3-C6, 7b-9; A-59/A-77 planted carrier; tests/lands; U3 B19 | — |
| 15 | `04_MB_headcount_grade_and_scale.md` | R1 §2 A-67/A-68/A-70 + 7b-10 (Drawn re-homing); A-3 (C3-L2 owed row); A-81/A-80; struck text removed; tests; U3 B17, §4.1 row 60 | — |
| 16 | `04_MB_manager_battle_one_resolver.md` | R1 §2 A-59/A-77 (`fortune` gone), A-61, A-30; D-U1-11f (`standing_order_cap`), D-U1-11g (`rally` on `CommandRecord`), D-U1-11b; A-3 conflict line; `lever_probe` → file; tests; U3 B20/B30 | — |
| 17 | `04_MB_playable_field_scenario.md` | R1 §2 A-57/58/66 + C3-L12 (end condition = aggressor's `seize`; head lines corrected), A-67/68/70 (§C), A-81 (gate 7), A-77; U5b head (2) applied to body (`armies_at_build`, `troops.yaml: doctrines`, MIL-C Edit 5); D-U1-06; struck §B text removed; tests; U3 B20/B22 | — |
| 18 | `04_MB_squad_grid_of_named_characters.md` | 7b-11 (composition row); struck text removed; pointers → PB; D-U1-11f, D-U1-11b; glossary *exchange*→pairing round, *command*; A-30; tests; U3 B30 | GC-9's row-rule choice left as written (a design choice no ruling settles) |
| 19 | `04_MB_typed_outcome_and_one_path.md` | R1 §1.2 config + 7b-13 + D-U1-11c (explicit `cfg`, no context variable); A-29; D-U1-11g/M-23 (§4 integer removed); D-U1-06; D-U1-11e; order, tests; U3 B17 | — |
| 20 | `04_MB_unit_loadout_and_weapon_in_hand.md` | R1 test 9: status SUPERSEDED; resolution text replaced by a pointer naming what `_B` keeps/replaces; confirmations table kept; U3 §4.1 row 7 | — |
| 21 | `04_MB_unit_loadout_and_weapon_in_hand_B.md` | D-U1-11d (host calls `combat_kit.carry_demand_of`); §1.2 data dependency; C3-N18 (six of ten confirmed); D-U1-11c; tests; U3 B17/B31, row 61 | — |

## MB `26_*`, `27_*`, `U5b_MB_*` (13 files) — finished

| # | file | rows applied | rows not applied, and why |
|---|---|---|---|
| 22 | `26_MASS_BATTLE_aggression_and_land.md` | R1 §2 A-65/A-66 + C3-L12 (seize is an act), A-67/68/70, A-68/A-85, A-70 (§4 plain reading), A-74, C3-L7 (no `conquest` basis); open items 1–4 answered; tests; U3 B23 | — |
| 23 | `26_MASS_BATTLE_calibration_targets.md` | `gauge_mb.py` opened (`[UNVERIFIED]` settled; block = `run_results()`); A-77; U1 M-08; C3-D2; tests/lands; U3 B19 | — |
| 24 | `26_MASS_BATTLE_cell_scale_and_time.md` | R1 §1.2 VIOLATES + 7b-15 Option A (bout loop inside `resolve_field`); glossary `opening_rows`, season; D-U1-11e (`bouts`); stamina share; A-30; tests; U3 B19, row 65 | U1 D-U1-11e assigns `fight_loss` here: wrong at the proposals (`26_rout` §4 defines it) — corrected |
| 25 | `26_MASS_BATTLE_maneuver_orders.md` | R1 §2 A-6/A-7/A-59 + §6.1 (e) (§1 → `27_MB_A` §4 form, kinds as steps), A-30, A-59/A-77, D-27a watch, U1 M-08, D-U1-11g; tests; U3 B20 | — |
| 26 | `26_MASS_BATTLE_movement_and_fatigue_as_data.md` | U1 §3 stamina share, D-U1-11c, glossary season; tests, call sites; U3 B31, rows 64/79 | D-U1-11e's owner of `stamina_left` (this file) corrected by order: `27_MB_E` 27E-2 lands first (B22) and declares it |
| 27 | `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` | R1 §1.2 VIOLATES (one ladder `degree_from_net`); A-61; A-24 [ASSUMPTION]; A-30; D-U1-11e (`fight_loss` declared here); tests; U3 B19, row 66 | re-targeting site left INCOMPLETE: `orchestration.py:2191` is the harness `run_multi_unit_battle`, not the season site |
| 28 | `U5b_MB_rulings_in_the_field.md` | C3-N10, C3-L12, A-67/68/70, C3-D2, C3-D4, head Folded (2) into §6 row 4, D-U1-11b, A-30, V-16 counts; `mirror_probe` → file; tests; U3 B05/B19/B23/B30 | — |
| 29 | `U5b_MB_residue.md` | probes → files; C3-L12 (H-355); A-30; glossary *role*; U3 B17/B22 | §4's `[UNVERIFIED: which of the 35]` left (tests lane's scan not in tree) |
| 30 | `27_MB_A_command_and_the_obedience_draw.md` | D-U1-01 (seat = `office` level; §2, §5, gate 7, test renamed), U1 R-14 (`talent_level`), R-10/R-16 (`obey.task` stand-in; INCOMPLETE 2 closed), glossary distance step, A-25 [ASSUMPTION], C3-D2 (INCOMPLETE 4 closed), INCOMPLETE 3 partly read at tree; U3 B19/B05 | — |
| 31 | `27_MB_B_unit_prowess_on_the_row.md` | D-U1-11p, D-U1-11o, glossary `layers`; INCOMPLETE 1 closed by order; U3 B31 | order note: 27B-1/27B-2 are CR-12 step 2 and land in B19, not B31 as U3's node row has it (reported) |
| 32 | `27_MB_C_dynamic_strength_and_the_residual_chance.md` | D-U1-06/C3-L5 (`observation_terms`), D-U1-11e, C3-C6, C3-D2 (fortune keyed), INCOMPLETE 2–4 closed by order; U3 B19 | — |
| 33 | `27_MB_D_the_commander_as_chooser.md` | R1 §1.2 VIOLATES D-42 + 7b-16 (believed officer pool), §1.2 watch row (`obey_odds` not a field closed form), glossary `reach_steps`, D-U1-11f; INCOMPLETE 2–3 closed; U3 B20 | 27D-4 stays returned to CHAR |
| 34 | `27_MB_E_what_an_army_carries_back.md` | C3-L11 (computed when read; `world_q.army_strength`; motion step removed; INCOMPLETE 2 closed), mover rewritten, A-30, D-U1-11e by order (`stamina_left` declared here), D-U1-10; U3 B22, row 63 | share tables and window stay NOT ESTABLISHED (Jordan's or a source search) |

## DICE (8 files) — finished

| # | file | rows applied | rows not applied, and why |
|---|---|---|---|
| 35 | `10_DICE_advantage_sources_for_the_arcs.md` | 7b-17 + 29-4 step 5 (bilateral `_wound_levels`); U3 §6.1 (`test_effort.py` → `test_cp_t01_05_npc_effort.py`); D-U1-01 (§E ARC-53 row: `office` level); U1 R-27; U3 B05 | R1 §2's "add (A-12)" superseded by D-U1-01 |
| 36 | `10_DICE_believed_odds_have_a_prior.md` | D-U1-06 / R-30 / C3-L5 (Edit D withdrawn), A-5 (`settled_margin`), A-79 (prior via `opposed_ob`), old-regime figures marked; tests; U3 B05 | — |
| 37 | `10_DICE_capability_axiom_map.md` | body brought to head: D-U1-01, D-U1-02, D-U1-07 (§B → pointer), D-U1-08, D-U1-06, C-07 site map, A-6, A-7, A-8, A-5; §G edit 9 (`opposed_roll` key) withdrawn; tests, call sites; U3 B04 | — |
| 38 | `10_DICE_exported_face_rule_and_band_edges.md` | A-5 (B, C, Problem 3, ED-833 paragraph removed), C3-L1 (`MARGIN_SCALE`, `BAND_FLOORS` in milli-units); tests; U3 B05 | — |
| 39 | `10_DICE_one_roller_one_fraction_rule.md` | 7b-7, C3-L1 (Edit A withdrawn), C3-N16, UMR §1 (continuous roll; `roll_pool_fractional` deleted); gates rewritten; U3 B05, row 18 | — |
| 40 | `10_DICE_one_score_two_roles.md` | 7b-6, D-U1-02 (head), D-U1-08, C3-A3, C-04; old-regime figures removed; U3 B04/B05 | — |
| 41 | `U5a_DICE_owed_edits.md` | C3-L1 (rows 1, 6), C3-D2, UMR §1 row 2 (row 4), Edit B bilateral, U1 R-27; row 2's call sites grepped (incl. three off-loop SC oracles, re-pointed); tests; U3 B05/B09 | — |
| 42 | `29_DICE_one_opposed_rule_form_and_tuning.md` | C3-L1 (D-29 row added), D-U1-08 (`defender.score`), OWED §B (table row 3 matched to item 29-2), glossary talent/training, J-29-01 CLOSED (A-79), item 29-5 round half completed; U3 B04/B05/B15/B30 | item 29-5 hearing half stays INCOMPLETE (`HearingInput`, `Speaker` unbuilt; R2's `05_SC_playable_hearing_B.md`) |


## GO (10 files) — finished

| # | file | rows applied | rows not applied, and why |
|---|---|---|---|
| 43 | `11_GO_design_reference_disposition.md` | R1 §1.4/§7; U3 B03; lands/tier | — |
| 44 | `11_GO_fidelity_and_campaign_modes.md` | A-30 (§4), A-1/A-4, D-U1-11n; U3 B34; tests/lands/tier | — |
| 45 | `11_GO_float_contract.md` | C3-L3 (Part B recorder removed; vectors), A-29 Part C ruled C2 (Layer 1 text owed to Jordan); gate 2 vectors; U3 B06 | — |
| 46 | `11_GO_one_draw_owner.md` | A-30 (Draw.u = keyed mix of (key, n); recorder, replay gate and GO-16 row removed; GO-08 vectors); `rngsource` Option A (threaded `rng`); U5b_PC_residue §4 (no-default signature); C3-Y10, C3-D3; go_probe scratch replaced by a named test; U3 B06 | `H2` homed in `draw.py`, not `ids.py` (leaf import rule) — reported, [ASSUMPTION] |
| 47 | `11_GO_player_surface_contract.md` | SUPERSEDED except §2 `explain` (live; typed `PersonInterior`; tests, build order, B34); A-30 draw row | — |
| 48 | `11_GO_player_surface_contract_B.md` | C3-L4 (host-side `receipt` deleted; two-branch §3 with test; WITNESS site `witness.py:339`, `:650-651`); C3-L5; R1 row 154 (`PersonInterior`, `View`); A-63/A-64 edge to lane 28; `PhaseOrder` → `GeneralAction`; glossary firmness grade; build order/tests; U3 B34 | D-U1-11n's `act_result` not built: U3 C3-L4 wins (person-side) |
| 49 | `11_GO_pointer_and_stale_text_resolutions.md` | R1 row 160 (items 4–5 merged with A-30 row text, one hunk; 4–6 owed to Jordan's merge); item 12 per A-30; C3-N15; U3 split (item 5 B06, rest B03); lands/tier | — |
| 50 | `11_GO_port_gate_order_and_coverage.md` | A-30/C3-L3 (no draw/float logs; GO-16 not built in §2), A-4 (§3 decider → `04_MB_manager` §4), C3-N15 (§4 command), 7b-8/D-U1-11c (§5 partition; build is `04_MB_typed_outcome` §3 in B17, this file checks); scenario names [ASSUMPTION]; gate 2 test; U3 B41 | — |
| 51 | `30_GO_F_the_plot_as_the_player_is_shown_it.md` | C3-L4 (recap reads `account`), glossary firmness grade, U1 player-view row, R1 row 161 flag (1) (CONVENTION grade), View builder named (`deliberate.py:168` → `questions.py::assemble` `:22`/`:51`); U3 B38 | — |
| 52 | `U5d_GO_owed_edits.md` | R1 row 163 (CONFORMS), A-30 sentence; §1 test names; batch order of §2 checked; U3 B06 | — |
