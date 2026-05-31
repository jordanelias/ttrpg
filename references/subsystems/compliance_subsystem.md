# Compliance Subsystem
**Status:** built · documented 2026-05-31 (Lane B, roadmap 2.3)
**Source:** `tools/compliance_check.py` (orchestrator) + `references/atomization_rules.yaml` (policy) + `tools/compliance_dryrun.py`

## Purpose
Enforces per-file **size / atomization policy** across the repo: governed files must stay under their token thresholds or be split ("atomized"). The policy is data-driven from `references/atomization_rules.yaml` — a top-to-bottom, **first-match** list of path rules. The orchestrator reports violations; since 2026-05-10 the bootstrap path is **print-only** (it surfaces violations in the Status Block, it does not halt).

## Public API (`tools/compliance_check.py`)
- `check_all(repo='ttrpg') -> list[Violation]` — full repo scan (used at bootstrap and session close).
- `check_all_cached(repo='ttrpg') -> list[Violation]` — the bootstrap-cached variant (avoids re-walking every session).
- `validate_commit(additions, deletions, ...) -> list[Violation]` — pre-commit check of proposed additions only.
- `_load_rules(repo)` — parses `atomization_rules.yaml`.
- `_match_rule(path, rules) -> dict | None` — **first** matching policy for a path (order in the YAML is significant).
- `_check_size(path, content, rule) -> Violation | None` — compares size to the rule's threshold; behaviour keys on `on_exceed`: `skip` → **no violation** (exemption), `flag_*` → warning Violation.
- `_check_index` / `_check_archive_pressure` — index-staleness and archive-year-split checks.
- `auto_fix(...)` / `apply_auto_fixes_to_additions(...)` — atomization helpers (dispatch to `atomizer`/`doc_index_gen`/`index_gen`, lazily imported).
- `report(violations) -> str` — Status-Block renderer.

## Policy file: `references/atomization_rules.yaml`
First-match list. Each rule: a path glob + a policy (threshold + `on_exceed`). To **exempt** a path from size enforcement, add a `skip` policy *above* the catch-all (this is how `research/**` and `tests/sim/**/session_activity_log.md` are exempted — see commit `c6465ea1`, 5.6). Order matters: a broad catch-all at the bottom; specific exemptions above it.

## Invocation
`check_all_cached()` runs at bootstrap (assert_bootstrap subsystems) and prints `[COMPLIANCE ✓]` / a violation list. `validate_commit()` is the pre-commit hook path. Manual: `python3 tools/compliance_check.py`.

## Gotchas
- **Print-only at bootstrap** since 2026-05-10 — a compliance violation does not block; it is advisory until separately enforced (or via CI register-size check).
- Dependencies (`atomizer`, `doc_index_gen`, `index_gen`, `github_ops`) are lazily imported and auto-fetched if missing in a fresh container (mirrors the `assert_bootstrap` auto-fetch).
- `_match_rule` is first-match — a misordered exemption (below the catch-all) silently never fires.
