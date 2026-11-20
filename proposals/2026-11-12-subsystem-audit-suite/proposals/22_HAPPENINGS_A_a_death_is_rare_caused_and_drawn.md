# HAPPENINGS-A — a death is rare, caused and drawn: ages, the spell of illness, one mortal reader, and the census that shows it

Reconciled: 2026-11-12, U5d closure — folded **A-15** (natural death on, after the 46 ages are authored). "Dark until you set a rate" is no longer the end state: the bout goes live behind edit 1 (the authored ages; a decision-ready table of the cast's ages is owed by a lane) and a rate, with one re-pin of every seeded result. Edit 1 is the one writer of `Person.born` from authored ages (`16_PESSIMIST_WR_C` edit 4 and `21_PROCEDURAL_B`'s generator write through it). A death's news travels apart from the vacancy it makes (A-33): edit 4's cause on the death Event is read by those who learn of the death, not by everyone who learns the seat is empty. The five-year prologue runs this rule (A-51), so its reading (about one to three natural deaths in twelve seasons) applies to the prologue's twenty seasons as well.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-07, G-08) — `born` is hashed (verified by probe); `mortal_terms` cannot live in `queries/world_q.py` and import `party_end` or `body_band_penalty` (`world_q.py:16-17` forbids both imports), so edit 3's home is corrected in place.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row death_is_rare (1, 2, 5, 6 CONFORMS; 3, 4 AMBIGUOUS), §2 rows "Held back" (A-15), WR_C collision (A-15), edit 1 (A-15, A-75, A-51), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-K4, C3-K10, C3-R2, C3-C8; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-10, §4 row F-42; `unified/U1_GLOSSARY.md` "bout"; `unified/U3_DEPENDENCY_ORDER.md` §1 items 15 and 37, §3.1, §4.1 rows 50, 89). The body now follows the head. Changed: (1) the "Held back, loudly" paragraph and "What it does not do"'s first sentence are replaced: A-15 turned natural death on, behind the authored ages and a rate, with one re-pin; the fixture table gains a "shipped" column; (2) edit 3: `mortal_terms(w, pid, cause, endurance)` stays in `queries/world_q.py` and takes the endurance as an argument from its caller, so `queries/` imports nothing new (25 G-08; C3-R2); it lands in B15 with `14_VERBS_PHYSICAL_A` A3, which passes the operands into `modules/combat/` (C3-C8); (3) edit 4: the spell's roll is a MATTER `step_call` module entry (the `settlements.subsist` / `settlements.produce` shape of `loop/matter.py:45-47`), not `seam/contest.py::grade` (RESOLVE's contest dispatcher); (4) this file owns the pass, the table and the fixtures; `16_PESSIMIST_WR_C_illness_on_the_body_ladder.md`'s exposure terms fold into edit 2 and its table and four fixtures are deleted by its own lane (C3-K4, F-42); (5) authored ages are in years (`age_years:`), converted through the one owner of the year (`len(SEASONS_OF_YEAR)`, D-U1-10); fixtures stay in seasons with years as a gloss; this file is the one writer of `Person.born` (C3-K10); (6) vocabulary: "bout" is the mass battle's 18-tick clash, so illness or age striking a person is a **spell of illness** (or **decline**), and the proposed keys are `spell_*`, the cause `spell` (glossary; the old proposed names `bout_*`, cause `bout`, mean these); (7) the 46 ages are marked INCOMPLETE (content); tests and the gate command are named; the design-arithmetic scripts are named as not in the repository; (8) dependency, batch and tier lines.

Depends on: `10_DICE_one_roller_one_fraction_rule.md` (B05); `09_WR_world_motion.md` (B12); `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 (B12, the year); `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (B15, with this file's edit 3); `03_PC_exits_withdrawal_recovery.md` (B16, `tend` as a draw); `16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` edit 3 (B12, `_die(…, cause=)`); `16_PESSIMIST_WR_C_illness_on_the_body_ladder.md` (B37, reduced, co-lands); `U5d_WR_owed_edits.md` §2 (c) (B37). `21_PROCEDURAL_B_cast_and_seats.md` (B39) ages its generated cast through edit 1's writer later (§4.1 row 89, LATER).
Lands in batch: edit 3 (`mortal_terms`) in B15; edits 1, 2, 4, 5, 6 in B37 (lane IN), first item, with `16_PESSIMIST_WR_C` reduced; the shipped rate in the batch that lands the 46 ages (one re-pin, declared).
Tier: opus for the unification with WR_C and PHYSICAL_A A3's reader (taken here); sonnet / high for the code and tests.

Source: `audits/22_HAPPENINGS.md` §1 (the King), rows H-01, H-02 of §2. Lane IN (owners: `loop/matter.py`,
`queries/world_q.py`, `data/fixtures.py`, `npcs.yaml`). Reference only (`CLAUDE.md` §0.05).
Binds on, and does not redo: `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (the mortal-wound draw),
`16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` edit 3 (`_die(…, cause=)`),
`03_PC_exits_withdrawal_recovery.md` Part C (`tend` as a graded draw, sweep D-05),
`09_WR_world_motion.md` edit 4 (the value is Jordan's), `21_PROCEDURAL_B_cast_and_seats.md` (`age_bands`
for a generated cast), `10_DICE_one_roller_one_fraction_rule.md`.

**A-15 (Jordan): natural death is on, behind the 46 authored ages and a rate.** ED-IN-0317 (c) deferred
`age_step` and `illness_rate` *as shipped values* to Jordan, and `data/fixtures.py:684` says all three
numbers are his; A-15 answers whether (on), and the shipped values are set in the batch that lands the
authored ages, read from the calibration below (the "proposed when on" column is its starting point), with
one re-pin of every seeded result, declared. Until the ages land, the rates stay at the control.

## What it changes in `engine/season/` at runtime

At the control (before the ages land): nothing but `Person.born` (edit 1, a declared mover of every world
hash, since `born` is in the content hash `[GROUNDED, 25 G-07: it is. Two `build_realm(0)` worlds differing only in one person's `born` have different `content_hash()` (`runs/GROUND_ENGINE/g3_small.out`); the field is `state/carriers.py:776`]`).

With `illness_rate` or `age_step` above 0 (shipped on with the ages, A-15):

1. Each season each named person (never a cohort) has a chance that a **spell of illness** (or the
   decline of age) strikes him. The chance is read from state (edit 2).
2. A struck person rolls his body against the spell through the engine's one roller. The four bands
   are four different seasons for him: he shrugs it off, he ails, he is gravely ill, or he is brought
   to death's door. **A man in full health cannot die of one spell**; a man already below the top band
   can (edit 3).
3. A death by a spell cites the spell (edit 4), so a chronicle can say what he died of and the season
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
| Success | he ails for a season | `body` falls `spell_step` | `body.changed` |
| Partial | he is gravely ill | `body` falls `2 × spell_step` | `body.changed` |
| Failure, body at or above the top floor | he is brought low | `body` falls to one below the last floor | `body.changed` |
| Failure, body already below the top floor | he dies | `_die(…, cause=<his last `body.changed`>)` | `person.died`, `tenure.closed` per seat |

Every band but the last is recoverable (`tend`; Part C of the PC proposal makes that a draw too).

## Exact edits, by owner

**1. Ages (`engine/season/npcs.yaml`, read by `data/cast.py`, written by `harness/populated.py`).**
A new optional key `age_years:` on a cast row, an int in **years** (how an age is authored). The builder
sets `Person.born = -(age_years × len(SEASONS_OF_YEAR))`, the year read from its one owner
(`rosters.yaml: seasons_of_year`, `20_NARRATIVE_E` edit 1; D-U1-10), so `world_q.age_of` keeps returning
seasons; a row without the key keeps `-age_at_build`. `data/cast.py` refuses a negative or non-int age at
load. **This is the one writer of `Person.born`** (C3-K10): `16_PESSIMIST_WR_C` edit 4 consumes it, and
`21_PROCEDURAL_B`'s generated persons and `23_STORY_E`'s valley rows are aged through it (the same
`age_years` key, the same conversion). `[ASSUMPTION; medium; Jordan to correct; revert: drop the key]`.
**INCOMPLETE (the 46 values), blocked on content:** the ages are Jordan's or the prose lane's (A-15 orders
a decision-ready table drafted by a lane); `references/npc_registry.yaml` carries `age: null [GAP]` on
most rows (29 of 46 per `16_PESSIMIST_WR_C`), and no source for the rest was read here; this file authors
none. Until they are authored, `age_at_build` moves from 0 to a prime adult's age so that `age_onset`
(edit 2) means something: proposed 140 seasons (35 years at the declared year).

**2. `queries/world_q.py::body_hazard` — the chance a spell strikes, from state.** Same name, same one
caller, same refusal of a rate outside [0, 1]. Returns

```
min(1, illness_rate × season_term × want_term  +  age_step × max(0, age_of(w, pid) − age_onset))
```

- `season_term`: `Fixtures.spell_season_factor[season_of_year(w)]`, a tuple with one multiplier per
  season of the year (its length checked against `len(SEASONS_OF_YEAR)` at the fixture's validation);
  `()` is 1 in every season (the control). Winter above 1.
- `want_term`: `Fixtures.spell_want_factor[band]` for `world_q.hunger` of the person's home settlement
  (`home_of`); `{}` is 1 (the control). Sickness follows dearth in the town, though a named person does
  not eat from the larder (ED-IN-0255 stands).
- `age_onset`: seasons; below it age adds nothing.
- A cohort returns 0, as today.
- **`16_PESSIMIST_WR_C`'s exposure terms fold here (C3-K4):** its dearth term (+1 where his settlement's
  cohort went short at this barrier, `w._subsistence_shortfall`) is the same fact `want_term` reads, and
  `want_term` is its one reader; its age term (`age_of // age_band` on the obstacle) is edit 3's one step
  per `spell_age_every` seasons past `age_onset`. WR_C's table and its fixtures `illness_step`,
  `illness_pool_base`, `illness_base`, `age_band` are deleted by its own lane (F-42); both files keep "no
  individual dies in a season he entered at full body".

**3. `queries/world_q.py::mortal_terms(w, pid, cause, endurance) -> (pool, obstacle)` — new, the one owner
of how hard a body is to kill.** `pool`: the body's endurance, **passed by the caller** (25 G-08; C3-R2):
`queries/` may import neither `party_end` nor `body_band_penalty` (`queries/world_q.py:16-17`: "nothing
here imports `shape`, `decision`, `loop` or `seam`"; `party_end` is `seam/wrappers/combat.py:143` and
composes `decision.body_band_penalty`, `combat.py:86`, `decision/budget.py:71`; and
`seam/wrappers/pool.py:15` already imports `world_q`, so the import would also close a cycle). So the
caller computes `party_end(person, fixtures)` where it may (the bodies pass of `loop/matter.py`; the host
side of the fight for PHYSICAL_A A3) and passes it in; `mortal_terms` stays in `queries/world_q.py` and
imports nothing new. `obstacle`: `Fixtures.mortal_ob[cause]` plus, for `cause == "spell"`, one step per
`spell_age_every` seasons past `age_onset`. `cause` is a member of a closed roster `mortal_causes`
(`rosters.yaml`): `spell`, and PHYSICAL_A A3's three terms `death`, `yield`, `blood`. **PHYSICAL_A A3 reads
its pool and obstacle from this function** (its `mortal_wound_ob` becomes the three keys of `mortal_ob`;
the draw itself runs in `modules/combat/`, keyed `H(seed, tick, subject, "fight.mortal")`, with these
operands on its typed input, C3-C8), so a wound and an illness are one ladder for one quantity
(`CLAUDE.md` §0.06 S). This edit lands in B15 with A3.

**4. `loop/matter.py`, the bodies pass.** Where it reads today

```python
if hazard > 0 and keyed(pid, "body_hazard").random() < hazard:
    _die(w, token, pid)
```

it becomes: on a strike, `pool, ob = world_q.mortal_terms(w, pid, "spell", party_end(person, fixtures))`;
one graded roll through a MATTER `step_call` module entry, the shape `loop/matter.py:45-47` already uses
for `settlements.subsist` and `settlements.produce` (`STEP_CALLS`, resolved through one
`composition_roles:` row in `references/module_contracts.yaml` and checked by
`manifest/registrar.py::require_entries`), returning the degree; not `seam/contest.py::grade`, which is
RESOLVE's contest dispatcher (04 §A.2 `:180-182`). [ASSUMPTION: medium; the role's name (`bodies.spell`)
and its module are the landing commit's — basis: the `settlements.*` precedent; one roller either way.]
The draw is keyed `H(seed, tick, pid, "spell")` (A-30); then the table above. The body write is the hunger pass's own write shape
(`w.write("body", …, emits="body.changed", subject=pid, causes=[prior body.changed or ROOT])`, followed
by `_crossings`). The death is `_die(w, token, pid, cause=<that Event's id>)` (PES-SE-A's signature). The
`body.changed` Event carries `observed=` naming the spell's terms (season, want band, age past onset) by
the `short_seen` precedent in the same file, as `observation_terms` members (D-U1-06), so the cause is on
the record and not in a comment.

**5. `data/fixtures.py`** (each with a `hole_register.yaml` NUMBER row, graded `assumption`, its id from
B00's block). Durations are in seasons; the years beside them are a gloss at the declared year:

| fixture | control | proposed when on | shipped (A-15) | sweep |
|---|---|---|---|---|
| `illness_rate` | 0.0 | 0.04 | set by the calibration in the batch that lands the ages | {0, 0.02, 0.04, 0.08} |
| `age_step` | 0.0 | 0.001 per season past onset | as above | {0, 0.0005, 0.001, 0.002} |
| `age_onset` | — | 180 (45 years) | as above | {160, 180, 200} |
| `spell_age_every` | — | 60 (15 years) | as above | {40, 60, 80} |
| `spell_step` | — | 200 (one band of `band_floors["body"]`) | as above | {100, 200, 300} |
| `mortal_ob["spell"]` | — | 0 | as above | {0, 1} |
| `spell_season_factor` | `()` | (1, 1, 1, 2) | as above | — |
| `spell_want_factor` | `{}` | by hunger band, 1 to 3 | as above | — |
| `age_at_build` | 0 → 140 | 140 | 140 until the ages land | — |

The proposed values are from the arithmetic in §"What the numbers give"; none is written into code by
this file. (Renamed from the earlier proposed `bout_age_every`, `bout_step`, `bout_season_factor`,
`bout_want_factor`, `mortal_ob["bout"]`: the glossary keeps "bout" for the mass battle's clash.)

**6. `harness/aperture.py::death_census` — three columns.** Per death: `cause` (the verb of the killing
act, else the first `causes[]` kind walked back from the death: `spell`, `hunger`, `wound`); `warned`
(a `body.changed` naming the victim in an earlier season of the run); `refilled` (for each seat he held:
the season a `tenure.opened` or `succession.claimed` names it, and the new holder, else `vacant`).
`report` prints them in the existing DEATH CENSUS block and its pooled form (`--seeds`).

## What the numbers give (design arithmetic, not an engine run)

`runs/HAPPEN/bout_calc.py`, `bout_calc2.py` (lane scratch, **not in the repository**; the figures are
design arithmetic, not a gate, and are re-derived by the calibration in the batch that lands the ages):
exact band odds from `dice_engine._die_result` and `degree_from_net` (whole dice; A-5 replaces the
sampler, so the figures are of the old regime and are a starting point only), then 6,000 simulated lives
per age under the table above with the proposed values and a natural mend of 100 a season standing in for
tending.

| age (years) | dies within 4 seasons | within 12 | within 40 | spells in 12 seasons |
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
to make a first spell rarely fatal, which is why death needs the second step.

For a cast of 46 of mixed age this is roughly one to three natural deaths in a twelve-season campaign,
each usually preceded by a season of visible illness. A king of fifty dies in his first year about once
in a thousand worlds.

## Gate (execution artifacts)

- `engine/season/tests/test_in34_bodies_clock.py` (exists; the file covering the bodies pass), three arms
  on the built realm, as named tests: `test_control_both_rates_zero_hash_equal_and_no_draw` (a): both rates
  0, the hash equals the base hash and no draw is taken; `test_on_arm_hale_person_never_dies_in_a_season`
  (b): on, 12 seasons, seeds 0 to 7, with a chooser that returns no scenes (the pass reads no act): at
  least one `body.changed` with a spell in its `observed` at every seed, at least one death across the
  eight, **no death of a person whose body was at or above the top floor at the start of that season**,
  and every death's `causes[0]` a `body.changed`; the loop asserts it asserted (`checked >= 40` strikes);
  `test_planted_below_top_floor_raises_deaths` (c): the same with every person's body planted below the
  top floor: deaths rise (the instrument can see the second step); `test_all_four_bands_occur` in arm (b);
  `test_age_years_converts_through_the_year_roster` (edit 1).
- `python -m engine.season.harness.aperture 4 --seeds 0 1 2`: the DEATH CENSUS with the three new
  columns, quoted in the commit.
- `mortal_terms` (B15): `PHYSICAL_A` A3's gate reads its operands from this function; a test beside
  `test_in34_bodies_clock.py`, `test_mortal_terms_takes_the_endurance_from_its_caller`, asserts that
  `queries/world_q.py` imports nothing from `seam/` or `decision/` (an AST scan of the module's imports).

## Falsifier

- Pin the roll to Failure: arm (b) shows deaths of hale persons and fails.
- Delete the second step (Failure kills at any body): arm (b)'s third assertion fails.
- Control equality: with both rates 0 the twelve-season hash equals the pre-item hash at seeds 0 to 2.

## What it does not do

It does not set the shipped rates: A-15 decided that natural death ships on, and the values are set by
the calibration in the batch that lands the 46 ages. It does not make anyone react to a sick king: the `body.changed` is witnessed and deposited like any other, and who acts on it is the
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

Small build. One declared mover at the control (`born`); the rest goes live with the authored ages and
the calibrated rate (A-15), one re-pin, declared. Depends on PES-SE-A edit 3 for `_die`'s `cause` (or
carries that one-line change itself if it lands first).
