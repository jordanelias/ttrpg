# CI Subsystem
**Status:** built but **non-enforcing** (branch protection disabled, D0) · documented 2026-05-31 (Lane B, roadmap 2.6)
**Source:** `.github/workflows/valoria-ci.yml` + `tools/ci_*.py` (`ci_co_file_checker`, `ci_editorial_checker`, `ci_hooks_verifier`, `ci_register_size_check`)

## Purpose
A GitHub Actions workflow that mirrors selected local hook gates **outside** Claude, on push/PR to `main`. It is the external counterpart to the in-process `valoria_hooks` gates. Because branch protection is disabled (roadmap D0), CI runs are **advisory/post-hoc** — there is no required-status-check gate, so a failing run does not block a commit that already landed. CI is therefore a detection mirror, not an enforcement wall, in the current configuration.

## Workflow: `.github/workflows/valoria-ci.yml`
Triggers on push + pull_request to `main`; concurrency-cancels rapid runs. **Eight jobs** (syntax-check is the foundation the rest depend on):
- **syntax-check** — `py_compile` every CI + repo tool (`ci_*`, `broken_dependency_checker`, `patch_propagation_checker`, `freshness_gate`, `compliance_check`, `atomizer`, `doc_index_gen`, `index_gen`).
- **register-sizes** — `ci_register_size_check.py` (external size gate).
- **hooks-verifier** — `ci_hooks_verifier.py` (enforcement architecture intact).
- **co-file-check** — `ci_co_file_checker.py` (co-file requirements).
- **editorial-check** — `ci_editorial_checker.py` (editorial-path markers).
- **integrity** — repository integrity checks (job name "Repository Integrity").
- **compliance-check** — delegates to `compliance_check.py` (see the Compliance subsystem doc).
- **skills-lint** — skills lint (job name "Skills Lint").

## CI scripts (`tools/ci_*.py`)
- `ci_register_size_check.py` — fails if any governed file exceeds its token threshold. The external "cannot be bypassed" size gate (in spirit — see drift note).
- `ci_co_file_checker.py` — verifies co-file requirements from the CI side: design-doc change → `canonical_sources.yaml`; patch content → `patch_register_active.yaml`; sim output → `coverage_matrix.md`; mechanical-value change → params file. Uses `git diff` against the GitHub event context (push/PR/squash-merge aware).
- `ci_editorial_checker.py` — commits touching editorial paths (`designs/npcs/`, `designs/world/`, `arcs/simulated/`, `canon/03_`) must carry `[EDITORIAL:` / `[PROVISIONAL:` / `[EDITORIAL GATE]` markers for substantive content (>200 chars; `_skeleton.md` exempt).
- `ci_hooks_verifier.py` — verifies the enforcement architecture is intact: `valoria_hooks.py` has the required functions (`assert_bootstrap`, `task_gate`, `editorial_gate`, `pre_commit_gate`, `commit_message_gate`, `propose_mechanic_gate`, `context_gate`, `safe_commit`); the orchestrator SKILL imports hooks + calls `assert_bootstrap`; uses `h.safe_commit` not `g.atomic_commit` directly; redundant stripped blocks have not returned; skills are under their token limits.

## Invocation
Automatic on push/PR to `main` (GitHub-hosted runners). Locally the `ci_*` scripts fall back to `HEAD~1` diffs.

## Drift findings (flag for Jordan — architecture is Jordan-applied)
- **`[DRIFT: architecture <open_items> vs repo]`** — architecture V2.5 lists *"CI external check (Level 5) not yet implemented"*. In fact `valoria-ci.yml` **exists and runs** the jobs above. The accurate state is: the workflow is **built but non-enforcing** (no branch protection / required-status-check, per D0), not "not implemented." The architecture open-item should be corrected to reflect built-but-advisory.
- **`[DRIFT: roadmap 2.6 count]`** — roadmap 2.6 says "4 ci_*.py + **2** workflow yml". Only **one** workflow (`valoria-ci.yml`) is present under `.github/workflows/`. Confirm whether a second was planned/removed.
- **`[DRIFT: ci_register_size_check.py thresholds]`** — its `THRESHOLDS` dict still keys on the **deprecated** pre-cutover files (`canon/editorial_ledger.yaml`, `canon/editorial_ledger_summary.yaml`, `references/file_index_summary.md`, `session_log_archive.md`). Post the 2026-05-28 JSONL/SQL cutover these are retired; the CI size gate's keys are stale and should be repointed to `registers/editorial_ledger.jsonl` / `references/valoria_index.sql` / the per-session-log + handoff/archive paths. (Lane B follow-up; pairs with 1.10b.)

## Gotchas
- With branch protection off, CI is informational — do not treat a green CI as a merge gate; the local hooks are the live enforcement surface.
