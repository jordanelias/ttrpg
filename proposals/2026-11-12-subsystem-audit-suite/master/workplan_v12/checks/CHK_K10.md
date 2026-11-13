# CHK_K10 — check lane K10 (Sonnet), workplan v12 parts 40 to 43

## Status: WORK ORDER output (a check lane's one-round report on `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

Read: parts `workplan_v12_part40.md`, `_part40_cont.md`, `_part41.md`, `_part41_cont.md` (batch B38-narrative-regimes), `_part42.md`, `_part42_cont.md` (B39-procgen-and-cases), `_part43.md`, `_part43_cont.md` (B40-inst-scenarios). 129 item bodies and 133 position rows (parsed by `scratchpad/k10/parse.py`). Checks are `V12_STRUCTURE_part3.md` §10.1 as the brief numbers them (1 to 11). Appended as I go; sections below are filled in order.

## 0. Parse facts (script `parse.py`, `a1.py`)

- Position rows: B38 65, B39 38, B40 30 (= `workplan_v12_part2.md` §1.3's counts). No handle appears in two rows; no item body without a row. Rows with no body: B39.34, B39.36, B40.09, B40.28, all READING (allowed, §5.3). One boundary row per batch, all three exact (`part41_cont:291`, `part42_cont:300`, `part43_cont:182`).
- `GATE: Batch` lines equal part 2's after-list for each batch (B38 19, B39 23, B40 11; set-compared by script, full handles exact).
- Rows are not in numeric order where a patch inserted one (B39.37 after B39.14; B40.29 after B40.08): the table is landing order, so this is not a defect.

## 1. Findings, worst first

Severity: H = an executor would build the wrong thing or stop; M = a gate or dependency that misleads; L = form or wording. "Fixed" says whether this lane edited it. Item handles are in the three batches B38, B39, B40.

| # | batch.item | check | what is wrong | evidence | fixed | who decides |
|---|---|---|---|---|---|---|
| 1 | B38.55 | 4, 10 | DEPENDS ON says `FACTION_CREED` and `round_half_up` are "made earlier in v12" by B38.19/.20/.24/.25 (`31_WR_A` commits 1 to 4). No first-half item defines either; neither word appears in `31_WR_A`, `30_WR_G` or any other proposal; only `31_WR_B` (this item's source) uses them. `sway_odds` as copied calls `round_half_up` and the resolver step reads `FACTION_CREED` rows, so an executor meets two undefined symbols. `grep -rn` of engine/ and modules/ finds neither either. | `workplan_v12_part41.md:5` ("Absent at this read and made earlier in v12 …") and `:190`; `grep -n "FACTION_CREED\|round_half_up" workplan_v12_part40*.md` → no hit; `grep -rln FACTION_CREED proposals/ unified/ master/` → only part41 and `31_WR_B` | N | the A41 lane / orchestrator: either B38.55 defines both (a rounding helper and the faction-creed carrier) or B38.24/B38.25 do; an ownership choice, not mechanical |
| 2 | B38.53 | 4 | Marks `held_edge_declines` MISSING ("not in the tree"), with no owner, on a BUILD item. The tree has it: `rosters.yaml:2725` and `data/verbs.py:1855` (`HELD_EDGE_DECLINES`). A false absence claim, and a MISSING without an owner on a non-BLOCKED item. | `grep -n held_edge_declines engine/season/rosters.yaml` → `:2725`; `data/verbs.py:1855` | Y: rewrote the DEPENDS ON clause to EXISTS-IN-TREE with both citations; the source's STOPS IF kept as fallback | none |
| 3 | B39.23 | 3, 5, 6 | GATE arm `pytest tests/valoria -q -m combat → pass after the combat goldens' re-pin (B39.99)` reads a later item's effect (cannot pass at B39.23). The item pins combat goldens and golden modes but had no `EXPECTED RED UNTIL`. WHERE for the new test is "NEW test in `tests/valoria/` beside the combat module's exchange tests": no file path. | `workplan_v12_part42_cont.md:77`; no `EXPECTED RED` in part42_cont | Y (partly): added an `EXPECTED RED UNTIL B39.99` line and moved the `-m combat` arm's reading to B39.99 in words. N for the test path (names no file) | orchestrator / A42: pick the test file path (THIN) |
| 4 | B39 head, B40 head | 6 | E-1: realm pins in `_realm_goldens.py` move at 9 (B39) and 12 (B40) items and are re-pinned at `.99`; B38's head says the file reads red until `.99`, B39's said "none named by a source" and B40 had no line. | `workplan_v12_part42.md:54`; B40 head had no `EXPECTED RED UNTIL` | Y: B39 line extended and a B40 line added (`part42:54`, `part43:30`), naming the mover items the blocks' own RE-PIN lines already list | none |
| 5 | B40 | 1 | `SERIAL EDGES` and `FILE CENSUS` sit after the boundary row (`part43_cont.md:184-187`); §5.2 puts SERIAL EDGES before PARALLEL and the boundary row last. A reader or script that cuts the block at the STOP row loses both. | `part43_cont.md:182` STOP, `:184` SERIAL EDGES, `:187` FILE CENSUS | N | orchestrator: move the two paragraphs into `part43.md` between `C(…)` and `PARALLEL` (not done: `part43.md` is 115 KB, near the 120 KB cap, and the move crosses a file) |
| 6 | B38 | 1 | B38.51 (riot design) and B38.52 (goal-row `axis:` content) are said to land "at the batch's open, before B38.01" and "the head's position table lists them first" (`part41.md:9`, B38.51 INSTRUCTION). Both position tables list them after B38.25. Position-table order is landing order, so the table and the text disagree about when two items land. | rows in table order: B38.01..B38.25, B38.51, B38.52, B38.53 …; `part41.md:9`, `:109` | N | orchestrator / H1: move the two rows (and bodies) first, or strike the "before B38.01" sentences. B38.84 depends on B38.51 either way, so only the order text is wrong |
| 7 | B38.89 | 3 | The gate's test "reports the finding by name and passes" in the failure case; a test that cannot fail cannot observe the failure it excludes (CLAUDE.md §0.1 pt 2). Copied from `IS-B3-SE-02`. The `checked >= 3` guard is there. | `part41_cont.md:254-257` | N | orchestrator: accept as a reading gate, or require a fail arm |
| 8 | B40.21 | 3 | Gate 6's pass condition is "both arms of the bearer line non-empty in one seed, or the report says plainly the chooser never sent a bearer": a disjunction the report can always satisfy. The 2 x 2 of step 3 is printed, not asserted. | `part43_cont.md:9-21`, GATE | N | orchestrator: it is the source's own wording ("a finding about candidates, not a pass"); keep or add an asserted reading |
| 9 | B39.30 | 5 | GATE arm "on the valley fixture with one works whose plan is a `hearth` (B39.31 adds the row; read at B39.31's gate if it lands after)": the arm needs a later item's row, as the source of B39.31 lands next. Should sit in B39.31's GATE (§5.8). | `part42_cont.md:186-197` GATE | N | orchestrator |
| 10 | B38.78 | 10 | THIN: WHERE and TESTS name no file ("the file and function B32's items named", "the test file B32's item created"), marked `[ASSUMPTION … this lane did not open B32's part]`. An executor cannot start from the item. | `part41_cont.md` B38.78 | N | A41 / B32's owner: name the B32 item handle and file |
| 11 | B39.20, B39.22 | 10 | THIN WHERE: "the test file `14_VERBS_MATERIAL_A_mending.md` names", "… `14_VERBS_PHYSICAL_A_custody_and_force.md` names for `context_terms`": the file is read off a proposal, not named. | `part42.md` B39.20, B39.22 WHERE | N | A42 |
| 12 | B40.05 | 3 | GATE has no command line (starts "2." of the source, quoting a scripted callback and "Seeds 0 to 4"). The harness call (`institution INST-BYZ-CHANCERY 2 s`) is implied by B40.04's. | `part43.md` B40.05 GATE | N | A43 |
| 13 | B40.23 | 3 | GATE reads "a `wardship` over six seasons with the sender's stores at zero from season three"; no A-114 note on the item (the block's (U14) says a hand-built fold over constructed ticks is not a run). Same wording in B40.06 for a six-season span is "reported against". | `part43_cont.md` B40.23 GATE; `part43.md:73` (U14) | N | none: covered by (U14), listed so a reader sees it |
| 14 | B40 head | 1 | UNDECIDED (U2) said "Taken: no `GATE: Batch B21d` line" after H2 added that line (line 28). Stale. | `part43.md:58` against `:28` | Y: appended a Patched note | none |
| 15 | B38.54, .69, .72, .86, .87; B39.16, .18, .33, .35; B40.13 | 1, 2 | Headings of the POINTER, READING, HELD and BLOCKED items carry no `· HASH …` part (§5.3 heading form). The position-table row has `—`. | `grep '^### B3[89]\.\|^### B40\.'` | N | orchestrator: cosmetic; a `HASH —` suffix would do |
| 16 | B38.20, B38.25 | 8 | CONTENT items (46 cast rows of authored opinion values; faction creeds) name `haiku`/`sonnet` only, no `opus` reader, though they are authored values for Jordan's correction. B38.20 is a byte-for-byte transcription (checked, see §4), so its tier is right; B38.25 authors creeds. | COST and TIER of both | N | orchestrator |
| 17 | several | 8 | Cost class outside §5.3's list: "calibration reading and an edit" (B38.13), "edit and data" (B38.76), "data with a small build" (B38.85), "edit with one reading" (B38.88), "the close" (B38.99), "content and small build" (B39.37, B40.29), "edit and the close's readings" (B39.99). Tiers are all present. | COST and TIER lines | N | none |
| 18 | B38.51 | 3 | DESIGN-FIRST gate includes `grep -c '^## Status: PROPOSED'`: a Status-line read, allowed only because the item is a design file; the "stated (1) to (6)" half is read by a critic. | GATE of B38.51 | N | none |

No defect found for: banned size words (company/battalion/regiment/troops), "capability" in prose, attribute/skill words, lap against round (every copied `round` for the season's pass has a `NAMES:` line, e.g. `part41_cont.md:80`), riposte (`finalblow_riposte`, `part41.md:9`).

## 2. Counts per check

| check | B38 (65 positions) | B39 (38) | B40 (30) |
|---|---|---|---|
| 1 forms: head lines, one row per item, one STOP row, `.99`, GATE lines = part 2's after-list, INVOCATION | all hold; one table-order text clash (finding 6) | holds | holds except SERIAL EDGES/FILE CENSUS after STOP (5) |
| 2 fields (build-like items: B38 60, B39 32, B40 27) | see §3 | see §3 | see §3 |
| 3 gates: named test files (32 absent from the tree, each created by a named item: 26 in these batches, 6 in earlier ones: B10, B11, B12a, B21, B32), harness modules (access, valley, institution, scenarios, worldgen: each created earlier or by the item), tools (all exist), flags (`--overlaps`, `--regimes`, `--stories`, `--cascade`, `--strands-life` each created by a named item); none past two seasons; none a Status line or count off a document | 2 weak (7, 18) | 1 weak (9), 1 THIN gate ref | 3 (8, 12, 13) |
| 4 dependencies: EXISTS-IN-TREE opened (329 mentions scripted, 179 symbol-greps hit, the rest dirs/data tokens/ASSUMPTION text read by hand) | 2 wrong (1, 2) | 0 | 0 |
| 5 back edges: none in position tables; `V12 <handle>` refs all land earlier (script `a6.py`, 546 refs); every batch named in DEPENDS ON is in the transitive closure of the after-list | B38.51 names B38.82 as "built after it" (forward note, kept) | 1 (9) | 0 |
| 6 hash: movers 13 / 9 / 12 as part 2 says; all point at the `.99` re-pin; EQUAL items scanned for field adds to hashed carriers (none found) | EXPECTED RED covered in head | fixed (4) | fixed (4) |
| 7 words | clean | clean | clean |
| 8 cost and tier | 3 (16, 17) | 1 (17) | 1 (17) |
| 9 copy fidelity | §4 | §4 | §4 |
| 10 THIN items (cannot execute from the item alone) | B38.55 (undefined symbols), B38.78 | B39.20, .22, .23 | B40.05 |
| 11 Layer 1 | no item makes a `.md` the head of a fact; design files go to `proposals/`; determinism clauses present | same | same |

## 3. Field grades (build-like items = BUILD, CONTENT, DESIGN-FIRST; POINTER, READING, HELD, BLOCKED are checked separately)

Grades PRESENT / THIN / ABSENT. A field is THIN when it names no file or command an executor can use (not when it is short because the source says "none new"; those are PRESENT).

| field | B38 (60 items) | B39 (32) | B40 (27) |
|---|---|---|---|
| SOURCE, ADVANCES, INSTRUCTION, FALSIFIER and CONTROL, HASH MOVERS, DEPENDS ON, GLOSSARY, COST and TIER, LANDS IT | 60 / 0 / 0 each | 32 / 0 / 0 each | 27 / 0 / 0 each |
| WHERE | 59 / 1 / 0 (B38.78) | 29 / 3 / 0 (B39.20, .22, .23) | 27 / 0 / 0 |
| TESTS | 59 / 1 / 0 (B38.78) | 32 / 0 / 0 | 27 / 0 / 0 |
| GATE | 60 / 0 / 0 | 32 / 0 / 0 | 26 / 1 / 0 (B40.05) |

Non-build positions: B38 POINTER 4 (B38.54, .69, .86, .87: 3 to 8 lines, target files, gate: PRESENT) and READING 1 (B38.72, text in `## Readings` R-1, byte-for-byte against `IS_B3_FA_SE_WR_GO.md:117-126`: matched); B39 POINTER 2 (B39.16, .33), HELD 2 (B39.18, .35: trigger stated), READING 2 (B39.34, .36: texts present); B40 BLOCKED 1 (B40.13: owner named in the heading and in the body: `data/goals.py`'s owner, CHAR), READING 2 (B40.09, .28: R1, R2 present).

A first automated pass mis-graded 33 INSTRUCTION fields ABSENT because labels read `INSTRUCTION (…)` or `INSTRUCTION, in order …`; those were re-parsed and are PRESENT. The counts above are from the re-parse.

## 4. Sampled citations (check 9, copy fidelity) and what was opened

Method: for each sampled BUILD mover, the item's SOURCE was resolved to a file, then every test name, file path and command flag in the item's INSTRUCTION, WHERE, TESTS, GATE and FALSIFIER was searched in that file (script `a7.py`/`a8.py`); the edit text was also read against the source's "Exact edits" or "What it changes" for the starred rows.

| item | source opened | outcome |
|---|---|---|
| B38.03 * | `proposals/20_NARRATIVE_A_stands_for.md` "What it changes", gate 2 to 5, falsifier | matched; the three-season gate is written at two with the A-114 note |
| B38.05 * | `proposals/20_NARRATIVE_C_who_holds_what.md` "Exact edits" 2, gate 1 to 5 | matched (test names, `deposit_holder`, call site) |
| B38.13 | `28_CORE_scene_access_C_the_petition_that_waits.md` | matched at token level (flags are this batch's, created earlier in the batch gate) |
| B38.20 * | `proposals/31_WR_A_house_cores_….md` §4 | matched: all 46 table rows byte-identical to the source |
| B38.60 * | `proposals/09_WR_B_draws_not_thresholds.md` "Edit 4", gate (4) | matched; the two test names are E-3 assumptions from gate (4), marked |
| B38.63 | `30_WR_C_strands_open_grow_join_conclude.md` | matched at token level |
| B38.88 | `U5d_SE_cohort_heavy_moves_and_caste.md` | matched at token level |
| B38.72 (READING) | `master/instructions/IS_B3_FA_SE_WR_GO.md:117-126` | matched byte for byte |
| B39.04 | `21_PROCEDURAL_B_cast_and_seats.md`, `21_PROCEDURAL_D_world_cards_and_churn.md` | matched (all 7 tokens found) |
| B39.19, B39.22, B39.23 | `U5d_STORY_owed_edits.md` §1, §4, §5 | matched (B39.23's WHERE for the new test is THIN, finding 3) |
| B39.28 | `23_STORY_B_a_house_continues.md` | matched |
| B39.32 | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, `12_ARCS_case_on_the_realm.md` | matched; one test name not in the source, marked `[ASSUMPTION: test name]` |
| B40.12 | `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` | matched |
| B40.14 | `15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` | matched; `INST-VENICE-01-ONE.yaml` is the item's own marked assumption |
| B40.16 | same | matched; two test names marked assumptions |
| B40.22, B40.24, B40.25 | `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` | matched; 6 test names are marked E-3 assumptions the source does not carry |

Not "drifted" anywhere in the sample; no item was "unverifiable" except the ones whose sources named no test (those carry the `[ASSUMPTION]` mark). The sample is 17 of 55 mover items; four (B38.20, .03, .05, .60) were read in full against the source text, the rest at token level.

Dependencies opened beyond the script: `counterparty:` in `verb_table.yaml:150`; `resolve_anchor`, `seat_anchor` in `harness/populated.py:147,184`; `endings_reached` (`world_q.py:2619`), `flows_in` (`:5172`), `Forbidden` (`gaps.py:57`), `actor_of` (`state/attribution.py:73`), `heritage_regard` (`person_q.py:468`), `roster`, `roster_map` (`data/rosters.py:208,328`); the verbs `petition, migrate, work, tend, comply, evade / defy` in `verb_table.yaml` (B38.82's `[ASSUMPTION: each present]`: true); `seasons_for` (`corpus_run.py:460`); absent-symbol claims `link_fit`, `circle_of`, `OPINION_LINKS`, `REGIME_CORES`, `FACTION_CREED`, `round_half_up`, `pool_of`, `null_scenes` read in the tree (all absent as stated; creators exist for the first four and `pool_of`/`null_scenes` by handle, none for the last two: finding 1).

## 5. Edits this lane applied (all in my range, one round, nothing re-read after)

| file | edit |
|---|---|
| `workplan_v12_part41.md` | B38.53 DEPENDS ON: MISSING `held_edge_declines` rewritten as EXISTS-IN-TREE with `rosters.yaml:2725` and `data/verbs.py:1855` |
| `workplan_v12_part42.md` | B39 head `EXPECTED RED UNTIL B39.99` line extended with the realm-pin and combat-golden movers |
| `workplan_v12_part42_cont.md` | B39.23: added `EXPECTED RED UNTIL B39.99` item line (combat goldens), `-m combat` arm read at B39.99 |
| `workplan_v12_part43.md` | B40 head: added `EXPECTED RED UNTIL B40.99` line; UNDECIDED (U2) given a Patched note about H2's `GATE: Batch B21d-fa-arc` |

An earlier run's edits (commit f4eb906) were not in my four-part range except as listed by `git diff HEAD~1`; none of the lines above overlaps them. No file outside parts 40 to 43 and this file was touched. No commit, no pytest, nothing run longer than a grep or a script.

## 6. What I did not check

- Copy fidelity for the 38 mover items outside the sample, and the INSTRUCTION text of every mover item against its source in full (the sample is 17 of 55; four read in full).
- Whether the commands in GATE lines run and print the stated readings (no run was made; tree state after B03 to B37 is not the tree I read).
- Flags of existing harnesses against the tree one by one: I confirmed each missing flag has a named creating item; for flags already in the tree (e.g. `chronicle --chains --min-depth`, `decision_spread --persons`) I confirmed the module exists and, for chronicle, the flag.
- The glossary rows each item says it edits, and the `IDS:` block-slot arithmetic (K1's by-script check).
- Intake coverage (check 6 of §10.1) and the file census against §7.3: K1's.
- Whether the tier named per item is the right tier; I checked it is present, a real tier name, and that DESIGN-FIRST/CONTENT items name an `opus` reader (B38.20, B38.25 do not: finding 16).
- Item sizes against E-12's 6 KB hard budget (not measured).
