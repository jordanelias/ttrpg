# U5b · PC — residue: the personal-combat items no proposal carried

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Author: U5b closure lane (Fable), 2026-11-12. Read at `6910680`. Each section is one finding or resolution
of `audits/03_PC_audit.md`, `03_PC_audit_addendum_B.md` or `16_PESSIMIST_PC.md` that was decided in its
audit and written into no proposal ("an edit", "recorded for the PC lane"), or an item another closure
handed to this family. Reference only (CLAUDE.md §0.05). Sections are independent unless a dependency is
named; each is commit-sized.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.1 (§4 edit 2 VIOLATES `hol` §53 / `04` §C.12 rejection 5: the new `raise ValueError` is replaced by a signature with no default stream, so a missing stream fails at the call site, not by a runtime raise in a path the port reaches), §1.1 and §2 row A-30 (§7's "position after the mortal-wound draw" is a counter: the mark draw takes its own key; §8's private stream is keyed), `U1_OWNERS_AND_VOCABULARY.md` §4 R-27 (§1 names the one calibration that sizes the in-fight wound σ and the season's `wound_step` together), `U1_GLOSSARY.md` *skill* (§1 item 4: the slot family is `axis`), 7b's "`[grep at landing]` sites by grep now" (§2, §4 and §6 resolved at the tree; §6's importer count corrected from three to five), test 9 (`Depends on:` / `Lands in batch:` per section from `U3_DEPENDENCY_ORDER.md`). §10 stays INCOMPLETE (reason at the section). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*).

**Depends on:** §7 on `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 for item 3's reading only (the keyed draw removes the order dependency); §8 on `10_DICE_believed_odds_have_a_prior.md` Edits A–B (B05); §1's fit and §3's census on the combat calibration batch (B15); all keyed draws on `11_GO_one_draw_owner.md` (B06).
**Lands in batch:** §2, §4–§10 in B14 (`B14-pc-outcome`, PC; U3 places §7–§8 there); §1 items 1–2 in B14 and the fit (item 3) with B15; §3 in B18 (`B18-pc-content`, before `03_PC_person_inputs_content.md` Part B).

## What it changes in `engine/season/` at runtime

§4 edit 1 refuses a fight between a person and himself at the seam (no shipped act reaches it). §7 moves
every fight that leaves a survivor at his wound limit, behind a fixture whose control is today. §8 lets
the chooser price a fight by believed odds, behind the shipped `odds_weighting`. Everything else moves no
season.

## §1 · A slope bound on a lever, and the read's literal scale (pessimist R-7; F-PES-PC-08; R-PC-43)

Measured: Perception 4 against 3 is 77 to 23, 5 against 3 is 94 to 6 and equals four points of trained
score; Strength 1 is felled 96.6%; the six skill axes are uncapped (+1 on all six, 18.1% felled)
(`audits/16_PESSIMIST_PC.md` §2.4; addendum E-B5). Which term carries the Perception slope was not
isolated (`[UNVERIFIED]` there).

1. **Isolate first** (a workbench reading, no edit): ablate in turn the read's logistic
   (`modules/combat/combat_systems.py:1145`, `core.logistic((read_d-read_a)/1.0)`), `mode_sigma`'s read
   term, `init_emphasis_sigma` and `tempo_pressure`, at Perception 5 against 3, n 1,000, with the
   disjoint-seed control; record which moves the 94.2%.
2. `modules/combat/config.py`: the literal `1.0` of the read's logistic becomes `CFG['READ_SCALE']`
   (value 1.0, byte-identical), so the exporter carries it and a sweep can fit it.
3. The calibration rule gains one line, at its owner (`combat_balancing_methodology.md` is quarantined
   reference; the executable owner is `workbench/build_levers.py`'s lever table): **one point of any
   attribute or skill axis moves the season-default mirror no more than one point of trained score does**
   (about fifteen points near parity, `pD_skill.py`). A lever outside the bound is reported by the table,
   not gated.
4. Combat axes are bounded where they are authored: the `axis` slot family (was `skill`; U1 glossary) of
   `03_PC_person_inputs_content.md` Part A takes its bounds from the capability row (U1 §2 `scale`), and
   `technique` and `grab` are not members of the family until a sweep shows them outside the interval.
5. *(W3-1, U1 §4 R-27:)* one quantity, two sites, one calibration: the in-fight wound σ
   (`CFG['WOUND_ATK_OB']`, `CFG['WOUND_DEF_OB']`, read by `combat_systems.wound_impairment`) stays the
   module's own rule, and the season's carried-wound level (`Fixtures.wound_step`, `U5b_PC_rulings_in_the_fight.md`
   §3) reads none of them; both are sized in the one combat calibration batch (B15,
   `U5b_PC_rulings_in_the_fight.md` §5 row 5), and the batch's commit states the two values side by side.

**Gate.** `build_levers.py` prints the attribute and skill ladders with the bound beside each; `READ_SCALE`
at 1.0 is byte-identical (`tools/ci_golden_modes_check.py` is mass battle's; here the combat goldens and
`export_engine_params.py --check`). **Falsifier.** A fitted `READ_SCALE` under which Perception 5 against 3
still exceeds four points of score. **Movers.** None until a value is changed; the fit rides the
calibration batch (`U5b_PC_rulings_in_the_fight.md` §5 row 5). **Lands:** PC lane.

## §2 · The grapple's outcome names (pessimist R-8; F-PES-PC-10)

`modules/combat/contact.py:53`: `GRAB_OUTCOMES = ('disarm', 'throw', 'pin', 'control', 'foot_pin',
'escape')`; each writes poise or initiative only (`wrapper.py:460-468`; 1,107 "disarms" in 5,000 fights
disarm nobody).

1. `contact.py`: the note above `GRAB_OUTCOMES` states what each outcome does (a poise or an initiative
   shift) and that none removes a weapon, moves a fighter to the ground or holds him.
2. The names are trace vocabulary and are **not shown to a player**: the workbench's `narrate.py` and
   `commentary.py` render them by effect ("his balance is taken"). *(W3-1, grepped at the tree:)* neither
   file renders a `GRAB_OUTCOMES` member today (`grep -n "disarm\|foot_pin\|GRAB_OUTCOMES"` over both prints
   nothing), so there is no edit now; the rule binds the first rendering added.
3. The port does not carry the contact axis until one outcome has an effect a fold or a grid reads: one
   line in `11_GO_port_gate_order_and_coverage.md`'s coverage list (U5d's file; named for that lane).

**Gate.** A narrated trace of a fight with a `disarm` event contains no sentence saying a weapon was lost.
**Falsifier.** A player-facing string built from a `GRAB_OUTCOMES` member. **Movers.** None.

## §3 · A census before an inventory (pessimist R-9; F-PES-PC-12; R-PC-12)

A spear against an arming sword in light armour fells him 99.2 to 99.8% in 1.1 turns; heavy armour
against a sword is 0 of 2,800. `rosters.yaml: arms_kinds` is empty, so neither reaches a season today.

1. One workbench instrument, `workbench/balance.py::census(n)`: every startable weapon against every
   other at each armour tier, tracker-true (never `fight`'s integer), printing each cell beyond 95% with
   its disjoint-seed control. It is run **after** the calibration batch (the scale, the bare zone and the
   riposte each move the cells).
2. `03_PC_person_inputs_content.md` Part B admits a kind to `arms_kinds` only with its census row named
   in the commit body: either no cell beyond 95% against the kinds already admitted, or the answering
   kind admitted with it (the estoc with plate).

**Gate.** The census table in the landing commit of Part B; each admitted kind's worst cell quoted.
**Falsifier.** A season fight between two admitted kits whose census cell reads beyond 95% and was not
named. **Movers.** None (an instrument). This is a reading the content lands behind, not a guard: it has
no CI row.

## §4 · Two refusals at the seam (pessimist R-10; U5a C5)

1. `engine/season/seam/wrappers/combat.py::resolve`: take `fight_estimate`'s `PARTY-GAP` line (`:257`,
   `actor == target`) so one id as both claimants is refused before the engine is called. Today it
   resolves and names a winner (`pS_season.py` S3).
2. *(Reconciled, W3-1, `R1_READ.md` §1.1: the first text made this a `raise ValueError`, a new raise in a
   path the port reaches, `hol` §53, `04` §C.12 rejection 5.)* `modules/combat/wrapper.py:555`:
   `def fight(A, B, cfg=None, rng=None, …)` becomes `def fight(A, B, cfg, rng, …)` (no default for either;
   `cfg=None` still means `CFG` inside), and the fallback `rng=rng or random.Random()` at `:565` is deleted, so
   a missing stream is a signature error at the call site, not a branch. Callers (grepped at the tree): every
   `wrapper.fight` call already passes a stream; the three that omit `cfg` gain `cfg=None` explicitly:
   `modules/combat/fight.py:111`, `tests/valoria/test_combat_ob_from_defender_consumers.py:96`,
   `engine/season/tests/test_combat_module.py:54`.

**Gate.** A hand-built self-fight returns `PARTY-GAP`; `git grep -n "random.Random()" modules/combat`
prints nothing; `inspect.signature(wrapper.fight).parameters['rng'].default is inspect._empty`.
**Falsifier.** A combat test that passes with no stream supplied. **Movers.** None. **Tests:**
`engine/season/tests/test_combat_module.py::test_a_self_fight_is_refused_party_gap`,
`::test_wrapper_fight_has_no_default_stream`.

## §5 · Six stale texts (R-PC-39; F-PC-22)

Each corrected at its site, when its file is next touched or in one commit:

| site | edit |
|---|---|
| `systems/combat/combat_engine_v1/workbench/build_levers.py:158-161` | the armour docstring: `act_cost` charges the wearer when Strength is short of the tier's demand (`combat_systems.py:168-174`) |
| `systems/combat/combat_engine_v1/state_graph.py:33-39` | `beat_exhaustion`'s note: "not observed in 1,728 fights (addendum E-B15) nor in 11,000 (`16_PESSIMIST_PC.md` §1.3)"; the "MEASURED, do not re-litigate" sentence deleted |
| `state_graph.py`, the `site:` values | line numbers dropped, as the injection table already did |
| `workbench/probabilities.py:55` | the citation of `wrapper.py:173-198` re-pointed to the function name |
| `modules/combat/weapon_physics.py:3` | `combatant.WEAPONS` → `weapons.WEAPONS` |
| `.designs/…/combat_flow_skeleton_v1.md` S2.7.19 | not edited: quarantined reference (CLAUDE.md §1); the deleted `disrupt_resist_p` branch is recorded here only |

**Gate.** `python systems/combat/combat_engine_v1/state_graph.py` still prints PASS. **Movers.** None.

## §6 · The tempo flat-top gets a position; the workbench's `trace.py` (R-PC-21; F-PC-11)

1. `workplans/valoria_master_workplan_v11_part5.md`, the PC-08 Phase-C row: one clause naming
   `combat_systems.py:107-113`'s `KNOWN BROKEN-LOGIC` note (38 of 53 weapons at one tempo penalty) as an
   item of that recalibration. A plan edit; no code. With A-31's batch landing first, PC-08's row is read
   after it.
2. `systems/combat/combat_engine_v1/workbench/trace.py` shadows the standard library's `trace` once its
   directory is on `sys.path`. It is renamed `fight_trace.py` with its importers, **five** at the tree
   (W3-1 grep, corrected from three): `workbench/commentary.py:205`, `workbench/server.py:26`,
   `workbench/narrate.py:109`, `systems/combat/combat_engine_v1/state_graph.py:195`,
   `tests/valoria/test_combat_tradition_levers.py:138`; or left and the shadow recorded in the workbench README if `03_PC_typed_outcome_one_door.md`
   Part B (which rewrites this file's entry) lands first and removes the path insert. The path inserts in
   `modules/combat/` themselves are the declared shrink-only seam (`engine/substrate/pc_engine.py`) and
   get no edit.

**Gate.** `python -c "import trace; print(trace.__file__)"` from the workbench directory prints the
standard library's path. **Movers.** None.

## §7 · The lasting mark is a draw (`audits/25_GROUNDING_ENGINE.md` G-22; `16_PESSIMIST_PC.md` §5)

`engine/season/loop/effects_combat.py:414-424` (`_marks`): every survivor whose tracker reads `wounds >=
max_wounds` has his `body_ceiling` lowered, with certainty, shipped live (`body_mark_model="deepest_gate"`,
`data/fixtures.py:723`). The standing rule asks a draw for a thing that could go either way; a man cut to
his limit who mends clean is such a thing.

1. `rosters.yaml: body_mark_models` gains `drawn`; `data/fixtures.py`: the swept set becomes `none`
   (control) / `deepest_gate` (today) / `drawn`; the shipped value stays `deepest_gate` until the gate is
   read.
2. `_marks` under `drawn`: for each survivor at his limit, one roll keyed `H(seed, tick, victim,
   "fight.mark")` (A-30: its own key, never a position in the scene's stream after the mortal-wound draw
   of `14_VERBS_PHYSICAL_A` A3): pool his body band, obstacle the fixture `mark_ob`, on the one sampler.
   Failure: the ceiling falls two bands'
   worth (`marked_ceiling` applied twice); Partial: it falls as today; Success and better: no mark. One
   Observation `marked` on the Event.
3. A3's Partial band ("left for dead, the lasting mark follows") keeps its certainty: that mark is the
   result of the mortal-wound draw, not a second draw.

**Gate.** 200 seeded fights that leave a survivor at his limit: the three outcomes each occur; control
(`deepest_gate`) reproduces the pre-change hash. **Falsifier.** Under `drawn`, a mark on every such
survivor. **Movers.** At the flip: every fight with a survivor at his limit. **Lands:** B14 with the
fixture shipped at `deepest_gate` (U3); the flip is read with the calibration batch, after A3 (B15).
**Tests:** `engine/season/tests/test_combat_module.py::test_drawn_marks_yield_all_three_outcomes_over_200_seeds`
(`assert checked >= 200`), `::test_deepest_gate_reproduces_the_pre_change_hash`.

## §8 · A fight can be priced by believed odds (addendum C-9; U5a F-DICE-14 Edit C)

`engine/season/seam/wrappers/sigma.py::believed_chance` (`:420`) answers `None` for a band of another
module, so `choose.odds_weight` never prices a `fight`, `accept` or `capture`.

1. `believed_chance`: for a row whose prize binds the `personal_combat` provider, the answer is the
   `estimate` provider's (`seam/wrappers/combat.py:235-296`, `fight_estimate`: the resolver sampled on a
   private stream keyed `H(seed, tick, believer, "estimate.fight")` (A-30), moving no hash), read over the
   bands asked, **on the believer's own picture of the
   opponent** (his kit and wounds as the believer's ledger gives them; the world's where he has seen
   them). A person who knows nothing of the opponent's kit gets the default kit, not the true one.
2. No closed form and no table: an estimate is the resolver sampled (Layer 1 §27.2; A-1).
3. `fight_estimate`'s sample count for this caller is a fixture (`believed_fight_samples`, seed 60: a
   belief is not a measurement), separate from the display's 400.

**Gate.** With `odds_weighting: believed`: a person at `body` 400 forms `fight` on an unhurt opponent less
often than the same person unhurt, over seeds 0 to 29 (today nothing reads his body, `16_PESSIMIST_PC.md`
§2.5); the estimate's stream leaves `content_hash` unchanged when the act is not chosen. **Falsifier.** An
estimate that reads a kit the believer has no claim about. **Movers.** Every world in which a violent
Candidate is scored. **Depends on** `10_DICE_believed_odds_have_a_prior.md` Edits A–B (U5a's).

## §9 · Register rows this family owns (pointer edits; `engine/season/hole_register.yaml`)

| row | edit |
|---|---|
| H-64 | closed: `fight` is a table row (`verb_table.yaml:733`); the stale symbol in its text stays marked |
| H-264 | re-pointed: the duel is no longer the only door; `03_PC_duel_chain_reach.md` and A-16's carrier are named as its closers; it closes when `aperture` shows a fight from a person's own act |
| H-349 | re-measured by `16_PESSIMIST_PC.md` §2.3 (light armour 1.5 points; plate a certainty); pointed at `16_PESSIMIST_PC_D` |
| H-97 | pointed at `U5b_PC_rulings_in_the_fight.md` §3 |
| H-258 | grade corrected from "closed as an assumption" to "a certainty at the gate (G-22)"; pointed at §7 |

**Gate.** `python -m engine.season.harness.register --requirements` still loads. **Movers.** None.

## §10 · Test strength handed across by U5a (`audits/01_CORE_audit_addendum_C_tests.md:263`)

*"valoria · PC: ten all-conditional loops over weapon rosters `[not adjudicated: PC]`"*. A loop whose
assertions all sit under a condition can pass by asserting nothing (CLAUDE.md §0.1 pt 2).

1. The ten are located by the tests lane's scan (`scan_tests.py`, in that lane's scratchpad; re-run at
   landing, since this lane did not open the test files `[UNVERIFIED: which ten]`).
2. Each gains a counter and `assert checked >= N`, `N` the roster count the loop is meant to cover (50
   startable weapons, 4 forms, per `probe_weapons.txt`), read from the roster and not typed.
3. No new test file and no CI row: an edit inside the existing tests, landed with the next change that
   touches each file (the one file covering the edit, CLAUDE.md §0.4).

**Gate.** With the roster emptied in process, each of the ten fails on its counter. **Movers.** None.

**INCOMPLETE (W3-1, test 9):** the ten loops are not named. The tests lane's `scan_tests.py` is not in the
repository and this lane did not re-derive the list; blocking reason: identifying an all-conditional loop
needs each candidate file in `tests/valoria/` read (the scan's own job). Completing step: the landing
session writes the scan as a one-time reading (output in the commit body, no CI row) and names the ten
here before editing them.

## Lands and tier (all sections, W3-1)

An IN-lane implementation session under `/methodology-execute` with PC review; edits (§2, §4, §5, §6, §9,
§10) `sonnet`; §1's isolation and §3's census run by `haiku` (`valoria-measure`) and read by `opus`; §7, §8
`sonnet`.

## NERS reading (E last)

N: each item is a decided resolution that would otherwise live only in an audit's table. R: two
certainties (the mark, the unpriced fight) become draws and readings. S: the estimate is the resolver
sampled, as everywhere. E: ten small edits, one instrument, two fixtures; no new owner.

## Cost class

Edits (§2, §4, §5, §6, §9, §10); small builds (§1's fit, §3's instrument, §7, §8).
