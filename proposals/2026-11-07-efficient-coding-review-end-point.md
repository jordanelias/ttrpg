# Efficient-coding-review — a standard to stop at, and an end point the skill cannot run past

## Status: PROPOSED — ratified on merge of its landing PR (CLAUDE.md §2, ED-1094), except §7, which is held back. Terminal by design: executing it deletes it (`FORK:` row, CLAUDE.md §1).

## Date: 2026-11-07 · Lane: IN (cross-cutting) · ED: none allocated (allocated at execution, with the Layer-1 text, §6)

**What this changes in `engine/season/`** (CLAUDE.md §3, `proposals/`): nothing at runtime. It proposes
a code-economy standard *over* `engine/season/` and `modules/`, one behaviour test (M3), and a rewrite
of `skills/efficient-coding-review` around that standard.

**Source.** One session's questions and answers (2026-11-07), re-read in full, with every repo claim
re-opened at its locus. Four of those answers were wrong or have been overtaken since; they are marked
**CORRECTION**.

---

## 0. The answer in one paragraph

The skill repeats because it has nothing to stop at. Its six lenses test whether *claims* are true;
none measures efficiency, and a search for defects in claims has no terminal state. A review finishes
only against a **fixed, finite, ratified standard**. The design below adds no tool, gate, scorer or
baseline, and four properties make it impossible to run indefinitely:

- **Scope.** A run's work is only the code that changed since the last run, so it creates no queue.
- **Order.** Every finding is collected before any repair, so no fix is ever re-reviewed.
- **Bound.** Each violation gets one attempt per run, so a run is finite.
- **No growth from inside.** The skill may not add a rule.

The standard is Jordan's definition of efficiency: as little code as possible, extremely clear,
organised, centralised and modular, sharpened by two questions:
- can the exact same behaviour and outcomes be produced with less code?
- can it be done without hard-coding values?

**The honest limit.** Whether a shorter program with the same behaviour *exists* cannot be computed. The
length of the shortest such program is Kolmogorov complexity, which is uncomputable, and program
equivalence is undecidable in general (Rice). So the end point is never "the code is minimal". It is
"each violation in scope was attempted once, every accepted change preserved behaviour, and the run is
recorded against the commit it produced". Re-opening that takes a change to the code or to the standard.

---

## 1. Findings, by premise

Each premise is a question asked this session. An action marked **§n** is resolved by the proposal
section of that number.

### P1 — "The skill can review the code base, identify issues and propose solutions"

| id | finding | evidence | action |
|---|---|---|---|
| **F1** | **The skill does not measure efficiency, centralisation or modularity.** Its lenses are SURVEY, ACCURACY, APPLICATION, LOGIC, ALL DIRECTIONS and ACROSS MODULES. The last is a *coverage* matrix (does each idea reach each module), not a test of modularity. "Efficient" occurs only in the name and the headings. | `skills/efficient-coding-review/SKILL.md:2,20,190`; STEP 6 at `:170–186` | Rewrite it around Jordan's definition (§3, §4); keep the claim-review method under its own name (§5) |
| **F2** | It hands the structural questions elsewhere: unearned complexity and second owners to `valoria-simplify`, Layer-1 conformance to `layer-conformance`. | `SKILL.md:14–17, 64–67` | The rewrite owns Jordan's four properties and reuses the siblings' instruments rather than duplicating them (§3) |

### P2 — "If it always finds something new, we loop"

| id | finding | evidence | action |
|---|---|---|---|
| **F3** | **Root cause: no reference standard, so no terminal state.** A review can say "this is false", never "this is enough". | the verdict template at `SKILL.md:189–211` has no condition for being finished | §2 |
| **F4** | **No memory between sessions, by design.** The skill writes no file. STEP 0 learns of prior review only from the commit message, the PR body and a critic pass. | `SKILL.md:61–62, 187, 224` | Record each run as a commit trailer and scope the next run from that commit (§2 E2) |
| **F5** | **Re-running it after its own fixes is the forbidden audit→fix→audit shape.** Only the request prevents it. | CLAUDE.md §0, "THE REQUEST IS THE SCOPE" | Findings are collected before repairs; the next run starts *after* the repairs (§2 E2, E3) |
| **F6** | **Sampling:** non-HIGH claims are sampled, so two runs examine different claims. | `SKILL.md:84–86` | Mechanical checks cover all of the run's scope, with no sampling (§3) |
| **F7** | **No consequence floor:** any observation can become a finding. | the verdict template has no admission test | A candidate rule is routed out, never adopted (§2 E5) |

### P3 — "The skill adjudicates whether the code is efficient, centralised, modular"

| id | finding | evidence | action |
|---|---|---|---|
| **F8** | **A standard is decided, not discovered,** so no review can supply it. Theory proves properties against a stated predicate. By Rice's theorem, no general procedure decides an arbitrary non-trivial property of programs. | — | Write each property as predicate + observable + threshold + falsifier (§3) |
| **F9** | **The repo already has a finite structural standard:** `04` PART D, graded STRUCTURAL / MECHANICAL / CONVENTION. | `architecture/meta/04_CODE_ARCHITECTURE.md:66–99` (grades), `:1019–1107` (PART D) | Reuse it rather than restating it (§3) |

### P4 — "The tests should come from software engineering practice and computer science theory"

| id | finding | evidence | action |
|---|---|---|---|
| **F10** | Theory supplies the properties and the ways to prove them, never the threshold for one code base. PART D already restates established principles: Parnas's information hiding (1972); coupling and cohesion (Stevens, Myers and Constantine, 1974); acyclic dependencies; single source of truth (Hunt and Thomas, 1999); types that make the defect impossible to write; non-interference (Goguen and Meseguer, 1982); mutation adequacy (DeMillo, Lipton and Sayward, 1978). | PART D rows 2, 9–12, 22, 28, 38 | Cite the source per rule; adopt only thresholds a source gives (§3) |
| **F11** | **CORRECTION** to an earlier answer: PART D row 11 ("a seat that knows its holder") was mapped to information hiding. It is a one-home-per-relation rule, a sibling of rows 10 and 12. | `04_CODE_ARCHITECTURE.md:1034–1038` | none |

### P5 — Efficiency as run time

| id | finding | evidence | action |
|---|---|---|---|
| **F12** | **No performance instrument exists.** | `[NULL: no perf_counter, timeit or tracemalloc in any .py under tools/, tests/ or engine/; no growth-order statement in requirements.yaml or 04]` | **Out of scope:** P7 defines efficiency as code economy. Held back (§7) |

### P6 — Practice for minimal code, plug-in modules, GDScript, conformance, testing

| id | finding | evidence | action |
|---|---|---|---|
| **F13** | **No type checker or import linter runs.** The jobs that run tests install `pyyaml pytest numpy pytest-xdist`; others install fewer packages. By `04` §0's own rule, every row graded "STRUCTURAL under a checker" is therefore MECHANICAL at runtime. | `.github/workflows/valoria-ci.yml:339, 421` (the four packages); `:98, 211, 476, 584` (fewer); `04:88–92` | **Held back** (§7): a new dependency is a decision |
| **F14** | **CORRECTION:** property-based testing *is* in use, as a method without the library. The invariant sweep, the dice-engine property tests and their mutation-verified predicates all run on the standard library. The earlier "not in use" was wrong in substance. | `engine/season/harness/invariants.py:1–25`; `tests/valoria/test_season_invariant_sweep.py`; `tests/valoria/test_dice_engine_properties.py` | Precedent for standard-library probes (§3) |
| **F15** | **No test shows a module can be added without editing the loop.** | `[NULL: no such test found]` | It becomes M3, the one committed test (§3) |
| **F16** | `tools/ci_module_shape_check.py` runs report-only. It checks reach-ins into `tests/`, not the `04` §A.2 module contract, and has its own unit test. | `.github/workflows/valoria-ci.yml:246` (`w`); its docstring at `:1–30`; `tests/valoria/test_module_shape_check.py` (5 tests) | Not extended; module shape is checked by a probe (§3 L2) |
| **F17** | **No GDScript-subset check exists, and the GDScript claims made this session were not checked** against the docs for the ruled series (ED-GO-0002). | `[NULL: tools/]`; `skills/valoria-simplify/SKILL.md`, the port note | Held back (§7) |
| **F18** | **Precedent risk.** The repo's recursion was generated by doctrine that turned each observation into a permanent artifact: guards on guards, and baseline ratchets that the repo later retired. | `proposals/2026-08-18-breaking-the-recursion.md` §2.1 (`:181–213`); `.github/workflows/valoria-ci.yml:171–173, 253` (retired ratchet and baseline) | No tool, gate, baseline or test of a check (§2, §3) |

### P7 — Jordan's definition: efficiency is as little code as possible, extremely clear and organised, centralised and modular

| id | finding | evidence | action |
|---|---|---|---|
| **F19** | Read literally, "as few lines as possible" conflicts with "extremely clear": golfed code is short and opaque. **[ASSUMPTION: clarity is the constraint and minimality the goal — minimise code without losing clarity; basis: "in an extremely clear organized manner" qualifies the minimising]** | — | Priority order in §3: clarity outranks minimality |
| **F20** | **CORRECTION:** both the line-count ratchet proposed this session and the standing size score of this proposal's first draft are **withdrawn**. The ratchet would block a split that improves clarity; the score is the "composite score" `valoria-simplify` rule 5 forbids. Size enters only per change: a reduction must delete more than it adds. | `skills/valoria-simplify/SKILL.md:204` | §3, the reduction test |
| **F21** | Thresholds: McCabe's complexity ceiling of 10 has a source. No source gives a minimum clone size, so the duplicate rule counts whole functions and needs no size threshold. | McCabe (1976); `valoria-simplify` rule 5 | §3 L1, N2 |

### P8 — "Can the exact same behaviour and outcomes be produced with less code? Without hard-coding values?"

| id | finding | evidence | action |
|---|---|---|---|
| **F22** | **This is the right definition of minimal:** a behaviour-preserving reduction, as in refactoring, which changes structure without changing behaviour (Opdyke, 1992; Fowler, 1999). Whether a shorter equivalent exists cannot be decided (§0). Whether a *given* reduction preserves behaviour can be checked against an observable definition of behaviour. | — | Hard constraint H1 (§3) |
| **F23** | **"The exact same behaviour" needs an observable definition.** A single `content_hash` on one seed can miss a change. A deletion or algorithm rewrite needs a differential run of old against new code that compares intermediate state. A run never proves code dead: dead means no reference. | `skills/valoria-simplify/SKILL.md:129` (C4), `:131` (C5) | H1 and N1 (§3) |
| **F24** | **Hard-coding is already guarded, and the rule is already in Layer 1.** PART D row 38: "a constant invented at the keyboard … MECHANICAL + a numeric-literal scan". `tools/ci_sim_fabrication_check.py` is blocking. It accepts honest provenance tags, including `[DECLARED-DIVERGENCE]`, per Jordan's 2026-07-24 ruling. It scans numbers only, on the changeset. It has a recorded gap at `modules/combat/`, which is a PC-lane decision. A scope-wide "no hard-coded value" gate is the tree-wide guard CLAUDE.md §0.05 refuses. | `04:1067` (row 38); `tools/ci_sim_fabrication_check.py:64–76, 164–170, 515–520`; `.github/workflows/valoria-ci.yml:183` (`v`, blocking); CLAUDE.md §0.05 | H2 reuses the existing gate on each change; no new rule; the `modules/combat/` gap is held back (§3, §7) |
| **F25** | **A reduction that moves logic or knots elsewhere is not a reduction.** Encoding branches as YAML, or moving a knot into a helper or config, leaves the reader holding the same concepts. | `skills/valoria-simplify/SKILL.md:147` ("Relocation is not reduction") | The reduction test adopts that pass condition (§3) |

### Conformance with the repository's own rules (found by the adversarial pass)

| id | finding | evidence | action |
|---|---|---|---|
| **F26** | **The first draft of this proposal conflicted with the ratified `valoria-simplify`:** a new scorer and tool, an invented threshold, a composite score, and blocking guards that code stays simple. | `skills/valoria-simplify/SKILL.md:165, 201–204` | The design adds none of these: existing checks plus throwaway probes in scratch, as `valoria-simplify` rule 4 requires (§3) |
| **F27** | **One active plan per lane.** A multi-position build order ratified on merge would be a second IN plan beside `valoria_master_workplan_v11`. | CLAUDE.md §2; `CURRENT.md:19` | §6 lands as one change, so it is not a plan |

---

## 2. The end point — what makes a review finish

**E1 · A fixed, finite, ratified standard.**
- The rules (§3) live in their own Layer-1 file, `architecture/meta/04_CODE_ARCHITECTURE_part2.md`
  (CLAUDE.md §4's sequential parts), so the file's git blob hash identifies the standard exactly.
- The skill owns the method only and copies no rule.
- The standard is frozen for the length of a run.

**E2 · Scope comes from the last run's commit.**
- Every run ends with one line in the body of the commit that carries its repairs:
  `Efficiency-Reviewed: <subject paths> std=<blob hash of the part2 file> attempted=<n> residual=<n>`.
- The next run finds the newest commit `T` carrying that trailer. In a shallow clone it deepens
  (`git fetch --unshallow`, precedent CLAUDE.md §2) until it finds `T` or history ends.
- **NOTHING TO DO** when, for every subject path, `T:<path>` equals `HEAD:<path>` and `std` matches
  the current file. The run stops before reading any code.
- **Otherwise the scope** is the files changed between `T` and the run's starting `HEAD`. If the
  standard itself changed, the whole subject is in scope once. With no `T` at all, the whole subject is
  in scope once.
- `T` is the commit *with* the repairs, so a run's own edits never fall inside the next run's scope.
- **Violations outside the scope are not the run's work.** That keeps the skill from becoming a standing
  queue (CLAUDE.md §0's test: "does this document create work for a future session?"). Jordan can still
  ask for a whole-subject run; the request is the scope.

**E3 · Findings first, then repairs, never re-read.**
- All findings, mechanical and judgment (L4), are collected from the **starting** tree over the scope.
- Repairs follow. No repair is reviewed again in the same run (CLAUDE.md §0) or in the next one (E2).

**E4 · Each violation gets one attempt; each accepted change must lower the count.**
- A repair is accepted only if it meets the hard constraints (§3) and lowers the run's vector of
  violation counts per rule lexicographically. It must reduce some rule's count without raising the
  count of any rule ranked above it. **This applies to judgment (L4) repairs too.**
- Each violation gets **one** attempt per run. A failed attempt makes it a residual, reported with its
  reason: a change to a mechanic (hand it to `ners`) or a candidate exemption (E5).
- **Termination:** a run is bounded by the number of violations in its scope, so it is finite. The
  lexicographic order on violation counts has no infinite descending chain (Floyd, 1967), so accepted
  repairs also cannot cycle.
- The vector is used only to accept or reject repairs inside one run. It has no weights and no sum, and
  it is never reported as a grade of the code. That keeps it outside `valoria-simplify` rule 5's
  "composite score". The conflict is named here so a reader can judge the distinction.

**E5 · No rule growth from inside.**
- An observation that violates no rule is a **candidate rule**, not a finding.
- It goes through CLAUDE.md §0's five answer-it-first tests. A survivor becomes at most one
  `needs_jordan: true` row, and a candidate that already has a row is never raised again.
- The skill never adopts a rule.

**E6 · Falsifiers are planted in a worktree and never committed.**
- For each probe, plant one violation in a worktree or scratch copy (`valoria-simplify` C2: "never the
  working tree"), confirm the probe sees it, and discard the copy.
- No test of a check is written.

**E7 · One round** (CLAUDE.md §0), unchanged.

**Why this cannot run indefinitely.**
- Within one run, work is bounded by E4.
- Across runs, work exists only where code or the standard changed since `T` (E2). Both changes
  originate outside the skill.
- On an unchanged tree, the second run costs one trailer lookup and one hash comparison.

---

## 3. The standard (proposed Layer-1 text, `04_CODE_ARCHITECTURE_part2.md`)

**Scope:** `engine/season/` and `modules/`, the game code (Layer 2). Not `tools/`, `tests/` or
`systems/` (F18).

**Instruments.** Existing checks, plus throwaway standard-library probes run in scratch and never
committed (`valoria-simplify` rule 4). Nothing here becomes a CI gate. CI keeps running what it already
runs.

**Hard constraints** (never traded against the violation counts):

- **H1 · Same behaviour and outcomes.** All of these must hold:
  - `World.content_hash()` is unchanged on every seed the goldens under `engine/tests/` and the season
    harness already pin;
  - the tests covering the touched files stay green (CLAUDE.md §0.4);
  - every exporter's `--check` passes;
  - for a deletion or an algorithm rewrite, a differential run of old against new code compares
    intermediate state on those seeds (`valoria-simplify` C4).
- **H2 · No hard-coding.** Two halves:
  - the existing blocking `tools/ci_sim_fabrication_check.py` passes on the change's added lines
    (PART D row 38);
  - no value that the code read from its owner (`engine/engine_params/` or the single Python owner)
    becomes a literal. This is checked by reading the diff.

**The reduction test** (Jordan's "the same behaviour with less code"). A change offered as a reduction
is accepted only if:
- H1 and H2 hold;
- it deletes more lines than it adds (`git diff --numstat`);
- the number of places a reader must open to predict the behaviour does not rise (`valoria-simplify`
  `:147`).

**Rules, in priority order** (earlier rules dominate, per E4):

| # | property · rule | violation | instrument | threshold | source |
|---|---|---|---|---|---|
| **1** | **MODULAR** | | | | |
| M1 | dependencies point one way | `engine/season/` imports a module by name; a module imports another module or `engine/season` internals outside a declared seam | existing: `test_importing_every_engine_module_pulls_in_no_subsystem` and the shrink-only `PATH_SEAM_ALLOWED`; a probe (`ast` import scan) for module-to-module imports | 0 in scope | acyclic dependencies; CLAUDE.md §3 (`engine/`); `04` PART D row 2 (`:1027`) |
| M2 | modules keep no state | a module-level mutable binding (list, dict or set literal, `global`) in `modules/` | probe (`ast` scan) | 0 in scope | `04` §A.2; Parnas (1972) |
| M3 | a module can be added without editing the core | a dummy module registered through `composition_roles` cannot run one seeded season unless `engine/season/` is edited | **the one committed test**, in `engine/season/tests/`. It asserts that the dummy's entry point **ran**, because `composition.require` resolves on demand (`engine/substrate/composition.py:43–69`) and an un-entered dummy would pass vacuously | must pass | dependency inversion; the permutation falsifier of PART D row 28 is its analogue |
| **2** | **CENTRALISED** | | | | |
| C1 | one owner per fact | a module-scope constant duplicated across modules; a stale export | existing: `python tools/export_sim_params.py --search`; exporters' `--check` | 0 in scope | single source of truth (Hunt and Thomas, 1999); CLAUDE.md §0.05 |
| C2 | one write path | a write that bypasses the write gate | existing: PART D row 3 and its tests | 0 | `04` §C.2 |
| **3** | **CLEAR** | | | | |
| L1 | bounded complexity | a function with cyclomatic complexity > 10 | probe (`ast` count of decision points + 1) | ≤ 10 | McCabe (1976) |
| L2 | one module shape | a module departing from the `04` §A.2 layout or entry signature | probe, read against `04` §A.2 | 0 in scope | `04` §A.2 |
| L3 | names from one source | a name that does not resolve through `references/names_index.yaml` | existing naming gate | 0 | CLAUDE.md §4 |
| L4 | a newcomer can find things (**CONVENTION**) | a reader opening a scoped file cold cannot find what it does and where its inputs come from | judgment, on the starting tree only (E3) | — | the current skill's SURVEY row |
| **4** | **MINIMAL** | | | | |
| N1 | no dead code | a function with no static non-test caller, no string or registry reference to its name, and no consumer the repository declares outside itself (the port, an exporter) | `valoria-simplify` C5 (`rg` over Python and data files). A coverage run is evidence only, never proof | 0 in scope | `valoria-simplify` C5 |
| N2 | nothing written twice | two functions whose normalised `ast` bodies are identical | probe | 0 in scope | single source of truth; no size threshold is needed (F21) |

**What the standard cannot see** (stated so that no one reads it as complete):
- semantic duplication written differently (`valoria-simplify` I3, on request);
- clarity beyond L1–L3 (L4, judgment);
- whether a mechanic should exist at all (`ners`).

**New apparatus:** one behaviour test (M3). No tool, gate, scorer or baseline.

---

## 4. The skill, rewritten (outline of the new `SKILL.md`)

- **STEP 0 · FRAME.** Name the subject (default: `engine/season/` + `modules/`), find the trailer
  commit `T`, and compute the scope (E2). If the result is **NOTHING TO DO**, stop.
- **STEP 1 · FALSIFIERS.** Plant one violation per probe in a worktree, confirm the probe sees it,
  discard the copy (E6).
- **STEP 2 · FIND.** Run every instrument in §3 over the scope on the starting tree, and do the L4 read.
  This produces all findings (E3).
- **STEP 3 · REPAIR.** Work from the highest-ranked rule down: one attempt per violation, each accepted
  only under E4 and the hard constraints. Reductions also pass the reduction test. A failed attempt
  becomes a residual with its reason.
- **STEP 4 · VERDICT.** The reply: violation counts before and after, residuals with reasons, falsifiers
  shown, candidate rules routed (E5), and the trailer line for the commit. No file.

**Guardrails kept from the current skill:** one round; edits, not documents; re-open any citation before
relaying it; independence is structural, with a `valoria-critic` used only for the L4 read.

---

## 5. What happens to the current skill

Its method is a sound **claim review**, so it is kept under a name that says so: `claim-review`.

- **Its end point:** the same trailer mechanism, keyed on the reviewed work's paths. A work unchanged
  since its trailer commit returns NOTHING TO DO. A high-load claim closes once it rests on an execution
  artifact (CLAUDE.md §0.2); a finding that cannot become one is dropped.
- **References to update in the same commit:**
  - CLAUDE.md:54 (ALL DIRECTIONS, STEP 5);
  - CLAUDE.md:537 (task routing);
  - `skills/premise-check/SKILL.md:71`;
  - the `.claude/skills/efficient-coding-review` symlink, plus a new one for `claim-review`.
- **Not rewritten:** the historical mention in `proposals/2026-10-29-parliament-and-debate/…:711`.

---

## 6. Execution — one change, not a plan

Ratification is the merge of this proposal (ED-1094). Execution is **one** change, so it adds no
position to any plan (F27):

1. allocate an `ED-IN` id and write §3 as `architecture/meta/04_CODE_ARCHITECTURE_part2.md`, indexed
   from `CURRENT.md`'s Layer-1 row;
2. add the M3 test;
3. rewrite `skills/efficient-coding-review` per §4, and move the current method to `claim-review` per §5;
4. delete this proposal, with an exact-file `FORK:` row.

If that cannot land as one change, its remaining items go to `valoria_master_workplan_v11` as IN-lane
positions in the same commit that stops.

---

## 7. Not decided by this merge (held back, per CLAUDE.md §2)

- **A type checker in CI (F13):** `pyright` in strict mode on the §3 scope would make `04`'s
  "STRUCTURAL under a checker" grades true. It is a new CI dependency.
- **A GDScript-subset check (F17):** a portability rule, outside P7's definition. It is owed a check of
  the ruled series' docs first.
- **A performance budget (F12):** outside P7's definition. It would need a stated growth order and a
  time budget per season.
- **`modules/combat/` in the fabrication gate's scope (F24):** a PC-lane decision, already filed under
  ED-IN-0119 (`tools/ci_sim_fabrication_check.py:164–170`). Not taken here.

---

## 8. Falsifiers for this proposal

- **Idempotence:** run the rewritten skill twice on an unchanged tree. The second run must stop at
  STEP 0 with NOTHING TO DO and open no source file. If it reports anything else, E2 is broken.
- **Scope:** add a duplicate function to one file in `modules/` and commit it. The next run's scope must
  be exactly that file. N2 must find the duplicate, the repair must pass H1 and the reduction test, and
  the run after that must return NOTHING TO DO.
- **Same behaviour:** in a worktree, plant a false reduction that deletes one executing branch whose
  effect reaches world state. H1 must go red. If it stays green, H1 cannot see the change and is paper.
- **No hard-coding:** in a worktree, replace one value read from `engine/engine_params/` with an
  uncited literal. The fabrication gate must go red. Then add a `[JUSTIFIED: …]` tag: the gate passes,
  and H2's second half (reading the diff) must still refuse it.
- **No growth:** executing this proposal must add exactly one test (M3), and no tool, gate, baseline or
  test of a check. Anything more and F18's failure has recurred.
