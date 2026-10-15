"""IN-55 / RS-24 -- the fan skip: an Event that changes only held Claims is witnessed by nobody.

`epistemic.changes_only_held_claims` is a DERIVED per-Event predicate (no act among the causes; every
`changes[]` subject is a claim id some ledger holds NOW), and `loop/witness.py::witness` does not ask
`observers_for` about an Event it selects. Skipping is sound only if `observers_for` would have answered
`[]`, so what each clause observes is that:

  (a) `test_m_skip_every_selected_event_has_no_observer_under_all_five` -- THE M-SKIP. Over two seasons
      of `populated.build_realm(0)` (decay first fires in the second), at the entry of every WITNESS
      barrier (the ledgers as the fan will read them), the predicate selects Events; each is put to the real, unskipped `observers_for`
      under the shipped `all_five`, and must answer `[]`. It asserts it checked (`>= MIN_SELECTED`),
      so a predicate that selected nothing cannot pass for a clean one. Independent of the wiring: it
      calls `observers_for` itself.
  (b) `test_the_wired_skip_is_taken_for_the_selected_events` -- the wiring: with `observers_for` spied
      on, no selected Event reaches it from WITNESS and every other Event still does.
  (c) the control -- `test_a_matter_death_is_not_selected_and_the_rejected_predicate_would_skip_it`:
      "every change subject resolves in no World store" (the formulation the plan rejects) selects a
      MATTER death, and wired in place of the real predicate it silences H-206's witnesses; the real
      predicate does not select it. (The same swap turns
      `test_h206_a_death_at_matter_is_witnessed.py` red -- run by hand, not committed.)
  (d) the predicate on hand-built Events: held-claim-only is selected; a claim beside a person subject,
      an Event with an act, a claim no ledger holds, a claim removed in the same Event, no change, a
      change with no subject are not.
  (e) `test_the_control_arm_total_is_never_skipped_...` -- under `total` the same Event fans to
      everyone, so the predicate (which takes the mode) refuses it; the other two arms answer `[]`.
      Found red on the first wiring, by `test_season_shape.py::test_r7_two_persons_hold_...`.
  (f) `test_the_skip_changes_the_work_and_nothing_else` -- A/B over `SEASONS` seasons: the same hash
      and log with the predicate forced False, and the skip arm asserts the predicate selected at
      least `MIN_SELECTED` Events. (a) also pins the selected-kind census to `claim.decayed`.
  (g) `test_a_kind_the_chronicle_admits_is_not_selected` -- a planted `binding_decision` row emitting
      the held-claim-only kind makes `chronicle` admit it, and the predicate refuses it.
"""

from __future__ import annotations

import pytest

from .. import epistemic as EP
from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..harness import probes as P
from ..loop import witness as WIT
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Claim, Event, Person, Rung, Tenure
from ..state.ids import ROOT
from ..queries import world_q

MIN_SELECTED = 1000      # a one-season realm run selects thousands; zero must fail, not pass


def _claim(cid, holder, subject="p_high"):
    return Claim(cid, holder, subject, "is_loyal", True, 0, "firsthand", 100, "own")


SEASONS = 2     # decay is first reachable in the SECOND season (the first has no claim to decay)


@pytest.fixture(scope="module")
def season_run():
    """ONE `SEASONS`-season realm run serving (a) and (b). At the entry of every WITNESS barrier -- the
    ledgers as the fan will read them, since nothing writes between that entry and the fan -- the
    predicate is put to every Event; each selected one is put to the real `observers_for`; and while
    the real barrier runs, `witness`'s own `observers_for` is spied on to see which Events it is asked."""
    out = {"selected": 0, "barrier_events": 0, "observers": [], "kinds": {}, "mode": None,
           "asked_selected": 0, "asked_other": 0}
    w = POP.build_realm(0)
    real_obs, orig = WIT.observers_for, SeasonDriver.witness

    def wrapped(self, token, events):
        w_ = self.w
        w_.discard_caches()
        mode = out["mode"] = w_.fixtures.get("fan_out_mode")
        everyone, held = list(w_.persons), EP.held_claim_ids(w_)
        chosen = set()
        for e in events:
            out["barrier_events"] += 1
            if EP.changes_only_held_claims(w_, e, held, mode):
                chosen.add(e.id)
                out["selected"] += 1
                out["kinds"][e.kind] = out["kinds"].get(e.kind, 0) + 1
                got = real_obs(w_, e, mode, everyone)
                if got:
                    out["observers"].append((e.id, e.kind, got[:3]))

        def asked(w2, e, m, ev):
            out["asked_selected" if e.id in chosen else "asked_other"] += 1
            return real_obs(w2, e, m, ev)

        WIT.observers_for = asked
        try:
            return orig(self, token, events)
        finally:
            WIT.observers_for = real_obs

    SeasonDriver.witness = wrapped
    try:
        POP.run(SEASONS, 0, w=w)
    finally:
        SeasonDriver.witness = orig
    return out


def test_m_skip_every_selected_event_has_no_observer_under_all_five(season_run):
    m = season_run
    assert m["mode"] == "all_five", "the shipped fan-out arm moved"
    assert m["selected"] >= MIN_SELECTED, (
        f"the predicate selected {m['selected']} of {m['barrier_events']} Events")
    assert m["observers"] == [], (
        f"{len(m['observers'])} selected Events have observers, e.g. {m['observers'][:3]}: "
        "the predicate is falsified, not to be coded around")
    assert m["selected"] < m["barrier_events"], "the predicate selected every Event"
    # the census `loop/witness.py`'s IN-55 comment states: `claim.decayed` is the whole of it today
    assert set(m["kinds"]) == {"claim.decayed"}, m["kinds"]


def test_the_skip_changes_the_work_and_nothing_else(monkeypatch):
    """A/B: `SEASONS` seasons of `build_realm(0)` with the skip, and the same with the predicate
    forced False (every Event fanned). The world hash and the log are identical -- the skip moves no
    deposit. `SEASONS`, not one: decay first fires in the second season, so a one-season A/B has a
    skip arm in which the predicate selects nothing and cannot fail. The skip arm therefore counts
    the predicate's True answers through a wrapper and asserts at least `MIN_SELECTED` of them.
    MUTATION (run): the skip arm's wrapper forcing False -> `selected == 0` -> red."""
    selected = [0]
    real = WIT.changes_only_held_claims

    def counted(*a, **k):
        got = real(*a, **k)
        selected[0] += bool(got)
        return got

    def one(skip: bool):
        monkeypatch.setattr(WIT, "changes_only_held_claims",
                            counted if skip else (lambda *a, **k: False))
        w = POP.build_realm(0)
        POP.run(SEASONS, 0, w=w)
        monkeypatch.undo()
        return w.content_hash(), [(e.kind, e.id) for e in w.log]
    (h_skip, log_skip), (h_fan, log_fan) = one(True), one(False)
    assert log_skip, "fixture: the season logged nothing"
    assert selected[0] >= MIN_SELECTED, (
        f"the skip arm selected {selected[0]} Events -- the A/B compares two identical arms")
    assert h_skip == h_fan and log_skip == log_fan


def test_the_wired_skip_is_taken_for_the_selected_events(season_run):
    """(b). `witness` asks `observers_for` about no selected Event, and about every other one."""
    m = season_run
    assert m["asked_selected"] == 0, "WITNESS asked `observers_for` about a selected Event"
    assert m["asked_other"] == m["barrier_events"] - m["selected"] >= 1, (
        "WITNESS did not ask about exactly the Events the predicate did not select")


# -- (c) the control: a MATTER death ----------------------------------------------------------------
HOLDER = "p_high"


def _world_with_neighbour():
    w = P.tiny_world()
    w.persons["p_near"] = Person("p_near", "a neighbour")
    w.rungs["p_near"] = Rung("p_near", "person")
    w.add_tenure(Tenure("t_near_in", "p_near", "S", "contain", 0))
    w.add_tenure(Tenure("t_near_home", "p_near", "S", world_q.RESIDE_KIND, 0))
    return w


def _die_at_matter(w):
    w.step = Step.MATTER
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person(HOLDER),
            record_kind="Person", fieldname="exists", driver="Event",
            emits="person.died", subject=HOLDER, causes=[ROOT])
    (ev,) = w._emitted_by_write
    return ev


def _rejected_predicate(w, e, held, mode):
    """The formulation the plan REJECTS: every change subject resolves in no World store. A MATTER
    death meets it, because `World.remove_person` pops the person before WITNESS."""
    stores = (w.persons, w.sites, w.records, w.dates, w.rungs, w.offices)
    return bool(e.changes) and causing_none(w, e) and all(
        c.subject and not any(c.subject in s for s in stores) for c in e.changes)


def causing_none(w, e):
    from ..state.attribution import causing_act
    return causing_act(w, e) is None


def _names_him(w, pid):
    return [c for c in w.persons[pid].ledger if c.subject in {HOLDER, "off_duke"}]


def test_a_matter_death_is_not_selected_and_the_rejected_predicate_would_skip_it(monkeypatch):
    w = _world_with_neighbour()
    ev = _die_at_matter(w)
    held = EP.held_claim_ids(w)
    assert HOLDER not in w.persons, "fixture: the death did not remove him"
    assert _rejected_predicate(w, ev, held, "all_five"), "fixture: the rejected formulation does not select the death"
    assert not EP.changes_only_held_claims(w, ev, held, "all_five"), "the real predicate selected a MATTER death"
    # the real predicate: H-206's witnesses are reached
    SeasonDriver(w).witness(mint_token(w, WriteClass.INTERIOR), [ev])
    assert sum(len(_names_him(w, p)) for p in ("p_near",)) >= 1, "no one at S holds a claim naming him"

    # the control: wire the rejected predicate in, and the same death reaches nobody
    w2 = _world_with_neighbour()
    ev2 = _die_at_matter(w2)
    monkeypatch.setattr(WIT, "changes_only_held_claims", _rejected_predicate)
    SeasonDriver(w2).witness(mint_token(w2, WriteClass.INTERIOR), [ev2])
    assert sum(len(_names_him(w2, p)) for p in ("p_near",)) == 0, (
        "the rejected predicate did not silence the death; the control observed nothing")


# -- (d) the predicate on hand-built Events -----------------------------------------------------------
def _ev(eid, subjects, causes=None, kind="claim.decayed"):
    return Event(id=eid, kind=kind, changes=[P.about(s) for s in subjects],
                 causes=causes or [ROOT], emitted_at=1)


def test_the_predicate_selects_a_held_claim_only_event_and_refuses_each_other_shape():
    w = P.tiny_world()
    w.persons["p_high"].ledger.append(_claim("c_held", "p_high"))
    w.persons["p_low"].ledger.append(_claim("c_held2", "p_low"))
    held = EP.held_claim_ids(w)
    assert held == {"c_held", "c_held2"}
    pred = lambda e: EP.changes_only_held_claims(w, e, held, "all_five")

    assert pred(_ev("e1", ["c_held"])), "a held claim and nothing else was not selected"
    assert pred(_ev("e2", ["c_held", "c_held2"])), "two held claims in two ledgers were not selected"
    assert not pred(_ev("e3", ["c_held", "p_low"])), "a claim beside a person subject was selected"
    assert not pred(_ev("e4", ["c_held", "S"])), "a claim beside a rung subject was selected"
    assert not pred(_ev("e5", ["c_nowhere"])), "a claim no ledger holds was selected"
    assert not pred(_ev("e6", ["c_held", "c_nowhere"])), "one unheld claim among held ones was selected"
    assert not pred(Event(id="e7", kind="condition.band_crossed", changes=[], causes=[ROOT],
                          emitted_at=1)), "an Event with no change was selected"
    assert not pred(Event(id="e8", kind="k", changes=[P.about("")], causes=[ROOT], emitted_at=1)), (
        "a change with no subject was selected")

    act = Act(id="a_in55", actor="p_high", verb="speak", payload={})
    w.acts.append(act)
    assert not pred(_ev("e9", ["c_held"], causes=[act.id])), "an Event with an act was selected"


def test_a_kind_the_chronicle_admits_is_not_selected(monkeypatch):
    """`chronicle` admits on `e.kind` alone: plant a `binding_decision` row emitting the held-claim-only
    kind, and the same Event is no longer selected (the fan runs). Control: selected before the plant."""
    from types import SimpleNamespace
    w = P.tiny_world()
    w.persons["p_high"].ledger.append(_claim("c_held", "p_high"))
    held, e = EP.held_claim_ids(w), _ev("e_chron", ["c_held"])
    assert EP.changes_only_held_claims(w, e, held, "all_five"), "control: not selected before the plant"
    monkeypatch.setitem(EP.VERB_TABLE, "v_in55_planted",
                        SimpleNamespace(stratum="binding_decision", emits=(e.kind,)))
    assert EP._ch_chronicle(w, e, None), "fixture: the planted row does not reach the chronicle"
    assert not EP.changes_only_held_claims(w, e, held, "all_five"), "a chronicled kind was selected"


def test_a_claim_removed_from_its_ledger_is_no_longer_held_so_its_event_is_not_selected():
    """The edge: the Event's claim has left the ledger (evicted, or its holder removed) by the time the
    fan is built, so it is not `held` and the fan runs -- the safe direction."""
    w = P.tiny_world()
    c = _claim("c_gone", "p_high")
    w.persons["p_high"].ledger.append(c)
    e = _ev("e_gone", ["c_gone"])
    assert EP.changes_only_held_claims(w, e, EP.held_claim_ids(w), "all_five")
    w.persons["p_high"].ledger.remove(c)
    assert not EP.changes_only_held_claims(w, e, EP.held_claim_ids(w), "all_five")
    w.persons["p_low"].ledger.append(_claim("c_held", "p_low"))
    w.step = Step.MATTER
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_low"),
            record_kind="Person", fieldname="exists", driver="Event",
            emits="person.died", subject="p_low", causes=[ROOT])
    assert "p_low" not in w.persons, "fixture: the holder was not removed"
    assert "c_held" not in EP.held_claim_ids(w), "a removed holder's claims are still reported held"


def test_the_control_arm_total_is_never_skipped_and_the_two_channel_arms_answer_nobody():
    """`total` asks no predicate and credits everyone, so a skip there would turn the control into a
    narrow arm; the predicate takes the mode and refuses it. The other two arms are exactly `[]`."""
    w = P.tiny_world()
    w.persons["p_high"].ledger.append(_claim("c_held", "p_high"))
    held, everyone, e = EP.held_claim_ids(w), list(w.persons), _ev("e_mode", ["c_held"])
    assert len(everyone) >= 2
    assert len(EP.observers_for(w, e, "total", everyone)) == len(everyone), (
        "fixture: `total` no longer fans a claim-changing Event to everyone")
    assert not EP.changes_only_held_claims(w, e, held, "total"), "the control arm's fan was skipped"
    for mode in ("presence_only", "all_five"):
        assert EP.changes_only_held_claims(w, e, held, mode), f"{mode}: a held-claim Event not selected"
        assert EP.observers_for(w, e, mode, everyone) == [], f"{mode}: a selected Event has observers"
