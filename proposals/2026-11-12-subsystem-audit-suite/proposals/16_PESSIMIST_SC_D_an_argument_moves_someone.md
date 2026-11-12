# 16 · PESSIMIST · SC · D — An argument moves someone: a lost argument moves the arguer, a held one is called held

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-06 (§2.5, §1.2). Runs: `runs/PES_SC/p5_argue.py`,
`d_projection.py`, `realm_sc.py` (seed 1, four seasons).

## What it changes in `engine/season/` at runtime

An `argue` that lands in Failure moves the **arguer's** held pursuits one step toward the hearer's, by
the rule that today moves the hearer at Success. The Partial band's Event is renamed from
`argument.won` to `argument.held`. Hashes move in every world where an `argue` is rolled; declared.

## The problem, measured

`p5_argue.py`, 300 seeded arguments, shipped fixtures (pool 2 against Ob 2):

| band | share | who changed |
|---|---|---|
| Failure, `argument.lost` | 0.75 | nobody |
| Partial, `argument.won` | 0.18 | nobody |
| Success, `argument.won` + `pursuit.moved` | 0.07 | the hearer |

The premise *an NPC argues against an NPC and one of them is moved* holds 0.07 of the time, and the
arguer is never the one. In the realm at seed 1, four seasons: 27 arguments rolled, 21 lost, 6 "won" at
Partial, **0 persons moved** (the SC lane's six-season log at the same seed: 52 rolled, 0 moved; at seed
0, 3 moved of 41).

Because a failure costs nothing, repetition converts: 200 arguments in one fold take the hearer from
`{wealth 1.0, honour 0.2}` to `{wealth 0.185, honour 0.852}` with the arguer unchanged and the hearer's
regard for him unchanged.

`argument.won` at Partial is a label that does not mean what it says (premise-check E10: *a result
called "won" moved something*).

## The resolution, decided

**Every decided argument moves somebody; an undecided one says so.**

- Success, Overwhelming: as today (the hearer moves toward the arguer, one and two steps).
- **Failure: the arguer moves toward the hearer, one step.** He put his position against another's and
  it did not hold. The rule is the one already in the tree, with the two persons exchanged:
  `argued_pursuits(arguer, hearer, …)`. The step is `|DEGREE_STEP[Failure]|` = 1, the ladder's own
  ordinal, which `consequence_pursuits` already reads as *"a failure moves him AGAINST the way the act
  points"* and which the plan names as intended and unbuilt for `determine` (`_eff_determine`'s
  docstring, H-221). Ladder step 3 (that intent) and step 4 (the sibling's method).
- Partial: nobody moves, and the Event is `argument.held`.

The write at Failure is the actor writing his own field, the cleanest ownership the row has (the Success
write is the actor writing another person's pursuits, admitted by the row's band-keyed `writes:`).

What this does to repetition (`d_projection.py`: the shipped `argued_pursuits` applied as proposed, the
same band draws in both arms, 200 seeds):

| arguments | arm | somebody moved, share of arguments | arguer ends (honour / wealth) | hearer ends (honour / wealth) |
|---|---|---|---|---|
| 50 | shipped | 0.07 | 1.00 / 0.00 | 0.44 / 0.69 |
| 50 | proposed | 0.81 | 0.28 / 0.90 | 0.27 / 0.91 |
| 200 | shipped | 0.07 | 1.00 / 0.00 | 0.81 / 0.24 |
| 200 | proposed | 0.81 | 0.27 / 0.91 | 0.27 / 0.91 |

At the default pair (0.74 Failure) a man who keeps arguing is talked round by the people he harangues.
That is a price, and it is steep because the default pair is steep; an arguer with `argue` 6 against
none fails 0.33 and succeeds 0.47 and converts his hearers. The size of the backward step is therefore
a fixture with a control.

## Exact edits

1. **`engine/season/verb_table.yaml`, row `argue`** —
   `writes.Failure: ["Person.pursuits"]`;
   `emits.Failure: ["argument.lost", "pursuit.moved"]`;
   `emits.Partial: ["argument.held"]` (a new kind, emitted by this row alone; `argument.won` stays on
   Success and Overwhelming). `emits_note` gains one sentence naming this proposal.
2. **`engine/season/queries/person_q.py::argued_pursuits`** — signature
   `argued_pursuits(mover, toward, steps, gain)`: `steps` is the number of ladder steps (a non-negative
   number), no longer a band label, so the function holds no band logic; the body is otherwise
   unchanged (only held keys move; a key `toward` does not hold pulls toward 0).
3. **`engine/season/loop/effects_information.py::_eff_argue`** —

   ```python
   step = DEGREE_STEP.get(res.degree, 0)
   if step > 0:
       who, moved = hearer, argued_pursuits(hearer, arguer, step, gain)
   else:
       who, moved = arguer, argued_pursuits(arguer, hearer, abs(step) * w.fixtures.get("argue_backstep"), gain)
   if moved is None:
       return NO_CHANGE
   …
   return Change((Subject.entity("persons", who.id, fields=("pursuits",)),), perform)
   ```

   The fold calls the body only on a band whose `writes:` names the field, so Partial never reaches it.
4. **`engine/season/data/fixtures.py`** — `argue_backstep = 1.0` (swept 0 control / 0.5 / 1.0; a
   hole-register row graded `assumption`, neighbour of H-221). At 0 the Failure band's write declines
   (`NO_CHANGE`), which the row's write-refusal turns into `argument.refused`; so the control arm is
   run with edit 1's `writes.Failure` reverted, and says so.
5. **`engine/season/write_matrix.yaml`** — `(Person, pursuits)`'s row already lists `argue`; no edit.
   `rosters.yaml`'s `deed:` cells gain `deed:argument.held` at the valence `deed:argument.won` carries
   today for Partial (0.0 in the run's printout), so no regard moves by the rename.

**Not in this proposal, named:** what is argued. The same draw moves the hearer identically on three
different Propositions, his own included (audit §1.2), and in the realm every argued Proposition is
`(OUGHT, subject, predicate '', value None)`. A Proposition that selects which pursuits move needs
`utter` to form one with content, which is FA's and CORE's formation, and
`02_CHAR_which_ground_moves_whom.md` supplies the hearer's side. The hearer's commitment as resistance
is `05_SC_obstacle_difficulty_and_modifiers_B.md`'s `regard` term (G-60).

## Gate (an execution artifact)

`p5_argue.py` (a) after the edit: "who changed" is non-empty in every Failure and every Success row,
empty in every Partial row, and the share of arguments in which somebody moved is `1 − P(Partial)`
(0.81 at the default pair). (d): after 200 arguments the arguer's pursuits have moved. A realm reading
at the batch close: `harness/conviction_spread.py` over three seasons, seeds 0 and 1, before and after;
the proposal is withdrawn or `argue_backstep` lowered if the spread of pursuits across persons
collapses.

## Falsifier

An executed `argue` at Failure or Success after which neither person's pursuits differ (other than the
declined cases: a mover who holds no pursuit, or who already stands where the other does).

## NERS

- **N**: cut the Failure write and arguing is free again; repetition is the dominant strategy
  (measured). From the chooser's side (bottom-up) `_writing_bands` now finds a writing band on both
  sides of the ladder, so the believed odds price an `argue` (F-SC-13's mechanism, cited).
- **R**: the no-player half gains the convert and the man talked out of his cause; both sides of a
  quarrel now have something at stake. Complete: a mover with no pursuits declines as today.
- **S**: one method for both movers of the field (`argue`, `determine`'s consequence), one ladder
  ordinal.
- **E (ratio)**: one band of one row, one renamed kind, one fixture; a player can say "if I argue and
  lose, I come away a little persuaded".

## Cost class

Edit (one row, one effect hunk, one function signature, one fixture, one kind).
