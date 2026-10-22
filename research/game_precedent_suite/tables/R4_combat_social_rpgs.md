# R4 (v2, verified): Combat/social RPGs (Disco Elysium, Griftlands, Baldur's Gate 3, Kingdom Come: Deliverance I/II)

Verification pass 2026-10-22. Tags: [V2 url ver/date] = text read in a fetched page body this session; [S2 url] = search snippet only; [M] = memory, not re-checked; [CONTESTED] = sources disagree. Original [V:...] tags were not trusted; each is re-tagged or corrected below. Fandom is HTTP 402 (still blocked); wiki.gg, bg3.wiki and Wikipedia were readable this time.
Version caveat: wiki.gg/bg3.wiki pages are live, undated wiki text (read 2026-10-22). Disco = base game/Final Cut rules (2019/2021); no patch number is shown by any source.

## 1. Disco Elysium (ZA/UM; Windows 2019-10-15, Final Cut 2021-03-30 consoles/PC update) [V2 en.wikipedia.org/wiki/Disco_Elysium]. Dialogue-driven CRPG, no combat system

| id | val | how |
|---|---|---|
| A1 | YES | Control Harry in isometric exploration; moves to interact with NPCs and "highlighted objects" [V2 wikipedia Disco_Elysium] |
| A2 | PART | 3 archetypes (Thinker 5/1/2/4, Sensitive 1/5/4/2, Physical 1/2/5/4 INT/PSY/FYS/MOT) or custom; signature skill raises its attribute's learning cap by 1 [V2 discoelysium.wiki.gg/wiki/Attributes]; no appearance customisation [M] |
| A3 | YES | 4 attributes x 6 skills = 24; skill points from levelling; skill cap raised by thoughts/drugs [V2 wikipedia; V2 wiki.gg Attributes] |
| A4 | PART | Clothing adds positive or negative skill modifiers [V2 wikipedia]; inventory size not checked [M] |
| A5 | PART | Kim Kitsuragi is a fixed partner who offers advice/support in some dialogue options; not controllable, influenced only by persuasion and skill checks [V2 wikipedia; V2 wiki.gg/wiki/Kim_Kitsuragi] |
| G1-G5 | NO | "No traditional combat"; conflicts resolved by skill checks and dialogue trees [V2 wikipedia] |
| H1 | YES | Skills speak in dialogue; active white/red checks 2d6 + skill vs difficulty [V2 wiki.gg/wiki/Skills] |
| H2 | PART | One tracked NPC opinion: Kim's "good cop/bad cop points" (hidden count; options branch at e.g. above/below 5); other NPCs react via checks and thoughts [V2 wiki.gg/wiki/Kim_Kitsuragi]. Earlier "no numeric meter" was wrong for Kim; whether the player can see the total is unstated |
| I1 | PART | Clues come via skills: Visual Calculus "reconstruct the cracked glass", "get an exact count" are white checks [V2 wiki.gg/wiki/Visual_Calculus]; no evidence-board object found [M] |
| I2 | PART | Thought Cabinet: fixed list of 53 thoughts, not player-written hypotheses [V2 wiki.gg/wiki/Thought_Cabinet] |
| I5 | PART | High Drama "detect and fabricate lies" [V2 wikipedia]; no forgery/disguise subsystem [M] |
| J3 | PART | Morale and Health pools; Morale drives Volition; death if hit on last Morale with no healing [V2 wiki.gg/wiki/Morale] |
| M1 | PART | Single case with authored endings [M] |
| M2 | YES | One authored case plus side tasks [V2 wikipedia premise: investigate hanged man] |
| M3 | YES | Check results and choices carry into later scenes [M]; failed/successful red checks one-time forks [V2 wiki.gg Skills] |
| M4 | YES | Hovering an active check shows its pass probability [V2 gry-online.pl poradnik]; the wiki's % ladder equals exact 2d6 math with crits (below) and a forum-reported 97% cap fits it, but no page states that the display is the engine's own number |
| D6 | NO | No court/trial mechanic found in the wikipedia gameplay text [V2 wikipedia, absence only] |
| B/C/E/F/L | NO | Not applicable |

Mechanics worth knowing:
- Active check: skill + modifiers + 2d6 >= difficulty; ties pass. Double 1 always fails, double 6 always passes, unless the thought "The Precarious World" changes it [V2 discoelysium.wiki.gg/wiki/Skills; V2 screenrant.com/disco-elysium-dice-guide-uses 2021-02-12; V2 gry-online.pl]. Corroborated by forum report of 97% cap [V2 steamcommunity 5533260453834275385, anecdotal].
- Exact odds, 2d6 >= N with crits applied (computed, and identical to the wiki.gg table values 3/8/17/28/42/58/72/83/92/97): N<=3: 97.2; 4: 91.7; 5: 83.3; 6: 72.2; 7: 58.3; 8: 41.7; 9: 27.8; 10: 16.7; 11: 8.3; 12 or more: 2.8 [V2 wiki.gg/wiki/Skills + own calculation]. Correction: the original table said "2: 100%"; with the snake-eyes rule no check exceeds 97.2% or goes below 2.8%.
- Marginal value of +1: 16.7 points at 7 -> 8, 11-14 points across 5-9, only 5.6 at the tails. The original "about 8 points mid-range, 3 at tails" understates it; it is ~2x that.
- Difficulty labels: Easy 8-9, Medium 10-11, Challenging 12, Formidable 13, Legendary 14, Heroic 15, Godly 16, Impossible 17/18/20; no active check at 6, 7 or 19 [V2 wiki.gg/wiki/Skills]. The wiki publishes no total-modifier column mapping.
- Passive checks: no dice. Value = skill + modifiers + 6, passes automatically if met; the wiki maps difficulty to required skill (Trivial 6-7: 0-1; Medium 10-11: 4-5; Legendary 14: 8; Impossible 17-20: 11-14) and counts ~10,287 passive and 211 "anti-passive" checks [V2 wiki.gg/wiki/Skills]. Earlier "conflict" (7 vs 5 vs 6) is a forum artefact: the 7 (median of 2d6) and 5 were guesses; skill+6 is stated by the wiki and two forum posters [V2 steamcommunity 1661194916746310440; V2 resetera thread 504849 post 49]. Anti-passive checks fire when the skill is too LOW and often cost Morale/Health [V2 wiki.gg Skills]. Crit rules are not applicable to passives (no roll) [inferred, not stated by a source].
- White checks retry after conditions change (add a skill point, explore, finish tasks, internalise thoughts; rare ones after a time delay); red checks cannot be retried and failing can beat succeeding [V2 wiki.gg/wiki/Skills]. "Fail-forward by design" (the earlier phrase) is an inference: Wikipedia says only that failed checks can produce negative effects, so the support is the red-check and retry rules above, not a design statement.
- Skill drawbacks discourage min-maxing: high Drama gives hysterics/paranoia, high Electrochemistry substance abuse [V2 wikipedia].
- Thought Cabinet: 3 free slots, +1 slot per skill point up to 12; internalisation 15 min to 20 in-game hours (sleep doesn't count; several at once); forgetting costs 1 skill point and removes the thought for the playthrough; 53 thoughts, not all obtainable in one run [V2 wiki.gg/wiki/Thought_Cabinet].
- Morale denominator does not exceed 13 (found by file editing) [V2 wiki.gg/wiki/Morale; low confidence on the figure].

## 2. Griftlands (Klei Entertainment; full release 2021-06-01 [V2 store.steampowered.com/app/601840; V2 wikipedia Griftlands]). Roguelike deckbuilder, combat + negotiation as cards

| id | val | how |
|---|---|---|
| A1 | PART | Move on an overworld map, conversation trees lead into card encounters [V2 wikipedia Griftlands] |
| A2 | PART | Three playable campaigns (Sal, Rook, Smith) with own decks; not custom builds [V2 wikipedia; V2 steam store] |
| A3 | YES | Draft/upgrade cards, grafts (lasting implants), mettle buys permanent meta-upgrades [V2 wikipedia] |
| A4 | PART | Grafts and item cards [V2 wikipedia (grafts)]; item cards [M] |
| A5 | PART | Recruit computer-controlled allies for negotiation and combat; hire mercenaries, pets [V2 wikipedia; V2 steam store] |
| B2 | PART | Hire mercenaries / allies per encounter [V2 steam store]; no roster screen found [M] |
| G1 | PART | Turn-based card combat: hand, action points, separate combat deck [V2 wikipedia] |
| G2 | PART | Weapons are cards/grafts; no armour model beyond Defend-type cards [M] |
| G3 | YES | Combat death ends the run; easiest difficulty allows one restart per checkpoint (3-4 per campaign) [V2 ladiesgamers.com/griftlands-review 2021-06-25; V2 wikipedia] |
| G4 | PART | Surrender/panic: enemies that "panic" can surrender and be spared or killed [V2 ladiesgamers; V2 turnbasedlovers 2022-02-11]; formal challenge [M] |
| H1 | YES | One-on-one negotiation card battle: reduce opponent's core-argument resolve before yours [V2 gameinformer 2021-07-05; V2 wikipedia] |
| H2 | YES | Five stages love/like/neutral/dislike/hate; Loved/Hated unlock faction-specific boon/bane [V2 thegamer.com/griftlands-beginner-tips 2021-07-13; V2 ladiesgamers; V2 steamcommunity 2568689796947776561 (2020)] |
| H3 | PART | Kill/spare/betray choices turn friends into enemies [V2 gameinformer]; no multi-step plot system [M] |
| H5 | PART | Panicked enemy can be spared (may become ally) or killed [V2 turnbasedlovers]; no ransom [M] |
| H6 | NO | No war/peace layer [M]; factions exist and each named character has a faction [V2 steam store] |
| M1 | YES | Per-run victory/death; seven Prestige difficulties + Story Mode, victory unlocks next [V2 wikipedia] |
| M2 | YES | World layout fixed, missions/events regenerated each run; "main story beats remain the same" [V2 wikipedia; V2 gameinformer] |
| M3 | PART | Persistent inside a run (everyone "remembers" kills); meta-unlocks across runs [V2 steam store; V2 wikipedia] |
| M4 | PART | Card text and arguments visible [V2 wikipedia (cards, arguments)]; enemy intents shown [M]; whether card damage is fixed or a range: ? (earlier "deterministic damage numbers" was [M] and I could not confirm it) |
| D6 | NO | Not modelled [M] |
| B1/B3-B7/C/D1-D5/E/F | NO | Not modelled |

Mechanics worth knowing:
- Negotiation mirrors combat: draw a hand, spend action points, play cards; the aim is wearing the opponent's resolve to zero before yours; friendly, hostile and composure card types [V2 wikipedia]. The win condition is the opponent's core argument; side arguments "stand separate from your core argument and must be defended as if they were allies in battle" [V2 gameinformer 2021-07-05]. Deck has three branches (diplomacy, manipulation, intimidation), diplomacy and intimidation often mutually exclusive; negotiations are always one-on-one [V2 turnbasedlovers 2022-02-11]. The earlier labels "influence" and "provoke" were not found in any page.
- Your resolve persists between negotiations; losing it costs resolve and possibly the task, and "may lead to a physical confrontation"; failing "doesn't end the game" [V2 thegamer 2021-07-13; V2 gameinformer; V2 ladiesgamers]. Fail-forward by state change.
- Relationship stages and effects: like = they help in nearby negotiations; love = also a faction-specific "social boon"; dislike = harder negotiation; hate = "social bane" [V2 ladiesgamers; V2 thegamer]. Boons/banes are per faction and job, e.g. Admiralty Goon Loved: +75 shills every morning, Hated: all enemy Admiralty +1 power; Jakes Dockhand Loved: 20-shill shop discount; Zealot Hated: negotiation hand size -2 [V2 steamcommunity 2568689796947776561, user-made table, early access 2020, may have changed]. Numeric thresholds between stages: ? (not found).
- Money in the loop: shills can bribe opponents who won't change their minds and buy cards; negotiated mission fees risk resolve and money [V2 thegamer 2021-07-13].
- Dice-free but not deterministic: draw order and procedurally generated missions/cast are the random layer; Rook's kit leans on coin-flip manipulation [V2 gameinformer]. "No dice" is accurate only for resolution of a check.
- Allies and negotiation "effects" act almost like companions; destroying them can pay out money [V2 turnbasedlovers]. Reviewer's criticism: few reasons to want characters to dislike you [V2 gameinformer].

## 3. Baldur's Gate 3 (Larian; Windows 2023-08-03, PS5 2023-09-06; eighth and final patch April 2025) [V2 en.wikipedia.org/wiki/Baldur's_Gate_3]. D&D 5e CRPG. Rules below = Patch 8 era (bg3.wiki live text, undated)

| id | val | how |
|---|---|---|
| A1 | YES | Control party members; turn-based combat on entering combat [V2 wikipedia BG3] |
| A2 | YES | 12 classes, 11 species, backstory; origin characters or custom [V2 wikipedia] |
| A3 | YES | Level cap 12 (vs 20 tabletop); feats, multiclassing; respec at Withers [V2 wikipedia] |
| A4 | YES | Deep gear/consumables [M, not checked] |
| A5 | YES | 10 recruitable companions (6 origin + Minthara, Halsin, Jaheira, Minsc); multiplayer cap four players [V2 wikipedia]; single-player active party of four [M] |
| B1-B7 | NO | No roster/office/duty systems; only companion party [M] |
| G1 | YES | Turn-based: d4 initiative, actions, bonus actions, movement [V2 wikipedia] |
| G2 | YES | AC, damage types, surfaces [M] |
| G3 | YES | Honour Mode: single save, party wipe = continue in Custom (ends Honour) or delete save [V2 bg3.wiki/wiki/Honour_Mode]; death saves [M] |
| G4 | PART | Scripted duels/challenges [M] |
| G5 | YES | Stealth vs passive Perception contest [V2 bg3.wiki Ability_checks; V2 thegamer DC article]; surprise round [M] |
| H1 | YES | d20 + modifier dialogue checks, mostly Charisma skills; Add Bonus button lets spells/items add before roll [V2 bg3.wiki/wiki/Dice_rolls; V2 bg3.wiki/wiki/Skills] |
| H2 | YES | Numeric companion approval (max 100, leave at -50) and separate per-trader Attitude [V2 bg3.wiki/wiki/Approval; V2 bg3.wiki/wiki/Attitude]; earlier "scripted affection, not an opinion model" understated this |
| H3 | NO | No schemes/plots system [M] |
| H4 | PART | Companion romance gated by approval thresholds [V2 bg3.wiki Approval]; no treaties/alliances [M] |
| H5 | NO | No hostage/ransom/tribute system [M] |
| I1 | PART | Investigation "Analyse clues. Solve mysteries." Int skill finds hidden clues/objects; no clue board or deduction mechanic on its page [V2 bg3.wiki/wiki/Investigation] |
| I2 | NO | No player-driven hypothesis system [V2 bg3.wiki Investigation, absence only] |
| I5 | PART | Disguise Self changes attitude scope "only that disguise" [V2 bg3.wiki/wiki/Attitude]; Deception dialogue checks [V2 bg3.wiki Skills] |
| J1 | YES | Spell slots, short/long rest recovery [V2 wikipedia: short rest 50% HP, two before long rest; long rest restores resources] |
| K5 | YES | Long rest wants 40 camp supplies (80 Tactician, up to 120 Custom); without it only a Partial Rest [V2 bg3.wiki/wiki/Camp_Supplies]. Earlier "limited by story" not supported by the page |
| M2 | YES | Authored campaign [M] |
| M3 | YES | Flag-based consequences [M] |
| M4 | PART | % on attack rolls [V2 bg3.wiki/wiki/Difficulty_class]; dialogue DC visibility [CONTESTED]: see bullets |
| D6 | PART | Witness reports to guards; interrogation with Persuasion/Intimidation/Deception checks, arrest, jail zone with escape routes, Fugitive condition; no trial, court or fines [V2 bg3.wiki/wiki/Crime] |

Mechanics worth knowing:
- Check: d20 + modifier vs DC; the wiki's own example is DC 15 vs 1d20+4 = 50% [V2 bg3.wiki/wiki/Difficulty_class]. Each +1 = 5 points (5e d20 math, computed). Advantage = better of two d20s; advantage + disadvantage cancel and sources don't stack; passive checks get a flat +5 / -5 [V2 bg3.wiki/wiki/Dice_rolls]. Computed: advantage ~ +3.3 on the die mean; DC 11 goes 50% to 75%.
- Natural 1 always fails / natural 20 always succeeds on attack rolls and ability checks; saving throws have no such rule except concentration and dialogue [V2 bg3.wiki/wiki/Dice_rolls].
- DC tiers: generic scale Very Easy 5, Easy 10, Medium 15, Hard 20, Very Hard 25, Nearly Impossible 30 is the 5e standard, reproduced by [V2 baldursgate3.wiki.fextralife.com/Ability+Check; V2 thegamer.com 2023-07-26]. bg3.wiki states only that DCs are "generally predetermined by the game" and gives no dialogue scale [V2 bg3.wiki/wiki/Difficulty_class]. One guide lists nine key dialogue DCs from 10 to 25 (Auntie Ethel 20, Helsik 20, Cordula 18, Nightsong 14-21, Elder Brain Crown phase 25) [V2 switchbladegaming.com/baldurs-gate-3/dialogue-charisma-guide, single guide, not checked against game data; treat as soft]. Larian's actual dialogue DC distribution: ? (no datamine found).
- Dialogue skill counts: Persuasion appears in 293 dialogues, Intimidation 209, Deception 147 (page marked "needs verification") [V2 bg3.wiki/wiki/Skills].
- Dialogue DC visibility [CONTESTED]: Early Access forum posters (Dec 2020) say skill name is shown but "you will never know the enemies DC" before choosing [V2 forums.larian.com thread 748529]; TheGamer (2023-07-26) says hovering/selecting a bracketed option shows the DC "at the top of the die image" [V2 thegamer.com]. bg3.wiki says % chance is shown for attacks and does not confirm it for dialogue.
- Karmic Dice (default on; formerly "Loaded Dice", introduced as loaded dice in Patch 4): tracks a "debt" per faction (party, allied NPCs, enemies; each player has a separate dialogue debt). A failed roll adds its success chance p to debt; with positive debt a hidden roll can force an automatic success, picking a d20 value among those that would have succeeded, then subtracting 2(1-p). Applies to attack rolls, target saving throws and ability checks in dialogue; NOT ability checks outside dialogue. For saving throws it only ever makes TARGETS fail, never succeed. Damage rolls use a normal distribution. It applies to NPCs and enemies too; Larian likened it to a "friendly DM"; toggle in Gameplay Options [V2 bg3.wiki/wiki/Karmic_Dice]. Correction to the earlier summary: it is symmetric across factions, per-faction debt, and the save rule is one-way. It is an undisclosed fairness layer on the displayed odds.
- Companion approval: scale max 100, thresholds -49..-40 Very Low, -39..-20 Low, -19..20 Neutral, 21..40 Medium, 41..60 High, 61..80 Very High, 81..100 Exceptional; swings of +/-1, +/-5, +/-10; warnings at -20 and -40; at -50 the companion leaves permanently with their gear; Charm Person, Friends, Hypnotic Pattern on a companion cost 10 approval when they end [V2 bg3.wiki/wiki/Approval]. Approval "might" raise DC when persuading companions [V2 same page; hedged wording].
- Merchant Attitude: only raised by gifting gold/items; lowered by attacking, stealing or touching things unobserved; per trader and per offender, severe negative stops conversation [V2 bg3.wiki/wiki/Attitude]. No global reputation and no trial or fines in the crime system [V2 bg3.wiki/wiki/Crime].
- Guidance adds 1d4 to ability checks [V2 bg3.wiki Dice_rolls]. Bardic Inspiration and Friends in Add Bonus: ? (not on pages read).
- Failure: dialogue failures mostly branch; some checks gate content [M]; combat loss reloads [M].

## 4. Kingdom Come: Deliverance I (Warhorse; Windows/PS4/XB1 2018-02-13) and II (2025-02-04; Royal Edition 2025-11-12) [V2 en.wikipedia.org/wiki/Kingdom_Come:_Deliverance and /Kingdom_Come:_Deliverance_II]. First-person realistic RPG
Version note: the kingdomcomedeliverance.wiki.gg pages are KCD1 text (Speech page last edited 2022-05-29, oldid 18568); KCD2 mechanics below come from Wikipedia and the Fextralife KCD2 wiki, both undated.

| id | val | how |
|---|---|---|
| A1 | YES | First-person Henry [M] |
| A2 | PART | Fixed protagonist; classless, stats grow by what the player does and says [V2 wikipedia KCD1]; appearance via gear [M] |
| A3 | YES | Skills improve by use; KCD1 lists 18 skills (7 combat, 11 non-combat); KCD2 max level 30 for stats, skills and Main level [V2 wiki.gg/wiki/Skills; V2 kingdomcomedeliverance2.wiki.fextralife.com/Stats] |
| A4 | YES | Equipment degrades, food spoils [V2 wikipedia KCD1]; layered armour/weight [M] |
| A5 | PART | Companion follows, little control [M] |
| B/C/E-F | NO | Not modelled |
| G1 | YES | Real-time melee with five attack zones [V2 wiki.gg/wiki/Combat] |
| G2 | YES | Better armour reduces health and stamina lost; blunt weapons best vs armour [V2 wiki.gg/wiki/Combat]; "layers" not on that page [M] |
| G3 | PART | No permadeath by default; saving requires drinking alcohol (KCD1); hardcore mode added to KCD2 post-launch [V2 wikipedia KCD1 and KCD2] |
| G4 | YES | Duels and fist fights [M] |
| G5 | YES | Lockpicking/pickpocketing are skill minigames [V2 wikipedia KCD1]; KCD2 derived stats Conspicuousness, Visibility, Noise [V2 fextralife KCD2 Stats] |
| H1 | YES | Dialogue stat icons (Speech, Charisma, Strength) beside options, plus bribery; branched trees with a time limit [V2 gamerguides.com KCD dialogue-options; V2 wikipedia KCD1] |
| H2 | YES | Reputation per town and demographic, summed from individuals; scale 0-100, trader start 50 [V2 wiki.gg/wiki/Reputation] |
| H4 | NO | No marriage/treaty mechanics found on any page read (absence only); KCD2 has romance content, title seen only [S2 deltiasgaming.com/?p=143961, not opened] |
| I1 | PART | Quest-level examination/witness interviews [M]; no evidence mechanic found on pages read |
| I6 | PART | Witnesses remember you even if you are not caught [V2 wiki.gg/wiki/Crime]; target stats hidden unless known or read [V2 wiki.gg Speech_and_Persuasion] |
| K3 | YES | Must sleep and eat; tiredness lowers Speech and Charisma in KCD2 [V2 wikipedia KCD1; V2 fextralife KCD2 Stats] |
| M4 | PART | Your ability numbers always shown, counterpart's only if you know them well or have Empathetic; exact success % not documented [V2 wiki.gg Speech_and_Persuasion; V2 gamerguides]; KCD2 fast-travel avoidance shows a % [V2 wikipedia KCD2] |
| D6 | YES | Witnessed crime -> fines/jail with a rate table; options pay, serve, talk (Speech/Charisma/Strength), flee [V2 wiki.gg/wiki/Crime]; KCD2 adds caning and branding [V2 wikipedia KCD2]. No trial or judge scene found |
| D1-D5 | NO | None |

Mechanics worth knowing:
- Speech success formula: no numeric formula is documented on any page read. What is documented: abilities "are compared with the abilities of his opponent"; Speech is "influenced by the reputation you have at that moment with the person"; Charisma = average of visible clothing Charisma, lowered by dirt and blood; intimidation rests on Strength and the deterrent look of weapons/armour; circumstances shift odds (luring a guard away eases intimidation); some options always succeed or fail [V2 wiki.gg/wiki/Speech_and_Persuasion; V2 wiki.gg/wiki/Charisma; V2 wiki.gg/wiki/Stats]. Whether a random roll exists: ? (no page says). Earlier "[M] compares Speech/Charisma/reputation/clothing" is consistent with this but unquantified.
- KCD2 dialogue stats: Wikipedia lists Oratory, Charisma, Intimidation supplemented by Appearance, Coercion and Dominate [V2 wikipedia KCD2]; the Fextralife KCD2 wiki lists Speech, Charisma, Might, Coercion, Domination, Dread and says "the higher your level, the more likely you are to succeed" with a skill icon beside gated options, no formula [V2 fextralife Persuasion+System, /Speech]. [CONTESTED naming]; the Stats page lists Coercion and Domination as "Dialogue Stats" and Speech/Charisma as base and derived [V2 fextralife Stats].
- Speech perks (KCD1 wiki): Final Offer (Speech 4: one more offer when a trader runs out of patience), Highborn / Lowborn (4: +3 Speech with nobles and wealthy vs commoners, mutually exclusive), Empathetic (8: shows counterpart's stats), Silver Tongue (8: Speech up when haggling), Troubadour (8: +50% reputation with women), Trustworthy Middleman (12: merchants more willing to buy stolen goods). The earlier "Empathetic (4/8)" is corrected to 8. Perk cadence [CONTESTED]: Speech page says a perk point "at every fourth level up", the Skills page says the option appears "after your third level up of each Skill" [V2 wiki.gg/wiki/Speech vs /wiki/Skills].
- Combat: five zones; zone changes after each strike unless set; feints change direction; polearms cannot strike overhead or stab to the head; at zero stamina you cannot attack until it regenerates and blocked hits cost health [V2 wiki.gg/wiki/Combat]. Perfect block costs no stamina and opens a riposte only another perfect block can stop. Master Strike is taught by Captain Bernard per weapon class; window grows with skill. A completed combo ends in a special technique with no defence [V2 same page]. No numeric stamina or window values on the page.
- Justice (KCD1 table, fine in groschen / jail): Animal Abuse 80/5 d; Assault 200/10 d; Breach of Curfew 10/1 d; Discharge of a Weapon 200/10 d; Lockpicking 300/10 d; Murder none/6 d; Pickpocketing 60/1 d; Reckless Riding 80/none; Stealing (looting non-bandit bodies) 60/18 h; Trespassing 15/1 d [V2 wiki.gg/wiki/Crime; page marked stub, no version]. Accepting punishment clears known crimes in that location; guards take loot; escape or resist brings force; stolen goods are marked and sell worse nearer in space and time.
- Reputation changes: falls with crimes, intimidation, refusing requests, lying if caught; recovers by helping, paying generously, selling cheaply or waiting; a crime seen by Rattay guards drops soldiers heavily; individual standing aggregates into the demographic "majority popularity is enough"; Local Hero perk converts village reputation into stat bonuses [V2 wiki.gg/wiki/Crime; V2 wiki.gg/wiki/Reputation]. No per-action amounts are published there.
- KCD2 punishments: Wikipedia confirms fines, caning, human branding, or excusal through dialogue skills [V2 wikipedia KCD2]; Fextralife names Pillory and Caning and says punishment makes it harder to deal with common people [V2 fextralife /Reputation]. The specific figures from the earlier draft (pillory -4 Charisma, branding halves reputation gains, merchant refusal, town-local scope) rest on Prima/PCGamer snippets I could not open (Prima 403, PCGamer body truncated): [S2 earlier-draft snippets, unverified].
- Failure: failed or crime-flagged talk escalates to fines/jail/force, not a blocked quest [V2 wiki.gg/wiki/Crime]; local scope of KCD1 reputation is per town [V2 wiki.gg/wiki/Reputation].

## Still unknown
- Griftlands numeric relationship thresholds between stages, and full boon/bane list: Fandom relationships page returned 402; Gamepur and Klei support 403; Steam threads give examples only. Settle: Fandom page or in-game codex.
- Griftlands card damage fixed vs range, and enemy-intent display (A/M4): no readable card page. Settle: Fandom card pages or a card data dump.
- BG3 Larian dialogue DC distribution and whether % is shown in dialogue: no datamine located (search budget ended mid-pass). Settle: unpacked Larian check data or a controlled in-game test.
- KCD speech numeric success formula and whether a random roll exists: not on any readable page; game scripts are not public. Settle: datamined dialogue scripts or a developer talk.
- KCD2 punishment numbers (pillory Charisma penalty, branding effects, scope): Prima 403, PCGamer truncated, fextralife /Pillory and /Caning 404. Settle: patch notes or an opened guide.
- Disco: how crit rules interact with The Precarious World (the page says only that it can change them); whether Kim's opinion total is visible to the player.
- BG3 Bardic Inspiration and Friends via Add Bonus; Disco A4 inventory size; KCD I1 evidence-gathering quests (still [M] in the tables).
- Search tool budget ended partway through the KCD2 work, so the KCD2 rows lean on Wikipedia and Fextralife.

## Sources
- https://en.wikipedia.org/wiki/Disco_Elysium ; https://discoelysium.wiki.gg/wiki/Skills ; /Attributes ; /Thought_Cabinet ; /Morale ; /Visual_Calculus ; /Kim_Kitsuragi
- https://screenrant.com/disco-elysium-dice-guide-uses/ (2021-02-12) ; https://www.gry-online.pl/poradniki/disco-elysium/testy-umiejetnosci/z11aedf ; https://www.itechguides.com/how-disco-elysiums-thought-cabinet-and-skill-checks-work/
- https://steamcommunity.com/app/632470/discussions/0/5533260453834275385 ; .../1661194916746310440 ; .../1697221074199323422 ; https://www.resetera.com/threads/don%E2%80%99t-understand-how-to-%E2%80%9Cplay%E2%80%9D-disco-elysium%E2%80%A6any-help.504849/
- https://en.wikipedia.org/wiki/Griftlands ; https://store.steampowered.com/app/601840 ; https://gameinformer.com/review/griftlands/griftlands-review-great-friends-in-low-places (2021-07-05) ; https://ladiesgamers.com/griftlands-review/ (2021-06-25) ; https://www.thegamer.com/griftlands-beginner-tips/ (2021-07-13) ; https://turnbasedlovers.com/review/griftlands-tbl/ (2022-02-11) ; https://steamcommunity.com/app/601840/discussions/0/2568689796947776561/ (2020) ; .../3108018655445797608 ; https://www.gamepressure.com/griftlands/
- https://en.wikipedia.org/wiki/Baldur%27s_Gate_3 ; https://bg3.wiki/wiki/Dice_rolls ; /Karmic_Dice ; /Difficulty_class ; /Ability_checks ; /Skills ; /Persuasion ; /Approval ; /Attitude ; /Crime ; /Investigation ; /Honour_Mode ; /Camp_Supplies
- https://www.thegamer.com/baldurs-gate-3-difficulty-class-dc-check-explained/ (2023-07-26) ; https://baldursgate3.wiki.fextralife.com/Ability+Check ; https://www.switchbladegaming.com/baldurs-gate-3/dialogue-charisma-guide/ ; https://forums.larian.com/ubbthreads.php?ubb=showflat&Number=748529
- https://en.wikipedia.org/wiki/Kingdom_Come:_Deliverance ; https://en.wikipedia.org/wiki/Kingdom_Come:_Deliverance_II ; https://kingdomcomedeliverance.wiki.gg/wiki/Combat ; /Speech ; /Speech_and_Persuasion ; /Crime ; /Reputation ; /Charisma ; /Stats ; /Skills ; https://www.gamerguides.com/kingdom-come-deliverance/introduction/useful-gameplay-tips/dialogue-options
- https://kingdomcomedeliverance2.wiki.fextralife.com/Stats ; /Reputation ; /Speech ; /Persuasion+System
- Search-returned only (not opened): https://primagames.com/tips/kingdom-come-deliverance-2-branded-and-other-punishments-effects ; https://www.pcgamer.com/games/rpg/i-messed-up-so-bad-in-kingdom-come-deliverance-2-that-i-was-literally-branded-a-criminal-and-hours-later-im-still-shunned-by-society/ ; https://www.jumpdashroll.com/article/disco-elysium-review
