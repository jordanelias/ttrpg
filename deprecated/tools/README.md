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

## Retired 2026-07-29 (Wave 4 mechanical sweep, OI-15/OI-16, ED-1082 precedent)

Confirmed orphaned by repo-wide grep across `.github/`, `.githooks/`, `.claude/`, `skills/`,
`tools/`, `registers/`, `CLAUDE.md` for each filename before moving (per-file greps recorded
in the Wave 4 sweep-lane execution notes) — every hit was either the file's own self-reference,
a generated-data mention (`incompleteness_data.js`, `INCOMPLETENESS.md`), or a plain-English
comment/docstring pointer in another tool, never an import or CI/hook invocation:

- `build_audit_registry_backfill.py` — one-time ledger-writer script; mentioned only in a
  docstring comment (`ci_audit_registry_check.py:71`) and a code comment
  (`build_apparatus_registry.py:313`), never imported or invoked.
- `geography/jsx_to_canonical.py` (`orphaned_no_cli` per the apparatus registry) — no importer,
  no CLI wiring, no test.
- `measure_stamp_false_positives.py` — mentioned only in a comment
  (`currency_consistency_check.py:91`), never imported or invoked.
- `observability/npc_audit_report_gen.py` (`orphaned_no_cli` per the apparatus registry) — no
  importer, no CLI wiring, no test.

## OI-16 (Wave 4) — `registry.py` NOT retired: HELD under a cross-program interlock

**`tools/registry.py` stays live.** The W4 sweep did retire it — zero production consumers were
re-verified by the ED-1082 grep precedent — and the retirement was **reversed during the W4 gate**,
before commit. It is recorded here because the reversal, not the retirement, is the disposition.

The concurrent `audit/2026-07-29-centralization-single-owner/` program (ED-IN-0103, merged PR #262)
declares a **BINDING** interlock on exactly this file (§0.1 row 1, "`tools/registry.py` retirement
race"): its W1.3 and §1 predicate 2 *make the facade real*, and it foresaw precisely this outcome —
"the ED-1082 grep-then-move precedent would find no consumers *precisely because W1 has not run*."
The zero-consumer finding is therefore evidence of the race, not evidence for retirement.

That interlock's declared executable form is a `[CSO]` blocking row in
`audit/2026-07-29-code-shape-open-items/04_execution_ledger.md` that W4 must read before its item 5.
**That row was never written** (grep for `[CSO]` in the ledger returned zero; the CSO pointer still
reads "W0 not yet started"), so nothing stopped the sweep — the interlock was protocol on a shared
surface, which that plan itself labels "stronger than prose but weaker than a gate." The plan's
intent is unambiguous even though its guard was absent, so W4 yields the file.

**Disposition:** OI-16's retirement half is **HELD**, routed to CSO W1.3 — that program either gives
the facade a consumer or retires it, and owns the call either way. W4 executed neither.

**Disposition of the companion OI-16 ask** (converged highest-leverage pointer artifacts,
`references/head_pointers.yaml` + `docs/REPO_MAP.md`): recorded **NOT-TO-BE-BUILT**. The role
those files would have played — a single human-readable index of "where is the current head for
X" — is already served by the `PROPOSALS.md`/`DECISIONS.md` observability family
(`tools/observability/obs_core.py` + `build_proposals.py`) plus `CURRENT.md` (CLAUDE.md §1,
the authoritative currency index). A third pointer surface would be a second owner of a role
one file already owns (CLAUDE.md §8 single-owner rule) — not built.

To restore one, `git mv deprecated/tools/<name>.py tools/<name>.py` (and
`deprecated/tools/test_registry.py` back to `tests/valoria/test_registry.py` for the facade)
and re-add its `tools/README.md` row.
