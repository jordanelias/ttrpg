# Per-Session-Log Subsystem

> **⚠️ RETIRED (2026-06-30).** This documents the `valoria-orchestrator` GraphQL/`/home/claude` session
> driver, now retired to `deprecated/skills/`. The Public API below is **not live — do not call it.**
> There is no session-log machinery in use; continuity lives in `HANDOFF.md` + git history. The
> `session_logs/` and `session_log_current.md` files in the tree are inert. Kept for historical
> reference. Tracked by ED-1054.

**Status:** RETIRED — superseded by HANDOFF.md + git (was: built/D5, documented 2026-05-31, Lane B, roadmap 2.5)
**Source:** `skills/valoria-orchestrator/scripts/github_ops.py` (`g`) — `start_session_log`, `update_session_log`, `close_session_log`, `safe_session_close` (legacy), `SESSION_SCOPES`, `_generate_pointer`

## Purpose
Tracks active sessions so concurrent/sequential work is legible. The **per-session** model (D5) gives each session its own log file under `session_logs/`, listed in an auto-generated index, with `session_log_current.md` regenerated as a pointer to the active set. The older **single-file** model (`safe_session_close`) wrote one `session_log_current.md` resumption block and archived the prior one; it is legacy and slated for retirement once D5 is fully migrated.

## Public API (`g`)
### Per-session (current)
- `start_session_log(scope, token) -> log_path` — creates `session_logs/<scope>_<token>.md` (frontmatter: `session_id`, `scope`, `token`, `started_at`, `status: ACTIVE`), appends an entry to `session_logs/index.md`, regenerates `session_log_current.md` (pointer via `_generate_pointer`). Commits `[infrastructure] Session start — scope: <scope>, token: <token>`.
- `update_session_log(scope, token, content) -> oid` — appends progress to the per-session log.
- `close_session_log(scope, token, final_log_content, handoff_id=None, extra_additions=None) -> oid` — archives to `archives/session/session_log_<scope>_<date>_<token>.md`, removes the entry from `session_logs/index.md`, regenerates the pointer, deletes `session_logs/<scope>_<token>.md`. If `handoff_id` is given it **must** resolve to an existing, schema-valid `handoffs/<id>.yaml` or the close is blocked. Required fields in `final_log_content`: `session_id`, `session_close`, `status`, `last_stage`, `next_action`, `blockers`.

### Legacy (single-file)
- `safe_session_close(new_session_log, bootstrap_session_log, extra_additions=None, message=...) -> oid` — writes `session_log_current.md` (capped at `TOKEN_THRESHOLDS['session_log_current.md']` = 2_000 tokens; resumption-block YAML only) and archives the prior content to `archives/session/session_log_archive_part_7.md`. Rejects prose (`## ` headers) and duplicate closes (same `session_id`). Required fields: `session_id`, `session_close`, `phase`, `status`, `last_stage`, `next_action`, `blockers`.

## Scopes
`SESSION_SCOPES = {infrastructure, godot, editorial, design, simulation, audit, general}`. (Note: this set differs from `TASK_REQUIRED_FILES` keys and the `COMMIT_FORMAT` scopes — the three are disjoint; unification is roadmap D6 / Lane B item 5.8.)

## Artifacts
- `session_logs/<scope>_<token>.md` — active per-session log.
- `session_logs/index.md` — active-session index (size-capped 2_000 tokens).
- `session_log_current.md` — auto-generated pointer (trusted-caller restricted, capped 2_000 tokens; resumption-block only, no prose).
- `archives/session/session_log_<scope>_<date>_<token>.md` — archived per-session logs.
- `archives/session/session_log_archive_part_7.md` — legacy single-file archive.

## Gotchas
- `session_log_current.md` is both **trusted-caller restricted** (only these authorized paths may write it) and **size-capped** — it must be a pure resumption block, never a prose summary.
- `close_session_log` with a `handoff_id` is the clean close: it ties the archived log to the durable handoff. Prefer it over `safe_session_close`.
- Legacy `safe_session_close` retirement is pending the D5 migration (audit Phase 3 item 3.4).
