# WR — the road is drawn: a journey takes its distance in time and can go wrong

Reconciled: 2026-11-12, U5d closure — folded **A-54** and **A-5**: the road's draw is on the one ladder with the one sampler, as written; no step changes. A march's passage is not this file's (an army's arrival is the field's end state); a march into another's held territory is aggression by A-58; a win leaves the marcher standing there to seize, occupy or withdraw (A-66), and a draw returns him to his station (A-67).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-5, A-6, A-7: `road_base = 2` and
integer border counts were a whole-dice obstacle; the obstacle is the task composer's form of U1 architecture §4, with
`road_base` a difficulty level set by the joint calibration and the borders, the weather and a war as named terms of the
same obstacle), §1 (CONFORMS; the module home decided), §7/§7b (test file and names, tier); A-30 (the draw is keyed
`H(seed, tick, pid, "road:<leg>")`); A-54 (the weather term reads the band of the season's draw, not "the lowest outcome
of its table"); U3 B12, C3-D6, §6.1 (`test_travel.py` does not exist: written as the batch's first commit), §6.2
(`p2_play.py` is not in the repository); STAGES.md (CP-T10-02 is a v11 card; the home is decided here for the v12 card).
Changed: the obstacle bullet, edit 1's `road_base`, edit 3's home, the gate and the falsifier's form. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (1).

## Status: PROPOSED

Lands in batch: **B12** (WR), after `16_PESSIMIST_GAME_the_world_draws.md` and `U5d_WR_owed_edits.md` §2 (a), §3, §4
(C3-D6). Depends on: `07_SE_kernel_repairs.md` §4 (R-SE-09, the same-place decline) and
`09_WR_B_weather_with_memory_and_the_year.md` edit 3 (`leg_price`) and edit 1 (the season's band), both B12;
`engine/dice_engine/draw.py` (B06).

Source: `audits/16_PESSIMIST_WR.md` §2.3, F-PES-WR-06. Read at `d161a61`. Reference only (`CLAUDE.md`
§0.05). Lane WR (the owner is `loop/matter.py`'s travel pass and `loop/effects_migration.py::_relocate`).
It decides the shape of plan position **CP-T10-02** (B10-18, held), which
`09_WR_B_weather_with_memory_and_the_year.md` edit 3 lists "for its owner as a draw" and does not write.

Not in this proposal, because another file carries it: the same-place decline of `move`
(`07_SE_kernel_repairs.md` §4, R-SE-09); the price the chooser sees before choosing
(`09_WR_B_weather_with_memory_and_the_year.md` edit 3, `leg_price`). This proposal depends on both: a
journey that goes nowhere must not draw, and the draw's distance term is `leg_price`'s.

## What it changes in `engine/season/` at runtime

One fixture, `road_hazard`, with a control arm (`off`) at which every base hash is reproduced. On: at
MATTER's travel pass, each traveller whose leg crossed at least one territory border takes **one draw on
the one ladder**, and the degree decides how he arrives. Nothing else moves.

## The problem, with evidence

"A journey is dangerous" is false in the running game (`runs/PES_WR/p2_s0_k3_shipped.txt`,
`p2_s0_k3_drawseed.txt`, `p2_s1_k3_shipped.txt`; three seasons each):

- no traveller was harmed: 0 of 10, 0 of 12 and 0 of 11 individuals who travelled (control: 0 of 36, 0 of
  34 and 1 of 35 who did not, the one a man killed in a `capture`);
- arrival is in the round of the act: one person made three journeys in one season at seed 0;
- the price is one scene per leg whatever the distance (`decision/budget.py:60`), so the 14 crossings of
  a territory border at seed 0 cost what a move inside a building cost;
- `Person.travel_leg` has one reader, the budget, and MATTER's travel pass (`loop/matter.py:831-843`)
  only empties it: no draw is taken and no state of the road is read.

A fixed charge would not repair this under the standing rule (`AUDIT_BRIEF.md`: *a thing that could go
either way for the people in the fiction goes by a draw*). Whether a traveller arrives whole is such a
thing.

## The resolution, decided

Ladder step 4, precedent: MATTER already calls pure module entries by composition row
(`STEP_CALLS = ((SUBSIST, "step_call"), (PRODUCE, "step_call"))`, `loop/matter.py:45-47`) and already
takes one keyed draw per living person in the bodies pass (`draw_factory`, `:727-731`). The road is the
same shape: the host projects a typed input, a pure entry returns a typed outcome, the host writes
through the gate at cells the write matrix already licenses for MATTER (`(Person, body)` `[MAT, RES]`,
`(Person, travel_leg)` `[MAT, RES]`).

**State sets the odds; the draw sets the outcome.**

- *Pool:* `seam/wrappers/pool.py::faculty(w, traveller, "move")`, the one owner of a person's pool for a
  verb (`pool_of(score, addends, pool_add, pool_floor)`, A-6; so a skill a designer attaches to `move`
  is read here with no engine edit).
- *Obstacle:* composed as every task obstacle is (U1 architecture §4: the even line, the difficulty, the
  stand-in for nobody opposite), with `road_base` the difficulty (a `difficulty_levels` member, its size set
  by the joint calibration of A-5/A-6/A-7, not 2), and three named hostile terms (A-25): the leg's border
  count (`leg_price`'s distance, the one owner), one step for each crossed territory whose season draw this
  tick landed Failure (bad weather, A-54; none while the weather arm ships at its control), and one step for
  each crossed territory in which a field was fought this tick or the last (`field.lost` / `field.won` placed
  there: a war on the road). The step's size is one fixture, `road_step_ob`, set with `road_base` at the
  calibration.
- *Draw:* keyed `H(seed, tick, pid, "road:<leg index>")` through the one keyed-draw owner (A-30), carried on the
  typed input as `draw_key`.
- *Degree:* `engine/dice_engine/dice_engine.py::degree_from_net` through `seam/ladder.py::degree_of`, the
  single ladder.

| degree | how he arrives | write |
|---|---|---|
| Overwhelming | on time, and with news: he holds a firsthand Observation of the stock of the place he passed (`stores:<kind>`, CR-23's predicate) | `travel.ended` with `observed=` |
| Success | on time | `travel.ended` (today's write) |
| Partial | **spent**: the leg is not emptied this barrier, so the budget penalty stands another season (he is a scene short in the season after the journey) | no write; one `travel.delayed` Event, causes the `travel.moved` |
| Failure | arrives, **hurt**: his body falls by `road_step` (fixture), through the body write and `_crossings`, as a hunger fall does | `body.changed` (cause: the `travel.moved`), then `travel.ended` |

Death is not an outcome of this table. A body that reaches zero dies through `_die`, the one owner, as it
does for hunger; so a journey kills only a traveller who set out already at the edge, which is the
recoverable shape the rule asks for (`tend` raises him; a wounded man can choose not to travel).

**Time.** A journey of more than one border takes more than one season: `_relocate` appends one leg per
border crossed (it appends one per act today), and MATTER ends **one leg a barrier** instead of all of
them. The traveller's `contain` edge moves at the act, as now (presence is ratified as the `contain` edge:
`effects_migration.py:140-145`); what the remaining legs hold back is his budget, which is the price
`leg_price` shows the chooser. No new carrier: `travel_leg` is already a list.

## The edits

1. **`engine/season/data/fixtures.py`** — `road_hazard="off"` (swept `off` / `on`), `road_base=<a
   difficulty level, calibration>`, `road_step_ob=<calibration>`, `road_step=100` (the body fall; one body
   band is 300 wide at `band_floors.body`; a third of a band), each `[ASSUMPTION; medium; Jordan to correct;
   revert: road_hazard = off]`, each with a hole-register row as `body_step` has (H-125's shape; ids from
   `references/id_reservations.yaml` `next_free`).
2. **`engine/season/queries/inputs.py`** — `RoadInput(travellers: tuple)`, each
   `(pid, pool: int, obstacle: float, draw_key: str)` (the obstacle a declared float, A-29);
   `RoadOutcome(rows: tuple)`, each `(pid, degree)`. No `World` crosses.
3. **The module entry** — `exposure(inp: RoadInput) -> RoadOutcome`, pure, rolling through the module's
   own roll owner as `modules/fieldwork/find.py` does; home `modules/settlements/exposure.py` (the module
   MATTER already calls twice; decided here for the v12 card of CP-T10-02, whose v11 text names no home)
   `[ASSUMPTION: settlements is the right module family for a travel hazard — basis: this file's own
   fallback; revert: a `modules/travel/` package if the v12 card says so]`. One `composition_roles:` row in
   `references/module_contracts.yaml` (`settlements.exposure`, kind `step_call`) and one tuple in
   `loop/matter.py::STEP_CALLS`, so `registrar.require_entries` refuses a missing row at construction.
4. **`engine/season/queries/world_q.py`** — `road_input(w)`: the travellers with a non-empty
   `travel_leg` whose last leg crossed a border, their `faculty`, their obstacle by the rule above.
5. **`engine/season/loop/matter.py`, the travel pass** — with `road_hazard` on: call the entry once;
   per traveller, by degree, the writes of the table; the leg list loses its first entry instead of
   being cleared. With it off: today's loop, byte for byte.
6. **`engine/season/loop/effects_migration.py::_relocate`** — appends `leg_price(origin, dest)` entries
   (the intermediate territory ids on the route) instead of `[dest]`; one entry where the price is one,
   which is today's.
7. **`engine/season/write_matrix.yaml`** — `(Person, travel_leg)`'s MAT row gains the kind
   `travel.delayed`; `(Person, body)`'s MAT emission is unchanged.

## The gate that shows it worked

NEW `engine/season/tests/test_travel.py` (no such file exists; `test_migrate_capacity.py` and `test_march.py` reference
`travel_leg`; written as the batch's first commit, U3 §6.1): `test_road_degrees_not_all_equal_over_forty_journeys`,
`test_four_borders_fail_more_than_one`, `test_road_hazard_off_hash_equal`, `test_hurt_traveller_is_tended_in_some_seed`,
`test_one_leg_ends_per_barrier`. Command: `python -m pytest engine/season/tests/test_travel.py -q`. On `build_realm`:

- with `road_hazard` on and forty hand-built journeys of three borders by one person kind (PROXY), the
  degrees **are not all equal**, at least one traveller arrives spent and at least one arrives hurt, and
  the count of each differs between two seeds; the loop asserts it read at least forty;
- a journey of one border and a journey of four differ in their share of Failure in the expected
  direction over those forty (state sets the odds);
- with `road_hazard = off` the season's hash is the base hash (the control);
- a traveller hurt on the road is `tend`ed in a later season in at least one seed (the outcome is
  recoverable in play, not only on paper).

## The falsifier

The scratch `runs/PES_WR/p2_play.py SEED 3 shipped` (not in the repository) printed
`individuals who travelled N, harmed 0` at every seed and `max moves by one person in one season 3`; after the
change, with `road_hazard` on, a three-season realm run at seeds 0-2 read through `harness/aperture.py`'s per-person
census must show neither for journeys that cross borders. If it does with `road_hazard` on, the draw is not reached by computed play
and the fault is upstream (the chooser forms no cross-border `move`).

## NERS reading

- **N.** Cut it and a journey is a change of address again: nothing in the game distinguishes a court
  that is near from one that is far, so position, the map and every "send someone" decision are free.
  From the other directions: bottom-up (the leg list, the keyed draw and the body cell exist), lateral
  (the budget penalty is already the journey's price and `leg_price` scales it; the hazard is the half of
  the price that is not known in advance), diagonal (a messenger who arrives late is how news can be stale, which the knowledge model
  needs and cannot get from instant travel), vertical (a wounded traveller is an occasion for `tend` at
  the personal scale from a decision made at the strategic one).
- **R.** The no-player half: spent and hurt arrivals happen to NPCs with nobody watching and leave Events
  a narrator can read (`travel.delayed`, a `body.changed` whose cause is a `travel.moved`). Completeness:
  a journey of zero borders draws nothing; a traveller at body zero is `_die`'s.
- **S.** One ladder; one pool owner; the same body write hunger uses; the leg ends where it ends today.
  *Pauses correctly:* a journey of several borders is still in progress at the next barrier, which is a
  state the playable host can show.
- **E** (last, against the above): three fixtures, one typed pair, one pure entry, one changed loop. The
  player can intuit it from one sentence: *far, in bad weather, through a war, is dangerous*.

## Cost class

Small build (design decided here; a declared hash mover when `road_hazard` flips, its own commit). Tier: `opus` for
the calibration of `road_base` and `road_step_ob`, `sonnet`, effort `high`, for the code. Lands it: B12, order the
typed pair and the module entry with its composition row (hash-equal) → `road_input` → `_relocate`'s legs → the travel
pass behind `road_hazard` off → the flip in its own commit.
