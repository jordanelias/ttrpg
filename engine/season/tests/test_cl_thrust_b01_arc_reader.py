"""CL-THRUST B0.1 -- `harness/arc.py`, the driver-side ARC reader and its two rosters (TL §1.2, §8 B0.1;
G-28). These tests pin the INSTRUMENT, never a number from a realm run (V2): what a real log reads is
the measurement and it moves whenever the game does, so the realm reading is printed and not asserted.

The falsifier the position names, observed rather than assumed (§0.1 pt 3):

  (i)   a linked self-and-world chain through `ARC_SELF` / `ARC_WORLD` writes reads TRUE;
  (ii)  both effects with no `causes` link reads FALSE;
  (iii) acts that write nothing read FALSE;
  (iv)  a WITNESSED `move` (a real season, real witnesses) reads FALSE;
  (v)   a WITNESSED `tell` reads FALSE;
  (vi)  a `petition` answered by the conferrer's `confer` of the petitioner reads TRUE through clause (4);
  and the REFUSAL NULL (an ARC whose clause (1) act was refused reads FALSE).

Every FALSE has a control that proves the world was not empty: the same log read with the bookkeeping
Receipts counting (`unrestricted=True`) reads TRUE for (iv) and (v), and the same chain with its missing
piece restored reads TRUE for (ii) and (iii). The planted failure -- the exclusion of `claim_ledger` and
`Person.travel_leg` dropped -- turns (iv) and (v) TRUE (`test_dropping_the_exclusions_...`), and was run
as a source mutation once at the build (the roster edited and `validate_roster` bypassed: (iv) and (v)
red). Two nulls: the shuffled-`causes` null, and the bookkeeping null, which must read HIGHER than the
restricted reading (the STOP-IF: when it does not, the roster is leaking).
"""

from __future__ import annotations

from types import SimpleNamespace as NS

import pytest

from ..data.matrix import MATRIX, WriteClass
from ..harness import arc as A
from ..harness import probes as P
from ..harness import storybar as SB
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Act, Claim, Event, Question, Receipt, Scene, StateChange
from ..state.ids import H, ROOT
from .test_g3_not_yours import _gov_world

THRUST = "th_planted"
CLAIM_LEDGER, TRAVEL_LEG = ("Person", "claim_ledger"), ("Person", "travel_leg")


def _on(*act_ids):
    return lambda act, occasion: THRUST if act.id in act_ids else None


def _by(actor):
    return lambda act, occasion: THRUST if act.actor == actor else None


# ---------------------------------------------------------------------------------------------
# PLANTED LOGS: a hand-built chain over `tiny_world`, read through `log=` (the reader does not care
# that the gate never minted these Receipts; the guard on `w.log` is the game's, not the instrument's).
# ---------------------------------------------------------------------------------------------

def _rc(subject, field, serial):
    return Receipt(subject=subject, mode="set", driver="Act", field=field, serial=serial)


def _chain(*, link=True, self_write=True, world_write=True, world_subject="site_harbour",
           world_field="condition", world_kind="condition.worn", actor="p_low", k=1):
    """`k` independent acts by `actor`, each with a self-effect Event citing the act and a world-effect
    Event that cites the self-effect Event (`link`) or nothing (`not link`). Returns `(w, d, log, ids)`."""
    w = P.tiny_world()
    own = next(t.id for t in w.tenures if t.subject == actor and t.kind == world_q.RESIDE_KIND)
    log, ids, serial = [], [], 0
    for i in range(k):
        a = Act(id=f"A{i}", actor=actor, verb="work")
        w.acts.append(a)
        ids.append(a.id)
        serial += 2
        e1 = Event(f"e1_{i}", "tenure.closed",
                   [_rc(own, "until", serial)] if self_write else [], [a.id], 0)
        e2 = Event(f"e2_{i}", world_kind,
                   [_rc(world_subject, world_field, serial + 1)] if world_write else [],
                   [e1.id] if link else [ROOT], 0)
        log += [e1, e2]
    return w, NS(scenes={}), log, ids


def _read(w, d, log, on, **kw):
    return A.read_arcs(w, d, on, log=log, refused=frozenset(), **kw)


# ---------------------------------------------------------------------------------------------
# REAL SEASONS: the witnessed `move` and `tell` run through the driver, so the claim deposits that made
# v1's "any Receipt" wrong are the gate's own.
# ---------------------------------------------------------------------------------------------

def _witnessed(verb):
    w = P.tiny_world()
    if verb == "move":
        actor, payload = "p_low", {"to": "S"}
    else:
        actor, payload = "p_mid", {"subject": "p_high", "to": "p_low"}
        w.persons[actor].ledger.append(
            Claim("c_k", actor, "p_high", "exists:Person", 1, 0, "firsthand", 100, "own"))

    def choose(p, v, s, ask_budget):
        return [P.Act_(w, p, verb, payload=payload)] if p.id == actor else []
    d = P._run_d(w, P.once(choose), contest_max_depth=w.fixtures.get("contest_max_depth"))
    acts = [a for a in w.acts if a.actor == actor and a.verb == verb]
    assert len(acts) == 1, f"the {verb} was not formed: {[a.verb for a in w.acts]}"
    return w, d, actor


def _petition_answered(*, link=True):
    """`p_mid` files a petition (the real `petition` fold); `p_king`'s `confer` of `p_mid` to `off_reeve`
    (the real `confer` fold) is chosen from a scene whose occasion is a claim landed on the petition's
    Event -- the route `loop/resolve.py::_act_events` stamps into `causes[]` (IN-50). `link=False` is the
    same confer with no scene: the same two Receipts, no edge between them."""
    w, d = _gov_world()
    w.step = None

    def fold(*acts):
        out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        w.log.extend(out)
        return out
    filed, = fold(Act(id="pet1", actor="p_mid", verb="petition",
                      payload={"record": "pet_x", "subject": "p_low", "to": "p_high", "from": "Hh"}))
    assert filed.kind == "petition.filed"
    scene = None
    if link:
        w.log.append(Event("ev_dep", "claim.deposited", [StateChange("claim_x", "set", "Act")],
                           [filed.id], w.tick))
        d.scenes["sc_x"] = Scene("sc_x", "p_king", [], occasion=Question("q_x", "claim_landed", (),
                                                                          about="claim_x"))
        scene = "sc_x"
    conferred = fold(Act(id="cf1", actor="p_king", verb="confer", via="off_crown", scene=scene,
                         payload={"subject": "off_reeve", "to": "p_mid"}))
    assert [e.kind for e in conferred] == ["tenure.opened"], [e.kind for e in conferred]
    return w, d


# ---------------------------------------------------------------------------------------------
# THE ROSTERS
# ---------------------------------------------------------------------------------------------

def test_the_rosters_are_acts_class_cells_of_the_write_matrix():
    checked = 0
    for roster in (A.ARC_SELF, A.ARC_WORLD):
        for pair in roster:
            row = MATRIX[pair]                      # KeyError: not a write_matrix.yaml key
            assert {s.name for s in row.steps} & {"RESOLVE"}, pair
            assert not {s.name for s in row.steps} & {"WITNESS"}, pair
            assert pair[1] != "claim_ledger" and pair not in (TRAVEL_LEG, ("Person", "exists")), pair
            checked += 1
    assert checked == len(A.ARC_SELF) + len(A.ARC_WORLD) >= 20
    assert A.validate_roster(A.ARC_SELF) == A.ARC_SELF and A.validate_roster(A.ARC_WORLD) == A.ARC_WORLD


@pytest.mark.parametrize("pair,why", [
    (("Nowhere", "field"), "not a key"),
    (("Person", "claim_ledger"), "claim_ledger"),
    (("Person", "travel_leg"), "excluded by name"),
    (("Person", "exists"), "excluded by name"),
    (("Person", "weight"), "no RES step"),      # CENSUS only
    (("Rung", "yield"), "no RES step"),         # MATTER only
])
def test_the_loader_refuses_what_the_roster_may_not_hold(pair, why):
    with pytest.raises(A.ArcRosterRefused, match=why):
        A.validate_roster({pair})
    w, d, log, _ids = _chain()
    with pytest.raises(A.ArcRosterRefused, match=why):      # and a roster handed to the reader
        _read(w, d, log, _by("p_low"), world_fields=A.ARC_WORLD | {pair})
    with pytest.raises(A.ArcRosterRefused, match=why):
        _read(w, d, log, _by("p_low"), self_fields={pair})


# ---------------------------------------------------------------------------------------------
# THE SIX PLANTED WORLDS (TL §8 B0.1)
# ---------------------------------------------------------------------------------------------

def test_i_a_linked_self_and_world_chain_reads_true():
    w, d, log, ids = _chain()
    r = _read(w, d, log, _on(*ids))
    assert r.holds("p_low") and r.arcs == {"p_low": {THRUST: ("A0",)}} and r.deaths == {}
    assert r.persons == ("p_low",) and r.count() == 1


def test_ii_both_effects_with_no_causes_link_reads_false():
    w, d, log, ids = _chain(link=False)
    r = _read(w, d, log, _on(*ids))
    assert r.persons == ("p_low",) and not r.holds("p_low") and r.arcs == {}
    # the control: the SAME two Receipts, linked, read TRUE -- the missing edge is the whole difference
    w, d, log, ids = _chain(link=True)
    assert _read(w, d, log, _on(*ids)).holds("p_low")


def test_iii_acts_that_write_nothing_read_false():
    w, d, log, ids = _chain(self_write=False, world_write=False)
    r = _read(w, d, log, _on(*ids))
    assert r.persons == ("p_low",) and not r.holds("p_low")
    assert not _read(w, d, log, _on(*ids), unrestricted=True).holds("p_low")       # nothing to count at all
    # controls: either half alone is not an arc; both restored is
    for kw in ({"self_write": True, "world_write": False}, {"self_write": False, "world_write": True}):
        w, d, log, ids = _chain(**kw)
        assert not _read(w, d, log, _on(*ids)).holds("p_low"), kw
    w, d, log, ids = _chain()
    assert _read(w, d, log, _on(*ids)).holds("p_low")


def test_iv_a_witnessed_move_reads_false():
    w, d, actor = _witnessed("move")
    on = _by(actor)
    assert not A.read_arcs(w, d, on).holds(actor)
    assert A.read_arcs(w, d, on).persons == (actor,)
    # the control: the move DID write (travel_leg) and was SEEN (deposits in other ledgers); with the
    # bookkeeping Receipts counted the same log reads TRUE, so the FALSE above is the roster's doing
    assert A.read_arcs(w, d, on, unrestricted=True).holds(actor)
    mv = next(e for e in w.log if e.kind == "travel.moved")
    assert [A._Records(w).of(r, mv)[0] for r in mv.changes] == [TRAVEL_LEG]       # its one write is the excluded one
    seen = [e for e in w.log if e.kind == "claim.deposited" and mv.id in e.causes]
    assert seen, "the move was not witnessed; the FALSE above observed no bookkeeping"


def test_v_a_witnessed_tell_reads_false():
    w, d, actor = _witnessed("tell")
    on = _by(actor)
    assert A.read_arcs(w, d, on).persons == (actor,)
    assert not A.read_arcs(w, d, on).holds(actor)
    assert A.read_arcs(w, d, on, unrestricted=True).holds(actor)       # deposits in his ledger and the hearer's


def test_vi_a_petition_answered_by_the_conferrers_confer_of_the_petitioner_reads_true():
    w, d = _petition_answered()
    r = A.read_arcs(w, d, _on("pet1"))
    assert r.arcs == {"p_mid": {THRUST: ("pet1",)}}, r.arcs
    # the effect pair is the one clause (4) links: the petition's Record (world) and the conferral on
    # the PETITIONER's hold (self) -- by the conferrer's act, not his own
    rec = A._Records(w)
    kinds = {rec.of(x, e) for e in w.log for x in e.changes if isinstance(x, Receipt)}
    assert (("Record", "exists"), "pet_x") in kinds and (("Tenure", "until"), "p_mid") in kinds, kinds
    # controls: (a) the same two Receipts with the edge between them absent read FALSE; (b) the conferrer's
    # own act is not the petitioner's arc: the confer, on the thrust, writes his OWN world only
    w2, d2 = _petition_answered(link=False)
    assert not A.read_arcs(w2, d2, _on("pet1")).holds("p_mid")
    assert not A.read_arcs(w, d, _on("cf1")).holds("p_king")


# ---------------------------------------------------------------------------------------------
# THE REFUSAL NULL
# ---------------------------------------------------------------------------------------------

def test_the_refusal_null_an_arc_whose_clause_one_act_was_refused_reads_false():
    w, d = _petition_answered()
    on = _on("pet1")
    assert A.read_arcs(w, d, on).holds("p_mid")                  # the control, read BEFORE the plant
    assert "pet1" not in SB.refusal_sets(w, w.tick)[0]
    # the driver's own sign of a refusal: an Event of the row's `emits_on_refusal` kind, id derived as
    # `corpus_run._attribute_acts` derives it; the act's writes and the chain are untouched
    w.log.append(Event(H(w.world_seed, w.tick, "p_mid", "petition.refused:pet1"), "petition.refused",
                       [], ["pet1"], w.tick))
    assert "pet1" in SB.refusal_sets(w, w.tick)[0]
    r = A.read_arcs(w, d, on)
    assert not r.holds("p_mid") and r.persons == ("p_king", "p_mid")
    # and the override reads the same way, so the planted-set path and the derived path agree
    assert not A.read_arcs(w, d, on, refused=frozenset({"pet1"})).holds("p_mid")
    assert A.read_arcs(w, d, on, refused=frozenset()).holds("p_mid")


# ---------------------------------------------------------------------------------------------
# WHAT THE CLAUSES TURN ON: ownership, deaths, the kind of a Receipt
# ---------------------------------------------------------------------------------------------

def test_a_write_on_ones_own_record_is_not_a_world_write_and_anothers_is():
    # `Rung.stores` of the actor's OWN person-rung (id == the person's) is his, so it is no world effect ...
    w, d, log, ids = _chain(world_subject="p_low", world_field="stores", world_kind="stores.changed")
    assert not _read(w, d, log, _on(*ids)).holds("p_low")
    # ... and the same cell on another person's rung is
    w, d, log, ids = _chain(world_subject="p_mid", world_field="stores", world_kind="stores.changed")
    assert _read(w, d, log, _on(*ids)).holds("p_low")


def test_a_death_is_counted_apart_and_is_not_the_arcs_world_effect():
    # `Person.body` is on the world roster (a wound to another); the same Receipt on a `person.died`
    # Event is a death, which is not
    w, d, log, ids = _chain(world_subject="p_mid", world_field="body", world_kind="body.changed")
    assert _read(w, d, log, _on(*ids)).holds("p_low")
    w, d, log, ids = _chain(world_subject="p_mid", world_field="body", world_kind="person.died")
    r = _read(w, d, log, _on(*ids))
    assert not r.holds("p_low") and r.deaths == {"p_low": ("A0",)}
    assert not _read(w, d, log, _on(*ids), unrestricted=True).holds("p_low")


def test_a_receipt_is_read_as_the_record_it_wrote():
    w = P.tiny_world()
    rec = A._Records(w)
    ev = lambda kind: Event("ev", kind, [], [ROOT], 0)
    own = next(t for t in w.tenures if t.subject == "p_low")
    assert rec.of(_rc(own.id, "until", 1), ev("tenure.closed")) == (("Tenure", "until"), "p_low")
    # a person-rung shares the person's id; the cell decides which collection is meant
    assert rec.of(_rc("p_low", "stores", 1), ev("stores.changed")) == (("Rung", "stores"), "p_low")
    assert rec.of(_rc("p_low", "stance", 1), ev("stance.moved")) == (("Person", "stance"), "p_low")
    # a docket item and a destroyed record are in no collection: the field, then the Event kind, say which
    assert rec.of(_rc("D", "petition", 1), ev("carry.made"))[0] == ("DocketItem", "petition")
    assert rec.of(_rc("gone", "exists", 1), ev("record.destroyed"))[0] == ("Record", "exists")
    assert rec.of(_rc("gone", "exists", 1), ev("no.such.kind"))[0] == (None, "exists")
    # a deposit is its holder's
    w.persons["p_mid"].ledger.append(Claim("c_h", "p_mid", "p_high", "exists:Person", 1, 0, "firsthand", 100, "own"))
    assert A._Records(w).of(_rc("c_h", "claim_ledger", 1), ev("claim.deposited")) == (CLAIM_LEDGER, "p_mid")


# ---------------------------------------------------------------------------------------------
# THE PLANTED FAILURE AND THE TWO NULLS
# ---------------------------------------------------------------------------------------------

def test_dropping_the_exclusions_turns_the_witnessed_move_and_tell_true(monkeypatch):
    """THE PLANTED FAILURE (§0.1 pt 3): the exclusion of `claim_ledger` and `Person.travel_leg` dropped
    (rosters widened, the loader's refusal bypassed) and (iv) and (v) read TRUE -- v1's "any Receipt"
    reading. This is what the two tests above would show if the exclusion were absent."""
    monkeypatch.setattr(A, "validate_roster", lambda pairs: frozenset(pairs))
    selfs = A.ARC_SELF | {TRAVEL_LEG, CLAIM_LEDGER}
    worlds = A.ARC_WORLD | {CLAIM_LEDGER}
    checked = 0
    for verb in ("move", "tell"):
        w, d, actor = _witnessed(verb)
        assert A.read_arcs(w, d, _by(actor), self_fields=selfs, world_fields=worlds).holds(actor), verb
        checked += 1
    assert checked == 2


def test_the_shuffled_causes_null_reads_below_the_linked_log():
    k = 40
    w, d, log, ids = _chain(k=k)
    real = len(_read(w, d, log, _on(*ids)).arcs["p_low"][THRUST])
    assert real == k
    below = 0
    for seed in range(8):
        shuffled = A.shuffled_causes(log, seed)
        assert [e.id for e in shuffled] == [e.id for e in log]
        assert any(s.causes != e.causes for s, e in zip(shuffled, log))       # the null moved something
        arcs = _read(w, d, shuffled, _on(*ids)).arcs.get("p_low", {}).get(THRUST, ())
        assert len(arcs) < real, (seed, len(arcs))
        below += 1
    assert below == 8


def test_the_bookkeeping_null_reads_higher_than_the_restricted_reading():
    """The STOP-IF: when the unrestricted reading is not HIGHER, the roster is leaking."""
    restricted = unrestricted = checked = 0
    for verb in ("move", "tell"):
        w, d, actor = _witnessed(verb)
        r = A.read_arcs(w, d, _by(actor))
        u = A.read_arcs(w, d, _by(actor), unrestricted=True)
        assert u.count() > r.count(), (verb, r.arcs, u.arcs)
        restricted, unrestricted, checked = restricted + r.count(), unrestricted + u.count(), checked + 1
    w, d = _petition_answered()                  # an arc the rosters keep: the null may not read BELOW it
    r, u = A.read_arcs(w, d, _on("pet1")), A.read_arcs(w, d, _on("pet1"), unrestricted=True)
    assert u.count() >= r.count() >= 1
    restricted, unrestricted, checked = restricted + r.count(), unrestricted + u.count(), checked + 1
    assert checked == 3 and unrestricted > restricted


# ---------------------------------------------------------------------------------------------
# EMPTY DATA, AND A REAL LOG (printed, never asserted)
# ---------------------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def realm():
    return SB.drive(0, 1, "off", None)


def test_with_no_thrust_authored_the_reader_reads_false_for_every_person_and_moves_no_hash(realm):
    w, d, bounds = realm
    before = w.content_hash()
    r = A.read_arcs(w, d)
    assert r.arcs == {} and r.deaths == {} and not any(r.holds(p) for p in r.persons)
    assert len(r.persons) > 0, "the realm log has no actors; the FALSE above observed nothing"
    assert not A.read_arcs(w, d, lambda act, occasion: None, unrestricted=True).arcs
    assert w.content_hash() == before


def test_the_reader_runs_on_a_real_log_and_changes_nothing(realm, capsys):
    w, d, bounds = realm
    before, n_log, n_acts = w.content_hash(), len(w.log), len(w.acts)
    on = A.ambition_thrusts(w)
    r = A.read_arcs(w, d, on, n=len(bounds))
    u = A.read_arcs(w, d, on, n=len(bounds), unrestricted=True)
    nulls = [A.read_arcs(w, d, on, n=len(bounds), log=A.shuffled_causes(w.log, s)).count() for s in range(3)]
    on_thrust = sum(1 for a in w.acts if on(a, A._occasion_row(d, a)) is not None)
    # relations that hold of ANY log, not counts: dropping restrictions only adds writes
    assert u.count() >= r.count()
    assert w.content_hash() == before and len(w.log) == n_log and len(w.acts) == n_acts
    with capsys.disabled():
        print(f"\n[B0.1 realm reading, seed 0, 1 season] persons={len(r.persons)} acts={n_acts} "
              f"on_thrust_acts={on_thrust} ARC_persons={r.count()} "
              f"ARC_acts={sum(len(a) for ts in r.arcs.values() for a in ts.values())} "
              f"persons_whose_acts_reach_a_death={len(r.deaths)} "
              f"bookkeeping_null={u.count()} shuffled_causes_null={nulls}")
