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
