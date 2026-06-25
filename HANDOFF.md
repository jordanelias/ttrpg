# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Pending

- _(nothing in flight)_

## Decisions

- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.

## Next actions

- After the migration PR merges, finish the deferred skill-port cleanup (strip `Model:`/
  `assert_bootstrap`/`g.read_files_graphql` boilerplate from the remaining `skills/*/SKILL.md`,
  rewrite `valoria-vector-audit` to read the working tree), then flip the `/home/claude`
  warning in `ci_hooks_verifier.py` to blocking.
- Archive the dead home-dir scripts (`~/github_ops.py`, `~/valoria_hooks.py`, `~/_task_*.py`, …).
- Triage the pre-existing debt the decoupled CI now surfaces (report-only), then flip each to blocking:
  ED-citation violations (`validate_ed_citations`, ~722) and stale canonical docs
  (`freshness_gate` — the canonical_sha SHA-split, roadmap K-2 / LB-6).
- Consolidate the `coverage_matrix` size threshold (currently in BOTH
  `tools/ci_register_size_check.py` and `references/atomization_rules.yaml`, set to 10000 in each)
  into a single source.
