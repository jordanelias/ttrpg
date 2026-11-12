# Digest research_rest1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: research files an earlier digest lane (`DG_research1.md`) could not read in full. Research is tier 3 (CLAUDE.md §0.05): shapes are the durable finding, figures are leads. Tags used: CORE, CHAR, PC, MB, SC, FA, SE, FI, WR, DICE, GO, ARCS, PROCESS.

### research/game_precedent_suite/dispositions/repo_claims_checked.md
- **What it is:** read-only scan (2026-10-22, agent-authored, precedent-suite "dispositions" layer) of what the repo already says about the comparison-set games, with claim-by-claim checks against outside sources.
- **Status:** no Status line. Reading: historical/reference; useful as a provenance map, not as design.
- **Bears on:** PROCESS, FI, SC, MB, FA, SE, CHAR, WR.
- **Content that matters:**
  - Provenance ceiling: Paradox/KOEI/Brigandine/Unicorn Overlord wikis returned 402/403, so "specific figures about games are leads; the durable findings are shapes"; strongest rows are Victoria 3 law enactment, Pax Pamir pricing, Burning Wheel Duel of Wits (:14-17). Four feeders: companion, verb-coverage doc VCD, uploaded surveys (uncommitted, cannot be re-opened), verbs lexicon where nearly every game cell is `[MEMORY]` (:17-22).
  - Coverage table of the comparison set with depth grades: Total War 58 files (deep on morale/autoresolve/governors); Mount & Blade "medium, thinnest treatment"; Disco Elysium 39 files, medium and partly unverified; Pentiment 32 files medium-deep; Shadows of Doubt "deep in VCD (snippet-level)"; L.A. Noire 9 files "partly [MEMORY]"; Return of the Obra Dinn 5 files "one mechanism (batch confirmation)"; Griftlands 5 "one mechanism (negotiation)"; Unicorn Overlord 14 mentions as a label; Ultimate General / Field of Glory name-drops (:28-60). Zero hits for Baldur's Gate 3, Darkest Dungeon, Eternal Darkness, Don't Starve, Vampire: Bloodlines (:61).
  - Per-game claims with file:line: Total War autoresolve "a different algorithm", calibration "never published", divergence "exploited in both directions" (:80); Total War 3K two-tier defeat (general's death destroys retinue only if army also routs) (:79); Obra Dinn "sets of three, last six in twos", Valoria rejects confirm-in-threes (`fieldwork:92`) (:116); Griftlands warning (spend-and-roll persuasion "a lot less fun than fighting", eleven-turn deadlock) "answered for the old kernel, never carried to the new one" (:119-121); L.A. Noire grades every answer vs a hidden reading, Truth/Doubt/Lie (:113).
  - Errors found in repo claims (section 4): Battle Brothers armour is a Max-Fatigue penalty, not a per-action drain (the `.designs` derived_stats claim is WRONG) (:160-161); Victoria 3 enactment numbers are stale/version-dependent, 2-year cooldown applies to cancelling (:162-164); Old World ambitions pass to successors as legacies, ten ambitions = victory, not "expire when the ruler dies" (:165-166). Internal admissions: M&B "layers do not couple" vs "fully fused" (`by_lane/PC:89`) (:167).
  - Games the repo leans on that are outside the comparison set: Romance of the Three Kingdoms (59 files, "officer mode" precedent), Dwarf Fortress, EU4, Jagged Alliance 2/3 (five-layer morale, militia vs regulars), RimWorld, Dominions (commander-anchored rout "scale-blind"), Football Manager (fidelity ladder, formation/role model; "the repo's model of the right shape"), Nemesis system, Caves of Qud, Ace Attorney 18 files, Triangle Strategy, Brigandine, Unicorn Overlord (:142-154). Tabletop: Burning Wheel 42 files, Pax Pamir, Republic of Rome (:156).
  - Method limits: only web checks run were sections 4.1-4.3 and Obra Dinn; `proposals/2026-10-16-verbs/*`, UI v4 and `.audit/` workings not read in full (:172).
- **Conflicts / stale:** the Battle Brothers finding contradicts `.designs/systems/_architecture/reference/derived_stats_v30.md:126-128`, which states armour adds to per-action fatigue; if the PC fatigue rule cites that precedent, the precedent is wrong (:160). Vic3 numbers used in `companion_part6` are pre-1.3.
- **Open items:** the Dominions edition, Total War title, Field of Glory edition are unspecified in the repo; "Total War calibration never published" cannot be confirmed (:82, :174).

### research/game_precedent_suite/tables/R7_magic_sanity_travel.md
- **What it is:** v2 verified comparison table (2026-10), cost-of-power, sanity/stress and travel/survival across Darkest Dungeon II, Sunless Sea, Eternal Darkness (+Call of Cthulhu 2018), Don't Starve, Pathologic 2, Vampire: Bloodlines; tags each claim V2/S2/M.
- **Status:** no Status line. Reading: reference, thin consumer in the design (threadwork Coherence cost).
- **Bears on:** WR (threadwork/Coherence), CHAR (stress/condition), SE (travel/hunger), CORE.
- **Content that matters:**
  - Valoria referent: threadwork cost = Coherence, a recoverable stretch of 6 over a permanent resting point; past 5 the practitioner leaves the human band; Mending costs 0 Coherence at every degree but is still a roll (MENDING_OB) (:2).
  - Don't Starve: Codex Umbra is a rental of max Sanity (the puppet dies after 2.5 days and the 55 max sanity returns), "closest in structure to Valoria's recoverable stretch" (:86); tiers are monotone thresholds of one scalar, costs legible per-minute rates from one table (:88).
  - DD2 stress fork: at Stress 10 a Meltdown (80% base) vs Resolute (20% base) fork whose odds are built from character state (quirks add percent points) (:12, :24); banter bands feed a stress-to-affinity scalar so one number drives the relationship layer (:22).
  - Sunless Sea: three clocks (Hunger, Fuel, Terror) share cargo space so "a trip is one allocation decision"; Terror above 50 drops to 50 on return, the excess becoming nightmares (a persistent cost) (:47, :52); story time counts completed voyages not minutes (:51).
  - Pathologic 2: the Bound-NPC infection roll is a seeded daily draw (random immunity vs a hidden 1-100 infection value, resolved at midnight, player mitigation raises it), "close to Valoria's draw model"; per-death permanent penalties (max health at deaths 1,2,4,5,8,...) (:102-103). Eternal Darkness: sanity effects need a display layer; a no-GM engine can reproduce the damage tiers (:66).
  - Bloodlines: power costs recoverable blood while Humanity is a slow score, "the power itself does not erode Humanity" unlike Valoria (:119); Masquerade is a 5-count lives meter (:112).
- **Conflicts / stale:** v1 claims corrected inside the file (Codex Umbra permanence, Pathologic infection roll attribution, spoiled food); Humanity floor 3 vs 0 CONTESTED (:116). Sunless Sea terror recovery prices from a player-edited wiki (:46).
- **Open items:** DD2 whether Stress resets after Meltdown; Call of Cthulhu 2018 shipped behaviour; Pathologic 3 shipped values (:126-133).

### research/game_precedent_suite/tutorials/T01_realm.md
- **What it is:** tutorial pass (2026-10-22) teaching how to play four realm/dynasty games (CK3, Victoria 3, Old World, Pathfinder: Kingmaker): setup, loop, choice menu, first hour, late game, failure, consequential vs cosmetic choices.
- **Status:** no Status line. Reading: reference; strongest on CK3 (read from the game's own script files) and Old World (developer build notes).
- **Bears on:** FA, SE, CHAR, CORE, WR (game-loop shape for the strategic layer).
- **Content that matters:**
  - CK3 loop: real time with pause; the player acts through instant character interactions, each with a price (gold, prestige, piety, hook, or long-running scheme); battles are not tactically controlled ("battles will happen automatically if two hostile armies cross paths") (:19-25). Game over only on death with no heir or the 1453 end date; no victory screen (:77-78). Council: one task per councillor, skill effect scales linearly, friend +20%, rival -20% (:32); claim-CB prestige 100 per county, 200 per duchy (:37); domain limit over-limit -20% levies and tax (:40); de jure drift ~100 years (:72).
  - Victoria 3 loop: player is the state, never a person; "you change a parameter and the simulation responds"; law enactment = 3 phases, checkpoint every ~100 days, 730-day cooldown, 3 setbacks fail it; enactment events time out to the default option so only one is ever pending (:107-122). Failure: default pauses construction; revolutionary war loss = game over (:158-159).
  - Old World: 1 turn = 1 year, Orders as the single action budget (Legitimacy grants Orders; formula unestablished, 0.1 per Legitimacy point is a CONTESTED older figure), undo of any order within a turn, events with Memories/Traits/Relationships that trigger later events, laws as pairs costing Civics (first switch 200, +100 each) (:190-217). Ambitions are offered by events; ten = victory; a National Ambition at 70% progress after 5 completed (:239).
  - Pathfinder Kingmaker kingdom layer: cards (problems/opportunities/projects/throne-room visitors), one free advisor assigned per card, resolution when days run out: d20 + advisor attribute mod + 2 per rank + unrest modifier (Serene +1 .. Crumbling -4) vs DC; bands Disaster 8+ under, Failure 1-7, Success 0-6 over, Triumph 7+; Crisis Points +5 each (:274-276, :285). Unrest ladder to "destroyed = game over"; the wiki calls it "more of a mini-game" (:322, :331).
  - Auto-management in Kingmaker "could get stuck and refuse to skip time" (patch 1.3), Auto cannot be switched off once on (:266, :279); time-limited chapters are the real lose condition (:323, :329).
- **Conflicts / stale:** versions pinned (CK3 1.20.1.2, Vic3 1.13.11, Old World 1.0.84977, Kingmaker 2.1.7b); council seat naming caveat (Confidant vs spouse seat) (:90); Old World Orders formula and Kingmaker random-card spawn rule unknown (`?`).
- **Open items:** Vic3 end-of-campaign behaviour, default succession law in CK3, Kingmaker 90-day Stolen Land consequence (:88, :170, :323). Attachment-claim table said to follow at end of file (a "see end of file" for CK3 claims at :92) but file ends at the capability line (:336).

### research/game_precedent_suite/tutorials/T02_warband.md
- **What it is:** v3 tutorial pass (2026-10-22) teaching Mount & Blade II: Bannerlord, Mount & Blade: Warband, Battle Brothers and Kenshi (setup, loop, choice menu, first hour, late game, failure).
- **Status:** no Status line. Reading: reference; the M&B and Battle Brothers rows are the campaign-economy and squad-manager precedents the MB brief names.
- **Bears on:** MB, CHAR, FA, SE, PC.
- **Content that matters:**
  - Bannerlord loop: real-time map with pause, year = 84 days / four 21-day seasons; each day the game eats food, pays wages (unpaid or unfed troops lose morale then desert), moves all AI parties; contact opens fight/avoid/talk, and a battle may be played, sent, or auto-resolved; personal kills raise influence/renown share (:15-18, :32). Troops "do nothing until told" in the player-fought battle (:19).
  - Troop economy: recruit from village/town notables; relation with the notable sets recruit tier, each notable favours a troop type, AI lords recruit "exactly the same way" so the player competes for a finite pool; upgrade needs XP + denars (+ a horse for cavalry); wages become "the most expensive thing in the game" with thousands of troops (:29-30, :65, :85).
  - Clan tier gates everything: renown 50/150/350/900/2,350/6,150 for tiers 1-6, each raising party size, party slots, companion cap; mercenary at tier 1, vassal at tier 2, found a kingdom at tier 4 + a town (:56, :63, :75). Influence is the scarce currency spent on armies, votes, fief revocation; kingdom decisions are weighted votes where the ruler overrides by paying (:39-40, :80-81).
  - Bannerlord character data: 6 attributes x 3 skills (18), focus points max 5 per skill; learning limit = (Attr-1) x 14 + Focus x 40 + 4 (330 at 10 attr/5 focus), CONFIRMED against forum tables; traits Mercy/Valor/Honor/Generosity/Calculating -2..+2 have stated behavioural hooks (:11, :83-84).
  - Battle Brothers: turn-based, units act one at a time with Action Points and Fatigue, 12 per fight, "you control every unit in battle (no auto-resolve)", equipment budget vs fatigue ("too heavy and fatigue runs out"), permanent deaths and injuries, crisis arcs; Warband: no influence currency, relation with each lord does the work, fief award formula (renown+500)/(1+3 towns+2 castles+villages) x random x conqueror bonus + 2x relation (:137, :166-169, :176).
  - Kenshi: per-limb health, squads under job queues, raids redirected to a built base; no auto-resolve fights in real-time AI-driven combat (:227-228, :246).
- **Conflicts / stale:** Warband tax-inefficiency cap 35% vs 65% CONTESTED; guide-grade throughout for Warband; Bannerlord numbers are 2020-2022 (1.0-1.1 era) not 1.4.8 (:4). A clan-tier-to-found-a-kingdom figure disputed (tier 3 with 100-man army vs tier 4) (:75).
- **Open items:** AI vote logic "reflexive" per players but no page opened (:73); vote cost `?` (:78); Battle Brothers daily wage scale and roster cap unestablished (:213).

### research/game_precedent_suite/tutorials/T03_colony_a.md
- **What it is:** tutorial pass on Dwarf Fortress (Steam 53.16), RimWorld (1.6) and Songs of Syx (V71 early access); 2026-10-22.
- **Status:** no Status line. Reading: reference; the DF and RimWorld rows carry verified need/mood numbers.
- **Bears on:** SE, CHAR, WR (storyteller/pressure), CORE.
- **Content that matters:**
  - DF: the player never commands a dwarf in Fortress mode; dwarves pick jobs from permitted labors, personal needs pre-empt fortress jobs; nobles gate by population and wealth (mandate caps 1/1/2/3/5 for baron/mayor/count/duke/monarch); invader size is set by population and wealth triggers (:24, :69-72). Values -50..+50 in 7 levels, 33 values; needs refresh to 400; focus formula (:87).
  - DF mandate/demand rule: a mandate to make an item within 3-6 months or the noble is unhappy and a dwarf is punished; a demand (furniture) has no punishment (:70). DF difficulty Enemies Off/Normal/Hard, economy Hard = 5x wealth for ranks (:17).
  - RimWorld raid-points formula: (wealth points + pawn points) x threat scale x start factor (0.7 until day 10) x adaptation (0.4-1.47); min 35, max 10,000; wealth points 0 at 14k, 2,400 at 400k; free colonist worth 15 points to 10k wealth (:159). Storyteller Cassandra 4.6-day on / 6-day off cycles (:159). Mood: base mood 42/42/37/32/27/22 by difficulty; breaks at mood under 35/20/5% of threshold with mean times 4/0.8/0.5 days (:102, :116).
  - RimWorld Royalty: Honor buys titles which demand throne rooms/apparel and unlock permits; Ideology: memes, precepts, rituals, roles (:162-163). Colony End when all colonists dead or gone; five story endings (:166).
  - Songs of Syx: six game modes, raider groups pre-spawned with only those near the player's wealth "rung" taking interest, raiders locked below pop 200, riots at 70% loyalty, battles up to 50,000 units with a Quick Battle option (:189, :200, :239). Wiki says "no fail state" (:244).
- **Conflicts / stale:** attachment claim "mean time to break major 3 days / extreme 0.7" is WRONG (0.8 and 0.5 days) (:176); DF immigration wave size CONTESTED 1-10 vs 5-15 (:64, :90); attachment "mandate-issuing nobles ~ anonymous citizens + capped delegates" judged "partly right, mostly not" (:88). Songs of Syx data rides small-model WebFetch summaries, official wiki HTTP 500 (:183).
- **Open items:** DF surrender mechanic stale in v2 cell F8 (:90); RimWorld early-game raid size in 1.6 not read (:179).

### research/game_precedent_suite/tutorials/T04_colony_b.md
- **What it is:** v3 tutorial pass on Manor Lords (Update 8), Frostpunk (1.6.2), Frostpunk 2 (1.6.1) and Banished (1.0.7); 2026-10-22.
- **Status:** no Status line. Reading: reference; carries the repo's own corrections to its Manor Lords / Banished claims.
- **Bears on:** SE, FA, CHAR, WR.
- **Content that matters:**
  - Manor Lords: approval from needs (food variety by category, clothing, church, tavern, housing) sets monthly family arrival/leave tiers (7 tiers, migration -3..+3, only if living space exists); tiers pay Influence (Admired +10, Revered +20); settlement level counts families by plot level; Duel and Fractured Realm modes; "no auto-resolve found" (:20, :60, :76, :83).
  - Frostpunk: laws as a book with exclusion pairs (Soup/Food Additives, Child Shelters/Child Labour), Hope and Discontent as two bars, Faith vs Order Purpose chosen once late; scouting is the only way to grow the workforce (:115-116, :140, :147).
  - Frostpunk 2: council of 100 seats, 51 majority, two-thirds for power-granting laws, 10-week cooldown after a law passes or fails, promises bought votes, "Guided Voting" forces laws at faction-relation cost, heat per district (:164-178, :211).
  - Banished: no money, housing vacancy gates births ("a household will only conceive a few children before stopping"), 5 ages per year, labouring age 10, school until 17, cohort die-off lore is community lore not sourced; players report lifespans into the 80s-90s, contradicting an attachment's "max 75" (:280, :285-288).
  - Repo claim checks: "AI settlements added during 2026 ... community says cheat" is WRONG on date (Update 5, 19 Dec 2025) and cheat unsupported; "2.5 million copies" stale (4 million) (:86-87).
- **Conflicts / stale:** immigration thresholds in the attachment true of 2024 only (:83); Frostpunk 2 pre-1.3 heat numbers replaced by district heat levels (:212).
- **Open items:** births/ageing of Manor Lords family members unestablished (:78); Frostpunk start population and storm day unestablished (:149).

### research/game_precedent_suite/tutorials/T14_squad_settlement.md
- **What it is:** v3 tutorial pass (2026-10-22) on Jagged Alliance 2 (+1.13, JA3 note), Medieval Dynasty, Dawn of Man, The Guild 2 and The Guild 3, with capability-id lines and checks of attachment/repo claims.
- **Status:** no Status line. Reading: reference. JA2 is the named-mercenary-squad plus militia-garrison precedent (Ogre Battle / Unicorn Overlord shape on the strategic layer); The Guild 2/3 carry the evidence-and-trial precedent for SC.
- **Bears on:** MB, CHAR, SE, SC, FA, FI.
- **Content that matters:**
  - JA2 1.13: real-time strategic map with pause, turn-based tactical on contact; pre-battle box offers Auto-resolve / Enter sector / Retreat; militia-only defences may be auto-resolved; retreat -5 morale, abandoned militia up to -7.5 loyalty everywhere (:18, :22, :35). Named mercs with contracts (1 day / 1 week / 2 weeks), salary +25% per experience level, buddy/hated lists; hated-colleague tolerance clock makes a merc refuse renewal or quit (:31-32, :63).
  - JA2 morale = default 50 + team + tactical + strategic + campaign-progress bonus (to +20) + drug/alcohol + Walkman (+20%): "five or seven layers by how you count", no single "five" in source; pairwise opinion matrix -25..+25 in MercOpinions.xml with a dynamic layer added by 1.13 (:76-77). MeLoDY audit tool itemises opinions by source (:78).
  - JA2 militia: green/regular/elite, $750 per training session of up to 10 ($75/head), trainer Leadership >= 20, town loyalty >= 20%; unpaid militia desert, upkeep $10/$20/$30 per midnight; Queen AI takes one decision per interval (8 h Novice down to 90 min Insane) and attacks a taken sector once a grace period ends; enemy gear improves with hidden "progress" (:20-21, :33, :59). No game-over on a team wipe: captured mercs go to prisons and can be rescued (:61).
  - The Guild 2 trial: evidence has a time-to-live ("6 rounds or year", unit ambiguous), strength x believability weighting, at most 3 evidences checked, Rhetoric vs Empathy shifts, slander via the town crier makes one evidence and propagates it to 10 neutral NPCs, judge plus two assessors; you must be present for your own trial or lose by default (:221, :261-262). The Guild 3: verdict scale not guilty / low fine / public shame / high fine / prison / death; offices are a four-tier tree, one must hold the office below to apply; "find or falsify evidence" is an action (:290, :305).
  - Medieval Dynasty: mood -100..+100 scales production/trading/repair +-20%, job-skill match +2% per skill point to +20%; Dynasty Reputation as the gate on population (price rises per head); -10,000 banishes (:134-135, :143-144). Dawn of Man: work areas painted with worker caps, production targets as % of population, era advance triggers extinctions and harder raiders (:158, :171).
  - Capability-id lines (B/C/D/F/L ids) per game give a compact feature matrix: e.g. JA2 B6 YES morale/opinion, F4/F5 YES tactical, C7 YES garrisons, B7 NO succession; Guild 2 D6 YES trials, D5 YES elections (:67, :257).
- **Conflicts / stale:** JA2 attachment claims judged wrong or stale: "towns yield daily tax" NOT FOUND (income is mines scaled by loyalty x share held), "Mobile Militia that patrol" removed 2018, roster 32 now 40 (:69-73); repo claim "docks town loyalty after three days of no offensive action" half NOT FOUND (:79). The Guild 3 "EHE disabled by publisher" unverified (:314).
- **Open items:** JA3 not played; Guild 3 loss rule unstated (:307); Medieval Dynasty reputation breakpoints outdated (:143).

### research/game_precedent_suite/tutorials/T13_koei.md
- **What it is:** v3 tutorial pass (2026-10-22) on Koei Tecmo and Black Sea strategy: Romance of the Three Kingdoms (VIII Remake, XI, XIII, XIV), Nobunaga's Ambition (SoI/Ascension/Taishi), Genghis Khan II, Knights of Honor II; plus checks of 13G/20G attachment claims and repo claims.
- **Status:** no Status line. Reading: reference; the officer-game shapes behind "officer mode" (`player_agency_v30`) and the troop-stock/personnel work.
- **Bears on:** FA, CHAR, MB, CORE, SE.
- **Content that matters:**
  - RTK VIII-R: the officer you pick fixes status (ruler/viceroy/governor/common officer...) and therefore which commands you hold; quarterly Parliament (Jan/Apr/Jul/Oct) spends Strategy Points; monthly city turns spend Action Points; mission quota 200% commended, under 20% reprimanded; public order below 50 = unrest, below 25 = revolt and conscription unavailable (verified, the repo's "order<25 blocks conscription") (:15, :21, :51, :83).
  - RTK XIV: Orders renewed each turn from areas held; Advancement runs 10 days during which orders cannot be changed; units fight automatically on contact with standing orders (enemy contact, retreat when supply cut); duels auto-resolve; suggestions always succeed on Beginner (:20, :49, :73). Area Overseers by stat (LEA order, STR barracks, INT commerce, POL agriculture, CHA conquering) (:78).
  - RTK XI: Action Points max 255 refilled per 10-day turn, delegation to Viceroy districts; sworn siblings/spouses cannot be poached but "may be able to recruit them" at Loyalty 100, so not a ban on defection (:18, :81). XIII: Rank 7 minister, 5 governor, 2 viceroy generate order slots (:19, :54).
  - Nobunaga Taishi: Daimyo "Resolve" (two traits, up to four effects each, effect 4 a malus) gates which policies exist, resettable on Retire; quarterly council approves up to 3 ideas giving "policy power"; popularity feeds revolts; Ascension: merit accrues a "voice" resource spent on proposals to the daimyo (:99, :123, :148-150).
  - Genghis Khan II: every command costs Body Points refilled each season (pool varies by person and falls with age; Politics letter changes cost not pool); vassal states commanded only by Decree and orders "will not necessarily be carried out"; kin governors never betray; no loyalty meter, only Popular Support 0-200 and Charm (:167-168, :218-220). Battle: 5 Legions of up to 4 Units, 30-day cap, auto or watch (:170).
  - Knights of Honor II: 9 seats (king + 8 knights) with class-gated verbs; a governed province yields about 10x an ungoverned one (repo-style "10% penalty" claim refuted in size); auto-calc of battles gives "lots of losses" when outnumbered; out-of-supply -30% speed, -12 morale (:250-251, :262, :282, :298).
- **Conflicts / stale:** repo claims "eight domestic commands each keyed to four stats, flat 10 gold" and "LOY recruiter tell <=70" NOT FOUND in VIII-R/XIV/XI manuals (:83); "RTK XIV: 141 Individualities" supported as a trait-entry count (:77). 13G claim that Genghis Khan "Politics grade sets commands per season" conflates cost and pool (:218). Scenario-1 deadline 1214 (manual) vs 1212 (Wikipedia) (:222).
- **Open items:** XIII loop details, SoI/Ascension monthly order list (OCR-garbled manuals), KoH2 Normal difficulty and auto-calc formula (:153, :301).

### research/by_lane/MB_mass_battle.md  (read lines 268-757 in full; lines 1-267 were covered by DG_research1; lines 548-657 and 755-811 skimmed by heading only)
- **What it is:** MB lane critical evaluation (2026-10-16, HEAD 5445e34): historical research, game precedent and repo work joined to code, with a field probe run by the author; sections 4 (join table), 5 (gaps), 7 (19 throughlines), 8 (missing areas), 9 (NERS pass), 10 (12 recommendations K-MB-1..12).
- **Status:** `FILED — reference, not canon … a critical evaluation; resolves nothing at runtime`. Reading: historical as of 2026-10-16 (code line numbers will have drifted); the design-intent claims and the probe are the durable part.
- **Bears on:** MB, CORE, SE, FA, PC, CHAR.
- **Content that matters:**
  - Season-path scale gap: the season builds one Line subunit per side from summed `Person.weight` (`massbattle.py:213-230`), largest realm side weight 6; the engine's rout floor is 80 troops (`config.py:117`), so an opposed march is always Lost. Probe (5 seeds per cell): 6v2, 11v1, 79v1, 80v80 attacker wins 0/5 with both sides routed; 100v100 1/5; 120v60 5/5; 1000v500 4/5; `attacker_wins = (not unit_a.routed) and ...` grades mutual rout as defender win (:335-344, :367).
  - The composite army Jordan wants (army -> unit -> subformation -> troop type) is already built on the harness side: `build_army` (`systems/mass_battle/sim/engine.py:213-453`), `Subunit.of_type`, `unit_type_for` (weapon decides melee/ranged, ED-MB-0001), `run_multi_unit_battle`; the season uses a one-Line stub ("minimum-viable defaults") and `modules/mass_battle/` imports nothing from `systems/` so it cannot call the constructor (T-MB-19, M-MB-2) (:368, :435).
  - Equipment: `TROOP_LOADOUT` wires weapon to melee/ranged in every harness build; armour, speed, lethality stay "NOT YET WIRED into resolution" per `equipment/__init__.py:10`; `Unit.officers` is "bookkeeping only"; only 9 of 16 role keywords drive a primitive (:287, :351, :383). Nothing in the list shows a per-unit mixed-weapon loadout with fatigue/speed cost (no row for it).
  - Jordan 2026-10-16 statements: troops are "levied from settlements as their own resource" and "levy typically doesn't refer to goods/stores"; v9's IN-52 design rejects "Converting stores into troops. That mints persons" (:280, :354, :384, :448). K-MB-1 proposes a levied troop stock per rung; K-MB-2 routes season sides through `build_army`; K-MB-4 lets the faction choose its order of battle (:705-707, :715-723).
  - Precedent verdicts: one engine headless for every fidelity (Football Manager, XCOM; Total War failure) SOUND but "necessary not sufficient" at an input domain no harness visits; Dominions rule "Command=0 -> instant rout" contradicts the repo's own "fraction, never flat" rule (`orchestration.py:2221`); garrison-as-assignment is degenerate at realm scale (:352-356, :377-382). Squad engagement names nine games and surveys none (`squad-engagement` precedent named not evidenced) (:287, :365).
  - Rout band 15-30% is a recorded Jordan design value (ED-MB-0031) credited to du Picq who gives no figure; `SUBUNIT_ROUT_FLOOR` pre-empts the stochastic band below ~94-114 troops (:273, :366, :521). Four false N-lines at shipped scale (engine, garrison, morale-start, survivor degree), three revive when a scale is ruled (:531).
  - Missing areas M-MB-1..17 incl. no commander, no experience axis, no mass->personal yield (duel handoff), no odds display, `at_war` has 0 production callers, death in battle emits no `person.died` (H-152) (:434-451).
- **Conflicts / stale:** code locators dated (HEAD 5445e34); MB-08 LEAVE falsifier; `requirements.yaml:116-118` vs `:1124-1125` read "reached" differently (:378). Author notes the audit's "equipment unread" claim is wrong for the harness (:383).
- **Open items:** men-per-weight scale and the new name for the store-extraction act are "Jordan's" (:715); a played fidelity (player commands the field) left undecided (:723); naval, steppe/non-Western formations not covered (:297-298).

### research/by_lane/FI_fieldwork_investigation.md  (read lines 255-395 and 473-522; lines 1-254 covered by DG_research1; 396-472 and 523-535 not opened)
- **What it is:** FI lane critical evaluation (2026-10-16): throughlines T-FI-1..10, missing areas M-FI-1..7, NERS pass, recommendations K-FI-1..11, built on the detective/noir precedent (Pentiment, Obra Dinn, L.A. Noire, Shadows of Doubt, Heaven's Vault, Her Story-style) and tested against the season loop.
- **Status:** `FILED — reference, not canon … resolves nothing at runtime`. Reading: historical (code locators of 2026-10-16) but the central finding is concrete and checkable.
- **Bears on:** FI, SC, CHAR, WR, CORE, GO.
- **Content that matters:**
  - Central finding: the six inquiry verbs (`research`, `examine`, `surveil`, `interview`, `reconstruct`, `thread_read`) all declare `writes: []`; no `_eff_` function; a finding is a content-free `finding.made` event-kind claim valued `True` (`witness.py:166-172`), so an investigator learns that a thing exists and that he stood there, never what a record says (M-FI-1) (:278, :288, :373).
  - The one content-bearing finding the loop makes is a commissioned faction sheet (`survey`, `effects_information.py:421-484`) plus WITNESS's content deposit for anyone a `hold` newly reaches (`witness.py:398-421, :682-710`); `research` opens no `hold`, so the deposit never reaches an investigator reading a Record without taking it (:278, :288).
  - Evidence as a typed object: corroboration groups claims on `(predicate, value)` (`person_q.py:556-568`) and only `belief_contradicts` weighs with it; `dissents` scores no `content:` claim (`decision/options.py:1165-1167`); `proofs` roster is BUILT but read only by the arrangements loader's validation, production reader is SC-08 (:259, :320). No inquiry producer feeds proceedings as evidence (:360).
  - Forgery/concealment: `Record.forgery_quality` (`carriers.py:752`) is built and unread (a planted forged sheet reads exactly like a true one); `forge` and `conceal` planned at IN-45/IN-12; `destroy_record` is built but dark (H-75); no concealer's score sets an inquiry's obstacle (M-FI-4) (:289, :291, :325-326). Honest misreading absent: refraction moves confidence only, no deposit holds a deed claim False (H-198) (:289).
  - Competence absent: H-200 "competence HAS NO CARRIER ... the factor is 1"; WITNESS refracts only deposits where `actor != pid` (`witness.py:495`), and the actor's own reading of his act (AX-7 layer 2) is unbuilt; so who you send to look is not a choice (M-FI-3, K-FI-1) (:290, :491).
  - Q5 "only through consequence" needs the consequence path legible; the person-side read `view_ids(..., "question_relevant")` exists but no surface renders it (M-FI-5, K-FI-11); `interview` yields no testimony beyond the questioned person's own later `tell` (M-FI-6, K-FI-3); `examine` strictly dominated by "do something else while there" (:292-293, :390).
  - Recommendations: K-FI-6 (give `research` a yield on the existing content deposit), K-FI-7 (a low-band inquiry confidently wrong), K-FI-8 (a refused inquiry stays witnessable), K-FI-5 (concealer's score as obstacle, score/2 for oppositional obstacles per Jordan 2026-08-18), K-FI-9 (FI-02 role only with a provider) (:481-485, :508-511).
- **Conflicts / stale:** plan holds two readings of investigation's seam ("not a seam" v8 line vs Jordan's "not a contest seam. it is its own thing"); FI-01 SKIP arm contradicts S-6's falsifier; uploaded audit A8 miscounts `survey` among six verbs (:262-263, :300). Most Records carry no `subject_matter` (112 of 120 in one seed) (:508).
- **Open items:** Jordan rulings: K-FI-1 competence form (person field vs capability key), K-FI-7, K-FI-8; Sites/Rungs have no content field the deposit could copy (:491, :508).

### research/by_lane/PC_personal_combat.md  (read lines 310-356 and 507-555; lines 1-307 covered by DG_research1; remainder not opened)
- **What it is:** PC lane critical evaluation (2026-10-16): missing areas M-PC-1..12, NERS pass, recommendations K-PC-1..12, with two author probes (`pc_actor_probe.py`, `pc_cohort_probe.py`).
- **Status:** `FILED — reference, not canon … resolves nothing at runtime`. Reading: historical locators; the findings bear directly on Jordan's personal-combat intent.
- **Bears on:** PC, CHAR, MB, CORE, GO.
- **Content that matters:**
  - Per-person inputs absent: `Person` has no attribute or kit field (`carriers.py:645-696`); `verb_capability` maps only `tell`/`speak`; every season fighter has class-default `history` 3 (`combatant.py:94`); "A duke and a copyist fight identically, and 53 weapons, 4 armour tiers and 7 traditions decide nothing in play" (M-PC-1); two equipment models exist (`modules/combat/weapons.py`, `modules/mass_battle/equipment/`, the latter "NOT YET WIRED") (:326, :353).
  - Spectator engine: the season calls the SIM harness `fight()` (`fight.py:52`), while `wrapper.py:504` says "the GAME calls one engagement per turn"; no in-fight decision, no grid ("GRID-BASED MAP COMBAT ... DOES NOT EXIST ANYWHERE", `requirements.yaml:149`); K-PC-4 would fight a played person's fight one engagement per act with pause between (:329, :537). IN-46 has "no build batch" (:329).
  - Actor outcome: only the subject's wound is written; probe of 400 seeded fights: actor felled with subject standing 205/400, actor wounded only 90/400; a felled starter yields `contest.undecided` (false report) (M-PC-2, K-PC-2) (:327, :530).
  - Scenes with more than two people absent (`fight.py:43` unpacks two); a design exists only in quarantine (scene_combat_design_v1 "wrap `engagement()`, never fork it"); K-PC-5 proposes one outer loop over `engagement()` for N-party fights and duels inside fields (:328, :538). Mass->personal yield point absent (M-PC-5).
  - Cohort at the combat seam: `fight`/`accept` admit any living Person including cohorts at weight>1; one `Felled` band can delete a whole cohort; seed 0 resolved an `accept` whose subject is a cohort (1 of 63 acts, seeds 0-4) (M-PC-12, K-PC-12) (:334, :531).
  - Duel roll is a continuous Normal with a logistic side-channel while the season and contests draw discrete dice (M-PC-7, K-PC-8); no game-path odds reader (`p_success` 0 hits) (:331-332). Duel terms/challenge Record planned (PC-10a/b), co-location IN-59 (:348-349).
- **Conflicts / stale:** code line numbers dated; `test_season_shape.py:13727-13733` would be re-pinned by K-PC-2 (:530).
- **Open items:** decision set for in-fight play (J-15 ask-then), standing actor's wounds, how a cohort fights at weight: all Jordan's (:554).

### research/game_precedent_suite/tutorials/T17_repo_strategy_a.md  (read lines 1-4 and 64-177: Dominions and Heroes of Might and Magic; the EU4 section 6-63 not opened)
- **What it is:** tutorial pass (2026-10-22) on Europa Universalis IV, Dominions 5/6 and Heroes of Might and Magic III/V/VII, with checks of repo claims.
- **Status:** no Status line. Reading: reference; the Dominions rout check and HoMM accrual check correct repo claims in `research/valoria_game_precedent_companion_v1_part5.md`.
- **Bears on:** MB, FA, SE, CHAR.
- **Content that matters:**
  - Dominions: battles are never played live; the engine runs them from Army Setup (squad placement, formation, battle orders) plus mage spell scripts, then a replay is viewed next turn (an auto-resolve-with-pre-set-orders shape, the Ogre Battle / Unicorn Overlord "orders set in advance" pattern); simultaneous turns, ~45-step resolution order, battles in random order (:78-80, :122).
  - Repo claim "Dominions commander-anchored rout, scale-blind" PARTLY CONFIRMED: troops without an unrouted leader of the appropriate type rout or dissolve, so sniping leaders removes armies; but it is per leadership type, a commander leads only as many troops as his Leadership value, and most routs are not commander-based (squad morale, army HP below 50%, auto-rout at 25% HP left D6 / 75% lost D5) (:122). Bears directly on the repo's "Command=0 -> instant rout" rule.
  - Dominions pretender-design: 450 design points minus chassis, scales of +-40 points per click, 9 magic paths (D6); commander Leadership >=40, >=80 unlocks line formations (:70-73, :105).
  - HoMM III: hex grid 11x15, creatures act by speed, morale -3..+3, hero casts one spell per round; town dwellings accrue cumulatively but map dwellings cap at weekly growth in vanilla (repo's "accrual in a place whether you visit or not" CONFIRMED for town dwellings, WRONG for map dwellings in vanilla); Halls pay 500/1000/2000/4000 per day; defeat = no town for seven days (:136, :176).
- **Conflicts / stale:** D5 vs D6 build prices and bless rules differ (:110); HoMM V and VII mostly [M]; Dominions manual unread (:65).
- **Open items:** D5 equivalent of army-HP turn-rout `?`; HoMM V/VII accumulation `?` (:122, :176).

### research/game_precedent_suite/tutorials/T18_repo_strategy_b.md  (read lines 1-4 and 153-283: XCOM and Brigandine; Shadow Empire and Stellaris sections 6-152 not opened)
- **What it is:** tutorial pass (2026-10-22) on Shadow Empire, Stellaris, XCOM (EU, XCOM 2) and Brigandine: The Legend of Runersia, with repo-claim checks.
- **Status:** no Status line. Reading: reference. Brigandine is the squad-on-a-grid, monsters-in-a-knight's-troop, season-phased campaign precedent (an Ogre Battle / Unicorn Overlord sibling).
- **Bears on:** MB, FA, SE, CHAR, DICE.
- **Content that matters:**
  - Brigandine: a "troop" is a knight plus up to 6 monsters, total Magic Cost <= the knight's Magic Pool, monsters stay within a Command Range of the knight; up to 3 troops a side on a hex map; attacker has 12 turns to beat every defending knight; a ruler's fall sends all that nation's knights home; undefended base is occupied unfought; empty-or-stacked base is the implicit garrison choice; Auto Mode battles (:233-235, :241-245, :252).
  - Brigandine campaign layer: each season = Organization Phase + Attack Phase with all nations' moves revealed together; mana income vs monster upkeep (reserve short -> all monsters start battles at 70% HP/MP); difficulty fixed per campaign and sets season limit (Normal 120 seasons, Hard 60) (:227, :231-236).
  - Repo claim "Brigandine garrisons are a precedent" (companion X5 "garrison is an assignment, never a unit type") PARTLY HOLDS: there is no garrison unit type, but the game names no garrison role and "Guard Castle Hex" is a CPU battle-AI option; "units lost wholesale if the territory falls" is WRONG (knights retreat, only abandoned monsters are captured) (:282).
  - XCOM hidden aim assist VERIFIED: lower difficulties flip misses to hits after a miss streak (Rookie x1.2, +10/miss; Veteran x1.1; Commander +15/miss; Legend none; threshold 50, cap 95) and alien hits to misses; displayed percentage is not what the dice use (:208-212). Relevant to any "show odds" decision in DICE/PC.
  - XCOM: concealed pod-patrol missions, Avatar Project doom meter as a clock, Dark Events, soldier permadeath (:165-170, :201).
- **Conflicts / stale:** Brigandine win rule CONTESTED (beat every knight in 12 turns vs occupy castle by last turn); who picks the defending three unknown (:281).
- **Open items:** Easy-mode CPU behaviour may describe only the demo (:281).

### research/game_precedent_suite/tutorials/T08_sanity_a.md, T09_sanity_b.md, T10_npc_economy.md, T11_policy_sims.md, T12_paradox_classical.md, T15_pressure_political.md  (head and section index only: first ~4 lines of each plus the `facts line` headings; bodies NOT read — see the closing `[PARTIAL]` note)
- **What they are:** same-format v3 tutorial passes (2026-10-22). T08: Darkest Dungeon II, Sunless Sea, Eternal Darkness. T09: Don't Starve, Pathologic 2, Vampire: Bloodlines. T10: The Sims 4, Anno 1800, Patrician IV, Wildermyth. T11: Tropico 6, Suzerain, Dragon Age: Inquisition (war table), Democracy 4. T12: Crusader Kings II, Imperator: Rome, Total War: Rome II (Emperor + Power & Politics), Oriental Empires. T15: Against the Storm, Pax Pamir 2e, Empires in Arms, Shadow of Mordor/War (Nemesis system).
- **Status:** no Status line. Reading: reference, same provenance rules as T01-T04.
- **Bears on:** T08/T09 WR, CHAR, SE (stress, sanity, survival clocks); T10 SE, CHAR, NPC economy; T11 FA, SC (policy/court/council); T12 FA, MB (Total War Rome II is the nearest Total War precedent in this list); T15 FA, WR, CHAR (Nemesis persistent-encounter log; Empires in Arms is a corps/strategic-war precedent).
- **Content that matters:** [PARTIAL] for five of six files: only the game rosters and headings were established, and no per-game claim from T08, T09, T10, T11, T15 is reported (the Nemesis system, T15 lines 189-262, is unread). T12 lines 178-259 (Total War: Rome II) were read in full:
  - Rome II loop: one turn per season, action points per character, battle choice per contact = fight on the 3D battlefield, auto-resolve "by comparing unit statistics", or withdraw; units muster directly to a general, upkeep deducted at the start of the next turn (T12:190-195, :207). Politics: party influence from gravitas, loyalty per party, secession protection for the first 20 turns, civil war takes regions at once (T12:227, :237); difficulty shifts party loyalty (+10 Easy to -25 Legendary) (T12:186).
  - Rome II repo-claim checks: "province owned only when every region held" PARTLY (edicts require the whole province); "Entice: >=30 gravitas, -8 loyalty" NOT FOUND in any source read; "Rome II's ambition is a multiplier called cosmetic" CONFIRMED as a multiplier on gravitas, not cosmetic (T12:251-255).
- **Conflicts / stale:** none checked.
- **Open items:** none checked.

### research/by_lane/00_COMPARATIVE_ANALYSIS.md  (read lines 1-120 only: C0 verdict, C1 matrix, C2 root causes, C3(a) dependencies; C3(b)-C9 not opened)
- **What it is:** IN-lane cross-cutting join (2026-10-16, HEAD bd8105b) of the ten lane evaluations: verdict, lane matrix, 11 shared root causes RC-1..11, dependency map D-1..18, adjudication, a register of missing areas and of Jordan's decisions (J-C-n).
- **Status:** `FILED — reference, not canon … resolves nothing at runtime … no recommendation here enters a plan or ledger until Jordan so rules`. Reading: historical (dated) but the best single map of cross-lane dependencies.
- **Bears on:** CORE, MB, PC, SC, FI, FA, SE, CHAR, WR, GO, DICE.
- **Content that matters:**
  - Verdict: the ten lanes describe one absence: the season loop resolves acts by persons who differ in what they want but not in what they hold, can do or know, so every scale seam is fed a default (:26-29). Ranked interactions: 1 troop chain, 2 per-person capacity source, 3 acts that carry no content, 4 no player surface/pause (IN-46/47 "no build batch"; R-04 therefore M1 cannot read `met`), 5 population that only shrinks (:31-37).
  - Lane matrix counts: MB 17 missing / 5 hollow-blocked / 11 planned-dark; SC 9/9/17; PC 9/3/8; SE 8/5/19; FA 5/6/18; NPC 12/10/14; WR 8/6/8; FI 7/7/15; IN 14/10/30; GO 10/4/9; totals 99/65/149 (:52-62). "The ranking inverts code maturity: MB and SC hold the most cited evidence and the deepest built modules and deliver least of it to the season" (:64).
  - RC-1: no ruled per-person capacity source (`Person.capability` empty on 429 of 430 persons; combat builds `Combatant(a_id, end=a_end)` only); carrier disagreement between new `Person.attributes` (Jordan's "it will be 10 attributes", ED-IN-0185 Q7) and capability derived at read (:34, :78). RC-2: no troop stock, three forms proposed (rung stock coupled to cohort weight / uncoupled `matter_kinds` row / troops as people), choice left to Jordan (J-C-2) (:79).
  - RC-4 acts carry no content (FI six verbs; every computed `utter` mints an OUGHT so war is never uttered); RC-9 combat draws a continuous Normal with logistic side-channel while season/contest/field use discrete dice; RC-10 `content_hash` folds `repr()` and floats and draws use CPython `random.Random` where Layer 1 wants an integer-domain hash (GO parity) (:81, :86-87).
  - Dependencies: composite army needs troop stock (D-1); `march` requiring war needs a war-mood source (D-7, D-8); competence needs RC-1 and, for an inquiry, AX-7 layer 2 (D-10); a played fight and a battle yielding to a duel extend IN-46's one call-out (D-17) (:103-119).
- **Conflicts / stale:** counts and locators as of 2026-10-16; decision list J-C-1..12 not opened here.
- **Open items:** J-C-2 (form of the troop stock), J-C-12 (what odds/derivations may be shown), X-14/X-16 adjudications at C4 not read.

### research/by_lane/FA_faction_actions.md  (read §0 verdict lines 10-24 and §10.0 lines 549-557 only; the remaining ~600 lines not opened)
- **What it is:** FA lane critical evaluation (2026-10-16): governance research, game precedent, repo work, missing areas M-FA, recommendations K-FA.
- **Status:** `FILED — reference, not canon`. Reading: historical.
- **Bears on:** FA, MB, SE, SC, CHAR, WR.
- **Content that matters:**
  - FA code that runs is grounded in Layer 1 and Jordan's rulings, not the lane's research; no v9 FA position cites any research document; research hooks are all in the retired Key/Directive/Need idiom (:10-14 of verdict items 1, 2, 4).
  - Archived FA corpus self-contradictory: 79 and 67 contradictions across 33 governance documents; victory, seizure, treaty lapse, Coup Counter, Standing range each have 2-6 versions (verdict item 3).
  - Strategic layer partial: `faction_q.head()` returns `None` in every built world, no computed act declares war or treaty, `levy` refused in the corpus run, no ending (H-176); treaty and war representable via existing verbs but nothing authors them; `covenant` unbuilt (verdict items 5, 7).
  - Top five: K-FA-13 faction raises troops from settlements and assembles its army from chosen subunits; K-FA-1 war can be declared, joined, ended (blocked by `attention_key` own-echo ranking); K-FA-6 one ending; K-FA-2 a treaty something reads; K-FA-9 a visible faction (:549-557).
- **Conflicts / stale:** `HANDOFF_FA.md` row 3 orders authoring into a quarantined file (verdict item 9). H-100 quotes a research generalisation in tension with its source (item 8).
- **Open items:** K-FA-11 early dismissal is Jordan's.

### research/by_lane/NPC_npc_cast.md  (read §10.0 lines 676-686 only; 770+ lines not opened)
- **What it is:** NPC lane critical evaluation (2026-10-16).
- **Status:** `FILED — reference, not canon` (assumed same header as siblings; line 3 not re-read). Reading: historical.
- **Bears on:** CHAR, FA, WR, SC, MB.
- **Content that matters:**
  - Top five: K-NPC-1 persons differ in wants only so every contest, duel, witness reading and field army resolves alike by person; K-NPC-4 a faction's creed names its head as a man and four of six heads die in one season at seed 0 (probe), so a regicide leaves members answering to a corpse; K-NPC-3 vacancy reaches only conferrers' questions (`confer` does not yet execute); K-NPC-2 nobody's values or body change over a campaign (mechanisms exist, ship off); K-NPC-11 none of this is visible to a player (:676-686).
  - Cross-lane NERS line quoted in 00_COMPARATIVE: "small because capacity and change were amputated".
- **Conflicts / stale:** none checked. **Open items:** none read.

### research/by_lane/SE_settlements_territory_economy.md  (read §10.0 lines 475-485 only)
- **What it is:** SE lane critical evaluation (2026-10-16).
- **Status:** `FILED — reference, not canon` (not re-read). Reading: historical.
- **Bears on:** SE, MB, FA, WR.
- **Content that matters:**
  - Top five: K-SE-13 a settlement's people are never its army (no troop stock, no levy that raises units, no quality by equipment/experience/commander); K-SE-1 a settlement's population cannot change (probe 74 -> 74 in every arm); K-SE-2 nobody can know who holds a place; K-SE-4 with K-SE-3 settlements have no neighbour and cannot trade with each other; K-SE-5 the verb `levy` is a stores extraction Jordan rules misnamed (:475-485).
  - K-SE-7 (silent chronic dearth, H-160 limit 3) was ruled a balance number by Jordan 2026-10-12 (:483).
- **Conflicts / stale:** none checked. **Open items:** none read.

### research/by_lane/WR_world.md  (read §10.0 lines 520-530 only)
- **What it is:** WR lane critical evaluation (2026-10-16).
- **Status:** `FILED — reference, not canon` (not re-read). Reading: historical.
- **Bears on:** WR, CORE, CHAR, GO.
- **Content that matters:**
  - Top five: K-WR-2 build thread operations as persons' acts (the lane's physics never enters play); K-WR-4 drive the Calamity from what persons do with threads (IN-35 HOLLOW); K-WR-5 give the crossing a consequence (P-15); K-WR-9 author ages and turn the world's forcing on (ageing on today would age everyone from 0); K-WR-11 build IN-47's chronicling space on S-2's per-person projection (:520-530).
- **Conflicts / stale:** none checked. **Open items:** none read.

### research/by_lane/IN_infrastructure.md  (read §10.0 lines 969-982 only)
- **What it is:** IN lane critical evaluation (2026-10-16), the longest lane file (1118 lines).
- **Status:** `FILED — reference, not canon` (not re-read). Reading: historical.
- **Bears on:** CORE, MB, PC, GO, SC, FI, WR.
- **Content that matters:**
  - Top five: K-IN-1 rule one source for per-person capacities every resolver reads; K-IN-13 make `levy` raise troops into a settlement's own stock and build the season's army from those stocks as composite subunits, rename the stores act; K-IN-10 put IN-46/47 builds in a batch (without it M1 cannot be met under v9); K-IN-6 let a battle pause for a person's act inside it; K-IN-9 rule what the player is shown (AX-7 gloss vs §C.11), then build `explain` (:969-982).
  - `confer` already executes (IN-53); what remains for `revoke` is a motive, under Jordan's H-207 ruling (:982).
- **Conflicts / stale:** none checked. **Open items:** none read.

### research/pre_firearms_formations/00_MANIFEST.md
- **What it is:** project manifest (2026-05-14) for the pre-firearms formations research: four tasks (catalogue, strategy, matchup, battle-phase choreography), vocabulary per Jordan (grand formation, unit formation, unit, strategy, tactic), chunk plan A-F, per-formation entry template.
- **Status:** `[2026-05-14] Manifest created. Chunk A in progress.` Reading: historical and stale (its chunk plan names `09_throughlines.md`; the tree has 09-16 with different names).
- **Bears on:** MB.
- **Content that matters:**
  - Vocabulary: grand formation = an army's spatial organisation, movement and strategies; unit formation = a sub-grouping with a specific role; unit = troops comprising a sub-formation (:12-18). Matches the army -> unit -> subformation -> troops nesting Jordan describes.
  - Per-formation template: name, era, composition, geometry (frontage, depth, intervals, alignment), equipment dependency, tactical role, strategic context, vulnerabilities, notable engagements (:36-46).
  - Weight: Renaissance Europe (E1) and Islamic/steppe (E2) at MAX (:28-29). Working discipline: "no commits, no repo writes; pure research" (:54).
- **Conflicts / stale:** chunk plan does not list files 10-16. **Open items:** none.

### research/pre_firearms_formations/01_ancient.md, 02_classical.md, 03_early_medieval.md, 04_high_medieval.md, 05_late_med_renaissance_europe.md, 06_renaissance_islamic_steppe.md, 07_renaissance_east_asia.md, 08_pre_columbian.md  (HEADINGS ONLY: bodies not read; 8 files, 2,880 lines)
- **What they are:** the formation catalogue (Task 1), chunks A-E4, each formation with composition, geometry, vulnerabilities and some phase choreographies.
- **Status:** no Status line seen. Reading: historical-reference; self-authored from memory and encyclopaedias per `by_lane/MB_mass_battle.md` section 1.1 (not independently sourced).
- **Bears on:** MB (formations, troop types, geometry), PC (weapon traditions) minor.
- **Content that matters (headings only, from `grep '^##'`):**
  - 01: Sumerian phalanx, Akkadian combined-arms levy, Egyptian New Kingdom, Hittite heavy chariot, Assyrian combined arms ("first true integrated system"), archaic hoplite, Achaemenid, steppe horse-archery.
  - 02: hoplite and Theban oblique order, Macedonian sarissa phalanx with Gaugamela choreography, Hellenistic successors, Roman manipular (triplex acies, quincunx, "the Cannae problem"), Roman cohort, Carthaginian, Parthian (Carrhae), Sassanid, Han, Mauryan/Gupta (elephant doctrine).
  - 03: Byzantine (Phokas hollow square, kataphraktoi wedge), early Islamic (Khalid), Carolingian (Tours), Viking (Stamford Bridge), Anglo-Saxon shield-wall (Hastings choreography), Tang/Song (Talas), Heian.
  - 04: Norman conroi/couched lance, Western feudal heavy cavalry, Crusader (Hattin, Arsuf), Seljuk/Ayyubid (Manzikert), Mongol decimal system (Liegnitz, Ain Jalut), Song/Jin, Kamakura, Khmer/Pagan.
  - 05 (650 lines): Courtrai, Scottish schiltron (Falkirk, Bannockburn), English longbow (Crecy, Poitiers, Agincourt), Hussite wagenburg, Swiss Gewalthaufen, Burgundian (Grandson, Murten, Nancy), Landsknechte (Bicocca).
  - 06: Ottoman (Nicopolis, Ankara, Varna, Constantinople, Mohacs; tabur cengi wagon-fortress), Mamluk furusiyya (Marj Dabiq, Raydaniyya), Timur, Safavid Qizilbash (Chaldiran), late Mongol successors.
  - 07: Sengoku ashigaru, Ming (wei-suo household system, Mu Ying volley, Tumu), Joseon hwacha, Dai Viet (Chi Lang), First Panipat. 08: Aztec, Inca (decimal), Maya, Mississippian, Spanish collisions.
- **Conflicts / stale:** the MB lane file notes these are the sole historical grounding for the formation geometry yet cannot be independently verified (MB_mass_battle.md :302 says the lane did not read 01-16).
- **Open items:** [SKIPPED: bodies of 01-08 — budget; headings only].

### research/pre_firearms_formations/09_throughlines_matchup.md  (read lines 354-395 conclusions; headings for the rest)
- **What it is:** Chunk F1 (2026-05): 29 throughlines in clusters A-J, 8 meta-throughlines M-1..M-8, and the Task-3 matchup matrix in seven tiers.
- **Status:** none seen. Reading: historical-reference.
- **Bears on:** MB, FA, SE.
- **Content that matters:**
  - Seven generic conclusions: no formation wins all matchups; pike-cavalry-missile RPS is real but qualified by terrain and command (Bicocca); combined arms beats mono-culture except in specific terrain; wagon-fortress plus firearms dominant late; steppe horse-archery dominant pre-gunpowder asymmetric formation; the decisive arm is the fixing arm's complement (hammer and anvil); single-arm matchups poorly model war (:356-368).
  - Composite system ranking: Ottoman mature system, Spanish coronelia/early tercio, Mongol decimal combined arms, Roman imperial legion+auxilia, Babur's hybrid, Byzantine, Swiss pike, Mamluk, English longbow, Hussite (:374-383).
  - Meta-throughlines: M-1 doctrine-substrate-opponent triangle, M-2 institution > tactics > weapons, M-4 discipline-timing axis as the universal command skill, M-5 perfect-system trap, M-6 cultural-doctrinal filter, M-7 strategic-political dimension, M-8 compound failures (headings :101-195).
- **Conflicts / stale:** MB lane found M-1/M-5/M-6/M-7 have no carrier below faction scale (MB_mass_battle.md :371). **Open items:** none.

### research/pre_firearms_formations/10_battle_phase_choreography.md  (read lines 298-363 and 437-546; Parts I, II, IV, V headings only)
- **What it is:** Chunk F2 (Task 4): a generic 8-phase framework (0 approach, 1 deployment, 2 skirmish, 3 missile attrition, 4 main contact, 5 decisive commit, 6 collapse, 7 pursuit), per-phase choreography, six battle archetypes, failure modes per phase, ten game-design observations for Valoria.
- **Status:** "The project's four deliverables are complete" (:535). Reading: historical-reference; cited by `modules/mass_battle` provenance as "PFF 10".
- **Bears on:** MB, PC, GO.
- **Content that matters:**
  - Reference tables: movement speeds (heavy infantry march 4-5 km/h, Swiss pike attack 5-7, cavalry charge final gallop 30-40 km/h "last 30-50 m only", army 15-25 km/day, Mongol 50-100 km/day) (:300-318); missile ranges and rates (longbow 200-250 m, 6-10/min; heavy crossbow 1/min; early arquebus 0.5-1/min) (:320-332); frontages per 1,000 men (hoplite 125 m x 8 deep, sarissa 60 m x 16, Roman maniple 100 m x 6) (:334-347); phase durations (decisive commit 2-10 min typical, main contact 1-3 h) (:349-360).
  - Observation 2: the decisive-commit window is "the one mechanic that captures pre-firearm tactics"; Observation 5: fixing/decisive duality visible as roles (anvil vs hammer); Observation 10: 5-15% loss on the winning side, 30-60% on the losing side, mostly in phases 6-7, so "fighting is dangerous but survivable; routing is devastating"; pursuit should be a separate decision (:447-457, :473-477, :507-514).
  - Observation 7: force generation as a strategic-level mechanic (institutions over a maxed elite unit); Observation 9: compound-failure stacking, catastrophic only when several failures stack (:485-505).
- **Conflicts / stale:** the MB lane notes the commit-window figures disagree across files (2-10, 5-30, 1-6 turns) (MB_mass_battle.md :357). **Open items:** the observations are "observations, not specifications" per the project-owner contract (:439).

### research/pre_firearms_formations/11_throughlines_ners_audit.md  (read lines 330-422; Parts I-III headings only)
- **What it is:** all-directions review, NERS scoring and canon-constraint (P-01..P-15) cross-check of the 29 throughlines + 8 meta-throughlines.
- **Status:** closure: "0 P1, 4 P2, 4 P3 findings; 19 strong NERS fit, 11 partial, 6 DEFER, 1 EXCLUDE" (:397-404). Reading: historical-reference.
- **Bears on:** MB, WR (P-10 Coherence x combat morale), PROCESS.
- **Content that matters:**
  - Prioritised integration: M-1 doctrine-substrate-opponent triangle, M-4 discipline-timing, T-1 shock+missile, T-5 force-generation depth, T-17/18/M-6 cultural filter, T-22 technology matrix, T-23 operational geography, T-24 hammer-and-anvil, T-26 single-shot charge, T-28/29/M-8 emergent propagation (:352-361).
  - P2 gaps for Jordan: thread-doctrine interaction, combat-morale x Coherence (is morale layer 2 or 3), tridimensional propagation of military outcomes (P-12), military intelligence x rendering asymmetry (:337-340, :380-390).
  - Scale assignments: personal M-4/T-29; settlement T-15/T-26; territory T-1..T-5, T-22..T-24, M-1/2/7; peninsula T-4/5/12/17/18, M-1/2/5/6/7 (:365-372).
- **Conflicts / stale:** the audit scored throughlines the MB lane later judged unreached (T-MB-7..9). **Open items:** Part V's six questions to Jordan (peninsula geography, gunpowder status, scale assignment) not visibly answered here.

### research/pre_firearms_formations/12_moment_by_moment_dynamic_spacing.md  (read lines 902-940; headings for Parts I-V)
- **What it is:** primary-source reconstruction (manual spacing vocabulary from Asclepiodotus, Aelian, Polybius, Vegetius, Byzantine Praecepta; nine battle reconstructions: Cannae, Pharsalus, Adrianople, Hastings, Crecy, Agincourt, Marignano, Pavia, Panipat), generic patterns of dynamic spacing, reference tables.
- **Status:** none seen. Reading: historical-reference; high confidence on manual-derived spatial primitives, low on absolute timings (:936).
- **Bears on:** MB, GO.
- **Content that matters:**
  - Generic patterns (headings :758-825): approach window 250 m-2 km; skirmish zone 50-300 m forward of main line; killing arc of mass missile fire 30-250 m; main-contact frontage matches initial deployment; lethal pocket forms when an army is pressed into a smaller area than its formation needs; cavalry final gallop 30-50 m; decisive commit occupies 5-30 minutes; full battle 2-9 hours.
  - Game notes O-1..O-7 (:906-918): 250-800 m first-contact distance as a natural battle-scale spatial unit; ~12-20 m2 per man lethal density gives step-change not linear casualty multipliers; compress a battle to 5-10 player minutes with the decisive commit in a 10-60 s window; cavalry cannot sustain full charge speed; rain/mud/terrain as dramatic modifiers; doctrinal manuals as a game-economy resource; chronicle authorship shaping memory.
  - `[GAP]` timing is mostly derived from speed x distance, not source-stated (:938).
- **Conflicts / stale:** none checked. **Open items:** none.

### research/diagrams/mass_battle_formations/README.md
- **What it is:** note on a visual engine-vs-history comparison of mass-battle deployment after ED-MB-0017 (generator `generate_comparison.py`, HTML and PNG outputs, `SOURCES.md`).
- **Status:** none. Reading: historical (the geometry test it cites was dropped 2026-11-04, :22); the artifact files (HTML/PNG/py) are not in the assigned list.
- **Bears on:** MB, GO.
- **Content that matters:**
  - Fixed and confirmed: no subunit overlap (P-1), symmetric double envelopment (P-2), echeloned refused flank (P-3) (:28-39).
  - Caveats: the wrap needs until ~t16-t20; no cavalry ride-around so the ring is a horseshoe not a circle (`_envelop_goal` models the infantry wrap only); single line not a reserve/triplex acies; envelopment "still often loses" in raw outcome (DG-6 over-decisiveness, ED-MB-0016) (:41-54).
- **Conflicts / stale:** `tests/valoria/test_deployment_geometry.py` dropped 2026-11-04 so the geometry is no longer pinned (:22). References `../../../audit/2026-07-22-mass-battle-stress-test/` (a retired path; `.audit/` now). **Open items:** cavalry rear-transit, depth-line relief unmodelled (:44-50).

### research/diagrams/mass_battle_formations/SOURCES.md
- **What it is:** citation list for the historical formation diagrams (Cannae, Leuctra, Leuthen, Roman triplex acies, phalanx/oblique order): Wikipedia/Commons maps, Historia Civilis animations, Polybius, Livy, Goldsworthy, Xenophon, Sabin.
- **Status:** none. Reading: reference. Images not stored (proxy denied downloads).
- **Bears on:** MB.
- **Content that matters:** schematics are the author's own drawings "from the geometry described in these sources", not tracings; they use the sim's coordinate convention (:58-61).
- **Conflicts / stale:** points at the retired `audit/2026-07-22-mass-battle-stress-test/` path (:59). **Open items:** none.

### research/diagrams/mass_battle_formations/perimeter_model/README.md
- **What it is:** note on a machine-vision check of the perimeter target-point / normal model for engine formations (Line, Arrowhead, Column, GappedLine).
- **Status:** none. Reading: historical (2026-07-23).
- **Bears on:** MB.
- **Content that matters:** target points are face midpoints (major) and corners (minor), sharp vertex at interior angle <=60 degrees, outward normals give the required approach angle; Line panel matches Jordan's hand drawing; the convex hull bridges the GappedLine's internal lane, so gapped formations need concave/internal-edge perimeter handling (:3-17). Spec cited: `audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md`.
- **Conflicts / stale:** spec path is the retired `audit/` tree. **Open items:** concave perimeter handling for gapped formations (:16-17).

### research/governance/00_MANIFEST.md
- **What it is:** manifest of the governance research corpus (2026-07-14, ED-IN-0064): three theme documents x 8 civilisations, with `=> Valoria design hook` lines.
- **Status:** `RESEARCH — filed 2026-07-14 · Lane: IN · ED-IN-0064 · analytic/reference, not a design ratification`. Reading: historical-reference.
- **Bears on:** FA, SC, WR.
- **Content that matters:** method was Sonnet researcher per civilisation then Opus verifier (every verdict SOUND_WITH_FIXES) (:16-24); civilisations: Ottoman, Roman, Carolingian, HRE, Renaissance Italy, Venice, Han/Three Kingdoms, Shogunate Japan; Byzantine omitted (:26-40); "Mandate of Heaven is history only, never proposed as a Valoria mechanic" (:58-60); hooks map to the PROPOSED 8-value `governance_mode` taxonomy, the `faction_politics` Standing ladder and Demotion Magnitude (:45-48).
- **Conflicts / stale:** hooks are proposals in a retired idiom (FA lane found all research hooks use Key/Directive/Need); refers to `designs/audit/...` paths (dissolved tree). **Open items:** Byzantium "add later if wanted" (:30).

### research/governance/governance_modes.md  (read the synthesis and hooks table, lines 1-48; per-civilisation detail 49-469 headings only)
- **What it is:** thematic governance research (2026-07-14): how a polity decides, across eight civilisations (Ottoman, Roman, Carolingian, HRE, Renaissance Italy, Venice, Han/Three Kingdoms, shogunal Japan), with a consolidated design-hooks table.
- **Status:** `RESEARCH — filed 2026-07-14 · Lane: IN · ED-IN-0064 · analytic/reference, not a design ratification`. Reading: historical-reference; hooks are phrased in the retired Key idiom (Key, Directive-Key, L/PS) and cannot be adopted as written (FA lane finding, `by_lane/FA_faction_actions.md` verdict 2).
- **Bears on:** FA, SC, CHAR.
- **Content that matters:**
  - Findings: autocracy bounded by a parallel legitimacy order (Ottoman kanun/seriat and fatwa, Roman auctoritas, Carolingian synods, Han tingyi); oligarchic councils split three ways (portfolio-differentiated, co-equal capped, estate-allocated with sequential veto and documented representation-lag); selection as anti-capture engineering (cursus honorum, Han cha ju, Florentine imborsazione, Venice's doge pipeline alternating random subsets and scrutiny, conclave Ubi periculum decaying holdout cost); governance mode as mask vs substance and as legislated migration (Venice Serrata) (:20-28).
  - Primitives named: peer-blocking veto (intercessio) distinct from vote-tallying and gating a "holdout" state; chain-bypass authorities constructed, purchased, negative-only, doubled or dormant-but-live; recognition-fission; rank = secession blast-radius (:22, :30).
  - The 11-row consolidated hook table maps each pattern to a mechanic named in the proposed 8-value `governance_mode` taxonomy (AUTOCRATIC_FIAT, OLIGARCHIC_COUNCIL, NEGOTIATED_ESTATES, MERITOCRATIC_BUREAUCRATIC, CONSENSUS_UNANIMITY, ROYAL_COURT_APPOINTMENT) (:34-47).
- **Conflicts / stale:** taxonomy values and Key/L-PS primitives belong to the proposed, since-retired governance design; no code reads them. Byzantium omitted.
- **Open items:** per-civilisation verifier notes are inline and (per FA lane) truncated mid-sentence in places.

### research/governance/political_hierarchy_standing.md  (read lines 1-12 and section headings only; synthesis 18-48 not opened; 486 lines)
- **What it is:** thematic research on rank/office hierarchy, advancement and demotion across the same eight civilisations, mapped to the `faction_politics` Standing ladder, Demotion Magnitude and a resolution-quality-to-standing bridge.
- **Status:** same RESEARCH header as `governance_modes.md`. Reading: historical-reference; retired idiom.
- **Bears on:** FA, CHAR, SC.
- **Content that matters:**
  - Framing (:10-16): standing was never a single scalar but a claim on an underlying currency (trust/itimad, patronage-credit/commendatio, immediacy/Reichsunmittelbarkeit, assessed yield/kokudaka, captured eligibility lists), and a rank is only as solid as its currency.
  - Per-civilisation sections cover ladder, routes up, routes down, standing currency (e.g. Roman cursus honorum as an 8(+)-rank ladder with senatorial vs equestrian parallel power bases; patronus/cliens) (headings :101-136, :209-249).
  - FA lane cites `political_hierarchy_standing.md:427-429` for the consort-clan counter-case behind H-100 "kinship-derived seats get containment" (`by_lane/FA` verdict 8).
- **Conflicts / stale:** Standing range has 2-6 versions across the archived FA corpus (FA lane). **Open items:** none read.

### research/governance/conflicts_power_struggles.md  (read synthesis and hooks table, lines 1-45; per-civilisation detail headings only)
- **What it is:** thematic research on succession crises, usurpation, civil war and ruler-vs-assembly collisions, with a 14-row design-hooks table.
- **Status:** same RESEARCH header. Reading: historical-reference; retired idiom (Key/two-signal primitive).
- **Bears on:** FA, WR, MB (army loyalty), SC.
- **Content that matters:**
  - Four generative mechanisms: succession vacuum, autonomy-equals-secession, displacement grievance, channel starvation (assassination where no contest channel exists) (:20). Legitimacy collapse modes: single fragile ritual (Praetorians auctioning the throne), split legitimating bodies, procedural legitimacy (Venice) (:22).
  - "Rank = secession blast-radius" restated; fuse length (fast Onin/Ciompi/Pazzi, slow Kamakura, no-relief-valve Roman third century); relief valves (Venice graduated removal ladder, Ottoman grand-vizier-as-scapegoat) (:24-26).
  - Hooks: two-signal resonance (objective strain + independent legitimating signal must co-fire), suppression-backfire (a "solved" unrest becomes a non-decaying grievance re-arming at a lower threshold), relief-valve scapegoat, emergent-arc seed (silent accumulator not reset between crises), "gate army/enforcement loyalty to an impersonal charter, never a seat-holder" (:32-43). The last bears on MB army loyalty and the K-NPC-4 finding that members answer to a dead head.
- **Conflicts / stale:** Mandate of Heaven excluded by ruling (:58-60 of manifest). **Open items:** none read.

<!-- END -->
