"""v10 IN-61 -- RS-27 SUCCESSION: THE HEIR IS A TITLE, THE THRONE IS THE HEIR'S OWN CLAIM (B10-09).

Jordan 2026-10-14: *"designated heir is not a verb but a status or title. the heir still has to claim
their throne"*. Built: `off_king` basis `inheritance`, `off_heir` basis `appointed` (`offices.yaml`);
`rosters.yaml: successions {off_king: off_heir}` and `inheritance` in `conferral_bases`;
`state/gate.py::FILLED_BY` keyed by gate basis with its first narrowing only (`inheritance` -> the claim
basis; refused to `conferral`, so `may_fill` refuses an inheritance seat), `REVOCATION_DISPOSAL
["inheritance"]: None`, both refused at import unless total; the `succeed` row as the heir's claim --
admitted iff the seat has no live `hold` and the actor holds its `successions` title -- whose ONE write
opens every vacant seat naming that title and closes the title. H-217's `succession` arrangement, the
`_disposal` hold site and the contested-succession arms are CR-35's (B10-17), not tested here.

EVERY ARM BELOW FAILS IF THE MECHANISM IS WRONG; each says which conjunct it observes. The hand-built
arms go through the REAL fold (`SeasonDriver.resolve`) and the real write gate; the planted-`release`
arm runs a real season after CR-26's `release` route (`test_in61_heir_hears_vacancy.py`).
"""
from __future__ import annotations

import copy

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import CONFERRAL_BASES, SUCCESSIONS
from ..decision import choose as CH
from ..gaps import Unspecified
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..state import gate as G
from ..state.carriers import Act, Tenure
from ..state.ids import H
from .test_in61_heir_hears_vacancy import _holder, _one_season

THRONE, TITLE, DUCHY = "off_king", "off_heir", "off_duke_valorsmark"


def _realm(seed=0):
    w = build_realm(seed)
    king, heir = _holder(w, THRONE), _holder(w, TITLE)
    assert king and heir and king != heir, "fixture: no distinct throne-holder and heir"
    return w, SeasonDriver(w), king, heir


def _act(w, d, actor, verb, n, **payload):
    """One hand-built act through the REAL fold at RESOLVE; returns the Events' kinds."""
    w.step = Step.RESOLVE
    w.frozen = False
    out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id=f"in61_{n}", actor=actor, verb=verb,
                                                         payload=payload)],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    return [e.kind for e in out]


def _vacate_by_release(w, d, king):
    kinds = _act(w, d, king, "release", "rel", subject=THRONE)
    assert _holder(w, THRONE) is None and king in w.persons, f"the release did not vacate: {kinds}"
    return kinds


def _live_hold(w, who, seat):
    return any(t.kind == "hold" and t.live and t.subject == who and t.object == seat for t in w.tenures)


# --- THE CLAIM EXECUTES (the exit), AND THE TITLE IS SPENT BY IT ---------------------------------

def test_the_heir_claims_the_vacant_throne_and_his_title_closes_in_the_same_act():
    """EXIT: the throne vacated, the title-holder's `succeed` opens the throne's `hold` for him, through
    the real fold. FALSIFIER: *the claimant's `off_heir` hold still live after the claim* -- asserted
    closed. The new `hold` carries the throne's grant (`World.add_tenure` stamps it)."""
    w, d, king, heir = _realm()
    _vacate_by_release(w, d, king)
    kinds = _act(w, d, heir, "succeed", "claim", subject=THRONE)
    assert "succession.refused" not in kinds, kinds
    assert {"succession.claimed", "tenure.closed"} <= set(kinds) and "tenure.opened" not in kinds, kinds
    assert _holder(w, THRONE) == heir, "the claim did not seat the heir"
    assert not _live_hold(w, heir, TITLE), "the claimant's title is still live after the claim"
    assert _holder(w, TITLE) is None, "the title passed to somebody (one title deep)"
    new = next(t for t in w.tenures if t.kind == "hold" and t.live and t.object == THRONE)
    assert set(w.offices[THRONE].remit_acts) <= set(new.granted_acts), new.granted_acts


def test_a_claim_on_a_held_throne_is_refused():
    """FALSIFIER: *a claim on a held throne admitted*. The King lives and sits; the heir's claim is
    refused at the precondition (`may_claim`'s vacancy conjunct) and moves nothing."""
    w, d, king, heir = _realm()
    kinds = _act(w, d, heir, "succeed", "held", subject=THRONE)
    assert kinds == ["succession.refused"], kinds
    assert _holder(w, THRONE) == king and _live_hold(w, heir, TITLE)


def test_a_claim_by_anyone_but_the_title_holder_is_refused_at_the_fold_and_at_the_gate():
    """FALSIFIER: *a hold opened through `inheritance` for an actor who does not hold the registered heir
    seat*. (1) The fold: every other living seat-holder's `succeed` on the vacant throne is refused.
    (2) The gate itself, below the precondition: a non-heir's own `hold` on the throne, opened in the same
    write that ended his OWN seat-`hold` (a released licence for a different title), is refused by every
    basis; the SAME write by the heir, ending `off_heir`, is admitted (the control: the gate is not
    refusing every opening)."""
    w, d, king, heir = _realm()
    _vacate_by_release(w, d, king)
    others = sorted({t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object in w.offices
                     and t.subject not in (heir,)})
    assert len(others) >= 5, others
    for i, p in enumerate(others):
        assert _act(w, d, p, "succeed", f"other{i}", subject=THRONE) == ["succession.refused"], p
    assert _holder(w, THRONE) is None

    def judged(who, title_seat):
        own = next(t for t in w.tenures
                   if t.kind == "hold" and t.live and t.subject == who and t.object == title_seat)
        was = copy.copy(own)                            # a detached copy from before (`was`)
        own.until = w.tick                              # the write's closure of his own seat-hold (T-m)
        nt = Tenure(H(w.world_seed, w.tick, who, f"hold:{THRONE}"), who, THRONE, "hold", w.tick)
        try:
            return G.refuse_unauthored(w, [(nt, None), (own, was)], who, None, frozenset())
        finally:
            own.until = None
    stranger = next(p for p in others
                    if any(t.kind == "hold" and t.live and t.subject == p and t.object in w.offices
                           for t in w.tenures))
    stranger_seat = next(t.object for t in w.tenures
                         if t.kind == "hold" and t.live and t.subject == stranger and t.object in w.offices)
    refused = judged(stranger, stranger_seat)
    assert [t.object for t, _ in refused] == [THRONE], refused     # his own closure passes (T-m)
    assert judged(heir, TITLE) == [], "the heir's claim write is refused by the gate: the control fails"


def test_no_seat_may_confer_the_vacant_throne():
    """FALSIFIER: *a `confer` of the vacant throne by the Widow Regent (or any seat) admitted*. `may_fill`
    refuses an `inheritance` seat through EVERY seat in the realm, and a hand-built `confer` through the
    Regent's seat is refused in the fold. CONTROL: the same seats with the throne's basis read as
    `appointed` -- at least one of them may fill it, so the refusal is the basis, not a purview miss."""
    w, d, king, heir = _realm()
    _vacate_by_release(w, d, king)
    off = w.offices[THRONE]
    seated = [(t.subject, t.object) for t in w.tenures
              if t.kind == "hold" and t.live and t.object in w.offices]
    assert len(seated) >= 20, len(seated)
    assert not any(G.may_fill(w, who, via, off) for who, via in seated)
    regent = _holder(w, "off_widow_regent")
    kinds = _act(w, d, regent, "confer", "conf", subject=THRONE, to=heir)
    assert kinds == ["confer.refused"], kinds
    assert _holder(w, THRONE) is None
    off.conferral = "appointed"                        # the control: the basis, not the purview
    try:
        assert any(G.may_fill(w, who, via, off) for who, via in seated), "no seat reaches the throne"
    finally:
        off.conferral = "inheritance"


# --- THE ONE-ACT CLAIM: TWO SEATS, ONE TITLE ----------------------------------------------------

def test_one_claim_opens_every_vacant_seat_that_names_the_title_and_closes_the_title(monkeypatch):
    """THE ONE-ACT FALSIFIER (the second decision round's): the King dies holding BOTH `off_king` and
    `off_duke_valorsmark`, and both seats name the heir's title (`off_duke_valorsmark`'s row is CP-T09-06's,
    B10-17, so it is planted here, in place, on this world and the shared roster dict only). ONE `succeed`
    on the throne opens both seats and closes the title: one act, one write. A second claim, now that both
    are held, is refused (first valid claim wins)."""
    w, d, king, heir = _realm()
    assert _holder(w, DUCHY) == king, "fixture: the King no longer holds the Crown's duchy"
    monkeypatch.setitem(SUCCESSIONS, DUCHY, TITLE)
    monkeypatch.setattr(w.offices[DUCHY], "conferral", "inheritance")
    w.step = Step.MATTER
    w._emitted_by_write = []
    _die(w, mint_token(w, WriteClass.MATTER), king)
    assert king not in w.persons and _holder(w, THRONE) is None and _holder(w, DUCHY) is None
    assert G.claimable_seats(w, heir, TITLE) == tuple(sorted((THRONE, DUCHY)))
    kinds = _act(w, d, heir, "succeed", "both", subject=THRONE)
    assert "succession.refused" not in kinds, kinds
    assert _holder(w, THRONE) == heir and _holder(w, DUCHY) == heir, "one claim did not open both seats"
    assert not _live_hold(w, heir, TITLE), "the title was not closed by the claim"
    opened = [t for t in w.tenures if t.kind == "hold" and t.subject == heir and t.since == w.tick
              and t.object in (THRONE, DUCHY)]
    assert len(opened) == 2, opened
    assert _act(w, d, heir, "succeed", "again", subject=DUCHY) == ["succession.refused"]


# --- A THRONE VACATED BY ITS HOLDER'S `release` REACHES THE HEIR, WHO FORMS THE CLAIM -------------

def test_a_throne_released_by_its_holder_reaches_the_heir_and_he_forms_the_claim(monkeypatch):
    """The `release` route IN-61's GATE names, CR-26's `_plant` shape: the King's own `release` of the
    throne through the real fold, the real WITNESS, then a real season. The heir is handed a question
    naming the vacant throne (CR-26's chain) and FORMS `succeed` on it (`confer`'s `referent_class: Office`
    machinery, narrowed by `own_title_declines`). NO OTHER PERSON forms it (the narrowing: everybody heard
    of the throne by the chronicle). Whether he then executes it is the scorer's draw; it is recorded,
    and if he did, his title is closed and the throne is his."""
    w, d, king, heir = _realm()
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS),
                       [Act(id="in61_rel", actor=king, verb="release", payload={"subject": THRONE})],
                       contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert _holder(w, THRONE) is None and king in w.persons
    w.log.extend(events)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    formed = []
    orig = CH.opening_set

    def spy(p, v, q, fx):
        out = orig(p, v, q, fx)
        formed.extend((p.id, c.subject) for c in out if c.verb == "succeed")
        return out
    monkeypatch.setattr(CH, "opening_set", spy)
    _one_season(w, d)
    assert (heir, THRONE) in formed, f"the heir never formed the claim; formed: {formed}"
    assert {pid for pid, _ in formed} == {heir}, f"somebody but the heir formed a claim: {formed}"
    claimed = _holder(w, THRONE) == heir
    print(f"\nIN-61 RELEASE ARM: heir {heir} formed `succeed` on {THRONE} {formed.count((heir, THRONE))} "
          f"time(s); executed in the season: {'yes' if claimed else 'no'}")
    if claimed:
        assert not _live_hold(w, heir, TITLE)


# --- THE IMPORT CHECKS: TOTAL OVER `conferral_bases`, REFUSED OTHERWISE ----------------------------

def test_the_shipped_mappings_pass_their_import_checks():
    """CONTROL for the refusals below: the shipped `FILLED_BY`, `REVOCATION_DISPOSAL` and `successions`
    pass, and `FILLED_BY` carries the first narrowing exactly (`inheritance` -> the claim basis alone)."""
    G.check_filled_by()
    G.check_revocation_disposal()
    G.check_successions()
    assert set(G.FILLED_BY) == set(CONFERRAL_BASES) | {None} and "inheritance" in CONFERRAL_BASES
    assert G.FILLED_BY[None] == frozenset(), "a seat declaring no basis is filled by something"
    assert G.FILLED_BY["inheritance"] == {G.CLAIM}
    assert all(G.FILLED_BY[b] == {G.CONFERRAL} for b in ("appointed", "elected", "annex"))
    assert G.REVOCATION_DISPOSAL["inheritance"] is None


def test_a_filled_by_missing_a_conferral_basis_is_refused_at_import(monkeypatch):
    monkeypatch.delitem(G.FILLED_BY, "inheritance")
    with pytest.raises(Unspecified, match="seat openers"):
        G.check_filled_by()


def test_a_basis_missing_from_revocation_disposal_is_refused_at_import(monkeypatch):
    monkeypatch.delitem(G.REVOCATION_DISPOSAL, "inheritance")
    with pytest.raises(Unspecified, match="revocation disposals"):
        G.check_revocation_disposal()


def test_a_new_conferral_basis_with_neither_mapping_is_refused_by_both_checks(monkeypatch):
    """A COPIED roster with a fifth basis, the shipped file untouched: both mappings now miss it, and each
    check refuses on its own."""
    monkeypatch.setattr(G, "CONFERRAL_BASES", frozenset(CONFERRAL_BASES) | {"tanistry"})
    with pytest.raises(Unspecified, match="seat openers"):
        G.check_filled_by()
    with pytest.raises(Unspecified, match="revocation disposals"):
        G.check_revocation_disposal()


def test_a_filled_by_naming_a_basis_that_opens_no_seat_is_refused(monkeypatch):
    monkeypatch.setitem(G.FILLED_BY, "inheritance", frozenset({G.HANDOVER}))
    with pytest.raises(Unspecified, match="name no basis that opens a seat"):
        G.check_filled_by()


def test_a_succession_on_a_seat_the_claim_does_not_open_is_refused(monkeypatch):
    """`successions` against `offices.yaml`: a key whose row is `appointed` (the claim does not open it),
    and an `inheritance` row with no key (a seat nobody can ever fill), each refuse."""
    monkeypatch.setitem(SUCCESSIONS, "off_widow_regent", TITLE)
    with pytest.raises(Unspecified, match="the claim does not open it"):
        G.check_successions()
    monkeypatch.delitem(SUCCESSIONS, "off_widow_regent")
    monkeypatch.delitem(SUCCESSIONS, THRONE)
    with pytest.raises(Unspecified, match="no title passes it"):
        G.check_successions()
