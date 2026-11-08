# Provenance for the CR-106 / CR-107 content drafts (first reading; Jordan to correct)

Every row in both drafts is `[ASSUMPTION; medium; Jordan to correct]`. Quarantined design documents are
cited by bare filename, as reference (intent and vocabulary), never as authority. "The plan" and an entry
handle (CR-106, CR-107) mean `workplans/valoria_master_workplan_v11_part16.md`'s entries. The engine's places win over prose (Jordan,
2026-11-08: "Canon territory locations should be matched to engine reality"). Places come from
`build_realm(0)` and the geography YAML as the engine loads it.

## A. `content_church_sites.yaml`

| row id | value | source file:line | rule applied | alternative rejected |
|---|---|---|---|---|
| A1 kinds | `worship`, `templar_quarters`, `school` | CR-106 (a); Jordan ruling 3 | the names CR-106 proposes. "schools/monasteries" is treated as one function | three kinds per function (chapel/church/cathedral). Rejected by CR-106 (a): it would duplicate the condition ladder (ED-IN-0279, H-38) |
| A2 wear_per_season | 0 ×3 | `engine/season/rosters.yaml:1868` (dwelling 0, control arm), `:1869-1873` (garrison, training kinds) | the control arm, as for every non-producing fabric | non-zero wear. Rejected: H-165, a pacing decision nobody has made (`rosters.yaml:1851-1863`, the wear note) |
| A3 capacity_floor | 0 ×3 | `rosters.yaml:1897-1906`; `queries/world_q.py:1855-1880` (capacity counts dwellings only) | every non-dwelling kind is 0 | — |
| A4 works_cost | `{timber: 10}` ×3 | `rosters.yaml:1939-1949`; H-166's one magnitude, `:1933-1938` | every fabric kind is priced alike. Optional per CR-106 (a) | unpriced, so `build` refuses (`loop/effects_founding.py:218-221`). That leaves the orchestrator a choice: with no price, a Church Site can never be newly built |
| A5 worship band_floors | chapel 100 / church 500 / cathedral 800 | `rosters.yaml:3497-3500` (`body`: 100/500/800, the only three-floor row) | Jordan's three scales map onto the one three-floor precedent ladder | the two-floor ladders (harbour 800/100 `:3491-3493`, seam 700/50 `:3494-3496`). Rejected: they carry two bands, and Jordan named three |
| A6 templar band_floors | station 100 / house 500 / chapter 800 | same ladder. `station` from `settlement_layer_v30.md:119` ("Templar Station", ref.); `chapter` from `venues.yaml:86` (`chapter_house`) | same ladder, so the methodology stays consistent (S) | `house` is UNDERIVED (see below) |
| A7 school band_floors | school 100 / monastery 500 / university 800 | Jordan ruling 3 (schools/monasteries); `canon/03_canonical_timeline.md:62` ("the university system"); `faction_politics_v30.md:850` (ref., "university curricula in all territories") | same ladder | — |
| A8 site_owner | `Church of Solmund` ×3, default null | CR-106 (b); Jordan ruling 3; the factions roster (`FACTIONS` holds `Church of Solmund`) | ownership is a data cell on the kind, with no branch on a name | a `Site.owner` field. Rejected by CR-106 (c) |
| A9 worship rows | Seat `cathedral`, City/Town/Village/Fortress/Fortress-City `chapel`, Cathedral-City `cathedral` | `venues.yaml:68,79,85,97,103,108,116`; `settlement_layer_v30.md:117` (ref., Axis 1: one religious building per settlement) | each type's single Church worship row | — |
| A10 school rows | Seat `scriptorium`, Cathedral-City `scriptorium` | `venues.yaml:73,87`; canon :50 ("educational monopoly"), :58 ("educational rights, archival authority") | a scriptorium is the archival/educational house | `chapter_house` and `almonry` as `school` (the plan's first reading). Rejected: an almonry is a charity house (canon :58 "charitable operations"), not on Jordan's list. `chapter_house` goes to A11 |
| A11 templar row | Cathedral-City `chapter_house` | `venues.yaml:86`; canon :50, :62 (Knights Templar established and incubated at the containment city) | the order's chapter meets at the Church's seat | no Templar row at start (the plan's first reading). Rejected: Jordan ruling 3 states that Templar quarters exist |
| A12 almonry | no `site:` | Jordan ruling 3's closed list | not worship, Templar or school | `school` (the plan). See A10 |
| A13 conditions | Village/Fortress 300; Town/City/Fortress-City 650; Seat 900; Cathedral-City 1000 | capacity tiers measured on `build_realm(0)` (validator line 10); band midpoints from A5-A7; `condition_scale` 1000 (`data/fixtures.py:217`) is every minted Site's start (`harness/populated.py:1219-1260`); the Church's seat is `venues.yaml:147` | tier → band; start at the band midpoint; the Church's venues seat starts at `condition_scale` | every Site at `condition_scale`. Rejected: every chapel would then sit in the cathedral band. Starting at the floor was also rejected: it leaves no downward headroom once wear is turned on |
| A14 condition key | nested `site: {kind, condition}` on the venue row | CR-106 (d); coordinator ruling B7 (the ADOPTED shape) | needed for A13 | a flat `site_condition:` key (my first draft). Replaced by the ruling |
| A15 coverage | every territory under `r_valoria` that holds a settlement holds at least one Church Site (15 of 15, measured). T16 Schoenland, a foreign root, also holds 1 | Jordan ruling 4; coordinator ruling B4 | — | Documented exceptions, not failures: `terr_T15` holds no settlement (geography `:201-214`, `settlements: []`); `terr_ALT` is a foreign root whose one settlement (`set_alt_1`, `harness/populated.py:1173-1178`) has no venue rows |

## B. `content_cohorts.yaml` (revision 2: coordinator rulings B1, B2, B3, B5)

The file header states rules H, C and V. `content_validate.py` re-derives all 51 rows from them and diffs the
result against the draft (an empty diff on the final run).

**Faction commitment is HELD (B1).** No row carries `faction:`. A `commit` Tenure makes the faction OCCUPY the
settlement at build (`world_q.py:2131-2172`: occupies, then mustered; the cohort's `contain` is at the
settlement, `populated.py:517`). That would license seize, raze and levies from tick 0 (Altonia in Lowenskyst
Fortress; the Church in six Varfell settlements) and turn `test_in36_foreign.py:120` red. Allegiance is carried
by `heritage` and `conviction` only. Re-admitting `faction:` waits on an audit of the readers of a cohort's
commit: `occupies`, `mustered`, `standing_at`, `raisable_by`, `acquaintance_pairs`, `opinion_referents`,
`footprint` and `density`.

| row id | value | source file:line | rule applied | alternative rejected |
|---|---|---|---|---|
| B-H1 T4, T12, T13 → southern_einhir | 7 settlements | `faction_politics_v30.md:657` (ref.) names T4 Grauwald, T13 Oastad and "the western fjords" (T12, region Western Fjords, geography `:165`); canon `03_canonical_timeline.md:76` (Lupicco, later Varfell, is the southern provinces) and `:100` (Varfell territories have the highest concentration; **its "T1-T4" translated to the engine's Varfell holdings**) | explicit territory ids win | — |
| B-H2 T11 → northern_einhir | S-028, S-029, S-030 | `faction_politics_v30.md:655` (ref., "Northern Einhir (Varfell highlands ...)"); geography `:152` (region Central Fjords), `:161` ("Varfell central fjords. North-of-lake") | T11 is the one Varfell territory that :657 does not name, that is not the western fjords, and that lies north of the lake | **The :655 vs :657 conflict:** read literally, "Varfell highlands" matches T4, the only Varfell territory whose region is "Highlands" (geography `:61`, Central Highlands), but :657 names T4 southern. Ladder step 3: an explicit territory id (:657) beats a regional phrase (:655), so :655's Varfell north is placed on T11, the north-of-lake territory nothing else claims. Rejected: T4 northern (contradicts :657's explicit id) and an all-southern Varfell (my first draft; it erases :655) |
| B-H3 band ≤1, non-Varfell → southern (T6) | S-012, S-013 | canon :100 ("Stigma radiates from the Southernmost"); geography `:842-872` (T6 is band 1); `faction_politics_v30.md:657` names T6 | — | — |
| B-H4 band 2-3 → central (T1, T5, T14) | 8 settlements | `faction_politics_v30.md:656` (ref., "Valorsmark core"); bands | — | T1 northern (canon :80, the first Almqvist's descent). Rejected: that is one family, not the populace |
| B-H5 band ≥4 → northern (T2 T3 T7 T8 T9 T10 T17) | 14 settlements | `faction_politics_v30.md:655` ("Hafenmark, Crown heartland"); canon :76 ("primarily northern") | — | T9 central (an unratified proposal's lifepath example). Rejected |
| B-H6 T16 → schoenlander | S-037 | heritage roster member; NPC-012 (`npc_registry.yaml:514`); T16 is a root (`populated.py:1145-1153`) | — | the band rule (band 4 → northern). Rejected: T16 lies outside the realm |
| B-C1 caste, T5 / T6 | T5 + `southern` ×3; T6 + `central` ×2 | canon :94-100 (the caste line; "Southern Crown territories are viewed as instrumental"); bands; Valorsmark's seat territory T1 (`venues.yaml:144`) → central | caste contact where the gradient meets a non-Varfell holder | — |
| B-C2 T11 + southern | `southern` at S-028 (cap 7), S-029 (4), S-030 (4) | `faction_politics_v30.md:657` ("distributed populations in the western fjords", which border T11; Varfell is Lupicco, canon :76); coordinator B2 | sum of weights 4 ≤ capacity at all three | — |
| B-C3 Varfell north minority | `northern` at S-026 (cap 7), S-031 (9), S-032 (7), S-033 (7), S-034 (7) | `faction_politics_v30.md:655` (Northern Einhir in Varfell); Jordan ruling 1's own example; coordinator B2 | southern-majority Varfell settlements of capacity ≥ 6. Villages S-027 and S-035 (capacity 4) stay single | a northern row in every Varfell village. Rejected: the coordinator's capacity threshold, and it would fill those villages to capacity |
| B-C4 altonian | `altonian` at S-007 | `venues.yaml:152` (`Altonian: S-007`); `names_index.yaml:352` (`Altonian` is a people, not a faction); geography `:875` `altonian_passes` (S-007 is the primary crossing) | a venues seat tag naming a people that is a heritage member | `Einhir` (S-026): not one heritage member, and S-026 already holds northern and southern |
| B-V conviction | header rule V. southern: einhir = 6 − band; northern/central: solmund = min(5, 1 + band); T9 solmund 5; every other affiliation 1 | geography `radiation_bands` `:842-872`; `descriptor_registry.yaml:245-247` (`engages:`); 0-5 scale (`data/affiliations.py:39-70`) | `[ASSUMPTION; one rule on the geography's band data, swept with the bands; Jordan to correct]`. I applied the solmund half to every northern/central cohort, minorities included (coordinator wording: "non-southern majorities"); it is limited to Einhir heritages because the bands are canon :100's peninsular gradient | **the cast median** (per-faction median_low of the `npc_registry.yaml` affiliations; my first draft). Rejected by the coordinator's ruling: it gives a whole populace its leaders' intensity. **The Piety tables** (`conviction_track_v30.md:43-60` vs `peninsular_strain_v30.md:102-120`, disagreeing on T1, T2, T3, T6, T13, T14): rejected, each is one territory-wide two-ended track with no split rule (`cohorts.yaml:103-111`) |
| B-V2 conviction, heritages with no band data | altonian (S-007): altonian_civics 4, others 1; schoenlander (S-037): 1 throughout | coordinator ruling (ladder steps 4/5); `descriptor_registry.yaml:245-247` (`altonian: altonia`; schoenlander has no `engages:` cell); Altonia's cast rows NPC-011/089/090 civics 3/4/5 (`npc_registry.yaml`), median_low 4; the people's faction is the faction whose cast rows carry the heritage (NPC-011 altonian, NPC-012 schoenlander) | the second branch of rule V. The branch key is DATA: does the heritage hold a majority cohort in a territory under `r_valoria`? (validator prints the band-data heritages: central, northern, southern Einhir). With no band data, the engaged affiliation reads the people's faction cast median and every other member reads 1. `[ASSUMPTION; medium; Jordan to correct; revert: 1 everywhere]` | 1 everywhere (revision 2). Rejected: Jordan names the Altonian political system as an axis, so it needs an intensity. Schoenland's civics median (2) is NOT applied: schoenlander engages no concern, and keying on the name would break the data rule. **The orchestrator decides** whether to add `schoenlander: altonia` to `engages:` (a registry edit, ED-IN-0301's confirmed cells) |
| B-W weights | all 2 | `cohorts.yaml:40-44` (S9's smallest weight; H-170) | — | — |
| B-L labels | majority unlabelled; minorities `southern`, `central`, `northern`, `altonian` | CR-107 (an unlabelled row keeps today's id) | majority id `cohort_<rung>` is kept | `commons` on the majority (moves every id) |
| B5 aliases | no `Guild`, `Altonian` or `Einhir` → faction mapping | coordinator B5; `names_index.yaml:352-353` | — | my first draft's hand map. Dropped |

**Rows dropped from the first draft, and why.** With no `faction:` (B1), no alias map (B5) and one conviction
rule (B3), these rows would be the majority cohort's twin (same heritage, same conviction), so they were
removed rather than kept as copies: `guilds` (S-006), `loewenritter` (S-014), `restoration` (S-026), and
`orthodox` (S-026, S-028, S-031, S-032, S-033, S-034, S-037). The creed contest the `orthodox` rows carried now
lives in the northern/southern pairs: in every one of the 8 settlements holding both, a solmund-leading row
sits beside an einhir-leading row.

## CANON LOCATION DISAGREEMENTS (engine wins; for a later editorial alignment)

| place | prose says | prose file:line | engine holds | engine file:line |
|---|---|---|---|---|
| Himmelenger (cathedral city) | T14 | `canon/03_canonical_timeline.md:58` | T9 (T14 is Ehrenfeld) | `systems/settlements/valoria_geography_v30.yaml:123-134` (T9), `:528`ff S-036 `territory: T9`; `venues.yaml:147` |
| Varfell territories | T1-T4 | `canon/03_canonical_timeline.md:100` | T4, T11, T12, T13 (T1-T3 are Valorsmark) | geography `:57-200` `faction:` fields; `build_realm(0)` `holder_faction_of` |
| Valorsplatz Cathedral | S-003 | `settlement_layer_v30.md:1093` | S-001 (S-003 is Königsbrück) | geography S-001 description; `cohorts.yaml:65,67` |
| Church holdouts if Himmelenger falls | S-023 through S-025 | `settlement_layer_v30.md:1093` | S-023..S-025 are Halvarshelm Town / Erzbach / Schmiedhof in T17 (Hafenmark). The intended referent is unknown | `cohorts.yaml:87-89` |
| Gransol / Gransol Parliament | S-015 | `settlement_layer_v30.md:712, 716, 1089` | S-018 (S-015 is Nordhain, T14) | `cohorts.yaml:79,82`; `venues.yaml:146` |
| Gransol Market Quarter | S-017 | `settlement_layer_v30.md:716` | S-017 is Holzbrück (T7); Gransol is S-018 | `cohorts.yaml:81` |
| Stillhelm | S-010 | `settlement_layer_v30.md:1091` | S-012 (S-010 is Erntehof, T5) | `cohorts.yaml:74,76` |

The territory numbering in `faction_politics_v30.md:657, 683`, `conviction_track_v30.md:43-60`,
`peninsular_strain_v30.md:102-120` and `territory_temperaments_v30.md:41-53` agrees with the engine for every
row I used. No translation was needed.



## UNDERIVED

1. The middle Templar band name `house` [ASSUMPTION]: no source names a mid-sized Templar establishment.
2. Band floors 100/500/800 for all three kinds are borrowed from `body` [ASSUMPTION].
3. The midpoint start rule (A13) is a structural choice, not a sourced magnitude [ASSUMPTION].
4. Per-type venue rows give Sigurdshelm (a southern Varfell seat) the same 900 cathedral and university as
   Valorsplatz. A per-settlement condition needs a per-settlement override that `venues.yaml` does not have.
5. Rule V2: `schoenlander` has no `engages:` cell, so its row holds 1 throughout. The ruling's "Schoenland's median for the schoenlander row" cannot be met without a registry edit (see B-V2).
6. Rule V's solmund half is applied to northern/central MINORITY rows as well as majorities (see B-V).
7. T15 and terr_ALT hold no Church Site; these are documented exceptions under A15.

## Consequences the orchestrator should see

- **Room for migration.** Every village and fortress holding two cohorts reaches summed weight 4 =
  capacity 4 (validator: min room 0). `has_room` counts named residents too (`world_q.py:1785-1798`, :1883), so
  `migrate` into them is refused from tick 0.
- **Creed contest.** `incompatible[solmund_orthodoxy][einhir_restoration]` is `true` (`rosters.yaml:3604`),
  so every northern/southern pair and every T5/T6 caste pair holds positions on both ends of that incompatible
  pair (whether `commensurate` reads them as opposed depends on its "held above 0" reading, which I did not run).
- **No new Tenures** beyond today's `contain` and `reside` per cohort (B1).
- **`set_alt_1`** (capacity 1) has no cohort, as today.

## VALIDATION — `content_validate.py`, run verbatim

Command, from the repository root: `python proposals/2026-11-08-flow-conditioning/content_validate.py` (exit 0). The same output is kept beside it as `content_validate.out`.

```
== A. Church-owned Sites
PASS new kinds ['worship', 'templar_quarters', 'school'] collide with no existing site_kinds member
PASS wear_per_season_rates keyed on exactly the three new kinds
PASS capacity_floor_floors keyed on exactly the three new kinds
PASS works_cost_costs keyed on exactly the three new kinds
PASS band_floors_cells keyed on exactly the three new kinds
PASS site_owner[worship] = 'Church of Solmund' is a factions member
PASS site_owner[templar_quarters] = 'Church of Solmund' is a factions member
PASS site_owner[school] = 'Church of Solmund' is a factions member
PASS capacity is uniform per settlement type: {'Seat': {9}, 'Town': {7}, 'Village': {4}, 'Fortress': {4}, 'Fortress-City': {6}, 'City': {6}, 'Cathedral-City': {6}}
PASS the Church's seat type Cathedral-City has exactly one settlement (per-type row = per-settlement)
PASS Seat:cathedral uses the adopted nested shape site: {kind, condition}
PASS Seat:cathedral is an existing venues.yaml row
PASS Seat:cathedral condition 900 == rule 900
PASS Seat:scriptorium uses the adopted nested shape site: {kind, condition}
PASS Seat:scriptorium is an existing venues.yaml row
PASS Seat:scriptorium condition 900 == rule 900
PASS City:chapel uses the adopted nested shape site: {kind, condition}
PASS City:chapel is an existing venues.yaml row
PASS City:chapel condition 650 == rule 650
PASS Cathedral-City:cathedral uses the adopted nested shape site: {kind, condition}
PASS Cathedral-City:cathedral is an existing venues.yaml row
PASS Cathedral-City:cathedral condition 1000 == rule 1000
PASS Cathedral-City:chapter_house uses the adopted nested shape site: {kind, condition}
PASS Cathedral-City:chapter_house is an existing venues.yaml row
PASS Cathedral-City:chapter_house condition 1000 == rule 1000
PASS Cathedral-City:scriptorium uses the adopted nested shape site: {kind, condition}
PASS Cathedral-City:scriptorium is an existing venues.yaml row
PASS Cathedral-City:scriptorium condition 1000 == rule 1000
PASS Fortress-City:chapel uses the adopted nested shape site: {kind, condition}
PASS Fortress-City:chapel is an existing venues.yaml row
PASS Fortress-City:chapel condition 650 == rule 650
PASS Fortress:chapel uses the adopted nested shape site: {kind, condition}
PASS Fortress:chapel is an existing venues.yaml row
PASS Fortress:chapel condition 300 == rule 300
PASS Town:chapel uses the adopted nested shape site: {kind, condition}
PASS Town:chapel is an existing venues.yaml row
PASS Town:chapel condition 650 == rule 650
PASS Village:chapel uses the adopted nested shape site: {kind, condition}
PASS Village:chapel is an existing venues.yaml row
PASS Village:chapel condition 300 == rule 300
Church Sites by kind: {'school': 3, 'templar_quarters': 1, 'worship': 37} total 41
Church Sites by territory: {'terr_ALT': 0, 'terr_T1': 4, 'terr_T10': 2, 'terr_T11': 3, 'terr_T12': 4, 'terr_T13': 2, 'terr_T14': 2, 'terr_T15': 0, 'terr_T16': 1, 'terr_T17': 3, 'terr_T2': 3, 'terr_T3': 2, 'terr_T4': 2, 'terr_T5': 3, 'terr_T6': 2, 'terr_T7': 2, 'terr_T8': 3, 'terr_T9': 3}
PASS terr_T1 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (4)
PASS terr_T10 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T11 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
PASS terr_T12 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (4)
PASS terr_T13 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T14 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T17 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
PASS terr_T2 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
PASS terr_T3 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T4 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T5 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
PASS terr_T6 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T7 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (2)
PASS terr_T8 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
PASS terr_T9 (under r_valoria, holds a settlement) holds >= 1 Church-owned Site (3)
coverage: 15 of 15 territories under r_valoria that hold a settlement
EXCEPTION terr_ALT: foreign root (not under r_valoria); 1 settlement(s), no venue rows; Church Sites 0
EXCEPTION terr_T15: holds no settlement; Church Sites 0
EXCEPTION terr_T16: foreign root (not under r_valoria); 1 settlement(s); Church Sites 1
PASS the single highest worship Site is at the Church's seat S-036 (1000)
worship band by type: {'Cathedral-City': ['cathedral'], 'City': ['church'], 'Fortress': ['chapel'], 'Fortress-City': ['church'], 'Seat': ['cathedral'], 'Town': ['church'], 'Village': ['chapel']}
PASS village chapel < town church < cathedral
PASS no duplicate minted Site (settlement, slug, kind)
== B. cohorts
PASS every row uses only rung/weight/label/heritage/conviction
PASS NO row carries `faction:` (B1: commitment HELD behind a reader audit)
PASS every one of the 37 geography settlements has a cohort
PASS every rung exists and is a settlement
PASS every weight is an int >= 2
PASS summed weight <= capacity at every rung (over: {})
PASS every heritage is a heritage_roster member
PASS every conviction passes conviction_map ([])
PASS no two cohorts share (rung, label)
PASS no row names a person or keys on a faction/office id
PASS drafted rows == rows re-derived from rules H/C/V (missing [], extra [])
cohort rows: 51 | settlements: 37 | settlements with >1 cohort: 14 ['set_s_007', 'set_s_009', 'set_s_010', 'set_s_011', 'set_s_012', 'set_s_013', 'set_s_026', 'set_s_028', 'set_s_029', 'set_s_030', 'set_s_031', 'set_s_032', 'set_s_033', 'set_s_034']
settlements with a northern AND a southern cohort: 8 ['set_s_026', 'set_s_028', 'set_s_029', 'set_s_030', 'set_s_031', 'set_s_032', 'set_s_033', 'set_s_034']
rows by label: {'(majority)': 37, 'altonian': 1, 'southern': 6, 'central': 2, 'northern': 5}
band-data heritages: ['central_einhir', 'northern_einhir', 'southern_einhir']
rows by heritage: {'central_einhir': 10, 'northern_einhir': 24, 'altonian': 1, 'southern_einhir': 15, 'schoenlander': 1}
room left for migrate (capacity - cohorts), min: 0
== 0 FAIL line(s)
```
