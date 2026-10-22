# T03 - Colony sims, tutorial pass (Dwarf Fortress, RimWorld, Songs of Syx)

Tags: `[V3 k]` = read in a page body fetched this session (2026-10-22); key `k` -> URL and version in "Sources (V3)" at the foot. `[S3]` search snippet only. `[M]` memory, not re-checked. `?` not established. `[CONTESTED]` sources disagree. `[V2 k]` = cited from the v2 table only, not re-read.

---
### Dwarf Fortress - facts line
Bay 12 Games (Tarn and Zach Adams), published on Steam by Kitfox Games; fortress-building colony sim inside a generated world. Version: **Steam Patch 53.16, 5 Aug 2026** `[V3 DFst]`; the wiki's current-version pages describe the same line `[V3 DFq]` (the v2 open question "does Steam = Classic 53.16" is settled: Steam notes say "Patch 53.16"). Tutorial assumes **Fortress mode**, default (Normal) difficulty, Play Now! embark, 7 dwarves; Adventure mode in two lines at the end of section 5. One session: first game-year about 1-3 h real time `[M]`. Mostly wiki-sourced `[V3]`; time estimates and some UI flow are `[M]`.

#### 1. Setup choices
| choice | options | what it changes |
|---|---|---|
| World generation | size (Pocket, Small, Medium...), history length (5-500 yrs; default stops yr 100), civilizations, sites, beasts, natural savagery, mineral occurrence, "Island"/"Region" shape | how many dwarf/human/elf/goblin neighbours, how dangerous wilderness is, how rich metals are; quickstart suggests Medium / 100 yrs / Medium / Medium / Low beasts / Very Low savagery / Everywhere minerals `[V3 DFq]` `[V3 DFx]` `[V3 DFcal]` |
| Game type | Fortress, Adventure, Legends | which mode you play in this world |
| Tutorial | Start tutorial (game picks site, dwarves, supplies) / Skip | whether the game does embark for you `[V3 DFq]` |
| Site | any tile cluster; check aquifer, trees, river, soil/clay/sand, metals (iron), flux, neighbours; resize embark (default 4x4); choose origin civilization | the real difficulty setting: aquifer and evil biomes make digging/farming hard; a home civ with fewer than 2 dwarf sites on your landmass ends immigration after the 2nd winter `[V3 DFq]` `[V3 DFe]` `[V3 DFx]` |
| Settlers | **Play Now!** (7 fixed profiles: miner, woodworker, stoneworker, metalcrafter, fisherdwarf, planter, expedition leader) or **Prepare Carefully** (10 skill ranks per dwarf, 1,504 embark points of which 544 are free to spend) | starting skills/kit; wiki says careful prep "makes little difference" to a novice `[V3 DFe]` `[V3 DFq]` |
| Difficulty | Enemies: Off / Normal / Hard; Economy: Normal / Hard; Custom per-setting | Off disables ambushes, sieges, megabeasts, werebeasts, agitated animals; Hard roughly halves the population/wealth triggers; economy Hard = 5x wealth for ranks, 3x zone value, half the noble period; changeable after embark except siege caps `[V3 DFd]` `[V3 DFe]` |
| Population cap | Population Cap / Strict Population Cap in Settings | stops migrants (and with Strict, births) at a number `[V3 DFi]` |

#### 2. The loop
Clock: real time with pause. Year = 12 months x 28 days, 4 seasons; Granite is the first month (early spring); embark is around 15 Granite `[V3 DFcal]` `[V3 DFi]`. Caravans are tied to seasons: elves spring, humans summer, dwarves autumn `[V3 DFcal]` `[V3 DFc]`.
1. Pause. Read announcements, the units list, Stocks; decide what is missing (food, drink, beds, rooms, materials).
2. **Designate**: dig, chop, build, place stockpiles and zones, queue work orders, set labors. You never command a dwarf directly in Fortress mode `[V3 DFq]`.
3. Unpause. Dwarves pick jobs themselves from the labors they are permitted; eating, drinking, sleeping and high-priority personal needs pre-empt fortress jobs `[V3 DFq]` `[V3 DFpn]`. Automated: hauling, job choice, workshop supply, farming, justice cases, mayor elections.
4. Time passes by the season: migrant waves arrive (first two seasons fixed, none in first winter), the autumn dwarf caravan and its liaison arrive, nobles issue mandates/demands, wealth is tallied `[V3 DFi]` `[V3 DFl]` `[V3 DFm]`.
5. Interrupts: ambush/siege banners, megabeasts, strange moods, tantrums, floods, cave-ins, fire. Control stays with you, in real time: pause, order squads (station/patrol/attack/burrow), seal the entrance, set civilian burrows `[V3 DFs]` `[V3 DFq]`.
6. Review and repeat: adjust labors, re-queue work orders, answer demands, check military schedule, plan the next dig.

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Designate dig/channel/stairs (m) | miner time, needs a pick; flooding/cave risk | opens rooms and z-levels | constant |
| Chop trees, gather plants, hunt, fish | axe/crossbow; outdoor danger | logs, food | frequent, early |
| Stockpile (p) with category filters | haul time; wrong filter clutters shops | where items live | constant, early |
| Zones (z): meeting, bedroom, office, dining, pasture, tavern, hospital, water source | tiles + furniture | rooms satisfy needs and noble room demands | constant |
| Build workshop / furniture (b) | materials, labor | production chain nodes | constant |
| Work orders (needs manager + office) | wealth from output | repeat/conditional production | frequent after year 1 |
| Labor / work details (y) | none; mis-set = idle dwarves | who may do which job; "Everybody/Nobody/Only selected" | frequent, tune rarely `[V2 DFlab]` |
| Farm plot crop per season | seeds | food and alcohol base | each season |
| Nobles screen (n): appoint manager, broker, bookkeeper, CMD, hammerer, sheriff, militia commander | office rooms | unlocks work orders, trading, stock counts, justice | a few times a year `[V3 DFq]` `[V3 DFn]` |
| Trade at the depot | goods, export bans, wagon access | import tools/food/seeds | 1-3x per year `[V3 DFq]` |
| Squads, uniforms, monthly schedule | idle dwarves, metal | defence and training | from year 1-2 |
| Traps, walls, drawbridge, siege engines | materials | passive defence | before pop ~80 `[V3 DFs]` |
| Justice: jail, hammerer, punish | space, labour | handles crimes/mandate violations | rare, rising |
| Provide for strange mood, respond to artifacts | materials | masterworks, or madness | occasional |
| World screen: missions, messengers (53.13) | dwarves leave site | raid, tribute, peace/war, trade | rare `[V3 DFst]` |
| Settings: difficulty, pop cap, retire/abandon | none | tunes the game | rare |

#### 4. First hour, step by step
Source: the wiki Quickstart guide (v50+ UI) and the in-game tutorial `[V3 DFq]`.
1. Create a world (Medium, 100 years, default sites) and choose Play now; pick **Fortress**. The game simulates two weeks and offers the tutorial.
2. Take the tutorial once (it picks the site and teaches "strike the earth"), or Skip and use **Find embark location**: no aquifer, trees, a river/brook, iron, calm surroundings.
3. On Prepare, set Enemies to **Off** for the first fort (wiki advice), choose **Play Now!**.
4. On arrival **press Space to pause immediately**. Look around, open Citizens (u) and Stocks, read the logs.
5. Labor menu (y): set Hunters and Fisherdwarves to "nobody" so nobody wanders out alone; give the Miners detail to two dwarves (three picks come with the wagon).
6. Dig an entrance tunnel at least 10 tiles long, one wide, near the wagon; if ground is flat, channel a 3x3 pit and tunnel from it. Add a 5x5 room (later trade depot), a stairwell room and a larger room for stockpiles.
7. Make a **general stockpile** that rejects corpses, refuse, stone, gems and wood; the dwarves start hauling the wagon's contents in.
8. Dig a room one z-level down and zone it **Meeting area**; make a refuse stockpile outside and a small wood stockpile; designate 3-5 trees.
9. Dig a soil room, build a 3x3 **farm plot**, set plump helmets for all four seasons (only five seeds at first, so half the plot is planted).
10. Build a **still** and brew (needs barrels/pots; first brewing within six months); add a water source zone or well; pasture grazers outdoors (about 10x10).
11. Build carpenter and mason shops; make beds (wood) and dig bedrooms; dwarves sleeping on floors get unhappy.
12. Nobles (n): expedition leader as manager and broker, planter as bookkeeper; give manager and bookkeeper an office (chair + table, zoned Office).
13. Build the trade depot (5x5 room, 3-wide path to the map edge) before the dwarven autumn caravan; sell crafts/gems, buy food, drink, seeds.
14. Migrants arrive (first two waves 1-10 each, `[CONTESTED]` vs "5-15" in the Quickstart text); give them beds and labors; keep fortress wealth low early because wealth pulls ambushes and sieges.
15. Watch what the game shows: red/yellow announcements, the SIEGE banner, a "Some migrants have arrived" notice, mandates on the nobles screen.

#### 5. What changes later
- Population and wealth drive everything: fortress title Hamlet 20 pop, Village 50, Town 80, City 110, Metropolis 140 (with created-wealth 5k/25k/100k/200k/300k *or* exported-wealth 500/2.5k/10k/20k/30k) `[V3 DFf]` `[V3 DFd]`.
- **Nobles**: expedition leader appoints administrators; at **pop 50 a mayor is elected** (highest social skill; replaces leader) and can mandate 1 item and demand 2 furnishings; the dwarven **liaison** (arrives with the autumn caravan) lets you appoint a **baron** at pop 20 + 100k created + 10k exported wealth, then count (200k/20k), duke (300k/30k); mandate caps 1/1/2/3/5 for baron/mayor/count/duke/monarch; monarch needs City rank, a living duke and happiness `[V3 DFn]` `[V3 DFmy]` `[V3 DFmo]` `[V3 DFm]` `[V3 DFl]`.
- **Mandates**: 3-6 months to make a named item (or an export ban of about half a year); miss it and the noble is unhappy and some dwarf is punished for "violation of production order". **Demands**: furniture in a room, about half a year, no punishment `[V3 DFm]` `[V3 DFdm]`.
- **Migrants** keep coming with created wealth (reported by the last caravan); danger score from deaths, executions and insanities over 5 years discourages them `[V3 DFi]`.
- **Sieges** from pop 80 or the wealth triggers: since 53.01 invaders build stairs, dig, bring rams, free caged allies, and track trap sites; you get bolt throwers, catapults, reinforced walls `[V3 DFs]` `[V3 DFst]`. Normal: 25% of invasions are sieges; Metropolis tier brings up to 120 soldiers and 40 monsters.
- Messengers (53.13) can make peace, declare war, make contact, improve trade; alliance only with a monarch present `[V3 DFst]`.
- **Adventure mode** (two lines): you create one character or party and walk the generated world as an open-world roguelike, visiting towns and caves and taking quests `[V3 DFadv]`. It is in the Steam build; site-building is not yet in `[V3 DFst]` (53.07 notes).

#### 6. Failure and ending
"Losing is fun" is the stated attitude `[V3 DFq]`. Typical losses: starvation/thirst, flood, tantrum spirals, megabeast or siege wipe-out; you can "succumb to the invasion" from the pause menu `[V3 DFs]`; or retire/abandon (the fort becomes a world site `[M]`). No scripted victory; the optional goal is climbing from baron toward monarch/mountainhome `[V3 DFn]`. Recovery is possible mid-crisis (seal entrance, burrows, military) but a dead fort stays dead; the world and its Legends record persist and a new fort can start in it `[M]`.

#### 7. Consequential vs cosmetic choices
- Site (aquifer, trees, metals, civ proximity) is consequential; community consensus and the wiki both call it the real difficulty setting `[V3 DFx]` `[V3 DFe]`.
- Created wealth and population are consequential because they set siege size and migrant size; you control them by what you make and sell `[V3 DFd]` `[V3 DFs]`.
- Who becomes baron/mayor matters: a noble with no item preference never mandates, one with a hard-to-make preference is a standing problem `[V3 DFm]`.
- Prepare Carefully and dwarf appearance are mostly flavour for a first fort (wiki: "little difference") `[V3 DFq]`; labor assignment is permission-based, so micro-tuning matters less than keeping jobs possible.
- Dominant answers: Enemies Off for learning, underground everything, a still before the first summer (community consensus `[V3 DFx]`).

#### 8. Open items
- Attachment `62dd3fd3` III.2 (values/needs/focus), file lines 239-271: **verified**. Values range -50..+50 and show in 7 levels; 33 values listed on the wiki (same 33 names as the attachment); cyan highlight when a dwarf differs from civ values; needs refresh to 400 and use the seven bands; focus formula is the same weights, divided by 4 x number of needs; skill effect up to +/-50%; low-priority (green) vs high-priority (magenta !) personal jobs; some memories can change values `[V3 DFpv]` `[V3 DFpn]`. Small flags: the wiki's focus table calls 100% "Untroubled" while need bands call it "Not distracted"; the attachment's "bothered by this" gloss on the romance-vs-no-love example is its paraphrase (the wiki facet text is only "never falls in love or develops positive feelings toward anything") `[V3 DFpf]`.
- Attachment `9226007a` (Nine Titles) line 357 and 571, `89a3a060` (Twenty Games, "20G") lines 138 and 397: claim that DF's "mandate-issuing nobles" sit close to the empty cell "many anonymous citizens + a few hard-capped named delegates". **Partly right, mostly not**: the capped, named office-holders and the mandate cap (1/1/2/3/5) exist `[V3 DFm]`, but DF citizens are not anonymous (each has values, needs, relations) and nobles are not channels for labour: work goes through labors, zones and work orders; nobles are demand sources, and only managers/brokers/bookkeepers (appointed administrators) gate functions `[V3 DFn]` `[V3 DFq]`. Also the mandate page is flagged `{{buggy}}` and the immigration page conflicts with the Quickstart on wave size.
- `e3f9f19a` line 347 ("zones plus mandate-issuing nobles", R2): zones and mandates coexist, but nobles do not delegate or zone work `[V3 DFn]`.
- v2 cell corrections: **DF version** "Steam build number not separately checked" -> Steam Patch 53.16 (5 Aug 2026) `[V3 DFst]`. **B2** "first two fixed (1-10 each)" stays (matches immigration mechanics `[V3 DFi]`) but the wiki lede says "2-10" and Quickstart "5 to 15" `[CONTESTED]`. **M2/A1** adventure mode exists in the Steam build (v2 did not say) `[V3 DFst]`. **F8** (v2: fortress creatures never surrender, `[V2 DFsur]`): the 53.16 notes say "Strengthened effect of unconditional surrender" `[V3 DFst]`, so that cell may be stale; the surrender mechanic itself was not read.
- Not established: real-time length of year 1 (`[M]` only); exact Steam in-game tutorial step list (the wiki only says it teaches interface and "strike the earth"); whether the Quickstart "no wagon until barony" caravan note still holds (Caravan page says wagons go to "the worthy" `[V3 DFc]`).

---
### RimWorld - facts line
Ludeon Studios (Tynan Sylvester); colony sim driven by an AI "storyteller". Version: **1.6** (free update with the Odyssey DLC, 11 Jul 2025 `[V2 RWblog]`); a 1.7 test branch is only a search snippet `[S2]`. Wiki pages are mixed-version (raid-points page tagged 1.3.3101); v2 cross-checked the raid formula to a third-party 1.6 decompile `[V2 RWcode]`, and this pass re-checked only the mental-break constants there `[V3 RWmbc]`. Tutorial assumes the **Crashlanded** scenario, one storyteller (Cassandra Classic), base game loop; Royalty and Ideology appear only where they change the loop. One session: a day is 16 m 40 s at speed 1 and speed 2 runs x3 `[V3 RWtime]`, so a 15-day quadrum is about 1.5 h at speed 2 (my arithmetic). Mostly wiki-read `[V3]`; first-hour steps are the wiki's own Quickstart guide.

#### 1. Setup choices
| choice | options | what it changes |
|---|---|---|
| Scenario | **Crashlanded** (3 colonists chosen from 8; 800 silver, 50 survival meals, 30 components, 30 medicine, rifle, revolver, knife, flak gear; 450 steel + 300 wood nearby), Lost Tribe (5 colonists, "difficult"), Rich Explorer (1, "extra difficult"), Naked Brutality (1, nothing) | starting people, kit, tech level (New Arrivals research is cheaper than New Tribe) `[V3 RWscen]` |
| Storyteller | Cassandra Classic (rising curve with rests), Phoebe Chillax (long gaps), Randy Random (no rules) | event timing and pacing only; changeable any time `[V3 RWst]` |
| Difficulty | Peaceful, Community builder, Adventure story, Strive to survive (default), Blood and dust, Losing is fun, or Custom | threat scale 0.10/0.30/0.60/1.00/1.55/2.20, base mood 42/42/37/32/27/22, adaptation; Custom adds a wealth-independent time-curve mode; changeable any time `[V3 RWrp]` `[V3 RWmood]` `[V3 RWst]` |
| Save mode | Commitment (one save, saved on quit; game over only when the whole colony is gone) or Reload anytime | cannot be changed after creation `[V3 RWst]` |
| Ideology (DLC) | system inactive / create fluid / create fixed / preset (e.g. "Mole people") | memes, precepts, rituals and roles that rewrite later play `[V3 RWideo]` |
| World | seed, globe coverage 30/50/100%, rainfall, temperature, faction population, pollution (Biotech), faction counts | map variety and neighbours `[V3 RWwg]` |
| Landing tile and map | biome, hills, latitude, growing period, starting season, map 200-325 cells | the real opening difficulty; Quickstart: temperate forest, latitude 20-30, small or large hills, near friendly tribes `[V3 RWqs]` |
| Colonists | reroll/save the three; look at passions, skills, traits, incapabilities | who can shoot, grow, build, heal `[V3 RWqs]` |

#### 2. The loop
Clock: real time with pause; 60 ticks per second, 2,500 ticks per game hour, 24 h per day, 15-day quadrums, 60-day year; speeds 1/2/3 are x1/x3/x6 `[V3 RWtime]`.
1. Pause, read alerts and letters, set or adjust work priorities, schedule, areas, bills, research.
2. Place blueprints and designations (build, zone, chop, mine, harvest, hunt, tame). You do not walk colonists; they take jobs by priority 1-4 and left-to-right column order `[V3 RWqs]` `[V2 RWwork]`.
3. Run time. Automated: hauling, construction, planting, cooking, tending, eating, sleeping, joy, hourly schedule; moods drift toward a target at +12/-8 per hour `[V3 RWmood]`.
4. The storyteller rolls events (traders, wanderers, weather, raids, manhunters, quests). Raid size is a points budget set by wealth, colonist count, a threat scale, a start-of-game factor and an adaptation factor `[V3 RWrp]`.
5. Interrupt: a threat letter. You **draft** colonists (direct control, real time) to take cover and shoot, or leave them on auto; afterwards tend wounds, jail or release prisoners, bury the dead.
6. Mental breaks fire when mood sits under 35%/20%/5% of a pawn's threshold, with mean times 4/0.8/0.5 days; fix the cause (food, beds, rooms, pain) `[V3 RWmbc]`.
7. Repeat; research projects, power, defences and a cash crop of trade goods compound.

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Work tab priorities (1-4, or checkboxes) | none; mistakes idle people | who does what first; hauling at 1 means everything is hauled first | constant early, tune weekly `[V2 RWwork]` |
| Architect: Structure/Floors/Furniture | steel, wood, stone, silver; build time | rooms, beds, roofs | constant |
| Zones: Growing, Stockpile, Allowed areas | none | where crops grow, where items go, where pawns may walk | constant early |
| Orders: chop, mine, harvest, hunt, tame, allow/forbid | work time | raw materials and food | constant |
| Production benches + Bills ("do X", "until you have X", "forever") | materials, labor | meals, medicine, tools, stone blocks | frequent |
| Research queue | bench + intellectual labor | power, medicine, turrets, new tech tiers | each few days |
| Power and Temperature (generators, coolers) | fuel, silver | freezer, lamps, benches | once, then upgrades |
| Security: sandbags, turrets, traps, walls | steel, components; raise wealth | passive defence | before the first raids |
| Draft and fight | injury, death risk | win a raid | when a threat arrives |
| Prisoners: recruit, release, sell, execute | bed + warden time; mood hit for sale (-3) | new colonists, goodwill, silver | after raids `[V3 RWqs]` |
| Medical: tend, bed rest, medicine policy | herbal/industrial medicine | survival after fights, disease | after fights |
| Caravans and trade (comms console, beacon) | silver, travel risk | buy/sell, faction goodwill | mid game |
| Quests tab: accept/ignore | time-limited, risky | rewards (with Royalty: Honor) | when offered |
| Schedule and Assign (apparel, food, drug policies) | none | sleep/work/joy hours, outfits | rarely |
| Royalty/Ideology: rituals, permits, roles | gold, honor, gathering time | mood, troops, titles | periodic |

#### 4. First hour, step by step
Source: RimWorld wiki Quickstart Guide + Scenario page `[V3 RWqs]` `[V3 RWscen]`.
1. Choose Crashlanded, Cassandra Classic on Strive to Survive (the guide recommends it; Peaceful if you only want to learn the UI), world defaults.
2. Pick a temperate-forest tile near friendly tribes; landing screen shows biome, growing period.
3. Reroll the trio: at least one with passion and 5+ in Shooting, Plants, Construction, Medical; avoid Lazy, Slothful, Slowpoke, Pessimist, Depressive, Chemical interest, Pyromaniac; keep two who can haul and fight.
4. On landing **pause**, wait for pods to open, then unforbid everything (Orders > Allow).
5. Equip the rifle on the best shooter, revolver on the next, knife on the brawler.
6. Work tab: turn on manual priorities; Firefight/Patient/Bed rest/Basic at 1 for all; Doctor, Cook, Construct, Grow at 1 on the best skill only; passions at 2; hauling at 1 for now.
7. Scout the terrain; order a chop-wood job.
8. Build one wooden room of about 50 tiles (7x7), three beds, doors; stockpile zone over its floor.
9. Before nightfall: campfire, roof, and four 5x5 growing zones (2 rice, 1 strawberries, 1 potatoes).
10. Pen or hitch spot for the pet; let the first night pass without ordering sleepers around (disturbed-sleep penalty).
11. Day 2-5: more wood, forage berries and healroot, add corn, cotton, healroot fields.
12. Butcher table + fueled stove with a "cook until you have 10-20 simple meals" bill; floor the kitchen.
13. Wood generator, then a 7x7 freezer with a cooler (hot side outside) set to -5 C, stockpile set to important.
14. Research bench: battery and solar panel first, then microelectronics; lamp in the main room.
15. First threat arrives about day 5: Cassandra always sends one mad animal, then one raider (day 5, hour 15) `[V3 RWcass]`. Draft, take cover, shoot, tend, capture or let die; bury corpses away from the base.
16. Set priorities and a bed for every new arrival; begin stone walls and expand defences.
The game shows: alerts on the right edge, letters (blue/yellow/red), "Pen needed", "Learning helper" lessons on demand `[V3 RWlh]`.

#### 5. What changes later
- **Wealth drives threat.** Raid points = (wealth points + pawn points) x threat scale x start factor (0.7 until day 10, 1 by day 40) x adaptation (0.4-1.47; starts 0.8, 30-day grace); minimum 35, maximum 10,000; wealth points 0 at 14k, 2,400 at 400k, 4,200 at 1M; a free colonist is worth 15 points up to 10k wealth, 140 at 400k `[V3 RWrp]`. Mechanoid raids can only appear above 300 points `[V3 RWev]`. Cassandra runs 4.6-day "on" and 6-day "off" cycles from day 11 (about 8.5 major threats a year) `[V3 RWcass]`.
- **Expectations**: colony wealth ladders mood bonus from +30 to 0 and raises recreation-tolerance loss from 18% to 7% a day `[V3 RWwealth]`.
- New tiers: sappers, breachers, sieges, drop pods; new colonists arrive via wanderers, refugees, recruits; research climbs Industrial to Spacer; caravans and faction trading open.
- **Royalty** adds the Empire: quests pay Honor, Honor buys titles (Freeholder to Archon), titles demand throne rooms, apparel and bedrooms and unlock permits (call troopers); conceited pawns refuse some work. Honor can also come from selling gold or prisoners `[V3 RWtit]`.
- **Ideology** adds an ideoligion with memes and precepts, rituals (gatherings with a quality roll for mood, recruits or loss), roles (leader, moral guide) and certainty; fluid ideoligions can be reformed with development points `[V3 RWideo]` `[V3 RWrit]` `[V2 RWroles]`.

#### 6. Failure and ending
Colony End: every colonist dead, kidnapped or gone; a wanderer can restart you, and a menu offers new wanderers after eight in-game hours (seven times) `[V3 RWend]`. Commitment mode makes this final. Five story endings (ship to the stars, Royal ascent, archonexus, void awakening, mechhive); the archonexus and the optional planetkiller timer end the planet; the others let the colony continue `[V3 RWend]`.

#### 7. Consequential vs cosmetic choices
- Opening trio and landing tile: consequential by the wiki's own advice (cover shooting/plants/construction/medical; avoid mood-poison traits) `[V3 RWqs]`.
- Difficulty/threat scale and adaptation: consequential and numeric (0.10 to 2.20); the storyteller's name changes pacing, not the points formula `[V3 RWrp]` `[V3 RWcass]`.
- Wealth management: real lever on raid size, but the wiki says not to micromanage it: invest in guns and armor instead `[V3 RWwealth]`.
- Food, freezer, beds and rooms are the dominant survival answer for the opening; scenario choice mostly changes start kit (community consensus `[V3 RWqs]`).
- Cosmetic: colonist looks, ideoligion styles, colony names.

#### 8. Open items
- Attachment `62dd3fd3` mood claims (III.3, lines 273-287): thresholds 35/20/5 and 4/7, 1/7 **verified** `[V3 RWmbt]` `[V3 RWmbc]`; sleeping pawns do not break `[V3 RWmood]`; "mean time to break" **wrong**: attachment says major 3 days, extreme 0.7 days; wiki and the 1.6 decompile (`MajorBreakMTBDays 0.8f`, `ExtremeBreakMTBDays 0.5f`, `MinorBreakMTBDays 4f`) say 0.8 and 0.5 days `[V3 RWmbc]`. The "mood targets depressed by wealth" claim is **true** (Expectations: +30..0 mood) but is cited to "IV.3", which is the L4D Director section; the claim is at line 382 `[V3 RWwealth]`.
- Attachment raid-point claims (IV.2, lines 367-382): floor 35, ceiling 10,000, threat scale 220%, "250 tribals / 25 centipedes", scyther 150, centipede 400, mechanoids from 300 points: **verified** `[V3 RWrp]` `[V3 RWraider]` `[V3 RWev]`. The linear rule "1/160.83 + colonists/3120 per wealth" is the wiki's marginal slope but **only between 14k and 400k wealth** (10k to 400k for the colonist term), with 0 wealth points below 14k and 15 flat points per colonist; it ignores the multipliers; the arithmetic of the four-row table and 143.6 points checks out. Siege at 500 and sappers/breachers at 700: **not established**; a Workshop-mod snippet says sieges have weight 0 below 700 `[S3 RWmod]`; wiki says weights vary by raid points. Weakest raider 30 / well-armed pirate 90: not extracted. "Randy multiplies after the cap": wiki says so `[V3 RWrp]`.
- v2 cells: **mood MTB (RWmb)** v2 had 4/0.8/0.5 days; now also confirmed in 1.6 code `[V3 RWmbc]`. Base mood by difficulty and +12/-8 per hour re-confirmed `[V3 RWmood]`. No v2 number corrected.
- Not established: Anomaly/Biotech/Odyssey loop changes (out of scope); Steam-specific tutorial prompts beyond the Learning helper; early-game raid size in 1.6 (code values not read).

---
### Songs of Syx - facts line
Gamatron AB (Jake de Laval, solo developer plus a small team); fantasy city-builder with a world-map strategy layer and large real-time battles. Version: **V71 "Reign of Terror", 15 Jun 2026**, still **Early Access**; a polish patch is aimed at end of 2026 and 1.0 at H1 2027 `[V3 SyxV71]` `[V3 SyxSt]`. Tutorial assumes a **Random game, Despot mode, Cretonian royal race**, because that is the one authoritative beginner path (community wiki, edited 18 Sep 2026) `[V3 SyxEm]`. One session: reaching 50 population (first rank) is probably 2-4 h `[M]`; real-time length of a game year `?`. **Source caution:** the official wiki (songsofsyx.com/wiki) still returns HTTP 500, so this section leans on the community wiki songsofsyx.wiki.gg, read through WebFetch (a small-model summary, not raw wikitext), on dev posts read raw through Steam's news API, and on one Steam guide read raw. No page I read states a game version; treat wiki details as "probably V70/V71".

#### 1. Setup choices
| choice | options | what it changes |
|---|---|---|
| Play type | Random Game (wiki guide uses it); a tutorial exists in stable builds (cut scenes added V68) but its steps are not documented; a campaign is in development `[V3 SyxSt]` `[V3 SyxV68]` | Random Game builds a procedural world |
| Game mode (V71) | **Utopia** (casual, creativity), **Despot** (standard difficulty), **Homestead** (self-sufficiency; subjects easier to please; diplomacy and region development costlier; fewer wars), **Merchant Prince** (peace and trade easier, less inflation; science and region development suffer), **Warlord** (more regions, stronger raiders), **Ruler of Kings** (disloyal subjects, many enemies) `[V3 SyxMo]` | rules and modifiers; some titles unlock only in one mode; V69 made "casual" the default difficulty `[V3 SyxV69]`; custom sliders (furniture, maintenance, spoilage, happiness, raid security) are reported by players `[S3 SyxFo]` |
| Royal race | Amevia (lizard folk, loners, eggs/fish/clay, good soldiers), **Cretonian** (pigmen, great farmers, weak crafters and fighters, "easy choice for the early game"), Dondorian (strong dwarves, no natural births, great crafters/soldiers, poor food), Garthimi (insect, mining/hunting, terrible crafters/farmers, low morale), Human (tech workers, good farmers, crime and insanity), Tilapi (orchards and archers, loners) `[V3 SyxSp]` | which jobs your people are good at; housing is single-race; the 2026 guide prefers Human or Tilapi `[V3 SyxTx]` (pre-V71) |
| Identity and titles | name, faction name, flag; up to five unlocked **titles** active (a new player has none) | small permanent bonuses (for example The Wise: universities +0.25) `[V3 SyxTi]` |
| World and capital site | Generate world; place capital and **throne** | the guide wants 100% moisture, temperate climate, forest and river, throne near but not on rich soil `[V3 SyxEm]` |

#### 2. The loop
Clock: real time with pause. Keys 1 = pause, 2 = x1, 3 = x5, 4 = x25 (double-press 2 for 1/4 speed, 4 for x250) `[V3 SyxEm]`. A "yearly economic summary" shows at each year start `[V3 SyxV71]`.
1. Pause and read: food days, workload, overlays, room problem icons.
2. Place rooms with a brush (farm, carpenter, well, house...), roads and warehouses; set worker numbers, priority (0-5) and warehouse pull sources `[V3 SyxEm]` `[V3 SyxAm]` `[V2 SyxV71]`.
3. Run. Automated: subjects pick workplaces by preference, walk, haul, fetch, use services (essential ones daily, two of the non-essential ones each day), age, reproduce, die; immigrants walk to the throne and swear fealty `[V3 SyxV67]` `[V3 SyxTh]`.
4. Periodic: yearly accounting and tariffs; events (over 100); taxes ("Squeeze"); disease and crime grow with size `[V3 SyxV67]` `[V2 SyxV71]`.
5. Interrupts: raiders once population reaches 200 (V71 locks them off below it); riots when a species' loyalty falls to 70% or lower; epidemics; AI factions; invasions. A battle is a separate real-time field fight (up to 50,000 units) with a Quick Battle option (50,000-unit scale `[V2 SyxStore]`, V70 `[V3 SyxV70]`); if invaders reach the throne they steal goods and money `[V3 SyxRa]` `[V3 SyxRi]` `[V3 SyxTh]`.
6. Review: adjust food, housing, services, law, tech and diplomacy, then repeat.

#### 3. The choice menu
| verb / choice | cost | effect | when |
|---|---|---|---|
| Place rooms (farm, workshop, service) | materials, build time, upkeep; oversized rooms cost more | production, services | constant |
| Roads, warehouses and pull orders | wood/stone, maintenance | logistics; warehouses halve decay, haulers cut it 25% `[V3 SyxLg]` | constant |
| Housing (house 3x5 holds 5, longhouse 6x6 holds 10 `[V3 SyxTx]`) | wood/stone | population cap per race | frequent |
| Worker count and priority per room | idle labour elsewhere | where people work | frequent |
| Invite immigrants / auto-immigration | food and housing must exist | population growth | when food surplus `[V3 SyxEm]` |
| Spend tech points (innovation, knowledge, administration) | lab/library/admin staff; points need upkeep `[V3 SyxTe]` | unlock rooms, boosts | each level |
| Law: punishment per crime, guards, decrees | happiness for loyalty | order vs mood `[V3 SyxV71]` | from mid game |
| Trade: import/export depots, agreements, barter | Denarii, goods, emissaries | resources, profit | frequent mid game |
| Diplomacy: stances, tribute, alliances | opinion, emissaries | peace, vassals, war | mid/late |
| Regions: conquer, develop, govern | army, Government Points | extra land and goods | late |
| Nobles: promote a citizen, assign to industry or governor | housing (Chamber + 4 servants) `[V3 SyxNo]` | boost 50 workers or region points | after a high rank |
| Armies: recruit, equip, divisions, supply | rations, clothes, weapons | defence and conquest | late |
| Slavery: buy/sell/free | mood and law effects | cheap labour | optional `[V3 SyxV71]` |
| Resettle (keep level and many resources) | lose city | restart faster | rare `[V3 SyxV70]` |

#### 4. First hour, step by step
Source: community wiki Beginner's Guide, chapters Emir and Amarir `[V3 SyxEm]` `[V3 SyxAm]`.
1. Play > Random Game > Despot > GO; pick species Cretonians; name yourself, faction and flag; skip titles; Generate.
2. Place the capital on moist, temperate forest by a river; place the throne near the river, near but not on rich soil. You start with 10 Cretonian plebeians, 60 fruit, 60 vegetables, 40 rations, 100 wood, 60 stone, 16 livestock.
3. Build a **hearth**, a **well** and housing for 10 (wood houses; Cretonians prefer wood). Short of wood: Jobs > Fell tree.
4. Build a vegetable farm and a fruit farm on rich soil by the river; forage and hunt meanwhile; keep the build cost under your food stock.
5. Two 7x7 warehouses (fruit, vegetables), a janitor covering non-farm rooms, a 7x7 mass grave.
6. With a food surplus invite 5 or 10 immigrants at a time (right-click the species icon); grow to 25 plebeians; set logistics buildings to auto-employ; add a speaker, a shrine and a food stall.
7. Dirt roads over the service square, then to every building and farm.
8. Two more warehouses for wood and stone; fell trees and clear rock until full; build bigger farms; demolish old farms only if you hold more than 20 food days.
9. Diplomacy > pick a faction > demand 100 fruit and 100 vegetables > Barter; trade wood and stone later; add workers (about 20 vegetable, 10 fruit).
10. At 50 population you earn the title **Emir**. Chapter 2 (50-75 pop): place a 15x15 carpenter near but not beside homes (noise), split oversized rooms with a wall, staff it with ~30, add a warehouse for wood and furniture, check Work-Load, Commute and Hauling near 1.00; Cretonians craft at 80% efficiency.
What the game shows: yellow tiles on oversized rooms, room-problem overlay, the Production panel's Work-Load / Commute / Hauling figures `[V3 SyxAm]` `[V3 SyxV67]`.

#### 5. What changes later
- Progress ranks (the guide's six chapter names): Emir, Amarir, Prontix, Approntix, Approntix Ray, Legati; the guide's end target is 1,000 population `[V3 SyxBG]`; the Nobles page says promotion opens at the rank Approntix Ray `[V3 SyxNo]`; V69 added "two new levels" and moved rooms into the tech tree `[V3 SyxV69]`.
- Pressures ramp with size: accidents disabled below 150 employees then scale up, raiders from 200, crime and disease grow, maintenance becomes "a science" `[V3 SyxV67]` `[V3 SyxV71]`.
- **Law and loyalty** (V71): choose a punishment per crime, guards radiate law auras, gallows radiate dread, secret police; happiness is traded for loyalty; a utopia needs almost no law `[V3 SyxV71]`.
- **Raiders** (V67 beta design, V71 adds the 200-pop lock): a fixed set of pre-spawned groups of varying power; only those near your wealth "rung" take an interest; beat them for a bounty, lose and they take goods and drop you down the ladder; unnamed raiders hit your regions instead `[V3 SyxV67]` `[V3 SyxRa]`.
- World layer: regions, tribute, vassals, alliances; armies are divisions with supply (6 days max) and spear/cavalry tactics `[V2 SyxV69]` `[V3 SyxV70]`.
- Tech and trade got remade in V71: techs 50% cheaper, tariffs both ways, tolls, per-item logistics cost.

#### 6. Failure and ending
The community wiki's Capital City stub says the game "has no fail state": losing citizens or money does not end it because immigrants return and resources regrow `[V3 SyxCC]` ([CONTESTED] with the store-page language about the realm collapsing `[V2 SyxStore]`). Real setbacks: starvation, riots at 70% loyalty, raiders reaching the throne, lost battles; recovery is by rebuilding or **Resettle** (start over keeping level and many resources) `[V3 SyxV70]`. No win condition is defined; 1.0 is unreleased `[V3 SyxSt]`; titles (34 listed) and achievements are the long goals `[V3 SyxTi]`.

#### 7. Consequential vs cosmetic choices
- Royal race and map moisture/climate are consequential: species multipliers (Cretonian 80% crafting) and farming yields drive early output `[V3 SyxAm]` `[V3 SyxSp]`.
- Food-first and compact layout are consequential; community consensus: "rushing" collapses from food, disease or morale `[V3 SyxTx]`; service proximity can never reach 100% so layout always matters `[V3 SyxV67]`.
- Law: dev says you can play the whole game without touching it, so it is optional at low population `[V3 SyxV71]`.
- Game mode shifts rules and which titles can unlock; titles themselves are small (+0.03 to +0.25 style stat boosts) `[V3 SyxTi]`.
- Cosmetic: flag, names, many decorations (though monuments give fulfilment).

#### 8. Open items
- v2 cell updates: **M1** (`?`): the community wiki says no fail state `[V3 SyxCC]`, still no stated win condition. **B3**: nobles unlock at rank Approntix Ray, any adult citizen can be promoted, boost 50 workers (+100 on later promotion) or serve as Governor; a Chamber houses one noble and needs four servants `[V3 SyxNo]` (page undated by version; may predate V69's "+2 on 50"). **B1** class split now partly seen (plebeians, servants, slaves, nobles) `[V3 SyxEm]` `[V3 SyxNo]`. **Raiders locked below 200 pop** confirmed by wiki `[V3 SyxRa]`. Game modes (six) were not in v2 `[V3 SyxMo]`. Wiki alternative: songsofsyx.wiki.gg (195 page titles in AllPages) works via WebFetch, not curl (HTTP 403).
- Not established: the in-game tutorial's steps; a game year's real duration; exact rank population thresholds beyond Emir=50 and Amarir=50-75; D5 votes, I* information, C7 garrisons (still unknown); numbers on the Despot happiness modifier (a forum snippet says 0.80x `[S3 SyxFo]`).
- Uncertain: WebFetch summaries can drop numbers; the 2026 Treyex guide predates V71 so its breeding, slave and law sections may be outdated.

---
## Sources (V3), all fetched 2026-10-22
- DF wiki `https://dwarffortresswiki.org/index.php?title=<P>&action=raw` (current-version pages, `{{av}}`): DFq=Quickstart_guide, DFe=Embark, DFd=Difficulty, DFn=Noble, DFm=Mandate, DFdm=Demand, DFi=Immigration, DFs=Siege, DFc=Caravan, DFl=Outpost_liaison, DFf=Fortress, DFmy=Mayor, DFmo=Monarch, DFcal=Calendar, DFpv=Personality_value, DFpn=Personality_need, DFpf=Personality_facet, DFadv=Adventurer_mode. DFst=Steam news API appid 975370 (53.01 gid 1815034433003631 3 Nov 2025; 53.07 gid 1819386365090176; 53.13 gid 1832700592786716 13 May 2026; 53.16 gid 1840310314339261 5 Aug 2026). DFx=https://explorminate.org/dwarf-fortress-beginners-guide-learn-to-strike-the-earth-better/ (1 Feb 2024, pre-Adventure).
- RimWorld wiki `https://rimworldwiki.com/index.php?title=<P>&action=raw` (mixed 1.3-1.6): RWqs=Quickstart_Guides, RWscen=Scenario_system, RWst=AI_Storytellers, RWwg=World_generation, RWtime=Time, RWmood=Mood, RWmbt=Mental_Break_Threshold, RWrp=Raid_points (tagged verified 1.3.3101), RWev=Events, RWraider=Raider, RWcass=Cassandra_Classic, RWwealth=Wealth, RWend=Endings, RWideo=Ideoligion, RWrit=Rituals, RWtit=Titles, RWlh=Learning_helper. RWmbc=https://raw.githubusercontent.com/32bitx64bit/RW-Decompiled-1.6/9c11094e22ccbd966b1ae589a348935e6f45fce4/Verse.AI/MentalBreaker.cs (third-party 1.6 decompile). RWcode, RWblog, RWroles, RWwork, RWmb: see v2 sources. RWmod=web-search snippet (Steam Workshop "Event Probabilities", id 3088239103).
- Songs of Syx: SyxV67=6242640076596103359, SyxV68=1788945554755579, SyxV69=1800991756308268, SyxV70=1818118366173283, SyxV71=1835236783570947, SyxSt=1846651706676679 (15 Oct 2026), Steam news API appid 1162750. Community wiki (WebFetch summaries) `https://songsofsyx.wiki.gg/wiki/<P>`: SyxEm=Beginner's_Guide_-_Emir (18 Sep 2026), SyxAm=...-_Amarir, SyxBG=Beginner's_Guide (8 Jul 2026), SyxSp=Species, SyxTi=Titles (12 Aug 2026, refers to V69), SyxRa=Raider, SyxTh=Throne, SyxNo=Nobility, SyxCC=Capital_City, SyxRi=Riot, SyxLg=Logistics, SyxTe=Technology. SyxMo=https://steamcommunity.com/sharedfiles/filedetails/?id=3760716997 (osmasker, V71 game modes, Jul 2026). SyxTx=https://www.treyexgaming.com/songs-of-syx-beginner-guide/ (10 Jan 2026, pre-V71, via WebFetch). SyxFo=search snippet of Steam forum "Difficulty Settings?" thread. SyxStore: see v2.
