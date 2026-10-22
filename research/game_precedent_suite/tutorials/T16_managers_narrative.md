# T16 - Managers and narrative tutorials: Football Manager 26, Caves of Qud, King of Dragon Pass, Six Ages

Written 2026-10-22. Tags: [V3 url] read in a fetched page body this session; [S3 url] search snippet only; [M] memory; ? not established; [CONTESTED]. No v2 capability tables exist for these games, so each section ends with a compact capability-id line (B, F, H, L, M). Repo-claim and attachment checks are in each section 8. Reading method: full page bodies by curl (Qud wiki raw, A Sharp pages and manuals, Six Ages manual, Steam news API, Wikipedia raw, the Grinblat PDF); the footballmanager.com, fmscout, Operation Sports, ggrecon, fm-arena, Steam-thread and blog.how-many-scenes pages came through WebFetch, which returns a small-model extract of the page, so those [V3] tags mean an extract, not a full read. v2 cells corrected: none (no v2 tables for these games).

### Football Manager 26 (current edition) - facts line
Sports Interactive / Sega; football (soccer) management sim. FM26 released 2025-11-04 (Windows, macOS, PS5, Xbox; Switch 2025-12-04; mobile via Netflix) [V3 https://en.wikipedia.org/wiki/Football_Manager_26 raw, 2026-10-22]. Patch relied on: the 26.x line, last Steam update listed 26.3.2 on 2026-06-09, "no further updates" announced July 2026 [V3 Steam news API appid 3551340, read 2026-10-22; Wikipedia]. FM27 is dated 2026-11-10, so this tutorial describes the edition about to be replaced [V3 Wikipedia FM27 raw; Steam news 2026-09-30]. Assumed: single-player career, Quick Start, men's club league. One play session = one match week, about 15-40 minutes [M]; a season is tens of hours [M]. Sources: official footballmanager.com guides and Steam news are [V3]; weekly routine detail is community guides (fmscout) [V3 page bodies, opinion]; match-simulation internals are [S3]/[M] (see section 8).

#### 1. Setup choices
1. **Start mode**: Quick Start (game loads the countries around your club) or Advanced Setup (you control database size, transfer windows, preferences; shows an "Estimated Game Speed" indicator) [V3 https://www.footballmanager.com/the-dugout/starting-your-first-save-fm26].
2. **Nations and leagues**: pick from 58 men's and 11 women's nations; each can be playable or view-only. More loaded data = slower saves [V3 same page].
3. **Database size**: from "Current international players" and "Players based in nation" up to "Players from top division clubs", "...continental reputation", "...national reputation" [V3 same page].
4. **Start date and transfer mode**: "Original", "Real World" (transfers on real dates) or "Your World" (data frozen at 25/26 season start) [V3 same page].
5. **Locked advanced switches**: fake players and staff, real fixtures, add key staff, add players to playable teams, first-window transfer activity, player attribute masking (scouting needed to see attributes), control teams with managers in place, in-game editor [V3 same page].
6. **Manager profile**: appearance, playing and non-playing achievements, coaching badges, management style and personality; these set your manager's ability, reputation, style and attributes [V3 same page; Xbox tips https://news.xbox.com/en-us/2025/11/21/football-manager-26-console-tips-guide/]. A beginner guide also names an "Experience Level" field, "No Experience" keeps tutorials on [V3 https://www.fmscout.com/a-beginners-guide-to-football-manager-2026.html]; the official page lists no difficulty setting or experience level [CONTESTED: left unresolved].
7. **Club**: any club in a playable league, or unemployed. Previews show predicted finish, board and supporter culture, finances, rivals [V3 official page]. Board expectations seen at selection: Mid-Table / Top Half / Title Favourites [V3 https://www.footballmanager.com/the-dugout/first-10-things-do-fm26].
8. **Staff delegation**: choose which jobs you keep (training, team talks, press, scouting) in the Overview/Delegation tabs [V3 first-10-things].

#### 2. The loop
Clock: calendar days. A Continue button advances the date until something needs you (a message, a match). Matches fall on set dates of a fixed fixture list; transfer windows are open at fixed periods [M for the Continue behaviour and windows; fixture list [V3 "Use Real Fixtures" setting]].
1. **Read the Portal** (Agenda + Messages, replaced the old Inbox): board notes, contract requests, injuries, scout reports, transfer offers [V3 fmscout beginner guide].
2. **Adjust the club**: Squad (selection, morale, contracts), Tactics, Scouting, Transfers, Training, Matches, Club, Youth are the top-bar sections [V3 fmscout].
3. **Set the plan for the next match**: Match Day area has Next Match Preparation and Data Hub [V3 first-10-things]. Tactics are two shapes, In Possession and Out of Possession, plus roles/duties and team instructions [V3 Xbox tips; fmscout].
4. **Pre-match**: press conference and team talk; the assistant can give team talks and can be sent to press conferences [V3 fmscout].
5. **Match**: pick how to watch (section 8); during play you may give shouts, make subs, change mentality/shape; the assistant now gives context advice such as spotting a weak full-back [V3 https://www.footballmanager.com/the-dugout/maximising-your-match-days-fm26].
6. **After**: ratings, injuries, morale, press; add Match Review to next week's training [V3 https://www.fmscout.com/a-fm26-training-guide-and-schedules-by-jonasmorais.html].
7. **Continue**. Automated: training progression, other clubs' transfers, finances, AI managers' tactics and subs; anything you delegated [V3 delegation; M for the rest].
Interrupts: match days hand control to the match screen; transfer bids and board messages stop the calendar [M].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Continue (advance day) | none | time passes, events fire | constantly |
| Pick XI and bench | attention; fitness/morale of omitted players | who plays | every match |
| Set tactic (formations, roles, instructions) | player familiarity if changed often | match behaviour | weekly; major rebuilds rarely |
| Team talk / shouts | none or morale risk | short morale swing | every match [V3 fmscout: positive vs weaker, cautious vs stronger] |
| Substitutions / in-match tweaks | slots (limited) | fix fatigue, cards, scoreline | every match |
| Training schedule and intensity | injury risk vs growth | development, condition | set rarely, revisit in busy weeks [V3 jonas guide] |
| Individual training | coach time | role/attribute focus per player | occasionally |
| Recruitment focus / shortlist | scout time | candidates appear | each window |
| Make a transfer or loan offer | fee, wages, budget split | new player | in windows |
| Post TransferRoom Requirement / Pitch Opportunity | none | tells all clubs what you want / can sell | each window [V3 transfer-market-top-tips-fm26] |
| Renew, sell, release | wages, morale | squad churn | as contracts expire |
| Press conference answers | board/player mood | pressure management | weekly (or delegate) |
| Player conversation, praise, criticise | morale | monthly nudges [V3 jonas] | occasionally |
| Hire / fire staff, delegate | money, attention | quality of automated work | rarely |
| Match view mode / Instant Result | none | what you see and may touch | every match |

#### 4. First hour, step by step
1. Choose Quick Start or Advanced; for a first game load only 3-5 nations with your own as playable [V3 fmscout].
2. Pick database size; leave transfer and attribute-masking switches at default or turn masking off to ease scouting [V3 official; fmscout].
3. Build the manager (badges, style); keep tutorials on [V3 official; fmscout].
4. Choose a club with sound finances and reasonable board expectations; avoid a relegation fight [V3 fmscout].
5. Read the welcome screens, board expectations (Club Vision, Five-Year Plan, Ongoing Tasks) and accept the first press conference [V3 fmscout].
6. Set staff responsibilities: decide what you delegate [V3 first-10-things].
7. Check Recruitment, then Clauses on day one: cash in a buy-out clause if the board has one [V3 first-10-things].
8. Review the squad in Squad Planner and the First Team screen before touching tactics [V3 first-10-things].
9. Build a tactic: an In Possession shape and an Out of Possession shape; keep roles simple [V3 fmscout].
10. Set training intensity at or below medium and give each player an in/out role to train toward [V3 jonas].
11. Create recruitment focuses (e.g. wonderkids 15-23 with 4-star potential, expiring contracts) [V3 first-10-things].
12. Set an autosave routine in Preferences [V3 first-10-things].
13. Play the first match in full or Dynamic mode and look for a tactical flaw [V3 Xbox tips; fmscout].
14. Substitute at 60-75 minutes if condition is under 75% or cards are booked [V3 fmscout].
15. After the match read ratings; carry one adjustment to next week's plan.

#### 5. What changes later
Transfer windows, contract expiry and youth intakes reshape the squad; international management returned in a free update in May 2026, with women's international management [V3 Wikipedia; Steam news 2026-05-26]. Board expectations may change with results. FM27 adds Tactical Effectiveness (player ability, next-match info, buy-in, understanding) and a training overhaul [V3 Steam news 2026-10-09]. Pressure ramps by fixture congestion and finances.

#### 6. Failure and ending
No fixed ending: a career continues across seasons [M]. You can be sacked by the board, then take another job or stay unemployed [M]. Board confidence, finances and fan mood are the pressure meters [M; V3 only that expectations exist]. Recoverable: yes, by taking a new post.

#### 7. Consequential vs cosmetic choices
- Tactics fit to the players' roles and attributes; a tactic needs time to bed in (named Tactical Familiarity, now Effectiveness) [V3 Steam news 2026-10-09].
- Selection, rotation and fitness: guides stress condition and morale [V3 fmscout].
- Recruitment and the budget split between wages and transfers [V3 official].
- Probably cosmetic: view mode. Most posters in one Steam thread say it changes what you see, not the result; no developer or moderator replies in the thread, so this is opinion only [V3 https://steamcommunity.com/app/872790/discussions/0/1742227264187754385].
- Dominant answer: none established; community guides disagree on training weight [S3].

#### 8. Open items
- Repo claim "instant ~ played" (REPO_MENTIONS s3; ruled doctrine cited there). **Not verified by SI.** Found: FM26 has an Instant Result (changelist mentions "freezing when using Instant Result during hotseat mode") [V3 Steam news 26.1.2, 2026-01-19]; a pre-launch report calls it a skip-to-result button that bypasses the match engine, historically a skin on PC and native in Touch/console [V3 https://www.operationsports.com/football-manager-26-adds-instant-result-option-for-matches/]. No SI statement says it runs the same simulation. A moderator says Match Plans work with it and a player asks why it makes no substitutions [S3 fm-arena]. A German preview says matches can be simulated in simplified form and 3D is atmosphere [S3 pcgames.de]. **Verdict: plausible, not established.** What visibly differs is your control (no live shouts or subs), which is not evidence about simulation fidelity either way. The ladder of Full Match / Comprehensive / Extended / Key / Only Commentary is real in FM24 [V3 https://ggrecon.com/guides/football-manager-2024-change-highlights; the page does not say what each shows]; FM26's official guide recommends Dynamic Highlight mode, which varies the number of highlights with the match's importance [V3 Steam news 2025-11-09]. Whether the FM24 list is unchanged in FM26: ?. What a skip shows: the pre-launch report says it simulates the rest of a match "without watching highlights or the 3D match engine" [V3 Operation Sports summary]; the post-match screen content is [M].
- Repo claim "formation/role model": FM26 uses In/Out-of-Possession formations, roles and duties [V3 Xbox tips; fmscout]: supported.
- Attachments: 62dd3fd3:553 files FM under "Management / policy-budget / days-months / medium compliance": imprecise, since you also set minute-level match tactics and how well players carry out your tactic depends on familiarity (the FM27 post says its new system builds "on the previous Tactical Familiarity system") [V3 Steam news 2026-10-09]. 62dd3fd3:601 "statistics -> commentary -> arc" [M]: unverified. 62dd3fd3:622 "assistant reports and delegated training": delegation of training, team talks and press is real [V3 first-10-things; fmscout]; "scapegoat" is a reading, not a mechanic.
- Not established: sacking rules, exact fixture/day rhythm, what Instant Result shows after the match (score and report? [M]).
- Capability line (B,F,H,L,M): B1 YES [V3 official], B2 YES [V3], B3 PART [M], B4 YES (training/roles) [V3], B5 YES (delegation) [V3], B6 YES (morale) [V3 fmscout], B7 NO [M]; F1-F8 NO [M]; H1 PART (team talks, press, conversations) [V3 fmscout], H2 YES [M], H3-H6 NO [M]; L1 YES [M], L2 YES (ageing, newgens) [V3 fmscout], L3 NO [M], L4 PART [M], L5 YES (AI clubs) [M]; M1 PART (board objectives, sacking) [V3 official], M2 NO [M], M3 YES [M], M4 PART (advice, Data Hub) [V3], M5 PART [M].

### Caves of Qud - facts line
Freehold Games; turn-based science-fantasy roguelike with open-world exploration. Version relied on: 1.0 (released 2024-12-05) and wiki build log up to Build 211.55 (2026-09-23) [V3 https://wiki.cavesofqud.com Version_history raw, read 2026-10-22]; wiki numbers are mostly "as of patch 2.0.2xx" code reads, so treat thresholds as 2.0-era values still current unless noted. Tutorial assumes Classic mode (permadeath), the Joppa start, no DLC. One session = open-ended (turn-based, save on exit); a full run to the ending is dozens of hours [M]. The Qud "faction reputation" content below is mostly [V3] from wiki raw pages; the first-hour steps are partly [M] because the wiki's own beginner page is marked out of date.

#### 1. Setup choices
1. **Game mode** (fixed for the save): Classic = permadeath ("the standard Qud experience"); Roleplay = on death you may reload the last checkpoint, which is set automatically on entering/leaving a settlement or by hand (Esc, then c); Wander = settlement checkpoints, every faction starts at 0 or higher rep, no XP for kills, more XP for discoveries/quests/water rituals [V3 https://freeholdgames.itch.io/cavesofqud/devlog/251161/feature-friday-may-7-2021, 2021 post; may have changed since]. A beginner tutorial preset shipped before 1.0 [V3 Steam news 2024-10-29]; a daily challenge exists [V3 same post].
2. **Genotype**: Mutated Human (mutations, no cybernetics, base attributes 10 each + 44 points to spend, cap 24) or True Kin (cybernetic implant, base 12 each + 38 points, cap 24; starts only -100 with the mutant-hating Putus Templar instead of hostile) [V3 wiki Mutated_Human, True_Kin].
3. **Subtype**: Mutated Humans pick one of 12 callings (Apostle, Arconaut, Greybeard, Gunslinger, Marauder, Pilgrim, Nomad, Scholar, Tinker, Warden, Water Merchant, Watervine Farmer); True Kin pick one of 12 castes in three arcologies (Horticulturist, Priest of All Suns, Priest of All Moons, Syzygyrior, Artifex, Consul, Praetorian, Eunuch, Child of the Hearth/Wheel/Deep, Fuming God-Child). Each sets attribute bonuses, starting skills, equipment, and some starting faction reputation (e.g. Gunslinger +200 Mysterious strangers; Warden +300 Fellowship of Wardens) [V3 wiki Callings, Castes, Reputation].
4. **Mutations** (mutants only): 12 points; each mutation costs 1-5; optional defect gives back 1-4; morphotype Chimera (physical only) or Esper (mental only) [V3 wiki Mutated_Human, Mutations]. **Cybernetic** (True Kin only): one of 16 starting implants, 2 license points; skipping it gives +1 Toughness [V3 wiki True_Kin].
5. **Attributes**: spend the point pool across Strength, Agility, Toughness, Intelligence, Willpower, Ego [V3 wiki Game_concepts].
6. **Starting village**: Joppa (fixed, game-recommended for new players) or a random village in a chosen biome (Salt Marsh, Salt Dunes, Desert Canyons, Hills), each giving small reputation grants and a signature skill taught by water ritual [V3 wiki Joppa, Village, Reputation]. Optional: a pet from the Harvest Dawn DLC [V3 Steam news 2024-12-05].

#### 2. The loop
Clock: strict turns. An ordinary action costs 1000 action-points and Quickness (base 100) sets how fast you recover them, so faster creatures act more often [V3 wiki Ten_Things...]. Nothing moves while you think. There is a calendar and creature hunger/thirst, and hostile NPCs who were angered "calm down" after about 16,800 turns (two weeks) if their faction still tolerates you [V3 wiki Factions tip, marked Opinion].
1. On the world map (one tile = one "parasang" = 3x3 zones) pick a tile and descend into a zone (a screen). Surface zones are by region tier; each stair down is a deeper, harder level [V3 wiki World_map, Zone_tier].
2. Each turn you move, attack, use an activated ability, interact (space), trade, or rest. Bump = melee; targeted fire = missile.
3. Every NPC then acts. Whether a creature attacks you is decided by its faction's reputation toward you plus its own demeanor (docile / neutral / aggressive) [V3 wiki Reputation].
4. Kills, quests and discoveries give XP (Wander removes kill XP); a level-up gives skill points (scaled by Intelligence) and, for mutants, 1 mutation point [V3 wiki quest pages, Ten_Things, Mutations; itch devlog].
5. Return to a settlement to sell loot (fresh water is the currency; secrets and gossip sell to the factions that want them), take quests, and do water rituals with unique/legendary creatures [V3 wiki Game_concepts].
Interrupts: hostile contact stops auto-explore/auto-actions [M; Steam build 211.55 notes show auto-explore interrupts]; reputation changes flip whole populations from friendly to hostile (e.g. attacking a friendly's faction mate) [V3 wiki Factions]. Automated: NPC behaviour, autoexplore, rest-until-healed.

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Move/explore (zone, world map) | turns, water, risk | find loot, lairs, villages, ruins | constantly |
| Melee / missile attack | turn; ammo | hit roll 1d20 + Agility mod vs DV, then penetration vs AV | constantly |
| Activated ability (mutation/skill) | cooldown | build-defining powers | constantly |
| Rest / eat / drink | turns, supplies | recover HP, stop thirst | often |
| Trade (barter) | water/items; Ego haggling; reputation shifts price | gear, ammo, healing | often at settlements |
| Take / turn in quest | time | XP, items, and +rep to quest faction (e.g. 200 with Joppa villagers) | at each settlement |
| Water ritual | 1 dram; reputation | +/-50..100 rep with that creature's faction, then trade rep for secrets, skills, recipes, a follower, or items | whenever a unique/legendary creature is non-hostile |
| Sell secret / gossip | the item itself | +50 secret, +100 gossip rep with an interested faction | opportunistically |
| Identify artifact | chance to break it | reveals function; Intelligence-based | often early |
| Spend skill / mutation points | level-up points | new powers; 4 MP buys 1 of 3 random mutations | at each level |
| Tinker / cook / mod | bits, ingredients | craft gear, tonics, meals | mid-game for specialists |
| Recruit follower | rep cost -(12*(creature lvl - yours)+200), min 50 | permanent companion, no cap via ritual | rarely |
| Wear faction-keyed items | opportunity cost | e.g. feathered +250 Birds; ape fur -100 Apes each piece | rarely, deliberately |
| Break water-bond (kill ritual partner) | -100..-200 with all factions | oathbreaker | almost never |
All reputation values from [V3 wiki Reputation, Water_ritual, Factions].

#### 4. First hour, step by step
1. Optionally play the in-game tutorial preset first [V3 Steam news 2024-10-29].
2. Pick Classic or Roleplay (Roleplay if you do not want permadeath) [V3 itch devlog].
3. Choose True Kin (stronger start, cybernetic) or Mutated Human (mutation sandbox); beginners are commonly pointed to simple builds [S3 forum.quartertothree.com thread posts 74/429; low confidence].
4. Spend attributes and the subtype; accept default start unless you have a plan.
5. Start in Joppa. The intro text sets the scene; the game recommends it for new players [V3 wiki Joppa].
6. Press look (l) on everything; hold Alt for an overlay (stairs magenta, friendly green, hostile red, chests yellow) [V3 wiki Ten_Things, marked out of date].
7. Visit Tam the dromad merchant (south-east) to buy basics; keep your water (heavy but currency) [V3 wiki Ten_Things, Joppa].
8. Talk to Mehmet; take "What's Eating the Watervine?" (level 1, Red Rock two parasangs north, return a girshling corpse; reward Ubernostrum injector, spray foam, 3 salve injectors, +200 Joppa rep) [V3 wiki quest page].
9. Do a water ritual with Mehmet and Elder Irudad (both teach Harvestry); this is your first reputation action [V3 wiki Joppa].
10. Talk to Argyve; take "Fetch Argyve a Knickknack" (any artifact needing identification; leads to the main quest line) [V3 wiki Fetch_Argyve_a_Knickknack].
11. Leave by the safer route: descend at Red Rock, not the waterlogged tunnel [V3 wiki quest page].
12. Fight in corridors; rest to full between fights; reload (Roleplay) or retreat if a fight reads "Very Tough" (look shows the rating) [V3 wiki Difficulty].
13. Return with the corpse; the elder explains lore and pays out.
14. Identify artifacts, turn one in to Argyve, spend new skill points, then pick the next goal (second knickknack, Grit Gate path, or a faction trip).

#### 5. What changes later
Zone tier raises monster level with distance and depth [V3 wiki Zone_tier]. Mutations are rapidly advanced at level 5 and every 10 after; mental mutations scale with Ego; esper builds attract esper hunters through Glimmer [V3 wiki Mutations]. Cybernetics expand through credit wedges and becoming nooks for True Kin. Reputation becomes a map of who will help or hunt you. The 1.0 update added the end of the main quest with multiple endings [V3 Steam news 2024-12-05]. An expansion, Diaspora, enters Early Access on 2026-12-09 adding playable animals/plants and new genotypes [V3 Steam news 2026-10-15]; not assumed here.

#### 6. Failure and ending
Classic: death deletes the character. Roleplay/Wander: reload last settlement checkpoint [V3 itch devlog]. Ways to die: thirst and hunger, being out-levelled [M], adverse reactions from stacked tonics [V3 wiki Ten_Things], and faction hostility after oathbreaking (-100 to -200 with every faction) [V3 wiki Factions]. Win: finish the main quest to one of several endings; players report "so many interpretations of the ending" [V3 Steam news 2024-12-19]. Details of endings: ? (not read; spoilers). Recovery: reputation can be rebuilt via ritual and quests; at -600 or lower even docile members attack, and the 'wait two weeks' calm-down tip only covers factions still at least neutral [V3 wiki Reputation, Factions].

#### 7. Consequential vs cosmetic choices
- Genotype and subtype: decide your gear, powers, and day-one standing with Putus Templar (hostile vs -100) [V3 wiki].
- Starting village: Joppa has fixed quests; a random village generates its own quest to start the main line [V3 wiki Village].
- Water ritual and who you ritual with: moves reputation across whole factions; breaking the bond hits all factions [V3].
- Procedural sultan lore is mostly cosmetic except where it decides a historic site, its relic, and which factions love/hate a sultan (trade goods) [V3 wiki Sultan, Historic_site].
- Dominant answers: no source examined; community "build tier lists" not read. ?

#### 8. Open items
- Claim check, repo claim "generate then rationalise; reify only when visited" (REPO_MENTIONS s3, `relay/G:61-71`): **first half VERIFIED** for sultan history: events are chosen at random and the cause is made up afterwards from the sultan's state, or by altering the state ("the effect causes the cause") [V3 https://pcgworkshop.com/archive/grinblat2017subverting.pdf, FDG 2017, sections 4.3, 4.5]. The same shape appears in faction feuds: every legendary gets randomized friend/foe factions "for a random reason" from a fixed list, including "some reason no one remembers" [V3 wiki Faction_relationship_reasons, citing GenerateFriendOrFoe.cs]. **Second half PARTLY WRONG**: shrines/paintings are built as the player explores new areas, yes (paper 4.1), but events and their gospel text are generated for all five periods at world creation, historic sites (at least eight) are placed at worldgen, and most generated regions never appear in play [V3 wiki World_generation, Historic_site]. "Only when visited" holds for the artifact layer, not for the history itself. Zones building on first entry: [M], unverified.
- Not examined: the 1.0 ending branches; exact game-mode list after 2021 (store listings say four modes [S3 search]); daily mode specifics.
- Attachment claims: the four attachments contain no Caves of Qud text (grep "qud", case-insensitive: 0 hits).
- Capability line (B,F,H,L,M): B1 PART [V3 wiki: followers by ritual/Beguiling/Proselytize], B2 YES [V3 Water_ritual: recruit cost formula], B3-B7 NO [M]; F1-F8 NO [M]; H1 YES (dialogue/ritual trade) [V3], H2 YES (per-faction rep with tiers at -600/-250/250/600) [V3 wiki Reputation], H3-H6 PART/NO [M]; L1 YES (named legendaries with generated relations) [V3 wiki Faction_relationship_reasons], L2 NO [M], L3 NO [M], L4 YES (generated sultan histories) [V3 paper], L5 PART [M]; M1 YES (endings since 1.0) [V3 Steam news], M2 YES (hand-authored main quest) [V3 wiki Joppa/Argyve], M3 YES (rep, oaths, permadeath) [V3], M4 PART (look shows odds, rep text) [V3 wiki Difficulty], M5 YES (world map to zone) [V3 wiki World_map].

### King of Dragon Pass - facts line
A Sharp (designers David Dunham, Greg Stafford, Robin D. Laws); clan strategy plus interactive-fiction hybrid set in Glorantha. PC/Mac 1999-10; iOS 2011-09; Android 2014; Steam port 2015-07 [V3 https://en.wikipedia.org/wiki/King_of_Dragon_Pass raw, 2026-10-22]. Version relied on: the official manual PDF (copyright 1999-2011, iOS-era wording) [V3 https://www.a-sharp.com/files/KoDP-Manual.pdf], Tips page (last updated 2019-07-07) and FAQ (2015-08-01) [V3 https://www.a-sharp.com/kodp/tips.html, /ifaq.html]. Assumed: Normal difficulty, Balanced Orlanth clan, Short game then Long. One session = a year or two (about 10-25 minutes) [M]; a Long game assumes about 53 years and about 5 random events per year [V3 https://kingofdragonpass.blogspot.com/2012/09/how-many-scenes.html, fetch summary]. Mostly [V3] from the manual and A Sharp pages.

#### 1. Setup choices
The game starts with an interactive "history of your clan" questionnaire; "no right or wrong answers", each answer sets your mythic profile, and your ancestors then expect you to live up to it [V3 manual]. Choices, in order:
1. **Main god**: Orlanth, Ernalda or Elmal; Orlanth is slightly easier and Elmal "significantly harder"; the game starts with a temple to the god chosen [V3 manual].
2. **Earliest famous event** (nine, e.g. Healing of Orlanth, Hundred-Day Hunt, Jested's Settlement, The First Pot, Clan-making Dance): grants a blessing or lifts leaders' skills in Combat, Bargaining, Animals, Plants, Custom or Leadership [V3 manual].
3. **Stick farmers** (slavery attitude), **ancient enemies** (you must keep the enmity), **dragons** (how you treat dragonewts) [V3 manual].
4. **Clan type** via King Heort: War, Balanced or Peace; changes starting fyrd size and magic allocation; Balanced is recommended to start; switching later is possible but some benefits need years of staying the same [V3 manual].
5. **The Dawn**: which deity you first awakened gets your starting shrine [V3 manual].
6. **Land claim**: more land supports a bigger clan but is harder to patrol [V3 manual].
7. **Difficulty**: three levels, affecting starting fortifications, trading partners, feuds and allies; "Hard can be very difficult", start on Normal [V3 manual; ifaq; tips]. **Length**: Short (tribe, then hold the kingship 10 years) or Long (found a tribe, unite the kingdom) [V3 manual].

#### 2. The loop
Clock: five seasons then Sacred Time: Sea (sow), Fire (war), Earth (harvest), Dark (indoors), Storm (anything goes) [V3 manual]. "Time will pass only when you initiate an action", two player actions per season; the season wheel forces time on [V3 manual]. Turn-based: you can stop and think [V3 ifaq].
1. **Sacred Time** (year end): recap of the year, kingship indicator, god-talkers' forecasts and omens; you allocate clan magic across rituals (Crops, Diplomacy, Health, Herds, Mysteries, Quests, Trade, War; later Destiny, Heroism). The game autosaves just before it [V3 manual].
2. **Look at the ring**: tap the faces at the bottom for advice; check skills by tapping a face [V3 manual].
3. **Action 1**: open a screen (Clan, Farming, Magic, War, Diplomacy/Emissary, Trade, Explore, Lore, Saga) and do one thing. A named leader executes it as a test of skill.
4. **The world answers**: raids, bandits, quarrels, spirits, visitors; an authored scene opens with art, text, ring advice, and several responses (five in the fan-wiki examples [V3 kingofdragonpass.fandom.com API, event pages]). You pick; a leader's skill test decides; consequences and a saga line follow [V3 OSL sample https://www.a-sharp.com/kodp/osl.html].
5. **Action 2** (or season wheel). Season changes; Farmers plant in Sea and harvest in Earth without you [V3 manual].
Automated: farming, herding, routine slaughter, patrols, other clans' politics. Interrupts: crises and adventures; "there is no way to duck an event in progress, except by deciding what to do about it"; advisors disagree but "will pursue the course of action you set" [V3 manual].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Consult advisors | none | conditional advice; reveals personalities | constantly |
| Respond to a scene | risk of a failed test | changes mood, relations, herds | constantly |
| Sacrifice to a god for blessing/myth | cattle or goods; under 7 cows hurts the odds, double or triple helps | a blessing or myth knowledge; odds depend on ring Magic skill, a ring devotee of that god, clan magic, omens | every year |
| Build shrine/temple | goods, worshippers, annual sacrifices | permanent blessing | early |
| Heroquest | one quester, risks, prior Quest magic helps only the first quest each year | big reward or injury or lost mysteries | rarely; more than one a year is "extremely risky" [V3 manual] |
| Emissary: gifts, ask favor, alliance, end feud, tribute | gifts; under a dozen cows can hurt reputation | relations, favors | often |
| Trade mission / caravan | goods in transit; bandit risk | cows, goods, horses, trade routes | often |
| Raid / cattle raid | warrior morale; counter-raid risk | plunder, fear | Fire/Storm [V3 manual]; sparingly |
| Recruit weaponthanes / farmers / hunters | gifts, horses | strength, food | as needed |
| Explore | explorer risk | map, discoveries, fewer bandits | early and repeatedly |
| Feast | food | clan mood up | in good times |
| Reorganize the ring | time, mood risk | magic bonuses, who advises | after deaths and rises |
| Farming sliders (wildlands/pastures/cropland), slaughter | labour | food now vs later | when food warns |
| Free or sacrifice thralls | farmer mood | magic vs reputation | rarely |
Source for the rows: [V3 manual sections Magic, War, Emissaries, Missions, Exploring, Farming, Feasting].

#### 4. First hour, step by step
1. Do the questionnaire; read the Lore if you want [V3 manual].
2. Play the one-time tutorial; it only shows on the first play [V3 manual].
3. Reorganize the ring first: it is called a "good, standard opening move" [V3 manual].
4. Spread gods across the ring: duplicates lose Sacred Time slots and heroquest bonuses [V3 manual].
5. Check Farming and the food forecast; "the quickest way to lose the game is to starve your people" [V3 manual].
6. Explore your own tula (do not move the cross) [V3 tips].
7. Send emissaries with gifts to nearby clans and try to end a feud [V3 manual Getting Started].
8. Hire weaponthanes [V3 manual].
9. Open a trade route with a neighbour [V3 manual].
10. Sacrifice for Mysteries to learn a blessing, then build a shrine for it [V3 manual].
11. Handle each scene by reading all advice, then pick the leader whose skill fits; the default list order is by Combat and "not necessarily the wisest" [V3 manual].
12. At Sacred Time put magic where the omens and forecasts point; ignoring them offends the gods [V3 manual].
13. Aim at the Storm Tribe heroquest only after reputation and relations are good; do not rush it [V3 manual; tips].
14. Reading the Saga each year shows what happened [V3 manual].

#### 5. What changes later
Tribe-making (needs three other clans), then a king chosen at a moot; new rituals (Destiny, Heroism), tribal favors and moots, distant raids [V3 manual Tribal Politics]. The Long game adds seven heroquests and unifying Dragon Pass; the story ends with marrying the Horse-Spawn ruler per Wikipedia [V3 Wikipedia plot]. Clans get unmanageable when too big; splitting is the standard fix [V3 tips].

#### 6. Failure and ending
Starvation is the quickest loss; a bad mood can spiral into rebellion; "the clan will go down to defeat" without kingly conduct [V3 manual]. Short game ends the moment you win or lose; you cannot continue into Long [V3 manual]. Recovery: restore to the end of any past year from the Saga screen [V3 manual]. Win Short: three heroquests in 10 years as king, enough cows, neighbours' good opinion; win Long: seven heroquests and unite the tribes [V3 manual].

#### 7. Consequential vs cosmetic choices
- Ring composition (different gods, a healer, a Trickster) drives magic and heroquest odds [V3 manual, ifaq].
- Sacred Time magic allocation and farming/herd health decide survival [V3 manual].
- Relations: favors owed and gifts decide the tribe-making [V3 manual, tips]. 
- Start-up questionnaire answers matter because ancestors "expect" conduct and give a few concrete boosts [V3 manual].
- Cosmetic: art; clan name. Winning "has nothing to do with conquering" [V3 tips], so war-maximising is a trap by design.

#### 8. Open items
- Claim check: "authored-branch selection by stored state" (REPO_MENTIONS s3, relay/G:121). **Verified on the branching, with two limits.** Each scene is an authored OSL script; conditionals read persistent global variables and flags, e.g. `[.mood < 0]`, `[WeLostOurLastRaid]`, `[S52Again > 1]` (an earlier showing of the same scene), and the chief's personality flags, and these gate both text and which advice lines appear [V3 https://www.a-sharp.com/kodp/osl.html]. "Since variables were persistent, one scene... could respond based on what an earlier one had tracked" [V3 https://kingofdragonpass.blogspot.com/2011/02/architecture-overview.html]. Limit 1: outcomes are not branch-selected, they are skill tests: "Tests have two outcomes: win or lose" (a margin variable q) [V3 https://kingofdragonpass.blogspot.com/2011/10/osl-king-of-dragon-pass-scripting.html]; the FAQ says the same choice can come out differently [V3 ifaq]. Limit 2: which scene fires is chosen by the C++ engine ("trigger: from c++"); the public sources say "many have specific preconditions" and some depend on earlier choices, with 544 distinct interactive events; the author's odds calculation assumes every event is equally likely because "there's no good way to figure that" [V3 blog how-many-scenes, fetch summary]; the actual selector and weights are not published [?].
- "Memory of past outcomes": the memory is the persistent variables, not the Saga; Saga text is output to the player (`saga:` writes to the saga file) and is not shown being read back by the engine [V3 osl.html].
- Attachments: grep "Dragon Pass" and "KoDP" in the four attachments: 0 hits ("Dragon Banner" at e3f9f19a:48 is Bannerlord).
- [CONTESTED within the manual]: Short-game win is "three heroquests" once king (Winning) but "the Making of the Storm Tribe quest, then three more" (Heroquests); Long game is "seven different heroquests" (questionnaire) vs the Storm Tribe quest plus seven more; Tips say "Ten times to the Other Side in a long game is easily enough" [V3 manual; tips].
- Not established: exact difficulty names in the current build; per-scene weights; the advice numbers in brackets (`[45]`, `[1236]`) which look like weights or flags [?].
- Capability line (B,F,H,L,M): B1 YES [V3 manual], B2 PART (recruit farmers/weaponthanes/hunters; nobles cannot be recruited) [V3], B3 YES (chief, ring, warleader/lawspeaker by merit) [V3], B4 PART (focus counts; leader per mission) [V3], B5 PART [V3], B6 YES (clan mood, farmer/weaponthane morale) [V3], B7 PART (ring refilled; king on death) [V3]; F1 PART, F3 PART (objective/tactic), F4 PART (round choices), F5 NO, F6 NO, F7 NO, F8 PART [V3 manual War]; H1 YES (scene responses) [V3], H2 YES (like/hate, favors) [V3], H3 PART, H4 YES (alliances, marriage) [V3], H5 PART (tribute, captives) [V3], H6 PART (feuds, no formal war) [V3]; L1 YES [V3], L2 YES (15 years to adult, deaths) [V3], L3 PART [V3], L4 YES [V3], L5 YES [V3]; M1 YES [V3], M2 YES [V3], M3 YES [V3], M4 PART [V3], M5 PART (clan, then tribe) [V3].

### Six Ages: Ride Like the Wind - facts line
A Sharp (leads David Dunham, Robin D. Laws); spiritual successor to King of Dragon Pass. iOS 2018-06-28; Windows/macOS 2019-10-17 (PC publisher Kitfox) [V3 https://en.wikipedia.org/wiki/Six_Ages:_Ride_Like_the_Wind raw, 2026-10-22]. Sequel Six Ages 2: Lights Going Out (2023) continues a victorious save [V3 https://sixages.com/resources/]. This section covers the first game only and mostly states differences from the King of Dragon Pass section; the loop is the same family. Version relied on: the online desktop manual (undated) [V3 https://sixages.com/manual/desktop/Manual-StormAge.html]. Assumed: "Easier" or "Normal" difficulty, a Riders (Hyaloring) clan in the Black Eel valley. Over 400 interactive scenes, over 472,000 words [V3 https://sixages.com/ride-like-the-wind/, resources page]. Sessions: "short episodes and automatic saving mean you can play even when you only have a minute or two" [V3 sixages.com].

#### 1. Setup choices
Questionnaire, no right answers; each choice sets your clan's mythic profile [V3 manual]: **First God** (which sacred stories you know best); **Famous Event** (leaders' skills, e.g. helping Ekarna gives Bargaining); **Ancestral Enemy** (tricks to fight them, and your ancestors expect the enmity kept); **Hyalor** (explains your people's name); **Departure** (the lesser god brought from Nivorah: exotic goods or literacy magic); **Division** (e.g. the warlike branch gives extra elite warriors and the "Elmal Guards the Sunpath" story; the magical branch gives more clan magic and an extra sworn spirit); **Second Migration** (how you treated outsiders, which you will be expected to keep doing); **Difficulty** ("Easier than last time", "About the same as our last migration", Hard, Harsh), which "primarily affects the initial setup"; clan name; and an option to limit your own ability to restore the game [V3 manual].

#### 2. The loop
Same wheel as King of Dragon Pass: Sea, Fire, Earth, Dark, Storm seasons, then Sacred Time [V3 manual]. "In the time it takes to perform two actions, a season passes"; events may occur after each action; the season button forces time on [V3 manual].
1. **Sacred Time**: year summary, divination of dangers, then allocate clan magic across Crafts, Diplomacy, Exploring, Fields, Harmony, Health, Pastures, Ritual, War, Wilds [V3 manual].
2. **Read the Concerns** listed in the menu beside the screen they concern (Houses Unfinished, Limited Fields, Limited Pastures at the start; also Happy Ancestors) [V3 manual].
3. **Act twice** per season on the Clan, Magic, Map, Relations, War or Wealth screens; **one Venture per year** is the big communal project (e.g. Herding, Crafting, Defense, Foraging); the same one cannot repeat within a year [V3 manual].
4. **Crises and Adventures** break in: art, text, advice from the circle; "pick your highest priority response", sometimes a second option; a circle member's skill (and sometimes personality) and luck decide [V3 manual].
5. **Combat** is abstract in most crises; raids use rounds in which both sides pick an option (Advance, Charge, Intimidate, Maneuver, Parley, Reserve, Ritual, Skirmish, then engaged options such as Fight cleverly or Press the attack) [V3 manual].
Automated: farming, herding, patrols, foraging in your own lands [V3 manual].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Consult the Clan Circle | none | advice; personalities colour it | constantly |
| Respond to a crisis | risk | resolves or defers it | constantly |
| Choose a Venture | one per year per type; occupies a leader | herding, crafting, defence, etc. | yearly |
| Sacrifice for blessing or sacred story | 7+ cows of herds/goods for good odds | blessing for a year, or a shrine if you build one | yearly |
| Build shrine/temple | goods, worshippers; annual upkeep sacrifices | permanent blessing | early |
| Bargain with a spirit | persuasion or clan magic | spirit's power for a year or two | occasionally |
| Otherworld ritual | quester risk | big reward or harm; do one at least every seven years | every few years |
| Emissary: gifts, favor, alliance, end feud, tribute | gifts; escorts | relations; alliances beyond about three get hard | often |
| Caravan / trade route | goods in transit | trade partners, market | often |
| Map mission: Explore, Capture Horses, Forage, Search for Spirits | leader and escort risk | map, food, horses, sworn spirits | often early |
| Herd raid / raid | Swords and Bows; counter-raid risk | plunder, fear | Fire/Storm seasons |
| Recruit Swords | gifts, horses | elite warriors (a Sword fights like five Bows) | as needed |
| Reorganize the circle | mood risk | magic points, who advises | after deaths |
[V3 manual, all rows.]

#### 4. First hour, step by step
1. Take the questionnaire; start on Easier or Normal [V3 manual].
2. You "just migrated": houses, fields and pastures are unfinished; plan ventures to finish them over several years [V3 manual Getting Started].
3. Rearrange the circle: seven different gods, ideally all Seven Families [V3 manual].
4. Check that a food shrine exists (Easier guarantees one) and you can feed the clan; without magic you produce about 90% of what you need [V3 manual].
5. Check the Relations screen first for neighbours' attitudes [V3 manual].
6. Establish a few trade routes and learn blessings via sacrifice [V3 manual].
7. Explore your own land and keep enough Swords [V3 manual].
8. Send emissaries with gifts, or propose alliances [V3 manual].
9. Respond to crises using the advice, then check each leader's skills.
10. After several years, perform an Otherworld ritual [V3 manual].

#### 5. What changes later
Alliances cap near three; feuds and honour raids; treasures and exotic goods; the "plot twist" goal is deliberately not spoiled: "you can't force victory" [V3 manual Basics]. Horses (Riders) matter for war strength [V3 manual].

#### 6. Failure and ending
"You can't win if your clan starves"; "few if any situations are so critical that a negative outcome will doom you" [V3 manual]. A finished game, won or lost, stays openable to read its saga [V3 manual]. Restore to the end of any year unless you restricted it [V3 manual]. The goal is survival through the gods' war rather than defeating enemies; "OK to experience the game rather than trying to beat it" [V3 manual Winning].

#### 7. Consequential vs cosmetic choices
- Circle composition: a vacancy costs one magic point a year; a circle with no men or no women generates less; all Seven Families represented gives +1 [V3 manual].
- Sacred Time allocation, especially Fields and Wilds for food [V3 manual].
- The questionnaire: it moves starting herd, mood, spirits and expectations [V3 manual]. Difficulty affects only the setup [V3 manual].
- Cosmetic: clan name; art. Dominant answer: none documented; "Easier or Normal until you have won a game or two" is the official advice [V3 manual].

#### 8. Open items
- Claim check "authored-branch selection by stored state" applies to this series too (REPO_MENTIONS s3: "KoDP / Six Ages"). For Six Ages the manual states the effect ("Some answers will end the situation, others may delay consequences..., still others will cause more events in the future") [V3 manual] but I did not find a source on the scripting; assuming it matches KoDP's OSL is [M]. See the KoDP section 8 for the verified mechanics.
- Wikipedia's Six Ages paragraph repeats KoDP's gameplay text ("seven-member clan ring", "five seasons"); the manual says "Clan Circle" (not "Ring") and the game "drops the warrior-farmer conflict, instead introducing the family politics of the different clan advisors" [V3 Wikipedia; manual].
- Not established: scene count of RLtW beyond "over 400"; per-venture list; endings.
- Attachments: the four attachments contain no Six Ages text ("six ages" matches Dawn of Man's "six ages" at 9226007a:298, unrelated).
- Capability line (B,F,H,L,M): B1 YES [V3 manual], B2 PART (recruit Swords/immigrants) [V3], B3 YES (circle) [V3], B4 PART (ventures, missions) [V3], B5 PART [V3], B6 YES (clan mood, Seven Families) [V3], B7 PART [V3]; F1 PART, F3 PART, F4 PART (round options), F5 NO, F6 NO, F7 NO, F8 PART [V3 manual Combat]; H1 YES [V3], H2 YES (like/hate/fear/mock, favors) [V3], H3 PART, H4 YES [V3], H5 PART [V3], H6 PART [V3]; L1 YES [V3], L2 YES (15 years to adult) [V3], L3 PART (Seven Families) [V3], L4 YES [V3], L5 YES [V3]; M1 YES [V3], M2 YES [V3], M3 YES [V3], M4 PART [V3], M5 PART [V3].
