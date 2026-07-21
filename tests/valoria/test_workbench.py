"""Tests for the Workbench (R1 prototype) — engine↔prose reconciliation workbench
(skills/valoria-vector-audit/scripts/workbench.py, program §2).

Pins: §8 reuse-by-identity of the sibling engine builders; the two-sided rows carry an
honest prose-co-occurrence state; stable card IDs; the notional-shadow guard; dispositions
memory; the two program vignettes; and — after the Opus-Max adversarial pass (2026-07-21) —
the matcher's DISCRIMINATION (a fabricated/common-word edge must NOT read co-mentioned) and
the doc-resolver's distinct declared-vs-missing states.
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'workbench.py')


def _load():
    spec = importlib.util.spec_from_file_location('workbench', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


workbench = _load()
_STATES = {'co-mentioned', 'mentioned', 'silent'}


def test_reuses_sibling_engine_builders_by_identity():
    import structure_audit as sa
    import formula_audit as fa
    assert workbench.sa.build_l2 is sa.build_l2
    assert workbench.fa.build_contract_edges is fa.build_contract_edges


def test_vignette_settlement_layer_is_two_sided():
    eng, has_doc, cards, rows = workbench.weave(_ROOT, 'settlement_layer')
    assert eng['node_state'] == 'engine-live' and has_doc and eng['doc_status'] == 'declared'
    assert rows and all(r['state'] in _STATES for r in rows)
    # a rich subsystem shows a genuine SPREAD — the prose co-mentions SOME engine edges and is
    # silent/thin on others (the siloed-prose gap is the point). Both halves pinned so neither a
    # false positive (all co-mentioned) nor a false negative (no co-mention) passes silently.
    states = {r['state'] for r in rows}
    assert 'co-mentioned' in states and (states & {'mentioned', 'silent'})
    # every open card carries a stable id + a both-directions question
    for c in cards:
        assert c['id'].startswith('wb-') and len(c['id']) == 13   # 'wb-' + 10 hex
        assert 'or should the engine not do this' in c['question'] or c['shadow']


def test_vignette_domain_actions_is_one_sided_notional():
    eng, has_doc, cards, rows = workbench.weave(_ROOT, 'domain_actions')
    assert eng['node_state'] == 'engine-notional' and eng['doc'] is None and not has_doc
    assert eng['doc_status'] == 'none'
    assert rows and all(r['state'] == 'silent' for r in rows)   # no doc => all silent
    # a notional module's cards are shadow-guarded (don't reconcile prose TO a fabricated row)
    assert cards and all(c['shadow'] and c['class'] == 'notional_shadow' for c in cards)
    # Finding 4: emits are read from the module's DECLARED contract, so its multiple declared
    # emits all surface — not just those a known consumer happens to attribute back.
    assert len(rows) >= 6


def test_card_ids_are_stable_and_deterministic():
    a = workbench._card_id('unspecced_wiring', 'm', 'cp', 'emits [k] to')
    b = workbench._card_id('unspecced_wiring', 'm', 'cp', 'emits [k] to')
    c = workbench._card_id('unspecced_wiring', 'm', 'cp', 'consumes [k] from')
    assert a == b and a != c and a.startswith('wb-')


def test_dispositions_partition_moves_answered_cards_to_resolved():
    cards = [{'id': 'wb-aaaa', 'class': 'x'}, {'id': 'wb-bbbb', 'class': 'y'}]
    open_, resolved = workbench.partition(cards, {'wb-bbbb': 'ruled: articulate in v31'})
    assert [c['id'] for c in open_] == ['wb-aaaa']
    assert [c['id'] for c in resolved] == ['wb-bbbb']
    assert resolved[0]['disposition'] == 'ruled: articulate in v31'


def test_articulation_states():
    # no doc => silent
    assert workbench.articulation(None, 'x', 'y')['state'] == 'silent'
    # endpoint present, relationship term absent => mentioned (NOT co-mentioned)
    assert workbench.articulation('the peninsular strain worsens', 'peninsular_strain',
                                  'env.disaster')['state'] == 'mentioned'
    # endpoint + relationship near => co-mentioned
    assert workbench.articulation('peninsular strain emits an env.disaster shock', 'peninsular_strain',
                                  'env.disaster')['state'] == 'co-mentioned'


def test_matcher_rejects_common_word_and_distant_false_positives():
    """The Opus-Max adversarial pass (Finding 1): the old common-word tail fallback let a
    fabricated `env.disaster` edge read as a link whenever any 'disaster' appeared in rich prose.
    The fix requires the literal-or-whole-phrase counterpart AND proximity for the top state."""
    # (a) the counterpart MODULE is absent; only the key's common word 'disaster' is present
    #     => silent (a fabricated module↔key edge does NOT manufacture a co-mention)
    r = workbench.articulation('a great disaster befell the realm; prosperity fell',
                               'peninsular_strain', 'env.disaster')
    assert r['state'] == 'silent'
    # (b) both endpoints present but > PROX apart => mentioned, never co-mentioned
    far = 'peninsular strain' + (' filler' * 120) + ' env.disaster'
    assert len(far) > workbench.PROX
    assert workbench.articulation(far, 'peninsular_strain', 'env.disaster')['state'] == 'mentioned'
    # (c) a lone short humanized tail (<4 chars) is not accepted as a fallback surface form
    assert workbench._mentions('the gap widened', 'x.gap') is False
    # (d) a multi-word humanized key IS matched (specificity preserved)
    assert workbench._mentions('a population change followed', 'env.population_change') is True


def test_doc_resolver_distinguishes_none_declared_and_missing():
    """Finding 2: the old _read_doc conflated 'no doc declared' with 'declared doc missing from
    disk' — both returned None, so a BROKEN contract pointer read as benign built-but-unspecced."""
    assert workbench._resolve_doc(_ROOT, None) == (None, 'none')
    text, status = workbench._resolve_doc(_ROOT, 'systems/settlements/settlement_layer_v30.md')
    assert status == 'declared' and text and 'Prosperity' in text
    assert workbench._resolve_doc(_ROOT, 'systems/nope/ghost_v30.md') == (None, 'missing')
