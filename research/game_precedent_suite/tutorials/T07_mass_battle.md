# T07 Mass battle and campaign war: how each game is played

Tag key: [V3 url date] page body read this session; [S3 url] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED] sources disagree; [V2 ...] v2 table (not re-opened). Order: Total War (three titles), Field of Glory II: Medieval, Ultimate General (two games), Hearts of Iron IV. Not compared to Valoria.

## Total War: Warhammer III, Total War: Three Kingdoms, Medieval II (one combined section)

### Total War (WH3 / Three Kingdoms / Medieval II) - facts line
Creative Assembly / SEGA; turn-based campaign map that hands off to real-time battles. Versions: **WH3** released 2022-02-17 [V3 https://en.wikipedia.org/wiki/Total_War:_Warhammer_III]; current patch 9.0.4 on 2026-10-15 [V3 Steam news API app 1142710, item "Patch 9.0.4"]; assumed: Immortal Empires, Normal difficulty. **3K** released 2019-05-23 [V3 https://totalwar.fandom.com/wiki/Total_War:_Three_Kingdoms, wiki API]; latest patch in the Steam feed is 1.7.2 (2023-01-19) [V3 Steam news app 779340]; assumed Romance mode. **M2TW** released Nov 2006 [V3 Wikipedia]; official manual build 2006-09-27 [V3 https://www.segaretro.org/images/3/33/MedievalII_Steam_manual.pdf]; assumed Grand Campaign. Sources: M2TW = official manual (strong); WH3/3K = community wiki pages read via the Fandom MediaWiki API (undated revisions) plus a Sept 2026 CA beginner post (medium); in-game tutorial scripts not read [M]. One session: a campaign takes "days, or even weeks" [V3 M2TW manual p8-9]; a single turn plus its battles is minutes to an hour [M].

#### 1. Setup choices
| choice | options | changes |
|---|---|---|
| Campaign (WH3) | The Lost God (short tutorial prologue), The Realm of Chaos, Immortal Empires (mega-map), plus two small ones [V3 totalwarwarhammer.fandom.com/wiki/Turn, wiki API] | Map size and rules; Immortal Empires is the flagship, available to every WH3 owner [V3 Steam news 2026-09-25] |
| Faction / Legendary Lord (all three) | WH3: race, faction, Legendary Lord; each race has its own mechanics [V3 wiki Turn]. 3K: warlord with a hero class (Commander, Vanguard, Sentinel...), unique resource and buildings; Cao Cao then Liu Bei suggested for beginners, Sun Jian harder [V3 PC Gamer guide, Steam news 2019-08-02]. M2TW: 17 factions [V3 Wikipedia] | Start position, units, special mechanic. CA recommends Boris Todbringer to WH3 beginners [V3 Steam news 2026-09-25] |
| Difficulty | WH3: campaign 5 levels, battle 4, set separately; Easy gives you bonuses, Hard+ gives AI cheaper upkeep and recruits; Legendary forbids manual saves and orders while paused [V3 wiki Difficulty]. M2TW: Difficulty (AI strength and diplomatic offence) and Battle Difficulty [V3 manual p9] | AI economy vs AI battle skill are separate dials |
| 3K mode | Romance (heroes with superhuman strength, duels, hero abilities) or Records (hero abilities off, historical bodyguard units) [V3 fandom Hero, Battle] | Battle feel; campaign systems are the same |
| M2TW options | Short or long victory condition; advice level (Only Vital Info / Get Me Started / Tell Me Everything); Manage All Cities; No Battle Time Limit; Show CPU Moves [V3 manual p9] | How much help, how much micromanagement |

#### 2. The loop
Clock: a turn is a pause-able planning phase with no timer; 3K advances one Season per turn [V3 fandom Campaign]; M2TW turn length is not in the manual `?`; WH3 turn length not established `?`. Cycle:
1. Turn opens; events and missions appear (M2TW: event icons; missions are optional, have turn limits, failing may carry a penalty) [V3 manual p11-12].
2. Manage: recruit, build, tax, cut upkeep (disband idle units), spend skill points, handle public order [V3 manual p11; wiki Money].
3. Move armies and agents with movement/action points; pick a stance (WH3: March, Encamp, Raiding, Ambush) [V3 wiki Stances].
4. Contact: right-click an enemy army or settlement; the pre-battle panel shows a strength comparison and projected result; choose Fight, Auto-resolve (3K calls it Delegate) or Withdraw [V3 manual p21, p47; fandom Battle].
5. Real-time battle: deploy (attacker first; defender sees it; no deployment if ambushed), fight with pause and time controls; win by killing or routing all enemies, or in a siege by holding the central square/capture points [V3 wiki Battles; manual p48; fandom Siege].
6. Post-battle: result screen, then choices (section 3) and replenishment.
7. End Turn: every AI faction moves; upkeep is deducted; recruits arrive (M2TW: "the following turn"; WH3: 1-4 turns) [V3 manual p28; wiki Recruitment]. Automated: AI turns, replenishment, attrition, population/public order, auto-resolve, garrisons that defend themselves.

#### 3. The choice menu
| choice | cost | effect | when |
|---|---|---|---|
| Recruit units (constant) | money now plus per-turn upkeep; slots/pools limit it | WH3: a Lord recruits up to 3 units a turn, 1-4 turns each, cannot move while recruiting; 3K: units added to a general's retinue, bought only in owned territory; M2TW: settlement slots, regional unit pools that refill, units arrive next turn [V3 wiki Recruitment; fandom Army; manual p28] | every turn |
| Raise a new army / lord (frequent) | money; WH3 lords come from settlements, M2TW only a General can govern or hire mercenaries, 3K army cap limits count [V3 wiki Armies; manual p14, p24; fandom Army] | a second front | early and mid |
| Hire mercenaries (M2TW, occasional) | immediate but costlier; a General outside a settlement [V3 manual p20] | skip the queue | emergencies |
| Build / upgrade (constant) | money, queue slots | unlocks units, income, order | every turn |
| Tax and public order (frequent) | unrest | WH3 per-province tax toggle; M2TW tax rate; 3K faction support after conquest [V3 wiki Money; manual p46; fandom Campaign] | after conquest |
| Disband surplus (frequent) | lose units | cuts upkeep; in WH3 an empty treasury at end of turn causes desertion [V3 wiki Money] | when income < 0 |
| Move / stance (constant) | movement points | WH3 Encamp: attrition immunity and global recruitment at a movement cost; March: range but ambush-prone [V3 wiki Stances]; M2TW woodland ambush [V3 manual p21] | every turn |
| Attack: fight vs auto-resolve (constant) | your time vs worse results | M2TW auto-resolve "casualties may be heavier" and your General can die; 3K Delegate "ignores many possible player inputs"; WH3 odds are shown beforehand and can be wrong [V3 manual p21; fandom Battle; wiki Autoresolve] | each contact |
| Siege (occasional) | turns of supplies, build points | M2TW: build ladders, rams, towers or hold the siege to starve defenders [V3 manual p57-58]; 3K: besieged commandery is cut from food [V3 fandom Siege] | walled targets |
| Agents / heroes (frequent in M2TW, selective in WH3) | recruit cost, capacity | M2TW: Priests, Diplomats, Princesses, Spies, Assassins (act of war), Merchants (trade) [V3 manual p14-15]; WH3: heroes move freely, join armies, are bound by "hero capacity", can be wounded or killed [V3 wiki Heroes]; 3K heroes are generals; spies can join foreign courts [V3 PC Gamer, Steam news] | scouting, sabotage, diplomacy |
| Diplomacy (frequent) | relations | treaties, trade, WH3 confederation as conquest without battle [V3 wiki Turn] | always |
| Post-battle captive option (every won battle) | small | WH3 per race, e.g. execute (+leadership or +XP), pardon/ransom (treasury, but -5% replenishment), venerate/force labour (extra replenishment); M2TW: ransom, release or execute prisoners (chivalry or dread) [V3 wiki Post-battle options (TWW3); manual p56] | after every victory |
| Settlement option (every capture) | public order | WH3: Occupy, Loot and Occupy, Sack, Raze (race variants) trade treasury against order and building damage [V3 wiki Settlement options]; M2TW and 3K options `?` (not in the M2TW manual text) | after a siege |
| Missions / court / skills (occasional) | none | optional rewards; 3K court posts and faction rank [V3 fandom Campaign] | between wars |

Per-title differences (what changes between the three):
| aspect | WH3 | Three Kingdoms | Medieval II |
|---|---|---|---|
| Army | one Lord plus 1-20 units; heroes join freely [V3 wiki Armies, Heroes] | up to 3 generals, each with a retinue of up to 6 units; generals appear as hero units in Romance [V3 fandom Army, Battle] | one General (or Captain) plus up to 20 units [V3 manual p21] |
| Recruit | Lord recruits; Encamp unlocks costlier "global recruitment" outside territory [V3 wiki Recruitment] | per retinue by general class; units start low and muster; swap a unit without disbanding [V3 fandom Army] | settlement slots and refilling pools; mercenaries for a General in the field [V3 manual p20, p28] |
| Upkeep | per unit, lord, hero; extra lords raise all upkeep (Supply Lines) [V3 wiki Money] | per-unit seasonal upkeep plus military supplies; low supply means attrition [V3 fandom Army] | per-turn unit upkeep; crusading armies pay none [V3 manual p46, Crusades text] |
| Agents/heroes | capacity-limited heroes, lords with skill trees [V3 wiki Heroes, Lords] | heroes are generals with classes; spies infiltrate courts [V3 fandom Hero; PC Gamer] | six agent types plus family-tree Generals who govern [V3 manual p13-15] |
| Battle | deploy attacker first; reinforcement timer in WH3; Winds of Magic [V3 wiki Battles] | ambush, encampment and siege capture-point battles; duels in Romance [V3 fandom Battle, Siege] | attacker timer; siege won by holding the central square [V3 manual p48, p57] |
| Auto-resolve | outcome tier shown before; losing units flash red [V3 wiki Autoresolve] | "Delegate": balance bar, projected casualties, advisor predictions [V3 fandom Battle] | Balance of Power odds; heavier casualties, General at risk [V3 manual p21, p47] |
| After battle | per-race captive option, then settlement option (Occupy, Loot, Sack, Raze) [V3 wiki] | captives and settlement options `?` | prisoner ransom, release or execute [V3 manual p56] |

#### 4. First hour, step by step
1. Do the tutorial first: WH3 The Lost God; M2TW "The Norman Conquest" prologue (Battle of Hastings, then campaign lessons including a city and a castle siege) [V3 manual p7; WH3 wiki Turn; Steam news 2026-09-25].
2. Choose a beginner-recommended faction (section 1) and leave difficulty on the default; M2TW offers three advice levels, from Only Vital Info to Tell Me Everything [V3 manual p9].
3. Read the first mission (M2TW: take a nearby rebel settlement within a set number of turns) [V3 manual p12].
4. Check treasury and income before anything else; WH3's wiki calls upkeep "the main factor which reduces your income", and the M2TW manual lists disbanding surplus units as a money tip [V3 wiki Money; manual p46].
5. In each settlement, fill the construction queue and recruitment queue (M2TW: the roster scroll lists empty queues) [V3 manual p11].
6. Recruit infantry first; keep a mix of spears, missiles and cavalry [V3 manual, Forming Armies, p17-18].
7. Merge units into one army (M2TW: General with highest Command leads; max 20 units) and move toward the weakest neighbour; note terrain, because the campaign terrain becomes the battle map [V3 manual, Merging Armies / Picking Your Ground, p18-21].
8. On contact, read the strength bar and projected result; if clearly favourable, fight; check which units auto-resolve would lose (WH3 unit cards flash red) [V3 wiki Autoresolve].
9. In the battle, deploy inside your coloured zone (an attacker deploys on the side it approached from; an ambushed army cannot deploy), then start and use pause [V3 manual p48; wiki Battles].
10. After winning, pick the captive option, then the settlement option; occupying lowers public order for turns [V3 wiki Settlement options].
11. Garrison the conquered town and watch public order (3K: faction support starts negative) [V3 fandom Campaign].
12. Send a diplomat/hero to scout or seal trade rights early [V3 manual p46].
13. End turn; read events; repeat until the first mission is done.

#### 5. What changes later
More lords and heroes (WH3: each extra lord raises every army's upkeep, "Supply Lines", except for a few races) [V3 wiki Money]; 3K faction ranks toward Emperor, army cap grows with rank and administrators, court posts and generals' relationships [V3 fandom Campaign, Army]; M2TW Papacy and crusades, Mongol, Timurid and Black Death events, gunpowder from the 13th century [V3 Wikipedia]. Multi-front wars and siege logistics (3K military supplies, attrition when out of friendly territory) [V3 fandom Army].

#### 6. Failure and ending
Bankruptcy (WH3: public order falls, unpaid troops desert) and lost settlements/armies; M2TW rebellion by generals or cities if loyalty is neglected [V3 wiki Money; manual p46-47]. Win: M2TW short or long campaign conditions (factions vary) [V3 manual p9]; 3K reach Emperor rank and defeat the other emperors [V3 Wikipedia]; WH3: one tips page names "Faction" and "Domination" victories [V3 https://www.ggrecon.com/guides/total-war-warhammer-3-tips/ 2022-02-18; page has an error, see section 8] `?`. Not recoverable after elimination; a lost battle can be recovered strategically (dead lords: WH3 forces a new lord) [V3 wiki Armies].

#### 7. Consequential vs cosmetic choices
- Faction/lord pick: strongest single choice in all three (unique resource, hero class, start position) [V3 PC Gamer].
- Economy and upkeep management: the manual's money tips and WH3 desertion rule make this the binding constraint [V3 manual p46; wiki Money].
- Fight versus auto-resolve: consequential on battles you could lose; the games themselves warn auto-resolve is worse [V3 manual p21; fandom Battle].
- Post-battle captive choice: small, race-bound numeric nudges (XP, replenish, treasury); likely low-stakes `?` (my judgment, no community source).
- 3K duels and hero abilities exist only in Romance mode; Records mode removes them [V3 fandom Hero].

#### 8. Open items
- Not established: WH3/3K/M2TW per-unit upkeep numbers (v2 E6), WH3 turn length, 3K and M2TW settlement-capture options, 3K captive options, M2TW turn length.
- v2 R6 F1/F2 filled: WH3 army 1-20 units; 3K army up to 3 generals x 6 units; M2TW 20 units per army [V3 wiki Armies; fandom Army; manual p21].
- v2 F7 filled: 3K military supply/attrition is real (supply bar, attrition when unsupplied); WH3 attrition from corruption, climate and rough terrain [V3 fandom Army; wiki Armies].
- v2 F5: WH3 formula still unpublished; M2TW manual says only that tactical skill is ignored, casualties may be heavy and a General cannot be protected.
- Attachments: no uploaded document mentions Medieval II, Warhammer or Total War: Three Kingdoms (the "Romance of the Three Kingdoms" hit at e3f9f19a:51 is Koei's game, not this one; grep -i for the title variants). Rome II claims (e3f9f19a:80-92, 196; 89a3a060:127) concern a title outside this batch and are unchecked. e3f9f19a:248 ("auto-resolve exists to manage the load and removes the payoff in doing so"): SUPPORTED for these three titles by the M2TW manual p21 and 3K Delegate text. 62dd3fd3:590 (Total War as campaign<->battle scale shift): SUPPORTED.
- GGRecon's WH3 tips page says WH3 money is "Favour"; WH3 wiki says Favour is only the name for certain Chaos races, so treat that page as unreliable [CONTESTED, minor].

## Field of Glory II: Medieval

### Field of Glory II: Medieval - facts line
Byzantine Games / Slitherine (Matrix Games published the manual); turn-based tactical wargame on a SQUARE grid (8 facings), with a chain-of-battles campaign wrapper and no strategic map. Version relied on: the official 227-page manual PDF, InDesign build 2022-07-25 [V3 https://ftp.matrixgames.com/pub/FieldofGloryIIMedieval/FOG2%20Medieval%20Manual%20EN%20EBook.pdf 2022-07-25]; this section is built from that manual (read in full text this session). Assumes single player, Custom Battle then Sandbox Campaign, default "Knight" difficulty. One session: a battle ~? (manual gives no length; battles carry a turn limit) [M: 1-2 hours for a medium battle]; a 3-battle campaign is therefore several hours [M].

#### 1. Setup choices
| choice | options (real ones) | what it changes |
|---|---|---|
| Mode | Tutorial scenarios; Quick Battles ("Fight Now!" = random); Custom Battle; Epic Battles (historical, most playable from either side); Campaigns (Sandbox, or 4 preset: Angevin Empire, Northern Crusades, Mongol Invasion of Europe, Alexander Nevsky) [V3 manual §3, §4, §6, §7.2] | Armies, map and scenario fixed (Epic), random (Quick) or chosen (Custom) |
| Army lists | 19 national chapters, e.g. France, Germany, England, Scotland, Wales, Ireland, Teutonic Knights, Poland, Lithuania, Russia, Hungary, Cumans, Mongols (manual §2); dated lists, sorted A-Z / by date / west-to-east, date and geography filters, "Pot Luck" [V3 §5.1] | Which troop types you can buy |
| Allies | optional ally list, historically permitted, a minority of the force [V3 §5.2] | Extra troop types; allies need not deploy under an ally general in custom battles |
| Scenario type | Open Battle; Reinforcements (own/enemy); Send Flank March; Rearguard; Advance Guard; Remove the Head; Escort Baggage; Own/Enemy Side Defending; Relieve Besieged Fortress (and enemy twin); Ambush (own/enemy); two "Enemy Overconfident" SP variants [V3 §5.3] | Win/loss condition (hold till nightfall, kill the C-in-C, save the baggage) and whether reinforcements or ambushes arrive |
| Force size, map size, map type | Very Small / Small / Medium / Large / Very Large, or Advanced (turn limit, width, height, size per side); map: Agricultural, Hilly, Wooded, Mountains, Steppe, Desert, Tropical, Marshy, Plains, with N. European / Frozen / Mediterranean / Middle-Eastern variants, "Pot Luck" [V3 §5.4-5.8] | Points budget, board width, how much cover/hills/woods exist |
| Force selection | Computer picks, or you tailor within limits (tailoring gives a slightly smaller force) [V3 §5.7] | Your composition; in Custom you can toggle Stakes/Field Fortifications off to lower cost [V3 §8.2] |
| Difficulty | Sergeant, Knight (default, most even), Baron, Duke, Prince, King [V3 §21.1] | Only the size of the force you get (plus slight troop quality at the extremes); the AI does not cheat on combat or dice [V3 §21.1] |
| Campaign wrapper | Focus Default / Focused / Duel; 3, 5, 7, 9, 11, 13 or 15 battles; first and last battle size; difficulty Static or Progressive (+1 level across the whole campaign) [V3 §7.1] | Who else attacks you, length, and how fast battles grow |

#### 2. The loop
Clock: alternating player turns ("I go, you go"), each with a turn limit; per-unit action points (AP), open ground 4 AP straight / 6 diagonal [V3 §8.3, §11.1]. Battle cycle:
1. Force selection (buy units to the points cap; "Autofill", "Autodeploy") then Deployment inside highlighted areas (light troops get more room), set facings, switch units between commands [V3 §8.2, §10].
2. Start of your turn: eligible Disrupted/Fragmented/Routed units test to rally automatically (a unit with a general always tests); command range is fixed at this moment [V3 §9.1, §14.3].
3. You issue orders in any sequence: Move, Turn, Fall Back, Form Square, Shoot (must be ordered, your turn only), Charge (click twice; tooltip shows Win:Draw:Lose odds from 1000 sample resolutions), Fight Melee for combats already joined, Move General, Dismount, Stakes, War Wagons [V3 §11, §11.11, §11.13.1].
4. Press End Turn (confirm). Any melee still "due" is resolved automatically; you cannot dodge a melee round by not clicking it [V3 §11.14].
5. Enemy AI plays the same sequence; combats and cohesion tests (2d6, §14.2) resolve by dice, while push-backs follow a fixed cadence (every other "lost badly" result if the unit faces orthogonally, every third if diagonally, §13.4) and break-off is decided by the AI (§13.5) [V3 §13.3-13.5, §14].
6. Repeat until a side "breaks" (60% of original troops routed or dispersed; or 40-59% with the enemy 25% lower) or the turn limit ends it [V3 §18].
Interrupts: flank-march arrivals and ambushes (all enemy units take a cohesion test when an ambush arrives) [V3 §5.3.13]. Automated: all dice, rallies, pursuit, routers' moves, ZOC enforcement, rout % scoreboard. Campaign: after each battle the Campaign Stage screen opens (replay/retreat/recruit/garrison/strategic choice), then the next generated map [V3 §7.3].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Move / Turn (constant) | AP; turns of 46-90 degrees cost 8 AP, larger turns cost all AP [V3 manual, Turns text] | Positioning; leaving ZOC edges only | every unit, every turn |
| Charge (constant) | needs AP to reach target square; target within 45 degrees of front; ZOC limits | Impact combat now, melee next turn; flank/rear charges hit hard (an automatic cohesion drop, once per turn; the +200 net POA and +50 minimum figures are v2's reading of the same rule) [V3 §11.13 flank text; V2 R6] | the decisive moment of each unit |
| Fight Melee (constant) | none (auto-resolves at End Turn anyway) | Resolves a continuing melee round | each turn units are locked |
| Shoot (constant for archers) | ammo: 5 shots at full effect then half [V3 §11.11.5] | Casualties and cohesion pressure; best at short range, full arc, stationary | every turn with a target; concentrate on one unit [V3 §23.1.3] |
| Fall Back | 1-2 squares; cohesion test if within charge reach of a non-light enemy [V3 §11.6] | Disengage | when losing or protecting a Fragmented unit |
| Form Square | units with >=25% pike etc. [V3 §11.7] | Immune to flank/rear, cannot charge | vs cavalry, rare |
| Move General | once/turn to a unit within 4 squares, not if in melee or pursuing [V3 §9.4] | +50 POA and +1 cohesion nearby in melee; rally help; risk of death | frequent |
| Switch Command | deployment only [V3 §11.15] | Re-assigns a unit to a general | setup only |
| Stakes / Deploy War Wagons | if the army has them [V3 §11.18-11.21] | Static defence | rare, army-specific |
| Retreat (briefing panel) | concede the battle [V3 §8.4.2] | Ends it as a loss | rare |
| Campaign: Review Army / garrison | points saved by leaving units in garrison fund recruits [V3 §7.6] | Reshape next army | every stage |
| Campaign: Strategic decision | choose one of two options affecting next battle [V3 §7.7] | Content of options not specified in manual `?` | a few times per campaign |
| Campaign: Replay stage | lose the stage's result (both scores recorded) [V3 §7.9, §7.12] | Re-roll the battle on a new map; may change decisions | after a loss or a poor win |

#### 4. First hour, step by step
1. Main menu: choose Tutorial; the manual says new players should play through it first (movement, shooting, close combat, morale, troop interactions); its scenario list is not in the manual `?` [V3 §3.1-3.2].
2. Leave Settings alone: the manual recommends default settings (Knight difficulty) for new players [V3 §3.1, §21.1].
3. Battles > Quick Battles: pick your side, the enemy side, the conflict; leave size at default "small"; Create [V3 §4].
4. In force selection (if shown) hit Autofill, then optionally swap units; hover each unit to read quality, armour, capabilities [V3 §8.2, §8.4].
5. Deploy: leave "Autodeploy" or drag units; keep units near their general (select the general, press 3 to show command range) [V3 §9, §10].
6. Open the briefing panel: read the victory conditions; note the turn limit on End Turn [V3 §8.4.2-8.4.3].
7. Turn 1: press TAB (Next Unmoved) to cycle units; select one and read the red/yellow ZOC marks and green rout% at top left [V3 §8.4.1, §8.4.4].
8. Move the line forward as one block; avoid leaving gaps or exposed flanks ("VERY bad" to be charged in flank) [V3 §11.13.5, §30.1].
9. Press B (Next Unshot) and shoot with every archer; stack fire on one enemy unit [V3 §8.4.4.2, §23.1.3].
10. End Turn; watch the enemy turn; open the Combat Log (C) to see why each round went as it did [V3 §8.4.4.7].
11. When an enemy unit is within reach, click a unit, then Charge twice, reading the odds tooltip first; favour matchups with Points of Advantage [V3 §11.13.1, §23.1.4].
12. Put the general into the combat that matters (+50 POA) only if it is at least even or critical; he cannot command while in melee [V3 §30.1].
13. Keep a reserve; rally shaken units by moving a general to them [V3 §23.1.1, §30.1].
14. When the enemy hits 60% routed the battle ends; use Review Battlefield [V3 §18].
15. Next: several Quick Battles, then Custom Battle with larger armies, then a 3-battle Sandbox campaign [V3 §3.1].

#### 5. What changes later
Larger sizes and allies; scenario types with flank marches, ambushes and relief of sieges; stakes, field fortifications, war wagons and Carroccio (Standard Wagons count as 4 heavy-infantry units in rout%) [V3 §18.1]. In campaigns the army persists: units gain experience and elan, may be promoted (Raw Spearmen to Spearmen); unit advancement is slower in longer sandbox campaigns; battles scale between first and last size; extra battles may be added by results [V3 §7.1.3, §7.4]. Pressure ramps by size and by Progressive difficulty; Prestige falls and rises, and low Prestige raises the chance of baron or populace revolts [V3 §7.12].

#### 6. Failure and ending
Battle loss = your army breaks, time limit with the scenario's tiebreak, or Retreat [V3 §18, §8.4.2]. In a campaign you may be offered a retreat to join reinforcements and fight the same enemy minus its losses; otherwise you replay the stage; replays do not forbid campaign victory [V3 §7.3, §7.11]. Win = meeting the victory conditions in every stage; the score averages per-battle scores and counts replays [V3 §7.12]. Fully recoverable by design; irrecoverable loss is limited to a general (may not survive to fight again) [V3 §9.3].

#### 7. Consequential vs cosmetic choices
- Unit matchups and Points of Advantage (100 net POA ~ 33% modifier, capped at 200 net) decide fights; "a powerful unit can lose to a much weaker one" [V3 §13.2, §23.1.4].
- Flank/rear exposure and cohesion: the manual says breaking cohesion matters more than casualties [V3 §23.1.2, §11.13.5].
- Campaign losses: ~15% losses holds parity; more makes the next battle harder [V3 §7.5].
- Difficulty is only a points handicap; the dice are unbiased [V3 §21.1].
- Cosmetic/flavour: naming units, banners, map-type variants within a region largely set terrain mix not outcomes `?` (no source); community consensus on dominant army builds not established.

#### 8. Open items
- Tutorial scenario contents, typical battle length, content of "strategic decisions" and the AI-offered retreat conditions `?` (not in manual).
- v2 R6 FoG2 F1: add "number of battles can grow with results" and "strategic decision = choice between two options" (manual §7.1.3, §7.7); campaign Prestige/revolt (manual §7.12) absent in v2.
- v2 F5 NO and F7 (5 shots, half effect) re-confirmed against the same manual text (grep for auto-resolve returns nothing; §11.11.5).
- v2 F2: "difficulty only changes force size" is stated in manual §21.1 and not in v2.
- Attachment claims: no uploaded document mentions Field of Glory (grep -i of all four files returned no hit).

## Ultimate General: Gettysburg and Ultimate General: Civil War

### Ultimate General (Gettysburg / Civil War) - facts line
Game-Labs; real-time tactical battles with pause, no unit-by-unit micromanagement required. **Gettysburg**: Steam release 2014-10-16, single battle fought across up to 4 days and 3 phases a day, multiplayer included [V3 https://store.steampowered.com/api/appdetails?appids=306660 (Steam store text), 2026-10]. **Civil War**: Steam release 2017-07-14, campaign of 50+ battles [V3 same API, app 502520]; v2 recorded early access 16 Nov 2016 and final patches 1.09 (Gettysburg) / 1.10 (Civil War) from Wikipedia [not re-checked this pass, M]. Assumed: Civil War campaign, Union, default difficulty `?` (difficulty names not established). Sources: Steam store text, the fan-run UGCW wiki (read via the Fandom API, undated revisions, game version unstated), a Steam tactics guide by the player DARTIS for Gettysburg (posted 2015-10-11, updated 2016-05-28) and Steam forum threads. No manual or in-game tutorial text read, so first-hour steps below are assembled from those; a session = one battle plus the between-battle shopping, length `?`.

#### 1. Setup choices
| choice | options | what it changes |
|---|---|---|
| Which game | Gettysburg (one battle, multi-day, multiplayer) or Civil War (campaign). Forum consensus: Gettysburg is the gentler way to learn combat; Civil War is longer and has the campaign [V3 https://steamcommunity.com/app/502520/discussions/0/2998799976096532258, Dec 2020; player claims] | Scope: tactics only vs tactics plus army building |
| Side | Gettysburg: Union or Confederate army. Civil War: Union or Confederates; Union has more men and weapons, Confederates better generals (a brigade under a colonel or higher auto-gains a star) [V3 ugcw.fandom.com Playable Factions] | Resource pressure: CSA struggles to arm well |
| AI opponent (Gettysburg) | Nine AI personalities, aggressive or defensive, "no AI gameplay cheats" [V3 Steam store text] | Difficulty is the opponent's style |
| Campaign battle (Civil War) | 13 "Grand" battles you must fight and 25 optional "Minor" ones per side; winning minors can shrink or weaken the Grand battle's enemy [V3 ugcw wiki Battles]. Store lists 16 named campaign battles + 48 smaller [V3 store text]; wiki counts 38 per side, counts differ slightly [CONTESTED, minor] | Order and optional strengthening |
| Army composition (Civil War, each battle) | Corps / divisions / brigades up to a cap set by career points (Army Organization level 1: 1 corps, 2 divisions, 3 brigades, 1500 men max; level 10: 5 corps, 4 divisions, 6 brigades, 2500) [V3 ugcw wiki Career Points]; weapons; officers; supply (wagons hold up to 35,000 supplies at $1 each) [V3 ugcw wiki Unit Types] | What you fight with and for how long |

#### 2. The loop
Clock: real time with pause and speed control `[M]` (store tags "real time"); Gettysburg adds a day/phase clock: a battle lasts up to 4 days, each day up to 3 phases, with the armies' condition and map positions saved between phases [V3 Steam store text]. Battle loop:
1. Choose the battle (campaign map in Civil War, scenario list in Gettysburg).
2. Set up the army and supply, read enemy intel (reconnaissance career level determines how much of the enemy order of battle you see) [V3 ugcw wiki Career Points].
3. Deploy and start; units "act on their own initiative": re-align, switch targets, withdraw, form lines; you give orders by dragging movement arrows or drawing a defensive line; division commanders act on their own [V3 store text].
4. During the fight you watch morale, condition (fatigue), ammunition and generals' radius; you pause, redirect, rest, detach skirmishers, mount or dismount cavalry [V3 store text; DARTIS guide].
5. Battle ends on the scenario's objectives/time or when a side is beaten. Gettysburg scores Victory Points: captured objectives plus 1 VP per casualty; you win by exceeding the enemy score plus a per-map "win threshold" (e.g. 500, 1000, 3000 on Pickett's Charge), else draw or defeat [V3 steamcommunity.com/sharedfiles/filedetails/?id=533709146 DARTIS guide; multiplayer maps]. Civil War: win, draw or defeat award gold, men and reputation (most for a win) [V3 ugcw wiki Battles].
6. Between battles (Civil War): spend gold on weapons (Armory), leaders (Barracks Academy) and reputation purchases, which reset after each Grand battle [V3 ugcw wiki Battles]; spend career points; recruit or refit. Units that fought gain experience and officers rank up or die [V3 store text].
Automated: unit self-alignment, AI division commanders, supply replenished after each battle to the amount you set [V3 ugcw wiki Unit Types], morale and fatigue calculation, AI opponent.

#### 3. The choice menu
| choice | cost | effect | when |
|---|---|---|---|
| Move/attack arrow (constant) | fatigue; running costs condition | Positions brigades; "bursts" of double-quick then rest [V3 DARTIS] | continuously |
| Defensive line / hold (constant) | none | Dense lines resist charges and flank attacks but suffer more from fire [V3 store text] | every battle |
| Charge (frequent) | morale/casualty risk | Needs numbers, high morale and condition, flank or rear approach; frontal attacks on prepared units "almost always failed" [V3 DARTIS] | decisive moments |
| Withdraw / fall back (frequent) | position | Lets neighbours break a charge; a flanked unit can be repositioned [V3 Steam thread 1457328392108109279, 2017; DARTIS] | when outflanked |
| Position artillery (constant) | ammo, supply | High ground and flanks, line of sight is strict in Gettysburg; keep guns protected [V3 Steam thread; player claims] | setup and mid-battle |
| Detach skirmishers / merge brigades (occasional) | frees control | Scout, harass guns, cover flank [V3 store text; S3 forum snippets] | as needed |
| Mount / dismount cavalry (occasional) | speed vs visibility | Flanking charges and supply raids [V3 store text] | as needed |
| Supply allocation (each battle, Civil War) | gold | Ammo shortage halves reload (about -50%, wiki) [V3 ugcw wiki Unit Types] | before each battle |
| Buy weapons / leaders (each battle) | gold, reputation | Rifles over smoothbores; generals add morale and perks [V3 ugcw wiki] | between battles |
| Spend career points (after wins) | points from battles | Politics, Economy, Medicine, Army Organization, Training, Logistics, Reconnaissance, 10 levels each [V3 ugcw wiki Career Points] | after wins |
| Unit perks on rank-up (occasional) | none | Per unit type perk tiers (e.g. Marksman Training) [V3 ugcw wiki Perks] | after promotions |
| Choose minor vs grand battle (occasional) | risk | Optional minors weaken a Grand opponent [V3 ugcw wiki Battles] | campaign map |
| Between-day decision (Gettysburg, rare) | positional | Attack or defend and wait for the AI to take initiative [V3 store text] | between phases |

#### 4. First hour, step by step
1. If new, start with Gettysburg: less to manage, same combat engine (forum consensus; player claims) [V3 Steam thread 2998799976096532258].
2. Pick the Union (defence-favoured) if you want to learn the battle system [V3 Steam thread 1457328392108109279, 2017; one player's advice].
3. Read the briefing and objectives; remember victory depends on objectives and casualties.
4. Deploy infantry on crests or forward slopes in cover, no gaps; guns on high ground or on flanks [V3 same thread].
5. Keep your general within reach of the units; his radius gives morale and condition recovery [V3 DARTIS; ugcw wiki].
6. Use movement arrows for small, steady moves; do not run constantly [V3 DARTIS].
7. Concentrate fire; place a unit at an angle to shoot into an exposed enemy flank [V3 thread].
8. Watch morale and condition bars; rest battered units in cover rather than sending them forward [V3 DARTIS].
9. Do not chase retreating enemies; they return when morale recovers [V3 thread; v2 same thread].
10. After the battle (Civil War), spend gold on rifles and veteran refits; buy officers; upgrade career points [V3 ugcw wiki Career Points; forum snippet `S3`: replace smoothbores with rifles early].
11. Set supply for the next battle; capture enemy wagons when you can [V3 ugcw wiki Unit Types].
12. Take on minor battles for reputation and weakening of the next Grand battle.

#### 5. What changes later
Armies grow with career levels and reputation; enemy scaling intensifies after Antietam (forum claim, `S3`); more artillery and larger brigades; officer ranks affect how big a unit can be without efficiency loss [V3 store text; ugcw wiki Unit Skills]. Units gain skill points through use (e.g. Firearms +1 per 5 reload cycles) [V3 ugcw wiki Unit Skills].

#### 6. Failure and ending
Civil War: reputation under 20 ends the game ("fired"); under 24 gives a morale penalty [V3 ugcw wiki Reputation]. A lost battle gives least gold and men and loses reputation; continuing with a weaker army while reputation stays above 20 is my inference from the wiki, not stated. Ending: complete the campaign to Richmond (Union) or Washington (Confederate) [V3 ugcw wiki Battles]. Gettysburg's campaign-style multi-day ending and scoring are `?` (VP thresholds above are documented for multiplayer maps).

#### 7. Consequential vs cosmetic choices
- Terrain, cover and flank exposure: the store text and DARTIS guide say morale and casualties are driven by them [V3].
- Fatigue/condition management decides whether lines hold [V3 DARTIS].
- Weapons and supply (Civil War): shortage halves reload; rifles over smoothbores is advice players repeat [V3 wiki; S3 forum].
- Career points: wiki's own comments rank Economy low value and Medicine/Politics higher (fan opinion) [V3 ugcw wiki Career Points; player claims].
- Cosmetic/flavour: faction differences beyond resource level are small per wiki ("there aren't many differences") [V3 ugcw wiki Playable Factions].

#### 8. Open items
- Not established: difficulty levels, pause and order keys, in-game tutorial contents, exact flank multiplier, officer rating numbers, auto-resolve (none known), session length; whether Civil War lets you retreat from a campaign battle.
- v2 R6 section 3: F1 filled: campaign is 38 battles per side on the fan wiki (13 grand, 25 minor) vs store "50+" [CONTESTED, minor]. F5: no auto-resolve found in store text, wiki or forum; unproven `?`. F7: supply wagons and ammunition are real (35,000 max, $1 per unit, -50% reload without ammo) [V3 ugcw wiki]. F8: reputation under 20 ends the game.
- Attachments: no uploaded document mentions Ultimate General (grep -i returned no hit).

## Hearts of Iron IV

### Hearts of Iron IV - facts line
Paradox Development Studio / Paradox Interactive; real-time-with-pause grand strategy wargame; released 6 June 2016, developed by Paradox Development Studio [V3 https://en.wikipedia.org/wiki/Hearts_of_Iron_IV]. Version: live patch 1.19.3 on 2026-09-17, expansion "Thunder at our Gates" 1.19.0 on 2026-06-11 [V3 Steam news API app 394360, items "Patch 1.19.3", "Thunder at our Gates | Patch Notes"]; dev posts July-Oct 2026 discuss an unreleased economy rework (Industrial Parks, Energy, consumer goods) in open beta, which this section does NOT describe as live [V3 Steam news 2026-09-08, 2026-10-01]. Assumed: single player, a major power (Germany or Italy), 1936 start, base-game rules. One session: a 1936-1948 game takes tens of hours; a session is 1-3 hours [M]. Source quality: the Paradox wiki is blocked (Client Challenge), so most of this is built from Paradox's own Steam dev diaries (2016 and 2026) and Wikipedia; production, research and tutorial steps are partly from memory and say so [M].

#### 1. Setup choices
| choice | options | changes |
|---|---|---|
| Start date | 1936-01-01 or 1939-08-14 [V3 https://en.wikipedia.org/wiki/Hearts_of_Iron_IV] | How much peacetime you get to industrialise |
| Country | Any nation in the world; each has its own focus tree; the in-game tutorial uses Italy (a short war with Ethiopia, "up to you when and how you get involved with WW2") [V3 Steam news, Dev Diary 58, 2016-05-27] | Starting industry, neighbours, objectives |
| Ideology and government | Democratic, communist, fascist or non-aligned; fascist can go to war easily but trades less, democracies struggle to invade [V3 Wikipedia] | What wars you can start and when |
| Expansions owned | Country packs, expansions (Waking the Tiger, La Resistance, No Step Back, By Blood Alone, Arms Against Tyranny, Gotterdammerung, No Compromise No Surrender...) add focus trees and systems [V3 Wikipedia list] | Which systems exist (tank designer, plane designer, espionage...) |
| Game rules, difficulty, ironman, AI behaviour | exist but names and values not established `?` [M] | AI strength and history adherence |

#### 2. The loop
Clock: real time with pause and speed steps; the engine ticks hourly (inferred from the "Hourly Reinforce Chance" trait in V3 dev diary 41, 2016-01-22); everything below happens while you pause or while time runs. Cycle:
1. Pause, read alerts and the map; political power (PP) accrues; spend it on laws, advisors, decisions, or a national focus (each country's "focus tree"; focuses grant bonuses or trigger events) [V3 Wikipedia].
2. Production: civilian factories construct buildings, military factories and dockyards, produce consumer goods and trade; military factories build equipment on production lines [V3 Wikipedia]. Most nations start with many civilian factories tied up making consumer goods; mobilisation frees them [V3 Wikipedia]; laws are bought with PP.
3. Research slots work through technologies for equipment; doctrines are bought with army XP [V3 Wikipedia].
4. Military: design a division template, train divisions from manpower plus equipment, group them into Armies inside Theatres, give them a commander [V3 Dev Diary 41].
5. War: draw battle plans per Army (assign front line, offensive line, fall back line, garrison area); a plan accumulates a planning bonus before you execute [V3 Dev Diary 45, 2016-02-19].
6. Combat resolves automatically every hour by width, organisation, equipment, terrain, supply and air [V3 Wikipedia; v2 defines]. You override any unit at any time.
7. Interrupts: country events with options, decisions, diplomatic offers, enemy declarations, capitulation at victory points [V3 Wikipedia]. Repeat.
Automated: combat, supply, reinforcement, AI factions, AI-controlled theatres if you choose to delegate.

#### 3. The choice menu
| choice | cost | effect | when |
|---|---|---|---|
| Pause/speed (constant) | attention | turns a continuous game into decisions | always |
| Production line assignment (constant) | military factory share; a new line starts at 10% efficiency (base cap 50%); the defines' comments give 90% for changing variant and 30% for changing parent type, read here as efficiency retained [V3 defines mirror] | which equipment; shifts mid-war | weekly |
| Research (constant) | research slot (base 2 per country in the defines mirror) and time | unlocks gear, doctrine | whenever a slot frees |
| National focus (frequent) | each focus point takes a week (FOCUS_POINT_DAYS 7) [V3 defines mirror]; a typical focus is 5 points = 35 days [M] | bonuses, events, war goals [V3 Wikipedia] | when ready |
| Construction queue (frequent) | civilian factories | factories, infrastructure, forts | early game |
| Division template (frequent) | design time; new gear needs production; support slots cost to unlock (10 in the defines mirror) | a grid of up to 5x5 regiment battalions plus a 1x5 support column; changes combat width (base 80), stats, equipment per division [V3 Killeritch defines mirror, undated; Steam news 2026-05-21] | when new tech arrives |
| Battle plan edit/execute (constant in war) | planning time | guides divisions; AI acts on plan; "is specifically not allowed to be clever" [V3 Dev Diary 45] | each offensive |
| Manual override (frequent) | attention | direct orders to a division or army | encirclements, emergencies |
| Laws and advisors (occasional) | PP | mobilisation, trade, conscription [V3 Wikipedia] | peacetime build-up |
| Diplomacy and factions (occasional) | PP, tension | pacts, guarantees, factions, war justification [V3 Wikipedia] | before war |
| Justify/declare war (rare) | PP, world tension | permits attack; tension 0-100 gates actions [V3 Wikipedia] | start of each war |
| Intelligence/espionage (rare) | agency resources | La Resistance expansion [V3 Wikipedia] | optional |
| Surrender/peace (rare) | none | ends a war | end of war |

#### 4. First hour, step by step
Source for steps 1-2 only is first-party (Steam dev diary 58); steps 3-12 combine Wikipedia and memory and are tagged.
1. Start the tutorial: it is "somewhat nonlinear", starts you as Italy, links each step to wiki pages, and does not end: you may keep playing the same save [V3 Dev Diary 58, 2016-05-27].
2. The game ships an in-game browser and offline wiki [V3 same post].
3. Check the focus tree and pick a first focus; each focus takes real in-game time [V3 Wikipedia; duration M].
4. Fill all research slots; early picks are infantry equipment and industry techs [M; S3 community snippet suggests military techs for Ethiopia].
5. Open construction and queue civilian or military factories [V3 Wikipedia; M].
6. Assign military factories to a production line for the equipment your divisions use [V3 Wikipedia; M].
7. Open the Division Designer: pick regiments and support; the grid shows combat width, resource and production cost; shift-click fills a regiment with one battalion type [V3 Steam news 2026-05-21; M on early picks].
8. Train divisions; group them into an Army with a general or field marshal; a general fully commands 12 divisions in the 2016 design [V3 Dev Diary 41, CONTESTED in v2: defines say 24].
9. Draw a front line and an offensive line for the army; hover the arrow to preview steps [V3 Dev Diary 45].
10. Wait for the planning bonus to build, then execute [V3 Dev Diary 45].
11. Watch supply and organisation bars; manually override stuck divisions [V3 Dev Diary 45; M].
12. After the war, keep playing; spend PP on laws and keep research and production running [V3 Dev Diary 58].
Caution: a Steam poster calls the stock tutorial weak and others say it can stall if Ethiopia surrenders early [S3 search result summary of Steam app 394360 threads, no single URL attributable]; Wikipedia cites GameSpot that the tutorial was the only weak point [V3 Wikipedia].

#### 5. What changes later
Mobilisation, conscription and economy laws expand the factory pool; research gives larger divisions and armour; factions and subjects (autonomy system) appear; naval invasions, paratroops, air, nuclear and special projects unlock [V3 Wikipedia]. Pressure ramps with world tension and capitulation; Thunder at our Gates adds Army HQs and ship captains, and a reworked Division Designer with regimental support companies [V3 Steam news 2026-05-21, 2026-06-03].

#### 6. Failure and ending
Your country can be conquered, capitulate at victory-point loss, or break up into civil war; a supply collapse or encirclement can destroy armies [V3 Wikipedia; v2 defines]. Ending: no scripted win beyond holding on to your objectives or conquering through 1948; the game continues past the historical end `?`. Recovery: yes, through peace, rebuilding, and government in exile `?`.

#### 7. Consequential vs cosmetic choices
- Developers say economic laws have a dominant answer: "higher mobilization is (ALMOST) always a better choice" and consumer goods "purely negative ... always better to lower their %-demand" [V3 Steam news Dev Corner, 2026-07-21; dev's own framing].
- Division template and combat width: consequential (the designer now shows combat width in the grid) [V3 Steam news 2026-05-21; v2 defines].
- Battle plans: the design goal is high-level plans plus overrides; the planning bonus rewards preparation [V3 Dev Diary 45]; forum players say they often farm the bonus with a small front and manage attacks by hand because the AI mishandles pockets [S3 https://steamcommunity.com/app/394360/discussions/0/1693795812301757587, snippet only].
- Commander traits and focus tree flavour: moderate or cosmetic depending on country `?` (no source).

#### 8. Open items
- Not established: current vanilla combat-width table, research slot counts, factory numbers, tutorial scripts (YouTube beginner series "Battle Plans", "Construction", "Division Designer" exist but were not watched) [V3 Steam news 2016-05-30..06-02].
- v2 R6 F2 / HOI4: commander division caps are CONTESTED between versions: 12 divisions for a general in the pre-release Dev Diary 41 (2016-01-22) vs 24 in the defines mirrors cited by v2.
- v2 F5 NO [M]: consistent with Dev Diary 45 (manual override always allowed, system "not allowed to be clever") but not directly proven.
- v2 planning figures (0.3 cap, 0.02 gain): not rechecked; Dev Diary 45 only says cap depends on doctrine and bonus decays as the plan progresses [V3].
- Attachments: no uploaded document mentions Hearts of Iron; the Paradox references (62dd3fd3:344-452, e3f9f19a:130,575) are about EU, CK2 and Imperator, so there is no HOI4 claim to verify.
