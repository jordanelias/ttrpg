# Valoria: content, characters, factions, settlements, playability, events, arcs (part 2 of 2)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 01 of the suite, second of two files (sections 10 to 15; sections 0 to 9 are in `01_MAIN_REPORT.md`). Same base and same patches as the first file: `main_clean.md` plus `heredoc_072531`, `heredoc_072607` and `heredoc_072811`, all applied, none failed. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This directory is a reconstruction from the session transcript's surviving reads and patch scripts, not the original files. Recovered in a second pass (2026-10-30), each with its own provenance: parts 05 and 07a to 07d, and the lens-3 (directive-compliance) critic report (`critic_lens3.md`). Parts 06 and appendices A1 to A5 are recovered in the third pass (see `00_INDEX.md`). Edits the session made by tools other than Bash heredocs (Edit-tool calls) were not captured, so the text may differ from the session's final file in ways not recorded here. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

## 10. Q6: What each subsystem needs to be legible and playable

**Verdict.** No subsystem is playable today. Each fails the same three ways: no seat, no odds before a choice, no account afterwards. One shared play surface fixes most of it.

**Principle: parity (governs seated play only; the management surface you added is §13 and overrides the "nothing more" below for that surface).** The player is the decision procedure of one seated person. Their menu, budget, admission and resolution are byte-identical to what the NPC chooser would face for that person; a callback that returns the chooser's pick must reproduce the run's `content_hash` (REM-31's planned exit tests exactly this). Presentation may be richer; the option set may not. **Legibility policy, settled by your directive and the ratified texts:** personal combat shows facts only (no forecast: your "we wouldn't really forecast"; record it as a ledger row); Proceedings shows no odds (`21_RECONCILIATION.md:617`, ratified as intent); the actor's other rolled acts show band odds (v10, `..._part14.md:282`). `04_CODE_ARCHITECTURE.md:858` ("the ARITHMETIC of what the character already holds, and nothing else") fits "facts the character holds" better than computed odds.

**Cards.**

| Subsystem | Verbs worth a menu now | Biggest gap |
|---|---|---|
| Season / persons | 51 resolvable rows | no seat; only the top question is shown; an empty menu is silent |
| Personal combat | `fight`, `accept` | the attacker takes no band: a fight is risk-free |
| Mass battle | `march` (only refusals run) | 0 fields fought in the one stored run (seed 0) |
| Social / Proceedings | `tell`, `utter`, `petition`, `open_case`, `convene`, `speak`, `determine`, `commit` | the pool is a flat default for everyone; the room can only lower the obstacle (reception and proofs, `roll.py:63-100`) |
| Fieldwork | `research`, `surveil`, `interview`, `forge`, `conceal` | failure teaches nothing (`finding.none` reaches nobody) |
| Threadwork | none that run | the oracle is not called by the loop; no menu |
| Settlements / economy | `confer`, `revoke`, `issue`, `requisition`, `transfer` | the spine never binds: hunger hurts no body |
| Factions / war | `covenant`, `commit`, `seize`, `oblige` | no succession; seven seats can never refill |
| World / NPC life | `move`, `forgive` | distance is free |

**Session shape.** First hour: choose one of 4 to 6 curated named persons plus one drawn opening Tension, then about four seasons. A season is at most five decisions (one scene released per round; the budget above five can never be spent because of this). A campaign is one person's line of 30–50 seasons; the client ends it, the engine halts nothing. The minutes (1–2 per decision) are an assumption.

**Top gaps and cheapest fix:** no seat (a text client over `dispatching_chooser`); no odds (`band_odds`, B10-08); menus name verbs, not consequences (render each row's `requires` and `writes`); only the top question is seen (hand the callback the whole list); silent nothing (a drop-reason trace); no stake or end (client-side end conditions plus IN-61); free acts (CP-T03-00 first); no season account (the ledger delta since the last deliberation is the log).

**Verb classes, computed from `verb_table.yaml`, never listed:** player-available (the seated person's option set), delegable (acts caused through a duty edge: dispatch, issue, confer, oblige, plus auto-resolved fights), engine-only (anything with no chooser). No verb exists only for the player.

---

## 11. Decisions

**Yours this session (none yet written to the ledger; the ledger rows are owed):**
- Agents may draft `[ASSUMPTION]` content for you to edit, each with a revert.
- B10-S, a text-first playable slice, is added before the port gate.
- The first playable person is seated at rung 1 or 2. *Consequence found later:* what a seat can order depends on that seat's remit list, not its rung. Klapp's and the Lord Steward's seats offer four orders (`issue`, `covenant`, `requisition`, `seize`) and cannot `confer`, `revoke` or `dispatch`; the Confessor, also a rung-1 seat, holds `confer`, `revoke` and `convene` (`engine/season/offices.yaml:364-369`). So the choice of starting seat, not the rung, decides how full the management console is.
- Combat shows facts only, no forecast (record as a ledger row; do not ask again).
- Directions, not yet rulings: troops follow Romance of the Three Kingdoms and Total War (a commander leads a counted stock); equipment follows tactical RPGs with physics-derived values; set pieces and event decks are wanted; each subsystem is a minigame on the seam; the management surface follows Crusader Kings and Koei.

**Settled by the evidence (no ruling needed):** dice TN is 7 always; wounds add a fractional obstacle (ED-PC-0005); a personal fight resolves at RESOLVE; Proceedings shows no odds; the Godot version is 4.7 (ED-GO-0002); `fac.*` was retired at plan position 29b, so the `fac.legitimacy` supersession row should be closed; ED-IN-0225 is answered by M20(b) and needs only a plan-text amendment (§8); `valoria-game` stays scaffolding and the slice runs on the Python engine; extend `build_realm`, do not build the VSG; retire `set.*` and use the geography triplet as seeds; governance mode stays deleted; no faction-named verbs; the Tensions deck is 6 cards, draw 1. The full adjudication of 754 recorded conflicts is in parts 07a to 07d: 0 of 754 needed a design ruling to settle what runs. The rulings below arise from the proposals, not from those conflicts.

**Rulings for you (12).** Each is a choice with what each side means; queue ids (M3, J-T2…) are in brackets. "Confirm all" on 2026-10-26 (ED-IN-0301) accepted the defaults then in force on the twelve plan questions; it did not say yes to any amendment (its own text says so). Rulings 1, 2 and 5 therefore reopen defaults you confirmed.

1. **Troop counts [M3].** Should an army be a stored count of troops by type under a named commander, as in Romance of the Three Kingdoms and Total War? *Yes:* a holding keeps "300 pikemen"; this amends Layer 1 (`04_CODE_ARCHITECTURE.md:801`, which now says a unit is only a list of persons, and `:810`). *No (the confirmed default):* an army is only the persons who live at home and fight at their weight, and there is no unit card, only persons. Every template proposal and P3-B's unit cards need yes.
2. **Attribute list [J-T2].** *(a) P2-A:* nine attributes plus Thread Sensitivity as a tenth, kept on the field it already has. *(b) The ten-score variant:* split Attention into Perception and Insight, fold Focus into Will, keep Bonds, count Thread Sensitivity; it passes the demand tests and overrides no ruling. *(c) P2-B:* the demand-derived eight, which overrides ED-IN-0185's ruled ten and a closed-agenda entry. *(d) P2-C:* six, used as floors and ceilings and never as dice. Recommended: (a) now, with (b) as the cheap revert if Perception and Insight prove distinct in play.
3. **Training rule [amends M2/CR-20].** Today a person's skill is the higher of their talent and their trained level, so a talented person's training changes nothing. *Sum:* talent plus a capped amount of training (recommended). *Higher-of:* keep today's rule.
4. **Who owns a sword [J-T5].** *(a)* A weapon is an item a person holds: it can be looted, inherited, given or seen, and it needs a new object type and a layer check. *(b)* Weapons are stores at a town's armoury and a person fights with the best class available: nothing new, but no heirlooms.
5. **Storyline form [new, part 02].** Do you accept authored story openings drawn when the world is built from pools attached to seats and places, each opened only by a person's own choice (P1-B, recommended)? It needs the B10-19 clause reworded and the Tensions card schema widened to role-bound goal rows plus one seeded claim, and an owner for the summons hook B4.1 (optional). The alternative P1-C adds dated beats and arcs as templates, which reopens the T-c default and the fourth-motion default and scripts whole arcs; not recommended.
6. **Mass-battle command [M4 Ask C].** *Plan before battle,* with a duel zoom for the general (the research recommendation K-MB-4, not a ruling), or *live command* during the battle.
7. **Founding in play.** May new factions be founded during play? Recommended: yes, by a person stating a purpose (`utter`) and others joining (`commit`); a seat is created only through `establish`; new towns are not founded in play.
8. **Mayor seats.** Should each of the 37 towns have a Mayor seat appointed by the territory holder? It adds up to 37 appointments (`confer`) per world; measure that load first.
9. **A world Thread substrate.** Is the world dying (a measurable condition on Thread sites that worsens) or only misunderstood (the Threads are a doctrine people argue about)? Choosing "dying" needs a new world-level condition and unlocks seven arcs.
10. **The management surface [your directive].** *(a)* Which reading? *Weak (recommended):* the seated person is the author of record and the menu batches their seat's orders; with no seat (between heirs) there is no management menu, and AX-1 is unchanged. *Strong:* the player's orders are independent of any character, which amends AX-1 and `04:853` and covers the gap between heirs. *(b)* Free of scene budget: for the player's person only, which breaks the rule that the player has exactly the options the engine would give that person, or for every person, which changes the simulated world and moves the hash. Either overrides your own 2026-09-02 ruling on the budget's unit and number (`decision/budget.py:19-20`); recommended: every person, implemented where the budget and release count live.
11. **Odds shown for acts other than combat.** The plan shows the true odds band (v10 `part14:282`; combat shows none, by your directive). A softer word computed from what the character believes is the believed-odds mode that AM-B-03 withdrew; it reopens only if AQ-X1 is ruled (b). Choose: *true band* (default, P3-A) or *reopen AQ-X1 (b)* for a believed word (P3-B's legibility option; otherwise P3-B shows the true band on request).
12. **What the console may show.** AX-7 says no state is hidden from the player; Layer 1 §C.11 (`04:851-862`) says no resolver-side value becomes visible inside a decision. A holdings tab showing a place's stores shows resolver values. Choose: *only what the character's own ledger holds* (recommended; consistent), or a wider reading that amends C.11.

**Closed or housekeeping, not choices.** *Altonia's default* (`foreign` off): confirmed 2026-10-26, so closed. *CLAUDE.md §3's line* that `systems/` retains social_contest contradicts ED-SC-0033 and ED-IN-0284; it is Layer 0 wording that ED-IN-0283 (d) reserves to you, and the recommended rewording is: subsystem code lives in `modules/`, the old kernel retires at SC-05, the `systems/` folders stay. *`valoria-game`:* move to Godot 4.7.x (ED-GO-0002), drop the 7 retired constants, delete `KeyStore.gd` and the 15 trigger resources (ED-1050); this is work, not a ruling.

**The coherent package I recommend:** P1-B (redrafted, drawn at build) + P2-A + P3-B reached through P3-A's text client, with the first playable slice at personal combat and a Proceedings hearing. It needs rulings 1, 2, 3, 5, 10 and 12 (and 4 when kit is built). Rulings 6 to 9 and 11 are independent.

---

## 12. Reliability and what was not examined

- **Method.** 43 digests of about 3 MB of source (cheap readers who quote and cite but do not judge) plus 8 further digests added during the work (troops and kit, narration, Proceedings, conflicts, supersession and errata, the 55-arc register, the prose-writer skill, the `valoria-game` census); seven analyses that re-opened sources; three proposal sets; an A6 re-derivation of the attributes; an A7 merit analysis; four conflict adjudicators; one adversarial pass on the earlier draft, and one three-lens pass on this suite whose findings were applied once.
- **Verified by me directly:** the headline counts (83 persons = 46 named + 37 cohorts, 32 offices, 412 rungs, 322 sites, 683 tenures, 67 Propositions, `capability` empty on 83 of 83, no cohort with pursuits, requirements 3/1/5); the seat-parity hash (plain and seated runs both `5301d6b6…`, two seasons, seed 0); `faculty` absent from `engine/season`; thread-sensitivity writers (set at build only); `tensions.yaml` absent; `harness/arc.py` built; the AX-5/T-c/B10-18 card rule; ED ids and their locations; the Godot attribute fields.
- **Not read in full:** plan parts 6 to 14 (digests and cards only); `RULINGS.yaml` (163 KB) and the Proceedings files beyond their heads; the Godot repo's GDScript beyond a census; process directories (`_session_provenance`, `shape-tracer`, `degree-sweep`), deliberately skipped.
- **Estimates:** reachable-arc counts are family-level (low confidence); cell counts, scenario counts and the 36-row figure are design estimates, untested.
- **From memory:** precedent claims outside the repo's research digests (Wildermyth, Fallen London, RimWorld storytellers, Fire Emblem, Total War odds, Burning Wheel, Traveller, World of Darkness).
- **Cannot be checked:** several files the old designs cite are gone from the tree (round-one governance files, `stats_1_7_scale.md`, rulebook sections for arcs 20 to 35).

---

## 13. The management surface (your directive, added after the analysts reported)

**Your point:** "only a person acts" governs the world's churn and impact. The player still needs an abstract surface, such as a roster management menu, where the engine acts on the player's behalf directly and no character does it.

*Final position: the weak reading with abstract presentation (AX-1 unchanged), with the strong reading offered as a live choice (§11, item 10).*

**Conflict, named.** Your wording is the strong reading: the engine acts on the player's behalf and no character does it. That breaks three things as ratified. (1) AX-1, which says "no ... engine is ever the subject of a decision" (`architecture/meta/01_AXIOMS.md:75-78`), and `04_CODE_ARCHITECTURE.md:853`, which refuses "the player is not an actor" by name. (2) The parity rule, that the player is the decision procedure of one seated person. (3) The rule "no verb exists only for the player". AX-7 is unaffected: it concerns what a character can see, not who gives orders.

**Two readings (you rule: §11, item 10).**
- *Weak (recommended; no amendment):* the menu is a batched front end over the seat verbs the player's own seated person already holds. The seated person is the author of record and the engine files the batch. AX-1 stands. Consequence in plain terms: **when the player has no seat (between an heir's accession, say) there is no management menu**; re-binding the player to an heir or a sworn tie (CP-T02-06, M7(b)) covers that gap, so no axiom is amended.
- *Strong (your words):* the player is outside the world, and a player order is an input authored by the player and executed by the engine. This needs an amendment to AX-1 and `04:853`: *"Only a person acts in the world. The player is not in the world; a player order is an input authored by the player, executed by the engine, and limited to the closed set in this section."* AX-5 has a precedent for an exogenous author (individuation: "the demand is its author").

**What the weak reading looks like.** Presentation is abstract, as in Romance of the Three Kingdoms and Crusader Kings 3. What the repo's research digests (D7b T13; D6a R1) show: the player is a character, the menu is abstract, the engine does the clerical execution, and the result depends on who carries the order out. RTK XIV gives each area an overseer and a priority, and the overseer's stats set the yield (T13:47, :78); Genghis Khan II costs scale with "the acting character's Political ability" (T13:174-188); Knights of Honor II yields 100% with a governor and a tenth without (T13:251); in CK3 the game ends when the lineage dies with no heir (R1:14, :81-84). In all of them the player's reach is bounded by the character's rank.

**The boundary (for you to correct).**
- **Which verbs are orders** is decided in one place, a `management:` marker on the verb row; this section lists no authoritative set. Built seat verbs that are candidates: `confer`, `revoke`, `establish`, `dispatch`, `issue`, `requisition`, `transfer`, `seize`, `covenant`. Unbuilt: `tax`, `ration`, formation orders (the plan-before reading of mass battle).
- **An order writes exactly what its verb row writes, and no more.** `confer` writes the seat Tenure itself (`verb_table.yaml:274`, `writes: Tenure.until/since/term`); `seize` writes a Tenure's dates; `transfer` writes stores; `requisition` moves stores; `dispatch` writes nothing. So orders do not "write only an instruction": several write a holding directly, with no delegate and no way to decline. What stays emergent is what comes after: the world's response passes through persons' choosers and the resolvers, and dice and MATTER decide results.
- **Same eligibility and refusal gates.** An order still passes the seat's eligibility (own, remit, hold, presence), the refusal rules and the verb's real costs (a `revoke` has a revocation cost, IN-31; a `transfer` spends the treasury). Without these the surface becomes a way around the friction that makes stories.
- **No scene budget** (your correction), implemented once, in the budget and release owner (`Scene.cost`, `deliberate.py:252-258`), not as a new column that a second place also reads. Whether this holds for the player's person only or for everyone is the second half of ruling 10.
- **Who pays.** For orders another person carries out (`dispatch`, and the executors of an `issue` dispensation, `verb_table.yaml:602`) the delegate's own chooser takes it up and spends the delegate's budget, so an absent or overworked delegate does nothing that season. For orders that write a holding directly there is no delegate; they cost what the verb costs in the world.
- **Falsifier.** A scripted order list equal to what the seat-holder's chooser would have issued reproduces the run's `content_hash`; and each order's writes equal its verb row's `writes:` list, no more.

**What it fixes.** The seat-vacancy and Mayor problem (appointments become a menu action); faction and settlement management at scale without playing every minute of a person's day; a season of five decisions becomes one management pass plus the scenes you choose to play. The roster is the natural catalogue view, which also helps §6. The plan must supply batching, so one pass issues many orders.

**Verb taxonomy, revised.** Three classes: player-available (seated play, including orders from the seat), delegable (acts caused through a duty edge), engine-only. "Player orders" is not a fourth class: an order is a seat verb authored by the seated person, so no verb exists only for the player.

**Risks.** It can become a way to skip emergent friction (many attempted acts are refused; §1) and flatten stories into spreadsheet play; the "same gates" rule is the safeguard. Precedent: CK3 council and appointments, Mount & Blade party management, Dwarf Fortress work orders [FROM MEMORY].

---

## 14. Each subsystem as a minigame on the season loop (your directive, added after §13)

**Directive.** Every subsystem should be playable as its own minigame that interfaces directly with the season loop, so that each minigame is informed by worldly state, acts upon it, and impacts it.

**The architecture already has this shape.** A *prize row* in `engine/season/rosters.yaml` names a `provider` and a `module_entry` (for example `personal_combat` → `combat.fight`; `mass_battle` → `mass_battle.resolve_field`; `social_contest` → `social_contest.roll`). A host *input builder* projects the `World` into a typed input (`PersonalCombatInput`, `MassBattleInput`, `FieldworkInput`, in `queries/inputs.py`). The module owns the minigame and returns a graded result. The host adapter lifts that result and the gate folds it into writes at RESOLVE, or at ENCOUNTER for a contest declared at RESOLVE and fought later (`loop/encounter.py`, M4). Wrappers "own nothing, ever" (`seam/wrappers/__init__.py`, 04 §A.2). Two roles are registered (`contest` and `inquiry`, `manifest/registry.py:38-39`), and construction refuses a prize with no registered provider.

**The minigame contract (a generalisation of that shape).**
1. **Informed by the world.** The input builder reads worldly state (who is present, what each side holds, fortification, the trail a finding can uncover) and freezes it. What the human sees is limited by AX-2 (the person's View) and by Layer 1 §C.11 (`04:851-862`: no resolver-side value becomes visible inside a decision); AX-7 binds the character, and says no state is hidden from the player.
2. **Played by a person at defined moments.** The human replaces the chooser at the module's decision moments (REM-31's six: measure, reopen, commit, mode, counter, contact). The engine plays every other role with the NPC choosers. Three fidelities run on one resolver: auto, scripted, human. A scripted pick equal to the chooser's reproduces the run's `content_hash` (the parity test from §10, applied per moment).
3. **Acts on the world only through the gate.** The module returns a graded result and writes nothing. The host converts it to writes under the step's token class, so every effect is a Receipt that can be audited.
4. **Re-enters the loop.** Later seasons read what the minigame wrote (wounds, claims, Records, holdings), which is how it impacts the world.

**Where each subsystem stands against the contract**

| Subsystem | Minigame form | Seam today | What it writes back | Missing |
|---|---|---|---|---|
| Personal combat | duel / grid bout (presented as a Fire Emblem-style window, no forecast) | `contest` provider BUILT; the fight resolves at RESOLVE (only the `a field` prize defers to ENCOUNTER; moving a fight there is REM-31, unbuilt) | wounds, stance, standing | the human fidelity (REM-31); the attacker takes no band (CP-T03-00) |
| Mass battle | plan-before orders, plus a duel zoom for the general | `contest` provider (`march`) BUILT | casualties, holdings, morale claims | fields rarely fought; troop stock (CL-TROOP, held on M3) |
| Social / Proceedings | a hearing or debate with bench, parties and proofs | `contest` provider (`social_contest.roll`) BUILT; nested run and `speak` writes UNBUILT | verdicts, Records, claims, standing | a flat default pool for everyone; no `Proceeding` object or nested run; several effect handlers (`_eff_speak`, `_eff_examine` …) are undefined |
| Fieldwork | an inquiry over a trail, with a case board | `inquiry` provider BUILT (`seam/wrappers/fieldwork.py`) | findings deposited at WITNESS | no case board; failure teaches nothing (`finding.none` reaches no one) |
| Threadwork | a working (weave, lock, mend, ward, knot) | **no provider and no role** | stress, Thread-state, claims | a new role; the oracle is not called by the loop |
| Settlements / economy | the management surface (§13) plus Hold Court (a proceeding) | MATTER yields; no provider | stores, edicts, offices, grievances | edicts (`tax`, `ration`), labour in the yield, a felt cost of governing |
| Factions / war | the management surface, diplomacy as a social matter, war as mass battle | none for diplomacy | covenants, commitments, seats | `declare`, `recruit`, succession |
| World / travel / survival | route legs with encounters | `move` only; distance is free | position, body bands, ties | route pricing (CP-T10-01), a map reader |

**Adjudication.** This does not conflict with the parity rule: parity governs *which options a person has at each moment*, and a minigame is a sequence of such moments. It does conflict with A4's first-slice framing (one seated person, a text menu), which should be a **front end onto these minigames** and not a separate surface. The decision to be made is not whether they interface (they must, by the contract) but which minigames reach a human first.

**Recommendation for the first playable slice (B10-S).** Personal combat (REM-31 is already planned) and a Proceedings hearing, because those are the two subsystems with running verb sets (§10), then fieldwork (the `inquiry` provider is built). Settlements, factions and travel stay at management-menu fidelity (§13) until they have a provider. Threadwork needs a new provider role before it can be a minigame; that is new architecture and belongs in the plan as a position, not in this review.

---

## 15. Directives received after the analysts reported (summary; detail in parts 02 to 05)

- **Combat presentation:** a Fire Emblem-style window that plays the fight back event by event with skills called out, driven by the repo's own combat system, with no pre-fight forecast. The adapter already returns the scene's trace (`seam/wrappers/combat.py:252`; 16 real event kinds, none naming a technique firing, so callouts need one new trace field). Inside the season every fighter is a default combatant until `Person.kit` exists. A playback viewer of auto-resolved fights can ship from today's trace without moving any hash.
- **Troops and kit:** troops follow Romance of the Three Kingdoms and Total War (a commander leads a counted stock with type, morale, training, upkeep); equipment follows tactical RPGs (slots, loadout, proficiency, durability, acquisition) with values derived from the physics model (`modules/combat/weapon_physics.py`, built). Today there is no `Person.kit`, no equipment object, no `recruit`, `muster`, `supply`, `disband`, `equip`, `repair` or `craft`; the troop levy feed is built and shipped off.
- **Subsystem merit (part 05):** worth playing alone: personal combat and Proceedings (the strongest design). Partly: season loop, mass battle, fieldwork, threadwork. Not minigames: dice (the engine), settlements and factions (the management menu), world and travel (the clock that makes stories). Recommended order of becoming playable: the frame, combat, Proceedings, fieldwork, the management menu, mass battle with troops, travel, threadwork.
- **Variety:** no instrument measures variety across seeds or worlds; P1 specifies one (`harness/variety.py`) as the falsifier for any storyline proposal.
