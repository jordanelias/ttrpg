# CHK_K9 — check lane K9 (Sonnet), workplan v12 parts 36 to 39

## Status: WORK ORDER output (a check lane's one-round report on `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

Read: `workplan_v12_part36.md`, `_part36_cont.md` (B35-wr-thread); `_part37.md` (B23-land) and `_part37_cont.md` (B30-mb-nested); `_part38.md`, `_part38_cont.md` (B33-inst-economy-hands); `_part39.md` (B36-wr-story-instruments) and `_part39_cont.md` (B31-mb-loadout-economy). Against `V12_STRUCTURE.md` §5, `V12_STRUCTURE_part3.md` §10.1, `V12_STRUCTURE_part4.md` (errata win), `workplan_v12_part2.md` (batch table, §11). Scripts (scratchpad `k9/`): `parse.py` (blocks, items, fields), `c1.py` (forms vs part 2), `c2.py` (field grades), `c3*.py` (gate files and tools vs `git ls-files` and the plan's own NEW rows), `c4.py` (seasons), `c5.py` (EXISTS-IN-TREE symbols), `c6.py` (dependency order), `c7.py` (words), `c9.py` (copy fidelity). One round; no second pass on my own fixes. Nothing here is deterministic; nothing was run but `ls`, `git ls-files`, `grep` and the scripts.

## 0. Parse facts

- Six batch blocks. Position rows: B35 30, B23 20 (19 numbered + `B23.R1`), B30 11, B33 49, B36 19 (18 + `B36.R1`), B31 21 = 150. Every position row has exactly one item body or reading entry; no handle twice. Landing order is not numeric where a patch inserted a position (`B30.10` sits after `B30.03`): the table is landing order, not a defect.
- Each block: `INVOCATION` exact; `IN-FLIGHT ROW` names the right lane file (WR, FA, MB, FA, WR, MB); head lines in the §5.2 order (line numbers monotonic); one boundary row, exact; a `Bnn.99 — re-pin and close readings` position last before it; `BATCH GATE` carries `register --check`, `--requirements`, `m1_acceptance --summary`, `tests_for_diff` and the §5.12 record sentence; `PYTHONHASHSEED=0` stated in every one.
- `GATE: Batch` lines equal part 2's after-list set for every batch (B35 10, B23 11, B30 10, B33 16, B36 9, B31 9; part 2's "+R" entries counted). No `GATE: Batch` names a batch closing at or after its own step.

## 1. Findings, worst first

| # | batch.item | check | what is wrong | evidence | fixed | who decides |
|---|---|---|---|---|---|---|
| 1 | B35.22 | 3, 5 | The GATE runs `storybar --world warden --arms off entrenched --null-scenes`. The arm `entrenched` and `--null-scenes` are created by B38.71 (`30_WR_E`, step S20), `--world` by B36.15 (S19); B35 is S18. The command cannot run at B35: a gate on later batches. | `workplan_v12_part41.md:457` ("`ARMS` gains `entrenched`"), `:84`; `workplan_v12_part39.md:371` (`--world` is B36.15's WHERE); tree `storybar.py:87` `ARMS = ("off",)`, no `--world`, no `--null-scenes`; `V12_STRUCTURE_part2.md` §5.8 ("a gate arm that reads the effect of a later item is moved to that item's GATE") | N | the B35 author lane or H2: move the arm to B38.71's GATE |
| 2 | B33.05 | 6 | Says HASH EQUAL but its WHERE adds `Office.passes_through` and `Office.hand_term` to `state/carriers.py` "only where step 0 finds them absent". They will be absent: B32's `SYN_A` item leaves them to B33 (`workplan_v12_part34.md:97`, `:247` "`passes_through`, `hand_term` by B33"). `Office` is a dataclass and `world.py::_object_head` (`:260-268`) hashes the class's field count and every field name, so this is an encoding mover; the item's own gate ("realm hash equal to B33.04's reading") would read red. No mechanism folds an absent field out of the hash (`_encode_into`, `world.py:294-299`). | `carriers.py:1019-1049` (Office; the file's own comment: "`Office`'s encoding folds into `World.content_hash` and carries every field NAME"); B33.05 heading, position row and HASH MOVERS "none (an absent key is not folded into the hash)" | N | H2 or the B33 author: declare MOVER(encoding) (heading, position row, HASH MOVERS, GATE control) and list it in B33.99's re-pin |
| 3 | B35.22 (and B35 BATCH GATE) | 3, 4 | Names `engine/season/tests/test_scenarios.py` as a test file (WHERE, GATE and the batch gate's pytest list). It is not in the tree and no item creates it; B11 creates `test_scenarios_runner.py` (`workplan_v12_part16.md:177`, also `part17_cont.md:95`, which add rows to that file). | `git ls-files` (no `test_scenarios.py`); plan grep | N | B35 author: name `test_scenarios_runner.py` (B11.xx creates it) or mark NEW |
| 4 | B23.04 | 4, 5 | Adds functions to `test_vm_mat_d_paper.py`, which B26.07 creates. B26 (step S17) is not in B23's after-list (part 2 §1) and has slack 2, so only the step number orders them. The register records the pair (C-03) and chose "earlier landing creates"; it did not add the edge. | `workplan_v12_part33_cont.md:480` (B26.07 NEW); `workplan_v12_part37.md:119`; part 2 B23 after-list | N | H2/K1: add B26 to B23's after-list, or let B23.04 create the file |
| 5 | B30.10, B31.17 (B31.08 conditionally) | 6 | Their GATEs run `tools/ci_golden_modes_check.py` and expect "moved" digests; the tool exits 0 only on byte-exact (`ci_golden_modes_check.py` docstring, `return 1 if failures`). Red between the item and `.99`, with no `EXPECTED RED UNTIL`. | GATE text of each; the tool's docstring "Exit 0 iff both modes print [BYTE-EXACT OK]" | Y (B30.10, B31.17); N (B31.08: its reading is "equal, or moved only where `check_drift` fires") | none |
| 6 | all 51 mover items (excluding the six `.99` positions) in the six batches | 6 | No item in these parts carries an `EXPECTED RED UNTIL` line (0 of 150), while other parts do (grep: 40 files). Every behaviour or encoding mover leaves the realm pins in `_realm_goldens.py` (B02's file) red until `.99`; E-1 says to list them. Only the two golden-digest cases (#5) were certain enough to fix. | `grep -c "EXPECTED RED UNTIL"` over parts 36-39: 0, then 2 after K9 | N | H2: one batch-level line ("every mover item is red on the realm pins until `.99`, `[skip ci]`") or per-item lines |
| 7 | B30.09 | 4 | `engine/dice_engine/sigma_leverage.py::opposed_ob` and `::even_line` marked EXISTS-IN-TREE; neither exists. B04.24 creates both (`workplan_v12_part7.md:497-500`; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md:82`). The same line also lists `V12 Batch B05`. | tree grep of `sigma_leverage.py` (functions listed; no such names) | Y: now `V12 B04.24` | none |
| 8 | B30.04 | 1, 4 | `tests/valoria/test_export_battle_orders.py` is in WHERE without NEW and its gate runs it; absent from the tree, created by no item. | `ls`; `grep -rl export_battle_orders tests` (none) | Y: marked NEW | none |
| 9 | B31.02, .03, .04, .05, .08, .14, .17, .18 | 7 | The copied text says "body" for a unit (e.g. B31.02 "A body with a missile weapon…", B31.08 "a body ordered to `reform`"). The lexicon's S-8 says each MB batch author fixes it (`unified/MB_LEXICON_part3.md:178`); `U1_GLOSSARY.md:162` rejects it. B31.04 and B31.08 also wrote new glossary readings with "body". | `c7.py` hits; B30.10 already carries `"body" → unit (S-8)` in NAMES | Y: NAMES lines added to the eight items; the two glossary readings reworded ("a unit moves", "to change a unit's unit formation") | none. Left as is: B31.99's "drifting bodies" (plan prose) and B30.05's "one-person body" (a person's body scale, not a unit) |
| 10 | 16 items: B35.03, .04, .05, .09, .11-.19, .27; B23.04; B33.10; B36.08 | 2, 10 | TESTS names not in any source file of the suite (grep over `proposals/`, `master/`, `unified/`, `audits/` outside `workplan_v12`) and not in the tree, but carry no E-3 mark. B35.11 and B35.14 verified by hand: E1.md gives the falsifier prose and no test name. | `c9`-family grep | Y: `[ASSUMPTION: test names; the item creates them (E-3)…]` appended to each TESTS field | none |
| 11 | B35.28, B35.29 / B23.R1, B36.R1 | 1 | none (clean). B35.28 is `BLOCKED (v12: a carrier is owed)` with MISSING owner "WR lane"; B35.29 and the two R1 rows are READING rows with a Readings block. | | n/a | none |
| 12 | B36.13 | 5 | DEPENDS ON ends "the readers of G1-G5: V12 Batch B38 (PROPOSED)": a later batch named as a dependency. The GATE does not need it (G1-G5 read `n/a (no reader)` at B36), so it is a forward note, not a gate; part 2 §1.1 records such notes as read and accepted (HD-17). | `workplan_v12_part39.md:316`, `:52` | N | H2 (keep as a note or reword) |
| 13 | B31.01 | 3 | GATE includes `grep -c '^## Status: PROPOSED' proposals/2026-11-12-mb-drill-step.md → 1`: a `## Status:` line as a reading (CLAUDE.md §0.05). The design-item rule ("the file exists and states (1) to (4)") already covers it. | `workplan_v12_part39_cont.md` B31.01 GATE | N | B31 author: delete the grep clause |
| 14 | B33.32 | 4 | STATE CONTENT carries `MISSING (SE/FA: CP-T08-07, B33.30)` for its tithe gate; the tithe gate is "not run". Half the item runs (the exempt-house gate), half waits on a HELD item. Acceptable as written; the §5.3 rule says MISSING means BLOCKED. | B33.32 GATE and DEPENDS ON | N | H2 (split or accept) |
| 15 | B35.13, .19, .27 / B23.18 | 2, 10 | THIN: FALSIFIER reads "the pair above" / "the pair" / "the test; control `wound=False`" (no statement of what would show it wrong); B23.18 GATE has no expected reading ("extended with the three assertions"). | item text | N | author |
| 16 | B23 head, B30 head, B36 head | 8 | EST counts: B30 says "10 positions" (11 rows); B23 "20" (20 ✓), B36 "19" (19 ✓). Part 2's table recomputes (B23 10.1, B30 6.9, B36 9.7) and governs. Low. | `EST:` lines vs rows | N | none |
| 17 | B35 head | 7 | "Thread Sensitivity is a practitioner's stat" (`part36.md:11`): "stat" is not one of attribute, skill, skill score, derived score. Low; A-11's own word. | | N | H2 |

Words otherwise clean: no company/battalion/regiment; "troop" appears only as the lexicon's "troops" (men counted) and `troops.yaml` / "troop row"; "capability" appears only in backticked identifiers (`capability:`, `capability_admits`) and the handle `B04-capability-home`; "round" for a season's pass appears only inside `NAMES:` lines that translate it to lap; `finalblow_riposte` stated in B30 and B36 heads; `faculty` only as the retired symbol in NAMES. Bare "formation" (5 hits) is the verb-formation sense (a verb "forms"), not army/unit formation.

## 2. Counts

Per check (defects found / items or blocks examined):

| check | result |
|---|---|
| 1 forms | 6 blocks examined; 0 form defects in heads, tables, boundary rows, `.99` positions, INVOCATION, GATE lists; 1 WHERE missing NEW (#8, fixed) |
| 2 fields | 135 non-exempt items x 12 fields = 1,620 cells: PRESENT 1,602, THIN 18, ABSENT 0 (per batch in the table below). Pointer/reading/blocked/held items (13) graded against E-5, not §5.3 |
| 3 gates | 150 gate sets; 3 defects (#1, #3, #13); 0 past two seasons after restatement (every >2-season source reading is rewritten "(four seasons in the source; A-114)" and read at two: B35.22, B35.26, B33.03/.11/.16/.20/.31/.35/.38, B36.01/.02/.04/.06/.13/.15/.17; `c4.py`) |
| 4 dependencies | 226 EXISTS-IN-TREE symbol tokens string-checked in their files (weak: symbol present in file, not definition-level): 2 false (#7, fixed). 3 `V12`-forward cases found by `c6.py`, 2 are notes (#12; B30.99's merge-baseline reference to B23, same step, §7.4). 1 cross-batch test file not ordered by the after-list (#4). 2 MISSING, both with owners |
| 5 back edges | 1 (#1); 1 forward note (#12) |
| 6 hash | 1 encoding mover called EQUAL (#2); 0 `EXPECTED RED UNTIL` where #5/#6 apply; one re-pin at `.99` in each of the six batches |
| 7 words | 1 pattern (#9, fixed), 1 low (#17) |
| 8 cost and tier | 135 non-exempt items carry a class and a tier; 0 missing tier; design items name `opus` with `ners` (B35.01, .02, B23.01, B30.01, B31.01); CONTENT items sonnet/medium or opus drafting; 0 judgment nodes without a reader tier found |
| 9 copy fidelity | section 3 |
| 10 instruction charge | THIN in the sense of "could not be executed from the item alone": none found of the items opened; weakest: B35.13/.19/.27 (falsifier by reference), B23.18 (gate), #10 (test names unverified) |
| 11 Layer 1 | 0 items make prose a mechanism or a `.md` the head of a fact (WHERE `.md` files are glossary rows, design items, one skill sentence, the ledger `FORK:` rows); the one `## Status:` gate is #13; no undrawn outcome introduced (every outcome gate states a share over named seeds with `checked >= N`, grep of `assert checked`) |

Grades per batch (cells over the 12 fields of §5.3, non-exempt items only; EXEMPT = POINTER, READING, BLOCKED, HELD items):

| batch | items (non-exempt / exempt) | PRESENT | THIN | ABSENT |
|---|---|---|---|---|
| B35 | 27 / 3 | 318 | 6 | 0 |
| B23 | 16 / 3 (+`B23.R1`) | 189 | 3 | 0 |
| B30 | 11 / 0 | 130 | 2 | 0 |
| B33 | 44 / 5 | 527 | 1 | 0 |
| B36 | 18 / 0 (+`B36.R1`) | 214 | 2 | 0 |
| B31 | 19 / 2 | 224 | 4 | 0 |

The THIN cells: B35.02 TESTS and GATE (a design item: "the file exists and states…", D-18, accepted), B35.13/.19/.27 FALSIFIER (#15), the six `.99` GATE cells ("the BATCH GATE, read once": E-1's form), B23.01 and B30.01 GATE (design items), B23.18 GATE (#15), B31.18/.19 INSTRUCTION (one-line value flips, complete), B36.99 and B31.99 DEPENDS ON ("B36.01 to B36.17, B36.R1": a range).

## 3. Sampled citations (what was opened)

Fidelity (check 9): item vs cited source file, WHERE/TESTS/GATE tokens and quoted spans compared by script, then the weak spots by hand. "matched" = every WHERE/TESTS/GATE token and quoted span found or explained; "drifted" = a difference of substance; "unverifiable" = the cited source is a carry-forward block or an audit I could not match line-for-line.

| item | source opened | outcome |
|---|---|---|
| B35.07 | `proposals/14_VERBS_PHYSICAL_D_thread_read.md` | matched (7 of 8 quoted spans verbatim; the eighth is the plan's `STOPS IF`) |
| B35.08 | `proposals/17_CENSUS_REST_2_wiring.md` | matched on quoted spans (4 of 8; the rest are the plan's own step text and repo paths the source abbreviates); WHERE paths are the plan's expansion: unverifiable at line level |
| B35.10 | `master/instructions/IS_B3_FA_SE_WR_GO_part2.md`, `master/eval/E1.md` | unverifiable (the home text is a carry-forward block; 12 WHERE tokens absent from the source are repo paths; 5 test names absent from every source: marked ASSUMPTION already) |
| B35.11, B35.14 | `master/eval/E1.md` (CP-T07-03, -04) | falsifier prose matched; test names not in source (now marked, #10) |
| B35.26 | `proposals/12_ARCS_substrate_as_ground.md` | matched on the gate (the eight-season reading is restated at two, with the source's number kept) |
| B23.02 | `proposals/U5d_FA_land_and_seats_pass_on_a_won_march.md` | partly matched (1 of 7 quoted spans verbatim; the rest are plan additions around `seats=`); unverifiable at line level |
| B23.04 | `proposals/14_VERBS_MATERIAL_D_paper.md` | test descriptions matched to §8; names authored (now marked) |
| B23.13 | `proposals/14_VERBS_BINDING_E_war_seats.md` | matched (3 of 3) |
| B23.14 | same | matched (4 of 7; the rest are plan notes) |
| B23.17, B23.18 | `master/eval/E7.md`, `E8.md` | unverifiable (carry-forward blocks; B23.17 test names flagged ASSUMPTION) |
| B30.03 | `master/instructions/IS_B1_PC_MB_DICE_part2.md` | unverifiable at line level (token check only) |
| B30.05 | `proposals/04_MB_squad_grid_of_named_characters.md` | matched on the table and scale rule (7 of 13 quoted spans; the rest are the plan's wrapper steps) |
| B30.09 | `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` | drifted on one point (#7, `opposed_ob` not in the tree), otherwise matched |
| B30.10 | `proposals/26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` | matched (call-table row "the body's officer is felled or yields … event", line 66) |
| B33.01 | `proposals/15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md` | matched on files; hash tag MOVER(encoding) agrees with the carrier rule |
| B33.08 | `..._BYZANTINE_C_the_hands_of_the_chain.md` | matched (7 of 11 spans); the `passes_through` key text is the SYN_A §3 form |
| B33.16 | `..._COLONIAL_B_distance.md` | matched (3 of 6; the border gate and M-ABROAD gate restated at two seasons) |
| B33.21 | `..._COLONIAL_D_accomplishment.md` | matched (the item says the first test replaces `test_accomplishment.py`, which the plan correctly does not add) |
| B33.25 | `..._PAPACY_D_sanction_and_absolution.md` | matched (4 missing tokens are the plan's names; `_load_alignment` in tree) |
| B33.40 | `..._VENICE_D_houses_charters_and_content.md` | matched on rows; the test name is flagged ASSUMPTION |
| B36.01 | `proposals/09_WR_story_instruments_that_can_fail.md` | matched (10 of 12 quoted spans; the two others are the plan's UNDECIDED (4) text and a restated `edge_null` docstring) |
| B36.10 | `proposals/16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings.md` ("the same file" means the previous item's source) | matched (`:75` the edit, `:82-84` the gate) |
| B36.13 | `proposals/20_NARRATIVE_F_story_inventory_and_gate.md` | matched (5 of 7) |
| B31.08 | `proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` §4, Gate 5 | matched (gate 5 verbatim) |
| B31.17 | same, §2 table and Gate 2 | matched on values (0.6, 0.25); drifted on the gate: Gate 2's reading ("on `forest_broken` in about half to two-thirds; on `uphill` after the foot") is not carried to the flip item, which reads only the digests |
| B31.18, B31.19 | same, Gate 3 and Gate 4 | matched (verbatim) |

Gate files and tools (check 3): every named test file, tool or harness module was checked against `git ls-files` or the plan's NEW rows. All present or created by an earlier item except the four found (#1, #3, #8; B33.21's `test_accomplishment.py` is a deliberate non-file). Created by earlier batches and in the after-list: `harness/scene.py`, `test_scene_contract.py` (B34.15), `field_scene.py`, `test_field_scene.py` (B20), `tools/export_troops.py`, `test_export_troops.py` (B17.10), `test_sc_hearing_sitting.py` (B24.03), `test_command_basis.py` (B21.19), `test_inst_syn_a_kit.py` (B32.01), `test_mass_battle_matchups.py` (B19.62), `tools/calibrate_mb_contact.py`, `tools/export_mb_contact.py` (B19a). `storybar` flags used by B36 (`--situations`, `--control`, `--overlaps`, `--stories`) are created by B36's own earlier items.

## 4. Fixes applied (small Edit/script edits in my parts; each target reread first)

- `workplan_v12_part37_cont.md`: B30.09 DEPENDS ON (EXISTS-IN-TREE to `V12 B04.24`); B30.10 `EXPECTED RED UNTIL B30.99` line; B30.04 WHERE (test file marked NEW).
- `workplan_v12_part39_cont.md`: B31.17 `EXPECTED RED UNTIL B31.99` line; NAMES `"body" (a unit) → unit (S-8)` on B31.02, .03, .04, .05, .08, .14, .17, .18; B31.04 and B31.08 glossary readings reworded.
- `[ASSUMPTION: test names…]` marks on the TESTS field of B35.03, .04, .05, .09 (`part36.md`), B35.11-.19 and .27 (`part36_cont.md`), B23.04 (`part37.md`), B33.10 (`part38.md`), B36.08 (`part39.md`).
- Nothing in the earlier interrupted run needed redoing (the `GATE: Batch` lines and boundary rows were already correct).

## 5. Not checked

- Line-for-line copy fidelity of the INSTRUCTION text for the 51 mover items: only the sampled ones above, by token overlap plus hand reads; the E1/E4/E5/E7/E8 carry-forward sources were not read whole.
- Whether each EXISTS-IN-TREE symbol is defined (not merely present as a string) in its file.
- Coverage (every U3 member, instruction item and intake entry appears once): K1's script lane.
- The settings table and file census against part 2 (`DIALS`, `SERIAL EDGES`, `PARALLEL`): K1.
- Whether every mover item's realm-pin test really is red mid-batch (#6): that needs a run.
- Items of other parts that these batches cite by handle (only their existence in position order was checked, by `c6.py`).
