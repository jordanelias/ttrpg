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


def test_resolve_structural_practitioner_stat_via_descriptor():
    # "Thread Sensitivity" (prac.thread_sensitivity) lives in descriptor_registry.yaml's
    # practitioner_stats section. descriptor_registry.resolve() itself does NOT scan it
    # (attributes only) and names_index.yaml does not mirror it — but the reader now resolves the
    # FULL descriptor_registry structural namespace (fac./set./prac./terr./agg.) via its
    # non-attribute index (ED-IN-0058), so this routes through the AUTHORITATIVE descriptor
    # registry (kind='descriptor'), not the fuzzy quantity merge. Same key, more authoritative via.
    reg = real_descriptor_registry.load()
    assert real_descriptor_registry.resolve(reg, 'Thread Sensitivity') is None   # attributes-only
    assert real_names.key_for('Thread Sensitivity') is None

    result = registry.resolve('Thread Sensitivity')
    assert result['kind'] == 'descriptor'
    assert result['key'] == 'prac.thread_sensitivity'
    assert result['registry_key'] == 'prac.thread_sensitivity'
    assert result['via'] == 'descriptor_registry'
    assert result['section'] == 'practitioner_stats'


def test_resolve_structural_territory_stat_alias_via_descriptor():
    # "Fort" is a declared alias of terr.fort_level — same story via an ALIAS form. Now resolved
    # through the descriptor registry's non-attribute index (kind='descriptor'), not quantity.
    reg = real_descriptor_registry.load()
    assert real_descriptor_registry.resolve(reg, 'Fort') is None
    assert real_names.key_for('Fort') is None

    result = registry.resolve('Fort')
    assert result['kind'] == 'descriptor'
    assert result['key'] == 'terr.fort_level'
    assert result['via'] == 'descriptor_registry'
    assert result['section'] == 'territory_stats'


def test_influence_string_collision_KNOWN_LIMITATION_but_key_now_reachable():
    # KNOWN LIMITATION (WS1 antagonist finding, ED-IN-0057), now PARTIALLY closed (ED-IN-0058).
    # The STRING "Influence" is BOTH an alias of attr.social.charisma AND the canonical name of
    # the faction-stat fac.influence; the attribute wins the string (checked first), so
    # "Influence" -> attr.social.charisma with no 'disagreement' (the loser is discarded UPSTREAM,
    # invisible to resolve()). That residual STRING ambiguity is the pointer-collision the WS1
    # data fold-in must resolve; it is not a facade bug.
    result = registry.resolve('Influence')
    assert result['key'] == 'attr.social.charisma'   # the attribute meaning wins the string
    assert result['disagreement'] == []              # collision invisible to disagreement (upstream)

    # PARTIAL FIX (ED-IN-0058): the ENTITY fac.influence is no longer wholly unreachable — it now
    # resolves by its bare structural key through the descriptor registry, even though its display
    # name is shadowed. So the faction stat is at least pointer-addressable today.
    bykey = registry.resolve('fac.influence')
    assert bykey is not None
    assert bykey['kind'] == 'descriptor'
    assert bykey['key'] == 'fac.influence'
    assert bykey['section'] == 'faction_stats'

    # And the reader SURFACES the residual string-collision as the fold-in work-list rather than
    # hiding it: collisions() reports exactly this ambiguity (and, today, only this one).
    col = registry.collisions()
    assert col.get('influence') == ['attr.social.charisma', 'fac.influence']


def test_collisions_is_the_foldin_worklist():
    # collisions() is the NS2 diagnostic: display strings bound to >1 structural key — what the
    # data fold-in must disambiguate. Deterministic dict of {term: sorted[keys]}; every listed
    # term genuinely maps to multiple distinct keys.
    col = registry.collisions()
    assert isinstance(col, dict)
    for term, keys in col.items():
        assert term == term.lower()
        assert keys == sorted(keys)
        assert len(keys) == len(set(keys)) >= 2


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
