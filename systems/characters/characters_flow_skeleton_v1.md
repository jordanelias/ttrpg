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
| `conviction.apply_conviction_scar` | `systems/characters/sim/conviction.py:167 apply_conviction_scar` | `systems/fieldwork/sim/knots.py:350 apply_conviction_scar` (late-imported at :348) — see §7 gap 1 |
| `conviction.check_conviction_threshold` | `systems/characters/sim/conviction.py:231 check_conviction_threshold` | — (see §7 gap 5) |
| `conviction.mark_belief_revision_pending` | `systems/characters/sim/conviction.py:254 mark_belief_revision_pending` | `systems/characters/sim/beliefs.py:177 mark_belief_revision_pending`, `systems/characters/sim/beliefs.py:228 mark_belief_revision_pending` (both intra-subsystem, late-imported) |
| `conviction.get_state` | `systems/characters/sim/conviction.py:264 get_state` | — |
| `conviction.reset_all` | `systems/characters/sim/conviction.py:268 reset_all` | — |
| `conviction.ConvictionState.to_dict` | `systems/characters/sim/conviction.py:125 to_dict` | `engine/autoload/game_state.py:330 serialize_world` (duck-typed via `hasattr`) |
| `conviction.ConvictionState.from_dict` | `systems/characters/sim/conviction.py:136 from_dict` | `engine/autoload/game_state.py:409-410 restore_world` — see §7 gap 4 |
| `beliefs.add_belief` | `systems/characters/sim/beliefs.py:121 add_belief` | — (see §7 gap 2) |
| `beliefs.revise_belief` | `systems/characters/sim/beliefs.py:140 revise_belief` | — (see §7 gap 5) |
| `beliefs.social_success` | `systems/characters/sim/beliefs.py:189 social_success` | `systems/social_contest/sim/contest_legacy_stub.py:242 social_success` (late-imported at :240) — see §7 gap 1 |
| `beliefs.get_active_beliefs` | `systems/characters/sim/beliefs.py:237 get_active_beliefs` | — |
| `beliefs.reset_all` | `systems/characters/sim/beliefs.py:243 reset_all` | — |
| `beliefs.Belief.to_dict` | `systems/characters/sim/beliefs.py:60 to_dict` | `engine/autoload/game_state.py:332-333 serialize_world` (duck-typed via `hasattr`) |
| `beliefs.Belief.from_dict` | `systems/characters/sim/beliefs.py:78 from_dict` | `engine/autoload/game_state.py:413 restore_world` — see §7 gap 4 |
| `companion.run_companion_scene` | `systems/characters/sim/companion.py:28 run_companion_scene` | `engine/tests/test_pipeline_reach.py:760 run_companion_scene` (conformance probe only) — see §7 gap 1 |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `actor` (str) | arg | caller | `systems/characters/sim/conviction.py:167 apply_conviction_scar` |
| `source` (str) | arg | caller | `systems/characters/sim/conviction.py:167 apply_conviction_scar` |
| `magnitude` (int) | arg | caller | `systems/characters/sim/conviction.py:167 apply_conviction_scar` |
| `conviction` (Optional[str]) | arg | caller, must be a member of module's `CONVICTIONS` tuple | `systems/characters/sim/conviction.py:168 apply_conviction_scar` |
| `certainty` (int) | arg (default) | caller | `systems/characters/sim/conviction.py:169 apply_conviction_scar` |
| `season` (int) | arg (default) | caller | `systems/characters/sim/conviction.py:170 apply_conviction_scar` |
| `world` | world-state | caller (optional `World` instance) | `systems/characters/sim/conviction.py:75 _store` |
| `world.convictions` | registry | `engine/autoload/game_state.py:216 convictions` field | `systems/characters/sim/conviction.py:78 _store` |
| `world.beliefs` | registry | `engine/autoload/game_state.py:217 beliefs` field | `systems/characters/sim/beliefs.py:108 _store` |
| `belief_id`, `new_position`, `evidence` | arg | caller | `systems/characters/sim/beliefs.py:140-141 revise_belief` |
| `aligned` (bool), `current_momentum` (int) | arg | caller | `systems/characters/sim/beliefs.py:189-190 social_success` |
| `underlying_convictions` (list) | arg (default) | caller | `systems/characters/sim/beliefs.py:123 add_belief` |
| `scene` | arg | caller (unused by the stub body) | `systems/characters/sim/companion.py:28 run_companion_scene` |
| snapshot dict entries `'convictions'`, `'beliefs'` | world-state (deserialized) | `engine/autoload/game_state.py:354 restore_world` argument | `engine/autoload/game_state.py:408 restore_world`, `engine/autoload/game_state.py:412 restore_world` |

## 3. Flow

**S1. Conviction Scar accumulation** (`apply_conviction_scar`)
- S1 Resolve or create per-actor `ConvictionState` from the store. `systems/characters/sim/conviction.py:160 _get_or_create`
- S1.1 `[branch]` `conviction is None` → return a magnitude-0 no-op `ScarRecord`, no state mutated. `systems/characters/sim/conviction.py:185-189 apply_conviction_scar`
- S1.2 `[branch]` `conviction not in CONVICTIONS` → return a magnitude-0 no-op `ScarRecord`. `systems/characters/sim/conviction.py:191-193 apply_conviction_scar`
- S1.3 `[gate]` Thread-witnessing season cap: if `source` matches a Thread/witness pattern and the actor was already Scarred on this Conviction this season, return the prior state unchanged. `systems/characters/sim/conviction.py:198-206 apply_conviction_scar`
- S1.4 Apply Certainty-based magnitude scaling to the base `magnitude`. `systems/characters/sim/conviction.py:208-210 apply_conviction_scar`
- S1.5 `[write]` Update `state.scars[conviction]` and `state.last_scar_season[conviction]`. `systems/characters/sim/conviction.py:212-214 apply_conviction_scar`
- S1.6 `[branch][write]` Threshold check: add `conviction` to `resonant_active` / `in_crisis` sets if the new total crosses each band. `systems/characters/sim/conviction.py:217-220 apply_conviction_scar`
- S1.7 `[write]` Append a `ScarRecord` to `state.log`; return it. `systems/characters/sim/conviction.py:222-228 apply_conviction_scar`

**S2. Conviction threshold summary** (`check_conviction_threshold`, uncalled — see §7 gap 5)
- S2 Resolve actor state, partition `scars` into destabilised (=1) / shifted (=2) / in-crisis (>=3) bands, return the summary. `systems/characters/sim/conviction.py:240-251 check_conviction_threshold`

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
- S5 Resolve actor state; append `belief_id` to `state.pending_belief_revisions` if not already present. `systems/characters/sim/conviction.py:259-261 mark_belief_revision_pending`

**S6. Companion scene resolution** (`run_companion_scene`)
- S6 `[gate]` Unconditionally calls the single-owner stub primitive and returns a typed `StubResult`; no `scene` argument is read, no state is touched. `systems/characters/sim/companion.py:29-33 run_companion_scene`

**S7. World lifecycle: write direction (live)**
- S7.1 `create_world` builds a fresh `World`; `convictions`/`beliefs` default to empty dicts and are not populated during world-gen. `engine/autoload/game_state.py:216-217 World`, `engine/autoload/game_state.py:257-268 create_world`
- S7.2 `[write]` At the end of every campaign run, `serialize_world` duck-type-calls `.to_dict()` on every value in `world.convictions` / `world.beliefs` (empty in production — see §7 gap 2) into the snapshot dict. `engine/autoload/game_state.py:330-334 serialize_world`
- S7.3 `[emit]` The snapshot becomes `CampaignResult.final_state`. `engine/mc_v18.py:307` (final_state=game_state.serialize_world(world))

**S8. World lifecycle: read direction (test-only — see §7 gap 4)**
- S8.1 `[branch]` If `'convictions'` is present in the snapshot, late-import `ConvictionState` and rebuild `world.convictions` via `from_dict`. `engine/autoload/game_state.py:408-411 restore_world`
- S8.2 `[branch]` If `'beliefs'` is present, late-import `Belief` and rebuild `world.beliefs` via `from_dict`. `engine/autoload/game_state.py:412-415 restore_world`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `ScarRecord` | return value | caller of `apply_conviction_scar` (`systems/fieldwork/sim/knots.py`) | `systems/characters/sim/conviction.py:222-228 apply_conviction_scar` |
| `ConvictionThresholdState` | return value | — (no caller — §7 gap 5) | `systems/characters/sim/conviction.py:244-251 check_conviction_threshold` |
| `RevisionResult` | return value | caller of `revise_belief`/`social_success` (`systems/social_contest/sim/contest_legacy_stub.py` for `social_success`) | `systems/characters/sim/beliefs.py:180-186`, `systems/characters/sim/beliefs.py:229-234` |
| `StubResult` | return value | `engine/tests/test_pipeline_reach.py` conformance probe only | `systems/characters/sim/companion.py:29-33 run_companion_scene` |
| `world.convictions` (dict of `ConvictionState`) | world-state (write) | `engine/autoload/game_state.py` snapshot | `engine/autoload/game_state.py:330-331 serialize_world` |
| `world.beliefs` (dict of list[`Belief`]) | world-state (write) | `engine/autoload/game_state.py` snapshot | `engine/autoload/game_state.py:332-334 serialize_world` |
| `CampaignResult.final_state['convictions'/'beliefs']` | return value | nothing reads these two keys downstream — see §7 gap 2 | `engine/mc_v18.py:315 final_state` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `ConvictionState.scars` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:113`, `systems/characters/sim/conviction.py:196`, `systems/characters/sim/conviction.py:212-213` |
| `ConvictionState.resonant_active` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:115`, `systems/characters/sim/conviction.py:217-218` |
| `ConvictionState.in_crisis` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:117`, `systems/characters/sim/conviction.py:219-220` |
| `ConvictionState.pending_belief_revisions` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:119 pending_belief_revisions`, `systems/characters/sim/conviction.py:260 mark_belief_revision_pending`, `systems/characters/sim/conviction.py:261 mark_belief_revision_pending` |
| `ConvictionState.last_scar_season` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:121`, `systems/characters/sim/conviction.py:202`, `systems/characters/sim/conviction.py:214` |
| `ConvictionState.log` | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:123`, `systems/characters/sim/conviction.py:227`, `systems/characters/sim/conviction.py:133 to_dict` |
| `_conviction_state` (module-level fallback dict) | RW | `systems/characters/sim/conviction.py` | `systems/characters/sim/conviction.py:72 _store`, `systems/characters/sim/conviction.py:79-80 _store` |
| `Belief.position` | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:55`, `systems/characters/sim/beliefs.py:161-162`, `systems/characters/sim/beliefs.py:216` |
| `Belief.history` | W | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:58`, `systems/characters/sim/beliefs.py:163-167` |
| `Belief.revision_pressure` | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:57`, `systems/characters/sim/beliefs.py:225` |
| `_beliefs_by_actor` (module-level fallback dict) | RW | `systems/characters/sim/beliefs.py` | `systems/characters/sim/beliefs.py:102 _store`, `systems/characters/sim/beliefs.py:109-110 _store` |
| `world.convictions` | RW | `engine/autoload/game_state.py` (field), `systems/characters/sim/conviction.py` (accessor) | `engine/autoload/game_state.py:196`, `systems/characters/sim/conviction.py:75-80 _store` |
| `world.beliefs` | RW | `engine/autoload/game_state.py` (field), `systems/characters/sim/beliefs.py` (accessor) | `engine/autoload/game_state.py:197`, `systems/characters/sim/beliefs.py:105-110 _store` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| in | `fieldwork` (FI) | `systems/fieldwork/sim/knots.py` late-imports and calls `conviction.apply_conviction_scar` from `apply_knot_loss`'s break-consequence branch | `systems/fieldwork/sim/knots.py:348-352 apply_knot_loss` |
| in | `social_contest` (SC) | `systems/social_contest/sim/contest_legacy_stub.py` late-imports and calls `beliefs.social_success` from `run_contest`'s post-contest resolution | `systems/social_contest/sim/contest_legacy_stub.py:239-247 run_contest` |
| down | `engine.autoload` (core) | `game_state.py` imports `ConvictionState`/`Belief` directly to deserialize a campaign snapshot | `engine/autoload/game_state.py:408-415 restore_world` |
| up | `engine.substrate` (core) | `companion.py` imports the single-owner stub primitive | `systems/characters/sim/companion.py:17` (import stubwire) |

## 7. Traced gaps

| Gap | Evidence |
|---|---|
| 1. No production entry point currently exercises the subsystem's core mechanics. `apply_conviction_scar`'s only caller, `knots.apply_knot_loss`, itself has zero production callers (only `engine/tests/test_knots_ed912.py:106`, `engine/tests/test_knots_ed912.py:112`, `engine/tests/test_knots_ed912.py:115`, `engine/tests/test_knots_ed912.py:121`). `social_success`'s only caller, `contest_legacy_stub.run_contest`, has zero callers anywhere in the tree except its own definition and docstrings — production dispatch (`scene_dispatch.py`) was migrated off it. `run_companion_scene` has zero callers anywhere except an OI-17 stub-wiring conformance probe. | `grep -rn "apply_knot_loss(" --include="*.py" .` → only `engine/tests/test_knots_ed912.py`; `grep -rn "run_contest(" --include="*.py"` → only the def at `systems/social_contest/sim/contest_legacy_stub.py:191` and docstring mentions; `engine/cross_scale/scene_dispatch.py:285-299` (comment "ED-SC-0006: route to the PROMOTED kernel ... retiring the deprecated contest_legacy_stub.run_contest call this branch used to make" then calls `contest.build_contest`/`contest.resolve_contest` instead); `engine/tests/test_pipeline_reach.py:767 test_oi17_full_module_conversions_are_stub_wired`, `engine/tests/test_pipeline_reach.py:767 test_oi17_full_module_conversions_are_stub_wired` is `run_companion_scene`'s only caller. |
| 2. `add_belief` — the sole production constructor of `Belief` objects (the class is otherwise only constructed by `Belief.from_dict`) — has zero callers anywhere in the tree, and `restore_world` (the only other path that can populate `world.beliefs`) is itself test-only (gap 4). A live campaign can therefore never contain a `Belief`; `social_success`/`revise_belief` would always take the "not found" branch (S4.1/S3.1) if reached. | `grep -rn "add_belief(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:121`; `grep -rn "Belief(" --include="*.py" .` → only the construction inside `add_belief` itself at `systems/characters/sim/beliefs.py:131`. |
| 3. Code↔contract divergence: `references/module_contracts.yaml`'s `piety_track` entry declares `conviction.py` as a Key-substrate consumer of 9 Key types and an emitter of `state.scar_acquired`, but `conviction.py`/`beliefs.py`/`companion.py` contain no Key subscription, `echo_scheduler`/`TickScheduler` reference, or `.emit(` call anywhere — the module is a plain function-call API. | `references/module_contracts.yaml:279`, `references/module_contracts.yaml:286-297` (`sim_module: .../conviction.py`, `consumes:` 9 entries, `emits: state.scar_acquired`); `grep -rn "scar_acquired\|echo_scheduler\|TickScheduler\|\.emit(" systems/characters/sim/*.py` → no matches. |
| 4. The read (deserialize) direction of the World save/restore round-trip is test-only in production. `serialize_world` (the write direction) is called at the end of every campaign (`engine/mc_v18.py:307`), but `restore_world` has zero production callers — only `engine/tests/test_world_population.py` exercises it. | `grep -rn "restore_world(\|serialize_world(" --include="*.py" .` → `serialize_world` called from `engine/mc_v18.py:307`; `restore_world` called only from `engine/tests/test_world_population.py`. |
| 5. Declared entry points `check_conviction_threshold` and `revise_belief` have zero callers anywhere in the tree, including tests. The same is true of four accessor/reset entry points — `conviction.get_state`, `conviction.reset_all`, `beliefs.get_active_beliefs`, `beliefs.reset_all` — which §1 also marks called-by `—`; §7 carves out no exemption for accessors, so they are listed here rather than left silent. | `grep -rn "check_conviction_threshold(" --include="*.py" .` → only the def at `systems/characters/sim/conviction.py:231` and its docstring mention at line 34; `grep -rn "revise_belief(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:140` and its docstring mention at line 30; `grep -rn "get_state(" --include="*.py" .` → only the def at `systems/characters/sim/conviction.py:264` (a same-named `get_state` in `systems/threadwork/sim/coherence.py:186` is a different module's symbol); `grep -rn "reset_all(" --include="*.py" .` → only the defs at `systems/characters/sim/conviction.py:268`, `systems/characters/sim/beliefs.py:243`, and an unrelated `systems/threadwork/sim/coherence.py:193`; `grep -rn "get_active_beliefs(" --include="*.py" .` → only the def at `systems/characters/sim/beliefs.py:237` and its docstring mention at line 31. |
| 6. `systems/social_contest/sim/contest/armature.py` states in its own module comments that it "REUSES" `conviction.py`'s per-Conviction-Scar shape for its adjudicator armature, but the file has no import of `systems.characters.sim.conviction` (or any `characters.sim` module) — the coupling is conceptual/structural only, not a code edge. | `systems/social_contest/sim/contest/armature.py:26-27` ("in sim/personal (conviction.py carries no vector or dot-product ... So this module REUSES..."); `grep -n "^import\|^from" systems/social_contest/sim/contest/armature.py` → import block at lines 139-146, no `characters.sim` entry. |
| 7. `apply_conviction_scar`'s nearest-to-production call site carries a bug independent of gap 1's wiring: `knots.apply_knot_loss` calls it with `conviction='Loyalty'`, which is not a member of the module's `CONVICTIONS` tuple (`Faith`, `Order`, `Reason`, `Equity`, `Precedent`, `Autonomy`, `Continuity`, `Community`, `Warden`). Every such call therefore takes the `conviction not in CONVICTIONS` no-op branch (S1.2) — magnitude 0, no `state.scars`/`state.log` mutation — even if `apply_knot_loss` were wired to a production caller. The covering test only asserts `knots.py`'s own hardcoded `consequences['conviction_scar']` value and never inspects `ConvictionState`, so it cannot observe the bug. **Which side is at fault is itself unsettled, and the module's own comment carries both readings**: the block immediately above `CONVICTIONS` declares a canonical **13**-Conviction set per PP-684 (taxonomy_v30) and calls the legacy **9**-Conviction set "superseded" — directly above a `CONVICTIONS` tuple that has exactly 9 entries, i.e. the tuple *is* the set the comment names as superseded. So either `'Loyalty'` is a bad literal on the caller side (the reading this gap originally asserted), or `CONVICTIONS` itself was never migrated to the declared canonical 13-set and `'Loyalty'` is a valid member of that undelivered set — the two surfaces cannot both be right, and nothing in the tree resolves which. | `systems/fieldwork/sim/knots.py:350-352 apply_knot_loss` (`conviction='Loyalty'`); `systems/characters/sim/conviction.py:46-49 CONVICTIONS` (no `Loyalty` member); `systems/characters/sim/conviction.py:191-193 apply_conviction_scar` (no-op branch taken); `systems/fieldwork/sim/knots.py:345 apply_knot_loss` (`consequences['conviction_scar'] = 1` set independently of the call's return); `engine/tests/test_knots_ed912.py:103-112 test_ed912_break_disposition_minus3_and_positive_strain_close_scar` (asserts only `c["conviction_scar"] == 1`, never reads conviction state); 13-vs-9 comment `systems/characters/sim/conviction.py:42-44`; the 9-entry tuple it sits above `systems/characters/sim/conviction.py:46-49 CONVICTIONS`. |
