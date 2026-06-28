# Deprecated skills

Skills retired from `skills/` but preserved for history.

- **valoria-orchestrator** — the session/bootstrap orchestrator from the retired `/home/claude`
  GraphQL harness (PAT management, `github_ops.py` downloads, `assert_bootstrap()`/`safe_commit`,
  `valoria_hooks.py`). Superseded by the Claude Code-native model (HANDOFF.md decision, 2026-06-24):
  enforcement now lives once in `tools/` and runs in CI + local hooks; the working tree is the source
  of truth, so session-start GitHub fetching and bespoke commit wrappers are no longer used. Kept
  here as a reference only — do not invoke; its scripts assume the dead sandbox.
