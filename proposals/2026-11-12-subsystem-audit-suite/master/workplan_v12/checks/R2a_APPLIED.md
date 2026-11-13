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
| K1 F5 (B00) | 3 (CLAUDE.md §0.05 cl. 4: ids are process data; the table may be their head) | B00.01's "one-line script over the table" written as a command (the id-block check: ED ranges per lane non-overlapping and `next_free` = last end + 1; H ranges non-overlapping); run here on the tree → `H ok`, nine `FAIL` (the pre-bump control); B00 BATCH GATE line 3 names it → `ok` ×10 | `workplan_v12_part3.md` B00.01 GATE, B00 BATCH GATE |
| K1 F5 (B02.38) | 5 | GATE gains an execution arm: step 6's runs tee to logs; each R-01..R-03 `holds: yes` conjunct's `reading.line` must be in its log (`grep -cF` ≥ 1); `m1_acceptance` row 3 relabelled a record line (DOC-DERIVED), not a gate arm | `workplan_v12_part3_cont.md` B02.38 |
| K1 F6 | 3 (D-17: "the longer form is left to B99's conjunct `argv`") + 4 (R1 repair 2's bracket form; B03.51/.56's "round" → "lap" drift said) | conjunct `argv` cells R-04.a, R-04.c6, R-05.b, R-09.b: `aperture 4` → `aperture 2` with a bracketed `[v12: …]` note (the item's own changes paragraph already said so); `text` of R-02.b, R-03.a, R-03.b and the copied R-03.c assumption: "round" → "lap", identifiers `(season, round)` and `rounds=` kept; one bracketed paragraph says it is the one departure from "verbatim" | `workplan_v12_part3_cont.md` B02.38 step 5 |
| K1 F7 (B02.10, B02.12) | 5 | SITE step gains the locating command: `git show 785bc62:<file> \| sed -n '<L>p'` then `grep -nF` on the current file (`785bc62` reachable: `git cat-file -t` → `commit`); no hit → "absent at base" | `workplan_v12_part3.md` B02.10, B02.12 |
| K1 F7 (B02.33, B02.35) | 3 (E-5: 3 to 8 lines) | each POINTER body gains what-it-does, targets and a gate; B02.35's gate is a command (`measured` count over `requirements.yaml` rows → 0; read 9 at the tree) | `workplan_v12_part3_cont.md` B02.33, B02.35 |
| K1 F7 (B03.55) | 5 | the A38 rewrite's call shape written, `[ASSUMPTION]`-marked: a reading arm takes the provider-derived `pool`/`ob`, then two arms sweep `obstacle_refusal_multiple` (via `Fixtures.sweep`) just above and just below `ob/pool`; refused arm `attempt.refused` 1, admitted arm 0 | `workplan_v12_part5.md` B03.55 |
| K1 F7 (B03.83) | re-checked | no edit: the item already states the shape (per-collection snapshot of `World._STATE_COLLECTIONS`, comparison rule, restore, `not_yours(…)` refusal, the named red-first test, the cost STOPS IF), marked `[ASSUMPTION]` with its basis; that is an executable shape, not a THIN one | `workplan_v12_part5_cont.md` B03.83 |
| K1 F8 | 3 (CLAUDE.md §10: the verify stage that gates a result is `opus`) | reader tier named `opus` (the close's terminal critique) on B03g.02 (item and batch COST), B03.75 (ladder pick and STOPS IF), B03.84 and B03.85 (DROP-IF verdict) | `workplan_v12_part6.md` B03g COST, B03g.02; `_part5_cont.md` B03.75, B03.84, B03.85 |
| K1 F9 | 3 (A-97: "each text follows a ruling") + 4 (A-115: an unlisted amendment applied on A-97's standing authority) | B03.71 step 3 names its licence: Jordan's RS-27 ("the heir still has to claim their throne", IN-61's cited ruling), applied under A-97; a node is re-worded only where RS-27 owes it, never because the code differs; commit body cites RS-27 and A-97 per node; `[ASSUMPTION]` on RS-27 owing the wording. B03.70 unchanged (already the orchestrator's, conditional on (RULED) checks) | `workplan_v12_part5.md` B03.71 |
| K1 F10 | 4 (R1 repair 6: a same-step pair is merge order with a `STOPS IF`, not an edge; B21b.05) | B16L BATCH GATE's `export_season_registries.py --check` arm made conditional on the tool being on the merged head (`test -f`), else "not run: B03g not merged", matching B16L.99 step 2 | `workplan_v12_part6.md` B16L BATCH GATE |
