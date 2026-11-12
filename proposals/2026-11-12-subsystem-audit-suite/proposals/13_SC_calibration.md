# SC — calibrating the social roll's tables: targets on the four-band ladder, the sweeps, the order

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md` §3, §5; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` edit 8, gate 6), on Jordan's A-71 — three changes to the test this file orders; C1 to C8 stand. (1) The grid is trained ranks 0, 2, 4, 7 (pools 6, 8, 10, 13 under A-6), and "equals" is equal trained rank, not "the counterparty's score equals the actor's pool". (2) One row is added, the even contest: at `plain`, equal ranks meet the obstacle 0.50 ± 0.005 at every rank (A-26). (3) One row is added, the better-arguer curve, with the fight's windows: of exchange pairs in which exactly one side reaches Success, the better arguer is that side in 60 to 70% at one rank, 72 to 82% at two, 88 to 95% at four. Read at the seed values: C1 holds to rank 6; rank 7 reads 30.1% against a 30% ceiling, which OBS §4 step 5 must close (C3-N6) (Failure 56.9 to 60.1%; Success-or-better 22.2 to 30.1%); C3 (score = 2 × pool) and C4 (score = pool ÷ 2) are restated on rank gaps, since a score can no longer be twice a pool: C3, an opponent four ranks better at `routine` fails the actor in 0.75 to 0.90 (read 0.823, 0.809); C4, an opponent four ranks worse, at most 0.45 (read 0.346, 0.351). The test names and expected readings are item 29-4 of that proposal.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-33) — the criteria are stated on outcomes and stand. The values they were solved for are whole-dice at the half-score rate and are re-solved once against the bell curve (Jordan, A-5), score plus a base (A-6), two inputs (A-7) and 0.4 per point (A-26). The test file is read red at `U5c_SC_one_obstacle_form.md` §4 step 4 and green at step 5.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row CAL, §2 row A-80, §6 row *equals at routine*, §7; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-01, ledger R-25, R-26; `unified/U3_CONFLICT_LEDGER.md` C3-N6, C3-C12; `unified/U3_DEPENDENCY_ORDER.md` §6.1, §6.2). Changed: the head's false "C1 holds" is corrected (C3-N6); the body follows the head's three folds (grid on trained ranks, the even-contest row C9 and the better-arguer row C10, C3 and C4 on rank gaps); the composition is OBS's, not SC-B's; `proof_step` → `proof_level`, and the room's subtraction-saturation reading → leverage saturation at the soft cap (A-25); T4's falsifier reads the seat's `modifier:` level (D-U1-01), T5's the `proofs` level; the measured column is marked whole-dice history (A-5); the realm read's scratch probe becomes a named test; A-80's entrenched-world control is cited (C3-C12); lands-it and tier added.

**Lands in batch:** B05 (the test file is written first, read red at OBS §4 step 4 and green at step 5). **Depends on:** `U5c_SC_one_obstacle_form.md` (B05), `13_SC_tuning_tables.md` commit 1 (B05), `29_DICE_one_opposed_rule_form_and_tuning.md` item 29-4 (B05).

## Status: PROPOSED

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §3.4, §6). Sets the
method for `13_SC_tuning_tables.md` (T1–T5) on the one obstacle form (`U5c_SC_one_obstacle_form.md`, which
superseded SC-B's composition). Ratifies nothing; reference under `CLAUDE.md` §0.05.
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

Exact odds, never sampled, for setting values: `modules/social_contest/roll.py::obstacle` (OBS §2,
returning the obstacle and its terms) and `engine.dice_engine.sigma_leverage.record_odds(pool, ob,
leverage)` over planted `SocialContestInput` records. Seconds per full grid. Seeded realm runs (seeds
0–2, one season, `PYTHONHASHSEED=0`; the audit's `realm_tap.py` is a scratch probe not in the repository,
restated as the named test of §5's exact edit 1) are read only for the
**distribution** the shipped content produces, never to set a value: the realm is the check that the
tables are reached, the grid is where they are set.

### 2. The targets (what "calibrated" means)

Reference cell: `plain` room, neutral regard, no evidence, no stakes, no effort; "equals" = equal skill
rank (A-79). Skill scores 0, 2, 4, 7 (pools 6, 8, 10, 13 under A-6). The last column is the audit's
whole-dice reading at the half-score rate (history under A-5; the live readings are lane 29's, quoted in the
Folded line).

| # | situation | target | half-step arm, measured (§3.4; whole-dice history) |
|---|---|---|---|
| C1 | equals, `routine` | P(F) ∈ [0.50, 0.65]; P(Success or better) ∈ [0.15, 0.30] | 0.58–0.64; 0.165–0.216 |
| C2 | each difficulty step, at equals | ΔP(F) ∈ [0.05, 0.20] | 0.06–0.16 |
| C3 | overmatched (an opponent four ranks better), `routine` | P(F) ∈ [0.75, 0.90] | 0.83–0.90 (lane 29: 0.823, 0.809) |
| C4 | underdog opponent (four ranks worse), `routine` | P(F) ≤ 0.45 | 0.31–0.42 (lane 29: 0.346, 0.351) |
| C5 | one full unit of favour (T3 at the clamp, or a room of reception +1) at equals, `routine` | ΔP(F) ≥ 0.12 | 0.16–0.28 |
| C6 | unopposed act (an inquiry, a self-plea) at its row's level | P(F) ∈ [0.25, 0.60] at pool 2–4 | `demanding`: 0.42, 0.32, 0.25 |
| C7 | every calibrated cell | P(F) ≤ 0.90 and P(Partial or better) ≥ 0.10 (the chance floor, CP-T01-06) and P(F) ≥ the `OB_MIN` floor's | holds by the bound |
| C8 | no adjacent pair of levels, rooms or regard values one unit apart at equals, every grid rank | distinct P(F) (≥ 0.03 apart) | holds |
| C9 | the even contest: equals at `plain` | P(margin ≥ 0) = 0.50 ± 0.005 at every rank (A-26) | lane 29: 50.0% |
| C10 | the better arguer: of exchange pairs in which exactly one side reaches Success, the better side | 60–70% at one rank, 72–82% at two, 88–95% at four | lane 29: 66 / 78 / 92% |

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
3. **T3 and T5**: `regard_step` 0 / 0.5 / 1.0 / 2.0 to C5; `proof_level` `None` / `minor` / `moderate` with
   admission on and off to C5's evidence analogue (four standing proofs ≈ one unit of favour; OBS §3, where
   `proof_step` is deleted). Then read leverage saturation on the calibrated arm: favour and proofs arrive as
   levels (A-25), so they saturate at the soft cap `M_MAX`, not at `OB_MIN`; the saturation point is
   reported, not tuned away (the soft cap is the dice engine's).
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
| T4 | a seat-holder's `office` level before his own bench equal to his level before a foreign one when his seat row carries `modifier:` (D-U1-01); a seat in his pool or his opposition; a `determine` disposing `ban` with the same obstacle as one disposing `oblige` |
| T5 | a non-zero `proofs` level under a row that admits no proofs; any `evidence` entry in `terms` (evidence is leverage, A-25) |
| all | any calibrated cell at P(F) 0 or 1 (the standing rule) |

## Exact edits, by owner

1. `engine/season/tests/test_sc_calibration_targets.py` (new; MISSING from the tree, written as B05's
   first commit, U3 §6.1): builds the grid of §2 from `DEFAULT_FIXTURES` through the module's `obstacle`
   and `record_odds`, asserts C1–C10, and asserts it checked `≥ 4 ranks × 10 targets` cells (`CLAUDE.md`
   §0.1 pt 2). The realm read of step 4 is the same file's
   `test_every_rolled_verb_with_five_rolls_shows_more_than_two_obstacles` (OBS gate 4), reading `Margin.terms`
   off SC-P1's record over `build_realm(0..2)`, one season each. It reads the shipped tables, so moving a
   value that breaks a target fails here first.
2. `engine/season/hole_register.yaml`: each T-table fixture's NUMBER row records its sweep arms and the
   target it was set to (C-number), so a re-pin names what it was for.

## Gate (execution artifacts)

- The test file run once against commit 2 of `13_SC_tuning_tables.md`: green; and against commit 1 (the control
  sizes 0/1/2/3, OBS §4 step 3): red on C1 and C8, which is the measured reason for commit 2 (the control shows the test can
  see the failure).
- The realm read of step 4, printed per verb, quoted in commit 2's body.

## Falsifier

The test passes against the control sizes 0/1/2/3 (then it cannot see C1's failure and is absent, not weak).

**Control for A-80.** A-79 makes positions hold (C1: an even argument on a routine matter fails about 59%);
A-80 requires that entrenchment still moves the world. The calibration's control arm for that requirement is
the entrenched-world arm carried by `28_CORE_scene_access_A_occupancy_and_precedence.md` gate row 12,
`28_CORE_scene_access_C_the_petition_that_waits.md` gate row 7 and `23_STORY_D_story_census_and_gate.md`
(C3-C12): with every contest at its control band, the world still produces stories at a stated rate.

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

Edit (one test file and register rows), after OBS steps 0–3 and the tuning tables' commit 1.

**Lands it and tier.** The B05 batch: the test file on `sonnet` (`high`, `valoria-author`), its first commit;
the calibration reading on `opus`; one `methodology-close` for the batch. **Hash movers.** None (a test).
