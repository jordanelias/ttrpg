"""Unit + integration tests for the Structural Observatory's G_pointer layer
(skills/valoria-vector-audit/scripts/pointer_audit.py).

Per the observatory governance (see test_structure_audit.py's docstring): unit-test
the scorecard/graph math on tiny synthetic fixtures with known answers, and pin at
least one integration check against the REAL corpus so the tool is proven to reuse
the real `tools/quantity_registry.py` resolver and `tools/ci_quantity_vocabulary_check.py`
(A17) scanners rather than a private reimplementation.
"""
import importlib.util
import os
import sys

import pytest
import yaml

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'pointer_audit.py')

# Make tools/ importable EXPLICITLY (mirrors tests/valoria/test_quantity_vocabulary_check.py)
# rather than relying on pointer_audit.py's own sys.path side effect at load time — the
# reuse-by-identity tests below import quantity_registry / ci_quantity_vocabulary_check
# directly and must not depend on import order.
_TOOLS = os.path.join(_ROOT, 'tools')
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)


def _load():
    spec = importlib.util.spec_from_file_location('pointer_audit', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pa = _load()


# ── proves real reuse: tools/quantity_registry.py is the resolver, not a copy ──

def test_module_imports_the_real_quantity_registry():
    # pointer_audit.py must import the actual tools/quantity_registry module (by
    # file identity), not a local reimplementation of resolve()/all_known().
    import quantity_registry as real_qr
    assert pa.quantity_registry is real_qr


def test_module_imports_the_real_a17_scanners():
    import ci_quantity_vocabulary_check as real_a17
    assert pa.a17 is real_a17
    assert pa.a17.scan_module_contracts is real_a17.scan_module_contracts
    assert pa.a17.scan_sim_literals is real_a17.scan_sim_literals


def test_known_alias_resolves_via_real_registry():
    # "Dexterity" is a declared alias of attr.body.agility in
    # references/descriptor_registry.yaml — must resolve through the real registry.
    matched, key = pa.quantity_registry.resolve('Dexterity')
    assert matched is not None
    assert key == 'attr.body.agility'


def test_nonsense_identifier_does_not_resolve():
    matched, key = pa.quantity_registry.resolve('totally_not_a_real_stat_xyz_123')
    assert matched is None
    assert key is None


# ── G_pointer graph + scorecard math on a tiny synthetic fixture ────────────

def _fake_occurrences():
    """4 occurrences over 3 unique identifiers, spanning 3 surfaces + a sim surface,
    with a deliberate repeat (Dexterity appears twice) to test occurrence vs unique
    identifier counting separately."""
    return [
        {'surface': 'module_contracts.state', 'location': 'mod_a', 'raw': 'Dexterity',
         'identifier': 'Dexterity', 'matched_as': 'Dexterity', 'key': 'attr.body.agility',
         'resolved': True},
        {'surface': 'module_contracts.derivations.output', 'location': 'mod_b', 'raw': 'Dexterity',
         'identifier': 'Dexterity', 'matched_as': 'Dexterity', 'key': 'attr.body.agility',
         'resolved': True},
        {'surface': 'module_contracts.derivations.inputs', 'location': 'mod_c', 'raw': 'made_up_stat',
         'identifier': 'made_up_stat', 'matched_as': None, 'key': None, 'resolved': False},
        {'surface': 'sim.stat_deltas', 'location': 'sim/fake.py:10', 'raw': 'made_up_stat',
         'identifier': 'made_up_stat', 'matched_as': None, 'key': None, 'resolved': False},
    ]


def test_build_g_pointer_dedupes_by_identifier():
    g = pa.build_g_pointer(_fake_occurrences())
    assert g == {'Dexterity': 'attr.body.agility', 'made_up_stat': None}


def test_scorecard_math_is_internally_consistent():
    occ = _fake_occurrences()
    sc = pa.build_scorecard(occ)
    ov = sc['overall']

    # occurrence-level: resolved + unresolved == total
    assert ov['occurrences_resolved'] + ov['occurrences_unresolved'] == ov['occurrences_total']
    assert ov['occurrences_total'] == len(occ)
    assert ov['occurrences_resolved'] == 2
    assert ov['occurrences_unresolved'] == 2
    assert ov['percent_resolved_occurrences'] == pytest.approx(50.0)

    # unique-identifier-level: resolved + unresolved == total, and total <= occurrence total
    assert ov['unique_identifiers_resolved'] + ov['unique_identifiers_unresolved'] == ov['unique_identifiers_total']
    assert ov['unique_identifiers_total'] == 2       # Dexterity, made_up_stat
    assert ov['unique_identifiers_resolved'] == 1
    assert ov['unique_identifiers_unresolved'] == 1
    assert ov['percent_resolved_unique_identifiers'] == pytest.approx(50.0)

    # by-surface breakdown sums back to the overall total (no occurrence dropped or double-counted)
    by_surface_total = sum(b['total'] for b in sc['by_surface'].values())
    by_surface_resolved = sum(b['resolved'] for b in sc['by_surface'].values())
    by_surface_unresolved = sum(b['unresolved'] for b in sc['by_surface'].values())
    assert by_surface_total == ov['occurrences_total']
    assert by_surface_resolved == ov['occurrences_resolved']
    assert by_surface_unresolved == ov['occurrences_unresolved']
    for b in sc['by_surface'].values():
        assert b['resolved'] + b['unresolved'] == b['total']
        if b['total']:
            assert b['percent_resolved'] == pytest.approx(100.0 * b['resolved'] / b['total'])
        else:
            assert b['percent_resolved'] is None

    # every occurrence's surface collapses into exactly one of the four named buckets
    assert set(sc['by_surface'].keys()) == set(pa.SURFACE_BUCKETS)
    # the sim.* surface must land in the 'sim_literals' bucket, not spill outside the 4 buckets
    assert sc['by_surface']['sim_literals']['total'] == 1  # made_up_stat's one sim.stat_deltas occurrence


def test_resolved_key_buckets_counts_occurrences_not_just_identifiers():
    buckets = pa.resolved_key_buckets(_fake_occurrences())
    assert len(buckets) == 1
    b = buckets[0]
    assert b['key'] == 'attr.body.agility'
    assert b['occurrences'] == 2          # Dexterity referenced twice
    assert b['unique_identifiers'] == ['Dexterity']


def test_unresolved_pointer_debt_dedupes_but_keeps_honest_counts():
    debt = pa.unresolved_pointer_debt(_fake_occurrences())
    # two distinct (surface, location, identifier) rows: mod_c and sim/fake.py:10
    assert len(debt) == 2
    for row in debt:
        assert row['identifier'] == 'made_up_stat'
        assert row['occurrences'] == 1
    total_debt_occurrences = sum(r['occurrences'] for r in debt)
    assert total_debt_occurrences == 2  # matches occurrences_unresolved above


# ── integration: real corpus, cross-checked against A17's own count ────────

@pytest.fixture(scope='module')
def real_occurrences():
    from pathlib import Path
    contracts_path = Path(_ROOT) / 'references' / 'module_contracts.yaml'
    contracts = yaml.safe_load(contracts_path.read_text(encoding='utf-8')) or {}
    sim_root = str(Path(_ROOT) / 'sim')
    return pa.collect_occurrences(contracts, sim_root)


def test_real_corpus_scorecard_matches_a17_totals(real_occurrences):
    # Cross-check against A17 (tools/ci_quantity_vocabulary_check.py) run directly on
    # the same inputs — same scanners + same resolver, so the totals MUST agree.
    import ci_quantity_vocabulary_check as a17
    from pathlib import Path
    contracts_path = Path(_ROOT) / 'references' / 'module_contracts.yaml'
    contracts = yaml.safe_load(contracts_path.read_text(encoding='utf-8')) or {}
    a17_resolved, a17_findings = a17.check(contracts, str(Path(_ROOT) / 'sim'))

    sc = pa.build_scorecard(real_occurrences)
    ov = sc['overall']
    assert ov['occurrences_total'] == a17_resolved + len(a17_findings)
    assert ov['occurrences_resolved'] == a17_resolved
    assert ov['occurrences_unresolved'] == len(a17_findings)


def test_real_corpus_has_a_known_unresolved_identifier(real_occurrences):
    # personal_combat's `state[].name` includes "Wounds" — not a registered descriptor
    # / names_index entry as of this writing. This is real, expected pointer-debt
    # (A17's own docstring calls this class of finding "a real, expected backlog
    # item, not a bug in this checker") — must surface as unresolved.
    g = pa.build_g_pointer(real_occurrences)
    assert 'Wounds' in g
    matching = [o for o in real_occurrences
                if o['identifier'] == 'Wounds' and o['location'] == 'personal_combat']
    assert matching, "expected an unresolved 'Wounds' occurrence from personal_combat state"
    assert all(not o['resolved'] for o in matching)


def test_real_corpus_dexterity_alias_resolves_in_context(real_occurrences):
    # Not every real occurrence need contain "Dexterity" itself, but the resolver
    # applied by collect_occurrences() must be the same one that resolves it —
    # cross-check identifiers already known-resolved carry the expected key.
    resolved_with_keys = {o['identifier']: o['key'] for o in real_occurrences if o['resolved'] and o['key']}
    assert resolved_with_keys, "expected at least one real occurrence to resolve to a registry key"
    # spot-check one concrete, stable mapping seen in the current corpus
    assert resolved_with_keys.get('Strength') == 'attr.body.strength'


def test_g_pointer_and_debt_totals_agree_with_scorecard(real_occurrences):
    sc = pa.build_scorecard(real_occurrences)
    debt = pa.unresolved_pointer_debt(real_occurrences)
    total_debt_occurrences = sum(r['occurrences'] for r in debt)
    assert total_debt_occurrences == sc['overall']['occurrences_unresolved']
    debt_identifiers = {r['identifier'] for r in debt}
    assert debt_identifiers.issubset(set(pa.build_g_pointer(real_occurrences).keys()))


# ── regression: degenerate empty-corpus percent must not render "None%" ───────
# (antagonist finding #3, agonist-antagonist reconciliation 2026-07-13)

def test_pct_helper_renders_none_as_dash():
    assert pa._pct(None) == '—'
    assert pa._pct(49.3) == '49.3%'
    assert pa._pct(0) == '0%'


def test_empty_corpus_scorecard_percents_are_none_not_zero():
    sc = pa.build_scorecard([])
    ov = sc['overall']
    assert ov['occurrences_total'] == 0
    assert ov['percent_resolved_occurrences'] is None
    assert ov['percent_resolved_unique_identifiers'] is None


# ── Category C: formula-local intermediate scope refinement (ED-IN-0061) ──────

def test_formula_local_intermediates_detects_lhs_defined_input():
    # A derivation input that its own formula DEFINES (LHS of '=') is a formula-local
    # intermediate, not an external quantity reference.
    contracts = {'modules': [{'module': 'm', 'derivations': [
        {'inputs': ['Legitimacy', 'W_s'], 'formula': 'W_s = a + b; T = W_s * 2'},
        {'inputs': ['Order'], 'formula': 'Order * 20'},   # no '=' LHS -> nothing local
    ]}]}
    locals_ = pa.formula_local_intermediates(contracts)
    assert ('m', 'W_s') in locals_
    assert ('m', 'Legitimacy') not in locals_   # a real input, not formula-defined
    assert ('m', 'Order') not in locals_


def test_formula_local_ignores_comparison_operators():
    # '==' at SEGMENT START must NOT be misread as an LHS definition. The comparison must sit
    # where the start-anchored regex would otherwise fire, so this actually exercises the `(?!=)`
    # guard: with the guard, 'X == 0' does NOT match (X's '=' is followed by '='); WITHOUT the
    # guard it WOULD match and wrongly mark X a local. (The old fixture 'gate when X == 0' put the
    # comparison mid-segment where the anchored regex never fires — vacuous; Fable-5 audit finding.)
    contracts = {'modules': [{'module': 'm', 'derivations': [
        {'inputs': ['X'], 'formula': 'X == 0'},
    ]}]}
    assert pa.formula_local_intermediates(contracts) == {}
    # sanity: a real single-'=' assignment on the SAME shape IS caught (proves the fixture is live)
    assert pa.formula_local_intermediates(
        {'modules': [{'module': 'm', 'derivations': [{'inputs': ['X'], 'formula': 'X = 0'}]}]}) == {('m', 'X'): 'X = 0'}


def test_is_formula_local_only_flags_derivation_inputs():
    local_set = {('m', 'W_s'): 'W_s = ...'}
    assert pa.is_formula_local(
        {'surface': 'module_contracts.derivations.inputs', 'location': 'm', 'identifier': 'W_s'}, local_set)
    # a STATE occurrence of the same name is NOT a formula-local (only inputs can be)
    assert not pa.is_formula_local(
        {'surface': 'module_contracts.state', 'location': 'm', 'identifier': 'W_s'}, local_set)
    # a different identifier on the input surface is not excluded
    assert not pa.is_formula_local(
        {'surface': 'module_contracts.derivations.inputs', 'location': 'm', 'identifier': 'Order'}, local_set)


def test_real_corpus_W_s_is_the_one_formula_local_and_refined_meter_is_smaller():
    from pathlib import Path
    contracts = yaml.safe_load(
        (Path(_ROOT) / 'references' / 'module_contracts.yaml').read_text(encoding='utf-8'))
    locals_ = pa.formula_local_intermediates(contracts)
    # settlement_layer's W_s (W_s = base(Type)+Prosperity+FacilityTier) is the corpus's one
    # formula-local today; it must be detected.
    assert ('settlement_layer', 'W_s') in locals_
    # the refined meter (formula-locals excluded) must count strictly fewer unique identifiers
    # AND fewer unresolved than the raw meter — the exclusion is real, not cosmetic.
    occ = pa.collect_occurrences(contracts, str(Path(_ROOT) / 'sim'))
    for o in occ:
        o['formula_local'] = pa.is_formula_local(o, locals_)
    raw = pa.build_scorecard(occ)['overall']
    refined = pa.build_scorecard([o for o in occ if not o['formula_local']])['overall']
    assert refined['unique_identifiers_total'] < raw['unique_identifiers_total']
    assert refined['unique_identifiers_unresolved'] < raw['unique_identifiers_unresolved']
