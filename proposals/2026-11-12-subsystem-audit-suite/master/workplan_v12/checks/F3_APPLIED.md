# F3 applied — stage 3 of the social-contest pipeline (the fold map, `2026-11-14-social-contest-redesign_part5.md` §F, into workplan v12)

## Status: PROPOSED (a log; reference under CLAUDE.md §0.05, nothing reads it at runtime; written by the stage 3 lane, 2026-11-14, branch `exec/v12-b00-b03`; deleted with the plan's other work files when v12 is adopted)

Paths: `wp` = `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/workplan_v12_`. One row per fold-map row: the target handle, what was done, the file. `UNAPPLIED` rows are also in `F3_UNAPPLIED.md`. Scripts are in the session scratchpad (`stage3/`): `rename.py`, `mk_b24p.py`, the appendix copies.

## F.1 The new batch

| row | done | file |
|---|---|---|
| the batch's part | ADD two files (the orchestrator's names, not the map's `part18_cont2.md`): `wp part22_b24p.md` (head, block, B24p.01 to B24p.12; 59 KB) and `wp part22_b24p_cont.md` (B24p.13 to B24p.99, Readings, boundary row; 43 KB). No `_cont2` was needed (each under 120 KB). Items copied from part 3 (line 17 to the end) and part 4 (`### B24p.13` to the STOP row) by `mk_b24p.py`, byte for byte. Added by this stage, plan-form fields the proposal's block lacked: (1) the part head (title, Status, Written against, What this part holds, Words, Paths); (2) a `source` column in the position table (the item headings' own source segment, so the table is the six-column form `pos / item / source / state / hash / gates on` every other batch and `parse_parts.py` read); (3) the `FILE CENSUS` line (from the items' WHERE lines, B01a's form); (4) the `Block:` sentence on `IDS:` (ids on paper, below). Nothing in an item body was edited. | `wp part22_b24p.md`, `wp part22_b24p_cont.md` |
| why S12, why before B24, the calibration batches | prose rows of the map: no plan text to write (the reasons are in the batch block's UNDECIDED (1) to (4) and PARALLEL line, already in Fable's block) | — |

## Scripted rename `hearing` → `proceeding` (F.3, after B24's gate line)

`rename.py` (dry run first, then `--apply`; over every `workplan_v12*.md` except `part3.md`, `part3_cont.md` (the do-not-touch files; they held none) and the new b24p parts). Dry-run and applied counts equal; a second dry run reads 0.

| old | new | count |
|---|---|---|
| `social_contest.hearing` | `social_contest.proceeding` | 23 |
| `modules/social_contest/hearing.py` | `modules/social_contest/proceeding.py` | 15 |
| any remaining `hearing.py` | `proceeding.py` | 5 |
| `` `hear` `` / `hear(` / `::hear` | `` `proceed` `` / `proceed(` / `::proceed` | 14 / 1 / 2 |
| `HearingInput` / `HearingTurnView` / `HearingOutcome` | `ProceedingInput` / `ExchangeView` / `ProceedingOutcome` | 17 / 5 / 10 |
| `hearing_input` | `proceeding_input` | 24 |
| `hearing_moves` / `hearing_faults` | `proceeding_moves` / `proceeding_faults` | 19 / 5 |
| `` `Seat(id, pool, modifier, lean)` `` / `` `Seat.lean` `` / `` `Seat` `` (`part22.md`, `part22_cont.md` only) | `` `Decider` `` forms | 1 / 2 / 8 |
| **total** | | **151 in 13 files** (`part7`, `part13`, `part22`, `part22_cont`, `part25_cont`, `part28_cont`, `part2_cont`, `part2_cont2`, `part2_cont3`, `part35`, `part35_cont`, `part37_cont`, `part41_cont`) |

Not renamed, as the map says: `headless --world hearing`, `build_hearing`, `test_sc_hearing_*.py`, *sitting*, `closing_odds`, `sitting_exchanges`. The `` `Seat` `` of `part7`, `part14`, `part37` (`04` §B.7's `Seat` tuple, a different thing) is untouched by construction. The rename ran BEFORE the item edits below, so the map's new text (which uses the new names) is inserted after it and never renamed.

## F.3 rows

### B01a, B05, BA1

| handle | action | applied |
|---|---|---|
| B01a.06 | NONE | none: already true in the tree (landed `1257a4a`); `part3.md` not touched |
| B05 block `UNDECIDED` (U-11) | EDIT, append | applied: the sentence appended at the end of U-11 in `part8.md` (the UNDECIDED line of the B05 block) |
| B05.21 | EDIT, append to step 1's `standard` sentence | applied in `part8_cont.md`: the ⚠ sentence inserted straight after the `standard (...)` clause, before `stakes` |
| B05.22 | EDIT, append to INSTRUCTION | applied in `part8_cont.md`: a last paragraph of INSTRUCTION (after the realm-read note); the item stays PROVISIONAL as the map says |
| B05.23 | EDIT, append to INSTRUCTION | applied in `part8_cont.md`: a last paragraph after step 7; stays PROVISIONAL as the map says |
| B05.24 | EDIT the rule sentence's last clause | applied in `part8.md` (the quoted sentence now ends with RD §D.4's clause) |
| B05.24 | EDIT step (2) | applied in `part8.md`: the `; of the 31, six …` clause inside the parenthesis |
| B05.25 | EDIT, append to step 1 | applied in `part8.md` (appended to step 1, before step 2) |
| B05.25 | EDIT step 3's kind rule | applied in `part8.md`: `or, from B24p.16, a `proceeds:` cell` after `(c) the exemption (…)` |
| BA1.13 | EDIT, append to INSTRUCTION; EDIT DEPENDS ON | applied in `part18_cont.md` (both) |

### B24 (the hearing)

| handle | action | applied |
|---|---|---|
| B24 block | `GATE: Batch B24p-sc-proceeding` after `GATE: Batch B11-fi-readers` | applied in `part22.md`. Also by coherence, in the block: `IDS:` (H 10 → H 7: B24.07 slots 1–4, slot 5 returned, B24.29's slots 9–10 returned; the map's own B24.07 line says `H 9` and its F.5 says B24 returns three slots, so H 7 is the sum), `DIALS AT CONTROL` (`argument_step`, `insight_gain` struck), `UNDECIDED (6)` marked CLOSED, the BATCH GATE's test list (check 8 and check 11), `SERIAL EDGES` (`B24p →` inserted before `B24` in eight file chains). The B24 block's id range (H-661..H-675) is not shrunk (every later block would move): the three slots are named at the expunge |
| B24.03 | REPLACE step 1's roster sentence | applied in `part22.md`; the two parentheticals of the old sentence (the four rung ids, the four fault ids and HEAR_B's "Faults") are kept inside the map's text so "as written" still has its referent. Coherence: step 3 and WHERE named `HEARING_MOVES`/`HEARING_FAULTS` (not in the rename list); now `PROCEEDING_FAULTS` and `PROCEEDING_MOVES`' effect set |
| B24.03 | EDIT step 2 | applied (appended to step 2) |
| B24.04 | EDIT | applied: the map-form text, the loader's map refusals; DEPENDS ON + B24p.01 |
| B24.05 | REPLACE step 1 | applied in `part22.md`; WHERE and DEPENDS ON re-pointed (B24p.02). The old closing clause "`Decider` is a record of this module, not 04 §B.7's Seat" is kept |
| B24.06 | REPLACE steps 1 and 2 | applied as one step 1; old step 3 renumbered 2 and its `ballots` → `verdicts`; the heading and table row retitled; |
| B24.06 | EDIT TESTS | applied |
| B24.06 | DELETE step 4 | applied; the WHERE, GATE (`export_composition --check`) and the B03 DEPENDS ON/gates-on cell of step 4 removed with it |
| B24.07 | EDIT | applied: `argument_step` struck from the settings, sweeps, WHERE, IDS (four rows, slots 1 to 4); the sentence naming `ProceedingInput.answer_ob` now reads `ProceedingInput.dials`; the block's `DIALS AT CONTROL` and `IDS` lines likewise (H 7, see the block row) |
| B24.08 | EDIT, append | applied (instruction, WHERE, control, DEPENDS ON) |
| B24.09 | REPLACE steps 1 and 2 | applied as one step 1 (the `bears:` map and its assumption kept inside it). "The sentence about a `None` arrangement goes": that sentence is in B24.10 step 2, not B24.09: removed there (`F3_UNAPPLIED.md`, row U1) |
| B24.10 | REPLACE step 1's first sentence and step 3 | applied: the text is split at "This item adds to the builder:" (the first sentence into step 1, the rest as step 3); `F3_UNAPPLIED.md` row U2 |
| B24.11 | EDIT step 3 | applied |
| B24.12 | EDIT, append to (1) | applied |
| B24.13 | EDIT step 1 | applied (appended to step 1) |
| B24.14 | EDIT | applied |
| B24.29 | REPLACE the draw's probability | applied in `part22_cont.md`: INSTRUCTION rewritten around the map's text; the `tables.capability_uses` row, the two fixtures, their two H rows (WHERE, IDS, the sweep sentence) dropped as the map says they are not created; the TESTS and control re-read at Attunement 2 and 5 |
| B24.30 | EDIT step 1 | applied (appended to step 1) |
| B24.32 | EDIT check 8 | applied (STOPS IF and "UNDECIDED (6) holds the other reading" removed) |
| B24.32 | ADD check 11 | applied (WHERE, TESTS, GATE) |
| B24.33 | EDIT step 3 | applied (`persuasion_track` deletion removed from the step) |
| B24.35 | REPLACE step 2 | applied; the heading retitled; WHERE (`tables.capability_uses` four rows) struck; `Speaker.backed` added to WHERE |
| B24.37 | EDIT | applied |
| B24.41 | EDIT INSTRUCTION | applied |
| every B24 row with an edit | position-table `gates on` | `; Batch B24p-sc-proceeding` appended to 14 rows (B24.03 to .06, .09 to .11, .13, .14, .29, .30, .32, .33, .35) |

### B24a, B25, B27, B28, B32, B33

| handle | action | applied |
|---|---|---|
| B24a.01 | ADD a step | applied in `part28_cont.md` (a closing sentence of INSTRUCTION; the item's INSTRUCTION is one paragraph, not numbered) |
| B24a.04 | EDIT | applied (a closing "Under B24p:" sentence; WHERE re-pointed to read `authorities.by_faction`; DEPENDS ON + B24p.01, .03) |
| B25.14 | EDIT, a pointer for the FI lane | applied in `part30_cont.md` as step 10. The body WAS opened at this stage (step 6's `approach` source is the one meant), so the proposal's `[UNVERIFIED]` mark is struck |
| B27.05 to B27.08 | EDIT B27.05 | applied in `part31.md` as step 4; DEPENDS ON + B24p.20 |
| B27.16 | EDIT step (2) | applied (the readers cited in step (2)'s parenthetical; DEPENDS ON + B24p.03, .11, .13, .15) |
| B28.10 | EDIT | applied in `part35.md` (step 1; DEPENDS ON + B24p.05) |
| B28.13 | EDIT, append | applied in `part35.md` (in step (2): `covenant` takes `proceeds:`) |
| B28.34 | EDIT INSTRUCTION (1) | applied in `part35_cont.md`. The map EDITS the item; it does not supersede it (the pipeline brief said "superseded"): no POINTER and no deletion |
| B28.35 | EDIT steps 1, 2, 4 | applied in `part35_cont.md`; WHERE and DEPENDS ON re-pointed (`proceeding_input`, B24p.13). Residual: step 4 still reads `opposed_attribute` for `speak`, which B24p.19 deletes (see `F3_UNAPPLIED.md`) |
| B32.15 | EDIT (five keys; `acclamation` values) | applied in `part34.md` |
| B33.18, B33.23 and any later item that seeds an arrangement row | EDIT | applied as one added line before WHERE in B33.18 (`audit`, `quo_warranto`), B33.23 (`consecration`), and by the "any later item" clause in B32.20 (`conclave`), B33.38 (`debt_suit`) and B33.41 (the two rows). Only `acclamation` has stated values; for the others the line says the values are written at the item's open from RD §C.3's nearest row and listed in the PR body (D-19) |

### B98 and the gate lines

| handle | action | applied |
|---|---|---|
| B98 block | `GATE: Batch B24p-sc-proceeding` | applied in `part44.md`, before `GATE: Batch B24-sc-hearing`; also in B99's block (`part44_cont3.md`: B99 is after every batch) and, by the batch block's own SERIAL EDGES sentence ("B24, B24a, B27, B28 and BA1.13 gate on this batch"), in B24a (`part28_cont.md`), B27 (`part31.md`) and B28 (`part35.md`). BA1 gets no GATE line: BA1 and B24p share step S12 and the pair is a merge order, as the map's S12 row says |
| B98, three positions at the next free handles | ADD | applied: B98.87 (the forty-five settings re-read, READING), B98.88 (`reading_kept`, a flip), B98.89 (`presumption_level` and `strike_level`, BLOCKED (design: no target reading)); table rows in `part44.md`, bodies in `part44_cont2.md` before `## Readings`; R1 and R2 and the `.99` DEPENDS ON and table row re-pointed; part 2 §4 rows 106 to 108 |

### F.2 The head parts, part 2, the appendix

| file : anchor | applied |
|---|---|
| `workplan_v12.md` id-block table | row added after B01a's: `B24p-sc-proceeding | SC | ED-SC-0054..0056 (1+2) | H-861..H-914 (49+5)`; the map's H-856..H-909 moved by B01a's block (`F3_UNAPPLIED.md` U5) |
| `workplan_v12.md` "`next_free` after B00" sentence | SC 54 → 57, IN 402 → 405, H-855 → H-915 |
| `workplan_v12.md` parts table | row `B24p-sc-proceeding | workplan_v12_part22_b24p.md, _part22_b24p_cont.md` after BA1's (before B12a's), the orchestrator's file names; the Parts line (line 7) and a "With B24p" figures paragraph added; the head's step table S12 row gains B24p |
| `workplan_v12_part2.md` §1.2 | step table S12 row; a "Re-run 2026-11-14 for B24p" paragraph (before → after) |
| `workplan_v12_part2.md` §1.3 batch table | B24p row added before B24's; the after-lists of B24, B24a, B27, B28 gain B24p; B98's row 87 → 90 positions, behaviour 38 → 39, 105 → 108 rows, 39.3 → 40.5 h |
| `workplan_v12_part2.md` §2 gate index | the B24p row; B24, B24a, B27, B28, B98, B99 re-counted (10, 4, 8, 14, 61, 62 gate lines) and their STOP lines re-read |
| `workplan_v12_part2.md` §3 hash movers | row `S12 | B24p | 15, 19, 20, 23 | — | — | B24p.99 | 1 of 5 movers`; BA1, B11, B15, B21 renumbered 2 to 5 of 5; B98 gains `88` |
| `workplan_v12_part2.md` §4 settings | rows 106 (the forty-five settings, a reading), 107 (`reading_kept`), 108 (`presumption_level`, `strike_level`); the counts line 105 → 108 rows, 34 → 36 TARGETED, 64 → 65 BLOCKED |
| `workplan_v12_part2_cont.md` §5.2, §5.4 | three S12 pairs (`B24p → BA1`, `B24p → B11`, `B24p → B15`), 57 → 60 pairs; 21 census rows gain B24p in their chain and counts, seven rows added (`tests/test_sc_proceeding_data.py`, `harness/pairs.py` and `tests/test_pairs.py` (the map's new chain `harness/pairs.py: B01a → B24p`), `tests/test_obstacle_form.py`, `tests/test_sc_calibration_targets.py`, `tests/test_sc01_provider.py`, `tests/test_verb_governing_attributes.py`) |
| `workplan_v12_part2_cont2.md` §9 | the id row and the `next_free` sentence |
| `workplan_v12_part2_appendix.md` | `parse_parts.py` reads the `_b24p` file names; `graph.py` injects B24p, `SCHED_FLOOR`, `CALIB` gains B24p (checked: the re-extracted scripts equal the scratch copies but for one comment) |

## The graph (appendix scripts run in the scratchpad `stage3/run_old` on `git archive HEAD` and `stage3/run_new` on the edited tree)

| reading | before (tree at `1b42689`) | after |
|---|---|---|
| batches | 62 | 63 |
| edges (S+G+R) | 543 | 558 (+11 structural, +4 GATE lines) |
| acyclic | yes | yes (Kahn's sort reaches all 63) |
| waves | 26 (W0..W25) | 26; B24p at W10 (pre-B01a numbering) |
| steps | 26 | 26; B24p at S12 (floor), first to merge |
| tied chains by waves | 90 | 90 |
| critical path | 390.8 h | 392.0 h (same 25 batches; +1.2 h is B98's three positions) |
| serial | 751.6 h | 766.9 h (B24p 14.1 h; B98 +1.2 h) |
| makespan | 426.4 h | 427.6 h |
| with the five pairs as edges | 28 waves, 28 steps, 421.4 h | 28, 28, 422.6 h |
| positions | 1,464 | 1,491 |
| behaviour movers / mover batches | 477 / 49 | 482 / 50 |
| `gates.py` | every block's GATE lines equal its after-list | the same, B24p included; no GATE line names a later batch |

## V12_FOR_JORDAN, DECISIONS_ANSWERED, the checks

- `V12_FOR_JORDAN.md`: J-SC-1 (Reason or Presence as the dice) and J-SC-2 (does the wrong ground cost), in the file's section form, each with options, a recommendation (A) and what the plan assumes (A).
- `unified/DECISIONS_ANSWERED.md`: A-117 to A-126, one row per ruling R1 to R10 of the rulings file, Jordan's words as quoted there, each marked "ruled by Jordan 2026-11-14 in the session". The redesign's own decisions are not rows.
- `python tools/ci_naming_check.py`: "no new use of a deprecated name", exit 0. A whole-tree case-insensitive search for the deprecated name (the pattern built in the shell, never written to a file) finds no hit in any file this stage created or edited; the hits in `references/`, `registers/`, `engine/engine_params/names.json`, `skills/prose-writer/SKILL.md` and `.designs/` are the names index and its mirrors.
- No pytest, no `register --check`, no commit.
