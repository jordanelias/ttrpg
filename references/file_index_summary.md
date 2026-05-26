# File Index Summary — DEPRECATED

This file is no longer the canonical file index for the Valoria repos.

**Use instead:** `references/valoria_index.sql` — committed text dump generated
by `tools/regenerate_file_index.py` from real `git ls-tree` walks. Runtime
SQLite database lives at `/home/claude/valoria.db` (never committed).

This stub is retained as a redirect note per the `<retirement>` protocol
(architecture V2.4+). The single sim-handoff line previously here is now
in `tests/sim/` directly and need not be indexed at this path.

Cut date: 2026-05-25.
Cut rationale: vestigial; superseded by the `valoria_index.sql` generation
pipeline (M6 partial-landed for editorial_ledger_summary; file_index moved
to the SQL track).
Audit reference: ecosystem audit 2026-05-25, Phase 0 item 0.5.
