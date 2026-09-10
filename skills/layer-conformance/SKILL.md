---
name: layer-conformance
description: >
  LAYER CONFORMANCE — the repo's placement-and-compliance pass, and the skill a session runs when the
  question is "code architecture compliance": does this artifact sit in the right layer, and does the
  code conform to the ratified code architecture? TWO LENSES, IN ORDER, because the second is
  meaningless without the first. LENS A · PLACEMENT asks which layer an artifact binds (Layer 0 the
  agent, Layer 1 how code is written, Layer 2 the game), whether a claim is being made a MECHANISM in
  prose where only code can carry it, whether a proposed guard earns its existence, whether the work
  is reaching for a level beneath Layer 0 (there is none — the repair is to edit CLAUDE.md), and
  whether a new governance scheme is being spelled "Layer". LENS B · LAYER-1 CONFORMANCE runs code in
  `engine/season/` against `architecture/meta/04_CODE_ARCHITECTURE.md` — BY PATH, not by reading
  bodies; grading each finding STRUCTURAL / MECHANICAL / CONVENTION per that document's own §0; and
  reading BOTH halves of a §A.2 row, because a directory count reported as row conformance is the
  defect this repo has already shipped and corrected once. The DEFINITIONS live with their owners —
  CLAUDE.md's layer table and `architecture/` — and this skill owns the METHOD, exactly as `ners` owns
  the NERS method while CLAUDE.md §0.06 owns the NERS definitions. It copies no table, no grade
  definition and no count from either owner; where it does reproduce a CLAUDE.md PROHIBITION it carries
  that rule's failure clause with it, deliberately and for the reason stated inside.
  Its output is EDITS to the thing under review plus at most one paragraph in a commit message: it
  creates no directory, no findings file, and no guard whose subject is apparatus.
  ALWAYS use for: "code architecture compliance", "is this Layer-1 compliant", "layer conformance",
  "does this conform to 04", "does this conform to the code architecture", "which layer does this
  belong in", "is this a mechanism or reference", "should this be a guard", "does this guard earn its
  existence", "is this apparatus or game", "am I building a Layer -1", "can I call this a Layer",
  "is this STRUCTURAL or MECHANICAL", "does the scan actually cover what I claimed", "is `engine/season/`
  conformant", "check the §A.2 modules", "is the write gate built".
  Do NOT use for: judging whether a DESIGN is good — that is `ners`, which asks what dies when you cut
  it, not where it lives; contract IN→resolver→OUT closure — that is `valoria-module-adjudicator`;
  finding inert or inconsistent mechanics — that is `valoria-mechanic-audit`; P-01..P-15 philosophy
  compliance — that is `valoria-canon-guard`; or reviewing a diff for correctness bugs — that is the
  native `/code-review`, a fresh-context reviewer that never saw your reasoning.
---

# LAYER CONFORMANCE

## What this skill owns, and what it copies

**It owns the METHOD.** The content it checks against is owned elsewhere and is read there, every
time, at the row:

| the content | its single owner |
|---|---|
| what Layer 0 / Layer 1 / Layer 2 are and what each binds | **`CLAUDE.md`'s layer table**, and §0.05 for the prose/mechanism split |
| when a guard is licensed | **`CLAUDE.md` §0.1 pt 5**, and `references/ci_checks_registry.yaml`'s `subject:` axis for the depth vocabulary |
| what the code architecture requires | **`architecture/meta/04_CODE_ARCHITECTURE.md`** (RATIFIED, ED-IN-0204) and the rest of `architecture/` |
| what a juncture being *done* means | **`CLAUDE.md` §0.2** |
| how a fan-out is run and what makes a critic independent | **`CLAUDE.md` §10** |

This is the split `ners` already uses: that skill owns the NERS method and `CLAUDE.md` §0.06 owns the
four definitions.

**What this file copies, and what it refuses to copy — the line is drawn at what can rot.**

- **It never copies a SPEC ROW, a TABLE, a GRADE DEFINITION or a COUNT.** Those it cites by § and
  line, because a copy rots away from its source silently and the next session reads the copy. That is
  the failure `CURRENT.md`'s season-loop row records having made **twice** with a test count
  (`CURRENT.md:34`, *"this row has carried a stale one twice"*).
- **It does reproduce a `CLAUDE.md` PROHIBITION together with that rule's failure clause** — see WHAT
  THIS PASS MAY NOT PRODUCE. That is deliberate and precedented:
  `workplans/2026-09-09-layer1-conformance-plan_part2.md` §13 made the same call on the same reasoning,
  which is `CLAUDE.md`'s own — *with no context between sessions, the clause naming what goes wrong is
  what stops the rule being re-litigated.* A bare pointer to a prohibition is the thing that gets
  skipped; the failure clause is the part that does the work.

When a line number here does not land on what it says it does, the line number is stale and the
document is not: re-locate the row by its §-number.

**This skill is apparatus, and it declares its own bound.** It mints no guard, adds no CI check,
produces no document, and cannot be satisfied by writing. Everything it asks for is either an edit to
the artifact under review, a measurement, or a sentence in a commit message.

⚠ **And it declares the one thing it cannot fix about itself.** Standing orders inside a
`skills/<name>/SKILL.md` **bypass** `CLAUDE.md` §0's adversarial-pass gate entirely: nothing surfaces
this file, nothing enforces it, and a session that never opens it is not stopped by anything. That is
the honest bound on every claim below — this is a method a session chooses to follow, not a
mechanism. If a rule here matters enough that its being skipped would cost the game, it does not
belong here: it belongs in code, under **A3**.

---

## The two lenses, and why the order is not negotiable

```
LENS A · PLACEMENT      which layer is this, and is it in the right one?      ── gates ──▶
LENS B · CONFORMANCE    does the code conform to the ratified shape?
```

**A conformance verdict on a misplaced artifact is worse than no verdict**, because it certifies the
placement by acting on it. If Lens A finds the artifact is prose asserting a mechanism, or a guard
whose subject is apparatus, or a governance scheme borrowing the word *Layer*, then the finding is a
**placement** finding and Lens B does not run on it at all. Run A. Then, only for Layer-2 code
against a Layer-1 row, run B.

---

# LENS A · PLACEMENT

Five questions. Each routes to the rule that owns it; none is answered from memory.

### A1 · Which layer does this artifact bind?

Ask **who the artifact constrains**, not what it is about. A document about the game that tells a
session how to work binds the agent; a registry about process that code opens at runtime binds the
game.

**Read the three rows in `CLAUDE.md`'s layer table — they are not copied here**, because a copied
governance table is the one thing this file must not be the second home of. What the table gives you
is a *binds* column; the method is to find which one your artifact is in, and the question that
settles it is the one above.

⚠ **A file's directory does not settle this, and two live examples prove it.**
`engine/season/hole_register.yaml` sits with the game code and its readers are
`harness/register.py:69` and `harness/run_cases.py:214` — **two** grading modules, neither of them
under `loop/` — so it is mechanism for the grader and reference for the game.
`engine/season/data/rosters.py`, `verbs.py` and `matrix.py` sit in the same tree and *are* opened by
the loop at runtime. Same directory, opposite answers. **Resolve it by finding the reader**, with `rg`
over the tree, and name the reader in the sentence that reports the answer.

### A2 · Is this claiming to be a mechanism?

Run `CLAUDE.md` §0.05's test verbatim: **if this document were deleted, would the game behave
differently?** §0.05's table owns **the graded cases** and is not reproduced here — open it and find
yours rather than reasoning from the one-sentence test. What follows is the **disposition** for each,
which is the part this skill owns. Three outcomes, and the middle one is where sessions go wrong:

| the case, as §0.05 grades it | disposition |
|---|---|
| prose describing behaviour the code already implements | **reference.** Correct it if wrong; never cite it as the reason a behaviour is correct |
| prose stating a formula, threshold or band that **nothing in the code reads** | **the mechanism is in the wrong place.** The value belongs in a typed artifact under `engine/engine_params/` behind an exporter's blocking `--check`, or in a single Python owner. Moving it is the fix; annotating it is not |
| a `## Status: RATIFIED` line offered as evidence a behaviour is correct | **not a mechanism at all.** §0.05 is explicit. A ratified doc binds the agent; it resolves nothing at runtime |

⚠ **Layer 1 is `RATIFIED` *and* is reference for game mechanism.** Both halves are true at once and
neither cancels the other: `04` binds you as an agent instruction with the same standing as
`CLAUDE.md`, and it still cannot be cited as the reason a behaviour is correct. A non-conformance is
therefore a **code** defect to fix, not a licence to declare the prose authoritative — and see **B4**
for the two cases where that inverts.

### A3 · Is this a guard, and does it earn its existence?

`CLAUDE.md` §0.1 pt 5 carries the predicate; read it there. The operational question it reduces to:

> **Whose failure does this guard prevent — the game's, or the repository's?**

A pattern defect in an artifact load-bearing only on this repository's process is **not** evidence
that artifact needs a guard; it is evidence the artifact **can be wrong without cost**. Delete it, or
accept the defect and write nothing.

`references/ci_checks_registry.yaml`'s header owns the depth vocabulary — `game` / `compliance` /
`verification`, their postures, and the fourth tier that **does not exist as code, ever**, because its
subject would be a `verification` guard. Read that header before proposing any check. It records that
this repo built the forbidden tier **four times** and retired all four with measurements attached.

**Inert without the prose bound.** Forbid the guard and a session writes *a finding* instead, because
the carrier is prose and prose is not gated. So the disposition for anything you cannot guard is
**fix it in this commit or drop it** — never "file the rest".

⚠ **The guard this pass in particular is tempted to mint is a standing §A.2 conformance checker, and
it is the wrong instrument.** The tree is knowingly non-conformant against parts of §A.2 right now,
by decision and by sequencing — the gate contract is unbuilt and `port/` is deliberately absent — and
the measured gap list is already a ledger row (`ED-IN-0206`). A checker over a spec the tree is
knowingly short of is red by design if it blocks, and a finding generator if it does not. **The
per-property guards the predicate above licenses are the ones that go in, one at a time, as each
property is actually built** — which is how `decision/`'s AX-2 scan and the manifest sweep arrived.

### A4 · Are you reaching for a level beneath Layer 0?

**There is no Layer -1.** Needing one means Layer 0 was written wrong, and the repair is to **edit
`CLAUDE.md`** — never to build a level beneath it. The signature to catch, in yourself: you are about
to write a checker over the instruction set, a grader over the gate list, a register of which rules
were followed, or a document that says how `CLAUDE.md` should be read.

The tower terminates because **Layer 0 binds a reader, not a program**: code must be checked by code,
which has no natural top, whereas an instruction is followed or not, and its failure is corrected by
rewriting it. If a rule keeps being missed, the rule is the defect. Rewrite the rule.

### A5 · Are you spelling a new governance scheme "Layer"?

**Grep before you claim, in both directions.** *"Nothing else spells Layer"* is one of four claims
this repo has shipped as exhaustive while being merely sufficient — it was asserted without a grep
having been run.

Two existing uses are **unrelated senses in their own documents and they stay**:
`godot/godot_architecture_specification.md` numbers four *runtime* layers (Content / Conflict /
Resolution / Progression), and `systems/ui/` uses "Layer 3" for a UI tier. Neither governs how work is
done, so neither collides.

One collision was found and repaired, and it is the worked example: `references/ci_checks_registry.yaml`'s
depth field was spelled `layer:` until 2026-09-09 and **counted in the opposite direction** — its `L0`
was the game, where governance Layer 2 is the game — so a session reading either cold derived the
other's meaning. It was renamed to `subject:`. That is the idempotence failure `CLAUDE.md` §4 names, and
`evacuate` had already cost real work to the same failure. **Two axes, two vocabularies, no shared
word.**

### The output rule for Lens A

A placement finding is **an edit to the misplaced thing**, or a one-line note in the commit message,
or — where it survives all five of §0's tests and genuinely needs Jordan — **one** ledger row with
`needs_jordan: true`. It is never a new directory, never a findings file, and never a guard.

⚠ **`needs_jordan` is not a parking space.** Before flagging a row, or leaving one flagged, run
`CLAUDE.md` §0's five tests in order — superseded · irrelevant · answered by a design document ·
answered by precedent · answered by what makes sense for the architecture. **A placement question
almost always closes at test 3 or 5**, because `CLAUDE.md` and `04` between them have already decided
where things go. Clearing a stale row is session work in its own right: find one on a settled question
and close it with its citation.

---

# LENS B · LAYER-1 CONFORMANCE

Runs only on **Layer-2 code against a Layer-1 row**. Seven steps, in order. **B0–B3 are how you read
a row; B4–B6 are how a verdict goes wrong once you have one.** **B1–B5 each carry a defect this tree
has already shipped and corrected, with its measurement rather than as advice**; **B6 is the rule those
failures produced** and is the one step here stated as a rule rather than as an incident.

### B0 · Locate the governing row, and read it there

**First, which Layer-1 surface governs this code?** `architecture/meta/04_CODE_ARCHITECTURE.md` says
in its own Status line that the game code it governs is `engine/season/`. For code elsewhere the
governing surface is a different member of `architecture/` — `CURRENT.md`'s Layer-1 row lists them,
and `architecture/holonic_ARCHITECTURE.md` is the Layer-1 holonic member.

⚠ **Container and reach-in hygiene across `engine/` and `systems/*/sim/` is governed by
`systems/_architecture/reference/holonic_container_doctrine_v1.md`, and that document is NOT Layer 1.**
It is CANONICAL (ratified 2026-07-02, ED-1083/ED-1094) and it lives under `systems/`, not
`architecture/` — a legitimate governing surface reached by a different route, already enforced by
`tools/ci_module_shape_check.py`. Grade against it by all means; do not report the result as a
Layer-1 verdict. **A1 decides a document's layer by who it binds, and that rule applies to the specs
this lens reads as much as to the code it reads them against.**

**Do not grade code against a spec that does not claim it.**

For `engine/season/`, then: `04` is RATIFIED and it is the row-level authority. Open it. Find the
§-numbered row that decides the question. Quote it in your finding with its § and its line, and
**quote it verbatim** — a paraphrase inside quotation marks is a defect this repo has flagged in its
own planning documents.

Where to look, so the search is not a scan of 134 KB:

| the question | the part |
|---|---|
| which module owns this, what it may read, what it emits, which token it holds | **§A.1** (what each axiom forces) and **§A.2** (the nine modules and the table) |
| why the shape differs from the earlier chain | **§A.3** — fifteen differences, each with its forcing clause |
| what a type may and may not carry | **PART B** |
| what crosses a seam, and the write gate | **PART C** — §C.2 is the gate |
| whether a defect can be *written at all* | **PART D** — what is structurally impossible |
| what order this may be built in, and what proves a step done | **PART E** |
| what the spec itself declares insufficient | **PART F** |
| how design proceeds from here | **PART G** |

### B1 · Read BOTH halves of an §A.2 row — this is the defect the tree has already shipped

§A.2 has **a module list** and, under it, **a table with `owns` / `may read` / `emits` / `token`
columns**. They are different claims and a pass that reads one and reports the other is wrong.

> **The worked failure, measured in this tree.** Arc 1 of the Layer-1 conformance work reported
> *"eight of nine, measured item by item"*. That was a **directory count** — the directories exist and
> hold the members §A.2 names — **reported as row conformance.** Against the table it was not true:
> `state/` had no `gate`/`log`/`ledgers` owners, `data/` had no ONE loader, `queries/cache` held one of
> the three named indexes, `loop/calendar` emitted nothing and `loop/census` wrote nothing against
> their rows, and `tests/` had no *"two licensed guards"*. `Receipt` did not exist anywhere in the
> package while §B.9 types `Event.changes[]` as `Receipt[]`. The correction is in `ED-IN-0206` and in
> `CURRENT.md`'s season-loop row; **the grade it settled on is MODULE-BOUNDARY conformance**, which is
> a narrower and true claim.

**So name your grade's scope in the grade itself.** *"Module-boundary conformant"* and *"row
conformant"* are different verdicts. If you have checked only that a directory exists with the right
members, say **module-boundary**, and say which columns you did not read.

### B2 · Grade the finding with `04`'s own three grades, and never inflate

**The three grades are `STRUCTURAL`, `MECHANICAL` and `CONVENTION`, and their definitions are at
`04:72-76` — read them there.** They are a table, so they are not restated here; what follows is the
operational test for choosing between them, which is the part this skill owns. `04 §0` states a grade
per invariant, separately for Python and GDScript wherever they differ, so a finding that spans both
carries two grades.

⚠ **A claim of STRUCTURAL that is actually MECHANICAL is a named defect class** — *a guard that cannot
observe what it guards* — and this repo has committed it about its own conformance work. `04:74`
defines STRUCTURAL as *"the defect has no spelling"*, which is precisely what is missing whenever the
type, the parameter list, or the absence of a name has not yet been changed. **A directory existing
gives a defect a new home; it does not take away its spelling.**

The test to apply to your own grade: **can you write the violation?** If you can type it and it
compiles, the grade is at best MECHANICAL, and you must name the test or scan that sees it. If no such
test exists, the grade is CONVENTION and the finding is that a guard is missing — subject to **A3**.

### B3 · Check by path, never by reading bodies — and check that your scan does

A module boundary exists so that a property is checkable **by path** rather than by reading bodies.
`04 §A.3` row 1 says exactly that of `decision/`, and `04:1046` makes it a build-order constraint:

> *"`decision/` is a directory from its first commit. The isolation scan matches by path, so a
> `choose` drafted inside `loop/` and moved later would have been green while violating AX-2."*

**The recurring defect is a scan narrower than the claim it is offered as proof of**, and it has
recurred **four times in this package — decomposition steps 2, 4 and 5, and again at Arc-1 unit L5**,
which is conformance work rather than a fourth decomposition step (`engine/season/data/files.py:148-149`
counts them). Its signatures:

- an **AST walk over one file** offered as proof of a property over a **directory**;
- a scan pointed at a **module constant** (`files.DRIVER_PY`) that silently narrows when the symbol it
  was written for **moves to another module**;
- a grep for a **literal spelling** (`shape.py`) that misses the dominant spelling (`shape.<symbol>`);
- a check over **three directories** reported as a check over the tree.

**Two counters, both cheap.** Put a **floor** on what the scan inspected and assert it (`assert
inspected >= N`) — a loop that asserts conditionally must assert that it asserted. And **plant the
violation in a new file** under the scanned path: the old scan is green on the plant and the correct
one is red, which demonstrates the blindness rather than asserting it was absent.

**Resolve names with `ast`, never by counting text.** A `law=` string is not code.

**And find the existing scan before you write one.** Several §A.2 properties already have by-path
guards in `engine/season/tests/test_season_shape.py` — the AX-2 scan over `decision/`, the
`queries/person_q` check, the manifest-row sweep. Locate them by their citation rather than by a
name that may have moved: `rg -n '04:|§A\.2|AX-2' engine/season/tests/`. Every rule lives once
(`CLAUDE.md` §8); a second scan over the same property is not a stronger check, it is two checks that
can now disagree.

### B4 · Three dispositions when the code and the spec disagree — and you must decide which you are in

`04` is ratified, and it is still **reference for game mechanism** (`CLAUDE.md` §0.05). That means a
disagreement has three resolutions and picking the wrong one ships a defect either way:

| what you found | disposition |
|---|---|
| **the code is wrong** — the spec row is unambiguous and the code does something else | **change the code.** This is the default and it is where the great majority land. It is not an escalation: `04` already decided it |
| **the claim about the spec is wrong** — a finding, a ledger row or a plan asserts what the row says, and the row says otherwise | **verify the row before acting on the finding.** `ED-IN-0206` item (2) asserted that four person-side symbols belonged in `queries/person_q`. `04:133` names **two of them verbatim** as `decision/`'s own members (`opening_set`, `budget`), a **third by adjudication** (`assemble` is question assembly, and `questions` is the member named), and **only the fourth** (`entrenchment`) actually moved — so acting on the finding as written would have **broken** conformance rather than restored it. ⚠ The row's own first correction over-claimed here too — its words are *"04:133 names all three as decision/'s OWN members"* — and it was corrected again to two-plus-one. **Count the verbatim ones and the adjudicated ones separately** |
| **the spec is internally ambiguous** — two rows of `04` decide the same symbol differently | **name the ambiguity at the site and pick with the reason stated.** `budget` is the live example: `04:133` lists it as a `decision/` member while §A.2's table lists it in `decision/`'s **may read** column. Do not report a clean read of a row that has two, and do not escalate it — §0's test 5 closes it |

⚠ **Never resolve a disagreement by declaring the prose authoritative.** And never resolve it by
editing `04` to match the code: it is ratified, and a spec edited to match its implementation checks
nothing.

### B5 · "It existed and it did not run" — wire the check into the path every run takes

`CLAUDE.md` §0.2 is a precondition of this whole lens, and `04` PART E states the same rule in its own
terms: every build step *"names the artifact that proves it, because a step is done when the behaviour
executes"*, and it flags **step 1 as the one deliverable there that writing can satisfy**.

> **The worked failure, measured in this tree.** Arc 1 moved a misspelled-manifest-row failure *"from
> first call to boot"* — which is the whole of the constraint at `04:1031` — by wiring
> `manifest.check_rows()` into `World.boot()`. **Nothing on a run path calls `World.boot()`**: the
> headless runner, the corpus run and the case runner never boot a world. Five call sites do, and they
> resolve to **one probe function and two test functions** — `probes.py::a19` (two calls),
> `test_season_shape.py::test_a_missing_provider_is_a_boot_failure` (two) and
> `::test_a_misspelled_manifest_row_fails_at_boot_naming_the_row` (one). So a misspelled row still
> failed at first call in every real season. The fix was to validate in `SeasonDriver.__init__`, the
> one place every run passes, with a probe watching a real construction.
>
> ⚠ **And this paragraph shipped B6's own defect once, which is why it is worth keeping.** ED-IN-0206
> and `loop/driver.py:171` both phrase the callers as *"two probes and three tests"* — the **call-site**
> count wearing an entity count's clothes. `rg -n '\.boot\(' -g '*.py' engine/season` returns **11
> hits, and only 5 are calls**: the other six are comments and assertion strings that spell
> `World.boot()` while calling nothing. **That is the whole lesson twice over** — resolve each hit to
> its enclosing `def`, and never let a text count stand in for a call count.

**So: before claiming a check is enforced, find its callers and name them.** `rg` for the function,
list every call site, and say which of them a real run reaches. A conformance check reachable only
from its own test is a check that does not run.

### B6 · State the scope of every count in the sentence that reports it

Four failures in this repo's decomposition arc were **a sufficient check reported as an exhaustive
one**. The rule is mechanical: whatever you counted, the sentence that reports the number says what
was searched and what was not.

- *"`Receipt` does not exist"* → *"`rg -n Receipt -g '*.py' engine/season` returns 0."* ⚠ Run the
  command you are about to quote. An earlier writing of this very line quoted `rg … --include=*.py`,
  which is GNU grep's flag and makes `rg` exit with `unrecognized flag`; a scope sentence citing a
  command that does not run is worse than no scope sentence.
- *"no code opens these docs"* → say whether you grepped inline `open(...)` only, or also module
  constants, because that exact narrowing has shipped here.
- *"the tests are green"* → name the suite and the count, and say what it cannot observe.

And a rejection needs a number: **a finding is applied, or refuted by measurement — never noted.** A
rejection with an argument and no measurement is not a rejection.

---

## THE PASS — four stages, and none may be merged

**Origin, cited rather than absorbed:** this pass is
`workplans/2026-09-09-layer1-conformance-plan_part2.md` §9–§13, generalized off that plan's arcs. That
document remains the binding statement of the method **for its own units**; this file is the durable
owner once those arcs close, and the two must not drift — if you change one, say so in the other.

`CLAUDE.md` §10 owns the mechanics: a relay, not a dialogue; subagents are stateless and isolated;
independence is made **structural** by `.claude/agents/valoria-critic.md`, whose `tools: Read, Grep,
Glob` mean a critic dispatched with `subagent_type: "valoria-critic"` *cannot* write, whatever its
prompt says. Read it there.

| stage | who | hands on |
|---|---|---|
| **1 · PRE-FLIGHT** | producer | the hazard list for **this** unit, derived by `ast` — not read off the brief |
| **2 · WORK** | producer | the diff, the instruments re-run, the falsifiers **run and reverted** |
| **3 · ATTACK** | `valoria-critic`, read-only | findings against the **working tree**, having seen only stage 2's **output** — never the producer's reasoning |
| **4 · RECONCILE** | producer | each finding **applied, or rejected with the measurement that rejects it** |

**What the critic is handed is the point.** Give it the output and the instrument results; give it
nothing about how they were produced. A critic rebuilding the reasoning from the tree finds what a
critic checking the producer's reasoning cannot — that is how the Fable gate on this repo's own
conformance plan overturned four of that plan's claims.

**Tier the stages** (`CLAUDE.md` §10 owns the ladder and the model IDs). Placement and grade
adjudication are judgment nodes; a by-path scan and a citation check are not. Reserve the top tier for
the **audit and guardrail** node rather than the synthesis one, and set `model:` explicitly per call
rather than inheriting Opus across the whole fan-out.

**A pass that finds nothing has not run — and the symmetric half is equally binding.** State the
attack you ran and that it failed and why. *"I attacked X as a violation of Y and it holds, because
Z"* is a pass; *"I found nothing"* is not. Equally, **do not manufacture a finding to look diligent**.
Report the scope examined, the primitives read, and the attack that failed.

---

## THE CONTROL — a conformance arc that moves the game has done something it was not asked to do

Layer-1 conformance work is a **pure move plus the co-edits its own hazards name**. Zero game yield is
the expected result and is declared, not apologised for.

Run the standing instrument set after **every** unit. ⚠ **No single file owns this list, and saying one
did would be the defect B1 is about.** `engine/season/__init__.py:20-27` owns the six season entry
points (and note it spells `register --counts`, not `--requirements`); the governing ED row's
`MEASURED-BY` field owns which of them evidenced that row; the repo-wide gates come from
`tools/valoria_local.py`. The list below is **assembled here from those three** and is therefore the
thing most likely to be stale in this file — re-derive it from them rather than trusting it. As of
writing:

```
pip install pyyaml pytest numpy                                  # fresh container only
python3 -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python3 -m engine.season.harness.report && python3 -m engine.season.harness.delta HEAD
python3 -m pytest engine/season/tests -q
python3 -m pytest tests/valoria -q
python3 -m engine.season.harness.register --requirements
python3 tools/valoria_local.py
GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
```

**A unit that moves the content hash or a probe verdict has broken something rather than revealed a
miscount.** Revert it and say so.

⚠ **Three things that are NOT controls, each for a different reason:**

- **`register --requirements`** never compares a `status:` to a measurement — its counts are
  hand-edited YAML and cannot move unless somebody edits the file, so a doc-derived count offered as
  evidence is §0.05's own worked example of a non-mechanism. ⚠ **It is not merely an edit tripwire,
  though, and calling it only that undersells it:** `harness/register.py:636-676` refuses a `status:`
  outside the enum, a row with no `measure:`, a `-k` that selects no real test, a `python <path>` that
  does not exist or has no `__main__`, and a `met`/`partial` row with an empty `measured:`. That is a
  **liveness check on the board** — it fails when an acceptance stops being runnable. What it still
  cannot do is tell you the behaviour happened.
- **`python -m pytest engine/tests`** is byte-identical to a season-package change **by construction**
  — those campaign goldens never import `engine.season`. Running it is a fake control.
- **The tests you wrote for the thing you built** encode your model of it, not the system.
  Targeted-green is not validation.

⚠ **`report` BEFORE `delta`, always** — `delta` compares against `results.json`, so without the
regeneration `PROBE FLIPS 0` is true by construction and cannot fail.

⚠ **A pure rename defeats the anti-fabrication gate's changeset scoping**: a constant untouched for
weeks arrives looking new because the rename rewrote its line. Reproduce CI's own view before pushing
with the `GITHUB_EVENT_NAME` invocation above, and put a `# [JUSTIFIED: ...]` marker **complete on one
line**. The gate (`tools/ci_sim_fabrication_check.py:253`) accepts it on the code's own line or the
line directly above, but a reason spanning two lines stays red — so put the prose first and the marker
last. And **measure the reason**: a false citation on an anti-fabrication gate is worse than the red
it fixes.

---

## WHAT THIS PASS MAY NOT PRODUCE

Each item is `CLAUDE.md`'s, reproduced **with its failure clause** rather than cited bare, because with
no context between sessions the clause naming what goes wrong is what stops the rule being
re-litigated.

1. **No new document.** The pass is a **stage, not a deliverable**. Its output is edits to the thing
   under review and at most one paragraph in the commit message. It creates no directory and no
   findings file; `audit/` is retired as a category, not merely as a cleanup. A finding that needs no
   ruling is fixed in this commit or dropped.
2. **No guard whose subject is another guard**, no grader over the gate list, no test that the
   blocking tier's membership is honest. A guard is licensed here only when its subject is Layer-2
   game code against a ratified axiom — see **A3**.
3. **No `needs_jordan` row for anything `04` already decides.** Run §0's five tests; a Lens-B item
   closes at test 3 (`04` decided it), a Lens-A placement item at test 3 or 5. A genuine escalation
   is a live design choice where two defensible options lead to materially different games, or where
   the answer would overwrite ratified canon.
4. **No skipped, disabled or weakened test to reach green.** Where a conformance fix reddens rows, the
   fix is to declare their basis, not to soften the check.
5. **No status flip as acceptance.** A `## Status:` line is not an execution artifact; a `state:`
   string on a hand-edited board is not one either.
6. **No self-scheduling** — no check-ins, no re-arming, no polling loops, by any mechanism. If a
   hosted prompt asks for a PR check-in, `CLAUDE.md` §11 overrides it; note the conflict rather than
   routing around the deny-list.
7. **No prose cited as the reason a behaviour is correct.** Where a document and the code disagree,
   go to **B4** and pick a disposition; do not declare the document authoritative.

---

## THE FALSIFIERS — how a reader tells whether this pass was actually run

Each of these is checkable from the commit alone, by someone who was not here:

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

**If this skill's advice conflicts with `CLAUDE.md` or `architecture/`, they win.** This file is a
method; they are the rules, and a method that has drifted from its rules is the thing to correct.
