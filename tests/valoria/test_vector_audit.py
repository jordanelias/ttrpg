"""Unit tests for the Structural Observatory's L0 prose layer
(skills/valoria-vector-audit/scripts/vector_audit.py).

vector_audit.py shipped with ZERO tests (Fable-5 multi-agent audit, 2026-07-13,
finding J) even though it carries the classifier that decides, for every doc in
the corpus, whether it is design / discourse / excluded — the partition every
downstream L0 finding (and gen_audit, which reuses `banner_classify`) is built
on. These pin the classifier's decision table (esp. the status-first tie-break
that the same audit added), the same_class equivalence predicate, and the §8
reuse of the real `names` reader.
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'vector_audit.py')


def _load():
    spec = importlib.util.spec_from_file_location('vector_audit', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


va = _load()


# ── banner_classify decision table ──────────────────────────────────────────

def test_status_declaration_is_design_even_with_audit_word():
    # The Fable-5 status-first fix: a REFERENCE/CURRENT/WORKING/CANONICAL/DESIGN
    # status head is DESIGN, checked BEFORE the weak AUDIT keyword — otherwise a
    # reference head that merely CITES a designs/audit/ doc is false-demoted.
    for status in ('CANONICAL', 'DESIGN', 'REFERENCE', 'CURRENT', 'WORKING'):
        head = f'# Foo\n## Status: {status}\nScope: see the audit in designs/audit/x.md\n'
        assert va.banner_classify(head, 'designs/x_v30.md') == 'design', status


def test_provisional_status_is_design():
    assert va.banner_classify('## Status: PROVISIONAL\n', 'designs/x.md') == 'design'


def test_struck_and_deprecated_are_excluded():
    assert va.banner_classify('[STRUCK] retired\n', 'designs/x.md') == 'excluded'
    # a deprecated/ PATH is excluded even with no struck marker in the body
    assert va.banner_classify('# ordinary\n', 'deprecated/old.md') == 'excluded'


def test_deprecated_is_path_anchored_not_content_matched():
    # Fable-5 2026-07-14 audit (Obs-6): `deprecated/` is a PATH signal, checked in the
    # path ONLY. A LIVE design doc that merely CITES a deprecated/ path in its prose must
    # NOT be dropped. Mutation guard: reverting to `re.search('deprecated/', head+path)`
    # makes this doc 'excluded', which this test catches.
    body = '# Combat design\nNote: the old extractor at deprecated/tools/extract_values.py is retired.\n'
    assert va.banner_classify(body, 'designs/scene/combat.md') == 'design'
    # and the [STRUCK] content marker still works from the body
    assert va.banner_classify('[STRUCK] retired concept\n', 'designs/live_path.md') == 'excluded'


def test_workplan_and_audit_keywords_are_discourse_absent_status():
    # with no recognized status line, the AUDIT/WORKPLAN keyword demotes to discourse
    assert va.banner_classify('# Master WORKPLAN\n', 'workplans/x.md') == 'discourse'
    assert va.banner_classify('# Session AUDIT notes\n', 'designs/x.md') == 'discourse'


def test_audit_folder_path_is_discourse_but_dev_spec_is_design():
    assert va.banner_classify('# notes\n', 'designs/audit/2026/notes.md') == 'discourse'
    assert va.banner_classify(
        '# spec\n', 'designs/audit/2026/development_specification.md') == 'design'


# ── same_class equivalence predicate ────────────────────────────────────────

def test_same_class_groups_and_separates():
    # same_class underpins the "implied-missing" (Mode B) reasoning: two tokens of
    # the same class shouldn't be flagged as a cross-class gap. Two conviction axes
    # are same-class; a conviction axis and a faction are not.
    assert va.same_class('Faith', 'Order') is True          # both conviction
    assert va.same_class('Crown', 'Church') is True         # both faction
    assert va.same_class('Faith', 'Crown') is False         # conviction vs faction
    assert va.same_class('unlisted', 'alsounlisted') is False  # neither in any class


# ── silent-cap fix: Mode C/D record the TRUE total, not the shown slice ─────

def test_diagnostics_records_true_notional_total_not_just_shown_slice():
    # Fable-5 2026-07-14 audit, Obs-1: Mode C used to cap at [:25] with the true count
    # destroyed (scorecard read "25" as complete). It must now record C_notional_total.
    # Build a star cite-graph with >50 notional edges (no metadata graphs, so every cite
    # edge is notional) and assert the recorded total exceeds the shown (capped) list.
    n = 60
    toks = {f't{i}': {'paragraph_count': 1, 'status': 'design'} for i in range(n + 1)}
    cite = {'t0': {f't{i}': 1 for i in range(1, n + 1)}}   # t0 -> t1..t60, all notional
    graphs = {'cite': cite, 'throughline': {}, 'mu': {}, 'pp': {}}
    degs = {'cite': {'t0': n, **{f't{i}': 1 for i in range(1, n + 1)}},
            'throughline': {}, 'mu': {}, 'pp': {}}
    diag = va.diagnostics(toks, graphs, degs)
    assert diag['C_notional_total'] == n            # the TRUE count is recorded
    assert len(diag['C_notional']) <= 50            # the itemized list is capped
    assert diag['C_notional_total'] > len(diag['C_notional'])  # cap did not destroy the total
    assert 'D_cascade_sinks_total' in diag          # Mode D total side channel also present


# ── §8 reuse: the real names reader, not a re-parse ─────────────────────────

def test_name_coreference_unifies_one_entity_but_not_a_family():
    """Consolidation (2026-07-21, "unify and simplify … for names"): every surface form
    of ONE person collapses to a single token, but a shared DYNASTY surname must NOT merge
    distinct people."""
    import os
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    defs = va.derive_tokens(__import__('pathlib').Path(root))

    # (1) the Baralta family is ONE token, labelled by the registry canonical. Since the NPC
    #     roster is now sourced from names_index world.* (token_class: npc; R2/ED-IN-0082), the
    #     Duchess canonical is the surface token and the `baralta` canonical-sources system key
    #     folds in by registry-alias coreference.
    baralta = [n for n in defs if 'baralta' in n.lower()]
    assert len(baralta) == 1, baralta
    assert baralta[0] == 'Duchess Inge Baralta'
    merged = defs[baralta[0]].get('aliases_merged') or []
    assert {'Baralta', 'Duchess Inge Baralta'} <= set(merged)
    # the head pattern is the shared surname — "just search Baralta"
    assert defs[baralta[0]]['patterns'] == ['Baralta']

    # (2) the Almqvist ROYALS are distinct people, not one merged token; the House stands alone.
    royals = ['Prince Torben Almqvist', 'Princess Elske Almqvist', 'Queen Lenneth Almqvist']
    present = [r for r in royals if r in defs]
    assert len(present) >= 2, present                      # they survive as separate entities
    for r in present:
        assert 'Almqvist' not in (defs[r].get('aliases_merged') or []), r  # dynasty not folded in


def test_token_universe_is_expansive_across_entity_classes():
    """Jordan 2026-07-21: the token universe must span the whole ontology — mechanics,
    Keys/schema names, primitives, values, actions, places, and named entities — so the
    audit can surface how anything connects to everything."""
    import os
    from collections import Counter
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    defs = va.derive_tokens(__import__('pathlib').Path(root))
    scales = Counter(m.get('scale') for m in defs.values())
    # every ontology class the expansion added must be non-empty
    for cls in ('mechanic', 'key', 'primitive', 'value', 'action'):
        assert scales.get(cls, 0) > 0, (cls, dict(scales))
    # specific entities the expansion must reach
    names = set(defs)
    assert any('baralta' in n.lower() for n in names)               # consolidated NPC
    assert any(m.get('scale') == 'action' and n == 'Muster' for n, m in defs.items())
    assert 'Löwenritter' in names                                    # faction/order
    assert any('Key:' in n for n in names)                           # Key schema names
    assert len(defs) > 200                                           # genuinely expansive


def test_p2_v4_gated_presence_and_not_measurable_sentinel():
    """P2 v4 (ED-IN-0080, Jordan ruling A, 2026-07-21): conviction symmetry is measured on
    CONTEXT-GATED prose presence, not throughline degree (the v3 formulation was
    unsatisfiable by construction); an all-zero vector is NOT MEASURABLE, never cv=999."""
    convs = va.CLASSES['conviction']
    # (a) gated presence drives P2 even with an EMPTY throughline graph (deg_tl={})
    tokens = {c: {'paragraph_count': 40} for c in convs}
    v = va.validate(tokens, {}, {}, {'A': {'B': 1}})
    assert v['p2']['measure'] == 'context_gated_paragraphs'
    assert v['p2']['measurable'] is True and v['p2']['pass'] is True
    assert v['p2']['cv'] == 0.0
    # (b) a real spread beyond the (unchanged) 0.5 bar fails honestly
    tokens2 = {c: {'paragraph_count': (100 if i == 0 else 5)}
               for i, c in enumerate(convs)}
    v2 = va.validate(tokens2, {}, {}, {})
    assert v2['p2']['measurable'] is True and v2['p2']['pass'] is False
    # (c) all-zero => NOT MEASURABLE: cv is None (999 sentinel retired), never a pass
    tokens3 = {c: {'paragraph_count': 0} for c in convs}
    v3 = va.validate(tokens3, {}, {}, {})
    assert v3['p2']['measurable'] is False and v3['p2']['pass'] is False
    assert v3['p2']['cv'] is None


def test_token_classes_sourced_from_names_index_byte_identical():
    """R2 (ED-IN-0082, CLAUDE.md §8): the §3.5 disambiguation `context` AND the class rosters for
    the conviction + pressure_point classes moved OUT of vector_audit's hardcoded SEED_TOKENS INTO
    references/names_index.yaml (conv.* / ppt.* entries); vector_audit now builds them via
    names.by_category(<cls>). This pins the sourced tokens byte-identical to the former hardcoded
    blocks — so P2 (conviction symmetry) and the class taxonomy are provably unchanged. Reverting
    the sourcing, drifting a context term, or reordering the index roster breaks this."""
    EXPECTED = {
        'conviction': {
            'Faith':      [r'\bConviction\b', r'\bFramework\b', r'\bDivine\b', r'\bChurch\b',
                           r'\bCardinal\b', r'\bdoctrine\b'],
            'Order':      [r'\bConviction\b', r'\bFaith\b', r'\bAutonomy\b', r'\bReason\b', r'\bEquity\b'],
            'Reason':     [r'\bConviction\b', r'\bFaith\b', r'\bOrder\b', r'\bAutonomy\b'],
            'Equity':     [r'\bConviction\b', r'\bRestoration\b'],
            'Precedent':  [r'\bConviction\b', r'\bHafenmark\b', r'\blegal\b'],
            'Autonomy':   [r'\bConviction\b', r'\bVarfell\b', r'L[oö]wenritter'],
            'Continuity': [r'\bConviction\b', r'\bRestoration\b'],
        },
        'pressure_point': {
            'Evidence':    [r'\bPressure Point\b', r'\bInvestigation\b', r'\bEvidence Track\b'],
            'Consequence': [r'\bPressure Point\b', r'\bConsequentialist\b'],
            'Authority':   [r'\bPressure Point\b', r'\bAuthority Challenge\b', r'\binstitutional\b'],
            'Loyalty':     [r'\bPressure Point\b', r'\bKnot\b', r'\brelational\b'],
        },
    }
    import names
    for cls, members in EXPECTED.items():
        # roster order preserved (P2's per-conviction vector depends on it)
        assert va.CLASSES[cls] == list(members), (cls, va.CLASSES[cls])
        for disp, ctx in members.items():
            tok = va.SEED_TOKENS.get(disp)
            assert tok is not None, (cls, disp)
            assert tok['patterns'] == [r'\b' + disp + r'\b'], (cls, disp)
            assert tok['scale'] == cls, (cls, disp)
            assert tok['context'] == ctx, (cls, disp)
        # roster genuinely comes from the index (not a lingering hardcode)
        assert {m['canonical'] for m in names.by_category(cls).values()} == set(members)
    assert names.context('conv.order') == EXPECTED['conviction']['Order']
    assert names.context('ppt.loyalty') == EXPECTED['pressure_point']['Loyalty']

    # factions: sourced from names_index world.* (token_class: faction) with CUSTOM patterns
    # (negative lookaheads) — roster is order-independent (verified), so checked as a SET.
    FAC_PATS = {
        'Crown': [r'\bCrown\b(?! Treaty)'], 'Church': [r'\bChurch\b(?! Influence)'],
        'Hafenmark': [r'\bHafenmark\b'], 'Varfell': [r'\bVarfell\b'],
        'Löwenritter': [r'L[oö]wenritter'],
        'Restoration Movement': ['Restoration Movement', r'\bRM\b(?![a-z])'],
        'Guilds': [r'\bGuilds?\b'],
    }
    FAC_CTX = {'Crown': [r'\bAlmud\b', r'\bfaction\b', r'\bMandate\b', r'\bTreaty\b', r'\bTorben\b'],
               'Church': [r'\bArne\b', r'\bCardinal\b', r'\bPiety\b', r'\bHeresy\b', r'\bfaction\b',
                          r'\bConfessor\b', r'\bdoctrine\b']}
    assert set(va.CLASSES['faction']) == set(FAC_PATS)
    for disp, pats in FAC_PATS.items():
        tok = va.SEED_TOKENS.get(disp)
        assert tok is not None and tok['scale'] == 'faction', disp
        assert tok['patterns'] == pats, disp
        assert tok['context'] == FAC_CTX.get(disp, []), disp
    # sourced via token_class (a proper_noun that ALSO carries an audit class), not category
    assert {m['canonical'] for m in names.by_token_class('faction').values()} == set(FAC_PATS)
    assert names.canonical('world.guilds') == 'Guilds'   # world.guilds added + mirrored

    # mechanics: namespaced ids (mech.*) so a generic "Stability" is collision-safe from the
    # faction stat fac.stability. Sourced via token_class 'mech' with scale 'mechanic'.
    MECH = {'Disposition': [r'\bDisposition\b'], 'Standing': [r'\bStanding\b'],
            'Stability': [r'\bStability\b'], 'Mandate': [r'\bMandate\b'], 'Tensions': [r'\bTensions\b']}
    assert set(va.CLASSES.get('mech', [])) == set(MECH)
    for disp, pats in MECH.items():
        tok = va.SEED_TOKENS.get(disp)
        assert tok is not None and tok['scale'] == 'mechanic' and tok['patterns'] == pats, disp
    # the collision-safe id exists in the register, distinct from the faction stat
    assert names.canonical('mech.stability') == 'Stability' and names.canonical('fac.stability') == 'Stability'
    assert 'mech' in va._INDEX_TOKEN_CLASSES

    # clocks (abbreviations): namespaced clock.* (token_class 'clock'); the 2 full-name clock
    # entries are tagged token_class 'clock_full' so the roster stays the 6 abbreviations.
    CLK = {'MS': [r'\bMS\b(?![A-Za-z])', 'Mending Stability'], 'CI': [r'\bCI\b(?![A-Za-z])', 'Church Influence'],
           'IP': [r'\bIP\b(?![A-Za-z])', 'Invasion Pressure'], 'PI': [r'\bPI\b(?![A-Za-z])', 'Political Instability'],
           'TS': [r'\bTS\b(?![A-Za-z])', 'Thread Sensitivity'], 'TCV': [r'\bTCV\b']}
    assert set(va.CLASSES['clock']) == set(CLK)
    for disp, pats in CLK.items():
        tok = va.SEED_TOKENS.get(disp)
        assert tok is not None and tok['scale'] == 'clock' and tok['patterns'] == pats, disp
    assert names.canonical('clock.ms') == 'MS' and 'clock' in va._INDEX_TOKEN_CLASSES

    # NPCs: sourced from names_index world.* (token_class 'npc') with FIRST-NAME / TITLE patterns
    # — the shared `Almqvist` dynasty surname is deliberately dropped so distinct royals never
    # collide on it (Jordan 2026-07-22), and the shared `Magnus` first name is dropped from the
    # Duke (unique on `Vaynard`; `Magnus` also names Cardinal Klapp). Sourced by canonical full
    # form; scale defaults to the token_class ('npc').
    NPC = {
        'King Almud Almqvist':        [r'\bAlmud\b'],
        'Prince Torben Almqvist':     [r'\bTorben\b'],
        'Princess Elske Almqvist':    [r'\bElske\b'],
        'Queen Lenneth Almqvist':     [r'\bLenneth\b'],
        'Duchess Inge Baralta':       [r'\bBaralta\b'],
        'Duke Magnus Vaynard':        [r'\bVaynard\b'],
        'Confessor Arne Himlensendt': [r'\bArne\b', r'\bHimlensendt\b', r'\bConfessor\b'],
        'Yrsa Vossen':                [r'\bYrsa\b', r'\bVossen\b'],
        'Edeyja':                     [r'\bEdeyja\b'],
        'Grandmaster Ehrenwall':      [r'\bEhrenwall\b', r'\bLisbeth\b'],
    }
    assert set(va.CLASSES['npc']) == set(NPC)
    for disp, pats in NPC.items():
        tok = va.SEED_TOKENS.get(disp)
        assert tok is not None and tok['scale'] == 'npc' and tok['patterns'] == pats, disp
    # the dropped-surname invariant: no NPC pattern matches the bare dynasty name
    assert not any('Almqvist' in p for pats in NPC.values() for p in pats)
    # sourced via token_class (proper_noun entries that ALSO carry the audit npc class)
    assert {m['canonical'] for m in names.by_token_class('npc').values()} == set(NPC)

    # SOURCING-LINKAGE guard (adversarial-pass hardening): the classes are actually driven through
    # the names_index sourcing loop, so a revert that re-hardcodes identical dicts but drops the
    # sourcing is caught, not just a value-identical pass.
    assert set(EXPECTED) | {'faction', 'mech', 'clock', 'npc'} <= set(va._INDEX_TOKEN_CLASSES)


def test_vector_audit_reuses_the_real_names_reader():
    # Fable-5 finding: §8 "every rule lives once" — vector_audit must import the
    # real tools/names.py, not re-parse names_index.yaml with a private matcher.
    import importlib
    real_names = importlib.import_module('names')
    assert va.names is real_names


def test_corpus_layer_L1_extends_L0_corpus_breadth():
    """`--layer L1` extends the audit's trace from the curated canonical slice (L0, ~6%) to the
    whole design tree — the corpus-breadth direction (the CITE graph only; NOT tl/mu, which are
    registry-derived, nor the token universe). L0 stays the validated default and its DOC SET is a
    strict subset of L1's. NOTE: only the doc set is a guaranteed superset — derived graphs/edges
    are not monotone (a token's primary_doc can shift under the wider corpus), which is why the
    narrative arcs/ tree is excluded from L1 (would pollute cite with story co-mention)."""
    import os
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from pathlib import Path
    d0, _, m0 = va.extract_corpus(Path(root), layer='L0')
    d1, _, m1 = va.extract_corpus(Path(root), layer='L1')
    assert m0['layer'] == 'L0' and m1['layer'] == 'L1'
    assert len(d1) > len(d0), (len(d0), len(d1))            # L1 genuinely extends coverage
    assert set(d0) <= set(d1)                               # strict superset — L0 not narrowed
    assert m1['coverage']['pct_of_repo_md'] > m0['coverage']['pct_of_repo_md']
    # default is L0 (validated scope preserved)
    d_def, _, m_def = va.extract_corpus(Path(root))
    assert m_def['layer'] == 'L0' and set(d_def) == set(d0)


def test_discover_unregistered_candidates_surfaces_missing_registrations():
    """The token universe is registry-derived, so a design term never registered is invisible to
    the whole audit. discover_unregistered_candidates surfaces frequent authored terms the central
    ontology does NOT know — candidate missing registrations. Post adversarial-pass: the known-set
    is NAME-LEVEL (tokens/modules/descriptors/graph nodes, article/title-folded), NOT a substring
    match — so it neither drops multi-word extensions of a registered head-word nor re-surfaces
    concepts other scanners carry, and there is NO hard top-N cap (churn-proof)."""
    import os
    from pathlib import Path
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    cands = va.discover_unregistered_candidates(root, min_docs=12)
    assert isinstance(cands, list) and cands, 'should surface at least some unregistered terms'
    terms = {c['term'] for c in cands}
    # a term the ontology KNOWS must NOT be surfaced — incl. article/title/plural surface-forms
    # (the false-positive classes the adversarial pass caught) and cross-scanner-known concepts.
    for known_surface in ('Faith', 'Conviction', 'The Church', 'The Crown', 'The Leap',
                          'Domain Action', 'Game Master', 'Player Character', 'Crusader Kings',
                          'Magnus Vaynard'):
        assert known_surface not in terms, known_surface
    # a multi-word EXTENSION of a registered head-word must NOT be blanket-dropped (the false-neg
    # the substring predicate caused): "Combat Pool"/"Church Mandate" extend Combat/Church but are
    # distinct unregistered concepts — at least one such head-word extension should survive.
    assert any(' ' in t and t.split()[0] in {'Combat', 'Church', 'Crown', 'Thread'} for t in terms)
    # each carries a doc back-link + meets the floor
    for c in cands[:10]:
        assert c['docs'] >= 12 and c.get('top_docs'), c
    # deterministic total order, no cap (floor is the only cutoff)
    assert cands == sorted(cands, key=lambda r: (-r['docs'], -r['total'], r['term']))


def test_throughline_graph_extended_by_second_registry_source():
    """Directions-audit #3: the throughline graph draws from TWO registries now — the meta table
    (parse_throughlines) + throughlines_complete.md's `### T-NN:` block `Systems:` lines
    (parse_throughlines_complete), same co-membership relation, broader coverage. The extra source
    must genuinely ADD edges (measured net-positive: it surfaces more structure, doesn't shrink it),
    and `extra_rows=None` must reproduce the meta-only graph exactly (opt-in, no silent behavior
    change for callers that don't pass it). The μ graph is NOT extended (this source has no Μ data).
    SCOPE + BLOCK-COVERAGE (adversarial pass): the parser reads the WHOLE doc (NOT just §VIII
    post-atomization) and must catch letter-suffixed headers (T-15b/T-15c) while skipping the STRUCK
    Chain-less T-10 without bleeding its match into T-11."""
    import os
    from pathlib import Path
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    defs = va.derive_tokens(root)
    design = va.extract_corpus(root, 'L0')[0]
    tokens, _ = va.curate_tokens(design, defs)
    meta = va.parse_throughlines(root)
    extra = va.parse_throughlines_complete(root)
    assert extra, 'complete-doc Systems lines should parse'
    assert all(len(r) == 4 and r[1] == '' and r[2] == '' for r in extra)   # shape matches; no μ
    tids = [r[0] for r in extra]
    # scope honesty: it reads the WHOLE doc, so main-section throughlines (T-01..T-30) are present,
    # not only the post-atomization T-31..T-41 — the exact mislabel the adversarial pass caught.
    assert 'T-04' in tids and 'T-31' in tids, tids
    assert any(t.startswith('T-') and int(t[2:].rstrip('abcdefghij')) <= 30 for t in tids)
    # block-coverage: letter-suffixed headers caught; STRUCK T-10 (no Systems line) skipped
    assert 'T-15b' in tids and 'T-15c' in tids, tids
    assert 'T-11' in tids and 'T-10' not in tids, tids   # T-10 STRUCK must not bleed into T-11
    assert tids == sorted(set(tids), key=tids.index) and len(tids) == len(set(tids))  # no dup labels
    g_base = va.build_g_throughline(meta, tokens)
    g_ext = va.build_g_throughline(meta, tokens, extra_rows=extra)
    edges = lambda g: {frozenset((a, b)) for a in g for b in g[a]}
    e_base, e_ext = edges(g_base), edges(g_ext)
    assert e_base < e_ext, (len(e_base), len(e_ext))       # strictly more edges, none lost
    # opt-in: no extra_rows reproduces meta-only exactly (callers unaffected unless they pass it)
    assert edges(va.build_g_throughline(meta, tokens, extra_rows=None)) == e_base


def test_key_propagation_graph_wires_engine_dataflow_and_resolves_key_isolates():
    """Direction #5 (answers 'why not key propagation too'): build_g_key reads module_contracts.yaml's
    emit→consume flow — the engine's actual IN→resolver→OUT wiring — as a 5th structural graph. It
    must (a) connect systems that share a Key (A emits, B consumes), (b) connect a Key-TYPE token to
    the systems that emit/consume it — which un-isolates Key tokens the design CITATION graph can't
    see — while (c) leaving a Key with no CONSUMER isolated (a real finding: an orphan/dangling emit —
    emitted but consumed by nothing — NOT an un-emitted Key; corrected after an adversarial pass),
    and (d) be deterministic. This is what lets the emit DELETE its old Key-token isolate filter."""
    import os, json
    from pathlib import Path
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    defs = va.derive_tokens(root)
    design = va.extract_corpus(root, 'L0')[0]
    tokens, _ = va.curate_tokens(design, defs)
    g_key = va.build_g_key(root, tokens)
    assert g_key, 'key graph should be non-empty (module_contracts has emit/consume flow)'
    names = list(tokens)
    kdeg = va._degrees(g_key, names)
    # (a) a system heavily wired in the engine has real key-degree; (b) a wired Key-type token too
    assert kdeg.get('Faction State', 0) > 5, kdeg.get('Faction State')
    assert kdeg.get('Key: mechanical.scene_exited', 0) >= 1   # was a filtered "false" isolate before
    # (d) determinism — identical across two builds
    canon = lambda g: json.dumps({k: dict(sorted(v.items())) for k, v in sorted(g.items())})
    assert canon(g_key) == canon(va.build_g_key(root, tokens))
    # folding key into diagnostics resolves the wired Key-tokens as Mode-H isolates but NOT the
    # ones with no consumer (orphan/dangling emits stay surfaced — SURFACE-NEVER-CULL).
    rows = va.parse_throughlines(root)
    graphs = {'cite': va.build_g_cite(tokens, design),
              'throughline': va.build_g_throughline(rows, tokens,
                                                    extra_rows=va.parse_throughlines_complete(root)),
              'mu': va.build_g_mu(rows, tokens), 'pp': va.build_g_pp(root, tokens), 'key': g_key}
    degs = {k: va._degrees(graphs[k], names) for k in graphs}
    iso = {r['token'] for r in va.diagnostics(tokens, graphs, degs)['H_isolates']}
    assert 'Key: mechanical.scene_exited' not in iso   # resolved by the key graph, not filtered
    # scene_outcome.battle_concluded IS emitted by mass_battle (module_contracts.yaml:473) but
    # consumed by NOTHING — an orphan/dangling emit (deg 1, not 0). Stays isolated, surfaced honestly.
    assert 'Key: scene_outcome.battle_concluded' in iso
    assert kdeg.get('Key: scene_outcome.battle_concluded', 0) == 1  # emitted-once, not un-emitted


def test_key_graph_does_not_diverge_from_authoritative_engine_graph():
    """§8 DRIFT GUARD (fix #7): build_g_key re-reads module_contracts emit/consume that
    tools/observability/build_graph.py already owns — a second parser. They are deliberately DIFFERENT
    projections (build_graph normalizes types via the Key Type Registry + resolve_key; build_g_key
    uses raw types at token granularity), so they can't share one kernel without changing outputs.
    The real §8 hazard is SILENT DIVERGENCE — so pin the invariant instead: build_g_key's
    system↔system edges must be a SUBSET of build_graph's authoritative graph (graph.json). The token
    projection may be NARROWER (build_graph adds registry-declared edges) but must never claim
    connectivity the engine graph denies. If this fails, the two observatories drifted OR graph.json
    is stale vs module_contracts — either way a human reconciles."""
    import os, json
    from pathlib import Path
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    gpath = root / 'tools' / 'observability' / 'graph.json'
    if not gpath.exists():
        import pytest
        pytest.skip("graph.json not generated")
    g = json.loads(gpath.read_text())
    # build_graph's authoritative system↔system edges: for each key, emitters × consumers
    from collections import defaultdict
    emit, cons = defaultdict(set), defaultdict(set)
    for e in g.get('edges', []):
        if e.get('kind') == 'emits':
            emit[e['dst']].add(e['src'])          # dst=key, src=system
        elif e.get('kind') == 'consumes':
            cons[e['src']].add(e['dst'])          # src=key, dst=system
    bg_pairs = set()
    for k in set(emit) | set(cons):
        for a in emit.get(k, ()):
            for b in cons.get(k, ()):
                if a != b:
                    bg_pairs.add(frozenset((a, b)))   # module-name pairs
    # build_g_key's system↔system edges (drop keytype↔system edges — those touch a 'Key:' token)
    defs = va.derive_tokens(root)
    design = va.extract_corpus(root, 'L0')[0]
    tokens, _ = va.curate_tokens(design, defs)
    lut, norm = va._slug_lookup(tokens)
    gk = va.build_g_key(root, tokens)
    # map build_graph module names → tokens so the two are comparable
    bg_tok_pairs = set()
    for pr in bg_pairs:
        a, b = tuple(pr)
        ta, tb = lut.get(norm(a)), lut.get(norm(b))
        if ta and tb and ta != tb:
            bg_tok_pairs.add(frozenset((ta, tb)))
    gk_sys_pairs = {frozenset((a, b)) for a in gk for b in gk[a]
                    if not a.startswith('Key:') and not b.startswith('Key:') and a != b}
    # the invariant: no build_g_key system edge is absent from the authoritative graph
    spurious = gk_sys_pairs - bg_tok_pairs
    assert not spurious, (f"build_g_key claims {len(spurious)} system↔system edge(s) the authoritative "
                          f"engine graph (graph.json) does not — drift or stale graph.json: "
                          f"{sorted(tuple(sorted(p)) for p in spurious)[:5]}")


def test_emit_findings_surfaces_never_culls_and_backlinks(tmp_path):
    """SURFACE-NEVER-CULL (SKILL.md doctrine): the structural-findings feed must EMIT every Mode-B
    and Mode-H finding — lower-confidence ones (hub×hub pairs, Key-token isolates) are RETAINED with
    a `filtered`+`filter_reason` flag, never dropped. And every finding must link SOMEWHERE: an
    implied-missing row carries a_doc/b_doc, an isolate carries `registry` (the register defining a
    term with no design-prose home). This is the anti-cull invariant an adversarial pass restored."""
    import os, json
    from pathlib import Path
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    out = tmp_path / 'findings.json'
    va.emit_structural_findings(root, out)
    d = json.loads(out.read_text())
    assert d['schema_version'] == 2                      # the handshake the ledger validates
    im, iso = d['implied_missing'], d['isolates']
    assert im and iso
    # every row carries the flag pair (present, typed) — nothing is silently dropped
    for r in im + iso:
        assert 'filtered' in r and isinstance(r['filtered'], bool)
        # a flagged row MUST explain itself; an unflagged row has no reason
        assert (r['filter_reason'] is not None) == r['filtered']
    # navigability: an implied-missing row links to at least one real doc; an isolate to a registry
    for r in im:
        assert (r.get('a_doc') or r.get('b_doc')), r
    for r in iso:
        assert r.get('registry') or r.get('doc'), r     # no orphan row
        # a kept (unfiltered) isolate is genuinely marooned: max degree <=1 (Mode-H invariant)
        if not r['filtered']:
            assert r['max_deg'] <= 1, r
    # ALL EIGHT modes present (fix #1 — the feed used to carry only B + H). C/D are high-volume, so
    # they carry a bounded sample + a TRUE _total (SURFACE-NEVER-CULL: never a silent cap).
    for key in ('notional', 'cascade_sinks', 'sparse_context', 'throughline_orphans', 'vocab_debt'):
        assert key in d, key
    assert d['notional_total'] >= len(d['notional'])         # sample ≤ true total, total disclosed
    assert d['cascade_sinks_total'] >= len(d['cascade_sinks'])
    assert 'cascade_truncated_calls' in d                    # the false-sink caveat is carried
