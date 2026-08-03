# Retired: `tests/hooks/` (2026-08-01, ED-IN-0119)

These 11 test modules were filed as **ED-IN-0045 item 1** on 2026-07-12 — "contain real pytest
code no CI job or local hook executes — wire in or explicitly retire" — and never actioned. This
is the retirement half of that decision.

## Why they are dead, not merely unwired

Every one of them imports `valoria_hooks` and/or `github_ops`, the retired orchestrator modules,
and several hardcode `sys.path.insert(0, '/home/claude')`. Neither module exists anywhere in the
live tree. Measured 2026-08-01: **10 of 12 failed at collection**; the other two
(`test_placeholder_names_gate.py`, `test_scope_vocabulary.py`) collect only because their imports
sit inside the test bodies, so all their cases error at run time instead. Zero of the 11 could
ever have passed.

Same profile, and the same disposition, as the tools retired to `deprecated/tools/` on 2026-07-09
and the `valoria-orchestrator` skill before them (ED-1082 precedent).

## What was kept, not retired

- `test_ed_citation_integrity.py` → **`tests/valoria/`**. 26 passing tests for
  `tools/validate_ed_citations.py`'s pure core, which that tool's own docstring points at. It was
  live the whole time and nothing ran it. It now runs in CI.
- `tests/registry/test_descriptor_registry.py` → **`tests/valoria/`** (1 passing test).

## Greps recorded before moving (ED-1082 procedure)

Searched `.github/workflows/`, `.githooks/`, `.claude/`, `tools/`, `skills/` and the whole tree for
each filename. Two live references existed, both prose, neither an invoker:

- `audit/2026-05-17-v18-integration/pass_3_handoff.md` mentions `test_placeholder_names_gate.py` as
  part of a historical session record — a snapshot, correctly left alone.
- `references/scope_vocabulary.md` advertised `test_scope_vocabulary.py` as a **"Drift guard …
  fails on any divergence"**. That claim was false: the test could not import, and nothing ran it.
  Real drift had accumulated behind it — the doc pins **11** commit scopes while `CLAUDE.md` §2
  lists **12** (`design` was added and no guard noticed). Replaced by a live guard at
  `tests/valoria/test_scope_vocabulary.py`; see ED-IN-0119.

## Do not resurrect

Reviving one means reviving `valoria_hooks`/`github_ops`, which are retired by ratified decision.
If the *behaviour* a file guarded is still wanted, write a new test against the live owner in
`tools/`, as was done for the scope vocabulary.
