---
name: valoria-simplify
description: >
  VALORIA SIMPLIFY — distil this repository's code and data without losing function. Two modes.
  SURVEY: a high-level map of a system or area, read in six directions (top-down, bottom-up, vertical,
  lateral, horizontal, diagonal), ending in a ranked list of where to look; no edits. DISTIL: for a named
  unit, find what is unearned (a second owner of a fact; apparatus where editing the existing owner
  would serve; scripting drift; indirection with no second user; speculative generality; dead or
  retired code; a knot moved, not loosened) and remove it, only after a control has been SHOWN to see
  the unit. Nine instruments drawn from a survey of the literature on architecture, data management,
  complexity and mutation analysis. Runs between `layer-conformance` Lens A and Lens B. Use for:
  "simplify / distil this module, engine or system", "survey the repo for complexity", "what can we cut
  without losing function", "too much scripting", "new module or an edit to the existing one", "dead
  code in <package>", "is this earned", "what would this cost to port". Not for: a diff's line-level
  cleanup or a single function (`/simplify`), bugs (`/code-review`), layer placement or Layer-1
  conformance (`layer-conformance`), whether a MECHANIC should exist (`ners`), inert design mechanics
  (`valoria-mechanic-audit`).
---

# VALORIA SIMPLIFY

## Status: RATIFIED on merge of its landing PR (CLAUDE.md §2, ED-1094). Supersedes `engine-simplify`, which was never merged and is deleted in the same change. Requested by Jordan in session, 2026-10-28. Invocable through the symlink `.claude/skills/valoria-simplify`.

## What it owns, and what it copies

**It owns the two obligations (EARN, OBSERVE), the survey's map and directions, and the nine instruments.** The rest is read at its owner:

| the content | its single owner |
|---|---|
| what each layer binds; mechanism versus reference | `CLAUDE.md`'s layer table, §0.05 |
| when a guard is licensed | `CLAUDE.md` §0.1 pt 5 |
| what the code architecture requires, and so what is already earned | `architecture/meta/04_CODE_ARCHITECTURE.md` |
| the pass's stages, the control's command set, what a pass may not produce | `layer-conformance`: THE PASS, THE CONTROL, WHAT THIS PASS MAY NOT PRODUCE — they apply here unchanged |
| tiering, fan-out sizing, what makes a critic independent; one round only | `CLAUDE.md` §10; §0 |
| which Godot series is ruled | `ED-GO-0002`'s last row |
| the project's port stance | `CLAUDE.md` §6; `04` §C.8–§C.10, §C.12 |
| what GDScript can and cannot do | Godot's reference for the ruled series, read each pass |

- **Never copy a spec row, a table, a count or a GDScript fact into this file.** A copy rots silently and the next session reads the copy.
- **Bound.** Mints no guard, adds no CI check, produces no document, builds no tool, and nothing enforces it.

---

## The claim, and the two obligations

To distil is to remove or merge only what is **unearned**, while **nothing observable is lost**. Two obligations, in this order; a change that meets one and not the other is not made.

1. **EARN.** The artifact has a live reason to exist as a separate artifact, shown (below). The unit of EARN is anything larger than a function: a module, class, registry or loader, tool, flag, parameter, seam, branch over a closed set, data file. A single function that names a concept is `/simplify`'s.
2. **OBSERVE.** A control that has been *shown* to see the artifact says nothing changed. A control that merely stays green proves nothing: a seeded run reaches only part of the code and misses some one-token changes even on lines it executes. Measure; do not assume.

**Used is not earned.** *Used* means it has a live non-test caller or reader. *Earned* means that merging it into its neighbour or inlining it would lose something (E1–E4). An artifact with no use is a deletion candidate; a used artifact that is not earned is a collapse or extension candidate.

**Mechanic or apparatus.** If removing the artifact changes what the game does, it is a MECHANIC and `ners` owns the cut. If it changes only how the code arranges what the game does, it is APPARATUS and this skill owns it. A moved content hash, on a control shown (C2) to see the artifact, is the boundary crossing.

**Order with `layer-conformance`:** Lens A → this skill → Lens B. After A, because polishing a misplaced artifact polishes the wrong thing; before B, because B must grade what remains. A3 keeps guards. Where `04` requires a shape (a seam, the write gate, a typed result) it is earned by E1 and is not a finding; "simpler than `04`" is amputation. If a clear `04` rule costs a great deal, keep it under E1, give the cost as one clause in the commit paragraph, and never edit `04` to fit.

## Modes

- **SURVEY** (no edits): build the map, read it in the six directions, rank where to look. The output is the reply, not a file.
- **DISTIL**: a unit named by the request (a package, a module, a registry family). **If none is named, ask one question — which unit — before doing anything else.**

---

## SURVEY — the map, then six directions

### The map: throwaway probes built with `ast`, `rg`, `git` and the repo's own registries; nothing is committed

Count with `ast`, resolve each hit to its enclosing `def`, and state in the sentence that reports a number what was searched and what was not (`layer-conformance` B5, B6).

| | layer | how | what it cannot see |
|---|---|---|---|
| M1 | **areas and import edges** | Python under `engine/`, `modules/`, `systems/*/sim` (not tests, workbenches, tools). One edge per (importing file, repo module imported), including relative imports. Areas: `engine.season.<sub>`, `engine.<pkg>`, `modules.<name>`, `systems.<sub>`. Report files and edges per area, the share crossing an area, the top cross-area edges, area pairs that import each other | seams resolved by string; shared data; `sys.path` seams |
| M2 | **data channels** | each YAML/JSON the code reads (under `engine/season/`, `engine/engine_params/`, `references/`): the non-test files that name it. Flag files read from more than one top area, and files no code names | a path built from parts (name-matching over- and under-counts) |
| M3 | **seams by string** | `engine/engine_params/composition.json` roles and `references/module_contracts.yaml`. `engine/` names no subsystem by import (`CLAUDE.md` §3), so the engine-to-module edges are **these**, not M1's; add them to the map, labelled | edges nothing declares |
| M4 | **reach** | for each run you will rely on (`python -m engine.season.harness.` `headless`, `populated`, `soak`, `corpus_run`, `run_cases` with `report`; and named test files), the stdlib trace: `python3 -m trace --count --missing --module --coverdir=<scratch> --ignore-dir=<stdlib and site-packages> <module> <args>`. Lines it did not execute begin `>>>>>>`. Per area: files imported, statements executed. **An area no named run reaches is unobserved**; say so. (`harness.probes` has no entry point: tracing it measures only its import.) | what other runs would reach |
| M5 | **history depth** | `git rev-list --count HEAD`; `.git/shallow`. A shallow clone cannot run the history instrument (I5): its verdicts are INCONCLUSIVE and stated. Deepen with `git fetch --unshallow` only when the request names history (`CLAUDE.md` §2) | squashed history |
| M6 | **claims** | the statements the code is meant to realise: `engine/season/requirements.yaml` (`statement:` ruled verbatim; `status:`; `measure:` and `measured:`), the active plan's positions (`CURRENT.md`), `engine/season/hole_register.yaml` (inert-by-decision features are listed there; read it before calling anything dead) | goals nobody wrote down |

### The six directions

A direction ends in one word. **SURVEYED**: an instrument ran over the whole area and its blind spot was tested for this area (for example, M2's name-matching sampled by hand). **PARTLY**: an instrument ran, with a blind spot not tested. **NOT SURVEYED**: no instrument could run; say why. Never "clear" for a direction whose instrument could not see.

| direction | the question | instruments | Valoria's evidence | its blind spot |
|---|---|---|---|---|
| **top-down** | is each stated goal realised, and does each artifact trace up to one? | I9, I2 | M6 | unwritten goals: INCONCLUSIVE, not FAILS |
| **bottom-up** | what justifies each artifact and each fact? | I2, I3, I1 | M1, M2, M4 | reach (M4) |
| **vertical** | do levels respect their order and hide their detail? | I4 | M1 by area; conformance to `04` Part D is `layer-conformance`'s | an import map sees only declared edges |
| **lateral** | do peers share anything no contract names? | I4, I3 | M1 between sibling areas; **M2** (a registry read from many areas is the widest lateral channel) | M2 is name-matching |
| **horizontal** | along the run and the history: order, replay, carried cost | I1, I5, I6 | seeded runs; M5 | one seed; shallow history |
| **diagonal** | coupling across levels and peers that no structure declares | I5 (co-change), I4 (transitive core), I3 | M3, M2, plus history | without history, only I4 and I3 run: PARTLY at best |

### Triage: where to look

Rank units by **named criteria, shown separately**; **no composite score**: (a) cross-area hubs (M1 fan-in or fan-out); (b) data channels read from many areas (M2); (c) the unobserved share (M4); (d) change hotspots, where history exists (M5); (e) units an open plan position touches (leave them: E3); (f) `hole_register.yaml` rows. A unit on two or more lists goes first. The reply names the units, the lists each is on, and **what the survey did not cover**.

---

## EARN — the earning test

An artifact with no provenance goes to the ladder's first rung. One with provenance is **earned** only if one of these holds, **cited** (a finding that says "earned" without the citation has not run the test):

| | earned because | the citation |
|---|---|---|
| **E1 REQUIRED** | a ratified rule demands this shape | the `04` row, `ED-` id or `CLAUDE.md` § — verbatim, with its §/line. Earned by ruling, not shown necessary |
| **E2 OBSERVED** | removing or collapsing it moves a measured output | a run, before and after, **on a control shown (C2) to see the artifact**. An unshown control cannot earn or clear anything |
| **E3 PLANNED** | an open position in the one active plan, or an open M1 juncture, needs it | the position id. Earned **on paper** until a run exercises it (`CLAUDE.md` §0.2); leave it, and say so |
| **E4 SOLE OWNER** | it is the one place a rule lives, and **two named sites would otherwise carry it** (`CLAUDE.md` §8) | the rule, and the two sites. "It implements a rule" is not enough |

**Unearned** is none of the four. **Provenance** is any of: a live non-test caller or reader (resolved to its enclosing `def`), a recorded requirement or goal, an incident, a history entry, an evaluation against the simpler form. A caller that is a test does not count. A fan-in of one is a candidate, never a verdict.

---

## OBSERVE — the control

**C1 Choose the control** for the artifact: the command set in `layer-conformance` THE CONTROL (hash, probe verdicts, the season tests) and the artifact's own tests. For a data row the control is the same run. For a tool or code no run reaches, it is the tool's own test or `--check`. If there is none, see C3.

**C2 Show it sees the artifact — reach, plant, observe, then edit.** The producer does this in a worktree or a scratch export, never the working tree.
1. *Reach first.* List the lines the edit touches or removes and their callers; intersect with statement coverage from the **same** control run (M4). A line the run does not execute is outside the control's sight: go to C3.
2. *Plant.* On each covered line, and on the narrowest interface the artifact's effects pass through, make a one-token change **whose effect on behaviour you can state** (flip a comparison, add one to a literal; for a data row, change its value or remove it). If effects can leave by another path, such as a global, a file or a registry, the run's hash is a boundary check only (`FEA.1`).
3. *Observe.* Run the control. Each plant must go red: the hash moves, a probe flips, the artifact's test fails, or the run stops (a crash is a catch).
4. *Survivors.* For each plant the control missed, find an input or seed on which original and changed code give different outputs (**live**: the control is blind there) or show the change cannot alter behaviour (**equivalent**: not a miss). Equivalence is undecidable in general, so a survivor shown neither way leaves the result INCONCLUSIVE; report the result as a range, not a score.

**Pass means every plant was caught or shown equivalent. A control that misses a live plant cannot certify the real edit.**
- *Cost:* the per-plant loop runs only the headless hash and the one test file that covers the artifact (the season suite did not finish in ten minutes, so per-plant runs of it are out); the full suites run once, at the close (`CLAUDE.md` §0.4). A control shrunk this way is itself a change of control: judge it by the plants, not the score. It may certify only if it catches every plant the full control catches, compared on one plant set; a plant the smaller control no longer executes counts as missed.
- *Hygiene:* set `PYTHONDONTWRITEBYTECODE=1` and remove `__pycache__` first; a same-size edit restored within a second leaves stale bytecode that gives wrong readings. `delta` and other commands that call `git` need a worktree; an export has no `.git`.

**C3 If the control misses**, take the first that serves, then **repeat C2 on the new control**: (a) **widen reach** with a run or case that reaches the artifact (M4); (b) **pin the behaviour first**, in the same change, with a test that executes it. A test of behaviour is a mechanism, not a guard (`CLAUDE.md` §0.05, §0.1 pt 5); it records what the code does, not that this is correct; and it is the one edit permitted before C2 passes; (c) otherwise report the artifact **UNOBSERVABLE** and do not edit it.

**C4 Edit, rerun, expect zero game yield:** hash, probe verdicts and the artifact's tests unchanged. A moved hash means it was a mechanic: revert, or hand it to `ners`. C2 shows the control sees a small change at the site; it does not show the control would see the difference the real edit makes. **For an edit that rewrites an algorithm or removes code that executes** (JUS14 lists algorithm modification or simplification, and code deletion, among the faults no mutant couples to), add a differential run of old against new code that compares more than the hash (intermediate state, or per-function outputs, on the same seeds), or a test written for that behaviour. A change to a draw-bearing mechanism that moves the hash cannot be settled here: there is no live campaign-level instrument (`CLAUDE.md` §7).

**C5 Dead means no reference.** No static non-test caller (resolved to its `def`), no string or registry reference to its name (`rg` over Python and data files), and no consumer the repository declares outside itself (the port, an exporter). A run adds evidence that a *branch* is not reached; it never proves a branch dead, so a branch is not deleted on a run alone. The sentence that reports "dead", "unused" or "never fires" names what was searched and the runs (case, seasons, seed, test files). A retired file: ask `load_alias_map()` for the **exact** `FORK:` row (`CLAUDE.md` §8).

**C6 Report the control's limits in the sentence that reports its result.**

---

## DISPOSE — the ladder

Take the first rung that serves.

1. **Delete.** No provenance, and dead (C5). Deleting a tracked file writes its exact-file `FORK:` row in `references/restructure_ledger.md` (`CLAUDE.md` §1).
2. **Collapse.** Inline the indirection; merge the second owner into the first.
3. **Make it data.** A per-case branch becomes a row in a registry the loop already opens at runtime (`CLAUDE.md` §0.05), never a new loader, and only if it passes the relocation test below.
4. **Extend the neighbour.** A row, field, parameter or branch in the existing owner, over a new module, class, registry, tool or flag. Name the neighbour and write the edit. The new thing stays only if that edit would give the owner **a second reason to change**, and the finding says which.
5. **Keep**, with the earning cited in one clause in the commit paragraph.

**Relocation is not reduction.** Moving a knot into config, a helper, a base class, the caller or a comment leaves the reader holding the same concepts. Pass condition: *the number of places a reader must open to predict the behaviour falls.* If it does not, revert.

**One fact or a lookalike?** Before merging two copies, decide which they are (I3, against inline-and-diff in I1). Copies of one fact merge. Lookalikes with different meaning stay apart, and a shared unit that has grown caller-flags is undone, not extended.

---

## THE INSTRUMENTS

Nine, by what the reviewer does. State each verdict so that every case falls under HOLDS, FAILS or INCONCLUSIVE; where an instrument leaves a case uncovered, report INCONCLUSIVE and say why. **Where no source gives a threshold, any cutoff ("large", "repeatedly", "most") is the reviewer's own and is labelled so; invent none.**

| id | the instrument | how, in this repository | FAILS when | INCONCLUSIVE when | usual misfire |
|---|---|---|---|---|---|
| **I1** | **Perturb and run**: change, remove, isolate or replay one thing; run; diff | the headless season and its content hash; the artifact's tests; replay a recorded run; a differential run of old against new code; permute a collection or a configured order; remove performance-only machinery (state kept for ease of expression stays); inline a shared unit into its callers and diff; plant a change to test a control. **Expected result by use:** as detection and at C4, the output must *not* change; at C2 the plant *must* be seen; at E2 a moved output earns it | the output differs where it should not | the run does not reach the thing (M4) | **a run that never reaches the perturbed path** |
| **I2** | **Trace provenance**: does the artifact have a live reason? | the provenance list under EARN, for every seam, parameter, branch over a closed set, flag, name | none found | reachability is dynamic, or history is missing | the caller is a test; a framework or external interface imposes it |
| **I3** | **Trace ownership**: one fact, one writer, one check | `python tools/export_sim_params.py --search <name>` lists the module-scope constants of that name across modules (second owners); `--check` says whether the export is current (`--build` rewrites a tracked file); M2; the exporters' `--check` round-trips; every write path of a fact | two writers, an unchecked copy, or a hand-kept count of what is derivable | writers are dynamic | a hand edit as the second writer; a generated copy with a round-trip check is not a failure |
| **I4** | **Map dependencies and boundaries** | M1, M2, M3: off-boundary entries, hubs, level-skipping, a closure that spans top-level areas | an off-boundary entry (reviewer's cutoff for "large") with no named reason, or strong coupling through data no contract names | only edge presence is measurable | shared data and dynamic lookup hide edges (a false clear); a legitimate hub reads as a failure |
| **I5** | **Mine change history** | M5 first. Co-change between structurally independent areas; carried cost of an unused provision; deprecation follow-through | independent areas co-change (reviewer's count for "repeatedly"); a provision is edited around by unrelated changes | history is shallow or squashed | association is not cause; bulk commits; a shared upstream dependency |
| **I6** | **Check that failure, and a change, is visible** | read how refusals, statuses and costs are reported (`04` §C.11, §C.12); break or overload a component where a run can; for a survivor of C2, find where it stopped (unexecuted, executed without changing state, or changing state that never reaches the output) | a failure or a live plant goes unobserved or unexplained; a status reports intent as state | no fault can be injected | only anticipated failures are tried; **a swallowed failure is not a simplification** |
| **I7** | **Score and compare** | a propagation-cost or complexity score before and after a refactor, to **rank only**; gives no FAILS; no scorer is installed and none is to be built | — | always (unvalidated; the extractions differ) | relocating complexity lowers a score |
| **I8** | **Needs people** | not run by a pass; report "paper" | — | always | — |
| **I9** | **Trace goals to code** | M6: each goal in `requirements.yaml` has its `measure:` and a code site a run exhibits (read `measure:` and `measured:`; do not restate them); a new quality statement a pass writes names a stimulus and a measurable response, the environment optional. Never apply this form to a ruled `statement:` | a goal lacking a code site or a run | goals are not written down | an emergent goal has no single site |

---

## THE PORT NOTE — what the Godot port changes in the verdict

The Python under `engine/` is the **oracle**; a port serves it and never corrects it (`CLAUDE.md` §6, ED-1050). Each finding, and each artifact kept under EARN, carries one line: **neutral · lowers · raises port cost**, naming the Python construct and the GDScript construct it becomes.

1. **Read the GDScript side in the reference for the ruled series** (`ED-GO-0002`; path `https://docs.godotengine.org/en/<series>/`), **once per pass, per construct class**, and quote the page. Not memory; not `godot/godot_conversion_strategy_v1.md` (PROPOSED) or `godot/godot_architecture_specification.md` (STALE). Read also the page that lists behaviour changes since the previous series. A construct the page does not mention is *not documented*, which is not *absent*. **This skill names no version.**
2. **Classes to put the question to** (questions, not answers): error signalling (`raise`, `except`, `assert` as control); laziness (generators); expression density (comprehensions); container kinds (tuple, set, non-scalar keys); number domain (arbitrary-precision `int`, integer division, float width; `04` §C.8–§C.10); order (dict and set iteration, sort stability); identity and copy (`04` D-49); object model (private constructors, mixins, decorators, import-time effects); call shape (`*args`, defaults); recursion depth; randomness (threaded, not global: `04` §C.12 rejection 4); I/O.
3. **Four rules.** (a) **Do not simplify toward the Godot idiom**: `04` §C.12 lists five places where the idiomatic answer is the wrong answer here. (b) **Inside `port/`** the engine's own facility is the least machinery; hand-building what it provides is unearned there. `valoria-game` is not in this clone: read its code only where the session has it. (c) **Do not pre-shape for the port**: porting beyond the combat slice waits on the port gate (`CLAUDE.md` §6). (d) **Between two simplifications that serve equally, take the lower port cost**; converting `raise` sites to returned results is a wide port project whose shape is not ruled (`04` §C.12), not a simplification.

---

## THE PASS

Stages are `layer-conformance`'s (PRE-FLIGHT, WORK, ATTACK, RECONCILE), with this content:

| stage | content |
|---|---|
| **1 · PRE-FLIGHT** | SURVEY's map for the unit's neighbourhood; the census of the unit by `ast` (top-level defs, registries and loaders, entry points and flags, each with provenance and neighbour); the control chosen (C1); **the producer runs the C2 plants** and keeps their diffs and outputs. Batch the mechanical census on `valoria-measure` (Haiku); extract once, share it |
| **2 · WORK** | each census row through EARN; dispose by the ladder; edits in this commit; C4 after every unit |
| **3 · ATTACK** | `valoria-critic`, which has Read, Grep and Glob only and **cannot run or edit**, reads stage 2's **output**, diffs and plant results. It tries to: find provenance for every deletion by searching; show every "extend the neighbour" gave the owner a second concern; open every cited earning and show it does not land; find a plant the control would miss, and **name the plants it wants run** |
| **4 · RECONCILE** | the producer applies each finding or refutes it with a measurement, and runs the plants the critic named |

- **Tier it** (`CLAUDE.md` §10): the census is mechanical (`haiku`); earning and port-note verdicts are judgment (`opus`). Set `model:` explicitly. One producer per package; no lane count is mandated.
- **One round** (`CLAUDE.md` §0): the named unit plus its one pass is the stop condition. Its fixes are not themselves audited; a second wave starts only after you report what the first found.
- **A pass that finds nothing has not run.** *"I attacked X as unearned and it holds, because Z"* is a pass. Report the unit, the census size, and the attacks that failed.

## WHAT THIS PASS MAY NOT PRODUCE

`layer-conformance`'s prohibitions bind here. In addition:

1. **No candidate list, register or census document.** The SURVEY reply is the output. A finding that needs no ruling is fixed in this commit or dropped (`CLAUDE.md` §0).
2. **No guard that the unit stays simple.** Its subject would be the repository's process (§0.1 pt 5).
3. **No behaviour change called a simplification**, and **no simplifying edit without C2 shown.**
4. **No new tool or scorer.** Probes are throwaway, in scratch, uncommitted; a tool the repository already has is used or extended.
5. **No threshold invented, and no composite score.**
6. **No edit to `04` or `architecture/`** to make a simplification fit.
7. **No port-shaped scaffolding and no `raise`-to-result sweep.**

## THE FALSIFIERS — how a reader tells whether the pass ran

| the claim | what would show it false |
|---|---|
| *"unearned"* | none of E1–E4 is shown tested against it |
| *"earned"* | the citation is absent or does not land when opened; E4 without two named sites |
| *"nothing was lost"* | C2 was not shown: no planted change that the control caught, or survivors neither shown live nor equivalent were counted as caught |
| *"the control sees it"* | the plant was made in the working tree, or with stale bytecode, or on a line the run does not execute, or changed no behaviour and was counted as a catch |
| *"dead / unused / never fires"* | what was searched and the runs are not named, or a branch was called dead on a run alone |
| *"only one caller"* | the sentence does not say what was searched; hits were counted as text, not resolved to a `def` |
| *"the existing owner could take it"* | the edit is not written out |
| *"simpler"* | the content hash moved on a seen control, or the places a reader must open did not fall |
| *"surveyed"* | the direction's instrument could not see (history absent, goals unwritten) and it was not marked PARTLY or NOT SURVEYED |
| *"port cost lowers / raises"* | the Python construct, the GDScript construct, or the page read for the ruled series is not named |
| *"the critic found nothing"* | no named failed attack, only an absent finding |

**If this skill conflicts with `CLAUDE.md`, `architecture/` or `layer-conformance`, they win**; correct the skill.
