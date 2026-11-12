# DICE (pessimist) — the obstacle's ceiling saturates as the advantage does: no flat range past the cap

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — stands. Under A-5 the pool's cap is solved on the closed form of the one sampler, and against the largest lawful disadvantage (`U5a_DICE_owed_edits.md` §1 row 3); the tables here are whole-dice figures. Favourable terms are levels, not obstacle reductions (A-25).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-5: every enumerated figure is
whole-dice history; gates 2 and 3 restated as properties on the closed form; A-6: the floor pool is `pool_floor`, so
"pools 1 to 12" and the one-die case are not reachable in play; A-25: edit 6's "favourable halves subtracted" struck),
§1 (A-29: `tanh` is named in the declared float contract), §7/§7b (dependency on the closed-form cap, tier); U3 B05,
§4.1 row 16 (CAP Part B lands with this in B05), C3-L1 (the margin is quantised at the ladder; the obstacle stays a
real number), C3-N26 ("16.5 %" is whole-dice history, unrelated to the throughput file's). Changed: edit 6, the
gate, the cost table's status; the evidence is kept and marked.

## Status: PROPOSED

Lands in batch: **B05** (IN/DICE, SC). Depends on: `U5a_DICE_owed_edits.md` §1 row 3 (`_chance_floor_cap` solved on the
closed form of the one sampler; until it lands this proposal reads the whole-dice `_chance_floor_cap` and its figures
stay void), `05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B, B05; its `bound()` is the function edited),
`U5a_capability_home_and_two_inputs.md` Part B (B05, the pool rule with `pool_floor`).

**Whole-dice figures.** Every percentage below ("90.0 %", "10.0 %", the cost table, gate 3's values) was enumerated on
the whole-dice sampler that A-5 retires; the curve and its properties survive, the figures do not and are re-derived
on the closed form at the calibration. Under A-6 no pool in play is below `pool_floor` (5), so the one-die case and
pools 1 to 4 are statements about the function, not about play.

Carries finding F-PES-DICE-03 of `../audits/16_PESSIMIST_DICE.md`. Lanes that own the edited files: IN
(`engine/dice_engine/sigma_leverage.py`), SC (`modules/social_contest/roll.py`, the obstacle's single
owner by ED-SC-0033 clause 3), with one field on the host record and one fixture. Composes with
`05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B), whose `bound()` is the function edited here.
Reference only (`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

It is a declared mover, small today. A rolled act whose composed obstacle exceeds the fixed ceiling
(`obstacle_ceiling`, shipped 2) at a pool of two or more dice is bounded by a saturating curve instead of
by `min`. In the realm as shipped that is 10 of 284 graded rolls over seeds 0 and 1, two seasons (the
seven examinations of forged Records, which compose 2.699 instead of 2.842, and three `speak` acts
before a hostile bench). Every roll at or below the fixed ceiling, and every roll at one die, composes
exactly what it composes today. The control arm (`ceiling_form: hard`) is today's function.

## The problem, with evidence

`modules/social_contest/roll.py::obstacle` ends `return min(ob, cap)`, where `cap` is the highest
obstacle at which this pool keeps the chance a one-die roll has at the fixed ceiling (10 %, H-213,
CP-T01-06). Past `cap` the function is flat. Measured by exact enumeration through the owner
(`runs/PES_DICE/pure.txt`):

1. **Flat in the pool.** At its own cap every pool from 1 to 12 reads Failure 90.0 %. Against a strong
   enough obstacle a die buys nothing.
2. **Flat in the opposition.** One die reads 10.0 % against scores of 4, 5, 6, 7, 10 and 20; two dice
   against 6 and up.
3. **Flat in every hostile modifier.** For two dice, forgery qualities 1, 2, 3 and 5 compose one
   obstacle (2.842), and receptions of −1, −2, −3 likewise. `default_forgery_quality` is 1, so every
   forged Record in the shipped realm stands on the cap: 7 of 7 examinations rolled at 2.842, and
   H-210's sweep arms 1 and 3 are one arm at the shipped pool.
4. **Control.** With `obstacle_ceiling=None` the same cells separate (16.5 / 7.0 / 4.0 %, then S27.4's
   refusal), so the flatness is the bound's.

The same roll's other operand is bounded differently. `sigma_leverage.soft_cap` is
`M_MAX · tanh(x / M_MAX)`, and its docstring states why: *"Small sums apply nearly fully; large sums
saturate toward ±M_MAX; no hard ceiling and no dead-zone."* Two saturation conventions for the two
operands of one roll is an S defect (`CLAUDE.md` §0.06, *calculations consistent in methodology*), and
the obstacle's is the one with the dead zone.

## The resolution, decided

Ladder step 4 (precedent: the engine's own). The obstacle's **excess over the fixed ceiling** saturates
toward **the pool's cap** by the function the advantage already uses:

```
bounded(ob) = ob                                              if ob <= knee
            = knee + (cap - knee) · tanh((ob - knee)/(cap - knee))   otherwise
knee = obstacle_ceiling            (the fixed ceiling; the cap at one die)
cap  = _chance_floor_cap(pool, obstacle_ceiling)   (unchanged; equals knee at one die)
```

No new number: both operands exist. Properties, each checked (`runs/PES_DICE/soft.txt`):

- identity up to the fixed ceiling, and continuous with slope 1 there;
- strictly below `cap` for every finite obstacle, so the chance never falls under the 10 % the hard cap
  holds (lowest chance seen on a 0.005 grid, pools 1 to 12, Ob 1 to 21: 10.0000 %);
- strictly decreasing chance in the obstacle at pools 3 to 12 over that whole grid, and at pool 2 up to
  Ob 14.9, where `tanh` is 1.0 in a float (a person's score tops at 7, an Ob of 3.5);
- S27.4 unchanged: the largest bounded obstacle ÷ (2 × pool) is 1.0, so no derived pair at a pool of
  one or more is refused, as today;
- at one die `cap == knee` and the function is today's `min`: one die nets at most 2, and no curve can
  give it more.

**What it costs, stated.** Like `soft_cap` (which makes 1.0σ worth 0.874), the curve compresses values
between the knee and the cap, so a strong opposition below a large pool's cap gets easier. (Table:
whole-dice figures, void under A-5; re-derived on the closed form at the calibration. The direction, easier
between knee and cap, is the finding that survives.)

| pool | raw Ob | hard: Ob, P+ | soft: Ob, P+ |
|---|---|---|---|
| 2 | 2.5 | 2.500, 16.50 % | 2.448, 17.48 % |
| 2 | 3.0 | 2.842, 10.00 % | 2.699, 12.72 % |
| 2 | 5.0 | 2.842, 10.00 % | 2.841, 10.03 % |
| 3 | 3.5 | 3.500, 11.20 % | 3.175, 15.11 % |
| 4 | 3.5 | 3.500, 19.90 % | 3.308, 22.98 % |
| 4 | 4.0 | 4.000, 11.86 % | 3.594, 18.39 % |
| 6 | 5.0 | 5.000, 14.19 % | 4.434, 22.09 % |
| 8 | 7.0 | 6.679, 10.00 % | 5.692, 19.24 % |

Nothing in the tree is calibrated to those cells (no person holds a score), which is why this is the
time to choose the form. The size of the bend is Jordan's to tune and is exposed as the sweep below.

## The exact edits, by owner

1. **`engine/dice_engine/sigma_leverage.py`** (the owner of the saturating function). Add

   ```python
   def saturate(x: float, m: float) -> float:
       """`m * tanh(x / m)`: nearly `x` for small `x`, approaching `m` for large; no hard ceiling and no
       dead-zone. The one saturating function: `soft_cap` is it at `M_MAX`, and the social obstacle's
       bound is it over the span between the fixed ceiling and the pool's cap."""
       return m * math.tanh(x / m)
   ```

   and make `soft_cap`'s body `return saturate(net_sigma, M_MAX)` (the same expression; the parity
   goldens are the control and do not move). `math.tanh` is a transcendental the port must match: it is
   listed in the declared float contract that A-29 orders (Layer 1 step 13, text owed,
   `OWED_TO_UNIFICATION.md` §A) and checked by the `fmath` vectors (`11_GO_float_contract.md` Part A; no
   recorder, C3-L3).
2. **`modules/social_contest/roll.py::obstacle`**. Old:

   ```python
       cap = float(ceiling)
       if inp.ceiling_per_pool and inp.pool >= 1:
           cap = _chance_floor_cap(inp.pool, cap) or cap
       return min(ob, cap)
   ```

   New:

   ```python
       knee = float(ceiling)
       cap = knee
       if inp.ceiling_per_pool and inp.pool >= 1:
           cap = _chance_floor_cap(inp.pool, knee) or knee
       if inp.ceiling_form == "hard" or cap <= knee or ob <= knee:
           return min(ob, cap)
       return knee + saturate(ob - knee, cap - knee)
   ```

   with `saturate` added to the module's one import line from `sigma_leverage`, and the docstring's
   ceiling paragraph restated (the sentences *"a hostile room cannot raise…"*, *"a forgery cannot
   raise…"* stay true of the `hard` arm and of one die only).
3. **`engine/season/queries/inputs.py::SocialContestInput`**: `ceiling_form: str = "hard"` (the default
   keeps every hand-built record, test and probe as it is).
4. **`engine/season/seam/wrappers/sigma.py::_frame`**: `ceiling_form=fx.get("ceiling_form")`.
5. **`engine/season/data/fixtures.py`**: `ceiling_form="soft"`, swept `hard` (control) / `soft`
   (shipped) / `soft_late` (the knee one whole success under the cap, never under the fixed ceiling:
   `knee = max(ceiling, cap - 1)`, the arm expected to bend least, `[not measured here]`; listed so the
   sweep has three points and a verdict that flips across it is itself the finding, S42.2.1). It rides H-213's row (the same hole:
   how hard one matter can get); no new row.
6. **SC-B, when it lands**: its `bound(x) = min(x, ceiling)` reads this function instead. The
   favourable halves are advantage rows, levels for the speaker
   (`16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md`; A-25), so `bound()` sees hostile terms
   only; nothing else in SC-B changes.

Order of edits: 1 (hash-equal alias) → 3 and 4 (the field and its host, default `hard`, hash-equal) → 2 (the
module reads the form) → 5 (the fixture flips to `soft`: the one re-pin).

## The gate (execution artifacts)

`runs/PES_DICE/pure.txt` and `soft.txt` were lane scratch, not in the repository; gate 2 is their committed
form. Commands: `python -m pytest engine/season/tests/test_sc01_obstacle_ceiling.py -q` (exists; gains the
gate 2 and gate 3 tests below), then `python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD`.

1. **Control.** At `ceiling_form: hard`, `build_realm(0)` and `build_realm(1)` through the shipped
   chooser for two seasons give `bacd687f1470883b412be9638d0b0f88` and
   `8aae8412c221edb44ffd45d91bae2671` (measured by this lane at 826b747; equal to the SC interrogation
   lane's seed-0 run and the determinism sweep's seed-1 run).
2. **At the owner** (`test_soft_bound_is_strictly_decreasing_and_floored`): over pools `pool_floor` to
   `pool_floor + 10` and obstacles from the knee to 14 in steps of 0.005, the chance of Partial-or-better
   computed on the closed form (`band_odds`) is strictly decreasing and never under
   `1 - band_odds(pool_floor, ceiling)[0]`; the `hard` arm equals `min` (the control inside the test).
3. **Ordered words give ordered odds** (`test_four_forgery_qualities_give_four_ordered_chances`): at the
   floor pool, forgery qualities 0, 0.5, 1 and 3 give four strictly ordered chances under `soft`; under
   `hard` the last two are equal, which is the assertion that can fail. No figure is asserted.
4. **The realm at the shipped arm**: the seven examinations of forged Records in seeds 0 and 1 compose
   2.699; the reading names how many bands moved. Declared hash movers: every world in which a rolled
   act composes above the fixed ceiling; re-pinned once, saying so.

## The falsifier

At the shipped arm: two obstacles a quarter apart, both above the fixed ceiling and below 14, composing
one value at any pool of two or more; a pool of one or more whose chance at any obstacle is under the
one-die chance at the fixed ceiling; any hash that moves at `hard`.

## NERS reading (E last)

- **N.** Bottom-up it reuses one existing function over two existing numbers. Top-down it serves the
  standing rule's *state sets the odds*: past the cap today, state stops setting them. Laterally it
  makes the roll's two operands saturate one way. Cut it and what dies is the difference between a
  good forgery and a masterwork, between a cold bench and a hostile one, between six dice and eight
  against the strongest opposition.
- **R.** Completeness at the extreme: the mechanism no longer goes flat where the fiction is most
  extreme. The floor that M-7 needs is kept exactly.
- **S.** One saturating function, owned once (`saturate`), read by both operands.
- **E.** One function, one field, one fixture, against a dead range that today covers every forged
  document in the realm. For legibility the rule a player holds becomes *"harder is always harder, and
  never hopeless"*.

## Cost class

Edit. One alias in the dice engine, five lines in the obstacle's owner, one field, one fixture arm, one
test body, a re-pin. Tier: `sonnet`, effort `high`. Lands it: B05, with the A-5 sampler and CAP Part B (the
`hard` control arm still equals that batch's hashes); hash movers: every world in which a rolled act
composes above the fixed ceiling, re-pinned once with the batch.
