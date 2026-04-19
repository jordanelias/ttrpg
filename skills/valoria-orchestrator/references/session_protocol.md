# Session Protocol (Per-Session Model)

## Overview

Each concurrent Claude session operates on its own session log file, scoped
by a user-declared tag (e.g. `infrastructure`, `godot`, `design`). A shared
index file tracks active sessions. The legacy `session_log_current.md` is
auto-generated as a pointer to the index — direct writes are blocked.

## Start

1. Bootstrap `github_ops.py` and `valoria_hooks.py` from repo.
2. `read_files_graphql()` fetches session-critical files including `session_logs/index.md`.
3. `h.assert_bootstrap(scope)` — sets session scope, prints active sessions,
   warns if another session shares the same scope.
4. `g.start_session_log(scope, token)` — creates `session_logs/<scope>_<token>.md`,
   updates index, auto-generates `session_log_current.md` pointer.
5. Report status. Stop. Wait for Jordan to verify and send task.

## During Session

- Scope → Plan → Execute → Verify on every task.
- Checkpoint after each skill execution.
- Per-session log: `g.update_session_log(scope, token, content)`.
- If context filling: run Session Close immediately.
- Never hold uncommitted output across a context reset.

## Close

1. Write final YAML block via `g.close_session_log(scope, token, content)`.
   This archives the session log to `archives/session/`, removes from index,
   updates `session_log_current.md` pointer, and deletes the active log file.
2. `h.close_checkpoint()` if a checkpoint was written.
3. Atomic — all in one commit.

## File Layout

```
session_logs/
  index.md                        — auto-generated list of active sessions
  <scope>_<token>.md              — per-session log (active)
archives/session/
  session_log_<scope>_<date>_<token>.md  — archived session logs
session_log_current.md            — auto-generated pointer (DO NOT EDIT)
```

## Scope Tags

`infrastructure` · `godot` · `editorial` · `design` · `simulation` · `audit` · `general`

User declares scope after "bootstrap" (e.g. `bootstrap infrastructure`).
Default is `general` if omitted.

## Write Policy

- Per-session log: single writer (the owning session). Free to update anytime.
- `session_logs/index.md`: only written by `start_session_log()` and `close_session_log()`.
- `session_log_current.md`: auto-generated only. Direct writes blocked by `pre_commit_gate`.

## YAML Block Schema (per-session close)

```yaml
session_id: <scope>_<token>
session_close: YYYY-MM-DD HH:mm
scope: <scope>
phase: Phase N (description)
status: CLOSED
last_stage: [stage name]
next_action:
  skill: name
  input_file: filename
  parameters: {}
blockers: []
```
