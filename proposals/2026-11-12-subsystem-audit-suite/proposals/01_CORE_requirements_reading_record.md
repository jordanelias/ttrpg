# CORE 03 — THE NINE: one typed reading per row, and a propagation measure with a control

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-01, C-U5a-05) — §1 (the `reading:` record) stands. §2 is withdrawn: `harness/chronicle.py --propagation` is not built. R-01's and R-02's `measure:` is the knockout arm of `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` (edits 2–3), with the realm tests of `01_CORE_tests_shipped_world_falsifiers.md` rows 1–2 as the standing falsifiers; one instrument per property. The two statuses are not moved by any proposal of this suite (the knockout reading supports them: 0 and 0 on the controls, 236 to 634 on the arms). The two `measured:` head rewrites of `02_CHAR_reason_trail_and_small_edits.md` Part C land as these rows' `reading.does_not_show`.

## Status: PROPOSED

Source: `audits/01_CORE_audit.md` F-CORE-03; resolutions 5, 6, 7.

## What changes in `engine/season/` at runtime

Nothing in the loop. `engine/season/requirements.yaml` changes shape; `harness/register.py::check_requirements`
reads the new shape; one harness reading is added for R-01 and R-02. `tools/m1_acceptance.py`'s
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

### 2. R-01 and R-02 are measured by a chain reading

One function in `harness/chronicle.py` (which already renders causal chains; `[body not opened:
UNVERIFIED that `--chains` exposes the count below]`), printed by one command:

```
python -m engine.season.harness.chronicle --propagation --seeds 0 1 2 --seasons 4
```

- **R-01 (decisions propagate).** Count *consequence chains*: an Event caused by person A's act that
  is deposited in person B's ledger and is then cited (through the act's occasion, `resolve.py::_occasion_ids`)
  by an act of B in a later round or season. Reported per seed as chains / acts.
- **R-02 (decisions affect later decisions).** Fork arm: re-run the same seed with one of A's acts
  withheld (through `Fixtures withheld_verbs` for that actor, or a `dispatching_chooser` override that
  drops the act); report the share of B's later acts whose verb or subject differs.
- **Control, both.** An arm in which no cross-person deposit can occur must read zero chains and zero
  divergence; a planted cross-person deposit must be found. `[UNVERIFIED: whether one of the three
  `rosters.yaml: fan_out_modes` arms deposits nothing across persons; if none does, the control arm is
  the same world with every person housed in a separate, unconnected rung.]` If the planted case is not found the
  reading is void and the status may not rest on it.

`[ASSUMPTION; medium; Jordan to correct]` The statuses are then *read*, not carried: if the chain
reading is non-zero at all three seeds against a zero control, R-01 stays `met`; if the fork divergence
exceeds the same-seed noise (two runs of one arm), R-02 stays `met`. Otherwise each drops to `partial`
in the commit that lands the reading. No threshold is invented beyond "above the control".

Edit: `engine/season/harness/chronicle.py` (one function, one flag); `requirements.yaml` R-01 and
R-02 `measure:` and `reading:`. The degree-sweep under `engine/reference/degree-sweep/` stays as the
frozen probe the season tests execute; it stops being a requirement's instrument.

## Gate (execution artifact)

`register --requirements` prints, for each row, status · tree · seed · the reading's line. The chain
command prints its control line first; exit non-zero when the planted deposit is not found.

## Falsifier

For the record shape: a row whose status moved without its `reading.tree` moving is visible in one
`git log -p` of the file. For the measure: on the control arm chains must be zero — if they are
not, the detector counts something other than propagation through ledgers. If the chain count at seeds
0–2 is zero on the shipped arm, R-01's `met` was unsupported and the row says so.

## NERS reading

Instrument, not play. **N:** the nine are the suite's measuring stick; two of three `met` rows cannot
presently be re-read inside a session. **R:** completeness — the reading carries its control and its
`does_not_show`. **S:** methodology consistent with the other rows (a harness command at named seeds).
**E (last):** nine short records replace 135,000 characters; one command replaces a 36-cell sweep.

## Cost class

Edit (the record) plus a small build (the chain reading). No hash moves. Statuses may move, by reading.
