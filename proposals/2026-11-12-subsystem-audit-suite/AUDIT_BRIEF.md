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
