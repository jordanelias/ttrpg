# T12 - Tutorials: Crusader Kings II, Imperator: Rome, Total War: Rome II, Oriental Empires (v3, read 2026-10-22)

Tags: [V3 key] page body read this session; [S3 key] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED]. Shorthand keys (each is a full [V3] tag when followed by a page/gid):
- CK2F = crusaderkings-two.fandom.com `api.php?action=query&prop=revisions` (community wiki; pages revision-dated 2012-2024, mostly written for patches 1.x-2.x). SN-<appid>/SS-<appid> = Steam news API (gid cited) / Steam store API `appdetails`. WP = en.wikipedia.org page via fetch.
- ACOUP = B. Devereaux, "Teaching Paradox: Imperator" parts I, IIa, IIb, IIIa, IIIb, acoup.blog/2024/07/19..08/31 (written on 2.0.x; secondary source, not a developer page).
- R2M = r2enc.totalwar.com/en/manual/single-player/<page>/index.html (official Rome II manual, undated, describes the POLITICS SYSTEM BEFORE Power & Politics). TWW = wiki.totalwar.com (Politics Guide (TWR2) oldid 22707; Patch 15/17 pages). SG-PP = Steam guide "A Comprehensive Guide to the Power & Politics System" by Mouse, steamcommunity.com/sharedfiles/filedetails/?id=1237207803 (posted 2017-12-21, upd. 2018-07-05).
- OEW = orientalempires.fandom.com `api.php` (Oriental Empires Wiki, revisions 2017-2024). MSQ = matchstickeyes.com/2015/06/15/oriental-empires-qa-with-bob-smith/. GH = grogheads.com/interviews/13455 (Oct 2017). SG-OE = Steam guide "Grand Oriental Empires Guide" by Sanvone, ?id=1156684266 (2017-10-11, upd. 2020-11-01).
Not read (blocked, not worked around): Paradox wikis (CK2, Imperator: Client Challenge), totalwar.com blog + Total War Academy (403/security checkpoint), MobyGames (403), Fandom Total War wiki (403). So every wiki number in the four attachment claims is checked against a different source or left unverified. Disclosure: one probe of a third-party reader proxy against the Imperator wiki returned a body; I discarded it unread and used none of it.
Capability ids requested: B,D,F,H,L only (ids as in COMPARE_BRIEF.md). No v2 table exists for these four games, so section 8 "corrections" are fills, not edits.

---
### Crusader Kings II - facts line
Paradox Development Studio / Paradox Interactive; grand strategy + dynasty RPG; released 2012-02-14 [V3 SS-203770]. Relied on the final 3.3.x line (last Steam post: hotfix 3.3.5.1, 2021-09-28 [V3 SN-203770 gid 3936699406887851549]) with the DLC the attachments assume (Way of Life 2014: story-event focus; Conclave 2016: vassal interaction, council power, child education [V3 WP Crusader_Kings_II]). Tutorial case: a Christian count/duke starting 1066, one character. One sitting ~1-3 h, a few decades of game time [M]; a full 1066-1453 run is many sittings [V3 SS "play until 1453"].
EVIDENCE: rule numbers are from the community wiki at the revision dates cited (old patches); the in-game tutorial text, UI layout, speeds and pacing are [M]. Final-patch drift is NOT caught.
Capability line: B1 YES[M] B2 YES[V3 CK2F Hard time? tips: invite characters via search] B3 YES[V3 CK2F Council 2014; Crown Law 2014] B4 PART[V3 CK2F Council: one mission each, councillor sent to a county] B5 PART[V3 same: missions run for months unattended] B6 YES[V3 CK2F Opinion 2018; Army/Levy 2018] B7 YES[V3 CK2F Succession Laws 2018, 11 laws] | D1 YES[V3 CK2F Crown Law] D2 PART[V3 CK2F Army/Levy: per-class tax/levy law multipliers] D3 YES[V3 Council] D4 PART[V3 Crown Law/Demesne: opinion + rebel risk; no single stability bar] D5 PART[V3 Succession Laws: elective, tanistry, patrician] D6 PART[M: imprison/execute/banish; no trials] | F1 YES[V3 Army/Levy; Mercenary Company 2013] F2 YES[V3 Combat & Battle 2014: 3 flanks, commanders] F3 PART[V3 Combat & Battle links an army-positioning page] F4 NO[M] F5 YES(only mode)[V3 Combat & Battle: phases run on their own] F6 YES[M] F7 PART[M] F8 YES[V3 Combat & Battle: retreat at 25% morale, Pursue phase] | H1 PART[M] H2 YES[V3 Opinion] H3 YES[V3 Plots (v1.06b); Council spymaster] H4 YES[V3 Marriage Guide 2020; Casus Belli usage 2014] H5 PART[M] H6 YES[V3 CK2F Casus Belli 2013: 15+ CB types] | L1 YES[V3 Ambitions 2013; Traits 2019] L2 YES[V3 Education 2012: guardian at ~6, adult at 16] L3 YES[V3 Marriage Guide: dynasty, matrilineal option] L4 YES[M] L5 YES[V3 Vassals 2019: AI vassals run plots against you]

#### 1. Setup choices
- Start date: base game 1066-09-15 to 1337-12-31; Old Gods adds 867, Charlemagne adds 769 [V3 WP Crusader_Kings_II]; the end date is 1453 [V3 SS-203770]. Each date fixes which realms/dynasties exist and how big your neighbours are.
- Character and title: any landed ruler on the map; four playable ranks - Count, Duke, King, Emperor [V3 CK2F All about titles 2024-03-01]. This sets culture, religion, starting vassals, claims and effective difficulty (a one-county count under a duke vs an emperor with dozens of vassals).
- Ruler designer / custom ruler exists [V3 CK2F page list, 'Ruler Designer' not read]; game rules and Ironman (no reload) [M]. Multiplayer for up to 32 other players [V3 SS-203770].

#### 2. The loop
Clock: real time with pause, speed 1-5, one tick = one day [M]. You control ONE character; when he dies you continue as the heir [V3 SS-203770 "a succession of his descendants"].
1. Pause, read your character (traits, five skills, gold/prestige/piety), demesne map, court, vassal list [M].
2. Staff the council: Chancellor, Marshal, Steward, Spymaster, Lord Spiritual (Court Imam for Muslims); age 16+; a councillor leading troops cannot do missions [V3 CK2F Council (and council actions) 2014-06-10].
3. Unpause. Each day the engine advances armies, sieges, tax/levy flows, births/deaths/marriages of every NPC; monthly income lands; council missions tick down [M; V3 Council for missions].
4. Interrupts: event pop-ups needing a choice, vassal/faction demands, plots against you, war declarations, invitations and proposals [M]; unpopular kings draw "a swathe of plots" [V3 CK2F Vassals 2019-07-15].
5. War: levies are called, armies move on the map; contact starts an AUTOMATIC battle: Skirmish -> Melee -> Pursue phases, up to three flanks, a flank retreats at 25% morale; you pick commanders/composition, not actions [V3 CK2F Combat & Battle 2014-05-24].
6. Peace is struck on the war's CB terms (e.g. claimant gains title + prestige; loser loses 100-200 prestige) [V3 CK2F Casus Belli 2013-10-11].
7. Death: succession law picks the heir; titles may split (gavelkind) [V3 CK2F Succession Laws 2018-01-31]. Automated: battles, AI rulers, NPC lives, taxes, levy sizes (opinion-scaled) [V3 CK2F Army/Levy (Guide) 2018-05-27].

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Appoint / replace councillor | 0.1 gold/mo salary each; fired ex-councillor keeps a long grudge [V3 Council] | skill added to yours + one mission each | start, then rarely; CONSTANT checking |
| Send councillor on mission (Fabricate Claim, Improve Relations, Sow Dissent, Collect Taxes, Oversee Construction, Train Troops, Uncover Plots, Build Spy Network...) | time away from court; failure can wound/kill or imprison him | claims, opinion, tax +2.5%/stewardship point, levy +25%, plot discovery +10% [V3 Council] | constant |
| Declare war on a CB (claim, de jure, law change, independence, depose, religious...) | 10-year truce after any war but Tribal Invasion; loss -100/-200 prestige; Invasion CB costs 500 piety [V3 CK2F Casus Belli 2013] | gains title/land, prestige | the main expansion verb; constant mid-game |
| Fabricate a claim (Chancellor) | "up to 200 prestige and some money" to press it [V3 Council] | creates a strong claim on a county/duchy | frequent |
| Marry / arrange marriages | gold/prestige; choose who | claims and heirs enter your dynasty; alliances [V3 CK2F Casus Belli (usage) 2014-03-25] | constant |
| Raise levies / hire mercenaries | levy = (base+buildings) x holding factors x levy law x opinion factor; mercs cost gold + monthly upkeep [V3 Army/Levy; Mercenary Company] | the army | each war |
| Build / upgrade holdings | gold + time; do castle-village -> castle-city first [V3 CK2F Making Money 2022] | income, levy, tech | constant early |
| Set succession law (gavelkind, primogeniture, seniority, elective, tanistry...) | must have reigned 10 y, be at peace, no regency, no vassal at war, no count+ vassal with negative opinion; one change per ruler [V3 Succession Laws] | decides who inherits; gavelkind +30% demesne limit, splits realm | RARE, huge |
| Raise crown authority (autonomous...absolute, 5 levels) | -30 opinion for 10 y from all vassals, plus permanent -5 (limited) to -30 (absolute); rebel risk -20% to +20% [V3 CK2F Crown Law 2014-03-03] | bigger minimum levy (page says 0-80%; the Army/Levy page says 0-40% [CONTESTED]), revoke titles, limit vassal wars | RARE |
| Grant / revoke titles | opinion swings; revoking needs limited+ authority [V3 Crown Law] | builds or breaks vassal power | frequent |
| Start / join a plot (murder, claim, depose) | backers, gold; plot time = base/number of backers [V3 CK2F Plots (1.06b)] | removes or replaces someone | occasional |
| Imprison / execute / banish | -20s opinion for known executioner [V3 Vassals] | removes threats | occasional |
| Choose an ambition / focus | ambitions give +1 skill or prestige on success (e.g. "Become Exalted among Men" needs 1000 prestige) [V3 CK2F Ambitions 2013-01-07]; focus is Way of Life [M] | skill growth, event flavour | every few years |
| Choose child's guardian | guardian from ~6 to 16 [V3 CK2F Education 2012] | child's traits/skills | each heir |
| Answer events | varies | traits, gold, opinion | constant (most frequent) |

#### 4. First hour, step by step
Source: the wiki's beginner chapter list and tips pages [V3 CK2F Videos for Beginners 2014-06-29; Hard time? tips 2019-04-05; Making Money 2022]; I did not read the in-game tutorial [?].
1. Pick 1066 and a small Christian count (the wiki's newbie series plays Ireland) [V3 Videos for Beginners].
2. Read the ruler: traits, five skills, age, heir, wife. Skills decide which council job he could do himself [M].
3. Open the demesne screen: note holdings vs limit ("12/7" style readout); each holding over the limit costs -10 vassal opinion [V3 CK2F Demesne 2018-04-13].
4. Fill the council. If your court is thin, press `.` (search character), filter to people who accept an invitation, and import the best skill per post [V3 Hard time? tips].
5. Look at vassals' opinion and your tax/levy law; remember levy = 0% at opinion 25 or less, 100% at 100 [V3 Army/Levy].
6. Build income first (castle village -> castle city), military buildings later [V3 Making Money].
7. Send the Steward to collect taxes in your richest county; the Chancellor to improve relations or fabricate a claim [V3 Council].
8. Open a title page, click "show claimants"; invite or marry claimants to gain claims [V3 CK2F Claims 2017; Casus Belli (usage)].
9. Check the neighbour's strength before declaring: army size, fort level, allies [V3 Hard time? tips].
10. Raise levies, march, win the first battle (flanks matter more than micromanagement) [V3 Combat & Battle].
11. Press the war to a peace; the winner of a claim war takes the title [V3 Casus Belli 2013].
12. Revoke or grant: keep unruly vassals on one title; don't hand duchies out freely [V3 Hard time? tips; How to Stabilize Your Realm 2023].
13. Once you wear a crown, grant duke titles (the series' last chapter) [V3 Videos for Beginners ch. 11]; why and when is [M].
14. Set a succession law before your heirs multiply [V3 Succession Laws].

#### 5. What changes later
Tech is per county and creeps by 0.1 per successful monthly roll; benefit only at whole levels [V3 CK2F Technology (guide) 2015-11-23]. Titles climb to king/emperor; crown-authority and succession-law fights with vassals grow; demesne limit stays binding [V3 Demesne]. Unpopular kings draw plots [V3 Vassals]. Later expansions (The Republic 2013, Horse Lords 2015, The Reaper's Due 2016, Holy Fury 2018 [V3 WP]) and the Mongol invasion [V3 SS-203770] add systems; what they add is [M].

#### 6. Failure and ending
The game ends when the current character dies with no same-dynasty heir, or when all landed count-or-higher titles are lost; at 1453 play continues only as observer. Score = prestige/piety rank against historic dynasties (Capetian, Rurikid, Habsburg top) [V3 WP Crusader_Kings_II]. Partial recovery: lose titles but keep a landed dynasty member - the wiki's "island fortress"/"shield" tips are exactly insurance [V3 CK2F Survival:A guide 2012]. No recovery from extinction.

#### 7. Consequential vs cosmetic choices
- Succession law: moves who holds what each generation; opinion effects are tabulated (gavelkind: oldest child -10 to parent, vassals +5) [V3 Succession Laws]. Consequential.
- Demesne vs vassals: -10 opinion per holding over the limit; vassal opinion drives levy size and revolts [V3 Demesne; Army/Levy]. Consequential.
- Council skill: stat is added to yours and mission success scales with it [V3 Council]. Consequential but replaceable.
- Crown authority: community advice says Medium is the usual sweet spot (one guide author, Meneth) [V3 Crown Law, community consensus not tested]. Dominant-answer risk.
- Cosmetic: dynasty shields/portraits [V3 page names]; many ambition rewards are +1 skill [V3 Ambitions].

#### 8. Open items
Attachment claims (file = /root/.claude/uploads/924794e6-.../e3f9f19a-thirteen_strategy_games.md unless noted):
| claim | file:line | verdict | source |
|---|---|---|---|
| "ducal holy war requires tier-scaled prestige (250/500/1000)" | e3f9:32 (also 89a3 ref. via A1 e3f9:174) | NOT VERIFIED, contradicted in what I read: wiki costs are piety and flat (Invasion CB 500 piety; loss -100/-200 prestige); a snippet gives Holy War 100 piety / religious invasion 250 piety in a 2013 patch [S3 search 2026-10-22]. Tier scaling not found. | [V3 CK2F Casus Belli 2013-10-11; CK2F Piety 2012] |
| truce break "-25 relations from defender's religion, -5 diplomacy for 5 years" | e3f9:33 | CONFIRMED verbatim (plus a prestige hit, 10-year truce on every CB but Tribal Invasion) | [V3 CK2F Casus Belli 2013-10-11] |
| de jure CB limited to "one county at a time" | e3f9:32 | CONFIRMED | [V3 CK2F De jure 2013-12-30] |
| "A king-tier character will have a CB for each county in their de jure kingdom" | e3f9:32 | [CONTESTED by version]: the 2013 Casus Belli page says kingdoms/empires do not provide de jure CBs; a later wiki may differ; not checkable | [V3 CK2F Casus Belli 2013] |
| de jure drift 100 y, kingdoms in/out of empires, not counties | e3f9:32; 89a3:17 "hundred-year drift" | CONFIRMED verbatim; extra rule: an interrupted count runs backwards | [V3 CK2F De jure 2013-12-30] |
| plots "carry a plot-power figure that must clear a threshold to fire" | e3f9:33 | PARTLY: 1.06b page makes plot power cut plot time (base/backers); the ">100 power" threshold is community advice | [V3 CK2F Plots] |
| gavelkind splits realm "among sons" | e3f9:37 | CONFIRMED but "among children" (gender law decides daughters); also +30% max demesne | [V3 Succession Laws 2018] |
| council = Chancellor, Marshal, Steward, Spymaster, Chaplain | e3f9:34 | CONFIRMED (Lord Spiritual; Court Imam for Muslims) | [V3 Council 2014] |
| levies "scale with vassal opinion"; retinues ignore opinion | e3f9:36 | levy half CONFIRMED (0% at <=25 opinion, 100% at 100); retinue half [M] | [V3 Army/Levy (Guide)] |
| ambitions + Way of Life focus + 16-year education | e3f9:35 | ambitions exist from base game (2013 page); education runs birth-16 with guardian from ~6 CONFIRMED; "focus" = Way of Life, page text does not say "focus" [?] | [V3 Ambitions; Education; WP] |
| "You lose only when your dynasty holds no titles" | e3f9:29 | INCOMPLETE: also ends when the current character dies without a same-dynasty heir | [V3 WP] |
Unestablished: in-game tutorial wording; final-patch values for any number above; Focus system numbers; speeds/pacing; retinue rules.

---
### Imperator: Rome - facts line
Paradox Development Studio; grand strategy; released 2019-04-25 [V3 SS-859580]. Relied on 2.0 "Marius" (released 2021-02-16 [V3 SN-859580 gid 4703417046217683306]) as patched to 2.0.5 "Augustus" (2025-04-24 [V3 SN-859580 gid 1797820624465715]); Paradox paused new content in 2021 [V3 SN-859580 gid 4074045878079798909]. Start 450 AUC = 304 BC [V3 ACOUP I]. Tutorial case: a mid-size Republic or monarchy. One sitting ~1-3 h [M].
EVIDENCE: mechanics come from Devereaux's 2024 series (ACOUP, secondary, 2.0.x era, careful but not the developer) and Steam news; the Paradox wiki quotes in the attachments could not be opened. The official Marius tutorial posts are YouTube embeds, only their titles were read. UI flow and pacing are [M].
Capability line: B1 YES[V3 ACOUP IIIa: offices, family marks] B2 PART[M: no hiring screen; characters are born/arrive] B3 YES[V3 ACOUP IIIa: 8 offices + a governor per non-capital region] B4 PART[V3 ACOUP IIIa: offices give stat bonuses, "do not make policy"] B5 PART[V3 ACOUP IIIa: governors pick a flat policy set] B6 YES[V3 ACOUP IIIa/IIIb: loyalty 0-100, disloyal <33] B7 YES[V3 ACOUP IIIa: succession / election / clan chief by government] | D1 YES[V3 ACOUP IIIa: laws gated by senate approval] D2 PART[M] D3 YES[V3 IIIa: 8 offices + senate] D4 YES[V3 IIIa/IIIb: stability, tyranny, legitimacy, civil-war threshold] D5 YES[V3 IIIa: senate factions elect ruler] D6 PART[V3 IIIa: imprisoning, triumphs; no trials] | F1 YES[V3 ACOUP I: levies, legions, mercenaries] F2 YES[V3 IIIa/IIIb: governors command levies; generals] F3 PART[V3 SS-859580 "choose your approach before battle"] F4 NO[M] F5 YES(only mode)[M] F6 YES[V3 SN-859580 gid 4703417046214342068: occupation, forts, engineers] F7 PART[M] F8 PART[M; V3 SN-859580 gid 1797820624465715: commanders can be captured/escape] | H1 NO[M] H2 PART[M: friends/rivals] H3 PART[V3 IIIb: assassination plots exist and cost tyranny] H4 YES[V3 ACOUP I: alliances, defensive leagues, subject types] H5 YES[V3 ACOUP I: feudatory/client status] H6 YES[V3 ACOUP I: war goals priced in war score] | L1 PART[V3 IIIa: personality influence "minor"] L2 YES[V3 SS-859580 "living world of characters", ageing portraits; M] L3 YES[V3 IIIa: major families] L4 PART[M] L5 PART[V3 IIIa: AI office-holders exist; they do not set policy]

#### 1. Setup choices
- Country: a large roster of nations [M]; the government type comes with it - Republic, Monarchy or Tribe [V3 SS-859580; ACOUP IIIa]. Changes your political game completely: republic = senate approval and tyranny; monarchy = legitimacy; tribe = clan chiefs and centralization [V3 ACOUP IIIa].
- Start date 304 BC (450 AUC) [V3 ACOUP I]; difficulty, Ironman, game rules [M]. Content packs (Heirs of Alexander, Magna Graecia, Epirus; Punic Wars free) change available mission trees [V3 SN-859580 gids 4703417046218130059, 2984138620263465428, 3667572003477331318, 3112493747263356150].

#### 2. The loop
Clock: real time with pause on a daily tick [M]; monthly political-influence income, yearly events [M]. The player plays "as" the ruler but is really the state [V3 ACOUP IIIa]. Per cycle:
1. Read the Government screen: ruler, 8 country-wide offices, one governor per non-capital region [V3 ACOUP IIIa].
2. Fill/rotate offices and governors - skill versus keeping elite families content [V3 ACOUP IIIa].
3. Unpause; the engine ticks pops (production, promotion, migration), trade, upkeep, character ageing, loyalty drift [V3 ACOUP IIa, IIIb; tick M].
4. You spend political influence on actions (laws, interactions, diplomacy); in a republic, actions needing senate approval cost tyranny when approval is low [V3 ACOUP IIIa].
5. War: pick a CB and a priced war goal; raise levies by region, legions from the capital, or hire mercenaries; battles resolve themselves after pre-battle tactics; peace is bought with war score [V3 ACOUP I; SS-859580].
6. Interrupts: events, missions completing, revolts when province loyalty hits 0, and a 40-month civil-war countdown if disloyal power base passes the threshold [V3 ACOUP IIIb].
Automated: battles, pop growth/promotion, trade, AI nations, character ageing, elections [V3 ACOUP IIa/IIIa].

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Appoint / dismiss office-holder, governor | free; dismissal blocked if holder loyalty <33 or stability <20 [V3 IIIa] | stat bonus; holder slightly more loyal; each missing family office = -5 loyalty to that family, stacking [V3 IIIa] | CONSTANT |
| Declare war / take war goal | aggressive expansion, tyranny (republic), war exhaustion [V3 ACOUP I] | claims, annexation priced in war score (100 can swallow S. Italy) [V3 I] | frequent |
| Raise levies / legions / mercenaries | levy capacity by region from non-slave integrated pops; casualties refill from manpower [V3 I]; mercs cost gold | the army; levy-heavy governors gain power base [V3 IIIb] | each war |
| Pass / change a law | political influence; tyranny 0.67 per point of approval under 50 in a republic; blocked under 30 [V3 IIIa] | state bonuses | occasional |
| Character interactions (imprison, triumph) | senate approval in republics; tyranny [V3 IIIa] | punish rivals / glory | occasional |
| Build in cities | gold + time [V3 IIb] | production, pop ratios (forum -> freemen, library -> nobles) [V3 IIa] | CONSTANT |
| Promote / move pops; integrate a culture | integration lowers other pops' happiness [V3 IIa] | who can rise to noble; manpower | frequent |
| Governor policy per region | choose one flat bonus/penalty set [V3 IIIa] | output vs happiness | when appointing |
| Strengthen Legitimacy (monarchy) | influence + a little tyranny: "0.02 tyranny for 0.05 legitimacy", stackable [V3 IIIa] | easier succession, loyalty | situational |
| Choose mission-tree objectives | none; the missions push you toward conquest [V3 ACOUP I]; Rome's give claims and free colonies per a reader comment under ACOUP I | claims, bonuses | steady |
| Diplomacy (ally, subject, improve relations) | influence; rank gates leagues (<25 territories) [V3 I] | safety / vassals | frequent early |
| Inventions / traditions | research, [M] | permanent bonuses | steady |
| Lobby the senate by choosing who gets office | slow: office grows power base -> faction seats [V3 IIIa] | which faction elects the ruler | rare, long-term |

#### 4. First hour, step by step
Source: I did not read the in-game tutorial; steps follow the Marius tutorial topics (Warfare, Economy & Trade, Culture & Religion, Characters & Inventions [V3 SN-859580 gids 4703417046214342068, 4059402835306847990, 4059402835310143536, 4059402835317156407], titles only) and the ACOUP walkthrough.
1. Choose a country; keeping the ruler's always-loyal share of power base high is "much easier in monarchies" [V3 ACOUP IIIb].
2. Pause. Open Characters/Government: find the ruler, offices, colored family marks, faction icons [V3 IIIa].
3. Fill empty offices from several families so no family goes "scorned" [V3 IIIa].
4. Open the mission tree and read the first mission; Rome's first one reportedly hands out claims (a reader comment, not the author) [V3 ACOUP I comments].
5. Open the economy view: pops by class (Nobles, Citizens, Freemen, Slaves, Tribesmen), trade, buildings [V3 IIa].
6. Queue buildings that fit what a region should become [V3 IIa].
7. Check the Levies screen: the ruler commands the capital region's levy [V3 ACOUP IIIb]; the rest is raised by region [V3 ACOUP I].
8. Check diplomatic rank and ally with a neighbour before a first war [V3 ACOUP I].
9. Declare a war using a mission claim; priced war score means one 100-point peace can annex a minor [V3 I].
10. Fight with levies; the battle runs on its own after your pre-battle choice [V3 SS-859580].
11. Annex; give the new region a governor; integrate or convert pops [V3 IIa, IIIa].
12. Watch the governor's loyalty and power base - levies he commands raise it [V3 IIIb].
13. Pause conquest for years if aggressive expansion and tyranny climb; the author did so to let them decay [V3 ACOUP I].

#### 5. What changes later
Civil-war threshold starts at 25% disloyal power base, falls to 22/20/17% for regional/major/great powers, and each tyranny point takes 0.12% off [V3 IIIb]. Major families rise from 3 to 4 to 5; major/great powers give generals, admirals and governors -2.5/-5 loyalty [V3 IIIb]. Standing legions bind to commanders [V3 IIIb]. Province loyalty <33 disables interactions; 0 = revolt [V3 IIIb]. Republics can accrue tyranny faster than others, and a strong unhappy "democrats" faction can trap you in a tyranny doom-loop [V3 IIIa].

#### 6. Failure and ending
No scripted loss. The failure state is civil war: after the 40-month countdown a rival tag takes all disloyal characters plus friends and family, their regions and armies; the war has no peace option [V3 IIIb]. Winning can still cripple the state [V3 IIIb]. Province revolts are weaker and act as a brake on expansion [V3 IIIb]. Game ends at a fixed end date (define exists) [S3 magicgameworld search 2026-10-22]; its value [M]. Recoverable by reloading or by shoring up key loyalty within 40 months.

#### 7. Consequential vs cosmetic choices
- Office allocation across families (-5 per missing office, stacking) and who holds levy-commanding posts: decides loyalty and power base [V3 IIIa, IIIb]. Consequential.
- Pace of conquest vs tyranny/aggressive expansion: forced pauses for decades [V3 IIIb]. Consequential.
- Concentrating development and levies in the capital region keeps the ruler's loyal share of power base high [V3 IIIb] - a dominant strategy, as the author calls it.
- Weak: variants of republic "don't matter very much"; governor personality influence is minor; characters do not make policy; pops play basically no role in politics [V3 IIIa, IIa]. Flavour, from one author's view.

#### 8. Open items
| claim | file:line | verdict | source |
|---|---|---|---|
| senate approval slope: nothing above 51, 0.67 tyranny per point below 50 | e3f9:134,180 | CONFIRMED with nuance: text says "falls below 51 ... per point below 50", and below 30 the actions are blocked outright (omitted by the attachment). Source is Devereaux, written on 2.0.x; the wiki value was not read | [V3 ACOUP IIIa 2024-08-24] |
| "four pop types" (20G:130 "Typed pool (4 pop types)"; e3f9:138 "four types") | 89a3:130; e3f9:138 | WRONG for 2.0: five classes - Nobles, Citizens, Freemen, Slaves, Tribesmen. The store page still lists four (citizens, freemen, tribesmen, slaves); DD #90 "New Pop Type" (May 2020, Menander) suggests Nobles came later (inference) | [V3 ACOUP IIa 2024-07-26; SS-859580; SN-859580 gid 3127131079139643913] |
| power base lowers loyalty "by 0.55 per unit" | e3f9:135,194 | NUMBER NOT VERIFIED. Mechanism CONFIRMED: each point of power base lowers loyalty for non-rulers; civil-war threshold is the disloyal share of power base (25% base); republic influence derives from power base | [V3 ACOUP IIIa, IIIb] |
| "even a single disloyal family head might be enough" | e3f9:137 | CONFIRMED in substance (large-power-base individuals can meet the threshold alone) | [V3 ACOUP IIIb] |
| Strengthen Legitimacy "+0.05/mo for 5 y at 10 PI, +0.02 tyranny/mo" | e3f9:134 | PARTLY: "0.02 tyranny for 0.05 legitimacy", stackable; PI cost and 5-year length not seen | [V3 ACOUP IIIa] |
| "tyranny decay does not scale... no easy way to lower it" | e3f9:134,180 | [CONTESTED]: Devereaux says tyranny "drops off relatively quickly" for most governments | [V3 ACOUP IIIa] |
| Appoint Dictator needs 75 senate support + 10 tyranny; loyal characters make "much more political influence"; ambitious-general chain "after 5 years" | e3f9:134,136 | `?` not found in any page I could read | wiki not read |
| war "largely with levies raised from pops rather than standing armies" | e3f9:133 | PARTLY: legions (standing, from capital levy capacity) and mercenaries remain | [V3 ACOUP I] |
| defection is "a threshold crossed at an unpredictable moment" | 89a3:262 | NUANCE: after crossing, Imperator runs a visible 40-month timer, i.e. a legible lag | [V3 ACOUP IIIb] |
Unestablished: daily tick and speeds; in-game tutorial wording; Ironman; end date.

---
### Total War: Rome II (Emperor Edition + Power & Politics) - facts line
Creative Assembly (Feral Interactive co-listed) / SEGA; turn-based campaign + real-time 3D battles; released 2013-09-02 [V3 SS-214950]. Layers I relied on: Emperor Edition (Patch 15, 2014-09-16; "significant improvements to the politics system and civil war mechanic" [V3 SN-214950 gid 521612247341573560]); Power & Politics = free update with Empire Divided, Patch 18, 2017-11-30 ("a huge overhaul to the politics system" [V3 SN-214950 gids 2163281492517404657, 2152021858896590678; TWW Patch Notes (TWR2) oldid 23321]); Ancestral Update/family tree, July 2018 [V3 SN-214950 gid 2838841185433247129]; last Steam post 2023-06-22 (compiler/chat update) [V3 SN-214950 gid 5124581515255017424]. Mode: Grand Campaign. One sitting ~1-2 h = roughly 10-30 turns [M].
EVIDENCE: the official manual (R2M) documents the politics system BEFORE P&P (Gravitas/Bribe/Adopt, no loyalty); P&P details come from one community guide (SG-PP). The Total War Academy and blog pages describing P&P were blocked. Pacing [M].
Capability line: B1 YES[V3 R2M 0036: important-characters column] B2 YES[V3 R2M 0037: recruit candidates, replace commanders] B3 YES[V3 R2M 0037: cursus honorum offices] B4 PART[V3 SG-PP: statesman missions Diplomat/Administrator/Organise Feast] B5 NO[M] B6 YES[V3 SG-PP: party loyalty + influence; R2M 0044b public order] B7 YES[V3 SN-214950 gid 2838841185433247129: family tree; heir M] | D1 PART[V3 R2M 0044: provincial edicts need the whole province; SG-PP: government types] D2 YES[V3 R2M 0039a: global tax, per-region exemption] D3 PART[V3 R2M 0037: statesmen hold offices; no council] D4 YES[V3 R2M 0044b; SG-PP loyalty/risk %] D5 PART[V3 R2M 0037: party influence = share of patrician support; no vote] D6 NO[M] | F1 YES[V3 R2M 0017] F2 YES[V3 R2M 0017/0037: mustering to general; replace commander] F3 YES[V3 R2M TOC: Deploying Your Forces] F4 YES[V3 R2M 0015a/TOC] F5 YES[V3 R2M 0015a: compares unit statistics] F6 YES[V3 R2M TOC: Sieges] F7 PART[V3 R2M 0044: plague attrition; TOC Replenishing] F8 YES[V3 R2M TOC: Morale] | H1 NO[M] H2 PART[V3 R2M 0015a: faction attitude column] H3 PART[V3 R2M 0037: assassinate, rumours, bribe] H4 YES[V3 R2M 0015a: trade, alliances, military access] H5 PART[M] H6 YES[V3 R2M 0015a: peace, formal war declarations] | L1 PART[V3 SG-PP: party traits; R2M ambition] L2 YES[V3 R2M 0037/SN: ageing, deaths, family tree] L3 YES[V3 SN gid 2838841185433247129] L4 PART[V3 R2M 0040: dilemmas] L5 PART[V3 R2M 0037: AI parties try to adopt/rumour you]

#### 1. Setup choices
- Campaign: Grand Campaign or a campaign pack (Imperator Augustus ships with Emperor Edition [V3 SS-214950]; Empire Divided, Rise of the Republic, Desert Kingdoms are later packs [V3 SN-214950]).
- Faction: major (playable) vs minor (not); every faction belongs to one of five cultures - Roman, Hellenic, Punic, Barbarian, Eastern - which sets buildings/units; each has permanent faction traits [V3 R2M 0014]. Rome and Carthage also make you pick a house (family) on the same screen; most factions have 2 parties, Rome/Carthage up to 4 [V3 R2M 0037].
- Difficulty incl. Legendary (no manual saves, autosave each turn and around battles; restricted battle UI) and a separate Battle Realism checkbox [V3 R2M 0015]. Difficulty also shifts party loyalty: Easy +10, Hard -10, Very Hard/Legendary -25 [V3 SG-PP].
- Victory route: military, cultural or economic [V3 R2M 0013].

#### 2. The loop
Clock: turns, one per season (Spring...Winter); no real-time pressure on the map [V3 R2M 0015a]. Per turn:
1. Every character has action points; moving, stance and actions all spend them [V3 R2M 0012].
2. You do anything, in any order: recruit (units muster directly to a general, only troop types of that region, multi-turn queue; mercenaries are instant) [V3 R2M 0017]; build in settlements [V3 R2M 0045]; research; diplomacy; agents; politics; edicts; tax rates [V3 R2M 0012].
3. Press End Turn. The UI locks while AI factions move [V3 R2M 0012].
4. Start of your next turn: upkeep is deducted [V3 R2M 0017]; you may have been attacked and must fight before consolidating [V3 R2M 0015a].
5. Interrupts: events/dilemmas needing a choice [V3 R2M 0040]; political events (an opposition party tries to adopt your man or spread rumours; you can pay to block) [V3 R2M 0037]; any attack opens the battle panel: fight on the 3D battlefield, auto-resolve by comparing unit statistics, or withdraw [V3 R2M 0015a].
6. Politics runs on its own: party influence and loyalty move each turn from gravitas, battles, offices [V3 R2M 0037; SG-PP]. Automated: AI turns, food distribution across provinces, growth, trade wealth from buildings [V3 R2M 0044, 0039a].

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Move / stance (army, fleet, agent) | action points [V3 R2M 0012] | position, ambush, raid, force march [stances: v2 R6, not re-read] | CONSTANT |
| Recruit / muster; disband; retrain | gold now + upkeep each turn; mercs cost upkeep = recruit cost [V3 R2M 0017] | army size | CONSTANT |
| Build / repair / demolish in a settlement | gold + turns; food and squalor limits [V3 R2M 0044, 0045] | income, order, growth, units | CONSTANT |
| Province edict | needs the whole province [V3 R2M 0044] | provincial bonus | occasional |
| Tax rate (global, or exempt a region) | public order [V3 R2M 0039a] | income | frequent |
| Diplomacy (trade, alliance, access, peace, payments, war) | varies [V3 R2M 0015a] | borders, trade | frequent |
| Attack: fight / auto-resolve / withdraw | casualties | the battle | each contact |
| After a siege: occupy / loot / raze | order vs cash [v2 R6 citing r2enc 0021, not re-read; M] | region fate | each conquest |
| Agents: dignitary, champion, spy | gold; dignitaries spread your culture before conquest [V3 R2M 0014] | order, sabotage | frequent |
| Secure Promotion (cursus honorum) | patrician support, then rising gold [V3 R2M 0037]; promoting a RIVAL general gives that party +2 loyalty per level up to 14, while the guide also lists promotions as costing loyalty [V3 SG-PP, internal tension] | gravitas per turn (+ Cursus traits) | occasional |
| Adopt / Bribe / Assassinate / Rumours / Marriage | gold + lost patrician support; leaders cannot be adopted or bribed [V3 R2M 0037] | move gravitas between parties | situational (not CONSTANT) |
| Secure Loyalty (P&P) | cheap: ~1,000 even with 1,000,000 in treasury; +10 loyalty for 5 turns [V3 SG-PP] | stops secession risk | whenever loyalty <0 |
| Purge (P&P) | costs other parties' loyalty; up to +4% influence at once [V3 SG-PP] | influence | situational |
| Statesman mission: Diplomat / Administrator / Organise Feast | 1 turn, loyalty cost, statesman may die [V3 SG-PP] | relations +~20, public order +10, food +4, gravitas | frequent |
| Research | turns [V3 R2M TOC] | tech | steady |

#### 4. First hour, step by step
Source: R2M 0003 says new players should play the Prologue (guided campaign + land + naval) or the video tutorials [V3 R2M 0003]; the rest follows the manual and SG-PP.
1. Play the Prologue to learn campaign, land and naval basics [V3 R2M 0003].
2. New Grand Campaign. First run: choose a faction with only two parties (ruling + one opposition) - the manual says so explicitly [V3 R2M 0037].
3. Open Objectives: read chapter objectives; pick military/cultural/economic route [V3 R2M 0013].
4. Click your capital: queue a building; check food, squalor, public order [V3 R2M 0044, 0044b, 0045].
5. Open Trade & Finance: read projected income; set tax [V3 R2M 0039a].
6. Select your general, press recruit, queue troops from local types [V3 R2M 0017].
7. Pick a first technology [V3 R2M TOC].
8. Open Diplomacy: trade or alliance with neighbours [V3 R2M 0015a].
9. Open the faction panel -> politics: see party influence, traits, loyalty; you are protected from secession for the first 20 turns [V3 SG-PP].
10. End turn; read events/dilemmas [V3 R2M 0040].
11. Attack a weak neighbour; at the battle panel choose fight or auto-resolve [V3 R2M 0015a].
12. After capture decide occupy/loot/raze (v2 R6, not re-read); garrison to hold order [V3 R2M 0044b].
13. Send a statesman on an Administrator mission where order is low [V3 SG-PP].

#### 5. What changes later
Imperium rises with conquest: party loyalty modifier runs +30 at level 1, +25 at 2, -16 at 8 [V3 SG-PP]; political action costs and incident frequency also rise, and your party gains support automatically past level 4, so civil war gets harder to avoid [V3 TWW Patch 15]. Rome can switch republic (-10 loyalty) to empire (+15); unions give -5 [V3 SG-PP]. Extra parties can appear (an event near Imperium III, per one author) [V3 SG-PP]. Pre-P&P, too weak or too strong a party triggered civil war [V3 R2M 0037]; Patch 15 made it a high/medium/low chance per turn from support [V3 TWW Patch 15].

#### 6. Failure and ending
Loss = losing your regions; civil war (pre-P&P: opposition generals defect with armies; Patch 15: all non-family commanders go over; P&P: secession, "Risk %" shown) takes regions at once and no diplomacy is possible with the new faction [V3 R2M 0037; TWW Patch 15; SG-PP]. Victory = your chosen route's ultimate objectives [V3 R2M 0013]. Recovery: reload (not on Legendary) [V3 R2M 0015]; after beating separatists you are protected for about 20 turns (author's belief) [V3 SG-PP].

#### 7. Consequential vs cosmetic choices
- Loyalty upkeep: one community author says influence balance "does not matter anymore" after P&P - no real penalty for maxing influence - and the exploit of purging each turn for the first 10 turns is safe because of the 20-turn grace [V3 SG-PP; single-author consensus]. Consequential, with a dominant answer (cheap Secure Loyalty).
- Party traits (3 per party, random, red/yellow/green) can be devastating; reloading re-rolls them [V3 SG-PP]. Consequential.
- Who commands armies: victories add gravitas to the commander's party [V3 R2M 0037]. Consequential.
- Marriage/divorce/embezzle: the guide author skips them; marriage helps the other party [V3 SG-PP]. Low value.

#### 8. Open items
| claim | file:line | verdict | source |
|---|---|---|---|
| gravitas quote "All the characters in a party contribute, but the effect is relative to the total Gravitas within other parties..." | e3f9:86 | CONFIRMED verbatim, but it is the PRE-P&P guide text (also in the manual); P&P keeps gravitas -> influence | [V3 TWW Politics Guide (TWR2) oldid 22707; R2M 0037; SG-PP] |
| statesmen quote ("same as commanders... don't have a physical presence...") | e3f9:87 | CONFIRMED (found in the manual, not a CA "politics overview") | [V3 R2M 0037] |
| "Party loyalty needs to be managed... New parties can appear..." (CA politics overview) | e3f9:86 | NOT OPENED (Academy 403); consistent with SG-PP and a search snippet "loyalty below zero after the first 20 turns can break away" [S3 academy.totalwar.com search 2026-10-22] | [V3 SG-PP] |
| Entice: >=30 gravitas, +2 cunning over target's authority, -8 loyalty | e3f9:86,196 | `?` NOT FOUND in the manual, the old Politics Guide, SG-PP or the Patch 15/17 notes; those use Bribe/Adopt. "Cunning/authority" stats not seen either. Treat as unverified | [V3 R2M 0037; TWW; SG-PP] |
| secession vs civil war ("more than one rival party, or one with lots of influence") | e3f9:86 | PARTLY: P&P guide treats secession risk with a visible Risk %; Patch 15: civil war = all non-family commanders; the party-count distinction not seen | [V3 SG-PP; TWW Patch 15] |
| "Rome II secession after ~turn 20" | 89a3:168 | CONFIRMED: secession protection for the first 20 turns | [V3 SG-PP] |
| province owned only when every region held | e3f9:85; 89a3:203 | PARTLY: a province is up to 4 regions; the rule found is edicts require the whole province | [V3 R2M 0044] |
| "Rome II's ambition is a multiplier" (called cosmetic) | 89a3:210 | CONFIRMED mechanically as a multiplier on gravitas's effect - not cosmetic: it scales party influence | [V3 R2M 0037] |
| defection "unpredictable" | 89a3:262 | NUANCE: visible Risk % and 20-turn grace make it partly legible | [V3 SG-PP] |
Unestablished: Total War Academy/CA P&P text; Entice; exact loyalty formula; 4-vs-2 turns per year; in-game Prologue steps.

---
### Oriental Empires - facts line
Shining Pixel Studios (R. T. "Bob" Smith, John Carline) / Iceberg Interactive; turn-based 4X with simultaneous turns and auto-resolved real-time battles on the map; Early Access 2016-09-20, full release 2017-09-14 [V3 SS-357310; SN-357310 gids 4249665521682797820, 4249665521682796135]. Layers I relied on: base game as patched to the last Steam post 2021-12-22 (AI tweaks, modding) [V3 SN-357310 gid 4224938027294999052]; DLC Genghis 2018-11-13 and Three Kingdoms 2019-08-29 only touched [V3 SN gids 2423394806014386301, 2415540140456519414]. Mode: The Great Campaign, a farming faction, default 300-turn limit. One sitting ~1-3 h = roughly 30-80 turns [M]; a full 300-turn game is many sittings [M].
EVIDENCE: all rule numbers are from OEW (community wiki, mostly stub-marked, revisions 2017-2024, early builds) and one 2017-2020 Steam guide (SG-OE, a single author); the in-game F1 help and tutorial text were not read, and one 2016 review calls the early-access tutorial "pretty much broken" [V3 WP Oriental_Empires, quoting Kotaku]. Section 4 is therefore my synthesis, not a transcript. Pacing [M]. MobyGames returned a Cloudflare challenge and was not read.
Capability line: B1 PART[V3 OEW Venerable Leaders: only leader, heir and hired characters are individuals] B2 YES[V3 OEW Edicts: Grand Commandant, Enlist a Shi, Appoint a Strategist hire characters; troops come from pools] B3 PART[V3 OEW Unrest: governor = leader/general/chancellor/shi inside city borders; SG-OE comment 2023 says offices exist, not in wiki pages read] B4 PART[V3 OEW Settlement Detail: labour split across farms, roads, clearing, buildings] B5 YES[V3 OEW Player Status: automate research, new settlements, farming; per-settlement Defense/Growth/Income/Military/Culture] B6 YES[V3 OEW Unrest: peasant and noble unrest per city] B7 YES[V3 OEW FAQ: heir, succession crises; OEW Authority: -3 or -9 authority] | D1 YES[V3 OEW Edicts: one per turn] D2 PART[V3 SG-OE 1.7: tax tiers come from edicts, no rate slider found] D3 PART[V3 OEW Edicts: Chancellor, Bureaucrat, Strategist characters] D4 YES[V3 OEW Unrest: 70/80/90/100% thresholds] D5 NO[V3 OEW Diplomacy: "Recognize Emperor" is a bilateral deal; no assembly found] D6 PART[V3 OEW Court: building, -10% peasant unrest; no trials] | F1 YES[V3 OEW Settlement Detail; MSQ: no recruitment queues] F2 YES[V3 OEW UI: stacks of up to 8 units; generals] F3 YES[V3 OEW Battle Plans: 8 plans plus formations] F4 NO[V3 OEW FAQ: no control mid-battle] F5 YES(only mode)[V3 MSQ: battles run on the map at end of turn] F6 YES[V3 SG-OE 2.3: gates and breaches] F7 PART[V3 SG-OE 2.2: readiness bar; SN gid 4249665521682797044: no replenish after a battle] F8 YES[V3 OEW FAQ: battle runs until one side flees] | H1 PART[V3 OEW Diplomacy: audiences, counter-offers; no persuasion] H2 YES[V3 OEW Diplomacy standing screen; SN gid 4249665521682797044: looting lowers liking] H3 NO[M] H4 YES[V3 OEW Diplomacy: Fraternal Harmony 40 turns, Defensive Alliance 50; marriage per SG-OE comment] H5 PART[V3 OEW Diplomacy: vassal, recurring payments 25 turns; hostages/ransom `?`] H6 YES[V3 OEW Diplomacy: war, peace 50 turns, truce 20] | L1 PART[V3 OEW Venerable Leaders: persistent Qi/Ren/Authority, no goals found] L2 YES[V3 OEW FAQ: characters age and die] L3 PART[V3 SG-OE comment: marriage yields characters; no dynasty page] L4 PART[V3 OEW Events, Encounters: randomly generated] L5 YES[V3 OEW FAQ: barbarian invasions, noble and peasant rebellions]

#### 1. Setup choices
- Mode: The Great Campaign (c. 1500 BC-1500 AD, you start with one town, recommended first, "wealth of hints") [V3 OEW The Great Campaign]; The Warring States scenario (407 BC after Jin splits, several cities and techs at start) [V3 OEW FAQ]; custom games on random maps [V3 OEW FAQ], with a starting-era choice since 2018-04-24 [V3 SN-357310 "More multiplayer options"]; multiplayer up to 15 players [V3 SS-357310].
- Faction: Grand Campaign lists 15; five Chinese farmers start unlocked (Shang, Zhou, Han, Chu, Shu), ten more unlock after 120 turns played (Qin, Wu, Min Yue, Ba; herders Dong Yi, Dog Rong, White Di, Xiongnu, Dingling, Xianbei) [V3 OEW Factions, The Xiongnu; OEW UI says 150 turns, [CONTESTED]]. Custom games 20 [V3 OEW FAQ]; store page says 24; Three Kingdoms DLC says 26 [V3 SS-357310; SN gid 2415540140456519414]. Farmer vs herder changes food (farms vs flocks), recruit pool (militia vs tribal) and the Nomadism tech [V3 SG-OE 1.4]. Each faction adds modifiers: Shang +1 starting authority, +20% Power research; Han +10% peasant happiness, crossbow bonus, -10% combat; Chu +20% culture rate, +10% noble happiness; Xiongnu +20% cavalry kill chance, -30% Thought research [V3 OEW Shang, Han, Chu, The Xiongnu].
- Options: difficulty (easy/normal/other names not seen; easy and normal cut labour unrest [V3 SN gid 4249665521682796827]), turn limit (default 300; beginners advised 350-400), research rate (default 100%), "Allow Cultural Victory" (default yes, fixed once started; option added 2016-11-24) [V3 OEW UI Options; SN gid 4249665521682797272].

#### 2. The loop
Clock: turns with simultaneous movement; you plot orders, press End Turn, and every army marches together [V3 OEW Turns]. Years per turn are not fixed; default game is 300 turns [V3 OEW FAQ]. Per turn:
1. Read the message list: events, battle reports (full reports at the start of the next turn), encounter offers [V3 OEW FAQ, UI].
2. Per settlement: allot forced labour (up to 2 families to farms, 2 to roads, 2 to clearing, 4 to buildings), queue buildings, raise troops from the recruitment pools [V3 OEW Settlement Detail Page].
3. Issue at most one edict [V3 OEW Edicts]; pick research (schools: Power, Craft, Thought, Knowledge) [V3 OEW Technology and Culture]; make up to 3 diplomatic offers [V3 OEW Diplomacy].
4. Give each stack (max 8 units) a destination, per-unit battle plan and formation [V3 OEW UI, Battle Plans].
5. End Turn: the game warns about idle units and unchosen techs unless automated [V3 OEW UI]. Armies move, battles play out in real time on the map ("a minute or two", no control), AI factions act, upkeep and growth resolve, unrest is recomputed [V3 MSQ; OEW FAQ].
6. Interrupts: random events (flood, drought, comet, phoenix) [V3 OEW Events]; encounters (a leader must END its turn on the hex; ignored ones lapse 10 turns after opening) [V3 OEW Encounters]; rebellions; leader death; AI offers can wait [V3 SN gid 4249665521682796135].
Automated if toggled: research choice, new settlements, farming, settlement build priorities [V3 OEW Player Status, Settlement Detail Page].

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Labour: farms, clearing, roads | peasant labour -> labour-service peasant unrest; rest turns bleed it off [V3 OEW Unrest] | food, population, tax | CONSTANT |
| Build a building | gold + per-turn upkeep, 1-6 turns with 4 peasants [V3 OEW Buildings] | tax/trade, recruit pools, happiness, culture points | CONSTANT |
| Recruit units | pool, gold, unrest (+1 peasant per militia, +2 noble per noble unit after the first few) [V3 SG-OE 3.3] | army; no queues | CONSTANT |
| Move stacks, set battle plan | free; contact starts a battle | position, sieges, raiding | CONSTANT |
| Pick research | turns; progress kept if you switch [V3 OEW FAQ] | units, farms, authority, culture | CONSTANT |
| Found a settlement | Settlers cost 2 population [V3 OEW Settlers] | new Town: 4 building slots, 80 pop cap [V3 OEW Town] | frequent early |
| Upgrade settlement | City at pop 40 (2000 gold, 8 slots, 160 pop); Huge City at pop 100 (4000, 12 slots, 250 pop) [V3 OEW City, Huge City] | space, range | occasional |
| Issue an edict | gold (0-3000), upkeep, temporary unrest, authority loss if cancelled [V3 OEW Edicts] | permanent law; Well Field System +2 income per farming pop [V3 SG-OE 1.7] | frequent early, then rare |
| Diplomacy deal | 3 offers/turn; Fraternal Harmony 40 turns, alliance 50 [V3 OEW Diplomacy] | peace, vassals, Emperor recognition | frequent |
| Raid, loot, sack | lowers AI liking [V3 SN gid 4249665521682797044]; a razed farm ~50 coins [V3 SG-OE 1.8] | income, damages rival | situational |
| Garrison nobles / station a leader | nobles raise noble unrest +2, cut peasant unrest 8 [V3 OEW FAQ] | local order | situational |
| Era edict | 1000 gold each, +15% noble unrest 10 turns [V3 SG-OE 3.5, 3.6] | unlocks next era's techs, units | rare (twice) |
| Encounter | a leader's trip | tech, authority, units, or a trap | early, rare |
| Move capital / loans | 500 gold / debt [V3 OEW Edicts] | noble-distance penalty / cash | rare |

#### 4. First hour, step by step
Source: no documented tutorial; synthesis of OEW and SG-OE (one author, opinion) plus the six developer beginner videos named on OEW (Resources, Farming vs Herding, Technology, Trading, Authority/Culture/Unrest, Edicts), whose content I did not see [V3 OEW How To Play Guide].
1. New Great Campaign with a starting-unlocked farming faction; keep 300 turns [V3 OEW Factions, UI Options].
2. Scout: send cheap Militia spearmen into fog; walk leaders onto encounter hexes [V3 SG-OE 2.1; OEW Encounters].
3. Open your settlement: put labour on farms, preferring fertile plains (best food per labour-turn) [V3 SG-OE 1.3].
4. Pace labour: build farms to ~40 pop or 40-50 unrest, rest 10-15 turns, then add farms one at a time [V3 SG-OE 1.3, opinion]. Watch the unrest tab; the FAQ says begin prevention at 40% [V3 OEW FAQ].
5. Research first: Flood Control (Power, unlocks Well Field System); Thought opens Shamanism, then Ancestor Worship -> Priest King (authority) or Divination -> Oracle Bones [V3 SG-OE 4.1, 4.3, opinion].
6. Issue Well Field System early: doubles farm income, +10 peasant / -10 noble unrest, cannot be cancelled [V3 OEW Edicts; SG-OE 3.4].
7. Recruit Settlers once population allows; hover the greyed Settle button to see why a site fails [V3 OEW Settlers].
8. Site rules: not on forest, marsh, sand, steep hill, mountain, river or coast, nor beside the last four; cities at least 4 hexes apart; the guide advises ~10 for farmers [V3 SG-OE 1.1; OEW FAQ].
9. Optional single-player trick: found a town (clears adjacent forest/marsh) then disband and reuse the Settlers; the wiki calls it a possible exploit [V3 OEW FAQ, Settlers].
10. Build a Bowyer or Weaponsmith for troops, a Shrine (peasants) or Pavilion (nobles) outside the walls, a Granary around pop 30 [V3 SG-OE 3.3, 2.2].
11. Meet neighbours; trade Fraternal Harmony (no attacks 40 turns) [V3 OEW Diplomacy].
12. Open Player Status (F9) for victory progress and automation switches; end turn, read battle reports, and save often (the FAQ recommends save-reload while learning battles) [V3 OEW Player Status, FAQ].

#### 5. What changes later
Era gates: Bronze Age -> Warring States by edict (needs "enough" Bronze Age techs); -> Imperial by edict (48 techs from the first two eras); each swaps units (dagger-axes to halberds, chariots vanish, nobles only as cavalry) [V3 SG-OE 3.5, 3.6; SN gid 4249665521682796135]. Central Bureaucracy (+2 authority, 500 upkeep) unlocks Salt Tax, Land Redistribution, Imperial University, Civil Service Examinations [V3 OEW Edicts]. Towns grow to 250 pop; trade networks (Bazaar, Quay, Caravansary) become the second income; artillery appears against better walls [V3 SG-OE 1.5, 2.2]. Pressure: settlements above authority add +10% noble unrest each; losing a leader with no heir costs -9 authority fading 1/turn [V3 SG-OE 3.1; OEW Authority]; the AI is "more likely to combine against" a winning player and harder to buy for Emperor recognition [V3 SN gids 4249665521682797044, 4249665521682796135].

#### 6. Failure and ending
Unrest of 90%+ raises the risk that the settlement and nearby armies rebel, and noble rebellions are civil wars inside a faction tied to noble unrest; peasant rebels (Red Eyebrows, Yellow Turbans) strike all factions and the FAQ says they are unrelated to peasant unrest, while OEW Unrest says high unrest spawns bandits and rebellion [CONTESTED] [V3 OEW FAQ, Unrest]. Peasant unrest 100% = no tax; 80% = no militia, noble 80% = no nobles [V3 OEW Unrest]. Victory: Conquest (65% of population), Cultural (50 cultural victory points and 50% over the runner-up), Son of Heaven (75% acknowledge you), or best score at the last turn [V3 OEW Player Status, Culture]. Recovery: reload; what a rival's win looks like `?`.

#### 7. Consequential vs cosmetic choices
- Where to settle: irreversible, pays off decades later, no consensus (8 vs 10 hexes) [V3 SG-OE 1.1, single author]. Consequential.
- Edict order and timing: Well Field System is a "first pick" for farmers per one author [V3 SG-OE 3.4, single-author]; delay worsens the penalty. Consequential, near-dominant.
- Labour pacing vs authority: both cap growth; the author says 3 settlements over authority is safe [V3 SG-OE 3.1]. Consequential.
- Battle plans: numeric modifiers are small (Charge +5% attack, Defend +10% defence); Ambush (forest only) decides whether a battle starts at all [V3 OEW Battle Plans]. The FAQ says terrain, numbers and unit types decide many battles but plans can swing them [V3 OEW FAQ]. Moderate.
- Faction modifiers are +-10-30% on a few rates; the FAQ admits the factions are not very diverse [V3 OEW FAQ].

#### 8. Open items
| claim | file:line | verdict | source |
|---|---|---|---|
| R. T. Smith "Project Director on Medieval II (2006)" | e3f9:118 | CONFIRMED in substance: Medieval II infobox director and designer Robert T. Smith; he says he was brought in to lead it; "Project Director and Lead Artist" on Total War. MobyGames itself NOT OPENED | [V3 WP Medieval_II:_Total_War; GH; MSQ] |
| "earlier work on Shogun and Rome"; "[SOURCE: T1 - MobyGames credits]" | e3f9:118,575 | PARTLY: Rome lists Smith among five designers; Shogun NOT FOUND (infobox names Simpson only); sources say "lead developer", not "design lead"; the T1 label is unsupported by what I could read (pedigree rests on Wikipedia and interviews) | [V3 WP Rome:_Total_War, Shogun:_Total_War; SN gid 4249665521682795652] |
| "four simultaneous tech trees" (UNVERIFIED) | e3f9:120,599 | CONFIRMED four schools (Power, Craft, Thought, Knowledge) with separate research-rate modifiers; "simultaneous" is inference only, no page says four run at once | [V3 OEW Technology and Culture, Factions; SG-OE 4.5] |
| "three victory paths" (UNVERIFIED) | e3f9:120,599 | [CONTESTED]: OEW lists FOUR (Conquest 65%, Cultural, Son of Heaven 75%, Points); three if the last-turn Points result is not a "path"; Cultural can be switched off | [V3 OEW Player Status, UI] |
| edicts "with paired benefits and costs" | e3f9:122 | CONFIRMED in substance: permanent effect plus temporary unrest, upkeep or cancel penalty; some edicts are not paired (Trade Venture) | [V3 OEW Edicts] |
| "at least one of which must be adopted per tech tier" | e3f9:122 | NOT FOUND. Closest real rule: the two era edicts gate each tier; all others optional, one per turn | [V3 OEW Edicts; SG-OE 3.5, 3.6] |
| "two opposed unrest pools - peasants and nobles" | e3f9:128 | CONFIRMED pools; "opposed" PARTLY: Well Field System and garrisoned nobles move them oppositely, authority/culture/events move both | [V3 OEW Unrest, FAQ; MSQ] |
| unrest "Immediate" latency | e3f9:316; 89a3:129 | NUANCE: "previous grievances" persist and labour unrest falls only 1 per turn | [V3 OEW Unrest] |
| "map runs continuously against a paused decision layer"; "two clocks" | e3f9:298,248 | WRONG/overstated: simultaneous turns, battles are 1-2 min on-map playback you cannot steer | [V3 OEW Turns, FAQ; MSQ] |
| "no preset provinces; spacing limits" | e3f9:224 | CONFIRMED (4 hexes minimum), but candidate sites are fixed at map generation | [V3 OEW FAQ; Settlers] |
| "population ... auto-builds infrastructure" | e3f9:128 | PARTLY: automation is an opt-in switch | [V3 OEW Player Status] |
Unestablished: F1 help and tutorial text; difficulty names; whether external buildings use slots; hostages/ransom; rival victory; wiki conflicts (clear time 3 vs 6 turns, claim radius 2 vs 3, disband limit 10 vs 15 pop); no v2 table, so no cell corrected.
