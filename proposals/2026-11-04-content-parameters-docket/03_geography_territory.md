# Content parameters docket, chapter 03: Geography and territorial hierarchy

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

All counts measured by loading `systems/settlements/valoria_geography_v30.yaml` (G) and `engine/season/cohorts.yaml`.
"Reader" = a non-test code path that opens the key; keys with no reader found are marked NO-READER (grep over engine/, modules/, tools/).

## TERRITORIAL LADDER (closed set of rung kinds) — owner: engine/season/rosters.yaml:267-270 (`rung_kinds`)
Population now: 8 kinds, `[person, hearth, community, settlement, territory, province, duchy, realm]`.   Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | tiers | realm | rung kind; `r_valoria`, one, built by `build_realm` | REQ | HAS (1) | populated.py:968 |
| 2 | tiers | duchy | rung kind; 3 minted `duchy_valorsmark` (Crown), `duchy_hafenmark` (Hafenmark), `duchy_varfell` (Varfell) | REQ | HAS (3, hardcoded tuple in populated.py) | populated.py:1004-1007 |
| 3 | tiers | province | rung kind declared; NOT minted; a query `world_q.provinces_of` (existence-conditional on one faction holding the constituent territories) | DERIVED | n/a | world_q.py:2168; populated.py:975-1000 |
| 4 | tiers | territory | rung kind; one per G `provinces:` row (17) | REQ | HAS (17) | populated.py:1021 |
| 5 | tiers | settlement | rung kind; one per G `settlements:` row (37) | REQ | HAS (37) | populated.py:1040 |

| 6 | tiers | title per rung kind (`titles.domains`, 11 titles: King, Queen->realm; Duke, Duchess->duchy; Count, Countess->province; Lord->territory; Mayor->settlement; Community Leader->community; Family Head->hearth; Individual->person) | closed map title -> rung kind, total over `rung_kinds` | REQ | HAS (11) | offices.yaml:155-182 |
| 7 | tiers | scale per rung kind (`scale_of_rung.scale`) | rung kind -> {Personal, Relational, Territorial, Structural}; 8 rows (settlement..duchy = Territorial, realm = Structural; `Object` unreachable) | REQ (total over `rung_kinds`) | HAS (8) | rosters.yaml:314-323 |
| 8 | tiers | seat anchor form `rung:` | one of `{realm: true}`, `{duchy: "<faction>"}`, `{territory: "<code>"}`, `{settlement: "<code>"}`; measured over offices.yaml seats: duchy Crown 1, Hafenmark 5, Varfell 4; realm 4; territory T1 10, T9 6, T15 1; settlement ALT-1 2 | REQ | HAS (28 anchors) | offices.yaml:99, populated.py `_index_anchor` |

Owed: none for the ladder itself (names/ruling are in code comments only). The duchy-to-faction map (Crown/Valorsmark, Hafenmark, Varfell) is a literal tuple in `populated.py`, not a registry row.
Conflicts: G's key is `provinces:` but its rows are territories (populated.py:1021 "geography's stale key"); code treats them as territory rungs.
Belongs elsewhere: seat contents and governance (offices agent). No key named kingdom, county, barony or march as a territorial tier exists in offices.yaml or rosters.yaml (`march` there is an act column, rosters.yaml:3565ff, not a tier).

## TERRITORY (G `provinces:`, 17 rows T1..T17) — loader: engine/season/data/geography.py:26 (`geography()`); mint populated.py:1021
Population now: 17 authored (T1-T17).   Status: AUTHORED (12 keys on every row)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id | `T<n>`, n 1..17; rung id `terr_T<n>` via `rosters.territory_rung_id` | REQ | HAS (17) | rosters.py:431 |
| 2 | identity | name | string | OPT | HAS (17) | UNREAD |
| 3 | identity | region | string (free; e.g. Eastern Lowlands, Northern Mountains, Southernmost) | OPT | HAS (17) | UNREAD (goals.yaml:345 cites T15 region in a comment only) |
| 4 | identity | sub | string (free: Capital, Heartland, ...) | OPT | HAS (17) | UNREAD |
| 5 | identity | description | string | OPT | HAS (17) | UNREAD |
| 6 | jurisdiction | faction (holder) | string, resolved by `cast.resolve_faction`; values present: Crown, Varfell, Hafenmark, Church, Uncontrolled, Schoenland | REQ | HAS (17) | READ-BY populated.py:1025, 1441 |
| 7 | position | anchor | [x,y] in canvas 1920x2880 | REQ for battle terrain (absent -> OPEN_FLAT) | HAS (17) | READ-BY modules/mass_battle/terrain.py:181, 248-249 |
| 8 | position | polygon | list of [x,y] (terrain.py:186,188 reads `terrain:` polygons, not these) | OPT | HAS (17) | UNREAD |
| 9 | membership | settlements | list of `S-nnn` ids; counts per territory T1:3 T2:3 T3:2 T4:2 T5:3 T6:2 T7:2 T8:3 T9:1 T10:2 T11:3 T12:3 T13:2 T14:2 T15:0 T16:1 T17:3 (sum 37) | OPT (containment is built from each settlement's `territory`, not from this list) | HAS (17) | UNREAD (populated.py:1044 reads the settlement-side key) |
| 10 | defence | fort_level | int; per-row values 0-3 (file text says max 4) | OPT | HAS (17) | UNREAD (terrain.py:134 states it deliberately does not read it; live value is `world_q.fortification_of`) |
| 11 | calamity | proximity_calamity | int | OPT | HAS (17) | UNREAD |
| 12 | spiritual | spiritual_weight | int | OPT | HAS (17) | UNREAD (workplan SE-06 row: "examined, not a basis") |
| 13 | economy | starting_pros | int | OPT (CR-40's disagreement source is RETIRED-KEY: `engine/engine_params/params_tables.yaml:6576`; live equivalent: settlement `stats` triplet) | HAS (17) | UNREAD; CR-40 (part4:381-391) calls for deleting all 17 lines |
| 14 | temperament | alpha | float in [0,1] | REQ per row present | HAS (16) | populated.py:393-436 (`TEMPERAMENT_FIELDS`), cohorts.yaml:145-161 |
| 15 | temperament | beta | float in [0,1] | REQ per row present | HAS (16) | same |

Temperament block (cohorts.yaml `temperaments:`): optional as a block (absent -> uniform cohorts); if present, rows must be exactly `{territory, alpha, beta}`, territory in G provinces, no duplicates. Authored rows: 16 (T1-T14, T16, T17). No row for T15 (Askeheim, 0 settlements, so no cohort). Marked `[ASSUMPTION; medium; Jordan to correct]` (cohorts.yaml:113). Only the alpha:beta ratio is used.
RETIRED-KEY re-check: alpha/beta stay current (a live loader, populated.py:393-436, reads cohorts.yaml:145-161). Their prose source's drift mechanics ("faction-effective-temperament model", cohorts.yaml:113-121) sit on the retired Key substrate and are NOT parameters here; live equivalent for drift: none found. No other row in this file rests only on a Key-based source or the retired `params_tables.yaml`; the one reference to it is the CR-40 comparison, marked RETIRED-KEY below.
Owed:
- Territory temperament conviction/affiliation content: no source for an `altonia` concern member; no Piety Track start value for T16; the two Piety tables disagree on T1,T2,T3,T6,T13,T14; no split rule for the bipolar track (SE-06, HELD, B10-Z; part3:436).
- Per-territory typology name/rationale are not carried (cohorts.yaml:118-120).
- CR-40: delete `starting_pros` x17 and add header note (part4:381-391).
Conflicts: workplan CR-40 says `starting_pros` disagrees with `params_tables.yaml:6576` (RETIRED-KEY) in 11 of 17: UNVERIFIED (not opened). G header says "PROVISIONAL" while line 1 says "CANONICAL".
Belongs elsewhere: faction identity (faction agent); per-territory `controller` of subordinate sub-holdings (see settlement).

## TERRITORY ADJACENCY (G `adjacency:`) — loader: data/geography.py:40 `adjacent_territories()`
Population now: 26 edges (road 22, gate 2, coastal 1, mountain_pass 1). Every one of T1-T17 appears in at least one edge.   Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | border | from | territory id `T<n>` | REQ | HAS (26) | geography.py:58 (`e["from"]`) |
| 2 | border | to | territory id | REQ | HAS (26) | geography.py:58 |
| 3 | border | type | string observed {road, gate, coastal, mountain_pass}; closed set not declared | OPT (not read) | HAS (26) | NO-READER (geography.py docstring: type "is not read") |

Edges are made undirected by the reader. Edges with non-road type: T1-T16 coastal; T6-T15 gate; T13-T15 gate; T10-T11 mountain_pass.
Owed: CP-T10-02 (part14:214) will add a BFS `band(territory)` over these edges (plan, no carrier yet), root `terr_T15`.
Conflicts: none. `radiation_bands:` (below) deliberately unread by game code.
Belongs elsewhere: none.

## SETTLEMENT IDENTITY / PLACE-IN-MAP (G `settlements:`, S-001..S-037) — loader: populated.py:1040, 1072
Population now: 37 authored.   Status: AUTHORED (7 keys on every row; `controller_subordinate` on 1)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id | `S-nnn`; rung id `set_<slug>` | REQ | HAS (37) | READ-BY populated.py:1041 |
| 2 | identity | name | string | OPT (used for cohort display names; falls back to id) | HAS (37) | READ-BY populated.py:1834 |
| 3 | place | territory | one of G provinces ids | REQ (KeyError if absent) | HAS (37) | READ-BY populated.py:1044 |
| 4 | identity | type | enum {Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1}; closed set owner `venues.yaml: buildings` keys (all seven covered) | REQ (KeyError) | HAS (37) | READ-BY populated.py:1072-1078 |
| 5 | jurisdiction | controller | string: Crown 15, Hafenmark 10, Varfell 10, Church 1, Schoenland 1 | OPT | HAS (37) | UNREAD (repo-wide grep outside .designs/.audit: only tests/valoria/test_mass_battle_terrain.py names the key; code reads territory `faction`) |
| 6 | jurisdiction | controller_subordinate | string (present on S-014 only: Löwenritter) | OPT | HAS (1) | UNREAD |
| 7 | position | coords | [x,y] | OPT | HAS (37) | UNREAD (CP-T10-01's planned `route` would read them) |
| 8 | description | description | string | OPT | HAS (37) | UNREAD |
| 9 | stats | stats | [Prosperity, Defense, Order] triplet | belongs to settlement-stats agent | HAS (37) | UNREAD (no reader in engine/, modules/, tools/, harness; tests/ only); CR-40 names it the one home of Prosperity |

Owed: none for identity. Territory T15 holds 0 settlements.
Conflicts: territory `faction` and settlement `controller` differ only for T15 (no settlements) by set comparison; no other territory shows mixed controllers.
Belongs elsewhere: stats/population/infrastructure and venue `quarters`/`buildings` (settlements agent).

## SETTLEMENT ADJACENCY / ROUTES (G `settlement_adjacency:`)
Population now: 55 edges (road 54, sea 1: S-001 to S-037). Every settlement appears in at least one edge.   Status: AUTHORED, NO-READER
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | route | from | `S-nnn` | OPT | HAS (55) | NO-READER |
| 2 | route | to | `S-nnn` | OPT | HAS (55) | NO-READER |
| 3 | route | type | observed {road, sea} | OPT | HAS (55) | NO-READER |
| 4 | route | note | string | OPT | HAS (55) | NO-READER |
| 5 | route | route pricing / leg cost | `route` returns None through a `mountain` settlement; priced by terrain matrix; ships OFF | PLAN | NONE | CP-T10-01 (part14:202-209), IN-47 |

Owed: a `route`/`terrain_type_at(point, *, geography)` owner and a `route` query row in `references/module_contracts.yaml` (CP-T10-01, B10-18). Person-side price reading of a leg is `[GAP: unowned]` (T10 D-1).
Conflicts: none.
Belongs elsewhere: `Person.travel_leg` (carriers.py:757, list[str] of destination ids, written by `move`/`migrate`/`march` via `_relocate`, read by `decision/budget.py:60` times `budget_leg_penalty`) is person carrier state, not authored geography.

## TERRAIN POLYGONS (G `terrain:`) and cost matrix — reader: modules/mass_battle/terrain.py:185, 247 (via `MassBattleInput.geography`)
Population now: 20 polygons (highland 4, plains 4, fjord_coast 3, marsh 3, mountain_pass 2, coast 2, mountain 1, forest 1).   Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | terrain | id | string `terrain-...` | OPT | HAS (20) | altonian_passes.terrain_id refers to it; no code reader |
| 2 | terrain | type | enum observed 8: {plains, coast, fjord_coast, forest, highland, marsh, mountain_pass, mountain}; mapped to six A.9 rows by `terrain.py _TYPE_TO_ROW` (unlisted type -> OPEN_FLAT) | REQ | HAS (20) | terrain.py:185-195 |
| 3 | terrain | polygon | list of [x,y] (smallest-area containing polygon wins) | REQ | HAS (20) | terrain.py:185 |
| 4 | terrain | description | string | OPT | HAS (20) | NO-READER |
| 5 | terrain | terrain_cost_matrix | 11 keys: plains 1.0, coast 1.0, fjord_coast 2.5, forest 1.5, highland 1.5, marsh 2.0, mountain_pass 2.0, mountain 999.0, river_crossing_no_bridge 1.5, river_crossing_with_bridge 1.0, road_overlay 0.7 | OPT | HAS (11) | NO-READER now; planned reader CP-T10-01 |
| 6 | terrain | vision_range (base_pixels 240; terrain_factor 8; weather_factor 5; season_factor 4) | numbers | OPT | HAS | NO-READER |
| 7 | terrain | march_budget (base_per_military_point 100, cavalry_modifier 1.5, skirmish_modifier 1.3) | numbers | OPT | HAS | NO-READER |

Owed: none authored-missing. Matrix and vision/march blocks are in the file's `[PROVISIONAL]` calibration (G header, ED-781).
Conflicts: terrain.py maps `fjord_coast` to FOREST_BROKEN and `coast` to OPEN_FLAT by ASSUMPTION (terrain.py:49-66).
Belongs elsewhere: mass-battle terrain rows (A.9) belong to the battle agent.

## WATER, BRIDGES, FORGETTING ZONE, CALAMITY BANDS, PASSES (G)
Population now: 1 lake, 1 river, 2 bridges, 1 forgetting zone, 6 radiation bands, 2 passes + 1 naval.   Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | water | lakes[] {id, shape, center, rx, ry, description} | 1 row (lake-eidursjo) | OPT | HAS | NO-READER |
| 2 | water | rivers[] {id, type, vertices, description} | 1 row (river-valoris, navigable); vertices read for river-crossing test | REQ for crossing test | HAS | terrain.py:252 |
| 3 | water | bridges[] {id, coords, crosses, description} | 2 rows | OPT (terrain.py: "bridges: is NOT read" by assumption) | HAS | NO-READER |
| 4 | hazard | forgetting_zone {id, polygon, description} | 1 | OPT | HAS | NO-READER |
| 5 | hazard | radiation_bands[] {band 0-5, center, radius, territories, description} | 6 rows, band 0 = T15 | OPT | HAS | NO-READER by design; CP-T10-02 keeps it as test oracle |
| 6 | border | altonian_passes {primary: T3/S-007/terrain-pass-lowenskyst, secondary: T10/S-021/terrain-pass-spartfell, naval: description only (IP 75+ via Schoenland)} | 3 keys | OPT | HAS | NO-READER (terrain.py:31 comment only) |
| 7 | scale | scale_anchors {hex_grid_size_px 32, strategic_to_tactical_zoom 4, settlement_scene_radius 80} | ints | OPT | HAS | NO-READER (port) |
| 8 | meta | meta {schema_version, canvas [1920,2880], origin, axis, units_to_pixels 16, authority, status} | | OPT | HAS | NO-READER |

Owed: none authored-missing.
Conflicts: G cross-reference footer cites `designs/...` paths, a dissolved tree (CLAUDE.md §3).
Belongs elsewhere: none.

## POINT OF INTEREST (G `poi_catalog:`)
Population now: 17 rows, one per territory, counts only: {resource, secret, remnant, anomaly} ints; total 31 POIs counted, no names.   Status: PARTIAL (counts only)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | poi | per-territory counts resource/secret/remnant/anomaly | int >=0 | OPT | HAS (17) | NO-READER |
| 2 | poi | authored POI records (name, kind, depth level) | 2-6 per territory | PLAN | NONE | ED-507 (part10:34), LEAVE until a reader or Jordan-authored names land |

Owed: named POIs (ED-507; no carrier, no reader).
Conflicts: ED-507 asks 2-6 POIs per territory; counts give 0-4 per territory (T15 = 4).
Belongs elsewhere: none.

## FOREIGN / OFF-MAP SEATS — carrier: rosters.yaml `foreign_cast.by_faction` (rosters.py:1069 `FOREIGN_CAST`); mint populated.py:945-955
Population now: 1 row (Altonia: territory code `ALT`, settlement code `ALT-1`).   Status: PLACEHOLDER ([ASSUMPTION; medium; Jordan to correct], codes are the author's)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | foreign | faction key | a faction name; Schoenland excluded (already in realm as root T16) | REQ | HAS (Altonia) | rosters.yaml:1835-1867 |
| 2 | foreign | territory.code | string; root `territory` rung with no `contain` edge to realm | REQ | STUB | rosters.yaml:1866 |
| 3 | foreign | settlement.code | string; one settlement under the root | REQ | STUB | rosters.yaml:1867 |
| 4 | foreign | homeland place names | none (a Rung carries no name) | PLAN | NONE | rosters.yaml:1859-1863 ("Jordan names the homeland places") |

Owed: homeland names for Altonia; scheduled arrival, border perception channels, Schoenland trade demand (FA-01) are unbuilt (rosters.yaml:1857).
Conflicts: none.
Belongs elsewhere: Schoenland's T16/S-037 (faction agent for its cast).

## Cross-cutting
Owed: the "Jordan decides" items nearby: territory `fort_level` vs live fortification (terrain.py:134-137 records G's value disagreed with live for T2); a `province` threshold (none stated, world_q.py:2186).
Not found in code/plan (so no rows): "realm temperament", climate tags, resource tags per map region (only poi_catalog counts), border/frontier objects other than adjacency edges and passes, claims fields (holding is the `hold` Tenure built at populated.py:1441 from `faction`), neighbours beyond the two adjacency lists. `proposals/2026-10-07-settlements-computation-modules.md` yielded no map fields (read by grep).
