"""
Drift guard for the coverage_matrix size threshold.

The threshold for tests/coverage_matrix.md is declared once, in
references/atomization_rules.yaml (the policy file). tools/ci_register_size_check.py reads it
via _coverage_matrix_threshold() into its THRESHOLDS dict. These tests pin that single-source
contract so the validator's enforced cap can never silently diverge from the policy file again.

Importing the validator is safe: its script body is guarded under `if __name__ == '__main__'`.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_register_size_check as rc  # noqa: E402

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
RULES = os.path.join(REPO_ROOT, 'references', 'atomization_rules.yaml')


def test_validator_threshold_matches_policy_file():
    """The cap the validator enforces equals the policy-file value — no drift."""
    policy_value = rc._coverage_matrix_threshold(rules_path=RULES)
    assert policy_value == rc.THRESHOLDS['tests/coverage_matrix.md']


def test_threshold_is_sourced_from_yaml_not_fallback():
    """The value comes from the YAML, not silently from the hardcoded fallback."""
    # Read the YAML directly and confirm the function returns that exact value.
    import yaml
    with open(RULES, encoding='utf-8') as f:
        rules = yaml.safe_load(f)
    yaml_value = next(p['max_tokens'] for p in rules['policies']
                      if p.get('match') == 'tests/coverage_matrix.md')
    assert rc._coverage_matrix_threshold(rules_path=RULES) == yaml_value


def test_missing_rules_file_falls_back():
    """A missing/unparseable policy file falls back rather than crashing the gate."""
    assert rc._coverage_matrix_threshold(rules_path='/no/such/file.yaml') == rc._COVERAGE_MATRIX_FALLBACK


def test_unknown_match_falls_back():
    assert rc._coverage_matrix_threshold(rules_path=RULES, match='tests/does_not_exist.md') == rc._COVERAGE_MATRIX_FALLBACK
