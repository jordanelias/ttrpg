# CHAR (pessimist) A — a crisis of faith is drawn, keeps its direction, and is told

## Status: PROPOSED

Written by the CHAR pessimist lane (`audits/16_PESSIMIST_CHAR.md`, F-PES-CHAR-03). Ratifies nothing;
reference under `CLAUDE.md` §0.05. It amends, and does not replace, `02_CHAR_scar_is_a_wound.md` (which
bounds how a scar count is reached) and `02_CHAR_scar_cap_and_regard_unit.md` item 1 (the rate): those
decide WHEN a crisis is reached; this decides WHAT a crisis does.

## What this changes in `engine/season/` at runtime

`queries/person_q.py::conviction_after_crisis` stops being a fixed function of `(conviction, scar)`.
`loop/resolve.py::_conviction_crisis` rolls one draw per person in crisis, grades it on the four-band
ladder, writes the band's result, and emits one Event that WITNESS deposits for the person himself and
for those present. With the new fixture `crisis_draw` at its control (`off`) the function is today's and
the hash is EQUAL. Shipped `on` it is a declared mover: every run in which a crisis fires re-records.

## The problem, with evidence

All figures: `PYTHONHASHSEED=0`, `build_realm`, shipped chooser, no player.

1. **The crisis is the only thing that moves a person's interior in computed play, and it is a fixed
   function of the build.** Three seasons: stored stance moved for 1 and 2 of 83 persons (seeds 0, 1),
   pursuits for 2 and 0 (largest single move 0.027 on a weight), capability and seats for 0;
   `Person.conviction` was rewritten for 6 persons at seed 0 and 7 at seed 1 (`b1_season.py`). The six
   at seed 0 (Sigrid Torsvald, Hedda Kronvald, Inge Baralta, Torben Almqvist, Gerik Strand, Wilhelm
   Voss) are six of the seven at seed 1 (the seventh is Annika Feldhaus), and each of the six lands on
   the same vector at both seeds. `person_q.py:903`: the rule *"ROLLS NOTHING"*.
2. **Its direction inverts the person.** `x1_extremes.py` asks `conviction_after_crisis` of every cast
   person with his held creeds at the threshold, with no play at all: of 46, **31 have their
   highest-held creed replaced by the creed it is incompatible with**, 1 is left holding nothing, 14 are
   unchanged (the unbuilt RESTABILISE branch). Every Einhir adherent at intensity 5 (Yrsa Vossen,
   Lenneth Almqvist, Aldric Hann, Magnus Vaynard, Ingrid Stenskald, Njal Torberg, Carin Vedel) becomes
   Solmund-orthodox at 5; the orthodox at 5 (Gustav Linder, Osten Jarnstal) become Einhir at 5; Arne
   Himlensendt and Sæmund Haelgrund (orthodox 5) become `thread_truth` 5. Cause, as the docstring itself
   records (`person_q.py:932-938`): the shared engagement column scars every co-held creed in one act, so
   all reach the threshold together, the selector takes the HIGHEST-held (`max(crisis, key=held)`), and
   folds it into its incompatible partner, however weakly that partner is held. A man who is orthodox at
   2 and Einhir at 1 ends Einhir at 3: more devout in the rival faith than he ever was in his own.
3. **Its trigger is not about faith.** The affiliation track is violated by three verbs for every creed
   alike (`destroy_record`, `evade / defy`, `forge`; `thread_read` for one creed more): `a0_words.py`. A
   believer converts because three forgeries or defiances happened where he could see them.
4. **It is silent.** `loop/resolve.py:706-708`: *"Nothing is emitted"*. Checked by run: in the cut
   test's `tau0` arm six convictions were rewritten within two seasons and the log holds 0
   `conviction.moved` Events (`d1_cuts.py`, `d1_read.py`). So no ledger holds it, nobody can tell of it,
   and no later act can have it among its causes. The convert himself holds no claim that he converted.
5. **It barely reaches a choice.** Replacing a person's whole `conviction` moves his score-top act in 6
   to 15 of 276 readings (`c1_two_men.py` (a)); redrawing the same person moves it in 61%.

The standing rule (`AUDIT_BRIEF.md`: *"a thing that could go either way for the people in the fiction
goes by a draw"*) applies in full: whether a man's faith survives what he has seen is the type case.

## The resolution, decided

Ladder: steps 1 to 3 are silent on the roll and on the direction (the direction is marked
`[ASSUMPTION; Jordan to correct]` at `person_q.py:912`, the draft's own direction is *"which affiliation
was scarred"*); step 4, precedent: the tree grades every contested outcome on the four bands through
`engine/dice_engine/dice_engine.py::degree_from_net` and writes per band (`row.writes_by_degree`); step
5 decides the rest.

**1. Which creed is in crisis.** Where the act's violation came from a per-affiliation cell, that creed
(the draft's direction, unchanged). Where it came from the shared column and several co-held creeds are
at the threshold together, the creed in crisis is the **lowest-held**, ties to the first by name: under
equal pressure on everything he holds, a man doubts first what he holds least. This reverses
`max(crisis, key=held.__getitem__)` to `min` for the shared-column case and for nothing else.

**2. The roll.** One draw per (person, act), keyed as every fold draw is (`World.new_draw`, the S33
ordinal, at RESOLVE; never the chooser's draw). Pool: the intensity he holds the creed at (the 0 to 5
spine; his faith is his dice). Obstacle: `crisis_obstacle` (new fixture, swept 1 / 2 / 3, shipped 1)
plus one per co-held incompatible creed. Graded by `degree_from_net`. No capability and no attribute
enters until the capability map names one (`02_CHAR_capability_definitions.md` is the door).

**3. What each band writes** (one row of data, `rosters.yaml: tables.crisis_bands`, read by
`conviction_after_crisis`; the function keeps its reader shape and gains a `band` argument):

| band | write | in words |
|---|---|---|
| Overwhelming | intensity +1 (clamped at the ceiling); `scar[x]` reset to 0 | faith renewed: the one outflow the count has |
| Success | nothing; `scar[x]` set to the threshold − 1 | he holds; it will take another wound to test him again |
| Partial | intensity −1 (a creed at 1 goes to a held rejection, 0) | he wavers; recoverable by the Overwhelming band of a later test |
| Failure | today's branch: FOLD into the highest-held incompatible co-held creed, else DESTROYED, else (something compatible is held) intensity −2 floored at 0 | he breaks |

The Failure row's third arm replaces the unbuilt RESTABILISE branch, so no person in crisis is a no-op.
`conviction_map`'s closed spine is kept (ints, clamped), so no rounding rule is needed.

**4. The Event.** `_conviction_crisis` emits `conviction.moved` (the kind the row already declares and
nothing emits), `degree` the band, subject the person, `causes` the act that scarred him, `observed`
the person himself and those in the room (the ordinary WITNESS fan). The docstring's objection (*"an
Event here would deposit claims about every observer at WITNESS"*) is answered by emitting once per
person in crisis, not once per scarred observer: a crisis is rare once the scar is a wound, and it is
the one interior event a chronicle has.

## Exact edits, by owner

| file | edit |
|---|---|
| `engine/season/data/fixtures.py` | `crisis_draw="on"` (swept `off` control / `on`), `crisis_obstacle=1` (swept 1 / 2 / 3), each with its `[ASSUMPTION; medium; Jordan to correct; revert: crisis_draw off]` line and a hole-register row |
| `engine/season/rosters.yaml` | `tables.crisis_bands` (the table above, four rows, each a list of typed writes); the loader in `data/rosters.py` refuses a band off the ladder or a write off the three it knows (`intensity`, `scar`, `branch`) |
| `engine/season/queries/person_q.py::conviction_after_crisis` | signature `(p, among=None, band=None, shared=False) -> (conviction, scar_delta)`; `band=None` is today's function exactly (the control); selector `min` when `shared`; the Failure arm's third case |
| `engine/season/loop/resolve.py::_conviction_crisis` | for each scarred person with a held creed at the threshold: draw, grade, ask the reader, write `conviction` and the scar reset through the gate in one `w.write`, emit `conviction.moved` |
| `engine/season/write_matrix.yaml` | `(Person, conviction)` and `(Person, scar)` rows already admit an act's write at RESOLVE; add `conviction.moved` to the emitting row's `emits:` if the loader requires it listed (it is declared on the row; verify at the row) `[UNVERIFIED]` |
| `engine/season/decision/sheet.py::Chronicle` | nothing: the Event deposits as a claim and the chronicle reads the ledger |

Not edited: `systems/characters/sim/conviction.py` (the retired second scar model; its deletion is the
first audit's).

## Gate (an execution artifact)

`python -m engine.season.harness.decision_spread --season` is not the instrument; the gate is a seeded
run through the season loop, `build_realm`, seeds 0 to 3, three seasons, shipped chooser:

1. `crisis_draw: off` reproduces today's hashes (`5ab73af2`, `bacd687f`, `52ff67bc` at seed 0).
2. `on`: the set of persons whose conviction moved differs between at least two seeds, and at least one
   person in crisis at some seed holds (band Success or better). Today both are false.
3. Of the persons whose highest-held creed changes, the count whose new top creed is one they held at
   less than half their old top's intensity is 0 without a Failure band on the roll.
4. Every conviction write has a `conviction.moved` Event with the scarring act in its `causes`, and the
   person's own ledger holds a claim of it.

## Falsifier

Gate 2 fails if the draw is keyed on state alone (the same persons break at every seed). Gate 3 fails
if the selector still folds the stronger creed. If, with `02_CHAR_scar_is_a_wound.md` landed, no crisis
fires in twelve seed-seasons, this proposal is correct and unobservable: say so and re-measure on a realm
with an inquisition case (ARC cases that turn on apostasy), not by loosening the scar.

## NERS reading (E last)

- **N.** Cut the scar and the crisis entirely (`d1_cuts.py` arm `noscar`, audit §2): at seed 0 not one
  of 1,529 resolved acts differs in two seasons; from season three what dies is 6 or 7 silent,
  pre-determined conversions with a 2 to 5% effect on choice. As built it is a free cut. As proposed it is the one mechanism by which what a person lives through changes
  what he is, and it holds from every direction: bottom-up (a scar count), top-down (a realm's
  confessional map can drift), lateral (a convert is an Event another person's regard and telling can
  read), and across scales (a cohort holds no creed today; when it does, the same roll serves it).
- **R.** The no-player half: apostasy, steadfastness and renewal happen and are recorded with nobody
  watching. Extremes: a creed at intensity 1 rolls one die and usually wavers to rejection; at 5 it
  usually holds; nobody is immune and nobody is doomed.
- **S.** One ladder, the tree's own; the roll is the fold's draw, not a second generator; pool and
  obstacle are composed as every contest's are.
- **E.** One table of four rows and one selector flip, against a rule whose present form needs a
  40-line docstring to explain why it does the opposite of what its source asked.

## Cost class

Small build (one reader's signature, one writer, one table, two fixtures, one Event kind already
declared). Design-first only in the band table's values, which are marked for Jordan.

## For Jordan (not resolved here)

The band table's four writes and the lowest-held selector are this lane's choices at ladder step 5 and
are stated as assumptions. One conflict is named and not resolved: `ED-IN-0261`'s superseding row folds
G-Q6 (*"the engine chooses per case, by a rule over state … and rolls nothing"*) into the build as
RULED; the standing rule of 2026-11-12 forbids a consequential outcome that is a fixed function of
state. Option A: G-Q6 stands, the crisis stays a rule, and only edits 1 (selector) and 4 (the Event)
land. Option B: the standing rule governs and the roll lands. Under A the realm's faith changes on a
schedule set at world-gen; under B it changes by fortune and a player can watch a man hold.
