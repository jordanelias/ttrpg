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
               'applied', 'superseded', 'closed',
               # synonyms / terminal states accepted so a decided ED is never a violation
               'ratified', 'RATIFIED', 'confirmed', 'deprecated'):
        assert vec._is_resolved(ok), ok
    for bad in ('open', None, 'pending', 'in_progress', 'provisional'):
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


def test_dash_range_expands_inclusive():
    docs = {'params/x.md': 'Batch ED-844-846 ratified — all canonical.'}
    v = vec.audit_citations(docs, {'ED-844': 'open', 'ED-845': 'open', 'ED-846': 'open'})
    for cid in ('ED-844', 'ED-845', 'ED-846'):
        assert 'OPEN_AS_BASIS' in _kinds(v, cid), cid


def test_endash_range_expands():
    docs = {'params/x.md': 'Batch ED-844–846 ratified — all canonical.'}
    v = vec.audit_citations(docs, {'ED-844': 'open', 'ED-846': 'open'})
    assert 'OPEN_AS_BASIS' in _kinds(v, 'ED-846')


def test_oversized_range_not_expanded():
    docs = {'params/x.md': 'See ED-1-500 canonical.'}
    v = vec.audit_citations(docs, {})
    assert _kinds(v, 'ED-500') == set()   # not expanded; only the low bound checked
    assert 'NONEXISTENT' in _kinds(v, 'ED-1')


def test_provenance_file_demotes_basis_to_info():
    # A provenance register records where an ED applies; never a canonical claim.
    docs = {'references/roadmap_state.yaml': 'RATIFY ED-867 — canonical defaults.'}
    v = vec.audit_citations(docs, {'ED-867': 'open'})
    assert _kinds(v, 'ED-867') == {'OPEN_INFO'}


def test_planning_negation_marker_demotes_basis_to_info():
    docs = {'params/x.md': 'ED-867 is canonical but execution pending in this batch.'}
    v = vec.audit_citations(docs, {'ED-867': 'open'})
    assert _kinds(v, 'ED-867') == {'OPEN_INFO'}


def test_working_doc_and_provenance_predicates():
    assert vec._is_working_doc('designs/audit/2026-06-22-x.md')
    assert vec._is_working_doc('references/mass_battle_redesign_workplan_v1.md')
    assert not vec._is_working_doc('params/contest.md')
    assert vec._is_provenance('references/roadmap_state.yaml')
    assert vec._is_provenance('references/splits/params_board_game_split.yaml')
    assert not vec._is_provenance('params/contest.md')


def test_canonical_claim_in_params_still_caught():
    # Regression: precision must not become permissiveness — a genuine ED-883-class
    # claim in a canonical params file is still a hard violation.
    docs = {'params/factions/stats_1_7_scale.md':
            'Resolver is CANONICAL per ED-869 (ratified).'}
    v = vec.audit_citations(docs, {'ED-869': 'open'})
    assert 'OPEN_AS_BASIS' in _kinds(v, 'ED-869')


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
