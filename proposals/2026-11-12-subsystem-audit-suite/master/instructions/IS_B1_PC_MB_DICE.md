# Instruction suite, lane IS-B1 — personal combat (PC), mass battle (MB) and the dice (DICE) as standalone playable games

## Status: PROPOSED (stage 4 of `STAGES.md`; batch-shaped instructions for workplan v12; nothing here is applied; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `b07fc1c` (working tree, 2026-11-12). Producer: Fable, lane IS-B1 of `master/INSTRUCTION_SUITE_ORDER.md`. One round; no second wave.

Parts: this file (the frame, PC) · `IS_B1_PC_MB_DICE_part2.md` (MB, DICE, the tables v12 takes, what was not checked).

## 0. What this file is, and how v12 uses it

It is the instruction set for three subjects, written as items a `/methodology-execute` batch can run. It does **not** restate the coding instructions the proposals already carry (`proposals/03_PC_*`, `04_MB_*`, `10_DICE_*`, `16_PESSIMIST_{PC,MB,DICE}_*`, `26_MASS_BATTLE_*`, `27_MB_*`, `29_DICE_*`, `U5b_*`, `U5a_DICE_owed_edits`). For each subject it states:

1. **the standalone-playable test** (`INSTRUCTION_SUITE_ORDER.md`, third paragraph): the entry, the scenario or seed, the player-facing surface, the stub contract for the neighbours, the ending kinds, the execution artifact that proves each, and the integrated check (the same module in the season loop);
2. **the batch sequence** that gets the subject to that test, by the handles of `unified/U3_DEPENDENCY_ORDER.md` §2.1, with what each batch contributes to the test and nothing else;
3. **the items the proposals do not carry**: the gaps of `unified/U4_TRACEABILITY.md` §6 that fall in these three subjects, the decidable missing parts of the INCOMPLETE proposals (`unified/U4_DOCUMENT_STATUS.md` §3.4), the holistic audit's findings that bear on them (`master/HOLISTIC_AUDIT*.md`; items `CI-01..CI-11` of `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md`), and the scenario, stub and reading work no proposal names.

**The item form** is the order's: `Item: <handle>` · subject advanced · INSTRUCTION · WHERE · FALSIFIER and control · GATE · hash movers · depends on (EXISTS-IN-TREE / PROPOSED / MISSING) · lane tag · batch it joins · cost class and model tier · what lands it. Handles are `IS-PC-nn`, `IS-MB-nn`, `IS-DICE-nn`. An item that only points at a proposal says **POINTER** and adds what is missing. An item whose missing part cannot be decided from the repository says **BLOCKED**, with the reason and its owner. Every claim about the tree cites the path and line opened at this read, or the probe run (§P2-5, the evidence log in part 2); a claim taken from a suite ledger and not re-opened is marked `[LEDGER: file]`; an inference is marked `[ASSUMPTION: … — basis]`.

**Words.** `unified/U1_GLOSSARY.md`; for the army and the field, `unified/MB_LEXICON.md` (A-95). A tree identifier that fails the ordinary-English test is given once in backticks and the plain word is used after (`STAGES.md`, "Terms mean what ordinary English says").

**What the three subjects are, in one sentence each.** PC is the fight between named persons (`modules/combat/`, reached through `engine/substrate/pc_engine.py` and `engine/season/seam/wrappers/combat.py`). MB is the field: two armies of unit rows resolved on cells (`modules/mass_battle/`, reached through `engine/season/seam/wrappers/mass_battle.py`). DICE is the one roll every contest draws (`engine/dice_engine/`), a substrate and not a module: its standalone test is read as *one roll played as a decision* (part 2, §P2-2.0), an answer taken by the five-step ladder at step 5 and reversible on Jordan's word. This lane lists nothing in `IS_FOR_JORDAN.md`: no item here overwrites canon, a `(RULED)` item or a ratified Layer 1 row.

**Words after A-98** (`unified/DECISIONS_ANSWERED.md:134`). *Attribute* (never aptitude or talent); *skill* for a learned rank and for the one capability kind; *skill score* for a person's number in a skill; *martial skill* for a person's skill at arms; *prowess* only for a unit's quality (A-59); *training* only for the act of learning; *derived score* for health, wound count, resolve and their kin; *choice score* for the chooser's valuation. Tree identifiers keep their names in backticks (`capability`, `faculties`, `scores`). Proposals quoted here may still carry the retired words until the sweep lane reaches them; this file does not.

**The readings this file rests on** (probes run at this read, `PYTHONHASHSEED=0`; full log in part 2, §P2-5):

| id | probe | reading |
|---|---|---|
| P-1 | `composition.require("combat.fight")` on a hand-built `PersonalCombatInput` (ends 4 and 4, default kit), seeds 0–199 | under `death` terms the first party wins 99, loses 99, undecided 2; `blood` 103 / 97 / 0; `yield` 98 / 101 / 1. A decider that withdraws at his first wound: 67 / 32 / 101. A decider that always answers `engage` equals no decider, cell for cell. So the module entry already runs alone, ends three ways, and a choice moves the ending |
| P-2 | `composition.require("mass_battle.resolve_field")` on a hand-built `MassBattleInput`, 40 against 40, seeds 0–99 | at the shipped `field_troops_per_weight` 1 (`engine/season/data/fixtures.py:789`): `Failure` 100 of 100, the attacker never wins. At 25: `Success` 37, `Failure` 63; 80 against 40: 50 / 49 and one `Partial`; 40 against 80: 21 / 79. The return has four keys (`attacker_size_pct`, `attacker_wins`, `defender_size_pct`, `degree`): no drawn end state, no report |
| P-3 | the same field at 25, one side given a `FieldOrder(role, retreat_at)`, 15 roles × 3 fall-back points × seeds 0–99 | the fall-back point changed the result in 1 of 1,500 role-and-seed cells; seven roles (`Anvil`, `Screen`, `Pursue`, `Feint`, `VolleyLine`, `Support`, `Reserve`) change nothing against no order at any seed; four (`Skirmish`, `Shock`, `Harass`, `Kite`) change every seed. Control: 33 distinct results over the 100 seeds with no order. One matchup, one size: a lead, not a balance claim (CLAUDE.md §0.1 pt 4) |
| P-4 | an `ast` scan of `tests/valoria/test_combat*.py` for a `for` loop all of whose assertions sit under a condition | four test functions (nine loop nodes); listed at IS-PC-04 |

---

## 1. Personal combat (PC) — the fight between named persons

### 1.0 The standalone-playable test

Jordan's intent is two modes on one code path (`AUDIT_BRIEF.md:300-319`): the duel, phase by phase; and the automatic duel round inside grid combat, where the player picks an approach and the engine runs the round. The test is therefore stated for both.

| element | today (opened at this read) | what makes it pass | carried by | the proof (execution artifact, expected reading) |
|---|---|---|---|---|
| **entry** | the registered entry `modules.combat.fight:fight(inp, rng, decide)` on a hand-built record (`modules/combat/fight.py:55`; P-1). No harness enters a module except by running a season (`proposals/01_CORE_one_scene_contract.md:34-37`); `engine/season/harness/` holds no `scene.py` and no duel file (`ls`, this read) | `python -m engine.season.harness.duel_scene --seed S --policy NAME` (the scenario, its own runner); `python -m engine.season.harness.scene combat.fight --fixture duel --seed S` (the generic scene entry); `python -m engine.season.harness.play_surface --seed S --person P --scenario duel` (the player's transcript) | **IS-PC-01** (the first); `01_CORE_one_scene_contract` edit 4 and `11_GO_player_surface_contract_B` §8 (B34; the other two) | each command exits 0 and prints a `Report` whose last line names an ending kind; same seed twice prints the same `content_hash` |
| **scenario** | none: *"No shipped fixture states two named persons, their kits, a cause and stakes"* (`audits/03_PC_audit.md:515`). B34's `duel` fixture is the headless world's first two persons, an `[ASSUMPTION]` (`01_CORE_one_scene_contract.md:115-117`), and those persons carry no attribute | a world of two named fighters and a witness, each fighter with authored attributes, a kit, a skill score in `arms`, a standing dispute, and one seat that can exercise `capture` | **IS-PC-01** | `test_duel_scene.py::test_the_two_fighters_differ_in_what_the_fight_reads` (their `(kit, skill score, end, attributes)` tuples differ) |
| **player-facing surface** | before: the offered verbs and a four-share odds reading (`seam/wrappers/combat.py:235`, `fight_estimate`). During: `engage` or `withdraw`, once a turn (`wrapper.TURN_CHOICES`, P-1). After: eighteen trace kinds; no client shows them on the loop's path (`audits/03_PC_audit.md:519`, `:523`) | before: `Offer` rows with odds; during: `CombatTurnView` and `APPROACHES` at each phase entry, the round's `trace` rendered between consults; after: the `account` | `11_GO_player_surface_contract_B` §2, §6 (row *duel, and a duel round on a grid*), §8 (B34); `03_PC_duel_round_and_approach_B` §3–§4 (B16) | GO-B gate 1 (the transcript's hash equals the plain run's at seeds 0–2); PB step 4's gate (equal plans, one hash) |
| **stub contract for the neighbours** | the typed input **is** the declared interface: `PersonalCombatInput` (`engine/season/queries/inputs.py:114-157`). The module reads no `World` (`fight.py:11-14`) | see the table below | **IS-PC-01** | `harness.scene combat.fight --fixture duel` with `apply=False` reaches `seam.contest` and nothing else writes |
| **ending kinds** | P-1: the entry returns `1`, `-1` or `0`. In the season a plain `fight` ends in a death 200 times in 200 (`audits/03_PC_audit.md:77`, H-263) and an untouched pair writes nothing (`verb_table.yaml:849-854`) | **win**: the foe is felled, yields, or is taken (`capture`). **lose**: the same against the player's person; his own death hands the line on (`play_surface.carry_on`). **draw**: both stand at the last round (`undecided`), or one withdraws. Every kind leaves a durable write (A-81) | B15 (`16_PESSIMIST_PC_A` the yield is a draw; `14_VERBS_PHYSICAL_A` A3 `mortal_terms`; `18_DETERMINISM_no_certain_matchup`); B14 (`03_PC_typed_outcome_one_door`: `prevailed`, `fell_to`, and the witnessed `undecided` Event, `:92`); B16 (`03_PC_exits_withdrawal_recovery` Part A, the priced withdrawal) | **IS-PC-01**'s `test_every_ending_kind_is_reached_and_each_writes` |
| **the world moves** | a fight writes `body`, `body_ceiling`, tenures closed, custody; the winner gains nothing and no witness's regard moves (`audits/03_PC_audit.md:27-30`) | the victor is recorded, the witness holds a claim of it, and the survivor's regard is readable by a later act | `16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight` and `03_PC_typed_outcome_one_door` (B14); the grudge is CHAR's (B10, `02_CHAR_scar_is_a_wound`) | the `Report`'s last block (what the world now holds) is non-empty for every ending kind |
| **mode 2, the grid** | no round to call: `fight` is one call of up to twelve engagements (`modules/combat/wrapper.py:555-625` `[LEDGER: audits/03_PC_audit.md:51]`) | one `combat.round` per attack action; the attacker gives one approach, which is the plan for every phase | `03_PC_duel_round_and_approach_B` steps 1–2, 4 (B16), step 5 (B30); `04_MB_squad_grid_of_named_characters` (B30) | **IS-PC-02**: the same round, called from the grid and from the duel, is identical |
| **integrated check** | seed 0, three seasons: 0 functions of `modules/combat` entered; seed 2: 155 in the first season `[LEDGER: master/HOLISTIC_AUDIT.md §3]` | the season reaches a fight from persons' own acts at every seed read | B01 (`03_PC_duel_chain_reach`), B15, B29, B37 (`22_HAPPENINGS_C`, A-16) | **IS-PC-03**: `aperture 2 s`, s = 0, 1, 2: the `ENGINES` block (CI-11) reads `combat.fight` above 0 at every seed |

**The stub contract** (what stands in for each neighbour when the fight is played alone; a stub is a plain value on the input record, never a second code path):

| neighbour | what the fight consumes from it in the loop | the stand-in in the scenario | what the stub may not do |
|---|---|---|---|
| DICE | `degree_from_net`, `roll_net_continuous`, `soft_cap` (`audits/03_PC_audit.md:577`) | **not stubbed**: the substrate is imported, as in the loop | — |
| CHAR | `Person.body`, `Person.attributes`, the skill score for the verb (`seam/wrappers/pool.py:78`), the decider for a person nobody plays | authored on the two fighters by the scenario's builder; the unplayed fighter's decider is `choose.approach_of` on his frozen `PersonInterior` (B16 step 4) | supply an approach by a rule in the scenario file (that is scripting drift; the falsifier of PB §9) |
| SE | each fighter's kit, read from rung stores (`queries/world_q.py:3484`, `kit_of`) | two store rows at the fighters' rung | hand a `Combatant` or a weapon record past `kit_of` |
| FA | the seat `capture` is exercised through; war stamps | one seat held by the first fighter; no war | grant custody without the seat's gate |
| SC | a `challenge` Record's `stakes`, which become the duel `terms` (`rosters.yaml:996`) | the dispute that lets `challenge` form (B01), and the Record the chain mints | set `terms` on the record by hand when the scenario is run with `apply=True` |
| MB, FI, WR, GO | nothing consumed | absent | — |

### 1.1 The batch sequence, and what each batch gives the test

Handles are `unified/U3_DEPENDENCY_ORDER.md` §2.1 and `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` §2. Only the contribution to the standalone test is stated; each batch's own gates are its proposals'.

| order | batch | what it gives personal combat | what the test can show after it |
|---|---|---|---|
| 1 | **B01-laneA** (IN) | the duel chain forms through the chooser (`03_PC_duel_chain_reach`) | the integrated check's first reading: `challenge` executed above 0 at seeds 0–2 |
| 2 | **B02-tests** (IN) | CI-11: the `ENGINES` block on `harness/aperture.py` | every later close can quote `combat.fight` entries |
| 3 | **B13-pc-package** (PC; CI-09) | `modules/combat` is a package; the path seam and its allow-list entry go | a scenario file imports no flat name; hash EQUAL |
| 4 | **B05-one-roll** (IN) | the fight's obstacle on the one opposed rule (`29_DICE` rows 2–4, 8; `U5b_PC_rulings_in_the_fight` §2–§3): the defender's skill score at one rate, attributes and wounds as named levels | two fighters of different skill scores no longer meet one obstacle |
| 5 | **B06-keyed-draw** (IN) | `Draw.u` and the A-30 key | a round is recomputable from its key (needed by B16 step 2) |
| 6 | **B14-pc-outcome** (PC) | the typed outcome and one door (`03_PC_typed_outcome_one_door`); weapon records in the export; what the world keeps of a fight | the workbench and the loop run one entry; the victor is recorded; an `undecided` fight still writes |
| 7 | **B15-pc-calibration** (PC) | fight length (A-31), the commit window, armour as a draw, `mortal_terms`, the riposte, the yield as a draw | **lose** is no longer always death; **draw** is reachable under every term |
| 8 | **B16-pc-round** (PC) | `fight.round`, the per-round key, the approach, a decider per party, the priced withdrawal; **IS-PC-01** as its last item | **PC plays alone, mode 1**: the scenario runs, choices move the ending, three ending kinds |
| 9 | **B18-pc-content** (PC) | per-person inputs as content, the secondary weapon, `unarmed` | the scenario's fighters can be given any kit a designer writes |
| 10 | **B29-pc-custody** (PC) | custody, capture, arrest (`14_VERBS_PHYSICAL_A` A1–A2) | the *taken* ending is formed by the chooser, not only by hand |
| 11 | **B30-mb-nested** (MB) | the nested entry at cap 1, PB step 5, the squad; **IS-PC-02** | **mode 2**: a grid attack is one round |
| 12 | **B34-go-surface** (GO) | `harness/scene.py`, the `--scenario` transcript, `Offer` and `account` | the duel is shown to a player as the player would see it |
| 13 | **B37-happenings** (IN) | a killing as a crime someone commits (A-16, A-96) | a fight arises without a duel |

**Where PC is playable alone:** at B16's close (mode 1, by the scenario's own runner) and at B30's (mode 2). B34 adds the player's transcript and is not a precondition for the scenario to run. **The cut:** IS-PC-01 joins B16 and not B34 because its edit set (`harness/duel_scene.py`, its test) meets no B34 file; only its one-line registration in `harness/scene.py::FIXTURES` waits for the batch that creates that file. Carrying the whole scenario to B34 would leave three PC batches (B16, B18, B29) with no scenario to read their work against.

### 1.2 Items

**Item: IS-PC-01 · the duel scenario: a world, a runner, a report**

- **Advances:** PC standalone, mode 1; the standing requirement's *scenario seed*, *end condition* and *instrument* (`audits/03_PC_audit.md` §9, ordered work 2 and 3).
- **INSTRUCTION** (in order; new file `engine/season/harness/duel_scene.py`, the sibling of MB's `field_scene.py` and SE's `valley.py`, so the three scenarios have one shape):
  1. `build(seed: int) -> World`. Two fighters and one witness at one settlement rung, placed by the same four writes the realm builder makes for a person (`harness/populated.py:515-518`; by CI-07's one placing function if `B03c-boot` has landed). Each fighter: authored `Person.attributes` on the registry keys of `modules/combat/attributes.py::SPEC`; a kit as store rows at his rung that `world_q.kit_of` reads; a skill score in `arms` on `Person.capability`; `body` at full. The two differ in at least kit and skill score. One seat held by the first fighter whose remit lets `capture` be exercised. One standing dispute between the fighters, in the form the `dispute` conjunct of B01 reads. No `Fixtures` override: the world runs at `DEFAULT_FIXTURES`.
  2. `POLICIES`: a closed mapping of name to decider over `CombatTurnView`: `auto` (no host: both fighters decided by `choose.approach_of`), `press` (the played fighter answers `aggressive` at every consult), `guard` (answers `defensive`, and `withdraw` at the top of the round after his first wound). A policy is a player-proxy; it reads the view and nothing else.
  3. `play(w, policy: str, seasons: int = 1) -> Report`. Runs `SeasonDriver.season` with `play_surface.dispatching_chooser` and `PlayHost(persons={first fighter}, deciders={"combat.fight": POLICIES[policy]})`; under `auto` no host. The played fighter's season acts come from the shipped chooser: the scenario authors no act.
  4. `Report` (a frozen dataclass, printed by `__str__`): per fight, the odds shown before it (`fight_estimate`), the verb and the `terms`, per round the approaches consulted and the wounding blows, the **ending per party** read from the Event's `ending` (`rosters.yaml: fight_endings`, `:986-994`: `felled`, `yielded`, `undecided` today; `prevailed` joins at B14) and, for an `undecided` fight, whether the trace carries a `withdraw` event and by whom (`03_PC_exits_withdrawal_recovery` Part A), and what the world now holds: each fighter's `body` and ceiling mark, tenures closed, custody, the claims the witness holds. `ending_kind(report) -> 'win' | 'lose' | 'draw' | 'none'` is derived from that, for the first fighter (`win`: he `prevailed`, or holds the other in custody; `lose`: he is `felled`, `yielded` or held; `draw`: both `undecided`); `none` means no fight formed in the seasons run, and the report then says which act was offered and not taken, so the run is never a dead end without a reason shown.
  5. `main()`: `--seed`, `--policy`, `--seasons`; prints the `Report` and the `content_hash`.
  6. Split part, lands in **B34**: `harness/scene.py::FIXTURES["duel"]` names `duel_scene.build` and its opening act, replacing the headless-world `[ASSUMPTION]` of `01_CORE_one_scene_contract.md:115-117`; `play_surface --scenario duel` resolves to the same builder.
- **WHERE:** `engine/season/harness/duel_scene.py` (new); `engine/season/tests/test_duel_scene.py` (new); in B34 one line each in `engine/season/harness/scene.py` and `engine/season/harness/play_surface.py`.
- **FALSIFIER and control:** a policy that cannot change the ending at any seed (then the approach is cosmetic and PB step 3's gate has failed upstream); an ending kind that leaves the world unchanged; a scenario whose fight differs from the season's for the same act, world and seed. Control: a decider that returns what `approach_of` returns gives the `auto` run's `content_hash` (REM-31's control, `engine/season/tests/test_rem31_grid_suspension.py`).
- **GATE:** `engine/season/tests/test_duel_scene.py`, written first and read red: `test_the_two_fighters_differ_in_what_the_fight_reads`; `test_an_echo_policy_equals_the_automated_hash`; `test_press_and_guard_end_differently_at_some_seed` (seeds 0–39, `assert checked >= 40`); `test_every_ending_kind_is_reached_and_each_writes` (seeds 0–199 under `auto`: `win`, `lose` and `draw` each occur, and for each kind the fight's Events carry a write other than the budget debit; `assert` on the count of fights read); `test_same_seed_twice_is_one_hash`. Expected reading of `python -m engine.season.harness.duel_scene --seed 0 --policy guard`: a report ending in one of the three kinds. `[ASSUMPTION: all three kinds occur within 200 seeds at season scale — basis: P-1 at module scale (2 undecided in 200 under death terms) and B15's yield draw; if `draw` does not occur the test names the seed count it needed and the item stops there]`
- **Hash movers:** none. A new world and a harness file; no realm pin reads it.
- **Depends on:** B16 steps 1–4 (PROPOSED); B14's `fight_endings` member `prevailed` (PROPOSED); B15's yield draw (PROPOSED); B01's dispute reading (PROPOSED, lane A's branch); `play_surface.dispatching_chooser`, `PlayHost`, `fight_estimate`, `kit_of` (EXISTS-IN-TREE); `harness/scene.py` for step 6 (PROPOSED, B34).
- **Lane:** PC. **Joins:** B16-pc-round, as its last item; step 6 in B34. **Cost class and tier:** small build; `sonnet`, `high`. **Lands it:** B16's `valoria-author` producer, one `Item: IS-PC-01` commit, `[skip ci]`.

**Item: IS-PC-02 · a grid attack is the same round**

- **Advances:** PC standalone, mode 2; one code path. PB §9 names the falsifier (*"a grid attack whose outcome differs from the same round inside a duel at the same plan, state and seed"*) and no proposal names its test.
- **INSTRUCTION:** in `engine/season/tests/test_squad_field.py` (created by `04_MB_squad_grid_of_named_characters`, B30) add `test_a_grid_attack_is_the_duel_round_at_the_same_key`: build one `DuelRoundInput` (two fighters from `duel_scene.build(0)`, round 1, a plan of `aggressive` for the attacker); call `fight.round` directly with the key `(fight_key, 1)`; run the squad host on a two-person field in which the same two persons are paired with the same plan and the same key; assert the two `DuelRoundOutcome`s are equal field by field and the draw counts are equal. Control: the plan changed to `defensive` on one side only makes them differ at some seed in 0–19 (`assert checked >= 20`).
- **WHERE:** `engine/season/tests/test_squad_field.py`.
- **FALSIFIER and control:** as stated; a squad host that applies the approach as a modifier on a result fails it (PB §6, first risk row).
- **GATE:** the test green; the control red when the squad's pairing passes a different key.
- **Hash movers:** none. **Depends on:** `03_PC_duel_round_and_approach_B` steps 1–2, 5; `U5b_PC_rulings_in_the_fight` §1 (`nested_entry`); `04_MB_squad_grid_of_named_characters` (all PROPOSED); IS-PC-01.
- **Lane:** MB (the batch's lane), PC review. **Joins:** B30-mb-nested, after the squad file. **Cost and tier:** edit; `sonnet`. **Lands it:** B30's producer.

**Item: IS-PC-03 · the integrated reading, quoted at four closes**

- **Advances:** the integrated half of the test; H-01 (`master/HOLISTIC_AUDIT_part2.md:10-37`).
- **INSTRUCTION:** at the close of B01, B15, B16 and B37, the batch's last commit body quotes `python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2: the `ENGINES` line for `combat.fight`; `attempted` and `executed` for `fight`, `challenge`, `accept`, `capture`; and the count of fights by ending kind. Each reading names its SHA and is taken once (`reading @<sha>`, `methodology-execute` CHECKPOINTS AND BASELINES). No count goes into `CURRENT.md` or a handoff (CLAUDE.md §1).
- **WHERE:** no file; the four close commits.
- **FALSIFIER and control:** `combat.fight` reads 0 at any of the three seeds after B01. Control: the reading before B01 at seed 0 is 0 (`master/HOLISTIC_AUDIT.md` §3).
- **GATE:** expected after B01: `challenge` executed above 0 at each seed (lane A measured 26, 19, 24 `[LEDGER: unified/U4_TRACEABILITY.md §4.2a]`) and `combat.fight` above 0 at each; after B15: the ending kinds are not all `fell`; after B37: at least one fight whose opening act is not `challenge` or `accept`.
- **Hash movers:** none. **Depends on:** CI-11 (PROPOSED, B02). **Lane:** PC (B15, B16), IN (B01, B37). **Joins:** those four batches' closes. **Cost and tier:** a reading; `haiku` (`valoria-measure`) runs it, the orchestrator reads it. **Lands it:** each batch's BATCH-CLOSE.

**Item: IS-PC-04 · the conditional test loops, named** (`U5b_PC_residue` §10, `U4_DOCUMENT_STATUS.md` §3.4 code SITE)

- **Advances:** test strength in the PC lane (CLAUDE.md §0.1 pt 2). The proposal says ten loops and names none; the tests lane's scan is not in the tree.
- **INSTRUCTION:** the criterion, stated: a `for` loop inside a `test_*` function in which every `assert` sits under an `if`, a `try` or a `match`. P-4 applied it to `tests/valoria/test_combat*.py` and finds four functions: `test_combat_duel_terms.py::test_yield_and_blood_are_different_stops` (loops at `:234-235`, no counter in the function); `test_combat_invariants.py::test_rear_clearance_monotone_non_decreasing` (`:1154`, over `C.WEAPONS.items()`); `test_combat_invariants.py::test_reach_class_beats_arming_not_inverted` (`:1314`); `test_combat_strength_jobs.py::test_an_armoured_weak_fighter_tires_faster_than_an_unarmoured_one` (`:222`). The last three already name a counter-like variable and are opened first to see whether it is asserted. For each function that does not assert its count, add a counter and `assert checked >= N` with `N` read from the roster the loop covers, as the proposal's step 2 orders. `[ASSUMPTION: these four are the set to edit; the proposal's count of ten came from a scan with a criterion this lane cannot see — basis: P-4; the landing session re-runs the scan over the files it touches and edits what it finds, without widening to other lanes' tests]`
- **WHERE:** the three test files named.
- **FALSIFIER and control:** with the loop's roster emptied in process, each edited test fails on its counter (the proposal's gate).
- **GATE:** the three files green; the emptied-roster run red.
- **Hash movers:** none. **Depends on:** nothing. **Lane:** PC. **Joins:** B14-pc-outcome (where `U5b_PC_residue` lands). **Cost and tier:** edit; `sonnet`. **Lands it:** B14's producer.

**Pointers: decided elsewhere in the suite, nothing added** (each closes an INCOMPLETE row of `U4_DOCUMENT_STATUS.md` §3.4 by naming where its missing part already is)

| handle | the row's missing part | where it is decided | batch |
|---|---|---|---|
| IS-PC-P1 | `03_PC_duel_round_and_approach_B` step 5, MB's side: what a contact is and what its result does to a unit | `04_MB_manager_battle_one_resolver` §7: two officers' units in contact at a window are a duel contact, one round a window, states in the module's loop frame; an officer felled or yielded lowers **his unit's** morale by `cascade_morale_hit` scaled by that unit's discipline. Its test is named: `tests/valoria/test_mass_battle_officers.py::test_officer_duel_moves_only_his_units_morale` | B30 |
| IS-PC-P2 | `03_PC_loadout_and_carry` items 4 and 6 (design-first in MB) | `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4 | B31 |
| IS-PC-P3 | an untouched pair's fight writes nothing (A-81) | `03_PC_typed_outcome_one_door.md:92`: the `undecided` Event is witnessed and deposited | B14 |
| IS-PC-P4 | a fighter with no weapon cannot be built (H-265) | `03_PC_person_inputs_content` Parts B–D (`unarmed`) | B18 |
| IS-PC-P5 | the flat module set behind a path insert (H-08) | CI-09 | B13-pc-package |

**Blocked items** (the missing part is not decidable from the repository)

| handle | what is missing | why it cannot be decided here | owner | what the suite assumes meanwhile |
|---|---|---|---|---|
| IS-PC-B1 | PB step 3d, the lean in the `measure` phase | it may ship *"only together with both of its costs"* (PB §7), and neither cost exists in the engine: pressing must raise stop-hit exposure, a missed stop-hit must cost the longer weapon | PC lane, design-first, after B16 | the menu ships with the `exchange` and `bind` leans; the `measure` phase is consulted and answers `normal`. The standalone test does not need it |
| IS-PC-B2 | the shipped `YIELD_OB` values (`16_PESSIMIST_PC_A` gate 4) | the proposal makes the pick Jordan's from a sweep table that exists only after B15's calibration runs | Jordan, at B15's calibration reading | B15 lands the draw with the value the sweep's bound admits (a first-blood duel ends at first blood more than nine times in ten) and marks it `[ASSUMPTION]` in `CFG`; IS-PC-01's ending test reads kinds, not shares, so it holds for any admitted value |

