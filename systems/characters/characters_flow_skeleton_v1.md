# Characters — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/characters/` · **Lane:** `PC` · **Contracts:** `piety_track` (conviction), no
contract entry located for beliefs or companion
**Code roots traced:** `systems/characters/sim/{conviction,beliefs,companion}.py`,
`systems/characters/__init__.py`, `systems/characters/sim/__init__.py`, plus every importer found by
grepping `characters.sim` / `sim.personal.(conviction|beliefs|companion)` across `engine/`, `systems/`,
`tests/`: `engine/autoload/game_state.py`, `engine/mc_v18.py`, `engine/tests/test_pipeline_reach.py`,
`systems/fieldwork/sim/knots.py`, `systems/social_contest/sim/contest_legacy_stub.py`,
`systems/social_contest/sim/contest/__init__.py`, `engine/cross_scale/scene_dispatch.py`,
`systems/social_contest/sim/contest/armature.py`, `references/module_contracts.yaml`
**Traced at:** `654506799c637e83eae33377a7b0974317721b0a`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `conviction.apply_conviction_scar` | `systems/characters/sim/conviction.py:177 apply_conviction_scar` | `systems/fieldwork/sim/knots.py:361 apply_conviction_scar` (late-imported at :349) — see §7 gap 1 |
| `conviction.check_conviction_threshold` | `systems/characters/sim/conviction.py:244 check_conviction_threshold` | — (see §7 gap 5) |
| `conviction.mark_belief_revision_pending` | `systems/characters/sim/conviction.py:267 mark_belief_revision_pending` | `systems/characters/sim/beliefs.py:177 mark_belief_revision_pending`, `systems/characters/sim/beliefs.py:228 mark_belief_revision_pending` (both intra-subsystem, late-imported) |
| `conviction.get_state` | `systems/characters/sim/conviction.py:277 get_state` | — |
| `conviction.reset_all` | `systems/characters/sim/conviction.py:281 reset_all` | — |
| `conviction.ConvictionState.to_dict` | `systems/characters/sim/conviction.py:135 to_dict` | `engine/autoload/game_state.py:355 serialize_world` (duck-typed via `hasattr`) |
| `conviction.ConvictionState.from_dict` | `systems/characters/sim/conviction.py:146 from_dict` | `engine/autoload/game_state.py:425-426 restore_world` — see §7 gap 4 |
| `beliefs.add_belief` | `systems/characters/sim/beliefs.py:121 add_belief` | — (see §7 gap 2) |
| `beliefs.revise_belief` | `systems/characters/sim/beliefs.py:140 revise_belief` | — (see §7 gap 5) |
| `beliefs.social_success` | `systems/characters/sim/beliefs.py:189 social_success` | `systems/social_contest/sim/contest_legacy_stub.py:242 social_success` (late-imported at :240) — see §7 gap 1 |
| `beliefs.get_active_beliefs` | `systems/characters/sim/beliefs.py:237 get_active_beliefs` | — |
| `beliefs.reset_all` | `systems/characters/sim/beliefs.py:243 reset_all` | — |
| `beliefs.Belief.to_dict` | `systems/characters/sim/beliefs.py:60 to_dict` | `engine/autoload/game_state.py:355-356 serialize_world` (duck-typed via `hasattr`) |
| `beliefs.Belief.from_dict` | `systems/characters/sim/beliefs.py:78 from_dict` | `engine/autoload/game_state.py:425 restore_world` — see §7 gap 4 |
| `companion.run_companion_scene` | `systems/characters/sim/companion.py:28 run_companion_scene` | `engine/tests/test_pipeline_reach.py:788 run_companion_scene` (conformance probe only) — see §7 gap 1 |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `actor` (str) | arg | caller | `systems/characters/sim/conviction.py:177 apply_conviction_scar` |
| `source` (str) | arg | caller | `systems/characters/sim/conviction.py:177 apply_conviction_scar` |
| `magnitude` (int) | arg | caller | `systems/characters/sim/conviction.py:177 apply_conviction_scar` |
| `conviction` (Optional[str]) | arg | caller, must be a member of module's `CONVICTIONS` tuple | `systems/characters/sim/conviction.py:178 apply_conviction_scar` |
| `certainty` (int) | arg (default) | caller | `systems/characters/sim/conviction.py:179 apply_conviction_scar` |
| `season` (int) | arg (default) | caller | `systems/characters/sim/conviction.py:180 apply_conviction_scar` |
| `world` | world-state | caller (optional `World` instance) | `systems/characters/sim/conviction.py:85 _store` |
| `world.convictions` | registry | `engine/autoload/game_state.py:282 convictions` field | `systems/characters/sim/conviction.py:88 _store` |
| `world.beliefs` | registry | `engine/autoload/game_state.py:283 beliefs` field | `systems/characters/sim/beliefs.py:108 _store` |
| `belief_id`, `new_position`, `evidence` | arg | caller | `systems/characters/sim/beliefs.py:140-141 revise_belief` |
| `aligned` (bool), `current_momentum` (int) | arg | caller | `systems/characters/sim/beliefs.py:189-190 social_success` |
| `underlying_convictions` (list) | arg (default) | caller | `systems/characters/sim/beliefs.py:123 add_belief` |
| `scene` | arg | caller (unused by the stub body) | `systems/characters/sim/companion.py:28 run_companion_scene` |
| snapshot dict entries `'convictions'`, `'beliefs'` | world-state (deserialized) | `engine/autoload/game_state.py:425 restore_world` argument | `engine/autoload/game_state.py:425 restore_world`, `engine/autoload/game_state.py:425 restore_world` |

## 3. Flow

**S1. Conviction Scar accumulation** (`apply_conviction_scar`)
- S1 Resolve or create per-actor `ConvictionState` from the store. `systems/characters/sim/conviction.py:170 _get_or_create`
- S1.1 `[branch]` `conviction is None` → return a magnitude-0 no-op `ScarRecord`, no state mutated. `systems/characters/sim/conviction.py:195-199 apply_conviction_scar`
- S1.2 `[branch]` an unknown Conviction name → `descriptors.resolve_conviction` RAISES `ValueError` (it folds the two rename aliases first). Until 2026-08-24 this branch returned a magnitude-0 no-op `ScarRecord` instead, which is how §7 gap 7 stayed invisible. `systems/characters/sim/conviction.py:205 apply_conviction_scar`
- S1.3 `[gate]` Thread-witnessing season cap: if `source` matches a Thread/witness pattern and the actor was already Scarred on this Conviction this season, return the prior state unchanged. `systems/characters/sim/conviction.py:210-219 apply_conviction_scar`
- S1.4 Apply Certainty-based magnitude scaling to the base `magnitude`. `systems/characters/sim/conviction.py:221-223 apply_conviction_scar`
- S1.5 `[write]` Update `state.scars[conviction]` and `state.last_scar_season[conviction]`. `systems/characters/sim/conviction.py:225-227 apply_conviction_scar`
- S1.6 `[branch][write]` Threshold check: add `conviction` to `resonant_active` / `in_crisis` sets if the new total crosses each band. `systems/characters/sim/conviction.py:230-233 apply_conviction_scar`
- S1.7 `[write]` Append a `ScarRecord` to `state.log`; return it. `systems/characters/sim/conviction.py:235-241 apply_conviction_scar`

**S2. Conviction threshold summary** (`check_conviction_threshold`, uncalled — see §7 gap 5)
- S2 Resolve actor state, partition `scars` into destabilised (=1) / shifted (=2) / in-crisis (>=3) bands, return the summary. `systems/characters/sim/conviction.py:253-264 check_conviction_threshold`

**S3. Belief revision** (`revise_belief`, uncalled — see §7 gap 5)
- S3.1 `[branch]` Belief not found for actor → return a rejected `RevisionResult`. `systems/characters/sim/beliefs.py:152-159 revise_belief`
- S3.2 `[write]` Mutate `belief.position`; append an entry to `belief.history`. `systems/characters/sim/beliefs.py:161-167 revise_belief`
- S3.3 `[branch][emit]` If the Belief has `underlying_convictions`, late-import `conviction.mark_belief_revision_pending` and call it (crosses back into S5 below). `systems/characters/sim/beliefs.py:174-177 revise_belief`
- S3.4 Return the `RevisionResult`. `systems/characters/sim/beliefs.py:180-186 revise_belief`

**S4. Belief-driven social success** (`social_success`)
- S4.1 `[branch]` Belief not found for actor → return a rejected `RevisionResult`. `systems/characters/sim/beliefs.py:201-208 social_success`
- S4.2 `[branch]` `aligned=True` → compute a capped Momentum delta, no state mutation, return. `systems/characters/sim/beliefs.py:210-219 social_success`
- S4.3 `[branch][write][emit]` `aligned=False` → increment `belief.revision_pressure`; late-import and call `conviction.mark_belief_revision_pending` (crosses into S5). `systems/characters/sim/beliefs.py:221-228 social_success`
- S4.4 Return the `RevisionResult`. `systems/characters/sim/beliefs.py:229-234 social_success`

**S5. Cross-module notification landing** (`mark_belief_revision_pending`, reached only from S3.3/S4.3)
- S5 Resolve actor state; append `belief_id` to `state.pending_belief_revisions` if not already present. `systems/characters/sim/conviction.py:272-274 mark_belief_revision_pending`

**S6. Companion scene resolution** (`run_companion_scene`)
- S6 `[gate]` Unconditionally calls the single-owner stub primitive and returns a typed `StubResult`; no `scene` argument is read, no state is touched. `systems/characters/sim/companion.py:29-33 run_companion_scene`

**S7. World lifecycle: write direction (live)**
- S7.1 `create_world` builds a fresh `World`; `convictions`/`beliefs` default to empty dicts and are not populated during world-gen. `engine/autoload/game_state.py:256-257 World`, `engine/autoload/game_state.py:304-315 create_world`
- S7.2 `[write]` At the end of every campaign run, `serialize_world` duck-type-calls `.to_dict()` on every value in `world.convictions` / `world.beliefs` (empty in production — see §7 gap 2) into the snapshot dict. `engine/autoload/game_state.py:355-359 serialize_world`
- S7.3 `[emit]` The snapshot becomes `CampaignResult.final_state`. `engine/mc_v18.py:307` (final_state=game_state.serialize_world(world))

**S8. World lifecycle: read direction (test-only — see §7 gap 4)**
- S8.1 `[branch]` If `'convictions'` is present in the snapshot, late-import `ConvictionState` and rebuild `world.convictions` via `from_dict`. `engine/autoload/game_state.py:425-428 restore_world`
- S8.2 `[branch]` If `'beliefs'` is present, late-import `Belief` and rebuild `world.beliefs` via `from_dict`. `engine/autoload/game_state.py:425-428 restore_world`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `ScarRecord` | return value | caller of `apply_conviction_scar` (`systems/fieldwork/sim/knots.py`) | `systems/characters/sim/conviction.py:235-241 apply_conviction_scar` |
| `ConvictionThresholdState` | return value | — (no caller — §7 gap 5) | `systems/characters/sim/conviction.py:257-264 check_conviction_threshold` |
| `RevisionResult` | return value | caller of `revise_belief`/`social_success` (`systems/social_contest/sim/contest_legacy_stub.py` for `social_success`) | `systems/characters/sim/beliefs.py:180-186`, `systems/characters/sim/beliefs.py:229-234` |
| `StubResult` | return value | `engine/tests/test_pipeline_reach.py` conformance probe only | `systems/characters/sim/companion.py:29-33 run_companion_scene` |
| `world.convictions` (dict of `ConvictionState`) | world-state (write) | `engine/autoload/game_state.py` snapshot | `engine/autoload/game_state.py:355-356 serialize_world` |
| `world.beliefs` (dict of list[`Belief`]) | world-state (write) | `engine/autoload/game_state.py` snapshot | `engine/autoload/game_state.py:355-357 serialize_world` |
| `CampaignResult.final_state['convictions'/'beliefs']` | return value | nothing reads these two keys downstream — see §7 gap 2 | `engine/mc_v18.py:315 final_state` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `ConvictionState.scars` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:123`, `systems/characters/sim/conviction.py:208`, `systems/characters/sim/conviction.py:225-226` |
| `ConvictionState.resonant_active` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:125`, `systems/characters/sim/conviction.py:230-231` |
| `ConvictionState.in_crisis` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:127`, `systems/characters/sim/conviction.py:232-233` |
| `ConvictionState.pending_belief_revisions` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:129 pending_belief_revisions`, `systems/characters/sim/conviction.py:273 mark_belief_revision_pending`, `systems/characters/sim/conviction.py:274 mark_belief_revision_pending` |
| `ConvictionState.last_scar_season` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:131`, `systems/characters/sim/conviction.py:215`, `systems/characters/sim/conviction.py:227` |
| `ConvictionState.log` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:133`, `systems/characters/sim/conviction.py:240`, `systems/characters/sim/conviction.py:143 to_dict` |
| `_conviction_state` (module-level fallback dict) | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:82 _store`, `systems/characters/sim/conviction.py:89-90 _store` |
| `Belief.position` | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:55`, `systems/characters/sim/beliefs.py:161-162`, `systems/characters/sim/beliefs.py:216` |
| `Belief.history` | W | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:58`, `systems/characters/sim/beliefs.py:163-167` |
| `Belief.revision_pressure` | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:57`, `systems/characters/sim/beliefs.py:225` |
| `_beliefs_by_actor` (module-level fallback dict) | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:102 _store`, `systems/characters/sim/beliefs.py:109-110 _store` |
| `world.convictions` | RW | `engine/autoload/game_state.py` (field), `systems/characters/sim/conviction.py` (accessor) | `engine/autoload/game_state.py:244`, `systems/characters/sim/conviction.py:85-90 _store` |
| `world.beliefs` | RW | `engine/autoload/game_state.py` (field), `systems/characters/sim/beliefs.py` (accessor) | `engine/autoload/game_state.py:245`, `systems/characters/sim/beliefs.py:105-110 _store` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| in | `fieldwork` (FI) | `systems/fieldwork/sim/knots.py` late-imports and calls `conviction.apply_conviction_scar` from `apply_knot_loss`'s break-consequence branch | `systems/fieldwork/sim/knots.py:349-363 apply_knot_loss` |
| in | `social_contest` (SC) | `systems/social_contest/sim/contest_legacy_stub.py` late-imports and calls `beliefs.social_success` from `run_contest`'s post-contest resolution | `systems/social_contest/sim/contest_legacy_stub.py:239-247 run_contest` |
| down | `engine.autoload` (core) | `game_state.py` imports `ConvictionState`/`Belief` directly to deserialize a campaign snapshot | `engine/autoload/game_state.py:425-432 restore_world` |
| up | `engine.substrate` (core) | `companion.py` imports the single-owner stub primitive | `systems/characters/sim/companion.py:17` (import stubwire) |

## 7. Traced gaps

| Gap | Evidence |
|---|---|
| 1. No production entry point currently exercises the subsystem's core mechanics. `apply_conviction_scar`'s only caller, `knots.apply_knot_loss`, itself has zero production callers (only `engine/tests/test_knots_ed912.py:106`, `engine/tests/test_knots_ed912.py:112`, `engine/tests/test_knots_ed912.py:115`, `engine/tests/test_knots_ed912.py:121`). `social_success`'s only caller, `contest_legacy_stub.run_contest`, has zero callers anywhere in the tree except its own definition and docstrings — production dispatch (`scene_dispatch.py`) was migrated off it. `run_companion_scene` has zero callers anywhere except an OI-17 stub-wiring conformance probe. | `grep -rn "apply_knot_loss(" --include="*.py" .` → only `engine/tests/test_knots_ed912.py`; `grep -rn "run_contest(" --include="*.py"` → only the def at `systems/social_contest/sim/contest_legacy_stub.py:191` and docstring mentions; `engine/cross_scale/scene_dispatch.py:285-299` (comment "ED-SC-0006: route to the PROMOTED kernel ... retiring the deprecated contest_legacy_stub.run_contest call this branch used to make" then calls `contest.build_contest`/`contest.resolve_contest` instead); `engine/tests/test_pipeline_reach.py:795 test_oi17_full_module_conversions_are_stub_wired`, `engine/tests/test_pipeline_reach.py:795 test_oi17_full_module_conversions_are_stub_wired` is `run_companion_scene`'s only caller. |
| 2. `add_belief` — the sole production constructor of `Belief` objects (the class is otherwise only constructed by `Belief.from_dict`) — has zero callers anywhere in the tree, and `restore_world` (the only other path that can populate `world.beliefs`) is itself test-only (gap 4). A live campaign can therefore never contain a `Belief`; `social_success`/`revise_belief` would always take the "not found" branch (S4.1/S3.1) if reached. | `grep -rn "add_belief(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:121`; `grep -rn "Belief(" --include="*.py" .` → only the construction inside `add_belief` itself at `systems/characters/sim/beliefs.py:131`. |
| 3. Code↔contract divergence: `references/module_contracts.yaml`'s `piety_track` entry declares `conviction.py` as a Key-substrate consumer of 9 Key types and an emitter of `state.scar_acquired`, but `conviction.py`/`beliefs.py`/`companion.py` contain no Key subscription, `echo_scheduler`/`TickScheduler` reference, or `.emit(` call anywhere — the module is a plain function-call API. | `references/module_contracts.yaml:390`, `references/module_contracts.yaml:397-408` (`sim_module: .../conviction.py`, `consumes:` 9 entries, `emits: state.scar_acquired`); `grep -rn "scar_acquired\|echo_scheduler\|TickScheduler\|\.emit(" systems/characters/sim/*.py` → no matches. |
| 4. The read (deserialize) direction of the World save/restore round-trip is test-only in production. `serialize_world` (the write direction) is called at the end of every campaign (`engine/mc_v18.py:307`), but `restore_world` has zero production callers — only `engine/tests/test_world_population.py` exercises it. | `grep -rn "restore_world(\|serialize_world(" --include="*.py" .` → `serialize_world` called from `engine/mc_v18.py:307`; `restore_world` called only from `engine/tests/test_world_population.py`. |
| 5. Declared entry points `check_conviction_threshold` and `revise_belief` have zero callers anywhere in the tree, including tests. The same is true of four accessor/reset entry points — `conviction.get_state`, `conviction.reset_all`, `beliefs.get_active_beliefs`, `beliefs.reset_all` — which §1 also marks called-by `—`; §7 carves out no exemption for accessors, so they are listed here rather than left silent. | `grep -rn "check_conviction_threshold(" --include="*.py" .` → only the def at `systems/characters/sim/conviction.py:244` and its docstring mention at line 34; `grep -rn "revise_belief(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:140` and its docstring mention at line 30; `grep -rn "get_state(" --include="*.py" .` → only the def at `systems/characters/sim/conviction.py:277` (a same-named `get_state` in `systems/threadwork/sim/coherence.py:186` is a different module's symbol); `grep -rn "reset_all(" --include="*.py" .` → only the defs at `systems/characters/sim/conviction.py:281`, `systems/characters/sim/beliefs.py:243`, and an unrelated `systems/threadwork/sim/coherence.py:193`; `grep -rn "get_active_beliefs(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:237` and its docstring mention at line 31. |
| 6. `systems/social_contest/sim/contest/armature.py` states in its own module comments that it "REUSES" `conviction.py`'s per-Conviction-Scar shape for its adjudicator armature, but the file has no import of `systems.characters.sim.conviction` (or any `characters.sim` module) — the coupling is conceptual/structural only, not a code edge. | `systems/social_contest/sim/contest/armature.py:26-27` ("in sim/personal (conviction.py carries no vector or dot-product ... So this module REUSES..."); `grep -n "^import\|^from" systems/social_contest/sim/contest/armature.py` → import block at lines 139-146, no `characters.sim` entry. |
| 7. **CLOSED 2026-08-24.** `knots.apply_knot_loss` called `apply_conviction_scar` with `conviction='Loyalty'`, a name from `npe.py`'s roster and absent from this module's own nine, so every call took the unknown-name branch and returned magnitude 0 with no `state.scars`/`state.log` mutation — ED-912 §6.1's Scar never landed. The covering test asserted only `knots.py`'s own `consequences['conviction_scar']` and never read `ConvictionState`, so it could not observe it. The 13-vs-9 question the row called unsettled is settled: the roster is now owned once by `references/descriptor_registry.yaml:conviction_roster`, cooked by `tools/export_descriptors.py` and read by `engine.substrate.descriptors`; both code rosters read it, the caller passes `'Honor'` (the pledged-oath Conviction), and an unknown name raises. | `systems/fieldwork/sim/knots.py:361-363 apply_knot_loss` (`conviction='Honor'`); `systems/characters/sim/conviction.py:59 CONVICTIONS` (read, not declared); `systems/characters/sim/conviction.py:205 apply_conviction_scar` (raises on unknown); `systems/fieldwork/sim/knots.py:346 apply_knot_loss` (`consequences['conviction_scar'] = 1`); `engine/tests/test_knots_ed912.py:141 test_a_broken_close_knot_actually_LANDS_the_conviction_scar` (the falsifier — asserts the scar STORE moved, not the announcement); `tests/valoria/test_conviction_roster_single_owner.py:63 test_no_second_conviction_roster_in_code`. |
