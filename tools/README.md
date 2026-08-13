# Valoria Tools Directory

The "CI Tools" and "Integrity Tools" tables below are **generated from
`references/ci_checks_registry.yaml`** (regenerated 2026-07-11, ED-IN-0033) rather than
hand-maintained a second time — that registry is now the single source of truth for what
each checker enforces, which CI job runs it, and whether it's blocking or report-only.
When a tool or job changes, update the registry first; this table is downstream of it, not
an independent record. (`references/ci_checks_registry.yaml` also carries a small mechanical
verifier — `tools/broken_dependency_checker.py::check_ci_registry_coverage()`, run in the
`validators` CI job — that cross-checks the registry's `path` and `ci_job` fields against
the working tree and the workflow, so this pairing can't silently drift the way the
pre-2026-07-11 snapshot did. The `paired_hook` field it also used to check was retired
2026-08-12 with `valoria_hooks.py`'s evacuation; the `integrity` job it used to name was
collapsed into `validators` on 2026-08-01.)

## CI Tools (wired into `.github/workflows/valoria-ci.yml`)

Blocking jobs fail the build; report-only jobs run with `continue-on-error: true` and are
excluded from `ci-summary`'s `needs:` list (see CLAUDE.md §8 for the report-only → blocking
ratchet convention). The three tools that run inside the `integrity` job are broken out
separately below, matching that job's own internal grouping.

| Tool | CI job | Blocking? | Purpose |
|---|---|---|---|
| `ci_register_size_check.py` | `register-sizes` | blocking | Token-threshold enforcement on governed files (session log, ledgers, registers, canonical_sources) |
| `ci_hooks_verifier.py` | `hooks-verifier` | blocking | Enforcement architecture intact: hooks wired, skeleton limits |
| `ci_co_file_checker.py` | `co-file-check` | blocking | Co-file requirements (design→canonical_sources, patch→propagation_map, sim→coverage_matrix) |
| `ci_editorial_checker.py` | `editorial-check` | blocking | Editorial paths carry `[EDITORIAL]`/`[PROVISIONAL]` markers |
| `ci_naming_check.py` | `naming-check` | blocking | Naming invariant gate over `enforce: block` entries in `references/names_index.yaml` |
| `ci_names_consistency.py` | `names-consistency` | blocking | descriptor/proper-noun registry mirrors agree with `names_index.yaml` |
| `ci_names_check.py` | `names-drift` | report-only | Naming-drift lint over every `enforce: warn` entry in `names_index.yaml` |
| `currency_consistency_check.py` | `currency-consistency` | report-only | Self-updating recency gate (ED-1087): stamps, ID ceilings, register headers, dead maintainer pointers |
| `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` | `contract-conformance` | report-only | Module contracts conform to the Key Type Registry + canonical sources (not in `tools/`, listed here for completeness) |
| `ci_quantity_vocabulary_check.py` | `quantity-vocabulary-check` | report-only | A17 stat-vocabulary closure: identifiers resolve to descriptor_registry/names_index |
| `mechanics_index_gen.py --strict` | `mechanics-index-check` | report-only | `canon/mechanics_index.yaml` schema, cross-reference, and GD-1 drift validation |
| `ci_generation_consistency.py` | `generation-consistency-check` | report-only (warn-only by design) | v40 generation currency: every canonical doc has a Status line and isn't superseded |
| `canon_coverage_check.py --strict --json` | `canon-coverage-check` | report-only | Bidirectional `Status: CANONICAL` ↔ `canonical_sources.yaml` verification |
| `ci_audit_registry_check.py` | `audit-registry-check` | report-only | Flags a `designs/audit/` folder newer than `references/audit_registry.jsonl`'s latest record with no matching entry |
| `export_engine_params.py --check` | `engine-params-roundtrip` | blocking | Typed engine-params JSON matches the canonical combat oracle (`config.py`) |
| `ci_module_shape_check.py` | `module-shape-check` | report-only | Holonic container hygiene: no `tests/` reach-ins or imports in engine/sim runtime code |
| `ci_sim_fabrication_check.py` | `sim-fabrication-check` | blocking | Every numeric literal in `sim/*.py` is ledger-cited or canonical-source-commented |
| `ci_supersession_check.py` | `supersession-check` | report-only (warn-only by design) | Flags changesets touching a path in a supersession-register `files_to_recheck` list |
| `ci_vetting_check.py` | `vetting-check` | blocking | PP-674 framework vetting: PP entries ≥674 carry a valid `vetting:` block |
| `validate_ed_citations.py` | `ed-citations` | blocking | Every cited ED-NNN / ED-`<LANE>`-NNNN resolves to a real, non-open ledger entry |
| `compliance_check.py --check-only --repo-state .` | `compliance-check` | blocking | Working-tree size-cap compliance scan (`atomization_rules.yaml` thresholds) |

## Integrity Tools (run inside the `integrity` CI job)

| Tool | Purpose |
|---|---|
| `broken_dependency_checker.py` | Scans propagation_map / canonical_sources / editorial ledgers for refs to nonexistent files; also runs `check_ci_registry_coverage()` (this file's own self-check, see above) |
| `freshness_gate.py` | Detects drift between canonical docs and their SHA records in `canonical_sources.yaml` |

## Utility Tools (manual use, not covered by `ci_checks_registry.yaml`)

These are generators, one-off migration executors, or shared library modules — not
gates/checkers, so they're intentionally not in the registry above.

| Tool | Purpose |
|---|---|
| `build_apparatus_registry.py` | Generates `references/apparatus_registry.{yaml,md}` — the inventory of every tool/skill/hook/workflow (output destination + format + orphan status) |
| `valoria_rename.py` | The "change once" executor for `names_index.yaml`-centralized definition renames |
| ~~`atomizer.py`~~ | **RETIRED 2026-08-13 → `deprecated/tools/` (ED-IN-0175).** Zero importers/invokers; Jordan's ruling *"Dead files get moved to deprecated."* (ED-IN-0171) |
| ~~`index_gen.py`~~ | **RETIRED 2026-08-13 → `deprecated/tools/` (ED-IN-0175).** Same wave. Its sole artifact (`registers/patch_register_index.md`) was last regenerated 2026-05-10 |
| ~~`doc_index_gen.py`~~ | **RETIRED 2026-08-13 → `deprecated/tools/` (ED-IN-0175).** Same wave. ⚠ Its **37 `systems/**/*_index.md` outputs are NOT retired** — grandfathered by the 2026-07-26 ruling, disposition HELD |
| `observability/obs_core.py` | Shared observability primitives (ledger reader, lane roster, status/marker parse, JS-bundle) — single owner, imported by the generators |
| `observability/build_proposals.py` | Generates the unified proposals/open-work register (`PROPOSALS.md` triad) |
| `names.py` | The single reader for `references/names_index.yaml` (legacy→canonical mapping) |
| `descriptor_registry.py` | Loader/resolver for `references/descriptor_registry.yaml` (key/name/alias resolution) |
| `quantity_registry.py` | Single reader for the merged quantity/attribute vocabulary (descriptor_registry + names_index) |
| `ci_common.py` | Shared changeset-diffing helpers used by the `ci_*.py` validators, the local hook, and the unit tests |
| `session_status.py` | Claude Code `SessionStart` hook — plain-language status banner from git + HANDOFF.md |
| `session_handoff_reminder.py` | Claude Code `Stop` hook — nudges to update HANDOFF.md if the tree is dirty at turn end (never blocks) |
| `hook_naming_guard.py` | Claude Code `PreToolUse(Write\|Edit\|MultiEdit)` hook — edit-time naming-invariant nudge (reuses `ci_naming_check.py`'s core) |
| `valoria_local.py` | Runs the same `ci_*.py` validators CI runs against the local staged changeset (`.githooks/pre-commit` entry point) |
| `workplan_status.py` | The only renderer of `designs/workplans/workplan_v6_progress.yaml`; feeds the SessionStart banner and `valoria-workplan-navigator` |
| `model_router.html` | UI for model routing decisions |
| `editorial_review/valoria-editorial-review.jsx` | React component for editorial review workflow |
| `sim_harness/` | **PROPOSED (ED-IN-0038), not wired into CI.** Gate-0 prototype of a generic, per-subsystem-adapter simulation/stress-test harness with canon-parameter resolution, depth-tiered probabilistic exploration, and mandatory triage-flag logging to `audit_registry.jsonl`. See `sim_harness/README.md` and `designs/audit/2026-07-12-simulation-test-harness-methodology/` |
