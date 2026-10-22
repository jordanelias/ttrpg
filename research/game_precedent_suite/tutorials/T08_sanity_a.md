# T08 tutorial pass: sanity / stress / voyage games (Darkest Dungeon II, Sunless Sea, Eternal Darkness)
Tags: [V3 url date/version] read in a fetched page body this session (2026-10-22); [S3 url] search snippet only; [M] memory; `?` not established; [CONTESTED] sources disagree. Valoria is not consulted anywhere below.
Source keys. DD2w = https://darkestdungeon.wiki.gg/wiki/<Page> (action=raw, official wiki; its DD2 main page still shows version 1.05.61812 and an Outdated banner). DD2news = Steam news API appid 1940340 (latest build named in the feed: 2.04.85095, hotfix 2026-04-28). PCG = https://www.pcgamer.com/darkest-dungeon-2-tips/ (early-access-era tips). GP = https://www.gamepressure.com/darkest-dungeon-ii/beginners-guide/zaf03a (undated beginner's guide). GD = https://gamerdigest.com/darkest-dungeon-2-how-to-reduce-stress/ (undated).

### Darkest Dungeon II - facts line
Red Hook Studios; party-based roguelike RPG (real-time coach driving between turn-based fights); relied on wiki.gg pages read 2026-10-22 plus Steam patch notes up to build 2.04.85095 (2026-04-28) [V3 DD2news]; full release 8 May 2023, early access 26 Oct 2021, DLC The Binding Blade (11 Dec 2023: Duelist, Crusader) and Inhuman Bondage (27 Jan 2025: Catacombs, Abomination) [V3 DD2w Darkest_Dungeon_II]. Assumes the base mode "Confessions" (Act 1 = Denial) with the four starting heroes; the free "Kingdoms" mode is described only where it differs. One expedition = roughly 1.5 to 3 hours [M]; `?` no source found.
Orientation, first game (Darkest Dungeon, 2016): you ran a hamlet (the Estate) and sent four-hero parties into fixed dungeons with torches, food and a Stress bar of 0-200; at 100 Stress a hero became Afflicted (75%) or Virtuous (25%) [V3 DD2w Stress_(Darkest_Dungeon), Affliction, Virtue]. DD2 drops the town and the dungeon crawl for one long road to a mountain, and Stress is now 0-10.

#### 1. Setup choices
- Mode: Confessions (five acts, each one full expedition; only Denial open at first, a clear unlocks the next, and after a first clear of an act the game forces the next act) or Kingdoms (free; persistent roster on an overworld map with a day limit, sieges and Escalation; three modules: Hunger of the Beast Clan, Secrets of the Coven, Curse of the Court) [V3 DD2w Confessions, Kingdoms].
- Confession (act): sets the final boss (Shackles of Denial, Seething Sigh, Focused Fault, Ravenous Reach, Body of Work), the number of regions (Denial = Sprawl and Tangle only; Resentment onward = three regions and a Boss Trophy needed for the Mountain), Ordainment (enemy buff) rules, Flame effects, Bounty Hunter chance [V3 DD2w Confessions].
- Party of exactly four at the Crossroads, from unlocked classes. Day one: Man-at-Arms, Highwayman, Grave Robber, Plague Doctor; eight more classes unlock at the Altar of Hope (Hellion, Runaway, Jester, Leper, Occultist, Vestal, Flagellant, Bounty Hunter [hired at an Inn only]) [V3 DD2w Heroes_(Darkest_Dungeon_II)]. Each hero is generated fresh: two random quirks (one good, one bad), a Goal for the run, and a Path (default Wanderer; three more unlockable) that tilts stats and skills.
- Skill loadout per hero (five start, up to eleven with Shrine of Reflection unlocks), two trinkets, one combat item; party order matters because skills need a rank (PCG: front two ranks Man-at-Arms and Highwayman, back two Grave Robber and Plague Doctor) [V3 DD2w Heroes; V3 PCG EA-era].
- Stagecoach: upgrades bought with Candles at the Altar (slots, Wheels, Armor, pets, skins); Flame type and Pet are chosen at the first Inn and cannot be changed that run [V3 DD2w Stagecoach_Items, Pets].
- The Dam (Altar menu) run toggles: Retreat button (costs +2 Loathing and +2 Stress to all if used), selling to the Hoarder, Mountain at every Inn, extra battle modifiers, extended Act 1/2 [V3 DD2w Altar_of_Hope]. No difficulty slider in Confessions: difficulty is the act. Kingdoms has a campaign difficulty screen that sets what hero death does [V3 DD2w Heroes].

#### 2. The loop
Clock: no calendar and no hunger. Time is spatial (region by region) and measured by two dials: Flame (0-100, resets to 100 each region, drains while driving or stalling a fight) and Loathing (0-4 tears, raised by Oblivion Tear roads and some nodes) [V3 DD2w Flame, Loathing].
1. Altar of Hope: spend Candles (meta), choose a Confession, go to the Crossroads and build the party [V3 DD2w Locations_(Darkest_Dungeon_II)].
2. The Valley (fixed tutorial region: a bridge, one Gaunt road battle) ends at the first Inn, always The Torch & Crown [V3 DD2w The_Valley, Inn].
3. At each Inn: heal and de-stress (the inn's own tier), spend Mastery Points, shop, repair/equip the coach, use Inn Items, then pick the next region from two or three (each shows a modifier, a goal and a reward). The Embark screen then reveals the Relationships rolled from Affinity [V3 DD2w Inn, Relationships].
4. On the road you drive the coach in real time through a graph of nodes joined by roads (Safe, Combat, Hazardous -1 Armor, Rough -1 Wheel, Oblivion Tear +1 Loathing). Nodes and roads may be hidden; scouting reveals them [V3 DD2w Locations; V3 DD2news 2025-07-16 (driving speed option)].
5. Between your actions the game drains Flame, heals HP slowly while travelling (Wheels give +20/33/50%), rolls banter that moves Stress and Affinity, and spawns ambushes: Flame 0 = Cultists, Flame under 30 = chance of the Shambler, a stripped Wheel or Armor road = a repair battle [V3 DD2w Road_Battle, Stagecoach_(Darkest_Dungeon_II)].
6. A node opens a choice (one option per hero for Assistance Encounters and Oases, where hero quirks change the outcome) or a fight. Fights are turn-based on four ranks; order is Speed plus a hidden 0-6 roll each round; every hero has Stress, HP, Death's Door and tokens [V3 DD2w Combat_Mechanics_(Darkest_Dungeon_II)].
7. A hero reaching Stress 10 mid-fight resolves instantly into Meltdown (80%) or Resolute (20%) (Flagellant: Toxic) [V3 DD2w Stress_(Darkest_Dungeon_II)]. A hero at 0 HP is on Death's Door; each further hit risks a Deathblow [V3 DD2w Death's_Door_(Darkest_Dungeon_II)].
8. Each region ends with a mandatory fight at Oblivion's Rampart, then the next Inn; Candles for the region arrive on entering it [V3 DD2w Oblivion's_Rampart, Candles_of_Hope].
9. After the last region the Mountain: the act boss. Then back to the Altar with Candles. Automated: damage over time, banter, Flame drain, relationship rolls, autosave after every enemy turn (no manual save; only the Inn screen is not saved) [V3 GP].

#### 3. The choice menu
| verb / choice | cost | effect | when picked | frequency |
|---|---|---|---|---|
| Pick next region at an Inn | the goal may force or forbid nodes | modifier (e.g. Heavy Winds -20% max Flame, Malaise +10% Meltdown chance), goal reward (Candles, Mastery Points, trinket, coach item) | every Inn | constant |
| Use Inn Items | item price (Relics); food once per hero per region | heal, Stress down, Affinity up (10% double), region buffs; most can also lower Affinity | every Inn, before Embark | constant |
| Spend Mastery Points | MP (from fights and goals) | upgrade a hero's skill once; lost with the hero | Inn | frequent |
| Buy trinkets and coach items | Baubles | gear; Relics buy consumables | Inn, Hoarder | frequent |
| Repair / equip at the Wainwright | 8 Baubles per Wheel or Armor point | Armor gives party Block at fight start; Wheels give travel healing | Inn | frequent |
| Steer, pick fork, ram debris | Flame drain per distance; road hazards | route, loot from debris (needs a free slot) | all the time | constant |
| Enter or bypass a node | node risk | combat nodes (Resistance Encounter, Creature Den, Oblivion's Ingress, Lair) give Mastery Points, Candles, Relics and lower Loathing; others heal or loot | each junction | constant |
| Fight: skill, target, position, combat item (free action) | HP, Stress, cooldowns | the combat itself | every fight | constant |
| Assistance Encounter option per hero (Assist, Help, Inspire, Donate, Steal, Kill) | quirk-gated: e.g. Austere -15 Relics gives +45 Flame; Greedy -15 Flame gives +32 Relics | the main Flame refill; changes Affinity | when Flame is low | frequent |
| Oasis / Field Hospital / Chirurgeon's Table | Relics (disease cure 8-16; lock a good quirk 32; remove a quirk 16) | Stress -5, heal, quirk management | when hurt | frequent |
| Shrine of Reflection | a fight or puzzle | permanent hero skill and backstory unlock | when seen | occasional |
| Watchtower | a node visit | reveals the rest of the region | early in a region | occasional |
| Fight the Lair boss | up to three battles, may leave after each | a Trophy and big Candles; Trophy opens the Mountain (act 2+) | optional | once per region |
| Retreat or abandon | +2 Loathing +2 Stress (retreat); abandoning at an Inn fails the run but keeps Memories | ends the danger, ends the run | desperate | rare |
| Spend Candles (Altar) | Candles | heroes, items, coach slots, Memories (heroes persist) | between runs | constant |
| Choose the Confession | none | next boss and ruleset | run start | rare |

#### 4. First hour, step by step
1. New save: a short story prologue and the Altar of Hope, almost empty because you have no Candles [V3 DD2w Altar_of_Hope].
2. Choose Denial (the only act open). It runs only through the Sprawl and the Tangle, in either order, and needs no Boss Trophy [V3 DD2w Confessions].
3. At the Crossroads take the four starting heroes. A sound line-up from the early-access guide: Man-at-Arms and Highwayman in front, Grave Robber and Plague Doctor behind; check each hero's quirks first [V3 PCG EA-era].
4. Read each Goal and skill panel; hero Goals pay Candles (all Wanderers get 2 on reaching the second Inn) [V3 DD2w Candles_of_Hope/Earning_Candles].
5. Drive the Valley. Early-access advice: double-tap forward for auto-drive, steer with single taps, ram breakable debris (no damage, chance of food and items) and keep one inventory slot free [V3 PCG EA-era].
6. Fight the Gaunt road battle. Fights are guaranteed hits unless the enemy has a Dodge or Block token; learn ranks, Speed, damage-over-time tokens (Bleed, Blight, Burn). The game generally recommends stacking one DoT and finishing with it [V3 DD2w Darkest_Dungeon_II; V3 GP].
7. Watch Stress: banter above 3 is mostly negative and snowballs; use stress heals and crits early [V3 DD2w Stress_(Darkest_Dungeon_II); V3 GP].
8. Reach The Torch & Crown. Its Relationship chances are reduced 10% each way on the first Inn, so few bonds form [V3 DD2w Inn].
9. Spend your first Mastery Point. Early-access advice was Plague Doctor "Ounce of Prevention" (stress heal for the party); that hero was reworked in the July 2025 Steadfast Steward update, so re-check [V3 PCG EA-era; V3 DD2news 2025-07-16].
10. Use Inn Items to push Affinity up and buy a Laudanum-type stress item; the guide says use consumables freely [V3 GP; V3 PCG].
11. Choose a region from the two offered, reading modifier and goal; embark and read the Relationships panel (Blessed skills you may equip; Cursed skills are forced on you).
12. In a region take the Watchtower or a Field Hospital if shown; fight Resistance Encounters mainly for Mastery Points, but each fight costs Affinity risk and Flame [V3 GP].
13. When Flame is low, visit an Assistance Encounter and pick the option your heroes' quirks support.
14. Clear the Oblivion's Rampart (mandatory) to reach the second Inn; in Denial, the second region then the Mountain.
15. Expect to lose the first run: Candles earned still unlock heroes and items for the next one [V3 GP].

#### 5. What changes later
- Later Confessions add regions (all six regions open from Resentment: Sprawl, Tangle, Foetor, Shroud, Sluice, plus Catacombs with DLC), a Boss Trophy gate, Ordainment (more enemies buffed, in a boss-specific way), cultist buffs, the Exemplar and Antiquarian [V3 DD2w Confessions, Ordainment].
- Meta layer: the Altar of Hope fills out; once complete, Candles buy starting items, quirk rerolls and powerful node choices [V3 DD2w Candles_of_Hope]. Memories make a hero persist across runs [V3 DD2w Heroes].
- Pressure ramp inside a run: Loathing rises, Flame drains faster, enemy advantage chance rises (+20/25/33% at tear levels 1-3) [V3 DD2w Loathing].
- Kingdoms (free module series, 2025): days, sieges on inns, Escalation surges, a fatigue stat, heroes recovering by being stationed [V3 DD2w Kingdoms].

#### 6. Failure and ending
- Hero death is permanent in Confessions. Hit 0 HP and you are on Death's Door; each hit survived lowers Deathblow RES by 10% (base 60%, clamp 33-90%) [V3 DD2w Death's_Door_(Darkest_Dungeon_II)]. A dead hero's skill upgrades, quirks and Memory are lost; at the next Inn a random unlocked class that has not died this expedition fills the slot [V3 DD2w Heroes, Death's_Door].
- All four dead: expedition over, the "Lost in Darkness" screen counts Candles, play returns to the Altar. Trinkets do not persist [V3 DD2w Death's_Door, Darkest_Dungeon_II].
- Win: kill the act boss at the Mountain (20 Candles, +6 for entering, +2 per survivor) and the next act unlocks [V3 DD2w Candles_of_Hope].
- Recovery: yes, within a run through Inns and the Field Hospital; a Meltdown costs a quirk chance and 3 Affinity per bond. Kingdoms is lost by too many hero deaths, too many destroyed inns, or time running out [V3 DD2w Kingdoms].

#### 7. Consequential vs cosmetic choices
- Consequential: party composition and ranks; keeping Stress low (Stress, Meltdown and Affinity are one feedback loop). Basis: PCG, GP and the wiki all say Stress is the main threat ("Focus on stress, not HP") [community consensus].
- Consequential: using Inn Items to buy Affinity before Embark, because Cursed skills are forced and uncancellable. Region choice (goal and modifier) and Flame management via Assistance Encounters.
- Consequential: how many optional fights you take; they pay Mastery Points and Candles but cost Affinity risk and open ambush windows (GP).
- Cosmetic: party names ("purely cosmetic" per the wiki), stagecoach skins, hero skins, most Inn flavour text, narrator lines [V3 DD2w The_Crossroads, Altar_of_Hope].
- Near-dominant: the early-access advice to upgrade the Plague Doctor stress heal first; the 2025 rework makes it unverified.

#### 8. Open items
- Stress after Meltdown or Resolute: [CONTESTED]. GD (fetched) says "reset to 1"; Fextralife [S3 darkestdungeon2.wiki.fextralife.com/Combat] says "close to 0"; NamuWiki [S3 en.namu.wiki ... Collapse and Resolution] says 0; wiki.gg Stress page silent. Unsettled; same as v2 "Still unknown".
- Session length `?` (no source); real-time pause during driving `?`; Kingdoms numbers not read.
- v2 cell fills: R7 DD2 B6 gives only 90/33/5/5/33/65/90; wiki.gg also lists affinity 1-4 = 65% negative and 14-16 = 33% positive, 17-19 = 65%, 20 = 90% [V3 DD2w Relationships]. R7 DD2 Flame "Assistance Encounters give 15-30": quirk-specific options give +30 or +45 (Compassionate, Raconteur, Field Surgeon, Generous, Ascetic/Austere) and Candle node choices +30 [V3 DD2w The_Desperate_Few, Candles_of_Hope]. R7 K5 inn tally (23 inns; 18 at 50%, 3 at 100%, 2 at 25%) recounted: confirmed [V3 DD2w Inn].
- Attachment claims (62dd3fd3-emergent-narrative-mechanics.md; DD1 baseline re-read on wiki.gg Affliction/Stress/Virtue pages, all DD1 numbers match):
  - :177 "act-outs cannot happen two times in a row for the same hero, and two different heroes cannot have act-outs back-to-back": TRUE for DD1 [V3 DD2w Affliction line 13]. DD2: no Affliction; the only act-outs are per-Relationship (e.g. Hateful may hit its partner) and no spacing rule appears on Relationships, Stress or Quirks pages: NOT CARRIED OVER as stated; `?` whether a hidden rule exists.
  - :293 Stress 0-200, check at 100, 25% Virtue / 75% Affliction, -5% per level gap, heart attack at 200: DD1-correct (Virtue resets to 45 not 40-45 on wiki). DD2: Stress 0-10, resolve at 10 is Meltdown 80% / Resolute 20%, no heart attack, no level-gap modifier [V3 DD2w Stress_(Darkest_Dungeon_II)]: DOES NOT CARRY OVER.
  - :295-305 Affliction History (weights 4, +2 per repeat, Virtue +1) and the "hero becomes the one who goes Hopeless" design lesson: DD1-correct [V3 Affliction lines 313-318]. DD2 has no weights; quirks are a first-in-first-out list of 3 good and 3 bad (oldest replaced), Meltdown/Resolute give a 40% chance of one quirk, quirks persist only with Memories [V3 DD2w Quirks_(Darkest_Dungeon_II)]: NOT CARRIED OVER (nearest analogue is quirk-weighted Meltdown odds: Shattered Will +20%, Fragile +15%).
  - :307 affliction barks deal 6 stress to the party (contagion): DD1-correct. DD2 analogue: negative banter adds Stress and removes Affinity, rising with Stress (0-3 none, 4-6 6%/6%, 7-9 90% negative), and Meltdown takes 3 Affinity from every bond: CARRIES OVER IN SPIRIT, different numbers.
  - :309 act-out probability vectors (Fearful 31.5% etc.): DD1-correct [V3 Affliction lines 32,116,132]; no DD2 equivalent.

Source keys (Sunless Sea). SSf = https://sunlesssea.fandom.com/wiki/<Page>, read through api.php revisions on 2026-10-22 (page revision dates 2016-2025 given where used). CLQ = https://cliqist.com/2015/04/01/sunless-sea-beginners-game-guide/ (2015-04-01). SSnews = Steam news API appid 304650. WP = https://en.wikipedia.org/wiki/Sunless_Sea.

### Sunless Sea - facts line
Failbetter Games; real-time ship exploration, trading and survival with card-style story events (a roguelite with heirs); released 6 Feb 2015 [V3 WP]. Latest build in the Steam feed is v3.0.0.31 of 2026-08-27, which followed a Unity engine upgrade (29 Jul 2026), and a "Legacy" branch v2.2.15.3229 is kept for old hardware [V3 SSnews]; the wiki figures below describe the v2.2 era and 2015 guides are older, so treat numbers as version-bound. Assumes the base game, a brand-new captain, no Zubmariner DLC. Session: a London-and-back voyage roughly 15-30 minutes, a captain's life several hours [M]; `?` no source.

#### 1. Setup choices
- Captain's Making: "Choose a Past" or "A Past Wreathed in Shadows" (start at once, choose later; a later pick will not lift a stat above 50) [V3 SSf Captain's_Making, rev 2021-03-22].
- Past, five options; every captain starts with Hearts, Veils, Pages, Mirrors, Iron at 25, [V3 SSf Character_creation, rev 2025-06-17]: street urchin (+25 Veils, +10 Echoes, a Longshanks Gunner officer); poet (+25 Pages, +20 Echoes, Sly Navigator); Veteran of the Campaign of '68 (+25 Iron, +20 Echoes, Shady Cook); ordained priest (+25 Hearts, +10 Echoes, Gall-Eyed Engineer); natural philosopher (+25 Mirrors, +20 Echoes, Plausible Surgeon). The community strategy page recommends urchin or philosopher but says no choice "makes or breaks" a game [V3 SSf Basic_Strategies, rev 2023-06-22, player-written].
- Ambition (the win condition): Fulfilment (be London's most venerated explorer, write the Zong of the Zee), Wealth (retire to a mansion with 30,000 Echoes), Your Father's Bones (find and bury him), Immortality (needs the Zubmariner DLC); "The Uttermost East" is listed as unavailable [V3 SSf Character_creation; Retire_from_Zeefaring_Life].
- Cosmetic: form of address (Madam, Sir, Citizen, my Lord, my Lady, Captain) and a portrait cameo.
- Fixed kit: Ligeia-class Steamer (Hull 75, Hold 40, 10 crew places, four slots), 7 zailors, 50 Echoes plus the past bonus [V3 SSf Character_creation, Basic_Strategies]. The map is randomised for each captain [V3 CLQ].
- From the second captain: a Legacy at the death screen (below). No difficulty setting found `?`.

#### 2. The loop
Clock: real time on the zee with a pause button; hunger and meals do not tick while the Gazetteer (the story book) is open [V3 CLQ; V3 SSf Mouths_to_Feed]. Story time in London counts voyages ("Another Day"), not minutes [V3 SSf Returning_to_London]. The hidden quality "Something Awaits You" (SAY) is re-rolled 1-100 every minute at zee (101-200 when submerged); many London and port storylets need it [V3 SSf Something_Awaits_You, rev 2024-09-06].
1. Fallen London (start and base): read the paper, sell Port Reports at the Admiralty, repair at the Drydock, hire crew (30 Echoes, a Hearts challenge), buy fuel, supplies and cargo, rest, collect harbour messages [V3 SSf Fallen_London].
2. Leave dock and sail yourself. Fuel burns by engine power; each crew member raises Hunger; at 50 one supply is eaten [V3 SSf Supplies, Crew].
3. Terror rises while the lamp is off and you are outside lit areas or shore; green dots mean it is held [V3 SSf Terror, rev 2024-03-11].
4. Use the zee-bat to find nearby land, dock, and the Gazetteer shows storylets: trade, passengers, Port Report, shore leave, skill challenges against Hearts, Iron, Pages, Mirrors, Veils, luck, items or story progress [V3 CLQ; V3 SSf Challenge].
5. Ships and monsters that notice you start real-time combat: aim arcs, weapons warm up to a firing solution, lamp speeds it [V3 SSf Combat, rev 2019-10-14].
6. Thresholds interrupt: Fuel 0 (Desperate Measures), Hunger over 50 (Mouths to Feed), 100 (Starvation Walks the Ship), Terror 100 (Mutiny), Hull 0 (Shipwrecked), Crew 0 (Lost With All Hands) [V3 SSf each page].
7. Return to London: Terror above 50 is set to 50 and costs 0-4 Nightmare's Strength [V3 SSf Returning_to_London]. Sell, restock, rest, repeat. Automated: Hunger, fuel, Terror dots, monster pursuit, SAY roll.

#### 3. The choice menu
| verb / choice | cost | effect | when | frequency |
|---|---|---|---|---|
| Load the voyage (fuel, supplies, crew, cargo) | Echoes; one Hold space per unit | sets how far you can go; 3:2 fuel to supplies advised | every departure | constant |
| Lamp on or off | fuel burned | lamp on saves about 5 Terror per fuel crate; speeds firing | continuous | constant (CONTESTED value) |
| Route and destination | time, fuel, Terror | what you discover or deliver | continuous | constant |
| Zee-bat | small, `?` | reveals nearby land | unknown waters | frequent |
| Dock and pick a storylet | time, SAY, a challenge | trade, quests, lore, Secrets | every port | constant |
| Trade goods | Echoes | buy low, sell high | every port | frequent |
| Port Report | a visit | later paid by the Admiralty in Echoes, fuel and Favour | each new port | frequent |
| Shore leave or rest | Echoes (cheapest London lodging: 10 Echoes for -1 Terror) [V3 SSf Your_Lodgings]; better lodgings and ports cost more | Terror down, Wounds healed | when Terror is high | frequent |
| Fight or flee | Hull, Crew, throttle (full power can blow the engine) | loot; killing a monster or ship lowers Terror, more when Terror is high [V3 SSf Basic_Strategies] | when pursued | frequent |
| Hire an officer; spend a Secret to raise a stat | Echoes, Secrets | stats up (+8 to +16 total per officer) | London visit with SAY | occasional |
| Buy ship, engine, guns | thousands of Echoes | capacity, speed, firepower | when rich | rare |
| Return home now or push on | fuel, supplies, Terror | resets Terror to 50, sells cargo | every few ports | constant |
| Starving crew: ration, consign, feast, hide the truth | Crew, Terror | survive another stretch | Hunger over 90 | rare |
| Mutiny: fight (Iron) or persuade (Hearts) | losing ends the run | winning costs about half the crew and 5 Iron but cuts Terror by 50 | Terror 100 | rare |
| Retire at the Lodgings | 30,000 Echoes for Wealth, etc. | the win | end of a captain | once |
| Legacy choice at death | none | what the heir inherits | each death | once per death |

#### 4. First hour, step by step
1. Pick the Past and Ambition; the game opens in London at Wolfstack Docks [V3 SSf Fallen_London].
2. Read the morning paper at Your Lodgings before every voyage [V3 CLQ].
3. Sell the starting book "Advice for Captains" at Mrs Plenty's Shipside Provisioners for 50 Echoes [V3 CLQ].
4. Visit the Admiralty Survey Office; take its mission; you will sell Port Reports here.
5. Hire crew once (30 Echoes); buy fuel and supplies, preferring fuel (15 fuel and 10 supplies suggested; do not over-hire, 50% crew gives full speed) [V3 SSf Basic_Strategies; V3 CLQ].
6. Optionally buy a cheap lamp at Bultitude's, or mushroom wine to sell at Venderbight for about 3 Echoes profit a bottle [V3 CLQ].
7. Accept the Tomb-Colonists passage to Venderbight; first route north: Hunter's Keep, Venderbight, Whither, Codex, back to London [V3 CLQ].
8. Cast off, lamp off, keep to the shore; watch the three gauges (fuel, hunger, Terror) at top left [V3 CLQ].
9. Send the zee-bat in unexplored water; dock at each port; make a Port Report; wait for the SAY bell (lamp icon at the log book) before docking where you want stories [V3 CLQ].
10. Fight only weak pirates near home, with the lamp on; flee zee-beasts [V3 CLQ].
11. Turn back when Terror passes about 50 or fuel runs short (the strategy page: never leave London above 50); arriving at London sets Terror to 50 [V3 SSf Returning_to_London, Basic_Strategies].
12. In London: sell cargo, hand in reports (first report per port also gives +1 Admiralty Favour), repair, rest, collect harbour messages (needs SAY and Terror 50 or less) [V3 SSf Port_Report, Returning_to_London].
13. Hire an officer if offered; talk to officers and spend Secrets to raise stats [V3 CLQ].
14. First upgrade: an engine, per CLQ (500 Echoes, +200 power), but the community page says wait until income is steady [CONTESTED].
15. Repeat with a longer route; a first captain usually dies within a few voyages [M].

#### 5. What changes later
- Ships (nine on the wiki list; community picks: Cladery Heart for new captains, Maenad frigate as all-rounder, Eschatologue dreadnaught strongest at 30,000 Echoes), weapons with Hull or Life damage, auxiliary gear crafted at the Lodgings [V3 SSf Basic_Strategies].
- Far regions (North, South, East), Ambition storylines, boss monsters, lodging upgrades (townhouse, mansion), a sweetheart and child, and a Scion who becomes a dynasty [V3 SSf Time_with_your_Family, Retire].
- Pressure: longer routes mean more Terror, hunger and fuel; ship upgrades add crew and supply burn.

#### 6. Failure and ending
- Death ends the captain: mutiny lost, Hull 0, crew 0, starvation. Then the Legacy screen: pick one (two with Scion) of Rival (half Iron plus a weapon), Pupil (half Mirrors, half Echoes), Salvager (half Veils, half Echoes), Shipmate (half Hearts plus an officer), Correspondent (half Pages plus the whole chart); an Ironclad Will (100 Echoes) carries lodgings and heirlooms [V3 SSf Legacy, rev 2023-05-26].
- Win: retire at the Lodgings with the Ambition met (Wealth 30,000 Echoes and a mansion; Fame by the Zong of the Zee; Father's Bones). Retiring without it is a "stalemate"; some quest endings (Venturer's Passage, hijacked zeppelin, Her Ladyship's embrace) end the game and give a Legacy bonus [V3 SSf Retire_from_Zeefaring_Life, Legacy].
- Recovery: Terror, Hunger, fuel, Hull recover with Echoes and time; crew and a lost ship do not; Terror 100 means mutiny.

#### 7. Consequential vs cosmetic choices
- Consequential: voyage loading and routing (fuel, supplies, crew size) and when to turn home. Basis: player-written strategy page and CLQ agree on ratios and the Terror-50 rule.
- Consequential: Lamp and shore handling of Terror, though the value of the lamp is CONTESTED (CLQ 2015 says it does not slow Terror; the 2024 wiki says about 5 Terror per fuel crate).
- Consequential: free sinks of Terror (family time -20, kills) versus paid ones; players call port Terror reductions overpriced [community consensus, V3 SSf Basic_Strategies].
- Cosmetic: form of address, portrait, ferret; the Past is a minor tilt (+25 to one stat), per the strategy page.
- Dominant-ish: Admiralty Port Reports for fuel; Cladery Heart as the first ship (community recommendation).

#### 8. Open items
- Session lengths, difficulty modes, the per-second fuel formula, what v3.0.0.31 changed `?`. Zubmariner (diving, Immortality) not covered.
- v2 corrections (R7 Sunless Sea): Mutiny: you choose Iron (167 for 100%) or Hearts (334 for 100%); failing the chosen one kills you; success costs about half the crew and 5 Iron and cuts Terror by 50; it fires at Terror 100 with at least 4 crew [V3 SSf MUTINY!]. Out of fuel (v2 "drift helplessly"): a Desperate Measures storylet lets you burn 2 Supplies for 1 Fuel, or gamble on a 50% luck challenge [V3 SSf Desperate_Measures_(Fuel)]. Returning to London above 50 Terror: 0-4 Nightmare's Strength, proportional to Terror [V3 SSf Returning_to_London]. SAY: re-rolled each minute at zee, not once per voyage [V3 SSf Something_Awaits_You]. A1 heir inheritance: the five Legacy choices above [V3 SSf Legacy]. Starvation: below 100 Hunger a 20% random event offers cannibalism; at 100 "Starvation Walks the Ship" [V3 SSf Desperate_Measures_(Hunger), STARVATION_WALKS_THE_SHIP!].
- Attachments: grep found no Sunless Sea claims in any of the four uploaded documents.

Source keys (Eternal Darkness). EDf = https://eternaldarkness.fandom.com/wiki/<Page>, read through api.php revisions on 2026-10-22 (page revision dates given). WPr = https://en.wikipedia.org/wiki/Eternal_Darkness (action=raw, 2026-10-22). NWR = https://nintendoworldreport.com/review/3905/eternal-darkness-gamecube (undated). NL = https://www.nintendolife.com/reviews/2010/10/eternal_darkness_sanitys_requiem_retro. HG = https://www.honestgamers.com/8629/gamecube/eternal-darkness-sanitys-requiem/review.html (2010-01-13). No manual or in-game tutorial text was reachable (StrategyWiki sits behind a Cloudflare challenge), so this tutorial is assembled from wiki chapter pages and reviews; button-level controls are mostly [M].

### Eternal Darkness: Sanity's Requiem - facts line
Silicon Knights (published by Nintendo); third-person action-adventure and psychological horror; GameCube only, released 24 Jun 2002 in North America [V3 WPr] (the Fandom infobox says 23 Jun [CONTESTED], trivial). A disc game with no patches [M]; any later re-release or port `?`. Assumes the single mode with no difficulty setting [M]; the chapter-1 path is the only difficulty lever. First run: 20-25 h for an experienced player, up to 40 h for a casual one [V3 NWR], against my memory of about 12-15 h [M, CONTESTED]. At about 12 chapters that is 1-2 h per chapter, so the first hour is the prologue, chapter 1 and the start of chapter 2 [derived].

#### 1. Setup choices
- No character build and no difficulty menu `?`: you start as Alex Roivas in a hub, her murdered grandfather's Rhode Island mansion; each chapter then hands you a fixed character [V3 WPr].
- The one real choice comes at the end of chapter 1: take one of three artifacts, which fixes the run's path. Red = Chattur'gha (matter, health), Green = Xel'lotath (insanity, sanity), Blue = Ulyaoth (planes, magick) [V3 EDf The_Chosen_One rev 2026-03-26; V3 HG]. It sets enemy alignment, some puzzles and items and cut scenes; red enemies are tougher, an "unofficial hard mode" [V3 WPr]. No explanation is offered at the choice [V3 NL]. A cleared path is locked out of later runs until all three are cleared [V3 WPr].
- Per chapter the meters and kit are fixed by character: HP 75-150, MP 75-125, SP (sanity) 75-150 (Karim 150/100/100; Edwin Lindsey 125/100/150; Paul Luther 75/125/100; Alex 100/125/125). Pious has no MP or sanity, Ellia no MP [V3 EDf character infoboxes, revs 2024-2026]. Weapons follow the era: swords and blowguns early, flintlocks, then revolvers to assault rifles [V3 HG].
- Spells are not chosen at the start; runes, codices and scrolls are found, and the Tome carries known spells into later chapters [V3 EDf Tome rev 2024-11-14; V3 NL].

#### 2. The loop
Clock: real time, no turns; chapter levels joined by a mansion hub. Meters: red Health, blue Magick, green Sanity, plus a hidden Stamina drained by running and wild swings [V3 HG; V3 EDf Stamina rev 2025-06-27]. The Tome is the menu: map, inventory, spells [V3 EDf Tome].
1. Hub: as Alex, search the mansion for the next chapter page (clues, puzzles, items), then read it in the Tome [V3 EDf Alexandra_Roivas rev 2026-08-18].
2. Chapter: you become a different character in another era (26 BC to 2000 AD; Persia, Cambodia, France, Rhode Island) and explore rooms, solve puzzles, collect items, runes, codices and scrolls [V3 WPr].
3. Combat: swing, or lock on to a body part; limb and head loss cripples or blinds enemies [V3 WPr]. Every enemy that sees you drains Sanity, except Guardians and Trappers (and, in Edward's chapter, the vampire's victims) [V3 EDf Sanity rev 2025-08-22; Zombie rev 2026-08-31].
4. A downed enemy can be finished for a Sanity refund; zombies stand up again unless finished or burned [V3 EDf Sanity; Zombie].
5. Automated: below 50% Sanity the camera tilts and an effect may fire on room entry, likelier and worse as the meter falls; at 0 the drain hits Health instead [V3 EDf Sanity_Effects rev 2026-08-31].
6. An effect plays out (you usually cannot cancel it), ends in a white flash and puts you back at the door you came through [V3 EDf Sanity_Effects].
7. Scripted chapter end (some heroes die); control returns to Alex, who starts the hub with less Sanity after each chapter [V3 EDf Tome trivia]. After the last page, Alex goes into Ehn'gha for the finale.

#### 3. The choice menu
| verb / choice | cost | effect | when | frequency |
|---|---|---|---|---|
| Swing, or lock on to a body part | Stamina (wild swings) | damage, dismember, decapitate to blind or disable | every fight | constant |
| Finish a downed enemy | seconds exposed; unfinished zombies rise | Sanity back, "usually" what the first gaze took (zombies, Bonethieves, Horrors) [V3 EDf Sanity] | after each knockdown | constant |
| Run, sneak, or let rival-aligned monsters fight | Stamina; any sighting costs Sanity | skip a fight, no refund [V3 EDf Zombie] | low Sanity or Health | frequent |
| Swap weapon (torch, firearm) | none | torch kills Mantorok and Xel'lotath zombies by fire [V3 EDf Zombie] | per enemy type | frequent |
| Cast a stored spell (Shield, Damage Field, Magickal Attack, Dispel, Reveal Invisible) | MP by Circle size (3, 5, 7) | defend, damage, dispel; puzzle barriers are keyed to specific runes [V3 EDf Magick rev 2024-12-04] | combat and puzzles | frequent |
| Pick the alignment rune of a cast | Recover: Xel'lotath (Sanity) 10/20/30 MP, Chattur'gha (Health) 30/40/50, Mantorok (both) 40/50/60, Ulyaoth refunds its own MP | counter Pious's Ancient: Ulyaoth > Chattur'gha > Xel'lotath > Ulyaoth [V3 EDf Alignment rev 2018-07-20] | every cast | frequent |
| Assemble a new spell (Circle + alignment + verb + noun + up to six Pargon power runes) | found runes only | discover spells without scrolls [V3 NWR]; the six-rune limit is on the Fandom Magick page [V3] | on finding a rune | occasional |
| Summon and steer Zombie, Trapper or Horror | MP; Sanity drains constantly while steering a Horror [V3 EDf Horror rev 2024-02-28] | fight, open doors, move objects | bosses, puzzles | occasional |
| Enchant a weapon | 5/10/15 MP, lasts 2 minutes | x1.375 / x1.5 / x2 vs the weak alignment; Mantorok saps [V3 EDf Magick] | hard fights | occasional |
| Drink Liquid Courage or use a restore item | limited stock (Edward starts with about 7) | about half the Sanity bar [V3 EDf Liquid_Courage rev 2024-11-27] | emergencies | rare |
| Take the optional Mantorok rune, or the Enchanted Gladius | long backtracking, three characters' statues | purple spells; best sword, only Alex can wield it [V3 EDf A_Journey_Into_Darkness; Weapons rev 2022-06-29] | once per run | rare |
| Pick the artifact (Red, Green, Blue) | irreversible for the run | sets the path | end of chapter 1 | once |

#### 4. First hour, step by step
1. Alex dreams of zombies, then a 3:33 AM call says her grandfather Edward is dead; she flies to the Roivas mansion [V3 EDf Alexandra_Roivas rev 2026-08-18].
2. Search the first floor; find the hidden study with the Tome of Eternal Darkness, which is also your menu; take the Gladius from the plaque there [V3 EDf Tome; Weapons].
3. Read the first page: chapter 1, Pious Augustus, 26 BC, a Roman centurion lured into the Forbidden City [V3 EDf The_Chosen_One rev 2026-03-26].
4. Go straight to the first Mantorok zombie and fight; it is slow and weak, and the chapter has no recovery and no Sanity meter [V3 same].
5. Collect the four colour-marked rune cubes and light the wall runes to open the next passage; smash the statue, which teaches lock-on targeting [V3 same].
6. Clear the last zombies, press the button, enter the final room and choose an artifact: your path. Pious turns lich and the chapter ends [V3 same].
7. Back in the mansion, find the next page: chapter 2, Ellia, a Khmer dancer in Angkor Thom, 1150 AD. Here the green Sanity meter first appears [V3 EDf Sanity_Effects; V3 WPr].
8. Watch Sanity fall each time a monster sees you; fight rather than flee, since Sanity comes back mainly by finishing enemies [V3 NWR].
9. After a knockdown, finish the enemy and watch Sanity refill; below 50% expect the tilt and room-entry hallucinations [V3 EDf Sanity].
10. Manage Ellia's kit: short sword, blowgun, a trap door that breaks the sword, which can be repaired only if you save the guard in that room from the zombies [V3 EDf Weapons rev 2022-06-29].
11. Past the first hour: chapter 3, Anthony, finds the 3-point Circle and Enchant Item scroll; chapter 4, Karim (by elimination [M]), finds the Recover scroll in the Forbidden City catacombs [V3 EDf Magick].
12. Open the Tome's spell screen, try rune combinations, and assign spells to buttons for quick use [V3 WPr; V3 NWR].

#### 5. What changes later
- Bigger Circles: 5-point (Paul Luther, chapter 7) and 7-point (Peter Jacob, chapter 9) add two and four power runes; a 9-point Circle exists only in Ehn'gha [V3 EDf Magick]. Summons unlock by Circle: Trapper (3), Zombie (5), Horror (7).
- New enemy classes: Bonethieves, Horrors, Guardians, Trappers, the Black Guardian, the vampire, the worm [V3 EDf pages]; heroes shift from a short sword to firearms, and chapters revisit the same places centuries later with changed puzzles [V3 HG; V3 NL]. The reviewer's complaint is that late combat is "just more of what you killed before" [V3 HG].
- Pressure: Alex's hub Sanity falls chapter by chapter [V3 EDf Tome]. Chapter numbers: Pious 1, Ellia 2, Anthony 3, Max 5, Lindsey 6, Paul 7, Roberto 8, Peter 9, Michael 11, Alex 12; Karim 4 and Edward 10 by elimination [V3 EDf chapter pages; M].

#### 6. Failure and ending
- Death shows a Game Over page in the Tome (Pious and Anthony get different text) and you retry from a save [V3 EDf Tome gallery, Pious_Augustus trivia; save rules `?`]. A chapter hero's death can be scripted, so survival is not always needed for the story to advance [V3 NL].
- Finale: Alex gathers the essences (not Pious's), uses the Ehn'gha towers to summon the rival Ancient, then fights Pious, who is invulnerable until his artifact is knocked out and hit; when her Sanity is low the spirits of the dead bearers enter her body to fight [V3 EDf Pious_Augustus rev 2026-08-18]. Losing: Pious spits on her body and proclaims the Darkness's rule; three richer lose endings (Red, Blue, Green Path) were cut [V3 EDf Red_Path, Blue_Path, Green_Path].
- Win: her Ancient destroys Pious's, then Edward's spirit binds it; Alex narrates differently by run count [V3 EDf Alexandra_Roivas]. After all three paths, Edward reveals the paths were simultaneous timelines and Mantorok manipulated the three rival Ancients [V3 WPr].

#### 7. Consequential vs cosmetic choices
- Consequential: the chapter-1 artifact, which sets enemy set and toughness, which Ancient you counter and summon, and the victory visions (Chattur'gha's win shows a red hell with Horrors over a slave population; Ulyaoth's, human enslavement overseen by Guardians) [V3 EDf Chattur_gha rev 2025-08-07; Ulyaoth rev 2025-01-04, gallery captions].
- Consequential but easy to satisfy: finishing every knocked-down enemy keeps Sanity high, and the HonestGamers reviewer says doing so makes the game "strategically gentle" [V3 HG]. Most Sanity effects are cosmetic (fake errors, fake deaths, a fake save-delete prompt); some hinder, such as a locked room or exploding limbs [V3 EDf Sanity_Effects].
- Dominant answer: finishing is free while Recover costs MP; Mantorok Recover (40/50/60) is cheaper than casting Xel'lotath plus Chattur'gha Recover (40/60/80) at Circles 5 and 7 and equal at 3 [derived from V3 EDf Magick], so the optional Mantorok rune wins when both bars are low, though it cannot summon; a single-bar heal is cheaper with its own alignment.
- Cosmetic or minor: path-specific cut scenes and some items [V3 NL], Ellia's sword repair, which era you prefer. Basis for this whole list: wiki and reviewer statements, not telemetry; no community consensus was sampled.

#### 8. Open items
- `?` per-enemy Sanity numbers, button-level controls, save rules, difficulty options, any re-release. [CONTESTED] the finale needs the Enchanted Gladius (Pious page) yet that sidequest "can be missed entirely" (Weapons page); how an unarmed run wins is not established.
- v2 corrections (R7 Eternal Darkness): J1 note "Casting does not cost sanity [M]" and "Still unknown: whether spells ever cost sanity": plain casts cost MP only (no sanity cost in any spell row), but steering a summoned Horror drains Sanity constantly [V3 EDf Horror rev 2024-02-28] and the Vampire page says players "summon creatures and control them to slowly drain their own sanity" [V3 EDf Vampire rev 2024-10-11]; the Summon Zombie and Horror flavour text mentions a toll on the psyche [V3 EDf Magick]. J1 stays PART.
- v2 "exact sanity percentages restored by a finishing blow for every enemy type": still `?`. Filled in: only "usually the amount lost from the initial gaze" for Zombies, Bonethieves, Horrors [V3 EDf Sanity]; Liquid Courage about half [V3 EDf Liquid_Courage]; vampire flee returns "a chunk" and its death fills Edward's bar [V3 EDf Vampire]. Meter sizes by character (SP 75-150) are new, as is the gauge scale: Recover's 24/40/100 points are measured against 75-150 bars. v2 Recover costs, 50% tilt threshold, empty-bar-to-Health and Pious-no-meter: confirmed.
- Capability line (J, K, G only): G1 YES [V3 WPr: real-time third person, lock-on by body part], G2 PART [V3 HG: era weapons from blowguns to grenade launchers, enchantable; no armour found; small kit per hero], G3 PART [V3 NL: scripted hero deaths; Health meter; no permadeath rule found], G4 NO [M], G5 PART [V3 EDf Zombie: rival-aligned monsters fight each other; Mantorok Reveal Invisible; no stealth system] | J1 PART [V3 EDf Magick: rune spells cost MP; summon steering costs Sanity], J2 NO [M], J3 YES [V3 EDf Sanity, Sanity_Effects] | K1 NO [V3 WPr: room-by-room levels, area map only], K2 NO [M], K3 PART [V3 EDf Stamina: hidden Stamina only; no hunger found], K4 YES [V3 WPr, NL: exploration and puzzle levels], K5 NO [M: no rest mechanic on any page read].
