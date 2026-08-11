# DIFF — strategic subsystems (factions · settlements · world · npcs)

Derivation 1 = shipped `systems/<x>/<x>_flow_skeleton_v1.md` (grep-driven trace, adversarially reviewed).
Derivation 2 = `trace2/{code_strategic,code_world,vector_audit,contracts,indexes}.md` (no-grep whole-file reads).
Adjudications below were made against the code/data directly (allowed for me, not for D2).

## Bucket counts

| Subsystem | CONFIRMED | MISSED | CONTRADICTED | SKELETON-ONLY | STALE-SOURCE |
|---|---|---|---|---|---|
| factions | 15 | 7 | 1 | 8 | 1 |
| settlements | 11 | 5 | 2 | 6 | 0 |
| world | 10 | 4 | 0 | 4 | 1 |
| npcs | 6 | 4 | 0 | 3 | 0 |

---

## 1. FACTIONS

### CONFIRMED (15, summarised)
Both derivations independently establish: the "GD-2 mandatory-before-stochastic" docstring is false and
the real mechanism is reweight-then-single-draw (`faction_action.py:191-220`); the four signals consume
no RNG and `roll = rng.random()` is the only draw; dispatch order unique → conquest → muster → govern;
`_try_faction_unique`'s internal chain (Crown 3-mode selector / Church Excommunication→Council→Absolution
/ Varfell+Hafenmark straight to NOOP) with the universal parliamentary-censure fallback; the six pure
`stubwire` modules; `treaty.propose_treaty` and `tribunal.run_tribunal` as stubwired functions inside
otherwise-live modules while `run_excommunication_tribunal` is live; `mass_seizure.py` fully implemented
with zero production callers; `parliamentary_bridge.run_parliamentary_scene`'s default-off
`echo_scheduler` early return before any mutation; `ADJACENCY` as the conquest/threat input; the
GD-2 phrase propagating across ≥4 sibling module headers.

**Check 5 (stub-wired count) — CONFIRMED, definitional difference resolved.** Skeleton §7 says "6 of 16
modules are pure `stubwire` armature stubs"; the vector audit's `stub_wired=8` for factions
(`structure_metrics.json`) counts *modules containing ≥1 `stubwire` call site*, which adds `treaty` and
`tribunal`. The skeleton documents both extra sites (entry-points rows for `propose_treaty` /
`run_tribunal`, plus §7's treaty code↔doc gap), so its coverage is complete; only the headline number
differs, and each is right under its own definition. Not a miss, not a contradiction. The skeleton does
not, however, state that factions holds the **largest** stub-wired count of any subsystem.

### CONTRADICTED (1) — **check 1, the dispatch cascade**

D2 claims the three `if roll < cum_X:` blocks are independent (not `elif`); because
`cum_unique < cum_conquest < cum_muster` are cumulative sums of non-negative weights, entering an early
bucket that returns `_NOOP` cascades through **every** remaining bucket to an unconditional, unchecked
`return _try_govern(...)`, and `_try_govern` itself returns `_NOOP` ('invalid'), so the top-level
function can return the literal sentinel.

**Adjudication — D2 is right on the code; the skeleton's account is incomplete and its S2.7 label is
wrong.** Read at `systems/factions/sim/faction_action.py:222-242`: three bare `if` statements, no
`elif`; `_NOOP = 'invalid'` (`:87`); final statement `return _try_govern(faction, world, rng)` with no
`_NOOP` check; `_try_govern` (`:531-537`) returns `_NOOP` when `faction.territories` is empty **or**
`world.territories.get(target)` is missing **or** `t.owner != faction.name`.
- The skeleton records the *one-step* fall-throughs (S2.4.3 unique→conquest, S2.6 conquest→muster) but
  never the compound cascade, and never that the terminal return is unchecked.
- Worse, **S2.7 is affirmatively wrong**: it labels `_try_govern` "Fallback (no threshold hit above)".
  There is no such condition — the call is unconditional and is reached on *every* path where the three
  guarded returns did not fire, including a roll inside the unique bucket that NOOPed three times.
- **Where D2 overstates:** its stated consequence is not reachable at the live call site. `engine/mc_v18.py:125-127`
  skips any faction with `not faction.parliamentary` or `not faction.territories`, so the landless case
  cannot arrive; and the ownership-mismatch case is closed because both live transfer sites keep the two
  sides in sync (`faction_action.py:465-471` removes from loser + appends to winner + sets `t.owner`;
  `parliamentary_transfer.py:272-294` does both, per the OI-04 fix). The one desyncing writer
  (`mass_seizure.py:292` sets `t.owner` without touching `Faction.territories`) has zero production
  callers. **Ruling: real latent defect, currently unreachable — a caller-side invariant, not a
  resolver-side guard.** The skeleton should record both the cascade and the fact that the caller gate is
  what makes it safe.

### MISSED (7)
1. **L2 `executes` flag vs measured trace (check 4).** `references/execution_map.json` sets
   `faction_state.executes = false`, while `references/execution_trace.json` `by_contract` records
   6+60+63+7+362 = **498** calls (and `unmapped_files` shows `faction_action.py` 1077 +
   `crown_initiative.py` 68 + `parliamentary_action.py` 54 + `parliamentary_transfer.py` 131). Verified
   directly. The skeleton never reads the execution map/trace at all, so this static-map-vs-measured
   divergence is absent from all four of my skeletons.
2. **`faction_action` is a code cut-vertex** (the subsystem's only one) — removing it disconnects the
   import graph. Not recorded.
3. **L2 cycle A**: `faction_state ↔ npc_behavior ↔ piety_track ↔ social_contest` — a contract-layer cycle
   spanning four folders. No skeleton records any L2 cycle.
4. **`TREATY_CONSENT_RATE_DEFAULT = 0.28` is declared and never read.** Adjudicated: `grep -rn` over the
   tree returns exactly one hit, `treaty.py:46` (the declaration). The skeleton's treaty gap covers the
   "raises vs stub" divergence but not this dead canonical constant.
5. **`crown_initiative.coronation_renewal_prereq` docstring vs body.** Verified at `:193-208`: the
   docstring says "We do block when Crown is BOTH excommunicated AND the Church just attempted to
   excommunicate this same season", but the body only checks `church is None or not church.parliamentary`.
   A declared gate that does not exist; skeleton silent.
6. **`terrain=None` placeholder.** Verified at `faction_action.py:436`:
   `terrain=None,  # [GAP: terrain modifiers deferred to Phase 7 follow-on Steps 2-9]`. The skeleton's
   S2.5.2 records the `resolve_mass_battle` seam but not the permanently-placeholdered parameter.
7. **Contract roster incomplete.** Skeleton header claims `faction_state`, `npc_behavior (partial)`.
   `references/module_contracts.yaml` also homes **`ci_political`** (`:793`, doc `systems/factions/ci_political_v30.md`,
   `sim_module: none`, "ZERO Key integration in a CANONICAL doc") and **`faction_politics`** (`:889`,
   doc `systems/factions/faction_politics_v30.md`, `sim_module: none`, sim explicitly DEFERRED) in this
   folder. Two contracts owned by the subsystem, both codeless, both unrecorded.

### SKELETON-ONLY (8) — none unsupported
`world.casus_belli` has zero writers (two distinct reasons, both anchored); `Territory.entry_terms_l_seed`
written as an undeclared dynamic attribute and read by nothing; `scene.battle_concluded` /
`da.public_governance` emitted with no live subscriber (`articulation._TRIGGER_TYPE_IDS` lists neither);
`faction_take_action`'s return string discarded by the only caller; `__init__.py`'s stale 14-module roster;
`register_treaty` and `check_sanctuary_active` with zero callers including tests; the `faction_state`
RESOLVER half (`cascade_resolution` / `mission_shift`) having no implementation anywhere. I spot-checked
`_NOOP`, the transfer sites and the caller gate; nothing here looks unsupported.

### STALE-SOURCE (1)
D2's `indexes.md` notes `mechanics_index.yaml` still cites `audit/2026-05-14-balance-audit/...` as canon
for `parliamentary_transfer` / `treaty_expiration` while `canonical_sources.yaml` shows both since
canonized to `systems/factions/` docs. That is D2 correctly *reporting* a stale registry, not D2 being
stale — but any factions claim resting on `mechanics_index` canon paths inherits the staleness.

---

## 2. SETTLEMENTS

### CONFIRMED (11, summarised)
`populate_from_geography` reads only the `settlements:` map of `valoria_geography_v30.yaml`, validates
`stype` against `LEGAL_TYPES`, and leaves every other `Settlement` field at its dataclass default;
`Settlement.legitimacy` / `.popular_support` inert (both derivations cite the module's own PRE-LPS-1 note
*and* independently confirm it); `settlement.py`'s `compute_settlement_state` / `aggregate_to_province`
orphaned; all four `temperaments.py` entry points orphaned, with `varfell_territorial_acquisition.py`
naming the module as a "Dependency" in a docstring with no matching import; `ADJACENCY` as the live
export consumed by factions and world; `count_infrastructure` / `seizure_ob_modifier` read only by
`mass_seizure.py` (itself unreachable); `Territory.templar` as the infrastructure seed fallback; the
ledger/`succeed_governor` path having no production writer.

### CONTRADICTED (2)

**(a) The skeleton's `Contracts:` header is wrong.** It lists `registry, settlement, ledger, adjacency,
infrastructure, temperaments` — those are **Python module names, not L2 contracts**. Adjudicated against
`references/module_contracts.yaml`: its 27 `- module:` entries contain no `registry` / `ledger` /
`adjacency` / `infrastructure` / `temperaments`. The subsystem's actual contracts are **`settlement_layer`**
(`:690`) and **`settlement_economy`** (`:770`). D2's `contracts.md` is right; the skeleton conflates the
code layer with the contract layer in the one field that is supposed to name the contract layer.

**(b) "settlements executes despite `executes:false`" — D2's inference is wrong.** `vector_audit.md`
row for settlements says it "Executes at boot + `loop.s3` (75 + 1,908 calls) though L2 flag says
`executes:false`". Adjudicated against `execution_trace.json` `unmapped_files`: **every one of those
1,983 calls is `systems/settlements/sim/registry.py`** (75 boot, 1,908 `loop.s3`). `settlement_layer`'s
declared `code:` is `systems/settlements/sim/settlement.py`, which appears **nowhere** in the trace —
consistent with the skeleton's independently-derived zero-importer orphan finding for exactly that file.
**Ruling: the `executes:false` flag is correct for the file it describes.** The real defect is different
and neither derivation states it cleanly: *the contract points at the dead file while the live file
(`registry.py`) has no contract at all* — structurally the same defect as check 3 in `world`.

### MISSED (5)
1. **`Settlement.religious_building` vs `InfrastructureState.religious_building` (check 2) — real, and
   entirely absent from the skeleton.** Verified by full-tree grep: `registry.py:81` declares
   `religious_building: str = "None"`, touched only by its own `to_dict` (`:123`) / `from_dict` (`:148`)
   — i.e. never set by `populate_from_geography` and never read by any logic; the only non-serialization
   reader anywhere is the un-wired prototype `tools/sim_harness/adapters/pr119_governance/pr119_event_deck_engine.py:242`.
   The *live* field is `infrastructure.py:81`'s `InfrastructureState.religious_building`, written at
   `:160` (`build_infrastructure`) and read at `:208,219,222,246` by `count_infrastructure` /
   `seizure_ob_modifier`. Two same-named fields, two stores keyed differently (`world.settlements` by
   `sid` vs `world.territory_infrastructure` by `territory_id`), no code path connecting them. The
   skeleton records `legitimacy`/`popular_support` as inert but not this one — and this one is worse,
   because it *round-trips through serialization*, so it looks alive to anyone reading `to_dict`.
2. **`settlement_economy` omitted.** A contract nominally owned by this folder, `doc: null`,
   `sim_module: none`, whose own gap notes call it a "phantom module (no doc/state/logic)" and
   **RECOMMEND RETIRE** (ED-SE-0005). Absent from the skeleton entirely.
3. **Contract-vs-code state conflict.** `settlement_layer`'s `state:` block declares "Legitimacy (L) /
   Popular Support (PS)" as a **writable track** row, and declares 3 gates + 5 derivations. The skeleton
   proves L/PS are never read or written and that the deriving module is an orphan — but never puts the
   two side by side, so the contract's writable-state claim is left standing.
4. **`registry.py` is a code cut-vertex** (the subsystem's only one) — the live registry is also the
   single point whose removal disconnects the graph. Not recorded.
5. `Settlement.ap` (the `@property`) has no caller anywhere in D2's read scope; the skeleton lists the
   ledger convenience methods but not `ap`.

### SKELETON-ONLY (6) — none unsupported
Two uncoordinated settlement-scale entity families (17 `Territory` from module constants vs 37
`Settlement` from the geography YAML, built in the same `create_world()`); the `accord_drift_probe_hits`
probe being report-only telemetry with no reconciliation; the Accord-Echo write leg wired-but-organically-dormant
(`classify_scene_outcome` trusts only an explicit `echo['scene_outcome']` that no live producer sets);
`build_infrastructure` having no non-prototype caller; the geography YAML's whole top-level `provinces:`
block being read by no production code; `restore_world`'s settlements branch having no production caller.
D2's narrower read scope simply didn't reach `echo_transport.py` or `accounting.py`; nothing looks
unsupported.

---

## 3. WORLD

### CONFIRMED (10, summarised)
`restoration_movement.process_rm_pt_decay` / `check_rm_emergence_trigger` and
`miraculous_event.trigger_miraculous_event` are unconditional `stubwire.stub_resolve` no-ops with no
callers (**check 6: CONFIRMED — the skeleton records all three at S3/S4 and §7 gaps 1-2, and goes
further than D2 by noting `check_rm_emergence_trigger` isn't even covered by the OI-17 probe**);
`insurgency_pipeline.check_insurgency_triggers` / `check_insurgency_promotion` fully implemented and
genuinely live via `accounting.run_accounting` → `season.run_season` → `mc_v18.run_campaign`;
`npe.generate_npc` implemented with no call site and an *honest* `stubwire` marker recording the
non-call; `npe.simulate_npc_actions` live every season; the stale `[ASSUMPTION]` "World has no registry
yet" docstrings in both `insurgency_pipeline.py` and `npe.py` contradicted by `World` already carrying
`insurgencies`/`uncontrolled_streaks`/`npcs`/`npc_counter`; `ADJACENCY` import for the contiguous-group
BFS; `canonical_accord` as a cycle-break leaf; `npe.py`'s canon citation pointing at a **fieldwork** doc.

**Check 3 (world executes with no L2 contract) — CONFIRMED.** The skeleton's header and §7 gap 7 both
state that `miraculous_event` is the only one of the four sim modules with a `module_contracts.yaml`
entry, and its flow section shows `insurgency_pipeline`/`npe` running every season. I verified the
numbers D2 quotes: `execution_trace.json` `unmapped_files["loop.s3"]` = `insurgency_pipeline.py: 84` +
`npe.py: 24` = **108**, and `execution_map.json` has no module entry for either file.

### MISSED (4)
1. **The coverage inversion is never stated as such, and the trace side is absent.** The one world module
   with a contract (`miraculous_event`, `execution_map.json`: `build: "stub"`, `executes: false`,
   `note: "trigger raises."` — itself stale, it stub-resolves rather than raising) is the one that never
   runs; the two modules carrying 100% of the subsystem's traced execution have no contract. The skeleton
   states each half separately and never joins them, and cites no execution evidence at all.
2. **`systems/world/` has no `CURRENT.md` head row.** Verified: `CURRENT.md`'s head table (lines 149-170)
   has no World row (nor Characters, Victory, or UI). This is load-bearing given the skeleton's own §7
   finding that `systems/world/insurgency_pipeline_v30.md` exists on disk with `## Status: CANONICAL` —
   a canonical head that the file CLAUDE.md §1 names as *the* currency authority does not index.
3. **`scenario_authoring`** is a `module_contracts.yaml` entry scoped `scales: [peninsula]` and homed at
   `scale: world` in `mechanics_index.yaml` with `canon_sources: []` and `sim_module: null` — a
   world-adjacent contract with zero doc and zero code. Not mentioned.
4. **Structural graph facts:** world = 4 code orphans, 2 stub-wired modules, no import cycle, no
   cut-vertex. No skeleton records orphan/cycle/cut-vertex status.

### SKELETON-ONLY (4) — none unsupported
`restore_world` has no production caller; `canonical_pt` as a leaf consumed by factions + overview;
`restoration_movement.py`'s cited canon sources resolving to nothing post-`designs/` retirement while
`insurgency_pipeline.py`'s `[CANON-GATED] not yet authored` comment is stale in the *other* direction;
the `InsurgencyRecord`/`NPC` late-imports in `restore_world`. All anchored and plausible.

### STALE-SOURCE (1)
D2's `vector_audit.md` numbers are pinned to the 2026-08-06 audit and `trace_seed: 20260803`. D2 itself
diffed 08-06→08-10 and showed **zero** changes under `engine/`, `systems/`, `tests/sim/mass_battle/`, so
the structural claims hold; only the L1 prose-corpus scorecard (199 docs etc.) is dated, and I relied on
none of it.

---

## 4. NPCS

### CONFIRMED (6)
`systems/npcs/` holds zero `.py` files (both derivations verify by listing, not by absence-of-grep);
`engine/autoload/npc_ai.py`'s `select_action` / `evaluate_priority_stack` are unconditional
`stubwire.stub_resolve` no-ops with no production caller; `systems/world/sim/npe.py` is the sole NPC
implementation in the repo; `generate_npc` has no call site; `simulate_npc_actions` is wired live through
`accounting.run_accounting`; `npc_memory` is `doc: null` / `sim_module: none` with no store in code.

### MISSED (4)
1. **`npc_behavior`'s doc lives outside `systems/npcs/`.** `module_contracts.yaml:129` shows
   `doc: systems/factions/political_dynamics_keys_migration_v30.md`, a **C-KEY-2 repoint dated
   2026-07-29** that demoted `npc_behavior_v30.md` to `sources:`. So the subsystem owns neither the code
   nor the doc of its own primary contract. Compounding it: `CURRENT.md:163`'s "NPC behaviour" row still
   heads at `systems/npcs/npc_behavior_v30.md` — the currency authority and the contract layer disagree
   about this subsystem's head. The skeleton cites `module_contracts.yaml:126-141` but records neither
   the doc location nor the CURRENT.md conflict.
2. **Zero `mechanics_index.yaml` entries resolve into `systems/npcs/`** — no mechanic cites any
   `systems/npcs/` path in `canon_sources` *or* `sim_module`; the conceptually-matching `npc_ai_service`
   is canon'd to `systems/_architecture/complete_systems_reference.md#part-1` and sim'd to
   `engine/autoload/npc_ai.py`. The skeleton cites the `npc_ai_service` row (gap 5) but not the
   subsystem-wide zero.
3. **L2 cycle A membership.** `npc_behavior` sits in the contract-layer cycle
   `faction_state ↔ npc_behavior ↔ piety_track ↔ social_contest` and is itself listed as an L2-layer
   cut-vertex. Not recorded.
4. **Multi-attribution emit conflicts involving `npc_behavior`**, self-flagged OPEN-Jordan in the
   contract file: `scene.dialogue` is emitted by `scene_slate`, `social_contest` **and** `npc_behavior`
   (the registry attributes it to only the first two); `state.belief_revised` is emitted by both
   `fieldwork_knots` and `npc_behavior` (registry attributes it to fieldwork only). The skeleton lists
   `npc_behavior`'s declared edges generically but not these contested attributions.

### SKELETON-ONLY (3) — none unsupported
The `flip_choice == 2` hidden-allegiance branch computing a value never passed to the `NPC(...)`
constructor (dead branch); `PIETY_HIGH`/`PIETY_LOW` declared and never referenced, with prosperity used
as a proxy; `role` accepted by `generate_npc` and never read. All three are interior details of `npe.py`
that D2's world-lane pass did not enumerate; all carry anchors.

---

## Cross-cutting observation

The single largest systematic gap across all four skeletons is that **none of them cross-checks the code
trace against the contract/execution layer** — `references/module_contracts.yaml`'s roster, and
`references/execution_map.json`'s `executes` flags against `references/execution_trace.json`'s measured
calls. That one omission produces MISSED items 1/7 (factions), 2/3 (settlements), 1/3 (world) and 1/2
(npcs), and it is also what let the settlements skeleton put Python module names in a field labelled
`Contracts:`. Adding a per-skeleton line of the form "contract X declares `executes:<flag>`; the seeded
trace records N calls into file Y" would close it, and the two adjudications above show the exercise is
not mechanical — it caught a real map error in factions and a real D2 inference error in settlements.
