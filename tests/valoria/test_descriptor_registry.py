"""tests/registry/test_descriptor_registry.py -- W1.13. Confirms the Descriptor Registry loads and
that alias-driven recategorization-without-rewiring works (the 'spirit move' payoff): legacy
attribute names back-resolve to their new keys, so existing formulas need no rewrite.

Revived 2026-07-08 (OPT-AV-7): the prior version imported a dead path and defined no test_*
function, so pytest silently collected zero tests from this file.

Re-pinned at CR-84 (ED-IN-0328): the roster is Jordan's TEN. KEYS ARE STABLE and names and aliases
moved, so the load-bearing assertion is ALIAS PRESERVATION: every name that resolved before CR-84
still resolves to the same key (`_PRE_CR84`), except Perception, which left Attunement for its own
key, and Bonds, which is retired and resolves with a deprecation flag. The preservation check is a
function (`_lost`) so a planted failure can be run through the same code (CLAUDE.md §0.1 pt 3)."""
import tools.descriptor_registry as dr

#: Every name -> key that resolved before CR-84, read off the registry at e71f1749. Perception is
#: absent on purpose (it moved to attr.mind.perception); Bonds and its aliases are in `_RETIRED`.
_PRE_CR84 = {
    'Strength': 'attr.body.strength',
    'Endurance': 'attr.body.endurance', 'Vitality': 'attr.body.endurance',
    'Agility': 'attr.body.agility', 'Dexterity': 'attr.body.agility',
    'Focus': 'attr.mind.focus',
    'Acuity': 'attr.mind.acuity', 'Reasoning': 'attr.mind.acuity', 'Cognition': 'attr.mind.acuity',
    'Will': 'attr.mind.will', 'Spirit': 'attr.mind.will',
    'Attunement': 'attr.social.attunement',
    'Charisma': 'attr.social.charisma', 'Presence': 'attr.social.charisma',
}
_RETIRED = {'Bonds': 'attr.social.bonds', 'Sincerity': 'attr.social.bonds',
            'Affability': 'attr.social.bonds'}
_THE_TEN = [
    'attr.body.strength', 'attr.body.endurance', 'attr.body.agility',
    'attr.mind.focus', 'attr.mind.acuity', 'attr.mind.will', 'attr.mind.perception',
    'attr.social.attunement', 'attr.social.charisma', 'attr.social.grace',
]


def _load():
    with open('references/descriptor_registry.yaml') as f:
        return dr.load(f.read())


def _lost(reg):
    """Names from `_PRE_CR84` (and the retired three) that no longer resolve to the key they did."""
    gone = []
    for name, key in {**_PRE_CR84, **_RETIRED}.items():
        e = dr.resolve(reg, name)
        if e is None or e['key'] != key:
            gone.append(name)
    return gone


def test_descriptor_registry():
    reg = _load()

    # the ten, in three categories (3 body, 4 mind, 3 social)
    assert [e['key'] for e in dr.all_attributes(reg)] == _THE_TEN
    assert len(dr.all_attributes(reg)) == 10, "expected 10 attributes"
    assert [len(dr.by_category(reg, c)) for c in ('body', 'mind', 'social')] == [3, 4, 3]

    # the 'spirit move' + legacy aliases resolve (this is what makes the move cost no rewrites)
    assert dr.resolve(reg, 'Spirit')['key'] == 'attr.mind.will'
    assert dr.resolve(reg, 'Cognition')['key'] == 'attr.mind.acuity'
    assert dr.resolve(reg, 'Presence')['key'] == 'attr.social.charisma'
    assert dr.resolve(reg, 'Vitality')['key'] == 'attr.body.endurance'
    assert dr.resolve(reg, 'Dexterity')['key'] == 'attr.body.agility'

    # primary names + keys resolve too; case-insensitive
    assert dr.resolve(reg, 'Will')['key'] == 'attr.mind.will'
    assert dr.resolve(reg, 'CHARISMA')['key'] == 'attr.social.charisma'
    assert dr.resolve(reg, 'Coordination')['key'] == 'attr.body.agility'
    assert dr.resolve(reg, 'Reason')['key'] == 'attr.mind.acuity'
    assert dr.resolve(reg, 'Grace')['key'] == 'attr.social.grace'
    assert dr.resolve(reg, 'attr.social.bonds')['name'] == 'Bonds'

    # retired attribute must NOT resolve
    assert dr.resolve(reg, 'Recall') is None, "'Recall' was retired; must not resolve"

    # aggregate placeholders (W2.8)
    assert set(dr.aggregate_members(reg, 'agg.mind')) == {
        'attr.mind.focus', 'attr.mind.acuity', 'attr.mind.will', 'attr.mind.perception'}
    assert set(dr.aggregate_members(reg, 'agg.body')) == {
        'attr.body.strength', 'attr.body.endurance', 'attr.body.agility'}
    assert set(dr.aggregate_members(reg, 'agg.social')) == {
        'attr.social.attunement', 'attr.social.charisma', 'attr.social.grace'}

    # domain partition (W2.9)
    assert len(dr.by_domain(reg, 'actor')) == 10

    # deprecation
    assert dr.is_deprecated(reg, 'resonance_style')
    assert not dr.is_deprecated(reg, 'attr.mind.will')


def test_every_alias_that_resolved_before_still_resolves_to_the_same_key():
    """CR-84's exit: alias preservation. `_lost` must be empty on the real registry."""
    assert _lost(_load()) == []


def test_alias_preservation_reddens_when_an_alias_is_dropped():
    """The planted failure (§0.1 pt 3): drop 'Dexterity' from the registry text and the SAME check
    that passes above must name it. Without this the assertion above could not observe a loss."""
    text = open('references/descriptor_registry.yaml').read()
    assert 'aliases: [Agility, Dexterity]' in text
    planted = dr.load(text.replace('aliases: [Agility, Dexterity]', 'aliases: [Agility]'))
    assert _lost(planted) == ['Dexterity']
    # and a retargeted alias (Presence moved to another key) is named too
    moved = dr.load(text.replace('aliases: [Charisma]', 'aliases: []').replace(
        'aliases: [Will, Willpower]', 'aliases: [Will, Willpower, Charisma]'))
    assert _lost(moved) == ['Charisma']


def test_perception_is_its_own_attribute_not_an_attunement_alias():
    reg = _load()
    assert dr.resolve(reg, 'Perception')['key'] == 'attr.mind.perception'
    assert dr.resolve(reg, 'Attunement')['key'] == 'attr.social.attunement'
    attunement = dr.resolve(reg, 'attr.social.attunement')
    assert 'Perception' not in attunement['aliases']


def test_bonds_is_retired_and_resolves_with_a_deprecation_flag():
    reg = _load()
    for name in _RETIRED:
        e = dr.resolve(reg, name)
        assert e is not None and e['key'] == 'attr.social.bonds', name
        assert e['deprecated'] is True, name
    # a live attribute carries no flag, and the retired one is outside the roster
    assert 'deprecated' not in dr.resolve(reg, 'Strength')
    assert 'attr.social.bonds' not in [e['key'] for e in dr.all_attributes(reg)]


def test_composure_is_not_an_attribute_alias():
    """Composure is the knot damage track (`not_descriptors.derived_values`). Aliasing it to Grace
    would make resolve('Composure') return the attribute where the track is meant."""
    reg = _load()
    assert dr.resolve(reg, 'Composure') is None
    assert 'Composure' in reg['not_descriptors']['derived_values']
    assert 'Resolve' in reg['not_descriptors']['derived_values']      # Spirit's derived value, not an attribute
    assert dr.resolve(reg, 'Resolve') is None


def test_every_attribute_name_and_alias_is_unique_across_the_roster():
    """One string, one attribute: a duplicate would make `resolve` return whichever came first."""
    reg = _load()
    seen = {}
    for e in list(dr.all_attributes(reg)) + list(reg['attributes']['retired']):
        for s in [e['key'], e['name']] + list(e.get('aliases', [])):
            k = s.lower()
            assert seen.setdefault(k, e['key']) == e['key'], f"{s!r} names two attributes"
