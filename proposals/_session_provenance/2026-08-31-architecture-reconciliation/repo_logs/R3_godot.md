# R3 — godot/ : the port, the contracts, and the version

All paths relative to repo root `/home/user/ttrpg`. Repo is a **shallow clone** (98 commits visible;
`git log --all` for `references/ecosystem_versions.yaml` returns nothing even though it is cited —
noted where it matters, section 5).

---

## 1. `godot_conversion_strategy_v1.md` — architecture, in full, with line numbers

File is 230 lines. Status line 2: `**2026-06-10 · status: PROPOSED (Jordan-vetoable throughout) · scope: both repos**`.

- **Section 0 (lines 9-20), verdict.** Three legs drifting apart: ttrpg design corpus (ahead), `valoria-game`
  (frozen since 2026-05-04 *as of this doc's writing* — see section 5 below, now stale), Python `sim/`
  armature (retired 2026-07-21, now `engine/`+`systems/<sub>/sim/`, per CLAUDE.md corrections
  inline in the doc's own restored sections — the strategy doc itself was never corrected for this).
  **Line 19**, the single most load-bearing sentence: *"the Key substrate is already the conversion
  architecture. Save state = initial conditions + Key log; replay = deterministic re-execution
  (key_substrate §1, §6); §4.1 defines the only state-mutation path; §8.8 already maps it to Godot
  (Key→Resource, registry→autoload, KEY_LOG→typed-array Resource, CAUSAL_GRAPH→sparse dict-of-sets,
  save=serialize the log)."*
- **PART I (23-51), inventory.** I.1 Keys/value taxonomy/actor model/Descriptor Registry (25-29). I.2
  kernel: one resolver, 3 probabilistic regimes + 2 non-probabilistic + armature dot-product = 5
  resolver archetypes (31-33). I.3 module-contract layer, 27 modules (35-38). **Line 41**: hook gates,
  CI, and — critically — *`ecosystem_versions.yaml` pins **Godot 4.6** + model/tokenizer* (see section 5).
  I.5 extraction artifacts (43-44). I.6 Python reference engines (46-50).
- **PART II (54-90), the 27-module conversion table.** Lines 58-86 is the full table (module / resolver
  / scales / VG home / wave / notes). **Lines 75-77** are rows 16-18: `personal_combat` (resolver
  `dice_pool`), `social_contest` (`dice_pool`), `mass_battle` (`dice_pool`) — **see section 9, this
  disagrees with the CURRENT `references/module_contracts.yaml`, which has `personal_combat`
  resolver = `d_sigma`**, not `dice_pool` (verified section 4 below). Row 27 `campaign_architecture` is
  **R** (retire, reclassified as a consolidation doc).
- **PART III (94-116), the Godot repo as it stood 2026-06-10.** III.1 (96-101): 5 autoloads
  (`EventBus`, `GameStateMachine`, `KeyStore`, `Meta`, `SceneTimer`); Container architecture
  (`ContainerBase`, 6 containers, `GameDirector`); kernel seed (`CoreResolver`/`CoreEngine`); 26 typed
  Resources; substrate v1 (`Key.gd` etc., Phase 5a PP-684-688 implemented through ~2026-05-04). III.2
  (103-113): drift census D1-D8, severity-ranked — D1 (Key.gd schema v1, **P1**) is Gate-0 work; D2
  (`CombatLogic.gd`, **P1**, superseded by `combat_engine_v1`); D3 (`DomainActionSystem.gd`, **P1**,
  pre-d+σ); D4 (Mandate as writable base field, **P1**). III.3 (116): three contradictory
  "what are the autoloads" docs; recommends the live 5-autoload pattern as keeper, per-system
  "Manager" autoloads from the 04-18 doc become RefCounted systems.
- **PART IV (120-134), directional laws.** IV.1 (122-123) scale spine + season clock. **IV.2
  (125-131), the four laws**: (1) **line 126** downward = derivation, read-only, no setters; (2)
  **line 127** upward = echo at substrate, never the aggregate; (3) **line 128** lateral = Keys only,
  *"the EventBus carries UI/lifecycle signals only — signals are not Keys (Keys are persisted facts;
  signals are transient wiring)"*; (4) line 129 time = Accounting cadence. IV.3 (133-134) conversion
  unit = one module contract.
- **PART V (138-167), the conversion dictionary.** V.1 (140-156) construct-mapping table — Python↔Godot
  for every substrate object. **Line 149**: registries *"Generated from the ttrpg yaml by the export
  ritual — never hand-transcribed"*. **Line 150**: conviction vectors → `PackedFloat32Array` + const
  name→index map. **Line 151**: params/config → *"Generated, generator-stamped export per system →
  `res://data/<system>_params.tres|json`"*. **Line 154**: `RuntimeError` → `push_error` + typed error
  result, *"a violated invariant must be visible in the result, not swallowed."* V.2 (158-164)
  determinism/parity protocol: named draws (160), recorded-draw replay (161), statistical parity
  (162), **float discipline (163)**: *"assert in integer domain at degree thresholds… never assert raw
  float equality across languages"*, **Key-log equality as master parity check (164)**: *"one harness,
  three uses."* V.3 (167-168 — header is 167, content is 168) language-semantics watchlist:
  integer division, dict iteration order, StringName vs String, typed arrays, no `frozen`.
  V.4 (169-171) Python corpus stays oracle until per-module GDScript parity, then retires — Jordan's
  call, carried open.
- **PART VI (174-190), sequencing.** VI.1 Gate-0 (176-181): **G0.1** (177) Key schema v1→v2 migration;
  **G0.2** (178) Godot-doc consolidation; **G0.3** (179) K8 verdict (Key-as-Resource vs RefCounted,
  *"[ASSUMPTION: K8 not yet executed]"*); **G0.4** (180) Key-type registrations; **G0.5** (181)
  per-module canonical gate, halt on untraceable values. VI.2 Stage 1 spine (183-184): kernel,
  KeyStore v2, seeded RNG service, statechart, generated registry loaders — *"Build… scene-tree-free
  and headless-testable."* VI.3 Stage 2 (186-187) six-step per-module ritual. VI.4 Stage 3 (189-190)
  cross-scale, articulation last.
- **PART VII (194-204), frictions R1-R10** — R1 Key schema v1≠v2 (P1); R4 RNG/float divergence,
  explicitly *not* solved by bit-parity (198); R7 downward-delivery gap (201).
- **PART VIII (208-216), the `[OPEN — Jordan]` register**, 8 items: (1) downward Key delivery, (2)
  Python corpus end-state, (3) faction-stat inversion, (4) Key runtime form (Resource vs RefCounted),
  (5) **autoload ruling (line 213)** — *"adopt the live pattern (Meta single state owner +
  EventBus/GameStateMachine/KeyStore/SceneTimer as thin services) as architecture.md v2, or direct
  otherwise. G0.2 executes whichever ruling stands"* — **this item is STILL OPEN**; nothing in this
  repo or `godot/` records a ruling on it. (6) first module target (settlement_layer recommended),
  (7) D6 Church stat mismatch, (8) standing dockets by reference.
- **PART IX (220-223)**, three-session plan (doc + Gate-0-docs, spine, first module) — **none of the
  three sessions this doc plans for are evidenced as having run**; `godot/skeleton/` is not a Gate-0
  artifact, it postdates this plan and is a separate, later, unrelated slice (personal_combat, not
  settlement_layer, the doc's own recommended first module).
- **X (227-230)**, provenance. As-of SHAs: ttrpg `~496f3d5`, valoria-game `main` (0 commits since
  2026-06-06, last design sync `9057663f`) — **both are stale as of this repo's current state**;
  CLAUDE.md now records `valoria-game` PR #2 merged 2026-08-20 (76+ days and ~1,596 ttrpg commits
  after this doc's provenance snapshot).

**This document has never been updated for anything that happened after 2026-06-10.** It predates the
`sim/`→`engine/`+`systems/*/sim/` restructure (2026-07-21), the composition-role registry
(2026-08-20), `combat_bridge.py`'s late-discovered seam (CLAUDE.md §3), the actual first compile of
`valoria-game` (2026-08-18/19, see section 5), and PR #2 (2026-08-20). Every "current state" claim in it about
`valoria-game` should be treated as a snapshot, not a fact.

---

## 2. `STRAT:NNN` citation verification

All citations in `04_GODOT_IMPLEMENTABILITY.md` resolve against the file read in section 1. Every one checked
below is **VERIFIED-TRUE** (quote matches, modulo the document's own ellipsis/paraphrase) unless noted.

| citation | what it's used for | line content | verdict |
|---|---|---|---|
| `STRAT:19` | save model (M-12) | "save state = initial conditions + Key log; replay = deterministic re-execution" | **VERIFIED-TRUE** — exact substring match |
| `STRAT:75-77` | O-5, three dice_pool resolvers | rows 16-18 of the module table: `personal_combat`/`social_contest`/`mass_battle`, all `dice_pool` | **VERIFIED-TRUE as a citation of what STRAT says** — but see section 9: STRAT's own `dice_pool` label for `personal_combat` **disagrees with the live `references/module_contracts.yaml`**, which has `resolver: d_sigma` for that module. The design doc's O-5 finding is really surfacing a THIRD disagreement (STRAT vs itself vs the registry), not just STRAT vs the new design. |
| `STRAT:97` | M-13, "Meta… single state owner" | line 97: "`Meta` (41.6k — **the single state owner**: …)" | **VERIFIED-TRUE** |
| `STRAT:126` | M-1, law 1 "no setters, getters only" | line 126: "Downward = derivation (read-only)… (R4 hook; VG mirror = **no setters, getters only**)" | **VERIFIED-TRUE** |
| `STRAT:128` | §4.1, "signals are not Keys" | line 128, verbatim: "the EventBus carries UI/lifecycle signals only — signals are not Keys (Keys are persisted facts; signals are transient wiring)" | **VERIFIED-TRUE**, exact quote |
| `STRAT:154` | §8.2/M-15, "no exceptions in GDScript" | line 154 table row, exact | **VERIFIED-TRUE** |
| `STRAT:163` | F-4, integer-domain thresholds | line 163: "assert in integer domain at degree thresholds… never assert raw float equality across languages" | **VERIFIED-TRUE**, exact quote |
| `STRAT:164` | M-12, "one harness, three uses" | line 164, exact | **VERIFIED-TRUE** |
| `STRAT:167` | §7.3 breaker 5, "corrupt silently" | **the actual "corrupt silently" phrase is on line 168** (`### V.3` header is on 167; the watchlist prose, incl. dict-iteration-order and "never order-dependent logic," is the next line) | **LINE-MISMATCH (off-by-one)** — cites the section header, not the sentence it quotes |
| `STRAT:177-184` | §0.2, Gate-0 preconditions "KeyStore v2, base classes, RNG service" | 177-181 = G0.1-G0.5; 182 = section break; 183 = `### VI.2` header; 184 = Stage-1 body (kernel, **KeyStore v2**, **seeded RNG service**, statechart, registry loaders) | **PARTIALLY VERIFIED** — `KeyStore v2` and the `RNG service` are both literally in this range (line 184). **"base classes" is not a literal phrase anywhere in 177-184** — the closest referent is "the kernel" (184, item 1), which only becomes `BaseEngine`/`EngineModule` in the *later* skeleton (section 3, not in scope of this citation). This phrase is inherited from `CLAUDE.md`'s own wording ("KeyStore v2, base classes, RNG service"), not independently derived from STRAT — a citation of a citation. |
| `STRAT:213` | M-13, autoload ruling still open | line 213, Part VIII item 5, exact | **VERIFIED-TRUE** |
| `STRAT:245` | (in the task's check-list) | **file is only 230 lines; line 245 does not exist** | **DOES NOT RESOLVE** — and it is not actually cited anywhere in `04_GODOT_IMPLEMENTABILITY.md`, `01_ARCHITECTURE.md`, `02_THE_SEASON_LOOP.md`, or `03_COMPENDIUM.md` (grepped all four; zero hits for `STRAT:245`). This appears to be a citation supplied for verification that the design corpus never actually made — a non-finding, not a defect. |

Additional citations spot-checked while reading (not on the assignment's list, found in the course of
reading sections 5-8 of the design doc): `STRAT:41` ("kernel scene-tree-free", and — separately — the
`ecosystem_versions.yaml` "pins Godot 4.6" sentence, section 5 below) — **VERIFIED-TRUE**; `STRAT:149`,
`:150`, `:151` (registry/param export language) — **VERIFIED-TRUE**; `STRAT:159` (bit-parity is a
false goal) — **VERIFIED-TRUE**; `STRAT:161-164` (named draws · recorded-draw replay · key-log
equality · integer thresholds) — **cited range starts one line late**: "named draws" is `STRAT:160`,
not inside `161-164`; the other three items are correctly in range. Minor.

---

## 3. `godot/skeleton/` — every file

Confirmed: **no `.gd` file anywhere in this repo defines** `BaseEngine`, `EngineModule`, `KeyBus`,
`GameState`, `Key`, `Resolver`, `MechanicsRegistry`, or `Kernel` (`grep -rn` across every `.gd` file →
zero hits; `find . -name "*.gd"` → exactly the 8 files below, nothing else). The skeleton is not
buildable as-is; it names a spine it never provides.

| file | `class_name` | `extends` | undefined symbols reached for | what it proves about intended architecture |
|---|---|---|---|---|
| `core/engine_manifest.gd` | `EngineManifest` | `Resource` | none (self-contained data class) | one engine = one manifest .tres; `MechanicsRegistry.load_manifests` is referenced only in the docstring, never defined anywhere |
| `core/key_type_resource.gd` | `KeyTypeResource` | `Resource` | none | one Key type = one `.tres`; `KeyTypeRegistry.load_from_dir` referenced only in the docstring, not defined |
| `engines/combat/combat_engine.gd` | `CombatEngine` | **`BaseEngine`** (undefined) | `GameState.get_actor`, `GameState.new_key_id`, `GameState.season_index`, `Key.new()`, `KeyBus.emit_key` | the `BaseEngine` pattern (`_on_setup`, `modules[]`, `consume()`) and the manifest-driven module list |
| `engines/combat/modules/strike_module.gd` | `StrikeModule` | **`EngineModule`** (undefined) | `GameState.get_actor` (x2, lines 38-39), `GameState.rng.seed =` (line 67, **a shared mutable global RNG**), `GameState.rng.randfn` (line 138), `GameState.new_key_id`, `GameState.season_index`, `Key.new()`, `produce()` (from `EngineModule`) | the `resolve(key: Key)` contract; the D_SIGMA resolution math ported from `core.py`/`wrapper.py` |
| `engines/combat/modules/wound_module.gd` | `WoundModule` | **`EngineModule`** (undefined) | `GameState.get_actor` (line 40), `Key.new()`, `produce()` | the wound-track math (`WI`, `MaxWounds`, `Health`, felled test) |
| `engines/combat/resources/combat_config.gd` | `CombatConfig` | `Resource` | none | Class-C tunables as one `.tres` (fixes the dead-DAMAGE_SCALE defect the comment documents) |
| `engines/combat/resources/tradition_resource.gd` | `TraditionResource` | `Resource` | none | martial traditions as data (channel-weight bias vectors), not code branches |
| `engines/combat/resources/weapon_resource.gd` | `WeaponResource` | `Resource` | none | weapon-as-continuous-vector, supersedes the 3-axis `data_serialization_spec.md` model |

**Independent finding, not surfaced anywhere in `04_GODOT_IMPLEMENTABILITY.md`:** `wound_module.gd`
**contradicts its own declared contract.** Line 31 declares `health` as
`{"bucket": "derived_value", "writable": false}` under an explicit **F1 GUARD** comment (lines 12-13:
*"this module writes the SUBSTRATE track… never the derived Health directly"*). But line 55 is:

```gdscript
actor.set("health", maxf(0.0, health_full - cum))            # derived display value (read-only)
```

This is a **direct write to the very field the module's own manifest declares non-writable**, inside
the module that documents the rule it is breaking. The comment calls it *"a derived display value
(read-only)"* while the code writes it. This is exactly the class of self-contradiction M-14
("`Container.matter` is untyped") and F1 more broadly are warning about, but it is a *new* instance,
found in this pass — not the one either document already names.

The `.tres` instances (`data/combat_config.tres`, `data/engines/combat/*.tres`,
`data/key_types/scene_combat_*.tres`, `data/weapons/longsword.tres`, `data/traditions/german.tres`,
`data/traditions/none.tres`, `data/weapons/arming.tres`) are internally consistent with the `.gd`
files' `@export` shapes (spot-checked `combat_config.tres`, `combat.tres`, `strike.tres`,
`scene_combat_hit.tres`, `longsword.tres`, `german.tres` — all resolve their `script_class` to a real
file and populate only declared `@export` fields). They cannot be *loaded* because the base classes
they depend on transitively (`EngineModule`, `BaseEngine`) do not exist.

---

## 4. Module contracts — all 27, parsed (not grepped)

Parsed with `yaml.safe_load` — `references/module_contracts.yaml`, `schema_version: 2`,
`status: EXTRACTED_STAGE1`, 1571 lines, `modules:` is a 27-element list.

| # | module | doc | resolver | scales | IN types | OUT types | assumption-grade? |
|---|---|---|---|---|---|---|---|
| 1 | faction_state | `systems/factions/faction_behavior_v30.md` | deterministic_accounting | provincial | 25 | 3 | **yes** (line 210) |
| 2 | npc_behavior | `systems/factions/political_dynamics_keys_migration_v30.md` | deterministic_accounting | personal, scene | 31 | 11 | **yes** (287) |
| 3 | npc_memory | **null** | state_reader | personal | 4 | 0 | **yes** (386) |
| 4 | piety_track | `systems/characters/conviction_track_v1.md` | deterministic_accounting | personal | 9 | 1 | **yes** (419) |
| 5 | territorial_piety | `systems/characters/conviction_track_v30.md` | deterministic_accounting | territory, provincial | 0 | 0 | **yes** (471) |
| 6 | threadwork | `systems/threadwork/threadwork_v30.md` | dice_pool | personal, thread | 0 | 2 | no |
| 7 | fieldwork_knots | `systems/fieldwork/knots_v30.md` | dice_pool | personal, scene | 1 (`*`) | 4 | no |
| 8 | scene_slate | **null** | manifest | scene | 0 | 8 | no |
| 9 | game_director | **null** | manifest | scene | 0 | 3 | no |
| 10 | scene_timer | **null** | state_reader | scene | 3 | 0 | no |
| 11 | audit | **null** | state_reader | scene | 3 | 0 | no |
| 12 | social_contest | `systems/social_contest/social_contest_v30.md` | dice_pool | scene | 1 | 4 | no |
| 13 | mass_battle | `systems/mass_battle/mass_battle_v30.md` | dice_pool | scene | 0 | 1 | no |
| 14 | domain_actions | **null** | d_sigma | provincial | 0 | 6 | **yes** (835) |
| 15 | peninsular_strain | `systems/overview/peninsular_strain_v30.md` | deterministic_accounting | peninsula | 0 | 4 | **yes** (877) |
| 16 | settlement_layer | `systems/settlements/settlement_layer_v30.md` | deterministic_accounting | settlement, territory | 2 | 1 | no |
| 17 | settlement_economy | **null** | deterministic_accounting | settlement | 2 | 0 | **yes** (1024) |
| 18 | ci_political | `systems/factions/ci_political_v30.md` | deterministic_accounting | provincial | 0 | 0 | no |
| 19 | victory | `systems/victory/victory_v30.md` | state_reader | provincial, peninsula | 0 | 0 | no |
| 20 | engine_clock | **null** | clock_advance | provincial | 0 | 2 | no (state field marked `[ASSUMPTION]` at line 1143, but resolver line itself isn't) |
| 21 | faction_politics | `systems/factions/faction_politics_v30.md` | deterministic_accounting | provincial | 0 | 4 | **yes** (1169) |
| 22 | miraculous_event | `systems/world/miraculous_event_v30.md` | state_reader | personal, settlement, peninsula | 0 | 1 | **yes** (1206) |
| 23 | scenario_authoring | **null** | manifest | peninsula | 0 | 2 | **yes** (1233) |
| 24 | articulation_layer | `systems/articulation/articulation_layer_v30.md` | deterministic_accounting | personal, scene, provincial | 1 (`*`) | 0 | no |
| 25 | clock_registry | `systems/overview/clock_registry_v30.md` | manifest | provincial | 0 | 0 | no |
| 26 | personal_combat | `systems/combat/combat_engine_v1/` | **d_sigma** | personal | 2 | 3 | no |
| 27 | campaign_architecture | `systems/_architecture/campaign_architecture_v30.md` | none (`status: stub`) | provincial | 0 | 0 | n/a — stub |

**`doc: null` count: 9, exact set** — `npc_memory, scene_slate, game_director, scene_timer, audit,
domain_actions, settlement_economy, engine_clock, scenario_authoring`. **This matches CLAUDE.md §6's
corrected claim exactly** (alphabetically identical set) — **VERIFIED-TRUE**, and matches
`04_GODOT_IMPLEMENTABILITY.md:55-58`'s claim verbatim too.

**`[ASSUMPTION]`-grade resolvers: 11, exact.** `grep -n "^\s*resolver:.*\[ASSUMPTION\]"` → 11 hits, at
lines 210, 287, 386, 419, 471, 835, 877, 1024, 1169, 1206, 1233 — modules `faction_state,
npc_behavior, npc_memory, piety_track, territorial_piety, domain_actions, peninsular_strain,
settlement_economy, faction_politics, miraculous_event, scenario_authoring`. **Matches CLAUDE.md §6's
"11/27 resolvers are `[ASSUMPTION]`-grade" exactly.**

**`engine_clock` (lines 1128-1160):** `doc: null`, `sim_module: none`, with an inline comment
(1131-1135): *"OI-54 (ED-IN-0097, W4)… grep for mechanical.season_change / mechanical.accounting
Key-type strings across systems/+engine/ finds no emitter. engine/autoload/season_manager.py advances
the season counter but does not emit either declared Key type — the temporal-spine gap CLAUDE.md §6
names."* `gap_notes` (1146-1147) confirm: home doc unlocated, `propagation_spec_v1.md` is a
*candidate* but `ED-1051` is open and `doc: null` "stays unflipped until then." `wiring:` block
(1153-1160): `build: design`, `godot: no-oracle`, `port_rank: 8`, note: *"doc:null temporal spine — the
sole remaining T0 blocker (ED-1051). Blocks the season/accounting cadence port."* This is exactly the
citation `04_GODOT_IMPLEMENTABILITY.md:1128-1136`/O-2 relies on — **VERIFIED-TRUE**, and see section 9 below
for whether the new design actually closes this gap.

`composition_roles:` block (lines 57-181+, separate from `modules:`) also exists in the same file,
governing `engine/substrate/composition.py`'s role→callable resolution — verified against the live
Python (`engine/substrate/composition.py:1-24`, which matches `04_GODOT_IMPLEMENTABILITY.md §8.1`'s
quotes *"Adding a subsystem to the campaign loop is a row in the registry, not an import in the
engine"* and *"the exporter imports and resolves every declared target AT EXPORT TIME, behind a
blocking CI gate"* — **both VERIFIED-TRUE, exact substring matches**).

---

## 5. THE GODOT VERSION QUESTION

### 5.1 Every piece of evidence in this repo, with path:line

| # | source | exact quote / content |
|---|---|---|
| 1 | `CLAUDE.md:10` | *"`project.godot:11` declares `features=("4.3")` and CI pins the 4.3 binary, while this document and `godot/` say 4.6. One of them is wrong… Awaiting a ruling (plan Q3); do not pick one by editing this line."* |
| 2 | `README.md:3` | *"Design source of truth for **Valoria**, a Godot 4.6 videogame that fuses…"* |
| 3 | `README.md:10` | table row: `jordanelias/valoria-game` \| **Godot 4.6 implementation** |
| 4 | `godot/godot_architecture_specification.md:4` | `## Engine: Godot 4.x (GDScript)` — deliberately loose |
| 5 | `godot/godot_architecture_specification.md:675` | *"Download Godot **4.3+** from https://godotengine.org/download"* — a minimum, not a target |
| 6 | `godot/godot_conversion_strategy_v1.md:41` | *"`ecosystem_versions.yaml` pins **Godot 4.6** + model/tokenizer"* — **the strongest documentary claim for 4.6 in this repo**, but see caveat below |
| 7 | `proposals/2026-08-18-recursion-interrogation-log.md:190` | (direct clone inspection of `valoria-game`) *"`project.godot` — real,… **Godot 4.3 features**"* |
| 8 | `proposals/2026-08-18-recursion-interrogation-log.md:226,431` | *"README says 'Godot 4.6+'; `project.godot` declares `config/features=PackedStringArray("4.3", …)`"* — the conflict independently rediscovered by direct repo inspection, not inference |
| 9 | `proposals/2026-08-18-recursion-interrogation-log.md:445,636` | Godot **4.3-stable** actually **downloaded and run headless** (`--headless --path . --editor --quit`) against `valoria-game`, twice, on different sessions — this is the only version anyone has ever executed against either repo |
| 10 | `workplans/return_to_game_queue.yaml:74-79` | `baselines.game_compile`: *"taken 2026-08-19, **Godot 4.3.stable.official.77dcf97d8**, headless --editor --quit, valoria-game@5e01065"* — `stock: {failed_to_load: 54, parse_errors: 169, broken_scripts: 61}`, down to `{5, 14, 8}` after five defect fixes + one project setting |
| 11 | `proposals/2026-08-20-return-to-game-plan-v1.md:101` (row D5) | *"**Godot version conflict.** `valoria-game/project.godot:11` declares `features=("4.3")` and CI pins the 4.3 binary… One of the two is wrong; a 4.3 binary parsing a 4.6-authored tree can mis-count the ratchet."* — `OPEN — §7 (Jordan)` |
| 12 | `proposals/2026-08-21-execution-order-v1.md:849,1115` | *"Godot 4.3 downloads through the proxy, so this is locally measurable — **84 errors** reproduce exactly, **63 of them `Cannot infer the type of X`**"*; Q3 row: *"Godot 4.3 or 4.6? … the meaning of the compile ratchet's 84"* |
| 13 | `04_GODOT_IMPLEMENTABILITY.md:30-34` | *"It asserts no engine version… `project.godot` declares 4.3, this repository and `godot/` say 4.6 — and forbids picking one. Exactly three recommendations below are version-gated… Everything else holds across the whole 4.x line."* |

### 5.2 The single strongest piece of "4.6" evidence does not exist on disk

**`references/ecosystem_versions.yaml`** — the file `STRAT:41` cites as pinning Godot 4.6 — **is not in
the working tree.** `find . -iname "ecosystem_versions*"` returns nothing. `references/restructure_ledger.md:1082`
records it as retired to `deprecated/references/ecosystem_versions.yaml` (2026-07-21 wave), and
`deprecated/` itself is a dir-prefix `FORK:c451bcb` row (`restructure_ledger.md:1228`) per the
2026-08-23 S6/6a cull. **This is a shallow clone (`git rev-parse --is-shallow-repository` → `true`,
98 commits visible) and `c451bcb` is unreachable** — `git show c451bcb:references/ecosystem_versions.yaml`
fails with "path does not exist," and `git log --all -- "*ecosystem_versions*"` returns zero commits.
**So the one artifact that would settle "was 4.6 ever actually pinned, and when" cannot be read from
this checkout at all.** The only remaining trace of its content is the strategy doc's own paraphrase
("pins Godot 4.6"), which is itself six weeks stale and was never re-verified against the file it
cites (the strategy doc has had no update since 2026-06-10, per section 1).

### 5.3 What was actually measured, and what it means

The **only executed fact** in this entire corpus is: **Godot 4.3-stable, run headless twice, against
`valoria-game`'s actual `.gd` tree.** Two independent sessions did this (2026-08-18 interrogation log,
2026-08-19 `return_to_game_queue.yaml` baseline). Neither ever ran 4.6. The dominant failure mode,
bisected properly (`recursion-interrogation-log.md:645-660`):

> *"Godot 4.3 promoted `INFERENCE_ON_VARIANT` to an **error by default**; the code was written against
> earlier semantics where `var x := some_dict[k]` was legal."* Setting
> `gdscript/warnings/inference_on_variant=1` (warn, not error) in `project.godot` took the error count
> from 121→16 and broken-script count from 27→3.

This is a **project-setting strictness default that changed AT 4.3**, not a `.gd`-syntax
incompatibility. It is the origin of most of the "84 errors" the compile ratchet holds
(2026-08-21-execution-order-v1.md:849: *"84 errors reproduce exactly, 63 of them `Cannot infer the
type of X`"*).

### 5.4 Does each of the design's version-gated recommendations differ between 4.3 and 4.6?

Judged from the engine's documented behaviour across the 4.x line (no Godot project was opened in
this pass, per the task's constraint — none of the rows below required one; each is a fact about which
GDScript release introduced a *language/API* feature, not a fact requiring execution).

| recommendation | 4.3 behaviour | 4.6 behaviour | does the design's claim survive in 4.6? |
|---|---|---|---|
| **typed `Dictionary`** (`Dictionary[K,V]`) — §5, m-4 | **not available**; `@export var qual: Dictionary` is untyped, every read is `Variant`, casts required (`combat_config.gd:29-38`) | **available** (introduced 4.4) | **Yes, and the fallback becomes unnecessary.** Under a genuine 4.6 target the design's own m-4 fallback (`const` array + name→index map, matching `STRAT:150`'s conviction-vector pattern) is no longer the only option — typed `Dictionary` can be used directly, closing the untyped-`@export` problem `combat_config.gd` demonstrates. **This is the single largest concrete change a 4.6 ruling makes.** |
| **`@abstract`** — §8.2 | **not available** | **available** (introduced 4.5, present in 4.6) | **Yes.** Under 4.6, `BaseEngine`/`EngineModule` role methods can be marked `@abstract` for a parse-time error on an unimplemented override, instead of the fallback (`push_error` + typed error result, `STRAT:154`). The fallback still has independent value (GDScript still has no exceptions), but it stops being load-bearing for *catching a missing override*. |
| **`WorkerThreadPool` ergonomics** — §6.2 | present since 4.0; `add_group_task`/`wait_for_group_task_completion` usable | present, incrementally hardened across the 4.x line | **Mostly no.** The API shape §6.2 relies on (data-parallel map, atomic refcount traffic on `RefCounted` hops) is unchanged in kind between 4.3 and 4.6 — this repo's own evidence has nothing that measures a behavioural difference here, and none was executed. Treat this row as **[unclear]** beyond "the API exists in both." |
| `class_name Container` collision (F-3) | present | present | **No difference.** `Container` has been the `Control`-derived base of `VBoxContainer` etc. since Godot 4.0 (and 3.x). Version-independent, exactly as `04_GODOT_IMPLEMENTABILITY.md:179` itself already states. |
| `Vector2` as a value type (§2.2) | value type | value type | **No difference.** Unaffected by the 4.3/4.6 question. |
| `.tres` resource-cache behaviour (`load()` returns the cached instance per path) — M-5 | true | true | **No difference.** Long-standing `ResourceLoader` behaviour across the whole 4.x line. |
| JSON int precision (`JSON.parse_string` → doubles, ids >2^53 don't round-trip) — M-6b | true | true | **No difference.** A property of `Variant`'s JSON representation, unaffected by version. |
| `RefCounted` cycle collection (O-1) | none (pure refcounting) | none (pure refcounting) | **No difference.** Godot has never had a cycle collector for `RefCounted`, in 4.x or 3.x. The design's ids-not-pointers discipline is load-bearing regardless of version. |
| **the compile ratchet's 84-error baseline** (not in the design doc's list, but load-bearing per this task's framing) | measured directly: 84, 63 of them `Cannot infer the type of X` | **not measured — no session has ever run 4.6 against `valoria-game`** | **Almost certainly does NOT change in the design's favor.** The 4.3-promoted `INFERENCE_ON_VARIANT`-as-error default was not reverted in later 4.x releases; a 4.6 run of the same untouched `.gd` tree would be expected to hit the same or a superset of the strictness errors, not fewer. **This is the one place a 4.6 ruling would NOT relax anything** — it would still need the same project-setting fix already found (`inference_on_variant=1`) or the underlying `var x := dict[k]` sites fixed. |

### 5.5 What targeting 4.6 changes, and what it does not — stated plainly

**Changes:** two of the design's three explicitly version-gated recommendations (typed `Dictionary`,
`@abstract`) become directly usable rather than needing their fallback — this is a genuine, if narrow,
simplification available only if 4.6 is confirmed. **Does not change:** the F-3 `Container` collision
(present in both), the `RefCounted`/JSON/`.tres` facts the design's save-format section depends on
(all version-independent), or — most importantly for the load-bearing question this task names — **the
meaning of the compile ratchet's 84 errors**, because the ratchet has only ever been run under 4.3 and
the dominant failure class (strictness-default promotion) is not the kind of thing later releases
typically relax. **The version question remains genuinely unresolved by this pass**: the one artifact
that asserted 4.6 authoritatively (`ecosystem_versions.yaml`) is unreadable in this shallow clone, and
the one thing anyone has ever actually run is 4.3.

---

## 6. The four FATALs, independently checked

- **F-1 (no-`World` guarantee is not type-enforceable in GDScript) — CONFIRMED.** GDScript genuinely has
  no `private`/module/package/friend mechanism, and an autoload registered in Project Settings is a
  bare global identifier reachable from any script body regardless of base class — this is accurate to
  the engine's actual design, not an overstatement. The repo's own skeleton is live proof, not a
  hypothetical: `strike_module.gd:38-39` (`GameState.get_actor`), `:67` (`GameState.rng.seed =`),
  `combat_engine.gd:60` (`KeyBus.emit_key`) all reach global state from inside a `RefCounted`
  resolution module (verified directly, section 3 above). **Also independently confirmed: `01_ARCHITECTURE.md`
  has already adopted the fix** (§3.1a, read in this pass) — the sibling design document now states
  the same downgrade (*"unwritten, not unwritable"*) and the World-first-parameter rule, so this
  FATAL is **already remediated in the current tree**, not merely recommended.
- **F-2 ("consensus broadcast is a type error" is false in GDScript) — CONFIRMED**, same reasoning as
  F-1: GDScript's static typing does not forbid a function signature of `(Array[Person], int) -> void`;
  nothing stops a second call site with that shape. **Also already remediated**: `01_ARCHITECTURE.md:707`
  now states *"'A consensus broadcast is a type error' is false in GDScript — the collection signature
  is trivially writable. It is a convention with a named check, not a property of the type system"* —
  verbatim adoption of the finding.
- **F-3 (`class_name Container` collides with the built-in) — CONFIRMED as a fact about the engine's
  class list**, and it is genuinely version-independent (`Container`/`Control`/`VBoxContainer` etc.
  have been present since Godot 4.0). Not executable-verified in this pass (no project opened, per
  constraint), but this is uncontroversial, well-documented Godot API surface, not a subtle claim. **Also
  already remediated**: `01_ARCHITECTURE.md:148-156` shows the object already renamed to `Rung`, with an
  inline note explaining the `Container` collision was a worse choice than the earlier-rejected `Node`.
  `03_COMPENDIUM.md:642` records `Rung` as *"ADOPTED, at the SECOND attempt."*
- **F-4 (`additive` order-independence conflates clamp-order with float-summation-order) — CONFIRMED, and
  UNIQUE among the four: this one is still LIVE in the current tree.** IEEE 754 addition genuinely is
  not associative; this is a correct, standard fact and the design's own architecture (a band gate on
  a summed value, `verbs(site,c) = {v : condition(c) ≥ floor(v)}`) does make a one-ulp difference
  observable at a band edge, exactly as claimed. **Grepped `01_ARCHITECTURE.md:445-449` and
  `02_THE_SEASON_LOOP.md:570-573` directly**: both still read *"`additive` is order-independent ONLY
  under batching"* with no fixed-point fix and no "canonically ordered" wording correction. **This is
  the one FATAL of the four that has not been addressed anywhere in the sibling documents as of this
  read.**

**Net: three of the four FATALs the axis document raised have already been fixed in `01_ARCHITECTURE.md`/
`03_COMPENDIUM.md` (visible in the current working tree, most likely via the PR referenced in the
latest commit, "[design] Adversarial review of PR #343 — the architecture is right and the vocabulary
is incomplete (#344)"). F-4 (fixed-point `condition`/`stores`) remains open and unaddressed.**

---

## 7. Carrier placement — the design's table, judged against a 4.6 target

Reproduced from `04_GODOT_IMPLEMENTABILITY.md §2.1` (table at lines 127-152) — every row judged
independently against Godot 4.6 semantics (no project opened; judged on documented engine behaviour):

| object | design's Godot form | judgment |
|---|---|---|
| Person / Cohort | one `RefCounted` `class_name` (both, weight≥1) | **Sound.** `RefCounted` has no scene-tree presence and no per-frame cost; a Person/Cohort at any N is exactly the shape `RefCounted` is for. |
| Rung (ex-Container) | `RefCounted` under the renamed identifier | **Sound, and necessary** — see F-3. |
| Office, Site | `RefCounted` | **Sound** — low-N, id-referenced records. |
| Tenure | `row` in a `TenureStore RefCounted` (not one object per edge) | **Sound, and the right call**: one `RefCounted` per Tenure at "the largest object count in the design" (design's own words) would be a real allocation cost; a struct-of-arrays store avoids it. |
| Act / touch / spec | `RefCounted` (Act, one tick) / value (touch, spec) | **Sound.** |
| Claim | `row` in a packed per-person ledger, not one object per claim | **Sound** — at `L=200` per person this is the difference between N×200 rows and N×200 `RefCounted` allocations; the design is right to avoid the latter. |
| Event | `row` in an append-only log | **Sound, and has a working precedent in this repo**: `engine/substrate/keys.py`'s `KeyLog` is exactly this shape already, in the Python reference (verified section 4/9). |
| Venue / door / MatterKind | `Resource` + `@export` + `.tres` | **Sound and proven**: `combat_config.gd`/`longsword.tres`/`german.tres` (verified section 3) are exactly this pattern, already working in the one slice that exists. |
| Sensation | `Vector2` | **The single strongest recommendation in the table.** A built-in value type genuinely cannot be widened with a third field the way a `RefCounted` subclass can — this is a property the compiler enforces, not a convention. Version-independent; `Vector2` has always been a value type in Godot 4.x. |
| World | `RefCounted`, owned by the driver, **never an autoload** | **Correct, and the load-bearing constraint of the whole port** (section 6/F-1 above) — if this one rule is violated, nothing else in the table matters. |

No row in this table requires anything specific to 4.6 over 4.3; the carrier-placement judgment holds
identically across the version boundary. The version question (section 5) bears on typing ergonomics and the
parse-error census, not on this architectural layer.

---

## 8. Reconciliation — design object → Godot 4.6 build → does `godot/` already say something? → conflict?

| design object | how it would be built in Godot 4.6 | does `godot/` already say something? | path:line | conflict? |
|---|---|---|---|---|
| **World** | one `RefCounted`, constructed by the season driver, passed by parameter down RESOLVE, never an autoload/`class_name` static/`res://` path | **No** — `godot/`'s own plan is the opposite. `godot/scene_tree_architecture.md:16-24` autoloads `GameState` holding "all tracked state"; `STRAT:97` records the live `valoria-game` tree's `Meta` as "the single state owner" | `scene_tree_architecture.md:16`, `STRAT:97,213` | **YES — direct conflict.** The port's own current plan (both the stale 04-18 doc and the live `valoria-game` tree it describes) puts exactly the state the new design's core guarantee forbids behind a global autoload name. `STRAT:213`'s autoload ruling (Part VIII #5) is **still open** — this is the fork point where the conflict must be resolved, not yet resolved anywhere. |
| **The four carriers (Person/Cohort/Rung/Office/Site)** | `RefCounted` per section 2/7 above | **Partially** — `godot/skeleton/`'s `EngineManifest`/`KeyTypeResource` establish the *manifest-as-data* pattern the design's Venue/MatterKind rows already match, but nothing in `godot/` names Person/Cohort/Rung/Office/Site at all — the skeleton only covers `personal_combat`, which is actor-agnostic (works via a duck-typed `GameState.get_actor()`) | `godot/skeleton/core/engine_manifest.gd`, `godot/skeleton/engines/combat/combat_engine.gd:13` | No direct conflict — disjoint scope, not contradictory. |
| **Tenure / StateChange** | `row` in a `TenureStore`; Tenure has no analogue at all in `godot/skeleton/` | **No** — `godot/`'s substrate is Key-shaped (`Key.gd` v1 per `STRAT:106`, superseded by v2 per Gate-0 G0.1), not Tenure-shaped. `StateChange` as a concept does not appear anywhere in `godot/` or `references/module_contracts.yaml`. | — | No conflict, but a genuine **gap** (section 10). |
| **Act / Event / Claim / View / Sensation / World** | value types + `RefCounted`s as tabulated in section 7 | **No** — none of these six names appear in `godot/` at all. The closest analogue is `Key` (Event-shaped) and the skeleton's `Key.new()` calls (section 3), but the design's `Event` is explicitly a `row` in a log, matching `KeyLog`'s actual Python shape (section 9) more than the skeleton's `Key.new()`/`RefCounted` pattern does. | `engine/substrate/keys.py` (Python, not `godot/`) | No direct conflict; `godot/`'s substrate concept (Key) and the design's (Event/Claim) are **compatible in shape but not reconciled in vocabulary anywhere**. |
| **Query (ex-Derived)** | `static func` on a namespace class, `World` as first param on resolver-side rows | **No mechanism exists in `godot/`** for this at all — the skeleton has no query layer, only imperative `resolve()` methods. `STRAT:126` (law 1, "no setters, getters only") is philosophically aligned but names no Godot construct. | `STRAT:126` | No conflict, aligned in spirit, unbuilt in `godot/`. |
| **The three signatures** (`choose`/`resolve`/`witness`) | as section 3/6 above (World-first param, no signals for witness) | **`resolve` partially exists** as `CombatEngine.resolve_round`/`StrikeModule.resolve(key: Key)`, but takes no `World` parameter at all — it reaches `GameState` globally instead (exactly F-1's finding). `choose` and `witness` have **no analogue anywhere in `godot/`.** | `strike_module.gd:36` | **Conflict, by omission** — the one `resolve`-shaped thing that exists does it the wrong way (global reach, not parameter). |
| **The six loop steps** (CALENDAR·MATTER·DELIBERATE·RESOLVE·WITNESS·CENSUS) | one `season(w: World)` driver function, `RefCounted`, headless | **`STRAT:184` names an equivalent shape** ("statechart for game flow"), and `STRAT:41`/`:184` both assert "scene-tree-free, headless-testable" as the engineering floor — **directly compatible**, no Godot construct built yet either side. | `STRAT:41,184` | No conflict; philosophically identical, neither side has code. |
| **Determinism/RNG** (`substream(world_seed,tick,subject_id,purpose)`) | one `RandomNumberGenerator` per operation, constructed-used-discarded | **Direct conflict with the existing skeleton, and the design doc already found it (§7.2/M-15)**: `strike_module.gd:67` — `GameState.rng.seed = key.rng_seed` — is exactly the anti-pattern (shared mutable global RNG, re-seeded in place) the new design's rule forbids. **Verified**: this is real code in this repo, not a hypothetical. | `strike_module.gd:67,138` | **YES — direct, evidenced conflict** between what exists and what the new design (correctly) prescribes. |
| **Save/load** | state snapshot (recommended) vs `STRAT:19`'s initial-conditions+log | **Direct, load-bearing conflict, already flagged as M-12**: `STRAT:19` (*"save state = initial conditions + Key log; replay = deterministic re-execution"*) is the opposite model from `01_ARCHITECTURE.md:1174-1176`'s *"replay is a re-run, not a log, and no decision function may read the event log"* (a full-state-snapshot model). **Verified both citations resolve as quoted** (section 2 above, `STRAT:19`; `01_ARCHITECTURE.md` not independently re-verified line-by-line in this pass but the surrounding text at `§3.1a`/`§9` was read and is consistent with the quoted framing). Neither document cites the other. | `STRAT:19,164` vs `01_ARCHITECTURE.md:1174-1176` | **YES — unreconciled, and it is the kind of conflict a session could resolve cheaply (state the ruling once) but nobody has.** |

---

## 9. Duplication — what the design proposes that `godot/`/`module_contracts.yaml` already specify

- **`O-2`'s claim that the new design "is" the missing `engine_clock` canon — checked against the actual
  contract, and it holds up well but is not a free lunch.** `module_contracts.yaml:1128-1160` (verified
  section 4) declares `engine_clock` as `doc: null`, resolver `clock_advance`, emitting exactly
  `mechanical.accounting` and `mechanical.season_change` — and its `gap_notes` explicitly says the
  Python `season_manager.py` "advances the season counter but does not emit either declared Key type."
  The new design's `CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS` loop with its four
  barriers (`02_THE_SEASON_LOOP.md:29-78`, read in this pass) is a genuinely more complete temporal
  spine than anything currently in `engine_clock`'s contract — **but nothing in `references/module_contracts.yaml`
  or `godot/` has been updated to point at it.** The connection is real and, per O-2, high-leverage, but
  it is currently a claim in one PROPOSED document about another PROPOSED document, not a closed loop —
  `ED-1051` (the item gating `engine_clock`'s `doc: null`) is still open per the contract's own
  `gap_notes`, and nothing in this pass found evidence it has been re-pointed at the new design.
- **The registry-row composition pattern (§8.1's O-3) is genuinely duplicated on both sides already**,
  verified independently in this pass: `engine/substrate/composition.py:1-24` (Python, live,
  2026-08-20) and `godot/skeleton/core/engine_manifest.gd:1-4` (GDScript, non-compiling but
  structurally identical — a manifest resource naming a script path, resolved by the loader, zero
  edits to a hub). This is a real, load-bearing point of agreement the design correctly cites — no new
  mechanism is needed, only pointing the two at each other, exactly as O-3 says.
- **The param-export pipeline (§5's ruling) is not a new recommendation** — `STRAT:149,151` already
  describe it (*"Generated from the ttrpg yaml… never hand-transcribed"*; *"Generated,
  generator-stamped export per system"*), and it is **substantially built**, verified in this pass:
  `engine/engine_params/` holds 10 generated JSON/YAML artifacts (`combat_engine_v1.json`,
  `composition.json`, `descriptors.json`, `game_constants.json`, `key_types.json`,
  `module_contracts.json`, `params_tables.yaml`, `sim_params.json`, `value_pointer_links.json`,
  `world_initial_state.json` — confirming the design doc's "ten artifacts exist
  today" at `04_GODOT_IMPLEMENTABILITY.md:376`, which is **VERIFIED-TRUE**), each with a corresponding
  `tools/export_*.py` and a blocking `--check` mode wired into `.github/workflows/valoria-ci.yml:126-150`
  (verified: `export_engine_params`, `export_key_types`, `export_game_constants`, `export_descriptors`,
  `export_composition`, `export_module_contracts`, `export_world_initial_state` all appear with
  `--check`; `export_sim_params.py` also has a documented `--check` mode in its own docstring though not
  seen wired by name in the same grep). What is genuinely new in the design's §5.2 ruling is the
  **fourth stage** — a `.tres` layer generated from the JSON, never hand-authored — which does not
  exist anywhere in this repo yet (`godot/skeleton/`'s `.tres` files are hand-authored, not generated).
- **`STRAT:75-77`'s three-resolver table for the deferred subsystems disagrees with the live
  `module_contracts.yaml`, and this is a real, three-way inconsistency, not the two-way one O-5
  frames it as.** O-5 frames it as "the shipped contract table" (i.e. `STRAT`) vs. the new design
  (`01:1372-1373`, "adds no resolver"). But the actual **current** `module_contracts.yaml` (verified section 4)
  has `personal_combat` resolver = `d_sigma`, not `dice_pool` as `STRAT:75` states — so there are
  *three* positions in play (STRAT's 2026-06-10 snapshot, the live registry, and the new design), not
  two, and STRAT is stale on its own terms even before the new design is considered.

---

## 10. Gaps — what the port needs that nothing in this repo provides

- **No `World` type exists anywhere in code or `.gd`.** O-6 is correct: it is the type every one of the
  design's central refusals is written against, and it has zero representation in `godot/skeleton/`,
  `references/module_contracts.yaml`, or the Python `engine/` package. This is the single highest-priority
  authoring gap if the port is to start from this design.
- **No `Tenure`/`Event`/`Claim`/`Query` vocabulary exists in `godot/` at all** — the skeleton is entirely
  combat-shaped (`Key`/`KeyBus`/`resolve(key)`), and the new design's substrate is Tenure/Claim/Event
  shaped. These are not proven incompatible (section 8 above found them compatible in spirit), but nothing
  bridges them.
- **No base classes (`BaseEngine`, `EngineModule`) are defined anywhere**, confirmed exhaustively (section 3) —
  the skeleton `extends` two classes that exist nowhere in this repo's `.gd` files. This is Gate-0-tier
  blocking work (`STRAT:177-184`) that the strategy doc calls for and nothing has executed.
  `valoria-game` itself (per the 2026-08-18 direct-clone inspection, `recursion-interrogation-log.md:200-206`)
  has a **working, different** hierarchy — `CoreEngine`/`CoreResolver`/`ResolutionMode` — that already
  compiles; the `ttrpg` skeleton reinvents a non-compiling parallel hierarchy against classes that were
  never written, while a working one already exists 500 metres away in the other repo. This is a
  genuine, actionable gap: **the port doesn't need `BaseEngine` authored from scratch, it needs someone
  to decide whether `godot/skeleton/`'s `BaseEngine`/`EngineModule` names are meant to become
  `valoria-game`'s existing `CoreEngine`/`CoreResolver`, or a deliberate replacement for them** — that
  decision is not recorded anywhere.
- **The autoload ruling (`STRAT:213`, Part VIII #5) is still open**, and it is now doubly load-bearing:
  it was already an open architectural decision before this design existed, and the new design's core
  purity guarantee (F-1, section 3/6/8 above) depends on it being resolved **in the direction the new design
  needs** (no live state behind any autoload name) — which is the *opposite* of what both `godot/`'s
  stale doc and the live `valoria-game` tree currently do. Nothing forces this resolution; it is an
  unforced conflict sitting at the exact fork point Part VIII #5 already named.
- **No fixed-point integer representation for `condition`/`stores` exists anywhere** — F-4 (section 6 above)
  remains the one FATAL not yet remediated in the sibling design docs, and nothing in `godot/` or the
  Python reference implements or even discusses fixed-point condition tracking (the Python `engine/`
  substrate uses floats throughout, per `engine/substrate/keys.py`'s dataclass fields read in this pass).
- **Save format**: `godot/`'s only concrete save code (`godot_architecture_specification.md:660-667`,
  STALE REFERENCE) serializes to `.tres` via `ResourceSaver.save()` — exactly the format M-5 (section 6 above)
  identifies as wrong (script-path fragility, execution-surface risk, resource-cache staleness). No
  `FileAccess`-based serializer exists anywhere in this repo for either the old or new save model.
- **No `.tres`-generation stage exists** for the fourth pipeline stage §5.2's ruling calls for (JSON →
  generated `.tres`, never hand-authored) — this is new work, not a gap in existing intent.

---

## 11. Claims to escalate

1. **The version question itself (`CLAUDE.md` §3/§0.2/Q3) is the top item**, and this pass adds one
   piece of information worth carrying into that ruling: the one artifact that positively asserted
   "Godot 4.6" (`ecosystem_versions.yaml`, cited at `STRAT:41`) **no longer exists on `main`** and is
   **unreachable in this shallow clone even at its fork ref**, so the 4.6 claim currently rests entirely
   on `README.md` and `CLAUDE.md`'s own header prose, with **zero executed evidence**, against 4.3's
   **two independent, executed, reproducible compile runs**. This does not resolve Q3 — a version can
   be correct without ever having been run — but it does mean the "4.6" side of the ledger is
   currently prose-only where the "4.3" side has a `git`-verifiable `project.godot:11` and two headless
   runs. Whoever rules Q3 should know the asymmetry is this stark.
2. **`STRAT:213` / Part VIII #5 (the autoload ruling)** is the fork point where the new design's core
   guarantee (F-1) and the port's current plan (both the stale `godot/` doc and the live `valoria-game`
   tree, per `STRAT:97`) directly disagree. This has been open since 2026-06-10 and is now higher-stakes
   than when it was filed, because a whole new design's central property depends on it landing one
   specific way.
3. **The save-model conflict (M-12, section 8 above)**: `STRAT:19`'s "initial conditions + Key log, replay =
   re-execution" versus the new design's "state snapshot, log never the load path" are genuinely
   incompatible and neither document cites the other. This is cheap to resolve (state one ruling) and
   expensive to leave open (whichever gets built first will need to be redone if the other wins).
4. **F-4 (fixed-point `condition`/`stores`) is the one FATAL of four not yet remediated** in the current
   `01_ARCHITECTURE.md`/`02_THE_SEASON_LOOP.md`, unlike F-1/F-2/F-3 which this pass found already fixed.
   Worth flagging precisely because the other three being already-fixed could read as "the axis
   document's job is done" — it is three-quarters done.
5. **`references/module_contracts.yaml`'s `engine_clock` entry (`doc: null`, `ED-1051` open) has not
   been re-pointed at `02_THE_SEASON_LOOP.md`** despite O-2's finding that the new design supplies
   exactly the missing canon. This is a one-line editorial action (update the `gap_notes`/candidate-doc
   field) that would close a real, load-bearing gap and currently isn't anyone's queued work.
6. **New finding, not in either audit**: `godot/skeleton/engines/combat/modules/wound_module.gd:55`
   writes directly to a field (`health`) its own manifest declares `writable: false` under an explicit
   `F1 GUARD` comment, three lines below the comment explaining why it must not do that (section 3 above). This
   is a small, concrete, fixable defect in the one piece of code in `godot/` that actually runs closest
   to "real" — worth a one-line fix (route the write through the same pattern used for
   `cumulative_damage`/`wounds`) independent of anything else in this report.
