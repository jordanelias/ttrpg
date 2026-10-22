# T04 - Colony sims B: Manor Lords, Frostpunk, Frostpunk 2, Banished (v3 tutorial pass)
Tags: [V3 url date] read in a fetched page/API body this session; [S3 url] search snippet only; [M] memory; `?` not established; [CONTESTED]. Steam news = `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1363080` (full patch-note bodies; item date given). The Hooded Horse wiki (incl. its Beginner's Guide), Gamespot and Sportskeeda returned 403 (Cloudflare) and were not bypassed; the PC Gamer tips page returned no body. "v2 table" = `../tables/R3b_colony_sims_2.md`.

### Manor Lords - facts line
Slavic Magic / Hooded Horse; medieval city builder with real-time battles on the same map; Early Access since 26 Apr 2024 ("a year since launch" post dated 26 Apr 2025 [V3 steam news]). Version relied on: **Major Update #8 exists: "Wide Valley, Cows, Cider, Advanced Construction & More", patch 0.8.090-0.8.104 on the main branch, Steam news 27 Aug 2026** [V3 steam news item 1842212951300554, 27 Aug 2026]; newest beta 0.8.110 (27 Sep 2026) and hotfix 0.8.111 (29 Sep 2026) [V3 steam news]; Steam posts after that (2 and 10 Oct 2026) are only sale notices; no 1.0 date seen. Tutorial assumes the Default template, peaceful Growth goal, main-branch Update 8, one settlement. A session has no fixed length; the first hour reaches roughly the first winter; Large Town takes many hours `?` (not found in any source read).
#### 1. Setup choices
Game Setup screen (restyled in Update 7 [V3 steam 10 Jul 2026]). Option names below are from search summaries of the wiki/Gamespot unless marked [V3]:
- **Map** (+ **starting location** on it, for you and the adversaries [V3 steam Update 5, 19 Dec 2025]): Germanic Valley, High Peaks, Devil's Hill, Jagged Cliffs, Divided, Lake Lemm, Twin Lakes (Update 6), Wide Valley (Update 8) [V3 steam notes]. Changes terrain, resource nodes, region count. Resource richness: every start gets Fish OR Small Game, Berries OR Mushrooms, Iron OR Salt, plus Clay, Stone, Fertility; two of them are boosted to "Rich" [V3 steam Update 5].
- **Mode**: normal single-lord game, **Duel** (1 vs 1 with an AI lord) or **Fractured Realm** (4-lord free-for-all) [V3 steam Update 5].
- **Template**: Relaxing / Default / Challenging [S3 search 22 Oct 2026]; **scenarios** Rise to Prosperity (peaceful, reach Large Town), On the Edge (same goal plus raiders and bandit camps), Restoring the Peace (claim every enemy region; hardest) [V3 gamerant.com/manor-lords-how-to-win-game-victory-conditions-restoring-peace/, 0.7 build].
- **End goal**: Growth (reach Large Town), Conquest (claim all regions), Domination (defeat all other lords; needs the off-map adversary), or None/endless [S3 search].
- **Off-map adversary** Present/absent and **AI aggressiveness** (players name "Reactionary" - never presses claims - and "balanced") [V3 steam forum thread 4355619963546558875]. Changes whether a rival lord challenges your regions.
- **Raids**: frequency, years with no raids, number of bandit camps [S3]; **Weather Events: None** exists (lightning fires switch off) [V3 steam Update 5]; **starting season** incl. a random option [V3 steam Update 7 bugfix list]. Winter start is "asking for trouble" [S3].
- **Origin Perk**: the first Development Perk batch (named e.g. "Of the Vogtland", "Regensburg Guildmen" [V3 steam Update 6 fix list]); the exact moment of choice `?`. Lord name/heraldry are cosmetic [M].
#### 2. The loop
Clock: real time with pause (Space) and speed multipliers, max 8x since Update 7 [V3 steam 10 Jul 2026]; days -> months -> four seasons. Villagers (families) act on their own; you queue plans while paused.
1. Plan (usually paused): draw roads, drop burgage plots, place production buildings, mark fields/pastures, set work areas.
2. Staff: click a building and assign family slots (one family = one job); unassigned families are the builders/haulers. Oxen with guides carry timber to sites; Update 8 adds a Construction Yard (handcart distribution, +50% build speed when maintained) and "Advanced Structures" needing builders assigned there [V3 steam Update 8].
3. The game runs: families fetch fuel and water, eat from market stalls, haul goods between granary/storehouse/stalls, craft, farm by season; buildings need maintenance deliveries or can collapse/injure [V3 steam Update 5]. All of that is automated.
4. Approval is a live score built from needs: food variety by category, clothing, church, tavern drink, housing [V3 steam Update 5 ; pcgamesn.com/manor-lords/approval-rating, 26 Apr 2024]; once a month families arrive or leave according to the Approval tier, and only if living space exists [S3 search of the wiki Family page; size of the effect is S3]. Tithe turns donated food into Influence; the Land Tax and Tithe settings exist [V3 steam Updates 5, 8]; what the Land Tax pays into [M].
5. Milestones: settlement level rises when enough Families reach the right plot level (since Update 6) -> pick a Development Perk (+100 Influence per level milestone in Update 8) [V3 steam Updates 5, 6, 8].
6. Interrupts: bandit camps/raiders (looting and torching until 50% loot taken or 40% burnt [V3 steam Update 7]), disease (whole family falls ill together), fire, winter shortage; rival lord claims or Challenges. A battle is on the same map: you command squads (militia from households, retinue at the Manor, mercenaries) in real time, then control returns to the settlement view.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Place/shape roads and burgage plots (constant) | timber, builder labour | living space -> migration; plots upgrade L1-L4 by meeting needs | every few minutes, all game |
| Assign families to jobs (constant) | 0 gold; labour trade-off | every building yields only with a staffed slot | after each build; at season changes |
| Gatherer/production buildings (constant) | timber/stone; worker slots | food, fuel, hides, iron, planks | opening and expansion |
| Logistics layer: hitching post/ox, granary, storehouse, market stalls, Construction Yard (frequent) | timber, oxen, workers | shortens haul distance; jams are the commonest failure (top Steam complaint [V3 steam 0.8.110]) | from minute 1 and whenever traffic stalls |
| Fields, crop and rotation, pastures (seasonal) | land, ox, labour | grain, flax, oats; animals with winter feed in Update 8; rotation mandatory in beta 0.8.110 [V3] | by February for spring sowing |
| Plot extensions (garden, orchard, coop, goat, smithy, tailor, bakery, cobbler...) (frequent) | Regional Wealth / materials | household becomes a workshop or adds food categories | after plots reach upgrade levels |
| Marketplace distribution + Active Recipes / Production Focus (moderate) | none | what stalls stock; what artisans make first | when approval needs a category |
| Trading Post: import/export, trade routes (moderate) | Regional Wealth, horse, family | sells surplus, buys iron/salt/dyes | once surplus exists |
| Tax and Tithe settings (rare) | approval vs Treasury/Influence | Tithe gives 2 Influence per 1 food donated [V3 steam Update 5] | when Influence or Treasury is short |
| Development Perk pick (rare, per level) | the level-up | specialisation; Rural Foundations: six perks at level 3 in beta [V3 steam 0.8.110] | on each settlement level |
| Build church / tavern (rare) | timber, stone, workers | approval and plot requirements; wooden church +100 Influence [V3 steam Update 8] | year 1-2 |
| Claim a region (rare) | 1,000 Influence, 2,000 if rival-held (2024 figure; v2 table, not re-opened this session) | new land; may trigger battle | after Influence builds |
| Raise militia / retinue / mercenaries; fight (rare unless raided) | weapons from stock, jobs left empty, 50 Treasury per retinue man (v2 table, not re-opened) | defends or conquers | when bandits or a Challenge appear |
| Castle planner: manor, walls, gates (rare) | stone, mortar, builders | sieges and a defensible core [V3 steam Update 5] | mid game |
#### 4. First hour, step by step
Source: Gamer Guides survival and build-order pages [V3 gamerguides.com/manor-lords/guide/basics/overview/survival-guide-for-your-first-few-years ; .../starting-strategies-and-build-orders; 2024 era, undated] checked against Update 8 notes; in-game tutorial popups cover the same ground (all tutorials rewritten in Update 5; a logistics tutorial added in Update 7) [V3 steam].
1. Pick a map and the Relaxing/Default template; leave None or Growth as the goal; spring start.
2. Pause. Look at the starting families (five, per the v2 table [S2]), the supplies and the resource overlay; most guides warn the default template is hard for newcomers [V3 steam forum].
3. Place a Logging Camp near trees; timber gates everything. Staff it.
4. Place a Hunter's Camp (no build cost [S3 primagames snippet]) and Forager's Hut near berries; limit hunting so the herd recovers (guide: stop at about eight animals).
5. Place a Woodcutter's Lodge; winter roughly doubles fuel use.
6. Add storage and haulage: granary, storehouse, hitching post with an ox; put the fifth family on the ox post.
7. Draw a road and place the first burgage plots; the guides say wait until Approval is over 50%, but homelessness only costs Approval after a 30-day grace period [V3 steam Update 5].
8. Hover Approval: the overlay lists missing requirements for every plot [V3 steam Update 5]. Mixing three food sources lifts Approval.
9. Add a Forester's Hut when a spare family arrives, so trees regrow.
10. Put surplus families on storehouse/granary and extra firewood before winter.
11. Build a small marketplace beside homes and storage so stalls carry food and fuel.
12. Year 2: Farmhouse by February, two fields (emmer, flax), a church, then windmill and communal oven before September.
13. Keep adding plots only while food and fuel exceed consumption.
14. Prepare for bandits in year 2: a Bowyer extension on one plot to field archers.
15. Reach the first level-up: spend the Development Perk; this is when the game starts asking trade-offs rather than survival.
#### 5. What changes later
- Levels: advancement checks families by plot level (Update 6), so plots must be lived in, not just built [V3 steam]. L3 adds cobbler/baker extensions; L4 is the old L3 look [V3 steam Update 6].
- New layers: artisans and Trading Post (Regional Wealth), maintenance, affinities (Meadow, Woodland, Farmland, Rural, Urban), cattle, cheese (needs L3) and cider/mead in Update 8 [V3 steam].
- Politics arrives by Influence: claim regions, face a rival lord's Challenges, build a castle. Approval tiers pay Influence (Revered +20, Admired +10 as of beta 0.8.046 [V3 steam 1 Dec 2025]; "per month" is [S3]).
- Pressure ramps: more raiders, larger populations, long haul distances, farming seasons.
#### 6. Failure and ending
Starvation, cold or homelessness drop Approval, families leave, production collapses: depopulation, recoverable if you rebuild. Raids burn or loot a settlement. Winning is by the end goal: Large Town (Growth), all regions (Conquest), all lords (Domination), or nothing (None). Whether losing the Manor ends a campaign `?`; the AI "rebuild a Settlement" logic exists [V3 steam Update 5].
#### 7. Consequential vs cosmetic choices
- Consequential: logistics layout, food-category variety and fuel stock (Approval drives migration, Influence, income); source: patch notes tie tiers to growth/influence/income [V3 steam Update 5].
- Consequential: opening staffing before the first winter (community consensus, Gamer Guides).
- Probably dominant: Reactionary AI or Relaxing template removes the threat (forum consensus, [V3 steam forum]).
- Perk picks are intended to be "less immediately obvious" [V3 steam Update 5]; no balance study found `?`.
- Cosmetic: heraldry, names, plot looks, Update 8 "randomized distribution preferences" [V3].
#### 8. Open items
Capability table (v2 R3b section 1) fixes:
- A3 old "PART: 4 trees Farming/Trade/Industry/Gathering, 1 point per level" -> new: tree replaced by Development Perks in Update 5; Origins first; "Policies are temporarily removed"; Rural Foundations (6 perks, level 3) in beta [V3 steam Update 5, 19 Dec 2025 ; 0.8.110, 27 Sep 2026].
- A1 old "lord/lady rank limiting the bailey NOT found, dropped" -> new: Update 5 notes say "Bailey area ... limited by your lord's or lady's Rank (still WIP)" [V3 steam Update 5]; still NO avatar.
- D1/D2 "tax/tithe, policies" -> policies removed; Land Tax and Tithe still set by AI/player [V3 steam Update 8].
- Latest version: Update 8 (27 Aug 2026) and beta 0.8.110/.111, newer than the v2 table (Update 7). Max speed 8x confirmed [V3 steam Update 7].
- F5 auto-resolve: no mention in the Steam notes read (Updates 5-8, betas to 0.8.111); leaning NO, absence `?` still.
- F6 sieges: "the Siege Camp building option was hidden" because it is WIP [V3 steam Update 6, 18 Mar 2026]; no later note read re-enables it.
- B1/L2: consumption, approval and disease data now sit on the Family; "whole families will now get sick together" [V3 steam Update 5]; births/ageing of family members still not established `?`.
- E2 trade: the dev put the trade rework (monopolies etc.) on hold in May 2026 [V3 steam 9 May 2026]; Update 8 added per-Trading-Post storage filters [V3 steam Update 8].
- Approval: Admired +10, Revered +20 Influence [V3 steam 0.8.046]; per-tier migration -3..+3 stays [S3 search of wiki Family page]; wiki Beginner's Guide still shows the old 50/75/25 table [S3].
Attachment claims (/root/.claude/uploads/924794e6-79aa-4348-9d83-3f218997fade/9226007a-Citizens_Settlements_and_Factions_-_Nine_Titles.md; line numbers are that file's):
- L138 "Major Update #8, 27 August 2026": CONFIRMED [V3 steam news 27 Aug 2026]; Update 8 also confirmed to add Construction Yard, ox carts, Advanced Structures, cows, cheese, oats, cider, mead, seasonal breeding and winter feed (L154); handcarts predate it (Update 7 notes mention returning handcarts) so "adding handcarts" is half-right.
- L148 (and L370) immigration "above a floor... below a lower floor leave": TRUE of 2024 (50% = 1 family/month, 75% = 2, under 25% leave [V3 destructoid.com/?p=502092 28 Apr 2024]); since Update 5 it is 7 tiers with migration -3..+3 and only if living space exists [S3 wiki Family]. The doc's "breakpoints moved" caveat is right.
- L148 approval inputs list: food variety, church, tavern drink, clothing agree with [V3 pcgamesn approval-rating 26 Apr 2024 + steam Update 5]; fuel, public order, unburied dead, tax: [S3 only].
- L150 "since March 2026 progression counts families by tier": CONFIRMED (Update 6, 18 Mar 2026). "single unmet need locks the upgrade chain": NOT FOUND in any note read `?`. "same period removed the tier-1 ale requirement": the change is Update 7 (10 Jul 2026): "Ale is no longer consumed by Lv1 Families" [V3 steam]; not March.
- L158 (and L543) "AI settlements added during 2026 ... community says cheat": WRONG on date - AI lords/towns and Duel/Fractured Realm shipped in Update 5, 19 Dec 2025, after being previewed Mar-Oct 2025 ("AI-controlled towns" Mar 2025; "AI can't challenge the player yet" Oct 2025) [V3 steam 2025 posts]; an off-map AI adversary (Baron Hildebolt) already existed in the 0.7 build [V3 gamerant, 2024]. "Cheat": no evidence; the only "cheating" is a dev aside on collision [V3 steam 0.8.078]; Update 6 notes show AI capped ("temporary max cap to the number of families in AI regions", no extra settling) [V3]. VERDICT: unsupported.
- L162 "2.5 million copies": stale; Steam news 27 Aug 2026 says over 4 million [V3 steam, PC Gamer item]. Peak 173,000 and team size not checked.

### Frostpunk (base game, scenario "A New Home") - facts line
11 bit studios; city-survival / society builder; released 24 Apr 2018 on Windows [V3 en.wikipedia.org/wiki/Frostpunk]. Version relied on: base-game patch **1.6.2, Steam news 11 Oct 2022**, the newest patch note in the feed (it also added the Builders' Monument for Endless Mode) [V3 steam news appid 323190]; Switch port scheduled 19 Oct 2026 [V3 Wikipedia]; a rebuilt "Frostpunk 1886" is announced for 2027, a different product [V3 Wikipedia ; steam news 9 Apr 2026]. Tutorial assumes A New Home, default difficulty, the Adaptation law book. Session: one attempt is several hours, exact length `?` ([M] roughly 5-10 h); the first hour is Days 1-4.
#### 1. Setup choices
- **Scenario**: A New Home (3-act main campaign), The Arks, The Refugees, The Fall of Winterhome (free prequel), The Last Autumn, On the Edge; plus **Endless Mode** with **Serenity** (milder weather) or **Endurance** (harder; random parts of the city shut down) [V3 Wikipedia].
- **Difficulty**: forum posts list Easy / Medium / Hard / Extreme, A New Home "medium" first [S3 search 22 Oct 2026]; **Extreme** was added in Update 1.1.1 as Survivor Mode difficulty "with the option to pause and save" [S3 search], so Survivor Mode itself has no pause/manual save (inferred). The Economy difficulty sliders exist [V3 steam patch 1.6.2]. Changes weather harshness, research time and supplies; per-slider values `?`.
- No faction, ruler or map choice: the map, the starting crew and the generator are fixed per scenario. All real choices are in-game (laws, Purpose).
#### 2. The loop
Clock: real time with pause; a day-night cycle; citizens work only in the warm daylight hours, so night is for planning [V3 Wikipedia ; gameskinny via search S3]. Shifts: Extended 14 h, Emergency 24 h [V3 gamepressure.com/frostpunk/adaptation/zdad7a]; the normal 8 h comes from the v2 table (citing gamingbolt), not re-opened.
1. Pause, read the stockpile, assign workers/engineers to buildings; Workers and Engineers are not interchangeable (Workshop and Medical Post need Engineers) [V3 thegamer.com/frostpunk-essential-beginners-tips/].
2. Place buildings on the circular grid around the generator; everything must sit in heat range; Steam Hubs extend heat [V3 Wikipedia ; thegamer].
3. Queue research in the Workshop (Sawmill, Steam Hub, Beacon...).
4. Sign a law when the Book of Laws is off cooldown (see open items for the length).
5. Let time run: the game feeds the generator, drops temperature on a script, spends food, makes people sick or injured, drains the finite surface deposits; Hope and Discontent move [V3 Wikipedia].
6. Interrupts: scripted events with a choice (e.g. Day 3 "Lost Expedition": save survivors at the cost of 2 workers [V3 ludo.guide/guide/frostpunk/side-quests-activities/special-events-dilemmas]); scouts return; storms; control returns to you after the choice.
Automated: heat radius effects, hauling, eating, healing, Automatons (work 24 h at 60% efficiency [V3 thegamer]).
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Assign workers (constant) | labour, night is free | each building yields only if staffed | every day |
| Gathering Posts on deposits (constant early) | wood/steel, workers | one post gathers ANY deposit in its radius, so fewer workers needed [V3 thegamer] | Days 1-10 |
| Houses/tents, medical (constant) | wood, steel | shelter, warmth, healing; Medical Post has five beds [V3 thegamer] | before each cold drop |
| Research (constant) | Engineer time | unlocks Sawmill, Beacon, Steam Hub, heaters... | all game |
| Steam Hubs, heaters, generator upgrade/overdrive (frequent) | coal, steel | more heated area; overdrive burns more coal | at each temperature drop |
| Scout via Beacon (frequent) | expedition time, risk | the only way to grow the workforce; finds survivors, steam cores, resources [V3 Wikipedia] | from Day 2, before the storm |
| Food chain: hunter's hut, cookhouse, Soup/Additives (frequent) | workers, laws | raw food becomes 2 rations (v2 table citing gamingbolt; not re-opened) | continuous |
| Emergency/Extended Shift (frequent) | Discontent | 24 h workplace opening | when a resource gap bites |
| Sign a Law (rare, a few dozen over a run) | Hope and/or Discontent | opens buildings; exclusion pairs | each time the book is free |
| Faith or Order Purpose (once) | rest of the run | turns the Hope bar into Devotion (Faith) or Obedience (Order); Discontent stays, and Order laws lower it [V3 Frostpunk Fandom Hope page; thegamer laws guide says only "your Hope bar will turn into Obedience"] | near the end, before the storm |
| Answer event dilemmas (rare) | people, hope | one-off | when they pop up |
| Medical policy (rare) | Hope, lives | Triage heals 60% but 25% of those die [V3 gamepressure] | when illness spikes |
| Child labour, funerals, Cemetery/Corpse Disposal (rare) | Hope | labour vs hope trade | early mid game |
#### 4. First hour, step by step
Sources: GOG forum build-order post [V3 gog.com/forum/frostpunk/new_home_build_orders, May 2018]; KeenGamer 5 tips [V3 keengamer.com/articles/guides/5-basic-tips-for-frostpunk-players/]; ludo.guide day list [V3]. In-game pop-ups teach Act 1 [V3 Wikipedia].
1. Pause on Day 1; do not run the generator yet - "not until the first night" [V3 keengamer].
2. Day 1 law: choose Emergency Shift (the forum author thinks the early boost is too good to skip) or Child Labour Safe Jobs [V3 gog ; ludo.guide].
3. Build a Gathering Post on the wood/steel scrap; when done move workers to a second post and a hunter's post.
4. Build a Workshop immediately; hold up to 5 Engineers [V3 keengamer].
5. Overnight, use the wood income for a cookhouse, a Medical Post and two more Workshops [V3 gog].
6. Day 2: research the Beacon first (forum), build it before the tents, then four tents [V3 gog].
7. Sign Soup before Day 2 ends so food lasts and hunters can wait [V3 gog]; Day 3 law choice is Soup or Radical Treatment [V3 ludo.guide].
8. Send scouts as soon as the Beacon stands; handle the Day 3 and Day 4 dilemmas.
9. Put a Gathering Post on a coal pile; research a way to get coal before the piles run out [S3 search of steam threads].
10. Research Sawmill, Hunter's Gear, then second-tier unlocks, Steelworks, Infirmary [V3 gog].
11. From Day 4 the first cold drop arrives: every decision must survive 20 degrees colder [V3 keengamer].
12. Watch for scouts bringing more refugees: build tents and an extra hunter's hut first [V3 thegamer].
#### 5. What changes later
Temperature keeps falling in steps, so heat range, insulation and housing upgrades dominate; the second act is internal conflict, the third the Great Storm with Winterhome falling [V3 Wikipedia]. More laws unlock down each tree (e.g. Public House after Fighting Arena) [V3 gamepressure]. Manpower and food grow only by scouting, so housing and rations scale together. Purpose arrives late.
#### 6. Failure and ending
Loss: Hope too low or Discontent too high for too long ends the game in revolt/exile; the generator can explode if overloaded [V3 Wikipedia ; thegamer]. People also die of cold, hunger, illness. You can reload a save outside Survivor Mode. Win: survive the Great Storm; the campaign then ends "like a novel" [V3 Wikipedia]. A totalitarian Faith/Order ending is possible. Storm day: one site says Day 44 [S3], unconfirmed.
#### 7. Consequential vs cosmetic choices
- Consequential: the opening order (gathering posts, workshop, Beacon) and the first laws; "many valid builds" exist on normal difficulty [S3 steam thread summary].
- Consequential: exclusion pairs (Soup/Food Additives, Child Shelters/Child Labour, Cemetery/Corpse Disposal, Radical Treatment/Sustain Life) [V3 gamepressure]; one forum author treats Emergency Shift on Day 1 as a must-take (one voice, not a consensus) [V3 gog].
- Consequential: Faith vs Order near the end.
- Mostly cosmetic (my judgement, no source): citizen names and the exact spot of a tent inside the heat circle.
#### 8. Open items
- v2 D1/D2 "Book of Laws: Adaptation open from start": CONFIRMED - the Day 1 law choice exists [V3 ludo.guide].
- v2 law cooldown [CONTESTED] stays: thegamer says one global wait, heading "24 hours" [V3 thegamer.com/frostpunk-book-of-laws-guide/], fandom per-law values (v2 table, S2).
- v2 K2 heat "-1 per 10 C" and Hope/Discontent deltas per law: not found in any page read `?`.
- v2 B2/K4: scouting is "the only way to grow the workforce" [V3 Wikipedia] (was PART/M).
- Version: 1.6.2 (11 Oct 2022) is the base game's latest note [V3 steam]; v2 gave none.
- Starting population and storm day not established `?`; "80 survivors" is an S3 snippet only.

### Frostpunk 2 (main campaign) - facts line
11 bit studios; political city-builder / survival sequel set 30 years after the first game; PC 20 Sep 2024, PS5/Xbox 18 Sep 2025 [V3 en.wikipedia.org/wiki/Frostpunk_2 ; store.steampowered.com/api/appdetails 1601580: "Sep 20, 2024"]. Version relied on: **hotfix 1.6.1, Steam news 2 Jul 2026**, after DLC Breach of Trust (23 Jun 2026) [V3 steam news appid 1601580]. Earlier steps: 1.1.0 QoL 21 Oct 2024; 1.2.0 27 Nov 2024; 1.3 free Major Content Update 8 May 2025; 1.4 controller support 18 Sep 2025; 1.5.0 Fractured Utopias 8-11 Dec 2025; 1.5.4 Feb 2026 [V3 steam news]. Tutorial assumes the base campaign (Prologue, Chapters 1-5, epilogue), no DLC. Session: a chapter is several hours `?`; the first hour is the Prologue plus the start of Chapter 1.
#### 1. Setup choices
- **Mode**: Campaign (multi-chapter, "spanning the life of the Steward") or **Utopia Builder** (sandbox, infinite play time) [V3 Steam store text]. This tutorial is the campaign.
- **Difficulty**: patch 1.6.1 speaks of "citizen and officer" and "steward and officer difficulty levels" [V3 steam 2 Jul 2026]; the 1.3 post says Serenity mode works with "Survivor, Extreme" presets [V3 steam 8 May 2025] [CONTESTED: name sets differ; Serenity is announced as a Utopia Builder setting]. Serenity = gentler weather, abundant resources, shorter whiteouts, no Fervour (minimal protests, no faction conflict) [V3 steam 8 May 2025]. A "midpoint start option" for the campaign was added in 1.3 [V3].
- **Start faction** exists only in the sandbox: the Fractured Utopias DLC lets you "force your starting faction" among 8 [V3 steam 8 Dec 2025]. In the campaign the faction commitments come in play (Chapter 1+).
- **In-campaign branch points**: Chapter 2 route "Defeat the Frost" vs "Embrace the Frost"; Chapter 3 salvage vs settle Winterhome; Chapter 5 banish / reconcile / enforce order [S3 search of selphie1999gaming.com and gamerguides chapter guides, 2024].
#### 2. The loop
Clock: real time with pause, counted in **weeks** (not hours/days as in the first game) [V3 Wikipedia]. Each chapter has a pacing timer or event trigger you can delay by finishing objectives late [V3 outsidergaming.com, 25 Mar 2025].
1. Pause, read the chapter objective and the timer (Chapter 1 is a coal timer).
2. **Frostbreak** snow to open land and deposits, then place **districts** (housing, extraction, food, logistics, research...) rather than single buildings; districts cost resources and upkeep [V3 Wikipedia ; upcomer.com/how-to-beat-chapter-1-of-frostpunk-2/ 19 Sep 2024].
3. Set heat: since 1.3 each district has its own level (Freezing, Very Cold, Cold, Chilly, Livable, Warm) filled by Heat Allocation from the Generator [V3 steam 8 May 2025].
4. Research ideas in the Idea Tree; collect **heatstamps** by keeping factions content [V3 selphie1999gaming.com, 21 Sep 2024].
5. Council: propose a law, buy votes with promises or favours, vote (51 of 100; two-thirds for laws giving the Steward more power) [V3 Wikipedia]; 10-week cooldown after a law passes or fails [V3 gamerguides.com/frostpunk-2/guide/communities-and-factions/laws, 2024].
6. Send Frostland teams, build outposts and colonies, and transfer resources between them [V3 upcomer].
7. The simulation runs: districts consume food/heat/materials; communities (and radicals inside factions) gain or lose Trust and Tension; protests, disease, whiteouts follow the timeline [V3 Wikipedia ; outsidergaming].
8. Interrupts: story events with choices, faction demands, chapter finales, murders, civil war. Citizens as individuals are mostly gone ("embrace macro") [V3 outsidergaming].
Automated: construction crews, hauling, per-district heating once allocated, faction behaviour.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Frostbreak (constant early) | time, workforce | opens land/deposits | first hour and every expansion |
| Place/expand a district (constant) | resources, upkeep | housing, extraction, food, research, logistics | all game |
| Allocate heat per district (frequent) | coal/oil | sickness, injuries, deaths if left cold [V3 steam 1.3] | each cold spell |
| Research an idea (frequent) | heatstamps, research time | new districts, laws, community actions | continuous |
| Propose a law (frequent, ~every 10 weeks per law) | promises, Trust | permanent rule changes; 4 categories Survival/City/Society/Rule [V3 gamerguides] | when a faction asks or a need appears |
| Negotiate: make a promise to a faction (frequent) | a kept promise | buys votes; broken promises harm the relationship (v2 table citing keengamer; not re-opened) | before votes |
| Guided Voting (Rule law) (rare) | faction relations | forces laws through; the guide's first Rule pick, another warns of "prolonged chaos" [V3 gamerguides ; outsidergaming] | when a vote fails |
| Community actions: Fund Projects, Promote, Increase Workload (moderate) | favour of a community | shifts Zeitgeist/Trust [V3 steam 1.2.0 notes] | to rebalance factions |
| Send Frostland teams / colonise (moderate) | 20 teams for the first colony [V3 upcomer] | oil, coal, food, workforce | Chapter 1-2 |
| Transfer resources city <-> colony (moderate) | up to 5k per transfer [V3 upcomer] | feeds the Generator | when stocks drop |
| Upgrade storage, build hospital (moderate) | materials | storm buffering; disease gets worse later [V3 outsidergaming] | before whiteouts |
| Accept newcomers / delegates (rare) | housing | population and faction growth | when prompted |
| Chapter branch decision (rare) | the rest of the campaign | see section 1 | end of a chapter |
#### 4. First hour, step by step
Sources: Upcomer Chapter 1 guide [V3 upcomer, 19 Sep 2024], Selphie Chapter 1 [V3, 21 Sep 2024], Outsider Gaming [V3, 25 Mar 2025]. Pre-1.2/1.3 builds; some menus moved.
1. Optional: do the Prologue, but the author calls it "a slow tutorial" and says the main systems open in Chapter 1 [V3 outsidergaming].
2. Pause, review resources, frostbreak toward the coal.
3. Build two Housing districts on the outskirts and frostbreak toward the southern materials.
4. When the next frostbreak opens, fill six tiles with an Extraction District around the coal; build a Food district.
5. When Extraction finishes, turn on the Generator.
6. Expand Housing, build a Research Institute, research a new coal mine (Dust vs Blasting Coal Mine, a materials-cost choice) and build it.
7. Frostbreak the remaining coal and cover five deposits with extraction.
8. Build a Council Hall and pass the vote of confidence; save first, the vote count can vary [V3 upcomer].
9. Build a Logistics district on an Old Waystation (SW, W, N of New London) and accept new Londoners.
10. Explore: Foothills (coal) or Frozen Bay / Desolate Coast (oil).
11. Make friends with factions to earn heatstamps; keep promises.
12. Send 20 Frostland teams to the Old Dreadnought, open its oil, build the trail.
13. Transfer 75 oil to New London to finish Chapter 1.
#### 5. What changes later
- Chapter 2: two routes (oil/Surplus Injector vs Adaptive Pumps and a 2,000-person Frostland settlement) then a whiteout; Chapter 3 finds Winterhome; Chapter 4 has a 48-week gas-outburst timer and either 40 Cores or a 9,000-person Winterhome; Chapter 5 is assassination and civil war [S3 search of selphie/gamerguides chapter pages, 2024].
- What changed since launch: 1.1 QoL (cancel construction, edge scroll, autosave options); 1.2 new tutorial pop-ups, infinite deep deposits, Ambitions changed; 1.3 per-district heat, Serenity, The Pit map, Tales; 1.5 DLC Fractured Utopias (8 factions with skill trees, 100+ events); 1.6 DLC Breach of Trust: New Edinburgh and the Aurora colony, five factions, tremors and Volcano Night, an Independent Colony system with "diplomacy, trade, coercion, or outright conquest", Resistance and weapons-cost abilities [V3 steam news items 2024-2026].
#### 6. Failure and ending
Failure: the city collapses into anarchy, or a chapter timer (Chapter 1's coal timer) runs out - what happens at zero was not read `?`; Tales in the sandbox end in "Game Over" if failed [V3 Wikipedia ; steam 8 May 2025]. Ending: the campaign ends when the faction conflict is resolved (peace, banishment, or becoming Captain with segregation camps) or the city falls; an epilogue follows Lily May [V3 Wikipedia]. Recovery: load a save; long-term recovery from low Trust is slow ("harder to recover than material losses") [V3 outsidergaming].
#### 7. Consequential vs cosmetic choices
- Consequential: faction commitments and promises - votes depend on them and factions radicalise [V3 Wikipedia ; outsidergaming].
- Consequential: Chapter branch picks (route, Winterhome, Chapter 5) change what later chapters demand [S3].
- Consequential: heat allocation and storage before whiteouts (post 1.3, deaths are tied to factions) [V3 steam 8 May 2025].
- Probably dominant: do not force laws (one reviewer: forcing damages faction relations; "no faction is objectively right") [V3 outsidergaming, one author]. Cosmetic (my judgement): district shapes and the legacy layout option, monument looks.
#### 8. Open items
- v2 FP2 cells confirmed [V3]: Council 100 seats, 51 majority, two-thirds for power-granting laws (Wikipedia), 10-week cooldown after pass or fail (gamerguides), weeks as the time unit.
- Out of date: pre-1.3 numbers such as "Heatpipe Watch -20 Heat Demand" [V3 gamerguides] - 1.3 replaced Heat Demand with district heat levels [V3 steam 1.3].
- Difficulty names `?`/[CONTESTED]; the "624 weeks" coal timer in one guide looks mistyped `?`.
- Breach of Trust F5/F6: Steam notes show Resistance abilities costing weapons (Enforce Military Zone 75->50, Force Takeover 200->120) and "Conquering Aurora" [V3 steam 2 Jul 2026]; whether battles are resolved in real time is not stated `?` (v2: not real time).
- Prologue contents and the vote-of-confidence mechanics not read in full `?`; PC Gamer tips page was paywalled/empty.

### Banished - facts line
Shining Rock Software (Luke Hodorowicz); survival city builder, no money, no win state; released 18 Feb 2014 (Steam post "Now Available on Steam" 18 Feb 2014 [V3 steam news appid 242920]). Version relied on: **game patch 1.0.7, build 170910**; the dev's mod page says "The mod kit is currently version 1.0.7 Build 170910" and gives no date (so "Sep 2017" is inferred from the YYMMDD build number) [V3 shiningrocksoftware.com/game/mods/]. 1.0.7 notes are crash fixes, custom-resource flags and "a bug caused by town hall deletion while nomads are in route" - no balance change [V3 same page]. Tutorial assumes Moderate difficulty, disasters on, default map seed. Time: at 10x speed a year takes about 10 minutes [V3 banished-wiki.com/wiki/Seasons], so a first hour at 10x is about 6 years; a full 12-16-year population cycle is 2-3 hours.
#### 1. Setup choices
- **Difficulty** (names Easy / Moderate / Hard per the wiki): Easy = 6 families, lots of clothing, food, firewood, materials, tools, houses and storage already built, seeds and livestock. Moderate = 5 families, food, firewood, tools, materials, a storage barn, some seeds (no clothing). Hard = 4 families, small amounts, no seeds; seeds and livestock only after a Trading Post trade [V3 banished-wiki.com/wiki/Tutorials/Getting_Started_Guide].
- **Disasters on/off**: tornadoes, fire, field/orchard pests, livestock disease go away; starvation, hypothermia, disease, harsh winters and work accidents stay either way [V3 banished-wiki.com/wiki/Disasters].
- **Map seed** (random by default, can be typed so two players get the same terrain) [V3 banished-wiki.com/wiki/Map_Seeds]; **map size, terrain (valley vs mountains) and climate** exist, exact labels `?` [S3 search 22 Oct 2026 of reviews].
- **Tutorial scenarios** in the main menu: Getting Started, Survival, Food Production, Trade [V3 wiki Getting_Started_Guide].
- No ruler, faction or character; names, sex and looks of citizens are random [V3 wiki Citizens].
#### 2. The loop
Clock: real time with pause and speed-up; a year is 12 named "seasons" (Early Spring ... Late Winter, new year at Early Spring) and citizens age 5 times a year [V3 wiki Seasons, Citizens].
1. Pause and place buildings. A placed building leaves a footprint; laborers clear it and carry logs, stone and iron; when materials are in, a builder constructs it [V3 wiki Getting_Started_Guide].
2. Set how many citizens work each profession in the Town Hall or Professions interface; whoever is unassigned becomes a laborer (hauling, building). You never order one person [V3 wiki Citizens].
3. The game runs: citizens choose tasks, haul, eat from stores, heat homes, wear clothes and tools, marry, have children, age and die. Automated: all of that.
4. Seasons set pressure: spring planting, summer the lowest stored food, autumn harvest (early frost can kill unharvested crops), winter the harshest (cold, no farming) [V3 wiki Seasons].
5. Interrupts: nomads ask for citizenship at the Town Hall (accept or reject); traders arrive at the Trading Post; disasters if on; disease outbreaks; starvation or freezing messages [V3 wiki Nomad, Trade, Disasters]. Control stays with you; the game does not take it away.
6. You react by adding houses, jobs or stocks; the lag is long (children take about 10 years to work).
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Place houses (constant) | wooden: logs; stone: much more stone | one family per house, up to 8 people; sets birth rate (see section 8) [V3 wiki House] | all game; the main dial |
| Set profession counts (constant) | none; pulls from laborers | who farms, fishes, mines, teaches | every season |
| Food buildings: Gatherer's Hut, Fishing Dock, Hunting Cabin (constant early) | logs, stone | Gatherer yields most; hunting also gives leather for Hide Coats [V3 wiki Getting_Started_Guide] | year 1 |
| Farms, orchards, pasture (frequent, later) | seeds, land, frost risk | steady food, but early-frost/disease risk [V3 same] | after year 1-2 |
| Firewood: woodcutter, forester (constant) | workers | winter survival; a wooden house uses about 25 firewood a winter [V3 wiki House] | before winter |
| Storage barn / stockpile / market (frequent) | wood | shorter hauls; Market raises happiness [V3 wiki Citizens] | as the town spreads |
| Tailor, blacksmith (frequent) | iron, leather, labour [M] | warm clothing keeps citizens warm longer outdoors [V3 wiki Seasons]; tools [M] | by year 2-3 |
| Trading Post (moderate) | wood; goods | buy seeds/livestock/tools, sell surplus; no money, goods have values; ordered goods cost 25% more [V3 wiki Currency] | to get seeds, or surplus firewood |
| School, hospital, cemetery, chapel, well, tavern (moderate) | materials, staff | education speeds work; hospital cuts disease [V3 wiki School, Hospital] | once food is stable |
| Accept or reject nomads (rare) | food and houses | instant population; may bring foreign disease [V3 wiki Nomad] | at each request |
| Upgrade wooden to stone house (rare) | same cost as new stone; occupants evicted | 1/3 less firewood [V3 wiki House] | when spare housing exists |
| Boarding House (rare) | most materials | shelter for nomads only [V3 wiki House] | before accepting nomads |
#### 4. First hour, step by step
Source: the wiki Getting Started Guide, which follows the in-game tutorials [V3 wiki Getting_Started_Guide]; the 5-ages-per-year and housing rules from the Citizens and House pages.
1. Play the "Getting Started" tutorial first.
2. New game: Easy or Moderate for a first run; Hard has no seeds.
3. Pause. Look at the families, food, firewood, tools, materials.
4. Homes first: every starting family needs one before winter; build wooden houses near work buildings.
5. Food: a Gatherer's Hut in thick forest, a Fishing Dock, a Hunting Cabin; skip crops, orchards and livestock for now.
6. Add a Herbalist and Forester next to the Gatherer; hunting leather lets the Tailor make Hide Coats against hypothermia.
7. Add woodcutters and stock firewood.
8. Open the Town Hall to set job counts (nomads need a Town Hall as well) [V3 wiki Nomad].
9. Build a school early so that children born now are educated; only a child who can enrol at age 10 ever can [V3 wiki School].
10. Add houses only as food and fuel allow: spare housing is what lets couples form and have a few children [V3 wiki House].
11. Build a Hospital before accepting nomads (disease) and a Boarding House for them.
12. Visit the Trading Post when you need seeds or tools; sell firewood.
13. Watch the winter: if housing runs short people "die very quickly" of cold [V3 wiki Getting_Started_Guide].
#### 5. What changes later
- Crops, orchards, herds and Taverns; mines and quarries for iron and stone, then blacksmith tools; stone houses; chapels and cemeteries for happiness.
- Pressure ramps by demography, not by a script: children become workers (or students) about two years after birth (age 10 at 5 ages a year, my arithmetic), a big cohort ages together, and pairs who move in together can die of old age "at almost the same time" and overload housing (one poster's claim) [V3 steam thread 358417461601681934].
- Hunting grounds and soil deplete, tools and clothes wear, and trade fills gaps [M].
#### 6. Failure and ending
Losses come from starvation, hypothermia, disease or accidents and cascade because dead workers stop producing; a town can end with extinction [M]. There is no victory screen; play is open-ended (the pre-release FAQ speaks of optional goals that can be disabled `?`) [V3 banished-wiki.com/wiki/FAQ]. Recovery is possible while adults and a spare house remain (my inference).
#### 7. Consequential vs cosmetic choices
- Consequential: housing pace, which sets how many couples start families; the page says a household "will only conceive a few children before stopping" [V3 wiki House].
- Consequential: winter housing and firewood before the first cold; food mix early (gatherers/fishers/hunters), seeds and livestock only through trade on Hard [V3 wiki].
- Consequential: school early (education raises output) [V3 wiki School]; nomad acceptance (food, housing, disease).
- Cosmetic: house style (6 wooden, 6 stone) [V3 wiki House], map seed look, citizen names.
- Dominant-looking: wooden houses first, stone later (the wiki's advice).
#### 8. Open items
Capability-table (v2 R3b section 3) corrections:
- L2 "~1 age per 2.4 seasons": the wiki counts 12 "seasons" per year, so 2.4 of them = 1/5 year; in four-season terms it is 0.8 of a season per age-year [V3 wiki Seasons]. One Steam poster's displayed-age conversion (40 shown = 10 years) does not fit 5/yr [V3 steam thread 358417461601681934] [CONTESTED].
- L2 lifespan `?` -> player reports only: "in their 60s" on poor diets, "mid 80s, a few 90s" when healthy, oldest seen 94 and 89 [V3 steam thread 1694917906659024571]; no developer or datamined figure found; education's effect on lifespan not found (the page says only productivity) [V3 wiki School].
- B6 "unhappy workers less effective `?`" -> found: "Happiness affects productivity. An unhappy population will idle frequently" [V3 wiki Citizens].
- L3 marriage rules `?` -> partly: a house must be empty or hold one young resident for a couple to form; adults otherwise stay with parents [V3 wiki House].
- B2/K3 nomads: Town Hall needed, group size scales with population, a refusal tends to shrink the next group, may bring foreign diseases (was [M]/anecdote) [V3 wiki Nomad].
- Version: 1.0.7 confirmed; no date on the page.
Attachment claims (nine-title doc, section 8):
- L280 "five personal years per in-game year": CONFIRMED [V3 wiki Citizens, Seasons]; "one year of age per 2.4 seasons" is true only in the wiki's 12-season year (see above).
- L280 "labouring age ten, students until sixteen to eighteen": CONFIRMED (10 and 17) [V3 wiki School].
- L280 "maximum of 75, spread about 15": NOT SUPPORTED - players report old-age deaths into the 80s and 90s [V3 steam thread 1694917906659024571]; both rest on anecdote.
- L282-284 "housing vacancy as the reproduction gate": CONFIRMED with nuance - "most likely won't" find a spouse, not "never"; "a few children" per household [V3 wiki House].
- L292 (also L17, L367) "twelve-to-sixteen-year die-off, populations halving, one or two houses a year": mechanism consistent with wiki rules; the numbers are community lore, not found in a source `?`. Arithmetic: 12-16 years is about 2 to 2.7 hours at 10x [V3 wiki Seasons].
- L278 "no money beyond barter": CONFIRMED [V3 wiki Currency]; "age-distribution graph" (L422) not checked `?`.

Sources opened this session: Steam news API (appids 1363080, 323190, 1601580, 242920); gamerguides.com Manor Lords pages; pcgamesn approval-rating and settlement-level; destructoid ?p=502092; gamerant victory-conditions; Steam forum threads 4355619963546558875, 1694917906659024571, 350533172701123370, 358417461601681934; en.wikipedia.org Frostpunk and Frostpunk_2; thegamer.com Frostpunk beginners and Book of Laws; keengamer 5 basic tips; gamepressure adaptation; gog.com build orders; ludo.guide special events; outsidergaming.com 9 tips; upcomer and selphie1999gaming Chapter 1; gamerguides Frostpunk 2 laws; store.steampowered.com appdetails 1601580; shiningrocksoftware.com/game/mods/; banished-wiki.com pages (Citizens, Seasons, House, School, Nomad, Disasters, Map_Seeds, Currency, Getting_Started_Guide, FAQ); vaporlens.app banished. Blocked: wiki.hoodedhorse.com (Cloudflare 403, not bypassed), Gamespot, Sportskeeda, PC Gamer tips, Nexus docs, Steam workshop (429).
