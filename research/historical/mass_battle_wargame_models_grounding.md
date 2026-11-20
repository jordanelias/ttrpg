# Grounding note: how wargames model movement, contact, morale, rout, pursuit and result

## Status: FILED — reference, tier 3 (`research/00_INDEX.md` §1) · not canon (CLAUDE.md §0.05) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: MB (historical adjudication lane of `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

Sibling of `mass_battle_casualties_and_results_grounding.md` (**its tier table applies**). A wargame is a
designer's model, not evidence about history: what transfers is the **shape** several independent designs
converge on, and where a rule set states its scale, a professional's or a scholar's judgment of what fits in
one interval of time. Figures from fan pages are leads (`research/00_INDEX.md` §1; the sourcing floor).

**What the tree already holds, and is relied on rather than re-sourced:**
`research/game_precedent_suite/tables/R6_mass_battle_campaign.md` (Total War: Rome II from the official
manual; Field of Glory II: Medieval from its 227-page manual; Ultimate General; Hearts of Iron IV),
`tutorials/T07_mass_battle.md`, `dispositions/D_T07.md`, `tables/R2_warband_sandbox.md` (Bannerlord, Warband),
`grounding/ogre_battle.md` (filed 2026-11-12), and the Unicorn Overlord and Football Manager rows the MB
audit cites. Rows below marked `R6` are that file's, with its own `[V2]` tag (page body read by that lane).

## Sources read by this lane

| key | source | what it is | tier · read |
|---|---|---|---|
| DBA | `https://en.wikipedia.org/wiki/De_Bellis_Antiquitatis` (revision of 2026-08-29) | encyclopedia summary of Phil Barker's rules (1990 onward) | `[T]` 2026-11-12 |
| KS | `https://en.wikipedia.org/wiki/Kriegsspiel` | encyclopedia summary of Reisswitz's 1824 rules and Verdy's 1876 free game | `[T]` |
| LB | `https://rulespal.com/lost-battles/rulebook` | a rules text for Philip Sabin's *Lost Battles* (2007) board game, with rule numbers; a third-party host, not the publisher | `[T]`; rule numbers as the tool returned them |
| TW-M | `https://r2enc.totalwar.com/en/manual/single-player/0087_enc_page_battle_play_phase_conflict_morale` | official *Total War: Rome II* manual, Morale | `[T]` |
| TW-F | `https://r2enc.totalwar.com/en/manual/single-player/0088_enc_page_battle_play_phase_conflict_fatigue` | official *Rome II* manual, Fatigue | `[T]` |
| SN-FOG | search result for the tabletop *Field of Glory* (2008) cohesion rules (Slitherine forum fragments) | snippet | `[S]` |
| SN-HC | search result for *Hail Caesar* (Warlord Games) break tests and army morale (publisher forum fragments, second-edition errata) | snippet | `[S]` |
| SN-MTW | search result quoting a community wiki for *Medieval: Total War* fatigue levels | snippet | `[S]` |

**Sought and not reached:** *Warhammer Ancient Battles* (the encyclopedia page describes no mechanics);
*De Bellis Multitudinis*; *Tactica*; *Dominions*; *Battle Brothers* (wiki returned HTTP 402); the *Medieval:
Total War* community wiki (403); the *Field of Glory* tabletop rulebook; Sabin, *Simulating War*; Perla, *The
Art of Wargaming*. Nothing below rests on them.

## What is established

### Kriegsspiel (Reisswitz, 1824): a professional army's planning game

| # | claim | tier |
|---|---|---|
| K1 | Map at about 1:8000; "A turn represents two minutes of time." Movement from a table: "a cavalry squadron can move 400 paces" on open ground, 250 through light forest, 100 up inclines; a pace about 63 cm. | `[T]` KS |
| K2 | Combat by dice chosen for the odds: one die for even-odds hand-to-hand, others for 3:2, 3:1 and 4:1. The **odds select the die; the die decides**. | `[T]` KS |
| K3 | Losses are tracked as points against a unit; a half-battalion "is removed 'when it loses half of its hitpoints'". No separate morale system: half strength is the end of usefulness. | `[T]` KS |
| K4 | Orders are written; players do not move pieces; the umpire "decides how troops would interpret and execute a given order" and can simulate delay by "holding on to a player's message for a round or two". | `[T]` KS |
| K5 | Hidden information: pieces are placed "only for troops which they judge to be visible to both sides". | `[T]` KS |
| K6 | "An open-ended game with no fixed victory conditions"; the umpire sets objectives. Verdy (1876) held the essentials were "the umpire and concealed information". | `[T]` KS |

### De Bellis Antiquitatis: the most abstract successful ancients game

| # | claim | tier |
|---|---|---|
| D1 | "Each army is composed of 12 elements"; a bound "represents 15 minutes"; ground scale one inch to 100 paces. | `[T]` DBA |
| D2 | Command is a die: each bound the player rolls for points that are "the player's level of control for the turn" and "do not carry over"; a point moves one element or one connected group. A commander cannot do everything he wants. | `[T]` DBA |
| D3 | Combat is one opposed die a side plus factors for troop type and situation ("outflanked or uphill"). "Achieving a roll twice as high as your opponent generally destroys that opponent"; lesser wins push the loser back out of the line. | `[T]` DBA |
| D4 | The battle ends on "the destruction of 1/3 of the enemy's army". | `[T]` DBA |

### Lost Battles (Sabin): a scholar's model, built to reproduce some 35 ancient battles

| # | claim | tier |
|---|---|---|
| L1 | "The battlefield is divided into 20 zones, 5 by 4"; no diagonal movement or attack. A turn is "roughly 3 minutes for every 100 metres of zone distance"; a battle "can last up to 10 turns". | `[T]` LB §2.1, §3.1 |
| L2 | A unit stands for a number of men that depends on its **class**: troop classes are Veteran, Average and Poor ("Poor infantry: 1,000 × M foot soldiers" at multiplier M), so a quality unit is fewer men. Fighting value 2, 3 or 4 by class. | `[T]` LB §1.1–1.4 |
| L3 | Command: "the active player rolls 1d6 and adds 1 for every full 10 points of the army's Fighting Value"; unspent orders are lost; a commander spends his own pool on units in his own zone. | `[T]` LB §4.1, §8.3 |
| L4 | Movement: an activated cavalry unit has 2 movements, infantry 1; rough ground costs cavalry 2. Units face one of four ways; turning about is free only when no enemy is to either side. | `[T]` LB §5.1–5.4 |
| L5 | A zone limits how many units may attack from it ("3, 4, or 5, depending on the scenario"; "Veteran heavy infantry counts as 1/2 a unit"): frontage, not numbers, sets the fighting strength. | `[T]` LB §6.3 |
| L6 | Units are Fresh, then "Disordered" on a first hit, then Shattered. A Fresh unit may make an all-out attack at the price of becoming Disordered. Fresh is a resource that is spent. | `[T]` LB §1.5, §6.7 |
| L7 | Morale is tested for the army "every time one of your units is Shattered and/or one of your commanders is killed"; units that fail leave: "considered to have withdrawn if they are 'Fresh,' or fled if they are Disordered". Modifiers include enemy "to the front and rear, and/or on both the left and right flanks" (−1) and outnumbering two to one (+1). | `[T]` LB §7.1–7.3 |
| L8 | Result: the battle ends at ten turns or when a side has fewer than three units; victory is by points with a **handicap** for the weaker army, and "Even a fled army can still win the game, if it achieves a better result than its historical counterpart did." | `[T]` LB §11 |
| L9 | No pursuit phase and no casualty count in the rules read: a shattered unit is gone and a fled one is worth points. | `[T]` LB (absence) |

### Total War: Rome II (official manual)

| # | claim | tier |
|---|---|---|
| T1 | Morale falls with "long, protracted melee fighting", casualties, fatigue and "facing overwhelming numbers"; a red bar means "the unit is wavering and about to break and rout". | `[T]` TW-M |
| T2 | Routers may be rallied by a general within his radius; "Units whose morale is shattered will not respond to the command to rally"; units that rout after the general's death, or in an army with no general, are shattered. | `[T]` TW-M; agrees with `R6` F8 |
| T3 | Fatigue: units "gradually become exhausted" from running and fighting; "once a unit becomes exhausted, even moving slowly becomes a great effort", leaving it open to cavalry; advice: "do not run everywhere". No levels or numbers on the page. | `[T]` TW-F |
| T4 | Auto-resolve "compares the statistics of all the units": a second calculation, with a known gap from the played battle. | `R6` F5 and its design note (`R6:28`) |
| T5 | An older title's community-reported fatigue ladder (Tired, Quite Tired, Exhausted, Completely Exhausted, each with attack and morale penalties) | `[S]` SN-MTW; a lead |

### Field of Glory (tabletop and FoG II: Medieval)

| # | claim | tier |
|---|---|---|
| G1 | Four cohesion states (Steady, Disrupted, Fragmented, Broken); a test on two dice, re-rolled by troop quality; triggers are shooting losses over about a tenth in a turn, losing a round of melee, a friend breaking, a general falling nearby; modifiers include a threatened flank and men lost over 25% and 50%. | `R6:46` `[V2 manual §14.2]`; tabletop section headings `[S]` SN-FOG |
| G2 | A flank or rear charge on a unit already fighting drops its cohesion a state automatically. | `R6:48` |
| G3 | "An average unit breaks near 50% strength; routers disperse after 5 rout moves; pursuit chances by troop type (mounted at least once; other foot never)." | `R6:52` |
| G4 | The army loses when 60% of its troops are routed or dispersed, or 40–59% with the enemy at least 25% better off. | `R6:51` |
| G5 | No auto-resolve exists in that game at all. | `R6` F5 |

### Hail Caesar (snippet tier only)

| # | claim | tier |
|---|---|---|
| H1 | A unit that has taken its stamina in casualties is "shaken": it fights worse, is exposed to break tests and cannot charge; the loser of a round of combat tests to break; results include breaking, giving ground and disorder; the army breaks when more than half its divisions are broken. The command roll was not found. | `[S]` SN-HC; leads |

### Ogre Battle and Unicorn Overlord

Filed elsewhere: `research/game_precedent_suite/grounding/ogre_battle.md` (the player "does not directly
control their unit, but selects a tactic"; one round an exchange; the side that did more damage wins and the
other is pushed back; a leaderless unit goes home). Unicorn Overlord's conditional tactics are in the suite's
MB proposals (`04_MB_manager_battle_one_resolver.md` §2, citing `tutorials/T19_tactics_narrative.md:146`).

## Convergences (what several independent designs agree on)

| topic | DBA | Kriegsspiel | Lost Battles | FoG | Total War | Hail Caesar |
|---|---|---|---|---|---|---|
| time step stated | 15 min | 2 min | about 3 min per 100 m of zone; ten turns | — | real time | — |
| horse to foot movement | not on page | cavalry given, foot not | 2 : 1 | by action points | — | — |
| terrain slows | — | 0.62 and 0.25 of open (cavalry) | cavalry pays double | yes | — | — |
| command is scarce and drawn | die a bound | written orders, umpire delay | die plus army quality | command range | general's radius | (not found) |
| contact resolved by | opposed die | die chosen by odds | 2d6 against a number | dice plus advantage | continuous | dice |
| states between whole and gone | pushed back | points to half | Fresh, Disordered, Shattered | four cohesion states | bar, wavering, routing, shattered | shaken, disorder, give ground |
| flank and rear | factor | — | morale −1; attack +1 | automatic cohesion drop | (not on page) | — |
| unit removed at | doubled | half strength | second hit | about 50% | morale | stamina then test |
| army beaten at | one third destroyed | umpire | fewer than 3 units, or by test | 60% routed | — | half the divisions |
| rally | no | no | no | yes, by a general | yes, by a general; never if shattered | — |
| pursuit | no | — | no | by troop type; foot never | (played out) | — |
| result | win or loss | umpire's judgment | points against history, named margins | win or loss | win or loss | win or loss |

Readings that the adjudication uses:

1. **Every design reads a unit as ended well before it is dead**: at half strength (Kriegsspiel, FoG), at one
   third of the army (DBA), at 60% routed (FoG). None fights to the last man.
2. **Every design with morale puts at least one state between sound and broken**, and several make "pushed
   back" or "give ground" a result of its own.
3. **Command is a scarce draw in the two most admired abstract designs** (DBA's die, Lost Battles' die plus
   army quality), and a delayed, interpreted message in the professional one.
4. **Fresh troops are a spendable resource** in the scholar's model (L6), which is Sabin's own historical
   finding (results note D3) turned into a rule.
5. **Pursuit is mostly not modelled on the table**; where it is, it is by troop type and horse does it.
6. **A stated time step runs from 2 to 15 minutes**, and a whole battle is on the order of ten steps in the
   one design that says (L1).
7. **Only the computer game with two resolvers has the two-answers problem** (T4); the board games have one
   resolver by construction, and FoG II has no auto-resolve at all.

## What this note does NOT establish

- Any rule of Warhammer Ancient Battles, DBM, Tactica, Dominions or Battle Brothers.
- Total War's numbers for morale, flanking or fatigue (the official pages give none).
- Whether any of these designs reproduces history. Lost Battles claims to (its designer's book was not read);
  the rest are games.
- The `[S]` rows are fragments of forum posts.
