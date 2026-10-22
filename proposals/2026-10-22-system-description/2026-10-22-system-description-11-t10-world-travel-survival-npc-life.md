# Tutorial: World, Travel and Survival (WT) and NPC Life (NP) — where a person stands, what it costs to go elsewhere, and how a person keeps the people around them alive, trained and on good terms

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`; revised in round 3 against `51d7b05` and the precedent suite
(`research/game_precedent_suite/`; the dispositions are `dispositions/D_T10.md` and `D_T10_also.md`). Text added or replaced in round 3
cites the tree at `51d7b05`; cites I did not touch are still at `a4ca9a5`, and PR #494 moved them: `world_q.py` +3 for lines 46–1676 and
+125 from line 1739 (e.g. `places_named` 1986 → 2111), `person_q.py` +2 for lines 58–416 and +90 above, `fixtures.py` +10 above line 715,
`rosters.yaml` +66 above line 2488. Paths are relative to the repo root; `es/` stands for `engine/season/`. The run figures are
taken from `ctl/realm_seed{0,1,2}_2seasons.txt` (the control run: `build_realm(seed)`, 2 seasons; "ok" means the act produced at least one
event that is not a refusal) and from my own read-only probes over the same recipe (§9).

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that spends a budget of scene actions each season
(5 by default, more for each office or held document, less when wounded or travelling) on acts from a closed table of verbs, and the
engine resolves them. "You" in this tutorial means the person acting: a player's character if one is ever
seated, an NPC today. So the tutorial teaches (a) what a person can do here, (b) what the rules do with it, and (c) what a person has to
arrange to reach a goal. Rules that exist only in proposals are marked **[PROPOSED]** and kept in §7.

**What you need from other subsystems.**
- *The season loop* (CALENDAR → MATTER → 5 rounds of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS → CENSUS). MATTER is the actorless
  clock that eats, yields, wears and ends journeys. WITNESS is how anyone learns anything, and it delivers by co-location.
- *Economy* (EC): `Rung.stores` and the yield of harbour and seam Sites are the larder your settlement eats from.
- *Personal combat* (PC) and *mass battle* (MB): they are the only things that lower a `body` in a shipped season, and `march` is the
  only runtime writer of grudges besides `forgive`.
- *Settlements and governance* (GV): offices (live `hold` Tenures) raise your scene budget; `capacity` counts dwelling Sites.

**Status, one line.** WT: the containment ladder, presence, `move`, the leg cost and MATTER's leg end are **RUNS-IN-LOOP**. `migrate` is
**TESTS-ONLY** (0 successes in 81, 143 and 143 acts that reached the fold, seeds 0–2). Weather, hunger, ageing and illness are **RUNS-IN-LOOP at control**
(they run and do nothing at shipped values). Routes, terrain, exposure, POIs and foraging are **DESIGN-ONLY** (the data exists and no
season code reads it). NP: cohorts, named persons, body bands, regard and `forgive` are **RUNS-IN-LOOP** (`forgive` executes at seeds
0, 1 and 2). `tend` and `train` are **TESTS-ONLY** at every seed. `give` executes at seed 2 only (1 of 19), and `commit` at seeds 1 and 2
only (1 each); both are TESTS-ONLY at seed 0. Kin, birth, marriage, household and inheritance are **DESIGN-ONLY** or absent. Grades follow
ERRATA G1 only, applied per seed: a refusal firing is not the verb executing.

## 0a How it plays

The lane as a run of the built game, then what is proposed. Figures are seed 0 of the control run unless they name a seed
(`ctl/realm_seed{0,1,2}_2seasons.txt`, re-run at `51d7b05`; count columns are *reached the fold / ok*, as in §4). The form follows the
precedent tutorials' "how it plays" sections (`research/game_precedent_suite/tutorials/`, tier 3, reference only).

**Setup choices.**
- *At world build* the one choice is the seed, `build_realm(seed)` (`ctl/control.py:7`). It fixes 83 persons (37 cohorts of weight 2, 46 named),
  37 settlements and 211 hearths (§1); every body starts at 1000 and every person has `born` 0 (`fixtures.py:608`, `carriers.py:687`).
- *The survival controls are fixtures, not choices*: `body_step` 0, `age_step` 0.0, `illness_rate` 0.0, `season_factor` 1.0 with an empty draw
  table (`fixtures.py:463, 469, 594, 606-607`). Their swept arms run only in tests (`fixtures.py:591-593`).
- *At the callback*: the season loop has no player interface. `dispatching_chooser` hands the persons in its `overrides` map to a callback
  that returns their Acts or Scenes (`play_surface.py:41-52`; TESTS-ONLY). It can name any rung as a destination and any of the 47 resolvable
  verbs with any payload: hand-built `migrate` (to an empty hearth), `tend` (on oneself) and `march` (at a settlement) each ran through the
  season loop at `51d7b05`. Outside the loop, `systems/social_contest/sim/contest/agon_harness.py` is a stdin-driven human-played social
  contest, and two HTTP designer workbenches exist (`systems/combat/combat_engine_v1/workbench/server.py`,
  `systems/mass_battle/sim/workbench/server.py`).

**The loop** (one season = one tick; all of it automated).
1. CALENDAR.
2. MATTER, in file order: claim decay 5 (`matter.py:317-347`, ERRATA G8) and standing crossings (`:351`); season factor (`:364`); larder draw,
   cohorts only (`world_q.py:1020`); hunger to body, skipped at `body_step` 0 (`matter.py:520`); ageing and illness, skipped (`:549`); debit and
   yield (`:560-606`); legs end (`:643-655`); wear 10 on harbour and seam (`:657-691`).
3. Five rounds (`driver.py:449-456`): DELIBERATE recomputes each budget (`budget.py:57-61`) and releases one scene, charging it
   (`deliberate.py:252-260`); RESOLVE folds; ENCOUNTER fights fields; WITNESS deposits by co-location and, for binding-decision kinds, to everyone (the chronicle channel,
   `epistemic.py:649`; ERRATA C5).
4. CENSUS individuates demanded persons (`census.py:35`); the season then reports `endings` (`driver.py:514-518`).

**The choice menu.** Candidates are scored by pursuit alignment plus stance toward the subject and ordered with Gumbel noise at τ 0.1
(ERRATA G12). The larder term (`urgency` of `Sensation.subsistence`, which in the realm run is the harness's home-stores formula, `harness/probes.py:144-149`,
not a body or hunger state) is added identically to every candidate (`choose.py:448, 452-453`), and a constant shift cannot reorder an ordering by
score/τ plus Gumbel noise (`:388`), which is all `pack_scenes` receives (`:481`). Room is not read when a choice is formed (`world_q.py:2126-2129`).

| verb | cost | effect | when a person picks it | grade (seeds 0, 1, 2) |
|---|---|---|---|---|
| `move` | one act; −1 point per leg until the next MATTER (`budget.py:60`) | `contain` moves, leg recorded (`effects_migration.py:91-119`) | the question's referent is a rung; a person rung or a non-rung is formed and refused | RUNS-IN-LOOP (16, 17, 12 executed; at seed 0 all to where the mover stood) |
| `migrate` | as `move` | `reside` moves if `population + weight ≤ capacity` (`effects_migration.py:203`) | his ledger names a rung he does not live under (`world_q.py:2111-2146`) or, for a seat-holder, a stocked larder his seat reaches (`world_q.py:2148`, spliced at `:2540-2545`) | TESTS-ONLY (0 of 81, 143, 143 that reached the fold) |
| `tend` | one act | subject's body to 1000 (`effects_combat.py:371-393`) | a living person "with" him, or himself | TESTS-ONLY (0 of 34, 22, 19) |
| `train` | one act | +1 in a key the subject holds | a vocation key exists (only `copying`) | TESTS-ONLY (0 of 38, 30, 30) |
| `forgive` | one act | his negative rows on the referent deleted (`effects_combat.py:431-450`) | only when he holds such a row | RUNS-IN-LOOP (1, 2, 2) |
| `give` | one act | a held Record changes hands | he holds a Record, the receiver is with him | RUNS-IN-LOOP at seed 2 (1 of 19); TESTS-ONLY at seeds 0, 1 (`engine/season/tests/test_give.py`) |
| `commit`, `oblige`, `release` | one act each | open a commitment or a duty; close an own edge | a Proposition or seat in reach; any own live edge | `commit` RUNS-IN-LOOP at seeds 1, 2 (1 each), TESTS-ONLY at seed 0 (`engine/season/tests/test_in11_utter_hold_commit.py`); `oblige` RUNS-IN-LOOP at seed 1 (22 of 24), never reaches the fold at seeds 0, 2 (§4); `release` RUNS-IN-LOOP (3, 5, 3) |

**First season, step by step** (seed 0, tick 0 then tick 1).
1. Build: 83 persons; starting budgets 52 at 5, 27 at 6, 1 at 7, 2 at 10, 1 at 13; 47 live holds.
2. MATTER at tick 0: the cohorts want 148 grain and 74 salt and find nothing, each 6 units short; at `body_step` 0 no body moves; ageing is
   skipped; yield is taken (37 `yield.taken`, 37 `stores.changed`); no leg to end.
3. Rounds 0–4: 676 acts released and charged, 535 reach the fold. In this lane: `move` 18 (5 `travel.moved`, 13 `travel.blocked`), `migrate` 25
   (25 `migrate.refused`), `tend` 15 and `train` 23 (all refused), `forgive` 1 (`stance.moved`), `give` 8, `commit` 39 released and 36
   folded, `release` 26.
4. Combat (another lane) kills 5 named persons, the King (`p_npc_020`) among them; 4 `body.changed`; no cohort dies.
5. Live holds reach 121 by the season's end; budgets then spread from 3 to 11 (legs not yet cleared).
6. Tick 1: the draw is met from last season's yield; 5 legs end (`travel.ended`); 731 acts released, 597 resolved; `move` 24 (11 moved),
   `migrate` 56 refused, `tend` 19 refused; 4 more deaths. Two wounded survivors finish at 250 and 48, untended. Acts per acting person
   (act-store basis): 8.14, then 9.37, maximum 15.

**What changes later.** Budgets diverge: holders mint holds and reach the 15-act ceiling while the wounded fall toward 2–3 (`budget.py:57-61`,
§3a). Seats without a conferral basis empty and stay empty (§5c). Harbours and seams lose 10 condition a season (`rosters.yaml:1465-1470`), so
yield reaches 0 at tick 100 without `restore` (C9); grain cover of about 10 seasons is a separate stock-against-draw figure (C9). Also drifting:
larders grow (§3b: `set_s_001` 40/30/50/10 → 75/57/99/19 in two seasons), claims decay 5 a season (`matter.py:317-347`;
`claim_decay_per_season`, `fixtures.py:293`) and ledgers fill toward the cap of 200 (13 of 74 at the cap at seed 0, ctl). Not drifting: age,
births, stance and weather.

**Failure and ending.** The loop does not stop on an ending: the season reports `endings`, a read and never an actor (`driver.py:514-518`;
`world_q.py:1764`), and the realm as built reaches none (`endings` is `[]` in both seasons at seed 0). The only failure in this lane is death,
and at shipped values only combat kills (G9; `matter.py:520, 549`). Death is final and closes every tenure naming the dead (`world.py:645-656`);
nobody heals passively and nobody inherits (`verb_table.yaml:1113`). A settlement's cohort never starves at shipped values and its weight never
changes, but it can be deleted whole by one `Felled` (ERRATA C1). No cohort dies at seeds 0 and 1; at seed 2 one is gone by the end of season 2:
ctl shows `pursuits empty` 36 against 37 at seeds 0 and 1 with 72 alive, only cohorts have empty pursuits, and the 11 deaths are 10 named persons
and `cohort_set_s_029` (uncommitted round-3 probe; every death there is an `accept` or `fight`).

**Consequential vs cosmetic choices.**
- Consequential: holds (+1 point each, `budget.py:57`); wounds (−1 point per band, `budget.py:64-83`); a leg in an early round (one or two acts,
  §3a); where you stand (who sees you, whom "with" admits, where a cohort eats, §2.1); custody (closes every road, `effects_migration.py:52-53`).
- Cosmetic or dominated: a `move` to where you stand (16 of 16 executed at seed 0, §4); terrain, adjacency and POIs (no reader, §1); hunger and
  age (inert, and no score term lets hunger move a choice); `migrate` (0 of 367); `train` (0 of 98).

**As proposed** — every line **[PROPOSED]** (§7; ERRATA G16).
- [PROPOSED] Player seat: IN-47 makes a player one person's decision procedure ("embedded", G16), on the callback above; IN-46, the played
  fight, is T03's.
- [PROPOSED] Setup: a year and a storm season (M-WT-2); hunger live at `body_step` 10 [ASSUMPTION] with a settlement hunger Query (RB-5, JQ-6);
  ageing rates Jordan's (#457 D2).
- [PROPOSED] Loop and menu: route cost over `settlement_adjacency` × `terrain_cost_matrix` replaces the flat leg (M-WT-1); journey roll and
  exposure (M-WT-3, -4); `travel` (a same-place journey not formed, H-140), `explore`, `forage` (MB's), `tie`, `marry`, `hire`, `defect`,
  `succeed` (GV's), `pledge`.
- [PROPOSED] Recovery: passive recovery with announced upward crossings (M1, H-211) and a care degree (M2) would make a wound cost time.
- [PROPOSED] Failure and ending: none proposed in T10's sources. Births are ruled out for now (ED-WR-0011, §7; the cast is closed in the run, not by construction), so a death is answered by
  no birth; estate transmission at death is M11. Even with RB-5, hunger binds only before the first yield (G18, C9).

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **Rung** | A node of the one containment tree. Kinds: person, hearth, community, settlement, territory, province, duchy, realm. | Realm at build (seed 0): 1 realm, 3 duchies, 17 territories, 37 settlements, 60 communities, 211 hearths, 83 person rungs, **0 province rungs** | `es/rosters.yaml:256-259`; built at `es/harness/populated.py:715-760` |
| **person rung** | Every person is also a Rung of kind `person`, with the same id as the person. | 83 of 83 | probe (§9); `es/loop/census.py:103-106` mints one per new person |
| **Tenure** | The one edge type: a subject → object relation with a kind (`contain`, `reside`, `hold`, `commit`, `oblige`, `detain`, …), opened at `since` and closed at `until`. Live = not yet closed. | — | `es/state/carriers.py`; kinds `rosters.yaml: tenure_kinds` |
| **hold** | The Tenure kind for holding something: a seat (an **Office**), a landholding, a Record or a Proposition you made. | Every live hold adds 1 to your budget | `budget.py:57` |
| **Record** / **Proposition** | A Record is a document (a writ, a case, a forged paper). A Proposition is a statement something can be committed to; a faction is a `fac_*` Proposition. | — | `es/state/carriers.py` |
| **"with"** | The relation "two persons stand in the same place", read through `place_of` on presence. | — | `world_q.py:2716-2720` (`with` stem) |
| **ladder** (§10 ladder) | A rung may sit only inside a rung of a higher kind. `World.contain_ascends` asks the question. | A person can be contained by a hearth or higher, never by another person. | `es/state/world.py:301-324` |
| **root rungs** | Rungs with no parent. The realm is one. **Schoenland's territory T16 is a second**: as a foreign territory it gets no parent. | T16 holds one settlement, S-037, and its cohort | `populated.py:720-735`; `es/cohorts.yaml:101` |
| **province** | Not a stored rung. The geography file's `provinces:` key holds territories; a province is a Query. | 17 territory rows | `populated.py:720` ("geography's stale key"); `es/queries/world_q.py:1563 provinces_of` |
| **geography file** | Authored map: territories, settlements, `adjacency`, `settlement_adjacency`, `terrain_cost_matrix`, `march_budget`, water, bridges, Forgetting zone, radiation bands, `poi_catalog`. | 17 territories, 37 settlements, 26 territory edges, **55** settlement edges as loaded (the file's comments say 55 at :580/:589 and 56 at :602, and the block header says "24 primary + 1 sea" at :640), 11 terrain costs, 17 POI-count rows | `systems/settlements/valoria_geography_v30.yaml`; read by world-gen, and its `provinces:`, `terrain:` and `water:` keys by the mass-battle field (`es/data/geography.py:1-8`) |
| **Site** | A built place on a rung, with a `condition` (0..1000). | Seed 0: 211 dwelling, 37 harbour, 37 seam, 37 garrison | `rosters.yaml: site_kinds`; built by `populated.py` |
| **contain** (presence) | A Tenure edge person → rung: where you ARE. Witnessing, the larder draw and "with" read it. | One live edge per person | `es/state/containment.py:73 home_of` |
| **reside** (residence) | A Tenure edge person → rung: where you LIVE. Population and capacity read it. | One live edge per person (a second raises) | `world_q.py:1208 residence_of` |
| **travel_leg** | The list of destinations you travelled to this season. | Cleared at the next MATTER | `es/state/carriers.py:708`; cleared `es/loop/matter.py:643-655` |
| **population(rung)** | Sum of the `weight` of everyone who *resides* in the rung's subtree. | A cohort counts 2, a named person 1 | `world_q.py:1262` |
| **capacity(rung)** | `max(1, number of dwelling Sites in the subtree)`. | Hearth = 1; settlement 4–9; territory 8–23 (seed 0) | `world_q.py:1310`; floor `rosters.yaml:1498` |
| **season / tick** | `w.tick` counts seasons. There is no year: `season_of_year` is `None` while `season_factor_draw` is empty. | Shipped draw table `()` | `world_q.py:951`; `es/data/fixtures.py:469` |
| **season factor** (weather) | One multiplier per season on yield. | `season_factor=1.0`, draw `()` → always 1.0 | `fixtures.py:463,469`; `world_q.py:960`; sole caller `matter.py:364` |
| **Person** | Everyone is one carrier type. | 83 at build (seed 0) | `carriers.py:655` |
| **cohort** | A Person with `weight > 1`: "the people of" a settlement as one actor. | 37, one per settlement, weight 2, empty pursuits | `carriers.py:726 is_cohort`; `es/cohorts.yaml`; `populated.py:387 seat_cohorts` |
| **named person** | A cast member at weight 1, with pursuits, conviction, stance and offices. | 46 | `es/npcs.yaml`; built by `build_realm` |
| **body** | A person's physical condition on the same scale as `Site.condition`. | 0..1000, built at 1000 (`condition_scale`) | `carriers.py:679`; `fixtures.py:217` |
| **body bands** | Floors on the body: full operations ≥ 800, limited ≥ 500, withdrawal only ≥ 100. | penalty = number of floors your body is below (0–3) | `rosters.yaml:2562-2564`; `es/decision/budget.py:64-83` |
| **scene budget** | The **scene actions** you may spend this season: a *cost* budget, not a count of scenes ("Returns SCENE ACTIONS"). | `max(1, 5 + 1·live holds − body bands − 1·legs)` | `budget.py:19-20,57-61`; `fixtures.py:228,526-527` |
| **scene** | A packet of up to 3 acts (interactions). A one-act scene costs 1; a scene of 2–3 acts is **extended** and costs 2. If only 1 point is left, a chunk is trimmed to one act. | `interactions_per_scene=3`, `extended_scene_cost=2`; the driver releases 1 scene per round over 5 rounds (rounds 0–4) | `fixtures.py:488-489,511`; `es/decision/choose.py:643-668`; `es/loop/driver.py:449-456`; `deliberate.py:250-259` |
| **round** | One of the 5 passes of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS within a season, numbered 0–4. | `rounds = scene_budget` = 5 | `driver.py:449,456` |
| **larder draw** | At MATTER each cohort wants `weight × subsistence_weight[kind]` of each food, taken from the nearest rung up its *presence* chain that holds any. | grain 2, salt 1 per unit of weight; named persons do not eat | `world_q.py:1017-1046`; weights `rosters.yaml:1554-1556` |
| **body_step** | Body lost per unit of unmet food. | **0** shipped (swept 0 / 10 / 67) | `fixtures.py:594`; read `matter.py:513-534` |
| **age / hazard** | Age = `tick − born`; hazard = `min(1, illness_rate + age_step × age)`, cohorts exempt. | `age_step=0`, `illness_rate=0`, `age_at_build=0` | `world_q.py:985-1010`; `fixtures.py:606-608` |
| **stance** | Rows `(referent, valence −5..+5, weight 0..5)`; `stance_toward` sums valence × weight. | Grudge rows from a lost field: valence −1, weight 1 | `carriers.py:664`; `es/queries/person_q.py:68`; `fixtures.py:653-654` |
| **regard** | `stance_toward + judged_gain × judged deeds + told_valence_gain × told deeds`. | 0.5 and 0.5 | `person_q.py:390-410`; `fixtures.py:812,814` |
| **capability** | Dice count per key; "gates nothing". | Empty on 83 of 83 persons; one vocation key exists (`copying`) | `carriers.py:663`; ctl "capability nonempty 0" |
| **census individuation** | A `dispatch` naming an id that does not exist mints that person at the event's place. | weight 1, `contain` only, no `reside`; 0 in all three seeds | `es/loop/census.py:35-106` |

What is **data** and what is **read**: the geography file is read once, at world-gen, to mint the ladder (`populated.py:715-760`: duchies,
territories, settlements, then communities and hearths from `es/venues.yaml`). One more reader exists: the mass-battle field reads
`provinces:`, `terrain:` and `water:` through `es/data/geography.py` (lines 1-8), but no seeded season fights a field, so that reader is
TESTS-ONLY (`tests/test_mass_battle_module.py`). Nothing reads `adjacency`, `settlement_adjacency`, `terrain_cost_matrix`, `march_budget`
or `poi_catalog` (`grep -rn "adjacency\|poi_catalog\|terrain_cost" engine --include=*.py` finds only comments, §9). The world you travel
through is the containment tree, not the map.

## 2 How it works

### 2.1 Where you are and where you live

You hold two edges. `contain` says where you stand; `reside` says where your home is. They start equal at build (every one of the 83
persons has both). Three different things read them:

| reader | reads | consequence |
|---|---|---|
| WITNESS co-location, the "with" relation (`tend`, `train`, `give`) | `contain` | to be seen, or to act on someone, you must stand where they stand |
| larder draw (`subsistence_draw` → `home_of`) | `contain` | a cohort eats where it stands, not where it lives (`world_q.py:1027`, `containment.py:73`) |
| `population`, `capacity` throttle | `reside` | a crowd of visitors fills no house; only settlers do (`effects_migration.py:139-143`) |

### 2.2 Travelling: `move`

1. **The choice.** Your chooser forms a `move` Candidate with a destination `to`. Eligibility is `own` (you move yourself only)
   (`es/verb_table.yaml:863-877`).
2. **The precondition** `contain_path` asks whether your person rung and the destination share an ancestor (`es/data/requires.py:374-400`;
   `world_q.py:2704-2709`). A destination that is not a rung is UNKNOWN and refused. Any two rungs under the realm share the realm, so
   distance never matters. **The exception is Schoenland**: T16 is a root with no parent, so nobody outside it shares an ancestor with
   S-037, and nobody inside it shares one with the rest of the world. Every journey into or out of Schoenland is `travel.blocked`, and its
   cohort can never leave. The check compares the destination with your *person rung*, not with where you stand, so a journey to the
   place you already stand passes (H-140).
3. **Custody.** If you are held by a live `detain` Tenure, the effect declines (`effects_migration.py:52-53,73-88`).
4. **The ladder.** The effect asks `contain_ascends(you, dest)`. Because you are a `person` rung, a destination of kind `person` fails:
   you cannot travel "to a person" (`effects_migration.py:62-67`).
5. **The journey** (`_relocate`, `effects_migration.py:91-119`): your live `contain` edges close (`until = tick`), a new one opens to
   `dest`, and `dest` is appended to `travel_leg`. Your `reside` edge is untouched. Event `travel.moved`; refusals emit `travel.blocked`.
6. **The price.** From that point on, `budget()` subtracts `len(travel_leg) × budget_leg_penalty` (1) (`budget.py:60`). Every
   destination costs the same single leg.
7. **Leg end.** The next MATTER (the start of the next season) clears `travel_leg` and emits `travel.ended` (`matter.py:643-655`). Every
   journey is complete within its season; nobody is ever between places.

### 2.3 Settling: `migrate`

`migrate` is a `move` plus a change of home (`effects_migration.py:122-217`). After the custody and ladder checks it refuses (event
`migrate.refused`):
- a destination you already live in (`home == dest`);
- **a full destination**: if you are a newcomer (you do not already live under `dest`) and
  `population(dest) + your weight > capacity(dest)`.

If admitted, the journey runs (same leg, same price) and your `reside` edge moves; event `residence.changed`. The destination comes
from `places_named` (`world_q.py:1986`): rungs your own ledger names that you do not already live under. **Room is not read when the
choice is formed**, only at the fold, so a person can keep choosing a full hearth.

### 2.4 The season clock: weather, food, bodies

MATTER runs once per season, before anyone deliberates (`matter.py:165` onward). Seasons are named here by tick: the first MATTER
runs at tick 0, the second at tick 1. In order:

1. **Weather** (`matter.py:364`): `factor = season_factor × choice(season_factor_draw[season_of_year])`. With the draw table empty the
   factor is the bare 1.0. Its one reader is yield.
2. **The larder draw** (`world_q.py:1017-1046`; `matter.py:415-430`). For each cohort, for each food kind: `want = weight × weight_of_kind`
   (grain 2, salt 1). Walk up from the rung it stands in to the first rung holding any of that kind (`nearest_store`, `world_q.py:902`),
   take `min(want, held)`. Named persons are skipped: "the individual does not eat" (ED-IN-0255).
3. **Hunger to body** (`matter.py:513-534`): `lost = body_step × units short`; body falls by `lost`; a downward band crossing emits;
   at body 0 the person dies. At `body_step = 0` the loop hits `continue` and nothing moves.
   Even switched on, hunger enters no score: the chooser's larder term, `urgency(subsistence)`, is added identically to every candidate
   (`es/decision/choose.py:448, 452-453`), a constant shift cannot reorder an ordering by score/τ plus Gumbel noise (`:388`), and `pack_scenes`
   receives only that order (`:481`); the docstring at `:217-238` says the same, as reference. The term reads `Sensation.subsistence`, which in
   the realm run is the harness's home-stores formula (`harness/probes.py:144-149`). A short cohort's choices would change only through its
   body bands (budget) and the Events its losses emit, never through a preference for food.
4. **Ageing and illness** (`matter.py:549-554`): skipped entirely unless `age_step` or `illness_rate` is non-zero. Then each non-cohort
   draws against `min(1, illness_rate + age_step × age)` and dies on a hit. Cohorts have no hazard by design (`world_q.py:1004-1008`, the
   test at `:1015`). Because `age_at_build` is 0 (`fixtures.py:608`) and no builder sets `Person.born`, every person the realm builds is
   the same age (`carriers.py:687`), so switching ageing on would give all of them one shared hazard each season (formula, not run).
5. **Stores and yield** (`matter.py:560-606`): draws are debited; each harbour yields grain 40 and salt 30, each seam ore 50 and timber
   10, scaled by `condition / 1000` and the season factor (`SITE_YIELD`). Sites wear by `wear_per_season`: harbour 10, seam 10,
   dwelling 0, garrison 0 (`rosters.yaml:1465-1470`).
6. **Leg end** (`matter.py:643-655`).

So at shipped values **MATTER kills nobody** (ERRATA G9). Every realm death in the control run is combat: seed 0 has 9 `person.died`,
caused by `accept` (7) and `fight` (2) by my probe.

### 2.5 The scene budget, and how bodies and legs cut it

`budget = max(1, 5 + 1 × (your live hold Tenures) − body_band_penalty − 1 × len(travel_leg))` (`budget.py:57-61`), counted in **scene
actions** (`budget.py:19-20`). Age is not an input: `budget()` reads holds, body and legs only, so an old person would do as much as a
young one (with ageing switched on, until the death draw takes him). Every live `hold` counts: a seat, a landholding, or a Record or Proposition you made. The verbs that mint
a maker's hold are `create_record`, `issue`, `open_case`, `petition`, `survey`, `forge` and `utter`, plus `conceal` through its cover
Record (cross-ruling C1; `utter` opens its hold at `effects_information.py:1030` through `_makers_hold`, `:125`). `utter` succeeded every
time it was attempted (39/39, 39/39, 49/49 for seeds 0, 1, 2), which makes it as reliable a budget lever as `create_record` (87/87, 88/88,
89/89).

How the points are spent, step by step:
1. **Packing** (`es/decision/choose.py:643-668`, rule `greedy`). Your ranked acts are cut into chunks of 3. Each chunk becomes a scene.
   A chunk of 2–3 acts is an *extended* scene and costs 2; a single act costs 1. If 1 point is left and the next chunk is extended, it is
   trimmed to its first act.
2. **Release** (`deliberate.py:250-259`). In each of the 5 rounds (0–4; `driver.py:449,456`) the driver releases at most one scene
   (`scenes_per_round = 1`) and charges its cost against your remainder, `budget − spent so far`. The remainder is recomputed every round
   (`deliberate.py:143-145`), so a leg or a wound bites from the next round. A scene you cannot afford stays queued.
3. **Charge on attempt.** The cost is charged at release, before the fold judges the act (`deliberate.py:259-261`).

What a budget buys, at most (enough candidates to fill every chunk):

| budget | scenes released (cost) | acts |
|---|---|---|
| 1 | 1 (1) | 1 |
| 2 | 1 (2) | 3 |
| 3 | 2 (2+1) | 4 |
| 4 | 2 (2+2) | 6 |
| **5** (default) | 3 (2+2+1) | **7** |
| 6 (one hold) | 3 (2+2+2) | 9 |
| 10 or more | 5 (2×5) | 15, the ceiling: 5 rounds × 1 scene × 3 acts |

So every point counts. A hold adds two acts when it turns a trailing single into a pair. A leg or a band takes one or two acts away.
Observed, on two bases (name one whenever you quote the figure): `d.resolved` (acts that reached the fold) gives 1,132 acts over about
74–83 persons and 2 seasons, about 7 per person-season (per-season means 6.3–8.0, §9); the act store (`w.acts`, every act passed to
RESOLVE, `resolve.py:967`, each charged at release, `deliberate.py:252-260`) gives 676 then 731 acts at seed 0, 8.14 then 9.37 per
acting person, maximum 15 (seed 1: 8.27 then 9.08; seed 2: 8.45 then 9.69; re-run at `51d7b05`). `d.resolved` is appended on entry to the fold (`resolve.py:377-379`), before the fold's own precondition check, so ordinary admission
refusals are counted. It leaves out three sets: acts whose actor was already gone (`resolve.py:974-977`), refusals for an obstacle too high for
the pool (`:981-998`), and contested or graded acts refused by `_admits` before the seam (`:1025-1032`). The act-store mean passes the base
7 because live holds grow from 47 to 121 during season 0 (`utter`, `create_record`) and the remainder is recomputed every round.

| your body | bands below | penalty |
|---|---|---|
| 800–1000 | 0 | 0 |
| 500–799 | 1 (full_operations) | 1 |
| 100–499 | 2 | 2 |
| 0–99 | 3 | 3 |

**The "sixth scene" comment.** `deliberate.py:89-97` says an office-holder's sixth point is unspendable because only 5 scenes can be
released. That counts *scenes*. The budget counts *cost* (`fixtures.py:497-502`; `choose.py:578-585`), and 5 released scenes can carry
10 points. Once extended scenes are costed, the sixth point is spent (2+2+2). The two comments count different quantities and do not
conflict (ERRATA G11 is resolved this way by cross-ruling C1). A leg or a wound therefore costs everyone, office-holders included.

### 2.6 Persons on persons

- **Cohorts and named persons both choose.** Both are Persons; both get a budget and choose from the same verb table. `is_cohort` is
  read only by the larder draw and the death hazard (`world_q.py:1012,1074`); no verb gate tests it. Cohorts have no pursuits (37 of
  37 empty), hold no seat and eat; named persons act through offices and do not eat.
- **Bodies fall** in combat (`fight`/`accept` through the PC seam; a lost field in `march`, `effects_combat.py:293-299`, which no seeded season reached) and, if switched
  on, in MATTER. They rise only by `tend` (`effects_combat.py:370-393`). Upward band crossings emit nothing (H-211). Downward ones emit only from MATTER's hunger write (`matter.py:530`, the one call of
  `_crossings` for a body); a combat wound crosses floors without a `condition.band_crossed` Event, so no body crossing fires in the realm
  run (seed 0, two seasons: 6 `body.changed` by ctl; 0 `condition.band_crossed` by an uncommitted round-3 probe). The fight's effect writes only its
  subject's body, and the actor's body is never written (ERRATA C1; `effects_combat.py:41-43`, `:179`). The RESOLVE fold may still scar the actor
  like any other observer (`loop/resolve.py:597-606, 644-650`; `scar_excludes_actor=False`, `fixtures.py:695`; `fight` violates eight pursuit
  elements by `elements_violated_by`), so the effect marks no winner, but his `scar` can move.
- **Grudges** are written at runtime only by `march` (one row `(winning faction, −1.0, field_grudge_weight 1)` and one morale row
  against your own faction, `effects_combat.py:300-306`) and removed only by `forgive` (ERRATA C1). The referent of a battle grudge is
  a *faction Proposition*, not a person. Seeded stance rows come from the cast's loyalty at build. Nothing decays a stance row: no MATTER
  pass writes stance (in `loop/` and `state/` only `effects_combat.py:306` and `:449` assign it, and the write matrix refuses a
  `(Person, stance)` write at MATTER, `state/world.py:58-61`), so a grudge lasts until its holder forgives it, while claims decay 5 a season.
- **Regard** combines your stored stance with the deeds you judged and were told about, each at 0.5 (`person_q.py:390-410`). It feeds
  `teller_weight`, which sets how much you believe what someone tells you. It is keyed on the teller *person*
  (`es/decision/options.py:1515-1522`), so a stance row keyed on a faction never moves it.

## 3 A worked example

All numbers come from `build_realm(0)` and the shipped fixtures, computed read-only (`python -I`; the probe scripts
are not committed, the control recipe `ctl/control.py` is; §9).

**3a. A wounded traveller's budget.** `p_npc_001` holds no office (0 live holds). `p_npc_003` holds one.

| person | body | legs | band penalty | `budget()` |
|---|---|---|---|---|
| p_npc_001 | 1000 | 0 | 0 | 5 |
| p_npc_001 | 1000 | 2 | 0 | 3 |
| p_npc_001 | 799 | 0 | 1 | 4 |
| p_npc_001 | 499 | 2 | 2 | 1 (5 − 2 − 2 = 1) |
| p_npc_001 | 99 | 2 | 3 | 1 (floor; 5 − 3 − 2 = 0) |
| p_npc_003 | 1000 | 0 | 0 | 6 |
| p_npc_003 | 799 | 2 | 1 | 3 |
| p_npc_003 | 1 | 2 | 3 | 1 (floor) |

The seed-0 run leaves two wounded survivors after its two seasons (ticks 0 and 1), at body 250 and 48. A person at 250 stands below two floors (800,
500): penalty 2, so 5 becomes 3 with no office. At 48 the person is below all three: penalty 3, budget 2.

In acts (the §2.5 table), the wounds cost: body 250, budget 3, gives 4 acts instead of 7. Body 48, budget 2, gives 3 acts.

Now walk `p_npc_001` (healthy, no hold, budget 5) through a season, packing greedily with `extended_scene_cost` 2. He ranks seven or
more acts, and his `move` is in the first chunk.

| round | `budget()` | spent before | remainder | scene released (acts, cost) | after |
|---|---|---|---|---|---|
| 0 | 5 | 0 | 5 | chunk 1 (3 acts incl. `move`, cost 2) | spent 2; the move resolves, `travel_leg = [dest]` |
| 1 | 5 − 1 leg = **4** | 2 | 2 | chunk 2 (3 acts, cost 2) | spent 4 |
| 2 | 4 | 4 | 0 | chunk 3 (1 act, cost 1) cannot be afforded and stays queued | — |
| 3–4 | 4 | 4 | 0 | nothing | — |

A new leg or a changed body is one of the inputs in his fingerprint (`deliberate.py:434-500`, the `body` / `travel_leg` term). So in
round 1 he re-deliberates and repacks against the new remainder (`deliberate.py:169`) rather than replaying the round-0 queue.
Total: **6 acts with the journey, against 7 without it** (without the leg, round 2 has remainder 1 and releases the single). So the
journey cost him the act it occupied plus one more act, the trailing single. The same journey for `p_npc_003` (one hold, budget 6):
without it he releases 2+2+2 = 9 acts in rounds 0–2. With it, round 1's remainder is 5 − 2 = 3, so he releases a pair (left 1). Round 2's
remainder is 5 − 4 = 1, so one single. That is 3 + 3 + 1 = **7 acts, two fewer**. No one travels free.

Two journeys, by placement:
- **Both in the round-0 scene**: `p_npc_001` drops to budget 3, so round 1's remainder is 3 − 2 = 1 and chunk 2 is trimmed to one act.
  He gets 3 + 1 = 4 acts.
- **One in round 0, one in round 1's scene**: the second leg lands after round 1's release. It cuts the remainder of round 2 onward, which
  was already 0, so the season stays at 6 acts.

When a leg falls matters as much as how many legs there are. At the next MATTER the leg clears, and the next season starts at the full
budget again.

**3b. A cohort's larder over a season.** `cohort_set_s_001` (weight 2) stands and lives at settlement `set_s_001`, whose harbour and seam
are at condition 1000. Its want each season: grain `2 × 2 = 4`, salt `1 × 2 = 2`.

| step | `set_s_001` stores (grain / salt / ore / timber) | draw | short | body change at `body_step` 0 |
|---|---|---|---|---|
| build (tick 0) | 0 / 0 / 0 / 0 (and every ancestor empty) | — | — | — |
| first MATTER (tick 0): draw | nothing to take | 0 / 0 | 4 + 2 = **6 units** | `0 × 6 = 0` |
| first MATTER (tick 0): yield at condition 1000, factor 1.0 | 40 / 30 / 50 / 10 | | | |
| second MATTER (tick 1): draw | 36 / 28 | 4 / 2 | 0 | 0 |
| second MATTER (tick 1): yield at condition 990 after 10 wear: `int(40 × 0.99) = 39`, `int(30 × 0.99) = 29`, 49, 9 | **75 / 57 / 99 / 19** | | | |

The last row is exactly what the probe prints after two seasons. Over the realm, 37 cohorts want 148 grain and 74 salt a season;
37 harbours yield about 1,480 grain and 1,110 salt. In the realm run, the only short MATTER is the first (tick 0), before any yield exists
(ERRATA G18). This holds only at the run's horizon. A harbour loses 10 condition a season, so without `restore` its yield falls by
about 1% of base each season and reaches 0 at tick 100 (cross-ruling C9). The remediation's "cover 21.7 → 41.7 seasons" figure counts
ore and timber as food; on grain alone, cover is about 10 seasons.

The same arithmetic on the *swept* arms (formula only, not run): at `body_step = 10` the cohort loses `10 × 6 = 60` at tick 0, from 1000 to
940, which crosses no floor. At `67` it loses 402, falling to 598 (below 800, one band), so its budget becomes 4: 6 acts instead of 7.
After that, no cohort in this realm is short within the horizon above. So even switched on, hunger here is one bad first season, not
a famine.

**3c. Why a settler is refused.** In seed 0, 72 of the 81 `migrate` acts that reached the fold name `b_s_001_court`, a hearth with one dwelling
(capacity 1) where 8 people reside. A named settler: `8 + 1 = 9 > 1`, refused. A cohort: `8 + 2 = 10 > 1`, refused. All 81 reach
the effect and all 81 fail the capacity test; none is a same-home or custody refusal, and the smallest overshoot is 1. Note also that
a **cohort cannot settle in any hearth at the shipped build**: an empty one gives `0 + 2 = 2 > 1`. A hearth with two or more dwellings,
which `found`/`build` could create (`world_q.py:1317-1321`, 0 executions in the run), would change that. Today only a settlement or
larger has room for a weight-2 mover. `set_s_001` is already over (population 12, capacity 9); a settlement at population 2,
capacity 7 would admit one.

## 4 What you can do

| verb | prerequisites | cost | who | outcome | writes | realm run (reached the fold / ok, seeds 0, 1, 2) |
|---|---|---|---|---|---|---|
| `move` | typed cell `contain_path` (of: actor, to: to): destination is a rung sharing an ancestor (true everywhere under the realm, false into or out of Schoenland's T16); effect-side: not in custody, destination kind above `person` | one act in a scene, plus 1 budget point per leg for the rest of the season | anyone, self only (`own`) | deterministic, no dice: arrive, or `travel.blocked` | `contain` close/open, `travel_leg` | 42/16, 35/17, 40/12 |
| `migrate` | as `move`, plus not already home, plus room at the destination (`population + weight ≤ capacity`) | as `move` | anyone, self only | `residence.changed`, or `travel.blocked` (no path) / `migrate.refused` (write) | as `move`, plus `reside` close/open | 81/0, 143/0, 143/0 |
| `tend` | typed cell `all: [existence(subject, Person), relation(subject, with)]`: the subject is a living Person "with" you (same place) | one act in a scene | anyone; subject may be yourself | body set to 1000 in one act; refused on a whole body (written to itself = no change) | `Person.body` | 34/0, 22/0, 19/0 |
| `train` | typed cell as `tend` (existence + with); effect-side: the vocation key is a `verb_capability` value **and the subject already holds it** | one act in a scene | anyone | that key +1; else `train.refused` | `Person.capability` | 38/0, 30/0, 30/0 |
| `forgive` | you hold at least one negative stance row naming the subject (the Candidate is only formed then) | one act in a scene | anyone, own rows | all your negative rows toward that referent are deleted; positive rows stay | your own `Person.stance` | 1/1, 2/2, 2/2 |
| `give` | typed cell `all: [existence(subject, Record), relation(subject, held_by), relation(to, with)]`: you hold the Record and the receiver is with you | one act in a scene | the holder | your `hold` closes, theirs opens, one write: `record.given` | Tenure `until`/`since` | 16/0, 21/0, 19/1 |
| `commit` | typed cell: `existence` of the subject, kind Proposition (`verb_table.yaml:171-175`) | one act in a scene | anyone. No code gate stops a cohort; none did in the run (NP-G36 is a [PROPOSED] gap row) | `commitment.made` | `commit` Tenure | 61/0, 56/1, 63/1 |
| `oblige` | (sworn service to a seat) | one act in a scene | the joiner | `duty.taken` | `oblige` Tenure | none reached the fold, 24/22, none reached the fold |
| `release` | a live edge of yours in its domain (`hold, commit, oblige, succeed, tie, knot`) | one act in a scene | owner | `tenure.closed` | edge `until` | 45/3, 44/5, 46/3 |
| `succeed`, `tie / knot` | rows present, effects **declined** | — | — | nothing; `succeed` declares `heir.designated` but nothing emits it | nothing | not in the menu |

Sources: rows at `verb_table.yaml:863` (move), `:839` (migrate), `:1146` (tend), `:1451` (train), `:453` (forgive), `:533` (give), `:167`
(commit), `:878` (oblige), `:965` (release), `:1096` (succeed), `:1439` (tie / knot); effects at `effects_migration.py:24,122` and
`effects_combat.py:370,396,430`. No verb in this lane rolls dice. Every outcome is a deterministic precondition and effect, and the
degree is the identity on an uncontested row (`effects_combat.py:376-378`). Run columns are **reached the fold / ok** (ctl's `att` column), which counts acts
that reached the fold (`resolve.py:377-379`, appended on entry), so the fold's own precondition refusals ARE in the count (`tend` 0/34 below
includes 20 of them). Left out are acts whose actor was already gone (`:974-977`), refusals for an obstacle too high for the pool (`:981-998`)
and contested or graded acts refused by `_admits` before the seam (`:1025-1032`).

Why the zeros (my probes, seed 0):
- **`tend` 0/34**: 30 targets were others and 4 were self. 20 were refused at the typed precondition, before the effect. Which conjunct
  refused them (a subject no longer a living Person, or one not "with" the tender) I did not observe: every refusal emits the one flat
  kind `tend.refused` (`verb_table.yaml:1164`), and the split is not logged. All 14 that reached the effect found a body of 1000. Bodies fall only in combat, and no `tend` in the run reached a wounded subject (two survivors end season 2 at
  250 and 48, untended). A hand-built self-`tend` at body 250 runs through the season loop and gives `body.tended`, 250 → 1000.
- **`train` 0/38**: every attempt carried key `copying`, and every subject's capability was `{}`. The key is never minted (a minted
  `{copying: 1}` would lower a pool from `pool_default`, `effects_combat.py:404-407`), so **no one in the realm can be trained**.
- **`migrate` 0/81**: capacity, as in §3c. Seeds 1 and 2: 142 and 141 of 143 reach the effect, every one over capacity. The verb itself
  runs: a hand-built `migrate` to an empty hearth, through the season loop, gives `residence.changed`.
- **`move` 16 executed of 42**: 13 named a non-rung (refused at the precondition), 13 named a person rung (ladder). **All 16 executed
  moves went to the place the mover already stood** (14 cohorts naming their own settlement, 2 hearth moves). Seeds 1 and 2: 1 and 2 real
  journeys. So the typical executed `move` pays a leg and changes nothing (H-140).

A refused act still costs its scene: scenes are charged when the driver *releases* the choice, before the fold judges it
(`deliberate.py:257-261`, "THE RELEASE RECORDS WHAT WAS *ATTEMPTED*").

## 5 Pursuing goals here

### (a) The goals, and how the code holds them

No verb here carries a goal object. A person's pursuits are value axes that score verbs (the chooser); what this lane gives a goal is
the *state* it moves:

| goal | the state that represents it | the verb that writes it |
|---|---|---|
| be where something is happening (see it, be seen, act on someone there) | live `contain` | `move` (and `march` for an army) |
| make a new home | live `reside`, counted in `population` | `migrate` |
| stay able to act | `body` above the floors; a short `travel_leg` | none raises body except `tend`; legs clear at MATTER |
| keep another person alive and well | their `body` | `tend` |
| recover from a wound | your own `body` | `tend` with yourself as subject (no passive recovery) |
| end a grudge | your own negative `stance` rows | `forgive` |
| get better at something | `capability[key]` | `train` |
| pass on a document | `hold` Tenure on a Record | `give` |
| bind yourself to a cause or a seat | `commit` / `oblige` Tenure | `commit`, `oblige`; ended by `release` |
| a settlement that is fed and grows | cohort `body`; `population` vs `capacity` | nothing a cohort can choose grows its weight |

### (b) The plays

**Relocate to act on a place (or a person).**
1. Name a *rung*, not a person and not a non-rung. To reach someone, travel to the hearth or settlement where they stand.
2. Do not name where you stand: it executes, costs a leg and changes nothing.
3. Travel in your first scene. If you travel in round 0, in an extended scene, you have remainder 2 from round 1, one more 3-act scene
   (§3a: 6 acts in the season instead of 7). In that scene you can `tend`, `train` or `give` to anyone now "with" you, and everyone there
   witnesses what you do.
4. Do not put two journeys in one scene: each leg costs a budget point from the next round on, so two legs in round 0 leave you 4 acts
   in the season. A second journey later in the season can cost nothing more, if the point it removes was already spent (§3a).
5. You stay where you arrived. A `move` is not a return trip. Next season you start at full budget in the new place, and your home is
   unchanged.

**Settle somewhere new.** You can only choose places your own ledger names (`places_named`), so you must first have been told of a
place or seen its larder drawn. Then pick one with room: `population + your weight ≤ capacity`. For a named person (weight 1), that means
an empty hearth (185 of 211 at seed-0 build) or a settlement or territory below capacity. For a cohort (weight 2) it means a
settlement or larger with two spare places; no hearth at the shipped build (each has one dwelling). Capacity rises only with
dwelling Sites (`found`/`build`, `world_q.py:1320-1324`; 0 executions in the run). The chooser does not read room, and it offers only rungs your own ledger names (`world_q.py:2111-2146`, `places_named`) or, for a seat-holder, a stocked larder his seat reaches (`larders_in_purview`, `world_q.py:2148`, spliced at `:2540-2545`). That second source does not exclude a rung above his home, and for such a rung `_eff_migrate`'s newcomer test is false, so capacity is never checked (`effects_migration.py:201-203`). At seed 0
every computed destination was an occupied hearth (81 of 81: 62 by cohorts, 19 by named persons; uncommitted round-3 probe), so that case did not arise, and none of the 185 empty ones was ever
chosen. So in practice persons keep naming the full court hearth of S-001. Nobody can settle into or out of Schoenland (no shared ancestor, §2.2).

**Keep someone alive.** Wounds come from `fight`/`accept` (and from a lost field, which no seeded season reached). Then: go where the
wounded person stands (`move`, round 0: one act plus the leg point), then `tend` in your round-1 scene. Whether a `tend` packed into the
same scene as the `move` already sees you "with" the patient I did not verify. One `tend` restores the body to 1000 whatever the wound, and consumes nothing. The code marks the magnitude [ASSUMPTION; medium; Jordan
to correct], with a named revert to a swept fraction of the headroom (`effects_combat.py:378-379`).
That gives the patient back up to 3 budget points from the next round on. A patient at body 48 with no hold goes from budget 2 to 5:
3 acts a season become 7 from the next full season, and part of that sooner, depending on what they have already spent. Two tenders on one person in one fold: the second is refused.
A body at 0 has died in the same write (`effects_combat.py:178`), and there is no one left to tend.

**Recover yourself.** Nothing heals you passively and hunger never bites at shipped values. Your only path is `tend` with yourself as
subject (4 of 34 seed-0 attempts did this), or someone else's `tend`.

**Rebuild a relationship.** You can remove only *your own* negative rows (`forgive`), and all of them toward that referent go at once.
Your regard for them still carries the deeds you judged and were told about (`person_q.py:390-410`), so a forgiven offender whose bad
deeds sit in your ledger still reads below zero. You cannot make anyone forgive *you*: there is no verb that writes another person's
stance, and `tie` (the bond) is declined. Battle grudges point at the winning *faction*, so you forgive a faction, not a man. Forgiving
raises your `stance_toward` that referent (the negative rows are gone, `person_q.py:68-77`), which moves the stance term of your
chooser's score toward acts about it. It changes no teller's weight unless the referent is the teller person (§2.6).

**Train.** In the shipped realm, no one holds any vocation key, so every `train` is refused. In a case world where the subject already
holds `copying`, each act adds 1. That means one more die for the verbs `verb_capability` maps to `copying` (`tell`, `speak`). Capability
"gates nothing": it adds dice and opens no option.

**What a settlement's people can and cannot do.** A cohort chooses like anyone. It can `move` (14 of the 16 executed seed-0 moves were
cohorts, all to their own settlement), attempt `migrate` (62 of the 81 that reached the fold), `survey`, `work` and others. No code gate stops it from
committing to a faction (`commit` needs only an existing Proposition); none did in the run, and NP-G36's "cohorts cannot commit" is a
[PROPOSED] gap row, not a built rule. It holds no seat and so cannot act through one. Its weight never changes: there are no births, no growth, and no partial migration, so "famine
cannot empty a town". It eats where it stands. One `Felled` deletes it whole (ERRATA C1).

### (c) Costs, risks, counter-play, blocks

- **Custody** (a live `detain` on you) blocks every journey and settlement, wherever the detaining seat is (`effects_migration.py:73-88`).
  That is the only counter-play another person has against your travel. Nothing contests a journey.
- **Capacity** is the only block on settling, and it is the destination's alone.
- **Budget** is the price of everything: a leg (−1 point), a wound band (−1 point each), a refused attempt (its scene's cost, 1 or 2).
  Each point is one or two acts (§2.5 table).
- **Death** is permanent, vacates seats (`test_in34_bodies_clock.py`), and has no successor mechanism (`succeed` is declined: its one
  reader, transmission at death, is unbuilt, `verb_table.yaml:1113`). 7 of the 32 built offices have no conferral basis (`off_npc_020`,
  `off_duke_valorsmark`, `off_npc_030`, `off_npc_031`, `off_npc_032`, `off_npc_050` and the unauthored guild-leader seat `off_npc_084`;
  `has_conferral_basis`, `state/gate.py:643-657`, and `_req_confer` refuses them first, `predicates.py:126-127`), so none can be refilled
  once its holder dies. At the end of season 2 the vacant seats number 8, 6 and 10 at seeds 0–2, and 3, 5 and 6 of them are those seats.
  The King (`p_npc_020`) is dead after the first season at every seed (checked by re-running seeds 0-2 at 51d7b05), vacating `off_npc_020` and the second seat he holds,
  `off_duke_valorsmark`. The one refill in all three seeds is a `confer` at seed 1 (4 later `confer.refused`).
- **Being seen.** Arriving puts you in front of every witness at the destination; there is no fog and no concealment of the journey
  itself.

### (d) What the mechanics structurally reward or punish

- **Distance is free, so geography carries no strategy.** The capital and the farthest fjord cost the same leg (`budget.py:60`), so
  nearness, roads, mountains and rivers are not inputs to any choice.
- **Staying is rewarded over going** by exactly one budget point per destination. Nothing pays you for arriving except presence.
- **The journey to where you stand is a dominated option the chooser still takes** (16 of 16 executed seed-0 moves).
- **`migrate` is a dead end in the realm**: 0 successes in 367 acts that reached the fold over three seeds, each charged a scene.
- **`train` is a dead end by construction** (no key holders); **`tend` is reachable but idle** (bodies stay whole outside combat).
- **Hunger and age are switched off**, so keeping a settlement fed or a person young rewards nothing; even with `body_step` on, the
  realm's larders run ahead of demand after the first MATTER (tick 0), within the horizon in §3b; and no fixture value lets hunger enter the
  score, because the larder term is the same for every candidate (`choose.py:448, 452-453`). It reaches choice only through body bands and the
  Events a loss emits (§2.4 step 3).
- **Holding pays acts.** +1 point per live hold: from 7 to 9 acts with one hold. Minting holds with `utter` or `create_record` (always
  successful in the run) is the cheapest way to buy a journey back. No one, office-holder or not, travels free: a round-0 leg costs a
  budget-6 holder two acts (9 → 7).

### (e) What success leaves in the world

A journey leaves a closed and an opened `contain` edge, a `travel.moved` event (witnessed at the destination), and a `travel.ended`
the next season. A settlement leaves a moved `reside` edge and `residence.changed`, which changes `population` for both rungs.
A `tend` leaves a body at 1000 and `body.tended`, but no upward band crossing, so no one is told that the patient recovered (H-211).
A `forgive` leaves a shorter stance list and `stance.moved`. A `give` leaves the Record in new hands (`record.given`). None of these
leaves a lasting relationship object: there is no friend, kin, spouse or household edge.

## 6 How it connects

| you feed | into | how |
|---|---|---|
| presence (`contain`) | WITNESS / information | witnesses are whoever stands there; travelling is how you come to see and be seen |
| presence | social contest, `tend`, `train`, `give` | the "with" relation requires the same place |
| presence of a cohort | economy | the larder draw is taken where the cohort stands |
| residence | GV | `population` and `capacity`, the RR-2 throttle |
| body bands and legs | every subsystem | fewer scenes for everything else this season |
| `forgive` | chooser; telling only for a person referent | raises `stance_toward` the referent (removes negative rows), so the stance term of the score rises; it moves `teller_weight` only when the referent is a person who tells you things, never for a faction grudge |

| you draw | from | how |
|---|---|---|
| wounds | PC (`fight`, `accept`), MB (`march` field) | the only shipped writers that lower body |
| grudges | MB (`march`) | stance rows against the winning faction |
| budget bonus | GV / FI | every live `hold`, including a Record you created |
| arrival of an army | MB | a won or unopposed `march` relocates its claimants through the same `_relocate` (`effects_migration.py:101-105`) |
| a new person | GV `dispatch` + CENSUS | an id demanded by a `dispatch` is individuated at the event's place |
| food | EC | harbour and seam yield, `transfer`/`requisition` between rung stores |

Combinations: **move then tend** (round 0, then round 1) is the one way to heal someone elsewhere. **Move then speak/tell** puts you in
the room for a social act and in front of its witnesses. **Forgive then listen** works only for a person: it raises the weight you give
that person's tellings through regard. A battle grudge's referent is a faction, so forgiving it changes how you score acts about that
faction and no teller's weight. **Create a Record or `utter`**: the extra live `hold` adds one point to your budget, which can offset a leg.

## 7 Playing it as proposed

Everything here is **[PROPOSED]** (`proposals/2026-10-16-verbs/…-17-lexicon-world-travel-and-survival.md`, `…-18-lexicon-npc-life-and-persons.md`;
`proposals/2026-10-21-v9-remediation/`). Verbs-03 §III.5 rulings override a lexicon's body (ERRATA G19).

**Travel as proposed.**
- **[PROPOSED] `travel`** replaces the name `move` (R-10), and a journey to where you already stand is not formed (H-140, WT-G01).
- **[PROPOSED] Route Query** (M-WT-1): path and cost over `settlement_adjacency` and `adjacency`, edges weighted by `terrain_cost_matrix`
  (plains 1.0, forest 1.5, marsh 2.0, mountain pass 2.0, mountain 999, road overlay 0.7, bridged river 1.0). Your leg price would become
  the route cost, `ride` lowers it, and `sail` uses water edges. Writes nothing. Waits on: nothing but building it.
- **[PROPOSED] Calendar** (M-WT-2): a year length; storm season refuses `sail`; a winter term.
- **[PROPOSED] Journey roll** (M-WT-3): an unopposed draw against an Ob set by terrain, on `degree_from_net`: arrive / delayed (the leg
  does not end at the next MATTER) / lost (`travel.blocked`). A delayed traveller would be "between places", which amends ratified
  Layer 1 (`contain : Rung → Rung`); L17 §3.9 item 2 recommends keeping journeys within the season.
- **[PROPOSED] Exposure** (M-WT-4): a leg through the Forgetting zone or radiation bands costs body unless you pass "Endurance check Ob 1
  per territory". Open question L17 §3.9 item 1: (a) only Calamity territory hurts a named traveller, or (b) weather does too. Not ruled.
- **[PROPOSED] `explore`** (WT's, R-09; waits on M-WT-5, POIs minted from `poi_catalog` counts): reveals one authored Site or secret
  Record as a belief, emits `site.discovered`.
- **[PROPOSED] `forage`** (MB's row, R-08; waits on M-WT-8 campaign supply): a standing force eats ahead of residents and one route edge
  out; the residents' cohort witnesses it and takes a grudge.
- **[PROPOSED, PARKED] `camp`** (trigger: multi-season legs + calendar + supply) and **`evacuate`** (a seat moving cohort weight; trigger:
  M-WT-6 cohort weight migration and a hazard warning a seat can read).

**Survival as proposed (RB-5, REM-50/51/52; JQ-6).** A settlement Query `hunger(w, S) → (band, cover, unmet)` with bands starving /
hungry / lean / fed; hunger claims reach the seat-holders whose purview holds the town; `body_step` live at 10 (marked [ASSUMPTION;
Jordan to correct]). Then cohorts lose body when short and their budgets narrow by band. ERRATA G18: even then, at today's magnitudes,
hunger binds only before the first yield (cover rises 21.7 → 41.7 seasons; that figure counts ore and timber as food, and on grain
alone cover is about 10 seasons, cross-ruling C9). Ageing and illness rates are Jordan's to set (#457 D2;
`fixtures.py:598-605`); per that comment, `references/npc_registry.yaml` carries `age: null` on 29 of its 46 rows and no age key on 17.

**Persons as proposed (L18; mechanics M1–M15).**
- **[PROPOSED] passive recovery** (M1, a MATTER rising arm) and **upward band crossings** (H-211); a **care degree** where the tender's
  skill sets an obstacle (M2). Today one `tend` heals fully.
- **[PROPOSED] capability sources** (M3, the J-13 remainder) and **readers in combat and choice** (M4). Until then `train` has nothing
  to raise and nothing reads what it would raise.
- **[PROPOSED] `tie`** split from `knot` (`knot` is TW's, R-02), with a partner operand (M8) and typed ties (friend, sworn, patron) (M7).
- **[PROPOSED] `marry`**: two directed `kin` Tenures with content `spouse` (M9), the spouse's consent as the obstacle [ASSUMPTION].
- **[PROPOSED] `hire`** (EC's row, R-01) and **`defect`** (close A, open B in one write, `allegiance.changed`; medium confidence).
- **[PROPOSED] `succeed`** as the heir's claim (GV's row, R-11; IN-61; waits on M12, a vacancy reaching the heir); `oblige` → **`pledge`**.
- **[RULED, Jordan 2026-09-13] no births for now: ED-WR-0011**, Option A, a closed authored cast of 46 with no season-tick generation
  ("We will return much later"; `registers/editorial_ledger_wr_archive.jsonl`, its later row); `es/loop/census.py:39-40` holds the "no clock
  generates" half, but a `dispatch` naming an absent id can still individuate one person (`census.py:46-99`; a Person is built at `:106`), so the
  cast is closed in the run (`person.individuated` 0 at seeds 0–2, ctl), not by construction. L18
  (`…-18-lexicon-npc-life-and-persons.md:85-86`, `:705`) still calls the row open: it read the superseded first row. `rear`, children
  and the dynastic layer stay PARKED on that ruling.
  Estate transmission at death is M11. Household has no source at all.

**Stubbed, inert at shipped defaults, or refused in the realm run.** Inert: `body_step` 0, `age_step` 0, `illness_rate` 0, empty
`season_factor_draw` (no year). Refused in every seed: `migrate` (0/367), `tend` (0/75), `train` (0/98). Refused in seed 0, with a single
success elsewhere: `give` (seed 2), `commit` (seeds 1 and 2). Declined effects: `succeed`, `tie / knot`. Absent: kin, marriage,
household, births, inheritance, routes, exposure, POIs, foraging.

## 8 Common mistakes and traps

1. **"Travel takes time and distance matters."** No: any rung, one leg, one point of budget, done this season (`budget.py:60`).
2. **"`move` to a person takes me to them."** It is blocked: persons are `person`-kind rungs and the ladder refuses (§2.2 step 4).
3. **"An executed `move` means someone went somewhere."** In seed 0 every one of the 16 went to where the mover already stood.
4. **"Moving changes where I live."** Only `migrate` touches `reside`; and a migrant who is refused still spent his scene.
5. **"A cohort can settle in a hearth."** Not at the shipped build: weight 2 against capacity 1. It can *move* into one (presence
   is not throttled). A hearth that `found`/`build` gave a second dwelling would admit it, but neither executes in the run.
6. **"Hunger, age and weather are part of play."** All three run and do nothing at shipped values; every realm death is combat (G9).
7. **"Named NPCs eat."** Only cohorts eat (ED-IN-0255), and they eat where they *stand*.
8. **"Wounded persons heal over time."** Nothing raises a body except `tend`, and the recovery is not announced (H-211).
9. **"The budget is 5 scenes, and each act costs one."** The budget is `5 + holds − bands − legs` *scene actions*, floor 1, spent as a
   cost: an extended scene (2–3 acts) costs 2. Budget 5 buys at most 7 acts (2+2+1), budget 6 buys 9, and 15 acts need budget 10 or more.
   Every point above 5 is spendable. Observed: about 7 acts per person-season on the `d.resolved` basis (1,132 acts, seed 0, 2 seasons);
   8.1 then 9.4 on the act-store basis, maximum 15 (seed 0).
10. **"The map drives the world."** It is read once at build, plus `provinces:`/`terrain:`/`water:` by the mass-battle field, which no
   seeded season fights. Adjacency, terrain costs and POIs have no runtime reader.
11. **"Any rung is reachable."** Not Schoenland's: T16 is a second root, so every journey into or out of it is `travel.blocked`.

**Where the draft appendix A6 (WT and NP blocks) was wrong, and the correction:**
- *WT §4 grades `move, migrate, _relocate` RUNS-IN-LOOP*, citing "D02 §4.1 … `migrate` 86 (formed)". Corrected: `migrate` is
  **TESTS-ONLY**, 81/0, 143/0, 143/0 (ctl; ERRATA G1, G2, C7); every refusal is the capacity throttle (my probe).
- *WT §2 step 1 lists `contain_ascends` among the preconditions.* It is an effect-side decline (`effects_migration.py:62-67,186-188`), and
  because every person is a `person` rung it is what blocks journeys "to a person". The precondition (`contain_path`) compares the
  person rung, not the standing place, which is why same-place journeys execute.
- *WT §3: "`work`, `restore` require presence".* Corrected by ERRATA C5: `work`'s typed precondition has no presence clause
  (`verb_table.yaml:1511-1517`). What requires presence in this lane is the "with" relation of `tend`, `train`, `give`.
- *WT §3 / NP §3: cohorts as "the migration actors".* They attempt; none succeeds, and none can ever enter a hearth.
- *NP §4 grades `tend, train, forgive` RUNS-IN-LOOP "executions unmeasured", and `commit, oblige, release, give` RUNS-IN-LOOP.*
  Measured: `tend` 0/34, `train` 0/38, `give` 0/16, `commit` 0/61 (seed 0) → TESTS-ONLY (ERRATA C7); `forgive` 1/1 and `release` 3/45
  execute; `oblige` executes 22/24 in seed 1 only (G2).
- *NP §2 and §4: `succeed` "still emits `heir.designated`".* Corrected (ERRATA C7): the row declares the event; nothing in the tree emits
  it (`grep -rn heir.designated --include=*.py engine/season`, outside tests: 0 hits).
- *NP §3: "stance is written at runtime only by `_eff_march` (grudges from battle)".* True in code (ERRATA C1), but no seeded season
  reaches a field (field events 0), so no battle grudge is written in the realm run; seed-0's one `forgive` acts on a seeded row.
- *NP §6: `knot` owner (TW vs FI) and `succeed` owner (GV vs NP) "unreconciled".* Corrected (ERRATA G19): rulings R-02 and R-11 govern,
  `knot` is TW's and `succeed` GV's; likewise `forage` is MB's (R-08), not WT's as L17's body says.
- *Overview/§2 counts the eight rung kinds as if all exist.* The realm builds no `province` rung; 17 territory rungs, and provinces are a
  Query (ERRATA G6).
- *WT §2 "survival passes in MATTER" omits claim decay.* MATTER also decays claim confidence by 5 a season (ERRATA G8).
- *The "5 scenes per season" shorthand* (draft overview) is wrong: the budget is 5 *scene actions* spent as a cost (trap 9).

Doc/code mismatches outside the draft: L18 calls `tend`, `train`, `forgive` absent (stale; rows at `verb_table.yaml:1146,1451,453`).
The geography file contradicts itself on the settlement edges: 55 at :580/:589, 56 at :602, and "24 primary + 1 sea" at :640. 55 is
what loads. L17's line cites into `matter.py` and `world_q.py` are stale by up to 213 lines.
The quarantined `.designs/systems/_architecture/reference/player_agency_v30.md` (ARCHIVED-NOT-CANON; not edited here) disagrees with
the code twice. `:63` says "The player has 3–5 scene actions per season"; the budget is `max(1, 5 + live holds − body bands − travel legs)`
scene actions (`budget.py:57-61`), and budget 5 buys at most 7 acts (§2.5). `:61` calls Pathologic 2 "a hard time constraint (12 days)";
its playable calendar is Days 1–11 and Day 12 is the ending text [CONTESTED] (T09 precedent, Pathologic 2 §8,
`research/game_precedent_suite/tutorials/T09_sanity_b.md`).

### §8 Round-2 corrections (audits J and L, cross-rulings C1–C13). I opened each cited line before accepting it.

1. **Budget unit and spending (J F1–F3, L X1, X2; C1).** My first version called the budget "scenes", charged a shared scene 1, and
   called the sixth point "disputed" with a possible "free journey" for office-holders. Wrong. `budget.py:19-20` returns *scene
   actions*. `choose.py:578-585,643-668` spends them as a cost, 2 for an extended scene, trimming to one act when 1 point is left.
   `deliberate.py:250-259` releases one scene per round over rounds 0–4 (`driver.py:449,456`). Rewritten: §1, §2.5, §3a, §5b, §5c, §5d,
   trap 9. No one travels free (9 → 7 acts for a budget-6 holder). I accept the ruling. `deliberate.py:89-97` counts scenes, not cost,
   so the two comments do not conflict.
2. **§3a walk redone** with `extended_scene_cost` 2 and rounds 0–4: 7 → 6 acts for one journey (budget 5). The walk adds that a leg
   triggers re-deliberation through the fingerprint (`deliberate.py:169,434-500`), so the next round repacks against the new remainder.
3. **Cohort commit (J F5, L X5; C7).** "Cohorts cannot commit (NP-G36)" was a gap-register row stated as a rule. `commit`'s typed cell
   needs only an existing Proposition (`verb_table.yaml:171-175`), and `is_cohort` is read in season code only at `world_q.py:1012,1074`.
   Corrected in §2.6, §4, §5b.
4. **Forgive and tellers (J F6, L X14).** I had written that forgiving raises a faction's tellers' weight. `teller_weight` reads regard
   toward the teller *person* (`options.py:1515-1522`), and battle grudges are keyed on the winning faction (`effects_combat.py:302-303`),
   so forgiving a faction moves no teller. Also corrected "lowers the stance term" to "raises `stance_toward`". §2.6, §5b, §6.
5. **Schoenland (J F7).** T16 is minted with no parent (`populated.py:720-735`), and my probe confirms two non-person roots (`r_valoria`,
   `terr_T16`) with no shared ancestor between S-037 and S-001. Journeys into or out of it are blocked, and its cohort cannot leave.
   Added to §1, §2.2, §4, §5b, trap 11.
6. **Geography readers (J F9).** `es/data/geography.py:1-8` reads `provinces:`, `terrain:` and `water:` for the mass-battle field (no
   seeded field is fought). I had said only world-gen reads the file. Corrected in §1 and in the data-vs-read paragraph.
7. **Edge counts (J F12).** The file states 55 and 56 and "24 primary + 1 sea"; I had reported one comment only. Corrected in §1 and above.
8. **Wear rates (J F13).** harbour 10, seam 10, dwelling 0, garrison 0 (`rosters.yaml:1465-1470`); I had said "Sites wear 10". §2.4.
9. **Capacity can grow (J F16).** "A cohort never settles in a hearth" now reads "not at the shipped build": `found`/`build` add dwellings
   (`world_q.py:1317-1321`). §3c, §5b, trap 5.
10. **Hunger cover caveat (L X8; C9).** The "21.7 → 41.7" figure counts ore and timber; grain cover is about 10 seasons; harbour yield
    reaches 0 at tick 100 without `restore`. §3b, §7.
11. **`tend` refusal split (L X9).** I had said 20 "failed 'with'". The refusal kind is flat (`verb_table.yaml:1164`); I observed only that
    20 never reached the effect, not which conjunct refused them. §4.
12. **Acts per person-season (L X10).** The basis is named: `d.resolved` 1,132 acts, seed 0, 2 seasons, about 7; per-season means 6.3–8.0.
    The draft errata's "~8-10" is not supported on the `d.resolved` basis the ctl files use; it is supported on the act-store basis
    (8.1, 9.4; see Round-3 corrections). §2.5, trap 9.
13. **Column order and tick names (L X19, X20; C2, C3).** Run columns were attempted/ok, with "attempted" meaning admitted to the fold (now "reached the fold", Audit fixes 3 and 19).
    MATTERs are named by tick (the first at tick 0); §3b had said "season 1 MATTER".
14. **Grades per seed (C12, L X4).** §0 now states `give` executes at seed 2, `commit` at seeds 1 and 2, and both are TESTS-ONLY at seed 0.
15. **Primitives (C11).** Added one-clause definitions of Tenure, hold/Office, Record/Proposition, "with" and round to §1.

Nothing in the round-2 findings for T10 did I reject.

### Round-3 corrections (against `51d7b05` and the precedent suite; "row" is a row of `dispositions/D_T10.md`, "also-row" of `D_T10_also.md`)

1. **Acts per person-season** (D_T10 row 36). Old: "about 7 per person-season ... the draft errata's ~8-10 is not supported by the ctl files".
   New: two bases. `d.resolved` gives about 7 (6.3–8.0); the act store gives 8.14 then 9.37 at seed 0, maximum 15 (676 and 731 acts; seed 1
   8.27, 9.08; seed 2 8.45, 9.69), so ~8–10 is supported on that basis. §2.5, trap 9, round-2 item 12. Evidence: `resolve.py:377-379, 967,
   974-977, 981-998, 1025-1032`; `deliberate.py:252-260`; re-run of the seed-0 control. (The overview's "~8–10 acts observed" needs the same two bases.)
2. **Hunger and the score** (row 8). Old: silent. New: `urgency(subsistence)` is added identically to every candidate and cannot change a
   decision, so switched-on hunger would reach choice only through bands and Events. §2.4 step 3, §5d. Evidence: `choose.py:217-238`.
3. **The zeros and their controls** (rows 18, 37). Old: `migrate` 0/81 "capacity", `tend` untended wounds. New: seeds 1 and 2 reach the
   effect 142 and 141 of 143 times, all over capacity; seed 0's 81 destinations were all occupied hearths (62 cohort, 19 named) and none of
   the 185 empty ones was chosen; a hand-built `migrate` to an empty hearth gives `residence.changed` and a hand-built self-`tend` at 250 gives
   `body.tended`, 250 → 1000. §4, §5b. Evidence: `world_q.py:2111-2146`; re-run with a wrapped `migrate` effect and a callback.
4. **The mend is an assumption** (rows 3, 15, 23). Old: "One `tend` restores the body to 1000 whatever the wound." New: it also consumes
   nothing, and the code flags the magnitude [ASSUMPTION; medium; Jordan to correct]. §5b. Evidence: `effects_combat.py:378-379`.
5. **One age for everyone** (row 19). Old: silent. New: cohorts have no hazard by design and every built person has `born` 0, so ageing
   would apply one shared hazard (formula, not run). §2.4 step 4. Evidence: `world_q.py:1004-1008, 1015`; `fixtures.py:608`; `carriers.py:687`.
6. **Death without succession** (rows 5, 24, 90; also-row 7). Old: "no successor mechanism (`succeed` is declined)". New: 7 of 32 offices
   have no conferral basis (ids listed, §5c), so they never refill; vacant at the end of season 2: 8, 6, 10 (null-basis seats 3, 5, 6); the
   King is dead after the first season at all three seeds; one refill in total across the three seeds (seed 1). Errata Part 2 C8 said six; Part 3 R-F1, T08 and T09 say seven.
   Evidence: `state/gate.py:643-657`; `predicates.py:126-127`; `verb_table.yaml:1113`; re-run of the realm, seeds 0–2.
7. **What a fight and a grudge leave** (rows 57, 61). Old: silent. New: a fight writes only its subject; nothing decays a stance row, and the
   write matrix refuses a stance write at MATTER. §2.6. Evidence: `effects_combat.py:41-43, 179, 306, 449`; `state/world.py:58-61`.
8. **Band crossings** (also-row 39). Old: "Upward band crossings emit nothing (H-211)." New: downward crossings emit only from MATTER's hunger
   write, so a combat wound crosses floors silently (seed 0: 6 `body.changed`, 0 `condition.band_crossed`). §2.6. Evidence: `matter.py:39-90,
   530, 690`.
9. **Age and the budget** (also-row 33). New clause: age is not an input to `budget()`. §2.5. Evidence: `budget.py:57-61, 71-83`.
10. **Births** (also-row 3). Old: "[HELD, Jordan] ... ED-WR-0011 (`needs_jordan: true`)". New: RULED 2026-09-13, Option A, a closed
    authored cast of 46, no births for now; L18 read the superseded first row. §7. Evidence: `registers/editorial_ledger_wr_archive.jsonl`
    (two ED-WR-0011 rows); `census.py:39-40`. (File 12's two ED-WR-0011 lines need the same change.)
11. **`.designs` disagreement** (also-row 61). New note in §8: `player_agency_v30.md:61, :63` ("12 days"; "3–5 scene actions per season") disagrees
    with `budget.py:57-61` and with Pathologic 2's Days 1–11; the quarantined file is not edited.
12. **Ending** (new since #494; changes the Part 3 draft's "no ending condition"). Old: "no ending condition in the loop (G17)". New: the season
    reports `endings` (a read, never an actor), and the realm as built reaches none (`[]` in both seasons at seed 0). §0a. Evidence:
    `driver.py:514-518`; `world_q.py:1764`; re-run.
13. **Player interface** (cross-suite qualifier). §0a carries the qualifier: none in the season loop, a test-only callback, and two other human-facing
    seams exist (`agon_harness.py`, two workbench servers).
14. **New section `## 0a How it plays`** (D_T10 Part 3), re-verified line by line against `51d7b05`. Differences from the draft: the ending
    line (item 12), the births line (item 10), the player-interface qualifier (item 13), `world_q.py` cites moved by #494, and "a settlement
    cannot fail" became "does not fail in the run" (0 cohort deaths at seed 0; at seed 2 one cohort is gone, Audit fixes 1).
15. **Scratchpad paths removed** from §3 and §9; the probe scripts are not committed.

## 9 Checks

Opened (path:line at HEAD `a4ca9a5`): `es/decision/budget.py:18-83`; `es/data/fixtures.py:217,228,463,469,488-511,526-527,571-608,
646-654,812-814`; `es/rosters.yaml:256-259,1472-1500,1540-1557,2520-2565`; `es/loop/effects_migration.py:24-217`; `es/loop/matter.py:165-200,
355-440,505-560,576-606,620-656`; `es/queries/world_q.py:902-1046,1208-1316,1986-2010,2698-2720`; `es/state/containment.py:73-93`;
`es/state/world.py:301-324`; `es/data/requires.py:374-400`; `es/loop/effects_combat.py:205-232,285-312,360-450`;
`es/queries/person_q.py:68-95`; `es/loop/census.py:1-106`; `es/loop/deliberate.py:88-145,257-261`; `es/verb_table.yaml` rows at
:453,:533,:839,:863,:1146,:1451; `es/harness/populated.py:715-760`; `es/harness/probes.py:144-149`; `systems/settlements/valoria_geography_v30.yaml`
(loaded with `yaml.safe_load`).

Ran (all `python -I`, read-only; the probe scripts are not committed, the control recipe is `ctl/control.py`):
- `probe1.py 0 0`: 83 persons (37 cohorts weight 2, 46 at 1); rung kinds as in §1; 211 dwellings; every body 1000, `born` 0; at build the
  realm draw wants 148 grain / 74 salt and takes 0.
- `probe2.py 0 2`: `set_s_001` stores 40/30/50/10 after season 1, 75/57/99/19 after season 2; `migrate` 81 reached the effect, 81 over
  capacity, all to hearths; `tend` 14 reached the effect, all at body 1000; `train` 19, key `copying`, capability `{}`; deaths 9
  (accept 7, fight 2); end bodies 1000 ×72, 250, 48.
- `probe3.py 0 2`: `move` by destination kind: settlement→moved 14, hearth→moved 2, person→blocked 13, non-rung→blocked 13; `tend`/`train`
  self vs other split.
- `probe4.py {0,1,2} 2`: executed moves to the mover's own place 16/16, 16/17, 10/12; acts per person per season ≈ 6.3–8.0.
- `probe5.py`: the `budget()` table in §3a; named holds 0:15, 1:27, 2:1, 5:2, 8:1; 185 empty hearths; `b_s_001_court` 8/1, `set_s_001` 12/9.
- `probe6.py 0 2`: `migrate` destinations `b_s_001_court` 72, `b_s_009_market` 5, `b_s_006_inn` 4; smallest overshoot 1.
- `probe7.py`: `cohort_set_s_037` ancestry `[cohort_set_s_037, set_s_037, terr_T16]`; no shared ancestor with `set_s_001`; non-person
  roots `r_valoria`, `terr_T16`.
- Round 2, opened: `es/decision/choose.py:570-590,640-668` (cost budget, trim, greedy chunks of 3); `es/loop/driver.py:449-456` (rounds =
  `scene_budget`, `range(rounds)`); `es/loop/deliberate.py:150-262,434-500` (re-deliberation on a changed fingerprint, release, charge);
  `es/data/fixtures.py:491-509`; `es/verb_table.yaml:167-182` (commit); `es/decision/options.py:1515-1524` (teller weight);
  `es/harness/populated.py:720-736`; `es/data/geography.py:1-10`; `es/rosters.yaml:1460-1471`; `es/queries/world_q.py:1310-1321`;
  geography file :578-603, :638-642; `es/loop/effects_information.py:125,1030` (`utter`'s maker's hold); grep of `is_cohort` readers.
- Round 3, opened at `51d7b05`: `es/decision/choose.py:217-238`; `es/loop/effects_combat.py:24-70, 100-182, 290-308, 365-395, 425-451`;
  `es/queries/world_q.py:985-1018, 1030-1048, 1764-1800, 2111-2146`; `es/loop/driver.py:445-460, 508-535`; `es/loop/resolve.py:374-380, 960-975, 1012-1034`;
  `es/loop/deliberate.py:245-265`; `es/loop/matter.py:39-92, 362-366, 511-535, 547-551, 641-656`; `es/state/gate.py:643-657`;
  `es/loop/predicates.py:120-130`; `es/state/world.py:50-72, 640-660`; `es/state/carriers.py:680-688`; `es/data/fixtures.py:586-608`;
  `es/harness/play_surface.py:1-52`; `es/loop/census.py:33-43, 104-106`; `es/verb_table.yaml:1096-1114, 1155-1166`; `es/offices.yaml:192-200`; `registers/editorial_ledger_wr_archive.jsonl` (the two ED-WR-0011 rows); `.designs/systems/_architecture/reference/player_agency_v30.md:55-66`
  (read only).
- Round 3, ran (`python -I`, read-only, seeds 0–2, two seasons, the `ctl/control.py` recipe; scripts not committed): per-season store and
  `d.resolved` act counts, deaths, verb counts and live holds (seed 0: 676 and 731 acts, 535 and 597 resolved, holds 47 → 121, deaths 5
  and 4, no cohort death; seeds 1 and 2 as in Round-3 correction 1; at seed 2 `cohort_set_s_029` is gone by the end, from a separate audit-fix probe); start budgets (52 at 5, 27 at 6, 1 at 7, 2 at 10, 1 at 13);
  conferral of every office and the vacant seats at the end (null-basis seats 7 of 32 at every seed; vacant 8, 6, 10; King dead at every
  seed); `confer` acts (0, 5, 0; seed 1 one `tenure.opened`, four `confer.refused`); a wrapped `migrate` effect (seed 0: 81 of 81 to occupied
  hearths, 62 cohort and 19 named); `endings` returned by each season (`[]`); `condition.band_crossed` count (0 beside 6 `body.changed`);
  and three hand-built acts through the callback (self-`tend` at 250 → 1000, `migrate` to an empty hearth → `residence.changed`, `march` at
  a settlement → `march.declared` then `field.lost`; `len(resolvable_verbs())` = 47).

Not confirmed: why `give` and `commit` are refused in seed 0 (not diagnosed); the §3a act counts as an executed trace (they are derived
from the packing and release code, not observed on one person in a run); whether a `tend` packed in the same scene as the `move` sees the
new presence; the hunger arithmetic at `body_step` 10 and 67 (computed from the formula, not run); the mass-battle seam's use of the geography
file (draft claim, `seam/wrappers/mass_battle.py`, only the import at :88 seen).
