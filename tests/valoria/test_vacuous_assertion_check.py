"""Guard for tools/ci_vacuous_assertion_check.py (ED-IN-0098).

A detector is only worth having if it catches the defects that motivated it, so the two primary
tests are FIXTURES OF THE REAL ASSERTIONS that slipped through, both from W4 (ED-IN-0097):

    assert sa.ci_common.has_main_guard is not None   # a function is never None      -> V3
    assert st['drift'] >= 0                          # an integer file count         -> S1

The second was written by the same session that had just fixed the first, citing §0.1 #2 in its
own commit. That is why a tool exists instead of a reminder.

Equally important: the precision tests. A vacuity detector that flags working assertions gets
switched off, and a switched-off guard is worse than none because the repo still believes it is
covered. So there are as many "must NOT flag" cases below as "must flag" ones.
"""
import os
import sys
import textwrap

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ci_vacuous_assertion_check as v  # noqa: E402


def _scan(src, tmp_path, name='probe.py'):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return v.scan_file(str(p))


# ─────────────────────────── must FLAG: the real historical defects ───────────────────────────

def test_catches_the_has_main_guard_shape(tmp_path):
    """W4's first vacuous assertion: `is not None` on a module-level def."""
    provable, _ = _scan('''
        def has_main_guard(tree):
            return True

        def test_x():
            assert has_main_guard is not None
    ''', tmp_path)
    assert [f['rule'] for f in provable] == ['V3'], provable
    assert 'never None' in provable[0]['why']


def test_catches_the_drift_count_shape(tmp_path):
    """W4's second vacuous assertion, in the heuristic tier (types are not statically known)."""
    _, suspicious = _scan('''
        def test_x():
            st = {'drift': 3}
            assert st['drift'] >= 0
    ''', tmp_path)
    assert [f['rule'] for f in suspicious] == ['S1'], suspicious


@pytest.mark.parametrize('line,rule', [
    ('assert True', 'V1'),
    ('assert 1', 'V1'),
    ('assert "nonempty"', 'V1'),
    ('assert [0]', 'V1'),
    ('assert len(x) >= 0', 'V2'),
    ('assert len(x) > -1', 'V2'),
    ('assert isinstance(x, object)', 'V4'),
    ('assert 1 == 1', 'V5'),
])
def test_provable_rules_fire(line, rule, tmp_path):
    provable, _ = _scan(f'''
        def test_x():
            x = []
            {line}
    ''', tmp_path)
    assert [f['rule'] for f in provable] == [rule], (line, provable)


# ───────────────────── must NOT flag: precision (a noisy guard gets disabled) ─────────────────

@pytest.mark.parametrize('line', [
    'assert len(x) == 1',            # a real length claim
    'assert len(x) > 0',             # non-empty is falsifiable
    'assert len(x) >= 2',            # a real floor
    'assert x == 1',
    'assert not x',
    'assert False',                  # always fails — wrong, but NOT vacuous
    'assert 0',                      # ditto
    'assert isinstance(x, list)',    # a real type claim
    'assert 1 == 2',                 # false, not vacuous
    'assert x is None',              # the opposite direction is a real claim
])
def test_legitimate_assertions_are_not_flagged(line, tmp_path):
    provable, suspicious = _scan(f'''
        def test_x():
            x = []
            {line}
    ''', tmp_path)
    assert provable == [], (line, provable)
    assert suspicious == [], (line, suspicious)


def test_is_not_none_on_a_call_result_is_not_flagged(tmp_path):
    """`assert compute() is not None` is a genuine check — a call can return None."""
    provable, suspicious = _scan('''
        def test_x():
            assert compute() is not None
    ''', tmp_path)
    assert provable == [] and suspicious == []


def test_local_variable_is_not_none_is_only_suspicious_never_provable(tmp_path):
    """A local bound from a call MIGHT be None — advisory at most, never a hard finding."""
    provable, suspicious = _scan('''
        def test_x():
            y = compute()
            assert y is not None
    ''', tmp_path)
    assert provable == []
    assert [f['rule'] for f in suspicious] == ['S2']


# ─────────────────────────────── the live corpus baseline ────────────────────────────────────

def test_live_corpus_has_no_provably_vacuous_assertions():
    """The repo-wide invariant, and the reason the PROVABLE tier could be promoted to blocking.

    MEASURED 2026-07-30: 0 across 132 files in tests/valoria + engine/tests, after ED-IN-0098
    fixed the three known instances (two from W4 plus
    engine/tests/test_accounting_accord_drift_probe.py, which this very tool surfaced). If this
    goes red, a new one landed — fix the assertion, do not relax the test.
    """
    provable = []
    n = 0
    for f in v.iter_py(list(v.DEFAULT_ROOTS)):
        n += 1
        p, _ = v.scan_file(f)
        provable += p
    assert n > 100, f'only scanned {n} files — the default roots may have moved'
    assert provable == [], (
        'provably-vacuous assertion(s) landed:\n' +
        '\n'.join(f"  {f['file']}:{f['line']} [{f['rule']}] {f['source']}" for f in provable))


def test_tool_is_report_only():
    """Exit 0 even when findings exist — promoting to blocking is Jordan's call."""
    assert v.main(['--path', 'tests/valoria/test_vacuous_assertion_check.py']) == 0
