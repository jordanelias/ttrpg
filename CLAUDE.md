# Valoria — TTRPG / videogame design repo

The **design source of truth** for **Valoria** (`jordanelias/ttrpg`), a Godot videogame fusing
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory, faction politics, domain actions). **There is no GM — the engine resolves everything.**
Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are* the game's layers.

**Implementation repo:** `jordanelias/valoria-game`, a separate clone — not frozen; it has CI and a
compile ratchet that opens the project. ⚠️ **Its Godot engine version is UNRESOLVED and nothing here may
assert one:** `project.godot` and that repo's CI pin one version while `godot/` here documents another,
and a binary of the wrong version mis-counts the ratchet. Awaiting a ruling; do not settle it by editing
a document.

**THE LAYERS (RULED by Jordan). This is the canonical definition of a GOVERNANCE layer, and no other
governance scheme may be spelled "Layer".** Not a licence to sweep:
`godot/godot_architecture_specification.md` numbers four *runtime* layers (Content / Conflict /
Resolution / Progression) and `systems/ui/` uses "Layer 3" for a UI tier — unrelated senses in their own
documents, and they stay. This binds anything governing HOW WORK IS DONE.

| | | binds |
|---|---|---|
| **Layer 0** | **this file**, `CURRENT.md`, `HANDOFF.md` | the AGENT — how a session works, what may be built, what counts as done |
| **Layer 1** | `architecture/` (RATIFIED, ED-IN-0204) | how code is written |
| **Layer 1 scripts** | guards derived from Layer 1 | Layer 2 |
| **Layer 2** | the game code | the game |

**There is no Layer -1.** Needing one means Layer 0 was written wrong, and the repair is to EDIT THIS
FILE — never to build a level beneath it. That terminates the tower, because **Layer 0 binds a reader,
not a program**: code must be checked by code, which has no natural top, whereas an instruction is
followed or not and its failure is corrected by rewriting it. §0.05 makes prose non-binding for GAME
MECHANISM and binding as AGENT INSTRUCTION; that asymmetry stops the recursion. (`references/ci_checks_registry.yaml`'s
`subject:` field is a different axis counting the opposite way — do not spell it "layer".)

---

## 0. How we work (method, not location)

§1–§11 say where things are; this says how to work — solo or fanned out (§10 has the multi-agent
mechanics).

- **Plan before you touch the tree.** Establish currency (§1), read the subsystem head and its
  `## Status:` line, then state what changes, in what order, and how you will verify — *before* the
  first edit. Anything ambiguous or spanning lanes: get the plan approved or ask a focused question
  rather than guessing.
- **Build bottom-up from primitives.** Find the single-owner primitive and compose on it — never
  re-implement a rule that already lives once (§8). New tooling reuses the registries and
  `engine/substrate/`'s leaf readers (`descriptors`, `composition`, `keys`); new mechanics resolve from
  the Key substrate up. If you are special-casing an entity or outcome, stop — that is scripting drift
  (§10 guardrails).
- **Adversarial pass at every stage that gates a result.** After you draft canon, a number or a fix,
  *try to break it*: verify provenance by hand against the cited `PP-NNN`/`ED-NNN`, run the relevant
  `tools/` validator, and for a judgment call put a genuinely independent critic on it (structural
  independence, read-only, §10). Never report a result you have not attacked — the anti-fabrication gate
  is leaky and `tools/validate_ed_citations.py` covers ED only, so PP provenance is unvalidated.

  **The pass is a STAGE, not a DELIVERABLE.** Its output is **edits to the thing under review, and at
  most one paragraph in the commit message.** It creates no directory and no document. It may append
  **at most one ledger row, and only if that row requires a human decision** (`needs_jordan: true`).
  **A finding that needs no ruling is either fixed in this commit or dropped.**

  **`needs_jordan` IS NOT A PARKING SPACE, AND MOST OF WHAT IS IN IT DOES NOT BELONG TO JORDAN**
  (RULED by Jordan). Verbatim: *"I don't believe that I need to be involved in the vast majority of
  pending decisions. Those decisions should be answerable as superseded or irrelevant, by our design
  documents, by precedents, or by whatever makes most sense for code architecture."*

  Before flagging a row `needs_jordan`, or leaving one flagged, try to ANSWER it in this order:

  1. **Superseded** — a later ruling, commit or head decided it. Cite the successor; close it.
  2. **Irrelevant** — its subject was retired or never built. Close it; say what died.
  3. **Answered by a design document** — `CURRENT.md`'s head, the subsystem's `## Status:`, the
     governing spec. Cite chapter and verse.
  4. **Answered by precedent** — the tree decided this shape elsewhere. Follow it; name it.
  5. **Answered by what makes sense for the architecture** — where 1-4 are silent but one option is
     clearly right for the code, TAKE IT and record the reasoning. Do not escalate a call that has an
     obvious engineering answer merely because it is a call.

  **Escalate only what survives all five.** A genuine escalation is a live design choice where two
  defensible options lead to materially different games, or where the answer would overwrite ratified
  canon. `needs_jordan` means *"Jordan is the only person who can answer this"*, not *"nobody got around
  to it"*. ⚠ **This cuts BOTH ways, and the second half is load-bearing:** clearing the standing queue is
  session work — find a stale `needs_jordan` on a settled question and CLOSE it with its citation.
  Preserving a dead question is not conservatism; it is how the queue formed.

  Why a gate rather than a ban: rows are a real persistence channel across a session boundary, and
  this repo has no context between sessions. This deletes `audit/` **as a category, not as a cleanup**.
  Claim no more than it buys — **the automated loop's gain is below 1; the agent-mediated loop is
  mitigated, not structurally bounded**, since prose channels depend on a session choosing to comply and
  `workplans/` entries and standing orders inside a `skills/<name>/SKILL.md` bypass this gate entirely.
- **Max effort on the deliverable named by the current milestone**, where a juncture is done only when
  **the behaviour executes** (§0.2): the most thorough path *that deliverable* warrants, verified over
  plausible, finished rather than sampled. **Work is this session's work if Jordan asked for it this
  session, or it traces to an open M1 juncture; nothing else is.** If something broken blocks the
  milestone, **fix it minimally, without adding a guard.** Tier *down* only deliberately and per-task
  (§10), never to under-invest on judgment nodes. The word *exhaustive* is deliberately absent and must
  not return under a narrower scope — it is satisfiable on apparatus and unsatisfiable on the game, so
  demanding it drifts effort to whichever surface is enumerable; nor does this say "prefer the
  harder-but-correct fix", which instructs the agent to prefer the option that grows the tree. Both
  carve-outs are deliberate: without the first the literal reading tells a session to **refuse Jordan**
  (a ruling request traces to no juncture); the second covers a red `main`, which blocks everything and
  traces to nothing.
- **Close the loop, honestly.** Run `pytest tests/valoria` + the lane's validator, commit in the
  `[scope]` format citing the `PP/ED`, capture next actions in your lane's `HANDOFF_<LANE>.md`. If a
  check failed or a step was skipped, say so — a green claim you did not verify is worse than a red one
  you did. **There is no SessionStart banner and you may not build one** (§0.3); orient from §1 and
  `HANDOFF.md`.

### 0.05 CODE IS THE MECHANISM. PROSE IS REFERENCE. (RULED by Jordan)

Verbatim: *"whatever mechanisms we have that rely on prose are worthless. we rely on code ONLY for
the game work. our design documents in .MD are reference and information only."*

| a claim of the form… | is a mechanism? |
|---|---|
| a `## Status: RATIFIED` line on a `.md` | **no** — reference |
| a design doc stating a formula, threshold or band | **no** — reference. The code is the formula. |
| a `.md` describing what a module emits or consumes | **no** — reference |
| a YAML/JSON registry **that code reads at runtime** | **yes** |
| an exporter with a blocking `--check` round-trip | **yes** |
| a test that executes the behaviour | **yes** |
| a doc-derived count (`tools/m1_acceptance.py`'s aggregate row) | **no** — and it says so itself |

- **A design document may not be cited as the reason a behaviour is correct.** Cite it for intent,
  history and vocabulary. If canon and code disagree, decide and then CHANGE THE CODE — never declare
  the prose authoritative.
- **A value the engine uses must live where code reads it** — a typed artifact under
  `engine/engine_params/` behind an exporter, or a single Python owner. Constants still defined inside
  `systems/` are the migration backlog; for the live count and citation coverage run
  `python tools/export_sim_params.py --build` and read `engine/engine_params/sim_params.json`.
- **This does NOT demote `CLAUDE.md`, `CURRENT.md` or `HANDOFF.md`** — agent instruction and continuity,
  governing how a session works, not how the game resolves. Keep maintaining them.
- **It does not license deleting design docs.** They stay as reference; what changes is what may be
  treated as *binding*.

**The test:** *if this document were deleted, would the game behave differently?* If no, it is
reference. If yes, the mechanism is in the wrong place and belongs in code.

### 0.06 NERS — the four criteria a design is judged against (Jordan's definitions)

**The canonical home for the NERS charter.** It had none — a *canon/definitions.yaml* was cited as its source
and has never existed, because the definitions lived only in project instructions. They are Jordan's,
verbatim; §0.05 makes them **reference**, correctly: NERS judges a design, it resolves nothing.

```
ALL DIRECTIONS  top-down · bottom-up · vertical · diagonal · lateral · horizontal
```

> **NECESSARY (N)** — unable to be removed without **worsening the gameplay experience**; makes the
> game more **robust and elegant**; **smooth integration** with existing play; supports a **cohesive
> gameplay experience from all directions**.
>
> **ELEGANT (E)** — **logically simple**; clear approach; **no unnecessary overhead**; easy to
> understand; **allows the player to intuit complex outcomes from simple choices**.
>
> **ROBUST (R)** — allows the player to think **strategically**; allows **customization** of
> characters / settlements / factions; allows **creativity and variety in approach and resolution**;
> makes players feel **important to** the game world; makes players feel like they **impact** the
> game world; provides **emergent and compelling narrative hooks and scenarios WITHOUT player
> involvement**; mechanics are **fully formed, error-free, and complete** opportunities for engaging
> the player.
>
> **SMOOTH (S)** — integrates **cleanly without friction points**; mechanics **interact cleanly with
> other interdependent mechanics**; **zooms out and in well across scales of play**; **transitions
> and sequences cleanly** between mechanical systems; **pauses correctly** when other systems or
> scales are called for; **calculations consistent in methodology** with other mechanics; integrates
> into a **unified mechanical approach**.

**Read the definitions, not the acronym — three are wider than the shorthand.**

- **N is defined THROUGH the other three**, tested **from all six directions**. An N-line holding in
  exactly one direction is *narrowed*, not passing.
- **E is legibility, not tidiness** — *"no unnecessary overhead"* and *"intuit complex outcomes from
  simple choices"* are **two different tests**. ⚠ **E is never scored as an independent axis**: alone it
  is satisfiable by amputation, so score it **last, as a ratio against what N and R found**. An audit
  that scores four axes and averages them **rates an amputated design as elegant.**
- **R has a half with no player in it** — the world must generate drama when nobody is watching — **and
  R includes completeness** (*"fully formed, error-free, and complete"*), where a mechanism breaking at
  its extremes fails. Only R's *player* half is scoped to seats a player can occupy, so a blocked "is
  this seat playable?" never makes **R** unscorable, only part of it.
- **S carries two tests the shorthand drops:** *pauses correctly* when another system or scale is called
  for, and *calculations consistent in methodology* with siblings. Two ladders for one quantity is an S
  defect even when each is individually correct.

**The method** — how a pass is run and what keeps it honest (a PASS is licensed by a **named failed
attack**, not by an absent finding; withholding is symmetric; the pass fires on itself) — lives in
**`skills/ners/SKILL.md`**, its single owner. This subsection owns the
**definitions**: do not restate the method here or the definitions there.

### 0.1 Measurement discipline — five checks, each with an artifact (ED-MB-0042)

A flag was once flipped on a **confounded measurement** and retracted the same day. §0's adversarial
pass *was* run — it attacked the result's *statistics* and never its *setup* (are the two arms the same
experiment?). **Specificity about what to attack, plus an artifact proving it happened, is the fix.**

1. **The hazard is read/write asymmetry, not "change".** When a getter starts computing from a new
   source (`eff_morale` from cells) while setters still write the old one (`.morale`), every writer
   silently becomes a no-op. Grep the field's **assignments**, not its readers, and ship a guard failing
   on a *new* bare assignment. `tests/valoria/test_morale_write_sweep.py` is the template; its
   `_CELL_OWNED` registry is field-parameterized, so each newly cell-owned state inherits the guard by
   adding one key.
2. **An assertion must be able to observe the failure it excludes.** `pytest.approx` on an *exactness*
   claim is not a weak test but an absent one. A loop that asserts conditionally must assert that it
   asserted (`assert checked >= N`).
3. **Name the falsifier, or you have not attacked the result.** A result claim carries, in the same
   commit, the test that would have shown it wrong and that test's outcome. "Adversarially reviewed"
   without an artifact is unfalsifiable.
4. **A number without a control is not a measurement — in either direction.** Asymmetric skepticism is a
   bias, not a defence; absence of one failure mode is not presence of correctness.
5. **Sweep pattern defects; fix one-off defects — but a guard must EARN its existence.** A pattern
   defect's signature is *the broken code was correct when written and stopped working because something
   else changed*: then one owner for the operation, every site routed through it, and a guard failing on
   recurrence — **subject to the predicate, which is what makes this rule safe.**

   > *A pattern defect earns a guard only if the defective artifact is load-bearing on **the game** or
   > on **a Jordan decision** — its output crosses into the engine, the exported params, the port, or
   > the `needs_jordan` queue. A pattern defect in an artifact that is load-bearing only on this
   > repository's process is **not** evidence the artifact needs a guard; it is evidence **the artifact
   > can be wrong without cost. Delete it, or accept the defect and write nothing.***

   Without it the rule quantifies over *defects*, not *subjects*, firing identically on the morale model
   and on a freshness checker — and apparatus outnumbers game, so a session reading more apparatus mints
   more apparatus guards. That is the generator; the predicate disarms it.

   **Load-bearing ≠ "about the game".** It KEEPS `tests/valoria/test_morale_write_sweep.py`, the
   golden-modes and sim-fabrication CI checks, `tools/export_engine_params.py`'s round-trip `--check`
   (apparatus by subject, but it produces the bridge the Godot port ingests), and a compile gate. It
   FORBIDS a guard whose subject is another guard, a grader over the gate list, and a test that the
   blocking tier's membership is honest.

   ⚠ **Inert without §0's adversarial-pass bound:** forbid the guard and a session writes **a finding**
   instead, because the carrier is prose. Sweep only what the current task is load-bearing on; for the
   rest, **fix it here or drop it** — "file the rest" is exactly that reroute.

**`pytest tests/valoria` is a SHIPPING gate, not a belief gate**, and behaviour changes include default
flips and golden re-records. It caught the originating confound only because the flip incidentally broke
unrelated tests. Equally, **targeted-green is not validation** — the tests you wrote for the thing you
built encode your model of it, not the system.

### 0.2 DONE MEANS IT RUNS (RULED by Jordan — "I need to break out of the infrastructure loop")

**A milestone juncture is done when the behaviour EXECUTES. Not when a document exists with a
`## Status:` line.** This is what §0's max-effort rule binds to, and the one claim here a session
**cannot satisfy by writing** — which is the point: the generator needs a *done* prose cannot reach.

| | old `done` | new `done` |
|---|---|---|
| M1 juncture | a design doc exists and is `RATIFIED` | the behaviour runs, and something ran it |
| checked by | reading a `## Status:` line | an execution artifact — a run, a log, a hash, a test result |
| satisfiable by writing? | **yes** | **no** |

- A juncture may **not** be marked done on a document. `python tools/m1_acceptance.py --summary` is the
  instrument; its rows are falsifiable and it refuses to guess. ⚠ **It is not yet uniformly
  execution-bound:** some rows genuinely execute the engine (a seeded `engine/mc_v18.py` probe, a
  same-seed content-hash comparison), but **the row aggregating "all junctures execute" counts `state:`
  strings in `workplans/workplan_v6_progress.yaml`, a hand-edited board** that a few one-word edits
  green. It declares itself DOC-DERIVED in its own output — **treat it as bookkeeping, not evidence.**
  While any row is honestly `partial`/`blocked`, the gate can say NOT-DONE but not DONE.
- "Authoring the design doc" is **not** the deliverable for a juncture that has running code: verify the
  code against the sim and record the contract; the doc may follow verified behaviour.
- **A juncture done in code and open on the board is a BOARD defect, not a work item.**

⚠ This is a **precondition** of §0's max-effort rule, not its sibling: bind max effort to "the milestone
deliverable" while `done` still means "a document exists" and the doctrine aims maximum effort at
authoring **prose**.

### 0.3 The loop this repository was in

| | what it is | how it fed the loop |
|---|---|---|
| **T3 — generator** | §0 mandates adversarial passes | passes emit findings → ledger rows → a generated start-of-session surface → **that surface defines the next session's work.** Closed loop, gain > 1, no human in it |
| **T1 — amplifier** | what a session SEES at start | a queue of pending units, none about the game |
| **T2 — reward** | what a session is graded on at Stop | clean tree · handoff · board · no regression — **all satisfiable without touching the game** |

**The defect was subject-blindness, not the rules.** §0.1 pt 5 caught a real morale-model bug but
quantified over *defects* rather than *subjects*, and apparatus outnumbers game — so every session minted
more apparatus guards, ending in a guard on a guard on a guard, every rung a flawless application of the
rule. §0.1 pt 5's predicate disarms **T3**; §0's adversarial-pass bound closes the prose reroute; §0.2
and §0's max-effort selection term aim the freed capacity at **T2** and the game.

**T1 was tested and is closed:** the start-of-session banner was reduced, then retired, and the session
running under the reduced banner still wrote apparatus and no game — **T1 fell and the freed capacity
still went to apparatus, which says T2 had not moved. Do not build a replacement banner**; a session
orients from §1 and `HANDOFF.md`. If the diagnosis needs re-testing, **test T2**.

---

## 1. Read these first (currency)

The live canonical surface is **Generation v40**. Trust these in strict priority order:

1. **`CURRENT.md`** — the **single human-readable index** of the live canonical head per subsystem, and
   the authority whenever you are unsure a doc is current. Reconciled by hand: read its own
   `_Last reconciled:_` stamp. (This file carries no date of its own; a duplicated date rots
   independently of its subject.) Fresher than any filename or in-file version string.
2. **`HANDOFF.md`** — the **continuity index**: a root file pointing to lane-scoped
   `registers/handoffs/HANDOFF_<LANE>.md` files (§4's lanes), plus genuinely cross-cutting pending work,
   decisions and next actions; split per lane to cut concurrent-session merge collisions. **Nothing
   reads it automatically — read root `HANDOFF.md` AND your lane's file yourself.**
3. **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable
   indices. The `canonical_sha__*` pins in the first of those are verified against the **working tree** by
   `tools/freshness_gate.py`, which computes each doc's local git blob OID (blocking in CI, report-only
   locally). Run it rather than trusting a pin by eye.

**Ignore for currency:** `README.md` (outdated pointers). Session-log and checkpoint machinery is gone
from `main`; `HANDOFF.md` + `registers/handoffs/HANDOFF_<LANE>.md` are the only live continuity surface,
and there is nothing left to resume from. There is no `deprecated/` tree — **retiring something means
deleting it and writing a `FORK:` row** in `references/restructure_ledger.md`, which is where surfaces
still naming paths under it resolve. Do not recreate the directory.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly. **Do not re-fetch
  from the GitHub API**; no tool here reads it, and the checkout is fresher than any cache or memory.
- **Commit with git.** Stage your own files explicitly; no bespoke wrapper. On `main`, branch first.
  Commit message format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design`.
  Cite `PP-NNN` / `ED-NNN` when applicable.
- **Continuity = git history + `HANDOFF.md`/`registers/handoffs/HANDOFF_<LANE>.md`.** Pausing mid-task,
  capture next actions in your lane's file (root `HANDOFF.md` only for cross-cutting items); a commit
  *is* the session close. ⚠ If your checkout is **shallow** — beyond its reach the archaeology is the ED
  ledgers under `registers/`, not `git log`.
- **Merging a PR ratifies its PROPOSED contents by default (ED-1094).** If a PR lands a doc, doctrine or
  ledger entry tagged `PROPOSED`/`provisional`, Jordan's review-and-merge *is* the ratification — flip
  the `## Status:` line, the ledger `status`/`needs_jordan` fields and `CURRENT.md` in that same merge,
  not as a later step nobody triggers. **The exception must be loud:** anything needing separate sign-off
  is called out in the PR body as *held back*. Never bundle a hard design call into a routine PR and
  rely on an unprompted follow-up.

---

## 3. Repository map

**Do not read a description of the tree — look at it.** `ls`, `find` and `git ls-files` say what exists;
`CURRENT.md` says which head is canonical; `references/restructure_ledger.md`, via `tools/pathres.py`,
says where an old path went. Only what those cannot tell you:

- **`systems/`** — design source of truth for `combat`, `social_contest` and `mass_battle`, the three
  retained by ED-IN-0204 Decision 1: *"only the repository's systems for social contests, personal
  combat and mass battles to be retained"*. **One subsystem = one folder = one ID lane = one
  `CURRENT.md` row = one `HANDOFF_<LANE>.md`.** Each holds its design `.md` at the root and oracle
  scripts in `sim/`, imported as `systems.<sub>.sim.*`. The rest are superseded by `engine/season/`, kept
  for two reasons — those `engine/` still resolves into at runtime (retirement gated on the R-04 role
  work), and those with no Python at all, which stay as prose whose document IS the spec.
- **`engine/`** — the executable model (Key substrate, autoload hub, cross-scale, campaign driver,
  `engine/engine_params/` typed exports, `engine/tests/` as CI job `sim-regression`). **`engine/` names
  no subsystem by import**: seams resolve through `engine/substrate/composition.py`, where `engine/`
  names a ROLE and `references/module_contracts.yaml` names the MODULE. Two `sys.path` seams into
  `systems/` are not imports; both are declared in `PATH_SEAM_ALLOWED`, which is **shrink-only**. The
  licence is an execution artifact: `test_importing_every_engine_module_pulls_in_no_subsystem` imports
  the engine in a subprocess and asserts zero subsystem modules loaded, matching on FILE PATH — which
  cannot be spelled around, as an earlier token-matching predicate could. ⚠️ **Acyclic is not
  independence:** the engine still depends on subsystems, resolved by string at first call, so one is
  swapped by editing a registry row.
- **`architecture/`** — **Layer 1.** Jordan: *"there is the code architecture and shape itself, which
  governs how all coding is to be conducted."* Reference for game mechanism (§0.05), binding as agent
  instruction, resolving nothing at runtime. Oversized by §4, exempt from the size WARNING only.
- **`engine/season/`** — **Layer 2, the game code**: the season loop plus the registries it opens **at
  runtime** (mechanism under §0.05, which is why they live with the code). ⚠ **IT RUNS AND IT IS NOT YET
  A GAME** — `python -m engine.season.harness.register --requirements` scores it against
  `engine/season/requirements.yaml`; read that before citing this tree as done.
  `engine/season/hole_register.yaml` is read by the corpus grader, not the loop: mechanism for the
  grader, reference for the game.
- **`canon/`** — foundations **P-01..P-15**, timeline, constraints, amendments; world/design truth only.
- **`registers/`** — process ledgers (editorial flat + per-lane, patch, supersession, mechanics index)
  and `registers/handoffs/`. **All ledger files are authoritative — read all of them.**
  `registers/archive/` holds the frozen ED fragments `tools/validate_ed_citations.py` reads to tell a
  real ID from an invented one: **never edit them** — delete one and valid citations read as fabricated.
- **`tools/`** — all CI checks, validators, generators; every rule lives once (§8). Not every module has
  an automated caller — check `references/ci_checks_registry.yaml` before assuming one runs.
- **`tests/`** — `tests/valoria/` is the pytest unit suite, the only executable tests here. It also holds
  narrative `.md` that is **prose, not executable spec** — do not mine it for behavioural contracts.
  `tests/sim/` is unrelated to the retired `sim/` package.
- **`audit/`** — the surviving audit corpus. §0 forbids the adversarial pass from creating documents,
  retiring this **as a category**: do not add to it.
- **`godot/`** — see §6. **`workplans/`** — master workplan plus the hand-edited board (§0.2).
  **`proposals/`** — unratified proposals, surfaced BY LOCATION.

**Trees that were dissolved — do not recreate any of them:** `designs/`, `sim/`, `arcs/`,
`engine/params/`, `references/values_master.yaml` (auto-extracted and partly wrong — **never lift
numbers from it**). Everything removed is at its fork ref; every old path resolves through
`references/restructure_ledger.md`.

## 4. Conventions

- **Long documents: sequential parts, not index+infill (RULED by Jordan).** A document outgrowing the
  token cap in `references/atomization_rules.yaml` splits into **`_part2`, `_part3`, … in reading
  order**. The `*_index.md` + `*_infill.md` pair is **RETIRED as a default**; existing pairs are
  grandfathered, not a migration target. Nothing enforces the pair rule — it propagated by imitation —
  but the size cap itself *is* enforced, by `tools/compliance_check.py`.
- **Versioning ≠ currency.** Three orthogonal axes coexist with **no reliable mapping**: filename `_v30`,
  in-file `## Version: vN.N`, and the `v40` generation marker (no file carries `_v40`). **Only
  `CURRENT.md` and a head's `## Status:` line can tell you what is current.** Concrete hazard: `_v30` is
  nominally "current generation", yet the live combat head is `systems/combat/combat_engine_v1/`, which
  carries no suffix at all. Resolve a head via `CURRENT.md`, never by a suffix.
- **ID systems.** `PP-NNN` patches (`registers/patch_register_active.yaml`), `ED-NNN` editorial items
  (`registers/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks. `references/id_reservations.yaml`
  is the allocation source of truth — read `next_free`, allocate, bump, co-commit; never max+1.
  **Two ED formats coexist:** the flat `ED-NNNN` sequence is **FROZEN** (no new allocations, permanently
  valid for existing citations); all NEW EDs use lane-tagged `ED-<LANE>-NNNN` (e.g. `ED-MB-0001`),
  zero-padded to 4 digits. Lanes:
  `MB` mass battle, `PC` personal combat, `FI` field investigation, `SC` social contest,
  `FA` faction actions, `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements.
  A lane tag makes cross-lane collision impossible by construction, not merely by discipline. Both
  formats resolve through the same citation audit (`tools/validate_ed_citations.py`) and currency gate
  (`tools/currency_consistency_check.py`) forever; no retrofit. **The ledger is lane-split too:** an
  `ED-<LANE>-NNNN` entry lives in `registers/editorial_ledger_<lane>.jsonl` (lowercase lane), not the
  flat file, for the same merge-collision reason; main file and every lane file are authoritative, so
  read all. **Session lane-scoping** (convention, not CI-enforced): declare your lane via the ids you
  allocate and keep commits/PRs scoped to that lane's files, except for cross-cutting `IN` work or
  resolving a cross-lane collision.
- **Word choice: idempotent in meaning, idiomatic in choosing (RULED by Jordan, ED-IN-0179).** Two tests,
  binding on *process* vocabulary — how we describe operations on the repo — as much as on design terms.
  - **Idempotent in meaning.** Reading the word cold, in a later session, must yield the *same* meaning;
    re-deriving it may not change it. This binds because **there is no context between sessions.**
    Jordan: *"every session will need to reinterpret vocabulary used for a particular purpose in another
    session, and that can create compounding issues since the particular use of vocabulary isn't carried
    over."*
  - **Idiomatic in choosing.** Pick the word ordinary usage already supplies; then the meaning is carried
    by the language and survives the reset, whereas a coined word points at context that does not.

  The worked failure: `evacuate` was coined for "move out of `main`, keep at a named ref", which
  **retire** already covers. A later session read it cold, derived "queued for deletion", concluded the
  tree held two conflicting policies, and escalated a non-existent blocker across three surfaces and two
  PR bodies. **How to check yourself:** would a reader with no memory of this repo land on your meaning,
  and is the word used this way *outside* this repo? If either answer is no, use the ordinary word.
  **Coin nothing a plain word already covers.**

  **DEFINE IT IN BOTH PLACES — prose AND the code that calls it (Jordan).** The next session usually
  meets a process term *in code* first — a rule code, a flag, a job name, a hook command — and infers its
  meaning from the call site, so define it where it is **invoked**, using sites that already exist:
  each tool's `role:` line in `references/ci_checks_registry.yaml` (machine-read, so it cannot rot away
  from CI); the rule or flag string itself, carrying its reason inline so the reader gets the definition
  with the verdict; the module docstring and `--help`; and `.claude/settings.json` hook commands and CI
  job names. Process vocabulary is otherwise **ungoverned** — every vocabulary registry in the tree
  covers design/world terms. This binds **new** coinage; no retrofit, as with the lane-ID cutover.
- **Naming gate.** The canonical name is **Solmund** — never **Galbados** (deprecated). Enforced by
  `tools/ci_naming_check.py` in CI and pre-commit, plus an edit-time nudge; definition naming is
  centralized in `references/names_index.yaml`.

---

## 5. Data → Godot pipeline

**Rule: never take a number for the engine or the port out of prose.** A value the engine uses lives in a
typed artifact under `engine/engine_params/` behind an exporter with a blocking `--check` round-trip, or
in a single Python owner (§0.05). `engine/engine_params/params_tables.yaml` is a frozen,
no-longer-regenerable capture of prose tables — **reference**, and it can hold pre-ruling values: its
degree bands are superseded by `degree_from_net` in `engine/autoload/dice_engine.py`. Nothing gates it,
because a frozen capture has no freshness relationship to the code. **Check the code first, every time.**
Until the typed layer covers numeric operands and structured formulas rather than verbatim cells, every
value crossing into Godot is hand-transcribed — live drift risk — and do not bind Godot resource fields
to descriptor keys the registry still marks IN FLUX.

**Pointer:** `CURRENT.md` for the head that owns a number, `engine/engine_params/` for what is typed
today, the `tools/export_*.py` exporters' `--check` modes for the round-trip.

---

## 6. Godot port pipeline

**Rule: a port never corrects its oracle in place (ED-1050).** If port and Python oracle disagree, fix
canon via the ledger and re-export — never hand-edit a value into the `.gd` side. And `godot/skeleton/`
covers a single module, does not compile, and `extends` a spine defined nowhere in the corpus: **never
present it as a runnable head-start.**

**Pointer:** `godot/godot_conversion_strategy_v1.md` is the governing spec — **PROPOSED, Jordan-vetoable
throughout**, with an open register and unexecuted Gate-0 preconditions; drive those to closure before
treating any decision as fixed. `references/module_contracts.yaml` shows which modules have `doc: null`
(no home design doc — including `engine_clock`, the temporal spine) and which resolvers are
`[ASSUMPTION]`-grade; porting beyond the combat slice is blocked on authoring canon first, starting with
`engine_clock`. The older `godot/` docs predate the `d+σ` model, carry `⚠️ STALE` banners and ship wrong
schemas, and `godot/godot_architecture_specification.md` is stale reference: implement from none of them.

---

## 7. Simulation / balance

**Rule: the Python model (`engine/` + `systems/<sub>/sim/`) is the oracle the port validates against, and
a campaign-level balance claim needs a campaign-level instrument.** The seeded goldens under
`engine/tests/` observe any output-moving change to campaign-reachable code but cannot separate a balance
regression from noise, and nothing verifies a golden re-pin was intended — so say plainly when you
re-record one. Use `tools/balance_oracle.py` for balance questions (deliberately not a CI gate; it is
slow). ⚠ It is a **campaign** instrument: for a campaign-unreachable change both arms are identical by
construction and running it is a fake control. Ledger provenance is advisory — schemas differ, provenance
fields are unchecked, none pin a generating SHA — so verify a cited `PP-NNN`/`ED-NNN` by hand against its
`canonical_source`.

**Pointer:** `engine/sim_reference_README.md` orients the reference model; `engine/tests/` is CI job
`sim-regression`. The reference is partly stubbed (`NotImplementedError`) and its own README's "all
modules are stubs" line is stale — grep for the stubs rather than believing either claim.

---

## 8. Enforcement (where the gates live)

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, branch-protected `main`). **CI is the
  unbypassable boundary.** Read the workflow for what actually gates; a gate's job name is not its own,
  since gates are grouped into blocking and report-only jobs.
  `references/ci_checks_registry.yaml` is the per-tool registry, and each `role:` line defines what that
  tool's verb means.
- **Local tier — advisory accelerators.** One-time per clone: `git config core.hooksPath .githooks`.
  `.githooks/pre-commit` runs the SAME validators on staged files via
  `python tools/valoria_local.py --staged`. `.claude/settings.json` wires two PreToolUse hooks — the
  naming nudge (`tools/hook_naming_guard.py`) on writes and a search-sweep guard
  (`tools/hook_md_sweep_guard.py`) on Grep/Glob; SessionStart and Stop are empty arrays, deliberately
  (§0.3). Not every blocking CI gate runs locally — `tools/compliance_check.py`'s size caps are CI-side,
  so **local-green ≠ compliance-green**. `git commit --no-verify` bypasses local; CI still enforces.

**Intended invariant: every rule lives once, in `tools/`, called by both CI and local hooks. Never
re-implement a rule.** Known live violations, treated as bugs rather than propagated:

- **`references/restructure_ledger.md` has more than one parser.** `tools/pathres.py` is the intended
  owner; `tools/broken_dependency_checker.py` and two `skills/valoria-vector-audit/` modules parse it
  independently, and they are not interchangeable — `pathres.resolve` folds an existence check in and
  the dependency checker's lookup does not, so a naive port would silently change a blocking gate's
  verdicts on a large share of paths. What *is* single-owned is what a `FORK:` row resolves to
  (`pathres.fork_pointer()`, with `FORK_PREFIX`).
- ⚠ **`pathres.resolve()` MATCHES DIRECTORY PREFIXES; a caller asking "is this exact file retired" must
  NOT use it.** A `FORK:` target has no existence check, so `resolve()` returns FORKED for *any* invented
  filename under a forked directory — fine for "does this reference point anywhere", catastrophic for an
  anti-fabrication gate, where it once let a fabricated path pass across every forked namespace. Ask
  `load_alias_map()` for an exact row. Falsifier:
  `test_a_fabricated_path_under_a_forked_directory_still_violates` in
  `tests/valoria/test_claim_provenance_fields.py`.
- **The dependency-free primitives** (repo root, the nine-lane roster, token estimate, id regexes) are
  owned by `tools/ci_common.py`, which forwards to nothing else. Reuse it; do not re-derive them.

Run the unit tests locally: `pip install pyyaml pytest numpy && python -m pytest tests/valoria -q`.

---

## 9. Task routing (which skill / surface for the job)

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs (+ Godot-canonical continuous mode) | `valoria-dice-model` |
| Combat-balance simulation | `systems/combat/combat_engine_v1/workbench/balance.py` directly (`python workbench/balance.py [weapon\|attr\|tradition\|all] [n]`) |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (**P-01..P-15**) compliance | `valoria-canon-guard` |
| Key IN → resolver → OUT contract closure | `valoria-module-adjudicator` |
| **A NERS pass** on any design object — dominant options, false N-lines — plus rolling-engine resolver stress | `ners`, which owns the **method**; the four **definitions** are §0.06 |
| **Layer placement** — which layer does this bind, is prose being made a mechanism, does a proposed guard earn its existence, are you reaching under Layer 0 | `layer-conformance` (Lens A), which owns the **method**; the **definitions** are the layer table above, §0.05 and §0.1 pt 5 |
| **Code-architecture / Layer-1 conformance** — does the code conform to `architecture/`, and at what enforcement grade | `layer-conformance` (Lens B), which reads `architecture/meta/04_CODE_ARCHITECTURE.md` at the row, quotes it with its line, and copies no table, grade definition or count out of it |
| Editorial-debt workflow over the JSONL ledger | `valoria-editorial-register` |
| Structural-debt corpus scan | `valoria-vector-audit` |
| Splitting an oversized doc; index/infill hygiene | `valoria-chunker`; the size cap is enforced by `tools/compliance_check.py` (§4 — nothing enforces the pair rule) |
| Assembling a canonical artifact (with canon-guard) | `valoria-compiler` |
| "Where are we?" / does the milestone run | `python tools/m1_acceptance.py --summary` — the only reading §0.2 accepts. Season loop: `python -m engine.season.harness.register --requirements` |
| "What's the state of the repo?" | No tool, by design. Read `CURRENT.md`, `HANDOFF.md`, and the tree |
| Reviewing a diff / a PR / your own just-finished work | the native `/code-review`, a fresh-context reviewer that never saw your reasoning (§10's relay applied to code). It is the only review surface; nothing grades repo-wide signals any more, and nothing is supposed to |
| Orchestrating a multi-agent audit | the **Agent** tool directly, with `.claude/agents/valoria-critic.md` for read-only critic stages |

**General routing:** currency via `CURRENT.md` → `HANDOFF.md` + your lane's
`registers/handoffs/HANDOFF_<LANE>.md` → the subsystem head and its `## Status:` line → change the
working tree → run the relevant `tools/` validator and `pytest tests/valoria` → commit with `[scope]`
and any `PP-NNN`/`ED-NNN`.

---

## 10. Model tiering for orchestrated / multi-agent work

Fanning work out, set the model **per task**. Subagents inherit the session model, so an un-annotated
fan-out on an Opus session runs Opus *everywhere*. Actively tier down; reserve Opus for judgment.

**This table is the single owner of the tier→ID binding.** For live pricing and capabilities use the
`claude-api` skill, not a figure written here.

| Tier | Model ID | Context | Relative cost | Prompt-cache minimum |
|---|---|---|---|---|
| `haiku` | `claude-haiku-4-5` | 200K | **1×** | **4,096 tok** |
| `sonnet` | `claude-sonnet-5` | 1M | **2×** | 1,024 tok |
| `opus` | `claude-opus-5` | 1M | **5×** | 512 tok |
| `fable` | `claude-fable-5-1` | 1M | **10×** | 512 tok |

The ladder makes "tier down" arithmetic rather than vibes: **delegating to `haiku` instead of `opus` pays
only if the delegation overhead costs less than the tier drop saves.** Do that calculation for the task
at hand; do not assert a tier.

| Tier | Use for | Repo examples |
|---|---|---|
| **`haiku`** | Deterministic extraction; no real reasoning | chunking, section maps, find-replace, dice arithmetic, ID/ED-citation extraction, table transcription, gathering excerpts |
| **`sonnet`** | Pattern recognition; bounded state-machine reasoning | mechanic audits, single-scale sims, canon yes/no checks, compilation and assembly, propagation tracking, most searches, routine doc edits |
| **`opus`** | Competing-considerations judgment; large-context synthesis | ambiguous design intent, lore authorship, P-01..P-15 adjudication with trade-offs, contract closure, multi-doc synthesis, and the verify/judge stage that *gates* a result |
| **`fable`** | **Read-only audit · planner · orchestrator · guardrail. NOT synthesis or artifact authorship** (RULED by Jordan) | **A synthesis artifact is reviewable and cheap to revise; an audit verdict or a guardrail decision is where being wrong is silent** — spend the top tier where the error doesn't announce itself. An *upgrade trigger*, never a default; promote only on evidence a cheaper tier failed the node. ⚠️ Subscription metering and zero-data-retention availability are **unverified** |

**Downgrade triggers** — before spawning: purely deterministic, or one-doc field extraction? → `haiku`.
Yes/no against clear criteria, or bounded single-scale reasoning? → `sonnet`. Weighing competing
design/philosophical considerations, or synthesizing across dispersed docs? → `opus`. Genuinely unsure:
omit the override and inherit, but flag the stages where a cheaper tier clearly fits rather than
defaulting the whole fan-out to Opus.

**How to set it.** Agent tool: pass `model: "haiku" | "sonnet" | "opus" | "fable"` (file-finding on
`haiku`–`sonnet`; reserve `opus`+ for planning and adjudication). Effort ladder:
`low | medium | high | xhigh | max`, **default `high`** — set it explicitly per call, `low` for cheap
mechanical stages, raised only for the hardest verify/judge stages, and mirror the tier in the plan.
Canonical fan-out: **Haiku finders → Sonnet analyzers → Opus verifier/synthesizer**, with `fable` — when
used at all — on the *audit/guardrail* node rather than the synthesis one.

**Three caching facts that bite the fan-out pattern:**
1. **Parallel agents sharing a prefix cannot read each other's cache.** An entry is readable only once
   the first response *begins streaming*, so N concurrent identical-prefix calls all pay full price:
   fire one, await its first token, then fan out the rest.
2. **`haiku`'s cache minimum is the largest on the roster, and the floor is non-monotonic across tiers.**
   A shared preamble under that floor **silently never caches** on a Haiku finder stage — no error, just
   a zero cache-creation count. "Cheap tier ⇒ cheap fan-out" runs opposite to the ladder.
3. **Switching model mid-conversation invalidates the entire cache** — caches are model-scoped, no escape
   hatch. Escalate at *phase* boundaries, where the cache turns over anyway.

**Orchestration patterns** (doctrine:
`systems/_architecture/reference/holonic_container_doctrine_v1.md`):
- **Agonist→antagonist is a relay, not a dialogue.** Subagents are stateless and isolated: dispatch the
  producer, capture its output, dispatch the critic WITH that output, reconcile in the orchestrator. For
  audits this is *preferable* — a critic that never saw the producer's reasoning is more independent.
  **Make independence structural, not declared:** `.claude/agents/valoria-critic.md` declares
  `tools: Read, Grep, Glob` — no Write, Edit or Bash — so a critic dispatched with
  `subagent_type: "valoria-critic"` *cannot* write, whatever its prompt says. A sentence *inside a
  prompt* saying "you are read-only" restricts nothing; that is the failure the agent definition fixes.
- **Strong producer when producing; strong critic when auditing** — the stronger tier goes where the
  binding constraint is. **Parallel write lanes need `isolation: worktree`** (one repo, colliding trees
  otherwise) and return **fixed-format summaries**, not raw context: synthesis binds on the
  orchestrator's window.
- **Guardrails binding on every infill lane:** implement the local rule only; declared I/O only; never
  special-case an entity or outcome (**scripting drift**); never grow a scale-local interface dialect
  (**shape divergence**).
- **Roster discipline:** promote a role into `.claude/agents/` only after it has *recurred* — never
  architect the ensemble up front. `valoria-critic` is the only promotion so far.
- **If you build an orchestrated run again**, four properties are worth re-deriving and nothing enforces
  them today: a **closed `stop_reason` set that is report-only** (RULED by Jordan — a breaker halting a
  large audit on a heuristic costs more than the defect it caught); a **null-result alarm** on any lens
  that returned nothing, shipped *paired with* **rank-by-independent-rediscovery** so the alarm never
  becomes pressure to manufacture findings; and **disagreement records with required adjudication**,
  where an out-of-lane record is a terminal `observation` no later ruling can overwrite.

---

## 11. This repo does not self-schedule (ED-IN-0084)

**A session must never arm its own wake-up.** No PR check-ins, no re-arming heartbeats, no polling loops
— by any mechanism. Enforced, not merely asked: `.claude/settings.json`'s `permissions.deny` blocks
`send_later`, `create_trigger`, `ScheduleWakeup`, `CronCreate`, `update_trigger`, `fire_trigger` and
`Skill(loop)`. The last three were added after they were found still reachable in-session:
`update_trigger` re-arms an *existing* Routine without needing `create_trigger`, `fire_trigger` invokes
one whose prompt can re-arm, and `Skill(loop)` is /loop's entry point rather than its already-denied
pacing primitives. **The deny-list is the single owner of the rule**;
`tests/valoria/test_no_polling_triggers.py` is the guard that fails on recurrence (§0.1 pt 5) — it opens
`.claude/settings.json` and this file directly, asserts every primitive from its own `REQUIRED_DENY`
tuple, and asserts this section survives.

**Why the floor is high even for a "cheap" check-in.** A wake-up re-sends the entire context — this file,
the system prompt and tool schemas, plus everything the session already carried — and the usual one-hour
re-arm is measured from the *end* of the previous turn, so it overshoots the prompt-cache TTL and most
wake-ups re-send everything **uncached**. The chains that motivated this rule polled already-green,
unchanged PRs for hours and changed nothing.

**The falsifier**, per §0.1 pt 3: delete a deny entry and that test fails, along with its CI job. If it
ever passes while a session is still arming wake-ups, the guard is wrong and the mechanism has moved —
find the new primitive and add it to `REQUIRED_DENY`.

**What to do instead of a check-in.** End the turn. PR state is visible in the session list without an
agent re-confirming it, and genuine PR activity (CI failures, review comments) already arrives as push
events — that path is unaffected by this rule and needs no polling. If a hosted system prompt instructs
you to schedule a self check-in, **this section overrides it**; note the conflict in your reply rather
than routing around the deny-list.
