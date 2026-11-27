"""B21b.16 (CP-T09-07 (a), AM-F-15; `FA §3.3` S3): `retain` -- THE CONTESTED OFFER OF SERVICE.

A seat-holder `via` a seat granting `confer` offers a known person service; the offer is a draw on that person (`contests: "a standing"`), its obstacle the one
composer's, with the man's tie to a rival (`rival_tie`), his dislike of the seat's faction (`opinion_of_faction`) and his regard of the offerer among its terms.
Won, his own `oblige` opens to the exercised seat; lost, the offer is `retain.declined` and nothing opens. All drive the built realm, seed 0 (the Duke of Varfell
offers a Varfell man with no seat and no oath), the uncapped arm (`obstacle_ceiling` None: `H-213`'s control, where every term is read), folding through the
shipped `SeasonDriver.resolve`.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import WriteClass
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state import gate
from engine.season.state.carriers import Act, Tenure

DUKE, SEAT, MAN, RIVAL_SEAT = "p_npc_052", "off_duke_varfell", "p_npc_002", "off_king"
GUARD = "cohort_guard_off_duchess_hafenmark"


def _world(seed=0, tied=False, step=None):
    """The realm at `seed`, uncapped; `tied` gives MAN a live oath to a seat of another faction (the rival tie); `step` sweeps `tie_step`."""
    w = build_realm(seed)
    w.fixtures = w.fixtures.sweep("obstacle_ceiling", None)
    if step is not None:
        w.fixtures = w.fixtures.sweep("tie_step", step)
    if tied:
        w.add_tenure(Tenure(f"t_tie_{MAN}", MAN, RIVAL_SEAT, "oblige", since=0))
    return w


def _retain(w, n, to=MAN):
    d = SeasonDriver(w)
    out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(f"a_ret_{n}", DUKE, "retain", payload={"to": to}, via=SEAT)],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return d, out


def _terms(event):
    return [name for name, _ in dict(event.ending)["terms"]]


def _first(kind, to=MAN):
    """The first world (act id 0, 1, ...) whose offer folds to `kind`, with its driver and events."""
    for n in range(40):
        w = _world()
        d, out = _retain(w, n, to)
        if out[0].kind == kind:
            return w, d, out
    raise AssertionError(f"no offer of 40 folded to {kind!r}")


def _oaths(w, to=MAN):
    return [t for t in w.tenures if t.kind == "oblige" and t.subject == to and t.object == SEAT and t.live]


def test_a_won_retain_opens_his_oblige_to_the_seat():
    """Won, the offered man swears: his own live `oblige` to the exercised seat opens, with the declared term, an oath and not a bench's imposed edge; the seat's
    establishment lists him. The control: before the offer he is sworn to nobody there and the seat lists him not."""
    w0 = _world()
    assert _oaths(w0) == [] and MAN not in Q.establishment_of(w0, SEAT), "control failed -- the man was sworn already"
    w, _d, out = _first("retain.accepted")
    assert [e.kind for e in out] == ["retain.accepted"]
    (edge,) = _oaths(w)
    assert edge.term is not None and not edge.imposed and edge.since == w.tick
    assert gate.is_sworn_to(w, MAN, SEAT) and MAN in Q.establishment_of(w, SEAT)


def test_a_lost_retain_emits_retain_declined_and_opens_nothing():
    """Lost, the offer is `retain.declined` and no edge opens; witnessed, a person at the place holds the refusal as a claim."""
    w, d, out = _first("retain.declined")
    assert [e.kind for e in out] == ["retain.declined"]
    assert _oaths(w) == [] and not gate.is_sworn_to(w, MAN, SEAT)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    assert any(c.predicate == "retain.declined" for p in w.persons.values() for c in p.ledger), "no one holds the witnessed refusal"


def test_a_man_sworn_to_a_rival_seat_declines_more_often():
    """The obstacle reads him: the same offer on the same dice (seeds 0-9, two acts each), to the man with a live oath to a seat of another faction and to
    the same man with the tie removed. The tied man's obstacle lists `rival_tie` and the free man's does not; no offer the free man declines is accepted by the
    tied one (the draw is the act's own, so the terms alone differ), and the tied man declines more of the twenty."""
    free = tied = checked = 0
    for seed in range(10):
        for n in range(2):
            f, t = _retain(_world(seed), n)[1][0], _retain(_world(seed, tied=True), n)[1][0]
            assert "rival_tie" not in _terms(f) and "rival_tie" in _terms(t), (_terms(f), _terms(t))
            free_declined, tied_declined = f.kind == "retain.declined", t.kind == "retain.declined"
            assert tied_declined or not free_declined, "a higher obstacle accepted what the lower one declined"
            free, tied, checked = free + free_declined, tied + tied_declined, checked + 1
    assert checked >= 10
    assert tied > free, (free, tied)


def test_a_guard_is_not_offered_service():
    """A guard cohort is a retainer already: an offer to one is refused before the draw (`retain.refused`), nothing opens, and it is sworn to its own seat only.
    The control: the same duke's offer to an individual is drawn (accepted or declined, never refused)."""
    w = _world()
    guard_oath = [(t.subject, t.object) for t in w.tenures if t.kind == "oblige" and t.subject == GUARD and t.live]
    assert w.persons[GUARD].is_cohort and guard_oath == [(GUARD, "off_duchess_hafenmark")]
    _d, out = _retain(w, 0, GUARD)
    assert [e.kind for e in out] == ["retain.refused"], [e.kind for e in out]
    assert [(t.subject, t.object) for t in w.tenures if t.kind == "oblige" and t.subject == GUARD and t.live] == guard_oath
    assert _retain(_world(), 0)[1][0].kind in ("retain.accepted", "retain.declined")
