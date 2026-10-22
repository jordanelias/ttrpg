# R6 - Mass battle and campaign war: Total War, Field of Glory II Medieval, Ultimate General, Hearts of Iron IV (v2, verified)

Evidence note (v2). Blocked: Fandom (402/403), Paradox wiki + forum (Client Challenge, incl. action=raw and api.php; not bypassed), web.archive.org (unreachable), gamewatcher (Cloudflare). Reached: official Total War Rome II manual, the FoG2 Medieval manual PDF (Matrix FTP), Steam threads/store, Slitherine forum, Wikipedia, GitHub raw (HOI4 `00_defines.lua` and `00_terrain.txt` mirrors). Tags: [V2 url ver/date] page body read this session; [S2 url] snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED] sources disagree. WebSearch budget was exhausted mid-pass, so some `?` cells could not be retried.

## 1. Total War - Creative Assembly/SEGA; real-time battles + turn-based campaign
Doc anchor: the official **Rome II** encyclopaedia manual (r2enc.totalwar.com; page dates not shown). It is the only official Total War manual reachable. v1 attributed its stance text to "Warhammer"; it is Rome II. Warhammer III / Three Kingdoms / Medieval II cells carry their own tags.

| id | val | how |
|---|---|---|
| F1 | YES | Units "muster" to a general standing in a region, from that region's troop types only; queue; no mustering during forced march, ambush or raiding [V2 r2enc recruit + stances, Rome II]. 3K "owned territory only" [M; Fandom 402] |
| E6 | YES | Upkeep paid from treasury at the start of each turn; mercenary upkeep = recruitment cost; raiding stance lowers upkeep [V2 r2enc recruit + stances, Rome II]. WH3/3K/M2 per-unit numbers `?`. Rome-engine data field `stat_cost turns,recruit,upkeep,wpn_upg,arm_upg,cb_cost` [V2 FeralInteractive EDU.md, Rome Remastered] |
| F2 | YES | More than 20 units are auto-fielded as one force unless unchecked, the rest arriving as reinforcements; battlefield command "up to forty units" [V2 r2enc attack + battle_play, Rome II]. WH3/3K caps, lord/hero skills [M] |
| F3 | YES | Secret deployment phase; deployable barricades, stakes, spike traps, brimstone; battle type fixes sides (river crossing: opposite banks; walled settlement: defend or sally; ambush) [V2 r2enc 0077, 0033, Rome II] |
| F4 | YES | Battlefield is "a real-time environment" [V2 r2enc 0075]; pause, per-unit orders, formations [M] |
| F5 | YES | Auto-resolve "compares the statistics of all the units"; Rome II adds an auto-resolve stance (aggressive / protective / balanced) [V2 r2enc 0016]. WH3 formula unpublished; community-measured wipe-out thresholds below |
| F6 | YES | Rome II: encircle (starvation timer, port doubles it) or assault with engines built on site, sally-outs, capture options occupy/loot/raze [V2 r2enc 0021]. WH3/3K/M2 siege battles [M] |
| F7 | PART | Rome II: attrition only in desert/extreme cold/deep sea; replenishment only in friendly land, faster nearer fresh-recruit regions; siege starvation [V2 r2enc 0026, 0021]. 3K food/supply attrition, WH attrition [M; v1 snippets, Fandom 402] |
| F8 | YES | Morale bar, rout, general's rally ability; routers "shatter" (unrallyable) if the general dies or none was fielded [V2 r2enc 0087, Rome II]. M2TW v1.2 lists "Generals are now more effective at chasing down routing units" under its AI heading, so AI generals [V2 gamepressure, 7 May 2007] |
| K1 | YES | Move within highlighted range; "cannot enter a zone of control unless you are attacking the army within it" [V2 r2enc 0019, 0016] |
| M3 | YES | Replenishment on friendly ground; experience page; captured settlements; 3K replenishment off in neutral/enemy land [M; Fandom 402] |
| B3/B4 | PART | General/lord assignment, 3K court posts [M, unverified] |

Mechanics worth knowing:
- **Stances (Rome II manual, not Warhammer)**: forced march "gets a significant increase in the action points", cannot muster, reduced line of sight (no percentage on the page); ambush "immobilises an army but increases its line of sight and makes it invisible"; raiding draws income from nearby trade routes and settlements, lowers upkeep, reduces defence and movement, and in one's own land causes unrest; muster/garrison replenish faster; a hidden army can attack anything entering its ZOC. Attacking an army in forced march gives an ambush battle in which the defender's allies cannot join [V2 r2enc + r2encv2 stances; r2enc 0033]. v1's "+50% movement" and "cannot retreat when attacked" appear on neither page.
- **Auto-resolve wipe-out thresholds (community-tested, not CA-published)**: in the Steam Workshop "Advanced Autoresolver" (a Warhammer II mod) discussion, a tester wrote on Jul 3 2023 "after some testing" that three default variables are `autoresolver_alliance_wipe_out_loser_strength_of_max_threshold` 0.3 (losing army under 30% of pre-battle strength is wiped out), `autoresolver_unit_wipe_out_threshold` 0.2 (multi-model unit under 20% of models wiped out) and `autoresolver_wipe_out_army_force_unary_lost` 0.92 (single-model unit, over 92% HP lost). The mod's developer, answering Jul 1 from memory ("IIRC"), reads the first as applying to a loser that might otherwise escape. Slightly different readings, same values; WH3 values not checked [V2 https://steamcommunity.com/workshop/filedetails/discussion/1954849209/2659871851778938275, WH2 mod, Jul 2023]. The three WH3 Steam threads v1 cited contain no such numbers.
- WH3 players: auto-resolve "just does a very simplified calculation"; abilities and spells are numeric stat additions to a unit's Combat Potential (AurumHawke, Oct 2024); low battle difficulty gives better auto-resolves [V2 Steam 3832045251561220120 (May 2023), 4697910068985751182 (Oct 2024); player claims]. M2TW: posters disagree whether it uses only power rating, defence stats, HP or command [CONTESTED; V2 Steam app 4700 thread 1735468693708609844].
- Mercenaries bypass the multi-turn recruit queue and cost upkeep equal to recruit cost [V2 r2enc recruit, Rome II].
- Design lesson (inference, not sourced): two resolvers for one fight (real-time and auto-resolve) with a known quality gap; Valoria's single automatic sim avoids that but offers no player-facing handle.

---
## 2. Field of Glory II: Medieval - Byzantine Games/Slitherine; turn-based tactical wargame on a SQUARE grid
Source: official game manual PDF, 227 pp, InDesign build dated 2022-07-25 (ftp.matrixgames.com), written after patch v1.3.5 (10 Feb 2022, whose notes say the manual was revised to cover all rules changes) [V2]. v1 said "hex"; the manual's movement, ZOC and facing are square-based. Campaign mode is a chain of 3/5/7/9/11/13/15 battles, not a strategic map [V2 manual §7.1.3].

| id | val | how |
|---|---|---|
| F1 | PART | Quick/custom battles: computer picks armies or player tailors within limits (slightly smaller force); campaign: recruitment points between battles sized to expected survivors [V2 manual §5.7, §7.5, §7.8] |
| F2 | YES | All non-light commands get a general; command range Troop 4 / Field 8 / Great 12 squares; C-in-C commands any troops, sub-general non-allied troops [V2 manual §9.1-9.2] |
| F3 | YES | Deployment inside specified areas (light troops get a larger one), set facings, switch units between commands; some scenarios allow none [V2 manual §10, §11.15] |
| F4 | YES | Turn-based, per-unit orders (move, charge, fight melee, fall back...); open ground costs 4 AP straight, 6 diagonal [V2 manual §11.1] |
| F5 | NO | No auto-resolve in a 227-page manual (grep: "auto-resolve"/"autoresolve" absent; "Autobreak" is morale). A lost campaign battle is replayed or fought again after retreat [V2 manual §7.3, §7.9] |
| F6 | PART | Scenarios "Relieve Besieged Fortress" and its enemy twin, garrisons can sally; Field Fortifications +100 POA, 33% cover; Heavy (castle/city walls) +200 POA, 75% cover, Difficult terrain to assaulters [V2 manual §5.3.11-12, §16.6.3] |
| F7 | NO | Only ammunition: 5 shooting turns at full effect, then half effect; campaign has points and garrison upkeep savings, no supply [V2 manual §11.11.5, §7.6] |
| F8 | YES | Four cohesion states, tests, rally, autobreak, pursuit by troop type, army break at 60% routed [V2 manual §14, §18] |
| M3 | PART | Core army persists, gains experience and elan, can promote; units with no losses gain no experience; enemy armies regenerated each battle [V2 manual §7.4-7.5] |

Mechanics worth knowing:
- **Cohesion test**: 2d6-equivalent, re-rolls by quality (Untrained re-roll 6s, Superior 1s, Elite 1s and 2s); pass at 6; fail drops a state, two states if the score is below 3, never two from shooting and from melee only if it "lost badly". Triggers: over ~10% shooting casualties in a turn, losing a melee round, a friend breaking, a general incapacitated nearby, falling back inside charge reach. Modifiers include -1 for >5% melee damage taken, -1 over 25% / 50% men lost, -1 threatened flank, +1 heavy/determined foot, +1 friendly general in melee within command range/4; Disrupted -1, Fragmented -2, Broken -3 [V2 manual §14.2]. Rome-era forum quote of the same rule, 10 Apr 2018, double drop at score 2 or less, close-combat limit planned to 1 [V2 forum p=927225].
- **Flank/rear**: a charge counts only if the charger starts its whole move on or behind the line extending the target's flank. If the target is already in melee or evaded: automatic -1 cohesion and a guaranteed +200 net POA for the flankers; otherwise min +50 POA, no cohesion drop. Squares, standard wagons and war wagons are immune; one flank cohesion drop per turn [V2 manual §11.13.5]. v1 cited forum p=668617 for this; that thread is the A.I. developer diary (AI rests a flank on a river or coast, avoids advancing into flank exposure), not the rule.
- **ZOC**: primary ZOC is the square directly in front, secondary the two squares either side; a move may enter but not pass beyond [V2 manual §11.1.1]. **Frontage**: no separate frontage rule found; a unit is one tile with 8 facings [V2 manual §11 text]; casualty % counts at most 12 ranks of men [V2 §14.2].
- **Generals**: a general in melee adds +50 POA to his unit and +1 cohesion to friends within command range/4; a killed or wounded general forces tests within 1 square (sub-general) or 2 (C-in-C/ally); a unit with a general always tests to rally, others "much lower chance" [V2 manual §9.3-9.5, §14.3]. v1's "20% without a general" is not in the manual.
- **Army break**: side loses when 60% of original troops are routed or dispersed, or 40-59% and the enemy lost at least 25% less; standard wagons (carroccio) count heavily in that percentage [V2 manual §18]. Valoria's army rout also has a "60% of troops in routed subunits" line, so the thresholds are parallel; the units differ.
- Autobreak: an average unit breaks near 50% strength; routers disperse after 5 rout moves; pursuit chances by troop type (mounted at least once; other foot never) [V2 manual §14.4, §14.6]. v1's Medieval-specific "combat round" note [S2 gamewatcher, 403 now]: the manual's trigger "lose a round of close combat" is consistent. Patch 1.3.5 raised the infantry impact CT modifier vs knightly lancers in open terrain from -1 to -2 [V2 forum t=108342, 10 Feb 2022].

---
## 3. Ultimate General (Gettysburg 2014, Civil War 2016-2018) - Game-Labs; real-time tactical battles [V2 Wikipedia: Gettysburg early access 12 Jun 2014, full 15 Oct 2014, final patch 1.09 Nov 2017; Civil War early access 16 Nov 2016, final patch 1.10 18 May 2018]
Little could be verified; no official officer-rating or flank-multiplier numbers were reachable.

| id | val | how |
|---|---|---|
| F1 | PART | Civil War: campaign over 1861-65, 50+ battles, success tied to battle outcomes [V2 en.wikipedia Ultimate_General:_Civil_War]; recruitment detail [M]. Gettysburg: battle-only plus a "non-linear battle campaign" across days [V2 store 306660] |
| F2 | YES | Gettysburg: full order of battle, brigades "differing competencies", generals/officers "actively participate" [V2 store 306660]. Civil War officer ratings [M] |
| F3 | PART | Placement before battle [M]; not verified |
| F4 | YES | Tagged "Real Time Tactics" [V2 store 306660]; pause [M] |
| F5 | PART | [M]; unverified |
| F7 | PART | Fatigue is a morale input [V2 store]; ammo/supply campaign layer [M] |
| F8 | YES | Morale reacts to flank or rear attacks, casualties, volley shocks, artillery fire, fatigue; elevation gives sight, morale, accuracy [V2 store 306660, 2014 text] |
| M3 | PART | Campaign persists across battles [V2 Wikipedia]; veterancy detail [M] |

Mechanics worth knowing:
- Dense formations resist charges and flank attacks but are more vulnerable to projectile fire [V2 store 306660].
- Player advice (not rules): flanking fire "drains a unit's morale faster"; do not pursue a retreating enemy, it returns once morale recovers [V2 Steam app 306660 thread 1457328392108109279; player claims].
- Not established: officer ratings, flank multiplier, frontage (`?`). Tried: store page, Steam thread, Wikipedia; Fandom 403, Game-Labs site now Stillfront.

---
## 4. Hearts of Iron IV - Paradox; automatic daily combat inside a grand strategy game
Numeric source: two community GitHub mirrors of the shipped `common/defines/00_defines.lua`, Killeritch (2,223 lines, carries `PLAYER_ORDER_PLANNING_DECAY`) and UssrLion (1,235 lines, does not); which is newer is not stated. Also Killeritch's `00_terrain.txt` and `units/infantry.txt`. Both mirrors are undated; values may lag the current patch [V2 raw.githubusercontent.com/Killeritch/Hearts-of-Iron-IV/master/common/defines/00_defines.lua ; .../UssrLion/Hoi4-defines/master/00_defines.lua]. v1's "Jan 2024 patch" is withdrawn (see log).

| id | val | how |
|---|---|---|
| F1 | YES | Infantry battalion: manpower 1000, 100 infantry equipment, `training_time` 90 (days [M]) [V2 Killeritch units/infantry.txt] |
| F2 | YES | Division = grid max 5x5 regiments + 1x5 support; corps commander and field marshal each cap at 24 divisions, marshal 5 armies [V2 defines] |
| F3 | YES | Battle plans; planning bonus gained over time [V2 defines] |
| F4 | PART | Manual orders lose planning 8x faster than normal decay [V2 defines] |
| F5 | NO | No auto-resolve toggle [M] |
| F6 | PART | Fort penalty and river-crossing penalties; no siege mechanic [V2 defines; "no siege" M] |
| F7 | YES | Supply grace, out-of-supply attrition, speed and org-regain penalties [V2 defines] |
| F8 | YES | Encirclement penalty, zero-org speed penalty [V2 defines]; retreat at 0 org [M] |
| K1 | YES | Province movement; no classic ZOC [M] |
| M3 | YES | Casualties, equipment loss persist [M]; attrition equipment loss chance in defines [V2] |

Mechanics worth knowing (defines key = value, Killeritch unless noted):
- **Width**: `BASE_COMBAT_WIDTH` 80, `ADDITIONAL_COMBAT_WIDTH` 40 (both mirrors). Terrain scales it: forest -0.20, hills -0.33, mountain -0.66, jungle and marsh -0.25, plains, urban and desert none, so forest ~64, hills ~54, mountain ~27 [V2 terrain file]. Over-width: `COMBAT_OVER_WIDTH_PENALTY` -2 "per %", max -0.33 "when you cant join no more". Battalion widths: infantry 2 [V2 infantry.txt]. [CONTESTED across versions] Wargamer (updated 5 May 2021, about 1.11): "80 for almost all terrain", changed to 75 (mountains) to 96 (urban), plains 90 [V2 wargamer.com/hearts-of-iron-4/update-combat-width]; eip.gg (14 Apr 2025) tabulates plains 70 (+35), forest 60, mountain 50, urban 80 (+40) [V2 eip.gg/hoi4/guides/best-combat-width]. Current vanilla widths `?`.
- **Stacking and flanking**: stacking penalty starts at 8 divisions (+4 from directions), -0.02 per division; `MULTIPLE_COMBATS_PENALTY` -0.5 on a defender attacked from several directions; flanking needs 3 attacking provinces; river crossing -0.3 small, -0.6 large; `BASE_FORT_PENALTY` -0.15; night attack -0.5.
- **Planning**: `PLANNING_GAIN` 0.02, `PLANNING_DECAY` 0.01, `PLAYER_ORDER_PLANNING_DECAY` 0.08, `PLANNING_MAX` 0.3 "can get more from techs". [CONTESTED across versions] UssrLion mirror has `PLANNING_MAX` 0.5 and no player-order decay. Time unit of gain/decay not stated in the file (per day [M]). So v1's dismissed "~30% cap, ~2% per day" figure matches the Killeritch file; the other mirror says 50%.
- **Supply**: troops carry 72 hours (`SUPPLY_GRACE`); worst penalty reached after `MAX_OUT_OF_SUPPLY_DAYS` 30: attrition 0.3, speed -0.8, org regain -0.3; `COMBAT_SUPPLY_LACK_IMPACT` -0.33; non-core supply speed -0.5; infantry battalion `supply_consumption` 0.07; `ATTRITION_EQUIPMENT_LOSS_CHANCE` 0.1 (scaled by attrition, cut by reliability).
- **Org and encirclement**: infantry battalion `max_organisation` 60, `max_strength` 25, `default_morale` 0.3; `ENCIRCLED_PENALTY` -0.3 "completely encircled"; `ENCIRCLED_DISBAND_MANPOWER_FACTOR` 0.2 (manpower returned when an encircled unit is disbanded); `ZERO_ORG_MOVEMENT_MODIFIER` -0.8; combat dice: org 4, strength 2, damage modifier 0.05 each.
- Closest to "set intent, let the engine resolve" at campaign scale, but aggregate (width, org, softness/hardness), not spatial.

---
## Cross-game observations (corrected)
- All four give a pre-battle intent step (deployment, battle plan, orders); Valoria's `march` hands the engine armies "built almost entirely from defaults" (F2/F3 gap, tutorial §0).
- Battle-to-campaign persistence (M3) is in all four, not only Total War and Ultimate General as v1 said: FoG2 Medieval carries experience, elan and recruitment points between battles; HOI4 carries casualties and equipment loss. Valoria's M3 for battle is unobserved in the control run (baseline above).
- Supply/attrition (F7) is numeric in HOI4 (above) and present but thin in Rome II; FoG2 has only ammunition; Valoria's battle path has none.
- Sieges (F6): Total War has campaign siege states and assault battles; FoG2 treats walls as terrain with POA bonuses (nearest to Valoria's WALLS row, DR +3).
- Army-level break: FoG2 60% routed or dispersed; Valoria 60% of troops in routed subunits (plus hp < 100 for one subunit) - the same shape.

## Still unknown
- UG officer ratings, flank multipliers, frontage; UG Civil War recruitment, auto-resolve and supply (F1, F2, F5, F7). Tried: store page, Steam thread, Wikipedia; Fandom 403. Settle with: a Steam guide or Game-Labs forum post, or the Civil War manual.
- WH3 and 3K unit upkeep numbers, 3K supply/attrition, WH3 army-size cap, Rice Garrison +15%. Tried: Fandom (402), Total War wiki (generic page). Settle with: DB-table dump (`main_units`) or an in-game check.
- Whether the WH3 auto-resolve variables keep the WH2 defaults. Settle with: WH3 DB tables or a WH3 mod thread.
- Current vanilla HOI4 terrain widths and over-width formula; planning bonus per-day unit. Tried: Paradox wiki (challenge), mirrors (undated). Settle with: a dated mirror of `00_terrain.txt` or the wiki table.
- TW F4 pause, F8 pursuit details, B3/B4 detail (M); HOI4 F5, K1 (M).

## Sources
- Total War: https://r2enc.totalwar.com/en/manual/single-player/ (pages 0016, 0017, 0018, 0019, 0020, 0021, 0026, 0033, 0075, 0076, 0077, 0087); https://r2encv2.totalwar.com/en/manual/single-player/0018_enc_page_campaign_play_military_stances/index.html ; https://steamcommunity.com/workshop/filedetails/discussion/1954849209/2659871851778938275 ; Steam app 1142710 threads 3790380616225869062, 3832045251561220120, 4697910068985751182, 3827536762634797868, 3781372783242014093 ; https://steamcommunity.com/app/4700/discussions/0/1735468693708609844/ ; https://www.gamepressure.com/download/medieval-ii-total-war-v12-eng-patch/zf3c7b ; https://raw.githubusercontent.com/FeralInteractive/romeremastered/main/documentation/data_file_guides/EDU.md
- FoG2: https://ftp.matrixgames.com/pub/FieldofGloryIIMedieval/FOG2%20Medieval%20Manual%20EN%20EBook.pdf ; https://forum.slitherine.com/viewtopic.php?t=108342 ; https://forum.slitherine.com/viewtopic.php?p=668617 ; https://forum.slitherine.com/viewtopic.php?p=708145 ; https://forum.slitherine.com/viewtopic.php?p=927225 ; https://www.magicgameworld.com/?p=125650
- Ultimate General: https://store.steampowered.com/app/306660/ ; https://steamcommunity.com/app/306660/discussions/0/1457328392108109279 ; https://en.wikipedia.org/wiki/Ultimate_General:_Civil_War
- HOI4: https://raw.githubusercontent.com/Killeritch/Hearts-of-Iron-IV/master/common/defines/00_defines.lua ; https://raw.githubusercontent.com/UssrLion/Hoi4-defines/master/00_defines.lua ; https://raw.githubusercontent.com/Killeritch/Hearts-of-Iron-IV/master/common/terrain/00_terrain.txt ; https://raw.githubusercontent.com/Killeritch/Hearts-of-Iron-IV/master/common/units/infantry.txt ; https://www.wargamer.com/hearts-of-iron-4/update-combat-width ; https://eip.gg/hoi4/guides/best-combat-width/ ; https://steamcommunity.com/sharedfiles/filedetails/changelog/2559317737?p=10
- Repo (read-only): /home/user/ttrpg/proposals/2026-10-22-system-description/2026-10-22-system-description-05-t04-mass-battle.md ; engine/season/loop/resolve.py, loop/sides.py, tests/test_march.py ; control re-run via `engine.season.harness`.
