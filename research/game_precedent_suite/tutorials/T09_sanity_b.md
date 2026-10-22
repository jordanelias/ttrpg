# T09 tutorial pass: Don't Starve (+DST), Pathologic 2, Vampire: The Masquerade - Bloodlines

Source keys (all read 2026-10-22; "V3 key Page" = page body fetched this session with `curl -sL`):
DSw = https://dontstarve.wiki.gg/wiki/<Page>?action=raw ; WPds = https://en.wikipedia.org/wiki/Don%27t_Starve (API extract) ; STEAM = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=<id>.
PLw = https://pathologic.wiki.gg/wiki/<Page>?action=raw ; VTf = https://vtmb.fandom.com/api.php (revisions) ; WPvt = https://en.wikipedia.org/wiki/Vampire:_The_Masquerade_%E2%80%93_Bloodlines.
Game text for DS is the base game with the Mega Update; the wiki mixes in DLC/DST notes, which I filter out and mark.

### Don't Starve - facts line
Klei Entertainment; open-world survival / action-adventure with roguelike permadeath; released 23 Apr 2013 [V3 DSw Don't_Starve]; last major patch "Major Quality of Life and Bug Fix Update", 27 Apr 2023 [V3 STEAM appid=219740]. This tutorial: base game only (no Reign of Giants/Shipwrecked/Hamlet), single player, Survival Mode (formerly Sandbox) on default world settings, Wilson. One run = open-ended; a "day" is 8 real minutes [V3 DSw Day-Night_Cycle], so the first hour is about 7 in-game days and a run that reaches the first winter (Day 21) is about 2.8 real hours. Sources: wiki.gg pages and Wikipedia; no official in-game tutorial exists (the game gives only Maxwell's one line).
#### 1. Setup choices
- **Character** (the only build choice). Unlocked by cumulative XP, which is only paid on permanent death at 20 XP per day survived [V3 DSw Experience]: Wilson (start; grows a beard), Wagstaff (start), Willow 160 XP/8 days (fire-immune, lighter, lights fires when nervous), Wolfgang 320/16 (stronger with a full belly, afraid of dark), Wendy 640/32 (comfortable in dark, hits weakly, twin ghost Abigail), WX-78 960/48 (eats anything, damaged by water, upgrades with gears), Wickerbottom 1280/64 (books, cannot sleep), Woodie 1600/80 (axe, werebeaver curse); Wes (via Adventure Mode) and Maxwell (by finishing Adventure) [V3 DSw Characters, Experience]. Each has its own Health/Hunger/Sanity maximums (Wilson 150/150/200 [V3 DSw Wilson]).
- **World settings** (optional screen before generation): each new world is randomly generated; the player may set frequencies such as Hound attacks, Deerclops, and which seasons occur [V3 DSw Survival_Mode, Deerclops]. Default seasons: Summer then Winter only; first winter begins Day 21 [V3 DSw Seasons/DS].
- **Mode**: Survival (default, no goal but survival) or Adventure, which is not chosen at setup: it is entered in-game through Maxwell's Door, found far from the spawn [V3 DSw Survival_Mode].
- No difficulty selector is documented (the world settings are the difficulty dial) and there is no starting kit beyond character-specific items; Maxwell's only instruction is to find food before night [V3 DSw Survival_Mode, Getting_Started_Guide].
#### 2. The loop
Clock: real time with pause (Esc); an 8-minute day made of sixteen 30 s segments split into Day, Dusk, Night [V3 DSw Day-Night_Cycle]; seasons: Summer 20 days then Winter 15 days (the Day-Night page says 20+16 = a 36-day cycle) [CONTESTED, see 8].
1. **Day**: forage (flint, twigs, grass, logs, carrots, berries), craft, scout; most monsters sleep and animals are active.
2. **Dusk** (red clock segments): a light source is not yet required; decide where to spend the night and ready a campfire or torches.
3. **Night**: total darkness lets Charlie attack, so the player stays in firelight, carries a torch, or sleeps in a tent [V3 DSw Getting_Started_Guide].
4. Meanwhile the game drains Hunger (9.375/min, 75 per day) and Sanity (-5/min at dusk, night, caves; -50/min in total darkness) [V3 DSw Hunger, Sanity], spoils food, runs mob schedules, regrows plants, changes the season and weather.
5. **Interrupts**, all in real time with no turn handoff: Hound packs every 6-13 days early (2 hounds, 120 s growling warning) escalating to 7-10 hounds after Day 100 [V3 DSw Hound]; Deerclops in Winter; full-moon Werepigs [V3 DSw Getting_Started_Guide]; rain, lightning and wildfire; shadow creatures when Sanity is low (they attack below 15%) [V3 DSw Sanity].
6. Dawn: the day counter increments; repeat. XP is paid only at death.
Automated: all meters' drain, spoilage, mob spawns and schedules, seasons, regrowth. Player-driven: everything else, including keeping the fire fuelled.
#### 3. The choice menu
| verb | cost | effect | when picked |
|---|---|---|---|
| Walk/scout/gather (constant) | daylight, risk from mobs | resources and map knowledge | all day |
| Craft tools/weapons/armor (constant) | flint, twigs, logs, grass; items have durability | Axe, Pickaxe, Spear, Log Suit | before leaving camp |
| Prototype at a Science Machine (frequent early) | Machine = 1 Gold + 4 Logs + 4 Rocks [V3 DSw Science_Machine]; each recipe costs its ingredients once | unlocks recipes for good; prototyping gives Sanity (listed in the Sanity table [V3 DSw Sanity]; +15 per [V2 R7]) | Day 3+, after finding gold |
| Eat raw/cooked/Crock Pot (constant) | food items, which spoil | refills Hunger; cooked > raw; raw meat -10 Sanity [V3 DSw Surviving_the_first_month] | when Hunger falls |
| Light a Campfire/torch/Fire Pit (every dusk) | logs, grass/twigs; 1 log fuels about an hour | keeps Charlie off, keeps Sanity up | every night |
| Sleep in a Tent (rare/mid) | craft cost; one of six uses [V2 R7] | +50 Sanity, +60 Health, -75 Hunger, skips night [V2 R7 DSw Tent] | low Sanity/Health at night |
| Fight, avoid, or lure (constant) | weapon/armor durability, Health | loot (meat, teeth, silk), safety | monsters near |
| Pick flowers/eat for Sanity (frequent) | flowers regrow slowly | +5 per flower [V3 DSw Getting_Started_Guide] | Sanity falling |
| Trap, farm, dry meat, keep bees (mid) | materials, a stable base | sustainable food | after Day 7 |
| Befriend/feed Pigs, trade at Pig King (mid) | meat, eggs | followers; Gold from the Pig King [V3 DSw Getting_Started_Guide] | when meat is spare |
| Choose/move the base (1-2 times) | days of scouting | everything else is cheaper nearby | Days 2-10 |
| Buy life insurance: Touch Stone, Life Giving Amulet, Meat Effigy (rare) | Effigy: -30 max Health each [V3 DSw Meat_Effigy] | revive at 50 Health, 2/3 Hunger, 1/2 Sanity [V3 DSw Death] | before boss or winter |
| Winter prep: Thermal Stone, warm clothing, stockpiles (once per cycle) | many days of gathering | survive freezing and long nights | last 5-10 days of Summer |
| Fight Deerclops/Hounds with preparation (rare) | gear, traps | removes the threat for 3-6 days (Deerclops respawn [V3 DSw Deerclops]) | Winter, Hound warning |
| Dig graves, use Worm Holes (rare) | Sanity | Amulet chance; faster travel | exploring |
| Assemble the Teleportato/enter Maxwell's Door (once) | clear a guarded chess set piece [V3 DSw Wooden_Thing] | next world / Adventure Mode | mid-late game, optional |
#### 4. First hour, step by step
Mostly from the wiki's Getting Started and first-month guides [V3 DSw Guides/Getting_Started_Guide rev 2022-11-28; Guides/Surviving_the_first_month rev 2026-06-23], with recipes [M].
1. Start with an empty inventory and Maxwell's warning; pick up flint, twigs, and grass tufts first, then craft an Axe (and a Pickaxe if you have 3 flint) from the Tools tab.
2. Chop logs, collect up to about 5 carrots/berries (enough to refill Hunger) and pine cones; do not over-cook or over-carry (food spoils).
3. Craft a Campfire before dusk but do not place it yet (build, then right-click to store it), plus two Torches; do not build a Fire Pit on night 1.
4. At dusk place the campfire beside resources you can gather by its light; cook and eat carrots/berries; one log lasts about an hour.
5. Stay in light all night; Sanity drains at dusk and night, and complete darkness lets Charlie kill you.
6. Day 2-3: scout for a base: near a road junction, a screen away from Pigs and Beefalo, with 2-3 Rabbit Holes and Ponds; avoid the Marsh (Tentacles) and Spider Dens.
7. Mine boulders for Gold, then craft and place a Science Machine; prototype Rope, Backpack, Log Suit, Spear, Hammer, Shovel.
8. Do not start fights you cannot finish: never poke Spiders, Bees, Tallbirds; Beefalo are a manure source.
9. Before Hounds (first attack about Day 6-13, two hounds, 120 s warning): wear Log Suit + Spear, or lure Hounds into Pigs/Beefalo herds.
10. Day 7+: replace the campfire with a Fire Pit; add Farms, Crock Pot, Traps for rabbits, Bee Boxes, Lightning Rod.
11. Keep an escape plan: find a Touch Stone, dig a Grave for an Amulet, or build a Meat Effigy around Day 16 (each costs 30 max Health).
12. From about Day 15, prepare for Winter on Day 21: Thermal Stone, Puffy/Breezy Vest or Winter Hat, Ice Box, Drying Racks (Jerky +10 Sanity [V3 DSw Winter]).
#### 5. What changes later
Winter: freezing is a new health drain; nights and dusks become much longer so Sanity drains faster; plants stop growing; Deerclops arrives and smashes structures; Blue Hounds replace Red; perishables spoil 25% slower [V3 DSw Winter]. Hounds scale: gap shortens to 3-8 days, pack to 7-10, warning to 30 s, special hounds 10% (Day 17) to 50% (Day 77+) [V3 DSw Hound]. Caves (via Sinkholes) add Depths Worms and constant -5 Sanity. Adventure Mode (5 chapters plus epilogue) wipes the character's kit and recipes [V3 DSw Adventure_Mode].
#### 6. Failure and ending
Death comes from starving, mobs, Charlie, burning, freezing, eating bad food at low Health and more [V3 DSw Death]. Without a revive item, the character and the world are permanently lost; the death screen pays 20 XP per day survived. Revival sets Health 50, Hunger 2/3, Sanity 1/2 and drops inventory at the corpse. Survival Mode has no win; Adventure Mode is the campaign (finishing it unlocks Maxwell [V3 WPds]). DST in two lines: a standalone multiplayer version (Steam Early Access 15 Dec 2014, 1.0 on 21 Apr 2016, up to six players; still live-patched, latest hotfix on Steam news 6 Jul 2026) with four seasons and nearly all characters available from the start [V3 WPds; DSw Experience; STEAM appid=322330]; death makes a player a ghost whom teammates can revive [M].
#### 7. Consequential vs cosmetic choices
- **Base site and winter prep** decide many deaths: the wiki says freezing "is often a recurring death for new players" who do not prepare [V3 DSw Winter]; the first-month guide spends most of its length on base location (wiki-guide consensus, not measured).
- **Light and Sanity upkeep** gate every night: below 15% Sanity shadow creatures attack, and Sanity falls -5/min at dusk and night while recovery needs food, flowers, sleep or crafted items [V3 DSw Sanity].
- **Life insurance timing** (Touch Stone / Amulet / Effigy) turns permadeath into a priced decision: each Effigy costs 30 max Health until used [V3 DSw Meat_Effigy].
- **Dominant answers per the wiki**: a field of Tooth Traps is "one simple strategy" against Hounds, and Drying Racks plus traps are "a simple and sustainable way" to feed through Winter [V3 DSw Hound, Winter]. Character choice changes play style (each has a perk and a drawback [V3 DSw Characters]); I found no sourced tier list.
- Cosmetic: in DST the paid add-ons are mostly skins [V3 WPds]; I could not source a purely cosmetic choice inside the base-game loop.
#### 8. Open items
- [CONTESTED] Winter length: Seasons/DS page says 20 Summer + 15 Winter (first winter Days 21-35); Winter page says 16; Day-Night page says 20+16 [V3 DSw Seasons/DS, Winter, Day-Night_Cycle]. v2 R7 did not state a winter length.
- v2 R7 DS K4 `[M]` (procedurally generated world): settled YES [V3 DSw Survival_Mode, WPds].
- v2 R7 confirmed in V3: Hunger 150 and Sanity 200 (Wilson) [V3 DSw Wilson], 9.375/min = 75/day [V3 DSw Hunger], 8-minute day, dusk/night -5 and total darkness -50 [V3 DSw Sanity], insanity tiers; no number was wrong. Tent numbers and +15 prototyping remain [V2] only.
- Not established: auto-save timing; exact Charlie grace period; tent recipe; DST current balance numbers (patch notes not read).
- Attachments: `grep -i "don.t starve"` over the four uploads found no claim about this game (only an unrelated "pathological" in the Citizens file).

### Pathologic 2 - facts line
Ice-Pick Lodge (publisher tinyBuild, Unity); open-world survival-horror adventure with a hard day clock; Windows 23 May 2019, Xbox One Dec 2019, PS4 Mar 2020 [V3 PLw Pathologic_2]. Patch number not established (Steam news feed for appid 505230 shows only Pathologic 3 posts, newest 9 Jan 2026 [V3 STEAM]); rules below are the wiki.gg Game_Mechanics page read 2026-10-22. Assumes the only shipped scenario, the Haruspex route, single player. One run is 11 playable days; the clock alone is 880 real minutes (100 min on Day 1 shrinking by 4 each day to 60 on Day 11 [V3 PLw Game_Mechanics, sum computed by me]), so about 15 h minimum before reloads and menus; total playtime [M] 20-30 h.
#### 1. Setup choices
- **Character: none.** You are Artemy Burakh, the Haruspex. The Bachelor and Changeling routes of the original were split off; the Bachelor route shipped as the separate Pathologic 3 (9 Jan 2026) and the Changeling route is unscheduled [V3 PLw Pathologic_2].
- **Difficulty: none found** in the wiki mechanics page or the game page `?` (not proven absent; a settings menu was not inspected).
- **Save file**: one file per playthrough; death penalties apply to all saves in that file and are removed only by starting a new file or taking the Fellow Traveler's deal [V3 PLw Game_Mechanics]. Saving is only possible at clocks inside major buildings; there are no autosaves outside the Prologue and the Abattoir start [V3 PLw Game_Mechanics].
- **Opening choices that matter**: which of four first stops to take on Day 1 (Bad Grief, Lara, the Bachelor, or home), then every quest decision (section 7).
#### 2. The loop
Clock: real time with a fast game clock (1 game hour = 4 real minutes on Day 1, 2.5 on Day 11); dawn 07:30; time stops in dialogue and most menus (trade, diagnosis, autopsy) but not while looting, or while the Alembic/Brewery run [V3 PLw Game_Mechanics].
1. **Dawn 07:30**: new quest markers, cutscenes, messengers; herbs respawn; children are outdoors; the Theatre closes; bandits disperse.
2. **Day**: pick quests and errands across the town's districts, each with its own infection state and reputation; some quests last a day and some several, and the game does not say which, so you do what you can [V3 PLw Game_Mechanics].
3. **Maintenance** woven through: eat (hunger fills in 6.5 h), drink, sleep only in named beds (exhaustion fills in 16.5 h), medicate, barter, repair, save at a clock.
4. **Triage**: treat Bound characters and patients (prophylaxis, diagnosis, antibiotics); from Day 4 do the daily Hospital chore at the Theatre that sets next day's Fund reward [V3 PLw Game_Mechanics, Theatre].
5. **Midnight** (the deadline): Bound at risk roll for infection, new districts become infected, last day's infected districts burn, the Theatre and Dead Item Shop open, stores restock at higher prices, children go home, bandits appear [V3 PLw Game_Mechanics].
6. Sleep, save, repeat. Interrupts: street fights (bandits, looters, arsonists from Day 5, the pain-mad sick), plague clouds, scripted arrivals (Inquisitor Day 7, Army Day 9); death sends you to the Theatre.
Automated: the district infection/burn schedule, Bound infection and death rolls, store prices, NPC routines, the accelerating clock. Player-driven: everything else.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Take / skip a quest or errand (constant) | game hours; some expire silently | story state, rewards, who lives | all day |
| Dialogue choice (constant) | no clock (time stops) | flags that change districts, Bound, endings | every conversation |
| Barter with townsfolk (constant) | items valued in integer trade points [V3 PLw Trading]; trading at a loss gives +0.5% reputation per value lost [V3 PLw Game_Mechanics] | food, drugs, ammo, clothes | when stocks are low |
| Loot bins, cabinets, houses (constant) | time; theft -1% to -4% reputation per item if seen; infected drawers cost Immunity | supplies | between errands |
| Eat/drink/coffee/lemon (constant) | rations; most raise thirst; coffee costs Health | fills Hunger, Exhaustion | a few times a day |
| Sleep (daily) | time at a bed with a clock; Exhaustion -20%/h, Health +25% per 2 h, hunger growth -60% | recovery | every ~16 h awake |
| Fight / sneak / run (frequent) | Stamina, weapon wear, bullets, reputation if the target is a townsperson | survive or loot | bandits, ambushes |
| Lockpick (occasional) | lockpick durability; -3% to -6% reputation | access | locked doors |
| Prophylaxis on a Bound (daily from Day 3) | boosters, tinctures, Twyrine | raises their immunity before the midnight roll | evening of danger days |
| Diagnose + prescribe antibiotic (mid) | tinctures (add pain), antibiotic; wrong layer = 25% potency | lowers infection; Bound: lowers death chance; raises the Fund | patients; hospital |
| Brew tinctures/antibiotics/painkillers (mid) | herbs, organs, clock time (time runs) | the medicine supply | at the Lair |
| Autopsy / drain blood (mid) | scalpel wear, reputation -10% healthy / -4% infected unless in Hospital or Steppe | organs, blood for brewing | when stocks are empty |
| Kill or spare a person (rare) | -5% to -50% reputation by act and witnesses | reputation below 40% closes shops to you, at 25% or less the militia attacks [V3 PLw Game_Mechanics] | quest forks |
| Repair clothes/weapons (occasional) | money + items | durability | when worn |
| Save at a clock (frequent) | walk to a clock | rollback point (rerolling Bound odds only before 07:30) | before risk |
| Final choice, Day 11 (once) | until 22:00 | deliver orders (Diurnal) or burn them (Nocturnal) | Day 11 |
#### 4. First hour, step by step
From the wiki's day-by-day plot [V3 PLw Plot:_Pathologic_2 rev as read 2026-10-22] and mechanics page; the Prologue plus Day 1 is the first session.
1. Wake in the Theatre; Mark Immortell shows a failed "12th Day" vision and offers a second chance; accept.
2. On the train, speak to the Fellow Traveller; after the crash walk into the black cloud: this is your first infection and a taught lesson.
3. Dreams teach the verbs: carry water to a sick woman, fight a man in the Kin's circle (the combat tutorial is in the Prologue [V3 PLw Game_Mechanics]).
4. Arrive at your father's house; take what you want from cabinets (you will hear laughter) and go upstairs.
5. Day 1: three men ambush you at the station; fight or flee; you start bleeding, hungry and tired. Take Lika's Tourniquet.
6. The Executors Talon and Beak tell you to watch Health, exhaustion, hunger and the passing of time. Read all the meters now.
7. Walk into town; choose one of four first stops; each tells you your father is dead and the town thinks you killed him.
8. Find water, food and a clock; save. Barter for supplies before spending money.
9. Bad Grief's errand in the Tanners: save or kill the wounded criminal; either way the house becomes lootable.
10. Visit Lara's Shelter (a bed and a clock); sleep when Exhaustion is high. The wiki's death penalties apply only to deaths after Day 1, so Day 1 is the low-risk day to learn combat [V3 PLw Game_Mechanics Death].
11. Attend Notkin's "trial" at the Soul-and-a-Half Fortress; your answer sets the Lika subplot.
12. Go to the Town Hall, get jailed, be cleared by Big Vlad; meet the Stamatin brothers at the Broken Heart and drink Twyrine for the cache clue.
13. At midnight watch the Theatre pantomime, then meet the Fellow Traveller, who trades dead items (broken ampoules, bloody bandages) for useful ones [V3 PLw Plot].
14. Sleep at a bed with a clock, save, and read the dawn messengers on Day 2.
#### 5. What changes later
Day 2 funeral and the debt plot; **Day 3** districts begin to be infected on a strict schedule and Bound start to be "in danger" [V3 PLw Plague]; Day 4 the Theatre becomes a hospital and the Fund starts; Day 5 arsonists and Rubin; Day 7 the Inquisitor arrives and food needs Inquisitorial Coupons; Day 9 the Army arrives with Commander Block, soldiers and Flame Corp units; Day 10 the Termites (your own Bound) are all infected and the Hospital is closed; Day 11 the hunt for the courier ends at 22:00 [V3 PLw Plot, Plague, Theatre]. Bound immunity rolls fall from 40-50% (Days 3-6) to 30-40% (7-9) to 20-30% (10-11) [V3 PLw Game_Mechanics]. The clock speeds up every day, so the same errand costs fewer game hours of slack.
#### 6. Failure and ending
Health 0 is not game over: from Day 2 you wake in the Theatre and Mark applies a permanent penalty to the file (max Health at deaths 1, 2, 4, 5, 8, 9, 11, 13, 14, 15, 17-20, totalling -50%; max hunger at 4, 12, 21; max exhaustion at 6, 16; touch lost at 2; Cotton Wool/Buttons in autopsies after 10) [V3 PLw Game_Mechanics]. On the 7th death the Fellow Traveler offers a deal that removes penalties at an undisclosed cost shown at the end (the Deal Ending) [V3 PLw Endings, Theatre]. Bound who die stay dead and are absent from the ending. A Late Ending (credits, no choice) follows missing the courier by 22:00 on Day 11. The two real endings are Diurnal (deliver the Inquisitor's orders, destroy the Polyhedron) and Nocturnal (burn the papers, keep it) [V3 PLw Plot, Endings]. Recovery from penalties: new save file only.
#### 7. Consequential vs cosmetic choices
- **Time allocation** is the real currency: the clock shortens each day and quests expire unannounced; this is the stated design [V3 PLw Game_Mechanics Time, Core Gameplay].
- **Bound triage** is mechanically real: immunity range, hidden infection value 1-100, and a death roll at midnight; prophylaxis and antibiotics move the odds; reloading after 07:30 does not reroll [V3 PLw Game_Mechanics]. The midnight animation itself is cosmetic (outcome fixed).
- **Quarantine-style forks** shift the district schedule: the House of Death (Day 3, Crude Sprawl), giving Lara a water barrel (Day 4, Flank), reporting the Chemist (Day 5, Bridge Square) [V3 PLw Plague]. The Bachelor's quarantine orders on Days 3-4 are scripted, not player-set.
- **Reputation** is a per-district gate: at "Unwelcome" (25-40%) you are denied stores and adult trading, at "Hated" (25% or less) the militia attacks, and a newly infected district resets to 40% [V3 PLw Game_Mechanics]. Murder is the largest single penalty (-50% if witnessed); Steppe/Station/Factory/Warehouses/Cape have no reputation, which makes them exploit zones.
- Cosmetic: first stop on Day 1, kill-or-spare Piecework (the house is lootable either way [V3 PLw Plot]).
#### 8. Open items
- "Twelve days": the plot summary says twelve days, but the playable calendar is Days 1-11 and "Day Twelve, in which the lights die out" is the ending text [V3 PLw Plot]. Treat Day 12 as the ending scene [CONTESTED between brief and wiki].
- Not established: patch/version, any difficulty setting, the money system's fluctuation rule, how many Bound P2 itself uses (the Bound page lists 24 in three groups, 8+7+9, and is tagged for Pathologic, Pathologic 2 and The Marble Nest [V3 PLw Bound]).
- v2 R7 cells: K3 6.5 h / 16.5 h, K5 sleep list and rates, G3 deaths list, Bound immunity ranges, and midnight list all confirmed [V3 PLw Game_Mechanics]. I3 rumours: no rumour mechanic found in the pages read; `?` stays.
- Attachments: `grep -i pathologic` found only "pathological" in the Citizens file (about The Guild 2, not this game).

### Vampire: The Masquerade - Bloodlines - facts line
Troika Games (publisher Activision, Source engine); first/third-person action RPG; released 16 Nov 2004 (NA) [V3 VTf Vampire:_The_Masquerade_-_Bloodlines rev 2026-02-02]. Version relied on: the shipped game plus the community Unofficial Patch, latest 11.5 of 28 Aug 2024 per its wiki page rev 2026-02-19 [V3 VTf Unofficial_Patch]; "Plus" extras are marked. Mode: single player, any of the seven Camarilla clans. Play length not established from a source: [M] roughly 25-35 h for a first run. Mostly V3 (wiki pages and the game's own loading-screen tips, which the wiki transcribes) plus one community guide.
#### 1. Setup choices
- **Gender**: male or female (the first wizard question) [V3 VTf Character_Creation_Wizard]; the community guide says Seduction is "more useful as a female character", and the Character Sheet recommends Appearance for female characters [community; V3 VTf Character_Sheet].
- **Method**: answer the Character Creation Wizard (7 of 56 questions; it ends by offering the two clans that fit your answers) or skip it to the Character Sheet [V3 VTf Character_Creation_Wizard].
- **Clan** (7), each with 3 in-clan Disciplines and a curse [V3 VTf Clan pages, Clan_Curse]:
  Brujah (Celerity, Potence, Presence; -2 on frenzy checks), Gangrel (Animalism, Fortitude, Protean; -1 on frenzy checks, +5 Strength/Wits/Stamina while frenzied), Malkavian (Auspex, Dementation, Obfuscate; madness: unique, hard-to-read dialogue, +2 Inspection), Nosferatu (Animalism, Obfuscate, Potence; Seduction capped at 0, a human seeing you breaks the Masquerade, so you travel by sewers; rats give 3 blood), Toreador (Auspex, Celerity, Presence; Humanity gains and losses both doubled, Humanity costs half the XP), Tremere (Auspex, Dominate, Thaumaturgy; no Physical attribute above 4), Ventrue (Dominate, Fortitude, Presence; cannot take blood from rats, lowlife blood may make you vomit).
- **Starting points**: each clan gives a different spread of free points across Attributes, Abilities and Disciplines (e.g. Brujah +2 Physical, +1 Mental; 3 Talents, 2 Skills, 1 Knowledge; Toreador +2 Social; Tremere +2 Mental, 3 Knowledges); each point costs 1 and each stat tops out at 5 [V3 VTf The_Protagonist, Character_Sheet; WPvt].
- **Histories**: an optional biography with one plus and one minus. Cut from the 2004 release; restored by the Plus patch [V3 WPvt; VTf Unofficial_Patch].
- **Patch**: install the Unofficial Patch, then choose Basic (fixes) or Plus (fixes plus restored content, rebalancing, extra endings, Histories) [V3 VTf Unofficial_Patch]. Community: Basic for a first run, and Plus needs a new game if added later [S3 search summary of community posts].
- No difficulty slider found `?`.
#### 2. The loop
Clock: none. The whole game takes place at night and there is no day counter or timer [V3 VTf game page]. Progress is by quests and by four hubs (Santa Monica, Downtown, Hollywood, Chinatown); earlier hubs stay open [V3 VTf game page].
1. **Haven**: read the email on the haven computer for new orders; return often [V3 VTf Loading_Screen_Tips].
2. **Pick a quest** from the Quest Log (L) in the current hub: main quests and many optional side quests.
3. **Travel the streets**; each area is tagged Masquerade zone, Elysium (no attacks, no Disciplines) or combat area (Disciplines free, no Masquerade breach) [V3 VTf Loading_Screen_Tips].
4. **Resolve each objective** by talking (Persuasion/Seduction/Intimidation/Dominate lines appear only if your feat is high enough), sneaking, lockpicking, hacking, or fighting.
5. **Feed** to refill blood, which pays for Disciplines, Bloodheal and Bloodbuff; humans give about 5-6, rats about 1, blood packs a little [V3 VTf Blood_Points, tips].
6. **Quest done**: XP arrives for completion, side goals and alternate routes, never for kills; spend it any time in the Character Editor (C) [V3 VTf tips, game page].
7. Main quests unlock the next hub and the next faction decision.
Interrupts: scripted ambushes, vampire hunters after a Masquerade breach, frenzy (hunger, pain, humiliation) which seizes control, a Blood Hunt late on. Automated: Defense checks against each attack, vendor prices by Haggle, Bloodheal over time, frenzy risk vs Humanity [V3 VTf tips, Frenzy].
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Choose a dialogue line (constant) | none; gated by feat level | quest branch, alternate solution, XP bonus | every conversation |
| Persuade (blue) / Seduce (pink) / Intimidate (green) / Dominate (constant) | needs the feat; Dominate costs blood and some Disciplines break the Masquerade if seen | non-violent outcome; Seduction lets you feed without a breach [V3 VTf tips] | when the line shows |
| Feed on a human (frequent) | risk of being seen (Masquerade); killing costs Humanity | about 5-6 blood | when blood is low |
| Feed on rats / blood pack (frequent) | time; little blood; Ventrue cannot | about 1 blood | when no humans are safe |
| Use a Discipline (frequent) | blood equal to its level [V3 WPvt]; barred in Elysium | combat, stealth or control effect | fights, infiltration |
| Bloodheal / Bloodbuff (frequent) | blood | heals over time / temporary physical boost, e.g. to Dexterity for lockpicking | after damage, at locks |
| Sneak, then ambush (frequent) | Sneaking feat, crouch, light meter | instant kill or bypass | guarded areas |
| Fight: melee, ranged or unarmed (frequent) | damage taken; weapon and ammo; Humanity if the victim is innocent | clears enemies; no XP for kills | forced fights |
| Lockpick / hack (frequent) | Dexterity+Security / Wits+Computer feats | doors, caches, computers | gated areas |
| Spend XP (every quest) | XP; cost rises as the game goes on [V3 WPvt] | stats, Disciplines, even Humanity | at the haven or any time |
| Buy/sell, skill books, teachers (periodic) | money; Haggle sets prices | gear, ammo, ability points | after loot |
| Spare or kill a target (frequent) | kill: Humanity loss; spare: Humanity gain and XP | quest path, dialogue tone | quest forks |
| Protect the Masquerade (continuous) | avoid public powers; clean-up quests | keep or reinstate Masquerade points | in public zones |
| Pick a faction/ending (once) | late-game commitment | one of five endings (seven with Plus) | final act |
#### 4. First hour, step by step
Sources: the wiki quest pages and tips [V3 VTf Jyhad_for_Beginners, Wherefore_Art_Thou,_Mercurio?, Loading_Screen_Tips] and the 2020 community guide [V3 https://morrowindnostalgia.bearblog.dev/vampire-the-masquerade-bloodlines-beginners-guide-2020-edition/ 2020-04-12, community].
1. Install the Unofficial Patch and start a new game. Choose a gender and either take the wizard or build by hand.
2. Pick a clan. Community consensus for a first run: Brujah, Tremere or Toreador; Malkavian and Nosferatu are harder and "typically recommended for a second playthrough" [community].
3. Spend your points: at least one combat feat, some Persuasion (the guide calls it "almost mandatory"), and one point toward Lockpicking (Bloodbuff boosts it) [community].
4. Watch the Embrace and the Camarilla trial: your sire is executed and Prince LaCroix spares you at Nines Rodriguez's urging [V3 WPvt].
5. Play the tutorial quest "Jyhad for Beginners" with Smiling Jack: feed on a human, lockpick, hack the tutorial computer, feed on the homeless man, sneak past the Sabbat, fight the gang; reward 2 XP [V3 VTf Jyhad_for_Beginners].
6. LaCroix sends you to Santa Monica; your haven is above Trip's Pawnshop. Read the email, take the cash and three blood packs from the fridge [V3 VTf Wherefore_Art_Thou,_Mercurio?].
7. Read the newspaper and the note by the computer: each starts a side quest (Carnival of Death, The Regent's Riddle).
8. Visit Mercurio at 24 Main Street, room 4 (+1 XP); he asks you to get his Astrolite from thugs at the beach house (Surf's Up).
9. Open the Quest Log (L), the Character Editor (C) and the power menu (K); use TAB to block.
10. Learn the zones: in Elysium you cannot attack or use Disciplines; seduce a human or use a combat area to feed without a Masquerade breach.
11. Do Surf's Up, then "Explosive Beginning": persuade the Voerman sister and Bertram Tung to end their feud; killing no one gives an XP bonus (8-9 XP total) [V3 VTf Explosive_Beginning].
12. Spend XP, then take the remaining Santa Monica quests in any order before moving Downtown.
#### 5. What changes later
Downtown brings the Ankaran Sarcophagus plot, then Hollywood and Chinatown; Sabbat, Anarch, Kuei-jin and Prince LaCroix all want your allegiance; the guide says the endgame "will force you towards combat more and more" [community]. Upgrade costs rise as the game progresses [V3 WPvt], Disciplines run in levels up to five and cost blood equal to their level [V3 VTf Disciplines; WPvt], and Humanity drift changes available dialogue [V3 WPvt]. The Plus patch adds restored quests, Sabbat and secret Malkavian endings, an optional post-game [V3 VTf Unofficial_Patch].
#### 6. Failure and ending
Loss: lose all five Masquerade points ("you will lose the game": the loading-screen text says you are summoned to account) [V3 VTf Loading_Screen_Tips]; also ordinary death (reload; [M] save anywhere); frenzy can ruin a scene. Humanity at its minimum does not end the game on the game page, but see section 8. Win: five endings (Camarilla, Kuei-jin, LaCroix, Anarch, personal), plus Plus-only Sabbat and Malkavian secret endings; the plot is non-linear in side content but "the overall plot line does not change" and core missions are mandatory [V3 VTf game page]. Recovery: Masquerade points are reinstated by protecting it; Humanity rises by kindness and XP [V3 VTf game page, tips].
#### 7. Consequential vs cosmetic choices
- **Clan** is the one irreversible build choice: three Disciplines, a curse, different dialogue (Malkavian) and closed doors (Nosferatu cannot be seen); Nosferatu and Malkavian are "second playthrough" clans by community consensus.
- **Persuasion** unlocks alternate solutions and Seduction is OK; **Intimidation** is cosmetic, "only useful for roleplay" (community guide, not tested by me).
- **Humanity** matters through frenzy risk and dialogue tone; buying it with XP works but the guide advises against, since club dancing and kind acts raise it [community].
- **Masquerade** is a hard lose-state, but zone discipline (no powers in public) avoids it nearly always.
- Cosmetic or dominated: **Haggle** (cash becomes plentiful), **Stealth** past a point (Obfuscate replaces it), and **Histories** (community: skip on a first run).
#### 8. Open items
- [CONTESTED] Humanity floor and effect: game page says minimum 3 and the game does not end; Character Sheet says zero means frenzy; Wikipedia says losing all Humanity ends the game; the wiki Humanity page is tabletop (0-10), not the game [V3 VTf game page, Character_Sheet, Humanity; WPvt]. Unofficial Patch 4.1 notes reportedly "prevented Humanity from reaching zero" [S3 search snippet of gamebanshee.com/h9d3]. Starting Humanity, per-act deltas, and whether blood drains passively were not found `?`.
- v2 R7 H3/J3/J1 cells confirmed: five Masquerade points, one lost per breach, zero loses [V3 VTf Loading_Screen_Tips]; 3 Disciplines per clan; frenzy mods Brujah -2, Gangrel -1 [V3 VTf Frenzy, Clan_Curse]. v2 "Unofficial Patch wiki not reachable": now read, latest 11.5 (28 Aug 2024), Basic/Plus split [V3 VTf Unofficial_Patch].
- Not established: official patch numbering (the Unofficial Patch page says one official patch; True Patch says prerequisite 1.1) and save rules.
- Attachments: grep for Bloodlines/VTMB/Vampire over the four uploads found no claim.
