"""v12 B21b.01 (IN-36 (a), A-103): AT MOST ONE MARCH A SEASON INTO EACH TERRITORY, AS A TYPED CONJUNCT OF `march`'S CELL.

`Fixtures.march_cap_per_territory` (shipped 1; 0 or a registered None = no cap). The conjunct counts the `march.declared` Events of the
current `w.tick` whose act's target lies in the asked target's territory (a settlement counts for its territory), and holds
while that count, with this march, is within the cap. It is read by the one admission path, `loop/resolve.py::_admits`, and
refuses on the row's own `march.refused`. Each test folds REAL acts through the real driver (`test_march.py::_fold_one`) and
hands the Events to the log between folds as `SeasonDriver.season()` does at the end of a lap, so what is observed is the
fold's refusal and never a hand-set verdict.

⚠ REACH, STATED: the log takes a lap's Events at the lap's end (`loop/driver.py`), so the cap sees the marches of EARLIER
laps of the tick and not of its own lap. That is the plan's reading (`w.log` at the current tick), not something this file
asserts either way.
"""
from engine.season.queries import world_q

from ._dispatch_realm import realm_seating_dispatch as build_realm
from .test_march import _fold_one, _march_act

CAP = "march_cap_per_territory"
#: The two seats that may march (`_dispatch_realm.MARCH_SEATS`): the Crown's Spymaster and the Church's Cardinal.
SPY, CARDINAL = ("p_npc_033", "off_spymaster"), ("p_npc_013", "off_cardinal_prudence")


def _march(w, marcher, target, act_id):
    """Fold one real march through RESOLVE and ENCOUNTER, then give its Events to the log as a lap's end does."""
    events = _fold_one(w, _march_act(marcher[0], target, marcher[1], act_id))
    for e in events:
        w.log.append(e)
    return [e.kind for e in events], events


def _cap_reads(events):
    """The cap's own two reads (`march.nth`, `march.cap`) on a refusal's `observed`: the proof the CAP refused, not the cell's other conjunct."""
    return {o.predicate: o.value for e in events for o in e.observed if o.predicate in ("march.nth", "march.cap")}


def test_a_second_march_into_one_territory_in_one_season_is_refused():
    w = build_realm(0)
    assert w.fixtures.get(CAP) == 1
    first, _ = _march(w, SPY, "set_s_001", "m_cap_1")
    assert "march.declared" in first, first
    second, events = _march(w, CARDINAL, "set_s_001", "m_cap_2")
    assert "march.declared" not in second, second
    assert second == ["march.refused"], second
    assert _cap_reads(events) == {"march.nth": 2, "march.cap": 1}, _cap_reads(events)
    # the cap is per territory: the same marcher, a march into another territory, the same tick, is admitted
    other, _ = _march(w, CARDINAL, "set_s_004", "m_cap_3")
    assert "march.declared" in other, other
    # the count is of the current tick's Events alone: the next season admits a march into the same territory again
    w.tick += 1
    next_season, _ = _march(w, CARDINAL, "set_s_002", "m_cap_4")
    assert "march.declared" in next_season, next_season
    # the fixture's documented semantic, which is also the mutation of this test: 0 (or a registered None) is no cap,
    # so the second march into the territory is admitted and the cap's two reads are the no-cap pair (0, 0)
    for off in (0, None):
        w_off = build_realm(0)
        w_off.fixtures = w_off.fixtures.sweep(CAP, off)
        _march(w_off, SPY, "set_s_001", "m_cap_1")
        both, events_off = _march(w_off, CARDINAL, "set_s_002", "m_cap_2")
        assert "march.declared" in both, (off, both)
        assert _cap_reads(events_off) == {"march.nth": 0, "march.cap": 0}, (off, _cap_reads(events_off))


def test_a_march_on_a_settlement_counts_against_its_territory():
    w = build_realm(0)
    assert world_q.ancestry(w, "set_s_001")[1] == world_q.ancestry(w, "set_s_002")[1] == "terr_T1"
    first, _ = _march(w, SPY, "set_s_001", "m_cap_1")
    assert "march.declared" in first, first
    # a sibling settlement of the same territory: refused
    sibling, events = _march(w, CARDINAL, "set_s_002", "m_cap_2")
    assert sibling == ["march.refused"] and _cap_reads(events)["march.nth"] == 2, (sibling, _cap_reads(events))
    # the territory's own rung is the same count (a march on the territory is a march into it)
    w2 = build_realm(0)
    _march(w2, SPY, "set_s_001", "m_cap_1")
    whole, events2 = _march(w2, CARDINAL, "terr_T1", "m_cap_2")
    assert whole == ["march.refused"] and _cap_reads(events2)["march.nth"] == 2, (whole, _cap_reads(events2))
