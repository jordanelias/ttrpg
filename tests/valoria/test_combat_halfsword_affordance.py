"""Emergent half-sword affordance (ED-PC-0014; audit G3 / plan P3 / consolidation JD-3, U4 slice).

Half-sword CAPABILITY is now derived from physical facts — a `grippable` element (ricasso / attested safe
forward grip) AND `geo['halfsword']` (geometry.can_halfsword_thrust) — not the old `HALFSWORD_FORM` name
whitelist. These tests pin: (1) the byte-identical-at-parity acceptance (derived set == {longsword, estoc}),
(2) that the formerly-DEAD `geo['halfsword']` coefficient + the new `grippable` field are now consumed, and
(3) that `halfsword_target` is byte-identical to the retired name-gated logic across the whole roster.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import combat_systems as S  # noqa: E402
from combatant import WEAPONS, Combatant, HALFSWORD_FORM, HALFSWORD_BASE  # noqa: E402


def test_affords_halfsword_emergent_set_is_parity():
    """P3 acceptance: on the un-extended roster the emergent affordance set is EXACTLY {longsword, estoc}
    (only those carry a `grippable` element). Marking a further attested ricasso is the JD-3 expansion."""
    aff = {n for n, w in WEAPONS.items() if 'base' not in w and S.affords_halfsword(w)}
    assert aff == {'longsword', 'estoc'}, aff


def test_grippable_is_the_gate_not_geometry_alone():
    """The `grippable` element is load-bearing: many weapons pass the geometry gate (can_halfsword_thrust)
    but must NOT afford the half-sword without an attested grippable zone — that is the whole point of the
    ricasso primitive (a spear/dagger passes the geometry but has no ricasso)."""
    geom_pass = [n for n, w in WEAPONS.items() if 'base' not in w and w.get('geo', {}).get('halfsword')]
    assert len(geom_pass) > 5, "geometry gate should pass many straight/pointed blades"
    for n in geom_pass:
        w = WEAPONS[n]
        has_grip = any(e.get('grippable') for e in w.get('elements', ()))
        assert S.affords_halfsword(w) == has_grip, n


def test_dead_coefficient_now_consumed():
    """De-vestigialisation: `geo['halfsword']` (computed by geometry.bake, formerly read by nothing) and the
    new `grippable` field are both read by affords_halfsword."""
    import inspect
    src = inspect.getsource(S.affords_halfsword)
    assert 'halfsword' in src and 'grippable' in src


def test_halfsword_target_byte_identical_to_retired_gate():
    """The capability gate moved from `base in HALFSWORD_FORM` to affords_halfsword, but the observable
    form-switch must be byte-identical over every (weapon x closed x armour) at parity."""
    def retired(weapon, closed, opp_armor):
        base = HALFSWORD_BASE.get(weapon, weapon)
        if base not in HALFSWORD_FORM:
            return weapon
        return HALFSWORD_FORM[base] if (closed and opp_armor in ('medium', 'heavy')) else base
    for n in WEAPONS:
        c = Combatant.__new__(Combatant); c.weapon = n
        for closed in (True, False):
            for a in ('none', 'light', 'medium', 'heavy'):
                assert S.halfsword_target(c, closed, a) == retired(n, closed, a), (n, closed, a)
