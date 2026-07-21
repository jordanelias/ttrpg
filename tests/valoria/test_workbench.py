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


def test_weave_all_corpus_map():
    """The --all corpus mode weaves every module and surfaces the STRUCTURAL reconciliation map:
    node state, doc status, and the built-but-unspecced set (the reliable, precise signal)."""
    summary = workbench.weave_all(_ROOT)
    assert len(summary) == 27
    assert all('node_state' in s and 'doc_status' in s and 'edges' in s for s in summary)
    unspecced = [s['module'] for s in summary
                 if s['node_state'] == 'engine-notional' and s['doc_status'] == 'none']
    assert 'engine_clock' in unspecced and len(unspecced) >= 5      # the T0 blocker is one of them
    # personal_combat's directory doc is surfaced as such, not a false 'missing'
    assert any(s['module'] == 'personal_combat' and s['doc_status'] == 'declared-dir' for s in summary)
    view = workbench.render_all(summary)
    assert 'corpus-wide reconciliation map' in view and 'Built-but-unspecced' in view


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


def test_module_aliases_improve_counterpart_detection():
    """R2 (ED-IN-0082): a module's declared display-aliases (module_contracts, carried through
    structure_audit.build_l2) let the Workbench match a counterpart referred to by its PROSE name,
    not just its humanized id. settlement_layer's doc says 'Faction Layer' (not 'faction_state'),
    so the emit->faction_state edge reads 'mentioned' (counterpart present) instead of a false
    'silent'. Co-mention is unchanged — the emit's Key concept genuinely isn't in the prose."""
    import structure_audit as sa
    from pathlib import Path
    _, meta, *_ = sa.build_l2(Path(_ROOT))
    assert 'Faction Layer' in meta['faction_state'].get('aliases', [])       # carried through build_l2
    # counterpart found via its display alias -> mentioned; without the alias the humanized id is absent -> silent
    assert workbench.articulation('the Faction Layer reacts here', 'faction_state', 'zzz.none',
                                  cp_aliases=['Faction Layer'])['state'] == 'mentioned'
    assert workbench.articulation('the Faction Layer reacts here', 'faction_state',
                                  'zzz.none')['state'] == 'silent'


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


def test_doc_resolver_handles_directory_valued_doc():
    """A DIRECTORY-valued doc (personal_combat -> combat_engine_v1/) is resolved by concatenating
    its .md files, not spuriously reported 'missing' — the corpus-wide Workbench run surfaced this
    false negative (a real dir mis-read as a broken pointer)."""
    text, status = workbench._resolve_doc(_ROOT, 'systems/combat/combat_engine_v1/')
    assert status == 'declared-dir' and text and len(text) > 500
    eng, has_doc, cards, rows = workbench.weave(_ROOT, 'personal_combat')
    assert has_doc and eng['doc_status'] == 'declared-dir'
