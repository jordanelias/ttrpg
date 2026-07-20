# Quantity Census — Attribute/Value Coherence Audit

Anchor: **ED-IN-0029** · Generated: 2026-07-08 · Evidence artifact of the census-merge stage — not a registry.

This is the merged, cross-family quantity census: one row per CONCEPT, aliases collapsed per descriptor_registry where an alias is declared, otherwise kept as separate cross-linked rows (a synonym finding in itself). Every formula variant is recorded with its surface — none are silently adjudicated. See `quantity_census.yaml` for the machine-readable form and the six `../01_workings/finder_F-*.json` files for raw per-family sweep evidence.

## C1 — Attributes / Aliases / Aggregates  (14 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Acuity<br><sub>aka: Reasoning; Cognition</sub> | attribute_scalar | references/descriptor_registry.yaml:39 | `raw attribute, scale 1-7 (registry primary: Acuity)` — references/descriptor_registry.yaml:39<br>`raw attribute, scale 1-7 (glossary primary: Cognition, no Acuity mention)` — references/glossary.md:37 | warn | attr.mind.acuity | **DRIFTED** |
| Agility<br><sub>aka: Dexterity</sub> | attribute_scalar | references/descriptor_registry.yaml:36 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:36 | warn | attr.body.agility | **ORPHANED** |
| Attunement<br><sub>aka: Perception</sub> | attribute_scalar | references/descriptor_registry.yaml:42 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:42 | warn | attr.social.attunement | **COHERENT** |
| Body (aggregate) | attribute_aggregate | references/descriptor_registry.yaml:49 | `sum(Strength, Endurance, Agility)` — references/descriptor_registry.yaml:49 | warn | agg.body | **ORPHANED** |
| Bonds<br><sub>aka: Sincerity; Affability</sub> | attribute_scalar | references/descriptor_registry.yaml:44 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:44 | warn | attr.social.bonds | **DRIFTED** |
| Charisma<br><sub>aka: Influence (attribute alias, distinct from fac.influence); Presence</sub> | attribute_scalar | references/descriptor_registry.yaml:43 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:43 | warn | attr.social.charisma | **COHERENT** |
| Endurance<br><sub>aka: Vitality</sub> | attribute_scalar | references/descriptor_registry.yaml:35 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:35 | warn | attr.body.endurance | **COHERENT** |
| Focus | attribute_scalar | references/descriptor_registry.yaml:38 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:38 | warn | attr.mind.focus | **COHERENT** |
| Mind (aggregate) | attribute_aggregate | references/descriptor_registry.yaml:50 | `sum(Focus, Acuity, Will)` — references/descriptor_registry.yaml:50 | warn | agg.mind | **ORPHANED** |
| Resonant Style | practitioner_stat | AMBIGUOUS:designs/npcs/npc_behavior_v30.md:32-34 vs references/module_contracts.yaml:231 (gate-only mention) | `enum determined by NPC Conviction taxonomy (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Community/Warden)` — designs/personal/conviction_track_v1.md:10-14 | unregistered | piety_track gate g_scar2 ('Resonant Style X exposed') | **AMBIGUOUS** |
| Social (aggregate) | attribute_aggregate | references/descriptor_registry.yaml:51 | `sum(Attunement, Charisma, Bonds)` — references/descriptor_registry.yaml:51 | warn | agg.social | **ORPHANED** |
| Strength | attribute_scalar | references/descriptor_registry.yaml:34 | `raw attribute, scale 1-7` — references/descriptor_registry.yaml:34 | warn | attr.body.strength | **COHERENT** |
| Thread Sensitivity (TS) | practitioner_stat | references/glossary.md:60 | `raw practitioner stat, scale 0-100+; TS>=30 gates Knot formation` — references/glossary.md:60; params/core.md:149 | unregistered | — | **UNREGISTERED-LOAD-BEARING** |
| Will<br><sub>aka: Spirit</sub> | attribute_scalar | AMBIGUOUS:references/descriptor_registry.yaml:40 (primary=Will) vs references/glossary.md:40 (primary=Spirit) | `raw attribute, scale 1-7 (registry primary: Will)` — references/descriptor_registry.yaml:40<br>`raw attribute, scale 1-7 (glossary primary: Spirit; used as 'Spirit' in every live formula seen)` — references/glossary.md:40; config.py:61 CONC_SPIRIT; params/core.md:247 | warn | attr.mind.will | **AMBIGUOUS** |

## C2 — Derived Values  (20 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Army Morale | derived_value | designs/scene/derived_stats_v30.md:396-407 (§10.2) | `floor(average unit Morale) + Command modifier(+-1) + Discipline modifier(+-1); thresholds 6+ Resolute...0 Routed` — designs/scene/derived_stats_v30.md:396-407; designs/provincial/mass_battle_v30.md:867-869 | unregistered | — | **COHERENT** |
| Certainty | derived_value | values_master.yaml:1178 / params/core.md:161 | `5 (starting, varies by background), range 0-5, cosmological worldview track` — values_master.yaml:1178; params/core.md:161 | not_descriptors | — | **COHERENT** |
| Command (mass combat rating) | derived_value | params/mass_combat.md:139,361-363,369 (ED-899) | `clamp(round((2*Charisma+Cognition)/3), 1, 7) — Charisma-primary, supersedes PP-232's equal-weight ceil((Cha+Cog)/2)` — params/mass_combat.md:139,361-363,369; designs/provincial/mass_battle_v30.md:266 | unregistered | — | **COHERENT** |
| Composure / Face<br><sub>aka: Composure (retained in combat/knots/conviction); Face (social-contest-scoped rename)</sub> | derived_value | designs/scene/social_contest_v30.md:229-258,481-512 (CR3, ED-1056, 2026-06-01) | `Composure (buffer magnitude) = Charisma*3, range 3-21` — designs/scene/derived_stats_v30.md:128-161; params/contest.md:137<br>`Face_max = Charisma*3; Face_current = round(Standing/10 * Face_max)` — designs/scene/social_contest_v30.md:481-512; params/contest.md:143-151 | not_descriptors | sim/personal/contest/primitives.py FaceScale<br>sim/personal/contest/resolver.py | **COHERENT** |
| Concentration | derived_value | AMBIGUOUS: config.py:61/combatant.py:141 (3*Focus+2*Spirit, matches most citations) vs F-SIM-01's specific citation of params/core.md:162 as 'Charisma*3' | `3*Focus + 2*Spirit (Jordan 2026-06-03), range 5-35, depletes 5/exchange (ED-890/DEP)` — designs/scene/combat_engine_v1/config.py:61 (CONC_FOCUS=3.0, CONC_SPIRIT=2.0); combatant.py:141; params/contest.md:140; params/contest_extensions.md:11-14 (PP-NEW-D); designs/scene/derived_stats_v30.md:128-161<br>`'Concentration = Charisma*3' asserted as a params/core.md:162 citation` — params/core.md:162 (as cited by F-SIM-01) | not_descriptors | stat_deltas payload (no registry key backing it, see divergences) | **AMBIGUOUS** |
| cumulative_drift | practitioner_stat | AMBIGUOUS: gate-only, no owning declaration | `gate trigger only: cumulative_drift > 0.5 -> scene.gossip emitted; no calculation rule stated` — references/module_contracts.yaml:169-173 | unregistered | npc_behavior gate g_drift | **UNREGISTERED-LOAD-BEARING** |
| Damage Resistance / Reduction<br><sub>aka: Damage Resistance (DR, registered name); Damage Reduction (used in combat_v30.md)</sub> | derived_value | AMBIGUOUS: registered as Resistance, used as Reduction | `registered term: 'Resistance'` — references/name_collision_database.yaml:463 (term_drift)<br>`used term: 'Damage Reduction'` — designs/scene/combat_v30.md:266 | warn | — | **DRIFTED** |
| Faction Legitimacy (derived meter) | derived_value | designs/scene/derived_stats_v30.md:297,325-336,544,554 (§8, §14.1 + footnote) | `Legitimacy(derived) = Mandate * 20, range 0-140` — designs/scene/derived_stats_v30.md:297,554 | not_descriptors | — | **DRIFTED** |
| Health | derived_value | designs/scene/derived_stats_v30.md:55-90 (§4.1, AUTHORITATIVE) | `Health(full) = round(WI*(MW+1) + 0.25*Strength*Endurance); WI=round(Endurance+4+0.4*Spirit); MW=min(floor(Endurance/2)+1,3). Felled at cumulative damage>=Health (D-A, ED-1021)` — designs/scene/derived_stats_v30.md:55-90<br>`implemented formula matches` — designs/scene/combat_engine_v1/combatant.py:40-42<br>`contract formula matches, but references Endurance/Spirit/Strength which are NOT declared personal_combat state entries` — references/module_contracts.yaml:819,826-829 | not_descriptors | scene.combat_hit stat_deltas route to cumulative_damage substrate (F1 rule) | **UNREGISTERED-LOAD-BEARING** |
| Inspiration | derived_value | designs/scene/derived_stats_v30.md:164-221 (§5.3) | `Total Inspiration per focus <= Spirit (Resolve cap); +1D genuine pursuit, Ob-1 strategic spend` — designs/scene/derived_stats_v30.md:164-221 | unregistered | — | **COHERENT** |
| Local Economy / Garrison Strength / Public Order | derived_value | designs/territory/settlement_layer_v30.md:43-59 / references/module_contracts.yaml:558,586-597 | `Local Economy=Prosperity*50; Garrison Strength=Defense*20+Fort*30; Public Order=Order*20 (riots below 0)` — references/module_contracts.yaml:586-597; designs/scene/derived_stats_v30.md:372-382 | not_descriptors | — | **DRIFTED** |
| Max Wounds (MW) | derived_value | designs/scene/derived_stats_v30.md:55-90 (§4.1, formula only) | `MW = min(floor(Endurance/2)+1, 3) — PP-717 cap` — designs/scene/combat_engine_v1/combatant.py:30-32<br>`same formula, comment-only in contract` — references/module_contracts.yaml:821,828 | unregistered | — | **UNREGISTERED-LOAD-BEARING** |
| Province Accord | derived_value | designs/territory/settlement_layer_v30.md:61 | `floor(mean settlement Order across province settlements); e.g. floor((4+2+1)/3)=2` — designs/territory/settlement_layer_v30.md:61 | unregistered | — | **COHERENT** |
| Resolve | derived_value | params/core.md:1206 / values_master.yaml:1206 | `Resolve = Spirit, range 1-7` — values_master.yaml:1206; params/core.md:1206 | not_descriptors | — | **COHERENT** |
| Stamina | derived_value | designs/scene/derived_stats_v30.md:96-122 (§4.2, RATIFIED S1 2026-05-29) | `CURRENT: (3*Endurance)+(2*Spirit), range 5-47; recovery 'Take a Breath' = (Endurance+relevant History)*2, capped` — designs/scene/derived_stats_v30.md:96-122,538<br>`OLD: Endurance*5, range 5-35 (ED-694); recovery = Endurance score` — designs/scene/combat_v30.md:302-303,98<br>`values_master.yaml carries the OLD formula` — values_master.yaml:1122<br>`implemented as (3*Endurance)+(2*Spirit) — matches CURRENT` — designs/scene/combat_engine_v1/combatant.py:45-47 | not_descriptors | — | **DRIFTED** |
| Thread Fatigue | derived_value | designs/scene/derived_stats_v30.md:227-260 (§6.1) | `Threshold = Spirit*5, range 5-35; per-op costs: Leap 3, Passive sensing 2, Mending 4, Pulling 5, Locking 7, Dissolution 10` — designs/scene/derived_stats_v30.md:227-260,541<br>`same formula` — values_master.yaml:1164; params/core.md:161 | not_descriptors | — | **COHERENT** |
| Thread Pool Score (TPS) | derived_value | params/threadwork.md:13 | `TPS = Thread Sensitivity / 10 (round down)` — params/threadwork.md:13; references/glossary.md:61; params/threadwork_superseded.md:22 (identical, correctly-retained historical copy) | unregistered | — | **UNREGISTERED-LOAD-BEARING** |
| Treasury / Reputation / Discipline / Levies Available | derived_value | designs/scene/derived_stats_v30.md:298-360 (§8) | `Treasury=Wealth*100; Reputation=Influence*15; Discipline=Stability*10; Levies Available=Military*2 (ceiling)` — designs/scene/derived_stats_v30.md:298-360,545-548 | not_descriptors | — | **COHERENT** |
| TroopCount / Size / block_size | unit_stat | designs/scene/derived_stats_v30.md:265-289 (§7) | `TroopCount=Size*block_size (set at muster); Size=floor(TroopCount/block_size); block_size by scale: Skirmish 10, Company 100, Battle 500, Campaign 1000, War 5000; effective_damage=floor(successes*(1+Power)*TroopCount/max_TroopCount), capped 1.0` — designs/scene/derived_stats_v30.md:265-289,543; designs/provincial/mass_battle_v30.md:68-91,138-140<br>`BLOCK_SIZE=100 (Company scale) implemented` — sim/provincial/massbattle.py | unregistered | — | **COHERENT** |
| Wound Interval (WI)<br><sub>aka: Wound Index</sub> | derived_value | AMBIGUOUS: no owning module — intermediate calculation only | `WI = round(Endurance + 4 + 0.4*Spirit)` — designs/scene/combat_engine_v1/combatant.py:35-37; references/module_contracts.yaml:819-820 (comment only) | unregistered | — | **UNREGISTERED-LOAD-BEARING** |

## C3 — Pools  (8 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Argue Pool | pool | designs/scene/social_contest_v30.md (home doc) | `restated 3x in home doc: '(Primary Attribute*2) + History bonus' (History bonus=points+3), OMITTING the up-to-+2D style/audience bonus dice the same doc says are added at Step 3` — designs/scene/social_contest_v30.md:119,135,164,490 vs :78<br>`complete form: (Primary*2) + History + 3 + style` — designs/scene/derived_stats_v30.md:585 | not_descriptors | — | **DRIFTED** |
| Combat Pool | derived_value | params/core.md:161 (ratified 2026-05-29 R1, ED-901; re-ratified ED-900/904) | `CANONICAL: max(5, Relevant History + 6), Agility-independent` — params/core.md:161<br>`STRUCK: (Agility*2) + History + 3, filed under nonexistent params/combat.md` — values_master.yaml:212<br>`STRUCK (duplicate stale entry)` — values_master.yaml:1150<br>`stale header comment still citing PP-247 struck form` — params/core.md:4<br>`canonical form implemented` — designs/scene/combat_engine_v1/combatant.py:117; references/module_contracts.yaml:810; combat_config.gd | not_descriptors | module_contracts.yaml:810 (resolver: d_sigma, pool=max(5,History+6)) | **DRIFTED** |
| Faction Domain Pool | pool | designs/scene/derived_stats_v30.md:590 (§14.4) | `bare faction stat, 1-7D` — designs/scene/derived_stats_v30.md:590 | not_descriptors | — | **COHERENT** |
| Fieldwork Pool | pool | params/fieldwork.md:6-15 | `(Primary Attribute*2) + History bonus (points+3); min 5D, max 24D` — params/fieldwork.md:6-15; params/core.md:252; designs/scene/fieldwork_v30.md:217; designs/scene/derived_stats_v30.md:587 | not_descriptors | — | **COHERENT** |
| Knot Pool | pool | mechanics_index.yaml:350 | `(Bonds*2) + 3, range 5-17D; tiers: distant -2..+5, close -5..+5` — mechanics_index.yaml:350; designs/scene/derived_stats_v30.md:588 | not_descriptors | — | **UNREGISTERED-LOAD-BEARING** |
| Mass Combat Pool (Board Game mode) | pool | designs/provincial/mass_battle_v30.md:755 (B.3) | `sum of all engaged unit Martial values + commander bonus` — designs/provincial/mass_battle_v30.md:755 | unregistered | — | **COHERENT** |
| Mass Combat Pool (personal/TTRPG-scale unit) | pool | params/mass_combat.md:62 (self-disclosed: ED-899/ED-1013 live engine is canonical, PP-233 is legacy) | `LEGACY/PP-233 (headline restated in 2 design docs): min(Size,Command) + Command` — params/mass_combat.md:60-76; designs/provincial/mass_battle_v30.md:28,443; designs/scene/derived_stats_v30.md:589<br>`LIVE ENGINE (ED-899/ED-1013): base=2*Command at full strength, smoothly -> Command at annihilation via cohesion=Size/maxSize; Command*(1+cohesion)` — params/mass_combat.md:62; tests/sim/mass_battle/config.py | unregistered | — | **DRIFTED** |
| Thread Pool | pool | designs/threadwork/threadwork_v30.md (restated ~7x, PP-619/624/625/616) | `(Spirit*2) + History bonus (points+3) + Thread Pool Score (TPS)` — designs/threadwork/threadwork_v30.md:19,155,266,317,350,374,455; designs/scene/derived_stats_v30.md:586 | not_descriptors | — | **COHERENT** |

## C4 — Tracks + Clocks  (13 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Church Influence (CI)<br><sub>aka: Crown Index (alleged collision, name_collision_database.yaml:459, unresolved); Theocracy Counter (TC, deprecated ED-782); Thread Consciousness (CI) — apparent mis-citation, victory.md Löwenritter row</sub> | faction_stat | AMBIGUOUS:params/bg/core.md:82 / params/bg/ci_seizure.md:119-120 / params/bg/parliament.md:52-53 (BG start=28, triangulated) vs params/factions_personal.md (TTRPG start=0) vs params/campaign_modes.md:46 (TTRPG start=15, unsupported anywhere else) | `0-100 clock; BG start=28 (P-32, corrects PP-188's 22)` — params/bg/core.md:82; params/bg/ci_seizure.md:119-120; params/bg/parliament.md:52-53<br>`TTRPG start=0` — params/factions_personal.md Clock Starting Values<br>`'TTRPG Session Zero' start=15, cites params_core.md/params_factions_ttrpg.md as source (neither supports 15)` — params/campaign_modes.md:46<br>`0-100 territorial clock, writable by territorial_piety, read-only by ci_political` — references/module_contracts.yaml:255,644 | not_descriptors | territorial_piety emits, ci_political reads | **DRIFTED** |
| Coherence (cross-scale) | track | AMBIGUOUS-BY-DESIGN (three intentional scales — see divergences) | `Personal: 10 (start) counting down to 0; at 0, character becomes NPC (PP-261)` — values_master.yaml:1192; params/core.md:161; references/glossary.md:49<br>`Personal: 0-10 (or 10->0), a 'permanent degradation track', explicitly NOT a derived value; Mending costs 0 Coherence (asymmetry)` — designs/scene/derived_stats_v30.md:261,563; designs/threadwork/threadwork_v30.md:56,92,133,283-284,344,395,429,446,481<br>`Cosmological: 4 TS-gated bands — Stirring 30-49, Attuned 50-69, Sensitive 70-89, Resonant 90-100` — references/mechanical_terms_index.md:368 | not_descriptors | stat_deltas (type:coherence) | **COHERENT** |
| Disposition | track | designs/scene/derived_stats_v30.md:388-394 (§10.1, ED-912) | `flat -5..+5, per NPC; decoupled from Bonds-as-ceiling (ED-912, supersedes PP-684 'ceiling=Bonds')` — designs/scene/derived_stats_v30.md:388-394,560<br>`same -5..+5 flat range, cross-references ED-912 explicitly` — params/core.md:147; params/fieldwork.md:123-153 | not_descriptors | — | **COHERENT** |
| Evidence (Track) | clock | designs/scene/fieldwork_v30.md:254-272 (§4.1) | `0 to per-investigation threshold; persistent across scenes/sessions, one per investigation regardless of territory` — designs/scene/fieldwork_v30.md:254-272 | not_descriptors | — | **DRIFTED** |
| Institutional Pressure / Invasion Pressure (IP)<br><sub>aka: Invasion Pressure; Imperial Pressure (alleged collision, unresolved)</sub> | clock | AMBIGUOUS:params/bg/core.md:83 ('Invasion Pressure') vs params/factions_personal.md/campaign_modes.md/mass_combat.md ('Institutional Pressure') — same value/thresholds, different full name | `0-100 clock, start 20, IP>=75 Altonian Vanguard deployment` — params/bg/core.md:83; params/bg/clocks.md:33; params/bg/geography.md:19; params/bg/victory.md:10,85<br>`same value/thresholds under 'Institutional Pressure' name` — params/factions_personal.md; params/campaign_modes.md:47; params/mass_combat.md:382<br>`0-100 clock [PROVISIONAL ED-793 start value]` — references/module_contracts.yaml:516 | not_descriptors | victory gates g_ip100/g_ip85/g_ip80/g_ipfall (module_contracts.yaml:521-536) | **DRIFTED** |
| Mending Stability (MS)<br><sub>aka: Rendering Stability (RS, historical name pre-ED-731); RS (bare abbreviation, still used undefined in several live files)</sub> | clock | params/core.md:95-101 (MS; ED-731 rename) | `0-100, floor 0 (Rupture), ceiling 100; TTRPG start=60, BG start=72; decay -1/in-game-year baseline (PP-255)` — params/core.md:95-101<br>`historical definition under prior name: 'Rendering Stability (RS) \| 100->0 \| World coherence (shared track)'` — params/threadwork_superseded.md:19<br>`live file still uses bare undefined 'RS Track' with no in-file expansion` — params/threadwork.md:139-142 | not_descriptors | impact_vector: MS (stat_delta)<br>victory conditions<br>threat_weaving prereqs | **DRIFTED** |
| Persuasion Track | track | designs/scene/social_contest_v30.md:89-93,184-276,481-488 | `0-10, banded: >=7 Side A wins, <=3 Side B wins, 4-6 compromise; Regroup/Concede a Point move it +-1; preserved unchanged by CR3` — designs/scene/social_contest_v30.md:481 | not_descriptors | — | **UNREGISTERED-LOAD-BEARING** |
| Piety Track / Conviction Track (multi-referent)<br><sub>aka: PT; CT; Conviction (personal worldview taxonomy, distinct referent); Persuasion Track (glossary appears to mis-describe this as Piety Track)</sub> | track | AMBIGUOUS: at least 4 structurally different referents share this name/abbreviation — see divergences | `(a) per-territory Church institutional-standing stat, 0-5, '(PT)'` — designs/scene/conviction_track_v30.md:14-23<br>`(b) per-character moral-belief/Scar mechanic, no stated 0-10 scale` — designs/personal/conviction_track_v1.md:1-10<br>`(c) 'Piety Track \| CT* \| 0-10 \| Debate position tracker... Side A wins >=7...' citing conviction_track_v1.md as canonical, but text matches Persuasion Track instead` — references/glossary.md:86<br>`(d) 'Piety Track \| 0-10 \| Per character \| Personal religious standing' — fourth uncited restatement` — designs/scene/derived_stats_v30.md:561<br>`range 0-5 (NOT 0-10), 0=Restoration/5=Orthodoxy, per-territory` — references/mechanical_terms_index.md:263 | not_descriptors | state.scar_acquired (module_contracts.yaml:225, per-Conviction scar count)<br>territory state vector<br>Calamity Drift formula | **AMBIGUOUS** |
| Renown | track | AMBIGUOUS: listed in registry, defined nowhere | — | not_descriptors | — | **ORPHANED** |
| Standing | track | references/glossary.md:110 | `0-10 (exception to 1-7 scale); no benefit above 7, 10 cosmetic max` — references/glossary.md:110 | not_descriptors | — | **COHERENT** |
| Turmoil (= Strain)<br><sub>aka: Strain</sub> | track | params/factions_personal.md:104 | `0-10, global; self-documented alias 'Also called "Strain" in peninsular_strain docs and phases.md §4d'` — params/factions_personal.md:104; params/bg/tracks.md:122-135 (PP-646); params/bg/core.md:141-149 | unregistered | — | **DRIFTED** |
| Vaynard Thread Mastery (VTM) | faction_stat | params/bg/tracks.md:22-24 ('VTM — STRUCK, PP-663, 2026-04-19) | `STRUCK as faction-level stat` — params/bg/tracks.md:22-24; params/bg/faction_actions.md:182-184; params/bg/npcs_special.md:29-32,91<br>`still gates numeric victory thresholds as if live: Path A VTM>=3, Path C VTM=5, Crown+Varfell VTM>=3, Varfell+RM VTM>=4` — params/bg/victory.md:13-15,52-53,88-90,129-130<br>`still gates Southernmost Champion access thresholds as if live: 'Vaynard (VTM 3+)', 'VTM 4+', 'VTM>=2: -1 Ob'` — params/bg/geography.md:270-403 | unregistered | — | **DEAD** |
| Warden's Accord (WA) / Warden Recognition (WR) | track | AMBIGUOUS: params/bg/victory.md (still cites WA) vs params/bg/geography.md (ED-311-resolved, states it replaces WA with WR) | `WA, range -3..+3, gates RM Emergence — Varfell Path B: WA>=+1; Varfell+RM co-victory: WA>=+2` — params/bg/victory.md:14,53,89,130; params/bg/npcs_special.md:75-84<br>`WR, range 0-4, Varfell-only, gates Path B — 'Replaces provisional conditions in victory_v30.md §3.4': WR>=2` — params/bg/geography.md:412-431; params/bg/npcs_special.md:40-51 | unregistered | — | **DRIFTED** |

## C5 — Faction / Settlement Stats  (13 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Defense (settlement) | settlement_stat | references/descriptor_registry.yaml:81 | `raw settlement stat, scale 0-5` — references/descriptor_registry.yaml:81 | warn | set.defense | **COHERENT** |
| Fort Level<br><sub>aka: Fort</sub> | settlement_stat | AMBIGUOUS:no owning module — appears only inside a derivation formula | `Garrison Strength = Defense*20 + Fort*30` — references/module_contracts.yaml:591-592 | unregistered | — | **UNREGISTERED-LOAD-BEARING** |
| Influence (faction stat) | faction_stat | references/descriptor_registry.yaml:65 | `raw faction stat, scale 1-7, floor 1 (cannot drop below 1)` — references/descriptor_registry.yaml:65; references/glossary.md:105 | warn | fac.influence | **COHERENT** |
| Intel | faction_stat | references/descriptor_registry.yaml:68 | `raw faction stat, scale 1-7 ('Intelligence capacity')` — references/descriptor_registry.yaml:68; references/glossary.md:108 | warn | fac.intel | **COHERENT** |
| Legitimacy (settlement, L)<br><sub>aka: L; L_s</sub> | settlement_stat | designs/territory/settlement_layer_v30.md:147-177 (§1.8, LPS-2e) | `per-settlement track, 0-7 (Jordan ruling 2026-05-30, supersedes PP-686 v2 faction-level L/PS)` — references/descriptor_registry.yaml:78; references/module_contracts.yaml:559 | warn | set.legitimacy<br>module_contracts.yaml derivation input L_s | **DRIFTED** |
| Mandate<br><sub>aka: Mandate Pool (deprecated usage, recommended rename: Political Pool per ci_political_v30 §3.4/§7.2)</sub> | faction_stat | AMBIGUOUS: params/factions_personal.md:14 (LINEAR) vs designs/provincial/faction_behavior_v30.md:398-410 §4 + faction_canon_v30.md:216 + references/module_contracts.yaml:598-601 (SATURATING) — the saturating form is the one actually cross-confirmed by 3 independent surfaces and is Stage-4 sim-validated | `LINEAR: round(0.5*Legitimacy + 0.5*Popular_Support), citing 'faction_behavior_v30 §4' as source` — params/factions_personal.md:14<br>`SATURATING: q_s=0.5*L_s+0.5*PS_s; W_s=base(Type)+Prosperity_s+FacilityTier_s; T=sum(W_s*(q_s/7)); Mandate=clamp(round(7T/(T+6)),0,7) — Lesson-5 bound, Stage-4 sim validated` — references/module_contracts.yaml:598-601; designs/provincial/faction_behavior_v30.md:398-410 (§4, current text); designs/provincial/faction_canon_v30.md:216; designs/territory/settlement_layer_v30.md:147-177 (§1.8, LPS-2e ruling that produced this form) | warn | echo_armature §2.1 Domain Echo Debate row<br>faction_state consumes<br>settlement_layer<->Mandate feedback loop (damper coefficient 0.6/season, module_contracts.yaml:562-563) | **DRIFTED** |
| Military (faction stat) | faction_stat | references/descriptor_registry.yaml:67 | `raw faction stat, scale 1-7; 0 = cannot Muster` — references/descriptor_registry.yaml:67; references/glossary.md:107<br>`Crown starting Military = 5 (Starting Stats table)` — params/bg/core.md:165<br>`Crown starting Military = 5/6, prior value 4 struck per ED-869/Jordan 2026-05-31` — params/factions/stats_1_7_scale.md:19 | warn | fac.military | **DRIFTED** |
| Order (settlement) | settlement_stat | references/descriptor_registry.yaml:82 | `raw settlement stat, scale 0-5` — references/descriptor_registry.yaml:82 | warn | set.order | **COHERENT** |
| Popular Support (settlement, PS)<br><sub>aka: PS; PS_s; Public Support (deprecated term, renamed 2026-05-30)</sub> | settlement_stat | designs/territory/settlement_layer_v30.md:147-177 (§1.8, LPS-2e) | `per-settlement track, 0-7` — references/descriptor_registry.yaml:79; references/module_contracts.yaml:559 | warn | set.popular_support | **DRIFTED** |
| Prosperity (settlement) | settlement_stat | references/descriptor_registry.yaml:80 | `raw settlement stat, scale 0-5` — references/descriptor_registry.yaml:80 | warn | set.prosperity | **COHERENT** |
| Settlement weight inputs (FacilityTier, base(Type), W_s) | derived_value | references/module_contracts.yaml:600 (formula-only, no owning state entries) | `W_s = base(Type) + Prosperity_s + FacilityTier_s; T = sum(W_s*(q_s/7))` — references/module_contracts.yaml:598-601; designs/territory/settlement_layer_v30.md:159 | unregistered | — | **UNREGISTERED-LOAD-BEARING** |
| Stability (faction stat) | faction_stat | references/descriptor_registry.yaml:69 | `raw faction stat, scale 1-7; 0 = Collapse trigger (P-15)` — references/descriptor_registry.yaml:69; references/glossary.md:109 | warn | fac.stability | **COHERENT** |
| Wealth | faction_stat | references/descriptor_registry.yaml:66 | `raw faction stat, scale 1-7; 0 = cannot Trade or fund Wealth-requiring actions` — references/descriptor_registry.yaml:66; references/glossary.md:106 | warn | fac.wealth | **COHERENT** |

## C6 — Code Constants / Export Pipeline  (20 rows)

| Name | Kind | Defining surface | Formula(s) | Registered | Key bindings | Status |
|---|---|---|---|---|---|---|
| Block Size (Mass Battle) | code_constant | sim/provincial/massbattle.py | `BLOCK_SIZE=100 (Company scale)` — sim/provincial/massbattle.py; designs/provincial/mass_battle_v30.md §A.3 | unregistered | — | **COHERENT** |
| CFG (Combat Engine coefficients, Class-C export) | code_constant | designs/scene/combat_engine_v1/config.py:2-172 | `~100+ tunable coefficients (L0=4.0, BASE_TEMPO=2.0, CONC_SPIRIT=2.0, CONC_FOCUS=3.0, INIT_SIGMA_K=0.16, etc.)` — designs/scene/combat_engine_v1/config.py:2-172 | unregistered | exports to references/engine_params/combat_engine_v1.json via tools/export_engine_params.py --check (blocking CI, the one typed export in the repo per CLAUDE.md §5) | **COHERENT** |
| CI Starting Value (code) | code_constant | sim/peninsular/ci_track.py | `CI_STARTING=28` — sim/peninsular/ci_track.py; faction_layer_v30.md starting CI | unregistered | — | **COHERENT** |
| Contest Resolver Constants | code_constant | sim/personal/contest/resolver.py:38-45 | `RES_FLOOR=0.15, REBUT_CAP=3.0, MERIT_SCALE=2.6, JITTER=0.08, PUBLIC_LEAK=0.5, INST_BIAS=0.6, PUB_BIAS=0.3, EVIDENCE_CAP=3.0` — sim/personal/contest/resolver.py:38-45 | unregistered | — | **COHERENT** |
| Contest Track Starting Position | code_constant | sim/personal/contest/modes.py:5-6 | `CANONICAL_TRACK_START=5.0 \| CHURCH_TRIBUNAL_TRACK_START=6.0` — sim/personal/contest/modes.py:5-6; params/contest.md; social_contest_v30.md §7 | unregistered | — | **COHERENT** |
| Degree Thresholds (Combat vs Contest) | code_constant | AMBIGUOUS-BY-DESIGN: two separate degree() functions with different Overwhelming-bar contracts | `Combat: Overwhelming net>=2*Ob AND net>=3 \| Success: net>=Ob \| Partial: net>0<Ob \| Failure: net<=0` — sim/autoload/dice_engine.py:94-122; params/core.md §Degrees of Success<br>`Contest: Overwhelming pool-aware (net>=muN+OVERWHELM_SIGMA*sigma*sqrt(N))` — sim/autoload/sigma_leverage.py:284-311; designs/audit/2026-06-03-contest-groundup/engine.py | unregistered | — | **DRIFTED** |
| Die Result Rule | code_constant | sim/autoload/dice_engine.py:43-51 | `1->-1, 2-6->0, 7-9->+1, 10->+2 successes (no chain)` — sim/autoload/dice_engine.py:43-51<br>`canonical source` — params/core.md §Die Rule, PP-246 | unregistered | — | **COHERENT** |
| LEVEL_SIGMA (modifier levels) | code_constant | sim/autoload/sigma_leverage.py:85-90 | `{minor:0.25, moderate:0.50, strong:0.75, major:1.00}` — sim/autoload/sigma_leverage.py:85-90; modifier_system_spec.md §2.3 | unregistered | — | **COHERENT** |
| M_MAX (soft-cap ceiling) | code_constant | sim/autoload/sigma_leverage.py:92 | `1.5 (sigma-units)` — sim/autoload/sigma_leverage.py:92; modifier_system_spec.md §3.1 | unregistered | — | **COHERENT** |
| MS Starting Value (code) | code_constant | sim/peninsular/ms_track.py | `MS_START=60` — sim/peninsular/ms_track.py; params/core.md (videogame canonical per Jordan 2026-06-06) | unregistered | — | **COHERENT** |
| MU_PER_DIE / SD_PER_DIE | code_constant | sim/autoload/sigma_leverage.py:100-101 | `0.40, 0.80 (TN7 only)` — sim/autoload/sigma_leverage.py:100-101; params/core.md §Expected Value (per die) | unregistered | — | **COHERENT** |
| OB_MIN | code_constant | sim/autoload/sigma_leverage.py:96 | `1` — sim/autoload/sigma_leverage.py:96; params/core.md §Obstacle Scale | unregistered | — | **COHERENT** |
| OVERWHELM_SIGMA | code_constant | sim/autoload/sigma_leverage.py:104 | `0.85` — sim/autoload/sigma_leverage.py:104; designs/audit/2026-06-03-contest-groundup/engine.py §degree | unregistered | — | **COHERENT** |
| Per-Die EV (mu, sigma) | code_constant | sim/autoload/dice_engine.py:58-62 | `TN6:(0.50,0.806) \| TN7:(0.40,0.800) \| TN8:(0.30,0.781)` — sim/autoload/dice_engine.py:58-62; sim/autoload/sigma_leverage.py:73-77 | unregistered | — | **COHERENT** |
| PT_MAP, ACCORD_MAP | code_constant | sim/autoload/game_state.py:50-80 | `PT_MAP: {0:1.0,1:2.5,2:4.0,3:5.5,4:6.5,5:7.0} \| ACCORD_MAP: {0:1.0,1:2.5,2:4.0,3:5.5,4:7.0}` — sim/autoload/game_state.py:50-80; settlement_layer_v30.md territory systems | unregistered | — | **COHERENT** |
| Readiness Constants (Contest) | code_constant | sim/personal/contest/primitives.py:18-31 | `MAX=12, REGAIN=4, BASE=3, MARGIN=1.0, READING_COEFF=1/6, CAP=3.0, ETHOS_UNLOCK=0.5, LEAK_CAP=0.9, FLOOR=0.40` — sim/personal/contest/primitives.py:18-31; designs/audit/2026-06-03-contest-groundup/primitives.py | unregistered | — | **COHERENT** |
| SIGMA_N_COEFF | code_constant | sim/autoload/sigma_leverage.py:93 | `0.8 (sigma-coefficient)` — sim/autoload/sigma_leverage.py:93; modifier_system_spec.md §2.1 | unregistered | — | **COHERENT** |
| STAMINA_REF | code_constant | designs/scene/combat_engine_v1/config.py:56 | `STAMINA_REF=18.0, defined but never consumed` — designs/scene/combat_engine_v1/config.py:56 | unregistered | — | **DEAD** |
| TN (Target Number) Standard | code_constant | sim/autoload/sigma_leverage.py:79 | `TN=7` — sim/autoload/sigma_leverage.py:79; params/core.md §TN Values | unregistered | — | **COHERENT** |
| Wound Ob Channel (WOUND_ATK_OB / WOUND_DEF_OB) | code_constant | designs/scene/combat_engine_v1/config.py:65 (ED-1041, ED-PC-0005 ratified 2026-07-08) | `WOUND_ATK_OB=0.15 (attacking), WOUND_DEF_OB=0.25 (defending) per wound; supersedes PP-716's universal -1D` — designs/scene/combat_engine_v1/config.py:65; designs/scene/derived_stats_v30.md:72,92,517; designs/scene/combat_v30.md:39,298; params/core.md:158; params/fieldwork.md:222-225; params/threadwork.md:63; params/mass_combat.md:434-435 | unregistered | — | **DRIFTED** |

## Divergence Highlights

Rows carrying a `divergences[]` entry (cross-surface disagreement, naming collision, or registration gap) are surfaced below, most consequential first (P1-flavored collisions and ambiguities before lower-severity synonym/staleness notes). Full evidence lives in each row's `finding_basis` field (yaml) — cite the underlying finder finding IDs (F-REG-*, F-PARAMS-*, F-DESIGN-*, F-C-*, F-SIM-*, FIX-*) for severity/calibration, not restated here to avoid re-litigating what the finders already established.

### Will  (C1, status: AMBIGUOUS)
- Registry names Will primary/Spirit alias, but every live formula sweep found (Concentration, Stamina, Thread-Read pool, Wound Interval, Thread Fatigue) uses 'Spirit' exclusively — the 'primary' name and the load-bearing name are inverted in practice.
  - *Finding basis:* F-REG-004, KNOWN-TRACKED ED-IN-0008

### Resonant Style  (C1, status: AMBIGUOUS)
- Referenced as an exposed state in module_contracts.yaml:231 gate g_scar2 but never declared as a state entry or emission anywhere in contracts.
  - *Finding basis:* F-C-010, F-DESIGN item; KNOWN-TRACKED ED-IN-0025 (resonance_style retirement correction, NEEDS-JORDAN — do not re-litigate disposition, only note registration gap)

### Piety Track / Conviction Track (multi-referent)  (C4, status: AMBIGUOUS)
- The narrower (a)-vs-tc_political_redesign 'Piety (PT)' duplicate is separately KNOWN-TRACKED (designs/provincial/faction_politics_v30.md:25 A-06; :1048 ED-644 'rename deferred') — that ED covers only that pair, not the broader 4-way collision.
- glossary.md:86's own description verbatim matches social_contest_v30.md:276's Persuasion Track, not the Scar mechanic its cited canonical doc (conviction_track_v1.md) actually defines — an apparent miscitation.
- name_collision_database.yaml separately records PT = Piety Track vs 'Piety Territory' as a third, still-pending collision (FIX-03); mechanical_terms_index flags an old diagnostic that used the wrong range (0-10 instead of 0-5).
  - *Finding basis:* F-DESIGN-4 (NEW, broader collision), F-C-001 (3-way collision per module_contracts gap_notes), FIX-03 (KNOWN-TRACKED acronym collision), ED-644 (KNOWN-TRACKED narrow duplicate — not re-litigated)

### Concentration  (C2, status: AMBIGUOUS)
- F-SIM-01 asserts a THIRD Concentration formula (Charisma*3) sourced to params/core.md:162, calling it a three-way collision with descriptor_registry and combatant.py. However every other family (F-REG, F-PARAMS, F-DESIGN) — including F-SIM's own combatant.py citation — independently converges on 3*Focus+2*Spirit, and Charisma*3 is elsewhere consistently attributed to Composure/Face, not Concentration. This merge does NOT silently resolve the discrepancy (per merge rule 5) but flags F-SIM-01's params/core.md:162 citation as the outlier requiring direct re-verification against the working file — possibly a transcription slip conflating Concentration with Composure, possibly a genuine stale duplicate entry in params/core.md itself.
- Concentration is referenced in Key stat_deltas payloads (per F-SIM) but has no descriptor_registry key of its own — stat_deltas accepts any string key with zero vocabulary validation (F-SIM-02/03, enforcement-gap).
  - *Finding basis:* F-SIM-01 (flagged AMBIGUOUS rather than adjudicated — needs direct re-check of params/core.md:162 against disk), F-SIM-02/03 (key-binding-gap + enforcement-gap, both NEW and independent of the formula question)

### Acuity  (C1, status: DRIFTED)
- descriptor_registry.yaml:39 names Acuity primary (aliases Reasoning/Cognition); references/glossary.md:37 names Cognition primary with no Acuity mention; names_index.yaml:49 marks Cognition legacy (enforce:warn).
  - *Finding basis:* F-REG-003, KNOWN-TRACKED ED-IN-0008 (7-vs-9 roster/naming-authority conflict)

### Bonds  (C1, status: DRIFTED)
- Absent from glossary.md's 7-attribute table entirely (glossary.md:27-41) even though descriptor_registry carries a 9-attribute roster (glossary.md:31 self-flags the conflict).
  - *Finding basis:* F-REG-005, KNOWN-TRACKED ED-IN-0008 (7-vs-9 roster)

### Military (faction stat)  (C5, status: DRIFTED)
- params/bg/core.md:172's own footnote (2026-05-30) still claims an UNRESOLVED conflict with stats_1_7_scale.md ('=4, direction undetermined, see ED-869') even though stats_1_7_scale.md's own text (dated one day later, 2026-05-31) shows the conflict was already resolved to 5/6 — the bg/core.md footnote is stale relative to its own cited resolution.
  - *Finding basis:* F-PARAMS-09, KNOWN-TRACKED ED-869 (footnote staleness itself is the NEW residual)

### Legitimacy (settlement, L)  (C5, status: DRIFTED)
- designs/provincial/faction_behavior_v30.md retains its old per-territory §3.4/§3.5 dynamics formulas (pre-LPS-2e) beneath an inline SUPERSEDED-BY banner rather than being rewritten/removed.
- Referenced as 'L'/'PS' in module_contracts prose but 'L_s'/'PS_s' in the Mandate derivation formula — abbreviation-vs-subscript synonym split (F-C-008).
  - *Finding basis:* F-C-008, F-DESIGN (Legitimacy/Popular Support per-settlement item)

### Popular Support (settlement, PS)  (C5, status: DRIFTED)
- Deprecated term 'Public Support' (pre-2026-05-30 rename) still appears live in settlement_layer_v30.md:631 — renamed but not propagated (FIX-08).
  - *Finding basis:* FIX-08 (KNOWN-UNTRACKED per name_collision_database.yaml:469 deprecated_term_residual)

### Church Influence (CI)  (C4, status: DRIFTED)
- campaign_modes.md's TTRPG-mode CI=15 matches neither the TTRPG value (0) nor the BG value (28) cited anywhere else (F-PARAMS-03).
- params/bg/victory.md:17,92 reuses the 'CI' abbreviation for a second, undefined quantity 'Thread Consciousness' inside the same table that uses CI exclusively for Church Influence elsewhere (F-PARAMS-06).
- name_collision_database.yaml:459 separately records CI = Church Influence vs 'Crown Index' as a pending Jordan-adjudication collision (FIX-03, KNOWN-TRACKED).
- Two CI thresholds (65 'primary victory' vs 60 'Mass Seizure available') coexist without cross-reference distinguishing them as separate gates.
  - *Finding basis:* F-PARAMS-03, F-PARAMS-06, FIX-03, F-C-012

### Institutional Pressure / Invasion Pressure (IP)  (C4, status: DRIFTED)
- Same 0-100 clock (start 20) carries two different full names across sibling files sharing abbreviation IP, never cross-referenced (F-PARAMS-05).
- name_collision_database.yaml separately records IP = Institutional Pressure vs 'Imperial Pressure' as a second, still-pending collision (FIX-03).
- No file in either family states an explicit season-over-season advancement formula for IP — thresholds are documented, the update rule is not (FIX-09).
  - *Finding basis:* F-PARAMS-05, FIX-03, FIX-09

### Mending Stability (MS)  (C4, status: DRIFTED)
- Renamed ED-731 in params/core.md and glossary.md, but params/threadwork.md (live, non-superseded) and params/bg/phases.md, bg/npc_priority_trees.md carry bare 'RS' with no expansion anywhere in-file.
- values_master.yaml:190 header still says 'Rendering Stability (start)'; mechanics_index.yaml:778 entry 'rs_track' still labeled 'Rendering Stability world-track' (F-REG-011).
- module_contracts.yaml gap_notes:671 flags MS as an unowned clock read by victory module gates (g_ms0/g_ms5/g_msrec) with no emitting module in contracts (F-C-002).
  - *Finding basis:* F-PARAMS-01 (KNOWN-UNTRACKED — no ED governs the MS<->RS name unification), F-REG-011, F-C-002

### Warden's Accord (WA) / Warden Recognition (WR)  (C4, status: DRIFTED)
- params/bg/geography.md's own ED-311-RESOLVED Path B table explicitly states it replaces victory.md §3.4's WA-gated version with a WR-gated version, but victory.md's Summary and Co-Victory tables were never updated off WA — an engine reading victory.md's own table would gate on the wrong (superseded) track.
- name_collision_database.yaml separately flags WC/WR as 'registered but no quantity-level definition/bounds/formula found' (FIX-07) — a narrower, still-open registration gap on WR specifically.
  - *Finding basis:* F-PARAMS-04 (NEW), FIX-07 (NEW, registration-gap angle)

### Turmoil (= Strain)  (C4, status: DRIFTED)
- Synonym is self-disclosed in-place (not silent) — lower severity than the MS/RS split. Table duplicated near-verbatim across 3 files, a maintenance/drift risk even though values currently agree.
  - *Finding basis:* F-PARAMS (KNOWN-UNTRACKED, low-stakes)

### Evidence (Track)  (C4, status: DRIFTED)
- kind_guess split: F-REG classifies as 'clock' (descriptor_registry.yaml:109 not_descriptors), F-DESIGN documents it as a fieldwork 'Evidence Track' — same concept, inconsistent kind taxonomy applied even within the not_descriptors framework.
  - *Finding basis:* F-REG (clock), F-DESIGN (track) — cross-family kind mismatch, NEW observation

### Combat Pool  (C3, status: DRIFTED)
- Triple-carried in values_master.yaml (quarantined, ED-1084) and params/core.md's own stale header — the prose/table body is correct but its provenance comment is stale.
- designs/scene/derived_stats_v30.md self-contradicts: §13 'What Does NOT Change' (line 515) states the struck (Agi*2)+History+3 form as still-current, while §14.4 (line 584) two sections later states that exact formula was STRUCK (F-DESIGN-1, NEW).
- module_contracts.yaml:810's 'History' term is not itself a declared attribute in the 9-attribute roster (descriptor_registry.yaml) — it is a derived/tracked quantity from elsewhere (relevant skill History), not flagged as a gap by any family but worth noting for completeness (F-C-006).
  - *Finding basis:* F-REG-001, F-PARAMS(F-SIM-06), F-DESIGN-1, F-C-006, FIX-05 — all KNOWN-TRACKED at the values_master level; F-DESIGN-1's specific self-contradiction is NEW

### Stamina  (C2, status: DRIFTED)
- designs/scene/combat_v30.md — the design-layer source doc for personal combat's non-resolution content — still carries the pre-S1 formula and recovery rule with no pointer to the S1-ratified values, even though derived_stats_v30.md's own §12 table documents the supersession explicitly (F-DESIGN-2, NEW).
- The sim implementation (combatant.py) already matches the CURRENT formula, so the drift is confined to prose (combat_v30.md, values_master.yaml), not the executable oracle.
  - *Finding basis:* F-DESIGN-2 (NEW), F-REG, F-SIM (canonical confirmation)

### Faction Legitimacy (derived meter)  (C2, status: DRIFTED)
- Namespace collision with settlement-scale Legitimacy (set.legitimacy, 0-7, C5) — same word 'Legitimacy' names two different quantities at two different scales (raw per-settlement stat vs faction-level derived meter). The doc's own footnote (line 554) documents the LPS-1->LPS-2e correction and disclaims a 0-100 master scale, but no registry key distinguishes the two 'Legitimacy' referents.
  - *Finding basis:* F-DESIGN footnote + cross-read against C5 Legitimacy row (NEW: the namespace collision itself)

### Local Economy / Garrison Strength / Public Order  (C2, status: DRIFTED)
- settlement_layer_v30.md:43 cites 'derived_stats_v1 §4' as its source, but current derived_stats_v30.md numbers this section §9, not §4 — a stale section-number citation (F-DESIGN).
- Gate g_dv0 ('derived value = 0 held through Accounting -> stat -1', module_contracts.yaml:575-578) doesn't specify which of the three derived values triggers it, or whether all three must be 0 simultaneously (F-C, gate-logic ambiguity noted but not fully adjudicated — F-GATES family territory).
  - *Finding basis:* F-C item notes, F-DESIGN (stale section citation)

### Argue Pool  (C3, status: DRIFTED)
- Own home document repeats an incomplete formula 3 times while a separate cross-scale comparison table (derived_stats_v30.md) states the complete version including the style/audience bonus — an intra-document rather than cross-document drift (F-DESIGN-6, NEW).
  - *Finding basis:* F-DESIGN-6

### Mass Combat Pool (personal/TTRPG-scale unit)  (C3, status: DRIFTED)
- params/mass_combat.md itself is a well-documented positive control (self-disclosed ED-899 FOLLOW-UP banner) — but derived_stats_v30.md's §14.4 cross-scale comparison table restates the LEGACY PP-233 form with NO ED-899/ED-1013 caveat at all, and mass_battle_v30.md's own §A.1 headline and §A.7 step-1 restatement likewise foreground the legacy form (with only a parenthetical aside pointing to the live default) (F-DESIGN-3, KNOWN-UNTRACKED — the design-doc-headline instance is a distinct, uncited residual from the already-known params/mass_combat.md header duplication).
  - *Finding basis:* F-DESIGN-3 (KNOWN-UNTRACKED), params/mass_combat.md self-disclosure (KNOWN-TRACKED, positive control)

### Degree Thresholds (Combat vs Contest)  (C6, status: DRIFTED)
- Two degree() functions coexist with different Overwhelming-bar contracts; sigma_leverage.py:287-294 explains the split as intentional, but it remains an unreconciled naming/contract collision between combat and contest resolution (F-SIM-05, KNOWN-UNTRACKED).
  - *Finding basis:* F-SIM-05

### Wound Ob Channel (WOUND_ATK_OB / WOUND_DEF_OB)  (C6, status: DRIFTED)
- Combat's own fractional-Ob value (ED-1041) is ratified; the same-day ruling (ED-PC-0005, 2026-07-08) that generalizes 'fractional Ob per wound' to non-combat pools (Thread ops, fieldwork, mass-battle Command) explicitly defers the actual value to a follow-on calibration (ED-PC-0006, not yet set) — this is KNOWN-TRACKED and cited near-identically across 4 files dated the same day as this audit.
  - *Finding basis:* KNOWN-TRACKED ED-PC-0005/ED-PC-0006, cited in all contributing families — not re-litigated

### Mandate  (C5, status: DRIFTED)
- params/factions_personal.md:14's citation of 'faction_behavior_v30 §4' is now stale: that section was rewritten under the LPS-2e ruling (2026-05-30) to the saturating, size-weighted form, but the params citation still states the old flat/linear mean — the params doc's own citation no longer matches its cited source (F-DESIGN-5, confirms the exact divergence named in this audit's baseline facts).
- name_collision_database.yaml separately flags 'Mandate Pool' as a stat-noun-as-pool-name collision, recommending 'Political Pool' (already canonical usage in ci_political_v30 §3.4/§7.2) — unresolved, low severity.
  - *Finding basis:* F-REG-002 (NEW), F-DESIGN-5 (NEW, confirms baseline-flagged divergence with exact citations), F-C (contract-side saturating form), FIX (Mandate Pool naming, low-severity unresolved)

### Fort Level  (C5, status: UNREGISTERED-LOAD-BEARING)
- Appears only in the Garrison Strength formula; never declared as a state entry for any module in module_contracts.yaml, not in descriptor_registry, not in names_index.
  - *Finding basis:* F-C-007

### Settlement weight inputs (FacilityTier, base(Type), W_s)  (C5, status: UNREGISTERED-LOAD-BEARING)
- FacilityTier, base(Type), and W_s all appear only as formula intermediates in the Mandate derivation; none are declared state entries or derivations of their own. 'base(Type)' notation is unclear (unresolved whether 'Type' is settlement-type metadata).
  - *Finding basis:* F-C-005

### Persuasion Track  (C4, status: UNREGISTERED-LOAD-BEARING)
- descriptor_registry.yaml:108 lists a bare 'Persuasion' in not_descriptors:tracks with NO scale or formula (F-REG-009, treated there as an orphan) — but a full, coherent definition of a *track by this name* exists in social_contest_v30.md. Likely the same concept under-linked from the registry's bare-name list rather than a genuinely undefined quantity; flagged as a registry-linkage gap, not a design gap.
- glossary.md:86's Piety Track entry appears to actually describe this Persuasion Track's mechanics verbatim (see Piety Track row).
  - *Finding basis:* F-REG-009 + F-DESIGN cross-read; NEW (the registry-vs-design contradiction itself)

### Health  (C2, status: UNREGISTERED-LOAD-BEARING)
- module_contracts.yaml's personal_combat module state list (Health, cumulative_damage, Wounds, Stamina, Initiative, Poise) does not include the character attributes (Endurance, Spirit, Strength) its own Health formula depends on — these must come from an external character-attribute model never cross-referenced in the contract (F-C-003, key-binding-gap).
  - *Finding basis:* F-C-003 (NEW), F-DESIGN/F-SIM (formula itself coherent across all three surfaces)

### Wound Interval (WI)  (C2, status: UNREGISTERED-LOAD-BEARING)
- Defined only in a formula comment in module_contracts.yaml, never declared as its own state entry or derivation despite being load-bearing for both Health and Wounds (F-C-009).
  - *Finding basis:* F-C-009

### Max Wounds (MW)  (C2, status: UNREGISTERED-LOAD-BEARING)
- Appears only in formulas (Wounds derivation line 821, Health derivation line 828) in module_contracts.yaml; never declared as its own state entry or derivation (F-C-009).
  - *Finding basis:* F-C-009

### Thread Pool Score (TPS)  (C2, status: UNREGISTERED-LOAD-BEARING)
- No key in descriptor_registry, not_descriptors, or names_index despite being a live bonus-dice source in multiple pool formulas (F-REG-007).
  - *Finding basis:* F-REG-007

### cumulative_drift  (C2, status: UNREGISTERED-LOAD-BEARING)
- Never declared as a state entry in npc_behavior's beliefs/opinions/concerns/projects/arc-state list (module_contracts.yaml:155-159); appears solely as a gate condition.
  - *Finding basis:* F-C-004

### Knot Pool  (C3, status: UNREGISTERED-LOAD-BEARING)
- No registry key (knots.pool not in key_type_registry_v30.md); knots module_contracts.yaml entry lists impact_vector (strain) but not pool (F-REG-013, key-binding-gap).
  - *Finding basis:* F-REG-013

### Agility  (C1, status: ORPHANED)
- STRUCK from Combat Pool formula (ED-900/904) — attribute still registered and scaled but its one load-bearing combat consumer was removed; no other consumer confirmed in this sweep.
  - *Finding basis:* F-REG (Agility STRUCK note)

### Body (aggregate)  (C1, status: ORPHANED)
- Legacy Stat*3 multipliers remain live in place of this aggregate wherever a body-scale multiplier is needed — the aggregate is defined but not consumed anywhere in this sweep.
  - *Finding basis:* CLAUDE.md baseline / descriptor_registry.yaml status:placeholder

### Renown  (C4, status: ORPHANED)
- descriptor_registry.yaml:108 lists Renown in not_descriptors:tracks; no scale, formula, or design-doc definition found anywhere in the swept corpus.
  - *Finding basis:* F-REG-008

### Vaynard Thread Mastery (VTM)  (C4, status: DEAD)
- The strike itself is KNOWN-TRACKED, but params/bg/victory.md's live victory-condition tables and params/bg/geography.md's entire Southernmost Access/Champion-qualification system never received the propagation and still treat VTM as a live, numerically-checkable stat — both are load-bearing surfaces for actual play resolution.
  - *Finding basis:* F-PARAMS-02 (NEW: the non-propagation, not the strike itself)

### STAMINA_REF  (C6, status: DEAD)
- Live code (combatant.py:45-47,122) reads STAMINA_PER_END/STAMINA_PER_SPIRIT directly ('cfg-free'), bypassing this constant entirely.
  - *Finding basis:* F-SIM-04

### Charisma  (C1, status: COHERENT)
- Alias 'Influence' for this attribute is a distinct namespace collision against fac.influence (Influence faction_stat, C5) — same word, two unrelated quantities at different scales; no registry cross-reference flags it.
  - *Finding basis:* F-REG

### Influence (faction stat)  (C5, status: COHERENT)
- Shares the bare word 'Influence' with attr.social.charisma's alias 'Influence' (C1) — different concept, different scale, no registry disambiguation.
  - *Finding basis:* F-REG

### Coherence (cross-scale)  (C4, status: COHERENT)
- mechanical_terms_index.md:2 explicitly endorses this as an INTENTIONAL cross-silo concept at three scales (personal countdown track, cosmological TS-gated bands) — treated here as by-design, not a defect.
- kind_guess itself is inconsistent across families (derived_value in F-REG vs track in F-DESIGN) for the same personal-scale referent — a minor taxonomy inconsistency riding on top of the intentional multi-scale design.
  - *Finding basis:* F-INDEX (intentional-design note), F-REG/F-DESIGN kind-guess mismatch (NEW, minor)

### Composure / Face  (C2, status: COHERENT)
- ED-1056 explicitly scopes the Composure->Face rename to social-contest only; combat/knots/conviction retain 'Composure' as a Jordan-confirmed scoped exception (self-documented, KNOWN-TRACKED, not re-litigated).
  - *Finding basis:* KNOWN-TRACKED ED-1056 — well cross-referenced in-file, logged for completeness

### Command (mass combat rating)  (C2, status: COHERENT)
- Reiterated identically in 3+ places across mass_combat.md (Commander Bonus Formulas Consolidated table, PP-190 note) and mass_battle_v30.md — redundant restatement, a maintenance-burden P3 rather than a coherence defect.
  - *Finding basis:* F-PARAMS, F-DESIGN — no value collision found, only redundancy

### Fieldwork Pool  (C3, status: COHERENT)
- fieldwork.md:9-12 explicitly documents (ED-1084) that its original by-analogy justification to Combat Pool no longer holds post-ED-901 (Combat Pool is now Agility-independent) but correctly notes its own x2 form now stands independently — a positive control case of successful ED-1084 propagation, unlike Combat Pool's own carriers.
  - *Finding basis:* F-PARAMS control-case note, no defect found

### Mass Combat Pool (Board Game mode)  (C3, status: COHERENT)
- Distinct BG-mode formula, explicitly a separate mode per the doc's own 'Three-mode' framing (line 9) — not a collision, catalogued for completeness.
  - *Finding basis:* F-DESIGN — no defect, different mode by design

### Faction Domain Pool  (C3, status: COHERENT)
- Doc's own V-1 note (§14.5, line 592-596) explicitly flags this as an intentional non-proportional scale-shift vs. personal-scale pools — by design, not a defect.
  - *Finding basis:* F-DESIGN — single occurrence, self-disclosed design intent

### PT_MAP, ACCORD_MAP  (C6, status: COHERENT)
- 'PT_MAP' translates Piety Track values — a code-level touchpoint into the multi-referent Piety Track collision (see that C4 row); not independently re-verified against which Piety Track referent it maps.
  - *Finding basis:* F-SIM; cross-link to Piety Track row is NEW observation

### MS Starting Value (code)  (C6, status: COHERENT)
- Matches params/core.md's TTRPG-mode MS start (60) — see Mending Stability (C4) row for the broader MS/RS naming split this code constant sits inside.
  - *Finding basis:* F-SIM; cross-link to Mending Stability row

### CI Starting Value (code)  (C6, status: COHERENT)
- Matches the BG-mode CI start (28) triangulated across bg/core.md, bg/ci_seizure.md, bg/parliament.md — see Church Influence (C4) row for the campaign_modes.md=15 discrepancy this code constant does NOT share.
  - *Finding basis:* F-SIM; cross-link to Church Influence row

## Totals

**Total rows:** 88

**By cluster:**
- C1 — Attributes / Aliases / Aggregates: 14
- C2 — Derived Values: 20
- C3 — Pools: 8
- C4 — Tracks + Clocks: 13
- C5 — Faction / Settlement Stats: 13
- C6 — Code Constants / Export Pipeline: 20

**By status:**
- COHERENT: 46
- DRIFTED: 21
- UNREGISTERED-LOAD-BEARING: 10
- ORPHANED: 5
- AMBIGUOUS: 4
- DEAD: 2

**By registered tier:**
- unregistered: 38
- not_descriptors: 26
- warn: 24

**By kind:**
- derived_value: 20
- code_constant: 20
- attribute_scalar: 9
- faction_stat: 8
- track: 8
- pool: 7
- settlement_stat: 6
- attribute_aggregate: 3
- practitioner_stat: 3
- clock: 3
- unit_stat: 1

**Rows with recorded divergences:** 49 / 88
