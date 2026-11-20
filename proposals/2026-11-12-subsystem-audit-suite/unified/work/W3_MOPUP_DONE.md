# W3 mop-up — cross-lane rows from the seven rewrite lanes

## Status: WORK FILE (progress record of the wave-3 cross-lane mop-up; resolves nothing at runtime; deleted when the stage closes)

Sources: the "for another lane" rows of `W3_2_DONE.md` (2), `W3_3_DONE.md` (3), `W3_4a_DONE.md` (2), `W3_4b_DONE.md` (1), `W3_5a_DONE.md` (4), `W3_5b_DONE.md` (1 section, 5 lane groups); `W3_1_DONE.md` has none. One producer, no fan-out. Each applied row adds a `Reconciled:` line (or a clause) to its target. Not touched: `audits/`, `U5_FINDINGS_CLOSURE_*`, code. Files under `proposals/` unless a path is given.

## Applied

| # | source row | target and change |
|---|---|---|
| 1 | W3-2 last row: lane-28 *occupy* → *engaged* | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`: "the occupancy half", clause `occupied`, `occupancy: off` → *engagement half*, `engaged`, `engagement: off` (28A head's fixture is `engagement`, checked). The file name of 28A keeps "occupancy". |
| 2 | W3-5a row 11 / Close: HAP_B edit 2 parenthetical | `22_HAPPENINGS_B_the_throne_is_never_stranded.md`: `off_duke_valorsmark: [off_heir]` → the throne's title list (checked against `16_PESSIMIST_FA_A` edit 1, A-19, C3-K9). W3-5b row 25 had named the edit but not made it. |
| 3 | W3-5a Close: HAP_D §3 T8/T12 | Already satisfied by W3-5b row 27 (`22_HAPPENINGS_D` lines name `terr_T8`/`terr_T12`). No edit. |
| 4 | W3-5a row 12 / W3-5b W3-5a group: `cross_chain` into BIND_C's obstacle table | `14_VERBS_BINDING_C_turnover.md`: `confer` row gains `cross_chain`. `U5c_SC_one_obstacle_form.md`: member 29 `cross_chain` added (FA-B's request; `Office.faction` compare at `state/gate.py` ~`:506`), since a table term must be a roster member. |
| 5 | W3-4b "For another lane": widen OBS member 12; `obligation` into `advantage_sources` | `U5c_SC_one_obstacle_form.md`: member 12 widened to the hearer's `owed_to` edges toward the other party; leverage source `obligation` added after `favour` (§3 order and row). Consistent with C3-C10 / F-39 / A-25. |
| 6 | W3-4b: BIND_C `revoke` Partial vs the 2026-10-21 disposal ruling ("check") | Checked at `engine/season/tests/test_in31_revocation_cost.py` docstring (the ruling's text): it prices a revocation by provenance and is silent on bands; no A-1..A-91 ruling speaks to a Partial revoke. `14_VERBS_BINDING_C_turnover.md` edit 6 marked `[ASSUMPTION]`. Not a conflict. |
| 7 | W3-4b: MATERIAL-B Partial's remainder read by `bills_due` | `14_VERBS_MATERIAL_B_stores.md`: sentence added. |
| 8 | W3-5a row 13 / Close: BIND_D edits 3-5 compose on FA_C's one `commands` | `14_VERBS_BINDING_D_orders.md`: edit 3 → pointer (no `state/gate.py::commands`), edits 4-5 compose on `world_q.commands`, head sentence repointed. |
| 9 | W3-4a row 7 / first bullet: cession case under C3-L7 | `U5d_FA_land_and_seats_pass_on_a_won_march.md`: new paragraph "The cession case"; edit 2 no longer has `_eff_surrender` pass `seats=` (tree: `_eff_surrender` returns `NO_CHANGE` when `receiver == a.actor`, actor is the yielder); gate arm (a″). `seize_place` stays `[ASSUMPTION]`. |
| 10 | W3-4a second bullet: A-81 needs `undeposited_kinds` to deposit an actor-only claim for a failed inquiry | `08_FI_04_small-edits.md` §1: paragraph narrowing the roster rule (tree: `rosters.yaml undeposited_kinds` and `loop/witness.py:381-386` drop `finding.none`); mechanism left to the `witness.py` edit; `[ASSUMPTION]` on the actor-only audience; named test. |
| 11 | W3-4a third bullet: BYZ_A/BYZ_E cite BIND_C's `provisional_term` 2 and Failure kinds | Already satisfied (BYZ_A line 128, BYZ_E line 71; BIND_C unchanged). No edit. |
| 12 | W3-5b W3-3 group: `09_WR_threadwork_module.md` edit 2 | Already satisfied by W3-3 row 34 (lines 3, 79-80 of that file). No edit. |
| 13 | W3-5b W3-3 group: `16_PESSIMIST_WR_C`, `09_WR_B_weather…`, `06_FA_seat_terms_by_body_B`, `07_SE_population_regrowth_B` read the year roster | Already satisfied (each cites `seasons_of_year` / D-U1-10; WR_C names the literal `-4 × age` gone). No edit. |
| 14 | W3-5b W3-3 group: `31_WR_A` commit-table row 4 wording | `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md`: row 4 now says NARR_D owns only the key, loader and readers, reader is its commit 1, this commit 4 is the declared mover. |
| 15 | W3-5b W3-3 group: `30_WR_G` `--crossings` → `--overlaps` | `30_WR_G_regime_opinions_and_the_pull_of_ones_own.md` gate line. (The tree's `storybar.py` has neither flag; `20_NARRATIVE_F` defines `--overlaps`.) |
| 16 | W3-5b W3-3 group: `07_SE_valley_scenario.md` loader admits `age_years`, `conferral`, `sworn_to`, `holders`, prehistory `to:` | `07_SE_valley_scenario.md` §4(a): closed key set paragraph and a named test. |
| 17 | W3-5b W3-3 group: `16_PESSIMIST_FI_C` `leaves` channels for its three `covert_kinds` | `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md` edit 1: the three maps from PROC_C (f), `[ASSUMPTION]`. |
| 18 | W3-5b W3-2 group: CHAR Addendum sets `regard_sign: -1` on `release` and tie-ending rows; W4 carried once | `02_CHAR_scar_cap_and_regard_unit.md` Addendum: `release` added to the `-1` values (`release` is the only row listing `tie` in `domain:`, `verb_table.yaml:1341`). W4 carriage already there. |
| 19 | W3-5b W3-2 group: `02_CHAR_scar_is_a_wound` lands before `stands_for` (B10 vs B38), one owner of the threshold | `02_CHAR_scar_is_a_wound.md`: `primary` arm for affiliations calls `person_q.stands_for`; no `scar_affiliation_floor`; writer-first order `[ASSUMPTION]` (descriptor scale is `0-5`, so "above midpoint" = 3 or more, the same threshold). |
| 20 | W3-5b W3-1 group: `11_GO_player_surface_contract.md` §4 (REST_3 C-5) if it survives | Already satisfied: that file is SUPERSEDED except §2 and its first `Reconciled:` line already carries C-5. No edit. |
| 21 | W3-5b W3-1 group: `14_VERBS_PHYSICAL_A` A3 reads `mortal_terms(..., endurance)` and the cause `spell` | `14_VERBS_PHYSICAL_A_custody_and_force.md`: `mortal_terms(...)` reading already present; fixtures row names `spell`. Fixture-name mismatch carried (below). |
| 22 | W3-5b W3-4a group: carrier check of C1A_02 W2 | `17_CENSUS_C1A_02_wires_and_corrections.md`: check made. One row has no carrier: `march`/`_siege` (`effects_combat.py:686`, reached `:520`) — `14_VERBS_MILITARY_A_movement.md` edits `move`/`migrate` only; `besiege` has no carrier (CP-T04-06). Marked INCOMPLETE. The other rows' execution is the closing gate's, not asserted. |
| 23 | W3-5b W3-4a group: rows that adopt a stake move from the `task` class to shape (b) | `14_VERBS_MATERIAL_B_stores.md`: `requisition` (the only listed row still in shape (a)); one move serves the stake and `requisition.rendered`. `move`/`migrate`/`found`/`build`/`sabotage` already shape (b). |
| 24 | W3-5b W3-5a group: `16_PESSIMIST_CHAR_A` owns the switch as `crisis_arm`, `reading="any"` | `16_PESSIMIST_CHAR_A…md`: `crisis_draw: off|on` → `crisis_arm: rule|drawn` (U1 F-43); `reading="any"` was already there. No `crisis_arm` in the tree (grep of `engine/season`). |
| 25 | W3-2 row 60: `08_FI_08` §1, §4 handed to the Thread lane (A-28) | `09_WR_threadwork_module.md`: receiving clause naming both sections; neither landed there. |

## Carried to the v12 stage (not edited; source row in brackets)

- Records of U1/U3 are not edited here: each item below is an owed correction to `unified/U1_OWNERS_AND_VOCABULARY.md` or `unified/U3_*`.
- U3 §1 item 4 / §3.1 still say "two declared movers" for `06_FA_hygiene` (none now; D-U1-11h) [W3-3].
- C3-L7 corrected at the tree: `Act.via` is a SeatId; the `claim` basis admits only heirs (`gate.py:236-253`); built as reading (i); U3 re-check owed [W3-3].
- C3-C4's stated reader of `Rung.envelope` is wrong (none reads it; `harness/probes.py:1851-1856` writes) [W3-3].
- C3-C2 vs D-U1-09 on `07_SE_capability_rate_B` §4 (e): D-U1-09 applied; the labour verb row and caller open [W3-3].
- R3 §1 cited `rosters.yaml: module_kinds` for `entry: query`; the home is `references/module_contracts.yaml` composition rows [W3-3].
- C3-K7 omits `31_WR_C` commit 3 (edits `harness/storybar.py`); placed last [W3-3].
- R3 7b-13 not applied (C3-N22 keeps each file's horizon); `besiege` is not in `march_postures` [W3-3].
- Identifier rename `Regime`/`regimes`/`regime_relation` → creed-body names across `30_WR_B`, `30_WR_G`, `31_WR_A`, `20_NARRATIVE_A`, owed at landing [W3-3].
- U1's own file: §3 `bench_reading` row and ledger C-22 still carry the threshold form; §3 item 5's `told_retain` line conflicts with C3-C14 [W3-2 rows 6, 63].
- Undecided names and members for U1: OBS membership of MIL_A–D's hostile terms and PHY_B's army-size source; `seize_place`; the challenge's `spent` stage; `requisition.rendered` vs `.taken`; `provisional_term`'s value (F-33 and U3 §11 each passed it) [W3-4a].
- `distance`'s definition (OBS: ladder `contain` edges; COL_B: territory adjacency + `border_hops`); one reader `world_q.distance` either way [W3-4b].
- Home of the three unruled seat keys (`patronage`, `eligible_from`, `cooling_off`, taken as tables); count of authored persons outside A-44's cap; `dignity` seat key [W3-4b].
- The qualifier key name of A-46's narrow `commitment.ended` entry (`20_NARRATIVE_D` edit 4 proposes `object_of`; strand-roster owner to fix) [W3-5b].
- `mortal_wound_ob` (PHYS_A, U1 P-13) vs `mortal_ob` (HAP_A edit 3): one fixture name needed [found at row 21].
- `U3_DEPENDENCY_ORDER.md` line 116 still names `crisis_draw: off` (now `crisis_arm: rule`) [found at row 24].
- U3/R5 rows corrected at the tree by W3-5b (`test_obligees.py`, §1 items 4/36/38/39/32, §4.1 rows 8/75-76/87, C3-R1, R5 HAP_D territories, glossary *lapse* file list) [W3-5b, informational].
- Owed Layer 1 text (Jordan): A-9, A-29, A-30, A-20 (`04:460`), A-84, A-85 `ED-IN-0352` (3), `04` §C.2 opening basis for seats freed by seizure, `04` §B.3/A.2 `Rung.envelope`, PART D row 36 amendment, J-U3-01 [W3-3/W3-5a, listed there].

## Not applied

- W3-2 last row, second target: `unified/U5_FINDINGS_CLOSURE_U5a.md` still says `occupied` — excluded by the order (no `U5_FINDINGS_CLOSURE_*` edits). Left for the stage that owns it.
- No row conflicted with A-1..A-91. One row was wrong at the tree in part: W3-4a's "name the cession case beside the won-field case" had to include removing `_eff_surrender` from the `seats=` callers in `U5d_FA_land` edit 2, which the row did not say (row 9). The BIND_C `revoke` check (row 6) found no conflict, only silence.

## Assumptions made

`[ASSUMPTION]` marks are in the edited files: rows 4 (member 29 added to OBS), 6, 9 (`seize_place`), 10, 16, 17, 19, 23. Basis for each is at the site.
