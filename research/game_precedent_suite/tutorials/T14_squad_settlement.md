# T14 - Squad/settlement tutorials (v3): Jagged Alliance 2 (+JA3 note), Medieval Dynasty, Dawn of Man, The Guild 2, The Guild 3

Tags: [V3 url date/version] read in a fetched page body this session; [S3 url] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED].
Shorthands (each is a full [V3] tag when followed by a page name): **D113** = https://1dot13.github.io/documentation/ (official 1.13 docs site, pages dated 2026-07-10/11, claims verified by its authors against 1dot13 GitHub source/data);
**O113** = https://raw.githubusercontent.com/1dot13/gamedir/master/Data-1.13/Ja2_Options.INI (shipped default INI, fetched 2026-10-22).
Capability-id line = ids B, C, D, F, L only, read by id meaning in `../tables/R1`/`R8`/`I1` (B1 roster view, B2 hire/recruit, B3 appoint, B4 give orders, B5 standing delegation, B6 loyalty/morale/opinion, B7 succession; C1 found, C2 build, C3 upgrade, C4 layout, C5 chains, C6 logistics, C7 garrison; D1 laws, D2 tax/ration, D3 offices, D4 unrest, D5 vote, D6 courts; F1 raise troops, F2 composition/officers, F3 posture/orders, F4 tactical battle, F5 player-controlled battle, F6 seize/siege, F7 supply, F8 aftermath; L1 ambitions/traits, L2 aging/death, L3 kin, L4 narrative events, L5 autonomous NPCs). No v2 table exists for these games, so nothing below "corrects" a cell.

---
### Jagged Alliance 2 (+ JA 1.13 community build; JA3 note at the end of section 8) - facts line
Sir-Tech Canada, 1999; turn-based squad tactics with a real-time-with-pause strategic map [V3 en.wikipedia.org/wiki/Jagged_Alliance_2 raw 2026-10-22]. Relied on: the 1.13 GitHub-era build as documented in D113 (docs dated 2026-07-10/11) and shipped defaults in O113; vanilla differences are flagged. Assumed: Experienced difficulty, Save Anytime, classic chance-to-hit (OCTH), Sci-Fi style, squad size 10, Drassen counterattack ON (the docs' own first-campaign suggestion is to switch it off) [V3 D113 getting-started/tutorial]. One session ~1-2 h of play; a full campaign is dozens of hours [M]. This tutorial is mostly [V3] (the 1.13 docs are an unusually complete primary source).
#### 1. Setup choices
1. **Difficulty** (locked for the campaign): Novice / Experienced (default) / Expert / Insane. Changes starting cash $45,000 / $35,000 / $30,000 / $15,000; Queen's troop pool 150 / 200 / 400 / unlimited; garrison strength 70 / 100 / 150 / 200%; Drassen counterattack 24 / 40 / 60 / 96 soldiers in 4 groups; merc deaths tolerated 2 / 4 / 6 / 8; grace before she can retake a sector 144 h (Novice) to 6 h (Insane) [V3 D113 playing/new-game-options, playing/economy, playing/features/strategic-war, getting-started tips].
2. **Skill Traits** Old/New; **Game Style** Realistic/Sci-Fi; **Extra Difficulty** Save Anytime / Iron Man / Soft Iron Man / Extreme Iron Man (saves only at one fixed hour); **Inventory/Attachments** Old-Old / New-Old / New-New; **Item progress speed** Very Slow..Very Fast; **Arsenal** Reduced / Tons of Guns; **Max squad size** 6/8/10; **Bobby Ray Quality/Quantity** 1-10 [V3 D113 playing/new-game-options].
3. **1.13 Features toggles** (override INI): NCTH aiming, Drassen/city/multiple counterattacks, prisoners, food, disease, dynamic opinions, Kerberus, enemy officers/assassins, intel... [V3 D113 same page].
4. **Your own merc (I.M.P.)**: $3,000 once, no salary; 500-point attribute pool, each 35-85; traits, disability, background, 20 portraits / 15 voices [V3 D113 tutorial step 5].
5. **Starting team from A.I.M.**: pick up to ~5 mercs with a contract of 1 day / 1 week / 2 weeks and one of up to 5 gear kits each; M.E.R.C. (cheap, billed daily) opens later [V3 D113 tutorial step 6; playing/features/hiring].
#### 2. The loop
Clock: strategic map runs in **real time with pause and time compression** (Space toggles); contact switches to **turn-based tactical** (action points); militia-only defences can be auto-resolved [V3 D113 tutorial; playing/features/militia].
1. Laptop/map: choose squads, plot routes, set assignments (Doctor, Repair, Train, Militia, Patient, Sleep...; an assignment needs 45 min to count) [V3 D113 playing/features/facilities].
2. Time runs. The game automatically: accrues M.E.R.C. daily bills, pays mine income at 09:00/12:00/15:00/18:00, charges militia upkeep at midnight ($10/$20/$30 green/regular/elite; unpaid militia desert), recomputes team morale hourly [V3 D113 economy, militia, morale].
3. The Queen's AI takes one decision per interval (8 +/-4 h Novice down to 90 +/-60 min Insane): reinforce, refill a patrol, or attack a sector you took once its grace period ends [V3 D113 strategic-war].
4. Contact: pre-battle box offers Auto-resolve / Enter sector / Retreat; entering starts turn-based play, each merc spends AP to move, aim, burst, change stance; unspent AP can trigger interrupts [V3 D113 playing, tutorial step 7; defeat].
5. After the fight: loot, sell, talk to NPCs, restore a mine (head miner), retrain, heal; then back to 1. Contracts expire with a popup; you extend or dismiss on the map screen [V3 D113 hiring].
6. Interrupts: Queen counterattacks, mine depletion (one mine runs dry: Drassen after 20 days of full output, others 10), random events, merc quitting over morale or hated colleagues [V3 D113 economy, morale].
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Move squad / plot route | game time; risk of contact | take or avoid sectors; Shift = direct route | constant |
| Tactical action (move, stance, aim, burst, suppress, throw) | AP per action | resolve the fight turn by turn | constant in fights |
| Assign merc (Doctor/Repair/Train/Patient/Sleep) | merc time, fatigue | heals, repairs, trains stats | constant |
| Hire from A.I.M./M.E.R.C./I.M.P. | fee per 1d/1w/2w; M.E.R.C. daily bill; IMP $3,000 | adds a named merc (traits, buddy/hated lists) | early, then when someone dies/expires |
| Extend / dismiss contract | salary rises +25% per experience level gained | keep or lose a merc | every 1-2 weeks |
| Train militia (town sector) | $750 per session of up to 10; trainer Leadership >= 20; town loyalty >= 20% | green, then regular; elite training off by default | after each town capture |
| Redistribute / move militia | free (strategic command is off by default) | spreads garrison over a town's sectors | after training |
| Auto-resolve vs enter vs retreat | retreat -5 morale; abandoned militia = up to -7.5 loyalty everywhere | choose how a battle is fought | each attack |
| Order Bobby Ray's | gun prices + shipping (unlocked by Drassen airport) | arms/ammo/armor | each town |
| Sell loot | Alt+click 10% of value; dealer Tony 75% (wallet $15,000/day) | converts captures to cash | after battles |
| Squad composition (split hated pairs, add squadleader) | none | morale and who quits | when forming squads |
| Talk to NPCs / quests / recruit rebels | time | mine access, free recruits, loyalty boosts | rarely, mostly early |
| Take prisoners / interrogate (optional) | needs prison; riot risk | ransom 25%, intel 25%, defect to militia 25% | rarely |
| Kerberus (optional): buy militia | $440 per regular, $810 per veteran; -0.1/-0.15 loyalty everywhere | instant militia in ~24 h | rarely, when rich |
[V3 D113 economy, militia, hiring, morale, defeat, strategic-war, tutorial]
#### 4. First hour, step by step
Source: the official 1.13 guided tutorial [V3 D113 getting-started/tutorial, 2026-07-11].
1. Start New Game, accept Experienced / Save Anytime / New traits / Tons of Guns / highest squad size; set resolution (higher unlocks bigger squads).
2. The game opens on the laptop: read e-mail (contains the I.M.P. access code XEP624).
3. Build your I.M.P. merc for a flat $3,000; a dependable shooter (Marksmanship, Health, Dexterity, Agility).
4. Hire 4-5 cheap A.I.M. mercs covering roles: medic (MD, Fox, Spider), technician (Barry, Vinny), fighters (Igor, Grunty, Buns, Grizzly, Meltdown). Keep a cash reserve for militia.
5. Close laptop; mercs helicopter into Omerta (A9). Press Space to wait; combat starts when enemies sight you.
6. Fight the Omerta garrison: use cover/low stances, keep some AP in reserve for interrupts, aim before shooting.
7. Talk to Fatima, go to A10, deliver the letter to Miguel's rebels; Ira can join.
8. Plot a route to Drassen (B13 airport, C13 residential, D13 mine) and take the sectors; the airport opens Bobby Ray's.
9. In D13 talk to the head miner or the mine pays nothing; mine income now funds everything.
10. Give a leader the Militia assignment in a Drassen sector ($750 per session).
11. Order ammo, optics, armor from Bobby Ray's, shipped to Drassen.
12. Prepare for the counterattack (4 groups converge on the mine sector): concentrate militia in the mine sector and its neighbour, put mercs in cover BEFORE compressing time, or set TRIGGER_MASSIVE_ENEMY_COUNTERATTACK_AT_DRASSEN = FALSE.
13. Survive; you now hold a town, airport, mine, income and garrison.
#### 5. What changes later
Mid game: Cambria, Alma, Grumm; late: Tixa, Orta, Estoni, Balime, Meduna [V3 D113 walkthrough/mid-game, late-game]. Enemy gear improves with hidden "progress" (grows with kills, mine income, towns) so week-one pistols give way to assault rifles on both sides; the AI upgrades admins to troops; offensive stages at progress 65 / 85 [V3 D113 playing; strategic-war]. Salaries grow as mercs level; Tixa and Orta cannot hold militia and are counterattacked persistently [V3 D113 late-game]. Optional layers (all FALSE by default unless noted): food, disease, prisons, intel, Rebel Command, militia volunteer pool, strategic militia command.
#### 6. Failure and ending
No game-over screen on a team wipe: you drop to the map and can hire a fresh team if you have money; capture sends 2-3 downed mercs through Alma -> Tixa -> Meduna prisons, to be rescued; Iron Man modes make a wipe the real game over [V3 D113 playing/features/defeat]. Win: kill Queen Deidranna in Meduna; the campaign ends the moment she dies [V3 D113 walkthrough/late-game "Victory"]. Recovery is usual; the only soft-locks are money gone plus contracts lapsed.
#### 7. Consequential vs cosmetic choices
- Consequential: squad chemistry (hated-colleague timers make a merc refuse renewal or quit; a buddy's death is -15 morale) [V3 D113 morale]; holding mines/towns (income scales with loyalty x share of town held) [V3 economy]; militia spending vs mercs; difficulty/starting cash.
- Consequential but a trap: killing civilians (-5 team morale, loyalty and opinion hits) and abandoning militia (loyalty hit equal to a lost battle) [V3 morale, defeat].
- Cosmetic-ish: Game Style, most gear kit choices, portrait/voice. Near-dominant: bring a medic and cover (community-written docs advise two medics) [V3 tutorial table]; locals are free recruits. Dominant-answer claims here rest on the docs' own tips, i.e. community consensus.
#### 8. Open items
- Capability ids (tag [V3 D113]): B1 YES (laptop Personnel, MeLoDY) B2 YES (A.I.M./M.E.R.C./I.M.P./locals/Kerberus) B3 NO (no offices; assignments only) B4 PART (squad orders; militia tactical orders menu) B5 PART (assignments run unattended; strategic militia command off by default) B6 YES (morale 0-100, +/-25 opinions, loyalty %) B7 NO | C1 NO C2 PART (Fortify assignment, sandbags only) C3 NO C4 NO C5 NO C6 PART (Get Item between town sectors; Bobby Ray shipments) C7 YES (militia garrisons, reinforcement from adjacent sectors) | D1 NO D2 NO D3 NO D4 PART (town loyalty %, no unrest events) D5 NO D6 NO | F1 PART (train/buy militia) F2 PART (tiers green/regular/elite; individual militia optional) F3 PART (militia orders, squadleader) F4 YES (turn-based AP tactics) F5 YES F6 YES (take sectors) F7 NO F8 YES (captured, morale, loyalty) | L1 PART (backgrounds, traits, personalities) L2 PART (death only; no aging) L3 NO L4 PART (random events system) L5 PART (mercs quit, AI patrols).
- **Attachment claims** (`e3f9f19a-thirteen_strategy_games.md`):
  - `:22` roster "18 vanilla, about 32 in 1.13" (TV Tropes): vanilla 18 [S3 tvtropes.org/pmwiki/pmwiki.php/VideoGame/JaggedAlliance]; **1.13 current default is 40** (valid 16-254) at `MAX_NUMBER_PLAYER_MERCS = 40` [V3 O113 line 173]. 32 is stale/older-build; a Nexus mod snippet says "increased from 32 to 80" [S3 nexusmods.com/jaggedalliance2/mods/10]. Verdict: partly stale.
  - `:22` squad size 6/8/10 tied to resolution: confirmed that sizes are 6, 8, 10 and resolution-bound. Thresholds [CONTESTED] inside D113: tutorial says 640x480 = 6, 800x600 = 8, 1024x768 = 10 [V3 tutorial step 2]; new-game-options says 6 / up to 8 from 800x600 / "1280x720 and above allow 10" [V3 playing/new-game-options].
  - `:20` "difficulty above Expert, INSANE, more and better enemies with unlimited reinforcements": confirmed; Queen pool flagged unlimited on Insane [V3 strategic-war]. Drassen counterattack switch name confirmed.
  - `:25` "Towns yield daily tax scaled by population and loyalty": NOT FOUND. Income is from mines only, scaled by town loyalty x fraction of the town you hold; no population term, no town tax (optional worker layer is off by default) [V3 economy]. Mark wrong.
  - `:25` "1.13 adds Mobile Militia that patrol between sectors": true only of old SVN builds; self-roaming mobile militia was removed March 2018 (r8548); current builds only move militia when you order it (and strategic militia command is OFF by default) [V3 playing/features/militia].
  - `:22` 1.13 backgrounds ("former profession such as SWAT officer or drill sergeant... small bonuses and penalties"): confirmed verbatim [V3 playing]; ENABLE_BACKGROUNDS on by default.
- **Repo claims** (REPO_MENTIONS s3 -> `research/valoria_game_precedent_companion_v1_part5.md:118,147,170`):
  - "Five-layer morale stack": morale = default 50 + team modifier + tactical modifier + strategic modifier + campaign-progress bonus (to +20) + drug/alcohol effects + Walkman (+20%): five or seven layers by how you count [V3 D113 playing/features/morale]; no single "five" in source.
  - "+/-25 pairwise opinion matrix": confirmed (-25 hatred to +25), matrix in MercOpinions.xml, externalised from vanilla prof.dat, so the base matrix predates 1.13; the dynamic layer is 1.13's (Flugente, 2014) [V3 same page].
  - "audit tool itemising every pairwise opinion by source": confirmed as MeLoDY's Pairwise comparison page [V3 same page]. "Hidden tolerance clock: No": the hated-merc tolerance (hours) exists and complaints begin at half; MeLoDY "shows the timers ticking", so it is not hidden once MeLoDY is open [V3 morale].
  - "Docks merc morale and town loyalty after three days without offensive action": morale confirmed (MORALE_PLAYER_INACTIVE = -3 after 3 days) [V3 morale; Morale_Settings.INI raw 2026-10-22]; **town-loyalty half NOT FOUND** in D113 or either INI; flag as unverified.
  - "Militia ~$75/head vs regulars ~$440": $750 per session of up to 10 = $75/head [V3 militia]; Kerberus regular = $440 (veteran $810) [V3 hiring]. Confirmed; note the $440 buys a regular, the $75 buys a green who then needs a second paid session. "2x daily upkeep ($40-60 vs $20-30)" holds only with the off-by-default INDIVIDUAL_MILITIA option; default Kerberus hires cost the same $20/$30 [V3 hiring]. "Loyalty 0.1 per regular, 0.15 per veteran, global" confirmed [V3 hiring].
  - JA3 "liked squadmate +1 AP / disliked -1 AP": a player guide says liked mercs give a morale bonus and disliked ones -1 morale, extra pay demands or refusal to join [S3 commonsensegamer.com/jagged-alliance-3-merc-relationships-and-affinities-full-guide, 2023-07-27, read]; AP wording not found `?`.
- **JA3 note** (Haemimont/THQ Nordic, 2023): isometric turn-based squad tactics on a strategic sector map with a roster of 40 mercenaries, each with personality and like/dislike preferences; side missions with consequences [V3 en.wikipedia.org/wiki/Jagged_Alliance_3 raw 2026-10-22]. Not played here; no more detail established.

---
### Medieval Dynasty - facts line
Render Cube / Toplitz Productions; first-person survival + village-building RPG on Unreal Engine 4; Early Access 2020-09-17, 1.0 on 2021-09-23, consoles 2022 [V3 en.wikipedia.org/wiki/Medieval_Dynasty raw 2026-10-22]. Version: update 2.7.0 "Wild Game" (2026-09-22), hotfix 2.7.0.4 (2026-10-07) [V3 Steam news app 1129580, fetched 2026-10-22]. The fan wiki I read (**MDW** = medieval-dynasty.fandom.com via api.php, read 2026-10-22) mixes stamps: chapter pages say v1.1.1.0, the Dynasty Reputation page is banner-marked "outdated"; every number below from MDW is therefore community-wiki, version-uncertain. Assumed: The Valley, Normal difficulty, single player, default 3-day seasons. Clock: 1 in-game hour = 2 real minutes, so a default day is 48 min, a season 2.4 h, a year 9.6 h [V3 MDW Seasons]. One session ~1-2 h; a first full year ~10 h.
#### 1. Setup choices
1. **Map/origin**: The Valley (fixed hero Racimir, uncle's murder plot), The Oxbow (customisable character, can be female, heir sex choice, co-op available), The Backwood (free DLC map, 2026-06-11, with a Creative Mode ignoring money, resources and reputation) [V3 wikipedia; Steam news 2026-06-11].
2. **Difficulty preset** Easy / Normal / Hard / Custom, which sets: tax multiplier, building limit (up to 200%), events on/off, unlimited health/stamina/carry weight, no hunger/thirst, poisoning, temperature, fast crafting, XP multiplier, technology multiplier, Dynasty Reputation multiplier, bandits, season length 1-30 days [V3 MDW Customization, Seasons]. Most can be changed later; difficulty only at new game.
3. No class/faction pick: you choose your first job by what you do (hunt, craft, farm).
#### 2. The loop
Clock: real time (no turn structure); day/night; four seasons; year ends with tax due [V3 MDW Seasons].
1. Daytime: you gather (sticks, stone, straw, logs), hunt, craft, build, fight animals and bandits yourself, talk to vendors/quests.
2. Villagers (once recruited) wake at 7:00, work 08:00-18:00 at the building and profession YOU assigned; output accrues at fixed rates (farmers only while animating); innkeepers to 22:00 [V3 MDW Profession].
3. Automated: villagers draw food, water and firewood from storages, repair via Builder, sell via Stallholder, women get pregnant, children age; mood updates continuously.
4. Season change: you auto-sleep, wake in your house; a random event may fire (Herald, famine, etc.); new side quests appear, unfinished ones from last season FAIL (reputation loss) [V3 MDW Seasons, Dynasty Reputation].
5. Each spring: last year's tax (per started building x development-stage multiplier, plus crops) auto-starts "Pay taxes"; unpaid by end of spring becomes debt and cuts reputation [V3 MDW Tax].
6. Control returns to you every moment; interrupts are events, bandit raids, Herald challenges, hunger/cold/stamina on the player character.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Gather/hunt/chop/mine by hand | stamina, daylight, carry weight | raw materials, food, hides | constant early, less later |
| Craft tools/weapons/clothes | materials, tech points | better tools, hunting, warmth | constant |
| Place/build a building (houses, storages, woodshed, barn, hunting lodge, workshop...) | materials; counts against the building limit | new capacity, jobs; tiers I-III | constant |
| Upgrade/replace to higher tier | materials; reassign workers | more workers, durability | mid game |
| Recruit a villager | Dynasty Reputation (price rises per head), free house with food/firewood | +1 worker | each growth step |
| Assign house and profession | free; wrong skill = lower mood and yield | decides output | constant |
| Set production orders / sow fields / People's Demand Control | none | what workers make and eat | constant |
| Do chapter/side quests | time, goods | Dynasty Reputation (the only real source), building limit stage | constant |
| Accept King's challenge (Herald) | large resource delivery | rep + king favour (lower tax) or loss | yearly, optional |
| Trade/sell (vendors, market stall) | goods | coins | constant |
| Flirt, gift, marry, have child | time, gifts (1/season per child) | wife, heir, mood +10%/+5% per child | once per generation |
| Pay tax | coins in spring | avoid debt | yearly (forced) |
| Spend skill points | points | six trees, perks | on level-up |
| Steal | none | gain; reputation loss if seen | rarely (trap) |
[V3 MDW Mood, Profession, Tax, King, Skills, Management]
#### 4. First hour, step by step
Source: MDW Getting Started (flagged stub) and chapter quest pages [V3 MDW Getting_Started, Starting a New Life, A New Beginning, A Survivalist].
1. Talk to the castellan Uniegost near Gostovia ("Starting a New Life"); receive a wooden hammer.
2. Pick up sticks and stones; craft a stone axe (10 sticks + 2 stones).
3. Chop ~5 trees for 6 logs; cut reed at the river for straw (32 needed).
4. Open the quick menu (Q) and lay the foundation of your first house; hammer walls and roof ("A New Beginning": 10 reputation, building limit 5).
5. Eat; the starting food lasts about two days. Set a rabbit trap, make a spear and stone knife, hunt one animal ("A Survivalist": survive one season).
6. Craft stone knives and sell them for coins; buy onions, plates, a large backpack/pouch.
7. Do three neighbour quests, spend a skill point, flirt once ("Good Morning My Neighbours": 50 reputation, stage Small Farm).
8. Build a Resource Storage first (your house chest fills), then Food Storage and Barn; plant cabbage in the first season.
9. Build a Hunting Lodge and hunt three fox/boar ("Into the Wilderness"), then fields ("A Farm").
10. Winter: stock firewood and food before inviting anyone; expect first tax in spring.
#### 5. What changes later
Chapters pay Dynasty Reputation 10, 10, 20, 50, 100, 250, 500, 750, 1,000, 2,500, 5,000 (about 10,190 total) and raise the building limit stage by stage (quest pages: 1, 5, 10, 15, 25, 35, 45, 55, 65) [V3 MDW chapter pages, v1.1.1.0]. Villagers: 2 residents then 10 inhabitants with 5 workers, tier-II/III buildings, iron and tools, King's challenges, naming the village and a crest, a wife and an heir ("The Dynasty Continues"). Pressure ramps via tax multiplier (x0.10 Hermitage to x2.00 City), reputation price per head, food/firewood demand, pregnancy gaps [V3 MDW Development Stage, Dynasty Reputation].
#### 6. Failure and ending
Loss: dynasty reputation reaching -10,000 (unpaid tax debt, theft, failed side quests) exiles you from the valley, game over; villagers whose mood hits -100% leave and cost reputation; player death continues as the heir if one exists [V3 MDW Dynasty Reputation, Tax, Mood, Heir]. No scripted win after the main chapters; sandbox continues generation to generation.
#### 7. Consequential vs cosmetic choices
- Consequential: who lives with whom and who does which job (job matching = +2% mood per skill point up to +20%, and mood scales speed +/-20%) [V3 MDW Mood]; keeping food/water/firewood stocked; doing side quests before the season ends; when to have children (a mother is off work about two years) [V3 Villager].
- Consequential, partly hidden: reputation price per head grows steeply, so population is gated by quest activity, not by economy [V3 MDW Dynasty Reputation].
- Cosmetic: house decorations beyond 20 (+10% cap), crest, most clothing, naming. House size has "no direct effect" on mood [V3 MDW Mood].
- Dominant answer (community consensus, not tested): build resource/food storage and woodshed early and run the earliest farm.
#### 8. Open items
- Capability ids [V3 MDW unless noted; NO = not found in pages read, not proof]: B1 YES (Management tab: age, mood, job, skills) B2 YES (invite travellers, rep-gated) B3 YES (home/job assignment) B4 PART (per-building orders) B5 YES (fixed-rate production unattended) B6 YES (mood -100..+100, leave at -100) B7 YES (heir takes over at 18 or on death) | C1 PART C2 YES C3 YES (tiers) C4 YES (free placement) C5 YES (ore to bars to tools) C6 PART (storages; no routes) C7 NO | D1 NO D2 PART (imposed yearly tax, multiplier editable) D3 NO D4 PART (mood leave, rep penalty) D5 NO D6 NO | F1-F3 NO F4 PART (first-person fighting) F5 PART F6-F8 NO | L1 PART (6 skills, preferred jobs) L2 YES L3 YES L4 PART (seasonal events, Herald) L5 PART (schedules, pregnancies).
- **Attachment claims** (`9226007a-Citizens...Nine_Titles.md:201-224`, `:559-565`; `89a3a060-consolidated_twenty_games.md:115,159-162,208`):
  - Mood -20% to +20% on production, trading, repair speed: confirmed by MDW Mood table (Production, Trading, Repairing: -20% at -100%, +20% at +100%) [V3 MDW Mood]. Attachment's "documented in update notes": not found in the latest 100 Steam news posts (no "mood" hit) `?`. Community-wiki only.
  - Mood sources: confirmed insulation (+1% per point above 50, max +50%), decorations (+0.5% each, max +10% at 20), job-skill match (+2%/skill point, max +20%), marriage +10%, each child +5%, season events, King's personality [V3 MDW Mood]. "Each child up to two": cap not found `?`.
  - Reputation breakpoints: MDW lists adult population 7 / 15 / 17 / 23 / 35 / 46 at 300 / 1,100 / 1,500 / 3,000 / 9,000 / 20,000 (then 67,500), costs 50/100/200/250/500/1,000/2,500 per head; same page says "This guide is outdated, you now need less" [CONTESTED / stale].
  - -10,000 banishment: confirmed, two MDW pages [V3 MDW Dynasty Reputation; Tax]; theft and failed side quests confirmed; tax debt also cuts reputation (not in the attachment).
  - Building cap "performance guard, raise at your own risk, community manager": a developer quote with that rationale appears in a Steam thread [S3 steamcommunity.com/app/1129580/discussions/0/6918175214328335606/]; speaker's title not shown. Cap values [CONTESTED]: quest pages 65 at final chapter, Development Stage page 70 (City), a forum snippet 70 default and 140 at 200% [S3 same search]; MDW Customization says 65 at 100%.
  - "Skills rise at a rate scaling with coin value of output": not found; MDW says workers get half the player's XP per item and farmers' XP is not shared `?`.
  - "Couples pair off without player instruction": MDW says the player assigns homes (one man + one woman per house) and pregnancy follows co-residence; so the player does decide pairings [V3 MDW Villager, Management]. Wrong in part.
  - "Children's stats average parents'": not found in pages read `?`.

---
### Dawn of Man - facts line
Madruga Works (Spain [M]; Unity engine per Steam news 1.8.0), settlement survival city-builder, Windows/Mac/PS4; Steam release 2019-03-01 [V3 Steam news app 858810, items "Now Available on Steam" 2019-03-01; MDW-style fan wiki **DOMW** = dawnofman.fandom.com via api.php, read 2026-10-22]. Latest build 1.8.4 (2025-10-22, a security/engine maintenance patch); studio has moved to Planetbase 2 [V3 Steam news 2025-10-22, 2026-10-02]. Mostly third-hand: DOMW is thin ("Stub" on most pages) and no official manual was reachable, so the tutorial leans on Steam patch notes, a PC Gamer review and a launch-week fan guide; treat counts as approximate. Assumed: Continental Dawn freeplay, normal (non-Hardcore) mode. Clock: real time with pause (Space) and x1/x2/x4/x8; spring/summer/autumn last 16 min each and winter 32 min at x1, so a year is about 80 min at x1 [V3 DOMW Seasons; How to play guide]. One session ~1-3 h; reaching the Iron Age takes many hours (an achievement exists for all techs in under 6 h) [V3 DOMW Achievements].
#### 1. Setup choices
1. **Scenario**: Continental Dawn (default freeplay), The Northlands (cold, mammoth/rhino/muskox, winter focus), Ancient Warriors (raider-heavy, techs cost more); plus workshop scenarios and a short in-game tutorial ("Ancient Apprentice" achievement) [V3 DOMW Milestones, Achievements; Steam news 1.2.2, 1.3].
2. **Mode**: normal; **Hardcore** (one save slot per game; separate Hardcore milestone achievements); **Creative** (techs half price, rounded up); **Nomad start** available in all freeplay scenarios (Steam 1.3) [V3 DOMW Research, Achievements; Steam 1.0.8, 1.3].
3. Map seed/terrain and raider settings: `?` not established.
#### 2. The loop
1. You pick a place and paint circular **work areas** (gather sticks/flint/stone, fish, berries, hunt, chop, harvest) each with a worker cap and a resource limit; settlers fill them on their own [V3 PC Gamer via Steam news 2019-03-18].
2. Automated: settlers gather, carry to storage, craft (production set by right-click to a limit expressed as % of population), eat, sleep, repair structures at 50% condition, bear children, die [V3 same; DOMW Condition].
3. You respond to alerts: a work area runs dry, someone starves, winter nears, the population hits tent capacity, a trader or raider group arrives [V3 PC Gamer].
4. Knowledge points arrive from doing things (first kills, crafting and building counts at 1/5/10/50/100/500, milestones +2); you spend them in the tech tree to unlock structures, tools, farming, animals, the next age [V3 DOMW Research, Milestones].
5. Seasons rotate: wild game and fruit by season, winter kills; crops sown only in spring (grain, flax) or winter (pulses) [V3 DOMW Seasons].
6. Raiders: periodically a red-clad group attacks; you can sound the Alert (everyone runs home, arms and mans towers); children shelter [V3 DOMW Raiders, Defense, Children].
7. Control is yours throughout; interrupts are alerts, not turns.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Paint/resize/cap a work area | none | directs gathering, fishing, hunting, farming | constantly |
| Set resource limits and production targets (% of pop) | none | stops hoarding/bottlenecks | constantly |
| Place a structure (tent, hut, storage, dryer, granary, mine...) | materials, workers | capacity, production | constantly |
| Research a tech | knowledge points (5 base in Paleolithic; 56 techs) | unlocks the next capability, may trigger extinctions in new ages | every few minutes early, then spaced |
| Hunt dangerous game (mammoth etc.) | injury, death risk | meat, skins, knowledge | early to mid |
| Trade with a visiting trader | 30/40/50% commission | tools, animals, even techs | when prestige draws one |
| Domesticate animals / sow fields | techs, stables, hay | steady food, wool, milk | from Neolithic |
| Build spiritual/megalithic structures (totem, menhir, stone circle, cairn) | stone, logs, sledges, labour | morale recovery and prestige | mid to late |
| Fortify (palisade, wall, gates, watchtowers, platforms) | wood/stone/metal | defence vs raiders | before raids ramp |
| Sound Alert / select hunters and fighters | none | manual combat control | during raids |
| Choose when to advance an era | tech cost | extinctions; harder raiders | judged moves |
[V3 DOMW pages cited; Steam news 1.2.0, 1.6]
#### 4. First hour, step by step
Source: fan guide "How to Survive Your First 5 Years" (launch-week, flagged stub) and PC Gamer [V3 DOMW; Steam news 2019-03-18]. Not an official tutorial.
1. Pause; use Primal Vision (Tab) to see resources and animals.
2. Make a fishing work area at the nearest water and a berry-gathering area.
3. Make flint, stone and stick areas.
4. Set a rock storage zone and a skins dryer; raise the stick limit (you build drying racks from sticks).
5. Build your first structure, a storage tent, from dried skins.
6. Hunt new species for knowledge; unlock Food Drying early, then build a Food Dryer.
7. Add tents/huts to let migrants settle; population growth needs shelter and welfare.
8. Use F4 (limits) to keep tools around 50% spears, 75-100% bows, 25% axes/picks/fishing, 75% sickles of population (a fan rule of thumb) [V3 DOMW How to play guide].
#### 5. What changes later
Six eras: Paleolithic, Mesolithic, Neolithic, Copper, Bronze, Iron; era techs gate the rest; some eras bring extinctions (mammoth and woolly rhino go extinct in the Copper Age) [V3 DOMW Research]. Farming, domestic animals (goat, sheep, pig, cattle, horse, donkey), mines and metal smelting, sledges/carts, watermills; population up to ~300 [V3 Steam 1.4]. Pressure: winter food, prestige (caps 500 buildings, 400 population, 100 era) drawing migrants/traders, raiders increasing from the Copper Age and wearing armour from the Bronze Age [V3 DOMW Prestige; Steam 1.2.0, 1.6].
#### 6. Failure and ending
Loss = everyone dies (starvation, cold, disease, raiders); disease and goat/crop plagues are the common collapse [V3 DOMW Death; RPS via Steam news]. There is no end screen; milestones per scenario (ten each, e.g. 150 people and a cairn) unlock the other scenarios and achievements [V3 DOMW Milestones]. Recovery is possible only while people remain.
#### 7. Consequential vs cosmetic choices
- Consequential: how many hunters/gatherers each work area allows and the limits you set (bad limits cause starvation or tool shortage) [V3 DOMW How to play guide]; population vs winter stores [V3 DOMW Population]; when to enter a new era (extinction timing, raider strength) [V3 DOMW Research].
- Consequential: fortifications before raids scale; dogs early (community consensus).
- Cosmetic: building variants (V key), banners/statues beyond morale recovery.
#### 8. Open items
- Capability ids [V3 unless noted]: B1 PART (stats/activity panels; settlers are individual) B2 PART (migrants come by prestige/welfare; no hiring) B3 NO B4 PART (work-area caps; hunter/fighter selection) B5 YES (work areas + production targets run unattended) B6 YES (morale among seven needs) B7 NO | C1 PART (hearth placement, Nomad start) C2 YES C3 PART (age upgrades of granary/stables) C4 YES C5 YES (grain-flour-bread; ore-bar-tool) C6 PART (carts/sledges, traders) C7 YES | D1-D6 NO | F1 NO F2 NO F3 PART (Alert) F4 PART (real-time melee/ranged, shields, platforms) F5 PART F6 NO F7 NO F8 YES (items drop, morale) | L1 NO L2 YES L3 PART (births) L4 PART (disease, raids, thunderstorms) L5 YES.
- **Attachment claims** (`9226007a-...Nine_Titles.md:294-308,377-378,404,449`; `89a3a060...:199`):
  - Six ages Palaeolithic to Iron: confirmed (era pages Paleolithic, Mesolithic, Neolithic, Copper, Bronze, Iron) [V3 DOMW page list, Research].
  - Morale falls with hunger, injury, hard labour, witnessing deaths; restored by morale structures and beer: hunger, raw meat, tedious tasks (farming, hauling), thunderstorms, deaths confirmed; "injury" not in the page `?`; restoration by spiritual structures, killing raiders, beer, and (1.4) burial mourning confirmed [V3 DOMW Morale; Steam 1.4]. Morale is one of seven welfare stats [V3 DOMW Morale].
  - Knowledge from hunting new species, crafting, building: confirmed with counts 1/5/10/50/100/500 [V3 DOMW Research]; "first deer" example from [V3 PC Gamer].
  - Raiders "arrive in later ages": partly wrong; Stone Age groups of 3-4 already exist, volume rises "from the Copper Age onward", armour from Bronze [V3 DOMW Raiders; Steam 1.2.0, 1.6].
  - Work areas "painted" with worker and resource caps; production as % of population: confirmed, but areas are circles you place and size [V3 PC Gamer via Steam news 2019-03-18].
  - "Hunters freezing on the return journey": not located in a source I read; RPS anecdote of settlers collapsing in snow hauling a megalith [V3 RPS via Steam news] `?` as a rule.

---
### The Guild 2 (Renaissance) - facts line
4HEAD Studios / JoWooD, Windows, 2006; the stand-alone *Renaissance* (Runeforge, 2010) bundles the base game and expansions and is the version to play [V3 theguild2.fandom.com The_Guild_2_Wiki via api.php 2026-10-22; **G2R** = guild2renaissance.fandom.com via api.php]. Rules text below is Renaissance 4.2x as documented by fans and by a Steam script-reading guide (**G2S** = steamcommunity.com/sharedfiles/filedetails/?id=1556565021, read 2026-10-22); no developer manual reached, so every number is community-derived and version-bound. Assumed: single player, map "The Hansa", Dynasty (sandbox) mode, Normal. Clock: real time with pause; a "round" is 24 real minutes at default speed and simulates one in-game day, at the end of which the game jumps year and season by the setting "Years per round" [V3 steamcommunity.com/sharedfiles/filedetails/?id=720569185 (Draco's guide)]. One session ~1-3 h.
#### 1. Setup choices
1. **Map** (e.g. The Hansa: Danzig, Hamburg, London... with bandit camps), **hometown**, **number of AI dynasties** [V3 Draco guide; G2R Game_mode].
2. **Game mode**: Dynasty (no goal), Extinction (eliminate all rivals), Time limit (victory points from possessions, titles, offices, defeated foes), Mission [V3 G2R Game_mode]. Difficulty = starting gold, applied to you not the AI (except Mission).
3. **Years per round** and **Office sessions** (rounds between elections) [V3 Draco guide].
4. **Your founder**: names, gender (a pregnant woman cannot act), religion Catholic/Protestant (matters mostly for scholars/priests), zodiac sign (+1 to one talent), coat of arms (flag colour), **class** Patron / Craftsman / Scholar / Rogue (decides which businesses you may build; Rogues produce nothing), and 500 XP to spend on ten talents (start 1, cap 10) [V3 theguild2 Player_Character; G2R Talents; Draco].
#### 2. The loop
1. You steer up to three dynasty members (a "group") in real time: walk to buildings, talk, work, court, sabotage; each action has cooldowns [V3 Draco guide; theguild2 Courting].
2. Automated: every NPC runs a daily script (wake, work, socialise, sleep) driven by 9 needs; employees work fixed hours; a constant unemployed pool respawns when you hire; sick workers stop a shop; businesses can be set to AI control [V3 G2S; theguild2 starter guide 500138628].
3. Markets reprice from supply and demand; carts follow trade routes you set; seasons change at round end [V3 G2S; Draco].
4. Council meetings (17:00 on set dates) elect office holders; trials start 09:00 the year after a charge; offices act on tax, law severity, guards [V3 G2R Politics, Trial].
5. Interrupts: crimes witnessed, feuds, fires, plague, siege; you must be present for your own trial or you lose by default [V3 theguild2 Trial].
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Buy/build a business (farm, bakery, pub, smithy, church, robber nest...) | gold; limited by title | income, jobs | constant |
| Hire employees, set production and sales stock | wages | output, guards/saboteurs | constant |
| Set up a trade route with carts | cart, goods | automatic sales | mid |
| Buy the next title at the town hall clerk | 500 / 2,000 / 6,000 / 25,000 / 30,000 / 80,000+ gold (Renaissance) | more businesses, better housing, office rights | every few rounds |
| Apply for office (+ bribe/flatter voters) | fee, favour | immunity, tax rate, guards, tithe, law severity | mid and late |
| Court, marry, spend the night | gold for outings, time | heir, free title if marrying up, relations | once per generation |
| School / apprenticeship for a child | 500 / 1,500 / 5,500; 1,000 | guild or imperial fame; class | per child |
| Accuse, gather evidence, slander at the town crier | money to the crier | trial, fines, jail, outlaw | rarely, decisive |
| Sabotage, rob, attack carts (thugs, rogues) | employees, bombs | harm rivals, loot | rogue play |
| Change diplomatic status (non-aggression, mutual aid, feud) | favour, building upgrade | who may attack you | occasionally |
| Take loans / bank | interest | cash now | rarely |
[V3 G2R Titles, Politics, Favour, Trial; theguild2 Education, Title]
#### 4. First hour, step by step
Source: in-game Tutorial (Single Player > Tutorial; on Steam it may need the "Latest Patch" beta) and Draco's guide [V3 G2R Tutorial; Draco guide].
1. Choose the map, mode, difficulty; pick a coat of arms.
2. Spend the 500 XP; pick the class (Patron/Craftsman are safe starts; Scholar churches earn fast per fan guides).
3. Buy or build one business inside the city (guards protect it); do not put a croft inside walls.
4. Hire an employee and set what the building makes and sells.
5. Court a suitable partner, varying interactions (a follower stays ~2 min, the romance cooldown is ~2 min); marry.
6. Take the spouse home, "spend the night"; a baby comes; keep ~1,500 gold for school/apprenticeship.
7. Visit the town hall: look at laws and the meeting schedule; buy Yeoman (500) only when gold clearly exceeds the price.
8. Watch favour with neighbours (compliments, gifts) before you need votes.
9. Save often; fans warn the game can corrupt saves and crash [V3 G2R Tutorial].
#### 5. What changes later
Titles run Serf, Commoner, Yeoman, Citizen without full rights, Citizen, Free Citizen, Patrician, Nobleman, Baron, Allodial Baron, Count, Marquis, Prince; business limits grow to 15 (Patrician) and unlimited; Imperial Fame (war service, hiring troops, noble schooling) gates nobility [V3 G2R Titles; theguild2 Imperial_fame]. Settlements gain City Rights (80 / 140 / 200 / 300 population; 10,000 to 100,000 gold) which add offices; one Imperial Capital per game [V3 G2R Level_of_development]. Office privileges include set sales tax, law severity, immunity, banish, torture, disappropriate [V3 G2R Politics]. Feuds escalate to raids and arson.
#### 6. Failure and ending
A dynasty ends when it has no married partner or child aged 16+ [V3 theguild2 Dynasty]. Also: outlaw (4 years), prison (4 years), disappropriation (property confiscated, demoted) [V3 G2R Trial, Politics]. Win only if the mode says so: Extinction, Time limit points, Mission; Dynasty mode never ends [V3 G2R Game_mode].
#### 7. Consequential vs cosmetic choices
- Consequential: class (gates buildings), marriage (an upward marriage gives the spouse's title free) and favour (shared across the whole dynasty) [V3 theguild2 Courting; G2R Favour]; office holding (immunity, taxes) [V3 G2R Politics]; evidence and Rhetoric vs Empathy at trial [V3 G2S].
- Cosmetic: religion for non-scholars, coat of arms colours; zodiac is one point.
- Dominant claims (community only): Scholar churches and tavern/inn chains on AI control are strong low-attention incomes; Rogue is strongest but everyone hates you [V3 theguild2 starter guide].
#### 8. Open items
- Capability ids [V3 G2R/theguild2/G2S unless noted]: B1 YES (dynasty panel, book of dynasties) B2 YES (hire employees, thugs, mercenaries) B3 PART (assign employees to jobs; offices are elected not appointed) B4 YES (tasks to employees and guards) B5 PART (AI-control a business; trade routes) B6 YES (favour; feud status) B7 PART (child becomes playable at 16; partner survives) | C1 YES (build/buy anywhere allowed) C2 YES C3 YES (dwelling and building upgrades) C4 PART C5 YES (wheat-flour-bread, ore-bar-tool) C6 YES (trade routes) C7 PART (guards, mercenary camps) | D1 PART (office holders set law severity, taxes) D2 YES (sales tax, tithe) D3 YES (council offices with privileges) D4 PART (siege/starvation behaviour) D5 YES (council elections at 17:00) D6 YES (trials, judges, assessors) | F1 PART (hire mercenaries, Imperial fame for war materials) F2 NO F3 NO F4 PART (group fights, duels) F5 PART F6 YES (siege/storm buildings) F7 NO F8 PART | L1 YES (talents, zodiac) L2 YES (aging, lifespan from Constitution) L3 YES (marriage, children, education) L4 PART (feuds, plague, fires) L5 YES (NPC daily scripts, AI dynasties).
- **Attachment claims** (`9226007a-...Nine_Titles.md:164-199`; `89a3a060...:179,235`):
  - Ten talents: confirmed count; names differ: wiki lists Constitution, Dexterity, Charisma, Martial Arts, Handicrafts, Stealth, Rhetoric, Empathy, Bargaining, Arcane Knowledge, not "Fighting, Craftsmanship, Shadow Arts, Secret Knowledge" [CONTESTED names; V3 G2R Talents]. Class-priced XP, cap 10, zodiac +1: confirmed.
  - Title ladder "Serf through Nobleman, Baron and Prince": confirmed for Renaissance; the base-game wiki instead ends at Landgrave/Baronet (100,000) [CONTESTED by version]. Costs differ: Free Citizen 15,000 (theguild2) vs 25,000 (G2R, Draco); Marquis 1,000,000 (G2R) vs 1,200,000 (Draco); Prince 1,500,000 vs 2,000,000.
  - Evidence "decay of roughly six years": G2S says each evidence has a time-to-live of "6 rounds or year" after the crime, unit ambiguous because a round ends with a year jump [V3 G2S]; the Trial wiki confirms expiry exists but gives no figure `?`. Strength x believability weighting, at most 3 evidences checked, Rhetoric vs Empathy shifts [V3 G2S]. Slander: town crier makes one evidence and propagates it to 10 neutral NPCs [V3 G2S] (attachment: "random townsfolk"): confirmed in substance.
  - Judge plus two assessors (assessors are not an office): confirmed [V3 G2S]; "judge ignores diplomatic standing, assessors do": not verified `?`.
  - Dynasty, children: school at 4, apprenticeship at 8, playable at 16 confirmed; "university at twelve" and "up to four children, adoption" not found `?` [V3 theguild2 Education]. Controllable group is 3, removal is permanent [V3 theguild2 starter guide].
  - Needs: 9 confirmed; autumn/winter double sickness confirmed; unemployed pool refills confirmed [V3 G2S].

---
### The Guild 3 - facts line
GolemLabs (Canada, from 2015) then Purple Lamp Studios (Vienna, from 2018) for THQ Nordic; Early Access 2017-09-26, 1.0 on 2022-06-14; last patch notes 1.0.7 "Editor and Modding" 2023-06-30 [V3 theguild3.fandom.com The_Guild_3 via api.php; Steam news app 311260, fetched 2026-10-22]. Rules below are from the fan wiki (**G3W** = theguild3.fandom.com, pages stamped v1.0.4) plus patch notes, so later balance changes are possible. Assumed: single player, Normal, default 2 years per round, Poor-fellow start. Clock: real time with pause; a "round" is one season and 24 in-game hours (30 real minutes at speed 1, 7.5 at max), after which N years pass, children are born and named, and the game autosaves [V3 G3W Time; Game_option]. One session ~1-2 h = 2-4 rounds.
#### 1. Setup choices
1. **Map**: 14 maps from the tutorial Wenighusen (4 dynasties) to the Hanseatic League (18) [V3 G3W Game_option].
2. **Opponents** (default max for the map) and **difficulty** Easy/Normal/Hard/Impossible (starting gold, influence 200/100/50/0, raw materials, family size cap, XP to Citizen; AI pace; the AI plays the opposite of your setting in 0.9.14 notes) [V3 G3W Influence, Game_option; Steam 0.9.14 notes].
3. **Years per round** 1-4 (default 2): faster aging and heirs.
4. **Game mode**: Poor fellow (Serf in a village, few coins) or Career mode (Citizen, city house, profession, funds) [V3 G3W Game_option].
5. **Family campaign** (win condition): Become Sovereign (hold the sovereignty one full round), Free game, Found a powerful dynasty (Lord, Mayor/legate/treasurer, 20,000 gold, an heir), The city smells of freedom (10 workshops, 18,000 gold, a manor), Become ruler of the city (Squire; hold the three top offices two rounds each), Long-distance trader, Warmonger [V3 G3W Game_option].
6. **Avatar**: names, one of 32 coats of arms, religion (Catholic/Secular/Protestant), startup profession (four branches), 15 points on primary attributes [V3 G3W Character_creation, Skills_and_Abilities].
#### 2. The loop
1. You steer a party (leader plus two "hands") around district maps; characters travel, work, talk, sabotage; employees run buildings from order lists [V3 G3W Party_member, Character].
2. Automated: workshops produce and sell; citizens roam; dynasty AIs build, trade, feud; seasons and weather advance at round end [V3 G3W Time; Steam 0.9.14].
3. City hall runs meetings, elections (12 h after applications close) and trials; you vote in advance by calendar when you hold seats [V3 G3W Office].
4. Round end: season change, aging, births, autosave, then a new 24-hour day [V3 G3W Time].
5. Interrupts: feuds, crimes, random events (famine, plague, war), call-to-arms and guild trips at the arsenal [V3 G3W The_Guild_3, Arsenal page].
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Erect a building (B) / lease resource spot | gold; limited by title (1-18 buildings) | production | constant |
| Assign workers and order lists | wages | goods, trade | constant |
| Claim next title (skill-tree menu F2) | I Serf..XV Archduke: e.g. Citizen 4,000 gold + 250 influence; titles are strictly sequential; 20% discount if done at the clerk | more businesses, henchmen, actions | each stage |
| Unlock a dynasty skill (shared by all members) | gold; 500 influence per business branch, 50 for social | new workshops, actions | steady |
| Apply for office / vote | influence fee; Citizen+ (Level 4), Patrician (3), Squire (2), Baron (sovereign) | salary, influence, votes on laws and verdicts | mid and late |
| Perform an action (praise, denounce, church donation, bribe, find or falsify evidence, spy, burgle, intrigue) | gold/influence, risk | reputation, evidence, crime | constant |
| Romance, marry, have children, send to school | gold, 250 influence for school | heir and new party members | once per generation |
| Hire henchmen | wages; limit by title | guards, thugs, escorts | mid |
| Join a guild | attitudes (honesty, generosity, diplomacy) within tolerance | access, expulsion if out of range | mid |
| Long-distance trade journey | goods, time | far-market profits | late |
| Declare/accept feud, war events | risk | raids, sabotage, kills | late (Warmonger) |
[V3 G3W Title, Influence, Office, Skills_and_Abilities, Game_option]
#### 4. First hour, step by step
Source: the in-game tutorial map "Humble beginnings" at Wenighusen [V3 G3W Humble_beginnings]; later steps are NOT documented in the pages I read `?`.
1. Start new game > Humble beginnings (fixed: 4 opponents, Tutorial difficulty, Poor fellow, crude craftsman, 2 years/round, Become Sovereign).
2. The tutorial page pops up on every first use of a function (F1 reopens it); open the Quest book (F7).
3. First quest: press B and erect a crude craftsman's hut; the tutorial only advances when you do the assigned task.
4. Continue by quest book: produce first item, sell at the market, hire first worker `?`.
5. Aim for the Resident/Citizen titles (Citizen unlocks city offices, Find evidence, Hire henchman, Run for office).
#### 5. What changes later
Titles unlock: Citizen (offices, henchmen, evidence), Free Citizen (trade missions, far markets), Patrician (insult, spy, mid-level offices), Nobleman (nepotism), Squire (highest offices, guilds), Lord (eligible to be Sovereign, war officer; the Office page instead says the sovereign level opens at Baron [CONTESTED within G3W]), up to Archduke (1.28M gold, 16,000 influence, 18 businesses, 8 henchmen) [V3 G3W Title]. Offices: four tiers (sovereign; council of 3; judges and constables; assistants, informers, town henchmen); you must hold an office one level below to apply for the next; the sovereign contest lets you pledge more influence than rivals [V3 G3W Office]. Verdicts: not guilty, low fine, public shame, high fine, prison, death [V3 G3W Office].
#### 6. Failure and ending
Win = the family campaign target you picked (e.g. hold the sovereignty one full round); a score exists (achievements at 1,600 Normal, 1,900 Hard, 2,200 Impossible) [V3 G3W The_Guild_3, Game_option]. Setbacks: a jailed family member can be bribed out via the arsenal master; execution is final (an "Executed" achievement exists) [V3 G3W Arsenal page, The_Guild_3]. The explicit loss rule (no heir / dynasty wiped out) is not stated in the pages I read `?`.
#### 7. Consequential vs cosmetic choices
- Consequential: title timing (gold plus influence, sequential), office path (informer to constable to council), reputation (elections depend on dynasty reputation) [V3 G3W Office]; family campaign target; guild attitudes tolerance.
- Cosmetic: coat of arms colour, religion mostly (detection alertness and success chance by denomination) [V3 G3W Character_creation].
- Dominant answer: none established.
#### 8. Open items
- Capability ids [V3 G3W unless noted]: B1 YES (book of dynasties, city records) B2 YES (workers, henchmen, lansquenets) B3 PART (assign workers; offices elected) B4 YES (order lists, party commands) B5 PART (leased businesses, auto level-up option) B6 YES (reputation; attitudes; relation bar) B7 YES (heir takes over) | C1 YES (build in any district you may) C2 YES C3 YES (tiers) C4 PART C5 YES (production chains) C6 YES (long-distance routes, transporters) C7 PART (guards, arsenal) | D1 PART (office holders vote on city laws) D2 PART D3 YES (four-tier office tree) D4 PART D5 YES (elections) D6 YES (trials, verdict scale) | F1 PART (call-to-arms) F2 NO F3 NO F4 PART (melee skirmishes) F5 PART F6 PART (conquer building) F7 NO F8 PART | L1 YES (attributes, skills, attitudes) L2 YES L3 YES (marriage, children) L4 PART (random events) L5 PART (AI characters).
- **Attachment claim, EHE disabled by publisher** (`9226007a-...Nine_Titles.md:193-197`; `89a3a060...:241-245`): NOT FOUND. Searched all 193 Steam news posts (2017-2026) for EHE/Evolutive/emulator/deactivated: no hit; the only primary mention is 2018 marketing that the AI "EHE" rests on "six character attributes" [V3 worthplaying.com/article/2018/6/25/news/109550]; neither Blue's News nor the GolemLabs-quitting Steam thread mention disabling it; two web searches found nothing on house-burning citizens [S3]. Patch 0.9.14 describes reworked AI archetypes and dynasty "moral attitudes" [V3 Steam 2021-06-09] but never names EHE. Verdict `?` (unverified, not refuted).
  - GolemLabs to Purple Lamp in 2018, EA 2017, 1.0 June 2022: confirmed [V3 G3W The_Guild_3; Steam 2022-06-14]. "Roughly five years": from 2015 start to 2022 is about seven, from EA about five.
  - Remake *The Guild - Europa 1410* (Ashborne/THQ Nordic) entered Early Access 2026-09-17: confirmed ("mid-2026" is close) [V3 Steam news 2026-09-17].
