"""MB-04 (A5 role instincts, #445 U-3): a role's instruction keywords drive engine primitives.

`config.ROLE_SPEC` gives every role a shape and an instruction package. Before MB-04 most of that
vocabulary had no reader: two roles whose packages differed only in those keywords fought identically,
so the role was a label, not a design axis. `hierarchy.units.ROLE_INSTRUCTION_PRIMITIVES` is the single
owner of which keyword drives which primitive; this file is its falsifier.

U-3's own observable: a `ShieldWall` and a `Push` of the same subunit produce different density and
advance. On the pre-MB-04 tree the two runs were identical to the last float — the `advance`/`hold`
keywords were read by nothing, and ShieldWall's `brace` never fires against a body that is not
charging it (Push carries none). `MB_ROLE_INSTRUCTIONS=0` reproduces that tree, and the OFF arm below pins it, so a
mapping that only renames keywords cannot turn this file green.
"""
import random

import pytest

import modules.mass_battle.config as C
import modules.mass_battle.hierarchy.units as _hu
import modules.mass_battle.orchestration as _orch
from systems.mass_battle.sim.engine import build_army, build_unit

from .test_reach_weapon_class import field_path  # noqa: F401  (fixture re-export)

_SEEDS = (11, 12, 13)


@pytest.fixture
def wired(monkeypatch):
    monkeypatch.setattr(_hu, 'MB_ROLE_INSTRUCTIONS', True)


@pytest.fixture
def unwired(monkeypatch):
    monkeypatch.setattr(_hu, 'MB_ROLE_INSTRUCTIONS', False)


def _fight(role, seed):
    """One heavy-infantry subunit in `role` against a plain balanced Line; returns (advance, density).

    advance: rows the role's subunit moved toward the enemy (faction A faces -row).
    density: its troops per occupied cell at the end of the engagement."""
    random.seed(seed)
    a = build_army([{'role': role, 'troop_type': 'heavy_infantry'}], 'R', 'A')
    b = build_unit('Line', 3, 'E', 'B', 25)
    su = a.units[0]
    r0 = su.centroid()[0]
    _orch.run_battle(a, b, max_ticks=18)
    advance = r0 - su.centroid()[0]
    occupied = [t for t in su.cell_troops.values() if t > 0]
    density = sum(occupied) / len(occupied) if occupied else 0.0
    return advance, density


def test_shieldwall_and_push_differ_in_density_and_advance(field_path, wired):
    """#445 U-3. ShieldWall = brace + hold, Push = push: the hold stance stands, the aggressive
    stance closes faster and presses — so the two must differ in BOTH advance and density."""
    checked = 0
    for s in _SEEDS:
        wall_adv, wall_den = _fight('ShieldWall', s)
        push_adv, push_den = _fight('Push', s)
        assert wall_adv == 0.0, f"seed {s}: a ShieldWall holds its ground, moved {wall_adv}"
        assert push_adv > wall_adv, f"seed {s}: Push advanced {push_adv}, ShieldWall {wall_adv}"
        assert push_den != wall_den, f"seed {s}: same density {push_den} under both roles"
        checked += 1
    assert checked == len(_SEEDS)


def test_unwired_reproduces_the_label_only_roles(field_path, unwired):
    """The control: with the mapping OFF the two roles fight to the last float alike — the pre-MB-04
    behaviour, and what a labels-only mapping would leave."""
    for s in _SEEDS:
        assert _fight('ShieldWall', s) == _fight('Push', s)


def test_explicit_stance_beats_the_role_default(wired):
    """A role's stance keyword is a default posture: an explicit non-balanced stance wins."""
    su = build_army([{'role': 'ShieldWall', 'troop_type': 'heavy_infantry', 'stance': 'aggressive'}],
                    'R', 'A').units[0]
    assert su.eff_stance == 'aggressive'
    su = build_army([{'role': 'ShieldWall', 'troop_type': 'heavy_infantry'}], 'R', 'A').units[0]
    assert su.eff_stance == 'hold'
    su = build_army([{'role': 'Push', 'troop_type': 'heavy_infantry'}], 'R', 'A').units[0]
    assert su.eff_stance == 'aggressive'
    su = build_army([{'role': 'Shock', 'troop_type': 'cavalry'}], 'R', 'A').units[0]
    assert su.eff_stance == 'aggressive'


def test_an_order_that_releases_to_balanced_beats_the_role_keyword(wired):
    """The engine's own release idiom (build_envelopment, build_refused_flank) writes
    {'stance': 'balanced'}. 'balanced' is also the neutral default, so it must be remembered as WRITTEN:
    a ShieldWall released by an Order moves again instead of re-asserting its 'hold' keyword."""
    from modules.mass_battle.core.contact import check_orders
    u = build_army([{'role': 'ShieldWall', 'troop_type': 'heavy_infantry',
                     'orders': (_hu.Order('tick:3', {'stance': 'balanced'}),)}], 'R', 'A')
    su = u.units[0]
    assert su.eff_stance == 'hold'
    check_orders(u, 2, [])
    assert su.eff_stance == 'hold', "the order must not fire before its tick"
    check_orders(u, 3, [])
    assert su.stance == 'balanced' and su.eff_stance == 'balanced'


def test_a_build_spec_that_writes_balanced_beats_the_role_keyword(wired):
    su = build_army([{'role': 'ShieldWall', 'troop_type': 'heavy_infantry', 'stance': 'balanced'}],
                    'R', 'A').units[0]
    assert su.eff_stance == 'balanced'


def test_a_volley_line_is_not_frozen_by_its_role(wired):
    """VolleyLine used to carry 'hold', which (STANCE_SPEED_MOD['hold'] = -99) stops archers advancing
    and braces them against shock. Its role keyword is 'volley' alone."""
    su = build_army([{'role': 'VolleyLine', 'troop_type': 'archers'}], 'R', 'A').units[0]
    assert su.eff_stance == 'balanced'


# B17.07: `Feint` is on no menu (no season path reaches the feint), so a body that carries the `lure` keyword is built
# by its package, not by naming the role: the primitive is still read live at `unit_lures`.
_FEINT_SPEC = {'shape': 'Line', 'instructions': ('lure',), 'troop_type': 'cavalry'}


def test_lure_declares_the_feigned_retreat(wired, monkeypatch):
    """Feint = lure -> PP-256's Feigned Retreat: a pursuer of a routing lure unit faces the
    recognise/hold checks; without the keyword (and no order) there is no feint to resolve."""
    monkeypatch.setattr(_orch, 'MB_FEIGNED_RETREAT', True)
    random.seed(5)
    pursuer = build_unit('Line', 3, 'P', 'A', 25, troop_type='cavalry', speed='Fast')
    lure = build_army([_FEINT_SPEC], 'L', 'B')
    plain = build_army([{'role': 'Shock', 'troop_type': 'cavalry'}], 'S', 'B')
    assert lure.feigned is False, "the keyword is read at the pursuit site, not written onto the Army"
    assert _orch.resolve_feigned_retreat(pursuer, lure) is not None
    assert _orch.resolve_feigned_retreat(pursuer, plain) is None


def test_lure_is_inert_unwired(unwired, monkeypatch):
    monkeypatch.setattr(_orch, 'MB_FEIGNED_RETREAT', True)
    pursuer = build_unit('Line', 3, 'P', 'A', 25, troop_type='cavalry', speed='Fast')
    lure = build_army([_FEINT_SPEC], 'L', 'B')
    assert _orch.resolve_feigned_retreat(pursuer, lure) is None


_OFF_EVERY_MENU = ('Pursue', 'Screen', 'Harass', 'Feint')   # B17.07: each has no primitive a season path reaches


def test_no_menu_offers_a_role_without_a_primitive():
    """B17.07 (`U5b_MB_residue` §1): a role stands on a troop type's menu only if a choice of it can matter.
    The four roles whose package no primitive reads (and whose one wired keyword, `lure`, no season path reaches)
    are on no menu; and every keyword a menu role hands out is read by a primitive (a row of
    `ROLE_INSTRUCTION_PRIMITIVES` that is not `None`). A role with an EMPTY package is a shape (VolleyLine,
    Skirmish) and stays. The role names themselves stay in `ROLE_SPEC`: a standing order ranges over all of them."""
    table = _hu.ROLE_INSTRUCTION_PRIMITIVES
    checked = 0
    for troop_type, menu in C.TROOP_TYPE_ROLES.items():
        for role in menu:
            assert role not in _OFF_EVERY_MENU, f"{troop_type!r} still offers {role!r}"
            unwired = [k for k in C.ROLE_SPEC[role]['instructions'] if table[k][0] is None]
            assert not unwired, f"{troop_type!r} offers {role!r}, whose keyword(s) {unwired} drive nothing"
            checked += 1
    assert checked >= 20
    assert set(_OFF_EVERY_MENU) <= set(C.ROLE_SPEC), "an order may still name them (the bypass of role_allowed)"


def test_every_role_keyword_is_classified():
    """Every keyword ROLE_SPEC hands out has a row in the mapping: a primitive, or None with the
    reason it is unwired. A keyword added to ROLE_SPEC without a row fails here."""
    vocab = {k for spec in C.ROLE_SPEC.values() for k in spec['instructions']}
    assert len(vocab) >= 8   # B17.07 cut seven unwired keywords from the 15 the menus carried: the eight left each have a row
    table = _hu.ROLE_INSTRUCTION_PRIMITIVES
    assert vocab <= set(table), f"unclassified: {sorted(vocab - set(table))}"
