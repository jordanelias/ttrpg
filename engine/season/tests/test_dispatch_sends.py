"""`IS-B3-FA-05` (V12 B21.57; CP-T09-08, CP-T09-07 (b)'s gate clause; closes `14_VERBS_BINDING_D` D4) -- A `dispatch` THAT SENDS:
the sender's act deposits the order, and the man's own `comply` is what moves him (A-24).

Every test drives the hand-built `tiny_world` (the Duke on `off_duke`, who grants `dispatch`; `p_mid`, an unseated clerk living at
S inside his land, whom his seat commands) through the real fold (`SeasonDriver.resolve`) and the real WITNESS. No test reads a
realm count: since B21.55 no `dispatch` forms in realm play (no ledger holds a `duty.taken` claim), so the realm cannot show one.
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q, world_q
from ..state.carriers import Act, Tenure
from ..state.gate import may_muster
from .test_in10_record_operands import _resolve

DUKE, SEAT = "p_high", "off_duke"          # seated at D, standing at S; grants `dispatch`
MAN, FROM, TO = "p_mid", "S", "D"          # an unseated clerk in the Duke's land, sent one rung up
STRANGER = "p_king"                        # stands at R, outside the Duke's land, holds no seat of his own


def _world():
    """`tiny_world` at a MATTER barrier, the clerk standing at S where the Duke does (he witnesses what the Duke does)."""
    w = P.tiny_world()
    for t in w.persons[MAN].tenures:
        if t.live and t.kind in ("contain", "reside"):
            t.object = FROM
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _witnessed(w, d, out):
    d.witness(mint_token(w, WriteClass.INTERIOR), out)


def _dispatch(w, d, key="d1", to=MAN, **payload):
    out = _resolve(w, d, Act(id=key, actor=DUKE, verb="dispatch", via=SEAT, payload={"subject": to, **payload}))
    _witnessed(w, d, out)
    return out


def _answer(w, d, verb, rid, key="ans", who=MAN):
    out = _resolve(w, d, Act(id=key, actor=who, verb=verb, payload={"subject": rid}))
    _witnessed(w, d, out)
    return out


def _place(w, pid):
    return world_q.place_of(w, pid)


def _kinds(out):
    return [e.kind for e in out]


def test_a_complied_dispatch_moves_the_man_and_charges_him_the_leg():
    """The sender's act moves nobody: it deposits the order (a `dispensation` addressed to the man, `at` the place) and the man
    learns it. His `comply` is the act that moves him, through `_relocate`, and the journey is charged to him (`travel_leg`).
    CONTROL: the same act before the answer, and a second `comply` on the order (he is there already) moves nothing."""
    w, d = _world()
    sent = _dispatch(w, d, dest=TO)
    assert _kinds(sent) == ["order.given"], _kinds(sent)
    rec = w.records["rec:d1"]
    assert rec.kind == "dispensation" and world_q.order_destination(w, rec.id) == TO
    assert _place(w, MAN) == FROM and w.persons[MAN].travel_leg == [], "CONTROL: the sender's act moved nobody"
    assert any(c.subject == rec.id and c.predicate.startswith("content:") for c in w.persons[MAN].ledger), \
        "the man learned the order's terms (proclaimed)"
    assert rec.id in world_q.writs_addressed(w, w.persons[MAN]), "the order is his to answer"
    done = _answer(w, d, "comply", rec.id)
    assert _kinds(done) == ["compliance.given", "travel.ordered"], _kinds(done)
    assert _place(w, MAN) == TO, "his own comply moved him"
    assert w.persons[MAN].travel_leg == [TO], "and charged him the leg (`budget`'s distance penalty reads its length)"
    again = _answer(w, d, "comply", rec.id, key="ans2")
    assert _kinds(again) == ["compliance.given"] and w.persons[MAN].travel_leg == [TO], "already there: answered, nothing to go to"


def test_a_defied_dispatch_moves_nobody_and_is_read_by_the_issuer():
    """`evade / defy` is the other answer: the man stays, and the issuer's own ledger holds the withheld answer, which
    `person_q.suspicion_of` (the recall occasion's reading) counts. CONTROL: before the defiance the issuer's suspicion is zero."""
    w, d = _world()
    _dispatch(w, d, dest=TO)
    rec = w.records["rec:d1"]
    assert person_q.suspicion_of(w.persons[DUKE], MAN) == 0, "CONTROL"
    out = _answer(w, d, "evade / defy", rec.id)
    assert _kinds(out) == ["compliance.withheld"], _kinds(out)
    assert _place(w, MAN) == FROM and w.persons[MAN].travel_leg == [], "nobody moved"
    assert person_q.suspicion_of(w.persons[DUKE], MAN) == 1, "the issuer reads it"


def test_a_dispatch_to_a_man_outside_the_command_is_refused():
    """A-22: the seat orders only whom it commands. The King stands at R and holds no seat the Duke's may revoke, so it is
    refused (`dispatch.refused`) and deposits no order; sworn to the Duke's seat he is commanded and it is admitted. A destination
    outside the seat's purview (the realm above the Duke's duchy) is refused the same way. CONTROL: the admitted pair."""
    w, d = _world()
    refused = _dispatch(w, d, key="d_far", to=STRANGER, dest=TO)
    assert _kinds(refused) == ["dispatch.refused"] and "rec:d_far" not in w.records, _kinds(refused)
    outside = _dispatch(w, d, key="d_up", dest="R")
    assert _kinds(outside) == ["dispatch.refused"] and "rec:d_up" not in w.records, "R is above the Duke's purview"
    w.add_tenure(Tenure("t_oath_king", STRANGER, SEAT, "oblige", 0))
    sent = _dispatch(w, d, key="d_sworn", to=STRANGER, dest=TO)
    assert _kinds(sent) == ["order.given"] and "rec:d_sworn" in w.records, "CONTROL: sworn, he is commanded"


def test_a_dispatch_with_no_destination_moves_nobody_even_when_answered():
    """CONTROL (the entry's): a `dispatch` naming no destination behaves as it did -- `order.given`, nothing moved -- and the
    man's `comply` on it is the answer alone, `compliance.given`, with nothing to go to."""
    w, d = _world()
    assert _kinds(_dispatch(w, d)) == ["order.given"]
    rec = w.records["rec:d1"]
    assert world_q.order_destination(w, rec.id) is None
    out = _answer(w, d, "comply", rec.id)
    assert _kinds(out) == ["compliance.given"], _kinds(out)
    assert _place(w, MAN) == FROM and w.persons[MAN].travel_leg == []


def test_the_muster_basis_admits_a_sworn_man_who_is_no_member_of_the_seats_faction():
    """CP-T09-07 (b): `may_muster` admits a moved man holding a live `oblige` to `via`, as well as one committed to its faction.
    The Duke's seat grants the muster act (`dispatch`). CONTROL: the same man before he swears, and a man sworn to another seat."""
    w, _ = _world()
    assert not may_muster(w, DUKE, SEAT, MAN), "CONTROL: no oath, no commitment to the faction"
    w.add_tenure(Tenure("t_oath_other", MAN, "off_dicastery", "oblige", 0))
    assert not may_muster(w, DUKE, SEAT, MAN), "CONTROL: an oath to another seat is no tie to this one"
    w.add_tenure(Tenure("t_oath_mid", MAN, SEAT, "oblige", 0))
    assert may_muster(w, DUKE, SEAT, MAN), "sworn to the seat: mustered, though no member of its faction"
