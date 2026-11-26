"""B21b.11 (CP-T09-02 (a), AM-F-10, AM-F-11): `declare` -- THE ROW, AND THE WAR ONLY A DECLARATION OPENS.

`declare` is a seated muster-holder's act (`remit:dispatch`, `march`'s and `raze`'s eligibility): through the one mint `_eff_utter` makes it writes the WAR
Proposition (subject the seat's faction, value the target) and the declarer's own `commit` to it in one write. `world_q.at_war` asks, beside B21's `may_wage`,
that the Proposition's creating Event's causing act is a `declare`. All three drive the built realm, seed 0, forming through `opening_set` and folding through
the shipped `SeasonDriver.resolve`.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import WriteClass
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state import gate
from engine.season.state.carriers import Act, Claim

from .test_in53_vacancy_need import _formed

OWN, TARGET = "fac_valorsmark", "fac_guilds"


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _declarer(w):
    """A Valorsmark member holding a seat whose grant carries `dispatch`, read off `Tenure.granted_acts` and not by `gate.may_wage`; and told of the
    target's creed, so the creed is a Proposition his own ledger names (`propositions_heard`) and `declare` forms on it."""
    pid = next(p for p in sorted(w.persons)
               if p in Q.members(w, OWN)
               and any(t.kind == "hold" and t.live and t.object in w.offices and gate.MUSTER_ACT in t.granted_acts
                       and gate.seat_faction(w, t.object) == OWN for t in w.persons[p].tenures))
    w.persons[pid].ledger.append(Claim(f"c_told_{pid}", pid, TARGET, "proposition.uttered", True, 0, "told", 100, "own", 0, doer="p_npc_052"))
    return pid


def _declare_candidates(w, pid, target):
    q = Q.questions_for(w, w.persons[pid])[0]
    return [c for c in _formed(w, pid, q) if c.verb == "declare" and c.subject == target]


def test_a_seated_muster_holder_declares_and_the_war_is_live():
    """A computed `declare` forms on the target's creed, folds (`war.declared`, no `proposition.uttered`), mints a WAR Proposition between the two factions
    with the declarer's own live `commit`, and `at_war` reads True both ways; the control reads False first. Witnessed, `war.declared` reaches a person who is
    not where the act was done (the realm reach of a `binding_decision` kind)."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    assert Q.at_war(w, OWN, TARGET) is False, "control failed -- a war before any declaration"
    cand = _declare_candidates(w, pid, TARGET)[0]
    out = _fold(w, d, Act("a_decl", pid, "declare", payload=_payload_of(cand), via=seat_of(w.persons[pid], cand)))
    assert [e.kind for e in out] == ["war.declared"], [e.kind for e in out]
    war = [p for p in w.propositions.values() if p.mood == Q.WAR_MOOD]
    assert len(war) == 1 and (war[0].subject, war[0].value) == (OWN, TARGET)
    assert any(t.kind == "commit" and t.object == war[0].id and t.live for t in w.persons[pid].tenures), "the declarer's own commit"
    assert Q.at_war(w, OWN, TARGET) is True and Q.at_war(w, TARGET, OWN) is True
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    here = Q.place_of(w, pid)
    far = [p for p in sorted(w.persons) if p != pid and Q.place_of(w, p) != here
           and any(c.predicate == "war.declared" for c in w.persons[p].ledger)]
    assert far, "no one away from the declarer holds the declaration"


def test_an_utter_of_mood_war_plus_a_commit_is_no_war():
    """THE S2 CONTROL: the same WAR Proposition minted by a plain `utter` and committed to by a seated muster-holder through the real fold is no war --
    `at_war` asks that the creating Event's causing act is a `declare`. The control: the identical chain minted by `declare` is."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    kinds = [e.kind for e in _fold(w, d, Act("a_utt", pid, "utter", payload={"mood": "WAR", "subject": OWN, "value": TARGET}))]
    assert kinds == ["proposition.uttered"], kinds
    kinds = [e.kind for e in _fold(w, d, Act("a_utt_commit", pid, "commit", payload={"subject": "prop:a_utt"}))]
    assert kinds == ["commitment.made"], kinds
    assert Q.at_war(w, OWN, TARGET) is False and Q.at_war(w, TARGET, OWN) is False
    cand = _declare_candidates(w, pid, TARGET)[0]
    _fold(w, d, Act("a_decl", pid, "declare", payload=_payload_of(cand), via=seat_of(w.persons[pid], cand)))
    assert Q.at_war(w, OWN, TARGET) is True


def test_declare_on_his_own_faction_is_refused():
    """`declare.refused`, nothing minted and no commit opened, for the declarer's own faction and for a target that is no rostered faction's Proposition."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    seat = next(t.object for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object in w.offices
                and gate.MUSTER_ACT in t.granted_acts and gate.seat_faction(w, t.object) == OWN)
    before = (len(w.propositions), sum(1 for t in w.tenures if t.kind == "commit"))
    refused = 0
    for n, target in enumerate((OWN, "prop:no_faction")):
        if target not in w.propositions:
            w.propositions[target] = type(w.propositions[OWN])(target, "OUGHT", pid, "a cause", True, 0)
            before = (before[0] + 1, before[1])
        kinds = [e.kind for e in _fold(w, d, Act(f"a_decl_{n}", pid, "declare", payload={"subject": target}, via=seat))]
        assert kinds == ["declare.refused"], (target, kinds)
        refused += 1
    assert refused == 2
    assert (len(w.propositions), sum(1 for t in w.tenures if t.kind == "commit")) == before
    assert Q.at_war(w, OWN, OWN) is False
