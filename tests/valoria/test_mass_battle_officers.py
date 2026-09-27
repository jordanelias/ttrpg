"""A3 + C5 (ED-MB-0067 Part A / Part C, ED-MB-0073) — subordinate-officer Cmd / span-of-control.

ED-1090 (2026-07-02) left this open: the ratified Command formula clamps to 1..7, so
`SUBUNIT_CAP=11` (`engine.py`) implies "a future Command-exceeding mechanism (e.g. subordinate
officers/lieutenancy) -- a future ED, not silently invented in the constructor." This is that ED.

`Officer` (`hierarchy/units.py`) holds its own Command, derived the SAME way a general's is
(`derive_command`, ED-899) -- no second formula one echelon down. `build_army`'s new `officers=`
parameter (default `()`, zero behavior change for every existing caller) replaces the flat
`SUBUNIT_CAP` ceiling with C5's ruled span-of-control ladder (ED-MB-0067 Part C, ruled 2026-09-25:
"one ladder... max commanded = Command... at every echelon, including the new officer post") checked
at TWO levels: each officer's own subunit count <= that officer's own Command, and the general's own
direct reports (distinct officers used + any un-officered subunits) <= the general's own Command.
"""
import pytest

from systems.mass_battle.sim.engine import build_army, SUBUNIT_CAP
from systems.mass_battle.sim.hierarchy.units import Officer


def _line_spec(officer=None):
    sp = {'shape': 'Line', 'troop_type': 'infantry', 'tier': 3}
    if officer is not None:
        sp['officer'] = officer
    return sp


def test_officer_command_defaults_to_tier3_baseline():
    """No charisma/cognition -> the same command=4 default build_army's own general parameter uses,
    not an invented 'quality tier' table (Part A's own text names one; C5 doesn't specify its
    magnitudes, so this reuses the existing baseline rather than fabricating new numbers)."""
    o = Officer(name='Aulus')
    assert o.command == 4


def test_officer_command_derives_from_charisma_and_cognition_like_a_general():
    """Same derivation a Unit's own Command uses (derive_command, ED-899) -- no second formula."""
    from systems.mass_battle.sim.core.exchange import derive_command
    o = Officer(name='Aulus', charisma=6, cognition=4)
    assert o.command == derive_command(6, 4)


def test_officer_command_clamps_to_1_7():
    assert Officer(name='X', command=99).command == 7
    assert Officer(name='X', command=0).command == 1
    assert Officer(name='X', command=-5).command == 1


def test_officers_default_is_backward_compatible_with_the_flat_cap():
    """officers=() (the default) must reproduce ED-1090's exact flat SUBUNIT_CAP check, unchanged --
    every existing caller of build_army never passes officers, so this must be byte-exact."""
    u = build_army([_line_spec() for _ in range(SUBUNIT_CAP)], 'Army', 'A', command=4)
    assert u.officers == ()
    assert all(s.officer is None for s in u.subunits)

    with pytest.raises(ValueError, match='exceeds the videogame cap'):
        build_army([_line_spec() for _ in range(SUBUNIT_CAP + 1)], 'TooMany', 'A', command=4)


def test_a_general_fields_more_than_command_subunits_through_officers():
    """THE 'DONE WHEN' CRITERION (Part A, A3): a general with Command c fields more than c
    sub-units through officers. c=3 here; 12 subunits (already > SUBUNIT_CAP=11) fielded through
    3 officers of Command 4 each -- each officer's own span (4) and the general's own direct
    reports (3 officers <= Command 3) both hold."""
    officers = [{'name': f'O{i}', 'command': 4} for i in range(3)]
    specs = [_line_spec(officer=f'O{i}') for i in range(3) for _ in range(4)]
    assert len(specs) > SUBUNIT_CAP
    u = build_army(specs, 'GeneralArmy', 'A', command=3, officers=officers)
    assert len(u.subunits) == 12 > 3  # more subunits than the general's own Command
    assert {o.name for o in u.officers} == {'O0', 'O1', 'O2'}
    assert all(o.command == 4 for o in u.officers)
    for i in range(3):
        assigned = [s for s in u.subunits if s.officer == f'O{i}']
        assert len(assigned) == 4


def test_an_officer_over_assigned_beyond_their_own_command_raises():
    with pytest.raises(ValueError, match="commands 5 subunits, exceeding their own Command 3"):
        build_army([_line_spec(officer='X') for _ in range(5)], 'Bad', 'A',
                   command=5, officers=[{'name': 'X', 'command': 3}])


def test_a_general_over_assigned_beyond_their_own_command_raises():
    """The SAME ladder applies one echelon up: the general's own direct reports (here, 5 distinct
    officers, none of them individually over-assigned) must also respect Command."""
    officers = [{'name': f'O{i}', 'command': 1} for i in range(5)]
    specs = [_line_spec(officer=f'O{i}') for i in range(5)]
    with pytest.raises(ValueError, match='general commands 5 direct reports'):
        build_army(specs, 'Bad2', 'A', command=2, officers=officers)


def test_unofficered_subunits_count_as_direct_reports_alongside_officers():
    """A mixed army: 2 officers + 1 un-officered subunit = 3 direct reports to the general."""
    officers = [{'name': 'O0', 'command': 4}, {'name': 'O1', 'command': 4}]
    specs = [_line_spec(officer='O0'), _line_spec(officer='O1'), _line_spec()]
    u = build_army(specs, 'Mixed', 'A', command=3, officers=officers)
    assert len(u.subunits) == 3
    assert sum(1 for s in u.subunits if s.officer is None) == 1

    # Same shape, but the general's own Command is now too small for 2 officers + 1 direct report.
    with pytest.raises(ValueError, match='general commands 3 direct reports \\(2 officers \\+ 1'):
        build_army(specs, 'Mixed2', 'A', command=2, officers=officers)


def test_referencing_an_unknown_officer_name_raises():
    with pytest.raises(ValueError, match="officer 'Ghost' is not in officers"):
        build_army([_line_spec(officer='Ghost')], 'Bad3', 'A', command=4,
                   officers=[{'name': 'Real', 'command': 4}])


def test_duplicate_officer_names_raise():
    with pytest.raises(ValueError, match='duplicate officer name'):
        build_army([_line_spec(officer='X')], 'Bad4', 'A', command=4,
                   officers=[{'name': 'X', 'command': 4}, {'name': 'X', 'command': 2}])


def test_officers_may_be_passed_as_instances_not_only_dicts():
    o = Officer(name='Instance', command=4)
    u = build_army([_line_spec(officer='Instance')], 'InstArmy', 'A', command=4, officers=[o])
    assert u.officers == (o,)
