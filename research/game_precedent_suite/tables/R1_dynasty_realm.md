# R1 - Dynasty / realm games vs Valoria capability checklist (v2, verified 2026-10-22)

Tags: [V2 url ver] read in a fetched page/file body this session; [S2 url] search snippet only; [M] memory, not re-checked; `?` not established; [CONTESTED].
Shorthands (each is a full [V2] tag when followed by a path or id):
- **GF-CK3** = https://github.com/jesec/ck3-mod-base (git clone; CK3 vanilla game files, HEAD commit d4cbb83 "Version 1.20.1.2 (Crozier)", 2026-10-21), paths under `base/game/`. Game data = executable truth for numbers; a reader of the .txt is reading what the engine reads.
- **SN-CK3** = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1158310 (Steam announcements, full text), cited by gid.
- **CK3-Council** = https://ck3.paradoxwikis.com/Council (WebFetch returned the body; says "verified for the current PC version (1.20)").
Paradox wiki (other pages), Paradox forum, Fandom, hoodedhorse, StrategyWiki: Cloudflare/"Client Challenge" for curl and WebFetch; web.archive.org blocked by the egress proxy (tunnel closed). Not worked around.
Changes from v1 are logged at the end. Cells I did not re-check keep [M].

---
## 1. Crusader Kings III (Paradox, grand strategy / dynasty sim)
Version relied on: **1.20.1.2 "Crozier"** (Steam update 2026-10-21; 1.20.0 with DLC By God Alone 2026-09-30) [V2 SN-CK3 gid 1847286114028159 / 1845383656377574]. Next DLC Silk & Silver (republics/merchants) announced for Nov 2026, not in these numbers.
Player is ONE character (the ruler). **Game over = your lineage dies out with no player heir**; you may then take over any other ruler; default **end date 1453** (game rule can disable) [V2 GF localization/english/game_concepts_l_english.yml game_over, end_date; common/game_rules/00_game_rules.txt end_date].

| id | val | how |
|---|---|---|
| A1 | YES | Play one ruler; on death continue as heir [V2 GF game_concepts game_over] |
| A2 | YES | Ruler designer, traits, education interactions [M]; education file exists [V2 GF character_interactions/00_education_interactions.txt] |
| A3 | YES | Five skills + lifestyles with perk trees [M]; `lifestyles/00_lifestyles.txt` exists [V2 GF common/lifestyles] |
| A4 | PART | Artifacts (equip, inheritable), no loadout depth [M]; `common/artifacts` exists [V2 GF] |
| A5 | PART | Courtiers/knights/commanders; no party control [M] |
| B1 | YES | Court/Vassals/Council tabs list every character with opinion, traits [M] (v1 tag rested on a search snippet) |
| B2 | PART | Invite to court, hire courtiers, mercenary captains by interaction [M]; `00_courtier_and_guest_interactions.txt` exists [V2 GF] |
| B3 | YES | Grant titles (`00_grant_titles_interaction.txt` [V2 GF]); council seats [V2 CK3-Council]; court positions [M] |
| B4 | YES | One council task per councillor (below) [V2 CK3-Council] |
| B5 | PART | Council tasks run on their own once set [V2 CK3-Council]; vassal levies/taxes automatic by contract [V2 GF subject_contracts/contracts/feudal.txt] |
| B6 | YES | Opinion, stress (max level 3 [V2 GF defines/00_defines.txt MAX_STRESS_LEVEL]), hooks (weak/strong blackmail, favor, obligation, indebted [V2 GF hook_types/00_hook_types.txt]), factions (liberty, claimant, peasant, populist [V2 GF factions/]) |
| B7 | YES | Per-title succession laws: partition, high partition, single-heir (4 keys), clan partitions (5), acclamation, appointment + 8 elective systems (feudal, princely, gaelic, saxon, scandinavian, tribal, confederation, theocratic) [V2 GF laws/00_succession_laws.txt, succession_election/]. Which is default at a given start: [M] |
| C1 | PART | Claim/conquer counties; no `found_*` decision exists in `common/decisions` (grep empty); Nomad/camp domiciles are DLC [V2 GF absence, M for DLC] |
| C2 | PART | Holdings and buildings; **barony 2 slots, county 3 slots** [V2 GF defines BARONY_BUILDING_SLOTS=2, COUNTY_BUILDING_SLOTS=3] |
| C3 | PART | Upgrade/replace buildings [M] |
| C4 | NO | Fixed slots per barony/county [V2 GF defines, same lines] |
| C5 | NO | No production chains; flat modifiers [M] |
| C6 | NO | No supply lines for goods; armies have supply/attrition [V2 GF defines SUPPLY_STATE_ATTRITION, ATTRITION_AFTER_DAYS=30] |
| C7 | PART | Garrison via levies/men-at-arms; sieges [M] |
| D1 | YES | Realm laws; **crown authority 4 levels; change cooldown 20 y (tribal 10, nomadic 5, church 20; the cooldown check is skipped for cultures with the All-Things innovation)** [V2 GF laws/00_realm_laws.txt L1-7, L80-90] |
| D2 | PART | Vassal contract tax levels exempt/low/normal/high/extortionate = **0 / 2.5% / 10% / 15% / 25%** of vassal income; separate levy contract [V2 GF subject_contracts/contracts/feudal.txt, script_values/00_goverment_values.txt L75-79]. No per-pop rate. |
| D3 | YES | Chancellor, Steward, Marshal, Spymaster, religious councillor, Confidant [V2 CK3-Council] |
| D4 | PART | Opinion, factions, dread, tyranny (illegitimate imprison/revoke) [V2 GF game_concepts dread/tyranny]; **realm Legitimacy with levels** that move marriage/alliance acceptance, claim-CB cost, faction numbers [V2 GF legitimacy/00_legitimacy.txt]. No unrest number. |
| D5 | PART | Elective succession votes among electors (8 systems above) [V2 GF succession_election/]; no standing assembly |
| D6 | PART | Imprison/ransom/execute (`00_prison_interactions.txt` [V2 GF]); no trial mechanic [M] |
| E1 | PART | Gold ("all liquid assets"), prestige, piety, dread scalar stocks [V2 GF game_concepts gold/prestige/piety/dread]; renown, influence [M] |
| E4 | PART | Gold; loans exist (`var:loan_amount_owed`, `loan_holder` in `00_gift.txt` [V2 GF]); no markets [M] |
| E6 | YES | Army/court costs vs income [M] |
| F1 | YES | Levies, men-at-arms (111 top-level type keys across 10 files), mercenaries [V2 GF men_at_arms_types/ count of top-level keys; M for mercs] |
| F2 | YES | Commanders appointed; Marshal task Train Commanders [V2 CK3-Council] |
| F3 | PART | Army raised and sent; no deployment grid [M] |
| F4 | NO | Armies move on the map; a battle starts when two armies enter the same barony, advantage from terrain/commander/traits, casualties from damage; no player control inside [V2 GF localization/english/game_concepts_l_english.yml game_concept_battle_desc] |
| F5 | YES | All battles auto-resolved (same source as F4) [V2 GF game_concepts] |
| F6 | YES | Sieges: daily morale loss, siege weapons, monthly attrition [V2 GF defines NSiege BASE_DAILY_MORALE_LOSS=1, MONTHLY_ATTRITION=0.01] |
| F7 | PART | Attrition after 30 days; supply states [V2 GF defines L642-703] |
| F8 | YES | Siege morale: defender base 100 + 75 per fort level, daily loss [V2 GF defines L980-985]; field-battle morale and retreat [M] |
| G1 | NO | No tactical combat [M] |
| G3 | YES | Traits wounded_1-3, maimed, one_eyed, one_legged, disfigured, infirm [V2 GF common/traits/00_traits.txt]; battle death and dynasty continues [M] |
| G4 | PART | Duels (`force_duel_criminals/anyone_interaction` [V2 GF 00_trait_interactions.txt]); Tournament activity [V2 GF activities/tournament.txt] |
| G5 | PART | Murder and Abduct schemes (hostile category, secret) [V2 GF schemes/scheme_types]; no ambush play [M] |
| H1 | PART | Interaction menus with acceptance (`ai_accept` blocks in interaction files [V2 GF]); no dialogue tree [M] |
| H2 | YES | Opinion per pair with modifiers (`opinion_modifiers/`), hooks, rivals, friends [V2 GF dir exists; M for UI] |
| H3 | YES | **Scheme list, from `scheme_types/`:** hostile Murder, Abduct, Fabricate Hook, Claim Throne, Seize Realm, Steal Back Artifact/Herd; personal Befriend, Elope, study/mentoring; basic Sway, Seduce, Courting; political Slander, Depose, Promote, Expand Power Base, Damage Legitimacy; contract (adventurer) schemes [V2 GF common/schemes/scheme_types file+category lines]. **"Fabricate Claim" is a Religious-councillor task, not a scheme** [V2 CK3-Council]. |
| H4 | YES | Marriage/betrothal/alliance interactions [V2 GF 00_marriage_interactions.txt, 00_alliance.txt] |
| H5 | YES | Hostages (offer/demand/exchange/return/recall [V2 GF 05_bp2_interactions.txt]), ransom, tribute (`00_tributary_interactions.txt`), vassal contracts |
| H6 | YES | Casus belli, war declaration, peace terms [V2 GF casus_belli_types/, 00_war.txt exist] |
| I3 | PART | Event notifications; no rumour propagation [M] |
| I4 | PART | Spymaster tasks (Disrupt/Support Schemes, Find Secrets) [V2 CK3-Council]; agents inside schemes [V2 SN-CK3 gid 6250522009531192816] |
| I6 | PART | 19 top-level entries in `secret_types/` [V2 GF]; schemes are hidden but breaches/discovery leak them (see below); no map fog [M] |
| J2 | YES | Religion types, faith types, doctrines, tenets, rites, holy sites as data (`common/religion/*`) [V2 GF]; By God Alone (1.20) reworks Christianity [V2 SN-CK3 gid 1845383656377574] |
| J3 | PART | Stress, 3 levels [V2 GF defines MAX_STRESS_LEVEL=3] |
| K1 | YES | Army map movement; character travel (`common/travel` [V2 GF]) |
| L1 | YES | **~306 top-level definitions in `traits/00_traits.txt`** [V2 GF; some are not traits]; AI goals (`ai_goaltypes/`). v1 "ambitions" is NOT a CK3 mechanic (no match in game_concepts) |
| L2 | YES | Aging, birth, death, inheritance, genetics (`genes/`, `dna_data/` exist [V2 GF]) |
| L3 | YES | Houses, dynasties, dynasty legacies/perks (`dynasty_houses`, `dynasty_legacies`, `house_unities` [V2 GF dirs]) |
| L4 | YES | Event system, random and trait-driven [M] |
| L5 | YES | AI rulers declare wars, plot, marry [M]; `ai_goaltypes`, `ai_war_stances` exist [V2 GF] |
| M1 | PART | **Default end date 1453; game over when your lineage ends without a player heir; you can continue as another ruler** [V2 GF game_concepts end_date, game_over]. No victory condition. (v1 said "loss when dynasty extinct": wrong unit.) |
| M2 | NO | Sandbox with historical bookmarks [M] |
| M3 | YES | Grudges, claims, hooks, dynasty memory [M] |
| M4 | YES | Tooltips itemise opinion/acceptance [M] |
| M5 | PART | Map zoom plus character view; scale is single-ruler [M] |

Council verbs [V2 CK3-Council, PC 1.20]: one task per councillor; changing task loses progress except Integrate Title and Increase Development/Control in County; progress kept on death; one task event per year, none in first month; effect scales linearly with skill; Friend +20% / Best Friend +30% / Rival -20% / Nemesis -30% efficiency; standard council = 6 (Spymaster + Confidant for all, plus Chancellor, Steward, Marshal, religious councillor).
- Spymaster: Disrupt Schemes, Support Schemes, Find Secrets. Confidant: Assist Ruler, Court Politics, Chivalry, Manage Domain, Court Intrigue, Patronage.
- Chancellor: Foreign Affairs, Domestic Affairs, Integrate Title, Bestow Royal Favor (Court Grandeur 2+). Steward: Collect Taxes, Increase Development, Promote Culture, Promote Cultural Acceptance, Convince De Jure Territory (Grandeur 6+).
- Marshal: Organize Army, Train Commanders, Increase Control, Manage Royal Guards (Grandeur 3+). Religious: Religious Relations, Fabricate Claim on County, Convert Faith in County.
- DLC variants: Kurultai (nomads) 4 seats; Hegemony of China 8 ministers (Grand Chancellor, Grand Marshal, Personnel, War, Revenue, Works, Rites, Justice).

Mechanics worth knowing for a designer:
- **Schemes were reworked in 1.13.0 "Basileus" (2024-09-24)**: parameters Success Chance, Potential (max), Phases, Secrecy, Breaches, Advantages; basic schemes = one phase, success chance only (Sway) [V2 SN-CK3 gid 6341720536521348110]. v1's "multi-month hidden projects, undiscovered until executed" is the pre-1.13 model.
- Numbers for a "t2" hostile scheme (Murder, Abduct, Fabricate Hook) [V2 GF script_values/00_scheme_values.txt L385-430; schemes/scheme_types/murder_scheme.txt]: phase base **120 d** (t1 170 d, t3 70 d); owner skill -0.25 d/point, target skill +0.1 d/point, min 10 d, plus a target-tier add (barony 5, county 10, duchy 20, kingdom 40, empire 80, hegemony 160; defines NScheme says 'speed', unit presumably days); success grows **0.45 per owner skill point per phase** (t1 0.3, t3 0.6); **Potential base 30** before agents (t1 20, t3 40); hard caps **95** (hostile/personal/political), 100 (contract); **5 breaches** destroy the scheme; Murder cooldown 10 y, Fabricate Hook 2 y, Abduct 10 y, Claim Throne 2 y (uses Learning, t1 pace). Murder opens 5 agent slots (2 assassin, thug, infiltrator, alibi); base chance adds owner Intrigue, -20/-30/-40 against king/emperor/hegemon targets, -50 if at war with target.
- Basic schemes (Sway, Befriend, Seduce): one 365-day phase, -2.5 d per skill point, max 95; Sway/Befriend open, Seduce secret [V2 GF sway/befriend/seduce_scheme.txt].
- Designer's intent: old system "too random... binary"; ~5 agents max, each with an agent type that boosts speed, secrecy or success; ~6-month discovery grace then low monthly chance; player executes manually and can trade surplus Advantages for success; murder blockers: one-use roll plus repeatable blockers summed to max 75% [V2 SN-CK3 gid 6250522009531192816, Dev Diary #157, 2024-09-17, pre-release text].
- Laws: crown authority 0-3 = Autonomous Vassals / Limited / High / Absolute. Limited: tributaries, change between Partition laws, revoke titles, retract vassals. High: change among all succession laws, vassals cannot war on each other without a hook, no foreign inheritance, refusers of revocation become criminals. Absolute: vassals cannot wage any war without a hook, designate heir, +25% vassal tax and levy contribution. Cost: opinion malus by personality group (Absolute: baron -20, glory-hound -25, parochial -25, courtly -10, zealot -20, minority -30; belligerent +15) [V2 GF laws/00_realm_laws.txt L21-286; localization/english/laws_l_english.yml L29-36]. Raising a level costs prestige and needs `can_pass` and no cooldown.
- Automation: council tasks, levies and taxes run themselves; every interaction/scheme start is a player click [M].

---
## 2. Victoria 3 (Paradox, economic/political grand strategy)
Version relied on: **1.13.11 "Matcha"** = last hotfix before today (Steam 2026-08-19); 1.13 "The Great Wave" went live 2026-04-28 [V2 SN-V3 gid 1841579228662409, 1830797770244834]. Free update **1.15 + State and Revolution is scheduled for 2026-10-22** (today; 1.14 was an open beta merged into 1.15) [V2 SN-V3 gid 1842846814443874, 1844115010492106]; not confirmed live, numbers below are 1.13.11.
- **SN-V3** = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=529340 (Steam announcements, full text, by gid). **V3REF** = https://alcaras.github.io/v3ref/ (static site generated from the game's own `game/common` files; footer "Game 1.13.11 (Matcha) synced Aug 25, 2026"): pages `laws`, `defines`, `concepts`, `institutions`, `interest-groups`.
Player acts as the STATE (a Country), not a character. Characters have Roles: Ruler, Heir (monarchies only), Politician (interest-group leader), Commander (general/admiral) [V2 SN-V3 gid 4598757090450598746, Dev Diary #53, 2022-08-04].

| id | val | how |
|---|---|---|
| A1 | NO | "both human and AI players each control a Country"; characters are state officers [V2 V3REF concepts "Head of State"; SN-V3 gid 4598757090450598746] |
| A2 | PART | Pick country and starting laws [M] |
| A5 | NO | No party [M] |
| B1 | PART | Characters: ruler, heir, IG leaders, commanders, agitators; each with traits and Popularity [V2 SN-V3 gid 4598757090450598746] |
| B2 | PART | Agitators come via "Invite Exile" or appear at random by Literacy [V2 V3REF concepts Agitator]; commanders promoted [M] |
| B3 | PART | Choose which IGs sit in government; Governance Principles law fixes who rules; Grant Command lets a monarch command forces [V2 SN-V3 gid 4598757090450598746; V3REF concepts] |
| B4 | PART | Assign production methods, order generals to Fronts; no per-person job [M] |
| B5 | YES | Pops and buildings run themselves; player sets laws and budget [M] |
| B6 | YES | IG Approval bands angry <=-10, unhappy -5, happy >=5, loyal >=10; Radicals vs Loyalists per pop [V2 V3REF defines APPROVAL_THRESHOLD_*] |
| B7 | PART | Heirs exist in monarchies; ruler set by Governance Principles law; min ruler age for an heir 20 [V2 V3REF defines RULER_MIN_AGE_FOR_HEIR]; player cannot pick the heir [M] |
| C1 | PART | Colonize states, claim by diplomatic play [M] |
| C2 | YES | Buildings built by the Construction sector; costs are paid weekly in goods + wages, no lump sum [V2 SN-V3 gid 4018887653980585574 DD#12]. v1 "per-state queue / capped points": not confirmed, dropped |
| C3 | PART | Build/downsize, swap production methods [M] |
| C4 | NO | Per-state buildings, no layout [M] |
| C5 | YES | Goods, buildings, production methods and pop needs are separate datasets [V2 V3REF index] |
| C6 | PART | Infrastructure links a State to its Market; buildings consume Infrastructure [V2 V3REF concepts Infrastructure]; no supply-line map [M] |
| D1 | YES | **26 law groups, 138 laws**; one active law per group [V2 V3REF laws, concepts "Law Group"]. Enactment: 3 phases, checkpoint every **100 days by default** (150 for Distribution of Power, Economic System, Slavery; 200 Governance Principles), **730-day cooldown** after failure, **3 setbacks** fail it [V2 V3REF defines LAW_ENACTMENT_*; SN-V3 gid 5121196841288559912 DD#80]. One enactment at a time: stated by a 2022 fan guide ("you can only pass one law at a time", v1.0-era) [V2 thegamer 2022-10-26]; the 1.13.11 encyclopedia speaks of "the currently Enacting Law" (singular) and lets you Negotiate with an IG during enactment (Amenability) [V2 V3REF concepts Negotiation] |
| D2 | YES | Level setting per tax type: income, poll, land, consumption (costs Authority), dividend; wages/spending levels; raising taxes costs Legitimacy and breeds Radicals [V2 SN-V3 gid 4018887653980585574 DD#12, 2021 pre-release]. v1 "per sector": wrong unit |
| D3 | NO | No ministers; Bureaucracy is a capacity that also pays for Commanders [V2 V3REF concepts Bureaucracy] |
| D4 | YES | Legitimacy (IG-in-government fit to laws; slows enactment, resists coups), Radicals, Turmoil, Coup by low-Loyalty commander [V2 V3REF concepts] |
| D5 | YES | **Elections every 4 years, 6-month campaign**; after an election one free government reform [V2 V3REF defines ELECTION_INTERVAL_YEARS=4, CAMPAIGN_PERIOD_MONTHS=6; concepts Election] |
| D6 | PART | Law Enforcement institution (-10% state penalties from Turmoil per level) [V2 V3REF institutions]; no trials [M] |
| E1 | YES | Goods, stockpiles, markets [M]; Gold Reserve soft cap [V2 SN-V3 DD#12] |
| E2 | YES | Market prices from buy/sell orders [V2 V3REF concepts Market Access, Buy/Sell Orders]; per-market dynamics [M] |
| E3 | YES | Trade routes, tariffs, treaties [M] |
| E4 | YES | Weekly budget, Gold Reserve, loans, debt ceiling (default if breached), bankruptcy [V2 SN-V3 gid 4018887653980585574 DD#12; V3REF concepts Bankruptcy] |
| E5 | YES | Production methods [V2 V3REF index] |
| E6 | YES | Wages, government and military wages [V2 SN-V3 DD#12] |
| F1 | YES | Barracks/Conscription Centers raise Battalions; Mobilize [V2 V3REF concepts] |
| F2 | YES | Generals/admirals lead Formations [V2 V3REF concepts Fleet/Formation] |
| F3 | PART | Order a General to advance or defend a Front [V2 V3REF concepts Front] |
| F4 | NO | Battle starts when Advancement Progress fills; no tactical control [V2 V3REF concepts Advancement Progress] |
| F5 | YES | Wars play out automatically [M] |
| F8 | PART | Morale on Battalions/fronts [M] |
| H2 | PART | Relations between countries; IG approval [M] |
| H3 | PART | Agitators, diplomatic plays, subject manipulation [M] |
| H4 | PART | Treaty articles incl. Alliance; no marriage [V2 V3REF concepts Treaty] |
| H6 | YES | Diplomatic plays with war goals, then war; Infamy [V2 V3REF index, concepts Infamy] |
| J2 | PART | State religion, pop religion and acceptance [M] |
| L2 | PART | Pops grow by Standard of Living (birth/mortality); characters: ruler/heir only [V2 V3REF concepts Standard of Living] |
| L4 | PART | Journal entries and events [M] |
| L5 | YES | AI countries act [M] |
| M1 | PART | Campaign is 1836-1936 (achievement "play a full campaign from 1836 to 1936"); losing a revolution = Game Over [V2 SN-V3 gid 4584121659781205633 DD#55; gid 4353300134225504187 DD#41]. Score screen: [M] |
| M4 | YES | Tooltips and pop/movement breakdowns [M]; Political Movement panel "Supporting Pops" tab [V2 SN-V3 DD#80] |
| M5 | YES | Map-state-pop zoom [M] |

Mechanics worth knowing:
- Law enactment (since 1.3, 2023-04-06): each checkpoint rolls Success (next phase), Advance, Debate (event with choice) or Stall (harm); Success needs endorsement by an IG in government, a supporting Movement, or a positive chance by other means [V2 V3REF concepts; SN-V3 DD#80]. Chance inputs: clout of supporting IGs, +5% per step for ruler ideology and Law Commitment treaties; opposing clout scaled by approval x1.5 angry / x1.0 unhappy / x0.5 neutral [V2 V3REF defines LAW_ENACTMENT_RULER_IDEOLOGY_EFFECT=0.05, IG_ANGRY_MULT=1.5, IG_UNHAPPY_MULT=1, IG_NEUTRAL_MULT=0.5]. Cancelling while a Movement demands the law shoots its Radicalism up [V2 SN-V3 DD#80].
- 8 interest groups (Armed Forces, Devout, Industrialists, Intelligentsia, Landowners, Petite Bourgeoisie, Rural Folk, Trade Unions); each has leader ideologies and 3 traits keyed to loyal+/happy+/unhappy- approval [V2 V3REF interest-groups]. 7 institutions (Home Affairs, Colonial Affairs, Law Enforcement, Education, Health System, Workplace Safety Office, Social Security) funded by laws [V2 V3REF institutions]. v1 "~50 weeks per level, Legitimacy 60%+" is 2022 fan-guide level advice [V2 thegamer, 2022-10-26], not a rule.
- Three capacities: Authority (decrees, managing IGs, consumption taxes), Bureaucracy (grows with population and institution levels; pays Commanders), Influence (diplomacy) [V2 V3REF concepts Authority, Bureaucracy].
- Political strength = pops by size and wealth; Political Movements gain Support/Activism from Radicals and can turn Insurrectionary into civil war [V2 V3REF concepts Political Movement]. The control grain is the opposite of CK3: no individual reachable by the player, only laws, budgets and war orders.

---
## 3. Old World (Mohawk Games / Hooded Horse; 4X + dynasty, turn-based)
Version relied on: **main branch 1.0.84977 (2026-10-07)**, test branch 1.0.85174 (2026-10-21) [V2 SN-OW gid 1846018067927469; BN-OW "Old World Test update 2026.10.21"]. Still weekly-patched.
- **SN-OW** = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=597180. **BN-OW** = https://github.com/MohawkGames/test_buildnotes and **MB-OW** = https://github.com/MohawkGames/main_buildnotes (the developer's own test-branch and main-branch build notes, git clones; file names carry the date). **PCGN** = https://www.pcgamesn.com/old-world/review (launch-era review, WebFetch body). The hoodedhorse wiki returned HTTP 403 (curl and WebFetch); Fandom blocked; Steam store, Wikipedia, PC Gamer, mohawkgames.com pages opened but carry no rules.
Player is a Nation Leader (a character in a family) who spends Orders; 1 turn = 1 year [M].

| id | val | how |
|---|---|---|
| A1 | YES | "a singular leader and their family"; units act on Orders [V2 PCGN] |
| A2 | PART | Select a historical leader/nation at setup [V2 https://www.mohawkgames.com/oldworld/]; custom traits [M] |
| A3 | YES | Characters gain traits and ratings; leader archetypes (Zealot, Schemer, Tactician, Sage...) [V2 BN-OW 2023.10.11/2023.11.15/2024.07.11]; attribute names [M] |
| A5 | YES | Generals, governors, council members, agents are characters [M] |
| B1 | YES | Inheritance screen lists all branches; Notable Characters filter (Exploring, Imprisoned, Exiled, Rising Star, Power Hungry, Vengeful, Plotting, Bypassed) [V2 BN-OW 2023.01.05, 2024.07.31] |
| B2 | PART | Characters arrive by events/missions [M] |
| B3 | YES | Council posts: Chancellor, Ambassador, Spymaster (+ Agents), Grand Vizier only via events (Behind the Throne); slots can be disabled or need no trait [V2 MB-OW 2026.08.05, 2026.09.09, 2024.06.26; BN-OW 2024.04.24, 2025.04.02] |
| B4 | YES | Missions assign a character to a target (marriage, declare war, imprison, assassinate heir...) [V2 BN-OW 2023.01.18, 2025.06.19, 2025.10.08]; governors [M] |
| B5 | PART | Cities queue projects; units sentried [M] |
| B6 | YES | Character-to-character and family opinion; marriage matchmaking weighs attraction/hatred [V2 BN-OW 2025.02.05]; Legitimacy [V2 PCGN] |
| B7 | YES | Line of succession, lateral/dynastic succession, usurper seizing the throne, **regents forced for child leaders up to age 6 (age 12 if the leader abdicated)** [V2 BN-OW 2023.01.05, 2024.01.24, 2024.04.24, 2025.02.05] |
| C1 | YES | Found cities on sites; minor cities easier to create (2023-05-31) [V2 SN-OW gid 5151601211223589411] |
| C2 | YES | Improvements and city projects cost yields/Orders [M]; "Add Urban" costs Orders [V2 BN-OW 2026.05.13] |
| C3 | YES | Upgrade/pillage/rebuild improvements [M] |
| C5 | PART | Resources feed yields; Wonders [M] |
| C7 | YES | Garrisons give +1 Order (2025-05-21) and defend [V2 BN-OW 2025.05.21] |
| D1 | YES | Laws chosen in pairs; **first switch 200 Civics, each later change +100; abolishing a law raises that pair's cost by 100**; rival notices at 1/4/7 laws [V2 BN-OW 2024.09.25, 2024.03.13, 2026.10.21]; some laws carry Order upkeep (Guilds 0.5/city; Legal Code 6 Money/city) [V2 BN-OW 2026.03.04] |
| D3 | YES | Council posts (see B3) each yield a resource (Ambassador culture, Spymaster science, Chancellor Money/Civics) [V2 MB-OW 2026.09.09] |
| D4 | YES | Legitimacy sets the Orders per turn and is earned by "protecting and growing the nation" [V2 PCGN]; leader change costs it, Regents do not (2023-10-11) [V2 BN-OW 2023.10.11] |
| D5 | NO | None [M] |
| E1 | YES | Yields incl. Food, Wood, Stone, Iron, Money, Civics, Training, Orders [V2 BN-OW 2025.03.12, 2024.09.25, 2024.08.21 mentions] |
| E3 | PART | Caravans/trade missions [V2 BN-OW 2024.07.11] |
| F1 | YES | Train units in cities [M] |
| F4 | YES | Turn-based tactical combat on hexes [M] |
| F5 | NO | Combat is manual [M] |
| G1 | PART | Hex unit combat; leaders attach to units [M] |
| G3 | YES | Leaders can die; early-game protection for starting leaders lasts 20 turns [V2 BN-OW 2024.07.11] |
| H1 | NO | Missions and events, no dialogue [M] |
| H2 | YES | Opinion, attraction, "Vengeful", "Power Hungry" states [V2 BN-OW 2024.07.31, 2025.02.05] |
| H3 | YES | Plotting characters, assassinate/imprison missions [V2 BN-OW 2024.07.31, 2025.06.19, 2025.10.08] |
| H4 | YES | Marriage candidates incl. tribal leaders; alliances [V2 BN-OW 2023.05.17] |
| J2 | YES | Religions, Disciples, Temples/Monasteries/Cathedrals, theologies [V2 BN-OW 2025.01.22, 2023.09.20] |
| L1 | YES | Traits, archetypes, per-character goals [V2 BN-OW above] |
| L2 | YES | Aging, heirs, regents [V2 BN-OW 2024.01.24] |
| L3 | YES | Family Seats (one per family; cannot be gifted since 2025-01-22); count "4 families, 10 classes": [M] [V2 BN-OW 2025.01.22 for seats] |
| L4 | YES | Events (e.g. 9 new events in the 2024-04-04 release) [V2 SN-OW gid 5756237364308306545] |
| M1 | YES | **Several separately toggled victory conditions: Points, Ambition (10th Crowning Ambition), Double, Alliance, Time** (below). v1 "10 Ambitions or score at 200 turns" is incomplete, not wrong. |
| M2 | YES | Authored scenarios exist (Heroes of the Aegean, Pharaohs of the Nile, Rise of Carthage, The Hill) [V2 BN-OW 2025.04.09, 2025.05.07, 2025.01.22]. v1 row said "NO | Scenarios": self-contradictory, corrected |

Mechanics worth knowing:
- **Victory (BN-OW is the primary source; no rules page could be opened).** Points victory: a Victory Point threshold that scales with map size and player count, with a Points-to-Win setting (Low/Normal/High +25%/Very High +50%) and **no cap** (">100 VPs on Normal" on large maps) [V2 BN-OW 2024.03.20, 2024.05.08]; VP breakdown includes endgame techs, Wonders, Holy Sites and the Opulence project (Behind the Throne) [V2 BN-OW 2024.05.08, 2026.04.15, 2024.06.10]. Ambition victory: separate condition, **off by default in multiplayer since 2025-01-22** [V2 BN-OW 2025.01.22]. Double victory: "grants victory when a player doubles the score of the highest AI player" [V2 PCGN]. Alliance victory: setup option, default off [V2 BN-OW 2024.11.27]. Time victory: exists, "not disabled by default in some presets" was a bug [V2 BN-OW 2024.06.10]; PCGN (launch): "earning the most points within 200 turns". Since 2025-07-02 players may accept a victory or play on, and each condition is disabled for others once someone completes it (2025-08-13) [V2 BN-OW 2025.07.02, 2025.08.13].
- **"10 Ambitions to win" is right for the Ambition victory only.** Ambitions come in tiers; the 10th, a "Crowning Ambition", is "the 10th and final ambition you will be offered in order to claim an ambition victory" (5 added 2024-06-26, e.g. 6 cities with positive happiness, stockpile 2000 of each resource, send 20 luxuries) [V2 MB-OW "Old World Release Update 2024.06.26", main 1.0.72907]. PCGN calls ambitions "alternate victory paths" that "add Legitimacy" [V2 PCGN]. National Ambitions are excluded from the tier count [V2 BN-OW 2025.03.12]. +10/-5 Legitimacy on completing/abandoning: no source opened, `?`.
- **Orders.** "The number of Orders a player gets each turn is determined by their ruler's Legitimacy" [V2 PCGN]; it "puts a hard limit on the number of decisions a player can make each turn" [V2 PCGN]. Orders are also a yield with flat sources/sinks: Garrison +1 (was 0.5), Orators +1 per Friendly city, Divine Rule +1 per Pagan religion, rider Family Seat 1 then 2, law upkeep in Orders; Schemer leaders can buy Orders with Legitimacy at +1 Legitimacy per use (resets per leader) [V2 BN-OW 2025.05.21, 2023.02.01, 2024.08.28, 2024.03.13/2025.05.14, 2026.03.04, 2026.03.25]. **The exact formula is not established; v1's "~0.1 Orders per Legitimacy point and 0.1 per citizen" has no source in anything I could open and is withdrawn.**
- Legitimacy ties to action count (a political stat that is also a resource budget). Contrast with Valoria: Orders is a scarce per-turn budget that scales with a single political scalar.
- Succession and plots are first-class: regencies, usurpers, plotting/vengeful characters, assassination missions; ruler death does not end the game unless the dynasty ends [M].

---
## 4. Pathfinder: Kingmaker (Owlcat, CRPG with a kingdom layer)
Version relied on: **Enhanced Edition line, last patch 2.1.7b (2021-05-27)**; later sold as "Enhanced Plus Edition" [V2 SN-PK gid 4069544815356533175, 5124582150131355465]. SN-PK = https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=640820. Kingdom rules below mix pre-EE (v1.2, Feb 2019) and EE (2.0, June 2019) text; each cell names which. Player controls a party; the kingdom is a separate screen with its own calendar.

| id | val | how |
|---|---|---|
| A1-A5 | YES | Party of tabletop-style characters, class builds, inventory, companions [M] (not re-checked; core CRPG) |
| B1 | YES | **10 advisor roles: General, Treasurer, Grand Diplomat, Warden, Minister, Curator, Magister, High Priest, Regent, Councilor**; reaching rank 1 of a stat creates its advisor position [V2 space4games guide 2019-02-02, pre-EE v1.2: https://space4games.com/en/games-en/pathfinder-kingmaker-kingdom-and-advisors-guide/]. Stat-to-role map: only High Priest=Divine confirmed |
| B2 | PART | EE lets you appoint mercenaries (custom characters) to government roles; they have "a lower base chance of successfully resolving an event" and can wear magic items [V2 SN-PK gid 2411028931158848761 Developers' Diary: Kingdom Reforms, 2019-06-11; gid 2400895196212840499]. The v1 "-4" figure: not found, `?` |
| B3 | YES | Appoint companions/NPCs/mercenaries to the roles above [V2 same sources] |
| B4 | YES | Each kingdom event and project is assigned an advisor; the card shows who and days left [V2 SN-PK gid 2408775863526376718, EE beta 2019-05-25]. Advisor card shows which events they resolve better [V2 gid 2411028931158848761] |
| B5 | PART | "Auto" kingdom mode and an "Effortless" level (added 1.1, 2018-11-16) delegate management [V2 SN-PK gid 3316234163917015010, 3244179105162974537]. Events with day>20 can be resolved until end of next month [V2 gid 3316234163917015010] |
| B6 | PART | Unrest log; each Stability rank-up lowers unrest one step; feast 200 BP then 400, 600... [V2 gid 2411028931158848761]. v1 "advisors' stats drop as unrest rises": not found, `?` |
| B7 | NO | No succession [M] |
| C1 | YES | Annex regions; settlement upgrades gated on annexations [V2 space4games guide] |
| C2 | YES | Build in settlement plots with BP [V2 space4games guide: first upgrade raises plots to 20] |
| C3 | PART | Village to small town needs 3 annexed regions + 6 finished buildings [V2 space4games guide]; "city needs 3 towns": `?`. Cancelling a project refunds 90% [V2 SN-PK gid 3244179105162974537] |
| C4 | PART | Plot grid per settlement [V2 space4games guide]; building synergies [M] |
| D1 | NO | No laws [M] |
| D2 | NO | BP only; no tax slider [M] |
| D3 | YES | The 10 roles above [V2 space4games guide] |
| D4 | YES | 10 stats (Community, Loyalty, Military, Economy, Relations, Divine, Arcane, Stability, Culture, Espionage); a stat at 0 or below makes riots likely, low Stability can destroy the kingdom [V2 space4games guide]; kingdom can be destroyed by events [V2 SN-PK gid 2417769111279428182, 2400895196212840499] |
| E1 | PART | Build Points (BP): base 30/week from Brevoy while a vassal, +1 per stat rank capped by Economy rank [V2 space4games guide]; BP buyable in the kingdom window (EE) [V2 gid 2411028931158848761] |
| G1,H1,K1 | YES | Real-time-with-pause party combat, alignment-checked dialogue, global map travel [M] |
| M1 | PART | Kingdom destruction is a loss state [V2 SN-PK gid 2417769111279428182]; "time-limited campaign" [M, unverified] |
| M2 | YES | Authored quests, companion plots; kingdom events tied to quests [V2 SN-PK gid 2408775863523623580] |

Mechanics worth knowing:
- Rank growth: every 20 points in a stat is one rank via a two-week project; as a subordinate barony stats cap at rank 6 [V2 space4games guide, pre-EE]; ranks reach at least 10 (Divine rank 10 mentioned in 1.3 notes) [V2 SN-PK gid 2465065785311762620].
- Events resolve by an advisor roll; EE shows the roll and its modifiers; Crisis Points (one per rank-up, some buyable from Hassuf) add a one-shot bonus [V2 SN-PK gid 2408775863526376718, 2411028931158848761]. DC and bonus values: `?` (no source opened).
- Going into negative BP does not raise unrest until the next day (1.1) [V2 SN-PK gid 3316234163917015010].
- No laws, no succession, no policy list: governance = events + buildings + advisors, which is also why Auto mode exists.

---
## Still unknown
- CK3: default succession law per bookmark; full agent-type bonuses (`schemes/agent_types/agent_types.txt` not read); F3/F8/G3/L4/L5/M3-M5 and UI claims (B1, H1/H2 UI, M4) remain [M]. Tried: GF script files only; Paradox wiki, forum, Fandom, web.archive.org all blocked. Settle: read `agent_types.txt`, `common/governments`, GUI files from the same clone.
- Vic3: whether 1.15 is live; "one enactment at a time" in 1.13 (only a 2022 fan-guide source); score screen at 1936; trade-route and convoy rules. Tried: Steam news, V3REF defines/concepts. Settle: v3ref `laws` per-law data or the game's `common/laws` files.
- Old World: Orders-per-turn formula; number of families/classes; Legitimacy +10/-5 for Ambitions; default turn limit for Time victory; VP per ambition/wonder; Points-to-win base values. Tried: Steam news, both Mohawk build-note repos, PCGN, Steam store, Wikipedia; hoodedhorse wiki 403, Fandom blocked. Settle: the game's `Reference/XML/Infos` files or an opened wiki page.
- Kingmaker: stat-to-role map; event DC and advisor roll formula; mercenary penalty; EE-era settlement tier rules ("city needs 3 towns"); campaign time limit; unrest effects on advisors. Tried: Steam patch notes (all 191 items), gamebanshee diary, space4games guide; Fandom/StrategyWiki blocked. Settle: game blueprints (`KingdomStatsAndRoles`) or an opened wiki page.
- Web search budget was exhausted mid-session (shared limit), so several searches I wanted (Vic3 one-law rule, Kingmaker role map) were not run.

## Sources
- CK3 game files: https://github.com/jesec/ck3-mod-base (cloned; HEAD d4cbb83 "Version 1.20.1.2 (Crozier)", 2026-10-21); files cited by path in cells.
- https://ck3.paradoxwikis.com/Council (WebFetch body, "verified for 1.20"). Other ck3.paradoxwikis.com pages, forum.paradoxplaza.com, admin-forum: Client Challenge/500; https://web.archive.org: proxy tunnel closed.
- https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1158310 (CK3), ?appid=529340 (Victoria 3), ?appid=597180 (Old World), ?appid=640820 (Kingmaker); item gids cited in cells.
- https://alcaras.github.io/v3ref/ (laws, defines, concepts, institutions, interest-groups; game 1.13.11, synced 2026-08-25); https://github.com/alcaras/v3ref (README via WebFetch).
- https://www.thegamer.com/victoria-3-government-laws-reforms-institutions-elections/ (2022-10-26, v1.0-era). https://github.com/yosbotnet/vic3/blob/main/notes/tutorials/05-how-to-pass-laws.md (fan notes "1.12+", corroborates 100/150/200-day checkpoints; not used as primary).
- https://github.com/MohawkGames/test_buildnotes and https://github.com/MohawkGames/main_buildnotes (cloned; Old World build notes 2022-2026); https://www.pcgamesn.com/old-world/review; https://store.steampowered.com/app/597180/Old_World/; https://www.mohawkgames.com/oldworld/; https://en.wikipedia.org/wiki/Old_World_(video_game) (opened, no rules).
- https://space4games.com/en/games-en/pathfinder-kingmaker-kingdom-and-advisors-guide/ (2019-02-02, pre-EE); https://www.gamebanshee.com/khpra (mirror of the Kingdom Reforms diary).
- Searched, not opened for facts: https://www.gamewatcher.com/crusader-kings-3-schemes-secrets-hooks-intrigue, https://guildorder.com/games/ck3/guides/schemes-choosing-the-right-plot (opened: confirms 5 breaches / up to five agents / Advantage, no numbers).
