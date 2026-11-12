# WR — illness falls the body by a graded draw; death is the body reaching zero

Reconciled: 2026-11-12, U5d closure — folded **A-15** (natural death on, after the 46 ages are authored). "Ships dark … switches nothing on" no longer holds as the end state: the rate goes live behind the authored ages (`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edit 1 owns `Person.born`; this file's edit 4 authors ages into the same field and is merged under it: one writer). The graded bout (a draw on the ladder; death only at body zero) is the form the live rate takes. One re-pin of every seeded result when the rate leaves zero, declared. Order: `U5d_WR_owed_edits.md` §2 (c).

## Status: PROPOSED

Source: `audits/16_PESSIMIST_WR.md` F-PES-WR-07. Read at `d161a61`. Reference only (`CLAUDE.md` §0.05).
Lane WR (owner: `loop/matter.py`'s bodies pass, `queries/world_q.py::body_hazard`).

It corrects one line of a sibling proposal: `09_WR_B_draws_not_thresholds.md` lists illness among the
things that "already comply" with the standing rule. It complies with one clause of three.

It does **not** switch natural death on. `illness_rate` and `age_step` stay at 0 (ED-IN-0317, the WR
audit's §11 item 2, Jordan's). This changes the shape of a mechanism that ships dark, so that when the
rate is set the thing switched on is the one the standing rule describes.

## What it changes in `engine/season/` at runtime

Nothing at the shipped rates (the pass is skipped at `matter.py:726`; the control is byte identical).
With a non-zero rate: an exposed person takes one draw on the one ladder; the degree lowers his **body**
by a step or two or not at all; he dies only when his body reaches zero, through `_die`, as a starved
cohort does. A person's age is authored where an age exists.

## The problem, with evidence

The standing rule (`AUDIT_BRIEF.md`): *a probabilistic roll with a graded, recoverable result; state
sets the odds; the draw sets the outcome*. The bodies pass, opened at `loop/matter.py:726-731`:

```python
hazard = world_q.body_hazard(w, pid)
if hazard > 0 and keyed(pid, "body_hazard").random() < hazard:
    _die(w, token, pid)
```

and `world_q.py:1262-1270`: `min(1.0, illness + age_step * max(0, age_of(w, pid)))`.

1. **Not graded.** Two outcomes: untouched, or dead. There is no ill person in the game, so nothing to
   tend, nothing to fear and nothing to see coming.
2. **Not recoverable.** The one bad outcome removes the person.
3. **State does not set the odds.** The chance is one number for every individual in the realm at a
   given tick. `runs/PES_WR/` (`build_realm(0)`, read at build): all 46 individuals have `born == 0`
   (`age_at_build=0`, `data/fixtures.py:692`), so `age_step` adds the same amount to the King, his heir
   and everyone else, rising in step for the whole cast. Body, hunger in his town, the season and the
   place enter nowhere.
4. **Not on the ladder.** `random() < hazard` is a second resolution methodology beside
   `degree_from_net` (NERS-S: *calculations consistent in methodology with siblings*).

The WR lane's illness arm (their E-11: eight deaths in three seasons at seed 0 with the rate at 0.05)
is that shape observed: eight people at full body, gone, with no Event before the death.

## The resolution, decided

Ladder step 4, by two precedents in the same barrier: the hunger fall (`matter.py:690-711`: one write to
`(Person, body)`, `_crossings` on `band_floors["body"]`, `_die` at zero) and the keyed draw the pass
already takes. Illness becomes a *fall of the body*, so every reader of the body already reads it: the
budget (`decision/budget.py`), the band crossing a co-located person witnesses, `wounded_with` and
`tend`.

- *Exposure* (eligibility for the draw): `illness_rate`, as now, keyed per person per season; 0 is the
  control and takes no draw.
- *Pool (what resists):* `illness_pool_base` + the number of body bands he stands above the lowest
  (`decision/budget.py::bands_below` over `band_floors["body"]`, the one band table): a hale body
  resists better than a failing one.
- *Obstacle (what he faces):* `illness_base` + `age_of(w, pid) // age_band` (the old face more;
  replaces `age_step`'s additive chance) + 1 if the cohort of his settlement went short at this barrier
  (`w._subsistence_shortfall`: dearth breeds sickness) + the season-of-year term when CP-T10-03's
  `season_terms` lands (listed, not built here).
- *Degree* (`seam/ladder.py`, `degree_from_net`):

| degree | his body | write |
|---|---|---|
| Overwhelming, Success | unchanged | none |
| Partial | falls `illness_step` | `body.changed`, then `_crossings` |
| Failure | falls `2 × illness_step` | the same |

Death is `body <= 0` → `_die`, the existing line (`matter.py:709-711`'s shape). A person at full body
needs several bad seasons to die of illness; a person already wounded or starved can die of one.

## The edits

1. **`engine/season/queries/world_q.py::body_hazard`** — keeps the name and the refusals
   (`[0, 1]`, NaN); returns the exposure chance only (`illness_rate`, 0 for a cohort). New beside it:
   `illness_odds(w, pid) -> (pool, obstacle)`, the rule above, a pure read.
2. **`engine/season/loop/matter.py:726-731`** — the block becomes: exposed? → roll `illness_odds`
   through the ladder → on Partial or Failure the body write of `:699-711` (factored into one local
   helper that the hunger fall and this both call, so *what a body fall writes* has one owner in the
   file) → `_die` at zero.
3. **`engine/season/data/fixtures.py`** — `illness_step=100`, `illness_pool_base=2`, `illness_base=2`,
   `age_band=40` (ten years of seasons), each `[ASSUMPTION; medium; Jordan to correct]` with a hole row;
   `age_step` is retired in the same commit (delete, `FORK:` row; its one reader is `body_hazard`).
4. **`engine/season/data/cast.py`** — `age_of(row) -> Optional[int]` on `thread_sensitivity_of`'s shape:
   a cast row's `age:` (in years) gives `Person.born = -4 × age`; a row with none keeps `age_at_build`.
   `references/npc_registry.yaml` carries `age: null [GAP]` on 29 of 46 rows; filling them is content
   and Jordan's, and the loader works with the gaps.
5. **Dependency, not built here:** `tend` must clear a believed wound (WR F-WR-23: `_eff_tend` and a
   MATTER rise write no body Observation), or every person who recovers draws `tend` every season
   after.

## The gate that shows it worked

The test file that covers the bodies pass (`grep -rl body_hazard engine/season/tests`), on
`build_realm`, test arms only (the shipped rate stays 0):

- with exposure at 0.5 over eight seasons at seeds 0 and 1: `body.changed` Events from the pass carry
  at least two distinct falls; **no individual dies in a season he entered at full body**; the set of
  the dead differs between the seeds; the loop asserts it read at least forty individuals;
- two cast rows given ages 20 and 70 (PROXY) differ in their share of falls over forty seeded seasons in
  the expected direction (state sets the odds);
- at least one `tend` forms on an ill individual in at least one seed (recoverable in play);
- at rate 0 the season is the base hash (the control).

## The falsifier

Under any illness arm, a `person.died` whose subject's body was at its ceiling at the barrier's entry.
Today that is every illness death; after the change it must be none.

## NERS reading

- **N.** Cut the grading and illness is a lottery that deletes people: no sickbed, no regent for an
  ailing king, no race between a succession and a death. From the other directions: bottom-up (the body
  cell, its bands, its crossing Event and `tend` all exist and are idle for individuals: in three seasons
  none of 46 is harmed at seed 0 and one at seed 1, a man killed in a `capture`); lateral (hunger already falls a body by this path); diagonal (a
  failing office-holder is the occasion FA's seat-term and regency proposals need); vertical (a town in
  dearth sickens the lord who lives in it, which couples the settlement scale to the personal one).
- **R.** The no-player half: people sicken, linger, recover or die unwatched, each stage an Event.
  Completeness: a cohort takes no draw (its bound is hunger, ED-IN-0255); a body at zero is `_die`'s;
  rate 0 is today.
- **S.** One ladder, one body-fall writer, one band table. `age_step`'s second arithmetic goes.
- **E** (last): one pure read, one changed block, four fixtures, one loader function. The player's
  sentence: *the old, the hungry and the already hurt sicken more easily, and sickness kills by stages*.

## Cost class

Small build. No hash moves at the shipped rates (assert it: the three-hash equality
`test_season_weather.py` holds for the weather control is the pattern).
