"""CR-76 (workplan v11, batch B11-S3): THE WORLD READING -- `queries/world_q.py`'s `flows_in`, `concluded`,
`within`, `presented`, `commensurate`, and `harness/strife.py`'s opening-to-terminal route check.

Every falsifier runs on a HAND-BUILT world (P9): the shipped realm, before B10-11, holds no live `detain` beyond
`arrest`, no `at_war` pair and no docketed matter a strand names, so those arms are exercised only here.

  1. Two realm-wide events while an era is open read as ONE era (two strands, one era holding both).
  2. A terminal move at the realm rung with no open referent concludes the era and frees the realm slot; the
     terminal missing leaves it open; a live `detain`, a docketed matter or (through a stand-in for the owner) an
     `at_war` pair among its parties leaves it open; a strand never concludes on its own opening move.
  3. A person within the realm flow whose ledger holds none of its moves is listed as within; a person under a
     root outside the realm is not.
  4. Two petitions sharing a matter open a strand holding both; two on different matters open none.
  5. `commensurate`: +1 (a `false` pair; a shared affiliation), -1 (a `true` pair), 0 (only `null`; none held).
  6. The route check names a planted gap: a verb removed from the resolvable set loses its pairs.
Each loop asserts that it asserted (`CLAUDE.md` §0.1 pt 2).
"""
import pytest

from engine.season.data import affiliations as A
from engine.season.data.rosters import DETAIN_KIND
from engine.season.harness import probes as P
from engine.season.harness import strife as H
from engine.season.queries import faction_q, world_q as W
from engine.season.state.carriers import Act, Event, Person, Record, Rung, StateChange, Tenure
from engine.season.state.ids import ROOT


def _world():
    """`tiny_world` (R realm > D duchy > S settlement > Hh hearth) plus three more duchies, each with a settlement,
    so a move naming two settlements in two duchies is realm-wide; and a root `F` outside the realm with `p_far`."""
    w = P.tiny_world()
    n = [0]

    def edge(sub, obj, kind):
        n[0] += 1
        w.add_tenure(Tenure(f"t_cr76_{n[0]}", sub, obj, kind, 0))
    for d, s in (("D2", "S2"), ("D3", "S3"), ("D4", "S4")):
        w.rungs[d] = Rung(d, "duchy")
        w.rungs[s] = Rung(s, "settlement")
        edge(d, "R", "contain")
        edge(s, d, "contain")
    w.rungs["F"] = Rung("F", "territory")
    w.persons["p_far"] = Person("p_far", "a foreigner")
    w.rungs["p_far"] = Rung("p_far", "person")
    edge("p_far", "F", "contain")
    return w


def ev(w, eid, kind, subjects, actor=None, verb="tell", payload=None, tick=1):
    causes = [ROOT]
    if actor is not None:
        aid = f"a_{eid}"
        w.acts.append(Act(id=aid, actor=actor, verb=verb, payload=payload or {}))
        causes = [aid]
    e = Event(eid, kind, [StateChange(s, "set", "Event", "exists") for s in subjects], causes, tick)
    w.log.append(e)
    return e


def test_the_side_read_has_one_owner():
    assert H.governors is W.governors and H.side_against is W.side_against


def test_two_realm_wide_events_while_an_era_is_open_read_as_one_era():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    ev(w, "e2", "field.lost", ["S3", "S4"], tick=2)
    fl = W.flows_in(w)
    assert len(fl.strands) == 2, fl.strands                         # they share no referent and no step
    assert all(s.rung == "R" for s in fl.strands)
    assert len(fl.eras) == 1 and not fl.eras[0].concluded
    assert set(fl.eras[0].strands) == {s.id for s in fl.strands} == {"e1", "e2"}
    assert W.open_era(fl) is fl.eras[0]


def test_a_terminal_move_with_no_open_referent_concludes_the_era_and_frees_the_slot():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    open_only = W.flows_in(w)
    assert W.open_era(open_only) is not None                        # the terminal missing: open
    ev(w, "e2", "rung.ceded", ["S", "S2"], tick=2)                  # `concludes` kind, realm-wide, links by S
    fl = W.flows_in(w)
    assert [e.concluded for e in fl.eras] == [True] and W.open_era(fl) is None
    (s,) = fl.strands
    assert W.concluded(w, s)
    ev(w, "e3", "field.lost", ["S3", "S4"], tick=3)                 # a realm-wide event after: a new era
    fl = W.flows_in(w)
    assert [e.concluded for e in fl.eras] == [True, False]


def test_a_strand_never_concludes_on_its_own_opening_move():
    w = _world()
    ev(w, "e1", "rung.seized", ["S"])
    fl = W.flows_in(w, terminal=lambda e, a: True)
    (s,) = fl.strands
    assert len(s.moves) == 1 and s.moves[0].terminal and not W.concluded(w, s)


@pytest.mark.parametrize("arm", ["detain", "docket", "at_war"])
def test_an_open_referent_keeps_the_era_open(arm, monkeypatch):
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2", "p_low", "p_mid"])
    ev(w, "e2", "rung.ceded", ["S", "S2", "p_low", "p_mid"], tick=2)
    assert W.open_era(W.flows_in(w)) is None                        # control: with nothing open it concludes
    if arm == "detain":
        w.add_tenure(Tenure("t_cr76_held", "p_low", "off_duke", DETAIN_KIND, 0))
    elif arm == "docket":
        w.docket.append({"date": None, "matter": "S2", W.DOCKET_ARRANGEMENT: None, W.DOCKET_PETITION: None})
    else:
        # `at_war` is False for every pair the tree can build, and its own falsifier drives the real fold
        # (`test_faction_q.py`); here the arm's WIRING is read through stand-ins for the two owners.
        monkeypatch.setattr(W, "faction_of", lambda w_, x: {"p_low": "fac_a", "p_mid": "fac_b"}.get(x))
        monkeypatch.setattr(faction_q, "at_war", lambda w_, a, b: {a, b} == {"fac_a", "fac_b"})
    fl = W.flows_in(w)
    assert W.open_era(fl) is not None, arm
    assert W.open_referents(w, fl.strands[0].parties, fl.strands[0].referents), arm


def test_a_person_within_the_realm_flow_need_not_hold_any_of_its_moves():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    era = W.open_era(W.flows_in(w))
    persons, offices, _ = W.within(w, era.rung)
    moves = {m.event for m in era.moves}
    assert "p_other" in persons and not any(c.subject in moves or c.subject in {"S", "S2"}
                                            for c in w.persons["p_other"].ledger)
    assert "p_far" not in persons                                   # control: outside the realm, never within
    assert "off_duke" in offices


def _petition(w, rid, actor, terms, tick):
    w.records[rid] = Record(rid, "S", "petition", subject_matter={"terms": terms, "to": "p_high", "from": "S"})
    ev(w, f"e_{rid}", "petition.filed", [rid], actor=actor, verb="petition", payload={"subject": terms}, tick=tick)


def test_two_petitions_on_one_matter_open_a_strand_and_on_two_matters_none():
    same = _world()
    _petition(same, "rec_1", "p_low", "S", 1)
    assert W.flows_in(same).strands == ()                           # a lone petition is civic life
    _petition(same, "rec_2", "p_mid", "S", 2)
    (s,) = W.flows_in(same).strands
    assert [m.event for m in s.moves] == ["e_rec_1", "e_rec_2"] and s.moves[1].opens
    other = _world()
    _petition(other, "rec_1", "p_low", "S", 1)
    _petition(other, "rec_2", "p_mid", "S2", 2)
    assert W.flows_in(other).strands == ()


@pytest.mark.parametrize("a, b, want", [
    ({"inner_tradition": 3}, {"thread_truth": 3}, 1),              # a `false` pair
    ({"altonian_civics": 2}, {"altonian_civics": 4}, 1),           # a shared affiliation (its pairs all null)
    ({"solmund_orthodoxy": 3}, {"thread_truth": 1}, -1),           # a `true` pair
    ({"inner_tradition": 3}, {"einhir_restoration": 3}, 0),        # only `null` pairs
    ({}, {"thread_truth": 3}, 0),                                  # one holds none
    ({"thread_truth": 0}, {"solmund_orthodoxy": 5}, 0),            # 0 is not held
])
def test_commensurate(a, b, want):
    w = _world()
    w.persons["p_low"].conviction, w.persons["p_mid"].conviction = a, b
    assert W.commensurate(w, "p_low", "p_mid") == want == W.commensurate(w, "p_mid", "p_low")


def test_incompatibility_keeps_every_cell_and_incompatible_is_its_true_half():
    vals = set(A.INCOMPATIBILITY.values())
    assert vals == {True, False, None}
    assert A.INCOMPATIBLE == frozenset(p for p, v in A.INCOMPATIBILITY.items() if v is True)
    assert A._load_incompatible() == A.INCOMPATIBLE


def test_the_route_check_names_a_planted_gap():
    from engine.season.loop.driver import resolvable_verbs
    ok = resolvable_verbs()
    base = set(H.routeless_pairs(H.MOVES, ok))
    checked = 0
    for r in H.MOVES:
        if r["code"] not in H.terminal_codes(H.MOVES):
            continue
        verbs = {v for v, _ in H.route(r, ok)}
        if not verbs:
            continue
        lost = set(H.routeless_pairs(H.MOVES, ok - verbs)) - base
        named = {(k, r["code"]) for k in H.opening_kinds() if H.opening_producers(k, ok - verbs)}
        assert named and named <= lost, r["code"]                   # every opening that still exists loses it
        checked += 1
    assert checked >= 10
    lost = set(H.routeless_pairs(H.MOVES, ok - {"requisition"})) - base
    assert {k for k, _ in lost} == {"requisition.taken"}             # the opening side, removed
