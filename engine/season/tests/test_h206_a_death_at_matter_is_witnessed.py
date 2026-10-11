"""H-206 -- A DEATH WRITTEN AT MATTER HAS A PLACE, SO IT IS WITNESSED.

THE DEFECT, MEASURED ON `build_realm(0)` BEFORE THE FIX (one seat-holder forced to a MATTER death,
one season, `fan_out_mode: all_five`): `person.died` found NO observer and 0 claims in any ledger named
the dead holder. `World.remove_person` takes him out of `w.persons` and closes every edge naming him in
the write that kills him; WITNESS runs after; an Event no act caused anchors on the removed person
(`state/attribution.py` tier 2), and `place_of` of a person is his LIVE `contain` edge -- gone. A death
at RESOLVE anchors on the killer, who is alive, so only the MATTER-written one was lost.

THE FIX under test is `world_q.event_place`: an Event about a person the world no longer holds is placed
where `remove_person` took him out, if that was the Event's own tick.

  * FALSIFIER -- a MATTER-written `person.died` for a seat-holder (`tiny_world`'s `p_high`, who holds
    `off_duke`) deposits claims naming him on every person standing where he stood, and on nobody
    elsewhere; each count is asserted to be at least one in the direction it must be (so a loop that
    found nobody cannot pass for "none out of reach").
  * CONTROL -- the same death written at RESOLVE by a killer (the real fold, the real `fight`) deposits
    EXACTLY what it deposited before the fix: the ledgers equal those of the same run with
    `event_place` put back to `place_of(w, anchor_of(w, e))`.
  * NARROW -- the dead man is still nowhere for `place_of` (a claim ABOUT him read by `reach` is not
    moved), and an Event of any other tick has no place for him.
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.attribution import anchor_of
from ..state.carriers import Act, Person, Rung, Tenure
from ..state.ids import ROOT

HOLDER, OFFICE = "p_high", "off_duke"
NEAR, FAR = ("p_near",), ("p_low", "p_mid", "p_other", "p_king")     # S is where p_high stands


def _world():
    """`tiny_world` (p_high holds `off_duke` and stands at `S`), plus `p_near`, who also stands at `S`;
    the rest stand at `Hh` or `R`."""
    w = P.tiny_world()
    w.persons["p_near"] = Person("p_near", "a neighbour")
    w.rungs["p_near"] = Rung("p_near", "person")
    w.add_tenure(Tenure("t_near_in", "p_near", "S", "contain", 0))
    w.add_tenure(Tenure("t_near_home", "p_near", "S", world_q.RESIDE_KIND, 0))
    assert world_q.home_of(w)[HOLDER] == "S" == world_q.home_of(w)["p_near"]
    return w


def _names_him(w, pid):
    """Claims in `pid`'s ledger about the dead holder or his office. (His closed `hold` is not a
    subject a claim can name: the edge left the store with its owner, and the Event does not list it.)"""
    return [c for c in w.persons[pid].ledger if c.subject in {HOLDER, OFFICE}]


def _die_at_matter(w):
    w.step = Step.MATTER
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person(HOLDER),
            record_kind="Person", fieldname="exists", driver="Event",
            emits="person.died", subject=HOLDER, causes=[ROOT])
    (ev,) = w._emitted_by_write
    return ev


def _witness(w, evs):
    SeasonDriver(w).witness(mint_token(w, WriteClass.INTERIOR), evs)


def test_h206_a_matter_death_is_witnessed_by_those_who_stood_there_and_nobody_else():
    w = _world()
    assert any(t.kind == "hold" and t.subject == HOLDER and t.object == OFFICE and t.live
               for t in w.tenures), "fixture: p_high does not hold off_duke"
    assert w.fixtures.get("fan_out_mode") == "all_five", "the shipped fan-out arm moved"
    ev = _die_at_matter(w)
    assert HOLDER not in w.persons and not any(t.live and OFFICE == t.object for t in w.tenures), (
        "fixture: the seat did not fall vacant")
    assert anchor_of(w, ev) == HOLDER and world_q.place_of(w, HOLDER) is None
    assert world_q.event_place(w, ev) == "S"

    _witness(w, [ev])

    near = {p: _names_him(w, p) for p in NEAR}
    far = {p: _names_him(w, p) for p in FAR}
    assert sum(len(v) for v in near.values()) >= 1, "no one standing at S holds a claim naming him"
    assert len(far) >= 1 and all(p in w.persons for p in far), "fixture: nobody stands elsewhere"
    assert sum(len(v) for v in far.values()) == 0, (
        f"a claim naming the dead holder reached persons elsewhere: {far}")


def test_h206_mutation_with_the_place_put_back_the_matter_death_reaches_nobody(monkeypatch):
    """THE MUTATION, run as a test: `event_place` as it was (`place_of(w, anchor_of(w, e))`). The
    positive half of the falsifier must go red, which is what makes it an observation."""
    monkeypatch.setattr(world_q, "event_place", lambda w, e: world_q.place_of(w, anchor_of(w, e)))
    w = _world()
    _witness(w, [_die_at_matter(w)])
    assert sum(len(_names_him(w, p)) for p in NEAR) == 0, (
        "the old expression reaches someone; the defect this file pins is not the one it describes")


def test_h206_the_dead_man_is_still_nowhere_for_place_of_and_an_event_of_another_tick_has_no_place():
    w = _world()
    ev = _die_at_matter(w)
    assert world_q.place_of(w, HOLDER) is None, "`place_of` was widened; `reach` reads it about the dead"
    w.tick += 1
    assert world_q.event_place(w, ev) == "S", "the Event's own tick is the key, not the world's"
    later = type(ev)(id="later", kind="body.changed", changes=ev.changes, causes=[ROOT],
                     emitted_at=ev.emitted_at + 1)
    assert world_q.event_place(w, later) is None, "an Event of another tick was placed"
    assert w.departed_from("p_near", 0) is None, "a person still here has no departure"


def _fight_until_he_dies(model_ids=range(40)):
    """The real fold, the real `fight`: p_near fights p_high under `wound_harm_model = total` (a
    wound kills) until one act id kills him. Returns the world and the Events, or None if no id did."""
    from ..seam.wrappers import combat as C
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")
    for i in model_ids:
        w = _world()
        w.step = Step.RESOLVE
        w.fixtures = w.fixtures.sweep("wound_harm_model", "total")
        d = SeasonDriver(w)
        evs = d.resolve(mint_token(w, WriteClass.ACTS),
                        [Act(id=f"h206_{i}", actor="p_near", verb="fight", payload={"subject": HOLDER})],
                        w.fixtures.get("contest_max_depth"))
        if HOLDER not in w.persons:
            for ev in evs:              # `resolve` returns the Events; the caller logs them (as a barrier does)
                w.log.append(ev)
            return w, evs
    return None


def _ledgers(w):
    return {pid: sorted((c.subject, c.predicate, c.source, str(c.value)) for c in p.ledger)
            for pid, p in w.persons.items()}


def test_h206_control_a_death_at_resolve_by_a_killer_deposits_what_it_deposited_before(monkeypatch):
    got = _fight_until_he_dies()
    assert got is not None, "no act id in range killed p_high; the control would be vacuous"
    w, evs = got
    died = [e for e in evs if e.kind == "person.died"]
    assert died and anchor_of(w, died[0]) == "p_near", "fixture: the death is not anchored on the killer"
    w.step = Step.WITNESS
    _witness(w, evs)
    after = _ledgers(w)
    deposited = sum(len(v) for v in after.values())
    assert deposited >= 1, "the RESOLVE death deposited nothing; the equality below would be empty"

    monkeypatch.setattr(world_q, "event_place", lambda w, e: world_q.place_of(w, anchor_of(w, e)))
    w2, evs2 = _fight_until_he_dies()
    w2.step = Step.WITNESS
    _witness(w2, evs2)
    assert _ledgers(w2) == after, "the fix moved what a RESOLVE-written death deposits"
