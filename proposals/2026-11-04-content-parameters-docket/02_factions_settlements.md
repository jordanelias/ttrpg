# Content parameters docket, chapter 02: Factions, offices, settlements

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Paths are repo-relative. `RO` = engine/season/rosters.yaml, `RP` = engine/season/data/rosters.py, `GEO` = systems/settlements/valoria_geography_v30.yaml, `POP` = engine/season/harness/populated.py, `FX` = engine/season/data/fixtures.py. Counts measured by loading the YAML.

## FACTION (roster) — carrier/loader: RO `factions` (from_names: faction) -> RP:1058 `FACTIONS`; names at references/names_index.yaml (token_class: faction)
Population now: 10 names authored: Crown, Church of Solmund, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds, Schoenland (foreign), Altonia (foreign), faction x (test fixture, governance_spine).   Status: PARTIAL (name and leader only; the rest is derived or absent)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | faction name (canonical, aliases, patterns) | string, `names_index.yaml` entry with `token_class: faction`; roster has no literal members (a pointer plus `values:` is refused) | REQ | HAS (10) | RO `factions` (row H-99); RP:1058 |
| 2 | identity | foreign flag / its two places (territory code, settlement code) | `foreign_cast.by_faction.<f>.{territory.code, settlement.code}`; row must name a roster faction (RP:1076-1084) | REQ for a foreign faction | HAS (Altonia: ALT, ALT-1; Schoenland is a geography territory T16, not in foreign_cast) | RO `foreign_cast`; POP:1040 |
| 3 | creed | leader (case id of founding head) | NPC id; `faction_leaders.by_faction` | OPT (absent = creed is a `HOLDS`, faction holds no provinces) | HAS 7 (Crown NPC-020, Church NPC-021, Hafenmark NPC-050, Varfell NPC-052, Restoration NPC-003, Löwenritter NPC-070, Altonia NPC-089); NONE for Guilds, Schoenland | RO `faction_leaders`; cast.py:366; POP:1274 |
| 4 | creed | role template (expected-pursuit bundle) | enum {sovereign, ecclesiastical, mercantile-procedural, intelligence-diplomatic, reformist, military-order} (RO `role_templates.values`), mapped `by_faction` | OPT (absent = no creed OUGHT, no loyalty read) | HAS 6 factions; Guilds, Schoenland, Altonia, faction x NONE. Note `intelligence-diplomatic` is mapped to no faction | RO `role_templates`; POP:1274-1285 |
| 5 | creed | template pursuit weights | table `role_template_pursuits.cells[template][pursuit]`, number, default 0.0, keyed on `role_templates` x `pursuits` | OPT | HAS (6 templates, 3-5 weights each) | RO tables `role_template_pursuits` |
| 6 | holdings | territories held (starting control) | faction name per territory row in GEO `provinces.<T>.faction` (value `Uncontrolled` writes no edge); held by the leader person, so a faction with no leader holds nothing | REQ per territory | HAS (Crown 6, Varfell 4, Hafenmark 4, Church 1, Schoenland 1, Uncontrolled 1) | POP:1395-1440; cast.py:172 |
| 7 | holdings | sub-organisations (offices' bodies) | `office_bodies.faction`: body name -> faction (19 bodies); `office_bodies.function`: body -> text | REQ per body used by a seat | HAS (19 bodies) | RO `office_bodies`; RP:1063,1228 |
| 8 | holdings | seats the faction owns | see OFFICE SEAT | | | |
| 9 | membership | member -> faction | per-person `faction` cell in references/npc_registry.yaml (cast file; another agent) | REQ per cast row | see Belongs elsewhere | cast.py `faction_of` |
| 10 | pursuits | faction goals (OUGHTs) | engine/season/goals.yaml (another agent) | OPT | Belongs elsewhere | POP:759-874 |
| 11 | derived | members, leaders, footprint, mustered, legitimacy, head, cohesion, wealth | queries over the above; nothing stored on a faction | DERIVED | n/a | appendix_A3 Q4 (map only); `head` has no writer |

Owed:
- Role template, leader and creed absent for Guilds, Schoenland (RO `role_templates` note; `faction_leaders`), and for Altonia/faction x (role template).
- Faction-level fields named by the held suite, no carrier: mission text, culture, beliefs, foils (PROPOSED-ONLY, proposals/2026-10-28-content-architecture-suite/appendix_A3_faction_settlement.md Q4).
- `fac.*` stats are retired (references/descriptor_registry.yaml); no faction stat block is called for by code.
Conflicts:
- names_index lists `faction x` (test fixture) as a faction; RO `factions` therefore carries it, so it gets a Proposition in the authored realm (governance_spine.yaml header).
- GEO calls Church `Church`; roster canonical is `Church of Solmund` (alias resolved by cast.resolve_faction).
- GEO `provinces.<T>.faction` for T16 is Schoenland, which has no leader, so the province is unheld at build (POP:1430 comment).
Belongs elsewhere: faction membership cells and cast (npc_registry.yaml / npcs.yaml); faction goals (goals.yaml); faction-held covenant/war verbs (verb_table.yaml).

## AFFILIATION (creed-side roster) — carrier/loader: RO `affiliations` (from_descriptor: affiliation_roster) -> engine/season/data/affiliations.py:31-186
Population now: 5 authored: solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics (references/descriptor_registry.yaml `affiliation_roster`, scale 0-5; concerns: church, einhir, altonia)   Status: AUTHORED (roster) / PARTIAL (engagement cells)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | affiliation name | string; roster owner is descriptor_registry.yaml, exported to engine/engine_params/descriptors.json | REQ | HAS (5) | RO `affiliations`; affiliations.py:31 |
| 2 | identity | `concerns` grouping (church/einhir/altonia -> names) | mapping | OPT | HAS | descriptor_registry.yaml `affiliation_roster.concerns` |
| 3 | allegiance | person's held affiliations with intensity | `Person.conviction`: {affiliation: 0-5} ; `conviction_map` refuses unknown names or out-of-scale (affiliations.py:38-70) | REQ per person who holds any | HAS on cast rows (`affiliations:`); NONE on cohorts and corpus worlds | affiliations.py:38; state/carriers.py |
| 4 | incompatibility | pairs that cannot be co-held | table `incompatible` (RO tables) read by `_load_incompatible` (affiliations.py:72-126; Forbidden on malformed) | OPT | HAS (table present) | affiliations.py:72 |
| 5 | engagement | shared column `sacred`: verb -> cell | `affiliation_engagement.cells.sacred.<verb>`: number or null, keyed on verb_table | OPT | HAS 11 cells (9 non-null) | affiliations.py:128-186 |
| 6 | engagement | per-affiliation cells | cell must be -1 or 1 (loader refuses other values); a verb carries shared or per-affiliation cells, never both | OPT | HAS 3 (solmund_orthodoxy thread_read -1, inner_tradition +1, thread_truth +1); einhir_restoration and altonian_civics NONE | affiliations.py:166-176 |

Owed:
- Content-keyed violations (what is said or recorded) have no tag carrier; nothing authored (RO `affiliation_engagement` note R-C4.3).
- Cells for `restore` not carried (RO note (i)).
- Cohort convictions held (SE-06): cohorts.yaml `temperaments` names the residue; workplan part3 SE-06 (HELD).
Conflicts: none found.
Belongs elsewhere: pursuit roster and axes (`pursuits`, `pursuit_axes`; person scope); verb_table rows.

## OFFICE TITLE LADDER (rung-to-title) — carrier/loader: engine/season/offices.yaml `titles.domains` -> RP `TITLE_DOMAINS`/`title_domain`
Population now: 11 titles authored: King, Queen (realm); Duke, Duchess (duchy); Count, Countess (province); Lord (territory); Mayor (settlement); Community Leader (community); Family Head (hearth); Individual (person)   Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | ladder | title -> rung kind | title string -> member of `rung_kinds` (RO) | REQ | HAS 11 | offices.yaml `titles`; RP `title_domain` |
| 2 | ladder | rung kinds themselves | enum {person, hearth, community, settlement, territory, province, duchy, realm}, ordered; `contain` must ascend strictly | REQ (closed in practice, `open: true`) | HAS 8 | RO `rung_kinds` |
| 3 | ladder | scale of each rung kind | enum {Personal, Relational, Territorial, Structural} per rung kind | REQ | HAS 8 (`open: false`) | RO `scale_of_rung` |
Owed: none. Conflicts: POP builds no `province` rung (a query, `provinces_of`); the ladder still lists it (POP:975-1000 comment). Belongs elsewhere: territory/province/duchy/realm rung content (geography agent).

## OFFICE SEAT — carrier/loader: engine/season/offices.yaml `seats` + `foreign_seats` -> RP:140-194 (`_load_offices`), state/carriers.py:949 `Office`
Population now: 31 seats in `seats` + 2 in `foreign_seats` (off_katepano, off_kommerkiarios; both Altonia). Method (measured): `yaml.safe_load(offices.yaml)`; faction = seat `faction`, else `rosters.yaml office_bodies.faction[body]`; Counter over seats. By faction: Crown 11, Church of Solmund 7, Hafenmark 4, Varfell 4, Löwenritter 3, Guilds 1, Restoration Movement 1. By rung kind: territory 17, duchy 10, realm 4, settlement/community/hearth 0. Conferral: appointed 18, elected 8, null 4, inheritance 1. Revocation: null 16, rung_above_same_faction 13, rung_above_in_holdings 2. Seats with a holder: 31 of 31. Seats with obligees: 2 (off_king 1, off_restoration_leader 1). No seat carries `upkeep` or `scope_rung`.   Status: PARTIAL (no seat below territory: zero seats at settlement, community or hearth rungs)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | seat id | unique string `off_*`, one namespace across `seats` and `foreign_seats` (RP:172) | REQ | HAS 33 | RP:162-177 |
| 2 | identity | post (title) | string; not normalised to the title list (e.g. "Cardinal of Justice") | REQ | HAS 33 | carriers.py:951 |
| 3 | belonging | faction | roster faction name; derived from `body` when body is set | REQ one of faction/body (else refusal) | HAS | carriers.py:989-1010 `office_faction` |
| 4 | belonging | body | `office_bodies` key or null; body and faction must agree | OPT | HAS | RP:1063,1228 |
| 5 | placement | rung anchor | `{realm: true}` / `{duchy: <faction>}` / `{territory: T<n>}` / `{settlement: <S-code>}`; resolved by POP `resolve_anchor`/`_index_anchor`; also a `{hearth: "<S-code>:<slug>"}` form for planned works | REQ | HAS (measured: realm 4, duchy 10, territory 17; territories used T1, T9, T15; foreign seats anchor settlement ALT-1) | POP:972 |
| 6 | powers | remit acts | subset of enum {issue, determine, confer, revoke, dispatch, convene} (RO `remit_acts`); a seat with none gets the testing default `remit_default` | REQ field (list may be empty) | HAS | carriers.py:970-980; RO `remit_default` (NOT CANON fixture) |
| 7 | filling | conferral basis | enum {appointed, elected, annex, inheritance} or null (RO `conferral_bases`) | OPT | HAS (measured: appointed 18, elected 8, inheritance 1, null 4) | carriers.py `Office.conferral` |
| 8 | filling | revocation basis | enum {rung_above_same_faction, rung_above_in_holdings} or null (RO `revocation_bases`) | OPT | HAS (measured: null 16, rung_above_same_faction 13, rung_above_in_holdings 2) | carriers.py `Office.revocation` |
| 9 | filling | binds basis | enum {members_by_admission} | OPT (default) | default only | RO `binds_bases` |
| 10 | tenure | initial holder | NPC id or absent | OPT | HAS | offices.yaml `holder` |
| 11 | tenure | obligees (service edges) | list of NPC ids | OPT | HAS (2 seats, 1 obligee each) | offices.yaml `obligees` |
| 12 | economics | upkeep | int or null (null defers to fixture `default_upkeep`=1, FX:971) | OPT | NONE on all seats | carriers.py:982; FX `default_upkeep` |
| 13 | scope | scope_rung | string or null | OPT | NONE | carriers.py:955 |
| 14 | succession | heir mapping | `successions.values`: seat -> heir seat | OPT | HAS 1 (off_king -> off_heir) | RO `successions` |
| 15 | documentation | source, note | text | OPT | HAS | offices.yaml |

Owed:
- Local seats: no Mayor, Community Leader or Family Head seat is authored. Title `Mayor: settlement` is ruled; plan M29 answered "no rows until a reader needs one" (workplans/valoria_master_workplan_v10_part15.md:88-90); suite E2 proposes them (PROPOSED-ONLY appendix_A3 Q5).
- Four seats carry conferral null (measured); offices.yaml header calls the hereditary-seat nulls a judgment call.
- Remit is a testing default, not canon (RO `remit_default`, Jordan 2026-09-18).
- Settlement governance shapes (elected mayor, elected council, assigned governor, assigned council) have no vocabulary (governance_spine.yaml header).
Conflicts:
- offices.yaml `meta.source` says 31 authored seats; measured 31 in `seats` plus 2 in `foreign_seats`, consistent.
- offices.yaml header says `conferral` for heredity is null for 4 seats while RO `conferral_bases` has `inheritance` (only off_king uses it).
Belongs elsewhere: seat-verb eligibility (verb_table.yaml); `holder`s are persons (npc_registry.yaml); ending conditions (RO `endings`).

## GENERIC GOVERNANCE SPINE (test fixture) — engine/season/governance_spine.yaml
Population now: 13 rungs authored (realm 1, duchy 2, province 2, territory 2, settlement 2, community 2, hearth 2), all under `faction x`   Status: PLACEHOLDER (declared a test fixture, not canon)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | rung id | string `lr_*` | REQ | HAS 13 | governance_spine.yaml `rungs` |
| 2 | identity | kind | member of `rung_kinds` | REQ | HAS | same |
| 3 | structure | under (parent rung id) | rung id; null only for realm | REQ | HAS | same |
| 4 | post | generic post label | string | REQ | HAS (Sovereign, Duke, Count, Lord, Mayor, Community Leader, Hearth Head) | same |
Owed: none called for. Conflicts: post `Hearth Head` differs from the title list's `Family Head`. Belongs elsewhere: none.

## SETTLEMENT (static row) — carrier/loader: GEO `settlements` (37 rows) read by POP:1021-1060; rung built as `set_<slug>`
Population now: 37 authored (S-001..S-037)   Status: AUTHORED for what the engine reads; PARTIAL for the rest
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | settlement id | `S-NNN` | REQ | HAS 37 | POP:1021 |
| 2 | identity | name | string; used for cohort display name only | OPT (display) | HAS 37 | POP seat_cohorts `names` |
| 3 | identity | territory (parent) | a GEO territory code (T1..T17) | REQ | HAS 37 | POP:1021 (`contain` edge) |
| 4 | identity | type | enum, must be a key of venues.yaml `buildings`/`quarters`: {Seat, City, Town, Village, Fortress, Fortress-City, Cathedral-City} (7, owner engine/season/venues.yaml) | REQ (KeyError otherwise) | HAS 37 (Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1) | POP:1070-1080 |
| 5 | governance | controller | faction name (Crown 15, Hafenmark 10, Varfell 10, Church 1, Schoenland 1); `controller_subordinate` on 1 row | not read by engine (holding comes from territory `faction`) | HAS | GEO only |
| 6 | location | coords | [x,y] pixels | not read by season loop | HAS 37 | GEO |
| 7 | state seeds | stats | [Prosperity, Defense, Order] triple | not read by engine; CR-40 keeps Prosperity at settlement grain | HAS 37 | workplans/valoria_master_workplan_v10_part4.md:380-383 (CR-40); appendix_A3 Q5 (PROPOSED-ONLY seeds) |
| 8 | colour | description | text | not read | HAS 37 | GEO |
| 9 | links | settlement_adjacency (road 54, sea 1; 55 edges) | list of {from,to,type,note} | not read by engine | HAS | GEO; appendix_A3 Q5 "unread" |

Owed:
- Prosperity/Defense/Order are authored and unread; seeding them into garrison condition, starting stores and stance is PROPOSED-ONLY (appendix_A3 Q5 MVP settlement).
- CR-40 asks deleting the 17 `starting_pros` lines (territory scope, see Belongs elsewhere).
Conflicts: GEO settlement `controller` and territory `faction` both state holder; engine reads only the territory's. Appendix_A3 Q5 says Seat 2 / Town 15 etc.; measured matches.
Belongs elsewhere: GEO `provinces` (17 rows: name, faction, region, sub, anchor, polygon, fort_level, spiritual_weight, proximity_calamity, starting_pros, settlements, description), `adjacency` (26: road 22, gate 2, coastal 1, mountain_pass 1), `terrain` (20), `terrain_cost_matrix`, `vision_range`, `march_budget`, `water`, `bridges`, `forgetting_zone`, `radiation_bands`, `altonian_passes`, `poi_catalog` (17), `scale_anchors`, `meta`, and cohorts.yaml `temperaments` (16): geography agent.

## SETTLEMENT POPULATION (cohort) — carrier/loader: engine/season/cohorts.yaml `cohorts` -> POP `seat_cohorts` (~line 450-520)
Population now: 37 cohorts authored, each weight 2 (one per settlement)   Status: PARTIAL (weights only; no politics)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | population | cohort rung | a built rung id (`set_s_NNN`); unknown id refuses | REQ | HAS 37 | POP seat_cohorts |
| 2 | population | cohort weight | positive number; refuses if > `capacity(rung)` | REQ | HAS (2 each) | POP seat_cohorts; ED-SE-0051 |
| 3 | pursuits | pursuits via territory temperament | cohorts.yaml `temperaments` (geography agent) | OPT | HAS | SE-06 |
| 4 | allegiance | cohort conviction / stance / commit | none carried | PLAN | NONE | workplans part3 SE-06 (HELD); appendix_A3 Q5 (PROPOSED-ONLY) |
| 5 | guards | guards (seat, weight) | cohorts.yaml `guards` | OPT | HAS (off_king 4, others) | cohorts.yaml |
Owed: cohort conviction and stance (SE-06). Conflicts: case-derived cast already overfills two settlements (S-001 10 vs 9, S-036 8 vs 6) per POP comment. Belongs elsewhere: `guards` block is cohorts/people scope if another agent owns it.

## SETTLEMENT INFRASTRUCTURE: SITE KINDS AND BUILDINGS — carrier: RO `site_kinds`, `wear_per_season`, `capacity_floor`, `works_cost`, tables `site_yield`, `band_floors`; state/carriers.py:786 `Site`; built per settlement at POP:1096-1150
Population now: 9 site kinds authored; 3 of them yield (harbour, seam, body); 1 garrison and per-kind sites built per settlement   Status: AUTHORED (values flagged invented/assumption in RO notes)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | infrastructure | site kind roster | enum {harbour, seam, body, dwelling, garrison, barracks, archery_range, stable, siege_workshop} (RO `site_kinds`, H-07) | REQ | HAS 9 | RO `site_kinds`; carriers.py:786 |
| 2 | infrastructure | condition scale | int, FX `condition_scale`=1000 | REQ | HAS | FX:217 |
| 3 | infrastructure | per-settlement site endowment (which kinds each settlement gets, starting condition) | POP builds every settlement the same: one site per yielding kind plus a garrison, condition = scale; no per-settlement authoring | PLAN | STUB (uniform) | POP:1096-1150; appendix_A3 Q5 "ground endowment" CP-T08-02 (PROPOSED-ONLY) |
| 4 | infrastructure | yield per season | `site_yield.cells[kind][matter]` int: harbour grain 40 salt 30; seam ore 50 timber 10; body none | REQ cell table | HAS (INVENTED per RO note) | RO tables `site_yield`; modules/settlements/produce.py |
| 5 | infrastructure | wear per season | `wear_per_season.rates[kind]` int: 10 for harbour/seam/body, 0 others | REQ | HAS (H-07) | RO `wear_per_season` |
| 6 | infrastructure | band floors | `band_floors.cells[kind][use]` int; dwelling and non-producing kinds empty | OPT | HAS (INVENTED) | RO tables `band_floors` (H-08) |
| 7 | infrastructure | works cost | `works_cost.costs[plan kind][matter]` positive int; plan kind in rung_kinds or site_kinds; 10 kinds all priced 10 of grain (hearth, community) or timber | REQ per kind that may be founded | HAS 10 | RO `works_cost`; FX loader `_check_works_cost`; loop/effects_founding.py:71 |
| 8 | buildings | settlement type -> quarters (community rungs) and buildings (hearth rungs: slug, quarter, serves) | engine/season/venues.yaml `quarters`, `buildings` | REQ per type | owned by venues agent | POP:1070-1100 |
| 9 | housing | dwelling site per building (one per hearth) | built by rule; capacity = max(floor, dwellings in subtree) | DERIVED | built | modules/settlements/housing.py |
| 10 | housing | capacity floor | `capacity_floor.floors[kind]` int: dwelling 1, others 0 | REQ | HAS (H-167) | RO `capacity_floor` |
| 11 | fortification | garrison condition | Site kind `garrison`, condition 0..scale; fortification = mean/scale | DERIVED from Site | HAS (all = scale) | modules/settlements/fortification.py; POP:1137 |
| 12 | fortification | garrison seeded from Defense stat | | PROPOSED-ONLY | NONE | appendix_A3 Q5 |
| 13 | fabric | works terms (declared/matured) of a live works | Record/hold data at runtime; scale from fixture | DERIVED | n/a | modules/settlements/fabric.py |
Owed: per-settlement site endowment and starting condition are uniform by build rule; yield, floors and works prices are flagged invented in RO notes (H-93, H-08, H-166).
Conflicts: RO `works_cost` prices `hearth`/`community` in grain and site kinds in timber, with equal amounts of 10 (placeholder-looking, graded `declared/halved/doubled` sweep).
Belongs elsewhere: venues.yaml building rows (7 types) and `planned_works` (venues agent); `hole_register.yaml` rows.

## SETTLEMENT ECONOMY (larder, produce, provision, subsistence) — carriers: RO `matter_kinds`, `subsistence_weight`, `hunger_bands`; FX; modules/settlements/{larder,subsist,produce,provision}.py
Population now: 5 matter kinds, 2 subsistence weights, 4 hunger bands authored   Status: AUTHORED (ration values assumption-grade)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | goods | matter kind roster | enum {grain, salt, timber, ore, coin}, open registry (RO `matter_kinds`, H-11) | REQ | HAS 5 | RO `matter_kinds` |
| 2 | stores | starting stores per rung | `Rung.stores` {kind: int}; authored where? set in realm builder, not in a settlement data file | REQ for a larder to exist | NONE after search: no `stores` value is authored in rosters.yaml (only prose and the `subsistence_weight`/`site_yield` tables), data/rosters.py, data/fixtures.py, modules/settlements/*, or the realm builder (populated.py references `stores` only in the census, lines 1858-1880). A realm rung starts with empty stores and is credited only by `produce` at MATTER (`site_yield`). Test worlds set stores by hand (harness/probes.py:80, scarce.py:99,153). FX:632 records that case worlds hold zero stores | modules/settlements/larder.py; produce.py; FX:632 |
| 3 | subsistence | per-eater ration weight per kind | `subsistence_weight.weights`: grain 2, salt 1 (x `Person.weight`, per cohort) | REQ | HAS | RO `subsistence_weight`; larder.py |
| 4 | subsistence | body loss per unit short | FX `body_step`=10 (control 0, swept 0/10/67) | REQ | HAS | FX:643 |
| 5 | subsistence | hunger band names (ordered) | {starving, hungry, lean, fed} | REQ (`open: false`) | HAS 4 | RO `hunger_bands` (REM-50) |
| 6 | subsistence | hunger band thresholds / per-head need | rule chosen by plan | PLAN | NONE | CR-22 (workplans/valoria_master_workplan_v10_part4.md:159-164) |
| 7 | production | season factor and its draw | FX `season_factor`=1.0, `season_factor_draw` () | OPT | HAS (control) | FX:490-500; produce.py |
| 8 | production | lattice coupling across borders | FX `lattice_coupling`=0 | OPT | HAS (control) | FX:660 |
| 9 | provision | field provisioning on/off | FX `field_provisioning`=False | OPT | HAS (control) | FX:745; provision.py |
| 10 | provision | ration for a field | = `subsistence_weight` | DERIVED | | provision.py |
| 11 | governance | seat upkeep | FX `default_upkeep`=1 | OPT | HAS | FX:971 |
| 12 | levy | standing levy / tax edict | | PLAN | NONE | CP-T08-07 (workplans part3:247) |
Owed: where starting stores per rung are authored was not located in a data file (item 2); per-head need rule (CR-22); tax edict (CP-T08-07).
Conflicts: none. Belongs elsewhere: `season_factor` weather events (events scope); the census output; `hole_register.yaml`.

## PROPOSED-ONLY rows (from proposals; not authority; nothing here has a carrier unless stated)
| # | entity | parameter | domain (as proposed) | req | now | cited at |
|---|---|---|---|---|---|---|
| P1 | faction | creed text / mission, culture, beliefs, foils, headquarters | colour fields, read by nothing | PROPOSED-ONLY | NONE | proposals/2026-10-28-content-architecture-suite/02_P1_templates.md "Faction dossier"; appendix_A3 Q4 |
| P2 | faction | relations at start (war, treaty, alliance) | list; `at_war` has no producer | PROPOSED-ONLY | NONE | 02_P1_templates.md "Faction dossier" |
| P3 | faction | goal rows per faction | goals.yaml rows (e.g. goal_crown_peninsular_sovereignty) | PROPOSED-ONLY (carrier exists, another agent) | see goals.yaml | 02_P1_templates.md "Crown (worked)" |
| P4 | settlement | Prosperity/Defence/Order triplet used as build seeds: starting stores, garrison condition, cohort stance | GEO `stats` [P,D,O] -> seeds | PROPOSED-ONLY | triplet HAS, seeding NONE | 02_P1_templates.md "Settlement dossier"; appendix_A3 Q5 |
| P5 | settlement | cohort seeds: pursuits, conviction, stance (e.g. S-006 wealth .4, community .3, stance -1 toward the toll's holder) | existing Person fields | PROPOSED-ONLY | NONE | 02_P1_templates.md "Goldenfurt S-006 (worked)" |
| P6 | settlement | local Mayor seat per settlement (vacant), site endowment, planned works (M5), colour | seat rows; Site rows | PROPOSED-ONLY | NONE | 02_P1_templates.md "Settlement dossier"; workplans part15 M29 |
| P7 | settlement | extra site families and kinds: PRODUCER (croft, field, mill, quarry), VESSEL (granary, warehouse, cistern, byre; a bound on `Rung.stores`, no reader column exists), ENCLOSURE (rampart, gate, ditch, tower, keep), HALL (moot_hall, guildhall, minster, chapter_house), DWELLING (cottage, townhouse, longhouse, barracks). Each new kind needs `wear_per_season` and `band_floors` rows or the world does not load; `site_yield` optional | enum rows in `site_kinds` | PROPOSED-ONLY (illustrative kinds) | roster has 9 kinds, none of these except dwelling/garrison/barracks | proposals/2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md §A.8 |
| P8 | settlement | works plan per `works` Record (`plan`, `at`; declared terms/stages that ripen) and the stage count a plan declares | Record kind `works` keys [plan, at] (built roster); stage content PROPOSED | PROPOSED-ONLY for stage content | kind HAS, no authored works except venues `planned_works` | 04_MATTER_AND_WORKS.md §A.6 (ceiling = scale x matured/declared) |
| P9 | settlement | levy feed: `field_provisioning` on; defender's treasury choice (nearest held rung, LF-2); consumption debit (LF-3) | fixture bool; design choices | PROPOSED-ONLY (LF-1..3 held for Jordan) | fixture HAS (False) | proposals/2026-10-07-settlements-computation-modules.md §5, §8 |
| P10 | faction/settlement | troop stock: commander, type (one of 10 `TROOP_TYPE_STATS` rows), count, kit kind, home rung | stock by kind and count; amends ratified 04:801 | PROPOSED-ONLY (needs Jordan yes, M3) | NONE | 02_P1_templates.md "Troop stock (M3 option A)" |
Notes: proposals/2026-09-17-governance-and-holdings (r1) 03_THE_SURFACE.md and r2 01, 02, 05 were searched by heading only and call for no additional faction or settlement content parameters beyond rows already counted (seat schema and 29 seats in r2 03 §A.14/A.15 are already in offices.yaml; conferral/revocation sets in r2 03 §A.4/A.5 were superseded by ED-IN-0256 per offices.yaml header). r2 03 and 05 were not read in full.

## Proposals consulted (PROPOSED-ONLY, not authority)
- proposals/2026-10-28-content-architecture-suite/appendix_A3_faction_settlement.md: used only to locate carriers; all measured items above re-verified in code or YAML.
- proposals/2026-10-07-settlements-computation-modules.md (§5, §8), proposals/2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md (§A.8, §A.6 grep), 02_P1_templates.md (sections 1): read for P1-P10 above.

## Global Belongs elsewhere
- All geography/territorial hierarchy rows (listed under SETTLEMENT).
- Verbs, troops, events, goals, pursuits, cast rosters in RO (other sections of rosters.yaml: tenure_kinds, hold_*_kinds, record_kinds, witness_channels, strata, eligibility_kinds, field/combat bands, march/raze kinds, goal_*, requires_*, ladder_rungs, standing_routes, covert_kinds, endings, etc.).
- venues.yaml building rows and planned_works.
