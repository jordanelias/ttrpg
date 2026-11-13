# CHK_K5 — check lane K5 (Sonnet), workplan v12 parts 21 to 24 (with `_cont` files)

## Status: CHECK RECORD (one round; a terminal verdict on parts that exist; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

Parts read: `workplan_v12_part21.md`, `_part21_cont.md` (B21b-fa-war); `_part22.md`, `_part22_cont.md` (B24-sc-hearing); `_part23.md` (B16-pc-round, B08-scene-order); `_part24.md`, `_part24_cont.md` (B12b-weather-arcs-population, B19a-mb-contact-instrument, B29-pc-custody). Seven batches, 147 position handles (144 headed items and 3 READING rows). Scripts: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/k5/` (`parse.py`, `items.py`). Findings are appended below as they are established.

## Progress note (written early; the findings table below is completed at the end)

Mechanical edits applied so far (each target reread before the Edit): B24.18 WHERE gained `NEW engine/season/tests/test_sc_hearing_evidence.py` (the test file is created in B24.18's TESTS "(new)" but WHERE did not say NEW); `EXPECTED RED UNTIL` added to B12b.43 and B29.02 (their GATE names a test file that pins 32-hex season hashes); SOURCE line added to B19a.99 and B29.99 (copied from B12b.99); B12b.06 given a heading and a three-line POINTER body (the position table row had only an unheaded paragraph; part 2 conflict C-25); prose "capability architecture" inside a copied quotation in B12b.37's neighbour (part24.md line 172) corrected to "skill-authoring architecture" with the source wording noted (A-98).

## 1. Findings, worst first

Columns: batch.item · check number (the eleven checks of `V12_STRUCTURE_part3.md` §10.1 as the brief numbers them: 1 forms, 2 fields, 3 gates, 4 dependencies, 5 back edge, 6 hash, 7 words, 8 cost and tier, 9 copy fidelity, 10 coding-instruction charge, 11 Layer 1) · what is wrong · evidence · fixed · who decides.

| # | batch.item | chk | what is wrong | evidence | fixed | who decides |
|---|---|---|---|---|---|---|
| 1 | B24 (11 movers), B21b (5), B08 (2), B12b (11), B29 (2 after fix) = 29 of 47 non-`.99` mover items | 6 | A mover item that leaves the batch's realm pins red until `.99` carries no `EXPECTED RED UNTIL` line (E-1: "a test that is red between its item and `.99` is listed in the item's `EXPECTED RED UNTIL` line"). B24 lists none for any of its 11 movers although its HASH MOVERS lines say "re-pinned at B24.99". The batch RE-PIN line names the realm pins, so an executor can infer the red, but the item form does not say it. | `grep -c "EXPECTED RED UNTIL"` per file: part21 11, part21_cont 4, part22 0, part22_cont 0, part23 3, part24 1, part24_cont 0 (before my two additions); `items.py` list of 31 mover items without the line | partly: added to B12b.43 and B29.02 only (the two where the item's own GATE names a test file that pins 32-hex season hashes: `test_season_weather.py` BASE_HASHES, `test_cr87_violence_contexts.py` BASE_SEASON) | orchestrator: accept the head's RE-PIN line as covering the realm pins, or ask the authors for one line per mover |
| 2 | B12b.43, B29.02 | 3, 6 | After my added `EXPECTED RED UNTIL`, the same item's GATE still reads `pytest ... test_season_weather.py` / `test_cr87_violence_contexts.py` → "pass", a reading that cannot hold while the pin is red. I did not change a gate's reading (brief). | B12b.43 GATE and TESTS ("a moved shipped-arm pin is B12b.99's"); B29.02 TESTS ("`test_cr87_violence_contexts.py` green with the `capture` line") | N | part 24 author lane or the orchestrator: restate the arm as "pass except the pin, red until `.99`" |
| 3 | B21b.05 | 4, 5 | Depends on `V12 Batch B12a` (`09_WR_world_motion` edit 3's settled-territory selector, read by the falsifier's last arm) but carries no `STOPS IF`; B12a → B21b is the edge H2 did not adopt (HD-04), handled "by merge order and the dependent item's `STOPS IF`". B21b.06 has the `STOPS IF`; B21b.05 does not. | B21b.05 DEPENDS ON and FALSIFIER; part 2 §1.1 ("the dependent item keeps its `STOPS IF` (B21.76; B21b.06; …)") | N | author lane (a content decision: the item's last arm waits or is dropped) |
| 4 | B12b.99, B19a.99, B29.99 | 2 | The three `.99` positions carry 4 of the 12 required §5.3 fields (SOURCE, INSTRUCTION, GATE, LANDS IT; B19a.99 and B29.99 lacked SOURCE until my edit). ADVANCES, WHERE, TESTS, FALSIFIER and CONTROL, HASH MOVERS, DEPENDS ON, GLOSSARY, COST and TIER are ABSENT in each (24 cells). B21b.99, B24.99, B16.99, B08.99 carry all twelve. Two forms for one position kind. | `matrix.py` | partly: SOURCE added to B19a.99 and B29.99 (copied from B12b.99); the other cells need content (a cost class, a depends-on list) | orchestrator: accept a short `.99` form or ask for the fields |
| 5 | B24.99, B21b.99, B12b.99, B29.99 | 6 | Re-pin baselines disagree with part 2 §3's merge order. B24 is "5 of 5" movers in S13 but B24.99 reads against "B11's close"; B21b is 4 of 5 but reads against "B21's close, or B12a's after-reading"; B12b is 1 of 4 in S14 but reads against "B12a's close" (the last S13 merger is B24); B29 is 3 of 4 but rebases on "B12b's merge" (B21c merges between). B16.99 (rebases on B08 and B12a) and B08.99 agree with §3. | `RE-PIN:` lines of parts 21, 22, 24; part 2 §3 table rows S13, S14 | N | orchestrator / K1 (baselines are quoted readings; a re-pin re-records current values either way) |
| 6 | 14 items over 6 KB; B16.09 12.5 KB | 9 (size), 10 | E-12 names 6 KB hard per item. Over: B21b.01 6.7, .05 7.0, .06 7.5, .11 6.6, .12 6.0, .13 7.0; B24.02 8.3; B16.01 7.5, **B16.09 12.5** (one commit: consult, view, per-party deciders, `approach_of`, temperament term, withdrawal), B16.11 7.3; B12b.18 7.5; B19a.01 6.1, .02 7.0. Batch sizes: B24 43 positions (11 behaviour movers, 125 KB), B12b 48 (12 behaviour + 1 encoding mover, 137 KB), B21b 28 (15 behaviour + 1 conditional, 113 KB). No lane re-cuts a batch (brief). | `items.py` sizes | N | orchestrator (B16.09 is the one a single producer commit may not hold; U3 §1 item 16 says "one commit") |
| 7 | B21b.10, B21b.12 | 4 | A `MISSING` dependency with an owner, while the item's state is BUILD, not BLOCKED; the batch head's DIALS line calls B21b.10 `BLOCKED (content: IN-08's cell pass)`. The item builds everything but the reward arm (B21b.10) or the war-over-a-killing arm (B21b.12), the E-14 shape (machinery with the dependent term absent), but the state word disagrees with the head. | B21b.10 DEPENDS ON (part21.md:259), B21b.12 DEPENDS ON (:301), head DIALS line | N | orchestrator (state word: BUILD with a stated absent arm, or split) |
| 8 | B21b.25 | 10 | `BUILD (gated on B21b.24)`: its INSTRUCTION is "build what §10 states, edit by edit in its order" of a design B21b.24 has not written. An agent that has not read the design cannot execute it from the item. This is D-18's shape, so THIN by construction, not by omission. | B21b.25 INSTRUCTION | N | none needed beyond the item's own STOPS IF; listed so the reader knows |
| 9 | B24.01 | 4, 10 | Step 2 (plan-added) says `_mint_document(...)` "returns" the record id. In the tree it returns a `Change`; the id is computed inside it (`rid = d.get("record") or f"rec:{a.id}"`, `engine/season/loop/effects_information.py:205-231`, called at :436). The parenthetical gives the right expression, so the executor can recover it. | opened `effects_information.py:205-231, 430-447` | N | author lane (one-word fix: "computes", and read it off the `Change`'s subjects or recompute) |
| 10 | B24.18 | 2, 3 | WHERE did not name `NEW engine/season/tests/test_sc_hearing_evidence.py`, which the item's TESTS creates; seven later B24 gates (B24.19-.21, .25, .27, .32, .37) name it, and part 2's test-file census has no row for it. | `gates.py`: the only gate-named file in none of the tree, a `NEW`, or an earlier TESTS "(new)"; part 2 §6 census rows 158-166 | Y (WHERE now says NEW) | K1: add the census row `test_sc_hearing_evidence.py` / B24.18 |
| 11 | B16.02 | 8 | Cost class "small mechanical rename" is not one of the eight §5.3 classes. A rename across sixteen files is `wide mechanical`. | B16.02 COST and TIER; WHERE lists 16 paths | Y (class corrected, noted in the line) | none |
| 12 | part24.md:172 (B12b.03, copied quotation) | 7 | Prose "the capability architecture's `settlement_effect` site" (the word is retired in prose, A-98; code identifiers keep it). | `words.py` | Y ("skill-authoring architecture's [source: "capability architecture"; A-98]") | none |
| 13 | B12b.06 | 1 | Position row says POINTER; the body was one unheaded paragraph, no heading, no SOURCE/GATE (part 2 conflict C-25). | `parse.py`: 48 positions, 46 headings | Y (heading and a three-line body made from the paragraph and R1; no new content) | none |
| 14 | position-table "gates on" cells: B24.02/.06/.11/.20/.29/.35 name `Batch B05`; B16.11 and B29.01 name `Batch B14` | 1, 5 | Batches that are not in the block's `GATE: Batch` list (they precede it through B07/B10 and B15 respectively). No back edge; the cell is not a `GATE:` line. | `pos.py` | N | none (note only) |
| 15 | B12b.29, .30, .31, .32, .07, .17 | 2 | POINTER bodies: E-5 asks for what the section does, target files and symbols, the gate. The gate is in running text ("Gate: ...") not on a GATE line; B12b.29-.32 carry no SOURCE line (the heading carries it). Content present, form thin. | `matrix.py` | N | none (form note) |
| 16 | B12b.44, B12b.43 (R1), B12b.47 | 3 | D-17 is respected (two seasons, "eight in the source; A-114"), but the copied quotation keeps "eight seasons" inside the quotation marks next to the correction; an executor reads two horizons. | part24_cont.md: B12b.44 INSTRUCTION; R1 | N | none (note) |
| 17 | B12b.? (part24_cont.md:262, R1 of `07_SE_...` copy) | 7 | "in rounds ... rounds repeat until one moves" is a third sense of *round* (a distribution pass of the larder walk). It is a copied quotation, not a fight, not the season's pass. | `words.py` | N | none (note; glossary row if the word recurs) |
| 18 | B19a.01 (title and prose), B12b.47 (quotes) | 7 | "the troop file", "a class of troops", "troop stat" in prose (code ids `troops.yaml`, `troop_types/` keep their names). No company/battalion/regiment anywhere. | `words.py` | N | MB lane (A-99: unit) |
| 19 | authors' `EST:` lines | 8 | B24 22 h, B16 10 h, B12b 26 h, B21b 14 h against part 2's table 19.7, 7.7, 21.7, 13.7 (part 2 §1.3 says its figures govern). | head lines vs part 2 §1.3 | N | none |

**Checked and found clean (so a reader need not re-open them):** block head lines and their order in all seven batches; exactly one boundary row per batch, text exact; a `Bnn.99 — re-pin and close readings` position in each (B19a.99 is the EQUAL record); every `GATE: Batch` line equals part 2 §1.3's after-list (7 of 7); INVOCATION and IN-FLIGHT ROW exact and the lane files exist (`HANDOFF_FA/SC/PC/IN/SE.md`); the position table lists every handle once (147 rows) and every row's state and hash cell equal its heading (0 mismatches); every BATCH GATE carries `register --check`, `--requirements`, `m1_acceptance.py --summary`, `tests_for_diff.py --base`, `PYTHONHASHSEED=0` and the close's record; no in-batch back edge in a `gates on` cell or a DEPENDS ON line; no cross-batch DEPENDS ON or GATE handle outside the batch's predecessors (every other mention of a later batch is a forward note, read in context); no seasons past two in any gate (every four- or eight-season source reading is rewritten with "A-114"); no gate is a `## Status:` line or a document count (the three "the file exists" gates are DESIGN-FIRST items B21b.24, B24.12, B24.41, which §5.8 allows); no `NEW` path is created twice, none already exists in the tree (46 `NEW` paths); no item makes a `.md` the head of a game fact and none edits `systems/`; no determinism (no `random`, clock or environment read).

## 2. Counts

### 2.1 Check 2: the twelve required fields (SOURCE, ADVANCES, INSTRUCTION, WHERE, TESTS, FALSIFIER and CONTROL, GATE, HASH MOVERS, DEPENDS ON, GLOSSARY, COST and TIER, LANDS IT) on the 128 full-form items (BUILD, DESIGN-FIRST, CONTENT). NAMES and IDS are conditional (omit if none) and are not graded. A cell is THIN where the item defers its body to a document another item writes (B21b.25 INSTRUCTION) or the field reads only "none" where the item creates a test (none found). Short but sufficient cells ("none (a reading)", "none new", "none (a design)", "R-04.c3.") are PRESENT.

| batch | positions | full-form items | pointer / held / reading rows | cells | PRESENT | THIN | ABSENT |
|---|---|---|---|---|---|---|---|
| B21b | 28 | 22 (21 BUILD, 1 DESIGN-FIRST) | 6 pointers | 264 | 263 | 1 (B21b.25 INSTRUCTION) | 0 |
| B24 | 43 | 41 (39 BUILD, 2 DESIGN-FIRST) | 1 pointer (B24.42), 1 reading (B24.39) | 492 | 492 | 0 | 0 |
| B16 | 13 | 11 | 1 pointer (B16.10), 1 reading (B16.12) | 132 | 132 | 0 | 0 |
| B08 | 7 | 7 | 0 | 84 | 84 | 0 | 0 |
| B12b | 48 | 39 (38 BUILD, 1 CONTENT) | 7 pointers (B12b.06, .07, .17, .29-.32), 1 held (B12b.26), 1 reading (B12b.34) | 468 | 460 | 0 | 8 (B12b.99) |
| B19a | 4 | 4 | 0 | 48 | 40 | 0 | 8 (B19a.99) |
| B29 | 4 | 4 | 0 | 48 | 40 | 0 | 8 (B29.99) |
| total | 147 | 128 | 15 pointers, 1 held, 3 readings | 1,536 | 1,511 | 1 | 24 |

(Position rows: 28 + 43 + 13 + 7 + 48 + 4 + 4 = 147; headed items 144 (28 + 42 + 12 + 7 + 47 + 4 + 4) after B12b.06 got its heading; the 3 READING rows have no body by §5.3.) Per field, the 24 ABSENT cells are ADVANCES 3, WHERE 3, TESTS 3, FALSIFIER and CONTROL 3, HASH MOVERS 3, DEPENDS ON 3, GLOSSARY 3, COST and TIER 3.

### 2.2 Other counts

- Check 1: 7 batches, 7 heads complete and ordered, 7 boundary rows exact, 7 `.99` positions, 7 of 7 GATE lines equal to the after-list.
- Check 3: 250 test-file, tool and harness-module tokens in the items' GATE lines (counted per item, not distinct): 159 exist in the tree, 83 are created by a `NEW` of this plan in an earlier position or batch, 8 are the one file finding #10 repaired (`test_sc_hearing_evidence.py`, created by B24.18's TESTS "(new)"), 0 unresolved after the fix; tools and harness modules: all exist except `tools/calibrate_mb_contact.py`, `tools/export_mb_contact.py`, `tools/export_troops.py`, `engine/season/harness/duel_scene.py`, which B19a.02, B19a.03, B17 (`part11.md:29, 46`) and B16.11 create before the gate that names them.
- Check 4: 328 backticked path or symbol claims in DEPENDS ON lines; 239 `path::symbol` claims resolved to a file and **defined** there (`def`/`class`/assignment/key; 0 absent, 0 mention-only); 8 further `world_q.x`/`person_q.x`/`faction_q.x` claims defined; 74 file-only claims exist; 15 unresolved by path are all files created by named earlier V12 items (`boot/realm.py` B03c; `references/troops.yaml`, `tools/export_troops.py`, `troop_types/table.py` B17; `decision/decider.py` B10; `engine/dice_engine/draw.py` B06; `harness/scenarios.py` B11; `sigma.py` is `seam/wrappers/sigma.py`, whose `contest_input` and `advantage_sigma` exist). MISSING: 2 (B21b.10, B21b.12), see #7.
- Check 6: 47 non-`.99` mover items (1 encoding: B12b.18; 1 conditional: B29.03; 4 conditional in text). EQUAL items that touch carriers: B08.02 (`Act.after`) is correctly EQUAL, `Act` is not in `_STATE_COLLECTIONS`, `docket` or Event frames (`state/world.py:1660-1707`, item's own argument opened and agreed); B16.01 dataclasses are in `queries/inputs.py`, not hashed. No encoding mover found hiding as EQUAL.
- Check 8: classes: small build 68, edit 27, build 12, reading 9, design 3, calibration 3, content 2, one outside the set (B16.02, fixed); tiers named on every item (sonnet only 79, sonnet+opus 31, opus 7, haiku mixed 8); every DESIGN-FIRST item names opus.
- Words (7): "capability" in prose 1 (fixed); company/battalion/regiment/squadron 0; "faculty"/"faculties" only as code identifiers or NAMES lines; `finalblow_riposte` present in B16 and B12b heads; no season "round" without a `NAMES` line except the third sense in #17.

## 3. Sampled citations (copy fidelity, check 9)

"Matched" means I opened the source and the quoted text is there (spelling, order); "matched in quoted parts" means the item's quoted blocks were found in the named source by a 70-character window probe (not a full diff) and the unmatched windows were plan-added text the item labels "Added by the plan" or `[ASSUMPTION]`; "unverifiable" means I did not open a source for it.

| item | source opened | outcome |
|---|---|---|
| B21b.01 | `master/eval/E1.md:2016-2040` (IN-36 REMAINING UNBUILT (a), EXIT and FALSIFIER, HASH MOVERS) | matched; the cap's text, the falsifier and the hash line are verbatim |
| B21b.04 | `master/eval/E1.md:1481-1486` (CP-T09-04 (b)) | matched; "round" → "lap" is declared in NAMES |
| B21b.06, .11, .13, .26 | E1.md, E2.md, E4.md, E5.md, `proposals/2026-10-24-v10-09-build-B10-17.md` by window probe (2/5, 3/5, 1/5, 2/5 windows found) | matched in quoted parts; the rest is plan-added steps and STOPS IF text |
| B24.01 | `master/instructions/IS_B2_SC_FI_CORE_CHAR.md:141-146` | matched (five steps, test names, gate); one plan-added tree claim inexact, #9 |
| B24.02 | `proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md:15, :46` | matched |
| B24.10, B24.14 | `proposals/05_SC_playable_hearing_B.md:184` (edit 6) and edit 7 | matched |
| B24.35 | `proposals/02_CHAR_which_ground_moves_whom.md` (3/5 windows) | matched in quoted parts |
| B24.27, B24.34 | not opened | unverifiable |
| B16.03 | `proposals/03_PC_duel_round_and_approach_B.md:96-97, :317` | matched (key text, test name) |
| B16.01, B16.09 | token check only (test names and paths found in the sources) | unverifiable beyond tokens; B16.09 is the 12.5 KB item |
| B08.03, .04, .05 | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`, `18_DETERMINISM_rival_acts_in_one_fold.md` (4/5, 2/4, 3/5 windows) | matched in quoted parts |
| B12b.12, B12b.25 | `16_PESSIMIST_WR_A_the_road_is_drawn.md`, `16_PESSIMIST_SE_B_...` (1/2, 1/3 windows) | matched in quoted parts |
| B12b.16 | `proposals/09_WR_provided_arcs.md:84` | matched |
| B12b.18 | tree: `state/carriers.py:1193, :1203`, `write_matrix.yaml:375-381`, `loop/census.py:88`; ruling `unified/DECISIONS_ANSWERED.md` A-115 | matched against the tree and the ruling; the item's source `U5d_SE_owed_edits.md` §3 says "keep the field", so the item follows A-115, which it cites in SOURCE (drift is the cited later ruling, not an error) |
| B12b.44, B12b.47 | `07_SE_ground_and_granaries.md` (3/5), E1/E2 ("ration min over kinds, casualties on all losers") | matched in quoted parts |
| B19a.01, .02, .03 | `MBA_DESIGN.md`, `_part2.md`, `_part3.md` (4/5 windows each) | matched in quoted parts |
| B29.01 | `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md:73-77` | matched (table rows → numbered steps, verbatim); the plan-added "third caller" claim opened in the tree: `loop/effects_information.py:970` |
| B29.02 | same file `:85` | matched |
| B29.03 | window probe 2/4 | matched in quoted parts |

Not every sampled item is a BUILD mover: B24 has 11, B12b 12 behaviour and 1 encoding, B21b 15, B08 3, B29 2 plus one conditional, B16 only B16.03 (so B16.01 and B16.09 were taken as the heaviest EQUAL items), B19a none (all three BUILD EQUAL items sampled). Where a batch has fewer than six movers I took what it has.

## 4. Dependencies opened at the symbol

The 239 + 8 symbol claims of §2.2 were each grepped as a definition in the named file (script `exists3.py` in the scratchpad), not as a mention. That is a presence test, not a signature test: I did not compare argument lists (for example `_docket_item(matter, arrangement, petition, date=None)` exists; the item adds `case=None`, which is its own edit).

## 5. What I did not check

- A full diff of every INSTRUCTION against its source (only the sampled items and the window probes above); the INSTRUCTION of non-sampled BUILD items is unverified against source.
- Semantic truth of EXISTS-IN-TREE claims beyond "defined in that file" (signatures, behaviour, the quoted line numbers inside items, e.g. B12b.18's `:1193`; only the ones I opened are confirmed: `carriers.py:1193, :1203`, `write_matrix.yaml:375-381`, `census.py:88`, `effects_information.py:205-231, :436, :970`).
- Expected readings such as "6 at `b07fc1c`" or "base 10" in gates (they are the sources' own; I ran nothing).
- Cross-part items (the item-level graph, the file census, the id counts, the settings table): K1's.
- Coverage of U3 §2.1 / intake entries by these items (check 6 of §10.1, by script): not in my brief.
- Whether `V12 <handle>` items in earlier batches say what these items rely on (I checked that handles exist in the batch's predecessors, not their content).
- Part 2 conflict C-16 (HD-21: B21b editing `loop/sides.py`): no B21b item edits `sides.py`; B21b.04 only opens `sides_of` as a SITE and `seat_people_at` is B21's (`IS-B3-FA-05`). I read that as resolved; the census row is K1's.
- No pytest, no engine run, no commit (brief).

## 6. Edits made (all in parts 21 to 24; each target reread before its Edit)

1. `workplan_v12_part22.md` B24.18 WHERE: appended `NEW engine/season/tests/test_sc_hearing_evidence.py` (#10).
2. `workplan_v12_part24_cont.md` B12b.43: `EXPECTED RED UNTIL B12b.99` line (#1, #2); B29.02: `EXPECTED RED UNTIL B29.99` line; B19a.99 and B29.99: SOURCE line (#4). The added lines carry `[ASSUMPTION: added by check lane K5 — basis: ...]`.
3. `workplan_v12_part24.md` B12b.06: heading plus a three-line POINTER body (#13); line 172: "capability architecture" corrected in a copied quotation (#12).
4. `workplan_v12_part23.md` B16.02 COST and TIER: class corrected to `wide mechanical` (#11).

Earlier edits from the interrupted run (commit f4eb906, `workplan_v12_part24_cont.md`, 8 lines) were left as found; I did not redo them.
