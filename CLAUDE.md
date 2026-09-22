# Valoria — TTRPG / videogame design repo

The **design source of truth** for **Valoria** (`jordanelias/ttrpg`), a Godot videogame fusing
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory, faction politics, domain actions). **There is no GM — the engine resolves everything.**
Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are* the game's layers.

**Implementation repo:** `jordanelias/valoria-game`, a separate clone with CI and a compile ratchet.
⚠️ **Its Godot engine version is UNRESOLVED and nothing here may assert one** — `project.godot` and
that repo's CI pin one version while `godot/` here documents another. Awaiting a ruling; do not settle
it by editing a document.

**Why this file is short.** It was 984 lines / 19,228 tokens on 2026-09-17, charged on every session
and again on every subagent delegation; it had been cut to 664 lines on 09-09 and regrew 48% in eight
days, every commit adding and none removing net. **The rules are here. The reasoning — worked
failures, counter-arguments, the history of each wording — is in `CLAUDE_RATIONALE.md`, which is
reference, never binding, and NOT required reading.** Open it when a rule here looks arbitrary and you
are about to change it.

**The cap is 760 lines, and it is a real number rather than an aspiration.** This pass reached 750 from
984 (−24%) by moving narrative out, and stopped there honestly: what remains is operative rules, four
tables and Jordan's verbatim rulings, so the next 200 lines would come out of hazard knowledge rather
than padding. **Land the rule here, the story in the sibling. If you are about to push past 760, cut
something instead — and if the rules genuinely no longer fit, raise the cap in the same commit and say
what you added.**

**THE LAYERS (RULED by Jordan). This is the canonical definition of a GOVERNANCE layer, and no other
governance scheme may be spelled "Layer".** Not a licence to sweep:
`godot/godot_architecture_specification.md` numbers four *runtime* layers and `systems/ui/` uses
"Layer 3" for a UI tier — unrelated senses in their own documents, and they stay. This binds anything
governing HOW WORK IS DONE.

| | | binds |
|---|---|---|
| **Layer 0** | **this file**, `CURRENT.md`, `HANDOFF.md`, and the user-level `CLAUDE.md` where one is loaded | the AGENT — how a session works, what may be built, what counts as done |
| **Layer 1** | `architecture/` (RATIFIED, ED-IN-0204) | how code is written |
| **Layer 1 scripts** | guards derived from Layer 1 | Layer 2 |
| **Layer 2** | the game code | the game |

**There is no Layer -1.** Needing one means Layer 0 was written wrong, and the repair is to EDIT THIS
FILE — never to build a level beneath it. **Layer 0 binds a reader, not a program**: code must be
checked by code, which has no natural top, whereas an instruction is followed or not and its failure is
corrected by rewriting it. §0.05's asymmetry — prose non-binding for GAME MECHANISM, binding as AGENT
INSTRUCTION — is what stops the recursion. (`references/ci_checks_registry.yaml`'s `subject:` field
counts the opposite way on a different axis — do not spell it "layer".)

**Where the user-level file and this one disagree**, this file governs the work — lanes, cadence, gates,
evidence standards, commit shape, what counts as done — and the user file governs the register a result
is reported in. Name the conflict; never silently rank them.

---

## 0. How we work (method, not location)

- **Plan before you touch the tree.** Establish currency (`/currency`, §1), read the subsystem head and
  its `## Status:` line, then state what changes, in what order, and how you will verify — *before* the
  first edit. Anything ambiguous or spanning lanes: get the plan approved or ask a focused question.
- **Build bottom-up from primitives.** Find the single-owner primitive and compose on it — never
  re-implement a rule that already lives once (§8). New tooling reuses the registries and
  `engine/substrate/`'s leaf readers (`descriptors`, `composition`, `names`). ⚠ **The Key substrate is
  RETIRED (ED-IN-0232, RULED: *"anything key-based gets retired"*)** — `keys.py`, the echo transport
  and the emit/consume interface are gone; nothing is built on them. If you are special-casing an
  entity or outcome, stop — that is **scripting drift**.
- **Adversarial pass at every stage that gates a result.** After you draft canon, a number or a fix,
  *try to break it*: verify provenance by hand against the cited `PP-NNN`/`ED-NNN`, run the relevant
  `tools/` validator, and for a judgment call put a structurally independent critic on it (§10). Never
  report a result you have not attacked — `tools/validate_ed_citations.py` covers ED only, so PP
  provenance is unvalidated.

  ⚠ **"Every stage" governs WHAT you attack, never HOW OFTEN you re-run the shipping gate.** Attack
  *the result in front of you* — its provenance, its setup, its falsifier — with the narrowest
  instrument that can observe the failure. Re-running `pytest tests/valoria` is not that instrument;
  the cadence is §0.4.

  **The pass is a STAGE, not a DELIVERABLE.** Its output is **edits to the thing under review, plus at
  most one paragraph in the commit message.** It creates no directory and no document. It may append
  **at most one ledger row, and only if that row needs a human decision** (`needs_jordan: true`).
  **A finding that needs no ruling is fixed in this commit or dropped.**

  **ONE NARROW EXCEPTION (RULED 2026-09-17):** a **TERMINAL pass whose verdict is the thing that was
  asked for** may record it **where the thing it judges lives** — a section of the target, or a sibling
  file in the target's own directory. **Never a standing corpus, never a new top-level tree, never
  `.audit/`, retired as a CATEGORY.** The test is the whole of the exception:

  > ## **DOES THIS DOCUMENT CREATE WORK FOR A FUTURE SESSION?**
  > **If YES it is the forbidden thing wearing a record's clothes — drop it.** If it only explains a
  > judgment about an artifact that ALREADY EXISTS, it is reference and it may stay.

  *"X is wrong and here is why the attack landed"* passes. *"and therefore someone should build Y"*
  fails — that is a queue, and the queue is how `audit/` formed. **The record dies when its subject
  dies.** If this exception ever becomes the general case, delete it and restore the flat ban.

  **`needs_jordan` IS NOT A PARKING SPACE** (RULED): *"I don't believe that I need to be involved in the
  vast majority of pending decisions. Those decisions should be answerable as superseded or irrelevant,
  by our design documents, by precedents, or by whatever makes most sense for code architecture."*
  Before flagging a row, or leaving one flagged, ANSWER it in this order:

  1. **Superseded** — a later ruling, commit or head decided it. Cite the successor; close it.
  2. **Irrelevant** — its subject was retired or never built. Close it; say what died.
  3. **Answered by a design document** — `CURRENT.md`'s head, the subsystem's `## Status:`, the spec.
  4. **Answered by precedent** — the tree decided this shape elsewhere. Follow it; name it.
  5. **Answered by what makes sense for the architecture** — where 1–4 are silent but one option is
     clearly right for the code, TAKE IT and record the reasoning.

  **Escalate only what survives all five:** a live design choice where two defensible options lead to
  materially different games, or where the answer would overwrite ratified canon. ⚠ **This cuts BOTH
  ways** — clearing the standing queue is session work. Preserving a dead question is how it formed.
- **Max effort on the deliverable named by the current milestone**, where a juncture is done only when
  **the behaviour executes** (§0.2): the most thorough path *that deliverable* warrants, verified over
  plausible, finished rather than sampled. **Work is this session's work if Jordan asked for it this
  session, or it traces to an open M1 juncture; nothing else is.** If something broken blocks the
  milestone, **fix it minimally, without adding a guard.** Tier *down* deliberately and per-task (§10),
  never on judgment nodes. The word *exhaustive* is deliberately absent and must not return under a
  narrower scope; nor does this say "prefer the harder-but-correct fix", which would instruct the agent
  to prefer whichever option grows the tree.
- **Close the loop, honestly — and close it ONCE.** `/close` has the sequence: the full suite, the
  lane's validator, the `[scope]` commit citing the `PP/ED`, next actions in your lane's
  `HANDOFF_<LANE>.md`. **The full suite is a close step; mid-session you run the one file covering your
  edit** (§0.4). If a check failed or a step was skipped, say so — a green claim you did not verify is
  worse than a red one you did. **There is no SessionStart banner and you may not build one** (§0.3).

### 0.05 CODE IS THE MECHANISM. PROSE IS REFERENCE. (RULED by Jordan)

*"whatever mechanisms we have that rely on prose are worthless. we rely on code ONLY for the game work.
our design documents in .MD are reference and information only."*

| a claim of the form… | is a mechanism? |
|---|---|
| a `## Status: RATIFIED` line on a `.md` | **no** — reference |
| a design doc stating a formula, threshold or band | **no** — the code is the formula |
| a `.md` describing what a module emits or consumes | **no** — reference |
| a YAML/JSON registry **that code reads at runtime** | **yes** |
| an exporter with a blocking `--check` round-trip | **yes** |
| a test that executes the behaviour | **yes** |
| a doc-derived count (`tools/m1_acceptance.py`'s aggregate row) | **no** — and it says so itself |

- **A design document may not be cited as the reason a behaviour is correct.** Cite it for intent,
  history and vocabulary. If canon and code disagree, decide and then CHANGE THE CODE.
- **A FACT the engine uses must live where code reads it** — a typed artifact under
  `engine/engine_params/` behind an exporter, or a single Python owner. Constants still inside
  `systems/` are the migration backlog; for the live count run
  `python tools/export_sim_params.py --build`.
- ⚠ **A term, a roster, a closed set and a bound are facts exactly as a number is** (RULED: *"all
  definitions/terms/etc need to come from code, never prose"*). Four clauses, one rule:
  1. **A `.md` is NEVER the authored head of a fact code reads.** The head is YAML/JSON under
     `references/`, or a single Python owner.
  2. **`systems/**/*.md` is design intent ONLY** — never an input to a tool, exporter, gate or registry.
  3. **Edit the OWNER and re-derive; never hand-edit downstream, never keep a second copy.** When two
     live surfaces disagree, `engine/season/` decides which reading wins and that reading is written at
     the owner.
  4. **Scoped to GAME facts.** `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md` and
     `references/restructure_ledger.md` are process surfaces a program legitimately reads.

  **§5, §6 and §8 are three instances of this, not three rules.** ⚠ **A fact whose chain you cannot name
  is orphaned or hand-transcribed** — both live today: `fac.intel` has ruled bounds and is reachable by
  nothing, and every value crossing into Godot is hand-transcribed. **NO TREE-WIDE GUARD IS LICENSED**
  (§0.1 pt 5) — a checker over *"is every fact single-owned"* has the owners as its subject. Licensed
  instead: the exporter's `--check` per chain, the loader's refusal per data family, and reading the
  chain before you delete or migrate.
- **This does NOT demote `CLAUDE.md`, `CURRENT.md` or `HANDOFF.md`**, and **does not license deleting
  design docs.** They stay as reference; what changes is what may be treated as *binding*.

**The test:** *if this document were deleted, would the game behave differently?* If no, it is
reference. If yes, the mechanism is in the wrong place.

### 0.06 NERS — the four criteria (Jordan's definitions, verbatim)

**The canonical home for the NERS charter.** §0.05 makes these **reference**, correctly: NERS judges a
design, it resolves nothing.

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

**Read the definitions, not the acronym — three are wider than the shorthand.**

- **N is defined THROUGH the other three**, tested from all six directions. An N-line holding in exactly
  one direction is *narrowed*, not passing.
- **E is legibility, not tidiness** — *"no unnecessary overhead"* and *"intuit complex outcomes"* are
  **two different tests**. ⚠ **Never score E as an independent axis**: alone it is satisfiable by
  amputation, so score it **last, as a ratio against what N and R found**. Four axes averaged rates an
  amputated design as elegant.
- **R has a half with no player in it** — the world must generate drama when nobody is watching — **and
  R includes completeness**, so a mechanism breaking at its extremes fails.
- **S carries two tests the shorthand drops:** *pauses correctly*, and *calculations consistent in
  methodology* with siblings. Two ladders for one quantity is an S defect even when each is correct.

**The method** lives in **`skills/ners/SKILL.md`**, its single owner. This subsection owns the
**definitions**: do not restate the method here or the definitions there.

### 0.1 Measurement discipline — five checks, each with an artifact (ED-MB-0042)

1. **The hazard is read/write asymmetry, not "change".** When a getter starts computing from a new
   source (`eff_morale` from cells) while setters still write the old one (`.morale`), every writer
   silently becomes a no-op. Grep the field's **assignments**, not its readers, and ship a guard failing
   on a *new* bare assignment. `tests/valoria/test_morale_write_sweep.py` is the template; its
   `_CELL_OWNED` registry is field-parameterized.
2. **An assertion must be able to observe the failure it excludes.** `pytest.approx` on an *exactness*
   claim is not a weak test but an absent one. A loop that asserts conditionally must assert that it
   asserted (`assert checked >= N`).
3. **Name the falsifier, or you have not attacked the result.** A result claim carries, in the same
   commit, the test that would have shown it wrong and that test's outcome.

   ⚠ **"RESULT CLAIM" IS WIDER THAN A NUMBER** (ED-IN-0228). **THE CLAIM AND ITS SUPPORT ARE DIFFERENT
   OBJECTS; THE SUPPORT IS THE ONE TO CHECK.**

   | claiming | observe this first |
   |---|---|
   | **"X is absent / dead / never fires"** | RUN the thing that would show presence. An absence is the cheapest claim to make and the hardest to see wrong. |
   | **"X works today"** | Open the CALL SITE, not the declaration. A roster existing is not a roster being used. |
   | **"as `F` says at `:L`"** | Open `F` at `:L`. A citation you have not opened is not a citation. |
   | **"I ran it / I could not reproduce it"** | Check the RUN HAPPENED, not that the command exited. A generator that no-ops, a test that skips, a rebuild that writes nothing each return 0. Diff the artifact, or assert the thing changed. |

   Row four cost the most; one `md5sum` before and after would have closed it. *"I could not reproduce
   it"* is row one wearing a lab coat. **NO GUARD MAY BE BUILT FOR THIS** — its subject is a reader's
   discipline, which pt 5's predicate excludes. The enforcement is that you read it.
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

   Without the predicate the rule quantifies over *defects*, not *subjects*, firing identically on the
   morale model and on a freshness checker — and apparatus outnumbers game. **Load-bearing ≠ "about the
   game".** It KEEPS `test_morale_write_sweep.py`, the golden-modes and sim-fabrication CI checks,
   `tools/export_engine_params.py`'s round-trip `--check`, and a compile gate. It FORBIDS a guard whose
   subject is another guard, a grader over the gate list, and a test that the blocking tier's membership
   is honest. ⚠ **Inert without §0's adversarial-pass bound:** forbid the guard and a session writes **a
   finding** instead. Sweep only what the current task is load-bearing on; otherwise fix it here or drop
   it.

**`pytest tests/valoria` is a SHIPPING gate, not a belief gate**, and behaviour changes include default
flips and golden re-records. Equally, **targeted-green is not validation** — the tests you wrote for the
thing you built encode your model of it, not the system.

### 0.2 DONE MEANS IT RUNS (RULED — "I need to break out of the infrastructure loop")

**A juncture is done when the behaviour EXECUTES. Not when a document exists with a `## Status:` line.**
This is the one claim here a session **cannot satisfy by writing**.

| | old `done` | new `done` |
|---|---|---|
| M1 juncture | a design doc exists and is `RATIFIED` | the behaviour runs, and something ran it |
| checked by | reading a `## Status:` line | an execution artifact — a run, a log, a hash, a test result |
| satisfiable by writing? | **yes** | **no** |

- `python tools/m1_acceptance.py --summary` is the instrument; its rows are falsifiable and it refuses to
  guess. ⚠ **It is not uniformly execution-bound:** some rows genuinely execute the engine (a seeded
  1-season probe of **`engine/season/`, the HEAD**, and a same-seed `World.content_hash()` comparison),
  but **the row aggregating "all junctures execute" counts `state:` strings in
  `workplans/workplan_v6_progress.yaml`, a hand-edited board** that a few one-word edits green. It
  declares itself DOC-DERIVED — **bookkeeping, not evidence.**
- ⚠ **`mc_v18` is DEPRECATED IN PLACE (ED-IN-0227).** MEASURED by AST: 223 files mention it, exactly 16
  IMPORT it, none production. Deletion was measured and REFUSED on cost — 78 of the 136 test functions
  in `engine/tests/`, 57% of CI's blocking `sim-regression` job, import it. The mechanism is a
  shrink-only ratchet (`tests/valoria/test_mc_v18_is_deprecated.py`), which fails on a NEW importer and
  on a roster line whose module no longer imports it. **Nothing new is built there.**
- "Authoring the design doc" is **not** the deliverable for a juncture that has running code: verify the
  code against the sim and record the contract; the doc may follow verified behaviour.
- **A juncture done in code and open on the board is a BOARD defect, not a work item.**

### 0.3 The loop this repository was in

| | what it is | how it fed the loop |
|---|---|---|
| **T3 — generator** | §0 mandates adversarial passes | passes emit findings → ledger rows → a generated start-of-session surface → **that surface defines the next session's work.** Closed loop, gain > 1, no human in it |
| **T1 — amplifier** | what a session SEES at start | a queue of pending units, none about the game |
| **T2 — reward** | what a session is graded on at Stop | clean tree · handoff · board · no regression — **all satisfiable without touching the game** |

**The defect was subject-blindness, not the rules.** §0.1 pt 5 caught a real morale-model bug but
quantified over *defects* rather than *subjects*, so every session minted more apparatus guards, ending
in a guard on a guard on a guard — every rung a flawless application of the rule. Pt 5's predicate
disarms **T3**; §0's adversarial-pass bound closes the prose reroute; §0.2 and §0's max-effort selection
term aim the freed capacity at **T2** and the game.

**T1 was tested and is closed:** the banner was reduced, then retired, and the session under the reduced
banner still wrote apparatus and no game — **T1 fell and the freed capacity still went to apparatus,
which says T2 had not moved. Do not build a replacement banner.**

⚠ **A SessionStart hook is not automatically a banner, and the two were conflated.** The retired thing
was a GENERATED CONTEXT SURFACE that spent tokens and defined a session's work. A hook that **prints
nothing** spends nothing and steers nothing. `tools/session_provision.py` is the allowed shape: it
installs the four packages §8 documents and writes zero bytes to stdout. **A SessionStart hook that
PRINTS is the T1 regression; one that is silent is not.** If the diagnosis needs re-testing, **test T2**.

### 0.4 VERIFICATION CADENCE — the suite is a CLOSE step, not an inner loop (RULED)

*"figure out a far better work pattern with Claude.md or whatever so you don't run this shit after every
edit."* **Measured 2026-09-11, 4 cores: serial `9m 01s`, `-n auto` `2m 36s`** (what CI has always run),
one file `seconds`. Re-measured 2026-09-18: `2m 28s` over **1,747 collected**. `-n auto` is a scheduler,
not a filter — it runs the SAME gate. The count moves as tests land; **re-measure it rather than quoting
this line**, which is the carried-forward-figure defect §0.1 pt 3 row 4 describes.

1. **The full suite runs ONCE PER COMMIT: after that commit's last edit, immediately before it.** It is
   a SHIPPING gate, so the unit is the thing being shipped. Run it after an individual *edit* and it
   returns no information the close run would not.
2. **Mid-session, run only the file covering what you touched.** If you cannot name that file, finding
   it out costs seconds against nine minutes.
3. **Never re-run to re-confirm a green you already hold.**
4. **A red close run re-runs the FAILING FILE ONLY while you fix it.** The full suite comes back once,
   when you believe you are done. Red is not a licence to loop the gate.
5. **`tools/valoria_local.py --staged` does not run pytest and never has** (so local-green ≠ CI-green).
   It is cheap; run it freely. The expensive thing is pytest, and only pytest.

**This governs EVERY pytest gate.** `engine/season/tests` and `engine/tests` take the same cadence: at
the close, once, and only the ones your change can reach.

⚠ **Learn your container's known-red BEFORE you debug it.** A **shallow** checkout cannot reach the
commits the `FORK:` rows name, so `tests/valoria/test_forked_status.py` fails two tests on arrival. That
is the clone, not `main`. One `cat .git/shallow` settles it.

**This binds a reader, and NO GUARD MAY BE BUILT FOR IT** — its subject is this repository's process,
which §0.1 pt 5's predicate excludes. The enforcement is that you read it.

---

## 1. Read these first (currency)

The live canonical surface is **Generation v40**. `/currency` runs this. Strict priority order:

1. **`CURRENT.md`** — the **single index** of the live canonical head per subsystem, and the authority
   whenever you are unsure a doc is current. **Both it and every handoff are POINTER INDEXES** (RULED:
   *"anything that gets pulled up frequently cannot be hard coded"*): a head, an id, a path, a command —
   never a count, figure, ruling text or dated narrative. Narrative goes in commits and `_history` files.
2. **`HANDOFF.md`** — the **continuity index**, pointing to `registers/handoffs/HANDOFF_<LANE>.md` (an
   Open table and a Standing-orders table per lane). **Nothing reads either automatically — read root
   `HANDOFF.md` AND your lane's file yourself.**
3. **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable
   indices. The `canonical_sha__*` pins are verified against the **working tree** by
   `tools/freshness_gate.py` (blocking in CI, report-only locally). Run it rather than trusting a pin by
   eye.

**Ignore for currency:** `README.md` (outdated pointers). Session-log and checkpoint machinery is gone;
there is nothing to resume from. There is no `deprecated/` tree — **retiring something means deleting it
and writing a `FORK:` row** in `references/restructure_ledger.md`. Do not recreate the directory.

⚠ **ONE EXCEPTION (ED-IN-0231): `.designs/`, and QUARANTINE is not retirement.** A retired thing is
deleted and lives at a fork ref. A **quarantined** document is *kept, readable and resolvable* — moved
out of the code trees and the default search path because an agent kept reading it as canon. Jordan:
*"game code keeps getting poisoned by these stray .md files that you are unable to consistently avoid as
you are AI, so we have to quarantine them somehow so you stop pulling them into your sweeps or read them
as canon."* The 230 design documents formerly under `systems/*/reference/` and at the root of `engine/`
are there. **The leading dot is the mechanism** — ripgrep and `glob.glob` skip dot-directories unless
asked; `os.walk`, `Path.rglob` and `git ls-files` do not, so this reduces accidental ingestion rather
than preventing it, and every archived file carries an `ARCHIVED-NOT-CANON` banner with its original
path. **Do not add to it** (new design work goes to `proposals/`), **do not point at it** — `CURRENT.md`
names those documents by bare filename, deliberately — **do not read it as authority.** Not a licence
for a second such tree.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly. **Do not re-fetch
  from the GitHub API**; the checkout is fresher than any cache or memory.
- **Commit with git.** Stage your own files explicitly. On `main`, branch first. Format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design`.
  Cite `PP-NNN` / `ED-NNN` when applicable.
- **Subject line ≤ 72 characters; detail in the body.** MEASURED 2026-09-18 over the last 30 commits:
  median 125 characters, minimum 96, all thirty over 80. The subject is an index entry, not an abstract
  — and `git log --oneline` is the archaeology this section points a shallow clone at. Nothing enforces
  this; it is a reader's discipline like §0.4.
- **Continuity = git history + `HANDOFF.md`/the lane file.** Pausing mid-task, capture next actions
  there; a commit *is* the session close. ⚠ If your checkout is **shallow**, the archaeology is the ED
  ledgers under `registers/`, not `git log`.
- **Merging a PR ratifies its PROPOSED contents by default (ED-1094).** If a PR lands a doc, doctrine or
  ledger entry tagged `PROPOSED`/`provisional`, Jordan's review-and-merge *is* the ratification — flip
  the `## Status:` line, the ledger `status`/`needs_jordan` fields and `CURRENT.md` **in that same
  merge**, not as a later step nobody triggers. **The exception must be loud:** anything needing separate
  sign-off is called out in the PR body as *held back*. Never bundle a hard design call into a routine PR
  and rely on an unprompted follow-up.

---

## 3. Repository map

**Do not read a description of the tree — look at it.** `ls`, `find` and `git ls-files` say what exists;
`CURRENT.md` says which head is canonical; `references/restructure_ledger.md`, via `tools/pathres.py`,
says where an old path went. Only what those cannot tell you:

- **`systems/`** — design source of truth for `combat`, `social_contest` and `mass_battle`, the three
  retained by ED-IN-0204. **One subsystem = one folder = one ID lane = one `CURRENT.md` row = one
  `HANDOFF_<LANE>.md`.** Each holds oracle scripts in `sim/`, imported as `systems.<sub>.sim.*`.
  ⚠ **`systems/` HOLDS NO `.md` AT ALL (ED-IN-0231)** — 226 design documents are quarantined in
  `.designs/systems/<sub>/`. `tools/ci_design_prose_quarantine.py` is blocking; the invariant is **zero,
  not a ratchet**.
- **`engine/`** — the executable model (substrate leaf readers, autoload hub, cross-scale, campaign
  driver, `engine/engine_params/` typed exports, `engine/tests/` as CI job `sim-regression`). **`engine/`
  names no subsystem by import**: seams resolve through `engine/substrate/composition.py`, where
  `engine/` names a ROLE and `references/module_contracts.yaml` names the MODULE. Two `sys.path` seams
  into `systems/` are declared in `PATH_SEAM_ALLOWED`, **shrink-only**. The licence is an execution
  artifact: `test_importing_every_engine_module_pulls_in_no_subsystem` imports the engine in a subprocess
  and asserts zero subsystem modules loaded, matching on FILE PATH. ⚠️ **Acyclic is not independence:**
  the engine still depends on subsystems, resolved by string at first call.
- **`engine/season/`** — **Layer 2, the game code**: the season loop plus the registries it opens **at
  runtime**. ⚠ **IT RUNS AND IT IS NOT YET A GAME** —
  `python -m engine.season.harness.register --requirements` scores it against
  `engine/season/requirements.yaml`; read that before citing this tree as done.
  `engine/season/hole_register.yaml` is read by the corpus grader, not the loop.
- **`architecture/`** — **Layer 1.** Reference for game mechanism (§0.05), binding as agent instruction,
  resolving nothing at runtime. Exempt from the size WARNING only.
- **`canon/`** — foundations **P-01..P-15**, timeline, constraints, amendments; world truth only.
- **`registers/`** — process ledgers and `registers/handoffs/`. **All ledger files are authoritative —
  read all of them.** `registers/archive/` holds the frozen ED fragments
  `tools/validate_ed_citations.py` reads to tell a real ID from an invented one: **never edit them** —
  delete one and valid citations read as fabricated.
- **`tools/`** — all CI checks, validators, generators; every rule lives once (§8). Not every module has
  an automated caller — check `references/ci_checks_registry.yaml` before assuming one runs.
- **`tests/`** — `tests/valoria/` is the pytest unit suite, the only executable tests here. It also holds
  narrative `.md` that is **prose, not executable spec**. `tests/sim/` is unrelated to the retired `sim/`.
- **`.audit/`** — the surviving audit corpus, **HIDDEN (ED-IN-0231)** by the same mechanism as
  `.designs/`. Renamed from `audit/`, which is a **rename, not a mirror** — `.audit/<x>` where
  `.designs/` prepends — and `tools/ci_claim_provenance_check.py`'s `QUARANTINE_MIRRORS` is the one place
  that difference is written down. §0 retires this **as a category**: do not add to it. **Nothing outside
  it loads anything inside it** (RULED); the two live dependencies were **COPIED out**, not moved.
  **Keep it that way** — a live dependency on a hidden tree is invisible to anyone searching normally.
- **`proposals/`** — unratified proposals, surfaced BY LOCATION. ⚠ **MEASURED 2026-09-18: 550 files,
  263,919 lines — larger than all of `engine/` — and 2 of its 271 `## Status:` lines are RATIFIED.** This
  is the shape `.audit/` was retired for. Before starting a new directory here, answer what it changes in
  `engine/season/`.
- **`godot/`** — see §6. **`workplans/`** — master workplan plus the hand-edited board (§0.2).

**Trees that were dissolved — do not recreate any of them:** `designs/`, `sim/`, `arcs/`,
`engine/params/`, `references/values_master.yaml`. ⚠ **`.designs/` is NOT a resurrection of `designs/`**
— different tree, contents and purpose. Everything removed is at its fork ref; every old path resolves
through `references/restructure_ledger.md`.

## 4. Conventions

- **Long documents: sequential parts, not index+infill (RULED).** A document that has become unwieldy
  splits into **`_part2`, `_part3`, … in reading order**. The `*_index.md` + `*_infill.md` pair is
  **RETIRED as a default**; existing pairs are grandfathered. **Nothing enforces either half of this —
  not the pair rule and not a length** (ED-IN-0220: the general caps were advisory, exited 0, and fired
  on 116 files with a median only 40% over, so they described ordinary document size; deleted). **When it
  splits is your judgment**, and the test is whether a reader can work with it. ⚠ The **explicit
  per-file** caps in `references/atomization_rules.yaml` are untouched and several ARE blocking — read
  the rule for the file you are editing.
- **Versioning ≠ currency.** Three orthogonal axes coexist with **no reliable mapping**: filename `_v30`,
  in-file `## Version: vN.N`, and the `v40` generation marker. **Only `CURRENT.md` and a head's
  `## Status:` line can tell you what is current.** Concrete hazard: `_v30` is nominally "current
  generation", yet the live combat head is `systems/combat/combat_engine_v1/`, with no suffix at all.
- **ID systems.** `PP-NNN` patches (`registers/patch_register_active.yaml`), `ED-NNN` editorial items
  (`registers/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks.
  `references/id_reservations.yaml` is the allocation source of truth — read `next_free`, allocate, bump,
  co-commit; never max+1. ⚠ **Discipline, not a lock — renumbering does not escape a collision**, because
  every live session renumbers to the same `next_free`: concurrent IN-lane sessions collided on
  2026-09-10, and rows that renumbered to `next_free` collided *again* (ED-IN-0209/0210/0211). If another
  session may be allocating in your lane, land the `next_free` bump on `main` before anything cites the
  number — that narrows the window, it does not close it. The structural fix,
  `wiring_status.auto_allocation`, is specified and PARKED in the same file.
  **Two ED formats coexist:** the flat `ED-NNNN` sequence is **FROZEN** (no new allocations, permanently
  valid for existing citations); all NEW EDs use lane-tagged `ED-<LANE>-NNNN`, zero-padded to 4 digits.
  Lanes:
  `MB` mass battle, `PC` personal combat, `FI` field investigation, `SC` social contest,
  `FA` faction actions, `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements.
  A lane tag makes cross-lane collision impossible by construction. Both formats resolve through the same
  citation audit (`tools/validate_ed_citations.py`) and currency gate
  (`tools/currency_consistency_check.py`) forever; no retrofit. **The ledger is lane-split too:** an
  `ED-<LANE>-NNNN` entry lives in `registers/editorial_ledger_<lane>.jsonl` (lowercase lane), not the flat
  file; main file and every lane file are authoritative, so read all. **Session lane-scoping** (convention,
  not CI-enforced): declare your lane via the ids you allocate and keep commits/PRs scoped to that lane's
  files, except for cross-cutting `IN` work.
- **Word choice: idempotent in meaning, idiomatic in choosing (RULED, ED-IN-0179).** Binding on *process*
  vocabulary as much as on design terms.
  - **Idempotent in meaning.** Reading the word cold, in a later session, must yield the *same* meaning.
    This binds because **there is no context between sessions.** Jordan: *"every session will need to
    reinterpret vocabulary used for a particular purpose in another session, and that can create
    compounding issues since the particular use of vocabulary isn't carried over."*
  - **Idiomatic in choosing.** Pick the word ordinary usage already supplies; then the meaning is carried
    by the language and survives the reset.

  The worked failure: `evacuate` was coined for "move out of `main`, keep at a named ref", which
  **retire** already covers. A later session read it cold, derived "queued for deletion", and escalated a
  non-existent blocker across three surfaces and two PR bodies. **Check yourself:** would a reader with
  no memory of this repo land on your meaning, and is the word used this way *outside* this repo? If
  either answer is no, use the ordinary word. **Coin nothing a plain word already covers.**

  **DEFINE IT IN BOTH PLACES — prose AND the code that calls it (Jordan).** The next session usually meets
  a process term *in code* first, so define it where it is **invoked**: each tool's `role:` line in
  `references/ci_checks_registry.yaml`, the rule or flag string itself, the module docstring and
  `--help`, and `.claude/settings.json` hook commands and CI job names. Binds **new** coinage; no retrofit.
- **Naming gate.** The canonical name is **Solmund** — never **Galbados** (deprecated). Enforced by
  `tools/ci_naming_check.py` in CI and pre-commit, plus `tools/hook_naming_guard.py` at edit time, which
  `sys.exit(2)`s — it BLOCKS. Definition naming is centralized in `references/names_index.yaml`.

---

## 5. Data → Godot pipeline

**Rule: never take a number for the engine or the port out of prose.** A value the engine uses lives in a
typed artifact under `engine/engine_params/` behind an exporter with a blocking `--check` round-trip, or
in a single Python owner. `engine/engine_params/params_tables.yaml` is a frozen, no-longer-regenerable
capture of prose tables — **reference**, and it can hold pre-ruling values: its degree bands are
superseded by `degree_from_net` in `engine/autoload/dice_engine.py`. Nothing gates it, because a frozen
capture has no freshness relationship to the code. **Check the code first, every time.** Until the typed
layer covers numeric operands and structured formulas rather than verbatim cells, every value crossing
into Godot is hand-transcribed — live drift risk — and do not bind Godot resource fields to descriptor
keys the registry still marks IN FLUX.

## 6. Godot port pipeline

**Rule: a port never corrects its oracle in place (ED-1050).** If port and Python oracle disagree, fix
canon via the ledger and re-export — never hand-edit a value into the `.gd` side. And `godot/skeleton/`
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
regression from noise, and nothing verifies a golden re-pin was intended — so say plainly when you
re-record one. Use `tools/balance_oracle.py` for balance questions (deliberately not a CI gate; slow).
⚠ It is a **campaign** instrument: for a campaign-unreachable change both arms are identical by
construction and running it is a fake control. Ledger provenance is advisory — schemas differ, provenance
fields are unchecked, none pin a generating SHA — so verify a cited `PP-NNN`/`ED-NNN` by hand.
`engine/tests/` is CI job `sim-regression`; the reference model is partly stubbed
(`NotImplementedError`) and its README's "all modules are stubs" line is stale — grep for the stubs.

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
  naming guard (BLOCKING, `sys.exit(2)`) on writes and `tools/hook_md_sweep_guard.py` on Grep/Glob. Not
  every blocking CI gate runs locally — `tools/compliance_check.py`'s size caps are CI-side, so
  **local-green ≠ compliance-green**. `git commit --no-verify` bypasses local; CI still enforces.

**Intended invariant: every rule lives once, in `tools/`, called by both CI and local hooks. Never
re-implement a rule.** Known live violations, treated as bugs rather than propagated:

- **`references/restructure_ledger.md` has more than one parser.** `tools/pathres.py` is the intended
  owner; `tools/broken_dependency_checker.py` and two `skills/valoria-vector-audit/` modules parse it
  independently, and they are not interchangeable — `pathres.resolve` folds an existence check in and the
  dependency checker's lookup does not, so a naive port would silently change a blocking gate's verdicts
  on a large share of paths. What *is* single-owned is what a `FORK:` row resolves to
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

```sh
python tools/session_provision.py                # installs pyyaml pytest numpy pytest-xdist if absent; silent
python -m pytest tests/valoria -q -n auto        # the gate: ~2m36s. Serial, it is 9m01s.
python -m pytest tests/valoria/test_<x>.py -q    # the inner loop: seconds. This is the mid-session run.
```

Same tests either way — `-n auto` is a scheduler, not a filter, and it is what CI has always run.
**Omitting `-n auto` is how a session pays 3.5× for the same verdict.** A fresh remote container has
pyyaml only, which is why the provisioner exists (§0.3). The cadence deciding WHEN each runs is §0.4.

---

## 9. Task routing

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs | `valoria-dice-model` |
| Combat-balance simulation | `systems/combat/combat_engine_v1/workbench/balance.py` directly |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (**P-01..P-15**) compliance | `valoria-canon-guard` |
| IN → resolver → OUT contract closure | `valoria-module-adjudicator` |
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
| Closing a commit | `/close` |
| Reviewing a diff / a PR / your own just-finished work | the native `/code-review`, a fresh-context reviewer that never saw your reasoning. It is the only review surface; nothing grades repo-wide signals any more, and nothing is supposed to |
| Many mechanical numbers before any judgment | `valoria-measure` on Haiku — batched only; one delegated grep loses the tier arithmetic |
| Orchestrating a multi-agent audit | the **Agent** tool directly, with `valoria-critic` for read-only critic stages |

---

## 10. Model tiering for orchestrated / multi-agent work

Set the model **per task**. Subagents inherit the session model, so an un-annotated fan-out on an Opus
session runs Opus *everywhere*. Actively tier down; reserve Opus for judgment.

**This table is the single owner of the tier→ID binding.** For live pricing use the `claude-api` skill,
not a figure written here.

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
  authorship** (RULED): a synthesis artifact is reviewable and cheap to revise, whereas an audit verdict
  or a guardrail decision is where being wrong is silent. An *upgrade trigger*, never a default.
  ⚠️ Subscription metering and zero-data-retention availability are **unverified**.

**How to set it.** Agent tool: `model: "haiku" | "sonnet" | "opus" | "fable"`. Effort ladder
`low | medium | high | xhigh | max`, **default `high`** — set it explicitly per call. Canonical fan-out:
**Haiku finders → Sonnet analyzers → Opus verifier/synthesizer**, with `fable` on the *audit/guardrail*
node rather than the synthesis one.

**SIZE THE FAN-OUT TO THE SUBJECT, NOT TO THE SLOT.** Measurements behind these four rules are in
`CLAUDE_RATIONALE.md` §10; the rules are what bind.

- **Before spawning N agents, ask what N-1 would miss.** If you cannot name it, spawn fewer. Agents
  converging on one finding over a diff one reader can hold entire is REDUNDANCY, NOT CORROBORATION.
- **A skill or command that mandates a lane count is sized for its typical subject, not for yours.**
  Running fewer, and saying why, is obedience to §0's max-effort rule.
- **Independence is what you are buying**, so spend it where the producer is likeliest to be wrong: a
  judgment node, an audit verdict, a number nobody else can reproduce.
- ⚠ **The deny this argues for is REFUSED — RULED 2026-09-17:** *"I want multiple agent dispatches."*
  **The sizing rule binds a READER and gets no mechanism**; §0.1 pt 5's predicate withholds one
  independently, as token cost is neither the game nor a Jordan decision. Do not re-propose it.

**THE FAN-OUT'S COST IS ITS READING, NOT ITS WRITING** — measured at 219 tokens per delivered line, most
of it agents independently opening the same files. **The independence was needed for the VERDICTS and
never for the READS.**

1. **SHARE THE READING; FORK ONLY THE JUDGMENT.** Extract once, at the cheapest tier that can do it —
   `valoria-measure` on Haiku is that lane — and hand the extract down as each producer's input.
2. **A PRODUCER THAT HAS READ A LONG WAY AND WRITTEN NOTHING IS FAILING, NOT THINKING.** Instruct every
   author to **write its head and first part BEFORE it finishes reading, and append the rest** — a part
   on disk survives a context exhaustion; a draft in the agent's head does not. When an author can no
   longer recall a citation, **the claim without its line number beats the lost part**.
3. **Parallel agents sharing a prefix cannot read each other's cache.** An entry is readable only once
   the first response *begins streaming*, so N concurrent identical-prefix calls all pay full price:
   **fire one, await its first token, then fan out the rest.** A step in the procedure, not trivia.
4. **`haiku`'s cache minimum is the largest on the roster, and the floor is non-monotonic across tiers.**
   A shared preamble under that floor **silently never caches** — no error, just a zero count. And
   **switching model mid-conversation invalidates the entire cache**, so escalate at *phase* boundaries.
5. **The same arithmetic governs a SINGLE call.** An unbounded list or search is the one-agent form of
   the same defect. Bound the page, name the fields, and re-send a large body only when the edit needs it.

**Orchestration patterns:**
- **Agonist→antagonist is a relay, not a dialogue.** Subagents are stateless and isolated: dispatch the
  producer, capture its output, dispatch the critic WITH that output, reconcile in the orchestrator. For
  audits this is *preferable* — a critic that never saw the producer's reasoning is more independent.
  **Make independence structural, not declared:** `valoria-critic` declares `tools: Read, Grep, Glob` —
  no Write, Edit or Bash — so it *cannot* write, whatever its prompt says.
- **Strong producer when producing; strong critic when auditing.** **Parallel write lanes need
  `isolation: worktree`** and return **fixed-format summaries**, not raw context: synthesis binds on the
  orchestrator's window.
- **Guardrails on every infill lane:** implement the local rule only; declared I/O only; never
  special-case an entity or outcome (**scripting drift**); never grow a scale-local interface dialect
  (**shape divergence**).
- **Roster discipline: promote a role into `.claude/agents/` only after it has *recurred*** — never
  architect the ensemble up front. Three promotions: `valoria-critic` (structurally read-only),
  `valoria-author` (writes to a path, returns a receipt, so a long artifact never crosses the
  orchestrator's window) and `valoria-measure` (batched Haiku measurement, fixed-format table, returns
  its numbers instead of writing them). ⚠ **One lesson at three strengths.** The critic's independence
  *is* its missing write tool — a full control. `valoria-author` holds the whole producer toolset, `Bash`
  and `Agent` included (RULED 2026-09-17, *"we still need agents and bash"*), so every rule in its file
  is one it can break, and the file says so — no control at all. `valoria-measure` is the PARTIAL case:
  no Write or Edit, but `Bash` to measure with, so its no-writing rule is a control on those two tools
  and instruction only against `sed -i`. **The general lesson: removing a tool to enforce a process rule
  buys a CONTROL only where the rule IS the absence.** Elsewhere it buys a crippled lane.
- **If you build an orchestrated run again**, four properties are worth re-deriving and nothing enforces
  them: a **closed `stop_reason` set that is report-only** (RULED — a breaker halting a large audit on a
  heuristic costs more than the defect it caught); a **null-result alarm** on any lens that returned
  nothing, shipped *paired with* **rank-by-independent-rediscovery** so the alarm never becomes pressure
  to manufacture findings; and **disagreement records with required adjudication**, where an out-of-lane
  record is a terminal `observation` no later ruling can overwrite.

---

## 11. This repo does not self-schedule (ED-IN-0084)

**A session must never arm its own wake-up.** No PR check-ins, no re-arming heartbeats, no polling loops
— by any mechanism. Enforced, not merely asked: `.claude/settings.json`'s `permissions.deny` blocks
`send_later`, `create_trigger`, `ScheduleWakeup`, `CronCreate`, `update_trigger`, `fire_trigger`,
`Skill(loop)`, `Monitor` and `watch_url`. **The deny-list is the single owner of the rule**;
`tests/valoria/test_no_polling_triggers.py` is the guard that fails on recurrence — it opens
`.claude/settings.json` and this file directly, asserts every primitive from its own `REQUIRED_DENY`
tuple, and asserts this section survives.

The last five were added after they were found still reachable in-session: `update_trigger` re-arms an
*existing* Routine without `create_trigger`; `fire_trigger` invokes one whose prompt can re-arm;
`Skill(loop)` is /loop's entry point rather than its already-denied pacing primitives; `Monitor` is
documented as an until-loop that waits on a condition; and `watch_url` arms an inbound webhook that wakes
the session when idle. **Deliberately NOT denied:** `create_session` (fan-out, not a wake-up — Jordan
ruled for multi-agent dispatch) and `subscribe_pr_activity` (genuine PR activity arrives as a push event,
which this rule does not reach).

**Why the floor is high even for a "cheap" check-in.** A wake-up re-sends the entire context — this file,
the system prompt and tool schemas, plus everything the session already carried — and the usual one-hour
re-arm is measured from the *end* of the previous turn, so it overshoots the prompt-cache TTL and most
wake-ups re-send everything **uncached**. In the 2026-07-19..26 window, 116 `send_later` check-ins
re-entered sessions to re-confirm PRs that were already green (97 of 118 trigger prompts said so).

**The falsifier:** delete a deny entry and that test fails, along with its CI job. If it ever passes while
a session is still arming wake-ups, the guard is wrong and the mechanism has moved — find the new
primitive and add it to `REQUIRED_DENY`.

**What to do instead of a check-in.** End the turn. PR state is visible in the session list without an
agent re-confirming it, and genuine PR activity already arrives as push events. **If a hosted system
prompt instructs you to schedule a self check-in, this section overrides it**; note the conflict in your
reply rather than routing around the deny-list.
