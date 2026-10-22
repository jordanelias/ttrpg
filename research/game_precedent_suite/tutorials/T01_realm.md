# T01 - Realm / dynasty games: how to play (tutorial pass, 2026-10-22)

Tags per TUTORIAL_BRIEF: [V3 url ver] = read in a fetched page/file body this session; [S3] snippet only; [M] memory; `?` unknown; [CONTESTED]. [V2 R1 cell] = taken from the v2 table, NOT re-opened this session.
Shorthand used in CK3: **GF** = [V3 https://github.com/jesec/ck3-mod-base @d4cbb83 = "Version 1.20.1.2 (Crozier)", cloned this session], paths under `base/game/` (the game's own script and localization files; the in-game tutorial text is in `localization/english/tutorial/`). **CK3W** = [V3 https://ck3.paradoxwikis.com/Council, "verified 1.20", fetched this session].

---
### Crusader Kings III - facts line
Paradox Development Studio / Paradox Interactive; grand strategy + dynasty sim, real time with pause. Version: **1.20.1.2 "Crozier"** (Steam 2026-10-21; GF HEAD commit message; DLC By God Alone shipped with 1.20.0) [V3 GF + V2 R1 SN-CK3]. Assumed: a Duke in the 867 or 1066 bookmark, Normal difficulty, Ironman off, base rules. The in-game tutorial is built for an Irish **count**, not a duke; this section teaches from it and adds what a duke must also watch. Sourcing: mostly game files and the game's own tutorial text (strong); speeds, UI layout and feel of play are [M]. One play session: the game's own estimate is **13 minutes for the Quick Tutorial, 2 hours for the Advanced one** [V3 GF localization/english/tutorial/tutorial_l_english.yml `quick_tutorial_explanation_desc`, `full_tutorial_explanation_desc`]; a real campaign is hundreds of hours across many generations [M]; one sitting of 2-3 hours is roughly 1 generation (20-40 game years) [M].

#### 1. Setup choices
1. **Start date (bookmark group).** Three groups: **867, 1066, 1178** [V3 GF bookmark/start_years_l_english.yml]. 867 bookmarks: Humble Origins (adventurer), The Carolingians, Autumn of Virtue (China), Fathers of the Faithful, The Struggle for Iberia, Living Gods on Earth (SE Asia), Wrath of the Northmen, The Iranian Intermezzo. 1066: Song of Splendor (China), The Fate of England, Iberia in Pieces, A Never-Waning Moon (Japan), The Wandering Exiles, At the Gates (nomads), Rags to Riches [V3 GF bookmark/bookmark_*_867/1066_l_english.yml `bm_*` keys]. Changes: the map, available cultures/religions, which tech ("innovations") exist; 867 has fewer innovations, so fewer casus belli and weaker laws early [M for innovation detail; GF `innovation_casus_belli` gates the county de jure CB].
2. **Character.** Take a featured bookmark character, or **"Choose any Character"**: "Play as any Ruler in <year>, or create your own!" [V3 GF gui/frontend_gamesetup_l_english.yml `PICK_ANY_CHARACTER`]. For the duke start you click a duke on the map (the title tier is shown on the pick card: title, culture, faith, age, relatives [GF bookmark_l_english.yml]). This is the real decision: your culture, faith, succession law, neighbours, vassals, claims, and traits are inherited from the pick.
3. **Create your own** (Ruler Designer): a new dynasty as a landless noble family or an adventurer; the point limit matters only for achievements [V3 GF bookmark_l_english.yml `BOOKMARK_SUBTITLE_NEW_NOBLE_FAMILY`; ruler_designer_l_english.yml `IRONMAN_POINT_MAX`].
4. **Difficulty (game rule): Very Easy / Easy / Normal (default) / Hard / Very Hard** [V3 GF common/game_rules/00_game_rules.txt `difficulty`]. Easy and Very Easy give YOU bonuses (less disease, hostile-scheme and stress impact, easier factions) and **block achievements**; Hard and Very Hard give the AI bonuses (less stress, more stable realms) [V3 GF game_rules_l_english.yml `setting_*_difficulty_desc`].
5. **Ironman on/off**: autosaves, no character switching, single player only [V3 GF game_rules_l_english.yml `IRONMAN_PAUSE_MENU_EXPLANATION`].
6. **Game rules**: the base file defines **84** top-level rules, in filters Difficulty, Titles & Realm, Health, Tweaks, Flavor, Historicity, Game Modes, AI, Setup, Culture, Faith [V3 GF 00_game_rules.txt count; game_rules_l_english.yml `game_rule_category_*`]. Ones a duke feels: End Date (default 1453), De Jure Requirement, Realm Stability, Casus Belli Costs, Diplomatic Range, Conquerors, plague frequency, Black Death [GF rule names].
7. **Tutorial prompt** for new players: Quick (13 min) or Advanced (2 h); it forces a fixed character [V3 GF `GAMESETUP_TUTORIAL_PROMPT_*`].

#### 2. The loop
1. **Clock: real time with pause.** The game starts paused; the tutorial tells you to unpause with Spacebar; "time stands still and your armies will not move" while paused; the game plays out "over the course of hundreds of years" [V3 GF tutorial_l_english.yml `lesson_basics_quick_resources_time_desc`, `lesson_army_purpose_step_1_desc`]. Five speed settings [M]. Hard end: 1453 [V3 GF game_concepts `end_date_desc`].
2. **You act through character interactions** (right-click a character, or a map province): marry, gift, Sway, declare war, imprison, grant title. Each is an instant click with a price (gold, prestige, piety, a hook, or a long-running scheme).
3. **The game, between your clicks:** council tasks tick toward completion; schemes (yours and others') add a phase each 70-170 days [V2 R1 H3]; taxes and levies arrive from vassals by contract; armies march and fight; buildings finish; characters age, marry, have children and die; AI rulers declare wars, fire factions and plot [M].
4. **What interrupts:** (a) **event pop-ups** that need a choice (stress, a courtier's request, a murder attempt on you); (b) the **"Important Actions" strip** at the top of the screen, which does not pause but nags: "You are not married", "Empty Council Position", "Above Domain Limit", "Dangerous Faction", "No player heir", "Criminal can be Imprisoned", "Title can be Created" [V3 GF localization/english/important_actions_l_english.yml `action_*`]; (c) war declarations on you and war-end summaries (victory / white peace / defeat); (d) your death.
5. **Control passes on death:** you continue as your heir under the title's succession law; you may lose titles to other heirs but keep claims on them [V3 GF tutorial_reactive_l_english.yml `reactive_advice_succession_desc`]. If no dynasty member can inherit: game over (section 6).
6. **Automated vs manual.** Automated: levies and taxes (by vassal contract), council tasks once set, battles (no tactical control: armies meet and resolve) and siege progress [V3 GF tutorial `lesson_army_purpose_step_1_desc`: "battles will happen automatically if two hostile armies cross paths"], construction, AI behaviour. Manual: every interaction, scheme start, army order, law change, event choice, and every appointment.

#### 3. The choice menu
| verb / choice | cost | effect | when picked (freq.) |
|---|---|---|---|
| Pause / speed / unpause | none | controls how many decisions you can fit | constantly |
| Answer an event | varies: stress, gold, opinion, traits | shapes traits, relationships, stress | constantly (dozens a year) |
| Appoint councillor + set task (Chancellor, Steward, Marshal, Spymaster, religious councillor, spouse/Confidant seat) | one task per councillor; changing task loses progress except Integrate Title and Develop/Control in County [V3 CK3W] | taxes, development, claims, scheme defence, integrating titles; effect scales linearly with skill; friend +20%, best friend +30%, rival -20%, nemesis -30% [V3 CK3W] | at start, then when a seat opens or a goal changes (monthly-to-yearly) |
| Marry / betroth (self, children, kin) | prestige loss if lowborn; opinion/hook costs | alliance (calls to war), claims to inheritance, skills added through the spouse seat, genes [V3 GF tutorial `lesson_basics_quick_marriage_window_desc`] | early, then once per child (every generation) |
| Gift / Sway / Befriend / Seduce | gold; Sway = one 365-day phase, -2.5 days per skill point, max 95% [V2 R1 H3] | opinion up; unlocks vassalization, alliance, claim requests | frequent |
| Hostile scheme (Murder, Abduct, Fabricate Hook, Claim Throne) | up to 5 agents; breaches (5 kill it); cooldowns 2-10 years [V2 R1 H3] | removes rivals, blackmail hooks, steal succession | situational but central to dynastic play |
| Fabricate / ask for a claim | religious councillor task, or piety to the head of faith [V3 GF tutorial_objectives `hint_ask_for_claim`] | a claim = a casus belli | before most wars |
| Declare war | prestige: **100 per target county (75 if pressed/strong claim), 200 per duchy** for the claim CB [V3 GF common/script_values/99_casus_belli_values.txt L727-752]; de jure CB 100/county [V3 GF 00_dejure_war.txt L314-420] | the war: raise levies, siege, war score -100..+100; at +100 enforce demands [V3 GF tutorial `lesson_warscore_step_1_desc`] | every few years |
| Raise levies / hire men-at-arms / mercenaries | gold; mercenary contract 3 years [V3 GF tutorial_objectives `hint_recruit_mercenaries`]; peace stops army upkeep [V3 GF `reactive_advice_bankruptcy_desc`] | army strength | per war |
| Build in a holding | gold; barony 2 slots, county 3 slots [V2 R1 C2] | income, levies, development | steady, every few months early |
| Grant / revoke / create titles | grant to stay under **domain limit** (each holding over: -20% levies and tax, cap 100%) [V3 GF common/defines/00_defines.txt NDomain L1153-1160]; revoking needs crown authority and angers vassals | vassals, de jure kingdom/empire formation, rightful-liege status | when the Important Actions strip says "Above Domain Limit" |
| Vassal contracts, crown authority, succession law | crown authority 4 levels, 20-year cooldown [V2 R1 D1]; tax steps 0/2.5/10/15/25% [V2 R1 D2] | how much levy/tax vassals owe; who inherits | rare (a few times a century) |
| Lifestyle + focus + perks | experience over years; perk points | permanent bonuses and the next unlock | every ~5-10 game years |
| Children: guardian, education, betrothal | gold, guardians' skill | child's traits (the future heir) | once per child |
| Decisions (e.g. create kingdom, found holy order) | gold/prestige/piety, conditions | big structural jumps | rare |
| Faction response (concede, bribe, crush, assassinate leader) | gold, opinion, war | stops independence/claimant/peasant uprisings [V3 GF `reactive_advice_protect_against_factions_desc`] | reactive |
| Imprison / ransom / execute / hold hostages | hooks, dread, tyranny | removes threats, extracts gold | situational |

#### 4. First hour, step by step
Drawn from the game's own Quick Tutorial lesson order [V3 GF tutorial_l_english.yml `lesson_basics_quick_*`], then its Advanced chapters and reactive advice.
1. **Setup**: pick 1066 > Choose any Character > a duke with 2-3 of his own counties and 3+ vassal counts. Keep Normal.
2. **Camera and zoom** (WASD, scroll; Home key returns to capital). Three zoom levels: detail, political, paper map.
3. **Click your own portrait**: titles (the leftmost is primary and names the realm), age, five skills (Diplomacy, Martial, Stewardship, Intrigue, Learning), traits (they change how you react to events), spouse, heir [V3 tutorial `quick_this_is_you_*`, `quick_skills`].
4. **Read the Important Actions strip** top of screen. Clear what it lists, starting with marriage and the heir. If unmarried, open "Find spouse"; the tutorial's criteria are politics (alliance), ability, genetics, nobility.
5. **Open Domain, then Realm**: your counties split into baronies/holdings; the difference between **domain** (land you hold) and **realm** (plus all vassals' land); duchy-level rulers hit the domain limit fast [V3 tutorial `quick_vassals_great_job_2_desc`].
6. **Open Vassals**: opinion, taxes, levies; note any "powerful vassal"; contracts can be changed here.
7. **Open Council**: fill the six seats (the tutorial calls it "six councillors, your spouse included"). Give each a task. The tutorial's task is **religious councillor: Fabricate Claim** on a county outside your borders.
8. **Learn the four resources** (top right): Gold (buildings, armies, bribes), Prestige (secular decisions, claim wars), Piety (faith actions, holy wars), Dynasty Renown (family decisions) [V3 tutorial `quick_resources_*`].
9. **Unpause at the slowest useful speed**; the tutorial ends here ("Good Luck!") and says to watch the "Reactive Advice" icons.
10. **Start a Sway** (Advanced chapter XIV): Sway raises a target's opinion; success is shown and depends on your Diplomacy; Abandon Scheme cancels it.
11. **Pick a lifestyle** when the strip says "No Lifestyle Chosen", then spend perk points as they appear.
12. **Build**: choose a holding with a free slot; the tutorial notes holdings "support several buildings".
13. **When the claim lands**: declare war on a neighbour whose title is de jure part of yours; the tutorial's example is the Earl of Desmond, valid without a claim because of de jure [V3 tutorial `lesson_declare_war_step_1_desc`].
14. **Rally armies** at your chosen rally point; unpause for a few days until full; send them to enemy holdings; sieges begin when an army sits on a holding [V3 tutorial `lesson_raise_troops`, `lesson_army_purpose`].
15. **Check War Score**; at +100 open War > Enforce Demands, or right-click the enemy > Offer Peace.
16. **Aftermath**: new land over the domain limit? Grant it to a vassal. New vassals who are not "rightful" under you get tax/levy multipliers of 0.5 (none of your titles de jure above them) or 0.75 (partial) [V3 GF 00_defines.txt L520-525].
17. **Raise children**: assign guardians (the game nags "Guardian can be assigned"; an heir with none triggers an Education advice), plan 2+ children "the second serving as a spare" [V3 tutorial `reactive_advice_succession_desc`].
18. **Save before the first big risk**, then play to the first death to see succession.

#### 5. What changes later
- **Rank climb.** Duke > King > Emperor by creating titles (a Create Title action appears on the strip); a duke who exceeds the **vassal limit** is told to form a kingdom, and you cannot hand away a primary title [V3 GF tutorial_reactive `reactive_advice_vassal_limit_desc`]. A duchy "too large" triggers a mega-duke penalty advice.
- **Law layer.** Crown authority (4 levels), succession-law changes, elective vs hereditary; vassals become more dangerous as they grow powerful and want council seats ("Powerful Vassal expects a Council Position", -40 opinion if denied) [V3 GF important_actions `powerful_vassal_not_on_council`; defines L507].
- **De jure drift.** Duchies fully held by someone not holding their de jure kingdom drift to that holder's kingdom over **1200 monthly progress points at +1 base per month = about 100 years**; the Chancellor's Integrate Title speeds it [V3 GF defines NTitle L953-956; game_concepts `de_jure_drift_desc`].
- **Pressure ramps**: hostile schemes against you, factions (independence, claimant, populist, peasant), stress, plague, holy wars/crusades, steppe invasions, culture and faith shifts; later eras add innovations that make CBs cheaper and laws stronger [M for era detail].
- **DLC systems** add courts, tours, diarchies, nomads, clergy [V3 GF dir names; M].

#### 6. Failure and ending
- **Game over = you die with no player heir** (any dynasty member), or you reach **1453** [V3 GF game_concepts `game_over_desc`, `end_date_desc`]. Even then you can choose to play as another ruler anywhere. Warning: "Looming game over" advice if no heir; fixes: legitimize bastards, change gender law, remarry, or worse [V3 GF `reactive_advice_looming_game_over_desc`].
- **No victory screen.** You set your own goals; the tutorial's closing line is "maybe you can even become the King of Ireland" [V3 tutorial `quick_done_desc`]. Achievements are the closest authored goals.
- **Setbacks you survive**: lost wars (loss of titles, prisoner status: use Ransom Yourself), bankruptcy (debt blocks wars; end wars to stop upkeep), factions, deposition [V3 GF reactive_advice texts]. Losing titles on succession is normal.

#### 7. Consequential vs cosmetic choices
- **Consequential:** your starting pick (culture, faith, succession law, neighbours); marriage and heir planning (the only game-over path); council task choices at the start; who you grant land to (domain limit and vassal opinion drive taxes, factions and war strength).
- **Consequential:** casus belli route (claims and de jure are cheap in prestige; other paths cost more) and war timing vs army upkeep.
- **Mostly cosmetic or dominated:** most event options differ by small stress/opinion amounts [M]; lifestyle focus within a lifestyle matters less than the lifestyle itself [M]; community consensus puts defensive vassal management and the schemes game ahead of battlefield micro because battles are auto-resolved [CONTESTED/M].
- **Dominant answers:** fill the council, keep Spymaster loyal [V3 GF `protecting_against_hostile_schemes_desc`], always hold 2+ children; these are the game's own advice, so treat as intended best practice.

#### 8. Open items
- Default succession law by bookmark/character: still `?` (history files not in the GF clone); v2 B7 stays `[M]`.
- Game speeds: exact day-tick length per speed `[M]`. Whether event pop-ups pause by default `[M]`.
- **v2 correction (council seat name):** R1 says standard council has "Spymaster + Confidant for all". CK3W confirms Confidant = the spouse seat [V3 CK3W]; the game's own script names that seat `councillor_spouse` ("Spouse") and uses "Confidant" for the clan Vizier [V3 GF common/council_positions/00_council_positions.txt L1021; localization/english/council_l_english.yml L61-62, L376]. R1 C/B cells unchanged, just a naming caveat.
- **v2 settled (D-area):** R1 H3/L1 lists no plots or ambitions for CK3: confirmed, `game_concepts` has no plot/ambition entry; schemes come in four types personal/hostile/political/contract; lifestyle focuses (20 in `focuses/00_lifestyle_focuses.txt`) are the CK2 "Way of Life" analogue [V3 GF game_concepts_l_english.yml L198, L765-767; focuses file].
- **Attachment claims (CK2 text vs CK3, see end of file for the table):** de jure drift 100 years exists in CK3 too, as the game defines above.

---
### Victoria 3 - facts line
Paradox Development Studio (Paradox Interactive); economic + political grand strategy, real time with pause, you play a **country**, not a person. Version: **1.13.11 "Matcha"** (hotfix 2026-08-19; 1.13 "The Great Wave" 2026-04-28); free update **1.15 + State and Revolution** was scheduled for 2026-10-22 and is not confirmed live, so numbers are 1.13.11 [V2 R1 SN-V3 gids 1841579228662409, 1830797770244834; Steam news list read this session shows 1.15 dev diaries #189/#193 and no live post]. Assumed: Sweden (mid-size, recommended by the game's own tutorial diary and a 2026 guide), "Learn the Game" objective, default rules. Sourcing: tutorial design and law/budget rules from Paradox dev diaries and the game-extracted reference site; "first hour" is the game's own tutorial journal entries (strong) plus a 2022 guide; speeds and UI feel are [M]. One play session: a campaign is 100 game years (1836-1936); the tutorial chain covers roughly the first 1-3 game years; real hours per full campaign `?` [M: dozens].
**Tag shorthand.** SN-V3 = [V3 https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=529340, read this session, cited by gid]. V3REF = [V3 https://alcaras.github.io/v3ref/ "Game 1.13.11 (Matcha)"], pages `concepts`, `defines`, `laws`, `journal-entries`.

#### 1. Setup choices
1. **Player Objective** (a layer on top of the sandbox): at launch **Learn the Game** (the tutorial), **Economic Dominance** (control a large share of global GDP in your market), **Hegemony** (large share of world population within your and subjects' borders), **Egalitarian Society** (most equal society: institutions, progressive laws, high average Standard of Living and education), or **Sandbox** (none). Completing the final objective gives an achievement [V3 SN-V3 gid 4474904295755725222, Dev Diary #52, 2022-06-30; the 1.13 list not re-checked, `?`].
2. **Country.** Any playable country; they "start off in very different positions" and a landlocked one-province vassal with subsistence farmers is a poor first game [V3 SN-V3 gid 4474904295730225610, DD#51, 2022-06-23]. Tutorial-recommended: Sweden or the USA (2022); 2023 forum post: Persia, Belgium, Japan [V3 SN-V3 gid 6560117310267177684]; 2026 guide for 1.13: Belgium, Netherlands, Sweden, Sardinia-Piedmont, Prussia, Chile, and avoid France/UK/USA/Russia/Austria/Japan on a first run [V3 https://after-strategy.com/en/complete-beginner-guide-victoria-3-2026-version-1-13/, 2026]. [CONTESTED] between sources.
3. **Game rules** (selectable before start). Named in dev diaries: AI aggressiveness (lowered by default for Learn the Game, which also makes the AI reluctant to start diplomatic plays on you until you show you grasp economy and politics), **Autonomous Investment** (default ON: pops build private buildings from the Investment Pool; OFF puts the pool back under your control), Pop Consolidation, custom RNG seed, Ruler Selector, Monument effects, Infamy scaling (new in 1.15 open beta) [V3 SN-V3 gids 4474904295730225610, 5035621474411252488, 5124581515254858730, 1802354289725273, 1846018067926226]. **There is no difficulty slider named in the sources I read** `?`; Ironman is optional and no longer needed for achievements; "a few game rules disallow achievements" [V3 SN-V3 gid 4584121659781205633].
4. **Start date.** Always 1836-01-01; the achievement text is "play a full campaign from 1836 to 1936" [V3 SN-V3 gid 4584121659781205633]. Other start dates: none announced (a search result said "none announced") [S3 gamewatcher].
5. **What the country choice sets:** which laws are active, which Interest Groups hold the government, whether you have a ruler/heir (monarchy), your starting buildings, markets, subjects, wars in progress, and your Rank (Minor/Major/Great Power).

#### 2. The loop
1. **Clock: real time with pause.** The game starts **paused**; Spacebar unpauses; slow speeds keep notifications from outrunning you [V3 PCGN https://www.pcgamesn.com/victoria-3/beginners-guide, 2022-12-02]. Daily tick, **weekly economy** ("there is no such thing as a lump sum cost... it's all about your weekly balance") [V3 SN-V3 gid 4018887653980585574, DD#12, 2021-08-26]. Law checkpoints every 100 days by default; elections every 4 years [V3 V3REF defines `LAW_ENACTMENT_DEFAULT_BASE_DAYS`=100, `ELECTION_INTERVAL_YEARS`=4].
2. **You set policy, not actions.** You choose what is built, which production method each building uses, tax and spending levels, laws, institutions, treaties and war orders. No unit or person does something because you clicked it; you change a parameter and the simulation responds.
3. **The game, between clicks:** pops work in buildings and earn wages; buildings buy inputs and sell outputs; markets set prices from buy/sell orders; pops spend income on needs; Standard of Living rises or falls, creating **Loyalists or Radicals**; Interest Groups' Approval and Clout shift; Political Movements form and push; construction advances with available construction capacity; research accrues from Innovation; AI countries trade, scheme, and start diplomatic plays [V3 V3REF concepts Pop, Standard of Living, Radical, Political Movement, Innovation].
4. **Interrupts:** event pop-ups (choices), **Journal Entries** (goals and warnings), a diplomatic play declared on you or involving your interests, war outcomes, enactment events (Debate/Stall) that "time out automatically (selecting the default option) when the clock fills up, so there's always only one enactment event pending" [V3 SN-V3 gid 5121196841288559912, DD#80, 2023-04-06], election campaigns (6 months), revolutions.
5. **Control never passes to a person.** A ruler may die or an election may change the Head of State; you remain the state.
6. **Automated:** all production, wages, trade flows, pop migration, private construction (with Autonomous Investment), battles once a General is ordered to advance/defend a Front, and AI behaviour. Manual: every parameter above.

#### 3. The choice menu
| verb / choice | cost | effect | when picked |
|---|---|---|---|
| Pause / speed | none | time to act | constantly |
| Order construction (new/expand building, Construction Sector) | goods + wages paid weekly while building; limited by **construction capacity** and queue; Government vs Private queue split set by Economic System law [V3 SN-V3 DD#12, gid 5035621474411252488; V3REF concepts Construction Queue] | GDP, jobs, tax base, goods supply | constantly; the early-game bottleneck |
| Change a production method | retooling lowers output briefly [M]; may need new goods/tech | profit, jobs, pollution/needs | often early, then periodic |
| Tax levels (income, poll, land, consumption, dividend); spending and wage levels | consumption taxes cost Authority; raising taxes costs Legitimacy and breeds Radicals [V3 SN-V3 gid 4018887653980585574] | treasury per week | several times a campaign |
| Borrow / spend Gold Reserve | interest; debt ceiling; default pauses construction [V3 V3REF concepts Default] | fund deficit growth | when budget goes red |
| **Enact a law** | 3 phases, one checkpoint per ~100 days (150 or 200 for some groups), 730-day cooldown on failure/cancel, 3 setbacks fail it [V3 V3REF defines + laws; SN-V3 gid 5121196841288559912] | changes economy, rights, army model, institutions | the central political verb; few per decade |
| Negotiate with an Interest Group during enactment | uses IG Amenability; no gold [V3 V3REF concepts Negotiation] | flips an IG from oppose to indifferent/endorse | each enactment |
| Government reform (add/remove IGs from government) | removed IGs gain Radicals unless done right after an election [V3 V3REF concepts Government Reform] | Legitimacy, which laws can pass | at elections or crises |
| Invest in an Institution | money + **Bureaucracy** | pop outcomes (education, health, police...) | once a law enables it |
| Issue a Decree in a state | **Authority** for as long as active [V3 V3REF concepts Decree] | local bonus | occasionally |
| Research a technology | Innovation; later eras cost more if you skipped earlier ones | unlocks buildings, PMs, laws | when a slot opens |
| Treaties, tariffs, trade routes | **Influence**; infamy from aggression raises costs [V3 V3REF concepts Influence, Infamy] | market access, alliances, subjects | steadily |
| Diplomatic play (demand) | needs an Interest tier in the region; Infamy; 3 phases Opening Moves / Maneuvers / Countdown, then war [V3 V3REF concepts Diplomatic Play] | territory, subjects, concessions | mid-game |
| Create/mobilize formations, assign commanders, order Front advance/defend | upkeep, goods, Bureaucracy for commanders | war | in war only |
| Bolster / suppress a Political Movement; appease a Lobby | political capital via Appeasement or laws | prevents revolutions | when radicals rise |
| Subsidize, charter a Company, colonize/incorporate states | treasury; Influence/construction | support industry, expand | mid-game |
| Journal/event choices | varies | rewards, penalties | constant |

#### 4. First hour, step by step
Source: the game's tutorial journal-entry set [V3 V3REF journal-entries "Tutorial" group] and the tutorial diary (reactive journal + popup "Tell me How / Tell me Why").
1. At setup choose **Learn the Game** and Sweden (or another recommended country). The game starts paused; an optional intro popup explains camera, HUD, and how to unpause [V3 SN-V3 gid 4474904295730225610].
2. **Click your states** (buildings, resources, standard of living). Open the nation menu: Overview, Government (which IGs rule and their opinion), Laws, Institutions [V3 PCGN].
3. Check Diplomacy (overlords, treaties, wars at start) and Military (assign generals to unled battalions) [V3 PCGN].
4. **Unpause on a slow speed.** After a few days, the first tutorial journal entry arrives: **Expand a basic Building**, tailored to you (a Rye Farm for Sweden, Millet Farm for Sokoto) because the game picks a "relatively safe investment" [V3 SN-V3 gid 4474904295730225610; V3REF "Expand a basic Building"].
5. Press **Tell me How** to be walked through the plus button; **Tell me Why** for why farms are safe. Both optional and in any order.
6. Learn the budget: hover the plus button on a building for its estimated weekly budget effect; green is good [V3 PCGN].
7. **Build Construction Sectors** in populous states first; they raise weekly construction capacity (you will start with too little) [V3 PCGN].
8. Next entries (not strictly linear): **Change Production Method** on a farm or ranch for a safe test; **Expand a Productive Building**; **Fix Capacity Deficit** if Bureaucracy/Authority/Influence run negative; **Solve Budget Deficit** if weekly balance is red [V3 V3REF journal-entries].
9. **Make Interest Group Happy**: an IG with low Approval of your government threatens to radicalize. **Research a Technology.** **Bolster a Political Movement** (choose a political vision).
10. **Passing an Institutional Law** once Bureaucracy is in surplus, then **Invest into an Institution**. The first law enactment is your first look at checkpoints: watch the success chance (Clout of endorsing IGs in government), answer events, and negotiate.
11. Meet food and goods demand: farms in each state, raw materials (wood, iron, coal) early; "Improve Access to Consumer Goods" appears when pops cannot buy something [V3 PCGN; V3REF].
12. **Increase Relations** and **Establish an Interest** (tutorial entries) to start diplomacy; **Create Formation** and **Recruit and Promote a Commander** to prepare an army; **Mobilize**/**Send Formation to the Front**/**Make Peace** only appear when war arrives.
13. **Grow GDP** and **Improve rank** appear as open-ended later goals. Keep peace for the first decade if possible (a guide's advice) [V3 after-strategy 2026].

#### 5. What changes later
- **Eras I-V** of technology (Era I known pre-1836; Era II First Industrial Revolution; Era III standardization; Era IV Second Industrial Revolution; Era V modern) unlock new buildings, laws, and decrees [V3 V3REF concepts Era].
- **Politics hardens**: Political Movements rework (1.8), revolutions (civil war when a movement is Insurrectionary), elections every 4 years once there is a franchise, Petitions from IGs in government that reward you with Legitimacy if you pass the law [V3 SN-V3 gid 5121196841288559912].
- **Foreign layer**: Interests become multi-level (1.13), Power Blocs (leverage on members), Companies, Great Power rank, naval supply and troop transport (1.13 Great Wave), strait tolls [V3 SN-V3 gid 1827626365753709].
- **1.15** adds State and Revolution content (communism, AI and war-support rework) `[M/S3 from titles]`.

#### 6. Failure and ending
- No fail screen for a bad economy: **default** pauses construction and hurts Throughput until the weekly balance is positive or you declare **bankruptcy**, which wipes cash reserves and angers owner pops [V3 V3REF concepts Default, Bankruptcy].
- **Revolution:** "Losing a revolutionary war means your country loses all its territory and Pops, in other words Game Over" [V3 SN-V3 gid 4353300134225504187, DD#41, 2022-04-07].
- Lost wars and annexation by a Great Power end a country; whether you may switch tag `?`.
- **Ending:** the campaign runs to 1936 (achievement "Victorian Century") [V3 SN-V3 gid 4584121659781205633]. What the game does on 1936-01-01 (score, continue) `?`. Objectives give an achievement, not an end.

#### 7. Consequential vs cosmetic choices
- **Consequential:** which IGs sit in government (they gate every law, drive Legitimacy and coups) [V3 V3REF concepts Government, Endorsement]; construction order and capacity (the bottleneck both guides name); tax level (Radicals, Legitimacy).
- **Consequential:** the Economic System law (sets private vs government construction share) and the Autonomous Investment rule [V3 SN-V3 gid 5035621474411252488].
- **Mostly flavour or automatic:** which decree; which individual pop wins a job; many events (the game says the "default option" auto-picks on timeout). Cosmetic: ship/building models, monuments' look (their effects can be switched off by rule) [V3 SN-V3 gid 1817483467036912].
- **Dominant answers (community, [CONTESTED]):** an early Construction Sector build-out and buying farms/raw materials before tech; the 2026 guide's "keep peace for 10 years" is advice, not a rule.

#### 8. Open items
- 1.13 objective list and rules list not re-fetched, only the 2022 diaries (launch-era) `?`. Difficulty setting `?`. End-of-campaign behaviour `?`. Sweden's actual starting laws and IGs `[M]`.
- **v2 settled (R1 D1):** "26 law groups, 138 laws" re-confirmed from the V3REF laws page header; base enactment days confirmed in `laws` (Distribution of Power 150, Governance Principles 200, Economic System 150, Slavery 150), default 100, cooldown 730, max phases 3, setbacks 3 [V3 V3REF laws, defines L157-171; SN-V3 gid 5121196841288559912].
- **v2 D1 "one enactment at a time":** DD#80 says "there's always only one enactment event pending", which implies a single active enactment, but it is not an explicit rule `?` [V3 SN-V3 gid 5121196841288559912].
- **v2 C2 (construction):** "weekly goods + wages, no lump sum" is confirmed (DD#12). The "20 construction points per building" cap: only [S3] from a guide snippet, `?`.
- **Attachment claims:** none of the four uploads makes a Victoria 3 law-enactment claim (grep for "enactment" returns nothing); the only Vic3 claims are listed in the attachment table below.

---
### Old World - facts line
Mohawk Games (designer Soren Johnson; published by Hooded Horse); turn-based 4X with a dynasty/character layer, one turn = one year. ("Mohawk" in the request is the developer, not a nation; the base game has 7 kingdoms [V3 Steam store API appdetails 597180, 2026-10-22].) Version: **main branch 1.0.84977 (2026-10-07)**, test branch 1.0.85174 (2026-10-21) [V3 MB-OW `Old World Release update 2026.10.07`; V2 R1]. Assumed: single player, one base-game kingdom (Rome used in examples; the setup screen's default nation is not established, `?`), the default **Introductory** option preset, lowest-to-mid difficulty. One play session: a full game runs on the order of 200 turns ("200 years") [V3 PCG]; session length is `[M]` 1-2 turns a minute early, slowing to several minutes a turn mid-game; the Learn to Play scenarios are short `[M]`.
**Sourcing: strong on setup options, laws, ambitions and victory (the developer's own build notes); thin on the in-game tutorial (only inferred from bug-fix lines) and on the Orders formula (`?`).** Shorthand: MB-OW / BN-OW = [V3 https://github.com/MohawkGames/main_buildnotes / test_buildnotes, cloned this session, cited by file date]; SN-OW = [V3 Steam news appid 597180, 346 items read]; FW-OW = [V3 old-world.fandom.com api.php, wiki pages mostly 2020-2022, stale]; PCG = [V3 https://www.pcgamer.com/old-world-guide-tips/, launch-era, no date in body].

#### 1. Setup choices
1. **Mode.** Learn to Play (five scripted scenarios plus an intermediate Scripted/Freeform menu; removed from the main menu once all are done or the tutorial is disabled), authored scenarios (Heroes of the Aegean, Pharaohs of the Nile, Rise of Carthage...), single-player Simple or Advanced setup, weekly challenge games, multiplayer (hotseat, async, cloud) [V3 MB-OW notes 2022-2026; SS-OW "weekly challenge games"].
2. **Nation + leader.** 7 base kingdoms (DLC adds more, e.g. Aksum is mentioned) [V3 SS-OW; SN-OW 2025-02-19]. Each has a fixed historical leader, unique units and four ruling families; or **Pick Later**: found the capital first, then choose nation, family and a **customized leader** (portrait, name, age, gender, starting trait, archetype) [V3 MB-OW/BN-OW "Customize Leader", "Found Capital"]. Changes: starting techs, bonus, unique units, which family classes you start with [V3 FW-OW Civilizations 2023-07-06, stale].
3. **Difficulty.** Named ladder with lowest **The New** (added 2023-11-22: AI penalties 25%, start with an extra Militia and more Civics/Training) and higher levels named by adjectives (Strong, Great, Magnificent, Glorious... the AI plays on "Thriving Prosperity" used on Strong); setups outside the presets show as "Custom" [V3 MB-OW 2023.11.22; BN-OW]. Full ladder order `?`.
4. **Game option preset.** **Introductory** (default since 2024-06: low events, low mortality, no AI development), Standard Settings, Random, Competitive; a **No Events** mode that drops every event not needed for progress; **Event Level** (High lets more events fire per turn); Balanced starting resources; Allow Negative Cognomens (off) [V3 BN-OW 2024.06.10, MB-OW 2024.06.26, SN-OW 1.0.76453].
5. **Map.** Script (**Continent** default since 2025-03-26), size, city-site count, tribe level, premade maps (The Old World, The Middle East, The Mediterranean, The Imperium Romanum) [V3 MB-OW 2025.03.26; SN-OW 2025-02-19].
6. **Victory conditions** (each toggled): Points (VP threshold), Ambition (fulfil 10), Double, Alliance, Time; after Points/Double/Ambition you can accept victory or play on [V3 MB-OW 2025.07.23; V2 R1 M1]. Ambition victory is off by default in multiplayer since 2025-02-19 [V3 MB-OW].
7. **Character modes.** Normal; No Characters / Role Playing variants exist in the options [V3 MB-OW 10-19-22, 11-30-22].

#### 2. The loop
1. **Clock: strict turns, 1 turn = 1 year.** A leader ages and dies in play; the line continues through heirs [V3 FW-OW Old World main page quoting the official description, 2024-03-07].
2. **Turn start (automatic):** characters are processed before units, then yields accrue, cities grow, research progresses, and **events fire** (how many depends on the event level; >1,000 events per the official text, ">3,000" per the 2026 Steam page) [V3 MB-OW 2026.10.07; FW-OW; SS-OW]. An event is a pop-up with options; some give Memories, Traits and Relationships that trigger later events.
3. **Your phase: spend Orders.** "Orders are a resource used to issue commands... each unit can be moved as many times as desired, until the player runs out of Orders. Other ways to spend: Combat, Construction, Events, Diplomacy" [V3 official text quoted in FW-OW and mohawkgames.com 2020-04-14 post]. **Undo and redo any order in a turn** (can be turned off) [V3 PCG; SS-OW "undo mistaken commands"].
4. **Yields are separate currencies:** Food, Wood, Stone, Iron, Money, Science, Culture, Training, Civics, Happiness (Discontent), Orders [V2 R1 E1; M]. Civics pays for laws; Training for unit upgrades/specialist; Culture raises a city's culture level.
5. **End turn:** AI nations, tribes and raiders act; wars progress; city and character mortality resolve.
6. **Interrupts:** event pop-ups, a ruler's death (heir takes over and chooses a new Ambition), foreign missions aimed at you, a captured city.
7. **Automated:** scouting (automated scouts), city "autonomous rule" repairs, AI play; manual: everything else, with Orders as the limiter.
8. **What Orders per turn are:** official text says Legitimacy grants "additional Orders each year"; the exact formula is not established `?`. Older sources say +0.1 Order per Legitimacy point [V3 FW-OW Leader page, 2020-05-14, pre-release] and +0.1 per Citizen [V3 PCG, launch-era]; [CONTESTED], not confirmed for 1.0.84977.

#### 3. The choice menu
| verb / choice | cost | effect | when picked |
|---|---|---|---|
| Move/attack with a unit | Orders (and fatigue) | explore, claim city sites, fight | every turn |
| Found a city on a City Site | Settler; sites are fixed; stationing a unit reserves a site [V3 PCG] | territory, new yield engine | first ~30 turns |
| Set city build (units, improvements, wonders, projects) | Wood/Stone/Iron/Training; "Add Urban" costs Orders [V3 BN-OW 2026.05.13] | growth, culture, defence | every few turns per city |
| Place improvements by adjacency (farm, pasture, quarry, shrine) | resources | adjacency bonuses [V3 PCG] | constantly |
| Research (draw 4 tech cards, pick 1) | Science | unlocks buildings, units, laws; unchosen cards go back in the deck [V3 FW-OW main page] | every 5-10 turns |
| Enact or switch a law (always a pair) | Civics: first switch 200, each later change +100, abolishing raises that pair by 100; Succession Law starts at 400 +100 per switch; some laws carry Order/Money upkeep [V3 MB-OW 2024.10.24, 2024.04.03, 2025.11.26, 2026.03.18] | permanent bonuses, family opinion | rarely |
| Assign characters: governors, generals, council (Chancellor, Ambassador, Spymaster), tutors for children | Orders; replaced characters hurt family opinion | yields and missions | when a person comes of age |
| Missions (marry, declare war, ask to join war, imprison, assassinate, exchange maps) | Orders + target opinion | diplomacy and intrigue | per turn |
| Family seats / assigning cities to families | one seat per family; seats cannot be gifted | bonuses; families pleased or envious | early, then at changes |
| Religion: shrines, found or adopt a religion, Disciples | resources; e.g. Zoroastrianism needs 2 shrines + 2 acolytes [V3 PCG] | happiness, culture, spread | mid-game |
| Buy/sell in the market | Money | convert surplus into need | occasionally |
| Diplomacy: alliance, truce, peace, tribute | Orders, Influence/opinion | war/peace | whenever |
| Marriage and heir planning | Orders; attraction/hatred weighted by the game [V3 BN-OW 2025.02.05] | succession, family ties | each generation |
| Choose an Ambition | none; picked in events | a progress goal; 10 = ambition victory | at each ambition offer and succession |
| Schemer: buy Orders with Legitimacy | extra Legitimacy each use, resets per leader [V3 MB-OW 2026.04.08] | one-off Orders | situational |
| Event options | varies | traits, memories, opinions | every event |

#### 4. First hour, step by step
Old World's tutorial is five **Learn to Play** scenarios; the build notes name them only through bug fixes, so the step contents below are inferred and marked `(inferred)`; the rest is from the launch-era PC Gamer guide.
1. Main menu > **Learn to Play**. Scenario 1 (inferred): moving units and exploring with Orders.
2. **Found your capital** on a City Site (LTP4 forces cities to be founded in order, so the tutorial has a prescribed sequence) [V3 MB-OW "Prevented cities from being founded out of order in Learn to Play 4"].
3. Build a **Warrior**; the tutorial fires an event when it is built (LTP2) [V3 MB-OW "warrior built event... Learn to Play 2"].
4. **Choose a technology** (LTP2 has a "choose tech" goal): you see four cards, you take one.
5. Put **improvements next to each other** to stack adjacency; a Shrine between three camps yields 30 Money/turn in PCG's example.
6. Meet **characters** (LTP3, built around Olympias, with an "Influence" goal reminder): spouse, family, the first diplomacy.
7. Meet **tribes** (LTP4: Thracians; a tribal truce mission; Ambitions cannot be abandoned in these scenarios) [V3 MB-OW 2025.11.26].
8. Fight a **short war** (LTP5: Rome, a pagan head of religion, a truce event).
9. Start a free game on the **Introductory** preset (few events, low mortality, passive AI). Pick a nation; found a capital.
10. Reserve city sites with military units; build **Workers/Scouts**; explore; press **undo** liberally to scout ahead [V3 PCG].
11. **Read the first events** and the tutorial pop-ups (they can be disabled directly from the event) [V3 MB-OW "toggle to tutorial events"].
12. When a mid-game tutorial event warns "don't use a single family", spread **family seats** across all four [V3 MB-OW 2023.01.11 "New tutorial event that warns against using a single family"].
13. First **Ambition** appears; pick from the offered ones; the tutorial blocks abandoning them. Your Legitimacy rises when you finish them (amount `?`).
14. Around turn 20-40: first **law pair** (200 Civics), first religion, second and third city.

#### 5. What changes later
- **New systems unlock with techs**: laws (Civics), Council posts, Grand Vizier only through events (Behind the Throne), religion tiers (Temples, Monasteries, Cathedrals, four world religions with prerequisites), wonders and Legendary improvements, trade caravans.
- **Ambitions get harder** (tiers) until a **National Ambition** (renamed from "Crowning" on 2025-03-26) may be offered after 5 completed ambitions once you reach 70% progress on one; it does not count toward tier difficulty [V3 MB-OW 2025.03.26].
- **Pressure ramps**: tribe level and raids, rival nations' victory pace ("Ruthless" AI weighs alliances and national ambitions), family jealousy, plotting and vengeful characters, regencies for child rulers (up to age 6, or 12 if the leader abdicated), usurpers [V2 R1 B7; V3 MB-OW 2025.05.28].
- Mid-game combat becomes real: flanking, unit upgrades, siege, generals with leaders [V3 SN-OW 2026-03-18].

#### 6. Failure and ending
- **Win:** any enabled condition: Points, Ambition (10), Double, Alliance, Time. If another player (or the AI) satisfies a condition first you can lose even while pursuing another victory; if both you and the AI hit one the player is given the win [V3 MB-OW 2025.07.23, SN-OW 1.0.76453].
- **Lose:** your nation is conquered, your dynasty dies out (the notes refer to "death with no heir" as an end state [V3 MB-OW, hotseat note]), or an enemy wins. Recovery: heirs, regents, usurpers continue a line; no mid-game reroll `?`.
- **Soft failure:** Legitimacy loss on leader change (regents avoid it) and family revolts [V2 R1 D4].

#### 7. Consequential vs cosmetic choices
- **Consequential:** how you build Orders (Legitimacy, Ambitions, Garrisons +1, some laws), since every action is spent from them [V3 BN-OW 2025.05.21 (Garrison +1 Order); MB-OW 2024.09.18 (Divine Rule +1 Order per pagan religion)].
- **Consequential:** family seats and class preferences; one family hoarding cities triggers jealousy [V3 SS-OW "Upset them, or make them too powerful, and you risk their ire"; MB-OW 2023.01.11 tutorial event].
- **Consequential:** the Ambition you pick steers you toward a victory; religion and city-site grabs in the first 30 turns snowball.
- **Cosmetic or dominated:** leader portrait/name; Learn to Play's scripted ambitions; most event options differ by small yields (`[M]`); undo makes tactical misclicks free. Community consensus ranks the early city-site race first [CONTESTED/M].

#### 8. Open items
- Orders formula, VP per ambition/wonder, Points-to-win base, Time-victory default turn limit: `?` (Time "200 turns" is PCGN launch-era). Difficulty ladder order `?`. LTP scenario steps `?` (inferred only).
- **v2 corrections:** (a) R1 M1/Ambitions: the 10th ("Crowning") ambition is called **National Ambition** since 2025-03-26 and can be offered early after 5 ambitions at 70% progress [V3 MB-OW 2025.03.26]. (b) R1 D1: laws switch cost **confirmed** (main branch 2024.10.24: "First switch costs 200 Civics, with each subsequent change costing 100 extra"); added: Succession Law switch starts at 400 Civics (+100 per switch), Judge leaders pay 100 [V3 MB-OW 2025.11.26]. (c) R1 L3 "4 families, 10 classes" `[M]`: **4 families per kingdom** [V3 SS-OW]; the 2023 wiki civ list shows 10 distinct classes (Champions, Hunters, Patrons, Clerics, Artisans, Traders, Sages, Riders, Statesmen, Landowners) [V3 FW-OW Civilizations 2023-07-06, stale]. (d) R1 Orders: two older sources give the 0.1 figures (see 2.8), not withdrawn-with-no-source as v2 said, but unconfirmed for the current build.
- **Attachment claim:** consolidated_twenty_games.md line 400, "Old World has an explicit character ambition and family system in a 4X frame": **verified** (ambitions generated from events and leader desires; four noble families per kingdom) [V3 FW-OW, SS-OW]. No attachment claims Orders or Legitimacy numbers.

---
### Pathfinder: Kingmaker - facts line
Owlcat Games (Steam store now lists publisher Knights Peak); isometric party CRPG on Pathfinder 1e rules with a kingdom-management layer; released 2018-09-25 [V3 Steam store API appdetails 640820, 2026-10-22]. Party play is real time with pause, plus a turn-based mode added 2020-08-18 [V3 Steam news appid 640820 gid 4828375451936483210]; the kingdom runs on a day clock. Version: **last patch 2.1.7b (2021-05-27)**, store title now "Enhanced Plus Edition"; no later patch appears in news through 2026-10-22 [V3 SN-PK listing, 100 items; PKW bug boxes say "ver=2.1.7b"]. Assumed: Main Story, Normal difficulty, kingdom setting Normal, one created character. One play session: a playthrough is "an estimated 80 hours" [V3 PKW:Quests 2024-09-06]; the kingdom starts only when chapter 1 ends `[M]` ~8-12 h in.
**Sourcing: strong on kingdom rules (fan wiki that tabulates game data, plus Owlcat's own patch notes and dev diary); thin on party-layer feel (combat, camp, exploration), which is [M] except where cited.** Shorthand: PKW:<Page> = [V3 https://pathfinderkingmaker.fandom.com/wiki/<Page>, wikitext fetched via api.php, revision dates: Kingdom 2025-11-02, Advisors 2025-08-26, Build points 2025-10-13, Crisis Points 2023-07-15, Kingdom events 2026-09-30, Kingdom problems 2026-10-06, Kingdom opportunities 2026-10-08, Kingdom projects 2026-05-14, Throne room events 2025-10-12, Regions 2025-08-16, Settlements 2025-10-20, How to Build a Kingdom (HTBK) 2022-10-05, Difficulty levels 2021-10-20, Character creation 2025-10-20, Stolen Land 2025-07-14, Against All Odds 2024-12-09]. SN-PK = Steam news; GG = [V3 gamerguides.com .../chapter-2-dire-narlmarches-expedition/first-day-on-the-job, undated]; MGW = [V3 magicgameworld.com/?p=25087, undated]. The wiki is volunteer-edited and shared with a sequel; counts I give for events are my tallies of its tables.

#### 1. Setup choices
1. **Scenario.** Main Story (you become baron), Varnhold's Lot (standalone side story), Beneath the Stolen Lands (standalone roguelike dungeon) [V3 PKW:Character creation].
2. **Difficulty.** Presets Story, Easy, Normal, Challenging, Hard, Unfair, or Custom: damage taken (Story -80% ... Unfair double), Death's Door, crit strength, enemy strength, Auto Level Up (Off / Companions / All), **Kingdom management: Auto, Easy, Normal or Hard (Auto cannot be switched off once on)**, Last Azlanti mode (one save, game over deletes it) [V3 PKW:Difficulty levels, pre-2.1.7].
3. **Character.** Build your own or take one of 5 premades (Hedwirg fighter, Melaku paladin, Vyleen ranger, Gimar sorcerer, Yadmilla cleric). Races: Human, Elf, Dwarf, Gnome, Halfling, Half-Elf, Half-Orc, Aasimar, Tiefling (DLC). 16 classes (Alchemist to Wizard; Kineticist DLC), 3 archetypes each, 7 prestige classes later [V3 PKW:Character creation]. Ability scores, skills, feats, deity, one of 9 alignments. **You are the ruler, not an advisor**, so your own scores matter for the party, not for kingdom rolls.
4. **Alignment** gates dialogue lines and some event outcomes; the kingdom's alignment unlocks buildings (Noticeboard for Lawful, orphanage for Good) [V3 PKW:Kingdom, Advisors].
5. **In-play setup:** which envoy attends your baronation (Shandra Mervey or Lander Lebeda; at the coronation one of Kassil Aldori / Shandra / Lander, exclusive), kingdom name and motto (when they are set: `?`), and which companions you recruit and place as advisors [V3 PKW:A Noble Welcome, Advisors; SN-PK gid 3978319116836382244].

#### 2. The loop
Two nested loops. Adventure loop: explore areas in real time with pause (or turn-based), fight, talk, camp, travel the global map; every day of travel or rest advances the calendar (12 months mirroring Gregorian names, 365 days; game starts 15 Gozran 4710) [V3 PKW:Calendar 2025-10-05, PKW:The First Step...]. Kingdom loop, in order:
1. **Clock:** days. Events and projects count down in days; BP income lands weekly; the barony's own counter reads "Day N" from founding [V3 PKW:Build points, Throne room events]. Kingdom screen opens only inside your territory [S3 WebSearch 2026-10-22, fan-guide summary, page not opened].
2. **Game adds cards:** problems (stat penalty if failed or left to expire), opportunities (reward on success, little or no penalty), projects (no deadline, usually cost BP), throne-room visitors (need you in person) [V3 PKW:Kingdom events, projects].
3. **You assign one free advisor per card** (card shows who can handle it, the DC, your success chance, days) [V3 SN-PK gid 2408775863526376718, HTBK]. The advisor is busy until the card ends.
4. **Resolution when the days run out** (not when you open the screen): d20 + advisor's governing attribute modifier + 2 per rank of that advisor's stat + unrest modifier (Serene +1 ... Crumbling -4) vs the card's DC [V3 PKW:Kingdom events, Kingdom; HTBK]. Bands: Disaster 8+ under, Failure 1-7 under, Success 0-6 over, Triumph 7+ over. You may spend Crisis Points first.
5. **Weekly:** BP income tallies; if BP is negative, unrest climbs each day that passes [V3 PKW:Build points].
6. **Interrupts:** throne-room audiences (rank-up talks, quest visitors); story problems that tick stat losses every few days; chapter deadlines that end the game (section 6).
7. **Automated:** in Auto mode the game assigns advisors and skips time itself [V3 SN-PK gid 2465065785311762620, patch 1.3: "automatic kingdom management could get stuck and refuse to skip time"]; rank-ups and region claims auto-skip 14 days either way [V3 PKW:HTBK].

#### 3. The choice menu
| verb / choice | cost | effect | when picked |
|---|---|---|---|
| Assign an advisor to a card | advisor busy ~7-45 days (problems median 14) | d20 roll; stats and BP change | **constantly** |
| Spend Crisis Points on a roll | 1+ CP (5 at start, +1 per rank-up) | +5 each (=+25 points of chance); a Disaster becomes a Failure [V3 PKW:Crisis Points, GG] | occasionally |
| Start a project | BP (about 50-200) and an advisor | permanent buffs, trade pacts, unlocks | often |
| Rank-up audience (a stat passes each multiple of 20) | visit throne room, pick a reply; then 14-day project | +1 rank: +2 to that advisor's rolls, +1 BP/week (capped by Economy rank), +1 CP, new options | roughly 10 stats x up to 9 ranks, rarely each |
| Build or upgrade a building | BP and days; slot adjacency matters | stat bonuses, income, artisan workshops | **constantly early** |
| Claim a region | 150-400 BP, prerequisite, advisor, 14 days | land, bonuses, new settlement sites | every few play-hours (12 claimable) |
| Found a settlement / upgrade it | 50 BP; town 100 BP 7 d; capital to city 200 BP 7 d | more slots | per region; rarely |
| Buy BP with gold | 80 gold per BP | instant BP | whenever short |
| Appoint or replace an advisor | none; they quit at 3 net displeasure | rolls, event outcomes | as roles unlock |
| Tax and policy posture | set inside Economy rank-up replies (Low / High / Wealth taxes) | buffs and weekly BP | rarely |
| Feast for the Afflicted | 200 BP, +200 each repeat | unrest improves | when unrest is high |
| Order artisan work | workshop cost (Bokken 30 BP) | monthly gifts (items) | early |
| Adventure verbs: pick quest order, fight, dialogue, camp | game-days, rations | story and chapter clocks | **constantly** |

#### 4. First hour, step by step
The kingdom does not exist for the first hours; steps 1-5 are the party layer, 6-14 follow the game's own "How to Build a Kingdom" quest chain [V3 PKW:HTBK journal KDM_01..KDM_17].
1. New Game > Main Story > difficulty > build a character or take a premade; start at Jamandi Aldori's mansion, 15 Gozran 4710 12:00; an assassin attacks; follow Linzi, save Tartuccio; Jaethal, Harrim and Valerie join (Amiri appears but joins later) [V3 PKW:The First Step on the Road to Glory].
2. Resolve the "Fire in the Mansion" book event (skill-check text event, party-wide damage on failures).
3. **Stolen Land** starts a 90-day clock; go to Oleg's Trading Post (a guaranteed tutorial encounter with 3 thylacines), defend it; alignment-gated replies change the fight [V3 PKW:Stolen Land].
4. Choose your order among Thorn Ford bandits, the Abandoned Hut, the Temple of the Elk and the Stag Lord's fort; optimal is 20-25 days, finishing within 30 earns extra rewards [V3 same].
5. Kill the Stag Lord; at the reception pick an envoy; take the barony [V3 PKW:A Noble Welcome]. The quest How to Build a Kingdom starts.
6. Open the kingdom screen. **Appoint an advisor** (companions fill four of the five starting posts, Treasurer is empty; 18 xp) [V3 HTBK].
7. Start a building in the capital Tuskdale: a Longhouse in the middle of the 3x3 grid, or for a Lawful ruler a Noticeboard (+2 to event rolls in its region) [V3 HTBK].
8. Claim the Outskirts: 150 BP and a Regent, Councilor or Treasurer; time skips 14 days [V3 HTBK, GG]. Buy BP with gold if short (80:1).
9. Found a village on the Outskirts (50 BP, near water for a pier slot).
10. Events appear: assign advisors, read the success chance, use a Crisis Point only if the chance is low; results are fixed at completion so an earlier save re-rolls [V3 HTBK].
11. Resolve ten events (quest objective); a stat reaches 20: talk to that advisor in the throne room, then run the 14-day rank-up project [V3 HTBK, PKW:Kingdom].
12. The first fixed-schedule threat, An Ancient Curse, shows a vague journal countdown (about 42 days); at 14 days left Eight-Legged Plague drains Community and Loyalty every other day until handled [V3 PKW:An Ancient Curse 2022-08-25].
13. Do the Court Alchemist errand; build Bokken's workshop (30 BP, 10 days) so artisan gifts start [V3 HTBK].
14. Start Troll Trouble (trolls generate more problems the longer it waits), then claim South Narlmarches and Kamelands for the first town upgrade [V3 HTBK].

#### 5. What changes later
- Advisor posts 6-10 open when an earlier stat hits rank III and 60 points; regions, rank-ups and settlements multiply the cards each month [V3 PKW:Advisors, Regions]. The wiki counts about 300 events and 100 projects (my tally of its tables: 111 problems DC 13-40, 87 opportunities DC 12-37, 59 story events DC 11-45) [V3 PKW:Kingdom, Kingdom problems, opportunities].
- Barony to kingdom at the coronation: the 30 BP/week Brevoy subsidy and 50% tax end, rank cap 6 lifts [V3 PKW:Kingdom, Build points]. Region taxes unlock after the Economy VI audience.
- Pressure ramps by schedule: chapter deadlines sit at barony days 278, 486, 690, 940, then War of the River Kings (X+60); An Ancient Curse recurs in seven parts; fey-invasion "doom counter" at Day 1500-1600 [V3 PKW:Throne room events, Against All Odds].
- Advisor strength must climb: each rank adds +2, an attribute-boosted companion reaches about +8 to +11 [V3 PKW:Advisors table].

#### 6. Failure and ending
- **Kingdom destroyed = game over.** Unrest runs Serene, Stable, Worried, Troubled, Rioting, Crumbling; below Crumbling the realm is destroyed [V3 PKW:Kingdom]. Negative BP while time passes drives unrest; -5 ends the game [V3 PKW:Build points]. Stability rank-ups lower unrest one step each; a feast also helps [V3 SN-PK gid 2411028931158848761].
- **Run out of time:** five scripted "Game Over" throne-room events (trolls, Bloom monsters or plague, Oculus, barbarians, Pitax) fire if the chapter quest is undone by its day [V3 PKW:Throne room events]. Missing Stolen Land's 90 days: consequence not read `?`.
- Your death is game over (on Normal after Death's Door); companions can be raised. No kingdom recovery except reloading; Last Azlanti deletes saves [V3 PKW:Difficulty levels].
- **Ending:** after the First World chapters, slides vary by Nyrissa (let go, ally, absorbed Briar), whether the First Crown went to Shyka, and Lantern King patronage vs lifting the curse [V3 PKW:Kingdom ending slides]. Winning is finishing the story, not a kingdom score.

#### 7. Consequential vs cosmetic choices
- **Consequential:** filling every post and matching high-attribute advisors to the stats where problems bite. My arithmetic on the formula: Amiri STR 16 (+3) at rank 3 gives +9, needing a 16 on the d20 against the median problem DC of 25 (25% chance) before Crisis Points; at rank 10 with +11 she gives +31 (certain against DC 25, 60% against DC 40) [V3 formula; PKW:Advisors].
- **Consequential:** BP floor and quest order. Losing the buffer drops unrest, which lowers every roll; deadlines are the real lose condition [V3 PKW:Build points, Throne room events].
- **Consequential:** triage when cards outnumber free advisors; forum advice is to clear crises before side quests because unresolved ones spawn harder problems `[S3 search summary of fan guides]`.
- **Cosmetic or dominated:** gold to BP at 80:1 (the wiki says players are "overflowing with wealth"); rank-up reply choices have "no major effect" per GG apart from flavor and advisor displeasure; the wiki calls kingdom management "more of a mini-game than a necessity", its only lasting stake being failure [V3 HTBK, GG]. Both are community opinion, not tested.

#### 8. Open items
- Unknown: spawn rule and rate of random cards `?`; consequence of missing the 90-day limit `?`; whether "Auto" was called "Effortless" earlier (v2 cites SN 1.1, not re-opened) `?`; Coronation barony day `?`. Roll text says "higher than the DC" but bands put equal as Success [CONTESTED, minor]. PKW:Kingdom says 14 regions, PKW:Regions says 13 with 12 claimable [CONTESTED, minor].
- **v2 R1 PK cells settled:** (a) B1 stat-to-role map was only partly known: Community-Regent (CHA), Loyalty-Councilor (WIS), Military-General (STR), Economy-Treasurer (INT), Divine-High Priest (WIS), Relations-Grand Diplomat (CHA), Stability-Warden (CON), Arcane-Magister (INT), Culture-Curator (CHA), Espionage-Minister (DEX); first five open at start [V3 PKW:Kingdom, Advisors]; GG says later posts open at rank IV, wiki says rank III plus 60 [CONTESTED]. (b) B2 `?` -4 found: mercenaries take -4 on the attribute modifier and pick neutral replies [V3 PKW:Advisors, GG]. (c) B6 "advisors' stats drop as unrest rises" is wrong: unrest is a roll modifier (+1 to -4); advisors instead keep a hidden displeasure counter and leave at 3 [V3 PKW:Kingdom, Advisors]. (d) D2 NO [M] becomes PART: tax posture via Economy rank-up buffs Low / High / Wealth Taxes [V3 PKW:Throne room events]. (e) Events `?`: formula and DC ranges above; Crisis Points start at 5, +1 per rank-up, +5 each [V3 HTBK, GG]; whether Hassuf sells them is [CONTESTED] (dev diary 2019: "buy a limited amount" [V3 SN-PK gid 2411028931158848761]; PKW:Crisis Points: "can not be bought"). (f) C3: city needs 3 towns and 16 occupied capital slots (200 BP); town project 100 BP, 6 occupied slots, unlock "Have 6/9/12 Settlements" for towns 2-4 per wiki (Settlements page: every third) vs "3 / 5 regions" per MGW [CONTESTED]. (g) M1 "time-limited campaign [M]" refined to per-chapter deadlines above. (h) G1/H1/K1 [M]: turn-based mode exists since 2020-08-18. (i) A1-A5, C4 [M]: 9 races, 16 classes, adjacency effects confirmed [V3 PKW:Character creation, HTBK]. (j) E1 confirmed: 30 BP tax-free subsidy, 50% tax on other income until coronation [V3 PKW:Build points]. B7 stays NO `[M]`; no succession found, PC death ends the run.
- Capability line (ids B,D,F,H,L only): B1 YES[V3 PKW:Advisors] B2 PART[V3 PKW:Advisors: mercenary hire, no firing] B3 YES[V3 PKW:Advisors: 10 posts] B4 YES[V3 PKW:Kingdom events] B5 PART[V3 PKW:Difficulty levels: irreversible Auto] B6 PART[V3 PKW:Advisors: hidden counter] B7 NO[M] | D1 NO[M] D2 PART[V3 PKW:Throne room events] D3 YES[V3 PKW:Advisors] D4 YES[V3 PKW:Kingdom: unrest ladder] D5 NO[M] D6 PART[V3 PKW:Throne room events: verdict-style replies, no trials] | F1 NO[M] F2 PART[V3 PKW:Difficulty levels: party of six] F3 PART[M] F4 YES[V3 SN-PK gid 4828375451936483210: real time + turn-based] F5 NO[M] F6 PART[M: scripted fort assaults] F7 YES[V3 PKW:Settlements: camping supplies] F8 NO[M] | H1 YES[V3 PKW:Stolen Land: Diplomacy DCs, alignment lines] H2 PART[V3 SN-PK gid 2408775863523623580: companion mood] H3 PART[V3 PKW:Kingdom: Espionage stat] H4 YES[V3 PKW:Kingdom: alliances, trade pacts; romance] H5 PART[V3 PKW:Build points: vassal of Brevoy] H6 PART[M: scripted war with Pitax] | L1 YES[V3 PKW:Advisors] L2 PART[M: deaths only] L3 NO[M] L4 PART[V3 PKW:Kingdom events: authored pool] L5 PART[M: advisors/rivals scripted]
