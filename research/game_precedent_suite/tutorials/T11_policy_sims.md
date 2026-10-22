# T11 (v3 tutorial pass) - Policy / court sims: Tropico 6, Suzerain, Dragon Age: Inquisition, Democracy 4
Tags: [V3 url date/version] page body read this session (2026-10-22); [S3 url] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED] sources disagree; [v2] carried from the v2 table, not re-opened.
Fetch notes: Fandom pages read through its MediaWiki API (`api.php?action=query&prop=revisions`, browser User-Agent), page-edit dates quoted; suzerain.wiki.gg via `index.php?...&action=raw`.

### Tropico 6 - facts line
Limbic Entertainment, published by Kalypso Media (maintained by Realmforge since Sep 2020); city-builder + dictator sim; PC release 2019-03-29, consoles later [V3 tropico.fandom.com/wiki/Tropico_6, rev 2025-07-15]. No patch pinned: wiki revisions span 2019-2026, the newest DLC listed is Return to Nature (2025-03-06) [V3 .../DLC_(Tropico_6), rev 2026-02-09]. Assumed: sandbox or the first mission on a Caribbean archipelago, Colonial start, Normal difficulty. A session: the 15 missions together take about "25 hours" [V3 gamepressure.com/tropico-6/how-long-does-it-take-to-complete/z8fb88]; one mission or sandbox sitting 2-4 h [M]; sandbox has no fixed length (same page).
#### 1. Setup choices
- Mode: tutorial (five chapters: economy basics; citizens and politics; government; advanced economy; advanced gameplay [S3 xboxaddict.com/Staff-Review/14310/Tropico-6.html]); 15 unrelated missions, more unlock as you finish a set number; DLC campaigns of 4-5 missions (Caribbean Skies, Festival, New Frontiers, Going Viral); sandbox; 2-4 player co-op/competitive [V3 .../Missions_(Tropico_6) rev 2024-06-19; .../Tropico_6; .../DLC_(Tropico_6)].
- Difficulty Easy/Normal/Hard = five sandbox dials: Foreign Aid (Plenty/Fair/None), Caribbean Happiness (Weak/Average/Strong), Political (Forgiving/Fair/Aggressive), Opposition (Friendly/Reluctant/Strong), Pirate (Cabin Boy/Skipper/Captain Blackbeard); disasters are off at every level except mission-specific ones [V3 Missions page].
- El Presidente: gender, outfit, hat, beard etc. (cosmetic) plus TRAITS - Apologetic, Charismatic (+2 standing with each faction and superpower), Compulsive Hoarder, Corrupt (+5% to Swiss payments), Kind of Normal, Manipulative (+50% standing from praising a faction in speeches), Pyromaniac, Savant, Seductive, Soft-Hearted, Spatial Sense Prodigy, Workaholic [V3 .../Customization_(Tropico_6) rev 2026-05-25]. How many traits you may take: `?`.
- Palace layout/garden/decor: cosmetic [V3 same page]. Map and start era in sandbox: `?` (missions fix both: era is printed on the mission card [V3 Missions page]).
#### 2. The loop
Clock: real time with pause and speed settings [M]; the game counts in months and years (edict cooldown "12 months", Early Elections "in 12 months" [V3 .../Edicts_(Tropico_6) rev 2025-06-20]). Repeating cycle:
1. Pause, read the Almanac (eight tabs: Overview, Happiness, People, Economy, Politics, Foreign Relations, Building List, Conflicts [V3 gamepressure.com/tropico-6/almanac/z8c04a]), pick the next problem.
2. Place or upgrade buildings, set work modes, wages and job priorities; unpause. Builders, hiring, housing choice, commuting, trade-route hauling and eating/praying all run by themselves (citizens are individually simulated [v2]).
3. Each month the economy ticks [M]: wages out, taxes/exports in, Knowledge from libraries/schools accrues toward research (per-month Knowledge is in Ministry text [V3 .../Ministry_(Tropico_6)]).
4. Happiness (average of eight needs: food, health, entertainment, faith, housing, work quality, liberty, safety) feeds approval; faction standing feeds it too [V3 gamepressure.com/tropico-6/happiness-and-approval/zbc04d].
5. Interrupts: Crown / faction / superpower requests with rewards; faction demands (two factions can ask at once and you must side with one); protests (negotiate, concede, or send the military); rebels and coups; pirates; era change; elections. Each pauses into a pop-up you answer.
6. Era gates (Colonial -> World Wars -> Cold War -> Modern Times) unlock buildings, edicts, factions and constitution paragraphs; the next-era goals are visible as tasks.
Automated [M]: citizen behaviour, pathing, production chains once supplied, trade routes once set, rebel spawning.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Place / upgrade building | construction $ plus workers | jobs, goods, happiness, faction likes/dislikes | CONSTANT |
| Work mode, wages, job priority | wage bill; efficiency | productivity vs. morale ("cutting pay -> bad morale" [V3 gaming.net tips]) | constant |
| Trade routes / export / import | teamsters, docks | revenue, superpower relations | frequent |
| Research | Knowledge Points | unlocks upgrades, edicts, buildings [V3 gamepressure starting tips] | frequent |
| Edict | where printed: Colonial $500-$7,500, World Wars $0-$10,000 (Cold War/Modern `?`); most have rank 1/2/3 | trade a benefit for faction standing or other costs | occasional |
| Constitution paragraph | research for half; changeable only "once a few years" [v2] | permanent rule shifts + faction likes | rare (12 slots) |
| Appoint / fire minister | Ministry building $16,000 (blueprint $8,000), upkeep $10 plus $60 per minister; firing $2,000 | +2 standing with the minister's faction plus a per-faction department perk [V3 Ministry page] | occasional |
| Answer faction demand / dual demand | build or spend what they ask | gain with one faction, lose standing with the rejected one [V3 .../Dual_Demands_(Tropico_6)] | frequent |
| Election speech | no cost stated | issue acknowledgements, praise (+10 relation), blame a superpower, promises [V3 .../Election_Speech_(Tropico_6)] | each election |
| Cancel / delay an election | Martial Law $7,500 or the Early Elections edict $2,000 | see section 6 | when losing |
| Swiss-account actions via the Broker | Swiss $ | buy Science/Raid Points, immigrants, faction bribes, trade-route boosts [V3 .../Swiss_Bank_Account rev 2026-07-01] | occasional |
| Raids / heists | Raid Points | goods, immigrants, wonders | occasional |
| Protests, rebels | time, soldiers | negotiate vs. force; force can breed rebels | when they arise |
| Superpower dealings / alliance | tasks, embassy, support | relations; alliance triggers attack by the opposing bloc [V3 gamepressure eras] | era boundary |
#### 4. First hour, step by step
Source: the first mission "Penultimo of the Caribbean" start state ($80,000, 75 citizens, 100% approval, Colonial) [V3 Missions page] plus gamepressure's ten starting tips [V3 .../starting-tips/z7c004] and a five-tip beginner article [V3 gaming.net/tropico-6-best-tips-for-beginners/].
1. Play the tutorial first; the article suggests about two hours.
2. Start the mission; Lord Wyndham (the Crown) demands a Sugar Plantation, then a Rum Distillery; the pay-off is cash or a mandate extension - the guide says take the extension [V3 Missions page].
3. Look at deposits before building so you do not cover them.
4. Build the rum economy: plantation (operational mode) -> Rum Distillery; it needs no qualified workers.
5. Add a Teamster's Office beside each industry cluster; a Dock for export.
6. Build cheap housing near work; check the "target group" - rich housing early loses money.
7. Build a Library as early as possible - it makes Knowledge.
8. Keep wages up; do not over-build, every building needs workers; read open jobs and unemployment in the Almanac.
9. Build High School then College early or you will be importing educated workers.
10. Place Fire Stations and Newspapers (blue range circle) to cover the most area.
11. Take tasks from Wyndham, Penultimo and Sofia Ortega (Revolutionaries); the game then asks for Teamster Ports on three other islands, a gold mine, a pirate cove.
12. Optional, my inference [M]: buy a first cheap edict (Food for the People $500, Mandatory Siesta $500) once money is steady; no source ranks them.
13. After the guard towers the mission offers a target of 55 Food, 35 Faith or 55 Liberty happiness to win the people's support for independence [V3 Missions page]; watch the Politics tab for Revolutionaries support.
14. Independence: Revolutionaries relations at least 50% and more than 60% of the population [V3 gamepressure eras]; then bribe the Crown ($15,000 in this mission) or survive a two-squad attack - mission won [V3 Missions page].
#### 5. What changes later
World Wars: elections, Constitution, Ministry, the Swiss account and the Broker appear; Crown/Revolutionaries dissolve and Communists, Capitalists, Religious, Militarists form; the Allies/Axis attack if relations drop low enough [V3 gamepressure eras; .../World_Wars_(Tropico_6)]. Cold War: Environmentalists, Industrialists; you must ally with one bloc and the other attacks. Modern Times: Intellectuals, Conservatives; end paths political, nuclear or tourist [V3 gamepressure eras]. Pressure ramps by faction count (2 -> 4 -> 6 -> 8 concurrent) and by opposing pairs: Royalists-Revolutionaries, Capitalists-Communists, Militarists-Religious, Conservatives-Intellectuals, Environmentalists-Industrialists [V3 infoboxes on each .../<Faction>_(Tropico_6) page]. Economic scale: exports, tourism, space/Mars (New Frontiers), DLC systems (Lobbyistico adds a bribe-and-corruption club) [V3 DLC page].
#### 6. Failure and ending
Loss: Colonial mandate runs out; an election lost (election result is by votes against vs. for) [V3 .../Election_Speech_(Tropico_6) rev 2019-05-13 and .../Election]; palace destroyed by rebels, a coup or a superpower attack [V3 .../Coup; gamepressure eras]. Escapes: Martial Law cancels elections but costs liberty (-35/30/25 by rank), +15% rebel chance, -15 standing with all other factions, +30 Militarists [V3 Edicts page]; rigging a vote lowers Intellectuals and democratic expectations [V3 .../Election; T4-era text, T6 status `?`]. Win: mission goals met; sandbox has none - you stay in power; the Swiss balance is part of the final score and counts even if you are deposed [V3 Swiss page]. Recovery: a lost election/palace ends the run; short of those events, a bad stretch (angry faction, protests, rebels) can be recovered by reversing the policy [M].
#### 7. Consequential vs cosmetic choices
- Consequential: keeping approval high enough to survive the election, so faction standing (edicts, buildings, constitution, ministers all move it) is the real steering wheel - the Capitalist page lists which constitution options and edicts they like or hate, so every policy has a named loser [V3 .../Capitalists_(Tropico_6) rev 2026-07-10].
- Consequential: the era gate (independence and the alliance choice) shapes which factions and threats you face.
- Cosmetic: the palace and outfits. [CONTESTED] speech parts: the T6 speech page says "Acknowledge issues" "does not contribute to the approval of voters" while Praise a faction (+10 relation), Blame a superpower (voter approval up, relations down) and Promise improvements (the most dissatisfied undecided vote for you) do [V3 Election_Speech page rev 2019-05-13]; the series-wide Election page says acknowledging an issue makes upset voters ignore it [V3 .../Election rev 2026-05-27, T3/T4-era text]. Broken promises anger voters at the next election (same series page).
- Dominant answer by community consensus [V3 gaming.net; gamepressure]: rum economy and an early library; no rich housing early. Election play, April 2019 Steam threads (player opinion, launch builds): popularity edicts (free housing, tax cuts, Food for the People) shortly before a vote, bribing faction leaders ("can take years"), the Audience edict, and Martial Law when approval is near 0-20% [V3 steamcommunity.com/app/492720/discussions/0/1771511442698758441 and .../3570700856113482908]. Edict value cannot be judged: most Cold War/Modern costs are `?`.
#### 8. Open items
- v2 "Still unknown: Tropico 6 edict dollar costs" - FILLED for Colonial and World Wars: Food for the People $500, Church Fee $1,500, No Free Lunch $500, Mandatory Siesta $500, Urban Development $7,500, Advanced Boat Service $2,500, Free Housing $500, Audience $1,000, Agricultural Subsidies $5,000, Building Permit $1,500, State Loans $0, Wealth Tax $2,500, Industrialization $10,000, Early Elections $2,000, Literacy Program $1,000, Martial Law $7,500, Prohibition $1,500, Bells to Bullets $2,000, Military Police $0, Free Wheels $0, Right to Arms $2,500, The Tropico Papers $5,000 [V3 Edicts page]; Cold War/Modern `?` (the page prints no cost).
- v2 "Constitution total": 12 paragraphs, 3 options each (36), 4 per era in World Wars/Cold War/Modern; two per era start unlocked and two need research [V3 .../Constitution_(Tropico_6) rev 2025-07-01]. v2's 2-per-era-unlocked line (was [S2]) is now [V3]. Colonial has none.
- v2 faction list: ten, confirmed; name conflict [CONTESTED]: the wiki calls the Colonial pro-Crown faction "Royalists" (rep. Lord Roger Wyndham); gamepressure calls it "The Crown". Opposing pairs now [V3]: five, not four (adds Royalists-Revolutionaries).
- Ministry (v2 B3 "whether edicts require specific ministers"): the wiki shows ministers give department perks and +2 faction standing, no edict link [V3 Ministry page]; five departments listed: Education, Defense, Economy, Foreign Affairs, Interior.
- v2 "election result formula; coup chance": still `?`. Election cadence [CONTESTED]: "Every 10 years the people will ask for elections" (page rev 2019-05-13, pre-launch) vs. "the more stable democracy is, the more often elections will be scheduled" (series-wide page, T3/T4 text); gamepressure says only "regularly or not at all"; two April 2019 Steam threads give no interval either [V3]. Treat as unestablished.
- ATTACHMENT CLAIM 9226007a-Citizens_Settlements_and_Factions_-_Nine_Titles.md:229 "for Tropico 6 these are Capitalists, Communists, Militarists, Religious, Environmentalists, Intellectuals, Nationalists and Loyalists": WRONG on two names. Nationalists appear on the Tropico 5 faction page; Loyalists on the T3/T4 election text. T6 has Capitalists, Communists, Conservatives, Environmentalists, Industrialists, Intellectuals, Militarists, Religious, Revolutionaries, Royalists/Crown [V3 .../Faction_(Tropico_6) rev 2025-06-09; .../Tropico_6]. Note "eight" is right as the Modern Times concurrent count (gamepressure era table: 2/4/6/8), which is probably why 89a3a060-consolidated_twenty_games.md:177 ("Eight factions whose satisfaction conditions conflict") reads plausibly; the conflict part is supported by the five opposing pairs.
- ATTACHMENT CLAIM 9226007a:237 elections "won, bought through faction leaders and brokers, rigged, or simply not held, at escalating cost" (and :235 "cancelling an election or rigging it applies a comparable penalty"): mostly SUPPORTED: not held via Martial Law and the cancel option [V3 Edicts; Election_Speech]; rigging offered to a losing president [V3 .../Election, series text]; bribes via the Broker and the El Presidente Club buy faction standing, not votes [V3 Swiss page; DLC page]. "At escalating cost": no source seen, `?`.
- ATTACHMENT CLAIM 9226007a:241 Swiss bank "in earlier entries mostly a score; from the Modern Times era onward a minimum balance gates real capabilities": SUPPORTED as series history - the wiki says money in the account gates corrupt actions and the palace-to-presidency upgrade in the Tropico 4 expansion Modern Times [V3 Swiss page]. For Tropico 6 it misleads: the account exists from World Wars and already spends on Science/Raid Points, immigrants, faction bribes, distractions and trade routes [V3 Swiss page]; T6 also has an era called Modern Times, which the phrase invites you to confuse.
- Not checked: 9226007a:225 "Tropico 7 announced for January 2027".

### Suzerain - facts line
Torpor Games (Berlin); text-based political RPG / government sim. Publisher Fellow Traveller, then Torpor self-publishing from the 3.1 "Sovereign" update (2025-05-07) [V3 Steam news, store.steampowered.com ISteamNews app 1207650]. Windows/macOS 2020-12-04, Switch 2021-09-23, Android/iOS 2022-12-08 [V3 suzerain.wiki.gg/wiki/Suzerain raw]; Kingdom of Rizia DLC 2024-03-25 [V3 store.steampowered.com/api/appdetails?appids=2352340]; consoles 2025-11-11 [V3 Steam news 2025-11-11]. Version: 3.1.0 line; newest build title seen "Patch 3.1.0 Build 175" 2026-06-09 [V3 Steam news list]. Assumed: the base game (Republic of Sordland, President Anton Rayne), Torpor Mode default; Rizia noted last. Session: whole game "under twelve hours" [V3 en.wikipedia.org/wiki/Suzerain_(video_game) raw]; minutes per turn `?`.
#### 1. Setup choices
- Campaign: Republic of Sordland (base) or Kingdom of Rizia (DLC, King Romus Toras) [V3 wiki Suzerain page]. Rizia accepts a transferred Sordland save or a chosen "Rayne archetype" [V3 Steam news 3.1 notes; Xbox blog].
- Mode: Torpor Mode is ON from the start - autosave at each turn start and after important conversations or decisions (Rizia: also after a decree is signed); once you have finished a game you may switch it off and skip the prologue; achievements only with it on [V3 Steam news 2025-09-25 "Suzerain Intelligence Dossier: Tips #1"]. Aids: "Skip Read Dialogue Text", a Journal (decisions diary, past reports, 1,000-character notebook) [same post].
- Prologue choices ARE the character build: Family - Deyr (poor: Personal Wealth 1, public opinion up, Oligarchs skeptical), Holsord (middle: PW 2), Lachaven (rich: PW 3, public opinion down, Oligarchs like you) [V3 wiki Turn]; Formative Years path Hard / Normal / Easy = starting Government Budget +5/+7/+9 (Easy also Economy +2, PW +1) [V3 wiki Decision]; University - Law (helps constitution reform), Economics (curbing recession), History (foreign policy); Extracurricular - Student Council (+1 economic development), Debate Group (stronger speeches), Human Rights Group (international standing); Youth organisation - Red Youth / Young Sords / neither; then USP-internal stance (back Alphonso / neutral / back Soll), how to take power from Alphonso (3 ways), campaign promise Democratic Reforms vs Preserve National Values [V3 wiki Turn + Decision].
- Turn-1 campaign promises: economic direction (planned / market), diplomatic leaning (East / West / Neutral), immigration (toughen / keep relaxed), term focus (Education / Defense / Law & Enforcement / Health) [V3 wiki Decision]. Rizia: a traits system (3.0.0 changelog) and the archetype pick (3.1) [V3 Steam news 3.0.0 and 3.1 notes].
#### 2. The loop
Clock: story turns, not real time. Prologue + 12 turns (each "four months of Rayne's four year term") + epilogue + summary [V3 wiki Turn]. Per turn:
1. The turn opens (autosave) with a briefing; you read reports and tokens on the table/map: country and city tokens, policies, situations, news, reports [V3 Steam store text, appdetails 1207650].
2. A chain of scenes (cabinet meetings, personal confrontations, press conferences [V3 Xbox blog 2025-11-11], family dinners) each ends in a choice. A choice carries signed stat increments: Government Budget, Economy, Personal Wealth, Public Opinion, Country Unrest, ideology and group meters (Democratic, Malenyevist, Sollist, Capitalist, Bludish Opinion...) [V3 wiki Decision].
3. The Assembly sends bills: sign or veto (veto only while the constitution still gives it) [V3 wiki Bill]. Constitutional reforms and presidential decrees are chosen when their turn arrives (Turn 7: up to 3 decrees from a list of 18) [V3 wiki Presidential_decrees].
4. Some choices are gated by stats: a superpower-clash decision "will only happen if Government Budget is -8 or lower" [V3 wiki Decision]; vote outcomes by seat count ("90 votes" shortfalls [v2]).
5. A budget allocation across Healthcare / Law and Order / Education / Military; skipping the promised "term focus" costs 4 Public Opinion [V3 wiki Decision, Turn 3].
6. The turn ends; the Journal files the choices; consequences arrive later through news, reports and later triggered decisions. Automated: all NPC behaviour, vote tallies, economy, news. No dice found; failure comes from thresholds [v2].
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Pick a dialogue stance / tone | none shown | relationship and meter shifts | CONSTANT |
| Sign / veto a bill (22 listed in order) | opinion meters of the bloc you cross | e.g. campaign-finance bill: sign = Democratic -3, Malenyevist -2, Sollist +1; veto = Sollist -1, Democratic +2 [V3 wiki Bill] | about each turn |
| Decision with a priced option | Government Budget -1 to -3, Personal Wealth -1 to -3 | megaproject, contractor, investment, subsidy | frequent |
| Contractor choice (Turn 2) | State Corp -1 Budget, less professional; Underhall -1, professional; Taurus 0, mediocre [V3 wiki Turn] | infrastructure quality | rare |
| Personal investment (Armadine shares 1/2/3 PW) | PW | later returns, later offers | rare |
| Accept or refuse a bribe / media deal | favours owed; Koronti: two favours [V3 wiki Turn] | press support, scandal risk | occasional |
| Budget allocation | e.g. Healthcare increase: Government Budget -2, Economy +1 [V3 wiki Decision, Turn 3] | funds the promised focus | occasional |
| Appoint / dismiss ministers | constitution sets who confirms | agendas, plots | occasional |
| Constitutional reform / political path (Reformist, Dictator, Autocrat) | Assembly and Supreme Court votes | locks later powers and endings [V3 wiki Political_path] | rare, decisive |
| Presidential decree (Turn 7) | none stated; judicial review limits it | e.g. VAT, amnesty, purge General Staff | rare |
| Diplomacy: alliance, embargo, trade, reparations | opinion with blocs | war risk | occasional |
| Security: state of emergency, Secret State Police, Anti-Corruption Police | legitimacy; impeachment risk | stop plots, enable endings [V3 wiki Endings, Decision] | rare |
| Speeches / campaign | Personal Wealth for ads [v2] | Public Opinion | election run-up |
| Family and personal scenes | emotional | endings such as retirement or exile | rare |
#### 4. First hour, step by step
Source: the wiki's Turn page, which walks Prologue, Turn 1 and 2 [V3 suzerain.wiki.gg/wiki/Turn raw].
1. Pick a family background (sets Personal Wealth and public opinion) and a path difficulty.
2. Choose university and major; Soll offers a ministry later if you vote for him.
3. In 1927 the coup: join the protest or hide ("will not have a huge effect"); pick a student group.
4. Join Red Youth, Young Sords or neither; each moves the left/right meters.
5. Pick a side in the USP; take power from Alphonso; make the campaign promise. Prologue ends.
6. Turn 1: set your term promises (economy, alignment, immigration, focus). Sign or veto the Electoral Campaign Finance Bill (signing limits public money to parties above 10%).
7. Decide whether to invest in Armadine (cap depends on your PW) and whether to meet media owner Koronti.
8. Confirm the free-market or planned economy (the wiki says you usually want what you promised).
9. Choose the mega-project: H-3 Highway (helps poor Agnland, closer to Agnolia) or L-1 High-speed Rail (boosts trade, ends recession faster) [V3 wiki Decision].
10. Say whether you will work with reformers on a new constitution.
11. Turn 2: make a public statement; hear the Oligarchs' bribe; pick the construction contractor; answer Koronti's media offer.
Guidance from the developers' tips post: learn Sordland's history, factions and constitution first; "you can't please everyone"; manage the economy; watch advisors and the press [V3 news.xbox.com 2025-11-11].
#### 5. What changes later
Turn 3 on: unrest, youth-group bans, budget allocation; bills pile up (22 total); Rumburg crisis and war/ATO-CSP choices; Heljiland; the Bludish dam revolt; Turn 7 decrees; a hidden "Late Game Crisis" counter feeds decisions ("Late Game Crisis is higher than 2") [V3 wiki Decision]. What scales: constitutional lock-in (Reformist/Dictator/Autocrat) and the threat of the final speech assassination. What Rizia adds: royal decrees in six categories (Order, Economy, Welfare, Trade, Construction, Religion; roughly 130 listed), each costing Authority (1-7 where stated) and often Energy, with implementation of "~2 Turns"; Authority has a capacity and per-turn income; noble Houses (Toras, Azaro, Sazon...) as factions; turn-based war and (3.1) an air force; House of Delegates [V3 wiki Royal_decrees (a stub page); Steam news 3.0.0, 3.1; v2].
#### 6. Failure and ending
No dice; you lose by thresholds and plots. Sordland main endings on the wiki: Reelection, Assassination (always at the final pre-election speech; avoid with Serge's lucky charm or by founding the Secret State Police), Lost Election (1957), Impeached, Early Retirement, Path to Exile, Coup d'etat, Hail the Queen (lose the war with Rumburg), World At War (nuclear exchange) = nine, with 16 sub-endings listed though the page says twenty [V3 wiki Endings]; the store says nine and "more than 25" [V3 appdetails 1207650] [CONTESTED]. Recovery: Torpor Mode gives automatic checkpoints only ("fewer save points") and can be switched off after one finished run [V3 Tips #1]; a lost election or exile is an ending, not a retry.
#### 7. Consequential vs cosmetic choices
- Consequential: the constitution path, the economy promise, and the Rumburg/alliance chain - they decide which of the nine endings exist.
- Consequential: Budget/Public Opinion ledger - choices carry visible increments, so you can price them.
- Cosmetic or soft: the protest-or-hide scene ("will not have a huge effect"), Collectibles (35 mementos shown on the desk, cannot all be got in one run) [V3 wiki Collectibles; Turn].
- Not established: how much tone/dialogue choices matter beyond increments - the developers' blog says "subtle but lasting ways" [V3 Xbox blog].
#### 8. Open items
- ATTACHMENT e3f9f19a-thirteen_strategy_games.md:154 "Roughly 1.4 million words in the base game, about 1.5 million with the DLC": NOT SUPPORTED. Figures found: 450,000 (developers, via Wikipedia citing Der Spiegel 2021) [V3 wiki raw]; "1 Million+-word" (Steam store text, 2026-10-22) and "over one million words" (Steam post 2025-11-11) [V3]; the Rizia changelog says "Over 400k words of story" (2024-03-25) [V3 Steam news 3.0.0]. So base ~1M+ and DLC ~0.4M, not 1.4M + 0.1M. v2's 450,000 is a launch-era figure [CONTESTED across versions].
- ATTACHMENT e3f9f19a:152 "Kingdom of Rizia DLC 2022": WRONG - announced 2023-05-04, released 2024-03-25 [V3 wiki Suzerain; appdetails 2352340].
- ATTACHMENT e3f9f19a:162 and :174 Authority "political capital and time to enact policy" with "Energy" in Rizia: Authority is NOT a base-game resource. "New resources for Authority and Energy" are listed under the Rizia DLC changelog [V3 Steam news 3.0.0]; Steam's Rizia page says "new invaluable resources such as energy and authority" [V3 appdetails 2352340]; the Xbox blog names Authority only for Rizia decrees. Base-game meters are Government Budget, Economy, Personal Wealth, Public Opinion and groups [V3 wiki Decision]. Authority is spent per decree, has capacity and per-turn gain [V3 wiki Royal_decrees]. "Hoard Authority for end-of-turn" (:174): no source seen, `?`. Not checked: :266 "alignment, unrest and opinion hidden from the player".
- v2 cell corrections: D1 verbs also include Sordland presidential decrees (Turn 7, 18 listed); v2 Rizia "energy and authority [S2 Epic listing]" now [V3]; I1/I4 was `?`: Secret State Police and Anti-Corruption Police are decisions in Sordland [V3 wiki Endings; Decision]; M1 sub-endings 16 on the wiki page / 25+ per store; M2 words see above; F: Rizia has War, Armed Forces and (3.1) air-force mechanics, resolution still `?`.

### Dragon Age: Inquisition (the war table) - facts line
BioWare / Electronic Arts; action RPG whose strategic layer is the war table; NA release 2014-11-18 [V3 en.wikipedia.org/wiki/Dragon_Age:_Inquisition raw]; Steam "Game of the Year Edition" listing 2020-06-04 [V3 store.steampowered.com/api/appdetails?appids=1222690]. Version: operation rewards differ by Patch 10 (2015-09-02) and the Trespasser DLC [V3 dragonage.fandom.com/wiki/War_table rev 2026-08-03]; assumed final patch, base game plus Skyhold, Normal difficulty. This section keeps to the table as a loop. A table visit takes a few minutes [M]; the whole game is dozens of hours [M]; operation timers run 0 (scouting) to about 24 hours [V3 same page: "18-24 hours long without agents"].
#### 1. Setup choices
- Before the table exists you pick: race (human, dwarf, elf, Qunari), class (warrior, mage, rogue) [V3 Wikipedia raw], looks and difficulty (Casual/Normal/Hard/Nightmare [M]). None sets up the table: advisors, operations and resources are fixed; it unlocks during play (first scouting op appears in Haven [V3 .../Scout_the_Hinterlands rev 2026-08-02]).
- The table-shaped choices come as you play: which advisor runs each operation; mages or templars (exclusive); which Divine candidate to back [v2]; which Skyhold upgrade (one of three per project, irreversible) [V3 .../Major_Upgrades rev 2026-07-29].
#### 2. The loop
Clock: real time. Mission timers run "independently of the save file's time" - even with the console unplugged [V3 War_table page]; scouting is instant.
1. Field play: explore regions, close rifts, set camps, take keeps, complete quests - this earns the two table currencies. Power: critical-path plots, camps, rifts, keeps, landmarks, high dragons [S3 Prima eGuide snippet]; Influence: "most quests" [S3 same].
2. Return to the war room (Haven, later Skyhold) and open the map. Operations are of two kinds: scouting (instant, costs Power, unlocks a region and its resource ops) and mission (timed, gives Influence/items/unlocks) [V3 War_table page].
3. Read the card: requirements (story flag or Inquisition Rank), Power cost, a time per advisor, rewards. Three advisors: Josephine (Connections), Leliana (Secrets), Cullen (Forces) [V3 .../Scout_the_Hinterlands].
4. Assign one advisor. Some ops have a preferred advisor, 20% faster; each recruited agent cuts that advisor's times by 5% [V3 War_table page].
5. Leave. While you play the timer runs; the table's advisors bicker in scripted dialogue when you visit.
6. Return, collect: Influence, items, unlocks, companion approval, sometimes a branch (see section 6). Influence fills Inquisition Rank; each rank grants perk points to spend on the table's perk screen [V3 .../Inquisition_perks rev 2026-06-02].
7. Story missions are themselves table operations (e.g. In Hushed Whispers: "Spend 15 Power to begin" [V3 .../In_Hushed_Whispers rev 2026-05-27]); starting one hands control to a mission, then back.
Automated: timers, outcome selection, resource refills for repeatable ops, report text.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Start a mission op | an advisor's time (about 12 min to 24 h) | 30 / 60 Influence or an item; unlocks follow-ups [v2 for the 30/60] | CONSTANT |
| Scout a region | Power: 1 (Hinterlands), 4 (Storm Coast), up to about 20 [V3 scout pages; v2] | unlocks the region and its resource ops | frequent early |
| Pick the advisor | different time and, on some ops, different odds | The Chantry Remains: 48 / 60 / 60 min; better outcome 75% Josephine, 50% Leliana, 25% Cullen [V3 .../The_Chantry_Remains rev 2025-08-29] | every op |
| Repeatable "Gather" / region resource ops | time | herbs, cloth, leather, metals, coin [V3 .../War_table_(repeatable)] | frequent mid-game |
| Story-gate op | 15+ Power; excludes the other branch | moves the main plot; mages vs templars | rare, big |
| Spend a perk | one perk point | 34 perks in four trees, 19 obtainable [V3 Inquisition_perks] | at rank-ups |
| Recruit agents (field decision) | dialogue choices | -5% time for one advisor each | occasional |
| Skyhold upgrade | resources; one of three branches | +1 Power; unlocks table ops; cosmetic variants | rare |
| Judge prisoners at the throne | none | consequences [M] | rare |
| Buy Influence from the merchant Farris | gold; needs Influence Level 6 | "she/he can simply buy it" [V3 .../Power_for_a_Price] | late |
#### 4. First hour, step by step
Source: the operation pages say the first op "serves as an introduction to the war table mechanic" [V3 Scout_the_Hinterlands].
1. Play the prologue and reach Haven; the table is in the war room.
2. Open "Scout the Hinterlands": Leliana only, Instant, Power cost 1 - it unlocks the Hinterlands. Click, watch the result.
3. Notice Josephine and Cullen are listed as Locked / N/A on this op; each op lists which advisors can take it.
4. Scout the Storm Coast (4 Power) when you have the Power; "Rescue Soldiers Missing in Ferelden" is a third Haven scouting op [V3 War_table_(Haven)].
5. After Val Royeaux, start The Chantry Remains: Josephine 48 min, 75% for the better branch; both branches pay 30 Influence.
6. Go play: explore the Hinterlands, set camps, close rifts (Power sources [S3 Prima]).
7. Return: collect rewards, check the rank-up, spend the perk point.
8. Finish the Haven-only operations before committing to the story op [V3 In_Hushed_Whispers: "Make sure that all of the Haven-only war table missions... are done"].
9. Choose mages (In Hushed Whispers, 15 Power) or templars (Champions of the Just): "Choosing the mages will make it impossible to work with the templars".
10. After In Your Heart Shall Burn the court moves to Skyhold; operations in progress carry over; some Haven ops cannot be finished after the move (The Chantry Remains: "cannot be completed after relocating to Skyhold"), though most carry over.
11. At Skyhold the table has regional trees (Ferelden, Orlais...) and the repeatable resource/Gather ops.
#### 5. What changes later
Skyhold adds hundreds of operations (about 310 operation rows across the wiki's Haven, Skyhold, repeatable and DLC lists - a transclusion count, duplicates possible [V3 War_table subpages]; developer pre-release "over 300" [v2]). Scouting unlocks each region's camps and its resource ops; Power costs climb (Western Approach 8, Emprise du Lion 20 [v2]). Perks are bounded (19 obtainable) but stack with agents. DLC adds ops (Jaws of Hakkon, The Descent, Trespasser's "Attend the Exalted Council") and an "Expedition table" [V3 .../War_table_(DLC)]. Pressure: finite Power gates the story pace; real-time hours become the scarce resource.
#### 6. Failure and ending
No operation can lose you the game. "Failure" is a branch: The Chantry Remains yields 30 Influence either way but unlocks The University of Orlais (Cassandra approves) or Grand Cleric Iona (Cassandra slightly disapproves); the better branch is "random" with the odds above; Cassandra's reaction reveals which happened [V3 The_Chantry_Remains]. Real losses are missed ops (Haven-only, 14 cut or bugged ops listed [V3 War_table page]) and irreversible picks. Ending: authored main plot with Trespasser epilogue; no run-level fail state beyond party defeat [M].
#### 7. Consequential vs cosmetic choices
- Consequential: mages vs templars; Divine candidates; Skyhold upgrades (irreversible, +1 Power) [V3 Major_Upgrades].
- Consequential: advisor choice on ops with odds (75/50/25). Evidence: the page's numbers; how many ops have odds `?`.
- Mostly cosmetic: which advisor on ops with identical rewards; the preferred-advisor speed-up "doesn't always lead to an ideal result" [V3 War_table page]; advisors' table banter.
- Dominant habit (my inference, not sourced): start the longest op before quitting, since timers run offline.
#### 8. Open items
- v2 [CONTESTED] "operations can fail": narrowed - at least one op has a random better/worse branch with advisor-dependent odds (75/50/25) [V3 The_Chantry_Remains]; the failure is not a loss. Count of ops with odds `?`.
- v2 [CONTESTED] Power spent vs threshold: the fan wiki says "Spend 15 Power to begin" and "Costs 4 Power to complete" and lists Power as a reward (+1 Power from the garden upgrade) [V3]; the developer said "spend" pre-release [v2]; Wikipedia says "required" [v2]. Leaning spent; on-screen drop never observed `?`.
- v2 "~20 perks per playthrough": the fan wiki says 34 perks, maximum 19 obtainable not counting agents [V3 Inquisition_perks]. v2 operation times (48 / 60 min) confirmed [V3 The_Chantry_Remains]. v2 `[S2]` "In Hushed Whispers 15 Power" is now [V3]; "What Pride Had Wrought 40" not re-opened.
- Not established: whether each advisor runs one op at a time (v2 [v2] fextralife), exact Rank thresholds (v2), Normal-difficulty names.

### Democracy 4 - facts line
Positech Games (UK; Cliff Harris and Jeff Sheen); policy simulation, Windows only [V3 positech.co.uk/democracy4/; en.wikipedia.org/wiki/Democracy_(video_game) raw]. Early access 2020-10-06, full release 2022-01-13 [V3 Wikipedia raw; Steam appdetails 1410710 says Jan 13, 2022]. DLC: Voting Systems (2022-05-31), Country Pack (2022-10-10), Event Pack (2023-03-27) [V3 Steam appdetails of each]. Newest build seen: 1.67 (2025-05-22) [V3 Steam news app 1410710]. Rules text below mixes the in-game-manual mirror (dated 2020-10-02 per v2; the page summary I fetched shows no date) [V3 gameplay.tips/guides/8590-democracy-4.html] with 2021-2022 patch notes; where they differ I say so. Assumed: base game, a default country and party, default difficulty. A session: terms are long (a turn is three months [V3 mirror]); minutes per turn and default term count `?`.
#### 1. Setup choices
- Country: base game by release notes UK, USA, Germany, then Spain (Jan 2021), South Korea (Feb 2021), Italy (Apr 2021), Japan (Jun 2021), plus Canada, Australia, France [V3 Wikipedia raw; Steam news]. Country Pack adds Greece, Ireland, Switzerland, Poland, Turkey, Brazil [V3 appdetails 2137220]. Each map carries a difficulty star rating [V3 Steam news 1.49, 2022-03-14].
- Party / system: two- and three-party systems, coalitions [V3 positech.co.uk/democracy4/; appdetails 1410710]. Which party you lead is chosen at start [M].
- Difficulty slider: it changes how often assassination attempts occur, how likely they succeed, the true success chance of a media-spin event, and the chance a minister resigns [V3 Steam news 1.35, 2021-08-13].
- Customise game: override term length and number of terms or play endlessly; set voter apathy [V3 mirror]. Voting Systems DLC: choose one metric as your campaign focus (economy, crime...) and an honest or cynical campaign tone; change electoral system between first-past-the-post and proportional [V3 appdetails 2004030].
- After one finished game: option to pick a new cabinet free on turn 1 [V3 Steam news 1.49].
#### 2. The loop
Clock: turns of three months; a quarterly report; fixed terms - "You cannot call a sudden election" [V3 mirror].
1. Read the board: policies grouped by department zone; situations (ongoing events, red or green), simulation values, 20 voter groups plus "everyone", polls, finances [V3 mirror].
2. Spend political capital to introduce, cancel, raise or lower policies; sliders have a transparent "ghost" showing the target, the live slider drifts toward it [V3 mirror; policy data: separate Introduce, Cancel, Raise, Lower capital costs [V3 positech.co.uk/democracy4/mod_policies.html]]. You cannot cancel a policy the turn you introduced it [V3 Steam news 1.35].
3. Resolve anything that blocks the turn: dilemmas ("You are not able to proceed to the next turn until outstanding dilemmas have been dealt with" [V3 mirror]); donors and ministers present specific demands for support [V3 positech.co.uk/democracy4/].
4. End turn. The game: moves each policy toward its target over its Implementation turns (minister competence adjusts it [V3 mod_policies]); averages effects over "inertia"; bills per-turn costs and credits income (MinCost to MaxCost by slider level [V3 mod_policies]); updates voter happiness; may start or stop situations; rolls events and media reports; ministers generate capital from loyalty [V3 mirror]; terror and assassination hazards run.
5. Interrupts: dilemmas, events with media-spin responses (a true success chance, capped at 99% even under censorship [V3 Steam news 1.42]), minister resignations, crises (emergency powers raise capital in a crisis [V3 positech.co.uk/democracy4/]).
6. At the end of a term: election. Turnout and vote follow voter-group happiness and mood; a coalition forms with the next-largest party if no majority, which lowers political capital [V3 mirror]. Win and go on; lose, or get assassinated, and the run ends.
Automated: the entire simulation (thousands of virtual voters [V3 Steam text]), cost accrual, inertia, ministers' work.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Move a policy slider | political capital (Raise/Lower), money per turn, implementation turns | shifts voter groups and statistics with delay | CONSTANT |
| Introduce / cancel a policy | capital (Introduce / Cancel); conflicting "opposite" policies cancel automatically [V3 mod_policies] | big change; cancelling a recent policy is blocked | frequent |
| Tax and spend sliders | capital plus popularity | income vs. deficit | frequent |
| Resolve a dilemma | none shown; outcomes shown after choosing (3 or more choices) [V3 positech.co.uk] | immediate and lingering effects | when forced |
| Accept / reject donor or minister demand | support lost if refused | adds a policy you did not plan | occasional |
| Appoint, fire or reshuffle ministers | firing is permanent; a reshuffle avoids the "bad PR of mass firings" [V3 mirror] | capital supply, implementation speed | occasional |
| Respond to a media-spin event | risk | public mood | when it appears |
| Declare emergency powers | liberty/civil costs [M] | extra capital during a crisis | rare |
| Read polls, focus group, Intel (terror) screens | free | informs every other choice [V3 FAQ: "watch terrorist groups on the Intel screen"] | CONSTANT |
| Campaign focus and tone (DLC) | trust risk for a cynical tone | election swing | before elections |
| Nationalise / privatise | credited as a percent of GDP [V3 mod_policies] | one-off funds vs. control | rare |
#### 4. First hour, step by step
Source: the in-game manual mirror [V3 gameplay.tips 8590], and one community opening for the USA, dated 2022-01-05, which is opinion not manual [V3 gameplay.tips/guides/democracy-4-first-10-turns-guide-america.html]. An in-game tutorial exists (patch note "Tutorial fixes", 2022-03-18 [V3 Steam news]); its contents `?`.
1. New game: pick a country and party; leave difficulty and term length at defaults for run one.
2. On turn 1 find the red situations (e.g. Prison Overcrowding, Antisocial Behavior, Alcohol Abuse in the US opening) - they show inputs; hover over a policy to see green (good) and red (bad) effect lines [v2].
3. Open the finance screen: income vs. cost; fix the deficit slowly.
4. Pick a few policies with long lead times first (the guide: Community Policing, Police Force, Private Prisons to Max on turn 1, keep the remaining capital for turn 2).
5. Turn 2: set Military Spending to Min for budget room; set Health Food Subsidies to Max; do not raise income or corporate tax yet (tax evasion and popularity).
6. Turn 3 on: Junk Food Tax (about $5B), Competition Law, Reforestation; avoid maxing the State Health Service ("21 political points and about $270B").
7. Check the polls each turn; note which voter groups are in your coalition and which dislike you; remember voters join a group only when more than 50% invested in an issue.
8. Resolve dilemmas as they appear; read the media report; check ministers' sympathy groups.
9. Do not make appeal-to-voter changes just before the election: cynicism "is caused by making policy changes that appeal to voters just before an election" [V3 mirror].
10. Go on to the election; read the results and polling by group.
FAQ warning: players "get assassinated" when they change the country "super-radically overnight"; invest in security and make slow, subtle changes [V3 positech.co.uk/democracy4/faq.html].
#### 5. What changes later
More situations trigger; prerequisites open new policies (PreReqs [V3 mod_policies]); coalition and donor demands appear; cynicism and complacency tracked per group build up; complacency grows when a group is "massively happy" and the cap rises per term [V3 mirror; blog 2022-02-24]. What eases: Cliff's data show win rates by term T1 54%, T2 76-79%, T3+ 83-84% and an average vote share of 74% against an intended 52-58% [V3 positech.co.uk/cliffsblog/2022/01/09, v1.45/1.46]; "things are too easy in the late game (3 terms on...)" [V3 blog 2022-02-24]. Pressure: the Steam text lists modern policies (quantitative easing, helicopter money, universal basic income...) [V3 appdetails 1410710]; which ones unlock only after situations or technology: `?` (PreReqs exist as a data column [V3 mod_policies]).
#### 6. Failure and ending
Two ways to lose: not re-elected, or assassinated [V3 mirror]. The store text: "Losing an election is just the end-game (unless you get assassinated); the real challenge... is whether you can create a country you are honestly proud of" [V3 appdetails 1410710]. Win: survive the set number of terms or play endless. Recovery: none; a hidden variable "Winning" shifts difficulty with your record [V3 blog 2022-01-09]; no save-scumming limit is stated `?`. A new run keeps the "free cabinet" option [V3 1.49].
#### 7. Consequential vs cosmetic choices
- Consequential: which voter groups you please - the vote follows group happiness; the mirror warns a group can be happy and still vote against you because of other group memberships [V3 mirror].
- Consequential: capital timing (introduce early; cynicism for pre-election giveaways) and speed of change (assassination risk).
- Partly overridden: Cliff tunes a hidden difficulty variable and logs average vote share above his intent [V3 blog 2022-01-09, v1.45-1.46]; my inference: when most terms end in a win, the margin between policy mixes is smaller than the game's presentation suggests.
- Possibly dominant, community-sourced: front-load long-lead-time policies and max low-cost ones (the US opening above); one author, US only; the Country Pack text says "each country has its own challenges" [V3 appdetails 2137220], so do not generalise.
#### 8. Open items
- v2 "full release 2021" is wrong: full release 2022-01-13 [V3 Wikipedia raw; Steam].
- v2 "assassination/terror is a chance hazard": add that media-spin success, assassination odds and minister resignation are chance events scaled by the difficulty slider (1.35) [V3 Steam news].
- Political capital absolute values: `?` (mod page has columns only). Default number of terms and terms-per-election length: `?`. Which party you may lead: [M].
- No attachment claims for Democracy 4 or Dragon Age: Inquisition: grep of the four uploads finds Democracy only in a genre table row (62dd3fd3-emergent-narrative-mechanics.md:553 lists "Victoria, Democracy") and no Dragon Age mention.
