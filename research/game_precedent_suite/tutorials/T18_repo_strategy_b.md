# T18 (v3) - Tutorials: Shadow Empire, Stellaris, XCOM (EU + XCOM 2), Brigandine (Runersia)

Tags: [V3 url date/version] read in a fetched body this session (2026-10-22); [S3 url] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED] sources disagree.
No v2 capability tables exist for these four games; capability-id lines (B, D, F, H, L only) are given per game and tagged. Sections appended game by game.

### Shadow Empire - facts line
Mostly [V3] from the official manual; the manual is v1.09 (2021) and the game is now far past it, so rules below are "as of the manual" unless a patch note says otherwise.
- Developer VR Designs (Victor Reijkersz, solo), publisher Slitherine/Matrix; PC, released 2020-06-04; "4X + computer wargame" [V3 en.wikipedia.org/wiki/Shadow_Empire raw, 2026-10-22].
- Manual: v1.09, 2021-04-28 [V3 matrixgames.com/amazon/PDF/SE/Shadow_Empire_manual_EBOOK.pdf]. Latest patch: 1.32.4, 2026-09-16; Republica DLC (9 political systems, Virtus, 200+ stratagems) 2026-04-09; morale/combat rework 1.30, 2026-03-11 [V3 Steam news API appid 1154840, fetched 2026-10-22].
- This tutorial assumes: base game, Low Tech, Normal development, Regular difficulty, Quick or Detailed generation, no DLC. One session: 1 turn = 2 earth months [V3 manual 5.16.2]; Moon/Planetoid classes are "quick and confrontational games" [V3 manual 3.1.1]; a full planet conquest is tens of hours [M].
#### 1. Setup choices
All before turn one [V3 manual 3.1]:
- Planet Class: Seth (desert, no liquid water), Boreas (icy desert), Siwa (Earth-like, limited water), Limos (some water, no life), Medusa (hostile alien biosphere), Cerberus (lava), Planetoid, Moon, or Unclassified (anything). Size runs ~200 hex circumference (Earth) / 100 (Mars) / 50 (Moon) [V3 manual 3.1.1]. [CONTESTED] fan wiki lists 10 classes incl. Hydra and Morgana "added in Patch 1.08.01" [V3 shadowempire.fandom.com api.php Planets page]; manual v1.09 lists only 8 + Unclassified.
- History Classes (optional flags, e.g. Survival Stress, Alien Lifeforms): leave blank for best procgen; flags force outcomes (Survival Stress = many Regimes, slow AI turns) [V3 manual 3.1.2].
- Generation Method: Immediate (skip everything), Quick (see result, re-roll whole), Detailed (re-roll each phase Planetology > Geology > Biosphere > Colonization > Dissolution War) [V3 3.1.3.1, 3.1.4-3.1.8].
- Fog of War: Complete / Complete after Colonization / Map known / Partial (see borders and comparative stats) [V3 3.1.3.2].
- Difficulty: Beginner/Regular/Hard/Extreme. Harder = stronger AI, more militarised Free Folk, slower Militia regrowth; Beginner gives +2 Fate Points, extra artillery and armor battalion, known nearby Metal/Water, 20% income tax; Hard/Extreme AI +10%/+20% combat and move [V3 3.1.3.3].
- Tech Level (Low default / Medium / High) and Development Speed (Normal / Slower x2 / Slowest x5 research time) [V3 3.1.3.4-5].
- History Choices: multiple-choice questions that nudge your starting Regime Profile (not in Quick Start); then name and flag (cosmetic) [V3 3.1.9-10]. Leaders, factions and government are rolled for you; there is no ruler-creation screen [V3 4.4.1].
#### 2. The loop
Clock: turns of 2 earth months, no real-time [V3 5.16.2]. Loop as printed in the manual [V3 3.2]:
1. AI Regimes take their turns (this is when non-aligned forces and rivals attack you; the manual's example shows a 2,400-troop stack hitting a battalion your recon said was 700).
2. "Start Turn" popup, then Vidcom messages (events and Decisions) in order; you may skip to the Map tab.
3. You make all moves: units, orders to Zones, construction, trades, stratagems, Decisions.
4. End Turn. Between turns the game automates: production and Private Economy (people build, save, invest, close assets without you), logistics network recomputed at start of turn, worker recruitment, taxes, Faction/Leader mood [V3 4.2.10, 4.3.8].
Interrupts: Decisions (event-based Decisions cost 1 PP if you make them yourself; if you press End Turn without deciding, your Secretary/Governor/Director decides, "usually the safest course", or one favouring their own profile if Relation is low and Authority high) [V3 5.6.3.3]; Faction Demands; elections every X rounds; unrest/rebel events. Control never leaves you except via those delegated Decisions.
#### 3. The choice menu
| verb | cost | effect | when picked |
|---|---|---|---|
| Move / attack hex (constant) | Action Points; a combat round costs 10 AP; ammo/fuel/food | odds popup shows attacker:defender strength, estimate only; result auto-resolved | every turn |
| Declare war (rare) | Prestige/Fist hit, bigger vs Majors and allies | opens Hexes and Cities of that Regime | when strong enough |
| Raise Formation (frequent early) | Recruits + Items + PP; recruited at 0 XP | Regular troops ~2.5x Militia; multi-unit Formation gets own OHQ | after first economy |
| Appoint Commander / play Posture (per formation) | PP to dismiss candidates; Posture is a stratagem | Commander skill rolls and Posture (e.g. +50% defence) add to combat | every new formation |
| Construct Public Asset (constant) | Metals etc.; "1,500 Metals" for Industry; pays Workers | production; taking several turns | economy build-up |
| Trade Order (frequent) | Credits; prices move with supply/demand | sell surplus, buy Metal/Machines | when short |
| Taxes, salaries via Secretary (periodic) | stifles Private Economy / happiness | Credits vs Worker, Leader, Soldier morale | tuning |
| National Budget (periodic) | BP split across Councils | speeds research, stratagems, tasks | every few turns |
| Create Council (rare) | PP | new Tasks (prospecting, posture cards, HR) | early, then as BP grows |
| Appoint/dismiss Leader (frequent) | small PP; Faction happiness if dismissing a member | Relation >50 gives bonus, <50 penalty | on nominations |
| Decisions (constant) | 1 PP self-made | shifts Regime Profile, Faction/Word effects | each Vidcom |
| Play Stratagem (frequent) | PP or Fate Points | Unit/Leader/Zone/Regime effects, e.g. Medal of Merit +25 Relation | when card fits |
| Zone Orders to Governor (periodic) | none | recruit more, worker policy, invest, emergency food | when zone stressed |
| Extend logistics (frequent mid-game) | build Truck/Train Station, Supply Base (+50 AP range) | units stay supplied | before advancing |
| Resign (rare) | one End Turn | becomes defeat [V3 5.15.2] | ending |
#### 4. First hour, step by step
Sources: manual chapter 4 and Gamepretty "Turn 1 Guide" (2020-12-03, no version) [V3 gamepretty.com/shadow-empire-turn-1-guide].
1. Choose planet class and options as above; accept defaults if unsure; Beginner difficulty gives nearby Metal and Water.
2. On turn 0, read the Start Turn popup and Vidcoms; open the Personnel Overview (REL, CAP, TR, CR, IPR per leader).
3. Confirm leaders fit jobs: Governor wants TR+IPR, Council Director TR, SHQ Commander CR [V3 4.4.1]. Attach your Advisor to the Director who plays diplomacy.
4. Check Factions: happiness over 60 yields Faction stratagems, under 60 yields problems [V3 4.4.3].
5. Open the Decision tab; use the Ascension Speech and set up the first council; Gamepretty suggests Economic Council first for Prospecting (guide's advice).
6. Look at your 4 Militia battalions + 1 regiment + SHQ; keep them within HQ power range [V3 4.2.1]; scout roads; find Free Folk settlements.
7. Claim ~2 hexes around your City to remove Danger Points from nearby non-aligned units [V3 4.2.2].
8. Do not attack with Militia unless massed from several sides (+40% for three-side attack in the example); expect "iffy" 2.2:1 [V3 4.2.2].
9. Raise Regular troops (infantry plus a Buggy battalion) as soon as Recruits allow; ask your Governor for more Recruits.
10. Next turn pick a Commander from the shortlist; play a Posture stratagem on the OHQ.
11. Call the Secretary to set salaries (a few micro-Credits per round raises morale).
12. Check SHQ Items: Food each round, Fuel when moving, Ammo when attacking; Workshop Order makes Ammo/Machinery.
13. Build Public Assets: Industry needs lots of Metal; sell excess and buy Metal from Traders [V3 4.3.5].
14. Watch the Logistics layers; extend the network with a Supply Base where Logistical Points are still strong.
15. Check Governor Relation (>50 gives up to +25% Public production); raise it with salary or a Medal of Merit.
16. Press End Turn and read the AI's response.
#### 5. What changes later
- Techs and Models: discover then research at Councils with BP; Model Design Council gives Light Tank, Artillery; Staff Council gives Formation Types and Postures [V3 4.2.5, 5.6.4].
- Growth costs: every extra SHQ costs PP per turn (-2, -5, -9, -14, -20 for 2..6) [V3 5.6.2.3]; bureaucracy grows inefficient (+100 BP bonus at 100 BP; -190 at 2,000 BP) [V3 5.6.2.5].
- Logistics becomes the game: 100 Logistical Points per Asset Level needed on the road to the City for a Public Asset [V3 4.3.13].
- Politics: Parliament/Senate/Politburo elections shuffle Faction power; Majority Factions issue Demands; Regime Profile (9 scores: Democracy/Autocracy/Meritocracy, Enforcement/Commerce/Government, Fist/Mind/Heart) unlocks Regime Feats above 40 [V3 5.6.9-12]. Republica DLC replaces this with 9 political systems and Virtus decay [V3 Steam news 2025-04-28, 2026-04-15].
- Rebels (Unrest > Rebel Manpower > units), leader rebellion, aging leaders losing stats [V3 5.3.17, 4.4.8]. Air forces chapter 6.1.
#### 6. Failure and ending
Win: Victory Score > 50 and at least 25 ahead of the nearest rival; score mixes % planetary Populace and % land Hexes [V3 5.15]. Loss: resignation becomes a defeat next turn [V3 5.15.2]; losing the Capital moves it to another Zone and decimates the Cabinet [V3 5.6.2.9]; explicit elimination text not read, `?`. Recovery from a lost war is possible via Rebel/AI dynamics but not documented [M].
#### 7. Consequential vs cosmetic choices
- Consequential: planet class and History flags (drive resources; "primary source of replayability" per a review [S3 turnbasedlovers.com/review/shadow-empire]); logistics reach (in-manual: units too far from pickup get 2 of 4 Fuel [V3 4.2.10]).
- Consequential: who holds which job (Relation moves production up to +-25%, skill rolls +-10..20 [V3 4.4.5]) and which Faction you keep happy.
- Dominant answer: Regular troops over Militia ("about 2.5 times better" [V3 4.2.3]); keep one SHQ (PP penalty) [V3 5.6.2.3]; Economic Council first is community advice [V3 gamepretty].
- Cosmetic: name, flag; History Choices only orient the start "somewhat" [V3 3.1.9]; Fog-of-war setting is informational.
#### 8. Open items
No v2 table, so no cell corrections. Not established: elimination rule; exact Republica turn-by-turn play; whether 1.09 numbers (PP income 5-10, BP table) survive to 1.32 (the 1.30 notes show morale was reworked); play-time figure [M].
**Capability ids (tagged):** B1-B6 YES [V3 manual 4.4, 5.6.3: roster, nominations, Director/Governor/Commander/Advisor, Relation, Secretary acts if you do not]; B7 NO? [M]. D1 YES (Decisions/Profile) D2 YES (taxes, salaries, National Budget) D3 YES (Cabinet/Councils) D4 YES (Unrest, Popularity, Prestige) D5 YES (elections) D6 ? [V3 4.3.7, 5.6.12]. F1 YES F2 YES F3 PART (Postures, no deployment screen) F4 YES (turn-based hex) F5 PART (odds popup then auto-resolved round) F6 ? F7 YES (Logistical Points, Food/Fuel/Ammo) F8 YES (morale, retreat <50% troops) [V3 4.1-4.5, 4.2.2]. H1 PART H2 YES (Relation per Regime/Leader) H3 YES (Secret Service stratagems, Assassinate Leader, election support) H4 YES (pacts) H5 ? H6 YES (declare war) [V3 4.4.7, 5.6.12.2, 4.1.3]. L1 YES (ratings, likes/dislikes) L2 PART (XP growth, aging, retirement) L3 NO? L4 PART (Vidcom events) L5 YES (AI Regimes, Private Economy, Rebels) [V3 4.4, 4.3.8, 5.3.17].

### Stellaris - facts line
Mixed sources: current-patch facts from Paradox's Steam news (dev diaries, patch notes); stable rules from the fandom wiki, whose pages are version-tagged 3.10 (edited 2024) and so pre-date 4.0. Older mechanics are marked.
- Paradox Development Studio / Paradox Interactive; real-time-with-pause 4X grand strategy; released 2016-05-09 [V3 en.wikipedia.org/wiki/Stellaris_(video_game) raw].
- Version relied on: 4.5.2 "Cygnus", 2026-10-06; next expansion Willpower (4.6) due 2026-11-23 [V3 Steam news API appid 281990, fetched 2026-10-22]. 4.0 "Phoenix" (2025-05-05) replaced Pops with Pop Groups + Workforce, removed Trade Routes, added Zones, Empire Focus tasks and an Empire Timeline [V3 Dev Diaries #366, #370, #371 and 4.0 post, Steam news].
- Assumes: a regular (non-gestalt) empire, default galaxy, base game plus whatever DLC you own. One session: no source; the game is long (a run to the default end year is many sessions) [M].
#### 1. Setup choices
Before day one [V3 fandom Ethics/Government/Origin pages, v3.10 tag; Steam DD#367]:
- Premade empire or custom. Guides tell new players to use a premade one (e.g. United Nations of Earth) [V3 gamerempire.net/stellaris-beginners-guide, mod. 2023-12-14].
- Species: portrait/traits (budgeted picks); homeworld type; ship set; flag (cosmetic).
- Ethics: 3 points; moderate costs 1, fanatic 2; so 3 moderate or 1 fanatic + 1 moderate; or Gestalt Consciousness (costs 3). Axes: Authoritarian-Egalitarian, Materialist-Spiritualist, Militarist-Pacifist, Xenophile-Xenophobe [V3 fandom Ethics].
- Authority: Democratic, Oligarchic, Dictatorial, Imperial, Corporate, Hive Mind, Machine Intelligence. It sets ruler term (Democratic: 10 years), election, empire-size effects [V3 fandom Government].
- Civics (extra traits of government) and Origin (backstory). 35 playable origins in the wiki list (v3.10 tag; newer ones such as Hard Reset in 4.0 and Willpower's Golden Generation, Lost Makers, Great Mosaic are not in it) [V3 Steam DD#368, DD#435], e.g. Prosperous Unification (+4 Pops, +2 districts, +15% happiness for 20 years), Void Dwellers, Lost Colony, Hegemon, Clone Army [V3 fandom Origin, edited 2025-09-21].
- Galaxy setup: size, AI empire count, habitable-world and pre-FTL sliders, crisis, victory year, Precursor selection (new in 4.0) [V3 DD#367].
- Difficulty and AI aggression [M].
#### 2. The loop
Clock: real time with pause; the economy ticks monthly [V3 DD#366 "calculations ... every month"]. Speed 1-5 and pause [M].
1. Unpause. Days pass; fleets and ships move without further orders once given.
2. Each month the game adds resources: planets produce, jobs are filled by Workforce, upkeep and trade/logistics deficits are charged, Unity and Influence accrue, pops grow [V3 DD#370, #369].
3. You queue things: research (three fields offer cards), construction, colonisation, fleets, policies, diplomacy.
4. Automated: science-ship exploring/surveying, construction-ship builds, colony/planet automation, AI empires' diplomacy and war [V3 DD#295, DD#366].
5. Interrupts: events and anomalies (4.0 turned purely informational ones into toasts and made popups chooseable; Message Settings let a message pause the game) [V3 DD#366-368]; first contact; diplomatic proposals; leader level-ups; ruler elections; war declarations; galactic crises [V3 Wikipedia].
6. The player resumes; there is no turn end. Time stops only when you pause.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Survey/explore systems (constant early) | science ship time | finds planets, anomalies, hyperlanes | first 20 years |
| Queue research (constant) | Research output; cards cost more as Empire Size grows | tech with random card draw | every few months |
| Build stations/outposts, claim systems (frequent) | Alloys, Influence | borders and resource access | expansion |
| Colonise a planet (frequent early) | colony ship | new population centre; choose designation and automation at order (4.0) [V3 DD#366] | year 5-30 |
| Planet management: districts, zones, buildings, job priority (constant) | Minerals, Alloys, Energy | what the planet produces | every new world |
| Traditions / Ascension perks (periodic) | Unity; tradition cost rises with count and Empire Size [V3 fandom Traditions] | permanent bonuses | when Unity allows |
| Policies (periodic) | free, but locked 10 years after change [V3 fandom Policies] | stances on war, trade, migration etc | at factions or crises |
| Edicts (periodic) | resource cost plus upkeep, +1% per Empire Size point [V3 fandom Edicts] | timed empire modifiers | opportunistic |
| Leaders: recruit, council seats, planet/sector governor, ships (frequent) | resources; leader caps per class | traits and level scale bonuses [V3 DD#316] | whenever a slot opens |
| Create sector, set capital/governor (mid-game) | none found; sector spans contiguous systems within 4 hyperlanes of its capital [V3 fandom Empire] | delegates planets | when too many colonies |
| Embrace/suppress faction (rare) | ethic shift once per 10 years [V3 fandom Ethics] | approval, Unity, ethics drift | when approval is bad |
| Diplomacy: envoys, pacts, federation, Galactic Community (periodic) | Influence, envoys | trade/research pacts, subjects | contact onward |
| Design ships, build fleets (frequent mid) | Alloys, naval capacity | power in war | before war |
| Declare war with casus belli and wargoals (rare) | needs a casus belli; war exhaustion; claims cost Influence | conquest, status-quo peace [V3 fandom Warfare] | when ready |
| Invade/bombard (in war) | armies, fleets | occupy planets | war |
| Special projects, archaeology, anomaly choices (frequent) | science ships, time | rewards, chains | exploration |
#### 4. First hour, step by step
Basis: gamerempire guide (mod. 2023-12-14, pre-4.0) + 4.0 dev diaries; the guide says nothing on policies, sectors or governors [V3 gamerempire].
1. Pause. Learn the top bar (economy), outliner (right), navigation (left). Use the galaxy map (M).
2. Set one research project per field; prefer speed or production boosts.
3. Send the science ship to a neighbouring system with Survey; queue more with Shift.
4. Order the construction ship to build a mining station and a research station in the home system, early; research first.
5. Keep every economic resource positive; fix deficits with buildings.
6. Open the Situation Log; pick an Empire Focus (Conquest, Exploration or Development) and note the offered tasks; completing them guarantees key research options [V3 DD#368].
7. Pick a first tradition tree (the guide says Discovery).
8. When Influence allows, claim nearby systems with stations/outposts to extend borders.
9. Send a colony ship to a planet near 80% habitability (the guide says about three nearby). In 4.0 you start with many civilians, enough to settle several worlds [V3 4.0 post].
10. Respond to event choices: since 4.0 they are meant to guide your empire's growth [V3 DD#366].
11. Send envoys to neighbours to open communication and learn standing; avoid war early; build corvettes and fight inside your borders if attacked [V3 gamerempire].
12. After about 10 years with a second species or contact, factions form; check approval (above 60% gives bonuses, below 20% costs 40% happiness) [V3 fandom Factions].
13. Spend Unity on traditions and then ascension perks; use policies/edicts to appease factions.
14. Around year 20 diplomacy dominates: the Galactic Community votes on galactic law; strengthen fleets; use chokepoints [V3 gamerempire].
#### 5. What changes later
- Mid game: sectors and governors absorb colony micromanagement; Empire Size raises tech, tradition and edict costs above 100 [V3 fandom Empire]. Governors apply full strength to their own planet and half to other planets of the sector if they govern the sector capital; a planet governor overrides [V3 DD#322, Steam news 2023-11-10].
- Federations, subjects/vassals, Galactic Community law; first-contact and fallen empires [V3 fandom Diplomacy; Wikipedia].
- Ascension paths and megastructures [V3 Wikipedia]; 4.0 trade acts as a logistics resource: planetary deficits and moving fleets pay trade upkeep, a trade deficit lowers advanced output and ship damage [V3 DD#369].
- Late game: Galactic crises (mid and late) force war footing [V3 Wikipedia]; victory score is tallied at the configured Victory Year [V3 fandom Empire].
#### 6. Failure and ending
No scripted ending: highest Victory Score when the configured Victory Year arrives is "declared winner", but play continues and the victory is "of little concern" [V3 fandom Empire, v3.10]. Loss is gradual: conquest, annexation, rebellion, or a crisis; recoverable until the last planet falls. Exact elimination rules not read, `?`. Crisis victory paths exist for players [V3 Wikipedia].
#### 7. Consequential vs cosmetic choices
- Consequential: Ethics + Authority + Origin; they gate civics, policies, events and AI reactions ("ethics choices have a greater impact ... than the bonuses listed") [V3 fandom Ethics]. Community tier lists for origins and traditions exist (file names on wiki pages) [V3 fandom Origin].
- Consequential: which planets run which Zones/specialisations, and which leader governs a sector (class-specific governance effects) [V3 DD#322].
- Mostly flavour: flag, portrait, ship set, names; many informational events were deliberately demoted to toasts in 4.0 because they had no choice [V3 DD#366].
- Dominant answer (community): premade empires and "Discovery" first for beginners [V3 gamerempire]; this is one guide's opinion, not consensus.
#### 8. Open items
No v2 table. Repo claim [emergent-narrative attachment `62dd3fd3`, line 620]: "Stellaris | Sector governors with traits and autonomous build orders | The incompetent viceroy". Verdict PARTLY: governors have class, level and traits that scale bonuses, and 4.3 patch notes still fix sector-governor trait propagation [V3 Steam news 2026-03-11]; a wiki says a Sector Focus makes a sector "develop itself automatically" (v3.10 tag, rev 2024-07-29) [V3 fandom Empire]; 4.x status of that auto-build: `?`. I found no mechanism that makes a governor incompetent in a story way: negative traits are modifiers (max 4 negative) [V3 fandom Leader]; the "incompetent viceroy" is a player-read narrative, not a game event. Colony/planet automation exists [V3 DD#366]. Also "Stellaris" in `REPO_MENTIONS` s3 is a label, not a studied mechanic.
**Capability ids (tagged):** B1-B4 YES [V3 DD#316/#322, fandom Leader]; B5 PART (sector governor, automation) [V3]; B6 YES (faction approval, happiness) [V3 fandom Factions]; B7 PART (ruler term/election by authority) [V3 fandom Government]. D1 YES (policies/edicts) D2 PART (no tax rate; policies and market) D3 YES (council) D4 YES (stability, approval) D5 YES (elections, Galactic Community) D6 `?` [V3 fandom Policies/Government]. F1 YES F2 YES F3 PART F4 PART (fleet orders; battles resolve automatically) [M] F5 NO [M] F6 YES (bombardment/ground armies) [V3 DD#295] F7 PART (naval capacity, trade upkeep) [V3 DD#369] F8 `?`. H1 PART H2 YES H3 PART (espionage/infiltration) H4 YES H5 YES (subjects, subjugation terms) H6 YES [V3 fandom Diplomacy/Warfare/Policies]. L1 PART (leader traits and ethics) L2 PART (leader aging) L3 NO [M] L4 YES (events/anomalies) L5 YES (AI empires, crises) [V3 DD#366/Wikipedia].

### XCOM (XCOM 2 [primary] and XCOM: Enemy Unknown) - facts line
Two entries, taught together: XCOM 2 (2016, with War of the Chosen 2017) for the loop; XCOM: Enemy Unknown (2012) where it differs. Stable, effectively frozen games; most mechanics come from fan wikis (fandom, Ufopaedia) = community reference, plus the shipped-script text for the aim-assist check.
- Developer Firaxis Games, publisher 2K. Enemy Unknown released Oct 2012 (Windows/PS3/X360), Enemy Within expansion Nov 2013 [V3 en.wikipedia.org XCOM:_Enemy_Unknown raw]. XCOM 2 released 2016-02-05 (PC); War of the Chosen (WotC) 2017-08-29 [V3 Wikipedia XCOM_2 raw; xcom.fandom.com WotC page].
- Version: the XCOM 2 patch list on the fandom wiki ends at the "Fall 2017 update" for WotC; EU's ends at a 2014 iOS update [V3 xcom.fandom.com Patches & Updates pages, rev 2024-06-24 / 2017-01-23]. The community Highlander mod on GitHub is the live code base for modders (its master was fetched 2026-10-22).
- Assumed: XCOM 2 + WotC on Veteran, Ironman off; EU on Normal. One mission is roughly 20-45 minutes and a campaign 30+ hours [M]; Legend "almost twice as long" [V3 fandom Game difficulty (XCOM 2)].
#### 1. Setup choices
- XCOM 2 difficulty: Rookie, Veteran, Commander, Legend. Changeable mid-game. Rookie/Veteran cap simultaneous attackers at 5, give easier mission variants and hidden aim help; Legend removes all aim help, all easier variants, disables the tutorial and makes the strategy layer "almost twice as long" [V3 fandom Game difficulty (XCOM 2), rev 2024-07-16].
- Ironman (one auto-save, no reloads); in EU also Second Wave toggles (Damage Roulette, Not Created Equally, Hidden Potential, Red Fog, Marathon ...), some unlocked by finishing a difficulty [V3 fandom Second Wave].
- EU difficulty: Easy, Normal, Classic, Impossible; the starting continent changes starting funds (Normal: North America 375, South America 245, Europe 265, Africa 347, Asia 265) [V3 ufopaedia.org Difficulty_(EU2012)].
- Soldier look/names (character pool) are cosmetic [V3 fandom patch notes]. There is no ruler or faction choice: you are the Commander.
#### 2. The loop
Clock: real-time strategic layer you advance by scanning/waiting, interrupted by turn-based missions [V3 fandom Geoscape (XCOM 2); ufopaedia Mission Control (EU2012)].
1. Geoscape: move the Avenger (XCOM 2) or watch the Hologlobe (EU); "scan" to advance time; contacted regions pay a monthly supply drop; the Avatar Project meter (12 blocks, starts at 3) is the clock to defeat [V3 fandom Geoscape, Avatar Project].
2. The game offers missions and events: Guerrilla Ops, Council missions, Supply Raids, Alien Facility assaults, Retaliation strikes, key story missions [V3 fandom Missions (XCOM 2)]; EU offers abductions, UFO crash/landings, terror sites, Council missions [V3 ufopaedia Missions (EU2012)].
3. Between missions you spend: research (autopsies, techs), engineering/facilities, Intel to contact regions, equipment, promotions, covert actions (WotC).
4. Launch a mission: pick squad and loadout; turn-based combat, you move all soldiers then the enemy moves; soldiers use limited actions, take cover, overwatch, hack, heal [V3 Wikipedia XCOM_2]; most XCOM 2 missions start concealed and nearly all have a timer [V3 fandom Squad Tactics].
5. After action: loot/corpses collected, wounded soldiers recover at the infirmary, dead are lost, soldiers rank up; return to 1.
Interrupts: ADVENT Dark Events, Chosen ambushes (WotC), Avenger/base defence, EU panic and country defections [V3 fandom; ufopaedia Panic]. Automated: the monthly resource tick, infirmary healing, research/engineering timers, enemy pod patrols.
#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Scan / move Avenger / wait (constant) | days of game time | missions appear, Avatar meter creeps | each strategic turn |
| Pick a mission (frequent) | time; some expire; skipping a Guerrilla Op triggers all pending Dark Events [V3 fandom Missions] | rewards (Intel, Supplies, soldiers) | whenever offered |
| Choose squad and gear (every mission) | soldiers tire or get hurt | who risks death | before launch |
| Research (frequent) | scientists, time, sometimes resources | techs, autopsy bonuses | queue always full |
| Build Avenger facilities (periodic) | Supplies; engineers must clear debris [V3 Wikipedia XCOM_2] | production, comms, healing | when objectives say so |
| Contact a region (periodic) | Intel; Resistance Comms research first [V3 fandom Geoscape] | supply income, new sites | early and mid |
| Promote/skill soldiers (frequent) | none (XP) | class abilities | after missions |
| Covert Action (WotC, periodic) | soldier/engineer time; risks of ambush or capture [V3 fandom Covert Actions] | faction influence, promotions, resources | monthly |
| Resistance Orders (WotC, rare) | faction influence | passive empire bonuses | per influence level |
| Black market trades (rare) | Intel/Supplies | gear, items | when stocked |
| Tactical: move, shoot, overwatch, hunker, hack, throw, heal (constant) | actions, ammo, risk | kills, cover, objectives | every turn |
| Evacuate early (rare) | abandons loot; a free action [V3 fandom Squad Tactics] | saves soldiers | when overwhelmed |
| Skip or fail a Council mission (EU) | country panic up [V3 ufopaedia Panic] | defections if panic 5 | when stretched |
| Satellites / interceptors (EU, frequent) | funds | panic control, UFO shoot-downs | early EU |
#### 4. First hour, step by step
Basis: fandom XCOM 2 pages (above) and the Wikipedia article; no official manual read. Steps 1-8 XCOM 2, 9-10 EU.
1. Pick Veteran for a first run; leave the tutorial enabled (Legend disables it). The first mission is Operation Gatecrasher [V3 fandom Game difficulty].
2. Play it concealed: scout, position overwatch ambushes, keep actions in reserve, do not hack everything [V3 fandom Squad Tactics].
3. On the Avenger, look for objectives marked with a star in a hexagon and do those first [V3 fandom XCOM 2 campaign].
4. Queue research; unlock Resistance Communications and spend Intel to contact adjacent regions [V3 fandom Geoscape].
5. Scan and take missions; Council missions require extracting the VIP and all soldiers within 12 turns [V3 fandom Missions].
6. Watch the Avatar Project meter and Dark Events; Guerrilla Ops counter Dark Events but only one can be done at a time [V3 fandom Missions, Avatar Project].
7. After each mission, promote soldiers, review the wounded, and queue autopsies for new alien types.
8. Build Avenger facilities as Supplies and engineers allow; with WotC, handle Covert Actions and meet the Chosen later.
9. EU: finish the tutorial, then choose where to build the base (it sets funding); deploy satellites and interceptors; pick which country's abduction to answer and expect the other panic to rise [V3 ufopaedia Panic/Alien Abductions].
10. EU: end each month at the Council funding report; keep every country's panic under 5.
#### 5. What changes later
- XCOM 2: harder enemy types, Chosen who capture and interrogate soldiers, The Lost, faction heroes (Reapers, Skirmishers, Templars), soldier bonds, SITREPs [V3 fandom WotC]; Avatar doom countdown starts at 12 blocks (24 days Rookie ... 15 Commander) [V3 fandom Avatar Project, one value flagged "needs verification"].
- Alien Facilities add Avatar progress until raided; story missions reduce it [V3 fandom Avatar Project].
- EU: Enemy Within adds EXALT and Meld; psionics; Council missions turn into "training runs" in late game [V3 ufopaedia Missions].
#### 6. Failure and ending
XCOM 2: loss when the Avatar Project completes after the doom countdown ("permanently destroyed") [V3 fandom Avatar Project]; wipe-out of a mission squad is mission failure, recoverable via the campaign. Win by completing the story missions leading to the final assault (details beyond scope). EU: loss when 8 of 16 Council countries leave, or a failed storyline mission [V3 ufopaedia Panic; Missions]. Soldiers die permanently.
#### 7. Consequential vs cosmetic choices
- Consequential: which soldiers to risk and how you flank/cover; when to skip missions (Dark Events, panic). Hit-chance perception matters because of hidden help below.
- **Hidden aim assist (VERIFIED, with corrections).** The displayed percentage is not what the dice use on lower difficulties.
  - XCOM 2 script: `X2AbilityToHitCalc_StandardAim` has "Aim Assist": after a miss for XCOM, it recomputes a modified chance and can flip the result ("AIM ASSIST forcing an XCom MISS to become a HIT!"); aliens' hits can be flipped to misses; reaction fire and guaranteed hits are exempt; modified chance = base x difficulty multiplier + miss-streak x adjustment + soldiers-lost term, only if base >= 50, capped at MaxAimAssistScore [V3 raw.githubusercontent.com/X2CommunityCore/X2WOTCCommunityHighlander master .../X2AbilityToHitCalc_StandardAim.uc, fetched 2026-10-22]. This is the community fork of the shipped class (a master switch to disable it is the fork's addition, issue 1228); I did not diff against vanilla.
  - Values from DefaultGameCore.ini as quoted in one Steam post (2020-10-03): Rookie x1.2, +10/miss, aliens -10/hit, +15/-10 per soldier lost; Veteran x1.1, +10/miss, +10/-10; Commander x1.0, +15/miss; Legend none; threshold 50, cap 95, squad 4 [V3 steamcommunity.com/app/268500/discussions/0/2944746708998250511; excerpt not checked against files]. The fandom page agrees [V3 xcom.fandom.com Game_difficulty_(XCOM_2)].
  - [CONTESTED] the script comments say "only applied in Easy & Normal" but the quoted ini and the wiki give Commander a +15 miss-streak bonus.
  - Enemy Unknown: Firaxis lead designer Ananda Gupta: "On Normal and Easy modes, there's a bad streak breaker"; on Easy three misses means "you're not going to miss your fourth shot"; "doesn't exist" on Classic or higher [V3 gamebanshee.com/news/112504 repost of a PCGamesN interview, 2013-10-17; I did not open the original]. Community datamining of XComGame.upk (XGAbility_Targeted) describes 120% of displayed chance with 4 or fewer soldiers on Easy/Normal, +15% per consecutive miss on shots >= 50%, aliens -10% per consecutive hit [V3 ufopaedia.org Chance_to_Hit_(EU2012) / Difficulty_(EU2012)]. [CONTESTED] the miss bonus cap: 30 on one Ufopaedia page, "no upper limit" on another; Gupta's "even 1%" example conflicts with the >= 50% threshold.
- Cosmetic: soldier names, appearance, nationality in EU, flags of squads.
- Dominant answer: concealment ambush with overwatch is the standard opener (guide advice) [V3 fandom Squad Tactics].
#### 8. Open items
No v2 table. Attachment `62dd3fd3` line 173 claim: VERIFIED as above (hidden player-favourable adjustment and streak-breaking on lower difficulties), refinements: Commander also gets a miss bonus; Legend/Impossible none; alien-side reductions exist; aids apply to non-reaction, non-guaranteed shots. Lineage "descendant of Meier's" fix `?` (no source links XCOM to it). Line 746 ("not verified to a Firaxis primary source"): now supported by a designer quote (secondary repost) and shipped-script text; still no first-party document. The original PCGamesN article not opened; time-per-session [M].
**Capability ids (tagged):** B1 YES, B2 YES (hire at Barracks / Resistance HQ) [V3 ufopaedia Soldiers (EU2012); Wikipedia XCOM_2]; B3 PART (class/skill choice; Resistance Orders WotC) [V3 fandom Covert Actions]; B4 PART (engineers/scientists to projects, covert actions) [V3 Wikipedia]; B5 `?`; B6 PART (soldier panic in EU [V3 Wikipedia EU]; bonds WotC [V3 fandom WotC]); B7 NO [M]. D1 PART (Resistance Orders) [V3 fandom Covert Actions]; D2 NO (funding is income) [M]; D3 PART (advisers: Tygan, Shen) [V3 Wikipedia XCOM_2]; D4 YES (EU country panic; XCOM 2 Avatar meter) [V3 ufopaedia Panic; fandom Avatar]; D5 NO, D6 NO [M]. F1-F3, F5-F7 NO (squad scale only, 1-6 soldiers in EU) [V3 Wikipedia EU]; F4 YES (turn-based squad) [V3 Wikipedia]; F8 PART (soldier panic) [V3 Wikipedia EU]. H1-H6 NO (no diplomacy; EU Council is a funder) [M]. L1 PART (soldier bios, bonds) [V3 fandom WotC]; L2 PART (death only; aging not seen) [M]; L3 NO [M]; L4 PART (stories arise from play, not scripted) [M]; L5 PART (ADVENT Dark Events, Chosen act on their own) [V3 fandom Dark Events, WotC].

### Brigandine: The Legend of Runersia - facts line
Mostly [V3] but second-hand: the official Happinet site (producer letters, game-system page) returned 403, so letters are read through press reposts; mechanics numbers come from the fandom wiki's wikitext (community reference, read via api.php, revs 2023-2026) and eight reviews. No first-party manual was reachable, so section 4 is assembled from reviews and the tutorial's published topic list, not the in-game script.
- Developer Matrix Software, publisher Happinet; turn-based strategy + tactical RPG; Switch 2020-06-25, PS4 2020-12-10, Windows/Steam 2022-05-11 [V3 en.wikipedia.org/wiki/Brigandine:_The_Legend_of_Runersia raw, 2026-10-22; Steam News API appid 1843940].
- Version: Steam v1.02 (2026-05-04, hang fixes only after an April known-issues notice; earlier 1.01 2022-05-24, 1.01.1 2022-06-14) [V3 Steam News API, 2026-10-22]. Rules cross-checked against the Switch/PS4 1.1.2 "Titans and the Iron Front" notes (2020-12: Custom difficulty, Auto Mode, monster cap 100 -> 200) [V3 gematsu.com/2020/12/brigandine-the-legend-of-runersia-titans-and-the-iron-front-update-now-available-for-switch-launches-december-10-for-ps4]; that Steam ships with them is [M]. Steam adds Creative Mode [V3 store.steampowered.com/api/appdetails?appids=1843940].
- Assumed: Main Mode, Easy, Norzaleo, Steam. Campaign 20-40 h per nation [V3 rpgsite.net/interview/9881 2020-06-17]; one sitting ~1-3 h = a handful of seasons [M].
- Contrast, Brigandine: The Legend of Forsena (Hearty Robin, PS1 1998; Grand Edition 2000): same skeleton, but monthly turns, stats named Rune Power/Rune Area (= Magic Pool/Command Range here), defeated knights retreat to their capital, a castle ringed by enemy castles forces its defenders to flee, monsters take no equipment (Grand Edition: accessories) [V3 brigandine.fandom.com Glossary, Capital, Monsters; Wikipedia Brigandine_(video_game) raw].
#### 1. Setup choices
- Mode: Training (hands-on tutorial: introduction, controls and movement, organise and invade, battle basics, combat strategies, quest rewards, class changes), The Legend of Runersia (Main), Alternate Chapter/Challenge (unlocks after a Main clear), Records, and on Steam Creative Mode [V3 gamepitt.co.uk review; rpgsite interview; Steam appdetails]. A switchable advice guide runs inside campaigns [V3 gematsu.com producer letter 1, 2020-03].
- Difficulty, fixed for the whole campaign [V3 blog.playstation.com/?p=344482, 2020-12-09]: Easy (no season limit, quests never fail, more knight-recruit events, CPU errs in combat), Normal (120 seasons = 5 years), Hard (60 seasons = 2.5 years; CPU weighs power gap and position); 24 seasons = 1 year [V3 nintendoeverything.com/brigandine-the-legend-of-runersia-details-difficulty-modes, 2020-03-13]. Custom (1.1.2): up to eight settings, six named: base difficulty, time limit, player mana multiplier, player EXP multiplier, Revival Stone supply, CPU Defensive AI incl. "Guard Castle Hex" [V3 gematsu 2020-12 page].
- Nation (the ruler comes with it), start castles/knights/monsters/mana [V3 brigandine.fandom.com nation pages, rev 2026-05]: Norzaleo (Rubino) 5/13/33/543; Guimoule (Eliza Uzala) 8/12/35/905; Shinobi Tribe (Talia) 5/12/30/482; Mana Saleesia (Rudo Marco) 10/14/49/1202; Mirelva (Stella Hamett) 7/14/39/727; Gustava (Tim Gustav) 6/11/35/1007; 41 bases in all [V3 rpgsite interview].
- Strategic difficulty by nation (lead designer): Norzaleo 1 star (5 bases, 2 front-line), Shinobi 1 star (2 front-line, forest home), Guimoule 2 stars (3 front-line) [V3 nintendoeverything.com/brigandine-the-legend-of-runersia-details-difficulty-selection, 2020-04-17]; the other three `?` (letters unreachable). No character build: starting knights, monsters and mana are fixed per nation.
#### 2. The loop
Clock: turns only, no real time. One season = one Organization Phase + one Attack Phase, all six nations in sequence [V3 Wikipedia Runersia; nintendoeverything difficulty-modes].
1. Season start: each base adds mana to the national reserve and every monster's upkeep is deducted (Lanster 568, Angrein 325 per season; Imp upkeep "7+", summon cost 70); if the reserve cannot pay, all monsters start battles at 70% HP/MP [V3 fandom Mana, Lanster, Angrein, Imp].
2. Organization Phase (you, no clock): summon at a base (each offers only its own monster list), fill troops within each knight's Magic Pool, equip, change class, move troops along roads between your connected bases, send knights on quests, then choose which adjacent enemy bases to hit and with which troops [V3 gamingtrend.com review 2020-06-25; waytoomany.games review; fandom Quest]. A troop that moved or went on a quest cannot attack this season.
3. Attack Phase: every nation's moves are revealed (bases that stood empty fill, full ones empty); clashes resolve in priority set by knight level/combat power; an undefended base is occupied with no fight [V3 gamingnexus.com review; fandom Glossary; Wikipedia].
4. Each battle (you attack or are attacked): up to three troops a side, hex map, the attacker has 12 turns to beat every defending knight; units act highest-level knight first, each followed by its monsters; a ruler's fall sends all that nation's knights home [V3 fandom Castle, Ruler; gamingtrend; Wikipedia Brigandine_(video_game) for Forsena-era text].
5. Aftermath: base changes hands or not; beaten knights are wounded and sit out, retreating ones recover sooner; abandoned monsters can be recruited by the winner next Organization Phase; story/conversation events fire (100+ keyed to who is fielded) [V3 gamingtrend; rpgsite interview].
6. Season counter +1; check victory (all 41 bases) and the time limit; back to 1. Automated: all CPU planning and attacks, mana tick, quest results, recovery, optional battle Auto Mode. Interrupts: forced defence battles, recruit/story events, random events in Challenge Mode [V3 fandom Challenge Mode].
#### 3. The choice menu
| verb (frequency) | cost | effect | when |
|---|---|---|---|
| Summon a monster (constant) | summon mana (Imp 70), upkeep (Imp 7+), Magic Cost slot (15-125; Imp 20); arrives Lv 1 | adds a body; list differs per base | early, refilling losses |
| Assign monsters to a knight (constant) | total Magic Cost <= Magic Pool; up to 6 per knight | sets troop power and role mix | after any summon/class change |
| Move a troop between your bases (constant) | that troop cannot attack this season; needs a chain of your bases | fills fronts, reaches other summon lists | every Organization Phase |
| Pick invasion targets and troops (constant) | origin base thinner; 3 troops fight | the only way to gain bases | each season you advance |
| Leave a base empty or stacked (constant, implicit) | none | empty = captured unfought; many knights deter CPU [V3 worthplaying.com review] | always |
| Quest or Training Grounds (frequent) | knight absent one season; Good/Great/Excellent odds; rulers Training/Phantom only | EXP, items, stats, rare monsters/knights | idle rear-base knights |
| Change class (periodic) | monsters upgrade at Lv 10 and cost more Magic Cost; knight classes gated by stats (mage classes INT >= 60) | new spells; Proficiency 5 keeps old ones | at thresholds |
| Equip / use items (periodic) | quest loot; Revival Stone scarce | stats, element, terrain; revive a monster | after quests |
| Release monsters (rare) | lose the unit | cuts upkeep; cap 200 | mana short |
| Battle: move, attack, skill, spell (constant in battle) | MP; counterattacks; skills/spells mostly not after moving | kill knights, hold terrain | every battle |
| Retreat (rare) | lose the fight; a defended base falls [V3 rpgsite interview] | saves the troop | losing fight |
| Auto Mode (periodic) | give up micro | faster battles | trivial fights |
| Inspect enemy CP/Power Relationship (constant, free) | none | judge odds | before attacking |
#### 4. First hour, step by step
Basis: producer letters, the tutorial's topic list and reviews above; steps 1-3 are from letters/store text, 4-13 are my assembly of review descriptions (no beginner's guide with exact steps was found).
1. Open Training and finish its seven sections [V3 gamepitt]. 2. Start The Legend of Runersia on Easy (producer: "If you're new or not used to this game genre, I would recommend going with Easy") [V3 gematsu producer letter 1]; difficulty is then locked.
3. Pick Norzaleo or Shinobi (1 star: only two front-line bases) [V3 nintendoeverything 2020-04-17]; leave the advice guide on.
4. Season 1, Organization: open the map, find front-line bases (adjacent to enemy bases) and read each neighbour's mana/knights/monsters/CP in the hover summary [V3 gamepitt].
5. Open each base's roster: note every knight's Magic Pool, Command Range and class.
6. Summon at bases that offer the monster you lack; fill each knight up to the Magic Pool; keep healers and sturdy fronts behind strong damage dealers [V3 nintendolife.com review].
7. Move your strongest troops to the front-line bases; never leave a border base empty.
8. Send low-level or spare knights on Training Grounds/quests only from rear bases; they are gone for the season.
9. End Organization; at Attack, either pass or choose one adjacent base where your combined CP clearly exceeds theirs; pick up to three troops.
10. In battle keep monsters inside the Command Range, aim for enemy knights, remember counters and that spells cannot follow a move.
11. After the win, read the results: level-ups, captured monsters, story event; the new base needs a troop immediately.
12. Next Organization: replace losses, class-change anyone at Lv 10, check mana income against upkeep in the summon menu.
13. Repeat, taking one neighbour at a time; use Auto Mode for lopsided fights [V3 gamingnexus; gematsu 2020-12].
#### 5. What changes later
- More bases means more fronts and more staffing; reviewers advise one enemy nation at a time [V3 gamingnexus]. Ruler classes upgrade at 23-28 castles (Prince -> Crown Prince at 23) [V3 fandom Rune Knight Classes]. Eliminating a Brigandine-holding nation lets you pull its Mana Stone and equip it [V3 fandom Mana Stone].
- Top-tier monster classes need Secret Treasures (quest loot); Mana Miracle summons add +20 HP/MP and +10 other stats (10% chance at Magic Cost <= 30, 5% at 35-60, 1% at 65+) [V3 fandom Monsters].
- Pressure: CPU nations gain EXP at the player's rate [V3 rpgsite interview] and, on higher difficulty, organize better and invade harder [V3 nintendoeverything 2020-03-13]; the season limit bites on Normal/Hard.
- After unification: Phantom Quests (ten battles unlocked in stages: 4, then 5, then 1), a final story battle, and in Challenge Mode a revolt of four rebel groups as victory condition 10 of 10 [V3 fandom Quest, Rune God, Challenge Mode].
#### 6. Failure and ending
Losing a battle is not game over: you lose that base and can rebuild and retake it [V3 rpgsite interview]. Losing every base is game over [S3 search summary citing gamerbraves.com/?p=58446 and a Nintendo page; neither opened]; hitting the season limit ends the game [V3 Wikipedia]. Win = hold all 41 bases at once, then the endgame choice (side with Aurora or the Rune God) and final battle [V3 Wikipedia; fandom Rune God]. Recoverable: lost bases yes, dead monsters only via scarce Revival Stones, a missed time limit no.
#### 7. Consequential vs cosmetic choices
- Consequential: how many knights stand on each border base and when you thin them to attack (the CPU is inclined to hit weak targets) [V3 worthplaying; rpgsite review 2020-06-25, one reviewer's claim]; which monsters fill the Magic Pool and where they stand relative to the knight, because a fallen knight takes the troop out of the fight [V3 nintendolife; worthplaying].
- Consequential: quests versus defence each season, and mana (upkeep deficits cut every monster to 70%) [V3 fandom Mana].
- Near-dominant (community consensus, one thread, poster had not played Challenge Mode): mass White Elemental stacks kill knights in a turn; the Elemental line is the "easy victory" build across the series [V3 steamcommunity.com/app/1843940/discussions/0/3409804177169141748, 2022-07-05]. One reviewer: brute damage plus healing wins and "none of the nations feel different in combat" [V3 worthplaying].
- Cosmetic or weak: ruler choice for combat feel (one reviewer); conversation events; the designer calls each nation's main story "more or less the same" bar one late branching point [V3 rpgsite interview].
#### 8. Open items
No v2 table, so no cell corrected. `?`: ratings for Mana Saleesia, Mirelva, Gustava; who picks the defending three; whether CPU-vs-CPU fights are played out; whether the time limit lifts mid-game ("at a certain point in all difficulties" [V3 nintendoeverything 2020-03-13] vs a Challenge Mode thread saying it stays); Easy-mode CPU not advancing and cheaper upkeep [S3 happinet letter 10, may describe only the demo]. [CONTESTED] win rule: attacker must beat every knight within 12 turns [V3 fandom Castle] vs "or occupy the castle by the last turn" [V3 rpgsite review]; and knight defeat: monsters "go with" or are "lost" with him [V3 worthplaying; gamecritics.com review] vs "may be left behind and captured" [V3 fandom Monsters].
**Repo claim "Brigandine garrisons are a precedent" (companion_part2.md:28 X5 "Garrison is an assignment, never a unit type - 4/4"; PMM:722-729 "Brigandine's shape: garrisoned units lost wholesale if the territory falls"; by_lane/MB:161,355; SE:99):** PARTLY HOLDS, with two corrections. Holds: there is no garrison unit type; a base is defended by whichever ordinary knight-plus-monster troops stand there, and moving or questing removes them [V3 Wikipedia; gamingnexus]. Overstated: the game names no garrison, order or role, and the repo's own table leaves Brigandine's cell "-" (companion_part5.md:168; MB:161 cites it), so the 4/4 is inference; "Guard Castle Hex" is a CPU battle-AI option, not a garrison. Wrong: units are not lost wholesale; knights survive and retreat to the nearest connected castle, only monsters left behind or stored unassigned are captured [V3 fandom Rune Knight, Monsters]; the repo's own sourcing note says the Brigandine wiki would not load (PMM:31). Its "Rune Area" is the Forsena term (Command Range here).
**Capability ids (tagged):** B1 YES (100+ knights, Info panel) [V3 fandom Rune Knight; gematsu 2020-12]; B2 YES (summon, quest recruits, release/dismiss) [V3 fandom Challenge Mode, Monsters]; B3 PART (assign to troops/bases, class change) [V3 gamingtrend]; B4 YES (quests, movement) [V3 fandom Quest]; B5 PART (quest Repeat; battle Auto) [V3 gematsu 2020-12]; B6, B7 NO (none seen) [M]. D1, D3-D6 NO [M]; D2 PART (mana budget, no rates) [V3 fandom Mana]. F1 YES, F2 YES [V3 fandom Monsters, Rune Knight]; F3 PART (pick 3 troops; entry road sets position) [V3 fandom Castle]; F4 YES [V3 Wikipedia]; F5 PART (Auto Mode) [V3 gematsu 2020-12]; F6 PART (castle hex, 12-turn timeout) [V3 fandom Castle]; F7 PART (upkeep deficit) [V3 fandom Mana]; F8 YES [V3 fandom Ruler, Monsters]. H1-H6 NO (war permanent from turn one) [V3 fandom Runersia]; one review mentions "unofficial truces" [S3 rpgsite review, unexplained]. L1 PART (named knights, 100+ keyed events) [V3 rpgsite interview]; L2 PART (monsters die, knights do not) [V3 fandom Monsters]; L3 NO [M]; L4 PART (CPU history differs per run) [V3 rpgsite interview]; L5 YES (CPU nations act and grow) [V3 rpgsite interview].
