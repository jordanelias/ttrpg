# T13 - Koei Tecmo and Black Sea: Romance of the Three Kingdoms, Nobunaga's Ambition, Genghis Khan II, Knights of Honor II (v3 tutorial pass, 2026-10-22)

Tags: [V3 url date/version] = read in a fetched page body this session; [S3 url] = search snippet only; [M] = memory, not re-checked; `?` = not established; [CONTESTED] = sources disagree. Capability lines (ids B,D,F,H,L only) use Y/P/N then a suffix: v = verified in a source cited in that section, m = memory, s = snippet, ? = unknown. No v2 capability table exists for these games, so section 8 corrects no v2 cell.
Shorthand (each is a full [V3] tag when followed by a page): **R8** = https://www.koeitecmoamerica.com/manual/rtk8-remake/en/<page>.html (official web manual, fetched 2026-10-22); **R14** = https://www.koeitecmoamerica.com/manual/rtk14/en/<page>.html; **TAI** = https://www.koeitecmoeurope.com/manual/taishi/en/<page>.html; **IA:x** = https://archive.org/download/<x> (OCR text of a scanned manual; OCR is lossy, numbers quoted only where legible). Steam data = store.steampowered.com/api/appdetails and api.steampowered.com/ISteamNews (appid in text). Attachments in /root/.claude/uploads/924794e6-.../: **13G** = e3f9f19a-thirteen_strategy_games.md, **20G** = 89a3a060-consolidated_twenty_games.md (line numbers are file lines).

---
### Romance of the Three Kingdoms (XI, XIII, XIV, VIII Remake) - facts line
Koei Tecmo (Koei); historical grand strategy / officer sim; the series rebuilds per entry, so four short flows below. Versions relied on: **VIII Remake** web manual (base-game text, no Gems/Turning Points) and Steam news: patch 1.1.3 on 2026-03-10, Destiny and Strategy Expansion Pack (power-up kit) released 2026-01-28 [V3 Steam 2288150 news; 3652820 store]; **XIV** 2020 web manual; Steam news shows a JP "with Power Up Kit Complete Edition" released 2026-09-10 [V3 Steam 872410 news], not covered here; **XIII** (Steam page date 2016-01-27 [V3 Steam 363150]; last Steam update note 2020-02-14, Fame and Strategy Expansion Pack bundle); **XI** English PS2 manual (2007) [V3 IA:ps2_Romance_of_the_Three_Kingdoms_XI_USA/Romance_of_the_Three_Kingdoms_XI_USA_djvu.txt] plus Steam "with Power Up Kit" (2018-01-16 [V3 Steam 628070]). Assumed: VIII-R as a common officer, XIII as a created officer, XIV and XI as ruler on a mid-sized force. One session [M]: VIII-R and XIII about 1 to 2 hours per in-game year; XIV and XI about 1 hour per 1 to 2 years; a full unification is dozens of hours. Provenance: VIII-R, XIV, XI from official manuals; XIII mostly one Steam player guide plus press [M] (no official XIII manual found).

#### 1. Setup choices
- **Scenario + start**: every entry picks a scenario (start year, forces). XI PS2 also has Challenge scenarios that end on an objective [V3 XI manual l.378].
- **XI** [V3 XI manual l.370-500]: force/ruler; AI strength Normal or Advanced ("stronger opponent"); Battle Deaths frequency; abilities-age-with-time on/off; female officers Historical or Event-only; Sorcery/Lightning tactics on/off; "Original officer" builder: abilities, equipment aptitudes, special skill, up to 2 sworn siblings, a spouse, a "close friend" (that officer's followers are loyal to you), liked/disliked officers.
- **XIII** [V3 steam 363150 discussion 352788552268657545, 2016-07-19]: any officer playable; a created officer starts at Rank 9 unless playing a ruler; ruler start = 2 free orders + 1 indirect order.
- **XIV** [V3 R14 2300, 2400; V3 gematsu 2019/12]: Tutorial or Start New; up to 150 original officers (importable from XIII on Steam); pick a force (difficulty shown per force); settings: 3 difficulty levels, events, injured-troop recovery, disasters, officer lifespan on/off.
- **VIII-R** [V3 R8 3100; V3 koeitecmoamerica.com/rtk8-remake/system.html]: pick any of 1,000+ officers ("All Officers Play"); the officer fixes your status (ruler, viceroy, governor, tactician, common officer, chieftain, comrade, free officer) and so which commands you hold; scenario settings for disaster frequency, lifespans; the Mar-2026 patch added toggles for Turning Points (expansion) and in-game editing [V3 Steam 2288150 news "March Update Details"].

#### 2. The loop
- **XI** (clock = 10-day turns, 3 per month [V3 XI manual l.691]): 1) Sovereign phase: spend Action Points (max 255, refilled each turn) on city, personnel, diplomacy and unit commands; Technique Points (TP) accrue from commands. 2) Cities set to Auto and districts (Capture Force / Capture City / Auto policy under a Viceroy) act on their own [V3 l.3000-3030]. 3) Press Advance; AI forces and units act; income and upkeep fall monthly (unpaid officers lose loyalty; no food and troops desert [V3 l.1300-1310]). 4) Units meeting on the map fight; duels and debates can interrupt.
- **XIII** [V3 steam guide; rest M]: 1) as an officer you take actions each turn with whatever free/indirect orders your rank grants; 2) ruler/governors/ministers (Rank 7 minister, 5 governor, 2 viceroy) generate more order slots; 3) AI officers act and form bonds on their own; 4) War Councils before battles [S3 gematsu 2016/06; M].
- **XIV** [V3 R14 3200, 3300]: 1) Strategy phase: Orders (renewed each turn from the number of areas held) buy Force/Base/Unit commands. 2) Press Advancement (3 speeds): 10 days run and orders cannot be changed. 3) Reporting phase: income/expense report (income on the first period of each month; supplies every turn). 4) Seasonal events in Jan/Apr/Jul/Oct (locusts, plague spread; Abundant Harvest in autumn). 5) Units fight automatically on contact; duels auto-resolve.
- **VIII-R** [V3 R8 3200, 4100, 4200]: 1) Parliament in Jan/Apr/Jul/Oct: rulers, viceroys, governors spend Strategy Points on policy commands; others suggest; governors assign missions. 2) Three monthly city turns: each action spends Action Points at a facility; Rest advances the month. 3) March in Parliament opens a War Council, then battle: each unit one move per day. 4) Tales and random events interrupt; disasters roll each season.
- Automated everywhere: AI forces, delegated cities/divisions, unit pathing, XIV duels, XIV area development by overseers.

#### 3. The choice menu
| verb | entries / cost | effect | when |
|---|---|---|---|
| Domestic orders (develop, farm, trade) | all; XI AP+gold, XIV 1 Order per change, VIII-R AP+gold per action, mission quota | raise gold/supply/troop income [V3] | constantly |
| Delegate (viceroy/division/Auto) | XI district, XIV division, VIII-R Policy>Create | cuts micromanagement; AI then chooses | each expansion |
| Appoint / rank / title | XI Ranks by Deeds, XIV Title+Administration, VIII-R Appoint | raises abilities and troop caps; XIV also raises stipend [V3 gematsu] | per promotion |
| Search / employ / recruit officers | XI Search+Recruit (Charm vs target Loyalty), XIV People>Search/Employ, VIII-R Employ (CHA; lower loyalty+honor, higher trust helps) | roster growth, the main early lever | constantly early |
| Reward / gift | XI Reward (gold, once per officer per turn, not at Loyalty 100), VIII-R Reward or Punish (specialties) | loyalty up | when a loyalty problem shows |
| Bond actions | VIII-R discuss, gift, banquet (monthly); XIII gifts, wine banquets; XI Oath/Marriage need 500 TP and 500 Deeds each | trust ladder, links, sworn siblings, spouse, children | constantly in officer play |
| Conscript / recruit troops | VIII-R Conscript (gold, order, supply, draft pop. all fall); XIV recruitment overseer; XI Recruit needs barracks | troops now | before war |
| March / attack | all | capture city/base | each war |
| Plots | XI Disrupt, Collaborate, order-lowering; XIV 5 plots; VIII-R Estrange, Destroy, Provoke, Collude, Spy | turn officers, cut order, break defenses | rarely to often |
| Diplomacy | Goodwill, Alliance, Coalition, Solicit, Demand surrender, XI Ceasefire | peace, pressure | rarely |
| Policy / doctrine | XIV Administration (Warlord INT 70+), VIII-R Parliament policy | force-wide modifiers | per milestone |
| Construct / traps | XIV buildings, obstacles, traps on hexes; XI facilities; VIII-R siege weapons via Science | terrain control | as needed |
| Duel / debate | VIII-R card-based duel and debate; XI duels (PUK adds success tuning); XIV auto duels | morale, capture | battle events |
| Train / learn | VIII-R Train, Learn (Wisdom); XI research skills (PUK) | personal growth | officer play |
| Rest / Advance | VIII-R Rest; XIV Advancement; XI Advance | spend the clock | every turn |
| Resign / revolt / rise up | VIII-R Resign, Revolt, Wander, Raise Banner [V3 R8 5100] | change allegiance or become chieftain | rarely |

#### 4. First hour, step by step
1. XIV: Start Menu > Tutorial: four scenarios - Raising Your Country's Strength, Marching and Suppressing, Battle Basics, City Suppression; a Liu Bei / Guan Yu / Zhang Fei story teaches the buttons [V3 R14 2300; V3 gematsu 2019/12].
2. XIV: Start New > pick a low-difficulty force, then read the Warlord's advice in the first Strategy phase (suggestions can be switched on/off; on Beginner they always succeed [V3 R14 4400]).
3. XIV: Base command Domestics > Area Government: give each area an overseer and a priority (commerce, agriculture or barracks); one set of Orders per change; unattended areas lose development each season [V3 R14 4200].
4. XIV: Force command People > Search for free officers; Employ them (INT-rich "Insightful"/"Recruiter" types are faster [V3 gematsu 2019/12]).
5. XIV: March a unit: pick leader, formation, troops (max by officer title), tactics (up to 3), goal, and standing orders (enemy contact, retreat when supply cut, pursuit) [V3 R14 5100]; press Advancement; read the report; repeat.
6. VIII-R: pick an officer. In Parliament, read city gold/supply/troops, and as a non-governor volunteer for a mission in your best stat (Farmland POL, Market POL, Workshop INT, Castle Gate LEA, Garrison STR) [V3 R8 4100, 4200].
7. VIII-R: in the city spend Action Points on the matching domestic action; at 200% of quota you are commended, under 20% reprimanded and may be demoted [V3 R8 4200].
8. VIII-R: Inquire at facilities to raise public attitude (events, Wisdom, a Symbol of Friendship at 100); talk, gift or hold a banquet at Home to lift trust [V3 R8 5200, 3500].
9. VIII-R: at "Trusting"+ trust a link can fire during domestic actions; four Sympathies make a Synergetic bond; "Devoted" officers can offer sworn-sibling ties [V3 R8 3500]. Rest to end the month.
10. XIII: a Rank-9 officer may make one suggestion to the ruler; earn merit; Rank 7 = Minister (+2 indirect orders, +free order if the stat is 90+), Rank 5 = Governor, Rank 2 = Viceroy [V3 steam guide].
11. XIII: raise rapport to 80, wait for an "emotion" state, accept the quest for a level-1 Friend bond; liked gifts are marked "O" in the gift list [V3 steam guide].
12. XI: set districts for outlying cities, use Search/Recruit, Reward weak-loyalty officers, give ranks (Sovereign > Ranks) and march [V3 XI manual l.3040-3260].

#### 5. What changes later
- XIV: Royal Rank grows with force size and unlocks Civil Service appointments, Surround-and-Conquer, Campaign (Duke) and Adjutants who time their tactics (Regional Governor) [V3 R14 5300, 6100; gematsu]. Doctrine level raises the cost budget and slots per department [V3 R14 4100].
- XI: title by city count - Lt. Governor 2 cities up to Emperor 24 - sets how high a rank you can award [V3 XI manual l.3090].
- XIII: each new governor-and-ministers set adds about 8 order slots; "9 actions" with the first regional ministers, "17" with the first governor set [V3 steam guide].
- VIII-R: Science Texts at Science 1000 and 2000 unlock troop types, siege weapons and tactics; Hero play can end in Region Unification, Interim or Personal endings [V3 R8 3100, 4100].

#### 6. Failure and ending
- VIII-R: unify, or finish an Ending-type Tale (Region, Interim = majority incl. Luoyang, Chang'an, Xuchang, Chengdu, Moling, Ye; Personal); fail if the protagonist dies with no successor (spouse, child, sworn sibling) or no ending by year 350 [V3 R8 3100]. Children join at 16 and can be taken over [V3 R8 3500].
- XIV: win when only your force remains; lose at year 351, with no city or no officer; a dead ruler is replaced from the force's officers [V3 R14 3100].
- XI: unify by war or accepted Solicit; lose at year 351, no officers, or by accepting Solicit [V3 XI manual l.1122]. XIII: [M] unify or reach year limit; not re-checked.

#### 7. Consequential vs cosmetic
- Consequential: which officer/status you start as (it fixes your commands) [V3 R8]; recruiting talent before rivals does [V3 gematsu 2019/12]; public order thresholds 50 and 25 in VIII-R [V3 R8 3200]; matching stat to task.
- Consequential in XIII: loyalty-100 AI officers cannot be poached at all, "doesn't matter if you have 100 INT or are their sworn brother" (one player's report); prisoners' loyalty drops over years [V3 steam guide].
- Cosmetic or dominant (community, not measured): gifting only liked items; banqueting 11-12 officers per city until bonds form [V3 steam guide, one player].
- XIV suggestions always succeed on Beginner [V3 R14 4400]: a difficulty setting that removes a risk.

#### 8. Open items
- Capability lines: B1 Y·v, B2 Y·v, B3 Y·v, B4 Y·v, B5 Y·v, B6 Y·v, B7 P·v (successor/heir by entry); D1 P·v, D2 N·m, D3 Y·v, D4 P·v (order/popularity/loyalty), D5 P·v (Parliament suggestions), D6 N·m; F1 Y·v, F2 Y·v, F3 Y·v (XIV standing orders), F4 P·v (XIV none during Advancement; VIII-R/XI turn-based Y), F5 P·m, F6 Y·v, F7 Y·v (XIV supply lines, VIII-R July supply), F8 Y·v; H1 P·v (card debate), H2 Y·v, H3 Y·v, H4 Y·v, H5 P·v, H6 P·v; L1 P·v (traits/Resolve-like), L2 Y·v, L3 Y·v (VIII-R spouse/children), L4 P·v (Tales, events), L5 Y·v.
- CLAIM "RTK XIV: 141 Individualities" (13G l.60 and l.599 [UNVERIFIED]; 20G l.211): SUPPORTED as a shipped count of trait entries: a launch-day fan guide dated 2020-01-16 lists exactly 141 entries, from unique ones (Cao Cao's Treacherous Hero) to "Weak" [V3 https://www.gamersky.com/handbook/202001/1254628.shtml, my count of the contiguous list = 141]. The English manual calls them "traits" and "character" (Insightful, Recruiter) [V3 R14 5100; gematsu], not "Individualities"; whether later patches/PUK changed the count `?`.
- CLAIM "Area Overseers cost a per-turn stipend; expand and suppress territory at a rate set by stats and traits" (13G l.60, 20G l.167): PARTLY. Panel path and stat dependence verified: "Domestics" base command > Area Government; LEA -> public order, STR -> barracks, INT -> commerce, POL -> agriculture, CHA -> conquering land; Conquer Land is auto-conquered "at the start of the Strategy phase"; a change costs 1 Order [V3 R14 4200]. No stipend line for the overseer role was found: stipend rises with the officer's Civil Service/Title (Greedy x2, Unselfish x0.5; lowering a service lowers loyalty) [V3 gematsu 2019/12]. "Suppress" territory not found. Expansion also needs a unit to march.
- CLAIM "RTK VIII Remake: Parliament every three months; Relationship Chart" (13G l.55): VERIFIED: Jan/Apr/Jul/Oct [V3 R8 3200]; chart + 7 trust levels (names partly image-only, lowest Hostile, "Unaware" until met, "Trusting", "Devoted") [V3 R8 3500]. Whether the original 2001 VIII had it: `?`.
- CLAIM "XIII: Bond system, upper tiers produce permanent loyalty" (13G l.59): tiers verified as graded, loyalty effect NOT found. [CONTESTED] numbering: one player: rapport 80 -> L1 Friend, rapport 100 -> L2 Best friend, L3 slow, L4 on gift [V3 steam 352788552268657545]; another: sworn/special bonds are L5, marriage and oath L4 [S3 steam 1726450077695067442]. Press says bonds give aid in battle and debate credibility, not loyalty [V3 gematsu 2016/06]. A player: LOY 100 cannot be recruited even by a sworn brother [V3 steam guide].
- CLAIM "sworn siblings and spouses become non-defecting (RTK XI)" (13G l.192 B3; 20G l.171): PARTLY. XI manual: you cannot employ an officer of another force "with their sworn siblings or spouses", yet those siblings/spouses "may be able to recruit them" even at Loyalty 100 [V3 XI manual l.2739-2742] - an anti-poaching rule, not a ban on defecting; a 2008 forum snippet says same-force sworn brothers "will not defect" [S3 the-scholars.com t=19870]. XIII player says the opposite (sworn brother cannot recruit LOY 100) - [CONTESTED] across entries.
- CLAIM "mass resignation after ruler's death; opposite-compatibility officers bleed loyalty" (13G l.58): not found in the XI manual; XI shows liked/disliked officers (relatives who quarrel, e.g. Cao Pi / Cao Zhi) [V3 XI manual l.612]. `?`.
- REPO CLAIMS (REPO_MENTIONS s.3; research/valoria_game_precedent_companion_v1_part5.md:80,120,148; troop-stock-design.md:670): "order<25 blocks conscription": VERIFIED for VIII-R: below 50 = unrest (fewer conscripts, no soldier income), below 25 = revolt, conscription unavailable [V3 R8 3200]; Conscript lowers gold, public order, supply balance and draft population [V3 R8 5100]; schemes that lower an enemy city's order to block conscription are advertised [V3 koeitecmoamerica.com/rtk8-remake/system.html] (Provoke, R8 5100). "Eight domestic commands, each keyed to one of four stats, flat 10 gold per officer": NOT FOUND in VIII-R: five domestic actions keyed to POL, POL, INT, LEA, STR (four stats) over eight city facilities (Home, Palace, Tavern, Farmland, Market, Workshop, Castle Gate, Garrison); gold and AP are consumed but no amount is printed [V3 R8 4200, 5200]; the claim may come from the 2001 original or another entry `?`. "Commerce, Cultivate and Conscript all drop Safety": only Conscript confirmed in VIII-R. "LOY recruiter tell <=70": NOT FOUND in the VIII-R, XIV or XI manuals (VIII-R Employ: lower loyalty and honor and higher trust make it easier; XI: Charm vs Loyalty [V3 XI manual l.3214]); only a speculative RTK VII forum reply about 70 [S3 the-scholars.com p=550449]. `?`
- RTK XI espionage (REPO_MENTIONS: "not retrieved"): XI Strategy commands exist: Disrupt (break two forces' relations), Collaborate (isolate a Prefect/Viceroy; Intelligence vs Ambition and Loyalty), and a command lowering a force's Order and Loyalty [V3 XI manual l.3314-3332].
- Not settled: XIII loop details, durations, VIII-R PUK systems (Turning Points, Gems, abdication, "Induce" to found a vagrant army, "Sever" to dissolve sworn/marital ties [V3 Steam 2288150 news, JP text]).

---
### Nobunaga's Ambition: Sphere of Influence / Ascension / Taishi - facts line
Koei Tecmo; Sengoku-era historical grand strategy (the series' 14th and 15th mainline entries). Versions: **Sphere of Influence (SoI)** Steam 2015-09-01 [V3 Steam 392470]; **Ascension** (officer play) Steam page 2016-03-23, Western release 2016-10-25 [V3 Steam 375450; V3 tech-gaming.com/nobunagas-ambition-ascension 2016-10-29], patch 1.0.8.2 on 2016-10-26 [V3 Steam 375450 news]; **Taishi** Steam 2017-11-29, last update note 2019-06-03 (with Power Up Kit) [V3 Steam 628890 news], official web manual dated 2018-06-05 [V3 TAI index]. Assumed: Taishi as a daimyo and Ascension as a retainer; SoI as the shared base. One session [M]: roughly 1 hour = 6 to 12 in-game months while learning; a 1551-1615 campaign is tens of hours. Provenance: Taishi is fully from the official manual [V3 TAI]; SoI and Ascension come from OCR of the Steam Chinese manuals (heavily garbled, so only legible phrases are used) [V3 **IA:PK** = IA:nobu-14-pk-steam-manual/Nobu14PKManual_djvu.txt (SoI); **IA:SR** = IA:nobu-14-sr-steam-manual/NOBU14SR_manual_TC_djvu.txt (Ascension); their line numbers are lines of my whitespace-collapsed copy, so search the quoted phrase, not the number], the Steam store text and two Ascension reviews; the monthly flow is therefore best-established for Taishi.

#### 1. Setup choices
- **Scenario and clan**: Ascension ships 21 scenarios spanning 1551-1615 and about 2,000 historical figures; SoI added 4 scenarios (1534 Birth of Nobunaga ... 1600 Sekigahara) and about 500 officers [V3 tech-gaming; V3 Steam 392470]; Taishi 2,000+ officers and a single 3D map [V3 Steam 628890].
- **Who you are** (Ascension): either a pre-built "officer play" life (four random officers offered, reroll allowed) or a normal scenario as daimyo; retainer play starts at the bottom [V3 tech-gaming].
- **Settings** (SoI/Ascension OCR, partly legible): historical events and Sengoku "chronicle" events on/off; officer lifespan and death-in-battle on/off; fictional "maidens" count as officers or not; in-game editing; auto-pause after the monthly assembly; the Taishi manual adds a Maiden Officers toggle [V3 IA:PK l.150-200; V3 TAI 2300].
- **Edited officers**: SoI/Ascension let you register custom officers (up to 1,000 in the OCR) [V3 IA:PK l.198; garbled].

#### 2. The loop
1. Clock: one turn = one month; four seasons. **SoI/Ascension**: an assembly ("evaluation") opens each month; you issue orders (domestic, diplomacy, "grand works" building) to officers, some of which also cost **labor** drawn from your bases' population; when the monthly gauge fills time moves on; a military council can be held alongside [V3 IA:PK l.301, 365, 532]. Rations arrive in September, with smaller payouts in Mar/Jun/Dec if you hold fields [V3 IA:PK l.380; IA:SR l.756].
2. **Taishi**: council in Jan/Apr/Jul/Oct: listen to retainers' ideas, approve up to 3; each gives "policy power" of 4 kinds (agriculture, commerce, military, rhetoric); an officer's LEA/INT/POL raises the yield; "Rethink" once, usually worse [V3 TAI 3200]. Then spend it on policies (permanent, linked into upgrade chains) [V3 TAI 3300].
3. Strategy phase: queue Civil/Military/Diplomacy/Infrastructure/Personnel commands, press **Advance**; time runs, commands execute, you can stop or speed it [V3 TAI 2200, 3100]. Some commands (commerce) are limited per month until a policy raises the count [V3 TAI 2400].
4. Automated: trade-zone income, popularity drift, harvest in September, AI daimyo acting from their own "resolves", disasters (drought, heavy rain, blizzard, typhoon, earthquake, disease) and bounties; low-popularity bases revolt (no farming or recruiting that month) [V3 TAI 2300].
5. Interrupts: rōnin, emissaries and Imperial messengers appear; side-picking requests; invasion alerts (press Advance to stop and order a counter-march); historical events from quests [V3 TAI 2300, 2400].
6. War: Declare War (allies may join either side) > March > battle: you command units each turn in a Command phase; officers suggest tactics; afterwards Blockade or Storm the castle; capturing needs morale or soldiers at 0 [V3 TAI 2200, 2400]. SoI/Ascension battles are plotted on the map with simultaneous execution, plus siege and naval battles and an optional officer view [V3 Steam 392470, 375450].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Agriculture (clear, irrigate, labor exemption) | gold + labor + fertilizer + seeds (shared by all bases, refreshed each September) | farmland, productivity, September harvest; exemption raises popularity but blocks labor commands [V3 TAI 2400] | constantly |
| Commerce: Expand / Invest / Monopolize | gold; Monopolize is expensive | income from trade zones; Expand first, Invest later [V3 TAI 2100] | constantly |
| Develop facilities (post/tea/trading/fishing town, reservoir, ranch, forge, patrol post, bulwark, fortress, drill ground) | gold, labor | refugees, popularity, income, horses/muskets, battlefield limits [V3 TAI 2400] | regularly |
| Recruit militia / infantry | militia free but pull farmers; infantry cost gold | strength of the next war [V3 TAI 2400] | before war |
| Trade (provisions, horses, muskets) | gold | stock for marches and special tactics | as needed |
| Goodwill / Negotiate (commerce agreement, alliance, vassal, peace) | gold, opinion | shared trade zones, allies, vassals | each turn |
| Reinforcement / Return | opinion | loan castles' troops for 6 months | in wars |
| Declare war / March | provisions | battle | each campaign |
| Council ideas / Policies | policy power | permanent modifiers | quarterly |
| Personnel: employ rōnin, prisoners, marry, adopt | gold | roster, marriage lock | occasionally |
| Daimyo > Retire | succession | choose to keep the old Resolve or take the heir's [V3 TAI 2400] | rarely |
| Ascension: fulfil lord's orders, build your fief, make proposals, declare independence | merit/"voice", labor, gold | rank ladder, new fiefs | constantly (officer play) |

#### 4. First hour, step by step
1. Pick a scenario that starts you with a low-pressure clan; in Ascension take the interactive tutorial (Hideyoshi and a girl explain chamberlain/lord/daimyo and honor; a five-part lesson on town planning) [V3 tech-gaming].
2. Read your Daimyo's Resolve (bottom bar): two traits, each with up to four effects, effect 4 usually a malus [V3 TAI 2100].
3. Civil > Commerce > Expand: send merchants into dark trade zones in your land first [V3 TAI 2400].
4. Civil > Agriculture early; use Labor Exemption if gold and labor are short, but keep popularity high to avoid revolts [V3 TAI 2400].
5. At the next council approve the ideas with the highest policy power and spend it on a policy that adds commerce actions [V3 TAI 3200, 2400].
6. Goodwill neighbours, then a commerce agreement and an alliance; check View Mode to see who fights whom [V3 TAI 2400].
7. Recruit militia; later infantry; avoid long wars (refugees and popularity drop) [V3 TAI 2100, 2400].
8. Declare war on a weak neighbour you can reach, March, set the strategy in battle prep (e.g. Leader Rush), and Blockade or Storm the castle [V3 TAI 2400].
9. Ascension: do the lord's orders, build your town, earn honor; Castle Lord needs "about 3000 honor" per one player [V3 steam 375450 discussion 312265672106898152, 2016-10-30].

#### 5. What changes later
- Taishi: trade zones merge into a grand trade zone if you hold the whole country and are the only clan in it; vassals; resource-linked policies unlock as retainers or disasters qualify [V3 TAI 2100, 3300].
- SoI/Ascension: corps (several fiefs under a commander who acts on his own judgment), larger fiefs, siege and naval battles, imperial court favour and ranks [V3 IA:PK l.1472, 1483; V3 Steam 392470].
- Ascension ladder: retainer, chamberlain, castle lord, corps commander, daimyo; each rank unlocks commands; castle lords and corps commanders can be offered independence when the clan is in turmoil [V3 IA:SR l.599, 647, 1796-1802].

#### 6. Failure and ending
- Taishi win: hold all bases; or hold over half the countries and issue a war ban in Nijo Palace; or hold half with allies on the rest then ban. Lose: lose all bases; the Daimyo dies with no successor; the calendar reaches 1700 [V3 TAI 2100]. Ascension: your officer's death ends the run; year 1700 also ends it [V3 IA:SR l.640, garbled].
- Recovery: a Retire in Taishi can rewrite Resolve; a lost fief is not recoverable, but a retainer can defect or declare independence [V3 TAI 2400; V3 IA:SR l.1801].

#### 7. Consequential vs cosmetic
- Consequential: Resolve (it gates which policies exist and what AI daimyo pursue) [V3 TAI 2100, 3300]; trade-zone control as the engine of gold [V3 TAI 2400]; popularity feeding revolts [V3 TAI 2100].
- Consequential: kin and marriage: a spouse "won't betray you even if captured" (Taishi); in Ascension a non-relative must raise friendship and marry into the daimyo's family to inherit [V3 TAI 2400; V3 IA:SR l.1801].
- Weak or dominant (community, one thread): gathering the clan's best officers as personal retainers means the AI lord pool never grows [V3 steam 375450 thread, a player's explanation].

#### 8. Open items
- Capability line: B1 Y·v, B2 Y·v (rōnin, prisoners), B3 Y·v, B4 Y·v, B5 Y·v (corps/castle deputy), B6 P·v (visible loyalty bands; hidden-ish disloyalty 100 = defect), B7 Y·v; D1 Y·v, D2 P·m, D3 Y·v, D4 Y·v (popularity), D5 P·v (council approval), D6 N·m; F1 Y·v, F2 Y·v, F3 Y·v, F4 Y·v, F5 P·m, F6 Y·v, F7 Y·v, F8 Y·v; H1 N·m, H2 P·v, H3 P·v, H4 Y·v, H5 Y·v, H6 Y·v; L1 P·v, L2 Y·v, L3 Y·v, L4 P·v, L5 Y·v.
- CLAIM "Ascension: player spends influence points on requests to the daimyo - transferring a retainer, requesting supplies" (13G l.65): SUPPORTED in spirit: rising merit accrues a "voice" resource that is spent on proposals to the daimyo (bigger proposals cost more); proposals "are always accepted" per the OCR note [V3 IA:SR l.1489, 1641-1642; garbled]. "Supplies" not legible.
- CLAIM "retainers held are capped by honour and rank; over-limit costs more influence; house-head promotion needs ~3000 honour" (13G l.65, l.599): PARTLY. The ~3000 figure is the same single player post the attachment tagged T3: "to become a lord you need ~3000 honor" [V3 steam 375450 discussion 312265672106898152, 2016-10-30, JustaGamer]; a 10,000 honor achievement exists [V3 steamcommunity.com/stats/375450/achievements]. The manual says merit from orders promotes you to chamberlain or lord "at a certain level" and gives no number [V3 IA:SR l.599, 647]. A retainer-count cap by honour is not found: the manual caps how many bases a rank governs `?`. Ascension "house head" = Castle Lord (13G wording imprecise).
- CLAIM "Taishi: Resolves = growth type, ideology and unique policies, roughly two bonuses and maluses, resettable at succession" (13G l.66): VERIFIED in shape: 2 traits, up to 4 effects each, effect 4 a malus; policies depend on the Daimyo's resolve; on Retire the heir's Resolve may replace the old, resetting policies and refunding policy power [V3 TAI 2100, 2400, 3300]. "Growth type" and "ideology" are not in the manual text.
- CLAIM "Taishi: trade-route income, seasonal rice-harvest allocation minigame, troop-lending repaid in weapons and food" (13G l.66): trade zones and loan-of-castles reinforcements (6 months) verified; the rice allocation is the shared labor/fertilizer/seed pool refreshed each September; "repaid in weapons and food" NOT found [V3 TAI 2400].
- CLAIM "Sphere of Influence: battles resolve largely on the overworld map" (13G l.64): not supported; Steam text says "simultaneous strategy executions" with dedicated battle fields [V3 Steam 392470].
- Not settled: exact monthly order list of SoI/Ascension (OCR), difficulty options, Ascension's battle deaths flag; Taishi PUK additions.

---
### Genghis Khan II: Clan of the Gray Wolf - facts line
Koei; turn-based grand strategy with three nested displays (province map, Fire-Emblem-like battle grid, unit combat); originally PC-88 1992-07-30, SNES/Genesis in North America Dec 1993 [V3 en.wikipedia.org/wiki/Genghis_Khan_II:_Clan_of_the_Gray_Wolf 2026-10-22]; Steam re-release 2017-06-27, which port it ships `?` [V3 Steam 628160]. Relied on: the US SNES instruction booklet, OCR from archive.org (raw line numbers) [V3 **IA:GK2** = IA:snes_Genghis_Khan_II_Clan_of_the_Gray_Wolf_USA/Genghis_Khan_II_Clan_of_the_Gray_Wolf_USA_djvu.txt], Wikipedia, and reviews [V3 nintendolife.com SNES review; V3 sega-16.com/?p=25752]. The US SNES version removed the "harem" sub-game [V3 Wikipedia]. Assumed: Scenario 1 as Temujin, 1 player. One session [M]: a season takes minutes; Scenario 1 is roughly 10 to 20 hours.

#### 1. Setup choices
- **Scenario** [V3 IA:GK2 l.274-290]: 1 Mongol Conquest (Mongolia, 1184) with four rulers per Wikipedia - Temujin (Mongols), Jamukha, Togril (Keraites), Tayan (Naimans); 2 Genghis Khan (Greater Eurasia, 1206); 3 Yuan Dynasty (1271; Kublai and rivals); 4 World Conquest, unlocked only if Scenario 1 is finished before winter 1214. Non-Mongol nations have fewer relatives and weaker leaders and lack the elite Mongol units [V3 Wikipedia].
- **Players/mode**: one, two, or COM demonstration; choose your nation on the map; whether to watch AI wars and AI unit combat [V3 IA:GK2 l.252-262].
- **Carry-over into Scenario 4**: keep one Advisor and eight Generals from your territory, or only the Home Base's [V3 IA:GK2 l.286-292].
- No difficulty setting is described; the Scenario/nation is the difficulty [V3 IA:GK2 setup l.240-300].

#### 2. The loop
1. Clock: a year is four seasonal turns; Scenario 1 must end before winter 1214 to unlock Scenario 4 [V3 IA:GK2 l.467, 285].
2. Your turn at the Home Base: choose to issue orders yourself or delegate to your Advisor (the Advisor asks approval for each command). Every command costs **Body Points (BP)**; BP refill each season; a ruler's maximum differs by person and falls with age or illness; press B > YES to end the turn [V3 IA:GK2 l.467-490, 705-718].
3. Vassal states: you cannot command them directly. Decree sets policy (labor split among agriculture/herding/specialty/construction, domestic style, investment, military focus, diplomatic stance); governors execute, and orders "will not necessarily be carried out" [V3 IA:GK2 l.752-905].
4. Between your actions the game: collects food every season and taxes in spring, pays salaries, moves AI nations, rolls events (epidemic spring/winter, sandstorm, blizzard, typhoon, drought, abundant harvest, revolt in summer/winter), and ages/kills characters [V3 IA:GK2 l.520-560, 1500-1580].
5. War (you invade, a governor invades, a revolt, or you are invaded): build up to 5 Legions of up to 4 Units (50 gold per Unit), carry food and gold, position on the Battle Display, then fight turns of one day for at most 30 days; where Units touch, the Combat Display opens; winning conditions include routing the first Legion or taking the commander [V3 IA:GK2 l.1620-1690]. You may let a General command or skip watching [V3 IA:GK2 l.1627-1634].
6. Aftermath: prisoners and recruiting talented men, then the next season.

#### 3. The choice menu
| verb | BP cost (Ability E) | effect | when |
|---|---|---|---|
| Decree (policy) | 8 | set labor split, domestic/military/diplomatic policy for a state | every few seasons |
| Advisor draft / Delegate | 10 / 5 | Advisor writes policy; rule delegated | when BP is short |
| Order (Attack, Move, Send, Diplomacy) to a governor | 7, 6, 6, 8 | indirect commands; not guaranteed | constantly |
| Governor / Advisor / General appoint-dismiss | 9 / 9 / 7 | staff states; max 8 Generals | constantly early |
| Prince as General / Marriage / Family | 6 / 6 / 7 | kin who never betray; son-in-law loyal; groom a successor | every generation |
| Recruit / Train / Dismiss Units | 6 / 7 / 8 | draft lowers arms, training and support; max 20 Units per state | before wars |
| Attack / Move / Send | 8 / 7 / 6 | invade; 20 gold per Unit moved | each campaign |
| Labor | 10 | reallocate workers | when economy shifts |
| Give alms / Special tax | 11 / 14 | support up / gold now, support down | emergencies |
| Demand surrender / tribute, Alliance | 10 / 9 / 8 | diplomacy; alliance 1-8 years | rarely to often |
| Trade and mercenaries (Sell, Buy, Mercenary) | 6 each | only when merchants are present | occasionally |
| Info | 0 | read states and characters | every turn |
Costs scale with the acting character's Political ability letter (A cheapest, E dearest) [V3 IA:GK2 l.489-492].

#### 4. First hour, step by step
1. Begin New Game > Scenario 1 > one player > pick the Mongols (Temujin); decide whether to watch AI wars [V3 IA:GK2 l.252-262].
2. Info > State: gold, food, population, economy, land yield, popular support (0-200), culture, climate [V3 IA:GK2 l.496-560].
3. Info > Ruler, Advisor, Generals: Politics, War, Command, Charm letters, current/maximum BP, age [V3 IA:GK2 l.660-720].
4. Do your own orders at first - a reviewer found the starting Advisor poor [V3 nintendolife review]; spend BP on a Decree that sets your labor split.
5. Recruit Free Generals (up to 8; 7 BP each); make a trusted one Advisor or Governor [V3 IA:GK2 l.380-410, 935-950].
6. Use Family/Marriage to groom an heir; sons become eligible as Generals or Successors at ten [V3 IA:GK2 l.400-420].
7. Recruit/Train Units; check the cap of 20 per state [V3 IA:GK2 l.1010-1030].
8. Attack a neighbour: pay 50 gold per Unit, form Legions, set food, position, and play or auto the battle [V3 IA:GK2 l.1620-1690].
9. Handle the postwar menu, then press B > YES; watch the seasonal event log.
10. Keep popular support up with alms; a draft or special tax makes it plummet [V3 IA:GK2 l.558-566].

#### 5. What changes later
- More vassal states mean more governors who may "proclaim their independence"; kin governors never do [V3 IA:GK2 l.360-366]. Direct control stays at the Home Base only.
- BP shrinks with age; the ruler dies and a prince succeeds (a son who is also a Governor makes his state the new Home Base; the new ruler has no children at first) [V3 IA:GK2 l.410-416, 705-718].
- Scenarios 2 to 4: larger Eurasian map, merchant types (Uighur, Islamic, Chinese, Venetian), regional unit types (sixteen kinds), alliance diplomacy [V3 IA:GK2 l.1090-1110, 390].

#### 6. Failure and ending
- Lose: the ruler is defeated with no Successor (a son aged 10+), or becomes a rival's vassal [V3 IA:GK2 l.133-136]. A revolt can turn a state into an independent nation if the rebels win [V3 IA:GK2 l.1571-1577].
- Win: Scenario 1 conquer Mongolia; others conquer Eurasia [V3 IA:GK2 l.128-132]. Recovery: pick a successor; no save slot beyond one (saving erases the previous) [V3 IA:GK2 l.300-305].

#### 7. Consequential vs cosmetic
- Consequential: the BP budget and who holds it (Politics letter and age) [V3 IA:GK2]; marriage/kin placement (the only visible way to guarantee a governor) [V3 IA:GK2 l.364, 408, 953].
- Consequential: popular support, because draft and taxes drain it and revolts come at low support [V3 IA:GK2 l.1571].
- Cosmetic: naming children, message speed, watch settings. Dominant choice (reviewers, not measured): do your own orders early; use a general who is a relative [V3 nintendolife review; M].

#### 8. Open items
- Capability line: B1 Y·v, B2 Y·v, B3 Y·v, B4 P·v, B5 Y·v, B6 P·v (no loyalty meter; Charm; support), B7 Y·v; D1 Y·v, D2 P·v, D3 P·v, D4 P·v, D5 N·v, D6 N·m; F1 Y·v, F2 Y·v, F3 Y·v, F4 Y·v, F5 Y·v, F6 P·v, F7 P·v, F8 P·v; H1 N·v, H2 N·v, H3 N·m, H4 Y·v, H5 Y·v, H6 P·v; L1 N·v, L2 Y·v, L3 Y·v, L4 P·v, L5 P·v.
- CLAIM "command budget decays with age: young 13-15, aged 8 or fewer; Politics grade sets commands per season; set policies costs 6" (13G l.96, 20G l.195, l.244): PARTLY. The 13-15 / 8 figures appear in a MobyGames user review that calls them "health points" [S3 search snippet of mobygames.com/game/1927 user-review/2518392; page returned 403, so the 13G quote is unconfirmed here]. The manual calls them Body Points; "Maximum Body Points differ from character to character"; they "may decline" with age and drop with illness/injury; Political ability changes the COST per command, not the pool size [V3 IA:GK2 l.480-492, 705-718]. Decree costs 8 BP at Ability E (6 may be a better letter; unconfirmed) [V3 IA:GK2 l.763]. So "Politics grade sets commands per season" conflates cost and pool.
- CLAIM "no loyalty meter" (13G l.100): VERIFIED as a display fact: no governor loyalty value is shown; visible inputs are state Popular Support (0-200) and each character's Charm ("rebellion and betrayal are less likely to break out against a Ruler with high charm") [V3 IA:GK2 l.556-566, 703-705].
- CLAIM "kinship hard lock" (13G l.99): VERIFIED: a Governor who is a family member "will always remain loyal"; sons-in-law "cannot betray"; Princes "never betray" [V3 IA:GK2 l.365, 408, 954, 964].
- CLAIM "child stats randomly generated at birth; poor roll costs decades" (13G l.100, l.553): not in the manual; `?`.
- CLAIM "[CONFLICT] scenario-1 deadline 1212 vs 1214" (13G l.101): RESOLVED to 1214: the manual says Scenario 4 starts if Scenario 1 is "successfully completed before winter of 1214" [V3 IA:GK2 l.284-286]; Wikipedia says 1212 [V3 Wikipedia]; I trust the manual (primary).
- Not settled: whether the Steam build matches the SNES text; exact random-event frequency; how a Governor's loyalty is computed (hidden).

---
### Knights of Honor II: Sovereign - facts line
Black Sea Games (Steam credits "Black Sea Games, Snapshot Games Inc.") / THQ Nordic; real-time medieval grand strategy, no turns, with optional RTS battles; Windows, released 2022-12-06 [V3 Steam appdetails 736820, fetched 2026-10-22]. Relied on patch 1.8.0 (Steam news dated 2026-10-01; the previous patch 1.7.0 is 2024-01-16) and a community wiki last edited Aug-Sep 2025, so wiki numbers pre-date 1.8.0's espionage and mercenary rebalance. Assumed: single-player sandbox, 1110 AD, a 3-4 province kingdom, default difficulty (its name is `?`). One session [M]: 1-3 hours; a goods victory has been done in under 4 hours [V3 ST:5971]; the sandbox is "dozens of hours" [V3 SN:pre]. Read in full: wiki, patch notes, forum threads, 3 guides/reviews. NOT readable (Cloudflare 403): the official dev diaries, Fandom index pages, PrimaGames, GamerJournalist, Checkpoint; so section 4 is built from guides and the wiki, not from the in-game tutorial text.
Shorthand (each is a full [V3] tag when followed by a page): **WK** = https://knights-of-honor.fandom.com/api.php?action=query&prop=revisions&titles=<Page> (community wiki via MediaWiki API; Royal Court, Kingdom's Resources, Goods and Advantages, Buildings and Upgrades, Settlements rev 2025-09-30; Skills and Traditions rev 2025-08-19). **SN:v** = api.steampowered.com/ISteamNews appid 736820, patch v (gid): 1.0.1 4980448574112734268, 1.0.2 5623338145750710024, 1.1.0 5000716037438923554, 1.2.0 5059267908814646665, 1.3.0 6539831519504031797, 1.4.0 5124582150127135040, 1.5.0 5480373588800786336, 1.6.0 5302486388016585339, 1.7.0 6300039510138146570, 1.8.0 1845383656381201, launch 4979322040035665681, pre (2022-11-30) 4979322040013210374. **ST:nnnn** = steamcommunity.com/app/736820/discussions/0/<id ending nnnn>: 4127=3728450372148484127 (traditions), 5217=3728449142727635217 (army size), 4703=4768836645921784703 (knight cap), 1067=3716062900630981067 (early attacks; [developer] posts), 2566=3711559949630872566 (aging), 3746=3728449142727413746 (mid-game), 9445=4040354734344039445 (auto-calc), 3070=4209245823539783070 (tactical battles), 5971=3834297567119455971 (Emperor vote). **MGW** = magicgameworld.com/?p=127993 (2022-05-11). **GP** = gamepressure.com/S013-amp.asp?ID=19976 (2022-12-10). **NF** = noobfeed.com/reviews/1986/knights-of-honor-ii-sovereign-pc-review (2022-12-04, press copy). **SA** = steamcommunity.com/stats/736820/achievements.

#### 1. Setup choices
- **Era and kingdom**: start in 1110, 1224 or 1360 AD [V3 NF; SN:launch "three different starting eras"], then one of 200+ realms (kingdoms, duchies, sultanates, caliphates, an early republic) across 300+ provinces [V3 Steam appdetails]. Size is the real difficulty: the developer advises a 3-4 province start over a one-province start [V3 ST:1067 developer, 2022-12-06].
- **Difficulty**: Easy, Hard and Very Hard are named; Normal is `?` [V3 SN:1.0.1; ST:4127]. It sets how long the AI's opening grace period lasts (longer on Easy, shorter on Hard/Very Hard) and how readily AIs declare war on you [V3 SN:1.0.1].
- **The king**: his class (marshal, merchant, diplomat, spy or cleric) is chosen before the start and cannot be changed; his aging speed runs slow to fast; princes are educated into one class from birth [V3 NF].
- **Victory rules**: Emperor of the World, all eight Kingdom Advantages, or conquer the map [V3 NF; MGW]; a "Minor Victory" setting also exists, contents `?` [V3 SN:1.3.0 fix note].
- **World shape**: "Kingdom Size" rule incl. Shattered World (every kingdom starts equal; no trade centers, vassals, autocephaly or caliphate), five "Kingdom standings" modes up to "Balanced" and "Historical" [V3 SN:1.3.0]; max building slots per province, up to 18 [V3 SN:1.5.0].
- **Multiplayer** (not covered): up to 6 players; First Blood, Peasants Rush, Destroy Kingdom, Greedy King, War for Goods; length by time or generations [V3 Steam appdetails; SN:pre; SN:1.4.0].

#### 2. The loop
1. Clock: real time on the world map, pausable; speeds up to 10x [S3 search snippet, source page not identified]. Only the king ages and dies (knights never age); an heir takes over, and a king's death and a dynasty change both cost stability or crown authority [V3 ST:2566; WK Kingdom's Resources].
2. Each tick the game accrues six resources: gold, books, faith, levies (stocks with income), food (supply minus army demand) and commerce (a capacity you allocate, not spend) [V3 WK Kingdom's Resources].
3. You select a knight (hotkeys 1-9) and give him a standing action: govern a province, lead an army, trade with a kingdom, improve opinions, infiltrate, preach [V3 MGW; WK Royal Court]. Knights also raise timed "opportunities" you take or ignore [V3 NF; SN:1.8.0].
4. The game sends messages (join a war, marriage, trade, crusade); court members show thumbs up/down; your answer moves class opinions and relations [V3 NF].
5. War: a marshal's army marches, sieges the capital and occupies. When armies meet you fight a tactical RTS battle (the world map pauses) or let the game simulate it ("auto-calc"); up to four armies join one battle [V3 ST:3070, ST:9445; SN:1.1.0 "simulated siege"; Steam appdetails].
6. Automated: population growth, construction, wages, inflation, army supply, AI kingdoms (wars, pacts, plots), trade once a merchant is assigned, and rebel population when stability is low [V3 WK Kingdom's Resources; SN:1.5.0].
7. Interrupts: war declarations, rebellion-warning icons, spy incidents, king death, the Emperor-of-the-World vote [V3 SN:1.5.0, SN:1.7.0, SN:1.2.0]. Messages stack on screen and a right-click dismisses one [V3 MGW].

#### 3. The choice menu
| verb | cost | effect | when |
|---|---|---|---|
| Hire a knight | gold 200, 500, 800, 1100, 1400, 1700, 2000, 2300 for the 1st to 8th of one class, plus rising wages (merchants: none) [V3 WK Royal Court] | fills 1 of 8 slots; class sets verbs and governing bonus | constantly early |
| Assign a governor | free; ties the knight to one province | governed = 100% of the province's resources, ungoverned "a tenth" [V3 WK Royal Court] | constantly |
| Exile a knight | class opinion drop (exiling a merchant lowers Merchants) [V3 NF, GP]; none with the Rhetoric tradition [V3 WK Skills and Traditions] | frees the slot; kings and princes cannot be exiled | occasionally |
| Learn / improve a skill | books plus gold, rising per level; learning is far cheaper than improving [V3 WK; MGW] | 5 skills x 3 levels per knight | constantly |
| Adopt a tradition | books + gold scaling with count; needs a knight with that skill at max [V3 WK] | kingdom-wide bonus; kept until abandoned | every few levels |
| Build / upgrade | gold + goods + time; 4 slots, the 5th costs 2000, each further +2000 [V3 WK Buildings and Upgrades] | an upgrade applies in every town with the building | constantly |
| Trade agreement | commerce allocated; a merchant must be assigned [V3 GP; WK] | gold, goods import | early, often |
| Diplomat actions | gold, ongoing upkeep | improve opinions, defensive pact, invasion plan, marriage, peace [V3 NF; WK] | often |
| Spy mission | gold; risk of exposure and prison [V3 WK] | vision, ruin relations, sow dissent, bribe, murder; costs rebalanced 1.8.0 [V3 SN:1.8.0] | mid-game on |
| Raise Crown Authority | gold + faith, scaling with size [V3 WK] | -5..+5 bar: taxes, espionage defense, stability | occasionally |
| Recruit squads / call to arms | levies, gold, workers, food upkeep [V3 GP; WK] | a marshal leads 8 squads, other knights 5 [V3 WK] | before wars |
| Audience: declare war / peace | relations, pact chain, war exhaustion [V3 MGW; NF] | peace with one pact member means peace with all | rarely |
| Fight or simulate a battle | attention versus losses: "lots of losses" in auto when outnumbered [V3 ST:5217] | outcome of a field or siege | each battle |
| Pay off / crush a rebellion | gold plus ceded conquered provinces [V3 SN:1.7.0]; or marshal Establish Order [V3 WK] | restores order | when stability fails |

#### 4. First hour, step by step
1. Pick 1110 AD and a 3-4 province realm (or Easy) [V3 ST:1067]; choose the king's class now, since it cannot change and a merchant king earns more trade income [V3 NF; WK Royal Court].
2. Pause. Read the HUD: court at top centre, resources top right, crown authority and five class opinions top left [V3 WK]. The in-game tutorial pops text on first use of a feature, with hotspots while holding ALT [V3 NF; SN:1.1.0].
3. Open each province: its 4-5 settlements set what buildings are worth (castles: levies, villages: gold and workers, religious: books and faith, crop farms: food); features unlock goods [V3 WK Settlements (KoH2)].
4. Hire a merchant (no wage; early gold) and a marshal (defence against bigger neighbours); if gold is short, family members can fill slots [V3 NF; WK Royal Court; GP].
5. Make each knight a governor where his class pays: marshals in castle-heavy provinces, merchants where goods and villages are many; aim for as many knights as provinces [V3 GP; MGW].
6. Spend books on a first skill (learning is far cheaper than improving, so a knight reaches level 5 quickly) [V3 MGW]; one player's tier list puts Writing, Archery, Learning and Logistics first, unmeasured [V3 ST:4127].
7. Build in the district your settlements favour; keep one province as the recruiting base [V3 GP].
8. Sign trade agreements and assign the merchant, or the route earns nothing [V3 GP]; early non-aggression pacts are advised [S3 PrimaGames beginner-tips snippet, page returned 403].
9. Watch food: a negative balance cuts army opinion, stability and growth; do not field more squads than you can feed [V3 WK Kingdom's Resources; MGW].
10. Before the AI's grace period ends, use a diplomat for a defensive pact or better relations [V3 ST:1067 developer].
11. Answer the first messages; check the thumbs and the opinion bars before refusing [V3 NF].
12. Attack a weak neighbour: march, siege, occupy; a cleric's Adopt Population ends disorder, then put a governor on the town [V3 WK Royal Court; Steam news gid 2579938650944908417, 2020-03-11].

#### 5. What changes later
- More provinces than seats: nine seats cap governors, wage cost climbs with each same-class hire [V3 WK]; the AI "always tries to govern all provinces" [V3 SN:1.5.0]. Players report mid-game boredom near 15 provinces and, at 100 provinces, war fatigue of -90 and constant AI declarations [V3 ST:3746, community].
- New layers: religion (Pope, crusades, excommunication, caliphate) [V3 SN:1.4.0], vassal types Scutage, March, Sacred Land [V3 SN:1.6.0], the great-power rankings and Emperor vote; the developers say espionage matters most for small kingdoms and again once rivals are large [V3 SN:1.8.0].
- Pressure: out of supply is -30% speed, -75% archer salvos, -50% cavalry attack, -12 morale abroad [V3 SN:1.6.0]; religious and cultural stability penalties cap at 25 and 10 [V3 SN:1.7.0].

#### 6. Failure and ending
- Lose: what a single-player defeat screen requires is `?` (not stated in any page read). Realms sink through low stability: rebellious population, rebel armies, independence bids; 59.1% of players have beaten a rebellion by force [V3 WK Kingdom's Resources; SA]. Recovery tools: pay off rebels, Establish Order, peace, vassalage [V3 SN:1.7.0; NF].
- Win: Emperor of the World (about eight great-power voters, each worth 100-150 points toward a ~6k bar, scaled by relations; bigger armies and royal marriages sway votes) [V3 ST:5971, community]; all eight Kingdom Advantages, each a fixed goods set whose bonus lapses if a good lapses [V3 WK Goods and Advantages]; or conquer the map [V3 SN:1.8.0]. Whether play continues after a win is `?`.

#### 7. Consequential vs cosmetic
- Consequential: who sits in the eight seats and who governs; a governed province yields about 10x an ungoverned one and each extra same-class hire costs more [V3 WK]. One poster calls the cap a bottleneck forcing marshals over other classes; another calls that "plain stupid lie" [CONTESTED, V3 ST:4703].
- Consequential: the food-levy-supply economy, because it caps army size [V3 WK Kingdom's Resources; SN:1.6.0]; and the five opinions plus crown authority, which feed stability and espionage defense [V3 WK].
- Dominant answers, community consensus not measured: Writing first, Archery and Logistics rated S+, marshal-heavy courts, manual fights against AI swarms [V3 ST:4127, ST:5217].
- Cosmetic or optional: tactical battles are "the spice"; one 2,000-hour player fought two [V3 ST:3070]; renaming (F2), camera and the 1.8.0 alternative battle view.

#### 8. Open items
- Capability line: B1 Y·v, B2 Y·v, B3 Y·v, B4 Y·v, B5 P·v, B6 P·v, B7 Y·v; D1 P·v, D2 P·v, D3 P·v, D4 Y·v, D5 P·v, D6 P·v; F1 Y·v, F2 Y·v, F3 P·s, F4 Y·v, F5 Y·v, F6 Y·v, F7 Y·v, F8 Y·v; H1 P·v, H2 Y·v, H3 Y·v, H4 Y·v, H5 Y·v, H6 Y·v; L1 N·m, L2 P·v, L3 Y·v, L4 P·v, L5 P·v. No v2 table exists for this game, so no v2 cell is corrected.
- CLAIM "nine slots, king plus eight knights, never growing" (13G l.147, l.318; 20G l.131, l.166 say 8): VERIFIED for the base game, 9 seats with the king in the centre [V3 WK Royal Court]; 20G's "8" excludes the king. Not literally never: the UI "now supports adding extra slots" for mods and Workshop mods add knights [V3 SN:1.3.0; ST:4703]. The "capped at eight+king" quote was not found.
- CLAIM "five classes marshal/merchant/diplomat/spy/cleric" (13G l.147, l.210): VERIFIED [V3 WK; Steam appdetails]; a cleric is a Christian cleric, Islamic scholar or Pagan shaman, and shamans (and any knight with a marshal skill) can lead armies [V3 WK Royal Court].
- CLAIM "10% ungoverned income penalty" (13G l.145; "roughly 10% of income" l.206): REFUTED in size. The wiki says kingdoms "usually receive only a tenth" of an ungoverned province's resources, governed provinces give 100% [V3 WK Royal Court; Kingdom's Resources]: a ~90% shortfall. Caveat: community wiki, no patch pinned; goods production needs no governor [V3 WK Goods and Advantages].
- CLAIM "Rhetorics tradition exiles without penalty" (13G l.147): VERIFIED; it is the Rhetoric tradition, effect "No penalties when exiling or abandoning a knight", needing a knight with Rhetoric at max level (a diplomat primary skill) [V3 WK Skills and Traditions]; one player rates it "C tier. Overall meh" [V3 ST:4127].
- CLAIM "kings and patriarchs learn skills at max level" (13G l.148): VERIFIED, "max" = skill level 3 (a knight's level is the sum of up to five skills, so 15); princes too under the Learning tradition [V3 MGW; WK Skills and Traditions]. Also checked: "hiring more armies than the kingdom can feed ... decrease the opinion of your kingdom's army" (13G l.149) is a verbatim MGW tip; knights not aging (20G l.166) holds, the developers disabled it [V3 ST:2566, community]; "dismissal is permanent" `?`; "heir disputes can produce civil war" (13G l.146) not found.
- Not settled: Normal difficulty; game speeds and default keys; the auto-resolve formula; stability thresholds; whether wiki hire costs survive 1.8.0; the Emperor vote threshold from a primary source.
