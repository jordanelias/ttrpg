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
from ..epistemic import Seen
from ..harness import probes as P
from ..queries import person_q as PQ
from ..state.carriers import Claim, Person

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
