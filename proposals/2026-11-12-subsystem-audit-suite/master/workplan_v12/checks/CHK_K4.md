# Check lane K4: workplan v12 parts 16 to 20 (batches B11, B15, BA1, B12a)

## Status: WORK ORDER output of check lane K4 (Sonnet), one round; a terminal record about artifacts that exist, resolves nothing at runtime (CLAUDE.md §0.05); deleted when v12 is adopted

Read at: working tree, HEAD `f4eb906` + uncommitted; parts `workplan_v12_part16.md`, `_part16_cont.md`, `_part17.md`, `_part17_cont.md`, `_part18.md`, `_part18_cont.md`, `_part19.md`, `_part20.md` (part numbers 16 to 20 only). Batches in them: B11-fi-readers (parts 16, 16_cont, 17, 17_cont; 58 positions), B15-pc-calibration (part 18; 16 positions), BA1-cast-content (part 18_cont; 13 positions), B12a-world-motion-and-ground (parts 19, 20; 40 positions). Scripts: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/k4/*.py`.

(This file is written early and appended as the lane proceeds; sections marked PENDING are filled before the receipt.)

## 0. Fixes already applied before this run (commit f4eb906, an earlier K4 run stopped by a container restart; reread, not redone)
- part 16: `EXPECTED RED UNTIL B11.99` line added to the B11 head.
- part 17: the BATCH GATE lines of the second half (test files its items create) and the `EXPECTED RED UNTIL B11.99` line.
- part 18_cont: `EXPECTED RED UNTIL BA1.99` line.
- part 19: `EXPECTED RED UNTIL B12a.99` line and the merge sentence in BATCH GATE naming the second half's added lines.

## 1. Findings (worst first): PENDING
