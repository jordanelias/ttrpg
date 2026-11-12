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

**Play against no play (the control this audit rests on).** `se_probe.py SEED N play` against the no-acts
arm, same seed:

| reading after season 2 (tick 3) | no acts, seed 0 | play, seed 0 | play, seed 1 |
|---|---|---|---|
| grain / ore / salt / timber, all rungs | 4070 / 5476 / 3108 / 1036 | 4070 / 5476 / 3108 / 1036 | 4070 / 5476 / 3108 / 1036 |
| stores outside settlement rungs | 0 | 2 (person rungs) | 4 (3 person, 1 realm) |
| Site condition min / mean / max | 970 / 993 / 1000 | 970 / 993 / 1000 | 970 / 993 / 1000 |
| cohort body min = max | 940 | 1000 (`tend`) | 1000 (`tend`) |
| acts resolved over the three seasons | 0 | 2,367 | 2,390 |

Two thousand four hundred acts by 83 persons leave the realm's economy where no acts leave it, to within
four units of 13,690. The one difference in bodies is `tend` restoring every cohort to 1000 in the
season it fell (H-304).

**Who performs the settlement verbs** (`se_who.py 0 2`, seed 0, two seasons, 1,529 resolved acts): cohorts
perform 708 of them. Every executed cohort `move` (11 of 11) and three of four executed named `move`s
name the mover's own rung. Cohort `migrate`: attempted 51, executed 0. Named `migrate`: executed 10, by
five people; the Crown's Spymaster changes residence four times in two seasons (Ehrenfeld to Saltbrück
to Königsbrück to Auerheim to Königsbrück). Both executed `transfer`s are a cohort moving 1 grain from
its own settlement into its own person-rung, where no draw reaches it.

**Hunger made to bind** (`se_bind.py`, no acts, eight seasons; per-head need multiplied, weather off or on):

| arm | reading |
|---|---|
| ×10, weather off, seed 0 | all 37 cohorts hold one body value every season (400, 400, 390 … 290); 37 of 37 in one band |
| ×20, weather off, seed 0 | all 37 cohorts die at season 0; thereafter 38 settlements read `fed` and realm grain rises 1,480 → 11,322 |
| ×10, weather on, seed 0 | bands differ from season 0; 8 cohort deaths at season 2; 29 cohorts thereafter |
| ×10, weather on, seed 1 | 19 cohort deaths by season 7; 18 cohorts alive; all 38 settlements `fed` at the end |

**A differentiated realm by hand** (`se_ground.py 0 8 G`, not a repo artifact: the 11 highland
settlements lose their harbour, their five territory rungs are stocked with G seasons of deficit): at
G = 4 the 11 highland cohorts stay at body 1000 for four seasons while their territory grain falls to 0,
then lose 60 a season, and the 26 lowland cohorts stay at 1000 throughout; at G = 0 the 11 fall from
season 0. The larder ladder feeds from the territory rung with no code change.

**The corpus** (`python -m engine.season.harness.corpus_run`, seed 0, 143 cases): 103 `RUNS-UNDECLARED`,
40 `SPAN-UNAUTHORED`, both bars `NOT-COMPUTABLE`. `transfer` and `move` executed; `build`, `found`,
`exchange`, `sabotage` only refused; `migrate`, `requisition`, `restore`, `work`, `raze` never attempted.

**Loops** (`python -m engine.season.harness.loops`): five declared LOOP rows, derived equals declared
for signed amplifiers; the instrument lists *"MATTER (every pass but claim decay and the lattice
coupling)"* under BLIND. The larder, yield, body and wear passes are outside the derived cycle check, and
the only settlement loop declared is H-235's lattice coupling, shipped at weight 0.

## 2. Steelman

Ranked by the weight each bears.

1. **The kernel is conserved, single-owned and typed, and it was extracted without moving a hash.** One
   function computes the draw MATTER writes from and the draw `demanded`/`delivered` report
   (`subsist.py:42`, `larder.py:39`); every store move goes through `_shift`
   (`effects_shared.py:128`); every write crosses the gate and emits. *Attack:* look for a second copy of
   the draw or a one-sided move. *Outcome:* none found; `build`'s one-sided consumption is declared
   (`effects_founding.py:238`). The steelman holds for whole positive amounts and fails outside them
   (F-SE-10).
2. **MATTER decides nothing.** A shortfall, a band crossing and a death are emissions; every consequence
   is some person's later act (L5, `matter.py:651-663`). This is what lets a famine be a story with
   authors rather than a script. *Attack:* find a social quantity written at MATTER. *Outcome:* none; the
   one mechanical consequence is death at body 0, a licensed cell. Holds.
3. **Scarcity reaching a person is built end to end and executes.** `scarce.py` shows shortfall →
   Observation → witness (seat channel since IN-22) → claim → question → `transfer` on computed acts.
   *Attack:* run it. *Outcome:* it executes once, for one kind, and the cohort keeps starving beside a
   full granary (F-SE-04). Holds as an existence proof, fails as a relief mechanism.
4. **Shipping the live arms dark was right while the worlds held nothing to eat.** A surplus realm with
   bodies that cannot fall is honest about being unbalanced, and Jordan ruled the realm's missing
   shortfall a balance number (H-160 limit 3, 2026-10-12). *Attack:* is the dark arm reachable by a
   number? *Outcome:* `body_step` is live at 10 since REM-52 and CR-22 holds the magnitude; but the
   number alone gives a synchronised famine (§1.4), so the steelman holds for the kernel and fails for
   the world it runs on (F-SE-01).
5. **The thin module is the architecture, not neglect.** A-25 has a module take typed input, return a
   typed outcome and hold nothing; wear, terms, travel and every effect are host by a stated reason each
   (`proposals/2026-10-07-settlements-computation-modules.md` §4). *Attack:* does any rule the module
   should own live twice? *Outcome:* no. Holds. The cost is elsewhere: there is no settlement *object*
   to play (§9).
6. **One cohort class, authored at world-gen, is a ruled economy of means** (ED-IN-0255, ED-WR-0011, S9).
   *Attack:* what does the class do in play? *Outcome:* it eats correctly and otherwise behaves as an
   individual: 46% of resolved acts, among them forging and duelling (F-SE-14). The ruling holds; its
   consequence was not priced.
7. **The plan already holds the missing dynamics** (CP-T08-01 labour, -03 spoilage, -02 endowment, -05
   price, -06 unrest, -07 tax; CR-08 census; CR-22 binding; CR-49 exchange), each with a falsifier and a
   control. *Attack:* read their gates against each other. *Outcome:* the order is circular at one point
   (the `ground` flip waits on a relief path that a uniform realm cannot exhibit) and silent at another
   (nothing schedules recovery after a cohort dies). Holds as coverage, fails as sequence.

## 3. Adversarial findings

Ranked worst first. Severity: **B** blocks a requirement, **D** degrades narrative, **H** hygiene.

**F-SE-01 · B · Every settlement is the same economic object, so nothing needs to move and any scarcity
binds everywhere at once.**
Evidence: `harness/populated.py:1215-1220` (one Site per producing kind at every settlement), `:1258-1261`
(one garrison at full scale each), `cohorts.yaml:65-101` (37 rows, weight 2). The canon map says
otherwise in untyped strings (`valoria_geography_v30.yaml:75,83,101,239`: *Breadbasket*, *Hafenmark food
dependency anchor*, *Timber Valley*, *Northern mines*).
Falsifier run: `se_bind.py 0 8 10 0`; a second body value or band among the 37 would break the claim.
Outcome: `distinct_bodies=1` in all eight seasons. Control: weather on gives distinct values, so the
instrument can see difference.
Touches R-01, R-04, R-05 (`transfer`, `exchange`, `requisition` have no occasion).
Consequence: no dependency, no leverage, no route worth cutting, no town worth relieving; a returning
finding (`.audit/2026-08-11-world-schema-gap-audit/03_discussion.md:71`, *"37 near-identical
settlements"*, on the retired sim; `research/by_lane/SE_…md` M-SE-8; `D_T08.md` row 32), scheduled once
(CP-T08-02) and shipped off behind a gate it cannot meet.
Fix: `proposals/07_SE_ground_and_granaries.md`.

**F-SE-02 · B · Population is a constant that can only fall, falls whole, and its loss is invisible.**
Evidence: no writer of `Person.weight` (CR-08 unbuilt); `subsist.py:71-76` and `matter.py:709-711` (body
0 is death of the whole cohort); `world_q.py:1921` docstring (*"A settlement with no cohort under it
(D = 0) reads `fed`"*); `produce.py:38-46` reads no person.
Falsifier run: `se_bind.py 0 8 20 0` and `1 8 10 1`; a dead settlement reading other than `fed`, or its
yield falling, would break it. Outcome: 37 dead, 38 `fed`, grain 1,480 → 11,322.
Touches R-01, R-04, NERS-R completeness.
Consequence: a famine has two states, untouched and extinct, and the extinct town is the realm's best
granary. No decline, no flight, no recovery.
Fix: `proposals/07_SE_population_census.md`; the rising half is survivor S-SE-1.

**F-SE-03 · D · The realm's only hunger event is a world-gen artefact, and a test pins it.**
Evidence: stores `{}` at build (§1.4); `matter.py:507-512` (draw before yield);
`test_hunger.py::test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield`.
Falsifier: any cohort not short at season 0, or any short after it. Outcome: 37 of 37 short at season 0,
0 after, both seeds and the no-acts arm.
Touches R-01, R-09.
Consequence: the opening season of every realm run is a simultaneous kingdom-wide dearth that `tend`
erases the same season; under CR-22's ×20 arm it is extinction. CR-22's SEASON-0 FLOOR RULE knows this.
Fix: stock the larders at world-gen (`07_SE_ground_and_granaries.md` §4 c).

**F-SE-04 · D · Relief is one act, one kind, once; the purpose-built fixture ends with a starving town
beside a full granary.**
Evidence: `scarce` named arm (§1.4): one `transfer` of 8 salt at tick 1; grain demanded 20, delivered 0
at ticks 1 to 3; granary 100 → 216 grain; at tick 3 the steward's `transfer` names `set_hungry` as both
`from` and `to` and is refused.
Falsifier: a second claim-sourced `transfer.made`, or any grain delivered. Outcome: neither.
Touches R-01, R-02, R-04.
Consequence: the chain proves propagation and delivers no relief story. The crossing-only report is
ruled a balance number (H-160 limit 3) and is not re-raised; what is added is the reading that one
question forms one bag of one kind (`store_kind_of`) and that the second question's `from` binds to the
hungry rung. The formation half is the CHAR lane's (`decision/options.py`); the SE half is that the
ladder, not an act, should be the standing relief path (`07_SE_ground_and_granaries.md` R3).

**F-SE-05 · D · The fabric's raising arm does not reach in play, and it used to.**
Evidence: `aperture 3 0`: `restore` formed for 1 person, attempted 0; `work` formed for 1, attempted 0;
`site.restored` and `site.worked` never emitted. H-171's cite recorded `restore` at 9 executed after
`24f` and `requirements.yaml`'s scale note still says *"in the realm only `restore` executes"*. `work`
cannot run on a dwelling or garrison at all (`D_T08.md` row 19: empty `band_floors`).
Falsifier: one `site.restored` in three seasons at seed 0. Outcome: none. The cause of the change since
`24f` was not isolated `[UNVERIFIED]`; candidates are the shipped `question_aggregation_rule: first` and
the cohort pursuit vectors added by SE-06.
Touches R-05, H-105.
Consequence: harbours and seams wear 10 a season and nothing mends them (read to season 20: minimum
condition 800, no crossing emitted). By arithmetic on that wear and the floors in `rosters.yaml`
(`bulk_shipping` 800, `deep_mining` 700), not by a run to that horizon, the first band crossing is at
season 21 for all 37 harbours at once and season 31 for all seams. Inside any horizon a session runs,
wear is a 1% a season decline nobody answers.
Fix: no SE edit until the cause is read; the reading belongs in H-105's cite (§6, R-SE-16).

**F-SE-06 · D · The geography feeds the battlefield and nothing else.**
Evidence: grep over `engine/`, `modules/`, `systems/`, `tools/` (non-test) for `settlement_adjacency`,
`terrain_cost_matrix`, `march_budget`, `vision_range`, `bridges`, `poi_catalog`, `starting_pros`,
province `fort_level`, settlement `stats` and `coords`: no reader. Read: `provinces`, `terrain`, `water`
(`modules/mass_battle/terrain.py`, through `data/geography.py`), settlement `territory`/`type`
(`populated.py:1157-1190`), `adjacency` (the lattice coupling, weight 0). Travel is the containment
ladder: one leg whatever the distance (H-328), and no settlement-to-settlement edge exists.
Falsifier: the grep. Outcome: as stated.
Touches R-04, GD-3 (contiguity, H-186).
Consequence: a march, a migration and a relief column cross the peninsula at the cost of crossing a
street; no pass is a chokepoint, no route can be cut, supply has no line. The design intent is a march
budget over a terrain-cost field with edge types and invasion sequencing
(`.designs/…/march_layer_v30.md` §1-§5, `settlement_adjacency_v30.md` §1-§3); none of it is game.
Fix: design-first (§8 step 7); the first use that pays is the granary's reach (territory rung) which
needs no adjacency, then IN-52's field provision.

**F-SE-07 · D · What persons do to the economy is nil in size and partly a sink.**
Evidence: §1.4 control table; `default_transfer_amount=1` (`fixtures.py:625`); both executed
`transfer`s at seed 0 deliver into the giver's own person-rung, which no ladder draws from
(`larder.py:56`: home first, then up).
Falsifier: stores differing between the play and no-acts arms by more than a handful. Outcome: 2 and 4
units.
Touches R-01, R-04.
Fix: amount as a choice (`07_SE_arc_needs.md` §3 b); the destination half is CR-49's `referent_class`,
extended to `transfer`.

**F-SE-08 · H (with a cost) · 248 of 322 `condition.worn` Events a season report a wear that did not
happen.** Evidence and fix: `07_SE_kernel_repairs.md` §3. Each is witnessed and deposited.

**F-SE-09 · D · Capacity acts as noise and migration as churn.**
Evidence: `aperture 3 0`: `migrate` attempted 116, executed 16, refused for room 79; the realm starts
with 4 settlements over capacity and stays so; capacity ignores dwelling condition and evicts nobody
(H-307); the executed migrations are five named persons re-homing repeatedly across territories with no
cost of distance; no cohort migrates.
Touches R-04. Consequence: the throttle that was to make `found` and `build` matter refuses individuals
at occupied hearths while most hearths stand empty (`D_T08.md` row 15 counted 185 of 211, not re-run
here; at this commit the realm's capacity sums to 212 against a population of 120).
Fix: CR-49's class for `migrate`'s `to`; `07_SE_population_census.md` gives weight a writer, which is
what flight would move.

**F-SE-10 · D · A store move accepts a negative, zero or fractional amount** (H-306). Fix:
`07_SE_kernel_repairs.md` §2.

**F-SE-11 · H · A move to where the mover stands publishes as travel** (H-140, H-329). Fix:
`07_SE_kernel_repairs.md` §4.

**F-SE-12 · D · The world never grows.** `found` 0 of 7 and `build` 0 of 4 at seed 0 over three seasons
(`exists:works=0`); two authored works exist (`venues.yaml:192-198`) and the batch card records them
executing by draw at seed 2 `[UNVERIFIED here]`; nothing in play declares a works. Rungs 414 at build,
414 at the end. A founded hearth would hold no resident and no dwelling (`effects_founding.py:110`).
Touches R-05. Fix: none new; the producer is IN-45's M5 (B) content (more `planned_works` rows), Jordan's.

**F-SE-13 · B (standing requirement) · There is no settlement scenario to play.** §9. Fix:
`07_SE_valley_scenario.md`.

**F-SE-14 · D · The people of a town act as one individual.** 708 of 1,529 resolved acts at seed 0 are
cohorts': `create_record` 115, `utter` 70, `challenge` 60, `forge` 47, `research` 30, `train` 25. S9.1
(one class) is ruled and working. Consequence: nearly half the realm's story is crowds forging documents
and issuing challenges. Cross-listed to CHAR (§10).

**F-SE-15 · H (cross-lane, load-confounded) · A season's cost grew with the tick in every arm run.** No
acts: 1 s at season 0, 47 s at season 18. Play: 49 s, 175 s, 571 s over three seasons at seed 0. The
machine was shared with the other lanes' runs, so the magnitudes are not measurements; the monotone
growth in a no-act world (events per season 1,270 → 10,594, the growth outside every settlement kind) is.
Owner: CORE (`harness/soak.py` grades exactly this). A settlement game needs tens of seasons.

**F-SE-16 · H · The instruments cannot see the economy's loops.** `loops` is BLIND to MATTER's larder,
yield, body and wear passes; `hunger` is read by `census` alone; `corpus_run` builds no eater. So no
instrument would report the first feedback loop the economy acquires (a thinner cohort wanting less).
Fix: none proposed (§0.1 pt 5); the readings named in each proposal's gate are the instruments.

## 4. Code matters

- **Ownership and duplication.** Clean. One draw (`larder_draw`), one debit owner (`_shift`/`_debit`),
  one rise formula (`_rise`, `_fall` its mirror), one journey (`_relocate`), one price reader (`_cost`),
  one capacity test (`has_room`). The world builder is the exception by placement, not duplication:
  `harness/populated.py::build_realm` (2,162 lines) is the only producer of the realm and lives in the
  instrument tree.
- **Dead or unreached in computed play at this commit** (`aperture 3 0`, seed 0): `_eff_work`,
  `_eff_restore`, `_eff_sabotage`, `_eff_found`, `_eff_build`, `_eff_raze`, `_eff_exchange`, `_renewals`
  (`term.renewed` never emitted), `provision`'s `on` arm, `_lattice_strain` (weight 0), the ageing and
  illness pass (rates 0), every band crossing. Each executes under a hand-built test.
- **Contract and seam fidelity.** The eight rows in `references/module_contracts.yaml:70-118` match the
  code; `test_settlements_module.py` imports every entry in a fresh process and asserts it asserted
  (`len(targets) >= 8`). The module imports only `queries/inputs.py`. Layer 1 §A.2:174 gives MATTER
  *"Sites, bodies, larders, ttl/term"* and §A.2:179 gives CENSUS `weight` and `envelope`; the code
  conforms, and CENSUS writes neither. `Rung.envelope` has no writer (H-171, IN-44).
- **Determinism.** Every order is sorted (`subsist.py:57,71,80`; `matter.py:744`); the season factor draw
  is keyed on `(world_seed, tick, territory)` (`world_q.py::season_factor_of`). `aperture 3 0`'s own
  control line reads `content_hash EQUAL` between `populated.run` and its instrumented arm (2,367 acts
  each). Same-seed repetition across processes was not run by this audit.
- **Test strength.** About 170 tests in 15 files, no `pytest.approx`, mutation notes in several
  docstrings. Three limits: (i) `test_hunger.py::test_i` pins F-SE-03's artefact as behaviour; (ii) the
  realm-level tests assert what the kernel does on a world that never exercises its consequence paths, so
  they cannot observe F-SE-01 or F-SE-02; (iii) no test runs the play arm against the no-acts arm, which
  is the cheapest observation that the economy is closed to persons. `[SKIPPED: test bodies beyond
  names, docstrings and the files quoted — sampled, not read in full]`.
- **Performance.** `produce` and `subsist` are linear in Sites and cohorts and called once a season. The
  cost that grows is not theirs (F-SE-15); their contribution to it is 433 actorless Events a season, 248
  of them no-ops (F-SE-08).

## 5. Design matters

- **Where intent, ruling and code agree.** The ladder (settlement < territory < duchy < realm, province a
  Query) follows `scale_hierarchy_v1.md` §1-§2 (RATIFIED, Jordan 2026-07-13) and is built
  (`populated.py:1127-1161`). Subsistence as a territorial matter carried by synecdoches (ED-IN-0255) is
  built. Capacity as a Query over dwellings with a floor (RR-2, ED-SE-0051) is built. Dearth as an
  entitlement failure a governor answers (`.designs/…/settlement_layer_v30.md` §4.3a, after Sen and
  Scott) is the shape `scarce.py` executes.
- **Where they disagree, and what the game follows.** (i) The ratified hierarchy ruling says *"factions
  … need to hold PEOPLE, and it is the number of people and the weight of their positions that carry the
  value"* (§5.1) and that settlements' consent modulates rule (§4). The code's people, the cohorts (74 of
  120 population weight), carry no `commit`, so they are no faction's, muster for nobody and consent to
  nothing; the game follows the code, and the cost is that the largest weights in the realm are outside
  faction power (CR-107b holds the `faction:` key). (ii) The design gives a settlement a type that sets
  what it produces (`settlement_layer_v30.md` §1.1-§1.2); the code's type sets its buildings
  (`venues.yaml`) and nothing economic. (iii) The design moves armies on a march budget over edges; the
  code moves them up a containment ladder.
- **Ruled items accepted as binding.** ED-IN-0255 (only cohorts eat); ED-WR-0011 (authored cast);
  ED-SE-0051/RR-2 (capacity); ED-SE-0053's standing orders (no hearth larder, no delivery across
  `contain`); ED-SE-0052 (`band_floors["body"]`, `fort_level` stays declared); H-160 limit 3 (the
  realm's silent dearth is a balance number); H-149 (`march_target_kinds`); the source-precedence tiers
  (`rosters.yaml:75-80`: research tier 3, the governance redesign tier 4).
- **NERS cuts.**
  - *`share` as the commons' divisor* (`fabric.py:37`): one act raises `headroom / present`. Cut it and
    a single hand at a harbour forty stand at mends it whole, which is what happens today at a hearth of
    one. It survives N weakly: its only effect in play would be to slow repair where people gather, the
    reverse of many hands; and no computed `restore` reaches it. E against that: a rule with a ruled
    heading and no executed instance. Keep, re-read when `restore` executes.
  - *`Rung.envelope`*: no writer, no reader in the settlement layer. Fails N from every direction. It
    dies; the deletion is a Layer-1 edit already routed (IN-44 row 16).
  - *The hunger band query*: cut it and `census` loses one line and nothing else. It survives only as
    CR-22's instrument; with `empty` added it becomes the valley scenario's end reading (§9).
  - *`provision` (IN-52)*: a clean bound with a control arm; it survives N the day a treasury holds
    stock, which is the same day the granary does. Its `min` over every eaten kind (a treasury holding
    grain and no salt fields nobody) is a completeness defect its own row lists.
- **Prose only, therefore not yet game.** Settlement stats (Prosperity, Defense, Order), L/PS and
  Mandate, facility tiers, charters, the dearth response verbs (Open Granary, Fix Prices, Provision),
  grain routes, Local Actors, entry terms, the stature ladder, the march layer, the governor's action
  budget (tier 4). The `stats` triplet sits in the canon data file and no code reads it.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Items the dossier lists

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-105 | absent (PRODUCER); closed? | **open, and worse than its cite** | `restore` 0 attempts in 3 seasons at seed 0 (F-SE-05) | cite gains this reading (R-SE-16) |
| H-140 | measured (RULING), open | open; **decided** | `se_who.py`: 14 of 15 executed moves same-place | R-SE-09, `07_SE_kernel_repairs.md` §4 |
| H-149 | ruled | closed (ruled, enforced) | `test_march.py`; not re-raised | none |
| H-166 | assumption; limits 1, 2 built | limits 1, 2 closed in code; 3 narrowed (`raze`); 4 narrowed | `effects_founding.py:51-89,170`; unreached in play | limit 3's Site closer stays with H-228 |
| H-236 | measured (lattice has no source) | open; wrongly filed under SE by path | T15 holds no Site; weight 0 | WR lane (H-85) |
| H-241 | assumption; built, shipped off | open (the flip) | `provision.py`; `fixtures.py:809` | IN-52's flip follows the granary (§8 step 5) |
| H-293 | measured (MECHANISM) | open; survives the ladder | §11, S-SE-2 | Jordan |
| H-303 | measured (RULING) | open; **decided** | direct call reproduced by the row; binds under `ground` | R-SE-11, `07_SE_ground_and_granaries.md` §4 d |
| H-305 | measured (MECHANISM) | open; **decided** | `subsist.py:72` | R-SE-04, `07_SE_population_census.md` §4 a |
| H-306 | measured (ABSENT_RULE) | open; **decided** | `effects_shared.py:120-136` | R-SE-07, `07_SE_kernel_repairs.md` §2 |
| H-309 | measured (RULING) | **closed by precedent** | a seat is a `hold`, exercised `via`; no seat verb asks presence at the seat's rung | R-SE-17 |
| H-327 | measured (MECHANISM) | open; **decided** | `matter.py:839-843` writes no `observed` | R-SE-10, `07_SE_kernel_repairs.md` §5 |
| H-304 (secondary) | measured | open; PC lane's `tend`; binds here | play arm: `body.tended` 37 at season 0 | cross-listed; CR-22 cannot bind while `tend` restores whole |
| H-307 (secondary) | measured | open | 4 settlements over capacity at build, unchanged | folded into F-SE-09 |
| H-168 (secondary) | measured: `migrate` executes only from hand-built acts | **now false** | `aperture 3 0`: 16 executed from computed acts (IN-45) | cite re-read (R-SE-18) |
| CR-40 | EDIT, first in B10-16 | open, correct as written | `starting_pros` has no reader (grep) | build |
| CP-T08-01 | BUILD | open | — | build before the `ground` flip (§8 step 3) |
| CP-T08-03 | BUILD | open | stores rise without bound (§1.4) | build |
| CP-T08-02 | BUILD, ships `uniform` | open; **gate and key amended** | 8 of 37 settlements in no polygon | R-SE-01, R-SE-03 |
| CP-T08-05, -06, -07, -08, -10, -04 | BUILD | open; each inert until stock and difference exist | §3 | after `ground` |
| CR-08 | BUILD | open; **specified** | — | R-SE-05 |
| CR-22 | MEASURE then BUILD | open; **rule amended** | `se_bind.py` | R-SE-02, R-SE-03 |
| CR-49 | BUILD | open | `exchange` 0 of 79 | extend the class to `transfer` and `migrate` (R-SE-19) |
| SE-04 (b) | held on IN-44 | open | `Rung.envelope` unwritten | delete (NERS cut, §5) through IN-44 |
| SE-06 | held | open; re-bases on CR-107 | — | none |
| CR-106, CR-107 | BUILD, content held | open | — | CR-107's weights are where cohorts stop being uniform |
| CR-67 | design-first | open | — | after CP-T08-05 |
| CP-T08-09 | withdrawn | closed | — | none |
| `HANDOFF_SE` Open row 1 | producer waits on ED-IN-0297 | **stale** | AM-E-15 | R-SE-13 |

### 6.2 Inconsistencies, gaps and unclear passages: decided resolutions

| id | what | resolution | ladder step | carried by |
|---|---|---|---|---|
| R-SE-01 | CP-T08-02 derives a ground class from terrain polygons that leave 8 of 37 settlements unclassified and cannot tell the breadbasket from the capital | the endowment is authored per territory in `rosters.yaml: site_endowment`; `ground_class` is not built | 5 | `07_SE_ground_and_granaries.md` |
| R-SE-02 | every larder is empty at build; CR-22's floor rule leaves "stock the larders" as an alternative | world-gen stocks one season of yield per settlement and a granary per territory | 4 (CR-22's own branch) | same |
| R-SE-03 | AM-E-13 gates the `ground` flip on a relief path a uniform realm cannot show | the gate is a draw whose `source` is a territory rung, with a stated runway | 5 | same |
| R-SE-04 | hunger's body loss scales with headcount (H-305) | per head: `body_step × short // weight` | 5 | `07_SE_population_census.md` |
| R-SE-05 | CR-08 names a writer and no arithmetic; a cohort dies whole | thinning at CENSUS under the `withdrawal_only` floor, death only at weight 1 | 3 (CR-08, M6) | same |
| R-SE-06 | a settlement with no cohort reads `fed` | `hunger_bands` gains `empty` | 5 | same |
| R-SE-07 | a store move accepts −5, 0, 2.5 (H-306) | one predicate at the owner of every move; the effects decline | 5 | `07_SE_kernel_repairs.md` |
| R-SE-08 | a wear of 0 emits `condition.worn` | no write where nothing wears | 4 (claim decay, same file) | same |
| R-SE-09 | a same-place `move` is travel (H-140) | declines, as `migrate` does | 4 | same |
| R-SE-10 | arrival teaches nothing (H-327) | the `travel.ended` write carries what was seen | 4 (`_stock_report`) | same |
| R-SE-11 | a partly stocked rung blocks the walk (H-303) | the walk continues for the remainder, behind a fixture | 5 | `07_SE_ground_and_granaries.md` |
| R-SE-12 | `systems/settlements/__init__.py` names the wrong reader | corrected | 1 (superseded by `data/geography.py`) | `07_SE_kernel_repairs.md` §6 |
| R-SE-13 | `HANDOFF_SE` Open row 1 waits on a closed ED | corrected | 1 (AM-E-15) | same |
| R-SE-14 | `requirements.yaml`'s settlement scale note says `restore` executes | re-read at this commit | 1 | same |
| R-SE-15 | `populated.py:1229` says nothing reads a dwelling | corrected | 1 | same |
| R-SE-16 | H-105 and H-171 cite `restore` executing in the realm | both cites gain the reading "0 attempts, seed 0, three seasons, this commit; cause not isolated" | 3 (the register is the record) | a register edit; no proposal file |
| R-SE-17 | H-309: a seat holder who migrates keeps the seat, *"intent undetermined"* | he keeps it. A seat is a `hold` exercised `via`; `revoke` and `confer` end it; absence is not an act. The absentee is story the engine already carries (his men's terms lapse if he does not pay) | 4 | a register edit (close the row) |
| R-SE-18 | H-168 says `migrate` executes only from hand-built acts | false since IN-45; cite re-read | 1 | a register edit |
| R-SE-19 | `transfer`'s `to` binds the question's referent, so a giver gives to himself or to a person-rung | `referent_class: Rung` and the `to != from` decline CR-49 gives `exchange`, on the `transfer` and `migrate` rows too | 4 (CR-49) | a plan edit to CR-49; CHAR cross-list |
| R-SE-20 | `Rung.envelope` is declared, unwritten and unread | delete, through IN-44's Layer-1 row | 2 (irrelevant: its subject was never built) | no proposal; IN-44 |
| R-SE-21 | a cohort's weight is 2 everywhere (H-170: *"a number nobody chose"*) | weights differ by authored row under CR-107; until then the shipped 2 stands. The archived design's size ladder (`settlement_layer_v30.md` §1.8: Seat, City, Cathedral 3; Town, Fortress 2; Village 1) is intent for the spread, not a source | 3 (CR-107 owns it) | none |
| R-SE-22 | `provision`'s ration is a `min` over every eaten kind, so a grain-only treasury fields nobody | at the flip, a kind the treasury does not hold bounds as 0 only if `subsistence_weight` gives it a weight and the fixture `field_ration_kinds` lists it; shipped list `[grain]` | 5 | folded into IN-52's flip entry; no file |
| R-SE-23 | settlement-scale case worlds hold no eater | a `world:` overlay block | 4 (`cast:` overlay) | `07_SE_arc_needs.md` |
| R-SE-24 | every computed store move is 1 unit | `amount` joins `choice_sourced` | 4 (`marshal`) | same |
| R-SE-25 | no settlement verb reads a capability; `f(degree)` is the identity (H-164) | `rate` beside `faculty`, one table | 4 | `07_SE_capability_and_chooser_surface.md` |

Twenty-five resolutions decided. Two items survive the ladder (§11).

(sections 7 to 14 appended below)
