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
