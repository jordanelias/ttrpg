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
