# Efficient-coding-review — a standard to stop at, and an end point the skill cannot run past

## Status: PROPOSED — decision requested from Jordan. Terminal by design: executing it deletes it (`FORK:` row, CLAUDE.md §1).

## Date: 2026-11-07 · Lane: IN (cross-cutting) · ED: none allocated (allocated at execution, with the Layer-1 amendment, §6)

**What this changes in `engine/season/`** (CLAUDE.md §3, `proposals/`): nothing at runtime. It proposes
a code-economy standard *over* `engine/season/` and `modules/`, the checks that measure it, and a
rewrite of `skills/efficient-coding-review` around that standard.

**Source.** One session's six questions and answers (2026-11-07), re-read in full, with every repo claim
re-opened at its locus. Four of those answers were wrong or have been overtaken since; they are marked
**CORRECTION** below rather than silently restated.

---

## 0. The answer in one paragraph

The skill repeats because it has nothing to stop at. Its six lenses test whether *claims* are true;
none measures efficiency, and a search for defects in claims has no terminal state. A review finishes
only against a **fixed, finite, ratified standard**, measured by checks that **compute** the end state from
the tree rather than remembering it. Three properties then make it impossible to run indefinitely:

- **Variant.** Every accepted fix strictly lowers a vector of violation counts, which cannot fall below
  zero (a ranking function: Floyd, 1967).
- **Idempotence.** An unchanged tree under an unchanged standard returns NOTHING TO DO at the first step.
- **No growth from inside.** The skill may not add a rule; a rule changes only by Layer-1 ratification.

The standard is Jordan's definition of efficiency: as little code as possible, extremely clear,
organised, centralised and modular, sharpened by two questions (P8):
- can the exact same behaviour and outcomes be produced with less code?
- can it be done without hard-coding values?

It is written below as thirteen rules over four properties, each with a check and a threshold.

**The honest limit.** Whether a shorter program with the same behaviour *exists* cannot be computed. The
length of the shortest such program is Kolmogorov complexity, which is uncomputable, and program
equivalence is undecidable in general (Rice). So the end point is never "the code is minimal". It is
**"no further behaviour-preserving reduction was found, and that fact is recorded against this exact
tree"**. Re-opening it takes a change to the tree or to the standard.

---

## 1. Findings, by premise

Each premise is a question asked this session. Every finding gives its evidence and an action; an action
marked **§n** is resolved by the proposal section of that number.

### P1 — "The skill can review the code base, identify issues and propose solutions"

| id | finding | evidence | action |
|---|---|---|---|
| **F1** | **The skill does not measure efficiency, centralisation or modularity.** Its lenses are SURVEY, ACCURACY, APPLICATION, LOGIC, ALL DIRECTIONS and ACROSS MODULES. The last is a *coverage* matrix (does each idea reach each module), not a test of modularity. "Efficient" occurs only in the name and the headings. | `skills/efficient-coding-review/SKILL.md:2,20,190`; STEP 6 at `:170–186` | Rewrite it around Jordan's definition (§3, §4); move the claim-review method to a name that says what it does (§5) |
| **F2** | It hands the structural questions elsewhere: unearned complexity and second owners to `valoria-simplify`, Layer-1 conformance to `layer-conformance`. | `SKILL.md:14–17, 64–67` | The rewrite owns Jordan's four properties; the siblings keep their own jobs, which never duplicate a check (§3) |

### P2 — "If it always finds something new, we loop"

| id | finding | evidence | action |
|---|---|---|---|
| **F3** | **Root cause: no reference standard, so no terminal state.** A review can say "this is false", never "this is enough". | the lens list (F1); the verdict template at `SKILL.md:189–211` has no condition for being finished | §2 E1–E2 |
| **F4** | **No memory between sessions, by design.** The skill writes no file. STEP 0 learns of prior review only from the commit message, the PR body and a critic pass. | `SKILL.md:61–62, 187, 223` | Compute the end point from the tree; key the judgment lens to a commit trailer (§2 E3, E5) |
| **F5** | **Re-running it after its own fixes is the forbidden audit→fix→audit shape.** Only the request prevents it. | CLAUDE.md §0, "THE REQUEST IS THE SCOPE" | Idempotence: an unchanged tree returns NOTHING TO DO (§2 E3) |
| **F6** | **Sampling:** non-HIGH claims are sampled, so two runs examine different claims. | `SKILL.md:84–86` | The new checks run over the whole subject, with no sampling (§3) |
| **F7** | **No consequence floor:** any observation can become a finding. | the verdict template has no admission test | Apply CLAUDE.md §0.1 pt 5's predicate; route a candidate rule out, never adopt it (§2 E6) |

### P3 — "The skill adjudicates whether the code is efficient, centralised, modular"

| id | finding | evidence | action |
|---|---|---|---|
| **F8** | **A standard is decided, not discovered,** so no review can supply it. Theory proves properties against a stated predicate. By Rice's theorem, no general procedure decides an arbitrary non-trivial property of programs. | — | Write each property as predicate + observable + threshold + falsifier + grade (§3) |
| **F9** | **The repo already has a finite structural standard:** `04` PART D, graded STRUCTURAL / MECHANICAL / CONVENTION. | `architecture/meta/04_CODE_ARCHITECTURE.md:66–99, 1019–1048` | The modular and centralised rules reuse it rather than restating it (§3) |

### P4 — "The tests should come from software engineering practice and computer science theory"

| id | finding | evidence | action |
|---|---|---|---|
| **F10** | Theory supplies the properties and the ways to prove them, never the threshold for one code base. PART D already restates established principles: Parnas's information hiding (1972); coupling and cohesion (Stevens, Myers and Constantine, 1974); acyclic dependencies; single source of truth (Hunt and Thomas, 1999); types that make the defect impossible to write; non-interference (Goguen and Meseguer, 1982); mutation adequacy (DeMillo, Lipton and Sayward, 1978). | PART D rows 2, 9–12, 22 | Cite the source per rule, and label every threshold that has none (§3) |
| **F11** | **CORRECTION** to an earlier answer: PART D row 11 ("a seat that knows its holder") was mapped to information hiding. It is a one-home-per-relation rule, a sibling of rows 10 and 12. | `04_CODE_ARCHITECTURE.md:1034–1038` | none |

### P5 — Efficiency as run time

| id | finding | evidence | action |
|---|---|---|---|
| **F12** | **No performance instrument exists:** no timing, benchmark or memory-profile code, and no stated growth order. | `[NULL: tests/, engine/tests, engine/season/tests, tools/ searched for perf_counter, timeit, benchmark, tracemalloc, time budget; requirements.yaml and 04 for growth-order statements]` | **Out of scope:** P7 defines efficiency as code economy. Kept as a separate decision (§7) |

### P6 — Practice for minimal code, plug-in modules, GDScript, conformance, testing

| id | finding | evidence | action |
|---|---|---|---|
| **F13** | **No type checker or import linter runs, and CI installs four packages only.** By `04` §0's own rule, every row graded "STRUCTURAL under a checker" is therefore MECHANICAL at runtime. | `git grep` for mypy, pyright, import-linter, vulture, mutmut: none in config or code; `engine/season/harness/invariants.py:19–21` (the CI package list) | **Held back** (§7): a new dependency is a decision. The rules in §3 are written to need none |
| **F14** | **CORRECTION:** property-based testing *is* in use, as a method without the library. The invariant sweep, the dice-engine property tests and their mutation-verified predicates all run on the standard library. The earlier "not in use" was wrong in substance. | `engine/season/harness/invariants.py:1–25`; `tests/valoria/test_season_invariant_sweep.py`; `tests/valoria/test_dice_engine_properties.py` | Precedent for building every check in §3 on the standard library alone |
| **F15** | **No test shows a module can be added without editing the loop.** | `[NULL: no such test found]` | It becomes rule M3, the falsifier for "modular" (§3) |
| **F16** | `tools/ci_module_shape_check.py` runs report-only. It checks reach-ins into `tests/`, not the `04` §A.2 module contract. | `.github/workflows/valoria-ci.yml:246` (the `w` prefix); its docstring at `:1–30` | The module-shape rules extend this tool, so one owner holds module shape (§3, §6) |
| **F17** | **No GDScript-subset check exists, and the GDScript claims made this session were not checked** against the docs for the ruled series (ED-GO-0002). | `[NULL: tools/]`; `skills/valoria-simplify/SKILL.md` port note | **Out of scope:** portability is not in P7's definition. Kept as a separate decision (§7) |
| **F18** | **Precedent risk.** The repo's recursion was generated by doctrine that turned each observation into a permanent artifact, including guards on guards. Any checks proposed here must not reproduce it. | `proposals/2026-08-18-breaking-the-recursion.md` §2.1 (`:181–213`), §5.1 (`:411–437`); CLAUDE.md §0.1 pt 5 | Scope the checks to game code; show each falsifier by planting a violation and reverting it, never as a committed test of the check (§2 E7, §3) |

### P7 — Jordan's definition: efficiency is as little code as possible, extremely clear and organised, centralised and modular

| id | finding | evidence | action |
|---|---|---|---|
| **F19** | Read literally, "as few lines as possible" conflicts with "extremely clear": golfed code is short and opaque. **[ASSUMPTION: clarity is the constraint and minimality the goal — minimise code without losing clarity; basis: "in an extremely clear organized manner" qualifies the minimising]** | — | Priority order in §3: clarity outranks minimality |
| **F20** | **CORRECTION:** the line-count ratchet proposed this session ("lines grow only with behaviour") is **withdrawn**. As a CI gate it would block a split that improves clarity, contradicting F19's priority order. Size returns in §3 as N0, measured in syntax-tree nodes and ranked **last** in *V*. A clarity fix lowers a higher-ranked count, so it is accepted even when size rises; size decides only between changes that tie on everything above it. | — | §3 N0 |
| **F21** | Two thresholds are owed: the clone size and the complexity ceiling. | — | Defaults in §3, one with a source and one labelled as a reviewer's default |

### P8 — "Can the exact same behaviour and outcomes be produced with less code? Without hard-coding values?"

| id | finding | evidence | action |
|---|---|---|---|
| **F22** | **This is the right definition of minimal:** a behaviour-preserving reduction, as in refactoring, which changes structure without changing behaviour (Opdyke, 1992; Fowler, 1999). Whether a shorter equivalent exists cannot be decided (§0, the honest limit). Whether a *given* reduction preserves behaviour can be checked against an observable definition of behaviour. | — | Make behavioural equivalence a hard constraint on every fix (§2 E2); add size as N0 (§3) |
| **F23** | **"The exact same behaviour" needs an observable definition.** A single `content_hash` on one seed can miss a change. `valoria-simplify` C4 says so, and asks for a differential run of old against new code that compares intermediate state for any change that rewrites an algorithm or deletes executing code. | `skills/valoria-simplify/SKILL.md:129` | §2 E2 defines equivalence as: the seeds the goldens already pin, the touched files' tests, and the C4 differential run for deletions and algorithm rewrites |
| **F24** | **Hard-coding is partly guarded today, and more weakly than P8 asks.** `tools/ci_sim_fabrication_check.py` is blocking and covers `engine/season/`. It accepts a literal that carries a `# [canonical: …]` comment, so a value can still be cited *in code*. It has a recorded known gap at `modules/combat/`. CLAUDE.md §0.05 asks for more: a fact the engine uses lives in a typed artifact under `engine/engine_params/` or a single Python owner. | `tools/ci_sim_fabrication_check.py:1–25, 164–167`; `.github/workflows/valoria-ci.yml:102, 183` (`v` = blocking); CLAUDE.md §0.05 | Rule C3 (§3), added as a stricter mode of that same tool so one owner holds "literal in game code". Introducing a hard-coded value is a hard constraint, never a trade (§2 E2) |
| **F25** | **A reduction that moves logic into data is not a reduction.** Encoding branches as YAML shrinks the Python and grows a second language: `valoria-simplify`'s "a knot moved, not loosened". Moving a *value* to its owner is right; moving *logic* to data is not. | `skills/valoria-simplify/SKILL.md` (the DISTIL list in its description) | N0 counts code; any data a change adds must be values or rows, never conditions or control flow (§3 N0) |

---

## 2. The end point — what makes a review finish

**E1 · A fixed, finite, ratified standard.**
- The rules (§3) live in Layer 1, as an amendment to `04` (§6).
- The checks live in `tools/` (Layer-1 scripts).
- The skill owns the method only, and copies no rule.
- The standard is frozen for the length of a run.

**E2 · A variant that must fall.**
- *V* is the vector of violation counts per rule, taken in the priority order of §3.
- A fix is accepted only if *V* falls lexicographically: it reduces some rule's count without raising
  the count of any rule ranked above it.
- It must also meet two **hard constraints**, which are never traded against *V*:
  1. **Same behaviour and outcomes (F22, F23).** `World.content_hash()` is unchanged on every seed the
     goldens under `engine/tests/` and the season harness already pin; the tests covering the touched
     files stay green (CLAUDE.md §0.4); and, for a deletion or an algorithm rewrite, a differential run
     of old against new code compares intermediate state on those seeds (`valoria-simplify` C4).
  2. **No value hard-coded (F24).** The fix introduces no game value as a literal in the §3 scope. A
     value it needs is read from its owner (`engine/engine_params/` or the single Python owner).
- A fix that moves the hash is a change to a mechanic. It is reverted and handed to `ners`.
- *V* is a vector of natural numbers under lexicographic order, which has no infinite descending chain.
  The repair loop therefore terminates, at *V* = 0 or at a set of **residuals** no accepted fix can
  reduce (Floyd, 1967, termination by a well-founded ranking function).

**E3 · Idempotence: the end state is computed, not remembered.**
- Every run ends with one commit-message trailer:
  `Efficiency-Reviewed: <subject> tree=<git rev-parse HEAD:<path> per path> standard=<blob hash of the rule section> V=<vector> residual=<n>`.
- The next run compares the current tree and standard hashes with the trailer. If both match, the
  verdict is **NOTHING TO DO** and the run stops before reading any code.
- A trailer is one line of the commit body, which the pass is already allowed (CLAUDE.md §0, "at most
  one paragraph in the commit message"). It creates no file and no queue.

**E4 · The baseline only shrinks.**
- At adoption, each check records the existing violations as a baseline. CI fails only on a violation
  above the baseline (the precedent is `PATH_SEAM_ALLOWED`, which only shrinks).
- The skill's work is to lower the baseline.
- A genuine exception is written into the **rule** (for example, "Godot export entry points are
  exempt"), which is a Layer-1 edit. It is never added to a list. The baseline has no path to grow.

**E5 · The judgment lens is bounded by scope.**
- The one non-mechanical check, the newcomer clarity read (§3 L4), covers only files whose content
  differs from the tree named in the last trailer.
- No trailer reachable in a shallow clone: deepen it (`git fetch --unshallow`, precedent CLAUDE.md §2).
  Never any trailer: run the read over the whole subject once, and write the first trailer.

**E6 · No rule growth from inside.**
- An observation that violates no rule is a **candidate rule**, not a finding.
- It goes through CLAUDE.md §0's five answer-it-first tests. A survivor becomes at most one
  `needs_jordan: true` row.
- The skill never adopts a rule. That keeps the standard finite, and keeps E2 and E3 meaningful.

**E7 · Falsifiers are planted and reverted, never committed.**
- Each run plants one violation per check, confirms the check goes red, and reverts: *k* checks give *k*
  plants, a bounded cost.
- No test of a check is written. That is the guard-on-guard shape F18 rules out.

**E8 · One round** (CLAUDE.md §0), unchanged.

**Why this cannot run indefinitely.**
- Within one run, the work is bounded by E2.
- Across runs, new work can come only from a change to the tree or a ratified change to the standard.
  Both originate outside the skill.
- On an unchanged tree, E3 makes the second run cost one hash comparison.

---

## 3. The standard (proposed Layer-1 amendment)

**Scope:** `engine/season/` and `modules/`, the game code (Layer 2). Not `tools/`, `tests/` or
`systems/`: F18 rules out pointing a standard at the repository's own apparatus.

**Hard constraints, outside *V*:** same behaviour and outcomes, and no value hard-coded, both as defined
in §2 E2. A fix that moves the hash is a mechanic; it goes to `ners`.

**Rules, in priority order** (lexicographic; earlier rules dominate). Every check is standard-library
only (F13, F14).

| # | property · rule | predicate (violation) | check | threshold | source |
|---|---|---|---|---|---|
| **1** | **MODULAR** | | | | |
| M1 | dependencies point one way | `engine/season/` imports a module by name; a module imports another module or `engine/season` internals outside a declared seam | the existing subprocess import test, plus an `ast` import scan of `modules/` added to `ci_module_shape_check.py` | 0 above baseline | acyclic dependencies; `04` PART D row 22 |
| M2 | modules keep no state | module-level mutable binding (list, dict or set literal, `global`) in `modules/` | `ast` scan in `ci_module_shape_check.py` | 0 above baseline | `04` §A.2; Parnas (1972) |
| M3 | a module can be added without editing the core | a dummy module registered through `composition_roles` cannot run one seeded season unless `engine/season/` is edited | one test in `engine/season/tests/` | must pass | dependency inversion; F15 |
| **2** | **CENTRALISED** | | | | |
| C1 | one owner per fact | a module-scope constant duplicated across modules; a stale export | existing: `python tools/export_sim_params.py --search`, exporters' `--check` | 0 above baseline | single source of truth (Hunt and Thomas, 1999); CLAUDE.md §0.05 |
| C2 | one write path | a write that bypasses the write gate | existing: `04` PART D row 3 and its tests | 0 | `04` §C.2 |
| C3 | no hard-coded game value | a numeric or string literal standing for a game fact in the §3 scope, **cited or not**. Exempt: the structural numbers `ci_sim_fabrication_check.py` already exempts, and literals inside the owner modules themselves | a stricter mode of `ci_sim_fabrication_check.py` over `engine/season/` + `modules/`, `modules/combat/` included (F24) | 0 above baseline | CLAUDE.md §0.05, §5 |
| **3** | **CLEAR** (mechanical part) | | | | |
| L1 | bounded complexity | a function with cyclomatic complexity > 10 | `ast` count of decision points + 1, in the new `tools/code_economy.py` | ≤ 10 | McCabe (1976) |
| L2 | one module shape | a module departing from the `04` §A.2 layout or entry signature | `ci_module_shape_check.py` | 0 above baseline | `04` §A.2 |
| L3 | names from one source | a name that does not resolve through `references/names_index.yaml` | existing naming gate | 0 | CLAUDE.md §4 |
| L4 | a newcomer can find things (**CONVENTION**, outside *V*) | a reader opening a changed file cold cannot find what it does and where its inputs come from | judgment, scoped by E5 | — | the current skill's SURVEY row |
| **4** | **MINIMAL** | | | | |
| N1 | no code that never runs | a function never entered by the tests covering the subject plus one seeded season | `python -m trace --listfuncs`, run in a single process (xdist workers would split the count), in `tools/code_economy.py` | 0 above baseline; each removal confirmed by `valoria-simplify` C4 (edit, rerun, no change) | dead-code removal; `valoria-simplify` I1 |
| N2 | nothing written twice | identical normalised `ast` subtrees of ≥ 6 statements | `tools/code_economy.py` | 0 above baseline | **reviewer's default — no source gives a size** (`valoria-simplify` rule 5) |
| N0 | **less code for the same behaviour** (last in *V*) | — (a quantity, not a violation): the count of syntax-tree nodes in the §3 scope. Nodes, not lines, so formatting and comments do not count. Data a change adds must be values or rows, never conditions or control flow (F25) | `tools/code_economy.py` | lower is better; never a gate; ranked last, so it never overrides clarity or structure (F20) | Opdyke (1992); Fowler (1999) |

**What the standard cannot see** (stated so that no one reads it as complete):
- semantic duplication written differently (`valoria-simplify` I3, on request);
- clarity beyond L1–L3 (L4, judgment);
- whether a mechanic should exist at all (`ners`).

**New apparatus:** one new tool (`tools/code_economy.py`), two extended tools
(`ci_module_shape_check.py`, `ci_sim_fabrication_check.py`) and one test (M3). Every other rule reuses
a check that exists today.

---

## 4. The skill, rewritten (outline of the new `SKILL.md`)

- **STEP 0 · FRAME.** Name the subject (default: `engine/season/` + `modules/`), the hash of the
  standard, and the last `Efficiency-Reviewed:` trailer (E3).
- **STEP 1 · MEASURE.** If the tree and standard hashes match the trailer: **NOTHING TO DO**; stop.
  Otherwise run the checks and compute *V*.
- **STEP 2 · FALSIFIERS.** Plant one violation per check, confirm red, revert (E7).
- **STEP 3 · REPAIR.** Work from the highest-ranked rule down. Accept a fix only under E2; revert
  anything else. A violation no fix can reduce is a residual, with its reason: a mechanic (hand it to
  `ners`) or a candidate exemption (E6).
- **STEP 4 · CLARITY.** The L4 read over changed files only (E5). Each finding is fixed now or dropped.
  If it reveals a gap in the rules, it is a candidate rule (E6).
- **STEP 5 · VERDICT.** The reply: *V* before and after, the residuals with reasons, the falsifiers
  shown, and the trailer line. No file.

**Guardrails kept from the current skill:** one round; edits, not documents; re-open any citation before
relaying it; independence is structural, with a `valoria-critic` used only for STEP 4.

---

## 5. What happens to the current skill

Its method is a sound **claim review**, so it is kept under a name that says so: `claim-review`.

- **Its end point:** the same trailer mechanism, keyed on the reviewed work's file hashes. A work whose
  hashes match its trailer returns NOTHING TO DO. A high-load claim closes once it rests on an execution
  artifact (CLAUDE.md §0.2); a finding that cannot become one is dropped.
- **References to update in the same commit:**
  - CLAUDE.md:54 (ALL DIRECTIONS, STEP 5);
  - CLAUDE.md:537 (task routing);
  - `skills/premise-check/SKILL.md:71`;
  - the `.claude/skills/` symlink.
- **Not rewritten:** the historical mention in `proposals/2026-10-29-parliament-and-debate/…:711`.

---

## 6. Build order

1. **Ratify** (the merge of this proposal, ED-1094). At execution: allocate an `ED-IN` id and write §3
   as a new subsection of `04` Part A, Jordan-directed, as `04`'s earlier amendments were.
2. **Extend `ci_module_shape_check.py`** with M1 (the `modules/` half), M2 and L2. Keep it report-only
   and record the baseline.
3. **Add `tools/code_economy.py`** with L1, N0, N1 and N2, standard library only. **Add C3** as a
   stricter mode of `ci_sim_fabrication_check.py`, report-only, with the baseline recorded. Report-only, baseline
   recorded, and registered in `references/ci_checks_registry.yaml`.
4. **Add the M3 plug-in test.**
5. **Rewrite `skills/efficient-coding-review`** per §4; move the current method to `claim-review` per §5.
6. **Move the §3 checks to blocking**, so that CI fails on a violation above the baseline.
7. **Delete this proposal**, with an exact-file `FORK:` row.

---

## 7. Not decided by this merge (held back, per CLAUDE.md §2)

- **A type checker in CI (F13):** `pyright` in strict mode on the §3 scope would make `04`'s
  "STRUCTURAL under a checker" grades true. It is a new CI dependency.
- **A GDScript-subset check (F17):** a portability rule, outside P7's definition. It is owed a check of
  the ruled series' docs first.
- **A performance budget (F12):** outside P7's definition. If wanted, it needs a stated growth order
  (derivable, an engineering answer) and a time budget per season (a design choice).

---

## 8. Falsifiers for this proposal

- **Idempotence:** run the rewritten skill twice on an unchanged tree. The second run must stop at
  STEP 1 with NOTHING TO DO and open no source file. If it reports anything else, E3 is broken.
- **Variant:** plant a duplicate block of ≥ 6 statements in `modules/`. *V*'s N2 count must rise by
  one, the run must remove it, and *V* must return to its prior value.
- **Same behaviour:** plant a false reduction, deleting one executing branch whose effect reaches world
  state, and confirm the hard-constraint run goes red. If it stays green, the equivalence definition
  cannot see the change and E2's first constraint is paper.
- **No hard-coding:** replace one value read from `engine/engine_params/` with its literal. C3 must go
  red, and the run must refuse the change even if *V* fell.
- **No growth:** across the build, no test whose subject is a §3 check may appear. If one does, F18's
  failure has recurred and this proposal has failed by its own measure.
