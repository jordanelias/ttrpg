"""Conditional stance/withdraw orders (Jordan directive 2026-07-23: "a unit only starts retreating
when the opponent is within X distance" / "advancing forward only to start withdrawing when X").

These codify + regression-guard the EXISTING Order primitive (trigger='enemy_range:D' +
behavior={'stance'/'yielding'}), reachable via the build_army spec `orders` key. No new engine
mechanism — the composable primitive already covers the directive; this pins the behaviour so it
cannot silently regress and documents the canonical usage.
"""
import math
import os
import random
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from mass_battle.engine import build_army, Order, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW  # noqa: E402


def _adv_then_withdraw(faction, trigger_range):
    """A subunit that ADVANCES (balanced), ordered to fighting-withdraw (yield + retreat) once the
    nearest enemy comes within `trigger_range` — the conditional Cannae bait."""
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    orders = (Order(trigger=f'enemy_range:{trigger_range}',
                    behavior={'yielding': True, 'stance': 'retreat'}),)
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
                        'stance': 'balanced', 'width': 6, 'depth': 2, 'troops': 1200,
                        'starting_position': (sr, 25), 'orders': orders}], faction, faction)


def _plain(faction, stance='aggressive'):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
                        'stance': stance, 'width': 6, 'depth': 2, 'troops': 1200,
                        'starting_position': (sr, 25)}], faction, faction)


def test_order_trigger_validates():
    # enemy_range is a recognized trigger; a typo fails loudly at construction
    Order(trigger='enemy_range:5', behavior={'stance': 'retreat'})
    with pytest.raises(ValueError):
        Order(trigger='enemy_rnge:5', behavior={'stance': 'retreat'})


def test_safe_fields_allow_stance_and_yielding():
    # both switches the directive needs must be settable by an order
    Order(trigger='enemy_range:5', behavior={'stance': 'retreat'})
    Order(trigger='enemy_range:5', behavior={'yielding': True})


def test_conditional_withdraw_fires_when_enemy_closes():
    ua = _adv_then_withdraw('A', 5)
    ub = _plain('B', 'aggressive')
    su = ua.subunits[0]
    assert su.stance == 'balanced' and su.yielding is False and su._order_idx == 0
    random.seed(2_000_555)
    resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
    # the enemy closed in -> the order fired -> the subunit flipped to a fighting withdrawal
    assert su._order_idx == 1, "the enemy_range order must fire once the enemy closes"
    assert su.stance == 'retreat' and su.yielding is True


def test_conditional_order_does_not_fire_out_of_range():
    # trigger range 0.5 (sub-cell): the centroids never come that close (min contact ~1 cell),
    # so the order must stay pending — a condition correctly never met stays unfired (by design).
    ua = _adv_then_withdraw('A', 0.5)
    ub = _plain('B', 'balanced')
    su = ua.subunits[0]
    random.seed(2_000_556)
    resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=6)
    assert su._order_idx == 0, "an enemy_range order must NOT fire while the enemy stays outside the range"
    assert su.stance == 'balanced' and su.yielding is False


def test_own_strength_trigger_validates():
    # ED-MB-0030: own_strength is a recognized trigger
    Order(trigger='own_strength:0.5', behavior={'stance': 'retreat'})
    with pytest.raises(ValueError):
        Order(trigger='own_strenght:0.5', behavior={'stance': 'retreat'})


def test_own_strength_fires_when_attrited():
    """A unit ordered to withdraw once it drops to <= 90% of spawn strength flips after taking losses."""
    sr = SIDE_A_START_ROW
    ua = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': 'balanced',
                      'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25),
                      'orders': (Order(trigger='own_strength:0.9',
                                       behavior={'yielding': True, 'stance': 'retreat'}),)}], 'A', 'A')
    ub = _plain('B', 'aggressive')
    su = ua.subunits[0]
    assert su._order_idx == 0 and su.troop_total() == pytest.approx(su._start_troops)
    random.seed(2_000_999)
    resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
    assert su._order_idx == 1, "own_strength order must fire once the subunit is attrited past the threshold"
    assert su.yielding is True and su.stance == 'retreat'


def test_own_strength_does_not_fire_at_full_strength():
    """own_strength:0.5 must NOT fire before the subunit is actually down to half — checked pre-battle."""
    sr = SIDE_A_START_ROW
    from mass_battle.core.contact import check_orders
    ua = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': 'balanced',
                      'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25),
                      'orders': (Order(trigger='own_strength:0.5', behavior={'stance': 'retreat'}),)}], 'A', 'A')
    su = ua.subunits[0]
    check_orders(ua, 0, [(0, 25)])  # a tick with the subunit at full strength
    assert su._order_idx == 0 and su.stance == 'balanced', "must not fire at full strength"


def test_retreat_only_when_within_range_via_stance():
    # the plainest form of the directive: hold/advance, then RETREAT (no yield) when enemy within X
    sr = SIDE_A_START_ROW
    ua = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': 'balanced',
                      'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25),
                      'orders': (Order(trigger='enemy_range:6', behavior={'stance': 'retreat'}),)}], 'A', 'A')
    ub = _plain('B', 'aggressive')
    su = ua.subunits[0]
    random.seed(2_000_557)
    resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
    assert su._order_idx == 1 and su.stance == 'retreat'
