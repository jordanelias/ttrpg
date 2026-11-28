"""A3 + C5 (ED-MB-0067 Part A / Part C, ED-MB-0073) — subordinate-officer Cmd / span-of-control.

ED-1090 (2026-07-02) left this open: the ratified Command formula clamps to 1..7, so
`UNIT_CAP=11` (`engine.py`) implies "a future Command-exceeding mechanism (e.g. subordinate
officers/lieutenancy) -- a future ED, not silently invented in the constructor." This is that ED.

`Officer` (`hierarchy/units.py`) holds its own Command, derived the SAME way a general's is
(`derive_command`, ED-899) -- no second formula one echelon down. `build_army`'s new `officers=`
parameter (default `()`, zero behavior change for every existing caller) replaces the flat
`UNIT_CAP` ceiling with C5's ruled span-of-control ladder (ED-MB-0067 Part C, ruled 2026-09-25:
"one ladder... max commanded = Command... at every echelon, including the new officer post") checked
at TWO levels: each officer's own subunit count <= that officer's own Command, and the general's own
direct reports (distinct officers used + any un-officered units) <= the general's own Command.
"""
import pytest

from systems.mass_battle.sim.engine import build_army, UNIT_CAP


def _line_spec(officer=None):
    sp = {'shape': 'Line', 'troop_type': 'infantry', 'tier': 3}
    if officer is not None:
        sp['officer'] = officer
    return sp


def test_officers_default_is_backward_compatible_with_the_flat_cap():
    """officers=() (the default) must reproduce ED-1090's exact flat UNIT_CAP check, unchanged --
    every existing caller of build_army never passes officers, so this must be byte-exact."""
    u = build_army([_line_spec() for _ in range(UNIT_CAP)], 'Army', 'A', command=4)
    assert u.officers == ()
    assert all(s.officer is None for s in u.units)

    with pytest.raises(ValueError, match='exceeds the videogame cap'):
        build_army([_line_spec() for _ in range(UNIT_CAP + 1)], 'TooMany', 'A', command=4)


# ─── B19.05 (27A-4): who rolls the obedience draw ────────────────────────────────────────────────────────────

from engine.dice_engine import draw  # noqa: E402
from engine.season.queries.inputs import CommandRecord  # noqa: E402
from modules.mass_battle import config as _mb_config, rngsource  # noqa: E402
from modules.mass_battle.core import contact  # noqa: E402
from modules.mass_battle.hierarchy.units import Army, Order, Unit  # noqa: E402


def _rec(person, score=4):
    return CommandRecord(person, score, 0, 0.0, None, ())


def _army(officer=None, commander=None):
    su = Unit(shape='Line', troop_type='infantry', tier=2, starting_position=(25, 25), advance_dir=1, stance='balanced',
              unit_type='melee', orders=(Order('tick:3', {'stance': 'hold'}),), officer_record=officer)
    return Army(name='off', faction='A', power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6,
                units=[su], commander=commander)


def test_a_standing_order_is_rolled_by_the_units_officer(monkeypatch):
    """A standing order with a local trigger is drawn once, on the unit's officer; a unit with none, on the commander."""
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'arm', 'on')
    seen = []
    real = contact.obey

    def spy(order, roller, *a, **kw):
        seen.append(roller.person)
        return real(order, roller, *a, **kw)

    monkeypatch.setattr(contact, 'obey', spy)
    for army, expect in ((_army(officer=_rec('officer'), commander=_rec('commander')), ['officer']),
                         (_army(commander=_rec('commander')), ['commander'])):
        seen.clear()
        with rngsource.using(draw.seeded(draw.H2("b19_05_officers", 1))):
            contact.check_orders(army, 3, [])
        assert seen == expect, seen


def test_an_improvised_order_to_an_officered_unit_draws_twice(monkeypatch):
    """An order drawn once for each person who has to pass it on: a standing order one link, an improvised order the
    commander and then the officer (two), to an unofficered unit the commander only. Read off the sampler's calls; the
    improvised path reaches `obey` when B20's `CommanderAction` lands, so `obey`'s `link` argument is called directly."""
    monkeypatch.setitem(_mb_config.ORDER_OBEY, 'arm', 'on')
    keys = []
    real = contact.roll_net_continuous

    def counting(pool, *a, rng, **kw):
        keys.append(rng.key)
        return real(pool, *a, rng=rng, **kw)

    monkeypatch.setattr(contact, 'roll_net_continuous', counting)

    def draws(army, source):
        keys.clear()
        order = Order('immediate', {'stance': 'hold'})
        sub = army.units[0]
        with rngsource.using(draw.seeded(draw.H2("b19_05_officers", 2))):
            for link, roller in enumerate(contact._roller_for(army, sub, source)):
                contact.obey(order, roller, sub, army, 3, link)
        return list(keys)

    officered = _army(officer=_rec('officer'), commander=_rec('commander'))
    bare = _army(commander=_rec('commander'))
    two = draws(officered, 'improvised')
    assert len(two) == 2 and len(set(two)) == 2, "one draw per link, each on its own key"
    assert len(draws(officered, 'standing')) == 1
    assert len(draws(bare, 'improvised')) == 1
