# CENSUS C1B · deletions: three batches, ordered by risk

## Status: PROPOSED

Carries `audits/17_CENSUS_C1B.md` §3.1 (the 21 dead rows this lane newly finds). The 80 dead rows that
other documents already carry are not restated: the SC-05 kernel (75 rows) is
`05_SC_sc05_kernel_disposition_B.md`; `altonian_reinforcements.py`, `rally_check`, `threadwork_check`
are `audits/04_MB_audit.md` F-MB-10; `dr_vs_piercing` and `with_keyword` go with `ARMOURY` and `ARSENAL`
under `04_MB_unit_loadout_and_weapon_in_hand.md`.

## What it changes in `engine/season/` at runtime

**Nothing.** Every symbol below is unreached by the season loop: D1 has no caller at all, D2 has test
callers only, D3 has no importer. Content hash EQUAL is the gate, not an expectation to argue.

## Batch D1 · no caller anywhere (lowest risk; one commit, no test changes)

| file | delete | lines | evidence (whole-word grep over `engine modules systems tools tests skills`) |
|---|---|---|---|
| `systems/combat/combat_engine_v1/workbench/calibrate_generics.py` | `newcombe` | `:180-183` | the def only |
| `modules/mass_battle/hierarchy/units.py` | `_reach_throttle` | `:187-199` | the def only; not in `__all__` |
| `systems/characters/sim/conviction.py` | `mark_belief_revision_pending` | `:268-275` | the def only |
| same | the field `ConvictionState.pending_belief_revisions` and its two (de)serialiser lines | `:130`, `:142`, `:154` | written by the function above and by nothing else; read by nothing but `to_dict`/`from_dict` |
| same | the `[ASSUMPTION: cycle resolution — beliefs.revise_belief calls into …]` paragraph of the module docstring | `:22` and the lines it runs to | names a module, `beliefs`, that does not exist |
| `systems/fieldwork/sim/knots.py` | `get_knot`, `get_active_knots` | `:384-389` | the defs only; `engine/tests/test_knots_ed912.py` uses neither |

ED-IN-0283 (RULED) keeps `systems/characters/` and `systems/fieldwork/` as the homes of those systems.
This batch removes three uncalled functions and one unread field from files that stay; it deletes no
file and no folder, so the ruling is not touched. `from_dict` must go on accepting a stored dict that
still carries the key (read with `d.get` and ignored), so an old saved state does not fail to load.

No `FORK:` row: no file is deleted. Covering tests to run: `engine/tests/test_knots_ed912.py`,
`tests/valoria/test_flow_skeletons.py` (if an archived anchor names one of the four symbols, add the
`(file, symbol)` pair to its `RETIRED_SYMBOLS`, the tree's own mechanism for a deleted symbol).

## Batch D2 · test-only, and superseded by what the resolver does run (one commit, with its test edits)

### D2a · `modules/mass_battle/hierarchy/units.py::_effective_reach` and the flag only it reads

| edit | where |
|---|---|
| delete `_effective_reach` | `units.py:169-184` |
| delete `MB_REACH_FACING_GATE` and the comment above it | `units.py:163-166`, and its name in `__all__` (`:119`) |
| delete the key `'MB_REACH_FACING_GATE': '1'` | `tools/ci_golden_modes_check.py:90` |
| reword the comment "(see _effective_reach)" to "(see `geometry.reach_reaches`)" | `units.py:137` |
| delete `test_facing_away_gets_no_reach` | `tests/valoria/test_reach_weapon_class.py:160-171` |

Why it is dead and not broken: the rule it states (a weapon's reach threatens only what is in front)
is the rule `geometry._reach_body_overlap` implements (the reach body is the cell's circle swept along
its own heading; `test_body_primitive.py::test_front_reach_engages_only_in_front` holds it), and that
is what contact calls (`core/contact.py:457`, `reach_reaches`). Wiring `_effective_reach` would give the
facing rule two owners.

⚠ **The flag is the risk in this batch.** `MB_REACH_FACING_GATE` is read by `_effective_reach` and by
nothing else (grep), yet `tools/ci_golden_modes_check.py` pins it as a canonical mode: CI pins a switch
that switches nothing. The pin and the flag must leave in the same commit, or the golden-modes check
(which compares each pin with a source-level `environ.get` default) goes red.

### D2b · `modules/mass_battle/perimeter.py`: the target-point half

| edit | where |
|---|---|
| delete `TargetPoint`, `_vertex_interior_angle`, `target_points`, `nearest_target`, `approach_alignment`, `SHARP_TIP_DEG` | `perimeter.py:25`, `:31-35`, `:104-111`, `:114-173` |
| cut the module docstring to what remains: faces from the convex hull of the cell centres, with outward normals, read by `units._envelop_goal` | `perimeter.py:1-19` |
| keep `Face`, `_convex_hull`, `_centroid`, `_unit`, `perimeter_faces` | — |
| `tests/valoria/test_perimeter_geometry.py`: delete `test_nearest_target_picks_the_faced_side` (`:63`), `test_approach_alignment_is_one_when_square_on` (`:78`); in `test_line_is_a_four_face_rectangle` (`:25`), `test_arrowhead_has_a_sharp_or_flagged_tip_geometry` (`:51`), `test_degenerate_footprint_still_returns_a_target` (`:93`) and `test_determinism` (`:100`) keep the `perimeter_faces` assertions and drop the `target_points` ones (the determinism test compares `perimeter_faces(cells)` with `perimeter_faces(reversed(cells))`) | — |

Decided on the ladder, because the file's own head calls the wiring "a separate, Jordan-gated step":
step 2, no ruling, plan position or suite proposal has carried the gate since 2026-07-23, and the MB
audit measured the file at 0% reached; step 5, the face a blow lands on is already read once, by
`orchestration._compute_atom_sides` (one F/B/L/R face per contacting enemy body, feeding the multi-side
shock), so a continuous alignment term beside it would be two ladders for one quantity (§0.06 S).
**If Jordan wants approach alignment to matter, the place is a term inside `_compute_atom_sides`'s
reading, not a second geometry.** What is lost: corner target points and the sharp-tip flag, which no
code ever read.

## Batch D3 · two oracle files nothing imports (highest risk here: registry rows move)

Delete `systems/threadwork/sim/threadcut.py` (200 lines) and `systems/threadwork/sim/co_movement.py`
(141 lines).

| edit | where |
|---|---|
| `git rm` the two files | — |
| drop the two lines naming them | `systems/threadwork/sim/__init__.py:11`, `:13` |
| `co_movement` and `threadcut_beings`: `sim_module: null` (the file's own form for "no module", `tools/mechanics_index_gen.py:233`); nothing else in the rows changes | `registers/mechanics_index.yaml:467`, `:485` |
| drop `'systems/threadwork/sim/co_movement.py'` from the live-file list and the pair `('systems/threadwork/sim/co_movement.py', 'apply_ms_delta')` | `tests/valoria/test_flow_skeletons.py:351`, `:427` |
| re-derive, never hand-edit: `python tools/export_sim_params.py --build` (both files' constants are in `engine/engine_params/sim_params.json`, 6 lines, and `value_pointer_links.json`, 5) | exporter output |
| reword the two remaining pointers to `co_movement.py` (text in `17_CENSUS_C1B_03_corrections.md` C-5) | `engine/season/hole_register.yaml:6110` (H-326), `systems/threadwork/sim/operations.py:212` |
| two `FORK:` rows (below) | `references/restructure_ledger.md` |

`FORK:` row text (the sha is the last commit that holds the files; `b8039982` holds them unchanged
today, so use it or the parent of the deleting commit):

```
| `systems/threadwork/sim/threadcut.py` | `FORK:b8039982` | FORKED (census C1B, D3: an [ASSUMPTION]-graded draft of threadcut beings; no importer, no test, a module-level registry with no carrier in the season World; the directory's move to `modules/threadwork/` deletes module stores, and every function here reads or writes one. Design text: `threadwork_v30.md` Part 6, quarantined) |
| `systems/threadwork/sim/co_movement.py` | `FORK:b8039982` | FORKED (census C1B, D3: the co-movement deck; no importer, no test; its one computed output, `ms_delta`, was reported and written nowhere since plan position 27, and its deck is persistent state with no carrier. Design text: `threadwork_v30.md` Part 4, quarantined) |
```

Why delete and not move with the rest of the oracle. `09_WR_threadwork_module.md` edit 2 deletes
"`_practitioner_state`, `_store`, `reset_all` and their siblings in `threadcut.py` and `co_movement.py`".
In `threadcut.py` every function is a read or write of `_threadcut_registry`
(`mark_threadcut`, `is_threadcut`, `reset_threadcut`, and `resolve_threadcut_interaction`, which reads
the flag and writes `rendering_strain`); in `co_movement.py` every function draws from or resets
`_deck_state`. With the stores gone nothing in either file runs, so the move would carry two files of
functions that cannot be called. `proposals/2026-10-07-unplugged-systems-replug.md` §3.3 already reads
both as having no carrier and expects them to stay unplugged. Ladder step 2 (the subject has no carrier
and no consumer) and step 5 (a registered module holds no game state).

**Put to the WR proposal's owner at unification, not to Jordan:** `09_WR_threadwork_module.md` should say
in its edit 2 that the two files are deleted rather than moved, citing this batch. If the WR lane holds
that the played working needs the five perception bands (`threadcut.py:35-42`,
`audits/09_WR_audit_addendum_B.md` names "visibility by the observer's sensitivity (five bands)" as
session content), the bands are a roster row in the session proposal's typed file, not this module.

## Gate (execution artifact)

For each batch, before and after, `PYTHONHASHSEED=0`:

1. `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` and `build_realm(0)`
   run one season: `World.content_hash()` equal (the SC kernel proposal's own gate, reused).
2. D2a: `python tools/ci_golden_modes_check.py` green; the mass-battle goldens under `engine/tests/`
   unchanged (`-m mass_battle` at the close, once).
3. D3: `python tools/export_sim_params.py --check` and `python tools/freshness_gate.py` green;
   `tests/valoria/test_flow_skeletons.py` green.
4. `python -c "import modules.mass_battle.perimeter, modules.mass_battle.hierarchy.units, systems.threadwork.sim"` exits 0.

## Falsifier

A content hash that moves, or a mass-battle golden that moves on D2a: then something read
`MB_REACH_FACING_GATE` or the deleted functions by a route the grep did not see; stop and find it. For
D3, an `ImportError` anywhere in the import probe of `audits/17_CENSUS_C1B.md` §5 run 3, re-run after
the deletion.

## NERS reading

- **N.** Cut from every direction: no caller above (the loop, the harness), none beside (sibling
  modules), none below (no primitive depends on them). Nothing in play changes.
- **R.** Completeness improves by removal: a CI-pinned flag that switches nothing, a "Jordan-gated"
  geometry nobody gated, and two drafts graded `[ASSUMPTION]` stop presenting as mechanics.
- **S.** D2 removes a second statement of the facing rule and a second reading of the struck face.
- **E, last.** About 480 lines of code and 60 of tests out; nothing in.

## Cost class

Edit (D1). Edit with test changes and one CI table row (D2). Small build, cross-lane on `registers/`,
`references/` and the exporter output (D3).
