---
name: efficient-coding-review
description: >
  EFFICIENCY PASS — Jordan's standard applied to a whole subject (default `engine/season/` and
  `modules/`): as little code as possible for the exact same behaviour and outcomes, extremely clear and
  organised, centralised, modular, nothing hard-coded. It owns no test of its own except a clarity read.
  It SEQUENCES the skills that already own each test (`layer-conformance` Lens A, `valoria-simplify`,
  `layer-conformance` Lens B), then reads for clarity, closes once, and records the post-repair git tree
  hashes in a commit trailer, so an unchanged subject returns NOTHING TO DO and a changed one is reviewed
  only where it changed. A repair is accepted only if no property gets worse and one gets better; each
  finding gets one attempt. Use for: "efficiency review", "efficiency pass", "is the code efficient",
  "can we get the same behaviour with less code", "is it centralised and modular", "is the code base
  minimal and clear", "why does this keep finding something new". Not for: whether a work's or a code
  area's claims about itself are true (claim-review), a diff (/code-review, methodology-close), the cut
  test on a design object (ners), run time or a performance budget (not covered), P-01..P-15
  (valoria-canon-guard).
---

# EFFICIENT-CODING-REVIEW — the efficiency pass

## Status: RATIFIED on merge of #583 (CLAUDE.md §2, ED-1094). Lane IN; no ED allocated. Invocable as a project skill through `.claude/skills/efficient-coding-review`. Replaces the skill of this name, whose method is now `claim-review`. Requested by Jordan in session, 2026-11-07. The design record is the proposal that #583 landed, retired by its execution (`FORK:` row in `references/restructure_ledger.md`).

## What it owns, and what it copies

**It owns the SEQUENCE, the REPAIR RULE, the END POINT and one rule: the clarity read (L4).** Everything
else is read at its owner, at the row, every time. **Never copy a rule, a table, a count or a threshold
into this file**: a copy rots silently and the next session reads the copy.

| the content | its single owner |
|---|---|
| placement: which layer an artifact binds, prose offered as mechanism, whether a guard earns its existence | `layer-conformance` Lens A |
| unearned artifacts, second owners, dead code, the removal ladder, relocation, the control and its plants | `valoria-simplify` (EARN, OBSERVE C1–C6, DISPOSE, the nine instruments) |
| module shape and Layer-1 conformance; the control's command set and cadence | `layer-conformance` Lens B, THE CONTROL |
| what `engine/season/` and `modules/` must be | `architecture/meta/04_CODE_ARCHITECTURE.md` (§A.2, §C.12, PART D) and `architecture/holonic_ARCHITECTURE.md` §43, §45–§47 |
| a constant invented at the keyboard | `04` PART D row 38; `tools/ci_sim_fabrication_check.py` |
| one round then stop; the pass is a stage, not a deliverable; `needs_jordan`; the request is the scope | `CLAUDE.md` §0 |
| the full suite runs at most once per commit | `CLAUDE.md` §0.4 |
| tiering, fan-out sizing, what makes a critic independent | `CLAUDE.md` §10 |
| code is the mechanism, prose is reference | `CLAUDE.md` §0.05 |

## JORDAN'S DEFINITION

*"Efficiency, for me, is as little code as possible in an extremely clear organized manner that is
centralized and modularity."* Sharpened: *"can we produce the exact same behavior and outcomes with less
code than currently exists? … and can we do so without hard-coding values?"* (Jordan, in session,
2026-11-07.)

**[ASSUMPTION: clarity outranks minimality. Basis: "in an extremely clear organized manner" qualifies the
minimising. Where the two conflict, clarity wins.]**

**The honest limit.** Whether a shorter program with the same behaviour *exists* cannot be computed
(Kolmogorov complexity is uncomputable; program equivalence is undecidable, by Rice's theorem). The end
point is never "the code is minimal". It is *every frozen finding in scope got one attempt, every
accepted change preserved behaviour, and the post-repair tree is recorded.*

## THE OWNERS — each property, and who decides it

| property | the question | owner of the test | counts as a violation |
|---|---|---|---|
| **MODULAR** (hierarchical, isolated, pluggable) | does each scoped module conform to its Layer-1 row, and do levels respect their order? | `layer-conformance` Lens B (both halves of an §A.2 row; B2's grade); `valoria-simplify` I4 | a Lens-B nonconformance (B4's first disposition); an I4 FAILS |
| **CENTRALISED** | does each fact have one owner and one writer? | `valoria-simplify` I3 (`export_sim_params.py --search`, the exporters' `--check`); `layer-conformance` A2 | an I3 FAILS; an A2 finding |
| **MINIMAL** | can the same behaviour be had with less code? | `valoria-simplify`: EARN, C1–C5, the ladder, lookalike-versus-copy | an unearned artifact, or a C5-dead one, that the ladder can remove |
| **NO HARD-CODING** | is a value typed where it belongs in its owner? | `04` PART D row 38; `tools/ci_sim_fabrication_check.py` | a repair that adds one (a hard constraint, H2) |
| **CLEAR** | can a newcomer find what a module does and where its inputs come from? | **this skill** (L4) | one named failed lookup |

**Verdicts are the owners'**: HOLDS, FAILS, INCONCLUSIVE. INCONCLUSIVE is reported with its reason and
never counted as clear.

**Subject.** `engine/season/` and `modules/`, the game code (Layer 2; `CLAUDE.md` §3). Not `tools/`,
`tests/` or `systems/`: a standard pointed at the repository's own apparatus is the recursion
`CLAUDE.md` §0.1 pt 5 exists to stop.

**When to run it.** Routine per-commit conformance is `/close` step 4 and `methodology-close`. This pass is
for the subject-wide questions a diff cannot ask: second owners across modules, subject-wide minimality,
pluggability, the clarity of code nobody has changed. The request is the scope (`CLAUDE.md` §0).

## THE SEQUENCE

Each stage is a *find, then repair* pair. **Findings are frozen at the start of their own stage**, so a
stage never re-reads its own repairs, and a later stage reads the tree as earlier stages left it. That is
the order the owners already rule: Lens A gates B, and `valoria-simplify` runs between them so that B grades
what remains.

| step | does |
|---|---|
| **0 · FRAME** | name the subject; compute the scope and the standard fingerprint (THE END POINT); if the scope is empty, **NOTHING TO DO**, stop |
| **1 · PLACE** | `layer-conformance` Lens A over the scope; repair |
| **2 · DISTIL** | `valoria-simplify` over the units the scope falls in (areas as its M1 defines them): SURVEY to triage, then EARN and the instruments; the owner shows its control before it edits (C2, plants in a worktree, never the working tree); repair by its ladder |
| **3 · CONFORM** | `layer-conformance` Lens B on the scoped modules; repair |
| **4 · CLEAR** | the L4 read, on scoped files this run did not edit; repair. Last, so it never judges code a structural stage is about to delete, and never reads this run's own edits |
| **5 · CLOSE** | the suites once (`layer-conformance` THE CONTROL; `CLAUDE.md` §0.4); a red re-runs the failing file only; a repair the red traces to is reverted and becomes a residual |
| **6 · RECORD** | the reply: violation counts per property before and after, residuals with reasons, controls shown, candidate rules routed; and the trailer line for the commit |

The owners' own stages apply inside steps 1–3 (PRE-FLIGHT, WORK, ATTACK by `valoria-critic`, read-only,
RECONCILE). One producer per package; tiers set per `CLAUDE.md` §10; no lane count is mandated here.

## THE END POINT — what makes a run finish

**E1 · The standard is fixed for a run.** It is this skill's text and the owners' text read at the row.
The trailer's `std=` is the blob hash of this `SKILL.md` alone: a change to a sibling skill does not
reopen the subject. Ask for a whole-subject run if wanted.

**E2 · Scope comes from recorded tree hashes, never from a remembered verdict.**

- A run that commits repairs puts one line in the body of its last commit:
  `Efficiency-Reviewed: engine/season=<tree> modules=<tree> std=<blob> attempted=<n> residual=<n>`.
  Read each `<tree>` from the **index** just before committing: `T=$(git write-tree); git rev-parse
  $T:engine/season $T:modules` (the plain `git rev-parse :engine/season` fails: a directory is not an
  index entry). `std=` is `git rev-parse :skills/efficient-coding-review/SKILL.md`.
- The next run finds the newest such line in the available history:
  `git log -n1 --grep='^Efficiency-Reviewed:' --format=%B`. A squash merge keeps each commit message's
  lines at line start, and the line records tree hashes, not a commit, so it survives a squash or a
  rebase. **It does not deepen a shallow clone** (`valoria-simplify` M5; `CLAUDE.md` §2): no line found
  means the whole subject, once.
- **NOTHING TO DO** when, for every subject path, `git rev-parse HEAD:<path>` equals the recorded tree
  and `std` matches. Stop before reading any code.
- **Otherwise the scope** is `git diff --name-only <recorded-tree> HEAD:<path>` per path, prefixed with
  the path. If `git cat-file -e <recorded-tree>` fails (a tree this clone no longer has), that path's
  scope is the whole path, once. If `std` differs, the whole subject, once.
- **A finding is in scope** if it is located in a scoped file, **or** has an endpoint in one (an import
  edge, a duplicate pair, a second owner), **or** concerns a name on a line the same diff removed
  (deleting a last caller makes its callee dead wherever the callee lives).
- **A violation outside scope is not this run's work**, and nothing records it as owed, so the pass never
  becomes a standing queue (`CLAUDE.md` §0: "does this document create work for a future session?").
- **What this cannot see:** a violation that arises because something *outside* the subject changed (a
  registry row naming a function being deleted; an owner's instrument being revised). Neither reopens the
  subject. Ask for a whole-subject run.

**E3 · Findings are frozen per stage; re-measuring is not re-reviewing.** After each repair the owner's
*cheap* instruments are re-run on what the repair touched (`layer-conformance` THE CONTROL). That is
measurement. The judgment findings (an earned or unearned verdict, an L4 finding) are not re-read. A repair
is never audited in the run that made it (`CLAUDE.md` §0), and the next run starts after it (E2).

**E4 · Each finding gets one attempt; a repair is accepted only if no property gets worse and one gets
better.**

- The measure is **a count per property** (THE OWNERS), componentwise, **never summed, weighted or reported
  as a grade of the code**. That keeps it outside `valoria-simplify`'s "no composite score".
- Accepted: no property's count rises **and** at least one falls (for an L4 repair: the named lookup
  becomes answerable). The conditions of ACCEPTANCE also hold.
- A repair that fixes one property and raises another is **not accepted**; the finding becomes a residual
  with its reason. Otherwise a repair could create violations in files the next run never examines.
- **Termination.** Within a run: each frozen finding gets at most one attempt, and L4 reads a finite set of
  files. Every accepted repair strictly lowers a total drawn from the natural numbers and raises no
  component, so accepted repairs cannot cycle (Floyd, 1967).

**E5 · No rule growth from inside.** An observation that violates no rule is a **candidate rule**, not a
finding. It goes through `CLAUDE.md` §0's five answer-it-first tests. A survivor becomes at most one
`needs_jordan: true` row, and a candidate that already has a row is never raised again. The skill never
adopts a rule.

**E6 · One round** (`CLAUDE.md` §0). The named subject plus its one pass is the stop condition.

**Why it cannot run indefinitely.** Within one run, work is bounded by E4. A run that commits repairs
records the post-repair trees, so the next run's scope is empty unless code changed, and changes originate
outside the skill. A run that commits nothing changes nothing: a repeat costs reading and cannot make the
tree worse or cycle. It can differ only in L4, where a repeat may find a lookup the first run did not; that
finding is repaired, a trailer is written, and the files leave scope. Over an unchanged subject the
sequence of runs is any number of no-op runs, then at most one repairing run, then NOTHING TO DO.

## ACCEPTANCE

**H1 · Same behaviour and outcomes** (hard constraint, never traded against a count).
`layer-conformance` THE CONTROL is the definition, read there: the cheap instruments after every unit, the
suites once at the close, only those the change can reach (`CLAUDE.md` §0.4). A repair that moves the
content hash or a probe verdict has broken something and is reverted. For a deletion or an algorithm
rewrite, add `valoria-simplify` C4's differential run of old against new code. Every exporter's `--check`
passes for a repair that touches an exported chain.

**H2 · No hard-coding** (hard constraint). (a) `tools/ci_sim_fabrication_check.py` passes on the repair's
added lines (the invocation is in THE CONTROL). (b) The repair does not turn a value its code read from its
owner (`engine/engine_params/` or the single Python owner) into a literal. Part (b) is read from the diff,
because the gate accepts a tagged literal (`[JUSTIFIED: …]`, `[DECLARED-DIVERGENCE: …]`) by design.

**The reduction test.** A change offered as a reduction is accepted only if H1 and H2 hold, **and** it
deletes more lines than it adds (`git diff --numstat`), **and** the number of places a reader must open to
predict the behaviour does not rise (`valoria-simplify`: relocation is not reduction). A repair that is not
offered as a reduction (a placement or conformance fix) is not held to the line count.

**L4 · The clarity read** (CONVENTION; the one rule this skill owns). Open a scoped file cold and try to
answer: *what does this module do, and where do its inputs come from?* `claim-review`'s SURVEY row asks
the same of a work (a stranger, ten minutes, judged by doing it); this reads it per module.

- **Scope:** scoped files this run did not edit (an edited file was already held to the reduction test or
  to Lens B).
- **Order:** by cyclomatic complexity, descending (McCabe, 1976), from a throwaway `ast` probe, **to rank
  where to look and nothing more** (`valoria-simplify` I7: rank only, no FAILS). There is no cutoff.
- **Admission:** a finding quotes the lookup, says where the reader looked (file and line) and why it
  failed. "This feels unclear" without a failed lookup is dropped.
- **Repair:** accepted when that same lookup is answerable in the repaired file, no other property's count
  rises, and H1 and H2 hold. The lookup is re-asked once, as the acceptance check; the repaired file is
  not re-read for new findings (E3).

## WHAT THIS PASS MAY NOT PRODUCE

`layer-conformance` WHAT THIS PASS MAY NOT PRODUCE and `valoria-simplify`'s list bind here unchanged:
**no new document** (the reply and the trailer are the output), **no guard, test, tool, scorer or
baseline**, **no composite score**, **no invented threshold**, **no edit to `04` or `architecture/`** to
make a repair fit, **no skipped or weakened test**, **no self-scheduling** (`CLAUDE.md` §11).

## THE FALSIFIERS — how a reader tells whether the pass ran

| the claim | what would show it false |
|---|---|
| *"NOTHING TO DO"* | a source file was opened, or a recorded tree was compared to something other than `HEAD:<path>` |
| *"the scope is the delta"* | the scope was taken from a commit range, or from a remembered verdict, not `git diff` between the recorded tree and `HEAD:<path>` |
| *"a repair was accepted"* | a property's count rose, or no count fell, or H1 or H2 does not hold |
| *"same behaviour"* | the control was not shown to see the artifact (`valoria-simplify` C2), or a deletion has no differential run |
| *"no hard-coding"* | only the gate was run, and the diff was not read for a value turned into a literal |
| *"clear"* | no lookup is quoted, or the repaired file was re-read for new findings |
| *"nothing found"* | no named failed attack, only an absent finding |

**If this skill conflicts with `CLAUDE.md`, `architecture/`, `layer-conformance` or `valoria-simplify`,
they win**; correct the skill.
