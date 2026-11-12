# Digest tools

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: everything under `tools/` (55 `.py` plus `README.md`; `ls tools | wc -l` = 56 entries). Read in full, to the end.

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

