# Mass battle: troop floor, troops per weight, typical army size, cells, and the cell-to-cell refill

## Status: PROPOSED 2026-11-20 (not ratified; reference only, CLAUDE.md §0.05). Prepared mid-close of batch B17-mb-scale at Jordan's request. Nothing here is built. ED-MB-0101 is the ruling it answers.

## 0. What is ruled, and what is open

Ruled (Jordan, 2026-11-20, `registers/editorial_ledger_mb.jsonl` ED-MB-0101), verbatim:
- "i expect armies to be a minimum of 1000 troops"
- "cells can hold 50-100 troops each. a unit is a minimum of 4 cells. this means that the minimum number of units for an army would be 3."
- "i want the battles to typically be between armies with like 5000 to 10000 troops"

Open, in the order this file takes them: (1) what the floor does when a side falls below it; (2) the troops-per-weight constant; (3) what makes a typical army 5,000 to 10,000; (4) the cell band, which two of your rulings cannot both meet for horse; (5) how many troops may move between cells per tick, and what that does to the unit minimum.

## 1. The chain, as built at B17.16 (read from the tree; every number can be re-run)

| step | rule | owner |
|---|---|---|
| weight to troops | `floor(weight x TROOPS_PER_WEIGHT x MUSTER_FRACTION)` = weight x 10,000 x 0.10 = 1,000 a weight | `troop_types/recruitment.py::under_arms_cap` |
| troops to units | fewest equal units none over `MAX_TROOPS_PER_UNIT` (10,000); a side at 1,000 troops or more is at least `MIN_UNITS_PER_ARMY` (3) units; at most `UNIT_CAP` (11) units | `massbattle._unit_counts`, `_cut` |
| units to cells | a unit of at least 200 troops has at least 4 cells; per-cell 50 to `cell_cap` (100 foot, 50 horse) | `geometry.footprint_for`, `config.cell_cap_for` |
| cells to loss | casualties are applied to cells; then `Unit.close_ranks` re-packs the living troops toward each cell's spawn density, front rank first, rear cells emptying first | `hierarchy/units.py:903`, called each tick at `battle_loop.py:357` |
| unit to rout | a unit under `UNIT_ROUT_FLOOR` (80) troops routs | `battle_loop.py:414`, `config.py:224` |

Largest side: 11 units x 10,000 = 110,000 troops (weight 11 at today's constant is 11,000; the ceiling is reached at weight 110).

## 2. What the realm produces today (measured, one season, seeds 0 to 11)

- Every person in the cast (46) is weight 1. Cohorts (`engine/season/cohorts.yaml`): 39 at weight 2, 1 at weight 4. A cohort is "a Person at `weight > 1`" standing for a populated place's people; a weight-1 person is a named individual.
- Of 29 (faction, place) sides with anyone mustered: 23 weigh 1, 3 weigh 2, 1 weighs 3, 1 weighs 5, 1 weighs 6 (the Church's six at `set_s_036`).
- At 1,000 troops a weight that is: typical side 1,000 (the floor itself), heaviest 6,000. Fields the realm reaches fold 1,000 against 2,000 to 5,000 (seeds 3, 4, 7, 9, 10); seeds 0 to 2 fold none.
- The army verbs (`ARMY_VERBS`) and `marshal` are in the shipped `withheld_verbs` (`engine/season/data/fixtures.py:1085`), and the aperture reading lists `army.formed`, `army.assigned` among the kinds never emitted. So a realm field is a headcount field of persons; nothing in the season builds an army out of cohorts.

Consequence: today a typical side equals the floor. The 5,000 to 10,000 band is reached by no realm field.

## 3. Proposals

### P1. The troops floor (1,000)

What exists: a form-time advisory only (`armyrecord.options`: `army_units`, `army_troops`, `army_routs`). `resolve_field` fights what it is given; it refuses only a unit over the ceiling, an army over `UNIT_CAP` units, and the no-party case (both sides at the one-man crash floor).

| option | effect | cost |
|---|---|---|
| **A. Warn, do not refuse (today)** | a thin garrison can still be attacked and defend; the warning is the player's information | the ruling is advice, not a rule; a side of 300 is fought as a battle |
| B. Refuse a field with both sides under the floor (a "skirmish", not a battle) | closes the gap the 1,000 ruling names | the realm's lone weight-1 person-against-person fields would refuse if a person were under 1,000; at 1,000 a weight they pass |
| C. Raise a side to the floor | none: it invents troops | rejected: it makes troops from nothing |

Recommend A for now. B only if a measured reading shows sub-floor fields reaching `march`; at 1,000 a weight none do. (Basis: this section's sources; not run.)

### P2. Troops per weight

Weights present: 1, 2, 3, 4, 6. Troops a side raises under each option:

| option | weight 1 | weight 2 | weight 4 | weight 6 | holds the floor | reaches 5,000 to 10,000 |
|---|---|---|---|---|---|---|
| **F. Floor sets it: 10,000 a weight (today)** | 1,000 | 2,000 | 4,000 | 6,000 | at weight 1 exactly | only at weight 5 to 10 |
| T. Typical sets it, linear: 50,000 a weight | 5,000 | 10,000 | 20,000 | 30,000 | far above | at weight 1 to 2; weight 6 is 30,000 |
| S. Sublinear: 5,000 x sqrt(weight) | 5,000 | 7,071 | 10,000 | 12,247 | above | at every present weight |
| H. Floor sets it, and the typical size comes from content (below) | as F | as F | as F | as F | exactly | by composition: 3 to 5 cohorts |

- F honours "minimum 1,000" as written: the smallest populated unit of weight raises the floor.
- T and S satisfy the band by the constant, so they stop the floor from meaning anything (every place above 5,000). T makes a weight-6 side 30,000: well over the typical band. S breaks additivity (two weight-1 people at one place sum to 7,071, not 10,000) and `_eff_march`'s per-person share assumes the linear form; I have not tested what S moves.
- H needs no change to the constant. A cohort is 2,000 troops under F; an army of 3 to 5 cohorts is 6,000 to 10,000, which is the ruled typical size, reached by assembly. It needs the withheld army verbs to run in the season, which is not B17's work.

Recommend F plus H: keep 10,000 a weight, and treat the band as what assembled armies reach, not what one place raises. The question for you is the one B17.99 carries: does the floor or the typical size set the constant? If you want the constant to do both, S is the only candidate here that does, at the price of additivity.

### P3. Typical army size (5,000 to 10,000)

State it as a calibration target for composition, not a rule: a typical field is two armies of 5,000 to 10,000, so 10,000 to 20,000 troops in the field. At 3 to 10 units a side that is 50 to 200 cells a side on a 51 x 51 field (2,601 cells), where one army at the extreme 11 x 10,000 would be 1,100 to 2,200 cells.

| option | meaning |
|---|---|
| **A. A reading** (today, B17.13) | the realm's sides are measured against the band; nothing enforces it |
| B. A content target | cohort sizes and muster caps are authored so assembled armies land in the band; checked by `aperture` once armies form |
| C. A refusal | a field outside the band is refused: rejected, since a garrison fight below it is legitimate |

Recommend A now, B when the army verbs ship. A third reading to take then: the share of realm fields whose both sides are inside the band.

### P4. Cells per troop (50 to 100, unit at least 4 cells)

Arithmetic at the ruled band: a unit of t troops has between ceil(t/100) and floor(t/50) cells (never under 4 for t of 200 or more). 1,667 troops (a third of a 5,000 side): 17 to 33 cells. 3,333 (a third of 10,000): 34 to 66. Lightest allowed unit 200 troops; heaviest 10,000 (100 to 200 cells).

The conflict (observed, `geometry.py:123-127`): horse rows carry `cell_cap: 50` (P-DEC-3, "a horse and rider take more ground"), and 50 is also `CELL_FLOOR`. A horse unit whose troops are not a multiple of 50 starts under 50 a cell: 333 troops give 7 cells of 47.6; 201 give 5 of 40.2 (reproduced by running `footprint_for`).

| option | effect |
|---|---|
| **A. Horse cap 75** | horse band 50 to 75 satisfies both rulings (333 troops: 6 cells of 55.5); 75 is an invented value, flagged assumption; it moves every mounted unit's footprint and the golden modes that field horse |
| B. Floor yields for horse | horse cells 25 to 50; the 50 to 100 ruling is true of foot only; no number invented; the cell-band test says so |
| C. Round horse units to multiples of 50 | cap 50 and floor 50 both hold; the muster and `_cut` round each person's horse troops, and the lost troops are unaccounted |
| D. Horse cap 100, with each horse cell counting two grid cells | one density, a doubled footprint; changes frontage and contact geometry |

Recommend A: it is the only option that keeps both rulings literal. Its 75 is a calibration, so it needs your word or a measurement, which I have not taken.

### P5. Replenishing cells, and what it implies for the unit minimum

What the mechanism is (read, `hierarchy/units.py:903-940`): after each tick's casualties, the unit's living troops are re-packed, front rank first, each cell filled to its spawn density (`_cell_target`) until the troops run out; the rearmost cells empty first. It conserves troops, it has no rate limit (a cell can receive any amount in one tick), and it does not remove emptied cells ("literal cell dissolution ... is a later increment"). Jordan's directive (ED-MB-0028): "as cells lose troops, unengaged troops from other cells fill them in to keep engaged cells at prescribed density; coverage shrinks as minimums aren't met".

Measured at the ruled scale (`scratchpad/refill_probe.py`, one seed, 5 weight v 5 weight, each side 3 units of 1,667 troops in 17 cells at 98 a cell; run once, so a single reading and not a distribution):
- Tick 1, no contact loss; from tick 2 the two sides together lose about 70 to 80 troops a tick, then 220 to 230 from tick 5 to 12 (roughly 110 a side, 2.2% of a 5,000 side a tick).
- The reflow moves about as many troops as the tick's loss (221 to 227 a tick from tick 5), because it refills the front from the rear by exactly what was lost.
- Front cells stay at 98 throughout. The thinnest live cell falls from 98 (tick 1) to 47.6 (tick 4), 24.3 (tick 5), 3.0 (tick 8), 2.5 (tick 12): the rear thins below the 50 floor long before the unit is gone, since the cell set does not shrink.
- The battle ended at tick 13.

What follows from the ruled numbers:
1. The 50-to-100 band is a start-of-battle band (the ruling says "at its start", and the engine does not enforce it later). As losses mount, the rear holds cells of a few troops while the front holds 98.
2. A unit under 200 troops cannot be 4 cells of 50. Its routing floor is 80. So between 80 and 200 a unit exists that the ruling says is below the minimum and the engine still fights.
3. The refill rate is unbounded, so depth is the only brake on the front thinning: a 4-cell unit that is one rank deep has nothing behind it and thins at once.

| option | effect |
|---|---|
| **A. Leave the refill as it is; decide with B19's recalibration** | no change to goldens; B19 owns the retreat and rout pairs already left red at army scale |
| B. Cap the refill per cell per tick (a cell passes forward at most `CELL_FLOOR`, 50, a tick) | ties replenishment speed to cell size; a deep unit holds its front under heavy loss; a thin one cannot. Adds one constant |
| C. Dissolve and merge a live cell under `CELL_FLOOR` into the nearest rank-mate with room | the band becomes an invariant to the end; cell count falls as the unit shrinks; makes the unit minimum natural |
| D. Raise `UNIT_ROUT_FLOOR` from 80 to `MIN_CELLS_PER_UNIT x CELL_FLOOR` (200) | a unit that cannot hold four cells of 50 routs; one number, owned once; moves every rout test and the golden modes |

C and D follow from your rulings together: if a cell holds at least 50 and a unit is at least 4 cells, a unit under 200 is not a unit. I recommend D read with C, and A until B19 can measure it (the `arms` instrument is a one-mechanic comparison and no campaign-level balance instrument exists, CLAUDE.md §7). Not measured: the retreat's effect on any of these, other seeds, horse units, the depth of the 17-cell shape.

## 4. A package that keeps every ruling literal and invents one number

| decision | choice |
|---|---|
| floor | warn at form time (as built) |
| troops per weight | 10,000 (floor-sets) |
| typical size | content target, reached by 3 to 5 cohorts once the army verbs ship |
| cells | foot 50 to 100; horse 50 to 75 (the one invented number, 75) |
| refill | unchanged now; C and D decided at B19 with a measurement |

## 5. What each change moves, so none is made blind

- TROOPS_PER_WEIGHT: every headcount field, `_realm_goldens.py` at seeds where fields fold (seeds 3, 4, 7, 9, 10 today), the cohort army sizes, `sim_params.json`.
- Horse cap: `troops.yaml`, `troops.json`, `troops_data.py` (exporter), every mounted unit's footprint, `ci_golden_modes_check`.
- Refill or rout floor: the whole combat tick: the two red retreat tests (`test_cp_t04_03_retreat`), the envelop test, every rout and conservation test.
- Floor as refusal: `massbattle._refusal`, the `march` fold, `test_mass_battle_module`.

## 6. Not verified here

- The refill reading is one seed at one size; it is a reading, not a distribution (CLAUDE.md §0.1 pt 4).
- The horse option effects are arithmetic from `footprint_for`; no horse battle was run.
- `S` (sublinear) was not run, and its effect on `_eff_march`'s per-person shares is inferred from reading `share_of`.
- Whether army formation, once unwithheld, produces armies in the band is a prediction from cohort weights (2 and 4), not a run.
