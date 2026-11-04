# Content parameters docket: master

## Status: PROPOSED (2026-11-04). A collation of the content inputs that code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism. Merging ratifies nothing and decides nothing.
## Lane: IN

## What this is

One place that lists, for every kind of game object, the content parameters Jordan must supply, in the order he would supply them, with what the tree already holds and what it lacks. It collates; it recommends nothing and grades nothing. Each chapter's entity tables are the field lists a template for that object would need.

Authority order used throughout: (1) code that reads the field (loader, dataclass, validator, a refusal); (2) typed registries and exports code reads; (3) the active plan, `workplans/valoria_master_workplan_v10*.md`; (4) held or proposed documents under `proposals/`, listed only as `PROPOSED-ONLY` with their path. Where code and a document disagree, code wins and the chapter carries a `Conflicts:` line. Nothing under `.designs/` or `.audit/` was used as authority. Parameters whose only source is the retired Key substrate (ED-IN-0232) are marked `RETIRED-KEY` and, where one exists, the live equivalent is given.

## Chapters, in the order requested

| ch | file | covers |
|---|---|---|
| 01 | `01_characters.md` | named NPCs (name, allegiances, pursuits, goals, stance, weight, body, born, scar, tenures, bonds, arc), cohorts, pursuit vectors, goals, affiliations, attributes, capability, heritage and lifepath, kit and tradition ownership, progression, player-character creation; **complete NPC roster appendix** (46 named, 2 foreign-seat, 37 cohorts) with blanks per NPC |
| 02 | `02_factions_settlements.md` | factions (creed, holdings, leaders), affiliations, office title ladder, office seats, settlements (population, infrastructure, buildings, economy) |
| 03 | `03_geography_territory.md` | territorial ladder, territories (provinces) and temperaments, adjacency, settlement place-in-map, routes, terrain, water and passes, points of interest, foreign and off-map seats |
| 04 | `04_events_decks.md` | event decks and cards, Tensions, Goldenfurt deck, scenarios and storylines, weather draw, endings, arc case files, narration fragments, travel and survival inputs |
| 05 | `05_clocks_threadwork.md` | clocks and tracks, timers and dated items, thresholds, conditional and triggered arcs, thrust axes, conviction and truth tracks, thread sensitivity and threadwork, scale transitions, calendar |
| 06 | `06_personal_combat.md` | abilities, attributes read, skills, levers, weapons, armour, kit, traditions, formations, combatant record, wound inputs; **complete actions and choices table** |
| 07 | `07_social_fieldwork.md` | social-contest actions, attributes and skills read, venue types, arrangements and proceeding shapes, speech kinds, propositions, parliament and debate, stance and audience; investigation actions, interactions, finds, information carriers, interviews; **actions and choices tables** |
| 08 | `08_mass_battle.md` | orders and actions, armies, units, formations, subformations, troop types, troop stock, equipment, commanders, order of battle, terrain, logistics; **actions and choices table** |
| 09 | `09_verbs_params.md` | all 63 season-level verbs with choice slots, handler, preconditions and gate; write matrix; engine parameter families; season fixtures |
| 10 | `10_season_loop_choices.md` | season phases, decision questions, option sets, the NPC chooser, budget, deliberation, contest and ladder seams, the player-facing seam, every choice point |
| 11 | `11_workplan_owed.md` | every position, question or gate in the v10 plan where content is owed by Jordan or by authoring |

## How to read an entity table

`#` suggested supply order (identity first, then the layers that depend on it). `group` the layer. `domain` the type, with the closed set or bounds where code states one and the path that owns it. `req`: **REQ** a loader or validator refuses without it; **OPT**; **DERIVED** the engine computes it, so it is not authored; **PLAN** the plan calls for it and no carrier exists; **PROPOSED-ONLY** only a proposal names it; **RETIRED-KEY** only the retired substrate names it. `now`: **HAS** a value is in the tree; **STUB** a placeholder, default or `[ASSUMPTION]`; **NONE**. Entity `Status`: **AUTHORED**, **PARTIAL**, **EMPTY**, **PLACEHOLDER**. `[ASSUMPTION; medium; Jordan to correct]` is the repo's own tag for values an earlier session supplied; it means Jordan has not ruled them.

## Inventory at a glance

One row per entity type, as each chapter states its own status. Count each row's detail in its chapter.

| ch | entity type | status as stated by the chapter |
|---|---|---|
| 01 | 1. NAMED CHARACTER (NPC) | PARTIAL (identity/pursuits/affiliations/faction/role authored 46/46; every other layer thi… |
| 01 | 2. COHORT (anonymous population / guard) | PARTIAL (rows exist, every magnitude an `[ASSUMPTION]`) |
| 01 | 3. PURSUIT VECTOR | AUTHORED (roster/projection) / PARTIAL (per-person weights flagged `[ASSUMPTION]`, see sec… |
| 01 | 4. GOAL (organization-level OUGHT) | PARTIAL (FA-05/06 authored; all `[ASSUMPTION]`-marked sources) |
| 01 | 5. AFFILIATION ROSTER (religious/civic conviction poles) | AUTHORED |
| 01 | 6. ATTRIBUTE SET | PLACEHOLDER (roster only) |
| 01 | 7. CAPABILITY / SKILLS | PLACEHOLDER |
| 01 | 8. HERITAGE / LIFEPATH / HISTORY | EMPTY |
| 01 | 9. KIT / TRADITION OWNERSHIP ON A PERSON | EMPTY (in the season loop); combat module holds its own constructor args. |
| 01 | 10. PROGRESSION | PARTIAL |
| 01 | 11. PLAYER-CHARACTER CREATION INPUTS (character sheet) | EMPTY |
| 01 | 12. NAMED-NPC ARC | PLACEHOLDER |
| 02 | FACTION (roster) | PARTIAL (name and leader only; the rest is derived or absent) |
| 02 | AFFILIATION (creed-side roster) | AUTHORED (roster) / PARTIAL (engagement cells) |
| 02 | OFFICE TITLE LADDER (rung-to-title) | AUTHORED |
| 02 | OFFICE SEAT | PARTIAL (no seat below territory: zero seats at settlement, community or hearth rungs) |
| 02 | GENERIC GOVERNANCE SPINE (test fixture) | PLACEHOLDER (declared a test fixture, not canon) |
| 02 | SETTLEMENT (static row) | AUTHORED for what the engine reads; PARTIAL for the rest |
| 02 | SETTLEMENT POPULATION (cohort) | PARTIAL (weights only; no politics) |
| 02 | SETTLEMENT INFRASTRUCTURE: SITE KINDS AND BUILDINGS | AUTHORED (values flagged invented/assumption in RO notes) |
| 02 | SETTLEMENT ECONOMY (larder, produce, provision, subsistence) | AUTHORED (ration values assumption-grade) |
| 02 | PROPOSED-ONLY rows |  |
| 03 | TERRITORIAL LADDER (closed set of rung kinds) | AUTHORED |
| 03 | TERRITORY (G `provinces:`, 17 rows T1..T17) | AUTHORED (12 keys on every row) |
| 03 | TERRITORY ADJACENCY (G `adjacency:`) | AUTHORED |
| 03 | SETTLEMENT IDENTITY / PLACE-IN-MAP (G `settlements:`, S-001..S-037) | AUTHORED (7 keys on every row; `controller_subordinate` on 1) |
| 03 | SETTLEMENT ADJACENCY / ROUTES (G `settlement_adjacency:`) | AUTHORED, NO-READER |
| 03 | TERRAIN POLYGONS (G `terrain:`) and cost matrix | AUTHORED |
| 03 | WATER, BRIDGES, FORGETTING ZONE, CALAMITY BANDS, PASSES (G) | AUTHORED |
| 03 | POINT OF INTEREST (G `poi_catalog:`) | PARTIAL (counts only) |
| 03 | FOREIGN / OFF-MAP SEATS | PLACEHOLDER ([ASSUMPTION; medium; Jordan to correct], codes are the author's) |
| 04 | EVENT DECK / EVENT CARD (general) | EMPTY |
| 04 | TENSIONS CARDS | EMPTY |
| 04 | GOLDENFURT DECK (28 cards) / SETTLEMENT OPENINGS | EMPTY |
| 04 | SCENARIO / STORYLINE / SET PIECE ROWS | EMPTY |
| 04 | WEATHER / SEASON-FACTOR DRAW | PARTIAL |
| 04 | ENDINGS | PARTIAL |
| 04 | ENDINGS_CLASSIFIED (arc closure classes) | AUTHORED (agent classification of prose, labelled non-execution) |
| 04 | NAMED-NPC / ARC CASE FILES (authored-content inventory) | AUTHORED (calibration corpus, "never runtime data", part B10-19) |
| 04 | NARRATION FRAGMENTS | EMPTY |
| 05 | 1. CLOCK / TRACK | EMPTY (as a registry); the clocks exist as fixture-driven code. |
| 05 | 2. TIMER / DATED ITEM (Date, DocketItem, Term) | EMPTY (by design; runtime-minted) |
| 05 | 3. THRESHOLD (band floors, crossing triggers, gates) | PARTIAL |
| 05 | 4. CONDITIONAL / TRIGGERED ARC (arc deck, goal stages) | EMPTY (schema BUILT) |
| 05 | 5. THRUST AXES (CL-THRUST axes roster) | AUTHORED (roster) / EMPTY (tagging) |
| 05 | 6. CONVICTION / TRUTH TRACKS (ED-IN-0251) | PARTIAL |
| 05 | 7. THREAD SENSITIVITY / THREADWORK | PARTIAL (TS gate carrier) / PLAN (everything else) |
| 05 | 8. SCALE TRANSITIONS / CALENDAR-SEASON STRUCTURE / HORIZONTAL INTEGRATION / PROP | PARTIAL |
| 06 | 1. COMBAT ACTION / ABILITY (learnable technique) | PARTIAL |
| 06 | 2. ATTRIBUTE (combat READS only; person roster owned elsewhere) | PLACEHOLDER (class defaults) |
| 06 | 3. SKILL (per-axis bias dict) | EMPTY |
| 06 | 4. LEVER (named modulation channel) | PARTIAL |
| 06 | 5. EQUIPMENT — WEAPON | AUTHORED (roster) ; the season sends none (seam default `arming`). |
| 06 | 6. EQUIPMENT — ARMOUR | AUTHORED (closed set, code-owned, no per-armour-item records) |
| 06 | 7. EQUIPMENT — SHIELD / KIT (bundle) | EMPTY |
| 06 | 8. TRADITION / STYLE | PARTIAL (chinese, filipino have 0 abilities; `none` is the null tradition) |
| 06 | 9. FORMATION (PC-scale) | EMPTY |
| 06 | 10. COMBATANT RECORD (per-fight party) | PLACEHOLDER |
| 06 | 11. CONFIG / TUNING INPUTS | AUTHORED. NO authored-content roster in this file; all are tuning families. |
| 06 | 12. VOCABULARY / CLOSED TOKEN SETS (code-owned) | AUTHORED (closed; no authoring surface for Jordan except by code edit) |
| 06 | 13. ENVIRONMENT / GEOMETRY INPUTS | EMPTY |
| 06 | 14. WOUND / BODY INPUTS | PARTIAL |
| 07 | Social-contest action (verb rows that run a contest) | AUTHORED (grades: 40 `assumption`, 23 `ruled` table-wide). |
| 07 | Attribute / skill read by contests | PARTIAL |
| 07 | Social-roll tunables (fixtures the contest reads) | AUTHORED (all `assumption`/swept) |
| 07 | Venue type (buildings) | AUTHORED (AUTHORED FOR PLAY, ED-IN-0223; works rows `[ASSUMPTION]`) |
| 07 | Arrangement / proceeding shape (closed set) | PARTIAL |
| 07 | Speech kinds (issue ladder) | PARTIAL |
| 07 | Closed rosters feeding proceedings |  |
| 07 | Proposition / claim / docket item inputs | EMPTY (authored content); schema AUTHORED |
| 07 | Parliament / debate inputs | PARTIAL |
| 07 | Stance / audience inputs | PARTIAL |
| 07 | Kernel input tables (NOT WIRED; evaluated, not deleted) | AUTHORED, unreachable from the season loop (roll.py:16-37). Retirement timing is Jordan's … |
| 07 | Investigation action (module-level and verb-level) | AUTHORED |
| 07 | Interaction (scene) | AUTHORED (fixtures) |
| 07 | Find / clue / evidence type | PARTIAL |
| 07 | Information carrier (claims, Records, sources, confidence) | AUTHORED (schema) |
| 07 | Interview inputs | PLACEHOLDER (per plan retype) |
| 08 | MASS-BATTLE ACTION / ORDER | AUTHORED (verbs) / EMPTY (content) |
| 08 | ARMY (the faction's army Record) | EMPTY (by design) |
| 08 | UNIT / FORMATION / SUBFORMATION (as authored for the battle) | EMPTY |
| 08 | TROOP TYPE | PARTIAL (14 types authored; four per-type tables have unequal membership) |
| 08 | RECRUITMENT PARAMETERS (troop stock as built: the `trained` pool) | AUTHORED (all [ASSUMPTION; medium]) |
| 08 | TROOP STOCK (PROPOSED design; no carrier) | EMPTY |
| 08 | EQUIPMENT | PLACEHOLDER (every record `provisional=True`; "NOT YET WIRED into resolution" except `unit… |
| 08 | COMMANDER / HIERARCHY | EMPTY |
| 08 | ORDER OF BATTLE (strategy roster + deployment) | AUTHORED (all [ASSUMPTION; medium]) |
| 08 | TERRAIN / GEOMETRY / PERIMETER INPUTS | AUTHORED (rows) / PARTIAL (mapping) |
| 08 | CONFIG INPUTS THAT ARE AUTHORED ROSTERS (numeric families only) | AUTHORED (many tagged CALIBRATED-DEBT / class-B) |
| 08 | LOGISTICS / SUPPLY | EMPTY |
| 09 | VERB | AUTHORED |
| 09 | WRITE_MATRIX | AUTHORED  (families = kind: Person 11, Record 6, Rung 5, Tenure 5, DocketItem 3, Date 2, O… |
| 09 | ENGINE PARAMETER FAMILIES |  |
| 09 | SEASON FIXTURES |  |
| 10 | SEASON PHASE / STEP | AUTHORED (code) |
| 10 | DECISION: QUESTION | AUTHORED (code + roster) |
| 10 | DECISION: OPTION SET (opening set) | AUTHORED (code) |
| 10 | DECISION: CHOOSER (engine-side NPC choice policy) | AUTHORED (code); weights are authored-content inputs. |
| 10 | DECISION: BUDGET | AUTHORED (code) |
| 10 | DELIBERATION (DELIBERATE step) | AUTHORED (code) |
| 10 | CONTEST / LADDER SEAM | AUTHORED |
| 10 | PLAYER-FACING CHOICE SEAM | AUTHORED, but it is a dispatch hook only. |

## Entity types that appear in more than one chapter

Each is owned where it is first named; the other chapter carries the facet that its subsystem reads.

| subject | chapters |
|---|---|
| cohorts, settlement population | 01 §2 and 02 (settlement population) |
| territory temperaments | 01 §2 (`cohorts.yaml` temperaments) and 03 (territory) |
| venue types and buildings | 07 (venue type) and 02 (site kinds and buildings) |
| thrust axes and goal tagging | 01 §4 (goals) and 05 §5 |
| thread sensitivity | 01 (cast `ts`) and 05 §7 |
| conviction and truth tracks | 01 §5 (affiliations) and 05 §6 |
| attributes | 01 §6 (person roster) and 06 §2 (those combat reads) |
| foreign and off-map seats | 02 (office seat) and 03 |
| endings and arc case files | 04 and 01 §12 (named-NPC arc) |
| verbs | 09 (the table), 07 (social and fieldwork verbs), 08 (army verbs), 10 (the chooser) |
| fixtures | 09 (all), 07 (social-roll tunables), 10 (those the loop reads) |

## Limits of this docket, collected

Verification: eleven collation passes, each over a disjoint scope, with one follow-up pass for most. The orchestrator re-measured eight headline figures against the tree and all matched (63 verbs; 31 seats plus 2 foreign; 37 settlements; 17 territories; 38 goals; 14 troop types; 46 named NPCs, 35 canonical; 37 cohorts; 54 weapon records). The remaining figures are the collating agents' own, measured by loading the files where the chapter says so, otherwise by grep. No independent second reader has checked them. Line numbers marked `[from grep]` or `rel.` were not opened.

Not read in full (parameters in these may be missing from the tables):
- ch02: `proposals/2026-09-17-governance-and-holdings` r1 `03_THE_SURFACE.md`; r2 `01`, `02`, `03`, `05`.
- ch07: proceedings-subsystem `03` B.1 to B.3, B.5 to B.8, C.1.1 and the E.2 per-game rows; `04` B.4, B.5 and Parts C and D; parliament-and-debate §7 to §12; the Key-era `social_contest_consolidation_integration_v1.md` (not enumerated); the fieldwork and social-contest card homes beyond their plan card rows.
- ch11: parts 2 and 14 of the plan were swept by grep for "Jordan", "content", "authored", "ASSUMPTION", not read in full.
- ch04: `chain/NPC3.yaml` does not parse as YAML, so counts over `cases/` are by grep.
- ch08: internal engine methods in `orchestration.py` and `core/` are not itemised; the `narrow_pass` and `forest_broken` dice constants and the "no troop-stock carrier" finding rest on a single grep.
- ch06: PC-14's "about 44 reads" attribute figure is not reconciled; `wound_harm_models` internals are not verified.

Open points the chapters record, not resolved here:
- ch01: the 34 lifepaths have no member list in the tree; the tenth attribute is unnamed; non-null `ts` measures 10 of 46 where the `cast.py` docstring says 32; per-NPC stance is computed from loyalty, not stored.
- ch03: no kingdom, county, barony or march tier exists in code (the tiers are realm, duchy, territory, settlement); `stats`, `controller`, `coords` and several territory keys have no reader; CR-40's "11 of 17" is unverified.
- ch04: the tree has no loader for event cards, Tensions cards or scenarios (`tensions.yaml`, `data/tensions.py` and `scenarios.yaml` do not exist); "name, type, effect" for an event card matches no field in code.
- ch05: no authored clock, threshold or arc registry exists; `goal_stages:` is in the schema and in no goal row; no goal row carries `axis:`.
- ch07: `speech_kinds` is read by a loader and tests only; no loop file reads it.

`RETIRED-KEY` marks: ch03 (CR-40 source `params_tables.yaml:6576`; temperament drift note), ch01 (temperament alpha and beta source document; flagged in its closing re-check), ch05 (clock row 14, scale-transition rows 2 and 5). The other chapters report no row with a Key-only source.

## Related, held

`proposals/2026-10-28-content-architecture-suite/` is an earlier analysis of the same ground, held back in full and unverified. It was used only as a map; nothing in this docket depends on it.
