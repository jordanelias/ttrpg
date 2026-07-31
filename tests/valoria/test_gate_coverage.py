"""Guard for tools/ci_gate_coverage.py (ED-IN-0098).

The tool exists because the W4 gate ran `tests/valoria` and forgot `engine/tests` (a separate
blocking job, `sim-regression`) and `tests/contracts` (also in `unit-tests`). Its one job is to
never let a pytest root that CI runs go unlisted, so that is what these tests pin — including the
count, so a root being ADDED to CI and silently missed here fails rather than passes.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ci_gate_coverage as g  # noqa: E402

# MEASURED 2026-07-30 against .github/workflows/valoria-ci.yml. If CI gains a pytest root, this
# set must grow in the SAME commit — that is the regression this pin exists to force.
EXPECTED_ROOTS = {'tests/valoria', 'tests/contracts', 'engine/tests'}


def test_workflow_parses_into_jobs():
    jobs = g.jobs()
    assert len(jobs) > 20, f'only parsed {len(jobs)} jobs — the workflow format may have changed'
    ids = {j['id'] for j in jobs}
    for required in ('unit-tests', 'sim-regression', 'compliance-check', 'ed-citations'):
        assert required in ids, f'known CI job {required!r} not parsed'


def test_every_ci_pytest_root_is_discovered():
    """THE regression: the two roots the W4 gate forgot must both be found."""
    roots = {r for j in g.jobs() for r in j['pytest_roots']}
    assert roots == EXPECTED_ROOTS, (
        f'CI pytest roots changed: found {sorted(roots)}, pinned {sorted(EXPECTED_ROOTS)}. If CI '
        f'legitimately gained or lost a root, update EXPECTED_ROOTS in this commit and say so — '
        f'do not delete the assertion.')


def test_engine_tests_is_recognised_as_blocking():
    """sim-regression has no continue-on-error, so a local gate skipping it is skipping a gate."""
    sim = next(j for j in g.jobs() if j['id'] == 'sim-regression')
    assert sim['blocking'] is True
    assert 'engine/tests' in sim['pytest_roots']


def test_continue_on_error_jobs_are_classified_non_blocking():
    """Precision: report-only jobs must not be presented as unbypassable gates."""
    jobs = g.jobs()
    advisory = [j['id'] for j in jobs if not j['blocking']]
    assert advisory, 'no advisory jobs detected — continue-on-error parsing is broken'
    # currency-consistency is continue-on-error in the workflow (CLAUDE.md §8 report-only tier).
    assert 'currency-consistency' in advisory


def test_every_discovered_root_actually_exists_on_disk():
    """A root parsed out of YAML but absent from the tree would send a session chasing nothing."""
    checked = 0
    for r in {r for j in g.jobs() for r in j['pytest_roots']}:
        assert os.path.isdir(os.path.join(ROOT, r)) or os.path.isfile(os.path.join(ROOT, r)), r
        checked += 1
    assert checked == len(EXPECTED_ROOTS) == 3, f'checked {checked} roots'


def test_base_distance_reports_an_integer_or_none():
    d = g.base_distance('origin/main')
    assert d is None or (isinstance(d[0], int) and d[0] >= 0)
    # An unknown ref must degrade to None, not crash a pre-commit advisory.
    assert g.base_distance('definitely/not/a/ref') is None


def test_tool_is_report_only():
    assert g.main(['--base', 'HEAD']) == 0
