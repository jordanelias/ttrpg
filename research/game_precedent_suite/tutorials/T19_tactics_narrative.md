# T19 - Tactics & narrative-choice games: how they are played (tutorial pass v3)

Four games: Triangle Strategy, Unicorn Overlord, Ace Attorney (Phoenix Wright trilogy), Lacuna. No v2 capability tables exist for these four, so section 8 fills nothing; each game carries one capability-id line (groups B, D, G, H, I, L) tagged. Tags: [V3 url date/version] read in a fetched page body this session; [S3 url] search snippet only; [M] memory; `?` not established; [CONTESTED] sources disagree. Fandom pages were read through the MediaWiki api.php (the revision date is given). Written 2026-10-22.
Cross-game note on "evidence decay" (REPO_MENTIONS s.3): I found no evidence that decays in any of the four; clues persist in the Triangle Strategy War Chronicle, the Ace Attorney Court Record and the Lacuna phone log, and Unicorn Overlord has no evidence layer [absence, not proven; V3 for the persistent logs].

### Triangle Strategy - facts line
Square Enix and Artdink (Square Enix publishes; Nintendo published the Switch version outside Japan until Dec 2024); turn-based tactical RPG with a branching story. Switch 2022-03-04, Windows 2022-10-13, Quest 2024-10-31, PS5/Xbox 2025-08-20 [V3 en.wikipedia.org/wiki/Triangle_Strategy 2026-10-22]. Patch number relied on: `?` (wiki revisions 2022-2024, Game8 pages 2026). Assumes the first playthrough on default difficulty. Campaign aimed at about 50 hours [V3 Wikipedia]; one sitting = one chapter or part, about 1-3 hours [M], and "a battle is often followed by over an hour of cutscenes" (Eurogamer, quoted on Wikipedia) [V3].
Capability ids (B,D,G,H,I,L): B1 PART (8 War Council members + optional recruits as roster) B2 PART (recruits unlock by conviction thresholds or route) B3 NO B4 NO B5 NO B6 NO B7 NO | D1 PART (vote picks a policy-like path) D3 YES (War Council advises/votes) D5 YES (Scales vote) D6 PART (authored scenes) | G1 YES (grid, height, facing) G2 PART G3 PART (fallen unit; mortality by chapter script) G4 PART G5 PART | H1 YES (persuasion before vote) H2 PART (Serenoa's 3 values, no pairwise opinion) H4/H6 PART (authored) | I1 PART (info items) I2 NO I3 NO I6 PART | L1 PART (fixed named cast) L2 NO L3 NO L4 NO L5 NO [V3 for the vote/recruit/battle facts below; the rest [M] and marked judgments].

#### 1. Setup choices
- Almost none. Protagonist, party and nation are fixed (Serenoa Wolffort of House Wolffort, Glenbrook, continent Norzelia) [V3 Wikipedia].
- Difficulty: the demo feedback added "additional difficulty modes" [V3 Wikipedia]; names and effects of the modes `?` (Game8 has a "Difficulty Mode Differences" page; not opened). Higher difficulty yields more Kudos [V3 game8.co/games/Triangle-Strategy/archives/368777 2026].
- New Game Plus (after the first ending): "increased difficulty level", makes conviction totals and the per-choice point notices visible, which are hidden on a first run [V3 Wikipedia; V3 game8 archives/370009]. Everything that shapes the story afterwards is made in play, not at setup.

#### 2. The loop
1. Story scenes. A chapter opens with a menu of scenes (the Chapter VII example offers one, then four, then one, then one); side-story scenes are skipped if not played before the main one [V3 fandom Chapter_VII_(Trial_Version) rev 2024-02-07].
2. Dialogue choices. At marked prompts three answers each add 50 to one hidden conviction (Morality, Liberty, Utility) [V3 fandom Conviction rev 2022-05-22; game8 370009].
3. Exploration phase (before a battle). Walk a town or the battle map, talk to NPCs, pick up items, collect "information" for the War Chronicle; some actions change the coming battle (a repair, a trap) [V3 fandom Battle rev 2022-02-13; War_Chronicle_-_Information rev 2024-11-14].
4. Encampment (after chapter 1 or so, `?`): shops, weapon upgrades with coin plus materials, the Sundry Shop (Kudos for Quietuses), mock battles [V3 fandom Encampment rev 2024-04-16].
5. Battle preparation: choose and place the deployed units; each battle shows a recommended level and units, and following or ignoring that recommendation moves convictions [V3 fandom Conviction].
6. Tactical battle: turn order by speed shown along the bottom; one tactical point (TP) gained per turn pays for skills; height, back attacks, follow-up ("giving chase") attacks [V3 fandom Battle].
7. After the battle, back to scenes; at some chapters a vote opens (item 8).
8. Scales of Conviction. The wiki lists 10 votes (Chapters III, VII, VIII twice, IX, X, XI, XIII, XV, XVII; the last three have three options), each option tagged with a conviction colour. 6-7 party members vote; each has a printed initial stance or is Undecided; the player talks to the ones who disagree, then the Scales tip by majority [V3 fandom Voting rev 2022-03-26; Tilting at Pixels review].
Automated: unit AI of enemies and allies not under control, vote tally, the story branch that follows, conviction accumulation (hidden). Interrupts: none are random; every branch is authored.

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Move/Attack/Skill | TP (1 per turn gained; magic often 2) | damage, status, terrain play | constantly |
| Position (height, flank, rear) | the move itself | back attack is a guaranteed crit; chase attack by a unit behind the target | constantly |
| Quietus | 100 Kudos per slot, once per battle | revive, heal, move an ally 8 squares | a few per battle |
| Choose dialogue answer | none visible | +50 to one hidden conviction | each prompt |
| Talk (exploration) | time only | info, items, NPC colour | every exploration phase |
| Persuade a voter | one attempt per voter (Tilting at Pixels) | may flip one vote | each Scales chapter |
| Cast the tie-break vote | none | Serenoa's second vote when the vote ties | rarely |
| Deploy recommended/other units | opportunity | moves Utility vs Liberty | every battle |
| Weapon upgrade / class promote | coin + materials | stat and skill unlock | between chapters |
| Mock battle (tavern) | none | +2 Morality, coin, materials | optional farming |
| Buy/sell at shops | coin | +8 Liberty per 10,000 coin spent; +8 Utility per 5,000 sold | optional [V3 fandom Conviction] |
| Retry a failed battle | time | restart the battle | on defeat |
Constant: attack/move/position. Rare: Quietus, tie-break. [V3 for the rows with a URL above; Persuade-once: V3 tiltingatpixels.com/post/Triangle-Strategy-Review/]

#### 4. First hour, step by step
1. Start Chapter I "A Young Hawk Soars": Serenoa and Roland rescue a young Aesfrosti woman, Frederica, from bandits [V3 fandom Chapter_I rev 2023-09-20].
2. The first dialogue prompts (the bandit leader, Frederica's hair) are the first conviction picks: three answers, one per conviction; the game does not label them [V3 fandom Chapter_I; imore.com article].
3. First battle "Beset by Brigands" at the harbour: 5 Bandit Rogues, 1 Bruiser plus two named bosses; victory = destroy the enemy, defeat = lose all allied forces [V3 fandom Chapter_I].
4. In-game tutorial pop-ups exist for enemy attack range (purple tiles, red arcs), weaknesses ("weak" over a target), backstabs and chase, loot and quietus; when each fires `?` [V3 fandom Battle captions].
5. Use back attacks and follow-ups; use Serenoa's Delayed Attack to limit Travis [V3 fandom Chapter_I].
6. Chapter II: the Tourney; six more dialogue prompts (a child hiding, the tourney strategy) [V3 fandom Chapter_II rev 2023-09-20].
7. Gather information from NPCs in the Chapter II exploration (Aesfrost, Hyzante, the Ice Mage...) - these are stored in the War Chronicle and later feed votes [V3 fandom War_Chronicle_-_Information].
8. Chapter III Part I: the first Scales vote (Aesfrost vs Hyzante). Anna starts undecided [V3 fandom Voting].
9. Pre-vote: talk to every voter who disagrees with you and choose among their dialogue options; intelligence gathered in Chapter II (e.g. "The Ice Mage") adds a third option [V3 nightlygamingbinge.com Chapter III walkthrough (fetch summary)].
10. Interact with the Scales: majority picks the destination; the choice sets whether a Frost Mage or a Hunter can be recruited, and convictions matter [V3 same walkthrough].
11. Part II goes to Aesfrost or Hyzante accordingly: different maps, battle, recruit.
12. Spend Kudos at the Sundry Shop, upgrade weapons, do a mock battle.

#### 5. What changes later
- More recruits: 14 optional recruits unlock at set conviction totals (110 to 1,600 points) and do not vote [V3 fandom Character rev 2024-01-05]. 8 story recruits are gated by route and chapter choices (Chapter 3 destination gives Corentin or Rudolph; six more later, one also needing 750 Morality and 1,050 Liberty) [V3 same page].
- The votes get heavier (surrender or protect Roland; deliver or defend the Roselle; a three-option vote at Chapter 13) [V3 fandom Voting].
- Mid game "collapsing timeline": branches rejoin, then the last vote chooses one of three finales; a fourth "Golden Route" needs specific votes (Game8 lists six choices; the Chapter 17 "Find another way" option appears only if all conditions are met) [V3 Wikipedia; V3 game8 archives/368777].
- Pressure: battles escalate; the hardest mock battles are level 50 and need later playthroughs (4+ to unlock all) [V3 fandom Mental_mock_battles rev 2023-11-28].

#### 6. Failure and ending
- Battle defeat: Chapter I lists "Lose all allied forces"; other battles list their own defeat conditions `?`; a lost battle is retried [V3 fandom Chapter_I; Tilting at Pixels "retrying the battle"]. Rules for a single fallen unit `?` ([M]: a countdown to revive).
- Story failure does not exist; every vote result is a valid path. Four endings (three plus Golden) [V3 Wikipedia]. The reviewer notes the first ending is a letdown and the Golden route is "very unlikely" to be found blind [V3 tiltingatpixels.com].
- A settled vote is redone only by reloading an earlier save or playing New Game Plus, which lets you see how decisions change the branch [V3 Wikipedia for NG+; reload is [M]].

#### 7. Consequential vs cosmetic choices
- Consequential: the Scales results, which set which scenes and recruits you get; the final vote picks one of three endings [V3 Tilting at Pixels: "all of these tough decisions do not affect the conclusion" except the final set]. 
- Consequential and hidden: your conviction totals decide who you can recruit and how easily a given voter flips [V3 game8 370009; fandom Character thresholds].
- Cosmetic: most dialogue answers beyond the +50 (the line itself).
- Dominant: Golden Route is a known fixed answer list in guides [V3 game8 368777, community consensus]; one player reports the early vote was "easily a 7-0" (anecdote, [V3 steamcommunity.com/app/1850510/discussions/0/599651305036722298]); a vote option also adds +20 to its conviction when voted [V3 fandom Conviction].

#### 8. Open items
- Difficulty names; patch number; Encampment unlock chapter; single-unit death rule `?`.
- Persuasion maths: GameFAQs community example (Roland needs 318-529 Morality depending on the argument) comes from a search summary only [S3 gamefaqs.gamespot.com/boards/313526-triangle-strategy/80063098]; page returned 403 here.
- Repo claims (REPO_MENTIONS s.3): "three hidden conviction axes per character" is WRONG as stated: the three axes (Morality, Liberty, Utility) are Serenoa's own totals, one set for the whole run and hidden until New Game Plus; each voter instead has a visible printed stance and a hidden persuasion threshold [V3 game8 370009; steamcommunity.com/sharedfiles/filedetails/?id=2984474233; tiltingatpixels.com review (UI shows where allies stand)]. "Convictions gate which arguments you may attempt" is partly true: info items add an argument; thresholds decide whether an argument succeeds. "Wrong appeal = flat fail" is only [S3] (some arguments never work regardless of conviction). "Fixed roster" is right for voters; optional recruits are conviction-gated.

### Unicorn Overlord - facts line
Vanillaware; published by Atlus (Japan) and Sega (worldwide); real-time-with-pause tactical RPG with an automated squad-vs-squad combat layer. Released 2024-03-08 on Switch, PS4, PS5, Xbox Series; no Windows version as of Wikipedia 2026-10-22 [V3 en.wikipedia.org/wiki/Unicorn_Overlord]. Version: launch patch Ver. 1.01 (added NORMAL difficulty and moved the old trial "CASUAL" to NORMAL); the wiki's patch list ends at Ver. 1.04 (2024-04-22), later patches `?` [V3 unicornoverlord.fandom.com Patch_Notes rev 2024-04-22]. Assumes NORMAL. One stage = about 3-5 real minutes (some about 1) [V3 fandom Battle_Stages rev 2025-07-13]; a sitting is a handful of stages plus overworld upkeep; main story 45-50 hours [V3 thenerdstash.com starter guide, "early information"].
Capability ids (B,D,G,H,I,L): B1 YES (about 70 unique characters plus generic hires) B2 YES (quests, spare-or-kill recruits, mercenaries bought with Honors at forts; dismiss at forts) B3 PART (choose a unit leader; post one guard per town) B4 PART (guards earn gold and forage; otherwise the player moves squads) B5 YES (per-character Tactics) B6 NO B7 NO | D1-D6 NO (no policy layer; rebuilding towns by delivery is the only civic act) | G1 PART (auto-resolved clashes; the player steers squads) G2 PART G3 `?` G4 NO G5 NO | H1 NO H2 PART (rapports) H4 PART (late choice of partner) H5/H6 NO | I1 NO I3 NO I4 NO I6 PART (enemy squad shown before engaging) | L1 PART (authored cast) L2 NO L3 NO L4 NO L5 NO [V3 for the facts in sections 1-6; B6, G3 and the NO rows are absences I did not find, not proven absent].

#### 1. Setup choices
- Difficulty: CASUAL, NORMAL (Ver. 1.01), and a harder "True Zenoiran" mode unlocked after one clear (in it the Hallowed Corne Ash is replaced by a weaker Luminous Corne Ash) [V3 fandom Patch_Notes; Hallowed_Corne_Ash rev 2024-03-17]. A middle "Hard" `?`.
- No character creation for the lead: Alain is fixed. Customisation is by hiring: at a fort you pick the mercenary's class, name, stat-growth type (Hardy, Offensive, Defensive, Precise, Lucky, Keen...), equipment and hair colour [V3 fandom Hiring_Mercenaries rev 2025-11-23].
- Story levers chosen in play: spare or kill certain defeated enemies (affects recruits and later events) [V3 Wikipedia]; the region order is partly free [V3 Wikipedia]; at the end the choice of partner and whether to visit all six sanctuaries (three endings) [V3 Wikipedia].

#### 2. The loop
1. Overworld (no timer, pausable at will): walk Alain's army over the map; take quests; pick up items and forage sites (they refill after some stages); roaming enemy sprites can be fought [V3 rpgsite.net/news/15121 (Atlus preview, pre-launch); fandom Foraging_sites].
2. Prepare: edit units (leader, formation grid, equipment, Tactics); the stage preview shows an outcome prediction [V3 thenerdstash starter guide].
3. Enter a Battle Stage: deploy squads from your blue-flag bases, each deployment costing Valor Points; there is a time limit [V3 rpgsite.net/news/15481; fandom Battle_Stages].
4. Real-time field phase: order squads to move (destinations, waypoints, group select); capture towns and forts on the way to open new deployment points and rest spots [V3 fandom Battle_Stages; nerdstash].
5. Contact: when two squads meet, an automatic exchange runs: combatants act in Initiative order using Active Skills (cost AP) and reactive Passive Skills (cost PP); it ends when both sides run out of AP or one is wiped; the loser is knocked back into a waiting state and can be hit with a First Strike [V3 rpgsite 15481].
6. Between contacts: swap places with a nearby ally, rest (recovers stamina but leaves the unit defenceless), spend Valor on class Valor Skills [V3 rpgsite 15481].
7. Stage ends on objective or failure; rewards in Gold, Honors, Renown; Valor refills from kills and liberations [V3 rpgsite; fandom Renown rev 2025-11-28].
8. Back on the map: spend Honors and Renown (the Expand, Hire and Promote rows below), deliver items to rebuild towns, post guards. Repeat region by region.
Automated: all fighting after contact (by Tactics), guard income and foraging, Optimize for Tactics and gear. Interrupts: encounter fights and stage failure (section 6).

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Move squad (destination/waypoints) | none, but a squad at 0 stamina cannot move | positions, capture points | constantly |
| Engage / Battle | stamina, and AP/PP spent in the exchange | triggers the auto-fight | constantly |
| Set Tactics (priority list, up to 2 conditions each) | free | scripts each character | every new unit, often re-tuned |
| Formation and leader | free | row/column matter; leader's effect applies to the squad | before each stage |
| Swap / First Strike / Rest | Stamina, time | tempo | frequently |
| Valor Skill | Valor | class effect | when a fight turns |
| Deploy another squad | Valor | reinforces | per stage |
| Optimize | free | auto Tactics and gear | when unsure |
| Expand unit number / size | Honors (e.g. size 3 costs 10, size 5 costs 200 and Renown A) | more squads, more members | at forts |
| Hire mercenary | Honors (Renown D to unlock) | custom character | at forts |
| Promote class | Honors 25-30 etc., Renown B | stronger class | rarely |
| Deliver goods / rebuild a town | items | Renown, shops, inn, fast travel | on liberating |
| Station one guard per liberated town | a character slot | gold and materials after each stage | each town |
| Spare or kill; accept quests | story | recruits, endings | occasional |
Costs: [V3 fandom Expanding_Units rev 2024-10-25; Renown; Class_Promotion rev 2024-03-31]. Wiki counts of squads at start conflict (see 8).

#### 4. First hour, step by step
1. Pick a difficulty (NORMAL) and start; watch the prologue: Valmore's coup, Alain smuggled out [V3 fandom Prologue; Wikipedia].
2. Ten years on, the first stage is the defence of the isle of Palevia against a Zenoiran raid; the on-screen tutorial wording `?` ([M]: it teaches moving a unit and engaging) [V3 Wikipedia plot].
3. Open the unit screen and read its parts: characters, formation, leader, equipment, Tactics [V3 thenerdstash.com starter guide].
4. Leave Tactics on defaults or press Optimize; with none set, a character just hits the enemy in front [V3 rpgsite 15481].
5. Reach Cornia and take the early quests (The Unicorn Ring, The Ravaged Swamp at Fort Groux, The Priestess, Abducted) [V3 fandom Quests rev 2025-09-13].
6. Before each fight shuffle the formation and watch the outcome prediction [V3 nerdstash].
7. Keep two squads close so a pushed-back enemy is open to a First Strike [V3 nerdstash].
8. Use a fast cavalry leader to liberate towns and points of interest, opening deployment and rest spots [V3 nerdstash].
9. Liberate a town, make the 1-3 repair deliveries and post a guard [S3 search summary of GameWith/Sportskeeda/GameSpot for "1-3"; V3 fandom Station_a_Guard rev 2024-03-18 for the guard rule].
10. At a fort spend Honors on unit size first, then unit count (beginner consensus, [S3]); costs [V3 fandom Expanding_Units].
11. Recruit generously, including spared enemies [S3].
12. Hire mercenaries once Renown reaches D [V3 fandom Renown].
13. Clear a region's battle stage before roaming on [V3 nerdstash].
14. Save Valor for Valor Skills rather than healing [S3].

#### 5. What changes later
- Renown ranks E to S gate unit count (to 10), unit size (to 5), promotion (B), and raise battle rewards from x1.0 to x2.0 [V3 fandom Renown].
- Four more nations after Cornia (Drakenhold, Elheim, Bastorias, Albion), then the siege of the Cornian capital Gran Corrine [V3 Wikipedia]; per-nation classes are shown on the wiki class list [V3 fandom Classes rev 2025-11-21]. Sanctuary pilgrimage unlocks the best ending [V3 Wikipedia].
- Extra systems: Coliseum (arena fights, coin exchange), siege weapons and traps, online AI-squad matches [V3 Wikipedia; fandom Coliseum].
- Pressure: bigger enemy formations, tight timers, classes that counter yours (a weapon-style triangle between classes) [V3 fandom Classes rev 2025-11-21].

#### 6. Failure and ending
- Stage Game Over: time limit expires, your command post is taken, or your army is wiped; one Hallowed Corne Ash prevents it (extends the timer, makes the enemy leave the base, or revives a wiped squad) [V3 rpgsite 15481; fandom Hallowed_Corne_Ash].
- Losing a roaming encounter sends you back to Liberation territory; the stage can be retried (retry of conditional stages added in 1.04) [V3 rpgsite 15121; Patch_Notes]. Permanent loss of characters: only missable recruits, not battle deaths `?` [V3 fandom Unique_Characters rev 2024-04-21 for "some can be missed permanently"].
- Ending: three endings by the final fight and the sanctuary pilgrimage [V3 Wikipedia].

#### 7. Consequential vs cosmetic choices
- Consequential and checked: Tactics priority order and the formation. The Atlus preview shows an unconditional "Slice" placed first means Heal is never used; fix by putting narrower conditions higher [V3 rpgsite 15481].
- Consequential: which Honors you spend on (size before count is community advice, not a measured result) [S3].
- Consequential for story only: spare-or-kill, sanctuaries, partner.
- Cosmetic (my reading): mercenary name and hair colour. Optimize is offered as a fallback for players who find hand-tuning overwhelming [V3 rpgsite 15481]; whether it matches a good hand-set priority list `?`.

#### 8. Open items
- Squad count at start: wiki Expanding_Units says you start with 3 units; the Renown table says D "expands unit number to 3"; Wikipedia says early units hold 2 characters. [CONTESTED]; `?`.
- Maximum members: 5 [V3 Wikipedia; rpgsite 15121; fandom]; The Nerd Stash says six characters [CONTESTED, rejected: it conflicts with Atlus text]. Grid shape 2x3 [M].
- Whether guard stationing defends against recapture: sources only mention income and foraging; `?`.
- Repo claims: (a) "Unicorn Overlord tactics are all conditional" (squad-engagement-concept-v5.md:226) is WRONG: each tactic has up to two condition slots, and an always-firing Slice is the Atlus example (and the default with none set is attack the one in front) [V3 rpgsite 15481; fandom List_of_Tactics shows N/A conditions]. (b) "Garrison is an assignment on existing units" (companion X5; 4/4 convergence): TRUE here, with the nuance that a station guard is one character per town who can still deploy, and the wiki says its effect is income and foraging [V3 fandom Station_a_Guard]. (c) "Squad composition and leader assignment | class synergy | squad size" matches [V3 fandom Classes leader effects; Expanding_Units]. (d) "Pure on-behalf" (companion part7): consistent with what I read, since I found no policy or social layer, but that is an absence, not a proof.

### Ace Attorney (Phoenix Wright: Ace Attorney Trilogy) - facts line
Capcom (with Digital Works Entertainment for the 2019 build); visual-novel adventure with a courtroom puzzle layer. This tutorial uses the 2019 multi-platform Trilogy (Switch/PS4/Xbox One/Windows; Steam 2019-04-09; mobile 2022-06-10) containing 14 episodes of the three games (2001, 2002, 2004), including the Nov 2025 title update [V3 en.wikipedia.org/wiki/Phoenix_Wright:_Ace_Attorney_Trilogy 2026-10-22; V3 store.steampowered.com/api/appdetails?appids=787480; V3 Steam news 2025-11-19]. Assumes Game 1 played in order, no Story Mode. One sitting = one act (an investigation day or a trial day); an episode is a few such acts; hours per episode `?` (the first episode is the shortest in the series [V3 aceattorney.fandom.com The_First_Turnabout rev 2026-08-22]).
The Great Ace Attorney was not used; its "dance of deduction" and different icon penalty are noted only where the wiki compares them.
Capability ids (B,D,G,H,I,L): B1-B7 NO (no roster; Maya/Mia/Gumshoe assist by script) | D6 PART (an authored courtroom trial; verdict is Guilty or Not Guilty; D1-D5 NO) | G1-G5 NO | H1 YES (press and present dialogue, multiple-choice answers) H2 NO H3 NO H4-H6 NO | I1 YES (Examine/Talk/Move/Present in investigation) I2 YES (player finds the statement/evidence contradiction) I3 NO I4 NO I5 PART (witnesses lie; Psyche-Locks mark hidden secrets) I6 YES (the truth is authored and hidden) | L1 PART (authored cast, no sim) L2-L5 NO [V3 for I1, I2, I5, D6 below; NO rows are absences, [M] otherwise].

#### 1. Setup choices
- Which game and episode: Game 1 first; the Nov 2025 update added Episode Selection, Story Mode (solve cases automatically) and Auto-play of dialogue, so a player can now opt out of the puzzle and failure layer [V3 Steam news 2025-11-19, steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1816849002006239].
- Language and audio/text options (more save slots, skip dialogue) [V3 Wikipedia Trilogy]. No difficulty, no character creation; the protagonist, the evidence and the culprit are fixed.

#### 2. The loop
Clock: story days with timestamps inside an episode; no real-time pressure. Each episode is a sequence of acts: Investigation Day, Trial Day, sometimes more [V3 fandom Turnabout_Sisters acts list].
1. Opening cutscene, often showing the crime [V3 Wikipedia Phoenix_Wright:_Ace_Attorney].
2. Investigation act (from Episode 2 on): at each location pick one of Examine, Move, Talk, Present; gather evidence and profiles into the Court Record; talk topics unlock as you progress. In Games 2-3 the magatama can be shown to someone with Psyche-Locks [V3 fandom Investigation rev 2024-12-06].
3. The act ends when the game decides you have enough, then the story moves to court [V3 Wikipedia].
4. Trial act: the prosecutor calls a witness who testifies; then a cross-examination of that testimony statement by statement.
5. Per statement the player may Press (ask for detail; free, usually) or Present an item from the Court Record against it; the judge also asks questions that need a multiple-choice answer or a presented item [V3 fandom Trial rev 2026-05-31].
6. Wrong present or wrong answer: a penalty cuts the Confidence Gauge; empty = guilty verdict and Game Over [V3 fandom Penalty rev 2026-04-18; Game_Over rev 2026-08-26].
7. Right present: the statement collapses, the witness changes testimony, new evidence or a new witness appears, and play loops to step 4 until the culprit breaks down.
Automated: all NPC behaviour, the culprit, branching (nearly none), and the checking of every pair. Interrupts: none are random; the game controls pacing.

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Examine (point and click) | none | finds evidence, adds to Court Record | constantly in investigation |
| Move | none | change location | constantly |
| Talk (topic list) | none | testimony, unlocks topics | constantly |
| Present evidence/profile to a person | usually none; Psyche-Lock attempts risk the gauge | unlocks dialogue or breaks a lock | often |
| Magatama (Games 2-3) | gauge risk | shows Psyche-Locks (a mark that a secret exists; 1-5 locks) | when a witness is evasive |
| Court Record (view) | none | read items | constantly |
| Press a statement | usually none; a few have penalties | more detail, changes testimony | on every statement |
| Present against a statement | wrong = penalty (20% in Game 1) | collapses a lie | on the key statement |
| Answer a question / present proof | wrong = penalty, sometimes shown beforehand | advances the argument | when asked |
| Pick a branch (rare) | none | e.g. "Ease her fears" or "Push her hard" in Turnabout Sisters | rarely |
| Save / restart act | none | recover | after Game Over |
Constant: Examine/Talk/Press/Present. Rare: branches. [V3 fandom Investigation; Trial; Penalty; Turnabout_Sisters trivia]

#### 4. First hour, step by step
1. Start Game 1 (Episode 1 "The First Turnabout"): a one-act trial, "the shortest in the series" and a tutorial [V3 fandom The_First_Turnabout].
2. In the defendant lobby, receive the autopsy report from Mia, your mentor; it enters the Court Record [V3 same page].
3. Court opens; the judge tests you on basic case details with questions [V3 same page].
4. The prosecutor presents the murder weapon (a statue called The Thinker) and the passport as evidence; study them in the Court Record.
5. Witness Frank Sahwit testifies that he found the victim at 1:00 p.m. Read each statement with the next/previous buttons [V3 fandom Trial].
6. Press statements (Press is not formally taught until Episode 2 and is optional here) [V3 fandom The_First_Turnabout].
7. Present the autopsy report on the "1:00 p.m." statement: time of death 4:00 p.m. contradicts it. First "Objection!".
8. Continue: his TV excuse contradicts the blackout record; his clock excuse leads to the statue's clock function.
9. Final present: the passport (Paris, nine hours) explains the three-hour offset [V3 fandom The_First_Turnabout trial summary].
10. Sahwit breaks down; verdict Not Guilty. Episode 2 "Turnabout Sisters" introduces investigation chapters and Press [V3 fandom Turnabout_Sisters].
11. Day 1 Investigation: Move/Examine/Talk/Present at the detention centre and scene; collect evidence for the next day's trial.
12. Day 2 Trial against Edgeworth; the penalty gauge refills at the start of each act in Game 1 [V3 fandom Penalty].

#### 5. What changes later
- Game 2 (Justice for All) adds Psyche-Locks and the magatama, lets profiles be presented anywhere, and moves from five icons to a variable Confidence Gauge that carries over between acts; breaking a person's locks recovers 50% [V3 fandom Penalty; Investigation].
- Game 3 uses the same gauge and magatama rules [V3 fandom Penalty]; trials get longer with more witnesses [M]. The 2019 builds redraw the gauge as 10 segments [V3 fandom Penalty "Segmented Confidence Gauge"].
- Later games (not in this tutorial) add Apollo's bracelet, Athena's Mood Matrix, Revisualization [V3 fandom Trial].
- Pressure: penalty size becomes variable (steps of 5% in the original builds); a few moments are harsher, e.g. in Turnabout Goodbyes (Episode 4) refusing to examine a photo enlargement is an immediate guilty verdict, and in Bridge to the Turnabout the prosecutor threatens the entire gauge [V3 fandom Penalty]. Longer chains of evidence [M].

#### 6. Failure and ending
- Loss: depleted gauge = the judge declares Guilty; in the older games it goes back to the title screen, while from Dual Destinies on you can resume at the failure point [V3 fandom Game_Over]. For the Trilogy build, whether Game Over resumes at the point of failure `?`.
- Magatama failure: the lock-breaking process stops and you restart it, no Game Over [V3 fandom Game_Over].
- Win: Not Guilty and the real culprit named; each episode ends in a fixed outcome. Recovery: unlimited retries; Story Mode removes failure [V3 Steam news 2025-11-19].

#### 7. Consequential vs cosmetic choices
- Consequential: choosing the right statement and right item; one pair per beat is the intended solution (my reading of the cross-examination loop [V3 fandom Trial]).
- Consequential and dominated: the penalty is a bounded, refilling resource, so a wrong guess is cheap in Game 1 (20% per miss, refill each act) [V3 fandom Penalty]; brute-force by exhaustion is possible but the community view of whether it is "intended" is [M].
- Cosmetic: nearly all dialogue branches; the game is "normally linear" with exceptions like the two ways to unmask Mr White in Turnabout Sisters [V3 fandom Turnabout_Sisters trivia].
- Dominant (my reading): Press on every statement first (usually free) to harvest hints; the penalty warning is not always reliable ("Turnabout Big Top") [V3 fandom Penalty].

#### 8. Open items
- Hours per episode; whether wrong-present rules are identical in the 2019 Game 1 build to the DS one: Wikipedia (DS manual) shows the old five exclamation marks, the 2019 wiki text shows 2 of 10 segments exploding per penalty, same 20% [V3 both].
- Repo claims (REPO_MENTIONS s.3): "a wrong present costs a fraction of a bar, never the case" is WRONG as a general rule: an empty gauge ends the case with a guilty verdict, and some mandatory decisions cause an immediate guilty verdict [V3 fandom Penalty; Game_Over]. "A flat deduction from a visible meter" is true for Game 1 (20%) but not Games 2-3, where penalties vary in 5% steps and are sometimes misleadingly previewed [V3 fandom Penalty]. "Inventory as argument: claims are objects you hold, spend and lose" is not supported: the Court Record is kept and evidence is not consumed by presenting; I found no loss rule [V3 fandom Court_record; the claim of no loss is an absence]. "One correct pair per round, space pruned to 2-4 statements and 1-3 bullets" is the Danganronpa Non-stop Debate shape, not Ace Attorney's, where the whole Court Record can be presented against any statement [V3 fandom Trial]. "Wrong present is charged, never refused" is TRUE: the game never blocks a present, it penalises.

### Lacuna - A Sci-Fi Noir Adventure - facts line
DigiTales Interactive; published by Assemble Entertainment (Steam also lists WhisperGames and Mayflower); 2D pixel-art narrative detective game (not a classic point-and-click). PC (Steam) 2021-05-20; Xbox and PlayStation 2021-12-21; Switch 2021-12-28 [V3 store.steampowered.com/api/appdetails?appids=1364100; V3 Steam news 2021-12-21]. Last numbered patch in the news feed: 1.2.1 (2021-10-20); PC-only "Chapter Select Update" 2026-05-20, no console date [V3 Steam news 2026-05-20, steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1833334318566441]. This tutorial assumes a first PC playthrough before the chapter-select option is used. One run is about 6-7 hours (a reviewer) and 3-7, commonly 4-6, in an AI-generated summary of player reviews [V3 jumpdashroll.com/article/lacuna-review; V3 vaporlens.app/app/1364100.md, third-party summary]; one sitting = a chapter between autosaves (the summary infers about 20 minutes).
Thinnest of the four games: no wiki page was reachable (no Wikipedia article, no fan wiki found); the mechanics below come from three reviews, an achievement guide, and the Steam page/news, so they are second-hand and I mark single-review claims.
Capability ids (B,D,G,H,I,L): B1-B7 NO | D6 PART (arrests and the choice to hand over or leak; no courts or sentencing system found) D1-D5 NO | G1 NO G3 `?` (a character can be shot; whether the player can die in play `?`) G5 NO | H1 YES (timed multi-option dialogue, non-repeating) H2 PART ("standing with the CDI" and with the character Zora feed the epilogue) H3 NO H4 NO H6 PART (the data leak "try to start / prevent a war") | I1 YES (detective-mode scanning plus conversations) I2 PART (multiple-choice Sheets as structured hypotheses, graded only by the story) I3 PART (news articles at kiosks react to choices) I4 NO I5 PART (NPCs lie; the player can lie to them) I6 YES (authored truth, partial knowledge) | L1 PART (authored cast) L2 NO L3 NO L4 NO L5 NO [V3 jumpdashroll; V3 a-to-jconnections; V3 gamepretty achievement guide; absences are mine].

#### 1. Setup choices
- You are always Neil Conrad, a Central Department of Investigation (CDI) agent; no build, class or difficulty menu that I found (GameFAQs users call it easy, S3 only) [V3 Steam store text].
- Profile: pick one of 3 save slots (the saved chapters belong to the profile) [V3 gamepretty comment "only 3 save slots"; Steam news 2026-05-20].
- Options: text and voice language can be set independently (since 1.2.0), an optional highlight toggle for interactables, and Steam lists the game as "Playable without Timed Input", so an option to relax the dialogue timers exists, details `?` [V3 Steam news 2021-09-17; appdetails categories; jumpdashroll].
- Small recurring choices you make from turn one: feed or pet your pet iguana Horace, smoke or not, tone (agreeable or aggressive) toward witnesses [V3 gamepretty guide].

#### 2. The loop
Clock: story days grouped into acts; a prologue, three acts and an epilogue are implied by the achievement list [V3 gamepretty]; the game autosaves at fixed points and each such point begins a chapter [V3 Steam news 2026-05-20].
1. Travel: Neil moves in a flat left-right/up-down world, mostly by train between districts of the city of Louville on the planet Ghara [V3 a-to-jconnections.com review; jumpdashroll].
2. Investigate: scan a scene with the investigation menu ("detective mode", an Arkham-like overlay); items and people are colour-coded by whether you have checked them or they have more to give [V3 a-to-jconnections; jumpdashroll].
3. Talk: dialogue starts by walking into someone or by choice; most replies are timed (a few seconds); conversations do not repeat, and some options appear only after you hold the right clues [V3 a-to-jconnections; Steam store text].
4. Everything learned is logged on the phone: clues, conversations, news articles, emails [V3 jumpdashroll; a-to-jconnections].
5. Close the section by filling out Sheets: multiple-choice forms for the key questions of the case; you may submit them wrong [V3 a-to-jconnections; jumpdashroll].
6. The story advances whatever you answered; consequences show up in later scenes, in news items and in the epilogue [V3 jumpdashroll].
7. Rest/domestic beat (home, ex, iguana), then the next day. Automated: the log, the save, all outcomes of Sheets and tone. Interrupts: scripted action beats with a short timer (shoot an armed suspect or talk him down) [V3 a-to-jconnections].

#### 3. The choice menu
| verb/choice | cost | effect | when picked |
|---|---|---|---|
| Walk / run / take train | time only | moves between scenes | constantly |
| Investigation menu / examine | none | reveals clues, marks checked | every scene |
| Choose a dialogue line | a few seconds | clue or loses a clue; may change a character's standing | constantly |
| Aggressive vs agreeable tone | none visible | tracked across the run (Good Cop / Bad Cop achievements) | at many confrontations |
| Timed action (shoot / de-escalate) | seconds | alters the next chapter | rare |
| Open the phone: read clues, news, email | none | information; news reacts to choices | between scenes |
| Submit a Sheet | irreversible | correct or wrong answers change who is caught and what you learn | once per section, about 8 times |
| Arrest, let go, lie | none | stored consequences (the guide names "arrest Dyson", "do not let Gary arrest her") | occasional |
| Leak or withhold the data | story | decides "start a war" vs "prevent a war" endings | once, late |
| Pet/feed Horace, smoke | none | flavour; achievements only | often |
Constant: dialogue, scanning. Rare: Sheets, timed actions, the leak. [V3 sources listed above]

#### 4. First hour, step by step
The free "Lacuna: Prologue" is about one hour of the opening [V3 Steam news 2021-05-20]; the steps below follow reviews, so the screens are [M] where marked.
1. Start a new profile; you are awoken by news of a murder, after an opening monologue over a city at dawn [V3 Steam store text].
2. Learn controls: move, run, talk, open the investigation menu, open the phone [V3 a-to-jconnections].
3. Take the train to the first scene; the ambassador's assassination is the case [V3 jumpdashroll].
4. Open the investigation menu and check every highlighted item; return to items after talking, as new clues appear [V3 a-to-jconnections].
5. Talk to people; pick lines within the timer; note that some lines never come back [V3 a-to-jconnections].
6. Read the phone's logs and read the Sheet; the prologue sheet asks three setting questions whose answers in the guide are Ghara, New Jordan, Tyllanium [V3 gamepretty guide].
7. Submit the first Sheet; a wrong answer does not stop the story [V3 jumpdashroll].
8. Next sections: the bullet, who helped a suspect escape, who the murderer is, each ending in a Sheet [V3 gamepretty guide list].
9. Visit home, feed or pet Horace, check news and email.
10. Decide about confrontation tone with early witnesses and guards (the first branches that feed Good Cop/Bad Cop) [V3 gamepretty guide].
11. Keep Sheets and clues in order, since "you can miss clues if you pick the wrong dialogue options or search in the wrong order" [V3 a-to-jconnections].
12. Accept that the save is automatic; no way back except the PC-only chapter select added in 2026 [V3 Steam news 2026-05-20].

#### 5. What changes later
- More factions and stakes: Drovia's independence, the anti-science Saviants, a mining dispute; later chapters carry arrests, a bomber, a mastermind, a data decision [V3 jumpdashroll; gamepretty guide].
- Sheets become harder (the Liberators sheet takes four fields) [V3 gamepretty guide].
- The epilogue checks your standing with the CDI and Zora and whether you retrieved the data: 2 x 2 x 2 = 8 endings [V3 gamepretty guide; S3 vaporlens says 8].
- No new systems unlock; pressure is moral and informational, not mechanical.

#### 6. Failure and ending
- Failure is branching, not a Game Over screen: "you don't have to be right to proceed", the story "marches on regardless" [V3 jumpdashroll]; wrong Sheets can mean "you never actually solve" a crime [V3 a-to-jconnections]. The store text says "No takebacks ... Play your cards right, and you might make it out alive" and that the truth appears "or not" [V3 Steam store]. Whether some choice kills Neil and shows a death/retry screen `?`.
- Recovery: only by loading an earlier chapter (PC since 2026-05-20), otherwise a new run; a reviewer reports being unable to revisit and not knowing where he went wrong [V3 jumpdashroll].
- Ending: eight epilogues; the guide's "Enter the Multiverse" asks for all eight [V3 gamepretty].

#### 7. Consequential vs cosmetic choices
- Consequential: Sheet correctness, the arrests and escapes it produces, the data leak, timed action beats, standing with the CDI and Zora [V3 gamepretty guide; jumpdashroll].
- Cosmetic: Horace, smoking, listening to street music, ads: achievements only, reported by a guide [V3 gamepretty guide].
- Dominated: Sheets are multiple choice and the options sometimes preview coming twists, so partial guessing works [V3 a-to-jconnections]; the game's "Master Investigator" (all Sheets correct) has a published answer list [V3 gamepretty]. A reviewer describes some timed choices as "railroaded", and some options loop back to the same line [V3 a-to-jconnections].
- Contested weight: whether tone choices change plot or only a counter; I found the counter and its achievements, not the effect `?`.

#### 8. Open items
- Not established: any hard Game Over; the timer length and accessibility option; the number of acts (3 from achievements); the chapter count; the Steam "8 endings" is from two non-official sources.
- Repo claims (REPO_MENTIONS s.3 and VCD): "consequence-tested submission: a judgment is accepted whether or not it is right and the world answers later" is CONFIRMED [V3 jumpdashroll; a-to-jconnections]. "highlight mode", "automatic logs", "structured hypothesis slots (Sheets)", "irreversibility (autosave only)" are all CONFIRMED [V3 same]. "Approach choice - calm or aggressive questioning" is PARTLY confirmed: aggressive-vs-agreeable choices are tracked, but whether they are an explicit verb is `?` [V3 gamepretty]. `.designs/.../investigation_systems_v30.md:209` ("Lacuna-style spatial attention: watch the scene, learn its rhythms, intervene at the moment of opportunity") and the "temporal drift" label are NOT supported by anything I read; the nearest real thing is a timer on dialogue and action beats [V3 a-to-jconnections].
