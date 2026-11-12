# Audit brief — shared by every Fable lane in this suite

## Status: REFERENCE (a work order, not canon; resolves nothing at runtime, CLAUDE.md §0.05)

Requested by Jordan, 2026-11-12: a subsystem-by-subsystem **adversarial steelman audit** of code matters,
design matters and the best path forward to a **dynamic, emergent-narrative game** (no GM; the engine
resolves everything), then a holistic audit, then instructions for the nine requirements and for each
subsystem running well alone.

## Standing requirement (Jordan, 2026-11-12): each subsystem is a playable game, in conformance, integrated

**Every subsystem must be able to function as a playable game of its own, comply with the code
architecture (Layer 1, `architecture/meta/04_CODE_ARCHITECTURE.md`; for `modules/`, `holonic_ARCHITECTURE.md`
§43, §45–§47), and integrate with the season loop.** Judge each subsystem against all three at once; they
are one requirement, not three. As an audit standard:

- **Playable alone** — a player (or the headless player-proxy the harness already provides: see
  `engine/season/harness/play_surface.py`, `headless.py`, `exercises.py`) can enter a scenario that
  exercises only this subsystem, see a situation, face real choices, have those choices change what
  happens, meet consequences, and reach an ending or a stable continuation. State what is missing: the
  scenario seed, the choice surface (the verb aperture the player is offered), the legibility of
  outcomes, the stakes, the end condition. "Resolves correctly" is not "plays".
- **One code path, not two** — the standalone game and the season-loop call must run the *same* registered
  module code (typed input, typed outcome, no held state, reached by composition row), not a standalone
  fork and a loop adaptation. A standalone mode that needs code the loop does not run, or a loop path the
  standalone cannot reach, is a finding.
- **Integrates** — what the subsystem consumes from the loop and emits to it must be executed edges (the
  loop's writes and readers, `write_matrix.yaml`, the composition rows in `references/module_contracts.yaml`),
  so that a standalone scene can be entered from the season, resolved, and its outcome written back with
  consequences other subsystems read (the scale-transition question: zoom in and out cleanly, pause the
  other scales correctly).
- **No GM** — everything the game needs a GM for must be resolved by the engine or be a gap you name.

Where the standing requirement and a ruled item conflict, name the conflict and do not resolve it.

## Standing rule (Jordan, 2026-11-12, emphatic): WE DO NOT DO DETERMINISTIC

*"We do not do deterministic!!!!!"* Every consequential outcome in the game resolves by a **draw**: a
probabilistic roll with a graded, recoverable result (the four-band ladder; R-09: chains of events within a
scene are probabilistic, not deterministic). No proposal, design, verb, institution procedure or code path
may make a consequential outcome a fixed function of state: not "evidence enters when presented", not "the
senior office always wins", not "a decree binds", not "the bench rules by score", not "a fight is decided by the
larger number". State sets the **odds** (pool, obstacle as the task's difficulty plus all modifiers, leverage,
modifiers from personality, venue, affiliation, evidence); the draw sets the outcome; a good position still
loses sometimes and a bad one still wins sometimes, within the engine's own bounds.

What this does **not** forbid: seeded replayability (same seed, same world: the RNG is seeded and the draw
is reproducible, which is what lets the engine be tested and ported), bookkeeping that is arithmetic by
definition (conservation of stores, a clock's tick, an id), and eligibility/requirement checks that decide
whether an act may be attempted at all (a person cannot sit a seat he does not hold). The line: *a thing
that could go either way for the people in the fiction goes by a draw.* When in doubt, draw.

For every lane: check your own text and your subject's code against this rule. A deterministic resolution you
find in the code is a finding (severity: degrades narrative; touches R-09); one you find in a document
(yours or another lane's) is corrected at once in your own files and listed for the owning lane if it is not
yours. The known cases to repair: the SC lane's deterministic evidence entry and strike (`05_SC_evidence_and_rebuttal_B.md`,
G-65); any fight that kills with certainty (`F-PC-04`: plain `fight` kills 200 of 200); any verdict that is a
default roll with no spread; any "binds"/"obeyed" effect with no resolution roll; the ruled-in `succession`
rules wherever the tree resolves an heir by a fixed order.

## Standing rule (Jordan, 2026-11-12): DO NOT GUESS; every claim is grounded in the repository

*"All ungrounded information should have info available on repository."* *"Do not guess."* A claim in any
suite document is either (a) **grounded**: it cites a repository path (and line where it is a code or data
fact), or a repository research note that records the external source (publication or URL, date read, and
the tier: page read / snippet / memory), or (b) **marked ungrounded** and not relied on. Memory-grade
history, game-mechanics recollection and `[UNVERIFIED]` engine claims are not acceptable as support for a
design decision. Where external knowledge is needed, the lane (or a grounding lane) sources it and stores
the note in the repository first (under `research/`, in the directory that fits: `research/governance/`,
`research/historical/`, `research/game_precedent_suite/`), then cites it. When you do not know, say "I do not
know" and mark the gap; do not fill it from memory. Exact figures you could not source are not quoted.

## Rulings given by Jordan in this session (2026-11-12; bind every later lane)

**The live list of Jordan's rulings is `unified/DECISIONS_ANSWERED.md` (A-1 to A-56, plus the ladder-closed table). It supersedes anything below and any lane document that disagrees. Read it before you write. Held open: D-34 and D-35 (battle luck and numbers), pending `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. A document that built on the other answer is rewritten or marked superseded by the unification stage.**

1. **Auto-resolve is the same resolver, run automatically** (from standing orders or the chosen approach),
   not a separate quicker calculation. A played and an auto-resolved battle or duel round with the same
   choices agree. Layer 1 holonic §27.2 and `03_VERBS_AND_LOOPS.md` §C.4 (not `04`'s) stand unchanged. Applies to mass battle and to the grid duel round.
2. **A unit is a row of data** on the army's record (troop type, formation, loadout, orders, officer,
   experience), not a thing with its own identity (ED-IN-0306 as ruled 2026-10-28 stands). A regiment's
   story is told through its officer and its men.
3. **A mass battle returns an end state: won, lost or drawn** (with Unopposed and Invested as the field's
   other bands), read off which side broke or conceded, as personal combat's scene is read; how hard it was
   shows in casualties and the report. This narrows Layer 1's "the return is a margin" for the field, as
   combat's exemption of 2026-09-03 did, **on Jordan's word**. Outcomes inside the battle remain draws.

## Authority granted (Jordan, 2026-11-12): author, design and resolve — in the form of proposals

Fable lanes may **author and design improvements, and resolve every inconsistency, gap and unclear
passage they find**, not only report them. (This lifts, for this suite, `CLAUDE.md` §10's limit that Fable
is audit/planner only; it lifts nothing else.) The form is a **proposal**, because a lane edits no code,
registry or canon:

- **Write proposals** to `proposals/2026-11-12-subsystem-audit-suite/proposals/NN_<SUB>_<slug>.md`
  (status line `## Status: PROPOSED`; `NN_<SUB>` as your dossier). Each: the problem (with evidence);
  the resolution, decided; the exact edits, by file and owner (the single owner of each fact, §0.05;
  quote the old and new text or give the structure of the new code and its typed interface); the
  gate that shows it worked (an execution artifact, §0.2); the falsifier; a NERS reading (§0.06, E last);
  cost class; and what it changes in `engine/season/` at runtime (answer this first; a proposal that
  changes nothing at runtime says so).
- **Resolve, do not park.** For every inconsistency (two readings of one fact, doc against code, two
  owners), gap (a hole, an orphan, a row nothing reads) and unclear passage (a rule that two careful
  readers would apply differently) in your subsystem, write the resolution in §6 of your audit, chosen by
  the five-step ladder in order, with the reasoning. Where the code and a design document disagree, the
  resolution follows the code unless the code is the defect; say which. Where a vague rule needs a number
  or a closed set, propose the value and name the owner artifact that would carry it (a typed file code
  reads, not prose).
- **Limits that remain.** Edit nothing outside your own audit and proposal files; do not commit; a
  resolution that would overwrite ratified canon or a `(RULED)` item is written as a proposal AND listed
  in §11 with the two defensible options. Proposals are not ratified by being written (CLAUDE.md §2:
  ratification happens on Jordan's merge, and only if the PR body says so). No guard, no standing
  corpus, no new top-level tree.
- **Count them in your receipt:** proposals written (paths) and resolutions decided (a number, from your
  §6 table).

## Added charge (Jordan, 2026-11-12): adjudicate what the game needs to simulate the provided arcs and characters

The repository holds a provided corpus of **narrative arcs and characters** the game is meant to be able to
simulate: `engine/season/cases/` (`ARC4/5/6.yaml`, `NPC4/5.yaml`, `chain/ARC1-3.yaml`, `chain/NPC1-3.yaml`,
`chain/CASE_BRIEF.md`, `exercises/ARC-nn.yaml`), `engine/season/ENDINGS_CLASSIFIED.yaml`,
`proposals/2026-08-30-arc-reachability/` (arcs 01–55 and the emergent set, with `04_SYNTHESIS.md`), and the
instruments that read them (`engine/season/harness/corpus_run.py`, `run_cases.py`, `exercises.py`, `arc.py`;
`engine/season/gaps.py`; the hole register). Each case states `season_requires:` needs with a hardness
(`core` / `important` / `flavour`) and a `temporal` block.

**Each lane adjudicates, for the cases whose needs fall in its subsystem** (read `CASE_BRIEF.md` first, then
run `python -m engine.season.harness.corpus_run` once and read its output; a need that spans subsystems is
adjudicated by the lane that owns the *mechanism* the need turns on, and cross-listed by the others):

- which `core` and `important` needs the engine **already represents** (cite the code path that makes it
  so, and a run that shows it — not the case file's own say-so; check the representation is reached, not
  declared);
- which it **cannot yet represent**, and the cheapest faithful change at the single owner (a verb row, a
  roster row, a predicate, an effect, a module input, a state field), written as a proposal;
- which needs are **wrongly stated** (a need no reading of the arc requires, or one two careful readers
  would take differently) and the resolution;
- which arcs and characters can be **simulated end to end** once the lane's changes land, with the
  execution artifact that would show it (a seeded run in which the arc's beats occur from persons' acts,
  not from a script — scripting drift is a failure of the test, not a way to pass it);
- which arcs depend on another lane's change first (name the dependency edge).

Append this as **§13. Provided arcs and characters — adjudication** at the end of your audit: a table
(case id · need (short) · hardness · represented today? · evidence · change required · owner lane ·
proposal file · gate), then a short ordered list of the arcs your lane can bring up soonest. The
holistic and instruction stages build the cross-lane sequence from these tables, so be exact about
dependency edges. Do not read the case files' statements as proof the engine behaves that way (§0.05);
they are the specification of what must be simulated.

## Added charge (Jordan, 2026-11-12): organise so that character capabilities are easy to define and map to RPG axioms

Jordan must be able to **define skills, abilities, aptitudes, traits and their kin, attach them to
characters, and have them correspond to RPG axioms** (what a capability is, what it adds to a roll or a
choice, how it is gained, lost, trained and opposed; the usual pool/threshold/advancement/tag
conventions of tabletop design) **without touching engine code**. Each subsystem, and the game as a
whole, should therefore be organised so that:

- every point at which a character's capability changes an outcome (a pool, an obstacle, a threshold, a
  ceiling, a candidate's score, an aperture, a cost) reads it from **one authoring surface** — a typed
  file code reads (§0.05), with one owner per fact — and not from a constant inside a module;
- a capability is defined **once** (its name, kind, scale, the axiom it implements, its inputs, its
  growth rule) and referenced by every subsystem that uses it, so a new skill can be added as data, and
  the verbs, contests, combats and choices that should respond to it do so by declaration;
- the mapping **capability → axiom → resolver input** is legible end to end: for any roll or choice, you
  can say which capabilities fed it, by which rule, and why.

Starting points in the tree (read, do not assume current): `proposals/2026-10-16-attribute-derivation*.md`,
`2026-10-16-attributes-from-scratch*.md`, `2026-10-16-character-template*.md`,
`2026-11-05-verb-attribute-map*.md`, `2026-11-05-attribute-rulings-*.md`,
`2026-10-24-character-layers-*.md`, `2026-10-07-character-sheet-spaces.md`, `engine/season/decision/sheet.py`,
the CR-20 (attributes) and CR-21 (cells) tests and code, `engine/season/verb_table.yaml`,
`write_matrix.yaml`, `rosters.yaml`, `modules/combat/` (attributes and thresholds, PC-14/15), and the
dice engine's inputs.

Append **§14. Capability authoring surface** to your audit: (a) every place your subsystem takes a
character capability as input, what it reads, and from where (cite code); (b) which of those reads
are data-driven today and which are hard-coded or doubled; (c) the target shape for your subsystem —
what a capability definition must say for your subsystem to use it, and the single file that should
carry it; (d) the RPG axioms your subsystem implements, named in the ordinary vocabulary of the
tradition, and any axiom it contradicts or lacks that a designer would expect; (e) proposals (files) for
the changes, ordered. Do not invent a second capability system: find the existing owner and say what
extends it. The holistic stage will merge the §14s into one authoring architecture, so state the
interface your subsystem needs rather than a private scheme.

## Full design descriptions (correction, 2026-11-12): read the subsystem's whole design set

The first dossiers listed only the design documents `CURRENT.md` names, which understates what the tree
holds. Each dossier now carries two further sections: **"FULL DESIGN DESCRIPTIONS for this subsystem"**
(every design document of the subsystem under the quarantined `.designs/systems/<subsystem>/`, with size
and Status line) and **"Cross-cutting design descriptions every lane reads"** (for example
`auto_manual_resolution_duality_v1.md`, `videogame_mode_spec.md`, `complete_systems_reference.md`,
`throughlines_complete.md`, `engine_atlas_v1.md`, `campaign_modes_v30.md`, `integration_proposal_v30.md`).
**Read them in full** (a document with `_index` and `_infill` siblings is one document in parts). They are
ARCHIVED-NOT-CANON: the source of intent, vocabulary and history, never the reason a behaviour is
correct (§0.05); where they disagree with code, the code governs and you say what the disagreement costs.
The design intent each Jordan statement below refers to is in those documents; do not audit against a
one-line summary of it.

For mass battle the design set is: `.designs/systems/mass_battle/reference/mass_battle_v30.md` (with
`_index`, `_infill`), `mass_battle_integration_v30.md`, `military_layer_v30.md` (with `_index`),
`mass_battle_flow_skeleton_v1.md`; with it `.designs/systems/combat/reference/scene_combat_design_v1.md`,
`.designs/systems/_architecture/reference/auto_manual_resolution_duality_v1.md` and `videogame_mode_spec.md`;
and the live material `proposals/2026-09-25-squad-engagement-*`, `2026-09-30-character-and-play-surface/08_mass_battle_units.md`,
`2026-10-29-army-phase5-design.md`, `proposals/multiunit_envelopment_plan.md`,
`proposals/mass_battle_fighting_withdrawal_v1.md`, `proposals/pc_formation_system.md`,
`proposals/weapon_physics_and_concentration_model.md`, `research/pre_firearms_formations`.

## Context and referents (Jordan, 2026-11-12): `.designs/` in full, and `.audit/` as the lesser corpus

Jordan directs that **`.designs/` be read, and `.audit/` too though with lesser weight, for context and
referents.** Both are hidden from default search; read them by path. `.designs/` is the archived design
documents (the whole tree: `systems/<subsystem>/`, `systems/_architecture/`, `systems/ui/`, `engine/`),
`.audit/` the surviving audit corpus (35 earlier audits; entry points in each dossier's "Surviving audit
corpus" section and `dossiers/99_cross_cutting.md`). Use them as follows:

- `.designs/`: intent, vocabulary, history and the **referents** the code and the cases cite (a term, a
  procedure, a table, a ruling's origin). Read the subsystem's whole set and the cross-cutting documents;
  go beyond your dossier's list wherever a referent leads. Full directory index: `dossiers/99_cross_cutting.md`.
- `.audit/`: what earlier audits found and **how they found it** (method, instruments, controls),
  which findings were fixed, which were never answered, and what a returning finding looks like. Weight:
  below `.designs/`, and below the working tree. An old finding is a lead, not a fact: re-verify it
  against the code before you rely on it or repeat it, and say when an old finding is now false.
- Both remain **ARCHIVED-NOT-CANON / hidden**: neither is the reason a behaviour is correct (§0.05); neither
  is loaded by anything (RULED: nothing outside `.audit/` loads anything inside it, and that is unchanged
  by reading); neither is a to-do list. Your audit may cite them as referents by path; the proposals you
  write must not make game code, a tool or a test read them.

## Design intent stated by Jordan, 2026-11-12: the detective and noir games that inspire fieldwork, and their bearing on social contests

Fieldwork is inspired by detective and noir games, and Jordan asks that this precedent be remembered in
the audits and **that its consequences for social contests, in evidence and in argument, be considered.**
Jordan gave no list; the games the tree itself names are (verify against the sources, and add any
detective or noir game the tree names that is not here): Disco Elysium, Return of the Obra Dinn, L.A.
Noire, Pentiment, Shadows of Doubt, the Ace Attorney / Phoenix Wright series, The Case of the Golden
Idol, Paradise Killer, Outer Wilds, Danganronpa, Her Story / Immortality, Heavy Rain, Blade Runner
(film and game material), the Frogwares Sherlock Holmes games. Sources: `research/game_precedent_suite/`
(`tables/R5_investigation_information.md`, `tutorials/T06_investigation.md`, `dispositions/D_T06.md`,
`tables/R4_combat_social_rpgs.md`, `tutorials/T05_social_rpgs.md`, `dispositions/D_T05.md`,
`tables/REPO_MENTIONS.md`, `THROUGHLINES.md`), `research/by_lane/FI_fieldwork_investigation.md` and
`SC_social_contest.md`, `research/valoria_game_precedent_companion_v1*.md`,
`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` (its player/character mapping
table), `.designs/systems/_architecture/reference/player_agency_v30.md` §1 (Disco Elysium, Pentiment),
`.designs/systems/fieldwork/reference/investigation_systems_v30.md` and `fieldwork_v30.md`,
`proposals/2026-10-16-verbs/…-12-lexicon-fieldwork-and-inquiry.md`.

What to extract and apply (the FI lane for the investigation side, the SC lane for the contest side,
CHAR for the voices and the knowledge a character brings, ARCS for the cases that turn on a reveal or a
trial):

- **Evidence as a typed, bindable object**: an accusation or argument that must *cite a held item* (L.A.
  Noire), an assertion as a typed structure a machine can grade (Golden Idol), a verification oracle that
  locks a conclusion only when its support is simultaneously right (Obra Dinn), knowledge as the only
  persistent state (Outer Wilds), traversal gated by what one knows (Her Story).
- **Argument as contradiction and rebuttal**: testimony set against evidence and found inconsistent
  (Ace Attorney cross-examination), argument-and-rebuttal as the structure of a trial (Danganronpa), an
  internal chorus of competing faculties arguing with the self (Disco Elysium), a community whose
  opinion of the investigator moves with every conversation and whose time is finite (Pentiment),
  procedural evidence chains and inference (Shadows of Doubt).
- **Questions for the code**: in the engine as built, can a contest (hearing, petition, plea, debate,
  negotiation, accusation) take evidence as a *typed input* (`Claim`, `proofs`, `reception`, the forged
  or concealed item), can an argument be *refuted by a held contradiction*, does the *strength of a case*
  come from what is held, witnessed and cited rather than from a free-floating skill roll, can an NPC
  build a case and be answered by another NPC, and what do falsehood, forgery and concealment do to a
  contest's outcome and to later trust? Where the answer is no, write the proposal at the single owner.
  Judge whether the precedent is understood or only named, and whether the nulls (problems no shipped
  game solves, `research/00_INDEX.md` §1 pt 4) are honestly marked.
- Where this intent conflicts with a ruled item (the proceedings ownership, ED-SC-0033..0039; the
  knowledge-model ruling), name the conflict and do not resolve it.

### Mass battle: the cell-based approach and the weapon-carry trade-off (Jordan, 2026-11-12; pay special attention)

The structure Jordan wants, which the MB lane judges the code and the design against with particular care:

- **Cell-based battlefield.** The battle is resolved on a grid of **cells**. An **army is a deployment of
  all its units in a formation** on that grid.
- **Nested structure.** Each **unit has its own subformation and its own troop types**: army → unit →
  subformation → troops (the existing code names `hierarchy/units.py`, `orderofbattle.py`,
  `troop_types/{registry,presets,recruitment}.py`, `geometry.py`, `perimeter.py`, `armies.py`; the design set
  is §A.3, §A.3b (the 25×25 cell grid), §A.12 in `mass_battle_v30.md`; the per-cell envelopment and
  front-fixer machinery is described in `proposals/multiunit_envelopment_plan.md`). Judge whether the
  hierarchy is real in the data model and the resolver (each level carrying its own formation, orders and
  state), or flattened at resolution time.
- **Mixed weapons per unit, with a cost.** **A unit can carry different weapons, but carrying more
  raises fatigue cost and lowers movement speed**, so that, for example, **a pike unit may also carry
  arming swords**: the benefit is being able to fight in either mode (pike formation against a charge,
  swords when the line closes or breaks), the price is a slower, more tiring unit. **Archers carry arming
swords too** (Jordan): the secondary melee weapon is a general loadout choice for any troop type, not a
pike-unit special case, so the rule must be one rule over any (troop type × primary weapon × secondary
weapon) and the ranged-to-melee switch (when archers' line is reached) must be a state change the
resolver handles with its cost. Judge: is weapon
  loadout a per-unit, per-troop-type datum; is "which weapon is in hand now" a state the resolver reads and
  an order or trigger changes; are the fatigue and speed penalties derived from the loadout by one rule
  (data, not constants in the module) and consistent with how the same penalty works for an individual
  character's kit in personal combat (CP-T03-03 kit, CP-T03-04 arms, `weapon_physics_and_concentration_model.md`);
  does the cost bite in play (fatigue over a long battle, pursuit, forced march, supply). Write the missing
  pieces as proposals, and state what a designer would edit to define a new troop type or loadout.
- **One path.** The cell-level battle that a player commands and the auto-resolved battle (Football
  Manager, Unicorn Overlord) must run the same cell-based resolver.

## Design intent stated by Jordan, 2026-11-12: personal combat

Personal combat is intended so that **each character can equip a weapon, armour and a suite of skills that
correspond to levers**, and can **choose a different intensity or approach of attack per phase** (for
example aggressive, normal, defensive). It must work in two modes from **one code path**:

1. **Moment by moment, as a duel** — the player (or an NPC chooser) selects the approach each phase and sees
   each exchange resolve.
2. **Inside turn-based grid combat in the manner of Final Fantasy Tactics / Tactics Ogre** — the "duel"
   sequence **resolves automatically**: the player simply selects an attack approach (aggressive, normal,
   defensive, …) and the engine executes a duel round on their behalf, returning the outcome to the grid.

Audit and design against this intent. It binds the PC lane (the module's inputs, levers, phases, the
approach choice surface, the automatic duel-round path, the grid seam; see the ratified grid-suspension
proposal `proposals/2026-10-07-grid-mode-suspension.md` and `engine/season/tests/test_rem31_grid_suspension.py`),
the CHAR and CORE lanes (equipment and skills as capability data, §14), the MB lane where a duel is
embedded in or arises from a mass engagement, and the instruction suite. Judge whether the present
`modules/combat/` already offers the two modes as one path (typed input, typed outcome, no held state),
and write the missing pieces as proposals. Where this intent conflicts with a ruled item, name the
conflict and do not resolve it.

## Added charge (Jordan, 2026-11-12): the NPC and AI-chooser design intent, in every audit

Every audit judges its subsystem's NPC-facing and chooser-facing surface against the design intent for
NPCs and the AI chooser. That intent is not restated here: it is what the tree records, and part of the
job is to read it, reconcile its sources, and say what it is. Sources, in order of weight (code is the
mechanism; prose is intent, §0.05):

- ruled and built: `engine/season/decision/` (`choose.py`, `options.py`, `questions.py`, `budget.py`,
  `sheet.py`), `queries/person_q.py`, `goals.yaml`, `npcs.yaml`, `cohorts.yaml`, the pursuit-basis worksheet
  (`proposals/2026-09-20-pursuit-basis-worksheet.yaml`, ED-IN-0261), the conviction split (ED-IN-0251),
  and the person-side rule (`holonic_ARCHITECTURE.md`, the NPC decision policy rows H-03/H-04/H-66/H-73/H-74
  in `engine/season/hole_register.yaml`);
- ratified or proposed design: `proposals/2026-09-16-conviction-decision-layer/`,
  `2026-09-17-governance-and-behaviour/`, `2026-09-30-character-and-play-surface/` (especially
  `03_play_surface`, `05_two_modes_of_one_bout`, `09_the_character_sheet`, `10_verbs_and_attributes`),
  `2026-09-12-emergent-narrative-primitives-v2/`, `2026-10-24-character-layers-*.md`,
  `2026-11-04-knowledge-model-build-plan.md`, B10-19's design-first clusters;
- intent and vocabulary only (`.designs/`, quarantined): `npc_behavior_v30.md` (ethical stance and
  resonance), `decision_policy_v1.md` (the precedence order Valoria decides by; DRAFT FOR RULING),
  `player_agency_v30.md`.

For each lane: (a) the NPC and chooser behaviours your subsystem needs (who decides, on what
information, with what temperament and conviction, at what budget, with what visible reasons); (b) whether
the same chooser serves a player-proxy and an NPC through one interface (the player and NPC are the same
kind of agent; the player's choices come from outside, the NPC's from the chooser); (c) where the
subsystem hard-codes an NPC rule instead of reading the chooser (scripting drift); (d) what an NPC needs
to be *characterful* in this subsystem (distinguishable choices from distinguishable people) and what
would make the choice legible afterwards (a reason trail the narrative can read); (e) what is missing, as
proposals. The CHAR lane owns the reconciliation of the sources above and states, in its audit, the intent
as it can be established from code plus ruling, marking what remains prose only; the other lanes cite that
statement rather than redo it. Where the sources disagree, the ruled and built wins; name the
disagreement.

## Design intent stated by Jordan, 2026-11-12: mass battle

Mass battle is **inspired by the Football Manager games and the Total War series**, and its referents
are **Ogre Battle, Unicorn Overlord, Football Manager, Total War and Mount & Blade II: Bannerlord**
(Jordan, 2026-11-12). Jordan gave no further text; read the references by what each is known for, in the
repo's research first (`research/game_precedent_suite/tables/R6_mass_battle_campaign.md`, `R2_warband_sandbox.md`,
`R4_combat_social_rpgs.md`, `tutorials/`, `dispositions/`, `REPO_MENTIONS.md`, the game-precedent companion,
`research/by_lane/MB_mass_battle.md`; mind the sourcing floor: fan-wiki figures for several of these were
bot-walled, so shapes are the durable finding, figures are leads), and test the subsystem against that.
In addition to the two below: from **Ogre Battle and Unicorn Overlord**, units are **small squads of named,
distinct characters** (classes, equipment, roles) placed on a formation grid, given standing tactical
**orders or priorities set in advance** (targeting, aggression, retreat conditions), and **resolved
automatically** while the player manages the composition and the orders; from **Bannerlord**, a
**campaign-scale party and army economy** (troops recruited, trained, tiered, upkept and lost; companions;
a commander whose own fighting and leadership matter) feeding **real-time field battles in which the player
may command, join or auto-resolve**, with the army's quality and morale derived from its individuals.

- from Football Manager: the player acts as a **manager** of a squad of individuals with roles, duties and
  instructions set before and adjusted during the match; a match engine that **resolves the contest
  automatically from those settings and the individuals' attributes**; the ability to watch, intervene,
  change tactics and substitute during play; and legible post-match analysis that explains why the result
  came out as it did;
- from Total War: **formations and units on a terrain-bearing battlefield**, with morale, routing,
  flanking, charges, fatigue and supply; a **campaign layer that feeds the battle and receives its
  result**; and the choice to **fight a battle or auto-resolve it**, with the two kept consistent.

Audit and design against this. It binds the MB lane (`modules/mass_battle/`: the orders and tactics
surface, individuals' roles and attributes feeding unit performance, the auto-resolve path versus the
playable battle as one code path, and the explanation of results), the PC lane (a duel inside a
mass engagement, the same duel-round path), CHAR and CORE (officers and soldiers as characters with
capability data, §14; the commander as an agent served by the chooser), SE and FA (the campaign layer:
supply, muster, territory, war), GO (what the player-facing layer must show), and the instruction
suite. Existing material to reconcile: the squad-engagement proposals
(`proposals/2026-09-25-squad-engagement-*`), `2026-09-30-character-and-play-surface/08_mass_battle_units.md`,
`2026-10-29-army-phase5-design.md`, `proposals/multiunit_envelopment_plan.md`,
`proposals/mass_battle_fighting_withdrawal_v1.md`, `research/pre_firearms_formations`,
`research/game_precedent_suite`. Judge whether the precedent has been **understood or only named** in
the code. Where this intent conflicts with a ruled item, name the conflict and do not resolve it.

## Ground rules (from `CLAUDE.md`; read it, these are the ones that bite here)

1. **Code is the mechanism; prose is reference** (§0.05). A design document is never the reason a
   behaviour is correct. Where design and code disagree, say which the game follows (the code) and what
   the disagreement costs.
2. **Name the falsifier** (§0.1 pt 3). A claim of "absent / dead / never fires" needs the run that would
   show presence; "works today" needs the *call site*; "as F says at :L" needs F opened at :L. A citation
   you have not opened is not a citation. `[UNVERIFIED]` marks what you did not check.
3. **A number without a control is not a measurement.** No balance claim from a single run.
4. **No new guards, no new apparatus, no new standing corpus** (§0.1 pt 5). Recommend an edit to the owner,
   or deletion. A forbidden guard may not reappear as a finding.
5. **`needs_jordan` is not a parking space** (§0). Before escalating anything, answer it in the order:
   superseded → irrelevant → answered by a design document → answered by precedent → answered by what
   makes sense for the architecture. Escalate only what survives all five, and say which two defensible
   options lead to materially different games.
6. **Rulings are not re-raised.** `HANDOFF.md` "Rulings — do not re-raise"; `(RULED)` marks in `CLAUDE.md`;
   the lane handoff's Standing orders.
7. **The request is the scope; one round, then stop** (§0). No second wave, no audit of your own fixes.
8. **The NERS definitions** are `CLAUDE.md` §0.06; the method is `skills/ners/SKILL.md`. Use the
   definitions for judging a design object; do not score E as an independent axis.
9. **All directions** (§0): top-down, bottom-up, vertical, diagonal, lateral, horizontal. A finding that
   holds from one direction only is narrowed, not established.
10. `.designs/` is ARCHIVED-NOT-CANON: readable for intent and vocabulary, never authority, never cited
    as the reason a behaviour is correct.
11. Spelling: Canadian English. Register: exact, no flattery, no promotion; hedge only where uncertainty
    is real.

## What "steelman, then adversarial" means in this suite

For each decision, structure or claim you assess: **(a)** state the strongest case for it, in the form its
best defender would make, grounded in code or ruling; **(b)** attack that case by the cheapest observation
that could break it; **(c)** record what survived. A finding that survives is stated with its evidence; a
steelman that fails is reported as such; a steelman you could not break is reported as holding, with the
attack you tried. Asymmetric skepticism is a bias in either direction.

## The measuring stick: a dynamic emergent narrative game

Judge every subsystem against what the nine requirements ask (`dossiers/00_NINE.md`; instrument
`python -m engine.season.harness.register --requirements`): propagation, consequence, scene-by-scene
ticking, strategic/management actions, all verbs built out, robust characters, memory/feeling/attitude,
non-omniscient and non-perfectly-rational characters, probabilistic event chains. Ask of each subsystem:
does it **generate** story when no player is watching (NERS-R's no-player half); do its outputs **feed**
the other subsystems' inputs; does a player's choice **change** what happens; does it **fail gracefully**
at its extremes (completeness).

## Reading discipline (the cost is reading; do the reading)

- **Read your dossier in full first** (`dossiers/NN_<SUB>.md`), then `dossiers/00_NINE.md`.
- **Read every code file the dossier lists for your subsystem, in full.** This is a comprehensive audit;
  sampling is a defect. Where a file is very large, read it in sections, but read it all. Open the
  call sites that consume its outputs.
- **Read every hole-register row the dossier lists for you in full** at its register line
  (`engine/season/hole_register.yaml`), not the 300-character excerpt. `closed?`/`open?` is a keyword
  hint only; verify each against the code. Rows listed as secondary: read their excerpt, open the full row
  only if it bears on a finding.
- **Read every workplan position and entry the dossier lists** at its line, the open batch card in
  `workplans/valoria_master_workplan_v11_part3.md`, and the lane handoff (`registers/handoffs/HANDOFF_<LANE>.md`).
- **Proposals and research**: read the Status line and head of each listed item; read in full the ones
  whose Status is RATIFIED or that bear on a finding. Historical proposals marked superseded or held back
  need only their Status line unless a finding depends on them.
- **Write early** (CLAUDE.md §10 pt 2): write the verdict and §1 of your file BEFORE you finish reading,
  then append. A reader that has read a long way and written nothing is failing. If you can no longer
  recall a citation, the claim without its line number beats the lost part.

## Research and precedent access (granted in full, by Jordan, 2026-11-12)

Every lane may read **all** of `research/` and any game-precedent or historical material in the tree, not
only the items its dossier lists (the dossier's classification is by keyword and misses some). Start from
`research/00_INDEX.md` (indexed by function, verb and primitive) and `research/by_lane/README.md` plus your
lane's file in `research/by_lane/`; then, as the subject warrants: `research/game_precedent_suite/`
(`THROUGHLINES.md`, the precedent tab, `dispositions/`), `research/valoria_game_precedent_companion_v1.md`
and its parts 2–8, `research/historical/`, `research/governance/`, `research/pre_firearms_formations/`,
`research/emergent_narrative_literature/`, `research/social_contest_procedures/`,
`research/rhetoric_oratory_contest/`, `research/provenance/`, the cross-scale and historical action
catalogues, and `proposals/2026-08-25-throughlines-and-precedent/`.
Rules for using it: research is tier 3 and informs design, it never settles it or supplies a canon name
(`research/00_INDEX.md` §1; `engine/season/rosters.yaml` source-precedence ruling); the sourcing floor
binds every number (fan-wiki figures are leads, shapes are the durable finding); convergence across
independent sources is the evidence that earns weight; **nulls are findings** (where no shipped game
solves a problem, say so rather than cite false comfort); a finding that reaches the game must reach it
through an owner code reads (§0.05). In §7 of your file, name the precedents you used and the ones you
tried that did not transfer.

## Executing things

You may run read-only instruments to observe behaviour (for example
`python -m engine.season.harness.register --requirements`, `... corpus_run`, `... aperture 3 0`,
`... strife 2 0`, `python tools/m1_acceptance.py --summary`), and short `python -c` probes, under these limits:

- **Do not run `pytest`** (the suite is a close step, §0.4) and do not run anything that writes a tracked
  file. Send any output file to the scratchpad path your prompt gives you. Before you finish, run
  `git status --short` and confirm the only change you made is your audit file.
- **Do not edit anything but your audit file.** Do not commit. No `Agent` fan-out unless a reading task
  is plainly separable and large; if you delegate, give the delegate a fixed-format request and verify
  what it returns.
- Seeds/hashes: `PYTHONHASHSEED=0` for any seeded run; say the seed and season count with each reading.

## The audit file — fixed layout

Write to `proposals/2026-11-12-subsystem-audit-suite/audits/NN_<SUB>_audit.md` (NN and SUB as your
dossier). Header: `# <SUB> — adversarial steelman audit`, then `## Status: REFERENCE (an audit; resolves nothing at runtime)`,
then `## Read at: <git short SHA of HEAD> (working tree)`.

0. **Verdict** — one paragraph, verdict in the first sentence: is this subsystem, as coded, a sound basis
   for a dynamic emergent narrative game, and what is the single largest obstacle.
1. **What it is, as coded** — modules, entry points, inputs/outputs, state it owns, how the season loop
   reaches it; with execution evidence (what you ran and what it showed).
2. **Steelman** — the strongest case for the present code and design, ranked by how much weight it bears.
3. **Adversarial findings** — ranked worst first. Each: `F-<SUB>-nn` · severity (blocks a requirement /
   degrades narrative / hygiene) · claim · evidence (`path:line`) · falsifier run and its outcome ·
   which of R-01..R-09 it touches · emergent-narrative consequence · minimal fix at the owner.
4. **Code matters** — ownership and duplication, dead or unreached code, contract/seam fidelity (against
   `references/module_contracts.yaml` and `architecture/meta/04_CODE_ARCHITECTURE.md`), determinism,
   test strength (can the assertion observe the failure it excludes?), performance where it matters.
5. **Design matters** — where intent, ruling and code agree and disagree; ruled items you accept as
   binding; design objects that fail a NERS cut (name what dies), or that survive one (name what the
   cut would lose); design that exists only as prose and is therefore not yet game.
6. **Hole-register and workplan disposition, and resolutions** — a table: item id · listed status ·
   verified status (closed / open / superseded / irrelevant / wrongly filed) · evidence · action; then a
   second table of every inconsistency, gap and unclear passage found, each with its **decided
   resolution**, the ladder step that decided it, and the proposal file that carries the edit. Apply the
   five-step ladder to anything flagged for Jordan.
7. **Research transfer** — which precedent or historical finding changes what to build, and which is
   decorative; nulls count (CLAUDE.md research index §1 pt 4).
8. **Best path forward** — an ordered list of builds/edits/deletions that move this subsystem toward a
   dynamic emergent narrative game. Each step: what changes, in which file, the gate that shows it
   worked (an execution artifact, §0.2), what it unblocks among R-01..R-09, and its cost class
   (edit / small build / design-first). Distinguish what is needed for the subsystem to run well alone
   from what is needed for it to compose.
9. **Playable standalone and integrated** — the standing requirement above, point by point: what exists
   today for this subsystem as a playable scenario (entry point, fixture, choice surface, outcome
   legibility, end condition, instrument), what is missing, whether the standalone and season-loop paths
   are one code path, whether the subsystem conforms to Layer 1 as a registered module, and the ordered
   work to close each gap. This is the section the instruction suite is built from.
10. **Interfaces** — what it consumes from and emits to each other subsystem, and which of those edges
    are real (executed) versus designed.
11. **Survivors for Jordan** — only items that survive the five-step ladder, each with the two defensible
    options and how they differ as games. May be empty; say so.
12. **Evidence log** — each command or probe run, seed, outcome.

Length follows the subject; a thorough audit of a large subsystem is long. Do not pad, do not recap.

## Return to the orchestrator

A receipt of at most 200 words: the file path, the verdict sentence, the five findings that matter most
(id and a clause each), anything you could not read (`[SKIPPED: file — what, why]`), and any item you
believe needs the orchestrator's attention. Not the audit itself.

## Standing charge: eras, regimes, strife, endings, momentum and cascades (Jordan, 2026-11-12)

*"Have Fable extend author and plan how to improve upon eras regimes and strife alongside methods to make the plot legible to player. Work to improve era endings (like death of monarch, change of rule, civil war breaks out, etc) and momentum mechanisms. Cascade effects and compounding are real."* Eras, regimes and strife are three distinct things. Carried by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` and `proposals/30_WR_*`, `30_GO_*`. Every later lane, closure and the v12 plan treats era endings, momentum, compounding (bounded, drawn, never triggered) and player legibility as in scope.

## Standing charge: every recommendation carries instructions to code it (Jordan, 2026-11-12)

*"Remember that all Fable work, proposals and recommendations will require instructions on how to code / implement in game so that it can be passed off to workplan v12."* A proposal or recommendation is not finished until it carries, in the form a later `/methodology-execute` batch can follow without re-deriving anything: the exact files and symbols to create or edit (the single owner), the order of edits, the data rows or schema, the call sites to change, the tests to add or change (named), the gate (an execution artifact with its expected reading), the falsifier and its control, the declared hash movers, the dependencies on other proposals, what lands it and at what cost class and model tier. A recommendation that is a design only, a finding with no edit, or a plan to "decide later" is marked INCOMPLETE and returned to its author or completed by a closure lane. The instructions are written for the game's code (`engine/season/`, `modules/`, registries), not for prose.
