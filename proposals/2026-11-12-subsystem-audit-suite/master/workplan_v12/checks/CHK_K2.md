# CHK_K2 — check lane K2 (Sonnet), workplan v12, parts 7 to 11 and their continuations

## Status: CHECK RECORD (one round; reference, not a mechanism; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite)

## Scope and method

Files: `workplan_v12_part7.md` (B04); `_part8.md`, `_part8_cont.md`, `_part9.md` (B05); `_part10.md` (B06); `_part10_cont.md` (B14); `_part10_cont2.md` (B07); `_part11.md` (B17); `_part11_cont.md` (B09). 147 item headings and 148 position rows (B17.13 is a READING row whose text sits in `## Readings (B17)`). Tree read: working tree of 2026-11-13, `git ls-files` for existence. The brief's numbering of the checks is used (1 forms, 2 fields, 3 gates, 4 dependencies, 5 back edges, 6 hash, 7 words, 8 cost and tier, 9 copy fidelity, 10 coding-instruction charge, 11 Layer 1), not `V12_STRUCTURE_part3.md` §10.1's.

Method: scripts in the session scratchpad (`k2/parse.py` parses blocks and `###` headings; `forms.py`, `grades.py`, `paths.py`, `deps2.py`, `refs2.py`, `fidelity.py`, `words.py`) did the counting; every claim below was then opened by hand in the file or the tree. Nothing was run against the engine: no pytest, no seeded run. `[ASSUMPTION: ...]` marks are mine.

## Verdict in one paragraph

The seven blocks are well formed and their copy from the sources is faithful (about 76 % of 1,004 quoted fragments match a suite source byte for byte after normalisation, and the remainder is plan text inside quotation marks, tree docstrings or line-wrap artefacts; no drifted edit text was found in the 25 sampled mover items). No gate reaches past two seasons, no gate is a `## Status:` line, every named command exists or is created by an earlier item, and there is no back edge. What is wrong is smaller and mostly form: two wrong symbol or path names (both fixed), six bare `Part C row` sources (fixed), 20 mover items with no `EXPECTED RED UNTIL`, B04 with no `.99`, and 3 of 7 blocks that put SERIAL EDGES and PARALLEL after the items.

## Findings, worst first

"Fixed" is Y only where this lane edited the file (all three edits are in the working tree and were picked up by the checkpoint commits).

| # | batch.item | check | what is wrong | evidence | fixed | who must decide |
|---|---|---|---|---|---|---|
| 1 | B09.16 | 4 | WHERE and DEPENDS ON claim EXISTS-IN-TREE `loop/resolve.py::_occasion_of`; the function is `_occasion_ids`. The source proposal (`audits/01_CORE_audit_addendum_B.md:90`) uses the old name. An agent who greps the symbol finds nothing. | `engine/season/loop/resolve.py:159` `def _occasion_ids`; `git grep -w _occasion_of -- engine modules` empty; B09.12 in the same batch names `_occasion_ids` | Y (WHERE and DEPENDS ON now say `_occasion_ids`; the quoted INSTRUCTION step 2 keeps the source's word, and WHERE says so) | none |
| 2 | B05.18 | 3 | GATE greps `engine/season/loop/epistemic.py` for `.ending`; no such file. `grep` of a missing file exits 2, so the reading "no read" cannot be observed as written. The source (`proposals/05_SC_contest_record_on_event.md:101`) carries the same wrong path. | `ls engine/season/loop/` has no `epistemic.py`; the module is `engine/season/epistemic.py`; `grep -n "\.ending"` on both real files finds no read | Y (path corrected, the correction said in the GATE) | none |
| 3 | B14.05, .06, .07, .08, .09, .10 | 2, 10 | SOURCE reads "Part C row R-PC-nn" with no file; Part C is not defined in the part. A cold agent cannot find the row. | all six rows are in `proposals/03_PC_typed_outcome_one_door.md` (`^\| R-PC-15 \|` etc., one hit each; R-PC-17 at `:133` quotes the same `core.py` line the item copies) | Y (file added to the six SOURCE lines) | none |
| 4 | 20 mover items outside B05: B04.01, .07; B06.04; B14.02, .03, .07, .15, .16, .24, .27; B07.05; B17.03, .08; B09.01, .05, .07, .08, .11, .12, .21 | 6 | The rule (E-1) is that a test red between its item and `.99` is listed in `EXPECTED RED UNTIL`. Every behaviour or encoding mover moves the realm content hash, and `_realm_goldens.py` (B02's one pin file) reads it, yet none of these items lists the pin test. Only B05 (head line, covers B05.02 on), B05.02/.03/.09/.16, B17.01, B09.10 and B09.02/.06 (own tests) do. B06.04 and B14.07 mention it in running text, not as the line. | `grep -n "EXPECTED RED UNTIL"` over the nine files: head line only in part 8; item lines in B05.02, .03, .09, .16, B06.03, B09.02, .06, .10, B17.01 | N | orchestrator: one batch-head line (B05's pattern) closes it for a batch; adding 20 item lines is the alternative. Lane left it: which pin tests go red is a judgment on `_realm_goldens.py`, which does not exist yet |
| 5 | B04 (B04.26) | 1, 6 | No `Bnn.99 — re-pin and close readings` position; B04.26 is a CONTENT drafting item and the re-pin in one commit, against E-1 (drafting before `.99`, `.99` a code/test commit). | position table ends at B04.26; part 2 §11 C-01 records it and names this lane | N (renumbering: other parts cite B04.26, C-01) | orchestrator (C-01 stands) |
| 6 | B04 | 4 | REM-30 ("HELD, decide at v12 against B04") has no B04 item that records the decision; the close that is due to decide it has no position. | part 2 §11 C-19; intake `:222`; `grep REM-30 workplan_v12_part7.md` empty | N | orchestrator (a held-list row, §8 row 6; E5 Block C37 was not enough to answer it by the ladder) |
| 7 | B04.22 | 4 | DEPENDS ON marks MISSING "(v12: a carrier is owed)" for the writer of another person's skill claim. That is not an owner, and the item stays BUILD. E-14 allows shipping the machinery with the term absent, and the item does (term reads `None`, setting at 0.0, listed in DIALS), but §5.7 says the dependent part becomes BLOCKED with an owner or goes in the receipt. | part 7 `:476`; DIALS line names `confer_fit_weight` BLOCKED in B98 | N | orchestrator (is the half-built term a BLOCKED sub-part, or is E-14 enough?) |
| 8 | B06, B14, B07 | 1 | SERIAL EDGES and PARALLEL sit after the last item, before the boundary row, not in the head between C(...) and COST (§5.2 order). B04, B05, B17, B09 have them in the head. E-11 says "write last", which the authors of parts 10 and 10_cont read as position. | `grep -n "^SERIAL EDGES"`: part 10 `:214`, part 10_cont `:530`, part 10_cont2 `:167` against COST at `:41`, `:25`, `:21` | N | orchestrator (E-11's wording decides; moving long lines was not mechanical) |
| 9 | B09.10 | 6 | Tagged HASH MOVER(encoding). It fills the value of the existing `Receipt.delta`; no field is added, removed or renamed. By D-04 that is a behaviour mover. Part 2 §3 and §1.3 count it as the batch's one encoding mover. | item HASH MOVERS text: "`Receipt.delta`, a field of a hashed record now filled, D-04"; `Receipt` at `state/carriers.py:209` | N | H2 / orchestrator (a count in part 2) |
| 10 | B04.08, B05.10, B05.15, B05.57, B05.64 (two names), B07.04 (two names) | 3 | Test names that exist in neither the tree nor the source and are not marked `[ASSUMPTION: test name; the item creates it]` (E-3). Seven items, nine names. | script `tests_names.py`: 44 names found in neither; 35 marked, 9 not | N | none needed; a mechanical marker to add, left because the item may be creating a name the source gives under another spelling |
| 11 | 21 BUILD items over 6 KB | 10 | E-12's hard cap is 6 KB per item. Over: B04.02, .05, .07 (6.3 to 6.5 KB); B05.02, .09, .10, .14 (10.4 KB), .17, .21, .23, .51, .57, .58, .60, .64; B06.04; B07.01 (9.7 KB); B17.01 (9.4 KB), .03, .10 (8.6 KB). All still carry the exact edit text; none was found unexecutable for size. | `size` column of `fields.py` (characters of the item body) | N | none (E-12 says copy only the exact edit text; the cut would rewrite items) |
| 12 | B04.26, B14.06, B09.15 | 3 | Gate arms that count a line in a document: `grep -c '^### ([a-e])' <draft .md> → 5` (B04.26), `grep -c '^## Status:' <proposal> → 1` (B14.06), `git grep ... CURRENT.md → nothing` (B09.15). Each sits beside an executed check (`register --requirements`, `currency_consistency_check.py`, `freshness_gate.py`), so the gate as a whole is an execution artifact; the document-count arm is weak. | GATE lines | N | none (the items edit a document, so there is nothing else to run) |
| 13 | B14.05 | 3 | `git grep -c "designs/audit/" modules/combat → 0`: with no hit `git grep -c` prints nothing and exits 1, so the stated reading "0" is never printed. | git behaviour; part 10_cont `:173` | N | none; the reading should be "no output, exit 1" |
| 14 | B07.01, B09.05, B05.21 | 8, 4 | Off-vocabulary words: COST class "medium build" (B07.01) and "a value flip and its readings" (B09.05) are not §5.3's classes; dependency mark "MISSING-BY-ORDER" (B05.21) is not EXISTS-IN-TREE, V12 or MISSING. B05.21's meaning is clear (a forward re-read, not a gate). | `grades.py`; part 8_cont | N | none |
| 15 | B05 (part 9) | 1 | Batch head split across two files and two position tables (part 8 ends with a collapsed row `B05.51 … B05.99`); several "gates on" cells in part 9 name prose ("the first half's OBS §4 step 5"), not handles, so a script cannot resolve them (B05.51, .56, .57, .59). Allowed by the lane assignment (lanes A08, A09), so noted only. | part 8 `:81`; part 9 `:48-:56` | N | none |
| 16 | B04.19 | 2 | WHERE omits `NEW engine/season/tests/test_fa_office_capabilities.py`, though TESTS creates it there (B04.21, .22, .23 reuse it). | part 7 `:434` against `:435` | N | none; the TESTS line says "New" |

Not defects, looked at and cleared: the `GATE: Batch` lines equal part 2's after-list for all seven batches (and the invocation text and the in-flight lane file are exact); every boundary row is exact and unique; each block has the thirteen head lines in §5.2 order (apart from #8); the position table lists each handle once and equals the headings; all `V12 handle` references in DEPENDS ON resolve to an earlier item or an `after` batch (script `refs2.py`; the four later-position hits in GATE and FALSIFIER text were forward notes or a gate arm moved on purpose, §5.8); B07.06's POINTER gate "B21.07's" names a later batch's gate, which is what a pointer to a later batch means (part 2 §1.1 records the same).

## Counts per check

| check | scope | result |
|---|---|---|
| 1 forms | 7 blocks | 7 of 7 have the thirteen head lines, exact INVOCATION, exact single boundary row, GATE lines equal to part 2's after-list; 4 of 7 in §5.2 order (B06, B14, B07 not: #8); `.99` position in 6 of 7 (B04 not: #5); position table complete in 7 of 7 |
| 2 fields | 131 bodied items (BUILD 128, CONTENT 1, DESIGN-FIRST 1, `.99` rows included) | 12 fields each, 1,572 cells: 1,547 PRESENT, 25 THIN (after fixing the six SOURCE cells: 19), 0 ABSENT. Table below |
| 3 gates | 131 gated items, 102 distinct `.py` files named in GATE and TESTS | 66 in the tree, 36 created by an item (35 by an earlier or the same item of these parts, B01, B02 or B03; all traced); 5 harness modules, 15 tools, all in the tree except `tools/export_troops.py` (created B17.10); 0 gates past two seasons; 0 `## Status:` gates; 1 wrong path (#2); 3 weak document-count arms (#12) |
| 4 dependencies | 224 `path::symbol` claims plus every EXISTS-IN-TREE leaf, grepped in the file or the tree | 1 false (#1); 4 MISSING marks, 1 with no owner (#7); 1 BLOCKED item (B09.20) with the carrier named as owed |
| 5 back edges | every `V12` reference and "gates on" cell | 0 |
| 6 hash | 87 mover items, 48 EQUAL items | every mover declared and re-pinned at `.99` (B04: B04.26); 0 EQUAL items found adding or renaming a carrier field; 1 mislabel (#9); 20 movers with no `EXPECTED RED UNTIL` (#4) |
| 7 words | prose outside code spans | 0 "capability" in prose except the glossary row names and handle `B04-capability-home`; 0 company, battalion, regiment; "troops" only as the lexicon's own word (B17, "troop file", "troop type"); the one `c.round` is a NAMES-line item (B05.62, `Claim.lap`); riposte code id used correctly; no `round` for the season's pass |
| 8 cost and tier | 131 bodied items | tier named in 131; class in 129 (two off-vocabulary, #14); judgment nodes (B04.26, B05.02, .23, .99, B06.99, B14.07, .27, .28, .99, B07.01, .04, .05, .99, B09.05, .21) name `opus` |
| 9 copy fidelity | 25 mover items sampled, 6 per batch where there are 6 | 25 matched (list below); 0 drifted; parts unverifiable are plan additions |
| 10 charge | 131 bodied items | THIN in the sense "an agent could not execute it from the item alone": none found; weakest: B09.14 and B09.08 (one-line INSTRUCTION, each leaning on the item before), and B14.21 (WHERE "the five files named") |
| 11 Layer 1 | WHERE lists and GATEs | no `.md` under `systems/`; no fact placed in a `.md` that code reads (B04.26 drafts the cast values in a `.md` under `proposals/` by D-19; BA1 lands them); B05.18 names its `Event.ending` use as a departure in a code comment and edits no Layer 1 text; B06 removes the unseeded generators; no new determinism found |

### PRESENT / THIN / ABSENT per batch (bodied items only; POINTER and READING rows have no fields by E-5 and E-10)

Order of cells: PRESENT/THIN/ABSENT. After the six B14 SOURCE edits B14 SOURCE is 27/0/0.

| field | B04 (24) | B05 (35) | B06 (7) | B14 (27) | B07 (5) | B17 (12) | B09 (21) |
|---|---|---|---|---|---|---|---|
| SOURCE | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 (was 21/6/0) | 5/0/0 | 12/0/0 | 20/1/0 |
| ADVANCES | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 18/3/0 |
| INSTRUCTION | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 20/1/0 |
| WHERE | 24/0/0 | 35/0/0 | 7/0/0 | 26/1/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| TESTS | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| FALSIFIER and CONTROL | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 20/1/0 |
| GATE | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 11/1/0 | 20/1/0 |
| HASH MOVERS | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| DEPENDS ON | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| GLOSSARY | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| COST and TIER | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |
| LANDS IT | 24/0/0 | 35/0/0 | 7/0/0 | 27/0/0 | 5/0/0 | 12/0/0 | 21/0/0 |

THIN cells and why: B14.21 WHERE "the five files named" (the files are in INSTRUCTION); B17.99 and B09.99 GATE "the BATCH GATE" (a reference, not a command; the batch gate itself is concrete); B09.03, .07, .08 ADVANCES "as B09.02/.06"; B09.14 SOURCE and INSTRUCTION (one line each, leaning on B09.13); B09.16 FALSIFIER (a quotation with no named control arm). Items over the six-line heads: POINTERs 12 (B04.20, .25; B05.05, .12, .13; B06.07; B14.14; B07.03, .06, .07, .08, .09; B17.06), all 3 to 8 lines as E-5 asks; READING rows 3 (B05.65, B14.17, B17.13) with text in `## Readings`; BLOCKED 1 (B09.20).

Grading note: ABSENT counts a missing label; a field filled only with a back-reference or a bare pointer counts THIN; "edit; `sonnet`, `high`." counts PRESENT (class and tier stated). Grading of the long fields is by length and by the presence of named files, symbols and tests; whether each text is *right* is checks 9 and 10.

## Fixes applied (three files, nine Edit calls, none re-read afterwards)

| file | change |
|---|---|
| `workplan_v12_part11_cont.md` (B09.16) | WHERE: `_occasion_of` → `_occasion_ids` with the note that the source's name is that function at `resolve.py:159`; DEPENDS ON: `loop/resolve.py::_occasion_ids` |
| `workplan_v12_part8_cont.md` (B05.18) | GATE: `engine/season/loop/epistemic.py` → `engine/season/epistemic.py`, correction stated |
| `workplan_v12_part10_cont.md` (B14.05 to .10) | six SOURCE lines gain `proposals/03_PC_typed_outcome_one_door.md` |

No `GATE: Batch` line, banned word, boundary row or INVOCATION needed fixing; the earlier interrupted run had left no edits in these nine files (`git diff HEAD~1` showed none in them).

## Copy fidelity: the sampled citations and what I opened

Method: for the 25 sampled mover items (all that exist where fewer than six: B04 two, B06 one, B07 one, B17 three; six each from B05, B14, B09) every double-quoted fragment of 30 or more characters in INSTRUCTION, TESTS, GATE, FALSIFIER and HASH MOVERS was normalised (backticks, dashes, wraps) and searched in the 567 suite documents (`fidelity.py`). Item-level match counts are in brackets; the unmatched fragments were read and sorted into plan text inside quotes, tree docstrings or wrap artefacts. Sources opened by hand are marked *opened*.

| item | cited source | outcome |
|---|---|---|
| B04.01 | `master/pc_round/PC_ROUND_SPEC_part2.md:214-228` (PCR-4) *opened*; tree `engine/season` `.round` reads counted: 41 in 12 non-test files | matched; WHERE, measuring command and the `rival_key` absence (not in tree) all true |
| B04.07 | `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2a steps 1 to 5, Tests, Check, Falsifier *opened*; tree `populated.py:1359` (`heritage_of`), `Person.capability` | matched; the plan adds `NAMES` and the four rows from `02_CHAR_which_ground_moves_whom` edit 1 |
| B05.02 | `proposals/U5a_DICE_owed_edits.md` §1 rows 1, 2, 3, 5, 8, 9 and Tests (W3-1) *opened* (`:29-:37`, `:55`) | matched row by row (13 of 18 fragments exact; the others are code and grep patterns) |
| B05.14 | OBS `U5c_SC_one_obstacle_form.md` §4 step 1a, SC-B Edits A, B (20 of 25 fragments exact) | matched; the 5 unmatched are lane A symbols (`obstacle_terms`, `task_difficulty`, `ob_terms`) that do not exist until B01, so correctly V12 B01 not EXISTS-IN-TREE |
| B05.20 | U1 §11 U1-D, D-U1-01a (7 of 9) | matched; `Office.modifier` correctly an encoding mover (`Office` is in `_STATE_COLLECTIONS`) |
| B05.23 | CAP Part B / T13 commit 2 / CAL (19 of 23) | matched; the "four seasons in the source; A-114" rewrite to two seasons is present |
| B05.60 | ADV Edits A to D (9 of 10) | matched |
| B05.64 | intake `:422` (H-199), `master/eval/E3.md:669`, tree docstrings `engine/season/decision/options.py:1565`, `queries/world_q.py:783` *opened* | matched; the spacing choice `k / K` is the plan's own and is declared UNDECIDED (7) in the head |
| B06.04 | `11_GO_one_draw_owner` rows 1, 2, 5 and `16_PESSIMIST_GO_keyed_draw_no_recorder` (6 of 11) | matched; the unmatched five are grep patterns and file lists |
| B07.05 | 18-A "The resolution, decided" 3, "Exact edits" 7, `IS-A-10` (12 of 17) | matched; the section names are in files named earlier in the part |
| B14.02, .03 | `03_PC_typed_outcome_one_door.md` Part A; D-U1-06, C3-L5 | matched; `rosters.yaml: fight_endings` and `Event.observed` exist |
| B14.15, .16 | `16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight.md` (11 of 13 and `_eff_kill` rows) | matched; `fell_to_hand` is a roster value, not a carrier field |
| B14.24, .27 | `10_DICE_believed_odds_have_a_prior` Edit C and `U5b_PC_residue` §8; the verb_table note at `engine/season/verb_table.yaml:958` | matched |
| B17.01 | `04_MB_headcount_grade_and_scale.md` (17 of 19) | matched |
| B17.03 | `04_MB_typed_outcome_and_one_path.md:66-78` *opened* ("Shares are integers", "Army path: a part is a cohort") | matched (the script missed both for line wraps) |
| B17.08 | `04_MB_unit_loadout_and_weapon_in_hand_B` (R-24) | matched |
| B09.01 | `01_CORE_claim_fade_as_read` edits; eight seasons rewritten to two (A-114) | matched |
| B09.05 | `16_PESSIMIST_CORE_a_refusal_is_remembered` edit 3, Gate | matched; the value 0.5 is a D-19 authored value, flagged for Jordan in the item |
| B09.10, .11, .12 | `16_PESSIMIST_CORE_the_record_holds_what_changed` edits 1 to 3; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` edits 1 to 3 | matched; `_occasion_ids` in .12 is correct (see #1) |
| B09.21 | intake `:144` (H-135), `master/eval/E6.md` Block 5 | matched |

Beyond the 25: the six B14 Part C items, B14.07's line (`modules/combat/core.py:135` reads `SL.soft_cap(net_sigma) * SL.sigma_n(pool)` as the item says) and B09.16 were opened against their sources; 197 source-file citations in SOURCE fields were resolved by script (1 unresolved: `holonic_ARCHITECTURE.md`, a root-level Layer 1 file, not a suite file).

## What I did not check

- Whether each *unquoted* part of an INSTRUCTION (the plan's own connecting text, the assumptions, the `STOPS IF` lines, the "AT OPEN" steps) is right; only the quoted copy and the named symbols were tested.
- The 106 non-sampled mover and EQUAL items were checked by the script's quote matching, the section-name check (197 source files) and the symbol and path checks, not by reading their sources.
- Line numbers in the items (`:260`, `:424`, `:1164`) were not opened; the V12 plan drops them for files B03a edits and most carry "at `8ce8d6a`".
- Seeded readings and expected values (for example B17.99's seed-2 reading, B05's C1 30.1 %) cannot be verified without a run.
- Whether the hash-EQUAL claims hold: only that none adds, removes or renames a field of a carrier `World.content_hash()` reaches (read from `_STATE_COLLECTIONS` and `_encode_into`), not that the values are equal. Tags for B09.02 to .04, .13 to .19 were taken from the items.
- Check 6 of `V12_STRUCTURE_part3.md` §10.1 (coverage by script), 9 (size across the plan) and K1's graph checks are not in this lane's brief.
- `Fixtures`: whether a new fixture reaches `content_hash` (`B04.22`, `B05.08`, `B09.05`): `Fixtures` is not in `_STATE_COLLECTIONS`, so no; taken from `state/world.py:1660`.
- The glossary rows each item says it edits were not compared with `unified/U1_GLOSSARY.md`.
- Determinism: gates over a draw were read for a share-over-seeds or `checked >= N` where I met one (B04.19, B09.01, B14.16); not every gate was read for it.
