# CHK_K7 — check lane K7 (Sonnet), workplan v12 parts 29 to 32 and their continuations

## Status: WORK ORDER (a check lane's table, one round; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite)

**Scope (the brief of `chk_7.txt`, not `V12_STRUCTURE_part3.md` §10.1's grouping, which gives K7 parts 23 to 27):** `workplan_v12_part29.md`, `_part29_cont.md`, `_part30.md`, `_part30_cont.md`, `_part31.md`, `_part31_cont.md`, `_part32.md`, `_part32_cont.md`. Eight batch blocks: B21d-fa-arc, B41-go-port-gate, B11F1-flow-se (29); B20-mb-orders, B25-fi-questioning (30); B27-sc-proceedings (31); B37-happenings, B11F2-flow-in (32). 137 item headings, 137 position rows.

**Rulers used:** `V12_STRUCTURE.md` §5 (via `_part2` §5.2/5.3/6), `V12_STRUCTURE_part3.md` §10.1, `V12_STRUCTURE_part4.md` E-1..E-15 (they win), `workplan_v12_part2.md` §1.3 (the after-lists, HEAD `7257911`) and §11 (the conflicts register). Scripts: scratchpad `k7/parse.py`, `form.py`, `fieldcheck2.py`.

Sections are appended as each check finishes. Findings table at the end of the file (worst first) is written last.

---

## 1. Check 1, forms (script `form.py`, parsed from the files)

| batch | head lines §5.2 in order | INVOCATION exact | `GATE: Batch` = part 2's after-list | positions = items | `.99` position | one boundary row, exact |
|---|---|---|---|---|---|---|
| B21d | yes | yes | yes (2 of 2) | 10 = 10 | B21d.99 "re-pin and close readings" | yes |
| B41 | yes | yes | yes (8 of 8; B17, B20 added by H2 HD-10) | 15 = 15 | B41.99 titled "the close's readings (EQUAL)" | yes |
| B11F1 | yes | yes | yes (1 of 1) | 8 = 8 | B11F1.99 | yes |
| B20 | `SERIAL EDGES` present (carries "(written after the position table, E-11)") | yes | yes (10 of 10) | 23 = 23 | B20.99 | yes |
| B25 | order differs: COST, EST come before SERIAL EDGES, PARALLEL | yes | yes (6 of 6) | 22 = 22 | B25.99 | yes |
| B27 | yes | yes | yes (6 of 6) | 28 = 28 | B27.99 | yes |
| B37 | yes | yes | yes (11 of 11; B29 added by H2 HD-11) | 19 = 19 | B37.99 | yes |
| B11F2 | yes | yes | yes (3 of 3) | 12 = 12 | B11F2.99 "close readings (EQUAL: nothing re-pinned)" | yes |

Every block names its in-flight lane file (`HANDOFF_FA/GO/SE/MB/FI/SC/IN.md`, Open table; B11F1 is SE alone, not a two-lane batch).

## 2. Check 2, fields of §5.3 (script `fieldcheck2.py`; 122 full-form items = BUILD, DESIGN-FIRST, CONTENT and HELD-with-HASH; 12 fields each)

Grade rule used: ABSENT = field line missing; THIN = under 40 characters and not `none`, or "as B21d.07"-style reference, or a COST line with no tier; `.99` positions grade GATE/HASH MOVERS/DEPENDS ON/ADVANCES/GLOSSARY by reference as PRESENT (the form of E-1). NAMES and IDS are conditional and not counted. The 15 POINTER/READING/HELD-without-HASH items (B41.01, B41.12, B11F1.07, B20.18, B20.22, B25.07, B25.08, B25.12, B25.18, B25.21, B37.07, B37.17, B37.18, B11F2.01, B11F2.04) are graded under E-5/§5.3 as pointers/readings (3 to 8 lines, target, gate) and are all present as such.

| field | PRESENT | THIN | ABSENT |
|---|---|---|---|
| SOURCE | 119 | 3 (B21d.08, B21d.09, B27.08) | 0 |
| ADVANCES | 112 | 10 | 0 |
| INSTRUCTION | 121 | 0 | 1 (B27.27, a READING) |
| WHERE | 121 | 0 | 1 (B27.27) |
| TESTS | 120 | 1 (B27.24) | 1 (B27.27) |
| FALSIFIER and CONTROL | 119 | 2 (B21d.08, B21d.09: "as B21d.07") | 1 (B27.27) |
| GATE | 120 | 2 (B21d.08, B21d.09: "as B21d.07.") | 0 |
| HASH MOVERS | 120 | 1 (B20.06 "as B20.05") | 1 (B27.27) |
| DEPENDS ON | 113 | 8 | 1 (B27.27) |
| GLOSSARY | 105 | 16 (a row name and a step number only) | 1 (B27.27) |
| COST and TIER | 122 | 0 | 0 |
| LANDS IT | 121 | 0 | 1 (B27.27) |

B27.27 is a READING that carries a position-table row, an item heading with HASH EQUAL and four fields (SOURCE, ADVANCES, GATE, COST); the other READING items (B20.22, B25.07, B25.21, B37.17, B37.18, B41.12) carry no fields at all, and all READING items have no COST/TIER line, so check 8 grades them "reading, tier not stated" (B27.27 alone says `haiku`; B20.22 says `haiku` inline).

Per batch, PRESENT/THIN/ABSENT cells of the 12 fields over the full-form items: B21d 108/12/0 (10 items); B41 155/1/0 (13); B11F1 81/3/0 (7 incl. B11F1.99); B20 247/5/0 (21); B25 197/7/0 (18); B27 315/13/8 (27); B37 190/2/0 (16); B11F2 120/0/0 (10).

THIN items an agent cannot run from the item alone (check 10) are listed in §9.

## 3. Check 3, gates (scripts `gates.py`, `deps.py`, a grep for season counts)

- **Every named file in a GATE resolves** to the tree (`git ls-files`) or to a `NEW` path of an earlier item. Lists: B21d: `harness/clocks.py` (B21d.04), `test_cr89_clocks.py` (B21d.02), `test_cr90_clock_marks.py` (B21d.04), `test_cr88_duty_of_office.py` (B21d.05), all created before the gate that reads them. B41: `tools/export_oracle_pins.py`, `harness/port_oracle.py`, `test_oracle_pins.py` (B41.06), `test_go12_providers.py` (B41.02), `test_go10_refusal_values.py` (B41.03), `test_surface_trace.py` (B41.05); `harness/scenarios.py` and `test_scenarios_runner.py` come from B11 (reachable: B41 after B34 after B16 after B11); `engine/tests/test_draw.py`, `test_fmath.py` from B06. B20: `field_scene.py`, `test_field_scene.py` (B20.11/.05); `scene.py`/`test_scene_contract.py` from B34 (in B20's after-list); `tools/export_troops.py` from B17 (in list); `tests/valoria/test_conditional_orders.py`, `test_mass_battle_signals.py`, `test_army_battle.py`, `test_army_verbs.py` exist (`git ls-files`). B25: `test_vm_s2_a/b/c/d_*.py` created by B25.02/.04/.09/.19; `test_sc_hearing_evidence.py` by B24 (opened: part22 lines 396-412); `test_conclusion.py` by B11 (part17); `test_task_draw.py` by B07. B27: `test_sc_hearing_sitting.py` by B24; `engine/season/tests/test_sc02_22b_standing_crossing.py` exists (the script's "MISSING" was a path-prefix artefact). B37: `boot/realm.py` does not exist today and is B03c's (B37 follows B03c transitively); the two new tests are B37.15/.16's. B11F2: `test_cr17_odds_weighting.py` and `test_strife_flows.py` exist; `test_cr105_choice_stakes.py` is "or a new" file in HELD B11F2.11.
- **No gate reads past two seasons.** Grep over all eight files for season counts 3 to 24 in gate lines: every source figure of three, four, six, eight, twelve or forty seasons is rewritten at two and says so (B21d "clocks 2 0 1 2"; B25 R1 "four seasons in the source; A-114"; B27.01, .07, .09 "two seasons (six/three/four in the source)"; B37 "two seasons (UNDECIDED (3); 12 seasons in the source)"; B11F2 horizon "two seasons"). One residue that is not a gate: B21d's DIALS/UNDECIDED 2 say the four Church-Influence band flips cannot be crossed in two seasons and leave the question to B98/B99 (finding F-19).
- **No gate is a `## Status:` line or a count read off a document.** The design items B21d.01, B11F1.06 gate on `test -f` plus `grep -c "^## Status: PROPOSED" <file>` → 1, and B27.14/.15/.19/.20/.22/.23 on "the file exists, `## Status: PROPOSED`, states (1) to (n)": allowed for DESIGN-FIRST by `_part2` §5.8, and read by a `ners` critic. B27.08 reads `grep -c "deed:argument.held" engine/season/rosters.yaml` equal to the `argument.won` count (a registry the code reads; an equality that could be wrong, thin).
- **BATCH GATE lines**: all eight carry `register --check`, `--requirements`, `m1_acceptance --summary`, `tests_for_diff.py --base`, `PYTHONHASHSEED`, and the §5.12 close record (script over each block).
- **Gate arms that cannot be wrong** (not fixed): B20.06 and B20.14 each end their GATE on "the seed-2 one-season realm hash → moved or equal, recorded"; their pytest arm is falsifiable. B27.12's GATE adds `modules/social_contest` to a pytest line: that directory holds `__init__.py` and `roll.py` only, so the arm collects nothing (the item's test file still runs). 14 item-level seeded commands in 11 items carry no `PYTHONHASHSEED=0` prefix (B41.07 `port_oracle`; B20.12, B20.21 `field_scene`; B25.03, .14, .15 `aperture 1 s`; B37.05, .10, .16; B11F2.03, .05) against `_part2` §5.8 and each batch's own header line (which says the prefix is on every seeded command); not edited.

## 4. Check 4, dependencies

- `DEPENDS ON` lines: 80 items carry EXISTS-IN-TREE and V12 marks, 39 carry V12 marks only, 2 carry EXISTS-IN-TREE only; no item uses `MISSING` (and no item is `BLOCKED`).
- **EXISTS-IN-TREE opened at the symbol:** 444 backticked tokens were parsed from the 121 lines that carry the mark and each symbol was searched in the named file (script `deps.py`); 28 tokens the script could not place were each re-opened by `grep` over `engine/ modules/ tools/`. 26 are in the tree (e.g. `world_q.docket_question` at `world_q.py:401`, `governing_hold` `:2539`, `person_q.held_against` `:85`, `Fixtures.odds_weighting` `fixtures.py:971`, `Fixtures.field_casualty_model` `:745`, `resolution.tracing`/`trace_event` in `modules/mass_battle/resolution.py:8,25`, `feigned_retreat_recognized` `orchestration.py:2101`, `Person.heritage` `carriers.py:826`, `guard_weight` `world_q.py:1543`, `restrained` `:1766`, `sworn_to` `gate.py:473`). **Two are not in the tree and are marked as if they were:** `stand_draw` (B20.10: `orchestration.py::stand_draw`; no hit in `engine/ modules/`; created by B19.54, part27 position table) and `rosters.yaml: task_fraction` (B25.20: no hit; created by the B07 item at part10_cont2:75-78).
- **`V12 <handle>` resolution (script `vref.py`):** every `Bnn.mm` handle in DEPENDS ON, GATE, TESTS, INSTRUCTION, SOURCE, ADVANCES, WHERE and FALSIFIER resolves to a position row in some part (0 unresolved). Cross-batch handles all belong to a batch in the cited batch's transitive after-list except B25.14's step 6 naming B26.01 (a forward note with its control: "until then the press term reads nothing"). Same-batch handles that point to a later position: 53 mentions (22 in INSTRUCTION, 7 TESTS, 7 GATE, 6 ADVANCES, 5 SOURCE, 3 FALSIFIER, 2 WHERE, 1 DEPENDS ON, 7 in all counted by field). They read as forward notes ("lands with", "until B27.07 the Failure band writes nothing", "turns green at", "recorded for B20.99"); the one in DEPENDS ON is B20.12 → B20.19 and the GATE ones are the pointer rows and B20.05/B20.13 → B20.99, all in §5.

## 5. Check 5, back edges

- Position-table `gates on` cells (script `posgates.py`): no cell gates on a later position, with four exceptions: B20.18, B25.08, B25.18 (POINTER rows whose gate is the built item they point at: B20.19, B25.14, B25.19; H2 §1.1 accepts pointer rows pointing forward) and B27.17.
- **B27.17** is `HELD (Batch B25 closed)` and gates on Batch B25, which is not in B27's after-list (H2 §1.1 HD-08 declined the edge: B25 and B27 open in S16; fallback "B27.17 moves to B32's tail"). Recorded, not a new finding.
- **B11F2.10** is `HELD (Batch B21s-strife-supply and Batch B21b-fa-war closed)`: B21s closes at S18, B11F2 at S17, and neither B21s nor B21b is in B11F2's after-list. H2's list of four forward `gates on` cells (§1.1) does not name it. A HELD row leaves the plan with its trigger, so it executes nothing in B11F2, but the trigger is a later batch (F-7).
- **B20.12** lists `V12 B20.19` under DEPENDS ON for `auto`'s window decider and says it "lands after"; the item is complete without it (F-6).
- B25 gates on B24 and B12c, B11; its steps reach B26.01 only as a note.
- Cut batches: B11F1 depends on B12c (S15) only; B11F2 on B09, B10, B11F1; no item of either depends forward except as above.

## 6. Check 6, hash

- **Movers declared per batch (item HASH tags; match `workplan_v12_part2.md` §1.3):** B21d 1 mover + 3 "if kept" flips (B21d.05; .07 to .09); B41 0; B11F1 3 (B11F1.02, .04, .05); B20 4 (B20.05, .06, .13, .14); B25 11; B27 10; B37 4 (B37.08, .09, .10, .16); B11F2 0 shipped (B11F2.10 conditional, HELD). Every mover batch has exactly one RE-PIN at `.99` (RE-PIN lines read in each block); B41 and B11F2 record EQUAL and re-pin nothing.
- **Encoding movers:** the EQUAL items whose WHERE touches `state/` or a carrier were opened: B41.04 (`_canonical` to `canonical`, a function), B27.02 and B37.12 (`gate.py` constants/keyword, no carrier field), B11F1.01 (explicitly "no `Site.owner` field"), B21d.02 (explicitly "no field added to `Claim`"). `World.content_hash()` reaches `persons, rungs, offices, sites, records, propositions, dates, docket, tenures` and the log (`world.py:1660-1726`); `Question` (B11F2.11, the one new carrier field in these parts) is not among them, and B11F2.11 says so as an `[ASSUMPTION]`. Module-internal classes (B20.20's `Order.ally`, B37.15's `PersonalCombatInput.opener_edge`, B41.05's `SurfaceRow`) are not hashed. No EQUAL item adds, removes or renames a field of a hashed class: no encoding-mover defect found in this range.
- **`EXPECTED RED UNTIL`:** present on B21d.05, B11F1.02, B11F1.04, B20.05 (the shared `_realm_goldens.py` pin, under `[skip ci]`), and, added by this lane, B37.14. Absent where a mover batch's first mover turns the shared pins red: B25 (first mover B25.02), B27 (B27.01; B27.99 says each item's red test is named "in its item's commit body" but no item carries the line), B37 (B37.08), and on B20.06/.13/.14 and B11F1.05, B21d.07 to .09 after the first (the pin is already red, acceptable). F-3, F-4.
- **B37.14**: GATE runs `test_cr87_violence_contexts.py` whole (`→ pass`) while `BASE_BUILD`/`BASE_SEASON` in that file (`test_cr87_violence_contexts.py:52,391,397`) are named in B37.99's RE-PIN line as pins the batch moves: once B37.08 or B37.10 lands those two assertions fail. B37.11 and B37.13 filter with `-k`; B37.14 does not.

## 7. Check 7, words

Grep over the eight files (case-insensitive): `company`, `battalion`, `regiment` 0; `Galbados` 0; `capability` appears only as a code identifier in backticks (B04.04's `capability:` cell, `verb_capability`, glossary row name) except part31's head which says so; `subunit`/`Subunit` appear only in `NAMES:` lines and in quoted source text carrying a correction (B20.16's `Subunit.officer_record` is corrected in its NAMES line); `troops` appears as file/verb identifiers (`troops.yaml`, `assign_troops`, `truncated_troops`) and once as a head-count in prose (B20.05, "the count of troops in engagement groups", from SCN §D); `round` for the season's pass appears only as the quoted source word with its "[lap]" correction (B25.14 `:102`, `:300`) or in NAMES; `riposte` once (part30 head: "none is named in this part"). `squad` (B20.21) is the IS-MB-04 fixture name. No finding.

## 8. Check 8, cost class and tier

COST and TIER is present on 122 of 122 full-form items and names a tier on all of them. Judgment nodes name their reader: DESIGN-FIRST items (8) `opus` with a `ners` critic; calibration B37.10 "the pick read by `opus`"; flips B21d.07 to .09 "the reading `opus`"; the contested B25/B27 rows `opus`; B41.02/.06 a third-tier critic `opus`. Gaps: (a) 15 POINTER/READING/HELD items state no tier and no class (B41.01, B41.12, B11F1.07, B20.18, B20.22, B25.07, B25.08, B25.12, B25.18, B25.21, B37.07, B37.17, B37.18, B11F2.01, B11F2.04; B20.22 says `haiku` in its body, B27.27 states `reading; haiku`); (b) class words outside §5.3's list: "content transcription" (B11F1.04), "edit and instrument time" (B20.99, B25.99), "small build plus data" (B20.10), "content and a small rule" (B41.11), "reading and one build" (B41.14), "small build per module" (B41.08), "re-pin" (B27.99), "edit (register rows) and a small build" (B11F2.05). Not edited.

## 9. Check 10, could an agent execute the item from the item alone?

THIN (an agent that has not read the source could not execute without opening it):
- **B20.10**: the data the edit needs is not in the item: "MNV §3's twelve manoeuvres ... the units and orders of MNV §3's second column, copied cell by cell" and the heading "(the table, copied by reference below)", but no table is below; `_part2` §5.4 requires cited data to be copied. The `stand_draw` call is also marked EXISTS-IN-TREE and is not (F-1).
- **B21d.05**: executes only after B21d.01's design exists (by D-18; its INSTRUCTION is "build what the design states"); every symbol it names is real. Acceptable by rule, listed for the reader.
- **B21d.07, .08, .09**: .08 and .09 are one-line flips whose SOURCE, FALSIFIER and GATE read "as B21d.07"; the trigger fixtures (`turmoil_vassal_war_on`, `nation_functions_on`) are named, but B21d.06 creates them and that is the only place they are defined.
- **B25.08, .12, .18, B20.18, B37.07, B11F2.01, .04, B41.01**: POINTER items, each with the target files and symbols and the gate item (E-5), 3 to 8 lines. Fine as pointers.
- **B27.12**, **B27.24**: B27.12 GATE has a vacuous arm; B27.24's TESTS is "step 2, read on the base and quoted" (a SITE item: the edit depends on what the base shows).
- 14 items exceed E-12's 6 KB hard cap (median item 3.4 KB): B27.01 (11.2 KB), B37.14 (8.5), B27.13 (8.3), B11F2.03 (8.1), B41.06 (7.3), B25.06 (7.1), B37.04 (7.2), B21d.02 (7.0), B11F2.05 (6.6), B27.18 (6.2), B11F2.07 (6.3), B25.19 (6.2), B21d.05 (6.1), B41.08 (6.0). Their text is the copied edit, not the evidence; listed for the batch review, not cut.

## 10. Check 9, copy fidelity: the citations opened (source file and section, item, outcome)

Opened and compared by reading the source text beside the item (matched / drifted / unverifiable); the script `fid.py` additionally searched every test name, path and symbol in each item's WHERE/TESTS/GATE for presence in the cited source.

| item | source opened | outcome |
|---|---|---|
| B21d.01 | `master/eval/E1.md:2135-2160` (CR-88 card and entry) | matched: the five-point charge, the ED-IN-0347 `accept` clause, GATE (design), EXIT, BUILDER copied verbatim |
| B21d.05 | same entry, build half | matched; horizon rewritten from three/four seasons to two and said so |
| B21d.02 | `master/eval/E1.md:2083-2106` (CR-89 commit (1), EXIT, HASH MOVERS) | matched verbatim; the two `[UNVERIFIED]` marks turned into SITE steps as `_part2` §5.7 asks |
| B21d.07 | same entry, commit (4) and CONTROL | matched (keep-or-revert rule copied); not a numeric gate by design |
| B11F1.05 | `workplans/valoria_master_workplan_v11_part16.md:82` (head item 4) | matched verbatim |
| B20.06 | `proposals/04_MB_manager_battle_one_resolver.md` §6 (`:161-173`), Gate 3, Falsifier | matched; the test `test_orders_fired_is_empty_with_no_orders` is marked ASSUMPTION, `test_conditional_orders.py` exists |
| B20.05 | `proposals/04_MB_playable_field_scenario.md` §D, Gate 3 | matched by token search (tests, paths); prose not read line by line: partly verified |
| B20.14 | same file §G and Gate 6 (`:149-170`) | matched (the fixture `field_aftermath` text and the test sentence) |
| B20.13 | `U5b_MB_residue.md` §5, SCN §F | test names are marked ASSUMPTION and are not in the source; paths from other sources; prose not read: partly verified |
| B25.04, .05, .06, .10, .16, .19 | `14_VERBS_SOCIAL2_B/_C/_D`, gate and falsifier sections (S2B `:179` on; S2C `:146`, `:175`) | content matched (gate figures such as weights 1.0 / 0.5 / none, seeds 0-2, two seasons); **drifted in labelling**: the source names no test function ("one function per gate line") and the items' coined names carried no `[ASSUMPTION]` mark in B25.04, .05, .06 (3 of 5), .10, .16, .19 (E-3). Fixed (§12) |
| B27.07 | `16_PESSIMIST_SC_D_an_argument_moves_someone.md` (resolution, edits 1-5, Gate `:130-142`) | matched; three-season realm reading rewritten to two |
| B27.12 | `19_LACUNA_verdict_ladder_and_reversal.md` ("Exact edits" `:105`, "Named tests" `:145`) | matched: the three named tests are the source's own |
| B27.01, .03, .09 | `05_SC_acquittal.md`, `U5c_SC_proceedings_residue.md`, `16_PESSIMIST_SC_C_...md` | matched by token search (every test name in TESTS is in the source); prose not read in full |
| B37.10 | `22_HAPPENINGS_A_...md` head and "What the numbers give" | matched by token search; the per-season target is an `[ASSUMPTION]` the item marks |
| B37.16 | `22_HAPPENINGS_D_batches_and_added_gates.md` (Gate `:126-131`) | matched: the three test names and "from 18" |
| B41.04, .05 | `16_PESSIMIST_GO_surface_pins.md` | matched by token search |
| B41.03 | `master/eval/E1.md` GO-10 and `11_GO_port_gate_order_and_coverage.md` §4 | not opened in E1; the item's quoted text was matched against §4 by token search: partly verified. The Layer 1 hunk is licensed by `ED-IN-0300` (ledger row, status ratified: `registers/editorial_ledger_in.jsonl:77`) |

Totals: 22 items opened or token-searched against 8 source files plus E1 and the v11 part; the 6-per-batch quota is met for the batches that have 6 or more BUILD movers (B25: 6 of 11, B27: 6 of 10 by token search plus 3 by reading) and all movers were taken for B21d, B20 (4 of 4, three read, B20.13 token-only), B37 (3 of 4: B37.08 was token-searched, B37.10 and B37.16 read); B11F1 (B11F1.05 of one BUILD mover; B11F1.02/.04 are CONTENT: the content files were not opened); B41 and B11F2 have no BUILD mover (B41.03, .04, .05 sampled as EQUAL).

## 11. Check 11, Layer 1 rule

- No item makes prose a mechanism. Design items write `proposals/v12_*.md` (design intent, `## Status: PROPOSED`, D-18) and gate on file existence; no item reads a `.md` as input to code. Glossary edits (`unified/U1_GLOSSARY.md`, 28 items) are the glossary rule of `_part2` §5.11 (reference).
- **B41.03** edits `architecture/meta/04_CODE_ARCHITECTURE.md` (§C.12 rejection 5, one paragraph): authorised by the ratified `ED-IN-0300` row (agent may land unmarked `architecture/` text, stated in the PR), and the item stops the hunk if a (RULED) mark sits at the anchor. Not a spec edited to match code (it adds the two result shapes GO-10 builds first). No finding; named for the PR body's "Layer 0/1 hunks".
- Facts live where code reads them: the new tables go to `rosters.yaml`, `fixtures.py`, `troops.yaml` (B20.10), `descriptor_registry.yaml` (B11F1.05) with `[JUSTIFIED: ... H-n]` tags and hole-register rows. B27.08's `grep -c` pair is a count over a registry code loads, not over a document.
- Determinism: every seeded command in the batch gates carries `PYTHONHASHSEED=0` as a block-level rule; 14 item-level commands omit it (§3). Gates over draws state shares and `assert checked >= N` (B25, B27, B37 sampled: B27.07 `>= 300`, B20.10 `>= 200`, B37.12). B25.16's "over seeds 0 to 9 ... all four bands occur" states a share over named seeds but no season count; not edited.

## 12. Fixes applied (small Edit calls, each reread first)

1. `workplan_v12_part30_cont.md`: E-3 marker `[ASSUMPTION: test names; the item creates them — basis: S2x names no function; E-3]` appended to the TESTS of B25.04, B25.05, B25.10, B25.16, B25.19, and widened to all five names in B25.06 (6 edits, 7 lines).
2. `workplan_v12_part29.md` (position row) and `_part29_cont.md` (heading): B41.99 now reads "re-pin and close readings: the EQUAL readings recorded" (the form of B03g.99, B03c.99, B13.99); `_part32_cont.md` (row and heading): B11F2.99 likewise (4 edits).
3. `workplan_v12_part32.md`: B37.14 gains an `EXPECTED RED UNTIL B37.99` line (the `BASE_BUILD`/`BASE_SEASON` tests in `test_cr87_violence_contexts.py`); its GATE reading was not changed (1 edit).
Total 11 edits in 5 files. Earlier-run edits on these parts (commit `f4eb906` and its parent) were not repeated: the two H2 GATE lines in B41 and the B29 line in B37 were already present.

## 13. Counts

PRESENT / THIN / ABSENT cells per field over the 122 full-form items are in §2. Per check, per batch, findings recorded (F-numbers of §14):

| batch | items (pos.) | check 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B21d | 10 (10) | F-10 | F-12 | F-19 | none | none | none | none | none | none | F-17 | none |
| B41 | 15 (15) | F-16 fixed, F-10 | F-12 | F-14 | none | none | none | none | F-13 | none | F-17 | none (B41.03 named) |
| B11F1 | 8 (8) | none | F-12 | none | none | none | none | none | F-13 | none | none | none |
| B20 | 23 (23) | F-11 | F-12 | F-14 | F-1 | F-6 | F-4 (B20.06 to .14 after B20.05 ok) | none | F-13 | none | F-5 | none |
| B25 | 22 (22) | F-11 | F-12 | F-14 | F-2 | F-9 | F-4 | none | F-13 | F-15 fixed | F-17 | none |
| B27 | 28 (28) | none | F-12 | F-14 | none | F-8 | F-4 | none | F-13 | none | F-17 | none |
| B37 | 19 (19) | none | F-12 | F-14 | none | none | F-3 fixed (ER), F-4 | none | F-13 | none | F-17 | none |
| B11F2 | 12 (12) | F-16 fixed | none | F-14 | none | F-7 | none | none | F-13 | none | F-17 | none |

## 14. Findings, worst first

"Fixed" = Y if this lane edited it; "decides" = who must act where N.

| # | batch.item | chk | what is wrong | evidence | fixed | decides |
|---|---|---|---|---|---|---|
| F-1 | B20.10 | 4, 10 | `stand_draw` is marked EXISTS-IN-TREE (`orchestration.py::stand_draw`) but is created by B19.54 (V12); and the item's data (MNV §3's second column, the twelve doctrine rows) is cited, "copied by reference below", not copied, so the item cannot run without the source | `grep -rn stand_draw engine modules` returns nothing; part27 row `| B19.54 | the stand draw ... behind stand_draw: off`; item text part30:283-290 | N | author lane A30 or the orchestrator: change the mark to `V12 B19.54` and paste the table (or cite `file:section` under E-12 and say so) |
| F-2 | B25.20 | 4 | `rosters.yaml: task_fraction` marked EXISTS-IN-TREE (B07); it is created by the B07 item at part10_cont2:75-78, not in the tree | `grep -rn task_fraction engine modules` returns nothing | N | A30: mark `V12 B07.nn` (the item that carries "Exact edits 1") |
| F-3 | B37.14 | 6 | GATE runs `test_cr87_violence_contexts.py` whole and expects pass, while `BASE_BUILD`/`BASE_SEASON` (assertions at `:391`, `:397`) are pins B37.99 re-records and B37.08/.10 already move; item lacked `EXPECTED RED UNTIL` | `test_cr87_violence_contexts.py:52,391,397`; part32 RE-PIN line 41; B37.11 and B37.13 use `-k` filters, B37.14 does not | Y for the missing line; the gate's reading is untouched | A34/the orchestrator: add `-k` or accept red until `.99` |
| F-4 | B25, B27, B37 (also B20.06/.13/.14 trivially) | 6 | The first mover of each batch turns the shared `_realm_goldens.py` pins red, and no item lists it in an `EXPECTED RED UNTIL` line (E-1); B27.99 says each red test is named "in its item's commit body" with no line in any item to say so. Only B21d.05, B11F1.02, B11F1.04, B20.05 follow the form | RE-PIN lines (B25:31, B27:34, B37:41); ER grep: 1 per block at most, none in B25/B37 | N | orchestrator: one rule for all batches (a batch-level line or one ER at each batch's first mover) |
| F-5 | B20 (B20.10, B20.17) | 10 | Data rows (doctrine table; B20.17 "Data rows ... U-9") copied from a table the item points to but does not reproduce, in part | see F-1; B20.17 SOURCE "Data rows (copied, U-9)" not compared | N | A30 |
| F-6 | B20.12 | 5 | DEPENDS ON lists `V12 B20.19`, which lands after (`auto`'s window decider, "lands after"); the item reads complete without it | part30 B20.12 DEPENDS ON; TESTS "(B20.19 ships no cell)" | N | A30: turn the entry into a note |
| F-7 | B11F2.10 | 5 | HELD on `Batch B21s` (closes S18, after B11F2's S17) and `Batch B21b` (not in B11F2's after-list); not among H2 §1.1's four forward gates-on cells | position row part32_cont:63; H2 `workplan_v12_part2.md` §1.1 last paragraph | N | orchestrator: H2's list adds this row, or confirm a HELD row may trigger on a later batch |
| F-8 | B27.17 | 5 | HELD on `Batch B25` which is not in B27's after-list; known and handled by H2 (HD-08 declined; fallback to B32's tail) | `workplan_v12_part2.md` §1.1 | N | none (recorded) |
| F-9 | B25.14 | 5 | step 6 names B26.01 (a later batch) as the source of the press term; control stated ("until then the press term reads nothing") | part30_cont:`B25.14` INSTRUCTION 6 | N | none (a forward note with control) |
| F-10 | B41, B21d | 1 | B41's PARALLEL line still says "S15 with B12c, B18, B19, B21d, B24a" after H2 moved B41 to S18; B21d's PARALLEL, SERIAL EDGES and census still list B41 as an S15 sibling in the merge order | part29:279, :49-50; H2 note at part29:242-243 | N | A29/the orchestrator (H2 left it) |
| F-11 | B25, B20 | 1 | B25's block has COST/EST before SERIAL EDGES/PARALLEL (§5.2 order: C, SERIAL EDGES, PARALLEL, COST, EST); B20 and B25 label the line `SERIAL EDGES (written after the position table, E-11):` instead of `SERIAL EDGES:` | part30_cont:52-56; part30:65 | N | A30 (a reorder, not mechanical enough to take here) |
| F-12 | all | 2 | THIN cells: GLOSSARY 16 (row name and step only), ADVANCES 10, DEPENDS ON 8, SOURCE 3, FALSIFIER/GATE 2 each ("as B21d.07"), HASH MOVERS 1; ABSENT 8 cells all on READING item B27.27; READING items B20.22, B25.07, B25.21, B37.17, B37.18, B41.12 carry no fields | `fieldcheck2.py` output (§2) | N | authors; none blocks execution |
| F-13 | all | 8 | 15 POINTER/READING/HELD items state no cost class or tier; 8 class words are outside §5.3's list | §8 | N | orchestrator |
| F-14 | B20, B25, B27, B37, B11F2, B41 | 3 | 14 seeded item-level commands in 11 items lack `PYTHONHASHSEED=0`; B20.06/B20.14 end on "moved or equal, recorded"; B27.12's `modules/social_contest` arm collects nothing; B27.08 reads a grep count equality | §3 | N | authors (prefix is mechanical, not taken: it touches 14 gates) |
| F-15 | B25.04, .05, .06, .10, .16, .19 | 9, 3 | coined test names without the E-3 `[ASSUMPTION]` mark | §10 | Y | none |
| F-16 | B41.99, B11F2.99 | 1 | position name was not "re-pin and close readings" | §1 | Y | none |
| F-17 | 14 items | 10 | over E-12's 6 KB hard cap | §9 | N | none (listed) |
| F-18 | B41.11 | 4 | the ASSUMPTION fallback says "NEW `tests/valoria/test_names_vocabulary.py` if none"; the grep `grep -rl export_names tests` finds `tests/valoria/test_names_chain.py`, so the fallback would not be taken | `grep -rl export_names tests` | N | A29 |
| F-19 | B21d | 3 | the four Church-Influence band flips (CI cannot exceed 38 in two seasons) are left as "BLOCKED or B99 argv" with the question to A44/H2 | part29:33, UNDECIDED 2 | N | A44/H2: write them BLOCKED (design: target beyond the two-season cap) in B98 or leave to B99 |

## 15. What was not checked

- Prose of source proposals was not read to the end: B20.05, B20.13, B25.04 to .06, .10, .16, .19, B27.01, .03, .09, B37.08, .10, B41.03 to .05 were token-searched, not read line by line; B11F1.02/.04 CONTENT files (`proposals/2026-11-08-flow-conditioning/content_*.yaml`) not opened. Of 66 BUILD movers in these parts, about 22 were compared with their source (10 read in prose).
- Coverage (check 6 of `V12_STRUCTURE_part3.md` §10.1: every U3/intake member appears once) is K1's and was not run. IDs counts (`IDS:` lines) were not recounted. Size/reviewability of B25 (22 positions) and B27 (28 positions, 10 movers) not judged: the brief does not ask.
- No pytest, no seeded run, no engine run: an EXISTS-IN-TREE symbol means "found by grep/read in the file named", not "behaves as the item says". Line numbers in the items (`:1543`, `:1766`, `:473`) were spot-checked true at today's tree and not otherwise.
- Test-function names that exist in the tree vs not were checked by `grep` for 3,125 `def test_` names; the coined names in B20/B25/B27/B37 beyond the six fixed items (33 items hold a new `test_` name with no nearby ASSUMPTION mark; most of those are names the source gives) were not each traced.
- Hash tags were read from item text; `World.content_hash()` reach was read from `world.py:1660-1726`; no executed hash.
