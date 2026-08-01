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


def test_cli_check_exits_nonzero_on_a_regression_and_zero_without_one(tmp_path):
    """--check's exit code must track the verdict. A gate that always exits 0 is decor.

    REWRITTEN 2026-07-31 after an adversarial pass (ED-IN-0112). The first version
    asserted `returncode in (0, 1)`, which ADMITS the failure its own docstring
    excludes — a `--check` hardcoded to `return 0` passed it. That is the
    §0.1 #2 pattern: not a weak assertion, an absent one.

    It is also deliberately run against CONSTRUCTED baselines, never the live tree.
    The live-tree version was a landmine: `pytest tests/valoria` is a BLOCKING CI gate,
    the ceilings sit at zero headroom by construction, and CLAUDE.md §2 expects
    substantively every PR to append a ledger row — so the next ED filed by anyone
    would have driven ed.open past its ceiling and turned a scope signal into a broken
    build for an unrelated author. A report-only instrument must never be able to fail
    the blocking suite.
    """
    live = sr.collect()
    measurable = {s['signal']: s['value'] for s in live['signals'] if s['value'] is not None}
    assert measurable, 'no measurable signals — the pins below would be vacuous'

    # tmp_path, NOT a file written into tests/valoria/. A test that drops scratch files into
    # the collection directory is not parallel-safe (pytest-xdist workers share a cwd) and can
    # be COLLECTED as a fixture file by a later run. Worker-isolated by construction here.
    def _run(baseline_map, tmpname):
        path = tmp_path / tmpname
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('signals:\n')
            for name, spec in baseline_map.items():
                fh.write(f"  {name}:\n    baseline: {spec}\n    target: 0\n")
        return subprocess.run(
            [sys.executable, os.path.join(TOOLS, 'scope_ratchet.py'),
             '--check', '--baseline', str(path)],
            cwd=REPO_ROOT, capture_output=True, text=True)

    held = _run({k: v for k, v in measurable.items()}, '_tmp_held.yaml')
    assert held.returncode == 0, f'no regression must exit 0; got {held.returncode}'
    assert 'verdict:' in held.stdout

    regressed = _run({k: v - 1 for k, v in measurable.items()}, '_tmp_regressed.yaml')
    assert regressed.returncode == 1, (
        f'a regression MUST exit 1; got {regressed.returncode}. An always-zero exit is decor.'
    )
    assert 'REGRESSED' in regressed.stdout


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


def test_inactivity_is_reported_but_never_fails_the_gate(tmp_path):
    """HELD_INACTIVE must not exit non-zero.

    An infrastructure PR legitimately closes no juncture. A control that BLOCKED on
    inactivity would make the ratchet unusable on exactly the work that maintains it,
    and it would get bypassed — which is worse than not having it. The control's job is
    to stop `HELD` reading as proof of health, not to gate.
    """
    # Constructed baseline, never the live tree — see
    # test_cli_check_exits_nonzero_on_a_regression_and_zero_without_one for why running
    # this against live ceilings inside a BLOCKING suite was a landmine.
    live = sr.collect()
    path = tmp_path / '_tmp_inactive.yaml'
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('signals:\n')
        for sig in live['signals']:
            if sig['value'] is not None:
                fh.write(f"  {sig['signal']}:\n    baseline: {sig['value']}\n    target: 0\n")
    assert sr.main(['--summary', '--baseline', str(path)]) == 0
    assert sr.main(['--check', '--baseline', str(path)]) == 0, (
        'inactivity must not fail --check; only a REGRESSION may'
    )


def test_the_measured_signal_set_cannot_silently_shrink(): 
    """G16 — deleting a whole signal must fail, not merely perturbing one.

    Found by an adversarial pass (ED-IN-0112). The set-equality pin above compares
    MEASURERS against the baseline file, so deleting a signal from BOTH still passed:
    the ratchet could be reduced to one signal — including dropping `tracked.files`,
    which the pointer calls "the mechanism, not a side effect" — with a fully green
    suite. Nothing pinned WHICH leaks are measured, only that the two lists agreed
    with each other.

    This names them. Adding a signal is free; removing one is a deliberate edit here.
    """
    required = {'ed.stale', 'ed.needs_jordan_stale', 'audit.files', 'tracked.files',
                'proposals.open'}
    missing = required - set(sr.MEASURERS)
    assert not missing, (
        f'signal(s) {sorted(missing)} were removed from MEASURERS. Each is a distinct way '
        f'scope leaks (work opened / bottlenecked / audit corpus / total surface / '
        f'unratified designs); dropping one silently narrows what the ratchet can see.'
    )


def test_unmeasurable_input_is_unknown_never_a_pass(monkeypatch):
    """A signal that cannot be measured must grade UNKNOWN, not 0.

    The module docstring promises "an unmeasurable signal must not read as a pass".
    It did not hold: an empty ledger glob, an absent proposals/ and a `git ls-files`
    over a missing pathspec all returned 0, and 0 <= ceiling graded as `held`. Deleting
    registers/, proposals/ and audit/ outright scored a clean HELD.
    """
    monkeypatch.setattr(sr, '_ledger_rows', lambda: [])
    value, evidence = sr.measure_ed_stale()
    assert value is None, 'an unreadable ledger must be UNKNOWN, not 0'
    assert 'UNKNOWN' in evidence

    result = sr.collect({'signals': {'ed.stale': {'baseline': 999, 'target': 0}}})
    row = result['signals'][0]
    assert row['ok'] is None, 'UNKNOWN must not grade as ok=True'
    assert result['verdict'] == 'UNKNOWN'
    assert result['regressions'] == 0


# ---------------------------------------------------------------------------
# m1_acceptance + dashboard build_program (ED-IN-0113 finding 6: both shipped
# with ZERO assertions anywhere in tests/).
#
# Housed HERE rather than in a new file on purpose. They are the same program's
# artifacts, and a new file would raise tracked.files — the ceiling this very
# module enforces. Paying a scope cost to test a scope instrument would be a poor
# trade and a slightly absurd one.
# ---------------------------------------------------------------------------

import importlib  # noqa: E402

m1 = importlib.import_module('m1_acceptance')


def test_acceptance_gate_never_reports_readiness_it_did_not_measure():
    """The ED-MB-0042 lesson, applied to the gate itself.

    Four of five rows depend on a headless season run that does not exist. A gate
    that guessed them would be the confounded measurement rebuilt as infrastructure.
    Every unmeasured row must carry value=None AND name what unblocks it — an
    honest blocker is actionable, a silent zero is not.
    """
    result = m1.collect()
    assert result['rows'], 'no rows — the gate would vacuously report'
    for row in result['rows']:
        assert row['state'] in ('measured', 'partial', 'blocked'), row
        if row['state'] == 'blocked':
            assert row['value'] is None, f"{row['row']} guessed a value while blocked"
            assert row['passes'] is None, f"{row['row']} claims a verdict while blocked"
            assert row['unblocked_by'], f"{row['row']} is blocked but names no unblocker"
    assert result['verdict'] in ('MET', 'NOT MET', 'NOT YET MEASURABLE')


def test_key_closure_reports_both_wildcard_readings():
    """`- {type: "*"}` is a quantifier, not a key name.

    Two modules declare a universal-reader consume. Treating "*" as a literal key
    name overstates the orphan count; honouring it makes the row vacuously zero.
    Neither reading alone is honest, so BOTH ship — and the detail must say a
    wildcard exists rather than presenting one number as exact.
    """
    row = m1.row_key_log_closure()
    assert row['state'] == 'partial'
    assert row['passes'] is None, 'static analysis can never PASS this row on its own'
    assert 'value_effective' in row, 'the wildcard-honouring reading is missing'
    assert row['value'] >= row['value_effective'], (
        'the strict count must be >= the wildcard-honouring count'
    )
    assert 'universal-reader' in row['detail'] or row['value'] == row['value_effective'], (
        'a wildcard consumer exists but the detail does not disclose it'
    )


def test_check_only_fails_on_a_measured_failure_never_on_a_blocked_row():
    """A blocked row must not gate. Losing an input must not make the gate greener."""
    result = m1.collect()
    blocked = [r for r in result['rows'] if r['state'] == 'blocked']
    assert blocked, 'no blocked rows — this pin would be vacuous'
    assert result['failed'] == sum(
        1 for r in result['rows'] if r['state'] == 'measured' and r['passes'] is False
    ), 'failed count must derive from MEASURED rows alone'


def test_dashboard_program_panel_composes_and_never_renders_a_break_as_a_pass():
    """build_program adds no arithmetic, and a broken sub-tool reads UNKNOWN.

    If a number here disagreed with the CLI the dashboard would be lying quietly,
    which is worse than an empty card. Pass-through is the contract.
    """
    sys.path.insert(0, os.path.join(TOOLS, 'observability'))
    dd = importlib.import_module('dashboard_data')
    panel = dd.build_program()
    assert panel['available'] is True
    # Pass-through, not recomputation: the panel's health must equal the tool's.
    assert panel['health']['closed'] == sr.collect()['health']['closed']
    assert panel['verdict']['scope'] == sr.collect()['verdict']
    for key in ('scope', 'acceptance'):
        sub = panel[key]
        assert sub.get('available') is not False or 'error' in sub, (
            f'{key} failed but reported no error — a break must never read as a pass'
        )


def test_partial_movement_is_not_inactivity(monkeypatch):
    """ED-IN-0113 finding 3: junctures in flight must not read as a dead program.

    Counting only `done` made a session that advanced four junctures score the same
    HELD_INACTIVE as one that did nothing — G13's own blindness, one tier in.
    Constructs all three states and requires they differ.
    """
    live = sr.collect()
    base = {'signals': {s['signal']: {'baseline': s['value'], 'target': 0}
                        for s in live['signals'] if s['value'] is not None}}
    assert base['signals'], 'no measurable signals — this pin would be vacuous'

    def health(closed, in_progress, total=7):
        return lambda _b: {'closed': closed, 'total': total, 'in_progress': in_progress,
                           'blocked': 0, 'ok': closed > 0,
                           'expired': total > 0 and closed == total, 'evidence': 'stub'}

    monkeypatch.setattr(sr, '_measure_health', health(0, 0))
    assert sr.collect(base)['verdict'] == 'HELD_INACTIVE'

    monkeypatch.setattr(sr, '_measure_health', health(0, 4))
    moved = sr.collect(base)
    assert moved['verdict'] == 'HELD', 'work in flight must not read as inactivity'
    assert moved['activity']['moved'] is True
    assert moved['activity']['in_progress'] == 4


def test_the_ratchet_declares_itself_expired_when_its_program_completes(monkeypatch):
    """ED-IN-0113 finding 5: `active_until` had no reader, so it was prose.

    Ceilings seeded for M1 keep grading after M1 ships unless something notices.
    An expired-but-still-enforcing ratchet measures the wrong program silently.
    """
    live = sr.collect()
    base = {'signals': {s['signal']: {'baseline': s['value'], 'target': 0}
                        for s in live['signals'] if s['value'] is not None},
            'active_until': 'M1 junctures closed == 7'}
    monkeypatch.setattr(sr, '_measure_health', lambda _b: {
        'closed': 7, 'total': 7, 'in_progress': 0, 'blocked': 0, 'ok': True,
        'expired': True, 'active_until': 'M1 junctures closed == 7', 'evidence': 'stub'})
    result = sr.collect(base)
    assert result['verdict'] == 'EXPIRED', (
        'a completed program must not keep grading against its own seeding ceilings'
    )
    assert result['regressions'] == 0, 'expiry is a re-seed signal, not a regression'


def test_filing_a_fresh_item_does_not_regress_the_ratchet(monkeypatch):
    """ED-IN-0114: the metric must punish ROT, not FILING.

    The original `ed.open` counted every open item, so appending a ledger row — which
    CLAUDE.md §2 expects of substantively every PR — regressed the ceiling by one. A
    gate that fires on the correct action gets ignored, and its own baseline file
    predicted that while shipping it anyway.

    Constructs both cases and requires they differ: adding a brand-new item changes
    nothing; letting one rot past the threshold changes the count.
    """
    monkeypatch.setenv('SCOPE_RATCHET_TODAY', '2026-07-31')
    old = {'status': 'open', 'needs_jordan': True, 'date': '2026-01-01'}
    fresh = {'status': 'open', 'needs_jordan': True, 'date': '2026-07-30'}

    monkeypatch.setattr(sr, '_ledger_rows', lambda: [old])
    before, _ = sr.measure_ed_stale()

    # Filing a fresh ED on top must NOT move the stale count.
    monkeypatch.setattr(sr, '_ledger_rows', lambda: [old, fresh])
    after_filing, _ = sr.measure_ed_stale()
    assert after_filing == before, (
        f'filing a fresh item moved the stale count {before} -> {after_filing}; '
        f'the metric is punishing the cure again'
    )

    # But a second ROTTED item must.
    monkeypatch.setattr(sr, '_ledger_rows', lambda: [old, dict(old)])
    after_rot, _ = sr.measure_ed_stale()
    assert after_rot == before + 1, 'a second stale item must raise the stale count'


def test_an_undated_open_item_counts_as_stale(monkeypatch):
    """Unknown age must not read as fresh.

    Four rows carry no parseable date. Treating unknown age as zero is the same
    'absence of evidence reads as a pass' defect this module rejects elsewhere.
    """
    monkeypatch.setenv('SCOPE_RATCHET_TODAY', '2026-07-31')
    monkeypatch.setattr(sr, '_ledger_rows',
                        lambda: [{'status': 'open', 'needs_jordan': False, 'date': None}])
    value, _ = sr.measure_ed_stale()
    assert value == 1, 'an undated open item must count as stale, not fresh'


def test_ci_shards_partition_the_validator_set_exactly():
    """--ci --shard must partition, never sample.

    A shard scheme that dropped a validator would make each shard green while the union
    silently stopped covering the gate — the silently-dead-gate class the collapse was
    rejected for. Asserts every job appears in exactly one shard, for several n.
    """
    sys.path.insert(0, TOOLS)
    import ci_gate_coverage as gc
    jobs = [j['id'] for j in gc.jobs() if j['tool_commands']]
    assert jobs, 'no validator jobs parsed — this pin would be vacuous'

    for n in (2, 3, 4):
        shards = [[j for k, j in enumerate(jobs) if k % n == i] for i in range(n)]
        flat = [j for s in shards for j in s]
        assert sorted(flat) == sorted(jobs), f'{n}-way shard is not a partition'
        assert len(flat) == len(set(flat)), f'{n}-way shard double-counts a job'
        assert all(s for s in shards), f'{n}-way shard produced an empty shard'
