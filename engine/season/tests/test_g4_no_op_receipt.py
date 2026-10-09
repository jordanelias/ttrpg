"""G4 -- `NoOpReceipt` and the final effect contract. Plan position 7.

`04 §C.2`: *"before = get(); store._set(); after = get() -- THE GATE APPLIES THE WRITE / before ==
after or raise NoOpReceipt -- F9"*, and `04:559-564`: *"A receipt with `before == after` IS minted
by the gate -- so `work` emitting `site.worked` while accumulating no delta, which is the instance
`ID-9` is written from, passes the check unchanged. The append-side test could not observe the
failure it excludes; the write side can."*

What each block proves, and the control that stops it passing vacuously:

  1. THE PLAN'S FALSIFIER, SHARPENED. An effect that names a subject and moves nothing is refused:
     at least one refusal Event for the act, and ZERO `set` receipts on that subject in anything
     the fold emits. Control, in the same test: with the gate's comparison switched off (every
     read unequal -- the pre-G4 contract), the same planted effect SUCCEEDS with a receipt on the
     subject, so the assertion can observe the failure it excludes.
  2. AN EFFECT STILL ON THE RETIRED CONTRACT (mutate, return ids) is refused by TYPE, not admitted
     as a closure.
  3. F3 BEFORE F9. An effect that names an unmoved subject AND writes somebody else's edge with no
     basis is `NotYours`, and the edge is put back -- never excused as a no-op that left it
     standing. The control: the same effect minus the unlawful write is `NoOpReceipt`.
  4. A NO-OP PUTS BACK THE TENURES ITS CLOSURE TOUCHED, even lawful ones, so a refusal Event never
     stands beside an edge the refused write opened.
  5. PER-EFFECT DECISIONS, EACH WITH ITS CONTROL: `fight` (renamed from `kill / wound`, plan
     `FIGHT-RENAME`) judges body and existence, and a refused wound scars nobody (IN-08 H3); a second identical `convene` in
     one season is refused and a reschedule is not; a
     `transfer` from a rung to itself is refused and a real one is made.

`work`'s own falsifier -- per act AND per site, both judgments -- is
`test_season_shape.py::test_w8_work_emits_a_success_only_when_the_site_moves`.
"""
import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.gaps import InstrumentDefect
from engine.season.harness import probes as P
from engine.season.loop import effects as _effects
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.state.carriers import Act, Receipt, Tenure
from engine.season.state.gate import Change, NoOpReceipt, NotYours, Subject
from engine.season.state.world import World

from ._scar_helpers import wounded as _wounded


def _driver(w):
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    return d


def _set_receipts_on(evs, sid):
    return [c for e in evs for c in e.changes
            if isinstance(c, Receipt) and c.subject == sid and c.mode == "set"]


def _plant(monkeypatch, verb, effect):
    monkeypatch.setitem(_effects.EFFECTS, verb, effect)


# ======================================================================================
# 1 -- THE PLAN'S FALSIFIER, SHARPENED, WITH ITS CONTROL
# ======================================================================================

def test_g4_an_effect_that_names_a_subject_and_moves_nothing_is_refused(monkeypatch):
    """`utter` is the host because its row has NO precondition, so nothing but the gate stands
    between the planted effect and a success; its refusal is the fold's own `act.refused`. The
    planted effect names the rung `Hh` -- a real, present entity -- and writes nothing."""
    _plant(monkeypatch, "utter",
           lambda w, a, res=None: Change((Subject.entity("rungs", "Hh"),), lambda: None))
    w = P.tiny_world()
    evs = _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                             [Act(id="g4_plant", actor="p_low", verb="utter")])
    mine = [e for e in evs if e.causes and e.causes[0] == "g4_plant"]
    refused = [e for e in mine if e.kind == "act.refused"]
    assert len(refused) >= 1, [e.kind for e in mine]
    assert not [e for e in mine if e.kind == "proposition.uttered"], [e.kind for e in mine]
    assert _set_receipts_on(evs, "Hh") == [], (
        "a `set` receipt names `Hh` though nothing wrote it -- the gate minted for a no-op")

    # THE CONTROL: the gate compares nothing (every read unequal), which is the contract before
    # G4 -- the fold minted for whatever the effect named. The same plant must now SUCCEED with a
    # receipt on `Hh`; if it did not, the assertions above could not tell G4 from a broken effect.
    monkeypatch.setattr(World, "state_of", lambda self, s: object())
    w = P.tiny_world()
    evs = _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                             [Act(id="g4_plant", actor="p_low", verb="utter")])
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert len(_set_receipts_on(evs, "Hh")) == 1


def test_g4_an_effect_still_on_the_retired_contract_is_refused_by_type(monkeypatch):
    """The pre-G4 shape -- mutate (here: nothing) and return the ids -- must not slip back in as a
    closure the gate does not judge. `World.write` refuses a change that is not a `Change`."""
    _plant(monkeypatch, "utter", lambda w, a, res=None: ["Hh"])
    w = P.tiny_world()
    with pytest.raises(InstrumentDefect) as e:
        _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id="g4_old", actor="p_low", verb="utter")])
    assert "Change" in str(e.value), str(e.value)


# ======================================================================================
# 2 -- F3 IS ASKED BEFORE F9, AND A NO-OP PUTS BACK WHAT IT TOUCHED
# ======================================================================================

def test_g4_an_unlawful_edge_write_is_not_yours_even_when_nothing_named_moved(monkeypatch):
    """The effect names `Hh` (unmoved) and, unnamed, closes `p_high`'s seat on `off_duke` -- an
    edge `p_low` has no basis to write (no seat in `via`). If F9 were asked first the write would
    be refused as a NO-OP and, F9 not being an authority check, the order of the two raises would
    decide whether the closure is put back. It must be `NotYours`, and the seat must be live."""
    def plant(w, a, res=None):
        seat = next(t for t in w.tenures if t.id == "t9")
        return Change((Subject.entity("rungs", "Hh"),), lambda: setattr(seat, "until", w.tick))
    _plant(monkeypatch, "utter", plant)
    w = P.tiny_world()
    with pytest.raises(NotYours):
        _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id="g4_ny", actor="p_low", verb="utter")])
    assert [t.live for t in w.tenures if t.id == "t9"] == [True], "the unlawful closure stood"

    # CONTROL: the same effect without the unlawful write is a plain no-op -- raised raw at the
    # gate as `NoOpReceipt`, and folded into the refusal -- so the `NotYours` above came from the
    # edge, not from the unmoved subject.
    _plant(monkeypatch, "utter",
           lambda w, a, res=None: Change((Subject.entity("rungs", "Hh"),), lambda: None))
    w = P.tiny_world()
    d = _driver(w)
    with pytest.raises(NoOpReceipt):
        w.write("exists", mint_token(w, WriteClass.ACTS), None, record_kind="Proposition",
                fieldname="exists", driver="Act", actor="p_low",
                change=_effects.EFFECTS["utter"](w, Act(id="g4_raw", actor="p_low", verb="utter")))
    evs = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="g4_ny2", actor="p_low", verb="utter")])
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]


def test_g4_a_no_op_puts_back_a_lawful_edge_its_closure_opened(monkeypatch):
    """`p_low` opening a `hold` of his own on the rung `Hh` is `T-m` -- lawful. The effect names
    `S`, which it does not move. The write is a no-op on everything it named, so it is refused, and
    the edge it opened beside the refusal is removed with it: a refusal Event must not stand beside
    a Tenure the refused write created."""
    def plant(w, a, res=None):
        t = Tenure("g4_side_hold", "p_low", "Hh", "hold", w.tick)
        return Change((Subject.entity("rungs", "S"),), lambda: w.add_tenure(t))
    _plant(monkeypatch, "utter", plant)
    w = P.tiny_world()
    evs = _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                             [Act(id="g4_side", actor="p_low", verb="utter")])
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]
    assert not [t for t in w.tenures if t.id == "g4_side_hold"], "the refused write's edge stood"

    # CONTROL: name the edge itself, and the same write is a success that keeps it.
    def named(w, a, res=None):
        t = Tenure("g4_side_hold", "p_low", "Hh", "hold", w.tick)
        return Change((Subject.edge(t),), lambda: w.add_tenure(t))
    _plant(monkeypatch, "utter", named)
    w = P.tiny_world()
    evs = _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                             [Act(id="g4_side", actor="p_low", verb="utter")])
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert [t.live for t in w.tenures if t.id == "g4_side_hold"] == [True]


# ======================================================================================
# 3 -- PER-EFFECT DECISIONS
# ======================================================================================

def _kill(w, aid, res):
    d = _driver(w)
    return [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                    Act(id=aid, actor="p_low", verb="fight",
                                        payload={"subject": "p_mid"}), res)]


def test_g4_kill_is_judged_on_body_and_existence_and_a_refused_wound_scars_nobody():
    """`_eff_kill`'s subject is the victim read as presence and `body` -- not the whole Person.

      * A `Wounded` scene that took NO health leaves `body` where it was: refused, not
        `body.changed` (the old contract published the success over an unchanged body).
      * RE-RECORDED AT IN-08 H3. This arm swept `scar_step = 10` and asserted the scar WAS written
        on the refused wound -- a rider inside `_eff_kill`. H3 retires `_scar` and `scar_step`: the
        fold scars the act's OBSERVERS only after an outcome that MOVED state, so a refused wound
        now scars nobody. Asserted over every person, so a scar landing on anyone fails it.
      * CONTROL: a scene that took half the health moves `body` and is `body.changed` -- and DOES
        scar an observer, so the no-scar arm above can fail (`tiny_world`'s persons hold no
        pursuits, so every person is given all fifteen; without that both arms read empty)."""
    from ..data.rosters import PURSUITS

    def _with_pursuits():
        w = P.tiny_world()
        for p in w.persons.values():
            p.pursuits = {e: 0.5 for e in PURSUITS}
        return w

    w = _with_pursuits()
    body = w.persons["p_mid"].body
    assert _kill(w, "g4_k0", _wounded("p_mid", 10, 10)) == ["kill.refused"]
    assert w.persons["p_mid"].body == body
    scarred = {pid: p.scar for pid, p in w.persons.items() if p.scar}
    assert not scarred, f"a refused wound scarred {scarred}"

    w = _with_pursuits()
    assert _kill(w, "g4_k2", _wounded("p_mid", 10, 5)) == ["body.changed"]
    assert w.persons["p_mid"].body == body // 2
    assert any(p.scar for p in w.persons.values()), (
        "a wound that moved `body` scarred nobody, so the refused arm's empty scar proves nothing")


def test_g4_a_second_identical_convening_is_refused_and_a_reschedule_is_not():
    """`convene`'s Date id is `H(seed, tick, actor, venue)`, so a second identical act in one
    season finds the date already due when it says: nothing moves, `convene.refused` -- where it
    used to publish a second `date.scheduled`. A different `when` moves `due_at`: a success."""
    w = P.tiny_world()
    d = _driver(w)
    fold = lambda aid, when: [e.kind for e in d._fold(
        w, mint_token(w, WriteClass.ACTS),
        Act(id=aid, actor="p_high", via="off_duke", verb="convene",
            payload={"subject": "S", "when": when}))]
    assert fold("g4_c0", 3) == ["date.scheduled"]
    assert fold("g4_c1", 3) == ["convene.refused"]
    assert fold("g4_c2", 4) == ["date.scheduled"]
    assert [x["due_at"] for x in w.dates.values()] == [4]


def test_g4_a_transfer_from_a_rung_to_itself_is_refused_and_a_real_one_is_made():
    """The corpus's own case (628 of its 900 `transfer` effect calls, `r_hearth -> r_hearth`): the
    decrement and the increment land on one store and cancel. Refused, the store unmoved, no
    receipt. CONTROL: `Hh -> S` moves one grain each way and is `transfer.made`."""
    w = P.tiny_world()
    d = _driver(w)
    pay = lambda to: {"from": "Hh", "to": to, "kind": "grain", "amount": 1, "subject": to}
    evs = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="g4_t0", actor="p_low", verb="transfer", payload=pay("Hh")))
    assert [e.kind for e in evs] == ["transfer.refused"], [e.kind for e in evs]
    assert w.rungs["Hh"].stores == {"grain": 8} and _set_receipts_on(evs, "Hh") == []
    evs = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="g4_t1", actor="p_low", verb="transfer", payload=pay("S")))
    assert [e.kind for e in evs] == ["transfer.made"], [e.kind for e in evs]
    assert (w.rungs["Hh"].stores, w.rungs["S"].stores) == ({"grain": 7}, {"grain": 41})
    assert len(_set_receipts_on(evs, "Hh")) == 1 and len(_set_receipts_on(evs, "S")) == 1
