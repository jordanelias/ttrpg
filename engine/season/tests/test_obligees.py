"""Plan position `17a` -- OBLIGEES. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`
§8 `17a`; content owner r2 item 9 (`proposals/2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md`
§A.3.4, §A.1.5 RULED (b) and (d)) and `03_SEATS_AND_CONTENT.md` §A.9.

What the position built, each asked of the real fold and the real WITNESS barrier:
  * `oblige` resolves: `_req_oblige` (the subject is a seat whose `binds` admits the joiner, the actor
    does not hold it, no live `oblige` already) and `_eff_oblige` (opens the `oblige` Tenure).
  * `world_q.establishment_of` is a Query over live `oblige` Tenures, and `_ch_post_remit` -- the
    obligee channel, minting `inferred` -- is its caller.
  * `Office.establishment`, its matrix row and `establish`'s third `writes:` entry are gone.

THE FALSIFIER, verbatim: *"The claim-source histogram moves `inferred` 0 -> N with `N >= 1` asserted;
and a person NOT obliged to the seat and NOT co-located does NOT receive the `inferred` claim -- the
flood control."* r2 `05`'s own: *"an obligee ELSEWHERE does not witness."*

The fixture is `probes.tiny_world`: `R` > `D` > `S` > `Hh`. `p_high` (the duke) stands in `S` and holds
`off_duke`, whose rung is `D`; `p_low`, `p_mid`, `p_other` stand in `Hh`, inside `D`; `p_king` in `R`,
outside it. So `p_mid` obliged to `off_duke` is AT the seat without being in the duke's room, and
`p_king` obliged to it is ELSEWHERE.
"""

from __future__ import annotations

import dataclasses
from collections import Counter

import pytest

from .. import epistemic as EP
from ..data.matrix import MATRIX, MATRIX_RETIRED, WriteClass
from ..data.rosters import BINDS_BASES, CHANNEL_CLAIM_SOURCE, WITNESS_CHANNELS
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..decision.options import opening_set
from ..epistemic import CHANNEL_PREDICATES, observers_for
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop import effects as EF
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.predicates import REQUIRES_PREDICATES
from ..queries import world_q
from ..state.carriers import Act, Office, Question, View
from ..state.gate import NO_CHANGE

SEAT = "off_duke"
DUKE = "p_high"


def _fold(w, d, *acts):
    """One RESOLVE pass over `acts`, logged and WITNESSED as `SeasonDriver.season` does it: the fold's
    Events go to the log before WITNESS so a deposit's cause resolves (S19.5)."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def _world():
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _oblige(w, d, who, seat=SEAT, key=None):
    return _fold(w, d, Act(id=key or f"ob_{who}_{seat}", actor=who, verb="oblige",
                           payload={"subject": seat}))


def _obliges(w, who, seat=SEAT):
    return [t for t in w.tenures
            if t.kind == "oblige" and t.subject == who and t.object == seat and t.live]


def _sources(w) -> Counter:
    """THE CLAIM-SOURCE HISTOGRAM, over every ledger -- `populated.run`'s own `claim_sources`."""
    return Counter(c.source for p in w.persons.values() for c in p.ledger)


def _holding(w, e, source):
    """Who holds the event-kind claim about `e` under `source`. Every Event these tests read is the
    only one of its kind in its world, so the kind names the Event."""
    return {pid for pid, p in w.persons.items()
            for c in p.ledger if c.source == source and c.predicate == e.kind}


# ================================================================================================
# 1 -- `oblige` RESOLVES, AND ITS EDGE IS WHAT `establishment_of` READS
# ================================================================================================

def test_17a_oblige_is_resolvable_and_takes_releases_route():
    row = VERB_TABLE["oblige"]
    assert "oblige" in resolvable_verbs(), "`oblige` has a precondition and a body and is still not foldable"
    assert "oblige" in EF.EFFECTS and "oblige" in REQUIRES_PREDICATES
    assert row.requires_typed is None, "a typed cell AND a predicate is two readings of one cell"
    assert row.emits == ("duty.taken",) and row.emits_on_refusal == ("duty.refused",)
    assert _OPENERS_FROM_EFFECTS.get("oblige") == ["oblige"], _OPENERS_FROM_EFFECTS.get("oblige")


def test_17a_an_oblige_opens_its_tenure_and_the_query_reads_it(monkeypatch):
    """The mechanism, and the control that it is THIS effect's edge: the same act with the body
    stubbed to `NO_CHANGE` opens nothing and is refused by the gate's `NoOpReceipt` (`7a`'s shape)."""
    w, d = _world()
    assert world_q.establishment_of(w, SEAT) == [], "fixture: somebody already serves the seat"
    out = _oblige(w, d, "p_mid")
    assert [e.kind for e in out] == ["duty.taken"], [e.kind for e in out]
    [t] = _obliges(w, "p_mid")
    assert t.since == w.tick and t.until is None
    assert world_q.establishment_of(w, SEAT) == ["p_mid"]

    w2, d2 = _world()
    monkeypatch.setitem(EF.EFFECTS, "oblige", lambda w, a, res=None: NO_CHANGE)
    out2 = _oblige(w2, d2, "p_mid")
    assert [e.kind for e in out2] == ["duty.refused"] and not _obliges(w2, "p_mid"), (
        [e.kind for e in out2])


# ================================================================================================
# 2 -- `_req_oblige`: EACH CLAUSE REFUSES, AS `duty.refused`, AND OPENS NOTHING
# ================================================================================================

@pytest.mark.parametrize("who, seat, why", [
    ("p_mid", "einhir_texts", "a bare string -- ED-IN-0211's own reverted case"),
    ("p_mid", "p_low", "a person is not a seat"),
    ("p_mid", "Hh", "a rung is not a seat"),
    (DUKE, SEAT, "the occupant is not his own seat's obligee"),
])
def test_17a_req_oblige_refuses_what_is_not_a_seat_one_can_serve(who, seat, why):
    w, d = _world()
    out = _oblige(w, d, who, seat)
    assert [e.kind for e in out] == ["duty.refused"], (why, [e.kind for e in out])
    assert not [t for t in w.tenures if t.kind == "oblige"], why


def test_17a_one_oblige_per_person_and_seat():
    w, d = _world()
    assert [e.kind for e in _oblige(w, d, "p_mid", key="first")] == ["duty.taken"]
    assert [e.kind for e in _oblige(w, d, "p_mid", key="second")] == ["duty.refused"]
    assert world_q.establishment_of(w, SEAT) == ["p_mid"], "one person listed twice"


def test_17a_the_seats_binds_is_read_at_the_act_and_refused_at_construction():
    """`ARCH F.17`: *"`oblige`'s `requires` reads the seat's `binds`"*. The roster's one value admits;
    an off-roster value refuses the act -- and the constructor refuses to build one at all, so the act
    clause is observable only on a value mutated after construction, which is what this does."""
    stray = "by_decree"
    assert stray not in BINDS_BASES and BINDS_BASES == {"members_by_admission"}
    with pytest.raises(Unspecified):
        Office("off_x", "Reeve", "S", ["issue"], faction="Crown", binds=stray)
    w, d = _world()
    w.offices[SEAT].binds = stray
    assert [e.kind for e in _oblige(w, d, "p_mid")] == ["duty.refused"]
    w.offices[SEAT].binds = "members_by_admission"
    assert [e.kind for e in _oblige(w, d, "p_mid", key="again")] == ["duty.taken"], (
        "control: the same act on the rostered basis is admitted")


# ================================================================================================
# 3 -- THE FALSIFIER: `inferred` 0 -> N, AND THE FLOOD CONTROL
# ================================================================================================

def test_17a_falsifier_inferred_moves_from_zero_and_only_the_obligee_at_the_seat_holds_it():
    """The duke declares a march on `S` through his seat. `march.declared` is `contested_physical`,
    so `chronicle` (a `binding_decision` filter) does not carry it -- it is the kind the retired remit
    broadcast carried to every `remit:dispatch` holder in the realm (47 pairs in `build_realm(0)`'s
    first season, all `march.declared`). Now:
      * `p_mid`  -- obliged, at the seat (Hh inside D), not in the room (S): holds it `inferred`;
      * `p_king` -- obliged, ELSEWHERE (R, outside D): holds nothing `inferred`;
      * `p_low`, `p_other` -- not obliged, not co-located: hold nothing `inferred` -- the flood control;
      * the duke -- in the room: `firsthand`, by the channel that precedes this one."""
    w, d = _world()
    assert _sources(w)["inferred"] == 0, "fixture: a ledger already holds an inferred claim"
    _oblige(w, d, "p_mid")
    _oblige(w, d, "p_king")
    assert sorted(world_q.establishment_of(w, SEAT)) == ["p_king", "p_mid"]
    before = _sources(w)["inferred"]
    assert before == 0, f"taking a duty minted {before} inferred claims -- `oblige` is no seat's act"

    out = _fold(w, d, Act(id="m1", actor=DUKE, verb="march", payload={"subject": "S"}, via=SEAT))
    e = next((x for x in out if x.kind == "march.declared"), None)
    assert e is not None, f"fixture: the march was not declared: {[x.kind for x in out]}"
    assert not any(CHANNEL_PREDICATES["chronicle"](w, e, pid) for pid in w.persons), (
        "fixture: `chronicle` carries this kind, so every person would be credited there first")

    n = _sources(w)["inferred"]
    assert n >= 1, f"the claim-source histogram did not move: inferred {before} -> {n}"
    assert _holding(w, e, "inferred") == {"p_mid"}, _holding(w, e, "inferred")
    for pid in ("p_low", "p_other", "p_king"):
        assert not [c for c in w.persons[pid].ledger if c.predicate == e.kind], (
            f"{pid} is neither at the seat as its obligee nor in the room, and holds the march")
    assert dict(observers_for(w, e, "all_five", list(w.persons))) == {
        DUKE: "co_located", "p_mid": "post_remit"}
    assert _holding(w, e, "firsthand") == {DUKE}


def test_17a_released_the_obligee_no_longer_infers():
    """`release` is the closer every `oblige` ends through (`04 §A.3` row 14). After it, the seat's
    next act reaches the former obligee by no channel -- the Query and the channel both follow."""
    w, d = _world()
    _oblige(w, d, "p_mid")
    assert [e.kind for e in _fold(w, d, Act(id="rel", actor="p_mid", verb="release",
                                            payload={"subject": SEAT}))] == ["tenure.closed"]
    assert world_q.establishment_of(w, SEAT) == []
    out = _fold(w, d, Act(id="m2", actor=DUKE, verb="march", payload={"subject": "S"}, via=SEAT))
    e = next(x for x in out if x.kind == "march.declared")
    assert not CHANNEL_PREDICATES["post_remit"](w, e, "p_mid")
    assert _sources(w)["inferred"] == 0


def test_17a_the_channel_reads_the_obligee_set_through_establishment_of(monkeypatch):
    """r2 `05` RULED (d): *"`_ch_post_remit` calls it"* -- the Query has a caller, and the channel has
    no second copy of the set. Emptying the Query empties the channel, on an Event it admitted."""
    w, d = _world()
    _oblige(w, d, "p_mid")
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="m3", actor=DUKE, verb="march", payload={"subject": "S"}, via=SEAT)],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    e = next(x for x in out if x.kind == "march.declared")
    assert CHANNEL_PREDICATES["post_remit"](w, e, "p_mid")
    monkeypatch.setattr(world_q, "establishment_of", lambda w, office_id: [])
    assert not CHANNEL_PREDICATES["post_remit"](w, e, "p_mid"), (
        "the channel admitted an obligee the Query does not list -- it derives the set itself")


def test_17a_an_act_through_no_seat_reaches_no_obligee():
    """Clause 1: the SEAT is the act's `via`. The duke's own `move` is his, not his office's."""
    w, d = _world()
    _oblige(w, d, "p_mid")
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="mv", actor=DUKE, verb="move", payload={"to": "D"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert out, "fixture: the move emitted nothing"
    assert not any(CHANNEL_PREDICATES["post_remit"](w, e, "p_mid") for e in out)


# ================================================================================================
# 4 -- THE PRECEDENCE: TOLD BEFORE INFERRED (`19_PLAN.md`'s ordinal), IN BOTH DIRECTIONS
# ================================================================================================

def test_17a_a_binding_decision_reaches_an_obligee_told_by_not_inferred(monkeypatch):
    """`post_remit` is LAST in `witness_channels`: an obligee the public record ALSO admits holds the
    Event `told_by` (`chronicle`), never downgraded to `inferred` -- *firsthand > knot > told >
    inferred*. ⚠ BOTH DIRECTIONS (§0.1 pt 2): with the `15d` order restored (post_remit before
    chronicle) the same obligee on the same Event is credited `post_remit`, so the ORDER decides."""
    assert WITNESS_CHANNELS[-1] == "post_remit" and CHANNEL_CLAIM_SOURCE["post_remit"] == "inferred"
    assert WITNESS_CHANNELS.index("chronicle") < WITNESS_CHANNELS.index("post_remit")

    w, d = _world()
    _oblige(w, d, "p_mid")
    out = _fold(w, d, Act(id="dp", actor=DUKE, verb="dispatch", payload={"subject": "p_low"},
                          via=SEAT))
    e = next((x for x in out if x.kind == "order.given"), None)
    assert e is not None, [x.kind for x in out]
    assert CHANNEL_PREDICATES["post_remit"](w, e, "p_mid") and CHANNEL_PREDICATES["chronicle"](
        w, e, "p_mid"), "fixture: both channels must admit the obligee"
    assert dict(observers_for(w, e, "all_five", list(w.persons)))["p_mid"] == "chronicle"
    assert "p_mid" in _holding(w, e, "told_by") and "p_mid" not in _holding(w, e, "inferred")

    old = tuple(c for c in WITNESS_CHANNELS if c != "post_remit")
    old = old[:old.index("chronicle")] + ("post_remit",) + old[old.index("chronicle"):]
    monkeypatch.setattr(EP, "WITNESS_CHANNELS", old)
    assert dict(observers_for(w, e, "all_five", list(w.persons)))["p_mid"] == "post_remit"


# ================================================================================================
# 5 -- NO COMPUTED `oblige`: THE CHOOSER CANNOT NAME A SEAT (`give`'s precedent, position 16)
# ================================================================================================

def _oblige_candidates(w, pid, referents):
    p = w.persons[pid]
    q = Question("q:ob", "need", tuple(referents))
    return [c for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures)
            if c.verb == "oblige"]


def test_17a_no_person_forms_an_oblige_it_cannot_name_a_seat_for(monkeypatch):
    """`counterparty: subject` on the untyped row: nothing is carried, so no Candidate forms -- even
    for a question ABOUT the seat. CONTROL: clear the column and they form, each one an act the fold
    would refuse for a non-seat referent -- the scene tax `7a`'s `commit` measured on the corpus."""
    w, _d = _world()
    referents = (SEAT, "p_low", "Hh")
    assert VERB_TABLE["oblige"].counterparty == "subject"
    assert not _oblige_candidates(w, "p_mid", referents), "an `oblige` Candidate was formed"
    monkeypatch.setitem(VERB_TABLE, "oblige",
                        dataclasses.replace(VERB_TABLE["oblige"], counterparty=""))
    assert _oblige_candidates(w, "p_mid", referents), (
        "control: with the column cleared no Candidate forms either, so the column is not what "
        "declined them")


# ================================================================================================
# 6 -- `Office.establishment`: THREE EDITS, NOT ONE (r2 `05:214-221`)
# ================================================================================================

def test_17a_office_establishment_is_gone_from_the_carrier_the_matrix_and_establish():
    off = Office("off_x", "Reeve", "S", ["issue"], faction="Crown")
    assert not hasattr(off, "establishment") and "establishment" not in repr(off)
    assert ("Office", "establishment") not in MATRIX
    assert ("Office", "establishment") in MATRIX_RETIRED, "deleted without its retirement reason"
    assert VERB_TABLE["establish"].writes == ("Office.exists", "Office.remit_acts", "Tenure.payload")
