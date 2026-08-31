# TRACE REGISTER — season loop · world churn · emergent narrative · persons

**Compiled 2026-08-31** at working-tree HEAD `f59fd0e`. Every line number below was opened and read
**this pass**. Where a number differs from a previously-asserted one, **this file's number is the
verified one** and the discrepancy is logged in §10.

**Method notes, so a citing author can reproduce:**
- Structured counts use `yaml.safe_load` / `json.load`, never `grep -c`. Where a value lives in a
  YAML **comment** (and is therefore invisible to the parser) that is stated explicitly.
- Reachability claims come from an executed probe, not from reading imports: a seeded
  `mc_v18.run_campaign(seed=42)` with `sys.modules` inspected after the run.
- Absence claims name the search that produced them.

**Status legend:** `LIVE` = executes in a default seeded campaign · `BUILT-INERT` = correct
implementation, zero production callers · `STUB` = typed no-op via `stubwire` · `DEAD` = declared
and structurally unreachable.

---

## 1. THE TICK AND ITS PHASES

### 1.1 `engine/autoload/engine_clock.py` (127 lines)

| Line | Symbol | What it guarantees / does | Status |
|---|---|---|---|
| 67 | `from engine.autoload.season_manager import advance_season` | The only direct import; SEASON_TICK body | LIVE |
| 68 | `from engine.substrate import composition` | Accounting is resolved by ROLE, not imported | LIVE |
| 73–75 | `PHASE_SEASON_TICK="season_tick"`, `PHASE_ACTION="action"`, `PHASE_ACCOUNTING_BOUNDARY="accounting_boundary"` | Exported phase names for callers/tests | LIVE |
| 77 | `PHASES = (PHASE_SEASON_TICK, PHASE_ACTION, PHASE_ACCOUNTING_BOUNDARY)` | The 3-tuple; **string values differ from the scheduler's own `_PHASE_ACTION`/`_PHASE_ACCOUNTING` in `keys.py:70–71`, deliberately (one owner each)** | LIVE |
| 80–87 | `scheduler_of(world)` | `getattr(world,"echo_scheduler",None)` — returns `None` when ECHO_TRANSPORT is off | LIVE |
| 90 | `def run_tick(world, action_callback=None)` | The composition owner per `propagation_spec_v1 §O.1` | LIVE |
| 115 | `result = advance_season(world)` | **SEASON_TICK** | LIVE |
| 117–118 | `if action_callback is not None: action_callback(world)` | **ACTION** body is **caller-supplied**; `engine_clock` defines no dispatch policy | LIVE |
| 120–122 | `sched = scheduler_of(world)` / `sched.accounting_boundary()` | Opens ACCOUNTING_BOUNDARY; drains OF-7 deferred applies; flips `_phase` | LIVE |
| **123** | `composition.require('accounting')(world)` | **The RAW `run_accounting` call, outside any drain** — the shape `propagation_spec §4.1` rejects. Bounded today only because accounting emits no Keys (see §1.4) | LIVE |
| 124–125 | `sched.next_tick()` | Runs **LAST**, so the per-tick emission counter spans BOTH phases | LIVE |
| 127 | `return result` | Returns `season_manager.SeasonResult` | LIVE |

**`run_tick` NEVER calls `drain_tick()`.** Search: `grep -rn "drain_tick" --include=*.py engine/ systems/ tools/`
→ 2 hits in `engine/substrate/keys.py` (the definition at :538 and its own docstring at :529) and
**zero elsewhere outside `tests/valoria/test_key_substrate.py`**. The scheduled-emission queue is
never drained in production.

### 1.2 `engine/autoload/season_manager.py` (50 lines)

| Line | Symbol | What it does |
|---|---|---|
| 23 | `SEASONS_PER_ARC = 4` | Arc length. Distinct from `ms_track.SEASONS_PER_YEAR = 4` (`systems/overview/sim/ms_track.py:48`) — two constants, same value, different owners |
| 26–30 | `@dataclass SeasonResult(season:int, arc:int, new_arc:bool)` | 3 fields |
| 33 | `def advance_season(world) -> SeasonResult` | The **only** module permitted to advance the season counter |
| 35 | `world.season += 1` | THE season counter write |
| 36 | `new_arc = (world.season % SEASONS_PER_ARC == 1)` | Arc boundary at season ≡ 1 (mod 4) |
| 37–41 | `world.arc += 1`; `f.reset_arc()` for every faction | Per-arc flag reset |
| 43–44 | `f.reset_seasonal()` for every faction | Per-season flag reset (unconditional) |
| 48–50 | `check_arc_boundary(season)` | `season % 4 == 1`. **Zero callers** — `grep -rn "check_arc_boundary" --include=*.py .` returns only the definition and its docstring |

### 1.3 `systems/overview/sim/season.py` (87 lines) — ADAPTER ONLY

| Line | Symbol | What it does |
|---|---|---|
| 7–13 | `⚠ THIS MODULE NO LONGER OWNS THE COMPOSITION (2026-08-27, ED-IN-0199)` | Explicit retraction banner |
| 41–47 | `@dataclass SeasonResult(season, arc, new_arc, accounting_run)` | **4 fields — a DIFFERENT shape from `season_manager.SeasonResult`'s 3.** Two same-named dataclasses coexist |
| 50 | `def run_season(world, action_callback=None) -> SeasonResult` | The `season_driver` composition role target |
| 59–72 | docstring "The composition is canonical:" | **Restates a composition it does not perform** — line 60–61 says so explicitly |
| 81 | `sr = engine_clock.run_tick(world, action_callback=action_callback)` | The whole body |
| 86 | `accounting_run=True` | **Hardcoded `True`** — never derived from whether accounting ran |

### 1.4 `systems/overview/sim/accounting.py` (143 lines) — SIX STEPS, ZERO KEYS

| Line | Step | What it does |
|---|---|---|
| 96 | `def run_accounting(world)` | The ACCOUNTING_BOUNDARY body |
| 113 | 1. `apply_seasonal_ci(world)` | PP-412 CI seasonal calculation — every season |
| 117–118 | 2. `if world.season > 0 and world.season % SEASONS_PER_YEAR == 0: apply_ms_baseline_decay(world)` | PP-255, Year-End only. **Cadence gate is HERE, not in `apply_ms_baseline_decay`** |
| 125 | 3. `check_insurgency_triggers(world)` | GD-3 a–b emergence. Returned events **discarded** |
| 132–133 | 4. `for ins_id in list(get_insurgencies(world).keys()): check_insurgency_promotion(ins_id, world)` | GD-3 c–e promotion, over a snapshot |
| **139** | 5. `simulate_npc_actions(world)` | NPE territory-level stance drift. Returned actions **discarded** |
| 143 | 6. `_probe_province_accord_drift(world)` | REPORT-ONLY, runs last |
| 54 | `def _probe_province_accord_drift(world)` | Never writes either compared value; sets `world.accord_drift_probe_hits` (a dynamic attribute, **not** a `World` dataclass field) |

**Does accounting emit Keys? NO.** Search: `grep -n "emit\|sched\|Key" systems/overview/sim/accounting.py`
→ **one** hit, `accounting.py:68`, inside a docstring naming `scene.accord_echo`. No `emit`, no
scheduler reference, no `Key` construction. All six steps are direct state writes. This is the fact
that makes the raw call at `engine_clock.py:123` currently harmless.

**MEASURED (seed 42, 50 seasons):** `accord_drift_probe_hits = 342` — the two provincial-Accord write
models diverge on most (season, province) pairs.

---

## 2. THE EVENT SUBSTRATE — `engine/substrate/keys.py` (601 lines)

### 2.1 Module constants

| Line | Symbol | Value |
|---|---|---|
| 59 | `AXES` | `("hierarchical","sacred","instrumental","traditional")` — the canonical 4 |
| 62 | `ROLES` | `("subject","object","witness","beneficiary","bystander")` |
| 65 | `SCALES` | `("personal","settlement","territory","peninsula")` |
| 67 | `PERMANENCE_VALUES` | `("transient","persistent","indelible")` |
| 68 | `TIME_HORIZON_VALUES` | `("immediate","near","far")` |
| 70–71 | `_PHASE_ACTION="ACTION"`, `_PHASE_ACCOUNTING="ACCOUNTING_BOUNDARY"` | Scheduler-internal, **not** re-exported |
| 74 | `class KeyValidationError(ValueError)` | Invariant / payload-contract breach |
| 78 | `class TerminationBreach(RuntimeError)` | Level-B guard breach. **Raises rather than clamping, deliberately** |

### 2.2 The four dataclasses — every field

| Line | Class | Fields (name : type = default) |
|---|---|---|
| 87–105 | `Target` | `actor_id:str` · `role:str` · `impact_vector:dict={}` (axis→signed magnitude) · `stat_deltas:dict={}` (stat_name→delta). `to_obj()` @99 |
| 108–121 | `Visibility` | `public:bool=True` · `semi_public_observers:list=[]` · `private_observers:list=[]`. `to_obj()` @116 |
| 124–134 | `EmittedAt` | `season_index:int` · `sub_step_index:int=-1` (**-1 = not yet appended**; assigned by `KeyLog.append`). `to_obj()` @133 |
| 137–174 | `Key` | `id:str` · `type:str` · `emitted_at:EmittedAt` · `source_actor:str\|None=None` · `causes:list=[]` · `targets:list=[]` · `scale_signature:list=[]` · `symbolic_dimensions:dict={}` · `visibility:Visibility=Visibility()` · `time_horizon:str="immediate"` · `permanence:str="transient"` · `payload:dict={}`. `to_obj()` @156 |

`Key` carries **no `cascade_depth` field** (@139–141, SSI-4): the re-entrancy meter is
scheduler-internal and is never logged.

### 2.3 `KeyLog` (@336)

| Line | Member | Contract |
|---|---|---|
| 345 | `__init__(registry, *, stat_vocabulary=None)` | `stat_vocabulary` default `None` skips invariant-9 entirely |
| 347–349 | `_entries:list` · `_ids:dict` · `_season_counters:dict` | **dict, not set — ORD-2** |
| 356 | `stat_vocabulary_warnings:list` | WARN-tier collection, never raises |
| 358/361 | `__len__` / `__iter__` | Length + append-order iteration |
| 364 | `lookup(key_id)` | `self._entries[self._ids[key_id]]` — raises `KeyError` on an unknown id |
| 367 | `append(key)` | validate → optional vocab check → **assign `sub_step_index` from the per-season counter (SSI-1 append order)** → index → append |
| 453 | `serialize()` | `json.dumps(..., sort_keys=True, ensure_ascii=False, separators=(",",":"))` per Key, newline-joined. Deterministic |
| 459 | `content_hash()` | `sha256(serialize().encode("utf-8")).hexdigest()` |

### 2.4 The numbered invariants, each with its line (`KeyLog._validate` @378)

| Invariant | Line | Rule | Enforcement |
|---|---|---|---|
| **1** id unique | 380–381 | `key.id in self._ids` → raise | RAISE |
| **2** type registered + payload | 383 | delegates to `registry.validate_payload` (@308) | RAISE |
| **3** causes[] already logged | 385–389 | every `cause_id` must be in `_ids` | RAISE |
| **4** cycle-freedom | 390–393 | **holds BY CONSTRUCTION** — no runtime check; comment only | (none) |
| **5** ordering | 394–398 | `season_index` may not regress below the last entry's | RAISE |
| **6** canonical axes | 399–405 | every key in `symbolic_dimensions` and every `target.impact_vector` must be in `AXES` | RAISE |
| — role check | 406–410 | `t.role in ROLES` (§2.2, unnumbered) | RAISE |
| **7** scale_signature | 411–418 | non-empty **and** every member in `SCALES` | RAISE |
| **8** visibility shape | 419–430 | `public=True` forbids observer lists; `public=False` requires **exactly one** non-empty list (XOR) | RAISE |
| — horizon/permanence | 431–434 | membership in `TIME_HORIZON_VALUES` / `PERMANENCE_VALUES` | RAISE |
| **9 (candidate)** stat vocabulary | 436–451 | `_check_stat_vocabulary` — appends to `stat_vocabulary_warnings` | **WARN, never raises** |

### 2.5 `TickScheduler` (@463)

| Line | Member | Contract |
|---|---|---|
| 476–490 | `__init__(log, *, cascade_depth_max, emissions_per_tick_max, no_sync_reentry=True, defer_apply=True)` | **Both caps are REQUIRED keyword args with NO default** — OF-CAP is an open fork, so no fabricated constant enters the substrate. `no_sync_reentry` (OF-B1) and `defer_apply` (OF-7) are RATIFIED-default-ON but caller-toggleable |
| 497–503 | `subscriptions:dict` · `_phase=_PHASE_ACTION` · `_queue:list` · `_pending_apply:list` · `_emitted_this_tick=0` · `_in_drain=False` · `_current_depth=0` | dict + list = ORD-1 |
| 506 | `subscribe(type_id, callback)` | Purely additive `setdefault(...).append(...)` — **calling twice registers duplicates** |
| 510 | `emit(key, apply=None)` | Root emission at depth 0. @518–522: **raises `TerminationBreach` if called during a drain while `no_sync_reentry`** |
| 525 | `schedule_emission(key, apply=None)` | Depth = `_current_depth + 1` if in a drain else 0. @531–535: **raises `TerminationBreach` if depth > `cascade_depth_max`** |
| 538 | `drain_tick() -> int` | FIFO pop from `_queue`; returns count drained. **Zero production callers** |
| 555 | `_emit_at_depth(key, depth, apply)` | @556–560 depth cap → `TerminationBreach`; @561–565 **`_emitted_this_tick + 1 > emissions_per_tick_max` → `TerminationBreach`**; @566 `apply_defaults`; @567 `log.append`; @569–573 OF-7 branch (defer if `_phase == _PHASE_ACTION`, else apply immediately); @576–577 synchronous subscriber notify |
| 581 | `accounting_boundary() -> int` | Sets `_phase = _PHASE_ACCOUNTING`, runs `_pending_apply` **in emission order**, clears, returns count |
| 593 | `next_tick()` | @598–599 **raises `TerminationBreach("tick advanced with undrained emissions in queue")` if `_queue` is non-empty**; @600 resets `_emitted_this_tick`; @601 returns `_phase` to ACTION |

**What happens when a cap is exceeded:** a `TerminationBreach` (RuntimeError) propagates. Nothing
catches it in `engine_clock` or `mc_v18`; the campaign aborts. Production caps come from
`engine/cross_scale/echo_transport.py:102–103`: `DEFAULT_CASCADE_DEPTH_MAX = 0` and
`DEFAULT_EMISSIONS_PER_TICK_MAX = 64`. **A depth cap of 0 makes any `schedule_emission` issued
during a drain raise immediately** — cascading is structurally impossible in a default campaign.

### 2.6 `TypeRegistry` (@184) and the `family.type` regex

| Line | Symbol | Contract |
|---|---|---|
| 177 | `_TYPE_HEADING = re.compile(r"^### (?P<tid>[a-z_]+\.[a-z_]+)\s*$", re.MULTILINE)` | The markdown heading shape; makes a malformed id unrepresentable in the authored source |
| 178 | `_YAML_BLOCK = re.compile(r"```yaml\s*\n(?P<body>.*?)\n```", re.DOTALL)` | Per-type body |
| **181** | `_TYPE_ID = re.compile(r"[a-z_]+\.[a-z_]+")` | **THE `family.type` id regex**, applied with `.fullmatch` in `load_json` |
| 213 | `load(registry_path)` | Dispatches on `.json` suffix → `load_json`, else markdown |
| 232 | `load_json(path)` | @250–254 rejects malformed ids; @255–259 rejects non-dict entries; @261–264 **cross-checks the document's own `type_count` against `len(types)` and raises on mismatch** |
| 268 | `_parse_entry(body)` | Deliberately tolerant line parser (registry yaml blocks are prose-flavoured). @294 the flow-list branch requires `value.startswith("[") and value.endswith("]")` — **a trailing `# comment` defeats it; see §9/§10** |
| 303 | `require(type_id)` | Raises `KeyValidationError ... (§2.3 invariant 2)` |
| 308 | `validate_payload(key)` | Strips `# comment` off each required field name, then checks presence |
| 322 | `apply_defaults(key)` | Fills `scale_signature` / `permanence` / `time_horizon` **only when the emitter left the dataclass default** |

### 2.7 `engine/substrate/__init__.py` (41 lines) — the NOT-implemented list

| Line | Item | Blocked on |
|---|---|---|
| 16–19 | observer resolution / armature interpretation (`key_substrate §4.1` steps 3–4) | **ORD-3 unratified** — implementing `compute_observers()` first would bake in hash-order nondeterminism |
| 20 | `decay()` over the key log (AU-4) | **OF-3, unspecified** |
| 21–22 | canonical cap constants | **OF-CAP open** — caps stay REQUIRED caller parameters |
| 23 | campaign-loop wiring | "PR-2 scope (flag-gated), not this module" — **this one is now DONE elsewhere** (`mc_v18.py:249–266`); the list is stale on this row |
| 26–41 | re-exports | `AXES, ROLES, SCALES, PERMANENCE_VALUES, TIME_HORIZON_VALUES, EmittedAt, Key, KeyLog, KeyValidationError, Target, TerminationBreach, TickScheduler, TypeRegistry, Visibility` — 14 names |

---

## 3. RESOLUTION

### 3.1 `engine/autoload/dice_engine.py` (299 lines)

| Line | Symbol | Contract |
|---|---|---|
| 27–31 | `class Degree(Enum)` | `OVERWHELMING / SUCCESS / PARTIAL / FAILURE` |
| 36–41 | `DEGREE_LABEL: dict[Degree,str]` | Title-Case strings — **one map**, so string-speaking modules resolve through the owner |
| **48–53** | `DEGREE_ORDINAL: dict[Degree,int]` | **EXISTS.** `FAILURE:0, PARTIAL:1, SUCCESS:2, OVERWHELMING:3` |
| 95 | `class BandExtension` | The ED-SC-0032 injection seam |
| 104 | `name = "band-extension"` | Named policy for reprs/stack traces |
| 107 | `context_keys: tuple = ()` | Declared context keys; the engine REFUSES any other |
| 109–111 | `may_overwhelm(net, ob, **context) -> bool` | Default `True` (never vetoes) |
| 113–135 | `validate_context(context)` | Raises `TypeError` on an undeclared key. Exists because the seam shipped with a silent-no-op hole |
| **Contract** | — | **An extension's ONLY power is to veto the top band (3→2).** Return is coerced with `not` and consulted in exactly one branch (@289–292). It cannot promote a band, move the Partial window, or touch Failure. @77–87 records the honest limit: an extension is arbitrary Python and could reach outside the seam; the bound is on the *return channel*, not a sandbox |
| 141–148 | `@dataclass RollResult` | `pool_size:int` · `tn:int` · `rolls:list[int]` · `net:int` · `degree:Degree\|None` · `ob:int\|float\|None` |
| **153–161** | `_die_result(face)` | **THE FACE RULE:** `1 → -1` · `2–6 → 0` · `7–9 → +1` · `10 → +2`. No chaining. **Never reads `tn`** |
| **174** | `_MU_PER_DIE: float = 0.40` | TN-7 per-die EV |
| **175** | `_SIGMA_PER_DIE: float = 0.800` | TN-7 per-die σ |
| 166–173 | comment | TN 6 (μ=0.50) and TN 8 (μ=0.30) rows **deleted** under ED-IN-0196 |
| 178–179 | `_TN_RULING` | Jordan 2026-08-25 verbatim: *"TN7 always. Never change TN anywhere ever."* |
| **182–193** | `_require_tn7(tn)` | **TN ENFORCEMENT: `if tn != 7: raise ValueError(...)`.** `tn` is kept as a parameter (carried on `RollResult`, ~30 call sites, crosses to the Godot bridge) but is now *refused* rather than ignored |
| 196 | `roll_pool(pool_size, tn=7, ob=None, rng=None)` | @199 calls `_require_tn7`; @202 `effective_pool = max(1, pool_size)` (pool minimum 1D) |
| 209 | `continuous_engine_sample(pool, tn=7, rng=None)` | @216 `_require_tn7`; @219–220 `pool <= 0 → 0.0`; @222–224 `Normal(μ·pool, σ·√pool)`. **@214 docstring: "Pool may be fractional (enables a fractional Ob)"** — accepts fractional pools with no quantisation |
| **227** | `degree_from_net(net, ob, extension=None, **context) -> Degree` | THE single degree ladder |

**The exact bands (`degree_from_net` body, lines 279–294) — margin-based, never Ob-scaled:**

```
279   margin = net - ob
280-281   margin  <  0   → Degree.FAILURE
282-283   margin  <  1   → Degree.PARTIAL        # 0 <= margin < 1, a whole-success-wide window
284-293   margin >=  3   → Degree.OVERWHELMING   # unless extension.may_overwhelm() is False → SUCCESS
294   (otherwise)        → Degree.SUCCESS        # 1 <= margin < 3
```

Explicitly **RULED OUT** at lines 263–267: Ob-scaled Overwhelming (`net >= 2*Ob`), the separate
PP-232 `net >= 3` floor, and the Ob-20 exception. @254–261 records that
`engine/engine_params/params_tables.yaml` §"Degrees of Success" still shows the **pre-ruling** bands
and is history, not canon.

| 297–299 | `degree_label(net, ob) -> str` | `DEGREE_LABEL[degree_from_net(net, ob)]` — convenience, not a second ladder |

### 3.2 `engine/autoload/sigma_leverage.py` (333 lines)

| Line | Symbol | Value / contract |
|---|---|---|
| 77–79 | `PER_DIE: dict[int, tuple[float,float]] = {7: (0.40, 0.800)}` | Keyed by TN so a non-7 fails with `KeyError` rather than silently resolving |
| 91 | `TN_STANDARD = 7` | |
| 97–102 | `LEVEL_SIGMA` | `minor 0.25 · moderate 0.50 · strong 0.75 · major 1.00` |
| 104 | `M_MAX = 1.5` | Soft-cap ceiling, σ-units |
| 105 | `SIGMA_N_COEFF = 0.8` | `sigma_N = 0.8·√Pool` |
| **108** | `OB_MIN = 1` | `[canonical: params/core.md §Obstacle Scale]`. Applied at @177 (`eff_ob`): `return max(float(OB_MIN), float(raw))` |
| 112–113 | `MU_PER_DIE = 0.40`, `SD_PER_DIE = 0.80` | GENERAL (not contest-specific); the contest's de-saturation extension reads them here |
| 114–116 | `OVERWHELM_SIGMA` **MOVED OUT** 2026-08-27 | now `systems/social_contest/sim/contest/degree_extension.py` |
| 269 | `roll_net(pool, tn=7, rng=None) -> int` | **DISCRETE path — keeps `max(1, int(round(pool)))` @274.** Whole dice are correct here |
| **282** | `roll_net_continuous(pool, tn=7, rng=None) -> float` | **@314: `effective_pool = max(1.0, float(pool))`** |
| — | **ARE POOLS FRACTIONAL NOW?** | **YES on the continuous path.** The `int(round(pool))` that stood at :314 was removed 2026-08-21 (M1 juncture 1, ED-IN-0187). The **1D floor stays** and is canon. `roll_net` (discrete) is unchanged |
| 116–130 | retirement block | `degree(net, ob, pool)`, `overwhelm_bar`, `crossover_pool` all moved to the contest package |

### 3.3 `derive_ob` — DOES NOT EXIST

| Search run | Result |
|---|---|
| `grep -rn "def derive_ob" --include=*.py .` | **0 hits** |
| `grep -rn "derive_ob" --include=*.py .` | **0 hits** — the string does not appear in any Python file in the tree |
| `grep -rln "derive_ob" --include=*.md --include=*.yaml .` | ≥20 files, **all under `proposals/` and `research/`** — proposal prose only |

**No `derive_ob` exists anywhere in `engine/` or `systems/`, as a definition or as a mention.** This
matches `dice_engine.py:243–247`, which states the fractional-Ob derivation is *"RULED … but ⚠ THAT
DERIVATION IS IMPLEMENTED NOWHERE — every call site in the tree still passes a hand-set Ob."*

---

## 4. STATE, AND WHO WRITES IT — `engine/autoload/game_state.py` (513 lines)

### 4.1 `World` (@255–301) — every field

| Line | Field | Default / note |
|---|---|---|
| 257 | `factions: dict[str,Faction]` | `{}` |
| 258 | `territories: dict[str,Territory]` | `{}` |
| 259 | `clocks: dict[str,float]` | `{}` — populated @338 with `{'CI':30.0,'MS':60.0,'IP':20.0,'PI':0.0,'Strain':0.0,'Turmoil':0.0}` |
| 260 | `season: int` | `0` |
| 261 | `arc: int` | `0` |
| 262 | `winner: str\|None` | `None` |
| 263 | `battle_count: int` | `0` |
| 264 | `scenes_resolved: int` | `0` — F7 telemetry. **NOT serialized** (see §10) |
| 265 | `rng: random.Random` | `random.Random()` |
| 274 | `practitioners: dict` | actor_id → CoherenceState |
| 275 | `insurgencies: dict` | insurgency_id → InsurgencyRecord |
| 276 | `uncontrolled_streaks: dict` | frozenset[tid] → int |
| 277 | `npcs: dict` | territory_id → list[NPC] |
| 278 | `npc_counter: int` | `0` |
| 279 | `treaties: dict` | frozenset[parties] → TreatyRecord |
| 286 | `convictions: dict` | actor_id → ConvictionState |
| 287 | `beliefs: dict` | actor_id → list[Belief] |
| 288 | `knots: dict` | knot_id → Knot |
| 289 | `knot_id_counter: int` | `0` |
| 290 | `territory_infrastructure: dict` | territory_id → InfrastructureState |
| 291 | `npc_drift_state: dict` | territory_id → float |
| 292 | `threadcut_beings: dict` | being_id → ThreadcutState |
| 293 | `comovement_deck: dict` | `{'remaining':[], 'discard':[]}` |
| 301 | `settlements: dict` | sid → Settlement |

**MEASURED after `run_campaign(seed=42)`:** `settlements` = **37**; `beliefs` = 0; `knots` = 0;
`convictions` = 0; `practitioners` = 0; `treaties` = 0; `npcs` = 0; `insurgencies` = 0. **Nine of the
fourteen registries stay empty for the whole campaign.**

Two attributes are set **dynamically and are not dataclass fields**: `world.echo_scheduler` +
`world.key_log` + `world._echo_key_seq` (`mc_v18.py:251/257/258`), `world.dispatch_combat_bridge`
(`mc_v18.py:245`), and `world.accord_drift_probe_hits` (`accounting.py:93`).

### 4.2 `Faction` (@109–205) — every field

| Line | Field | Default |
|---|---|---|
| 111 | `name: str` | — |
| 112 | `parliamentary: bool` | `True` |
| 113–117 | `L / Sta / W / I / Mil: float` | `2.0 / 3.0 / 2.0 / 2.0 / 3.0` |
| 123 | `intel: float` | `0.0` — **ratified 2026-07-08, unread and unwritten by live code; `adjust('intel',…)` raises `KeyError` at :193 because `MULTS` has no `intel` key** |
| 124 | `territories: list` | `[]` (was a `set`; changed 2026-05-20 for hash-seed determinism) |
| 127–129 | `senator_inward_used / consul_used: bool`, `peaceful: bool`, `standing: int` | `False / False / True / 0` |
| 131–132 | `excommunicated: bool`, `council_used_this_arc: bool` | `False / False` |
| 137 | `parl_transfer_used_this_arc: bool` | `False` |
| 148 | `UNDECLARED_FLOOR = 0.5` | Fallback bound. **No faction stat reaches it any more** (all six declared) |
| 151 | `UNDECLARED_CEILING = 7.0` | |
| 230 | `descriptors.assert_faction_roster_is_covered(...)` | **Import-time, ONE-WAY** check: a registry-declared stat with no field here stops the engine importing |

### 4.3 `MULTS` and the clamp

| Line | Symbol |
|---|---|
| **74** | `MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}` — **spans TWO registry blocks (5 faction + 2 territory), which is why it stays a literal (@57–73)** |
| 76 | `ACCORD_MAP = {0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}` |
| 77 | `PT_MAP = {0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:6.5, 5:7.0}` |
| 91 | `canonical_pt(continuous_pt) -> int` — nearest-neighbour, cutoffs 1.75 / 3.25 / 4.75 / 6.0 / 6.75 |
| 36 | `canonical_accord` re-exported from `engine/substrate/canon_buckets.py` (moved 2026-07-29, OI-52a) |

**`Faction.adjust` (@153–196) — the exact clamp:**
```
188   bounds  = descriptors.faction_bounds(stat)              # the registry is the owner
189-190 floor   = bounds[0] if bounds else UNDECLARED_FLOOR    # all six declared → 0
191-192 ceiling = bounds[1] if bounds else UNDECLARED_CEILING  # all six declared → 7
193   mult    = MULTS[stat]                                   # KeyError for 'intel'
195   val     = max(floor, min(ceiling, val + granular_delta / mult))
196   setattr(self, stat, val)
```
The explicit `floor` / `ceiling` parameters (@154) survive **with no live caller** (@184–186).

### 4.4 `Territory` (@233–252) — every field

`tid:str` @235 · `owner:str|None` @236 · `accord:float` @237 · `pt:float` @238 · `garrison:bool` @239 ·
`prosperity:int` @240 · `fort_level:int` @241 · `templar:bool=False` @242 · `uncontrolled_since:int|None=None` @243.
Methods: `is_uncontrolled()` @245; `adjust_accord()` @248 (`max(0.5, min(7.0, accord + Δ/MULTS['accord']))` — **hardcoded 0.5/7.0, NOT registry-read, unlike `Faction.adjust`**); `adjust_pt()` @251 (same shape).

### 4.5 serialize / restore

| Line | Function | Note |
|---|---|---|
| 355 | `serialize_world(world) -> dict` | Emits `season, arc, winner, battle_count, clocks`, 5 faction stats + 6 flags, 7 territory fields, and **all 15 registries** |
| 425 | `restore_world(snapshot) -> World` | Reconstructs via `composition.require('snapshot_state.*')` (12 roles) + `.from_dict()`. Missing keys default to empty |

### 4.6 `.adjust(` CALL-SITE CENSUS — AST-counted, non-test code only

Method: `ast.walk` over every `.py` under `engine/`, `systems/`, `tools/`, excluding `tests/` dirs and
`test_*.py`, matching `ast.Call` with `func.attr == 'adjust'`.

| Metric | Count |
|---|---|
| **Total non-test `.adjust(` call sites** | **31** |
| …writing `L` | **20** (matches `game_state.py:217`'s AST-counted claim exactly) |
| …writing `Sta` | 5 |
| …writing `W` | 4 |
| …writing `Mil` | 1 |
| …dynamic (`_stat` variable) | 1 |
| …writing `I` | **0** |
| …writing `intel` | **0** (would raise `KeyError`) |
| **Key-mediated** (inside an `apply=` closure or a function that emits a Key for this write) | **1** |
| **Direct, unmediated state writes** | **30** |

The single Key-mediated site is `engine/cross_scale/echo_transport.py:455`
(`f.adjust(_stat, _delta * MULTS[_stat])`), inside the `_apply` closure defined at `:441` and handed to
`sched.emit(key, apply=_apply)` at **`:457`**. Verified by AST enclosing-function analysis, not by proximity.

The two other production `sched.emit` sites emit **log-only** Keys with **no `apply=`**, so they move
no state and their sibling `.adjust(` calls are NOT Key-mediated:
- `systems/factions/sim/parliamentary_transfer.py:242` in `_emit_public_governance_transfer`; its
  `.adjust(` calls at `:366/:376/:384` are in `propose_transfer`, a different function.
- `systems/factions/sim/faction_action.py:425` in `_emit_battle_concluded`; its `.adjust(` calls at
  `:498/:546/:555/:579` are in `_try_conquest` / `_try_muster` / `_try_govern`.

| Full site list | stat |
|---|---|
| `engine/cross_scale/echo_transport.py:455` | dynamic `_stat` — **Key-mediated** |
| `systems/factions/sim/absolution.py:72 / :78 / :81` | L, Sta, Sta |
| `systems/factions/sim/council_solmund.py:71 / :78 / :84` | L, L, L |
| `systems/factions/sim/crown_initiative.py:91 / :97 / :106 / :161 / :166 / :171 / :174 / :246 / :253 / :261` | W, L, L, W, L, L, L, W, L, L |
| `systems/factions/sim/excommunication.py:141 / :158 / :180 / :181` | L ×4 |
| `systems/factions/sim/faction_action.py:498 / :546 / :555 / :579` | L, W, Mil, Sta |
| `systems/factions/sim/parliamentary_action.py:157 / :158` | Sta, L |
| `systems/factions/sim/parliamentary_transfer.py:366 / :376 / :384` | L, Sta, L |
| `systems/social_contest/sim/parliamentary_vote.py:214` | L |

**Territory writes, separately (AST-counted, 5 non-test sites, ALL direct / none Key-mediated):**
`crown_initiative.py:103`, `crown_initiative.py:111`, `faction_action.py:513`, `faction_action.py:524`,
`faction_action.py:577` — all `adjust_accord`. **Zero non-test `adjust_pt` call sites.**

**Raw `.accord =` assignments (bypassing `adjust_accord` entirely):**
`systems/factions/sim/mass_seizure.py:296` and `systems/factions/sim/parliamentary_transfer.py:346`,
both `t.accord = ACCORD_MAP[tier]`. **`mass_seizure.py` is never imported by a campaign** (§7.5), so
only one of the two executes.

---

## 5. PERSONS — THE THROUGHLINE

### 5.1 `systems/world/sim/npe.py` (414 lines)

| Line | Symbol | Value / contract |
|---|---|---|
| 51–53 | `DEVIATION_DIE_THRESHOLD=5`, `DEVIATION_DIE_MAX=6`, `DEVIATION_ARC_VECTOR_THRESHOLD=5` | d6; on 5–6 one axis flips; ≥5 also makes the NPC an **arc vector** |
| 57–62 | `PIETY_HIGH=4 / PIETY_LOW=1 / ACCORD_HIGH=4 / ACCORD_LOW=1 / PROSPERITY_HIGH=4 / PROSPERITY_LOW=1` | Ecology thresholds |
| 66–71 | `STANCE_MIN=1 / STANCE_MAX=5 / VOLATILITY_MIN=1 / VOLATILITY_MAX=5 / LOYALTY_MIN=0 / LOYALTY_MAX=3` | Axis bounds |
| 76 | `FACTION_DEFAULT_WEIGHT_PCT = 60` | Controlling faction is the default for 60% |
| **91** | `CONVICTIONS = descriptors.CONVICTIONS` | **READ, NOT DECLARED** — owner is `references/descriptor_registry.yaml:conviction_roster` (13 names). @82–89 records that the eight hardcoded names it replaced included five that appear in no taxonomy |
| 96 | `COMPROMISE_CATEGORIES = ("Economic","Informational","Political","Personal","Nothing")` | |
| 99–100 | `ACTIVE_ISSUES = ("Thread reality","Church authority","Altonian threat","RM legitimacy","Varfell autonomy")` | 5 issues |
| **106–107** | `_npcs_by_territory: dict = {}` · `_npc_counter = [0]` | **THE MODULE-LEVEL STANCE STORE** — the fallback when `world is None` |
| 110–113 | `_npc_store(world)` | Router: `world.npcs` if `world` has it, else the module dict |
| **116–122** | `_next_npc_id(world)` | Increments `world.npc_counter` (or `_npc_counter[0]`) and **returns the post-increment value**, so the first NPC is `NPC-00001` |

**`NPC` dataclass (@125–175) — every field:**

| Line | Field | Default | Axis |
|---|---|---|---|
| 128 | `npc_id: str` | — | id |
| 129 | `territory_id: str` | — | id |
| 131 | `stance: dict[str,int]` | `{}` | 1 (per active issue, 1–5) |
| 133 | `worldview: list[str]` | `[]` | 2 (1–2 convictions) |
| 135 | `affiliation_faction: Optional[str]` | `None` | 3 |
| 136 | `affiliation_loyalty: int` | `1` (0–3) | 3 |
| 137 | `hidden_allegiance: Optional[str]` | `None` | 3 |
| 139 | `compromise_category: str` | `"Economic"` | 4 |
| 141 | `volatility: int` | `3` (1–5) | 5 |
| 143 | `deviation_roll: int` | `0` | provenance |
| 144 | `is_arc_vector: bool` | `False` | provenance |
| 145 | `persistent_state: dict` | `{}` | persistence |

`to_dict()` @147, `from_dict()` @161. `NPCAction` @178–183: `npc_id / action_type / season / details`.

| Line | Function | Contract |
|---|---|---|
| 186 | `_ecology_weights(world, territory_id)` | Buckets `t.accord` through `canonical_accord` (@200) before comparing — @195–199 records the drift bug this fixes. **@209–210: Territory has no piety field; prosperity is used as a proxy, flagged as an approximation** |
| **226** | `generate_npc(faction, role, world, territory_id=None, rng=None)` | Tier 1 archetype @253–287; Tier 2 deviation @289–333; id assigned @335–337 as `f"NPC-{n:05d}"`; **@348–349 appends to the store** |
| 292–333 | deviation branch | `flip_choice = rng.randint(0,4)` → 0 stance flip · 1 worldview redraw (**uniform over the other twelve — the old `opposites` map was a roster leak, @302–320**) · 2 hidden allegiance · 3 compromise→"Nothing" · 4 volatility extreme |
| **353** | `simulate_npc_actions(world) -> list[NPCAction]` | Pairwise, same-territory, shared-worldview, adjacent-stance drift. `avg_vol = (a.volatility+b.volatility)/2` @384; `rng.randint(1,6) <= avg_vol` @385; both shift 1 toward each other @388–393 |
| 403 | `get_npcs_in_territory(territory_id, world=None)` | |
| 408 | `reset_npcs(world=None)` | Test helper |

**Where `simulate_npc_actions` is called from:** exactly one production site —
**`systems/overview/sim/accounting.py:139`**, unconditional, every season. (Three surfaces cite this
as `accounting.py:78-82`; that is stale — see §10.)

**Where `generate_npc` is called from: NOWHERE in production.** Search:
`grep -rn "generate_npc" --include=*.py engine/ systems/ tools/` → the definition at `npe.py:226`,
docstring mentions at `npe.py:23/:29`, and the `stubwire` deferral text in `mc_v18.py:195`. The
consequence is measured: `npcs_generated == 0` in every campaign.

### 5.2 `engine/autoload/npc_ai.py` (47 lines) — STUB

| Line | Symbol | State |
|---|---|---|
| 6 | `Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 …]` | |
| 19 | `from engine.substrate import stubwire` | The **only** import in the module |
| **33** | `def select_action(actor_id: str, world: GameState):` | **THE EXACT DECLARED SIGNATURE.** ⚠ `GameState` is **never imported** — `from __future__ import annotations` (@17) defers evaluation, so the module imports cleanly, but `typing.get_type_hints(select_action)` raises `NameError: name 'GameState' is not defined` (executed and verified this pass) |
| 34–38 | body | `stubwire.stub_resolve('engine.autoload.npc_ai', 'select_action(actor_id: str, world: GameState) -> Action', reason='Pass 2l armature stub … OI-17, ED-IN-0091 plan §2.2')` — **returns a typed no-op; there is no priority tree, no action selection, no faction AI dispatch** |
| 41 | `def evaluate_priority_stack(actor_id: str, world: GameState)` | Same shape, same stub |

**`npc_ai` is never imported by a campaign.** Verified by `sys.modules` inspection after
`run_campaign(seed=42)`: `engine.autoload.npc_ai` is absent from the 89 loaded `engine.*`/`systems.*`
modules.

### 5.3 `engine/mc_v18.py` (348 lines) — the stubwire deferrals and the population

| Line | Item | Contract |
|---|---|---|
| 100 | `npcs_generated: int = 0` | `CampaignResult` field — "F7 telemetry: `world.npc_counter` (generate_npc call-count proxy)" |
| 101 | `stub_hits: int = 0` | Per-campaign delta of `stubwire.invocations` |
| 124 | `def _faction_actions_callback(world)` | The ACTION-phase body handed to `run_tick` |
| 149–150 | `scene_dispatch.run_scene_phase(world, world.rng)`; `world.scenes_resolved += …` | The scale seam |
| 156–160 | parliamentary bridge, gated on `world.echo_scheduler is not None` | |
| 162–168 | comment | Records that `accounting_boundary()` / `next_tick()` **MOVED OUT** to `engine_clock.run_tick` on 2026-08-27 |
| **194–202** | `stubwire.stub_resolve('engine.mc_v18', 'generate_npc(world-gen\|season-tick)', reason=…)` | **DEFERRAL 1** — no world-gen count and no season-tick trigger exists in canon to cite |
| **212–217** | `stubwire.stub_resolve('engine.mc_v18', 'form_knot(world-gen\|season-tick)', reason=…)` | **DEFERRAL 2** — `knots_v30 §3.1` prerequisites (Disposition, Bonds, TS) are personal-scale fields absent from the aggregate World |
| 230 | `_stub_start = stubwire.invocations` | Snapshot for the delta |
| 268–278 | the season loop | `for _ in range(max_s): … composition.require('season_driver')(world, action_callback=_faction_actions_callback)` |
| 310 | `npcs_generated=world.npc_counter` | |
| 311 | `stub_hits=stubwire.invocations - _stub_start` | |

**MEASURED (seed 42, default 50 seasons):** `stub_hits = 100` = exactly the two deferrals × 50 seasons.
`world.npcs` is **empty for the entire campaign**; `npcs_generated = 0`.

### 5.4 Tests that pin `npcs == 0`

| File:line | Assertion | Kind |
|---|---|---|
| `engine/tests/test_f7_smoke_oracle.py:371` | `assert npcs == 0, "npcs_generated is no longer 0 …"` (sum over the n=8 seed-42 batch) | golden guard |
| `engine/tests/test_world_population.py:152` | `assert r.npcs_generated == 0` after `run_campaign(seed=1, max_seasons=5)` | honest-deferral guard |
| `engine/tests/test_pipeline_reach.py:626–629` | `@pytest.mark.xfail(strict=True, …)` on `assert r.npcs_generated > 0` | **strict xfail — asserts the population is STILL empty, from the other direction** |
| `engine/tests/test_world_population.py:132–139` | `assert 'simulate_npc_actions(world)' in inspect.getsource(accounting.run_accounting)` | source-text guard that the drift half stays wired |

---

## 6. COMPOSITION AND SEAMS

### 6.1 `engine/substrate/composition.py` (69 lines)

| Line | Symbol | Contract |
|---|---|---|
| 21–23 | docstring | **IT IS A LEAF** — stdlib only, no `engine.*` / `systems.*` module-level imports |
| 27–29 | `import importlib, json, os` | The whole import list |
| 31–32 | `_PATH = …/engine/engine_params/composition.json` | The **cooked** artifact (written by `tools/export_composition.py`, blocking `--check`) |
| 34–35 | `with open(_PATH) as _fh: _DATA = json.load(_fh)` | **Loaded at import time** — a missing/corrupt artifact fails the import, not a campaign |
| **38** | `ROLES = _DATA['roles']` | `{role → {target, kind, needed_by}}` |
| 40 | `_CACHE = {}` | Resolution happens once per role per process |
| **43** | `def require(role)` | **How a role resolves:** @66 `mod_name, attr = row['target'].split(':', 1)`; @67 `fn = getattr(importlib.import_module(mod_name), attr)`; @68 cache; @69 return |
| 59–65 | missing-role branch | **Raises `KeyError` — deliberately NOT `get(role, default)`**, so a campaign can never run with a subsystem quietly absent |

### 6.2 `references/module_contracts.yaml#composition_roles` — **27 roles**, parsed with `yaml.safe_load`

| # | Role | Target | Kind |
|---|---|---|---|
| 1 | `faction_action` | `systems.factions.sim.faction_action:faction_take_action` | callable |
| 2 | `season_driver` | `systems.overview.sim.season:run_season` | callable |
| 3 | `accounting` | `systems.overview.sim.accounting:run_accounting` | callable |
| 4 | `parliamentary_vote` | `systems.social_contest.sim.parliamentary_vote:run_parliamentary_vote` | callable |
| 5 | `parliamentary_motion` | `systems.social_contest.sim.parliamentary_vote:Motion` | callable |
| 6 | `parliamentary_vote_declaration` | `systems.social_contest.sim.parliamentary_vote:VoteDeclaration` | callable |
| 7 | `territory_transfer_candidate` | `systems.factions.sim.parliamentary_transfer:derive_transfer_candidate` | callable |
| 8 | `territory_transfer_proposal` | `systems.factions.sim.parliamentary_transfer:propose_transfer` | callable |
| 9 | `world_gen_settlements` | `systems.settlements.sim.registry:populate_from_geography` | callable |
| 10 | `snapshot_state.practitioners` | `systems.threadwork.sim.coherence:CoherenceState` | callable |
| 11 | `snapshot_state.insurgencies` | `systems.world.sim.insurgency_pipeline:InsurgencyRecord` | callable |
| 12 | `snapshot_state.npcs` | `systems.world.sim.npe:NPC` | callable |
| 13 | `snapshot_state.treaties` | `systems.factions.sim.treaty:TreatyRecord` | callable |
| 14 | `snapshot_state.convictions` | `systems.characters.sim.conviction:ConvictionState` | callable |
| 15 | `snapshot_state.beliefs` | `systems.characters.sim.beliefs:Belief` | callable |
| 16 | `snapshot_state.knots` | `systems.fieldwork.sim.knots:Knot` | callable |
| 17 | `snapshot_state.territory_infrastructure` | `systems.settlements.sim.infrastructure:InfrastructureState` | callable |
| 18 | `snapshot_state.threadcut_beings` | `systems.threadwork.sim.threadcut:ThreadcutState` | callable |
| 19 | `snapshot_state.settlements` | `systems.settlements.sim.registry:Settlement` | callable |
| 20 | `scene_resolver.combat` | `systems.combat.sim.combat:resolve_combat_round` | callable |
| 21 | `scene_resolver.contest` | `systems.social_contest.sim.contest:resolve_contest` | callable |
| 22 | `scene_builder.contest` | `systems.social_contest.sim.contest:build_contest` | callable |
| 23 | `contest_side.a` | `systems.social_contest.sim.contest:A` | **value** |
| 24 | `contest_side.b` | `systems.social_contest.sim.contest:B` | **value** |
| 25 | `scene_resolver.fieldwork` | `systems.fieldwork.sim.fieldwork:run_fieldwork_scene` | callable |
| 26 | `scene_resolver.investigation` | `systems.fieldwork.sim.investigation:resolve_npe_response` | callable |
| 27 | `rs_track_delta` | `systems.overview.sim.rs_track:apply_rs_delta` | callable |

**Only 5 roles are resolved during a default campaign:** `season_driver`, `accounting`,
`faction_action`, `world_gen_settlements`, plus the contest builder/resolver pair. The 10
`snapshot_state.*` roles resolve only inside `restore_world`, which no campaign path calls.

### 6.3 `engine/cross_scale/combat_bridge.py` — THE PATH SEAM

| Line | Symbol | Contract |
|---|---|---|
| 81–83 | `_COMBAT_ENGINE_V1_DIR = <repo>/systems/combat/combat_engine_v1` | Computed from `__file__` |
| 85 | `_engine = None` | Memo slot |
| **88–100** | `_load_engine()` | @94 `import sys`; @95–96 **`sys.path.insert(0, _COMBAT_ENGINE_V1_DIR)`**; @97 **`import combatant as _combatant_mod`**; @98 **`import wrapper as _wrapper_mod`** — **BARE NAMES, no dotted package path.** LAZY and MEMOIZED: `import combat_bridge` never mutates `sys.path` |
| 103 | `_combatant_from_faction_mil(fid, world)` | Derives one side from `f.Mil`: `history = max(1, round(f.Mil))` @109 |
| 114 | `derive_parties(ctx, world)` | Needs `ctx['factions'] = (fid_a, fid_b)`; returns `None` on a derivation gap — **never invents a substitute** |
| 131 | `resolve(a, b, rng)` | @140 `fight_rng = _random_mod.Random(rng.getrandbits(32))`; @141 `_wrapper_mod.fight(a, b, rng=fight_rng)`. Returns `{'result':-1|0|1, 'winner', 'a_label', 'b_label', 'a_history', 'b_history'}` |

**The declaration:** `tests/valoria/test_engine_does_not_import_systems.py:212`
`PATH_SEAM_ALLOWED = {'cross_scale/combat_bridge.py'}` — **one entry, shrink-only**, asserted for exact
set equality at `:288`.

**The flag:** `mc_v18.py:78–89` `_dispatch_combat_bridge_on()` — **default OFF**
(`os.environ.get('DISPATCH_COMBAT_BRIDGE','0') == '1'`), stashed once per campaign on
`world.dispatch_combat_bridge` at `mc_v18.py:245`. **Verified: `engine.cross_scale.combat_bridge` is
NOT in `sys.modules` after a default `run_campaign(seed=42)`.**

### 6.4 `engine/cross_scale/echo_transport.py` (474 lines) — THE ONE KEY-MEDIATED WRITE LOOP

| Line | Symbol | Contract |
|---|---|---|
| 56 | `from engine.autoload.game_state import MULTS` | |
| 102 | `DEFAULT_CASCADE_DEPTH_MAX = 0` | **Depth 0 — cascading is structurally impossible in a default campaign** |
| 103 | `DEFAULT_EMISSIONS_PER_TICK_MAX = 64` | |
| 108–111 | `KEY_TYPE_BY_SCENE = {"contest": "scene.contest_resolved", "combat": "scene.combat_resolved"}` | Only the two live personal-scale resolvers are mapped |
| 114–119 | `_OUTCOME_BY_DEGREE` | contest: Overwhelming/Success→`initiator_win`, Partial→`compromise`, Failure→`target_win`; combat: →`attacker_win` / `draw` / `defender_win` |
| 124–125 | `_ACCORD_SCENE_OUTCOMES = frozenset({"governance","destabilisation","territorial_transfer","violence"})` | §5.5 closed vocabulary |
| 127–142 | correction block | The `{"combat": "violence"}` fallback was **DELETED** — the Accord leg is **WIRED but DORMANT** until a caller declares `echo['scene_outcome']` |
| 184 | `make_scheduler(cascade_depth_max=…, emissions_per_tick_max=…)` | `KeyLog(_registry())` + `TickScheduler` with `defer_apply=True`, `no_sync_reentry=True` |
| 211 | `_apply_accord_echo(...)` | The settlement-Order leg |
| 336 | `def _apply(_k, _world=world, _sid=sid, …)` | Closure over `settlement.order`, **canonical-index space, no MULTS/ACCORD_MAP conversion** (@285–295) |
| 354 | `sched.emit(key, apply=_apply)` | OF-7: settlement-Order write lands at `accounting_boundary()` |
| 371 | `emit_scene_echo(scene_type, result, ctx, world)` | The main producer |
| 421 | `if er.fires and er.affected_faction is not None and er.affected_stat is not None and er.delta != 0:` | The gate |
| 441 | `def _apply(_k, faction=…, _stat=…, _delta=…)` | **THE ONE KEY-MEDIATED FACTION-STAT WRITE** |
| **454–455** | `if f is not None and hasattr(f,"adjust") and _stat in MULTS: f.adjust(_stat, _delta * MULTS[_stat])` | ⚠ **`_stat in MULTS` IS NOT "is a faction stat"** — `MULTS` carries `accord` and `pt`, which are Territory fields, and `most_relevant_stat` is caller-supplied and unvalidated. A scene declaring `most_relevant_stat: 'accord'` passes the guard and then raises `AttributeError` inside a deferred apply. Recorded, not fixed (@445–452) |
| **457** | `sched.emit(key, apply=_apply)` | **THE producer.** The consumer is `TickScheduler.accounting_boundary()` (`keys.py:581–591`), reached from `engine_clock.py:122` |
| 458 | `_domain_echo_key_id = key.id` | Feeds `causes[]` on the Accord Key |
| 365 | `composition.require('rs_track_delta')(…)` | The §5.5 RS leg |

**WHAT IS MISSING from the loop:** the producer emits and the boundary applies, but
`schedule_emission` / `drain_tick` are **never called in production**, so a consumer that reacts to an
observed Key cannot enqueue a follow-on Key. The subscriber side exists
(`engine/cross_scale/articulation.py:168–169` registers 13 callbacks) but **every callback it registers
is for a type nothing emits** (§7.4). The observed loop is one hop deep: emit → log → deferred apply.

### 6.5 `engine/cross_scale/scene_dispatch.py` (423 lines)

| Line | Symbol | Dispatches |
|---|---|---|
| 76 | `evaluate_triggers(world)` | **Only ONE canonical §4.3.2 trigger is field-evaluable: Stability Crisis** (@81–96, `f.Sta <= 2` → an `emergency_council` contest). @97 `evaluable = {"Stability Crisis"}`; @98–99 the other 7 are **reported as deferred, not faked** |
| 103 | `queue_triggered_scenes(world)` | `scene_slate.queue_scene(...)` per fired trigger |
| 118 | `EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"` | **[SEED]** — a provisional proceeding choice |
| 217 | `_resolve_slot(slot, world, rng)` | Routes by `scene_type`: `combat` → `combat_bridge.resolve` (@239, flag ON) **or** `composition.require('scene_resolver.combat')` (@274, flag OFF); `contest` → `scene_builder.contest` + `scene_resolver.contest` (@288–301); `fieldwork` / `investigation` → **stub-wired resolvers** (@354, @356); anything else → `stubwire.stub_resolve` total-mapping fallback (@367) |
| 337–339 | `composition.require('contest_side.a' / '.b')` | The two `kind: value` roles |
| 402 | `dispatch_scenes(world, rng)` | Drains `scene_slate` to empty; returns `{dispatched, resolved, deferred}` |
| 417 | `run_scene_phase(world, rng=None)` | `queue_triggered_scenes` then `dispatch_scenes`. **Declared side-effect-free on strategic stats by construction** (@418–419) |

**MEASURED (seed 42):** `scenes_resolved = 124` over 50 seasons. **No live trigger queues a `combat`
scene** — verified in the module's own docstring (@37) and by the runtime key census (§7.4), where
`scene.combat_resolved` is emitted zero times.

---

## 7. INERT-BUT-BUILT MACHINERY (the compose-on targets)

### 7.1 `systems/settlements/sim/ledger.py` (75 lines) — correct, and its API is dead

| Line | Symbol | Contract |
|---|---|---|
| **30** | `TAG_KINDS = {"Precedent","Grudge","Debt","Reputation","Leverage"}` | §1.6 tag kinds. ⚠ **`TAG_KINDS` is never read by any function in this module or anywhere else** — search `grep -rn "TAG_KINDS" --include=*.py .` returns only this definition. `ledger_add` does **not** validate `tag.kind` against it |
| 32 | `SINGLE_VALUED = {"Reputation"}` | Latest-wins replacement set |
| 35–44 | `@dataclass LedgerTag` | `kind:str` · `key:str` · `value:float=1.0` · `created_season:int=0` · **`ttl:int\|None=None`** (`None` = durable, survives succession + sweeps). `is_expired(season)` @43: `ttl is not None and season >= created_season + ttl` |
| 47 | `ledger_add(ledger, tag)` | Dedupes by `(kind,key)`; a `SINGLE_VALUED` kind replaces any prior tag of that kind @50–53; otherwise refresh-in-place @54–57 or append @58 |
| 61 | `ledger_has(ledger, kind, key=None)` | |
| 65 | `ledger_get(ledger, kind)` | |
| 69 | `ledger_sweep(ledger, season)` | Drops expired; returns removed |

**PRODUCTION CALLERS: ZERO.** Search `grep -rn "ledger_add\|ledger_sweep\|ledger_has\|ledger_get\|LedgerTag" --include=*.py .`
→ every hit outside `ledger.py` is in `systems/settlements/sim/registry.py` (:34–35 import, :88 field,
:102/:105/:108 the `Settlement` convenience wrappers, :154 `from_dict`, :207 `succeed_governor`). Those
wrappers themselves have zero callers (§7.2). **The one unrelated hit,
`tests/valoria/test_claim_provenance_archives.py:47`, is a function named `test_every_live_ledger_has_…`
and is about the ED ledger, not this one.**

### 7.2 `systems/settlements/sim/registry.py` (267 lines)

**`Settlement` dataclass (@54–90) — every field:**

| Line | Field | Default |
|---|---|---|
| 56–59 | `sid / name / stype / province_id: str` | — |
| 60–61 | `owner_faction / governor_id: str\|None` | `None` |
| 63–67 | `prosperity / defense / order / fort_level: int`, `garrison: bool` | `0,0,0,0,False` |
| **74–75** | `legitimacy: int = 0`, `popular_support: int = 0` | §1.8 per-settlement political acceptance |
| 77–79 | `facility_tier: int=0`, `suspicion: int=0`, `pressure: float=4.0` | |
| 81–84 | `active_directive: str\|None=None`, `religious_building: str="None"`, `church_attention: int=0`, `governor_emergence: int=0` | |
| 86–90 | `subnational: dict={}`, `npc_ids: list=[]`, `ledger: list=[]`, `open_needs: list=[]`, `deck_state: dict={}` | |

| Line | Member | Contract | Callers |
|---|---|---|---|
| **92–97** | `@property ap -> int` | `2 + facility_tier + (1 if stype in ("Seat","Cathedral","Cathedral-City") else 0)` | **ZERO** |
| **100–102** | `add_tag(kind, key, value=1.0, created_season=0, ttl=None)` | delegates to `ledger_add` | **ZERO** |
| 104–105 | `has_tag(kind, key=None)` | | **ZERO** |
| 107–108 | `tags(kind)` | | **ZERO** |
| 113 / 137 | `to_dict()` / `from_dict()` | Reached via `serialize_world` / `restore_world` | serialize only |
| 199 | `succeed_governor(sid, new_governor, world=None, season=0)` | @207 `ledger_sweep(s.ledger, season)` | **ZERO** |
| 185 | `province_accord(province_id, world=None) -> int` | `floor(mean settlement order)` | `accounting.py:88` — **LIVE** |
| 181 | `province_members(province_id, world=None)` | | `accounting.py:86`, `settlement.py:176` |
| 216 | `populate_from_geography(world, path=None) -> int` | Role `world_gen_settlements`, called at `game_state.py:351` | **LIVE — 37 settlements at seed 42** |

**Are `legitimacy` / `popular_support` read or written?** Search
`grep -rn "legitimacy\|popular_support" --include=*.py .` outside `registry.py` and `tools/`:
**every hit is about `fac.legitimacy` (the FACTION descriptor), a docstring, or a test.** No code
reads or writes `Settlement.legitimacy` or `Settlement.popular_support`. The module's own comment
(@69–73) says so: *"declared but NEVER READ OR WRITTEN anywhere in sim/ … an INERT LPS-1 schema stub."*
**Confirmed still true this pass.**

### 7.3 `systems/characters/sim/beliefs.py` (245 lines)

| Line | Symbol | Declares |
|---|---|---|
| 41 | `MOMENTUM_CAP = 4` | fieldwork_v30 §5.5 |
| 46 | `BELIEF_MOMENTUM_PER_CONTEST_CAP = 1` | social_contest_v30 §9.5 |
| 49–87 | `@dataclass Belief` | `belief_id:str` · `actor:str` · `statement:str` · `position:str` ('strong'/'wavering'/'revised') · `underlying_convictions:list[str]=[]` · `revision_pressure:int=0` · `history:list[dict]=[]`; `to_dict` @60 (coerces non-serializable `evidence` to `str`), `from_dict` @78 |
| 90 | `@dataclass RevisionResult` | |
| 105 | `_store(world)` | Module-level fallback router — `World.beliefs` when supplied |
| 113 | `_find_belief(actor, belief_id, world=None)` | |
| 121 | `add_belief(actor, belief_id, statement, …)` | **the constructor** |
| 140 | `revise_belief(actor, belief_id, new_position, evidence, world)` | |
| 189 | `social_success(actor, belief_id, aligned, …)` | |
| 237 | `get_active_beliefs(actor, world=None)` | |

**Does anything construct a `Belief`?** Search
`grep -rn "sim.beliefs\|add_belief\|revise_belief\|get_active_beliefs\|Belief(" --include=*.py .`
outside `beliefs.py` → **three hits, none of them a construction on a live path:**
`systems/characters/sim/conviction.py:22` and `:268` (docstrings), and
`systems/social_contest/sim/contest_legacy_stub.py:240` (`from systems.characters.sim.beliefs import
social_success`, inside a legacy stub). Plus the `snapshot_state.beliefs` composition role, which fires
only from `restore_world`. **MEASURED: `world.beliefs` is empty after `run_campaign(seed=42)`.**
`systems.characters.sim.beliefs` is **not loaded at all** during a campaign.

### 7.4 Key types with a subscriber and no emitter — `engine/cross_scale/articulation.py` (170 lines)

| Line | Symbol | Contract |
|---|---|---|
| 35 / 44 / 53 | `render_protagonist_lens` / `evaluate_articulation_triggers` / `generate_chronicle_entry` | **All three are `stubwire.stub_resolve` no-ops.** The render layer is ED-IN-0073's docket, unbuilt |
| **116–130** | `_TRIGGER_TYPE_IDS` | **13 type ids** (verified `len == 13`): `state.scar_acquired`, `state.coup_attempted`, `state.succession`, `mechanical.mission_shift`, `da.covert_betrayal`, `meta.knot_formed`, `meta.knot_ruptured`, `env.peninsular_strain_shock`, `meta.cascade_cluster_event`, `state.belief_revised`, `scene.combat_resolved`, `scene.combat_felled`, `scene.accord_echo` |
| 133 | `_make_trigger_callback(type_id)` | Each callback is a `stubwire` flag that observes and returns, **storing nothing and rendering nothing** |
| 152–170 | `subscribe_all(scheduler) -> int` | Called from `mc_v18.py:266`. Returns 13 |

**MEASURED (seed 42, 50 seasons, ECHO_TRANSPORT on): the key log contains exactly two types —
`scene.contest_resolved` ×104 and `scene.battle_concluded` ×65 (169 total).** **None of the 13
subscribed types is ever emitted.** All 13 subscriber callbacks are dead at runtime.

### 7.5 Every non-test module NOT loaded by a seeded campaign

Method: `sys.modules` after `mc_v18.run_campaign(seed=42)`, differenced against every non-`__init__`
`.py` under `engine/` and `systems/` (excluding test dirs).

**140 modules on disk · 69 reached · 71 unreached.** Excluding the `combat_engine_v1` and
`mass_battle` internals (which the mass-battle path does reach through its own package), the
unreached list that bears on the season loop, world churn, persons or narrative:

| Module | Lines | Shape |
|---|---|---|
| `engine.autoload.npc_ai` | 47 | STUB (both entry points) |
| `engine.cross_scale.combat_bridge` | — | BUILT, flag-gated OFF |
| `systems.characters.sim.beliefs` | 245 | BUILT-INERT |
| `systems.characters.sim.conviction` | 283 | BUILT-INERT (no stubs) |
| `systems.characters.sim.companion` | — | BUILT-INERT |
| `systems.fieldwork.sim.knots` | 396 | BUILT-INERT (no stubs) |
| `systems.fieldwork.sim.fieldwork` | — | STUB (`scene_resolver.fieldwork` role target) |
| `systems.fieldwork.sim.investigation` | — | STUB (`scene_resolver.investigation` role target) |
| `systems.settlements.sim.settlement` | 204 | BUILT-INERT (no stubs) |
| `systems.settlements.sim.temperaments` | 179 | BUILT-INERT (no stubs) — owns `world.npc_drift_state` |
| `systems.settlements.sim.infrastructure` | — | BUILT-INERT (`snapshot_state.territory_infrastructure` role target) |
| `systems.world.sim.miraculous_event` | 33 | STUB (1 `NotImplementedError`, 1 `stub_resolve`) |
| `systems.world.sim.restoration_movement` | 43 | STUB (1 `NotImplementedError`, 2 `stub_resolve`) |
| `systems.overview.sim.rs_track` | 33 | STUB — **but it is the `rs_track_delta` composition-role target, called at `echo_transport.py:365`** on a path that never fires |
| `systems.overview.sim.ip_track` | — | STUB — the `IP` clock is initialised to 20.0 at `game_state.py:338` and never moves |
| `systems.factions.sim.treaty` | 164 | BUILT-INERT (`snapshot_state.treaties` role target) |
| `systems.factions.sim.mass_seizure` | — | BUILT-INERT — **writes `Territory.accord` at `:296` on a path a campaign never reaches** |
| `systems.factions.sim.charter_liberties`, `.hafenmark_equipment`, `.home_sanctuary`, `.infrastructure_reclamation`, `.varfell_mandate_action`, `.varfell_territorial_acquisition` | — | BUILT-INERT faction-unique actions |
| `systems.social_contest.sim.parliamentary_stay` | — | BUILT-INERT |
| `systems.threadwork.sim.{co_movement, coherence, collective, operations, opposing, rendering, threadcut}` | — | BUILT-INERT (3 are `snapshot_state.*` role targets) |
| `systems.combat.sim.combat` | — | **The `scene_resolver.combat` role target — never resolved, because no trigger queues a combat scene** |

---

## 8. THE GOLDENS AND CONTROLS

### 8.1 `engine/tests/test_mc_v18_regression.py` (189 lines) — seed 0, n=2

| Line | Constant | Value |
|---|---|---|
| 91 | `_SEED` | `0` |
| 92 | `_N` | `2` |
| 126 | `GOLDEN_WIN_SHARE` | `{'Crown': 50.0, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 50.0}` |
| 127 | `GOLDEN_WINNERS` | `{'Crown': 1, 'Varfell': 1}` |
| 129 | `GOLDEN_BATTLES_MEAN` | `36.0` |

Campaign length: **50 seasons** (`DEFAULT_PARAMS['CAMPAIGN_SEASONS']`; `run_batch` passes no override).
Tests: `test_mc_v18_batch_is_deterministic` @132 · `test_mc_v18_batch_matches_golden` @142 ·
`test_mc_v18_resolves_at_least_one_contest` @151 · `test_mc_v18_win_share_is_well_formed` @162 ·
`test_flag_on_resolves_at_least_one_contest` @171.
@123–125 records honestly that **only `battles_mean` moved on the last re-pin (34.5 → 36.0)** and that
at n=2 the win-share is quantised to 50pp steps, so its stability *is not evidence*.

### 8.2 `engine/tests/test_f7_smoke_oracle.py` (469 lines) — seed 42, n=8

| Line | Constant | Value |
|---|---|---|
| 51 | `_SEED` | `42` |
| 52 | `_N` | `8` |
| 53 | `_FACTIONS` | `['Crown','Church','Hafenmark','Varfell']` |
| **303** | `GOLDEN_WIN_SHARE` | `{'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 12.5, 'Varfell': 75.0}` |
| 309 | `GOLDEN_WINNERS` | `{'Crown': 1, 'Hafenmark': 1, 'Varfell': 6}` |
| 310 | `GOLDEN_BATTLES_MEAN` | `35.9` |
| 311 | `GOLDEN_SCENES_RESOLVED` | `1072` |
| 312 | `WALL_TIME_CEILING_S` | `90.0` |

Tests: `test_f7_determinism` @335 · `test_f7_golden_win_share` @344 ·
`test_f7_scenes_live_insurgency_and_npe_still_islands` @353 (`scenes == 1072` @369, `insurgencies == 0`
@370, `npcs == 0` @371) · `test_f7_hafenmark_elimination_lockout` @374 (`hafenmark_wins == 1` @413,
`flipped.winner == 'Hafenmark'` at seed 44 @436) · `test_f7_victory_threshold_is_a_dead_param` @452
(`base == hi == lo` @457, sweeping 11 → 999 → 1) · `test_f7_wall_time_ceiling` @463.

**Two docstring/constant contradictions in this file — see §10 rows C8 and C9.**

### 8.3 `tools/balance_oracle.py` (298 lines)

| Line | Item | Contract |
|---|---|---|
| 2–13 | header | Explicitly closes `test_f7_smoke_oracle.py:8`'s standing demand for an n≥100 oracle |
| 11–13 | | **"It is NOT a CI gate and must not become one — 240 campaigns take roughly 13 minutes."** |
| 15–18 | | Runs the same seeds **twice in one process**, one arm patched to the old behaviour, so the only difference between arms is the mechanic |
| 54 | `Z_THRESHOLD = 1.96` | two-sided 5% |
| 57 | `_pool_arm(round_pool: bool)` | Patches `sigma_leverage.roll_net_continuous`; returns an undo |
| 230 | `mc_v18.run_campaign(seed=base_seed + i, max_seasons=50)` | The per-campaign call |
| 261 | `--n` default `120` | campaigns **per arm** |
| 262 | `--seed` default `20260819` | |
| 140 | comment | **"NOTHING EXECUTES THIS FILE"** — no CI job, no test |
| 20–30 | first-use record | 2026-08-21 fractional-pool comparison: Church −0.8pp (z −0.21), Crown +2.5 (z +0.40), Hafenmark +1.7 (z +0.45), Varfell −3.3 (z −0.52). Nothing significant |

### 8.4 Exporters with a blocking `--check` — `.github/workflows/valoria-ci.yml`, job `validators` ("Validators (blocking)", @79–80)

| CI line | Command | Cooked artifact |
|---|---|---|
| 126 | `python3 tools/export_engine_params.py --check` | `engine/engine_params/combat_engine_v1.json` |
| 127 | `python3 tools/export_key_types.py --check` | `engine/engine_params/key_types.json` |
| 134 | `python3 tools/export_game_constants.py --check` | the writer half of the ttrpg → Godot constants bridge (its reader lives in `jordanelias/valoria-game`, **not gateable from here**) |
| 137 | `python3 tools/export_descriptors.py --check` | `engine/substrate/descriptors.py` — read at RUNTIME |
| 141 | `python3 tools/export_composition.py --check` | `engine/engine_params/composition.json` — **imports and resolves every declared target at export time** |
| 146 | `python3 tools/export_module_contracts.py --check` | the `emits:`/`consumes:` interface artifact |
| 150 | `python3 tools/export_world_initial_state.py --check` | read at import by `engine/substrate/world_initial_state.py` |

**Seven blocking exporters.** The campaign-golden job is separate: `sim-regression` @369–405,
`timeout-minutes: 20` @387 (raised from 5 on 2026-08-25 — the job **had never once completed**),
running `python -m pytest engine/tests -q` @405, measured ~6m15s, **kept serial deliberately** because
it pins seeded goldens and key-log content hashes.

---

## 9. REGISTRIES THE PORT INGESTS

### 9.1 `engine/engine_params/key_types.json` — parsed with `json.load`

| Metric | Value |
|---|---|
| Top-level keys | `_generated, schema_version, source, type_count, types` |
| Declared `type_count` | **55** |
| Actual `len(types)` | **55** (they agree; `TypeRegistry.load_json` @261–264 would raise if not) |

**Type count by family (6 families):**

| Family | Count |
|---|---|
| `scene` | 18 |
| `mechanical` | 12 |
| `state` | 10 |
| `meta` | 6 |
| `da` | 5 |
| `env` | 4 |

**Live coverage, measured:** of the 55, **16 appear as a string literal anywhere in non-test
`engine/`+`systems/`+`tools/` code**; 3 appear only in prose; **36 appear nowhere at all**. Of the 16,
**11 appear only in `articulation.py`'s subscriber tuple** and 4 have a real emitter
(`da.public_governance`, `scene.contest_resolved`, `scene.battle_concluded`, `scene.accord_echo`;
`scene.combat_resolved` is mapped but unreachable). **In an executed seed-42 campaign only 2 of 55 are
ever emitted.**

**MALFORMED / POLYMORPHIC FIELDS IN THE COOKED JSON — four, across two types:**

| Type.field | Cooked value | Should be |
|---|---|---|
| `mechanical.scene_entered.default_scale_signature` | `'[personal, territory, peninsula]   # mirrors scope'` (**str**) | list |
| `meta.cascade_cluster_event.default_scale_signature` | `'[territorial]   # peninsular when abs(similarity) > 0.95 …'` (**str**) | list |
| `meta.cascade_cluster_event.consuming_systems` | `'[articulation]        # [PROVISIONAL] …'` (**str**) | list |
| `meta.cascade_cluster_event.emitting_systems` | `'[articulation]         # [PROVISIONAL] …'` (**str**) | list |

Field-shape census across all 55: `consuming_systems` `{list:54, str:1}`; `emitting_systems`
`{list:54, str:1}`; `default_scale_signature` `{list:53, str:2}`. Every other field is monomorphic.

**Root cause and consequence, executed and verified this pass.** `TypeRegistry._parse_entry`
(`keys.py:294`) takes the flow-list branch only when `value.startswith("[") and value.endswith("]")`;
a trailing `# comment` defeats `endswith`, so the value is stored as a raw string. Then
`apply_defaults` (`keys.py:325–326`) does `key.scale_signature = list(entry["default_scale_signature"])`
— **`list()` of a string is a list of CHARACTERS**. Executed:

```
after apply_defaults, scale_signature = ['[','p','e','r','s','o','n','a', …] len 50
log.append(k) → KeyValidationError: key 'x' has non-canonical scale '[' (§2.1)
```

**Emitting a `mechanical.scene_entered` or `meta.cascade_cluster_event` Key without an explicit
`scale_signature` RAISES.** Neither type is emitted today, so it is latent — but `articulation.py`
subscribes to `meta.cascade_cluster_event`, and this is what the first emitter would hit.

### 9.2 `references/descriptor_registry.yaml` — parsed with `yaml.safe_load`

| Block | Count | Members |
|---|---|---|
| `attributes` | **9** | body: `strength, endurance, agility` · mind: `focus, acuity, will` · social: `attunement, charisma, bonds`. Scale `1-7`, default `1` |
| **THE TENTH-ATTRIBUTE BANNER** | @39–43 | *"⚠ THE COUNT IS RULED; THE ROSTER IS NOT COMPLETE. Jordan, 2026-08-14: 'it will be 10 attributes'. NINE are defined below. **The TENTH IS UNNAMED** — naming it is the open workshop … Until the tenth is named, 'IN FLUX' stays and Godot fields stay unbound."* @12 also states "9 personal attributes … IN FLUX" |
| `aggregates` | 3 | `agg.body, agg.mind, agg.social` — all `status: placeholder`, not wired |
| **`conviction_roster`** | **13** | `Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor`. `count: 13` declared and matches. Source: `conviction_taxonomy_v30.md §2` |
| `faction_stats` | **6** | `fac.influence, fac.legitimacy, fac.wealth, fac.military, fac.intel, fac.stability`. Note: *"Mandate remains a size-weighted derived aggregate … NOT a base attribute and NOT the same thing as `fac.legitimacy`"* |
| `territory_stats` | 1 | `terr.fort_level` |
| `settlement_stats` | 6 | `set.legitimacy, set.popular_support, set.prosperity, set.defense, set.order, set.facility_tier` |
| `practitioner_stats` | 2 | `prac.thread_sensitivity, prac.tps` |
| `category_b_scalars` | 8 | `pc.wounds, pc.poise, pc.initiative, prov.turmoil, set.accord, fac.coup_posture, fac.succession_status, clock.season_counter` |
| `not_descriptors` | derived_values 21 · tracks 7 · clocks 4 · pools 8 | |
| `by_reference` | 7 | |
| `deprecated` | 1 | |

### 9.3 `references/module_contracts.yaml` — parsed with `yaml.safe_load`

| Metric | Parsed value | Naive-grep value | Note |
|---|---|---|---|
| `modules` | **27** (a LIST, not a dict) | — | |
| `doc: null` | **9** | `grep -c "doc: null"` → **10** | **The tenth grep match is inside a quoted prose string, not a module field.** The nine: `audit, domain_actions, engine_clock, game_director, npc_memory, scenario_authoring, scene_slate, scene_timer, settlement_economy` |
| `composition_roles` | **27** | — | Listed in full at §6.2 |
| `[ASSUMPTION]`-grade resolvers | **11** | | ⚠ **`yaml.safe_load` returns ZERO** — the tag lives in a YAML **comment** on each `resolver:` line, which the parser discards. The correct method is `grep -cE "^\s+resolver:.*\[ASSUMPTION\]"` → **11**, at lines 210, 287, 386, 419, 471, 835, 877, 1024, 1169, 1206, 1233. (A twelfth `resolver:` field is `None`.) **This is the one count on this page where grep is right and the parser is wrong; both methods are recorded so neither is repeated blind.** |

**Note on `engine_clock`:** it is one of the nine `doc: null` modules, and it is also now a real,
executing module (`engine/autoload/engine_clock.py`, §1.1). The registry row has not caught up.

---

## 10. CONTRADICTION TABLE

Each row: two surfaces that disagree, both cited, verified this pass.

### A. Docstrings/comments that contradict their own module's live constant or line

| # | Claim (citation) | Live fact (citation) |
|---|---|---|
| **C1** | `engine/autoload/engine_clock.py:16` — *"**Line 103** below calls it raw."* | The raw `composition.require('accounting')(world)` is at **`engine_clock.py:123`**. Line 103 is inside the `run_tick` docstring |
| **C2** | `engine/autoload/sigma_leverage.py:292` — *"`dice_engine.continuous_engine_sample` has always accepted a fractional pool and says so at **`dice_engine.py:92`**"* | The "Pool may be fractional" line is **`dice_engine.py:214`**. Line 92 is a comment about band-extension power |
| **C3** | `engine/cross_scale/echo_transport.py:458` — *"now genuinely in-log (**keys.py:325**)"* | `self.log.append(key)` is **`keys.py:567`**. Line 325 is inside `TypeRegistry.apply_defaults` |
| **C4** | `engine/cross_scale/articulation.py:63` — *"`TickScheduler.subscribe` (**engine/substrate/keys.py:447**)"*, and `:163` — *"**keys.py:447-448** appends to a list"* | `subscribe` is **`keys.py:506–507`**. Line 447 is inside `KeyLog._check_stat_vocabulary` |
| **C5** | `systems/world/sim/npe.py:28`, `engine/mc_v18.py:177`, `engine/tests/test_world_population.py:133` — all three cite *"**accounting.py:78-82**"* as where `simulate_npc_actions` is wired | The call is **`accounting.py:139`**. Lines 78–82 are inside `_probe_province_accord_drift`'s docstring. **Three surfaces carry the same stale citation** |
| **C6** | `systems/overview/sim/accounting.py:33` and `:66–67` — *"`Territory.accord` … written DIRECTLY by **`parliamentary_transfer.py:210`** and **`mass_seizure.py:295`**"* | The writes are **`parliamentary_transfer.py:346`** and **`mass_seizure.py:296`**. `:210` is off by 136 lines and lands in a docstring |
| **C7** | `engine/cross_scale/articulation.py:86–87` — *"**All 10** §3.1 type_ids are therefore subscribed"* | `_TRIGGER_TYPE_IDS` (`:116–130`) has **13** entries; `subscribe_all`'s own docstring at `:158` says 13. The "10" is a stale pre-W3 sentence left standing beside the correction that supersedes it |
| **C8** | `engine/tests/test_f7_smoke_oracle.py:16` — *"The n=8 seed-42 golden win-share **{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}**"* | The live constant at **`:303`** is `{'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 12.5, 'Varfell': 75.0}`. **A docstring stating a golden its own module no longer holds** |
| **C9** | `engine/tests/test_f7_smoke_oracle.py:24` — islands are *"**C-EMERGE-5/6**"* | Same file, `:361` — *"**C-EMERGE-4/5**"*. Two IDs for the same pair, in one file |
| **C10** | `engine/tests/test_f7_smoke_oracle.py:311` comment — the `GOLDEN_SCENES_RESOLVED` history reads *"975 → 1072 (ED-SC-0031); 862 → 858 … → 947 … → **967** (roster rulings, 08-23)"* | The live value is **`1072`**. The comment's chain terminates at 967, so the comment's own last entry contradicts the constant it annotates |
| **C11** | `engine/substrate/__init__.py:23` — *"campaign-loop wiring: PR-2 scope (flag-gated), **not this module**"*, listed under **"Deliberately NOT implemented"** | The campaign loop IS wired: `mc_v18.py:249–266` attaches the scheduler, log and subscribers. The item is done and the list is stale |
| **C12** | `engine/tests/test_f7_smoke_oracle.py:8` — *"no balance claim without an oracle + n ≥ 100"*, echoed as an absence at `engine/tests/test_mc_v18_regression.py:97` (*"an n≥100 oracle that still does not exist"*) | **`tools/balance_oracle.py` has existed since 2026-08-21** and its own header (`:4`) cites `test_f7_smoke_oracle.py:8` as the line it closes. `CLAUDE.md §7` already carries this correction; the two test files do not |
| **C13** | `engine/autoload/npc_ai.py:2` header — *"`sim/autoload/npc_ai.py`"*; `:9–10` Dependencies — *"`sim/autoload/game_state`, `systems/factions/sim/faction_action`"* | `sim/` was retired 2026-07-21, and the module's **only** import is `from engine.substrate import stubwire` (`:19`). It depends on neither named module. (`dice_engine.py:3` and `sigma_leverage.py:3` both fixed this same header defect on 2026-08-27; `npc_ai.py` was missed) |

### B. Declared-but-unreachable fields, parameters and API

| # | Declared | Why unreachable |
|---|---|---|
| **C14** | `engine/mc_v18.py:220` — `def run_campaign(seed=None, **max_seasons: int = 50**, params=None)` | **DEAD PARAMETER.** `:239` reads `max_s = effective_params.get('CAMPAIGN_SEASONS', max_seasons)` and `DEFAULT_PARAMS` (`:51`) *always* supplies `CAMPAIGN_SEASONS: 50`, so the fallback is never taken. **Executed: `run_campaign(seed=42, max_seasons=3)` runs 50 seasons; `run_campaign(seed=42, params={'CAMPAIGN_SEASONS':3})` runs 3.** `engine/tests/test_world_population.py:151` passes `max_seasons=5` and silently gets 50 |
| **C15** | `engine/autoload/game_state.py:123` — `Faction.intel: float = 0.0`, ratified 2026-07-08 | `MULTS` (`:74`) has no `intel` key, so `adjust('intel', …)` raises `KeyError` at `:193` before any bound is consulted. `descriptors.faction_bounds('intel')` returns `(0,7)` that no code path can reach. **0 of 31 `.adjust(` sites write it** |
| **C16** | `engine/autoload/game_state.py:264` — `World.scenes_resolved` | **Written every season** (`mc_v18.py:150`, `:160`) but **absent from `serialize_world` (`:365–422`) and from `restore_world` (`:425–513`)**. A save/restore round-trip silently zeroes it. Same for `Faction.intel`, `Faction.peaceful`, `Faction.senator_inward_used`, `Faction.consul_used` and `Territory.uncontrolled_since` |
| **C17** | `systems/settlements/sim/ledger.py:30` — `TAG_KINDS` | Never read. `ledger_add` (`:47`) does not validate `tag.kind` against it. `grep -rn "TAG_KINDS" --include=*.py .` → the definition only |
| **C18** | `systems/settlements/sim/registry.py:92/100/104/107/199` — `Settlement.ap`, `.add_tag`, `.has_tag`, `.tags`, `succeed_governor` | **Zero callers anywhere.** `grep -rn "add_tag\|succeed_governor\|has_tag\|\.tags(" --include=*.py .` → the definitions plus three unrelated hits in `tools/tag_normalizer.py` and its test |
| **C19** | `systems/settlements/sim/registry.py:74–75` — `Settlement.legitimacy`, `.popular_support` | **Never read or written by any code.** Only reached via `to_dict`/`from_dict` |
| **C20** | `engine/autoload/npc_ai.py:33/:41` — `world: GameState` | **`GameState` is never imported.** `typing.get_type_hints(select_action)` raises `NameError` (executed). **The same phantom annotation appears in 14 other modules** (AST-scanned): `articulation.py:35`, `ip_track.py:29`, `rs_track.py:28`, `restoration_movement.py:30`, `miraculous_event.py:28`, `altonian_reinforcements.py:20`, `varfell_territorial_acquisition.py:42`, `home_sanctuary.py:29`, `infrastructure_reclamation.py:29`, `charter_liberties.py:27`, `varfell_mandate_action.py:40`, `rendering.py:29`, `investigation.py:30`, and `fieldwork.py:38` (`FieldworkScene`). **Two of these — `fieldwork.py` and `investigation.py` — are composition-role targets `scene_resolver.fieldwork` / `.investigation`** |
| **C21** | `engine/mc_v18.py:61` — `DEFAULT_PARAMS['VICTORY_THRESHOLD'] = 11` | **A dead param copy, deliberately kept.** The live gate is `engine/autoload/victory.py:27` `VICTORY_THRESHOLD = 15`. `test_f7_smoke_oracle.py:452` sweeps 11 → 999 → 1 and asserts **no outcome moves** |
| **C22** | `engine/autoload/season_manager.py:48` — `check_arc_boundary(season)` | **Zero callers.** The live arc check is the inline `world.season % SEASONS_PER_ARC == 1` at `:36` — the same rule, written twice |
| **C23** | `engine/autoload/game_state.py:248/251` — `Territory.adjust_accord` / `adjust_pt` | Clamp to **hardcoded `0.5` / `7.0`**, while `Faction.adjust` (`:188`) reads `descriptors.faction_bounds()`. Territory bounds are not registry-owned. Also: **`adjust_pt` has zero non-test callers** |

### C. Declared consumer with no emitter · declared emitter with no consumer

| # | Consumer / emitter | The gap |
|---|---|---|
| **C24** | `engine/cross_scale/articulation.py:116–130` subscribes to **13** key types | **None of the 13 is emitted by any code path.** Measured over a seed-42 50-season campaign, the log holds only `scene.contest_resolved` (104) and `scene.battle_concluded` (65) — neither is in the roster. All 13 callbacks are dead |
| **C25** | `engine/engine_params/key_types.json` registers **55** types | **36 appear nowhere in non-test code at all**; 3 appear only in prose. **2 of 55 are emitted at runtime** |
| **C26** | `engine/substrate/keys.py:525` `schedule_emission` and `:538` `drain_tick` | **Zero production callers.** `engine_clock.run_tick` calls `accounting_boundary()` and `next_tick()` but never `drain_tick()`. Compounding this: `echo_transport.py:102` sets `DEFAULT_CASCADE_DEPTH_MAX = 0`, so a `schedule_emission` issued during a drain would raise `TerminationBreach` at `keys.py:531–535` before it queued. **The B1 cascade path is doubly inert** |
| **C27** | `references/module_contracts.yaml` declares `scene_resolver.combat` → `systems.combat.sim.combat:resolve_combat_round`, and `echo_transport.py:110` maps `"combat" → "scene.combat_resolved"` | **No live trigger ever queues a `combat` scene.** `scene_dispatch.py:37` states it; the runtime census confirms `scene.combat_resolved` is emitted zero times. Both the resolver role and the bridge are unreachable from the trigger side |
| **C28** | `composition_roles.rs_track_delta` → `systems.overview.sim.rs_track:apply_rs_delta`, called at `echo_transport.py:365` | `rs_track.py` (33 lines) is a **`stub_resolve` no-op**, AND `systems.overview.sim.rs_track` is **never imported by a campaign** — the §5.5 Accord leg that would call it is DORMANT (`echo_transport.py:136–139`: it needs a caller-declared `echo['scene_outcome']` that nothing declares) |
| **C29** | `composition_roles.scene_resolver.fieldwork` / `.investigation` | Both targets are `stubwire` no-ops and neither module is loaded by a campaign |
| **C30** | 10 `snapshot_state.*` composition roles (`game_state.py:458–511`) | Reached **only** from `restore_world`, which **no campaign path calls**. `serialize_world` runs every campaign (`mc_v18.py:318`); its inverse never does |
| **C31** | `systems/factions/sim/mass_seizure.py:296` writes `Territory.accord` — cited by `accounting.py:33` as one of two live write paths | **`systems.factions.sim.mass_seizure` is never imported by a campaign.** Only `parliamentary_transfer.py:346` executes. The drift probe measures 342 divergences against a single live writer |
| **C32** | `systems/world/sim/insurgency_pipeline` is imported and called every season (`accounting.py:125`, `:132–133`) | **`insurgencies_formed == 0`** in every campaign — `test_f7_smoke_oracle.py:370` pins it. A live consumer with an emitter that never fires |

### D. Cross-document contradictions against `CLAUDE.md`

| # | `CLAUDE.md` claim | Verified fact |
|---|---|---|
| **C33** | §6 — *"9/27 modules have `doc: null`"* (with the inline correction that a naive grep returns 10) | **CONFIRMED CORRECT** by `yaml.safe_load`: 9. The correction holds |
| **C34** | §6 — *"11/27 resolvers are `[ASSUMPTION]`-grade"* | **CONFIRMED CORRECT — but only by grep.** `yaml.safe_load` returns **0**, because the tag lives in a YAML comment. This is the inverse of the `doc: null` case and the method note must not be applied blindly |
| **C35** | §6 — *"`data_serialization_spec.md` ships wrong schemas (… 34 vs 35 settlements)"* | The live count is **37** (`len(final_state['settlements'])` after `run_campaign(seed=42)`), from `populate_from_geography`. Both figures in the CLAUDE.md sentence are stale |
| **C36** | §5 — *"read the capture [`params_tables.yaml`]"*, with the 2026-08-24 warning that its Degrees-of-Success bands are pre-ruling | **CONFIRMED.** `dice_engine.py:254–261` carries the same warning at the owner. The live ladder is margin-based (`dice_engine.py:279–294`); the capture holds `Net ≥ 2×Ob` / `Net ≤ 0` |

---

## APPENDIX — reproduction commands

```bash
# Runtime module reachability + key-type census
python3 -c "
import sys; sys.path.insert(0,'.')
from engine import mc_v18
r = mc_v18.run_campaign(seed=42)
print(r.winner, r.season, r.keys_emitted, r.scenes_resolved, r.npcs_generated, r.stub_hits)
print(sorted(m for m in sys.modules if m.startswith(('engine.','systems.'))))
"

# .adjust( call-site census (AST, non-test)
#   -> 31 total, 20 on L, 1 Key-mediated

# Structured counts
python3 -c "import json; d=json.load(open('engine/engine_params/key_types.json')); print(d['type_count'], len(d['types']))"
python3 -c "import yaml; d=yaml.safe_load(open('references/module_contracts.yaml')); print(len(d['modules']), len(d['composition_roles']))"
grep -cE '^\s+resolver:.*\[ASSUMPTION\]' references/module_contracts.yaml   # 11 — comments, invisible to the parser

# Absence proofs
grep -rn "def derive_ob" --include=*.py .          # 0
grep -rn "derive_ob"     --include=*.py .          # 0
grep -rn "drain_tick"    --include=*.py engine/ systems/ tools/   # definition + docstring only
```
