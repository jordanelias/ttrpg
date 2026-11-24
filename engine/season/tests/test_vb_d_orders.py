"""B21.54 (`14_VERBS_BINDING_D` commit D1; A-21, A-22): WHAT A WRIT ORDERS IS A PROPOSITION.

`issue` declares `referent_class: Proposition`, and `queries/world_q.py::questions_for` stamps the Propositions a person
is committed to as an OUGHT (`ambitions`, the one owner) beside the ones he has heard of, so `issue`'s `subject` -- the
writ's `terms` -- binds a Proposition and never a person. The writ's `terms` was a person before this (a warrant read off
it would have the holder arrest himself); the declared widening is that `argue` forms on the same ids, and `commit` does not
(`rosters.yaml: held_edge_declines`).

Each function reads the formed set of `build_realm(1)`'s whole cast through the real `questions_for` and `opening_set`
(seconds, no season run); the seeded two-season readings are commit-body readings (`aperture 2 0` and `2 1`), never here.
The ambition Propositions are given a claim in their holder's ledger (`issue`'s `terms` conjunct forms only on a
Proposition its issuer holds a claim of), the deposit a heard utterance leaves.
"""
import pytest

from engine.season.boot.realm import build_realm
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.queries import world_q
from engine.season.state.carriers import Claim


@pytest.fixture
def realm():
    return build_realm(1)


def _formed(w, verbs, hold_claims):
    """`(verb, class of subject, subject is one of his ambitions)` for each formed Candidate of `verbs`, over every person of
    `w`; `hold_claims` gives each person a heard claim of each of his ambitions first."""
    out = []
    for pid, p in w.persons.items():
        ambs = world_q.ambitions(w, p)
        if hold_claims:
            # B21.55: `issue` fans over the persons he reads as commanded (`commanded_read`), so he reads every other person as sworn
            # here -- D1 observes the writ's `terms`, not whom the seat may address.
            for j, other in enumerate(w.persons):
                p.ledger.append(Claim(f"c_d1_sworn_{pid}_{j}", pid, other, "duty.taken", True, w.tick, "firsthand", 100, "own"))
            for i, a in enumerate(ambs):
                p.ledger.append(Claim(f"c_d1_{pid}_{i}", pid, a, "proposition.uttered", True, w.tick, "firsthand",
                                      100, "own", doer="p_not_himself"))
        for q in world_q.questions_for(w, p):
            for c in opening_set(p, assemble(p, q, 12), q, w.fixtures):
                if c.verb in verbs:
                    out.append((c.verb, w.class_of(c.subject), c.subject in ambs))
    return out


def test_d1_no_writ_terms_name_a_person(realm):
    """G D1: every `issue` the cast can form has a Proposition as its `terms`; and the ones formed are on ambitions."""
    formed = [f for f in _formed(realm, {"issue"}, hold_claims=True)]
    assert len(formed) >= 1, "`issue` formed for nobody: the assertion below observed nothing"
    assert [f for f in formed if f[1] != "Proposition"] == []
    assert any(f[2] for f in formed), "no writ is formed on an ambition: the stamp reaches nothing"


def test_d1_argue_gains_the_ambitions_and_commit_does_not(realm):
    """The declared widening and its control: `argue` forms on a held ambition; `commit` is declined on it
    (`held_edge_declines`), so its formed count on them is unchanged (zero)."""
    formed = _formed(realm, {"argue", "commit"}, hold_claims=False)
    argues = [f for f in formed if f[0] == "argue" and f[2]]
    assert len(argues) >= 1, "`argue` formed on no ambition: the widening is not observed"
    assert [f for f in formed if f[0] == "commit" and f[2]] == []


# ---------------------------------------------------------------------------------------------------------------------
# D2 (B21.55; A-22): `issue` and `dispatch` form only on those the seat commands.
# ---------------------------------------------------------------------------------------------------------------------

def _orders(w, pid, held_claims=()):
    """`[(verb, addressee)]` for every `issue` (its `to`) and `dispatch` (its `subject`) person `pid` forms over his
    whole `questions_for`, after `held_claims` (`(subject, predicate)`) join his ledger as untold, firsthand claims. Each of
    his ambitions is also given as a heard claim, so `issue`'s `terms` conjunct is not what narrows the set (the D1 deposit)."""
    p = w.persons[pid]
    for i, a in enumerate(world_q.ambitions(w, p)):
        p.ledger.append(Claim(f"c_d2_amb_{pid}_{i}", pid, a, "proposition.uttered", True, w.tick, "firsthand", 100, "own",
                              doer="p_not_himself"))
    for i, (subject, predicate) in enumerate(held_claims):
        p.ledger.append(Claim(f"c_d2_{pid}_{i}", pid, subject, predicate, True, w.tick, "firsthand", 100, "own"))
    out = []
    for q in world_q.questions_for(w, p):
        for c in opening_set(p, assemble(p, q, 12), q, w.fixtures):
            if c.verb == "issue":
                out.append(("issue", c.operands["to"]))
            elif c.verb == "dispatch":
                out.append(("dispatch", c.subject))
    return out


def _commanded_by_a_seat(w, pid, person):
    return any(world_q.commands(w, pid, t.object, person) for t in w.seat_holds(pid))


def test_d2_no_writ_or_order_to_a_person_the_seat_does_not_command():
    """G D2: a writ or an order is formed only on a man the sender reads as commanded, and the ones read here are commanded.
    The King reads p_npc_050 as sworn (`duty.taken`; the realm seeds the oath to `off_king`) and is offered a writ to no one
    else he knows; the Katepano reads p_npc_011 and is offered the order. Control: with nothing read neither forms a thing (the
    realm's strangers, whom every unnarrowed writ addressed); and nobody orders himself."""
    w = build_realm(1)
    assert "p_npc_050" in world_q.establishment_of(w, "off_king")
    assert _orders(build_realm(1), "p_npc_020") == [], "a writ formed on a man the King reads nothing of"
    king = _orders(w, "p_npc_020", [("p_npc_050", "duty.taken")])
    assert [a for v, a in king if v == "issue"], "no writ formed to the man the King reads as sworn: the assertions below observe nothing"
    assert {a for _, a in king} == {"p_npc_050"}
    assert all(_commanded_by_a_seat(w, "p_npc_020", a) for _, a in king)

    w2 = build_realm(1)
    kat = _orders(w2, "p_npc_089", [("p_npc_011", "duty.taken")])
    assert ("dispatch", "p_npc_011") in kat, "the order to the man the Katepano commands did not form"
    assert all(_commanded_by_a_seat(w2, "p_npc_089", a) for _, a in kat)

    own = _orders(build_realm(1), "p_npc_050", [("p_npc_050", "duty.taken")])
    assert [a for _, a in own if a == "p_npc_050"] == [], "a man ordered himself"
