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
import re
import pytest

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
    # Build a star cite-graph with >100 notional edges (no metadata graphs, so every cite
    # edge is notional) and assert the recorded total exceeds the shown (capped) list.
    # (Cap raised 50→100 2026-07-23 after an adversarial pass; the total-preservation invariant
    # this test guards is unchanged.)
    n = 130
    toks = {f't{i}': {'paragraph_count': 1, 'status': 'design'} for i in range(n + 1)}
    cite = {'t0': {f't{i}': 1 for i in range(1, n + 1)}}   # t0 -> t1..t130, all notional
    graphs = {'cite': cite, 'throughline': {}, 'mu': {}, 'pp': {}}
    degs = {'cite': {'t0': n, **{f't{i}': 1 for i in range(1, n + 1)}},
            'throughline': {}, 'mu': {}, 'pp': {}}
    diag = va.diagnostics(toks, graphs, degs)
    assert diag['C_notional_total'] == n            # the TRUE count is recorded
    assert len(diag['C_notional']) <= 100           # the itemized list is capped
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


@pytest.mark.slow
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


@pytest.mark.slow
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
    # scene_outcome.battle_concluded was DELETED from mass_battle.emits 2026-07-29 (ED-MB-0010,
    # plan-v2 E1): it was the family name of scene.battle_concluded, never a Key. Recurrence
    # guard — if the fabricated emit reappears in module_contracts, its key-degree goes back to
    # ≥1 and this fails. (Mutation-verified: re-adding the row flips this red.)
    assert kdeg.get('Key: scene_outcome.battle_concluded', 0) == 0


@pytest.mark.slow
def test_key_graph_matches_an_independent_rederivation_from_contracts():
    """§8 DRIFT GUARD (fix #7, rewritten after an adversarial pass). The first cut only subset-checked
    the 40 system↔system edges against build_graph's graph.json — it EXCLUDED the 128 keytype↔system
    edges build_g_key exists to compute (a bad _keytype_token → false isolate went unguarded), a subset
    check can't catch build_g_key going too NARROW (the dangerous drift for an isolate hunter), and it
    depended on graph.json being co-fresh with module_contracts. This rewrite instead validates
    build_g_key against an INDEPENDENT re-derivation straight from module_contracts.yaml — ALL edges,
    EQUALITY (catches both spurious and missing edges), no graph.json dependency. The keytype
    correspondence is checked by TOKEN NAME (a 'Key: <type>' token ↔ the contract type), independent of
    _keytype_token's regex, so a regex bug shows up as a diff."""
    import os
    import yaml
    from pathlib import Path
    from collections import defaultdict
    root = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    defs = va.derive_tokens(root)
    design = va.extract_corpus(root, 'L0')[0]
    tokens, _ = va.curate_tokens(design, defs)
    lut, norm = va._slug_lookup(tokens)
    mc = yaml.safe_load((root / 'references' / 'module_contracts.yaml').read_text())
    # Key-type tokens indexed by the dotted type in their name ('Key: mechanical.scene_exited' → type)
    keytok_by_type = {}
    for name in tokens:
        if name.startswith('Key:'):
            keytok_by_type[name.split('Key:', 1)[1].strip()] = name
    emit, cons, modtok = defaultdict(set), defaultdict(set), {}
    for m in mc.get('modules', []):
        n = m.get('module')
        if n and norm(n) in lut:
            modtok[n] = lut[norm(n)]
        for e in m.get('emits') or []:
            if isinstance(e, dict) and e.get('type'):
                emit[e['type']].add(n)
        for c in m.get('consumes') or []:
            if isinstance(c, dict) and c.get('type'):
                cons[c['type']].add(n)
    expected = set()
    for t in set(emit) | set(cons):
        if t == '*':
            continue
        es, cs = emit.get(t, set()), cons.get(t, set())
        for a in es:                                   # system↔system: emitter × consumer
            for b in cs:
                if modtok.get(a) and modtok.get(b) and modtok[a] != modtok[b]:
                    expected.add(frozenset((modtok[a], modtok[b])))
        kt = keytok_by_type.get(t)                     # keytype↔system: by NAME, not the regex
        if kt:
            for s in es | cs:
                if modtok.get(s):
                    expected.add(frozenset((kt, modtok[s])))
    gk = va.build_g_key(root, tokens)
    actual = {frozenset((a, b)) for a in gk for b in gk[a] if a != b}
    spurious = actual - expected      # build_g_key claims an edge the contracts don't support
    missing = expected - actual       # build_g_key MISSES an edge the contracts declare (→ false isolate)
    assert not spurious, f"build_g_key has {len(spurious)} edge(s) not in module_contracts: {sorted(tuple(sorted(p)) for p in spurious)[:5]}"
    assert not missing, f"build_g_key MISSES {len(missing)} contract edge(s) (too narrow → false isolates): {sorted(tuple(sorted(p)) for p in missing)[:5]}"


def test_cascade_mode_d_is_deterministic_across_neighbor_order():
    """Mode D (cascade sinks) does a return-path DFS under a traversal cap; a capped search's answer
    depends on VISIT ORDER, so iterating hash-randomized set() adjacency made it churn across runs
    (adversarial pass HIGH). The fix sorts adjacency. This pins order-independence: run diagnostics on
    the SAME cite graph with each node's neighbor dict in two different insertion orders and assert the
    Mode-D output is identical. A regression to set()-typed adjacency would make these differ."""
    def _tok(names):
        return {n: {'paragraph_count': 3, 'status': 'canonical', 'primary_doc': 'd.md',
                    'patterns': [n], 'source': 'seed'} for n in names}
    # a graph with cascade structure: A→B→C→D→B (B..D loop, A feeds in, no path back to A)
    fwd = {'A': {'B': 1}, 'B': {'C': 1}, 'C': {'D': 1}, 'D': {'B': 1}}
    rev = {k: dict(reversed(list(v.items()))) for k, v in reversed(list(fwd.items()))}
    def run(cite):
        toks = _tok(['A', 'B', 'C', 'D'])
        graphs = {'cite': cite, 'throughline': {}, 'mu': {}, 'pp': {}, 'key': {}}
        names = list(toks)
        degs = {k: va._degrees(graphs[k], names) for k in graphs}
        return va.diagnostics(toks, graphs, degs)
    a, b = run(fwd), run(rev)
    assert a['D_cascade_sinks'] == b['D_cascade_sinks'], (a['D_cascade_sinks'], b['D_cascade_sinks'])
    assert a['D_cascade_truncated_calls'] == b['D_cascade_truncated_calls']


def test_every_emitted_ledger_category_has_an_explicit_severity():
    """Fix #4 gate (added after an adversarial pass flagged it ungated): finding() defaults an
    unmapped category to 'med' silently, so a NEW scanner category would ship unranked and nobody would
    notice. Pin it — every category the ledger actually emits must be in the SEVERITY map explicitly."""
    import importlib.util, os
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    spec = importlib.util.spec_from_file_location(
        'build_incompleteness', os.path.join(root, 'tools', 'observability', 'build_incompleteness.py'))
    bi = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bi)
    emitted = {f['category'] for f in bi.build()['findings']}
    unmapped = emitted - set(bi.SEVERITY)
    assert not unmapped, f"categories emitted but missing from SEVERITY (silently default med): {sorted(unmapped)}"


@pytest.mark.slow
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


# ═══════════════════════════════════════════════════════════════════════════
# OI-55 / ED-IN-0092 (G12 correction): the register claimed vector_audit's
# "analytical core has no known-answer coverage beyond one total-pin". That
# claim was already stale for banner_classify/diagnostics/build_g_key/etc
# (see the tests above), but a genuine set of pure analytical functions had
# ZERO direct known-answer coverage — exercised only as plumbing inside other
# tests (if at all), never verified against a hand-computed expected output.
# Every test below was hand-traced against the function's source before being run once. Not all
# are the same guarantee, though: _median / _percentile_10_cut / _top_quintile / validate P1 /
# validate P3 / vocabulary_debt are concept-derivable (expected value comes from the spec, not the
# code) — true known-answer tests where a wrong implementation would fail. _source_rank's default,
# _pattern_for's boundary case, and _humanize_system's lookup table are source-traced (hand-computed
# FROM the function's current source) — regression guards against future drift, not proof of
# current correctness.
# ═══════════════════════════════════════════════════════════════════════════
#
# Already-covered map (function → pre-existing test), assembled so this claim is auditable
# in-tree rather than asserted from memory:
#   same_class                              -> test_same_class_groups_and_separates
#   banner_classify                         -> the 6 banner/status tests (test_status_declaration_
#                                               is_design_even_with_audit_word, test_provisional_
#                                               status_is_design, test_struck_and_deprecated_are_
#                                               excluded, test_deprecated_is_path_anchored_not_
#                                               content_matched, test_workplan_and_audit_keywords_
#                                               are_discourse_absent_status, test_audit_folder_path_
#                                               is_discourse_but_dev_spec_is_design)
#   diagnostics C/D totals + determinism    -> test_diagnostics_records_true_notional_total_not_
#                                               just_shown_slice, test_cascade_mode_d_is_
#                                               deterministic_across_neighbor_order
#   validate p2                             -> test_p2_v4_gated_presence_and_not_measurable_sentinel
#   derive_tokens/consolidate_tokens        -> test_name_coreference_unifies_one_entity_but_not_a_
#     (real-corpus)                            family, test_token_universe_is_expansive_across_
#                                               entity_classes
#   CLASSES/SEED_TOKENS sourcing            -> test_token_classes_sourced_from_names_index_byte_
#                                               identical
#   names reuse                             -> test_vector_audit_reuses_the_real_names_reader
#   extract_corpus L0/L1                    -> test_corpus_layer_L1_extends_L0_corpus_breadth
#   build_g_key                             -> test_key_graph_matches_an_independent_rederivation_
#                                               from_contracts (the contracts rederivation test)
#   build_g_throughline                     -> test_throughline_graph_extended_by_second_registry_
#                                               source
#   discover_unregistered_candidates        -> test_discover_unregistered_candidates_surfaces_
#                                               missing_registrations
# ═══════════════════════════════════════════════════════════════════════════

def test_median_known_answer():
    # xs=sorted; odd->middle element, even->mean of the two middle, empty->0.0 (not an exception)
    assert va._median([]) == 0.0
    assert va._median([3, 1, 2]) == 2                # odd: middle of [1,2,3]
    assert va._median([4, 1, 3, 2]) == 2.5            # even: mean of [2,3]
    assert va._median([7]) == 7


def test_percentile_10_cut_known_answer():
    # xs=sorted; index = max(0, int(0.10*n) - 1). n=10 -> int(1.0)-1=0 -> xs[0].
    # n=20 -> int(2.0)-1=1 -> xs[1]. n<10 -> int(...) truncates to 0 -> max(0,-1)=0 -> xs[0].
    assert va._percentile_10_cut([]) == 0
    assert va._percentile_10_cut(list(range(1, 11))) == 1     # n=10: xs[0]
    assert va._percentile_10_cut([5, 3, 1, 4, 2]) == 1        # n=5:  xs[0]
    assert va._percentile_10_cut(list(range(1, 21))) == 2     # n=20: xs[1] (the int() truncation edge)
    assert va._percentile_10_cut([1, 2, 3]) == 1


def test_top_quintile_known_answer():
    # k = max(1, len//5); cut = the k-th largest value; membership requires d>=cut AND d>0
    # (the d>0 guard is the case a naive "top 20%" reading would miss on an all-zero graph).
    deg10 = {c: 11 - i for i, c in enumerate('abcdefghij')}   # a=11..j=2, i.e. 10 distinct values
    assert va._top_quintile(deg10) == {'a', 'b'}              # k=2, cut=vals[1]=10 -> a(11),b(10)
    assert va._top_quintile({}) == set()
    assert va._top_quintile({'x': 5, 'y': 5, 'z': 1}) == {'x', 'y'}   # tie at the cut both included
    assert va._top_quintile({'a': 0, 'b': 0}) == set()        # all-zero: d>0 guard excludes everyone


def test_add_edge_known_answer():
    g = {}
    va._add_edge(g, 'A', 'B')
    assert g == {'A': {'B': 1}, 'B': {'A': 1}}          # symmetric, weight 1 on first insert
    va._add_edge(g, 'A', 'B')
    assert g == {'A': {'B': 2}, 'B': {'A': 2}}          # weight increments on repeat, both sides
    va._add_edge(g, 'A', 'A')
    assert g == {'A': {'B': 2}, 'B': {'A': 2}}          # self-loop is a no-op (a==b guard)


def test_neighbors_union_and_degrees_known_answer():
    graph = {'A': {'B': 1, 'C': 1}, 'D': {'A': 1}}
    assert va.neighbors_union(graph, 'A') == {'B', 'C', 'D'}   # out {B,C} union in {D} (D->A)
    assert va.neighbors_union(graph, 'B') == {'A'}             # no out-edges; in-edge from A
    assert va.neighbors_union(graph, 'Z') == set()             # absent node: empty union
    g2 = {'A': {'B': 1, 'C': 1}, 'C': {'A': 1}}
    assert va._degrees(g2, ['A', 'B', 'C', 'D']) == {'A': 2, 'B': 1, 'C': 1, 'D': 0}


def test_to_paragraphs_strips_comments_code_and_filters_short_blocks():
    para1 = 'A' * 60          # > 50 chars: kept
    para2 = 'B' * 10          # <= 50 chars: dropped
    para3 = 'C' * 55          # > 50 chars: kept
    content = (f'<!-- hidden comment text -->\n{para1}\n\n{para2}\n\n'
               f'```\nZZZ code block ZZZ\n```\n\n{para3}\n')
    result = va.to_paragraphs(content)
    assert result == [para1, para3]      # comment vanishes, code block vanishes, short block dropped


def test_compiled_falls_back_to_escaped_literal_on_invalid_regex():
    out = va._compiled(['abc', '('])     # '(' is an invalid regex (unbalanced group)
    assert len(out) == 2
    assert out[0].search('xxabcxx')                 # 'abc' compiled normally, matches as a regex
    assert out[1].search('a(b')                      # '(' fell back to re.escape -> matches the literal char
    assert not out[1].search('abc')                  # ...and does NOT match unrelated text


def test_count_in_sums_matches_across_patterns():
    comp = [re.compile(r'\bfoo\b'), re.compile(r'\bbar\b')]
    assert va._count_in('foo bar foo baz bar bar', comp) == 5   # 2 foo + 3 bar


def test_norm_name_known_answer():
    assert va._norm_name('Duchess Inge Baralta') == 'duchess inge baralta'
    assert va._norm_name('Restoration-Movement!!') == 'restoration movement'   # punctuation -> space, stripped
    assert va._norm_name(None) == ''
    assert va._norm_name('  MiXed_CASE_123  ') == 'mixed case 123'


def test_to_native_converts_container_types():
    out = va.to_native({'a': [1, 2, (3, 4)], 'b': {'c'}})
    assert out == {'a': [1, 2, [3, 4]], 'b': ['c']}     # tuple->list recursively; single-elem set->list
    assert isinstance(out['a'][2], list) and not isinstance(out['a'][2], tuple)


def test_strip_display_known_answer():
    # (bare label, abbreviation|None); markdown bold stripped; only an UPPERCASE-led trailing
    # parenthetical yields an abbreviation, but ANY trailing parenthetical is stripped from the label.
    assert va._strip_display('**Restoration Movement** (RM)') == ('Restoration Movement', 'RM')
    assert va._strip_display('**Solmund**') == ('Solmund', None)
    assert va._strip_display('Some Term (lowercase)') == ('Some Term', None)   # lowercase paren: no abbr
    assert va._strip_display(None) == ('', None)


def test_pattern_for_known_answer():
    # empty label -> []; short (<=6 chars) single word -> word-boundary anchored;
    # a space OR length>6 -> plain phrase (no \b); an abbr always gets its own \b-anchored pattern.
    assert va._pattern_for('') == []
    pats_short = va._pattern_for('Faith')          # 5 chars, no space -> word-boundary
    assert re.fullmatch(pats_short[0], 'Faith') and not re.search(pats_short[0], 'Faithful')
    pats_phrase = va._pattern_for('Restoration Movement')   # has a space -> plain phrase, no \b required
    assert re.search(pats_phrase[0], 'the Restoration Movement grows')
    pats_long = va._pattern_for('Longerword')      # 10 chars, no space, > 6 -> plain (no \b)
    assert len(pats_long) == 1 and re.search(pats_long[0], 'xLongerwordx')
    pats_boundary6 = va._pattern_for('Faithy')      # exactly 6 chars -> still word-boundary
    assert not re.search(pats_boundary6[0], 'Faithyz')
    pats_with_abbr = va._pattern_for('MS', 'Mending')
    assert len(pats_with_abbr) == 2
    assert re.fullmatch(pats_with_abbr[0], 'MS') and re.fullmatch(pats_with_abbr[1], 'Mending')


def test_humanize_system_known_answer():
    assert va._humanize_system('mass_battle_npc') == 'Mass Battle'   # trailing _npc stripped
    assert va._humanize_system('ci_political') == 'CI Political'     # 'Ci' restored to acronym 'CI'
    assert va._humanize_system('ui_ux_spec') == 'UI UX Spec'         # two acronyms in one label
    assert va._humanize_system('threadwork') == 'Threadwork'         # no acronym, plain title-case


def test_source_rank_known_answer():
    assert va._source_rank('derived:proper_noun') == 0
    assert va._source_rank('seed') == 1
    assert va._source_rank('derived:names_index') == 2
    assert va._source_rank('derived:canonical_sources') == 3
    assert va._source_rank('unknown_source') == 4     # unmapped source: the documented default
    assert va._source_rank(None) == 4


def test_passes_context_known_answer():
    assert va._passes_context('anything at all', []) is True          # no context requirement: always passes
    ctx = [re.compile(r'\bChurch\b')]
    assert va._passes_context('The Church is powerful', ctx) is True
    assert va._passes_context('The Crown is powerful', ctx) is False
    ctx2 = [re.compile(r'\bFoo\b'), re.compile(r'\bBar\b')]
    assert va._passes_context('contains Bar only', ctx2) is True       # ANY pattern matching passes


def test_consolidate_tokens_substring_signal_merges_unique_container_not_shared_surname():
    """Signal 2 (proper-noun substring, NAME scales only): a short form contained in exactly ONE
    longer name merges (Baralta -> Duchess Inge Baralta); a short form contained in MULTIPLE longer
    names is a shared dynasty surname and must NOT merge anyone (Almqvist stays standalone, the two
    royals stay separate). Non-name-scale tokens (Combat / Mass Combat) never trigger this signal."""
    token_defs = {
        'Baralta':               {'patterns': ['Baralta'], 'scale': 'npc',
                                  'source': 'derived:canonical_sources'},
        'Duchess Inge Baralta':  {'patterns': ['Duchess Inge Baralta'], 'scale': 'npc',
                                  'source': 'derived:proper_noun'},
        'King Almud Almqvist':   {'patterns': ['Almud'], 'scale': 'npc', 'source': 'seed'},
        'Prince Torben Almqvist': {'patterns': ['Torben'], 'scale': 'npc', 'source': 'seed'},
        'Almqvist':              {'patterns': ['Almqvist'], 'scale': 'npc', 'source': 'seed'},
        'Combat':                {'patterns': ['Combat'], 'scale': 'mechanic', 'source': 'seed'},
        'Mass Combat':           {'patterns': ['Mass Combat'], 'scale': 'mechanic', 'source': 'seed'},
    }
    res = va.consolidate_tokens(token_defs, {})   # empty coref: purely signal-2 driven
    assert sorted(res) == ['Almqvist', 'Combat', 'Duchess Inge Baralta', 'King Almud Almqvist',
                           'Mass Combat', 'Prince Torben Almqvist']
    # the unique-container merge: 'Baralta' folds into the longer registry-canonical form
    merged = res['Duchess Inge Baralta']
    assert merged['patterns'] == ['Baralta']                          # HEAD pattern = the shared surname
    assert sorted(merged['aliases_merged']) == ['Baralta', 'Duchess Inge Baralta']
    assert merged['source'] == 'derived:proper_noun'                  # winner = lowest _source_rank member
    assert 'Baralta' not in res                                       # absorbed into the merged label
    # the shared-dynasty-surname guard: 'Almqvist' merges with NOBODY (2 containers -> ambiguous)
    assert res['Almqvist'] == token_defs['Almqvist']
    assert 'aliases_merged' not in res['Almqvist']
    assert res['King Almud Almqvist'] == token_defs['King Almud Almqvist']
    assert res['Prince Torben Almqvist'] == token_defs['Prince Torben Almqvist']
    # non-name-scale substring relation (Combat ⊂ Mass Combat) never triggers signal 2
    assert res['Combat'] == token_defs['Combat']
    assert res['Mass Combat'] == token_defs['Mass Combat']


def test_consolidate_tokens_registry_alias_signal_merges_across_scale():
    """Signal 1 (registry-alias coreference) is authoritative for ANY scale — unlike signal 2, it is
    not restricted to name-like scales. Two 'mechanic'-scale surface forms merge here purely because
    `coref` declares them the same entity, which signal 2 alone would never do for this scale."""
    token_defs = {
        'Piety':       {'patterns': ['Piety'], 'scale': 'mechanic', 'source': 'seed'},
        'Piety Track': {'patterns': ['Piety Track'], 'scale': 'mechanic', 'source': 'derived:names_index'},
    }
    coref = {'piety': 'Piety Track', 'piety track': 'Piety Track'}
    res = va.consolidate_tokens(token_defs, coref)
    assert list(res) == ['Piety Track']                 # merged; labelled by the registry canonical
    assert 'Piety' not in res
    merged = res['Piety Track']
    assert sorted(merged['aliases_merged']) == ['Piety', 'Piety Track']
    assert merged['source'] == 'seed'                   # 'Piety' wins on _source_rank (1 < 2)
    # HEAD pattern resolved to the shared word-boundary substring ('Piety' is a whole word inside
    # 'Piety Track'), so the merged pattern matches the short form and the full phrase alike.
    assert any(re.fullmatch(p, 'Piety') for p in merged['patterns'])
    assert any(re.search(p, 'the Piety Track advances') for p in merged['patterns'])


def test_curate_tokens_paragraph_count_primary_doc_and_context_gate():
    """curate_tokens counts, per token, how many corpus PARAGRAPHS (>50 chars, per to_paragraphs)
    match its patterns AND pass its disambiguation context; primary_doc is the doc with the most
    hits. A context requirement that is never satisfied must zero the token out entirely."""
    para1 = ('Combat resolution uses a dice pool mechanic that determines success degree for a '
             'check.')
    para2 = ('Combat also interacts with the Momentum economy across every scene transition in '
             'play.')
    para_faith = ('Faith is one of the seven personal Conviction axes tracked for narrative '
                  'purposes here.')
    para3 = ('A single mention of Combat appears in this short reference paragraph for the b doc '
             'test.')
    design = {'a.md': para1 + '\n\n' + para2 + '\n\n' + para_faith, 'b.md': para3}
    token_defs = {
        'Combat': {'patterns': [r'\bCombat\b'], 'context': [],
                  'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
        'Faith':  {'patterns': [r'\bFaith\b'], 'context': [r'\bChurch\b'],
                  'scale': 'conviction', 'status': 'canonical', 'source': 'seed'},
    }
    tokens, _ = va.curate_tokens(design, token_defs)
    assert tokens['Combat']['paragraph_count'] == 3     # 2 hits in a.md + 1 in b.md
    assert tokens['Combat']['primary_doc'] == 'a.md'    # a.md has more hits (2) than b.md (1)
    assert tokens['Faith']['paragraph_count'] == 0      # the one 'Faith' mention has no 'Church' nearby
    assert tokens['Faith']['primary_doc'] is None


def test_build_g_cite_threshold_context_gate_and_self_exclusion():
    """build_g_cite: a token is a citation SOURCE only via its primary_doc; an edge forms only when
    the target's mention count in that doc is >= thresh (default 2, boundary-tested at exactly 2 and
    3); a target with an unsatisfied disambiguation context is excluded even above threshold; a token
    is never wired to itself; and a token with no primary_doc can never be a source."""
    tokens = {
        'A': {'primary_doc': 'doc1.md', '_ctx': [], '_compiled': [re.compile(r'\bA\b')]},
        'B': {'primary_doc': None, '_ctx': [], '_compiled': [re.compile(r'\bB\b')]},
        'C': {'primary_doc': None, '_ctx': [], '_compiled': [re.compile(r'\bC\b')]},
        'D': {'primary_doc': None, '_ctx': [re.compile(r'\bXyz\b')], '_compiled': [re.compile(r'\bD\b')]},
        'E': {'primary_doc': None, '_ctx': [], '_compiled': [re.compile(r'\bE\b')]},
    }
    design = {'doc1.md': ('B B B mentioned. C mentioned once. A is here too. D D D D D also '
                          'appears. E E occurs exactly twice.')}
    g = va.build_g_cite(tokens, design)
    assert g == {'A': {'B': 3, 'E': 2}}    # B: 3>=2 kept; C: 1<2 dropped; D: context-gated out despite
                                            # 5 mentions; E: exactly-2 boundary kept; A excluded from its
                                            # own edges (self-exclusion); B/C/D/E never become sources
    g3 = va.build_g_cite(tokens, design, thresh=3)
    assert g3 == {'A': {'B': 3}}           # raising thresh to 3 drops E's exactly-2 count


def test_throughline_orphans_known_answer():
    """Mode F: a throughline is an 'orphan' when <=2 corpus paragraphs jointly mention >=2 of its
    listed systems. An all-placeholder ('—'/'-') row is skipped outright (nothing to substantiate by
    design); a single-system row can structurally never reach the >=2-systems-in-one-paragraph bar,
    so it is always an orphan at substantiating=0; a row whose systems co-occur in >2 paragraphs is
    well-substantiated and must NOT appear."""
    para1 = ('Combat and Threadwork share the resolution pipeline in this first substantiating '
             'paragraph okay yes.')
    para2 = ('Combat interacts with Threadwork again through Momentum flow in this second '
             'substantiating para here.')
    para3 = ('This third paragraph also connects Combat mechanics with Threadwork resolution steps '
             'in detail now.')
    para4 = ('Combat teams up with Fieldwork investigation only once in this single substantiating '
             'paragraph today.')
    para5 = ('This paragraph only mentions Combat by itself without the other system referenced '
             'anywhere at all today.')
    design = {'doc.md': '\n\n'.join([para1, para2, para3, para4, para5])}
    rows = [
        ('T-CT', '', '', ['Combat', 'Threadwork']),      # co-occurs in 3 paragraphs -> NOT an orphan
        ('T-CF', '', '', ['Combat', 'Fieldwork']),        # co-occurs in 1 paragraph  -> orphan, subst=1
        ('T-PLACEHOLDER', '', '', ['—', '-']),             # all placeholders -> skipped entirely
        ('T-SINGLE', '', '', ['Combat']),                  # 1 system -> structurally always subst=0
    ]
    out = va.throughline_orphans(rows, design)
    assert out == [
        {'throughline': 'T-CF', 'systems': ['Combat', 'Fieldwork'], 'substantiating': 1},
        {'throughline': 'T-SINGLE', 'systems': ['Combat'], 'substantiating': 0},
    ]


def test_vocabulary_debt_known_answer():
    design = {
        'a.md': 'Game Master appears twice: Game Master.',
        'b.md': 'no mention here',
        'c.md': 'Coup Counter once.',
        'd.md': 'Coup Counter shows up here too.',
        'e.md': 'Coup Counter shows up a third time here.',
        'f.md': 'Coup Counter and Coup Counter and Coup Counter show up here four times overall.',
    }
    out = va.vocabulary_debt(design, ['Game Master', 'Coup Counter', 'Cultural Reformation'])
    assert [r['term'] for r in out] == ['Coup Counter', 'Game Master']   # sorted by -total (6 > 2)
    coup = out[0]
    assert coup['total'] == 6 and coup['docs'] == 4          # 1+1+1+3 across 4 docs
    assert coup['concentration'] == [('f.md', 3), ('c.md', 1), ('d.md', 1)]   # top-3 by count, ties
                                                                              # keep first-seen order
    gm = out[1]
    assert gm == {'term': 'Game Master', 'total': 2, 'docs': 1, 'concentration': [('a.md', 2)]}
    assert 'Cultural Reformation' not in {r['term'] for r in out}   # zero occurrences: not surfaced


def test_validate_p1_foundation_periphery_known_answer():
    """P1: PASS iff the foundation tokens' MEAN cite-degree (and MEAN tl-degree) exceeds the
    MEDIAN over ALL tokens. Hand-computed both directions of the inequality."""
    tokens = {n: {} for n in ['Self-Rendering', 'Leap', 'A', 'B', 'C']}
    deg_cite_pass = {'Self-Rendering': 10, 'Leap': 8, 'A': 1, 'B': 2, 'C': 1}
    deg_tl_pass = {'Self-Rendering': 5, 'Leap': 5, 'A': 0, 'B': 1, 'C': 0}
    v = va.validate(tokens, deg_cite_pass, deg_tl_pass, {})
    # foundation mean cite = (10+8)/2=9.0 > overall median of [10,8,1,2,1]=2 ; tl mean=5.0 > median 1
    assert v['p1'] == {'pass': True, 'foundation_cite_mean': 9.0, 'overall_cite_median': 2,
                       'foundation_tl_mean': 5.0, 'overall_tl_median': 1}

    deg_cite_fail = {'Self-Rendering': 1, 'Leap': 1, 'A': 5, 'B': 5, 'C': 5}
    deg_tl_fail = {'Self-Rendering': 1, 'Leap': 1, 'A': 5, 'B': 5, 'C': 5}
    v2 = va.validate(tokens, deg_cite_fail, deg_tl_fail, {})
    # foundation mean=1.0, overall median=5 -> 1.0 > 5 is False
    assert v2['p1'] == {'pass': False, 'foundation_cite_mean': 1.0, 'overall_cite_median': 5,
                        'foundation_tl_mean': 1.0, 'overall_tl_median': 5}


def test_validate_p3_citation_density_known_answer():
    """P3: PASS iff mean cite-degree (directed edge count / token count) >= 6.0. Boundary-tested at
    exactly 30/5=6.0 (pass, the floor is inclusive) and 29/5=5.8 (fail)."""
    tokens5 = {n: {} for n in ['t1', 't2', 't3', 't4', 't5']}
    g_pass = {'t1': {f'x{i}': 1 for i in range(30)}}
    v = va.validate(tokens5, {}, {}, g_pass)
    assert v['p3'] == {'pass': True, 'n_cite_edges': 30, 'n_tokens': 5,
                       'mean_cite_degree': 6.0, 'floor': 6.0}
    g_fail = {'t1': {f'x{i}': 1 for i in range(29)}}
    v2 = va.validate(tokens5, {}, {}, g_fail)
    assert v2['p3'] == {'pass': False, 'n_cite_edges': 29, 'n_tokens': 5,
                        'mean_cite_degree': 5.8, 'floor': 6.0}


def test_diagnostics_mode_a_hubs_and_mode_e_sparse_known_answer():
    """Mode A (multi-graph hubs): top-quintile in >=3 of the structural graphs. Mode E (sparse
    context): bottom-decile in BOTH paragraph_count and cite-degree. Built from a 5-token graph
    where exactly one token ('Hub') qualifies for A and exactly two ('P4','P5') qualify for E,
    independently hand-verified against _top_quintile / _percentile_10_cut's own known answers."""
    names = ['Hub', 'P2', 'P3', 'P4', 'P5']
    graphs = {'cite': {'Hub': {'P2': 3, 'P3': 3, 'P4': 3, 'P5': 3}},   # Hub cite-deg 4, others 1
             'throughline': {'Hub': {'P2': 1, 'P3': 1}},              # Hub tl-deg 2, P2/P3 1, P4/P5 0
             'mu': {'Hub': {'P2': 1}},                                # Hub/P2 tie at mu-deg 1
             'pp': {}}                                                # all pp-deg 0
    degs = {k: va._degrees(graphs[k], names) for k in graphs}
    tokens = {
        'Hub': {'paragraph_count': 50, 'status': 'canonical'},
        'P2': {'paragraph_count': 1, 'status': 'canonical'},
        'P3': {'paragraph_count': 1, 'status': 'canonical'},
        'P4': {'paragraph_count': 0, 'status': 'canonical'},
        'P5': {'paragraph_count': 0, 'status': 'canonical'},
    }
    diag = va.diagnostics(tokens, graphs, degs)
    # A: Hub is top-quintile in cite (4 vs 1s), throughline (2 vs 1/0), and mu (tied at 1 with P2,
    # but pp is all-zero so pp's tq is empty) -> in_graphs=3, qualifies; nobody else reaches 3.
    assert diag['A_multigraph_hubs'] == [
        {'token': 'Hub', 'in_graphs': 3, 'cite': 4, 'throughline': 2, 'mu': 1, 'pp': 0}]
    # E: pcut=_percentile_10_cut([50,1,1,0,0])=0, dcut=_percentile_10_cut([4,1,1,1,1])=1.
    # P4/P5 have paragraphs=0<=0 and cite_deg=1<=1 -> both flagged; Hub/P2/P3 fail one of the two.
    assert diag['E_sparse_context'] == [
        {'token': 'P4', 'paragraphs': 0, 'cite_deg': 1, 'status': 'canonical'},
        {'token': 'P5', 'paragraphs': 0, 'cite_deg': 1, 'status': 'canonical'},
    ]


def test_keytype_token_known_answer():
    """_keytype_token maps a contract Key-TYPE string to the 'Key: <type>' token that names it, by
    full-matching the token's own patterns — restricted to names starting with 'Key:' so a same-text
    non-Key token can never steal the mapping, and an invalid regex pattern is skipped, not fatal."""
    tokens = {
        'Key: mechanical.scene_exited': {
            'patterns': [re.escape('mechanical.scene_exited'), r'\bScene Exited\b']},
        'NotAKey': {'patterns': ['mechanical.scene_exited']},   # same text, wrong name prefix
    }
    assert va._keytype_token('mechanical.scene_exited', tokens) == 'Key: mechanical.scene_exited'
    assert va._keytype_token('unknown.type', tokens) is None
    # an invalid regex in an earlier pattern is caught and skipped, not raised
    tokens2 = {'Key: bad.type': {'patterns': ['(unbalanced', re.escape('bad.type')]}}
    assert va._keytype_token('bad.type', tokens2) == 'Key: bad.type'


# ── ED-MB-0047 (I4 / ED-MB-0043 F6): alias-spanning seed tokens have ONE owner ──

def _derived_token_universe():
    from pathlib import Path
    return va.derive_tokens(Path(_ROOT))


def test_seed_alias_names_are_not_minted_as_separate_tokens():
    """A seed token that declares `alias_names` OWNS those names — no derivation may mint a
    second token for one.

    The defect class (ED-MB-0043 F6, measured): the curated core matched six surface forms
    spanning TWO names, and each name was independently derived — 'Mass Battle' from
    module_contracts' `mass_battle` module (scale 'mechanic'), 'Mass Combat' from
    canonical_sources' `mass_combat` system key (scale 'system'). `add()` dedupes on the exact
    normalized NAME, which cannot see an alias, so one subsystem occupied two graph nodes at
    two scales and its citations split between them (the audit's Μ-degree 0 vs 23).

    This guard is parameterized over the seed table, not over mass battle: any seed entry that
    later declares `alias_names` inherits it by adding the key. Mutation: delete the
    `alias_names` pre-seeding loop in `derive_tokens` and this fails on 'Mass Combat'.
    """
    tokens = _derived_token_universe()
    norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()
    live = {norm(n) for n in tokens}
    claimed = [(name, alias)
               for name, meta in va.SEED_TOKENS.items()
               for alias in (meta.get('alias_names') or [])]
    assert claimed, "no seed token declares alias_names — this guard would be vacuous"
    for name, alias in claimed:
        assert norm(alias) != norm(name), f"{name}: alias_names must not repeat the token's own name"
        assert norm(alias) not in live, (
            f"seed token {name!r} claims alias {alias!r}, but {alias!r} was ALSO minted as its "
            f"own token — the alias-spanning duplicate-owner class (ED-MB-0043 F6)")


def test_mass_battle_token_has_one_owner_at_the_provincial_scale():
    """The mass-battle subsystem is ONE token, at the scale its own registry records.

    Two independent assertions, because the F6 finding had two halves:
      (1) ONE owner — exactly one token matches the `mass_battle` identifier;
      (2) the RIGHT scale — 'province', agreeing with registers/mechanics_index.yaml
          (`mass_battle: scale: provincial`). 'mechanic' is not a member of this ontology at
          all: it is the flat default `derive_tokens` stamps on EVERY module_contracts module,
          so it carried no classification information about mass battle specifically.

    Mutation: re-key the seed entry to 'Mass Combat' and (1) fails with two owners; drop
    `'scale': 'province'` to the module-derived default and (2) fails.
    """
    import yaml
    tokens = _derived_token_universe()
    owners = [name for name, meta in tokens.items()
              if any(re.search(p, 'mass_battle') for p in meta.get('patterns', [])
                     if _compiles(p))]
    assert owners == ['Mass Battle'], f"expected one owner named 'Mass Battle', got {owners}"
    assert tokens['Mass Battle']['scale'] == 'province'

    mi = yaml.safe_load(open(os.path.join(_ROOT, 'registers', 'mechanics_index.yaml'),
                             encoding='utf-8'))
    recorded = (mi.get('mechanics') or mi).get('mass_battle', {}).get('scale')
    assert recorded == 'provincial', f"mechanics_index moved: {recorded!r}"
    assert tokens['Mass Battle']['scale'] == recorded.replace('provincial', 'province')


def _compiles(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
