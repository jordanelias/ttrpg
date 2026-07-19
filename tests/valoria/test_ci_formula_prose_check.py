"""Tests for tools/ci_formula_prose_check.py (A18 — formula prose-drift detector, ED-1052 slice).

Pins the tool's CONTRACT, not corpus specifics: normalization equivalence, drift detection,
supersession suppression, the roster-open exclusion, reuse-by-identity of the A17 resolver, and
the measures-never-gates (exit 0) guarantee. Mirrors the discipline of test_formula_audit.py.
"""
import importlib
import os
import sys

import pytest

TOOLS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

mod = importlib.import_module('ci_formula_prose_check')


# ─── normalization: the whole test is string-normalized (in)equality ───

def test_norm_operator_and_markdown_equivalence():
    # unicode × maps to *, spacing collapses, markdown emphasis is stripped — none create a diff.
    # (ASCII 'x' is deliberately NOT treated as multiply — it is a common variable letter.)
    assert mod._norm('(3 × Endurance) + (2 × Spirit)') == mod._norm('(3*Endurance)+(2*Spirit)')
    assert mod._norm('**(3 × Endurance) + (2 × Spirit)**') == mod._norm('(3*Endurance)+(2*Spirit)')


def test_norm_distinguishes_genuinely_different_formulas():
    # the Combat Pool case: the struck form must NOT normalize-equal the ratified form
    assert mod._norm('(Agility × 2) + History + 3') != mod._norm('max(5, History + 6)')


def test_core_expr_takes_primary_not_recovery_subformula():
    # prose-wrapped field with a trailing recovery clause: compare the PRIMARY formula
    prose = "CURRENT: (3*Endurance)+(2*Spirit), range 5-47; recovery = (Endurance+History)*2, capped"
    assert mod._norm(prose) == mod._norm('(3 × Endurance) + (2 × Spirit)')


def test_looks_like_formula_rejects_bold_number_and_hyphenated_word():
    assert not mod._looks_like_formula('**28**')          # markdown bold, not a `*` operator
    assert not mod._looks_like_formula('slow-integrating')  # hyphenated word, not subtraction
    assert not mod._looks_like_formula('MS +2')            # a bare state-change delta (effect)
    assert mod._looks_like_formula('(3 × Endurance) + (2 × Spirit)')
    assert mod._looks_like_formula('floor(Bonds/2)+1')


# ─── scan(): drift detection + suppression + roster exclusion ───

def _census(formula_b, kind='pool', divergences=None):
    row = {
        'canonical_name': 'Test Pool', 'aliases': ['TP'], 'kind': kind,
        'defining_surface': 'a.md:1',
        'formulas': [
            {'formula': '(Spirit × 2) + 3', 'surface': 'a.md:1'},
            {'formula': formula_b, 'surface': 'b.md:9'},
        ],
        'status': 'DRIFTED',
    }
    if divergences:
        row['divergences'] = divergences
    return [row]


def test_scan_flags_divergent_carrier():
    findings, stats = mod.scan('.', _census('(Agility × 2) + 3'), live_scan=False)
    assert stats['census_drift'] == 1
    assert findings[0]['type'] == 'CENSUS_DRIFT'
    assert findings[0]['drift_surface'] == 'b.md:9'


def test_scan_does_not_flag_matching_carrier():
    findings, stats = mod.scan('.', _census('(Spirit*2)+3'), live_scan=False)
    assert stats['census_drift'] == 0
    assert findings == []


def test_scan_suppresses_superseded_restatement():
    # a divergent carrier explicitly marked superseded is NOT a violation
    findings, stats = mod.scan('.', _census('(Agility × 2) + 3 [STRUCK, superseded ED-901]'), live_scan=False)
    assert stats['census_drift'] == 0


def test_scan_excludes_attribute_rows_while_roster_open():
    # attribute_scalar rows carry "raw attribute 1-7" and must never be flagged (OPT-AV-1 OPEN)
    row = [{
        'canonical_name': 'Agility', 'kind': 'attribute_scalar',
        'defining_surface': 'r.yaml:1',
        'formulas': [
            {'formula': '(3 × Endurance) + 1', 'surface': 'r.yaml:1'},
            {'formula': '(9 × Endurance) + 1', 'surface': 'x.md:2'},
        ],
        'status': 'DRIFTED',
    }]
    findings, stats = mod.scan('.', row, live_scan=False)
    assert stats['roster_skipped'] == 1
    assert stats['census_drift'] == 0


# ─── reuse-by-identity (CLAUDE.md §8): the resolver is imported, not re-implemented ───

def test_reuses_quantity_registry_resolver():
    import quantity_registry
    assert mod.quantity_registry is quantity_registry


# ─── measures-never-gates: main() returns 0 regardless of findings ───

def test_main_exit_zero(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['ci_formula_prose_check.py', '--repo-root', '.'])
    assert mod.main() == 0


if __name__ == '__main__':
    sys.exit(pytest.main([__file__, '-q']))
