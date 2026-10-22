# R8 - NPC life and economy comparison (Sims 4, Anno 1800, Patrician IV, Wildermyth) - v2 verified

Evidence note (v2, 2026-10-22). v1 reported Fandom as HTTP 402 to WebFetch (still true), but the **MediaWiki API on those hosts answers plain `curl`**
(`https://anno1800.fandom.com/api.php?action=query&prop=revisions&rvprop=content&titles=...`; same for `patrician4.fandom.com`, `sims.fandom.com`), as does `wildermyth.com/w/api.php`.
Anno 1800 and Patrician IV wiki cells below are therefore read from wikitext, not memory. Anno 1800 data tables: `NiHoel/Anno1800Calculator` `js/params.js` (extracted game data).
Tags: `[V2 url ver/date]` page body read this session; `[S2 url]` search snippet only; `[M]` memory; `?` not established; `[CONTESTED]`.
Valoria has no currency, price or craft today (per brief), so every Valoria gap is relative to that.

## The Sims 4 (Maxis/EA, life sim; Windows release 2014-09-02; latest pack relied on: Royalty & Legacy, 2026-02-12)
Version basis [V2 https://en.wikipedia.org/wiki/The_Sims_4 fetched 2026-10-22]. Stage table [V2 thegamer, updated 2024-12-26].

| id | val | how |
|---|---|---|
| A1 | YES | Direct control of the active household; other Sims autonomous. [V2 simscommunity.info/2014/06/15 SimGuruGraham: "the family you're currently playing"] |
| B5 | PART | Player queues actions (usually max 8 interactions); free will fills idle time and can be switched off for the selected Sim; no standing-order layer found. [V2 sims.fandom.com Action_queue 2026-07-21; Free_will 2026-06-07] |
| B6 | PART | Emotions/moodlets per Sim, driven by actions, events, social interactions; no faction-level loyalty. [V2 wikipedia The_Sims_4] |
| B7 | YES (Royalty & Legacy only; base game PART) | Dynasty head uses "Designate Heir"; rivals challenge by duel/chess/fistfight or "Usurp Family Headship"; underage heir keeps title "cosmetic" until Teen. [V2 ea.com/nl/games/the-sims/the-sims-4/news/royalty-and-legacy-expansion-pack; V2 thesimstree.com developer Q&A recap]. Trailer features "selecting heirs", succession, inheritance, overhauled family tree: [V2 simscommunity.info/2026/01/29]. A Last Will choosing who gets Simoleons/estate: [S2 search summary of a review; thumbculture.co.uk page returned 429; not on EA page] |
| E2 | PART | Yard-sale tables (City Living, Jungle Adventure, Eco Lifestyle, Crystal Creations): player picks markup 0/25/50/75/100/200/300%, higher markup means fewer buyers; 3 Sim-hour event. No city-wide market. [V2 sims.fandom.com Sales_stand 2026-08-15]. v1 said NO. |
| E3 | NO | No trade routes or caravans found. [M] |
| E4 | PART | Single currency; household starts with §20,000 plus §2,000 per extra Sim; bills; no loan mechanic found. [V2 sims.fandom.com Simoleon 2026-09-29] |
| E5 | PART | Creative skills (painting, writing, instrument tips) earn money; per-item sale values fixed. [V2 Simoleon 2026-09-29 for earning; fixed values M] |
| E6 | YES | Weekly bill (utilities, taxes, penalties); unpaid leads to power shutoff then Repo-man. [V2 snootysims.com/wiki/sims-4/how-to-pay-bills-in-sims-4-guide] Careers pay salaries [V2 wikipedia] |
| K3 | YES | Six needs: hunger, bladder, hygiene, social, fun, energy, depleting daily, restored by objects. [V2 wikipedia The_Sims_4] |
| L1 | YES | 3 traits (adult) + aspiration bonus trait; 14 aspiration categories for teen+, most with four milestones, completion gives a reward trait (several allowed). [V2 wikipedia; V2 sims.fandom.com Aspiration_(The_Sims_4) 2026-08-17]; "teens 2, children 1" [S2 primagames]; wikipedia says children and teens 2 [CONTESTED, minor] |
| L2 | YES | Eight life stages newborn..elder; elder dies naturally within days of the minimum. [V2 thegamer.com/sims-every-stage-of-life-length] |
| L3 | YES | Pregnancy, genetics, households, family trees; R&L adds dynasty membership by blood/marriage/adoption only. [V2 thesimstree; genetics/pregnancy M] |
| L4 | PART | Emergent from needs/traits/relationships; no authored arcs. R&L adds scandal/blackmail events. [M; V2 thesimstree for R&L] |
| L5 | PART | Unplayed households, if "Neighbourhood Stories" is on, adopt, change/leave careers, retire, die in accidents; default ON for Other Households, OFF for My Households. [V2 simscommunity.info/2022/03/16/the-sims-4-guide-to-neighbourhood-stories-customisation]. Marriage/dating/babies listed in [S2 ggrecon snippet]. Effects stay local to that household. |
| H2 | YES | Two relationship bars (friendship green, romance pink); statuses boyfriend/engaged/married/WooHoo partner; one spouse at a time. [V2 simscommunity.info/2022/10/16/the-sims-4-romance-guide]. Decay without contact: [S2 search summary] |
| M1 | NO | Sandbox; no win/loss condition found [M]. Aspirations are optional lifelong goals. [V2 wikipedia: "lifelong goals with tasks"] |

Mechanics worth knowing:
- Life stages in Sim days, Short / Normal / Long: Newborn 0.5/1/4, Infant 2.5/5/20, Toddler 3.5/7/28, Child 7/14/56, Teen 10.5/21/84, Young Adult 14/28/112, Adult 21/42/168, Elder 7+/14+/56+. Elder numbers are minimums. [V2 thegamer, 2024-12-26]. Identical table in [V2 simscommunity.info/2023/03/15, 2023-03-15], whose prose says Normal Teen is "nearly eleven days" rather than seven, contradicting its own table (21): [CONTESTED within source]. TheGamer prose says Long "more than triple"; its table is exactly 4x Normal.
- Aging is three separate switches: lifespan Short/Normal/Long applies to every Sim; unplayed Sims may auto-age or not; played families may all age, or only the household being played (others pause). [V2 simscommunity.info/2014/06/15, 2014 post]; menu entry names: [S2 2023 guide in search results]
- Active and Long-Lived traits lengthen Elder; aging pauses during pregnancy; Potion of Youth resets the current stage. [V2 thegamer]. How many days Long-Lived adds is [CONTESTED] among fan sources (17-22 days in one, "lowers death chance" in another) - not quoted.
- Autonomy loop: lowest need picks an interaction from nearby objects that advertise what they satisfy. [M]
- Unpaid-bill timings differ by guide: power off at 48 h and Repo-man after 2 more days [V2 snootysims]; another lists 48/72/96 h [S2 search summary] - [CONTESTED].
- Royalty & Legacy (2026-02-12): "Any Sim can become head of their own Dynasty"; a Kingdom has one ruler; monarch can appoint advisors, who may be family; a dynasty need not be royal; Sims advance by "earning favor at court"; titles cannot be made in CAS. [V2 ea.com page, thesimstree recap]. A "Council of Peers" stripping a title for scandal appears only in [S2 search summary of a review, not opened] - not on the EA page, the recap, or the 2026-01-29 trailer article.
- Design lesson (author inference about Valoria, not checked here): persistent traits + need decay give unauthored stories but need per-NPC state ticking each turn.

## Anno 1800 (Ubisoft Blue Byte, city builder; Windows 2019-04-16, consoles 2023-03-16 [V2 wikipedia.org/wiki/Anno_1800]; wiki pages read are revisions dated 2021..2026-09, named per row)
Fandom wikitext via API; extracted data from Anno1800Calculator params.js (game GUID/`tpmin` tables, undated master branch, includes 13 DLCs).

| id | val | how |
|---|---|---|
| C2 | YES | 3x3 residences must be road-linked to a trading post or residents leave and the house ruins. [V2 anno1800.fandom.com Residences 2021-12-10; Population 2025-11-20] |
| C4 | PART | Radius effects: Trade Union / Palace affect buildings in a radius or street range; union radii cannot overlap. [V2 Trade_Union 2026-05-17; Palace 2023-07-26]. Service-radius coverage for markets/fire: [M] |
| C5 | YES | Chains with fixed rates, e.g. Fishery `tpmin` 2, Flour Mill -> Bakery. [V2 params.js factories] |
| C6 | YES | Route ships loop their load/unload orders until paused; options "wait for goods", "discard cargo". [V2 Trade_routes 2025-06-15] |
| B3,B4 | NO | Workforce is an island-wide pool per tier; a Fishery needs 25 farmer workforce; shortage lowers efficiency, can reach zero. No named workers. [V2 Workforce 2023-05-06] |
| B5 | YES | Trade routes and passive-trade rules (buy / sell / both with a minimum stock) run unattended. [V2 Trade 2025-01-24; Trade_routes] |
| B6 | YES | Happiness rating per residence from five factors; levels Angry < -40 ... Euphoric >= 40. [V2 Happiness 2023-05-23] |
| D1,D3 | PART | Seat of Power palace: five departments, each with a passive buff and five policies, one policy selectable per department; no ministers (term absent in both pages). [V2 anno-union.com/en/devblog-seat-of-power; Palace 2023-07-26] |
| D2 | PART | No player-set rate found; income per house = sum over needs of (I*S*(1+R)*(1+N)+B)*F. Game imposes "royal taxes" (below). [V2 Needs 2022-12-08; Royal_Taxes 2021-04-01]. Absence of a slider: not provable from a page, only not found. |
| D4 | YES | Unhappy residents riot; rioters stop working and paying taxes; mobs damage/ignite buildings. [V2 City_incidents 2025-03-09] |
| D5 | NO | No voting or assembly mechanic in the Palace, Diplomacy or Characters pages (absence in those pages, not a proof). [V2] |
| E1 | YES | Per-island storage; a palace department buff gives e.g. "+200 tons islands storage per Harbormaster's office". Base capacity figures: ? [V2 anno-union devblog-seat-of-power] |
| E2 | PART | Fixed coin price per good (below); no stock-driven price. [V2 Template:GoodsValues 2023-01-20; Trade 2025-01-24] |
| E3 | YES | Ship routes, passive trade, and Docklands barter contracts. [V2 Trade; Exchange_Ratios 2023-01-20] |
| E4 | PART | One currency (coins); go bankrupt at -5000; Archibald Blake gifts 25000 once; shares of islands tradable. No loan mechanic found. [V2 Coins 2022-07-14] |
| E5 | YES | Chains plus goods feeding population/construction. [V2 params.js; Population] |
| E6 | YES | Maintenance of buildings and ships, charter-route upkeep, royal taxes feed the per-minute balance. [V2 Coins 2022-07-14] |
| F4 | YES | Real-time naval combat in the same session as city building. [V2 wikipedia Anno_1800] |
| H2,H4,H6 | YES | Reputation 0-100 per faction; treaties War / Peace / Trade Rights / Alliance; actions have per-character success chance. [V2 Diplomacy 2024-02-25] |
| L1 | PART | AI competitors have "personality and preferences" that move reputation; citizens are counts. [V2 Diplomacy] |
| L2,L3 | NO | Population is residents per house (e.g. Farmers 10, Investors 50 per full house). [V2 params.js populationLevels] |
| L4 | NO | Random incidents only (fire, riot, illness), gated by conditions (illness needs 1500 artisans globally). [V2 City_incidents] |
| M1 | YES | Sandbox victory conditions: Monuments, Investors, Target Population/Wealth/Revenue, Diplomatic; loss by bankruptcy. [V2 Sandbox_mode 2022-10-03; Coins] |

Mechanics worth knowing:
- **Prices are fixed per good** (confirms v1). Buy price = 2.5 x sell price: fish buy 40 / sell 16, coal 20 / 8, bricks 50 / 20, bread 210 / 84, sewing machines 576 / 230. A neutral trader's or pirate's "special request" pays 4 x sell (potatoes 8 -> 32). Trading with an AI competitor reverses the perspective: you buy at their sell price and sell at their buy price (coal: 8 buy, 20 sell). [V2 Template:GoodsValues 2023-01-20; Trade 2025-01-24]. The wiki states production cost per t/min beside each price; balance comes from throughput and from which partner you use.
- Docklands barter has an explicit formula: R = V(G_I)/V(G_E) x M_I/M_E, with fixed per-good values V "derived from their production chains" and an export multiplier from a specialty pyramid. [V2 Exchange_Ratios 2023-01-20; anno-union devblog-docklands]
- Tiers: 5 Old World (7 with DLC: Tourists, Scholars), 2 New World (3 with DLC: Artista), 2 Arctic, 2 Enbesa. [V2 Population 2025-11-20; params.js]. v1 said "five and two": correct for base game only.
- Basic needs raise residents per house and all must be met to advance (house must be full); luxury needs raise happiness and tax, are optional. [V2 Population]. Need unlocks are population counts in data (farmers' fish need unlocks at 50 farmers, schnapps at 100). [V2 params.js]
- Consumption: Farmers' fish need has `tpmin` 0.0025 and a Fishery `tpmin` 2, so 2 / 0.0025 = 800 residents per fishery (my arithmetic; reading `tpmin` as per resident is my inference). [V2 params.js]. v1's "fish about 0.0025" is confirmed.
- Happiness: luxury fully met +20, none met -20; factors luxury, island peace, working conditions, pollution, news. Positive/negative balance news shifts happiness by 5. [V2 Happiness 2023-05-23; Coins]
- **Royal taxes** (anti-snowball): from 1000 residents of one tier on one island, 9% of that tier's income is deducted, rising to 40% at 4875; rate = floor(1 + pop/125). [V2 Royal_Taxes 2021-04-01]
- "Trade Union" is an administration building holding up to three items that buff production buildings in its radius (no road needed, radii cannot overlap); it is not a political body, and "ministers" do not appear. [V2 Trade_Union 2026-05-17; Palace 2023-07-26]
- Design lesson: chain graph + per-resident consumption + radius coverage is the minimum C5/C6 loop; for Valoria the closest transferable idea is a fixed goods-value table plus a barter ratio, not a market.

## Patrician IV (Gaming Minds/Kalypso, trading sim; Patrizier 4 released September 2010 [V2 de.wikipedia.org/wiki/Patrizier_IV]; Rise of a Dynasty 2011-04-11 [V2 store.steampowered.com/app/57730])
Sources: fan wiki wikitext via API (patrician4.fandom.com, revisions 2021-01..2022-01); Steam guide "Patrician IV Guide" steamcommunity.com/sharedfiles/filedetails/?id=682751098 (posted 2016-05-13, updated 2023-07-01; player guide, flagged removed-from-community by Steam but readable); 2010 reviews. Patrician IV is not documented in a first-party manual I could reach.

| id | val | how |
|---|---|---|
| E1 | YES | 20 commodities (Goods Index lists exactly 20); counting house stores 1000 barrels, each warehouse +1000. [V2 p4 wiki Goods_Index, Counting_house 2021-01-11] |
| E2 | YES | Per good per city a 4-diamond supply/demand indicator (4 red = extreme shortage, 4 green = extreme surplus); "the greater the demand, the higher the price"; your own buying/selling shifts it. [V2 Steam guide 682751098]. "Prices fluctuate daily" (v1) not verified; guide says stock "fluctuate[s] over time". Formula: ? |
| E3 | YES | Convoys under a captain; per-good load/unload with min/max price; auto-trade; land routes (wagon trains) in Rise of a Dynasty. [V2 Steam guide; Steam store 57730] |
| E4 | PART | Tavern "offers loans"; low-interest loans are a way to build reputation. Terms: ? [V2 Steam guide; V2 de.wikipedia] |
| E5 | YES | Own production buildings; produced goods cost less than market; "vertical monopoly" advised. [V2 gamingnexus.com/Article/2819, review 2010-11-15] |
| E6 | YES | Config `tradesystem.ini` has daily wages for factory workers, guards and administrators; ships carry "Daily Costs"; warehouse rent for over-capacity storage; counting house 50/day. [V2 steamcommunity.com/sharedfiles/filedetails/?id=1788651794 modding guide, third-hand from Kalypso forum archive; V2 p4 wiki Counting_house] |
| C5 | PART | City-level chains: wiki lists each city's produced goods and goods consumed for production (Boston makes Brick, Grain, Salt, Mead, Cloth; consumes Wood, Wool, Honey). [V2 p4 wiki Cities 2021-01-11; V2 gamingnexus review] |
| C6 | YES | Ships and convoys; wagon trains on land routes need escorts vs bandits (player post). [V2 Steam guide; V2 steamcommunity app/57730 thread] |
| B2 | YES | Hire a captain per convoy (4 skills, ranks 0-5), sailors, workers, counting-house administrator, guards. [V2 p4 wiki Captain, Counting_house] |
| B5 | YES | Administrator buys/sells at set prices up to set quantities; convoy "trade according to specific" rules. [V2 Steam guide] |
| D5 | PART | Elections exist: Burgher screen shows current mayor, next election date and lets you run; guild office (Alderman) is contested by rival merchants; game goal is Elderman. Council acts on money: a player reports paying ~100K to "convince the council" to build a minster and again at its next sitting about a month later (anecdotal, [V2 steamcommunity.com/sharedfiles/filedetails/?id=3018508023]). Vote tally rule: ? [V2 Steam guide; V2 store.steampowered.com/app/57620; V2 en.wikipedia Patrician_IV: "participate in mayoral politics"] |
| H2 | PART | Guild reputation gates what you may build; burgher screen ranks reputable people; hoarding a scarce good costs reputation in that town. [V2 Steam guide for first two; S2 gamespot.com/articles/patrician-iv-impressions-first-look/1100-6266569 for the third, page 403] |
| F4 | PART | Simple naval combat: pick shot type and target; pirates attack convoys, appear from Wholesaler rank. [V2 cgmagonline.com/review/game/patrician-iv 2010-12-16; p4 wiki Trader_Rank] |
| L1,L2 | PART | Marriage possible from Merchant rank; spouse stats/dowry randomized; family listed on personal screen. Player aging/death: ? [V2 p4 wiki Trader_Rank; Steam guide] |
| L5 | PART | AI traders respond to your trades; saturation from fixed routes or luxury-only cargo. [V2 de.wikipedia]. Rivals can be sabotaged. [V2 Steam store 57620] |

Mechanics worth knowing:
- **Rank ladder is a four-key threshold** (wealth, ships, counting houses, workers): Trader 80,000 wealth; Wholesaler 150K + 2 ships; Merchant 300K + 25 workers; Traveling Merchant 500K, 4 ships, 100 workers; Grand Merchant 800K, 6 ships, 200 workers; Councilman 1.1M, 10 ships, 3 counting houses, 400 workers; Council Chairman 1.5M, 15 ships, 5 CH, 600 workers; President 2.2M, 20 ships, 7 CH, 800 workers; Patrician 3.2M, 25 ships, 10 CH. [V2 p4 wiki Trader_Rank 2021-01-13 and Steam guide agree]
- Rank unlocks politics: Merchant sees council information; **Councilman can propose council actions and support council projects**; Council Chairman can run for mayor; Patrician can run for Alderman. [V2 p4 wiki Trader_Rank]. How a proposal is voted: ? (tried both pages, 3 reviews, Steam store/GOG).
- Mayor controls: city 10-day balance, treasury transfers, head tax rate, and price guarantees (inflate buy/sell price of a good until the city holds your chosen quantity; you pay the difference from the treasury). Non-mayors can finance city projects, at a cost "a lot more" than the project. [V2 Steam guide]. Mayor decides whether the city builds a cathedral or university [V2 gamingnexus review]; campaigns can turn dirty (assassinate or smear rivals) [V2 cgmagonline review].
- Price structure evidence: the guide says selling 200 bricks at once drops the price 57 -> 43 and that one big sale loses no money versus selling 10 at a time (price falls more slowly then); its table gives wood (Normal) buy 40 / sell 59, narrower on harder levels (Advanced 40/52, Professional 36/46). [V2 Steam guide]. The fan wiki's Goods Index gives Low / Average / High per good (wood 29 / 48 / 66, wool 45 / 73 / 100); Low equals 0.75 x the recommended purchase price in every row I checked, High about 1.11 x the recommended sell price (my arithmetic). [V2 p4 wiki Goods_Index 2021-01-11]. Economy constants are data: `tradesystem.ini` holds a global consumption "Factor", per-commodity per-citizen consumption, per-factory production, wages, citizens per house; ship material cost is "variable based on the supply-and-demand of the commodities in the city". [V2 modding guide id=1788651794]. The stock-to-price equation itself was not found; do not quote one.
- Concentration drives trade: 40 cities (20-26 at start, 12 selectable homes), each makes about 5 of the 20 goods. [V2 p4 wiki Cities]. Burghers split poor/wealthy/rich 70/20/10 and pay rent 1/2/3 per day; under-supply (below one pip on most goods) shrinks the wealthy and rich share. [V2 p4 wiki Burghers]
- Automation compares with "<", not "<=": add or subtract one coin. [V2 Steam guide; V2 p4 wiki Goods_Index]
- Design lesson: price as a function of local stock gives arbitrage that routes exploit, tying E2 to E3 to C6 in one loop; rank-gated politics (wealth/ships/buildings/workers) is a ready template for an office ladder.

## Wildermyth (Worldwalker Games, tactical RPG with procedural story; 1.0 released 2021-06-15 [V2 wildermyth.com/wiki/Main_Page]; wiki revisions read 2019-12..2025-06, named per row)
Official wiki wikitext via `wildermyth.com/w/api.php` (the `/wiki/api.php` path 404s).

| id | val | how |
|---|---|---|
| A1,A5 | YES | Party of heroes in tactical fights; a recruitment event is offered whenever the party has fewer than 3. [V2 Hero 2025-05-21] |
| A2 | PART | Heroes are generated: a permanent "upbringing" (origin + anecdote + motivation; 1,035,914 regular upbringings) fixes stat bonuses, hooks, backstory. Manual appearance editing: ? [V2 Upbringing 2024-11-23] |
| A3 | YES | 7 levels, XP to level 2/3/.../7: Warrior 20/50/90/140/200/270; each promotion offers 3 random abilities (+1 upgrade option). [V2 Hero] |
| B7 | PART | Retired or tombed heroes enter the legacy; return as younger heroes (ages 22-26 at tier 1 up to 30-34 at tier 5) for +1 Legacy Point per tier. [V2 Legacy 2025-05-28; Hero] |
| G3 | YES | At 0 health a "mortal choice": die for a party boon, or be maimed/scarred and withdraw; a second fall in a chapter is death. [V2 Mortal_Choice 2025-03-30; Hero] |
| H2 | YES | Friends, lovers, rivals, 5 levels each, each with a combat bonus; changes arise "without the player's input". [V2 Relationship 2025-03-16] |
| L1 | YES | Personality stats, hooks and aspects per hero, set by upbringing and history. [V2 Hero; Upbringing] |
| L2 | YES | Retirement age starts at 45 for a human, modified by hooks and scars; heroes retire at chapter end after passing it. [V2 Stat 2024-06-01; Hero] |
| L3 | YES | "During intervals, a child of one of the heroes will often join the party for free"; romances need compatible personality and similar age. [V2 Hero; Relationship] |
| L4 | YES | The game picks an event matching party personality, hooks and relationships; see recency rule below. [V2 Event 2025-05-03] |
| L5 | PART | A calamity card is drawn after every battle and at timed intervals (Legacy Points can cancel them); story outputs change biomes, walls, threats. [V2 Calamity 2022-02-20; Story_Inputs_and_Outputs] |
| M3 | YES | Maimed limbs, themes, hook resolutions persist and carry into legacy recruits. [V2 Legacy] |
| E1,E5 | PART | Stations (built for 1 Legacy Point) and towns yield resources each chapter (town: 1 each of heartwood, hide, ingot, fabric; built station 2; wild station 3) to upgrade gear. v1 said "no economy": corrected to a small resource loop. [V2 Station 2019-12-04; Legacy_Point 2025-03-22] |
| E2,E3,E4,E6 | NO | No prices, trade, credit or upkeep found in Hero, Station, Legacy_Point pages. [V2, absence] |
| B5,B6 | NO | Player directs heroes; no standing orders or loyalty meter found. [M] |

Mechanics worth knowing:
- Story selection is data: targets are filled in listed order (most important role first); a "mandatory" role plus a score threshold sends the game to another story when no hero fits; an event NPC given an `npcId` can reappear later. [V2 wildermyth.com/wiki/Story_Inputs_and_Outputs]
- Inputs a story can read: company state, legacy unlocks, present/all/particular heroes (personality, relationship, hook, aspect, primary stat), overland tile (biome, adjacent rivers/mountains, contents), site type, foe faction. [V2 same]
- Outputs: gear, body modifications, history lines, permanent stat boosts, hooks/aspects, overland stations, map changes, calamities, one-fight combat advantages, relationship changes, unlocks, sacrifice a hero, recruit an NPC, trigger a fight. [V2 same]
- **Repeat suppression across campaigns**: each time an event occurs it becomes 1/4 as likely in the player's next campaign (stacking: two straight = 1/16); an unseen event doubles, up to its default. [V2 Event 2025-05-03]
- Authoring rules: risky choices read as risky, no strictly better option, big permanent changes only at chain ends, farmable tactical stories give few permanent rewards. [V2 Story_Inputs_and_Outputs]
- Time: between chapters an interval passes 10-12 years of peace in generic campaigns (older builds: from cleared tiles); years of peace "do nothing mechanically except make your heroes older"; each chapter end also removes calamity cards (1 per 7/9/11/14 collected by difficulty, plus an excess fraction). [V2 Chapter 2025-06-07]
- Legacy Points: +2 for a successful assault, defense or interception; spent to recruit, build stations, cancel calamities, or substitute for missing resources; each 10 left at campaign end buys a Legacy promotion. [V2 Legacy_Point 2025-03-22]
- Relationship bonuses: Friends +10 to +30 block when adjacent; Lovers +1 to +5 damage vs enemies who attacked the lover; Rivals +25% (level 1) up to +100% (level 5, guaranteed stunt vs a single target) stunt chance after the rival stunts. [V2 Relationship]
- Design lesson (author inference): relationships as both input and output of events is the pattern Valoria's no-GM story engine shares; the data-driven role-casting with fall-back is the part Valoria lacks.

## Still unknown
- Patrician IV stock-to-price equation and recovery rate. Tried: Steam store and 13 Steam guides screened by keyword (price table, 200-brick example, modding guide naming `tradesystem.ini`), fan wiki (40 stub pages), GameSpot (403), Kalypso forum archive (302 then 503), web.archive.org (blocked), WebSearch (quota exhausted). Would settle it: the `.ini` files in the modding guide's zip, or play-testing price against stock.
- Patrician IV vote rules (who votes, tally, council sittings). Tried the same sources. Would settle it: the printed manual or in-game help text.
- Patrician IV player aging/death, NPC personality, loan terms. Not in any page read.
- Sims 4: E3, M1, autonomy-loop description (all [M]); Council of Peers and Last Will (search summary only; thumbculture.co.uk 429).
- Wildermyth: manual appearance editing (A2); B5/B6 [M]. Anno 1800: service-radius coverage, base storage capacity, C1 (all [M]); absence of a tax slider is "not found", not proven.

## Sources
Fetched this session (page body read):
- https://www.thegamer.com/sims-every-stage-of-life-length/ (updated 2024-12-26)
- https://simscommunity.info/2023/03/15/the-sims-4-life-span-update-sim-age/
- https://simscommunity.info/2014/06/15/the-sims-4-simgurugraham-explains-aging
- https://simscommunity.info/2022/03/16/the-sims-4-guide-to-neighbourhood-stories-customisation/
- https://simscommunity.info/2022/10/16/the-sims-4-romance-guide/
- https://simscommunity.info/2026/01/29/dynasty-features-sims-4-royalty-and-legacy-we-noticed/
- https://en.wikipedia.org/wiki/The_Sims_4
- https://www.ea.com/nl/games/the-sims/the-sims-4/news/royalty-and-legacy-expansion-pack
- https://www.thesimstree.com/en/news-about-the-sims/tst-news/developer-qanda-recap-everything-we-learned-about-dynasties-in-the-sims-4-royalty-and-legacy.html
- https://snootysims.com/wiki/sims-4/how-to-pay-bills-in-sims-4-guide/
- https://sims.fandom.com/api.php (pages Free will, Action queue, Aspiration (The Sims 4), Simoleon, Motive, Sales stand, Buying and selling)
- https://anno1800.fandom.com/api.php (pages Trade, Template:GoodsValues, Exchange Ratios, Population, Needs, Coins, Residences, Trade routes, Trade Union, City incidents, Happiness, Sandbox mode, Royal Taxes, Palace, Diplomacy, Characters, Workforce)
- https://www.anno-union.com/en/devblog-seat-of-power/ and https://www.anno-union.com/en/devblog-docklands/
- https://en.wikipedia.org/wiki/Anno_1800
- https://raw.githubusercontent.com/NiHoel/Anno1800Calculator/master/js/params.js
- https://devtrackers.gg/anno-1800/p/0da09800-trading-explained-and-how-to-make-a-bigger-profit and https://steamcommunity.com/app/916440/discussions/0/1638668568130668641 (player claims, consistent with the wiki)
- https://patrician4.fandom.com/api.php (pages Trader Rank, Burghers, Cities, Counting house, Goods Index, Captain)
- https://steamcommunity.com/sharedfiles/filedetails/?id=682751098 (Patrician IV Guide), ?id=1788651794 (Modding Guide), ?id=3018508023 (FreeTheChickieNob's Tips), ?id=235985761 (Buy/Sell Prices)
- https://store.steampowered.com/app/57620, https://store.steampowered.com/app/57730, https://www.gog.com/en/game/patrician_iv
- https://www.gamingnexus.com/Article/2819/Patrician-IV, https://www.cgmagonline.com/review/game/patrician-iv/, https://www.gamingnexus.com/News/18951/Learn-how-to-trade-in-Patrician-IV
- https://en.wikipedia.org/wiki/Patrician_IV, https://de.wikipedia.org/wiki/Patrizier_IV
- https://wildermyth.com/wiki/Story_Inputs_and_Outputs, https://wildermyth.com/wiki/Main_Page, https://wildermyth.com/w/api.php (pages Hero, Legacy, Event, Relationship, Stat, Chapter/Interval, Calamity, Mortal Choice, Legacy Point, Station, Upbringing)
Search snippet only [S2]: https://www.gamespot.com/articles/patrician-iv-impressions-first-look/1100-6266569/ (403 on fetch); https://primagames.com/eguides/the-sims-4-eguide/living-the-sim-life (403); https://www.thumbculture.co.uk/the-sims-4-royalty-legacy-pc-review (429); https://ggrecon.com/guides/sims4-neighbourhood-stories.
