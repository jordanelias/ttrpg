# L1_PROPAGATION — proposals that still carry a "waits on the amendment" clause

## Status: WORK LIST (the Layer 1 amendment lane, 2026-11-12; reference, resolves nothing at runtime; for the later pass that removes the clauses; deleted with `unified/work/` when v12 is adopted)

The `L1` nodes are APPLIED (`unified/work/L1_APPLIED.md`, `ED-IN-0358`). The proposals below still say their Layer 1
text is owed, drafted and not applied, or that an arm waits on Jordan's amendment. **This lane edits no proposal**; a
later pass removes or rewrites each clause. Found by grep over `proposals/` (not hand-read in full):
`grep -rniE "amendment" proposals/ | grep -iE "layer 1|\`04\`|04 §|PART D|§B\.7|§C\.|holonic|Jordan's amendment|L1-"`,
then `grep -rnE "only once the owed|until (Jordan|the node|the amendment)|applied only by|by Jordan's amendment|Jordan applies"`.
Lines are as read 2026-11-12.

| proposal (under `proposals/`) | lines | node it waited on | what the later pass does |
|---|---|---|---|
| `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` | 3, 17, 107 (edit 5) | `L1-A9` | drop edit 5 (applied); the `interactions_per_scene` above-1 arm no longer waits |
| `18_DETERMINISM_rival_acts_in_one_fold.md` | 5, 7, 11 | `L1-A64` (row 36) | drop "the PART D row 36 amendment text … stays Jordan's" |
| `28_CORE_scene_access_A_occupancy_and_precedence.md` | 3, 209-216 (edit 8), 321 | `L1-A64` | drop edit 8 and the "VIOLATES … until Jordan applies it" clause; `precedence_level` may be set |
| `06_FA_war_lives_in_seats_B.md` | 9, 62, 91 (edit 4) | `L1-A20` | drop edit 4 (applied at `04:460`, row 48, F.32) |
| `16_PESSIMIST_GO_keyed_draw_no_recorder.md` | 16, 106 | `L1-A30` | drop the "owed" status clause and the `04` §C.12 row of its edits table |
| `11_GO_pointer_and_stale_text_resolutions.md` | 3, 30 | `L1-A30` (items 4–6 edit `04:927`, `:955-959`) | drop the `04` items as applied (the text applied is the U3 draft, not this proposal's wording) |
| `11_GO_float_contract.md` | 97 | `L1-A29` | Part C applied at step 13 (`04:1131`); the line that says D-29 holds stays true |
| `14_VERBS_BINDING_C_turnover.md` | 13 | `L1-A12` | drop "stands only once the owed `04` §B.7 amendment … is applied" |
| `13_SC_tuning_tables.md` | 137 | `L1-A12` | drop "`04` §B.7 amendment text is owed … not applied"; the bench die may leave null |
| `U5c_VERBS_residue_and_governance_owner.md` | 243 | `L1-A12` | drop "A-12's amendment to `04` §B.7 is owed" |
| `15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` | 234 | `L1-A12`, `L1-A13` | `dignity` is NOT among the applied keys (A-13 applied `passes_through?`, `hand_term?`, `audit_at_exit?`; A-12 applied `modifier?`); its clause stays, re-pointed |
| `U5c_SC_one_obstacle_form.md` | 32 | `L1-A12` | the `office` source's `modifier?` read is now Layer 1's; drop any held-at-null clause tied to the amendment |
| `04_MB_manager_battle_one_resolver.md` | 3 | `L1-A3`, `L1-A4`, `L1-A72` | the field decider and `duel` callable no longer wait |
| `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` | 23 | `L1-A92` (J-U3-01, answered as A-92) | "`sway_gain` at 0 until Jordan answers J-U3-01": answered and applied; the dial waits only on the calibration batch |
| `U5a_CORE_owed_edits.md` | 139 | `L1-A62` | drop "the amendment … owed" for D-51 (applied at row 51) |
| `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` | 9, 11, 12, 154 | `L1-A96`, `L1-A96b` | the Failure arm no longer waits; **edit 8 (the oath arm of `may_warrant`) should be replaced** by the `detention` basis `L1-A96b` names (see `L1_APPLIED.md` §L1-A96b) |

**Not tied to an applied node (stay as written):** `30_WR_A_the_era_is_a_named_period.md:5` (A-84, the strife master,
held); `U5d_FA_land_and_seats_pass_on_a_won_march.md:93` (a twelfth gate basis `conquest`, no ruling A-n applied it;
`04` §C.2's enumeration is also behind the code's five bases, see `L1_APPLIED.md`); `U5d_SE_owed_edits.md:3, :53`
(`Rung.envelope`, IN-44, not a ruling); `08_FI_04_small-edits.md:114` (`04` §A.2 `loop/witness` row, no ruling);
`01_CORE_reason_trail_in_the_act_store.md:74` and `02_CHAR_reason_trail_and_small_edits.md:3` (`Scene.decided`, no
ruling); `U5b_MB_residue.md:59` (R-38, ED-IN-0306 note, no ruling); `02_CHAR_capability_definitions.md:5`,
`16_PESSIMIST_DICE_task_difficulty_and_throughput.md:11`, `18_DETERMINISM_task_draw_for_uncontested_verbs.md:7`
(amendments to other proposals, not Layer 1). False positive of the second grep: `26_MASS_BATTLE_cell_scale_and_time.md:93`
("until Jordan sets it", a `volleys` value, no Layer 1 node).
