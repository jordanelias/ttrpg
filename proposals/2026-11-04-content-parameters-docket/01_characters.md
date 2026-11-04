# Content parameters docket, chapter 01: Characters and NPCs

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Collation only. Counts measured 2026-11-04 by loading the YAML. `now` is HAS/STUB/NONE for the NPC-roster population as a whole unless a cell says otherwise.
Shorthand: `REG` = `references/npc_registry.yaml`; `NPCS` = `engine/season/npcs.yaml`; `COH` = `engine/season/cohorts.yaml`; `ROS` = `engine/season/rosters.yaml`; `DESC` = `references/descriptor_registry.yaml`; `W10` = `workplans/valoria_master_workplan_v10_part*.md`.

---

## 1. NAMED CHARACTER (NPC)  — carrier: `engine/season/state/carriers.py:693` (`Person`); loader `engine/season/data/cast.py` (reads `REG`); seating `engine/season/harness/populated.py:1190-1234`
Population now: 46 rows in `REG` (35 `status: canonical`, 11 `proposed`), ids NPC-001.. ; 46 rows in `NPCS` (1:1 by case id); 46 case files `engine/season/cases/**/NPC-*.yaml`.   Status: PARTIAL (identity/pursuits/affiliations/faction/role authored 46/46; every other layer thin or absent)

Supply order below follows Jordan's sequence: name -> allegiances/affiliations -> pursuits -> goals -> stance -> weight -> body -> born -> scar -> tenures -> relationships -> arc.

| # | group | parameter | domain (type / closed set / bounds) | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `id` (case id) | string `NPC-NNN`; must equal an NPC case id | REQ | HAS 46/46 | `REG` schema.required; `cast.py:100` (`_rows` keys on `id`) |
| 2 | identity | `first_name` | string | REQ | HAS 46/46 | `REG:35` schema.required; `cast.py:122` `name_of` |
| 3 | identity | `last_name` | string or null (null = mononym; Edeyja, Orm) | REQ | HAS 44 non-null, 2 null | `REG:35`; `cast.py:122-131` |
| 4 | identity | `title` | free string, not normalised to the ladder (e.g. Doux, Confessor, Father, Prince) | OPT | HAS 7/46 | `cast.py:315` `title_of`; `populated.py:1521` |
| 5 | identity | `role` | free string; becomes the seated post when no title | REQ | HAS 46/46 | `REG:35`; `populated.py:1547` |
| 6 | identity | `status` | enum {canonical, proposed}; only `canonical` rows seat an office | REQ | HAS 35 canonical / 11 proposed | `REG:35`; `populated.py:1615,1668` |
| 7 | identity | `source` | provenance string | OPT | HAS 46/46 | `REG` rows (no code reader found) |
| 8 | allegiance | `faction` | string; packed cell `Faction (sub-organization)`; base or parenthetical must resolve to a name in `ROS rosters.factions` (owner `references/names_index.yaml` via `engine/substrate/names.py`) | REQ | HAS 46/46; `cast.defects()` reports unresolved/unbalanced cells | `cast.py:133-170` `faction_of`; `REG:35` |
| 9 | allegiance | `institution` (body the person answers to) | string or null (null = unaffiliated life) | OPT | HAS 28 non-null / 18 null in `NPCS` | `NPCS` header; `populated.py:1176,1744` |
| 10 | allegiance | `affiliations:` — religious/civic conviction map | `{affiliation: int 0-5}`; keys from `DESC affiliation_roster.names` (5); a held 0 = considered rejection; REFUSED unless one member of EACH concern (einhir, altonia, church) present | REQ | HAS 46/46 (einhir_restoration 46, altonian_civics 46, solmund_orthodoxy 44, thread_truth 10, inner_tradition 2) | `cast.py:238-275` `conviction_of`; `data/affiliations.py:38` `conviction_map`; ED-IN-0293 (2) |
| 11 | allegiance | loyalty to faction | DERIVED 0..100 (cosine of person pursuits vs faction `role_template_pursuits`); None for factions with no template | DERIVED | n/a (computed) | `cast.py:372` `loyalty`; `populated.py:904,1394` |
| 12 | allegiance | faction leader designation | map faction -> case id | REQ (per faction) | HAS 7 factions (see section 11 closed sets) | `ROS rosters.faction_leaders.by_faction`; `cast.py:366` |
| 13 | pursuits | `convictions.primary[]` = `{conviction: <pursuit>, weight: float}` | all 15 pursuits named (REFUSED if fewer); names from `DESC pursuit_roster.names`; weight float (unbounded in loader; `float(weight or 0)`); `primary` and `secondary` groups read flat | REQ | HAS 46/46 x 15 entries (690 weights); header marks the whole authoring `[ASSUMPTION; medium; Jordan to correct]` | `cast.py:189-236` `pursuits_of`; ED-IN-0293 (1); `REG:1-30` |
| 14 | goals | `goals:` (per-person free-text list) | list of strings | OPT | HAS 17 non-null of 46 | `REG:35` optional; NO reader (template proposal F9: "not carried") |
| 15 | goals | `want` + `concerns` + `tie` (who the want is about, how chosen) | `want` string; `concerns` case id; `tie` enum {named, institution, roof, neighbour} | REQ (in `NPCS`) | HAS 46/46 (tie: neighbour 17, institution 15, named 12, roof 2) | `NPCS` header; `populated.py:1760-1762`; `want` text has no reader beyond subject (hole H-185) |
| 16 | goals | org-level goals the person commits to | see section 4 (Goal) | — | — | `engine/season/goals.yaml` |
| 17 | stance | `stance` toward persons/seats | DERIVED at build from loyalty: `(valence -5..+5, weight 0..5)` | DERIVED | n/a (35 of 46 hold >=1 row per template proposal probe; not re-measured) | `cast.py:419-445` `stance_from_loyalty`; `carriers.py:703` |
| 18 | weight | `weight` | int >= 1 (1 = individual; >1 = cohort) | OPT | default 1 on all 46 | `carriers.py:698,785` (`__post_init__` refuses <1) |
| 19 | body | `body` (tick-0 value) | int on the `condition_scale` fixed-point (fixture 1000 = full) | OPT | STUB default 1000 | `carriers.py:718`; `data/fixtures.py:217` |
| 20 | born | `age` / `born` | registry `age` int (never present); `Person.born` = tick, default `-age_at_build` | OPT | NONE: `age` non-null 0/46; `born` defaulted on all | `carriers.py:726`; `REG` `age: null [GAP]` |
| 21 | born | `birthplace` | free string | OPT | HAS 5/46 | `REG:35` optional; no reader found |
| 22 | born | `territory` | string `Tnn (name)` | OPT | HAS 7/46 | `REG:35` optional; no reader found |
| 23 | scar | `scar` | `{pursuit-or-affiliation name: count}`; never pre-seeded; written in play | DERIVED | empty by design | `carriers.py:737`; thresholds 1/2/3 ED-IN-0261 |
| 24 | scar | `conviction` (live affiliation intensities) | filled from #10 | DERIVED | — | `carriers.py:746` |
| 25 | tenures | home (`contain`+`reside` Tenures) | a building/rung id in `engine/season/venues.yaml` | REQ (in `NPCS`) | HAS 46/46 | `NPCS` `home`; `populated.py:1178` |
| 26 | tenures | office held (`hold` Tenure) | seat id in `engine/season/offices.yaml`, holder = case id | per seat | HAS (offices scope; see Belongs elsewhere) | `populated.py:1641-1668` |
| 27 | tenures | oaths sworn (`oblige`) | offices.yaml `obligees:` case ids | OPT | HAS (offices scope) | `populated.py:1678` |
| 28 | relationships | kin / bonds | no carrier: Tenure kinds are hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban; none is kin | PLAN/none | NONE | `proposals/2026-10-16-character-template.md` F20 (PROPOSED-ONLY; decision J-T3) ; `W10` part6:130 "bonds have a carrier (`tie`)" |
| 29 | relationships | `tie` Tenures for authored bonds | (referent person id) | OPT | NONE authored on cast; `NPCS.concerns` seeds one OUGHT per row | `W10 part15` CL-OPEN/catalyst (plan, no carrier) |
| 30 | thread | `ts` (Thread Sensitivity) | whole int >= floor `DESC practitioner_stats prac.thread_sensitivity` (0); also accepts range `A-B` (reads A) or `~N`; null = unknown (person cannot attempt `thread_read`) | OPT | HAS 10/46 non-null | `cast.py:283-312`; `carriers.py:756` |
| 31 | thread | `coherence` | int | OPT | HAS 1/46 | `REG:35` optional; write-matrix row but NO `Person` field; no reader |
| 32 | thread | `resonant_style` | free string | OPT | HAS 18/46 | `REG` rows; no reader found (listed RETIRED in suite A2 map) |
| 33 | stats | `stats:` {cognition, focus, endurance, social} | ints (ranges seen) | OPT | HAS 1/46 (NPC-001 only) | `REG:35`; sole planned consumer CR-20 (section 6) |
| 34 | arc | `arc_trajectory` | free string | OPT | HAS 36/46 | `REG:35`; no reader (see section 12) |
| 35 | misc | `cultural_label`, `self_other_initial`, `certainty`, `notes` | `cultural_label` string (17/46), `self_other_initial` float (2/46), `certainty` (8/46), `notes` (15/46) | OPT | partly HAS | `cast.py:215` skips non-list `convictions` keys; `self_other_initial` is `orient`/Self-Other, RETIRED per suite A2 map (ED-IN-0261); no reader |

Owed:
- A pursuit weight vector flagged `[ASSUMPTION; medium; Jordan to correct]` across all 46 rows (`REG:1-30`); 3 weights dropped without a home (NPC-033, NPC-086, NPC-089, `REG` header).
- `age`/`born` for every named person: 0/46 authored (`REG`; `carriers.py:726`).
- Affiliation vectors similarly `[ASSUMPTION]` (`REG:20-26`).
- `ts` authored for only 10 of 46; the remaining 36 read UNKNOWN and cannot pass `thread_read` (`carriers.py:756`).
- `stats` for 45 of 46 (`REG` "deferred per npc_roster_v30"); consumer is CR-20 / PC-14.
- `capability` for 45 of 46: only NPC-088 Carin Vedel carries `{copying: 3}` (`ROS verb_capability.note`; `W10 part2:140` "empty on all 83 realm persons").
- Kin/bond content: no carrier and no data (F20, J-T3).
- `body` per-person tick-0 value and any persistent injury: none authored (default only).
- `goals:` per-person lists exist on 17 rows but nothing seats them.
- The 11 `proposed` rows seat no office (`populated.py:1615`).

Conflicts:
- `REG` rows `NPC-081` `Hafenmark (Inner Council #4)` and `NPC-082` `Varfell (Jarl Council #5)` are unquoted so YAML drops the seat number (`cast.py:133-170` docstring; reported by `cast.defects()`).
- Code names the pursuit `doctrine`/`stewardship` (`DESC pursuit_roster`); `proposals/2026-09-20-pursuit-basis-worksheet.yaml` lists `faith` and `warden` instead (code wins).
- `cast.py` module docstring says `ts` on 32 rows; measured 10 non-null.
- `NPCS` header says "GENERATED by `tools/export_npc_roster.py --build` from case files, hand-editable after"; `name`/`want` are the case's, not authored in `NPCS`.

Belongs elsewhere: office/seat holder rows (`engine/season/offices.yaml`, `populated.py:1641`); faction roster/leaders (`ROS rosters.factions`, `faction_leaders`); venues (`engine/season/venues.yaml` home ids).

---

## 2. COHORT (anonymous population / guard)  — carrier: `Person` at `weight > 1` (`carriers.py:693,785`); loader `engine/season/harness/populated.py:335-560` (`cohort_rows`, `temperament_rows`, `guard_rows`)
Population now: 37 population cohorts (one per settlement S-001..S-037, all `weight: 2`); 16 territory temperaments (T1-T14, T16, T17; T15 absent, holds no cohort); 3 guard cohorts (`off_king` 4, `off_duchess_hafenmark` 2, `off_duke_varfell` 2).   Status: PARTIAL (rows exist, every magnitude an `[ASSUMPTION]`)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `cohorts[].rung` | `set_` + geography settlement id, must be a built settlement rung | REQ | HAS 37/37 | `populated.py:335` `COHORT_FIELDS={rung,weight}` (extra/missing field REFUSED) |
| 2 | weight | `cohorts[].weight` | int > 1, never above `capacity(w, rung)` | REQ | STUB: all 37 = 2 (smallest legal; "a choice against inventing a magnitude") | `COH:50-60`; H-170 |
| 3 | pursuits | `temperaments[].territory` | geography `provinces:` id T1..T17 | REQ per territory holding a cohort | HAS 16 rows | `populated.py:393` `TEMPERAMENT_FIELDS={territory,alpha,beta}` |
| 4 | pursuits | `temperaments[].alpha` | number in [0,1] (bool refused) | REQ | HAS 16, `[ASSUMPTION]` | `populated.py:396-420`; `data/pursuits.py:101` `temperament_pursuits` |
| 5 | pursuits | `temperaments[].beta` | number in [0,1] | REQ | HAS 16, `[ASSUMPTION]` | same |
| 6 | affiliations | cohort convictions | HELD: `Person.conviction` stays `{}`; no source for altonia member, T16 value, or splitting bipolar track | PLAN/HELD | NONE | `COH` header comment (SE-06 / ED-IN-0296) |
| 7 | goals | cohort goals | none by design | — | NONE | `COH` header |
| 8 | guards | `guards[].seat` | an `offices.yaml: seats` id; one row per guarded principal | REQ | HAS 3 | `populated.py:523` `GUARD_FIELDS={seat,weight}` |
| 9 | guards | `guards[].weight` | int > 1, <= capacity of residence settlement | REQ | HAS 3 (4,2,2), `[ASSUMPTION]` | `populated.py:523-560`; IN-60 |

Owed:
- Per-cohort pursuit vector is derived from only alpha/beta; the source gives no 15-pursuit vector or affiliation content per territory (`COH` comment).
- Real population weights: all 2 (H-170).
- Temperament for T15 (Askeheim): in source, holds no cohort, no row.
- Conviction half of cohorts HELD (`COH` header, ED-IN-0296).

Conflicts:
- None found between code and `COH`.

Belongs elsewhere: settlement ids/capacity (settlements agent); `offices.yaml` seat ids.

---

## 3. PURSUIT VECTOR (the 15 pursuits, 7 axes, projection, role templates)  — carrier: `Person.pursuits` (`carriers.py:704`); owners `DESC pursuit_roster`, `DESC axis_roster`, `ROS tables.pursuit_projection`, `ROS tables.role_template_pursuits`; validator `engine/season/data/pursuits.py:40`
Population now: pursuit roster 15 names; axis roster 7; projection table 15x7 = 105 cells (89 nonzero); role-template table 6 templates (5,4,5,3,5,4 entries); ruled by ED-IN-0261.   Status: AUTHORED (roster/projection) / PARTIAL (per-person weights flagged `[ASSUMPTION]`, see section 1 #13)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | the 15 pursuit names | {virtue, honour, liberty, justice, wealth, reputation, scholastics, stability, individuality, community, doctrine, happiness, family, love, stewardship} (owner `DESC pursuit_roster`) | REQ | HAS 15 | `data/pursuits.py:40` `pursuit()`; `cast.py:189` |
| 2 | roster | the 7 axis names | {hierarchical_equal, precedent_substantive, partisan_equitable, selfish_selfless, rigid_flexible, grandiose_humble, deontological_instrumental}; bipolar [-1,+1]; `exposure` forbidden bare; `refusing_pole` = {deontological_instrumental: -1} (owner `DESC axis_roster`, `ROS rosters.pursuit_axes`) | REQ | HAS 7 | `data/rosters.py:819,368` |
| 3 | projection | 15x7 cell values `pursuit -> axis -> float` | every pursuit row and axis key rostered; all-zero matrix refused | REQ | HAS 105 cells (89 nonzero) | `data/verbs.py:1343-1384` `_load_projection`; `ROS tables.pursuit_projection` |
| 4 | role templates | `rosters.role_templates.values` | {sovereign, ecclesiastical, mercantile-procedural, intelligence-diplomatic, reformist, military-order} | REQ | HAS 6 | `ROS role_templates`; `data/rosters.py:1065` |
| 5 | role templates | faction -> template map | Crown sovereign; Church of Solmund ecclesiastical; Hafenmark mercantile-procedural; Varfell military-order; Löwenritter military-order; Restoration Movement reformist; Guilds, Schoenland, Altonia have none | REQ | HAS 6 factions | `ROS role_templates.by_faction` |
| 6 | role templates | `role_template_pursuits` weights per template | `{template: {pursuit: weight}}`; default cell 0.0; keys NOT validated at read (fails silently on a bad pursuit name per worksheet note) | REQ | HAS 6 templates | `data/verbs.py:1387-1408`; `cast.py:372` `loyalty` |
| 7 | per person | pursuit weight per person | see section 1 #13 | REQ | HAS 46 | `cast.py:189` |
| 8 | per cohort | temperament | see section 2 #3-5 | REQ | HAS 16 | `data/pursuits.py:101` |

Owed:
- Intelligence-diplomatic template claimed by no faction (`ROS role_templates.note`).
- Templates for Guilds, Schoenland, Altonia: none; `loyalty` returns None for them (`cast.py:372`).

Conflicts:
- `proposals/2026-09-20-pursuit-basis-worksheet.yaml` pursuit names (`faith`, `warden`) differ from the ruled roster (`doctrine`, `stewardship`); code wins.

Belongs elsewhere: `tables.alignment` (verb x axis) -> verbs agent.

---

## 4. GOAL (organization-level OUGHT)  — loader: `engine/season/data/goals.py` (the one reader); file `engine/season/goals.yaml`; minted at `harness/populated.py` (`seed_goals`)
Population now: 38 goals (org: faction 20, body 16, seat 2; 24 `orientation`, others seat_holders/deed_doers); `goal_stages:` 0 rows; `axis:` carried by 0 rows; 7 rows plus 2 with `stance` carry `derives`/`stance`.   Status: PARTIAL (FA-05/06 authored; all `[ASSUMPTION]`-marked sources)

Fields per goal row (loader refuses on any violation, `data/goals.py:467-560`):

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `id` | unique string (the Proposition id) | REQ | HAS 38 | `goals.yaml:15` |
| 2 | owner | `org` | exactly one of `{faction: name}` / `{body: name}` / `{seat: seat id}` | REQ | HAS 38 | `goals.yaml:16` |
| 3 | content | `text` | display string | REQ | HAS | `goals.yaml:17` |
| 4 | content | `object` | `{kind, ...}` kind in {person, seat_holders, rung, deed_doers, orientation}; referent per kind (`case`; `seats[]`; `rung`; exactly one of `against`/`engaging`/`kinds`; none) (owner `ROS goal_object_kinds`) | REQ | HAS 38 | `goals.yaml:18-24`; `data/goals.py:264` |
| 5 | content | `stance` | -1 or +1 | OPT | HAS 7 | `goals.yaml:25` |
| 6 | pursuits | `pursuits` | `{pursuit: weight > 0}`, >= 1 entry, names from the 15 | REQ | HAS 38 | `goals.yaml:28` |
| 7 | derivation | `derives` | `{from: goal id, kind in {establishes, influences}}`; acyclic; scope rules (body from own faction, seat from own body/faction) | OPT | HAS 9 (`derives` appears on 9) | `goals.yaml:30`; `ROS goal_derivations` |
| 8 | thrust | `axis` | member of `ROS thrust_axes.values` (14): suppress_einhir_revival, hide_thread_truth, overthrow_church, overthrow_caste, purge_altonia, political_authority, faction_standing, community_benevolence, heal_calamity, revive_einhir, reveal_thread_truth, uphold_church, uphold_caste, altonian_ascendancy; refused on `orientation` | OPT | NONE (0 rows) | `goals.yaml:34` (CL-THRUST B2.1) |
| 9 | provenance | `source` | string | REQ | HAS 38 | `goals.yaml:36` |
| 10 | stages | `goal_stages[]` = `{id, for[], stages[{id, term, predicate, pursuits}]}` | term in {short, medium, long} non-decreasing; >= 2 stages; predicate a `requires_typed` cell | OPT | NONE (0 rows) | `goals.yaml:38-52` (CL-THRUST B2.2); `ROS goal_stage_terms` |
| 11 | completeness | a row per faction with an authored head and per body with a seated member | refusal at `seed_goals` (`goals_complete`) | REQ | see note | `goals.yaml:8-10` |

Owed:
- Thrust `axis` and `goal_stages` ladders: loader supports, zero authored (CL-THRUST, `W10 part15`).
- Per-person (not per-org) ambitions: no carrier (see section 1 #14, #16; layers proposals PROPOSED-ONLY).

Conflicts:
- None.

Belongs elsewhere: faction/body/seat identity of `org` (factions agent).

---

## 5. AFFILIATION ROSTER (religious/civic conviction poles)  — owner `DESC affiliation_roster`; validator `engine/season/data/affiliations.py:31-180`
Population now: 5 members {solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics}; scale 0-5; concerns: einhir=[einhir_restoration], altonia=[altonian_civics], church=[solmund_orthodoxy, inner_tradition]; `incompatible` table 4 rows; `affiliation_engagement` table 4 rows x 11 columns.   Status: AUTHORED

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | affiliation names | the 5 above | REQ | HAS 5 | `data/affiliations.py:31` |
| 2 | roster | concerns -> members | map | REQ | HAS 3 concerns | `cast.py:238` via `AFFILIATION_CONCERNS` |
| 3 | table | `incompatible` pairs | bool per affiliation pair; default None | REQ | HAS | `data/affiliations.py:72-114` `_load_incompatible` |
| 4 | table | `affiliation_engagement` | float/None per (verb column x affiliation); `sacred` shared column | REQ | HAS (verb columns: verbs agent) | `data/affiliations.py:122-180` |

Owed: none found in code. Conflicts: none. Belongs elsewhere: verb columns of `affiliation_engagement`.

---

## 6. ATTRIBUTE SET  — carrier: NONE in `Person` (PLAN `CR-20`: `Person.attributes`); registry `DESC attributes` (read by `engine/substrate/descriptors.py` as `ATTRIBUTES`)
Population now: registry names 9 keys; 0 persons carry one; `Combatant` args take 8 integer attributes in `modules/combat/combatant.py:93`.   Status: PLACEHOLDER (roster only)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | nine attribute keys | attr.body.{strength, endurance, agility}; attr.mind.{focus, acuity, will}; attr.social.{attunement, charisma, bonds}; scale 1-7, default 1 (owner `DESC attributes`) | REQ | HAS 9 | `DESC attributes`; `W10 part12:124` CR-20 |
| 2 | roster | tenth attribute | name unresolved; slot refuses a value; default in force = nine | PLAN | NONE | `W10 part12:307`, part15 M23 / J-T2 (ED-IN-0185 Q7 "10 attributes", ED-IN-0301) |
| 3 | carrier | `Person.attributes` keyed by the nine keys | int 1-7 | PLAN | NONE (no field) | CR-20 (`W10 part3:78`) |
| 4 | per person | attribute values per cast row | via cast row `stats:` | PLAN | 1/46 rows have `stats:` (different names: cognition, focus, endurance, social) | CR-20; `W10 part15:139` |
| 5 | derivation | `vocation_attribute` closed row set: vocation -> attribute | rows | PLAN | NONE | CR-20; `faculty` base = vocation's attribute |
| 6 | combat | combat attributes: one owner, one storage, changeable | typed export | PLAN | NONE | PC-14 (`W10 part12:175`) |
| 7 | readers | Attunement reader (competence) | `competence_gain` swept | PLAN | NONE | CR-19 (`W10 part12:123`) |
| 8 | aggregates | agg.body / agg.mind / agg.social | sum of three; status `placeholder` | DERIVED | STUB | `DESC aggregates` |
| 9 | alt designs | six-attribute roster (Body/Frame, Hand, Wit, Nerve/Will, Presence, Sense), ten-axis layer, fifteen traits | — | PROPOSED-ONLY | — | `proposals/2026-10-24-character-layers-v2.md` §3-5; `proposals/2026-10-28-content-architecture-suite/03_P2_attributes_skills_histories.md` §5 (P2-C), held; `proposals/2026-10-16-attribute-derivation*.md`, `attributes-from-scratch*.md` |

Owed: the tenth name (J-T2); every per-person attribute value; vocation->attribute rows.
Conflicts: `DESC attributes` names 9 keys (Strength..Bonds); `modules/combat/combatant.py:93` uses 8 arguments (strength, agi, end, cog, att, spirit, focus, history) plus `disp`; the cast `stats:` uses {cognition, focus, endurance, social}; the held suite proposes six. Four vocabularies exist.
Belongs elsewhere: combat attribute consumption (combat agent).

---

## 7. CAPABILITY / SKILLS  — carrier: `Person.capability` (`carriers.py:702`); owner of keys `ROS rosters.verb_capability.values`; validator `harness/corpus_run.py:335-365` `_check_capability`
Population now: 1 capability key exists in the roster ({copying}, mapped from verbs tell, speak); 1 of 46 cast persons carries it (NPC-088 `{copying: 3}`); `capability` empty on all other persons.   Status: PLACEHOLDER

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | capability key names (the vocations) | closed set = `verb_capability.values` (currently {copying}); a key no verb maps to is refused | REQ | HAS 1 | `ROS verb_capability`; `data/verbs.py:1599` `VOCATIONS` |
| 2 | roster | verb -> capability map | `{verb: key}`; a verb with no row falls back to `pool_default` (not an error) | OPT | HAS 2 rows (tell, speak) | `ROS verb_capability`; `seam/wrappers/sigma.py` |
| 3 | per person | `capability: {key: whole number}` per cast entry | whole int (float truncation refused) | OPT | HAS 1 person | `_check_capability` (`corpus_run.py:351-362`); `corpus_run.py:540` |
| 4 | default | `pool_default` | int fixture (2) | OPT | STUB 2 | `data/fixtures.py:414` |
| 5 | plan | four deferred `verb_capability` rows | — | PLAN | NONE | REM-30 last step / CP-T01-01 (AM-B-01) (`W10 part3:77`) |
| 6 | plan | practice (live windowed results add dice) | — | PLAN (CR-18 "landed" per plan) | see plan | `W10 part12:122` |
| 7 | training | `train` +1 on a held key | writer exists | DERIVED | BUILT | `loop/effects_combat.py:495-512` |

Owed: the vocation/skill list itself (only `copying` exists); per-person capability for 45 of 46 cast and all cohorts; the four deferred rows.
Conflicts: none (`W10 part2:140` "capability empty on all 83 realm persons" vs `ROS` "1 of 430 built persons": different populations, both state near-empty).
Belongs elsewhere: verb names (verbs agent).

---

## 8. HERITAGE / LIFEPATH / HISTORY  — carrier: NONE (PLAN `CR-30` `Person.heritage`; `CR-33` `rosters.yaml: lifepath_templates`, cast row `lifepath:` key)
Population now: 0 authored; no `heritage_roster`, `lifepath_templates`, or `lifepath` key exists in `engine/`, `references/`.   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | heritage | `heritage_roster` 5 members | {northern_einhir, central_einhir, southern_einhir, altonian, schoenlander} with `engages:` cells; confirmed as written, not IN FLUX | PLAN | NONE | CR-30 (`W10 part3:79`, ED-IN-0301) |
| 2 | heritage | `Person.heritage` per person | one of #1; read-off field, written once at world build | PLAN | NONE | CR-30 |
| 3 | heritage | `heritage` member of `person_predicates` | listed predicate {heritage, grade, church_standing, office, residence}; no producer | STUB | HAS name only | `ROS person_predicates`; `W10 part12:313` |
| 4 | heritage | `heritage_gain` | swept value (shipped 0.5, swept [0,0.5,1.0]) | PLAN | NONE | CR-31 |
| 5 | lifepath | `lifepath_templates` rows (34 lifepaths), each expanding to held capability keys at `pool_default`; no dice magnitude, no id stored on `Person` | 34 rows | PLAN | NONE | CR-33 (`W10 part3:81`) |
| 6 | lifepath | `lifepath:` key on each cast row | a lifepath id | PLAN | NONE (0/46) | CR-33; suite appendix_A2 §4 "content (46 cast lifepaths) is Jordan's" (PROPOSED-ONLY) |
| 7 | lifepath | four stages per history (origin -> heritage + conviction intensity; formation -> keys + pursuit tilt; vocation -> keys; catalyst -> one OUGHT commit + `tie` Tenures) | — | PROPOSED-ONLY | NONE | `proposals/2026-10-28-content-architecture-suite/appendix_A2_character.md` §4 |
| 8 | standing | Standing ladders as posts on seats (`offices.yaml: ladders:`), livery in `marks` | names and order | PLAN | NONE | CR-32 (`W10 part3:279`) |

Owed: the 34 lifepath rows; heritage per person (46); lifepath per cast row; ladders (CR-32).
Conflicts: none found in code (no code exists); `marks` field was DELETED from `Person` (`carriers.py:699` comment) while CR-30 plans "the `marks` term's carrier".
Belongs elsewhere: —

---

## 9. KIT / TRADITION OWNERSHIP ON A PERSON  — carrier: NONE in `Person`
Population now: 0.   Status: EMPTY (in the season loop); combat module holds its own constructor args.

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | kit | weapon, armour, equipped, skills per person | combat constructor args `weapon='arming', armor='light', skills, equipped` | PLAN (kit) | NONE on Person; STUB defaults in `Combatant` | `modules/combat/combatant.py:93-94`; `W10 part15` M25 / CL-TROOP kit half (DESIGN-FIRST, no v10 batch builds it) |
| 2 | kit | item class / `hold` Tenure on an item | — | PROPOSED-ONLY | NONE (`state/carriers.py` has no item class) | `appendix_A2_character.md` §3 (held) ; `W10 part13:333` (arms_at_build, 0 entries) |
| 3 | kit | `arms_at_build` inventory | entries | PLAN | NONE (0 entries) | `W10 part13:334` |
| 4 | tradition | `tradition` per person (cognitive-mode profile) | string, default 'none' | STUB | Combatant arg only | `modules/combat/combatant.py:94,103`; `modules/combat/tradition.py`, `traditions.py` |
| 5 | temperament | `disp` combat lean | 1-7, 4 neutral | STUB | default 4 | `combatant.py:99`; unmapped to Person (layers v2 §2) |

Owed: whole carrier and all content. Conflicts: none. Belongs elsewhere: tradition tables and weapon lists (combat agent).

---

## 10. PROGRESSION  — mechanisms: `loop/effects_combat.py:495` (train), `loop/effects_information.py` (pursuit shift), `queries/person_q.py` (scar thresholds)
Population now: BUILT writers; authored content: none required beyond fixtures.   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | training | `train`: +1 on a key the subject already holds | writer | DERIVED | BUILT | `loop/effects_combat.py:495-512` |
| 2 | practice | windowed practice (window 4, step 2, cap `pool_default`) | fixture values | OPT | STUB `[ASSUMPTION]` | `data/fixtures.py:435`; CR-18 |
| 3 | values | pursuit shift on a judgement | fixture (0.1 shipped; ships 0 for some arms) | OPT | STUB | `fixtures.py`; suite A2 §5 |
| 4 | scar | scar thresholds 1/2/3 | ruled constants | DERIVED | HAS | ED-IN-0261, `person_q.py:468-469` |
| 5 | age | `age_step`, `illness_rate` | fixtures | OPT | STUB ship 0 | `data/fixtures.py:542-544` |
| 6 | attributes | change by age band/permanent wound only | — | PROPOSED-ONLY | NONE | `proposals/2026-10-24-character-progression-adjudication.md` (partly superseded by M2/ED-IN-0301) |
| 7 | creation | creation sheet (REM-30 / IN-47) | — | PLAN | NONE | `W10 part3:77` |

Owed: the progression numbers are fixtures flagged `[ASSUMPTION]`. Conflicts: none. Belongs elsewhere: —

---

## 11. PLAYER-CHARACTER CREATION INPUTS (character sheet)  — carrier: NONE; PLAN `REM-30` (IN-47), `CL-CHAR`, `CL-OPEN`
Population now: 0. No `Person` is constructed in the season loop; construction lives in `harness/` only (`corpus_run.py:510`, `populated.py`). Cast entry shape is the closed `CAST_KEYS = (who, role, capability, office, ought)` (`harness/corpus_run.py:313`), with no `pursuits` key.   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | creation | player-authored person (name, pursuits, conviction, capability, attributes, heritage, lifepath) | no carrier | PLAN | NONE | `W10 part3:77` REM-30; CR-20/30/33 |
| 2 | creation | C1 arm: player picks an already-seated person | person id | PROPOSED-ONLY | NONE | `proposals/2026-10-07-character-sheet-spaces.md` §2 |
| 3 | creation | cast-overlay entry | `{who, role, capability?, office?, ought?}` | REQ (for cases) | HAS (corpus cases) | `corpus_run.py:313,335` |
| 4 | creation | dossier option / story openings | — | PLAN | NONE | CL-OPEN / CL-CHAR (`W10 part15:167-172`) |
| 5 | field table | 21-field per-person template (identity, home, institution, faction, office, want/tie, pursuits, affiliations, goals, stance, obligations, ledger, born, body, capability, attributes, TS/coherence, kit, temperament, kin, weight) | — | PROPOSED-ONLY | see section 1 | `proposals/2026-10-16-character-template.md` §2 |

Owed: everything above. Conflicts: none. Belongs elsewhere: —

---

## 12. NAMED-NPC ARC  — carrier: NONE (`arc_trajectory` in `REG` is free text with no code reader)
Population now: `arc_trajectory` string on 36/46 `REG` rows; arc corpus cases `engine/season/cases/ARC*.yaml` and `cases/chain/ARC1-3.yaml`.   Status: PLACEHOLDER

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | arc | `arc_trajectory` | free string | OPT | HAS 36/46 | `REG:35` (no reader; `grep -rn arc_trajectory engine tools --include=*.py` empty) |
| 2 | arc | catalyst: one authored OUGHT commit with thrust ladder | see section 4 #8, #10 | PROPOSED-ONLY / PLAN (CL-THRUST) | NONE | suite appendix_A2 §4; goals.yaml stages |
| 3 | arc | cross-NPC arc conditioners | not adopted | — | NONE | ED-604 ruling (`W10 part10:48`) |

Owed: any executable arc content for named persons. Conflicts: none. Belongs elsewhere: events/arcs (another agent).

---

## CLOSED SETS Jordan must populate (members and counts)

| set | owner | n | members |
|---|---|---|---|
| pursuits | `DESC pursuit_roster` | 15 | virtue, honour, liberty, justice, wealth, reputation, scholastics, stability, individuality, community, doctrine, happiness, family, love, stewardship |
| pursuit axes | `DESC axis_roster` | 7 | hierarchical_equal, precedent_substantive, partisan_equitable, selfish_selfless, rigid_flexible, grandiose_humble, deontological_instrumental |
| affiliations | `DESC affiliation_roster` | 5 | solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics |
| affiliation concerns | same | 3 | einhir, altonia, church |
| attributes | `DESC attributes` | 9 (+1 unnamed) | attr.body.{strength,endurance,agility}, attr.mind.{focus,acuity,will}, attr.social.{attunement,charisma,bonds} |
| role templates | `ROS role_templates` | 6 | sovereign, ecclesiastical, mercantile-procedural, intelligence-diplomatic, reformist, military-order |
| capability keys | `ROS verb_capability.values` | 1 | copying |
| thrust axes | `ROS thrust_axes` | 14 | listed in section 4 #8 |
| goal object kinds | `ROS goal_object_kinds` | 5 | person, seat_holders, rung, deed_doers, orientation |
| goal derivations | `ROS goal_derivations` | 2 | establishes, influences |
| goal stage terms | `ROS goal_stage_terms` | 3 | short, medium, long |
| stance polarities | `ROS stance_polarities` | 3 | legacy, regard, declared |
| person predicates | `ROS person_predicates` | 5 | heritage, grade, church_standing, office, residence |
| faction leaders | `ROS faction_leaders` | 7 | Crown NPC-020; Church of Solmund NPC-021; Hafenmark NPC-050; Varfell NPC-052; Restoration Movement NPC-003; Löwenritter NPC-070; Altonia NPC-089 |
| heritage (PLAN, not in tree) | CR-30 | 5 | northern_einhir, central_einhir, southern_einhir, altonian, schoenlander |
| lifepaths (PLAN, not in tree) | CR-33 | 34 | no member list in tree |

---

## ROSTER APPENDIX (complete; built by script)

Method: one Python script loaded `references/npc_registry.yaml`, `engine/season/npcs.yaml`, `engine/season/offices.yaml` (seats + foreign_seats) and `engine/season/cohorts.yaml`, resolved faction/loyalty through `engine/season/data/cast.py`, and printed one row per id; Y = value present/derivable, blank = absent. `weight` is blank because every named person defaults to 1 (none authored); `stance` Y = `cast.loyalty` is computable (faction has a role template); `capability/attrs` Y = NPC-088's capability overlay or a registry `stats:` block.

Reconciliation: 46 ids in REG, 46 in NPCS, 46 distinct NPC ids across `engine/season/cases/**` (grep), 0 ids held by an office but absent from REG, 0 symmetric difference REG vs NPCS. No `placeholder`-status NPC exists in any source. No NPC appears only in cases/offices/rosters.

### A. Named cast (46)

| id | name | status | faction (raw) | office/seat held | home (venue) -> settlement | pursuits | goals | stance | weight | capability/attrs | body/born/scar | arc_trajectory | kin/bonds | blanks | lines |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NPC-001 | Edeyja | canonical | Independent (Southernmost Wardens) |  | b_s_004_cottage -> S-004 | Y | Y |  |  | Y |  | Y |  | stance, weight, body/born/scar, kin/bonds | REG:46; NPCS:266 |
| NPC-002 | Maret Uln | canonical | Varfell |  | b_s_002_market -> S-002 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:92; NPCS:93 |
| NPC-003 | Yrsa Vossen | canonical | Restoration Movement | off_restoration_leader (offices.yaml:587) | b_s_004_market -> S-004 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:133; NPCS:229 |
| NPC-004 | Sæmund Haelgrund | canonical | Church | off_senior_inquisitor (offices.yaml:434) | b_s_036_cathedral -> S-036 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:174; NPCS:102 |
| NPC-005 | Sigrid Torsvald | canonical | Löwenritter (Riskbreakers) | off_riskbreaker_covert (offices.yaml:561) | b_s_001_court -> S-001 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:215; NPCS:67 |
| NPC-006 | Halvar Brandt | canonical | Löwenritter |  | b_s_014_barracks -> S-014 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:255; NPCS:275 |
| NPC-007 | Annika Feldhaus | canonical | Guilds | off_guild_comptroller (offices.yaml:486) | b_s_006_guildhall -> S-006 | Y | Y |  |  |  |  | Y |  | stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:295; NPCS:156 |
| NPC-008 | Peder Almstedt | canonical | Crown (Ministry) | off_parliamentary_clerk (offices.yaml:317) | b_s_018_hall -> S-018 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:334; NPCS:129 |
| NPC-009 | Gerik Strand | canonical | Crown | off_lord_steward (offices.yaml:343) | b_s_001_court -> S-001 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:373; NPCS:284 |
| NPC-010 | Dalla Virke | canonical | Independent (Virke syndicate — Niflhel DISSOLVED) |  | b_s_006_guildhall -> S-006 | Y | Y |  |  |  |  | Y |  | stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:412; NPCS:75 |
| NPC-011 | Alexios Laskaris | canonical | Altonia |  | b_s_007_barracks -> S-007 | Y | Y |  |  |  |  | Y |  | stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:451; NPCS:293 |
| NPC-012 | Rikard Solberg | canonical | Independent (Schoenland) |  | b_s_001_townhouse -> S-001 | Y | Y |  |  |  |  | Y |  | stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:491; NPCS:84 |
| NPC-013 | Aldric Tormann | canonical | Church | off_cardinal_prudence (offices.yaml:408) | b_s_036_cathedral -> S-036 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:530; NPCS:147 |
| NPC-020 | Almud Almqvist | canonical | Crown | off_king (offices.yaml:187), off_duke_valorsmark (offices.yaml:200) | b_s_002_cottage -> S-002 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:573; NPCS:183 |
| NPC-021 | Arne Himlensendt | canonical | Church | off_confessor (offices.yaml:369) | b_s_003_market -> S-003 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:615; NPCS:192 |
| NPC-030 | Elske Almqvist | canonical | Crown (Royal Family) | off_princess (offices.yaml:265) | b_s_001_court -> S-001 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:662; NPCS:257 |
| NPC-031 | Torben Almqvist | canonical | Crown (Royal Family) | off_heir (offices.yaml:252) | b_s_001_court -> S-001 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:701; NPCS:248 |
| NPC-032 | Lenneth Almqvist | canonical | Crown (Royal Family) | off_widow_regent (offices.yaml:239) | b_s_004_inn -> S-004 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:740; NPCS:239 |
| NPC-033 | Kolbrun Thale | canonical | Crown (Inner Circle) | off_spymaster (offices.yaml:304) | b_s_014_barracks -> S-014 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:780; NPCS:111 |
| NPC-034 | Gustav Linder | canonical | Church (dual-loyalty: Crown Inner Circle agent for Himlensendt) | off_archbishops_rep (offices.yaml:356) | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:819; NPCS:174 |
| NPC-035 | Theodor Kreutz | canonical | Crown (Inner Circle) / Löwenritter Liaison | off_guard_captain (offices.yaml:330) | b_s_014_barracks -> S-014 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:859; NPCS:302 |
| NPC-036 | Wilhelm Voss | canonical | Crown (Inner Circle) | off_royal_marshal (offices.yaml:278) | b_s_001_court -> S-001 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:898; NPCS:311 |
| NPC-037 | Annalie Reichard | canonical | Crown (Inner Circle) | off_lord_treasurer (offices.yaml:291) | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:937; NPCS:320 |
| NPC-038 | Arnlod Olafsson | canonical | Church | off_cardinal_justice (offices.yaml:395) | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:983; NPCS:138 |
| NPC-039 | Magnus Klapp | canonical | Church | off_cardinal_temperance (offices.yaml:421) | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1023; NPCS:330 |
| NPC-040 | Osten Jarnstal | canonical | Church | off_cardinal_fortitude (offices.yaml:382) | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1064; NPCS:339 |
| NPC-041 | Aldric Hann | canonical | Restoration Movement |  | b_s_036_cathedral -> S-036 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1107; NPCS:347 |
| NPC-050 | Inge Baralta | canonical | Hafenmark | off_duchess_hafenmark (offices.yaml:213) | b_s_001_court -> S-001 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:1145; NPCS:201 |
| NPC-052 | Magnus Vaynard | canonical | Varfell | off_duke_varfell (offices.yaml:226) | b_s_003_inn -> S-003 | Y | Y | Y |  |  |  | Y |  | weight, capability/attrs, body/born/scar, kin/bonds | REG:1185; NPCS:211 |
| NPC-070 | Lisbeth Ehrenwall | canonical | Löwenritter | off_grand_master (offices.yaml:538) | b_s_003_cottage -> S-003 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1228; NPCS:220 |
| NPC-071 | Torvi Heljason | canonical | Hafenmark (Inner Council) | off_legal_advisor_hm (offices.yaml:447) | b_s_002_inn -> S-002 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1263; NPCS:165 |
| NPC-072 | Olaf Geirson | canonical | Hafenmark (Inner Council) | off_military_commander_hm (offices.yaml:460) | b_s_014_barracks -> S-014 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1295; NPCS:356 |
| NPC-073 | Björn Holdar | canonical | Varfell (Jarl Council) | off_senior_jarl_west (offices.yaml:499) | b_s_005_croft -> S-005 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1327; NPCS:365 |
| NPC-074 | Ingrid Stenskald | canonical | Varfell (Jarl Council) | off_skald_chief (offices.yaml:512) | b_s_006_market -> S-006 | Y |  | Y |  |  |  |  |  | goals, weight, capability/attrs, body/born/scar, arc, kin/bonds | REG:1359; NPCS:373 |
| NPC-075 | Orm | canonical | Independent (Southernmost Wardens) |  | b_s_001_market -> S-001 | Y | Y |  |  |  |  | Y |  | stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1391; NPCS:58 |
| NPC-080 | Vidar Haldorsen | proposed | Löwenritter (Riskbreakers) | off_riskbreaker_doctrine (offices.yaml:574) | b_s_006_inn -> S-006 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1429; NPCS:382 |
| NPC-081 | Uta Falkenrath | proposed | Hafenmark (Inner Council) | off_commune_rep_hm (offices.yaml:473) | b_s_006_cottage -> S-006 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1463; NPCS:391 |
| NPC-082 | Njal Torberg | proposed | Varfell (Jarl Council) | off_military_jarl (offices.yaml:525) | b_s_008_croft -> S-008 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1495; NPCS:399 |
| NPC-083 | Hedda Kronvald | proposed | Crown |  | b_s_001_court -> S-001 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1527; NPCS:120 |
| NPC-084 | Frieda Kessler | proposed | Guilds |  | b_s_009_market -> S-009 | Y |  |  |  |  |  | Y |  | goals, stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1560; NPCS:408 |
| NPC-085 | Nessa Grindvold | proposed | Guilds |  | b_s_001_court -> S-001 | Y |  |  |  |  |  | Y |  | goals, stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1592; NPCS:418 |
| NPC-086 | Joren Bergvall | proposed | Guilds |  | b_s_006_guildhall -> S-006 | Y |  |  |  |  |  | Y |  | goals, stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1624; NPCS:49 |
| NPC-087 | Uwe Askeland | proposed | Restoration Movement |  | b_s_026_workshop -> S-026 | Y |  | Y |  |  |  | Y |  | goals, weight, capability/attrs, body/born/scar, kin/bonds | REG:1656; NPCS:41 |
| NPC-088 | Carin Vedel | proposed | Restoration Movement |  | b_s_026_workshop -> S-026 | Y |  | Y |  | Y |  | Y |  | goals, weight, body/born/scar, kin/bonds | REG:1688; NPCS:32 |
| NPC-089 | Zoe Palaiologina | proposed | Altonia | off_katepano (offices.yaml:608) | b_s_009_inn -> S-009 | Y |  |  |  |  |  | Y |  | goals, stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1720; NPCS:427 |
| NPC-090 | Stephanos Doukas | proposed | Altonia | off_kommerkiarios (offices.yaml:621) | b_s_009_cottage -> S-009 | Y |  |  |  |  |  | Y |  | goals, stance, weight, capability/attrs, body/born/scar, kin/bonds | REG:1752; NPCS:437 |


### B. Foreign-cast seat holders (`offices.yaml: foreign_seats`, 2 rows; holders are in table A)

| seat | holder | faction | line |
|---|---|---|---|
| off_katepano | NPC-089 | Altonia | offices.yaml:608 |
| off_kommerkiarios | NPC-090 | Altonia | offices.yaml:621 |

### C. Population cohorts (37, anonymous; no name, faction, office, goals, stance, capability, body/born/scar, arc, kin; pursuits derived from territory temperament, section 2)

| cohort rung | weight | settlement | pursuits | line |
|---|---|---|---|---|
| set_s_001 | 2 | S-001 Valorsplatz (Seat, T1) | derived (alpha/beta) | cohorts.yaml:65 |
| set_s_002 | 2 | S-002 Auerheim (Town, T1) | derived (alpha/beta) | cohorts.yaml:66 |
| set_s_003 | 2 | S-003 Königsbrück (Town, T1) | derived (alpha/beta) | cohorts.yaml:67 |
| set_s_004 | 2 | S-004 Kronmark (Town, T2) | derived (alpha/beta) | cohorts.yaml:68 |
| set_s_005 | 2 | S-005 Saatfeld (Village, T2) | derived (alpha/beta) | cohorts.yaml:69 |
| set_s_006 | 2 | S-006 Goldenfurt (Town, T2) | derived (alpha/beta) | cohorts.yaml:70 |
| set_s_007 | 2 | S-007 Lowenskyst Fortress (Fortress, T3) | derived (alpha/beta) | cohorts.yaml:71 |
| set_s_008 | 2 | S-008 Tiefental (Village, T3) | derived (alpha/beta) | cohorts.yaml:72 |
| set_s_009 | 2 | S-009 Feldmark (Town, T5) | derived (alpha/beta) | cohorts.yaml:73 |
| set_s_010 | 2 | S-010 Erntehof (Village, T5) | derived (alpha/beta) | cohorts.yaml:74 |
| set_s_011 | 2 | S-011 Spelzdorf (Village, T5) | derived (alpha/beta) | cohorts.yaml:75 |
| set_s_012 | 2 | S-012 Stillhelm (Town, T6) | derived (alpha/beta) | cohorts.yaml:76 |
| set_s_013 | 2 | S-013 Aschenbach (Village, T6) | derived (alpha/beta) | cohorts.yaml:77 |
| set_s_014 | 2 | S-014 Ehrenfeld (Fortress-City, T14) | derived (alpha/beta) | cohorts.yaml:78 |
| set_s_015 | 2 | S-015 Nordhain (Village, T14) | derived (alpha/beta) | cohorts.yaml:79 |
| set_s_016 | 2 | S-016 Rendstad (Town, T7) | derived (alpha/beta) | cohorts.yaml:80 |
| set_s_017 | 2 | S-017 Holzbrück (Village, T7) | derived (alpha/beta) | cohorts.yaml:81 |
| set_s_018 | 2 | S-018 Gransol (City, T8) | derived (alpha/beta) | cohorts.yaml:82 |
| set_s_019 | 2 | S-019 Niedersol (Town, T8) | derived (alpha/beta) | cohorts.yaml:83 |
| set_s_020 | 2 | S-020 Saltbrück (Town, T8) | derived (alpha/beta) | cohorts.yaml:84 |
| set_s_021 | 2 | S-021 Spartfell Fortress (Fortress, T10) | derived (alpha/beta) | cohorts.yaml:85 |
| set_s_022 | 2 | S-022 Gelbgrund (Village, T10) | derived (alpha/beta) | cohorts.yaml:86 |
| set_s_023 | 2 | S-023 Halvarshelm Town (Town, T17) | derived (alpha/beta) | cohorts.yaml:87 |
| set_s_024 | 2 | S-024 Erzbach (Village, T17) | derived (alpha/beta) | cohorts.yaml:88 |
| set_s_025 | 2 | S-025 Schmiedhof (Village, T17) | derived (alpha/beta) | cohorts.yaml:89 |
| set_s_026 | 2 | S-026 Grauwald (Town, T4) | derived (alpha/beta) | cohorts.yaml:90 |
| set_s_027 | 2 | S-027 Skogheim (Village, T4) | derived (alpha/beta) | cohorts.yaml:91 |
| set_s_028 | 2 | S-028 Halvardshelm (Town, T11) | derived (alpha/beta) | cohorts.yaml:92 |
| set_s_029 | 2 | S-029 Geirsvik (Village, T11) | derived (alpha/beta) | cohorts.yaml:93 |
| set_s_030 | 2 | S-030 Yrnastead (Village, T11) | derived (alpha/beta) | cohorts.yaml:94 |
| set_s_031 | 2 | S-031 Sigurdshelm (Seat, T12) | derived (alpha/beta) | cohorts.yaml:95 |
| set_s_032 | 2 | S-032 Brynjard (Town, T12) | derived (alpha/beta) | cohorts.yaml:96 |
| set_s_033 | 2 | S-033 Sundfjord (Town, T12) | derived (alpha/beta) | cohorts.yaml:97 |
| set_s_034 | 2 | S-034 Oastad (Town, T13) | derived (alpha/beta) | cohorts.yaml:98 |
| set_s_035 | 2 | S-035 Salgrund (Village, T13) | derived (alpha/beta) | cohorts.yaml:99 |
| set_s_036 | 2 | S-036 Himmelenger (Cathedral-City, T9) | derived (alpha/beta) | cohorts.yaml:100 |
| set_s_037 | 2 | S-037 Schoenland (City, T16) | derived (alpha/beta) | cohorts.yaml:101 |

Guard cohorts (3): off_king 4, off_duchess_hafenmark 2, off_duke_varfell 2 (cohorts.yaml guards block).

---

## KEY-FORMAT RE-CHECK (orchestrator correction: Key substrate RETIRED, ED-IN-0232)

Every row above was re-checked for a Key-only source. Result:
- Section 2 #4-#5 (`temperaments[].alpha`/`beta`): the numbers come from the archived `territory_temperaments_v30.md`, whose drift mechanics sit on the retired Key substrate (`COH` comment). The values are read by LIVE code (`harness/populated.py:396`, `data/pursuits.py:101`) and are not themselves Key objects, so they stay REQ; source flagged RETIRED-KEY (source doc only). Live equivalent: none other than these `COH` rows.
- Section 1 #32 `resonant_style` and #35 `self_other_initial`/`cultural_label`: no code reader; `self_other_initial` (`orient`) is RETIRED by ED-IN-0261, `resonant_style` is listed RETIRED in suite appendix_A2 §3. Not Key-based; shown as OPT/no reader, not current parameters.
- Section 1 #11 `loyalty`: docstring cites `key_substrate_v30.md` §2.4 for rationale only; computation is live (`cast.py:372`, pursuit cosine). No row change.
- Section 3 #6 role-template weights: source text cites the old 13-Conviction taxonomy (migrated to the 15 pursuits); the live table is `ROS tables.role_template_pursuits`. No row change.
- No other row in this file rests only on a Key-based, `params_tables.yaml`, `.tres` or KeyStore source.
