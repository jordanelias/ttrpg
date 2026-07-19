# Retired tools

Not authoritative. History only. Do not import from or resume these.

## Retired 2026-07-15 (ED-IN-0068, apparatus consolidation — prune pass)

Four pure-function tools with **zero importers** anywhere (CI, hooks, skills, tests,
tools) and only self-test `__main__` blocks — confirmed dead by the apparatus registry
(`references/apparatus_registry.{yaml,md}`, orphan flag derived from `structure_audit`'s
import graph) and a repo-wide import grep. Retired here to keep them recoverable:

- `propagator.py` — exact-text propagation across compiled stage files (self-test only).
- `verify_cuts.py` — scan compiled output for cut-mechanic references (self-test only).
- `coverage_matrix.py` — 7-dimension coverage-matrix pure functions (self-test only).
  (Unrelated to the live `tests/coverage_matrix.md` data file or its size-threshold test,
  which use `ci_register_size_check.py`.)
- `find_references.py` — exact-occurrence search across file contents (self-test only).

To restore one, `git mv deprecated/tools/<name>.py tools/<name>.py` and re-add its
`tools/README.md` row.

Earlier retirals (2026-07-09 token-efficiency pass) are recorded in `CLAUDE.md` §8.
