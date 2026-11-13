# R2a_APPLIED — repair lane R2a (Opus): the open findings of CHK_K1 and CHK_K2

## Status: WORK RECORD (one round; edits to parts 3 to 11 of `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite when v12 is adopted)

Scope: `checks/CHK_K1.md` (F1..F13) and `checks/CHK_K2.md` (#1..#16), after `checks/R1_APPLIED.md`. Each row: finding → what was done (edit / already fixed / for Jordan) → file:handle. Ladder steps are CLAUDE.md §0's (1 superseded, 2 irrelevant, 3 design document, 4 precedent, 5 architecture). Appended as applied.

## Already resolved before this lane (re-checked against the current text)

| finding | resolved by | re-check |
|---|---|---|
| K1 F13 | K1's own edit | B02.13 carries the `EXPECTED RED UNTIL` line |
| K1 F2 | R1 repair 6 | B03a, B13 blocks carry `GATE: Batch B03g-go-early-landings` |
| K1 F3 | R1 repair 2 (B02.39) | — |
| K1 F4 | R1 repair 5 (B00.99, B01.99, B02.99; B00's E-6 gate line) | — |
| K2 #1, #2, #3 | K2's own edits | — |
| K2 #4 | R1 repair 4 (batch-head `EXPECTED RED UNTIL` for B04, B06, B14, B07, B17, B09) | — |
| K2 #5 | R1 repair 5 (B04.99) | — |

## Resolved by this lane

| finding | ladder | what was done | file:handle |
|---|---|---|---|
| K1 F12 | 3 (E-1) | one sentence on B03's second-half `EXPECTED RED UNTIL` line: every item GATE "→ pass" on a covering suite excepts the two pin tests and the batch line's files | `workplan_v12_part5.md` B03 head lines |
| K1 F1 | 3 (the source's "else in … B17"; `STAGES.md` parallel rule 6) | new **B17.14** (HELD: lands only if no `Item: B02.07` commit is on its base), body copied from B02.07; B17 table row, `.99` gates-on, EST 14 → 15 positions (8.5 h); B02.07 LANDS IT names B17.14; part 2 §1.3 B17 row (15, 8.5 h); part 2_cont file-census row gains B17.14. **Not recomputed:** part 2 §1.2 totals (+1 position, +0.4 h, B17 off the critical path, slack 4) | `workplan_v12_part11.md` B17.14; `_part3.md` B02.07; `_part2.md` §1.3; `_part2_cont.md` census |
