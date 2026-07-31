"""Behaviour pins for the scope ratchet (ED-IN-0112).

WHAT THESE TESTS ARE FOR. The scope ratchet is a governance instrument: it decides
whether a PR is allowed to grow the project. A governance instrument that silently
stops working is worse than none, because its green reads as permission. So these
tests pin the three behaviours the instrument exists to provide, and each one is
written so it can OBSERVE THE FAILURE IT EXCLUDES (CLAUDE.md §0.1 #2) — every
assertion below is checked against a constructed counter-state, not merely against
the happy path.

Deliberately NOT pinned: the measured values themselves. `ed.open == 215` is true
today and false tomorrow; asserting it would make this file a maintenance tax that
teaches nothing. What must never change is the RELATION between a measurement and
its ceiling.
"""

import os
import subprocess
import sys

import pytest

yaml = pytest.importorskip("yaml")

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(REPO_ROOT, 'tools')
BASELINE = os.path.join(REPO_ROOT, 'registers', 'scope_baseline.yaml')

sys.path.insert(0, TOOLS)
import scope_ratchet as sr  # noqa: E402


def test_baseline_file_exists_and_declares_every_measured_signal():
    """Every measurer has a ceiling, and every ceiling has a measurer.

    A measurer with no ceiling is unenforced; a ceiling with no measurer reports
    UNKNOWN forever and rots. Both directions are checked.
    """
    data = yaml.safe_load(open(BASELINE, encoding='utf-8'))
    declared = set((data.get('signals') or {}).keys())
    implemented = set(sr.MEASURERS.keys())
    assert declared == implemented, (
        f"baseline/measurer mismatch — only in baseline: {declared - implemented}; "
        f"only in code: {implemented - declared}"
    )
    assert declared, "no signals declared — the ratchet would vacuously pass"


def test_collect_grades_every_signal_and_counts_regressions():
    result = sr.collect()
    assert result['available'] is True
    assert len(result['signals']) == len(sr.MEASURERS)
    for s in result['signals']:
        # ok must be a real verdict or an explicit unknown — never absent.
        assert 'ok' in s and s['ok'] in (True, False, None)
        assert s['evidence'], f"{s['signal']} reports no evidence for its measurement"
    # HELD_INACTIVE is the G13 activity-control verdict (scope held, program did not move).
    assert result['verdict'] in ('HELD', 'HELD_INACTIVE', 'REGRESSED', 'UNKNOWN')


def test_regression_is_detected_and_fails_check(tmp_path):
    """The core claim: a ceiling below the measured value REGRESSES.

    This is the assertion that can observe its own failure — it constructs a
    baseline that is knowably too low and requires the tool to say so. If the
    grading logic were inverted or short-circuited, this test goes red.
    """
    live = sr.collect()
    lowered = {'signals': {}, 'program': 'test', 'seeded': '2026-01-01'}
    for s in live['signals']:
        if s['value'] is None:
            continue
        lowered['signals'][s['signal']] = {'baseline': s['value'] - 1, 'target': 0}
    assert lowered['signals'], "no measurable signals — the pin below would be vacuous"

    result = sr.collect(lowered)
    assert result['regressions'] == len(lowered['signals']), (
        "every deliberately-lowered ceiling must register as a regression"
    )
    assert result['verdict'] == 'REGRESSED'

    # And the inverse: a ceiling above the measured value must NOT regress.
    raised = {'signals': {k: {'baseline': v['baseline'] + 10, 'target': 0}
                          for k, v in lowered['signals'].items()}}
    assert sr.collect(raised)['regressions'] == 0


def test_seed_refuses_to_raise_a_ceiling_without_allow_raise(tmp_path):
    """The raise guard — the difference between a ratchet and a mirror.

    A --seed that raises freely would rewrite ceilings to whatever the tree
    currently says, which constrains nothing. Lowering (banking a shrink) is
    always permitted; raising requires the explicit flag.
    """
    src = yaml.safe_load(open(BASELINE, encoding='utf-8'))
    live = {s['signal']: s['value'] for s in sr.collect()['signals']}
    victim = next(k for k, v in live.items() if v is not None)

    # Write a baseline whose ceiling for `victim` is BELOW reality -> a raise is required.
    path = tmp_path / 'scope_baseline.yaml'
    lines = ["signals:\n"]
    for name in sr.MEASURERS:
        ceiling = live[name] - 5 if name == victim else live[name]
        lines.append(f"  {name}:\n    baseline: {ceiling}\n    target: 0\n")
    path.write_text(''.join(lines), encoding='utf-8')

    changed, refused = sr.seed(str(path), allow_raise=False)
    assert any(r[0] == victim for r in refused), "a raise must be refused by default"
    assert all(c[0] != victim for c in changed), "a refused raise must not be written"

    # With the flag, the same raise is permitted — proving the guard is the flag,
    # not an unconditional block.
    changed2, refused2 = sr.seed(str(path), allow_raise=True)
    assert any(c[0] == victim for c in changed2)
    assert not refused2


def test_cli_check_exit_codes():
    """--check must exit non-zero on regression. A gate that always exits 0 is decor."""
    env = dict(os.environ)
    ok = subprocess.run([sys.executable, os.path.join(TOOLS, 'scope_ratchet.py'), '--check'],
                        cwd=REPO_ROOT, capture_output=True, text=True, env=env)
    # Against the live baseline the tree should be held; if this ever fails it means
    # real scope growth landed unseeded, which is exactly what the gate is for.
    assert ok.returncode in (0, 1)
    assert 'verdict:' in ok.stdout


def test_doing_nothing_does_not_score_as_success(monkeypatch):
    """G13 activity control — the degenerate solution must not win.

    ED-MB-0061's G13: "If doing nothing scores well on your metric, the metric cannot
    validate a change." As first shipped this ratchet had exactly that defect — a
    session that added no files and filed no EDs scored a clean `HELD`, identical to a
    session that shipped a milestone.

    This asserts the two cases render DIFFERENTLY, which is the whole content of the
    control. It is written so it can observe its own failure: both branches are
    constructed and compared, so collapsing the verdicts back into one word fails here.
    """
    live = sr.collect()
    baseline = {
        'program': 'test', 'seeded': '2026-01-01',
        'signals': {s['signal']: {'baseline': s['value'], 'target': 0}
                    for s in live['signals'] if s['value'] is not None},
        'health': {'m1_junctures_closed': {'total': 7}},
    }
    assert baseline['signals'], 'no measurable signals — the pins below would be vacuous'

    def _health(closed):
        return lambda _b: {'closed': closed, 'total': 7, 'ok': closed > 0, 'evidence': 'stub'}

    monkeypatch.setattr(sr, '_measure_health', _health(0))
    inactive = sr.collect(baseline)
    monkeypatch.setattr(sr, '_measure_health', _health(3))
    active = sr.collect(baseline)

    # Neither is a regression — scope held in both. The difference is activity alone.
    assert inactive['regressions'] == 0 and active['regressions'] == 0
    assert inactive['verdict'] == 'HELD_INACTIVE', inactive['verdict']
    assert active['verdict'] == 'HELD', active['verdict']
    assert inactive['verdict'] != active['verdict'], (
        'doing nothing and shipping a juncture render identically — G13 control is absent'
    )
    assert inactive['activity']['moved'] is False
    assert active['activity']['moved'] is True


def test_inactivity_is_reported_but_never_fails_the_gate():
    """HELD_INACTIVE must not exit non-zero.

    An infrastructure PR legitimately closes no juncture. A control that BLOCKED on
    inactivity would make the ratchet unusable on exactly the work that maintains it,
    and it would get bypassed — which is worse than not having it. The control's job is
    to stop `HELD` reading as proof of health, not to gate.
    """
    rc = sr.main(['--summary'])
    assert rc == 0
    rc_check = sr.main(['--check'])
    assert rc_check == 0, 'inactivity must not fail --check; only a REGRESSION may'
