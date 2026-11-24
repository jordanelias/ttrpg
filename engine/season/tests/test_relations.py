"""B10.20 -- what is done to a man decides what he thinks of who did it (`U5a_CHAR_owed_amendments` §4; `Fixtures deed_counterparty`, H-474).

`person_q.deed_term` scores an unpaired deed by the judge's pursuits alone; at `deed_counterparty: person_subject` a deed whose verb row takes a
Person as its subject is multiplied by `_bond(judge, <the one it was done to>, lean)` as a paired deed is. The one acted on is read off the
judge's own `seen` claims (`person_q.deed_counterparty`); the arm ships at `paired_only`, today's reading.

FALSIFIER: the four judges below read alike at `person_subject` (the term does not reach the deed), or the judge who has no sighting of the
one acted on reads differently at the two arms (the factor guessed a counterparty).
"""
from __future__ import annotations


from ..data.pursuits import to_axes
from ..data.rosters import PURSUITS, SEEN_PREDICATE
from ..decision import choose as CH
from ..epistemic import Seen
from ..harness import probes as P
from ..queries import person_q as PQ
from ..state.carriers import Candidate, Claim, Person

DOER, ONE = "p_doer", "p_acted_on"        # the doer, and the one the deed was done to
FULL = (ONE, 5, 5)                        # valence 5 x weight 5 = STANCE_MAX: full allegiance (enmity is its negative)


def _kind_and_pursuit():
    """A deed kind of a Person-subject row, and a pursuit whose lean on it is NEGATIVE (so allegiance doubles the condemnation, enmity cancels it)."""
    for kind in sorted(PQ.PERSON_SUBJECT_KINDS):
        if not PQ._KIND_STRATA[kind]:
            continue                      # a kind no row's stratum names is never paired to a sighting
        for e in sorted(PURSUITS):
            if PQ._lean(to_axes({e: 1.0}), kind) < 0:
                return kind, e
    raise AssertionError("no Person-subject deed kind is condemned by any pursuit: the factor could not be shown to matter")


def _judge(pid, e, kind, stance=(), saw_who_it_was_done_to=True):
    """`pid`, who holds one firsthand deed claim `(DOER, kind, True)` and, unless `saw_who_it_was_done_to` is false, the sighting
    that names `DOER` acting on `ONE`."""
    p = Person(pid, pid)
    p.pursuits = {e: 1.0}
    p.stance = list(stance)
    p.ledger.append(Claim(f"c_deed_{pid}", pid, DOER, kind, True, 0, "firsthand", 100, "own"))
    if saw_who_it_was_done_to:
        stratum = next(iter(PQ._KIND_STRATA[kind]))
        p.ledger.append(Claim(f"c_seen_{pid}", pid, ONE, SEEN_PREDICATE, Seen(stratum=stratum, marks=(), who=DOER), 0, "firsthand", 100, "own"))
    return p


def test_a_deed_done_to_a_man_is_weighed_by_his_bond_to_him():
    kind, e = _kind_and_pursuit()
    w = P.tiny_world()
    judges = {"himself": _judge(ONE, e, kind),
              "ally": _judge("p_ally", e, kind, stance=[FULL]),
              "stranger": _judge("p_stranger", e, kind),
              "enemy": _judge("p_enemy", e, kind, stance=[(ONE, -5, 5)]),
              "blind": _judge("p_blind", e, kind, saw_who_it_was_done_to=False)}
    checked = 0
    for unit in ("raw", "stance"):
        base = w.fixtures.sweep("regard_unit", unit)
        control = {k: PQ.regard(j, DOER, base.sweep("deed_counterparty", "paired_only")) for k, j in judges.items()}
        live = {k: PQ.regard(j, DOER, base.sweep("deed_counterparty", "person_subject")) for k, j in judges.items()}
        # today's reading: every judge reads the deed by his pursuits alone, and it is a condemnation
        assert len(set(control.values())) == 1 and control["stranger"] < 0, (unit, control)
        # the live arm: an ally doubles the condemnation, an enemy cancels it, a stranger reads the control
        assert live["ally"] < live["stranger"] < live["enemy"], (unit, live)
        assert live["stranger"] == control["stranger"], (unit, live, control)
        # a judge who IS the one it was done to is his own full ally
        assert live["himself"] == live["ally"], (unit, live)
        # a judge whose ledger does not name the one acted on is not guessed a counterparty
        assert live["blind"] == control["blind"], (unit, live, control)
        checked += len(live)
    assert checked == 2 * len(judges)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# B10.62 -- an authored relation seeds a stance row and the holder's own `bond:` claim (`02_CHAR_relations_have_a_ground`; `boot/realm.py::seed_relations`).
#
# FALSIFIER: with rows authored a rival ranks a hostile act on his rival no differently from on a stranger (the stance term does not reach the candidate),
# or a holder's ledger holds no `bond:` claim after the build, or a person nobody authored a relation for holds one.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# The source's six rows (`02_CHAR_relations_have_a_ground` edit 6), AUTHORED at BA1.08 on the shipped registry with the draft's weights.
# [ASSUMPTION; low; Jordan to correct; basis: `IS-A-11` draft table (d), weight 4 where the source's words are absolute, else 3]
SIX = (("NPC-020", "NPC-032", "kin", 1, 4),         # Almud -> Lenneth
       ("NPC-032", "NPC-020", "kin", 1, 4),         # Lenneth -> Almud
       ("NPC-050", "NPC-020", "rivalry", -1, 3),    # Baralta -> Almud
       ("NPC-020", "NPC-050", "rivalry", -1, 3),    # Almud -> Baralta
       ("NPC-070", "NPC-020", "service", 1, 3),     # Ehrenwall -> Almud
       ("NPC-052", "NPC-050", "rivalry", -1, 4))    # Vaynard -> Baralta


def _pid(cid):
    return "p_" + cid.lower().replace("-", "_")


def test_an_authored_relation_gives_its_holder_a_stance_row_and_his_own_bond_claim():
    from ..boot.realm import seed_relations
    w = P.tiny_world()
    seed_relations(w, [("p_mid", "p_low", "rivalry", -1, 2), ("p_mid", "p_high", "kin", 1, 3), ("p_other", "p_mid", "service", 1, 2)])
    mid, other, low = w.persons["p_mid"], w.persons["p_other"], w.persons["p_low"]
    assert mid.stance == [("p_low", -1, 2), ("p_high", 1, 3)] and other.stance == [("p_mid", 1, 2)]
    held = {(c.subject, c.predicate, c.value, c.source, c.confidence, c.visibility, c.chain) for c in mid.ledger}
    conf = w.fixtures.get("confidence_default")
    assert held == {("p_low", "bond:rivalry", True, "firsthand", conf, "own", ()), ("p_high", "bond:kin", True, "firsthand", conf, "own", ())}
    # a bond is the HOLDER's own knowledge: the one it names holds nothing of it, and a person nobody authored a relation for holds no stance row or claim
    assert low.ledger == [] and low.stance == [] and w.persons["p_king"].ledger == []


def test_a_rival_ranks_hostile_acts_higher_than_a_stranger():
    """On `build_realm(0)`: the shipped registry authors the six rows (BA1.08), so none is planted."""
    from ..boot.realm import build_realm
    w = build_realm(0)
    fx = w.fixtures
    checked = 0
    for holder, to, ground, valence, weight in SIX:
        p, other = w.persons[_pid(holder)], _pid(to)
        # each of the six rows reached the holder's stance and his ledger through `build_realm`
        assert (other, valence, weight) in p.stance, (holder, to)
        assert any(c.subject == other and c.predicate == f"bond:{ground}" and c.value is True and c.source == "firsthand" for c in p.ledger), (holder, to)
        checked += 1
    assert checked == len(SIX)
    for holder, rival in (("NPC-020", "NPC-050"), ("NPC-050", "NPC-020")):
        p, rival = w.persons[_pid(holder)], _pid(rival)
        named = {_pid(t) for h, t, *_ in SIX if h == holder}
        stranger = next(pid for pid in sorted(w.persons) if pid != p.id and pid not in named and pid.startswith("p_npc_")
                        and CH.stance_term(p, Candidate("challenge", pid), fx) == 0.0)
        # the act done against him (`challenge`, regard_sign -1) is a pull toward a rival and no pull on a stranger; `confer` (regard_sign +1) falls the other way
        assert CH.stance_term(p, Candidate("challenge", rival), fx) > CH.stance_term(p, Candidate("challenge", stranger), fx) == 0.0, holder
        assert CH.stance_term(p, Candidate("confer", rival), fx) < CH.stance_term(p, Candidate("confer", stranger), fx) == 0.0, holder
