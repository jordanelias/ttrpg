# 21 · PROCEDURAL A — the world-generation switch, tables and sheet; ground drawn inside canon's bands

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05)

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.0–§4.3, §5, §6, resolutions R-21-02, -03, -13; plan
batches **PG-0** and **PG-1**. Builds on, and does not restate, `proposals/07_SE_ground_and_granaries.md`
(CP-T08-02: `rosters.yaml: site_endowment`, fixture `endowment_mode`) and
`proposals/07_SE_population_census.md`.

## 1. What changes in `engine/season/` at runtime

With `build_realm(variable=False)` (shipped): nothing; every hash is the base hash.
With `variable=True`: the realm's producing sites, starting stores, garrison condition, cohort weights
and each territory's climate base rates are drawn from tables by the world seed, inside the bands canon
and the SE lane's endowment rows set. Two seeds then build two different realms. A realm that fails the
invariants raises; one that fails the story-possibility bars is redrawn.

## 2. The problem, with evidence

- `build_realm(seed)` takes a seed and draws nothing from it. Probe P1 (audit §12): at seeds 0, 1, 2 the
  rungs, persons, names, pursuits, sites, site conditions, stores and offices are equal; two `hold` tenure
  ids and `world_seed` differ.
- 37 of 37 settlements carry the site signature `(garrison, harbour, seam)` and empty stores
  (`harness/populated.py:1215-1261`: one site per producing kind per settlement, every site at full
  `condition_scale`); every cohort is `weight: 2` (`cohorts.yaml`).
- Canon already differentiates the places and the build does not read it: 14 distinct `stats` triplets
  across 37 settlements, per-territory `starting_pros`, `poi_catalog`, terrain and water
  (`systems/settlements/valoria_geography_v30.yaml`); the build reads `type`, `territory`, `faction`.
- Consequence, measured by the SE lane: no scarcity, so no exchange, requisition, hunger band crossing or
  migration in computed play (`audits/07_SE_audit.md` §0).

## 3. The resolution, decided

1. **A switch, not a rewrite.** `build_realm` gains `variable: bool = False`, on the `foreign` / `guards` /
   `cast_attributes` precedent: the off arm is the control, and each later batch that flips a default is
   its own declared mover.
2. **One pure planner.** `engine/season/data/worldgen.py::draw(seed, tables, canon) -> RealmPlan` returns
   data; `build_realm` mints from the plan with the constructors it already uses. The planner holds no
   `World`.
3. **Keyed draws through the existing owner.** `state/ids.py::H(world_seed, 0, entity_key,
   "worldgen:<generator>:<field>:<attempt>")`. No new RNG, no sequential stream.
4. **Endowment has one owner: the SE lane's.** `endowment_mode` gains a third value, `drawn`, over the same
   `rosters.yaml: site_endowment` rows. No second endowment table.
5. **Validation is part of generation:** V1 refusals in the loader and planner; V2 bars with redraw.
6. **A sheet and a range table** so a table edit is seen without a season run.

## 4. Exact edits

### PG-0 — switch, loader, sheet, stability

**(a) New file `engine/season/worldgen.yaml`** (typed; the authoring surface; every value
`[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`). Empty tables ship; the file's presence
changes nothing while `variable` is off.

```yaml
meta:
  authority: "AUTHORED FOR PLAY. Not canon. Read by engine/season/data/worldgen.py and nothing else."
  schema: 1
max_attempts: 8            # redraws on a V2 failure before the build raises
scenario:                  # THE ONLY BLOCK IN WHICH A ROW MAY NAME A FACTION, HOUSE OR PERSON (04 PART D row 27a)
  pinned_persons: []       # case ids that generation may not move, re-home or re-seat
ground: {}                 # PG-1
climate: {}                # PG-1
bars: {}                   # PG-1 onward
cast_quota: {}             # PG-2 (proposal B)
lifepaths: {}              # PG-2
relations: {}              # PG-2
local_seats: {}            # PG-3
prologue_seasons: 0        # PG-4 (proposal C)
```

**(b) New module `engine/season/data/worldgen.py`** (beside `data/cast.py`; one read per process, that
module's idiom; `load_yaml`'s duplicate-key refusal). Typed interface:

```python
@dataclass(frozen=True)
class SitePlan:      settlement: str; kind: str; condition: int            # geography code; SITE_YIELD kind; on condition_scale
@dataclass(frozen=True)
class StorePlan:     settlement: str; kind: str; amount: int               # an existing stores kind; a non-negative int
@dataclass(frozen=True)
class CohortPlan:    settlement: str; weight: int; stance_seed: int        # Person.weight; a stance value toward the holder
@dataclass(frozen=True)
class ClimatePlan:   territory: str; rates: Mapping[str, int]              # per-territory base rates the MATTER draws read
@dataclass(frozen=True)
class RealmPlan:
    seed: int; attempt: int
    sites: tuple[SitePlan, ...]; stores: tuple[StorePlan, ...]
    cohorts: tuple[CohortPlan, ...]; climate: tuple[ClimatePlan, ...]
    poi: Mapping[str, tuple[str, ...]]                                     # territory -> settlement codes its points of interest lie at
    persons: tuple = (); seats: tuple = (); cards: tuple = ()              # filled by proposals B, C, D

def load(text: str | None = None) -> dict: ...                             # schema-checked tables; each refusal names the row
def pick(seed: int, key: str, purpose: str, weights: Mapping[str, int], attempt: int = 0) -> str: ...
def spread(seed: int, key: str, purpose: str, lo: int, hi: int, attempt: int = 0) -> int: ...
def draw(seed: int, tables: dict, canon: dict, fixtures, attempt: int = 0) -> RealmPlan: ...   # pure; no World
def invariants(plan: RealmPlan, canon: dict) -> list[str]: ...             # V1: empty list or the defects, each naming a row
def possibility(w) -> dict[str, int]: ...                                  # V2: counts of armed situations in a BUILT world
```

`pick` and `spread` are the only two draw forms. Both reduce the hex digest of
`H(seed, 0, key, f"worldgen:{purpose}:{attempt}")` to an integer; `pick` walks cumulative integer weights
in sorted-key order (so file order is not an input), `spread` returns an integer in `[lo, hi]`. Neither
ever returns "the largest weight".

**(c) `engine/season/harness/populated.py::build_realm`** gains `variable: bool = False` and, when true,
calls `worldgen.draw` once before the site loop and mints from `plan.sites`, `plan.stores`,
`plan.cohorts` instead of the uniform loops at `:1215-1220` (producing sites), `:1258-1261` (garrison
condition) and `seat_cohorts`'s rows. On a V1 defect: raise, listing the defects. After the build, if
`bars` is non-empty: `possibility(w)`; on a miss, rebuild with `attempt + 1`; after `max_attempts`, raise
naming the bars missed and the counts reached.

**(d) New `engine/season/harness/worldgen.py`** (an instrument; no loop step imports it):
`--seed N --sheet` prints, per territory and settlement, the canon band, the drawn value and the live
query beside each other (sites, conditions, stores, cohort weight, expected yield against expected draw),
then the V2 counts; `--range N` builds seeds `0..N-1` (build only, about 1.4 s for three builds today,
audit P1) and prints, per metric, min, quartiles and max, and the rejection rate.

**(e) Tests** (`engine/season/tests/test_worldgen_switch.py`; each executes the build):
- `variable=False` reproduces the pinned realm hash at seeds 0, 1, 2;
- with one filled table, `build_realm(0, variable=True)` and `build_realm(1, variable=True)` differ in at
  least one site or store (the assertion that asserts it asserted: it counts the differing settlements and
  requires at least `N`);
- **stability under a table edit:** plant a table with one extra optional kind on one territory; every
  settlement outside that territory draws exactly what it drew before (the property keyed draws buy, and
  the falsifier for it);
- same seed twice: equal plan, equal hash.

### PG-1 — ground, endowment, climate, points of interest

**(f) `engine/season/rosters.yaml: site_endowment`** (the SE lane's table; this edit extends each ground
row, it does not add a table). Each row gains two optional keys:

```yaml
site_endowment:
  ground:
    T2:
      kinds: [field, ford]            # the SE lane's: what this ground always gives
      optional: {seam: 1, orchard: 2, none: 3}     # NEW: at most one more kind, by keyed draw over integer weights
      spread: 200                     # NEW: half-width, on condition_scale, of the starting-condition draw
```

The kind names above are illustrative (the producing kinds built today are `harbour` and `seam`; the SE
lane's proposal names the rest). A kind named in `optional:` must be a `SITE_YIELD` kind or `none`; refused at import otherwise, naming the
row (the `_check_arms_at_build` idiom).

**(g) `engine/season/data/fixtures.py`**: `endowment_mode` gains the value `drawn` (swept
`uniform / ground / drawn`). `endowment_for` is unchanged; `worldgen.draw` calls it for the fixed kinds and
adds the `optional:` draw (`pick(seed, settlement_code, "endowment:optional")`).

**(h) `engine/season/worldgen.yaml: ground, climate, bars`:**

```yaml
ground:
  stores_seasons_by_P: {1: [0, 1], 2: [1, 2], 3: [1, 3], 4: [2, 4]}   # canon stats[0] -> seasons of own yield in store, [lo, hi]
  garrison_by_D:       {0: [200, 500], 1: [400, 700], 2: [600, 900], 3: [800, 1000], 4: [900, 1000]}   # canon stats[1] -> condition band
  cohort_weight_by_type: {Village: [1, 2], Town: [2, 4], Fortress: [1, 2], City: [4, 6], Seat: [4, 6], Fortress-City: [3, 5], Cathedral-City: [3, 5]}
  cohort_stance_by_O:  {0: [-2, 0], 1: [-1, 0], 2: [-1, 1], 3: [0, 1], 4: [0, 2]}   # canon stats[2] -> stance seed toward the holder
  poi: by_draw          # each territory's poi_catalog counts are placed on its settlements by keyed draw; `none` leaves them unplaced
climate:
  by_terrain:           # base rates per season, integers per thousand, read by the MATTER weather draw (09_WR_B_weather…)
    lowland:  {poor_yield: [80, 160],  illness: [20, 60]}
    upland:   {poor_yield: [140, 260], illness: [20, 50]}
    coastal:  {poor_yield: [60, 140],  illness: [40, 90]}
bars:
  deficit_settlements: 3   # settlements whose expected yield is under their cohort's draw AND that border a surplus settlement
  aggrieved_cohorts: 3     # cohorts with a negative stance toward a holder who can be petitioned
```

Every key in `*_by_P`, `*_by_D`, `*_by_O` must cover every value canon's `stats` uses; refused otherwise.
The terrain keys must be the terrain classes the geography file declares (the loader reads the file's own
set; the three above are placeholders to be replaced by that set at build of the batch).

**(i) `build_realm`**: under `variable=True` and `endowment_mode == "drawn"`, stores are set to
`spread(…)` seasons of the settlement's drawn Sites' base yield (the SE lane sets exactly one season under
`ground`); garrison and site conditions from the bands; cohort rows from `plan.cohorts` (the authored
`cohorts.yaml` rows remain the off arm); `plan.climate` is written where the WR lane's weather proposal
reads its base rate (that proposal names the owner; if it has not landed, `climate` is drawn, shown on the
sheet and read by nothing, and the sheet says so).

**(j) `possibility(w)`** computes `deficit_settlements` from `world_q.subsistence_draw` and `SITE_YIELD`
(existing readers), `aggrieved_cohorts` from cohort stance rows and `world_q` seat scope.

## 5. Gate (execution artifacts)

- **PG-0:** the four tests of (e); `python -m engine.season.harness.worldgen --seed 0 --sheet` prints the
  shipped realm with every drawn column empty (the off arm is legible).
- **PG-1:** `--range 20`: 20 of 20 seeds pass V1; rejection rate printed and under one in five; distinct
  settlement signatures per world at least 10 (today 1); scarcity index (deficit settlements) has a
  non-zero range across seeds. Control: `optional` absent and `spread: 0` gives the SE lane's `ground`
  hash exactly. Play: 3 seeds × 3 seasons, at least one of `exchange.made`, `requisition.taken`, a hunger
  band crossing or an executed cohort `migrate` per world (today: none in any, `07_SE_audit.md` §0),
  against the `uniform` arm run the same way.

## 6. Falsifiers

- If two `variable=True` seeds build equal sites and stores, the planner is not reading the seed.
- If a table edit on one territory moves a draw in another, the draws are not keyed.
- If under `drawn` no world shows want in three seasons while `ground` does, the spread is washing out
  the SE lane's differentiation and the bands are wrong.
- If the rejection rate is high, the bars are doing the generator's work; edit the tables.

## 7. NERS reading

- **N:** cut it and every world is the same world; the kernel the SE lane audited keeps nothing to account
  for; no later generator has a differentiated place to put a person in. The cut is not free: the SE
  lane's `ground` arm gives differentiation between *places* but the same differentiation in every
  *world*, which is the sameness Jordan's content suite named.
- **R:** variety with no player in it (which valley is short this year); customization by table; the
  mechanism is complete at its extremes (an empty table is the off arm; a table that cannot produce a
  valid world raises).
- **S:** one draw owner, the engine's own scales, the SE lane's one endowment table; pauses nothing; the
  sheet zooms from realm to settlement.
- **E, last, as a ratio:** one module, one file, one parameter and one instrument against a realm that
  differs by seed and can be tuned without touching code.

## 8. Cost and dependencies

PG-0 small build, depends on nothing. PG-1 small build, after `07_SE_ground_and_granaries.md` (the
`site_endowment` table and `endowment_for`), CR-22 (hunger binds) for the play half of the gate, and
`09_WR_B_weather_with_memory_and_the_year.md` for a reader of `climate`.
