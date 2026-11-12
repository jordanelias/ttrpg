# 16 · PESSIMIST · SC · A — What the speaker brings is leverage: proofs and a bench's favour as named levels, never an obstacle reduction

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-04 (§1.5). Amends the favourable half of
`05_SC_obstacle_difficulty_and_modifiers_B.md` (G-41, G-57) and of `13_SC_tuning_tables.md` T5; the hard
terms of both are untouched. Runs: `runs/PES_SC/n1_favour_two_ladders.py`, `p1_petitioner.py`.

## What it changes in `engine/season/` at runtime

A `speak` whose speaker holds unmirrored proofs, or whom the bench favours, rolls against the obstacle
the task and the opposition set, with a μ-shift for what he brought. Today those two subtract from the
obstacle. Every other social roll is unchanged (no other prize row is `heard_by: bench`). World hashes
move for any world in which a `speak` rolled with `proofs > 0` or `reception > 0` (the realm: seven
`speak` rolls in four seed-seasons, 13_SC §3.2); declared.

## The problem, measured

`modules/social_contest/roll.py:142-143`:

```python
room = float(inp.reception_gain) * float(inp.reception) + float(inp.proof_step) * float(inp.proofs)
ob = max(ob - room, min(ob, float(OB_MIN))) if room > 0 else ob - room
```

The favourable half is advantage applied as an obstacle reduction and clamped at `OB_MIN`. That is the
form `ED-884` retired for the whole engine (*"the engine applied advantage as an Ob reduction … violating
canon P-232"*; re-ratified `ED-934`, approved by Jordan), and `rosters.yaml: advantage_sources` states
the rule for this very roll: a later source, *"a held finding"* among its examples, is *"a ROW HERE …
never a flat bonus on the net and never an Ob reduction"*. `effort` obeys it. `proofs` and `reception`
predate the roster and do not. Two ladders for one quantity (`CLAUDE.md` §0.06, S).

Exact odds, pool 2, P(Failure), by proofs held (firsthand, unmirrored):

| | 0 | 1 | 2 | 4 | 8 |
|---|---|---|---|---|---|
| shipped, nobody opposes | 0.74 | 0.66 | 0.58 | 0.42 | 0.42 |
| shipped, hostile bench (reception −2) or opponent's score 8 | 0.90 | 0.90 | 0.90 | 0.90 | 0.74 |
| shipped, pool 5 against score 8 | 0.80 | 0.76 | 0.71 | 0.62 | 0.40 |
| **levels** (`minor` per proof), nobody opposes | 0.74 | 0.65 | 0.57 | 0.42 | 0.27 |
| **levels**, hostile bench or score 8 | 0.90 | 0.85 | 0.80 | 0.69 | 0.54 |
| **levels**, pool 5 against score 8 | 0.80 | 0.72 | 0.64 | 0.50 | 0.33 |

Control: `effort` 0 / 1 / 2 before the hostile bench is 0.90 / 0.80 / 0.69 — today two slots of effort
beat four firsthand proofs. In the premise run (`p1_petitioner.py`) a good case moved the speech 0.74 →
0.42 before a neutral bench and not at all before a hostile or a friendly one.

`05_SC_obstacle_difficulty_and_modifiers_B.md` subtracts the favourable terms *after* the ceiling. That
removes the clip and keeps the reduction, the `OB_MIN` saturation (13_SC §4 cell 4: *"the room has three
states, not a scale"*) and the second ladder.

## The resolution, decided

**What stands against the act is the obstacle; what the actor brings is leverage.**

- Obstacle terms (unchanged owner, `roll.py::obstacle`): the task's difficulty, the opposition's
  `score/2`, a hostile bench, a forgery's quality, and SC-B's other hard terms. Each raises the
  obstacle; the ceiling bounds the sum; nothing lowers it, so `OB_MIN` is never approached from above
  by a modifier (P-232 holds by construction, not by a clamp).
- Advantage sources (unchanged owner, `rosters.yaml: advantage_sources` and
  `seam/wrappers/sigma.py::ADVANTAGE_SOURCES`): `effort` (as today), **`proofs`**, **`favour`**. Each
  returns named levels; `levels_to_net_sigma` sums them; `net_boost` applies the soft cap. Bounded
  (±1.5 σ), monotone, uniform in z at every pool.

This follows the ladder at step 1 (`ED-884` / `ED-934`; the roster's own law). It does not contradict
Jordan's clarification of 2026-11-12 (*the obstacle is the task's difficulty plus all modifiers*) on the
reading that a modifier of the obstacle is something that stands against the act; if the clarification
means favourable terms too, SC-B's form stands as written and the saturation above is its cost. That
one reading is listed for Jordan in the audit's §5 (item 1), with both options.

## Exact edits

1. **`engine/season/rosters.yaml: advantage_sources`** — two members after `effort`, in order:
   `proofs`, `favour`. Note text: *`proofs`: one `proof_level` per whole unit of
   `world_q.proofs(speaker, opponent, venue)` (the remove-weighted, unmirrored sum, rounded half up).
   `favour`: one `favour_level` per whole unit of `reception_gain × reception` where that is positive.*
2. **`engine/season/data/fixtures.py`** — `proof_level="minor"` (swept `None` control / `minor` /
   `moderate`), `favour_level="major"` (swept `None` / `strong` / `major`); `proof_step` is deleted
   with its register row (H-216's magnitude becomes `proof_level`'s). `reception_gain` stays and scales
   both halves. Hole-register rows for the two new magnitudes, graded `assumption`, with the sweeps
   above. First values chosen to reproduce today's unclipped odds at pool 2 (table above: 0.65 / 0.57 /
   0.42 against 0.66 / 0.58 / 0.42 for proofs; a unit of reception was Ob −1.0, which at pool 2 is a
   boost of 0.88 σ, and `soft_cap(1.0)` is 0.874).
3. **`engine/season/seam/wrappers/sigma.py`** —
   - `ADVANTAGE_SOURCES = {EFFORT: _effort_levels, "proofs": _proof_levels, "favour": _favour_levels}`
     with `_proof_levels(fx, operands) -> [fx.get("proof_level")] * int(operands.get("proofs", 0) + 0.5)`
     (empty when the fixture is `None`) and `_favour_levels` the same over
     `max(0.0, fx.get("reception_gain") * operands.get("reception", 0.0))`.
   - `_frame`: `leverage=advantage_sigma(fx, {EFFORT: effort, "proofs": room_terms.get("proofs", 0.0),
     "reception": room_terms.get("reception", 0.0)})`. It stays *the one place the operands are named*,
     so `contest_input` and `believed_input` cannot diverge.
4. **`modules/social_contest/roll.py::obstacle`** — lines 142-143 become

   ```python
   hostile = max(0.0, -float(inp.reception_gain) * float(inp.reception))
   ob += hostile
   ```

   and the docstring's two paragraphs on the favourable half and its clip are replaced by one sentence
   naming this proposal's rule. `inp.proofs` and `inp.proof_step` are no longer read by the module;
   `proof_step` leaves `queries/inputs.py::SocialContestInput`, `proofs` stays on the record as a raw
   operand for SC-P1's trace.
5. **Tests re-pointed, not weakened** (`engine/season/tests/test_sc02_reception.py`):
   `test_sc02_17_two_benches…` asserts `_ob(heard) < _ob(plain)`; it becomes
   `_input(heard).leverage > _input(plain).leverage` and keeps its band-differs sweep, which is the
   behaviour. `test_sc02_17_a_told_claim_moves_the_obstacle_strictly_less…` and
   `test_sc02_18_…mirrored proof…` read `leverage` the same way. The hostile assertions are unchanged.
6. **Downstream proposals**: in `05_SC_obstacle_difficulty_and_modifiers_B.md`, the `favourable`
   subtraction and the `evidence` term's favourable half become advantage rows; `Margin.terms` (G-61)
   lists obstacle terms only and SC-P1's record lists the levels by source. In
   `05_SC_evidence_and_rebuttal_B.md` and `19_LACUNA_admission_rides_the_citing_draw.md`, a standing
   item for the speaker is one aggressor level and a standing answer against him one defender level
   (`levels_to_net_sigma(aggressor, defender)` already nets the two).

## Gate (an execution artifact)

`n1_favour_two_ladders.py`'s table A, recomputed through the module after the edit, equals its table B
row for row; and `p1_petitioner.py`'s `speak` column is strictly ordered across all six cells
(hostile/none > hostile/good > neutral/none > neutral/good, friendly/none > friendly/good). Control:
`proof_level=None`, `favour_level=None` gives 0.90 / 0.74 / 0.74 (hostile / neutral / friendly) with
proofs moving nothing.

## Falsifier

A cell in which adding a proof, or a unit of favour, leaves the exact odds unchanged at any pool from 1
to 8 (the dead zone) — present today at four of six cells.

## NERS

- **N**: cut it and evidence goes back to helping only where it is least needed (an unopposed speaker
  before a neutral bench). From the other directions: lateral (combat's advantage is already levels),
  vertical (the same record at every pool), bottom-up (one sum, one cap).
- **R**: complete at the extremes — no floor to saturate against, the soft cap is the bound, a pool of
  1 and a pool of 8 take the same shift in z.
- **S**: one ladder for advantage in the social roll, the same one combat uses.
- **E (ratio)**: two fixtures replace one; one line of the module is removed; a player can now say
  "each thing I can show for my case is one step of advantage".

## Cost class

Edit (one module hunk, one wrapper hunk, two roster members, two fixtures, three test assertions).
