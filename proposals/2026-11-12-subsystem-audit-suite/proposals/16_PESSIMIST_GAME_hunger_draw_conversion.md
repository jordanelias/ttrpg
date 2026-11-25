# GAME: how a body and a shortfall become a pool and an obstacle (the hunger draw's conversion)

## Status: PROPOSED

Plan position: **B12a.57** (workplan v12, `valoria_master_workplan_v12_part20.md`), the design item that settles
`16_PESSIMIST_GAME_the_world_draws.md` edit 3's INCOMPLETE part. Read at `83ef6daf5`. Reference only
(`CLAUDE.md` §0.05): this file is not a mechanism. The two fixtures it names live in
`engine/season/data/fixtures.py` once B12a.58 builds them, and the draw lives in
`engine/season/queries/world_q.py::subsist_input` once B12a.61 builds it. Neither lives here.
The batch's PR merge ratifies this by default (ED-1094).

Sources: `16_PESSIMIST_GAME_the_world_draws.md` edits 1 to 4; `09_WR_B_draws_not_thresholds.md` edit 2 and its
wave-3 Reconciled line ("pool from the roller's score plus base, floor five; obstacle from the task's difficulty and
named terms"); rulings A-5, A-6, A-54.

## 0 · Settled here

| | fixture | form | ships at |
|---|---|---|---|
| pool | `hunger_body_pool` | `sigma_leverage.pool_of(hunger_body_pool × body / condition_scale, 0, pool_add, pool_floor)` | `4` `[ASSUMPTION; medium; Jordan to correct]` |
| obstacle | `hunger_depth_obstacle` | `hunger_depth_obstacle × Σ_k(want_k − take_k) / Σ_k want_k` over the eater's cells (one share, in (0, 1]) | `4.5` `[ASSUMPTION; medium; Jordan to correct]` |
| band → loss | `hunger_band_steps` | `{Overwhelming 0.0, Success 0.5, Partial 1.0, Failure 2.0}` × `body_step × units short` | unchanged: `09_WR_B` edit 2's multiples |

The draw, per eater short this season and with `hunger_severity_draw` on, is
`degree_from_net(roll_net_continuous(pool, rng=draw_factory(world_seed, lambda: w.tick)(pid, "hunger_severity")), ob)`.
This is the form `loop/matter.py::_drawn_wear` (B12a.10) and `world_q.py::_ending_degree` (B12a.12) use. §6 says
where this draw departs from them.

## 1 · The pool a cohort's body gives (`hunger_body_pool`)

**Form.** The cohort is the roller, so its pool comes from the one pool rule,
`engine/dice_engine/sigma_leverage.py::pool_of(score, addends, pool_add, pool_floor)` = `max(pool_floor, score +
addends + pool_add)`. Inputs:

- `score = hunger_body_pool × Person.body / condition_scale`. This is fractional, which the sampler accepts (A-5).
  The body is the cohort's own `Person.body` as `subsist_input` already projects it, read before this season's fall.
- `addends = 0`. The draw is not an act, and no verb row supplies an addend.
- `pool_add` and `pool_floor` are read from the shipped Fixtures pair (H-420 `6`, H-421 `5`) and never retyped.

So a full body rolls `6 + 4 = 10` dice and a body at 1 rolls `6.004`.

**The floor ("floor five") applies, and it applies through the pair, not as a hunger-local floor.** Ladder step 4
gives the precedent: `fixtures.py`'s H-420/H-421 block reads *"One pair for every site (`pool_add`, `pool_floor`);
the per-site names … are not created."* A hunger-local floor would be exactly such a per-site name, so this design
writes none. The floor has a real job here. Without a base, the pool goes to 0 as the body goes to 0, and a pool of
nothing rolls nothing (`continuous_engine_sample` returns `0.0`). The weakest bodies would then fail with certainty,
which is the draw collapsing into a threshold at the bottom. With the shipped pair, the base `pool_add` (6) is what
keeps the pool off zero. At those values `pool_floor` (5) never binds, because the pool is always at least 6.

**Why not floor the body term itself** (`max(5, k × body / scale)`)? A floor on the body term makes every body below
`5000 / k` roll the same pool, which removes the body's effect where it matters most. Score plus base keeps the body
working from end to end.

**A consequence of sharing the pair (stated, not fixed).** Moving the pair moves this draw as it moves every other
roll site. At the swept arm `pool_add 0, pool_floor 5`, the pool is `max(5, 4 × body / 1000) = 5` for every body,
so the body has no effect. At `pool_add 3, pool_floor 5`, every body below 500 rolls 5. These are calibration arms
of H-420/H-421, not shipped values. The cause of the inertness at `(0, 5)` is local: `hunger_body_pool` (4) is below
`pool_floor` (5), so the body's whole score range sits under the shared floor; whoever moves the pair re-reads
`hunger_body_pool` with it. At the pair's declared revert `(0, 0)` (both rows say `revert: 0`) the pool tends to 0
with the body, a body at 1 rolls about 0.004 dice against an obstacle of at least 0.75, P(Failure) is near 1, and
falsifier 4 fails: the threshold at the bottom returns. At `(0, 5)` falsifier 2 fails by construction, since both
pools are 5. Anyone who re-calibrates the pair re-reads §3's table.

## 2 · The obstacle a shortfall gives (`hunger_depth_obstacle`)

**Form.** `ob = hunger_depth_obstacle × depth_share`. Here `depth_share = Σ(want − take) / Σ want` over the eater's
cells in `modules/settlements/larder.py::larder_draw`, the same cells `subsist` reads its `short` from, so the
depth and the loss cannot disagree. The share lies in `(0, 1]`: the draw is taken only when the eater is short.
Like every obstacle it is fractional (A-5). It is one named term, with no difficulty level, because no verb row
stands behind this draw.

**A share, not units.** The magnitude already carries units: edit 4's loss is `body_step × units short ×
multiplier`. (The wear draw, B12a.10, scales its obstacle and its loss with the same rate, so this reason is not
a defect found in it; the reason that carries here is the next.) Units are not comparable across cohorts once weights differ. `want = weight ×
subsistence_weight[kind]` (`larder.py`), and `07_SE_population_census`'s per-head weights (B12b) make weights
differ, so a large cohort one tenth short would face a larger obstacle than a small cohort that is wholly short. The
share asks how hard this shortfall bites against this cohort's need, and the units ask how much is lost.

On the shipped realm today the two readings give the same numbers. Every one of the 37 cohorts has weight 2, so
want is 6 (grain 4, salt 2) and one unit short is a share of 1/6. They part only under per-head weights.

## 3 · Expected band shares at the three named states (computed)

**States** (want = 6, the shipped realm's cohort want):

- **S1** a full body (1000), one unit short (share 1/6)
- **S2** a half body (500), half the want short (3 units, share 1/2)
- **S3** a body at the first floor, the whole want short (6 units, share 1). The first floor is `band_floors.body.full_operations` = 800 (open question 1).

**Method.** Two computations at `83ef6daf5`, both on `engine/dice_engine`:

1. The closed form of the one sampler, `sigma_leverage.band_odds(pool, ob)`. This is the Normal CDF of
   `continuous_engine_sample` against `BAND_FLOORS` in `MARGIN_SCALE`, so it is exact for this sampler with no
   enumeration needed.
2. A seeded sample of 200,000 draws per state through the engine's own path: `roll_net_continuous` on a
   `draw_factory(0, lambda: 0)(f"{state}:{i}", "hunger_severity")` stream, one key per draw as the loop would key
   one eater, graded by `degree_from_net`.

The command was a scratch script, not in the tree. Run from the repo root with `PYTHONHASHSEED=0` and the repo on
`PYTHONPATH`:

```python
from collections import Counter
from engine.dice_engine import sigma_leverage as sl
from engine.dice_engine.dice_engine import degree_from_net
from engine.season.data.fixtures import DEFAULT_FIXTURES as F
from engine.season.state.ids import draw_factory
K, C, WANT, N = 4, 4.5, 6, 200_000
for name, body, short in (("S1", 1000, 1), ("S2", 500, 3), ("S3", 800, 6)):
    pool = sl.pool_of(K * body / F.get("condition_scale"), 0, F.get("pool_add"), F.get("pool_floor"))
    ob = C * short / WANT
    draw = draw_factory(0, lambda: 0)
    got = Counter(degree_from_net(sl.roll_net_continuous(pool, rng=draw(f"{name}:{i}", "hunger_severity")), ob).name for i in range(N))
    print(name, pool, ob, [round(x, 3) for x in sl.band_odds(pool, ob)], {k: round(v / N, 3) for k, v in sorted(got.items())})
```

**Results** (closed form; the 200k sample in brackets; F/P/S/O = Failure/Partial/Success/Overwhelming):

| state | pool | ob | F | P | S | O | expected multiple of `body_step × units` |
|---|---|---|---|---|---|---|---|
| S1 full body, 1 unit short | 10.0 | 0.75 | 0.099 [0.099] | 0.087 [0.087] | 0.274 [0.276] | 0.539 [0.539] | 0.423 |
| S2 half body, half short | 8.0 | 2.25 | 0.337 [0.338] | 0.172 [0.171] | 0.309 [0.309] | 0.183 [0.182] | 1.000 |
| S3 first floor (800), whole short | 9.2 | 4.5 | 0.632 [0.630] | 0.141 [0.141] | 0.169 [0.171] | 0.058 [0.057] | 1.490 |

The sample agrees with the closed form within 0.003 at every cell. At n = 200k the standard error is about 0.001.

**Each axis alone (closed form).** The named states vary body and depth together, and S3's body (800) is better
than S2's (500). This grid holds one axis fixed at a time and shows P(Failure):

| body ↓ / short → | 1 of 6 | 3 of 6 | 6 of 6 |
|---|---|---|---|
| 1000 | 0.099 | 0.244 | 0.578 |
| 800 | 0.114 | 0.278 | 0.632 |
| 500 | 0.139 | 0.337 | 0.717 |
| 100 (the last floor, `withdrawal_only`) | 0.186 | 0.439 | 0.831 |
| 1 | 0.200 | 0.469 | 0.858 |

Every row rises left to right (a deeper shortfall) and every column rises top to bottom (a worse body). No cell is
0 or 1:

- The best cell still fails one season in ten.
- The worst cell (body 1, wholly short) escapes Failure one season in seven (P(not Failure) = 0.142) and is spared
  or lighter than today's step (Success or Overwhelming) about one season in eighteen (0.057); P(Overwhelming) =
  0.005.
- Depth is the stronger lever: at a full body it moves Failure from 0.10 to 0.58. The body is the weaker lever: at
  half short it moves Failure from 0.24 to 0.47. The famine decides, and the weak go first, for a planted body.
  **While H-304 stands** (`engine/season/hole_register.yaml`; `tend` restores a starving cohort's body whole,
  `loop/effects_combat.py::_eff_tend`), a hungry cohort on the realm draws at a body at or near 1000, so there only
  depth and noise separate cohorts, and the body lever's compounding (a cohort that drew badly draws worse next
  season) is reachable only once H-304 is answered. The source document names this limit in its "What it does not
  fix"; the claim above holds for planted bodies.

## 4 · Shipped values

- `hunger_body_pool = 4` `[ASSUMPTION; medium; Jordan to correct]`. The body is a secondary lever worth up to four
  dice on the shared base of six. The value is chosen so that across the whole body range, depth moves Failure
  further than the body does (the grid's two spans above).
- `hunger_depth_obstacle = 4.5` `[ASSUMPTION; medium; Jordan to correct]`. Given the pool, this is the value at
  which **S2's expected loss equals today's step to three decimals** (1.0003 × `body_step × units`, closed form). The middle
  state therefore keeps the control's expected loss, and the draw changes only the spread around it. Lighter
  shortfalls cost less than today on average (S1: 0.42) and deeper ones more (S3: 1.49). This anchors the value
  instead of picking it. The anchor is itself an assumption (open question 3).
- `hunger_band_steps` stays `09_WR_B` edit 2's multiples: `{Overwhelming 0.0, Success 0.5, Partial 1.0, Failure
  2.0}`. Nothing here changes it.
- `hunger_severity_draw`, the arm, ships `False` at B12a.58 and is flipped by B12a.62. That is its owner's matter,
  and this file does not set it.

Unlike `wear_draw_pool` and `ending_draw_*`, which ship `None` and wait on B98, these two rows ship valued, because
B12a.62 flips the hunger arm inside this batch ("Lands it" in the source). The refusal shape still holds:
`_wear_draw_rows`' pattern applies, so an arm read with either row `None` raises `Unspecified`, naming the row.

Proposed sweeps for B12a.58's hole-register rows:

- `hunger_body_pool` 0 (the body term off) / 4 (SHIPPED) / 8
- `hunger_depth_obstacle` 3 / 4.5 (SHIPPED) / 6

B12a.58 allocates the ids.

**Reader's note: no cohort is short at season 0 on the shipped realm.** With B12a.55's `granary_seasons` 4 (and
`ground`, `through`), the realm's larder draw at seed 0, season 0 leaves 0 units short across all 37 cohorts:
`larder_draw(larder_input(build_realm(0)))`, read at `83ef6daf5`. A realm reading at season 0 therefore observes
no hunger draw at all. That is why §3 gives the shares by **planted state** (a body and a depth set by hand), not
by realm reading, and why the falsifiers below are planted.

## 5 · Falsifiers

Each is a planted test for B12a.58 or B12a.61 to write in `engine/season/tests/test_hunger.py`. The closed form
(`band_odds`) is the exact check, and 200 keyed draws per cell are the engine-path check.

1. **Depth (`hunger_depth_obstacle`).** At a fixed body, a deeper shortfall that does not raise Failure's share is
   a falsification. Check: for each body in {1000, 500, 100}, F(1/6) < F(3/6) < F(6/6).
2. **Body (`hunger_body_pool`).** At a fixed depth, a worse body that does not raise Failure's share is a
   falsification. This catches the body term being floored away, `hunger_body_pool` 0, or a pair arm under which the
   floor binds. Check: F(body 100) > F(body 1000) at share 1/2.
3. **No threshold at the top.** A body at 1000 that cannot fall to Failure (`09_WR_B`'s "The falsifier": the draw
   collapsed into a threshold) is a falsification. Check: at S1 over 200 seeds, at least one Failure. The chance of
   none is 0.901^200 ≈ 1e-9.
4. **No threshold at the bottom.** A worst state that is always Failure is a falsification. Check: at body 1,
   wholly short, over 200 seeds, at least one band that is not Failure. The chance of none is 0.858^200 ≈ 5e-14.
5. **The control (`hunger_band_steps` and the arm).** With `hunger_severity_draw` `False`, any body that falls by
   other than `body_step × units short`, or a realm hash that moves, is a falsification. This is the source's
   `test_hunger_draw_off_is_the_base_hash`.
6. **The anchor (a reading, not a gate).** S2's expected multiple, computed by `band_odds` at the shipped values, is
   1.000. If a later re-calibration of `pool_add`/`pool_floor` moves it, the anchor has drifted, and the two rows
   are re-read. Nothing fails.

## 6 · Same form as the clock draws, and where it differs

**Same as wear (B12a.10) and endings (B12a.12):**

- one keyed draw per subject per season through `draw_factory`
- the pool rolled by `roll_net_continuous`, the one sampler
- graded by `degree_from_net`, the one ladder
- the band choosing a multiple of the control's magnitude (`_WEAR_BAND_SHARE`'s shape)
- eligibility from state: only an eater short this season draws, as only a Site that wears draws
- a control arm that takes no draw

**Differs:**

- **The pool goes through `pool_of` and the shared pair.** Wear rolls a raw fixture pool, and an ending rolls
  `pool_step × stood × share` with no floor. The hunger roller is a person, the subject the capability form (A-6;
  `09_WR_B`'s Reconciled line) is written for. A Site and the realm hold no score.
- **The obstacle reads a share, not a count.** Wear's obstacle is `ob_step × rate` in points. Wear rates are
  comparable across Sites of a kind, and wants are not comparable across cohorts (§2).
- **The rows ship valued, not `None`** (§4).

## 7 · Open questions (each with the reading taken)

1. **"The first floor".**
   - (a) `full_operations` 800: `fixtures.py`'s own `body_step` comment calls it "the first floor" ("a person must
     lose 201 to cross the first floor").
   - (b) `withdrawal_only` 100: the last floor before death, which would make the three states descend in body as
     well as depth.
   - **Taken: (a)**, the repo's own usage. §3's grid gives (b)'s row too (F = 0.831 wholly short), so the numbers do
     not depend on the reading.
2. **Depth as units or as a share.**
   - (a) a share of want.
   - (b) units, as wear counts points.
   - **Taken: (a)** (§2). On the shipped realm they differ only by the constant 1/6, so no number in §3 moves. They
     part under B12b's per-head weights.
3. **The anchor for `hunger_depth_obstacle`.**
   - (a) S2's expected loss equals the control step.
   - (b) no anchor: a picked value.
   - **Taken: (a)**, because it ties the value to the control rather than to taste. Ladder step 5: the draw then
     redistributes today's loss at the middle state instead of raising or lowering it. Whether the drawn arm should
     instead make famine deadlier on average is a balance question for the joint calibration (A-5, A-6). It is not
     a fork between two games, so it is not escalated.
4. **Sharing the calibration pair.**
   - (a) `pool_of` with `pool_add`/`pool_floor`.
   - (b) a hunger-local base and floor.
   - **Taken: (a)**, from the precedent "one pair for every site" (H-420's block), with its consequence stated in §1.

No question survives the ladder as a live design fork, so nothing here is `STOPPED` for Jordan. The two values are
`[ASSUMPTION; medium; Jordan to correct]`.

## NERS (reference)

- **N.** Without the conversion, the hunger draw cannot be built, and every hungry cohort keeps falling by the same
  step and dying in the same season (`16_PESSIMIST_GAME_the_world_draws.md`'s premise). This holds from the
  following directions:
  - bottom-up: the pool rule and the sampler exist, and this composes them
  - laterally: wear and endings draw on the same form
  - top-down: a hard year differs from town to town
  - narrowed: cutting `hunger_body_pool` leaves the draw working (depth and noise still separate cohorts); what dies is the
    compounding, which H-304 already erases on the realm (§1), so its N-line holds in narrowed form until H-304 is answered
- **R.** Both extremes still roll (falsifiers 3 and 4). A weak cohort in a deep famine is likelier to suffer but is
  never doomed by arithmetic, so the world makes unequal fates with nobody watching.
- **S.** One ladder and one sampler are shared with the social roll and the clock draws; the pool rule is shared with
  the social roll (the fight reads `score + addends` and never the pair, and the clock draws a raw pool). The
  departure (a share for depth) is stated with its reason.
- **E**, last, as a ratio against N and R: two numbers and two one-line formulas, each composed on an existing
  owner (`pool_of`, `band_odds`, `degree_from_net`). The player can read the outcome as "a deeper famine and a
  weaker people fare worse", which is the intuition the bands carry.
