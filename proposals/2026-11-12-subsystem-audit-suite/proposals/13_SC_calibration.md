# SC — calibrating the social roll's tables: targets on the four-band ladder, the sweeps, the order

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md` §3, §5; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` edit 8, gate 6), on Jordan's A-71 — three changes to the test this file orders; C1 to C8 stand. (1) The grid is trained ranks 0, 2, 4, 7 (pools 6, 8, 10, 13 under A-6), and "equals" is equal trained rank, not "the counterparty's score equals the actor's pool". (2) One row is added, the even contest: at `plain`, equal ranks meet the obstacle 0.50 ± 0.005 at every rank (A-26). (3) One row is added, the better-arguer curve, with the fight's windows: of exchange pairs in which exactly one side reaches Success, the better arguer is that side in 60 to 70% at one rank, 72 to 82% at two, 88 to 95% at four. Read at the seed values: C1 holds (Failure 56.9 to 60.1%; Success-or-better 22.2 to 30.1%, a tenth of a point over C1's edge at rank 7, which step 1's sweep reads); C3 (score = 2 × pool) and C4 (score = pool ÷ 2) are restated on rank gaps by the step-5 lane, since a score can no longer be twice a pool.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-33) — the criteria are stated on outcomes and stand. The values they were solved for are whole-dice at the half-score rate and are re-solved once against the bell curve (Jordan, A-5), score plus a base (A-6), two inputs (A-7) and 0.4 per point (A-26). The test file is read red at `U5c_SC_one_obstacle_form.md` §4 step 4 and green at step 5.

## Status: PROPOSED

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §3.4, §6). Sets the
method for `13_SC_tuning_tables.md` (T1–T5) on SC-B's composition
(`05_SC_obstacle_difficulty_and_modifiers_B.md`). Ratifies nothing; reference under `CLAUDE.md` §0.05.
Under the standing rule (*"we do not do deterministic"*, `AUDIT_BRIEF.md`) every target below is a
distribution with both tails open: no calibrated cell may reach P(Failure) 0 or 1.

## What it changes in `engine/season/` at runtime

Nothing by itself. It adds one test file that executes the composition over a declared grid and
asserts the targets against the shipped fixtures; the values it calibrates move only in
`13_SC_tuning_tables.md`'s commit 2. A calibration is a behaviour test (`CLAUDE.md` §0.05: *"a test that
executes the behaviour"* is a mechanism), not a guard over another guard.

## The problem, with evidence

There is no stated target for what a social contest's odds should be. SC-B chose level sizes by
reproducing today's 2.0 (a control, correctly), not by a target; the audit measured that those sizes put
equals at P(F) 0.71–0.74 and merge the top two levels (§3.4). Without targets, every later value is
taste, and a re-pin cannot be told from a regression (`CLAUDE.md` §7).

## The resolution, decided

### 1. The instrument

Exact odds, never sampled, for setting values: `modules/social_contest/roll.py::obstacle` (after SC-B,
returning the obstacle and its terms) and `engine.dice_engine.sigma_leverage.record_odds(pool, ob,
leverage)` over planted `SocialContestInput` records. Seconds per full grid. Seeded realm runs (seeds
0–2, one season, `PYTHONHASHSEED=0`, the audit's `realm_tap.py` shape) are read only for the
**distribution** the shipped content produces, never to set a value: the realm is the check that the
tables are reached, the grid is where they are set.

### 2. The targets (what "calibrated" means)

Reference cell: `plain` room, neutral regard, no evidence, no stakes, no effort; "equals" = the
counterparty's score equals the actor's pool. Pools 2, 3, 4, 6, 8.

| # | situation | target | half-step arm, measured (§3.4) |
|---|---|---|---|
| C1 | equals, `routine` | P(F) ∈ [0.50, 0.65]; P(Success or better) ∈ [0.15, 0.30] | 0.58–0.64; 0.165–0.216 |
| C2 | each difficulty step, at equals | ΔP(F) ∈ [0.05, 0.20] | 0.06–0.16 |
| C3 | overmatched (score = 2 × pool), `routine` | P(F) ∈ [0.80, 0.90] | 0.83–0.90 |
| C4 | underdog opponent (score = pool ÷ 2), `routine` | P(F) ≤ 0.45 | 0.31–0.42 |
| C5 | one full unit of favour (T3 at the clamp, or a room of reception +1) at equals, `routine` | ΔP(F) ≥ 0.12 | 0.16–0.28 |
| C6 | unopposed act (an inquiry, a self-plea) at its row's level | P(F) ∈ [0.25, 0.60] at pool 2–4 | `demanding`: 0.42, 0.32, 0.25 |
| C7 | every calibrated cell | P(F) ≤ 0.90 and P(Partial or better) ≥ 0.10 (the chance floor, CP-T01-06) and P(F) ≥ the `OB_MIN` floor's | holds by the bound |
| C8 | no adjacent pair of levels, rooms or regard values one unit apart at equals, pools 2–6 | distinct P(F) (≥ 0.03 apart) | holds |

The basis of the numbers: C1 is "a fair fight between equals is a coin with a slight edge to the
status quo" (the contest moves someone; the default is that he stays where he is); C3's upper edge is the
engine's own chance floor; C5 makes favour worth the effort the player can see (two effort levels at pool 2
move P(F) 0.32); C6 keeps inquiries from today's 0.74 failure (the FI lane's dead-end shape) without
making them free. They are design targets, stated once in the test, and Jordan may move any of them by
one edit there.

### 3. The order (one value moved at a time, against its control)

1. **T1 alone**: sweep the size ladder (0/1/2/3, 0/0.5/1/1.5, 0/0.75/1.5/2.25) to C1–C4, C6, C8. The
   half-step ladder passes all six today; take it.
2. **T2 and T4 at fixed T1**: each arrangement row's `standard` at its first-reading level ± 1, and
   `stakes_ob` at 0 / 0.5× / 1× / 2×, in a planted hearing per row (a docketed `speak` and its
   `determine`); a row whose ± 1 changes no band at pools 2–4 is over-ruled by the floor or cap and its
   level is lowered. Here the `floor: open` bump is swept (+1 level on open-floor rows) and kept only if
   it moves C1's cell by ≥ 0.05.
3. **T3 and T5**: `regard_step` 0 / 0.5 / 1.0 / 2.0 to C5; `proof_step` 0 / 0.25 / 0.5 with admission on
   and off to C5's evidence analogue (four standing proofs ≈ one unit of favour). Then read the room's
   saturation (audit degenerate cell 4) on the calibrated arm: at pool 2 the favourable half floors at
   `OB_MIN` after one unit; that is reported, not tuned away, since `OB_MIN` is the dice engine's floor
   (PP-232).
4. **The realm read**: seeds 0–2, one season each, per verb: the obstacle distribution, the band
   distribution and the term list. Expectation stated in advance: until cast scores, relations and
   docketed arrangement rows exist, most realm rolls sit in the `routine` / no-score cell (the content's
   gap, owned by DICE's one-score proposal and CHAR's relations); the read must show T1's level per verb,
   `speak`'s room and the new draws of `13_SC_draw_for_unrolled_contests.md`.

### 4. Per-table falsifiers

| table | falsifier |
|---|---|
| T1 | two adjacent levels with the same P(F) at equals, pools 2–6; or an act whose term list shows `difficulty 0` under a non-`plain` row |
| T2 | a docketed act under a non-`plain` row with no `standard` term; or a row whose ± 1 moves no band at pools 2–4 |
| T3 | SC-B's two-NPC fold: the Events' terms differ by anything but `regard`, or by other than `2 · regard_step · 0.8` |
| T4 | a seat-holder's pool before his own bench equal to his pool before a foreign one at `standing_dice` 1; a `determine` disposing `ban` with the same obstacle as one disposing `oblige` |
| T5 | a non-zero `evidence` term under a row that admits no proofs |
| all | any calibrated cell at P(F) 0 or 1 (the standing rule) |

## Exact edits, by owner

1. `engine/season/tests/test_sc_calibration_targets.py` (new): builds the grid of §2 from
   `DEFAULT_FIXTURES` through the module's `obstacle` and `record_odds`, asserts C1–C8, and asserts it
   checked `≥ 5 pools × 8 targets` cells (`CLAUDE.md` §0.1 pt 2). It reads the shipped tables, so moving a
   value that breaks a target fails here first.
2. `engine/season/hole_register.yaml`: each T-table fixture's NUMBER row records its sweep arms and the
   target it was set to (C-number), so a re-pin names what it was for.

## Gate (execution artifacts)

- The test file run once against commit 2 of `13_SC_tuning_tables.md`: green; and against commit 1 (SC-B's
  sizes): red on C1 and C8, which is the measured reason for commit 2 (the control shows the test can
  see the failure).
- The realm read of step 4, printed per verb, quoted in commit 2's body.

## Falsifier

The test passes against SC-B's 0/1/2/3 sizes (then it cannot see C1's failure and is absent, not weak).

## NERS reading

- **N**: without targets a value cannot be wrong; with them every table has a reason that survives the
  session that set it.
- **R**: the targets keep both tails open everywhere (C7), so a good position still loses and a bad one
  still wins, as the standing rule requires.
- **S**: one instrument (the module's own obstacle and the dice engine's own odds), one ladder, the same
  target shape for a quarrel, a trial and an inquiry.
- **E** (last): eight rows of targets and one test file, against tables whose every value can be
  defended in a sentence.

## Cost class

Edit (one test file and register rows), after SC-B and the tuning tables' commit 1.
