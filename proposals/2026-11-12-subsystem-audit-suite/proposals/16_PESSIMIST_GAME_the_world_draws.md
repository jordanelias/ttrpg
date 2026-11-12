# GAME — the world's own motion is drawn: hunger and wear per subject, on the weather draw's precedent

## Status: PROPOSED

Source: `audits/16_PESSIMIST_GAME.md` F-PES-GAME-05, §5 rows W-2 to W-4; premise 2.4. Read at `4995824`.
Reference only (`CLAUDE.md` §0.05). Lane IN (the owners are `loop/matter.py` and
`modules/settlements/subsist.py`). It is the MATTER half of `audits/18_DETERMINISM_SWEEP.md`, which
covers the act side (C-01 to C-15) and does not cover the clocks.

Not in this proposal, because another lane owns it: natural death off its control (`09_WR_world_motion.md`
edit 4, Jordan's); the weather draw shipped on (CL-EVENTS commit (2), B10-18, named there); `tend`
as a graded draw (`03_PC_exits_withdrawal_recovery.md` Part C, sweep D-05).

## What it changes in `engine/season/` at runtime

Two fixtures, each with a control arm (`()`) that reproduces every base hash:

1. `hunger_severity_draw`: when an eater goes short, the body loss is today's `body_step × units short`
   times one multiplier drawn **per eater per season** from the fixture's outcomes.
2. `wear_draw`: a Site's seasonal wear is today's `wear_per_season[kind] (+ lattice pull)` times one
   multiplier drawn **per Site per season**.

Both draws are keyed (`state/ids.py::draw_factory`, keyed on `(world_seed, tick, subject, purpose)`), so
the same seed gives the same world and no other stream moves.

## The problem, with evidence

The standing rule (`AUDIT_BRIEF.md`): *a thing that could go either way for the people in the fiction
goes by a draw*. Whether a hungry town loses its weak this winter, and whether this storm takes the
harbour wall, are such things. Today:

- `runs/PES_GAME/x3_nullglobal_s0.txt` (seed 0, every granary emptied and every producing Site at 0
  before each season, nobody acting — a planted famine): all 37 cohorts read body 940, 880, 820 … 40,
  identically, and **all 37 die in the same season, the seventeenth**. `modules/settlements/subsist.py`:
  `lost = inp.body_step * sum(short[pid].values())`; its docstring: *"draws nothing"*.
- `runs/SE/probe_noacts_s0_120.txt` (SE lane) and X1's NULL arm: `condition.worn` 322 a season, every
  Site of a kind by the same step; site condition is equal at seeds 0, 1 and 2 after three played
  seasons (`sites=6227d4facf` in all three `x1_s*_k3.txt`).
- Of the season engine's seven draw sites, four ship off (audit §1.3). The world a player meets has no
  bad winter, no hard year and no town that fares worse than its neighbour.

## The resolution (decided)

Ladder step 4, precedent: `queries/world_q.py::season_factor` — *"each season of the year holds the
equally likely multipliers it draws from"*, `()` the control, keyed per territory. The same shape, per
eater and per Site. The host draws; the module stays pure (it *"draws nothing"*, and keeps that: the
multiplier arrives on its typed input).

## Edits

### 1 · `engine/season/data/fixtures.py` — two fixtures, graded `assumption`

```python
"hunger_severity_draw": (0.0, 0.5, 1.0, 2.0),   # spared · light · full (today's) · hard
"wear_draw":            (0.0, 1.0, 1.0, 3.0),   # a quiet season · ordinary · ordinary · a storm
```

`[ASSUMPTION; medium; Jordan to correct; revert: () for either]` The values are placeholders with mean
near 1 (0.875 and 1.25); the tuned values are Jordan's. `()` ships nothing drawn and is the control.
Per the standing rule the shipped value is non-empty.

### 2 · `engine/season/queries/inputs.py::SubsistInput` — one field

`severity: tuple = ()` — `((pid, multiplier), …)`, empty meaning 1 for every eater.

### 3 · `engine/season/queries/world_q.py::subsist_input` (the host's projection) — fills it

```python
outcomes = w.fixtures.get("hunger_severity_draw")
keyed = draw_factory(w.world_seed, lambda: w.tick)
severity = tuple((pid, keyed(pid, "hunger_severity").choice(outcomes)) for pid in eaters) if outcomes else ()
```

### 4 · `modules/settlements/subsist.py::subsist` — one line

```python
sev = dict(inp.severity)
lost = int(inp.body_step * sum(short[pid].values()) * sev.get(pid, 1))
```

`lost <= 0` already means no fall (the `body_step = 0` control branch), so a spared season needs no
second branch.

### 5 · `engine/season/loop/matter.py`, the wear loop (`wear = w.fixtures.wear(s.kind) + pull.get(s.id, 0)`)

```python
mult = keyed(s.id, "wear").choice(wd) if (wd := w.fixtures.get("wear_draw")) else 1
wear = int((w.fixtures.wear(s.kind) + pull.get(s.id, 0)) * mult)
```

A zero-wear season writes nothing and emits nothing (the gate's no-op), which also thins
`condition.worn` (966 Events in three seasons today).

## Gate (execution artifacts)

- `engine/season/tests/test_hunger.py` (the file covering `settlements.subsist`): with `hunger_severity_draw` at the shipped value and a planted shortfall on every cohort for eight
  seasons, the cohorts' bodies are **not all equal** at the end and the season of first death differs
  between at least two cohorts; with `()` they are all equal and the hash is the base hash (the control).
  The loop asserts it asserted (at least 30 cohorts read).
- The wear half: two Sites of one kind differ in condition after six seasons at the shipped value; equal
  at `()`.
- Falsifier of the proposal's premise: `x3_famine.py 0 0 20 nullglobal` after the change must no longer
  print one synchronized death season.

## What it does not fix

A cohort that is short `tend`s itself whole the same season (audit F-PES-GAME-06: the 37 cohorts lose 60
in season 0 and every one is back at 1000 by the season's end). Until `tend` costs something
(sweep D-05; hole row H-304) a drawn hunger loss is undone as surely as a fixed one.

## NERS

- **N.** Cut the draws and every town is the same town and every year the same year; nothing in the
  material layer can start a story. From the other directions: bottom-up (the keyed draw exists),
  lateral (the weather draw is the sibling), diagonal (a hard year is the occasion the FA and SC lanes'
  petitions and requisitions wait for).
- **R.** The no-player half is the whole of it: this is the world generating difference unwatched.
  Completeness: the multipliers include 0 and an upper outcome; the control is the empty tuple.
- **S.** One methodology for the three clock draws (weather, hunger, wear).
- **E** (last): two fixtures, one input field, two changed lines.

Cost class: edit. Depends on nothing; composes with `07_SE_ground_and_granaries.md` (scarcity must exist
for hunger to be reached at all).
