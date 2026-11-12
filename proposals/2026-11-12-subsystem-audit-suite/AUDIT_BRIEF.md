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

Mass battle is **inspired by the Football Manager games and the Total War series.** Jordan gave no
further text; read the two references by what each is known for, and test the subsystem against that:

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
