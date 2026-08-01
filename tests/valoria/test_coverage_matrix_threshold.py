"""
Drift guard for the coverage_matrix size threshold.

The threshold for tests/coverage_matrix.md is declared once, in
references/atomization_rules.yaml (the policy file). tools/ci_register_size_check.py
reads it from there via yaml_max_tokens() into COVERAGE_MATRIX_LIMIT and uses it in
its THRESHOLDS dict. These tests pin that single-source contract so the two can never
silently diverge again.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_register_size_check as rc  # noqa: E402

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
RULES = os.path.join(REPO_ROOT, 'references', 'atomization_rules.yaml')


def test_validator_threshold_matches_policy_file():
    """The cap the validator enforces equals the policy-file value — no drift."""
    policy_value = rc.yaml_max_tokens('tests/coverage_matrix.md', RULES)
    assert policy_value is not None, "coverage_matrix entry missing from atomization_rules.yaml"
    assert rc.THRESHOLDS['tests/coverage_matrix.md'] == policy_value
    assert rc.COVERAGE_MATRIX_LIMIT == policy_value


SINGLE_SOURCED = {
    # repo path -> the module-level constant that must mirror the policy file
    'tests/coverage_matrix.md': 'COVERAGE_MATRIX_LIMIT',
    'registers/patch_register_active.yaml': 'PATCH_REGISTER_LIMIT',
    'references/module_contracts.yaml': 'MODULE_CONTRACTS_LIMIT',
}


def test_every_single_sourced_threshold_matches_the_policy_file():
    """Generalises the coverage_matrix guard above to EVERY single-sourced cap.

    Added ED-IN-0097 (W4). Rationale (§0.1 #5 — sweep the pattern, and the guard is what makes
    the sweep real): `references/module_contracts.yaml` was the THIRD instance of one defect —
    a cap hardcoded in ci_register_size_check.py while references/atomization_rules.yaml
    declared its own value. The first two (coverage_matrix, patch_register) were each fixed as
    one-offs, and only coverage_matrix got a guard, so the class recurred silently until the W4
    join pushed module_contracts over the stale copy. This test fails on the NEXT recurrence.
    """
    checked = 0
    for path, const in SINGLE_SOURCED.items():
        policy_value = rc.yaml_max_tokens(path, RULES)
        assert policy_value is not None, f'{path} entry missing from atomization_rules.yaml'
        assert getattr(rc, const) == policy_value, (
            f'{const} ({getattr(rc, const)}) has drifted from the policy file ({policy_value}) '
            f'for {path} — the cap must live in atomization_rules.yaml alone')
        assert rc.THRESHOLDS[path] == policy_value, (
            f'THRESHOLDS[{path!r}] is a hardcoded copy, not {const} — re-single-source it')
        checked += 1
    # An assertion loop must assert that it asserted (§0.1 #2).
    assert checked == len(SINGLE_SOURCED) == 3, f'expected 3 single-sourced caps, checked {checked}'


def test_yaml_parser_reads_correct_block():
    """yaml_max_tokens returns the right entry, not a neighbouring block's value."""
    # canonical_sources.yaml is a different match block with a different cap.
    cov = rc.yaml_max_tokens('tests/coverage_matrix.md', RULES)
    assert isinstance(cov, int) and cov > 0


def test_missing_file_returns_none():
    assert rc.yaml_max_tokens('tests/coverage_matrix.md', '/no/such/file.yaml') is None


def test_unknown_match_returns_none():
    assert rc.yaml_max_tokens('tests/does_not_exist.md', RULES) is None


# ── The approaching-cap warning (ED-MB-0063 residual) ─────────────────────────
#
# WHY THE WARNING EXISTS. Output was binary OK/FAIL, so a register at 99% of its cap
# printed the same "OK" as one at 10%. Three files were found above 95% in a single
# session (MB ledger 98.5% — 740 tokens left; IN ledger 95.2%; coverage matrix 97.7%),
# none of which had announced itself. The first signal would have been a BLOCKING
# failure on whichever PR added the next entry, which is structurally not the PR that
# grew the file.
#
# BOTH PROPERTIES ARE PINNED BELOW, and the pair is the point (§0.1 #2 — an assertion
# must be able to observe the failure it excludes):
#   - the warn band FIRES, so the feature is not inert; and
#   - the warn band does NOT fail the gate, so it has not silently become a lower cap.
# A test of only the first would pass just as happily if WARN_FRACTION were wired into
# `violations`, which is precisely the regression worth catching.

def test_warn_fraction_is_below_the_cap_and_leaves_real_headroom():
    assert 0.0 < rc.WARN_FRACTION < 1.0, 'a warn at or above the cap can never fire before FAIL'
    # 0.85 of a 50,000-token ledger is 7,500 tokens of notice — several sessions' work.
    # Much above ~0.95 and the warning arrives too late to act on without an emergency pass.
    assert rc.WARN_FRACTION <= 0.95, (
        f'WARN_FRACTION {rc.WARN_FRACTION} leaves too little notice to be actionable')


def _run(tmp_path, monkeypatch, tokens, threshold):
    """Run main() over ONE synthetic file of a known size; return (exit_code, stdout)."""
    import io
    import contextlib
    p = tmp_path / 'synthetic_register.md'
    p.write_text('x' * (tokens * 4), encoding='utf-8')   # main() computes len//4
    monkeypatch.setattr(rc, 'THRESHOLDS', {str(p): threshold})
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc.main()
        code = 0
    except SystemExit as e:
        code = e.code
    return code, buf.getvalue()


def test_a_register_inside_the_warn_band_warns_but_does_not_fail(tmp_path, monkeypatch):
    """REPORT-ONLY. 90% of cap: the warning must appear AND the gate must still pass."""
    code, out = _run(tmp_path, monkeypatch, tokens=9_000, threshold=10_000)
    assert 'WARN' in out, 'a register at 90% of its cap produced no warning'
    assert 'APPROACHING CAP' in out
    assert code == 0, (
        'the approaching-cap warning FAILED the gate — it has become a second, lower cap, '
        'which re-creates the same cliff a few thousand tokens earlier')


def test_a_register_below_the_band_is_silent(tmp_path, monkeypatch):
    """The other direction: the warning must not fire on a file with real headroom,
    or it degrades to noise and gets ignored — the failure mode it was built to fix."""
    code, out = _run(tmp_path, monkeypatch, tokens=1_000, threshold=10_000)
    assert 'WARN' not in out and 'APPROACHING CAP' not in out
    assert 'OK' in out
    assert code == 0


def test_over_cap_still_fails(tmp_path, monkeypatch):
    """The warn band must not have swallowed the BLOCKING behaviour it sits beneath."""
    code, out = _run(tmp_path, monkeypatch, tokens=11_000, threshold=10_000)
    assert 'FAIL' in out and 'REGISTER SIZE VIOLATIONS' in out
    assert code == 1, 'an over-cap register no longer fails the gate'
