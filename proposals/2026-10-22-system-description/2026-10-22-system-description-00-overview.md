# Valoria as a game system — suite index

## Status: PROPOSED (reference). Merging this PR ratifies nothing; this suite describes the code and two proposal directories as read on 2026-10-21/22 and is reference, not a ruling (`CLAUDE.md` §0.05).
## Lane: IN (cross-cutting). Grade under `CLAUDE.md` §0.2: `paper`. What it changes in `engine/season/`: nothing.
## Provenance: produced by extraction → synthesis → tutorial writing, then two rounds of independent adversarial audit (findings in file 13), then a round-3 precedent-disposition pass with two verification probes (file 13 Part 3; the precedent suite is `research/game_precedent_suite/`). Probe scripts the tutorials cite (`t01_odds.py` and the like) were session working files and are NOT committed; only `ctl/` (the control run) is.

Written against `a4ca9a5` (2026-10-21); revised in round 3 (2026-10-22) against `51d7b05` and the precedent suite. The control run is
byte-identical on `51d7b05` for seeds 0, 1 and 2 (two seasons), so every `ctl/` count below still holds; code line numbers were re-opened
at `51d7b05` wherever round 3 touched a sentence. Reference only; nothing here is ratified. Built by: cheap extractors (Haiku/Sonnet) →
Opus synthesisers → Opus tutorial writers, then two rounds of independent adversarial audit whose findings were applied.

| file | what it is |
|---|---|
| `2026-10-22-system-description-00-overview.md` | this file: breakdown into primary engine, resolution and subsystems; reachability matrix; how the parts work together; defects; comparison handles |
| `2026-10-22-system-description-01-shared-reference.md` | glossary of every primitive, process-id key, action economy, time scales, resources, comparison axes |
| `2026-10-22-system-description-02-t01-resolution-and-dice.md` … `2026-10-22-system-description-11-t10-world-travel-survival-npc-life.md` | ten tutorials, one per subsystem: pieces, mechanics, worked example with real numbers, actions, how to pursue goals, as-proposed, traps |
| `2026-10-22-system-description-12-reference-appendices.md` | first-draft subsystem references A1–A8 (superseded wherever the tutorials or the errata differ) |
| `2026-10-22-system-description-13-errata-and-audit-record.md` | round-1 errata, cross-cutting rulings, every audit finding, the control-run method, and the round-3 rulings (Part 3) |
| `ctl/` | control-run outputs (seeds 0, 1, 2; two seasons) and the script |
| `research/game_precedent_suite/README.md` | the precedent suite the round-3 revision compared Valoria against: capability tables, "how it plays" tutorials for about seventy games, and the disposition record (reference, tier 3) |

Read order for the question "how is each subsystem played": 00 → 01 → the tutorial for the subsystem. T02 (season, persons, choosing) and T01 (dice) are prerequisites for the rest.

---

# Valoria as a game system: engine, resolution, subsystems (revised after audit)

Repo `jordanelias/ttrpg`, written at `a4ca9a5` (2026-10-21), revised in round 3 at `51d7b05`. Sources: the code tree; `proposals/2026-10-21-v9-remediation/` (4 parts, "remediation");
`proposals/2026-10-16-verbs/` (23 parts, "verbs"). This overview supersedes the first draft's overview; the corrections it applies are
itemised in the Errata (Part C). Where an appendix (Part E) disagrees with this overview or the Errata, the Errata and this overview win.

## 0 Conventions

**Evidence grades** (one rule for the whole suite; first-draft appendices used several, which the audit found inconsistent):

- **RUNS-IN-LOOP**: the behaviour produced a non-refusal outcome inside `SeasonDriver.season` over `build_realm`, run the way
  `harness/populated.py::run` runs it. The barrier passes (MATTER, CENSUS, WITNESS) qualify by being executed every season.
- **RUNS-IN-LOOP at control**: it executes but is inert at shipped fixture values (`body_step 0`, `age_step 0.0`, `illness_rate 0.0`,
  `telling_privacy 0.0`, `confliction_weight 0`, `scar_weight_shift 0`).
- **TESTS-ONLY**: implemented or wired, but it executes only under unit tests, fixture worlds or oracle scripts, or it fired zero successful times
  in the realm run. A refusal gate firing is not the verb executing.
- **DESIGN-ONLY**: no executing code (a proposal, a stub, an empty hook, a deleted layer).

**Run figures.** "The realm run" is `build_realm(seed)`, two seasons, with the chooser built as `populated.run` builds it. The control script
is `ctl/control.py` in this directory; outputs for seeds 0, 1, 2 are `ctl/realm_seed*_2seasons.txt`. It counts per verb the acts that
**reached the fold** ("att", `d.resolved`, appended in `loop/resolve.py:377-379`) and the acts with at least one non-refusal event ("ok").
Contested and graded acts refused at admission or failed at the contest branch never reach the fold and are not counted: the act store
`w.acts` holds 1,407 / 1,394 / 1,447 formed acts against 1,132 / 1,122 / 1,175 that reached the fold (275 missing in seed 0: `research` 111,
`examine` 62, `surveil` 21, `speak` 19, `accept` 16, `fight` 12, `argue` 10 ...; I1 verification, re-run at `51d7b05`). So "att" means
*reached the fold*, not *attempted*; where a verb is formed and refused before the fold, the formed count is given too. Runs are identical
across processes (checked with random `PYTHONHASHSEED`). Results differ by seed: seed 1 executes `oblige` 22 of 24 and `confer` 1 of 5,
which seed 0 never forms. Every "never" below is therefore a statement about the seeds run (0 and 1 chiefly, 2 for spot checks), not about
the game.

**Who "you" are.** The code has no player character and no GM. Every person is a chooser that picks scenes from a closed verb table. The
tutorials (Part D) teach the rules from the position of the acting person.

---

## 1 Verdict

Valoria, as built, is a **seeded, reproducible agent simulation without a player**. Every person (46 named NPCs, 37 settlement cohorts) picks
acts each season from a table of 53 verb rows (47 admitted by the fold; 46 choosable once `destroy_record` is withheld), scored by the verb's
fit with the person's values plus stance toward the subject, then ordered by sampling noise that, on the one measurement available, often
decides between near-equal options. One gated store records the results. Contested acts go to one of three resolvers: a one-roll social
resolver that uses the margin ladder, a duel engine whose degree is read off wound state, and a battle engine whose result is
Won/Lost/Unopposed. Everything else is deterministic arithmetic behind typed preconditions. The repo's own acceptance instrument says it is
"not yet a game": 3 of 9 ruled requirements are met, 5 partial, 1 not met, and the milestone verdict is NOT MET.

Four facts organise the rest:

1. **The engine is running; the subsystems are thin where they meet it.** The season loop, world store, write gate, witnessing and chooser
   execute and are exercised. Combat (5,643 + 2,812 LOC), mass battle (10,154 + 3,089), the social-contest kernel (6,693) and threadwork
   (1,955) are far larger than the seams that call them. The seam into combat varies one input (`end`). The seam into mass battle varies troop
   count, morale start and one terrain row. The seam into social contest varies a default pool, plus bench "reception" and "proofs" terms on
   `speak`/`determine`, and forgery on inquiries.
2. **Wiring is not execution.** Most governance, faction, economy and migration verbs are wired and fire zero successful times in the realm
   runs. The chooser forms acts that the fold then refuses (`work` 77 reached the fold / 0 succeeded; `migrate` 81 / 0 in seed 0). The
   verbs themselves run: a callback that hand-builds the act with the right operand gets an outcome for `march`, `found`, `build`,
   `revoke`, `establish`, `migrate`, `tend`, `restore` and `work` (I1 verification claim 5), so most zeros are formation defects, not dead effects.
3. **Consequence ships switched off.** Hunger, ageing, illness, the scar-to-pursuit shift and the confliction damper default to zero, so MATTER
   kills nobody and every realm death is combat. The remediation's hunger design (RB-5) would bind only before the first yield, even
   if built (food cover rises from 21.7 to 41.7 seasons).
4. **Persons have no capacities.** `Person.capability` is empty on 83 of 83 realm persons and no attribute field exists, so the social roll is
   a 2-die pool against a default obstacle of 2 and fails 74% of the time.

---

## 2 The three tiers

### 2.1 Primary engine: the season loop (RUNS-IN-LOOP)
`engine/season/` is "Layer 2, the game code". `SeasonDriver.season` advances one tick (one season) in seven steps and four write barriers:
**CALENDAR → MATTER → (5 rounds of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS) → CENSUS**, then `tick += 1` (A1 §2.2).

| part | what it does | notes |
|---|---|---|
| World store | one entity-edge store: `Person`, `Rung` (eight kinds in one type: person, hearth, community, settlement, territory, province, duchy, realm), `Tenure` (the one edge type), `Office`, `Site`, `Record`, `Proposition`, `Claim`, `Event` | no stored Faction, Settlement or Province entity; `faction_q.Faction` is a per-barrier view; 17 territory rungs, provinces are a Query |
| Write gate | every change goes through `World.write`: a token constructed in `driver.py` (one per barrier), a 40-row write matrix (+6 retired), authorship rules F3, no-op rule F9 | content hash makes runs reproducible |
| Chooser | per person per round: one question in, candidates out, score + Gumbel order at τ = 0.1, scene budget from 5 | never receives a World (by type and test); constructed only by harnesses and probes, never in `loop/` |
| Verb fold | 53 rows: eligibility, typed precondition (37 typed, 6 `none`, 10 no key), writes per degree, emitted events, refusal kinds | refusals are events |
| WITNESS | the information bus: five ranked channels, refraction, ledger cap 200 | the chronicle channel broadcasts every Event whose kind a `binding_decision` row emits (a kind filter, `epistemic.py:685-686`; CROSS C5) to everyone |
| MATTER | the actorless clock: term lapse, claim decay (5 per season), larder draw, yield, wear, travel-leg end, hunger, ageing | `Rung.stores` is also written at RESOLVE by `transfer`/`requisition` |
| Queries | aggregates (population, faction members, province, war, sovereignty, reception) computed on demand, stored nowhere | since PR #494 also `endings_reached` (reported by every season, `loop/driver.py:515-518`) and IN-23's `legitimacy` / `stability`, one person's windowed estimate (`queries/person_q.py:451`, `:480`), whose only reader is the `harness/storybar.py` instrument |

No player interface reaches the season loop. A "play surface" is a callback that hands named persons to a human function
(`harness/play_surface.py:41-52`, `dispatching_chooser`, exercised only by tests); a callback can submit any resolvable verb with any extra
payload, and every hand-built act the I1 verification submitted ran (claim 5). Outside the loop, `systems/social_contest/sim/contest/agon_harness.py`
lets a human play Side A of one Bout-kernel contest from stdin against a kernel policy (`input()` at `:148-155`; three scripted runs at
`51d7b05`, `yes 1 | python3 -m systems.social_contest.sim.contest.agon_harness`: 9 prompts over 3 exchanges each, verdict `A_decisive` once
and a committee compromise twice, so the harness is not seeded), and two HTTP workbenches (`systems/combat/combat_engine_v1/workbench/server.py`,
`systems/mass_battle/sim/workbench/server.py`) let a designer configure and trace one duel or one battle with branch odds. None of them
seats a person in the realm. D-2 (ruled yes) has the remediation build IN-46 (a played, paused fight) and IN-47 (character-sheet space)
in RB-3; the repo's comparative frame describes the intended player position as "embedded: the player is one person's decision procedure".

### 2.2 Resolution: one ladder, three resolvers, three dice codes
- **The ladder** (`engine/dice_engine/dice_engine.py:286-301`): margin = net − Ob; Failure < 0, Partial [0,1), Success [1,3), Overwhelming ≥ 3.
  TN is fixed at 7. Faces: 1 → −1, 2–6 → 0, 7–9 → +1, 10 → +2. Advantage is a mean shift for σ-leverage (`soft_cap(x) = 1.5·tanh(x/1.5)` ×
  `0.8·√pool`); σ-leverage never changes an obstacle. The social obstacle does change with bench room terms and forgery; leverage itself is 0.
- **Three resolvers reach the season**, selected by a verb's `contests:` prize:

  | prize | resolver | where the degree comes from | seven contested verbs |
  |---|---|---|---|
  | a standing / a proposition / a matter | `social_contest.roll`: one pool roll | **the margin ladder** | `tell`, `argue`, `determine`, `speak` (+ graded inquiries `research`, `examine`, `surveil`) |
  | the body | `combat.fight`: a beat-level duel | wound state of the *subject*: Felled / Wounded / Untouched | `fight`, `accept` |
  | a field | `mass_battle.resolve_field`, at ENCOUNTER | `attacker_wins` → Won / Lost / Unopposed | `march` |

- **Rival dice code.** Mass battle spells its own roller and ladder copy, held equal by a test. A third copy is the frozen oracle
  `engine/reference/contest-groundup`. No single owner derives the obstacle (ED-IN-0202, suspended).
- **Seeding.** Rolls are keyed to `(world_seed, tick, actor, purpose)`; same seed, same game, across processes.

### 2.3 Subsystems: ten lanes, five kinds of existence
The verbs proposal names ten subsystems: PC personal combat, MB mass battle, SC social contest, FI fieldwork/investigation, TW threadwork,
GV settlements and governance, FA faction actions, EC economy, WT world/travel/survival, NP NPC life. They are **not** engine modules. The repo's
own module roster (`references/module_contracts.yaml`) has 26 rows, mostly `sim_module: none`, and only four composition roles
(`combat.fight`, `fieldwork.find`, `mass_battle.resolve_field`, `social_contest.roll`) reach the season.

| kind | subsystems | what exists |
|---|---|---|
| A. Large oracle + thin seam | PC, MB | full engine in `modules/`; the season gives it near-default input |
| B. Two implementations, the loop uses the small one | SC | kernel (tests) and one-roll path (loop) |
| C. Oracle never called by the loop | TW; FI `knots`; `systems/characters` scar oracle | tests only |
| D. No module; verb effects, queries, MATTER | GV, FA, EC, WT, NP | deterministic, mostly wired, mostly zero successes |
| E. Cross-cutting layer | information/witnessing, persons, chooser | running; the inquiry yield is empty in the realm run |

**Designed layers whose code was deleted** (`module_contracts.yaml`): `victory` (MS reaches 0 → Post-Calamity; all factions dissolved →
Anarchy; code deleted at plan position 28-iii), the MS clock `systems/overview/sim/ms_track.py` (0–100, −1 per year, start 60, no live caller),
`faction_state` (Mandate, Treasury, stats 1–7; action code deleted at 29b), `accounting_sequence`, `piety_track`
(= `systems/characters/sim/conviction.py`). **The running loop has no ending condition that halts it and no world-scale clock.** Since PR
#494 (IN-27) the season *reports* endings: `world_q.endings_reached` is "a read, never an actor" (`queries/world_q.py:1764-1767`) over the
two `rosters.yaml: endings` rows (`:2494-2553`), `peninsular_sovereignty` (the victory: GD-1 without its sustain, Accord and Stability
clauses, "UNREACHABLE IN COMPUTED PLAY", `:2531-2541`) and `theocracy` (the King's seat held under the Church; not a victory). The realm
as built reaches neither: `endings` is `[]` after both seasons in seeds 0, 1, 2 (round-3 probe). The read RUNS-IN-LOOP; reaching an
ending is TESTS-ONLY (`engine/season/tests/test_in27_endings.py`).

---

## 3 Reachability matrix

"att/ok" = acts that reached the fold / acts with a non-refusal event (§0); seed 0 first, `[seed 1]` where it differs in kind; "formed N"
is the act-store count where acts are refused before the fold (round-3 probe at `51d7b05`, matching the I1 verification). Source:
`ctl/realm_seed{0,1}_2seasons.txt`. "ok" includes events that change nothing (e.g. `dispatch`, `tell`); the state-changing subset is smaller
(the audit counted about 14 verbs that changed world state). Grades follow §0.

| subsystem | standalone size | what the season reaches | realm run | grade |
|---|---|---|---|---|
| Resolution core | 673 LOC | every contested verb | every contest | RUNS-IN-LOOP |
| Season loop / state / gate | 13,141 LOC | itself | 1,132 acts reached the fold in seed 0, 1,122 in seed 1 (1,407 and 1,394 formed) | RUNS-IN-LOOP |
| Chooser | 2,546 LOC | called at `deliberate.py:170` | all acts | RUNS-IN-LOOP |
| **PC** | 5,643 + 2,812 LOC; 54 weapon keys, 7 traditions + `none`, 9 abilities | `fight`, `accept` → wrapper; only `end` varies | fight 7/4 of 19 formed [5/5 of 13], accept 18/11 of 34 [9/6 of 29], challenge 23/6; `person.died` 9 [6], `contest.undecided` 10 [3]; over seeds 0-2, 33 of 59 combat calls felled the actor in the scene, exactly the 33 that left the subject Wounded or Untouched, and none wrote the actor (round-3 seam trace) | RUNS-IN-LOOP (default build); weapons, traditions, abilities TESTS-ONLY |
| **MB** | 10,154 + 3,089 LOC | `march` declared at RESOLVE, fought at ENCOUNTER; one Line subunit per side | `march.declared` 21 [10], `march.refused` 25 [10], `field.won/lost/unopposed` 0, `army.arrived` 0; no natural `march` names a settlement in seeds 0-2 (targets are persons, hearths, territories, dead ids), so the army is empty and the act refused | wiring RUNS-IN-LOOP; the battle TESTS-ONLY in natural play. The loop's ENCOUNTER does call it on a hand-built settlement march: `march {subject: set_s_036}` by `p_npc_033` via `off_npc_033` gives `march.declared` then `field.lost` in seeds 0, 1, 2 (attacker body 1000 → 20, budget 6 → 3; I1 verification, re-run at `51d7b05`) |
| **SC** roll | 127 LOC | `tell`, `speak`, `argue`, `determine`; graded inquiries | tell 23/4 of 27 formed [25/7 of 33]; speak 3/3 of 22 formed (all `matter.turned`) [0 of 14, all `speech.unheard`]; argue formed 10 [17; 18 at seed 2], every one refused before the roll (`argument.refused`); determine 0 of 2 formed [1/1 of 6] | tell, speak RUNS-IN-LOOP (degenerate); argue TESTS-ONLY; determine executes at seed 1 only |
| SC kernel (Bout) | 6,693 LOC | none | 389 checks pass under test | TESTS-ONLY |
| SC proceedings | docket, bench, 8 arrangements, 6 speech kinds | docket and bench read; arrangements only via `disposes` on a hand-named row | petition 42/14, open_case 12/6, convene 1/0 | docket/bench RUNS; arrangements, speech kinds DESIGN-ONLY as mechanism |
| **FI** | `modules/fieldwork` 36 LOC; knots 406 LOC | 6 inquiry verbs + 4 document makers | research 14/7 of 125 formed, surveil 30/5 of 51, interview 32/11, reconstruct 39/33, survey 57/13, forge 52/12, conceal 19/19; `examine` formed 62 [59; 39 at seed 2] and never passes admission, because its `site` operand is filled with the question's subject (`decision/options.py:1047-1048`), never a Site; 0 found deposits (FI-03's trail, PR #489) in seeds 0-2 | document makers RUN; inquiries RUN with empty yield; `examine` TESTS-ONLY; knots TESTS-ONLY |
| **Information (WITNESS)** | — | every Event | 11,869 `claim.deposited`, 5,329 `claim.decayed`; 13 of 74 ledgers at cap (11 of 72 seed 2) | RUNS-IN-LOOP; `witness_key` admits nobody (TESTS-ONLY); `post_remit` executes at seeds 1 and 2 only (one `inferred` claim each: the King's obligee `p_npc_070` learns of a refused royal act at tick 0; round-3 trace) |
| **TW** | 1,955 LOC | none; no importer in `engine/season/`; `thread_read` is absent from the chooser's menu because `resolvable_verbs()` lacks it (`loop/driver.py:101`; used at `harness/populated.py:1531`) | 0 | TESTS-ONLY |
| **GV** | — | MATTER economy + remit verbs | release 45/3, issue 6/5, dispatch 18/6 (writes nothing); revoke 6/0, convene 1/0, requisition 2/0, found 24/0, build 19/0; confer, establish, oblige, seize 0 formed [confer 5/1, establish 5/0, oblige 24/22]. Seven of the 32 seats have no conferral basis and can never be refilled once vacant (§6 #11); only `off_duke_valorsmark` sits directly above a revocable seat (`state/gate.py:452-476`), and it is vacant from tick 0 in every seed, so no `revoke` can pass after that, `office` operand or not | MATTER RUNS; release, issue, dispatch RUN; the rest TESTS-ONLY |
| **FA** | — | membership, `survey`, goal salience | survey 57/13; covenant 13/0 [4/0]; sabotage 34/0; `at_war` no non-test caller; `faction_q.head` always None | state RUNS; survey RUNS; covenant, sabotage, seize TESTS-ONLY; declare, recruit, levy, conspire DESIGN-ONLY |
| **EC** | — | yield, draw, wear; transfer, requisition, work, restore, found, build | `stores.changed` 111, `yield.taken` 74; transfer 45/1; work 77/0; restore 23/0 | yield, draw, wear RUN; trade, craft, price, tax, credit DESIGN-ONLY |
| **WT** | 17 territories, 37 settlements, 55 adjacencies in the geography file | `move`, `migrate` as containment hops; one scene-budget leg each | move 42/16; migrate 81/0 [143/0] | move RUNS; migrate TESTS-ONLY; routes, terrain, hazards DESIGN-ONLY |
| **NP** | — | cohorts; tend, train, forgive, give, commit | forgive 1/1; tend 34/0; train 38/0; give 16/0; commit 61/0 | forgive RUNS; the rest TESTS-ONLY; kin, birth, marriage, household DESIGN-ONLY |
| Persons / character model | 15 pursuits, 7 axes, 5 affiliations | carrier and crisis | scar ≥ 3 on 35 persons in 4 seasons; 9 convictions rewritten; pursuits changed on 0 | carrier RUNS; attributes, template DESIGN-ONLY |

---

## 4 How each subsystem operates alone (short; the tutorials in Part D teach each in full)

**Resolution core.** A pool of d10s gives a net score by the face rule; net minus obstacle gives a margin; the margin gives a degree. Pool 2 vs
Ob 2: Failure .74 / Partial .19 / Success .07 / Overwhelming 0.

**PC.** Two fighters, up to 12 turns of ~10 s engagements. Each engagement is a beat loop of closing, commit depth, lunge, a read contest that
picks the defence, binds, ripostes and grapples, with stamina, concentration and initiative. Wound impairment enters as a σ term; the obstacle
is the defender's history ÷ 2. Damage is physical (mass, head length, armour penetration).

**MB.** Two armies on a 51×51 cell grid, 18 ticks. Subunits carry formation, troop type, morale, discipline, stamina, ammunition and orders.
Contact is by frontage with support ranks; casualties are Lanchester-linear; rout is stochastic. Tactic cards are an empty dict.

**SC.** Season path: one pool roll per act. Kernel: 1–5 exchanges of seven move kinds with Standing, Reserve, Room and a stasis ground,
resolved by a venue's win condition. The code keeps the roll and does not adopt the kernel (retirement timing is Jordan's, SM-15).

**FI.** Six inquiry verbs, three graded by the borrowed social roll, with findings gated by a `finding_terms` band table; trails are
reachable only through a planted forged Record. The `knots` sim is separate and unplugged.

**TW.** Seven operations roll a d10 pool at TN 7: pool = Spirit×2 + 3 + TS//10. Coherence is a recoverable stretch of up to 6 over a permanent
resting point; past 5 the practitioner leaves the human band. No operation writes to its target; mending costs nothing and pays the mender.

**GV, EC, WT, NP, FA.** No dice. Deterministic writes behind three-valued typed preconditions. Seats grant a remit of up to six acts; stores
move by conserved shifts; yield is `int(base × condition/1000 × season_factor)`; movement is a tree hop costing one scene-budget leg; persons
heal, train or forgive in whole steps.

---

## 5 How they work together

### 5.1 The five joins
1. **The verb is the join.** A row names its resolver (by prize), its writes and its events. Subsystems never call each other. `engine/` names no
   subsystem by import.
2. **Events and WITNESS are the information bus.** Everything that happens becomes claims in the ledgers of whoever could perceive it, and the
   next round's questions come from those claims. Governance acts of `binding_decision` stratum are broadcast realm-wide.
3. **MATTER is the exogenous clock.** Economy, hunger, ageing, weather, travel-leg end, term lapse and claim decay happen there.
4. **The Tenure edge is the political connective** (`hold`, `commit`, `oblige`, `contain`, `reside`, `detain`, `ban`). Killing a person closes
   every tenure naming them, so combat reaches governance by cascade.
5. **Body, stance and scar are the cross-scale carriers.** Body feeds the scene budget and the next fight's `end`; a lost field writes grudge and
   morale stance rows; witnessed value violations raise scar, which can fold a conviction.

### 5.2 Loops: what reaches what (return legs unmeasured unless stated)
| loop | status |
|---|---|
| Event → claim → question → act → Event | runs; the engine's main loop |
| deed witnessed → scar → conviction crisis | runs (9 rewrites in 4 seasons); no measured effect on a later choice (confliction weight 0); pursuits never change (0 in 4 seasons) |
| yield → stores → larder draw → wear | runs one way; repair never lands (`work` 77/0, `restore` 23/0); stores accumulate (cover 21.7 → 41.7 seasons) |
| unpaid `oblige` lapses unless `transfer` renews | closes in tests; authored obligees are term-less and cannot lapse; seed 1 shows 24 live `oblige`, seed 0 none |
| shortfall → governor claim → relief `transfer` | fires only in `harness/scarce.py` |
| wound → body → `end` → next fight | reaches the next fight; no repeat fight traced; only `tend` (0/34) raises body |
| lost field → grudge/morale → next field | not run: no field is fought |
| population ↔ hunger ↔ body | open at the shipped control; RB-5 designs it (JQ-6 sets the ratio) |
| treaty/war → mustering → march | open: `at_war` has no caller, `head` is always None |
| forge → plant (`give`) → inquiry → tell | open: every `give` was refused |
| thread operation → coherence → anything | open: TW not reached |

### 5.3 Scale
One loop serves every scale. Scale is carried by the `Rung` a seat sits on and by the prize a verb routes to. A king and a peasant cohort run
the same chooser. Each live `hold` (seat, landholding, held Record or Proposition) adds one to the scene budget. The budget counts scene
ACTIONS; a scene of more than one act is "extended" and costs 2, so budget 5 buys 7 acts (2+2+1), budget 6 buys 9, and the release ceiling is
5 scenes (`deliberate.py:89-97` is the scene ceiling; `fixtures.py:497-502` and `choose.py:643-657` are the cost budget; the two count different
quantities, which the first draft took for a dispute). A travel leg costs one act. No institution acts; the holder of a seat does. Zoom is
structural (queries aggregate up the rung ladder); there is no separate strategic turn.

---

## 6 Defects and drifts, ranked, with cause

| # | finding | cause class |
|---|---|---|
| 1 | The chooser sees verb identity, not consequence: not odds, opponent, place, witnesses or contents. 13 of 53 verbs have no alignment cell (10 uncelled by design incl. `tell`, `thread_read`, `restore`; `carry`, `examine`, `interview` are true gaps). 37 of 83 actors (cohorts) have no pursuit vector. The verbs proposal calls this the next design lever (D-V6) | design gap |
| 2 | Gate-rich, response-poor. Of 47 admitted verbs in seed 0, 22 produced a non-refusal outcome, 19 were always refused, 6 never attempted; 6 rows cannot be resolved. Causes differ: `work` waits on a works Record (H-165); `train` needs a vocation key and only `copying` exists; `destroy_record` is withheld; wrong-class referents (REM-22/23, REM-27) are defects; `give` is untraced | by-construction / defect / untraced |
| 3 | Rich oracles do not reach play: weapons, traditions, abilities (PC); formations, orders, officers (MB); the Bout kernel (SC); all of TW | seam design |
| 4 | Degenerate social default: one capability key in 430 persons; pool 2; leverage 0; obstacle ceiling = default | shipped control + missing attributes |
| 5 | No Ob owner; three dice codes; combat and field bypass the margin ladder by ruling | ruled / suspended |
| 6 | The information model runs but does not deceive: no lie verb, covers do not hide `who` from those present, forgery inert at the ceiling, no chained told-claim survived, inquiries yield nothing in the realm run | design gap / untraced |
| 7 | The initiator of violence cannot die: the actor is never written; mirror fights fell the actor about half the time and report `contest.undecided`; a cohort is deleted whole by one Felled | defect (seam) |
| 8 | No ending, no world clock in the running loop (deleted layers) | design gap |
| 9 | Documents lag the code: the verbs proposal counts 46 shipped rows (HEAD 53); `VT:` line cites drift +3 to +228; `CLAUDE.md` §3/§5 name `engine/autoload/dice_engine.py` and a campaign driver that do not exist | drift |
| 10 | Acceptance is partly doc-derived; `register --requirements` checks syntax only. The R-08 stored text is partly self-corrected: the sampler is built (requirements.yaml:1274-1285), the row stays partial because inclination cannot break ties | instrument |

---

## 7 Handles for comparison

Grades in brackets: [R] runs in the loop, [W] wired with zero successes or tests only, [D] design only.

| axis | resolution core | PC | MB | SC | FI / information | GV · FA · EC · WT · NP | chooser / persons |
|---|---|---|---|---|---|---|---|
| resolution style | success-counting d10 pool with a −1 face; fixed TN 7; variable Ob; Gaussian stand-in for big pools [R] | Gaussian roll per exchange within many probability draws; degree from accumulated damage [R, default build] | own d10 per side, each net the other's Ob; Lanchester casualties; stochastic rout [W: no field fought] | one pool roll per act [R]; exchange-race with judged tally [W, kernel] | one borrowed roll; table lookup of what is uncovered [R, empty yield] | none: deterministic state writes [R/W by verb] | utility score + Gumbel sampling, τ = 0.1 [R] |
| granularity | one roll | beat → ~10 s engagement → ≤ 12 turns | 51×51 cells, 18 ticks [W] | one act; 1–5 exchanges (kernel) | one act per inquiry | one verb per scene action; ≤ 5 scenes of ≤ 3 acts per person-season (~8–10 acts observed) | one question per deliberation |
| scale | every | 1 v 1 only | army v army [W] | person ↔ person / bench | person | hearth to realm on one ladder | all |
| state model | — | scalars; persistence only as `Person.body` | troop counts, HP, per-cell morale [W] | stateless (season); Standing/Reserve/Room (kernel) | event log + per-person claim ledgers | integer stores, 0–1000 condition, typed edges, computed aggregates | weight vectors, signed stance, bounded belief store |
| agency | engine rolls | chooser picks verb and target; engine picks every move | chooser picks `march`; defender has no chooser | chooser picks verb and target; opponent static | engine-chosen for all | every act is a person's; a seat grants a remit; no faction turn | autonomous for all; player is intended as "embedded" (D-2/IN-47) |
| information | closed-form odds exist, shown to no one | scene invisible except as witnessed Events | none in-battle | no deception channel | strictly subjective; chooser reads only own ledger; governance acts public | co-location is visibility; chronicle broadcasts binding acts | cannot see odds, opponent, place, witnesses, clock, contents |
| failure model | `Failure: []` lawful | lethal on Felled; wound scales `body`, floor 1; actor never written | loser's bodies scaled; grudge; winner untouched [W] | failed act costs the slot, writes nothing | silent: inquiry failure and refusal teach nothing | refusals are Events; unpaid service lapses | acts fail at the fold, cost a scene, leave a belief (except inquiries) |
| content model | — | authored physics tables; generic combatants | authored troop/terrain tables; armies from persons | authored closed sets; no dialogue | generated from Events | 31 authored seats, 37 settlements, 17 territories; nothing founds in the run | 46 authored cast, 37 cohorts |
| pacing | — | resolved in RESOLVE | one call at ENCOUNTER [W] | one act per scene slot | findings deposit at WITNESS in the same round, shape the next round's question | seasonal | 5 scene releases per season |
| **player position** | — | none today; IN-46 planned | — | — | `in_loop: false` for an investigation mode | — | "embedded" per repo frame; IN-47 planned |
| **control channel** | — | verb choice only | `march` only | verb + target | verb + target | remit acts via seats | the verb menu |
| **contested object** | the obstacle | the body | a field (a place) | a standing, a proposition, a matter | a record's secrecy | stores, seats, sites | — |
| **ending / progression** | — | death | — | — | — | none in the loop (deleted `victory`) | scar/conviction only; no growth path |

The repo already holds a sourced frame of 20 comparison games (`research/by_lane/00_COMPARATIVE_ANALYSIS.md:302-336`: population resolution,
named-agent cardinality, contested object, player position, control channel, coupling latency, durability/ending, clock count, legibility) and
names Mount & Blade as the closest whole-game analogue (`research/valoria_game_precedent_companion_v1.md:506`). I did not read these; the
bold axes above are taken from that frame as the audit reported it.

---

## 8 What the two proposal directories add that the code lacks

**Remediation (v9, PROPOSED, grade `paper`).** 40 items in RB-0..RB-5; verdict: even fully executed it cannot make THE NINE met. R-01..R-03 stay
met and could fall; R-04, R-05, R-07 move up without guarantee; R-06, R-08, R-09 are made honest, not met. Open forks: JQ-1..JQ-6 (JQ-2:
whether "pool only" reaches combat and mass battle — "materially different games"; JQ-3: four character-change magnitudes; JQ-4: weight→troop
value; JQ-5: optional release of the two RB-3 designs; JQ-6: hunger ratio). Rulings recorded: D-1, D-2, L1-6.

**Verbs (v2, PROPOSED, static reading).** A 92-verb roster in ten subsystems (48 descend from the 46 shipped rows then existing, 11 planned, 33
new); 127 named mechanics of which 14 are shared; 488 gaps traced to precedent and research documents (312 "closed" meaning answerable
once a mechanic exists, 58 parked, 97 out of scope, 13 stale, 8 disputed; 189 first-pass rows undisposed); a ten-attribute character model
(Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds + Thread Sensitivity) stored on the person, with the template
buildable now; build order V0..V6 for verbs and B1–B7 for persons. The roster has no critic; the from-scratch attribute work failed its
critic; precedents marked [MEMORY] are unchecked. A lexicon's body that disagrees with its "Rulings that override" header is superseded by
verbs-03 §III.5, not in conflict.

---

## 9 Method, audit record and limits

- **Pipeline.** 13 code extractors and 19 proposal extractors (Sonnet for code and concept documents, Haiku for ten lexicons and three gap
  registers) wrote cited extracts. Eight Opus synthesisers wrote Appendices E1–E8 from them. Ten Opus writers wrote the tutorials (Part D).
- **Audit (adversarial, structurally independent: read-only critics that saw the suite and the repo, not the producers' reasoning).** Six
  auditors: A, B, C accuracy of overview and appendices; D comprehensiveness against the verbs directory; E comprehensiveness against the
  remediation directory and the code tree; F logic and consistency. Counts of findings: A 15, B 13 (+2 observations), C 18, D 17, E 18, F 41; all
  are in Part C as corrections. Load-bearing outcomes: the grade convention was inconsistent across appendices (rule fixed in §0); the verbs
  appendices read lexicon bodies without the governing roster, so listed resolved items as conflicts; the first draft overstated what runs
  (PC/EC/WT/NP rows); the designed-and-deleted world layers, D-2 and the JQ forks were omitted; the R-08 reading was wrong.
- **Round-2 audit of the tutorials** (six more auditors: G, H, I, J, K accuracy per tutorial; L cross-tutorial consistency, verb coverage and teaching
  completeness). Finding counts: G 15, H 16, I 19, J 17, K 14, L 23. Load-bearing outcomes: the scene-cost rule was wrong in six tutorials (a multi-act
  scene costs 2; the "dispute" is resolved); six authored seats (the throne among them) can never be refilled once vacant; occupation for `seize`
  is members present, not only a march; the rout rule for a one-subunit army is 100 troops, not 80; the first Column experiment never took effect;
  inquiries do not draw on any capability key; `forgive` raises the stance term. All were applied by the tutorial writers after re-opening the cited lines.
- **Control run.** An independent script re-ran the realm (seeds 0, 1, 2) and showed (a) results are deterministic across processes, (b) the
  first draft's per-verb counts mixed counting methods, (c) several "never attempted" statements are seed 0 only.
- **Not done / residual risk.** The corrected tutorials were not audited a third time (the repo's own rule against looping a gate). The reference
  appendices (Part E) are first-draft text with a known error list; the tutorials and the Errata supersede them. Lexicon appendices still rest on a first-pass gap
  register that describes itself as stale. `.designs/` (quarantined) was not read. Quantities from runs are one horizon (two seasons) and three
  seeds. The 72% sampler-override figure is a harness-slice reading, not a season measurement. Why `give`, `march` and `commit` are refused
  was not traced.
- **Status.** Everything under `proposals/` is PROPOSED and ratifies nothing; this suite is reference, not a ruling, and is not committed.

---
