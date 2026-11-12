# HAPPENINGS-A — a death is rare, caused and drawn: ages, the bout, one mortal reader, and the census that shows it

## Status: PROPOSED

Source: `audits/22_HAPPENINGS.md` §1 (the King), rows H-01, H-02 of §2. Lane IN (owners: `loop/matter.py`,
`queries/world_q.py`, `data/fixtures.py`, `npcs.yaml`). Reference only (`CLAUDE.md` §0.05).
Binds on, and does not redo: `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (the mortal-wound draw),
`16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` edit 3 (`_die(…, cause=)`),
`03_PC_exits_withdrawal_recovery.md` Part C (`tend` as a graded draw, sweep D-05),
`09_WR_world_motion.md` edit 4 (the value is Jordan's), `21_PROCEDURAL_B_cast_and_seats.md` (`age_bands`
for a generated cast), `10_DICE_one_roller_one_fraction_rule.md`.

**Held back, loudly (`CLAUDE.md` §2):** ED-IN-0317 (c) defers `age_step` and `illness_rate` *as shipped
values* to Jordan, and `data/fixtures.py:684` says all three numbers are his. This proposal changes the
**shape** of natural death and ships it at the same control (no draw, every base hash unchanged). Turning
it on is one fixture value and is item 1 of the audit's §4.

## What it changes in `engine/season/` at runtime

At the shipped control: nothing but `Person.born` (edit 1, a declared mover of every world hash, since
`born` is in the content hash `[UNVERIFIED: that `born` is hashed; if it is not, edit 1 moves nothing]`).

With `illness_rate` or `age_step` above 0:

1. Each season each named person (never a cohort) has a chance that a **bout** strikes him: illness or
   the decline of age. The chance is read from state (edit 2).
2. A struck person rolls his body against the bout through the engine's one graded route. The four bands
   are four different seasons for him: he shrugs it off, he ails, he is gravely ill, or he is brought
   to death's door. **A man in full health cannot die of one bout**; a man already below the top band
   can (edit 3).
3. A death by a bout cites the bout (edit 4), so a chronicle can say what he died of and the season
   before it can say he was ill.

## The problem (evidence)

- `queries/world_q.py:1248-1270::body_hazard`: `illness_rate + age_step * age`, one draw, death. No
  band, no warning, no recovery, nothing read but age. It is a fixed two-outcome hazard, not the graded
  draw the standing rule asks for (`AUDIT_BRIEF.md`: *"a probabilistic roll with a graded, recoverable
  result"*).
- `harness/populated.py` builds every person with `born = 0` (probe `runs/HAPPEN/king_0.out`: the King's
  `born` is 0; `21_PROCEDURAL_B`: *"`Person.born` is 0 for 83 of 83"*). With `age_step` on, a king and
  a page age from the same zero.
- WR measured the existing arm (`09_WR_world_motion.md` edit 4): at `illness_rate` 0.05, deaths over
  three seasons go 0 → 8 at seed 0. That is one named person in six dead in under a year, each without
  a day's illness. The control is immortal and the test arm is a plague.
- At the shipped control nobody dies of anything in six seasons at seed 0 (WR addendum B F-WR-22; this
  lane's `king_0.out`).

## The resolution, decided

Ladder step 5 for the shape (the standing rule decides that it is a graded draw; step 4 gives the form:
PHYSICAL_A A3's mortal-wound draw, *pool = his body band, obstacle = a fixture plus named modifiers*).
One body track (`Person.body`, `band_floors["body"]`), one roller, one death owner (`_die`). No new
state: an illness **is** a lowered body, which already costs scene actions (`decision/budget.py::
body_band_penalty`) and already lowers his endurance in a fight.

| band | what happens to him | writes | emits |
|---|---|---|---|
| Overwhelming | he shrugs it off | nothing | nothing |
| Success | he ails for a season | `body` falls `bout_step` | `body.changed` |
| Partial | he is gravely ill | `body` falls `2 × bout_step` | `body.changed` |
| Failure, body at or above the top floor | he is brought low | `body` falls to one below the last floor | `body.changed` |
| Failure, body already below the top floor | he dies | `_die(…, cause=<his last `body.changed`>)` | `person.died`, `tenure.closed` per seat |

Every band but the last is recoverable (`tend`; Part C of the PC proposal makes that a draw too).

## Exact edits, by owner

**1. Ages (`engine/season/npcs.yaml`, read by `data/cast.py`, written by `harness/populated.py`).**
A new optional key `age:` on a cast row, an int in **seasons** (the unit of `world_q.age_of` and of
`21_PROCEDURAL_B`'s `age_bands`). The builder sets `Person.born = -age`; a row without the key keeps
`-age_at_build`. `data/cast.py` refuses a negative or non-int age at load. The 46 values are content
and are Jordan's or the prose lane's; this file authors none. `[ASSUMPTION; medium; Jordan to correct;
revert: drop the key]`. Until they are authored, `age_at_build` moves from 0 to a prime adult's age so
that `age_onset` (edit 2) means something: proposed 140 (35 years at four seasons).

**2. `queries/world_q.py::body_hazard` — the chance a bout strikes, from state.** Same name, same one
caller, same refusal of a rate outside [0, 1]. Returns

```
min(1, illness_rate × season_term × want_term  +  age_step × max(0, age_of(w, pid) − age_onset))
```

- `season_term`: `Fixtures.bout_season_factor[season_of_year(w)]`, a tuple of four multipliers; `()` is 1
  in every season (the control). Winter above 1.
- `want_term`: `Fixtures.bout_want_factor[band]` for `world_q.hunger` of the person's home settlement
  (`home_of`); `{}` is 1 (the control). Sickness follows dearth in the town, though a named person does
  not eat from the larder (ED-IN-0255 stands).
- `age_onset`: seasons; below it age adds nothing.
- A cohort returns 0, as today.

**3. `queries/world_q.py::mortal_terms(w, pid, cause) -> (pool, obstacle)` — new, the one owner of how
hard a body is to kill.** `pool`: the body's endurance, `party_end(person, fixtures)` (the reader the
fight uses: authored endurance less `body_band_penalty`, floored at 1) `[UNVERIFIED: whether `queries/`
may import it from `seam/wrappers/combat.py`; if not, the function moves beside `body_band_penalty` in
`decision/budget.py`, which it already composes on]`. `obstacle`: `Fixtures.mortal_ob[cause]` plus, for
`cause == "bout"`, one step per `bout_age_every` seasons past `age_onset`. `cause` is a member of a
closed roster `mortal_causes` (`rosters.yaml`): `bout`, and PHYSICAL_A A3's three terms `death`, `yield`,
`blood`. **Request to PHYSICAL_A A3:** read its pool and obstacle from this function (its
`mortal_wound_ob` becomes the three keys of `mortal_ob`), so a wound and an illness are one ladder for one
quantity (`CLAUDE.md` §0.06 S). Not edited there.

**4. `loop/matter.py`, the bodies pass.** Where it reads today

```python
if hazard > 0 and keyed(pid, "body_hazard").random() < hazard:
    _die(w, token, pid)
```

it becomes: on a strike, `pool, ob = world_q.mortal_terms(w, pid, "bout")`; one graded roll through
`seam/contest.py::grade` (the route `research` takes; sweep C-01's `task`) on the keyed stream
`keyed(pid, "bout")`; then the table above. The body write is the hunger pass's own write shape
(`w.write("body", …, emits="body.changed", subject=pid, causes=[prior body.changed or ROOT])`, followed
by `_crossings`). The death is `_die(w, token, pid, cause=<that Event's id>)` (PES-SE-A's signature). The
`body.changed` Event carries `observed=` naming the bout's terms (season, want band, age past onset) by
the `short_seen` precedent in the same file, so the cause is on the record and not in a comment.

**5. `data/fixtures.py`** (each with a `hole_register.yaml` NUMBER row, graded `assumption`):

| fixture | control (shipped) | proposed when on | sweep |
|---|---|---|---|
| `illness_rate` | 0.0 (unchanged; Jordan's) | 0.04 | {0, 0.02, 0.04, 0.08} |
| `age_step` | 0.0 (unchanged; Jordan's) | 0.001 per season past onset | {0, 0.0005, 0.001, 0.002} |
| `age_onset` | — | 180 (45 years) | {160, 180, 200} |
| `bout_age_every` | — | 60 (15 years) | {40, 60, 80} |
| `bout_step` | — | 200 (one band of `band_floors["body"]`) | {100, 200, 300} |
| `mortal_ob["bout"]` | — | 0 | {0, 1} |
| `bout_season_factor` | `()` | (1, 1, 1, 2) | — |
| `bout_want_factor` | `{}` | by hunger band, 1 to 3 | — |
| `age_at_build` | 0 → 140 | 140 | — |

The proposed values are from the arithmetic in §"What the numbers give"; none is written into code by
this file.

**6. `harness/aperture.py::death_census` — three columns.** Per death: `cause` (the verb of the killing
act, else the first `causes[]` kind walked back from the death: `bout`, `hunger`, `wound`); `warned`
(a `body.changed` naming the victim in an earlier season of the run); `refilled` (for each seat he held:
the season a `tenure.opened` or `succession.claimed` names it, and the new holder, else `vacant`).
`report` prints them in the existing DEATH CENSUS block and its pooled form (`--seeds`).

## What the numbers give (design arithmetic, not an engine run)

`runs/HAPPEN/bout_calc.py`, `bout_calc2.py`: exact band odds from `dice_engine._die_result` and
`degree_from_net`, then 6,000 simulated lives per age under the table above with the proposed values
and a natural mend of 100 a season standing in for tending.

| age (years) | dies within 4 seasons | within 12 | within 40 | bouts in 12 seasons |
|---|---|---|---|---|
| 20 | 0.000 | 0.003 | 0.013 | 0.6 |
| 35 | 0.000 | 0.002 | 0.011 | 0.6 |
| 50 | 0.001 | 0.006 | 0.038 | 0.9 |
| 60 | 0.014 | 0.097 | 0.418 | 1.4 |
| 70 | 0.025 | 0.158 | 0.763 | 1.8 |
| 80 | 0.094 | 0.450 | 0.932 | 2.0 |

Median age at death about 71 for those who meet no violence. With no mend at all the 50-year-old's
ten-year figure rises from 0.038 to 0.149: recovery matters, which is what makes tending a sick lord an
act worth a scene. The one-step alternative (Failure kills at once) gives a healthy 35-year-old 0.037
in twelve seasons, because a pool of four fails 8.7% of the time at obstacle 0: the ladder is too coarse
to make a first bout rarely fatal, which is why death needs the second step.

For a cast of 46 of mixed age this is roughly one to three natural deaths in a twelve-season campaign,
each usually preceded by a season of visible illness. A king of fifty dies in his first year about once
in a thousand worlds.

## Gate (execution artifacts)

- `engine/season/tests/test_in34_bodies.py` (the file covering the bodies pass), three arms on the built
  realm: (a) control: both rates 0, the hash equals the base hash and no draw is taken; (b) on, 12
  seasons, seeds 0 to 7 with a null chooser (the pass reads no act): at least one `body.changed` with a
  bout in its `observed` at every seed, at least one death across the eight, **no death of a person
  whose body was at or above the top floor at the start of that season**, and every death's `causes[0]`
  a `body.changed`; (c) the same with every person's body planted below the top floor: deaths rise (the
  instrument can see the second step). The loop asserts it asserted (`checked >= 40` strikes).
- `aperture 4 --seeds 0 1 2` DEATH CENSUS with the three new columns, quoted in the commit.
- All four bands occur in arm (b).

## Falsifier

- Pin the roll to Failure: arm (b) shows deaths of hale persons and fails.
- Delete the second step (Failure kills at any body): arm (b)'s third assertion fails.
- Control equality: with both rates 0 the twelve-season hash equals the pre-item hash at seeds 0 to 2.

## What it does not do

It does not decide that natural death ships on (Jordan's, §4 item 1). It does not make anyone react to a
sick king: the `body.changed` is witnessed and deposited like any other, and who acts on it is the
chooser's (`02_CHAR_offer_what_can_be_done.md`, `01_CORE_unmet_need_is_attended_first.md`). It adds no
birth (`07_SE_population_regrowth_B.md`). It names no person: no rule mentions a king.

## NERS reading

- **N.** Cut it and the cast is immortal outside a fight: no succession ever opens by itself, the
  Hafenmark arc cannot start, and age means nothing. From the other directions: bottom-up it reuses the
  body track and the roller; laterally it is the wound's ladder; top-down it is what opens every seat
  the institutions lanes design a succession for; diagonally a hungry town sickens its lord.
- **R.** The half with no player: sickness, recovery and death arise unwatched and differ by seed.
  A player can protect a person (tend him, feed his town, keep him from the field). Complete at the
  extremes: rate 0 is today; a body at the last band and an obstacle above the pool is near-certain
  death and still a draw.
- **S.** One ladder for wound and illness; it pauses nothing; the draw is keyed, so no other stream
  moves.
- **E, last.** One reader, one changed branch, six fixtures, one content key, three report columns,
  against a realm in which people grow old.

## Cost class

Small build. One declared mover at the control (`born`); every other edit is dark until Jordan sets a rate.
Depends on PES-SE-A edit 3 for `_die`'s `cause` (or carries that one-line change itself if it lands
first).
