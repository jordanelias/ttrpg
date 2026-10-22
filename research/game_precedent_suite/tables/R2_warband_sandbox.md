# R2 (v2, verified): Warband-style sandboxes (Bannerlord, Warband, Battle Brothers, Kenshi)

Method note (v2, 2026-10-22). Tags: [V2 id] = I read the text in a fetched page body this session; `id` keys the "Sources (v2)" list, which gives URL and the page's date/version. [S2 id] = search-result snippet only, page not opened (weaker). [M] = memory, not re-checked. [CONTESTED] = sources disagree. `?` = could not establish. Fandom (402), Fextralife (mostly 404), taleworlds.com News (403), Prima/gamewatcher (403) and web.archive.org (tool-blocked) stayed closed; GitHub code search is blocked in this session, so no game data files were read. Old tags S0..S25 from the first pass are dropped.

---
## 1. Mount & Blade II: Bannerlord (TaleWorlds, strategy/action RPG sandbox)
Versions (checked this pass). Early Access 30 Mar 2020 (Steam page), full release 25 Oct 2022 [V2 b7]. War Sails naval DLC announced 20 Mar 2025, slipped from 17 Jun 2025, launched 26 Nov 2025 [V2 b1, b2]. **1.3.x is stable, not beta**: the free base-game update shipped with War Sails as patch v1.3.4 (articles title it "v1.3.0 - v1.3.4"), 26 Nov 2025 [V2 b2]; v1.3.14 on PC early Feb 2026 [V2 b3]; v1.4.0 reached consoles 17 Jun 2026 (the article labels its notes "Beta v1.4.0") [V2 b4]; v1.4.7 + War Sails v1.2.7 on PC and consoles 8 Jul 2026 [V2 b5]; **latest found: v1.4.8 + War Sails v1.2.8 on PC, 18 Aug 2026** (console update 1.37/1.038) [V2 b6]. Nothing newer found; whether a v1.4.9 exists is `?`. The first pass's "1.3 is beta, newest patch unknown" was stale by 11 months. Clan-tier/companion numbers below come from undated guides and 2021 forum posts (the 1.2/1.5-era game); no source I could open states them for 1.4.x.

| id | val | how |
|---|---|---|
| A1 | YES | Player hero fights in person in battles [V2 b1] |
| A2 | YES | Creation walks six stages (Family, Early Childhood, Adolescence, Youth, Young Adulthood, Story Background) that "influence your skills and attribute points" [V2 b30]; per-stage grants not read |
| A3 | YES | Attributes, skills, focus, perks; Leadership perk "We Pledge our Swords" at skill 250 raises companion limit [V2 b9] |
| A4 | YES | Equipment slots, smithing, horses, weight [M] |
| A5 | YES | Four companion roles (Scout, Engineer, Quartermaster, Surgeon), one each; family does not count against the cap [V2 b9] |
| B1 | YES | Clan screen lists parties, companions, family, fiefs, workshops [M] |
| B2 | YES | Companions cost "generally 1,400-3,000 denars" [V2 b9]; troops recruited from every non-hostile settlement [V2 b21]; tavern mercenaries and garrison draft [M], not on the page |
| B3 | YES | Governors assigned to fiefs "to offload managing your fiefs to a trusted clan member" [V2 b13]; party and caravan leaders [M] |
| B4 | PART | One of four roles per companion [V2 b9]; no work-priority board [M] |
| B5 | PART | Governor runs a fief with small bonuses [V2 b13]; party AI [M]; no schedules [M] |
| B6 | PART | Companions "more likely to leave or even betray" if you act against them [V2 b9]; per-fief loyalty (see D4) [V2 b31] |
| B7 | YES | On death choose heir from spouse, siblings, children, extended kin; none left = observer only, load or restart [V2 b20, b1] |
| C1 | PART | Fiefs come by conquest or by vote on who receives a captured fief [V2 b11]; founding a kingdom needs a fief [S2 b32]; cannot found towns [M] |
| C2 | YES | Per-fief project queue; progress per day set by population; villages inherit bonuses from bound town/castle [V2 b13] |
| C3 | PART | Projects have levels; no demolish or layout [M] |
| C4 | NO | Projects are list items; no placement [V2 b13 implies; M] |
| C5 | PART | Workshops (limit by clan tier) and caravans [V2 b8, b1]; workshops in towns with loyalty <25 stop producing but still cost upkeep (1.3) [V2 b10] |
| C6 | NO | No supply lines between fiefs [M] (first pass cited a snippet; downgraded) |
| C7 | YES | Guard House project spawns a town patrol party (1.3) [V2 b10]; garrison, wall level, militia [M] |
| D1 | YES | Kingdom "Policies" tab: propose new or vote to repeal; kingdom-wide [V2 b12] |
| D2 | PART | **No tax-rate control found.** Oct 2020 forum posts ask for a slider as a missing feature [V2 b17]; 1.3 notes list tax rebalances (village +30%, town/castle +130% in beta), not a control [V2 b10]; policies change tax [S2 b33]. Current-patch absence unverified |
| D3 | PART | Governors per fief; kingdom screen has Clans/Fiefs/Policies/Armies, no ministers [V2 b12]; clan "roles" [V2 b9] |
| D4 | YES | Fief loyalty drifts toward 50; >75 gives ruler a tax bonus (cap 20% at 100); rebellion chance below 25 (slight) and 15 (high), only if militia exceeds garrison [V2 b31]; 1.3: workshops stop at loyalty <25 [V2 b10] |
| D5 | YES | Decisions: policies, war/peace, annexation, clan expulsion, fief distribution; clans vote, influence pays [V2 b11, b12] |
| D6 | NO | No trials or sentences [M] |
| E1 | YES | Gold, food, goods, influence, renown [M] |
| E2 | YES | Town markets with supply/demand [M] |
| E3 | YES | Caravan costs 15,000-18,000 denars by merchant, needs one companion leader, pays back "within a few in-game weeks" [V2 b25]; 1.3 trade agreements "boost caravan traffic" [V2 b2] |
| E4 | PART | Gold only [M] |
| E5 | YES | Smithing; workshops [M] |
| E6 | YES | Party and garrison wages [M] |
| F1 | YES | Recruit at settlements, upgrade with XP + gold (cavalry also a horse) [V2 b21] |
| F2 | YES | Faction leaders assign objectives to armies in the Armies tab [V2 b12]; cohesion/officers [M] |
| F3 | YES | Deployment phase, formations [M] |
| F4 | YES | Number keys 1-8 select formations; F1 Movement, F2 facing, F3 Formation, F4 fire, F5 mount, F6 delegate to sergeant, F7 retreat [V2 b22] |
| F5 | YES | Simulated battles and sieges; 1.3 adds morale, retreat, loss at zero morale [V2 b10] |
| F6 | YES | Siege engines, campaign-map bombardment of walls, murder holes [V2 b1] |
| F7 | PART | Food and wages; no foraging layer [M] |
| F8 | YES | Sim morale/retreat [V2 b10]; in-battle rout [M] |
| G1 | YES | Real-time melee/ranged/mounted [V2 b1] |
| G2 | YES | Many weapon/armour classes, smithing [M] |
| G3 | PART | Death in battle is a difficulty setting: Freebooter no hero deaths; Warrior heroes die, player cannot; Bannerlord preset heroes and player can die [V2 b19]; troops wounded/killed [M] |
| G4 | PART | Tournaments across towns; winning gives +1 daily renown [V2 b8] |
| G5 | PART | 1.3 stealth for prison breaks, hideouts, hostile-town infiltration; disguise needs a contact [V2 b2, b10] |
| H1 | YES | Persuasion: fill a progress bar by pushing arguments [V2 b1] |
| H2 | YES | Relation per hero; voting changes relation with sponsor [V2 b11] |
| H3 | PART | Quests/issues; no plot engine [M] |
| H4 | YES | Spouse, children [V2 b1]; 1.3 alliances (2 per kingdom), trade agreements (2, one year, war cancels) [V2 b10]; June 2026 revised alliance/trade rules and a renewal decision [V2 b4] |
| H5 | PART | Mercenary and vassal service [V2 b8, b14]; ransom/tribute [M]; 1.3 war scoring covers "war, peace, and tribute decisions" [V2 b2] |
| H6 | YES | War and peace are kingdom decisions [V2 b11]; 1.3 war-progress score [V2 b2] |
| I1 | PART | Quest clues only [M] |
| I2 | NO | [M] |
| I3 | PART | 1.3 contacts inside towns [V2 b10]; tavern talk [M] |
| I4 | PART | Disguise: first infiltration of a town needs a contact [V2 b10] |
| I6 | PART | Party sight radius, Scouting [M] |
| J1-J3 | NO | None in vanilla [M] |
| K1 | YES | Overland party movement; difficulty adds map speed bonus [V2 b19] |
| K2 | PART | Terrain speed [M] |
| K3 | PART | Food and starvation [M]; disease `?` |
| K4 | PART | Hideouts, villages; no fog-of-war discovery [M] |
| K5 | NO | [M] |
| L1 | YES | Lords hold relations and decide votes on interest, influence, cost, relation to sponsor [V2 b11]; personality traits [M] |
| L2 | YES | Heroes die of disease/old age, "most likely over 60" [V2 b20] (b20 calls this the only death; b19 shows battle death is a preset option [CONTESTED]); 18-year adulthood [M] |
| L3 | YES | Spouse, children inherit soldiers and fiefs [V2 b1] |
| L4 | PART | Random events came with the free War Sails-era update [V2 b1]; "short moments of decision" [V2 b2] |
| L5 | YES | AI lords raise armies; AI clans vote [V2 b11, b12] |
| M1 | PART | No win state found; ends if you die with no heir [V2 b20]; scripted ending absent [M] |
| M2 | PART | Kingdom founding runs through the Dragon Banner questline (Neretze's Folly first; then Arzagos or Istiana) [S2 b32]; clan-tier requirement 3 vs 4 [CONTESTED]; fetch of the guide failed |
| M3 | YES | Fiefs, relations, wars persist [M] |
| M4 | PART | Tooltips explain numbers [M] |
| M5 | YES | Map, party, battle, fief views [M] |

Mechanics worth knowing for a designer comparing a faction/roster/policy/combat/investigation game
- **Clan tiers (6)**: renown 50 / 150 / 350 / 900 / 2,350 / 6,150 for tiers 1-6 (Gamer Empire table, undated) [V2 b8]. A Steam post says "6,000" needed for tier 6, a rounding by a player [S2]. Same table: workshop limit 4/5/6/7 at tiers 3-6, parties 2/3/4 at tiers 2-4, "+15 party size" from tier 2 [V2 b8]. Dev blog (Jul 2019): "each tier gives an extra party slot and an increased companion limit" [V2 b14].
- **Companion cap [CONTESTED below tier 4]**: Gamer Guides: starts at 4, +1 per new tier [V2 b9] (=9 at tier 6). Gamer Empire table: tier 2=4, 3=5, 4=7, 5=8, 6=9 (a 5-to-7 jump, internally odd) [V2 b8]. Both and a Jun 2021 Steam post (9 companions at tier 6; 10 with perks) agree on **9 at tier 6** [V2 b23]; the low-tier values differ by one or two. Family does not count [V2 b9].
- **Tier unlocks [CONTESTED]**: Gamer Empire: mercenary at tier 1, vassal at tier 2, found kingdom at tier 4 [V2 b8]; 2019 dev blog says mercenary needs "the second tier" [V2 b14]; a search summary says guides give vassal at tier 3 and kingdom quests at 3 or 4 [S2 b32]. Not settled.
- **Politics**: four decision families (policies, war/peace, annexation, clan expulsion), plus fief distribution; "varying costs per type"; a ruler overruling a decision pays influence "equivalent to the difference between the majority and minority vote" [V2 b11]. Clan AI weighs interest, available influence, chance/cost to succeed, time since last vote, relation to sponsor; supporters gain relation with the sponsor they back [V2 b11]. **Vote costs `?`**: no official number found. Early-access forum posts: a policy "costs 50" to bring to a vote, "net -100" if nobody backs it (Apr 2020, speculative) [V2 b16]; a TrueAchievements guide says 100 [S2 b35]. The first pass's "about 100 to propose, 40 per clan to vote against" is not found anywhere; treat as unsupported.
- **Influence flows**: Forum starts at 1/day; Supreme Authority +1 as ruler, Prominence +1 as vassal; tournament win +10 (Champion perk) [V2 b18]. 2020 early-access change: losing a fief costs 50 influence (town), 25 (castle); Council of the Commons 1.0 to 0.1 per notable [V2 b15]. Retracting a fief from another lord costs "a large sum" and needs a lord vote, then a second vote on the recipient [V2 b12].
- **Fief management**: projects queue; progress/day follows population; housing "daily project" adds +1 population/day [V2 b13]. 1.3 (beta text, 18 Sep 2025): settlements start with a military, economic or balanced focus; village taxes +30%, town/castle +130% [V2 b10]. Whether these numbers survived to the stable release is unverified.
- **Battle death model**: heroes' deaths are a difficulty switch (Freebooter none; Warrior: not you; Bannerlord: you and heroes), with clan-member death rate 0% / 50% / 100% by preset [V2 b19].
- **Persuasion and skills**: persuasion is a progress bar; courtship and barter use it [V2 b1].

---
## 2. Mount & Blade: Warband (differences from Bannerlord only; no table, as in v1)
Version: standalone expansion of Mount & Blade, TaleWorlds; Windows 30 Mar 2010 (NA) / 2 Apr 2010 (EU); consoles 2016; Napoleonic Wars 19 Apr 2012; Viking Conquest 11 Dec 2014 [V2 w2]. Final patch number `?` (Wikipedia gives none). Every Warband claim here is forum- or guide-grade: no official Warband document could be opened.
- **Rent is automatic, not collected in person.** A 2015 thread: rent is "automatically figured into your weekly budget"; cities pay most, then well-kept villages, castles least; rent is lost when a village is pillaged or its castle/town is taken [V2 w1]. Search summaries add that Warband "removed the need to visit" and that income accumulates if you skip weeks, and that "tax inefficiency" cuts fief rent by up to 65% as you hold more fiefs [S2 w7]. The first pass's "collected in person (tax cart/rent)" was wrong for Warband (that is the original Mount & Blade; not re-checked).
- **Politics**: over the original, Warband added "more political options" and "the ability to start your own faction by capturing a town or castle" [V2 w2]. Players report: giving a fief to one lord costs about 2-3 relation with passed-over lords; a feast gives about +1 relation per day; a **marshal** role exists for the king's war leader [V2 w3, 2021 thread, player claims]. Lords are won one by one by talking; Bannerlord's influence screen replaced that (the "thinner" opinion was a forum summary; not re-opened).
- **Claimants/pretenders exist**: taverns point to claimants; you pledge to one, and on success the claimant names you marshal; whether you must first give up your own kingdom is disputed within one thread [V2 w4, Jun 2017; CONTESTED, low-grade]. Needed renown: `?`.
- **Family**: marriage exists ("you can marry ladies") [V2 w2]; children, heirs and old-age death are Bannerlord additions [V2 b1 for Bannerlord; Warband absence M]. The first pass's "no family" was too strong.
- **Sieges**: attackers wait while the army leader builds "ladders or tower", then assault [V2 w5, Dec 2015]; no rams or catapults mentioned there (not proof of absence). Bannerlord sieges are "intended to be more strategic than in Warband" [V2 b1].
- **Ending**: "no set objectives", common goal is conquering Calradia [V2 w2]; original Mount & Blade has "no overarching storyline" [V2 w6]. Vassals "manage and collect taxes" from a fief [V2 w6].
- **Calendar**: Bannerlord year is 84 days, four 21-day seasons (in-game calendar, Steam thread Apr 2022) [V2 b24]. Warband year length `?` (v1's "12 months of ~30 days" dropped, unsourced).
- Still [M]: companion cap tied to party size/Leadership; Warband troop trees upgrade on XP alone (Bannerlord adds a gold cost and a horse for cavalry [V2 b21 for the Bannerlord half]); formation keys F1-F3 for classes; companions-as-roles absent.

---
## 3. Battle Brothers (Overhype Studios, turn-based tactical mercenary-company sim)
Version: Windows full release 24 Mar 2017; Switch 11 Mar 2021; PS4/PS5/Xbox 13 Jan 2022; Hooded Horse acquired PC publishing 2 Dec 2025 (consoles unaffected) [V2 x1]. Steam lists DLC Of Flesh and Faith (free), Lindwurm (free), Blazing Deserts, Warriors of the North, Beasts & Exploration [V2 x2]. **Latest patch found: 1.5.2.2, reported 19 Jun 2026 (prior 1.5.1.8)**; it adds Pollaxe, Executioner's Sword, Estoc, Brigand Marauders, Men at Arms for noble armies [V2 x3]. Nothing newer found, but the shared search budget ran out, so "newest" is not exhaustive.

| id | val | how |
|---|---|---|
| A1 | PART | No avatar by default; **Lone Wolf origin** gives one hedge knight who cannot be fired and whose death ends the campaign [V2 x5] |
| A2 | PART | Company origins (Militia, Cultists, Lone Wolf, Northern Raiders, Slave Drivers, Gladiators...) each with own start and special rules [V2 x4, x5, x6]; recruits have random backgrounds [V2 x2] |
| A3 | YES | No classes; eight attributes plus a perk tree [V2 x2]; perk counts and tier-lock rule [S2 earlier snippet, unverified] |
| A4 | YES | Per-brother gear, shared stash [M] |
| A5 | YES | Whole company fights, but only 12 per battle by default (see B1) [V2 x4, x8] |
| B1 | YES | Roster plus reserve; **caps are origin-dependent** (see bullets) [V2 x4-x9; CONTESTED] |
| B2 | YES | Hire "procedurally generated hopefuls" in towns [V2 x2]; dismiss [M] |
| B3, B5, B7 | NO | No titles, standing orders or succession [M] |
| B4 | PART | Choose who fights; no jobs [M] |
| B6 | YES | Battle morale states; mood and traits [M] (Steam page does not mention) |
| C1-C7 | NO | Company holds no land [M]; Cultists origin and DLCs change starts only [V2 x4] |
| D1-D6 | NO | None [M] |
| E1 | YES | Gold, food, tools, ammo, medicine [M]; "you have to pay and feed your brothers" [V2 x11] |
| E2 | PART | Town buy/sell lists [M]; Militia home village "offers great prices" [V2 x4] |
| E3 | NO | No caravans [M] |
| E6 | YES | Daily wages and food [V2 x11]; the v1 figure "~500/day for 18" is unverified and dropped |
| F1 | PART | Hire individuals only [V2 x2] |
| F4 | YES | Turn-based grid combat (hex per a review snippet [S2 x13]) with heights, terrain, fatigue [M] |
| F8 | YES | Enemy morale and rout [M] |
| G1 | YES | Action points, one unit at a time [M] |
| G2 | YES | Weapon and armour layers, called shots [M]; 1.5.2.2 adds three weapon types [V2 x3] |
| G3 | YES | Injuries temporary or permanent, some "permanently reduce a warrior's abilities"; permadeath; optional no-save-scum [V2 x2, x1] |
| G4 | PART | Duel contract [M] |
| G5 | NO | No stealth [M] |
| H1, I1-I6 | NO | Contracts and events text only [M] |
| H2 | PART | Faction relations with houses/cities [M] |
| H6 | PART | Noble wars are a crisis [V2 x2]; you take sides via contracts [M] |
| J1 | NO | None; undead and greenskins are enemies [V2 x2] |
| J2 | PART | Cultists origin: Davkul demands sacrifices; cultists get permanent boons; non-cultists react [V2 x4]; Of Flesh and Faith DLC content [M] |
| K1 | YES | Real-time travel between settlements on a procedural world [V2 x2] |
| K2, K3, K4 | YES | Terrain, food per day, ruins/loot sites [M] |
| L1 | PART | Backgrounds and traits, no goals [V2 x2 backgrounds] |
| L2 | NO | Brothers do not age or breed [M] |
| L4 | YES | Crises (noble wars, undead uprising, Greenskin invasion) reshape the world [V2 x2] |
| L5 | YES | World factions act during crises [V2 x2 "reshape the world"; settlement-change detail M] |
| M1 | PART | Late-game crises; no fixed victory; ends if company or Lone Wolf dies [V2 x1, x5; M] |
| M3 | YES | Permadeath, injuries, crisis outcomes [V2 x1, x2] |
| M4 | PART | Hit chance shown [M] |

Mechanics worth knowing for a designer
- **Battle cap is 12 by default**; forum posters say "the entire game is balanced around a party of 12" (Dec 2018) [V2 x8]; dev blog: "the usual maximum in battle is 12" [V2 x4].
- **The 12-vs-16 dispute is origin-dependent, not a single number**: Slave Drivers "up to 16 into battle" (dev blog 13 Jun 2020) [V2 x6]; Militia 18 in battle (dev blog 9 Feb 2019, pre-release, "details may change") [V2 x4] versus 16 in battle and 25 roster per the wiki (search summary only) [S2 x12] and a Jun 2019 forum "16 with a peasant army" [V2 x7]. Lone Wolf and Gladiators cap the roster at 12 [V2 x5, x6].
- **Default roster cap [CONTESTED]**: 18 ("18 battle brothers at once, 12 in combat", Feb 2017) [V2 x9]; 20 (Jun 2019 post asks "why 20 slots?", answered "reserve for wounded") [V2 x7]. My memory says 20 in the shipped game [M]; later patches unchecked.
- **Scaling**: one 2020 poster says the world scales off your "12 highest level brothers", reserves included [V2 x10] (single forum claim).
- Attrition is the design core: temporary vs permanent injury, permadeath, optional save-scum block, configurable difficulty and opening crisis [V2 x1, x2].
- Lone Wolf: single hedge knight fights front line; his death ends the campaign [V2 x5]. Nothing like clans, fiefs, policies or votes: BB is the roster/injury/morale reference only.

---
## 4. Kenshi (Lo-Fi Games, squad-based sandbox RPG)
Version: Early Access Mar 2013; full release 6 Dec 2018 [V2 k2, k1]. Steam threads: "0.99" 5 Dec 2018, "1.0 Out Now!" 9 Oct 2019, "1.0.64" 6 Feb 2024 [V2 k3]. **Latest numbered patch is `?`**: 1.0.65 hotfix and 1.0.67 appear in a Steam event listing dated 27 May 2025 and 25 Sep 2025 [V2 k4], but search snippets dated the same posts 5 Apr 2024 and 29 Nov 2024 [S2 k5] and a trainer site lists 1.0.68 [S2]; the two date sets conflict [CONTESTED]. Sales passed three million by May 2026; Kenshi 2 (Unreal Engine prequel, announced Mar 2019) has no release date [V2 k2].

| id | val | how |
|---|---|---|
| A1 | PART | "No hero characters"; you command a squad [V2 k1] |
| A2 | YES | Custom-designed characters, many races [V2 k1, k2] |
| A3 | YES | Skills rise by doing; stats and appearance change with experience; no difficulty scaling to your level [V2 k2, k1] |
| A4 | YES | Gear; prosthetic limbs [V2 k1 prosthetics; M gear] |
| A5 | YES | Recruit named and generic characters from many factions and species [V2 k2] |
| B1 | YES | Squad list [M] |
| B2 | YES | Recruit from factions [V2 k2]; buy/free slaves, capture [M] |
| B3, B7 | NO | No offices or succession [M] |
| B4 | YES | Per-member job queue in priority order; Shift makes a task permanent [S2 k5, guide not opened] |
| B5 | YES | "Squad AI ... can handle base management" [V2 k1]; guard/stance orders [M] |
| B6 | PART | Hunger, rest; no morale meter [M] |
| C1 | PART | "Purchase and upgrade your own buildings"; eventually an outpost [V2 k1, k2] |
| C2, C3 | YES | Build and upgrade fortified buildings or businesses [V2 k1] |
| C4 | PART | Free placement, no zoning [M] |
| C5 | YES | "Research and craft gear" [V2 k1]; mining/farming chains [M] |
| C6 | NO | Haulers move within base only [M] |
| C7 | YES | Walls, turrets, guards; unfortified bases get raided [M] |
| D1 | PART | Support or oppose factions; no laws [V2 k1] |
| D3, D5 | NO | None [M] |
| D6 | PART | Slavery, imprisonment, bounties ("trader to slave" roles) [V2 k1; rest M] |
| E1, E2 | YES | Items, food, shops with varying prices [M] |
| E3 | PART | Player carries goods; no caravans [M] |
| E5 | YES | Crafting [V2 k1] |
| E6 | NO | No wages [M] |
| F1, F2 | PART | Squads of any size; factions fight each other [M] |
| F4 | YES | Real-time-with-pause squad command; "RTS and RPG elements" [V2 k1; pause M] |
| G1 | YES | Real-time melee/ranged [M] |
| G2 | YES | Weapon/armour classes [M] |
| G3 | YES | Per-body-part health; severed limbs, prosthetics; blood loss knocks characters out; injuries affect movement and combat [V2 k2, k1] |
| G5 | PART | Stealth skill (thievery from use) [V2 k2 "stealing builds thievery"] |
| H1 | NO | Menus only [M] |
| H2 | YES | Faction relations change with actions [V2 k1 "support or oppose"] |
| H6 | PART | Factions fight; player influence limited [M] |
| I1-I6, J1, J3 | NO | None; setting "avoids fantasy clichés and magic" [V2 k1] |
| K1 | YES | "870 square kilometers" [V2 k1] |
| K2 | YES | Terrain and weather hazards [M] |
| K3 | YES | Hunger, blood loss [V2 k1]; race-specific hunger [S2] |
| K4 | YES | Ruins, hidden places [M] |
| K5 | PART | Beds for rest [S2 earlier snippet] |
| L1 | PART | Named NPCs; "every NPC is potentially your equal" [V2 k1] |
| L2 | NO | No aging/birth in play [M] |
| L4 | YES | Unscripted capture by cannibals/slavers; "world keeps changing whether or not you act" [V2 k1]; world states [V2 k2] |
| L5 | YES | A notable's death can spawn locations or let factions take towns [V2 k2] |
| M1 | NO | "Open-ended sandbox ... rather than a linear story" [V2 k1] |
| M3 | YES | Limbs lost, faction attitudes, world states persist [V2 k1, k2] |

Mechanics worth knowing for a designer
- **No level scaling, no hero**: difficulty does not adapt to you; early survival is a struggle [V2 k1].
- **Delegation**: squad AI carries wounded to safety and can handle base management [V2 k1]; per-member job queue with priority order [S2 k5].
- **Injury model**: per-body-part health, limb loss, prosthetics, blood-loss knockouts [V2 k1, k2]; skeleton-race repair details unverified.
- **World states**: notable deaths spawn locations or let factions take towns [V2 k2]; random capture events are unscripted [V2 k1].
- Closest to Valoria's no-GM sandbox in feel, with no governance layer; no ending.

---
## Still unknown
- Bannerlord policy-proposal and vote influence costs in 1.4.x: tried dev blogs, Gamer Guides, forums, TrueAchievements; no official number. Settle: read DefaultKingdomDecisionModel / the in-game proposal tooltip.
- Bannerlord clan-tier table in 1.4.x and companion cap for tiers 1-3: guides undated; Fandom/Prima/taleworlds.com closed. Settle: in-game Clan screen, or a decompiled DefaultClanTierModel (GitHub search blocked here).
- Whether Bannerlord 1.4.8 is the newest, and whether a tax-rate control exists in 1.4.x: Steam news and TaleWorlds forum closed.
- Bannerlord disease (K3), I1/I6 detail, M1 win state: no source opened.
- Warband: needed renown for claimants, final patch, year length, upgrade cost, siege-engine set: strategywiki (403) and Fandom (402) closed.
- Battle Brothers: shipped default roster cap (18 vs 20) and whether any 2026 patch changed it; perk counts; wage scale. Settle: battlebrothers.fandom.com or Steam update history.
- Kenshi: newest version number and true dates of 1.0.65-1.0.68; job-queue details (Steam guide fetch hit 429).

## Sources
Bannerlord
b1 https://en.wikipedia.org/wiki/Mount_%26_Blade_II:_Bannerlord
b2 https://mp1st.com/title-updates-and-patches/mount-blade-2-bannerlord-update-1-026-1-25-out-war-sails-expansion (26 Nov 2025; also ?p=299447)
b3 https://mp1st.com/title-updates-and-patches/mount-blade-2-bannerlord-new-update-1-32-1-033-version-1-3-14-consoles (9 Feb 2026)
b4 https://mp1st.com/?p=309105 (17 Jun 2026)
b5 https://mp1st.com/title-updates-and-patches/mount-blade-2-bannerlord-update-july-8-brings-patch-1-35-1-036 (8 Jul 2026)
b6 https://mp1st.com/title-updates-and-patches/mount-blade-2-bannerlord-new-update-1-37-1-038 (18 Aug 2026)
b7 https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/
b8 https://gamerempire.net/mount-blade-2-bannerlord-how-to-increase-clan-tier/ (undated)
b9 https://gamerguides.com/mount-and-blade-ii-bannerlord/guide/introduction/character-development/companions (undated)
b10 https://www.holy.gg/de/post/bannerlord-update-1-3-beta-guide-how-to-play-major-patch-notes (18 Sep 2025, beta)
b11 https://www.gamebanshee.com/3whda (dev blog 7 Dec 2019)
b12 http://www.gamebanshee.com/k4h96 (dev blog 5 Oct 2018)
b13 https://www.gamebanshee.com/k4qhy (dev blog 8 Dec 2018)
b14 http://www.gamebanshee.com/kccy3 (dev blog 19 Jul 2019)
b15 http://www.gamebanshee.com/383f8 (patch e1.3.0, 10 May 2020)
b16 https://steamcommunity.com/app/261550/discussions/0/4233889512147599279 (Apr 2020)
b17 https://steamcommunity.com/app/261550/discussions/0/2935742047971254525 (Oct 2020)
b18 https://www.gamerguides.com/mount-and-blade-ii-bannerlord/guide/introduction/useful-gameplay-tips/how-to-gain-influence
b19 https://gamersdecide.com/articles/mount-and-blade-bannerlord-difficulty-levels
b20 https://gamerempire.net/mount-blade-2-bannerlord-what-happens-if-you-die/
b21 https://mountandblade2bannerlord.wiki.fextralife.com/Troops (footer: edited 9 Oct 2026)
b22 https://www.gamerguides.com/mount-and-blade-ii-bannerlord/guide/introduction/useful-gameplay-tips/tactics
b23 https://steamcommunity.com/app/261550/discussions/0/3112530528180876720 (Jun 2021)
b24 https://steamcommunity.com/app/261550/discussions/0/3272436038137248707 (Apr 2022)
b25 https://www.gamerguides.com/mount-and-blade-ii-bannerlord/guide/economy/how-to-make-money/investing-in-a-caravan
b30 https://www.greenmangaming.com/intel-feature/taleworlds/bannerlord-character-creation/
b31 https://gamerempire.net/mount-blade-2-bannerlord-town-loyalty-guide/
[S2] b32 https://www.gamewatcher.com/mount-and-blade-2-bannerlord-how-to-become-king and https://windowscentral.com/how-create-your-own-kingdom-mount-blade-ii-bannerlord (fetch returned navigation only); b33 https://earth.gamerguides.com/mount-and-blade-ii-bannerlord/guide/perks/intelligence; b35 https://i2.trueachievements.com/a374423/lawmaker-achievement (403)
Warband
w1 https://steamcommunity.com/app/48700/discussions/0/530649887212562367 (Aug 2015)
w2 https://en.wikipedia.org/wiki/Mount_%26_Blade:_Warband
w3 https://steamcommunity.com/app/48700/discussions/0/3031473435696296429 (Aug-Sep 2021)
w4 https://steamcommunity.com/app/48700/discussions/0/1353742967815735288 (Jun 2017)
w5 https://steamcommunity.com/app/48700/discussions/0/451848854994350346 (Dec 2015)
w6 https://en.wikipedia.org/wiki/Mount_%26_Blade
[S2] w7 https://strategywiki.org/wiki/Mount%26Blade/Fiefs and https://mountandblade.fandom.com/wiki/Taxes (both closed; summary only)
Battle Brothers
x1 https://en.wikipedia.org/wiki/Battle_Brothers
x2 https://store.steampowered.com/app/365360/Battle_Brothers/
x3 https://turnbasedlovers.com/news/a-new-update-for-strategy-rpg-battle-brothers-has-suddenly-arrived/ (19 Jun 2026)
x4 http://www.gamebanshee.com/k4ywr (dev blog #113, 9 Feb 2019)
x5 https://www.gamebanshee.com/k4y6q (dev blog #114, 16 Feb 2019)
x6 http://www.gamebanshee.com/3d8qw (dev blog #140, 13 Jun 2020)
x7 https://steamcommunity.com/app/365360/discussions/0/1644292549032541080 (Jun 2019)
x8 https://steamcommunity.com/app/365360/discussions/0/1742229167188787787 (Dec 2018)
x9 https://steamcommunity.com/app/365360/discussions/0/135510194250427957 (Feb 2017)
x10 https://steamcommunity.com/app/365360/discussions/0/2971775284257693403 (Nov 2020)
x11 https://gideonsgaming.com/battle-brothers-complete-review/ (Jul 2021, upd. Apr 2023)
[S2] x12 https://battlebrothers.fandom.com/wiki/Peasant_Militia (402); x13 https://rpgamer.com/review/battle-brothers-review/ (403)
Kenshi
k1 https://store.steampowered.com/app/233860/Kenshi/
k2 https://en.wikipedia.org/wiki/Kenshi_(video_game)
k3 https://steamcommunity.com/app/233860/discussions
k4 https://steamcommunity.com/app/233860/eventcomments (event listing; its years conflict with k3 and k5)
[S2] k5 search snippets: steamcommunity.com/app/233860 hub (1.0.65 hotfix, 1.0.67) and Steam guide id=2359162973 (fetch 429)
