# F3 unapplied — what stage 3 could not apply exactly, and what it left (the fold map into workplan v12)

## Status: PROPOSED (a log; reference under CLAUDE.md §0.05, nothing reads it at runtime; stage 3, 2026-11-14; deleted with the plan's other work files when v12 is adopted)

Part A is the fold-map rows whose target differed from what the map quoted. Part B is text the map does not reach that now describes the old design (left, not guessed at). Part C is the places where the map's numbers or its brief were stale.

## A. Rows whose target differed

| id | map row | what differed | what was done |
|---|---|---|---|
| U1 | B24.09, "the sentence about a `None` arrangement goes" | B24.09 holds no such sentence. It is in B24.10 step 2 (`IS-B2-SC-03` step 3: *"… and `default` where the item's arrangement is `None` (every computed case today …)"*) | deleted there; B24.09's replaced step 1 carries no meta-sentence |
| U2 | B24.10, "REPLACE step 1's first sentence and step 3" with one text | one text for two targets | split at "This item adds to the builder:": the first sentence (`proceeding_input` and the provider path exist) replaces step 1's first sentence; the rest replaces step 3 (the old resolve-path text). Step 1's second sentence and step 4 are kept (B below) |
| U3 | B24.06, "REPLACE steps 1 and 2" | the item's step 3 (board effects, the ballot) is not in the row | steps 1 and 2 replaced by one step; step 3 renumbered 2 and its `ProceedingOutcome.ballots` → `verdicts` (HEAR_B's `ballots` is `verdicts`, the map's own B24.05 row) |
| U4 | B28.34 / B28.35 (the brief said "superseded") | the map EDITS both and supersedes neither | edited as the map says; no POINTER, no deletion |
| U5 | F.2, id row `H-856..H-909 (49+5)`, sentence `H-855 → H-909` | the table's last allocated H is H-860 (B01a, allocated 2026-11-14 after the row the map read); the map flagged this assumption | allocated H-861..H-914 (49+5); the next free H is H-915; the sentence reads SC 57, H-915 (and IN 402 → 405, B01a's, which the head's sentence had not taken) |
| U6 | F.2, chains: "insert `B24p` immediately before `B24` (or before `BA1` where the chain has it and no `B24`)" | where a chain holds both `BA1` and `B24` (`rosters.yaml`, `verb_table.yaml`, `data/fixtures.py`), "before B24" puts B24p after BA1, B11, B15 and B21; the batch's own SERIAL EDGES say `B07 → B24p → BA1 → B24` and "B24p merges first" | the census chains follow the landing order the appendix's `census.py` gives with B24p listed before BA1 (first in S12): `B24p` before `BA1` / `B11` / `B15` / `B21` where the chain has one, else before `B24`, else before the next batch |
| U7 | F.2, the batch table's `W12` | B24p's wave by its edges (after B07, W9) is W10; W12 was a placement (after B10), which is not an edge | wave W10, step S12 (held by a schedule floor after B10, not an edge); the heading and part 2 say so |
| U8 | F.2, the close table row "its UNDECIDED count 4" | the gate index (§2) has no column for it | the row is added with the columns it has (the line of the STOP row, 9 gates) |
| U9 | F.3, B25.14 `[UNVERIFIED: B25.14's body was not opened]` | the body was opened at this stage | the pointer is step 10 of B25.14; the mark is struck there |
| U10 | F.3, B27.05 to B27.08 | the map names B27.05 only | applied as B27.05 step 4 |

## B. Text the map does not reach, left as it is (for the item's own session or the orchestrator)

1. B24.10 step 1's second sentence still says each speaker's `pools` are `((skill id, dice), …)` and the `effort` is the act's own; B24p.13 builds `Speaker.ranks`, `Speaker.effort` (`+1` for the actor, `type.exchanges[1]` for the one addressed).
2. B24.30 steps 2 to 4 and B28.13 step (2) still say `ProceedingInput.closing` (`None` for a mutual row) and `proceed` "on `closing is None`, skip the closing draw"; `ProceedingInput` (B24p.02) has no `closing`: the map's own step-1 note says nobody is balloted under `mutual` (B24p.12). B24.30's TESTS and `Offer`/`accepted` fields stand.
3. B24.35's GATE (c) still reads the edge "reported by the `capability` advantage source (in `fed_by` and SC-P1's `levels`)": with no uses rows written it is the `fit` source (B24p.08).
4. B28.35 step 4 reads the self-plea opponent "on the row's `opposed_attribute`"; B24p.19 deletes `opposed_attribute:` from `speak` (RD §D.3). The map says "the rule is unchanged".
5. B24.33 step 3 still says `resolver: d10_sigma`; B24p.12 set `resolver: d_sigma` (B05.04's name) and left the rest of the row to B24.33 (its own `[ASSUMPTION]`).
6. B24.05's TESTS name `test_the_hearing_records_are_frozen_and_world_free` and B24p.02's `test_the_proceeding_records_are_frozen_and_world_free` test the same records; both kept.
7. B24.03's TESTS name `test_the_hearing_rosters_load_with_the_rows_named` and B24p.01's `test_the_proceeding_rosters_load_with_the_rows_named` overlap on `proceeding_moves`; both kept.
8. Item headings keep the word *hearing* where the item is the hearing's (B24.03, B24.05, B24.07, B24.13 and others): the map's rename list does not include prose headings.
9. Part 2 §5.1's counts (879 files named, 269 in two or more batches) and the 25 §2 rows whose `part:line` cells were already stale before this stage (B09, B10, B12a, B15, B17, B20, B21, B33 and others) are not recomputed: the orchestrator's GATE-line rewrite moves every line again. The six §2 rows this stage touched (B24, B24a, B27, B28, B98, B99) and the new B24p row are exact as of this stage.
10. Part 2 §1.3's B01a row still reads 6 positions and 6.9 h; the tree has 7 and 7.3 h (B01a.06): the graph reads 7.

## C. For the orchestrator (decisions only it can make)

1. B24p's wave and step: W10 and S12 as the tables now read, S12 by a schedule floor after B10. To drop the floor, B24p could open at S11 beside B10 (the other reading of the block's UNDECIDED (1)); no critical-path hour moves either way.
2. The pipeline brief called B28.34/.35 "superseded"; they are edited, not superseded (U4).
3. `references/id_reservations.yaml` is not touched: at B24p's start SC `next_free` 54 → 57 (ED-SC-0054..0056); the hole-register ids H-861..H-914 live only in the plan's id table.
4. `V12_FOR_JORDAN.md` J-SC-1 and J-SC-2 are the two questions that overwrite a ratified letter (ED-IN-0350, ED-1062): the plan assumes the redesign's option A in both.
