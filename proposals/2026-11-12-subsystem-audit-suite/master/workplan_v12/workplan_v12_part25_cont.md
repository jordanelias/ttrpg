# Workplan v12 — part 25, continued: batch B34-go-surface

## Status: PROPOSED (the continuation of `workplan_v12_part25.md`, `V12_STRUCTURE_part2.md` §4.1's `_cont` rule; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

Words, paths and forms as the head of `workplan_v12_part25.md` states them.

---

## Batch B34-go-surface · lane GO · wave W14 · step S14 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B34-go-surface
IN-FLIGHT ROW: registers/handoffs/HANDOFF_GO.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B03-hygiene
GATE: Batch B10-character
GATE: Batch B21-fa-governance
GATE: Batch B24-sc-hearing
GATE: Batch B16-pc-round                                                  (added by this part, not in `V12_STRUCTURE.md` §2.1: UNDECIDED U1)
REQUIREMENT: R-04.c1 (the sheet) → the creation-sheet test green (`IS_A_NINE_part2.md` §12.2, row B34): `engine/season/tests/test_seat_holders_from_ledger.py::test_creation_sheet_marks_cohorts_and_holdings` and `engine/season/tests/test_season_shape.py::test_creation_sheet_shows_holdings_for_a_seat_holder` pass on the closing tree; the conjunct's `reading:` record is written at B34.99; `status:` is not edited (A-114).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_play_surface.py engine/season/tests/test_play_surface_own_outcome.py engine/season/tests/test_scene_contract.py engine/season/tests/test_seat_holders_from_ledger.py engine/season/tests/test_management_orders.py engine/season/tests/test_governance_spine_play.py engine/season/tests/test_scenarios_runner.py engine/season/tests/test_go07_canonical_digest.py engine/season/tests/test_rem30_character_sheet.py engine/season/tests/test_rem31_grid_suspension.py engine/season/tests/test_season_shape.py tests/valoria/test_explain.py -q` → all pass;
  `python -m engine.season.harness.play_surface --seed 0 --person p_npc_001 --seasons 1` → exit 0, a transcript whose `content_hash` equals the plain run's at seed 0 (GO-B gate 1), and again at seeds 1 and 2;
  `python -m engine.season.harness.play_surface --scenario valley --seed 0 --seasons 2` (or `--scenario season` if `valley`, B12c's, is not yet registered: B34.20) → ends with an `ENDING` line (twelve seasons in the source, A-114);
  `python -m engine.season.harness.scene combat.fight --fixture duel --seed 0` → exit 0, a record; `python -m engine.season.harness.scene social_contest.roll --fixture roll --seed 0` → a record whose terms sum to its obstacle and one of the four degrees (B34.17);
  `python tools/export_engine_params.py --check` → exit 0; `python tools/export_battle_orders.py --check` → exit 0 (B34.07);
  the C1A_02 W1 reading (B34.22);
  (Patched: P-29) `U5a_CORE_owed_edits` §I's falsifier, moved here from B03.65 (§5.8): `grep -rn "footprint(\|density(\|sovereign_fraction(\|provinces_of(" engine/season --include=*.py` outside `tests/` → finds, besides the definitions, `faction_q.standing`'s composition (B03.65) and its two callers' call of `standing` (B21.72's per-season print, B34.04's faction view); "still finds only definitions" is the defect;
  `python -m engine.season.harness.interactions` at seeds 0–2, two seasons → the count of persons named through a classed referent and outside the closure = 0 (B34.23, gate 1 of `16_PESSIMIST_GO_the_offer_names_what_is_held`);
  the realm content hash of `build_realm(s)` after one season at s = 0, 1, 2 → moved by B34.23 and B34.24 (and B34.01 if its branch 2 was taken) as declared, every other item equal (`reading @<sha>` of B24's and B21's merged close, the step's base);
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines, quoted; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core, harness, an exporter: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed: a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, R-04.c1's reading with its tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; B34.99 writes R-04.c1's `reading:` record; `status:` is not edited (`IS-A-12`).
RE-PIN: once, at B34.99: the realm pins in `engine/season/tests/_realm_goldens.py` and the seeded goldens the movers reach ("One re-record of the seeded goldens, said plainly", `16_PESSIMIST_GO` gate 5), read against the step's base (`reading @<sha>`); the commit says "re-pin: ledgers at build and the questions formed from them (B34.23, B34.24)" and, if B34.01 took branch 2, "and the doer's own-outcome claim".
IDS: ED-GO 0; H 1 (B34.24's NUMBER row for `holder_known_chance`, block slot 1)
DIALS AT CONTROL: `rosters.yaml: management_orders` = `[]` (B34.10); set by: none in v12 (the list is CL-MGMT's content, held: `V12_STRUCTURE_part3.md` §7.8); target: none stated (A-104 names examples, not a list), so B98 writes it `BLOCKED (content: CL-MGMT's list)`. `holder_known_chance` ships at its stated values, not at control (B34.24: a declared mover in this batch, revert 1.0 everywhere).
EXPECTED RED UNTIL B34.99: the realm pins after B34.23 and B34.24 (and after B34.01 in branch 2), under `[skip ci]`.
UNDECIDED:
  (U1) **B34's `after` list** (`V12_STRUCTURE.md` §2.1: B00, B01, B02, B03, B10, B21, B24) does not hold B16, but `IS-PC-01` step 6 (B34.15) names `duel_scene.build`, which B16 creates (B16.11), and `IS-DICE-01` (B34.17) builds on it. Taken: `GATE: Batch B16-pc-round` is added here. It does not lengthen the graph (B16 is W13, B34 W14; B16 closes at S13 in §2.3's schedule, before B34 opens at S14); H1 and H2 recompute B34's slack.
  (U2) **`IS-MB-01` step 4** (`harness/scene.py::FIXTURES["field"]`, `play_surface --scenario field`) needs `harness/field_scene.py`, which `04_MB_playable_field_scenario` creates in **B20** (W16, S16), after B34. Carried here it is a back edge. Taken (`V12_STRUCTURE_part4.md` E-8's rule, "the dependency wins"): B34.18 is a POINTER and the step lands in B20 after `IS-MB-01` steps 1–3, with `harness/scene.py` already on B20's base (B34 closes at S14). **For lane A30 and H2:** B20 gains `GATE: Batch B34-go-surface` (no wave change: W14 < W16) and an item carrying the step's text (copied in B34.18).
  (U3) **`01_CORE_one_scene_contract` names two later batches.** (a) The nesting cap `Fixtures.contest_nesting_cap` and `Refusal(depth_cap)` (A-4, A-72; U1 ledger P-01) are created with `nested_entry` in B30 (UPR §1, as B15's author placed it, `workplan_v12_part18.md` DIALS line note (1)). Taken: B34.15 builds `apply=False` through `seam.contest` with the tree's `max_depth` and its typed refusal (`seam/contest.py::ContestError("max_depth reached")`), and the A-72 test (`test_a_duel_round_called_from_a_battle_may_not_call_a_third_scene`) moves to B30's nesting item (§5.8: an arm that reads a later item's effect moves there). (b) The `engaged` clause of `28_CORE_scene_access_A` (B28, S17) is applied by the fold when it lands; `play(…, apply=True)` runs the fold, so nothing here waits on it. Both are written for H2's serial-edge table as edges not taken.
  (U4) **`CreationRow.holdings` has two sources** (`11_GO_fidelity_and_campaign_modes` exact edit 1; `16_PESSIMIST_GO` §4). Taken: one field, landed once at B34.06 in `16_PESSIMIST_GO` §4's shape (`creation_sheet(persons, holdings_of)`, the caller's reader), because that shape keeps `decision/` free of `World` whether or not `OwnStateReader` answers Tenures; B34.12 adds `cohort` and the test.
  (U5) **The transcript's stop rule has two sources**: `U5a_CORE_owed_edits` §F (stop on a realm ending only when the seated person has no continuation; print "the ending, and the reveal") and `IS-B3-GO-02` (print `ENDING <name> <kind>` and stop; `realm_ended` split by the seat's side). Taken (changes less): B34.19 lands §F's three stop rules **without the reveal** (`reveal` is `30_GO_F`'s, B38, `IS-B3-GO-04`: "B34 builds none"), and B34.20 amends the printed line and the reader's names; with a continuation the run records the ending and plays on (§F rule 1), so `ENDING` is printed when the run stops.
  (U6) **Test files.** `IS-B3` part 2 §6.1 (Sonnet check, ladder step 4) decided one file, `engine/season/tests/test_play_surface.py`, and `test_play_surface_own_outcome.py` beside it; GO-B's `tests/valoria/…` paths are not used. `11_GO_player_surface_contract` §2 names `tests/valoria/test_explain.py`: no ruling moves it, so it stays.
  (U7) **`Scene.cost` is not an encoding mover.** `V12_STRUCTURE.md` §2.2 marks B34 "encoding: `Scene.cost`" (D-04). `IS-B3-GO-07` changes a method's signature, not a field, and `state/world.py` names no `Scene` (grep), so `World.content_hash()` does not reach it; B34.10 is EQUAL at control (the empty list), as its source says.
  (U8) **The combat seam's stream** (`01_CORE` edit 4: "the combat seam's `random.Random(seed)` … is replaced in the same edit") was keyed by B06 (`workplan_v12_part10.md`, the contest call's `draw_factory`); the source's own fallback applies ("a mover only if B06 has not already keyed it (then it is B06's)"), so B34.15 makes no stream edit and moves nothing.
C(B34-go-surface): this batch's entries; the plan's head parts; `proposals/11_GO_player_surface_contract_B.md` (read whole: B34.01 to B34.04 copy its dataclasses); `proposals/11_GO_player_surface_contract.md` §2; `proposals/11_GO_fidelity_and_campaign_modes.md`; `proposals/16_PESSIMIST_GO_the_offer_names_what_is_held.md`; `proposals/01_CORE_one_scene_contract.md`; `proposals/U5a_CORE_owed_edits.md` §F; `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` W1; `master/instructions/IS_B3_FA_SE_WR_GO.md` (`IS-B3-FA-02`), `_part2.md` §6 (`IS-B3-GO-02`, `-03`, `-07`); `master/instructions/IS_B1_PC_MB_DICE.md` (`IS-PC-01` step 6), `_part2.md` (`IS-MB-01` step 4, `IS-DICE-01`);
  `engine/season/decision/sheet.py`; `engine/season/decision/choose.py` (`make_ranker`, `score_terms`, `pack_scenes`, `_sample_order`); `engine/season/decision/options.py` (`opening_set`); `engine/season/queries/person_q.py` (`LedgerReader`, `OwnStateReader`); `engine/season/queries/world_q.py` (`goal_referents`, `_goal_referents`, `seats_named`, `questions_for`, `endings_reached`); `engine/season/queries/inputs.py` (`PlayHost`, `CombatRoundView`); `engine/season/state/carriers.py` (`View`, `Claim`, `Candidate`, `Scene.cost`, `PersonInterior`); `engine/season/state/world.py` (the GO-07 encoder, `decode`); `engine/season/loop/witness.py` (`witness`); `engine/season/loop/deliberate.py`; `engine/season/seam/contest.py` (`contest`); `engine/season/seam/wrappers/_entry.py`, `combat.py`, `sigma.py`, `mass_battle.py`, `fieldwork.py`; `engine/season/harness/play_surface.py`, `scenarios.py` (B11), `governance_spine.py`, `duel_scene.py` (B16), `headless.py`, `military_menu.py`, `interactions.py`; `engine/season/boot/realm.py` (B03c); `engine/season/data/fixtures.py`, `data/rosters.py`; `engine/season/rosters.yaml`; `engine/season/hole_register.yaml` (H-203); `modules/combat/wrapper.py` (`ROUND_CHOICES`), `modules/combat/vocabulary.py` (`APPROACHES`); `modules/social_contest/roll.py`; `engine/dice_engine/sigma_leverage.py` (`band_odds`); `tools/export_engine_params.py`, `tools/export_battle_orders.py`; `registers/handoffs/HANDOFF_SC.md`;
  instruments: `play_surface`, `scene`, `interactions`, `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; `engine/season/tests/_realm_goldens.py`; the closing SHAs of B03, B10, B16, B21, B24; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_GO.md`, the skill and `methodology-close`).
COST: small builds and edits; producer `valoria-author` on `sonnet`, `high`; `opus` on B34.01's branch decision if branch 2 is taken (GO-B "Lands it") and on the three chances of B34.24 (its own "an `opus`-or-Jordan judgment"); IN and CHAR review `decision/` and `person_q`; the close's terminal critique `opus`.
EST: 12 h [estimate: `V12_STRUCTURE.md` §2.4's formula over 22 committing positions (0.4 h × 22 + 2.5 h) ≈ 11.3 h, plus the 2,000-seed scene test of B34.17]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B34.01 | the gate tests first; the doer holds his own act's outcome | GO-B "Build order" 1–2, §3 | BUILD | EQUAL, or MOVER(behaviour) in branch 2 | Batch B24, Batch B10 |
| B34.02 | `Situation` and `Offer`: what is in front of him, what he may do | GO-B §1, §2 | BUILD | EQUAL | B34.01 |
| B34.03 | `account` and `dossier`: what he has learned, what he holds about one subject | GO-B §4, §5 | BUILD | EQUAL | B34.02 |
| B34.04 | the transcript: one runner for every playable scenario | GO-B §8 | BUILD | EQUAL | B34.03; Batch B11 (via B24) |
| B34.05 | `explain`: a value's derivation from his own claims | SURF §2 | BUILD | EQUAL | B34.02 |
| B34.06 | a creation row shows the seat's holdings; no decider means his own policy | fidelity edits 1–2, with `16_PESSIMIST_GO` §4's shape | BUILD | EQUAL | B34.04 |
| B34.07 | each closed choice set exported with a name and a line of text | fidelity edit 3 | BUILD | EQUAL | B34.06; Batch B16 |
| B34.08 | fork C closed; the difficulty overlay and the holdings test | fidelity edit 4, gates 3–4 | BUILD | EQUAL | B34.07 |
| B34.09 | the spine's menu is the `Offer` | `IS-B3-FA-02` | BUILD | EQUAL | B34.08; Batch B21 |
| B34.10 | a management order costs no scene budget, at control | `IS-B3-GO-07` | BUILD | EQUAL | B34.09 |
| B34.12 | a creation row marks cohorts | `16_PESSIMIST_GO` §4 | BUILD | EQUAL | B34.06 |
| B34.15 | the host names a decider per module role; the party test once; a module's scene alone | `01_CORE` edits 1, 2, 4; `IS-PC-01` step 6 | BUILD | EQUAL | B34.04; Batch B16, Batch B24 |
| B34.16 | the player is shown all his questions | `01_CORE` edit 5 | BUILD | EQUAL | B34.15 |
| B34.17 | one roll, played | `IS-DICE-01` | BUILD | EQUAL | B34.15 |
| B34.18 | the field as a scene fixture | `IS-MB-01` step 4 | POINTER (Batch B20) | — | — |
| B34.19 | the transcript stops | `U5a_CORE_owed_edits` §F | BUILD | EQUAL | B34.04 |
| B34.20 | a run's ending reaches the surface, with its kind | `IS-B3-GO-02` | BUILD | EQUAL | B34.19, B34.08 |
| B34.21 | a snapshot names its scenario; resume | `IS-B3-GO-03` | BUILD | EQUAL | B34.20 |
| B34.22 | the character sheet's spaces have a caller | `17_CENSUS_C1A_02` W1 | READING | — | B34.04 |
| B34.23 | a goal's seat-holders are read from his own ledger | `16_PESSIMIST_GO` §1, §3 | BUILD | MOVER(behaviour) | B34.12, B34.20 |
| B34.24 | the builder seeds who knows each seat's holder, by a draw | `16_PESSIMIST_GO` §2 | BUILD | MOVER(behaviour) | B34.23 |
| B34.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | every position above |

Order notes. U3 §1 item 34 orders GO-B → SURF → fidelity → `16_PESSIMIST_GO` → `01_CORE` → U5a §F → C1A_02 W1; `V12_STRUCTURE.md` §2.2 places `IS-B3-FA-02` and `IS-B3-GO-02` after fidelity, `IS-B3-GO-07` after FA-02, `IS-DICE-01` after `01_CORE`. U3 §1.2's B34 row makes `01_CORE` need only GO-B, so `16_PESSIMIST_GO`'s two movers are moved to the batch's tail (B34.23, B34.24), with its hash-EQUAL §4 earlier (B34.12): §5.9, hash-EQUAL items first where the source's order allows (the file's own order, §4 → §1/§3 → §2 → re-pin, is kept). Handles B34.11, B34.13 and B34.14 are not used (handles need not be contiguous; none is cited).

SERIAL EDGES: within the batch: B34.01 → B34.02 → B34.03 → B34.04 (GO-B's build order: tests, §3, then the readers, then the runner); B34.02 → B34.05 (`explain`'s first values are `OfferRow`'s terms); B34.04 → B34.06 → B34.07 → B34.08 (fidelity after GO-B; gate 3's test runs the transcript); B34.08 → B34.09 → B34.10 (`IS-B3-GO-07` after `IS-B3-FA-02`); B34.06 → B34.12 → B34.23 → B34.24 (`16_PESSIMIST_GO`'s own order); B34.04 → B34.15 → B34.16, B34.17 (`IS-DICE-01` after `01_CORE` edit 4); B34.04 → B34.19 → B34.20 → B34.21; B34.20 → B34.23 (the realm-ending reader lands before the mover, so B34.20's tests read an EQUAL tree); B34.99 last.
  With other batches, by file (U3 §5.1's rows, in v12's step order): `decision/sheet.py` B10 → **B34** → B38; `harness/play_surface.py` B11 → **B34** → B41 → B38 → B39; `queries/inputs.py` B16, B24 → **B34** → B19 → B22 → B35; `decision/choose.py` B16 → **B34** → B28 → B38; `loop/deliberate.py` B09 → **B34** → B28; `state/carriers.py` B21 → **B34** → B32 → B38; `queries/person_q.py` B24 → **B34** → B25; `queries/world_q.py` B21c and **B34** in S14 (different functions) → B25; `data/fixtures.py` B24 → **B34** → B19; `rosters.yaml` B21c and **B34** in S14 (different keys: B34 adds `management_orders` at the end of its family's block) → B19; `data/rosters.py` B21 → **B34** → B32; `boot/realm.py` B21 → **B34** → B32; `harness/scene.py` **B34** → B20 (U2) → B30 (U3) → B38; `hole_register.yaml` once per batch.
PARALLEL: S14 with B12b (SE+WR), B19a (MB), B21c (FA), B29 (PC). Shared with B21c: `queries/world_q.py` (B21c `judging_set`; B34 `_goal_referents`, `seats_named`), `rosters.yaml` (B21c `conferral_bases`, `revocation_bases`, `record_kinds`; B34 `management_orders`), `hole_register.yaml`: different keys and functions, kept by hand at merge (`V12_STRUCTURE_part3.md` §7.3). Shared with B29 (its WHERE lines): `queries/world_q.py` (B29 `warrants_for`, `warrants_heard`, `_stamped`; B34 `_goal_referents`, `seats_named`, `goal_referents`), different functions. B12b's edit set is read from its block at the step's open by the coordinator (the census). B19a shares nothing. Movers in S14 (B12b, B21c, B29, B34) merge in §2.1's order; the later rebases and re-pins once (§7.4).

### B34.01 — the gate tests first; the doer holds his own act's outcome · GO-B "Build order and tests" 1–2, §3 · BUILD · HASH EQUAL, or MOVER(behaviour) in branch 2
- SOURCE: `proposals/11_GO_player_surface_contract_B.md` ("GO-B") §3 "The outcome of his own act", "Build order and tests" 1–2, "The gate" 1–5; C3-L4 (the host-side `receipt` is deleted), C3-L5; `IS-B3` part 2 §6.1 (one test file, UNDECIDED U6); rulings A-81; closes F-GO-15 to F-GO-19 in part (GO-B's head).
- ADVANCES: GO standalone (S3, S6); A-81 in branch 2 ("the doer's own claim is a durable write of every scene").
- INSTRUCTION:
  1. Write the gate tests first (GO-B build order 1), in `engine/season/tests/test_play_surface.py` (U6): `test_transcript_hash_equals_plain_run` (gate 1, seeds 0–2; control "the plain run's hash, seed 0 one season", re-read on this batch's base, `reading @<sha>`), `test_offer_rows_follow_make_ranker_and_watch_terms` (gate 2), `test_account_prior_teller_unattributed` (gate 4), `test_withheld_rows_are_own_state_only` (gate 5). "Expected before the build: all fail (the readers do not exist) except possibly §3's."
  2. §3, branch 1, "Test first": write `engine/season/tests/test_play_surface_own_outcome.py::test_the_doer_holds_his_own_acts_outcome`: "seat `p_npc_001` at `populated.build_realm(0)`, plant one act of his whose Event WITNESS processes (a `research` act that ends `finding.none`), read his ledger after the barrier, and assert a claim with `doer == p_npc_001` on that act's Event. If it passes on the tree, nothing is added: `account` already reads it."
  3. §3, branch 2, only if step 2's test fails: "add the self-deposit rule at WITNESS (`engine/season/loop/witness.py::witness`; it already stamps `doer = pid if actor == pid else None`, so the rule widens who is a witness, not what a deposit carries): the doer of an act receives a firsthand claim of its Event's band and kinds. A declared hash mover, its own commit, with the realm hash at seeds 0–2 old and new in the commit body." The commit body names the branch taken.
- WHERE: NEW `engine/season/tests/test_play_surface.py`; NEW `engine/season/tests/test_play_surface_own_outcome.py`; `engine/season/loop/witness.py` (`witness`, branch 2 only).
- TESTS: the five above; the four gate tests red until B34.02 to B34.04 land (EXPECTED RED UNTIL B34.04, under `[skip ci]`).
- FALSIFIER and CONTROL: "Every act the seated person resolved has an `own=True` `AccountRow` …; a planted act of another person yields none" (gate 3, read at B34.03). Control: in branch 1 the realm hash at seed 0 equals the step's base; in branch 2 a planted act by another person deposits no `doer` claim to `p_npc_001`.
- GATE: `python -m pytest engine/season/tests/test_play_surface_own_outcome.py -q` → pass (in branch 1 before any edit; in branch 2 after step 3); the realm hash at seed 0, one season → equal (branch 1) or moved and declared (branch 2).
- HASH MOVERS: none in branch 1; branch 2 "a declared hash mover" (WITNESS's self-deposit). Re-pinned at B34.99.
- DEPENDS ON: EXISTS-IN-TREE `loop/witness.py::witness`, `state/carriers.py::Claim.doer`; V12 Batch B03c (`boot/realm.py::build_realm`); V12 Batch B05 (`05_SC_contest_record_on_event`, SC-P1: the roll's record on `Event.observed`).
- GLOSSARY: none.
- NAMES: `populated.build_realm` → `boot/realm.py::build_realm` (B03c).
- COST and TIER: a test, then nothing or one WITNESS rule; `sonnet`, `high`; `opus` reads branch 2's decision (GO-B "Lands it").
- LANDS IT: B34's `valoria-author` producer, `isolation: worktree`; `Item: B34.01`, `[skip ci]`.

### B34.02 — `Situation` and `Offer`: what is in front of him, what he may do · GO-B §1, §2 · BUILD · HASH EQUAL
- SOURCE: GO-B §1, §2, "Build order" 3; SURF §1 (stands and is extended, GO-B head); rulings A-48 (the player picks which questions to attend; an NPC takes the first), A-47 (a threshold question is mandatory), A-9; `30_GO_F` adds rows' later fields (B38, not here).
- ADVANCES: GO standalone (S3); R-04.c1 (with B34.06).
- INSTRUCTION (GO-B's records, copied; every reader's `p` is the frozen `PersonInterior` (B03, `U5a_CORE_owed_edits` §E item 1) and `v` is `state/carriers.py::View`):
  1. `engine/season/decision/sheet.py`, `DevelopmentSheet` split in two:
     ```
     @dataclass(frozen=True)
     class AskedRow:
         question: Question            # source, referents, classes, about: as carried on View.questions
         claim: Optional[Claim]        # the claim of HIS that `about` names, where it is one; else None
     @dataclass(frozen=True)
     class Situation:
         person_id: str
         budget: int                   # ask_budget()
         body: int; capability: Mapping; pursuits: Mapping; stance: tuple; conviction: Mapping; scar: Mapping
         holdings: tuple               # ((tenure kind, object id), ...): his own live Tenures, through OwnStateReader
         asked: tuple                  # AskedRow per Question in v.questions, in attention_key order
     def situation(p, v, ask_budget) -> Situation
     ```
     "`holdings` is empty until `OwnStateReader` answers his own Tenures (CHAR's item 2); the field ships with the reader." Lane 28's readings (who occupies him, which petitions wait) join `Situation` in B28 under lane 28's names; no field is invented here.
  2. The same file:
     ```
     @dataclass(frozen=True)
     class OfferRow:
         candidate: Candidate          # a deep copy, as today
         occasion: Optional[str]       # the id of the AskedRow question whose referents hold candidate.subject;
                                       # None for a standing candidate (one formed on no referent)
         terms: tuple                  # score_terms' tuple, exactly as the chooser summed it
         odds: Optional[tuple]         # View.odds for this candidate: what he BELIEVES, which may be wrong
         cost: int                     # Scene.cost's unit
     @dataclass(frozen=True)
     class WithheldRow:
         verb: str; subject: Optional[str]
         unmet: str                    # the own-state conjunct of the row's requires_typed that answered False
     @dataclass(frozen=True)
     class Offer:
         rows: tuple                   # make_ranker's order
         withheld: tuple               # own-state declines only
     def offer(p, v) -> Offer
     ```
     "`terms` has one source: CHAR's `watch` hook on `make_chooser`." "`occasion` is derived in the sheet from `candidate.subject` and `v.questions`; it forms nothing and ranks nothing `[ASSUMPTION; low; revert: drop the field, the client groups by subject]`." "`withheld` is the display of CHAR's decline (`opening_set` declining on a conjunct the actor's own state answers `False`): the decline returns the conjunct instead of dropping it. **Only own-state stems appear.**" "A candidate that runs against a conviction is **not locked**." "The army verbs are not `OfferRow`s … `harness/military_menu.py` is their surface and stays as ruled."
- WHERE: `engine/season/decision/sheet.py` (`AskedRow`, `Situation`, `situation`, `OfferRow`, `WithheldRow`, `Offer`, `offer`; `DevelopmentSheet` split).
- TESTS: `test_offer_rows_follow_make_ranker_and_watch_terms` turns green; `test_withheld_rows_are_own_state_only` turns green.
- FALSIFIER and CONTROL: "An `OfferRow.terms` differing from the chooser's sum. A `WithheldRow` naming a world-side requirement." Gate 2: "for one deliberation, the order of `Offer.rows` equals `make_ranker`'s and each row's `terms` equals what the `watch` hook reported; a planted claim that changes his belief about one subject changes `odds` for acts on that subject only." Control: realm hash equal (readers that write nothing).
- GATE: `python -m pytest engine/season/tests/test_play_surface.py -k "offer or withheld" -q` → pass; `python -m pytest engine/season/tests/test_season_shape.py -q` → the `decision/` path scan green (no `World` under `decision/`).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `decision/sheet.py::DevelopmentSheet`, `decision/choose.py::make_ranker`, `::score_terms`, `state/carriers.py::View` (`questions`, `odds`), `Scene.cost`; V12 Batch B03 (`PersonInterior`); V12 Batch B09 (the `watch` hook, `02_CHAR_reason_trail_and_small_edits` Part A); V12 Batch B10 (`02_CHAR_offer_what_can_be_done`: the own-state decline); V12 B34.01.
- GLOSSARY: rows *offer* and *situation* if absent: "offer": what a person may do now, ranked, as a shop's offer; "situation": what is in front of him now. Each owner `decision/sheet.py`. `[ASSUMPTION: no row exists — basis: grep of `U1_GLOSSARY.md` for "offer" found none]`.
- COST and TIER: small build; `sonnet`, `high`; IN and CHAR review `decision/`.
- LANDS IT: B34's producer; `Item: B34.02`, `[skip ci]`.

### B34.03 — `account` and `dossier`: what he has learned, what he holds about one subject · GO-B §4, §5 · BUILD · HASH EQUAL
- SOURCE: GO-B §4, §5, "Build order" 3; replaces SURF's `aftermath` (SURF §3, corrected).
- ADVANCES: GO standalone (S3); R-08 (a person reads only what he holds).
- INSTRUCTION:
  1. `engine/season/decision/sheet.py`, beside `chronicle`:
     ```
     @dataclass(frozen=True)
     class AccountRow:
         claim: Claim                  # as held: subject, predicate, value, source, confidence, when, lap, chain, doer
         own: bool                     # claim.doer == holder: the echo of his own deed
         prior: Optional[Claim]        # the claim he held on the same (subject, predicate) just before, if he still holds it
         unattributed: bool            # a change he can see (prior differs, or an event-kind deposit) for which
                                       # no claim of his names a doer (no doer, no Seen.who, no deed_doer answer)
     def account(p, since: tuple) -> tuple[AccountRow, ...]      # since = (tick, lap), questions_for's own key
     ```
     "Read from the person's own ledger and nothing else." "**Another person's reasons are shown exactly here**: as the claims the player's person holds about that person's deeds, tellings and commitments, with their sources."
  2. `engine/season/queries/person_q.py`:
     ```
     @dataclass(frozen=True)
     class DossierRow:
         claim: Optional[Claim]        # FI-05's E1: a belief he holds
         record: Optional[str]         # FI-05's E2: the id of a Record on his live hold
         proof_kind: str               # derived, rosters.yaml: proofs
         support: float                # LedgerReader's support over distinct origins
         against: tuple                # ids of claims of his that the pairing rule marks as disagreeing
     def dossier(p, subject) -> tuple[DossierRow, ...]
     ```
     "The content rules are FI's and SC's"; "Until FI-05 lands, `dossier` is `chronicle`'s `beliefs` filtered to one subject." FI-05 (`08_FI_05_evidence-interface_B`) lands in B24, before B34: build the full form, reading B24's evidence items by symbol at the item's open.
- WHERE: `engine/season/decision/sheet.py` (`AccountRow`, `account`); `engine/season/queries/person_q.py` (`DossierRow`, `dossier`).
- TESTS: `test_account_prior_teller_unattributed` turns green; gate 3's `own=True` arm added to `test_play_surface_own_outcome.py` (`test_every_resolved_act_has_an_own_account_row`) `[ASSUMPTION: test name (E-3)]`.
- FALSIFIER and CONTROL: "A value in an `AccountRow` that the person does not hold." Gate 4: "`account` after a season: a planted told claim reads `own=False` with `claim.teller` set; two claims on one cell give the later row a `prior`; an event-kind deposit with no doer reads `unattributed=True`." Gate 3: "a planted refusal on a world fact he holds no claim on shows the conjunct without its value; with the claim planted, the value." Control: realm hash equal.
- GATE: `python -m pytest engine/season/tests/test_play_surface.py engine/season/tests/test_play_surface_own_outcome.py -q` → the account and own-outcome tests pass (the transcript test stays red until B34.04).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `decision/sheet.py::chronicle`, `queries/person_q.py::LedgerReader`, `state/carriers.py::Claim` (`teller`, `hops`, `chain`, `doer`); V12 Batch B24 (FI-05's evidence items); V12 B34.02.
- GLOSSARY: row *account* (the person's own record of what he learned since a point): owner `decision/sheet.py::account`; *dossier*: "what he holds about one subject, as a case file" `[ASSUMPTION: rows absent — basis: grep]`.
- NAMES: `(tick, round)` → `(tick, lap)`; `Claim.round` → `Claim.lap` (B04, PCR-4).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.03`, `[skip ci]`.

### B34.04 — the transcript: one runner for every playable scenario · GO-B §8 · BUILD · HASH EQUAL
- SOURCE: GO-B §8, "Build order" 4–5, gate 1; GO-B §7 (presentation is triggered by an `AccountRow`, never by a log Event: a rule for the port, recorded in the runner's docstring); `IS-B2-CORE-01` (B11: `scenarios.run`, the one loop).
- ADVANCES: GO standalone (S1, S3, S6); every lane's scenario is printed by one runner.
- INSTRUCTION: `engine/season/harness/play_surface.py` gains a command: "`python -m engine.season.harness.play_surface --seed S --person P --seasons K [--scenario NAME]` seats `P` with `take_ranked`, and per deliberation prints the `Situation` (asked rows), the `Offer` (rows with terms and odds, withheld rows), the pick, then the `account` since the last deliberation, and for a suspended scene the `trace`. Every lane's standalone scenario (the valley, the governance spine, the hearing, the inquiry, the duel, the field) is printed by this runner instead of by its own `sheet(w)`; a lane's world-reading summary stays what it is, an instrument for a developer, and is not the player's surface." `--scenario NAME` resolves through `scenarios.SCENARIOS` (B11) and runs `scenarios.run` (no season loop of the runner's own, `IS-B2-CORE-01` (4)); with no `--scenario`, the realm row. The docstring states GO-B §7's rule: "A player-facing presentation is triggered by an `AccountRow` of the seated person, never by a log Event."
  (Patched: P-29) The host-side faction view calls `faction_q.standing` (B03.65), copied from `U5a_CORE_owed_edits` §I step 2: "Callers, each by its own proposal and neither inside the season loop: the host-side faction view of `11_GO_player_surface_contract_B.md` (a seated person's faction, beside `account`) …"; and step 3: "A person's own reading of where a faction stands stays a belief (AX-2): this record is resolver-side and may not be handed to `decision/`." So the transcript prints, per season, the seated person's faction's `standing(w, f, realm_rung)` as a host line labelled resolver-side, never inside the `Situation` or `account` rows and never passed to `decision/`; it defines no second footprint, density or provinces reading (B03.65's U-2).
- WHERE: `engine/season/harness/play_surface.py` (`main`, the transcript function; the faction view's call, P-29).
- TESTS: `test_transcript_hash_equals_plain_run` turns green (seeds 0–2).
- FALSIFIER and CONTROL: "A transcript whose hash differs from the plain run. A scenario that prints through a `World`-reading sheet and calls it the player's view." Control: gate 1, the plain run's hash.
- GATE: `python -m engine.season.harness.play_surface --seed 0 --person p_npc_001 --seasons 1` → exit 0, prints rows, `content_hash` equal to the plain run's; `python -m pytest engine/season/tests/test_play_surface.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/play_surface.py::dispatching_chooser`, `::carry_on`, `decision/sheet.py::seat`, `::take_ranked`; V12 Batch B11 (`scenarios.py`, `run`); V12 B34.03.
- GLOSSARY: row *transcript* if absent: "the printed record of a played run, deliberation by deliberation", owner `harness/play_surface.py`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.04`, `[skip ci]`.

### B34.05 — `explain`: a value's derivation from his own claims · SURF §2 · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_player_surface_contract.md` §2 (the one live section: "SUPERSEDED … except §2 (`explain`), which is live and lands in B34") and its "Build (W3-1, §2 only)"; `04` §C.11 (the signature, ratified); U3 §6.3 (`explain` / `Derivation`: this section).
- ADVANCES: GO standalone (S3: why a value is what it is, from what he holds).
- INSTRUCTION (copied): "Order: (1) write `tests/valoria/test_explain.py` with `test_explain_takes_no_world` (a signature test, as `choose`'s: `inspect.signature(person_q.explain)` has exactly the parameters `p`, `v`, and `p`'s annotation is `PersonInterior`) and `test_a_fact_held_by_no_claim_appears_in_no_derivation` (plant a `World` fact his ledger holds no claim of; expect it in no `Derivation.terms`); both fail first (`explain` does not exist). (2) Add `Derivation` and `explain` to `engine/season/queries/person_q.py`, reading only `p`'s own ledger." The record:
  ```
  def explain(p: PersonInterior, v: Value) -> Derivation      # no World; no walk of causes[] -> Act.actor
  @dataclass(frozen=True)
  class Derivation:
      value: Value
      terms: tuple          # (claim_id, source, confidence, when, contribution) per own Claim that fed it
      unattributed: bool    # True where the value moved and no claim of his names an author
  ```
  "First `Value`s, in the order a player meets them: an `OfferRow`'s `pursuit` and `stance` [GO-B: the `terms` tuple's two members]; a belief the chronicle shows; the person's own `body` and `stores` readings."
- WHERE: `engine/season/queries/person_q.py` (`Derivation`, `explain`); NEW `tests/valoria/test_explain.py` (U6).
- TESTS: the two above, red first.
- FALSIFIER and CONTROL: "a `Derivation` naming an actor the person holds no claim about fails the second test; control: the EQUAL hash."
- GATE: `python -m pytest tests/valoria/test_explain.py -q` → pass; the realm hash at seed 0, one season → equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B03 (`PersonInterior`); V12 B34.02 (`OfferRow.terms`).
- GLOSSARY: row *derivation* if absent: "how a value came to be, term by term, from what he holds".
- COST and TIER: small build; `sonnet`; IN reviews `person_q`.
- LANDS IT: B34's producer; `Item: B34.05`, `[skip ci]`.

### B34.06 — a creation row shows the seat's holdings; no decider means his own policy · fidelity edits 1–2, with `16_PESSIMIST_GO` §4's shape · BUILD · HASH EQUAL
- SOURCE: `proposals/11_GO_fidelity_and_campaign_modes.md` ("fidelity") "Exact edits, by owner" 1, 2; §2's clause "No decider means the person's own policy"; §4 "Begin"; `proposals/16_PESSIMIST_GO_the_offer_names_what_is_held.md` §4 (the shape, UNDECIDED U4); rulings A-1, A-48, A-49, A-53 (fidelity's head).
- ADVANCES: R-04.c1 (the sheet: creation shows the seat); GO standalone (S4).
- INSTRUCTION:
  1. Edit 1, in `16_PESSIMIST_GO` §4's shape: "`engine/season/decision/sheet.py` — `CreationRow` gains `holdings: tuple`" (`# ((tenure kind, object id), ...): his own live Tenures, the same pairs SURF-B's Situation.holdings defines, from the same reader`); `def creation_sheet(persons, holdings_of) -> tuple     # holdings_of: person id -> tuple; the caller's reader`. "`decision/` still names no World: the caller, which already holds the persons, passes the reader (CHAR's `OwnStateReader` when it lands; until then `harness/play_surface.py` builds the mapping host-side from `w.tenures`, as `harness/military_menu.py` does for an army)." Every caller of `creation_sheet` (`git grep -n "creation_sheet(" engine tests`, recorded in the commit body) passes the reader.
  2. Edit 2: "`engine/season/queries/inputs.py::PlayHost` docstring — add the clause "a scene with no decider is decided by the person's own policy" and name the present interim (the module default)."
- WHERE: `engine/season/decision/sheet.py` (`CreationRow.holdings`, `creation_sheet`); `engine/season/harness/play_surface.py` (the host-side `holdings_of`); `engine/season/queries/inputs.py` (`PlayHost` docstring); the callers the grep names (`engine/season/tests/test_rem30_character_sheet.py` among them).
- TESTS: `engine/season/tests/test_season_shape.py::test_creation_sheet_shows_holdings_for_a_seat_holder` (fidelity gate 4), written first and read red.
- FALSIFIER and CONTROL: gate 4: "`creation_sheet` on a built realm shows a non-empty `holdings` for a seat holder and takes no `World` (the path scan)". Control: realm hash equal (a reader).
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -k "creation_sheet or path" engine/season/tests/test_rem30_character_sheet.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `decision/sheet.py::CreationRow`, `::creation_sheet`, `queries/inputs.py::PlayHost`; V12 B34.04.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.06`, `[skip ci]`.

### B34.07 — each closed choice set exported with a name and a line of text · fidelity edit 3 · BUILD · HASH EQUAL
- SOURCE: fidelity "Exact edits" 3; §3 ("a module's closed choice set is exported with a `name` and one line of `text` per member (SURF-B §6 rule 2), so the client shows a named move and never a matrix"); GO-B §6 rule 2 ("`TURN_CHOICES` and PC's `APPROACHES` join `combat_engine_v1.json`"; `battle_orders.json` the precedent).
- ADVANCES: GO standalone (S3; the port renders and computes nothing).
- INSTRUCTION: "Each module's exporter — its closed choice set with `name` and `text` (`tools/export_battle_orders.py` has the roles; `tools/export_engine_params.py` gains combat's `TURN_CHOICES`/`APPROACHES`)." In order: (1) open `tools/export_engine_params.py` and `engine/engine_params/combat_engine_v1.json` and record whether B16 already exports `ROUND_CHOICES` and `APPROACHES` (B16.05 re-derived the export); (2) add what is missing so each member of `ROUND_CHOICES` and `APPROACHES` is exported as `{name, text}`; (3) `tools/export_battle_orders.py`: each order member gains `text` where it has none; (4) re-derive both artifacts with the tools, never by hand. The `text` lines are authored content (D-19): drafted, `[ASSUMPTION]`-marked in the exporter's source module, and listed in B34's PR body for Jordan's correction.
- WHERE: `tools/export_engine_params.py`; `engine/engine_params/combat_engine_v1.json` (re-derived); `tools/export_battle_orders.py`; `engine/engine_params/battle_orders.json` (re-derived); the owning vocabulary modules where the `text` lives (`modules/combat/vocabulary.py` `[ASSUMPTION: the text sits beside the tuple it describes — basis: the exporter reads the module, `battle_orders.json`'s precedent]`).
- TESTS: in the exporters' existing round-trip tests (`grep -rln "export_engine_params\|export_battle_orders" tests engine/tests`, named in the commit body): a member with no `text` is refused.
- FALSIFIER and CONTROL: a member exported with no `text`, or a second copy of a choice tuple under `game/`. Control: the realm hash equal (no runtime reader).
- GATE: `python tools/export_engine_params.py --check` → exit 0; `python tools/export_battle_orders.py --check` → exit 0; `python -c "import json; d=json.load(open('engine/engine_params/combat_engine_v1.json')); print(sorted(d))"` → names the choice block.
- HASH MOVERS: none (an export; no realm pin reads it).
- DEPENDS ON: V12 Batch B13 (`modules.combat` imports), V12 Batch B16 (`ROUND_CHOICES`, `APPROACHES`); EXISTS-IN-TREE `tools/export_battle_orders.py`, `tools/export_engine_params.py`.
- GLOSSARY: none.
- NAMES: `TURN_CHOICES` → `ROUND_CHOICES` (B16, PCR-3).
- COST and TIER: edit and content; `sonnet`; the texts drafted by `opus`.
- LANDS IT: B34's producer; `Item: B34.07`, `[skip ci]`.

### B34.08 — fork C closed; the difficulty overlay test · fidelity edit 4, gate 3 · BUILD · HASH EQUAL
- SOURCE: fidelity "Exact edits" 4; §2 ("**Fork C (the calibration tolerance) needs no number.** Two clauses replace it"); §3 ("Difficulty is a fixtures overlay chosen at world build"); "The gate" 3; "Tests (W3-1)".
- ADVANCES: GO standalone (S1: difficulty is data); ED-SC-0013 fork C.
- INSTRUCTION: (1) "`registers/handoffs/HANDOFF_SC.md` — ED-SC-0013 fork C closed by the two clauses above, citing the module-scene pin as its instrument": the two clauses are "*Equal on matched decisions.* A played scene whose decider returns what the automated call would have chosen reproduces the automated outcome and the same keyed draws (A-30; no draw log is recorded)" and "*No decider means the person's own policy.*" A pointer row in the handoff's own form (a head, an id, a path), not narrative (CLAUDE.md §1). (2) Write `engine/season/tests/test_play_surface.py::test_scene_budget_overlay_gives_three_scenes` (gate 3): "A `Fixtures` with `scene_budget` swept to 3 gives the seated person three scenes and moves the hash; nothing else in the engine reads a difficulty."
- WHERE: `registers/handoffs/HANDOFF_SC.md` (ED-SC-0013's row); `engine/season/tests/test_play_surface.py`.
- TESTS: the gate-3 test, green at landing (the overlay exists; the test is new).
- FALSIFIER and CONTROL: "A second resolution formula reachable from the loop under any name. A decider default that differs for a played person and an NPC of the same sheet. A row absent from `Offer.rows` because of a cap." Control: gate 1 (`overrides = {}` reproduces the plain hash; `test_rem31_grid_suspension.py`, existing).
- GATE: `python -m pytest engine/season/tests/test_play_surface.py engine/season/tests/test_rem31_grid_suspension.py -q` → pass.
- HASH MOVERS: none ("the only run that moves a hash is gate 3's `scene_budget` sweep to 3, an overlay the gate applies and no pinned world does").
- DEPENDS ON: EXISTS-IN-TREE `data/fixtures.py` (`scene_budget`), `registers/handoffs/HANDOFF_SC.md`; V12 B34.04.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B34's producer; `Item: B34.08`, `[skip ci]`.

### B34.09 — the spine's menu is the `Offer` · `IS-B3-FA-02` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO.md` "Item: IS-B3-FA-02"; rulings A-104 (its step 4).
- ADVANCES: FA standalone (S3); GO's one surface.
- INSTRUCTION (copied): "`06_FA_playable_scenario.md` adds `offered(p, v, s, ask_budget, auto) -> list[str]`, the seat-gated candidates grouped by remit act. `11_GO_player_surface_contract_B.md` §2 then adds `Offer.rows` with `occasion`, `terms` and `odds` for every candidate, and §8 says the player's surface for every scenario is the transcript runner. When B34 lands: (1) delete `governance_spine.offered`; (2) `play`'s callback prints the `Offer` through `play_surface`'s transcript function, and the grouping by remit act becomes a grouping on `OfferRow.candidate` read off the verb row's `eligibility` cell (`remit:<act>`), done in the print and not in the reading; (3) `digest` and `loop_closed` stay: they read `w.log` and are the developer's instrument (GO §8). (4) *(A-104.)* The `Offer`'s seat verbs that CL-MGMT lists as management orders cost no scene budget and may open scenes after; the price is `Scene.cost`'s alone (`IS-B3-GO-07`), and nothing in this item prices a row."
- WHERE: `engine/season/harness/governance_spine.py` (`offered` deleted; `play`'s callback); `engine/season/tests/test_governance_spine_play.py`.
- TESTS: `test_play_prints_the_offer_and_holds_no_second_menu`, written first and read red.
- FALSIFIER and CONTROL: "`grep -n "def offered" engine/season/harness/governance_spine.py` prints nothing; the transcript of `spine.order` at seed 0 shows the writ's question as an `AskedRow` and at least one `OfferRow` whose `occasion` is that question. Control: the run's content hash is unchanged by the swap (a print moved)."
- GATE: `python -m engine.season.harness.play_surface --scenario spine.order --seed 0 --seasons 2` → prints an occasioned row for `comply`; `python -m pytest engine/season/tests/test_governance_spine_play.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B21 (`06_FA_playable_scenario`'s `offered`, `IS-B3-FA-01`'s spine rows); V12 B34.04.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet` (GO review).
- LANDS IT: B34's producer; `Item: B34.09`, `[skip ci]`.

### B34.10 — a management order costs no scene budget, at control · `IS-B3-GO-07` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` "Item: IS-B3-GO-07"; rulings A-104 (*"menu orders, which are management orders like 'assign this' or 'fire this person' or 'raise army' or whatever do not cost scene budget because they are not scenes. however, these CAN prompt scenes after being performed."*); `L1-A104` APPLIED (`ED-IN-0360`); closes M31 (b), E-3 (the intake §4).
- ADVANCES: GO and FA standalone (S3); R-04.
- INSTRUCTION (copied): "(1) **The list, as data.** `engine/season/rosters.yaml: management_orders`, a closed set of verb names, loaded by `data/rosters.py` and refused at import when a member is not a row of `verb_table.yaml`; it **ships empty** (the control: today's prices, hash EQUAL). Its members are CL-MGMT's `[BLOCKED: CONTENT — CL-MGMT's list, A-104]`. (2) **One price owner.** `Scene.cost(extended_cost, orders=frozenset())`: a scene whose every act's verb is in `orders` costs 0; any other scene as today. The callers pass `rosters.MANAGEMENT_ORDERS` (DELIBERATE and `pack_scenes`; `decision/` may read `data/`). No caller computes a price of its own. (3) **No mixed scene.** `pack_scenes` puts an order candidate in a scene of its own, so an order never makes a priced scene free and never rides in one at a price. (4) **Orders open scenes after.** Nothing new … (5) **Scope.** Every person's orders, the player's and every NPC's `[ASSUMPTION: A-104's own]`. (6) **Layer 1.** … APPLIED 2026-11-12 (`L1-A104`) … Not decided here: whether a person's free orders per lap need a cap (the release count `scenes_per_lap` counts scenes, so an order scene would take a lap's slot); the first reading below decides whether a setting is owed." The new key sits at the end of its family's block in `rosters.yaml` (CIP part 2 §5 note 1).
- WHERE: `engine/season/rosters.yaml` (`management_orders`); `engine/season/data/rosters.py` (`MANAGEMENT_ORDERS`, the refusal); `engine/season/state/carriers.py` (`Scene.cost`); `engine/season/decision/choose.py` (`pack_scenes`); `engine/season/loop/deliberate.py` (the two `cost` call sites); NEW `engine/season/tests/test_management_orders.py`.
- TESTS (copied, written first and read red): "`test_an_order_scene_costs_nothing_and_a_priced_scene_is_unchanged` (with a planted one-member list: the order scene's cost is 0, a plain scene's 1, an extended one's `extended_scene_cost`); `test_an_order_never_shares_a_scene_with_a_priced_act`; `test_a_person_with_a_full_budget_may_still_order` (budget spent to 0, an order is still released); `test_an_order_opens_a_scene_next_round` [next lap] (a planted `dispatch` forms the recipient's `comply` next round [lap], priced 1)."
- FALSIFIER and CONTROL: the four tests; "Control: the list empty, the realm content hash at seeds 0, 1, 2 equals the base."
- GATE: `python -m pytest engine/season/tests/test_management_orders.py -q` → pass; the realm hash equal at seeds 0, 1, 2 with the list empty. (The source's "with CL-MGMT's list loaded, `aperture 2 0` and `2 2` print orders per person per season" is the list's own commit's reading, HELD with the list.)
- HASH MOVERS: "None at the control. Loading CL-MGMT's list is a declared mover … re-pinned once at that commit."
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Scene.cost`, `decision/choose.py::pack_scenes`, `loop/deliberate.py`; V12 Batch B21 (`IS-B3-FA-05`, `dispatch`); V12 B34.09; MISSING (content: CL-MGMT's list, held; the load is not an item of v12).
- GLOSSARY: row **management order**: "an order a seat gives from its desk, costing no scene, as a manager's instruction is", owner `rosters.yaml: management_orders`.
- NAMES: `scenes_per_round` → `scenes_per_lap`; "next round" → "next lap" (B04, PCR-4; A-101).
- COST and TIER: small build; `sonnet`.
- LANDS IT: B34's producer; `Item: B34.10`, `[skip ci]`.

### B34.12 — a creation row marks cohorts · `16_PESSIMIST_GO` §4 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GO_the_offer_names_what_is_held.md` ("PES-GO") §4, "Exact edits" row `decision/sheet.py`, gate 4; "Cost class" ("order §4 (hash-equal) → §1 and §3 → §2 … → the re-pin"); rulings A-56 (a played cohort is offered the heavy moves only; whether a cohort may be played is not ruled); closes F-PES-GO-10.
- ADVANCES: R-04.c1 (the creation-sheet test: this item's `test_creation_sheet_marks_cohorts_and_holdings` is the conjunct's reading).
- INSTRUCTION: `CreationRow` (as B34.06 left it, with `holdings`) gains `cohort: bool  # Person.is_cohort`, copied from §4's record: `id: str; name: str; cohort: bool; capability: Mapping; pursuits: Mapping; conviction: Mapping; attributes: Mapping; holdings: tuple`. `creation_sheet(persons, holdings_of)` fills it. No knowledge rule is touched ("Creation happens before the first season and shows the seat's own state").
- WHERE: `engine/season/decision/sheet.py` (`CreationRow.cohort`); NEW `engine/season/tests/test_seat_holders_from_ledger.py` (its first test).
- TESTS: `test_creation_sheet_marks_cohorts_and_holdings` (gate 4), written first and read red: "`creation_sheet` at seed 0: 37 rows with `cohort=True`; the Inquisitor's row carries `("hold", "off_senior_inquisitor")` and the fugitive's does not." The count 37 is read at landing (the source's reading at `826b747`) and the test asserts the count `sum(p.is_cohort for p in persons)` gives, not a typed 37.
- FALSIFIER and CONTROL: a cohort row with `cohort=False`, or a holdings pair the person does not hold. Control: realm hash equal.
- GATE: `python -m pytest engine/season/tests/test_seat_holders_from_ledger.py -k creation -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B34.06; EXISTS-IN-TREE `state/carriers.py::Person.is_cohort` (a method at `7c37586`: the row stores its value).
- GLOSSARY: none (*cohort* has its row).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.12`, `[skip ci]`.

### B34.15 — the host names a decider per module role; the party test once; a module's scene alone · `01_CORE` edits 1, 2, 4, with `IS-PC-01` step 6 · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_one_scene_contract.md` ("CORE-SC") Edits 1, 2, 3 (the interface), 4 and "(a) restated", "Gate", "Named tests"; `master/instructions/IS_B1_PC_MB_DICE.md` `IS-PC-01` step 6; rulings A-1, A-4, A-30, A-63, A-72 (`L1-A4`, `L1-A72` APPLIED); C-U5a-03, C-U5a-04; UNDECIDED U3, U8.
- ADVANCES: every module playable alone by the entry the fold uses; PC standalone (`duel` fixture).
- INSTRUCTION:
  0. SITE: open `engine/season/queries/inputs.py::PlayHost` (B24.05 added `deciders` beside `decide`) and `engine/season/seam/wrappers/combat.py::resolve` (B16 made its decider per claimant) and record both shapes in the commit body; the edits below compose on them.
  1. Edit 1 (copied): "`PlayHost` names a decider per module role":
     ```python
     @dataclass(frozen=True)
     class PlayHost:
         persons: frozenset
         deciders: Mapping[str, Callable]     # module role (`combat.fight`, `social_contest.roll`, …) -> decide(view) -> choice
         def decider_for(self, role: str) -> Optional[Callable]
     ```
     "`decide` (today's single field) becomes `deciders["combat.fight"]`; a constructor argument `decide=` is kept for the three existing callers and maps to that key. A role with no decider is automated for that host." The nesting cap clause of Edit 1 is B30's (U3 (a)).
  2. Edit 2 (copied): "owner `engine/season/seam/wrappers/_entry.py` — the party test, once": `def played_by(host, role: str, parties) -> Optional[Callable]: """The host's decider for `role` when the host plays one of `parties`, else None (AUTOMATED)."""` "`combat.resolve` calls it in place of its inline test. `sigma.resolve`, `mass_battle.resolve` and the fieldwork provider call it and pass the result as `decide=` to `entry.fn`. Until a module's entry accepts `decide`, its provider passes nothing and the mode is automated." The hearing's resolve (B24) reads `host.deciders` for `social_contest.hearing`; it is re-pointed at `played_by` in this edit.
  3. Edit 3 is the interface each module lane owns: "A module entry that can be played has the signature `fn(inp, rng, *, decide=None) -> outcome` … the **wrapper** (`seam/wrappers/<m>.py`, the adapter) resolves the person's decider — `played_by(host, role, parties)`, else the sampled decider the host builds for that person from `decision/` (`_sample_order`, D-06) — and passes it as `decide=`; with neither, the entry runs its named interim policy." No module file is edited here.
  4. Edit 4 (copied, with "(a) restated"): NEW `engine/season/harness/scene.py`, `def play(role: str, fixture: dict, *, seed: int = 0, decide=None, apply: bool = False) -> dict`. "(a) `apply=False` calls `seam.contest(w, rung, prize, claimants, depth=0, max_depth=fixture["max_depth"], causes=[], verb=…, subject=…, rng=…, host=…)`, not `provider.resolve`, so the depth cap and the one ladder run and the degree is the one ladder's"; "(b) `apply=True`: runs a one-act season with that act as an authored `choose` return, so the fold's `writes_at(degree)` and emissions happen and the returned world carries the consequences. Both use `host=PlayHost(persons={actor}, deciders={role: decide})` when `decide` is given." "**The seed:** the generator is the keyed stream `draw_factory(seed, tick)(person, f"{role}:{act_id}")` (A-30; one draw per key, no recorder)". `apply=False`'s output says the counterparty's received-scene debit and the `engaged` clause are not asked (the head's A-63 statement). `main()`: "`python -m engine.season.harness.scene combat.fight --fixture duel --seed 0`".
  5. `FIXTURES`, a dict keyed by name, with `FIXTURES["duel"]` = `duel_scene.build` (B16.11) "and its opening act, replacing the headless-world `[ASSUMPTION]` of `01_CORE_one_scene_contract.md`" (`IS-PC-01` step 6; "`max_depth: 0`" kept). `play_surface --scenario duel` already resolves through the registry's `duel` row (B16.11) and B34.04's runner: the commit body records the reading and adds no line if it holds.
- WHERE: `engine/season/queries/inputs.py` (`PlayHost`); `engine/season/seam/wrappers/_entry.py` (`played_by`); `engine/season/seam/wrappers/combat.py`, `sigma.py`, `mass_battle.py`, `fieldwork.py` (the call to `played_by`); NEW `engine/season/harness/scene.py`; NEW `engine/season/tests/test_scene_contract.py`.
- TESTS (CORE-SC "Named tests", written first and read red): `test_echo_decider_equals_no_decider` (gate 1); `test_empty_deciders_is_hash_equal_to_no_host` (gate 2); `test_a_deviating_decider_moves_a_played_module` (gate 3, for `combat.fight` and the hearing, the modules that accept `decide` by B34); `test_apply_false_goes_through_seam_contest` (with the tree's `max_depth` and typed refusal, U3 (a)); `test_the_wrapper_not_the_module_resolves_the_decider` ("a source scan: no `modules/` file names `PlayHost`"). `test_a_duel_round_called_from_a_battle_may_not_call_a_third_scene` moves to B30 (U3 (a)).
- FALSIFIER and CONTROL: "A provider that builds a different input, or draws a different seed, when a host is present (compare `inp` and the seed across the two modes for one act). A standalone run whose result differs from the season's result for the same act, world and seed." Control: gate 2 ("a season run with `PlayHost(deciders={})` and one with no host produce one content hash").
- GATE: `python -m pytest engine/season/tests/test_scene_contract.py engine/season/tests/test_rem31_grid_suspension.py engine/season/tests/test_duel_scene.py -q` → pass; `python -m engine.season.harness.scene combat.fight --fixture duel --seed 0` → exit 0, a record, the same record twice.
- HASH MOVERS: none ("None with no host (gate 2 is the control)"; the stream's mover was B06's, U8).
- DEPENDS ON: EXISTS-IN-TREE `seam/contest.py::contest`, `seam/wrappers/_entry.py`, `state/ids.py::draw_factory`; V12 Batch B24 (B24.05's `deciders`; `05_SC_playable_hearing_B` edit 4); V12 Batch B16 (`duel_scene.build`, B16.11; the per-claimant combat decider); V12 Batch B06 (the keyed stream); V12 B34.04.
- GLOSSARY: the row *scene* names **scene instance** as the word for a module's playable form (ED-IN-0302); a row **scene instance** is added: "one module's scene run alone from a small world, as one staging of a play", owner `harness/scene.py::play`, the row *scene*'s own sense (Layer 1's `Scene`, what the budget counts) kept.
- NAMES: `CombatTurnView` → `CombatRoundView`; `TURN_CHOICES` → `ROUND_CHOICES` (B16); `Refusal(depth_cap)` is read as the tree's `ContestError("max_depth reached")` until B30 (U3).
- COST and TIER: edits and a small build; `sonnet`, `high` (CORE-SC "Lands it and tier").
- LANDS IT: B34's producer; `Item: B34.15`, `[skip ci]`.

### B34.16 — the player is shown all his questions · `01_CORE` edit 5 · BUILD · HASH EQUAL
- SOURCE: CORE-SC Edit 5 ("Edit 5 lands (A-48 B)"); rulings A-48 (the slate is a list of questions for the player; NPCs take the first), A-63/A-64 (an ask for audience arrives in `View.questions`).
- ADVANCES: GO standalone (S3).
- INSTRUCTION (copied): "No engine edit is needed: `View.questions` (CP-T02-07) already carries every question the driver computed for the person this lap [round in the source], in attention order, beside the aggregated `View.question`. What is missing is a client that shows them: `DevelopmentSheet` holds `question` only. The sheet gains `questions` (a tuple, copied from the view) and `development_space` ranks for the question the player picks. The automated chooser is untouched. No slate object is built." After B34.02, the sheet's `Situation.asked` is that tuple: `development_space` takes the picked `AskedRow`'s question.
- WHERE: `engine/season/decision/sheet.py` (`development_space`, the sheet's `questions`); `engine/season/harness/play_surface.py` (the pick of a question).
- TESTS: `test_development_space_ranks_for_the_picked_question` in `test_play_surface.py` `[ASSUMPTION: name (E-3)]`, red first: a pick of the second question ranks candidates whose `occasion` is that question first; a pick of the first equals today's ranking (control).
- FALSIFIER and CONTROL: an NPC's choice moves (the automated chooser touched). Control: realm hash equal; `take_ranked` on the first question reproduces the plain run.
- GATE: `python -m pytest engine/season/tests/test_play_surface.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B34.02; EXISTS-IN-TREE `state/carriers.py::View.questions`, `decision/sheet.py::development_space`.
- GLOSSARY: none.
- NAMES: "round" (the season's pass) → "lap" (A-101).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.16`, `[skip ci]`.

### B34.17 — one roll, played · `IS-DICE-01` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE_part2.md` "Item: IS-DICE-01"; the audit's §8 step 7 (`audits/10_DICE_audit.md`).
- ADVANCES: DICE standalone ("the dice play alone", IS-B1 P2-2.1 row 9).
- INSTRUCTION (copied; "edits to `engine/season/harness/scene.py`, which `01_CORE_one_scene_contract` edit 4 creates in the same batch"): "1. `FIXTURES["roll"]`: the world of `duel_scene.build(seed)` (IS-PC-01) with one more authored skill score on each of its two fighters, in the skill the fixture's verb row names, and one authored opening act of a rolled verb. The verb is chosen at landing from the rows of `verb_table.yaml` whose band cells differ, and named in the fixture. `[ASSUMPTION: the duel's world is reused — basis: it already holds two persons who differ and a witness]` 2. For the role `social_contest.roll`, `scene.play`'s printed record: the pool and its parts (the skill score, the base, the floor); each obstacle term by name and their sum; the levels in force (attributes, wounds, a seat's modifier); the exact band odds (`sigma_leverage.band_odds`); the actor's believed odds; the draw's key; the dealt band; and, with `apply=True`, the writes that band made. 3. `main()` gains `--verb` and `--effort`."
- WHERE: `engine/season/harness/scene.py` (`FIXTURES["roll"]`, the printed record, `main`); `engine/season/tests/test_scene_contract.py`.
- TESTS (copied, written first and read red): "`test_the_roll_fixture_prints_terms_that_sum_to_the_obstacle`; `test_printed_odds_match_realised_bands` (seeds 0–1,999); `test_effort_changes_the_printed_odds_and_some_dealt_band` (seeds 0–199, `assert checked >= 200`); `test_each_band_is_reached_and_each_writes` (all four bands occur within the 2,000 seeds; each has a write other than the budget debit)."
- FALSIFIER and CONTROL: "printed exact odds that disagree with the realised bands beyond the sampling band at 2,000 seeds; a band that leaves the world unchanged with `apply=True`. Control: `--effort 0` twice at one seed prints one record."
- GATE: `python -m pytest engine/season/tests/test_scene_contract.py -k roll -q` → pass; `python -m engine.season.harness.scene social_contest.roll --fixture roll --seed 0` → "a record whose terms sum to its obstacle and one of the four bands". The 2,000-seed test is sized on two small runs first (100 and 400 seeds, its wall time in the commit body) and run in the background at the item's open if it exceeds a few minutes (the skill, "Running a slow instrument").
- HASH MOVERS: none.
- DEPENDS ON: V12 B34.15 (`scene.py`); V12 Batch B16 (`duel_scene.build`); V12 Batch B05 (`05_SC_contest_record_on_event`'s `terms`; `10_DICE_believed_odds_have_a_prior`); V12 Batch B09 (`16_PESSIMIST_CORE_a_refusal_is_remembered`); EXISTS-IN-TREE `modules/social_contest/roll.py::roll`, `engine/dice_engine/sigma_leverage.py::band_odds`, `seam/wrappers/sigma.py::odds_of`.
- GLOSSARY: none ("degree band" is the glossary's form for a band of the one ladder: the printed record says "degree").
- COST and TIER: edit; `sonnet` (GO, with IN review).
- LANDS IT: B34's producer; `Item: B34.17`, `[skip ci]`.

### B34.18 — the field as a scene fixture · `IS-MB-01` step 4 · POINTER (Batch B20)
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE_part2.md` "Item: IS-MB-01" step 4 and its WHERE ("in B34 one line each in `harness/scene.py` and `harness/play_surface.py`"); UNDECIDED U2.
- What it points at: step 4's text, to be carried by B20's item after `IS-MB-01` steps 1–3: "`harness/scene.py::FIXTURES["field"]` names `field_scene.build` and its opening `march`; `play_surface --scenario field` resolves to the same builder." `field_scene.py` is created in B20 (`04_MB_playable_field_scenario` §A), after B34; `harness/scene.py` is on B20's base from B34.15.
- Target: Batch B20-mb-orders (lane A30), which gains `GATE: Batch B34-go-surface`.
- GATE: none here; B20's item's own (`python -m engine.season.harness.scene mass_battle.resolve_field --fixture field --seed 0` → a record).

### B34.19 — the transcript stops · `U5a_CORE_owed_edits` §F · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_CORE_owed_edits.md` §F ("F in B34 with `11_GO_player_surface_contract_B.md` §8", U3 §4.1 row 12); F-CORE-05, addendum B res. 22, C7; rulings A-49; UNDECIDED U5.
- ADVANCES: GO standalone (S5: no dead end reaches the client).
- INSTRUCTION (copied, the reveal left to B38): "This row adds its end conditions, at the same owner (`engine/season/harness/play_surface.py`), and nothing else: 1. when `SeasonDriver.season(...)["endings"]` is non-empty (`world_q.endings_reached` is computed every season and shown to no one today), the runner stops on the ending **only when the seated person has no continuation** (rule 2's test) and prints the ending [the reveal: `30_GO_F`'s `reveal`, B38, `IS-B3-GO-04`; not printed here]; with a continuation it records the ending and plays on; 2. it stops when the seated person is dead and `carry_on` returns no continuation; with a continuation it re-seats and says so; 3. it stops at `--seasons K`." "The archived design's third end (a player concludes after two of three starting convictions resolve) has no field to read and is **not built**." The rules read the run's ending through `scenarios.run`'s returned `ending` (B11's `season_ending`), not a second reader.
- WHERE: `engine/season/harness/play_surface.py` (the transcript's stop).
- TESTS: in `test_play_surface.py` `[ASSUMPTION: names (E-3)]`, written first and read red: `test_a_reached_ending_with_no_continuation_stops_the_transcript`; `test_an_ending_with_a_continuation_plays_on`; `test_a_killed_seat_continues_under_the_heir`.
- FALSIFIER and CONTROL: "The transcript runs to `K` past a non-empty `endings`" with no continuation. Control: "the transcript's content hash equals the plain run's at seeds 0–2 (GO B's own gate 1)".
- GATE: §F's gate, at two seasons: "A world with a planted roster ending reached in season 1 and a seated person with no continuation ends the transcript at season 1 with the ending's id; the same with a continuation plays on; a seated person killed with an heir continues under the heir"; `python -m pytest engine/season/tests/test_play_surface.py -q` → pass.
- HASH MOVERS: none ("a reader").
- DEPENDS ON: EXISTS-IN-TREE `harness/play_surface.py::carry_on`, `queries/world_q.py::endings_reached`; V12 Batch B11 (`scenarios.run`, `season_ending`); V12 B34.04.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`; `opus` critique at the close (U5a "terminal `opus` critique per batch (… B34 for F)").
- LANDS IT: B34's producer; `Item: B34.19`, `[skip ci]`.

### B34.20 — a run's ending reaches the surface, with its kind · `IS-B3-GO-02` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` "Item: IS-B3-GO-02"; part 1 §2 gap 2; rulings A-49; GD-1 (`rosters.yaml: endings`).
- ADVANCES: GO standalone (S5), and S5 of every scenario; R-04.
- INSTRUCTION (copied): "(1) `harness/play_surface.py`'s transcript runner … runs through `scenarios.run` …, and when the run returns an ending prints one line, `ENDING <name> <kind>`, after the seated person's last `account`, then stops [when B34.19's rules stop it]. (2) The season's reader, which `IS-B2-CORE-02` writes (`season_ending`: `realm_ended` when `world_q.endings_reached(w)` is non-empty, `line_extinct` when `carry_on` returned no person, `time` at the count), gains the seat's side so that each name has one kind: `realm_ended` splits into `realm_held`, when one of the seated person's own live `commit`s is to the faction the reached row's holders cohere under (his own Tenures, read as `Situation.holdings` reads them), and `realm_fallen` otherwise; with nobody seated it stays `realm_ended`. Kinds: `realm_held` `won`; `realm_fallen` and `line_extinct` `lost`; `realm_ended` and `time` `drawn`. `time` is the headless stand-in for "the player concludes". `[ASSUMPTION: a seat of the faction that holds the peninsula has won — basis: GD-1 as `rosters.yaml: endings` quotes it names the one victory, and the roster row's `under: one_faction` names the winner as a faction. The split is an amendment to `IS-B2-CORE-02`'s reader, made in this item's batch.]` (3) What the client is shown at an ending: the name and kind, `chronicle(p)` and the whole `account`, and nothing of the world's truth. The antecedents `endings_reached` computes stay host-side and reach the client only through `reveal` (`IS-B3-GO-04`). (4) An ending is read at a season boundary only (the barrier at which a save is allowed), never inside a suspended scene."
- WHERE: `engine/season/harness/play_surface.py`; `engine/season/harness/scenarios.py` (`season_ending` and the `kinds` of the rows that use it); `engine/season/tests/test_play_surface.py`.
- TESTS (copied, written first and read red): "`test_the_transcript_stops_on_an_ending_and_prints_its_kind` (a planted reader); `test_a_realm_ending_is_held_for_a_seat_of_the_holding_faction_and_fallen_for_another` (on the hand-built world `test_in27_endings.py` uses); `test_line_extinct_is_lost_and_a_living_continuation_is_not_an_ending`."
- FALSIFIER and CONTROL: the three tests. "Control: a reader that never returns a name leaves the transcript's hash equal to the plain run's (gate 1 of the surface contract)."
- GATE: `python -m engine.season.harness.play_surface --scenario valley --seed 0 --seasons 2` → ends with an `ENDING` line (`ENDING time drawn` at the count, or an earlier ending) (twelve seasons in the source; A-114); `python -m pytest engine/season/tests/test_play_surface.py engine/season/tests/test_scenarios_runner.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B11 (`IS-B2-CORE-01`, `IS-B2-CORE-02`, `IS-B3-GO-01`); V12 Batch B12c (the `valley` row) — B12c closes at S15, after B34 (S14): the gate's `--scenario valley` is read on the realm row (`--scenario season`) if `valley` is not yet registered at B34's open, and the commit body says which `[ASSUMPTION: the gate's world is any registered row — basis: the item's tests carry the claim; the valley is the source's example]`; V12 B34.19; V12 B34.06 (`Situation.holdings`' reader).
- GLOSSARY: row *ending kind*: "won, lost or drawn, read from the seated person's side", owner `harness/scenarios.py::ENDING_KINDS` (B11).
- COST and TIER: edit; `sonnet`.
- LANDS IT: B34's producer; `Item: B34.20`, `[skip ci]`.

### B34.21 — a snapshot names its scenario; resume · `IS-B3-GO-03` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` "Item: IS-B3-GO-03"; `U5d_GO_owed_edits.md` §1 (B06.06: the snapshot and `decode`).
- ADVANCES: GO standalone (save and resume).
- INSTRUCTION (copied): "`U5d_GO_owed_edits.md` §1's snapshot is the GO-07 encoding of the hashed frames plus four named extras (`world_seed`, `tick`, the act store, the settings digest). A resumed run also needs to know which `ending` reader applies, which is not world state. (1) A fifth extra, `scenario`: a key of `SCENARIOS`, or `None` for a world no scenario built. (2) `decode` returns the name with the world and does not look it up (`state/` may not import the instrument package); `scenarios.resume` refuses an unknown name by value. (3) `scenarios.resume(snapshot, seasons, pick=None, host=None) -> dict`: decodes, looks the row up, and continues `run`'s loop from the decoded world without `build`. The seat is not saved: who is played is the client's own choice and changes at `carry_on`."
- WHERE: `engine/season/state/world.py` (beside the encoder, `decode`); `engine/season/harness/scenarios.py` (`resume`); `engine/season/tests/test_go07_canonical_digest.py`.
- TESTS (copied, two seasons, written first and read red): "`test_a_snapshot_names_its_scenario_and_resume_refuses_an_unknown_one`; `test_a_resumed_run_reaches_the_ending_the_unbroken_run_reaches` (for one registered row: `run(name, 0, 2)` against `run(name, 0, 1)` then `resume(..., 1)`: one hash, one ending)" (six and three seasons in the source; A-114).
- FALSIFIER and CONTROL: the two tests; "Control: §1's own round trip, unchanged, with `scenario` `None`."
- GATE: `python -m pytest engine/season/tests/test_go07_canonical_digest.py engine/season/tests/test_scenarios_runner.py -q` → pass.
- HASH MOVERS: none ("no game path reads a snapshot").
- DEPENDS ON: V12 Batch B06 (B06.06, `decode`); V12 Batch B11 (`scenarios.py`); V12 B34.20.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B34's producer; `Item: B34.21`, `[skip ci]`.

### B34.22 — the character sheet's spaces have a caller · `17_CENSUS_C1A_02` W1 · READING
- SOURCE: `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` W1 ("No edit from this lane"; "W1's gate in B34"); U3 §4.1 row 41.
- The reading (Readings block, R-1).

### B34.23 — a goal's seat-holders are read from his own ledger · `16_PESSIMIST_GO` §1, §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: PES-GO §1, §3, "Exact edits" row `world_q.py`, gates 1–3; ED-IN-0292 (2) (closed 2026-10-26: "a vacancy reaches a person as a claim deposited through the channels, not as a world stamp"); AX-7; rulings A-32, A-33 (a goal's `seat_holders` may name a holder he does not know is dead, and the offer must not correct him); closes F-PES-GO-03.
- ADVANCES: R-08 (a person decides from his own claims); GO's offer names only what he holds.
- INSTRUCTION (copied): "§1. `_goal_referents`, kind `seat_holders` (`queries/world_q.py`). Old (the kind's branch): the subjects of live `hold` Tenures on the listed seats, in `w.tenures` order. New: for each listed seat, the person `p`'s own ledger names as its holder, by the reader `seats_named` already is ("THE SEATS `p` HAS BEEN TOLD OF … the Offices among `person_q.ledger_names(p.ledger)`"), extended to return the holder his latest claim on that seat names (`LedgerReader.latest_about`, the one comparator). A seat he holds no such claim on contributes nobody. He may be wrong: a claim naming a dead or replaced holder forms a question about that person, which the fold then refuses or the world then corrects." "§3. `goal_referents`' `⚠ seat_holders IS A WORLD READ …` paragraph is replaced by one sentence: the kind reads the person's own ledger, per ED-IN-0292 (2)."
- WHERE: `engine/season/queries/world_q.py` (`_goal_referents`' `seat_holders` branch; `seats_named` returns the named holder; `goal_referents`' docstring); `engine/season/tests/test_seat_holders_from_ledger.py`.
- TESTS (copied, written first and read red): "`test_goal_referent_reads_own_ledger`, `test_unheard_holder_forms_no_question_until_a_deposit_names_him`". `test_all_chances_one_reproduces_todays_referents` lands with B34.24.
- FALSIFIER and CONTROL: "A person whose offer names a seat-holder he holds no claim about (gate 1 above zero)." Control at B34.24 (every chance 1.0).
- GATE: `python -m pytest engine/season/tests/test_seat_holders_from_ledger.py -q` → the two tests pass; the realm hash at seed 0 → moved (declared).
- HASH MOVERS: "ledgers at build and the questions formed from them (every seeded world)". EXPECTED RED UNTIL B34.99: the realm pins. Re-pinned at B34.99.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::_goal_referents`, `::seats_named`, `::goal_referents`, `queries/person_q.py::LedgerReader.latest_about`, `::ledger_names`; V12 B34.12; V12 B34.20 (UNDECIDED: the EQUAL items' tests read an EQUAL tree first).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.23`, `[skip ci]`.

### B34.24 — the builder seeds who knows each seat's holder, by a draw · `16_PESSIMIST_GO` §2 · BUILD · HASH MOVER(behaviour)
- SOURCE: PES-GO §2, "Exact edits" rows `populated.py`, `fixtures.py`, `hole_register.yaml`, gates 1–3, "Cost class" (the three chances "an `opus`-or-Jordan judgment"); H-190 (`intent_disclosure`'s keyed chance, the precedent); A-30.
- ADVANCES: R-08; R-05's no-player half (someone acts on a stale belief about a seat).
- INSTRUCTION (copied): "For every seat named by any loaded goal's `seat_holders`, and every person, one keyed draw (`draw(pid, f"knows_holder:{seat}")`) against a chance read from one new fixture block:
  ```
  # data/fixtures.py
  holder_known_chance = {"same_settlement": 0.95, "same_faction_or_goal": 0.9, "elsewhere": 0.5}
  ```
  `same_faction_or_goal` is a person whose own `commit` Tenures include a goal naming that seat or the faction the seat belongs to. On success the builder deposits the claim the record channel deposits for a `hold` opening (source `told_by`, empty `chain`), dated before tick 0. The values are `[ASSUMPTION; medium; Jordan to correct; revert: 1.0 everywhere, which reproduces today's referents]`. No chance is 1.0." The deposit sits beside the acquaintance claims the builder already writes (`seed_acquaintances`). The fixture line carries its `[JUSTIFIED: …]` tag naming its NUMBER row; `engine/season/hole_register.yaml`: one NUMBER row for `holder_known_chance` (B34's H block, slot 1), and "H-203's `cite:` gains the seed".
- WHERE: `engine/season/boot/realm.py` (the seed draw and deposit, beside `seed_acquaintances`); `engine/season/data/fixtures.py` (`holder_known_chance`); `engine/season/hole_register.yaml` (the NUMBER row; H-203 `cite:`); `engine/season/tests/test_seat_holders_from_ledger.py`.
- TESTS: "`test_all_chances_one_reproduces_todays_referents` (gate 2)", written first; and gate 3 as `test_shipped_chances_leave_some_unheard_and_one_learns_later` `[ASSUMPTION: name (E-3)]`.
- FALSIFIER and CONTROL (copied): "A run in which the seeded claims make every person know every holder (the draw is decoration). A goal that never forms for anyone at the shipped chances (the seed is too thin and ambition dies)." "Control, exact: with every chance set to 1.0, the set of `need` questions and their referents returned by `questions_for` for every person at tick 0 equals today's [B34.23's base, before §1]." Gate 3: "At the shipped chances, over seeds 0–9: the share of persons with a `seat_holders` goal who hold no claim on any of its seats at build is neither 0 nor more than a quarter (the draw is a draw); and at least one such person forms the question later in the run [within two seasons], after a deposit names the holder." Gate 1: "The count inside `harness/interactions.py` at seeds 0–2, two seasons: occurrences of a person named through a classed referent and outside the closure = **0**."
- GATE: `python -m pytest engine/season/tests/test_seat_holders_from_ledger.py -q` → pass; `python -m engine.season.harness.interactions` at seeds 0–2, two seasons → the out-of-closure count 0 `[ASSUMPTION: `interactions` prints that count — basis: PES-GO "its count is committed as a reading of `python -m engine.season.harness.interactions` (exists)"; if it prints none, the count is computed in the gate-3 test and the commit says so]`; `python tools/ci_sim_fabrication_check.py` → exit 0 (the new fixture's tag).
- HASH MOVERS: "ledgers at build" (every seeded world). Re-pinned at B34.99.
- DEPENDS ON: V12 B34.23; V12 Batch B03c (`boot/realm.py`); V12 Batch B06 (`draw`, the keyed purpose); EXISTS-IN-TREE `harness/populated.py::seed_acquaintances` (moved to `boot/realm.py` by B03c), `hole_register.yaml` H-203.
- GLOSSARY: none.
- NAMES: `harness/populated.py` → `boot/realm.py` (B03c, `CI-07`).
- IDS: H block slot 1 (the NUMBER row).
- COST and TIER: small build; `sonnet`, `high`; the three chances read by `opus` (marked ASSUMPTION; Jordan corrects).
- LANDS IT: B34's producer; `Item: B34.24`, `[skip ci]`.

## Readings (B34)

R-1 (B34.22, `17_CENSUS_C1A_02` W1 "The gate these census rows close on", copied byte for byte): "After GO-B lands: `grep -n "from ..decision.sheet import\|from ..decision import.*\(seat\|development_space\|chronicle\|creation_sheet\)" engine/season/harness/play_surface.py` returns a line, and the entry above exits 0 at seed 0 printing the same hash as the plain run. **Falsifier.** The entry prints a different hash from the unseated run at the same seed (the seat changed the world it was meant only to read)." The entry is `python -m engine.season.harness.play_surface --seed S --person P --seasons K`; read at seed 0, one season, at B34.99.

### B34.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; PES-GO gate 5 ("One re-record of the seeded goldens, said plainly").
- INSTRUCTION: (1) re-record, once, the realm pins in `engine/season/tests/_realm_goldens.py` and every seeded golden B34.23 and B34.24 (and B34.01's branch 2, if taken) moved, reading seeds 0 to 2 against the step's base (`reading @<sha>`); the commit says "re-pin". (2) Read R-1 and every BATCH GATE line; write R-04.c1's `reading:` record in `engine/season/requirements.yaml` (the creation-sheet tests' result and this tree's sha; `status:` not edited, `IS-A-12`). (3) The commit body records the close (§5.12).
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/requirements.yaml` (R-04.c1's `reading:` record).
- GATE: the BATCH GATE.
- HASH MOVERS: the re-pin.
- COST and TIER: reading and a re-pin; `sonnet`, `high`.
- LANDS IT: B34's producer; `Item: B34.99`, the batch's last `Item:` commit (no `[skip ci]`).

| STOP. Batch B34-go-surface closes here |
