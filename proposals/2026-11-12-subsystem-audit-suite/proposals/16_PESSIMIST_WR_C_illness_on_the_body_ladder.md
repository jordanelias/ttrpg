# WR — illness falls the body by a graded draw; death is the body reaching zero

Reconciled: 2026-11-12, U5d closure — folded **A-15** (natural death on, after the 46 ages are authored). "Ships dark … switches nothing on" no longer holds as the end state: the rate goes live behind the authored ages (`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edit 1 owns `Person.born`; this file's edit 4 authors ages into the same field and is merged under it: one writer). The graded bout (a draw on the ladder; death only at body zero) is the form the live rate takes. One re-pin of every seeded result when the rate leaves zero, declared. Order: `U5d_WR_owed_edits.md` §2 (c).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: U3 C3-K4 and U1 F-42 (`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`
owns the bodies pass and the spell, its four-band table, its fixtures and `mortal_terms`, one ladder for one quantity
with `14_VERBS_PHYSICAL_A` A3; this file is **reduced to its exposure terms**, already folded into HAP_A edit 2: its
own band table, its fixtures `illness_step`, `illness_pool_base`, `illness_base`, `age_band`, and its edits 1-4 are
withdrawn and removed from the body), C3-K10 (one writer of `Person.born`: HAP_A edit 1; this file consumes it), C3-K11 /
D-U1-10 (the year's length is `rosters.yaml: seasons_of_year`; the literal `-4 × age` is gone), `R5_READ.md` §2 (A-15:
natural death is on behind the authored ages; the "ships dark" paragraphs rewritten), §7/§7b (the covering test file);
U3 B37, §4.1 row 49. Kept: the finding (the problem section), the correction to `09_WR_B_draws_not_thresholds.md`, the
"no individual dies in a season he entered at full body" property (HAP_A keeps it too), and edit 5's named dependency.

## Status: PROPOSED (reduced: carried by `22_HAPPENINGS_A` edit 2, C3-K4)

Lands in batch: **B37** (WR), with `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` and `U5d_WR_owed_edits.md` §2 (c)
(U3 §4.1 row 49). Depends on: HAP_A edits 1-4 (B37); `09_WR_B_draws_not_thresholds.md` (B12).

Source: `audits/16_PESSIMIST_WR.md` F-PES-WR-07. Read at `d161a61`. Reference only (`CLAUDE.md` §0.05).
Lane WR (owner of the finding; the bodies pass's owner is HAP_A).

It corrects one line of a sibling proposal: `09_WR_B_draws_not_thresholds.md` lists illness among the
things that "already comply" with the standing rule. It complies with one clause of three.

Under A-15 natural death is on, behind the 46 authored ages and a rate: the rate leaves 0 in the batch that lands
the ages (HAP_A edit 1), one re-pin of every seeded result, declared. The rate-0 arm stays the control.

## What it changes in `engine/season/` at runtime

Nothing of its own: the graded spell on the body is HAP_A's (edits 2-4). This file's two exposure facts are read
there: dearth in the person's settlement raises the chance of a spell (HAP_A's `want_term`), and age past onset
raises it (HAP_A's age term and edit 3's step per `spell_age_every`). With a non-zero rate an exposed person takes
one draw on the one ladder; the degree lowers his **body** or not; he dies only when his body reaches zero,
through `_die`, as a starved cohort does.

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
`tend`. **The form is HAP_A's** (C3-K4): its spell is the one graded draw of the bodies pass, with
`mortal_terms` the one owner of how hard a body is to kill. This file's contribution is two exposure terms,
already folded into HAP_A edit 2:

- *Dearth breeds sickness:* where the cohort of a person's settlement went short at this barrier
  (`w._subsistence_shortfall`), the chance of a spell rises; HAP_A's `want_term` is the one reader of that fact.
- *The old face more:* age past `age_onset` raises the chance (HAP_A's age term) and stiffens the spell (HAP_A
  edit 3's step per `spell_age_every` seasons), replacing `age_step`'s flat additive chance for the whole cast.

## The edits

None of its own (C3-K4): edits 1-4 of the earlier text (a separate `illness_odds`, its own block at
`loop/matter.py:726-731`, the fixtures `illness_step`, `illness_pool_base`, `illness_base`, `age_band`, and
`data/cast.py::age_of` writing `Person.born = -4 × age`) are withdrawn. Ages enter through HAP_A edit 1, the one
writer of `Person.born`, counted in seasons of the declared year (`len(SEASONS_OF_YEAR)`, D-U1-10).

**Dependency, named for HAP_A and the `tend` owner (`14_VERBS_MATERIAL_A_mending.md` §6), not built here:** `tend`
must clear a believed wound (WR F-WR-23: `_eff_tend` and a MATTER rise write no body Observation), or every person
who recovers draws `tend` every season after.

## The gate that shows it worked

The test file that covers the bodies pass is `engine/season/tests/test_in34_bodies_clock.py` (exists; `grep -rl
body_hazard engine/season/tests` finds it), HAP_A's gate file. This file's readings are asserted there, beside HAP_A's
three arms: `test_dearth_raises_the_spell_share` and `test_no_individual_dies_in_a_season_entered_at_full_body`. Command:
`python -m pytest engine/season/tests/test_in34_bodies_clock.py -q`. The readings, on `build_realm`, test arms:

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
- **S.** One ladder, one body-fall writer, one band table (HAP_A's). `age_step`'s second arithmetic goes.
- **E** (last): two exposure terms in HAP_A's one reader, no table of its own. The player's sentence: *the old,
  the hungry and the already hurt sicken more easily, and sickness kills by stages*.

## Cost class

Edit (two assertions in HAP_A's test file; the code is HAP_A's). Tier: `sonnet`, effort `high`. Hash movers
declared: HAP_A's (one re-pin when the rate leaves zero behind the authored ages, A-15). Lands it: B37, with HAP_A.
