# T15 Pressure and political games - tutorial pass (v3)

### Against the Storm - facts line
Eremite Games (publisher Hooded Horse); roguelite city builder, real time with pause; latest patch found 1.11.2 (hotfix 2026-09-28, "Rebel Hideout" update 1.11 of 2026-09-24) [V3 https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1336490 2026-10-22]; 1.0 on 2023-12-08, Keepers of the Stone DLC (Frogs) 2024-09-26, Nightwatchers DLC (Bats) 2025-07-31 [V3 same Steam news; Wikipedia]. Assumed: base game, Viceroy difficulty (Prestige 0), tutorial then first settlements; one settlement is roughly 1 h [9T:247 says ~1 h; derived: a year is 10 min (12 at Prestige 2+) and Jacka treats year ~10 as near-unsurvivable Hostility]. No official wiki page was readable (wiki.gg HTTP 401); the Fandom wiki is stale (page revisions 2023-2025, only 5 species); the best strategy source is Jacka's guide (~Sept 2024, Prestige-oriented) [V3 https://benedictjacka.co.uk/other-writing/against-the-storm-strategy-guide/]. Treat numbers as version-bound.
Capability ids (B,D,H,L,M): B1 YES (villager panel) [V3 Steam 1.11 notes] B2 PART (newcomers arrive; no hiring; villagers leave/die) [V3 wiki Beginners Guide] B3 PART (Hearthkeeper post) [V3 Jacka] B4 YES (assign workers, specialisations) [V3 Jacka] B5 PART (Consumption Control; Automaton unit) [V3 Steam 1.2] B6 YES (Resolve per species) [V3 wiki] B7 NO [M] | D1 PART (Consumption Control, Favoring) [V3 wiki] D2 PART (rationing only; no taxes) [M] D3 NO [M] D4 YES (Hostility, Impatience tooltips) [V3 Steam] D5 NO D6 NO [M] | H1 PART (glade event choices) [V3 Jacka] H2-H6 NO [M] | L1 NO (typed pools, no named agents) [V3 9T:247-258 + wiki] L2 NO (no aging; death/leaving only) [M] L3 NO L4 PART (random glade events, mysteries) L5 NO [M] | M1 YES [V3 wiki] M2 PART (orders; tutorials) [V3 wiki] M3 YES (Citadel upgrades, seals, deeds) [V3 wiki] M4 YES (tooltips show per-minute gains) [V3 Jacka] M5 PART (settlement vs world map cycle) [V3 Steam 2023-05-18].
#### 1. Setup choices
- World map site (between runs): each hex has a biome and 0-n modifiers (positive more likely near the Smoldering City, negative farther); farther sites force a higher minimum difficulty ("difficulty zones", Seals mark zone borders) [V3 Steam 2023-05-18, 2023-06-13 experimental notes; final shape not re-checked]. 1.11 adds Rebel Hideout (limits you to two species) [V3 Steam 2026-09-24].
- Difficulty: Settler, Pioneer, Veteran, Viceroy, then Prestige 1-20 (unlocked by winning). Settler: half food use; Pioneer: 14 reputation to win; Veteran: Blightrot and corruption; Hostility multiplier 100/150/200/300% by tier; P1 18 reputation; P2 4-minute storm (2 before); P4 blueprint rerolls cost amber; P7 +50% chance of double food; P12-13 fewer blueprint/cornerstone choices; P19 pay amber per glade [V3 wiki Difficulty rev 2023-12-26; Jacka confirms 18 and 4 min].
- Caravan: pick one of several parties = a mix of 3 species and a villager count (6-8 base in 2023 notes); Jacka: take 8+ villagers over better goods [V3 Steam 2023-06-13; Jacka]. Embarkation points buy extra goods; Jacka: always buy food to 100+ [V3 Jacka].
- First blueprints: 2 or 3 offered, pick one at a time; Jacka: take a planks building first, then bricks/fabric [V3 Jacka; wiki Difficulty P16].
#### 2. The loop
Clock: real time with pause (Space) in a year of Drizzle 4 min, Clearance 4 min, Storm 2 min (4 at P2+) [V3 wiki Orders timeline; Jacka]. Meta clock: a Cycle counted in years; when it runs out the Blightstorm resets the world map except the Citadel, upgrades and deeds [V3 wiki Mechanics; Steam 2023-06-13].
1. Pause and read: map, Forest Mysteries (top right), blueprints, orders; place buildings; assign workers. Villagers fetch, build, haul and eat on their own (breaks every ~2 min per species) [V3 wiki Species].
2. Orders: 3 tier-I orders unlock 1:30 into year 1; later tiers at fixed times; each gives reputation and rewards [V3 wiki Orders].
3. Glades: woodcutters cut toward a glade; opening one is an act (Small, Dangerous, Forbidden), adds Hostility, may start a timed Glade Event [V3 wiki Beginners Guide; Jacka].
4. Reputation: each point fills the bar, lowers Impatience, and (at milestones) offers a new blueprint choice [V3 Steam 2023-02-16; wiki; Jacka].
5. Drizzle start of each year: pick one of 4 cornerstones (offered until year 10) [V3 wiki Cornerstone; Difficulty P13]. Traders also arrive on a timer, and you can summon one [V3 Jacka].
6. Storm: Forest Mysteries penalise Resolve by Hostility level; at 0 Resolve a species' villagers start leaving, each loss or death adds 0.3 Impatience [V3 wiki Beginners Guide]. Player unassigns woodcutters, burns fuel at the Hearth, stockpiles.
7. End: win when reputation is full; lose when Impatience reaches 14 or every villager is gone; settlement score, XP, seal fragments and Citadel resources go to the meta layer [V3 wiki; Steam].
#### 3. The choice menu
| verb | cost | effect | when | freq |
|---|---|---|---|---|
| Place/queue buildings | building materials (planks, bricks, fabric, parts), build time | production chains, housing | always | constant |
| Assign villagers | free; specialisations give bonuses | output, and "desired job" resolve | always | constant |
| Open a glade | cutting time; +Hostility (a Small Glade ~15 points; Dangerous/Forbidden more) | resources, ruins, blueprint, event | year start or mid-storm | common |
| Solve a Glade Event | goods and 5-7.5 min of work | reputation 0.5-1 (Forbidden ~1+), or penalties | right after opening | common |
| Choose an order | goods, time | reputation, rewards | tier unlock times | constant |
| Choose blueprint / cornerstone | none (rerolls cost amber at P4+) | permanent options for this run | per reputation point / per year | common |
| Consumption Control | forbid/allow goods per species | save goods; trade Resolve | storm, resolve party | common |
| Favor a species | 60 s cooldown | +Resolve one species, -Resolve others | emergencies | occasional |
| Sacrifice / unassign woodcutters / extra Hearth | fuel, lost output | lowers Hostility | before and during storm | per storm |
| Trade, trade routes | goods, amber | buy food, tools, fuel | any time with trader present | common |
| Send caches to Citadel | tools | reputation + amber | mid-late | common |
| World-map site, difficulty, caravan | meta currencies | next run | between runs | per run |
| Citadel upgrades, Seals, Queen's Hand | meta resources, seal fragments | permanent unlocks | between runs | rare |
#### 4. First hour, step by step
1. Play the two mandatory tutorial missions (Aunt Lori dialogue, a hint if you fail to build the first Woodcutters' Camp in time) [V3 Steam 2023-11-09, 2026-09-24]; the world-map tutorial follows [V3 Steam].
2. Optional scenarios "Hostility & Trade" and "Rainpunk & Blightrot" unlock after that and after Rainpunk; take the first at least [V3 Steam 2023-11-09].
3. First real settlement: caravan with 8+ villagers and 100+ food [V3 Jacka].
4. Pause; read Forest Mysteries and blueprints; choose a planks building first [V3 Jacka].
5. Build two Woodcutters' Camps, Crude Workstation, Makeshift Post, Trading Post; lay paths to the Main Warehouse and Hearth [V3 Jacka].
6. Staff woodcutters and stockpile wood; cut up to your chosen Dangerous Glade but do not open it yet.
7. Build shelters (housing = +3 Resolve) and comfort decorations to raise the Hearth to level 1 [V3 Jacka, wiki Species].
8. Take the year-1 cornerstone; make Packs of Provisions for trade routes; open the three orders.
9. Open the first Dangerous Glade about mid-Storm of year 1 (Jacka); pause and read the whole event text first.
10. Solve it before the next Storm (13 min timer, 5-7.5 min solve at Viceroy+).
11. Year 2+: open about one Dangerous Glade per year; get a food chain, ideally complex food your 3 species like.
12. Before the Storm each year: stockpile fuel, unassign woodcutters, check Resolve forecast under each portrait.
13. Mid-game: second Hearth; services once the town is ~20-30 villagers [V3 Jacka].
14. Final year: stack temporary Resolve ("resolve party") to fill the bar [V3 Jacka].
#### 5. What changes later
Early: setup and food; mid: exploration, trade routes, services, Blightrot/Rainpunk; late: closing out with cached tools, orders and resolve. Hostility ratchets every year and with every villager and glade, so late storms are worse. Meta: XP levels unlock buildings and cornerstones, Harpy at level 5 and Fox at 10 in the 2023 wiki; Seals, Queen's Hand permadeath trial after reforging the Adamantine Seal [V3 wiki Level; Steam 2023-12-08]. Prestige adds a modifier per level.
#### 6. Failure and ending
A settlement is lost at Impatience 14 or with no villagers; in normal mode the Cycle then continues (inferred from the Queen's Hand text), while Queen's Hand permadeath ends the trial on one lost or abandoned settlement [V3 Steam 2023-12-08]. Reforging Seals is the long goal; the Blightstorm resets the map but keeps upgrades [V3 wiki Mechanics].
#### 7. Consequential vs cosmetic choices
- Food: complex food your species like is "the big turning point" (Jacka, community expert) [V3 Jacka].
- Glade cadence trades Hostility against reputation and ruins; Jacka's "one Dangerous Glade per year" is a dominant default for ~80% of maps (his claim).
- Species mix: Jacka says good players win with any combination (community consensus); decorations and many perks are cosmetic.
- The Impatience-for-Hostility lever is real but not obvious [V3 wiki, Jacka].
#### 8. Open items
- Per-point Impatience-to-Hostility offset, and stats for Frogs and Bats: `?` (wiki table has 5 species, 2023-12 rev: Human base Resolve 15, Beaver 10, Harpy/Lizard/Fox 5; Demanding 30/30/15/15/15; Decadence +4/+2/+3/+7/+5 [V3 wiki Species]).
- Attachment claims, `9226007a...:247-312` and `89a3a060...:192`: species stat blocks (base Resolve, threshold, Resilience, Decadence, hunger tolerance, break interval) VERIFIED against the wiki table; "Frogs and Bats added later" VERIFIED. "Reputation lowers Impatience" VERIFIED [V3 Steam 2023-02-16]. "Raises Hostility" is INDIRECT: no source lists reputation as a Hostility driver (years, villagers, woodcutters, glades only), but because Impatience lowers Hostility, falling Impatience raises it; Jacka also says Hostility increases from the reputation you earn [V3 Jacka]. "Departures spike Impatience" VERIFIED (+0.3 each, +0.5 more at P20). "Higher Impatience lowers Hostility" VERIFIED, offset `?`. "~one-hour run" consistent with derived year length. 20G:440 "current to v1.5.x" is stale: current is 1.11.2.
- Wiki internally inconsistent on order counts: 12/10/10/9 (Difficulty) vs 12/11/10/9 (Orders) vs 11/10 (Mechanics) [CONTESTED]. Sacrifice values 50 per wood, 80 per coal [S3 Steam discussion snippet].

### Pax Pamir, Second Edition - facts line
Cole Wehrle (design; Drew Wehrle development; Wakhan solo AI by Richard Wilkins), Wehrlegig Games; tabletop tableau-builder / area-control, 1-5 players (solo or 2p vs the Wakhan bot), ~1-2 h [V3 https://en.wikipedia.org/wiki/Pax_Pamir 2026-10-22]. Rules relied on: publisher "Rulebook PDF" = Rules of Play, Third Printing 2021 [V3 https://www.dropbox.com/scl/fi/rxcttget9flnuuv12lhlf/PaxPamir-Rules.pdf (link from https://wehrlegig.com/products/pax-pamir-second-edition) fetched 2026-10-22]; Rally the Troops' copy is Second Printing 2020 [V3 https://rally-the-troops.com/pax-pamir/info/rules.html]; the numbers I compared (setup, costs, dominance, end) are identical. Assumed: standard rules, 3 players, no Wakhan. Digital: see section 8. Everything below is [V3 rulebook] unless tagged.
Capability ids (B,D,H,L,M; tabletop, so "NPC" = cards) [V3 rulebook]: B1 PART (your court of cards) B2 PART (buy+play card in, discard/Betray out) B3 NO B4 NO B5 NO B6 NO B7 NO | D1 NO D2 PART (Tax action only) D3 NO D4 PART (dominance/influence feedback) D5 NO D6 NO | H1 NO H2 NO H3 PART (spies, Betray, Battle on court cards) H4 PART (coalition = loyalty; deals explicitly non-binding) H5 PART (hostage-holding of a court card) H6 NO | L1 NO L2 NO L3 NO L4 PART (coalition swings, betrayals arise from play) L5 NO | M1 YES M2 NO M3 PART (board wiped by successful check; cylinders and cards persist) M4 YES M5 NO.
#### 1. Setup choices
The only real pre-game choices are player count, whether to add Wakhan, and starting loyalty; the rest is mechanical. Player order/first player is random [V3 rulebook p4].
- Players / Wakhan: 1-5 humans; Wakhan (with 1 or 2 humans) counts as a player for deck size and takes the first turn. She is "effectively loyal to all coalitions" with a per-turn "pragmatic loyalty" [V3 p16].
- Starting loyalty: each player, in turn order, sets a dial to British (pink), Russian (yellow) or Afghan (green); the last chooser takes the first turn [V3 p4]. It decides the colour of every block you place and whose dominance you can score from.
- Deck is built fresh every game: six piles of (5 + players) court cards, shuffled per pile; 4 Dominance Check events go one each into the four rightmost piles, 2 other events into pile 2 and one each into piles 3-6 (6 events unused); piles stacked unshuffled, so checks are always in the back half but at unknown depth [V3 p4]. Deck = 40 + 6n cards (n=3: 58); 12 are dealt face up into a 2x6 market.
- Each player starts with 4 rupees, 10 cylinders on their board, 1 on the VP track at 0; favored suit marker starts on the political suit [V3 p4].
#### 2. The loop
Clock: strict clockwise turns, no phases or rounds; the game clock is the deck running out and the four Dominance Checks. No hidden dice anywhere; the only randomness is deck order. Nothing is automated except cleanup and market refill.
1. Your turn: take up to 2 actions (fewer allowed). Always available: Purchase, Play. Every court card also grants its printed actions (Tax, Gift, Build, Move, Betray, Battle); each court card can be used for at most ONE action per turn [V3 p8-9].
2. Bonus actions: actions on court cards of the currently favored suit do not count against the 2-action cap (still one use per card) [V3 p12].
3. Cleanup (mandatory, 4 steps): discard court cards down to 3 + purple (political) stars; discard hand down to 2 + blue (intelligence) stars; discard any event in the market's leftmost column (its top effect hits everyone; a Dominance Check there resolves now); slide each market row left (rupees travel with cards) and refill from the deck [V3 p9].
4. Interrupts: a Dominance Check (when bought, or when it reaches the leftmost column at cleanup) scores immediately; "Instability": a second check revealed while one is in the market resolves at once and both are discarded [V3 p9, p15]. Other players affect your turn only through standing positions (rulership bribes, hostage spies) and events; I saw no out-of-turn reaction action in the rules text.
5. Worked turn (rulebook examples, [V3 p10-14]): Chas buys a 4th-column card for 3 rupees (one onto each card to its left, the vacant slot's coin goes to the other row) and cannot re-buy those cards this turn. Cati Plays a Punjab card: pays the Punjab ruler (Hope, 2 tribes) a 2-rupee bribe (if unpaid, nothing happens and no action is lost), then resolves icons top-down (road on a Punjab border, spy on a Punjab court card, +2 rupees = leveraged). Her Build: 2 armies in Kabul = 4 rupees, paid onto the rightmost market cards.
6. Game arc: first check lands in the back half; each check either pays the dominant coalition's members (5/3/1 by influence) and wipes every block, or pays everyone by cylinders in play (3/1); the 4th check doubles points; any check can end the game if one player leads by 4+ VP [V3 p9, p15].
#### 3. The choice menu
| verb | cost | effect | when | freq |
|---|---|---|---|---|
| Purchase | column index in rupees, put on cards to its left (x2 if military suit favored) | card to hand, plus any rupees on it; events resolve at once | opening, every turn you need cards or tempo | constant |
| Play | bribe to the region's ruler = their tribes there (waivable); free if unruled | card to either end of court; impact icons: army, road, tribe, spy, +2 rupees (leveraged), shift favored suit | after Purchase; the main way pieces enter the map | constant |
| Tax | free; take up to card rank in rupees from rivals with a court card in a region you rule, or from market cards | money; only rupees above the victim's tax shelter (gold stars) | when poor and ruling a region | common |
| Gift | 2 / 4 / 6 rupees (price printed on dial) | +1 influence each, in current coalition; lost on loyalty change | when contesting a check you expect to win | occasional |
| Build | 2 rupees per unit, paid to market, up to 3 armies/roads in regions you rule | the only direct way to add blocks to dominance | before a check, to swing dominance | common |
| Move | free; 1 move per rank, armies need a road of their own colour; spies walk the courts | reposition armies, spies | set up battle/rule/hostage | common |
| Battle | free; remove units = rank (max = your armies/spies present) at one region or court card; never your own coalition's armies/roads/tribes, but allies' spies are fair game | remove tribes/armies/roads/spies; can break a ruler, trigger Overthrow | to unseat a ruler or strip a hostage | common |
| Betray | 2 rupees; discard a card where you have a spy (own court too) | kills the card (leveraged = pay 2 back); may keep it as a prize (+1 influence, can flip loyalty) | to defect or to cripple a rival | occasional |
| Change loyalty | free but total: lose all gifts, prizes, patriots of old coalition | new coalition's blocks and scoring | when your coalition is losing a check | rare |
| Hold hostage | spies on a card > any other player | owner pays you spies-count to use that card's actions | positional | passive |
| Buy a Dominance Check | normal purchase cost | scores now, on your timing | when the board is in your favour | rare (4 per game) |
| Negotiate | nothing; deals are non-binding, cards never transfer | coordinate attacks and bribes | always | constant |
#### 4. First hour, step by step
The rulebook suggests teaching only Purchase and Play first and adding other actions "gradually over the first few rounds" [V3 p10]. No official in-game tutorial exists (tabletop); the sequence below is the rulebook's own order plus play derived from it (strategy beyond the rules is [M]).
1. Build the 6-pile deck and the 12-card market; give everyone 4 rupees and 10 cylinders ready; favored suit on political [V3 p4].
2. Everyone sets starting loyalty; last chooser starts. The map is empty: nobody rules anything, so every card is bribe-free.
3. First turn: Purchase a free (leftmost column) card or a 1-2 rupee card, Play it. Read its region, suit/rank stars, impact icons, actions and special ability (p3 anatomy).
4. Resolve icons: tribe in its region, spy on a court card of that region (your own card counts). A tribe and a political-suit card for the same region are tied by the Overthrow rule (lose the last of one, lose the other).
5. Mind the favored suit: icons on the card may flip it, making other suits' cards bonus actions or making purchases cost double (military).
6. Next turns: keep one action to Purchase and one to Play until your court has a Tax/Build/Move card; then use those card-actions.
7. Watch the three tableau limits in cleanup: court size 3 + purple stars, hand 2 + blue stars; excess is discarded (you choose).
8. Take ruler tokens by having a tribe AND a plurality of tribes + loyal armies in a region; this earns Build, tax rights and bribe income.
9. When you control a region, use Build to add armies in your coalition's colour; roads let armies move.
10. Spot the first Dominance Check in the market. Count blocks per coalition; dominance needs the most and 4 more than each rival.
11. Decide: if your coalition is far ahead, buy the check yourself; if no coalition leads, cylinders in play score (3/1). Hedging is the designed tension.
12. After the first check, if successful the board has no blocks; rebuild. Check VP track for a 4-point lead (immediate win).
13. Changing loyalty when your coalition is weak: play a patriot of the other colour or Betray a card with a prize; accept losing gifts/prizes/patriots.
14. Use Battle on court cards where you have spies to gain hostage control or knock out a rival's key card.
#### 5. What changes later
Complexity is constant; the pressure comes from the structure of the deck. Early game: cheap cards, spies, tribes. Mid: roads/armies, rulership and bribes, Overthrow threats, hostage positions, event cards that persist until the next check. Late: the 4th check doubles points (including ties split after doubling), the market thins as the deck depletes, and action-cost rupees with no market card to land on leave the game. No new system unlocks; the favored suit migration and event stack change what is cheap [V3 p9, p12, p15].
#### 6. Failure and ending
No elimination. A player can be locked out of scoring if their coalition is not dominant; fallback is cylinders-in-play points. Overthrow can strip your court after a lost tribe. Game ends after any check with a 4+ VP leader (immediate win), or after the final (4th) check; ties: red stars, then rupees [V3 p9]. Recovery is by defecting; the wipe removes accumulated blocks, so leads decay unless banked in VP.
#### 7. Consequential vs cosmetic choices
- Loyalty and timing of loyalty switches decide whether you score at a check; strongly consequential (rule-derived; unproven by data).
- Which card to buy, because the paid-on-left rupee scheme subsidises rivals and blocks your own repurchase [V3 p10].
- Overthrow: pairing tribes and political cards is binding in both directions [V3 p8].
- Cosmetic: card biographies and art; the three coalitions have no different rules, only different colour and sponsor; Afghan is not mechanically special.
- Whether any single line (e.g., pure military, pure intelligence) dominates is `?`; community-consensus sources not located (searches returned retail/wiki pages only).
#### 8. Open items
- Digital: Rally the Troops (free web play, programming Tor Andersson, CC BY-NC-SA 4.0) [V3 https://rally-the-troops.com/pax-pamir]; the rulebook credits a Tabletop Simulator module (AgentElrond) [V3 rulebook p19]; a Vassal module exists [S3 https://vassalengine.org/wiki/Module:Pax_Pamir_(Second_Edition)]. No commercial Steam/mobile edition turned up in two searches [S3]; Wikipedia lists none.
- Beginner strategy guide not found; turn count per game not stated in the rulebook (deck = 40 + 6n cards, 12 in market at start); BGG blocked (HTTP 403).
- Attachment claims (9T 1.1, `9226007a...:31-110`), checked against the rulebook, all VERIFIED [V3 rulebook]: 36 blocks/55 cylinders/36 coins (:35-37; p2); 142 cards = 100+16+26 (:39; p3); 2x6 market, column cost paid on cards to the left, cannot rebuy (:43; p10); bribe = ruler's tribes (:45; p11); impact icons list (:45); court 3+purple, hand 2+blue, shelter = gold, red tiebreak (:47; p6); military favored doubles purchase (:47; p10); rule = tribe + plurality of tribes+loyal armies (:51; p7); Build 3 units x 2 (:51; p13); Overthrow (:53; p8); Tax/Gift 2-4-6/Move/Betray 2/Battle three limits/Hostage (:57-65; p13-14); influence = 1+patriots+prizes+gifts and loyalty wipe (:69-71; p7); piles/DC placement, Instability, 4-block margin, 5/3/1, 3/1, board wipe, doubling, early end, kebab tie (:75-87; p4, p9, p15); Wakhan (Wilkins), pragmatic loyalty, priority list, arrows, Ambition (:91-93; p16-17); bibliography (Noelle, Bayly, Burbank & Cooper) and "emergent partnerships" statement (:97-101; p19-20). Minor: attachment cites the 2020 second printing; I read the 2021 third printing plus the RTT 2020 copy, no rule difference seen.

### Empires in Arms - facts line
Board game: Australian Design Group 1983 (Harry Rowland; Greg Pinder also signs the designer's notes), Avalon Hill licence 1985; up to 7 players each a Great Power; full game 132 monthly turns, "200-250 hours or more" [V3 https://en.wikipedia.org/wiki/Empires_in_Arms 2026-10-22]. Computer adaptation: Matrix Games / Slitherine, released 2007-12-05, lead developer Marshall Ellis, 1-7 players, solo vs AI, hotseat or PBEM, $39.99; product page lists installer v1.23.08 (2021-10-11) and update v1.27.04 (2026-04-01) [V3 https://www.matrixgames.com/game/empires-in-arms 2026-10-22; https://armchairgeneral.com/pr-empires-in-arms-now-available.htm 2007-12-06]. The Matrix news post names the 2021 update "v2.23.08" [CONTESTED vs 1.23.08]. Rules text relied on: a full reproduction of the board rulebook on RulesPal, edition not stated [V3 https://rulespal.com/empires-in-arms/rulebook]; the Matrix in-game manual PDF was not reachable, so the computer game's screens are `?` beyond the press/review text. Assumed: Grand or 1805-1807 campaign, one Great Power, rest AI/UMP.
Capability ids (B,D,H,L,M): B1 PART (corps and leader counters) B2 YES (buy factors, corps; retire leaders) B3 PART (leaders as commanders, 10.6) B4 NO B5 PART (combined movement; Matrix lets you pre-set diplomatic responses) B6 PART (national morale values; political status) B7 NO | D1 PART (peace terms lists) D2 PART (maintenance, optional economic manipulation) D3 NO D4 YES (Political Status Display zones) D5 NO D6 NO | H1 NO H2 PART (Natural Alliance Table) H3 NO H4 YES (alliances, call to allies) H5 YES (ceding, formal debts, prisoners) H6 YES (secret declarations, formal peace) [V3 rulebook 4.0, 10.5, 14.3; Armchair General 2008] | L1 NO (fixed-rating leaders) L2 NO L3 NO L4 PART L5 PART (UMPs and AI powers act on their own) [V3 rulebook 14.3; 9T/13G] | M1 YES (VP victory level) M2 YES (scenarios) M3 PART M4 PART (no tutorial in the 2008 Matrix release) M5 NO [V3 rulebook 8.1, 13-14; Armchair General].
#### 1. Setup choices
- Scenario or campaign: 1805 introductory (Sept-Dec 1805, Austria and Russia vs France), 1809, 1812, 1813-14, Peninsular War (1808-14); campaigns 1805-07, 1812-15, 1813-15 and the Grand Campaign (132 turns) [V3 rulebook 13.2, 14]. Matrix shipped one scenario (Jan 1805 on) with no editor in 2008 [V3 Armchair General 2008-01-27]; a 2009 news item promised a Scenario Editor (the spec table still says Game Editor: No) [CONTESTED], and a new 1812 scenario with EiA and "EiH" orders of battle in 2021 [V3 Matrix news 2009-08-26 headline; 2021-09-29].
- Which Great Power: France, Great Britain, Russia, Austria, Prussia, Spain or Turkey, chosen by secret VP bids; the highest bid wins that power and is subtracted from that player's VP total/level; one player may run at most 2 powers (France's player may not also take Britain) [V3 rulebook 14.2].
- Uncontrolled powers (UMPs, 2-6 players): each December, secret bids 0-5 VP per UMP plus 2 dice with modifiers decide who steers them [V3 rulebook 14.3].
- Options: morale method 1 or 2, economic manipulation (12.5), new political combinations (Poland, Italy, Westphalia, Bavaria, Confederation of the Rhine, Ottoman Empire), American trade [V3 rulebook table of contents, 7.5.2.6, 11-12].
#### 2. The loop
Clock: one turn = one month (Jan 1805 to Dec 1815); winter months Dec, Jan, Feb apply ice lines [V3 rulebook 9.1]. Matrix runs the month as diplomacy and builds, then a variable number of impulses with simultaneous movement and battles at the end of each impulse (differs from the board's power-by-power land phase) [V3 Matrix page].
1. Political Phase (A-I): Diplomacy (5-10 min talk), secret written Declarations of War (revealed together), Call to Allies, Peace, Creating Alliances, Minor Country Control, Breaking Alliances, Free State Declaration, Combined Movement [V3 rulebook 3.1, 4.0].
2. Reinforcement Phase: naval then army reinforcements placed in a fixed power order [V3 3.2].
3. Naval Phase: each power in sequence (Britain announces its slot): move fleets (7 points), intercept, naval combat [V3 3.3, 6].
4. Land Phase: each power in sequence (France announces its slot): depots, move corps (3 points, 4 French infantry, 5 cavalry), supply or forage, combat, guerrillas; Conquest step last [V3 3.4, 7].
5. Economic Phase only at end of Mar, Jun, Sep, Dec: A Victory Points, B collect money/manpower, C lend, D manipulation, E expenditure, F political status adjustment, G civil disorder, H ceding, I new political combinations, J levy, K UMP control [V3 3.5, 8].
6. Time Record: advance the month marker [V3 9.0].
Dice resolve combat and foraging; the Matrix program automates dice, supply arithmetic and bookkeeping (extent `?`).
#### 3. The choice menu
| verb | cost | effect | when | freq |
|---|---|---|---|---|
| Negotiate (secret talks) | time; promises non-binding | war plans, alliances, peace terms | every Political Phase | constant |
| Declare war on a major power | -3 political points (-2 more if breaking an alliance); -1 per district on a minor | legal right to attack; allies may be called | after an Economic Phase, short wars | occasional |
| Call allies | ally that refuses loses -2 (and the caller too if aggressor) | pulls allies in | right after declarations | occasional |
| Sue for / grant peace | surrender conditional -5 / unconditional -8; winner +3 / +5 | winner picks terms from lists A,B,C | when losing | rare |
| Create / break alliance | gain (about +1 each, per a 15.8 example) / -2 | formal ally, loans, combined movement | before big wars | occasional |
| Take a neutral minor | die roll, modifiers; +1 political point per district | yields money, manpower | after a war on a minor | occasional |
| Buy troops/ships/corps | money and manpower, months of delay per unit type (infantry 3); new counters 1 money | reinforcements | each Economic Phase | constant |
| Place a depot | 1 money (maintenance 1 per depot) | supply chain | before a march | constant |
| Move corps | movement points; force march | position, siege | every Land Phase | constant |
| Forage vs depot supply | die roll vs area forage value, or money | attrition vs cost | after movement | constant |
| Choose combat chit | none | tactic (outflank, withdraw, probe...) | each field battle | per battle |
| Lend money / cede territory | cede costs -1 political point | help ally | Economic Phase | occasional |
| Economic manipulation | optional rule | trade political points for money | Economic Phase | optional |
#### 4. First hour, step by step
Board rules advise playing "a scenario or two" before a campaign [V3 rulebook 1.3]. Matrix has no tutorial in the 2008 review; later patches unverified.
1. Read 1.3 and pick the 1805 introductory scenario (Austria, Russia vs France; 4 months).
2. Set up forces by the scenario list (13.2.1); note starting money (Austria $5, Russia $3, France $10).
3. Check victory: France wins by holding Vienna at the end; otherwise the Allies win [V3 13.2].
4. Move in sequence (France first), counting movement points per corps; force marching adds 1 point but forces foraging [V3 7.3.1.2, 7.4.1].
5. After moving, resolve supply: depot supply costs money, foraging risks losses on a die roll.
6. When armies meet, each side secretly picks an Operational Possibilities chit; reveal and cross-index; compute morale; roll rounds [V3 7.5.2].
7. Retreat, pursuit and political points follow combat (see 8 for values).
8. Next month, repeat; reinforcements arrive by schedule.
9. Graduate to a campaign (1805-07): bid for a power, set up, then add Political and Economic Phases.
10. First Political Phase: talk, write declarations or "no declarations", reveal.
11. Run the first Economic Phase (March): victory points by status box, collect taxes, pay maintenance, buy factors.
12. Check where your marker sits on the Political Status Display; avoid Instability/Fiasco.
#### 5. What changes later
Mid game: coalitions form (designers advise "divide and conquer" for France), peace terms reshape borders, UMPs change hands each December, new political combinations appear. Late: bankruptcy (-3), capitals occupied (-3 London/Paris, -2 Berlin/Constantinople/Vienna, -1 Madrid/Moscow/St Petersburg), Free States, guerrillas. Victory requires average ~9 VP per quarter for Austria (110 VP in 1805-07) [V3 15.8].
#### 6. Failure and ending
A power that collects no home manpower is out permanently (civil disorder), its enemies gain 5 political points [V3 8.7]. A marker forced off the bottom must sue for peace; a ceded capital province also removes a power [V3 10.5.1, 4.4]. Campaign winner = first to reach its victory level (manpower in controlled provinces counts at the final check); Great Britain wins if none does [V3 8.1.3.2]. Scenarios have fixed objectives.
#### 7. Consequential vs cosmetic choices
- Declaring war costs political points up front, so "the ideal war is short and successful, declared just after an Economic Phase" (designer hint) [V3 15.8].
- Timing of alliances relative to the Economic Phase (the status box's adjustment can nullify the gain) [V3 15.8].
- VP bid to play a power prices asymmetry (France is expensive) [V3 14.2].
- Cosmetic: historical names and art (leader ratings do matter). Combat chits matter per battle; whether any one chit or opening dominates is `?`.
#### 8. Open items
- Political Points Chart (back of rulebook) and the Political Status Display box values (VP and PSA per box) are not in the fetched text; values below are reconstructed from rule text only: -3 war on major, -2 break alliance, +3/-5 conditional surrender, +5/-8 unconditional, +/-1 per corps in a field combat (max 3, extra 2 if NAPOLEON loses), -1 per scuttled fleet, +1 per conquered district [V3 rulebook 4.2, 4.4, 7.5, 10.2].
- Attachment claims (13G = `e3f9f19a...`): 13G:74 political phase list A-I VERIFIED verbatim; 13G:78 economic list A-F is TRUNCATED (real list A-K); 13G:72 "132 turns" VERIFIED (Wikipedia), "100-150 hours" (box copy) NOT checked, Wikipedia says 200-250; "status gravitates to centre" CONSISTENT (negative PSA in the Dominant Zone box, 8.6/15.8) but per-box values `?`; 13G:77/427/537 "VP bids to choose power" VERIFIED (14.2), though the bid reduces the player's VP level rather than being "spent"; `13G:469` "battles resolve in one step as in EiA" FALSE: field combat has ~14 steps with secret chits, outflank, withdrawal, morale and rounds [V3 7.5.2]; "chart of credits and debits, per-turn debits" VERIFIED in part (per-turn -1 for forcible access, 10.3).
- Matrix manual/screens, AI quality: `?`.

### Middle-earth: Shadow of Mordor and Shadow of War (the Nemesis system) - facts line
Monolith Productions (closed by Warner Bros. Games, Feb 2025) / WB; third-person open-world action-adventure with Arkham-style combat; the Nemesis layer is a persistent hierarchy of named enemy orcs. Shadow of Mordor (SoM) 2014-09-30 on PS4/PC/XOne (PS3/360 2014-11-18); Shadow of War (SoW) 2017-10-10 (Gamereactor says 9 Oct) [V3 WP-W, WP-M, ST 2025-02-25]. Relied on SoW as it stands after July 2018 (marketplace and microtransactions removed; Definitive Edition Aug 2018) [V3 WP-W]; both reached Switch 2 on 2026-09-30 [V3 ST]. Exact patch/build `?`. Assumed: SoW single-player campaign, SoM differences marked. A session is about 1-2 h [M]; the campaign is long (Gamereactor needed "almost 30 hours" to craft a first top-level gem) [V3 GR]. Sourcing is wiki plus press plus designer interviews; no first-party manual was read, and the SoM first hour is [M] (no SoM beginner's guide fetched).
Source keys (all read as saved page bodies this session): WP-M/WP-W = en.wikipedia.org/wiki/Middle-earth:_Shadow_of_Mordor / _Shadow_of_War (raw wikitext, 2026-10-22); FW-N/T/F/D/B/DT/W/M/LM/SW = shadowofwar.fandom.com/wiki/Nemesis, Nemesis_Traits, Fortress, Domination, Brand, Death_Threat, Middle-earth:_Shadow_of_War, Middle-earth:_Shadow_of_Mordor (rev 2019-09-11), Lord_of_Mordor, Shadow_of_Mordor_Super_Walkthrough (api.php revisions; Nemesis rev 2025-07-03, Traits 2025-08-01; the wiki mixes SoM and SoW, game named where it says); PM = de Plater's Gamasutra postmortem as quoted by gamebanshee.com/news/114981-middle-earth-shadow-of-mordor-postmortem.html (2015-01-20) and kotaku.com/shadow-of-mordors-nemesis-system-couldve-been-way-more-1681120649 (2015-01-22); GB = gamesbeat.com/shadow-of-mordors-nemesis-system-draws-from-burnout-football-and-an-architecture-book/ (DICE 2015 interview); SDT = selfdeterminationtheory.org/gamasutra/ (2015-02-04); SN = shacknews.com/article/101634/ (2017-10-09); RS = rpgsite.net/feature/6192-shadow-of-war-domination-guide (2017-10-16); GR = gamereactor.eu/shadow-of-war-beginners-guide/ (2017-10-10); GRD = gamesradar.com/middle-earth-shadow-of-war-tips/; GBolt = gamingbolt.com Nemesis guide (2017-10-12); US = image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10926179 (image PDF, pp.1 and 36 read); ST = Steam news API, appids 356190 and 241930.
Capability ids (B,D,H,L,M; SoW unless noted): B1 YES (Army screen lists captains, warchiefs, followers) B2 YES (Dominate Captain then Recruit; Shun/Retreat to dismiss; SoW also sold followers via war chests until July 2018) B3 YES (bodyguard to a warchief, spy, Overlord, assault leaders) B4 YES (Command: duel, assassinate, spy, pit fight) B5 PART (send captains on missions alone; "Stay and Fight for Me"; no standing rules) B6 PART (SoW followers grow loyal or antagonistic by treatment and can betray; no meter seen; SoM none) B7 PART (vacancies refilled by promotion; SoM-to-SoW Nemesis Forge imports one nemesis and one follower) [V3 FW-N, FW-D, FW-W, RS, WP-W] | D1-D6 NO (no laws, taxes, councils or courts; the only "policy" is fortress upgrades) [V3 FW-F] | H1 PART (a Dominate menu and taunts, no dialogue trees) H2 YES (rivals, blood brothers, bodyguards, grudges) H3 YES (spies, betrayal, death threats, staged power struggles) H4 PART (blood-brother bonds, tribes; no treaties) H5 PART (chain of command, thralls; no ransom) H6 NO [V3 FW-N, FW-D, FW-T] | L1 YES (names, traits, history, memory) L2 PART (death and scarred return; no ageing or births) L3 NO L4 YES (power struggles, vendettas) L5 YES (AI captains run missions and rise or fall; staged, see 2) [V3 FW-N, SN, PM] | M1 YES (campaign endings; death is not a loss) M2 YES (story missions, Gollum/Ithildin/weapon quests) M3 YES (promotion, scars, fortress state persist) M4 PART (silhouettes until intel; outcome odds `?`) M5 PART (open world to Army screen to siege; no strategic map) [V3 WP-M, WP-W, SN].
#### 1. Setup choices
- Which game and edition: SoM (2014; Game of the Year adds Lord of the Hunt, 2014-12-16, and The Bright Lord) or SoW (Standard/Silver/Gold/Mithril retail editions; Definitive Edition bundles the expansions, Aug 2018) [V3 WP-M, FW-W, WP-W]. SoW expansions: Desolation of Mordor (May 2018, plays Baranor) and a second one (Eltariel) [V3 WP-W].
- No character creation: Talion is fixed in both; the only build choices come later (skill tree, gear, bodyguard) [V3 WP-W, GR].
- Difficulty: SoW added an "easy" mode in a post-launch update [V3 WP-W]; the full list of levels is `?`.
- SoW only: import a top SoM nemesis and most loyal follower through the Nemesis Forge (needs a SoM save; current availability `?`) [V3 WP-W].
- Online (asynchronous; server status now `?`): Online Vendetta enters another player's nemesis system to kill their nemesis; Social Conquest invades their fortress, friendly or ranked (ranked risks losing followers) [V3 WP-W].
- The army itself is not chosen: names, titles, looks and traits are generated per playthrough with no seed or option to set [V3 FW-N].
#### 2. The loop
Clock: real time with a pause menu; the enemy hierarchy does not tick on a timer but advances at beats: Talion's death, a Forge Tower (SoM) and mission markers [V3 FW-N]. One older description claims the world "progresses in real time even if you do not interfere" [V3 FW-M, quoting a 2013 Game Informer preview] [CONTESTED with FW-N]; Shacknews calls Vendetta and Nemesis missions timed [V3 SN].
1. Generation (automated): a grunt becomes a Captain by killing Talion, beating a Captain, or taking a vacant slot; he gets a name, title, look and traits from large pools; low Power Level guarantees more weaknesses and fewer strengths, high Power the reverse, and traits shift as he levels [V3 FW-N]. SoM traits: strengths (invulnerabilities, "hate" triggers that enrage, attacks, weapons) and weaknesses (instant or extra damage, fears that make him flee, e.g. fire, caragors, ghuls, graugs, flies, a rival, betrayal, the Gravewalker) [V3 FW-T]. SoW adds seven tribes (+2 DLC), ten advanced classes and elements; his label reads like "Cursed Terror Slayer" [V3 FW-N]. Level cap 20 (25 Bright Lord DLC) in SoM, 85 in SoW [V3 FW-N].
2. Open the Army screen: captains in rows, warchiefs above, (SoW) an Overlord at the top; unknown nemeses are silhouettes [V3 FW-N, SN].
3. Gather intel: dominate a Worm, a grunt, a Captain, or read an intel drop or bulletin board; SoW grunts give only name, level, location and strengths, while weaknesses need a Captain, drop or Worm, and warchiefs only come from Captains or Worms [V3 FW-N, RS].
4. Pick a target and approach it by its traits (ranged, stealth, beasts, fire, or avoid what enrages it), then fight in the open world [V3 SN, GR].
5. Resolve: kill (loot), dominate, or die. Meanwhile AI nemeses run Power Struggles shown as map markers: Duel/Riot, Ambush, Execution, Feast, Recruitment, Trial by Ordeal, Beast Hunt, Betrayal; a win gives +1 power, a loss death or flight; you may help, hinder or kill both [V3 FW-N]. Automated: promotions into vacancies, level gains, scarred returns.
6. Interrupts: your death (mission cancelled, killer rises, SoW spawns a timed Vendetta), ambushes by nemeses, betrayal by a follower, siege milestones [V3 WP-M, WP-W, SN, RS].
7. Fortress loop (SoW): intel on a fortress, thin its warchiefs, pick assault leaders and upgrades, assault, capture one victory point per warchief, kill the Overlord alone in the throne room, appoint a new Overlord and defend later [V3 FW-F, WP-W].
#### 3. The choice menu
| verb | cost | effect | when | freq |
|---|---|---|---|---|
| Fight/avoid a Captain by traits | health, risk of death | kill gives rune/gear and opens a slot; losing promotes him | whenever one is met | constant |
| Gather intel (Worm, grunt, drop) | stealth and time | reveals strengths/weaknesses/level/location | before any target | constant |
| Dominate a grunt | a few seconds, health drained | sleeper agent/ally, heals Talion; may fill a vacancy under your control | stealth or mid-fight | constant |
| Dominate Captain: Recruit | captain broken first; level must be <= Talion's (SoW); Iron Will resists | joins your army | prize with useful traits | occasional |
| Shame (SoW) | none; may backfire | level -5 (-12 with Worse Than Death), permanent scar, may go deranged or maniac | captain too high to recruit | occasional |
| Death Threat | one active at a time (RS); target +5 power and more bodyguards (SoM) | better rune/loot chance | only if you will kill him | occasional |
| Command a branded captain | none | duel or assassinate another nemesis; he levels | after recruiting | occasional |
| Initiation, bodyguard, Betrayal | a branded captain | draws out a warchief; his bodyguard may betray him | warchief hunting | occasional |
| Interfere in a Power Struggle | time, risk | choose winner, or kill both | when a marker appears | constant |
| Die on purpose | mission progress lost | killer levels, a Vendetta pays richer loot | loot gaming [V3 GRD] | rare |
| Pit fights, solo missions (SoW) | followers can die for good | followers level | between sieges | constant (Act 2+) |
| Assign bodyguard (SoW) | cooldown, exposure | ally on call | always | constant |
| Siege prep: assault leaders and upgrades | one leader per warchief slot | siege beasts, hosts, archers, banners | each fortress | per fortress |
| Defend a fortress: Overlord, warchiefs, upgrades | captains tied to slots | walls, gates, hosts, beasts, mines | after conquest | per fortress |
| Raise dead / Undying Loyalty | late skills | revived orc, lower level, cannot level | after losing a favourite | rare |
#### 4. First hour, step by step
SoW from guides [V3 GR, GRD, RS, SN]; SoM beats [M] unless marked.
1. Play the prologue: climb, stealth, strike chains (8 strikes unlock a finisher), parry on the symbol, dodge red attacks [V3 WP-W].
2. Learn to run: elven dash and vaults, then drain rats and spiders to heal [V3 GRD].
3. Purify Haedir towers for fast travel and map reveal [V3 WP-W].
4. Spend skill points sparingly: one perk of three is active per skill; skills unlock by story or level [V3 GR].
5. Meet the first Captain and open the Army screen: silhouettes, rows, an Overlord [V3 SN].
6. Find a green-marked Worm in wraith vision and dominate it for fortress hierarchy and weaknesses [V3 RS].
7. Read the traits, choose the approach (arrow to the knee roots a runner; fire for fire-fearers) [V3 GR].
8. Wear him down until a green icon marks him broken, then Dominate Captain (story skill) [V3 RS].
9. Choose Recruit, Shame or Fight to the Death; guides say to shame what is above your level [V3 GRD].
10. Die once: see the killer promoted and a Vendetta appear; finish it before the timer for better gear [V3 SN, GRD].
11. Equip loot by rarity; kill white-marked orcs for gems; open Ithildin poem doors for legendary gear [V3 GRD, GR].
12. Act 2: build an army, assign a bodyguard, send captains to missions and pit fights [V3 GR, RS].
13. Dominate a warchief's bodyguards; they betray him, or send a captain as spy [V3 GBolt].
14. Prepare and run the first siege; plan assault leaders against the defenders' fears [V3 GRD].
SoM opening [M]: Black Gate prologue, first quests The Slaver, An Interested Party, The Spirit of Mordor (the wiki's three first main quests) [V3 FW-SW], Brand unlocks later.
#### 5. What changes later
SoM: Branding arrives mid-game, Warchiefs must be drawn out (Initiation, Betrayal, Riot) and the endgame fights your "ultimate nemesis" with five branded Warchiefs [V3 FW-LM]. SoW: five regions, four fortresses ruled by Overlords with 2-6 Warchiefs each, then Barad-dur [V3 WP-W, FW-F, FW-W]; blood brothers, tribes, betrayal, beasts and Olog-Hai; after the campaign Shadow Wars (renamed Epilogue, July 2018) require defending fortresses 20 times for the bonus ending [V3 WP-W]. Pressure ramps through levels (cap 85), immunities, Iron Will and enraged triggers; intel loses its edge ("glaring weak links are rarer") [V3 GR].
#### 6. Failure and ending
Dying is never a loss state: respawn, mission cancelled, killer promoted [V3 WP-M]. Real losses: followers killed in pits or missions are gone for good [V3 RS]; ranked Social Conquest can cost followers [V3 WP-W]; betrayal. A beheaded nemesis never returns; others may return scarred [V3 FW-N]. What a failed fortress defence costs is `?`. Endings: SoM kills the Black Hand and Sauron's body; SoW storms Barad-dur and leaves Talion holding Minas Morgul [V3 WP-M, FW-W]. Always recoverable.
#### 7. Consequential vs cosmetic choices
- Trait intel plus the matching approach is the main skill lever: "mortal vulnerabilities" one-shot many low Captains (press guide, not measured) [V3 GR].
- Dominating a warchief's bodyguards first makes the warchief fall to treachery; guides call it the standard route (consensus, not tested) [V3 RS, GBolt].
- Dying and Death Threats are loot levers with a dominant exploit shape (feed a captain, then kill him) [V3 GRD, FW-DT].
- Recruiting is gated by level, so shaming is the dominant path for high-level captains (press guide) [V3 GRD].
- Cosmetic: names, titles, scars and taunts mirror traits and history; whether any alters power is `?` (inference).
#### 8. Open items
- No v2 capability table exists for these games, so nothing was corrected; the ids above are fills. SoM army slot counts (five branded Warchiefs per FW-LM) and SoW Overlord count per region are `?`; fortress-defence failure cost, difficulty levels, trait counts per Power Level, SoW loyalty visibility, online servers: `?`.
- Attachment claims (EN = `62dd3fd3...`; the other three attachments: 0 hits for Nemesis or Mordor): EN:313 "best documented by de Plater's DICE 2015 talk and Gamasutra postmortem" VERIFIED that both exist [V3 GB, SDT, PM]; the postmortem was read only as quoted, not in full.
- EN:315-319 captains with generated name/look, strengths, weaknesses, fears: VERIFIED mechanically [V3 FW-N, FW-T: "Fear" and "Hate" trait classes; GB: pen-and-paper recurring villain]; the quote "If you're a dungeon master ... trait or mannerism or a quirk" (EN:317) NOT FOUND verbatim in pages read (GB carries a different D&D quote) `?`. Traits as approach-dictating: VERIFIED (invulnerable to ranged/stealth, vulnerable to finishers) [V3 FW-T].
- EN:319 killer is promoted, gains power, remembers; survivors scarred: VERIFIED with a nuance: a grunt who kills Talion becomes a Captain, a Captain/Warchief gains Power Levels; scars and "cheating death" returns [V3 FW-N, WP-W, GB].
- EN:321 de Plater's framing as self-determination theory: VERIFIED (competence, autonomy, relatedness; also PENS and GNS) [V3 SDT]. Sports seasons: the framing is VERIFIED in substance (EA Sports/Madden career commentary; narrative "from season start to midseason and onto playoffs") [V3 GB]; the exact quote "In sports games, you very much create your own narrative through a season" NOT FOUND verbatim (one search; a German PC Games interview carries the idea) `?`.
- EN:321/525/673 "Christmas tree": the quote is VERIFIED verbatim: "multiple Uruk Factions with separate bars for Morale and Discipline, each Captain influenced these Bars ... their Hierarchy UI looked somewhat like a Christmas tree" [V3 PM]. The bars also "determined the behavior of the Orcs in combat as well as emergent missions", so they were state, not just display. EN's gloss "the team cut the state rather than fix the display" is NOT STATED: the postmortem says they "progressively returned" to the original focus after playtests; Kotaku reads it as dropping warring fiefdoms [V3 PM]. An inference, partly supported.
- EN:327-331 table, "Player can be disobeyed: n/a": true for SoM (RS: "unlike in Shadow of Mordor"); WRONG for SoW, where recruited captains can betray and fight you [V3 RS, WP-W].
- Patent: not in any of the four attachments (0 hits for "patent" or "926,179"); it appears in `v2/REPO_MENTIONS.md:151`. VERIFIED that US 10,926,179 B2 exists, titled "Nemesis characters, nemesis forts, social vendettas and followers in computer games", Warner Bros. Entertainment, inventors include de Plater and Stephens, filed 2016-03-25, granted 2021-02-23, 36 claims [V3 US p.1]. "Covers it" PARTLY: claim 1 (read) is a method where an NPC automatically opposes avatars by parameters, a predefined event triggers changing a second NPC's parameters, and the change is output; claims 2-4 add avatar death or zone entry as the trigger and a ranked faction hierarchy; 5-9 share faction data with another player's game [V3 US p.36]; other independent claims and legal scope not read.
