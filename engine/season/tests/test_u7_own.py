"""Plan position `14` (U7-own) -- the unbuilt verb rows, and the binding they wait on.

What each block proves, and the control that stops it passing vacuously:

  1. THE FOLD'S COUNTERPARTY CLAUSE (`loop/resolve.py::_admits`, `COUNTERPARTY_CLAUSE`). For EVERY row
     naming a `counterparty:`, an act naming the ACTOR there -- or naming nobody -- is refused with the
     row's own `counterparty` refusal, with the precondition and eligibility stubbed open so the clause
     alone decides. Control: the same act naming another person is admitted. The loop asserts it
     checked every such row (`checked == len(rows) >= 1`).
  2. THE SELF-LOOP, END TO END: a `give` to oneself through the real fold opens nothing and leaves
     the giver's custody as it was -- a `handover` to oneself is the `Tenure(X, X)` fiat `ED-IN-0210`
     ruling 1 names. Control: the same Record to another person standing there is given.
  3. THE BARE-STRING OBLIGE (`ED-IN-0211`, the F7/F8 recurrence that reverted `_eff_oblige` once): an
     `oblige` whose object names no entity is `duty.refused` and opens no edge. Control: the same act
     on a real seat opens one.
  4. THE ALWAYS-REFUSED SET DOES NOT GROW BY THIS POSITION. Every row `14` declined stays out of
     `resolvable_verbs()` -- so it can never be formed, attempted and refused -- and the one untyped
     row that names a second party it cannot carry (`oblige`) forms no Candidate person-side. The
     corpus's always-refused set itself is pinned in `test_season_shape.py` and did not move.
  5. `destroy_record` STAYS UNFORMABLE (`A-13` taken and HELD on measurement -- the row's
     `decline_note`): the holder of a Record forms no `destroy_record` on it, both eligibility
     alternatives being placeholders (`H-75`). Goes red the day the held decision lands, which is the
     day to re-measure `release`'s corpus worlds against the live always-refused pin (the told-channel
     reason the note once gave is withdrawn at HEAD, and the variant it measured is not kept).
  6. `give` IS FORMABLE: one Candidate per known receiver (`test_give.py` owns the fan's detail).
  7. CANDIDATE-WHY: `Candidate` carries no `why` -- it was written once and read nowhere.
"""
import dataclasses

import pytest

from engine.season.data.verbs import COUNTERPARTY_CLAUSE, VERB_TABLE
from engine.season.decision.options import opening_set
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.queries.world_q import hold_force
from engine.season.state.carriers import Act, Candidate, Claim, Question, View

# The rows this position DECLINED or STOPPED on, each recorded with its reason in the position's
# receipt; none may become resolvable without the reason being answered first.
# roster-exempt: TEST EXPECTATION, the declined set this position's falsifier asserts.
DECLINED = ("carry", "exchange", "forge", "repudiate", "succeed", "thread_read", "tie / knot")


def _view(w, pid):
    return View(pid, [], w.fixtures.get("view_k"))


def _formed(w, pid, verb, referents):
    q = Question("q:u7own", "need", tuple(referents))
    return [c for c in opening_set(w.persons[pid], _view(w, pid), q, w.fixtures) if c.verb == verb]


# ======================================================================================
# 1 -- THE FOLD'S COUNTERPARTY CLAUSE, OVER EVERY ROW THAT NAMES ONE
# ======================================================================================

def test_14_every_counterparty_row_is_refused_at_the_fold_when_the_act_names_no_second_party():
    w = P.tiny_world()
    d = SeasonDriver(w)
    rows = [r for r in VERB_TABLE.values() if r.counterparty]
    assert rows, "no row names a counterparty -- the clause below would be checked against nothing"
    checked = 0
    for row in rows:
        # the clause ALONE: eligibility `own` and no precondition, so nothing earlier can refuse
        open_row = dataclasses.replace(row, eligibility=("own",), requires="—", requires_typed=None)
        want = row.refusal_for(COUNTERPARTY_CLAUSE)
        assert want, f"{row.verb!r} names a counterparty and declares no refusal for it"
        other = {"subject": "Hh"} if row.counterparty != "subject" else {}
        for key, named in (("self", "p_low"), ("none", None)):
            payload = {**other, **({row.counterparty: named} if named is not None else {})}
            ok, kinds, _ = d._admits(w, Act(id=f"cp_{key}", actor="p_low", verb=row.verb,
                                             payload=payload), open_row)
            assert ok is False and tuple(kinds) == tuple(want), (row.verb, key, ok, kinds)
        # CONTROL: a second party who is somebody else is admitted by the same clause
        ok, kinds, _ = d._admits(w, Act(id="cp_other", actor="p_low", verb=row.verb,
                                         payload={**other, row.counterparty: "p_mid"}), open_row)
        assert ok is True and not kinds, (row.verb, kinds)
        checked += 1
    assert checked == len(rows) >= 1


# ======================================================================================
# 2 -- THE SELF-LOOP, END TO END
# ======================================================================================

def _petition_held_by(w, pid):
    """`pid` files a petition through the real fold and holds it. Returns its id."""
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "petition", payload={
        "subject": "p_mid", "to": "p_mid", "from": "Hh"})] if p.id == pid else []))
    (rid,) = [r for r, rec in w.records.items() if rec.kind == "petition"]
    assert hold_force(w, rid).subject == pid, "fixture: the petitioner does not hold his petition"
    return rid


def test_14_a_give_to_oneself_opens_nothing_and_a_give_to_another_moves_the_hold():
    w = P.tiny_world()
    rid = _petition_held_by(w, "p_low")
    before = [(t.id, t.subject, t.until) for t in w.tenures if t.object == rid]
    d = P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "give", payload={"subject": rid, "to": "p_low"})]
                                        if p.id == "p_low" else []))
    kinds = [e.kind for e in w.log if (e.causes or [None])[0] in {a.id for a in d.resolved}]
    assert "give.refused" in kinds and "record.given" not in kinds, kinds
    assert [(t.id, t.subject, t.until) for t in w.tenures if t.object == rid] == before, (
        "a give to oneself touched the custody it should have refused")
    # CONTROL: the same Record to a person standing in the giver's hearth is given
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "give", key="2",
                                            payload={"subject": rid, "to": "p_mid"})]
                                    if p.id == "p_low" else []))
    assert hold_force(w, rid).subject == "p_mid", "the control give did not move the hold"


# ======================================================================================
# 3 -- THE BARE-STRING OBLIGE
# ======================================================================================

@pytest.mark.parametrize("seat, ok", [("einhir_texts", False), ("off_dicastery", True)])
def test_14_an_oblige_to_a_bare_string_opens_no_edge_and_one_to_a_seat_does(seat, ok):
    w = P.tiny_world()
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "oblige", payload={"subject": seat})]
                                    if p.id == "p_low" else []))
    edges = [t for t in w.tenures if t.kind == "oblige" and t.subject == "p_low" and t.live]
    kinds = {e.kind for e in w.log}
    if ok:          # CONTROL: a real seat the actor does not hold
        assert [t.object for t in edges] == [seat] and "duty.taken" in kinds, (edges, kinds)
    else:
        assert not edges and "duty.refused" in kinds and "duty.taken" not in kinds, (edges, kinds)


# ======================================================================================
# 4 -- THE ALWAYS-REFUSED SET DOES NOT GROW BY THIS POSITION
# ======================================================================================

def test_14_no_declined_row_is_resolvable_and_no_unbindable_counterparty_row_forms():
    rv = resolvable_verbs()
    leaked = sorted(v for v in DECLINED if v in rv)
    assert not leaked, (f"{leaked} became resolvable, so it can be formed, attempted and refused in "
                        "every world -- the always-refused set grows by a row this position declined")
    assert len(DECLINED) >= 1 and all(v in VERB_TABLE for v in DECLINED), DECLINED
    # the untyped rows naming a second party their cell cannot carry: formed by nobody
    unbindable = sorted(v for v, r in VERB_TABLE.items() if r.counterparty and r.requires_typed is None)
    assert unbindable == ["oblige"], unbindable
    w = P.tiny_world()
    referents = ("off_duke", "off_dicastery", "p_mid", "Hh")
    for v in unbindable:
        assert not _formed(w, "p_low", v, referents), f"{v!r} formed with no carriable second party"


# ======================================================================================
# 5 -- `destroy_record` STAYS UNFORMABLE (A-13 HELD)
# ======================================================================================

def test_14_destroy_record_is_formed_by_nobody_while_a_13_is_held():
    w = P.tiny_world()
    rid = _petition_held_by(w, "p_low")
    assert hold_force(w, rid).subject == "p_low", "fixture: the holder must exist for this to mean anything"
    assert not _formed(w, "p_low", "destroy_record", (rid, "Hh", "p_mid")), (
        "`destroy_record` formed -- `A-13` landed; re-measure `release`'s corpus worlds against the "
        "live always-refused pin before re-pinning (the row's `decline_note`)")
    # CONTROL: the same holder forms OTHER verbs on the same referents, so the empty set above is the
    # row's eligibility and not an empty opening set
    assert _formed(w, "p_low", "give", (rid,)) or _formed(w, "p_low", "research", (rid,)), (
        "the holder forms nothing at all on his own document -- the assertion above is vacuous")


# ======================================================================================
# 6 -- `give` IS FORMABLE IN COMPUTED PLAY
# ======================================================================================

def test_14_give_forms_once_per_known_receiver_and_never_to_the_giver():
    w = P.tiny_world()
    rid = _petition_held_by(w, "p_low")
    w.persons["p_low"].ledger.append(
        Claim("c_u7_k", "p_low", "p_other", "exists:Person", 1, 0, "firsthand", 100, "own"))
    got = _formed(w, "p_low", "give", (rid,))
    tos = sorted(c.operands.get("to") for c in got)
    assert tos and "p_low" not in tos and "p_other" in tos, tos


# ======================================================================================
# 7 -- CANDIDATE-WHY
# ======================================================================================

def test_14_a_candidate_carries_no_why():
    assert "why" not in {f.name for f in dataclasses.fields(Candidate)}
    w = P.tiny_world()
    got = opening_set(w.persons["p_low"], _view(w, "p_low"),
                      Question("q:u7own", "need", ("Hh",)), w.fixtures)
    assert got and all(not hasattr(c, "why") for c in got), "the opening set formed nothing to check"
