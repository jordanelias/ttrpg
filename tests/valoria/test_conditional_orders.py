"""Conditional stance/withdraw orders (Jordan directive 2026-07-23: "a unit only starts retreating
when the opponent is within X distance" / "advancing forward only to start withdrawing when X").

These codify + regression-guard the EXISTING Order primitive (trigger='enemy_range:D' +
behavior={'stance'/'yielding'}), reachable via the build_army spec `orders` key. No new engine
mechanism — the composable primitive already covers the directive; this pins the behaviour so it
cannot silently regress and documents the canonical usage.
"""
import math
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from systems.mass_battle.sim.engine import build_army, Order, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW  # noqa: E402
from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import rngsource  # noqa: E402


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
    su = ua.units[0]
    assert su.stance == 'balanced' and su.yielding is False and su._order_idx == 0
    with rngsource.using(draw.seeded(draw.H2("test_conditional_orders", 2_000_555))):
        resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
        # the enemy closed in -> the order fired -> the subunit flipped to a fighting withdrawal
        assert su._order_idx == 1, "the enemy_range order must fire once the enemy closes"
        assert su.stance == 'retreat' and su.yielding is True


def test_conditional_order_does_not_fire_out_of_range():
    # trigger range 0.5 (sub-cell): the centroids never come that close (min contact ~1 cell),
    # so the order must stay pending — a condition correctly never met stays unfired (by design).
    ua = _adv_then_withdraw('A', 0.5)
    ub = _plain('B', 'balanced')
    su = ua.units[0]
    with rngsource.using(draw.seeded(draw.H2("test_conditional_orders", 2_000_556))):
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
    su = ua.units[0]
    assert su._order_idx == 0 and su.troop_total() == pytest.approx(su._start_troops)
    with rngsource.using(draw.seeded(draw.H2("test_conditional_orders", 2_000_999))):
        resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
        assert su._order_idx == 1, "own_strength order must fire once the subunit is attrited past the threshold"
        assert su.yielding is True and su.stance == 'retreat'


def test_own_strength_does_not_fire_at_full_strength():
    """own_strength:0.5 must NOT fire before the subunit is actually down to half — checked pre-battle."""
    sr = SIDE_A_START_ROW
    from modules.mass_battle.core.contact import check_orders
    ua = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': 'balanced',
                      'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25),
                      'orders': (Order(trigger='own_strength:0.5', behavior={'stance': 'retreat'}),)}], 'A', 'A')
    su = ua.units[0]
    check_orders(ua, 0, [(0, 25)])  # a tick with the subunit at full strength
    assert su._order_idx == 0 and su.stance == 'balanced', "must not fire at full strength"


def test_retreat_only_when_within_range_via_stance():
    # the plainest form of the directive: hold/advance, then RETREAT (no yield) when enemy within X
    sr = SIDE_A_START_ROW
    ua = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'stance': 'balanced',
                      'width': 6, 'depth': 2, 'troops': 1200, 'starting_position': (sr, 25),
                      'orders': (Order(trigger='enemy_range:6', behavior={'stance': 'retreat'}),)}], 'A', 'A')
    ub = _plain('B', 'aggressive')
    su = ua.units[0]
    with rngsource.using(draw.seeded(draw.H2("test_conditional_orders", 2_000_557))):
        resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
        assert su._order_idx == 1 and su.stance == 'retreat'


# ─── B19.05 (27A-4): an order takes effect by a draw -- the obedience draw at check_orders ───────────────────
# `arm: off` is today's certainty: an order that fires is applied and no draw is taken (no `rngsource` is scoped in the control, so a
# draw would raise). The draws below are made on a hand-built Army with one pending order, checked at its trigger tick.

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA  # noqa: E402
from engine.season.queries.inputs import CommandRecord  # noqa: E402
from modules.mass_battle import config as _mb_config  # noqa: E402
from modules.mass_battle.core.contact import check_orders  # noqa: E402
from modules.mass_battle.hierarchy.units import Army, Unit  # noqa: E402

_MINOR = LEVEL_SIGMA['minor']


def _rec(person='p', score=4, addends=0, levels=0.0, post=None):
    return CommandRecord(person, score, addends, levels, post, ())


def _army_with(order, n_units=1, officer=None, commander=None, post_name=None, gap=0):
    """An Army of `n_units` Units, each holding `order`; unit 0 (named `post`) carries `officer`, the army `commander`. `gap` is
    how far (in columns) each later unit stands from the first."""
    units = [Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 5 + gap * i), advance_dir=1,
                  stance='balanced', unit_type='melee', orders=(order,),
                  officer_record=officer if i == 0 else None) for i in range(n_units)]
    for i, u in enumerate(units):
        u.name = f'u{i}' if i else 'post'
    return Army(name='obey', faction='A', power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6,
                units=units, commander=commander, commander_post=post_name)


def _hold_at_3():
    return Order(trigger='tick:3', behavior={'stance': 'hold'})


def _outcome(army, seed, t=3, slot=0):
    """What the draw did to unit `slot`'s one pending order at tick `t`: 'obeyed', 'late' or 'not'."""
    su = army.units[slot]
    with rngsource.using(draw.seeded(draw.H2("b19_05", seed))):
        check_orders(army, t, [])
    if su._order_idx == 1:
        return 'obeyed'
    return 'late' if su._order_due else 'not'


def _on(monkeypatch, **terms):
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'arm', 'on')
    for k, v in terms.items():
        monkeypatch.setitem(_mb_config.ORDER_OBEY, k, v)


def _share(make, seeds=400, want='obeyed', **kw):
    return sum(1 for s in range(seeds) if _outcome(make(), s, **kw) == want) / seeds


def test_obey_off_applies_every_order_at_its_trigger():
    """CONTROL (gate 1): at `arm: off` every order is applied at its trigger and no draw is taken -- no source is scoped here,
    so a draw would raise LookupError."""
    assert _mb_config.ORDER_OBEY['arm'] == 'off'
    checked = 0
    for _ in range(50):
        army = _army_with(_hold_at_3(), commander=_rec(score=0))
        su = army.units[0]
        check_orders(army, 2, [])
        assert su._order_idx == 0 and su.stance == 'balanced'
        check_orders(army, 3, [])
        assert su._order_idx == 1 and su.stance == 'hold' and su._order_due == 0
        checked += 1
    assert checked >= 50


def test_with_the_draw_on_an_order_is_obeyed_late_or_not(monkeypatch):
    """Gate 2: with `arm: on` a unit with `(tick:3, {stance: hold})` has its order obeyed, late, or not carried out, across 400 fields."""
    _on(monkeypatch)
    counts = {'obeyed': 0, 'late': 0, 'not': 0}
    checked = 0
    for seed in range(400):
        counts[_outcome(_army_with(_hold_at_3()), seed)] += 1
        checked += 1
    assert checked >= 400
    assert all(n > 0 for n in counts.values()), counts


def test_command_score_and_each_attribute_move_the_obeyed_share(monkeypatch):
    """Gate 3: the officer's `command` score gives dice and each attribute gives signed levels; none is folded into the other. The
    host builder that turns Presence and Reason into `levels` is not in this tree, so the attribute halves stand in with signed
    `minor` steps from the mid-point 4 (the size U1 section 4 gives a governing attribute), each attribute alone and both together."""
    _on(monkeypatch)

    def share(**rec):
        return _share(lambda: _army_with(_hold_at_3(), officer=_rec(**rec)))

    def lv(presence=4, reason=4):
        return _MINOR * ((presence - 4) + (reason - 4))

    assert share(score=5) > share(score=0) + 0.2
    assert share(levels=lv(presence=6)) > share(levels=lv(presence=2)) + 0.05          # Presence alone
    assert share(levels=lv(reason=6)) > share(levels=lv(reason=2)) + 0.05              # Reason alone
    assert share(levels=lv(6, 6)) > share(levels=lv(2, 2)) + 0.1                       # both, at equal score


def test_distance_from_the_commanders_post_lowers_the_obeyed_share(monkeypatch):
    """Gate 4: a unit with no officer is rolled on its commander, and the farther it stands from his post (the unit named
    `post`), the lower the obeyed share; with `distance: 0` the near and far fields are equal field for field."""
    _on(monkeypatch, reach=2)

    def build(gap):
        a = _army_with(_hold_at_3(), n_units=2, commander=_rec(score=5), post_name='post', gap=gap)
        a.units[0].orders = ()                      # unit 0 is the post; the order under test is unit 1's
        return a

    near = _share(lambda: build(2), slot=1)
    far = _share(lambda: build(30), slot=1)
    assert near > far + 0.2, (near, far)
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'distance', 0)
    checked = 0
    for seed in range(100):
        assert _outcome(build(2), seed, slot=1) == _outcome(build(30), seed, slot=1)
        checked += 1
    assert checked >= 100
