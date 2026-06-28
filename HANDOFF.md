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
- 2026-06-28 — Finished the skill-port cleanup and CI/ergonomics hardening (this PR):
  retired `valoria-orchestrator` to `deprecated/skills/`; stripped `Model:`/`assert_bootstrap`/
  `g.read_files_graphql` boilerplate from the 13 active skills and converted them to working-tree
  reads; rewrote `valoria-vector-audit` Step 1 + skeleton to read the working tree; flipped the
  `ci_hooks_verifier.py` `/home/claude` warning to **blocking for `skills/`** (tools/ stays a
  warning pending the API→disk port); single-sourced the `coverage_matrix` threshold to
  `atomization_rules.yaml` (+ drift-guard test); refreshed CLAUDE.md's skills list. Retired the
  now-dead `check_skill_registry` in `broken_dependency_checker.py`.

## Next actions

- **(Deferred, real debt)** Triage the pre-existing debt the decoupled CI surfaces (report-only),
  then flip each to blocking: ED-citation violations (`validate_ed_citations`, ~722) and stale
  canonical docs (`freshness_gate` — the canonical_sha SHA-split, roadmap K-2 / LB-6).
- **(Deferred refactor)** Port the GitHub-API CI checks / analysis utilities off `/home/claude`
  onto working-tree reads: `freshness_gate.py`, `broken_dependency_checker.py`,
  `patch_propagation_checker.py`, `compliance_check.py`, `extract_*.py`, `valoria_collator.py`,
  `valoria_bulk_fix.py`. Once clean, flip the `tools/` scope of `ci_hooks_verifier.py` Check 4 to
  blocking too. (11 `tools/` files currently emit the report-only `/home/claude` warning.)
- **(Ergonomics, blocked)** Add a read-only Bash permissions allowlist to `.claude/settings.json`
  (git status/log/diff, `python tools/*` validators, `pytest tests/valoria`) — the auto-mode
  classifier blocked the agent from self-editing permission rules; add via `/fewer-permission-prompts`
  or by hand.
- Archive the dead home-dir scripts (`~/github_ops.py`, `~/valoria_hooks.py`, `~/_task_*.py`, …);
  the in-repo copies moved with the orchestrator to `deprecated/skills/`.
- Stale (non-gated) references to the old `skills/valoria-orchestrator/` path remain in
  `references/lane_assignments.yaml` and the regenerated `references/valoria_index.sql`; refresh
  when convenient.
