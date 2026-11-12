# SE — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subsystem SE: settlements, territory, economy, migration, founding, hunger. Dossier
`dossiers/07_SE.md`. Every count below is a reading at this commit with the seed and season count
stated beside it; `PYTHONHASHSEED=0` on every run. Probe scripts and raw outputs are in the scratchpad
(§12), not in the tree.

## 0. Verdict

**Not yet a sound basis for a dynamic emergent narrative game: the settlement layer as coded is a correct,
conserved, well-factored accounting kernel standing under a world that gives it nothing to account for.**
The eight entries of `modules/settlements/` are pure, typed, single-owner and reached by composition row;
the larder ladder, the draw-before-yield order, the two-sided store moves and the capacity throttle are
each right in isolation and each has an executing test. The single largest obstacle is that **the built
realm has no scarcity, no differentiation and no population dynamics, so none of the kernel's
consequence paths is ever reached in computed play**: 37 settlements are stamped identically (one
harbour, one seam, one garrison, one cohort of weight 2), produce about twenty-one times what they eat
every season forever, accumulate stores that nothing spoils, spends or trades, and hold a population that
no rule grows, shrinks, splits or moves. In three seasons of seed 0 (2,367 acts) the realm emitted no
`site.restored`, `site.worked`, `site.built`, `rung.founded`, `rung.razed`, `exchange.made`,
`requisition.taken`, `condition.band_crossed` or `person.died`; its one hunger event is a world-gen
artefact (every larder is empty before the first yield, so all 37 cohorts lose the same 60 body in season
0 and never again). Settlements are therefore not a living substrate; the economy closes arithmetically
and opens nowhere (production has one consumer, and that consumer is saturated); and the canonical
geography feeds the battlefield's terrain and nothing else — not travel cost, not supply, not trade, not
yield. The path forward is short and mostly data: make places differ and make matter scarce at the owner
(`rosters.yaml`, `cohorts.yaml`, `harness/populated.py`), then build the three missing dynamics (spoilage,
a census writer, a works producer) on the kernel that already exists.

## 1. What it is, as coded

### 1.1 The module (`modules/settlements/`, 371 lines, eight entries)

| entry | file | kind | rule in one line | host caller (opened) |
|---|---|---|---|---|
| `settlements.larder_draw` | `larder.py:39` | query | per cohort, per weighted kind: `want = weight × Person.weight`; source is the first rung up the ladder holding `> 0` in the running view; `take = min(want, held)`; the remainder is not walked on | `queries/world_q.py::subsistence_draw` (`:1273`) |
| `settlements.drawn_under` | `larder.py:73` | query | one column of the draw summed over a subtree | `world_q.demanded` / `delivered` (`:1454`, `:1494`) |
| `settlements.subsist` | `subsist.py:40` | step_call | debit per source rung; who is short; drained rungs and their subtree gap; `lost = body_step × units short`; body floors at 0 | `loop/matter.py:600` |
| `settlements.produce` | `produce.py:32` | step_call | per rung, per Site on it: `int(base × condition/scale × factor)`; credit onto post-debit stores | `loop/matter.py:741` |
| `settlements.housing` | `housing.py:27` | query | population = Σ resident weight in subtree; capacity = `max(floor, dwelling Sites in subtree)` | `world_q.population` / `capacity` (`:1786`, `:1856`) |
| `settlements.fabric` | `fabric.py:29` | query | ceiling = `scale × min(matured, declared) // declared`; share = `1 / max(1, present)` | `world_q.ceiling` / `share` (`:564`, `:595`) |
| `settlements.fortification` | `fortification.py:23` | query | mean garrison condition over scale, `0.0` with no garrison | `world_q.fortification_of` (`:2206`) → `seam/wrappers/mass_battle.py` |
| `settlements.provision` | `provision.py:30` | query | `troops = min(weight, min_k stores[k] // ration[k])` when the fixture is on; identity when off (shipped off) | `seam/wrappers/mass_battle.py::resolve` |

Every entry takes a frozen input record from `engine/season/queries/inputs.py`, returns a typed outcome,
imports nothing but those record types (and, for `subsist`, its sibling `larder`), reads no `World`, holds
no token and keeps no state. The registrar refuses a missing or re-kinded row at driver construction
(`references/module_contracts.yaml:70-118`; `loop/matter.py:47`, `STEP_CALLS`).

### 1.2 The host (where the settlement layer actually lives)

The module is the arithmetic. The behaviour is in the host, and it is roughly ten times the module's size:

- **`loop/matter.py::matter` (`:284-903`)** — barrier 2, once a season, in this order: term maturation
  (Record stages, Tenure terms), docket lapse, claim decay, standing crossings, **subsist** (`:600`), body
  falls and deaths from hunger (`:690-711`), the ageing/illness hazard (shipped at rate 0, `:726`),
  **produce** (`:741`), per-rung debit / `yield` / credit writes (`:744-795`), travel-leg end (`:831`),
  lattice strain (shipped at weight 0), Site wear and band crossings (`:852-884`). Every write is through
  the gate and emits (`stores.changed`, `yield.taken`, `body.changed`, `person.died`, `condition.worn`,
  `condition.band_crossed`, `travel.ended`).
- **`loop/effects_economy.py`** — `work` and `restore` (one `_rise` formula: headroom to the ceiling times
  the commons' share, staged on the fold's accumulator and clamped once), `sabotage` (`_fall`, the
  mirror), `transfer` (two-sided `_shift`, plus `_renewals`: a payment out of a seat's rung renews the
  `oblige` terms of obligees present at the receiving rung), `exchange` (two `_shift`s).
- **`loop/effects_migration.py`** — `move` (re-homes `contain` only; refused in custody, into an
  arrival-only rung, or off the §10 ladder), `migrate` (re-homes `contain` and `reside`; additionally
  refused into a rung at capacity), `_relocate` (shared with `march`'s arrival).
- **`loop/effects_founding.py`** — `found` (mints a Rung of the works' plan kind under the works' `at`,
  moves the `works_cost` stake two-sided into it, opens the founder's `hold`), `build` (mints a Site at
  condition 0, consumes the cost one-sided), `raze` (ends an occupied settlement held by another faction;
  closes every edge naming it; re-homes nothing).
- **`queries/world_q.py`** — the projections (`subsist_input`, `produce_input`, `larder_input`, …) and the
  public readers (`demanded`, `delivered`, `hunger`, `population`, `capacity`, `has_room`,
  `fortification_of`, `season_factor_of`, `requisitionable`, `governors_of`, `larders_in_purview`).
- **Data owners** — `rosters.yaml`: `site_yield` (harbour 40 grain + 30 salt; seam 50 ore + 10 timber;
  every other kind nothing), `wear_per_season`, `band_floors`, `capacity_floor`, `works_cost` (10 of one
  kind per priced plan), `subsistence_weight` (grain 2, salt 1), `hunger_bands`; `data/fixtures.py`:
  `body_step=10`, `season_factor=1.0`, `season_factor_draw=()`, `field_provisioning=False`,
  `stock_report="crossing"`, `default_transfer_amount=1`; `cohorts.yaml` (37 rows, every one weight 2);
  `venues.yaml` (quarters and buildings by settlement type, eleven institutional seats, two planned
  works); `systems/settlements/valoria_geography_v30.yaml` (17 provinces, 37 settlements, adjacency,
  terrain, water).
- **`data/geography.py`** — one cached read of the geography file; `adjacent_territories()` for the
  lattice coupling. Its two consumers are `modules/mass_battle/terrain.py` (through
  `MassBattleInput.geography`) and `loop/matter.py::_lattice_strain`.

### 1.3 State the subsystem owns

`Rung.stores` (a `{kind: units}` map), `Rung.yield` (last season's product), `Site.condition`
(0..`condition_scale`), `Site.rung`/`Site.kind`, `Person.body` and `Person.weight` (shared with CHAR),
the `contain` and `reside` Tenures, `Person.travel_leg`, and `World._subsistence_shortfall` (a report
field the loop never reads). There is no `Settlement` object: a settlement is a `Rung` of kind
`settlement` with Sites hanging from it and hearth/community rungs beneath it.

### 1.4 Execution evidence

**The populated realm, no acts (the economy alone).** `se_probe.py 0 N noacts` — `build_realm(0)`, the
real `SeasonDriver`, a chooser that returns nothing for every person, so only the barriers run:

| reading | build | after season 0 | after season 4 | after season 14 |
|---|---|---|---|---|
| persons / cohorts | 83 / 37 | 83 / 37 | 83 / 37 | 83 / 37 |
| cohort body (min = max) | 1000 | 940 | 940 | 940 |
| total stores | 0 | 4,810 | 22,385 | 63,122 |
| next draw: want / take (grain+salt) | 222 / 0 | 222 / 222 | 222 / 222 | 222 / 222 |
| last yield (all kinds) | — | 4,810 | 4,551 | 4,070 |
| Site condition min / mean | 1000 / 1000 | 990 / 997 | 950 / 988 | 850 / 965 |
| hunger bands (38 settlement-kind rungs) | 37 starving, 1 fed | 38 fed | 38 fed | 38 fed |
| settlements over capacity | 4 | 4 | 4 | 4 |

Reading: the only shortfall is at tick 0 and it is identical for all 37 cohorts (min equals max); the
surplus ratio is 4,810 produced against 222 eaten, about 21.7 to 1, and it decays only as fast as wear (10
per season on harbours and seams, about 1% of yield a season); stores rise without bound. Population,
capacity and the over-capacity count never move.

**The populated realm, computed play.** `python -m engine.season.harness.aperture 3 0` (seed 0, 3 seasons,
83 persons, 2,367 acts; the instrument's own control line reads `content_hash EQUAL`). SE verbs, acts
attempted → executed:

| verb | attempted | executed | deciding read on refusal |
|---|---|---|---|
| `work` | 0 (formed for 1 person) | 0 | — |
| `restore` | 0 (formed for 1 person) | 0 | — |
| `sabotage` | 47 | 0 | `exists:Site=0` ×47 (the referent is never a Site) |
| `found` | 7 | 0 | `exists:works=0` ×7 |
| `build` | 4 | 0 | `exists:works=0` ×4 |
| `raze` | 22 | 0 | post-admission ×21 (no occupation) |
| `transfer` | 70 | 2 | `stores:grain=>0` ×53 post-admission; `stores:grain=0` ×14 |
| `exchange` | 79 | 0 | post-admission ×37; `stores:salt=UNKNOWN` ×28 |
| `requisition` | 5 | 0 | `clause:authority` ×5 |
| `move` | 78 | 21 | `audience=True` ×40 post-admission; `audience=UNKNOWN` ×16 |
| `migrate` | 116 | 16 | `clause:room` ×79; `clause:path` ×20 |
| `march` | 29 | 3 `field.unopposed`, 1 `field.lost`, 0 `field.won` | no-read ×25 |

Kinds never emitted in that run, from the instrument's own list: `site.restored`, `site.worked`,
`site.built`, `site.damaged`, `rung.founded`, `rung.razed`, `rung.seized`, `exchange.made`,
`requisition.taken`, `condition.band_crossed`, `person.died`, `weight.changed`, `envelope.changed`,
`term.renewed`, `field.won`. Kinds emitted with no act behind them: `condition.worn` 966, `yield.taken`
111, `stores.changed` 185, `body.changed` 37 (season 0's uniform fall), `travel.ended` 24.

**The scarce fixture.** `python -m engine.season.harness.scarce` (4 seasons, both arms): with the steward's
question named, a shortfall is recorded at tick 0 (`shortfall:grain 15`, `shortfall:salt 8`), reaches the
steward as a claim, and he executes one claim-sourced `transfer` of 8 salt at tick 1; grain is never
relieved in four seasons (demanded 20, delivered 0 at ticks 1, 2 and 3) while the granary rises from 100
to 216 grain. With the question not named (the shipped H-54 arm) no relief is ever sent. So the chain
*shortfall → witness → claim → question → transfer* executes on computed acts in a hand-built world, once,
for one of two kinds.

(remaining sections appended below)
