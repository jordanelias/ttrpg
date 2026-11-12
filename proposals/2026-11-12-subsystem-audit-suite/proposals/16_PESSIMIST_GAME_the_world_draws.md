# GAME — the world's own motion is drawn: hunger and wear per subject, on the weather draw's precedent

Reconciled: 2026-11-12, U5d closure — folded **A-54**: Jordan chose the one four-band ladder over this file's form (multipliers drawn from equally likely tables on the weather draw's precedent). The two fixtures (`hunger_severity_draw`, `wear_draw`) are kept as names and as control arms (`()` reproduces every base hash) and their drawn arm is rewritten to `09_WR_B_draws_not_thresholds.md` edits 1 and 2: a keyed draw on `degree_from_net` with pool and obstacle set by state, the four bands grading the magnitude. The keying (`draw_factory`, per eater and per Site per season), the host-draws-module-stays-pure rule and the gate's control stand. The multiplier-table arm is not built.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 and §1 (A-54: the body's multiplier tables
are removed, not kept beside the drawn form; the drawn arm is `09_WR_B_draws_not_thresholds.md` edits 1-2), §7/§7b (tests,
tier); U3 C3-D6 (B12 order: `09_WR_B` edits 1-3 → `09_WR_world_motion` → `16_PESSIMIST_WR_B` → this file), §4.1 row 47
(`tend` is owned by `14_VERBS_MATERIAL_A_mending.md` §6, not the PC exits file), §6.2 (`x3_*` probes are not in the
repository); A-15 (natural death is on behind authored ages). **Correction to R5 §2 / 7b ("blocked on the band
magnitudes"):** read 2026-11-12, `09_WR_B_draws_not_thresholds.md` edits 1-2 state the band magnitudes (wear:
Overwhelming 0, Success half the rate, Partial the rate, Failure twice; hunger: the same steps of `body_step`) and the
pool and obstacle grounds, so this file is not blocked on them. **One owner per half:** the wear draw is
`09_WR_B` edit 1's own (WR's file, which also names the fixture `wear_draw: False | True`); this file's former edit 5
is struck in its favour. The hunger draw's code (listed for SE by `09_WR_B` edit 2, "the shape stated") is carried
here. Not decidable from the repository: how the cohort's body and the shortfall's depth convert to a pool and an
obstacle on the A-5 sampler; marked INCOMPLETE at edit 3 (the joint calibration).

## Status: PROPOSED

Lands in batch: **B12** (SE/WR), after `09_WR_B_draws_not_thresholds.md` edits 1-3, `09_WR_world_motion.md` and
`16_PESSIMIST_WR_B` edits 1-2 (C3-D6). Depends on: those; the keyed draw owner (`engine/dice_engine/draw.py`, B06);
`07_SE_ground_and_granaries.md` (scarcity must exist for hunger to be reached).

Source: `audits/16_PESSIMIST_GAME.md` F-PES-GAME-05, §5 rows W-2 to W-4; premise 2.4. Read at `4995824`.
Reference only (`CLAUDE.md` §0.05). Lane IN (the owners are `loop/matter.py` and
`modules/settlements/subsist.py`). It is the MATTER half of `audits/18_DETERMINISM_SWEEP.md`, which
covers the act side (C-01 to C-15) and does not cover the clocks.

Not in this proposal, because another lane owns it: natural death (A-15: on, behind the authored ages and a rate,
`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`); the weather draw shipped on (CL-EVENTS commit (2), B10-18,
named there); `tend` as a graded draw (`14_VERBS_MATERIAL_A_mending.md` §6, C-32); the wear draw
(`09_WR_B_draws_not_thresholds.md` edit 1).

## What it changes in `engine/season/` at runtime

One fixture with a control arm (`False`, today's exact `body_step`) that reproduces every base hash:

1. `hunger_severity_draw`: when an eater goes short, one keyed draw **per eater per season** on the shared
   ladder (`degree_from_net`), and the band grades the body loss: Overwhelming none, Success half of today's
   `body_step × units short`, Partial today's, Failure twice (`09_WR_B` edit 2's steps).

The draw is keyed `(world_seed, tick, pid, "hunger_severity")` through the one keyed-draw owner (A-30), so the
same seed gives the same world and no other stream moves.

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

Ladder step 1 (A-54: the world's motion draws on the one four-band ladder, pool against obstacle) and step 4
(`09_WR_B_draws_not_thresholds.md`'s shape: eligibility by state, then a keyed draw on `degree_from_net`; the
`season_factor_of` precedent for a keyed draw inside a Query). The host draws; the module stays pure (it
*"draws nothing"*, and keeps that: the graded multiplier arrives on its typed input).

## Edits

### 1 · `engine/season/data/fixtures.py` — two rows, graded `assumption`

`hunger_severity_draw: bool` (`False` control, today's exact step; `True` the arm, shipped per the standing rule)
and `hunger_band_steps: {Overwhelming: 0.0, Success: 0.5, Partial: 1.0, Failure: 2.0}` (the multiples of
`body_step` that `09_WR_B` edit 2 states; `[ASSUMPTION; medium; Jordan to correct]` as there), each with its
hole-register row (id from `references/id_reservations.yaml` `next_free`). The shape matches `wear_draw` in `09_WR_B`
edit 1 (one methodology for the clock draws).

### 2 · `engine/season/queries/inputs.py::SubsistInput` — one field

`severity: tuple = ()` — `((pid, multiplier), …)`, empty meaning 1 for every eater.

### 3 · `engine/season/queries/world_q.py::subsist_input` (the host's projection) — fills it

For each eater short this season, when `hunger_severity_draw` is on: one draw keyed `(pid, "hunger_severity")`
through the keyed-draw owner (`draw_factory`, B06's `Draw`), rolled on the one sampler with the cohort's own body
as pool ground and the shortfall's depth (how far the larder fell short of want) as obstacle ground (`09_WR_B`
edit 2), graded by `degree_from_net`; `multiplier = hunger_band_steps[band]`. **INCOMPLETE (not decidable from the
repository):** the conversion of a body (0-1000) and a shortfall to a pool and an obstacle on the A-5 sampler is
not stated by the owner; it is set by the joint calibration (A-5, A-6), the batch's first commit writing it as two
named fixtures beside `hunger_band_steps`.

### 4 · `modules/settlements/subsist.py::subsist` — one line

```python
sev = dict(inp.severity)
lost = int(inp.body_step * sum(short[pid].values()) * sev.get(pid, 1))
```

`lost <= 0` already means no fall (the `body_step = 0` control branch), so a spared season needs no
second branch.

### 5 · struck (the wear loop)

The wear draw is `09_WR_B_draws_not_thresholds.md` edit 1 (WR's file; it lands before this in B12); this file
does not edit `loop/matter.py`'s wear loop.

## Gate (execution artifacts)

- `engine/season/tests/test_hunger.py` (exists; the file covering `settlements.subsist`) gains
  `test_hunger_draw_on_bodies_diverge_and_first_deaths_differ`: with `hunger_severity_draw` on and a planted
  shortfall on every cohort for eight seasons, the cohorts' bodies are **not all equal** at the end and the
  season of first death differs between at least two cohorts; the loop asserts it asserted (at least 30
  cohorts read). And `test_hunger_draw_off_is_the_base_hash`: with `False` they are all equal and the hash is
  the base hash (the control). Command: `python -m pytest engine/season/tests/test_hunger.py -q`.
- The wear half's gate is `09_WR_B` edit 1's (two harbours diverge).
- Falsifier of the proposal's premise: the scratch `x3_famine.py 0 0 20 nullglobal` (not in the repository)
  printed one synchronized death season; the first test above is its committed form and must no longer show it.

## What it does not fix

A cohort that is short `tend`s itself whole the same season (audit F-PES-GAME-06: the 37 cohorts lose 60
in season 0 and every one is back at 1000 by the season's end). Until `tend` costs something
(`14_VERBS_MATERIAL_A_mending.md` §6; hole row H-304; `16_PESSIMIST_SE_A` edit 4) a drawn hunger loss is undone as
surely as a fixed one.

## NERS

- **N.** Cut the draws and every town is the same town and every year the same year; nothing in the
  material layer can start a story. From the other directions: bottom-up (the keyed draw exists),
  lateral (the weather draw is the sibling), diagonal (a hard year is the occasion the FA and SC lanes'
  petitions and requisitions wait for).
- **R.** The no-player half is the whole of it: this is the world generating difference unwatched.
  Completeness: the bands include a spared season and a hard one; the control is `False`.
- **S.** One methodology for the three clock draws (weather, hunger, wear): one ladder, keyed per subject.
- **E** (last): two fixture rows, one input field, one draw, one changed line.

Cost class: edit. Depends on the B12 predecessors above; composes with `07_SE_ground_and_granaries.md` (scarcity
must exist for hunger to be reached at all). Tier: `sonnet`, effort `high` for the code; `opus` for the pool and
obstacle conversion at the calibration. Hash movers declared: none at `False`; every world with a hungry eater at
`True` (one re-pin at B12's close). Lands it: B12, order 1 (fixtures at control) → 2 → 4 → 3 → the flip to `True`.
