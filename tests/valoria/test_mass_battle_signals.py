"""A4, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — go-codes only (NOT
messenger latency, explicitly out of scope for this item).

A sixth Order trigger kind, `signal:NAME`, fires once NAME is present in the issuing Unit's
`fired_signals` set (new per-Unit transient state, `hierarchy/units.py`'s Unit dataclass, cleared at
the campaign battle boundary alongside feigned/overextended -- ED-MB-0022's precedent). An order's
own `behavior` may also set the pseudo-field `fire_signal: NAME`, which adds NAME to `fired_signals`
the moment THAT order's own trigger condition fires -- the real, order-writable, in-battle path a
review found nothing else provided (only a test writing to `fired_signals` directly could exercise
`signal:` at all before this). Propagation is at most one tick, order-dependent (subunit iteration
order decides whether a watcher on the SAME Unit sees the signal in the same check_orders call or
the next one) -- no messenger latency is modelled either way.
"""
import pytest

from systems.mass_battle.sim.core.contact import check_orders
from systems.mass_battle.sim.hierarchy.units import Order, Subunit, Unit
from systems.mass_battle.sim.orchestration import reset_morale_between_battles


def _signal_unit(signal_name='advance'):
    su = Subunit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(25, 25), advance_dir=1, stance='balanced', unit_type='melee',
                 orders=(Order(f'signal:{signal_name}', {'stance': 'hold'}),))
    return Unit(name='signalled', faction='A', power=4, command=4, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=[su])


def _pair(faction='A'):
    """Two subunits of one Unit: index 0 (`signaler`) fires 'advance' once its own tick:1 trigger
    is met; index 1 (`watcher`) sets stance='hold' once 'signal:advance' fires."""
    signaler = Subunit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 20),
                       advance_dir=1, stance='balanced', unit_type='melee',
                       orders=(Order('tick:1', {'fire_signal': 'advance'}),))
    watcher = Subunit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 30),
                      advance_dir=1, stance='balanced', unit_type='melee',
                      orders=(Order('signal:advance', {'stance': 'hold'}),))
    u = Unit(name='pair', faction=faction, power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[signaler, watcher])
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
    su = u.subunits[0]
    check_orders(u, 1, [])
    assert su._order_idx == 0, "signal:advance must not fire before 'advance' is in fired_signals"
    assert su.stance == 'balanced'


def test_signal_order_fires_once_the_signal_is_issued():
    u = _signal_unit('advance')
    su = u.subunits[0]
    check_orders(u, 1, [])
    assert su._order_idx == 0
    u.fired_signals.add('advance')
    check_orders(u, 2, [])
    assert su._order_idx == 1, "signal:advance must fire on the next check once 'advance' is signalled"
    assert su.stance == 'hold'


def test_signal_order_ignores_an_unrelated_signal():
    u = _signal_unit('advance')
    su = u.subunits[0]
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
    su = Subunit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 25),
                 advance_dir=1, stance='balanced', unit_type='melee',
                 orders=(Order('tick:1', {'fire_signal': 'advance'}),))
    u = Unit(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[su])
    assert u.fired_signals == set()
    check_orders(u, 1, [])
    assert u.fired_signals == {'advance'}
    assert su._order_idx == 1
    assert not hasattr(su, 'fire_signal'), "'fire_signal' must not leak onto the Subunit as a real attribute"


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
    u.subunits = [watcher, signaler]
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
