# Content parameters docket, chapter 06: Personal combat

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Scope note (measured): the season seam passes the combat engine ONE authored-or-derived field per party, `end` (from `body_band_penalty`); every other `Combatant` field is the class default. `engine/season/seam/wrappers/combat.py:130-153` (`party_end`, `combat_input`); `modules/combat/fight.py:49-50` (`Combatant(a_id, end=a_end)`); `engine/season/queries/inputs.py:112-126` (`PersonalCombatInput` = claimants, ends, wound_quantities). Everything below the seam row is content the engine READS from `modules/combat/` but the season does not yet send. No `terms` field exists on the input yet (`fight.py:52` getattr default).

Typed export `engine/engine_params/combat_engine_v1.json` top-level keys (measured): `_generated, canonical_status, schema_version(=3), sections, source`; `sections` = `cfg` (205 keys) and `core` (25 keys). NO roster Jordan must populate lives in it: all 205 `cfg` keys are numeric tuning (5 are per-armour-tier dicts), `core` holds 18 scalars + 7 token-keyed tables (listed under ENTITY 5/6). No `attributes` section exists (PC-14 unbuilt; `modules/combat/attributes.py` absent).

---

## 1. COMBAT ACTION / ABILITY (learnable technique) — carrier/loader: modules/combat/ability_primitives.py:29 (`ABILITIES`)
Population now: 9 authored (indes, staerke_schwaeche, mezzo_tempo, misura, true_times, atajo, shinogi, zwerchhau, ringen_am_schwert)   Status: PARTIAL
(No per-verb "combat action" roster exists: the engine's actions — attack/parry/dodge/wind/bind/grab/disengage — are code, not authored content. `DEFENCE_MODES` and `GRAB_OUTCOMES` are closed code tuples, see ENTITY 12.)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | ability key (dict key) | str, unique | REQ | HAS (9) | ability_primitives.py:29 |
| 2 | access | `tradition` | enum = keys of TRADITIONS (8) ; import-assert refuses unknown | REQ | HAS | ability_primitives.py:74-77 |
| 3 | grounding | `grade` | str label ('S1/S2','S2','S2/S3'; PC-17 adds 'GENERIC'); read by nothing at resolution | OPT | HAS | ability_primitives.py:31; PC-17 (part4:924) |
| 4 | effect | `lever` | str; levers read at sites (measured via eff_cw/ability_factor call sites): visual, tempo, leverage, balance, tactile, measure, spine_press, facing_regime, choke_control, precommit, edge_read, edge_grab, counter_success, counter_select, anti_overcommit | REQ | HAS | ability_primitives.py:120-147 (ability_bonus/factor) |
| 5 | effect | `op` | enum {'+','*'} ('+' read at 2 sites only) | REQ | HAS | ability_primitives.py:120-147; PC-17 |
| 6 | effect | `value` | float (level-1 anchor; `*` composed value**level clamped [1e-4,1e3]) | REQ | HAS; most tagged [SIM-CALIBRATE] | ability_primitives.py:95-97 |
| 7 | text | `desc` | str | OPT | HAS | ability_primitives.py:29 |
| 8 | investment | level per fighter (`Combatant.equipped` list or {name: level}) | float in [0, MAX_INVESTMENT_LEVEL=8.0] | OPT | NONE (default `[]`) | ability_primitives.py:95,103-123; combatant.py:116 |
| 9 | gate | `known_traditions` (fighter-side) | set/list of tradition keys; falls back to `tradition` | OPT | NONE | ability_primitives.py:111-113 |
| 10 | prerequisite predicate (per ability) | PROPOSED-ONLY | predicate over weapon (e.g. spine>0, grab_hazard>0) | PROPOSED-ONLY | NONE | proposals/2026-09-30-character-and-play-surface/06_weapons_from_physics.md W-5 |

Owed:
- Levers with NO ability authored: `visual, precommit, tactile, tempo, balance, edge_read, choke_control, facing_regime, measure(only misura)`; `seize` lever DEAD — ability_primitives.py:19-27 (docstring); proposals/.../04_the_bout.md B-1.
- 21 GENERIC abilities (7 levers `visual, precommit, tactile, tempo, balance, edge_read, choke_control` x 3 tiers; `op '*'`; x1.10/1.25/1.50, choke_control x0.90/0.75/0.55) + allocate ED-PC-0059 — PC-17 (workplans/valoria_master_workplan_v10_part4.md:924), unbuilt.
- Traditions chinese, filipino have 0 abilities (TRADITION_KIT empty): ability_primitives.py:80 (measured).
- Techniques for unhooked levers (precommit/visual: sen-sen-no-sen, metsuke; balance: compas; tactile: Fuhlen; tempo) — PROPOSED-ONLY, 04_the_bout.md B-1.
Conflicts: ability_primitives.py:19 docstring says "TWO populated morphology levers"; ABILITIES has `shinogi`, `ringen_am_schwert` for those and `zwerchhau`/`atajo` re-homed to counter_select/leverage (code wins; no action).
Belongs elsewhere: `capability`/`technique:indes` practice key (verb `practice`) — Person carrier, proposals/.../09_the_character_sheet.md K-4 (PROPOSED-ONLY).

---

## 2. ATTRIBUTE (combat READS only; person roster owned elsewhere) — carrier/loader: modules/combat/combatant.py:93 (`Combatant.__init__`)
Population now: 9 constructor names, all defaulted; season supplies only `end`   Status: PLACEHOLDER (class defaults)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | body | `strength` | number, default 4 | OPT | STUB(4) | combatant.py:93 ; read ~14x in modules/combat (measured grep) |
| 2 | body | `agi` | number, default 4 (centring literal 4) | OPT | STUB(4) | combatant.py:93 ; ~6 reads |
| 3 | body | `end` | number, default 4; floor 1; ONLY field the season sets, `max(1, 4 - body_band_penalty)` | OPT | HAS (derived) | seam/wrappers/combat.py:130-138; combatant.py:93 |
| 4 | mind | `cog` | number, default 3 | OPT | STUB(3) | combatant.py:93 ; ~2 reads |
| 5 | mind | `att` | number, default 3 (registry key unmapped) | OPT | STUB(3) | combatant.py:93 ; ~3 reads |
| 6 | mind | `spirit` | number, default 3 | OPT | STUB(3) | combatant.py:93 ; ~7 reads |
| 7 | mind | `focus` | number, default 3 (conc_max = 3*Focus + 2*Spirit) | OPT | STUB(3) | combatant.py:93,148-152 |
| 8 | mind | `history` | number, default 3 (pool = max(5, round(History)+6); Ob = History/2) | OPT | STUB(3) | combatant.py:94 ; core.py:54-56 ; ~10 reads |
| 9 | temperament | `disp` | number 1-7, default 4 = neutral; lean=(disp-4)/3 | OPT | STUB(4) | combatant.py:94 ; combat_systems.py:182-183 |
| 10 | structure | attribute storage (`attrs` dict, spec tuple with key/default/neutral/registry_key/status) | PLAN | PLAN | NONE | PC-14 (part4:885) |

Owed:
- PC-14: `modules/combat/attributes.py` spec, `attributes` section in combat_engine_v1.json (SCHEMA_VERSION bump), `rederive()`; unbuilt. Whether `att` = registry Attunement or a separate Attention stays open (J-T2); `registry_key` null for att/history/disp.
- Per-person attribute values: season carrier lands via CR-20 (`Person.attributes`) — PC-14 "LANDED ALREADY: nothing".
Conflicts: workplan PC-14 says "nine names, about 44 reads"; measured read-site regex gives a different tally (undercount-prone); not reconciled here.
Belongs elsewhere: the person's attribute roster (nine registry keys; tenth unnamed, ED-IN-0193) — other docket; `body` band floors `rosters.yaml band_floors` (wound/body input, see ENTITY 11).

---

## 3. SKILL (per-axis bias dict) — carrier/loader: modules/combat/combatant.py:115,156 (`skills`, `skill(axis)`)
Population now: 0 authored (default `{}`; no roster of skill axes)   Status: EMPTY

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | axis | `bind` | float >=0 (0 untrained) | OPT | NONE | combat_systems.py:349,1053 |
| 2 | axis | `grab` | float, clamped so (1-skill)>=0 | OPT | NONE | contact.py:47 |
| 3 | axis | `technique` | float | OPT | NONE | combat_systems.py:332 |
| 4 | axis | `balance` | float | OPT | NONE | combat_systems.py:188 |
| 5 | axis | `parry` (= vocabulary.DEF_PARRY) | float | OPT | NONE | combat_systems.py:337 |
| 6 | axis | `dodge` (= DEF_DODGE) | float | OPT | NONE | combat_systems.py:347 |

Owed: no closed set of skill axes is declared anywhere; the 6 axis names are the call-site literals (measured grep `\.skill(`). `arms` vocation key (CP-T03-04: `capability["arms"]`, derivation formula in `SW`, cast overlay of named fighters) — plan-called, unbuilt (proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-03-personal-combat.md:159-175; workplan row CP-T03-04, part3 / part12).
Conflicts: none.
Belongs elsewhere: `capability` carrier / `train` verb (NPC/EC lane).

---

## 4. LEVER (named modulation channel) — carrier/loader: none as a roster; implicit in `ABILITIES[*]['lever']` and call sites (ability_primitives.py:120-159; combat_systems.py `eff_cw`)
Population now: 15 distinct lever names read at call sites (measured); 9 carry >=1 authored ability   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | lever name | closed set of lever keys | NO owner roster; 15 literals: visual, tempo, leverage, balance, tactile, measure, spine_press, facing_regime, choke_control, precommit, edge_read, edge_grab, counter_success, counter_select, anti_overcommit | REQ(implicit) | HAS (as literals) | combat_systems.py / contact.py call sites |
| 2 | levers with an ability | leverage, measure, counter_success, counter_select, anti_overcommit, spine_press, edge_grab | n=7 populated (from ABILITIES) | — | HAS | ability_primitives.py:29-70 |
| 3 | bare levers | visual, tempo, balance, tactile, precommit, edge_read, choke_control, facing_regime | n=8 unpopulated | PLAN | NONE | PC-17; 04_the_bout.md B-1 |
| 4 | new cfg key | `INIT_TEMPO_LEVER_K` | float [SIM-CALIBRATE] | PLAN | NONE | PC-17 (part4:924) |

Owed: PC-17 (above); `INJECTION_POINTS` stale prose (PC-16 / B-2) — `state_graph.py` not in modules/combat (grep found none).
Conflicts: workplan PC-17 says "21 generic levers" over 7 levers; ability_primitives docstring names 7 "channel levers" + 3 conditional + 5 morphology (different grouping, code lists above).
Belongs elsewhere: none.

---

## 5. EQUIPMENT — WEAPON — carrier/loader: modules/combat/weapons.py:74 (`WEAPONS`)
Population now: 54 records (50 base + 4 derived `_halfsword` forms carrying `base`): rapier, arming, longsword, greatsword, greatsword_halfsword, sabre, dagger, paired_short, spear, staff, mace, poleaxe, longsword_halfsword, yari, kama_yari, dangpa, bear_spear, ranseur, spetum, naginata, glaive, guandao, podao, fauchard, bardiche, sparr_axe, voulge, guisarme, ji, bec_de_corbin, lucerne_hammer, goedendag, katana, tachi, odachi, tsurugi, changdao, nandao, jian, scimitar, pulwar, shamshir, szabla, cinquedea, flamberge, flamberge_halfsword, estoc, estoc_halfsword, falchion, rondel, main_gauche, stiletto, misericorde, hook_sword   Status: AUTHORED (roster) ; the season sends none (seam default `arming`).

Per-record keys measured over 54 records: mass 54, head_len 54, grip_len 54, hands 54, head 54, wclass 54, hilt 54, elements 54, haft 54, geometry 54, guards 45, pommel 31, reach_adj 29, mode_elements 11, butt 8, adornments 3, base 4. Computed at import (not authored): `hand_guard`, `blade_guard` (overwritten, weapons.py bake), `gap`, `geo`, `_derived`.

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | weapon key | str, unique | REQ | HAS (54) | weapons.py:74 ; `Combatant.weapon` combatant.py:94 |
| 2 | classification | `wclass` | enum {bladed(31), hafted_tip(21), hafted_block(2)} (weapon_physics C_HEAD keys, weapon_physics.py:68) | REQ | HAS | weapons.py:20 schema; weapon_physics.py:68 |
| 3 | classification | `head` (native mode) | enum vocabulary.HEADS {blunt, point, cut_thrust, straight_cut, curved_cut, cut}; native counts cut_thrust 18, point 14, curved_cut 12, blunt 6, straight_cut 4 | REQ | HAS | vocabulary.py:30-36 |
| 4 | classification | `hands` | {1 (19), 2 (35)} | REQ | HAS | weapons.py schema |
| 5 | classification | `hilt` | enum vocabulary.HILT_TYPES {compound(5), simple(22), none(27)} | REQ | HAS | vocabulary.py:62-66 ; weapon_physics.py:67,651 |
| 6 | physical | `mass` (kg, = sum of part masses) | float | REQ | HAS | weapons.py schema |
| 7 | physical | `head_len`, `grip_len` (metres) | float | REQ | HAS | weapons.py schema; contact.py:_short_reach_exempt (GRAB_SHORT_REACH_M) |
| 8 | physical | `reach_adj` (reach-points residual) | float, optional (29 of 54) | OPT | HAS(29) | weapons.py schema |
| 9 | parts | `elements[]`: x_m, mass_kg, extent_m, orient_deg, material, [edge_undulation{amplitude_mm,period_mm} (1 weapon)], edges{sides 0/1/2, false_edge_frac} | per-element; `material` str free text (steel/iron/wood/mixed; DELIBERATELY INERT); `edges` set from `_EDGES` (assert every non-base weapon has a row) | REQ | HAS | weapons.py:846-900 |
| 10 | parts | `guards[]`: x_m, mass_kg, extent_m, type, orient_deg, material, [dual_role_element] | `type` free strings measured: cross 16, lug 12, disc 8, wing 6, knucklebow 3, langet 3, ring 3, shell 2, crescent-guard 2, collar 1, quillon 1 ; 45 of 54 records have guards | OPT | HAS | weapons.py schema |
| 11 | parts | `haft` {x_m, mass_kg, extent_m}; `pommel` {x_m, mass_kg} (31); `butt` {x_m, mass_kg} (8) | float | REQ(haft)/OPT | HAS | weapons.py schema |
| 12 | geometry | `geometry`: curvature, point_concentration, cross_section, edge_keenness, strike_concentration | each float 0..1 (geometry.py:16-24) | REQ | HAS (54) | geometry.py bake; weapons.py:923 |
| 13 | modes | `mode_elements[]`: head, element_ref (int index into elements, assert in range), geometry | 11 weapons carry them | OPT | HAS(11) | weapons.py D0 build assertion |
| 14 | read | `adornments[]`: count, extent_m | 3 weapons (ranseur, guandao, jian) | OPT | HAS(3) | weapon_physics.distraction() |
| 15 | half-sword | `HALFSWORD_FORM` map base->form; record `base`, `grippable` | 4 pairs (longsword, estoc, greatsword, flamberge) | OPT | HAS | weapons.py:927-935 |
| 16 | mount/ranged/shield | any weapon class beyond bladed/hafted_tip/hafted_block | — | — | NONE (no ranged, thrown, shield, mounted record or field in modules/combat) | measured: wclass counter; no shield token in combatant/weapons field set |

Owed: fields the seam does not send: weapon selection per person (`Combatant(weapon=)`) — CP-T03-03 (arms_kinds roster + typed export of WEAPONS keys + `PersonalCombatInput.kits`), unbuilt; JQ-2-gated (proposals/2026-10-23-subsystem-completion/...-03-personal-combat.md:140-157). Loadout as `hold` tenures on equipment objects — PROPOSED-ONLY, 09_the_character_sheet.md K-5.
Conflicts: weapons.py header says "53-weapon roster"; measured 54 records (50 + 4 halfsword forms). Comment `hand_guard`/`blade_guard` literals in records are stale pre-bake images (weapons.py:21-24).
Belongs elsewhere: mass-battle `TROOP_LOADOUT`/`ARSENAL`/`ARMOURY` (modules/mass_battle/equipment/__init__.py:13-36; proposals/2026-10-16-troop-stock-design.md:98-101,219-221) — mass-battle docket.

---

## 6. EQUIPMENT — ARMOUR — carrier/loader: modules/combat/core.py (tier tables) + vocabulary.py:48-60; field `Combatant.armor` combatant.py:94
Population now: 4 tiers authored as code tables {none, light, medium, heavy} -> 4 materials {none, cloth, mail, plate}; season sends none (default `light`)   Status: AUTHORED (closed set, code-owned, no per-armour-item records)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | armour tier key | enum vocabulary.ARMOUR_TIERS {none, light, medium, heavy}; every table asserted to share this key set at import | REQ | HAS (4) | vocabulary.py:46-51; combatant.py:94 |
| 2 | mapping | `TIER2MAT` tier -> material | {none:none, light:cloth, medium:mail, heavy:plate} | REQ | HAS | core.py:189 |
| 3 | resistance | `RESIST[material][mode]` | 4 materials x {percussion, puncture, shear}; floats | REQ | HAS (12 values) | core.py:185 |
| 4 | penetration | `PEN_THR[tier]` | none 0, light 0, medium 2.5, heavy 6.5 | REQ | HAS | core.py:169 |
| 5 | gap | `GAP_EXPOSURE[material]` ; `COVERAGE_GAP` | none 1.0, cloth .97, mail .95, plate .90 ; 0.15 | REQ | HAS ([SIM-CALIBRATE]) | core.py:190,208 |
| 6 | cfg per-tier | `ADEF_THRESHOLD`, `ADEF_W`, `REACH_W`, `PERC_BLUNT_TRANSMIT` | each dict keyed by 4 tiers | REQ | HAS | config.py (export `cfg`) |
| 7 | equipment health | `WoundTracker(equipment_health=)` | int, default 0 | OPT | NONE (never passed by Combatant) | combatant.py:52-58 |
| 8 | per-item armour (coverage zones, mass, quality, helmet/shield/gauntlet pieces) | — | — | — | NONE (no field exists) | measured: Combatant has only `armor` tier string |

Owed: season kit for armour — CP-T03-03 (`arms_kinds` mapping a kind to `armor`; validated against the armour tiers) unbuilt. Armour material term in armour-defeat (staff defeats plate by mass only) — PROPOSED-ONLY, 06_weapons_from_physics.md W-1.
Conflicts: none.
Belongs elsewhere: mass-battle `ARMOURY` (see ENTITY 5).

---

## 7. EQUIPMENT — SHIELD / KIT (bundle) — carrier/loader: none in modules/combat
Population now: none   Status: EMPTY
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | shield | any shield/buckler record or field | — | — | NONE (grep `shield / buckler` in modules/combat hits only comments about armour "shielding") | measured grep |
| 2 | kit | `arms_kinds` roster (kind -> one of `weapon`/`armor` field, key, `rank`) | roster in `rosters.yaml`, validated at load vs typed export of WEAPONS keys + armour tiers | PLAN | NONE (grep `arms_kinds` in engine/season/*.yaml: 0) | CP-T03-03 (…-03-personal-combat.md:140-157) |
| 3 | kit | `arms_at_build` (seeding arms into stores by holding rung kind) | map; [ASSUMPTION; medium] | PLAN | NONE | CP-T03-03 |
| 4 | kit | arms as `matter_kinds` members | open registry members | PLAN | NONE | CP-T03-03 (ROS:1423) |
| 5 | kit | `kits` field on PersonalCombatInput (tuple per party) | (weapon, armor) per party | PLAN | NONE | CP-T03-03 (iv) |
Owed: all rows above. The inventory is stated as "Jordan's content" in the workplan row CP-T03-03 (workplans/valoria_master_workplan_v10_part3.md row CP-T03-03). Withdrawn if JQ-2 option (b) ("identical fighters intended").
Conflicts: none.  Belongs elsewhere: `craft` verb as arms producer (EC).

---

## 8. TRADITION / STYLE — carrier/loader: modules/combat/traditions.py:18 (`TRADITIONS`)
Population now: 8 authored (german, italian, spanish, japanese, chinese, filipino, english, none)   Status: PARTIAL (chinese, filipino have 0 abilities; `none` is the null tradition)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | tradition key | str; abilities' `tradition` tag asserted against this dict | REQ | HAS (8) | traditions.py:18 ; ability_primitives.py:74-77 |
| 2 | label | `set` (named-set bridge mapping) | str or None: Bind Fighter, Thrust Duelist (x2), Counter-time (x2), Burst, Continuous-flow | OPT | HAS (metadata, read by nothing at resolution) | traditions.py:18-27 |
| 3 | label | `mode` (cognitive-mode label) | str or None | OPT | HAS (flavour metadata) | traditions.py:18-27 |
| 4 | familiarity | `ADJACENT` pairs | set of frozenset pairs; 7 pairs | OPT | HAS (7) | traditions.py:32-37 |
| 5 | familiarity | `FAMILIARITY_DEFAULT`, `FAMILIARITY_ADJACENT` | 0.85 , 0.93 | REQ | HAS | traditions.py:30-31 |
| 6 | kit | derived: `TRADITION_KIT[t]` = abilities tagged t | DERIVED | DERIVED | HAS | ability_primitives.py:80 |
| 7 | fighter-side | `Combatant.tradition` | key; seam default 'none' | OPT | NONE (season sends none) | combatant.py:94 |

Owed: abilities for chinese, filipino (and `none` by design). Season-side tradition assignment: no carrier — 09_the_character_sheet.md K-5 "tradition access derived from techniques a person holds" (PROPOSED-ONLY).
Conflicts: traditions.py module header (and tradition.py) still describe the retired imposition gate vs body text saying removed — PC-16 / 04_the_bout.md B-2 (stale comments).
Belongs elsewhere: none.

---

## 9. FORMATION (PC-scale) — carrier/loader: none in modules/combat
Population now: none   Status: EMPTY
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | — | any PC-scale formation record | — | — | NONE | grep modules/combat for formation: no authored carrier (measured: modules/combat/ contains no formation file) |
| 2 | shapes (mass-scale) | Line, Wedge/Arrowhead, Skirmish, Refused flank, Horseshoe, Gapped line, Column | 7 named shapes, arrangement only | PROPOSED-ONLY | NONE | proposals/pc_formation_system.md §4 (status: partially superseded; engine half built in mass battle) |
| 3 | roles/instructions | role menu by troop type; instruction vocab brace/hold/advance/charge/skirmish/refuse/lure/harass | open | PROPOSED-ONLY | NONE | pc_formation_system.md §3.5, §9 item 2 |
| 4 | open magnitudes | density primitive magnitude; MIN_DISCIPLINE gate; subunit coordination limit | open Jordan decisions | PROPOSED-ONLY | NONE | pc_formation_system.md §9 items 1,3,7 |
Owed: nothing code-called at PC scale. Conflicts: file name "pc_formation" is the P-C (compositional) system and its engine half is mass-battle (status line); treated as belonging to mass battle.
Belongs elsewhere: all rows 2-4 -> mass-battle docket.

---

## 10. COMBATANT RECORD (per-fight party) — carrier/loader: modules/combat/combatant.py:92 (`Combatant`) ; seam input engine/season/queries/inputs.py:112
Population now: season supplies `end` only   Status: PLACEHOLDER

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `label` (claimant id) | str | REQ | HAS | fight.py:49 |
| 2 | attributes | nine attribute fields | see ENTITY 2 | OPT | STUB (only `end`) | combatant.py:93-94 |
| 3 | kit | `weapon` (key of WEAPONS, default 'arming'), `armor` (tier, default 'light') | see 5, 6 | OPT | STUB | combatant.py:94 |
| 4 | style | `tradition` (default 'none'), `equipped` ([] or {name: level}), `skills` ({}) | see 1, 3, 8 | OPT | STUB | combatant.py:94 |
| 5 | derived | health_full, wound_interval, max_wounds, stamina_max, conc_max | DERIVED from attributes | DERIVED | — | combatant.py:130-143 |
| 6 | live state (engine-managed, not authored) | grip_position, lunge_depth, sel_*, range_avail, facing, stamina, conc, initiative, poise | reset per bout | DERIVED | — | combatant.py:98-130 |
| 7 | scene input | `terms` | enum DUEL_TERMS {yield, blood, death}; default 'death' (LETHAL_TERMS) | PLAN | NONE on input record | wrapper.py:508-509 ; fight.py:52 ; PC-10b / CP-T03-09 |
| 8 | scene input | `yield_decl` (Yield: by, turn 1..max_bouts, accepted, objective_contested) | object | OPT | NONE from season | wrapper.py:475-492,533-541 |
| 9 | scene input | `max_bouts` | int, default 12 | OPT | STUB(12) | wrapper.py:533 |
| 10 | seam output roster | `wound_quantities` | roster {felled, wounds, max_wounds, health_remaining, health_full} (5), ordered | REQ | HAS | engine/season/rosters.yaml:903-916 |
| 11 | seam output roster | `combat_degree_bands` | ordered severity {Felled, Wounded, Untouched} (3) | REQ | HAS | rosters.yaml:882-901 |
| 12 | seam output roster | `combat_band_edges` | Felled: {felled, above 0}; Wounded: {wounds, above 0}; swept fixture `combat_wounded_above` | REQ | HAS (2 edges) | rosters.yaml:918-946 |

Owed: PC-10b duel-terms input and a `terms` field (RS-25); CP-T03-01 cohorts never a party; CP-T03-00 both parties take their band. `kits`, `attributes` input fields: see 2, 7.
Conflicts: `combat.py` docstring says Combatant defaults "strength 4, agi 4, end 4, cog 3, att 3, spirit 3, focus 3, disp 4"; `history` default 3 omitted from that list but present in combatant.py:94 (code wins).
Belongs elsewhere: Person carrier (engine/season/state/carriers.py:694).

---

## 11. CONFIG / TUNING INPUTS — carrier/loader: modules/combat/config.py:2 (`CFG`) -> engine/engine_params/combat_engine_v1.json (`sections.cfg`)
Population now: 205 numeric keys (all authored, Class-C calibrated); 5 are 4-tier dicts   Status: AUTHORED. NO authored-content roster in this file; all are tuning families.

Families by key prefix (measured, count): INIT 12, BIND 8, PERC 8, POISE 8, REC 8, REACH 7, ADEF 6, CLOSE 6, CONC 6, LEGIB 6, LUNGE 6, DISENGAGE 5, GRAB 5, ACT 4, CHOKE 4, COMMIT 4, COUNTER 4, EXPOSE 4, INDES 4, LEVER 4, NEUTRALIZE 4, TEMPO 4, WIND 4, plus ~60 smaller prefixes (full list: tools/export_engine_params.py output).
`core` section: scalars BASE_POOL 6, POOL_FLOOR 5, TN, CUT_AUTH_REF, CUT_REF_NATIVE, DMG_SCALE, GAP_PREC_REF, HEFT_HEAVY, OW_MAX, OW_Z, PEN_DEFICIT_K, PERC_AUTH_REF(+_SOFT), PERC_TRANSMIT_FLOOR, THRUST_AUTH_REF, THRUST_LEVER_FLOOR/REF, COVERAGE_GAP; tables DELIVERY(5), GAP_EXPOSURE(4), HEAD_MODE(6), PEN_THR(4), QUAL(4), RESIST(4), TIER2MAT(4).
Combatant.py constants (not in export): WOUND_INTERVAL_BASE 4, SPI_WI_W 0.4, STR_HEALTH_W 0.25, MAXWOUNDS_DIV 2/ADD 1/CAP 3, STAMINA_PER_END 3, STAMINA_PER_SPIRIT 2 (combatant.py:17-27) — plan PC-15 moves 0.3/4.0 literals, STAMINA_COLLAPSE (-4), BEAT_BUDGET (24), RIPOSTE_CAP (0.95), contact multipliers into CFG (part4:898).
ability_primitives bounds: MAX_INVESTMENT_LEVEL 8.0, ABIL_FACTOR_FLOOR 1e-4, CEIL 1e3 (ability_primitives.py:95-97).
Owed: new keys `CLOSE_GAP_REF` re-use, `DEEP_COMMIT`, `STAMINA_COLLAPSE`, `BEAT_BUDGET`, `RIPOSTE_CAP`, `INIT_TEMPO_LEVER_K`, concentration `T_err`/`ERR_K` (PROPOSED-ONLY, weapon_physics_and_concentration_model.md §7, never built).
Conflicts: none.  Belongs elsewhere: none.

---

## 12. VOCABULARY / CLOSED TOKEN SETS (code-owned) — carrier/loader: modules/combat/vocabulary.py
Population now: HEADS 6, DAMAGE_MODES 3, ARMOUR_TIERS 4, MATERIALS 4, DEFENCE_MODES 3 (ordered, RNG-contract), HILT_TYPES 3, ADEF diagnostic labels 4, GRAB_OUTCOMES 6 (contact.py), DUEL_TERMS 3 (wrapper.py:508), TRADITIONS 8; GUARDED_TOKENS 18   Status: AUTHORED (closed; no authoring surface for Jordan except by code edit)
Members: HEADS {blunt, point, cut_thrust, straight_cut, curved_cut, cut}; DAMAGE_MODES {percussion, puncture, shear}; DEFENCE_MODES (parry, dodge, wind); GRAB_OUTCOMES (disarm, throw, pin, control, foot_pin, escape).
Called for by: vocabulary.py:30-107; contact.py (GRAB_OUTCOMES). Owed: none. Conflicts: none.

---

## 13. ENVIRONMENT / GEOMETRY INPUTS — carrier/loader: none
Population now: none authored   Status: EMPTY
Measured: grep `terrain|footing|weather|slope` in modules/combat returns no file; no arena, ring, lighting or surface parameter. Geometric inputs that exist are per-weapon (ENTITY 5 `geometry`) and engine-derived per beat (`measure_gap`, `range_avail`, `facing`, `grip_position`, `lunge_depth`; wrapper.py:142 etc.) — DERIVED, not authored. `OOB` cfg=2 (stamina-out penalty, config.py:114) is tuning. Duel-mode intents per beat (six open moments) and grid-mode engagement cadence — PROPOSED-ONLY: proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md M-2, M-5.
Owed: none code-called. Belongs elsewhere: map geometry `systems/settlements/valoria_geography_v30.yaml` (other docket).

---

## 14. WOUND / BODY INPUTS — carrier/loader: modules/combat/combatant.py:50 (`WoundTracker`) ; seam engine/season/seam/wrappers/combat.py:130
Population now: 1 derived input (`end` = max(1, 4 - body_band_penalty)) ; body bands from `rosters.yaml band_floors`   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | body | `Person.body` int on condition scale -> `body_band_penalty` (count of `band_floors["body"]` floors fallen below) | int; floors in rosters.yaml | REQ (seam) | HAS | seam/wrappers/combat.py:130-138; decision `body_band_penalty` |
| 2 | derivation | `default_end` literal 4 (floor 1) inside `party_end` | int | REQ | HAS (literal in code) | combat.py:135-138 |
| 3 | tracker | WoundTracker derivation: WI = round(end + 4 + 0.4*spirit); MaxWounds = min(end//2 + 1, 3); Health = WI*(MW+1) + 0.25*str*end | constants in combatant.py:17-27 | DERIVED | HAS | combatant.py:30-48 |
| 4 | persistence | wound state persisting between engagements / on Person (count + interval) | decision: Person field vs re-derive from body bands | PROPOSED-ONLY | NONE | 05_two_modes_of_one_bout.md M-3 |
| 5 | harm | `wound_harm_models` (how much body a wound costs) | roster | REQ | HAS (rosters.yaml:948) | rosters.yaml:948-969 (read, not verified further) |
| 6 | body ceiling / marks | `body_ceiling` Person field + marks (CP-T03-07); `tend` verb (CP-T03-08) | PLAN | PLAN | NONE | CP-T03-07, CP-T03-08 (…-03-personal-combat.md:201-234) |
Owed: rows 4, 6. Conflicts: combatant.py header comments cite `derived_stats_v30` (a design doc) as canonical for WI/MaxWounds; the code is the formula (§0.05).
Belongs elsewhere: `Person.body` carrier (person docket).

---

## Parameter-row count
Entity 1: 10, 2: 10, 3: 6, 4: 4, 5: 16, 6: 8, 7: 5, 8: 7, 9: 4, 10: 12, 11: 0 (families named, no authored rows), 12: 0 (member lists), 13: 0, 14: 6 -> 88 rows.

---

## 15. ACTIONS / CHOICES TABLE (the combat module's own; complete over `modules/combat/` entry points and in-bout decision sites)
Carrier: modules/combat/wrapper.py (`engagement`:47, `fight`:533), fight.py:32, contact.py, combat_systems.py. Measured by reading `wrapper.py` decision sites and `grep ^def` over wrapper/combat_systems/contact/core/fight/combatant/ability_primitives/traditions. Population: 0 player-selectable options in the module today. Every in-bout choice below is made by the ENGINE (sigma/probability, seeded rng); the only externally supplied choices are the scene-level inputs in A1-A5. Duel-mode player intents (six open moments) are PROPOSED-ONLY (05_two_modes_of_one_bout.md §2, M-5): not built.
Status: AUTHORED (engine-chosen) / PLAN (player-chosen)

### 15a. Scene-level entry points and externally supplied choices
| id | name | who chooses | inputs / arguments | preconditions | outputs returned | path:line |
|---|---|---|---|---|---|---|
| A1 | module entry `fight(inp, rng)` | host (season seam) | `PersonalCombatInput`(claimants, ends, wound_quantities); optional `terms` via getattr; `rng` | pc_engine loadable | dict(status, result, trace, ends, wound_state) | fight.py:32-74 |
| A2 | engine `fight(A,B,cfg,rng,max_bouts,yield_decl,terms)` | caller | two Combatants; cfg (default CFG); `max_bouts` int default 12; `yield_decl`: Yield; `terms` in DUEL_TERMS | `terms` in {yield,blood,death} else ValueError; Yield.by is A or B (identity); 1<=Yield.turn<=max_bouts | int +1 / -1 / 0 (0 = UNRESOLVED, ruled); 95% UPSET_FLOOR flip applied to decided results | wrapper.py:533-594 |
| A3 | `terms` choice: death / blood / yield | caller (agreed before scene) | enum DUEL_TERMS; default 'death' (LETHAL_TERMS) | `blood` stops at wt.wounds>=1; `yield` stops at health_remaining <= YIELD_HEALTH_FRAC*health_full | stop emits `yield` event w/ terms; tie -> UNRESOLVED | wrapper.py:508-531,570-582 |
| A4 | declare Yield | caller (yielder), opponent decides acceptance | Yield(by, turn, accepted, objective_contested) | refused if `objective_contested`; accepted -> fight ends; not accepted -> yielder unresisting, disposition is caller's | `yield` event (accepted, refused) | wrapper.py:475-492,556 |
| A5 | `max_bouts` | caller | int | Yield.turn must lie within | bound on turns | wrapper.py:533 |
| A6 | engagement entry `engagement(A,B,first,cfg,rng,prev_closed,terms)` | caller (grid cadence) / fight loop | `first` = initiating Combatant | — | (felled loser or None, closed state) | wrapper.py:47-473 |
| A7 | engine loader `pc_engine.load()` | host | none | engine tree present; raises otherwise | PCEngine(wrapper, combatant) | engine/substrate/pc_engine.py:41 |
| A8 | host input builder / adapter | host | `combat_input(w, claimants)`; `resolve(...)` | two claimants, both persons else PARTY-GAP; `entry_for` found else refusal | dict(status, result, winner, wound_state, unresolved, surrender, bouts, trace, parties, seed) | seam/wrappers/combat.py:141,180-257 |
| A9 | `party_end(person, fx)` | host | person body | — | end = max(1, 4 - body_band_penalty) | seam/wrappers/combat.py:130-138 |
| A10 | `surrender_of(trace)` | host | trace list | yield event with refused None | dict(by, turn, accepted) or None | seam/wrappers/combat.py:116-127 |

### 15b. In-bout choices and actions (engine-chosen; in order of the beat)
| id | name | who chooses | choice inputs / arguments | preconditions | outputs | path:line |
|---|---|---|---|---|---|---|
| B1 | who acts first each turn | engine (initiative) | `first` Combatant | — | `turn_start` | wrapper.py:564 |
| B2 | grip (gather in / full reach) | engine | `grip_target(c, closed, cfg)` | pole-class weapon closing (can_choke) | grip_position in [0,1] | wrapper.py:141; combat_systems.py:287,291 |
| B3 | facing | engine | `facing_target(c, closed, cfg)` | — | facing state | wrapper.py:143; combat_systems.py:414 |
| B4 | use-mode / head selection | engine | `select_mode(c, defender_armor, closed, cfg, measure_gap, grip, room)` over `afforded_heads(w, grip, room)` / `element_afforded` | weapon affords >1 head only for mode_elements weapons | sel_dmg, sel_head, sel_gap, sel_perc, sel_pc, sel_eff | wrapper.py:146,257; combat_systems.py:545,627,667 |
| B5 | half-sword switch | engine | `halfsword_target(c, closed, opp_armor)`; `affords_halfsword(w)` | weapon in HALFSWORD_FORM and grippable | weapon key swapped (wrapper owns mutation) | wrapper.py:250-251; combat_systems.py:864,880; weapons.py:927 |
| B6 | approach / close measure | engine | `close_rate`, `approach_displace`, `approach_step`, `reach_threat`, `represent_measure_p` | measure open | `approach` event | wrapper.py:93,235; combat_systems.py:759,782,950,1368,1409 |
| B7 | stop-hit by longer weapon | engine (probability) | `stophit_sigma`, STOPHIT_CHANCE | gap > 0 | `stophit` event, possible wound | wrapper.py:216-227; combat_systems.py:1298 |
| B8 | pursuit of a withdrawal | engine | `pursuit_sigma` | after failed disengage | `disengage` (ok False, pursued) | wrapper.py:189-196; combat_systems.py:1345 |
| B9 | reach re-open (created moment) | engine | `reopen_prob`, `reach_threat` | closed, beats>1, reopen_moment, base_gap>0.3 | measure re-opened | wrapper.py:165; combat_systems.py:961 |
| B10 | proactive disengage / withdrawal | engine | `disengage_attempt_p`, `disengage_clean_p` | closed, beats>1, base_gap>0.3, longer out-leveraged | `disengage` ok True/False | wrapper.py:183-196; combat_systems.py:973,994 |
| B11 | who attacks (aggressor) | engine (ready/tempo; rng on tie) | `weapon_tempo`, `close_tempo`, `tempo_pressure`, ACT_THRESHOLD | open: higher ready; closed: actors[0] | aggressor/defender roles | wrapper.py:238-245; combat_systems.py:89,147,1311 |
| B12 | commit depth | engine (Beta draw) | `commit_depth(aggressor, defender, cfg, rng, TR)` | — | commit value; `commit` event | wrapper.py:265; combat_systems.py:1106 |
| B13 | lunge | engine | `lunge_quality`; LUNGE_COMMIT | commit >= LUNGE_COMMIT | lunge_depth set | wrapper.py:267; combat_systems.py:309 |
| B14 | read contest | engine | `read_contest(...)` using `reading`, `legibility`, `consistency`, `mental_fatigue`, `familiarity` | — | read_win, read_d, read_a; `read` event | wrapper.py:291; combat_systems.py:1123,171,915,1423,1427; traditions.py:47 |
| B15 | defence mode: parry / dodge / wind | engine (chosen by read win, else random) | `mode_sigma(mode, ...)` per mode in DEFENCE_MODES | missed read -> `modes[rng.randrange(3)]` (order is RNG contract) | mode, msig; `mode` event | wrapper.py:295; combat_systems.py:329; vocabulary.py:DEFENCE_MODES |
| B16 | indes steal / counter attempt | engine | `indes_steal_amount`, `counter_select` | read_win and commit >= 4 | initiative transfer; counter_attempt flag | wrapper.py:307-312; combat_systems.py:1139,1146 |
| B17 | attack roll / resolution | engine | pool = max(5, History+6); `assemble_net_sigma(...)`; `core.resolve(pool, net_sigma, rng, ob)` | — | degree in {fail, partial, success, overwhelming}; `roll` event | wrapper.py:313-316; core.py:54,118 |
| B18 | overcommit loss | engine | `overcommit_exposure`, `init_overcommit_loss` | exposure > 0 | initiative/poise loss | wrapper.py:322-326; combat_systems.py:1151,1189 |
| B19 | outcome: hit / bind / riposte / neutralize | engine | NEUTRALIZE_PARRY/DODGE/WIND, WIND_BIND_P, RIPOSTE_ON_FAIL, RIPOSTE_ON_NEUTRALIZE, `counter_success_prob` | per degree | hit damage via `core.strike`; bind; riposte | wrapper.py:329-380; core.py:621; combat_systems.py:1438 |
| B20 | strike damage | engine | `core.strike(attacker, defender, deg, cfg, net, pool)` -> `damage`, `coupling`, `adef_cap` | hit landed | damage int applied to WoundTracker | core.py:573,621,436 |
| B21 | bind exchange (dominance, kuzushi, steal) | engine | `bind_sigma`, `bind_dominance_p` | bind True | bind winner; poise/initiative shifts | wrapper.py:403-425; combat_systems.py:1047,1445 |
| B22 | percussion stagger | engine | `percussion_stagger(striker, victim, wound, deg, cfg)` | blunt/percussive hit | poise/wind effect | wrapper.py:227,400,421,432; combat_systems.py:1206 |
| B23 | contact: grab attempt gate | engine | `grab_available(actor, opponent, opening_created, cfg)`; `_short_reach_exempt` | dagger-class (head_len <= GRAB_SHORT_REACH_M) or a real opening this beat | bool | contact.py:19,29; wrapper.py:443 |
| B24 | grapple branch: disarm / throw / pin / control / foot_pin / escape | engine | `grab_sigma`, `grab_outcome(gsig, rng, cfg)` | gate B23 | token from GRAB_OUTCOMES; `contact` event | contact.py:41,57; wrapper.py:445-457 |
| B25 | opening created / reopen / push | engine | opening_created, reopen_moment, push_avail flags | deep-commit, defensive win by longer weapon, 2H freed hand | flags for next beat | wrapper.py:380-395 |
| B26 | burst continuation or separation | engine | BURST_MAX, stamina <= -4, clean defence | — | `separation` reason in {terms, collapse, burst_ceiling, clean_defence, beat_exhaustion} | wrapper.py:125,238,470-473 |
| B27 | between-turn recovery | engine | RECOVERY_FRAC, CONC_DRAIN_BOUT, CONC_RECOVER_FRAC | — | stamina, conc updated | wrapper.py:583-585 |

### 15c. Fighter-build selections (made once, before the scene; consumed by the choices above)
| id | name | who chooses | arguments | preconditions | outputs | path:line |
|---|---|---|---|---|---|---|
| C1 | choose weapon | build/host (season: none yet) | key in WEAPONS | key must exist | `Combatant.weapon` | combatant.py:94,100 |
| C2 | choose armour tier | build/host (season: none yet) | ARMOUR_TIERS | KeyError in tier tables otherwise | `Combatant.armor` | combatant.py:94; vocabulary.py:46 |
| C3 | choose tradition | build (season: none yet) | key in TRADITIONS | — | `Combatant.tradition`; gates kit access | combatant.py:94; ability_primitives.py:100-123 |
| C4 | invest in techniques | build | `equipped` list or {name: level 0..8} | technique in `kit(known_traditions)` else inert | factor/bonus per lever via `ability_factor`, `ability_bonus`, `eff_cw` | ability_primitives.py:100,129,140,154 |
| C5 | skills | build | dict axis -> float | — | `Combatant.skill(axis)` | combatant.py:115,156 |
| C6 | attributes | build | nine fields | — | WoundTracker via `max_wounds`, `wound_interval`, `health_full`, `stamina_max`, `derive_stats` | combatant.py:30-48,144 |
| C7 | tradition read edge | derived | `familiarity(reader, opponent)` | 1.0 if same or either 'none' | 0.85 / 0.93 / 1.0 | traditions.py:47 |

Owed: player-selectable duel-mode intents at six open moments (measure, reopen, commit, mode, counter, contact) and engine-resolved closed moments (read, bind entry, burst length) — PROPOSED-ONLY 05_two_modes_of_one_bout.md §2 (not built); engagement-cadence seam entry (M-2). No `feint`, `seize` (lever dead) or separate maneuver exists in code (wrapper.py comment "FEINT DISSOLVED INTO THE ATTACK").
Conflicts: none.
Belongs elsewhere: season verbs `fight`, `accept`, `capture`, `yield` wiring (other agent).

Parameter-row count addendum: ENTITY 15 adds 10 + 27 + 7 = 44 action rows (total 132 rows).

---

## 16. RETIRED-KEY RE-CHECK (orchestrator correction, ED-IN-0232)
Method: grep (case-insensitive) `keystore|keys.py|import keys|echo|consume|emit_key|params_tables|holonic` over modules/combat/*.py and engine/season/seam/wrappers/combat.py; grep `key` over wrapper.py; grep `params_tables|KeyStore|keys` over the cited proposals.
Result: NO row in this file has a Key-substrate-only source. Rows marked RETIRED-KEY: none.
- `wrapper.py` `_emit()`/`_TRACE` (wrapper.py:16-19) is the scene-trace hook (a callable set by `fight.py`), not the retired emit/consume interface; B-rows citing `_emit` events stand.
- `combatant.py:12` mentions "holonic doctrine §3" in a comment only; no Key use. `combatant.py:117` "CONSUME" is a comment about derived figures.
- "key" in wrapper.py hits are Python `key=` / "keyed on" prose, not Key substrate.
- Proposal "capability keys" (09 K-4, CP-T03-04 `capability["arms"]`, `technique:indes`) are Person.capability dict keys, a live carrier, not the retired Key substrate.
- `combat_engine_v1.json` is a typed export behind `tools/export_engine_params.py`, live; `params_tables.yaml` is not cited anywhere in this file as a source.
- Stale-source notes (not Key): rows citing design docs for intent (combatant.py comments naming `derived_stats_v30`) are reference only; the code constants are the current source (see ENTITY 14 Conflicts).
