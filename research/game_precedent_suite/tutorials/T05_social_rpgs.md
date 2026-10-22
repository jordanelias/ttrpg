# T05 Tutorials: social/combat RPGs (Disco Elysium, Griftlands, Baldur's Gate 3, Kingdom Come: Deliverance I/II)
Tags: [V3 url date/version] = read in a fetched page body this session (2026-10-22); [S3 url] = search snippet only; [M] = memory, not re-checked; `?` = not established; [CONTESTED] = sources disagree.
URL aliases used inside tags: DEw = https://discoelysium.wiki.gg/wiki (live undated wiki text, read via action=raw); WP = https://en.wikipedia.org/wiki.

### Disco Elysium (The Final Cut) - facts line
(Day-1 room/void beats and the opening sequence are [M]; mechanics, timing, tasks and numbers are wiki-sourced [V3]. No Valoria comparison.)
- Developer/publisher ZA/UM; single-player isometric dialogue CRPG, no combat system [V3 WP/Disco_Elysium; V3 DEw/Disco_Elysium]. Windows 2019-10-15; The Final Cut 2021-03-30 (full voice acting, narrator, four Political Vision Quests, new art/music) [V3 DEw/Disco_Elysium].
- Version relied on: Final Cut rules as on the live wiki; last patch listed there 2025-12-17 (its notes: a Unity vulnerability patch and a storefront link; no rules change listed) [V3 DEw/Disco_Elysium, Patch History].
- Assumed: standard difficulty (Hardcore noted below), the Thinker archetype or a custom build. One session = one in-game day, roughly 2-4 hours [M]; a full playthrough 25-40 hours [V3 earlyguides.com/disco-elysium/beginners-guide, undated].

#### 1. Setup choices
- **Build**: three archetypes or a custom spread. Thinker INT5/PSY1/FYS2/MOT4 (signature Encyclopedia); Sensitive 1/5/4/2 (Inland Empire); Physical 1/2/5/4 (Hand/Eye Coordination) [V3 DEw/Skills]. Custom = 12 points over the four attributes, "max out at six" each [V3 gamerevolution.com/guides/621124-disco-elysium-best-build-starting-stats]; archetype sums are all 12 [computed from V3 DEw/Skills].
- **What an attribute point does**: sets the starting level of all six skills under it and their learning cap; the signature skill gets +1 level and raises the learning cap of its whole attribute by 1 [V3 DEw/Skills]. Exact cap arithmetic: see 8.
- **Signature skill**: one pick, as above. **Hardcore mode** (optional, off by default): every white check +1 difficulty, healing items and drugs cost 2x (drugs start with one less dose), reál found in containers -15%, +5 XP per finished task [V3 DEw/Disco_Elysium].
- **Not chosen up front**: appearance (none) [M]; the opening "void" dialogue answers shift your first wake time (8:05 or 8:06) [V3 DEw/Time].

#### 2. The loop
Clock: a day counter and an in-game clock that moves ONLY during dialogue and story events; walking the map costs nothing [V3 DEw/Time]. Days start 7:30; time freezes at 2:00 AM until you sleep; the earliest possible finish is Day 5; no day limit [V3 DEw/Time]. Day 1 is Monday 12 March '51 [V3 DEw/Time].
1. Walk (isometric, real-time, no time cost) to a person or object; hold Tab to highlight interactables [S3 search snippet, source unclear].
2. Open a dialogue. Your 24 skills interject as voices; each line that surfaces is a PASSIVE check (no roll: skill+modifiers+6 vs difficulty) [V3 DEw/Skills]. Clock advances a few minutes per exchange.
3. Choose a reply. Some replies are ACTIVE checks: 2d6 + skill + modifiers >= difficulty; double 1 always fails, double 6 always passes [V3 DEw/Skills]. White = retryable after something changes; red = once [V3 DEw/Skills].
4. XP: every task gives XP; each 100 XP = 1 skill point [V3 DEw/Tasks]. Spend points to raise a skill (reopens a failed white check), to open Thought Cabinet slots, or to forget a thought [V3 DEw/Tasks; DEw/Thought_Cabinet].
5. Optionally slot a Thought; it "internalises" over 15 min to 20 h of in-game time (several at once; sleep does not count) [V3 DEw/Thought_Cabinet].
6. Health and Morale take damage from failures, anti-passives and drugs; heal with Magnesium/Hypnogamma charges or by sleeping (restores both to full) [V3 DEw/Morale; DEw/Time].
7. From 21:00 you may sleep (room at the Whirling 20 reál/night; free in the Coastal Shack from Day 3) [V3 DEw/Time]. The day counter advances; new NPCs/areas appear on fixed days (Hardie boys Day 2, west Martinaise Day 3, Political Vision Quests Day 4) [V3 DEw/Time].
Interrupts: scripted cutscenes (the Mercenary Tribunal, then the island and The Return) take control [V3 DEw/Harry_Du_Bois; DEw/The_Return]. Automated: passive checks, time, Kim's commentary, Thought research timers.

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Pick a dialogue reply (constant) | minutes of clock | advances plot, may trigger a check, sets hidden flags ("microreactivity") [V3 DEw/Disco_Elysium] | every conversation |
| Attempt an active check (constant) | white: free retry once conditions change; red: permanent; failure may cost Health/Morale or branch | pass/fail fork; failing can beat passing [V3 DEw/Skills] | when the % shown on hover is acceptable [per V2 gry-online] |
| Spend a skill point (frequent) | 1 point (100 XP) | +1 skill, up to its learning cap; reopens white checks [V3 DEw/Skills] | after a white-check failure or at a milestone |
| Internalise a Thought (frequent) | a free slot, 15 min-20 h clock, temporary penalty during research | permanent skill/cap changes or unique effects [V3 DEw/Thought_Cabinet] | when a thought appears |
| Forget a Thought / buy a slot (rare) | 1 skill point each | frees slot; forgotten thought is gone for the playthrough [V3 DEw/Thought_Cabinet] | when slots are full |
| Equip clothing (occasional) | none, but slots are finite | skill modifiers up and down (e.g. +1/+2, some -1/-2) [V3 DEw/Skills] | before a key check |
| Drugs/alcohol/cigarettes (occasional) | reál, Health/Morale | temporary skill shifts [V3 DEw/Skills] | before a check, or when stressed [M] |
| Heal with Magnesium/Hypnogamma (as needed) | one charge | Morale/Health restored [V3 DEw/Morale] | when a bar is low |
| Sleep (daily) | 20 reál/night at first | full heal, next day, content unlocks [V3 DEw/Time] | after 21:00 |
| Raise money: bottles, pawn, favours (Days 1-2) | time | tare machine pays 0.10 reál per bottle (0.20 with Hobocop) [V3 DEw/Pay_for_damages] | Day 1 |
| Pursue / ignore a task (constant) | clock | most tasks are optional XP [V3 DEw/Tasks] | whenever the Journal shows one |
| Ask Kim to step in (rare) | after 3-4 failed checks | auto-resolves the Titus checks [V3 DEw/Skills; DEw/Prove_your_authority_to_Titus_Hardie] | stuck on a scripted-success check |
| Wait on a bench 15/30/60 min (rare) | clock | lets timers run [V3 DEw/Time] | to finish a thought |
| Order a die from the Novelty Dicemaker (rare) | 8 h clock + reál | retry certain failed checks [V3 DEw/Time; DEw/Skills] | after a key failure |

#### 4. First hour, step by step
1. New Game; choose Hardcore or not; pick an archetype (or spread 12 points) and a signature skill [V3 DEw/Skills].
2. The void: you talk to your own brain (Ancient Reptilian Brain, Limbic System). Answers set the wake time [V3 DEw/Time]; the voices teach that skills talk [M].
3. Wake in a wrecked hostel room with a hangover; you may die in minutes (turning on the lights can cause a heart-attack Game Over) [V3 DEw/Harry_Du_Bois].
4. Search the room: the tie on the ceiling fan is a Medium (10) white Savoir Faire check, failing hurts Health [V3 DEw/Harry_Du_Bois]. Failing is part of the tutorial.
5. Phone the station's lazaret (Nix Gottlieb) and read the ledger/badge [V3 DEw/Tasks lists the task "Call your station's lazareth"; call details [M]]; open the Journal.
6. Go downstairs. Garte hands you the "Pay for damages" task: 130 reál, reducible to 100/60/30 by a red Authority 10 or Savoir Faire 10 check [V3 DEw/Pay_for_damages].
7. Meet Lt Kim Kitsuragi; accept the hanged-man case [V3 WP/Disco_Elysium]; the map opens and the case is the thread.
8. Walk to the body behind the hostel; examine it. Visual Calculus and other skills fire passive/active checks [V3 DEw/Skills].
9. Spend your first skill points when a white check shows "reopen"; watch the Thought Cabinet when a thought is offered (3 free slots) [V3 DEw/Thought_Cabinet].
10. Collect bottles with the yellow bag at the Frittte tare machine for small money [V3 DEw/Pay_for_damages].
11. Check the Journal: tasks plus found white checks listed beside the map [V3 DEw/Skills].
12. By 21:00 secure 20 reál/night; if short, Kim offers the Radiant Spinners pawn (200 reál) [V3 DEw/Pay_for_damages].
13. After 22:00 take the end-of-day debrief on the balcony (an essential task) [V3 DEw/Tasks]. Then sleep.
14. Day 2: the Hardie boys appear; "Prove your authority" (white Authority 16) starts [V3 DEw/Prove_your_authority_to_Titus_Hardie]. Not paying Garte on Day 2 can soft-lock the game [V3 DEw/Time].

#### 5. What changes later
- Content gates by day: Day 2 Hardie boys and Sunday friend interview; Day 3 west Martinaise and the water lock; Day 4 Political Vision Quests (Final Cut) and the PISSF****T/Fuck the World jackets [V3 DEw/Time].
- Scaling: more thoughts accumulate (53 total, 12 slots); skill caps rise through thoughts and drugs; ~10,287 passive and 211 anti-passive checks sit in the script, 115 (Hand/Eye) to 899 (Empathy) passives per skill [V3 DEw/Skills]. High skills pull more dialogue.
- Plot compresses into the Tribunal, the island/phasmid and The Return (final task) [V3 DEw/Harry_Du_Bois; DEw/The_Return]. Pressure is money (rent), then Health/Morale attrition.

#### 6. Failure and ending
- Health 0 or Morale 0 = Game Over; on the last Morale unit with charges left a countdown prompts healing [V3 DEw/Morale]. Reload saves. Most failed checks branch rather than end [V3 DEw/Skills].
- Soft-lock: unpaid room on Day 2 [V3 DEw/Time]. Five scripted checks cannot be passed; four scripted ones almost cannot be failed [V3 DEw/Skills].
- Win = The Return, a trial; ends with credits, no post-game [V3 DEw/The_Return]. Outcomes: the page says 6 but lists 4 [V3 DEw/The_Return].

#### 7. Consequential vs cosmetic choices
- Consequential: the attribute spread and where points go (shapes which of ~10,000 passives and which options exist); thought selection (53, some mutually exclusive); rent/money in Days 1-2 [V3 DEw/Skills; DEw/Thought_Cabinet; DEw/Time].
- Mostly cosmetic or near-dominant: the clothing slot (+1 to +2, wear the best for the check); healing consumables, since sleep restores both bars free; the Hardcore toggle (numbers only) [V3 DEw/Disco_Elysium].
- Dominant-answer signal: Kim auto-passes the Titus checks after 3-4 failures, so those checks are not real gates [V3 DEw/Skills].
- Community consensus (not mechanics): 4-4-2-2 favouring Intellect/Psyche is the commonly recommended narrative build; failure is often funnier, so do not reload every failed check [S3 search summary of gamerevolution/gamersdecide for the build; V3 earlyguides for the advice].

#### 8. Open items
- V2 A2/M4: custom build limits now sourced (12 points, per-attribute max 6) but the same guide's cap example is ambiguous (a base-3 skill "can gain up to three more points"), so learning-cap arithmetic is `?`; archetype table above shows max 5.
- earlyguides.com states white checks are one-time and red retryable: the OPPOSITE of the wiki [CONTESTED]; wiki followed.
- V2 J3: Morale ~13 maximum is still unchecked. Whether the % shown on hover is the engine's own number: still `?`.
- Day-1 steps 2 and 5 (void, phone call) are [M]; no official tutorial text was fetched. Starting Health/Morale totals: `?`. V2 A4 inventory size still `?`.
- V2 M2 fill: the wiki task list has 138 rows, 16 flagged essential to plot progression (own count of TRUE/FALSE, list may be incomplete) [V3 DEw/Tasks]. V2 H2 (Kim's opinion total visible?) still `?`.
- Attachment grep: no Disco, Griftlands or KCD claims exist in the four uploads (hits are "discourse", "discontinuity", "disconnection", "discoverable", "discontent" only; word-boundary grep returns zero lines).

### Griftlands - facts line
(Mostly [V3]: Klei's own Steam update posts plus the Fandom wiki read through its MediaWiki API. WARNING: several wiki pages are Alpha-era stubs, banner "mechanics subject to change"; where a later Klei post contradicts them I follow Klei. Fandom page-body fetch is Cloudflare-blocked; API `prop=revisions` worked.)
Aliases: GLw = https://griftlands.fandom.com/wiki ; STM = Steam news for app 601840 via api.steampowered.com/ISteamNews (posts dated below).
- Developer Klei Entertainment; roguelike deckbuilder with two card games, combat and negotiation; Early Access 2020-06-14, 1.0 on 2021-06-01 (Smith campaign completed that day) [V3 STM 2021-06-01]. Last Klei news post in the feed: 2021-08-30 (translations/modding only) [V3 STM]. Rules relied on: 1.0 plus the 2020 Perks/Prestige/Mettle updates [V3 STM 2020-08-20, 2020-12-10].
- Assumed: Sal's campaign "Hunting Kashio", Prestige 0 (Normal). One run = 5 in-game days for Sal, 4 for Rook and Smith [V3 GLw/Quests]; real-time per run `?` (not found; [M] a few hours).

#### 1. Setup choices
- **Character/campaign**: Sal (bounty hunter, dual daggers, Combo/Finisher; start HP 65 / Resolve 30 / 75 shills), Rook (aging spy, charge cells + Parasite; 48 / 36 / 75), Smith (bottles, Moxie, Renowned; unlocked by beating Rook's first day when added) [V3 GLw/How_to_play_guide_of_Griftlands (alpha figures, may have shifted); STM 2020-11-05]. Each has its own battle AND negotiation deck (Sal starts with 11 battle and 10 negotiation cards) [V3 GLw/Cards; GLw/Sal].
- **Difficulty**: Prestige 0-7, each stacked on the last and +10% XP: 1 no day-restart + promoted enemies; 2 tougher fights/negotiators; 3 no resolve restore after battle, sleep heals 50%; 4 weaker allies, stronger bosses; 5 -20% max HP/resolve; 6 +25% prices, -1 graft slot of each type; 7 no Mettle [V3 GLw/Prestige]. Also a low-difficulty Story Mode [V3 STM 2020-08-20]. New prestige unlocks by clearing the final day at the current level, per character [V3 GLw/Prestige].
- **Perks** (up to 3 slots, 34 perks, 5 tiers; bought with points from "Grifts") e.g. +6 max Health, +75 starting shills [V3 STM 2020-08-20; GLw/Perks]. **Card Sets** (10 per hero, 3 negotiation + 3 battle cards each) toggled before the run [V3 GLw/Card_Sets; How_to_play_guide]. **Outfits**: cosmetic [V3 same guide].
- **Custom game mode**: mutators (17 at Alpha, e.g. Barbarous = no murder repercussions) and custom card pools live here, not in normal play [V3 STM 2020-08-20; GLw/Mutators].
- **In-run first choices**: a starting bonus on Day 1 (Sal: "Lost and Found"; Rook declares an item to the guard; Smith drafts a card) [V3 GLw/Sal's_Campaign, Rook's_Campaign, Smith's_Campaign].

#### 2. The loop
Clock: story days (Sal 5, Rook/Smith 4), each split into jobs, optional events, a night job and a boss; no real-time pressure (turn-based) [V3 GLw/Sal's_Campaign].
1. Pick a quest. You see name, one-to-five-star difficulty, "focus" (combat, negotiation or both) and rewards; Sal often chooses among three givers [V3 GLw/Quests].
2. Travel the overworld map; a "Limited Time Opportunity"/random event may fire at set points (rewards never scale) [V3 GLw/Events].
3. Resolve each encounter with a card game. Negotiation: draw 5, 3 Action Points, destroy the opponent's core argument before yours falls (resolve = HP); Composure = temporary armour [V3 GLw/Negotiation (alpha numbers)]. Battle: AP-and-card combat vs HP; enemies panic at a threshold (animals flee, people surrender) [V3 GLw/Battle].
4. After a fight you may kill or spare survivors; killing in public can make hated enemies [V3 GLw/Battle; GLw/Relationships].
5. Rewards: shills by difficulty plus one random extra: card upgrade, card removal, restore 20 Health or 10 Resolve, an item card, or a graft choice. Nothing if you fail [V3 GLw/Quests].
6. Between jobs: shop, eat (+15 Health, adds a Bloated card), drink (30 shills, +10 Resolve, adds Tipsy and Slurred Speech cards), gift shills to Liked NPCs [V3 GLw/Battle; Drinking; Gifting].
7. Evening: night quest or merchant, then a boss fight. Then sleep: full heal, or 50% at Prestige 3+; status cards marked "Sleep it off" vanish; next day begins [V3 GLw/Sal's_Campaign; Sleep_It_Off; Prestige].
Interrupts: provoked fights from failed negotiations; ambushes (Day 2 assassin boss for Sal); killing someone whose friends are present. Automated: enemy intent selection, draw/shuffle, faction relationship changes, Mettle awards [V3].

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Play a card (constant) | AP (default 3 per turn) | damage, defence, argument, status | every turn |
| Pick a target / break an argument (constant) | AP/cards | overflow damage hits the core argument [V3 GLw/Negotiation] | each negotiation turn |
| End turn / concede at turn start (rare) | fail the negotiation, keep remaining resolve | avoids a resolve wipe [V3 GLw/Negotiation] | losing |
| Choose negotiate vs fight vs bribe (constant) | resolve vs HP vs shills | different risk pool and reward | each quest node |
| Pick a quest (each node) | time-of-day slot | rewards by stars | day start |
| Draft/upgrade/remove a card (constant) | reward slot or shop shills | deck shape; cards level by play [V3 GLw/How_to_play_guide] | after fights |
| Install a graft (occasional) | graft slot (separate battle/negotiation) | permanent run modifier [V3 GLw/Grafts] | when offered |
| Spare vs kill (frequent) | relationship cost | spared may become ally; killed may anger friends [V3 GLw/Battle] | after panic/surrender |
| Gift shills to a Liked NPC (occasional) | 50 x max(2, renown, combat strength) [V3 GLw/Gifting] | converts to Loved: social boon | when you can afford it |
| Eat/drink (frequent) | shills + junk cards | Health or Resolve | before boss |
| Hire a mercenary / bribe an NPC (occasional) | shills | ally for one encounter [V3 STM 2021-06-01] | before a hard fight |
| Haggle for quest pay (rare) | needs Haggle Badge boon | mini-negotiation raises reward [V3 GLw/Haggling] | side quests |
| Choose a faction/side (Day 2 for Sal) | relationships | unlocks that side's quests and the final fight [V3 GLw/Sal's_Campaign] | once per run |
| Flourish (when meter full) | meter filled by playing cards, dealing/mitigating damage | super-move in battle or negotiation [V3 STM 2020-12-10] | when the meter is full |
| Meta: spend Mettle between runs (rare) | Mettle from quests/wins | permanent upgrades [V3 STM 2020-12-10] | at the Mettle shopkeeper |

#### 4. First hour, step by step (Sal, Day 1)
1. Choose Sal; skip mutators; look at the starting decks (negotiation: Sal's Instincts, 3 Deflection, 3 Fast Talk, 2 Threaten, 1 Quick Thinking) [V3 GLw/Sal].
2. Arrive in Murder Bay, reunite with Fssh at the Grog n' Dog; take the "Lost and Found" starting bonus [V3 GLw/Sal's_Campaign].
3. Take your first job; the screen shows stars and focus [V3 GLw/Quests].
4. First encounter, most likely a negotiation: read the core argument and the opponent's intent ring before playing [V3 GLw/Negotiation].
5. Play cards, break any arguments, keep Composure up; know that you may concede at turn start [V3 GLw/Negotiation].
6. Win; read the reward menu; prefer card removal/upgrade early (community, [M]).
7. Take the next job: a battle. Watch the panic threshold; try to push enemies to surrender and spare them [V3 GLw/Battle].
8. Collect a Limited Time Opportunity on the map [V3 GLw/Sal's_Campaign].
9. Do not enter the night market before healing: the Grog n' Dog triggers the last fight, so eat/drink first [V3 GLw/Sal's_Campaign].
10. Night Merchant quest, then the Day 1 boss fight, then sleep [V3 GLw/Sal's_Campaign].
11. Day 2: choose a side (Admiralty or Spree), face a night assassin, decide to kill, delegate or free him [V3 GLw/Sal's_Campaign].

#### 5. What changes later
- Enemy difficulty rises each day: Hunting Kashio quests run stars 1,1,2,2,3,3,4,4,5 [V3 GLw/Difficulty]. Deck bloat from status cards and drafted cards is the main pressure (deck cap 50, smaller decks recommended by the alpha guide) [V3 GLw/Cards; How_to_play_guide].
- New systems unlock across runs: card sets, outfits, prestige levels, Flourishes (by beating bosses at higher prestige), Mettle upgrades, perks via Grifts, a new daily-run type [V3 STM 2020-08-20, 2020-12-10].
- Mid-run: factions harden (Day 3 faction quests; Day 4 capture Nadan or assassinate Oolo; Day 5 Auction Day and final boss Kashio) [V3 GLw/Sal's_Campaign].

#### 6. Failure and ending
- Health 0 ends the run. At Prestige 0 you may restart the day once; at Prestige 1+ you cannot [V3 GLw/Prestige] (the Alpha Battle page says "only from day 2" [V3 GLw/Battle]). Losing Resolve only locks negotiation until you restore some [V3 GLw/Negotiation].
- Failed negotiations can force fights and lose rewards [V3 GLw/How_to_play_guide]. Win = finish the final boss of the campaign; unlocks the next prestige (per character) [V3 GLw/Prestige]. A new run reshuffles missions/cast around fixed story beats [V3 STM 2021-06-01].

#### 7. Consequential vs cosmetic choices
- Consequential: deck thinning/pruning (alpha guide "smaller decks better", [M]-grade community strategy); which side you pick on Day 2; who you kill (hate is sticky); resolve and HP management into the night boss.
- Consequential and mechanical: relationship stage shifts a negotiation's core resolve by -20/-10/+10/+20 for Loved/Liked/Disliked/Hated [V3 GLw/Relationships].
- Cosmetic: outfits [V3 GLw/How_to_play_guide]; many arguments ("not worth memorizing") [V3 GLw/Negotiation].
- Likely dominant (community consensus, not verified here): armour/Defense and small-deck builds; Game Informer's reviewer says few reasons to want characters to dislike you [per V2].

#### 8. Open items
- V2 H1 note ("influence/provoke not found"): Influence AND Dominance exist as player-side arguments boosting Diplomacy and Hostility cards; negotiation card types are Manipulation (purple), Diplomacy (green), Hostility (red) [V3 GLw/How_to_play_guide, alpha-era]. "Provoke" still not found. V2's "intimidation" branch name = Hostility [CONTESTED naming].
- V2 H2 "numeric thresholds between stages ?": stages are discrete and event-driven (attack/shakedown = Disliked, murder = Hated, favours/drinks = Liked, gifts = Loved); effect on opponent core resolve -20/-10/+10/+20 [V3 GLw/Relationships].
- V2 M4: card damage can be a range for some cards (Drunken Master "wide damage spread"; Interrogate 2-5; Wanted 6-9) and negotiation intents ARE shown as an inner ring; battle intents `?` [V3 GLw/Arguments_and_Bar_Fights, Negotiation].
- V2 G3: Prestige 0 allows one day restart, Prestige 1+ none [V3 GLw/Prestige]; V2's "3-4 checkpoints" unconfirmed here.
- Not established: real-time length of a run; Brawl mode rules (appears in difficulty table only); whether the 3-AP/5-card figures still hold in 1.0.

### Baldur's Gate 3 - facts line
(Rules and numbers are [V3] from bg3.wiki, read through its MediaWiki API: live, undated community wiki text; beginner advice from two fetched guides. Playtime and exact tutorial prompts are [M].)
Alias: BGw = https://bg3.wiki/wiki.
- Larian Studios; D&D 5e-based party CRPG, real-time exploration, turn-based combat. PC 2023-08-03 [per V2 WP/Baldur's_Gate_3]. Version: Patch 8, the final major patch, 2025-04-15 (12 new subclasses, photo mode); the wiki names Hotfix 36 as latest [V3 BGw/Patch_notes/Patch_8].
- Assumed: Balanced difficulty, single player, a Custom character (not an Origin), Karmic Dice at its default (on). One session = one rest cycle (a camp night), about 1-2 hours [M]; whole campaign tens of hours `?`.

#### 1. Setup choices
- **Character**: Custom, one of six Origins (Astarion, Gale, Karlach, Lae'zel, Shadowheart, Wyll; each has a fixed background, unique quest and dialogue) or The Dark Urge (customisable, unique background Haunted One) [V3 BGw/Character_creation]. Origins can change class after an early point; Custom/Hireling appearance via the camp Magic Mirror [V3 BGw/Character_creation; BGw/Campsite].
- **Race** 11 (Human, Elf, Drow, Half-Elf, Half-Orc, Halfling, Dwarf, Gnome, Tiefling, Githyanki, Dragonborn); **class** 12 (Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard), subclass at level 1-3; **background** 12, which gives proficiencies and Inspiration but "do not impact dialogue or quests" [V3 BGw/Character_creation]. Race, body type and background are locked after creation [V3 same].
- **Ability scores**: 27-point buy, scores 8-15, 13 and below cost 1 per point, 14 and 15 cost 2, then a +2 and a +1 bonus [V3 BGw/Character_creation].
- **Difficulty** (changeable any time except Honour): Explorer (enemy HP -30%, party +100% HP bonus, all proficiency +2, 20% merchant discount, no multiclassing); Balanced (baseline); Tactician (+20-30% NPC HP, enemies +2 to hit and +2 DC, smarter targeting, long rest costs 80 supplies); Honour (one save slot, boss legendary actions, restoration pods once); Custom (e.g. rest cost up to 120) [V3 BGw/Difficulty; BGw/Resting].
- **Settings**: Karmic Dice (default on) in Gameplay Options [V3 BGw/Dice_rolls].

#### 2. The loop
Clock: no calendar; three modes: real-time exploration, turn-based combat (initiative, rounds), and cutscene dialogue; time-of-day matters only at camp [V3 BGw/Turn-based_mode; BGw/Campsite]. Save is manual plus autosave; Honour mode is one overwritten slot [V3 BGw/Difficulty].
1. Explore in real time with up to four party members; Perception/trap checks fire automatically and passively [V3 BGw/Dice_rolls; DigitalTrends].
2. Talk: a cutscene dialogue where the active member picks replies; class, race and discoveries unlock options; some options are ability-check rolls with an "Add Bonus" step first [V3 BGw/Dialogue; BGw/Dice_rolls].
3. A combat starts (or you start it): turn-based mode engages automatically; everyone in range rolls d4 + Dex for initiative; a hidden attacker gives a surprise round [V3 BGw/Turn-based_mode].
4. On your turn each creature has one Action, one Bonus action, one Reaction (a response to triggers) and movement; allies adjacent in order may play simultaneously (up to 10 creatures) [V3 BGw/Resources; BGw/Turn-based_mode].
5. Attack/save rolls resolve mostly in the background; Karmic Dice may force a hidden auto-success after failures [V3 BGw/Dice_rolls; DigitalTrends].
6. Loot, XP, level-ups (cap 12 at 100,000 XP) [V3 BGw/Experience].
7. Short rest (twice per long rest, anywhere) restores up to half HP and some class resources; long rest at camp costs 40 camp supplies (full restore), else a partial rest (half HP/resources, camp events still play) [V3 BGw/Resting].
8. Camp night: companion and origin scenes, quest advancement and time-sensitive events trigger on rests; swap party, store items, use Withers (respec 100 gold, resurrect 200 gold) [V3 BGw/Resting; BGw/Campsite; BGw/Withers].
Interrupts: story cutscenes, ambushes, crimes witnessed. Automated: initiative, passive checks, Karmic debt, approval changes.

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Choose a dialogue reply (constant) | none, or an ability check | branches, approval, quest flags | each conversation |
| Make a check, Add Bonus first (constant) | spell slot/item/consumable if used | +bonus before d20 + mod vs DC [V3 BGw/Dice_rolls] | persuasion/deception/intimidation moments |
| Pick which party member speaks (frequent) | none | uses that member's modifier | before a check |
| Attack/cast/ability (constant in combat) | Action, spell slots | damage, control [V3 BGw/Resources] | every turn |
| Bonus action / Reaction / Move (constant) | the matching resource | smaller actions, opportunity attacks | every turn |
| Stealth/hide, surprise first strike (frequent) | Stealth vs passive Perception [V3 BGw/Dice_rolls] | sneak past or open with surprise round | before fights |
| Use item/throw/shove (frequent) | action/bonus action | potions, grenades, terrain | combat |
| Short rest (frequent) | one of 2 per long rest | partial restore | between fights |
| Long rest (frequent) | 40 camp supplies (80 Tactician/Honour) | full restore, triggers camp scenes [V3 BGw/Resting] | end of day |
| Level up/multiclass/feat (per level) | XP | new features [V3 BGw/Classes] | on level gain |
| Respec at Withers (rare) | 100 gold | reset to level 1 and rebuild [V3 BGw/Withers] | after unlocking him |
| Recruit/dismiss/swap companions (occasional) | none | party of 4 [V3 DigitalTrends] | at camp |
| Steal/attack/break in (occasional) | witness risk, Attitude loss, arrest [V3 BGw/Crime] | gain items, lose trader goodwill | opportunistic |
| Save/quicksave (constant, player discipline) | none in non-Honour | undo bad outcomes | before risky checks |

#### 4. First hour, step by step
1. New game: pick an Origin or Custom, a difficulty and the 27 ability points [V3 BGw/Character_creation; BGw/Difficulty].
2. The opening cinematic ends with you infected by a mind flayer tadpole aboard the Nautiloid; you break out of a pod in the Nursery [V3 BGw/Escape_the_Nautiloid].
3. Use the Restoration device to heal; a DC 10 Investigation check shows the nursery casing is fragile [V3 BGw/Escape_the_Nautiloid].
4. Meet the githyanki Lae'zel: she says escape is by reaching the helm; the first combat tutorial follows [V3 BGw/Escape_the_Nautiloid; combat tutorial prompts [M]].
5. Reach the helm and connect the nerves of the transponder to leave the Hells [V3 BGw/Escape_the_Nautiloid].
6. The ship crashes: Act One begins on the Ravaged Beach with the "Find a Cure" quest [V3 BGw/Act_One].
7. Gather allies; companions join the active party of four; talk to each at camp [V3 BGw/Act_One; BGw/Companions].
8. Your first Long Rest discovers the camp and triggers the first camp scenes [V3 BGw/Campsite].
9. Take a short rest when HP is low (two per long rest); a long rest spends 40 camp supplies, so buy/collect supplies [V3 BGw/Resting; BGw/Camp_Supplies].
10. Keep three manual saves in rotation; do not reload merely because a conversation check failed (failures open other branches) [V3 digitaltrends.com/gaming/baldurs-gate-3-tips-tricks-beginners, undated].
11. Put a socially skilled party member forward when talking; a scout looks ahead [V3 rpgsite.net beginner guide, undated].
12. Head for the Emerald Grove, where the goblin/tiefling conflict forms the Act One political centre [V3 BGw/Act_One].

#### 5. What changes later
- Act Two: Shadow-Cursed Lands/Moonrise Towers; recruit Halsin, Jaheira, Minthara; Act Three: Baldur's Gate city, Minsc, the Netherstones, the Netherbrain finale [V3 BGw/Act_Two; BGw/Act_Three].
- Points of no return: leaving Act One, entering the Shadowfell, leaving Act Two lock out whole campsites; items left behind can be lost [V3 BGw/Campsite; BGw/Act_Two].
- Scaling: levels to 12, multiclassing, feats; Tactician/Honour raise enemy accuracy and boss actions. Long-rest content (companion arcs) keeps advancing on rest count, so rest rhythm shapes story pacing [V3 BGw/Resting].

#### 6. Failure and ending
- Party wipe: reload; Honour: continue in Custom (ends Honour) or delete the save [V3 BGw/Difficulty]. Most dialogue failures branch; some checks are scripted gates [M].
- Ending: Act Three resolves the cult and the Absolute/Netherbrain, then an Epilogue scene at camp [V3 BGw/Act_Three; BGw/Campsite]. Full ending variety `?`.

#### 7. Consequential vs cosmetic choices
- Consequential: class and race (unlock dialogue options; spell/skill access) [V3 BGw/Dialogue]; who is in the party and who you talk with (their modifiers and approval); which Act One factions you save or kill (Minthara, Halsin availability) [V3 BGw/Act_Two].
- Cosmetic: background (explicitly no dialogue or quest effect) [V3 BGw/Character_creation]; appearance.
- Dominant-ish (community): lead with a Charisma "face"; Persuasion is the most common dialogue skill (293 dialogues vs 209 Intimidation, 147 Deception, page flagged "verify") [V3 BGw/Dice_rolls; rpgsite beginner guide].
- Hidden fairness layer: Karmic Dice changes outcomes without changing displayed odds [V3 BGw/Dice_rolls].

#### 8. Open items
- V2 M4 [CONTESTED] dialogue DC display: Digital Trends (undated) says skill checks "show a die, the minimum roll needed, and your stat modifiers" [V3]; with TheGamer 2023 this leans to shown in the shipped game, against a Dec-2020 Early Access forum post. Still not confirmed from a datamine.
- V2 Karmic Dice: auto-success probability printed as p / (1 - Debt), then subtract 2(1-p); Larian's 2021-04-15 Hotfix 10 note quoted there: "loaded dice will only bend RNG in the rolling character's favour" [V3 BGw/Dice_rolls]. I did not open the forum post.
- V2 A5 (party of four) now [V3 digitaltrends]; V2 G1 initiative = d4 + Dex [V3 BGw/Turn-based_mode]; V2 J1 and K5 confirmed (40/80/120 supplies) [V3 BGw/Resting]; level cap 12 = 100,000 XP, respec 100 gold, resurrect 200 gold [V3].
- Not established: Bardic Inspiration in Add Bonus; Friends and Guidance are castable in dialogue [V3 BGw/Dialogue]; real tutorial prompt text; playtime.

### Kingdom Come: Deliverance I and II - facts line
(KCD1 tutorial/save/sleep/hardcore facts are [V3] from the KCD wiki.gg codex text; KCD2 loop details lean on Wikipedia, the Steam patch feed and two beginner guides, so KCD2 is thinner. Fandom/Prima/PCGamer were not usable.)
Aliases: KCw = https://kingdomcomedeliverance.wiki.gg/wiki (read via API; live text, KCD1-era unless stated); STM = Steam news API (app 1771300 = KCD2).
- Warhorse Studios; first-person open-world action RPG, Bohemia 1403 (KCD2) [V3 WP/Kingdom_Come:_Deliverance_II]. KCD1 2018-02-13 [per V2]; KCD2 2025-02-04, Royal Edition 2025-11-12 [per V2]. Latest KCD2 patch in the feed: 1.5.6, 2026-06-25 [V3 STM]. Hardcore Mode added by patch 1.2.4 on 2025-04-15 [V3 KCw/Hardcore_Mode].
- Assumed: KCD2 normal mode, KCD1 differences marked. One session = one in-game day (wake, errands, sleep), roughly 1-2 hours `?` [M]; a full game is far longer `?`.

#### 1. Setup choices
- **Character**: none; you are Henry (blacksmith's son, later squire). Build emerges from use, not creation [V3 KCw/Stats: "improvements come automatically simply by playing"].
- **Difficulty**: no slider found for normal play `?`. KCD1 offers "Hardcore" at new game: pick at least 2 permanent negative perks, quest autosaves off, deadlier combat, dearer trade, no fast travel, no map position [V3 KCw/Hardcore (KCD1)]. KCD2 Hardcore Mode (patch 1.2.4): pick at least 3 of 10 negative perks (e.g. Bad Back -50% carry, Numbskull 40% slower XP, Punchable Face, Menace), no map position, compass without cardinal points, no fast travel [V3 KCw/Hardcore_Mode].
- **Opening choices inside play**: dialogue approaches to the first tutorial quest (below) and, in KCD2, what to do first after the prologue [V3 method.gg/kcd2].

#### 2. The loop
Clock: continuous real-time with a day/night cycle; you can skip time by waiting (raises tiredness and hunger) or sleep (restores rest, saves only at "Sleep and save" beds) [V3 KCw/Tiredness_and_Waiting]. Menus pause the game; whether dialogue pauses the world `?` [M].
1. Pick a quest from the journal or talk to NPCs; KCD1 has 29 main quests (4 side quests folded in) plus separate side quests and activities [V3 KCw/Kingdom_Come:_Deliverance_quests]; ordering freedom after the opening `?`.
2. Travel on foot or by horse; fast travel via the map generates road encounters (KCD2: a percentage chance to avoid hostiles; failing forces a fight) [V3 WP/Kingdom_Come:_Deliverance_II].
3. Meet an NPC: a timed branching dialogue with stat icons (Speech, Charisma, Strength/Intimidation) beside options [per V2].
4. Resolve by words, stealth, theft, money or force; real-time melee has five attack zones, block, feints and stamina [per V2 KCw/Combat].
5. Witnessed crime brings guards: pay a fine, serve time, talk your way out, flee or fight; KCD2 adds caning, branding, pillory [V3 WP/KCD2; per V2 KCw/Crime].
6. Maintain Henry: eat (below 50 nourishment: less stamina, then health loss), sleep (tiredness cuts Speech and Charisma), clean and repair gear [V3 KCw/Hunger; KCw/Tiredness].
7. Save: Saviour Schnapps (a brewed or bought potion), or sleep and save in a bed, or quest autosaves; Save & Exit allowed once [V3 KCw/Saviour_Schnapps; KCw/Tiredness_and_Waiting].
Automated: NPC schedules, reputation updates, stat XP from use. Interrupts: ambushes, witnessed crimes, timed dialogue.

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Choose a dialogue approach (constant) | time limit on options; stat icons | persuade, charm, intimidate, bribe or fight | each conversation |
| Fight (constant) | stamina, health, gear wear | zone attacks, blocks, perfect block, Master Strike | bandits, duels, arena |
| Sneak/knock out/steal (frequent) | noise, visibility | avoid fights, gain gear | camps, houses |
| Pickpocket/lockpick (frequent) | skill minigame; failed picks may wake sleepers | loot; crimes if seen | when skilled |
| Eat/drink (constant) | food, money | keeps stamina and health | when hungry |
| Sleep or wait (daily) | rent a bed 2 groschen or buy for 250 (KCD1) [V3 KCw/Tiredness_and_Waiting] | rest, maybe save | evening |
| Save (constant) | Saviour Schnapps (base price 100 groschen in KCD1) [V3 KCw/Saviour_Schnapps] | manual save | before risk |
| Trade/haggle (frequent) | reputation with the merchant | prices; stolen goods marked | after loot |
| Read / train with a master (occasional) | hours or money | skill gains | down time |
| Pick a perk (rare) | main-level perk points; KCD1 every second Main Level [V3 KCw/Main_Level] | permanent modifier | on level up |
| Fast travel (frequent) | encounters, hunger/tiredness | skip distance | long trips |
| Respond to arrest (rare) | fine, jail days, branding | clears or escalates the crime | after being caught |
| Alchemy/brew (occasional) | herbs and bench time | potions, schnapps | prep |

#### 4. First hour, step by step (KCD1 tutorial quest "Unexpected Visit")
1. Your mother wakes Henry; eat breakfast because hunger harms abilities [V3 KCw/Unexpected_Visit].
2. Meet your father Martin at the forge; he gives an errand list (charcoal 0/10, collect Kunesh's debt, pick up a cross-guard, buy ale) [V3 KCw/Unexpected_Visit].
3. Collect the crossguard from the castle guards [V3 same].
4. Train with Combat Master Vanyek: slashing 0/5, stabbing 0/3, chain strikes 0/3 [V3 KCw/Unexpected_Visit].
5. Confront Kunesh about the debt: fight him, pass a Speech or Intimidation check, or find items to sell; losing a check means a fight; your mother patches wounds [V3 same].
6. Buy ale at the tavern; do not let it get warm [V3 same].
7. Join friends in the Deutsch-house prank, then run from the catchpole [V3 same].
8. Return to the forge and deliver the errands; the town is then attacked in "Run!" (quest 2) [V3 KCw/Kingdom_Come:_Deliverance_quests].
9. Several quests later "Train Hard, Fight Easy" teaches blocks, zone change, perfect block at three speeds, dodge and feints with Captain Bernard [V3 KCw/Train_Hard,_Fight_Easy].
10. Learn to save: brew or buy Saviour Schnapps, or sleep and save in a bed you own or rent [V3 KCw/Saviour_Schnapps].
11. KCD2 start: after the prologue Henry is "stranded in the middle of the map"; early targets are recovering horse Pebbles and dog Mutt, finding schnapps, and the blacksmith tutorial [V3 method.gg/kcd2/kcd2-beginners-guide, undated]. A free bed and personal chest at the Tachov blacksmith or Nebakov Mill [S3 search snippet, gfinity/windowscentral not opened].

#### 5. What changes later
- Stats climb with use: Strength, Agility, Vitality from combat, Speech from talking; KCD1 caps at Main Level 20 (all four stats 20) [V3 KCw/Level_cap]; KCD2 stats/skills/Main level cap 30 [per V2 Fextralife]. Perks reshape play (carry weight, stamina, reputation gains, hunger) [V3 method.gg].
- KCD2 adds crossbows and early firearms, mounted shooting, branding/pillory, two large regions (Wikipedia: twice KCD1's size; method.gg: about 125% larger; minor [CONTESTED]) [V3 WP; method.gg].
- Reputation per town and crime history accumulate; Hardcore tightens saves and economy [per V2 KCw/Reputation; V3 KCw/Hardcore].

#### 6. Failure and ending
- Death reloads the last save; losing progress is the real cost of rare saves. KCD2 punishments (caning, branding) persist as social penalties [V3 WP/KCD2; per V2]. Quest failure when key NPCs die or you refuse [M].
- KCD2 "concludes Henry's story" with the war against Sigismund [V3 WP/KCD2]; KCD1's 29th and last main quest is "Epilogue" [V3 KCw/Kingdom_Come:_Deliverance_quests]. Recovery: yes by reload; Hardcore removes quest autosaves [V3 KCw/Hardcore].

#### 7. Consequential vs cosmetic choices
- Consequential: how you build by doing (what you train is what you become); how you dress and wash (Charisma averages visible clothing; dirt and blood lower it) [per V2]; whom you rob where you can be seen; reputation per place; saving habits.
- Cosmetic: clothing colour and many minor perks; the first-day prank branch (outcomes minor) [M].
- Dominant answer (community consensus): focus on one weapon type; sword Master Strike is strongest [V3 method.gg: Master Strike "only available with swords"] - CONTESTED against V2's "per weapon class".
- How I know: wiki effects and method.gg advice, not sims.

#### 8. Open items
- V2 G3: KCD1 manual save item is Saviour Schnapps (a potion), also "Sleep and save" beds; Hardcore disables quest autosaves; KCD2 allows autosave, own beds and Schnapps but no quicksave [V3 KCw/Saviour_Schnapps; KCw/Hardcore; V3 destructoid.com/all-ways-to-save-in-kingdom-come-deliverance-2 undated]. Camp beds: Destructoid says no, one search snippet says yes [CONTESTED].
- V2 K3: Tiredness lowers Speech and Charisma already in KCD1 [V3 KCw/Tiredness], not only KCD2. V2 A2 hardcore: KCD1 also has Hardcore (>=2 negative perks) [V3].
- V2 Master Strike "per weapon class" vs method.gg "only swords" [CONTESTED]. Perk cadence still `?` for stat perks; Main Level perk every second level in KCD1 [V3 KCw/Main_Level].
- Not found: a normal-mode difficulty setting; KCD2 save details beyond Destructoid; real session length. KCD2 punishment numbers still [S2].
- Attachment grep: zero KCD, Griftlands, Disco or BG3 hits (see Disco item).
