# CENSUS C1B — unreferenced symbols outside `engine/season/` proper (harness, modules, systems, dice, substrate, reference)

## Status: REFERENCE (a census lane's audit; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 7a4d5e1 (working tree; game code is unchanged through b8039982, `git diff --stat 7a4d5e1 HEAD -- engine modules systems tests tools references` is empty)

Lane: PART=C1B of `CENSUS_BRIEF.md`. Rows: every row of `census/C1_unreferenced_symbols.md` whose file
starts with `engine/season/harness/`, `modules/`, `systems/`, `engine/dice_engine/`, `engine/substrate/`,
`engine/engine_params/` or `engine/reference/`. No row of the census falls under `engine/engine_params/`.

## 0. Verdict

**Four rows in five are false leads: 518 of 643 are reached by a route a name search cannot see, and
only 26 rows are dead code this lane newly finds.** The census's largest single block, the 115 rows
of `harness/probes.py`, is one mechanism (a decorator registry) and every one of the 121 registered
probes executes. The dead rows are dominated by one decision the suite has already made (the SC-05
kernel, 75 rows). What the lane adds: two instruments that are tested and that no person can run
(`harness/arc.py`'s arc reader, `corpus_run.foreign_kinds`), ten rows of threadwork oracle that
nothing reaches and nothing carries, and eleven rows of `modules/mass_battle/` that are test-only or
empty.

| | rows |
|---|---|
| examined | **643** |
| false positive | **518** |
| dead: delete | **101** (75 the SC kernel, carried by `proposals/05_SC_sc05_kernel_disposition_B.md`; 5 already decided by `audits/04_MB_audit.md` F-MB-10 or the MB loadout proposal; **21 new**: batches D1 to D3) |
| broken: wire | **23** (18 threadwork, carried by `proposals/09_WR_threadwork_module.md`; 2 army presets, carried by `proposals/04_MB_playable_field_scenario.md`; **3 new**: wires W-1, W-2) |
| mislabelled: correct | **1** (C-1), plus five text corrections that ride on the deletions |

| family | rows | false positive | dead | broken | mislabelled |
|---|---|---|---|---|---|
| `engine/dice_engine/` | 5 | 5 | 0 | 0 | 0 |
| `engine/reference/` | 1 | 1 | 0 | 0 | 0 |
| `engine/season/harness/` | 325 | 320 | 0 | 5 | 0 |
| `engine/substrate/` | 1 | 1 | 0 | 0 | 0 |
| `modules/combat/` | 32 | 32 | 0 | 0 | 0 |
| `modules/mass_battle/` | 65 | 54 | 11 | 0 | 0 |
| `systems/characters/` | 4 | 3 | 1 | 0 | 0 |
| `systems/combat/` | 50 | 48 | 1 | 0 | 1 |
| `systems/fieldwork/` | 5 | 3 | 2 | 0 | 0 |
| `systems/mass_battle/` | 52 | 51 | 1 | 0 | 0 |
| `systems/social_contest/` | 75 | 0 | 75 | 0 | 0 |
| `systems/threadwork/` | 28 | 0 | 10 | 18 | 0 |
| **total** | **643** | **518** | **101** | **23** | **1** |

Proposals: `proposals/17_CENSUS_C1B_01_deletions.md` (batches D1 to D3, ordered by risk, with the
`FORK:` row text), `17_CENSUS_C1B_02_wires.md` (W-1, W-2, and the gap W-4 put to the WR proposal's
owner), `17_CENSUS_C1B_03_corrections.md` (C-1 to C-6). Every row is in Annex A.

## 1. Method (how each row was read)

The census is name-based: a symbol is listed when no other game file names it. Three things it cannot
see decide most rows, so each row was re-read with an AST pass over its own file, a repo-wide name
search and a module import graph (scripts kept in the session scratchpad, not in the tree):

1. **In-file reachability.** A symbol named only in its own file is live when a chain of in-file calls
   reaches it from a root. Roots: the `if __name__ == "__main__":` block, any other module-level
   statement (it runs at import), a decorator defined in the same file (a registry), and any symbol that
   another file names while also naming this module.
2. **Dynamic reach.** `globals()[name]`, a decorator registry, a string roster.
3. **Module reach.** For `modules/mass_battle/` and `modules/combat/`, name-based reachability inside the
   package from the composition entries (`references/module_contracts.yaml` `target:` rows:
   `resolve_field`, `armyrecord.apply/fielded/options`, `presets.plan`, `fight`). It over-approximates
   liveness, so a symbol it does not reach is not reached by name at all.
4. **What "live" means per family.** A harness instrument and a `systems/*/sim` or workbench script are
   run by hand, so reach from `__main__` is live (the lane prompt's instruction). Inside `modules/` a
   `__main__` block is a demo, not an entry, so reach from it alone is not live (two rows).
5. **What "needed" means.** The suite's own audits and proposals, cited per row; then the tree's ruled
   items. A symbol reached by tests and by nothing a person or the loop runs is decided on that, not on
   the test's existence.

Limits, stated once. (a) Reach from `__main__` shows a path exists, not that the path runs: every
file with rows was imported as a script (§5, run 3), but no `main` was run except where §4 says so.
(b) Cross-file edges are by name; a common name can supply a false edge. The 26 rows this lane calls
dead or newly broken were each read at the call site and grepped by whole word.

## 2. Why the false positives are false (518 rows, six mechanisms)

| mechanism | rows | evidence |
|---|---|---|
| **Decorator registry**: `@probe(pid, …)` writes `PROBES[pid] = dict(…, fn=fn)` (`harness/probes.py:61-68`); `run_cases.py:169-172` calls `spec["fn"]()`; `run_cases.main` runs every id (`:473`) | 111 probe functions, plus 4 helpers they call (`NOCHOOSE`, `_one_pass`, `_run_d`, `_seed_near_floor`) | run 1: 121 registered, 121 distinct functions, all executed: 64 PASS, 57 GAP, 0 INSTRUMENT-ERROR |
| **String roster through `globals()`**: `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`harness/invariants.py:242`), run by `violations` and `sweep` | 13 | `tools/m1_acceptance.py:366` and `:380` call `sweep`; `tests/valoria/test_season_invariant_sweep.py` breaks each by name |
| **Reached from `__main__`** of a hand-run instrument (harness) | 178 | AST chain per row, Annex A; `aperture` 34, `decision_spread` 23, `soak` 21, `strife` 16, `interactions` 13, `storybar` 12, others |
| **Runs at import** (a module-level table or call: `MOVES = load_moves()`, `validate_roster(ARC_SELF)`, `ABILITIES.update(_generics())`, `setattr(Combatant, _key, _attribute_property(_key))`) | 14 in the harness, others in modules | chain root `import` in Annex A |
| **Reached from `__main__`** of a hand-run oracle or workbench script under `systems/combat/` and `systems/mass_battle/` (`balance.py` is CLAUDE.md §9's named instrument) | 99 | all 22 files import as scripts (run 3); `main` not run `[UNVERIFIED that each main completes]` |
| **Called from another file through a caller the census did list as live** (`modules/`, `engine/dice_engine/`): the row is a private helper of a function the loop reaches | 91 in `modules/`, 5 in `engine/dice_engine/` | package reach from the composition entries, §1 pt 3; `roll_pool`, `band_odds`, `settle_margin` are named by `engine/season/seam/wrappers/sigma.py` and `modules/social_contest/roll.py` |

Six false positives that needed a judgment and are not one of the mechanisms above:

| row | reading | evidence |
|---|---|---|
| `systems/characters/sim/conviction.py` `ConvictionState`, `ConvictionThresholdState`, `check_conviction_threshold` | retained oracle, unreached by the loop | `knots.py` imports it late; `engine/tests/test_knots_ed912.py`; kept by ED-IN-0283 (RULED: the `systems/` folders are the home of those systems) and by `audits/02_CHAR_audit.md` §6 row 27 |
| `systems/fieldwork/sim/knots.py` `KnotState`, `_count_knots_for_actor`, `reset_knots` | retained oracle | `form_knot`/`sustain_knot` and the same test; `audits/08_FI_audit.md` R-14 keeps it unplugged with small edits (`proposals/08_FI_04_small-edits.md`) |
| `modules/mass_battle/geometry.py::body_overlap` | specification predicate | the control that `reach_reaches` (runtime, `core/contact.py:457`) is checked against in `tests/valoria/test_body_primitive.py`; removing it means rewriting nine tests to save six lines |
| `engine/substrate/stubwire.py::reset_invocations` | test-isolation helper | declared test-only at `stubwire.py:70-72`; `tools/m1_acceptance.py:150` records that it must not be called from a reporting surface, and does not call it |
| `engine/reference/degree-sweep/sweep_core.py::contested_verbs` | called from a proposal script | `proposals/2026-09-04-degree-sweep/arm1_admissibility.py:36`; the census did not search `proposals/` |
| `modules/mass_battle/troop_types/registry.py::support_ranks_for` | flag-gated runtime | `registry.py:156` under `MB_SUPPORT_RANK_CAP`; `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` separately proposes its removal |

## 3. The rows that are not false positives

### 3.1 Dead: delete (101)

| rows | reading | decision and what dies | evidence |
|---|---|---|---|
| `systems/social_contest/sim/contest/*` (75 rows in ten files) | the SC-05 kernel: reached by `engine/tests/test_contest_kernel.py` and by `agon_harness`'s `__main__`; never by the loop | delete with the kernel, in the order `proposals/05_SC_sc05_kernel_disposition_B.md` sets (after the `hearing` entry); this lane adds nothing to that proposal | ED-SC-0033 clause 2 (RULED); the import graph gives no `engine/season` or `modules/` importer for any of the ten files |
| `calibrate_generics.py::newcombe` | a confidence interval helper nothing calls | D1; nothing dies | `grep -rw newcombe`: the def only |
| `units.py::_reach_throttle` | a TOI closing-budget throttle nothing calls | D1; nothing dies | the def only; the directional reach body (`geometry.reach_reaches`) is what contact uses |
| `conviction.py::mark_belief_revision_pending` | names a caller, `beliefs.revise_belief`, that does not exist | D1, with the field `pending_belief_revisions` it alone writes; nothing dies | `grep -rn pending_belief_revisions`: the field, its (de)serialiser, this function |
| `knots.py::get_knot`, `get_active_knots` | store accessors nothing reads, not even the oracle's test | D1; nothing dies | the defs only |
| `altonian_reinforcements.py::invoke_altonian_reinforcements` | raises `NotImplementedError` | already decided: `audits/04_MB_audit.md` F-MB-10 | — |
| `orchestration.py::rally_check`, `threadwork_check` | called at every phase boundary; the body is `pass` | already decided: F-MB-10 (delete the no-ops and their calls) | `orchestration.py:271-273`, `:316-318` |
| `equipment/armour.py::dr_vs_piercing`, `equipment/weapons.py::with_keyword` | each called only by its file's `__main__` demo print | already decided: F-MB-10 (no reader); they go with `ARMOURY`/`ARSENAL` under `proposals/04_MB_unit_loadout_and_weapon_in_hand.md` | `armour.py:63`, `weapons.py:72` |
| `units.py::_effective_reach` | one test caller | D2; the facing-gated reach it computes is `geometry._reach_body_overlap`'s (reach extends along the heading only), so nothing dies but a second statement of it | `tests/valoria/test_reach_weapon_class.py:165-166` |
| `perimeter.py` `TargetPoint`, `_vertex_interior_angle`, `target_points`, `nearest_target`, `approach_alignment` | test-only; the file's own head says the wiring is "a separate, Jordan-gated step" (2026-07-23) | D2. Ladder step 5: the face an attack lands on is read once already, by `orchestration._compute_atom_sides` (one F/B/L/R face per contacting body, `:746`, `:1403`); a continuous alignment term beside it is two ladders for one quantity (§0.06 S). Step 2: no ruling, plan position or suite proposal carries the gate. What dies: corner target points and the sharp-tip flag, which nothing ever read. `perimeter_faces`, `_convex_hull`, `_centroid` stay (`units._envelop_goal` calls `perimeter_faces`) | `tests/valoria/test_perimeter_geometry.py`; `audits/04_MB_audit.md:356`, `:548` (0% reached) |
| `systems/threadwork/sim/threadcut.py` (6 rows), `co_movement.py` (4 rows) | no importer, no test, a module-level store each | D3: delete both files. `proposals/09_WR_threadwork_module.md` edit 2 deletes their stores when the directory moves; every function in them reads or writes that store, so nothing in either file survives the move as written. `proposals/2026-10-07-unplugged-systems-replug.md` §3.3 reads both as having "no carrier". What dies: an `[ASSUMPTION]`-graded draft of threadcut beings and of the co-movement deck; the design text stays in `.designs/`, the code at its fork ref | module graph: 0 importers each; `grep -rn threadcut\|co_movement` over `engine modules systems tools tests`: registry rows and one docstring only |

### 3.2 Broken: wire (23)

| rows | reading | decision | evidence |
|---|---|---|---|
| `harness/arc.py::ambition_thrusts`, `ArcReading` | the arc reader (`read_arcs`) and its only real predicate are reached by one test file and by nothing a person can run; the file has no `__main__` | **W-1**: a `__main__` in `arc.py`. Needed: `audits/09_WR_audit.md` R-10 already quotes the reader's count, and `proposals/12_ARCS_case_on_the_realm.md` and `09_WR_B_readings_of_closure_and_tension.md` both build on this file | run 4: realm seed 0, 2 seasons, arm `off`: 83 actors; default predicate 0; `ambition_thrusts` 21; shuffled-causes null 1; unrestricted 53 |
| `harness/corpus_run.py::foreign_kinds` | "what an act's Events say that its row does not declare"; test-only, while its sibling `unrowed_acts` is printed by `aperture` | **W-2**: one key and one line in `aperture`. Needed: it is the executed form of census C4's question | run 5: realm seed 0, 3 seasons: empty over 2,630 acts and 74,510 events; `test_aperture.py:230` plants one and sees it, so the zero is a reading |
| `harness/army_presets.py::_commander`, `plan_for` | reached through `install`, which tests alone call | carried: `proposals/04_MB_playable_field_scenario.md` (MB R-07: install presets at realm build behind one fixture) | `module_contracts.yaml:114`: "shipped off: nothing in the season loop calls it" |
| `systems/threadwork/sim/operations.py` (8), `coherence.py` (4) | the oracle's operations; tests only | carried: `proposals/09_WR_threadwork_module.md` (entry `threadwork.work`) and `09_WR_B_threadwork_session_and_practitioner.md` | import graph: `TESTS` only |
| `systems/threadwork/sim/collective.py` (3), `opposing.py` (3) | as above, and no verb | carried by the same move, **with a gap this lane names (W-4)**: neither WR proposal gives a collective or an opposed working an entry, a verb or a caller, so after the move they are still test-only, now inside `modules/` | `09_WR_threadwork_module.md:79-80` (signatures change; no row added); `…replug.md` §3.3 ("no verb") |

### 3.3 Mislabelled: correct (1, and the corrections that ride on deletions)

`systems/combat/combat_engine_v1/capabilities.py:23` (`_affords_point`): the docstring names `systems.py`;
the module is `combat_systems.py` (C-1). Five further corrections follow from §3.1 and are in the
corrections proposal: a comment that points at a deleted function, a package docstring, two
`mechanics_index.yaml` rows, a field, and a composition row's `needed_by` text.

## 4. Where the census script cannot see (the brief's last paragraph, within this lane's files)

| finding | evidence | resolution |
|---|---|---|
| **X-1. Tests that exercise code nothing calls.** Beyond §3: `harness/arc.py::read_arcs` (not a census row: a test names it), `army_presets.install`, the whole threadwork oracle, `conviction.py`, `knots.py`, the SC kernel | the import graph tags each `TESTS` only | each has its decision above; none is left without one |
| **X-2. A `__main__` demo inside a registered module** is the only caller of two functions | `equipment/armour.py:55-63`, `equipment/weapons.py:66-72` | deleted with their functions (already decided, §3.1) |
| **X-3. An empty body that runs.** `rally_check`, `threadwork_check` | AST: body is `pass`; 2 of the 3 no-ops F-MB-10 lists (the third, `Subunit.halt_before_enemy`, is a method and not a census row) | already decided |
| **X-4. Text that describes code which does not exist** | `conviction.py:269` (`beliefs.revise_belief`); `capabilities.py:24` (`systems.py`); `registers/mechanics_index.yaml:466`, `:484` (`canon_sources: systems/threadwork/threadwork_v30.md`, a path under a tree that holds no `.md`; `test_status: not_implemented` beside a `sim_module` that exists) | C-1 to C-4 |
| **X-5. `[canonical: params/*.md]` and `designs/…` provenance tags** in code comments (about 250 lines in 40 files of this lane; for example `sigma_leverage.py:295`, `orchestration.py:2173`) name retired paths | grep, run 6 | **not corrected, and no sweep.** The paths resolve through `references/restructure_ledger.md` by the tree's own convention, and a comment is not a mechanism (§0.05). A pattern in a process-only artifact earns no guard (§0.1 pt 5) |
| **X-6. All 121 probes execute** | run 1 | none needed; recorded because "does every registered probe still run" is what the 115 rows were really asking |

## 5. Evidence log

| # | command or probe | seed, seasons | outcome |
|---|---|---|---|
| 1 | `run_cases.run_probe(pid)` for every `pid` in `probes.PROBES`, `PYTHONHASHSEED=0` | n/a | 121 registered, 121 distinct functions; PASS 64, GAP 57; unregistered top-level functions are the 13 helpers |
| 2 | AST reachability over the 86 files with rows; module import graph over every tracked `.py` | n/a | Annex A; the family table of §0 |
| 3 | `runpy.run_path(file, run_name="census_import_probe")` for every file with rows under `systems/`, `modules/`, `engine/dice_engine/`, `engine/substrate/`, `engine/reference/` | n/a | all import; the nine SC kernel files refuse as scripts because they are package-relative (expected) |
| 4 | `storybar.drive(0, 2, "off", None)`; `arc.read_arcs(w, d, …)` four ways | seed 0, 2 seasons | 83 actors; default 0; `ambition_thrusts` 21; shuffled null 1; unrestricted 53; drive 24.6 s |
| 5 | `populated.run(3, 0, w=build_realm(0))`; `corpus_run.foreign_kinds(w)`, `unrowed_acts(w)` | seed 0, 3 seasons | 2,630 acts, 74,510 events; `foreign_kinds` empty; `unrowed_acts` 0. One seed: a count, not a rate |
| 6 | whole-word greps for each of the 26 new dead or broken rows over `engine modules systems tools tests skills` | n/a | as cited per row |
| 7 | `git status --short` at the end | n/a | only this lane's four files under the suite directory are new; no tracked file changed by this lane |

No `pytest` was run. Nothing was written outside the suite directory and the session scratchpad.

## 6. Layer 1 conformance of what is proposed (`UNIFICATION_BRIEF.md` item 7)

- **Deletions D1 to D3** remove functions and two files; they add no interface. `modules/mass_battle/`
  keeps typed input, typed outcome and no state. No Layer 1 row is in play.
- **W-1, W-2** touch `engine/season/harness/` only: driver-side readers that write no world.
  `architecture/meta/04_CODE_ARCHITECTURE.md` has no row naming the harness (a search of the file for
  "harness" returns nothing), so no row is graded; neither edit touches `state/`, `loop/`, a registry or
  a module.
- **W-4** is a gap named in another lane's proposal, not an edit.
- No guard, no new apparatus, no new corpus. Nothing here needs Jordan: every decision was taken on
  ladder steps 1 to 5 and the step is named at the row.
