"""Tests for the Loom (R1 prototype) — engine↔prose reconciliation workbench
(skills/valoria-vector-audit/scripts/loom.py, program §2).

Pins: §8 reuse-by-identity of the sibling engine builders; the two-sided rows carry a
prose-articulation state; stable card IDs; the notional-shadow guard; dispositions memory;
and the two program vignettes (settlement_layer both-sided, domain_actions one-sided/notional).
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'loom.py')


def _load():
    spec = importlib.util.spec_from_file_location('loom', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


loom = _load()


def test_reuses_sibling_engine_builders_by_identity():
    import structure_audit as sa
    import formula_audit as fa
    assert loom.sa.build_l2 is sa.build_l2
    assert loom.fa.build_contract_edges is fa.build_contract_edges


def test_vignette_settlement_layer_is_two_sided():
    eng, has_doc, cards, rows = loom.weave(_ROOT, 'settlement_layer')
    assert eng['node_state'] == 'engine-live' and has_doc
    assert rows and all(r['state'] in ('articulated', 'mentioned', 'silent') for r in rows)
    # a rich subsystem articulates SOME but not all edges (the siloed-prose gap is the point)
    states = {r['state'] for r in rows}
    assert 'articulated' in states and (states & {'mentioned', 'silent'})
    # every open card carries a stable id + a both-directions question
    for c in cards:
        assert c['id'].startswith('loom-') and len(c['id']) == 15
        assert 'or should the engine not do this' in c['question'] or c['shadow']


def test_vignette_domain_actions_is_one_sided_notional():
    eng, has_doc, cards, rows = loom.weave(_ROOT, 'domain_actions')
    assert eng['node_state'] == 'engine-notional' and eng['doc'] is None and not has_doc
    assert rows and all(r['state'] == 'silent' for r in rows)   # no doc => all silent
    # a notional module's cards are shadow-guarded (don't reconcile prose TO a fabricated row)
    assert cards and all(c['shadow'] and c['class'] == 'notional_shadow' for c in cards)


def test_card_ids_are_stable_and_deterministic():
    a = loom._card_id('unspecced_wiring', 'm', 'cp', 'emits [k] to')
    b = loom._card_id('unspecced_wiring', 'm', 'cp', 'emits [k] to')
    c = loom._card_id('unspecced_wiring', 'm', 'cp', 'consumes [k] from')
    assert a == b and a != c and a.startswith('loom-')


def test_dispositions_partition_moves_answered_cards_to_resolved():
    cards = [{'id': 'loom-aaaa', 'class': 'x'}, {'id': 'loom-bbbb', 'class': 'y'}]
    open_, resolved = loom.partition(cards, {'loom-bbbb': 'ruled: articulate in v31'})
    assert [c['id'] for c in open_] == ['loom-aaaa']
    assert [c['id'] for c in resolved] == ['loom-bbbb']
    assert resolved[0]['disposition'] == 'ruled: articulate in v31'


def test_articulation_states():
    assert loom.articulation(None, 'x', 'y')['state'] == 'silent'                  # no doc
    assert loom.articulation('talks about Prosperity here', 'Prosperity', 'Zzz')['state'] == 'mentioned'
    assert loom.articulation('Prosperity drives Local Economy', 'Prosperity',
                             'Local Economy')['state'] == 'articulated'
