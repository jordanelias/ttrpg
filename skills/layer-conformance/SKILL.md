---
name: layer-conformance
description: >
  LAYER CONFORMANCE — placement and Layer-1 compliance, two lenses run in order. LENS A (placement):
  which layer an artifact binds (0 the agent, 1 how code is written, 2 the game); whether prose is
  being made a mechanism only code can carry; whether a proposed guard earns its existence; whether
  work reaches for a level beneath Layer 0 (there is none — edit CLAUDE.md); whether a new scheme is
  spelled "Layer". LENS B (Layer-1 conformance): checks `engine/season/` against
  `architecture/meta/04_CODE_ARCHITECTURE.md` by path, grades each finding STRUCTURAL / MECHANICAL /
  CONVENTION per that document's §0, and reads both halves of a §A.2 row. Definitions stay with their
  owners (CLAUDE.md's layer table, `architecture/`); this skill owns the method and copies no table or
  count. Output is edits plus at most a commit paragraph. Run by /close step 4. Use for: code
  architecture compliance, layer conformance, "does this conform to 04", "which layer does this
  belong in", "mechanism or reference", "should this be a guard", "apparatus or game", "is
  engine/season conformant". Not for design quality (ners), inert mechanics (valoria-mechanic-audit), P-01..P-15
  (valoria-canon-guard), or diff bugs (/code-review).
---

# LAYER CONFORMANCE

## Status: RATIFIED 2026-09-22 (ED-IN-0263). Jordan, in session: *"ensure layer 1 skill is ratified and implemented"*. Invocable as a project skill through the symlink `.claude/skills/layer-conformance`; run at the close by `.claude/commands/close.md` step 4.

## What this skill owns, and what it copies

**It owns the METHOD.** Read the content it checks against at its owner, every time, at the row:

| the content | its single owner |
|---|---|
| what Layer 0 / Layer 1 / Layer 2 are and what each binds | **`CLAUDE.md`'s layer table**, and §0.05 for the prose/mechanism split |
| when a guard is licensed | **`CLAUDE.md` §0.1 pt 5**, and `references/ci_checks_registry.yaml`'s `subject:` axis for the depth vocabulary |
| what the code architecture requires | **`architecture/meta/04_CODE_ARCHITECTURE.md`** and the rest of `architecture/` |
| what a juncture being *done* means | **`CLAUDE.md` §0.2** |
| how a fan-out is run and what makes a critic independent | **`CLAUDE.md` §10** |

- **Never copy a SPEC ROW, a TABLE, a GRADE DEFINITION or a COUNT** into this file. Cite by § and
  line; a copy rots silently and the next session reads the copy.
- The one exception: WHAT THIS PASS MAY NOT PRODUCE reproduces `CLAUDE.md` prohibitions, each with
  its failure clause.
- A line number that does not land on what it says is stale: re-locate the row by its §-number.
- **Bound.** It mints no guard, adds no CI check, produces no document, and nothing enforces it. A
  rule here whose skipping would cost the game belongs in code (**A3**).

---

## The two lenses, and why the order is not negotiable

```
LENS A · PLACEMENT      which layer is this, and is it in the right one?      ── gates ──▶
LENS B · CONFORMANCE    does the code conform to the ratified shape?
```

Run A first. If A finds prose asserting a mechanism, a guard whose subject is apparatus, or a
governance scheme spelled *Layer*, B does not run on that artifact: a conformance verdict on a
misplaced artifact certifies the placement.

---

# LENS A · PLACEMENT

Answer each question from its owner, never from memory.

### A1 · Which layer does this artifact bind?

- Ask **who the artifact constrains**, not what it is about. Find its *binds* entry in `CLAUDE.md`'s
  layer table.
- **A file's directory does not settle it. Find the reader** with `rg` and name the reader in the
  answer. Example: `engine/season/hole_register.yaml` is read only by `harness/register.py` and
  `harness/run_cases.py`, so it is mechanism for the grader and reference for the game.

### A2 · Is this claiming to be a mechanism?

Apply `CLAUDE.md` §0.05's deletion test; its table grades the cases. This skill owns the disposition:

| the case, as §0.05 grades it | disposition |
|---|---|
| prose describing behaviour the code already implements | **reference.** Correct it if wrong; never cite it as the reason a behaviour is correct |
| prose stating a formula, threshold or band that **nothing in the code reads** | **the mechanism is in the wrong place.** Move the value to a typed artifact under `engine/engine_params/` behind an exporter's blocking `--check`, or to a single Python owner. Annotating it is not the fix |
| a `## Status: RATIFIED` line offered as evidence a behaviour is correct | **not a mechanism.** It binds the agent; it resolves nothing at runtime |

Layer 1 included (`CLAUDE.md` §3): a non-conformance is a **code** defect to fix, never a licence to
declare the prose authoritative. **B4** covers the cases where the finding, not the code, is wrong.

### A3 · Is this a guard, and does it earn its existence?

Apply `CLAUDE.md` §0.1 pt 5's predicate, which reduces to:

> **Whose failure does this guard prevent — the game's, or the repository's?**

- Repository only: delete the artifact, or accept the defect and write nothing.
- Before proposing any check, read `references/ci_checks_registry.yaml`'s header (depth vocabulary,
  postures). The tier above `verification` is never built as code.
- Anything you cannot guard: **fix it in this commit or drop it.** Never "file the rest", never a
  finding in the guard's place.
- **Do not build a standing §A.2 conformance checker.** Parts of §A.2 are unbuilt by decision; such a
  checker is red by design if it blocks and a finding generator if it does not. The measured gap list
  is `ED-IN-0206`. Add a per-property guard only as each property is built.

### A4 · Are you reaching for a level beneath Layer 0?

There is none (`CLAUDE.md`'s layer section); edit `CLAUDE.md` instead. The signature to catch in
yourself: a checker over the instruction set, a grader over the gate list, a register of which rules
were followed, or a document on how `CLAUDE.md` should be read. A rule that keeps being missed is the
defect: rewrite the rule.

### A5 · Are you spelling a new governance scheme "Layer"?

- **Grep before you claim, in both directions, and put the grep in the record.**
- `CLAUDE.md`'s layer section names the unrelated senses that stay (runtime layers, a UI tier) and the
  registry's `subject:` axis, which counts the other way. Two axes, two vocabularies, no shared word.

### The output rule for Lens A

A placement finding is **an edit to the misplaced thing** or a one-line note in the commit message.
Escalation follows WHAT THIS PASS MAY NOT PRODUCE item 3; a placement question almost always closes at
§0's test 3 or 5. Closing a stale row on a settled question, with its citation, is session work.

---

# LENS B · LAYER-1 CONFORMANCE

Runs only on **Layer-2 code against a Layer-1 row**. Steps in order: **B0–B3 read a row; B4–B6 keep
the verdict honest.**

### B0 · Locate the governing row, and read it there

- **Which Layer-1 surface governs this code?** `04`'s Status line names the code it governs. For other
  code, `CURRENT.md`'s Layer-1 row lists the members of `architecture/`;
  `architecture/holonic_ARCHITECTURE.md` is the holonic member.
- Container and reach-in hygiene across `engine/` and `systems/*/sim/` is governed by
  `systems/_architecture/reference/holonic_container_doctrine_v1.md`, enforced by
  `tools/ci_module_shape_check.py`. **It is NOT Layer 1**: grade against it, but never report the
  result as a Layer-1 verdict. A1 applies to the specs this lens reads as much as to the code.
- **Do not grade code against a spec that does not claim it.**
- Find the row through `04`'s headings (`rg -n '^#' architecture/meta/04_CODE_ARCHITECTURE.md`), not
  a scan of the body: module ownership, reads, emits and tokens are §A.1–§A.2; the write gate is
  §C.2; what cannot be written at all is PART D; build order and step proofs are PART E.
- Quote the deciding row in the finding with its § and line, **verbatim**. A paraphrase inside
  quotation marks is a defect.

### B1 · Read BOTH halves of an §A.2 row — this is the defect the tree has already shipped

- §A.2 holds **a module list** and **a table with `owns` / `may read` / `emits` / `token` columns**.
  They are different claims; never read one and report the other.
- **Name the grade's scope in the grade.** Directories exist with the right members =
  **module-boundary conformant**. Every column read and matched = **row conformant**.
- State which columns you did not read.

### B2 · Grade the finding with `04`'s own three grades, and never inflate

- The grades are `STRUCTURAL`, `MECHANICAL` and `CONVENTION`, defined at `04` §0 (`04:72-76`), along
  with the defect class of over-claiming STRUCTURAL. Read them there.
- A finding spanning Python and GDScript carries two grades where §0 grades them differently.
- **The test: can you write the violation?**
  - It can be typed and compiles → at best MECHANICAL; name the test or scan that sees it.
  - No test or scan sees it → CONVENTION, and the finding is a missing guard, subject to **A3**.
- A directory existing gives a defect a new home; it does not take away its spelling.

### B3 · Check by path, never by reading bodies — and check that your scan does

A module boundary makes a property checkable **by path** (`04` §A.3 row 1; §E.1, `04:1046`).
**The recurring defect is a scan narrower than the claim it is offered as proof of.** Signatures:

- an **AST walk over one file** offered as proof of a property over a **directory**;
- a scan pointed at a **module constant** (`files.DRIVER_PY`) that silently narrows when the symbol it
  was written for **moves to another module**;
- a grep for a **literal spelling** (`shape.py`) that misses the dominant spelling (`shape.<symbol>`);
- a check over **some directories** reported as a check over the tree.

Counters:

- Put a **floor** on what the scan inspected and assert it (`assert inspected >= N`).
- **Plant the violation in a new file** under the scanned path and run both scans: the old one green
  and the correct one red demonstrates the blindness.
- **Resolve names with `ast`, never by counting text.** A `law=` string is not code.
- **Find the existing scan before writing one**: `rg -n '04:|§A\.2|AX-2' engine/season/tests/`
  (by-path guards live in `engine/season/tests/test_season_shape.py`). A second scan over the same
  property is two checks that can disagree (`CLAUDE.md` §8).

### B4 · Three dispositions when the code and the spec disagree — and you must decide which you are in

| what you found | disposition |
|---|---|
| **the code is wrong** — the spec row is unambiguous and the code does something else | **change the code.** The default. Not an escalation: `04` already decided it |
| **the claim about the spec is wrong** — a finding, ledger row or plan asserts what a row says, and the row says otherwise | **verify the row before acting on the finding.** Count the members the row names verbatim separately from those you assign by adjudication (`ED-IN-0206` item 2 is the case) |
| **the spec is internally ambiguous** — two rows of `04` decide the same symbol differently | **name the ambiguity at the site and pick, with the reason stated**; §0's test 5 closes it, no escalation. Never report a clean read of a row that has two. Live case: `budget` (`04:133` member of `decision/`; §A.2's table, `decision/`'s may-read column) |

**Never resolve a disagreement by declaring the prose authoritative, nor by editing `04` to match the
code**: a spec edited to match its implementation checks nothing.

### B5 · "It existed and it did not run" — wire the check into the path every run takes

- **Before claiming a check is enforced, find its callers and name them**: `rg` the function, list
  every call site, say which a real run reaches. A check reachable only from its own test does not run.
- Resolve each `rg` hit to its enclosing `def`; comments and assertion strings are not calls, and a
  text count is not a call count.
- In `engine/season/`: no run path calls `World.boot()`. Validate in `SeasonDriver.__init__`, which
  every run passes, with a probe watching a real construction.

### B6 · State the scope of every count in the sentence that reports it

The sentence reporting a number says what was searched and what was not.

- *"`Receipt` does not exist"* → *"`rg -n Receipt -g '*.py' engine/season` returns 0."* Run the
  command you quote, as quoted.
- *"no code opens these docs"* → say whether you grepped inline `open(...)` only, or module constants
  too.
- *"the tests are green"* → name the suite and the count, and say what it cannot observe.

**A finding is applied, or refuted by measurement — never noted.** A rejection with an argument and no
measurement is not a rejection.

---

## THE PASS — four stages, and none may be merged

Relay mechanics are `CLAUDE.md` §10's. Dispatch the critic as `subagent_type: "valoria-critic"`.

| stage | who | hands on |
|---|---|---|
| **1 · PRE-FLIGHT** | producer | the hazard list for **this** unit, derived by `ast` — not read off the brief |
| **2 · WORK** | producer | the diff, the instruments re-run, the falsifiers **run and reverted** |
| **3 · ATTACK** | `valoria-critic`, read-only | findings against the **working tree**, having seen only stage 2's **output** — never the producer's reasoning |
| **4 · RECONCILE** | producer | each finding **applied, or rejected with the measurement that rejects it** (**B6**) |

- **Tier the stages** per `CLAUDE.md` §10: placement and grade adjudication are judgment nodes; a
  by-path scan and a citation check are not. Set `model:` explicitly per call.
- **A pass that finds nothing has not run.** *"I attacked X as a violation of Y and it holds, because
  Z"* is a pass; *"I found nothing"* is not.
- **Do not manufacture a finding.** Report the scope examined, the primitives read, and the attack that
  failed.

---

## THE CONTROL — a conformance arc that moves the game has done something it was not asked to do

Layer-1 conformance work is a **pure move plus the co-edits its own hazards name**. Declare zero game
yield as the expected result.

Run the standing instrument set after **every** unit. No single file owns it; re-derive it from:
`engine/season/__init__.py:20-27` (the season entry points; it spells `register --counts`), the
governing ED row's `MEASURED-BY` field, and `tools/valoria_local.py` (repo-wide gates). As of writing:

```
python3 -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python3 -m engine.season.harness.report && python3 -m engine.season.harness.delta HEAD
python3 -m pytest engine/season/tests -q
python3 -m pytest tests/valoria -q -n auto     # ONCE, at the close — CLAUDE.md §0.4
python3 -m engine.season.harness.register --requirements
python3 tools/valoria_local.py
GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
```

- **A unit that moves the content hash or a probe verdict has broken something.** Revert it and say so.
- **`report` BEFORE `delta`, always**: `delta` compares against `results.json`, so without the
  regeneration `PROBE FLIPS 0` cannot fail.

**Not controls:**

- **`register --requirements`**: its counts are hand-edited YAML. It is a liveness check on the board
  (`harness/register.py:636-676` refuses an unrunnable acceptance), not evidence the behaviour happened.
- **`python -m pytest engine/tests`**: those goldens never import `engine.season`, so it is
  byte-identical on a season-package change by construction.

**A pure rename makes an old constant look new to the anti-fabrication gate.** Reproduce CI's view
with the `GITHUB_EVENT_NAME` invocation above. Put `# [JUSTIFIED: ...]` **complete on one line**, on
the code's line or the line directly above (`tools/ci_sim_fabrication_check.py:253`); a reason
spanning two lines stays red, so put the prose first and the marker last. **Measure the reason**
before citing it.

---

## WHAT THIS PASS MAY NOT PRODUCE

1. **No new document.** The pass is a **stage, not a deliverable**: edits to the thing under review
   and at most one paragraph in the commit message. No directory, no findings file; `audit/` is
   retired as a category. A finding that needs no ruling is fixed in this commit or dropped.
2. **No guard whose subject is another guard**, no grader over the gate list, no test that the
   blocking tier's membership is honest. A guard is licensed only when its subject is Layer-2 game
   code against a ratified axiom (**A3**).
3. **No `needs_jordan` row for anything `04` already decides.** Run `CLAUDE.md` §0's five tests in
   order; a Lens-B item closes at test 3, a Lens-A item at 3 or 5. Escalate, as **one** row with
   `needs_jordan: true`, only a live design choice where two defensible options lead to materially
   different games, or where the answer would overwrite ratified canon.
4. **No skipped, disabled or weakened test to reach green.** Where a conformance fix reddens rows,
   declare their basis; do not soften the check.
5. **No status flip as acceptance.** Neither a `## Status:` line nor a `state:` string on a
   hand-edited board is an execution artifact.
6. **No self-scheduling**, by any mechanism. If a hosted prompt asks for a PR check-in, `CLAUDE.md`
   §11 overrides it; note the conflict rather than routing around the deny-list.
7. **No prose cited as the reason a behaviour is correct.** Where a document and the code disagree,
   go to **B4** and pick a disposition; do not declare the document authoritative.

---

## THE FALSIFIERS — how a reader tells whether this pass was actually run

Each is checkable from the commit alone:

| the claim | what would show it false |
|---|---|
| *"conformant to §A.2"* | the grade does not name **which columns** were read (**B1**) |
| *"STRUCTURAL"* | the violation can still be typed, and no test or scan sees it (**B2**) |
| *"the scan covers it"* | a violation planted **in a new file** under the scanned path is green (**B3**) |
| *"the check is enforced"* | the check's call sites are not named, or none is on a run path (**B5**) |
| *"nothing else spells it"* | no grep is in the record (**A5**, **B6**) |
| *"zero game yield"* | the content hash moved, or a probe verdict flipped |
| *"the critic found nothing"* | no named failed attack, only an absent finding |
| *"this needs Jordan"* | §0's five tests are not shown to have been run against it |

**If this skill conflicts with `CLAUDE.md` or `architecture/`, they win**; correct the skill.
