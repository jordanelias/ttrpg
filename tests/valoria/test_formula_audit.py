"""Unit + integration tests for the Structural Observatory's L1 formula-dependency
layer (skills/valoria-vector-audit/scripts/formula_audit.py).

Per the observatory governance (see test_structure_audit.py's docstring): the graph
math is unit-tested on a tiny synthetic fixture with known answers, and at least one
assertion is pinned against the REAL corpus so the tool is proven to reuse the real
tools/quantity_registry.py resolver, tools/ci_quantity_vocabulary_check.py's
`_split_bundled`, and structure_audit.py's `tarjan_scc`/`degrees` rather than a
private reimplementation.
"""
import importlib.util
import os
import sys

import pytest
import yaml

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'formula_audit.py')

# Make tools/ importable EXPLICITLY (mirrors tests/valoria/test_pointer_audit.py)
# rather than relying on formula_audit.py's own sys.path side effect at load time.
_TOOLS = os.path.join(_ROOT, 'tools')
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fa = _load(_SCRIPT, 'formula_audit')
# formula_audit.py's own module-level `sys.path.insert(0, _SCRIPT_DIR)` (run above,
# as part of loading it) already put scripts/ on sys.path and cached 'structure_audit'
# in sys.modules via its `from structure_audit import tarjan_scc, degrees` — a plain
# `import structure_audit` here (NOT a second importlib.util load) hits that same
# cache entry, so identity checks below compare the real shared module, exactly
# mirroring how test_pointer_audit.py cross-checks tools/quantity_registry identity.
import structure_audit as sa  # noqa: E402


# ── proves real reuse (CLAUDE.md §8: "every rule lives once") ───────────────

def test_module_imports_the_real_quantity_registry():
    import quantity_registry as real_qr
    assert fa.quantity_registry is real_qr


def test_module_imports_the_real_a17_splitter():
    import ci_quantity_vocabulary_check as real_a17
    assert fa.a17 is real_a17
    assert fa.a17._split_bundled is real_a17._split_bundled


def test_module_imports_the_real_descriptor_registry_loader():
    import descriptor_registry as real_dr
    assert fa.descriptor_registry is real_dr


def test_module_reuses_structure_audit_tarjan_and_degrees():
    # must be the SAME function objects as structure_audit.py's — not a second
    # Tarjan/degrees implementation living in formula_audit.py.
    assert fa.tarjan_scc is sa.tarjan_scc
    assert fa.degrees is sa.degrees


def test_reuses_structure_audit_is_notional_and_cycles_by_identity():
    # capstone #12 (ED-IN-0056): the `notional` provenance predicate and the
    # self-loop-aware cycle extractor were copy-pasted here; now single-sourced in
    # structure_audit and IMPORTED. Pinned by identity so a future edit to either
    # rule can't silently fork the two layers' definitions.
    assert fa.is_notional is sa.is_notional
    assert fa._cycles is sa._cycles


def test_tarjan_still_finds_a_cycle_through_the_reused_import():
    adj = {'a': ['b'], 'b': ['c'], 'c': ['a']}
    comps = fa.tarjan_scc(adj)
    assert sorted(len(c) for c in comps) == [3]


# ── resolve_component: node identity ─────────────────────────────────────────

def test_resolve_component_known_name_maps_to_registry_key():
    resolved, node = fa.resolve_component('Strength')
    assert resolved is True
    assert node == 'attr.body.strength'


def test_resolve_component_alias_maps_to_registry_key():
    resolved, node = fa.resolve_component('Dexterity')  # alias of attr.body.agility
    assert resolved is True
    assert node == 'attr.body.agility'


def test_resolve_component_unknown_name_keeps_raw_text_as_node_id():
    resolved, node = fa.resolve_component('totally_not_a_real_quantity_xyz')
    assert resolved is False
    assert node == 'totally_not_a_real_quantity_xyz'


def test_loose_form_strips_trailing_parenthetical_only():
    assert fa._loose_form('faction Mandate (cross-module -> faction_state)') == 'faction Mandate'
    assert fa._loose_form('faction Mandate') == 'faction Mandate'
    # NOT normalized: a leading qualifier word is a stated, disclosed limitation
    assert fa._loose_form('settlement Order') == 'settlement Order'


def test_cycles_via_loose_form_catches_paren_hidden_feedback():
    # Fable-5 2026-07-14 audit, finding F (now FIXED, not just disclosed): a cross-module
    # feedback whose legs spell the same quantity differently — output annotated, input bare —
    # is missed by the exact-identity SCC but caught by the loose-form pass.
    adj = {
        'Legitimacy': {'faction Mandate (cross-module -> faction_state)'},  # L feeds Mandate
        'faction Mandate (cross-module -> faction_state)': set(),
        'faction Mandate': {'Legitimacy'},                                  # Mandate feeds L
    }
    # exact-identity: the two Mandate spellings are distinct nodes -> NO cycle
    assert fa._cycles(fa.tarjan_scc(adj), adj) == []
    # loose-form pass: collapses the annotation -> the Legitimacy<->Mandate cycle closes
    paren = fa.cycles_via_loose_form(adj, [])
    assert ['Legitimacy', 'faction Mandate'] in paren


def test_cycles_via_loose_form_drops_collapse_induced_self_loops():
    # An output annotated form of a node feeding ONLY back to its own bare name must NOT be
    # reported as a cycle (that's the annotation-shadowing false-positive the fix guards against).
    adj = {'X': {'X (annotated)'}, 'X (annotated)': set()}
    assert fa.cycles_via_loose_form(adj, []) == []


# ── build_contract_edges / build_descriptor_edges on tiny synthetic fixtures ─

def _synthetic_contracts():
    """Two modules, three derivations: a clean edge (Strength -> Foo Bar Stat),
    an orphan input (bogus_intermediate, not registered and never an output),
    and a same-output multi-definition with differing input sets (Widget
    Total defined twice: once from Strength, once from a made-up field)."""
    return {
        'modules': [
            {
                'module': 'canon_mod', 'doc': 'designs/fake.md', 'resolver': 'deterministic_accounting',
                'derivations': [
                    {'output': 'Foo Bar Stat', 'inputs': ['Strength', 'bogus_intermediate'],
                     'formula': 'Strength - bogus_intermediate', 'source': 'fake §1'},
                    {'output': 'Widget Total', 'inputs': ['Strength'],
                     'formula': 'Strength * 2', 'source': 'fake §2'},
                ],
            },
            {
                'module': 'notional_mod', 'doc': None, 'resolver': None,
                'derivations': [
                    {'output': 'Widget Total', 'inputs': ['made_up_field'],
                     'formula': 'made_up_field + 1', 'source': 'fake §3 [ASSUMPTION]'},
                ],
            },
        ],
    }


def _synthetic_descriptor():
    return {
        'aggregates': {'entries': [
            {'key': 'agg.body', 'name': 'Body', 'compute': 'sum',
             'members': ['attr.body.strength'], 'status': 'placeholder'},
        ]},
        'practitioner_stats': {'entries': [
            {'key': 'prac.tps', 'name': 'Thread Pool Score', 'derived_from': 'prac.thread_sensitivity',
             'formula': 'floor(TS / 10)'},
        ]},
    }


def test_build_contract_edges_produces_expected_edge_count():
    edges, definitions = fa.build_contract_edges(_synthetic_contracts())
    # canon_mod derivation 0: 2 inputs x 1 output = 2 edges
    # canon_mod derivation 1: 1 input x 1 output = 1 edge
    # notional_mod derivation 0: 1 input x 1 output = 1 edge
    assert len(edges) == 4
    assert all(e['layer'] == 'module_contracts.derivations' for e in edges)


def test_build_contract_edges_notional_flag_follows_module_doc_and_resolver():
    edges, _ = fa.build_contract_edges(_synthetic_contracts())
    canon_edges = [e for e in edges if e['module'] == 'canon_mod']
    notional_edges = [e for e in edges if e['module'] == 'notional_mod']
    assert canon_edges and all(e['notional'] is False for e in canon_edges)
    assert notional_edges and all(e['notional'] is True for e in notional_edges)


def test_build_descriptor_edges_aggregate_member_and_derived_from():
    edges = fa.build_descriptor_edges(_synthetic_descriptor())
    layers = {e['layer'] for e in edges}
    assert 'descriptor_registry.aggregates' in layers
    assert 'descriptor_registry.practitioner_stats' in layers

    agg_edge = next(e for e in edges if e['layer'] == 'descriptor_registry.aggregates')
    assert agg_edge == {
        'src': 'attr.body.strength', 'dst': 'agg.body',
        'src_raw': 'attr.body.strength', 'dst_raw': 'agg.body',
        'src_resolved': True, 'dst_resolved': True,
        'module': None, 'derivation_index': None, 'notional': True,  # status: placeholder
        'formula': 'sum', 'source': 'descriptor_registry.yaml aggregates',
        'layer': 'descriptor_registry.aggregates',
    }

    df_edge = next(e for e in edges if e['layer'] == 'descriptor_registry.practitioner_stats')
    assert df_edge['src'] == 'prac.thread_sensitivity'
    assert df_edge['dst'] == 'prac.tps'
    assert df_edge['notional'] is False


# ── detections on the combined synthetic fixture: known answers ─────────────

@pytest.fixture()
def synthetic_dag():
    contract_edges, definitions = fa.build_contract_edges(_synthetic_contracts())
    descriptor_edges = fa.build_descriptor_edges(_synthetic_descriptor())
    edges = contract_edges + descriptor_edges
    adj = fa.build_adjacency(edges, definitions)
    return {'edges': edges, 'definitions': definitions, 'adj': adj}


def test_orphan_input_detected_and_registered_ones_are_not(synthetic_dag):
    orphans = fa.find_orphan_inputs(synthetic_dag['edges'], synthetic_dag['definitions'])
    ids = {o['identifier'] for o in orphans}
    # bogus_intermediate: unresolved, never an output -> orphan
    assert 'bogus_intermediate' in ids
    # made_up_field: unresolved, never an output -> orphan (from the notional module)
    assert 'made_up_field' in ids
    # Strength: resolves via the registry -> never an orphan
    assert 'Strength' not in ids
    assert 'attr.body.strength' not in ids


def test_orphan_canon_vs_notional_bucketing(synthetic_dag):
    orphans = fa.find_orphan_inputs(synthetic_dag['edges'], synthetic_dag['definitions'])
    by_id = {o['identifier']: o for o in orphans}
    assert by_id['bogus_intermediate']['any_canon'] is True    # canon_mod, doc set
    assert by_id['made_up_field']['any_canon'] is False        # notional_mod, doc: null


def test_multi_definition_output_detected_with_differing_inputs(synthetic_dag):
    multis = fa.find_multi_definitions(synthetic_dag['definitions'])
    nodes = {m['node']: m for m in multis}
    assert 'Widget Total' in nodes
    m = nodes['Widget Total']
    assert len(m['definitions']) == 2
    assert m['differing_inputs'] is True    # ['Strength'] vs ['made_up_field']
    assert m['any_canon'] is True           # canon_mod's definition is not notional
    # Foo Bar Stat / agg.body / prac.tps are each defined exactly once -> not flagged
    assert 'Foo Bar Stat' not in nodes
    assert 'agg.body' not in nodes


def test_no_cycle_on_the_synthetic_dag(synthetic_dag):
    scc = fa.tarjan_scc(synthetic_dag['adj'])
    assert fa._cycles(scc, synthetic_dag['adj']) == []


def test_cycle_detected_when_present():
    # A depends on B, B depends on A: a hand-built 2-node cycle (not achievable
    # via the real corpus today, so exercised directly at the adjacency level).
    adj = {'quantity.a': {'quantity.b'}, 'quantity.b': {'quantity.a'}}
    scc = fa.tarjan_scc(adj)
    cycles = fa._cycles(scc, adj)
    assert len(cycles) == 1
    assert set(cycles[0]) == {'quantity.a', 'quantity.b'}


def test_self_loop_is_a_cycle():
    adj = {'x': {'x'}}
    scc = fa.tarjan_scc(adj)
    assert fa._cycles(scc, adj) == [['x']]


def test_max_depth_on_a_simple_chain():
    # a -> b -> c : two edges, max depth 2
    adj = {'a': {'b'}, 'b': {'c'}, 'c': set()}
    scc = fa.tarjan_scc(adj)
    assert fa.compute_max_depth(adj, scc) == 2


def test_roots_and_leaves_on_synthetic_dag(synthetic_dag):
    adj = synthetic_dag['adj']
    nodes = list(adj)
    deg = fa.degrees(adj, nodes)
    roots = {n for n in nodes if deg[n]['in'] == 0 and deg[n]['out'] > 0}
    leaves = {n for n in nodes if deg[n]['out'] == 0 and deg[n]['in'] > 0}
    assert 'attr.body.strength' in roots       # attr.body.strength feeds agg.body, never fed itself
    assert 'bogus_intermediate' in roots       # dangling input, never derived
    assert 'Widget Total' in leaves            # never consumed as an input downstream
    assert 'agg.body' in leaves


# ── integration: runs on the REAL corpus and produces a non-empty DAG ───────

@pytest.fixture(scope='module')
def real_dag():
    from pathlib import Path
    contracts = yaml.safe_load((Path(_ROOT) / 'references' / 'module_contracts.yaml').read_text(encoding='utf-8')) or {}
    import descriptor_registry as real_dr
    descriptor = real_dr.load(text=(Path(_ROOT) / 'references' / 'descriptor_registry.yaml').read_text(encoding='utf-8')) or {}
    contract_edges, definitions = fa.build_contract_edges(contracts)
    descriptor_edges = fa.build_descriptor_edges(descriptor)
    edges = contract_edges + descriptor_edges
    adj = fa.build_adjacency(edges, definitions)
    return {'edges': edges, 'definitions': definitions, 'adj': adj}


def test_real_corpus_produces_a_nonempty_dag(real_dag):
    assert len(real_dag['adj']) > 10
    assert len(real_dag['edges']) > 10
    # cross-layer connectivity: a module_contracts input that resolves to a
    # registry key (Strength -> attr.body.strength) should land on the SAME
    # node the descriptor_registry aggregate-member edge also touches.
    assert 'attr.body.strength' in real_dag['adj']
    contract_sources = {e['src'] for e in real_dag['edges'] if e['layer'] == 'module_contracts.derivations'}
    descriptor_sources = {e['src'] for e in real_dag['edges'] if e['layer'].startswith('descriptor_registry')}
    # attr.body.strength is BOTH a module_contracts-derivation input (personal_combat's
    # Health formula references "Strength") AND a descriptor_registry aggregate member
    # (agg.body's members) -- the same registry key, reached from both source layers.
    assert 'attr.body.strength' in contract_sources
    assert 'attr.body.strength' in descriptor_sources


def test_real_corpus_has_known_orphan_inputs_pinned(real_dag):
    # personal_combat's Health derivation subtracts cumulative_damage, which is
    # not a registered descriptor and not the output of any derivation in the
    # corpus today (2026-07-13) — a real, expected pointer-debt/orphan.
    orphans = fa.find_orphan_inputs(real_dag['edges'], real_dag['definitions'])
    ids = {o['identifier'] for o in orphans}
    assert 'cumulative_damage' in ids
    # settlement_layer's faction-Mandate derivation inputs were canonicalized
    # (ED-IN-0060): L_s/PS_s -> Legitimacy/Popular Support, which ARE registered
    # (set.legitimacy/set.popular_support) so they are no longer orphans. What
    # remains is W_s -- a formula-local intermediate (W_s = base(Type)+Prosperity+
    # FacilityTier), unregistered and derived nowhere else -- the one real residual
    # orphan of that derivation.
    assert 'W_s' in ids
    assert 'L_s' not in ids and 'PS_s' not in ids   # canonicalized away, no longer orphans


def test_real_corpus_faction_mandate_paren_variant_is_not_a_false_orphan(real_dag):
    # settlement_layer derivation #5 ("settlement L/PS (Mandate feedback)")
    # takes input "faction Mandate", which differs from the real output
    # "faction Mandate (cross-module -> faction_state)" only by a trailing
    # parenthetical -- the one normalization this tool applies -- so it must
    # NOT be reported as an orphan.
    orphans = fa.find_orphan_inputs(real_dag['edges'], real_dag['definitions'])
    ids = {o['identifier'] for o in orphans}
    assert 'faction Mandate' not in ids


def test_real_corpus_resolved_input_never_shows_as_orphan(real_dag):
    orphans = fa.find_orphan_inputs(real_dag['edges'], real_dag['definitions'])
    ids = {o['identifier'] for o in orphans}
    assert 'attr.body.strength' not in ids
    assert 'Strength' not in ids


def test_real_corpus_scc_and_degrees_run_without_error(real_dag):
    scc = fa.tarjan_scc(real_dag['adj'])
    cycles = fa._cycles(scc, real_dag['adj'])
    assert isinstance(cycles, list)   # today's corpus is expected acyclic; not asserting emptiness
    deg = fa.degrees(real_dag['adj'], list(real_dag['adj']))
    assert all('in' in d and 'out' in d for d in deg.values())


# ── run() end-to-end smoke test (writes register + JSON) ────────────────────

def test_run_end_to_end_writes_register_and_json(tmp_path):
    result = fa.run(_ROOT, tmp_path)
    assert (tmp_path / 'formula_register.md').exists()
    assert (tmp_path / 'data' / 'g_formula.json').exists()
    assert (tmp_path / 'data' / 'formula_metrics.json').exists()
    text = (tmp_path / 'formula_register.md').read_text(encoding='utf-8')
    assert 'CONTRACT-level formula structure only' in text
    assert 'cumulative_damage' in text
    assert result['orphans']


# ── regression: agonist-antagonist reconciliation fixes (2026-07-13) ──────────

def test_null_output_derivation_surfaces_orphan_and_flags_malformed():
    # MED3: a derivation with output:None must NOT silently drop its inputs (which
    # would hide a genuine orphan). Inputs route to a sentinel node; malformed flagged.
    c = {'modules': [{'module': 'broken', 'doc': 'x.md', 'resolver': 'r',
                      'derivations': [{'output': None,
                                       'inputs': ['definitely_undefined_qty_zzz', 'Strength']}]}]}
    edges, defs = fa.build_contract_edges(c)
    assert len(edges) == 2  # was 0 before the fix
    orphans = {o['identifier'] for o in fa.find_orphan_inputs(edges, defs)}
    assert 'definitely_undefined_qty_zzz' in orphans   # the genuine orphan surfaces
    assert 'Strength' not in orphans                    # resolves via the registry
    malformed = fa.find_malformed_derivations(c)
    assert len(malformed) == 1
    assert malformed[0]['module'] == 'broken' and malformed[0]['derivation_index'] == 0


def test_placeholder_stat_edge_marked_notional():
    # LOW6: a *_stats derived_from edge whose entry carries status:placeholder must be
    # notional (was hardcoded False, so it would have shown as canon).
    desc = {'practitioner_stats': {'entries': [
        {'key': 'prac.x', 'derived_from': 'prac.y', 'status': 'placeholder'}]}}
    edges = fa.build_descriptor_edges(desc)
    assert len(edges) == 1 and edges[0]['notional'] is True


def test_non_mapping_contracts_exits_gracefully(tmp_path):
    # LOW4: a YAML list at the top level of module_contracts.yaml must exit cleanly,
    # not crash with a raw AttributeError.
    (tmp_path / 'references').mkdir()
    (tmp_path / 'references' / 'module_contracts.yaml').write_text('- a\n- b\n')
    with pytest.raises(SystemExit):
        fa.run(tmp_path, tmp_path / 'out')
