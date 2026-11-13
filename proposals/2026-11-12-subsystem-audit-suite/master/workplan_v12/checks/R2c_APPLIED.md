# R2c_APPLIED — repair lane R2c (Opus): open findings of `CHK_K5.md` and `CHK_K6.md` (parts 21 to 28)

## Status: WORK RECORD (one round; a record of edits to `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite when v12 is adopted)

Appended finding by finding as each is settled (a restart resumes from the last row written). Ladder steps are CLAUDE.md §0's: 1 superseded, 2 irrelevant, 3 a design document, 4 precedent, 5 what the architecture needs.

## Per finding

| finding | outcome | file : handle | what was done |
|---|---|---|---|
| K5 F1 | re-checked: already fixed by R1 | part22 B24, part23 B16/B08, part24 B12b, part24_cont B29, part21 B21b heads | R1 repair 4's batch-head `EXPECTED RED UNTIL` lines cover every mover of the six batches (ladder 3: E-1 asks a listing, the head line is one) |
| K5 F2 | edit | part24_cont B12b.43 GATE; B29.02 TESTS, GATE | the pytest arm reads "pass except the pin test(s) the item moves, red until `.99`" |
| K5 F3 | re-checked: already fixed by R1 | part21 B21b.05 | the `STOPS IF` line R1 added is present |
| K5 F4 | re-checked: already fixed by R1 | part24_cont B12b.99, B19a.99, B29.99 | R1 repair 5(b) filled the eight cells each |
| K5 F5 | edit (ladder 3: part 2 §3's merge order and `V12_STRUCTURE_part3.md` §7.4) | part21 head RE-PIN, B21b.01 GATE, REQUIREMENT, part21_cont B21b.99; part22 head RE-PIN, part22_cont B24.99; part24 head RE-PIN, BATCH GATE, B12b controls (two items), part24_cont B12b.99; part24_cont B29 RE-PIN, PARALLEL | baselines now: B21b against B16's after-reading; B24 against B21b's; B12b against the S14 base (B24's after-reading; every "B12a's close" baseline in B12b's text); B29 against B21c's. Not edited (no CHK finding names them, same shape): the RE-PIN lines of B21c ("B21b's close"; B12b precedes it), B34 ("the step's base"; B29 precedes), B12c ("B12b's close"; S14's last is B34), B24a ("B24's close"; B21d precedes), B19 ("B19a's close"; B18 precedes) — for the orchestrator |
| K5 F7 | edit (ladder 3: E-14) | part21 B21b.10, B21b.12 DEPENDS ON; head DIALS; part2_cont2 §8 row 67 (outside my parts: required by this finding) | state stays BUILD; each item says the absent arm ships absent by E-14 and is held in part 2 §8 row 67; the head and row 67 no longer say "BLOCKED" for the item |
| K5 F8 | no edit (ladder 4: D-18's shape, B21b.24 → B21b.25, as every DESIGN-FIRST pair) | part21_cont B21b.25 | the item is executable once B21b.24's design is merged; its own `STOPS IF` and gate on B21b.24 hold it; K5 asks nothing |
| K5 F9 | edit | part22 B24.01 (plan-added line, step 2) | "returns" → "computes"; the item says `_mint_document` returns a `Change` (`engine/season/loop/effects_information.py:205-231`, opened) and how to get the id |
| K5 F10 | edit outside my parts (required by this finding) | part2_cont2 §6 test census | row `S/tests/test_sc_hearing_evidence.py` / B24.18 / S13 added |
| K5 F14 | no edit (note only, K5: no back edge) | — | — |
| K5 F15 | no edit (ladder 3: E-5 asks what the section does, its files and symbols, and the gate — content, which K5 found present; no field label is required) | part24/24_cont B12b.07, .17, .29-.32 | — |
| K5 F16 | no edit (ladder 3: D-17 / A-114 respected; the copy keeps the source's bytes and the "(eight in the source; A-114)" note beside it is the plan's reading) | part24_cont B12b.44 | — |
| K5 F17 | edit | part24_cont (B12b, the `07_SE_…` larder-walk copy) | a `[v12: …]` note after the quotation: "round" there is a pass of the larder walk; write "pass" in new text (A-101) |
| K5 F18 | no edit (ladder 3: `unified/U1_GLOSSARY.md` rows *unit* "men of one troop type" and *kit* "(troop type)" use the word; A-99 refuses size words and "a body of troops", none present) | part24_cont B19a.01, B12b.47 | — |
| K5 F19 | edit (ladder 3: E-15; part 2 §1.3's figures are the schedule's) | part21, part22, part23 (B16), part24 heads' EST lines | each EST line names part 2 §1.3's figure (13.7, 19.7, 7.7, 21.7 h) as the one the schedule uses |
| K6 F1 | re-checked: already fixed (K6's row edit; R1 repair 8 regenerated part 2 §1.3 and §3 for B19, 15 behaviour movers, `.60` listed) | part27 B19.60; part2 §1.3, §3 | — |
| K6 F6 | edit (CLAUDE.md §0.05: a Status line is not an execution artifact) | part25 B21c.06 GATE | the `grep -c "^## Status: PROPOSED"` arm deleted; a `git diff --stat` arm (only the design file and `hole_register.yaml`) stated in its place, the item's own CONTROL |
| K6 F7 | edit (THIN: the edit text copied from the source) | part25 B21c.01 INSTRUCTION step 1 | the nine ladders' 66 names copied from `faction_politics_v30.md` (archived; opened: Part 1 §1.1–§1.4, Part 2 §2.1–§2.5 ladder tables) as the `ladders:` YAML block, rank 0 first, `livery` per ladder; the count matches the entry's 66 (rank 0 names included); the sub-office ladders' faction carried as `[ASSUMPTION]` (no Riskbreaker/Inquisitor/Templar member in `rosters.yaml: factions`, read from `references/names_index.yaml` `token_class: faction`) |
| K6 F9 | re-checked: already fixed by K6 | part26_cont B19.17 | — |
| K6 F13 | edit for B21c and B34 (ladder 3: `V12_STRUCTURE_part2.md` §5.2's order puts SERIAL EDGES and PARALLEL after `C(...)` and before COST); no edit for B19 | part25 (B21c), part25_cont (B34) | the three lines of each block moved verbatim to before COST (multiset of non-blank lines unchanged, checked by `diff` of sorted lines). B19: its head (part26) already carries SERIAL EDGES and PARALLEL in §5.2's place; the second half's paragraphs (part27 :81-84, part26_cont :223-226) are labelled continuation notes for the head ("what the batch head carries from this half"), left in place |
| K6 copy note (B21c.03) | edit (E-3) | part25 B21c.03 TESTS | `[ASSUMPTION: test name; the item creates it]` added to `test_confer_of_an_elected_seat_refused` |
