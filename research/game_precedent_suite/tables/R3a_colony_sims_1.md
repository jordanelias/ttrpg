# R3a (v2, verified) — Colony sims: Dwarf Fortress, RimWorld, Songs of Syx

Verification pass, 2026-10-22. Tags: `[V2 k]` = text read in a page body fetched this session; `k` is a source key whose URL and version/date are in "Sources (v2)" (so `[V2 k]` stands for `[V2 <url> <version/date>]`). `[S2 k]` = search snippet only. `[M]` = memory, not re-checked. `?` = not established. `[CONTESTED]` = sources disagree.
Access that worked: DF wiki and RimWorld wiki via `index.php?title=<Page>&action=raw` (plain curl, HTTP 200; the v1 agent's HTTP 429 did not recur). Songs of Syx: see section 3. Cells changed from the v1 draft are marked **(chg)**; full before/after is in the Verification log.

---
## 1. Dwarf Fortress (Bay 12 / Kitfox), Fortress + Adventure + Legends modes
Version relied on: the wiki's main-namespace pages carry the banner "about the current version of DF" `[V2 DFav]`; wiki current = **v53.16, released Aug 5, 2026** `[V2 DFver]`, matching the Bay 12 download line "DWARF FORTRESS CLASSIC 53.16 (August 5, 2026)" `[V2 DFb12]` (Steam build number not separately checked). The v1 draft used v0.31/DF2014 pages for nobles and military; those are superseded below. Pages flagged `{{old}}`/`{{buggy}}` by the wiki (Mission) are noted.

| id | cell | how |
|---|---|---|
| A1 | PART | Adventure mode = one controlled character, "open world roguelike" `[V2 DFadv]`; Fortress mode has no avatar, you issue labor/squad orders `[V2 DFsqd]`. |
| A3 | YES | Skills up to Legendary (migrants arrive with them) `[V2 DFimm]`; focus gives up to +/-50% effective skill `[V2 DFneed]`; use-based gain `[M]`. |
| A4 | YES | Per-position uniforms (item type, material, colour), no gear sharing between squadmates; squad ammo pools, food/drink loadout `[V2 DFsqd]` `[V2 DFb12]`. |
| B1 | YES | Citizens/units menus list each dweller with skills, needs, relationships `[V2 DFlab]` `[V2 DFneed]`. |
| B2 | PART | Migrant waves arrive per season; first two fixed (1-10 each), later waves scale with created wealth; population-cap setting; residency petitions; no hiring `[V2 DFimm]`. |
| B3 | YES | Player appoints bookkeeper, broker, chief medical dwarf, hammerer, manager, militia commander, sheriff / captain of guard, dungeon master via Nobles screen (appointer = expedition leader, later mayor); mayor is elected `[V2 DFnob]`. |
| B4 | YES | Work details: each labor set is "Everybody / Nobody / Only selected" plus per-citizen "specialized" lock; a permission matrix, no numeric priority `[V2 DFlab]`. **(chg: no 'alerts')** |
| B5 | YES | Manager work orders repeat daily/monthly/seasonally/yearly with AND-ed conditions `[V2 DFwo]`; fortress-wide standing orders `[V2 DFso]`; squad routines + monthly schedules `[V2 DFsch]`. |
| B6 | YES | Short-term stress -100000..100000 drives mood; long-term stress states at +25000 stressed, +50000 haggard, +100000 harrowed `[V2 DFstr]`; needs drive focus `[V2 DFneed]`. |
| B7 | PART | Titles carry `SUCCESSION:BY_HEIR` (monarch, baron) and citizens can inherit them; the player cannot choose heirs; hereditary titles otherwise unfilled by fortress dwarves `[V2 DFmon]` `[V2 DFbar]` `[V2 DFnob]`. **(chg)** |
| C1 | PART | Embark on one site; Conquer/Demand-surrender missions make a site a "holding" with an administrator, insurrection disabled `[V2 DFmis]` (page flagged old/buggy). |
| C2 | YES | Designate dig/build, builders fetch materials; constructions become map tiles once complete `[V2 DFcon]`. |
| C3 | YES | Constructions can be intentionally deconstructed `[V2 DFcon]`; repair `[M]`. |
| C4 | YES | Zones (meeting, barracks, dungeon, etc.) and burrows overlay tiles; barracks zone assigns squads `[V2 DFsch]`. |
| C5 | YES | Workshops fed by stockpiles; manager work orders `[V2 DFwo]`; chains `[M]`. |
| C6 | PART | Hauling is a labor (work detail); minecart track networks with stops and logic routes (page flagged old) `[V2 DFmine]` `[V2 DFlab]`; no supply-line abstraction `[M]`. |
| C7 | YES | Station, patrol route, defend-burrow orders per squad `[V2 DFsch]`; Siege Update adds siege engines and reinforced walls `[V2 DFb12]`. |
| D1 | PART | No player-authored laws. Nobles issue production mandates (3-6 months) or export bans and furniture demands; civ ethics set punishment tier `[V2 DFman]` `[V2 DFdem]` `[V2 DFjus]`. |
| D2 | NO | Economy disabled ("currently disabled", account exemptions unused); tax collector not implemented `[V2 DFnob]`. |
| D3 | PART | Offices are functional roles not advisers: manager, broker, bookkeeper, CMD, hammerer, sheriff, militia commander `[V2 DFnob]`; mayor/expedition leader consoles unhappy dwarves and meets diplomats `[V2 DFmay]`. |
| D4 | PART | Nobles get happy/unhappy thoughts from fulfilled/unmet mandates and demands; migrant "danger" score from deaths+executions+insanities over 5 years (weights 1,1/2,..,1/32; 10+ = dangerous, 50+ = tomb) `[V2 DFimm]`; no legitimacy meter. |
| D5 | PART | Mayor auto-elected at 50 population, re-elected 4pm on 17 Summer yearly, winner = highest summed social skills; player cannot vote, can override by appointing `[V2 DFmay]` `[V2 DFele]`. |
| D6 | YES | Justice screen: open/closed/cold cases, interrogation (captain's social skills vs target's), convicts, punishments beating / jail / hammering; guard needs cages+restraints ~ pop/10 `[V2 DFjus]` `[V2 DFcap]`. No trial or defence phase. |
| E1 | YES | Stockpiles accept item types; haulers carry items to them `[V2 DFstock]`. |
| E2 | PART | Barter with caravans; trade agreements (from outpost liaison) set requested goods and price multipliers `[V2 DFtra]` `[V2 DFlia]`. |
| E3 | PART | Yearly caravans; tribute caravans from missions; messengers can "improve trade", open trade with humans/elves early (53.13) `[V2 DFmis]` `[V2 DFb12]`. |
| E5 | YES | Deep material/quality crafting `[M]`. |
| F1 | YES | Squads of at most 10; militia commander required; each further squad has a militia captain `[V2 DFsqd]`. |
| F2 | YES | Commander over captains; uniforms, ammo pools by material and use, backpack rations/flask `[V2 DFsqd]` `[V2 DFb12]`. |
| F3 | YES | Monthly schedule per squad: Station / Patrol Route / Defend Burrow / Train orders, "min soldiers to follow" default 10; routines Off Duty, Staggered Training (3-month blocks), Constant Training, Ready `[V2 DFsch]`. **(chg: PART to YES)** |
| F4 | PART | Real-time with pause; direct orders attack/station/patrol/burrow/train to squads or selected members `[V2 DFsqd]` `[V2 DFcom]`. |
| F5 | PART | Local fights never auto-resolve, but missions (raid, pillage, raze, tribute, conquer) run off-map with "no control" `[V2 DFmis]` (page flagged old/buggy). **(chg: NO to PART)** |
| F6 | PART | Defender side: Siege Update (53.01, Nov 3 2025) invaders build stairs, bring rams, dig, free caged allies; player sieges via abstract raze/conquer missions `[V2 DFb12]` `[V2 DFsie]` `[V2 DFmis]`. **(chg)** |
| F8 | PART | Fortress-mode creatures never surrender, fights to death or escape `[V2 DFsur]`; fear/flee `[M]`. **(chg: YES to PART)** |
| G1 | YES | Adventure mode: slower frame-by-frame combat, body-part targeted attacks, yield/flee `[V2 DFcom]`. |
| G2 | YES | Edged/blunt effectiveness from material yield and fracture, contact area, armour dent stress `[V2 DFcom]`; armour layering `[M]`. |
| G3 | YES | Targeted wounds, bleeding, organ damage `[V2 DFcom]`; permadeath `[M]`. |
| H2 | YES | Friend, lover, spouse, grudges; romance needs idle co-location `[V2 DFmar]`. |
| H3 | PART | Actor: NO (player runs no schemes). Target: villain networks recruit/corrupt your residents and nobles, steal artifacts; you counter via interrogation, "Intelligence" tab; unfinished at .47 `[V2 DFint]` `[V2 DFagt]` `[V2 DFjus]`. **(chg: NO/PART resolved)** |
| H4 | PART | Marriage among citizens `[V2 DFmar]`; trade agreements `[V2 DFtra]`; messenger alliance only if monarch in fortress `[V2 DFb12]`. |
| H6 | PART | 53.13 (May 13 2026): appointed messengers do make peace, declare war, make contact, improve trade; raiding a site risks war with its civ `[V2 DFb12]` `[V2 DFdip]` `[V2 DFmis]`. **(chg: NO to PART)** |
| I3 | PART | Rumor system: witnessed events spread person to person, artifact location knowledge fades; liaison brings yearly news `[V2 DFrum]` `[V2 DFlia]`. |
| I6 | PART | Legends can hide most history until uncovered; knowledge fades in rumors `[V2 DFleg]` `[V2 DFrum]`; map fog `[M]`. |
| J1 | PART | Necromancy exists; procedurally generated magic in development ("magic/army/diplomacy release") `[V2 DFb12]`. |
| J2 | PART | Religions made in worldgen, temples, prayer needs scaled by faith `[V2 DFrel]` `[V2 DFneed]`; no doctrine control. |
| J3 | YES | Stress thresholds `[V2 DFstr]`; breakdown types tantrum / obliviousness / depression, repeated breakdowns end in insanity `[V2 DFmb]`. |
| K3 | YES | Psychological needs `[V2 DFneed]`; thirst and failing to drink `[V2 DFthirst]`; hunger/sleep/disease `[M]`. |
| K5 | PART | Adventure mode sleep/fatigue; unsafe sleeping invites ambush `[V2 DFadv]`. |
| L1 | YES | Facets and beliefs set which needs a dwarf has and how strongly `[V2 DFneed]`. |
| L2 | YES | Babies 0-1, children 1-18, old-age death checked each 1 Granite `[V2 DFage]`; migrants bring children `[V2 DFimm]`. |
| L3 | YES | Marriage, relatives, heir succession `[V2 DFmar]` `[V2 DFbar]`. |
| L4 | YES | Tantrums become crimes (vandalism, assault) feeding justice `[V2 DFjus]`; legends log `[V2 DFleg]`. |
| L5 | YES | Worldgen historical figures run plots, funding, assassination; agents visit forts `[V2 DFint]` `[V2 DFagt]`. |
| M1 | PART | Losing is fun; optional "victory goal" = noble title / becoming mountainhome `[V2 DFnob]`; "succumb to the invasion" on siege `[V2 DFsie]`. **(chg: NO to PART)** |
| M2 | PART | Fortress none; adventure mode has procedural quests (slay, retrieve) `[V2 DFqst]`. **(chg: NO to PART)** |
| M3 | YES | Legends records fortress/adventurer achievements, world persists `[V2 DFleg]`. |
| M4 | PART | Needs sub-tab, thought lists, announcements, justice report text `[V2 DFneed]` `[V2 DFjus]`. |
| M5 | PART | World, local map, adventure share one world but are separate play modes `[V2 DFleg]`. **(chg: YES to PART)** |

### Mechanics worth knowing (designer view, current build)
- **Work assignment is permission, not priority.** Labors are grouped in work details ("Everybody / Nobody / Only selected"); "Nobody" does not override another detail's grant; a "specialized" citizen takes only assigned labors and assigned workshop/occupation tasks. The engine picks which dwarf takes a job. 51.09 stopped Mining, Woodcutting and Hunting being held by one dwarf. `[V2 DFlab]` `[V2 DFb12]`
- **Nobles are a mandate engine tied to rooms.** Appointed: bookkeeper, broker, CMD, hammerer, manager, militia commander, sheriff/captain of guard (by expedition leader, then mayor). Mayor at pop 50 (elected); captain of guard replaces sheriff at 50. Baron/count/duke need pop 20 plus created/exported wealth 100k/10k, 200k/20k, 300k/30k, elevated through the outpost liaison. Mandates 3-6 months, max live: baron/mayor 1, count 2, duke 3, monarch 5; demands max 2/2/3/5/10. Unmet production mandate = noble's unhappy thought plus a crime "violation of production order" punished on dwarves who tend to have a fitting skill (random ones possible). Mandate items come from the noble's item preferences (a noble with none never mandates). `[V2 DFnob]` `[V2 DFman]` `[V2 DFmay]` `[V2 DFdem]`
- **Justice has real tiers.** Beating (guard), jail, hammering; PUNISH_SERIOUS = beating or 1 month jail, PUNISH_CAPITAL = 8 months or 50 hammerstrikes (>=50 counts as execution and deters immigration); no jail = downgrade to beating with a happy thought for the criminal and an unhappy one for the victim. Exempt: children, insane, animals, strange-mood dwarves, position holders with `PUNISHMENT_EXEMPTION`. `[V2 DFjus]`
- **Needs and thoughts are separate channels.** Focus = met/unmet need ratio: >=140% very focused ... <=60% badly distracted; skill effect up to +/-50%. Stress states +25000 / +50000 / +100000. `[V2 DFneed]` `[V2 DFstr]`
- **Military = routines x monthly orders.** Squad max 10; four default routines; per-month orders (Station, Patrol, Defend Burrow, Train) with a minimum-soldiers criterion and optional "preferred" positions; direct orders (attack/station/patrol/burrow/train) override and ignore burrow limits; station = random reachable tile in a 7x7 box. `[V2 DFsch]` `[V2 DFsqd]`
- **Intrigue is something done to you.** Visitors (agents under false identities) corrupt residents using social-skill contests; interrogating an innocent has no penalty beyond lost work time; failed interrogation can still end in a false conviction. `[V2 DFint]` `[V2 DFagt]` `[V2 DFjus]`
- **Diplomacy arrived late.** The Diplomacy page describes trade agreements and missions (tribute demand is the "no war" first contact); the 53.13 patch notes add messenger peace/war/alliance/trade on top. `[V2 DFdip]` `[V2 DFb12]`
- Not found: how current Steam build handles "legitimacy"/laws beyond mandates; no per-labor numeric priority exists in the Labor page (absence of mention, not a run).

---
## 2. RimWorld (Ludeon) with Royalty, Ideology, Biotech, Anomaly, Odyssey DLC
Version relied on: **1.6** (free update released with Odyssey, July 11, 2025 `[V2 RWblog]`); wiki pages are mixed-version (Raid points page "verified 1.3.3101", Titles page cites 1.4.3704) so numbers were cross-checked against a third-party decompile of 1.6 `[V2 RWcode]`. A 1.7 test branch is reported on Steam unstable (Oct 2026) `[S2 RWsearch]`; nothing here checked against it.

| id | cell | how |
|---|---|---|
| A1 | PART | Draft colonists to move/attack; right-click forced task for assigned work types `[V2 RWwork]`. |
| A3 | YES | Skills with 0-2 passion flames; incapabilities from traits, backstories, titles, slave status, ideo roles stack `[V2 RWwork]`. |
| A4 | YES | Apparel policies (v1 called "outfits") auto-equip best apparel per weather; medical-care policy per pawn `[V2 RWassign]`. |
| B2 | YES | Warden "Recruit" lowers prisoner resistance then recruits; slaves; wanderers join by event `[V2 RWprison]` `[V2 RWslavery]` `[V2 RWend]`. |
| B3 | YES | DLC-gated: Ideology Leader (1 colony-wide), Moral Guide (needs >=3 same-ideo colonists), up to 2 specialist types; assigned by a ritual `[V2 RWroles]`; Royalty titles by Honor `[V2 RWtitles]`. **(chg: PART to YES)** |
| B4 | YES | Work tab: standard (checkbox, left column outranks right) or manual priorities 1-4; all work at one priority done before the next `[V2 RWwork]`. |
| B5 | YES | Hourly schedule per pawn (Anything/Work/Joy/Sleep/Meditate, need thresholds 35%/30%/30%) `[V2 RWmenus]`; bills "do X times / until you have X / forever" `[V2 RWbill]`; colonists only work inside their allowed area `[V2 RWwork]`. |
| B6 | YES | Mood bar 0-100% vs mood target; break lines at 5/20/35% for a typical pawn `[V2 RWmood]`. |
| B7 | PART | Titles from Acolyte are inheritable; heirs auto-assigned, spouse-weighted; changing heir needs a comms console + monument quest; heir gets Freeholder only `[V2 RWtitles]`. |
| C1 | PART | Pick landing tile; caravans/outposts `[M]`; Odyssey gravship `[S2 RWsearch]`. |
| C4 | YES | Zone/area system (growing, stockpile, allowed areas) `[V2 RWzone]`. |
| C2 C5 C7 | YES/YES/PART | Blueprints; workbench bills `[V2 RWbill]`; no garrison abstraction `[M]`. |
| D1 | PART | Per-pawn policies (apparel/food/drug/medical) `[V2 RWassign]` and ideoligion precepts picked at creation or by reformation (fluid: 10 development points first, +2 per reform up to 20) `[V2 RWideo]`; not continuously legislated. |
| D3 | NO | Empire permits are cooldown abilities (troop calls, drops, strikes), not advisers; no council `[V2 RWtitles]`. **(chg: PART to NO)** |
| D4 | PART | Expectations: 6 stages keyed to total colony wealth, titles and ideo roles raise them `[V2 RWthoughts]`; Ideology certainty `[V2 RWideo]`. |
| D5 | NO | No votes found; Ideology Trial uses spectators in a probability roll, not a ballot `[V2 RWritual]`. |
| D6 | PART | Ideology Trial ritual: accuser vs accused; conviction chance by social abilities and spectator count; convicted can be freely banished/arrested/executed `[V2 RWritual]` `[V2 RWroles]`; wardens execute `[V2 RWprison]`. **(chg: no trials to Trial ritual)** |
| E3 | YES | Caravans, trade, comms-console traders; Royalty rank gates faction base trade (Knight) and trade ships (Baron) `[V2 RWtitles]`. |
| F1 | PART | Drafted colonists only; Royalty permits call 4 troopers (Acolyte), janissaries (Praetor), cataphracts (Archon), cooldown 40-60 days `[V2 RWtitles]`; allies send aid `[V2 RWfactions]`. |
| F4 F5 G1 | YES/NO/YES | Real-time pausable direct control; raids played out `[M]`. |
| G3 | YES | Body-part injuries, permadeath mode `[V2 RWend]`; detail `[M]`. |
| H1 | PART | Autonomous interactions (chitchat, deep talk, slight, insult, kind words, social fights) `[V2 RWsocial]`; player-driven: warden recruit, Ideology conversion `[V2 RWprison]` `[V2 RWideo]`. |
| H2 | YES | Opinion numbers: beauty +/-20 per level capped +/-40; traits e.g. annoying voice -25 `[V2 RWsocial]`; romance rules `[V2 RWsocial]`. |
| H4 | PART | Marriage `[V2 RWevents]`; faction goodwill hostile <= -75, ally >= +75, max +100 `[V2 RWfactions]`. |
| H5 | PART | Release a prisoner +12 goodwill (+15 toward natural goodwill); sell prisoners/slaves to a tribute collector for 3 honor each `[V2 RWfactions]` `[V2 RWtitles]`; no ransom found. **(chg)** |
| J1 | PART | Psycasts need psylink levels (max 6) from neuroformers, titles, anima trees `[V2 RWpsy]`. |
| J2 | YES | Up to 4 memes, precepts, rituals, roles, relics, fluid reformation `[V2 RWideo]`. |
| J3 | YES | 3 severities; mean time to break 4 days minor, 0.8 major, 0.5 extreme; 25+ named break types `[V2 RWmb]`. |
| L1 | YES | Traits/backstory/passions per pawn `[V2 RWwork]`. |
| L3 | PART | Biotech children with age-scaled weights, babies `[V2 RWraidpts]`; families `[M]`. |
| L4 | YES | Storyteller weighs wealth, colonists, animals, recent death/wound, time since last event `[V2 RWstory]`. |
| M1 | YES | Five endings (ship, royal ascent, archonexus, void awakening, mechhive) plus colony end and optional planetkiller timer `[V2 RWend]`. **(chg: more than ship)** |
| M2 | PART | Quests tab; mostly faction-offered, timed `[V2 RWquests]`. |
| M4 | PART | Mood and thought lists visible; raid points hidden unless Development mode "Write Storyteller" `[V2 RWraidpts]`. |
| A2 B1 | YES/YES | Scenario system customises starting situation and starting pawn backstory categories `[V2 RWscen]`; colonist management page `[V2 RWcol]`. |
| (v1 rows not re-checked: A5 C2 E1 E5 K3 L5) | | stay `[M]` as in v1. |

### Mechanics worth knowing
- **Threat points (the director's budget).** Points = (wealthPoints + sum pawnPoints) x random factor x lerp(1, adaptation, adaptationEffect) x threatScale x daysPassedFactor, clamped between a floor (35 up to a difficulty ceiling) and 10000. wealthPoints: 0 at <=14,000 storyteller wealth, 2400 at 400k, 3600 at 700k, 4200 at 1M (buildings count 50%). Per free colonist: 15 points up to 10k wealth, 140 at 400k, 200 at 1M; slave x0.75, cryptosleep x0.3, health bar pulls the value down by up to 65%. Threat scale: Peaceful 0.10, Community builder 0.30, Adventure story 0.60, Strive to survive 1.00, Blood and dust 1.55, Losing is fun 2.20. Start factor 0.7 at <=10 days rising to 1 at 40 days. The two player-controlled levers on raid size are wealth and colonist count. `[V2 RWcode]` `[V2 RWraidpts]`
- **Adaptation.** Adaption factor starts 0.8, range 0.4-1.47 (Losing-is-fun effective 0.75-1.19); 30-day grace; days since colonist deaths/downings shift it, so a struggling colony is raided smaller. `[V2 RWraidpts]`
- **Work priority is a 4-level sort plus capability gates.** 1 (highest) to 4, blank = never; ties break by column order; hauling at 1 means hauling everything first. The v1 line "nobles can only research and fight fires" is the *Medieval lord backstory*, not Royalty titles. `[V2 RWwork]`
- **Mood is thresholds.** Break lines 35% / 20% (4/7) / 5% (1/7) of the pawn's threshold stat (base 0.35, min 0.01, max 0.50); Iron-willed -18%, Steadfast -9%, Nervous +8%, Volatile +15%, Too smart +12%, Neurotic +8%, Very neurotic +14%. Mood moves +12/hour up, -8/hour down; base mood 42 Peaceful and Community builder, 37 Adventure story, 32 Strive, 27 Blood and dust, 22 Losing is fun. `[V2 RWmood]` `[V2 RWmbt]`
- **Royalty.** Honor thresholds (cumulative): Freeholder 1, Novice 7, Acolyte 13, Knight/Dame 21, Praetor 31, Baron 45, Archon 65; matches per-step `favorCost` 1,6,6,8,10,14,20 in the Royalty defs `[V2 RWdefs]`. One permit per title from Acolyte (max 5); permits stop working while the Empire is hostile; re-assigning all permits costs 8 honor; titles need throne room + bedrooms; conceited pawns (Empire recruits, Greedy/Jealous/Abrasive) refuse work tags per rank (Acolyte: Cleaning ... Archon: also Animals). `[V2 RWtitles]` `[V2 RWdefs]`
- **Ideology.** Leader abilities share a 600,000-tick (10 day) cooldown: Work Drive +50% work speed for 3 days, Combat Command aura, Trial, Leader speech; Moral Guide needs 3 followers, -5 mood unfilled, x2 conversion; role loss -15 mood. `[V2 RWroles]`
- **Economy of leverage.** You steer through priorities, schedule, areas, policies, rituals; pawns choose tasks. Factions have 3 states by goodwill (0, -75, +75 lines) with explicit upkeep actions (+12 returned prisoner, +20 destroying a mutual enemy's base, +1 per 500 silver traded). `[V2 RWfactions]`
- Not found: current-1.6 event table weights; Royalty permit list beyond the 12 on the Titles page; any ransom mechanic.

---
## 3. Songs of Syx (Gamatron AB / Jake de Laval)
Version relied on: **V71 "Reign of Terror", released June 15, 2026** `[V2 SyxV71]`. Still **Early Access**; dev post of Oct 15, 2026 plans a polish patch for end of 2026 and 1.0 "in the first half of next year" `[V2 SyxState]`. The game wiki (songsofsyx.com/wiki) returns HTTP 500 (MediaWiki DB error) on every page, web.archive.org is blocked by the egress proxy, so v1's wiki-snippet cells are `[S2]` at best. The primary source used instead is the developer's Steam announcements (patch notes) fetched through the Steam news API (40 posts, Mar 2021 to Oct 2026), plus the Steam store page `[V2 SyxStore]`.

| id | cell | how |
|---|---|---|
| B1 | YES | Individually simulated citizens/slaves "each with their own life, religion, fears and desires" `[V2 SyxStore]`; V67 biographies tied to traits `[V2 SyxV67]`; class split (nobles/citizens/children/slaves, retirees/recruits/students/workers) from v1 wiki snippet `[S2 SyxWiki]`. |
| B3 | PART | Nobles are appointed or imported; since V68 each is assigned to an office manually: industry offices boost a limited number of workers, regional offices produce Government Points; V69: every rank boosts 50 workers by +2; usurpation risk per store page `[V2 SyxV68]` `[V2 SyxV69]` `[V2 SyxStore]`. **(chg: v1's "17 types, Master of Farms +10%" is the pre-V68 system)** |
| B4 | YES | Workers allocated per room; priorities (0 = no employment, V63); V71 new work-priority screen, max 20 reduced to 5; rooms can be tied to specific races (V68); sick/injured no longer count as workforce (V66) `[V2 SyxV63]` `[V2 SyxV71]` `[V2 SyxV68]` `[V2 SyxV66]`. **(chg: PART to YES)** |
| B5 | PART | Subjects choose workplace by building preference (V68); V67 remade subject priorities/needs "to make a more dependable schedule"; automatic settings for all decrees (V71); no player shift scheduling found `[V2 SyxV68]` `[V2 SyxV67]` `[V2 SyxV71]`. **(chg: ? to PART)** |
| B6 | YES | Happiness vs loyalty vs fulfilment; riots when loyalty is low (put down with guards and soldiers); slave uprisings (V59) `[V2 SyxV59]` `[V2 SyxV71]`. |
| C1 | YES | World-map regions, conquest (V58), resettle with resources and levels kept (V70) `[V2 SyxV58]` `[V2 SyxV70]`. The v1 "5% per year uprising" dev quote not re-found `[?]`. |
| C2 C5 | YES/YES | Build houses, streets, plazas `[V2 SyxStore]`; rooms with multiple recipes, consumption techs (V71) `[V2 SyxV71]`. |
| C4 C7 | PART/? | Placement layout `[M]`; v1 "garrisons raise loyalty" is a player claim, not found in dev notes `?`. |
| D1 | YES | Decrees (handouts, persecution etc.) with automatic settings; law per crime `[V2 SyxV71]`. |
| D4 | YES | Law is "primarily about trading happiness for loyalty"; utopia needs almost no law `[V2 SyxV71]`. |
| D5 | ? | No vote/election/council mention in 40 announcements 2021-2026 (absence in patch notes is weak evidence). |
| D6 | YES | You set the punishment for each crime; effects multiplied by guard count, post coverage, execution sites, secret police; gallows are placeable items; V68 swap captives' punishments `[V2 SyxV71]` `[V2 SyxV68]`. **(chg: PART to YES)** |
| F1 | YES | Recruit/train at facilities, conscripts, mercenaries; recruit costs 6 days of health supplies (V69) `[V2 SyxV65]` `[V2 SyxV69]`. |
| F2 | PART | Armies are divisions with equipment and flags (V70); supply max 6 days (V69, was 24); no officer rank found, "perhaps add commanders to divisions" (2023) `[V2 SyxV70]` `[V2 SyxV69]` `[V2 SyxRoad]`. |
| F4 | YES | Real-time battles up to 50,000 units, spearmen/cavalry, tactics and morale, quick-battle mode (V70) `[V2 SyxStore]` `[V2 SyxV70]`. |
| F6 | PART | Fortifications can be breached or scaled (V68); formal sieges/ports listed as "plans, not promises"; "besiege you until you die" planned (V65) `[V2 SyxV68]` `[V2 SyxV65]`. **(chg: ? to PART)** |
| H3 | PART | Diplomacy "sabotage" option makes a faction attack you without betrayal penalty; low-opinion factions "secretly convince other factions to attack you"; assassination of foreign royals; secret police at home `[V2 SyxV66]` `[V2 SyxV64]` `[V2 SyxV71]`. **(chg)** |
| H4 | YES | Alliance (share enemies), Colleague (non-aggression pact), Vassal/Protector, Join Federation; minimum opinion needed to hold a stance `[V2 SyxV66]` `[V2 SyxV68]`. |
| H5 | YES | Vassal pays yearly tribute (15% stated V66, overlord picks kind); raid stance takes slaves/resources; slaves tradable `[V2 SyxV66]` `[V2 SyxV71]`. |
| H6 | YES | Break agreements down to neutral before declaring war; peace signs with all enemies; betrayal penalty from all factions; V71 trust system `[V2 SyxV68]` `[V2 SyxV66]` `[V2 SyxV71]`. |
| I* | ? | No espionage/rumour/fog-of-war mention found in the 40 announcements. |
| J1 | NO | Author (2023): "I will leave 'magic' to the modding community" `[V2 SyxRoad]`. |
| J2 | PART | Shrines to all gods, temples with wider radius, religion conversion at both (V65, V67) `[V2 SyxV65]` `[V2 SyxV67]`. |
| L1 | YES | Per-subject traits, biographies, wishes, race-specific `[V2 SyxV67]`. **(chg: PART to YES)** |
| L3 | YES | V71: natural reproduction, family tree up to 1,000,000 entries, children inherit last name `[V2 SyxV71]`. **(chg: PART to YES)** |
| M1 | ? | No win condition stated; collapse of the city/kingdom is the failure mode `[V2 SyxStore]`; 1.0 not yet released `[V2 SyxState]`. |

### Mechanics worth knowing
- **Law is a trade, not a rulebook.** V71 law: choose a punishment for every crime; each crime-punishment pair moves happiness and loyalty differently; all effects scale with guards, coverage, execution sites, secret police; dread aura from gallows; "invest deep into law and the returns become exponential" toward tyranny. Raiders are locked off below 200 population. `[V2 SyxV71]`
- **Nobles changed twice.** Pre-V68 per-industry offices (v1's wiki snippet); V68 onward: appoint a noble, assign to an industry office (boosts a limited number of workers) or a regional office (Government Points that build the city hall and upgrade regions); V69: +2 on 50 workers per rank; V71 adds an emissary office. The dev called nobles "the only place-holder feature remaining" in Jan 2025. `[V2 SyxV68]` `[V2 SyxV69]` `[V2 SyxV71]`
- **Diplomacy is a stance ladder with upkeep.** Trade / pact (colleague) / alliance / vassal-protector / federation; emissaries are a diplomatic point system that "sticks to the court when someone dies"; foreign royals have a trait system; sabotage lets you start a war without betrayal; peace deals are weak unless you threaten with armies in their territory. `[V2 SyxV66]` `[V2 SyxV68]`
- **Armies are logistics.** Rations and clothes mandatory, artillery a supply, drinks add morale; army supply depot loads carts on demand; armies can be supplied anywhere in your territory (V69); divisions can transfer only on the same tile (V71). AI factions "make sure they can beat you in auto resolve" before attacking, so an auto-resolve exists on the world map (player-side option `?`). `[V2 SyxV66]` `[V2 SyxV68]` `[V2 SyxV69]` `[V2 SyxV71]`
- **Economy knobs.** V71 Squeeze replaces the tax rate (large temporary resources, city devastation); immigration rate raised in V69; inflation 10% of credits per year (V58); tariffs both ways as a percentage; per-item logistics toll; trade caps removed in V71. `[V2 SyxV58]` `[V2 SyxV71]`
- Not found: officer ranks, formal siege equipment, any information-war system; wiki-only claims in v1 (17 noble types, class list) unverified.

---
## Still unknown
- Syx D5 (votes), I* (information), M1 (win condition), C7 (garrisons), C1 uprising odds, B1 class list: wiki HTTP 500, IA blocked by proxy, reddit/Discord/Trello not tried; settle with the wiki when it recovers or a V71 play check.
- Syx F5 player-side auto-resolve, officer ranks: only AI-side auto-resolve is stated (V66).
- DF cells kept `[M]`: A3 use-based gain, C5 chains, E5 crafting, F8 fear/flee, G3 permadeath, I6 map fog, K3 hunger/sleep/disease; "no player-authored laws" is an absence claim from the Labor/Noble pages, not a run. Whether the Steam build number equals Classic 53.16 was not checked.
- RW cells kept `[M]`: A5, C1, C2, C7, E1, E5, F4, F5, G1, G3 detail, K3, L5; event weights in 1.6; wealth "buildings count 50%" and adaptation numbers come from the wiki (1.3), not the 1.6 code read; 1.7 changes.

## Sources
- DF wiki (fetched 2026-10-22 via `https://dwarffortresswiki.org/index.php?title=<Page>&action=raw`): DFnob=Noble, DFmay=Mayor, DFman=Mandate, DFdem=Demand, DFjus=Justice, DFcap=Captain_of_the_guard, DFsqd=Squad, DFsch=Scheduling, DFlab=Labor, DFwo=Work_orders, DFso=Standing_orders, DFmis=Mission, DFsie=Siege, DFdip=Diplomacy, DFint=Intrigue, DFagt=Agent, DFlia=Outpost_liaison, DFele=Elections, DFimm=Immigration, DFneed=Personality_need, DFstr=Stress, DFmb=Mental_breakdown, DFmar=Marriage, DFrum=Rumor, DFrel=Religion, DFleg=Legends, DFadv=Adventurer_mode, DFcom=Combat, DFsur=Surrender, DFqst=Quest, DFmon=Monarch, DFbar=Baron, DFtra=Trade_agreement, DFcon=Construction, DFmine=Minecart, DFstock=Stockpile, DFthirst=Thirst, DFage=Age, DFav=Template:ArticleVersion, DFver=Template:Current/version and Template:Current/lastupdate (v53.16, Aug 5 2026).
- DFb12 = https://www.bay12games.com/dwarves/ (release feed 50.04 to 53.16; fetched with curl, text parsed).
- RimWorld wiki (fetched 2026-10-22 via `https://rimworldwiki.com/index.php?title=<Page>&action=raw`): RWwork=Work, RWassign=Assign, RWprison=Prisoner, RWslavery=Slavery, RWend=Endings, RWroles=Roles, RWtitles=Titles, RWmenus=Menus, RWbill=Bill, RWmood=Mood, RWzone=Zone/Area, RWideo=Ideoligion, RWthoughts=Thoughts, RWritual=Rituals, RWfactions=Factions, RWsocial=Social, RWevents=Events/Incidental, RWpsy=Psycasts, RWmb=Mental_break, RWmbt=Mental_Break_Threshold, RWraidpts=Raid_points (tagged verified 1.3.3101), RWstory=AI_Storytellers, RWquests=Quests, RWscen=Scenario_system, RWcol=Colonist.
- RWcode = https://raw.githubusercontent.com/32bitx64bit/RW-Decompiled-1.6/9c11094e22ccbd966b1ae589a348935e6f45fce4/RimWorld/StorytellerUtility.cs (third-party decompile of 1.6, found by GitHub code search). RWdefs = https://raw.githubusercontent.com/AustenXiyue/RimWorldLibrary/5083255e14ea47ec0ce003b2f604ba8767cae72c/vanilla/Data/Royalty/Defs/RoyalTitles/RoyalTitles_Empire.xml (third-party mirror, game version not stated). RWblog = https://ludeon.com/blog/?p=2278 (Jul 11 2025). RWsearch = web search results (jeu.video, RimDroid release note, journaldugeek; snippets only).
- Songs of Syx: Steam news API `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1162750&count=40&maxlength=0&format=json`, item ids under `https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/<id>`: SyxV71=1835236783570947 (2026-06-15), SyxState=1846651706676679 (2026-10-15), SyxV70=1818118366173283 (2025-12-04), SyxV69=1800991756308268 (2025-05-29), SyxV68=1788945554755579 (2025-01-15), SyxV67=6242640076596103359 (2024-09-05), SyxV66=6474562312199934047 (2024-04-16), SyxV65=5409450219982749682 (2023-12-17), SyxRoad=5219165352641663894 (2023-09-26), SyxV64=5124581515272852730 (2023-06-27), SyxV63=5000716037482418159 (2023-01-02), SyxV59=5418383147749509017 (2021-09-20), SyxV58=4032392655063756098 (2021-06-24). SyxStore=https://store.steampowered.com/app/1162750/Songs_of_Syx/ (fetched). SyxWiki=https://songsofsyx.com/wiki/index.php/Noble (HTTP 500; v1 snippet only).
