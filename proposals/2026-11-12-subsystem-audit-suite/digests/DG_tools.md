# Digest tools

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: everything under `tools/` (54 `.py` plus `README.md` = the 55 assigned files; `tools/__pycache__` ignored). Read in full, to the end. Entries follow assignment order except `valoria_local.py` and `validate_ed_citations.py`, which appear in the opposite order near the end. Nothing skipped. Nothing was run (no instruments); counts quoted from artifacts were read from the committed JSON/YAML with a one-line loader, and are marked as read where they are not in the tool's own text.

Wiring facts used throughout (read once, from the sources, not from the tools' own claims):
- `.github/workflows/valoria-ci.yml` job `validators` (BLOCKING, no fail-fast): ci_register_size_check, ci_co_file_checker, ci_editorial_checker, ci_pp_frozen_check, ci_naming_check, ci_design_prose_quarantine, ci_names_consistency, export_engine_params --check, export_game_constants --check, export_descriptors --check, export_composition --check, export_npc_roster --check, export_names --check, ci_sim_fabrication_check, ci_claim_provenance_check, ci_vetting_check, validate_ed_citations, broken_dependency_checker, freshness_gate (`valoria-ci.yml:119-188`).
- Job `validators-report` (`continue-on-error`, `w` wrapper swallows the exit): m1_acceptance --summary, ci_naming_check --warn, currency_consistency_check, ci_quantity_vocabulary_check, mechanics_index_gen --strict, ci_generation_consistency, canon_coverage_check --strict --json, ci_module_shape_check, ci_vacuous_assertion_check (`:237-257`).
- Separate jobs: `ci_golden_modes_check` (job field-goldens, `:518`), `compliance_check.py --check-only --repo-state .` (job compliance-check, `:586`), and `syntax-check` py_compiles every `tools/**/*.py` (`:52-54`).
- Local tier: `.githooks/pre-commit` runs `python tools/valoria_local.py --staged` only; `.claude/settings.json` wires exactly two hooks: `hook_naming_guard.py` (Write|Edit|MultiEdit) and `hook_md_sweep_guard.py` (Grep|Glob). SessionStart and Stop are empty arrays.
- `references/ci_checks_registry.yaml` has rows for the CI tools above plus `build_identifier_census`, `fold_ledger_to_latest`, `export_battle_orders` (`ci_job: ""`); it has NO row for `export_sim_params`, `gen_sigma_parity_goldens`, `link_values_pointers`, `triage_work_items`, `join_audit_workings`, `verify_handoff_split`, `methodology_drive`, `tag_normalizer`, `build_engine_atlas`, `tests_for_diff`, `session_provision` (these are utilities, not gates).
- Registry header says `subject: game` is "NOTHING IN THIS FILE IS game" yet two rows (`export_battle_orders`, `export_npc_roster`) carry `subject: game` (`ci_checks_registry.yaml:314,322`) while the header at `:24-26` says nothing is game. Internal contradiction in the registry.

---

### tools/README.md
- **What it is:** directory guide, tables "generated from" the registry 2026-07-11 (ED-IN-0033); no author-lane stated.
- **Status:** no Status line. Reading: STALE (historical in large part).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Claims the CI/Integrity tables are "downstream of" `references/ci_checks_registry.yaml`, the single source of truth (`:3-8`); the tables were not regenerated after later changes.
  - Lists CI job names that no longer exist (`register-sizes`, `co-file-check`, `editorial-check`, `naming-check`, `names-consistency`, `engine-params-roundtrip`, `ed-citations`, `vetting-check`, `sim-fabrication-check`, `generation-consistency-check`, `canon-coverage-check`, `mechanics-index-check`, `currency-consistency`, `quantity-vocabulary-check`, `module-shape-check`) at `:25-47`; the live workflow has only `validators`, `validators-report`, `field-goldens`, `compliance-check`, etc. (`valoria-ci.yml:79,191`).
  - Row for `export_key_types.py --check` (`:41`) names a retired Key-substrate tool (ED-IN-0232); not marked RETIRED, unlike the other dead rows.
  - Says `integrity` CI job (`:20,:49`) which was collapsed into `validators` 2026-08-01 (its own opening paragraph admits the collapse at `:13-14`).
  - Utility table omits live tools: `export_game_constants`, `export_npc_roster`, `export_names`, `export_battle_orders`, `export_sim_params`, `pathres`, `registry`, `definitions_store`, `vocab_store`, `tag_normalizer`, `methodology_drive`, `triage_work_items`, `join_audit_workings`, `link_values_pointers`, `verify_handoff_split`, `m1_acceptance`, `fold_ledger_to_latest`, `tests_for_diff`, `session_provision`, `freshness_gate` is mentioned only under Integrity.
  - Many rows are strikethrough/RETIRED tombstones with `FORK:` pointers (`:26-81`); it describes `session_status.py`, `workplan_status.py` etc. that do not exist.
- **Conflicts / stale:** contradicts CLAUDE.md §3 ("look at the tree, do not read a description of it") by being exactly a description that has drifted; `designs/...` paths (`:65,:81`) are dissolved dirs.
- **Open items:** none; a delete-or-regenerate decision nothing owns (a README guard would be forbidden by §0.1 pt 5, so deleting is the consistent option).

### tools/broken_dependency_checker.py
- **What it is:** blocking CI validator, ED-1053 port to working tree; stdlib only.
- **Status:** no Status line; live. Blocking (`validators`).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Four checks (`:481-486`): `references/propagation_map.md` file refs (remap-aware via restructure_ledger, `:92-122`); `references/canonical_sources.yaml` refs, bare membership with NO remap (`:124-131`); live-status editorial ledger rows across main + 9 lane files + `_archive` siblings (`:228-283`); `ci_checks_registry.yaml` coverage (`:318-470`).
  - Registry coverage: (a) every registry `path:` exists; (b) every `ci_job:` is a real job id; (c) every `python3 tools/X.py` in a non-comment workflow line has a registry row (`:350-460`). Sub-check (b2) "the job actually invokes the tool" is DEAD: `_gate_jobs()` returns `[]` permanently (`:34-52`), so a registry row's `ci_job` claim is no longer cross-checked; the code appends a one-time error string (`:374-384`) that is never fatal.
  - It has a THIRD independent parser of `restructure_ledger.md` (`_load_restructure_map`, `:138-147`) which CLAUDE.md §8 names as a known live violation; fork predicate shared with `pathres.FORK_PREFIX` (`:171`).
  - `extract_file_refs` patterns include dissolved roots `designs`, `compilation` (`:78-81`), harmless but dead.
  - `get_all_repo_files` walks everything except `.git` (`:55-63`), so refs resolving into `.designs/`/`.audit/` count as existing.
- **Conflicts / stale:** the registry's header asserts `check_ci_registry_coverage()` "enforces that join in both directions" (`ci_checks_registry.yaml:91-93`); direction (registry row -> workflow job invocation) is not enforced any more. README says it runs inside `integrity` job (stale).
- **Open items:** whether (b2) should be restored or the registry's `ci_job` field removed; the dependency checker's tests (`tests/valoria/test_forked_status.py`) pin only the FORK/ledger branch.

### tools/build_engine_atlas.py
- **What it is:** generator of `references/ENGINE_ATLAS.md` + `engine_atlas.json` (ED-IN-0152); `--check` mode. Not in CI or any hook.
- **Status:** no Status line. Reading: largely DEAD/unclear. Outputs are untracked (`ls references/ENGINE_ATLAS.md` fails).
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Reads the subsystem roster by regex from a `.designs/` markdown table (`## 3. Roster`) in `subsystem_flow_skeletons_v1.md` (`:61-62,:104-118`): prose as the input of a tool, §0.05 cl.2 forbids `systems/**/*.md` as tool input; here it is `.designs/` and the tool's docstring justifies it (`:58-61`) as "sanctioned shape", contradicting §0.05 cl.1 ("a .md is never the authored head of a fact code reads").
  - Both execution inputs are permanently absent (`:132-135`, retired 2026-09-29 plan position 28-i); so `trace` and `emap` are always empty and sections 1-2 of its output render "not in trace" for everything.
  - The coverage check AST-parses `systems/<sub>/**/*.py` public defs and greps them in a skeleton `.md` (`:288-308`); the skeleton files live at `systems/<x>/<x>_flow_skeleton_v1.md` per the banner (`:69`) but `systems/` holds no .md (quarantine), so `skeleton_present` is False for most subsystems.
  - `nomenclature_audit` counts bare occurrences of every contract name across `systems/engine/references/registers/tools` text (`:373-420`); evidence-only, enforces nothing.
  - Run on demand only by the `generated_layer` fixture in `tests/valoria/conftest.py:102` (and named in `test_engine_params_bridge.py:101`).
- **Conflicts / stale:** `ci_co_file_checker.py:101` still cites `build_engine_atlas --check` as a check; header says skeleton files in `systems/` (they were moved to `.designs/`).
- **Open items:** no live consumer of ENGINE_ATLAS beyond the fixture; whether the tool should be deleted (outputs untracked, inputs retired, process-only).

### tools/build_identifier_census.py
- **What it is:** generator of per-subsystem `systems/<sub>/_identifier_census.yaml` and `references/identifier_census.json`: for each identifier in design-doc prose, whether a Python name or typed-export key defines it (Jordan 2026-08-04).
- **Status:** no Status line; registry row says "NO LONGER A FRESHNESS GATE" (ED-IN-0194). Live as an on-demand builder; outputs untracked (`references/identifier_census.json` absent).
- **Bears on:** PROCESS (measures prose-vs-code gap; relevant to every subsystem lane as a backlog signal).
- **Content that matters:**
  - Dispositions are BUILT / SUPERSEDED-DOC / UNRESOLVED (`:418-426`); BUILT is a NAME match only (own caveat `:432-440`).
  - Inputs are design prose in `.designs/systems/<sub>/reference/*.md` and `systems/<sub>/*.md` (`:371-373`) - prose is the input but the output is evidence-only, no gate.
  - `built_names()` harvests every function/class/param/module-level name/dict-key in `engine/ systems/ tools/` and all keys of `engine/engine_params/*.json` (`:220-285`); includes a Key-substrate step reading `key_type_registry_v30.md` (`:286-293`) although the Key substrate is RETIRED (ED-IN-0232) - dead if the file is gone.
  - A bare `--subsystem` run refuses to overwrite the roll-up (`:530-533`).
  - Callers: `tests/valoria/conftest.py:103` (generated_layer), `tests/valoria/test_flow_skeletons.py`, `tools/ci_common.py:409` (comment). The CI workflow only mentions it in comments (`valoria-ci.yml:175`).
- **Conflicts / stale:** `built_names` counts tools/ as "built", so a design identifier matching any tool symbol reads BUILT (self-acknowledged, `:223-225`); the CLAUDE.md-cited count "~736 unknown vs ~46 known" is from 2026-08.
- **Open items:** the UNRESOLVED bucket (unbuilt vs outmoded) is "Jordan's call" and nothing ever consumed it.

### tools/canon_coverage_check.py
- **What it is:** bidirectional check between `Status: CANONICAL` headers and `references/canonical_sources.yaml`; ED-IN-0031 port off GitHub API.
- **Status:** no Status line; live but nearly vacuous. Report-only (`validators-report`, `--strict --json`, the `w` wrapper swallows exit).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Walks `systems/` only (`:73,:121-149`), for `.md/.yaml/.svg` files containing the literal `Status: CANONICAL`. `git ls-files systems | grep -c '\.md$'` = 0, so `declared` contains at most a few yaml/svg files while `registered_no_header` lists every `systems/` path in canonical_sources (`:174-176`): the output is dominated by the quarantine move, not by drift.
  - Prose is the mechanism here: whether a doc is "canonical" is decided by a header string, which is §0.05's named non-mechanism (`## Status: RATIFIED` line).
  - Pure reader; `if relroot == '.audit'` guard is dead (`:125-127`, admitted "dead under systems/").
  - Docstring still says walks `designs/` (`:22,:32-35`), stale.
- **Conflicts / stale:** docstring vs code (designs/ vs systems/); its documented "27 registered-no-header" figure (ci yml comment `:212-215`) predates the ED-IN-0231 quarantine.
- **Open items:** none that matter to the game; candidate for deletion (process-only, reads prose as mechanism).

### tools/ci_claim_provenance_check.py
- **What it is:** blocking validator (ED-PC-0040): a ledger entry stating measured numbers must carry `MEASURED-BY: <path>` naming an instrument that exists.
- **Status:** no Status line; live, blocking (`validators`). Scope is a process artifact (editorial ledgers), not game state.
- **Bears on:** PROCESS (PC, IN lanes' ledgers).
- **Content that matters:**
  - `LEDGERS` maps 6 ledger files to cutover ids (`ED-PC-0040`, `ED-IN-0087`), incl. the `registers/archive/*pre-2026-09.yaml` fragment (`:54-100`); only PC and IN lanes are covered, no other lane's claims are checked.
  - Claim detection is five narrow regexes: `x -> y`, `n=NN`, `pp`, `mean N`, `decided N%` (`:114-120`); an entry without those shapes is never examined.
  - Verifies only that a named path EXISTS (in tree, in a `.designs/`/`.audit/` mirror, or as an exact row in the restructure ledger via `pathres.load_alias_map`, `:136-179,:293-322`); it cannot check the number is right (own admission `:19-22`).
  - Cutover is an ID comparison (`_is_pre_cutover`, `:181-204`).
  - Owns `QUARANTINE_MIRRORS = (('', '.designs/'), ('audit/', '.audit/'))` (`:133`): `.designs/` PREPENDS, `.audit/` REPLACES the `audit/` prefix; CLAUDE.md §3 names this constant as the one place that difference is written (consistent).
- **Conflicts / stale:** comment cites `tools/ci_claude_workflow_paths.py` as the IN-lane instrument (`:58`) - not in tools/ now `[UNVERIFIED that it is retired; not in the ls]`.
- **Open items:** the claim-pattern set cannot see most real measured claims (percentages other than "decided", ratios, counts).

### tools/ci_co_file_checker.py
- **What it is:** blocking CI/pre-commit validator of three "co-file" rules over the git diff.
- **Status:** no Status line; live, blocking. Rule 4 retired with tombstone `:85-123`.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Rule 1: a changed `systems/.+_v30.md` with added lines must co-change `references/canonical_sources.yaml` (`:50-57`). Structurally unreachable: `systems/` holds no `.md` (quarantine gate, ED-IN-0231), so this rule can never fire.
  - Rule 2: any change under `registers/patch_register*` requires `references/propagation_map.md` in the commit (`:60-66`).
  - Rule 3: any file under `tests/sim/` requires `tests/coverage_matrix.md` (`:73-83`) - reads a coverage doc as a gate.
  - Runs at module scope (no functions, no `main`), unlike its siblings; not importable for tests without side effects.
- **Conflicts / stale:** the tombstone lists `build_engine_atlas --check` as a surviving freshness gate (`:100-109`), though that tool is wired nowhere; docstring says it checks "design->params" (retired).
- **Open items:** Rule 1 dead; whether `tests/coverage_matrix.md` and `propagation_map.md` still exist or are read by anything beyond this gate.

### tools/ci_common.py
- **What it is:** shared primitives for the tools (changeset oracle, repo root, lane roster, status reader, ledger readers); ED-IN-0159 G7.
- **Status:** no Status line; live; imported by nearly every tool. Registry says it has "no subject".
- **Bears on:** PROCESS, CORE (defines `MODULE_CODE_ROOTS`, the map of where game Python lives).
- **Content that matters:**
  - `get_changed_files / get_added_lines / get_removed_lines` over modes `ci|staged|local` (`:182-264`); CI mode derives the base from `GITHUB_EVENT_*` env, falling back to `HEAD~1` (so a shallow clone with no parent diffs against the empty tree and every file reads "added").
  - `MODULE_CODE_ROOTS = (('systems','*/sim'),('modules','*'))`, `MODULE_CODE_DIRS`, `MODULES_WITH_OWN_EXPORT = ('combat',)` and `sim_reference_roots()` (`:90-139`): the single answer to "which directories hold game Python"; consumed by the fabrication check, quantity vocab check, `export_sim_params`, and the prose quarantine. `combat` is outside every sim root and gets its own exporter.
  - `LANE_CODES = (MB, PC, FI, SC, FA, WR, IN, GO, SE)` (`:339`); `STATUS_RE`, `STATUS_HEAD_LINES = 80`, `doc_status`, `tokens = len//4` (`:424-488`); `load_yaml`; editorial-ledger readers `editorial_ledger_paths / read_editorial_ledger_rows / fold_ledger_to_latest` (`:648-757`).
  - Docstring `load_yaml` carries a hand-kept count ("17 bare yaml.safe_load calls remain in tools/") pinned by a test, a count the docstring itself shows decrementing only by retirement (`:502-528`).
  - `fold_ledger_to_latest` here duplicates the CLI tool `tools/fold_ledger_to_latest.py` in name (that one imports this? see its entry).
- **Conflicts / stale:** big comment blocks narrate retired tools (`obs_core`, `observability/`, `ci_workplan_pointer_check`, `atomizer`, `index_gen`); `STATUS_RE` lets bare `Status:` match, so a prose line "Status: ..." anywhere in the first 80 lines counts.
- **Open items:** none in the game; the file is 44 KB of mostly historical narration around ~15 small functions.

### tools/ci_design_prose_quarantine.py
- **What it is:** blocking gate: no tracked `.md` under `systems/**`, `modules/**` or `engine/**` except `engine/season/**` (ED-IN-0231).
- **Status:** no Status line; live, blocking (`validators`); falsifier `tests/valoria/test_design_prose_quarantine.py`.
- **Bears on:** PROCESS, CORE (protects the game trees from prose), all subsystem lanes (explains why no design doc sits in `systems/`).
- **Content that matters:**
  - `GAME_TREES = (*(d+'/' for d in ci_common.MODULE_CODE_DIRS), 'engine/')`, i.e. `systems/`, `modules/`, `engine/` (`:62`); `EXEMPT = ('engine/season/',)` (`:68`).
  - Reads `git ls-files` (or the index with `--staged`), so an untracked `.md` is invisible.
  - Cites §0.1 pt 5: argues the guarded artifact is load-bearing on the game "because a session reads prose in the code trees when resolving a mechanic" - the load is on an agent's reading, not the engine's runtime.
  - Consequence for audits: `engine/season/**/*.md` (case briefs, run reports) is the only prose permitted in game trees.
- **Conflicts / stale:** none found.
- **Open items:** none.

### tools/ci_editorial_checker.py
- **What it is:** blocking gate: a changed `.md` under `systems/npcs/`, `systems/world/` or `canon/03_*` (>=200 chars, with added lines) must contain `[EDITORIAL:`/`[PROVISIONAL:`/`[EDITORIAL GATE]`.
- **Status:** no Status line; live, blocking (`validators`).
- **Bears on:** PROCESS, WR, CHAR (guards the editorial paths for NPCs/world).
- **Content that matters:**
  - Path set `('systems/npcs/','systems/world/','canon/03_')` (`:23-30`); two of the three prefixes cannot hold a `.md` after the quarantine (`ci_design_prose_quarantine`), so only `canon/03_` is reachable.
  - Deleting a governed `.md` requires an `[EDITORIAL]` marker in the last commit message (`:46-64`), reading `git log -1` (the tip, not the commit under test).
  - Encodes "user retains exclusive authority over setting, worldbuilding, characters, narrative, faction behaviour" (`:96-97`) - a prose convention enforced by string presence.
  - Module-scope script like `ci_co_file_checker`.
- **Conflicts / stale:** `systems/npcs/` and `systems/world/` are quarantined paths; an NPC/world design now lives in `proposals/` or `.designs/` and escapes this gate.
- **Open items:** none.

### tools/ci_generation_consistency.py
- **What it is:** "v40 generation currency" check: every canonical design doc exists, has a Status line, and is not in the supersession register.
- **Status:** no Status line; report-only, always returns 0 (`:114-115`); in `validators-report`.
- **Bears on:** PROCESS.
- **Content that matters:**
  - The doc set comes from regexing `canonical_sources.yaml` lines for keys `design_doc|index|infill|integration_plan_doc|spec|related` pointing at `designs/` or `systems/` `.md` (`:39-51`). `grep -cE` of those patterns over `references/canonical_sources.yaml` = 0 and `systems/` holds no `.md`, so it checks ZERO documents and prints OK.
  - `RECOGNIZED` Status vocabulary: CANONICAL, CURRENT, CANON, WORKING, DESIGN, REFERENCE, PROVISIONAL (`:37`); non-recognised only INFO.
  - Treats a `## Status:` line as the currency signal - the §0.05 non-mechanism.
- **Conflicts / stale:** docstring cites `designs/audit/2026-06-28-deprecation-currency-sweep/v40_generation_plan.md` (dissolved tree). CLAUDE.md §1 still names "Generation v40" as the live surface.
- **Open items:** its subject has been emptied; nothing to flip to blocking.

### tools/ci_golden_modes_check.py
- **What it is:** CI job `field-goldens` runner: executes `systems/mass_battle/sim/bat.py --check` in three pinned digest modes; blocking, CI-only (not in `valoria_local`, ~275 s).
- **Status:** no Status line; live; the one validator here that RUNS GAME CODE.
- **Bears on:** MB, DICE (byte-exact battle regression oracle). Load-bearing on the game.
- **Content that matters:**
  - `MODES`: `unit_field_mor0` (FIELD_MOVEMENT=1, PER_CELL=0), `cell_field_mor0` (PER_CELL=1), `cell_legacy_mor1` (FIELD_MOVEMENT=0, MB_CELL_MORALE=1) (`:127-137`); the two legacy grid modes are no longer pinned by anything (registry notes, ED-MB-0061).
  - `FIELD_PINS` (`:56-116`) pins ~75 env toggles to their recorded values - the MB tuning surface as shipped (e.g. ROUT_CASCADE_FRAC 0.6, POOL_QUALITY_SCALE 0.8, K_LINEAR 12, K_SQUARE 0.25, LANCHESTER_ENABLED 1, MB_AMMO_ENABLED 1, MB_VOLLEYS_START 10, MB_SUPPORT_RANK_CAP 1, MB_CELL_EXCLUSION 1). These are game numbers hand-copied into a CI tool; drift guard is `tests/valoria/test_field_golden_pins.py` (asserts equality with `config.py` env defaults).
  - Green means the digest equals `bat.py`'s `EXPECTED` golden, not that battle balance is right; the mode assertion `DIGEST {mode}` prevents a perturbed selector from matching another golden (`:174-179`). `--perturb NAME=VALUE` is the mutation check.
  - Docstring says "TWO"/"both modes" in places while MODES holds three (`:3-10,:30`).
- **Conflicts / stale:** wording only; the doc names `PYTHONPATH` fix after port to `systems/mass_battle/sim/` (2026-08-24).
- **Open items:** whether the cell/field golden digests encode the intended weapon-carry/cell design (MB audit): the pins record what shipped, not what should.

### tools/ci_module_shape_check.py
- **What it is:** report-only hygiene lint: runtime code must not `sys.path` into a `tests/` tree or import `tests.*`; INFO-tier lists untagged module-scope numeric constants in the combat engine.
- **Status:** no Status line; live, report-only (`validators-report`; exit 1 never propagates).
- **Bears on:** PC, CORE.
- **Content that matters:**
  - `RUNTIME_ROOTS = ('sim','systems/combat/combat_engine_v1','engine', 'modules')` (`:49-54`); `sim/` is a dissolved dir (silently skipped by `isdir`).
  - INFO tier scope: `systems/combat/combat_engine_v1/` and `modules/combat/` (via `MODULES_WITH_OWN_EXPORT`) except `config.py` (`:58-59,:107-113`).
  - Cites `.designs/.../holonic_container_doctrine_v1.md §3` (archived prose) as its rule's authority, contrary to §0.05.
  - Overlaps `tests/valoria/test_engine_does_not_import_systems.py` (the CLAUDE.md §3 named execution artifact for the engine seam); this tool is regex-based, that test is a subprocess import.
- **Conflicts / stale:** `PROVENANCE_TAGS` list includes `'ed-'` (any comment containing "ed-" substring, e.g. "fixed-" passes).
- **Open items:** none.

### tools/ci_names_consistency.py
- **What it is:** blocking gate: `descriptor_registry.yaml` and `proper_noun_registry.yaml` mirror fields must equal `names_index.yaml` canonicals, both directions (reverse direction added 2026-09-16).
- **Status:** no Status line; live, blocking (`validators`).
- **Bears on:** CHAR, FA, SE, WR (names of attributes `attr.*`, aggregates `agg.*`, faction stats `fac.*`, settlement stats `set.*`; proper nouns).
- **Content that matters:**
  - Mapping by key prefix `attr|agg|fac|set` -> `descriptor_registry.yaml` `name`; `category == proper_noun` -> `proper_noun_registry.yaml` `canonical` (`:92-104`).
  - The reverse sweep exists because `fac.legitimacy` (ruled a base faction stat 2026-08-23) was in the descriptor registry but not the names index for three weeks, so `Legitimacy` resolved silently to `set.legitimacy` (`:107-115`).
  - Imports `names` (tools/names.py) - the same reader as `ci_naming_check`.
  - Reads `descriptor_registry.yaml` groups `body/mind/social/retired` attributes (`:59`): "retired: Bonds (CR-84)".
- **Conflicts / stale:** message tells the user to run `tools/valoria_rename.py` which is retired (`:134`).
- **Open items:** none.

### tools/ci_naming_check.py
- **What it is:** the naming-invariant gate: no ADDED line may introduce a `legacy` name of an `enforce: block` entry in `references/names_index.yaml` (canonical Solmund; its one deprecated name is never to appear); `--warn` runs the warn tier.
- **Status:** no Status line; live. Block tier BLOCKING (`validators`); warn tier report-only by caller policy. Imported by `hook_naming_guard.py`.
- **Bears on:** PROCESS, WR (the one proper noun enforced).
- **Content that matters:**
  - Diff-aware via `ci_common.get_added_lines(mode)`; deprecated names are NOT hard-coded: `names.all_legacy(enforce=tier)` (`:67-85`).
  - Fail-safe: empty block tier returns 1 (index unreadable), empty warn tier returns 0 (`:250-256,:283-296`).
  - A long `EXCLUDE` substring list (`:89-151`) with a rooted subset `EXCLUDE_ROOTED = ('.audit/',)`; several entries name retired trees (`tools/observability/lexicon`, `dashboard/data.json`, `deprecated/`); the stale ones are inert.
  - Own test: `test_the_audit_exclusion_is_ROOTED_not_a_substring` (note in `:121-128`); `'tests/'` exclusion is a substring, so any path containing `tests/` is exempt.
  - A rename in prose elsewhere is not caught unless the line is newly added; `.designs/` is NOT excluded, so a quarantined-doc edit adding the token fails.
- **Conflicts / stale:** `names_index.yaml` header warns "NOTHING VALIDATES the `enforce` field" (`names_index.yaml:24`): an unknown tier value silently disables an entry.
- **Open items:** none.

### tools/ci_pp_frozen_check.py
- **What it is:** blocking gate making PP (patch) ids frozen history: no cited `PP-NNN` above 726, and archive pointers in `registers/patch_register_active.yaml` must name fork ref `c451bcb` (Jordan ruling 2026-08-14, ED-IN-0190).
- **Status:** no Status line; live, blocking (`validators`).
- **Bears on:** PROCESS.
- **Content that matters:**
  - `PP_FROZEN_CEILING = 726`; scans `canon/ systems/ modules/ references/ registers/ workplans/ godot/ engine/ proposals/ tools/` for `.md .yaml .jsonl .py .json` (`:50-59`). Any new PP id above the ceiling in any scanned file reds CI, including in `proposals/`.
  - Excludes only its own file, so a digest/proposal that quotes an example PP number above 726 reds the gate.
  - Own-boundary regex `(?<![A-Za-z0-9])PP-(\d+)\b` instead of `ci_common.PP_ID_PAT` (bare) because of `OPP-03` collisions (`:25-31,:53`).
  - It does not scan `.designs/`/`.audit/`/`skills/`/`tests/`/`CLAUDE.md`.
- **Conflicts / stale:** `FORK_REF = 'c451bcb'` is hard-coded; elsewhere forks are `1e4c6f4`, `6f740d9`, `c9daad6`: PP evacuation ref is one of many.
- **Open items:** none.

### tools/ci_quantity_vocabulary_check.py
- **What it is:** A17 stat-vocabulary closure: stat identifiers in `module_contracts.yaml` state/derivations and literal `stat_deltas={}`/`impact_vector={}` dict keys in sim code must resolve to the descriptor registry or names index (via `quantity_registry`).
- **Status:** no Status line; report-only (`validators-report`), exits 1 on any unresolved.
- **Bears on:** CORE, CHAR, all (vocabulary closure of module I/O).
- **Content that matters:**
  - Two scans: `scan_module_contracts` and `scan_sim_literals` (regex `(stat_deltas|impact_vector)\s*=\s*\{([^{}]*)\}`, `:71,:99-125`); roots from `ci_common.sim_reference_roots()` (engine, systems/*/sim, modules/* except combat).
  - Bundled names "A / B / C" are split on `/` (`:75-78`); computed quantities with no registry identity "report as unresolved ... expected backlog" (`:38-41`).
  - Docstring authority is the Key & Echo armature quantity extension (retired substrate); echo_transport named as the one live call site (retired).
  - Prints `N unresolved / M scanned`; the backlog size is not recorded in the file.
- **Conflicts / stale:** cites `designs/audit/2026-07-08-...` (dissolved tree); the Key substrate was retired (ED-IN-0232) so the `stat_deltas` call sites may no longer exist `[UNVERIFIED]`.
- **Open items:** "flip to blocking at zero backlog" (own lifecycle, `:21-23`) has not happened.

### tools/ci_register_size_check.py
- **What it is:** blocking size-cap gate (tokens = chars//4) over ~35 governed files: canonical_sources, patch register, coverage_matrix, propagation_map, names_index, id_reservations, module_contracts, 9 lane editorial ledgers and their archives, audit_registry.
- **Status:** no Status line; live, blocking (`validators`), WARN at 85% report-only.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Caps: `canonical_sources.yaml` 14,000; `module_contracts.yaml` single-sourced from `atomization_rules.yaml` (fallback 18,000; comment says policy raised to 24,000 by W4 OI-54); lane ledgers 120,000 (raised from 50,000, Jordan 2026-08-21 "merely fiat"), `_archive` 250,000 (`:56-183`).
  - Uses repo-RELATIVE paths with `os.path.exists(path)` (`:207-210`) so it only works from the repo root, unlike siblings using `ci_common.REPO`.
  - Reads `atomization_rules.yaml` with a hand-rolled line parser (`:13-34`); `compliance_check.py` is a second size gate over the same policy file (see its entry).
  - Prints archive criteria (ED-IN-0245: pre-current-month OR terminal status leaves the live ledger).
- **Conflicts / stale:** `tests/coverage_matrix.md` is capped here and also demanded by `ci_co_file_checker` Rule 3; `references/audit_registry.jsonl` cap persists (the file exists); `registers/patch_register_active.yaml` is the PP register that `ci_pp_frozen_check` freezes.
- **Open items:** none.

### tools/ci_sim_fabrication_check.py
- **What it is:** blocking anti-fabrication gate: every numeric literal on a line ADDED to a "sim" `.py` must be exempt, ledger-cited, or carry `# [canonical|GROUNDED|JUSTIFIED|DECLARED-DIVERGENCE|CALIBRATED-DEBT|FORK: ...]` on the same/previous line.
- **Status:** no Status line; live, blocking (`validators`); also in `valoria_local --staged`.
- **Bears on:** CORE, all subsystem sims (it is the provenance rule for every game constant in `engine/`, `systems/*/sim/`, `modules/*` other than combat).
- **Content that matters:**
  - Scope `is_sim_file` = (`ci_common.sim_reference_prefixes()` OR basename containing "sim"/"simulation") minus `tools/`, `deprecated/`, `engine/tests/`, `engine/season/tests/`, `tests/valoria/`, `tests/contracts/` (`:138-219`). `modules/combat/` is OUTSIDE scope (KNOWN GAP, `:164-170`, filed ED-IN-0119; `MODULES_WITH_OWN_EXPORT` keeps combat out): the personal-combat oracle's constants are not provenance-gated by this tool.
  - Exempt literals: 0, 1, 2, 10, 100 (+ `.0` forms) and 0.5 (`:130-131`); `range/len/enumerate/slice` idioms skipped.
  - Only ADDED lines are gated (`added_only`, `:484-509`); pre-existing debt is counted and printed ("carried"). Measured at writing: 642 uncited constants across 47 live-oracle files (`:487-499`), i.e. most existing constants have no citation.
  - Citations are accepted by marker presence only, never checked against content ("labelling a value honestly must never be harder than mislabelling", `:65-76`); FORK tag needs a sha with a digit or `refs/...` (`:111-113`). A ledger match is by `(sim_variable, value)` from `sim_verification_ledger.json` (co-located or at repo root) (`:342-373,:376-466`); `ls` of such ledgers not checked here.
  - Removing a provenance tag forces a whole-file scan (`displaced_citation_paths`, `:469-481`).
- **Conflicts / stale:** "the gate is intentionally noisy" printed on failure while the tool is changeset-scoped; mention of `tests/sim/` (frozen tree) as in scope, CLAUDE.md §3 says `tests/sim/` is unrelated to the retired `sim/`.
- **Open items:** `modules/combat/` out of scope; markers are honour-system.

### tools/ci_vacuous_assertion_check.py
- **What it is:** report-only AST scan of `tests/valoria` and `engine/tests` for assertions that cannot fail (V1 truthy literal, V2 `len>=0`, V3 `name is not None` for in-module def/class/import, V4 `isinstance(x, object)`, V5 literal==literal, V6 `0*x==0`) plus heuristic S1/S2.
- **Status:** no Status line; live, report-only (always returns 0, `:290`). Registry's only `subject: verification` row.
- **Bears on:** PROCESS (guards the tests that guard the game).
- **Content that matters:**
  - Static, single-file, cannot resolve imports or types (own limits `:40-45`); does not see `pytest.approx` on exactness claims or loops that may assert zero times, though CLAUDE.md §0.1 pt 2 names both (the registry row claims it detects them: `ci_checks_registry.yaml:373`); code implements only the six rules. Registry role text over-claims relative to code.
  - Default roots `('tests/valoria','engine/tests')` (`:68`); `engine/season/tests` and `modules/**` tests are not scanned.
  - Origin: two vacuous assertions written in one session (ED-IN-0098); kept by Jordan's ruling 2026-08-21 as a literal encoding of §0.1 pt 2.
- **Conflicts / stale:** registry role vs code (above).
- **Open items:** "promoting PROVABLE to blocking is Jordan's call" (`:289`).

### tools/ci_vetting_check.py
- **What it is:** blocking gate: patch-register (`registers/patch_register_active.yaml`) entries PP-674 and above must carry a `vetting:` block (class A-E; A/B need class, necessity, omega, mu, m_ratings, q) or `class: C|D|E` / `pre-framework: true`.
- **Status:** no Status line; live, blocking (`validators`).
- **Bears on:** PROCESS (patch register; PP now frozen, so no new entries possible).
- **Content that matters:**
  - Regex parsing of YAML (PyYAML-free) with an indentation-aware block extractor (`:52-83`); entries `-\s+id:\s+PP-(\d+)` (`:110-113`).
  - Uses repo-relative `REGISTER_PATH` (needs CWD = repo root, `:49,:176`).
  - Cites `references/throughlines_meta.md §8` as the framework definition (prose authority for the vetting scheme: omega, mu, m_ratings, q).
  - Since `ci_pp_frozen_check` forbids PP ids above the frozen ceiling, this gate can only ever re-check a closed set: its subject is frozen.
- **Conflicts / stale:** none beyond the frozen subject.
- **Open items:** none; candidate for retirement along with the PP register (process-only).

### tools/compliance_check.py
- **What it is:** CI job `compliance-check` (`--check-only --repo-state .`): walk the whole tree for `.md`/`.yaml`, match each to a policy in `references/atomization_rules.yaml` by `fnmatch`, and fail on a token-cap breach whose `on_exceed` is blocking.
- **Status:** no Status line; live, blocking. NOT in `valoria_local` (CI-only), so local-green is not compliance-green (CLAUDE.md §8).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Closed `on_exceed` vocabulary: blocking `error`, `block_commit`; advisory `warn_only`, `flag_*`, `chunk_by_quarter`; `skip` = no violation; an unknown token raises `UnknownOnExceedToken` (`:93-128`). Falsifier: `tests/valoria/test_compliance_on_exceed_vocabulary.py`.
  - The walk is `os.walk(repo_state)` with NO directory exclusions (`:182`): it reads `.designs/`, `.audit/`, `.claude/worktrees/**` and `proposals/**` as well, and the policy file decides which patterns bind. Reads files with default encoding and no `errors=` (`:191`), so a non-UTF-8 `.md` crashes it.
  - Half the module is dead scaffolding: `Violation.fix_action`, `auto_fixable` and 'atomizer.atomize'/'doc_index_gen' references name retired tools (`:38-44`); the interactive mode exits 2 (`:229-237`).
  - Second size gate beside `ci_register_size_check.py` (two token-cap enforcers over the same policy file; one is per-path, one is pattern-matched).
- **Conflicts / stale:** CLAUDE.md §4 says "nothing enforces a length cap" and "several ARE blocking" per-file caps: consistent only for the explicit patterns.
- **Open items:** whether the unexcluded walk over `.claude/worktrees/` can false-red CI (agent worktrees are untracked, so CI checkout would not contain them).

### tools/currency_consistency_check.py
- **What it is:** report-only "recency gate" (ED-1087): CURRENT.md stamp vs head commit dates, reconcile-chain structure, CURRENT.md paths exist, ED/lane id ceilings vs `id_reservations.yaml`, patch-register header, dead "maintained by" pointers, HANDOFF.md `## Next` heading.
- **Status:** no Status line; live, report-only. Docstring warns it prints `[CURRENCY DRIFT: n]` but its `main` returns 1 (`:532`) while the docstring says it exits 0 (`:43-46`): code and docstring disagree (CI `w` wrapper swallows either).
- **Bears on:** PROCESS (it reads CURRENT.md and HANDOFF.md, which CLAUDE.md §0.05 cl.4 says a program may legitimately read).
- **Content that matters:**
  - Eight checks listed at `:500-510`. The stamp check compares `git log -1 --format=%cs -- <path>` for each backticked path under canonical-head trees (`designs systems engine params references canon sim`) against `Last reconciled:` + 1 day (`:138,:228-264`); depth-1 clones skip it (stderr notice, `:203-225`).
  - ID checks read `registers/editorial_ledger*.jsonl` by regex `"id": "ED-XX-NNNN"` and compare each lane's max to `id_reservations.yaml` `lane_ids.<LANE>.next_free` (`:167-200,:415-432`); archives included on purpose.
  - Patch-register check reads "Next PP number: N" against body max (`:435-443`): the PP register is frozen (ci_pp_frozen_check), so this check watches a dead counter.
  - `check_dead_maintainers` scans `references designs params canon` for "maintained by <skill>" naming a skill under `deprecated/skills/` (`:450-477`); CLAUDE.md §1 says there is no `deprecated/` tree, so `dep_skills` is empty and the check returns immediately (`:456-457`): dead.
  - `summary_line()` and `--summary` exist for the retired SessionStart banner (`:513-520`).
- **Conflicts / stale:** `CANONICAL_HEAD_TREES` names dissolved `designs`, `params`, `sim`; `_PATH_IN_BACKTICKS` includes dissolved roots. CURRENT.md "reconcile-stamp" chain format is policed structurally here (non-monotonic dates, duplicated bodies >= 400 chars).
- **Open items:** none.

### tools/definitions_store.py
- **What it is:** builder/checker/query CLI for `references/definitions/definitions.yaml`, a generated merge of `names_index.yaml` + `descriptor_registry.yaml` (ED-IN-0077 Phase 2).
- **Status:** no Status line; ORPHAN. `references/definitions/` holds only `vocab_source.yaml`; `definitions.yaml` does not exist, so `--check` fails with "missing" (`:133-134`). Not in CI, `valoria_local`, or the registry; referenced by `tests/valoria/test_definitions_store.py` and `test_engine_params_bridge.py` only.
- **Bears on:** PROCESS, CHAR/FA/SE (descriptor keys).
- **Content that matters:**
  - `build()` unions names_index and descriptor entries: canonical, aliases, legacy, category, enforce, scale, compute, group, `in_registers`, and a `gap` flag for descriptor-only keys (`:83-109`).
  - Descriptor sections read: attributes body/mind/social, aggregates (compute verb), practitioner_stats, territory_stats, faction_stats, settlement_stats (`:60-80`) - a useful list of the descriptor registry's categories.
  - Comment says generated store is "an eventual inversion (registers generated FROM the store)" (`:12-15`), never done.
  - `ci_register_size_check.py:93` still caps the nonexistent store at 8,000 tokens.
- **Conflicts / stale:** second implementation of the name-parity check of `ci_names_consistency.py`. `engine/engine_params/names.json` and `descriptors.json` (exported) are the runtime copies, so this store carries no reader.
- **Open items:** delete or regenerate; nothing reads it.

### tools/descriptor_registry.py
- **What it is:** loader/resolver library for `references/descriptor_registry.yaml` (W1.13; OPT-AV-7 live replacement of a retired module).
- **Status:** no Status line; live as a library for tests and skills only (`skills/valoria-vector-audit/scripts/*`, `tools/quantity_registry.py`, tests). The engine reads descriptors via `engine/substrate/descriptors.py` + `descriptors.json`, not this.
- **Bears on:** CHAR (attribute roster), PROCESS.
- **Content that matters:**
  - `load()` reads `references/descriptor_registry.yaml` relative to CWD only (`_PATHS`, `:16-29`).
  - `all_attributes` flattens `attributes.body|mind|social` with `domain: actor`, `kind: attribute_scalar` (`:32-38`); `resolve()` by key/name/alias, retired attributes (e.g. Bonds) resolve with `deprecated` (`:41-59`).
  - `aggregate_members` for placeholder `agg.body|mind|social`; `is_deprecated` against `deprecated:` list (`:62-83`).
  - Third reader of the descriptor registry (with `export_descriptors.py`, `definitions_store._load_descriptors`, `ci_names_consistency.descriptor_names`): four loaders, four shapes of the same YAML.
- **Conflicts / stale:** none.
- **Open items:** consolidating the readers is outside any gate's remit.

### tools/export_battle_orders.py
- **What it is:** exporter: `modules/mass_battle/massbattle.py` `ORDER_ROLES` / `ORDER_RETREAT_AT` (checked equal to `config.ROLE_SPEC` names) -> `engine/engine_params/battle_orders.json` (CP-T04-02 "marshal"); `--check` round-trip.
- **Status:** no Status line; live. Wired in `valoria_local.py:86` (blocking) and `engine/season/tests/test_cp_t04_02_marshal.py` only; NOT in `valoria-ci.yml` (the registry says the CI line is "Jordan's file" under CODEOWNERS and was left out). So CI does not run it directly (the season job's pytest does).
- **Bears on:** MB, CORE (season reads order roles from the artifact via `engine/substrate/battle_orders.py`; `engine/season/rosters.yaml` `order_roles`/`order_retreat_at` use `from_battle_orders`).
- **Content that matters:**
  - Load-bearing on the game: it observes that the MB module's closed sets of standing-order roles and retreat triggers equal what the season's choosers read. A role added to `ROLE_SPEC` reaches the season only by re-running this (`:1-15`).
  - Refuses empty or repeating sets and a role set different from `ROLE_SPEC` (`:36-40`).
  - Output has only `roles` and `retreat_at` lists, `source`, `schema_version` (`:41-48`): none of the role parameters (`ROLE_SPEC` values) cross, only names.
  - Imports `modules.mass_battle.massbattle` directly (a `sys.path` insert of the repo root): a tools-side import by name, which is fine for a build tool.
- **Conflicts / stale:** registry row marks `subject: game` while the registry header says nothing is `game` (`ci_checks_registry.yaml:24-26,:314`).
- **Open items:** the CI workflow line `v python3 tools/export_battle_orders.py --check` is owed (registry notes, `:318`).

### tools/export_composition.py
- **What it is:** exporter + validator: `references/module_contracts.yaml` `composition_roles:` -> `engine/engine_params/composition.json` (schema_version 3), which `engine/substrate/composition.py` reads; also `validate_wiring` over the `modules:` list. BLOCKING (`validators`).
- **Status:** no Status line; live. The only blocking gate whose subject is `module_contracts.yaml`.
- **Bears on:** CORE (the season/engine -> subsystem seam), all subsystems that expose a callable. LOAD-BEARING ON THE GAME: it IMPORTS every declared target at export time (`_resolve`, `:110-126`), so a moved/typo'd module fails CI instead of a campaign run.
- **Content that matters:**
  - Cooked artifact (read from the JSON, 16 roles): `combat.fight` (entry `verb_call`, verb `fight`), `mass_battle.resolve_field` (`verb_call`, `march`), `social_contest.roll` (`verb_call`, `tell`); `fieldwork.find` and `settlements.produce|subsist` (`step_call`); `mass_battle.army|army_options|army_order|army_preset` and `settlements.drawn_under|fabric|fortification|housing|larder_draw|provision` (`query`). NO role exists for factions, governance, diplomacy, threadwork, victory or characters: those subsystems are not reachable through the composition seam.
  - Closed vocabularies `_KINDS = (callable, value)` and `_ENTRIES = (verb_call, step_call, query)` (`:70-83`); `entry:`/`verb:` consistency enforced (`_check_entry`, `:86-107`): a `verb_call` row names its verb, no other kind does.
  - `validate_wiring`: every module row named, uniquely named, with `wiring:` block whose `build`/`godot` are in `wiring_vocabularies` (`:129-200`). It validates that facts exist, not that `build` status is true.
  - Reads the YAML with `ci_common.load_yaml`; writes with bare `open()`, no encoding argument (`:255,:262`).
  - The `mass_battle.army_*` and `settlements.*` query roles show the MB/SE modules as typed-input queries, not as verbs.
- **Conflicts / stale:** docstring cites `keys.py` vs `key_types.json` (Key substrate, retired, ED-IN-0232) as the precedent; `needed_by` is cooked per role but its readers are not named here.
- **Open items:** which of the 27 `module_contracts.yaml` modules have no composition role (roles = 16; module rows count is printed only at run time).

### tools/export_descriptors.py
- **What it is:** exporter: `references/descriptor_registry.yaml` -> `engine/engine_params/descriptors.json` read by `engine/substrate/descriptors.py` (sole runtime reader). BLOCKING (`validators`), `--check` round-trip.
- **Status:** no Status line; live; LOAD-BEARING ON THE GAME (attribute roster and scale, pursuit/axis/affiliation/heritage rosters).
- **Bears on:** CHAR (attributes), CORE, SE (settlement_stats), WR/FA (affiliations).
- **Content that matters:**
  - Attributes: scale floor/ceiling parsed once from `"lo-hi"` (`SCALE_RE`, `:67`); roster = body, mind, social keys. Cooked JSON now has 10: strength, endurance, agility, focus, acuity, will, perception, attunement, charisma, grace; a `pending_tenth` sentinel emitted only if the roster has fewer than 10 (`:256-260`; absent in the JSON).
  - Rosters enumerated and validated by `_named_roster` (names exist, declared `count` equals length, no duplicates): `pursuit_roster` (15), `axis_roster` (7 bipolar ethical axes), `affiliation_roster` (5, intensity scale as closed integer `lo-hi`, `player_sees`, `concerns` mapping, no member under two concerns), `heritage_roster` (5, with `engages` cells naming an affiliation concern) (`:96-218`).
  - `settlement_stats` (`set.legitimacy, popular_support, prosperity, defense, order, facility_tier`), `practitioner_stats` (`prac.thread_sensitivity`, `prac.tps`), `territory_stats` (`terr.fort_level`); the faction block (`fac.*`) is GONE since plan position 29b (`:40-41`): factions have no descriptor stats in the runtime artifact.
  - `unimplemented: {}` (empty); the tool itself warns an empty block is "not evidence the register is complete" (`:30-33`).
  - Attribute alias map `names` (every live name/alias/key lowercased -> key) refusing a spelling shared by two keys (`:188-197`).
- **Conflicts / stale:** `fac.intel` (ruled bounds) is cited by CLAUDE.md §0.05 as an orphaned fact: it is no longer exported anywhere here; `ci_names_consistency` still expects `fac.*` mirror rows (`faction_stats`) in the descriptor registry although this exporter ignores them.
- **Open items:** the faction stats' route to runtime (none via this artifact).

### tools/export_engine_params.py
- **What it is:** exporter: the personal-combat oracle (`modules/combat/config.py` `CFG` + `core.py` UPPERCASE constants + `attributes.SPEC` + weapons/armour-tier/Combatant-default kit) -> `engine/engine_params/combat_engine_v1.json` (schema_version 7); `--check` round-trip. BLOCKING (`validators`).
- **Status:** no Status line; live; LOAD-BEARING ON THE GAME: observes that the typed JSON the port ingests equals what the Python oracle computes now.
- **Bears on:** PC, DICE, GO (the Godot port's combat seed).
- **Content that matters:**
  - Read from the committed JSON: sections `cfg` (214 keys), `core` (26 auto-collected UPPERCASE JSON-typeable constants), `attributes` (8 entries: the combat-read attributes; `cog` removed at v7, `strength.neutral` null -> 4), `kit` (54 weapons, armour tiers, Combatant default weapon/armor).
  - Auto-collection (`_module_constants`, `:81-95`) means a new constant in `core.py` is exported with no edit here, but also that any new UPPERCASE constant, however incidental, enters the port contract.
  - The oracle's `attributes` use `registry_key` to point at descriptor keys; "Godot fields stay unbound (CLAUDE.md §5)" (`:98-107`).
  - Observes only equality export-vs-oracle; it does not check the oracle against the design; "Class-C = calibrated against the harness, not canon prose" (`:139`).
  - `sys.path.insert(0, ENGINE_DIR)` then bare `import config, core, combatant, vocabulary, weapons, attributes`: this is the `modules/combat` by-path load (CLAUDE.md §3 names it as the one `sys.path` seam).
- **Conflicts / stale:** docstring refers to `systems/combat/combat_engine_v1/` "until plan position 31b" and to a retired `tools/ci_formula_prose_check.py` (A18 detector).
- **Open items:** attributes: combat reads 8 of the 10 roster attributes.

### tools/export_game_constants.py
- **What it is:** exporter: composes `sim_params.json` + `combat_engine_v1.json` into `engine/engine_params/game_constants.json`, keyed by the Godot port's own constant names; the writer half of the ttrpg -> `valoria-game` constants bridge. BLOCKING `--check` (`validators`).
- **Status:** no Status line; live. Reader half is `valoria-game/tools/check_constants_parity.py` (other repo, not visible here `[UNVERIFIED]`).
- **Bears on:** GO, DICE, PC, WR (coherence), FI (knot formation), CORE.
- **Content that matters:**
  - Only FIVE oracle constants cross, hand-paired (`MAPPING`, `:54-89`; JSON: `TN_STANDARD` 7, `COMBAT_POOL_MINIMUM` 5 (= `combat.core.POOL_FLOOR`), `KNOT_FORMATION_TN` 7, `KNOT_FORMATION_OB` 2, `SEASONS_PER_YEAR` 4). The docstring says the port's `systems/util/Constants.gd` holds ~200 hand-transcribed constants and that, as of 2026-08-20, `valoria-game` read zero bytes of `engine_params` (`:5-16`). So the port is almost entirely hand-transcribed; the bridge covers about 5 of them.
  - `COLLISIONS` (`:93-115`): port `POOL_FLOOR` = 1 (universal dice-pool floor, `RollContext.gd:26`) vs oracle `combat.core.POOL_FLOOR` = 5 (combat pool minimum): different quantities; port `MOMENTUM_MAX` 4 vs kernel `M_MAX` 1.5 (tanh ceiling); "Momentum 0-4 has no scalar owner in engine/ today".
  - `DIVERGENCES` (real, need rulings, `:120-169`): (1) `accord_range`: oracle holds NO accord state (Accord clock has no season analogue, ED-WR-0011 option A); port keeps an integer accord clamped [0,3]; (2) `weapon_tn_modifiers`: oracle TN is always 7 (ED-IN-0196, Jordan 2026-08-25) while port TN varies 5-8 per weapon; (3) `coherence_bands`: oracle models Coherence as distance from the human equilibrium with resting point + elastic displacement (4 displacement bands + terminal "Coherence failure" when the resting point leaves `HUMAN_BAND_LIMIT`, no Severed band, `systems/threadwork/sim/coherence.py`) vs port's retired 10-0 depleting track with DISSONANT=6, FRAGMENTED=4, FRACTURED=2, SEVERED=0.
  - Rows that LEFT the table because their Python owner was deleted: `OB_FLOOR`, `CI_START`, `VICTORY_SUSTAIN_SEASONS`, `COHERENCE_*`, `WEAPON_TN_BASE`, `OB_CAP` (`:63-88,:112-114`): the season loop "reports `endings` since v9 IN-27 (H-176 in engine/season/hole_register.yaml) and carries no sustain count".
  - Ambiguity handling: a sim_params key defined at two sites with different values is withheld, e.g. `mass_battle.SEED_BASE` (bat.py 1,000,000 vs lanchester_signature.py 2,000,000) (`:172-202`).
- **Conflicts / stale:** docstring says "five parameter files" and cites `export_key_types.py` (retired); `engine_params/` now holds eight JSON files.
- **Open items:** the three divergences are explicit rulings owed (port alignment); no oracle value for accord, victory sustain, Faction OB floor or CI start.

### tools/export_names.py
- **What it is:** exporter: `references/names_index.yaml` -> `engine/engine_params/names.json`, read by `engine/substrate/names.py` (single runtime reader of canonical names, aliases, `token_class` rosters). BLOCKING (`validators`), `--check` round-trip; refuses non-idempotent shapes.
- **Status:** no Status line; live; LOAD-BEARING ON THE GAME (`engine/season/data/cast.py` resolves NPC faction strings through it and `engine/season/rosters.yaml` derives its `factions` roster from it via `from_names:`).
- **Bears on:** CORE, FA, CHAR, WR (names), PROCESS.
- **Content that matters:**
  - Refused with `SystemExit`: an alias mapping to two canonicals; an alias that is another row's canonical; a legacy tag that is also a live alias; a legacy tag that is another row's canonical (`:110-144`). Recorded not refused: two entries sharing one display string -> `ambiguous` block (`:92-104`).
  - Cooked artifact (read): 122 canonical names, 62 aliases, 19 legacy tags, `by_class` rosters clock 6, clock_full 4, faction 10, mech 5, npc 10; `ambiguous` = `Order` (`conv.order` vs `set.order`) and `Reason` (`attr.mind.acuity` vs `conv.reason`).
  - Legacy map includes the retired vocabulary: `Cohesion`->`Discipline`, `Combat Power`->`Power`, `Command Rating`->`Command`, `Contact Rounds`->`Thread Fatigue`, `Peninsular/Political/Public Instability`->`Turmoil`, `Theocracy Counter`->`Church Influence`, `Rendering Stability`->`Mending Stability`, `EventImpact`->`Key`, `convictions`/`conviction_axes`->`pursuits`/`pursuit_axes` (and one deprecated proper noun -> Solmund).
  - Its output `engine/engine_params/names.json` is in `ci_naming_check.EXCLUDE` because it carries the deprecated name as data.
  - The check message prints "4 idempotence checks passed" while the module lists five rules ((1),(2),(4),(5) refused and (3) recorded); count wording drifted (`:32-34,:177`).
- **Conflicts / stale:** docstring/message say "four"/"five"; the CLAUDE.md names Solmund only.
- **Open items:** `Reason` and `Order` display collisions are recorded, resolved by raising in the leaf.

### tools/export_npc_roster.py
- **What it is:** generator + checker for `engine/season/npcs.yaml` (46 NPC rows: case, name, institution, home, want, concerns, tie) derived from `engine/season/cases/NPC*.yaml` by running `populated.build_realm(0, from_roster=False)` (~10 s).
- **Status:** no Status line; live. `--check` is BLOCKING in CI (`validators`, wired 2026-09-16) but fails ONLY on a row naming a nonexistent case, place or unseated person; differences from the derivation are REPORTED, not failed (`:196-211`). `--build` OVERWRITES hand edits.
- **Bears on:** CHAR (NPC cast), CORE, WR (placement), SE (homes are venue rungs).
- **Content that matters:**
  - `npcs.yaml` read at runtime by `engine/season/harness/populated.py` (registry note); after `--build`, the regex matchers inside `populated.py` are a bootstrap, not a runtime dependency (`:26-29`): "a row a human corrected must not be silently re-derived".
  - `tie` records which rule chose `concerns`: `named | institution | roof | neighbour` (`:84,:143`); `want` = first `core` row of the case's `season_requires` (`:73-75`).
  - Imports the season harness (`engine.season.harness.populated`) from tools: this validator is a heavy game-code consumer (realm build per check). The earlier first cut was vacuous because `build_realm(0)` defaulted to reading the roster itself (`:93-98`), fixed by `from_roster=False`.
  - Declares the world generator invents no NPC count (ED-WR-0011 OI-05): every NPC traces to a case id (`:71-76`).
  - Registry row marks `subject: game` and quotes the roster as `references/npc_registry.yaml` (identity, convictions, role) vs `npcs.yaml` (placement, wants): two NPC data heads with disjoint fields.
- **Conflicts / stale:** the docstring mentions `01_AXIOMS.md ID-13` (an archived prose axiom) as the rule against unread columns.
- **Open items:** the only enforced property is referential integrity; a hand-edited home/tie that is semantically wrong passes.

### tools/export_sim_params.py
- **What it is:** AST extractor: every module-scope numeric/collection literal constant in the sim reference roots (`ci_common.sim_reference_roots()`: `engine/`, `systems/*/sim`, `modules/*` except combat) -> `engine/engine_params/sim_params.json` (schema_version 2) with file, trailing comment `note`, typed `citation` and `citation_grade`. `--build`, `--check`, `--search`.
- **Status:** no Status line; live. NOT in CI workflow, `valoria_local` or the registry; the drift gate is `tests/valoria/test_export_sim_params.py` (inside pytest). Its output feeds `export_game_constants.py` (a blocking exporter) and `link_values_pointers.py`.
- **Bears on:** CORE, MB, SC, FI, WR, all (the "migration backlog" count in CLAUDE.md §0.05 comes from `--build`).
- **Content that matters:**
  - Read from the committed JSON: 283 constants, 125 cited, 158 uncited, 8 assumption-grade; by module: `mass_battle` 164, `threadwork` 36, `social_contest` 31, `engine.season` 21, `fieldwork` 15, `engine.dice_engine` 6, `characters` 5, `overview` 5. NO rows for `settlements`, `factions`, `world`, or `combat` (combat has its own export, `MODULES_WITH_OWN_EXPORT`): FA and SE sim constants do not reach the typed layer at all.
  - Anti-fabrication by construction: `ast.literal_eval` only (non-literals skipped) so computed constants, class attributes, and constants defined by expression never export (`:54-60,:225-233`).
  - Citation detection is a regex over the trailing comment: `[canonical: ...]`, `PP-N`, `ED-...`, `J-N`, or a bracketed `§` section; "ASSUMPTION/FLAG/SEED/TODO" markers are excluded (`:153-211`). Counts "cited" by string shape, never verified (the same limit as the fabrication gate).
  - Skips tests, `engine/reference/` (frozen parity oracles) and duplicates (`:124-150`).
  - Key `<module>.<NAME>` is not unique (`mass_battle.SEED_BASE` has two values); `export_game_constants` withholds such keys.
- **Conflicts / stale:** `_subsystem` still handles a dissolved `sim/` root (`:119-120`); docstring lists "systems/*/sim, engine, sim/*".
- **Open items:** it exports constants as found, so which of 283 are in the live game path (versus oracle/bench scripts such as `bat.py`'s `SEED_BASE`) is not marked.

### tools/fold_ledger_to_latest.py
- **What it is:** CLI instrument (`--queue [--list]`, `--id`, `--stats`) that folds `registers/editorial_ledger*.jsonl` to the last row per id and counts `needs_jordan: true`.
- **Status:** no Status line; live; manual-only, not in CI (registry: "DELIBERATELY NOT WIRED").
- **Bears on:** PROCESS (the `needs_jordan` queue; CLAUDE.md §0 "needs_jordan is not a parking space").
- **Content that matters:**
  - Thin CLI over `ci_common.read_editorial_ledger_rows/fold_ledger_to_latest/editorial_ledger_paths` (`:43-45`): the logic lives in `ci_common`; this file only prints.
  - Reports `needs_jordan: true` at ANY status plus the `status: open` subset, since several ruled/partial/resolved rows are still Jordan's (names ED-IN-0210, ED-IN-0261, ED-IN-0247 in docstring, `:49-63`).
  - Does not scan the older `registers/archive/*.yaml` corpus (docstring `:14-18`): a flagged row sitting only there is invisible to `--queue`.
  - Fourth-or-fifth reader of the editorial ledger: `triage_work_items.work_items` calls the same `ci_common` fold; `validate_ed_citations`, `broken_dependency_checker`, `currency_consistency_check` keep their own.
- **Conflicts / stale:** none.
- **Open items:** the archive-YAML blind spot above.

### tools/freshness_gate.py
- **What it is:** blocking gate: git-blob SHA of each canonical doc path in `references/canonical_sources.yaml` must equal its recorded `canonical_sha__...` pin; `--update` rewrites the pins from the working tree.
- **Status:** no Status line; live, blocking (`validators`); also `valoria_local` report-only.
- **Bears on:** PROCESS (pins on design docs).
- **Content that matters:**
  - `grep -c canonical_sha__ references/canonical_sources.yaml` = 7: the gate currently verifies about seven pins (the ED-IN-0077 review had counted 133 and the regex covers only paths under the listed prefixes `designs|params|compilation|canon|references|skills|tests|systems|engine|registers|arcs`, `:107-110`).
  - Blob OID computed over LF-normalized bytes so CRLF checkouts agree with CI (`:49-73`).
  - Exit 2 ("NO-SHA") when a path line has no pin right after it; any stale/missing path exits 1 (`:218-231`).
  - Anything it pins is a design doc, so it detects document CHANGE, not that a doc matches code (§0.05: prose-hash currency, not a mechanism). `--update` is one command that silences it.
  - Opens canonical docs by working-tree path, so quarantined paths (`systems/**/*.md`) that no longer exist would report MISSING (counted stale).
- **Conflicts / stale:** `valoria_local.py:108` comment says "blocking in CI's integrity job" (job collapsed into `validators`).
- **Open items:** none.

### tools/gen_sigma_parity_goldens.py
- **What it is:** generator of `engine/tests/goldens/sigma_leverage_parity.json`: frozen expected values from two historical reference oracles (`tests/sim/v32-combat-balance/m1_dice_sigma_core.py` numpy original; `engine/reference/contest-groundup/engine.py`), against which `engine/dice_engine/sigma_leverage.py` is tested by `engine/tests/test_sigma_leverage_parity.py`. `--check` mode.
- **Status:** no Status line; live; NOT wired in CI/`valoria_local`/registry (only run by hand; the golden file is consumed by the engine test).
- **Bears on:** DICE (sigma-leverage kernel, degree-of-success bands), PC, SC.
- **Content that matters:**
  - Row families: `sigma_n`, `soft_cap`, `sigma_space_ob_shift`, `net_boost`, `eff_ob`, `p_success`, `levels_to_net_sigma` from the numpy original; `level(minor|moderate|strong|major)` and `degree(net, ob, pool)` from the ground-up contest engine (`:114-149`). Grids: net sigma -50..50, pools 1/5/10/26, TN 6/7/8, base Ob 1-5, degree nets -3..20 (`:53-61`).
  - Edge cases added because changing `OVERWHELM_SIGMA` 0.85 -> 0.86 left all 1,851 assertions green: `(pool, net)` = (22,12), (82,39), (98,46), (105,49), (112,52) sit on the pool-aware Overwhelming bar `mean + OVERWHELM_SIGMA*sd*sqrt(pool)` (`:62-68`).
  - Parity is with a historical oracle (v32 combat numpy and the ground-up contest engine) not with canon; the `engine/reference/contest-groundup` copy was made 2026-09-16 (ED-IN-0231) so a blocking job doesn't reach into `.audit`.
  - The `--check` regenerates by importing both oracles, so it needs `numpy` for the m1 oracle.
- **Conflicts / stale:** docstring cites `audit/2026-06-03-contest-groundup/engine.py` (now `.audit/` and the copy under `engine/reference/`); `engine/reference/contest-groundup/engine.py:6` names this tool as its reader.
- **Open items:** `--check` is unwired, so golden staleness is observed only if someone runs it.

### tools/hook_md_sweep_guard.py
- **What it is:** Claude Code PreToolUse hook on `Grep|Glob` (wired in `.claude/settings.json`): blocks (exit 2) a Glob/Grep that would sweep markdown broadly; Jordan 2026-08-24.
- **Status:** no Status line; live; ADVISORY STEERING: a `Bash(grep *)` call bypasses it (CLAUDE.md §8). Escape: `VALORIA_ALLOW_MD_SWEEP=1`.
- **Bears on:** PROCESS (agent behaviour; the audit suite itself runs under it).
- **Content that matters:**
  - Blocks: Glob whose pattern ends `*.md`/`**/*.md`; Grep with `glob`/`type` restricted to markdown; Grep with no `path`, `glob` or `type` (`:57,:95-102`). Allows any call that names a specific `.md` path or mentions a machine-read markdown file.
  - The allowlist of machine-read `.md` is DERIVED by `triage_work_items.machine_read_inputs()` (`:60-68`), failing OPEN on any error; so this hook depends on `triage_work_items.py` importing cleanly.
  - Block message tells the agent to `Read` a named doc instead and mentions "the Key-type registry" as a machine-read input (`:124`), a retired substrate.
  - Hook-pattern consequence for the audit lanes: an unscoped `Grep` (no path) is blocked; give `path`.
- **Conflicts / stale:** message cites `Read("systems/combat/combat_v30.md")` (no such file under `systems/`).
- **Open items:** none.

### tools/hook_naming_guard.py
- **What it is:** PreToolUse hook on `Write|Edit|MultiEdit`: scans ADDED text of the edit with `ci_naming_check.scan_text` and blocks (exit 2) a use of the deprecated name for Solmund.
- **Status:** no Status line; live, BLOCKING at edit time. Not seen by `Bash` edits (`sed`, heredocs).
- **Bears on:** PROCESS, WR (the one enforced proper noun).
- **Content that matters:**
  - Reuses the CI core (no second copy of the rule); collects `content`, `new_string`, and `edits[].new_string` (`:32-42`); path exclusions inherited (`ci_naming_check.EXCLUDE`, so edits under `tests/`, `.audit/`, `CLAUDE.md`, `registers/editorial_ledger*` can contain the token).
  - Fires on this very digest if the token is typed (it blocked one of this lane's edits), so the audit suite's own writing cannot quote the deprecated name outside excluded paths.
  - Stderr message hard-codes the names in text (`:44`) although the rule is read from the index.
- **Conflicts / stale:** none.
- **Open items:** none.

### tools/join_audit_workings.py
- **What it is:** utility that concatenates the nested working-paper `.md` files of one audit unit into `_workings_joined.md` with exact-string BEGIN/END delimiters, verifies a byte-exact round trip, and optionally purges the sources (`--list`, `--unit`, `--purge`, `--check`, `--include-top`).
- **Status:** no Status line; live but a one-off migration utility for the audit corpus (Jordan 2026-08-04); not wired anywhere (`--check` "CI mode" is not in the workflow or the registry).
- **Bears on:** PROCESS (only the `.audit/` archive).
- **Content that matters:**
  - Walks `.audit/` for already-joined units (`:167-172`) but its docstring and `--unit` examples use the old `audit/<session>` path (`:34-35,:177`), so `--unit audit/...` resolves to a path that no longer exists (`unit_root = REPO/unit`).
  - Order is join, verify, then purge; refuses to purge when the round trip fails (`:229-245`).
  - CLAUDE.md §3 says `.audit/` is retired as a category and "do not add to it", so this tool's remaining job is maintenance of joined archives.
- **Conflicts / stale:** path spelling (above).
- **Open items:** none; candidate for deletion (process-only, archive-only).

### tools/link_values_pointers.py
- **What it is:** generator of `engine/engine_params/value_pointer_links.json`: links each `sim_params.json` constant to "pointers" (definitions) by literal token match on constant name/dict keys (ED-IN-0079). `--build`, `--check`, `--pointer`.
- **Status:** no Status line; BROKEN/ORPHAN: reads `references/definitions/definitions.yaml` (`:43,:55`), which does not exist (only `vocab_source.yaml` is there), so `--build` and `--check` raise FileNotFoundError; not wired in CI/local/registry.
- **Bears on:** PROCESS (a derived index; nothing in the game reads `value_pointer_links.json`, to be verified by one grep `[UNVERIFIED]`).
- **Content that matters:**
  - Match method: alphabetic tokens of the constant name (not followed by a digit) and dict keys against a vocabulary built from definitions' canonical/aliases/legacy plus `name_collision_database.yaml` abbreviations (`:52-100`); excludes `pp, ed, sim, tn, ob, ev` and silos 16A/16B.
  - A literal-token join with no semantic check: "every link records the matched token" (`:7-10`) - evidence, not a verdict.
  - A stale committed output `engine/engine_params/value_pointer_links.json` remains in `engine_params/` beside seven live artifacts, so a reader of that directory sees a file no tool can regenerate.
- **Conflicts / stale:** depends on the orphaned `definitions_store.py` output.
- **Open items:** delete the generator and its JSON, or restore the store.

### tools/m1_acceptance.py
- **What it is:** the "M1 acceptance gate" (ED-IN-0112), CLAUDE.md §0.2's instrument: four rows, two of which RUN `engine/season/` headless.
- **Status:** no Status line; live; report-only in CI (`validators-report`, `--summary`); `--check` exits 1 only on a measured failure. The docstring still says "five falsifiable rows" and a table listing `key_log_closure` and `m1_junctures` (`:9,:27-34`); `ROWS` holds FOUR (`:408-413`): `stub_invocations`, `determinism`, `nine_requirements`, `invariant_violations`. The CI comment and registry still say `m1_junctures` fails (`valoria-ci.yml:170`): that row no longer exists in code.
- **Bears on:** CORE (the only execution instrument for the season loop), CHAR/WR (the populated 46-NPC world), all.
- **Content that matters:**
  - Row `stub_invocations`: delta of `engine.substrate.stubwire.invocations` across a 1-season headless run (`headless.run(seasons=1, seed=20260819)`) must be 0 (`:132-226`); the head calls `stubwire` nowhere, so the row can only fire if something resolved by string hits a stub; mutation-verified per its docstring.
  - Row `determinism`: two runs of the same seed compare `World.content_hash()` (folds persons, sites, rungs, tenures, docket and the log; `H-118`) (`:229-275`).
  - Row `nine_requirements`: counts `status: met` in `engine/season/requirements.yaml`; self-declared DOC-DERIVED, not execution (`:293-325`).
  - Row `invariant_violations`: `invariants.sweep` over 24 headless seeds x 4 seasons plus the populated world (2 seeds x 1 season; the populated world is the only one carrying Offices and stance rows); passes only if zero violations and no predicate was unexercised (carrier count 0) (`:327-405`). 8 predicates; the first two writings over-fired (176 violations, 136 invented) (`:348-356`).
  - Verdict logic: any measured failure -> NOT MET; any blocked -> NOT YET MEASURABLE; else MET (`:416-427`). The registry notes no CI signal can fail on regression (report-only, `ci_checks_registry.yaml:413-421`).
  - Imports `engine.season.harness.{headless,invariants,populated}` defensively; a broken import turns rows 1-2 and 5 to `blocked` rather than failing.
- **Conflicts / stale:** docstring/registry row count and `m1_junctures` (above); line-1 text "stub_invocations ... fail today" is stale (the head has no stubs); `--json` has no consumer.
- **Open items:** when a row first passes, a blocking baseline form must be restored (registry text); `nine_requirements` can be greened by editing a YAML string.

### tools/mechanics_index_gen.py
- **What it is:** validator for `registers/mechanics_index.yaml` (90 mechanics): required keys, enum values for `scale` and `test_status`, `gd_applicable` references, path existence for `sim_module`/`canon_sources`, GD-1 victory-path singularity; `--strict` makes warnings errors; `--update` writes a `drift_report` back into the register.
- **Status:** no Status line; live, report-only (`validators-report`).
- **Bears on:** PROCESS; reads a prose-like status register of the mechanics (CORE, all subsystems).
- **Content that matters:**
  - The register is a hand-authored status ledger (`test_status`): of 90 mechanics, 82 `not_implemented`, 4 `contested`, 2 `provisional`, 1 `validated_pc`, 1 `validated_n1000_v12c` (read from the YAML); `scale` counts provincial 26, personal 13, thread 13, primitive 12, peninsular 8, service 6, territory 4, world 4, cross_scale 4. Not read by the engine (a grep for `mechanics_index` shows only skills, `engine/season/harness/register.py` and a comment); it is reference, not a mechanism (§0.05).
  - Hard-codes a game fact: `categories.victory_paths == ['peninsular_sovereignty']` (GD-1, exactly one victory path) as an ERROR (`:280-303`). This contradicts the engine direction where the season loop reports `endings` (export_game_constants notes `H-176`) and "the retired oracle modelled no ending"; the validator enforces a single-victory design rule from a register nothing executes.
  - `VALID_SCALES` use the old peninsular/provincial/thread vocabulary (`:96-106`).
  - `find_repo_root` markers `canon` + `references` (`:423`); previously fataled on a retired `sim/` marker unnoticed because the CI job is report-only (`:412-422`).
- **Conflicts / stale:** docstring "v2 scope" mentions `designs/`, `sim/`; sim_module paths in the register may point into `systems/` code that moved.
- **Open items:** whether a report-only validator over an unread register should exist at all.

### tools/methodology_drive.py
- **What it is:** unattended driver: runs `/methodology-execute` once per fresh `claude -p` process, reading the status line `METHODOLOGY-EXECUTE: COMPLETE | NEXT <handle> | STOPPED <reason>` (exit 0/3/4/2).
- **Status:** no Status line; live utility, run by a person; not CI, not a hook, not in the registry; self-declares "NOT A GUARD" (`:16-18`).
- **Bears on:** PROCESS (agent orchestration).
- **Content that matters:**
  - Refuses `-c/--continue/-r/--resume/--bare`; requires `.claude/skills/methodology-execute/SKILL.md` to exist (`:59-61,:105-115`); sets `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`.
  - Spend caps `--max-total-usd` and per-batch `--attempts`; stops on a repeated `NEXT` handle (no progress).
  - Constructs the CLAUDE.md §11-adjacent pattern (a loop that starts the next process after the previous exits); the file argues it is not self-scheduling because a person runs it.
  - Imports `ci_common` as a bare name (`from ci_common import REPO`), so it only runs with `tools/` on `sys.path` (works because the script's own directory is `sys.path[0]` when executed as a script).
- **Conflicts / stale:** `.claude/skills/methodology-execute/` path is the checked location; CLAUDE.md §9 routes `methodology-execute` to `skills/`: verify which root exists `[UNVERIFIED]`.
- **Open items:** none.

### tools/names.py
- **What it is:** the tools-side single reader of `references/names_index.yaml` (`entries`, `canonical`, `aliases`, `legacy`, `all_legacy(enforce=)`, `key_for`, `context`, `by_category`, `by_token_class`); fault-tolerant (returns `{}` on any failure).
- **Status:** no Status line; live; imported by `ci_naming_check`, `ci_names_consistency`, `hook_naming_guard` (transitively), the vector-audit skill.
- **Bears on:** PROCESS, WR/FA/CHAR (vocabulary).
- **Content that matters:**
  - Default `enforce` tier when absent is `warn` (`:109`); an unknown tier silently matches nothing (the index header's "NOTHING VALIDATES this field").
  - `by_token_class` masks `category` with `token_class` (`:151-163`); `context()` carries the disambiguation terms for display strings colliding with English words (Faith/Order/Reason).
  - Two readers of the same index exist: this (YAML, tools/CI) and `engine/substrate/names.py` (JSON `names.json`, runtime). They share the exporter's rules only through `export_names.py`; this reader does NOT enforce the idempotence rules at load.
  - Cache `_cache` is process-global; tests passing `path` bypass it.
- **Conflicts / stale:** docstring cites `tools/valoria_rename.py` (retired).
- **Open items:** none.

### tools/pathres.py
- **What it is:** library + CLI (`resolve`, `scan`, `pipeline`): the intended single owner of path-reference extraction and resolution through `references/restructure_ledger.md` (`LIVE | ALIASED | DEAD | FORKED`); also `py_joined_paths`, `py_path_io` AST I/O tracer.
- **Status:** no Status line; live; imported by `broken_dependency_checker`, `ci_claim_provenance_check`, `build_identifier_census`, tests, skills. Not a gate itself. Self-admits it is NOT yet the sole parser (`:189-197`): `broken_dependency_checker` and two vector-audit scripts keep their own.
- **Bears on:** PROCESS (path resolution for the retired/forked tree), no game bearing.
- **Content that matters:**
  - `resolve()` returns a `Resolution` object whose `__bool__` raises TypeError so a caller must say which question it asks (`:163-186`). Directory-prefix rows match any filename under a forked directory (CLAUDE.md §8 warning): `load_alias_map()` exact rows are the right question for "is this exact file retired".
  - `fork_pointer(sentinel, path)` is the one answer to "what a FORK row resolves to": `FORK:<ref>:<path>` (`:116-160`); `test_forked_status.UNRESOLVABLE_CEILING` = 78 rows whose paths moved before the ref (`:145-152`).
  - Later row wins for repeated keys (8 conflicting keys measured); 654 of 1,363 probes disagree with bdc's `_resolve_remap` because it folds the existence check in (`:247-258`).
  - `TREES` roster includes dissolved `designs`, `sim`, `params`, `arcs` deliberately (`:92-96`).
  - `pipeline` lists paths written-never-read and read-never-written across `tools engine systems tests`; admitted lower bound (`:621-633`).
- **Conflicts / stale:** the docstring's counts of parsers (four, then three) are re-measured notes; `ci_claude_workflow_paths` is retired.
- **Open items:** porting `broken_dependency_checker` and the vector-audit scripts onto this module (explicitly refused by D1).

### tools/quantity_registry.py
- **What it is:** reader library: merges `descriptor_registry.yaml` (via `descriptor_registry.load`) and `names_index.yaml` into one known-vocabulary map and resolves a raw stat identifier with normalisation (underscore->space, strip parenthetical, strip Track/Clock/Pool/Field suffix).
- **Status:** no Status line; live as a library; sole production caller `ci_quantity_vocabulary_check.py` (report-only) plus `tools/registry.py`, vector-audit skill scripts and tests.
- **Bears on:** PROCESS, CORE (vocabulary closure).
- **Content that matters:**
  - `load()` includes descriptor sections attributes, aggregates, faction_stats, practitioner_stats, territory_stats, settlement_stats, `category_b_scalars` (Wounds/Turmoil/Accord/Poise/Initiative/season counter), `by_reference`, and `not_descriptors` buckets `derived_values/tracks/clocks/pools` (`:127-164`); `faction_stats` is read though `export_descriptors` no longer cooks it.
  - Resolution is "best effort" over prose-adjacent display strings (own admission `:28-31`); case-insensitive; no key returned for `not_descriptors` hits.
  - Cache is process-global; fault-tolerant (returns empty on any failure).
- **Conflicts / stale:** docstring mentions a "KeyLog stat_vocabulary hook" (retired substrate).
- **Open items:** none.

### tools/registry.py
- **What it is:** read-side FACADE over `names`, `descriptor_registry`, `quantity_registry`: `resolve(term)` tries descriptor -> names -> quantity and discloses disagreements; also `resolves`, `all_known`, `collisions()`.
- **Status:** no Status line; live as a library (tests, skills); no gate; "WS1 step one" of a "one registry, one reader" program whose end state (`references/registry/*.yaml`) is PROPOSED, not built.
- **Bears on:** PROCESS, CHAR/FA/SE (vocabulary).
- **Content that matters:**
  - Fourth vocabulary reader on top of three (names / descriptor_registry / quantity_registry) plus the runtime leaves `engine/substrate/{names,descriptors}.py`: six readers of two YAML files.
  - `collisions()` reports display strings bound to more than one descriptor key; its live remainder per the docstring is "legitimacy" -> `fac.legitimacy`, `set.legitimacy` (`:389-400`). `export_names.names.json` `ambiguous` records `Order` and `Reason` (not Legitimacy); so a third ambiguous string is known to one reader and not recorded in the cooked artifact, a possible runtime divergence `[UNVERIFIED]`.
  - Alias `Influence` was removed from attr.social.charisma so `fac.influence` owns it (2026-09-16) (`:97-104`).
  - Disclosed example: "Thread Fatigue": names -> `thread.thread_fatigue`, quantity -> keyless (`:80-85`).
- **Conflicts / stale:** docstring says the attribute roster is "the 9-attribute" (`:48`); descriptors.json carries 10.
- **Open items:** the WS1 end state.

### tools/session_provision.py
- **What it is:** silent provisioner: installs `pyyaml pytest numpy pytest-xdist` via pip if any import is missing; prints nothing.
- **Status:** no Status line; live as a command. NOT installed as a hook: `.claude/settings.json` has `"SessionStart": []`, and a grep of `.claude/` for the name finds nothing; CLAUDE.md §8 lists it as a command a person/agent runs. Its docstring says "SessionStart hook" and CLAUDE.md §0.3 calls it "the allowed shape". Described as hook; wired as nothing.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Exits 0 always; errors swallowed; `REQUIRED` map import-name -> pip-name (`:26-31`) is the copy of CLAUDE.md §8's package list that must be kept in step by hand.
  - `numpy` is installed because the combat surface needs it (CI comment `valoria-ci.yml:277-288`).
- **Conflicts / stale:** hook claim vs `settings.json`.
- **Open items:** whether to wire it (CLAUDE.md §0.3 permits a silent hook).

### tools/tag_normalizer.py
- **What it is:** import-only library for `[[id]]` / `[[id|display]]` canonical-identifier tags in prose: `find_tags`, `render`, `strip`, `unknown_tags`, `stray_open_brackets` (Reconciliation Program §3).
- **Status:** no Status line; effectively DEAD in practice: `[[...]]` tags do not occur in the corpus (a grep for `[[<dotted id>]]` finds only `references/names_index_history.md`); callers are `tests/valoria/test_tag_normalizer.py` and `skills/valoria-vector-audit/scripts/workbench.py`.
- **Bears on:** PROCESS (prose vocabulary).
- **Content that matters:**
  - Resolves ids through `names.canonical` (the tools-side reader); an unknown id stays raw (`'keep'`), so typos surface (`:70-99`).
  - Designed as a "change once" mechanism for display names inside prose: a mechanism for prose that §0.05 demotes to reference.
- **Conflicts / stale:** none.
- **Open items:** delete (process-only; no tags in the corpus).

### tools/tests_for_diff.py
- **What it is:** inner-loop helper: lists changed files (since merge-base with `origin/main`, staged, unstaged, untracked) and prints the narrowest pytest command(s); `--run` executes them.
- **Status:** no Status line; live; not CI. CLAUDE.md §0.4 names it at close.
- **Bears on:** PROCESS; encodes the test-to-subsystem map for PC, MB, SC only.
- **Content that matters:**
  - Only three subsystems have pytest markers: `combat` (`modules/combat/`, `systems/combat/`), `mass_battle`, `social_contest` (`SOURCE_PREFIXES`, `:31-35`); the filename regexes live in root `conftest.py` `SUBSYSTEM_FILES` (single owner). Fieldwork, settlements, threadwork, world, characters, factions and the season loop have no marker: any edit there forces the full commands (`commands()`, `:81-86`).
  - Admits the narrow answer misses realm-level effects: "a `modules/combat/` edit is reached by tests costing about three quarters of the season suite" (measured 2026-11-04) (`:14-18`).
  - Trees run: `tests/valoria`, `engine/season/tests`, `engine/tests` (`:37`).
- **Conflicts / stale:** none.
- **Open items:** none.

### tools/triage_work_items.py
- **What it is:** classifier of editorial-ledger work items (effective status unresolved or `needs_jordan`) into CODE / PROPOSAL / DOC-DEFECT / REFERENCE-ONLY / UNCLASSIFIED, by regexes over their text fields (Jordan 2026-08-24: "If the work item doesn't concern code, then it isn't a work item"); `--list`, `--json`.
- **Status:** no Status line; live utility. Not CI. Its `machine_read_inputs()` is imported by the live hook `hook_md_sweep_guard.py` (so this file is on the agent's Grep/Glob path).
- **Bears on:** PROCESS (the `needs_jordan` queue; cull of doc-subject items).
- **Content that matters:**
  - Default is KEEP: unclassifiable rows are work; PROPOSAL (unbuilt mechanics: "AUTHORED (", "Grounding:", "OPT-", "SE-N", "FA-N", "needs Jordan") is tested before any doc test so the design backlog is not culled (`:59-88,:226-234`).
  - `machine_read_inputs()` regex-scans `tools engine systems skills` for quoted `.yaml/.json/.jsonl/.md` names within 200 chars of a read-context token (`:149-168`): a heuristic that decides which `.md` count as "inputs".
  - `code_identifiers()` reads `engine_params/key_types.json` (retired, guarded by existence) and `composition.json` role names plus `systems/` directory names; it deliberately refuses to parse `module_contracts.yaml` (a ratchet test, `test_no_new_parser_of_an_authored_surface`, `:120-124`).
  - Records two mis-culls (ED-IN-0014, ED-IN-0004) that named Key types rather than filenames; the Key vocabulary that prevented them is gone (`:111-118`).
  - Imports `validate_ed_citations` (`V._is_resolved`) for the "unresolved" predicate.
- **Conflicts / stale:** it treats every `.md` that code "reads" as an input, which is the §0.05 cl.4 boundary; the sweep guard's allowlist inherits whatever this regex finds.
- **Open items:** none.

### tools/valoria_local.py
- **What it is:** local orchestrator (`.githooks/pre-commit` runs `valoria_local.py --staged`): shells a fixed list of validators, blocking vs report-only; `--local` HEAD~1..HEAD; `--ci` retired.
- **Status:** no Status line; live; local tier only. Registry says it has no subject (dispatch, no verdict aggregation).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Blocking locally (`:68-92`): ci_pp_frozen_check, ci_naming_check, ci_names_consistency, ci_design_prose_quarantine, ci_co_file_checker, ci_editorial_checker, ci_register_size_check, ci_vetting_check, ci_sim_fabrication_check, ci_claim_provenance_check, and `--check` of export_engine_params, export_game_constants, export_descriptors, export_composition, export_battle_orders, export_npc_roster. Report-only locally: ci_naming_check --warn, ci_generation_consistency, ci_module_shape_check, currency_consistency_check, freshness_gate, validate_ed_citations, broken_dependency_checker.
  - ASYMMETRY (the pattern its own text says is the defect): `export_names.py --check` is BLOCKING IN CI (`valoria-ci.yml:157`) and ABSENT here; `export_battle_orders.py --check` is blocking HERE and ABSENT from CI. `ci_quantity_vocabulary_check`, `mechanics_index_gen`, `canon_coverage_check`, `ci_vacuous_assertion_check`, `m1_acceptance` (CI report-only) and `compliance_check`, `ci_golden_modes_check` (CI-only) are not local. The recurrence guard (`test_gate_coverage.py`) was retired, so nothing detects it.
  - Does not run pytest and does not grade the changeset at CI scope: changeset-scoped gates grade ADDED lines against index/last commit locally but `origin/main...HEAD` in CI (PR #421 reddened twice, `:14-33`); recipe: `GITHUB_BASE_REF=main GITHUB_EVENT_NAME=pull_request python3 tools/ci_sim_fabrication_check.py`.
  - Exit semantics: report-only failures print a qualified pass line, never fail (`:221-226`).
  - Missing scripts are skipped silently (`if not os.path.exists(path): continue`, `:194-195`).
- **Conflicts / stale:** comments at `:108` and `:160` say "blocking in CI's integrity job" (collapsed into `validators`); the `:88` comment "MIGRATION-WINDOW gate: retire with engine/params/" names a check no longer in the list.
- **Open items:** the two-list asymmetry above (`export_names`, `export_battle_orders`).

### tools/validate_ed_citations.py
- **What it is:** blocking validator: every `ED-NNN` / `ED-<LANE>-NNNN` cited in scanned docs must resolve to a ledger entry (active ledgers + lane files + `_archive` JSONL siblings + `registers/archive/*.yaml`), and an OPEN ED must not be cited as a basis ("canonical", "ratif", "applied", "closes", "per ed" ...). `--info`, `--path`.
- **Status:** no Status line; live, blocking (`validators`); report-only in `valoria_local`.
- **Bears on:** PROCESS (citation provenance in canon/design/reference docs); the `ED` ledger universe (about 1,264 ids at the 2026-08-23 relocation).
- **Content that matters:**
  - Scan scope `SCAN_PREFIXES = ('canon/','designs/','.designs/','systems/','references/')` with suffixes `.md .yaml .yml` (`:130-131`); NOT scanned: `proposals/`, `engine/`, `modules/`, `architecture/`, `registers/` docs, `skills/`; working docs (`workplans/`, `*workplan*`) are excluded by mandate. So a new proposal citing a nonexistent ED is invisible to the gate.
  - `.designs/` is deliberately scanned (quarantine must not hide prose from citation audits); a burn-down allowlist keeps four known open-as-basis pairs, ceiling `BURN_DOWN_MAX = 9`; two pairs are in `.designs/systems/_architecture/reference/key_type_registry_v30.md` (retired Key substrate) and two in `articulation_layer_v30.md` (`:162-171`).
  - Statuses that count as resolved: resolved*, ratif*, landed, struck, applied, superseded, closed, confirmed, deprecated (`_is_resolved`, `:215-232`). `needs_jordan` is NOT considered.
  - PP is parsed by the regex but `checked_prefixes=('ED',)` only (`:577`): PP citations are never validated here (CLAUDE.md §0 notes "PP provenance is unvalidated").
  - Excludes generated sidecars (`_*` with the banner `GENERATED by tools/`) so the identifier census quotes are not double-counted (`:398-424`).
  - YAML archive fragments that fail to parse are regex-salvaged and warned (`:351-366`).
- **Conflicts / stale:** reads dissolved `designs/` prefix; `WORKING_PREFIXES` still includes `designs/audit/`; `.audit/` not in scope (consistent with its hidden status).
- **Open items:** none.

### tools/verify_handoff_split.py
- **What it is:** one-shot FALSIFIER for the 2026-09-13 handoff split (ED-IN-0221): proves per lane (IN, MB, PC, SC) that every content line of the pre-split `HANDOFF_<LANE>.md` is still readable in the live / `_closed` / `_history` siblings; `--stress N SEED` measures its own sensitivity by deleting one real line at a time.
- **Status:** no Status line; live but self-described as "NOT A GATE, MUST NOT BECOME ONE" and wired nowhere (`:55-63`); "Delete it once the split is old news".
- **Bears on:** PROCESS only (handoff files).
- **Content that matters:**
  - Content comparison by normalized words with three bounds (still a line; glued to a neighbour; anchored cover for a one-line block) and a `MIN_RUN_CHARS` floor of 24, measured: first false alarm on the real split appears at 43 (`:279-294`).
  - Reports exit 1 only for lost content or an unreadable pre-split ref; reparenting and exact-line deficit are report-only (`ED-IN-0239` edits made the exact column non-zero).
  - Quoted-index-row coincidence is its residual blind spot, stated on the OK line (`:643-656`).
  - `LANES = ('IN','MB','PC','SC')`: only four lanes, though nine handoffs exist.
- **Conflicts / stale:** needs git history reaching the `HANDOFF_IN_closed.md` add commit; a shallow clone cannot resolve `_before_ref` (`:366-372`).
- **Open items:** deletion is owed by its own text; 36 KB of process tooling for a closed event.

### tools/vocab_store.py
- **What it is:** generator + parity checker for the "vocabulary fold" (ED-IN-0078): `references/definitions/vocab_source.yaml` is the source; `alias_registry`, `deprecated_terms_registry`, `censured_vocabulary`, `synonym_registry` are GENERATED views; `name_collision_database` is a frozen mirror. `--seed`, `--build`, `--check`.
- **Status:** no Status line; ORPHAN-ish. Not in CI, `valoria_local` or the registry; only `tests/valoria/test_vocab_store.py` runs it. Its stated sole consumer, `tools/observability/build_lexicon.py`, is retired (`tools/observability/` is gone). `vocab_source.yaml` exists (the only file in `references/definitions/`).
- **Bears on:** PROCESS (vocabulary registers; no runtime reader).
- **Content that matters:**
  - Four registers are regenerated as YAML dumps with a `GENERATED` header; per-register hand-authored doc headers kept in `view_headers` (`:65-99`).
  - The registers carry deprecated names as data, which is why `ci_naming_check.EXCLUDE` lists them.
  - Runtime vocabulary reaches the engine through `export_names` -> `names.json` instead, not through these registers; the engine substrate leaves reference `alias_registry` only in a comment/docstring (`export_names.py:6-8`).
- **Conflicts / stale:** consumer retired; `definitions_store.py` is the sibling "Phase 2" (also orphan).
- **Open items:** delete or keep as a generated-view mechanism nothing reads.

---

## Cross-subsystem leads

- **Which game facts actually have a typed route to the engine (CORE, all):** the CI-blocking exporters that cross into runtime are `export_descriptors` (10 attributes + scale, 15 pursuits, 7 ethical axes, 5 affiliations with `concerns`, 5 heritages; settlement stats `set.legitimacy|popular_support|prosperity|defense|order|facility_tier`; `prac.thread_sensitivity|tps`; `terr.fort_level`; NO faction stats since plan position 29b), `export_names` (122 canonical names, 19 legacy, `Order`/`Reason` recorded ambiguous), `export_composition` (16 roles: `combat.fight`/`mass_battle.resolve_field`/`social_contest.roll` as verb_call; `fieldwork.find`, `settlements.produce|subsist` as step_call; mass_battle.army*/settlements.* as query; no role for factions, governance, diplomacy, threadwork, victory, characters), `export_npc_roster` (46 NPC rows), `export_engine_params` (combat: 214 cfg + 26 core + 8 attributes + 54 weapons) and `export_battle_orders` (MB order roles/retreat triggers; CI-wired only through a season test, not the workflow). FA, SE economy, WR and FI constants reach `sim_params.json` only if they sit in `engine/`, `systems/*/sim` or `modules/*`; that artifact has 283 constants, 158 uncited, 164 of them `mass_battle`, and none from `settlements`, `factions`, `world` (tags FA, SE, WR, FI, MB).
- **The Godot port is almost entirely hand-transcribed (GO, DICE, PC, WR):** `export_game_constants` pairs only five constants (`TN_STANDARD` 7, `COMBAT_POOL_MINIMUM` 5, `KNOT_FORMATION_TN` 7, `KNOT_FORMATION_OB` 2, `SEASONS_PER_YEAR` 4) against the port's ~200 hand-typed constants, and records three open model divergences that need rulings: accord (oracle holds none; port integer 0-3), weapon TN (oracle always 7, port 5-8 per weapon), coherence (oracle two-quantity distance model; port 10-0 depleting track with four bands). Port `POOL_FLOOR` (1) and `MOMENTUM_MAX` (4) are different quantities from the oracle's namesakes (5; `M_MAX` 1.5), and "Momentum 0-4 has no scalar owner in engine/ today".
- **The only execution instrument for the game is `m1_acceptance` (CORE, all):** four rows, report-only in CI; two run `engine/season/` headless (stub delta, same-seed `World.content_hash()` equality, seed 20260819), one sweeps 8 invariants over 24 headless seeds x 4 seasons plus the 46-NPC populated world (2 seeds x 1 season), one is doc-derived (`status: met` in `engine/season/requirements.yaml`). No CI signal can fail on regression (registry's own admission). Its docstring/registry still describe five rows and an `m1_junctures` row that code no longer has.
- **Test-to-subsystem map exists only for PC, MB and SC (all):** `tests_for_diff.py` + root `conftest.py` `SUBSYSTEM_FILES` give pytest markers `combat`, `mass_battle`, `social_contest`; fieldwork, settlements, threadwork, world, characters, factions have none, so any edit there runs the full gates.
- **MB regression oracle (MB, DICE):** `ci_golden_modes_check` runs `systems/mass_battle/sim/bat.py --check` in 3 digest modes (`unit_field_mor0`, `cell_field_mor0`, `cell_legacy_mor1`) with ~75 pinned env toggles = the shipped MB tuning surface (e.g. `ROUT_CASCADE_FRAC` 0.6, `POOL_QUALITY_SCALE` 0.8, `K_LINEAR` 12, `K_SQUARE` 0.25, `MB_VOLLEYS_START` 10, `MB_AMMO_ENABLED` 1, `MB_SUPPORT_RANK_CAP` 1, `MB_CELL_EXCLUSION` 1); the two legacy grid modes are pinned by nothing. Green means "digest unchanged", not balanced.
- **Fabrication gate does not cover personal combat's oracle (PC):** `ci_sim_fabrication_check` scope excludes `modules/combat/` (`MODULES_WITH_OWN_EXPORT = ('combat',)`; "KNOWN GAP" filed ED-IN-0119); combat's constants are covered only by the round-trip export, which proves equality to the oracle, not provenance. `ci_module_shape_check` INFO tier lists untagged module-scope constants there but never fails.
- **Dice kernel parity is with historical oracles, not canon (DICE, SC, PC):** `gen_sigma_parity_goldens` freezes `engine/dice_engine/sigma_leverage.py` against `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` and the ground-up contest engine copy under `engine/reference/contest-groundup/`, over net-sigma, pool 1/5/10/26, TN 6/7/8 grids plus five (pool, net) pairs on the pool-aware Overwhelming bar (`OVERWHELM_SIGMA`); its `--check` is unwired.
- **Victory/endings (FA, WR, CORE):** `mechanics_index_gen` hard-fails any `victory_paths` other than the single `peninsular_sovereignty` (GD-1) in a register no code reads, while `export_game_constants` records that the season loop "reports `endings` since v9 IN-27 (H-176)" and carries no sustain count. The two disagree about whether the game has one ending.
- **Retired vocabularies still wired into gate text (all):** Key substrate (ED-IN-0232) remains in `hook_md_sweep_guard` message, `build_identifier_census.built_names`, `triage_work_items.code_identifiers`, `ci_quantity_vocabulary_check` docstring, and the two `validate_ed_citations` BURN_DOWN pairs on `key_type_registry_v30.md`.

## Likely stale or superseded

Dead or empty subject (gate runs, observes nothing):
- `tools/ci_generation_consistency.py`: reads `canonical_sources.yaml` for `.md` docs under `designs|systems`; `grep` count 0 and `systems/` holds no `.md`, so zero documents are checked.
- `tools/canon_coverage_check.py`: walks `systems/` for `Status: CANONICAL` in `.md/.yaml/.svg`; no `.md` exists there (quarantine), so `registered_no_header` is the whole registry.
- `tools/ci_co_file_checker.py` Rule 1 (`systems/.+_v30.md`) and `tools/ci_editorial_checker.py` prefixes `systems/npcs/`, `systems/world/` can never match a tracked `.md` (blocked by `ci_design_prose_quarantine`); only `canon/03_` is reachable.
- `tools/currency_consistency_check.py` `check_dead_maintainers` (no `deprecated/skills/`), `check_patch_register_header` (frozen counter); `tools/ci_vetting_check.py` and `tools/ci_pp_frozen_check.py` guard the frozen PP register.
- `tools/broken_dependency_checker.py` sub-check (b2) ("a registry row's `ci_job` is really invoked by that job") has been a no-op since `_gate_jobs()` returns `[]`; the registry header still claims the join is enforced "in both directions".
- `tools/freshness_gate.py`: about seven `canonical_sha__` pins remain; detects document change, not code agreement.

Orphans (no caller, or broken):
- `tools/definitions_store.py` (store file absent), `tools/link_values_pointers.py` (reads the absent store; `value_pointer_links.json` stale in `engine_params/`), `tools/vocab_store.py` (consumer `build_lexicon` retired), `tools/tag_normalizer.py` (no `[[id]]` tags in corpus), `tools/join_audit_workings.py` (archive-only, stale `audit/` path), `tools/build_engine_atlas.py` (both execution inputs retired; outputs untracked; reads a `.designs/` roster table as input), `tools/build_identifier_census.py` (outputs untracked; reads prose; still reads the retired Key-registry md), `tools/verify_handoff_split.py` (one-shot falsifier, wired nowhere, "delete once old news"), `tools/gen_sigma_parity_goldens.py --check` and `tools/export_sim_params.py --check` (run only by pytest, not by the workflow or registry), `tools/session_provision.py` (documented as a SessionStart hook; `settings.json` has `SessionStart: []`).
- `tools/README.md`: names `export_key_types.py`, CI job names that no longer exist, an `integrity` job collapsed in 2026-08, and omits ~15 live tools.

Doubled:
- Ledger parsers: `broken_dependency_checker`, `currency_consistency_check`, `validate_ed_citations`, `ci_claim_provenance_check._load` and `ci_common.read_editorial_ledger_rows` each read the editorial ledgers with their own globs; `restructure_ledger.md` has `pathres`, bdc's `_load_restructure_map` and two vector-audit parsers.
- Vocabulary readers: `names.py`, `descriptor_registry.py`, `quantity_registry.py`, `registry.py`, `definitions_store.py`, plus runtime `engine/substrate/{names,descriptors}.py`.
- Size caps: `ci_register_size_check.py` (per-path table) and `compliance_check.py` (pattern table from `atomization_rules.yaml`), each with its own policy parser.
- Local vs CI lists disagree: `export_names --check` CI-only; `export_battle_orders --check` local-only; no guard (the recurrence test was retired).

Registry/text drift: `ci_checks_registry.yaml` header says nothing is `subject: game` yet marks `export_battle_orders` and `export_npc_roster` as `game`; `ci_vacuous_assertion_check` role text claims detection of `pytest.approx` and zero-iteration loops that the code does not implement; `m1_acceptance` docstring/registry row count (five vs four).

## Items that could change an audit finding

(No `F-*` ids were cross-checked from `audits/*.md`; claims are described.)
- **"The port validates against the oracle" (GO, DICE, PC, WR):** the typed bridge covers five constants; three oracle/port model disagreements are open (accord, weapon TN, coherence); the oracle holds no accord state and no victory-sustain model. Any GO finding that treats Godot constants as derived from the oracle is overstated.
- **"Constants in the engine are provenance-gated" (PC, MB, CORE):** `ci_sim_fabrication_check` grades only ADDED lines in `engine/`, `systems/*/sim`, `modules/*` except `modules/combat/`; 158 of 283 exported sim constants carry no citation; cited means "a marker string is present". Nothing checks a marker against its source.
- **"The season loop is gated" (CORE):** CI wires `m1_acceptance` report-only and by registry admission "NO GAME-FACING SIGNAL CAN NOW FAIL CI ON REGRESSION" (the season's own pytest job is a separate gate, not in this lane). Row 3 is doc-derived from a YAML `status:` string.
- **"Descriptors/factions" (FA, CHAR):** `descriptors.json` carries no `fac.*` stats since 29b, yet `ci_names_consistency` and `names_index` still mirror `fac.*` rows, and `quantity_registry` still reads `faction_stats`; the faction stat vocabulary exists in registries but has no runtime artifact route.
- **"Single victory path" (FA, WR):** a validator hard-codes GD-1 `peninsular_sovereignty` while the season loop reports `endings`; an audit claiming one ending, or many, can cite either side.
- **"NPC cast is authored" (CHAR, WR):** `engine/season/npcs.yaml` is generated from `cases/NPC*.yaml` and hand-editable after; `--check` fails only on dangling references, not on drift; two NPC data heads (`references/npc_registry.yaml` identity/convictions/role vs `npcs.yaml` placement/wants).
- **"Naming is enforced" (WR):** the naming gate enforces one block-tier deprecated proper noun; `names_index.yaml`'s `enforce` field is unvalidated (an unknown value silently disables a row); the edit-time hook misses `Bash` edits.
- **"Mass-battle cell/weapon design is pinned" (MB):** three digest modes pin the shipped cell-based configuration; no instrument observes that the weapon-carry/cell design intent holds, and the legacy grid modes are unpinned.
- **"Tests are scoped per subsystem" (all):** only PC, MB and SC have markers; the realm-level effect of a module edit is reached only by the full season suite (about three quarters of suite cost, measured 2026-11-04).

