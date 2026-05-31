# Checkpoint Subsystem
**Status:** built · documented 2026-05-31 (Lane B, roadmap 2.2)
**Source:** `skills/valoria-orchestrator/scripts/valoria_hooks.py` (`h`) — `CHECKPOINT_PATH`, `write_checkpoint`, `close_checkpoint`, `read_active_checkpoint`, `prompt_resume_from_checkpoint`, `context_gate`

## Purpose
A checkpoint is a single in-flight snapshot of the *current* session's state, written to `canon/session_checkpoint.md` so that if the session is interrupted (or hits the context ceiling) a fresh session can resume from it rather than starting cold. Distinct from a handoff: a handoff is a durable, named, per-workstream resumption doc; a checkpoint is the one live "where this session is right now" marker, gated by context pressure.

## Public API (`h`)
- `write_checkpoint(task_scope, files_verified=[], completed=[], pending=[], decisions=[], open_questions=[], next_actions=[], commits=[], narrative="", sim_ledger=False) -> oid` — writes YAML-frontmatter + markdown to `CHECKPOINT_PATH` with `status: active`. Commits **directly via `atomic_commit`** (not `safe_commit`) because checkpoints are session metadata, not task output, and `task_gate` may not have run. Requires bootstrap first.
- `close_checkpoint() -> oid | None` — flips frontmatter `status` to `closed` (adds `closed_at`). Called at session close after the final session-log commit. No-op if absent or already closed.
- `read_active_checkpoint() -> dict | None` — parsed frontmatter iff `status == active`.
- `prompt_resume_from_checkpoint() -> dict | None` — bootstrap helper; prints the active checkpoint's summary and returns it. Does **not** auto-resume — Jordan confirms resume vs. fresh start.

## Context gate (the trigger)
`context_gate()` estimates usage (`fetch bytes / 4 + system overhead`) against three tiers — values are calibrated for the **1M-token window**:
- `CONTEXT_SOFT` = 600_000 (60%) — warn: plan a handoff, write a draft checkpoint at the next clean stop.
- `CONTEXT_CHECKPOINT_HARD` = 750_000 (75%) — **raises** unless `write_checkpoint()` has been called this session.
- `CONTEXT_HARD` = 900_000 (90%) — **raises** unconditionally; session-close protocol only.
Call at session start and every ~10 tool calls.

## Artifact / schema
`canon/session_checkpoint.md` — YAML frontmatter (`schema_version`, `session_token`, `created_at`, `status` ∈ active|closed|stale, `task_scope`, `context_tokens_at_checkpoint`, `files_verified`, `commits_this_session`, `completed`, `pending`, `decisions_made`, `open_questions`, `next_bootstrap_actions`) followed by a human-readable narrative body.

## Gotchas
- The `context_gate` token estimate is derived from the **session fetch cache** (bytes fetched ÷ 4 + overhead), not the conversation window — on a 1M model it can read high if a large file (e.g. the editorial ledger) was fetched, while the actual conversation context is far lower. Treat the number as a fetch-budget proxy, not a window gauge.
- Checkpoint commits use a dedicated `[infrastructure]` scope and the direct `atomic_commit` path — they are not routed through `safe_commit`/`task_gate`.
