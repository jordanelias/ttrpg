# 16 · PESSIMIST · SC · D — An argument moves someone: a lost argument moves the arguer, a held one is called held

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-79: the band shares quoted are U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*).
whole-dice at the old default pair; A-79's centre for an even argument on a routine matter is 59% fail, 16% half-land,
25% carry, and the tables are re-measured there; A-81: the Partial band's write named; A-80: a held position is a
source of motion, `30_WR_D_momentum_and_its_brakes.md` §4), §1 (CONFORMS: writes and emits keyed together), §7/§7b
(tests, tier); `unified/U5_CONFLICTS_U5c.md` C-15 (this file is the one carrier of `argument.held`; `08_FI_04` defers);
U3 B27, §6.2 (`p5_argue.py`, `d_projection.py`, `realm_sc.py` are not in the repository). Changed: "The problem"'s and
the projection's figures marked, the Partial bullet, the gate.

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Lands in batch: **B27** (SC), after `16_PESSIMIST_SC_C`. Depends on: `02_CHAR_which_ground_moves_whom.md` (B24) and
`08_FI_04_small-edits.md` (B11).

**Whole-dice figures.** "Pool 2 against Ob 2", the 0.75 / 0.18 / 0.07 table, the projection's 0.81, and "fails 0.33,
succeeds 0.47" were read on the whole-dice sampler and the old opposition (A-5, A-79). Under A-79 an even argument on a
routine matter fails 59%, half-lands 16%, carries 25%; the share in which somebody moves after this edit is
`1 − P(Partial)`, about 0.84 at that centre, and the tables are re-measured there in the landing commit.

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-06 (§2.5, §1.2). Runs: `runs/PES_SC/p5_argue.py`,
`d_projection.py`, `realm_sc.py` (seed 1, four seasons).

## What it changes in `engine/season/` at runtime

An `argue` that lands in Failure moves the **arguer's** held pursuits one step toward the hearer's, by
the rule that today moves the hearer at Success. The Partial band's Event is renamed from
`argument.won` to `argument.held`. Hashes move in every world where an `argue` is rolled; declared.

## The problem, measured

`p5_argue.py`, 300 seeded arguments, shipped fixtures (pool 2 against obstacle 2):

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
- Partial: nobody's pursuits move, and the Event is `argument.held`. The scene is not still (A-81): the Event is
  witnessed and deposited as a claim in the hearer's ledger and each witness's (a belief gained: that the
  position held), which `30_WR_D_momentum_and_its_brakes.md` §3 counts as a durable write ("a claim deposited
  in the actor's or a counterparty's ledger counts") `[ASSUMPTION: that definition is the suite's, not yet
  checked against `write_matrix.yaml` by a lane — basis: A-81's own assumption]`. A held position is a source
  of motion (A-80): the arguer who could not move the hearer turns to another means on the same matter
  (`30_WR_D` §4); this row adds no write for it.

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
   Wherever `rosters.yaml` authors a `deed:argument.won` cell, a `deed:argument.held` cell of the same
   value is added beside it, so no regard moves by the rename.

**Not in this proposal, named:** what is argued. The same draw moves the hearer identically on three
different Propositions, his own included (audit §1.2), and in the realm every argued Proposition is
`(OUGHT, subject, predicate '', value None)`. A Proposition that selects which pursuits move needs
`utter` to form one with content, which is FA's and CORE's formation, and
`02_CHAR_which_ground_moves_whom.md` supplies the hearer's side. The hearer's commitment as resistance
is `05_SC_obstacle_difficulty_and_modifiers_B.md`'s `regard` term (G-60).

## Gate (an execution artifact)

The probes were lane scratch (not in the repository). NEW `engine/season/tests/test_argue_failure_moves_the_arguer.py`:
`test_failure_moves_arguer_one_step_toward_hearer`, `test_partial_emits_argument_held_and_moves_nobody`,
`test_partial_deposits_a_claim_in_the_hearers_ledger` (A-81), `test_backstep_zero_reproduces_todays_failure`
(the control, with edit 1's `writes.Failure` reverted). Command:
`python -m pytest engine/season/tests/test_argue_failure_moves_the_arguer.py -q`. The scratch readings, once committed:

`p5_argue.py` (a) after the edit: "who changed" is non-empty in every Failure and every Success row,
empty in every Partial row, and the share of arguments in which somebody moved is `1 − P(Partial)`
(re-measured at A-79's centre). (d): after 200 arguments the arguer's pursuits have moved. A realm reading
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

Edit (one row, one effect hunk, one function signature, one fixture, one kind). Tier: `sonnet`, effort `high`. Hash
movers declared: every world where an `argue` is rolled; one re-pin at B27's close. Lands it: B27, order 2 (signature,
hash-equal) → 3 → 4 (fixture at control) → 1 (the row's bands and the new kind) → 5 (the `deed:argument.held` cells).
