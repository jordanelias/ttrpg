# Handoff Subsystem
**Status:** built · documented 2026-05-31 (Lane B, roadmap 2.1)
**Source:** `skills/valoria-orchestrator/scripts/github_ops.py` (write/read/archive/conflicts/context) + `valoria_hooks.py` (validation/enforcement)

## Purpose
Handoffs are the authoritative resumption documents for parallel or paused workstreams. Each handoff is a YAML file at `handoffs/<id>.yaml` capturing what was done, what's next, which files matter, and which repo paths the workstream owns. Bootstrap surfaces all active handoffs in the Status Block; a new session resumes from one instead of starting cold. Handoffs are the coordination primitive that makes the multi-lane write-disjoint model safe (see `references/lane_assignments.yaml`).

## Public API (github_ops, `g`)
- `write_handoff(handoff: dict, extra_additions=None) -> oid` — validates schema (`_validate_handoff_schema`), self-commits to `handoffs/<id>.yaml` with message `[infrastructure] handoff write — <id>`, then prints a paste-ready RESUME block. Bypasses `pre_commit_gate` (it is its own authorized commit path). Idempotent on `id` (re-writing the same id overwrites that handoff).
- `read_all_handoffs() -> list[dict]` — every active handoff under `handoffs/`.
- `load_handoff_context(handoff_id: str) -> {handoff, files}` — returns the parsed handoff plus the contents of its `context_files` (the resume path fetches these into memory).
- `archive_handoff(handoff_id, extra_additions=None) -> oid` — moves a handoff to `archives/handoffs/` (git preserves the original).
- `check_handoff_conflicts(proposed_paths: list) -> list[(path, owner_handoff_id)]` — fnmatch of each proposed write-path against every active handoff's `owns` globs (`*` spans `/`). Returns the owning handoff per overlapping path. **Empty list = safe to write.** A match against your *own* handoff is expected; a match against any *other* handoff is a real conflict — do not write that path.
- `report_handoffs(handoffs=None)` / `print_resumption_block(handoff_id)` — Status-Block + resume-block renderers.

## Validation (valoria_hooks, `h`)
- `_validate_handoff_schema(handoff) -> list[str]` (in github_ops) — returns errors, does not raise. Required: `id`; `task` (dict with `skill`, `description`); `context_files` (non-empty list of `{path, depth∈{full,skeleton}, reason}`); `working_state` (dict with non-empty `next`); `last_commit`; `owns` (non-empty list).
- `validate_handoff(handoff)` / `require_handoff_on_close(handoff_id)` (hooks) — raising wrappers used at session close.

## Artifacts
- `handoffs/<id>.yaml` — active handoff (`id` must be a slug).
- `archives/handoffs/<id>.yaml` — archived handoffs.

## Invocation
Written/updated when a workstream pauses or hands off; read at every bootstrap (Status Block); referenced by `close_session_log(handoff_id=...)`, which refuses to close unless the named handoff exists and validates.

## Gotchas
- `context_files` and `working_state.next` and `owns` must be non-empty or the schema rejects the write.
- `depth` is `full` or `skeleton` only — `index` (the live fetch term) is **not** a valid handoff depth value.
- A `CollisionError` (HEAD moved) on the self-commit is the normal optimistic-concurrency signal: re-run and retry.
