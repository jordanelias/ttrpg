"""B11.22 (`08_FI_06`): A TELLING CARRIES THE HAND THAT DID THE DEED (`Fixtures told_pairing`, `Said.pairing`).

Through the real WITNESS barrier on a hand-built world, `test_told_by_channel.py`'s `g6` method: W witnessed K kill V
(a `person.died` claim on V and the `seen` claim that names K, both firsthand, one `when` and `lap`); W tells J; J tells L.
`tiny_world`: `p_low` (W), `p_mid` (J) and `p_other` (K) stand in `Hh`; `p_high` (L) stands in `S`; `p_king` (V) is the victim.
"""
from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..epistemic import SEEN_PREDICATE, Seen
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q as PQ
from ..state.carriers import Act, Claim, Event, Said
from ..state.ids import H

W, J, L, K, V = "p_low", "p_mid", "p_high", "p_other", "p_king"
DIED = "person.died"
STRATUM = "contested_physical"       # the stratum of a row emitting `person.died` (`person_q._KIND_STRATA`)
SIGHTING = Seen(stratum=STRATUM, marks=(), who=K, why=None)


def _world(arm: str):
    """The gate's world at `told_pairing` `arm`. Returns `(w, tell, claims)`: `tell(teller, subject, degree)` has the teller choose
    `said_of(own ledger, subject)` and runs the telling through the real WITNESS barrier, returning the `Said` it carried;
    `claims(pid, predicate)` is `pid`'s claims of that predicate on V."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("told_pairing", arm))
    d = SeasonDriver(w)
    n = [0]
    w.persons[W].ledger.extend([
        Claim("c_w_died", W, V, DIED, True, w.tick, "firsthand", 100, "own", 0),
        Claim("c_w_seen", W, V, SEEN_PREDICATE, SIGHTING, w.tick, "firsthand", 100, "own", 0)])

    def move(pid, rung):
        next(t for t in w.tenures if t.subject == pid and t.kind == "contain" and t.live).object = rung

    def tell(teller, subject, degree="Success"):
        n[0] += 1
        w.tick += 1
        p = w.persons[teller]
        said = PQ.said_of(p.ledger, subject, w.fixtures, p)
        act = Act(id=f"a_tp_{n[0]}", actor=teller, verb="tell", payload={"subject": subject, "said": said})
        w.acts.append(act)
        ev = Event(H(w.world_seed, w.tick, teller, f"ev:news.told:{act.id}"), "news.told", [], [act.id], w.tick, degree, ())
        w.log.append(ev)
        d.act_of[ev.id] = act
        d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
        return said

    def claims(pid, predicate):
        return [c for c in w.persons[pid].ledger if c.subject == V and c.predicate == predicate and c.source == "told_by"]

    w.move = move
    return w, tell, claims


def _doers(w, pid):
    return PQ.deed_doers(w.persons[pid].ledger, {"kinds": [DIED]}, pid)


def test_a_telling_carries_the_hand():
    """W tells J what he saw: J names K as the doer of V's death, holds the deed as an act of K's, and judges K by the told half."""
    w, tell, claims = _world("on")
    said = tell(W, K)
    assert said == Said(V, DIED, True, 100, (), SIGHTING), said
    ledger = w.persons[J].ledger
    assert _doers(w, J) == (K,)
    assert [c.chain for c in claims(J, DIED)] == [(W,)] and [c.chain for c in claims(J, SEEN_PREDICATE)] == [(W,)]
    assert [c.predicate for c in PQ.attributed_deeds(ledger, K)] == [DIED]
    assert [c.predicate for c in PQ.suffered_deeds(ledger, V)] == [DIED]
    # the deed is judged by the `told` half: a pursuit that leans on a death moves it, the firsthand half stays 0
    w.persons[J].pursuits = {"honour": 1.0}          # a pursuit the shipped `deed:person.died` cell leans on (read: a nonzero told half)
    judged, told = PQ.deeds_judged(w.persons[J], K)
    assert judged == 0.0 and told < 0.0, (judged, told)


def test_a_retelling_keeps_the_chain():
    """J tells L, who was not there: L names K, and both his claims carry the chain `(W, J)`."""
    w, tell, claims = _world("on")
    tell(W, K)
    w.move(J, "S")                                  # J stands with L, away from W and K
    said = tell(J, V)
    assert said.pairing == SIGHTING and said.chain == (W,), said
    assert _doers(w, L) == (K,)
    assert [c.chain for c in claims(L, DIED)] == [(W, J)] and [c.chain for c in claims(L, SEEN_PREDICATE)] == [(W, J)]
    assert [c.predicate for c in PQ.attributed_deeds(w.persons[L].ledger, K)] == [DIED]


def test_a_partial_telling_withholds_it():
    """At `Partial` the copy says that it happened and not who: J holds the death, the told sighting names nobody, and the deed names nobody."""
    w, tell, claims = _world("on")
    tell(W, K, "Partial")
    assert [c.value for c in claims(J, DIED)] == [True]
    (seen,) = claims(J, SEEN_PREDICATE)
    assert seen.value == Seen(stratum=STRATUM, marks=(), who=None, why=None), seen.value
    assert _doers(w, J) == () and list(PQ.attributed_deeds(w.persons[J].ledger, K)) == []


def test_the_witness_asked_about_the_doer_says_the_death():
    """W asked about K says `(V, person.died, True)` with the sighting as its pairing; asked about V (whose claims are the pool as before) says the same."""
    w, _tell, _claims = _world("on")
    p = w.persons[W]
    said = PQ.said_of(p.ledger, K, w.fixtures, p)
    assert (said.subject, said.predicate, said.value) == (V, DIED, True) and said.pairing == SIGHTING, said
    assert PQ.said_of(p.ledger, V, w.fixtures, p) == said


def test_off_arm_is_todays_reading_and_hash_equal():
    """`off`: the witness asked about K says nothing, nothing is told with a hand, J names nobody; and the realm at seed 0 after one
    season reads the hash it read before this item (B11.21's after-reading; B11.99 re-reads it with the other arm-off pins)."""
    w, tell, claims = _world("off")
    assert PQ.said_of(w.persons[W].ledger, K, w.fixtures, w.persons[W]) is None
    said = tell(W, V)
    assert said.pairing is None
    assert claims(J, SEEN_PREDICATE) == [] and _doers(w, J) == ()
    from ..boot.realm import build_realm
    from ..harness import populated
    realm = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("told_pairing", "off"))
    populated.run(1, 0, w=realm)
    assert realm.content_hash() == "879408acf51cb0882800d0058eebbea8"


def _ledger(*rows):
    """A hand-built hearer's ledger from `(holder-chain, predicate, value)` rows at one `(when, lap)`."""
    out = []
    for i, (chain, predicate, value) in enumerate(rows):
        out.append(Claim(f"c_f_{i}", J, V, predicate, value, 5, "told_by" if chain else "firsthand", 100, "own", 0, chain=chain))
    return out


def _sight(who):
    return Seen(stratum=STRATUM, marks=(), who=who, why=None)


def test_a_hearers_own_sighting_is_never_the_told_ones():
    """J holds his OWN sighting that Y struck V in that lap, and was told by W (sighting K) and by X (sighting Z) of the same death in the
    same lap: each deed names its own hand, from its own chain. Planted failure: key the told index without the chain (or fold it into the
    own index) and the deeds read two hands and name nobody."""
    ledger = _ledger(((), DIED, True), ((), SEEN_PREDICATE, _sight("p_x")),
                     ((W,), DIED, True), ((W,), SEEN_PREDICATE, _sight(K)),
                     (("p_third",), DIED, True), (("p_third",), SEEN_PREDICATE, _sight("p_z")))
    seen = PQ._seen_index(ledger)
    assert [PQ.deed_doer(c, seen) for c in ledger if c.predicate == DIED] == ["p_x", K, "p_z"]
    assert PQ.deed_doers(ledger, {"kinds": [DIED]}, J) == ("p_x", K, "p_z")


def test_an_unpaired_telling_names_nobody():
    """A told death with no pairing names nobody, though the hearer holds his own sighting of someone acting on V in that lap; a told
    pairing that names two hands, or one that withholds the hand, names nobody either."""
    own = ((), SEEN_PREDICATE, _sight("p_x"))
    for told in ([], [((W,), SEEN_PREDICATE, _sight(K)), ((W,), SEEN_PREDICATE, _sight("p_z"))], [((W,), SEEN_PREDICATE, _sight(None))]):
        ledger = _ledger(own, ((W,), DIED, True), *told)
        assert PQ.deed_doer(ledger[1], PQ._seen_index(ledger)) is None, told
