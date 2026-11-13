# Evaluation of workplan v11, part 10: lane E3, tables and carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The tables and carry-forward blocks of lane E3, copied by script from `master/eval/E3.md` lines 27 to 682, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E3:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

## Table 1 — part 6 (the Jordan queue)

| id | gist | disposition | evidence / cite | v12 target (STILL-NEEDED / MISSING-DEP) |
|---|---|---|---|---|
| M1 | how deliberate an NPC's choice is (polarity, aggregation, believed odds, tau, cohort vectors) | DONE-IN-CODE | `data/fixtures.py:963` `stance_polarity="declared"`, `:547` `question_aggregation_rule="first"`, `:971` `odds_weighting="believed"`, `:321` `choice_temperature=0.05` (CR-17's derived value), `cohorts.yaml:145` `temperaments:`; `T:test_cr17_odds_weighting.py`. Session extends, does not replace: `P:02_CHAR_resolve_and_temper` (B10), `P:02_CHAR_goal_lean_on_its_own_question` (B10). | — |
| M2 | where a person's resolution inputs come from; the tenth attribute | DONE-IN-CODE | `data/fixtures.py:479` `practice_cap=2`, `:1060` `competence_gain=0.0` (control); `T:test_cr19_competence_gain.py`, `T:test_cr20_attributes.py`; `references/descriptor_registry.yaml:47` `attr.mind.will` named Spirit (Jordan's ten, ED-IN-0328). The input model is re-opened by session rulings A-7 (two inputs) and A-98 (one capability kind, skill) through `P:U5a_capability_home_and_two_inputs` (B04): that is session content layered on this decision, owned by E1's CR-18 to CR-20 rows. | — |
| M3 | what a troop is once raised (stock in `Rung.stores`, field force, company Person) | SUPERSEDED | A-2 (a unit is a row of data on the army's record; ED-IN-0306 stands) replaces option (A)'s `Rung.stores` stock and the Layer 1 `04:793` amendment it needed; the rows are `P:04_MB_headcount_grade_and_scale` (B17), `P:04_MB_unit_loadout_and_weapon_in_hand` (B17), `P:14_VERBS_MILITARY_C_the_muster` (`recruit`, `discharge_troops`; B22). `DECISIONS_FOR_JORDAN.md` D-02 shows the option A (a row) answered. | — |
| M4 | when a field is fought; what it leaves | DONE-IN-CODE | Ask B (b): `data/fixtures.py:803` `field_winner_casualties="engine"`, `T:test_cr_24_winner_casualties.py`. Ask C (a) same-round fields: unchanged (`loop/encounter.py`). Session adds the end state and the return (A-3, A-67 to A-70, A-78) through `P:04_MB_headcount_grade_and_scale`, `P:26_MASS_BATTLE_aggression_and_land` (B17, B23); they extend, not replace. | — |
| M5 | where a works comes from | DONE-IN-CODE | `venues.yaml:188` `planned_works:`; `harness/populated.py::mint_planned_works`; `T:test_in45_planned_works.py`. Session `P:14_VERBS_MATERIAL_C_works` (B12) builds on it; A-55 (fixed map, empty founded household may lapse) does not contradict. | — |
| M6 | how scarce the world is (hunger magnitude) | DONE-IN-CODE | `data/fixtures.py:678` `body_step=10` (REM-52 shipped), `:512` `hunger_band_floors=(1, 2)`; `T:test_hunger.py`. Residue: the calendar flip (`year_length` appears in no engine file: `grep` 0) is CP-T10-03's, dispositioned by E5; session `P:09_WR_B_weather_with_memory_and_the_year` (B12) names `year_length` as absent too and carries the year. | — |
| M7 | which ties carry a seated line past death | DONE-IN-CODE | `rosters.yaml:3090` `continuation_ties` (closed ordered roster, loader refuses a member with no reader: `queries/world_q.py::_TIE_READERS`); `T:test_cp_t02_06_continuations.py`. A-19 (deed race when the line fails) adds a branch for the throne (`P:22_HAPPENINGS_B_the_throne_is_never_stranded`, B21); extends. | — |
| M8 | can a living top-seat holder be removed (corrected: joint-concurrence deposition of the throne, CR-37) | STILL-NEEDED | Tree: `offices.yaml:194` `off_king` `revocation: null`; `grep joint_concurrence` finds 0 files; CR-37 is not built. Session amends but does not supersede: `P:06_FA_seat_terms_by_body_B` edit 3 (A-35, A-36) rewrites CR-37's sentence ("deposition is the turnover of a life seat"; the Confessor is excluded) and `P:15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger` names "any deposition motion (CR-37)". No A-n replaces Jordan's 2026-10-26 words. | FA, batch B21 (with `06_FA_seat_terms_by_body_B`); edit set `state/gate.py::REVOCATION_RULES`, `offices.yaml: off_king.revocation`, `data/rosters.py` revocation_bases; gate: a hand-built motion revokes the throne by the Holy See's `revoke` at `joint_concurrence`, and a planted single signer is refused; moves hashes: no (hand-built only; `off_king` null today); tier opus. Block 1. |
| M9 | may persons lie | DONE-IN-CODE | `data/fixtures.py:1068` `lie_offered=True`; `T:test_cr27_lie.py`. Session `P:14_VERBS_SOCIAL1_C_persuasion_and_deceit` (B28) re-draws the `lie` row on two arms; extends. | — |
| M10 | does a march need a declared war | SUPERSEDED | v11 itself superseded option (b) by ED-IN-0317 (a march needs a casus belli, carrier CR-91). The session replaces both: A-58 (aggression is read from the act; a casus belli "is context ... not a precondition"), A-68 (peace and a working bench make an unopposed entry a disliked trespass), A-74 (a march may also be thought of on a claim or grievance), carried by `P:26_MASS_BATTLE_aggression_and_land` (B23), `P:06_FA_war_lives_in_seats_B` (B23), `P:14_VERBS_MILITARY_A_movement` (B22). `grep casus engine/season` finds only a hole-register comment: CR-91 is unbuilt. See item J-E3-1 for Jordan. | — |
| M11 | may an agent land unmarked Layer 0/1 text (D-1); sixth §C.6 channel row | DONE-IN-CODE | Jordan's answer (a) 2026-10-26 recorded in `registers/editorial_ledger_in.jsonl` (ED-IN-0299/0300 rows); the hunks are applied (`CLAUDE.md` carries no `mc_v18`: `grep -c` 0). A-97 ("Layer 1: make amendments as required") is the session's wider licence. The sixth-row channel itself is CR-29 (E-lane). Whether `04` §C.6 has the sixth row: not opened. | — |
| M12 | a focalized journal for the player | SUPERSEDED | `P:09_WR_B_chronicle_that_tells` (B36) folds A-49, A-33, A-43: "the focalized journal is the in-play telling and reveals nothing its holder does not hold"; `P:11_GO_player_surface_contract_B` (B34) is the surface. `grep focali` in `queries/` and `harness/` finds nothing: NM-W5 is unbuilt and replaced. | — |
| M13 | "do you rule Godot 4.6" | WRONG | The ruling exists and is not 4.6: `registers/editorial_ledger_go.jsonl` ED-GO-0002, status `resolved`, "RULED BY JORDAN 2026-10-09 ... the Godot 4.7 series. His words: 'Actually, adopt Godot 4.7 now'", which supersedes the 4.6 note. The question's premise (a 4.6 to confirm) is false at the ledger. `P:11_GO_port_gate_order_and_coverage` says GO-01's one need (ED-GO-0002 on `main`) is met. | — |
| M14 | the cell-value and cosine pass | DONE-IN-CODE | `T:test_cr21_cells.py` (CR-21 landed); `data/fixtures.py:862` `refusal_axis=None` (arming left open as the row says). Session `P:02_CHAR_choice_alignment` (B10) adds cells on choice values; extends. | — |
| M15 | retire `CLAUDE.md` §0.2's `mc_v18` bullet | DONE-IN-CODE | `grep -c mc_v18 CLAUDE.md` = 0 (read this session). | — |
| M16 | exogenous event channel (weather per territory; Tensions receiver) | SUPERSEDED | Weather: `T:test_season_weather_per_territory.py` exists (commit (1)), but `data/fixtures.py:535` `season_factor_draw=()` still ships and the live arm is unbuilt; the session replaces its draw shape: A-54 (the one four-band ladder: weather, harvest and wear draw on place endurance against season hardship), `P:09_WR_B_draws_not_thresholds` (B12), `P:09_WR_B_weather_with_memory_and_the_year` (B12). Tensions receiver (a six-card deck read once at build, shipped off): `grep -rli tensions engine/season` finds nothing; replaced by A-50 (world cards draw bounded starting state) = `P:21_PROCEDURAL_D_world_cards_and_churn` (B39). | — |
| M17 | how a seat-holder learns what a larder holds | DONE-IN-CODE | `data/fixtures.py:641` `stock_report="crossing"`; row H-243 CLOSED (part 8). Session `P:07_SE_treasury_granary_B` (B12) builds on it. | — |
| M18 | which reading of PP-624 (thread pool) | DONE-IN-CODE | CR-85/ED-IN-0330 removed the history term: `systems/threadwork/sim/operations.py:239-241` ("`.history` is no longer read"); `T:test_cr85_faculty_replaces_history.py`. The question is dissolved by deletion (v11's own note). | — |
| M19 | decline wrong-kind acts at formation | DONE-IN-CODE | `verb_table.yaml` carries 62 `referent_class` lines; `T:test_cr28_propositions_heard.py` (CR-28). Session `P:08_FI_01_claim-sourced-referents` (B11) and `P:14_VERBS_SOCIAL2_A_formation_on_what_is_known` (B25) extend the same shape. | — |
| M20 | typed ladder of stages beneath an ambition | DONE-IN-CODE | `goals.yaml:38` `goal_stages:` loader; `T:test_cl_thrust_b2_schema.py`, `T:test_cl_thrust_b31_current_stage.py`, `T:test_cl_thrust_b32.py` (the released pieces B0.1, B2.x, B3.1, B3.2). The held pieces (B4.x, B5.2, B6.n) are CL-THRUST positions (E5). Session `P:12_ARCS_arcs_as_staged_goals` (B10) writes the stage rows and A-47 restates threshold-closed arcs as "threshold opens a scene". | — |
| M21 | is a beaten fighter killed outright (`Slain` band) | DONE-IN-CODE | `grep Slain engine/season` = 0 files; `Felled` is death (decision (a)). Session `P:22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` (B37) makes deaths rare by a draw at `mortal_terms` without a new band (its `Felled` mentions: not read beyond the head); A-31 (damage scale) does not touch it. [ASSUMPTION: no session proposal adds a `Slain` band — basis: grep 0 in engine and none named in U3 §2.1.] | — |
| M22 | troop counts (M3's yes arm) | SUPERSEDED | A-2; same as M3. | — |
| M23 | the attribute list | DONE-IN-CODE | Ten keys: `references/descriptor_registry.yaml:47` `attr.mind.will` Spirit (Jordan's ten, ED-IN-0328). A-98: "aptitude is an attribute"; the suite's words are attribute and skill. | — |
| M24 | the training rule (`max`) | SUPERSEDED | A-98 ("training names only the act of learning ... never the rank"; one capability kind, skill) with A-7 (two inputs): `P:U5a_capability_home_and_two_inputs` (B04) and `P:02_CHAR_capability_definitions` (B04) replace CR-20's `max` of held key and vocation attribute. [head only] | — |
| M25 | who owns a sword (no kit carrier) | SUPERSEDED | `P:03_PC_loadout_and_carry` (B18) and `P:04_MB_unit_loadout_and_weapon_in_hand` (B17) give a loadout carrier; `T:test_cp_t03_03_kit.py` is the interim arms-kind reader they replace. [head only] | — |
| M26 | storyline form (no story pools; arcs never runtime data) | SUPERSEDED | `P:09_WR_provided_arcs` (B12) and `P:12_ARCS_arcs_as_staged_goals` (B10) with A-47 carry the arc form; the Tensions receiver goes with M16. [head only: `09_WR_provided_arcs` not read beyond its title and batch.] | — |
| M27 | mass-battle command | SUPERSEDED | A-59 (command is a draw from a learned skill plus attributes; each unit carries its own prowess) = `P:27_MB_A_command_and_the_obedience_draw` (B19), `P:27_MB_D_the_commander_as_chooser` (B20), `P:26_MASS_BATTLE_maneuver_orders` (B20). | — |
| M28 | founding in play | SUPERSEDED | A-55 (fixed map; a founded household may lapse) = `P:23_STORY_C_a_founded_place_can_fail` (B39); the default "no settlement is founded in play" is replaced. | — |
| M29 | mayor seats | SUPERSEDED | A-44 (cast of about 94 plus kin) = `P:21_PROCEDURAL_B_cast_and_seats` (B39) authors seats. [head only] | — |
| M30 | a world Thread substrate | SUPERSEDED | A-40 (the Thread is ground, a real condition of places; one site per territory) contradicts the default "no world-level Thread condition": `P:09_WR_world_motion` edit 1 (B12), `P:12_ARCS_substrate_as_ground` (B35). | — |
| M31 | the management surface | DONE-IN-CODE | Default = none; the player acts only through the seated person (AX-1). A-48 (the scene slate) is a read surface, `P:11_GO_player_surface_contract_B` (B34); no management verb is added. | — |
| M32 | odds shown for non-combat acts | DONE-IN-CODE | `T:test_odds_of.py`; `odds_of` mode (a). Session `P:10_DICE_believed_odds_have_a_prior` (B05) adds a prior; extends. | — |
| M33 | what the console may show | DONE-IN-CODE | Ratified `04` §C.11; `P:11_GO_player_surface_contract` §2 (`explain`, live; B34) obeys it. | — |
| M34 | `selfish_selfless` at spread 0 | DONE-IN-CODE | As shipped (no stored offset); A-34 (self-knowledge a belief, built narrowly) adds a belief, not an offset: `P:U5a_CHAR_self_knowledge_is_a_belief` (B10). | — |
| M35 | tau against trait spreads | DONE-IN-CODE | `data/fixtures.py:321` `choice_temperature=0.05` after CR-17's rule. `P:02_CHAR_resolve_and_temper` is "evidence for M35 and M40". | — |
| M36 | per-verb declared cells | DONE-IN-CODE | None added; `verb_table.yaml` as shipped. | — |
| M37 | the refusal gate's convention | DONE-IN-CODE | `data/fixtures.py:862` `refusal_axis=None`. | — |
| M38 | PR #527's RJ-calls, its two Layer 1 hunks, the marquis question | STILL-NEEDED | The default is "CR-38 as written until #527 merges; canon's count and countess stand". Whether #527 merged: not found in the tree or the suite [ASSUMPTION: unmerged — basis: no `RJ-` hit in `engine/` or `registers/`]. CR-38 (Court Parliament design) is E5's; A-76 ("any working realm bench stands in now, built switchable" until the Court Parliament exists) gives it an interim, so this row only keeps the marquis rule. | IN/FA, batch B21 or B32 (no new batch); edit set: none beyond CR-38; gate: n/a (a standing rule: no marquis in canon). Block 2. |
| M39 | the motion source (RJ-11/RM2) | DONE-IN-CODE | Default = none in computed play (a motion is hand-built; CR-37 unbuilt). | — |
| M40 | ED-IN-0304's undecided residue (CR-17 follow-on; CL-PERSON HELD) | DONE-IN-CODE | Default = unbuilt and undesigned. `P:02_CHAR_resolve_and_temper` states it "does not pre-empt CL-PERSON, which is HELD on a ruled sentence". The held position is E5's. | — |
| §1a-M11 | Jordan's answer: D-1 stands | DONE-IN-CODE | As M11. | — |
| §1a-J-T2 | the tenth attribute | DONE-IN-CODE | As M2/M23 (Jordan's ten). | — |
| §1a-doctrine | zero both `doctrine` cells or keep | DONE-IN-CODE | Confirmed at the default (both as shipped): `rosters.yaml` carries the `doctrine` row; `T:test_cr21_cells.py`. | — |
| §1a-M1res | foreign march frequency; `foreign`/`guards` defaults | STILL-NEEDED | `foreign=True` ships (`harness/populated.py:1015`); `guards` ships off (`:1015` signature, `inspect` per `audits/25` L-08: `guards` False). The casus-belli gate (CR-91) is unbuilt and the cap of one march per season per territory is IN-36's (E5); A-58 and A-74 revise the casus-belli half (see M10). Only the cap and `guards`-ON-after-CP-T09-07(b) survive. | FA, batch B21/B23; edit set `harness/populated.py::build_realm` (`guards`), the march-per-territory cap in `loop/sides.py`; gate: `T:test_in36_foreign.py` extended: no territory receives two marches in one season; moves hashes: yes (declared mover); tier sonnet. Block 3. |
| §1a-M3 | amend `04:793/:802` for counted troop stock | SUPERSEDED | A-2; as M3. | — |
| §1a-M4opt | Ask C (b) earlier-round fields; Ask B (d) captives into custody | DONE-IN-CODE | Defaults hold: same-round fields (`loop/encounter.py`), no custody write; `T:test_cp_t03_09_capture.py` is `capture` as a verb, not a field write. Session A-96 (a failed attempt on a guarded target: detained) does not touch fields. | — |
| §1a-M16-4th | a fourth motion (actorless political event) | DONE-IN-CODE | Default no; A-50 world cards write only starting state at build (a generation draw, not a runtime motion). | — |
| §1a-Tc | amend T-c to admit R3' pulse and the stage `deadline` | DONE-IN-CODE | Default excluded; `goals.yaml:38-40` refuses stray keys. A-80/A-81 (entrenchment moves the world; scenes never leave stillness) are met by pressure that compounds from acts (`P:28_CORE_scene_access_C_the_petition_that_waits`), not by a stage deadline. | — |
| §1a-(a) | the five heritage members | DONE-IN-CODE | `state/carriers.py:826` `heritage: Optional[str]`; `T:test_cr30_heritage.py`, `T:test_cr31_heritage_regard.py`. A-87 to A-90 add caste and opinion rows as data under the conviction roster; extends. | — |
| §1a-(b) | the Cardinal electorate rule | DONE-IN-CODE | `state/gate.py:697` `FILLED_BY`; `T:test_cr34_declared_disposal.py`. `P:15_INSTITUTIONS_PAPACY_B_patronage_election_discipline` (B32) states "the electorate in force is two seats of one arm ... `quorum: 2`": the session keeps the rule. | — |
| §1a-(c) | GD-3 and emerged creeds | STILL-NEEDED | IN-30 (`faction_props`) is unbuilt (`grep faction_props` 0); H-186 records the GD-3 FAIL. Closure: `CL:U5d` H-176/H-186 RESOLVED-BY `P:09_WR_world_motion` edit 2 ("MOTION edit 2"); the session does not rule on whether a seat may serve an emerged creed. [ASSUMPTION: edit 2 of `09_WR_world_motion` replaces the streak/contiguity triggers only — basis: `CL:U5d` row names it for "insurgency"; proposal body not opened.] | FA/WR, batch B12 (with `09_WR_world_motion`); edit set `queries/faction_q.py` (`faction_props`), `data/rosters.py` faction Propositions; gate: a hand-built creed commit makes an emerged faction readable and its `seize` is refused with the GD-3 FAIL named; hash EQUAL; tier opus. Block 4. |
| §1a-(d) | merge the held-back Layer 0/1 PR | DONE-IN-CODE | Applied in PR #507 (ED-IN-0300/0301); `CLAUDE.md` shows H-L0-6 (no `mc_v18`). | — |
| §1b-1 | what belongs on a Person (heritage field; faction, rank, office derived) | DONE-IN-CODE | CR-30, CR-31, CR-33 landed: `T:test_cr30_heritage.py`, `T:test_cr31_heritage_regard.py`, `T:test_cr33_lifepaths.py`. CR-32 (`ladders:` in `offices.yaml`): `grep '^ladders:'` 0, not built; it is H-181's row below. A-41/A-42 (caste: regard, vote blocks, informal tiers) extend. | — |
| §1b-2 | something that happens without the player (Tensions receiver, arcs rule) | SUPERSEDED | As M16 and M26: A-50, A-54, `P:21_PROCEDURAL_D_world_cards_and_churn` (B39), `P:09_WR_provided_arcs` (B12). | — |
| §1b-3 | widen succession and revocation (election, nomination, contested succession, joint-concurrence deposition) | STILL-NEEDED | Partly landed: `state/gate.py:697` `FILLED_BY` (CR-35 arm), `T:test_in61_succession.py`, `T:test_cr25_computed_establish.py`; unbuilt: CR-36 (nominated seats) and CR-37 (`grep joint_concurrence` 0). Session amends: `P:06_FA_seat_terms_by_body_B` (A-35, A-36), `P:22_HAPPENINGS_B_the_throne_is_never_stranded` (A-19), `P:14_VERBS_BINDING_C_turnover` (B21). The unbuilt remainder is CR-36/CR-37 (E-lane positions); this row keeps the decision record. | FA, B21; as M8 (Block 1) plus CR-36's `nominated` basis; gate: `confer` on a body's carried `resolution` fills a `nominated` seat in a hand-built world; hash EQUAL. Block 1 (shared). |
| §1b-4 | make the endings reachable | SUPERSEDED | `CL:U5d` row "H-176, H-186, H-235, H-236 | endings; insurgency; the lattice | RESOLVED-BY | MOTION edits 3, 2, 1" = `P:09_WR_world_motion` (B12), with `P:09_WR_provided_arcs` (B12). IN-30's `faction_props` rides §1a-(c). | — |
| §1b-5 | translate board-game aggregates (five forms, eight refusals) | DONE-IN-CODE | The refusals are rules for authors, not data; their one code consequence is CR-34: `T:test_cr34_declared_disposal.py` (`quorum: 2`, live-commit tally). A-14 (a vote is a draw on the voter inside the presiding act) is extended by `P:15_INSTITUTIONS_PAPACY_B_patronage_election_discipline`, which "carries at the pass mark" the same tally. | — |
| §1b-6 | reconcile the sources (ministries, Prosperity, `PI`, arc ids, faction count) | DONE-IN-CODE | CR-40 to CR-44 are editorial; the faction count is not pinned (`engine/substrate/names.py` quote in v11). `[ASSUMPTION: edited — basis: v11 says each is hash EQUAL and CR-41..44 land in one IN pass; I did not re-open the five sites.]` | — |
| §1d | the strife fold: nothing queued | DONE-IN-CODE | `T:test_strife_flows.py`, `T:test_strife_kinds.py`, `T:test_strife_execution.py` exist; `harness/strife.py`. | — |

## Table 2 — part 7 §1: A1 (88 asks)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| A1-01 | newborn Record a `founding` basis: NO | DONE-IN-CODE | Jordan's ruling in the last ED-IN-0292 row (`registers/editorial_ledger_in.jsonl`); `04` §C.2 unchanged; A-75 (births on) mints persons, not a founding Record. | — |
| A1-02 | a vacancy reaches a person as a claim | DONE-IN-CODE | `T:test_in61_heir_hears_vacancy.py`, `T:test_in53_vacancy_need.py`; the session adopts the decision unchanged and generalises it in `P:08_FI_01_claim-sourced-referents` (B11: "builds a decision already recorded as taken ... A1-02"). | — |
| A1-03 | how much goals, stance and loyalty decide acts | DONE-IN-CODE | As M1. | — |
| A1-04 | cohorts get pursuits, convictions, spread | DONE-IN-CODE | `cohorts.yaml:145` `temperaments:`; spread at weight 2 has no subject (A2-41). A-91(3) wants cohort convictions able to move: `P:31_WR_B_the_revival_gathers` (extends). | — |
| A1-05 | own-act screen spares tier-1 claims (arm D2) | STILL-NEEDED | The screen exists (ED-IN-0294, `T:test_in57_attention_tiers.py`); `grep own_act` in `decision/`, `loop/` finds none: the D2 arm is CR-10 (E-lane), unbuilt. `CL:U5a` H-233 maps "goal lean; reason trail", not the screen. | IN, B10; edit set `queries/world_q.py` attention tiers (`own_purview` is at `:1080`); gate: a 3-seed reading (R3 figures) with tier-1 echoes spared; moves hashes: yes; tier sonnet. Block 5. |
| A1-06 | where a works comes from | DONE-IN-CODE | As M5. | — |
| A1-07 | sixth §C.6 channel row | DONE-IN-CODE | Closed by D-1 and A-97; the channel build is CR-29 (rows H-214, H-234, A2-43). | — |
| A1-08 | `reception`/`proofs` source: commits (option B) | DONE-IN-CODE | `T:test_sc02_reception.py`, `T:test_sc02_22b_standing_crossing.py`; `04` B.2's F8 row stands. | — |
| A1-09 | ED-IN-0293 has no own question | DONE-IN-CODE | Ledger row (`editorial_ledger_in.jsonl`); successors A1-10, A1-04. | — |
| A1-10 | B-X's design decisions (ED-IN-0295) | DONE-IN-CODE | Built at IN-64: `T:test_in64_cast_integration.py`, `T:test_in66_goals_loader.py`, `T:test_in68_goal_seeding.py`. | — |
| A1-11 | ED-FA-0039 goal content | DONE-IN-CODE | `goals.yaml`; `T:test_fa06_org_goals.py`. | — |
| A1-12 | refused inquiry deposits `finding.none`? | DONE-IN-CODE | `rosters.yaml: undeposited_kinds` = `[finding.none]` (`audits/25` G-15, VERIFIED-CORRECTED). | — |
| A1-13 | ED-914 / PP-719 | DONE-IN-CODE | No ask; PP vocabulary frozen. | — |
| A1-14 | ED-IN-0261 close condition | DONE-IN-CODE | `rosters.yaml` `doctrine` row; `T:test_in08_cells.py`. | — |
| A1-15 | source of per-person capability | DONE-IN-CODE | As M2. | — |
| A1-16a | three magnitudes at 0: scar shift, confliction weight | DONE-IN-CODE | `data/fixtures.py:834` `scar_weight_shift=0`, `:842` `confliction_weight=0`. | — |
| A1-16b | ageing and illness rates at 0 | SUPERSEDED | A-15 (natural death ON after the 46 ages are authored, behind an authored rate) = `P:22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn` edit 1 (B37), `P:16_PESSIMIST_WR_C_illness_on_the_body_ladder` (B37). Tree: `data/fixtures.py:690-691` `age_step=0.0`, `illness_rate=0.0` (`audits/25` L-22). | — |
| A1-17 | weight-to-troop value (REM-32) | DONE-IN-CODE | `T:test_rem32_scale.py`. The session's `P:04_MB_headcount_grade_and_scale` (B17) sets "one scale" over it; extends. | — |
| A1-18 | ratify IN-46/IN-47 designs | DONE-IN-CODE | `T:test_rem30_character_sheet.py`, `T:test_rem31_grid_suspension.py`. | — |
| A1-19 | which magnitude makes hunger bind | DONE-IN-CODE | As M6. | — |
| A1-20 | D-1; `Sensation.subsistence` | DONE-IN-CODE | REM-44 landed (v11 row H-73 CLOSED: `urgency`, `benefits_me`, `Sensation.subsistence` deleted); [ASSUMPTION: verified by absence — basis: `grep subsistence engine/season/decision` not run; v11 H-73 cell is the source]. | — |
| A1-21 | verb roster 46 or 92 | DONE-IN-CODE | The tree's roster is the code's: 67 rows (`audits/25` L-12), not the 56 v11 writes; A-28 (tie/knot split) takes it to 68 = `P:14_VERBS_SOCIAL2_D_tie` (B24). | — |
| A1-22 | eight handoff rules | DONE-IN-CODE | R-04's `met` reads no handoff (v11); no change. | — |
| A1-23 | THE BAR's ordering | SUPERSEDED | `P:23_STORY_D_story_census_and_gate` and `P:09_WR_story_instruments_that_can_fail` (B36) carry the M2 story gate; `T:test_sc01_the_bar.py` is SC-01's bar, a different thing. [head only] | — |
| A1-24 | FI-03 trail reachable only by a plant | SUPERSEDED | `P:08_FI_03_playable-inquiry` (B11) makes the inquiry playable; `T:test_fi03_trail.py` is the red-on-purpose test it retires. [head only] | — |
| A1-25 | build `explain(p, v)` | SUPERSEDED | `P:11_GO_player_surface_contract` §2 (`explain`, "live, lands in B34") supplies the first reader v11 required. | — |
| A1-26 | move R-01/R-02 narrative out of `requirements.yaml` | SUPERSEDED | `P:01_CORE_requirements_reading_record` (B02) adds the `reading:` record; A-97/IS_A_NINE carry the register reading. | — |
| A1-27 | delete `params_tables.yaml` | DONE-IN-CODE | `engine/engine_params/params_tables.yaml` does not exist (`ls`); `CLAUDE.md` §5 says retired. | — |
| A1-28 | move `build_realm` out of `harness/` | DONE-IN-CODE | Declined (no module owns world-gen); still at `harness/populated.py`. Session `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` H-04 touches its parameters, not its home. | — |
| A1-29 | loader invariant 5 (`writer:` column) | DONE-IN-CODE | `04` B.13 decides it as agent work; no R-row reads it. | — |
| A1-30 | H-185, H-191 unread | DONE-IN-CODE | `CL:U5a`: H-191 "STALE-FALSE-POSITIVE (as findings) ... carried"; nothing builds them. | — |
| A1-31 | pursuit-scar writes read by nothing | DONE-IN-CODE | As A1-16a. | — |
| A1-32 | value term reads the verb only | SUPERSEDED | `P:02_CHAR_choice_alignment` (B10): "alignment cells on `choice_sourced` values" widens what the term reads (the shape stays; the weighting is open per §F2). | — |
| A1-33 | `faction_q.at_war` has no reader | SUPERSEDED | A-20 (war lives in the seats that wage it): `P:06_FA_war_lives_in_seats_B` (B23) gives it readers. | — |
| A1-34 | actor's own deposit unrefracted | DONE-IN-CODE | AX-7 permits it; A-34 adds a belief about self, not a refraction: `P:U5a_CHAR_self_knowledge_is_a_belief` (B10). | — |
| A1-35 | non-monotone P(Partial+) on the equal-score diagonal | SUPERSEDED | A-26 reopens and overrides the half-score ruling (`roll.py` `score/2`): 0.4 per point; A-71, A-79 = `P:29_DICE_one_opposed_rule_form_and_tuning` (B05), `P:05_SC_opposed_obstacle_parity` (B05). | — |
| A1-36 | `restore`'s `NoOpReceipt` | DONE-IN-CODE | Lawful refusal (`04` C.4); A-62 amends the receipt shape (no changes list on a refusal; text applied under A-97). | — |
| A1-37 | `tell`'s `with` = UNKNOWN | DONE-IN-CODE | `data/requires.py:808` (v11 re-opened); no session change. | — |
| A1-38 | ED-IN-0261 self/other weighting | DONE-IN-CODE | Consumer chain deleted by REM-44. | — |
| A1-39 | move 1,017 ED rows | DONE-IN-CODE | Declined (`CLAUDE.md` §0.1 pt 5); nothing owed. | — |
| A1-40 | retire process checks | DONE-IN-CODE | Declined (request is the scope); nothing owed. | — |
| A1-41 | delete `_drop_what_was_already_done` | DONE-IN-CODE | `loop/deliberate.py` still carries it (comment at `:222`); `P:16_PESSIMIST_CORE_no_stored_plan` (B03) deletes a different branch (queue reuse), not this guard. | — |
| A1-42 | all-zero cohort score field vs R-08 | DONE-IN-CODE | G-1 precedent; no change. | — |
| A1-43 | gate `chronicle`'s deletion | DONE-IN-CODE | `chronicle` is kept (`T:test_in37_chronicle.py`); the paired reach channel is CR-29 (row H-214). | — |
| A1-44 | does Jordan rule Godot 4.6 | WRONG | ED-GO-0002 is ruled and is 4.7 (see M13). | — |
| A1-45 | which module owns the proceedings verbs | DONE-IN-CODE | Verbs are host rows in `verb_table.yaml`; A-10 (the loop's own verbs; no governance module). | — |
| A1-46 | cut the inert `scale:` column | STILL-NEEDED | `verb_table.yaml` still carries `scale:` on 15 rows (`grep`); CR-07 unbuilt. `CL:U5a` H-89: "RESOLVED-BY workplan CR-07 ... with the precondition and Layer-1 ground in `U5a_CORE_owed_edits.md` §E row 3" (opened): give seat `off_npc_084` a scope first; re-run CR-07's pre-flight. The session adds the precondition only. | IN, B03 (`U5a_CORE_owed_edits` §E 3); edit set `verb_table.yaml`, `data/verbs.py` (`VerbRow.scale`, load check, `:129-137, :619-621`), `tests`; gate: `grep -n "scale:" engine/season/verb_table.yaml` finds none and a planted `scale:` key fails the load naming the row; hash EQUAL; tier sonnet. Block 6. |
| A1-47 | may a seam run a nested DELIBERATE | SUPERSEDED | A-4 (a duel is called from inside the battle as a nested contest) and A-72 (a battle may call one duel round; a duel round calls nothing) replace the flat "No": `P:04_MB_squad_grid_of_named_characters` (B30), `P:03_PC_duel_round_and_approach_B` step 5. The "No" still holds for a seam running a whole DELIBERATE. | — |
| A1-48 | common-fact store vs channels | DONE-IN-CODE | No store exists; channels are the ledger. (v11's flag stands: Jordan excluded the store from RS-29's ratification; the session did not rule.) | — |
| A1-49 | re-band `degree_from_net` | DONE-IN-CODE | One ladder; A-5, A-8, A-79 keep it (`engine/dice_engine/dice_engine.py:227`). | — |
| A1-50 | IN-14: more rounds | STILL-NEEDED | `loop/driver.py:479` `rounds = int(w.fixtures.get("scene_budget"))`: the ceiling is live. `CL:U5a` H-10: "RESOLVED-BY F-CORE-06's carrier (IN-14)". A-9 (a turn is a short sequence; B08) changes scene order, not the round count. | IN, B08 or B16 (after `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order`); edit set `loop/driver.py`, `decision/budget.py`; gate: `T:test_season_shape.py` `test_n3` floor re-taken before and after; moves hashes: yes; tier sonnet. Block 7. |
| A1-51 | cell-value pass | DONE-IN-CODE | As M14. | — |
| A1-52 | IN-52: troops bounded; flip ON | SUPERSEDED | `P:16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate` edit 4 (the flip's load-time refusal) and `P:07_SE_campaign_supply_and_muster` (B22); `CL:U5d` H-241 "RESOLVED-BY SUPPLY". `data/fixtures.py:809` `field_provisioning=False`. | — |
| A1-53 | `dispatch` a generic remit act | DONE-IN-CODE | `remit_default` fixture; no session change. | — |
| A1-54 | which posts hold `dispatch` | SUPERSEDED | A-22 (a seat orders its sworn men, holders of seats it may revoke, and the unseated in its land) and `P:06_FA_remit_grant_by_row` (B21) fix remit by row; A-44 authors the posts. [head only] | — |
| A1-55 | unwatched fights: one act or span scenes | SUPERSEDED | A-1 (auto-resolve = the same resolver on standing orders) and A-4: `P:03_PC_duel_round_and_approach` (B16), `P:04_MB_manager_battle_one_resolver` (B20). | — |
| A1-56 | sentence `oblige` vs service `oblige` | DONE-IN-CODE | Delegated ruling shipped; A-37 (an imposed service ends by pardon or term) is a rule on top, `P:05_SC_arrangement_rows_that_bind` (B27). | — |
| A1-57 | jurisdiction follows presence | DONE-IN-CODE | `state/gate.py` `may_determine` clause 3 (`home_of`). | — |
| A1-58 | adopt the SC kernel as automated mode | SUPERSEDED | `P:05_SC_sc05_kernel_disposition_B` and `P:05_SC_sc05_kernel_retirement` (B24). [head only] | — |
| A1-59 | cavalry recoil | DONE-IN-CODE | No season field fields cavalry; A-60 keeps melee linear. | — |
| A1-60 | NPC-lane overlays (RS-21 item 2) | DONE-IN-CODE | Adopted; overlays authored where sourced. | — |
| A1-61 | ending vocabulary a Query over holds and seats | DONE-IN-CODE | `rosters.yaml: endings`; `T:test_in27_endings.py`. | — |
| A1-62 | one foreign faction, two seats | DONE-IN-CODE | `T:test_in36_foreign.py`; `foreign=True`. | — |
| A1-63 | ageing and illness in scope, rates swept | SUPERSEDED | A-15 arms them; as A1-16b. | — |
| A1-64 | cap support at weapon reach (J-18) | DONE-IN-CODE | MB-07r closed (v11 state index). [ASSUMPTION: not re-probed — basis: v11 §4.] | — |
| A1-65 | delete dead off-hand branch (J-20) | DONE-IN-CODE | ED-PC-0055 `resolved`. | — |
| A1-66 | katana flip asymmetry (J-21) | DONE-IN-CODE | ED-PC-0051 `resolved`. | — |
| A1-67 | `inheritance` basis; heir's claim | DONE-IN-CODE | `T:test_in61_succession.py`. | — |
| A1-68 | `pool_default` interim | DONE-IN-CODE | `data/fixtures.py` `pool_default`; M2. | — |
| A1-69 | candidate cell drafts | DONE-IN-CODE | RS-1 (ED-IN-0291). | — |
| A1-70 | Calamity class and baseline sign | SUPERSEDED | `P:16_PESSIMIST_WR_B_the_calamity_strains_and_breaks` (B12) edits 1-2 and `P:09_WR_world_motion` edit 1; A-40, A-54. [head only] | — |
| A1-71 | H-235/H-236 owner line | SUPERSEDED | As A1-70 (`CL:U5d`: "H-176, H-186, H-235, H-236 ... MOTION edits 3, 2, 1"). | — |
| A1-72 | grid/map variant a mode of one module | DONE-IN-CODE | `T:test_rem31_grid_suspension.py`. | — |
| A1-73 | vassalage derived, never stored | DONE-IN-CODE | `state/gate.py:353` `purview_reaches` `oblige` clause. | — |
| A1-74 | `decision_policy_v1.md` | DONE-IN-CODE | Quarantined; nothing reads it. | — |
| A1-75 | PR #450 deletions | DONE-IN-CODE | No; stays deleted. | — |
| A1-76 | governance-corpus rebuild | DONE-IN-CODE | No subject. | — |
| A1-77 | stale-text edits to `CLAUDE.md`, `CURRENT.md`, `architecture/` (IN-44) | SUPERSEDED | `P:U5a_CORE_owed_edits` (B03), `P:11_GO_pointer_and_stale_text_resolutions` (B03), `P:09_WR_B_pointer_text_for_the_orchestrator` (B03) and A-97 (apply every owed Layer 1 amendment). [head only] | — |
| A1-78 | `mc_v18` bullet | DONE-IN-CODE | As M15. | — |
| A1-79 | holonic `decision/` vs host | DONE-IN-CODE | A-25 later governs; A-10. | — |
| A1-80 | `RemoteTrigger` a self-scheduling primitive | STILL-NEEDED | `grep RemoteTrigger tests/valoria/test_no_polling_triggers.py .claude/settings.json` finds nothing; v11 made the add conditional on first observing that it arms a routine, which was never done, and the edit is Jordan's (settings). `CLAUDE.md` §11 says to add a primitive when observed. | IN; no batch (a Jordan-approved settings change); gate: `tests/valoria/test_no_polling_triggers.py` `REQUIRED_DENY` includes it after the observation; moves hashes: no; needs Jordan's approval. Block 8. |
| A1-81 | re-word `succeed` designation nodes to the title route | STILL-NEEDED | IN-61 landed (`T:test_in61_succession.py`); whether the `04` nodes still say `founding` was not opened. [UNVERIFIED] A-97 licenses the edit; the amendments list (`U3_LAYER1_AMENDMENTS.md`) does not name it. | IN, B03; edit set `architecture/meta/04_CODE_ARCHITECTURE.md` heir nodes; gate: `grep -n founding` on the nodes reads the title route; hash EQUAL; tier haiku. Block 8. |
| A1-82 | `Rung.envelope` unwritten field | DONE-IN-CODE | Kept (`audits/25` V-03); the writer is `P:07_SE_population_regrowth_B` (B12) as part of CR-08. | — |
| A1-83 | H-198 deception | DONE-IN-CODE | As M9. | — |
| A1-84 | H-212 occupation's larder effect | SUPERSEDED | A-66 (occupy without seizing is a recognised state) with `P:07_SE_campaign_supply_and_muster` (B22); `CL:U5b` "H-147, H-212, ... closed in Part 2 (MB)". | — |
| A1-85 | H-219 failure severity | SUPERSEDED | A-81 (every graded band has a durable write) with `P:05_SC_arrangement_rows_that_bind` (B27), `P:U5c_FI_residue` (B11); `CL:U5c` names H-219. | — |
| A1-86 | H-221 failure arm | SUPERSEDED | `P:16_PESSIMIST_SC_D_an_argument_moves_someone` (B27); `CL:U5a` "res. 8 Failure moves the arguer ... RESOLVED-BY PES-D | H-221 intent". | — |
| A1-87 | H-222 person-predicate claim writer | STILL-NEEDED | `T:test_sc02_22b_standing_crossing.py` exists (the crossing reader) but v11's row says no deposit mints a `person_predicates` claim; `CL:U5c` places H-222 under `P:17_CENSUS_REST_3_corrections` only as a filed correction. Writer not found in `loop/witness.py` (grep). [UNVERIFIED: writer absence — basis: grep of two files only] | SC, B27 (with `16_PESSIMIST_SC_B_one_reader_of_a_ledger`); edit set `loop/witness.py` (a deposit of person-predicate claims through the channels); gate: `standing_of` non-constant in a seeded realm and a standing-band crossing occurs; moves hashes: yes; tier opus. Block 9. |
| A1-88 | H-228 re-homing after `raze` | DONE-IN-CODE | Layer 1 §B.8 cascade; `CL:U5b`: "re-homing stays out; the displaced recover by `migrate`". `T:test_in12_raze.py`. A-73 (the taker may raze while it is in his hand) rewrites the occupier's licence: `P:14_VERBS_PHYSICAL_B_field_and_ruin` (B22). | — |

## Table 3 — part 7 §2: A2 (59 asks)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| A2-01 | believed chance in the NPC score (AQ-X1) | DONE-IN-CODE | As M1 (`odds_weighting="believed"`); `P:10_DICE_believed_odds_have_a_prior` (B05) adds a prior. | — |
| A2-02 | which ties carry a line past death | DONE-IN-CODE | As M7. | — |
| A2-03 | what a raised troop is (Ask A) | SUPERSEDED | A-2 and `P:14_VERBS_MILITARY_C_the_muster`; as M3. | — |
| A2-04 | what a fought field writes (Ask B) | DONE-IN-CODE | As M4. | — |
| A2-05 | fields declared in an earlier round (Ask C) | DONE-IN-CODE | As M4 (same-round stands). | — |
| A2-06 | do "pool only" constraints bind combat and mass battle | DONE-IN-CODE | As M2; A-5/A-6/A-7 route every contest through one pool rule: `P:10_DICE_one_score_two_roles` (B05). | — |
| A2-07 | may a holder burn a Record (`destroy_record`) | DONE-IN-CODE | `withheld_verbs` fixture ships `("destroy_record",)` (`grep` 12 files); CP-T06-08 stays parked. | — |
| A2-08 | what a person becomes at the latch | SUPERSEDED | A-43 (zero coherence: seats and goals kept; the person becomes unknowable to others) = `P:U5d_WR_zero_coherence_unknowable` (B35); the either-or of v11 is replaced. | — |
| A2-09 | who may declare war | DONE-IN-CODE | `verb_table.yaml` `capture` `eligibility: ["remit:dispatch"]`; `march` and `raze` gate on `remit:dispatch`. A-20/A-22 refine who commands in `P:06_FA_war_lives_in_seats_B` (B23); extends. | — |
| A2-10 | T03's "no new ask" holds | DONE-IN-CODE | A verification note; nothing owed. | — |
| A2-11 | T05's "no new ask" holds | DONE-IN-CODE | Same. | — |
| A2-12 | T08's "no new ask" holds | DONE-IN-CODE | Same. | — |
| A2-13 | T10's "no new ask" holds | DONE-IN-CODE | Same; births now ruled by A-75 (see A2-15). | — |
| A2-14 | remove a living top-seat holder (D-V1) | STILL-NEEDED | As M8 (Block 1). | FA, B21; Block 1. |
| A2-15 | births exist? (ED-WR-0011: the 46 only, "return much later") | SUPERSEDED | Jordan has returned to it: A-75 (named births on, behind `birth_rate`), A-44 (cast of about 94 plus kin, capped), A-15 (ages) = `P:21_PROCEDURAL_B_cast_and_seats`, `P:23_STORY_B_a_house_continues` (B39). | — |
| A2-16 | channel after `chronicle`'s deletion | DONE-IN-CODE | As A1-43. | — |
| A2-17 | may persons lie | DONE-IN-CODE | As M9. | — |
| A2-18 | withdrawn vs routed army | DONE-IN-CODE | `modules/mass_battle/hierarchy/units.py` `MB_YIELD_POCKET`, `orchestration.py` `MB_YIELD_RALLY`; `T:test_cp_t04_03_retreat.py`. A-61 (rout floor) and `P:16_PESSIMIST_MB_rout_has_two_exits` (B19) extend. | — |
| A2-19 | NPC score gain a contents-aware term | DONE-IN-CODE | Verb-keyed alignment shipped (M1); `P:02_CHAR_choice_alignment` (B10) extends to choice values. | — |
| A2-20 | keep the name `dispatch` | DONE-IN-CODE | `verb_table.yaml` has `dispatch`; ED-IN-0210 (ruled) stands. | — |
| A2-21 | field force with the march (D-V8) | SUPERSEDED | As M3. | — |
| A2-22 | march requires a declared war | SUPERSEDED | As M10. | — |
| A2-23 | a treaty binds the signer or the seat | STILL-NEEDED | The decision (signer; a successor re-seals) is a spec for the treaty edge (CP-T09-03, unbuilt: no treaty reader in the tree). The session's war-seats files say nothing about treaty signers (`grep treaty` finds it only in `15_INSTITUTIONS_COLONIAL_*`, `SYNTHESIS_E`); A-20 puts war-ending in the seats, so this may read differently [UNVERIFIED: did not open `14_VERBS_BINDING_E_war_seats` body]. | FA, B23 (`14_VERBS_BINDING_E_war_seats`); edit set the treaty edge in `loop/effects_governance.py`; gate: a hand-built treaty lapses when the signer dies and a successor re-seals; hash EQUAL (unbuilt verb); tier opus. Block 10. |
| A2-24 | = A2-09 | DONE-IN-CODE | As A2-09. | — |
| A2-25 | a won contest opens an edge the counterparty owns | DONE-IN-CODE | `verb_table.yaml:1067` (`determine` opens an `oblige` owned by the bound party). | — |
| A2-26 | who eats, in what order, under scarcity | SUPERSEDED | `P:07_SE_ground_and_granaries` (B12: "the remainder walk") and `P:16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted` (B12) replace host-pid order; `modules/settlements/larder.py` is the owner they edit. | — |
| A2-27 | road cost: Calamity only, or weather too | SUPERSEDED | `P:09_WR_B_weather_with_memory_and_the_year` edit 3 ("a journey priced before it is chosen", B12) prices weather into the road; the v11 answer ("Calamity only") is replaced. | — |
| A2-28 | between places (amend `contain`) | DONE-IN-CODE | Layer 1 `04:240` stands; nothing proposes the amendment. | — |
| A2-29 | how a questioned person answers an `interview` | DONE-IN-CODE | Option (b), own act next season; `P:14_VERBS_SOCIAL2_C_case_question_confession` (B25) keeps AX-2. | — |
| A2-30 | `guard` Tenure kind; seatless custody | DONE-IN-CODE | `T:test_cp_t03_09_capture.py`; A-23 (custody suspends acts through the seat), A-96 (guard's `capture` on a failed attempt) use the same seat custody. | — |
| A2-31 | unpaid upkeep: lapse or debt | DONE-IN-CODE | Lapse (term matures): `T:test_term_upkeep.py`. | — |
| A2-32 | Coherence's elastic return | DONE-IN-CODE | Decision (read-time projection) stands; its build CP-T07-06 is E5's. | — |
| A2-33 | are knots permanent | SUPERSEDED | A-28 (tie and knot split; knot to the Thread lane): `P:08_FI_08_knots-season-form` (B24), `P:14_VERBS_SOCIAL2_D_tie` (B24). | — |
| A2-34 | = A2-08 | SUPERSEDED | As A2-08. | — |
| A2-35 | is `sack` kept | DONE-IN-CODE | Never built; no live item. | — |
| A2-36 | levied stock goes home after a term | SUPERSEDED | `P:14_VERBS_MILITARY_C_the_muster` (`discharge_troops`, B22). | — |
| A2-37 | decline wrong-kind acts | DONE-IN-CODE | As M19. | — |
| A2-38 | may the scenario author occasions | DONE-IN-CODE | T-c: no dated pins; `P:21_PROCEDURAL_D_world_cards_and_churn` draws world cards at build only (A-50). | — |
| A2-39 | focalized journal row | SUPERSEDED | As M12. | — |
| A2-40 | narrow the sites citing ED-IN-0225 | STILL-NEEDED | `harness/chronicle.py:8`, `populated.py:51`, `soak.py:45` still carry the ED-IN-0225 citation in its wide form [UNVERIFIED: whether v11's CR-02 edit already narrowed them — basis: first lines only]. | IN, B03 (hygiene; with `09_WR_B_pointer_text_for_the_orchestrator`); edit set the three docstrings; gate: `grep -n ED-IN-0225 engine/season/harness/{chronicle,populated,soak}.py` reads "no carrier"; hash EQUAL; tier haiku. Block 8. |
| A2-41 | cohort spread construal | SUPERSEDED | A-91(3) (cohort convictions must be able to move) and A-56 (heavy moves of the common people) = `P:31_WR_B_the_revival_gathers`, `P:U5d_SE_cohort_heavy_moves_and_caste` (B38/B12). | — |
| A2-42 | FORCE-FOREIGN content | DONE-IN-CODE | `T:test_in36_foreign.py`. | — |
| A2-43 | authorize a sixth witness channel | STILL-NEEDED | CR-29 (event-kind `reach` roster, then `chronicle`'s paired deletion) is unbuilt: `rosters.yaml` carries no event-kind reach map; `P:08_FI_01_claim-sourced-referents` names "plan position CR-29 (the `reach` roster) `[PL]`". A-32 (one reach row for seat changes, realm-wide) and A-33 (a death reaches by presence, trail, telling) are the first rows' content. | IN, before B11 (CR-29 is a dependency of `08_FI_01`): a new batch `B-CR29` or fold into B09-memory; edit set `rosters.yaml` (`reach` roster), `loop/witness.py`; gate: `person_q.stability` non-zero at a settlement rung in seeds 0-2 of `build_realm(S, foreign=True)` over four seasons (H-234's falsifier); moves hashes: yes (commit 2); tier opus. Block 11 (shared with H-214, H-234). |
| A2-44 | IN-46/IN-47 ratification hold | DONE-IN-CODE | As A1-18. | — |
| A2-45 | J-15 playable fight choice set | SUPERSEDED | As A1-55. | — |
| A2-46 | WR-01's `resilience` slot | DONE-IN-CODE | Spirit (`attr.mind.will`) per M2. | — |
| A2-47 | `piety_track` name collision | DONE-IN-CODE | Module does not plug; nothing reads it. | — |
| A2-48 | IN-48 `delegate` Tenure kind | DONE-IN-CODE | Build reverted; ask moot. | — |
| A2-49 | the attribute roster and the source of `capability` | DONE-IN-CODE | As M2/M23. | — |
| A2-50 | troop stock, J-C-2 | SUPERSEDED | As M3. | — |
| A2-51 | eight troop tuning values | SUPERSEDED | As M3 (`P:04_MB_headcount_grade_and_scale`, `P:14_VERBS_MILITARY_C_the_muster`). | — |
| A2-52 | JQ-1 how much of a person is the draw | DONE-IN-CODE | As M1. | — |
| A2-53 | JQ-3 four magnitudes | DONE-IN-CODE | As A1-16a; ageing split is A1-16b. | — |
| A2-54 | JQ-4 weight-to-troop | DONE-IN-CODE | As A1-17. | — |
| A2-55 | JQ-6 hunger magnitude | DONE-IN-CODE | As M6. | — |
| A2-56 | SM-15 SC kernel adopt | SUPERSEDED | As A1-58. | — |
| A2-57 | ED-IN-0296 (1),(2),(3) | DONE-IN-CODE | As M1; (3) is A1-05 (STILL-NEEDED, CR-10). | — |
| A2-58 | ED-IN-0297 works | DONE-IN-CODE | As M5. | — |
| A2-59 | remit roster closed or open | DONE-IN-CODE | `rosters.yaml:317-324` `values: [issue, determine, confer, revoke, dispatch, convene]` and `open: true`: the loader reads `values` as closed. The contradiction (`open: true`) is part 8 §7 row C4 (a comment fix, STILL-NEEDED there). | — |

## Table 4 — part 8 §2: hole rows H-85 to H-248 that v9 registered (67 rows in the file; its own text says 62 and 61)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| H-85 | `thread_substrate` kind gate unread | SUPERSEDED | `CL:U5a` "C3 `knowledge_kinds` (W3) ... RESOLVED-BY R2 W3 ... the gate is a `capability_uses` row at site `told_retain`, read through `capability_admits`; A-11 admits it" = `P:17_CENSUS_REST_2_wiring` W3 (B35). | — |
| H-166 | no computed act declares a works; `found`/`build` refused at `exists:works` | SUPERSEDED | The producer (`venues.yaml:188` `planned_works:`) is built; the formation of `found`/`build` is rebuilt by `P:14_VERBS_MATERIAL_C_works` (B12) and unheld-place occupation by `P:09_WR_world_motion` edit 2 (`CL:U5d` H-166). | — |
| H-176 | no ending shown reachable | SUPERSEDED | `CL:U5d` "H-176, H-186, H-235, H-236 ... RESOLVED-BY MOTION edits 3, 2, 1" = `P:09_WR_world_motion` (B12), `P:09_WR_provided_arcs`. | — |
| H-182 | a telling does not knit teller and hearer | SUPERSEDED | A-28 (tie and knot split; knot to the Thread lane) = `P:08_FI_08_knots-season-form` (B24), `P:14_VERBS_SOCIAL2_D_tie` (B24); `CL:U5c` C-1 "the knot waits on rumour traffic ... FI-08 §3"; `tie_known` absent in the tree. | — |
| H-186 | insurgency trigger has no season form | SUPERSEDED | `CL:U5d` as H-176 (MOTION edit 2). The identity owner `faction_props` is not in that edit [UNVERIFIED]; it is kept at §1a-(c) and IN-30 below. | — |
| H-187 | `scar_weight_shift` ships 0 | DONE-IN-CODE | `data/fixtures.py:834`. | — |
| H-188 | `confliction_weight` ships 0 | DONE-IN-CODE | `data/fixtures.py:842`. | — |
| H-189 | crisis at scar threshold 3: restabilise and pursuit-track unbuilt | SUPERSEDED | A-24 (a crisis of faith is drawn and seen): `P:16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told` (B10); `CL:U5a` "H-189, H-237 RESOLVED-BY `02_CHAR_reason_trail_and_small_edits.md` Part C". | — |
| H-190 | `intent_disclosure` ships 0 | DONE-IN-CODE | `data/fixtures.py` (`grep` 9 files). | — |
| H-191 | declared intent kept? read by nothing | DONE-IN-CODE | `CL:U5a`: "STALE-FALSE-POSITIVE (as findings) ... carried"; the marker stands. | — |
| H-192 | `judged_gain` live 0.5 | DONE-IN-CODE | `data/fixtures.py` (`judged_gain`, 7 files). | — |
| H-193 | `told_valence_gain` live 0.5 | DONE-IN-CODE | `data/fixtures.py` (6 files). | — |
| H-194 | `stance_polarity` | DONE-IN-CODE | `data/fixtures.py:963` `"declared"` (CR-16). | — |
| H-195 | `holder` operand (M0g >= 5%) | STILL-NEEDED | `CL:U5a` lists H-195 among rows "open by design or declared absent ... carried"; no session proposal cites it. Trigger now live (`declared` ships). | IN, after B10; edit set `decision/options.py` `holder` operand reading `held_by` claims; gate: a 3-seed reading with >= 5% of persons holding a `held_by` claim, then the build, hash mover; tier sonnet. Block 12. |
| H-196 | `said_slant` ships `newest` | DONE-IN-CODE | `data/fixtures.py` (`said_slant`); optional ruling. | — |
| H-197 | `telling_privacy` 0; G6 dormant | SUPERSEDED | `CL:U5a`/`U5c` R-28: "the confidence break path ... RESOLVED-BY FI-02 (gate at `telling_privacy` 1.0)" = `P:08_FI_02_rumour-that-travels` (B11). | — |
| H-198 | deception | DONE-IN-CODE | As M9. | — |
| H-199 | refraction ordinal vs `remove_weight`: two ladders for one quantity | STILL-NEEDED | `CL:U5a` lists it as "carried"; no session proposal reconciles them (`grep H-199` in proposals: 0). `refraction_gain` and `remove_weight` both live. An S defect (`CLAUDE.md` §0.06). | SC/CHAR, B05 (with `U5c_SC_one_obstacle_form`) or B10; edit set `decision/options.py::refracted_confidence`, `remove_weight` reader; gate: one ladder for one quantity, the two orderings agree on a 3-point sweep; moves hashes: yes; tier opus. Block 12. |
| H-200 | AX-7 reader-competence factor | DONE-IN-CODE | `data/fixtures.py:1060` `competence_gain` (control 0), `T:test_cr19_competence_gain.py`; live grade is `assumption`. | — |
| H-201 | act-level prior measured inert | DONE-IN-CODE | Closed. | — |
| H-202 | `stance_gain` live 1 | DONE-IN-CODE | Moves outcomes under `declared` (CR-16 shipped). | — |
| H-203 | no Record names an office; `evade / defy`, `construe` | DONE-IN-CODE | `verb_table.yaml:457` `evade / defy`, `:1310` `construe` exist (restored by REM-2B/IN-09); they are attempted and refused (`audits/25` L-14); the refusal is `P:06_FA_decree_binds` (B21), `P:16_PESSIMIST_GO_the_offer_names_what_is_held` (B34). | — |
| H-204 | G6 `confidence.broken` path | SUPERSEDED | As H-197 (`CL:U5c` R-28). | — |
| H-205 | vow-break priced | DONE-IN-CODE | `T:test_cr21_cells.py`; live grade `assumption`. | — |
| H-206 | dead holder's office and `hold` unnamed | SUPERSEDED | `CL:U5d` "H-206, H-230 stale heads ... HYG item 1" = `P:06_FA_hygiene` (B03); `T:test_h206_a_death_at_matter_is_witnessed.py`, `T:test_cp_t02_01_death_names_seats.py` exist. | — |
| H-207 | `revoke` executes 0; vacancy motive | SUPERSEDED | A-35 (the head strips an officer by a resistible draw), A-19 = `P:14_VERBS_BINDING_C_turnover` (B21), `P:22_HAPPENINGS_B_the_throne_is_never_stranded` (B21); `T:test_in53_vacancy_need.py` is the vacancy-as-need reader. | — |
| H-208 | ageing and illness at the control | SUPERSEDED | A-15; as A1-16b. | — |
| H-209 | dead victim's claim never reaches `questions_for` | SUPERSEDED | A-33 (a death reaches by presence, trail, telling) with `CL:U5d` §6 ("4 rows whose measurement is stale: H-168, -209, -225, -230 ... PTR-B (re-pointed)") = `P:09_WR_B_pointer_text_for_the_orchestrator` (B03). | — |
| H-210 | `default_forgery_quality` 1 | DONE-IN-CODE | `data/fixtures.py:499`. | — |
| H-211 | MW-11 red: nothing raises a body | SUPERSEDED | `CL:U5d` "H-211 a body only falls | RESOLVED-BY ARCS-WR edit 2; plan CP-T10-04" = `P:09_WR_provided_arcs` edit 2 (B12). | — |
| H-212 | occupation's MATTER reader | SUPERSEDED | As A1-84. | — |
| H-213 | `obstacle_ceiling` 2 | SUPERSEDED | A-8 (a wound is a level "stacking under the soft cap") and `P:16_PESSIMIST_DICE_soft_ceiling` (B05) replace the fixed ceiling; fixture `data/fixtures.py:454` `obstacle_ceiling=2`. [head only] | — |
| H-214 | `chronicle` deletion; event-kind reach channel | STILL-NEEDED | CR-29 unbuilt (A2-43). `P:08_FI_01_claim-sourced-referents` lists "plan position CR-29 `[PL]`" as its dependency. | See A2-43 (Block 11). |
| H-215 | `reception_gain` 1.0; F8 reconciled | DONE-IN-CODE | `T:test_sc02_reception.py`; the valence sweep is a measurement owed by `P:05_SC_obstacle_difficulty_and_modifiers_B` (B05). | — |
| H-216 | `proof_step` 0.25 inert | DONE-IN-CODE | Re-source built (`T:test_sc02_reception.py`); a non-mirrored proof source is `P:05_SC_evidence_and_rebuttal` (B24). | — |
| H-217 | SC-04 `succession` row not seeded | STILL-NEEDED | `arrangements.yaml:52` still says "NO `succession` ROW (`disposes: hold`) YET -- CR-35's"; `state/gate.py:697` `FILLED_BY` is the first narrowing. `P:15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger` names "the `succession` contest (CR-35)" as a reader; A-14 changes the tally form, not the row. | FA, B21 (with `22_HAPPENINGS_B`) ; edit set `arrangements.yaml` (`succession`, `disposal: declared`), `loop/effects_information.py::_disposal`, `state/gate.py` election arm; gate: a hand-built vacated seat is filled by the declared row at `quorum: 2`; hash EQUAL (realm reach 0); tier opus. Block 13. |
| H-218 | `product` column; 3 of 8 asked never learn | DONE-IN-CODE | Ruled the other way by K-36/K-37 (v11); the residue is a design choice. | — |
| H-219 | failure severity by observer set | SUPERSEDED | As A1-85. | — |
| H-220 | `EventLog.append` kind check | SUPERSEDED | `CL:U5a` F-CORE-11: "H-220: `U5a_CORE_owed_edits.md` §E row 2" (B03). | — |
| H-221 | `determine` Failure arm | SUPERSEDED | As A1-86. | — |
| H-222 | person-predicate claim writer | STILL-NEEDED | As A1-87 (Block 9). | SC, B27. |
| H-223 | standing-gap bands (500,) | DONE-IN-CODE | Shipped, hash-neutral; assumption row. | — |
| H-224 | `window` arms never ran in a realm | STILL-NEEDED | A measurement that waits for a shortfall input reaching governors, i.e. for CR-29 and FA-01 (Block 11); no session item cites it. | Read in CR-29's exit (Block 11). |
| H-225 | faction-referent attention conjunct admits nothing | STILL-NEEDED | `CL:U5d` §6 marks its measurement stale ("PTR-B re-pointed"): the cause (a dead doer coheres under no faction) is unverified at the tree; re-take the measurement first. | IN, B09; edit set none until the re-take; gate: a 3-seed reading of the conjunct's admissions, then decide; hash EQUAL; tier haiku (measure). Block 14. |
| H-226 | `interrogate` has no site for custody | SUPERSEDED | `CL:U5c` G-17 "rewrite H-226 to its residue ... RESOLVED-BY RES §1"; `P:14_VERBS_SOCIAL2_C_case_question_confession` (B25), `P:08_FI_05_evidence-interface` (B24); `T:test_in12_interrogate.py`. | — |
| H-227 | `terms_sourced` admits only dispensation | STILL-NEEDED | No session proposal or closure row cites H-227 (`grep` 0). `T:test_in12_*` do not cover a petition-as-occasion. | SC/IN, B27 (`05_SC_arrangement_rows_that_bind`); edit set `data/rosters.py` `RECORD_REFERENT_KINDS`/`writs_held`; gate: a `commit` forms on a docketed petition in a hand-built world; moves hashes: yes; tier sonnet. Block 14. |
| H-228 | `raze` executes 0 in computed play | SUPERSEDED | `CL:U5b`/`U5c`; A-73 (the taker may raze while it is in his hand) = `P:14_VERBS_PHYSICAL_B_field_and_ruin` (B22); `T:test_in12_raze.py`. | — |
| H-229 | `give` on a Rung executes 0 | SUPERSEDED | `CL:U5a` (owning lanes' closures); `P:14_VERBS_SOCIAL1_A_formation` (B11), `P:14_VERBS_PHYSICAL_A_custody_and_force`; `T:test_in12_give_rung.py` is the producer. | — |
| H-230 | IN-61 stopped; no claim names the throne | DONE-IN-CODE | `T:test_cp_t02_01_death_names_seats.py`, `T:test_cp_t02_02_seat_ids.py`, `T:test_in61_succession.py`, `T:test_in61_heir_hears_vacancy.py`; `CL:U5d`: "stale heads". | — |
| H-231 | razing witnessed by the razer alone | SUPERSEDED | `CL:U5c` R-23 = `P:08_FI_04_small-edits` §3 (B11) and `P:16_PESSIMIST_...` PES-C edit 1. | — |
| H-232 | `pardon`/`raze` form on every referent | SUPERSEDED | `CL:U5d` "H-232 is CHAR's and FA's formation" = `P:14_VERBS_SOCIAL2_A_formation_on_what_is_known` (B25), `P:02_CHAR_offer_what_can_be_done` (B10). | — |
| H-233 | empire's `march` chosen at 7 of 80 seeds | SUPERSEDED | `CL:U5a` "H-233, H-343 RESOLVED-BY goal lean; reason trail" = `P:02_CHAR_goal_lean_on_its_own_question` (B10). The per-territory cap is §1a-M1res. | — |
| H-234 | no unrest sign has a settlement subject | STILL-NEEDED | CR-29 (A2-43, Block 11); `CL:U5d`/`audits/25` G-11 correct that the row is not flagged by `needs_jordan`. | See A2-43. |
| H-235 | lattice coupling ships 0 | SUPERSEDED | `CL:U5d` MOTION edit 1 = `P:09_WR_world_motion` (B12); `data/fixtures.py:700` `lattice_coupling=0`. | — |
| H-236 | lattice has no source | SUPERSEDED | `CL:U5d`: "WR's (Part 3: `09_WR_world_motion.md` edit 1; A-40 makes the wear a real condition of places)". | — |
| H-237 | no told claim carries a chain | SUPERSEDED | `CL:U5a` = `P:02_CHAR_reason_trail_and_small_edits` Part C (B10). | — |
| H-238 | superseded as blocker | DONE-IN-CODE | Nothing to build. | — |
| H-239 | TS gate 30 | DONE-IN-CODE | `T:test_k3_thread_sensitivity.py`. | — |
| H-240 | PC-10b `accept` binds a `challenge` Record | DONE-IN-CODE | `T:test_pc10b_challenge_record.py`. | — |
| H-241 | `field_provisioning` OFF | SUPERSEDED | As A1-52 (`CL:U5d` "SUPPLY"). | — |
| H-242 | `hunger_band_floors` | DONE-IN-CODE | `data/fixtures.py:512`. | — |
| H-243 | `stock_report` | DONE-IN-CODE | `data/fixtures.py:641`. | — |
| H-244 | `effort_level` | DONE-IN-CODE | `data/fixtures.py:466`; `T:test_cp_t01_05_npc_effort.py`. | — |
| H-245 | `practice_window` 4 | DONE-IN-CODE | `data/fixtures.py` (3 files). | — |
| H-246 | `practice_step` 2 | DONE-IN-CODE | Same. | — |
| H-247 | `practice_cap` 2 | DONE-IN-CODE | `data/fixtures.py:479`. | — |
| H-248 | `odds_weighting` `believed` | DONE-IN-CODE | `data/fixtures.py:971`; `T:test_cr17_odds_weighting.py`. | — |

## Table 5 — part 8 §3 (19 editorial ids), §4 (40 state-index rows)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| ED-914 | PP-719 recorded | DONE-IN-CODE | `registers/editorial_ledger.jsonl` last row 2026-10-26 `closed`. | — |
| ED-FA-0039 | goal content assumptions | DONE-IN-CODE | `editorial_ledger_fa.jsonl` `open`, `needs_jordan` false; `goals.yaml`. | — |
| ED-FI-0009 | `finding.none` routing | DONE-IN-CODE | `editorial_ledger_fi.jsonl` `open`, false; `undeposited_kinds`. | — |
| ED-IN-0261 | cells folded; doctrine PROVISIONAL | DONE-IN-CODE | `editorial_ledger_in.jsonl` `partial` (2026-11-12), false. | — |
| ED-IN-0292 | founding; vacancy as claim | DONE-IN-CODE | Last row `closed` (2026-11-06), `needs_jordan` false. | — |
| ED-IN-0293 | pursuit counts | DONE-IN-CODE | `superseded` (2026-10-26). | — |
| ED-IN-0295 | B-X decisions | DONE-IN-CODE | `open`, false; built at IN-64. | — |
| ED-IN-0296 | the three questions | DONE-IN-CODE | Last row `resolved` (2026-11-04), false. | — |
| ED-IN-0297 | works from where | DONE-IN-CODE | `closed` (2026-10-26). | — |
| ED-IN-0298 | sixth §C.6 channel | STILL-NEEDED | Last row `partial`, `needs_jordan` false (2026-10-26): the build (CR-29) is open. | See A2-43 (Block 11). |
| ED-SE-0003 | OPT-9 armature keying | DONE-IN-CODE | `editorial_ledger_se_archive.jsonl` `superseded` (2026-10-26). | — |
| ED-SE-0006 | fort level bundle | DONE-IN-CODE | Same. | — |
| ED-SE-0025 | Gongsuo Registration | DONE-IN-CODE | Same. | — |
| ED-SE-0026 | Convene the Circle | DONE-IN-CODE | Same. | — |
| ED-SE-0027 | Borrow / financier loan | DONE-IN-CODE | Same. | — |
| ED-SE-0028 | Boschi Pubblici Requisition | DONE-IN-CODE | Same. | — |
| ED-SE-0029 | Podestà | DONE-IN-CODE | Same. | — |
| ED-SE-0030 | Corregidor overlay | DONE-IN-CODE | Same. | — |
| ED-SC-0040 | F8 reception/proofs | DONE-IN-CODE | `editorial_ledger_sc.jsonl` `closed` (2026-10-26); `T:test_sc02_reception.py`. | — |
| IN-09 | restore `evade / defy`, `construe` | DONE-IN-CODE | Rows exist (H-203). | — |
| IN-12 | proceedings verbs remainder | SUPERSEDED | The remainder is split across `P:14_VERBS_SOCIAL2_C_case_question_confession`, `P:14_VERBS_SOCIAL1_A_formation`, `P:08_FI_04_small-edits` (rows H-226, H-229, H-231, H-232); H-227 is the one orphan (STILL-NEEDED above). | — |
| IN-14 | more rounds; narrow the `budget` hold count | STILL-NEEDED | As A1-50 (Block 7); `CL:U5c`/`U5a` H-92: R-22 "SUPERSEDED by R-39: measured and declined ... lands only after FI-02's traffic arm". | See A1-50. |
| IN-18 | telling residue | SUPERSEDED | `P:08_FI_02_rumour-that-travels` (B11), `P:16_PESSIMIST_SC_E_an_honest_teller_is_not_marked` (B11), `P:14_VERBS_SOCIAL1_C_persuasion_and_deceit` (B28). | — |
| IN-30 | insurgency / emerged factions | STILL-NEEDED | The streak and contiguity triggers go with `P:09_WR_world_motion` edit 2 (SUPERSEDED, H-186); the `faction_props` identity owner and creed `utter` are not in it [UNVERIFIED]. | See §1a-(c) (Block 4). |
| IN-32 | tie/knot, told chain | SUPERSEDED | As H-182, H-237. | — |
| IN-33 | `exchange` restore | DONE-IN-CODE | `T:test_in33_exchange.py`. | — |
| IN-36 | foreign + guards | DONE-IN-CODE | `T:test_in36_foreign.py`; remainder is §1a-M1res. | — |
| IN-44 | stale text | SUPERSEDED | As A1-77. | — |
| IN-45 | works authored | DONE-IN-CODE | As M5. | — |
| IN-46 | grid suspension | DONE-IN-CODE | `T:test_rem31_grid_suspension.py`. | — |
| IN-47 | character sheet | DONE-IN-CODE | `T:test_rem30_character_sheet.py`. | — |
| IN-48 | delegation | SUPERSEDED | A-10, A-22; `CL:U5d` H-108 "SUPERSEDED ... IN-48 the owner; A-22 fixes whom a seat commands". | — |
| IN-52 | troop provisioning | SUPERSEDED | As A1-52. | — |
| IN-58 | sworn half; petition conjunct | STILL-NEEDED | No `test_in58*`; blocks H-209/H-225 re-measure (Block 14). CR-16 (its blocker) is shipped. | IN, B09/B10; edit set `decision/options.py` sworn read; gate: a hand-built sworn person attends the petition question first; moves hashes: yes; tier sonnet. Block 14. |
| IN-61 | succession | DONE-IN-CODE | `T:test_in61_succession.py`. | — |
| SC-02 | reception, 22b | DONE-IN-CODE | `T:test_sc02_reception.py`, `T:test_sc02_22b_standing_crossing.py`, `T:test_sc02_22b_consequence_and_forgery.py`; remainder: H-219..H-223 above. | — |
| SC-03b | `DEGREES RESOLVED` gaining `a proposition` bands | WRONG | v11's own reading (2026-10-26): "the observable as worded cannot be met" (`corpus_run 0` prints one histogram over all verbs; `determine` foldable but never attempted). | — |
| SC-04 | `succession` row | STILL-NEEDED | As H-217 (Block 13). | See H-217. |
| SC-05 | kernel adoption | SUPERSEDED | `P:05_SC_sc05_kernel_disposition_B`, `P:05_SC_sc05_kernel_retirement` (B24). | — |
| SC-06 | proceedings verb owner | DONE-IN-CODE | Row deleted at adoption; A-10. | — |
| SC-07 | P-4, V-4, V-5 speech kinds | SUPERSEDED | `CL:U5a` H-153/H-154 "SUPERSEDED by the owning lane's closure (SC: U5c)" = `P:U5c_SC_proceedings_residue` (B27). [head only] | — |
| SE-04 | cohort seats, envelope writer | SUPERSEDED | (c) closed at weight 2; (b) the `Rung.envelope` writer is `P:07_SE_population_regrowth_B`/`07_SE_population_census` (B12); (a) landed. | — |
| SE-05 | alias of IN-30 | STILL-NEEDED | As IN-30. | See §1a-(c). |
| SE-06 | cohort temperaments | DONE-IN-CODE | `cohorts.yaml:145`. | — |
| MB-07r | cap support at weapon reach | DONE-IN-CODE | Closed (v11 §4). | — |
| MB-08 | commander-chosen orders (LEAVE) | SUPERSEDED | `P:27_MB_D_the_commander_as_chooser`, `P:26_MASS_BATTLE_maneuver_orders` (B20). | — |
| PC-05 | Godot target | DONE-IN-CODE | Closed by GO-14's `ED-PC-0013` row (v11). | — |
| PC-06 | thread sensitivity gate (K-1, K-5 held) | SUPERSEDED | K-3 landed (`T:test_k3_thread_sensitivity.py`); the held remainder is replaced by `P:09_WR_threadwork_module` (B03), `P:14_VERBS_PHYSICAL_D_thread_read` (B35). [head only] | — |
| PC-08 | unwatched fights (LEAVE) | SUPERSEDED | A-1, A-4. | — |
| PC-10 | challenge/accept | DONE-IN-CODE | `T:test_pc10b_challenge_record.py`. | — |
| FI-05 | alias of IN-32 | SUPERSEDED | As IN-32. | — |
| WR-01 | practitioner resilience slot | SUPERSEDED | `P:09_WR_B_threadwork_session_and_practitioner` (B35). [head only] | — |
| GO-01 | Godot version owner | STILL-NEEDED | `tools/export_game_constants.py` has no version reference (`grep 4.7|godot_version` 0). ED-GO-0002 is on `main` (4.7). `P:11_GO_port_gate_order_and_coverage` assumes GO-01's need "is met". | GO, B41; edit set `tools/export_game_constants.py` reads the ED-GO-0002 version; gate: its `--check` round-trip includes the version; hash EQUAL; tier haiku. Block 15. |
| GO-05 | port pipeline step | SUPERSEDED | `P:11_GO_port_gate_order_and_coverage` (B41). [head only] | — |
| GO-06 | another-repository step | SUPERSEDED | Same. [head only] | — |
| FA-01 | trade-demand clause | STILL-NEEDED | Needs CR-29 (Block 11). | See A2-43. |
| FA-02 | alias of IN-30 | STILL-NEEDED | As IN-30. | See §1a-(c). |
| FA-03 | LEAVE | STILL-NEEDED | Trigger-held; content owner entry is in v11 parts 3/4 (E-lane); not copied here [UNVERIFIED]. | FA, B-Z; see lane E1/E2. |
| FA-07 | LEAVE (five row texts) | SUPERSEDED | `P:15_INSTITUTIONS_SYNTHESIS_A_one_kit` (B32), A-14: elections and benches resolve in one act. [head only] | — |

## Table 6 — part 8 §5 to §7 (failing tests, v9 contradictions, verb-suite gaps, errata)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| FT-1 | `test_forked_status.py::test_the_fork_rows_name_a_real_ref` fails (shallow) | DONE-IN-CODE | The clone, not `main`: `.git/shallow` holds the boundary (`audits/25` §0: 176 reachable commits). No code change. | — |
| FT-2 | `...test_the_evacuated_content_is_actually_at_the_ref` | DONE-IN-CODE | Same. | — |
| CT-1 | IN-14: state index vs entry | STILL-NEEDED | As A1-50 (BUILD wins). | See A1-50. |
| CT-2 | ED-IN-0292 (1): PENDING vs ruled NO | DONE-IN-CODE | Last row `closed`. | — |
| CT-3 | Godot heading removed | DONE-IN-CODE | Re-read before citing; `godot/godot_conversion_strategy_v1.md` PROPOSED. | — |
| CT-4 | SC-03b `DEGREES RESOLVED` | WRONG | As SC-03b. | — |
| PC-G33 | `fight` gated on war (disputed) | DONE-IN-CODE | `rosters.yaml: violence_contexts` (CR-87, `T:test_cr87_violence_contexts.py`); A-16/D-41. | — |
| MB-G03 | `levy`/`requisition` rename | DONE-IN-CODE | `verb_table.yaml:1010` `requisition`. | — |
| MB-G40 | arrival, `seize`, `raze` | DONE-IN-CODE | `verb_table.yaml:1416` `raze`, `:1439` `seize`. | — |
| SC-G02 | docket item names arrangement | DONE-IN-CODE | Landed SC-03a. | — |
| SC-G30 | `determine.unheard` struck | DONE-IN-CODE | Contested by the suite's own lane; no defect. | — |
| SC-G46 | `challenge`/`accept` duel; accusation = `petition` | DONE-IN-CODE | `T:test_pc10b_challenge_record.py`. | — |
| SC-G53 | `tell` uncelled; `speak` cells owed | DONE-IN-CODE | Contested; cells fall to M14. | — |
| FI-G15 | finding an effect-side deposit | DONE-IN-CODE | Contested. | — |
| FI-G37 | half false | DONE-IN-CODE | Contested; yield defect is FI-G01's. | — |
| FI-G44 | pool vs Ob not a contest | DONE-IN-CODE | Contested. | — |
| TW-G22 | `+1 Ob` per wound stale prose | SUPERSEDED | A-8 (a wound is a level, replacing 0.15 per wound): the "ruled figure in code" is itself replaced by `P:10_DICE_one_score_two_roles`/`U5a_DICE_owed_edits` (B05). | — |
| TW-G25 | `weave` held load | DONE-IN-CODE | Correction is in the suite. | — |
| GV-G01 | store row is `requisition` | DONE-IN-CODE | `verb_table.yaml:1010`. | — |
| GV-G12 | readers built; `church_standing` unchecked | STILL-NEEDED | Unowned [INFERRED in v11]; a one-grep check. | PC/SC, B27; edit set none unless `church_standing` is read; gate: `grep church_standing engine/season`; hash EQUAL; tier haiku. Block 12. |
| GV-G37 | vassalage read by `oblige` clause | DONE-IN-CODE | `state/gate.py:353`. | — |
| FA-G48 | reader exists | DONE-IN-CODE | Same. | — |
| EC-G01 | rename landed | DONE-IN-CODE | As MB-G03. | — |
| EC-G22 | unpaid upkeep | DONE-IN-CODE | As A2-31. | — |
| WT-G02 | `move`/`migrate` clauses | DONE-IN-CODE | Contested. | — |
| WT-G09 | leg lifetime | DONE-IN-CODE | Ruled in code. | — |
| NP-G23 | `repudiate` merged into `release` | DONE-IN-CODE | IN-11 landed. | — |
| ER-G10 | the log refuses only at the fold | SUPERSEDED | `U5a_CORE_owed_edits` §E row 2 (`CL:U5a`; B03). | — |
| ER-G18 | 40-item remediation cannot meet THE NINE | DONE-IN-CODE | A pointer to `_part2`; the session's nine map is `master/instructions/IS_A_NINE.md`. | — |
| ER-C5 | `work`/`restore` readings | SUPERSEDED | `P:14_VERBS_MATERIAL_C_works` (B12); `CL:U5d` OWED-SE §1 (R-SE-16: cause not isolated; no code edit planned). | — |
| ER-C8 | the 250 `finding.none` breakdown unreproduced | WRONG | v11: "unreproduced by its own arithmetic: treat as unverified"; the census counts afresh (`audits/17_CENSUS_REST`). | — |
| ER-C4 | remit roster `open: true` while comments say CLOSED | STILL-NEEDED | `rosters.yaml:317-324` still carries `open: true` beside the closed `values` (A2-59). A comment/flag fix, hash EQUAL. | IN, B03 (hygiene); edit set `rosters.yaml` remit roster flag; gate: the roster loader reads the flag consistently and no comment contradicts it; tier haiku. Block 8. |
| ER-GF9 | dead constants exported to `sim_params.json` | STILL-NEEDED | `engine/engine_params/sim_params.json` and `value_pointer_links.json` still name `DEPTH_TS_MINIMUM`, `BREADTH_OB`, `DISTANCE_OB` (`grep`). | IN, B03; edit set the exporter source (`tools/export_sim_params.py`); gate: `--check` round-trip without them; tier haiku. Block 8. |
| ER-GF10 | `attempt_leap` docstring vs hard-coded 30 | STILL-NEEDED | `systems/threadwork/sim/operations.py:354,360` still: docstring "optional `ts_minimum` (default 30)", code `if ts < 30`. | WR/PC, B35; edit set that function; gate: `ts_minimum` honoured or the docstring corrected; tier haiku. Block 8. |
| ER-JF10 | pursuit weights not normalised (Saemund 1.31) | STILL-NEEDED | `grep Saemund` finds nothing in `references/npc_registry.yaml` or `goals.yaml` (the registry names differ) [UNVERIFIED]; `P:16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says` (B10) gives pursuit cells a target (`CL:U5a`). | CHAR, B10 (read there first); edit set none beyond that proposal; gate: pursuit weights sum to one per person or the loader refuses; tier sonnet. Block 12. |
| ER-JF12 | 55 vs 56 regions in a geography file | DONE-IN-CODE | Reference only (`CLAUDE.md` §0.05); no position. | — |
| ER-JU | u-value 0.9505; acts per person-season | DONE-IN-CODE | `audits/25` L-15..L-17 settled the related counts. | — |
| ER-KF3 | contact not explained (discipline < 3, speed 0.4) | SUPERSEDED | `P:26_MASS_BATTLE_calibration_targets`, `P:27_MB_A_command_and_the_obedience_draw` (B19). [head only] | — |
| ER-KF13 | seed-1 breakdown names nine of ten | DONE-IN-CODE | Superseded by the census counts. | — |
| ER-X9 | `tend` refusal split differs | DONE-IN-CODE | Same. | — |
| ER-X15 | conviction crisis never graded | SUPERSEDED | A-24 = `P:16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told` (B10). | — |
| ER-P3 | "what remains Jordan's" (JQ, D-V, J-C) | DONE-IN-CODE | Answered at A1/A2 and M-rows above. | — |
| ER-TL6 | THROUGHLINES §6 five dispositions | DONE-IN-CODE | Reference only. | — |

## Table 7 — part 9 §2: the other 171 hole rows

Evidence shorthand for this table: "script" = every backticked symbol and path of the v11 cell was found in the tree by the scratch check (see head), so the v11 CLOSED/ACCEPT claim is at least not contradicted; "live grade" = `engine/season/hole_register.yaml` grade, unchanged from the v11 cell unless said.

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| H-01 | `social:` value per `(kind, field)` | DONE-IN-CODE | `write_matrix.yaml` 40 rows with `social:`; `data/matrix.py:163`; script. | — |
| H-02 | one fold over the verb rows | DONE-IN-CODE | `loop/resolve.py` single `resolve`; the table is 69 `verb:` lines now (v11 says 56, `audits/25` L-12 says 67 rows: both counts stale); script. | — |
| H-03 | chooser weighting injected | DONE-IN-CODE | `decision/choose.py::make_chooser`; script. | — |
| H-04 | question sources | DONE-IN-CODE | `queries/world_q.py::questions_for`; script. | — |
| H-05 | cast not empty of `hold` | DONE-IN-CODE | Probe `W12`; script. | — |
| H-06 | `condition_scale` 1000 | DONE-IN-CODE | `data/fixtures.py` (40 files name it). | — |
| H-07 | per-kind wear rates | DONE-IN-CODE | `rosters.yaml: wear_per_season`; script. | — |
| H-08 | band floors | DONE-IN-CODE | `rosters.yaml: band_floors`; script. | — |
| H-09 | `ledger_cap`, `view_k`, `confidence_default` | DONE-IN-CODE | `data/fixtures.py` (13/28/12 files). | — |
| H-10 | scene budget ceiling live | STILL-NEEDED | `loop/driver.py:479` `rounds = int(w.fixtures.get("scene_budget"))`. `CL:U5a` "H-10 open, live | RESOLVED-BY F-CORE-06's carrier (IN-14)"; A-56 also supersedes part of its cohort case (`P:U5d_SE_cohort_heavy_moves_and_caste`). | See A1-50 (Block 7). |
| H-11 | `subsistence_weight` magnitudes | STILL-NEEDED | CR-22 (per-head need by a reading rule) has only register mentions in the tree. `P:07_SE_ground_and_granaries` "amends ... CR-22 (hunger binds)" (B12) and does not replace it. | SE, B12; Block 16. |
| H-12 | silent write refused | DONE-IN-CODE | `state/world.py` refuses an undeclared `emits` kind; `CL:U5a` H-12 "closed". | — |
| H-20 | pursuit/axis roster | DONE-IN-CODE | `rosters.yaml` `pursuits`, `pursuit_axes`; script. | — |
| H-21 | pooled quantity not social | DONE-IN-CODE | `write_matrix.yaml` `Rung.stores`. | — |
| H-22 | `Record` rows | DONE-IN-CODE | `write_matrix.yaml:298-331`. | — |
| H-23 | no cost column | DONE-IN-CODE | The refusal is the ruling. | — |
| H-24 | `Person.exists` row | DONE-IN-CODE | `write_matrix.yaml:233`. | — |
| H-25 | five `kind: LOOP` rows | DONE-IN-CODE | LEAVE with a trigger recorded in the register row; `harness/loops.py`, `T:test_loops_instrument.py`. [convention 6, below] | — |
| H-26 | `season_factor_draw` keyed per territory | SUPERSEDED | As M16 (A-54; `P:09_WR_B_draws_not_thresholds` B12); `T:test_season_weather_per_territory.py` is commit (1). | — |
| H-27 | `Person.travel_leg` | DONE-IN-CODE | `state/carriers.py`; script. | — |
| H-28 | person-side budget | DONE-IN-CODE | `decision/budget.py`. | — |
| H-29 | `standing_of`, `agreement` | DONE-IN-CODE | `decision/options.py`. | — |
| H-30 | canonical order | DONE-IN-CODE | `loop/resolve.py::_canonical_order`. | — |
| H-31 | degree ladder | DONE-IN-CODE | `engine/dice_engine/dice_engine.py:227` `degree_from_net`; `audits/25` V-16 compares it with the mass-battle ladder (6 of 10,000 cells differ), which `P:10_DICE_exported_face_rule_and_band_edges` (B05) closes. | — |
| H-32 | bench judging set | DONE-IN-CODE | `queries/world_q.py::judging_set`. | — |
| H-33 | fan-out `all_five` | DONE-IN-CODE | `data/fixtures.py` (16 files). | — |
| H-34 | `establishment_of` | DONE-IN-CODE | `queries/world_q.py`; script. | — |
| H-35 | `scene_budget=5` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-36 | receiver-side refraction | DONE-IN-CODE | `decision/options.py::refracted_confidence`. | — |
| H-37 | no fault roster | SUPERSEDED | SC-05 kernel disposition (A1-58): `P:05_SC_sc05_kernel_disposition_B`, `P:05_SC_sc05_kernel_retirement` (B24). | — |
| H-38 | `Person.body` banded as penalty only | DONE-IN-CODE | `decision/budget.py::body_band_penalty`. | — |
| H-39 | cohort spread shape | DONE-IN-CODE | Closed by M1. | — |
| H-40 | `claim_decay_per_season=5` | DONE-IN-CODE | `data/fixtures.py` (7 files); `T:test_cr55_matter_lapses.py` exists. | — |
| H-41 | `found`/`build` rows | DONE-IN-CODE | `verb_table.yaml`; `T:test_works_founding.py`. | — |
| H-42 | `utter` row | DONE-IN-CODE | `verb_table.yaml`. | — |
| H-43 | `_mint_document` | DONE-IN-CODE | `loop/effects_information.py`. | — |
| H-44 | nine dispensation term types unenumerated | SUPERSEDED | `CL:U5a` H-44 "other lanes' mechanisms SUPERSEDED by the owning lane's closure (FA: U5d)": A-21 (a decree is proclaimed) = `P:06_FA_decree_binds` (B21), `P:14_VERBS_BINDING_A_formation` (B21). [head only] | — |
| H-45 | inquiry rows | DONE-IN-CODE | `verb_table.yaml`. | — |
| H-46 | pursuits and axes from the registry | DONE-IN-CODE | `rosters.yaml:465,501`. | — |
| H-47 | `Person.coherence` has no producer | SUPERSEDED | `CL:U5a` "H-47 refiled: row present, producer absent | RESOLVED-BY §A row 3"; the producer: A-43 (zero coherence unknowable) = `P:U5d_WR_zero_coherence_unknowable`, `P:09_WR_B_threadwork_session_and_practitioner` (B35). `grep coherence state/carriers.py` finds none. | — |
| H-48 | `disclosure:` column | DONE-IN-CODE | LEAVE; trigger (a player-facing reader) may now fire through `P:09_WR_B_chronicle_that_tells` (B36) and `P:11_GO_player_surface_contract_B` (B34): E6 to E8 re-dispose the register row. | — |
| H-49 | `(Person, weight)` has no writer | SUPERSEDED | `P:07_SE_population_census` (B12: "CR-08's CENSUS writer, specified") and `P:07_SE_population_regrowth_B`; `CL:U5a` H-49 "by workplan CR-08 ... withdrawn: conflict C-U5a-02". `grep weight.changed loop/` finds none. | — |
| H-50 | `Tenure.payload` | DONE-IN-CODE | `write_matrix.yaml:399`; `state/world.py::_grant_remit`. | — |
| H-51 | `demanded_person` | DONE-IN-CODE | `queries/world_q.py`; `T:test_territorial_subsistence.py`. | — |
| H-52 | `remit:determine` eligibility | DONE-IN-CODE | `verb_table.yaml:981` note; see A2-59. | — |
| H-53 | `recent` View rule | DONE-IN-CODE | `decision/questions.py::view_ids`. | — |
| H-54 | aggregation `first` | DONE-IN-CODE | `data/fixtures.py:547`. | — |
| H-55 | `observers_for` flood bounded | DONE-IN-CODE | `epistemic.py`. | — |
| H-56 | nested DELIBERATE half | SUPERSEDED | A-4, A-72 (as A1-47); `CL:U5a` "H-56's held half closed as irrelevant until nesting exists" (now exists). | — |
| H-57 | `forgive` | DONE-IN-CODE | `T:test_in12_forgive.py`. | — |
| H-58 | `exchange` untyped row | DONE-IN-CODE | `T:test_in33_exchange.py`; live grade `assumption`. | — |
| H-59 | grudges end by forgive | DONE-IN-CODE | `loop/effects_combat.py::_eff_forgive`. | — |
| H-60 | same budget for all | DONE-IN-CODE | `loop/deliberate.py`. | — |
| H-61 | module entry rows | DONE-IN-CODE | `references/module_contracts.yaml`. | — |
| H-62 | `(Person, coherence)` write | SUPERSEDED | As H-47. | — |
| H-63 | `speak` writes `[]` | DONE-IN-CODE | `verb_table.yaml:1189-1193`; `CL:U5a` "SUPERSEDED by the owning lane's closure (SC: U5c)" for `speak`'s values. | — |
| H-64 | probes issue invented verbs | DONE-IN-CODE | LEAVE; process-only artefact. | — |
| H-65 | three untyped rows | DONE-IN-CODE | `exchange`, `construe` (`verb_table.yaml:1310`), `evade / defy` (`:457`) exist after REM-2B; `queries/readers.py` is gone (the row says so). | — |
| H-66 | alignment table | DONE-IN-CODE | `rosters.yaml:3041-3047`; `CL:U5a` "H-66's and H-347's cells are now given a target by `16_PESSIMIST_CHAR_B`" (extends). | — |
| H-70 | `budget_office_bonus`, `budget_leg_penalty` | DONE-IN-CODE | `data/fixtures.py:526-527`; script. | — |
| H-71 | remit grant snapshot | DONE-IN-CODE | `state/world.py::_grant_remit`; script. | — |
| H-72 | `evaluate` map | DONE-IN-CODE | `data/requires.py:672`. | — |
| H-73 | self/other consumer chain | DONE-IN-CODE | REM-44 landed (v11). | — |
| H-74 | `make_chooser` | DONE-IN-CODE | `decision/choose.py`. | — |
| H-75 | `hold:<kind>` placeholder | DONE-IN-CODE | LEAVE; `audits/25` G-16 re-grounds (rows at `verb_table.yaml:340,659,2062`). | — |
| H-76 | `interactions_per_scene=3` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-77 | `extended_scene_cost=2` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-78 | `scene_packing_rule` | DONE-IN-CODE | `data/fixtures.py` (3 files). | — |
| H-79 | `claim_subject_rule` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-80 | `record_stages_default` | DONE-IN-CODE | `data/fixtures.py`; readers waiting on it (CR-34 landed, CR-35 partly, CR-36/37 not). | — |
| H-81 | `obstacle_refusal_multiple=2` | DONE-IN-CODE | `seam/wrappers/sigma.py:273`. | — |
| H-82 | cause union invariant | DONE-IN-CODE | `state/log.py`. | — |
| H-83 | `stratum_of` | DONE-IN-CODE | `loop/resolve.py`. | — |
| H-84 | `give` producer; reach thin | DONE-IN-CODE | `T:test_give.py`; reach: `T:test_cr03_acquaintance_arm.py`, `T:test_cr81_realm_acquaintances.py` landed. | — |
| H-86 | conditional emission exemption | DONE-IN-CODE | `rosters.yaml: conditional_emission_rows`. | — |
| H-87 | `contest_max_depth=2` | DONE-IN-CODE | `data/fixtures.py`. A-72 sets nesting cap 1 for a battle's duel round: the number is `P:03_PC_duel_round_and_approach_B` step 5's. | — |
| H-88 | seam refuses by name | DONE-IN-CODE | Superseded by the build (`seam/wrappers/`). | — |
| H-89 | inert `scale:` column | STILL-NEEDED | As A1-46 (CR-07, Block 6). | IN, B03. |
| H-90 | ladder/purview built; Parliament, delegation, sovereign power unbuilt | SUPERSEDED | `CL:U5d` H-90: A-14 (a vote is a draw on the voter inside the presiding act), A-76 (any working realm bench stands in), `P:15_INSTITUTIONS_VENICE_C_roll_lot_ballot` (B32). | — |
| H-91 | `remit:revoke` beside purview | DONE-IN-CODE | `CL:U5d` "STALE-FALSE-POSITIVE ... closed by precedent"; `state/gate.py:370-375`. | — |
| H-92 | `budget` counts every `hold` | STILL-NEEDED | `CL:U5a` R-22: "SUPERSEDED by R-39: measured and declined at IN-14; lands only after FI-02's traffic arm" — the narrowing stays owed, gated on `P:08_FI_02_rumour-that-travels` (B11). | See A1-50 (Block 7); gate adds FI-02 landed. |
| H-93 | `SITE_YIELD` | DONE-IN-CODE | `data/fixtures.py`; draws replaced by A-54 (M16). | — |
| H-94 | operands for payloads | DONE-IN-CODE | `decision/options.py::operands_for`; CR-25 landed. | — |
| H-95 | 143 worlds run | DONE-IN-CODE | Not re-run (v11's critic could not either); no contradiction. | — |
| H-96 | tau | DONE-IN-CODE | `data/fixtures.py:321` `0.05` (CR-17's rule). | — |
| H-97 | `party_end` | DONE-IN-CODE | `seam/wrappers/combat.py`. | — |
| H-98 | fourth combat band | DONE-IN-CODE | LEAVE with trigger; `P:03_PC_typed_outcome_one_door` (B14) may fire it [head only, UNVERIFIED]. | — |
| H-99 | `Office` three axes | DONE-IN-CODE | `state/carriers.py`. | — |
| H-100 | `REVOCATION_DISPOSAL` | DONE-IN-CODE | `state/gate.py:599`; `T:test_in31_revocation_cost.py`. v11's `test_in40_oblige_purview.py` is not in the tree (script): the closure rests on the first test. | — |
| H-101 | `own_purview` misses the `oblige` clause | STILL-NEEDED | CR-09 has no mention in the tree; `queries/world_q.py:1080` `own_purview` still re-derives the walk; `CL:U5d` "H-101 ... RESOLVED-BY plan CR-09 (the set form)". | IN, B09 or B21; Block 17. |
| H-102 | signed loop bounded | DONE-IN-CODE | LEAVE with trigger (`harness/loops.py`). | — |
| H-103 | decay | DONE-IN-CODE | `loop/matter.py`. | — |
| H-104 | eviction | DONE-IN-CODE | `loop/witness.py`; `test_tracer_is_honest.py` does not exist (row says so). | — |
| H-105 | raising arm of `restore`/`work` | SUPERSEDED | `CL:U5d` F-SE-05: "RESOLVED-BY OWED-SE §1 (the reading added to H-105's and H-171's cites; cause not isolated, so no code edit is planned until it is)" = `P:U5d_SE_owed_edits`. | — |
| H-106 | loops completeness | DONE-IN-CODE | LEAVE; `harness/loops.py`. | — |
| H-107 | `Event.subject` deleted | DONE-IN-CODE | `state/carriers.py`. | — |
| H-108 | delegation without a `hold` | SUPERSEDED | `CL:U5d` H-108 "A-10 ... leaves IN-48 the owner; A-22 fixes whom a seat commands". | — |
| H-109 | `_req_revoke` | DONE-IN-CODE | `loop/predicates.py`. | — |
| H-110 | `band_crossed` Question | DONE-IN-CODE | Dissolved. | — |
| H-111 | `finding.none` skip at WITNESS | DONE-IN-CODE | `rosters.yaml: undeposited_kinds`; CP-T06-04 in code (54 mentions). | — |
| H-112 | `_emitted_by_write` bound | DONE-IN-CODE | `state/world.py`. | — |
| H-113 | `emits_at` | DONE-IN-CODE | `loop/resolve.py`. | — |
| H-114 | `_eff_kill` takes `res` | DONE-IN-CODE | `loop/effects_combat.py:38`. | — |
| H-115 | `Unspecified` | DONE-IN-CODE | `data/verbs.py`. | — |
| H-116 | `belief_contradicts` | DONE-IN-CODE | `epistemic.py:72`. | — |
| H-117 | budget never binds | DONE-IN-CODE | REM-16 re-take instrument in the tree (5 mentions). | — |
| H-118 | `content_hash` folds state | DONE-IN-CODE | `state/world.py`. | — |
| H-119 | degree read off the scene | DONE-IN-CODE | `seam/ladder.py::combat_degree`; A-3 reads end state for fields. | — |
| H-120 | five prizes claimed | DONE-IN-CODE | `rosters.yaml: prizes`. | — |
| H-121 | `default_store_kind` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-122 | `observation_deposit_mode` | DONE-IN-CODE | `data/fixtures.py` (17 files). | — |
| H-123 | `wound_harm_model` | DONE-IN-CODE | `data/fixtures.py`; A-8 changes what a wound costs a roll, not this write. | — |
| H-124 | `scenes_per_round=1` | DONE-IN-CODE | `loop/deliberate.py`. | — |
| H-125 | `body_step` | STILL-NEEDED | `data/fixtures.py:678` `body_step=10` (REM-52 shipped); the CR-22 re-derivation "by this row's own 'season or campaign' test" is unbuilt; `CL:U5d`: "H-125 is re-derived by CR-22". | SE, B12; Block 16. |
| H-126 | `pool_default` and the roll varying by person | DONE-IN-CODE | `seam/wrappers/pool.py:78` `faculty` (CP-T01-01 landed; `audits/25` L-09). | — |
| H-127 | `obstacle_default`, `obstacle_ceiling` | DONE-IN-CODE | `data/fixtures.py:451,454`. | — |
| H-128 | `scar_excludes_actor` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-129 | `body.changed` reads the anchor | DONE-IN-CODE | `loop/matter.py:699` `last_emission_of("body.changed", pid, written=True)`. | — |
| H-130 | `apply()` before `subject is None` raise | DONE-IN-CODE | LEAVE; unreached by any caller. | — |
| H-131 | gate window | DONE-IN-CODE | `state/world.py`; `T:test_gate_remove_person_requires_an_open_write.py`. | — |
| H-132 | re-stamp by `may_fill` | DONE-IN-CODE | CR-25 landed: `T:test_cr25_computed_establish.py`. | — |
| H-133 | `_req_confer` reads first hold | DONE-IN-CODE | LEAVE; `CL:U5d` "stays registered ... no builder produces the state". | — |
| H-134 | opportunity key shared by two seat-acts | DONE-IN-CODE | `decision/options.py:351-356`. | — |
| H-135 | closure branch unjudged by F9 | DONE-IN-CODE | LEAVE; `CL:U5d` "READ-B (H-135's reading)". | — |
| H-136 | self-transfer no-ops | SUPERSEDED | `CL:U5a`: "H-136, H-270, H-322, H-300, H-329 (acts formed that cannot succeed) | RESOLVED-BY `02_CHAR_offer_what_can_be_done.md`; `16_PESSIMIST_CORE_a_refusal_is_remembered.md`" (B10, B09). | — |
| H-137 | effect body outside the gate window | DONE-IN-CODE | CR-06: `T:test_tenure_gate_effect_body.py`, `T:test_tenure_diff_exact.py`. | — |
| H-138 | zero-valued key in `_shift` | DONE-IN-CODE | LEAVE (trigger-held); `CL:U5c` re-files it. | — |
| H-139 | removed Tenure invisible | DONE-IN-CODE | LEAVE. | — |
| H-140 | same-place `move` | SUPERSEDED | `CL:U5b`/`U5d`: "MIL-A Edits 1, 2, 4, 6 | H-329"; "KERN-SE §4" = `P:14_VERBS_MILITARY_A_movement`, `P:07_SE_kernel_repairs` (B12/B22). `same_place` absent in the tree. | — |
| H-141 | `earns` sentinel | DONE-IN-CODE | CP-T02-01 landed: `T:test_cp_t02_01_death_names_seats.py`. | — |
| H-142 | rungless seat purview | DONE-IN-CODE | Ruling (a) shipped; `CL:U5c` "wrongly filed". | — |
| H-143 | `NotYours` not caught | DONE-IN-CODE | `T:test_g3_not_yours.py`. | — |
| H-144 | remit change on an existing office | DONE-IN-CODE | CR-25 landed. | — |
| H-145 | bare `StateChange` admitted | DONE-IN-CODE | LEAVE; `CL:U5a` leaves it to NM-W9 (held). | — |
| H-146 | refusing pole read from data | DONE-IN-CODE | CR-21 landed (`T:test_cr21_cells.py`); `refusal_axis=None` armed nowhere (`data/fixtures.py:862`). [repair half not separately probed] | — |
| H-147 | `field_degree_bands` | DONE-IN-CODE | `rosters.yaml:875`; `T:test_march.py`. | — |
| H-148 | `field_casualty_model` | DONE-IN-CODE | `data/fixtures.py`; CR-24 `T:test_cr_24_winner_casualties.py`. | — |
| H-149 | `march_target_kinds` | DONE-IN-CODE | `loop/sides.py:108`; `T:test_march.py`. | — |
| H-150 | graded walls | DONE-IN-CODE | CP-T04-05: `T:test_cp_t04_05_graded_walls.py`. | — |
| H-151 | own-settlement march unopposed | DONE-IN-CODE | `T:test_march.py`. | — |
| H-152 | `total` arm `Lost` emits no `person.died` | DONE-IN-CODE | CP-T02-01 landed. | — |
| H-153 | `speech_kind_terminal_fault` | DONE-IN-CODE | `CL:U5a` "SUPERSEDED by the owning lane's closure (SC: U5c)"; no reader. | — |
| H-154 | `denial_detail_outperforms` | DONE-IN-CODE | Same. | — |
| H-155 | `told_drift_band=0.5` | DONE-IN-CODE | `loop/witness.py:217`. | — |
| H-156 | wrong-kind acts | DONE-IN-CODE | As M19. | — |
| H-157 | `teller_weight` | DONE-IN-CODE | `decision/options.py`. | — |
| H-158 | `default_upkeep` unread; no act pays upkeep | SUPERSEDED | `CL:U5d`: "H-158 no computed act pays upkeep | RESOLVED-BY `07_SE_population_census.md` (men under arms do not `work`, R-31); `04_MB_campaign_party_economy.md`". | — |
| H-159 | `oblige_term=4` | DONE-IN-CODE | `data/fixtures.py`; swept. | — |
| H-160 | shortfall reach limits | SUPERSEDED | `CL:U5d`: "J-1 does a chronic dearth speak | SUPERSEDED | D-69 (A: famine reports once; the never-stocked edge repaired); PES-SE-A edit 2" = `P:16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted` (B12). | — |
| H-161 | `bench_quorum` | DONE-IN-CODE | CR-34: `T:test_cr34_declared_disposal.py`. | — |
| H-162 | disposal edge degree | DONE-IN-CODE | `loop/effects_information.py::_eff_determine`. | — |
| H-163 | limit 3(a) larder knowledge | DONE-IN-CODE | CR-23: `data/fixtures.py:641`. | — |
| H-164 | `restore` identity | DONE-IN-CODE | `loop/effects_economy.py::_rise`. | — |
| H-165 | what shipped worlds do not reach | SUPERSEDED | `CL:U5a` (owning lanes' closures); `P:09_WR_world_motion` (B12), `P:14_VERBS_MATERIAL_C_works` (B12). | — |
| H-167 | `capacity_floor` | DONE-IN-CODE | `rosters.yaml`; `T:test_migrate_capacity.py`. | — |
| H-168 | `migrate` capacity refusals | SUPERSEDED | `CL:U5d`: "PES-SE-A edit 4 ...; OWED-SE §1 (R-SE-18)"; `P:14_VERBS_MILITARY_A_movement` (B22), `P:U5d_SE_owed_edits`. | — |
| H-169 | sheet limits | DONE-IN-CODE | LEAVE; no session cite. | — |
| H-170 | cohort weight 2 | DONE-IN-CODE | `cohorts.yaml`; A-44 changes the cast, not this default. | — |
| H-171 | cohorts in corpus; `Rung.envelope` writer | SUPERSEDED | `CL:U5a`/`U5d` OWED-SE §1; `P:07_SE_population_regrowth_B` (B12) writes `envelope`. | — |
| H-172 | round-stamp tripwire | SUPERSEDED | `CL:U5a` R-03: "RESOLVED-BY TDA §G; `16_PESSIMIST_CORE_no_stored_plan.md` (the skip and its test go)" (B03). | — |
| H-173 | sentence vs service `oblige` readers latent | STILL-NEEDED | v11's trigger (a computed `determine` executes) fired; no session cite; A-37 adds a release rule for imposed service. | SC, B27 (`05_SC_arrangement_rows_that_bind`); edit set the four readers of `oblige` kind in `queries/`; gate: a seeded reading of the four consequences with `determine` executing at 3 of 3 seeds; hash EQUAL (measure); tier sonnet. Block 12. |
| H-174 | jurisdiction follows presence | DONE-IN-CODE | `state/gate.py` `may_determine` clause 3; the stale docstring (`:773`) is one sentence for the next touch. | — |
| H-175 | `march` reaches a field | SUPERSEDED | `CL:U5a` (owning lanes' closures); `P:14_VERBS_MILITARY_A_movement` (B22), `P:14_VERBS_PHYSICAL_B_field_and_ruin` (B22), A-57/A-58. | — |
| H-177 | `told_weight=0.5` | DONE-IN-CODE | `data/fixtures.py:915`. | — |
| H-178 | `rank_gain=0.5` | DONE-IN-CODE | `data/fixtures.py:917`; dormant until H-181. | — |
| H-179 | `regard_gain` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-180 | stake factor marker | DONE-IN-CODE | LEAVE; field-less marker. | — |
| H-181 | rank ordering has no producer | STILL-NEEDED | CR-32 (Standing ladders as posts, `offices.yaml: ladders:`) is unbuilt (`grep '^ladders:'` 0; CR-32 absent in code). `P:30_WR_B_regimes_who_believes_whom` cites H-181 as a consumer. | FA/CHAR, B21 then B38; Block 18. |
| H-183 | `record_gain` | DONE-IN-CODE | `data/fixtures.py`. | — |
| H-184 | `combat_wounded_above` | DONE-IN-CODE | `T:test_combat_band_edges.py`. | — |
| H-185 | OUGHT `predicate` read by nothing | DONE-IN-CODE | LEAVE; `CL:U5a`/A1-30. | — |

## Table 8 — part 9 §5: work v9 names that is not a hole row (28)

| id | gist | disposition | evidence / cite | v12 target |
|---|---|---|---|---|
| V9-01 | `source:` names v9 in `lane_assignments.yaml` | DONE-IN-CODE | `grep -c valoria_master_workplan_v9 references/lane_assignments.yaml` = 0. | — |
| V9-02 | lane handoff rows naming a v9 file | STILL-NEEDED | 3 handoff files still contain `workplan_v9` (`grep -l registers/handoffs/*.md`); history rows may stay. | IN, B03 (hygiene); edit set `registers/handoffs/HANDOFF_*.md` Open rows; gate: `grep` finds only history rows; hash EQUAL; tier haiku. Block 8. |
| V9-03 | `ARC ENDS` NOT-COMPUTABLE string | DONE-IN-CODE | LEAVE with trigger. | — |
| V9-04 | where `leverage` comes from | DONE-IN-CODE | Carried in M2. | — |
| V9-05 | R-09 `measure:` in `headless` world seats no `capability` | SUPERSEDED | `U4_TRACEABILITY` §2 R-09: `P:U5a_capability_home_and_two_inputs` Part B gate (4): `python -m engine.season.harness.aperture 4 0` prints "two actors at different pools"; `master/instructions/IS_A_NINE.md` R-09. | — |
| V9-06 | run-to-run noise unmeasured | DONE-IN-CODE | No action (instrument deterministic). | — |
| V9-07 | IN-10 loop half; church ratchet bound | DONE-IN-CODE | LEAVE (H-25). | — |
| V9-08 | `domain_actions` contract `doc: null` | DONE-IN-CODE | LEAVE. | — |
| V9-09 | eight superseded ledger rows | DONE-IN-CODE | Written 2026-10-26 (`editorial_ledger_se_archive.jsonl`, see Table 5). | — |
| V9-10 | IN-47 cannot see scars/crises | DONE-IN-CODE | Stated limit; `T:test_rem30_character_sheet.py`. | — |
| V9-11 | IN-57 own-act screen arm D2 | STILL-NEEDED | As A1-05 (Block 5). | IN, B10. |
| V9-12 | combat reading felled 47 to 82 | SUPERSEDED | A-31 (longer fights) and `P:U5b_PC_rulings_in_the_fight` (B15) recalibrate the reading. | — |
| V9-13 | IN-38 remainder: 19 NPC cases without overlay | DONE-IN-CODE | LEAVE with trigger. | — |
| V9-14 | IN-36 flip | STILL-NEEDED | As §1a-M1res (Block 3). | See there. |
| V9-15 | IN-08 H3 violation predicate | DONE-IN-CODE | Carried in M14. | — |
| V9-16 | `intelligence-diplomatic` cells | DONE-IN-CODE | `T:test_cr21_cells.py`. | — |
| V9-17 | pins every verb step re-records | SUPERSEDED | `P:01_CORE_tests_one_golden_owner` (B02) makes one owner of the pins. | — |
| V9-18 | Layer-1 nodes F.20b, invariant 2, MOD 4, MOD 1 | DONE-IN-CODE | `rosters.yaml: fold_kinds`; `write_matrix.yaml:65-70`; `T:test_conviction_roster_single_owner` (tests/valoria); MOD 1 LEAVE. | — |
| V9-19 | retire three provenance drafts | DONE-IN-CODE | `find` finds no `candidate_pursuit_cells.md` or `candidate_affiliation_content.md` in the tree. | — |
| V9-20 | squad-engagement Status line; `MB-05r` dangling | STILL-NEEDED | `MB-05r` still appears in `research/by_lane/MB_mass_battle.md`. CR-02 (h) hygiene. | IN, B03; edit set the synthesis Status line; gate: `grep MB-05r` finds only history; tier haiku. Block 8. |
| V9-21 | parallel DELIBERATE map | DONE-IN-CODE | LEAVE with trigger. | — |
| V9-22 | [UNVERIFIED] D1-b #1 render = IN-37's | DONE-IN-CODE | Carried as a half-sentence. | — |
| V9-23 | birth-side consumer of `capacity` | SUPERSEDED | v11 closed it on ED-WR-0011 (no births); A-75 turns births on: `P:07_SE_population_regrowth_B` (B12), `P:23_STORY_B_a_house_continues` (B39). | — |
| V9-24 | two LEAVE rows (A9, ED-PC-0007) | DONE-IN-CODE | Live in `HANDOFF_MB.md`, `HANDOFF_PC.md`. | — |
| V9-25 | `sim-regression` job folds into `unit-tests` | DONE-IN-CODE | Carried by SC-05; `.github/workflows/valoria-ci.yml` still names it. [no session item: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` not searched for it] | — |
| V9-26 | superseding ledger rows owed at v9 adoption | DONE-IN-CODE | Written; handoff rows gone. | — |
| V9-27 | `requirements.yaml:997` says 44 rows | STILL-NEEDED | The verb table has 69 `verb:` lines now; the comment is stale again (`grep "44 rows"` finds none at `:997`: [UNVERIFIED] — the text moved). | IN, B02 (with `01_CORE_requirements_reading_record`); edit set the R-05 `measure:` comment; gate: no figure in the comment, a command instead; tier haiku. Block 8. |

## Carry-forward blocks

Each block is the v11 content-owner text, copied verbatim from the cited cell, so the v12 author need not reopen v11. Where v11 has no INSTRUCTION/WHERE/FALSIFIER/GATE entry for the item (the position's own entry is in another part, lanes E1/E2/E4/E5), the block copies the hole row's "what closes it" and the DECISION text, and the v12 target column of the table row names the instruction to write.

**Block 1 — CR-36 / CR-37: widen succession and revocation; the joint-concurrence deposition (M8, §1b-3, A2-14).** Source: `workplans/valoria_master_workplan_v11_part6.md` §1 M8 DECISION and §1b item 3 DECISION. M8: "**DECISION — TAKEN, step 3 (H-132, H-144: step 4); CORRECTED by Jordan's 2026-10-26 request (step 1: his words select option (b) under M8's 'Jordan to correct' clause, and M8's own revert names the form; the trigger did not fire).** (a): no seat with no revocation basis is stripped; `depose` is PARKED, not cut (trigger: H-90's sovereign power is built, or Jordan rules on the Royal Deposition conjunction of his 2026-08-18 Crown Claim precedent); H-132 (b) and H-144 (b) build inside CR-25. `[ASSUMPTION; medium; Jordan to correct; revert: a third `revocation_bases` value for the throne; restore the two clauses]` Corrected 2026-10-26 (Jordan: 'Canon needs ... a joint-concurrence deposition'; 'resolve all of these'): revert taken; `off_king.revocation` `joint_concurrence` (CR-37; H-L0-9 applied in PR #507); `depose` CLOSED, answered by `revoke` [ASSUMPTION; medium; Jordan to correct; revert: off_king null, depose PARKED]. The revocation strips the throne only: the deposed King keeps `off_duke_valorsmark` until his death or his release (CR-37). The Royal Deposition conjunction is not ruled; it is restated (the second decision round, item 5, §1b). H-132 (b) and H-144 (b) stay inside CR-25." Item 3: "**DECISION — TAKEN.** An elected seat is filled by its faction's bench (`determine`), a contested succession by the throne's bench, a `nominated` seat by `confer` on a body's held `resolution`, and the throne is revoked by the Holy See's `revoke` on a carried motion; Valorsmark passes with the line through one claim (the heir's `succeed` opens every vacant seat whose `successions` value is his title, then closes the title, in one act; if that write does not execute, CP-T09-06's `appointed` stands); Hafenmark stays null. ... `[ASSUMPTION; medium; Jordan to correct; revert: per position: CR-35, delete the rows, the arm and the wiring, `elected` seats falling back to `confer`; CR-36, the clerk back to `appointed`, dropping `nominated`, the `resolution` kind and the Record disposal site; CR-37, off_king null, depose PARKED; IN-61, no FILLED_BY (every basis passes `confer`) and the claim opens the throne only; CP-T09-06, `appointed`; the contest polarity, party-as-opponent on every row]` ... Limits named: a computed `open_case` carries no arrangement or petition (H-80, §F1), so the new routes have realm reach 0 and their realm readings are residues." **Session amendment to apply (not in v11):** `P:06_FA_seat_terms_by_body_B` edit 3 (CR-37's sentence reads "deposition is the turnover of a life seat" and excludes the Confessor, A-36; every other Church officer's turnover is the head's strip by a resistible draw, A-35).

**Block 2 — M38: PR #527's RJ-calls, its two Layer 1 hunks, the marquis question.** Source: part 6 §1c table, M38 row: "CR-38 as written (`-04`) until #527 merges; canon's count and countess stand (no marquis)". Session interim: A-76, "any working realm bench stands in now, built switchable".

**Block 3 — M1's residue: `foreign`/`guards` defaults and the march frequency (§1a-M1res, V9-14).** Source: part 6 §1a, M1's residue row, answer column: "`foreign`: ANSWERED by Jordan, ED-IN-0310 (2026-11-04), ON by default. `guards`: CONFIRMED AT THE DEFAULT (ED-IN-0301), kept off by ED-IN-0310 until CP-T09-07 (b)'s union lands (before it the flip musters nobody); TAKEN by the ladder on 2026-11-04 (ED-IN-0317: ships ON once CP-T09-07 (b)'s union lands, its own declared mover in B10-17; `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]`). The march frequency (first scene in 7 of 80 seeds, H-233) is ANSWERED in kind by Jordan, 2026-11-04 (ED-IN-0317): a march needs a casus belli, civil war excepted (a held design piece, its carrier `[GAP]`, IN-36), and for testing a cap of one march per season into each territory (built under IN-36 in B10-17)". **Session revision:** A-58/A-74 make a casus belli context, not a precondition (item J-E3-1); only the cap and `guards` ON survive.

**Block 4 — IN-30 / `faction_props` (§1a-(c), IN-30, SE-05, FA-02).** Source: part 8 row H-186, "what closes it": "BUILD (IN-30) after one of: seize on unheld land, `march` classed `Rung`, a question source; plus design choices (adjacency, streak, promotion, emerged-faction identity) that may need a ruling when reached [INFERRED]. Decided by the second decision round, item 4: IN-30 builds `faction_props` (one identity owner that admits emergence: the rostered faction Propositions plus every Proposition in the creed shape) and the creed `utter`, its occasion CP-T09-01's leaver [ASSUMPTION; medium; Jordan to correct; revert: `faction_props` returns `FACTION_BY_PROP`'s keys; the creed term dropped]; CP-T09-04's unpeopled clause makes `terr_T15` takable [ASSUMPTION; medium; Jordan to correct; revert: drop the clause]; the streak and contiguity triggers are not carried (a clock; no carrier). **GD-3 FAIL, recorded:** an emerged creed cannot `seize` (a seat's faction is the authored `Office.faction`), which fails GD-3's violation test (`canon/04_game_design_constraints.md:29`); ... the fix (a seat serving an emerged creed) or an amended GD-3 is `-05` §1a question (c), blocking nothing built now. Promotion is CR-39, HELD on CR-38 (B10-Z)". §1a (c) question text: "An emerged creed cannot `seize`, which fails GD-3's violation test (`canon/04_game_design_constraints.md:29`). Let a seat serve an emerged creed (every same-faction rule then re-reads `seat_faction`), or amend GD-3?" Answer: "CONFIRMED AT THE DEFAULT (ED-IN-0301)": IN-30 ships with the GD-3 FAIL named on H-186.

**Block 5 — CR-10: IN-57's own-act screen, arm D2 (A1-05, V9-11).** Source: part 7 A1-05 reason: "The screen exists by the user's ruling ED-IN-0294 (`editorial_ledger_in.jsonl:69`, opened), whose stated problem is a claim about the person's AMBITION subject that his own act occasioned, ranking in TIER 0. Arm D2 (tier-1 echoes spared, tier-0 still demoted) is that scope exactly; D1 restores the no-screen failure the ruling exists to stop (80.4 % own-act echoes, per the J.2 row). Measured on one seed only. `[ASSUMPTION; medium; Jordan to correct]` (a reading of a ruling's scope)"; revert: "screen every tier (as built at IN-57). Reopen if a three-seed reading reverses D2's R3 figures." Part 9 §5 row: "BUILD | CR-10 (B10-09)". [UNVERIFIED whether CR-10 is already built: the tree's code mentions CR-10 61 times but I did not open the screen.]

**Block 6 — CR-07: cut the inert `scale:` column (A1-46, H-89).** Source: part 9 row H-89, "what closes it": "EDIT, unowned: apply A1-46. Remove `scale:` and `scale_note` from the 13 rows, `VerbRow.scale` and its load check, and the guard test over the inert column (`tests/test_season_shape.py:5281`). Exit: loader loads, that test file green The edit list also removes the `.scale` asserts at `test_season_shape.py:5386-5387` and the stale 'nine rows' header at `verb_table.yaml:66-79`." A1-46 reason: "`verb_table.yaml:66-75` (opened) already states the answer to Jordan's scale question: scale is *'THE SCOPE OF THE SEAT BEING EXERCISED -- `Act.via.scope` -- not a column on the verb. The key is retired when `Act.via` carries the scope'*". **Session addition** (`P:U5a_CORE_owed_edits` §E row 3): first give the registry-derived seat `off_npc_084` a scope at its owner; re-run CR-07's pre-flight (seeds 0-2, two seasons; `Act.via.scope` was missing on 19 of 309 acts); then the deletion, and correct `data/verbs.py:129-137, 619-621`. Count rows by symbol at the edit (15 in the tree, 13 in v11). Falsifier: a planted `scale:` key loads.

**Block 7 — IN-14: more rounds; narrow the `budget` hold count (A1-50, H-10, H-92, IN-14, CT-1).** Source: part 9 row H-10: "BUILD: rounds = max budget over the living, `scene_budget` the floor (shape delegated-ruled MORE ROUNDS)"; row H-92: "BUILD the narrowing and re-take the `test_n3` floor (IN-14). Witness half: ACCEPT [ASSUMPTION; medium; Jordan to correct; revert: landholders are not document-key witnesses of a rung change], R5 intends the channel". Session gating (`CL:U5a` R-22): "lands only after FI-02's traffic arm, with `test_n3`'s `attempt_cases` read before and after".

**Block 8 — hygiene bundle (hash EQUAL).** (a) A1-80, `RemoteTrigger`: part 6 §3: "`CLAUDE.md` §11 says to add a new self-scheduling primitive to `REQUIRED_DENY` once one is observed to arm or re-arm a routine; v9 marks that observation as never made. Acting on it would edit `.claude/settings.json`'s deny-list, which is a human-approved change; **no agent edit is proposed here**, and the item is listed for Jordan only." (b) A1-81: "re-word the `succeed` designation nodes to the title route ... Lands with IN-61's build so the text describes the carrier built." (c) A2-40: "The edit lands at citing sites, never the frozen archive": `harness/storybar.py`, `soak.py`, `populated.py`. (d) ER-C4: "a one-off comment fix; rides the next commit that edits `rosters.yaml` (R8: B10-09)". (e) ER-GF9: "dead constants crossing into the port contract: B10-03's export hunk (DEF-9 deletes the capture)". (f) ER-GF10: "a one-off docstring or code fix; rides the next commit that edits `attempt_leap`". (g) V9-02: "CR-02 (g): re-point each such row to v10; rows that cite v9 as history stay; dated record text in `requirements.yaml` stays". (h) V9-20: "CR-02 (h): 'open: MB-07r (J-18 (A) built, shipped OFF), MB-08 (LEAVE)'; drop `MB-05r`". (i) V9-27: "`requirements.yaml:997` (R-05's `measure:` comment) says the verb table has 44 rows; it has 56 | EDIT | CR-02 (h), at the next batch that touches R-05" (the tree has 69 `verb:` lines).

**Block 9 — H-222: person-predicate claim writer (A1-87).** Source: part 8 row H-222: "BUILD (a writer of person-predicate claims through the channels)"; A1-87 reason: "A deposit through the existing channels (AX-7, `01_AXIOMS.md:113-120`, opened: no unmediated world truth), owned by the successor to 19_PLAN step 19 (superseded by the verb-coverage proposal, ED-IN-0288, per G2). The game (pressure surfaces as a question about the tellers) is the same whichever channel carries it. `[ASSUMPTION; medium; Jordan to correct]`"; revert: "pressure is not person-keyed (remove step 23's consumer)".

**Block 10 — A2-23: a treaty binds the signer.** Source: part 7 A2-23: "`[ASSUMPTION; medium; Jordan to correct]` The signer. Verified ratified Layer 1 `architecture/meta/04_CODE_ARCHITECTURE.md` §B.7 (:322-329): `Seat := (...)` with 'NEVER: who holds it · who serves it · a modifier of any kind'; edges are persons' Tenures. F09 §6 (verified) answers the same at step 5: 'a successor re-seals'. A seat-bound treaty would need a carrier §B.7 denies." Revert: "Jordan rules treaties bind the seat — then the treaty edge's object becomes the Seat (`oblige : Person → Seat` exists, §B.7 call 2) and survival across holders is read there". A-20 (war lives in the seats that wage it) is the session ruling that may reopen it.

**Block 11 — CR-29: the event-kind reach channel, `chronicle`'s paired deletion, FA-01's trade-demand clause (A2-43, H-214, H-234, H-224, ED-IN-0298, FA-01).** Source: part 8 row H-234, "what closes it": "BUILD (CR-29, released from M11): commit (1) a `reach` roster row keyed on event kind, shipped with an empty map, its §C.6 row landing only with the channel's code and first reader; commit (2) the kinds it carries (the coercive kinds this row names among them) and `chronicle`'s deletion. Falsifier: NPC-090's `person_q.stability` at a settlement rung non-zero in at least one of seeds 0-2 of `build_realm(S, foreign=True)` over four seasons". Row H-214: "BUILD (CR-29, released from M11): the event-kind reach channel (commit (1), EQUAL, empty map), then `chronicle`'s paired deletion (commit (2), a declared mover re-reading R-07 conjunct (1); its controls drop `told_by` to 0 with the map emptied and keep realm reach for `tenure.closed` and `person.died`)". Row H-224: "MEASURE (window arms) once a shortfall input reaches governors". Session content to add: A-32 ("One reach row for seat changes": realm-wide shipped, B built as the test arm) and A-33 (a death reaches by presence, trail and telling, apart from the seat's news); `P:08_FI_01_claim-sourced-referents` (B11) depends on CR-29, so it lands before B11.

**Block 12 — small measures and one S defect (H-195, H-199, H-173, GV-G12, ER-JF10).** H-195: "MEASURE (M0g >= 5%) then BUILD; matters only under `declared` polarity, which CR-16 ships (B10-07b)". H-199: "RULING (Jordan corrects 0.5 and chooses one ladder) [INFERRED]"; part 8 §8: "A new CR position in B10-13 to pick one ladder (an S-test defect that ladder step 5 may take) [INFERRED]; Jordan's magnitude correction stays optional." H-173: "MEASURE the four consequences now: the row's own re-read trigger has fired (`determine` executes in computed play, 3 of 3 over three seeds, `-02`:46). The ACCEPT stands for the ruling only". GV-G12: "closed for the readers; `church_standing` is unchecked and unowned [INFERRED]". ER-JF10: "pursuit weights not normalised (Saemund sums 1.31) | REM-05 (B10-01) and the goal-weighting dial (M1)".

**Block 13 — H-217 / SC-04: the `succession` row (CR-35).** Source: part 8 row H-217: "BUILD in CR-35 (the second decision round, item 3): the `_disposal` `hold` literal, the gate's election arm, the petition operand (the seat is the docketed petition's `terms`; no new operand), and the `succession` row seeded at `disposal: declared` [ASSUMPTION; medium; Jordan to correct; revert: no rows]; the row closes at CR-35's commit; H-L0-8 is applied in PR #507, so CR-35 builds the arm and the rows in the ordinary way; the rows' shipped state is whatever the position's own falsifier and control say. IN-61 keeps `FILLED_BY`'s first narrowing and the claim write; this row's part, the contested-succession arms and the tripwire re-record left it for CR-35".

**Block 14 — stale measurements and IN-12 / IN-58 residues (H-225, H-227, IN-58).** H-225: "BUILD (H-209's options for cause 1; an Event-bound membership record for cause 2)" — `CL:U5d` §6 calls the measurement stale; re-take first. H-227: "BUILD (a petition becomes a held-writ occasion or `writs_held` widens; IN-09's files)". IN-58 (part 8 §4): "CARRIED (as the same handle, in -03) | B10-09"; blockers named in part 6 M1: "IN-58's sworn half; the RS-23 petition conjunct in IN-12".

**Block 15 — GO-01: the Godot version owner.** Source: part 8 §4: "CARRIED (as the same handle, in -03); released whole: the version owner only, read by `tools/export_game_constants.py`, once `ED-GO-0002` is on `main` (B10-01's entry action)". Tree: `registers/editorial_ledger_go.jsonl` ED-GO-0002 is `resolved` and rules 4.7; `tools/export_game_constants.py` does not read it.

**Block 16 — CR-22: hunger magnitude by a stated rule; `body_step` re-derivation (H-11, H-125).** Source: part 9 row H-11: "BUILD (CR-22, MEASURE then BUILD): M6 taken (a) (delegated, step 5), the per-head need chosen by a reading rule (the gentlest of M-H2's arms at which REM-50 reads a settlement below `fed` after season 1 at every seed, under the season-0 floor rule); this row gains the chosen arm and the rule [ASSUMPTION; medium; Jordan to correct; revert: another arm is one value]". Row H-125: "BUILD: M6 taken (a); REM-52 sets the one data value to 10, its own declared-mover commit in B10-05 [ASSUMPTION; medium; Jordan to correct; revert: 0]; CR-22 re-derives `body_step` by this row's own 'season or campaign' test (10 is a delegated pick). The 67 arm skips the bottom band, per the SE-03 test the row cites". Session: `P:07_SE_ground_and_granaries` (B12) "amends three open positions rather than adding one: CP-T08-02 (endowment by ground), CR-22 (hunger binds) and the open ruling row H-303".

**Block 17 — CR-09: `own_purview` through `purview_reaches` (H-101).** Source: part 9 row H-101: "[GAP, scoped to `own_purview`]: route `queries/world_q.py::own_purview` through `state/gate.py::purview_reaches` (or one shared clause walk) so the set form equals the predicate where a seat-holder has sworn an `oblige`. `faction_q.purview` has no game caller, so it is left. A declared hash mover: `own_purview` feeds `reach`, `attention_key` tier 1 and `larders_in_purview`, so it moves question formation, and it imports the clause's recorded unbounded over-reach. Exit: a hand-built world (as `test_in40_oblige_purview.py`) where the swearer's ground lies outside the sworn seat's own ground" (that test file is not in the tree).

**Block 18 — CR-32: Standing ladders as posts; `rank` producer (H-181).** Source: part 9 row H-181: "BUILD (CR-32: Standing ladders as posts on seats in `offices.yaml: ladders:`; a visible ladder post shown in `marks`, only where the ladder's livery names a visible mark; `rank` compares within one scale only, a ladder post never against a title). Its producer reads CR-30's `marks` carrier; builds with its reader in the same commit, as this row required".

