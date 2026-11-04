# Content parameters docket, chapter 08: Mass battle and armies

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Measured against the tree (Python import + YAML load), 2026-11-04. Paths relative to /home/user/ttrpg.
Standing fact for every entity below: **the season ships no authored army, unit, subformation or order of battle.** `army` Records are minted at runtime by verbs (`create_record kind: army`); `engine/season/cohorts.yaml` seats 37 cohorts (`cohorts` key, measured) that are the population troops are drawn from. Every mass-battle roster below lives in Python dicts inside `modules/mass_battle/` (single Python owner), not in YAML/JSON under `engine/engine_params/`. Most carry `[ASSUMPTION; medium; Jordan to correct]` or `provisional=True` tags in the source.

---

## MASS-BATTLE ACTION / ORDER  — carrier/loader: engine/season/rosters.yaml:2294 (`army_verbs`), modules/mass_battle/armyrecord.py:35 (`OPS`), loop/effects_army.py:69-121, modules/mass_battle/hierarchy/units.py:312 (`Order`)
Population now: 6 army verbs (`recruit, form_unit, assign_troops, order_unit, disband_unit, discharge_troops`, measured from the roster); 0 authored orders of battle. Order triggers and behaviour fields are code-closed.   Status: AUTHORED (verbs) / EMPTY (content)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | verb roster | army verb set | closed list of 6 verbs, each must be a verb_table.yaml verb | REQ | HAS | engine/season/rosters.yaml:2303 |
| 2 | payload | recruit: cohort, troop_type, count | cohort = Person id (weight>1); troop_type in TROOP_TYPE_STATS; count positive int | REQ | n/a (runtime) | loop/effects_army.py:81; armyrecord.py:57 |
| 3 | payload | form_unit: name, troop_type, role | name non-empty str unique per army; role in `roles_for(type)` or None | REQ | n/a | effects_army.py:94; armyrecord.py:135 |
| 4 | payload | assign_troops: name, cohort, count | positive int, bounded by trained pool | REQ | n/a | effects_army.py:101 |
| 5 | payload | order_unit: name, role, stance, target, fall_back_at, strategy | see Subformation rows | OPT | n/a | effects_army.py:118-121 |
| 6 | payload | disband_unit: name; discharge_troops: cohort, troop_type, count | | REQ | n/a | effects_army.py:105,111 |
| 7 | Order (in battle) | trigger kind | `'immediate' \| 'tick:N' \| 'enemy_range:D' \| 'ally_at:D' \| 'own_strength:FRAC' \| 'signal:NAME'` | OPT | HAS (code-closed) | hierarchy/units.py:312-318 |
| 8 | Order (in battle) | behavior dict | attr->value restricted to `_ORDER_SAFE_FIELDS`; may set `feign_retreat` | OPT | HAS | units.py:319-330 |

Owed: none authored; verbs are complete. Order trigger set is not an authored roster.
Conflicts: none.
Belongs elsewhere: `march` verb / `arrival_only_kinds` ['territory'] / `march_target_kinds` ['settlement','territory'] (rosters.yaml, territory/rung scope).

---

## ARMY (the faction's army Record)  — carrier/loader: modules/mass_battle/armyrecord.py:40 (`KEYS`); engine/season/rosters.yaml:246 (`record_kinds.army`)
Population now: 0 authored (runtime-minted).   Status: EMPTY (by design)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | faction | faction Proposition id | REQ | NONE | armyrecord.py:42-47 |
| 2 | identity | commander (the Record's holder) | a Person; "an army is where its commander is" | REQ | NONE | seam/wrappers/mass_battle.py:178-193 |
| 3 | doctrine | strategy | enum {line, advance, defend} (modules/mass_battle/orderofbattle.py:53); default 'line' | REQ | HAS (default) | armyrecord.py:43-47 |
| 4 | composition | trained | ((cohort id, troop type, count), ...) unassigned pool | REQ | NONE | armyrecord.py:40 |
| 5 | composition | subformations | list of Subformation dicts (see UNIT/SUBFORMATION); at most 11 | REQ | NONE | armies.py:41 (`SUBUNIT_CAP=11`) |
| 6 | derived | strength fielded | scaled by fit fraction of each cohort present | DERIVED | n/a | armyrecord.py `to_order_of_battle` / `fielded`; queries/inputs.py:446 |

Owed: the record has no fields beyond the four keys; any extra (name, banner, upkeep, home rung) has no carrier. Troop-stock design (PROPOSED-ONLY, below) would add commander/count/kit/home rung to a Rung store.
Conflicts: proposals/2026-10-29-army-phase5-design.md M2 says troops fight when the commander is present at the place; massbattle.py `_oob_unit` doc and field_input follow that. No code/doc conflict found.
Belongs elsewhere: commander's attributes (Person, characters scope).

---

## UNIT / FORMATION / SUBFORMATION (as authored for the battle)  — carrier/loader: modules/mass_battle/orderofbattle.py:78 (`Subformation`), :97 (`OrderOfBattle`), :115 (`validate`); hierarchy/units.py:392 (`Subunit`), :2779 (`Unit`)
Population now: 0 authored. Dataclass `Subformation` has 7 fields; `Subunit` ~35 fields (most engine-internal); `Unit` ~25 fields.   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | Subformation.name | str, unique within the order of battle | REQ | NONE | orderofbattle.py:123-127 |
| 2 | identity | Subformation.troop_type | key of TROOP_TYPE_STATS (14 members, see TROOP TYPE) | REQ | NONE | orderofbattle.py:128 |
| 3 | size | Subformation.troops | float > 0 headcount | REQ | NONE | orderofbattle.py:130 |
| 4 | role | Subformation.role | key of ROLE_SPEC within `roles_for(troop_type)`; None = plain Line | OPT | NONE | orderofbattle.py:132 |
| 5 | stance | Subformation.stance | enum {balanced, aggressive, hold} (STANCES, orderofbattle.py:44); None takes strategy's | OPT | NONE | orderofbattle.py:134 |
| 6 | targeting | Subformation.target | enum {None, nearest, weakest} (TARGETINGS, orderofbattle.py:47) | OPT | NONE | orderofbattle.py:136 |
| 7 | withdrawal | Subformation.fall_back_at | float strictly in (0,1): fraction of own starting strength | OPT | NONE | orderofbattle.py:138 |
| 8 | cap | subformations per army | <= 11 (`SUBUNIT_CAP`) | REQ | HAS 11 | armies.py:41; orderofbattle.py:121 |
| 9 | floors | routing floors | subunit < `SUBUNIT_ROUT_FLOOR` 80 routs; unit < `BLOCK_SIZE` 100 routs; `MAX_TROOPS_PER_UNIT` 10000 | DERIVED | HAS | config.py:117,118,156 |
| 10 | Unit baseline | Unit power / command / discipline / morale | 4 / 4 / 5 / season-derived 1-7 (floor 1, ceil 7, base 5) | DERIVED | STUB (`_UNIT_POWER`, `_UNIT_COMMAND`, `_UNIT_DISCIPLINE`; `_MORALE_START_BASE`) | orderofbattle.py:75; massbattle.py:95-103,172-198 |
| 11 | Unit | speed tier | enum {Slow, Standard, Fast} (terrain.py:290) | OPT | STUB (default 'Standard'; per-type tier is an ASSUMPTION in units.py comment) | units.py (Unit.speed) |
| 12 | Subunit | per-subunit power/discipline/morale/morale_start overrides, dr, stamina, shape, width, depth, distribution (`uniform\|front\|rear`) | ints / enum | OPT | NONE (engine-internal; type presets fill power/discipline/morale) | units.py:392-470 |

Owed: nothing in the tree authors any subformation. Per-subunit `dr` (armour) and `stamina` (endurance) are deliberately unbridged from the troop table (registry.py:32-43 comment; 08_mass_battle_units.md U-6).
Conflicts: orderofbattle.py:75 duplicates baseline literals from massbattle.py (cycle avoidance; a test pins them equal) — two copies of one fact.
Belongs elsewhere: none.

---

## TROOP TYPE  — carrier/loader: modules/mass_battle/troop_types/registry.py:44 (`TROOP_TYPE_STATS`); config.py:582 (`TROOP_TYPE_ROLES`); registry.py:108 (`TROOP_TYPE_REACH`); config.py:126 (`TROOP_TYPE_DENSITY_CAP`); registry.py:75 (`MOUNTED_TYPES`); troop_types/recruitment.py:55 (`TRAINING_SITE`); equipment/__init__.py:21 (`TROOP_LOADOUT`)
Population now: 14 types in TROOP_TYPE_STATS: levy, light_infantry, heavy_infantry, cavalry, archers, crossbow, sling, artillery, knights_templar, pike, spearmen, skirmishers, mounted_archers, light_cavalry. Plus 'infantry' (bare default, in TROOP_TYPE_REACH and TROOP_TYPE_ROLES only) and 'any' (role fallback). 4 canonical-to-§B.2 stat rows (light_infantry, heavy_infantry, knights_templar + original table); pike, spearmen, skirmishers, mounted_archers, light_cavalry are tagged provisional-by-analogy (mirror the nearest type).   Status: PARTIAL (14 types authored; four per-type tables have unequal membership)

Per-table coverage (measured): stats 14; roles menu 11 keys (missing: artillery, sling, crossbow, levy, knights_templar — they fall to the 'any' menu [Support, Reserve]); reach 15 (14 + 'infantry'); loadout 14; training site 13 (levy absent by design: needs no Site); density cap 4 (cavalry, knights_templar, mounted_archers, light_cavalry; others use CELL_CAP 200); mounted set 3 (cavalry, mounted_archers, light_cavalry — knights_templar deliberately not in it, registry.py:72-74); preset `ROLE_OF` 12 (missing: mounted_archers, artillery, which the preset plan never raises).

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | troop type id | string key; closed set = TROOP_TYPE_STATS keys; lookups lower-cased | REQ | HAS 14 | registry.py:44,78; armyrecord.py:50 |
| 2 | stats | power | int (existing values 1-5) | REQ | HAS 14 | registry.py:44-71 |
| 3 | stats | discipline | int (existing 1-6; MIN_DISCIPLINE per shape 1/4/5/3) | REQ | HAS 14 | registry.py:44-71 |
| 4 | stats | morale | int (existing 2-6; season ladder 1-7) | REQ | HAS 14 (but the side's season morale overrides it in `build_unit`) | registry.py:44-71; orderofbattle.py:233 |
| 5 | reach | front-face reach (lattice units) | float; existing {0.1, 0.2, 0.3}; default `REACH_MELEE_DEFAULT` 0.1 | OPT | HAS 15 | registry.py:108 |
| 6 | roles | gated role menu | list of ROLE_SPEC keys; fallback 'any' | OPT | HAS 11 of 14 | config.py:582 |
| 7 | mount | mounted? | membership in `MOUNTED_TYPES` (frozenset) | OPT | HAS 3 | registry.py:75 |
| 8 | density | max troops per cell | int; mounted 100, default `CELL_CAP` 200, floor `CELL_FLOOR` 40 | OPT | HAS 4 (value is "needs_jordan" calibration per config.py:126 comment) | config.py:40,41,126 |
| 9 | equipment link | loadout (weapon id, armour id) | ids of ARSENAL and ARMOURY | OPT | HAS 14 | equipment/__init__.py:21 |
| 10 | recruitment | training Site kind + minimum condition fraction | kind in rosters.yaml `site_kinds` {barracks, archery_range, stable, siege_workshop}; fraction 0.0 or 0.5 | OPT | HAS 13 | troop_types/recruitment.py:55 |
| 11 | preset | preset role (AI factions) | role in type's menu or None | OPT | HAS 12 | troop_types/presets.py:45 |
| 12 | derived | ranged/melee `unit_type` | derived from loadout weapon `reach` | DERIVED | n/a | registry.py:172 |
| 13 | derived | support ranks | reach / 0.1, min 1 | DERIVED | n/a | registry.py:147 |
| 14 | unbridged | dr (armour), stamina (endurance) per type | not mapped from §B.2 | PLAN | NONE | registry.py:32-43; proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md U-6 |
| 15 | unbridged | per-type speed tier | Slow/Standard/Fast | PLAN | NONE | hierarchy/units.py (Unit.speed comment) |

Owed: roles for artillery, sling, crossbow, levy, knights_templar (currently the 'any' menu); `ROLE_OF` preset for mounted_archers and artillery; stats for any type beyond the 14; item 14/15 above. Workplan: "Equipment, tradition and troop types have no carrier in the season loop" (workplans/valoria_master_workplan_v10.md:132); CL-TROOP held on M22 (workplans/valoria_master_workplan_v10_part12.md:20, part15.md:60-62).
Conflicts: registry.py:75-74 comment excludes knights_templar from MOUNTED_TYPES though it has a lance reach and density cap 100; stat comments cite `mass_battle_v30.md §B.2` (a quarantined doc) as source.
Belongs elsewhere: Site kinds barracks/archery_range/stable/siege_workshop (settlements scope; rosters.yaml:1506, `wear_per_season` 0, `works_cost` {timber: 10} each, `band_floors` {}).

---

## RECRUITMENT PARAMETERS (troop stock as built: the `trained` pool)  — carrier/loader: modules/mass_battle/troop_types/recruitment.py:35
Population now: 2 scalars + 13-row table above.   Status: AUTHORED (all [ASSUMPTION; medium])

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | scale | `TROOPS_PER_WEIGHT` | int; people per Person.weight | REQ | HAS 300 | recruitment.py:44 |
| 2 | scale | `MUSTER_FRACTION` | float 0-1; share under arms | REQ | HAS 0.10 | recruitment.py:49 |
| 3 | table | `TRAINING_SITE` type -> (site kind, min condition) | see TROOP TYPE row 10 | REQ | HAS 13 | recruitment.py:55 |
| 4 | doctrine | `ARM_SHARES` class -> (share of cap, type preference order) | 3 classes: melee 0.45 (heavy_infantry, spearmen, pike, light_infantry), missile 0.25 (crossbow, archers, sling, skirmishers), mounted 0.20 (cavalry, knights_templar, light_cavalry); levy takes remainder | OPT | HAS 3 | troop_types/presets.py:37 |
| 5 | doctrine | `ROLE_OF` | see TROOP TYPE row 11 | OPT | HAS 12 | presets.py:45 |

Owed: nothing absent. Doc names TROOPS_PER_WEIGHT 100->300 revision (army-phase5 M1).
Conflicts: none.
Belongs elsewhere: cohort weights (cohorts.yaml, 37 rows; settlements/people scope).

---

## TROOP STOCK (PROPOSED design; no carrier)  — carrier: none in code. Proposed: proposals/2026-10-16-troop-stock-design.md, _part2.md §6 (L324-349)
Population now: none. Not built; `Rung.stores` holds no troop kind; `matter_kinds` has no `recruits` or `troops_<grade>` row in the code path measured (not exhaustively verified: grep of `pool_rung|troop_grades|men_per_weight|recruit_share` over engine/season .py/.yaml listed no file).   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | pool | `recruits` matter kind row | whole weight units in a settlement rung's stores | PROPOSED-ONLY | NONE | proposals/2026-10-16-troop-stock-design_part2.md:329 |
| 2 | pool | `pool_rung_kinds`, `immovable_kinds` rosters | closed lists | PROPOSED-ONLY | NONE | _part2.md:330-331 |
| 3 | pool | `recruit_share` (per-mille), `recruit_regrowth` (per-mille/season) | ints; sweeps 500/1000/2000 and 0/250/1000 | PROPOSED-ONLY | NONE | _part2.md:332-333 |
| 4 | pool | `men_per_weight`, `garrison_men` | ints; sweeps 1/120/250 and 0/120/250 | PROPOSED-ONLY | NONE | _part2.md:334-335 |
| 5 | grade | `troop_grades` rows `{id, discipline:+d, morale:+m}` | ordered; proposal raw 0/0, drilled +1/+1, seasoned +1/+2, veteran +2/+2 | PROPOSED-ONLY | NONE | _part2.md:337 |
| 6 | grade | `troops_<id>` matter kinds | one per grade, loader-derived | PROPOSED-ONLY | NONE | _part2.md:338 |
| 7 | kit | `kind_for_kit`, `UNARMED_KIND`; equipment matter kinds per weapon/armour class | one per class or a coarser three: OPEN | PROPOSED-ONLY | NONE | _part2.md:341-342 |
| 8 | feed | `field_army` fixture `single_line \| order_of_battle` | temporary arm | PROPOSED-ONLY | NONE | _part2.md:344 |
| 9 | stored | army = commander, type, count, kit kind, home rung | M22 yes arm | PLAN | NONE | workplans/valoria_master_workplan_v10_part15.md:60,160-166 (CL-TROOP, M22 ESCALATE; M25 kit DESIGN-FIRST) |

Owed: Jordan's M22 answer gates all rows (part15.md:62: "Default in force: the field stays persons at weight").
Conflicts: the built army Record (armyrecord.py: trained/subformations as cohort headcounts) is a different body from the stock design's Rung store; the design predates ED-IN-0306.
Belongs elsewhere: recruit pool in settlement rungs (settlements scope); `subsistence_weight` grain 2 / salt 1 for troop eating (rosters.yaml, economy scope).

---

## EQUIPMENT  — carrier/loader: modules/mass_battle/equipment/weapons.py:29 (`ARSENAL`), armour.py:29 (`ARMOURY`), _base.py:15,47 (open `EquipmentRecord` / `Registry`)
Population now: 10 weapons (light_cut, heavy_cut, heavy_blunt, pike, spear, javelin, bow, crossbow, sling, siege); 4 armours (none, light, medium, heavy); 14-row troop->(weapon, armour) loadout.   Status: PLACEHOLDER (every record `provisional=True`; "NOT YET WIRED into resolution" except `unit_type_for`, which reads weapon `reach`)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | weapon identity | weapon name | string | REQ | HAS 10 | weapons.py:38-47 |
| 2 | weapon | damage_type | enum {cut, blunt, pierce} (weapons.py:25) | OPT | HAS 10 | weapons.py:25 |
| 3 | weapon | weight | enum {light, heavy} (weapons.py:26) | OPT | HAS 10 | weapons.py:26 |
| 4 | weapon | reach | enum {melee, ranged} (weapons.py:27); read by `unit_type_for` | REQ (live reader) | HAS 10 | weapons.py:27; registry.py:172 |
| 5 | weapon | keywords | tuple from {anti_armour, anti_cavalry, armour_piercing, pole, volley} (observed, open) | OPT | HAS 10 | weapons.py:38-47 |
| 6 | armour identity | armour name / tier | enum {none, light, medium, heavy} (armour.py:27) | REQ | HAS 4 | armour.py:27 |
| 7 | armour | material | {none, cloth, mail, plate} provisional | OPT | HAS 4 (STUB) | armour.py:37-40 |
| 8 | armour | dr_vs_piercing | 0/1/2/3 | OPT | HAS 4 (canonical per tag) | armour.py:37-40 |
| 9 | loadout | troop type -> (weapon, armour) | ids in the two registries | OPT | HAS 14 | equipment/__init__.py:21 |
| 10 | grounding | physical axes (mass_kg, reach_m, percussion, coverage, per-damage-type DR) | open fields | PLAN | NONE | armour.py/weapons.py docstrings; 08_mass_battle_units.md U-2 (PROPOSED-ONLY) |
| 11 | kit carrier | who owns a weapon (item class) | no Layer-1 carrier | PLAN | NONE | workplans/valoria_master_workplan_v10_part15.md:73-74 (M25 DESIGN-FIRST) |

Owed: items 10-11. Wiring of weapons/armour into resolution (08 U-2) — PROPOSED-ONLY.
Conflicts: weapons.py/armour.py docstrings cite `designs/scene/combat_engine_v1/...` (dissolved path); armour tiers' `material` placeholder vs personal combat tier->material not yet bridged.
Belongs elsewhere: personal-combat weapon/armour records (combat scope).

---

## COMMANDER / HIERARCHY  — carrier/loader: modules/mass_battle/hierarchy/units.py:2750 (`Officer`), :2779 (`Unit`); config.py:530-533,576
Population now: 0 authored. No Person supplies command; the season Unit uses baseline command 4.   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | Officer.name | str | REQ | NONE | units.py:2751 |
| 2 | stat | Officer/Unit.command | int clamped 1-7 (`clamp_command`); default 4 | OPT | STUB (4) | units.py:2751-2776; orderofbattle.py:75 |
| 3 | stat | charisma, cognition (both set => command = derive_command) | int | OPT | NONE | units.py:2757-2758; config.py:532-533 (`CMD_CHA_WEIGHT` 2, `CMD_COG_WEIGHT` 1) |
| 4 | span | officers per general | counted vs `SUBUNIT_CAP` 11 via `build_army(officers=)` | OPT | NONE | armies.py:119 |
| 5 | pool | `COMMAND_POOL_MULT` | float, default 2 | OPT | HAS 2 | config.py:531 |
| 6 | link | seated commander (Person) -> Unit.command/charisma/cognition | no feed | PLAN | NONE | 08_mass_battle_units.md U-4 (PROPOSED-ONLY); workplans part15.md CL-TROOP "commander" |

Owed: item 6; per-echelon officers.
Conflicts: none.
Belongs elsewhere: Person attributes charisma/cognition (characters scope).

---

## ORDER OF BATTLE (strategy roster + deployment)  — carrier/loader: modules/mass_battle/orderofbattle.py:53 (`STRATEGIES`), :44 (`STANCES`), :47 (`TARGETINGS`), :66-70 (deployment constants)
Population now: 3 strategies (line, advance, defend); 3 stances; 2 targeting values + None; unit classes melee/ranged/mounted derived.   Status: AUTHORED (all [ASSUMPTION; medium])

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | strategy | id -> stance per class | {line:{melee,ranged,mounted: balanced}, advance:{aggressive, balanced, aggressive}, defend:{hold, balanced, hold}} | REQ | HAS 3 | orderofbattle.py:53-57 |
| 2 | deployment | A front row, approach rows, anchor col, margins | 27, 3, 25, cols 1..49 | OPT | STUB | orderofbattle.py:66-70 |
| 3 | deployment | layout rule (melee front, ranged behind, mounted flanks alternating) | code | OPT | STUB | orderofbattle.py:15-19 |
| 4 | geometry | `DEPLOY_GAP` 1, `ENVELOP_WING_GAP` 3, `REFUSE_ECHELON` 6 | ints | OPT | HAS | armies.py:52-54 |
| 5 | planned | envelopment presets (multi-unit) | not built | PROPOSED-ONLY | NONE | proposals/multiunit_envelopment_plan.md (Status: un-adopted, held); orderofbattle.py:21-23 |

Owed: none required.
Conflicts: none.
Belongs elsewhere: none.

---

## TERRAIN / GEOMETRY / PERIMETER INPUTS  — carrier/loader: modules/mass_battle/terrain.py:66,272-290; massbattle.py:347 (`resolve_field`); engine/season/queries/inputs.py:130 (`MassBattleInput`); perimeter.py:25
Population now: 6 terrain rows (narrow_pass, uphill, forest_broken, walls, river_crossing, open_flat); 8 geography-type -> row mappings; geography read from systems/settlements/valoria_geography_v30.yaml (`provinces`, `terrain`, `water`).   Status: AUTHORED (rows) / PARTIAL (mapping)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | rows | terrain row set | closed 6 | REQ | HAS | terrain.py:45-50 |
| 2 | mapping | geography `type:` -> row | {mountain_pass:narrow_pass, mountain:uphill, highland:uphill, forest:forest_broken, marsh:forest_broken, coast:open_flat, fjord_coast:forest_broken, plains:open_flat}; unmapped type absent | REQ | HAS 8 | terrain.py:66-75 |
| 3 | modifiers | WALLS_DEFENDER_DR 3; UPHILL_ATTACKER_OFF_D -1; UPHILL_DEFENDER_DEF_D 1; RIVER_CROSSING_OFF_D -1; narrow_pass / forest_broken dice | ints | REQ | HAS (narrow_pass and forest_broken constants not listed in my grep: unverified) | terrain.py:272-289 |
| 4 | input | territory id, fort_level [0,1], origin territory | geography ids; fort_level from garrison Site condition | REQ | runtime | queries/inputs.py:130-152 |
| 5 | input | walls_dr fixture (`field_walls_dr`, H-150) | int or None | OPT | runtime | inputs.py:143 |
| 6 | input | stances, loyalties, loyalty_gain (`field_morale_loyalty_gain`, H-148) | floats; gain 0 = control | OPT | runtime | inputs.py:148-152 |
| 7 | geography | per-province `anchor`, terrain polygons, water rivers (polyline), `bridges` (not read) | geography YAML | REQ | HAS | terrain.py docstring |
| 8 | perimeter | `SHARP_TIP_DEG` | 60.0 | OPT | HAS | perimeter.py:25 |
| 9 | battlefield | BATTLEFIELD_SIZE 51, UNIT_GRID_SIZE 30, BUFFER_CELLS 10, start rows 34/15, ticks/phase 6, route budget 18 ticks | ints | OPT | HAS | config.py:16-28,155,429 |

Owed: none authored beyond geography; known gap: provinces whose anchor sits outside their dominant polygon (T3, T10 pass case) cannot resolve to NARROW_PASS (terrain.py docstring).
Conflicts: terrain.py docstring cites `designs/territory/...` path as stale; `fort_level` in geography YAML is ignored (live Site condition wins).
Belongs elsewhere: geography polygons/anchors, province `fort_level` (settlements/geography scope); garrison Site (settlements).

---

## CONFIG INPUTS THAT ARE AUTHORED ROSTERS (numeric families only)  — carrier/loader: modules/mass_battle/config.py
Population now: 4 closed dicts + 4 numeric families; others are tunables (env-overridable) and not listed individually.   Status: AUTHORED (many tagged CALIBRATED-DEBT / class-B)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | `TROOP_TYPE_ROLES` | 11 keys -> role lists | REQ | HAS 11 | config.py:582 |
| 2 | roster | `ROLE_SPEC` | 15 roles: ShieldWall, Hold, Anvil, Push, Skirmish, Screen, Pursue, Shock, Flanker, Feint, VolleyLine, Harass, Kite, Support, Reserve; each (shape, instructions) | REQ | HAS 15 | config.py:603 |
| 3 | roster | shapes + `MIN_DISCIPLINE` | {Line:1, Arrowhead:4, GappedLine:5, Column:3} | REQ | HAS 4 | config.py:201 |
| 4 | roster | `ANGLE_DEF_MOD` / `OCTAGON_DMG_MULT` | {GREEN:0, YELLOW:-1, RED:-2}; {1.0, 1.5, 2.0} | REQ | HAS | config.py:208,219 |
| 5 | roster | `STANCE_SPEED_MOD`, `STANCE_COMMITMENT` | stances {aggressive, balanced, hold, retreat} | REQ | HAS 4 | config.py:279,290 |
| 6 | family | size: `TROOPS_PER_TIER` {1:100,2:200,3:400,4:800}, `TROOPS_PER_SIZE` 100, `BLOCK_SIZE` 100 | ints | OPT | HAS | config.py:33,34,156 |
| 7 | family | support: `SUPPORT_WEIGHTS` {1:1.0,2:0.7,3:0.5}, floor 0.3 | floats | OPT | HAS | config.py:139,140 |
| 8 | family | volley: range 2-8, `RANGED_DR_DEFAULT` 2, `MB_VOLLEYS_START` 10, `MB_VOLLEYS_RESUPPLY` 3 | numbers | OPT | HAS | config.py:191-193,507,508 |
| 9 | family | rout: onset 0.15, cap 0.30, `SUBUNIT_ROUT_FLOOR` 80, cascade 0.6 | floats | OPT | HAS | config.py:116,117,186,187 |

Owed: none. Item 7/8/9 values carry CALIBRATED-DEBT / class-B tags in source; ~110 further tunables exist in config.py (lines 15-576) and are not itemised.
Conflicts: config.py:568-style "SCAFFOLD — INERT" claim in 08_mass_battle_units.md §1.2 vs ROLE_INSTRUCTION_PRIMITIVES wiring (units.py, MB-04): doc stale; code wins.
Belongs elsewhere: none.

---

## LOGISTICS / SUPPLY  — carrier: none in modules/mass_battle (no supply, forage, ammo-resupply-by-supply, or march-rate parameter beyond below)
Population now: none for armies. `MB_AMMO_ENABLED` and `MB_VOLLEYS_*` are in-battle only. Army ration: billed on the weight of the cohorts the army drew from (army-phase5 M8); `subsistence_weight` grain 2, salt 1 (rosters.yaml, per troop-stock part2 §6).   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | provisioning | `field_provisioning` fixture flag | bool | OPT | runtime fixture | proposals/2026-10-29-army-phase5-design.md §2 (flag exists; not re-verified in code here) |
| 2 | upkeep | troop upkeep / treasury bound | LF-1 ruled-revertible | PLAN | NONE | workplans/valoria_master_workplan_v10_part12.md:328 (DEF-7); IN-52 |
| 3 | weight->troops | REM-32 weight->troop multiplier fixture | one fixture | PLAN | NONE | workplans/valoria_master_workplan_v10_part13.md:326-329 |

Owed: items 2-3.
Conflicts: none.
Belongs elsewhere: treasury, grain/salt rations, provisioning (economy scope).

---

## PROPOSED-ONLY MASS-BATTLE PARAMETERS NOT ABOVE
- proposals/mass_battle_fighting_withdrawal_v1.md — Status: BUILT (gated); its parameters are in config (`YIELD_RALLY_MORALE_FRAC` 0.75, `YIELD_POCKET_REACH` 3.0, `MB_YIELD_*` flags, config.py:266-277). No authored content.
- proposals/multiunit_envelopment_plan.md — un-adopted, held; no content parameters.
- proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md — recommendations U-1 to U-6 (inputs beyond headcount, equipment merge, role wiring, officers as Persons, mounted_archers preset [now has one], armour/endurance bridge). PROPOSED-ONLY.

## Conflicts (collected)
1. 08_mass_battle_units.md §1.1 says ten types and mounted_archers has no preset; code has 14 and a mounted_archers preset (registry.py:69). Code wins.
2. 08 §1.2 says roles are INERT; config.py:601 comment says wiring is `hierarchy.units.ROLE_INSTRUCTION_PRIMITIVES` since MB-04.
3. Troop-stock design (PROPOSED) vs built army Record (ED-IN-0306): different bodies for troops.

---

## ACTIONS / CHOICES TABLE — the mass-battle module's own (season verbs excluded)
Who chooses: HOST = season code calling a composition row; PLAYER/COMMANDER = a choice carried in the army Record or an in-battle Order; ENGINE = fixed by code, no one selects. All paths relative to /home/user/ttrpg. Counts measured by listing below: 8 module entries/composition rows, 7 record operations, 3 strategies, 3 stances (+retreat via order), 3 targeting values (+2 order-only forms), 6 order triggers, 15 roles, 4 shapes, 18 instruction keywords, 17 order-settable fields.

### A. Module entries (composition rows, references/module_contracts.yaml)
| # | name | who | inputs | preconditions | outputs | cite |
|---|---|---|---|---|---|---|
| A1 | `mass_battle.resolve_field` (`resolve_field`) | HOST (`march`, `entry: verb_call`) | `MassBattleInput`: weights, territory, fort_level, stances, walls_dr, origin, loyalties, loyalty_gain, geography, orders_of_battle; kwargs rng, troops_a, troops_b | a field is joined (adapter ran PARTY-GAP checks and Unopposed branch) | `_run_and_grade` result (graded outcome) | references/module_contracts.yaml:64-68; modules/mass_battle/massbattle.py:347; engine/season/queries/inputs.py:130 |
| A2 | `mass_battle.army` (`armyrecord.apply`) | HOST (army verbs, query row) | `ArmyCommand{record, op, args}` | op in `OPS` | new `subject_matter` dict; ValueError = refusal | module_contracts.yaml:99-102; armyrecord.py:279; inputs.py:433 |
| A3 | `mass_battle.army_order` (`armyrecord.fielded`) | HOST (field input builder) | `ArmyMuster{record, fit}` | army Record exists; side's cohorts present | `OrderOfBattle` or None | module_contracts.yaml:103-106; armyrecord.py:379; inputs.py:446 |
| A4 | `mass_battle.army_options` (`armyrecord.options`) | HOST (military menu, read-only) | `ArmyOptionsQuery{record, cohorts, full, others}` | record valid | dict: strategies, stances, targets, troop_types, raise, advisories | module_contracts.yaml:107-110; armyrecord.py:335; inputs.py:458 |
| A5 | `mass_battle.army_preset` (`presets.plan`) | HOST (AI factions; shipped off) | `ArmyPresetQuery{faction, cohorts, full, others}` | none | tuple of (verb, payload): recruit, form_unit, assign_troops | module_contracts.yaml:111-114; troop_types/presets.py:53; inputs.py:473 |
| A6 | provisioning row (levy-to-field feed) | HOST | `ProvisionInput` (weight, treasury stores, ration, `field_provisioning` fixture) | fixture True to act | `troops`, `consumed` | module_contracts.yaml:98 (row name not re-read; target not listed in my grep) |
| A7 | `fortification` query | HOST | `FortInput` (garrison conditions, scale) | none | fort level [0,1] | module_contracts.yaml:116-118 (target `modules.settlements.fortification`; settlements scope) |

### B. Army-record operations (armyrecord `OPS`, armyrecord.py:276)
| # | name | who | arguments | preconditions / refusals | output | cite |
|---|---|---|---|---|---|---|
| B1 | `new` | HOST | faction, strategy (default 'line') | strategy in STRATEGIES | empty record | armyrecord.py:43 |
| B2 | `recruit` / `raised` | PLAYER via verb | cohort, troop_type, count | known type; positive int; within `recruit_limit` (population cap, Site condition, claims across all armies) | record + trained row | armyrecord.py:109; recruitment.py:83 |
| B3 | `form` | PLAYER | name, troop_type, role | non-empty unique name; role in `roles_for(type)`; < 12th subformation (`SUBUNIT_CAP` 11) | record + empty subformation | armyrecord.py:135 |
| B4 | `assign` | PLAYER | name, cohort, count | subformation exists; trained troops of that cohort and type available | trained -> assigned | armyrecord.py:153 |
| B5 | `release` | PLAYER (internal to disband) | name, cohort, count | held amount | assigned -> trained | armyrecord.py:167 |
| B6 | `order` | PLAYER | name; role, stance, target, fall_back_at (each optional, unset-sentinel `_UNSET`) | role in type menu; stance in STANCES; target in TARGETINGS; fall_back_at in (0,1) | record with fields set | armyrecord.py:203 |
| B7 | `set_strategy` | PLAYER | strategy | in STRATEGIES | record | armyrecord.py:228 |
| B8 | `disband` | PLAYER | name | subformation exists | troops return to trained | armyrecord.py:177 |
| B9 | `discharge` | PLAYER | cohort, troop_type, count | trained troops held | troops return home | armyrecord.py:189 |
| B10 | `validate` | HOST/ENGINE | record | arithmetic of record | ValueError or ok | armyrecord.py:235 |
| B11 | `to_order_of_battle` | ENGINE | record, fitness callable | record valid | `OrderOfBattle` scaled by cohort fitness | armyrecord.py:256 |
| B12 | `cohort_claims`, `by_type`, `unassigned`, `fielded` | ENGINE | record(s), cohort | none | tallies | armyrecord.py:84,98,116,379 |

### C. Choices carried on an Order of Battle (orderofbattle.py)
| # | name | who | domain | precondition | output | cite |
|---|---|---|---|---|---|---|
| C1 | strategy | PLAYER | {line, advance, defend} | at least one subformation | stance per class (melee/ranged/mounted) | orderofbattle.py:53,118 |
| C2 | subformation stance | PLAYER | {balanced, aggressive, hold} (retreat only via fall_back_at) | role stance wins over strategy if subformation stance unset | spec stance | orderofbattle.py:44,154-160 |
| C3 | subformation targeting | PLAYER | {None, nearest, weakest} | none | `target_condition` | orderofbattle.py:47,165 |
| C4 | fall-back point | PLAYER | float in (0,1) | none | Order `own_strength:F` -> stance retreat | orderofbattle.py:167-168 |
| C5 | role | PLAYER | key of ROLE_SPEC in type menu; None = plain Line; mounted_archers with no role = Kite | role in menu | shape + instruction package | orderofbattle.py:150-164; config.py:582,603 |
| C6 | `build_unit`, `validate`, `class_of` | ENGINE | oob, name, side 'A'/'B', morale_start | validate passes | multi-subunit Unit | orderofbattle.py:229,115,107 |
| C7 | deployment placement | ENGINE | melee front, ranged behind, mounted on alternating flanks | fits field else one centred line | starting_position | orderofbattle.py:180 |

### D. In-battle commander Orders (hierarchy/units.py `Order`, core/contact.py `check_orders`)
| # | name | who | arguments | precondition | output | cite |
|---|---|---|---|---|---|---|
| D1 | trigger `immediate` | COMMANDER | none | none | fires at once | units.py:305 (`_ORDER_TRIGGER_KINDS`) |
| D2 | trigger `tick:N` | COMMANDER | N ticks | none | fires at tick N | units.py:305 |
| D3 | trigger `enemy_range:D` | COMMANDER | distance D | enemy within D | fires | units.py:305 |
| D4 | trigger `ally_at:D` | COMMANDER | D + `waypoint_ref` | waypoint named | fires | units.py:305,312-318 |
| D5 | trigger `own_strength:FRAC` | COMMANDER | FRAC of spawn count | troops <= FRAC | fires | units.py:305,312-318 |
| D6 | trigger `signal:NAME` | COMMANDER | NAME | NAME in issuing Unit's `fired_signals` | fires | units.py:305; core/contact.py:64 |
| D7 | behavior fields settable by an order (17): stance, instructions, unit_type, role, target_condition, target_delay_ticks, order_target_idx, escort_of, escort_offset, escort_engage_on_contact, yielding, route, _route_idx, fire_signal*, feign_retreat* (*pseudo-fields) | COMMANDER | attr -> value | name in `_ORDER_SAFE_FIELDS`; malformed trigger raises at construction | setattr on subunit (pseudo-fields act on Unit) | units.py:271-300; core/contact.py:64 |
| D8 | targeting values in play | COMMANDER | `nearest`, `weakest`, `in_range:N`, `direct` | none | target assignment | units.py:411; core/contact.py:199 |
| D9 | stance (engine set) | COMMANDER | aggressive / balanced / hold / retreat | none | speed mod +1/0/-99/0; commitment +1/0/-1/-1 | config.py:279,290 |

### E. Role instruction keywords (what a role package contains; ROLE_INSTRUCTION_PRIMITIVES, units.py:71)
| # | keyword | wired to | cite |
|---|---|---|---|
| E1 | brace | charge-shock floor, recoil, setup delay | units.py:73 |
| E2 | envelop | envelop path | units.py:74 |
| E3 | sweep | sweep path | units.py:75 |
| E4 | kite | kite standoff band | units.py:76 |
| E5 | reserve | `unit_in_reserve` | units.py:77 |
| E6 | hold | stance hold | units.py:79 |
| E7 | push | stance aggressive | units.py:80 |
| E8 | charge | stance aggressive | units.py:81 |
| E9 | lure | Feigned Retreat (PP-256) | units.py:83 |
| E10 | pin, loose, harass, screen, pursue, volley, shoot_move | UNWIRED (no primitive; reasons in source) | units.py:85-100 |

### F. Roles x shapes (ROLE_SPEC, config.py:603) and shapes
| # | role | shape | instructions |
|---|---|---|---|
| F1 | ShieldWall | Line | brace, hold |
| F2 | Hold | Line | hold |
| F3 | Anvil | Line | brace, pin |
| F4 | Push | Line | push |
| F5 | Skirmish | GappedLine | loose, harass |
| F6 | Screen | Line | screen |
| F7 | Pursue | Line | pursue |
| F8 | Shock | Arrowhead | charge |
| F9 | Flanker | Line | envelop |
| F10 | Feint | Line | lure |
| F11 | VolleyLine | Line | volley |
| F12 | Harass | GappedLine | loose, shoot_move |
| F13 | Kite | GappedLine | kite, shoot_move |
| F14 | Support | Line | reserve |
| F15 | Reserve | Line | reserve |
Shapes with min discipline (MIN_DISCIPLINE, config.py:201): Line 1, Arrowhead 4, GappedLine 5, Column 3 (Column has no role using it).

### G. Battle-run functions the module exposes (ENGINE; no one selects)
| # | name | inputs | cite |
|---|---|---|---|
| G1 | `run_battle` (18 ticks) | unit_a, unit_b, max_turns | orchestration.py:1815 |
| G2 | `run_multi_turn_battle`, `run_multi_unit_battle` | units, shapes, pairings | orchestration.py:2485,2688 |
| G3 | `resolve_engagements`, `resolve_engagements_cascading` | units, pairs | orchestration.py:727,1400 |
| G4 | `resolve_feigned_retreat` | pursuer, feigning unit | orchestration.py:2622 |
| G5 | `check_orders`, `assign_targets`, `resolve_cross_side_contention` | unit(s), tick | core/contact.py:64,199,232 |
| G6 | `terrain_row_for_territory`, `river_crossed` | tid, fort_level, river_crossing, geography | terrain.py:~110 (function name located by grep of docstring; line not re-read) |
| G7 | perimeter: `perimeter_faces`, `target_points`, `nearest_target`, `approach_alignment` | cells, attacker | perimeter.py:78,114,151,162 |
| G8 | recruitment: `under_arms_cap`, `recruit_limit`, `training_site_for` | weight, sites, raised, full | recruitment.py:72,78,83 |
| G9 | registry accessors: `stats_for`, `reach_for`, `roles_for`, `role_allowed`, `is_mounted`, `support_weight`, `support_ranks_for`, `unit_type_for`, `loadout_for` | troop type | registry.py:23-27,78,127,147,151,172; equipment/__init__.py:45 |
| G10 | `build_army` | specs, name, faction, power, command, discipline, morale, stance, speed, anchor_col, officers | armies.py:119 |

Caveats: this table was built from module_contracts.yaml, armyrecord.py, orderofbattle.py and the Order/ROLE sections of hierarchy/units.py. hierarchy/units.py is 3068 lines and orchestration.py/core/ were only grepped for public `def` names; internal Subunit/Unit methods (movement, morale, cell primitives) are engine-computed and not itemised. The provisioning row's name (A6) and `terrain_row_for_territory`'s line were not individually opened.
