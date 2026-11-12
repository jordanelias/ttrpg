# 16 · PESSIMIST · SC · E — An honest teller is not marked a liar: a hearer who knows hears true, and a lie has a direction

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-02 and F-PES-SC-10 (§2.2). Owners touched: the telling
workplan's (`loop/witness.py::_told_value`, `ED-IN-0222`; lane IN) and CR-27's (`lie_said_of`); listed
for FI. Runs: `runs/PES_SC/p2_lie.py`, `p2b_lie_extremes.py`, `realm_sc.py` (seed 1).

## What it changes in `engine/season/` at runtime

A half-heard (Partial) number told to a hearer who holds that cell firsthand is heard as the value he
holds, so nothing new is deposited and the teller's record with him is unchanged. A lie about a number
is formed in both directions and the liar's own choice picks one. Hashes move wherever a Partial `tell`
or `lie` of a number reaches a hearer who holds the cell firsthand, and wherever a `lie` forms; declared.

## The problem, measured

`p2_lie.py`, 60 seeded seasons per cell, shipped fixtures; the hearer holds the cell firsthand:

| verb | landed | hearer's `record` of the speaker falls to 0.5 |
|---|---|---|
| `lie` | 13 | 12 |
| `tell` (the truth) | 16 | **13** |

A Partial telling (0.73 of all landings at the default pair) garbles a number through
`person_q.drifted` at `told_drift_band`; a lie falsifies it through the same function at the same band
(`lie_said_of`; `test_cr27_lie.py::test_the_liars_number_and_the_channels_lossy_copy_are_one_rule`). To
a hearer who knows the true value the two are the same event: a told number that disagrees with his.
And a clean (Success) truth to such a hearer deposits nothing (the exact-triple guard,
`loop/witness.py:958`), so it forms no agreeing pair. To a hearer who knows, an honest teller's record
can only fall. `record` is the tree's one separator of liars from honest tellers (`H-183`; CR-83's
designated home), and it does not separate.

Second defect, same function: `lie_said_of` calls `drifted(held, band, 0, whole_band=True)` with the
selector fixed at 0, which is *upward*. Every numeric lie is the held value plus half of it (8 → 12 in
`test_cr27_lie.py`; in the realm at seed 1 the four lies that landed in four seasons said 2 for a held
1 three times and 113 for a settlement's grain the liar held at 40 by the season's end). A village can
boast of grain it lacks and can never hide grain it has; what a liar says is a fixed function of what
he holds (the standing rule), and no interest selects it.

## The resolution, decided

1. **A hearer who holds the cell firsthand resolves a half-heard number to the value he holds.** The
   Partial band's loss is the *listener's* (`_told_value`'s docstring: *"the draw decided what the
   listener took away, never what the teller meant"*); a listener who already knows the figure is not
   left with a different one by mishearing it. The exact-triple guard then suppresses the deposit, as
   it does at Success. Consequences, all intended:
   - an honest teller is never marked by a hearer who knows (0 of 16, from 13 of 16);
   - a liar heard *clearly* (Success or better) by a hearer who knows is marked (the pair disagrees);
     a liar half-heard is not — the knower took it for what he already believed. So a lie is caught by
     someone who knows the truth in `P(Success+) / P(Partial+)` of landings (0.27 at the default pair)
     and by someone who does not in none; the catch is the liar's own draw.
   - a hearer who holds nothing is garbled as today (he has nothing to resolve it against).
   Ladder step 5: the pairing `record` counts is only meaningful if the two things paired are the
   teller's assertion and the hearer's knowledge; today one of them is the channel's noise.
2. **A numeric lie is formed in each direction.** `lie_said_of` returns the false values there are
   (for a number, the step up and the step down, the lower omitted where it would reach or cross zero;
   for a truth value, the one other member, as today), and `opening_set` forms one Candidate per
   value. Which is said is the liar's choice, sampled by the chooser like any other pair of
   candidates; a later interest term (the liar's goal) scores them apart without another edit here.

**Not in this proposal, named:** an agreeing pair for a clean truth told to a knower (it needs a
deposit the guard exists to prevent; the 175-of-180 measurement behind that guard stands), and any
Event or claim that says "a lie was told". Detection stays a reading of `record`, which after edit 1
means something.

## Exact edits

1. **`engine/season/loop/witness.py::_told_value`**, the numeric branch (the last `if`):

   ```python
   if isinstance(held.value, (int, float)) and not isinstance(held.value, bool):
       own = [c for c in w.persons[pid].ledger
              if c.firsthand and c.subject == held.subject and c.predicate == held.predicate]
       if own:
           return LedgerReader(own).belief_among().value     # he knows the figure: he hears it as he holds it
       return drifted(held.value, w.fixtures.get("told_drift_band"), sel)
   ```

   WITNESS already reads the hearer's ledger at this deposit (the exact-triple guard that follows the
   call), so no new read class is opened. A fixture `knower_hears_true` (bool, shipped `True`, swept `False`: the
   control, today's branch) gates the `if own:` so the arm is reversible.
2. **`engine/season/queries/person_q.py::lie_said_of`** — returns a tuple of `Said` (possibly empty)
   instead of `Said | None`; the numeric branch builds `drifted(held, band, 0, whole_band=True)` and
   `drifted(held, band, ceil(band × |held|), whole_band=True)` (the selector whose direction bit is
   downward, `person_q.drifted`'s clause (2); the function's own clamp keeps the sign, so a step that
   would reach zero comes back as the upward one) and drops duplicates and the held value.
3. **`engine/season/decision/options.py::opening_set`** — where a row in `lie_verbs` reads its `said`
   (`said_of_entity[entity] = …`), it iterates the tuple and forms one Candidate per `Said`; a row not
   in `lie_verbs` is untouched.
4. **`engine/season/tests/test_cr27_lie.py`** — `test_a_number_moves_one_whole_step…` asserts both
   values; `test_a_lie_to_a_hearer_who_holds_the_cell_firsthand_lowers_the_liars_record…` forces
   `net=3` (Success) and stands; a new case forces Partial (`net=2` against Ob 2) and asserts the record
   is unchanged for liar and honest teller alike.

## Gate (an execution artifact)

`p2_lie.py` after edit 1: KNOWS / `tell`: `record` 1.0 in every landing; KNOWS / `lie`: 0.5 in the
Success landings and 1.0 in the Partial ones; NOTHING rows unchanged. After edits 2–3: over 200 formed
lies of a held 8, both 12 and 4 are said. Control: `knower_hears_true=False` reproduces today's table.

## Falsifier

A landed truthful telling after which the hearer's `record` of the teller is below 1.0. Present today
in 13 of 16.

## NERS

- **N**: cut edit 1 and `record`, `teller_weight`'s third factor, measures the channel's noise; every
  later reader of a teller's reliability inherits that. From FI's side (lateral) `08_FI_06` and
  CR-83's separator need a record that separates.
- **R**: a lie is caught by a draw, by the right person, and not always; the liar's own roll being
  what exposes him to an eyewitness is a small readable irony. The village that hides its grain
  becomes sayable.
- **S**: the pair `record` counts is the same kind of thing on both sides.
- **E (ratio)**: four lines in one branch, one tuple, one loop; a player can say "telling a man what he
  already knows cannot make him doubt me".

## Cost class

Edit.
