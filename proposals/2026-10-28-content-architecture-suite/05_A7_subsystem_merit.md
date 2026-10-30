# Part 05: what each subsystem is worth (A7)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 05 of the suite (what each subsystem is worth alone and in the world; the analyst's report A7, corrected). Base: the session's read of `suite/05_A7_subsystem_merit.md` at 07:11:33 (a tool result, line numbers stripped; the repeat read at 07:11:34 is identical). That file was the analyst's `analysis/A7_subsystem_merit.md`, copied into the suite and patched by two heredocs at 07:10:29 and 07:10:35; the read already contains both, and their result is 15,074 bytes, equal to the `ls` the session ran at 07:10:36, so neither was replayed. Replayed afterwards, in time order: the part-05 half of the heredoc at 07:28:02 (four pairs, and the `04_CODE_ARCHITECTURE.md:793, :802` replacement), and the part-05 effect of the sweep heredoc at 07:28:11 (`04:793` to `04:801`). Applied: all; failed: none (every assert held). Checks: lines 26, 57, 87, 148 and 183 of the result match the session's own greps at 07:27:55 (before) and 07:28:03 (after the patch). No Edit-tool call touched this file in the surviving transcript, and no tool call touched it after 07:28:11. The title line below was added in this reconstruction: the original file began with the italic line that follows the rule. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This file is a reconstruction from the session transcript (second pass, 2026-10-30; the first pass could not see this part), not the original file. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

*Part 05 of the review suite. Corrected after adjudication (07d §2): where the personal fight resolves; the pool claim; the Proceedings odds policy.*

# A7: What each subsystem needs to be worth playing alone, and to matter to the world

HEAD `be24c71`. VT means `engine/season/verb_table.yaml`. Precedents cite the digests D6a, D6b, D7a and D7b; anything else is marked [FROM MEMORY].

## Verdicts
- **A subsystem earns its place when two things hold.** It is a small game with one central tension, and it WRITES something that the season loop reads back. None of the ten is playable today. There is no seat for a human player: `dispatching_chooser` is called only by tests (`harness/play_surface.py:41`).
- **Four can stand as minigames once their main gap closes.** These are personal combat, Proceedings, mass battle with troops, and fieldwork. Threadwork can stand as a small minigame.
- **Two are the frame, not minigames:** the dice and the season loop.
- **Three become the MANAGEMENT MENU.** These are settlements with the economy, factions, and travel with NPC life. They are where the world keeps score.
- **Cut nothing, but merge three overlaps.**
  - One dice roller, not three. One case record: fieldwork fills it, Proceedings spends it. War is declared in a Proceeding and fought in mass battle; factions get no resolver.
- **Two rulings go to Jordan** (end of file).

---

## 1. Resolution / dice. Alone: NO (it is the engine). World: STRONG
- **How it works.** You roll a pool of ten-sided dice against an obstacle. The result lands in one of four bands: Failure, Partial, Success or Overwhelming (`dice_engine.py:286-301`). Advantage raises the roll; it never lowers the obstacle (PP-232).
- **The problem.** The graded bands teach well, but combat and `p_success` use a smooth stand-in curve, not the real dice. At small pools it is wrong: at pool 2 against obstacle 2, the dice fail 74.0% of the time and the curve says 85.6% (D3e (c)9).
- **What it gives the world.** Every contested act resolves here. But there are three copies: the social roll, mass battle's own roller, and the stand-in curve. Two ladders measuring one quantity is a smoothness defect (CLAUDE.md §0.06).
- **Minimum version.** One roller, plus `odds_of` (B10-08) wherever odds are shown.

## 2. Season loop and persons choosing. Alone: PARTLY. World: STRONG (it is the hub)
- **How it works.** Each season you read what you have heard and spend up to 5 scene actions. What comes back arrives as beliefs. The fog of war is about what you know, held in your own claim ledger, not about the map.
- **What exists.** It runs: 56 verb rows. Your scene budget is 5, plus 1 per live `hold` Tenure (seats, and also each Record you create), minus the body and travel penalties (`decision/budget.py:57-61`); at most 5 scenes are released a season (`loop/deliberate.py:85-113`).
- **What is missing.**
  - A seat for the player.
  - Only the top question is kept (`fixtures.py:481`).
  - There is no season report.
  - There are no stakes: no ending stops the game, and succession is unbuilt (IN-61, B10-09).
- **Minimum version.** A text seat where the player's menu is exactly the menu the NPC chooser would see. Show the full question list. The season report is what changed in your ledger since last season.
- **Redundancy risk.** The management menu must not grow a second turn. Its orders cost no scene budget, and their cost falls on the person you delegate to.

## 3. Personal combat (+ kit). Alone: YES, as a Fire Emblem-style window with no forecast. World: STRONG
- **Jordan's framing.** The fight plays out in a window: two fighters, with techniques firing. It is driven by `modules/combat` (weapon physics, traditions, abilities). No odds are shown beforehand. The adapter already returns the scene trace (`seam/wrappers/combat.py:245-252`). The trace has 16 event kinds and none names a technique firing; "technique fired" callouts need a new trace field (PC lane, no rng draw, no state change). In the season every fighter is a default `Combatant` until `Person.kit` exists.
- **Conflict.** v10 said "show the true odds". Jordan's newer words are "we wouldn't really forecast". The newer ruling wins for combat. Matchup odds (CP-T03-05) stay internal.
- **The game is the choices made BEFORE the window.**
  - **Whom to fight, and whether.** The attacker must risk injury too (CP-T03-00).
  - **Kit:** two or three slots, weight against fatigue (Battle Brothers: "too heavy and fatigue runs out", D7a T02:170), proficiency on the practice ladder, and durability that wears.
  - **Terms:** first blood, until one yields, or to the death.
  - **A yield threshold**, set beforehand.
- **What you read instead of odds.** The opponent's visible kit, wounds and fighting tradition, and what your own ledger says about him.
- **What the window teaches.** WHY the fight went as it did: reach, balance, which technique fired. Mastery means learning the physics, not reading a number.
- **Does it stay interesting without a forecast?** Yes, if three things hold: the outcome is graded, harm carries over, and the trace names the causes.
  - Unicorn Overlord: you set tactics, then watch an automatic exchange (D7b T19:102-115).
  - Dwarf Fortress: no direct command (D7a T03:20); fights told in a log [FROM MEMORY].
  - Total War: shows only a rough outcome tier (D7a T07:29).
  - Fire Emblem's forecast and Battle Brothers' hit chances are what this design drops [FROM MEMORY].
- **What exists.** The resolver; wounds carry forward; a death closes the dead person's seats; 54 weapons built from parts.
- **What is missing.**
  - The attacker risks nothing.
  - Kit belongs to the fight, not the person (`combatant.py:94`; J-T5).
  - `challenge` writes nothing (VT:772).
  - There is no yield or spare in the season.
- **Contribution.**
  - Reads body, kit, presence; writes wounds, deaths, closed seats, claims (the personal fight resolves at RESOLVE, `rosters.yaml:1080`; ENCOUNTER holds only `a field`, :1284; moving it is REM-31). Feeds succession, grudges, the general's duel.
  - The fantasy: a sword-arm whose kills and wounds are remembered.
- **Minimum version.**
  - Both fighters risk injury.
  - Two kit slots, owned by the person through `hold` Tenures (K-5).
  - A yield threshold.
  - A text window that replays the trace.

## 4. Mass battle (+ troops and logistics). Alone: PARTLY (the engine is good, the loop is missing). World: WEAK today, STRONG as designed
- **The loop Jordan wants (Romance of the Three Kingdoms, Total War).**
  - Raise a counted troop stock from a town's recruits.
  - Feed and pay it every season.
  - Give orders and a battle plan.
  - Fight or withdraw.
  - Casualties return to the population.
- **This loop stands alone.** See Total War (D7a T07:29), Romance of the Three Kingdoms (D7b T13:25-42), Dominions (D7b T17:85-96).
- **Signature.** A side is named persons plus counted troops; a fallen commander opens his seats.
- **What exists.** An 18-tick grid engine and 10 troop types (`troop_types/registry.py:39-57`).
- **What is missing.**
  - No battle was fought at seed 0 (`…/ctl/realm_seed0_2seasons.txt:41-42`).
  - The army is just whoever lives at home (`loop/sides.py:116`).
  - There is no troop stock (CL-TROOP, held on M3).
  - There is no upkeep (IN-52 is switched off).
  - There is no siege.
- **Contribution.** It reads recruits, stores and walls. It writes bodies, holdings, and casualties back to the troop stock and to population weight (TS-6). It depends on settlements and factions.
- **Minimum version.**
  - Troop stock option A (TS-1 to TS-8).
  - A `levy` act.
  - Upkeep drawn from stores.
  - A plan set before battle: formation, reserve, and the loss level at which to withdraw.
- **Recommended (K-MB-4, a research recommendation, not a ruling; ruling 6 in part 01 §11).** The plan is fixed before battle, as in Dominions; there is no live command. NPC wars run unwatched.

## 5. Proceedings (the social contest). Alone: YES (the best design in the repo). World: STRONG
- **How it works.** You bring a matter before the people who can decide it, and you choose what to spend and what to keep. *"...in a room whose mind they cannot see"* (`07_THE_GAME.md:13`). Twelve kinds of proceeding are one mechanism with different settings; 8 are built (`arrangements.yaml`).
- **What is missing.**
  - The pool reads nobody (`pool_default`, `sigma.py:119-131`); under the H-213 ceiling of 2 the room can only lower the obstacle (`roll.py:63-100`, `test_sc02_reception.py`). [UNVERIFIED: non-zero reception in a seeded run.]
  - Speaking (`speak`) changes nothing.
  - The proceeding's inner rounds (the nested run) are unbuilt.
  - Speech cannot lie (J-C-6).
- **Compare.** Griftlands; Ace Attorney (D7b T19:180-190); Triangle Strategy (T19:23).
- **Conflict, settled.** `21_RECONCILIATION.md:617` (ratified as intent, ED-SC-0039) refuses to show the room, the obstacle or the odds, and makes that refusal structural; CP-T01-03 is narrowed and held (`_part13:40`). Proceedings shows no odds. The actor's own other rolled acts band odds (CP-T01-03 (a)). The other side's limits, and its lies, stay hidden.
- **Contribution.** It writes binding results: duties, detention, banishment. The fantasy: advocate, judge, or accused. Fieldwork feeds it proofs. It feeds factions, governance and war.
- **Minimum version.** A legal trial whose verdict weighs the bench and the proofs, and where the accused may answer (CP-T05-01/-02). Fieldwork's `interview` and the proceeding's interrogation become one act.

## 6. Fieldwork / investigation. Alone: PARTLY. World: STRONG (it feeds Proceedings)
- **How it works.** Go where something happened, read the scene, follow a lead, then make a charge that the world answers. Evidence is a belief with a source, and documents can be forged.
- **What is missing.**
  - A failed inquiry tells even the investigator nothing (`rosters.yaml:1147-1151`), so failure teaches nothing.
  - `interview` uncovers nothing.
  - There is no case object.
  - Nothing says whether there is more to find.
- **Rule kept.** Nothing grades the player's conclusion (AX-7). The world answers through a Proceeding, as in Pentiment.
- **Minimum version.**
  - A failed inquiry still tells the actor something.
  - A place can be read after the fact.
  - A signal says whether there is more to find.
  - One case record is shared with Proceedings.

## 7. Threadwork. Alone: PARTLY (strong idea, broken price). World: WEAK
- **How it works.** You perceive or alter the substrate of the world, and you pay in distance from being human. Coherence measures that distance: elastic at first, then permanent (`systems/threadwork/sim/coherence.py`).
- **What is missing.**
  - It is not plugged into the season loop (`loop/matter.py:135`).
  - `thread_read` writes nothing.
  - Mending is free, so it beats every other operation (TW-T:137-143).
- **Compare.** Darkest Dungeon II, Sunless Sea, Bloodlines (D6b §5).
- **Minimum version.**
  - `thread_read` as a fieldwork inquiry for sensitive characters.
  - One working with a real price.
  - Coherence bands that change the practitioner's own odds before any breach (CP-T07-07).
  - A working that others see carries a social cost.
- **Keep it:** nothing else delivers P-08, P-10, P-15.

## 8. Settlements, governance, economy. Alone: NO as scenes, YES as the MANAGEMENT MENU. World: STRONG
- **How it works.** On the menu you appoint, levy, requisition, build and issue edicts. At the end of the season you read stores, hunger and recruits.
- **Compare.** Manor Lords, Frostpunk (D6b §1); King of Dragon Pass: *"the quickest way to lose is to starve your people"* (D7b T16:205).
- **What is missing.** The core chain never bites. Hunger hurts no one (`body_step=0`, `fixtures.py:594`), and harvests do not depend on labour.
- **Signature.** A town has no stat block; its approval is what its people think (A3 Q5).
- **Minimum version.** Hunger that hurts (`body_step` above 0), labour in the harvest, a levy edict, and a treasury that pays upkeep.

## 9. Factions, war, diplomacy. Alone: NO. World: STRONG (the political glue)
- **Cut test.** Cut a separate faction minigame and nothing is lost: something already built does every job it would do.
  - Joining a faction is `commit`.
  - Defecting is `repudiate`.
  - War is declared through a council-of-state Proceeding.
  - The fighting is mass battle.
- **Keep instead.**
  - A menu view of who stands with whom, and of wars and treaties.
  - Succession (IN-61). Seven seats can never refill today.
- **Order of work.** Succession first, then `declare` as a Proceeding outcome (CP-T09-02), then defection.

## 10. World, travel, survival, NPC life. Alone: NO. World: STRONG (the clock that makes stories)
- **What is missing.** Distance is free: each trip costs one travel leg whatever its length (`budget.py:60` subtracts one penalty per leg and prices no distance). Ageing, illness and hunger are all switched off.
- **Demote it.**
  - Travel becomes a cost on the route (CP-T10-01), plus a ROAD CARD. A road card writes an occasion, such as someone met or a rumour heard, never an outcome. Set pieces live here (directive 2).
  - NPC life runs inside the engine.
  - Household acts go on the menu.

---

## Ranking (H/M/L; "Alone" = merit as designed, once the minimum version lands)
| subsystem | alone | world | becomes |
|---|---|---|---|
| Proceedings | H | H | minigame |
| Personal combat + kit | H | H | minigame (window, no forecast) |
| Mass battle + troops | H | M → H | minigame |
| Fieldwork | M | H (feeds Proceedings) | minigame, sharing the case record |
| Threadwork | M | L → M | small minigame, plus a fieldwork inquiry |
| Season loop | M | H (hub) | the frame |
| Dice | L | H | the frame (one roller) |
| Settlements, economy | L | H | management menu |
| World, travel, NPC life | L | H | menu, road cards, engine clock |
| Factions, war | L | H | menu view; resolved through Proceedings and mass battle |

## Order of becoming playable (text slice B10-S first)
1. **The frame.** A seat, a season report, and handing play to an heir (REM-30/31, CP-T02-06).
2. **Combat.** Both fighters risk injury, kit slots, and a text replay window.
3. **Proceedings.** A trial whose pool and obstacle read the case.
4. **Fieldwork,** feeding that trial.
5. **The menu.** Hunger, labour, the levy (needs M3).
6. **Mass battle with troops** (TS-1 to TS-8), then succession and `declare`.
7. **Travel.** Route costs, road cards, NPC-life clocks.
8. **Threadwork.** Needs its stat carrier, a price on mending, and A1.

Left for Jordan: troop-grade ladder, recruit share, A1 content, kit values.

## Escalations (2)
- **E1. M3: allow a counted troop stock in a town's stores (`Rung.stores`).** This changes ratified Layer 1 (`04_CODE_ARCHITECTURE.md:801`, `:810`). Your Romance of the Three Kingdoms and Total War direction needs it. I recommend yes (option A, `proposals/2026-10-16-troop-stock-design.md`).
- **E2. J-T5: where a person's kit lives.** I recommend that a named person's kit be `hold` Tenures on equipment objects (K-5). Then slots, proficiency and durability belong to the person, and troop kit stays the town's stock. It needs an equipment object kind the loop does not have yet. [UNVERIFIED: whether that is a Layer-1 amendment.]
