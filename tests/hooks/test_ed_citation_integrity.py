"""
Hermetic tests for the ED citation-integrity validator (tools/validate_ed_citations.py).

Prevents recurrence of the 2026-05-31 P1 resolver incident (ED-883): a canon doc
asserting CANONICAL/ratified status via ED ids that are either nonexistent (ED-874,
ED-885) or OPEN and cited as a basis (ED-865). Network-free — exercises the pure core.
Convention matches tests/hooks/test_correctness_gates.py + test_scope_vocabulary.py.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(HERE, '..', '..', 'tools'), '/home/claude'):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import validate_ed_citations as vec   # noqa: E402


def _kinds(viols, cid):
    return {v['kind'] for v in viols if v['id'] == cid}


def test_is_resolved():
    for ok in ('resolved', 'resolved-mechanical-tier-jordan-vetoable', 'struck',
               'applied', 'superseded', 'closed'):
        assert vec._is_resolved(ok), ok
    for bad in ('open', None, 'pending', 'in_progress'):
        assert not vec._is_resolved(bad), bad


def test_build_status_map_normalises_padding():
    m = vec.build_status_map([{'id': 'ED-017', 'status': 'resolved'},
                              {'id': 'ED-865', 'status': 'open'},
                              {'id': 'PP-7', 'status': 'applied'},
                              {'id': 'not-an-id', 'status': 'x'}])
    assert m == {'ED-17': 'resolved', 'ED-865': 'open', 'PP-7': 'applied'}


def test_nonexistent_flagged():
    docs = {'d.md': 'The resolver is CANONICAL (ED-874, ratified).'}
    v = vec.audit_citations(docs, {'ED-865': 'open'})
    assert 'NONEXISTENT' in _kinds(v, 'ED-874')


def test_open_as_basis_flagged():
    docs = {'d.md': 'Domain Action Resolution — CANONICAL (ED-865, ratified 2026-05-29).'}
    v = vec.audit_citations(docs, {'ED-865': 'open'})
    assert 'OPEN_AS_BASIS' in _kinds(v, 'ED-865')


def test_open_bare_reference_is_info_not_error():
    docs = {'d.md': 'An unresolved question is tracked in ED-865; awaiting Jordan.'}
    v = vec.audit_citations(docs, {'ED-865': 'open'})
    assert _kinds(v, 'ED-865') == {'OPEN_INFO'}


def test_resolved_basis_is_clean():
    docs = {'d.md': 'Intel restored as canonical stat per ED-787 closure 2026-05-03.'}
    v = vec.audit_citations(docs, {'ED-787': 'resolved'})
    assert _kinds(v, 'ED-787') == set()


def test_pp_skipped_unless_checked():
    docs = {'d.md': 'Operates via PP-460 (canonical).'}
    assert vec.audit_citations(docs, {}, checked_prefixes=('ED',)) == []
    v = vec.audit_citations(docs, {}, checked_prefixes=('ED', 'PP'))
    assert 'NONEXISTENT' in _kinds(v, 'PP-460')


def test_reproduces_p1_resolver_incident():
    # Mirrors params/factions/stats_1_7_scale.md L56/L92/L95/L101.
    doc = (
        "## Domain Action Resolution (deterministic+stochastic) — CANONICAL (ED-865/874, ratified 2026-05-29)\n"
        "Treaty positioning & ratification (ED-865/874 extension, 2026-05-30).\n"
        "Unique Actions (migrated 2026-05-30, ED-885 — Jordan-ratified).\n"
        "> [SUPERSEDED 2026-05-29, ED-865/874] the resolver above is canonical.\n"
        "Intel restored as canonical stat per ED-787 closure.\n"
    )
    universe = {'ED-865': 'open', 'ED-787': 'resolved'}   # 874 & 885 absent => nonexistent
    v = vec.audit_citations({'params/factions/stats_1_7_scale.md': doc}, universe)
    assert 'NONEXISTENT' in _kinds(v, 'ED-874')
    assert 'NONEXISTENT' in _kinds(v, 'ED-885')
    assert 'OPEN_AS_BASIS' in _kinds(v, 'ED-865')
    assert _kinds(v, 'ED-787') == set()   # resolved citation -> no false positive
