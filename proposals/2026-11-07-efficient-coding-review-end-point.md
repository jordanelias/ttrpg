# Efficient-coding-review — Jordan's efficiency standard, as a sequence over the owners that already exist, with an end point it cannot run past

## Status: PROPOSED — ratified on merge of its landing PR (CLAUDE.md §2, ED-1094), except §8, which is held back. Terminal by design: executing it deletes it (`FORK:` row, CLAUDE.md §1).

## Date: 2026-11-07 · Lane: IN (cross-cutting) · ED: none allocated

**What this changes in `engine/season/`** (CLAUDE.md §3, `proposals/`): nothing. It adds no code, no test, no tool, no gate, no scorer and no baseline. It rewrites one skill, renames the method that skill currently holds, and retargets four references.

**Source.** One session's questions and answers (2026-11-07), re-read in full, then attacked once by an independent read-only critic, then re-checked against the sibling skills and the code. Every repo claim below was re-opened at its locus. Five earlier answers were wrong or overtaken; they are marked **CORRECTION**.

---

## 0. The answer in one paragraph

`skills/efficient-coding-review` can be re-run without end because it has no standard to stop at: its lenses test whether *claims* are true, which has no terminal state. Jordan's definition of efficiency is a standard, but almost every rule in it already has an owner: `valoria-simplify` owns "same behaviour, less code" and "one owner per fact"; `layer-conformance` owns module shape and placement; the blocking fabrication gate owns hard-coded values. A new rule set would duplicate them (§1 P10). So the rewritten skill **owns no rule except one**, the clarity read. It owns a **sequence** over the owners, a **repair rule** (no property gets worse, one gets better), and an **end point**: a run's work is only the code that changed since the last run's recorded tree, found by comparing git tree hashes, so an unchanged subject returns NOTHING TO DO and a changed one yields only the delta.

**The honest limit.** Whether a shorter program with the same behaviour *exists* cannot be computed (Kolmogorov complexity is uncomputable; program equivalence is undecidable, by Rice's theorem). The end point is therefore never "the code is minimal". It is "every frozen finding in scope got one attempt, every accepted change preserved behaviour, and the post-repair tree is recorded".

---

## 1. Findings, by premise

An action marked **§n** is resolved by that section of this proposal.

### P1 — "The skill can review the code base, identify issues and propose solutions"

| id | finding | evidence | action |
|---|---|---|---|
| **F1** | **The skill does not measure efficiency, centralisation or modularity.** Its lenses are SURVEY, ACCURACY, APPLICATION, LOGIC, ALL DIRECTIONS and ACROSS MODULES. The last is a *coverage* matrix (does each idea reach each module), not a test of modularity. "Efficient" occurs only in the name and headings. | `skills/efficient-coding-review/SKILL.md:2,20,190`; STEP 6 `:170–186` | Give it Jordan's definition and a sequence (§2, §3); keep the claim-review method under its own name (§6) |
| **F2** | Its own description hands the structural questions to siblings: unearned complexity to `valoria-simplify`, Layer-1 conformance to `layer-conformance`. | `SKILL.md:14–17, 64–67` | The rewrite sequences those owners instead of competing with them (§2) |

### P2 — "If it always finds something new, we loop"

| id | finding | evidence | action |
|---|---|---|---|
| **F3** | **Root cause: no reference standard, so no terminal state.** | the verdict template, `SKILL.md:189–211`, has no condition for being finished | §4 |
| **F4** | **No memory between sessions, by design.** The skill writes no file; STEP 0 learns of prior review only from the commit message, PR body and a critic pass. | `SKILL.md:61–62, 187, 224` | A trailer keyed on git tree hashes (§4 E2) |
| **F5** | **Re-running after its own fixes is the forbidden audit→fix→audit shape**; only the request prevents it. | CLAUDE.md §0, "THE REQUEST IS THE SCOPE" | The trailer records the *post-repair* tree, so the next run starts after the fixes (§4 E2) |
| **F6** | **Sampling:** non-HIGH claims are sampled, so two runs examine different claims. | `SKILL.md:84–86` | The owners' instruments run over all of the scope, not a sample (§3) |
| **F7** | **No consequence floor.** | no admission test in the verdict template | A candidate rule is routed out, never adopted (§4 E5); an L4 finding needs a named failed lookup (§5) |

### P3 — "The skill adjudicates whether the code is efficient, centralised, modular"

| id | finding | evidence | action |
|---|---|---|---|
| **F8** | **A standard is decided, not discovered**; no review supplies it. Theory proves a property against a stated predicate; by Rice's theorem no general procedure decides an arbitrary non-trivial property of programs. | — | §2 maps each of Jordan's properties to the owner whose instrument decides it |
| **F9** | **The repo already has a finite structural standard**: `04` PART D, graded STRUCTURAL / MECHANICAL / CONVENTION. | `04_CODE_ARCHITECTURE.md:66–99` (grades), `:1019–1107` (PART D) | Read at the row by `layer-conformance` Lens B; copied nowhere |

### P4 — "The tests should come from software engineering practice and computer science theory"

| id | finding | evidence | action |
|---|---|---|---|
| **F10** | Theory supplies properties and ways to prove them, never the threshold for one code base. PART D restates established principles: information hiding (Parnas, 1972); coupling and cohesion (Stevens, Myers and Constantine, 1974); acyclic dependencies; single source of truth (Hunt and Thomas, 1999); non-interference (Goguen and Meseguer, 1982); mutation adequacy (DeMillo, Lipton and Sayward, 1978). | PART D rows 2, 3, 9–12, 22, 28, 38 | Cite per rule where a rule is stated (§2); adopt no threshold a source does not give |
| **F11** | **CORRECTION:** PART D row 11 ("a seat that knows its holder") was mapped to information hiding. It is a one-home-per-relation rule, a sibling of rows 10 and 12. | `04:1034–1038` | none |

### P5 — Efficiency as run time

| id | finding | evidence | action |
|---|---|---|---|
| **F12** | **No performance instrument exists.** | `[NULL: no perf_counter, timeit or tracemalloc in any .py under tools/, tests/ or engine/; no growth-order statement in requirements.yaml or 04]` | Out of scope (Jordan's definition is code economy). §8 |

### P6 — Practice for minimal code, plug-in modules, GDScript, conformance, testing

| id | finding | evidence | action |
|---|---|---|---|
| **F13** | **No type checker or import linter runs.** Test jobs install `pyyaml pytest numpy pytest-xdist`; others install fewer. By `04` §0's own rule, every row graded "STRUCTURAL under a checker" is MECHANICAL at runtime. | `.github/workflows/valoria-ci.yml:339, 421` (four packages), `:98, 211, 476, 584` (fewer); `04:88–92` | Held back (§8): a new dependency |
| **F14** | **CORRECTION:** property-based testing *is* in use, as a method without the library. | `engine/season/harness/invariants.py:1–25`; `tests/valoria/test_season_invariant_sweep.py`; `tests/valoria/test_dice_engine_properties.py` | none |
| **F15** | **CORRECTION: "a module can be plugged in by registry row alone, and a test should prove it" was wrong on both counts.** A row attaches an entry through `engine/substrate/composition.py` and the registrar; the loop-side adapter that *calls* it is host code by ruling (A-25, ED-IN-0284, ED-IN-0285; `holonic_ARCHITECTURE.md` §43, §44.3). And `tests/valoria/test_module_registrar.py` already plants rows, each case in a fresh subprocess, and checks registration at construction and refusal of a malformed row. Whether a planted `verb_call` row is *dispatched by a season* is not tested. | `engine/season/manifest/registrar.py:1–60`; `engine/substrate/composition.py:1–25`; `tests/valoria/test_module_registrar.py:134, 262–336` | No new test. The "pluggable" question is a Lens B question (§2); the dispatch gap, if it is one, is a finding that run reports |
| **F16** | `tools/ci_module_shape_check.py` runs report-only and `layer-conformance` already ranks its output as evidence, not a Layer-1 verdict. | `valoria-ci.yml:246` (`w`); `skills/layer-conformance/SKILL.md:152–156` | Not extended (§2) |
| **F17** | **No GDScript-subset check exists, and the GDScript claims made this session were not checked** against the docs for the ruled series (ED-GO-0002). | `[NULL: tools/]`; `skills/valoria-simplify/SKILL.md:171–177` (the port note) | Held back (§8) |
| **F18** | **Precedent risk.** The repo's recursion was generated by doctrine that turned each observation into a permanent artifact: guards on guards, and baseline ratchets the repo later retired. | `proposals/2026-08-18-breaking-the-recursion.md:181–213`; `valoria-ci.yml:171–173, 253` | No tool, gate, test, scorer or baseline (§0, §7) |

### P7 — Jordan's definition: as little code as possible, extremely clear and organised, centralised and modular

| id | finding | evidence | action |
|---|---|---|---|
| **F19** | Read literally, "as few lines as possible" conflicts with "extremely clear". **[ASSUMPTION: clarity is the constraint and minimality the goal; basis: "in an extremely clear organized manner" qualifies the minimising]** | — | Priority in §2: clarity outranks minimality |
| **F20** | **CORRECTION:** the line-count ratchet proposed this session, and the standing size score and the complexity-threshold rule of the first draft of this proposal, are **withdrawn**. The ratchet would block a split that improves clarity. A score is the "composite score" `valoria-simplify` rule 5 forbids, and a complexity score may only *rank* (instrument I7). | `valoria-simplify/SKILL.md:165, 204` | Size enters only per change, as the reduction test (§5); complexity only orders the clarity read (§5) |

### P8 — "The same behaviour and outcomes with less code? Without hard-coding values?"

| id | finding | evidence | action |
|---|---|---|---|
| **F21** | **This is the right definition of minimal**: a behaviour-preserving reduction (Opdyke, 1992; Fowler, 1999). Whether a shorter equivalent exists is undecidable (§0); whether a *given* reduction preserves behaviour can be checked. | — | Hard constraint H1 (§5) |
| **F22** | **"The exact same behaviour" needs an observable definition.** One hash on one seed can miss a change; a deletion or algorithm rewrite needs a differential run of old against new code. Dead means no reference, and a run alone never proves a branch dead. | `valoria-simplify/SKILL.md:129` (C4), `:131` (C5) | H1 is `layer-conformance`'s THE CONTROL plus C4 (§5) |
| **F23** | **Hard-coding is already guarded, and the rule is already in Layer 1.** PART D row 38: "a constant invented at the keyboard … MECHANICAL + a numeric-literal scan". `tools/ci_sim_fabrication_check.py` is blocking, accepts honest provenance tags including `[DECLARED-DIVERGENCE]` (Jordan, 2026-07-24), scans numbers only and the changeset only, and has a recorded gap at `modules/combat/` (a PC-lane decision). A scope-wide "no hard-coded value" gate is the tree-wide guard CLAUDE.md §0.05 refuses. | `04:1067`; `tools/ci_sim_fabrication_check.py:64–76, 164–170, 515–520`; `valoria-ci.yml:183`; CLAUDE.md §0.05 | H2 reuses the gate on each change and adds a diff read (§5); `modules/combat/` held back (§8) |
| **F24** | **A reduction that moves a knot elsewhere is not a reduction.** | `valoria-simplify/SKILL.md:147` | Adopted as the reduction test (§5) |

### P9 — Sequencing and structure defects in the first design (found by the user's question and the critic)

| id | defect | resolution |
|---|---|---|
| **F25** | **Judgment (L4) repairs could never be accepted.** The first draft required every accepted repair to *lower* a violation count; L4 has no count. | L4 findings are countable: each is one named failed lookup. An L4 repair is accepted when that lookup becomes answerable and no count rises (§5) |
| **F26** | **A run that makes no repairs leaves no record**, so the next run repeats the same scope. | Accepted and bounded: such a run changes nothing, so repeating it costs reading, never churn. Stated as a limit (§4 E2, §9) |
| **F27** | **Scoping by changed files is unsound for relational rules** (a deleted caller makes a callee in an untouched file dead; a new function can duplicate an untouched one). | A finding is in scope if it is located in a changed file, has an endpoint in one, or concerns a name on a line the same diff removed (§4 E2) |
| **F28** | **Falsifiers ran first, on every run, for probes that may find something.** A clean result needs a named failed attack; a probe that finds something has shown it can see. | The skill has no probes of its own. Each owner shows its own control before it edits (C2, B3), after FIND (§3) |
| **F29** | **The control cadence conflicted with CLAUDE.md §0.4** (full controls on every repair). | H1 *is* `layer-conformance`'s THE CONTROL: cheap instruments after every unit, suites once at the close (§5) |
| **F30** | **The trailer was keyed on the commit that carries it, which a squash merge replaces; and the first draft's "tree at commit time" recorded the parent's tree.** | Key on tree hashes from the index (`git write-tree`), compared by `git diff` between trees, found by trailer search in available history; a missing tree object means the whole subject once (§4 E2). Tested (§9) |
| **F31** | **"Collect every finding first" conflicted with the owners' order.** `valoria-simplify` runs between Lens A and Lens B so that B grades what remains. | Findings are frozen **per stage**, not once for the run. The stage order is the owners' (§3) |
| **F32** | **The clarity read came before the repairs, so its findings could concern code the structure stages then delete; read after, it would read the run's own fixes.** | L4 runs last, on scoped files this run did not edit (§3, §5) |
| **F33** | **"No repair is reviewed again" read as forbidding the re-measure that acceptance needs.** | Re-running an owner's instruments on the repaired code is measurement; the L4 and judgment findings are not re-read (§4 E3) |

### P10 — Conflicts and duplicates (found by the user's question and the sibling skills)

| id | finding | evidence | resolution |
|---|---|---|---|
| **F34** | **Modular rules duplicated `layer-conformance` Lens B**, and a new scan would be "two checks that can disagree". Lens A3 forbids a standing §A.2 checker; B3 says to find the existing scan first. | `layer-conformance/SKILL.md:98–100, 182–201`; `engine/season/tests/test_season_shape.py` | Modular is Lens B's, run over the scope (§2). No probe or scan is added |
| **F35** | **Minimal and centralised rules duplicated `valoria-simplify`** (EARN, C4, C5, the ladder, I3). | `valoria-simplify/SKILL.md:98–149, 161` | Owned there; read at the row (§2) |
| **F36** | **The first draft's tool, thresholds and blocking checks conflicted with `valoria-simplify` rules 2–5** ("no guard that the unit stays simple", "no new tool or scorer", "no threshold invented, and no composite score"). | `valoria-simplify/SKILL.md:201–204` | None are added (§0) |
| **F37** | **The `04` amendment was a second owner of rules already in `04`, `layer-conformance` and `valoria-simplify`.** | — | No Layer-1 file. Jordan's definition is recorded in the skill, the way the current skill records "ALL DIRECTIONS" (`SKILL.md:39–44`) |
| **F38** | **`CLAUDE.md` §9 routes "distilling code and data without losing function" to `valoria-simplify`**, and "attacking a whole subject" to `efficient-coding-review`. | `CLAUDE.md:527, 537` | Both rows are retargeted one-for-one (§6) |
| **F39** | **`CLAUDE.md` is exactly at its 640-line cap.** | `wc -l CLAUDE.md` = 640; CLAUDE.md header | The edits replace text within lines and add none; checked at execution (§7) |
| **F40** | **Four references to the skill's name, three of them to the method that is being renamed.** | `CLAUDE.md:54` (STEP 5), `:537`; `skills/methodology-close/SKILL.md:229` (STEPS 4 and 5); `skills/premise-check/SKILL.md:71`; the symlink `.claude/skills/efficient-coding-review` | Retargeted in the same change (§6). The historical mention in `proposals/2026-10-29-parliament-and-debate/…:711` stays |
| **F41** | **Routine per-commit conformance is already `/close` step 4**, and `methodology-close` runs `/code-review`, `/simplify` and `layer-conformance` on a diff. An incremental mode would repeat that. | `layer-conformance/SKILL.md:23`; `CLAUDE.md` §9 | The skill is for the subject-wide questions a diff cannot ask (§2, "when to run it") |
| **F42** | **The "plug-in test" (M3) was a duplicate and its premise false.** | F15 | Dropped |

---

## 2. Jordan's definition, and who owns each part

*"Efficiency, for me, is as little code as possible in an extremely clear organized manner that is centralized and modularity."* Sharpened (Jordan, in session, 2026-11-07): *"can we produce the exact same behavior and outcomes with less code than currently exists? … and can we do so without hard-coding values?"* [ASSUMPTION: clarity outranks minimality; F19.]

The skill records this definition, as the current skill records ALL DIRECTIONS. It owns **no rule below**; each is read at its owner, at the row, every time.

| property | the question | owner of the test | counts as a violation |
|---|---|---|---|
| **MODULAR** (hierarchical, isolated, pluggable) | does each scoped module conform to its Layer-1 row, and do levels respect their order? | `layer-conformance` Lens B (`04` §A.2 both halves, §C.12, `holonic_ARCHITECTURE.md` §43, §45–§47; the grade is B2's); `valoria-simplify` I4 for dependencies | a Lens-B nonconformance (B4's first disposition); an I4 FAILS |
| **CENTRALISED** | does each fact have one owner and one writer? | `valoria-simplify` I3 (`export_sim_params.py --search`, the exporters' `--check`); `layer-conformance` A2 (a mechanism living in prose) | an I3 FAILS; an A2 finding |
| **MINIMAL** | can the same behaviour be had with less code? | `valoria-simplify`: EARN, C1–C5, the ladder, relocation, lookalike-versus-copy | an *unearned* artifact, or a C5-dead one, that the ladder can remove |
| **NO HARD-CODING** | is any value typed where it belongs in its owner? | PART D row 38; `tools/ci_sim_fabrication_check.py` on the change's added lines | a repair that adds one (a hard constraint, §5) |
| **CLEAR** | can a newcomer find what a module does and where its inputs come from? | **this skill** (§5, L4) | one named failed lookup |

**Verdict vocabulary** is the owners': HOLDS, FAILS, INCONCLUSIVE. INCONCLUSIVE is reported with its reason and is never counted as clear (`valoria-simplify` `:81, 155`).

**When to run it.** Routine per-commit conformance is `/close` step 4 and `methodology-close`. This skill is for the subject-wide questions a diff cannot ask: second owners across modules, subject-wide minimality, pluggability, clarity of code nobody has changed. The request is the scope (CLAUDE.md §0).

**Subject.** `engine/season/` and `modules/`, the game code (Layer 2; CLAUDE.md §3). Not `tools/`, `tests/` or `systems/`: pointing a standard at the repository's own apparatus is the recursion F18 records.

---

## 3. The sequence

Each stage is a *find, then repair* pair. **Findings are frozen at the start of their own stage**, so a stage never re-reads its own repairs, and later stages read the tree as earlier stages left it, which is the order the owners already rule (`valoria-simplify/SKILL.md:55`; `layer-conformance/SKILL.md:56–58`).

| step | does | why here |
|---|---|---|
| **0 · FRAME** | name the subject; compute the standard fingerprint; find the last trailer; compute the scope; if empty, **NOTHING TO DO**, stop (§4 E2) | stops before any reading |
| **1 · PLACE** | `layer-conformance` Lens A over the scope; repair | Lens A gates B (`layer-conformance` `:56–58`): polishing a misplaced artifact polishes the wrong thing |
| **2 · DISTIL** | `valoria-simplify` over the units the scope falls in (areas as its M1 defines them): SURVEY to triage, then EARN and the nine instruments; each owner shows its control before it edits (C2, with the plants in a worktree, never the working tree); repair by its ladder | between A and B, by the owners' ruling |
| **3 · CONFORM** | `layer-conformance` Lens B on the scoped modules; repair | B grades what remains |
| **4 · CLEAR** | the L4 read, on scoped files this run did not edit (§5); repair | last, so it never judges code a structural stage is about to delete or rewrite, and never reads this run's own edits |
| **5 · CLOSE** | the suites once (`layer-conformance` THE CONTROL; CLAUDE.md §0.4); a red re-runs the failing file only; a repair the red traces to is reverted and becomes a residual | cadence |
| **6 · RECORD** | the reply (violation counts per property before and after, residuals with reasons, controls shown, candidate rules routed), and the trailer line for the commit | the end point |

**The owners' own stages apply inside steps 1–3**: PRE-FLIGHT, WORK, ATTACK by `valoria-critic` (read-only), RECONCILE (`layer-conformance` THE PASS; `valoria-simplify` THE PASS). One producer per package; tiers set per CLAUDE.md §10; no lane count mandated here.

**Prohibitions are the owners' and bind here unchanged**: `layer-conformance` WHAT THIS PASS MAY NOT PRODUCE (`:303–322`) and `valoria-simplify`'s (`:196–206`): no document, no guard, no tool or scorer, no composite score, no invented threshold.

---

## 4. The end point — what makes a run finish

**E1 · The standard is fixed for a run and fingerprinted.** The standard is this skill's text and the owners' text it reads at the row. The trailer records `std=` as the blob hash of this skill's `SKILL.md` alone. A change to a sibling skill does not reopen the subject; ask for a whole-subject run if wanted (F26 states the same limit for runs without repairs).

**E2 · Scope comes from recorded tree hashes, never from a remembered verdict.**

- A run that commits repairs puts one line in the body of its last commit:
  `Efficiency-Reviewed: engine/season=<tree> modules=<tree> std=<blob> attempted=<n> residual=<n>`
  where each `<tree>` is read from the **index** just before committing: `T=$(git write-tree); git rev-parse $T:engine/season $T:modules` (the plain `git rev-parse :engine/season` fails: a directory is not an index entry), and `std=` is `git rev-parse :skills/efficient-coding-review/SKILL.md`.
- The next run finds the newest such line in the available history: `git log -n1 --grep='^Efficiency-Reviewed:' --format=%B`. A squash-merge keeps each commit message's lines at line start (observed in #580), so the line survives it; because the line records tree hashes, not a commit, it also survives a rebase. **It does not deepen a shallow clone** (`valoria-simplify` M5; CLAUDE.md §2): a line not found means the whole subject, once.
- **NOTHING TO DO** when, for every subject path, `git rev-parse HEAD:<path>` equals the recorded tree and `std` matches. The run stops before reading any code.
- **Otherwise the scope** is `git diff --name-only <recorded-tree> HEAD:<path>` per path, prefixed with the path. If `git cat-file -e <recorded-tree>` fails (a tree the clone no longer has), that path's scope is the whole path, once. If `std` differs, the whole subject, once.
- **A finding is in scope** if it is located in a scoped file, **or** has an endpoint in one (an import edge, a duplicate pair, a second owner), **or** concerns a name that appears on a line the same diff removed (the dead-code case: deleting a last caller makes its callee dead wherever the callee lives).
- **A violation outside scope is not this run's work**, and nothing records it as owed. The skill therefore never becomes a standing queue (CLAUDE.md §0: "does this document create work for a future session?").
- **What this cannot see** (stated, not hidden): a violation that arises because something *outside* the subject changed, such as a registry row naming a function being deleted (`valoria-simplify` C5 searches the whole repository for references, but only for scoped candidates), or an owner's instrument being revised. Neither reopens the subject. Ask for a whole-subject run.

**E3 · Findings are frozen per stage; re-measuring is not re-reviewing.** After each repair the owner's *cheap* instruments are re-run on what the repair touched (`layer-conformance` THE CONTROL). That is measurement. The judgment findings (an earned/unearned verdict, an L4 finding) are not re-read. A repair is never audited in the run that made it (CLAUDE.md §0), and the next run starts after it (E2).

**E4 · Each finding gets one attempt; a repair is accepted only if no property gets worse and one gets better.**

- The measure is **a count per property** (§2), componentwise, **never summed or weighted and never reported as a grade of the code**. That keeps it outside `valoria-simplify` rule 5's "composite score"; the distinction is named here so a reader can judge it.
- Accepted: no property's count rises **and** at least one falls (for an L4 repair, the named lookup becomes answerable, §5). The conditions of §5 also hold.
- A repair that fixes one property and raises another is **not accepted** and the finding becomes a residual with its reason. A repair that trades a lower-ranked count for a higher-ranked one is no longer permitted (the first draft allowed it, which let repairs create violations in files the next run never examines).
- **Termination.** Within a run: each frozen finding gets at most one attempt, and L4 reads a finite set of files, so the run is finite. Every accepted repair strictly lowers a total drawn from the natural numbers and never raises any component, so accepted repairs cannot cycle (Floyd, 1967). Across runs: see E2 and §9.

**E5 · No rule growth from inside.** An observation that violates no rule is a **candidate rule**, not a finding. It goes through CLAUDE.md §0's five answer-it-first tests. A survivor becomes at most one `needs_jordan: true` row, and a candidate that already has a row is never raised again. The skill never adopts a rule.

**E6 · One round** (CLAUDE.md §0), unchanged. The named subject plus its one pass is the stop condition.

**Why this cannot run indefinitely.**

- Within one run, work is bounded by E4.
- A run that commits repairs records the post-repair trees, so the next run's scope is empty unless code changed (E2). Changes originate outside the skill.
- A run that commits nothing changes nothing, so a repeat costs reading and cannot make the tree worse or cycle. It can differ only in L4, where a repeat may find a lookup the first run did not; that finding is then repaired, a trailer is written, and the files leave scope. The sequence of runs over an unchanged subject is therefore: any number of no-op runs, then at most one repairing run, then NOTHING TO DO.

---

## 5. Acceptance rules

**H1 · Same behaviour and outcomes** (hard constraint, never traded against a count). `layer-conformance` THE CONTROL (`:258–299`) is the definition, read there: the cheap instruments after every unit; the suites once, at the close, only those the change can reach (CLAUDE.md §0.4). A repair that moves the content hash or a probe verdict has broken something and is reverted (`:283`). For a deletion or an algorithm rewrite, add `valoria-simplify` C4's differential run of old against new code. Every exporter's `--check` passes for a repair that touches an exported chain.

**H2 · No hard-coding** (hard constraint). (a) `tools/ci_sim_fabrication_check.py` passes on the repair's added lines (the invocation is `layer-conformance` `:275`). (b) The repair does not turn a value its code read from its owner (`engine/engine_params/` or the single Python owner) into a literal. Part (b) is read from the diff, because the gate accepts a tagged literal (`[JUSTIFIED: …]`, `[DECLARED-DIVERGENCE: …]`) by design (`ci_sim_fabrication_check.py:64–76`).

**The reduction test.** A change offered as a reduction is accepted only if H1 and H2 hold, **and** it deletes more lines than it adds (`git diff --numstat`), **and** the number of places a reader must open to predict the behaviour does not rise (`valoria-simplify/SKILL.md:147`: relocation is not reduction). A repair that is *not* offered as a reduction (a placement or conformance fix) is not held to the line count.

**L4 · The clarity read** (CONVENTION; the one rule this skill owns). Open a scoped file cold and try to answer: *what does this module do, and where do its inputs come from?* The current skill's SURVEY row asks the same of a work (`SKILL.md:197, 213`: a stranger, ten minutes, "judged by doing it"), and this reads it per module.

- Scope: scoped files this run did not edit (a file the run edited was already held to the reduction test or to Lens B).
- Order: by cyclomatic complexity, descending (McCabe, 1976), computed with a throwaway `ast` probe, **to rank where to look and nothing more** (`valoria-simplify` I7: "to rank only; gives no FAILS"). There is no cutoff.
- **Admission:** a finding must quote the lookup, say where the reader looked (file and line) and why it failed. A "this feels unclear" without a failed lookup is dropped (F7).
- **Repair:** accepted when that same lookup is answerable in the repaired file, no other property's count rises, and H1 and H2 hold. The lookup is re-asked once, as the acceptance check; the repaired file is not re-read for new findings (E3).

---

## 6. What happens to the current skill

The current method is a sound **claim review** (is what a work says about itself true, does it transfer, does it follow), and `methodology-close` and `premise-check` depend on it. It is kept, under a name that says what it does: `claim-review`. Its description keeps the claims a code base makes about itself (docstrings, contracts, registries, tests; `SKILL.md:64–67`); it drops any claim to judge efficiency. It gains the same tree-keyed end point for a reviewed work, with the trailer `Claim-Reviewed: <path>=<tree-or-blob> …`: a work unchanged since its trailer returns NOTHING TO DO.

`efficient-coding-review` becomes the skill of §2–§5.

**Changes at execution, in one commit:**

| where | change |
|---|---|
| `skills/claim-review/SKILL.md` | the current `skills/efficient-coding-review/SKILL.md` moved here (`git mv`), renamed, with the end point above and the Status line kept |
| `skills/efficient-coding-review/SKILL.md` | rewritten per §2–§5 |
| `.claude/skills/claim-review` | new symlink to `../../skills/claim-review`; `.claude/skills/efficient-coding-review` stays and now resolves to the new skill |
| `CLAUDE.md:54` | `skills/efficient-coding-review` STEP 5 becomes `skills/claim-review` STEP 5 |
| `CLAUDE.md:537` | the claim-review route points at `claim-review`; the code-base wording moves to the efficiency route |
| `CLAUDE.md:527` | the "distilling" row adds the whole-subject efficiency pass in the same line |
| `skills/methodology-close/SKILL.md:229` | `efficient-coding-review` STEPS 4 and 5 become `claim-review` STEPS 4 and 5 |
| `skills/premise-check/SKILL.md:71` | "(a whole subject's claims)" retargeted to `claim-review` |

---

## 7. Execution — one change, not a plan

Ratification is the merge of this proposal (ED-1094); the CLAUDE.md rows are Layer 0 and are ratified by the same merge. Execution is **one** change, so it adds no position to any plan (CLAUDE.md §2; `CURRENT.md:19`): the table in §6, plus deleting this proposal with an exact-file `FORK:` row in `references/restructure_ledger.md`.

**Checks at execution:**

- `wc -l CLAUDE.md` is still 640 (F39). If an edit would add a line, rewrite within the line instead; do not raise the cap without saying what was added.
- No file under `tools/`, `tests/`, `.github/` or `engine/` appears in the diff (§0).
- `python3 tools/valoria_local.py --staged` passes; the tests that read the touched skill files run (`grep -rl <path> tests/`, CLAUDE.md §0.4 pt 1).

---

## 8. Not decided by this merge (held back, per CLAUDE.md §2)

- **A type checker in CI (F13):** `pyright` in strict mode on the subject would make `04`'s "STRUCTURAL under a checker" grades true. It is a new CI dependency.
- **A GDScript-subset check (F17):** a portability rule, outside Jordan's definition, owed a check of the ruled series' docs first.
- **A performance budget (F12):** outside the definition. It would need a stated growth order and a time budget per season.
- **`modules/combat/` in the fabrication gate's scope (F23):** a PC-lane decision already filed under ED-IN-0119 (`ci_sim_fabrication_check.py:164–170`).
- **Whether a planted `verb_call` module is dispatched by a season (F15):** a possible gap that Lens B reports when it runs. Closing it would be a new test, a separate decision.

---

## 9. Falsifiers for this proposal

Run each at execution; record the result in the commit paragraph. A red here means the design is paper (CLAUDE.md §0.2).

1. **Idempotence.** Run the rewritten skill on a subject where it commits repairs; run it again on the unchanged result. The second run must stop at STEP 0 with NOTHING TO DO and open no source file.
2. **Squash survival.** After the first PR carrying a trailer is squash-merged with no other change to the subject, the next run must return NOTHING TO DO. If another change landed in the subject, its scope must be exactly `git diff --name-only` between the recorded tree and `HEAD`. (Checkable only after that merge.)
3. **Missing tree.** Replace a recorded tree hash with one that does not exist. The run must take the whole path, once, and write a new trailer.
4. **Relational scope.** Delete the last caller of a function in a scoped file, where the function itself lives in an unscoped file. The function must appear as a C5-dead finding in the next run.
5. **Repair rule.** Offer a repair that removes a duplicate but adds a new import edge across modules. It must be rejected and recorded as a residual.
6. **L4.** Plant an unclear module with a lookup that fails; the finding must be admissible, and the repair accepted once the lookup is answerable. A finding without a failed lookup must be dropped.
7. **Same behaviour.** In a worktree, plant a false reduction that deletes one executing branch whose effect reaches world state. H1 must go red. If it stays green, H1 cannot see the change.
8. **No hard-coding.** In a worktree, replace a value read from `engine/engine_params/` with a literal carrying a `[JUSTIFIED: …]` tag. The fabrication gate passes; H2(b), read from the diff, must still refuse it.
9. **No growth.** The execution diff touches only the files in §6's table and the `FORK:` row. If it adds a tool, test, gate or baseline, F18's failure has recurred.
