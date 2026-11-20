# Check lane K6 — workplan v12 parts 25 to 28 (with continuations)

## Status: CHECK RESULT (lane K6 of `V12_STRUCTURE_part3.md` §10.1; one round; not canon; resolves nothing at runtime, CLAUDE.md §0.05)

Files read: `workplan_v12_part25.md`, `_part25_cont.md`, `_part26.md`, `_part26_cont.md`, `_part27.md`, `_part27_cont.md`, `_part28.md`, `_part28_cont.md`, `_part28_cont2.md` (3,015 lines). Batches: **B21c-fa-seats** (part 25), **B34-go-surface** (25_cont), **B19-mb-field-calibration** (one block: head in 26, items 26/26_cont/27/27_cont, boundary row in 27_cont), **B12c-material-verbs-and-valley** (28, 28_cont), **B24a-sc-outside-the-room** (28_cont), **B18-pc-content** (28_cont2). 119 body items, 11 non-body rows (2 HELD in B21c, 1 POINTER in B21c, 1 POINTER and 1 READING in B34, 2 HELD + 1 BLOCKED + 1 POINTER + 1 READING in B19, 2 POINTER + 1 HELD + 3 READING in B12c; B12c.23, .24, .31 are READING rows with text in the batch's `## Readings` block, no item heading).

Method: scripts kept in the session scratchpad (`.../scratchpad/k6/`): a block and item parser, a field grader, a gate-file resolver (`git ls-files` against every `*.py` a GATE or BATCH GATE names, and against every `NEW` file any part creates), a dependency and landing-order graph (position tables, `V12 Bnn.mm` marks, `gates on` cells, part 2 §1.3's after-lists closed transitively), an EXISTS-IN-TREE extractor and symbol grep, a test-name matcher (every `test_` name in a TESTS or GATE line against the source proposals and the tree), then reading. Assumptions are marked `[ASSUMPTION: ... — basis]`. No pytest, no run of the engine, no commit.

Tree read: HEAD `c0d3e9e` (checkpoint over `f4eb906`) plus the edits listed under "Fixes applied". Nothing in this file is a decision; it is a table for the orchestrator.

---

## 1. Findings, worst first

Severity: **M** a plan defect that would mis-sequence or mis-tag a build; **L** a form, wording or precision defect; **n** a note. "Fixed" is Y only where I edited my own parts.

| # | batch.item | check | what is wrong | evidence | fixed | who must decide |
|---|---|---|---|---|---|---|
| 1 | B19.60 | 6 | The position-table row says `EQUAL`; the item heading, its HASH MOVERS line and B19.99's mover list say MOVER(behaviour). Part 2 §1.3 (B19: "behaviour 14") and §3 (B19's mover list: 12, 13, 23-26, 51, 58, 61, 63, 64, 70, 67, 68) were generated from the row and leave out `.60`. | `workplan_v12_part27.md:32` (row) against `:266` (heading) and B19.60's HASH MOVERS ("the band Event's `observed` where a season field ends in a rout … declared; `B19.99`"); B19.99 INSTRUCTION names `B19.60` | row Y (now `MOVER(behaviour)`) | H2 / orchestrator: regenerate part 2 §1.3 and §3 for B19 (15 behaviour movers, not 14) |
| 2 | B12c.06, B12c.35 (also B18.04, B24a.01, B24a.02, B19.22) | 4, 5 | Dependencies on batches that are not in the dependent batch's after-list. B12c's after-list is `B12b` alone, and B15 and B34 are not in its closure; the dependencies hold only because B15 closes at S12 and B34 at S14, before B12c opens at S15. B12c.06 `V12 Batch B15 (B15.07: the healing definition row)`; B12c.35 `V12 Batch B34` and a `gates on` cell `B12c.34; Batch B34`. B18.04 (`V12 Batch B12c`, B12c.25), B24a.01 and .02 (`V12 Batch B12c`, B12c.13 .14 .16 .17) are same-step (S15) merge-order dependencies: B24a's are the recorded HD-17 pair, B18's appears only as a merge position in part 2 §3 (B12c 1 of 5, B18 2 of 5) and in B18's RE-PIN line. B19.22 names `V12 Batch B20 … LATER`, a forward note. | deps script (`order.py`, `deps.py`); part 2 §1.3 after-lists | N | H2: add B15 and B34 to B12c's after-list (and a `GATE: Batch` line each), or drop the wording; add B18 after B12c to §1.1's merge-order list |
| 3 | B12c.35 | 2, 10 | DESIGN-FIRST item with six of twelve §5.3 fields ABSENT: ADVANCES, WHERE, TESTS, FALSIFIER and CONTROL, HASH MOVERS, GLOSSARY. Its INSTRUCTION is one sentence naming a design file whose contents ("who reports; to whom; whether it is a management order; what he may say") the agent must invent; its GATE is "the file exists, names its control, and is merged" with no reading. | `workplan_v12_part28_cont.md:248-262` | N | B12c's author lane / orchestrator: write the six fields (the design file's path and the commit's `git diff --stat` control, as B24a.02 does) |
| 4 | B12c.07 | 3 | A gate over a draw reads "`site.restored` > 0 at every seed; at least two degrees among them" over seeds 0-2. `restore` resolves by a task draw; `V12_STRUCTURE_part2.md` §5.8 last sentence: a gate over a draw states a share over named seeds with `assert checked >= N`. The text is the source's own (`14_VERBS_MATERIAL_A` §8). | B12c.07 GATE | N | orchestrator: restate as a share over seeds with `checked >= N`, or accept as a seeded reading (the seeds are fixed, so the reading is reproducible; the claim "at every seed" is not about the draw's law) |
| 5 | B24a.08 | 4 | DEPENDS ON carries `MISSING-until-B28 the writ's delivery (14_VERBS_SOCIAL1_B §1) for two rows`; the state is BUILD with a STOPS IF, not BLOCKED. The form says MISSING has an owner and the item is BLOCKED. E-14 (ship the machinery with the design-dependent term absent) would license it, but the item does not say so. | B24a.08 DEPENDS ON | N | orchestrator: BLOCKED for the two rows, or cite E-14 in the item |
| 6 | B21c.06 | 3 | GATE includes `grep -c "^## Status: PROPOSED" … → 1`, a `## Status:` line read as an execution artifact (CLAUDE.md §0.05); the BATCH GATE's `ls proposals/v12_B21c_court_parliament_bench.md` is allowed for a design item. | B21c.06 GATE; B21c BATCH GATE | N | orchestrator: delete the `grep -c` arm (existence, `git diff --stat` and the six statements remain) |
| 7 | B21c.01 | 10, 11 | The nine ladders' 66 posts are not in the item: the INSTRUCTION says "transcribed from `faction_politics_v30.md` (archived)". An agent that has not read that file cannot write `ladders:`. The fact then lives in `offices.yaml` (code reads it: correct under §0.05) but the item cannot be executed from the item alone. Recorded as content with a recount in the commit body and an `[ASSUMPTION; medium]`. | B21c.01 INSTRUCTION 1; source E1.md CR-32 REMAINING UNBUILT (1) says the same | N | orchestrator: accept (D-19 content item, the source is the only owner) or add the ladder rows |
| 8 | B24a.04 | 10 | The rites' cells are "written `[ASSUMPTION]` from P4 §3.4 as the entry cites it": the cells of `accusatorial` and `inquisitorial` are not in the item. | B24a.04 INSTRUCTION | N | orchestrator: as #7 |
| 9 | B19.17 | 4 | An absence claim that is false: `_spec_span` "is not in the tree at `8c087bc` (grep: none)". `modules/mass_battle/armies.py:51` defines `_spec_span`, and `orderofbattle.py:33` imports it. | `grep -rn "def _spec_span" modules/mass_battle` | Y (clause corrected in place: the symbol is in the tree; the conclusion "not needed" is unchanged) | none |
| 10 | B19 (head) | 6 | `EXPECTED RED UNTIL B19.99` appears only on B19.12's HASH MOVERS line (the field goldens under `engine/tests/`, `tests/valoria/test_field_golden_pins.py`); the other 14 movers (B19.13, .23-.26, .51, .58, .60, .61, .63, .64, .67, .68, .70) do not repeat it and the head carries no batch-level line (B21c, B34, B24a, B18 do). Red from B19.12 to B19.99 is covered by that one line, so no item is left unlisted; the form is thin. | grep `EXPECTED RED` in parts 26-27 | N | orchestrator: add a head line in the form of B34's |
| 11 | B12c (head) | 6 | The head's `EXPECTED RED UNTIL B12c.99` line says "none beyond each item's own `EXPECTED RED UNTIL` line"; no B12c item has one. It also says the realm pins move "from B12c.04"; B12c.04 is hash EQUAL (first mover is B12c.06). | `workplan_v12_part28.md:31`; position table | N | orchestrator: "from B12c.06 (the first mover), under `[skip ci]`" |
| 12 | B12c (part 2 §1.3) | 1 | Part 2 §1.3 lists B12c as "36 (B28 P2 R3 H2 DF1)"; the position table has BUILD 29 (B12c.30 became BUILD under A-116), HELD 1 (B12c.17). | position table `workplan_v12_part28.md:78-` | N | H2 |
| 13 | B21c, B34, B19 (2nd half) | 1 | SERIAL EDGES and PARALLEL stand after the position table; §5.2 and the pilot exemplar (`workplan_v12_part7.md`) put them before it. E-11 says to write them last, not to place them after. B12c, B24a and B18 keep the §5.2 order. | `workplan_v12_part25.md:60-62`, `_part25_cont.md:81-83` | N | orchestrator (cosmetic; the parts are read by humans and by the in-flight reader alike) |
| 14 | B12c.09 | 6 | Heading `HASH EQUAL`; its HASH MOVERS line declares a mover "once `notice_arm` is on" (B11's flip). Conditional on a dial; part 2 counts no conditional mover in B12c. B12c.99 handles it ("B12c.09/.10 if `notice_arm` was on at the open"). | B12c.09 | N | H2 (add a conditional mover) or accept |
| 15 | B12c.33, .99 (and B21c.99, B34.99, B24a.99, B18.99) | 2 | ABSENT cells in §5.3: B12c.33 ADVANCES; the five `.99` items lack ADVANCES and GLOSSARY, B21c.99 and B34.99 also TESTS, FALSIFIER and CONTROL, DEPENDS ON. B19.99 carries all twelve and is the exemplar. | field grader | N | orchestrator (cheap: copy B19.99's lines) |
| 16 | B34.05, .07-.10, .17, .19-.21; B19.23-.26 | 8 | COST and TIER names a tier but no effort level (CLAUDE.md §10: "set it explicitly per call"); 13 items. Non-standard cost class words: B21c.01 ("data and a reader"), B34.01 ("a test, then nothing or one WITNESS rule"), B19.09 ("an instrument repair with a judgment in it"). | cost script | N | orchestrator |
| 17 | B34.20 | 4, 5 | The batch gate and B34.20 read `--scenario valley` "or `--scenario season` if `valley`, B12c's, is not yet registered". B12c closes at S15 after B34 (S14), so the fallback is the only path at B34's close and the valley reading is never taken in B34. The text states the condition; it is not in `C-11`'s list of fallbacks naming a later batch. | B34 BATCH GATE line 3; B34.20 DEPENDS ON | N | H2 (add to §11 C-11) |
| 18 | B12c.28, B18.03 | 4 | EXISTS-IN-TREE symbol imprecise: B12c.28 names `data/files.py` `GOVERNANCE_SPINE`; the tree has `GOVERNANCE_SPINE_YAML` (`engine/season/data/files.py:111`). B18.03 names `contact.py::GRAB_SHORT_REACH_M`; it is a key of `CFG` in `modules/combat/config.py:339`, read by `contact.py:25`. B19.03 names `orderofbattle.py::_UNIT_COMMAND`; the tree has `massbattle.py::_MVP_UNIT_COMMAND` (the item marks it `[ASSUMPTION … grep at the item's open]`, so it is honest). | grep | N | orchestrator |
| 19 | B19.27, B19.52, B19.16 | 4, 5 | BLOCKED (B20) and HELD rows gating forward on B20. This is what those states mean (part 2 §1.1 lists B19.27 and B19.52). B19.27 is a BLOCKED row with prose fields (What it does / Targets / Gate / Owner) in place of §5.3's; it is not an item of B19. | | n | none |
| 20 | B19.17, B19.18 | 7 | Bare "formation" in two item titles (A-99: bare "formation" is refused). | `workplan_v12_part26.md:80-81`, `_part26_cont.md:9,40` | Y ("a unit formation …", "the army formation …") | none |
| 21 | B19.99 | 6 | Its mover list omitted B19.70 (a mover by its own HASH MOVERS line). | `workplan_v12_part27_cont.md:144` | Y | none |
| 22 | B24a.99, B18.99 | 2, 8 | COST and TIER without a cost class; WHERE "the pin files above" (THIN). | | Y (class "reading and a re-pin"; WHERE names `_realm_goldens.py`, and for B24a `test_season_weather.py` `BASE_HASHES[1, 2]` and `test_go07_canonical_digest.py` `BASE`, from the block's RE-PIN line) | none |
| 23 | B18 (head) | 1 | BATCH GATE had no `tools/tests_for_diff.py --base <batch-start-sha>` line (§5.2 requires it); it said only "`tools/tests_for_diff.py` names the rest". | `workplan_v12_part28_cont2.md:21` | Y (line added) | none |

Not defects, recorded so a reader need not re-open them: the position table of B19 is split across parts 26 and 27 with a placeholder row `| B19.51 … B19.99 |` in the first half (the real rows are in part 27); B19.28 is numbered between B19.08 and B19.09 (Patched: P-10) and the order of the position table follows landing order, not numbering; B34's handles .11, .13, .14 and B12c's .26-.27 gap are authors' numbering; B21c.07 and .08 are HELD rows that leave for the held table at the expunge.

---

## 2. Checks, per batch

Counts come from the scripts; "body items" are BUILD, DESIGN-FIRST and CONTENT rows (the rows with a heading and the §5.3 fields), "non-body" POINTER, HELD, READING, BLOCKED.

| batch | positions | body items (non-body) | movers (behaviour) | `.99` | boundary row | `GATE: Batch` = part 2 after-list | INVOCATION | IN-FLIGHT |
|---|---|---|---|---|---|---|---|---|
| B21c | 10 | 7 (3) | 4 | yes, last | 1, exact | yes (B21b) | exact | HANDOFF_FA |
| B34 | 22 | 20 (2) | 2 (+B34.01 in branch 2) | yes, last | 1, exact | yes (8 lines; B16 added by the part, matches §1.3) | exact | HANDOFF_GO |
| B19 | 49 | 43 (6) | 15 (B19.60 corrected) | yes, last | 1, exact (27_cont:157) | yes (12 lines, B29 added by H2) | exact | HANDOFF_MB |
| B12c | 36 | 30 (6) | 13 | yes, last | 1, exact | yes (B12b) | exact | HANDOFF_SE plus a WR pointer row (D-21) |
| B24a | 9 | 9 (0) | 5 | yes, last | 1, exact | yes (B21c, B24) | exact | HANDOFF_SC |
| B18 | 10 | 10 (0) | 4 | yes, last | 1, exact | yes (7 lines) | exact | HANDOFF_PC |

Check 1 (forms): block head lines present in all six (INVOCATION, IN-FLIGHT ROW, GATE lines, REQUIREMENT, BATCH GATE, RE-PIN, IDS, DIALS AT CONTROL, C(...), SERIAL EDGES, PARALLEL, COST, EST; UNDECIDED and EXPECTED RED UNTIL as the pilots' additions); every position row has an item heading except the 15 rows noted; no handle twice; no `.99`-less batch; waves and steps in the heads equal part 2 §1.3 (B18 "W14, S15 (D-20)"). Defects: #12, #13, #23.

Check 2 (fields, 12 per body item: SOURCE, ADVANCES, INSTRUCTION, WHERE, TESTS, FALSIFIER and CONTROL, GATE, HASH MOVERS, DEPENDS ON, GLOSSARY, COST and TIER, LANDS IT; NAMES and IDS are conditional and not counted). PRESENT / THIN / ABSENT cells:

| batch | cells | PRESENT | THIN | ABSENT | where the non-PRESENT cells are |
|---|---|---|---|---|---|
| B21c | 84 | 79 | 0 | 5 | B21c.99: ADVANCES, TESTS, FALSIFIER and CONTROL, DEPENDS ON, GLOSSARY |
| B34 | 240 | 235 | 0 | 5 | B34.99: the same five |
| B19 | 528 | 522 | 6 | 0 | THIN by length, not by content: B19.08, .25, .26 INSTRUCTION (one-key flips or one sentence copied from the source); B19.24, .25, .26 DEPENDS ON (one line) |
| B12c | 360 | 351 | 0 | 9 | B12c.33 ADVANCES; B12c.35 six; B12c.99 ADVANCES, GLOSSARY |
| B24a | 108 | 106 | 0 | 2 | B24a.99 ADVANCES, GLOSSARY |
| B18 | 120 | 118 | 0 | 2 | B18.99 ADVANCES, GLOSSARY |

By field over the 119 body items: SOURCE 119/0/0, ADVANCES 112/0/7, INSTRUCTION 116/3/0, WHERE 118/0/1, TESTS 116/0/3 ("none new" counts as PRESENT), FALSIFIER and CONTROL 116/0/3, GATE 119/0/0, HASH MOVERS 118/0/1 ("none" counts as PRESENT), DEPENDS ON 114/3/2, GLOSSARY 113/0/6 ("none" counts as PRESENT), COST and TIER 119/0/0, LANDS IT 119/0/0 (P/T/A). THIN here is a length floor, so it overstates for one-line flips; the reading judgments are #3, #7, #8 and #10 above.

Non-body rows: POINTER bodies of three to eight lines (E-5): B21c.09 (4), B34.18 (4), B19.65 (7) are inside; **B12c.05 and B12c.27 are one long line each** with the three required contents (what it points at, files, gate) and are PRESENT in content; HELD B12c.17 is two lines, B21c.07/.08 five each.

Check 3 (gates): every `python -m` module and `python tools/…` a GATE or BATCH GATE names is in the tree or created by an earlier item: `engine.season.harness.scene` (B34.15), `…valley` (B12c.28), `tools/export_troops.py` (B17.10), `tools/export_mb_contact.py` (B19a.03). Every test file a GATE or BATCH GATE names that is not in the tree is created by a named earlier item or by itself (`_realm_goldens.py` B02.01; `test_vb_c_turnover.py` B21.13; `test_scenarios_runner.py` B11.05; `test_sc_hearing_sitting.py` B24.03; `test_docket_names_its_case_file.py` B24.01; `test_duel_scene.py` B16.11; `test_governance_spine_play.py` B21.72; `test_finding_what_is_hidden.py` B11.68; `test_notice_draw.py` B11.65; `test_export_troops.py` B17.10; `test_vm_mat_b_stores.py` B12c.11, written as `(NEW; …)`; `test_mass_battle_entry_stamina.py` B19.07 in TESTS, and B31.07 also creates it: the C-03 pattern, K7's lane). No gate reads past two seasons: every `aperture 3 s`, `aperture 4 0` and "twelve seasons" is quoted as the source's with its two-season reading (A-114). Gates with no `→` reading: B21c.06, B12c.35, B24a.02 (design items; allowed) and B19.67 (a calibration printed in the commit body). `Status:`-line gate: #6. Draw asserted certain: #4.

Check 4 (dependencies): 434 `path`, `path::symbol` and bare-symbol tokens extracted from EXISTS-IN-TREE segments of 119 items; 419 resolve on a loose match (file found, name found in the file) and the 15 that do not were opened: 6 are post-rename paths the item says are created by B03c (`boot/realm.py`), 4 are commit SHAs, 3 are marked `[grep at the open]`, 2 are the imprecise symbols of #18; a strict (definition-only) pass flags 45, of which I opened the 14 that name a file and symbol explicitly (`MB_CELL_DAMAGE`, `stores.changed`, `strife_kinds`, `EVENT_KINDS`, `surveil`, `conceal`, `standing_routes`, `RESTRAINT_KINDS`, `faction_q`, `destroy_record`, `degree_from_net`, `field_casualty_model`, `_subsistence_shortfall`, `ProduceInput`): all exist, in a file other than the one my resolver guessed. The one false claim is #9. `V12 Bnn.mm` marks within a batch: no mark names a later position except B12c.30 (`B12c.32` and `.33` "compose on" its stamp) and B19.66 (`B19.68` "deletes it"), both descriptive forward notes. Batch-level references outside the after-list: #2.

Check 5 (back edges): no item gates on a later item or batch. Four `gates on`/DEPENDS marks point at later batches by design: B19.27 and B19.52 (BLOCKED/HELD on B20), B34.18 (POINTER to B20), B24a.08 (MISSING-until-B28, #5).

Check 6 (hash): see #1, #10, #11, #14. Encoding movers: I searched every hash-EQUAL item's WHERE and INSTRUCTION for a field added to, removed from or renamed on `Person`, `Rung`, `Office`, `Site`, `Record`, `Proposition`, `Tenure`, `Event`, `Claim`, `Date` or a `docket` row (the classes `World.content_hash()` reaches through `_STATE_COLLECTIONS`, `_STATE_SEQUENCES`, tenures and events, `engine/season/state/world.py:1660-1700`): none. Records that look like carriers and are not hashed: `Scene.cost` (B34.10, correct), `CreationRow`, `MassBattleInput`, `ContactVector`, `OfferRow`, `VerbRow` (B12c.11). `Office.scope_rung` already exists (B24a.04 changes a value, a declared mover). Every item with a pinned test that is not at `.99` and moves a golden is covered by a head or an item `EXPECTED RED UNTIL` line except as #10 and #11 say. Each `.99` re-pins once and says "re-pin"; each `.99` names its movers (after fix #21).

Check 7 (words): no company, battalion, regiment, banner, aptitude, talent, prowess in prose; "capability" appears only inside code blocks and identifiers (`capability:` rows, `CAPABILITIES`, a copied docstring); "troop" appears only as the troop-type registry and file (`troops.yaml`, "troop loader", "troop class"); `round` for the season's pass is corrected to `lap` where it occurs (B34 line 351, B12c line 317, B34 `NAMES`); `finalblow_riposte` is the only riposte id used (B18). `faculty` appears in B18's batch gate inside a quoted gate, with the A-112 reading said ("read as the skill score in `arms`, `NAMES`"). #20.

Check 8 (cost and tier): 119 of 119 body items carry COST and TIER; judgment nodes name the reader's tier (`opus` reads: B21c.01 transcription, B21c.02-.05 producers, B34.01 branch 2, B34.24's chances, B19.09, B19.12 step 2, B19.23-.26 flips, B12c.34 reading, B24a.08 rows, B18.08-.09 readings). #16, #22.

Check 9 (copy fidelity): section 3. Check 10 (could an agent execute from the item alone): #3, #7, #8; otherwise the median body item has an INSTRUCTION of 1,330 characters with files, symbols, test names and a gate; the shortest are the one-key flips B19.25 and B19.26 (111 and 113 characters), which name key, old and new value, revert and re-export, and B19.08 (233). Check 11 (Layer 1): section 4.

Size (§10.1 item 9; no lane re-cuts): B19 closes 49 positions (44 BUILD, 15 behaviour movers) in one close, B12c 36 (29 BUILD, 13 movers), B34 22 (20 BUILD, 3 possible movers), B21c 10 (4 movers), B24a 9 (5), B18 10 (4). B19 and B12c are the two a single close would find hardest to review.

---

## 3. Copy fidelity: citations opened

Method for "script": every quoted `test_` name in TESTS and GATE (all 103 BUILD/CONTENT items with names) against the source proposals and the tree: 101 found, 2 not (B21c.03 `test_confer_of_an_elected_seat_refused`, a name the item coins for arm (vi) without the `[ASSUMPTION: test name]` mark; B19.25 re-reads B19.21's test); WHERE file basenames against the cited source; gate command modules against the source.

| item | source opened | outcome |
|---|---|---|
| B21c.01 | `master/eval/E1.md:1901-1925` (CR-32 entry, REMAINING UNBUILT 1-4, EXIT, HASH MOVERS) | matched (items 1-5 copied; loader path flagged `[ASSUMPTION]`) |
| B21c.02 | `E1.md:1927-1951` (CR-35 REMAINING UNBUILT 1-7, 9, EXIT) | matched |
| B21c.03 | `E1.md` CR-35 (8) (read to the cut at "ladder step 3 on `01_AXIOMS.md:1681` and") | matched as far as read; the tail of (8) unverifiable (cut off in my read) |
| B21c.04 | `E1.md:1953-1977` (CR-36) | matched |
| B21c.05 | `E1.md:1979-2003` (CR-37) | matched |
| B34.23, B34.24 | `proposals/16_PESSIMIST_GO_the_offer_names_what_is_held.md:90,97,132-149` (the fixture line, "No chance is 1.0", the test names and the three gates) | matched (the added `harness/interactions` ASSUMPTION is marked) |
| B34.01-B34.22 | not opened beyond script (GO-B and the IS-B3 parts) | unverifiable by hand; script: test names matched |
| B19.12 | `master/mb_abstraction/MBA_DESIGN_part3.md:69-90` (MBA-04 steps 0-8, FALSIFIER (a)-(e), GATE, hash movers) | matched (steps 2-4; tests (d), (e) and the pair rule's five rows; GATE) |
| B19.13, .23, .51, .58, .70 | script only (sources `MBA_DESIGN*.md`, `26_MASS_BATTLE_*`, `27_MB_A`) | unverifiable by hand; WHERE files found in the source except `value_pointer_links.json`, `battle_loop.py` (B19.51), `test_mass_battle_yield.py`, `core/contact_draw.py` (B19.58), which the author added; test names matched |
| B12c.06 | `proposals/14_VERBS_MATERIAL_A_mending.md` (lines 11, 32, 175, 206 grepped) | matched on the A-81 clause, the `_eff_tend` clause and the graded-amount edit; WHERE adds `effects_combat.py`, `witness.py`, `sigma.py`, derived from those clauses |
| B12c.07, .12, .13, .14, .19 | script only | unverifiable by hand; test names matched; B12c.12's `sigma.py` and `effects_economy.py`, B12c.14's `test_in33_exchange.py` and B12c.19's `data/rosters.py` are author additions |
| B24a.01 | `E1.md:2662-2684` (CR-58 REMAINING UNBUILT, EXIT, HASH MOVERS) | matched (the data owner `rosters.yaml: consent_acts` is the item's UNDECIDED (4) choice) |
| B24a.04, .05, .06, .08 | script only (E1 CR-60, CR-61, CR-62, CR-63) | unverifiable by hand; test names matched; B24a.04 adds `boot/realm.py` (rename, `NAMES`) |
| B18.05 | `proposals/03_PC_person_inputs_content.md:106-108` (Part D) | matched |
| B18.09 | `proposals/03_PC_loadout_and_carry.md:98,114,132,138` (item 5, Gate 3, the test name) | matched |
| B18.04, .08 | script only | unverifiable by hand; B18.08 adds `fight.py` and `inputs.py` to WHERE |

Per batch, items opened by hand: B21c 5 of 5 movers and the EQUAL .02; B34 2 of 3; B19 1 of 6 sampled; B12c 1 of 6; B24a 1 of 5; B18 2 of 4. The rest of the sample is script-compared, which finds a missing test, file or command and cannot find a changed sentence. Where I say "matched" I read the source at the cited lines.

---

## 4. Layer 1 and §0.05 (check 11)

No item makes prose a mechanism. Game facts land where code reads them: `offices.yaml: ladders:` (B21c.01), `rosters.yaml: consent_acts`, `authority.by_faction`, `larder_reaches`, `store_spoil`, `references/troops.yaml` blocks with `tools/export_troops.py --check` (B19), `engine/engine_params/` via exporters with `--check` (B34.07, B18's `export_engine_params.py --check`). The only `.md` edits in any WHERE are the glossary (reference, with owner pointers), a design file under `proposals/` (B21c.06) and a handoff row (B34.08). B21c.01 reads an archived design file for a one-time transcription and names it by bare filename, as ED-IN-0231 asks. No item uses `random`, `time` or an unkeyed draw; every draw is keyed through the one draw owner (B06) or the keyed contact/volley/stand/captured draws, and the gates over them read shares over named seeds (except #4). The Key substrate is not built on. B34 U3 (a) and B12c UNDECIDED (1) put design-dependent terms behind settings at control (E-14), listed under DIALS AT CONTROL.

---

## 5. Fixes applied (mechanical, in my own parts; each target reread before the edit)

1. `workplan_v12_part27.md:32` — B19.60 position row hash cell `EQUAL` → `MOVER(behaviour)` (#1).
2. `workplan_v12_part26.md:80-81`, `workplan_v12_part26_cont.md:9,40` — "a unit's formation" → "a unit formation"; "the army's formation" → "the army formation" in the B19.17 and B19.18 rows and headings (#20).
3. `workplan_v12_part27_cont.md:144` — B19.99's mover list gains `B19.70` (#21).
4. `workplan_v12_part26_cont.md:34` — B19.17's false "`_spec_span` … not in the tree (grep: none)" corrected to its real site (#9).
5. `workplan_v12_part28_cont.md:448`, `workplan_v12_part28_cont2.md:212` — COST and TIER of B24a.99 and B18.99 gain the class "reading and a re-pin" (#22).
6. `workplan_v12_part28_cont.md` B24a.99 WHERE and `workplan_v12_part28_cont2.md` B18.99 WHERE — "the pin files above" replaced by the named files (#22).
7. `workplan_v12_part28_cont2.md` BATCH GATE — the `tests_for_diff.py --base <batch-start-sha>` line added (#23).

An earlier run of this lane (commits `28a5788`, `f4eb906`) had already added `EXPECTED RED UNTIL` head lines to B21c, B24a and B18; I did not redo them.

---

## 6. What I did not check

- The INSTRUCTION text word for word against its source for every BUILD mover (check 9 as the structure states it: all of them); I opened 12 of the 119 items' sources and compared the rest by script (test names, file names, commands).
- Coverage by script (§10.1 item 6: every member, instruction item and intake entry once) and the item-level acyclicity across all parts; K1's.
- The IDS counts against the blocks, the settings table against the DIALS lines, the names table against the NAMES lines (K1's).
- That `R-04.c1`, `R-04.c4`, `R-04.c6` and the other conjunct ids named in REQUIREMENT lines exist in `engine/season/requirements.yaml` (the file has R-01 to R-09; I did not open the conjunct ids).
- The FILE CENSUS lines (present in B19 only; not required by §5.2) and PARALLEL claims about shared files.
- That a symbol an item says is "EXISTS-IN-TREE" has the signature the item uses; the symbol grep finds the name, not the shape.
- Estimated hours (EST lines) and the per-commit formula.
- Anything about the sources' own correctness (the plan copies; I checked the copy where I opened it).
