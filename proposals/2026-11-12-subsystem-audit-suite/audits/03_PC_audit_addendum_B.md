# PC — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 2c24c81 (working tree)

Addendum to `audits/03_PC_audit.md` (read at `601e715`; not edited here). It reads what that audit
reported unread, corrects it where the reading or a run shows it wrong, continues its numbering
(findings from `F-PC-15`, resolutions from `R-PC-27`), judges Jordan's personal-combat intent of
2026-11-12 against the whole design set, and carries a decision-ready design for the per-phase
approach and the automatic duel round. Section numbers are prefixed `B`. The orchestrator committed
suite files while this was read (HEAD was `4832a6c` at the last check); `git diff --stat 2c24c81 HEAD`
over `modules/`, `engine/`, `systems/`, `tools/`, `references/` and `architecture/` is empty, so every
code reading below holds at both. All figures: `PYTHONHASHSEED=0`; scripts and outputs are in the
scratchpad named in §B11.

## B0. Verdict of the addendum

**The first audit's verdict stands, and its proposal 5 is right in shape and wrong in four particulars
a builder would trip on: what a "phase" is, which hook makes aggression dominant, what a round must
carry and where that state may live, and how an NPC chooses.** The engine was written from the start
to be called one engagement per turn (`modules/combat/wrapper.py:576`; the design set recorded the
missing caller as a traced gap), so the round is not a new idea but an unexposed one. The approach is
different: the design set has asked for it four times under four names (the pool split, the C4
stances, the six-intent Plan layer, and now aggressive / normal / defensive) and the engine has never
carried it. The one axis that resembles it is not a trade, and the reason is a single unpriced hook
(F-PC-17). The superseding design is `proposals/03_PC_duel_round_and_approach_B.md`.

## B1. What was read

| what | how |
|---|---|
| `modules/combat/weapon_physics.py` (972 lines), `wrapper.py`, `combatant.py`, `fight.py` | in full |
| `modules/combat/weapons.py` (934) | the schema header, the first four records, every record head and top-level comment, the edges table and the bake loop by eye; all 54 records by a field scan (`probe_weapons.py`) |
| `modules/combat/combat_systems.py` | the disposition, commit, read, counter, exposure, σ-assembly, half-sword, stamina, handling and closing functions (`:160-200`, `:860-900`, `:1040-1215`, `:1375-1395`); the rest by its function list |
| `modules/combat/config.py` | `:270-342` |
| `engine/season/decision/choose.py` (800), `options.py` (1,827) | in full |
| `systems/combat/`: `__init__.py`, `capabilities.py`, `state_graph.py`, workbench `trace.py`, `presets.py`, `narrate.py`, `probabilities.py`, `server.py`, `commentary.py`, `balance.py`, `build_levers.py`, `structure_scan.py`, `armour_participation.py` | in full |
| workbench `catalogue.py`, `calibrate_generics.py` | head, structure and the quantity registries; `static/index.html` by its controls; `data/combat_armour_reference.json` by its header and through `--drift` |
| `.designs/systems/combat/reference/`: `combat_reference_v1.md`, `combat_flow_skeleton_v1.md`, `combat_c4_draft_v0.md`, `combat_currency_v1.md`, `scene_combat_design_v1.md` | in full |
| `.designs/systems/combat/combat_engine_v1/reference/`: `README.md`, `combat_throughlines_v1.md`, `engagement_psychology_recovered.md`, `REARCHITECTURE_v1.md`, `combat_balancing_methodology.md`, `tradition_decomposition_v1.md`, `ability_armature.md` | in full |
| `…/phase4_5_plan_v1.md` (52 KB) | its status head, Context, Phase 5 and Phase 4 (4a to 4c) in full; Workstream 0 and Phase 3 by heading |
| `.designs/systems/_architecture/reference/videogame_mode_spec.md` | in full |
| `.audit/`: fiat audit, combinatorial findings, wiring audit | in full |
| `.audit/` four-dimension index; stress-test findings (TL;DR, B.2, B.3) and its ratified-unimplemented register (PC rows); balance-state and defect register (headings and finding tables) | in part |
| `.audit/` four-dimension infill; balance-state plans, value catalogue and emit-key map; weapon-morphology set; the two July scene-combat working-paper joins and their JSON lenses | **not read** beyond a head each |
| `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` (77 KB, HELD) | §1 to §3, §6 to §13, §15 to §21 |
| `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md`, `proposals/weapon_physics_and_concentration_model.md` | in full |
| `proposals/pc_formation_system.md` | §0 to §3.5 |
| `proposals/2026-10-07-grid-mode-suspension.md` | §1 to §4 (a) |
| Layer 1: `architecture/holonic_ARCHITECTURE.md` §27.2, §39.2 to §39.4, §44.2 to §44.3; `architecture/meta/04_CODE_ARCHITECTURE.md` `:116-122`, `:757-811`; `architecture/meta/03_VERBS_AND_LOOPS.md` §C.4 | at the cited lines |
| research: `research/by_lane/PC_personal_combat.md` (headings and the tactics, stance and auto-resolve rows), `game_precedent_suite/tutorials/T19` (Unicorn Overlord), `tables/R4` (Kingdom Come), `THROUGHLINES.md` (P17, P36) | in part |
| `audits/02_CHAR_audit.md` §0A and §10's mass-battle note; `02_CHAR_choice_alignment.md`, `02_CHAR_resolve_and_temper.md`; `03_PC_loadout_and_carry.md`; the MB audit's loadout finding and addendum head | in full for the sections named |
| tests | none opened; the tests lane covers them |

## B2. Corrections to the first audit, and new findings

### B2.1 Corrections

| # | the first audit says | what the reading or a run shows |
|---|---|---|
| C-1 | F-PC-13 lists "no off-hand or shield slot" as a gap against the intent; §5 lists the off-hand slot as design that is only prose | The off-hand was decided out of scope and its one hook deleted: ED-PC-0055's closing row (2026-10-08, J-20 option B) made `core.COVERAGE_GAP` a scalar and removed the `coverage` parameter (`modules/combat/core.py:217-220`). The held proposal's §13 ("the shield's hook already exists") is false at this SHA. The stated intent names weapon, armour and skills. Not a gap; a closed scope call (R-PC-35) |
| C-2 | F-PC-13 and P5: the played and automatic fights should agree "in expectation" (the ruled duality doctrine) and step 4's gate is a fidelity reading | The text with authority is Layer 1: "They agree exactly, because they are the same slice" (`03_VERBS_AND_LOOPS.md:146-153`), ratified 2026-09-05, after the quarantined duality note. Equal choices must give the identical outcome; a difference in expectation belongs to a difference in choices (R-PC-32) |
| C-3 | F-PC-05 and F-PC-14 call the free withdrawal a breach of that doctrine | The finding holds on better ground: a played person holds a choice an NPC lacks (I-1, one kind of agent) and the choice is unpriced. No expectation test is needed to see it |
| C-4 | P5 §6 conflict 2: R-04 reads the grid as mass battle's cell field, the intent describes a tactics grid, "two different builds" | Layer 1 names it one build: "grid squad combat: the same thing one scale down … every combatant a `Person`" (`04_CODE_ARCHITECTURE.md:811`); `05_two_modes_of_one_bout.md` M-6 recommends the cell field at weight 1 as the grid. Not a conflict (R-PC-33) |
| C-5 | P5 §6 conflict 5 cites `videogame_mode_spec.md` only for "No grid. Zones" | The same table says "Pool-split offence/defence: **Use.** Core combat mechanic", which is the approach's ancestor; and its §1.5 and §5 item 4 ("extract the simplified formula for non-zoomed resolution") are the auto-resolve formula Layer 1 §27.2 refuses. The document is superseded on both points (R-PC-41) |
| C-6 | §1.3, F-PC-13: disposition is monotone (56.3% and 41.4%), so "a choice built on it has one right answer" | Confirmed with the repository's own instrument (`build_levers.py disposition 2000`: 57.7 and 40.8). The cause is one hook, not the axis (F-PC-17) |
| C-7 | R-PC-22 and P5 §2: `DuelState` has four fields; the host or adapter holds it | A fifth piece of state crosses engagements (the weapon form, F-PC-16); an adapter may hold nothing and the field's adapter never runs between field turns (F-PC-19) |
| C-8 | F-PC-10: 18 engine constants are outside the export | 64 numeric constants in five modules are, among them the whole wound and stamina model, and so is every field of every weapon (F-PC-15) |
| C-9 | §12 `[UNVERIFIED: clients of sigma.odds_of not opened]` | Opened: `choose.odds_weight` asks `View.odds` for a contested candidate under the shipped `odds_weighting: believed`; the query answers `None` for a band of another module (`seam/wrappers/sigma.py`, `believed_chance`), so a fight is never priced by believed odds in the chooser |
| C-10 | §7: Fire Emblem and Final Fantasy Tactics "presuppose a progression layer" and did not transfer | They were asked about directly: the held proposal's Appendix A answers Jordan's question of what a Final Fantasy Tactics game on this engine would be, and maps one command per unit per turn onto one plan per engagement. It is the nearest thing in the tree to a precedent for the stated intent, and it is unsurveyed (the precedent suite has no row for either game) |

### B2.2 New findings

**F-PC-15 · hygiene with a port cost (widens F-PC-10) · The typed export carries the weapons' names
and nothing else about them.** `engine/engine_params/combat_engine_v1.json` holds `CFG` (214 keys),
`core`'s constants, the attribute spec and a `kit` section of 54 names. No field of any weapon
record, none of `weapon_physics.py`'s 33 module constants, none of `combat_systems.py`'s 18, none of
`combatant.py`'s 8 (Wound Interval, Max Wounds, Health, Stamina), no ability and no tradition is in
it (`probe_weapons.txt`; E-B3). The four half-sword forms are listed as weapons a person may be armed
with. Falsifier: any weapon field or any of those constant names found in the JSON; outcome none.
Consequence: the port has the σ coefficients and nothing to apply them to; the engine's central claim
(behaviour derives from physical primitives) is the part that does not cross. Fix:
`proposals/03_PC_weapon_records_in_the_export.md`.

**F-PC-16 · correctness, latent in the season · The half-sword form persists across engagements, and
the next engagement opens on it.** The open-measure reset (`wrapper.py:83-90`, ED-PC-0033) zeroes
grip and lunge and leaves `Combatant.weapon` as the last closed exchange set it (`:273-274`). In 800
fights, 1,142 of 3,318 fighter-starts entered a later engagement in a half-sword form
(`probe_round_state.txt`). With the form reset at engagement start, the share of engagements opening
at open measure moves from 36.4% to 60.5% for a longsword against an arming sword in plate (control
35.9%) and from 88.7% to 25.6% for an estoc (control 88.9%); the share of decided fights moves beyond
its control in one of five matchups (longsword against mace, 74.8 to 78.9, control 74.5)
(`probe_form_reset.txt`). The reach labels do not invert (0 of 1,958 half-sword starts); the
re-presentation gate reads the record in hand. It is the defect ED-PC-0033 fixed, one field over, and
the engine's own predicate ("full form at reach", `combat_systems.py:880-890`) says which side is
wrong. It reaches no season fight today (arming sword, light armour). It is also round state the
first proposal's `DuelState` omits. Fix: `proposals/03_PC_weapon_form_at_round_start.md`.

**F-PC-17 · design (refines F-PC-13) · The monotone advantage of aggression is one hook, the
initiative drift; without it the lean is a small weapon-conditional trade.** Disposition has three
hooks (`config.py:280-286`): commit skew, counter tilt and a per-beat initiative drift
(`wrapper.py:164`, `DISP_INIT_K`). Leaning fighter against a normal one, arming mirror, n 2,000
(`probe_disp_matrix.txt`): as built, aggressive 58.2% and defensive 43.1% (control 50.3%); with the
drift at 0, 52.4% and 47.5%; with commit at 0, 56.0% and 42.5%; with counter at 0, 58.6% and 42.4%;
the drift alone, 56.1%. Aggressive against defensive reads 63.5%: a strict order, no cycle. With the
drift off and the lean doubled (`probe_lean_wide.txt`, n 1,500) the sign follows the weapon: mace
mirror aggressive 43.2, defensive 51.5; rapier mirror 50.9 and 45.9. That is the design's own
commitment-and-recovery claim (`combat_throughlines_v1.md`) showing up in outcomes. Falsifier: with
the drift at 0, an aggressive lean outside the control band in the arming mirror; outcome 52.4 (interval
50.2 to 54.5) against 50.3 (48.1 to 52.5), inside. Consequence for the design: the first proposal's
plan (add a lean to `disp_lean`, then sweep three costs) would import the one hook that has no cost.
The comment's "BOTH poles cost" is false for that hook only. Fix: proposal B §3 (the approach never
moves the drift) and its step 3e (`DISP_INIT_K = 0`).

**F-PC-18 · design (an unclear passage in the intent, resolved) · "Phase" has a referent in the design
set, and it is not a whole round.** The state graph names the moments a fighter could lean in
(`state_graph.py::INJECTION_POINTS`); `ability_armature.md` §2a calls them phases (Approach,
Initiative, Exchange, Separation); the recovered plan names seven phase-slots; the held Plan layer
puts one intent on each of six of them; Jordan's sentence of 2026-09-30 asks for "a duel version
where you actually decide at each step/beat" and a grid version where "you choose to attack and then
… see the bout" for a round (`05_two_modes_of_one_bout.md:8-11`). The 2026-11-12 intent says the
same in other words: per phase in the duel, one selection on the grid. The first proposal asks once
per round in both modes. Resolution R-PC-27; proposal B §3 and §4.

**F-PC-19 · contract (Layer 1) · The first proposal puts round state on a host adapter and has the
field's adapter interleave rounds; neither can be built as written.** Layer 1 §44.3: a wrapper never
holds state, decides, resolves or drives a clock (`holonic_ARCHITECTURE.md:1679-1686`). The field is
one provider call (`seam/wrappers/mass_battle.py:446`); its adapter runs before and after the battle,
not between its turns. Resolution R-PC-30: state lives in the frame of the loop that calls the round;
a module that needs the round is handed a callable. §B4 gives the whole Layer-1 reading.

**F-PC-20 · integration (the loadout rule's individual side) · The roster the MB lane proposes as
the only weapon roster is melee only.** 54 records: 50 weapons and 4 forms; no pike, javelin, bow,
crossbow or sling (five of the ten classes of `modules/mass_battle/equipment/weapons.py::ARSENAL`),
no shield, no unarmed record; the engine has no ranged resolution (the July wiring audit §3.1 and
the defect register D7, re-verified here by the roster scan). "Archers carry arming swords too" has
an individual-kit side only for the sword. Resolution R-PC-38; §B7.

**F-PC-21 · design (extends F-PC-09 and F-PC-02) · Of the levers a "suite of skills" would be, four
skill axes are real, two are not, and the weapon still erases the build.** `build_levers.py` at this
SHA: +1 on bind 61.4%, dodge 60.8%, balance 59.5%, parry 58.1%; technique 50.1% and grab 47.6%
(inside the interval, n 1,000); all six, 79.6%. Skills are uncapped (`combatant.py:197`). Abilities
at levels 1 to 8 stay within 4 points of 50 (n 600). Four archetypes with different attributes,
skills and kits land at 93.6, 94.9, 95.7 and 95.4 against a neutral fighter (the July report's D1,
standing). Consequence: equipping skills that "correspond to levers" is half true in the engine
(skills move outcomes; techniques do not) and wholly untrue in a season (no carrier). R-PC-43.

**F-PC-22 · hygiene · Instrument and comment text that no longer describes the code.**
`build_levers.py:158-161` says no site charges the wearer for armour; `act_cost` has done so since
PC-20 (`combat_systems.py:168-174`; heavy armour at Strength 4 costs 2.595 stamina an action against
2.095). `state_graph.py:33-39` says `beat_exhaustion` is reachable, "MEASURED, do not re-litigate";
its own self-test prints the dead-branch flag for it, and a sweep of 1,728 fights over twelve
weapons, three Endurance values and two armour tiers saw it 0 times (`probe_beat_exhaustion.txt`).
`state_graph.py`'s `site:` values cite `wrapper.fight:282` and neighbours (the function is at `:555`).
`probabilities.py:55` cites `wrapper.py:173-198`. `weapon_physics.py:3` names `combatant.WEAPONS`.
`combat_flow_skeleton_v1.md` S2.7.19 describes a `disrupt_resist_p` branch deleted at PC-11.
R-PC-39.

**F-PC-23 · hygiene (extends F-PC-08 a) · The workbench owns a third copy of the roll.**
`workbench/probabilities.py::degree_distribution` rebuilds the mean and spread of the exchange roll
from the frozen harness's constants (`tests/sim/v32-combat-balance/m1_dice_sigma_core`), not from the
dice engine `core.resolve` uses. The odds a narrated trace prints are therefore a second derivation
`[UNVERIFIED: not compared numerically here; the file names its falsifier,
tests/valoria/test_combat_ob_from_defender_consumers.py]`. R-PC-42.

## B3. The intent, set against the full design set

**The intent (Jordan, 2026-11-12).** Each character equips a weapon, armour and a suite of skills
that correspond to levers; chooses an intensity or approach of attack per phase (aggressive, normal,
defensive, …); and the fight works moment by moment as a duel and, inside turn-based grid combat in
the manner of Final Fantasy Tactics or Tactics Ogre, as a duel round the engine executes from the
selected approach, both on one code path.

**What each design document says of it, and what the code does.**

| part of the intent | where the design set carries it | the code at this SHA | verdict |
|---|---|---|---|
| a weapon | the weapon as physical primitives (`weapon_physics_and_concentration_model.md` §1 to §6, built; `REARCHITECTURE_v1.md` L0) | 50 startable records of located mass; every dynamic derived; none exported (F-PC-15); the season arms everyone alike (F-PC-02) | built in the engine; not in the export, not in the season |
| armour | four tiers; "Armour = damage reduction only" (`weapon_physics_and_concentration_model.md` §0) | target-side protection, plus a wearer-side stamina cost when Strength is short of the tier's demand (PC-20); heavy against none still 94.9% (n 1,000) | built; the largest unpriced lever after the weapon |
| a suite of skills that correspond to levers | an ability targets a lever addressed by a phase and a competence (`ability_armature.md` §2); seven phase-slots and a budget (`phase4_5_plan_v1.md` 4b, not started); abilities as access, efficacy from investment (fiat audit, Jordan's principle) | six skill axes (four live), 30 abilities over 15 levers (aggregate effect inside noise), no slots, no budget, no carrier in the season | the vocabulary and the hooks exist; the content and the carrier do not (F-PC-21) |
| an approach per phase | the Offence and Defence pool split, "the action economy" (`combat_reference_v1.md` §1; `videogame_mode_spec.md` §1.1); four stances with a counter table, with "2 stances (Aggressive/Defensive)" as the simpler option (`combat_c4_draft_v0.md` M2 and Q4); six intents, each "a prior, not a command", each "a trade with both ends wired" (the held Plan layer §2.1, §3) | absent. Disposition is fixed for the fight and monotone because of one hook (F-PC-17) | asked for four times, built never |
| moment by moment as a duel | "decide at each step/beat"; intents at the six open moments; the read, the bind entry and the burst length stay the engine's (`05_two_modes_of_one_bout.md` §2) | one binary choice per turn for a played person (`wrapper.py:586-592`) | the suspension exists; the choice and its cadence do not |
| an automatic duel round on a grid | "the GAME calls one engagement per turn" (`wrapper.py:576`); the flow skeleton records "the intended per-turn game entry point, `wrapper.engagement`, has no outside caller"; the scene envelope wraps `engagement` and never forks it (`scene_combat_design_v1.md`) | no entry fights one round; no grid at person scale | designed from the first day, never exposed |
| one code path | one engine at three fidelities (`05` §1.6); Layer 1: no second resolver, fidelity never forks the slice | one resolver; two doors (F-PC-07) | holds for the resolver; §B4 |

**Three judgements the documents support.**

1. *The approach is the pool split, returning.* The tabletop design's per-round choice was how many
   dice to put on offence and how many on defence, with Full Guard as its end. The physics engine
   replaced the pool with a continuous commit depth and gave the choice to a random draw skewed by
   temperament. Every later design that wanted the player back in the fight (C4, the Plan layer)
   re-derived a lean on that draw. Aggressive, normal and defensive are the same request at its
   simplest.
2. *The design set has two rules the approach must meet, and the engine's nearest axis breaks one.*
   A lean is a prior on a gate the engine already rolls (never a command, never an imposed outcome:
   ED-PC-0023), and every lean pays at both ends in the same change (the held proposal's rule 3,
   written because of disposition). The drift hook pays at one end.
3. *The grid in the intent is not a new subsystem.* Layer 1 calls it grid squad combat, the battle
   seam one scale down with every combatant a person; the September suite recommends the cell field
   at weight 1. Positions, movement and turn order are that module's. Personal combat supplies the
   round and nothing else.

**Against `weapon_physics_and_concentration_model.md`.** §§1 to 6 are built and are the reason a
weapon is a real lever. §7, the concentration error (a threshold below which a tired mind misfires),
was never built, and Focus is the attribute the July report measured as buying nothing; it is the
one place where a skill-like lever (keeping one's head) is specified, grounded and absent. It is not
needed for the approach and is not proposed here.

**Against `pc_formation_system.md`.** It is mass battle's design, and its top level is an army
doctrine of Aggression: Cautious, Balanced, Pressing, with the rule that an instruction modulates
primitives and adds no flat number. The personal approach is the same dial one scale down and should
keep the same rule; that is the argument for the leans in proposal B and the argument against its
optional transfer term, which §B10 leaves to Jordan.

**Against the research.** The lane file's verdict stands: no surveyed game precedent exists for the
bout (T-PC-6). The precedents that do transfer are about the frame, not the clash: a plan, stance or
script set before the engine resolves is a nine-game pattern (`THROUGHLINES.md` P36, among them
Imperator's approach chosen before battle and Empires in Arms' secret pick), and a per-character
priority list of conditional tactics with an automatic fallback is Unicorn Overlord's (`T19`: up to
two conditions per tactic; with none set a character attacks what is in front; an Optimize button
for players who will not hand-tune). Both support a default that needs no input and a choice that is
set in advance. **Nulls:** Final Fantasy Tactics and Tactics Ogre, the games the intent names, have
no row in the precedent suite; the September document's account of their clash is marked unverified.
Nothing in the research says three approaches are enough, or that a per-phase choice inside an
automatic round has been shipped. Neither may be cited as support.

## B4. One resolver, run by a chooser (Layer 1)

Asked by the coordinator after the coverage digest `digests/DG_canon_arch1.md`; the passages were
opened at the cited lines.

**What Layer 1 says.** "No second resolver. No auto-resolve formula. No fast path", enforced "by a
person noticing" (`holonic_ARCHITECTURE.md:984-990`, §27.2; listed among the seam's leaks at `:1392`
and the refusals at `:1962`). A wrapper never holds state, decides, resolves or drives a clock; "a
wrapper that computes an outcome **is** the second resolver" (`:1679-1686`, §44.3). Fidelity does not
fork the slice: a scene summarised, narrated or expanded is "the same object; only its rendering
changes", and the two "agree exactly" (`03_VERBS_AND_LOOPS.md:146-153`, §C.4). One resolver and one
ladder (`04_CODE_ARCHITECTURE.md:122`, T-k; `:761`, graded CONVENTION). Grid squad combat is the
battle seam one scale down (`:811`).

**How the duel round and the approach stay inside it.**

1. *The automatic round is the resolver, not a formula for it.* A grid attack calls
   `wrapper.engagement` once, through the `round` entry. Nothing estimates, tabulates or shortens
   the engagement. "Automatic" describes who supplies the approach and how much of the trace is
   shown.
2. *The modes differ only in rendering and in who chooses.* The duel, the grid attack, a contact
   inside a field and an unwatched fight are the same call on the same record. With equal plans,
   state and seed the outcomes are identical, which is the "agree exactly" of §C.4 and a stronger
   test than the first proposal's reading in expectation. The per-round private stream is what makes
   a fight identical whether its rounds are called in one frame or one at a time.
3. *The approach is an input to the one roll, not a modifier on its result.* It enters as `plans`
   on the typed input and is read inside `combat_systems` at gates the engine already rolls. A host
   that adjusted a round's result by the approach would be the second resolver; proposal B forbids it
   and names it as a falsifier.
4. *A chooser, not the wrapper, picks.* Every claimant has a decider: the player's call-out for a
   played person (REM-31), `choose.approach_of` for everyone else, a standing order evaluated into
   the same callable for a squad member. The adapter builds the callables and decides nothing; the
   module asks them and cannot tell them apart. "Every person decides" (CHAR §0A I-1) then holds
   inside a fight, where today it does not.
5. *No one holds state.* `DuelState` is a value in the frame of the loop that calls the round, for
   one provider call. Health between scenes stays `Person.body`, written by the fold.
6. *The chooser uses no outcome model.* It scores temperament and what the person sees. An estimate,
   if ever wanted, is the resolver sampled on a private stream (the shape of the existing `estimate`
   provider), never an approach-against-approach table.

**Where it does not fit cleanly (named; Layer 1 is not edited).**

| item | the two options |
|---|---|
| The adapter row of `04` §A.2 lists "the projection" as the wrapper's input. `host` is already a declared departure (`seam/wrappers/combat.py:331-332`). Deciders for every claimant, and a `duel` callable handed to a field or skirmish module, are two more | (a) read the row as admitting person-supplied callables as one class of input, declared once; (b) keep each as its own declared departure, which makes the count of departures grow with every mode |
| A field or skirmish module invoking a callable that runs another module's resolver is nested resolution; §39.3 gives nesting a depth cap with no default and warns that "a nested instance is an instance" is not a bound (`holonic_ARCHITECTURE.md:1397-1402`) | (a) the callable is a nested contest and is counted against the cap, with a typed error at the cap; (b) the grid or field owns no loop of its own at person scale: each attack is its own act with its own provider call, the round's state is written to the world between acts through the fold, and nothing nests. Option (b) costs a carrier for the round's state (CR-85 §4 step 2's question) and makes a grid battle span acts (J-15's question) |
| The upset flip reverses a decided fight after the engagement has resolved (`wrapper.py:618-624`) | already the first audit's §11 item 3; under the round design it stays on `fight`'s integer, which the fold does not read, and no round has one |
| `videogame_mode_spec.md` §1.5 prescribes a simplified formula when the player does not zoom in | superseded by Layer 1 (R-PC-41); recorded so that nobody builds from it |

## B5. The design, in brief

The whole design, its edits by owner, gates and falsifiers are in
`proposals/03_PC_duel_round_and_approach_B.md`. In brief:

- **The round.** `fight.round(DuelRoundInput, rng, deciders) -> DuelRoundOutcome`; `fight` is the loop
  over it. `DuelState` is damage, stamina, concentration, poise and the weapon form, which is the
  whole set a probe finds crossing an engagement boundary.
- **The approach.** `APPROACHES = (defensive, normal, aggressive)` over `PHASES = (measure, exchange,
  bind)`. A lean moves commit depth and counter selection in the exchange and the fighting
  withdrawal in the bind, all with both ends already built; the `measure` lean waits for its costs.
  The drift hook is retired. An optional conserved transfer between a fighter's own attack and
  defence makes intensity change how long a fight lasts, how much blood the winner pays and how
  often it ends undecided, while a mirror stays level (rounds 2.34, 3.50, 6.16; undecided 0.0%,
  0.4%, 7.9%; `probe_guard_transfer_K030.txt`).
- **The cadence.** The decider is consulted at the top of a round and whenever a phase is entered. A
  duel asks the player each time; a grid attack gives one answer for the round.
- **Order.** Round and loop (hash EQUAL), private stream (one re-record), leans (byte-identical at
  `normal`), drift retired (season EQUAL), deciders and chooser (EQUAL with no cell authored), field
  contact.

## B6. What the chooser must do to pick an approach for an NPC

The NPC and chooser intent is CHAR's statement, `audits/02_CHAR_audit.md` §0A (I-1 every person
decides; I-2 on his own state; I-5 the option set is computed; I-6 a choice is a ranking by values and
regard, sampled; its limit (2): inside a contest an NPC has no decider). It is cited, not redone.
Against `decision/choose.py` and `options.py` as read:

| question | answer from the code | what must be added |
|---|---|---|
| (a) what an NPC decides in a fight, on what information | nothing today. The chooser ranks whether to fight (`opening_set`, `score_terms`); the fight then runs with `decide=None` | an approach at each consult, from his projected pursuits, the view (phase, round, measure, both parties' wound bands, his own leans) and nothing else |
| (b) one interface for player and NPC | before the fight yes (`choose(p, v, s, ask_budget)`); inside it no | `(CombatTurnView) -> str` for every claimant; the adapter supplies `host.decide` or a closure over `choose.approach_of` |
| (c) NPC rules hard-coded in the subsystem | the first audit's list stands: engage every turn, disposition 4, one yield fraction, every yield accepted, never withdraw | `approach_of` removes the first two; the others are `03_PC_exits_withdrawal_recovery.md`'s |
| (d) characterful and legible | CHAR's proposals give temperament a table (`02_CHAR_choice_alignment.md`) and a per-person steadiness (`02_CHAR_resolve_and_temper.md`) | the `approach` block of that table read per phase; a response table of what a person does when he or his opponent is wounded; the consult's view and the winning term on the `approach` trace event |
| (e) what is missing | `choose.approach_of`; `CHOICE_RANGES['approach']` as a pointer to the module's set; `rosters.yaml: approach_responses` (empty); per-party deciders at the seam | proposal B §5 and step 4 |

**Four properties the function must have, each from a precedent in the file it joins.** It reuses
`score_terms`' dot product rather than a second scoring rule (the file's own "ONE owner of the
formula", `choose.py:193-197`). It samples by `_sample_order`'s rule, with the noise keyed to the
value and not to the round, on a stream that is not the fight's (`:441-454`; a missing draw at a
non-zero temperature raises, `:434-440`). It returns `normal` without drawing when no cell and no
response row is authored, so the shipped realm is unmoved (the `tau == 0` control's reasoning,
`:352-358`). It reads no `World` (AX-2 by path).

**Two decisions where the lanes differed.** CHAR's proposal puts the approach on the act as a
`choice_sourced` value fanned at DELIBERATE and leaves in-contest change to "a policy inside the
module parameterised by data on the typed input". Decided here (R-PC-34): no fan, and no module-side
policy. A fan triples the violent candidates to pick a value the fighter re-chooses each phase, and
the roster's own note says the fan is a draw; a policy inside the module would have the module
decide for a person, which is what I-1 and §44.3's "never decides" exclude and what makes the player
and the NPC different kinds of agent. The alignment cells stay CHAR's and are read by the decider.
One sentence of CHAR's proposal must change with this (its loader rule should refuse a key outside
`CHOICE_RANGES`, not a key that is not `choice_sourced`); it is named for that lane.

## B7. The loadout rule shared with mass battle: the individual-kit side

The MB lane judges the unit side (`audits/04_MB_audit.md` F-MB-19;
`proposals/04_MB_unit_loadout_and_weapon_in_hand.md`). The first PC lane wrote the shared rule
(`proposals/03_PC_loadout_and_carry.md`, R-PC-26): one `carry_demand` leaf over a kit with a
secondary, charged in the Strength-demand form `act_cost` already uses, with the weapon in hand as
round state. That proposal is not redone. What the reading adds to the individual side:

**What an individual's kit costs today** (`probe_weapons.txt`).

| charge | rule | owner | example |
|---|---|---|---|
| stamina per action, weapon | `ACT_BASE + ACT_WEIGHT × wield_heft + ACT_COMMIT × commit`, of the weapon in hand | `combat_systems.py:168-174` | 1.76 for a dagger to 3.16 for a guandao at commit 3 |
| stamina per action, armour | `ACT_WEIGHT / D_WT × max(0, ARMOR_DEMAND[tier] − Strength)` | the same line; `config.py` `ARMOR_DEMAND` 0, 1.67, 3.33, 5.0 | +0.5 for heavy armour at Strength 4; 0 for the other tiers |
| handling (σ on attack and defence) | `HANDLE_K × max(0, str_demand − Strength)`, `str_demand` from reach, swing inertia, balance, two hands and `D_MASS × mass` | `:183-189` | demand 3.0 (dagger) to 9.5 (guandao) against a default Strength of 4 |
| tempo | swing inertia of the weapon in hand | `weapon_tempo`, `close_tempo` | — |
| closing speed | balance and the weapon's tempo | `:1380-1387` | armour and carried mass do not enter |

Nothing reads what is carried and not held; armour has a Strength demand and no mass; a kit is one
weapon. So "carrying more raises fatigue and lowers movement speed" is true of nothing at individual
scale, and the form it should take is already in the engine twice (the harness term and the handling
penalty are both `max(0, demand − Strength)`).

**The one rule at one owner** is the first lane's `carry_demand`, and this reading supports it with
three amendments.

1. *The weapon in hand is already state, in one narrow form, and the proposal should build on it.*
   The half-sword form is a record in hand that persists across rounds (F-PC-16). `in_hand` and the
   form are one field: the key of the record currently held.
2. *The single roster must be able to hold what a unit carries.* It cannot hold a bow (F-PC-20).
   Decided in `03_PC_weapon_records_in_the_export.md` item 6: a pike is content in the existing
   schema; a ranged weapon waits for a ranged resolution; until then MB's ranged classes carry only
   a `mass`, the one field `carry_demand` needs, and that is the declared exception.
3. *The mass a unit is charged for must come from where the person's does.* `mass` per weapon is not
   in the export (F-PC-15); the same proposal adds it, so that `carry_demand` reads one table at both
   scales.

A fourth matter is recorded and not decided: which weapons may be carried where. The held proposal's
§12 derives a carry context from stored length and hands (concealable to 0.60 m, a sidearm to
1.20 m, a weapon of war from 1.50 m, with every dominant weapon in the last band). It is a legality
rule, not a cost rule, it crosses PC, SE and FA, and it remains held with that proposal.

## B8. Resolutions

Continuing the first audit's table (which ends at R-PC-26). Each is decided by the first rung of
CLAUDE.md §0's ladder that answers it. `PB` = `03_PC_duel_round_and_approach_B.md`, `PX` =
`03_PC_weapon_records_in_the_export.md`, `PF` = `03_PC_weapon_form_at_round_start.md`.

| id | inconsistency, gap or unclear passage | decided resolution | rung | carried by |
|---|---|---|---|---|
| R-PC-27 | "per phase" can mean per round or per phase of the engagement | per phase of the engagement (`measure`, `exchange`, `bind`), consulted when a phase is entered; a grid attack gives one answer for the round | 3 (Jordan's sentences of 2026-09-30 and 2026-11-12; the state graph's own moments) | PB §3, §4 |
| R-PC-28 | P5 adds the approach to `disp_lean`, moving all three hooks | own coefficients on commit, counter and the bind break; the drift is never moved | 5 (the measurement at F-PC-17) | PB §3 |
| R-PC-29 | `config.py:280-286` says both poles cost; the drift charges only caution | `DISP_INIT_K = 0` | 4 (ED-PC-0037 deleted `ATTACKER_BIAS` for the same reason, `combat_systems.py:1109`) | PB step 3e |
| R-PC-30 | where round state lives | in the frame of the loop that calls the round, for one provider call; another module gets a `duel` callable | 3 (Layer 1 §44.3) | PB §2, §4 |
| R-PC-31 | `DuelState` omits the weapon form | carried as `form` for step 1's equality; dropped if PF lands | 4 (ED-PC-0033) | PB §2; PF |
| R-PC-32 | step 4's gate is a reading in expectation | exact equality for equal plans; an expectation reading is a balance reading of the choice | 3 (Layer 1 §C.4) | PB step 4 |
| R-PC-33 | two readings of "grid" (cell field or tactics grid) | one build: the cell field at weight 1, every combatant a person | 3 (`04_CODE_ARCHITECTURE.md:811`) | PB §8 |
| R-PC-34 | an NPC's in-fight choice: a `decision/` function, or a fan at DELIBERATE with a module-side policy | the person's decider, from `decision/`, reading CHAR's alignment cells; no fan, no module policy | 5 (one agent interface; I-1) with 4 for its parts (`score_terms`, `_sample_order`) | PB §5 |
| R-PC-35 | the off-hand slot listed as a gap | closed: out of scope by ED-PC-0055's last row; re-open only with the first weapon that needs one | 1 superseded | none |
| R-PC-36 | the export omits every weapon field, the wound model and 64 constants | `weapons`, `derived` and per-module constant sections | 3 (CLAUDE.md §5) | PX |
| R-PC-37 | forms listed as kits | `kit.weapons` (50) and `kit.forms` (4) | 5 | PX |
| R-PC-38 | one roster cannot hold a unit's ranged weapons | pike as content; ranged waits on a ranged resolution; `mass` only until then | 3 for the pike, 5 for the exception | PX item 6 |
| R-PC-39 | six stale texts in instruments and comments (F-PC-22) | correct each at its site: the armour docstring; `beat_exhaustion`'s note to say what the sweep now shows, or widen the fixture until it fires; drop the `site:` line numbers as the injection table already did; the two stale citations | 2 or 3 at each site | none (edits named here) |
| R-PC-40 | the held proposal's Q1 (decision cadence) and Q2 (is disposition a trade) are listed as Jordan's | both answered by the 2026-11-12 intent: the cadence is the phase in a duel and the round on a grid; an approach offered as a choice among three is a trade | 3 | PB |
| R-PC-41 | `videogame_mode_spec.md` prescribes an auto-resolve formula and no grid | superseded by Layer 1 §27.2 and `04:811`; nothing is built from it | 1 | none |
| R-PC-42 | the workbench re-derives the exchange roll from the frozen harness | call the roll's owner, as R-PC-17 does for `core.resolve` | 4 | the first lane's typed-outcome appendix, extended |
| R-PC-43 | two skill axes move nothing; skills are uncapped | do not expose `technique` or `grab` as levers until a sweep shows them outside the interval (the methodology's ablation gate); bound skills where capabilities are authored | 3 (`combat_balancing_methodology.md` §6) | `03_PC_person_inputs_content.md` (first lane), amended by this row |

Seventeen resolutions decided here (R-PC-27 to R-PC-43); forty-three with the first audit's.

## B9. Proposals written by this lane

Under `proposals/2026-11-12-subsystem-audit-suite/proposals/`:

1. `03_PC_duel_round_and_approach_B.md`: supersedes the first lane's proposal 5 where they differ.
2. `03_PC_weapon_records_in_the_export.md`: the export carries the weapons, the wound model and the
   physics constants; forms are not kits; what a single roster can and cannot hold.
3. `03_PC_weapon_form_at_round_start.md`: the half-sword form is reset with the grip.

The first lane's `03_PC_loadout_and_carry.md` is amended by §B7 and not rewritten.

## B10. Survivors for Jordan

The first audit's three stand. One is added; it survives the ladder because the design set points
both ways and the two options are different games.

4. **Is intensity a declared term, or only a lean on the engine's own draws?**
   *Option A, leans only.* An approach skews commit depth, counter selection and the bind break. It
   obeys the principle recorded for formations (an instruction modulates primitives and adds no flat
   number) and ED-PC-0023's rule against imposition. Measured, it is a small edge whose sign depends
   on the weapon and a modest change of pace (rounds 3.25, 3.50, 3.74 for aggressive, normal and
   defensive mirrors). The choice is real for a player who knows his weapon and nearly invisible to
   one who does not.
   *Option B, leans plus a conserved transfer.* A fighter also shifts weight between his own attack
   and his own defence. A mirror stays level by construction; the fight's length, the winner's
   wounds and the chance of no decision all move with the two fighters' summed intensity (rounds
   2.34 to 6.16; undecided 0% to 7.9%). The choice is legible to anyone and is the old pool split in
   the engine's unit; it is also a term no primitive produces.
   Not settled by a document: the pool split is "Core combat mechanic" in a superseded specification
   and distilled into a pool split by a deferred ruling (ED-PC-0007), while the engine's own design
   notes ask that effects emerge. Proposal B builds A first and B behind a coefficient of 0.

**Named and not resolved** (conflicts with ruled, ratified or recorded items; detail in proposal B
§8): ED-PC-0007's reopen condition; CR-85 §4 step 2; the ratified suspension does not cover a
consult inside a round; the adapter row of `04` §A.2 and nested resolution under §39.3 (§B4's
table); ED-IN-0304's risk appetite as the temperament carrier; J-15.

## B11. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PC_B/`.
All runs `PYTHONHASHSEED=0`. No pytest was run. No tracked file was written by any run
(`armour_participation.py` was run with `--drift` only, which writes nothing).

| id | command or probe | seeds, counts | outcome |
|---|---|---|---|
| E-B1 | `probe_weapons.py` → `probe_weapons.txt` | — | 54 records, 4 forms; hands 1: 19, 2: 35; mass 0.22 to 3.80 kg; no ranged, shield or unarmed key; `ARMOR_DEMAND` 0, 1.67, 3.33, 5.0; `act_cost` at commit 3 from 1.758 (dagger) to 3.158 (guandao); heavy armour 2.595 against 2.095; export sections attributes 8, cfg 214, core 26, kit 3; `weapon_physics` 33 constants, 0 exported; `combat_systems` 18, 0; `core` 19, 18 |
| E-B2 | workbench imports, from the workbench directory | — | all eleven modules import |
| E-B3 | `python -c` over `combatant`, `contact`, `geometry`, `traditions`, `ability_primitives` against the export | — | `combatant` 8 constants, `traditions` 2, `ability_primitives` 3: none exported; no `ABILITIES` or `TRADITIONS` key; 30 abilities |
| E-B4 | `workbench/build_levers.py disposition 2000` | crc32 seeds | disposition 1 to 7 against 4: 40.8, 44.0, 48.2, 53.3, 54.6, 57.7 |
| E-B5 | `build_levers.py mirror 2000`, `armour 1000`, `skills 1000`, `archetypes 1000`, `abilities 600` | — | mirrors 48.2 to 52.1; heavy against none 94.9; skills as F-PC-21; archetypes 93.6, 94.9, 95.7, 19.3 (dagger grappler), 95.4; abilities 48.8 to 54.3 |
| E-B6 | `workbench/structure_scan.py`; `state_graph.py`; `capabilities.py`; `armour_participation.py --drift` | — | duplicates `adef_cap`, `fight`; zero-caller functions 0; inline literals 94; `sys.path.insert` 10 in the engine, 38 in the workbench; dead exported keys `[]`; state graph PASS with the dead-branch flag on `beat_exhaustion`; capabilities PASS; drift 0 cells |
| E-B7 | `probe_round_state.py` | four matchups × seeds 0 to 199 | 1,659 later engagement starts; state differing from the fight's start: stamina, concentration, poise, damage, weapon (1,142 fighter-starts), plus per-beat fields re-derived inside the round |
| E-B8 | `probe_form_reset.py` | five matchups × 3,000 fights, seeds from 0; control from 500,000 | as F-PC-16 |
| E-B9 | `python -c`: estoc against arming sword in plate, 600 fights | seeds 0 to 599 | 2,558 engagement starts; 1,958 with the estoc half-sworded; the arming sword labelled longer in 0 |
| E-B10 | `probe_disp_matrix.py 2000` | crc32 seeds | 3×3 and the single-hook ablations, as F-PC-17 |
| E-B11 | `probe_disp_matchups.py 1500` | crc32 seeds | eleven matchups, as built and with the drift off; with it off every cell within about 3 points of `normal` |
| E-B12 | `probe_lean_texture.py 2000` | seeds 0 to 1,999; control from 1,000,000 | with the drift off, mean rounds 3.25, 3.50, 3.74 for both-aggressive, both-normal, both-defensive; the winner's damage 38.9%, 35.6%, 36.2% |
| E-B13 | `probe_lean_wide.py 1500` | seeds 0 to 1,499 | lean ±2, drift off: arming 49.4 and 46.8; mace 43.2 and 51.5; rapier 50.9 and 45.9; +2 against −2 in the arming mirror 50.3 |
| E-B14 | `probe_guard_transfer.py 1500 0.30`, and the same with the commit lean riding | seeds 0 to 1,499; control from 1,000,000 | as proposal B §3; with the commit lean riding the nine cells read 49.8 to 52.2 and both-defensive 10.1% undecided |
| E-B15 | `probe_beat_exhaustion.py` | 12 weapons × 3 opponents × Endurance 1, 2, 6 × none, heavy × 8 seeds = 1,728 fights | separations: clean defence 4,590, burst ceiling 449, collapse 204, beat exhaustion 0 |
| E-B16 | `git diff --stat 2c24c81 HEAD -- modules engine systems tools references architecture` | — | empty |

**Limits of these readings.** The lean probes use disposition 1, 4 and 7 (and values outside its
scale for ±2) as stand-ins for an approach that does not exist; the transfer probe patches one
function for the run. They show shape and direction for a design decision. None is a balance figure
to ship, and no coefficient is recommended from them. The mis-specified "better fighter" rows of
E-B14 (the default faculty is 3, so both rows are mirrors) are not used.

**Not read:** the items marked in §B1; the remaining 57 combat test files; `modules/combat/core.py`,
`contact.py`, `geometry.py`, `traditions.py`, `ability_primitives.py` beyond the lines cited (the
first lane read them); the research lane file beyond the rows named.
