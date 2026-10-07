# Valoria — TTRPG / videogame design repo

The **design source of truth** for **Valoria** (`jordanelias/ttrpg`), a Godot videogame fusing
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory, faction politics, domain actions). **There is no GM — the engine resolves everything.**
Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are* the game's layers.

**Implementation repo:** `jordanelias/valoria-game` (separate clone, CI, compile ratchet). ⚠️ **Its
Godot engine version is UNRESOLVED and nothing here may assert one** — its `project.godot` and CI pin
one version, `godot/` here documents another. Awaiting a ruling; do not settle it by editing a document.

**This file holds rules only, and POINTERS, never figures** (§1). Reasoning and history live in
`CLAUDE_RATIONALE.md` — reference, never binding, not required reading; the story goes there, the rule
here. Open it when a rule here looks arbitrary and you are about to change it. **The cap is 640 lines
(`wc -l CLAUDE.md`), and that number is the cap.** Past it, cut something; if the rules genuinely no longer fit, raise the cap in
the same commit and say what you added. **(RULED)** marks a rule as Jordan's, not agent-revisable.

**THE LAYERS (RULED by Jordan) — the canonical definition of a GOVERNANCE layer (how work is
done). No other governance scheme may be spelled "Layer".** Not a licence to sweep:
`godot/godot_architecture_specification.md`'s runtime layers and `systems/ui/`'s "Layer 3" UI tier are
unrelated senses and stay.

| | | binds |
|---|---|---|
| **Layer 0** | **this file**, `CURRENT.md`, `HANDOFF.md`, and the user-level `CLAUDE.md` where one is loaded | the AGENT — how a session works, what may be built, what counts as done |
| **Layer 1** | `architecture/` (RATIFIED, ED-IN-0204) | how code is written |
| **Layer 1 scripts** | guards derived from Layer 1 | Layer 2 |
| **Layer 2** | the game code | the game |

**There is no Layer -1.** Needing one means Layer 0 was written wrong: EDIT THIS FILE, never build a
level beneath it. **Layer 0 binds a reader, not a program**; §0.05's asymmetry — prose non-binding for
GAME MECHANISM, binding as AGENT INSTRUCTION — stops the recursion. The `subject:` field of
`references/ci_checks_registry.yaml` counts the opposite way on a different axis — never call it "layer".

**Where the user-level file and this one disagree**, this file governs the work — lanes, cadence, gates,
evidence standards, commit shape, what counts as done — and the user file governs the register a result
is reported in. Name the conflict; never silently rank them.

---

## 0. How we work (method, not location)

- **Plan before you touch the tree.** Establish currency (`/currency`, §1), read the subsystem head and
  its `## Status:` line, then state what changes, in what order, and how you will verify — *before* the
  first edit. Anything ambiguous or spanning lanes: get the plan approved or ask a focused question.
- **Build bottom-up from primitives.** Compose on the single-owner primitive; never re-implement a rule
  that already lives once (§8). New tooling reuses the registries and `engine/substrate/`'s leaf readers
  (`descriptors`, `composition`, `names`). ⚠ **The Key substrate is RETIRED (ED-IN-0232, RULED:
  *"anything key-based gets retired"*)** — `keys.py`, the echo transport and the emit/consume interface
  are gone; build nothing on them. Special-casing an
  entity or outcome is **scripting drift** — stop.
- **Adversarial pass at every stage that gates a result.** After you draft canon, a number or a fix,
  *try to break it*: verify provenance by hand against the cited `PP-NNN`/`ED-NNN` (PP provenance is
  unvalidated — `tools/validate_ed_citations.py` covers ED only), run the relevant `tools/` validator,
  and for a judgment call put a structurally independent critic on it (§10). Never report a result you
  have not attacked. "Every stage" governs WHAT you attack — provenance, setup, falsifier, with the
  narrowest instrument that can observe the failure — never HOW OFTEN you re-run the gate (§0.4).
  - **The pass is a STAGE, not a DELIVERABLE.** Its output is edits to the thing under review plus at
    most one paragraph in the commit message. No directory, no document; at most one ledger row, only
    if it needs a human decision (`needs_jordan: true`). **A finding that needs no ruling is fixed in
    this commit or dropped.**
  - **One exception (RULED):** a **TERMINAL pass whose verdict is the thing asked for** may record it
    where its subject lives — a section of the target, or a sibling file in the target's directory;
    never a standing corpus, a new top-level tree or `.audit/`. **The test: DOES THIS DOCUMENT CREATE
    WORK FOR A FUTURE SESSION?** If yes, drop it. If it only explains a judgment about an artifact that
    ALREADY EXISTS, it is reference and it may stay. *"X is wrong and here is why"* passes; *"and
    therefore someone should build Y"* is a queue and fails. **The record dies when its subject
    dies.** If the exception becomes the general case, delete it and restore the flat ban.
  - **`needs_jordan` IS NOT A PARKING SPACE** (RULED): *"I don't believe that I need to be involved in
    the vast majority of pending decisions. Those decisions should be answerable as superseded or
    irrelevant, by our design documents, by precedents, or by whatever makes most sense for code
    architecture."* Before flagging a row, or leaving one flagged, ANSWER it in this order:
    1. **Superseded** — a later ruling, commit or head decided it. Cite the successor; close it.
    2. **Irrelevant** — its subject was retired or never built. Close it; say what died.
    3. **Answered by a design document** — `CURRENT.md`'s head, the subsystem's `## Status:`, the spec.
    4. **Answered by precedent** — the tree decided this shape elsewhere. Follow it; name it.
    5. **Answered by what makes sense for the architecture** — where 1–4 are silent but one option is
       clearly right for the code, TAKE IT and record the reasoning.

    **Escalate only what survives all five:** a live design choice where two defensible options lead to
    materially different games, or where the answer would overwrite ratified canon. ⚠ **This cuts BOTH
    ways** — clearing the standing queue is session work.
- **Max effort on the deliverable named by the current milestone** (done = **the behaviour executes**,
  §0.2): the most thorough path *that deliverable* warrants, verified over plausible, finished rather
  than sampled. **Work is this session's work if Jordan asked for it this session, or it traces to an
  open M1 juncture; nothing else is.** If something broken blocks the milestone, **fix it minimally,
  without adding a guard.** Tier *down* deliberately and per-task (§10), never on judgment nodes. Never
  restore *exhaustive* here, nor read this as "prefer the harder-but-correct fix".
- **Close the loop, honestly — and close it ONCE.** `/close` has the sequence: the full suite, the
  lane's validator, the `[scope]` commit citing the `PP/ED`, next actions in your lane's
  `HANDOFF_<LANE>.md`. Mid-session, run only the file covering your edit (§0.4). If a check failed or
  a step was skipped, say so — an unverified green is worse than a verified red. No banner (§0.3).

### 0.05 CODE IS THE MECHANISM. PROSE IS REFERENCE.

Jordan: *"whatever mechanisms we have that rely on prose are worthless. we rely on code ONLY for the game
work. our design documents in .MD are reference and information only."*

| a claim of the form… | is a mechanism? |
|---|---|
| a `## Status: RATIFIED` line on a `.md` | **no** — reference |
| a design doc stating a formula, threshold or band | **no** — the code is the formula |
| a `.md` describing what a module emits or consumes | **no** — reference |
| a YAML/JSON registry **that code reads at runtime** | **yes** |
| an exporter with a blocking `--check` round-trip | **yes** |
| a test that executes the behaviour | **yes** |
| a doc-derived count (`tools/m1_acceptance.py`'s aggregate row) | **no** — and it says so itself |

- **A design document may not be cited as the reason a behaviour is correct** — only for intent, history
  and vocabulary. If canon and code disagree, decide and then CHANGE THE CODE.
- **A FACT the engine uses must live where code reads it** — a typed artifact under
  `engine/engine_params/` behind an exporter, or a single Python owner. Constants still inside
  `systems/` are the migration backlog (live count: `python tools/export_sim_params.py --build`).
- ⚠ **A term, a roster, a closed set and a bound are facts exactly as a number is** (Jordan: *"all
  definitions/terms/etc need to come from code, never prose"*). Four clauses, one rule:
  1. **A `.md` is NEVER the authored head of a fact code reads.** The head is YAML/JSON under
     `references/`, or a single Python owner.
  2. **`systems/**/*.md` is design intent ONLY** — never an input to a tool, exporter, gate or registry.
  3. **Edit the OWNER and re-derive; never hand-edit downstream, never keep a second copy.** When two
     live surfaces disagree, `engine/season/` decides which reading wins; write it at the owner.
  4. **Scoped to GAME facts.** `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md` and
     `references/restructure_ledger.md` are process surfaces a program legitimately reads.

  §5, §6 and §8 are instances of this rule. ⚠ **A fact whose chain you cannot name is orphaned or
  hand-transcribed** (`fac.intel`: ruled bounds, reachable by nothing). **NO TREE-WIDE GUARD IS
  LICENSED** (§0.1 pt 5); licensed instead: the exporter's `--check` per chain, the loader's refusal per
  data family, and reading the chain before you delete or migrate.
- **This does NOT demote `CLAUDE.md`, `CURRENT.md` or `HANDOFF.md`**, and **does not license deleting
  design docs.** They stay as reference; what changes is what may be treated as *binding*.

**The test:** *if this document were deleted, would the game behave differently?* If no, it is
reference. If yes, the mechanism is in the wrong place.

### 0.06 NERS — the four criteria (Jordan's definitions, verbatim)

The canonical home of the NERS definitions — reference (§0.05): NERS judges a design, resolves nothing.

```
ALL DIRECTIONS  top-down · bottom-up · vertical · diagonal · lateral · horizontal
```

> **NECESSARY (N)** — unable to be removed without **worsening the gameplay experience**; makes the game
> more **robust and elegant**; **smooth integration** with existing play; supports a **cohesive gameplay
> experience from all directions**.
>
> **ELEGANT (E)** — **logically simple**; clear approach; **no unnecessary overhead**; easy to
> understand; **allows the player to intuit complex outcomes from simple choices**.
>
> **ROBUST (R)** — allows the player to think **strategically**; allows **customization** of characters /
> settlements / factions; allows **creativity and variety in approach and resolution**; makes players
> feel **important to** the game world; makes players feel like they **impact** the game world; provides
> **emergent and compelling narrative hooks and scenarios WITHOUT player involvement**; mechanics are
> **fully formed, error-free, and complete** opportunities for engaging the player.
>
> **SMOOTH (S)** — integrates **cleanly without friction points**; mechanics **interact cleanly with
> other interdependent mechanics**; **zooms out and in well across scales of play**; **transitions and
> sequences cleanly** between mechanical systems; **pauses correctly** when other systems or scales are
> called for; **calculations consistent in methodology** with other mechanics; integrates into a
> **unified mechanical approach**.

**Read the definitions, not the acronym:**

- **N is defined THROUGH the other three**, tested from all six directions; an N-line holding in exactly
  one direction is *narrowed*, not passing.
- **E is legibility, not tidiness** — *"no unnecessary overhead"* and *"intuit complex outcomes"* are
  two tests. ⚠ **Never score E as an independent axis** (amputation satisfies it alone): score it
  **last, as a ratio against what N and R found**.
- **R has a half with no player in it** (the world generates drama when nobody is watching) **and
  includes completeness**: a mechanism breaking at its extremes fails.
- **S carries two tests the shorthand drops:** *pauses correctly*, and *calculations consistent in
  methodology* with siblings — two ladders for one quantity is an S defect even when each is correct.

**The method** lives in **`skills/ners/SKILL.md`**, its single owner; this subsection owns the
**definitions**. Do not restate the method here or the definitions there.

### 0.1 Measurement discipline — five checks, each with an artifact (ED-MB-0042)

1. **The hazard is read/write asymmetry, not "change".** When a getter starts computing from a new
   source (`eff_morale` from cells) while setters still write the old one (`.morale`), every writer
   silently becomes a no-op. Grep the field's **assignments**, not its readers, and ship a guard failing
   on a *new* bare assignment. Template: `tests/valoria/test_morale_write_sweep.py` (its `_CELL_OWNED`
   registry is field-parameterized).
2. **An assertion must be able to observe the failure it excludes.** `pytest.approx` on an *exactness*
   claim is not a weak test but an absent one. A loop that asserts conditionally must assert that it
   asserted (`assert checked >= N`).
3. **Name the falsifier, or you have not attacked the result.** A result claim carries, in the same
   commit, the test that would have shown it wrong and that test's outcome. A result claim is wider than
   a number, and **the claim and its support are different objects; check the support.**

   | claiming | observe this first |
   |---|---|
   | **"X is absent / dead / never fires"** | RUN the thing that would show presence. An absence is the cheapest claim to make and the hardest to see wrong. |
   | **"X works today"** | Open the CALL SITE, not the declaration. A roster existing is not a roster being used. |
   | **"as `F` says at `:L`"** | Open `F` at `:L`. A citation you have not opened is not a citation. |
   | **"I ran it / I could not reproduce it"** | Check the RUN HAPPENED, not that the command exited. A generator that no-ops, a test that skips, a rebuild that writes nothing each return 0. Diff the artifact, or assert the thing changed. |

   **NO GUARD MAY BE BUILT FOR THIS** — a reader's discipline, excluded by pt 5's predicate.
4. **A number without a control is not a measurement — in either direction.** Asymmetric skepticism is a
   bias, not a defence; absence of one failure mode is not presence of correctness.
5. **Sweep pattern defects; fix one-off defects — but a guard must EARN its existence.** A pattern
   defect's signature is *the broken code was correct when written and stopped working because something
   else changed*: then one owner for the operation, every site routed through it, and a guard failing on
   recurrence — **subject to the predicate:**

   > *A pattern defect earns a guard only if the defective artifact is load-bearing on **the game** or on
   > **a Jordan decision** — its output crosses into the engine, the exported params, the port, or the
   > `needs_jordan` queue. A pattern defect in an artifact load-bearing only on this repository's
   > process is **not** evidence the artifact needs a guard; it is evidence **the artifact can be wrong
   > without cost. Delete it, or accept the defect and write nothing.***

   **Load-bearing ≠ "about the game".** KEPT: `test_morale_write_sweep.py`, the golden-modes and
   sim-fabrication CI checks, `tools/export_engine_params.py`'s round-trip `--check`, a compile gate.
   FORBIDDEN: a guard whose subject is another guard, a grader over the gate list, a test that the
   blocking tier's membership is honest. ⚠ A forbidden guard may not reappear as **a finding** (§0).
   Sweep only what the current task is load-bearing on; otherwise fix it here or drop it.

**`pytest tests/valoria` is a SHIPPING gate, not a belief gate**; behaviour changes include default flips
and golden re-records. **Targeted-green is not validation** — tests you wrote for the thing you built
encode your model of it, not the system.

### 0.2 DONE MEANS IT RUNS (RULED)

**A juncture is done when the behaviour EXECUTES — not when a document exists with a `## Status:`
line.** This is the one claim here a session **cannot satisfy by writing**.

| | old `done` | new `done` |
|---|---|---|
| M1 juncture | a design doc exists and is `RATIFIED` | the behaviour runs, and something ran it |
| checked by | reading a `## Status:` line | an execution artifact — a run, a log, a hash, a test result |
| satisfiable by writing? | **yes** | **no** |

- `python tools/m1_acceptance.py --summary` is the instrument; its rows are falsifiable and it refuses to
  guess. ⚠ **It is not uniformly execution-bound:** some rows execute the engine (a seeded 1-season probe
  of **`engine/season/`, the HEAD**, and a same-seed `World.content_hash()` comparison), but **the row
  counting THE NINE met reads `status:` strings in `engine/season/requirements.yaml`** (validated by
  `register --requirements`, still not execution). It declares itself DOC-DERIVED.
- ⚠ **`mc_v18` is DEPRECATED IN PLACE.** No game code imports it; do not delete it — tests in CI's
  blocking `sim-regression` job do. `tests/valoria/test_mc_v18_is_deprecated.py`'s `ALLOWED_IMPORTERS`
  is the shrink-only live list; it fails on a NEW importer and on a stale roster line. **Nothing new is
  built there.**
- For a juncture with running code, "authoring the design doc" is **not** the deliverable: verify the
  code against the sim and record the contract; the doc may follow verified behaviour.
- **A position done in code and open in its plan is a PLAN defect, not a work item.**

### 0.3 No SessionStart banner (RULED)

**A SessionStart hook that PRINTS is the regression; one that is silent is not. Do not build a
replacement banner.** `tools/session_provision.py` is the allowed shape: it installs the four packages
§8 documents and writes zero bytes to stdout. Retiring the banner is a closed experiment, not one to
re-run from a hunch; reasoning in `CLAUDE_RATIONALE.md` §0.3.

### 0.4 VERIFICATION CADENCE — the suite is a CLOSE step, not an inner loop (RULED)

Timings: `CLAUDE_RATIONALE.md` §0.4 — re-measure rather than quote them.

1. **The full suite runs AT MOST once per commit, and only when it can observe something CI will not
   (RULED).**
   CI runs it on every push. Name what a local run would catch first; a diff of prose, ledgers, skills
   or links runs only the test files that read what it touched (`grep -rl <path> tests/`).
2. **Mid-session, run only the file covering what you touched.** If you cannot name it, find it — that
   costs seconds.
3. **Never re-run to re-confirm a green you already hold.**
4. **A red close run re-runs the FAILING FILE ONLY while you fix it.** The full suite comes back once,
   when you believe you are done. Red is not a licence to loop the gate.
5. **`tools/valoria_local.py --staged` does not run pytest** (local-green ≠ CI-green). It is cheap; run
   it freely. The expensive thing is pytest, and only pytest.

**This governs EVERY pytest gate** — `engine/season/tests` and `engine/tests` too: at the close, once,
only the ones your change can reach. ⚠ **Learn your container's known-red BEFORE you debug it:** a
**shallow** checkout cannot reach the commits `FORK:` rows name, so `tests/valoria/test_forked_status.py`
fails on arrival — the clone, not `main`; `cat .git/shallow` settles it. **NO GUARD MAY BE BUILT FOR
THIS SUBSECTION** (§0.1 pt 5).

---

## 1. Read these first (currency)

The live canonical surface is **Generation v40**. `/currency` runs this. Strict priority order:

1. **`CURRENT.md`** — the **single index** of the live canonical head per subsystem, and the authority
   whenever you are unsure a doc is current. **It and every handoff are POINTER INDEXES** (RULED): a
   head, an id, a path, a command — never a count, figure, ruling text or dated narrative (those go in
   commits and `_history` files).
2. **`HANDOFF.md`** — the **continuity index**, pointing to `registers/handoffs/HANDOFF_<LANE>.md` (an
   Open table and a Standing-orders table per lane). **Nothing reads either automatically — read root
   `HANDOFF.md` AND your lane's file yourself.**
3. **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable
   indices. The `canonical_sha__*` pins are verified against the **working tree** by
   `tools/freshness_gate.py` (blocking in CI, report-only locally); run it rather than trusting a pin.

**Ignore for currency:** `README.md` (outdated pointers). There is no session log or checkpoint to
resume from. There is no `deprecated/` tree — **retiring something means deleting it and writing a
`FORK:` row** in `references/restructure_ledger.md`. Do not recreate the directory.

⚠ **ONE EXCEPTION (ED-IN-0231): `.designs/` — QUARANTINED, not retired:** *kept, readable and
resolvable*, moved out of the code trees and default search path so it is not read as canon. It holds
the design documents
formerly under `systems/*/reference/` and the root of `engine/`, each bannered `ARCHIVED-NOT-CANON` with
its original path. **The leading dot is the mechanism** — ripgrep and `glob.glob` skip it unless asked;
`os.walk`, `Path.rglob` and `git ls-files` do not. **Do not add to it** (new design work goes to
`proposals/`), **do not point at it** (`CURRENT.md` names those documents by bare filename), **do not
read it as authority.** Not a licence for a second such tree.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly. **Do not re-fetch
  from the GitHub API**; the checkout is fresher than any cache or memory.
- **Commit with git.** Stage your own files explicitly. On `main`, branch first. Format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design`.
  Cite `PP-NNN` / `ED-NNN` when applicable.
- **Subject line ≤ 72 characters; detail in the body.** The subject is an index entry, not an abstract.
  Check: `git log --format=%s -30 | awk '{print length}'`. A reader's discipline, like §0.4.
- **Continuity = git history + `HANDOFF.md`/the lane file.** Pausing mid-task, capture next actions
  there; a commit *is* the session close. ⚠ In a **shallow** checkout, the archaeology is the ED ledgers
  under `registers/`, not `git log`.
- **Merging a PR ratifies its PROPOSED contents by default (ED-1094).** If a PR lands a doc, doctrine or
  ledger entry tagged `PROPOSED`/`provisional`, Jordan's review-and-merge *is* the ratification — flip
  the `## Status:` line, the ledger `status`/`needs_jordan` fields and `CURRENT.md` **in that same
  merge**. **The exception must be loud:** anything needing separate sign-off is called out in the PR
  body as *held back*. Never bundle a hard design call into a routine PR and rely on a follow-up.
- **ONE ACTIVE PLAN PER LANE (RULED: *"Retire ALL plans … We are allowed to have one active plan per
  lane."*)**, under `workplans/`, naming its lane; `CURRENT.md` names it. A lane's plan may **carve
  out** a scoped workplan **by name** (RULED): the carve-out owns its items alone; the plan names it,
  schedules none of them; no item sits in both. **Adopting a plan RETIRES what it supersedes in the same
  commit** — delete + exact-file `FORK:` row (§1), carrying forward any content the new plan still
  needs; "superseded but kept on disk" is not a state. A shallow clone runs `git fetch --unshallow` to
  write the `FORK:` row; it does not defer. Finished positions leave the plan; the commit is their
  record. A reader's discipline (§0.1 pt 5).

---

## 3. Repository map

**Do not read a description of the tree — look at it.** `ls`, `find` and `git ls-files` say what exists;
`CURRENT.md` says which head is canonical; `references/restructure_ledger.md`, via `tools/pathres.py`,
says where an old path went. Only what those cannot tell you:

- **`systems/`** — design source of truth for `combat`, `social_contest` and `mass_battle` (retained by
  ED-IN-0204). **One subsystem = one folder = one ID lane = one `CURRENT.md` row = one
  `HANDOFF_<LANE>.md`.** Oracle scripts live in `sim/`, imported as `systems.<sub>.sim.*`. ⚠ **`systems/`
  HOLDS NO `.md` AT ALL** — its design documents are in `.designs/systems/<sub>/`;
  `tools/ci_design_prose_quarantine.py` is blocking and the invariant is **zero, not a ratchet**.
- **`engine/`** — the executable model (substrate leaf readers, autoload hub, cross-scale, campaign
  driver, `engine/engine_params/` typed exports, `engine/tests/` = CI job `sim-regression`). **It names
  no subsystem by import**: seams resolve through `engine/substrate/composition.py` (`engine/` names a
  ROLE, `references/module_contracts.yaml` the MODULE). Two `sys.path` seams into `systems/` are in
  `PATH_SEAM_ALLOWED`, **shrink-only**; the execution artifact is
  `test_importing_every_engine_module_pulls_in_no_subsystem` (subprocess import, matching on FILE PATH).
  ⚠️ **Acyclic is not independence:** the engine still depends on subsystems, resolved by string.
- **`engine/season/`** — **Layer 2, the game code**: the season loop plus the registries it opens **at
  runtime**. ⚠ **IT RUNS AND IT IS NOT YET A GAME** — read
  `python -m engine.season.harness.register --requirements` (against `engine/season/requirements.yaml`)
  before citing it as done. `engine/season/hole_register.yaml` is read by the corpus grader, not the
  loop.
- **`architecture/`** — **Layer 1.** Reference for game mechanism (§0.05), binding as agent instruction,
  resolving nothing at runtime. Exempt from the size WARNING only.
- **`canon/`** — foundations **P-01..P-15**, timeline, constraints, amendments; world truth only.
- **`registers/`** — process ledgers and `registers/handoffs/`. **All ledger files are authoritative —
  read all of them.** **Never edit** the frozen ED fragments in `registers/archive/`:
  `tools/validate_ed_citations.py` reads them; deleting one makes valid citations read as fabricated.
- **`tools/`** — all CI checks, validators, generators; every rule lives once (§8). Check
  `references/ci_checks_registry.yaml` before assuming a module has an automated caller.
- **`tests/`** — `tests/valoria/` is the pytest unit suite, the only executable tests here; its
  narrative `.md` is **prose, not executable spec**. `tests/sim/` is unrelated to the retired `sim/`.
- **`.audit/`** — the surviving audit corpus, **HIDDEN** like `.designs/`. A **rename** of `audit/`, not
  a mirror (`.audit/<x>`, where `.designs/` prepends); `tools/ci_claim_provenance_check.py`'s
  `QUARANTINE_MIRRORS` is the one place that difference is written down. Retired **as a category**
  (§0): do not add to it. **Nothing outside it loads anything inside it** (RULED) — keep it that way.
- **`proposals/`** — unratified proposals, surfaced BY LOCATION. ⚠ **Almost none of it is RATIFIED**
  (`git ls-files proposals | wc -l`; `git grep -l '^## Status:.*RATIFIED' -- proposals`). Before
  starting a new directory here, answer what it changes in `engine/season/`.
- **`godot/`** — see §6. **`workplans/`** — at most one active plan per lane (§2).

**Dissolved — never recreate:** `designs/`, `sim/`, `arcs/`, `engine/params/`,
`references/values_master.yaml`. ⚠ **`.designs/` is NOT a resurrection of `designs/`.** Everything
removed is at its fork ref; every old path resolves through `references/restructure_ledger.md`.

## 4. Conventions

- **Long documents (RULED): sequential parts (`_part2`, `_part3`, … in reading order), not
  index+infill.** The `*_index.md` + `*_infill.md` pair is **RETIRED as a default**; existing pairs are
  grandfathered.
  Nothing enforces either half — not the pair rule, not a length; **when it splits is your judgment**
  (can a reader work with it?). ⚠ The **explicit per-file** caps in `references/atomization_rules.yaml`
  are untouched and several ARE blocking — read the rule for the file you are editing.
- **Versioning ≠ currency.** Three orthogonal axes coexist with **no reliable mapping**: filename `_v30`,
  in-file `## Version: vN.N`, and the `v40` generation marker. **Only `CURRENT.md` and a head's
  `## Status:` line can tell you what is current** (`_v30` is nominally current, yet the live combat
  head is `systems/combat/combat_engine_v1/`, with no suffix).
- **ID systems.** `PP-NNN` patches (`registers/patch_register_active.yaml`), `ED-NNN` editorial items
  (`registers/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks.
  `references/id_reservations.yaml` is the allocation source of truth — read `next_free`, allocate, bump,
  co-commit; never max+1. ⚠ **Discipline, not a lock:** renumbering does not escape a collision, since
  every live session renumbers to the same `next_free`. If another session may allocate in your lane,
  land the `next_free` bump on `main` before anything cites the number (narrows the window, does not
  close it). The structural fix, `wiring_status.auto_allocation`, is PARKED in the same file.
  **Two ED formats coexist:** the flat `ED-NNNN` sequence is **FROZEN** (no new allocations, permanently
  valid for existing citations); all NEW EDs use lane-tagged `ED-<LANE>-NNNN`, zero-padded to 4 digits.
  Lanes:
  `MB` mass battle, `PC` personal combat, `FI` field investigation, `SC` social contest,
  `FA` faction actions, `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements.
  Both resolve through `tools/validate_ed_citations.py` and `tools/currency_consistency_check.py`
  forever; no retrofit. **The ledger is lane-split:** `ED-<LANE>-NNNN` lives in
  `registers/editorial_ledger_<lane>.jsonl` (lowercase); the main file and every lane file are
  authoritative — read all. **Lane-scoping** (convention, not CI-enforced): declare your lane via the
  ids you allocate; keep commits/PRs to that lane's files, except cross-cutting `IN` work.
- **Word choice: idempotent in meaning, idiomatic in choosing (RULED, ED-IN-0179)** — process
  vocabulary as much as design terms. A reader with no memory of this repo must land on your meaning,
  and the word must be used that way *outside* this repo; if either fails, use the ordinary word.
  **Coin nothing a plain word already covers** (`retire`, not `evacuate`). **Define new coinage in BOTH prose AND where it is
  invoked**: the tool's `role:` line in `references/ci_checks_registry.yaml`, the rule or flag string,
  the module docstring and `--help`, `.claude/settings.json` hook commands and CI job names. No retrofit.
- **Naming gate.** The canonical name is **Solmund** — never **Galbados** (deprecated). Enforced by
  `tools/ci_naming_check.py` in CI and pre-commit, plus `tools/hook_naming_guard.py` at edit time, which
  `sys.exit(2)`s — it BLOCKS. Definition naming is centralized in `references/names_index.yaml`.

---

## 5. Data → Godot pipeline

**Rule: never take a number for the engine or the port out of prose.** A value the engine uses lives in a
typed artifact under `engine/engine_params/` behind an exporter with a blocking `--check` round-trip, or
in a single Python owner. `engine/engine_params/params_tables.yaml` is a frozen, no-longer-regenerable,
ungated capture of prose tables — **reference**, and it can hold pre-ruling values (its degree bands are
superseded by `degree_from_net` in `engine/autoload/dice_engine.py`). **Check the code first, every
time.** Until the typed layer covers numeric operands and structured formulas, every value crossing into
Godot is hand-transcribed — live drift risk — and do not bind Godot resource fields to descriptor keys
the registry still marks IN FLUX.

## 6. Godot port pipeline

**Rule: a port never corrects its oracle in place (ED-1050).** If port and Python oracle disagree, fix
canon via the ledger and re-export — never hand-edit a value into the `.gd` side. `godot/skeleton/`
covers a single module, does not compile, and `extends` a spine defined nowhere in the corpus: **never
present it as a runnable head-start.**

`godot/godot_conversion_strategy_v1.md` is the governing spec — **PROPOSED, Jordan-vetoable throughout**,
with an open register and unexecuted Gate-0 preconditions. `references/module_contracts.yaml` shows which
modules have `doc: null` (including `engine_clock`, the temporal spine) and which resolvers are
`[ASSUMPTION]`-grade; porting beyond the combat slice is blocked on authoring canon first, starting with
`engine_clock`. The older `godot/` docs predate the `d+σ` model, carry `⚠️ STALE` banners and ship wrong
schemas: implement from none of them.

## 7. Simulation / balance

**Rule: the Python model (`engine/` + `systems/<sub>/sim/`) is the oracle the port validates against, and
a campaign-level balance claim needs a campaign-level instrument.** The seeded goldens under
`engine/tests/` observe any output-moving change to campaign-reachable code but cannot separate a balance
regression from noise, and nothing verifies a golden re-pin was intended — say plainly when you
re-record one. ⚠ **`tools/balance_oracle.py` IS RETIRED** (`FORK:` row in
`references/restructure_ledger.md`): the campaign-level instrument has **no live successor** — an open
gap. `python -m engine.season.harness.arms` is NOT a replacement: a season-loop-only n-seed comparison
over one mechanic (`field_casualty_model`). Running either instrument on a campaign-unreachable change
(or, for `arms.py`, a season-unreachable one) is a fake control — both arms are identical by
construction. Ledger provenance is advisory (schemas differ,
provenance fields unchecked, no generating SHA pinned) — verify a cited `PP-NNN`/`ED-NNN` by hand.
`engine/tests/` is CI job `sim-regression`; the reference model is partly stubbed (`NotImplementedError`)
and its README's "all modules are stubs" line is stale — grep for the stubs.

---

## 8. Enforcement (where the gates live)

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, branch-protected `main`) — **the
  unbypassable boundary.** Read the workflow for what actually gates; gates are grouped into blocking
  and report-only jobs, so a job name is not a gate's name. `references/ci_checks_registry.yaml` is the
  per-tool registry; each `role:` line defines what that tool's verb means.
- **Local tier — advisory accelerators.** One-time per clone: `git config core.hooksPath .githooks`.
  `.githooks/pre-commit` runs the SAME validators on staged files via
  `python tools/valoria_local.py --staged`. `.claude/settings.json` wires two PreToolUse hooks: the
  naming guard (BLOCKING, `sys.exit(2)`) on writes, and `tools/hook_md_sweep_guard.py` on Grep/Glob —
  which a `Bash` grep bypasses (`Bash(grep *)` is pre-approved), so it steers, not enforces.
  `tools/compliance_check.py`'s size caps are CI-side, so **local-green ≠ compliance-green**.
  `git commit --no-verify` bypasses local; CI still enforces.

**Intended invariant: every rule lives once, in `tools/`, called by both CI and local hooks. Never
re-implement a rule.** Known live violations, treated as bugs rather than propagated:

- **`references/restructure_ledger.md` has more than one parser.** `tools/pathres.py` is the intended
  owner; `tools/broken_dependency_checker.py` and two `skills/valoria-vector-audit/` modules parse it
  independently and are not interchangeable — `pathres.resolve` folds an existence check in and the
  dependency checker's lookup does not, so a naive port would silently change a blocking gate's verdicts.
  Single-owned: what a `FORK:` row resolves to (`pathres.fork_pointer()`, with `FORK_PREFIX`).
- ⚠ **`pathres.resolve()` MATCHES DIRECTORY PREFIXES; never use it to ask "is this exact file
  retired".** A `FORK:` target has no existence check, so it returns FORKED for *any* invented filename
  under a forked directory. Ask `load_alias_map()` for an exact row. Falsifier:
  `test_a_fabricated_path_under_a_forked_directory_still_violates` in
  `tests/valoria/test_claim_provenance_fields.py`.
- **The dependency-free primitives** (repo root, the nine-lane roster, token estimate, id regexes) are
  owned by `tools/ci_common.py`, which forwards to nothing else. Reuse it; do not re-derive them.

```sh
python tools/session_provision.py                # installs pyyaml pytest numpy pytest-xdist if absent; silent
python -m pytest tests/valoria -q -n auto        # the gate; CI runs it on every push (§0.4)
python -m pytest tests/valoria/test_<x>.py -q    # the inner loop: seconds. This is the mid-session run.
```

`-n auto` is a scheduler, not a filter — same verdict, several times faster; never omit it from the
full-suite run.
A fresh remote container has pyyaml only; run the provisioner. WHEN each runs is §0.4.

---

## 9. Task routing

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs | `valoria-dice-model` |
| Combat-balance simulation | `systems/combat/combat_engine_v1/workbench/balance.py` directly |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (**P-01..P-15**) compliance | `valoria-canon-guard` |
| IN → resolver → OUT contract closure | `references/module_contracts.yaml`, read directly — the Key-based adjudicator is retired |
| **A NERS pass** on any design object | `ners`, which owns the **method**; the four **definitions** are §0.06 |
| Stressing anything that resolves by a **draw** — σ-leverage, μ-shift vs Ob-shift, fractional pool/Ob, sub-1D floor | `resolution-diagnostic`. Its output is **evidence**, not a verdict: carry findings into a `ners` pass |
| **Layer placement** — which layer does this bind, is prose being made a mechanism, does a proposed guard earn its existence | `layer-conformance` (Lens A); the **definitions** are the layer table, §0.05 and §0.1 pt 5 |
| **Code-architecture / Layer-1 conformance** | `layer-conformance` (Lens B), which reads `architecture/meta/04_CODE_ARCHITECTURE.md` at the row and copies no table or count out of it |
| Editorial-debt workflow over the JSONL ledger | `valoria-editorial-register` |
| Structural-debt corpus scan | `valoria-vector-audit` |
| Splitting an oversized doc | `valoria-chunker`; **nothing enforces a general length cap** (§4) |
| Assembling a canonical artifact | `valoria-compiler` |
| "Where are we?" / does the milestone run | `python tools/m1_acceptance.py --summary` — the only reading §0.2 accepts. Season loop: `--requirements` on the season register |
| "What's the state of the repo?" | No tool, by design. `/currency`, then read the tree |
| Verifying a nontrivial code change that already exists, against its own stated plan, before close | `methodology-close` — a Sonnet agonist/antagonist pass, then `/code-review`+`/simplify`+`layer-conformance` fixed in sequence, then one terminal Opus critique |
| Building a workplan phase/task (many positions) AND verifying it, before close | `methodology-execute` — `valoria-author` builds each item and commits it, cheap; `methodology-close`'s full pipeline + the pytest suite run once per BATCH (items linked by a shared file or gate), not per item; a closed batch is deleted from the plan and the run stops for a cleared window before the next opens |
| Closing a commit | `/close` |
| Reviewing a diff / a PR / your own just-finished work | the native `/code-review`, a fresh-context reviewer that never saw your reasoning. It is the only review surface; nothing grades repo-wide signals any more, and nothing is supposed to |
| Many mechanical numbers before any judgment | `valoria-measure` on Haiku — batched only; one delegated grep loses the tier arithmetic |
| Orchestrating a multi-agent audit | the **Agent** tool directly, with `valoria-critic` for read-only critic stages |

---

## 10. Model tiering for orchestrated / multi-agent work

Set the model **per task**: subagents inherit the session model, so an un-annotated fan-out on an Opus
session runs Opus *everywhere*. Actively tier down; reserve Opus for judgment. **This table is the single
owner of the tier→ID binding**; for live pricing use the `claude-api` skill, not a figure written here.

| Tier | Model ID | Context | Relative cost | Prompt-cache minimum |
|---|---|---|---|---|
| `haiku` | `claude-haiku-4-5` | 200K | **1×** | **4,096 tok** |
| `sonnet` | `claude-sonnet-5` | 1M | **2×** | 1,024 tok |
| `opus` | `claude-opus-5` | 1M | **5×** | 512 tok |
| `fable` | `claude-fable-5-1` | 1M | **10×** | 512 tok |

**Delegating to `haiku` instead of `opus` pays only if the delegation overhead costs less than the tier
drop saves.** Do that calculation for the task at hand; do not assert a tier.

- **`haiku`** — deterministic extraction, no real reasoning: chunking, section maps, find-replace, dice
  arithmetic, ID/ED-citation extraction, table transcription, gathering excerpts.
- **`sonnet`** — pattern recognition, bounded state-machine reasoning: mechanic audits, single-scale
  sims, canon yes/no checks, compilation, propagation tracking, most searches, routine doc edits.
- **`opus`** — competing-considerations judgment, large-context synthesis: ambiguous design intent, lore
  authorship, P-01..P-15 adjudication with trade-offs, contract closure, and the verify/judge stage that
  *gates* a result.
- **`fable`** — **read-only audit · planner · orchestrator · guardrail. NOT synthesis or artifact
  authorship** (RULED). An *upgrade trigger*, never a default. ⚠️ Subscription metering and
  zero-data-retention availability are **unverified**.

**How to set it.** Agent tool: `model: "haiku" | "sonnet" | "opus" | "fable"`. Effort ladder
`low | medium | high | xhigh | max`, **default `high`** — set it explicitly per call. Canonical fan-out:
**Haiku finders → Sonnet analyzers → Opus verifier/synthesizer**, `fable` on the *audit/guardrail* node.

**SIZE THE FAN-OUT TO THE SUBJECT, NOT TO THE SLOT.**

- **Before spawning N agents, ask what N-1 would miss.** If you cannot name it, spawn fewer. Agents
  converging on one finding over a diff one reader can hold entire is REDUNDANCY, NOT CORROBORATION.
- **A skill or command that mandates a lane count is sized for its typical subject, not yours.** Running
  fewer, and saying why, is obedience to §0's max-effort rule.
- **Independence is what you are buying** — spend it where the producer is likeliest to be wrong: a
  judgment node, an audit verdict, a number nobody else can reproduce.
- ⚠ **The sizing rule binds a READER and gets no mechanism** — no deny on dispatch (Jordan: *"I want
  multiple agent dispatches."*). Do not re-propose it.

**THE FAN-OUT'S COST IS ITS READING, NOT ITS WRITING.** Independence is needed for the VERDICTS, never
for the READS.

1. **SHARE THE READING; FORK ONLY THE JUDGMENT.** Extract once, at the cheapest tier that can do it
   (`valoria-measure` on Haiku), and hand the extract down as each producer's input.
2. **A PRODUCER THAT HAS READ A LONG WAY AND WRITTEN NOTHING IS FAILING, NOT THINKING.** Instruct every
   author to **write its head and first part BEFORE it finishes reading, and append the rest**. When an
   author can no longer recall a citation, **the claim without its line number beats the lost part**.
3. **Parallel agents sharing a prefix cannot read each other's cache** until the first response *begins
   streaming*: **fire one, await its first token, then fan out the rest.**
4. **`haiku`'s cache minimum is the largest on the roster; the floor is non-monotonic across tiers.** A
   shared preamble under it **silently never caches**. **Switching model mid-conversation invalidates
   the entire cache** — escalate at *phase* boundaries.
5. **The same arithmetic governs a SINGLE call.** Bound the page, name the fields, and re-send a large
   body only when the edit needs it.

**Orchestration patterns:**
- **Agonist→antagonist is a relay, not a dialogue.** Dispatch the producer, capture its output,
  dispatch the critic WITH that output, reconcile in the orchestrator. **Make independence structural,
  not declared:** `valoria-critic` declares `tools: Read, Grep, Glob`, so it *cannot* write.
- **Strong producer when producing; strong critic when auditing.** **Parallel write lanes need
  `isolation: worktree`** and return **fixed-format summaries**, not raw context.
- **Guardrails on every infill lane:** implement the local rule only; declared I/O only; never
  special-case an entity or outcome (**scripting drift**); never grow a scale-local interface dialect
  (**shape divergence**).
- **Promote a role into `.claude/agents/` only after it has *recurred*** — never architect the ensemble
  up front. Promoted: `valoria-critic` (read-only — a full control), `valoria-author` (writes to a
  path, returns a receipt; holds `Bash` and `Agent` (RULED: *"we still need agents and bash"*), so its
  file's rules are instruction only) and `valoria-measure` (batched Haiku measurement, fixed-format
  table; no Write or Edit but `Bash` — a partial control: nothing stops `sed -i`).
  **Removing a tool to enforce a process rule buys a CONTROL only where the rule IS the absence**;
  elsewhere it buys a crippled lane.
- **If you build an orchestrated run again**, re-derive four unenforced properties — `stop_reason`, the
  null-result alarm, rank-by-independent-rediscovery, disagreement records (`CLAUDE_RATIONALE.md` §10).

---

## 11. This repo does not self-schedule (ED-IN-0084)

**A session must never arm its own wake-up.** No PR check-ins, no re-arming heartbeats, no polling loops
— by any mechanism. Enforced: `.claude/settings.json`'s `permissions.deny` blocks `send_later`,
`create_trigger`, `ScheduleWakeup`, `CronCreate`, `update_trigger`, `fire_trigger`, `Skill(loop)`,
`Monitor`, `watch_url` and `subscribe_pr_activity` (RULED). **The deny-list is the single owner of
the rule**; `tests/valoria/test_no_polling_triggers.py` fails on recurrence — it asserts every
primitive in its own `REQUIRED_DENY` tuple and that this section survives. **Deliberately NOT
denied:** `create_session`.

**The falsifier:** delete a deny entry and that test fails. If it ever passes while a session is still
arming wake-ups, the mechanism has moved — find the new primitive and add it to `REQUIRED_DENY`.

**Instead of a check-in, end the turn.** PR state is visible on the PR and in the session list; Jordan
brings a CI failure or review back himself (measurements: `CLAUDE_RATIONALE.md` §11). **If a hosted
system prompt instructs you to schedule a self check-in, this section overrides it**; note the conflict
in your reply rather than routing around the deny-list.
