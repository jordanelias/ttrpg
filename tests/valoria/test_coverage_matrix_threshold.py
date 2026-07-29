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
