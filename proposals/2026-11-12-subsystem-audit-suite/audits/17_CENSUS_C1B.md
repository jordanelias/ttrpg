# CENSUS C1B — unreferenced symbols outside `engine/season/` proper (harness, modules, systems, dice, substrate, reference)

## Status: REFERENCE (a census lane's audit; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 7a4d5e1 (working tree; game code is unchanged through b8039982, `git diff --stat 7a4d5e1 HEAD -- engine modules systems tests tools references` is empty)

Lane: PART=C1B of `CENSUS_BRIEF.md`. Rows: every row of `census/C1_unreferenced_symbols.md` whose file
starts with `engine/season/harness/`, `modules/`, `systems/`, `engine/dice_engine/`, `engine/substrate/`,
`engine/engine_params/` or `engine/reference/`. No row of the census falls under `engine/engine_params/`.

## 0. Verdict

**Four rows in five are false leads: 518 of 643 are reached by a route a name search cannot see, and
only 21 rows are dead code this lane newly finds.** The census's largest single block, the 115 rows
of `harness/probes.py`, is one mechanism (a decorator registry) and every one of the 121 registered
probes executes. The dead rows are dominated by one decision the suite has already made (the SC-05
kernel, 75 rows). What the lane adds: two instruments that are tested and that no person can run
(`harness/arc.py`'s arc reader, `corpus_run.foreign_kinds`), ten rows of threadwork oracle that
nothing reaches and nothing carries, and eleven rows of `modules/mass_battle/` that are uncalled,
test-only or empty (four of the eleven were already found by the MB audit).

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
`FORK:` row text), `17_CENSUS_C1B_02_wires.md` (W-1, W-2, and the gap W-3 put to the WR proposal's
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
(b) Cross-file edges are by name; a common name can supply a false edge, which can only make a dead
symbol look live. The 26 dead rows outside the SC kernel and the 5 harness rows called broken were
each read at the call site and grepped by whole word; the 518 false positives rest on the AST chain
in Annex A, spot-checked on the largest rows of each harness file and not row by row.

## 2. Why the false positives are false (518 rows, six mechanisms)

| mechanism | rows | evidence |
|---|---|---|
| **Decorator registry**: `@probe(pid, …)` writes `PROBES[pid] = dict(…, fn=fn)` (`harness/probes.py:61-68`); `run_cases.py:169-172` calls `spec["fn"]()`; `run_cases.main` runs every id (`:473`) | 111 probe functions, plus 4 helpers they call (`NOCHOOSE`, `_one_pass`, `_run_d`, `_seed_near_floor`) | run 1: 121 registered, 121 distinct functions, all executed: 64 PASS, 57 GAP, 0 INSTRUMENT-ERROR |
| **String roster through `globals()`**: `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`harness/invariants.py:242`), run by `violations` and `sweep` | 13 | `tools/m1_acceptance.py:366` and `:380` call `sweep`; `tests/valoria/test_season_invariant_sweep.py` breaks each by name |
| **Reached from `__main__`** of a hand-run instrument (harness) | 172 | AST chain per row, Annex A; `aperture` 34, `decision_spread` 23, `soak` 21, `strife` 16, `interactions` 13, `storybar` 12, others |
| **Runs at import** (a module-level table or call: `MOVES = load_moves()`, `validate_roster(ARC_SELF)`, `ABILITIES.update(_generics())`, `setattr(Combatant, _key, _attribute_property(_key))`) | 48 (harness 20, `systems/` 22, `modules/` 6) | chain root `import` in Annex A |
| **Reached from `__main__`** of a hand-run oracle or workbench script under `systems/combat/` and `systems/mass_battle/` (`balance.py` is CLAUDE.md §9's named instrument) | 76 | all 21 files import as scripts (run 3); `main` not run `[UNVERIFIED that each main completes]` |
| **A private helper of a function another file calls** (`modules/`, `engine/dice_engine/`, one in `systems/combat/`): the census listed the helper because only its own file names it | 84 (`modules/` 78, `engine/dice_engine/` 5, `probabilities.py::_beta_pdf` 1) | package reach from the composition entries, §1 pt 3; `roll_pool`, `band_odds`, `settle_margin` are called from `engine/season/seam/wrappers/sigma.py` and `modules/social_contest/roll.py` |

Ten false positives, in six groups, that needed a judgment and are not one of the mechanisms above:

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
| `systems/threadwork/sim/collective.py` (3), `opposing.py` (3) | as above, and no verb | carried by the same move, **with a gap this lane names (W-3)**: neither WR proposal gives a collective or an opposed working an entry, a verb or a caller, so after the move they are still test-only, now inside `modules/` | `09_WR_threadwork_module.md:79-80` (signatures change; no row added); `…replug.md` §3.3 ("no verb") |

### 3.3 Mislabelled: correct (1, and the corrections that ride on deletions)

`systems/combat/combat_engine_v1/capabilities.py:23` (`_affords_point`): the docstring names `systems.py`;
the module is `combat_systems.py` (C-1). Five further corrections follow from §3.1 and are in the
corrections proposal: a comment that points at a deleted function, a package docstring, two
`mechanics_index.yaml` rows, a field, and a composition row's `needed_by` text.

## 4. Where the census script cannot see (the brief's last paragraph, within this lane's files)

| finding | evidence | resolution |
|---|---|---|
| **X-1. Tests that exercise code nothing calls.** Beyond §3: `harness/arc.py::read_arcs` (not a census row: a test names it), `army_presets.install`, the whole threadwork oracle, `conviction.py`, `knots.py`, the SC kernel | the import graph tags each `TESTS` only | each has its decision above; none is left without one |
| **X-2. A `__main__` demo inside a registered module** is the only caller of two functions | `equipment/armour.py:59-63`, `equipment/weapons.py:67-72` | deleted with their functions (already decided, §3.1) |
| **X-3. An empty body that runs.** `rally_check`, `threadwork_check` | AST: body is `pass`; 2 of the 3 no-ops F-MB-10 lists (the third, `Subunit.halt_before_enemy`, is a method and not a census row) | already decided |
| **X-4. Text that describes code which does not exist** | `conviction.py:269` (`beliefs.revise_belief`); `capabilities.py:24` (`systems.py`); `registers/mechanics_index.yaml:466`, `:484` (`canon_sources: systems/threadwork/threadwork_v30.md`, a path under a tree that holds no `.md`; `test_status: not_implemented` beside a `sim_module` that exists) | C-1 to C-4 |
| **X-5. `[canonical: params/*.md]` and `designs/…` provenance tags** in code comments (about 250 lines in 40 files of this lane; for example `sigma_leverage.py:295`, `orchestration.py:2173`) name retired paths | grep, run 6 | **not corrected, and no sweep.** The paths resolve through `references/restructure_ledger.md` by the tree's own convention, and a comment is not a mechanism (§0.05). A pattern in a process-only artifact earns no guard (§0.1 pt 5) |
| **X-6. All 121 probes execute** | run 1 | none needed; recorded because "does every registered probe still run" is what the 115 rows were really asking |

## 5. Evidence log

| # | command or probe | seed, seasons | outcome |
|---|---|---|---|
| 1 | `run_cases.run_probe(pid)` for every `pid` in `probes.PROBES`, `PYTHONHASHSEED=0` | n/a | 121 registered, 121 distinct functions; PASS 64, GAP 57; unregistered top-level functions are the 13 helpers |
| 2 | AST reachability over the 94 files with rows; module import graph over every tracked `.py` | n/a | Annex A; the family table of §0 |
| 3 | `runpy.run_path(file, run_name="census_import_probe")` for every file with rows under `systems/`, `modules/`, `engine/dice_engine/`, `engine/substrate/`, `engine/reference/` | n/a | all import; the nine SC kernel files refuse as scripts because they are package-relative (expected) |
| 4 | `storybar.drive(0, 2, "off", None)`; `arc.read_arcs(w, d, …)` four ways | seed 0, 2 seasons | 83 actors; default 0; `ambition_thrusts` 21; shuffled null 1; unrestricted 53; drive 24.6 s |
| 5 | `populated.run(3, 0, w=build_realm(0))`; `corpus_run.foreign_kinds(w)`, `unrowed_acts(w)` | seed 0, 3 seasons | 2,630 acts, 74,510 events; `foreign_kinds` empty; `unrowed_acts` 0. One seed: a count, not a rate |
| 6 | whole-word greps for each of the 26 non-kernel dead rows and the 5 broken harness rows over `engine modules systems tools tests skills` | n/a | as cited per row |
| 7 | `git status --short` at the end | n/a | only this lane's four files under the suite directory are new; no tracked file changed by this lane |

No `pytest` was run. Nothing was written outside the suite directory and the session scratchpad.

## 6. Layer 1 conformance of what is proposed (`UNIFICATION_BRIEF.md` item 7)

- **Deletions D1 to D3** remove functions and two files; they add no interface. `modules/mass_battle/`
  keeps typed input, typed outcome and no state. No Layer 1 row is in play.
- **W-1, W-2** touch `engine/season/harness/` only: driver-side readers that write no world.
  `architecture/meta/04_CODE_ARCHITECTURE.md` has no row naming the harness (a search of the file for
  "harness" returns nothing), so no row is graded; neither edit touches `state/`, `loop/`, a registry or
  a module.
- **W-3** is a gap named in another lane's proposal, not an edit.
- No guard, no new apparatus, no new corpus. Nothing here needs Jordan: every decision was taken on
  ladder steps 1 to 5 and the step is named at the row.

## Annex A. Row ledger (all 643 rows, by file)

Generated from the AST pass and the decisions of §3; one line per census row. Chains are in-file call paths read by AST, name-based across files.

| file:line | name | decision | evidence |
|---|---|---|---|
| `engine/dice_engine/dice_engine.py:142` | `RollResult` | false positive | named in `modules/`: roll_pool > RollResult (`resolution.py`, `roll.py`) |
| `engine/dice_engine/dice_engine.py:191` | `_require_tn7` | false positive | named in `modules/`: roll_pool > _require_tn7 (`resolution.py`, `roll.py`) |
| `engine/dice_engine/sigma_leverage.py:292` | `_dice_dealt` | false positive | named in `modules/`: band_odds > _dice_dealt (`roll.py`) |
| `engine/dice_engine/sigma_leverage.py:299` | `_net_counts` | false positive | named in `modules/`: band_odds > _net_counts (`roll.py`) |
| `engine/dice_engine/sigma_leverage.py:316` | `_split_margin` | false positive | named in `modules/`: settle_margin > _split_margin (`roll.py`) |
| `engine/reference/degree-sweep/sweep_core.py:132` | `contested_verbs` | false positive | called at `proposals/2026-09-04-degree-sweep/arm1_admissibility.py:36`; the census did not search `proposals/` |
| `engine/season/harness/aperture.py:129` | `seat_gated` | false positive | `__main__`: `__main__` > main > report > seat_gated |
| `engine/season/harness/aperture.py:147` | `seat_depth` | false positive | `__main__`: main > measure > measure_world > seat_depth |
| `engine/season/harness/aperture.py:163` | `_Replay` | false positive | `__main__`: instrumented_season > refusal_reading > _replayed > _Replay |
| `engine/season/harness/aperture.py:176` | `_observed_of` | false positive | `__main__`: measure_world > instrumented_season > refusal_reading > _observed_of |
| `engine/season/harness/aperture.py:182` | `read_label` | false positive | `__main__`: measure_world > instrumented_season > refusal_reading > read_label |
| `engine/season/harness/aperture.py:201` | `_replayed` | false positive | `__main__`: measure_world > instrumented_season > refusal_reading > _replayed |
| `engine/season/harness/aperture.py:268` | `kind_census` | false positive | `__main__`: measure > measure_world > instrumented_season > kind_census |
| `engine/season/harness/aperture.py:306` | `_events_by_act` | false positive | `__main__`: measure_world > instrumented_season > refusal_reading > _events_by_act |
| `engine/season/harness/aperture.py:317` | `deaths_of` | false positive | `__main__`: measure_world > instrumented_season > wrong_kind > deaths_of |
| `engine/season/harness/aperture.py:335` | `_exists_zero_on` | false positive | `__main__`: measure_world > instrumented_season > wrong_kind > _exists_zero_on |
| `engine/season/harness/aperture.py:346` | `_lives_in` | false positive | `__main__`: measure_world > instrumented_season > wrong_kind > _lives_in |
| `engine/season/harness/aperture.py:357` | `wrong_kind` | false positive | `__main__`: measure > measure_world > instrumented_season > wrong_kind |
| `engine/season/harness/aperture.py:432` | `death_census` | false positive | `__main__`: measure > measure_world > instrumented_season > death_census |
| `engine/season/harness/aperture.py:454` | `source_key` | false positive | `__main__`: measure > measure_world > instrumented_season > source_key |
| `engine/season/harness/aperture.py:469` | `scene_sources` | false positive | `__main__`: measure > measure_world > instrumented_season > scene_sources |
| `engine/season/harness/aperture.py:595` | `measure_world` | false positive | `__main__`: `__main__` > main > measure > measure_world |
| `engine/season/harness/aperture.py:644` | `_control_same` | false positive | `__main__`: `__main__` > main > pooled_report > _control_same |
| `engine/season/harness/aperture.py:650` | `_control_line` | false positive | `__main__`: `__main__` > main > report > _control_line |
| `engine/season/harness/aperture.py:658` | `exists_zero` | false positive | `__main__`: main > report > _refusal_blocks > exists_zero |
| `engine/season/harness/aperture.py:666` | `_refusal_blocks` | false positive | `__main__`: `__main__` > main > report > _refusal_blocks |
| `engine/season/harness/aperture.py:704` | `verb_counts` | false positive | `__main__`: `__main__` > main > report > verb_counts |
| `engine/season/harness/aperture.py:722` | `pool_verb_counts` | false positive | `__main__`: `__main__` > main > pooled_report > pool_verb_counts |
| `engine/season/harness/aperture.py:736` | `_verb_line` | false positive | `__main__`: `__main__` > main > report > _verb_line |
| `engine/season/harness/aperture.py:744` | `verb_totals` | false positive | `__main__`: main > report > _verb_total_line > verb_totals |
| `engine/season/harness/aperture.py:749` | `persons_separated` | false positive | `__main__`: main > report > pools_lines > persons_separated |
| `engine/season/harness/aperture.py:758` | `pools_lines` | false positive | `__main__`: `__main__` > main > report > pools_lines |
| `engine/season/harness/aperture.py:778` | `_verb_total_line` | false positive | `__main__`: `__main__` > main > report > _verb_total_line |
| `engine/season/harness/aperture.py:793` | `pool_worlds` | false positive | `__main__`: `__main__` > main > pooled_report > pool_worlds |
| `engine/season/harness/aperture.py:845` | `_wrong_kind_blocks` | false positive | `__main__`: main > report > cr14_blocks > _wrong_kind_blocks |
| `engine/season/harness/aperture.py:878` | `_death_blocks` | false positive | `__main__`: main > report > cr14_blocks > _death_blocks |
| `engine/season/harness/aperture.py:895` | `_answered_blocks` | false positive | `__main__`: main > report > cr14_blocks > _answered_blocks |
| `engine/season/harness/aperture.py:921` | `cr14_blocks` | false positive | `__main__`: `__main__` > main > report > cr14_blocks |
| `engine/season/harness/aperture.py:927` | `seed_row` | false positive | `__main__`: `__main__` > main > pooled_report > seed_row |
| `engine/season/harness/aperture.py:941` | `pooled_report` | false positive | `__main__`: `__main__` > main > pooled_report |
| `engine/season/harness/arc.py:112` | `ArcRosterRefused` | false positive | runs at import: import > validate_roster > ArcRosterRefused |
| `engine/season/harness/arc.py:142` | `validate_roster` | false positive | runs at import: import > validate_roster |
| `engine/season/harness/arc.py:173` | `ambition_thrusts` | broken: wire | `read_arcs` and its clause-(1) predicate have no caller but `engine/season/tests/test_cl_thrust_b01_arc_reader.py`; the file has no `__main__`; wire W-1 |
| `engine/season/harness/arc.py:196` | `ArcReading` | broken: wire | `read_arcs` and its clause-(1) predicate have no caller but `engine/season/tests/test_cl_thrust_b01_arc_reader.py`; the file has no `__main__`; wire W-1 |
| `engine/season/harness/arms.py:160` | `_resolve_arm` | false positive | `__main__`: `__main__` > main > run_arm > _resolve_arm |
| `engine/season/harness/arms.py:188` | `run_arm` | false positive | `__main__`: `__main__` > main > run_arm |
| `engine/season/harness/arms.py:215` | `two_proportion_z` | false positive | `__main__`: `__main__` > main > two_proportion_z |
| `engine/season/harness/arms.py:255` | `_pool_arm` | false positive | runs at import: import > _pool_arm |
| `engine/season/harness/army_presets.py:52` | `_commander` | broken: wire | reached through `install`, whose callers are tests only; contract row `mass_battle.army_preset` says "shipped off: nothing in the season loop calls it"; the wire is `proposals/04_MB_playable_field_scenario.md` (MB R-07) |
| `engine/season/harness/army_presets.py:58` | `plan_for` | broken: wire | reached through `install`, whose callers are tests only; contract row `mass_battle.army_preset` says "shipped off: nothing in the season loop calls it"; the wire is `proposals/04_MB_playable_field_scenario.md` (MB R-07) |
| `engine/season/harness/chronicle.py:86` | `deepest_chain` | false positive | `__main__`: `__main__` > main > deepest_chain |
| `engine/season/harness/chronicle.py:170` | `chain_ends` | false positive | `__main__`: `__main__` > main > consequence_chains > chain_ends |
| `engine/season/harness/chronicle.py:177` | `consequence_chains` | false positive | `__main__`: `__main__` > main > consequence_chains |
| `engine/season/harness/chronicle.py:193` | `render_chains` | false positive | `__main__`: `__main__` > main > render_chains |
| `engine/season/harness/conviction_spread.py:50` | `_covariance` | false positive | `__main__`: `__main__` > main > spread > _covariance |
| `engine/season/harness/conviction_spread.py:68` | `_eigenvalues` | false positive | `__main__`: `__main__` > main > spread > _eigenvalues |
| `engine/season/harness/conviction_spread.py:200` | `_report` | false positive | `__main__`: `__main__` > main > _report |
| `engine/season/harness/corpus_run.py:131` | `_exercise_docs` | false positive | runs at import: import > cast_overlay > _exercise_docs |
| `engine/season/harness/corpus_run.py:213` | `_waits_on_player` | false positive | `__main__`: build_at > seating > _partition_cast > _waits_on_player |
| `engine/season/harness/corpus_run.py:217` | `_partition_cast` | false positive | `__main__`: main > build_at > seating > _partition_cast |
| `engine/season/harness/corpus_run.py:317` | `_referent` | false positive | `__main__`: `__main__` > main > build_at > _referent |
| `engine/season/harness/corpus_run.py:367` | `_check_cast` | false positive | runs at import: import > cast_overlay > _check_cast |
| `engine/season/harness/corpus_run.py:685` | `_register_sites` | false positive | `__main__`: `__main__` > main > run_case > _register_sites |
| `engine/season/harness/corpus_run.py:738` | `_span_status` | false positive | `__main__`: `__main__` > main > run_case > _span_status |
| `engine/season/harness/corpus_run.py:751` | `_emission_id` | false positive | `__main__`: main > planted_control > _r3_propagates > _emission_id |
| `engine/season/harness/corpus_run.py:832` | `foreign_kinds` | broken: wire | test-only (`test_aperture.py:225-230`); its sibling `unrowed_acts` is printed by `aperture` (`aperture.py:583`) and this is not; wire W-2 |
| `engine/season/harness/corpus_run.py:891` | `degrees_by_verb` | false positive | `__main__`: `__main__` > main > run_case > degrees_by_verb |
| `engine/season/harness/corpus_run.py:909` | `bands_that_differ` | false positive | `__main__`: `__main__` > main > bands_that_differ |
| `engine/season/harness/corpus_run.py:919` | `deposit_only_rulings` | false positive | `__main__`: `__main__` > main > emits_and_writes_nothing > deposit_only_rulings |
| `engine/season/harness/corpus_run.py:926` | `emits_and_writes_nothing` | false positive | `__main__`: `__main__` > main > emits_and_writes_nothing |
| `engine/season/harness/decision_spread.py:127` | `realm_mean_pursuits` | false positive | `__main__`: main > _build > apply_control > realm_mean_pursuits |
| `engine/season/harness/decision_spread.py:137` | `realm_mean_conviction` | false positive | `__main__`: main > _build > apply_control > realm_mean_conviction |
| `engine/season/harness/decision_spread.py:145` | `apply_control` | false positive | `__main__`: `__main__` > main > _build > apply_control |
| `engine/season/harness/decision_spread.py:172` | `null_alignment` | false positive | `__main__`: `__main__` > main > null_alignment |
| `engine/season/harness/decision_spread.py:240` | `new_split` | false positive | `__main__`: `__main__` > main > read_decisions > new_split |
| `engine/season/harness/decision_spread.py:245` | `tally_split` | false positive | `__main__`: `__main__` > main > read_decisions > tally_split |
| `engine/season/harness/decision_spread.py:263` | `split_figures` | false positive | `__main__`: `__main__` > main > read_decisions > split_figures |
| `engine/season/harness/decision_spread.py:276` | `_cosine` | false positive | `__main__`: `__main__` > main > read_persons > _cosine |
| `engine/season/harness/decision_spread.py:283` | `projected_vector` | false positive | `__main__`: `__main__` > main > read_persons > projected_vector |
| `engine/season/harness/decision_spread.py:288` | `territory_of` | false positive | `__main__`: `__main__` > main > read_persons > territory_of |
| `engine/season/harness/decision_spread.py:298` | `profile_key` | false positive | `__main__`: `__main__` > main > read_persons > profile_key |
| `engine/season/harness/decision_spread.py:310` | `_pair_cosines` | false positive | `__main__`: `__main__` > main > read_persons > _pair_cosines |
| `engine/season/harness/decision_spread.py:315` | `read_persons` | false positive | `__main__`: `__main__` > main > read_persons |
| `engine/season/harness/decision_spread.py:377` | `decision_question` | false positive | `__main__`: `__main__` > main > read_decisions > decision_question |
| `engine/season/harness/decision_spread.py:383` | `formed_set` | false positive | `__main__`: `__main__` > main > read_decisions > formed_set |
| `engine/season/harness/decision_spread.py:391` | `read_decisions` | false positive | `__main__`: `__main__` > main > read_decisions |
| `engine/season/harness/decision_spread.py:509` | `print_persons` | false positive | `__main__`: `__main__` > main > print_persons |
| `engine/season/harness/decision_spread.py:528` | `print_decisions` | false positive | `__main__`: `__main__` > main > print_decisions |
| `engine/season/harness/decision_spread.py:541` | `print_split` | false positive | `__main__`: `__main__` > main > print_season > print_split |
| `engine/season/harness/decision_spread.py:551` | `print_season` | false positive | `__main__`: `__main__` > main > print_season |
| `engine/season/harness/decision_spread.py:565` | `_decider_total` | false positive | `__main__`: `__main__` > main > print_decisions > _decider_total |
| `engine/season/harness/decision_spread.py:572` | `_build` | false positive | `__main__`: `__main__` > main > _build |
| `engine/season/harness/decision_spread.py:579` | `run_arms` | false positive | `__main__`: `__main__` > main > run_arms |
| `engine/season/harness/delta.py:62` | `_cases` | false positive | `__main__`: `__main__` > report > _cases |
| `engine/season/harness/exercises.py:155` | `orphan_cases` | false positive | `__main__`: `__main__` > orphan_cases |
| `engine/season/harness/heir_hears.py:57` | `HeirSpy` | false positive | `__main__`: `__main__` > main > seeded_reading > HeirSpy |
| `engine/season/harness/heir_hears.py:94` | `one_season` | false positive | `__main__`: `__main__` > main > seeded_reading > one_season |
| `engine/season/harness/heir_hears.py:100` | `seeded_reading` | false positive | `__main__`: `__main__` > main > seeded_reading |
| `engine/season/harness/interactions.py:99` | `held_offices` | false positive | `__main__`: `__main__` > main > run > held_offices |
| `engine/season/harness/interactions.py:104` | `same_faction` | false positive | `__main__`: main > run > relation > same_faction |
| `engine/season/harness/interactions.py:111` | `faction_heads` | false positive | `__main__`: `__main__` > main > run > faction_heads |
| `engine/season/harness/interactions.py:117` | `office_relation` | false positive | `__main__`: main > run > relation > office_relation |
| `engine/season/harness/interactions.py:147` | `known_via` | false positive | `__main__`: main > run > relation > known_via |
| `engine/season/harness/interactions.py:194` | `person_targets` | false positive | `__main__`: `__main__` > main > run > person_targets |
| `engine/season/harness/interactions.py:207` | `is_hostile` | false positive | `__main__`: `__main__` > main > run > is_hostile |
| `engine/season/harness/interactions.py:217` | `_question` | false positive | `__main__`: `__main__` > main > run > _question |
| `engine/season/harness/interactions.py:330` | `act_rows` | false positive | `__main__`: `__main__` > main > run > act_rows |
| `engine/season/harness/interactions.py:397` | `print_summary` | false positive | `__main__`: `__main__` > main > print_summary |
| `engine/season/harness/interactions.py:418` | `print_audit` | false positive | `__main__`: `__main__` > main > print_audit |
| `engine/season/harness/interactions.py:435` | `_rows_by_i` | false positive | `__main__`: `__main__` > main > print_audit > _rows_by_i |
| `engine/season/harness/interactions.py:439` | `write_jsonl` | false positive | `__main__`: `__main__` > main > write_jsonl |
| `engine/season/harness/invariants.py:53` | `_entities` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:78` | `_all_tenures` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:95` | `tenure_interval` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:108` | `tenure_referent` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:126` | `log_ids_unique` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:137` | `log_not_from_the_future` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:147` | `claim_not_from_the_future` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:163` | `body_in_range` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:174` | `stance_row_shape` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:228` | `office_singly_held` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:249` | `carrier_census` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:299` | `_declared_for` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/invariants.py:342` | `carrier_census_keys` | false positive | `CHECKS = {name: globals()[name] for name in INVARIANTS}` (`:242`) or called by `sweep`/`violations`; `tools/m1_acceptance.py:366` runs `sweep` |
| `engine/season/harness/loops.py:188` | `_mul` | false positive | `__main__`: `__main__` > main > derive_cycles > _mul |
| `engine/season/harness/loops.py:214` | `_simple_cycles` | false positive | `__main__`: `__main__` > main > derive_cycles > _simple_cycles |
| `engine/season/harness/loops.py:239` | `derive_cycles` | false positive | `__main__`: `__main__` > main > derive_cycles |
| `engine/season/harness/loops.py:286` | `check_bounds` | false positive | `__main__`: `__main__` > main > check_bounds |
| `engine/season/harness/loops.py:306` | `row_quantities` | false positive | `__main__`: `__main__` > main > row_quantities |
| `engine/season/harness/loops.py:311` | `_ledger_max` | false positive | runs at import: import > _ledger_max |
| `engine/season/harness/loops.py:315` | `_confidence_max` | false positive | runs at import: import > _confidence_max |
| `engine/season/harness/loops.py:352` | `_leaves` | false positive | `__main__`: `__main__` > main > build_processes > _leaves |
| `engine/season/harness/loops.py:359` | `_exists_reads` | false positive | `__main__`: `__main__` > main > build_processes > _exists_reads |
| `engine/season/harness/loops.py:374` | `build_processes` | false positive | `__main__`: `__main__` > main > build_processes |
| `engine/season/harness/loops.py:442` | `loop_rows` | false positive | `__main__`: `__main__` > main > loop_rows |
| `engine/season/harness/loops.py:455` | `_bound_arg` | false positive | `__main__`: `__main__` > main > _bound_arg |
| `engine/season/harness/military_menu.py:46` | `MilitaryMenu` | false positive | runs at import: import > MilitaryMenu |
| `engine/season/harness/obligee_report.py:71` | `ObligeeReading` | false positive | `__main__`: `__main__` > main > read_obligee_reports > ObligeeReading |
| `engine/season/harness/obligee_report.py:94` | `_live_at` | false positive | `__main__`: `__main__` > main > read_obligee_reports > _live_at |
| `engine/season/harness/obligee_report.py:98` | `read_obligee_reports` | false positive | `__main__`: `__main__` > main > read_obligee_reports |
| `engine/season/harness/populated.py:133` | `_index_anchor` | false positive | `__main__`: `__main__` > main > build_realm > _index_anchor |
| `engine/season/harness/populated.py:216` | `_mentions` | false positive | `__main__`: main > build_realm > institution_of > _mentions |
| `engine/season/harness/populated.py:226` | `_institutions` | false positive | `__main__`: main > build_realm > institution_of > _institutions |
| `engine/season/harness/populated.py:255` | `institution_of` | false positive | `__main__`: `__main__` > main > build_realm > institution_of |
| `engine/season/harness/populated.py:284` | `surname_index` | false positive | `__main__`: `__main__` > main > build_realm > surname_index |
| `engine/season/harness/populated.py:565` | `_first_holder` | false positive | `__main__`: main > build_realm > acquaintance_pairs > _first_holder |
| `engine/season/harness/populated.py:589` | `acquaintance_pairs` | false positive | `__main__`: `__main__` > main > build_realm > acquaintance_pairs |
| `engine/season/harness/populated.py:802` | `goals_missing` | false positive | `__main__`: main > build_realm > seed_goals > goals_missing |
| `engine/season/harness/probes.py:142` | `NOCHOOSE` | false positive | called by registered probes: <module>, f10 |
| `engine/season/harness/probes.py:188` | `_one_pass` | false positive | called by registered probes: a37, a38, a5 |
| `engine/season/harness/probes.py:203` | `_run_d` | false positive | called by registered probes: a31, a36, a37 |
| `engine/season/harness/probes.py:228` | `p1` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:380` | `p2x` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:395` | `p2y` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:433` | `p3` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:452` | `p4` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:467` | `p5` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:478` | `p6` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:495` | `p7` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:514` | `p8` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:528` | `p9` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:549` | `p10` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:598` | `p12` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:626` | `p13` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:639` | `p14` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:666` | `p15` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:731` | `p16` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:744` | `p17` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:758` | `p18` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:810` | `p19` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:820` | `p20` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:835` | `p21` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:864` | `p22` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:906` | `p23` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:919` | `p24` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:946` | `p25` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:957` | `p26` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:965` | `p27` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:978` | `p28` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1016` | `p29` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1025` | `p30` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1039` | `p31` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1103` | `p33` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1113` | `p34` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1130` | `p35` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1140` | `p36` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1269` | `f4` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1283` | `f5` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1314` | `f6` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1370` | `f8` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1397` | `f9` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1415` | `f10` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1498` | `f11` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1511` | `f12` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1548` | `f13` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1573` | `f14` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1585` | `f15` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1598` | `f16` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1628` | `f16b` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1636` | `f17` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1655` | `f18` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1676` | `f19` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1688` | `_seed_near_floor` | false positive | called by registered probes: p18, w1 |
| `engine/season/harness/probes.py:1722` | `w1` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1745` | `w1x` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1765` | `w3` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1775` | `w4` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1787` | `w5` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1796` | `w6` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1808` | `w7` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1828` | `w8` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1848` | `w9` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1863` | `w10` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1872` | `w11` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1883` | `w12` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1934` | `a3` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1946` | `a4` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:1965` | `a5` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2073` | `a6` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2083` | `a7` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2092` | `a8` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2121` | `a9` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2132` | `a10` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2148` | `a11` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2156` | `a12` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2165` | `a13` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2182` | `a14` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2227` | `a15` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2237` | `a16` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2249` | `a17` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2262` | `a18` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2273` | `a19` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2282` | `a20` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2296` | `a21` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2306` | `a22` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2326` | `a23` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2336` | `a24` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2353` | `a25` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2372` | `a26` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2385` | `a27` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2399` | `a28` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2440` | `a29` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2452` | `a30` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2460` | `a31` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2485` | `a31b` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2528` | `a32` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2552` | `a33` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2562` | `a34` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2573` | `a36` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2597` | `w13` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2609` | `p37` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2644` | `p38` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2659` | `p39` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2675` | `p40` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2691` | `p41` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2705` | `f20` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2724` | `f21` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2755` | `a37` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2786` | `a38` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2817` | `a31c` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2867` | `a39` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2917` | `p43` | false positive | called by registered probes:  |
| `engine/season/harness/probes.py:2929` | `p42` | false positive | called by registered probes:  |
| `engine/season/harness/register.py:149` | `section_exists` | false positive | runs at import: import > rule_G8 > section_exists |
| `engine/season/harness/register.py:165` | `part_b_defects` | false positive | runs at import: import > rule_G8 > part_b_defects |
| `engine/season/harness/register.py:188` | `rule_R0` | false positive | runs at import: import > rule_R0 |
| `engine/season/harness/register.py:205` | `rule_R1` | false positive | runs at import: import > rule_R1 |
| `engine/season/harness/register.py:232` | `rule_R3` | false positive | runs at import: import > rule_R3 |
| `engine/season/harness/register.py:239` | `rule_G6` | false positive | runs at import: import > rule_G6 |
| `engine/season/harness/register.py:245` | `rule_G12` | false positive | runs at import: import > rule_G12 |
| `engine/season/harness/register.py:277` | `rule_G8` | false positive | runs at import: import > rule_G8 |
| `engine/season/harness/register.py:315` | `rule_G13` | false positive | runs at import: import > rule_G13 |
| `engine/season/harness/register.py:374` | `_source_bucket` | false positive | `__main__`: `__main__` > main > counts > _source_bucket |
| `engine/season/harness/register.py:439` | `_cite_norm` | false positive | `__main__`: `__main__` > main > verify_citations > _cite_norm |
| `engine/season/harness/register.py:457` | `_contains` | false positive | `__main__`: `__main__` > main > verify_citations > _contains |
| `engine/season/harness/register.py:470` | `_rows_text_excluding` | false positive | `__main__`: `__main__` > main > verify_citations > _rows_text_excluding |
| `engine/season/harness/register.py:631` | `check_requirements` | false positive | `__main__`: `__main__` > main > check_requirements |
| `engine/season/harness/run_cases.py:318` | `_probe_view` | false positive | `__main__`: `__main__` > main > grade > _probe_view |
| `engine/season/harness/scarce.py:171` | `shortfall_question` | false positive | `__main__`: `__main__` > main > run > shortfall_question |
| `engine/season/harness/soak.py:91` | `_require_pinned_hashseed` | false positive | `__main__`: `__main__` > main > _require_pinned_hashseed |
| `engine/season/harness/soak.py:103` | `_require_out_dir` | false positive | `__main__`: `__main__` > main > _require_out_dir |
| `engine/season/harness/soak.py:118` | `_require_clean_engine` | false positive | `__main__`: `__main__` > main > _require_clean_engine |
| `engine/season/harness/soak.py:146` | `_act_row` | false positive | `__main__`: `__main__` > main > _run_world > _act_row |
| `engine/season/harness/soak.py:178` | `_canary_h156` | false positive | `__main__`: `__main__` > main > _run_world > _canary_h156 |
| `engine/season/harness/soak.py:198` | `_tenure_row` | false positive | `__main__`: main > _run_world > _person_row > _tenure_row |
| `engine/season/harness/soak.py:202` | `_claim_row` | false positive | `__main__`: main > _run_world > _person_row > _claim_row |
| `engine/season/harness/soak.py:209` | `_person_row` | false positive | `__main__`: `__main__` > main > _run_world > _person_row |
| `engine/season/harness/soak.py:229` | `_innermost_season_frame` | false positive | `__main__`: `__main__` > main > _run_world > _innermost_season_frame |
| `engine/season/harness/soak.py:238` | `_append_jsonl` | false positive | `__main__`: `__main__` > main > _run_world > _append_jsonl |
| `engine/season/harness/soak.py:244` | `_record_escape` | false positive | `__main__`: `__main__` > main > _run_world > _record_escape |
| `engine/season/harness/soak.py:256` | `_run_world` | false positive | `__main__`: `__main__` > main > _run_world |
| `engine/season/harness/soak.py:448` | `grade_cost` | false positive | `__main__`: `__main__` > main > grade_run > grade_cost |
| `engine/season/harness/soak.py:469` | `_tv_distance` | false positive | `__main__`: main > grade_run > grade_mix > _tv_distance |
| `engine/season/harness/soak.py:480` | `grade_mix` | false positive | `__main__`: `__main__` > main > grade_run > grade_mix |
| `engine/season/harness/soak.py:521` | `_read_jsonl` | false positive | `__main__`: main > grade_run > load_series > _read_jsonl |
| `engine/season/harness/soak.py:529` | `load_series` | false positive | `__main__`: `__main__` > main > grade_run > load_series |
| `engine/season/harness/soak.py:542` | `grade_run` | false positive | `__main__`: `__main__` > main > grade_run |
| `engine/season/harness/soak.py:570` | `_fmt_grade` | false positive | `__main__`: `__main__` > main > grade_run > _fmt_grade |
| `engine/season/harness/soak.py:579` | `_parse_args` | false positive | `__main__`: `__main__` > main > _parse_args |
| `engine/season/harness/soak.py:605` | `_require_fresh_world_dir` | false positive | `__main__`: `__main__` > main > _require_fresh_world_dir |
| `engine/season/harness/storybar.py:154` | `_depths` | false positive | `__main__`: main > draw_seed_arm > read > _depths |
| `engine/season/harness/storybar.py:192` | `summarise` | false positive | `__main__`: `__main__` > main > draw_seed_arm > summarise |
| `engine/season/harness/storybar.py:203` | `per_season` | false positive | `__main__`: `__main__` > main > compare > per_season |
| `engine/season/harness/storybar.py:226` | `executed_items` | false positive | `__main__`: main > compare > run_seed > executed_items |
| `engine/season/harness/storybar.py:233` | `executed_summary` | false positive | `__main__`: `__main__` > main > compare > executed_summary |
| `engine/season/harness/storybar.py:255` | `executed_per_season` | false positive | `__main__`: `__main__` > main > compare > executed_per_season |
| `engine/season/harness/storybar.py:318` | `run_seed` | false positive | `__main__`: `__main__` > main > compare > run_seed |
| `engine/season/harness/storybar.py:406` | `draw_seed_arm` | false positive | `__main__`: `__main__` > main > draw_seed_arm |
| `engine/season/harness/storybar.py:445` | `chain_difference` | false positive | `__main__`: `__main__` > main > _print_draw_seeds > chain_difference |
| `engine/season/harness/storybar.py:451` | `_print_draw_seeds` | false positive | `__main__`: `__main__` > main > _print_draw_seeds |
| `engine/season/harness/storybar.py:484` | `_fmt_exec` | false positive | `__main__`: `__main__` > main > _fmt_exec |
| `engine/season/harness/storybar.py:492` | `_fmt_est` | false positive | `__main__`: `__main__` > main > _fmt_est |
| `engine/season/harness/strife.py:66` | `Readers` | false positive | `__main__`: main > measure > readers_for > Readers |
| `engine/season/harness/strife.py:143` | `terminal_codes` | false positive | `__main__`: `__main__` > main > report > terminal_codes |
| `engine/season/harness/strife.py:148` | `routeless_terminals` | false positive | `__main__`: `__main__` > main > report > routeless_terminals |
| `engine/season/harness/strife.py:155` | `opening_kinds` | false positive | `__main__`: measure > strands_block > opening_routes > opening_kinds |
| `engine/season/harness/strife.py:160` | `opening_producers` | false positive | `__main__`: measure > strands_block > opening_routes > opening_producers |
| `engine/season/harness/strife.py:170` | `opening_routes` | false positive | `__main__`: main > measure > strands_block > opening_routes |
| `engine/season/harness/strife.py:184` | `routeless_pairs` | false positive | `__main__`: main > measure > strands_block > routeless_pairs |
| `engine/season/harness/strife.py:198` | `_reachable_codes` | false positive | runs at import: import > _reachable_codes |
| `engine/season/harness/strife.py:221` | `terminal_for` | false positive | `__main__`: main > measure > strands_block > terminal_for |
| `engine/season/harness/strife.py:236` | `_single_code_runs` | false positive | `__main__`: measure > strands_block > pair_profile > _single_code_runs |
| `engine/season/harness/strife.py:274` | `_by_pair` | false positive | `__main__`: strands_block > link_lines > flow_profile > _by_pair |
| `engine/season/harness/strife.py:282` | `_instances` | false positive | `__main__`: strands_block > link_lines > flow_profile > _instances |
| `engine/season/harness/strife.py:294` | `link_profile` | false positive | `__main__`: measure > strands_block > link_lines > link_profile |
| `engine/season/harness/strife.py:316` | `flow_profile` | false positive | `__main__`: measure > strands_block > link_lines > flow_profile |
| `engine/season/harness/strife.py:353` | `link_lines` | false positive | `__main__`: main > measure > strands_block > link_lines |
| `engine/season/harness/strife.py:383` | `opened_on` | false positive | `__main__`: main > measure > strands_block > opened_on |
| `engine/season/harness/strife.py:389` | `strands_block` | false positive | `__main__`: `__main__` > main > measure > strands_block |
| `engine/season/harness/strife_data.py:26` | `declared_kinds` | false positive | runs at import: import > load_moves > declared_kinds |
| `engine/season/harness/strife_data.py:37` | `load_moves` | false positive | runs at import: import > load_moves |
| `engine/substrate/stubwire.py:80` | `reset_invocations` | false positive | test-isolation helper for a process-global counter, declared test-only at `stubwire.py:70-72`; called by `tests/valoria/test_stubwire.py` |
| `modules/combat/ability_primitives.py:112` | `_generics` | false positive | runs at import: import > _generics |
| `modules/combat/combat_systems.py:65` | `forward_extent` | false positive | named in `modules/`: reach_base > forward_extent (`config.py`, `wrapper.py`) |
| `modules/combat/combat_systems.py:88` | `_heft_of` | false positive | named in `modules/`: wield_heft > _heft_of (`config.py`) |
| `modules/combat/combat_systems.py:452` | `_commit_range_factor` | false positive | named in `modules/`: commit_depth > _commit_range_factor (`wrapper.py`) |
| `modules/combat/combat_systems.py:488` | `_element_mass_x` | false positive | named in `modules/`: element_afforded > _element_mass_x (`core.py`, `vocabulary.py`) |
| `modules/combat/combatant.py:200` | `_attribute_property` | false positive | runs at import: import > _attribute_property |
| `modules/combat/contact.py:18` | `_short_reach_exempt` | false positive | named in `modules/`: grab_available > _short_reach_exempt (`wrapper.py`) |
| `modules/combat/core.py:303` | `_transmit` | false positive | named in `modules/`: cut_thrust_arm > _transmit (`combat_systems.py`, `weapon_physics.py`) |
| `modules/combat/core.py:366` | `_shear_yield` | false positive | named in `modules/`: coupling > _shear_yield (`combat_systems.py`, `combatant.py`) |
| `modules/combat/core.py:518` | `_puncture_adef` | false positive | named in `modules/`: adef_cap > _puncture_adef (`combat_systems.py`, `combatant.py`) |
| `modules/combat/core.py:595` | `strike_impact` | false positive | named in `modules/`: cut_thrust_impacts > strike_impact (`combat_systems.py`, `weapon_physics.py`) |
| `modules/combat/fight.py:32` | `_kit_kw` | false positive | named in `modules/`: fight > _kit_kw (`ability_primitives.py`, `attributes.py`) |
| `modules/combat/fight.py:38` | `_faculty_kw` | false positive | named in `modules/`: fight > _faculty_kw (`ability_primitives.py`, `attributes.py`) |
| `modules/combat/fight.py:44` | `_attr_kw` | false positive | named in `modules/`: fight > _attr_kw (`ability_primitives.py`, `attributes.py`) |
| `modules/combat/geometry.py:60` | `percussion_concentration` | false positive | named in `modules/`: bake > percussion_concentration (`combat_systems.py`, `core.py`) |
| `modules/combat/weapon_physics.py:42` | `_ltr_sum` | false positive | named in `modules/`: derive > _ltr_sum (`combat_systems.py`, `combatant.py`) |
| `modules/combat/weapon_physics.py:108` | `energy_credit` | false positive | named in `modules/`: percussion_authority > energy_credit (`combat_systems.py`, `combatant.py`) |
| `modules/combat/weapon_physics.py:156` | `_all_parts` | false positive | named in `modules/`: derive > _all_parts (`combat_systems.py`, `combatant.py`) |
| `modules/combat/weapon_physics.py:262` | `grip_swing_ratio` | false positive | named in `modules/`: phi_grip > grip_swing_ratio (`combat_systems.py`) |
| `modules/combat/weapon_physics.py:292` | `phi_room_percussion` | false positive | named in `modules/`: percussion_authority > phi_room_percussion (`combat_systems.py`, `combatant.py`) |
| `modules/combat/weapon_physics.py:367` | `delivered_strike` | false positive | named in `modules/`: strike_point_lever > delivered_strike (`combat_systems.py`) |
| `modules/combat/weapon_physics.py:657` | `_guard_catch_raw` | false positive | named in `modules/`: hand_guard > _guard_catch_raw (`combat_systems.py`, `config.py`) |
| `modules/combat/weapon_physics.py:735` | `_blade_edges` | false positive | named in `modules/`: edge_lines > _blade_edges (`combat_systems.py`, `config.py`) |
| `modules/combat/weapon_physics.py:822` | `_arm_lever` | false positive | named in `modules/`: heft_by_arm > _arm_lever (`core.py`) |
| `modules/combat/weapon_physics.py:908` | `_gather_len` | false positive | named in `modules/`: grip_choke_max > _gather_len (`combat_systems.py`, `config.py`) |
| `modules/combat/weapon_physics.py:925` | `_geom_slide_max` | false positive | named in `modules/`: at_circumstance > _geom_slide_max (`combat_systems.py`) |
| `modules/combat/weapons.py:845` | `_E` | false positive | runs at import: import > _E |
| `modules/combat/wrapper.py:36` | `_emit_outcome` | false positive | named in `modules/`: engagement > _emit_outcome (`combat_systems.py`, `config.py`) |
| `modules/combat/wrapper.py:49` | `_select` | false positive | named in `modules/`: engagement > _select (`combat_systems.py`, `config.py`) |
| `modules/combat/wrapper.py:57` | `_carry` | false positive | named in `modules/`: engagement > _carry (`combat_systems.py`, `config.py`) |
| `modules/combat/wrapper.py:528` | `_terms_met` | false positive | named in `modules/`: engagement > _terms_met (`combat_systems.py`, `config.py`) |
| `modules/combat/wrapper.py:531` | `_terms_yielder` | false positive | named in `modules/`: fight > _terms_yielder (`combat_systems.py`, `combatant.py`) |
| `modules/mass_battle/armyrecord.py:50` | `_type` | false positive | named in `modules/`: raised > _type (`presets.py`) |
| `modules/mass_battle/armyrecord.py:57` | `_pos` | false positive | named in `modules/`: raised > _pos (`presets.py`) |
| `modules/mass_battle/armyrecord.py:84` | `by_type` | false positive | named in `modules/`: cohort_claims > by_type (`presets.py`) |
| `modules/mass_battle/armyrecord.py:122` | `_sf_index` | false positive | named in `modules/`: order > _sf_index (`presets.py`) |
| `modules/mass_battle/armyrecord.py:129` | `_replace_sf` | false positive | named in `modules/`: order > _replace_sf (`presets.py`) |
| `modules/mass_battle/armyrecord.py:256` | `to_order_of_battle` | false positive | named in `engine/season/`: fielded > to_order_of_battle (`inputs.py`) |
| `modules/mass_battle/core/contact.py:417` | `_find_contacts_standoff` | false positive | named in `modules/`: find_contacts > _find_contacts_standoff (`battle_loop.py`, `exchange.py`) |
| `modules/mass_battle/core/contact.py:479` | `_find_contacts_field` | false positive | named in `modules/`: find_contacts > _find_contacts_field (`battle_loop.py`, `exchange.py`) |
| `modules/mass_battle/equipment/_base.py:15` | `EquipmentRecord` | false positive | named in `modules/`: Registry > EquipmentRecord (`armour.py`, `weapons.py`) |
| `modules/mass_battle/equipment/armour.py:50` | `dr_vs_piercing` | dead: delete | its one caller is the file's own `__main__` demo print (`:63`); `audits/04_MB_audit.md` F-MB-10: no reader; dies with `ARMOURY` under `proposals/04_MB_unit_loadout_and_weapon_in_hand.md` |
| `modules/mass_battle/equipment/weapons.py:63` | `with_keyword` | dead: delete | its one caller is the file's own `__main__` demo print (`:72`); weapon `keywords` have no reader (F-MB-10); dies with `ARSENAL` under `proposals/04_MB_unit_loadout_and_weapon_in_hand.md` |
| `modules/mass_battle/geometry.py:11` | `arrowhead_cells` | false positive | runs at import: import > arrowhead_cells |
| `modules/mass_battle/geometry.py:21` | `line_cells` | false positive | runs at import: import > line_cells |
| `modules/mass_battle/geometry.py:27` | `column_cells` | false positive | runs at import: import > column_cells |
| `modules/mass_battle/geometry.py:62` | `_build_shape_n` | false positive | named in `modules/`: footprint_for > _build_shape_n (`armies.py`, `units.py`) |
| `modules/mass_battle/geometry.py:215` | `atom_max_width` | false positive | named in `modules/`: support_engage_frac > atom_max_width (`exchange.py`, `orchestration.py`) |
| `modules/mass_battle/geometry.py:379` | `_normalize_heading` | false positive | named in `modules/`: CellBody > _normalize_heading (`contact.py`, `units.py`) |
| `modules/mass_battle/geometry.py:393` | `_rotate90` | false positive | named in `modules/`: engaged_frontage > _rotate90 (`attrition.py`, `contact.py`) |
| `modules/mass_battle/geometry.py:421` | `_dist_point_to_segment` | false positive | named in `modules/`: reach_reaches > _reach_body_overlap > _dist_point_to_segment (`contact.py`, `units.py`) |
| `modules/mass_battle/geometry.py:435` | `body_overlap` | false positive | specification predicate: the control `reach_reaches` (runtime, `core/contact.py:457`) is checked against in `test_body_primitive.py` (`test_zero_reach_collapses_to_plain_overlap_seeded`); in `__all__` |
| `modules/mass_battle/geometry.py:443` | `_reach_body_overlap` | false positive | named in `modules/`: reach_reaches > _reach_body_overlap (`contact.py`, `units.py`) |
| `modules/mass_battle/geometry.py:473` | `_project_interval` | false positive | named in `modules/`: engaged_frontage > _project_interval (`attrition.py`, `contact.py`) |
| `modules/mass_battle/geometry.py:479` | `_merge_intervals` | false positive | named in `modules/`: engaged_frontage > _merge_intervals (`attrition.py`, `contact.py`) |
| `modules/mass_battle/geometry.py:494` | `_interval_union_length` | false positive | named in `modules/`: engaged_frontage > _interval_union_length (`attrition.py`, `contact.py`) |
| `modules/mass_battle/hierarchy/units.py:127` | `standoff_from_reach` | false positive | named in `modules/`: standoff > standoff_from_reach (`battle_loop.py`, `config.py`) |
| `modules/mass_battle/hierarchy/units.py:169` | `_effective_reach` | dead: delete | one test caller (`test_reach_weapon_class.py:165-166`); facing-gated reach is now `geometry._reach_body_overlap` (reach extends along the heading only); batch D2 |
| `modules/mass_battle/hierarchy/units.py:187` | `_reach_throttle` | dead: delete | no caller anywhere; the directional reach body (`geometry.reach_reaches`, called at `core/contact.py:457`) replaced the TOI throttle; batch D1 |
| `modules/mass_battle/hierarchy/units.py:202` | `_pair_toi_scale` | false positive | named in `modules/`: resolve_toi_and_commit > _pair_toi_scale (`battle_loop.py`, `config.py`) |
| `modules/mass_battle/hierarchy/units.py:2400` | `_ToiCell` | false positive | named in `modules/`: resolve_toi_and_commit > _ToiCell (`battle_loop.py`, `config.py`) |
| `modules/mass_battle/hierarchy/units.py:2423` | `_pairs_within` | false positive | named in `modules/`: separate_all_bodies > _pairs_within (`battle_loop.py`, `massbattle.py`) |
| `modules/mass_battle/hierarchy/units.py:2444` | `_relax_bodies` | false positive | named in `modules/`: separate_all_bodies > _relax_bodies (`battle_loop.py`, `massbattle.py`) |
| `modules/mass_battle/massbattle.py:106` | `_round_half_up` | false positive | named in `modules/`: _morale_start > _round_half_up (`orderofbattle.py`) |
| `modules/mass_battle/massbattle.py:242` | `_retreat_orders` | false positive | named in `modules/`: _weighted_unit > _retreat_orders (`orderofbattle.py`) |
| `modules/mass_battle/massbattle.py:358` | `_oob_unit` | false positive | named in `modules/`: resolve_field > _oob_unit (`__init__.py`, `rngsource.py`) |
| `modules/mass_battle/orchestration.py:250` | `_subunit_depth` | false positive | named in `modules/`: stamina_check > _subunit_depth (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:271` | `rally_check` | dead: delete | reached at every phase boundary and the body is `pass`; already decided by `audits/04_MB_audit.md` F-MB-10 (delete the no-ops and their calls) |
| `modules/mass_battle/orchestration.py:316` | `threadwork_check` | dead: delete | reached at every phase boundary and the body is `pass`; already decided by `audits/04_MB_audit.md` F-MB-10 (delete the no-ops and their calls) |
| `modules/mass_battle/orchestration.py:393` | `_cascade_depth_key` | false positive | named in `modules/`: resolve_engagements_cascading > _cascade_depth_key (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:561` | `_compute_atom_sides` | false positive | named in `modules/`: resolve_engagements > _compute_atom_sides (`battle_loop.py`, `contact.py`) |
| `modules/mass_battle/orchestration.py:604` | `_cell_damage_weights` | false positive | named in `modules/`: resolve_engagements > _cell_damage_weights (`battle_loop.py`, `contact.py`) |
| `modules/mass_battle/orchestration.py:625` | `_accum_cell_damage` | false positive | named in `modules/`: resolve_engagements > _accum_cell_damage (`battle_loop.py`, `contact.py`) |
| `modules/mass_battle/orchestration.py:642` | `_merge_cell_damage` | false positive | named in `modules/`: resolve_engagements_cascading > _merge_cell_damage (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:654` | `_expire_charger_latches` | false positive | named in `modules/`: resolve_engagements_cascading > _expire_charger_latches (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:678` | `_compute_front_fixers` | false positive | named in `modules/`: resolve_engagements > _compute_front_fixers (`battle_loop.py`, `contact.py`) |
| `modules/mass_battle/orchestration.py:1560` | `_volley_density_mult` | false positive | named in `modules/`: volley_phase > _volley_density_mult (`armies.py`, `battle_loop.py`) |
| `modules/mass_battle/orchestration.py:1699` | `_cell_snapshot` | false positive | named in `modules/`: _unit_snapshot > _subunit_snapshot > _cell_snapshot (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:1709` | `_subunit_snapshot` | false positive | named in `modules/`: _unit_snapshot > _subunit_snapshot (`battle_loop.py`) |
| `modules/mass_battle/orchestration.py:2169` | `freed_attacker_damage` | false positive | named in `modules/`: run_multi_unit_battle > freed_attacker_damage (`battle_loop.py`, `units.py`) |
| `modules/mass_battle/orderofbattle.py:142` | `_spec_for` | false positive | named in `modules/`: build_unit > _spec_for (`armies.py`, `massbattle.py`) |
| `modules/mass_battle/orderofbattle.py:172` | `_rows_of` | false positive | named in `modules/`: _place > _rows_of (`armies.py`) |
| `modules/mass_battle/percell.py:107` | `_apply_with_spill` | false positive | named in `modules/`: distribute_casualties > _apply_with_spill (`units.py`, `orchestration.py`) |
| `modules/mass_battle/percell.py:195` | `_erode_cell_morale_from_damage` | false positive | named in `modules/`: distribute_casualties > _apply_with_spill > _erode_cell_morale_from_damage (`units.py`, `orchestration.py`) |
| `modules/mass_battle/perimeter.py:31` | `TargetPoint` | dead: delete | test-only (`tests/valoria/test_perimeter_geometry.py`); the wiring was left "Jordan-gated" on 2026-07-23 and never ruled; the face an attack lands on is already read by `orchestration._compute_atom_sides` (`:746`, `:1403`), so an alignment signal would be a second reading of one quantity; `perimeter_faces` (the one function `units._envelop_goal` calls) stays; batch D2 |
| `modules/mass_battle/perimeter.py:46` | `_convex_hull` | false positive | named in `modules/`: perimeter_faces > _convex_hull (`units.py`) |
| `modules/mass_battle/perimeter.py:104` | `_vertex_interior_angle` | dead: delete | test-only (`tests/valoria/test_perimeter_geometry.py`); the wiring was left "Jordan-gated" on 2026-07-23 and never ruled; the face an attack lands on is already read by `orchestration._compute_atom_sides` (`:746`, `:1403`), so an alignment signal would be a second reading of one quantity; `perimeter_faces` (the one function `units._envelop_goal` calls) stays; batch D2 |
| `modules/mass_battle/perimeter.py:114` | `target_points` | dead: delete | test-only (`tests/valoria/test_perimeter_geometry.py`); the wiring was left "Jordan-gated" on 2026-07-23 and never ruled; the face an attack lands on is already read by `orchestration._compute_atom_sides` (`:746`, `:1403`), so an alignment signal would be a second reading of one quantity; `perimeter_faces` (the one function `units._envelop_goal` calls) stays; batch D2 |
| `modules/mass_battle/perimeter.py:151` | `nearest_target` | dead: delete | test-only (`tests/valoria/test_perimeter_geometry.py`); the wiring was left "Jordan-gated" on 2026-07-23 and never ruled; the face an attack lands on is already read by `orchestration._compute_atom_sides` (`:746`, `:1403`), so an alignment signal would be a second reading of one quantity; `perimeter_faces` (the one function `units._envelop_goal` calls) stays; batch D2 |
| `modules/mass_battle/perimeter.py:162` | `approach_alignment` | dead: delete | test-only (`tests/valoria/test_perimeter_geometry.py`); the wiring was left "Jordan-gated" on 2026-07-23 and never ruled; the face an attack lands on is already read by `orchestration._compute_atom_sides` (`:746`, `:1403`), so an alignment signal would be a second reading of one quantity; `perimeter_faces` (the one function `units._envelop_goal` calls) stays; batch D2 |
| `modules/mass_battle/resolution.py:164` | `_depth_prep` | false positive | named in `modules/`: _wall_prep > _depth_prep (`orchestration.py`) |
| `modules/mass_battle/terrain.py:77` | `_point_in_polygon` | false positive | named in `modules/`: terrain_row_for_territory > _point_in_polygon (`massbattle.py`) |
| `modules/mass_battle/terrain.py:96` | `_polygon_area` | false positive | named in `modules/`: terrain_row_for_territory > _polygon_area (`massbattle.py`) |
| `modules/mass_battle/terrain.py:196` | `_orient` | false positive | named in `modules/`: river_crossed > _orient (`massbattle.py`) |
| `modules/mass_battle/terrain.py:202` | `_on_segment` | false positive | named in `modules/`: river_crossed > _on_segment (`massbattle.py`) |
| `modules/mass_battle/troop_types/recruitment.py:72` | `training_site_for` | false positive | named in `modules/`: recruit_limit > training_site_for (`armyrecord.py`, `presets.py`) |
| `modules/mass_battle/troop_types/registry.py:147` | `support_ranks_for` | false positive | called at `registry.py:156` under `MB_SUPPORT_RANK_CAP`; `04_MB_unit_loadout_and_weapon_in_hand_B.md` proposes its removal |
| `systems/characters/sim/conviction.py:120` | `ConvictionState` | false positive | retained oracle: reached by `systems/fieldwork/sim/knots.py` (late import) and `engine/tests/test_knots_ed912.py`; kept by ED-IN-0283 (RULED) and `audits/02_CHAR_audit.md` §6 row 27 |
| `systems/characters/sim/conviction.py:161` | `ConvictionThresholdState` | false positive | retained oracle: reached by `systems/fieldwork/sim/knots.py` (late import) and `engine/tests/test_knots_ed912.py`; kept by ED-IN-0283 (RULED) and `audits/02_CHAR_audit.md` §6 row 27 |
| `systems/characters/sim/conviction.py:245` | `check_conviction_threshold` | false positive | retained oracle: reached by `systems/fieldwork/sim/knots.py` (late import) and `engine/tests/test_knots_ed912.py`; kept by ED-IN-0283 (RULED) and `audits/02_CHAR_audit.md` §6 row 27 |
| `systems/characters/sim/conviction.py:268` | `mark_belief_revision_pending` | dead: delete | no caller; docstring names `beliefs.revise_belief`, a module that does not exist; the field it writes (`pending_belief_revisions`, `:130`) has no reader but its own (de)serialiser; batch D1 |
| `systems/combat/combat_engine_v1/capabilities.py:23` | `_affords_point` | mislabelled: correct | live (workbench `catalogue.py` imports the file); its docstring names `systems.py`, which is `modules/combat/combat_systems.py`; correction C-1 |
| `systems/combat/combat_engine_v1/capabilities.py:74` | `capability_table` | false positive | `__main__`: `__main__` > markdown_table > capability_table |
| `systems/combat/combat_engine_v1/capabilities.py:80` | `markdown_table` | false positive | `__main__`: `__main__` > markdown_table |
| `systems/combat/combat_engine_v1/state_graph.py:131` | `injection_markdown` | false positive | `__main__`: `__main__` > injection_markdown |
| `systems/combat/combat_engine_v1/state_graph.py:143` | `reachable_from` | false positive | `__main__`: `__main__` > reachable_from |
| `systems/combat/combat_engine_v1/state_graph.py:155` | `fired_states_from_events` | false positive | `__main__`: `__main__` > fired_states_from_events |
| `systems/combat/combat_engine_v1/state_graph.py:187` | `separation_reasons_from_events` | false positive | `__main__`: `__main__` > separation_reasons_from_events |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:71` | `_duel` | false positive | `__main__`: `__main__` > tier_table > _duel |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:118` | `strike_profile` | false positive | `__main__`: `__main__` > strike_profile |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:165` | `tier_table` | false positive | `__main__`: `__main__` > tier_table |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:206` | `reference_table` | false positive | `__main__`: `__main__` > write_reference > reference_table |
| `systems/combat/combat_engine_v1/workbench/armour_participation.py:239` | `write_reference` | false positive | `__main__`: `__main__` > write_reference |
| `systems/combat/combat_engine_v1/workbench/balance.py:84` | `weapon_matchup_table` | false positive | `__main__`: `__main__` > weapon_matchup_table |
| `systems/combat/combat_engine_v1/workbench/balance.py:94` | `attribute_parity_table` | false positive | `__main__`: `__main__` > attribute_parity_table |
| `systems/combat/combat_engine_v1/workbench/balance.py:106` | `tradition_field_table` | false positive | `__main__`: `__main__` > tradition_field_table |
| `systems/combat/combat_engine_v1/workbench/balance.py:121` | `tradition_context_matrix` | false positive | `__main__`: `__main__` > tradition_context_matrix |
| `systems/combat/combat_engine_v1/workbench/balance.py:143` | `_md_context` | false positive | `__main__`: `__main__` > _md_context |
| `systems/combat/combat_engine_v1/workbench/balance.py:155` | `weapon_armour_matrix` | false positive | `__main__`: `__main__` > weapon_armour_matrix |
| `systems/combat/combat_engine_v1/workbench/balance.py:179` | `_md_weapon_armour` | false positive | `__main__`: `__main__` > _md_weapon_armour |
| `systems/combat/combat_engine_v1/workbench/balance.py:193` | `_md_weapon` | false positive | `__main__`: `__main__` > _md_weapon |
| `systems/combat/combat_engine_v1/workbench/balance.py:200` | `_md_attr` | false positive | `__main__`: `__main__` > _md_attr |
| `systems/combat/combat_engine_v1/workbench/balance.py:207` | `_md_trad` | false positive | `__main__`: `__main__` > _md_trad |
| `systems/combat/combat_engine_v1/workbench/build_levers.py:85` | `_hdr` | false positive | `__main__`: `__main__` > mirror > _hdr |
| `systems/combat/combat_engine_v1/workbench/build_levers.py:186` | `archetypes` | false positive | runs at import: import > archetypes |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:44` | `teaching_tradition` | false positive | `__main__`: `__main__` > _job > run_cell > teaching_tradition |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:62` | `cell_seed` | false positive | `__main__`: `__main__` > _job > run_cell > cell_seed |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:66` | `run_cell` | false positive | `__main__`: `__main__` > _job > run_cell |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:180` | `newcombe` | dead: delete | no caller in the file, tree, tests or tools (grep -w); batch D1 |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:186` | `wilson_wins` | false positive | `__main__`: `__main__` > _job > summarize > wilson_wins |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:213` | `_job` | false positive | `__main__`: `__main__` > _job |
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py:222` | `analyze` | false positive | `__main__`: `__main__` > analyze |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:56` | `_fighter` | false positive | `__main__`: `__main__` > values > _fighter |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:60` | `_safe` | false positive | `__main__`: `__main__` > values > _safe |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:164` | `_groups` | false positive | `__main__`: `__main__` > mechanics > _groups |
| `systems/combat/combat_engine_v1/workbench/catalogue.py:190` | `coupling_matrix` | false positive | `__main__`: `__main__` > coupling_matrix |
| `systems/combat/combat_engine_v1/workbench/commentary.py:27` | `_commit_band` | false positive | `__main__`: `__main__` > commentate > _beat > _commit_band |
| `systems/combat/combat_engine_v1/workbench/commentary.py:42` | `_who` | false positive | `__main__`: `__main__` > commentate > _who |
| `systems/combat/combat_engine_v1/workbench/commentary.py:115` | `_beat` | false positive | `__main__`: `__main__` > commentate > _beat |
| `systems/combat/combat_engine_v1/workbench/commentary.py:177` | `render_text` | false positive | `__main__`: `__main__` > render_text |
| `systems/combat/combat_engine_v1/workbench/narrate.py:17` | `_pct` | false positive | `__main__`: `__main__` > render > _pct |
| `systems/combat/combat_engine_v1/workbench/narrate.py:21` | `_dist` | false positive | `__main__`: `__main__` > render > _dist |
| `systems/combat/combat_engine_v1/workbench/narrate.py:26` | `_sig` | false positive | `__main__`: `__main__` > render > _sig |
| `systems/combat/combat_engine_v1/workbench/probabilities.py:83` | `_beta_pdf` | false positive | named in `systems/`: beta_band_probs > _beta_pdf (`commentary.py`, `narrate.py`) |
| `systems/combat/combat_engine_v1/workbench/server.py:32` | `_make_fighter` | false positive | `__main__`: main > Handler > do_trace > _make_fighter |
| `systems/combat/combat_engine_v1/workbench/server.py:65` | `do_montecarlo` | false positive | `__main__`: `__main__` > main > Handler > do_montecarlo |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:70` | `zero_caller_functions` | false positive | `__main__`: `__main__` > report > zero_caller_functions |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:177` | `_docstring_nodes` | false positive | runs at import: import > _read_sites > _docstring_nodes |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:187` | `_read_sites` | false positive | runs at import: import > _read_sites |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:207` | `exported_keys` | false positive | `__main__`: `__main__` > report > exported_keys |
| `systems/combat/combat_engine_v1/workbench/structure_scan.py:214` | `dead_exported_keys` | false positive | `__main__`: `__main__` > report > dead_exported_keys |
| `systems/fieldwork/sim/knots.py:146` | `KnotState` | false positive | retained oracle: reached from `form_knot`/`sustain_knot` and `engine/tests/test_knots_ed912.py`; kept unplugged by ED-IN-0283 and `audits/08_FI_audit.md` R-14 |
| `systems/fieldwork/sim/knots.py:168` | `_count_knots_for_actor` | false positive | retained oracle: reached from `form_knot`/`sustain_knot` and `engine/tests/test_knots_ed912.py`; kept unplugged by ED-IN-0283 and `audits/08_FI_audit.md` R-14 |
| `systems/fieldwork/sim/knots.py:384` | `get_knot` | dead: delete | no caller, no test; store accessors of an unplugged oracle; batch D1 |
| `systems/fieldwork/sim/knots.py:388` | `get_active_knots` | dead: delete | no caller, no test; store accessors of an unplugged oracle; batch D1 |
| `systems/fieldwork/sim/knots.py:392` | `reset_knots` | false positive | retained oracle: reached from `form_knot`/`sustain_knot` and `engine/tests/test_knots_ed912.py`; kept unplugged by ED-IN-0283 and `audits/08_FI_audit.md` R-14 |
| `systems/mass_battle/sim/altonian_reinforcements.py:20` | `invoke_altonian_reinforcements` | dead: delete | raises NotImplementedError, imported by nothing; already decided by `audits/04_MB_audit.md` F-MB-10 (delete with FORK row) |
| `systems/mass_battle/sim/bat.py:657` | `_cfg_mod` | false positive | `__main__`: `__main__` > main > compute > _cfg_mod |
| `systems/mass_battle/sim/bat.py:662` | `_mode_key` | false positive | `__main__`: `__main__` > main > compute > _mode_key |
| `systems/mass_battle/sim/lanchester_signature.py:86` | `_sweep` | false positive | `__main__`: `__main__` > run > check_linear > _sweep |
| `systems/mass_battle/sim/lanchester_signature.py:106` | `check_linear` | false positive | `__main__`: `__main__` > run > check_linear |
| `systems/mass_battle/sim/lanchester_signature.py:141` | `check_no_annihilation` | false positive | `__main__`: `__main__` > run > check_no_annihilation |
| `systems/mass_battle/sim/lanchester_signature.py:248` | `_trajectory` | false positive | `__main__`: `__main__` > run > check_law_exponents > _trajectory |
| `systems/mass_battle/sim/lanchester_signature.py:319` | `_new_diag` | false positive | `__main__`: `__main__` > run > check_law_exponents > _new_diag |
| `systems/mass_battle/sim/lanchester_signature.py:323` | `_best_exponent` | false positive | `__main__`: `__main__` > run > check_law_exponents > _best_exponent |
| `systems/mass_battle/sim/lanchester_signature.py:348` | `check_law_exponents` | false positive | `__main__`: `__main__` > run > check_law_exponents |
| `systems/mass_battle/sim/stress.py:79` | `_layout` | false positive | `__main__`: `__main__` > main > fight_one > _layout |
| `systems/mass_battle/sim/stress.py:84` | `_prep` | false positive | `__main__`: main > fight_one > _build_side > _prep |
| `systems/mass_battle/sim/stress.py:94` | `_depth` | false positive | `__main__`: main > fight_one > _build_side > _depth |
| `systems/mass_battle/sim/stress.py:106` | `_place_line` | false positive | `__main__`: main > fight_one > _build_side > _place_line |
| `systems/mass_battle/sim/stress.py:162` | `_penetration` | false positive | `__main__`: main > fight_one > analyse > _penetration |
| `systems/mass_battle/sim/stress.py:168` | `_nodes` | false positive | `__main__`: main > fight_one > analyse > _nodes |
| `systems/mass_battle/sim/stress.py:182` | `analyse` | false positive | `__main__`: `__main__` > main > fight_one > analyse |
| `systems/mass_battle/sim/stress.py:279` | `fight_one` | false positive | `__main__`: `__main__` > main > fight_one |
| `systems/mass_battle/sim/validators.py:71` | `_line` | false positive | runs at import: import > v_reform > _defender > _line |
| `systems/mass_battle/sim/validators.py:83` | `_defender` | false positive | runs at import: import > v_reform > _defender |
| `systems/mass_battle/sim/validators.py:94` | `_attacker` | false positive | runs at import: import > v_shock > _attacker_retained > _attacker |
| `systems/mass_battle/sim/validators.py:106` | `_attacker_retained` | false positive | runs at import: import > v_shock > _attacker_retained |
| `systems/mass_battle/sim/validators.py:124` | `v_cannae` | false positive | runs at import: import > v_cannae |
| `systems/mass_battle/sim/validators.py:142` | `v_fixing` | false positive | runs at import: import > v_fixing |
| `systems/mass_battle/sim/validators.py:162` | `v_shock` | false positive | runs at import: import > v_shock |
| `systems/mass_battle/sim/validators.py:181` | `v_brace` | false positive | runs at import: import > v_brace |
| `systems/mass_battle/sim/validators.py:200` | `_attacker_envelop` | false positive | runs at import: import > v_envelop > _envelop_reach > _attacker_envelop |
| `systems/mass_battle/sim/validators.py:218` | `_set_movement_path` | false positive | runs at import: import > v_sweep > _sweep_disp > _set_movement_path |
| `systems/mass_battle/sim/validators.py:236` | `_envelop_reach` | false positive | runs at import: import > v_envelop > _envelop_reach |
| `systems/mass_battle/sim/validators.py:254` | `v_envelop` | false positive | runs at import: import > v_envelop |
| `systems/mass_battle/sim/validators.py:277` | `v_reform` | false positive | runs at import: import > v_reform |
| `systems/mass_battle/sim/validators.py:320` | `_archer_pair` | false positive | runs at import: import > v_archer > _archer_far_loss > _archer_pair |
| `systems/mass_battle/sim/validators.py:337` | `_archer_far_loss` | false positive | runs at import: import > v_archer > _archer_far_loss |
| `systems/mass_battle/sim/validators.py:355` | `v_archer` | false positive | runs at import: import > v_archer |
| `systems/mass_battle/sim/validators.py:374` | `_attacker_sweep` | false positive | runs at import: import > v_sweep > _sweep_disp > _attacker_sweep |
| `systems/mass_battle/sim/validators.py:382` | `_sweep_disp` | false positive | runs at import: import > v_sweep > _sweep_disp |
| `systems/mass_battle/sim/validators.py:400` | `v_sweep` | false positive | runs at import: import > v_sweep |
| `systems/mass_battle/sim/validators.py:423` | `run_all` | false positive | `__main__`: `__main__` > run_all |
| `systems/mass_battle/sim/walkthrough.py:42` | `_oob` | false positive | `__main__`: `__main__` > main > fight > _oob |
| `systems/mass_battle/sim/walkthrough.py:50` | `_subs` | false positive | `__main__`: `__main__` > main > fight > _subs |
| `systems/mass_battle/sim/walkthrough.py:60` | `_snap_unit` | false positive | `__main__`: main > fight > _Recorder > _snap_unit |
| `systems/mass_battle/sim/walkthrough.py:114` | `_collapse` | false positive | `__main__`: `__main__` > main > fight > _collapse |
| `systems/mass_battle/sim/walkthrough.py:185` | `_summary` | false positive | `__main__`: `__main__` > main > build_page > _summary |
| `systems/mass_battle/sim/walkthrough.py:195` | `build_page` | false positive | `__main__`: `__main__` > main > build_page |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:68` | `_multi_subunit_row_ids` | false positive | `__main__`: `__main__` > main > _multi_subunit_row_ids |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:82` | `_worker` | false positive | `__main__`: `__main__` > main > _worker |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:123` | `_run_one` | false positive | `__main__`: `__main__` > main > _run_one |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:135` | `_row_passes_win_band` | false positive | `__main__`: `__main__` > main > _print_table > _row_passes_win_band |
| `systems/mass_battle/sim/workbench/rout_cascade_sweep.py:141` | `_print_table` | false positive | `__main__`: `__main__` > main > _print_table |
| `systems/mass_battle/sim/workbench/server.py:102` | `do_mode` | false positive | `__main__`: `__main__` > main > do_mode |
| `systems/mass_battle/sim/workbench/server.py:117` | `do_roster_options` | false positive | `__main__`: `__main__` > main > Handler > do_roster_options |
| `systems/mass_battle/sim/workbench/trace.py:33` | `_anchor_for` | false positive | `__main__`: `__main__` > _anchor_for |
| `systems/social_contest/sim/contest/_kernel_tests.py:18` | `ck` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:125` | `evrate` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:149` | `prate` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:161` | `_bands` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:190` | `_commfrac` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:206` | `_adv` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:221` | `_adv_ev` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:233` | `_bth` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:240` | `_barred_out` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:249` | `_awin` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:269` | `_shapes` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:282` | `_bt` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:307` | `_same` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:327` | `_reb` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:453` | `_d3` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:478` | `_d3_paired` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:504` | `_rawres` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:612` | `_rejects_opt_in` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:683` | `_bc_rejects` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:750` | `_golden_trace` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:878` | `_raises` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1363` | `_cr4_choice_adv` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1415` | `_cr4_church_tribunal_adv` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1503` | `_obscuring_probe` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1544` | `_face_after_failed_obscuring` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1647` | `_armature_track` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/_kernel_tests.py:1689` | `_same_off` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/agon_harness.py:142` | `HarnessState` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:148` | `_raw_input` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:160` | `ask_choice` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:191` | `setup_contest` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:219` | `print_setup_screen` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:249` | `_band_name` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:253` | `print_appraise` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:281` | `print_bars` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:313` | `human_turn` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:370` | `ai_turn` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:379` | `print_move_result` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:401` | `_describe_verdict` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/agon_harness.py:419` | `run_contest_interactive` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` and `agon_harness` `__main__` |
| `systems/social_contest/sim/contest/appraise.py:110` | `_dominant_axis` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/appraise.py:119` | `_strength_band` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/degree_extension.py:60` | `PoolDesaturation` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/degree_extension.py:90` | `owner_overwhelming_margin` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/dictionaries.py:583` | `_build_proceedings_table` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/faction.py:37` | `_adj` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/faction.py:41` | `_one_vote` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:70` | `disputation_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:77` | `appeal_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:115` | `_default_panel` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:121` | `fused_arbiter_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:127` | `deliberative_body_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:137` | `scholastic_disputation_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:166` | `public_oration_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:181` | `inquisition_hearing_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:200` | `excommunication_court_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:219` | `imperial_petition_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:241` | `secret_council_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:258` | `memorial_remonstrance_venue` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:282` | `public_oration_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:285` | `inquisition_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:291` | `excommunication_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:298` | `imperial_petition_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:304` | `secret_council_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:311` | `memorial_remonstrance_mode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:342` | `NegotiationMode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:351` | `CeremonialMode` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/modes.py:521` | `_use_tracker` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/narrative.py:103` | `_per_exchange` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/policy.py:5` | `_low` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/policy.py:25` | `fallback_ladder` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/policy.py:32` | `off_ground_chancer` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/policy.py:45` | `counterpuncher` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/wrapper.py:91` | `_as_contestant` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/social_contest/sim/contest/wrapper.py:220` | `_stub` | dead: delete | the kernel retires whole, after the `hearing` entry: `proposals/05_SC_sc05_kernel_disposition_B.md` (ED-SC-0033 cl. 2); today reached by `engine/tests/test_contest_kernel.py` |
| `systems/threadwork/sim/co_movement.py:63` | `CoMovementCard` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/co_movement.py:84` | `_shuffle_deck` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/co_movement.py:94` | `draw_comovement_card` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/co_movement.py:137` | `reset_deck` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/coherence.py:154` | `_displacement_band` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/coherence.py:166` | `CoherenceLogEntry` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/coherence.py:280` | `CoherenceFailureResult` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/coherence.py:411` | `check_coherence_failure_transition` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/collective.py:47` | `CollectiveResult` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/collective.py:62` | `_helper_contribution` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/collective.py:71` | `attempt_collective_operation` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/operations.py:225` | `_compute_degree` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:375` | `attempt_weaving` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:388` | `attempt_pulling` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:397` | `attempt_past_pulling` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:417` | `attempt_locking` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:434` | `attempt_dissolution` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:456` | `MendingPrice` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/operations.py:592` | `_mend_own_configuration` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` |
| `systems/threadwork/sim/opposing.py:79` | `opposing_engagement_modifier` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/opposing.py:87` | `_degree_label` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/opposing.py:102` | `resolve_opposing_operations` | broken: wire | the oracle has no season caller (module graph: reached by tests only); the wire is `proposals/09_WR_threadwork_module.md` (move to `modules/threadwork/`, entry `threadwork.work`) with `09_WR_B_threadwork_session_and_practitioner.md` — ⚠ neither gives this file an entry or a verb (W-3) |
| `systems/threadwork/sim/threadcut.py:72` | `ThreadcutState` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/threadcut.py:92` | `mark_threadcut` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/threadcut.py:100` | `is_threadcut` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/threadcut.py:105` | `perception_band` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/threadcut.py:114` | `resolve_threadcut_interaction` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
| `systems/threadwork/sim/threadcut.py:198` | `reset_threadcut` | dead: delete | file has no importer and no test (module graph: 0 importers); its module-level store is deleted by `proposals/09_WR_threadwork_module.md` edit 2 and nothing carries the state (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3: "no carrier"); batch D3 |
