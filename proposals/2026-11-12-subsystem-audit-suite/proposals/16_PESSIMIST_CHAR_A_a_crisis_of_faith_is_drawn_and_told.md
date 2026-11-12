# CHAR (pessimist) A — a crisis of faith is drawn, keeps its direction, and is told

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-09) — the roll is confirmed by Jordan's answer A-24 (D-26, D-27): Option B; `crisis_arm` ships `drawn`; ED-IN-0261's *rolls nothing* is superseded by that ruling. This file is the emitter of `conviction.moved` (the CORE record proposal emits `scar.taken` only). The draw is the one sampler's (A-5) and its pool follows the one pool rule with the held intensity as the score (U1 architecture §4), so `crisis_obstacle` is set at the calibration, not at 1.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-5/A-6/A-7: the roll's pool,
obstacle and talent rewritten in body item 2; A-30: the ordinal draw replaced by a keyed draw; A-24: "For Jordan"
CLOSED), §1 (the Event names the person only by its receipt, `04` §B.9 `:433`; the draw key, PART D 35), §7/§7b
(tests, gate, tier); U3 C3-K2 (one composed signature, this file first with `reading="any"`), C3-L6 / J-U3-01 (this
file's emitter is the RESOLVE-side step `31_WR_B` commit 1 composes on, dial at zero), C3-Y8, B10; U1 glossary
*conviction*, *stands for*; U1 architecture §3 (a new site `crisis`). Changed: item 2, item 4's wording, the edits
table's reader row and `write_matrix` row (verified at the tree), the gate, the For-Jordan section.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-5a item; `unified/U1_OWNERS_AND_VOCABULARY.md` F-43): the crisis switch is `Fixtures.crisis_arm`, values `rule` (control, today's function) and `drawn` (ships, A-24), where this file said `crisis_draw: off|on`. The test file name `test_crisis_draw.py` and its `test_off_*` function names are unchanged. No prior `crisis_arm` exists in the tree (`engine/season`), so nothing else renames. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "highest-held" → "strongest" (glossary *stands for*: "held" is above the mid-point).

Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A92`, `unified/work/L1_PROPAGATION.md`): the "until Jordan answers J-U3-01" clause of the consumers line is rewritten: J-U3-01 is A-92, its `04` §B.2 / row 18 text is applied (`04:251`, `:1044`), and `sway_gain` at 0 now waits on the calibration batch only (`unified/DECISIONS_ANSWERED.md` A-92: "the dial ships at zero until the calibration batch sets it"). The "For Jordan" heading's "superseding ledger row is owed" (`ED-IN-0261`) is likewise rewritten to the applied state, node `L1-A24`. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (1); "talent" → attribute or governing attribute (2); rewordings by sense (1: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

## Status: PROPOSED

Lands in batch: **B10** (IN/CHAR; one re-pin when `crisis_arm` is `drawn`). Depends on: `engine/dice_engine/draw.py`
and the A-30 key function (`16_PESSIMIST_GO_keyed_draw_no_recorder.md` with `11_GO_one_draw_owner.md`, B06);
`seam/wrappers/pool.py` / `sigma_leverage.pool_of` (U1 architecture §11 batch U1-B, B05); `02_CHAR_capability_definitions.md`
(B04); `02_CHAR_scar_cap_and_regard_unit.md` and `02_CHAR_scar_is_a_wound.md` (B10, land before this);
`16_PESSIMIST_CORE_the_record_holds_what_changed.md` (B09, emits `scar.taken` only). Consumers that compose on this
file: `20_NARRATIVE_A_stands_for.md` edit 4b (passes `reading="stands"`, B38), `20_NARRATIVE_E` (its edit 3 is struck in
favour of this), `31_WR_B_the_revival_gathers.md` commit 1 (the sway is a drawn term at this RESOLVE-side step, its dial
`sway_gain` at 0 until the calibration batch sets it; J-U3-01 is ANSWERED as A-92 (Option 1) and its Layer 1 text is APPLIED, 2026-11-12, A-97, node `L1-A92`: `04:251`, PART D row 18 `:1044`, so the sway conforms; the dial waits on calibration alone and on no amendment).

**Words.** *Conviction* is the affiliation-intensity map on `Person` (DR `affiliation_roster`); a *creed* in this
file is one affiliation of that map, never the map. "Highest/lowest-intensity" replaces the earlier
"highest/lowest-held" (U1 glossary: *held* in the old sense means "stored above zero").

Written by the CHAR pessimist lane (`audits/16_PESSIMIST_CHAR.md`, F-PES-CHAR-03). Ratifies nothing;
reference under `CLAUDE.md` §0.05. It amends, and does not replace, `02_CHAR_scar_is_a_wound.md` (which
bounds how a scar count is reached) and `02_CHAR_scar_cap_and_regard_unit.md` item 1 (the rate): those
decide WHEN a crisis is reached; this decides WHAT a crisis does.

## What this changes in `engine/season/` at runtime

`queries/person_q.py::conviction_after_crisis` stops being a fixed function of `(conviction, scar)`.
`loop/resolve.py::_conviction_crisis` rolls one draw per person in crisis, grades it on the four-band
ladder, writes the band's result, and emits one Event that WITNESS deposits for the person himself and
for those present. With the new fixture `crisis_arm` at its control (`rule`) the function is today's and
the hash is EQUAL. Shipped `on` it is a declared mover: every run in which a crisis fires re-records.

## The problem, with evidence

All figures: `PYTHONHASHSEED=0`, `build_realm`, shipped chooser, no player.

1. **The crisis is the only thing that moves a person's interior in computed play, and it is a fixed
   function of the build.** Three seasons: stored stance moved for 1 and 2 of 83 persons (seeds 0, 1),
   pursuits for 2 and 0 (largest single move 0.027 on a weight), skill and seats for 0;
   `Person.conviction` was rewritten for 6 persons at seed 0 and 7 at seed 1 (`b1_season.py`). The six
   at seed 0 (Sigrid Torsvald, Hedda Kronvald, Inge Baralta, Torben Almqvist, Gerik Strand, Wilhelm
   Voss) are six of the seven at seed 1 (the seventh is Annika Feldhaus), and each of the six lands on
   the same vector at both seeds. `person_q.py:903`: the rule *"ROLLS NOTHING"*.
2. **Its direction inverts the person.** `x1_extremes.py` asks `conviction_after_crisis` of every cast
   person with his held creeds at the threshold, with no play at all: of 46, **31 have their
   strongest creed replaced by the creed it is incompatible with**, 1 is left holding nothing, 14 are
   unchanged (the unbuilt RESTABILISE branch). Every Einhir adherent at intensity 5 (Yrsa Vossen,
   Lenneth Almqvist, Aldric Hann, Magnus Vaynard, Ingrid Stenskald, Njal Torberg, Carin Vedel) becomes
   Solmund-orthodox at 5; the orthodox at 5 (Gustav Linder, Osten Jarnstal) become Einhir at 5; Arne
   Himlensendt and Sæmund Haelgrund (orthodox 5) become `thread_truth` 5. Cause, as the docstring itself
   records (`person_q.py:932-938`): the shared engagement column scars every co-held creed in one act, so
   all reach the threshold together, the selector takes the STRONGEST (`max(crisis, key=held)`), and
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
at the threshold together, the creed in crisis is the **lowest-intensity**, ties to the first by name: under
equal pressure on everything he holds, a man doubts first what he holds least. This reverses
`max(crisis, key=held.__getitem__)` to `min` for the shared-column case and for nothing else.

**2. The roll.** One draw per (person, scarring act), keyed `H(seed, tick, person, "crisis:" + act.id)`
through the A-30 key function (`04` PART D 35: `H(seed, tick, subject, purpose)`, no counter; the copy of
`16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` item 4's purpose key). Not `World.new_draw`: that is the S33
ordinal (`state/world.py:1632-1635`, reset every tick), the counter A-30 retires; and not the chooser's draw.
The act id is in the purpose so two crises of one person in one tick have two keys. The roll is composed as
every roll is (U1 architecture §4; A-5, A-6, A-7):
- **Pool** (the dice input): `sigma_leverage.pool_of(score = intensity of the creed, addends = (), pool_add,
  pool_floor)`, i.e. `max(pool_floor, intensity + pool_add)`, through the one pool rule
  (`seam/wrappers/pool.py`); the held intensity is the score (A-6).
- **Governing attribute** (A-7): a `capability_uses` row `{use: crisis, role: edge, key: attr.mind.will, side: roller,
  per: mid}`, read by the one `edge` reader; `crisis` is added to `capability_use_sites` with
  `_conviction_crisis`'s input builder as its reader (U1 architecture §3, "a new site is a new reader and a
  new map member"). `[ASSUMPTION; medium: will governs faith — basis: `descriptor_registry.yaml` lists
  `attr.mind.will`; the CHAR content pass may substitute; revert: no attribute row]`.
- **Obstacle**: the fixture `crisis_obstacle` (a difficulty level; **no shipped literal**: its value is set by
  the joint calibration of A-5, A-6, A-7 and A-26, `13_SC_calibration.md` being the instrument) plus one per
  co-held incompatible creed (a hostile term, A-25).
- **Draw and grade**: `roll_net_continuous(pool) + net_boost(levels, pool)` against the obstacle, graded by
  `degree_from_net` (A-5; the margin quantised at the ladder, C3-L1).

**3. What each band writes** (one row of data, `rosters.yaml: tables.crisis_bands`, read by
`conviction_after_crisis`; the function keeps its reader shape and gains a `band` argument):

| band | write | in words |
|---|---|---|
| Overwhelming | intensity +1 (clamped at the ceiling); `scar[x]` reset to 0 | faith renewed: the one outflow the count has |
| Success | nothing; `scar[x]` set to the threshold − 1 | he holds; it will take another wound to test him again |
| Partial | intensity −1 (a creed at 1 goes to a held rejection, 0) | he wavers; recoverable by the Overwhelming band of a later test |
| Failure | today's branch: FOLD into the highest-intensity incompatible co-held creed, else DESTROYED, else (something compatible is held) intensity −2 floored at 0 | he breaks |

The Failure row's third arm replaces the unbuilt RESTABILISE branch, so no person in crisis is a no-op.
`conviction_map`'s closed spine is kept (ints, clamped), so no rounding rule is needed.

**4. The Event.** `_conviction_crisis` emits `conviction.moved` (the kind the row already declares and
nothing emits), `degree` the band, `causes` the act that scarred him, and in `changes[]` the receipt of
`(Person, conviction)` for that person minted by the gate: that receipt is how the Event names him, since an
`Event` has no `actor`, `target` or `subject` field (`04` §B.9 `:433`, STRUCTURAL). Who learns of it is
WITNESS's ordinary co-located fan (the person himself and those in the room), not a field the emitter
sets. The docstring's objection (*"an
Event here would deposit claims about every observer at WITNESS"*) is answered by emitting once per
person in crisis, not once per scarred observer: a crisis is rare once the scar is a wound, and it is
the one interior event a chronicle has.

## Exact edits, by owner

| file | edit |
|---|---|
| `engine/season/data/fixtures.py` | `crisis_arm="drawn"` (swept `rule` control / `drawn`, A-24 ships `drawn`; U1 F-43's name and values), `crisis_obstacle=<calibration>` (a difficulty level, no shipped literal), each with its `[ASSUMPTION; medium; Jordan to correct; revert: crisis_arm rule]` line and a hole-register row (id from `references/id_reservations.yaml` `next_free` at build) |
| `engine/season/rosters.yaml` | `tables.crisis_bands` (the table above, four rows, each a list of typed writes); the loader in `data/rosters.py` refuses a band off the ladder or a write off the three it knows (`intensity`, `scar`, `branch`); `capability_use_sites` gains `crisis`; `tables.capability_uses` gains the `edge` row of item 2 |
| `engine/season/queries/person_q.py::conviction_after_crisis` | one composed signature (C3-K2): `(p, among=None, band=None, shared=False, reading="any") -> (conviction, scar_delta)`; `band=None` is today's function exactly (the control); selector `min` when `shared`; the Failure arm's third case. `reading="any"` is the value at which `held_reading` is hash-equal; `20_NARRATIVE_A_stands_for.md` edit 4b later passes `"stands"`, so the Failure arm's fold candidates become the creeds the person stands for |
| `engine/season/loop/resolve.py::_conviction_crisis` | for each scarred person with a creed at the threshold: draw (item 2's key), grade, ask the reader, write `conviction` and the scar reset through the gate in one `w.write`, emit `conviction.moved` |
| `engine/season/write_matrix.yaml` | no edit: verified 2026-11-12, the `(Person, conviction)` row already declares `emits: "`conviction.moved`"` and is written by `_conviction_crisis` at the fold; `(Person, scar)` declares `scar.taken` (emitted by the CORE record proposal) |
| `engine/season/decision/sheet.py::Chronicle` | nothing: the Event deposits as a claim and the chronicle reads the ledger |

Not edited: `systems/characters/sim/conviction.py` (the retired second scar model; its deletion is the
first audit's).

## Gate (an execution artifact)

The figures in "The problem" came from lane scratch (`x1_extremes.py`, `a0_words.py`, `b1_season.py`,
`c1_two_men.py`, `d1_cuts.py`, `d1_read.py`; not in the repository, U3 §6.2). The batch writes, first:
NEW `engine/season/tests/test_crisis_draw.py`: `test_off_reproduces_conviction_after_crisis` (gate 1),
`test_lowest_intensity_creed_is_the_one_in_crisis_for_shared_column` (gate 3),
`test_every_conviction_write_has_a_conviction_moved_event_with_the_scarring_act_in_causes` (gate 4, the
receipt names the person), `test_two_seeds_move_different_persons` (gate 2),
`test_two_crises_of_one_person_in_one_tick_have_two_keys`. Command:
`python -m pytest engine/season/tests/test_crisis_draw.py -q`; then the seeded run below through
`python -m engine.season.harness.headless --seasons 3 --seed N` for N in 0..3, and `report` / `delta HEAD`.

`python -m engine.season.harness.decision_spread --season` is not the instrument; the gate is a seeded
run through the season loop, `build_realm`, seeds 0 to 3, three seasons, shipped chooser:

1. `crisis_arm: rule` reproduces today's hashes (`5ab73af2`, `bacd687f`, `52ff67bc` at seed 0).
2. `on`: the set of persons whose conviction moved differs between at least two seeds, and at least one
   person in crisis at some seed holds (band Success or better). Today both are false.
3. Of the persons whose highest-intensity creed changes, the count whose new top creed is one they held at
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
  watching. Extremes: a creed at intensity 1 rolls the floor pool (A-6) and wavers more often; at 5 it
  usually holds; nobody is immune and nobody is doomed (the band shares are re-read at the calibration,
  not stated here).
- **S.** One ladder, the tree's own; the roll is the fold's draw, not a second generator; pool and
  obstacle are composed as every contest's are.
- **E.** One table of four rows and one selector flip, against a rule whose present form needs a
  40-line docstring to explain why it does the opposite of what its source asked.

## Cost class

Small build (one reader's signature, one writer, one table, two fixtures, one Event kind already
declared). Design-first only in the band table's values, which are marked for Jordan. Hash movers
declared: none at `crisis_arm: rule`; every run in which a crisis fires, at `drawn` (one re-pin at B10's
close). Tier: `opus` for the band table and the `will` assignment (the judgment nodes), then `sonnet`, effort
`high`, for the edits and tests. Lands it: B10, after the scar proposals and before `_CHAR_B`, `_CHAR_C`
(U3 §1 item 11). Order of edits: fixtures at the control → roster table and site → reader signature →
emitter with the Event → `crisis_arm: drawn` in its own commit.

## For Jordan (CLOSED by A-24, 2026-11-12: Option B taken, the roll lands and `crisis_arm` ships `drawn`; ED-IN-0261's "rolls nothing" is superseded, its superseding ledger row is written, 2026-11-12, A-97, node `L1-A24`: `ED-IN-0261` in `registers/editorial_ledger_in.jsonl`. Kept as the finding.)

The band table's four writes and the lowest-intensity selector are this lane's choices at ladder step 5 and
are stated as assumptions. One conflict is named and not resolved: `ED-IN-0261`'s superseding row folds
G-Q6 (*"the engine chooses per case, by a rule over state … and rolls nothing"*) into the build as
RULED; the standing rule of 2026-11-12 forbids a consequential outcome that is a fixed function of
state. Option A: G-Q6 stands, the crisis stays a rule, and only edits 1 (selector) and 4 (the Event)
land. Option B: the standing rule governs and the roll lands. Under A the realm's faith changes on a
schedule set at world-gen; under B it changes by fortune and a player can watch a man hold.
