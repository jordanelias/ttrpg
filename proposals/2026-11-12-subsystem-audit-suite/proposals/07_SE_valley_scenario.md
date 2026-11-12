# 07 · SE — the settlement game as a scenario: three towns, one granary, one seat

Reconciled: 2026-11-12, U5d closure — folded **A-54**, **A-50** and **A-56**. The scenario's seasons draw their harvest on the four-band ladder with the steward's skill as named levels on the place's draw (wave 3, D-U1-09, replacing "in the pool"), so the player's stewardship is felt as odds; its three towns' starting stores may be drawn within the fixture's bounds; its cohorts form the heavy moves only, so a starved town answers by petition, flight, refusal or riot. The P-13 change stands (the granary at the steward's seat rung).

Reconciled: 2026-11-12, wave 3 (W3-3) — D-U1-09 applied to the head's A-54 phrase (the steward's skill is named levels at site `settlement_effect`, not a pool term); 7b-7 (a named pytest file for the loader's refusals and the gate's three readings, the CLI commands kept as the readable form); tier and batch added (R3 7b-0; U3 B12, last). R3 §1's question whether "one code path" is met by sharing `SeasonDriver` only is answered by the file as written: the valley runs the unmodified driver, the registered entries and the shipped chooser, and a played seat is the existing `dispatching_chooser`, `[ASSUMPTION: U3 left no row on it — basis: CLAUDE.md §0 "one code path" names the loop, which is shared]`.

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), last in U3 §1 item 13.
Depends on: nothing proposed for the build; its `field` towns wait on `07_SE_ground_and_granaries.md` (B12, the `field` site kind), its weight readings on `07_SE_population_census.md` (B12).

Carries finding F-SE-13 and §9 of `audits/07_SE_audit.md` (the standing requirement: playable alone, one
code path, integrated). It proposes a scenario seed and its printer, built from parts that exist. It is
not a new subsystem, driver or module, and it adds no rule: every rule it exercises is the season loop's.

## 1. What changes in `engine/season/` at runtime

Nothing in the loop, the modules or the realm. Two files are added beside their precedents:

- `engine/season/valley.yaml` — an authored small world (the precedent is `governance_spine.yaml`: a
  fixture world as data, read by one harness builder, bannered *a test fixture, not canon*).
- `engine/season/harness/valley.py` — `build(seed)`, `run(seasons, seed, play=None)`, `sheet(w)` and a
  `main` (the precedents are `harness/scarce.py` and `harness/governance_spine.py`).

The scenario runs the unmodified `SeasonDriver`, the registered `settlements.*` entries and the shipped
chooser. A played seat is `harness/play_surface.dispatching_chooser(auto, {pid: callback})`, the existing
single-player hook, so the played and the automated valley are one code path by construction.

## 2. The problem, with evidence

A settlement cannot be played today, alone or in the realm, in the brief's sense (*a situation, real
choices, choices that change what happens, consequences, an ending*):

| element | state at this commit | evidence |
|---|---|---|
| scenario seed | `harness/scarce.py`: two settlements, one cohort, one steward; hand-built in Python; *"every id and number below is chosen to make one chain observable"* | `scarce.py:1-40` |
| choice surface | the steward is offered what the chooser forms; in four seasons he forms one useful `transfer` (8 salt) and three `transfer`s from the granary to itself | `python -m engine.season.harness.scarce`, named arm |
| change | the one transfer feeds one kind for one season; grain demanded 20, delivered 0 at ticks 1 to 3 while his granary holds 139 to 216 | same run |
| consequence | the cohort's body falls; nothing else reads it (no weight, no yield, no unrest, no seat at risk) | `subsist.py`; `produce.py` reads no person |
| legibility | per-tick lines printed by `scarce.main`; no reason is shown for an act not taken | same run |
| end condition | none; `run(seasons)` stops at a count | `scarce.py:182` |

The realm is not a substitute: its economy is unmoved by play (2 units of 13,690 in three seasons at
seed 0, 4 at seed 1).

## 3. The resolution, decided

One scenario that makes each of the settlement layer's consequence paths bind inside eight to twelve
seasons, sized so a reader can hold it entire:

- **Three settlements under one territory rung**, endowed unlike: a field town (grain), a harbour town
  (salt, a little grain), a seam village (ore and timber, no food).
- **Three cohorts of unlike weight** (4, 3, 2), within each place's dwelling count.
- **A territory rung holding a granary** worth four seasons of the village's want, and one territory
  seat (`remit: [issue]`, so `requisition` and `transfer` are his `via` it) whose holder lives at the
  field town. He is the played seat when `play` names him, the chooser's otherwise.
- **Two named residents with their own ends**: a reeve at the harbour town who holds it, and a miller
  at the field town with a planned `works` (a second field) and no seat. They give the steward's
  choices someone to cost.
- **Stakes that exist in code today:** bodies, deaths, the granary's level, the renewal of the steward's
  sworn men's terms (`_renewals`), the works' ripening terms. With `07_SE_population_census.md` built,
  weight as well; with `07_SE_ground_and_granaries.md`'s walk arm, the village's reach to the granary.
- **End conditions**, read by `sheet`, never decided by the loop: `lost` when any settlement reads
  `empty` (or, before the census proposal lands, when a cohort dies); `held` when twelve seasons pass
  with none; the run stops at whichever comes first. They are a scenario's reading, on
  `endings_reached`'s precedent (`world_q.py:2619`), not a win rule in the engine.

## 4. The exact edits

**(a) `engine/season/valley.yaml`** (structure; every number is the scenario's, `[ASSUMPTION]`):

```yaml
meta: {authority: "A TEST FIXTURE, NOT CANON. Three places and one seat, sized to make the settlement layer bind."}
territory: {id: terr_valley}
settlements:
  - {id: set_field,   sites: [field, field],  dwellings: 5, stores: {grain: 80, salt: 6}}
  - {id: set_harbour, sites: [harbour],       dwellings: 4, stores: {grain: 10, salt: 30}}
  - {id: set_seam,    sites: [seam],          dwellings: 3, stores: {ore: 50, timber: 10}}
granary: {rung: terr_valley, stores: {grain: 16, salt: 8}}
cohorts:
  - {rung: set_field, weight: 4}
  - {rung: set_harbour, weight: 3}
  - {rung: set_seam, weight: 2}
seats:
  - {id: off_steward, rung: terr_valley, remit: [issue], holder: p_steward, lives: set_field, obligees: 2}
persons:
  - {id: p_reeve, lives: set_harbour, holds: set_harbour}
  - {id: p_miller, lives: set_field}
planned_works:
  - {id: works_second_field, kind: works, plan: field, at: set_field, rung: set_field, master: p_miller, terms: 3}
```

Until `field` is a site kind (CP-T08-02), the file uses `harbour` for the field town and the scenario
still differentiates the seam village; the loader refuses a kind `rosters.yaml: site_kinds` does not hold,
so the file cannot run ahead of the roster.

**(b) `engine/season/harness/valley.py`** (structure and interface):

```python
def build(seed: int = 0, fixtures=DEFAULT_FIXTURES) -> World: ...
    # reads valley.yaml through data/files.py's anchor and load_yaml; mints rungs, Sites, cohorts, the seat,
    # the two residents and the works through the same constructors scarce.governed and
    # populated.mint_planned_works use (create_record's own effect for the works).
def sheet(w: World) -> dict: ...
    # per settlement: hunger band and cover (world_q.hunger), stores, cohort weight and body,
    # population/capacity; the granary's stores; the steward's live sworn terms; `ending`: None | "lost" | "held".
def run(seasons: int = 12, seed: int = 0, play: Mapping[str, Callback] | None = None) -> dict: ...
    # SeasonDriver(w); choose = dispatching_chooser(P.chooser(w, verbs=resolvable_verbs()), play or {});
    # one season at a time; appends sheet(w) and the season's acts by the steward, the reeve and the miller
    # with each act's Event kinds and `observed`; stops at an ending. Returns the series and content_hash.
def main(argv=None) -> int: ...
    # python -m engine.season.harness.valley [--seasons N] [--seed S] [--policy hoard|relieve|auto]
```

`--policy` is the headless player-proxy: two `Callback`s shipped in the file, each choosing among the
candidates the chooser already formed (`sheet.py`'s development space ranks and selects, never forms):
`relieve` takes any candidate `transfer` or `requisition` whose `to` is the granary or a settlement in a
band below `fed`; `hoard` refuses every such candidate. `auto` is the shipped chooser (the control).

**(c) No other file.** `data/files.py` gains the path constant `VALLEY_YAML`.

## 5. The gate, and the falsifier

- **Execution artifact.** `python -m engine.season.harness.valley --seasons 12 --seed 0 --policy X` for
  the three policies, seeds 0 to 2. The scenario **plays** when: (i) `hoard` and `relieve` end
  differently at every seed (a different ending or, at equal endings, a different season of first
  death); (ii) `auto` matches neither exactly at some seed; (iii) every season's sheet names, for each
  act the steward took, the Observation it was formed from.
- **Falsifier.** If `hoard` and `relieve` produce one content hash, a player's choice changes nothing
  and the settlement layer does not play, whatever resolves. That reading is the finding, and it is
  reported, not tuned away (scripting drift is a failure of the test). At this commit it is the
  expected first reading: the candidates `relieve` needs are formed once per crossing (H-160 limit 3,
  ruled a balance number) and name one kind.
- **Control.** `--policy auto` twice at one seed gives one hash.
- **Named tests (7b-7).** New file `engine/season/tests/test_valley.py`: `test_auto_twice_gives_one_hash`,
  `test_valley_yaml_refuses_a_site_kind_the_roster_lacks`,
  `test_hoard_and_relieve_end_differently_or_the_finding_is_reported` (asserts that it asserted over the
  three seeds; a same-hash result is reported, not failed, per the falsifier above).

## 6. NERS reading

- **N.** Cut it and the standing requirement has no instrument for this subsystem: the realm cannot show
  a settlement decision and `scarce` shows one chain once.
- **R.** It is the smallest world in which whom to feed is a choice with a loser, and it runs with
  nobody playing (`auto`).
- **S.** It enters from the season (the same driver), pauses nothing, and its outcome is ordinary world
  state other subsystems read: a field fought in this valley reads the same treasuries and walls.
- **E, last.** One data file and one harness of the size of `scarce.py`.

## 7. Cost class

Small build. No hash moves: nothing shipped reads the new files. Tier: `sonnet` (harness; R3 7b-0).
