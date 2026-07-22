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
        'Duchess Inge Baralta':       [r'\bBaralta\b', r'\bInge\b'],
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
