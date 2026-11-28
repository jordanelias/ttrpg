"""A4, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — go-codes only (NOT
messenger latency, explicitly out of scope for this item).

A sixth Order trigger kind, `signal:NAME`, fires once NAME is present in the issuing Army's
`fired_signals` set (new per-Army transient state, `hierarchy/units.py`'s Army dataclass, cleared at
the campaign battle boundary alongside feigned/overextended -- ED-MB-0022's precedent). An order's
own `behavior` may also set the pseudo-field `fire_signal: NAME`, which adds NAME to `fired_signals`
the moment THAT order's own trigger condition fires -- the real, order-writable, in-battle path a
review found nothing else provided (only a test writing to `fired_signals` directly could exercise
`signal:` at all before this). Propagation is at most one tick, order-dependent (subunit iteration
order decides whether a watcher on the SAME Army sees the signal in the same check_orders call or
the next one) -- no messenger latency is modelled either way.
"""
import pytest

from modules.mass_battle.core.contact import check_orders
from modules.mass_battle.hierarchy.units import Order, Unit, Army
from systems.mass_battle.sim.multi import reset_morale_between_battles  # B17.05: moved out of the module


def _signal_unit(signal_name='advance'):
    su = Unit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(25, 25), advance_dir=1, stance='balanced', unit_type='melee',
                 orders=(Order(f'signal:{signal_name}', {'stance': 'hold'}),))
    return Army(name='signalled', faction='A', power=4, command=4, discipline=5, discipline_start=5,
                morale=6, morale_start=6, units=[su])


def _pair(faction='A'):
    """Two units of one Army: index 0 (`signaler`) fires 'advance' once its own tick:1 trigger
    is met; index 1 (`watcher`) sets stance='hold' once 'signal:advance' fires."""
    signaler = Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 20),
                       advance_dir=1, stance='balanced', unit_type='melee',
                       orders=(Order('tick:1', {'fire_signal': 'advance'}),))
    watcher = Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 30),
                      advance_dir=1, stance='balanced', unit_type='melee',
                      orders=(Order('signal:advance', {'stance': 'hold'}),))
    u = Army(name='pair', faction=faction, power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, units=[signaler, watcher])
    return u, signaler, watcher


def test_signal_is_a_recognized_trigger():
    Order(trigger='signal:advance', behavior={'stance': 'hold'})            # does not raise
    with pytest.raises(ValueError):
        Order(trigger='signl:advance', behavior={'stance': 'hold'})         # typo'd kind
    with pytest.raises(ValueError):
        Order(trigger='signal:', behavior={'stance': 'hold'})               # empty name


def test_fired_signals_defaults_empty_and_inert():
    u = _signal_unit()
    assert u.fired_signals == set()


def test_signal_order_does_not_fire_before_the_signal_is_issued():
    u = _signal_unit('advance')
    su = u.units[0]
    check_orders(u, 1, [])
    assert su._order_idx == 0, "signal:advance must not fire before 'advance' is in fired_signals"
    assert su.stance == 'balanced'


def test_signal_order_fires_once_the_signal_is_issued():
    u = _signal_unit('advance')
    su = u.units[0]
    check_orders(u, 1, [])
    assert su._order_idx == 0
    u.fired_signals.add('advance')
    check_orders(u, 2, [])
    assert su._order_idx == 1, "signal:advance must fire on the next check once 'advance' is signalled"
    assert su.stance == 'hold'


def test_signal_order_ignores_an_unrelated_signal():
    u = _signal_unit('advance')
    su = u.units[0]
    u.fired_signals.add('retreat')   # a DIFFERENT signal is live
    check_orders(u, 1, [])
    assert su._order_idx == 0, "a differently-named signal must not fire this order"
    assert su.stance == 'balanced'


# ─── Adversarial-review round 2: a real in-battle path to fire a signal ──────

def test_fire_signal_is_a_recognized_order_safe_field():
    Order(trigger='tick:1', behavior={'fire_signal': 'advance'})   # does not raise
    with pytest.raises(ValueError):
        Order(trigger='tick:1', behavior={'fire_signal': ''})      # empty name


def test_fire_signal_adds_the_name_to_fired_signals():
    su = Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 25),
                 advance_dir=1, stance='balanced', unit_type='melee',
                 orders=(Order('tick:1', {'fire_signal': 'advance'}),))
    u = Army(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, units=[su])
    assert u.fired_signals == set()
    check_orders(u, 1, [])
    assert u.fired_signals == {'advance'}
    assert su._order_idx == 1
    assert not hasattr(su, 'fire_signal'), "'fire_signal' must not leak onto the Unit as a real attribute"


def test_fire_signal_end_to_end_when_the_signaler_is_checked_first():
    """The signaling subunit is index 0 -- its own turn through check_orders' per-subunit loop
    happens before the watcher's, so the watcher sees the signal WITHIN THE SAME call."""
    u, signaler, watcher = _pair()
    check_orders(u, 1, [])
    assert signaler._order_idx == 1
    assert watcher._order_idx == 1, "the watcher must see the signal within the same check_orders call when checked after the signaler"
    assert watcher.stance == 'hold'


def test_fire_signal_end_to_end_when_the_watcher_is_checked_first():
    """Same two orders, subunit list order reversed: the watcher's own turn is taken BEFORE the
    signaler's this tick, so it must wait one more call -- an honest, disclosed, order-dependent
    property (not messenger latency, which stays out of scope), not "always next call"."""
    u, signaler, watcher = _pair()
    u.units = [watcher, signaler]
    check_orders(u, 1, [])
    assert watcher._order_idx == 0 and watcher.stance == 'balanced', \
        "checked before the signal existed this tick -- must not fire yet"
    check_orders(u, 2, [])
    assert watcher._order_idx == 1 and watcher.stance == 'hold', \
        "must fire on the very next check once the signal is live"


def test_fired_signals_is_cleared_at_the_battle_boundary():
    """ED-MB-0022 precedent: feigned/overextended are per-battle transient flags cleared at
    reset_morale_between_battles; fired_signals is the same kind of state and must not leak a
    go-code from one campaign battle into the next."""
    u = _signal_unit('advance')
    u.fired_signals.add('advance')
    assert u.fired_signals == {'advance'}
    reset_morale_between_battles(u)
    assert u.fired_signals == set(), "fired_signals must be cleared at the battle boundary"


# ─── Adversarial-review round 2, F11 -- eager validation gaps ───────────────

def test_fire_signal_rejects_a_non_string_value():
    """F11: `fire_signal`'s value was checked only for truthiness, not type -- an int raised
    nothing useful (added to fired_signals silently, never matches a string 'signal:NAME'
    trigger's own str split), a list raised an unhashable-type TypeError deep inside
    `unit.fired_signals.add(v)`, mid-battle, far from where the mistake was made. Must fail loudly
    at Order construction instead, matching this class's own eager-validation doctrine."""
    with pytest.raises(ValueError, match="string"):
        Order(trigger='immediate', behavior={'fire_signal': 5})
    with pytest.raises(ValueError, match="string"):
        Order(trigger='immediate', behavior={'fire_signal': ['advance']})


# ─── B19.05 (27A-4): the obedience draw on a signal ──────────────────────────────────────────────────────────

from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import config as _mb_config, rngsource  # noqa: E402


def _army_on(orders_per_unit):
    """An Army whose unit i holds `orders_per_unit[i]`, none with an officer or a commander record (the default roller)."""
    units = [Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 5 + 3 * i), advance_dir=1,
                  stance='balanced', unit_type='melee', orders=tuple(o)) for i, o in enumerate(orders_per_unit)]
    return Army(name='sig', faction='A', power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6,
                units=units)


def _check(army, seed, t=1):
    with rngsource.using(draw.seeded(draw.H2("b19_05_signals", seed))):
        check_orders(army, t, [])


def test_a_unit_on_two_signals_can_misread_and_on_one_cannot(monkeypatch):
    """A unit holding orders on two different signals can answer the wrong one (it applies the other order, now, and the one
    signalled stays pending); a unit on one signal is only ever on time, late or not carried out, never misread."""
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'arm', 'on')
    misread = late_or_not = checked = 0
    for seed in range(400):
        two = _army_on([[Order('signal:a', {'stance': 'hold'}), Order('signal:b', {'stance': 'aggressive'})]])
        two.fired_signals.add('a')
        _check(two, seed)
        su = two.units[0]
        if su.stance == 'aggressive':               # the other signal's order was answered
            assert su._order_idx == 0 and len(su.orders) == 1 and su.orders[0].trigger == 'signal:a'
            misread += 1
        one = _army_on([[Order('signal:a', {'stance': 'hold'})]])
        one.fired_signals.add('a')
        _check(one, seed)
        s1 = one.units[0]
        assert s1.stance in ('balanced', 'hold') and len(s1.orders) == 1, "a unit on one signal has no other order to answer"
        late_or_not += s1._order_idx == 0
        checked += 1
    assert checked >= 400
    assert misread > 0, "a unit on two signals never misread in 400 fields"
    assert late_or_not > 0, "a unit on one signal was never late or not carried out"


def test_more_units_on_one_signal_answer_together_less_often(monkeypatch):
    """The across-units term: one signal waited on by eight units is obeyed less often, per unit, than by three."""
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'arm', 'on')

    def obeyed_share(n):
        got = 0
        for seed in range(300):
            a = _army_on([[Order('signal:go', {'stance': 'hold'})] for _ in range(n)])
            a.fired_signals.add('go')
            _check(a, seed)
            got += a.units[0]._order_idx == 1
        return got / 300

    assert obeyed_share(3) > obeyed_share(8) + 0.2
