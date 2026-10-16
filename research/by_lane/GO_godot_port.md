# GO — Godot port: historical research, game precedent and repository work, critically evaluated

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a critical evaluation; resolves nothing at runtime
## Date: 2026-10-16 · HEAD as stated in the opening note · Lane: GO

Read at HEAD `021fd96`. Marks: [CHECKED] = opened in the working tree by this lane; [READER] = taken from the named extraction. Extraction short names: `G2` = `out/G2_godot.md`, `A7.1/.2/.3` = `out/A7_architecture_{1,2,3}.md`, `B1.2` = `out/B1_engine_data_2.md`, `B2.2` = `out/B2_hole_register_2.md`, `W3` = `out/W3_plan_3.md`. `STRAT` = `godot/godot_conversion_strategy_v1.md`; `ARCHSPEC` = `godot/godot_architecture_specification.md`; `L1-04` = `architecture/meta/04_CODE_ARCHITECTURE.md`; `MC` = `references/module_contracts.yaml`.

## 0. VERDICT

The GO lane has no historical research and almost no game precedent; its repository work is grounded in engine-reference reading and in its own reconciliation audits. Its governing strategy, though, was written for an architecture the tree has since retired (the Key substrate, the campaign driver, `cross_scale/`), and its recommended `Meta` single state owner, an autoload, is the "world state behind a global name" that ratified Layer 1 rules out (`L1-04:1065`, D-46).

Problems, worst first:

1. **The governing spec targets a retired architecture, and no `godot/` document takes up the successor Layer 1 names.** STRAT (PROPOSED, 2026-06-10) makes the Key substrate "the conversion architecture" and the Key log the parity and save surface. That text is now struck as `[RETIRED ED-IN-0232]`, and "no replacement is ruled here" (`STRAT:5,20,190,193`) [CHECKED]. Gate-0 G0.1, G0.3 and G0.4 and Stage-1 KeyStore v2 are struck too (`G2 §F`). RATIFIED Layer 1 does name the successor: the seeded content hash is "the only execution artifact this architecture has" (`L1-04:942-944`), and Part E step 13, the Godot shell, is done when "a headless run prints the Python oracle's hash in the integer domain" (`L1-04:1119`); `World.content_hash` is defined at `engine/season/state/world.py:1338` [all CHECKED]. What is missing is a `godot/` document that adopts it and a cross-repository instrument that runs it.
2. **The PROPOSED strategy contradicts RATIFIED Layer 1 on the state owner, and only there.** STRAT recommends "Meta as single state owner + thin services", with Meta as an autoload (`STRAT:119,146,181`) and holds that autoload ruling OPEN (`STRAT:216`, item 5) [CHECKED]. L1-04 never names `Meta` (its only autoload hits are `:889`, `:920-924`, `:1000`) [CHECKED]; the rule it breaks is D-46, "world state behind a global name (Godot)" (`L1-04:1065`), with rejection 1, "`World` is NOT an autoload", for "global game state" (`:920-921`) [CHECKED]. Reading `Meta` as the `World` slot is this lane's inference. STRAT's thin service autoloads are not ruled out by L1-04, which keeps signals at the `port/` boundary (`:938`) [CHECKED].
3. **The contracts registry calls the combat slice ported, validated and regenerated; none of that holds.** `MC:872` "combat.strike + combat.wound are PORTED + validated to the Godot shape"; `MC:835` "the port regenerates from THIS, never hand-edits"; `MC:974-975` "This is the template every other port copies" [CHECKED]. The skeleton's `RESIST` table is hand-transcribed and differs from `engine/engine_params/combat_engine_v1.json` in 4 of 12 cells; per `CLAUDE.md` §6 the skeleton does not compile, and `BaseEngine` is defined nowhere [CHECKED]. The enum value `godot: gd-ported` (`MC:882`) is true by its own definition, "a GDScript port exists (the skeleton slice)" (`MC:963`), with no compile claim [CHECKED]. Already tracked: the drift is `ED-PC-0013` item 1 (last row `partial`, `registers/editorial_ledger_pc_archive.jsonl:82`) and plan PC-05 (`_part7:35-40`); `gd-ported` against the non-compiling skeleton is `ED-IN-0017` F9 (`registers/editorial_ledger_in_archive.jsonl:195`) [CHECKED]. Neither record names `MC:835`, `:872` or `:974`.
4. **Every Layer-0 pointer about the port is stale on `engine_clock`, and one gives a dead path.** `CLAUDE.md` §6 lists `engine_clock` among the modules with `doc: null`. `CURRENT.md:38` says "Gate-0 waits on ED-1051". Yet `MC:717` sets `doc:`, and ED-1051's last row is `resolved` (2026-10-08, `registers/editorial_ledger.jsonl:296`) [CHECKED]. `CLAUDE.md` §5 names `engine/autoload/dice_engine.py`, but that directory does not exist; the file is `engine/dice_engine/dice_engine.py` [CHECKED].
5. **Two live files outside `godot/` pin Godot 4.6, while the plan implies nothing asserts a version.** The plan: "The v8 sentence 'nothing in this repository asserts a version' was not true of the tree until that heading went at B-C" (`workplans/valoria_master_workplan_v9_part7.md:88`) [CHECKED]. Live pins remain: `README.md:3,10` "Godot 4.6" and `references/glossary.md:36` "Valoria is a videogame (Godot 4.6)" (no `*.py` names `glossary.md`) [CHECKED]. The other sites differ in kind: `ARCHSPEC:4` "Godot 4.x" and `:675` "Godot 4.3+" are floors, of the kind §2.3 accepts for "Godot 4.0"; `L1-04:951` records which documentation was read; `.designs/…/march_layer_v30.md:60,153` "Godot 4.6" and `.designs/systems/ui/reference/valoria_ui_ux_v4_1.md:1411`, `valoria_ui_ux_v4.md:2066` "Godot 4.2+" are quarantined [CHECKED]. The `CLAUDE.md` preamble already acknowledges a conflict for `godot/` ("godot/ here documents another"), not for `README.md` or the glossary. GO-01's EXIT ("the version string appears in exactly one machine-read file", `_part7:90`) cannot pass while those two carry the string, and neither is in GO-01's EDITS [CHECKED].
6. **Five of the seven `godot/` documents are stale, and the index contradicts itself.** The four ED-1054 banners ("STALE / PARTIALLY SUPERSEDED") and `ARCHSPEC:5` "STALE REFERENCE" [CHECKED]. `godot/README.md:17` says of the four "Do not implement from them", while `:25` says `scene_tree_architecture.md` and `gm_to_engine_conversion.md` "remain valid as amended in Parts III–IV" [CHECKED]. `godot/README.md` still names "Gate-0 G0.1 (Key schema v2)" as the first action item [CHECKED].
7. **Named draws exist as streams, not as sites.** STRAT V.2 rests parity on named draws under recorded replay. Streams are purpose-keyed in code: `H(world_seed, tick, subject_id, purpose)`, "`purpose` must be unique per DRAW" (`engine/season/state/ids.py:16-18`); `draw_factory` gives each person a stream per purpose (`ids.py:27-68`); the combat seam seeds with purpose `f"contest:{prize}:{cause}"` (`engine/season/seam/wrappers/combat.py:222`); `L1-04:1053` (row 35) sets the same rule [CHECKED]. What is absent is per-site naming inside `modules/*`, which draw anonymously from the stream, and mass battle falls back to the process-global `random` (`modules/mass_battle/rngsource.py:45,60`) [CHECKED]. Recorded as `ED-IN-0017` F5 (which cites `:46`/`:61`, one line off) [CHECKED].
8. **MC's module count disagrees with the strategy.** MC holds 26 module rows; STRAT and `godot/README.md` say 27 [CHECKED]. Its `parity: key-log` value (19 rows, plus `key-log + typed-export round-trip` on a 20th) is the retired Key log [CHECKED: counted]; `ED-IN-0017` F9 recorded that exact count and disposed of the value at ladder 2, "irrelevant: the Key substrate is retired" [CHECKED]. It is recorded and disposed of, not open.

Solid: (a) the constants bridge `tools/export_game_constants.py`. It is blocking in CI, keeps hand-confirmed `MAPPING` pairs, and records `COLLISIONS` and `DIVERGENCES` instead of copying values (`.github/workflows/valoria-ci.yml:131-137`; `engine/engine_params/game_constants.json`) [CHECKED]. (b) The port-seam audit `ED-IN-0017` (2026-10-12, `registers/editorial_ledger_in_archive.jsonl:195`) opened the live seams file by file and returns ten port-facing findings with line locators [CHECKED].

## 1. HISTORICAL RESEARCH

### 1.1 Sources

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| — | none | — | `research/00_INDEX.md` §3 row "Godot port (GO) — None located" and §7 "No game or historical source for threadwork or the Godot port" [CHECKED]. `G2 §G`: "No historical cases or research-corpus files cited" [READER]. |

### 1.2 Cases and patterns

None. This lane is a software port. Historical research does not apply to it, and its absence is not a defect.

### 1.3 Critical evaluation

Nothing to evaluate. One near-miss for the record: L1-04's "fixed point for `condition`, `stores`, `margin`" and STRAT V.2 item 4, "float discipline: integer domain at thresholds; quantize 1e-6", are engineering claims, not history (`L1-04:892`; `G2 §F`).

## 2. GAME PRECEDENT

### 2.1 Sources

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| `L1-04` §C.12 rejection 5 (`:950-995`) | The Godot 4.6 engine reference on error handling: no `try`/`catch`, `assert()` compiled out of release builds, `push_error()` is `void`, and `FileAccess.open()` returns a sentinel plus last-error | "read against `docs.godotengine.org/en/4.6` … Sourced from the engine reference, not inferred" (2026-09-05) | **The lane's only fetched external source.** It quotes the docs directly, and its measurement was corrected in place (`:980-982`). Its repo counts are now stale: they cite `engine/season/shape.py` and `engine/season/seam.py`, and neither exists [CHECKED]. A recursive count today gives 401 `raise` sites under `engine/season/` [CHECKED, not comparable to its 167, which counted one directory level]. |
| STRAT I.2 (`G2 §G`) | d+σ regime "basis CK3 / EU / KoDP" | ED-874, ratified 2026-05-31 | Belongs to the IN lane (resolution kernel), not the port. No source is given beyond the game names [READER]. |
| STRAT III.3, V.2 (`G2 §G`) | "Godot's autoload guidance"; "standard deterministic-replay porting practice" | asserted, not cited | Unsourced appeals to common practice [READER]. |
| `ARCHSPEC` Part 6 (`G2 §G`) | GDUnit4 and Dialogic 2 as tooling; renderer "Compatibility" | STALE REFERENCE | Tool choices with no evaluation recorded [READER]. |
| `proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md`; `proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F3_godot46.md` | Godot-semantics analysis of the proposed code shape | PROPOSED, "Nothing here has executed"; F3 is REFERENCE, by `fable`, and labels engine claims `[engine]` | Heads only read [CHECKED: status lines]; bodies not read (§5). |
| `proposals/2026-08-18-recursion-interrogation-log.md` §R9; `proposals/2026-08-18-breaking-the-recursion.md` §4.6 | The one recorded execution of the port: Godot 4.3-stable run headless against `valoria-game`, giving 58 error lines on `main`, five root causes, all 5 autoloads failing to load | PROPOSED, 2026-08-18 | First-hand run record [CHECKED: passages opened]. Dated: it describes `valoria-game` at 2026-08-18, and this repository cannot re-check it. |

### 2.2 Games and systems

| game / system | borrowed or warned against | shape | evidence grade | assessment | locator |
|---|---|---|---|---|---|
| Godot engine idioms (autoload, `Node`, signals, global RNG, sentinel errors) | **warned against**: five idioms rejected, each with the invariant it would break | divergence (deliberate) | engine reference, quoted for rejection 5 only; rejections 1-4 reason from the repo's own invariants | Sound. It is the only constructive port guidance under ratified canon. Rejection 4, on the RNG, says itself it is "not yet load-bearing" | `L1-04:918-995` [CHECKED] |
| `valoria-game`'s own container architecture (Meta, `ContainerBase`, GameDirector zoom stack, 5 autoloads) | STRAT adopts it as "the keeper" | convergence (with itself) | live-tree reads as of 2026-06-10 | Superseded in the ratified layer as to the state owner only: a single state owner behind a global name is what D-46 rules out (`L1-04:1065`, `:920-921`); L1-04 does not name `Meta` and does not rule out thin service autoloads. The 2026-08-18 run's autoload failures are no evidence against the pattern: they trace to five trivial root causes (an undeclared var, one annotation, a missing constant, a non-API call, a missing enum member), the rest cascading, "roughly 12 lines of fix" (`proposals/2026-08-18-recursion-interrogation-log.md:447-460`) | `STRAT:100,119` [CHECKED]; `G2 §F` III.1-III.3 [READER]; log [CHECKED] |
| CK3 / EU / KoDP | d+σ "basis" | — | name only | Not this lane's evidence | `G2 §G` [READER] |

### 2.3 Critical evaluation

- There is no game precedent for porting in the corpus. `research/00_INDEX.md` §3 says "None located" [CHECKED]. The precedent companion's porting-adjacent rows, such as the auto-resolve and cross-scale material in `COMP-6` §13.6, are about game design, not engine conversion.
- The one external reading that reaches canon is L1-04's Godot 4.6 docs passage (`:951`, a record of which documentation was read, not a pin). That raises a version dependency the preamble does not acknowledge. **Ratified Layer 1 reasons from 4.6 documentation while `CLAUDE.md` holds the version UNRESOLVED.** Whether the three facts it relies on (no exceptions, `assert` compiled out, `push_error` void) hold on 4.3 as well is not stated anywhere read [GAP]. If they do, the dependency is harmless. Nothing in the tree says which.
- `architecture/holonic_ARCHITECTURE.md:1468,1960` and `engine/season/harness/probes.py:2227` reason from "Godot 4.0" API availability (`WorkerThreadPool.add_group_task`) [CHECKED]. That is a floor, not a pin, and consistent with any 4.x.

## 3. REPOSITORY WORK

### 3.1 Heads and code: what runs, what is scheduled

| object | state as stated | what this lane observed |
|---|---|---|
| `CURRENT.md:38` GO row | head = STRAT, PROPOSED; "ED-GO-0001; Gate-0 waits on ED-1051" | Stale: ED-1051 resolved 2026-10-08 [CHECKED] |
| `registers/handoffs/HANDOFF_GO.md` | Open table empty; two standing orders (`CLAUDE.md` §6) | The table is empty while the plan holds three open GO rows. The handoff points to no plan row [CHECKED] |
| `registers/editorial_ledger_go.jsonl` | 0 rows; archive holds ED-GO-0001 only (lane activated 2026-08-14) | GO-lane work is recorded under IN ids (ED-IN-0017, ED-IN-0193) and PC ids (ED-PC-0013) [CHECKED] |
| Plan GO-01 | `J:J-9`, B-Z; "the ruled version where code reads it; the tenth attribute name" | Bundles two unrelated rulings, the engine version and the attribute name, with no reason given. Its EXIT is unsatisfiable as scoped while `README.md` and `references/glossary.md` pin 4.6 (§0 item 5) [CHECKED `_part7:86-91`] |
| Plan GO-05 | BLK:GO-01; manifest resource lists module paths (SM-13); `.gd` RESIST re-export | Its own gate, IN-05, is met. Only J-9 holds it. The manifest half has no stated dependency on the version [CHECKED `_part7:101-106`] |
| Plan GO-06 | BLK on a `valoria-game` checkout; the parity reader against the shrunk `MAPPING` | Not checkable here, as it says itself [CHECKED `_part7:108-113`] |
| Plan PC-05 | BLK:GO-01, GO-05; `combat_config.gd` RESIST re-export; "until then annotate it stale" | A partial annotation exists: `combat_config.gd:57-58` says "Fuller re-export of RESIST / GAP_EXPOSURE / … is the deferred module port" and "Key-log parity known-red". It does not say the RESIST values are superseded, and the RESIST block comment at `:33` carries no marker [CHECKED] |
| Plan M3 (main file `:209-216`) | GO-02 (= IN-42) and GO-03 landed at B-C; `engine/autoload/engine_clock.py` deleted; spine = `engine/season/loop/driver.py` + `calendar.py` | Consistent with `MC:716-718` [CHECKED] |
| `engine/engine_params/` | 7 JSON + `params_tables.yaml` | See the table below |

**What is actually exported** [CHECKED: listing, keys, CI lines]:

| artifact | writer | gate | Godot reach |
|---|---|---|---|
| `combat_engine_v1.json` | `tools/export_engine_params.py` from `modules/combat/config.py` + `core.py` | blocking (`valoria-ci.yml:130`) | Indirect, through `game_constants.json`. The skeleton `.gd` is **not** generated from it: hand-transcribed, 4 of 12 RESIST cells drifted (tracked: `ED-PC-0013` item 1, PC-05) |
| `game_constants.json` | `tools/export_game_constants.py` | blocking (`:137`) | **The only Python→Godot bridge.** 6 constants (`COMBAT_POOL_MINIMUM 5`, `KNOT_FORMATION_OB 2`, `KNOT_FORMATION_TN 7`, `SEASONS_PER_YEAR 4`, `TN_STANDARD 7`, `WEAPON_TN_BASE 7`), 2 collisions (`POOL_FLOOR`, `MOMENTUM_MAX`), 2 divergences (`accord_range`: port integer 0-3 vs no oracle model; `coherence_bands`: port 10→0 track vs ruled two-quantity distance). Its reader half is in `valoria-game` |
| `sim_params.json` | `tools/export_sim_params.py` | via `tests/valoria/test_export_sim_params.py`, not a CI line (`.github/workflows/valoria-ci.yml` does not name `export_sim_params`) | none named; 274 params, 116 cited, 158 uncited |
| `descriptors.json`, `names.json`, `composition.json` | their exporters | blocking (`:140,144,157`) | Python runtime readers only. `composition.json` exports `composition_roles:` but not `modules:`, which the seam reads raw at runtime (ED-IN-0017 F8) |
| `value_pointer_links.json` | `tools/link_values_pointers.py` (the only `*.py` that names it) | none: `valoria-ci.yml` does not name it | none named |
| `params_tables.yaml` | frozen capture | none | reference only (`CLAUDE.md` §5); holds pre-ruling degree bands (`engine/dice_engine/dice_engine.py:262`) |

### 3.2 Design documents and proposals

| path | status as stated | what it defines | grounding cited | assessment |
|---|---|---|---|---|
| `godot/godot_conversion_strategy_v1.md` | PROPOSED, Jordan-vetoable; Key text `[RETIRED ED-IN-0232]`; version "held at J-9" | conversion unit = module contract; four directional laws (law 3, lateral = Keys, retired); 4 value buckets; parity protocol V.2 (named draws, recorded replay, statistical parity, float discipline; Key-log equality retired); Gate-0 G0.1-G0.5 (three retired); a 27-row module table with waves S/1-4/R; drift census D1-D8 of `valoria-game`; frictions R1-R10; `[OPEN — Jordan]` 1-8 | design corpus and both repos as of 2026-06-10; no research | **Partly superseded and partly contradicted.** It predates `engine/season/` entirely. Its inventory is of `valoria-game` frozen since 2026-06-06 (`G2 §F`). Its cross-scale stage names `cross_scale/`, which retired at plan position 28-iii (`references/ci_checks_registry.yaml:324`) [CHECKED]. Its Meta single-state-owner recommendation contradicts L1-04's D-46 (`:1065`); it holds that ruling open itself (`:216`). What survives as live intent: named draws, float discipline, oracle-retained-until-parity (V.4), the per-module param export |
| `godot/godot_architecture_specification.md` | "STALE REFERENCE — predates the d+σ resolution model" | four-layer runtime (Content/Conflict/Resolution/Progression, not governance Layers); Tracker `scope:owner:id` with a seasonal cap; Consequence IMMEDIATE/DEFERRED; SituationGenerator; 5 resolution modes; containers; zoom depth 3; phases 0-9, "~28-38 weeks" | none | Stale by its own head (`:5`). Its version lines are floors, "Godot 4.x" (`:4`) and "Godot 4.3+" (`:675`), not pins [CHECKED]. `godot/README.md` lists it with no stale flag (`G2 §H`) [READER] |
| `godot/{scene_tree_architecture,gm_to_engine_conversion,data_serialization_spec,implementation_sequence}.md` | "STALE / PARTIALLY SUPERSEDED (2026-06-30)… Do not implement from this doc" (ED-1054) | 7 autoloads; 10 scene transitions; a 7-row GM→engine registry (POI stunt bonus, Lock drift, fieldwork thresholds 3/5/8, Piety Track partials); `.tres` schemas; G1-G7 over 20 weeks | none | Superseded. Their mechanics are v30 prose (Piety Track contest, Scar, Lock drift) with no code reader. ED-1054 is still `open` [CHECKED] |
| `godot/README.md` | no Status; "PROPOSED and largely un-executed" | the index of the above | — | Stale: "first action items are Gate-0 G0.1 (Key schema v2)"; "1 of 27 modules" [CHECKED] |
| `godot/skeleton/` (8 `.gd`, 12 `.tres`) | not runnable (`CLAUDE.md` §6) | combat slice: `CombatConfig`, strike/wound modules, `EngineManifest`, `KeyTypeResource`, 4 `key_types/*.tres` | "Ported from designs/scene/combat_engine_v1/config.py" | Built on the retired Key substrate (`key_type_resource.gd`, `data/key_types/`). `extends BaseEngine`, defined nowhere. RESIST is 4 of 12 cells off the oracle [CHECKED] |
| `.designs/systems/_architecture/reference/videogame_mode_spec.md` | "CANONICAL — single-mode extraction reference for Godot implementation" under an ARCHIVED-NOT-CANON banner | two scales with no mode switch; zoom depth 3; Domain Echo; containers; discards GM adjudication and mode switching | v30 docs | Quarantined. Its status contradicts its banner (`A7.3 §H`) [READER]. Its discards (no GM, no mode switch) remain consistent with `CLAUDE.md`'s preamble |
| `L1-04` §C.8-§C.12 | RATIFIED (ED-IN-0204) | Godot degradations; shape→construct table; five rejected idioms; typed `Result` (shape PROPOSED, `:993`) | the Godot 4.6 docs | **The live port doctrine.** It names the port's parity target: Part E step 13, the Godot shell, is done when "a headless run prints the Python oracle's hash in the integer domain" (`:1119`) [CHECKED]. Its stale parts: "the Key substrate the port already ingests (`engine/engine_params/`)" (`:1000-1001`) contradicts ED-IN-0232; `engine/autoload/dice_engine.py` (`:1000`) does not exist; `shape.py`/`seam.py` counts are stale [CHECKED] |
| `MC` (wiring block) | `status: EXTRACTED_STAGE1`; enums `[ASSUMPTION]`-grade | per module: `build`, `godot` (`gd-ported`/`python-oracle`/`no-oracle`/`retire`), `port_rank`, `parity` | registry-derived | `combat` reads `gd-ported` (`:882`), true by the enum's own definition, "a GDScript port exists (the skeleton slice)" (`:963`). The false claims are in its notes: "PORTED + validated to the Godot shape" (`:872`), "the port regenerates from THIS, never hand-edits" (`:835`), "the template every other port copies" (`:974-975`), against a hand-transcribed slice 4 of 12 RESIST cells off. `parity: key-log` on 20 rows, disposed of at ladder 2 by `ED-IN-0017` F9. `engine_clock`: `build: live` but `godot: no-oracle` with an `[ASSUMPTION]` state row (`:722,734`) [CHECKED] |
| `registers/editorial_ledger_in_archive.jsonl:195` (ED-IN-0017, 2026-10-12) | resolved; "asserts no Godot engine version" | ten port-facing findings F1-F10: string-resolved module entries, import-order registration, unbounded `sys.path` inserts, module state at the seam, anonymous RNG, untyped outputs, string-typed refusal, a runtime read of non-exported `MC` with silent `unknown` fallback, stale contract rows, `engine_clock` trigger met in `doc:` only | file-by-file reads at `5422ed1e` / `175384fc` | **The strongest GO artifact.** Spot-checked: F9 and F10 hold at HEAD [CHECKED]. It closes every finding at a ladder step, but nothing in the plan schedules F2, F5, F6, F7 or F8 (`_part7` GO rows name only SM-13 and RESIST) [CHECKED] |

### 3.3 Internal contradictions that matter

| subject | locator A | locator B |
|---|---|---|
| state owner | STRAT `:119,181`: Meta as single state owner (autoload); the ruling held open at `:216` | L1-04 `:1065` D-46, "world state behind a global name (Godot)", and `:920-921`, "`World` is NOT an autoload" for "global game state" [both CHECKED]. L1-04 never names `Meta`; the mapping is this lane's, and it covers the state owner only, not STRAT's thin services |
| autoload count | ARCHSPEC: one (Meta); `scene_tree_architecture.md`: 7 | STRAT III.3: live tree 5; `sim/README` 6 (`G2 §H`) [READER] |
| version asserted | `CLAUDE.md` preamble: "nothing here may assert one"; it acknowledges that "godot/ here documents another" | live pins outside `godot/`: `README.md:3,10` and `references/glossary.md:36`, both "Godot 4.6". Not pins: `ARCHSPEC:4,675` (floors), `L1-04:951` (which docs were read), `.designs/` sites (quarantined) [CHECKED] |
| plan's claim about the version | `_part7:88`: untrue "until that heading went at B-C" | the two live pins above survive B-C [CHECKED] |
| `engine_clock` doc | `CLAUDE.md` §6: `doc: null`; `CURRENT.md:38`: waits on ED-1051; `MC:903`: "its home doc remains unlocated" | `MC:717,727`: doc set at IN-42, ED-1051 applied [CHECKED] |
| combat resolver name | STRAT Part II: `dice_pool` (`G2 §F`) | `MC` `combat`: `d_sigma`; `social_contest`'s live entry returns `d10_sigma` (ED-IN-0017 F9) [CHECKED for MC] |
| module count | STRAT, `godot/README.md`: 27 | `MC`: 26 rows; no `articulation_layer` [CHECKED] |
| "remain valid" docs | STRAT `:4`; `godot/README.md:25`: scene_tree and gm_to_engine "remain valid as amended in Parts III–IV" | both banners: "Do not implement from this doc" (`G2 §H`) [READER]; `godot/README.md:17`, of the same four: "Do not implement from them" [CHECKED] |
| combat slice ported | `MC:872` "PORTED + validated to the Godot shape"; `:835` "the port regenerates from THIS"; `:974-975` "the template every other port copies" | `CLAUDE.md` §6: skeleton does not compile; RESIST hand-transcribed, 4 of 12 off [CHECKED]. Drift tracked as `ED-PC-0013` item 1 / PC-05; the `gd-ported` value itself is true by `MC:963` |
| settlements and NPC counts in the stale docs | 34 / 36 / 35 settlements; 13 / 14+ / 22 named NPCs; Disposition −5..+5 vs −3..+5 | `G2 §H` [READER]; moot, since the docs are stale |

**Built on the retired Key substrate (ED-IN-0232):** STRAT's law 3, V.2 item 5, G0.1/G0.3/G0.4, Stage-1 KeyStore and Stage-3 save/load (all marked); the `godot/skeleton/` Key-type files and `combat_config.gd:58` (unmarked); `MC`'s `parity: key-log` (unmarked in `MC`; disposed of at ladder 2 by `ED-IN-0017` F9); `L1-04:1000-1001` (unmarked); `godot/README.md` (unmarked) [CHECKED]. The campaign driver and `cross_scale/` that STRAT Part II and Stage 3 port are deleted; `engine/autoload/engine_clock.py` too (main plan `:214`) [CHECKED].

### 3.4 Critical evaluation

- **Layer 1 names the parity successor; the `godot/` documents do not.** Stage 2's per-module ritual set three gates: golden-master parity by Key-log equality, adjudicator-equivalent checks A1-A9, and property checks. ED-IN-0232 and ED-IN-0265 retired the Key log and the adjudicator (`MC:3-4`) [CHECKED]. RATIFIED L1-04 names the seeded content hash as "the only execution artifact this architecture has" (`:942-944`) and makes step 13, the Godot shell, done when "a headless run prints the Python oracle's hash in the integer domain" (`:1119`); the hash is `World.content_hash` (`engine/season/state/world.py:1338`) [all CHECKED]. What is missing is a `godot/` document that takes it up (STRAT still says "no replacement is ruled here", `:190`) and a runnable cross-repository instrument. ED-IN-0017 F9 cites STRAT's own retirement bracket for "parity on downstream state", which STRAT never specifies.
- **What the port depends on, as the tree stands.** (1) Typed exports: real but narrow. One blocking bridge carries 6 constants; the rest of the 274 sim params and the 669 KB prose capture have no Godot path, and §5 of `CLAUDE.md` names that hand-transcription risk itself. (2) The combat slice: the oracle is real and gated (`combat_engine_v1.json`); the port side is non-compiling and drifted, the drift tracked as `ED-PC-0013` item 1. (3) `engine_clock`: the doc pointer is closed; its wiring fields and `[ASSUMPTION]` state row are not (F10). (4) `valoria-game`: last observed failing to load its autoloads (2026-08-18) on five trivial root causes, "roughly 12 lines of fix" (`proposals/2026-08-18-recursion-interrogation-log.md:447-460`) [CHECKED], with its state unverifiable from here.
- **The lane schedules little and leaves its audit unread.** Three plan rows, all held on one Jordan ruling or another repository, against ten audit findings. The audit's own rule ("NOTHING HERE NEEDS JORDAN") means its findings are not held on J-9, yet no plan row carries them. This is an observation of coverage, not a work item.
- **Tier-3 rule respected.** No GO document cites `research/`. That suits a port.

## 4. JOIN: FUNCTION, VERB AND PRIMITIVE AGAINST EVIDENCE

GO owns no verbs. The rows are port primitives.

| primitive | repository claim (status) | historical | game / engine evidence | joined verdict | locator |
|---|---|---|---|---|---|
| engine version | UNRESOLVED, held at J-9 (`CLAUDE.md`; plan GO-01) | — | Jordan typed "4.6" three times as organizing instructions (`_part5:515`); L1-04 sources 4.6 docs; `valoria-game` `project.godot` declared 4.3 (2026-08-18 log) | **CONTRADICTED**: pinned at 4.6 in two live files (`README.md:3,10`; `references/glossary.md:36`) while ruled open; the other sites are floors, provenance notes or quarantined text, and the preamble already acknowledges the `godot/` conflict | §0 item 5 |
| conversion unit = module contract | STRAT IV.3 (PROPOSED) | — | none | **PARTLY**: `MC` exists and is exported in part; its `parity` value is dead (disposed of by `ED-IN-0017` F9) and its count drifted | `MC`; `G2 §F` |
| parity: named draws + recorded replay | STRAT V.2 (PROPOSED) | — | "standard deterministic-replay porting practice" (uncited) | **PARTLY**: streams are purpose-keyed in code (`H(…, purpose)`, `engine/season/state/ids.py:16-18`; `seam/wrappers/combat.py:222`; `L1-04:1053`); per-site naming inside `modules/*` is absent and mass battle can fall back to global `random` (`rngsource.py:45,60`) | ED-IN-0017 F5; §0 item 7 |
| parity: Key-log equality | STRAT V.2 item 5 | — | — | **RETIRED** (ED-IN-0232); STRAT rules no replacement, but L1-04 names the content hash (next row) | `STRAT:20,190`; `L1-04:1119` |
| determinism artifact: seeded content hash | `CLAUDE.md` §0.2; L1-04 `:942-944` and step 13 (RATIFIED) | — | — | **GROUNDED in code** (`World.content_hash`, `engine/season/state/world.py:1338`) and named by ratified Layer 1 as the Godot shell's done-condition; no `godot/` document adopts it and no cross-repository instrument runs it | `B2.2` H-118; `L1-04:1119` |
| typed param export → `res://data/` | STRAT Stage 2 step 1; `CLAUDE.md` §5 | — | — | **PARTLY**: `game_constants.json` (6 constants, blocking) is the only bridge | §3.1 table |
| combat slice | `MC:872` "PORTED + validated"; `:835` "regenerates from THIS"; `:974-975` "the template" (`gd-ported`, rank 0, true by `:963`) | — | HEMA facts feed the oracle (PC lane), not the port | **CONTRADICTED**: skeleton non-compiling, RESIST hand-transcribed and drifted (tracked, `ED-PC-0013` item 1), Key-based | §0 item 3 |
| `engine_clock` / season spine | doc set (IN-42); `build: live`; `godot: no-oracle` | — | — | **PARTLY**: Layer 0 still says `doc: null` | `MC:715-739` |
| state owner / autoloads | STRAT: Meta as single state owner, an autoload (ruling held open, `STRAT:216`); L1-04 D-46: world state never behind a global name, `World` threaded | — | Godot autoload idiom, rejected with reasoning | **CONTRADICTED** between PROPOSED and RATIFIED as to the state owner only (L1-04 does not name `Meta` and does not rule out thin service autoloads); L1-04 governs (Layer 1) | `L1-04:920-921,1065`; §3.3 |
| refusal as typed `Result` | L1-04 rejection 5; shape PROPOSED | — | 4.6 docs quoted | **GROUNDED** in the engine reference; the port debt it measures is stale-counted | `L1-04:950-995` |
| module manifest (SM-13) | GO-05 | — | — | **UNREACHED**: blocked on J-9 with no stated dependency on it | `_part7:101-106` |
| accord tracker | port: integer 0-3 | — | — | **CONTRADICTED**: oracle holds no accord model (divergence recorded) | `game_constants.json` |
| Coherence | port: 10→0 track | — | — | **CONTRADICTED**: oracle is a two-quantity distance (ED-WR-0010); the port's track models a different quantity from the oracle's | `game_constants.json` |
| Tracker / Consequence IMMEDIATE-DEFERRED; zoom depth 3; SituationGenerator | ARCHSPEC, videogame_mode_spec (stale / quarantined) | — | — | **UNGROUNDED** as port targets now: not the season loop's carriers (L1-04 §C.12 table) | `G2 §F`; `A7.3 §F` |

## 5. WHAT THIS LANE'S CORPUS DOES NOT COVER, AND WHAT YOU DID NOT READ

- [GAP: historical research — none exists for a port; not a defect.]
- [GAP: game precedent for engine conversion — none in the corpus (`research/00_INDEX.md` §3, §7).]
- [GAP: `jordanelias/valoria-game` — not in this container. Its version pin, compile state, `check_constants_parity.py` and drift since 2026-08-18 are unverifiable here. `CLAUDE.md`'s preamble says its `project.godot` and CI pin a version; not checked.]
- [GAP: whether L1-04's three 4.6 facts hold on 4.3 — not stated in any file read.]
- [GAP: W3 is interim. It has no `## X` section and covers parts 6-7 only. The GO entries were read directly in `workplans/valoria_master_workplan_v9_part7.md:84-113` and the main file `:209-216`, `:317-319`.]
- [SKIPPED: `B1_engine_data_2.md`, `B2_hole_register_2.md` — read for Godot and engine_params rows; none found beyond H-118 (`content_hash`) and NUMBER rows tagged `params` (H-121, H-167, H-170) with no port reach.]
- [SKIPPED: `A7_architecture_1.md`, `A7_architecture_2.md` — read only where they touch the port, `engine_clock` and campaign architecture (`A7.1 §H` flow §7 gaps; `A7.2 §H` KEA 5.15, NVR B11), per assignment.]
- [SKIPPED: bodies of `proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md` (69 KB), `F3_godot46.md` (61 KB), `03_CODE_SHAPE_GODOT_4_6.md`, `_session_provenance/…/repo_logs/R3_godot.md` — outside the assigned extractions; heads only. They are the lane's largest unread corpus.]
- [SKIPPED: `registers/handoffs/HANDOFF_GO_history.md` — narrative; not opened.]
- [CONFIDENCE: medium — the stale-docs and STRAT internals (`G2`) are taken from the extraction except where marked CHECKED; the STRAT lines on version, retirement, Meta and Gate-0 were opened.]

## 6. METHOD NOTE

Written from the reader extractions named in the head, with the locators marked [CHECKED] opened in the working tree. Then attacked by an independent read-only critic that checked about 45 claims: the headline verdict held, and no locator was wrong. Each correction below was verified against its source before it was applied.

1. Parity successor: ratified L1-04 names the seeded content hash (`:942-944`, `:1119`; `world.py:1338`); the gap is a `godot/` document and a cross-repository instrument, not a successor (§0 item 1, §3.2, §3.4, §4).
2. Named draws: streams are purpose-keyed in code (`ids.py:16-18,27-68`; `combat.py:222`; `L1-04:1053`); only per-site naming inside `modules/*` is absent; `rngsource.py:45,60` (F5 cites `:46`/`:61`) (§0 item 7, §4).
3. Combat slice: `gd-ported` is true by `MC:963`; the false claims are `MC:835,872,974-975`; drift tracked as `ED-PC-0013` item 1 / PC-05 and `gd-ported` as `ED-IN-0017` F9 (§0 item 3, §3.1, §3.2, §3.3, §4).
4. Version: of the four sites first listed, only `README.md` is a live pin; `ARCHSPEC` lines are floors, `L1-04:951` a reading note, `.designs/` quarantined; the preamble acknowledges the `godot/` conflict (§0 item 5, §2.3, §3.2, §3.3, §4).
5. Version: `references/glossary.md:36` added as a second live 4.6 pin, and the `.designs/` UI "Godot 4.2+" sites named (§0 item 5, §3.1 GO-01, §3.3, §4).
6. The 2026-08-18 autoload failure is a parse-error cascade on five trivial roots, no evidence against the Meta pattern (§2.2, §3.4).
7. PC-05: a partial annotation exists at `combat_config.gd:57-58`; the RESIST block at `:33` is unmarked (§3.1).
8. State owner: L1-04 never names `Meta`; the conflict is D-46 (`:1065`) with `:920-921`, the state owner only; STRAT holds the ruling open at `:216` (verdict, §0 item 2, §2.2, §3.2, §3.3, §4).
9. Stale `godot/` documents: five of seven, not four; `godot/README.md:17` against `:25` (§0 item 6, §3.3).
10. `parity: key-log`: recorded and disposed of at ladder 2 by `ED-IN-0017` F9, not open (§0 item 8, §3.2, §3.3, §4).
11. A work-item phrase removed from the Coherence row; "organizing" spelled "organizing" (§4).
12. `value_pointer_links.json`'s writer named (`tools/link_values_pointers.py`); the CI workflow names neither it nor `export_sim_params` (§3.1).

§0 re-ranked after corrections: the combat-slice registry claim moved up to item 3; the version item moved down to item 5 and the named-draws item to item 7; the dead `parity` value became a recorded disposition under item 8.
