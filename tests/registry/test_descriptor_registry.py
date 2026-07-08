"""tests/registry/test_descriptor_registry.py -- W1.13. Confirms the Descriptor Registry loads and
that alias-driven recategorization-without-rewiring works (the 'spirit move' payoff): legacy
attribute names back-resolve to their new keys, so existing formulas need no rewrite.

Revived 2026-07-08 (OPT-AV-7, coherence-audit hygiene batch): the prior version imported a dead
path (/home/claude, skills/valoria-orchestrator/scripts/) and defined no test_* function, so pytest
silently collected zero tests from this file. Fixed to import tools/descriptor_registry.py (the
live replacement) and to expose a real test_* entry point. Assertions are UNCHANGED from the
original -- they still match the current registry (the attribute-roster ratification, ED-IN-0029
OPT-AV-1, was explicitly deferred; this fix is import-mechanics only, no design content)."""
import tools.descriptor_registry as dr


def test_descriptor_registry():
    with open('references/descriptor_registry.yaml') as f:
        reg = dr.load(f.read())

    # 9 attributes, 3 per category
    assert len(dr.all_attributes(reg)) == 9, "expected 9 attributes"
    for cat in ('body', 'mind', 'social'):
        assert len(dr.by_category(reg, cat)) == 3, f"{cat} should have 3 attributes"

    # the 'spirit move' + legacy aliases resolve (this is what makes the move cost no rewrites)
    assert dr.resolve(reg, 'Spirit')['key'] == 'attr.mind.will'
    assert dr.resolve(reg, 'Cognition')['key'] == 'attr.mind.acuity'
    assert dr.resolve(reg, 'Presence')['key'] == 'attr.social.charisma'
    assert dr.resolve(reg, 'Vitality')['key'] == 'attr.body.endurance'
    assert dr.resolve(reg, 'Dexterity')['key'] == 'attr.body.agility'

    # primary names + keys resolve too; case-insensitive
    assert dr.resolve(reg, 'Will')['key'] == 'attr.mind.will'
    assert dr.resolve(reg, 'CHARISMA')['key'] == 'attr.social.charisma'
    assert dr.resolve(reg, 'attr.social.bonds')['name'] == 'Bonds'

    # retired attribute must NOT resolve
    assert dr.resolve(reg, 'Recall') is None, "'Recall' was retired; must not resolve"

    # aggregate placeholders (W2.8)
    assert set(dr.aggregate_members(reg, 'agg.mind')) == {'attr.mind.focus', 'attr.mind.acuity', 'attr.mind.will'}
    assert set(dr.aggregate_members(reg, 'agg.body')) == {'attr.body.strength', 'attr.body.endurance', 'attr.body.agility'}

    # domain partition (W2.9)
    assert len(dr.by_domain(reg, 'actor')) == 9

    # deprecation
    assert dr.is_deprecated(reg, 'resonance_style')
    assert not dr.is_deprecated(reg, 'attr.mind.will')
