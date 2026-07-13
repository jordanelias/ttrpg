"""Unit tests for tools/registry.py — the unifying FACADE reader over the three existing
name/descriptor/quantity resolvers (tools/names.py, tools/descriptor_registry.py,
tools/quantity_registry.py; see that module's docstring for the precedence rationale).

Per the observatory / audit-tool testing convention already established in this suite (see
test_pointer_audit.py's and test_gen_audit.py's docstrings): prove REUSE BY IDENTITY first
— registry.py must import the real resolver modules, never a private reimplementation
(CLAUDE.md §8: "every rule lives once ... never re-implement a rule") — then pin resolve()
against terms VERIFIED directly against the real registries (not invented; each pin below
was independently confirmed by calling the underlying resolver by hand before the assertion
was written), then exercise the disagreement-disclosure mechanism BOTH on a real, LIVE corpus
disagreement ("Thread Fatigue" — names vs quantity_registry, see the pin below) AND on a
controlled synthetic conflict (monkeypatch, for the multi-resolver shape not present live).

Two real pointer-COLLISIONS are pinned as KNOWN LIMITATIONS, not as correct behavior (WS1
antagonist findings, ED-IN-0057 — they are what the WS1 data fold-in exists to resolve):
"Influence" (an attribute alias that shadows the faction-stat fac.influence's canonical name,
making fac.influence reachable by no string) and the attribute-only reach of bare structural
keys. Pinning them as limitations keeps a green test from silently CERTIFYING the shadowed
answer as correct.
"""
import os
import sys

import pytest

# Make tools/ importable EXPLICITLY (mirrors tests/valoria/test_pointer_audit.py /
# test_gen_audit.py) rather than relying on registry.py's own sys.path side effect at load
# time — the reuse-by-identity tests below import names / descriptor_registry /
# quantity_registry directly and must not depend on import order.
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_TOOLS = os.path.join(_ROOT, 'tools')
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)

import registry                             # noqa: E402
import names as real_names                  # noqa: E402
import descriptor_registry as real_descriptor_registry  # noqa: E402
import quantity_registry as real_quantity_registry      # noqa: E402


# ── proves real reuse: registry.py delegates, it does not reimplement (CLAUDE.md §8) ───

def test_module_imports_the_real_names():
    assert registry.names is real_names
    assert registry.names.key_for is real_names.key_for
    assert registry.names.canonical is real_names.canonical
    assert registry.names.entries is real_names.entries


def test_module_imports_the_real_descriptor_registry():
    assert registry.descriptor_registry is real_descriptor_registry
    assert registry.descriptor_registry.resolve is real_descriptor_registry.resolve
    assert registry.descriptor_registry.load is real_descriptor_registry.load
    assert registry.descriptor_registry.all_attributes is real_descriptor_registry.all_attributes


def test_module_imports_the_real_quantity_registry():
    assert registry.quantity_registry is real_quantity_registry
    assert registry.quantity_registry.resolve is real_quantity_registry.resolve
    assert registry.quantity_registry.all_known is real_quantity_registry.all_known
    assert registry.quantity_registry.DESCRIPTOR_PATH == real_quantity_registry.DESCRIPTOR_PATH


# ── resolve(): pinned against terms VERIFIED directly against the real registries ──────

def test_resolve_descriptor_attribute_primary_name():
    # 'Strength' is attr.body.strength's primary name in descriptor_registry.yaml. All
    # three resolvers actually agree on this term (verified by hand: names.key_for and
    # quantity_registry.resolve both also land on attr.body.strength) — descriptor_registry
    # wins the 'via' slot purely because it is checked first in the documented precedence,
    # not because the others fail to recognize it.
    result = registry.resolve('Strength')
    assert result['term'] == 'Strength'
    assert result['kind'] == 'descriptor'
    assert result['key'] == 'attr.body.strength'
    assert result['via'] == 'descriptor_registry'
    assert result['disagreement'] == []
    assert 'matched_as' not in result  # only present for a quantity_registry-sourced winner


def test_resolve_descriptor_attribute_alias():
    # 'Dexterity' is a declared alias of attr.body.agility (descriptor_registry.yaml),
    # exercising the alias-resolution path rather than a primary name.
    result = registry.resolve('Dexterity')
    assert result['kind'] == 'descriptor'
    assert result['key'] == 'attr.body.agility'
    assert result['via'] == 'descriptor_registry'
    assert result['disagreement'] == []


def test_resolve_literal_descriptor_key_uniquely_decided_by_descriptor_registry():
    # Confirm, against the real modules, that a bare structural key is a case ONLY
    # descriptor_registry can resolve — quantity_registry.resolve() returns (None, None)
    # for it and names.key_for() returns None (both verified directly here) — so this term
    # is uniquely decided, not merely first-in-line among agreeing resolvers.
    assert real_quantity_registry.resolve('attr.body.strength') == (None, None)
    assert real_names.key_for('attr.body.strength') is None

    result = registry.resolve('attr.body.strength')
    assert result['kind'] == 'descriptor'
    assert result['key'] == 'attr.body.strength'
    assert result['via'] == 'descriptor_registry'
    assert result['disagreement'] == []


def test_resolve_canonical_proper_noun_name():
    # 'Solmund' is world.solmund's canonical display name in names_index.yaml (category:
    # proper_noun). descriptor_registry.resolve() cannot see it at all — verified directly
    # below, it is out of that resolver's attributes-only scope. quantity_registry ALSO
    # resolves 'Solmund' (it merges names_index.yaml too), but names.py is checked first in
    # the precedence, so it surfaces as kind='name' rather than being swallowed by
    # quantity_registry's broader merge of the same underlying entry.
    reg = real_descriptor_registry.load()
    assert real_descriptor_registry.resolve(reg, 'Solmund') is None
    assert real_quantity_registry.resolve('Solmund') == ('Solmund', 'world.solmund')  # confirms the overlap exists

    result = registry.resolve('Solmund')
    assert result['term'] == 'Solmund'
    assert result['kind'] == 'name'
    assert result['key'] == 'Solmund'
    assert result['via'] == 'names'
    assert result['disagreement'] == []


def test_resolve_quantity_only_practitioner_stat():
    # "Thread Sensitivity" (prac.thread_sensitivity) lives in descriptor_registry.yaml's
    # practitioner_stats section, which descriptor_registry.resolve() does NOT search (it
    # only scans body/mind/social attributes) and which names_index.yaml does not mirror
    # (its own header comment lists only attr./agg./fac./set. as mirrored sections) —
    # confirmed directly against both real resolvers below, before asserting the facade's
    # answer. This is the clearest real (non-monkeypatched) case where quantity_registry is
    # not just first-checked but the ONLY resolver of the three with an answer at all.
    reg = real_descriptor_registry.load()
    assert real_descriptor_registry.resolve(reg, 'Thread Sensitivity') is None
    assert real_names.key_for('Thread Sensitivity') is None

    result = registry.resolve('Thread Sensitivity')
    assert result['kind'] == 'quantity'
    assert result['key'] == 'prac.thread_sensitivity'
    assert result['via'] == 'quantity_registry'
    assert result['matched_as'] == 'Thread Sensitivity'
    assert result['disagreement'] == []


def test_resolve_quantity_only_territory_stat_abbreviation():
    # "Fort" is a declared alias of terr.fort_level — same uniquely-quantity_registry story
    # as Thread Sensitivity above, but exercising an abbreviation/alias form instead of a
    # primary name.
    reg = real_descriptor_registry.load()
    assert real_descriptor_registry.resolve(reg, 'Fort') is None
    assert real_names.key_for('Fort') is None

    result = registry.resolve('Fort')
    assert result['kind'] == 'quantity'
    assert result['key'] == 'terr.fort_level'
    assert result['via'] == 'quantity_registry'
    assert result['matched_as'] == 'Fort'


def test_influence_alias_shadows_faction_stat_KNOWN_LIMITATION():
    # KNOWN LIMITATION (WS1 antagonist finding, ED-IN-0057) — pinned as a limitation, NOT
    # certified as correct. "Influence" is BOTH an alias of attr.social.charisma AND the
    # canonical name of the faction-stat fac.influence. The attribute registers first inside
    # both underlying resolvers (first-write-wins), so:
    #   (a) the string "Influence" resolves to attr.social.charisma, and
    #   (b) fac.influence is reachable by NO display string at all, and
    #   (c) NO 'disagreement' fires — the losing candidate is discarded UPSTREAM of resolve().
    # This is the pointer-collision the WS1 fold-in must resolve (give fac.influence a
    # non-colliding pointer); it is NOT a precedence bug in the facade. If a future fold-in
    # fixes it, THIS test should start failing — that is the signal to update it.
    result = registry.resolve('Influence')
    assert result['key'] == 'attr.social.charisma'      # the attribute meaning wins the string
    assert result['disagreement'] == []                 # the collision is invisible to disagreement
    # fac.influence is a real ratified faction stat, yet unreachable by every string form:
    assert registry.resolve('fac.influence') is None    # (bare key: attribute-only reach, below)
    data = real_quantity_registry.load()
    assert 'fac.influence' not in set(data['known'].values()) or \
        [k for k, v in data['known'].items() if v == 'fac.influence'] == []


def test_thread_fatigue_is_a_real_LIVE_disagreement():
    # The disagreement mechanism is exercised against REAL corpus data, not only a monkeypatch:
    # "Thread Fatigue" resolves via names to thread.thread_fatigue, but quantity_registry's
    # not_descriptors loop (seeded before its names_index merge) matches it keyless — a genuine,
    # live, standing disagreement the facade discloses rather than swallows.
    assert real_names.key_for('Thread Fatigue') == 'thread.thread_fatigue'
    assert real_quantity_registry.resolve('Thread Fatigue') == ('Thread Fatigue', None)
    result = registry.resolve('Thread Fatigue')
    assert result['kind'] == 'name'
    assert result['key'] == 'Thread Fatigue'                     # names' display-string currency
    assert result['registry_key'] == 'thread.thread_fatigue'    # its dotted structural pointer
    assert {'kind': 'quantity', 'key': None, 'via': 'quantity_registry'} in result['disagreement']


def test_registry_key_is_a_uniform_structural_pointer_across_kinds():
    # capstone/WS1 antagonist finding: a `name` hit's `key` is a DISPLAY string, so callers
    # had no uniform way to recover its dotted key. `registry_key` now carries it for every kind.
    assert registry.resolve('Strength')['registry_key'] == 'attr.body.strength'   # == key (descriptor)
    solmund = registry.resolve('Solmund')
    assert solmund['kind'] == 'name'
    assert solmund['key'] == 'Solmund'                    # display string
    assert solmund['registry_key'] == 'world.solmund'     # dotted structural pointer, recoverable now


def test_resolve_nonsense_term_returns_none():
    assert registry.resolve('totally_not_a_real_term_xyz') is None


@pytest.mark.parametrize('bad_term', [None, '', '   ', 12345, ['Strength']])
def test_resolve_rejects_non_string_and_blank_input(bad_term):
    assert registry.resolve(bad_term) is None


# ── resolves() / all_known(): thin conveniences ─────────────────────────────────────────

def test_resolves_matches_resolve_is_not_none():
    assert registry.resolves('Strength') is True
    assert registry.resolves('Solmund') is True
    assert registry.resolves('Thread Sensitivity') is True
    assert registry.resolves('totally_not_a_real_term_xyz') is False
    assert registry.resolves('') is False
    assert registry.resolves(None) is False


def test_all_known_is_a_set_and_a_superset_of_every_pinned_term():
    known = registry.all_known()
    assert isinstance(known, set)
    for term in ('Strength', 'Dexterity', 'attr.body.strength', 'Solmund',
                 'Thread Sensitivity', 'Fort', 'Influence', 'Wealth'):
        assert term in known, f'{term!r} resolves() but is missing from all_known()'
    assert 'totally_not_a_real_term_xyz' not in known


def test_all_known_is_a_superset_of_quantity_registrys_own_vocabulary():
    # all_known() must never DROP anything quantity_registry itself already knows about —
    # it only ever adds (descriptor keys, names.py entries not already surfaced).
    assert real_quantity_registry.all_known() <= registry.all_known()


def test_all_known_is_deterministic_across_repeat_calls():
    assert registry.all_known() == registry.all_known()


# ── disagreement disclosure: proven via a controlled, monkeypatched conflict ────────────
# (no live three-way disagreement exists in the real corpus today — see the pins above —
# so the mechanism itself is exercised directly rather than waiting on real corpus drift.)

def test_disagreement_is_disclosed_not_silently_dropped(monkeypatch):
    monkeypatch.setattr(registry, '_descriptor_hit', lambda term: (
        {'kind': 'descriptor', 'key': 'attr.body.strength', 'via': 'descriptor_registry'}
        if term == 'Zeta' else None))
    monkeypatch.setattr(registry, '_names_hit', lambda term: None)
    monkeypatch.setattr(registry, '_quantity_hit', lambda term: (
        {'kind': 'quantity', 'key': 'fac.wealth', 'via': 'quantity_registry', 'matched_as': 'Zeta'}
        if term == 'Zeta' else None))

    result = registry.resolve('Zeta')
    assert result['kind'] == 'descriptor'      # precedence still decides the top-level answer
    assert result['key'] == 'attr.body.strength'
    assert result['via'] == 'descriptor_registry'
    assert result['disagreement'] == [
        {'kind': 'quantity', 'key': 'fac.wealth', 'via': 'quantity_registry'}
    ]


def test_disagreement_reports_every_differing_resolver_not_just_one(monkeypatch):
    monkeypatch.setattr(registry, '_descriptor_hit', lambda term: (
        {'kind': 'descriptor', 'key': 'attr.body.strength', 'via': 'descriptor_registry'}
        if term == 'Zeta' else None))
    monkeypatch.setattr(registry, '_names_hit', lambda term: (
        {'kind': 'name', 'key': 'Zeta Display Name', 'via': 'names', '_registry_key': 'world.zeta'}
        if term == 'Zeta' else None))
    monkeypatch.setattr(registry, '_quantity_hit', lambda term: (
        {'kind': 'quantity', 'key': 'fac.wealth', 'via': 'quantity_registry', 'matched_as': 'Zeta'}
        if term == 'Zeta' else None))

    result = registry.resolve('Zeta')
    assert result['via'] == 'descriptor_registry'
    assert len(result['disagreement']) == 2
    assert {'kind': 'name', 'key': 'Zeta Display Name', 'via': 'names'} in result['disagreement']
    assert {'kind': 'quantity', 'key': 'fac.wealth', 'via': 'quantity_registry'} in result['disagreement']


def test_agreement_across_all_three_yields_empty_disagreement_even_when_all_hit(monkeypatch):
    monkeypatch.setattr(registry, '_descriptor_hit', lambda term: (
        {'kind': 'descriptor', 'key': 'attr.body.strength', 'via': 'descriptor_registry'}
        if term == 'Zeta' else None))
    monkeypatch.setattr(registry, '_names_hit', lambda term: (
        {'kind': 'name', 'key': 'Strength', 'via': 'names', '_registry_key': 'attr.body.strength'}
        if term == 'Zeta' else None))
    monkeypatch.setattr(registry, '_quantity_hit', lambda term: (
        {'kind': 'quantity', 'key': 'attr.body.strength', 'via': 'quantity_registry', 'matched_as': 'Zeta'}
        if term == 'Zeta' else None))

    result = registry.resolve('Zeta')
    assert result['disagreement'] == []
