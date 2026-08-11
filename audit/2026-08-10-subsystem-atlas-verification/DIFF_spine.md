# DIFF — Derivation 1 (shipped skeletons) vs Derivation 2 (blind re-derivation)

Subsystems: `_architecture`, `overview`, `victory`, `articulation`, `ui`.
D2 sources read: `code_spine.md`, `vector_audit.md`, `contracts.md`, `indexes.md`.
D1 read: `systems/{_architecture,overview,victory,articulation,ui}/*_flow_skeleton_v1.md`.
Adjudication tool use (grep/Read of live code + registries) applied to every CONTRADICTED row and to
the six named check-hard items. Tree state: `6545067`-era; D2's vector-audit staleness caveat (§D)
verified as stated — zero files changed under `engine/`, `systems/` since 2026-08-06.

## Counts

| Subsystem | CONFIRMED | MISSED | CONTRADICTED | SKELETON-ONLY | STALE-SOURCE |
|---|---|---|---|---|---|
| `_architecture` | ~15 | 3 (+1 low) | 0 | ~8 (all supported) | 0 |
| `overview` | ~18 | 3 (+2 low) | 1 (D2 wrong) | ~8 (all supported) | 0 |
| `victory` | ~8 | 2 | 0 | ~4 | 0 |
| `articulation` | ~7 | 1 (+2 low) | 0 | ~6 | 0 |
| `ui` | ~5 | 0 | 0 | ~5 | 0 |

---

## 1. CONFIRMED (independent rediscovery — summarised)

**`_architecture` (~15).** Both derivations independently establish: the single substrate update rule
and its exact ordering (`emit` → depth/per-tick caps → `apply_defaults` → `KeyLog.append`+`_validate`
→ `_pending_apply` queue under OF-7 → synchronous subscriber notify); `accounting_boundary` drains in
emission order and `next_tick` raises on a non-empty queue; `schedule_emission`/`drain_tick` have zero
production callers (every emission is root, depth 0); `domain_echo.compute_thread_echo` has zero
callers corpus-wide; `handoff_rules` is production-reachable for exactly 1 of its 8 §3.x pairs
(`Scene→Faction`); `combat_bridge` is unreachable for **two independent** reasons (flag default OFF
*and* no `queue_scene("combat", …)` anywhere); Stability Crisis is the only field-evaluable trigger;
the Accord-Echo branch is organically dormant because no live producer sets `echo['scene_outcome']`;
`rs_track.apply_rs_delta` is a stub reached only through that dormant leg; articulation's three tier
functions are stub-wired no-ops with no production callers; `engine_clock` carries `sim_module: none`;
`echo_transport` has exactly two live Key producers (emergency-council contest, per-season
parliamentary vote); `zoom_in`/`zoom_out`/`check_mandatory_triggers` call sites agree line-for-line.

**`overview` (~18).** Campaign init order (create_world → victory.reset → scene_slate.clear → params
merge → flags → scheduler+subscribe_all); the season loop's break-on-winner; `run_season`'s composition
of **exactly three** steps; `advance_season`'s arc/seasonal reset semantics; faction dispatch gated on
`parliamentary` + ≥1 territory with exceptions swallowed; `run_accounting`'s **exactly six** steps in
fixed order with the Accord-drift probe last and report-only; the year-end-only MS decay cadence;
`DEFAULT_PARAMS['VICTORY_THRESHOLD']=11` dead against `victory.py`'s live `15`; the two per-season
`stub_resolve` calls for `generate_npc`/`form_knot`; `check_arc_boundary` orphaned; `apply_ms_delta`
never called from accounting; `ci_track`'s two lower helpers internal-only; **`ip_track`'s two entry
points both stubbed AND uncalled** (check-hard item 4 — the skeleton records this in §1 *and* §7,
and adds that `apply_ip_delta` is touched only by a generic pipeline-reach test); `rs_track` wired-but-
dormant; `world.clocks['Turmoil']` read as the PS gate with no writer (also independently found by the
victory trace and by `module_contracts.yaml`'s own peninsular_strain note — a three-way rediscovery).

**`victory` (~8).** `check_all_factions`'s sole caller `mc_v18:270`; `reset` at `:225`; the sorted
result list and first-`won` winner write; the inline fallback scoring living outside `victory.py`;
Turmoil-gate no-op; contract-declared `sim_module: engine/autoload/victory.py` with no code in the
folder; the four era gates (`g_ms0`,`g_ms5`,`g_msrec`,`g_diss`) declared and absent from code;
`executes: true` in the trace (384 calls, `loop.victory`) consistent with the once-per-season call.

**`articulation` (~7).** `subscribe_all`'s sole production caller (`mc_v18:258`) registering 13
stub-wire callbacks; all three tier functions uncalled and no-op; callbacks reachable only via
`keys.py:576-577`; code home `engine/cross_scale/articulation.py` despite an empty folder; the
contract's `consumes: {type: "*"}` wildcard vs the code's 13 explicit subscriptions — D2 found the
wildcard from the contract side, D1 found the divergence from the code side, a clean independent join;
zero orphans / zero cycles for the folder.

**`ui` (~5).** Zero `.py`/`.gd` under `systems/ui/`; no `module_contracts.yaml` entry; no
`mechanics_index.yaml` entry; `canonical_sources.yaml` names design docs only, no code pointer; no
`CURRENT.md` row. Both derivations reach "doc-only subsystem" by disjoint routes.

---

## 2. MISSED — D2 establishes it, the skeleton does not record it

### M1 (overview, HIGHEST VALUE) — the dangling emit `peninsular_strain → env.crisis`

D2 `vector_audit.md` §A/§C.1: `dangling-emits=1`, canon-grade, non-notional:
`peninsular_strain emits env.crisis` with no consumer anywhere.

**Adjudicated against the live tree — D2 is right, and it is worse than D2 states:**
- `references/module_contracts.yaml:649` — `peninsular_strain` `emits: env.crisis`; also emitted by
  `scenario_authoring` at `:952`.
- No `consumes:` row anywhere in the file carries `env.crisis`. Its three sibling types all do:
  `env.disaster` (`:79`, `:703`), `env.peninsular_strain_shock` (`:80`, `:148`, `:704`),
  `env.population_change` (`:81`, `:780`). `env.crisis` is the sole `env.*` with no `from:` row.
- **None of peninsular_strain's four declared emits is produced by any `.py` in the tree.** Grep for
  all four literals across `engine/`, `systems/`, `tools/` returns only
  `engine/cross_scale/articulation.py:124` (a *subscription* roster entry),
  `systems/settlements/sim/temperaments.py:85,144` (comments) and `tools/dashboard_data.py:784`
  (a dashboard label). Zero emitters.

`overview_flow_skeleton_v1.md` names `peninsular_strain` on its Contracts line and never diffs the
contract's emit set against code — no mention of `env.crisis`, of the dangling edge, or of the
zero-emitter fact. This is the single highest-value gap in my five subsystems: the skeleton traces the
*live* overview code (season/accounting/ci/ms/ip/rs) thoroughly and is silent on the contract the
folder actually owns.

### M2 (overview, HIGH VALUE) — `ms_track.py`'s stale `_ms_decay` docstring

D2 `code_spine.md` §4.3: `ms_track.py:19-25`'s `[DRIFT: accounting._ms_decay (…L36-39) ALSO implements
PP-255 baseline decay inline]` describes something that does not exist.

**Adjudicated — D2 is right, and there is a second corroborating surface D2 did not see:**
- `systems/overview/sim/ms_track.py` docstring still carries the `[DRIFT: accounting._ms_decay …]`
  block verbatim.
- `systems/overview/sim/accounting.py` contains no `_ms_decay`; it imports `apply_ms_baseline_decay`
  at `:43` and calls it, year-end-gated, at `:117`. Its `:36-39` is drift-probe docstring prose.
- `references/module_contracts.yaml`'s `peninsular_strain` `state:` MS row **already corrected this
  exact claim on 2026-07-29 (W3 item 8)**, states it is FALSE against the current tree, and explicitly
  records that it was "carried over from `ms_track.py`'s own docstring … not corrected there, out of
  this file's scope; logged per CLAUDE.md §0.1 point 5."

The skeleton files three stale-comment gaps of precisely this class (`__init__`'s 13-step claim, the
`stub_hits` comment, `accounting.py:31-32`'s bad `parliamentary_transfer` line cite) but not this one —
in a file it lists among its own code roots. The correction was logged in one register and never
propagated to the code; the skeleton pass was the moment to catch that and did not.

### M3 (_architecture) — the `campaign_architecture` contract is not recorded

D2 `contracts.md` #27 + `vector_audit.md` §B: `campaign_architecture` (doc
`systems/_architecture/campaign_architecture_v30.md`) is the contract actually doc-homed in this
folder; it is the **only** module with `status: stub`; it uniquely **omits** `resolver`/`consumes`/
`emits`/`state`/`transitions`/`loops` entirely rather than carrying empty lists like every other
zero-edge module (a schema-convention inconsistency); its gap_notes recommend stub retirement
[OPEN-Jordan]; its L2 correspondence is NONE (disclosed absence, not undeclared).

`_architecture_flow_skeleton_v1.md`'s Contracts line names `engine_clock` and `articulation_layer`
only. `engine_clock` is `doc: null` with `propagation_spec_v1.md` merely a *candidate* home; the
skeleton therefore claimed the folder's candidate contract and omitted its actual one. Verified in
`references/module_contracts.yaml`.

### M4 (_architecture) — `engine/autoload/npc_ai.py`: doubly dead, and the engine core's sole orphan

D2 `code_spine.md` §3/§4.1 + `vector_audit.md` §B (engine row: `1 orphan = autoload.npc_ai`;
also one of engine's 4 stub-wired modules). Both entry points (`select_action`,
`evaluate_priority_stack`) are unconditional stub-wire no-ops **and** neither is called anywhere;
its docstring names `faction_action` as a dependency while the live dispatch (`mc_v18:130`) bypasses
it entirely — a docstring asserting a dependency direction no call in the tree realises.
Per `indexes.md`, `npc_ai_service` canons to `systems/_architecture/complete_systems_reference.md#part-1`,
so this module is `_architecture`-doc-homed. Neither the `_architecture` nor the `overview` skeleton
records it at all.

### M5 (_architecture) — `engine_clock`'s `mechanical.season_change` is itself a dangling emit

D2 `vector_audit.md` §A (notional tier). **Adjudicated:** `references/module_contracts.yaml:876`
declares `engine_clock` emits `mechanical.season_change`; the only `from: [engine_clock]` consumer row
in the file is for `mechanical.accounting` (`:82`). No consumer for `season_change`. The skeleton
records `engine_clock`'s `sim_module: none` but not that one of its two declared emits is unconsumed.

### M6 (victory) — no `CURRENT.md` head row, and no code pointer in `canonical_sources.yaml`

D2 `indexes.md` §C: `victory` has no row in `CURRENT.md`'s head table; both of its mechanics
(`victory_check_service`, `peninsular_sovereignty`) sim to `engine/autoload/victory.py`, never into the
folder; `canonical_sources.yaml` names only `victory_v30.md`, no code pointer.
**Verified:** `CURRENT.md`'s 24-row table (`:147-170`) has no Victory / peninsular-sovereignty row.
This is in-format for a skeleton: the `ui` skeleton records exactly this class of fact about itself.
`victory_flow_skeleton_v1.md` states "`systems/victory/` holds no `.py`" but records neither the
missing head row nor the registry-side doc-home-for-`engine/`-code status.

### M7 (victory) — the contract declares reads the code never performs

D2 `contracts.md` #19: `victory`'s `state:` is a single aggregate row declaring reads of
**MS / IP / CI / Turmoil / Accord / Mandate / PV / PT** (clock, not writable — reader only).
`engine/autoload/victory.py` reads only `Turmoil`, territory `accord`, `owner`, and faction fields.
The skeleton records the analogous divergence for the four era **gates** but not for the declared
**state reads** — same defect class, half-recorded.

### M8 (articulation, low–moderate) — the L2 `executes:false` / `build:"stub"` flag

D2 `vector_audit.md` §B: `articulation` L2 row `executes:false`, not observed in the trace.
**Verified** in `references/execution_map.json` (`articulation_layer`: `build:"stub"`,
`executes:false`) and `execution_trace.json` (`by_contract` has no articulation entry in any phase).
The skeleton's substantive finding (all 13 callbacks wired, none can fire) is *stronger* and correct —
`subscribe_all` genuinely runs at `mc_v18:258` every default boot, so the flag means "no logic
executes", not "no code runs". Recording the flag plus that reading would close the map/trace-vs-code
loop the way `vector_audit` finding #11 does for `faction_state`.

### Low-priority misses (recorded, not weighted)

- **L1 (overview):** `world.knots` is permanently empty for the life of any campaign (D2 §4.5;
  `World.knots` at `game_state.py:196` has no populator). The skeleton records the `form_knot` stub
  call but not the state consequence.
- **L2 (overview / _architecture):** graph-fragility properties from `vector_audit` §C.7 — overview
  owns 2 code cut-vertices (`ms_track`, `season`), engine core owns 5 (`game_state`, `echo_transport`,
  `scene_dispatch`, `mc_v18`, `substrate.keys`), neither has an import cycle. No skeleton records
  cut-vertex status; arguably out-of-format for a flow skeleton, but it is a real structural fact
  neither §6 Seams nor §7 Gaps captures.
- **L3 (overview):** `peninsular_strain` shows **30 calls in `loop.s3`** in `execution_trace.json`
  while `execution_map.json` flags it `executes:false` — the overview-lane instance of the map/trace
  divergence pattern. Recorded by neither derivation (see C1).
- **L4 (articulation):** the contract's own gap_note ("significance function / `belief_revised`
  emission path not extracted") is not cross-referenced by the skeleton, which records
  `state.belief_revised` only as one of the 10 unemitted ids.

---

## 3. CONTRADICTED (adjudicated against the code)

### C1 — "overview not observed as its own bucket in the trace" (D2 wrong)

`vector_audit.md` §B, `overview` row: "Not observed as its own bucket in the trace."
**Adjudicated against `references/execution_trace.json`** — the file D2's own agent cites:
`by_contract["loop.s3"]["peninsular_strain"] = 30`. The overview contract *is* present in the trace.
D2's row is wrong (it read `by_subsystem_path`, where overview's files are attributed to
`engine/substrate`/`world`/`settlements` buckets, and did not cross-check `by_contract`). The skeleton,
which traces those accounting calls as live, is right. **Ruling: D2 error, no skeleton change.**

### C2 (check-hard item 5) — "`dice_engine.py` / `sigma_leverage.py` have zero callers"

`code_spine.md` §5 asserts both are "complete, clean root primitives with **zero callers anywhere in
this entire scope**", correctly caveated as scope-limited. Propagated without the caveat it would be a
serious false finding. **Adjudicated by grep over the live tree:**

- `sigma_leverage` has real production importers: `systems/combat/combat_engine_v1/core.py:19`
  (`from engine.autoload import sigma_leverage as SL` — the canonical PC resolver's σ-kernel),
  `systems/social_contest/sim/contest/resolver.py:23-24`, `primitives.py:9`, `armature.py:146`,
  `wrapper.py:376`.
- `dice_engine` has ~15 production importers, including several reached **from the traced season loop**:
  `systems/social_contest/sim/parliamentary_vote.py:40,177` (live every season via
  `parliamentary_bridge`), `systems/factions/sim/council_solmund.py:20,63`, `tribunal.py:26,125`,
  `crown_initiative.py:27,82`, `absolution.py:21,64`, `parliamentary_transfer.py:52`,
  `mass_seizure.py:49`, plus threadwork/fieldwork/combat.
- `sigma_leverage` itself imports `dice_engine` (`engine/autoload/sigma_leverage.py:66`) and delegates
  every roll to it (`:266`, `:277`).

**Ruling: D2's spine agent was right within its declared scope and wrong as a global claim — the one
concrete corroboration it cited (`combat_engine_v1/core.py` imports `sigma_leverage`) is correct.
Both modules are live, heavily-used substrate primitives reached from the campaign loop.** No skeleton
of mine asserts otherwise (none traces `engine/autoload/dice_engine.py`; per `indexes.md` §D these
primitives canon to the evacuated `engine/params/core.md` and belong to no `systems/` folder), so no
correction is required — but this bullet must not be propagated as a dead-module finding.

---

## 4. SKELETON-ONLY (D2 did not see it; none unsupported)

D2's spine agent read only `engine/{substrate,autoload,cross_scale,mc_v18}` + `systems/overview/sim` and
read **no tests**; the skeletons traced tests and registries too. Everything in this bucket spot-checked
as anchored and none looks unsupported:

- `_architecture`: the full caller table incl. test call sites; `TypeRegistry.load_json` never called
  directly; the WARN-tier `stat_vocabulary` check being default-off corpus-wide; `causes[]` populated in
  exactly one place; `cross_scale/__init__.py` docstring-only vs `substrate/__init__.py`'s re-exports;
  `faction_action.py`'s two stale in-code claims; the `parliamentary_transfer` third emitter.
- `overview`: `max_seasons` dead-param shadowing; the `stub_hits` stale comment; the LPS-1
  port-blocking note; `accounting.py:31-32`'s bad line citation; the CI Assert/Suppress params never
  supplied; the 13-step-vs-6-step `__init__` drift; `PI`/`Strain` seeded-and-dead; the
  `Territory.adjust_accord` write-path note (explicitly flags that a literal grep misses it).
- `victory`: the `test_f7_victory_threshold_is_a_dead_param` falsifier; three `VictoryResult` fields
  computed-and-unread while `.held` is *not* dead (sort tie-break); the fallback formula's absence from
  the contract.
- `articulation`: the 13-id roster split into 10-with-no-emitter + `scene.combat_felled` (no path at
  all) + `scene.combat_resolved` (default-off flag) + `scene.accord_echo` (dormant); `subscribe_all`
  non-idempotent and unguarded.
- `ui`: the `godot/skeleton/` `.gd` survey and zero-`.tscn` finding; the `dashboard/` vs game-UI
  disambiguation by direct evidence rather than name; `_identifier_census`'s 24 BUILT rows all resolving
  into *other* subsystems; the `render_protagonist_lens` scope-boundary note.

## 5. STALE-SOURCE

None. D2's `vector_audit.md` §D verifies zero changes under `engine/`, `systems/`,
`tests/sim/mass_battle/` between the 2026-08-06 audit and today, and `module_contracts.yaml` /
`execution_map.json` / `execution_trace.json` all predate the audit — so every structural claim it
carries is current against the tree the skeletons traced. The only dated figures are L1 prose-corpus
counts, which nothing here relies on.

## 6. Check-hard items — disposition

| # | Item | Verdict |
|---|---|---|
| 1 | `peninsular_strain → env.crisis` dangling emit | **MISSED (M1)** — overview skeleton silent; verified dangling *and* zero code emitters for all four declared emits |
| 2 | L2 cycle `faction_state ↔ npc_behavior ↔ piety_track ↔ social_contest`; `personal_combat` self-loop | **Out of my lane** — no member belongs to my five subsystems. Flag for the factions/characters/social_contest/combat diff owners. Positive observation: `articulation_layer`'s wildcard `*` consumes edge with `emits: []` makes it a structural sink, so it cannot participate in an L2 cycle — neither derivation states this |
| 3 | `ms_track.py`'s docstring claiming an inline `accounting._ms_decay` | **MISSED (M2)** — verified false against `accounting.py`; already corrected once in `module_contracts.yaml` (2026-07-29) and never propagated to the code |
| 4 | `ip_track` both entry points stubbed AND uncalled | **CONFIRMED** — recorded by the overview skeleton in §1 and §7, with the extra fact that `apply_ip_delta` is touched only by a generic pipeline-reach test |
| 5 | `dice_engine` / `sigma_leverage` zero callers | **CONTRADICTED (C2)** — scope-true, globally false; both are live primitives reached from the season loop; `combat_engine_v1/core.py:19` confirmed |
| 6 | `mass_battle` sole UNDECLARED L2 contract | **Out of my lane.** Both D2 sources independently agree the omission is *deliberate* (`contracts.md` #13: an inline comment declares the row MB-lane-owned single-writer; `vector_audit` #8: verified pre-existing at `f03357d`, so the register's "regression" classification is wrong). Flag for the MB diff owner |
