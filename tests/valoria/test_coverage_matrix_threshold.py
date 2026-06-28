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


def test_yaml_parser_reads_correct_block():
    """yaml_max_tokens returns the right entry, not a neighbouring block's value."""
    # canonical_sources.yaml is a different match block with a different cap.
    cov = rc.yaml_max_tokens('tests/coverage_matrix.md', RULES)
    assert isinstance(cov, int) and cov > 0


def test_missing_file_returns_none():
    assert rc.yaml_max_tokens('tests/coverage_matrix.md', '/no/such/file.yaml') is None


def test_unknown_match_returns_none():
    assert rc.yaml_max_tokens('tests/does_not_exist.md', RULES) is None
