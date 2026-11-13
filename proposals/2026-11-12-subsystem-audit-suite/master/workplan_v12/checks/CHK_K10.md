# CHK_K10 — check lane K10 (Sonnet), workplan v12 parts 40 to 43

## Status: WORK ORDER output (a check lane's one-round report on `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

Read: parts `workplan_v12_part40.md`, `_part40_cont.md`, `_part41.md`, `_part41_cont.md` (batch B38-narrative-regimes), `_part42.md`, `_part42_cont.md` (B39-procgen-and-cases), `_part43.md`, `_part43_cont.md` (B40-inst-scenarios). 129 item bodies and 133 position rows (parsed by `scratchpad/k10/parse.py`). Checks are `V12_STRUCTURE_part3.md` §10.1 as the brief numbers them (1 to 11). Appended as I go; sections below are filled in order.

## 0. Parse facts (script `parse.py`, `a1.py`)

- Position rows: B38 65, B39 38, B40 30 (= `workplan_v12_part2.md` §1.3's counts). No handle appears in two rows; no item body without a row. Rows with no body: B39.34, B39.36, B40.09, B40.28, all READING (allowed, §5.3). One boundary row per batch, all three exact (`part41_cont:291`, `part42_cont:300`, `part43_cont:182`).
- `GATE: Batch` lines equal part 2's after-list for each batch (B38 19, B39 23, B40 11; set-compared by script, full handles exact).
- Rows are not in numeric order where a patch inserted one (B39.37 after B39.14; B40.29 after B40.08): the table is landing order, so this is not a defect.
