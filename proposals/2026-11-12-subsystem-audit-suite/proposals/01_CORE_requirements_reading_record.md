# CORE 03 — THE NINE: one typed reading per row, and a propagation measure with a control

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-01, C-U5a-05) — §1 (the `reading:` record) stands. §2 is withdrawn: `harness/chronicle.py --propagation` is not built. R-01's and R-02's `measure:` is the knockout arm of `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` (edits 2–3), with the realm tests of `01_CORE_tests_shipped_world_falsifiers.md` rows 1–2 as the standing falsifiers; one instrument per property. The two statuses are not moved by any proposal of this suite (the knockout reading supports them: 0 and 0 on the controls, 236 to 634 on the arms). The two `measured:` head rewrites of `02_CHAR_reason_trail_and_small_edits.md` Part C land as these rows' `reading.does_not_show`.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row CORE 03, §7 (COMPLETE except lands-it and tier), §7b-T; `unified/U1_GLOSSARY.md` *record / Record*, *reading*; `unified/U3_CONFLICT_LEDGER.md` C3-K5). The withdrawn §2 body (the `chronicle --propagation` reading) is removed and replaced by the head's pointer (stale text is not left beside the decision); the edit list, gate, falsifier and cost class follow; in prose the requirement row carries a **reading** (the `reading:` key keeps its name; "record" is the `Record` carrier, glossary); lands-it and tier added.

Reconciled: 2026-11-12, unification lane U4c (test 9; from `unified/U3_DEPENDENCY_ORDER.md` §3.1, node B02) — dependency line added, which the file lacked: **Depends on:** no other proposal (no inbound edge); it is the first edit of `engine/season/requirements.yaml` and `harness/register.py`, and `01_CORE_tests_shipped_world_falsifiers.md` and `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` depend on it. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "knockout" → "removal test" (glossary *removal test*; file names keep their words).

**Lands in batch:** B02 (hash EQUAL). **Serial edge:** first edit of `engine/season/requirements.yaml` (B02 → B03 → B09 → …, U3 §5.1) and of `harness/register.py`.

## Status: PROPOSED

Source: `audits/01_CORE_audit.md` F-CORE-03; resolutions 5, 6, 7.

## What changes in `engine/season/` at runtime

Nothing in the loop. `engine/season/requirements.yaml` changes shape; `harness/register.py::check_requirements`
reads the new shape. `tools/m1_acceptance.py`'s
doc-derived row still counts `status:` and still says so.

## The problem, with evidence

- `register --requirements` checks that a row has a status word, a `measure:` naming an existing file
  or test name, and non-empty `measured:` (`harness/register.py:631-701`). It ran here in 0.5 s. CI runs
  exactly this (`.github/workflows/valoria-ci.yml:447`). No `measure:` is executed by anything.
- The nine `measured:` fields hold about 135,000 characters. R-01's is 35,912 and opens *"[SUPERSEDED
  by the IN-50 (B-I) paragraph at the end of this block"*. R-05's last recorded figure is *"20 of 56"*;
  the instrument on this tree prints 23 of 67.
- R-01 and R-02 read `met` on the degree-sweep fork-and-follow (`proposals/2026-09-04-degree-sweep/wd_collect.py`
  after 36 chunk runs, about 75 minutes on four cores by the block's account), one seed, with the
  blocks' own caveats: *"no noise estimate"* and *"detected OVER THE BASELINE on ALL 4 plants: False"*.
  The instrument lives under `proposals/`.

## Resolution (decided)

### 1. `measured:` becomes `reading:`, a record

```yaml
- id: R-05
  statement: ...
  status: not_met
  measure: python -m engine.season.harness.corpus_run
  reading:
    tree: 601e715
    date: 2026-11-12
    seed: 0
    seasons: per case
    line: "VERBS THAT EXECUTED : 23 of 67"
    control: none            # or the arm and what it read
    does_not_show: "one seed; a verb executing is not a verb built out"
  blocks: [...]
```

History is the file's git log. `register.py::check_requirements` (owner of the shape) refuses a row
with `status` in `met`/`partial` and no `reading.tree`, `reading.seed` and `reading.line`; it does not
execute anything and does not compare the tree to HEAD (no new guard; a stale reading is visible
because the tree is printed beside the status).

Edit: `engine/season/requirements.yaml` (nine rows; the `scales:` block is untouched);
`harness/register.py:683-694` (the `measured` test and the print line, which gains `reading.tree`).

### 2. R-01 and R-02's instrument (withdrawn here; carried elsewhere)

Withdrawn (head line; C-U5a-01, C3-K5: one instrument per property). R-01's and R-02's `measure:` is the
removal-test arm of `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` (edits 2–3), with the realm tests
of `01_CORE_tests_shipped_world_falsifiers.md` rows 1–2 as the standing falsifiers. No
`chronicle --propagation` is built for a `measure:` (`16_PESSIMIST_GAME_consequence_reading.md` may land it as
an unwired chronicle reading). The two statuses are not moved by this file.

## Gate (execution artifact)

`register --requirements` prints, for each row, status · tree · seed · the reading's line, and exits
non-zero on a `met`/`partial` row with no `reading.tree`, `reading.seed` or `reading.line` (named test,
new: `engine/season/tests/test_register_reading.py::test_a_met_row_without_a_reading_is_refused`).

## Falsifier

For the reading shape: a row whose status moved without its `reading.tree` moving is visible in one
`git log -p` of the file; a planted `met` row with no `reading.line` must make `register --requirements` exit
non-zero.

## NERS reading

Instrument, not play. **N:** the nine are the suite's measuring stick; two of three `met` rows cannot
presently be re-read inside a session. **R:** completeness — the reading carries its control and its
`does_not_show`. **S:** methodology consistent with the other rows (a harness command at named seeds).
**E (last):** nine short readings replace 135,000 characters.

## Cost class

Edit (the reading shape). No hash moves.

**Lands it and tier.** The B02 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B02's
`methodology-close` once.
