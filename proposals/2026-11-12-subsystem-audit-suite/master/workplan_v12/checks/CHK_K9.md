# CHK_K9 — check lane K9 (Sonnet), workplan v12 parts 36 to 39

## Status: WORK ORDER output (a check lane's one-round report on `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

Read: `workplan_v12_part36.md`, `_part36_cont.md` (B35-wr-thread, 30 positions); `_part37.md` (B23-land, 19) and `_part37_cont.md` (B30-mb-nested, 11); `_part38.md`, `_part38_cont.md` (B33-inst-economy-hands, 49); `_part39.md` (B36-wr-story-instruments, 18) and `_part39_cont.md` (B31-mb-loadout-economy, 21). Against `V12_STRUCTURE.md` §5, `V12_STRUCTURE_part3.md` §10.1, `V12_STRUCTURE_part4.md` (errata win), `workplan_v12_part2.md` (batch table, §11 register). The task brief (the K9 brief) names "parts 36 to 39": that is what was read; `V12_STRUCTURE_part3.md` §10.1 gives K9 parts 32-35, K10 36-39 - a lane-name difference, no content difference. One round; no second pass on my own fixes.

(This file is written head first and appended: sections below are filled as the checks finish.)

## 0. Parse facts (scratch scripts `parse.py`, `c1.py`, `c2.py` in the lane scratchpad)

- Six batch blocks, 148 position rows, 148 item headings (positions == item headings in order for every batch; no handle twice; no item without a row).
- Each block: INVOCATION text exact; IN-FLIGHT ROW names the right lane file (WR/FA/MB/FA/WR/MB); exactly one boundary row, exact `| STOP. Batch <full handle> closes here |`; a `Bnn.99` position as the last row before the boundary.
- `GATE: Batch` lines equal part 2's after-list set for every batch (B35 10, B23 11, B30 10, B33 16, B36 9, B31 9), counting part 2's "+R" entries as edges added by H2 (B22 -> B30, B21d/B21s -> B33, B20/B22 -> B31).
- No `GATE: Batch` names a batch that closes at or after the batch's own step (steps from part 2: B35 S18 after B32 S17/B34 S14/B12c S15; B23 S18 after B22 S17; B30 S18 after B22 S17/B24 S13; B33 S19 after B21d S15, B21s S18, B28 S17; B36 S19 after B35 S18; B31 S19 after B22 S17).

