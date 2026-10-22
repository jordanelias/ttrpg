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
  in the realm run. A refusal gate firing is not the verb executing. A behaviour that runs inside the real season only on an act a harness
  callback hand-built (round 3: a settlement `march` fighting a field) stays TESTS-ONLY: the grade is about the natural run (file 13 Part 3 R-F5).
- **DESIGN-ONLY**: no executing code (a proposal, a stub, an empty hook, a deleted layer).

**Run figures.** "The realm run" is `build_realm(seed)`, two seasons, with the chooser built as `populated.run` builds it. The control script
is `ctl/control.py` in this directory; outputs for seeds 0, 1, 2 are `ctl/realm_seed*_2seasons.txt`. It counts per verb the acts that
**reached the fold** ("att", `d.resolved`, appended in `loop/resolve.py:377-379`) and the acts with at least one non-refusal event ("ok": an
Event whose kind's last word is not on the script's refusal list, `ctl/control.py:13, :21`; so "ok" is not Partial-or-better: seed 0's 3 `speak`
"ok" are all `matter.turned`, a Failure, and for `fight` and `accept` it means a Felled or Wounded subject).
Three kinds of act never reach the fold and are not counted: contested or graded acts refused at admission (`loop/resolve.py:1025`), acts whose
actor was already gone (`:974`) and acts refused for an obstacle above `obstacle_refusal_multiple` times the pool (`:980`); an ordinary
precondition refusal of an uncontested act does reach the fold and is counted. The act store
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
#494 (IN-27) the season *reports* endings: `world_q.endings_reached` is "a Query over holds and seats that the season reports -- never an actor" (`queries/world_q.py:1764-1766`; the driver calls it "A READ", `loop/driver.py:515`) over the
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
| **GV** | — | MATTER economy + remit verbs | release 45/3, issue 6/5, dispatch 18/6 (writes nothing); revoke 6/0, convene 1/0, requisition 2/0, found 24/0, build 19/0; confer, establish, oblige, seize 0 formed [confer 5/1, establish 5/0, oblige 24/22]. Seven of the 32 seats have no conferral basis and can never be refilled once vacant (§6 #11); only `off_duke_valorsmark` sits directly above a revocable seat (`state/gate.py:452-484`; six (seat, target) pairs at build, all through it, held by the King), and it is vacant from tick 0 in every seed, so no `revoke` can pass after that, `office` operand or not | MATTER RUNS; release, issue, dispatch RUN; the rest TESTS-ONLY |
| **FA** | — | membership, `survey`, goal salience | survey 57/13; covenant 13/0 [4/0]; sabotage 34/0; `at_war` no non-test caller; `faction_q.head` always None | state RUNS; survey RUNS; covenant, sabotage, seize TESTS-ONLY; declare, recruit, levy, conspire DESIGN-ONLY |
| **EC** | — | yield, draw, wear; transfer, requisition, work, restore, found, build | `stores.changed` 111, `yield.taken` 74; transfer 45/1; work 77/0; restore 23/0. Every settlement gets one Site of each yielding kind (`harness/populated.py:771-776`), so all 37 yield the same four goods; yield reads a Site's condition, not people. `work` can never run on dwellings and garrisons (248 of 322 Sites: their `band_floors` are empty, `rosters.yaml:2631-2632`), and `restore` refuses a Site at full condition | yield, draw, wear RUN; trade, craft, price, tax, credit DESIGN-ONLY |
| **WT** | 17 territories, 37 settlements, 55 adjacencies in the geography file | `move`, `migrate` as containment hops; one scene-budget leg each | move 42/16; migrate 81/0 [143/0]: a destination comes only from places the mover's own ledger names (`queries/world_q.py:2111`), every chosen hearth was full, and none of the 185 hearths empty at build was chosen | move RUNS; migrate TESTS-ONLY; routes, terrain, hazards DESIGN-ONLY |
| **NP** | — | cohorts; tend, train, forgive, give, commit | forgive 1/1; tend 34/0; train 38/0; give 16/0 [seed 2: 19/1]; commit 61/0 [56/1] | forgive RUNS; `give` executes at seed 2 only, `commit` at seeds 1 and 2; the rest TESTS-ONLY; kin, marriage, household DESIGN-ONLY; births set aside by ruling (ED-WR-0011, Option A, Jordan 2026-09-13: a closed cast of 46 "for now"; `loop/census.py:39-40`) |
| Persons / character model | 15 pursuits, 7 axes, 5 affiliations | carrier and crisis | scar ≥ 3 on 35 persons in 4 seasons; 9 convictions rewritten (seed 0; 5 after 2 seasons, and none in 2 seasons at seed 1, I1 verification J2); pursuits changed on 0 | carrier RUNS; attributes, template DESIGN-ONLY |

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
   next round's questions come from those claims. Any Event whose kind a `binding_decision` row emits is broadcast realm-wide (a kind
   filter, `epistemic.py:685-686`), including `argue`'s `pursuit.moved` and MATTER's `tenure.closed`.
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
| wound → body → `end` → next fight | runs: seed 0, tick 0, the King (`p_npc_020`) is Wounded to body 450 (`end 2`) in a fight with `p_npc_006`, who is felled, and Felled the same tick by `p_npc_032`'s `accept`; over seeds 0-2, 11 combat calls met a subject below `end 4` and 7 of them Felled him (round-3 seam trace at `51d7b05`); only `tend` (0/34) raises body |
| lost field → grudge/morale → next field | no field is fought in the realm runs; a hand-built settlement march fights one inside the season (`field.lost`, §3 MB row); the return leg is unmeasured |
| population ↔ hunger ↔ body | open at the shipped control; RB-5 designs it (JQ-6 sets the ratio). Even switched on, no score term reads hunger: `urgency(subsistence)` adds the same amount to every candidate and "CANNOT CHANGE ANY DECISION" (`decision/choose.py:220`) |
| treaty/war → mustering → march | open: `at_war` has no non-test caller, `head` is always None; a hand-built WAR Proposition plus `commit` makes `at_war` True and nothing reads it (I1 verification claim 5) |
| forge → plant (`give`) → inquiry → tell | open: `give` reached the fold 16 / 21 / 19 times and executed once (seed 2) |
| thread operation → coherence → anything | open: TW not reached |

### 5.3 Scale
One loop serves every scale. Scale is carried by the `Rung` a seat sits on and by the prize a verb routes to. A king and a peasant cohort run
the same chooser. Each live `hold` (seat, landholding, held Record or Proposition) adds one to the scene budget. The budget counts scene
ACTIONS; a scene of more than one act is "extended" and costs 2, so budget 5 buys 7 acts (2+2+1), budget 6 buys 9, and the release ceiling is
5 scenes (`deliberate.py:89-97` is the scene ceiling; `fixtures.py:497-502` and `choose.py:643-657` are the cost budget; the two count different
quantities, which the first draft took for a dispute). A travel leg costs one act. Budgets drift up, because every held Record and every
uttered Proposition is a hold and `create_record` and `utter` always succeed: at seed 0 the mean budget is 5.57 at build, 6.41 after tick 0
and 7.69 after tick 1, and after tick 1 eleven of 74 persons hold more than 10 actions, an excess no round can release (H-92;
`loop/deliberate.py:107-113`; round-3 probe). Acts per acting person per tick at seed 0: 8.1 then 9.4 formed, 6.4 then 7.7 reaching the
fold, at most 15 (the 5-scene × 3-act ceiling is reached in both ticks). State the basis whenever a number is given. No institution acts;
the holder of a seat does. Zoom is structural (queries aggregate up the rung ladder); there is no separate strategic turn.

---

## 6 Defects and drifts, ranked, with cause

| # | finding | cause class |
|---|---|---|
| 1 | The chooser sees verb identity, not consequence: not odds, opponent, place, witnesses or contents. 13 of 53 verbs have no alignment cell (10 uncelled by design incl. `tell`, `thread_read`, `restore`; `carry`, `examine`, `interview` are true gaps). 37 of 83 actors (cohorts) have no pursuit vector. The verbs proposal calls this the next design lever (D-V6) | design gap |
| 2 | Gate-rich, response-poor. Of 47 admitted verbs in seed 0, 22 produced a non-refusal outcome (beyond `march`'s declaration), 19 were always refused (three of them, `argue`, `examine`, `determine`, before the fold), 6 were never formed; 6 rows cannot be resolved. Causes differ: `work` waits on a works Record (H-165) and can never run on a dwelling or garrison (empty `band_floors`); `examine`'s `site` is the question's subject, never a Site; no natural `march` names a settlement; `migrate` names only full hearths; `revoke` lacks its `office` operand and has one usable seat (§3 GV row); `train` needs a vocation key and only `copying` exists; `destroy_record` is withheld; wrong-class referents (REM-22/23, REM-27) are defects; `give` is untraced. Paired controls show the effects run once the operand is right (I1 verification claim 2) | by-construction / defect / untraced |
| 3 | Rich oracles do not reach play: weapons, traditions, abilities (PC); formations, orders, officers (MB); the Bout kernel (SC); all of TW | seam design |
| 4 | Degenerate social default: one capability key in 430 persons; pool 2; leverage 0; obstacle ceiling = default | shipped control + missing attributes |
| 5 | No Ob owner; three dice codes; combat and field bypass the margin ladder by ruling | ruled / suspended |
| 6 | The information model runs but does not deceive: no lie verb, covers do not hide `who` from those present, forgery inert at the ceiling, no chained told-claim survived, inquiries yield nothing in the realm run (`examine` never passes admission; FI-03's trail deposits nothing in seeds 0-2; a Partial finding closes that trail to its finder for good, `epistemic.py:356-366`); people learn only by being present or by the chronicle | design gap / untraced |
| 7 | The initiator of violence cannot die: the actor is never written; mirror fights fell the actor about half the time (33 of 59 realm calls, seeds 0-2) and report `contest.undecided` or `body.changed`; every Wounded or Untouched band is a fight the attacker lost; a cohort is deleted whole by one Felled | defect (effect): the seam returns both parties' wound states (`seam/wrappers/combat.py:230`); `_eff_kill` reads the subject's only (`loop/effects_combat.py:108`, `:125`); verbs-09 M1 names the fix (`proposals/2026-10-16-verbs/2026-10-16-verbs-09-lexicon-personal-combat.md:316`) |
| 8 | No ending is reached and none halts the loop; no world clock. Since PR #494 the season reports `endings_reached` each tick (§2.3): its victory row is unreachable in computed play by its own note, and the realm reached no ending in seeds 0-2. IN-23's legitimacy and stability are one person's windowed estimates read only by `harness/storybar.py`; IN-37's chronicle renderer (`harness/chronicle.py`) is an observer the loop never imports. Goals are attention-only: "it never acts, and nothing aggregates" (A-31, `engine/season/goals.yaml:10-12`), and nothing tests whether one is met | design gap (deleted layers; the ending rows are `[ASSUMPTION]`-graded) |
| 9 | Documents lag the code: the verbs proposal counts 46 shipped rows (HEAD 53); `VT:` line cites drift +3 to +228; `CLAUDE.md` §3/§5 name `engine/autoload/dice_engine.py` and a campaign driver that do not exist | drift |
| 10 | Acceptance is partly doc-derived; `register --requirements` checks syntax only. The R-08 stored text is partly self-corrected: the sampler is built (requirements.yaml:1274-1285), the row stays partial because inclination cannot break ties | instrument |
| 11 | No succession. Seven of the 32 built seats have no conferral basis and can never be refilled once vacant: King, Queen (the Widow Regent row), Prince (the Heir row), Princess, Duchess of Hafenmark, Duke of Valorsmark (`conferral: null`, `offices.yaml:188, 201, 214, 240, 253, 266`) and the unauthored guild-leader seat `off_npc_084`, which `harness/populated.py:1240-1250` builds with no row and so with conferral None; `_req_confer` refuses them first (`loop/predicates.py:126-127`) and `succeed` has no effect (`verb_table.yaml:1113`). The King dies at tick 0 in every seed; seats vacated by the end of season 2 are 8 / 7 / 10 (seeds 0 / 1 / 2), null-basis seats 3 / 5 / 6 of them, and one seat is refilled across the three seeds (a self-conferral at seed 1) | by construction (null rows) / design gap (no transmission) |
| 12 | The control run's "att" column counts acts that reached the fold, not acts formed (§0): 275 acts in seed 0 are formed and refused before the fold and do not appear, which the first draft read as "never attempted" for `argue`, `examine` and seed-1 `speak` | instrument |
| 13 | The only closed-form odds helper, `sigma_leverage.p_success`, is the Gaussian stand-in and understates Partial-or-better on the real social dice by 7-15 points (pool 2 / Ob 2: 14.4 % against 26.0 % exact; pool 2 / Ob 1: 43.0 against 58.0), so a surface that printed it would show worse odds than the dice deal; under the ruled ladder Partial is never the most likely band at pools 1-8 against Ob 1-4 (largest 32 %, pool 2 / Ob 1). Layer 1 says no state is hidden from the player (AX-7, `architecture/meta/01_AXIOMS.md:301-302`) | latent (no surface reads it) |

---

## 7 Handles for comparison

Grades in brackets: **[R]** runs in the loop (ERRATA G1 RUNS-IN-LOOP), **[W]** wired with
zero successes, or tests, harnesses and hand-built acts only, **[D]** design only, **[P]** proposed. The axes in §7.1-§7.2 are those of
*Twenty Games, One Frame* ("20G", an upload that is not in the tree: Part 2 §2.1 defines them, §2.2 plots twenty titles, §2.3 names four
empty cells, Part 4 lists nine asymmetries). The repo's earlier reading of Valoria on those axes is `research/by_lane/00_COMPARATIVE_ANALYSIS.md:302-336`
("COMP"); the cells below were re-derived from the code at `51d7b05`, not copied from it. Precedent pointers name a file under
`research/game_precedent_suite/` ("T07" = `tutorials/T07_mass_battle.md`, "R4" = `tables/R4_combat_social_rpgs.md`) and the game heading,
and carry the source's own tag. Precedent is tier-3 reference: it shows what Valoria lacks or does differently, and decides nothing.

### 7.1 The 20G axes, filled for Valoria

| 20G axis (its poles) | Valoria as built | as proposed | nearest verified precedent |
|---|---|---|---|
| **1 population resolution** (individual → household → typed pool → token → absent) | two tiers at once: 46 named persons as individual objects [R]; the populace as one acting Person per settlement (37 cohorts at `weight` 2), a token whose size nothing writes at runtime [R]; population is fixed at build and only falls (83 → 74 persons at seed 0 in two seasons, every death combat) | growth at CENSUS to capacity (J-C-9, COMP:534) [P]; hunger binds settlements (RB-5) [P] | individual citizens who age five times a year: Banished (T04 [V3 wiki Seasons, Citizens]); pops by class: Imperator (T12 [V3 IIa]) |
| **2 named-agent cardinality** (none → scarce and capped → many → unbounded) | scarce and closed by ruling, not by a slot rule: 46, a closed cast "for now" (ED-WR-0011, ruled Option A, `registers/editorial_ledger_wr_archive.jsonl`; `loop/census.py:39-40` "NO CLOCK GENERATES ANYTHING"); CENSUS individuation exists and fired 0 times in seeds 0-2 [W]; falls by death only (46 → 37 named at seed 0 in two seasons) | births parked on the ruling ("We will return much later") | a hard cap of eight knight slots: Knights of Honor II (T13 [V3 WK Royal Court]); 1,000+ playable officers: Romance of the Three Kingdoms VIII Remake (T13 [V3 R8 3100]) |
| **3 contested object** (land / allegiance / labour / time / logistics) | the body (`fight`, `accept`) [R]; a standing, a proposition or a matter (the social roll) [R]; seats (`confer`, one success in three seeds) [W]; stores (`requisition`, 0 successes) [W]; land by `seize`, licensed by members present (0 formed) [W], and a field only on a hand-built march [W]; allegiance moves only by a person's own `commit` / `release` [R]. Labour and time are uncontested: yield reads a Site's condition and no person (`loop/matter.py:589-591`), and there is no clock to race | land by occupation (IN-13, COMP:311) [P]; troops levied from settlements (J-C-2) [P] | allegiance: Pax Pamir (T15); labour: Banished (T04); time: Against the Storm, lost at Impatience 14 (T15 [V3 wiki; Steam]); logistics: Manor Lords (T04) |
| **4 player position** (administrator above the system ↔ embedded actor) | none in the loop [R, an absence]; a callback seat in the harness [W]; outside the loop a stdin-played social contest and two designer workbenches (§2.1) [W] | embedded: "for a player character the player IS the decision procedure" (`architecture/meta/04_CODE_ARCHITECTURE.md:844-846`); IN-46 played fight, IN-47 character-sheet space (D-2) [P] | embedded and continuing through an heir: Crusader Kings III (T01 [V3 GF `reactive_advice_succession_desc`]); administrator who "never command[s] a dwarf directly": Dwarf Fortress (T03 [V3 DFq]) |
| **5 control channel** (rung 1 direct order → 2 zone → 3 delegate → 4 lobby a body) | a person commands only his own acts: one verb and subject from the menu per scene slot (rung 1) [R]; rung 3 inert: `dispatch` writes nothing (`verb_table.yaml:380`) and an `issue`d writ binds nobody (I1 verification claim 4) [R as an Event, no effect]; rung 4 partly: `petition` / `open_case` → a bench's `determine` (one disposal, seed 1) [W]; rung 2 absent [D] | the vote over commitments is blocked on J-4 (COMP:313) [P] | rung 2: Dwarf Fortress zones and stockpiles (T03 [V3 DFq]); rung 3: RTK XIV area overseers (T13 [V3 R14 4200]); rung 4: Victoria 3's three-phase law enactment (T01 [V3 V3REF defines + laws]) |
| **6 coupling latency** (immediate / shock-punctuated / lagged cohort) | one round: an Event deposits at WITNESS in the round it happens and can shape the next round's question (`loop/driver.py:510`) [R]; shocks: a death closes every tenure naming the dead (the King dies at tick 0 in every seed and vacates two seats) [R]; a slow lag on belief only: claim decay 5 a season [R]; no lagged cohort: population is fixed and births are ruled out for now; the one scheduled lag, the 4-season `oblige` term, never renewed (`term.renewed` 0) [W] | a lagged population (J-C-9) [P] | lag: Banished, where children take about ten years to work (T04); shock: at a death the succession law picks the heir and titles may split: Crusader Kings II (T12 [V3 CK2F Succession Laws 2018-01-31]); scheduled lag: Victoria 3 law checkpoints about every 100 days (T01 [V3 V3REF defines + laws]) |
| **7 durability and reset** (persistent / ephemeral / ephemeral with meta-progression) | persistent, and nothing halts: the season reports `endings_reached` (§2.3), whose victory row is unreachable in computed play by its own note; no ending reached in seeds 0-2 [R as a read; reaching one W] | IN-27's relational victory is the built Query; GD-1's Accord, Stability and sustain clauses have no carrier (`rosters.yaml:2531-2541`) | ephemeral with meta-progression: Against the Storm (T15 [V3 wiki; Steam]); game over at no heir or at 1453: Crusader Kings III (T01 [V3 GF `game_over_desc`]) |
| clock count (discipline, not an axis) | one world clock, `w.tick` (one season), with five rounds as a driver-local index; a fight (≤ 12 turns) and a battle (≤ 18 ticks) run to completion inside one step: auto-resolve only [R] | a paused, played fight (IN-46) would give the second clock a player [P] | the per-battle choice of fighting or auto-resolving: Total War (T07 [V3 manual p21, p47]) |
| legibility (discipline) | no surface [R, an absence]; closed-form odds exist and are shown to no one, and the only helper understates them (§6 #13); refusals are Events kept in the actor's own ledger; the designer workbenches show branch odds outside the loop [W] | "No state is hidden from the player" (AX-7, `architecture/meta/01_AXIOMS.md:301-302`); IN-47 [P] | the pass probability shown on hover: Disco Elysium (R4 [V2 gry-online.pl poradnik]); the loss timer given a face ("Impatience"): Against the Storm (T15) |

### 7.2 The 20G asymmetries and empty cells, against Valoria

| 20G asymmetry | Valoria | evidence |
|---|---|---|
| A1 allegiance with a delay | crossed in shape (belief travels by telling and regard is read at choice time), not delayed | `news.told` 4 / 7 / 6 in seeds 0-2; `loyalty` is computed and read only at world-gen to seed stance (`data/cast.py:328`; `harness/populated.py:620, :1047`) |
| A2 zone plus delegate | not crossed | rung 2 absent, rung 3 inert (§7.1 row 5) |
| A3 conscription that removes a cohort | not crossed | an army is the faction's members present (`queries/world_q.py:1473` `mustered`); no levy verb; one Felled deletes a cohort whole, so war removes eaters and no yield |
| A4 relational victory | partly built | `endings_reached` scores holds under one faction (IN-27); unreachable in computed play |
| A5 graduated agent layer | crossed in mechanism, not in data | every consequence ships behind a fixture dial with a zero control (`body_step`, `age_step`, `illness_rate`, `telling_privacy`, `confliction_weight`, `scar_weight_shift`) and the chooser's τ = 0.1; the 37 cohorts carry no pursuits |
| A6 ephemerality with carry-over | not applicable | persistent |
| A7 dual-use political currency | not crossed | no currency; `coin` is registered and no site yields it (file 01 §5) |
| A8 scarce named agents over an anonymous many | structure crossed, loop not | 46 named over 37 cohorts; no steward acts on a populace, and yield reads no people |
| A9 belief with provenance | crossed; deceit absent | every Claim keeps `source` and `chain` (`state/carriers.py:291-348`), refracted by remove; no lie verb; forgery inert at the ceiling; chained claims nearly unused (0 / 0 / 1 alive after two seasons in seeds 0-2, round-3 probe) |

20G's empty cells, read against Valoria: **1** fine populace × scarce named agents: the structure is there (46 named over 37 cohorts), the
loop is not. **2** labour contested between players: empty. **3** lagged allegiance: crossed in shape, thin in delivery. **4** zone and
delegate together: empty. 20G bounds these itself: "Read 'empty' as corpus-bounded" (its §2.3, naming Dwarf Fortress, RimWorld, the Victoria
series and Frostpunk as likely occupants); the precedent suite covers all four (T03, T01, T04).

### 7.3 The handles the round-2 audit found missing (file 13, audit L)

| handle | Valoria as built | nearest verified precedent |
|---|---|---|
| **action economy across subsystems** | one budget for every subsystem, in scene actions per season: `max(1, 5 + live holds − body bands − legs)`; a scene of more than one act costs 2; ceiling 5 scenes × 2 = 10 actions; no verb has its own action price; budgets drift up with holds (§5.3). Per-subsystem costs and degrees: file 01 §3 | up to two actions a turn, each court card usable once: Pax Pamir (T15 [V3 p8-9]); two actions a season: King of Dragon Pass (T16 [V3 manual]); Body Points per command, refilled each season: Genghis Khan II (T13 [V3 IA:GK2 l.467-490, 705-718]) |
| **in-world time per season / round / tick** | one tick is one season and `w.tick += 1` is the only advance (`loop/driver.py:519`); five rounds per season are a driver-local index with no stated duration; no year exists (`season_of_year` is `None`, `queries/world_q.py:954`); a combat turn is "~10 s"; a battle tick has no stated duration. File 01 §4 | one turn = one year: Old World (T01 [V3 FW-OW]); one turn per season: Rome II (T12 [V3 R2M 0015a]); one turn = one month: Dominions (T17 [V3 IW5:introduction_to_dominions]); five seasons then Sacred Time: King of Dragon Pass (T16 [V3 manual]) |
| **campaign length and end state** | none: the realm runs as many seasons as the harness asks; nothing halts; endings are reported and none is reached; no world clock (the MS track has no caller) | a default end date of 1453 and game over without an heir: Crusader Kings III (T01 [V3 GF]); a default 300-turn limit: Oriental Empires (T12 [V3 OEW FAQ]); "no win state": Banished (T04 [V3 steam news]) |
| **resolution families, with genre analogues** | (a) social path and graded inquiries: a success-counting d10 pool against an obstacle, read off a four-band margin ladder: a bell like 2d6, but in whole steps (one Ob step moves Partial-or-better by up to 32 points at pool 2; T01 tutorial) [R]; (b) personal combat: a beat-level duel simulated to the first felling inside one step, degree off the subject's wound tracker [R]; (c) mass battle: a 51 × 51 grid with Lanchester-linear casualties, auto-resolved at ENCOUNTER [W]; (d) governance, economy, travel, NPC life, factions: deterministic typed preconditions, no draw [R]; (e) the chooser: a utility score with Gumbel sampling at τ = 0.1 [R] | (a) 2d6 + skill against a difficulty: Disco Elysium (T05 [V3 DEw/Skills]); a flat d20 against a DC: Baldur's Gate 3 (T05 [V3 BGw/Dice_rolls]); (b), (c) auto-resolve beside a played battle: Total War (T07 [V3 manual p21]); a square-grid wargame: Field of Glory II (T07 [V3 FoG2 Medieval manual 2022-07-25]); (e) needs-and-traits autonomy for every unplayed Sim: The Sims 4 (T10 [V3 wiki Free_will]) |
| **sources and sinks per resource** | grain and salt: harbour yield in, cohort larder draw out; ore: no reader; timber: the works cost; coin: none; stores never cap, spoil or cost upkeep (realm stores 0 → 9,250 in two seasons, every seed). Full table: file 01 §5 | per-minute maintenance on most buildings: Anno 1800 (T10 [V3 wiki Marketplace]); heat allocated per district and paid in coal or oil: Frostpunk 2 (T04 [V3 steam 1.3]) |
| **player-interface position** | none in the loop; a test-only callback seat; a stdin social contest and two designer workbenches outside it (§2.1) | a pre-battle panel with a strength comparison and projected result: Total War (T07 [V3 manual p21, p47]); one played Sim among autonomous ones: The Sims 4 (T10 [V3 wiki Free_will]) |
| **information model against standard fog of war** | no map and no sight radius: each person holds a bounded ledger (cap 200) fed only by WITNESS channels (co-location first; the chronicle broadcasts binding-row kinds realm-wide), refracted by remove, decaying 5 a season; the World holds the truth and no decision code reads it (AX-2). The fog is epistemic and per person, not spatial | map fog as a setup option: Shadow Empire (T18 [V3 manual 3.1.3.2]); a reconnaissance level that sets how much of the enemy order of battle you see: Ultimate General (T07 [V3 ugcw wiki]); a fixed truth beside a separate player belief: Return of the Obra Dinn (R5 [V2 wiki General]); "player knows only what they find": Shadows of Doubt (R5 [V2 store page]); hidden schemes that leak through breaches: Crusader Kings III (R1 [V2 GF]) |

### 7.4 Per-subsystem handles (the round-1 table, corrected in round 3)

| axis | resolution core | PC | MB | SC | FI / information | GV · FA · EC · WT · NP | chooser / persons |
|---|---|---|---|---|---|---|---|
| resolution style | success-counting d10 pool with a −1 face; fixed TN 7; variable Ob; Gaussian stand-in for big pools [R] | Gaussian roll per exchange within many probability draws; degree from accumulated damage [R, default build] | own d10 per side, each net the other's Ob; Lanchester casualties; stochastic rout [W: no natural field; runs in the loop on a hand-built settlement march] | one pool roll per act [R]; exchange-race with judged tally [W, kernel] | one borrowed roll; table lookup of what is uncovered [R, empty yield] | none: deterministic state writes [R/W by verb] | utility score + Gumbel sampling, τ = 0.1 [R] |
| granularity | one roll | beat → ~10 s engagement → ≤ 12 turns | 51×51 cells, 18 ticks [W] | one act; 1–5 exchanges (kernel) | one act per inquiry | one verb per scene action; ≤ 5 scenes of ≤ 3 acts per person-season (seed 0, per acting person per tick: 8.1 / 9.4 formed, 6.4 / 7.7 reaching the fold, at most 15) | one question per deliberation |
| scale | every | 1 v 1 only | army v army [W] | person ↔ person / bench | person | hearth to realm on one ladder | all |
| state model | — | scalars; persistence only as `Person.body` | troop counts, HP, per-cell morale [W] | stateless (season); Standing/Reserve/Room (kernel) | event log + per-person claim ledgers | integer stores, 0–1000 condition, typed edges, computed aggregates | weight vectors, signed stance, bounded belief store |
| agency | engine rolls | chooser picks verb and target; engine picks every move | chooser picks `march`; defender has no chooser | chooser picks verb and target; opponent static | engine-chosen for all | every act is a person's; a seat grants a remit; no faction turn | autonomous for all; player is intended as "embedded" (D-2/IN-47) |
| information | closed-form odds exist (Gaussian, understating), shown to no one | scene invisible except as witnessed Events | none in-battle | no deception channel | strictly subjective; chooser reads only own ledger; governance acts public | co-location is visibility; the chronicle broadcasts binding-row Event kinds | cannot see odds, opponent, place, witnesses, clock, contents |
| failure model | `Failure: []` lawful | lethal on Felled; wound scales `body`, floor 1; actor never written | loser's bodies scaled; grudge; winner untouched [W] | failed act costs the slot, writes nothing | silent: inquiry failure and refusal teach nothing | refusals are Events; unpaid service lapses | acts fail at the fold, cost a scene, leave a belief (except inquiries) |
| content model | — | authored physics tables; generic combatants | authored troop/terrain tables; armies from persons | authored closed sets; no dialogue | generated from Events | 31 authored seats + 1 derived, 37 settlements, 17 territories; nothing founds in the run | 46 authored cast, 37 cohorts |
| pacing | — | resolved in RESOLVE | one call at ENCOUNTER [W] | one act per scene slot | findings deposit at WITNESS in the same round, shape the next round's question | seasonal | 5 scene releases per season |
| **player position** | — | none today; IN-46 planned; the combat workbench configures and traces a duel for a designer | none; the mass-battle workbench configures an army for a designer | none in the loop; a standalone stdin kernel harness, `agon_harness.py` | `in_loop: false` for an investigation mode | — | "embedded" per repo frame; IN-47 planned |
| **control channel** | — | verb choice only | `march` only | verb + target | verb + target | remit acts via seats | the verb menu |
| **contested object** | the obstacle | the body | a field (a place) | a standing, a proposition, a matter | a record's secrecy | stores, seats, sites | — |
| **ending / progression** | — | death | — | — | — | endings reported each season, none reached (IN-27); nothing halts | scar/conviction only; no growth path |

**TW** has no column above because nothing of it reaches the loop: resolution a d10 pool at TN 7 [W]; state two integers per
practitioner, a recoverable stretch of up to 6 over a lasting resting point [W]; failure model none in the loop, the crossing only
relabels and latches [W]; control channel none (no thread verb is resolvable). Nearest verified precedents for a cost track of this
shape: Sunless Sea's Terror, which rises in the dark and is capped back to 50 in port (T08 [V3 SSf Terror, Returning_to_London]); Don't
Starve's revive bought with 30 maximum Health (T09 [V3 DSw Meat_Effigy]); Pathologic 2's death penalties, which bind every save in the
file (T09 [V3 PLw Game_Mechanics]). The closest whole-game analogue the repo names is Mount & Blade
(`research/valoria_game_precedent_companion_v1.md:506`); the suite's Bannerlord and Warband tutorials are T02.

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
  scene costs 2; the "dispute" is resolved); six authored seats (the throne among them) can never be refilled once vacant (seven built seats,
  counting the unauthored `off_npc_084`: round 3, file 13 Part 3 R-F1); occupation for `seize`
  is members present, not only a march; the rout rule for a one-subunit army is 100 troops, not 80; the first Column experiment never took effect;
  inquiries do not draw on any capability key; `forgive` raises the stance term. All were applied by the tutorial writers after re-opening the cited lines.
- **Control run.** An independent script re-ran the realm (seeds 0, 1, 2) and showed (a) results are deterministic across processes, (b) the
  first draft's per-verb counts mixed counting methods, (c) several "never attempted" statements are seed 0 only. Round 3 found that its "att"
  column counts acts that reached the fold, not acts formed (§0, §6 #12). It is byte-identical on `51d7b05`.
- **Round 3 (precedent dispositions and verification).** A verified precedent suite (`research/game_precedent_suite/`) was routed game by game
  to the ten tutorials; thirteen read-only Opus critics gave every item a disposition (HAS / LACKS / DIFFERS / CONTRADICTS / DISCARD); an
  independent probe re-checked the code-capability inventory those critics read; ten appliers made the CONTRADICTS edits after re-opening
  each cited line at `51d7b05`; this file, file 01 and file 13 were revised by one more applier, who re-ran the decisive probes at `51d7b05`
  (control run, combat seam trace, hand-built march, seat conferral and revocation scans). The rulings are file 13 Part 3; §7 was rebuilt
  from 20G's own axes rather than the audit's report of them.
- **Not done / residual risk.** The corrected tutorials were not given a third accuracy audit (the repo's own rule against looping a gate);
  round 3 was a comparison pass with verification probes, not a re-audit. The reference appendices (Part E) are first-draft text with a known
  error list; the tutorials and the Errata supersede them. Lexicon appendices still rest on a first-pass gap register that describes itself as
  stale. `.designs/` (quarantined) was not read. Quantities from runs are one horizon (two seasons) and three seeds. The 72% sampler-override
  figure is a harness-slice reading, not a season measurement. `march` and `commit` refusals are traced (I1 verification claim 2: no natural
  march names a settlement; computed `commit`s rarely name a Proposition); why `give` is refused was not traced.
- **Status.** Everything under `proposals/` is PROPOSED and ratifies nothing; this suite is reference, not a ruling. It was merged in PR #495;
  the round-3 revision is a later change on top of it.

### Round-3 corrections

Each line: old claim → new claim (evidence; the R-ids are file 13 Part 3). Probes re-run at `51d7b05`.
- Header "HEAD `a4ca9a5`" → written at `a4ca9a5`, revised at `51d7b05`; control run byte-identical there.
- §0 "att" = "acts that reached RESOLVE" → acts that reached the fold, with formed counts where they differ (R-F3; `loop/resolve.py:377-379`); TESTS-ONLY covers behaviour seen only on hand-built acts (R-F5).
- §1 fact 2: the zeros are mostly formation defects; the effects run on hand-built acts (I1 verification claim 5).
- §2.1 "No player interface exists" → none reaches the season loop; `agon_harness.py` and two designer workbenches outside it (R-F4); Queries row adds `endings_reached`, `legitimacy`, `stability` (R-F12); WITNESS row: chronicle is a kind filter (CROSS C5).
- §2.3 "no ending condition" → endings reported each season since PR #494, unreachable in computed play, none reached, nothing halts (R-F12).
- §3: formed counts for `fight`, `accept`, `tell`, `speak`, `argue`, `determine`, `research`, `surveil`, `examine` (R-F3); MB grade note on the hand-built field (R-F5); `post_remit` executes at seeds 1-2 (R-13); GV seats and revocation (R-F1, R-F2); EC and WT causes (R-F9, R-F10); NP per-seed grades and the births ruling (R-F7).
- §5.1 binding acts broadcast → binding-row Event kinds broadcast (CROSS C5). §5.2: wound loop runs (R-14); lost-field loop fought by hand (R-F5); hunger enters no score (R-F10); `give` executed once at seed 2. §5.3: budget drift and acts per acting person per tick (R-F6).
- §6 rows 2, 6, 7, 8 revised; rows 11 (no succession, R-F1), 12 (the ctl column, R-F3), 13 (the odds helper, R-F11) added.
- §7 rebuilt from 20G's own axes, asymmetries and empty cells, with graded cells, the seven handles audit L listed as missing, and a precedent pointer per handle into `research/game_precedent_suite/`; the round-1 table kept as §7.4 with corrected cells and a TW note.
- §9: round-3 method added; "the suite is not committed" → merged in PR #495; `march` and `commit` refusals now traced.

---
