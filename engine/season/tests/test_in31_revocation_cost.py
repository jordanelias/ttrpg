"""v9 IN-31 (H-100), batch B-Q: WHAT A REVOCATION COSTS, BY THE SEAT'S PROVENANCE.

The position's brief: only WHO may attempt a revocation was modelled, never what it costs the man revoked.
The provenance carrier already exists -- a `hold`'s seat's `Office.conferral` (ED-IN-0256 (2)), which no act
changes on a live seat -- and the cost has ONE owner, `state/gate.py::REVOCATION_DISPOSAL`. JORDAN,
2026-10-21, answering the design's A1 (*"Design's answer"*): `appointed` -> a PERMANENT `ban : him ->
Act.via`; `elected`, `annex`, `None` -> nothing; a `confer` displacing an incumbent -> nothing.

THE EXIT (amended, ORCH: a computed `revoke` executes 0 times, H-207 ruling (A)): a seeded test with one
hand-built `revoke` per seat provenance, folded through the REAL fold, showing more than one outcome across
provenances -- `test_in31_the_exit_on_the_built_realm` (the realm: appointed, elected, None) and
`test_in31_one_revoke_per_provenance_through_the_fold` (all four, on the governance world).
THE FALSIFIER: every revocation writing the same thing whatever the seat's provenance -> fail. Observed
live by `monkeypatch.setitem(gate.REVOCATION_DISPOSAL, "appointed", None)` in the EXIT test (the outcomes
collapse), and by the build's mutations (recorded in the producer's receipt): the ban block deleted from
`_eff_revoke`; the `revoked` licence dropped from `refuse_unauthored`; the `_req_revoke` backstop deleted.

The helpers here are written afresh (the IN-48 test file the design names was deleted by its revert).
Nothing here builds on a `delegate` tenure kind (`architecture/meta/01_AXIOMS.md` §E.2.4).
"""
from __future__ import annotations

import pytest

from engine.season.data import verbs as V
from engine.season.data.matrix import Step, WriteClass
from engine.season.gaps import Unspecified
from engine.season.harness import populated as POP
from engine.season.loop import predicates as _preds
from engine.season.loop.effects import EFFECTS
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries.world_q import BAN_KIND, restrained
from engine.season.state import gate as G
from engine.season.state.carriers import Act, Tenure
from engine.season.state.gate import (
    DETERMINATION, NO_CHANGE, T_O, NotYours, may_determine, may_revoke)

from .test_g3_not_yours import _gov_world, _hold
from .test_in10b_termed_seat import _seasons

KING, VIA, DUKE, TARGET = "p_king", "off_crown", "p_high", "off_duke"


def _edges(w) -> set:
    """Every live Tenure as `(kind, subject, object)`."""
    return {(t.kind, t.subject, t.object) for t in w.tenures if t.live}


def _fold(w, d, act: Act) -> tuple:
    """Fold ONE hand-built act through the shipped `SeasonDriver.resolve`; `(event kinds, opened edges)`,
    the opened edges being the live `(kind, subject, object)` triples the act added."""
    before = _edges(w)
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out], _edges(w) - before


def _revoke(key, actor=KING, office=TARGET, via=VIA) -> Act:
    return Act(id=key, actor=actor, verb="revoke", payload={"subject": office, "office": office}, via=via)


def _gov(conferral="appointed"):
    """The governance world (`test_g3_not_yours._gov_world`): `p_king` on `off_crown` (realm, grants
    `confer`/`revoke`, NO `determine` -- a non-judging seat) on the rung above `off_duke`, held by `p_high`.
    The duke's seat's conferral is set to `conferral`."""
    w, d = _gov_world()
    w.offices[TARGET].conferral = conferral
    return w, d


# 1 -- THE PLAN'S FALSIFIER, ON THE GOVERNANCE WORLD -----------------------------------------------------

def test_in31_one_revoke_per_provenance_through_the_fold():
    """One hand-built `revoke` per provenance, the same revoker through the same NON-judging seat. Only
    `appointed` leaves a ban on the man revoked, objected on the revoking seat; every act emits exactly
    `tenure.closed` (the ban is no event of its own) and closes the hold."""
    w0, _ = _gov()
    assert not may_determine(w0, KING, VIA, DUKE), "fixture: `off_crown` must not judge"
    outcome = {}
    for basis in ("appointed", "elected", "annex", None):
        w, d = _gov(basis)
        kinds, opened = _fold(w, d, _revoke(f"rv_{basis}"))
        assert kinds == ["tenure.closed"], (basis, kinds)
        assert _hold(w, TARGET) is None, (basis, "the hold did not close")
        outcome[basis] = opened
    assert outcome["appointed"] == {(BAN_KIND, DUKE, VIA)}, outcome
    assert outcome["elected"] == outcome["annex"] == outcome[None] == set(), outcome
    assert len({frozenset(v) for v in outcome.values()}) > 1, "every provenance wrote the same thing"


# 2 -- PROVENANCE UNREADABLE MEANS REFUSE ----------------------------------------------------------------

def test_in31_an_unreadable_provenance_refuses_and_the_control_is_revoked():
    """A conferral off the roster, set past `Office.__post_init__` (`harness/probes.py`'s hand-mutation
    pattern). NO BUILT WORLD REACHES THIS: the constructor refuses such a value; this is the backstop."""
    w, d = _gov("purchased")
    act = _revoke("rv_bad")
    assert may_revoke(w, KING, VIA, w.offices[TARGET]), "fixture: the revoker's authority must hold"
    assert not _preds._req_revoke(w, act)
    assert EFFECTS["revoke"](w, act) is NO_CHANGE, "the effect's own backstop defaulted to a cost"
    kinds, opened = _fold(w, d, act)
    assert kinds == ["revoke.refused"] and opened == set(), (kinds, opened)
    assert _hold(w, TARGET) is not None and not restrained(w, DUKE, BAN_KIND)
    w.offices[TARGET].conferral = "appointed"                      # CONTROL
    kinds, opened = _fold(w, d, _revoke("rv_ok"))
    assert kinds == ["tenure.closed"] and opened == {(BAN_KIND, DUKE, VIA)}, (kinds, opened)


# 3 -- THE MAPPING IS TOTAL, REFUSED AT IMPORT ------------------------------------------------------------

def test_in31_the_disposal_mapping_is_total_and_names_restraints(monkeypatch):
    G.check_revocation_disposal()                                  # the shipped mapping passes
    assert set(G.REVOCATION_DISPOSAL) == set(G.CONFERRAL_BASES) | {None}
    with monkeypatch.context() as m:
        m.delitem(G.REVOCATION_DISPOSAL, "elected")
        with pytest.raises(Unspecified, match="disagree"):
            G.check_revocation_disposal()
    with monkeypatch.context() as m:
        m.setitem(G.REVOCATION_DISPOSAL, "purchased", None)
        with pytest.raises(Unspecified, match="disagree"):
            G.check_revocation_disposal()
    for kind in ("oblige", "detain"):       # `detain` is a restraint, but `_eff_revoke` opens only a ban
        with monkeypatch.context() as m:
            m.setitem(G.REVOCATION_DISPOSAL, "elected", kind)
            with pytest.raises(Unspecified, match="no restraint"):
                G.check_revocation_disposal()


# 4 -- THE WRITE GATE ------------------------------------------------------------------------------------

def _ban(w, owner, obj, n=0):
    return Tenure(f"ban_probe_{owner}_{obj}_{n}", owner, obj, BAN_KIND, w.tick)


def _write(w, actor, via, close=None, opens=()):
    """A bare gate write: close `close` (a Tenure) and open each of `opens`, as `actor` through `via`."""
    def apply():
        if close is not None:
            close.until = w.tick
        for t in opens:
            w.add_tenure(t)
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), apply, record_kind="Tenure",
                   fieldname="until", driver="Act", actor=actor, via=via)


@pytest.fixture
def bases(monkeypatch):
    """`{tenure id: basis}` -- the LAST verdict the gate's own `tenure_write_basis` gave each Tenure."""
    seen = {}
    real = G.tenure_write_basis

    def spy(w, t, *a, **k):
        b = real(w, t, *a, **k)
        seen[t.id] = b
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    return seen


def test_in31_the_gate_enforces_the_mapping_for_a_non_judging_seat(bases):
    # CONTROL: a closure of an appointed seat's hold plus ONE ban on `via`, in one write -- both `T-o`.
    w, _ = _gov("appointed")
    hold, ban = _hold(w, TARGET), _ban(w, DUKE, VIA)
    _write(w, KING, VIA, close=hold, opens=(ban,))
    assert (bases[hold.id], bases[ban.id]) == (T_O, T_O), bases
    assert restrained(w, DUKE, BAN_KIND)
    refusals = {
        "a ban with no revocation in the write": dict(conferral="appointed", close=False, objs=(VIA,)),
        "a ban beside an elected closure": dict(conferral="elected", close=True, objs=(VIA,)),
        "a ban on another seat": dict(conferral="appointed", close=True, objs=("off_mayor",)),
        "a second ban": dict(conferral="appointed", close=True, objs=(VIA, VIA)),
    }
    for name, c in refusals.items():
        w, _ = _gov(c["conferral"])
        hold = _hold(w, TARGET)
        opens = tuple(_ban(w, DUKE, o, n) for n, o in enumerate(c["objs"]))
        with pytest.raises(NotYours):
            _write(w, KING, VIA, close=hold if c["close"] else None, opens=opens)
        assert hold.live and not restrained(w, DUKE, BAN_KIND), (name, "the store was not put back")


def test_in31_a_judging_seat_admits_a_ban_by_its_own_authority(bases):
    """§2.5's ACCEPTED scope, pinned: where `via` judges the man (`may_determine`), the `determination`
    basis admits a ban beside an ELECTED closure -- the mapping is `_eff_revoke`'s alone there, because
    that seat could write the same ban by a `determine`. Flip this deliberately if a conjunct closes it."""
    w, _ = _gov_world()
    w.offices["off_reeve"].conferral = "elected"
    w.add_tenure(Tenure("t_reeve_mid", "p_mid", "off_reeve", "hold", 0))
    assert may_revoke(w, DUKE, TARGET, w.offices["off_reeve"]), "fixture: the duke may strip the reeve"
    assert may_determine(w, DUKE, TARGET, "p_mid"), "fixture: the duke's seat judges the reeve"
    hold, ban = _hold(w, "off_reeve"), _ban(w, "p_mid", TARGET)
    _write(w, DUKE, TARGET, close=hold, opens=(ban,))
    assert (bases[hold.id], bases[ban.id]) == (T_O, DETERMINATION), bases


# 5 -- THE BAN BITES THROUGH ITS EXISTING READERS --------------------------------------------------------

@pytest.mark.parametrize("basis,banned", [("appointed", True), ("elected", False)])
def test_in31_the_ban_bars_seating_and_service(basis, banned):
    w, d = _gov(basis)
    _fold(w, d, _revoke("rv_bite"))
    assert restrained(w, DUKE, BAN_KIND) is banned
    kinds, opened = _fold(w, d, Act(id="cf_bite", actor=KING, verb="confer", via=VIA,
                                    payload={"subject": "off_reeve", "office": "off_reeve", "to": DUKE}))
    if banned:
        assert kinds == ["confer.refused"] and opened == set(), (kinds, opened)
    else:
        assert "tenure.opened" in kinds and ("hold", DUKE, "off_reeve") in opened, (kinds, opened)
    serve = Act(id="ob_bite", actor=DUKE, verb="oblige", payload={"subject": "off_mayor"})
    assert _preds._req_oblige(w, serve) is (not banned)


# 6, 7 -- NO SELF-BAN; NO SECOND BAN ---------------------------------------------------------------------

def test_in31_a_self_revocation_closes_under_t_m_and_bans_nobody():
    w, d = _gov("appointed")
    w.add_tenure(Tenure("t_crown_high", DUKE, VIA, "hold", 0))     # the duke ALSO sits on the King's seat
    kinds, opened = _fold(w, d, _revoke("rv_self", actor=DUKE))
    assert kinds == ["tenure.closed"] and opened == set(), (kinds, opened)
    assert _hold(w, TARGET) is None and not restrained(w, DUKE, BAN_KIND)


def test_in31_a_man_already_banned_is_not_banned_twice():
    w, d = _gov("appointed")
    w.add_tenure(Tenure("t_prior_ban", DUKE, "off_mayor", BAN_KIND, 0))
    kinds, opened = _fold(w, d, _revoke("rv_twice"))
    assert kinds == ["tenure.closed"] and opened == set(), (kinds, opened)
    assert _hold(w, TARGET) is None
    assert sum(1 for t in w.tenures if t.kind == BAN_KIND and t.subject == DUKE and t.live) == 1


# 9 -- NOT A REVOCATION, NO COST -------------------------------------------------------------------------

def test_in31_a_release_a_displacing_confer_and_a_matured_term_cost_nothing():
    w, d = _gov("appointed")
    kinds, opened = _fold(w, d, Act(id="rl", actor=DUKE, verb="release", payload={"subject": TARGET}))
    assert _hold(w, TARGET) is None and not any(k == BAN_KIND for k, *_ in opened), (kinds, opened)
    w, d = _gov("appointed")
    kinds, opened = _fold(w, d, Act(id="cf_disp", actor=KING, verb="confer", via=VIA,
                                    payload={"subject": TARGET, "office": TARGET, "to": "p_mid"}))
    assert "tenure.closed" in kinds and ("hold", "p_mid", TARGET) in opened, (kinds, opened)
    assert not restrained(w, DUKE, BAN_KIND), "a displacing confer charged the incumbent (A1: nothing)"
    w, _, first = _seasons(term=1)                                   # `off_reeve`: an appointed seat
    assert w.offices["off_reeve"].conferral == "appointed" and first is not None and not first.live
    assert not any(t.kind == BAN_KIND for t in w.tenures), "a matured term charged its holder"


# 10 -- DERIVED OPENERS; KIND_VERB UNMOVED ----------------------------------------------------------------

def test_in31_ban_is_opened_by_determine_and_revoke_and_kind_verb_is_unmoved():
    assert set(V._derive_openers_from_effects()[BAN_KIND]) == {"determine", "revoke"}
    assert V.KIND_VERB.get("tenure.opened") == "confer", "a second `tenure.opened` emitter unpriced confer"
    assert V.VERB_TABLE["revoke"].emits == ("tenure.closed",)
    assert V.VERB_TABLE["revoke"].writes == ("Tenure.until", "Tenure.since")


# 11 -- THE EXIT, ON THE BUILT REALM ---------------------------------------------------------------------

_STEWARD, _VARFELL, _HAFEN = "off_lord_steward", "off_npc_052", "off_npc_050"


def _realm(place=True):
    """`build_realm(0)`, plus (by hand: Jordan 2026-10-12's *"a flag as to whether that office is in the
    holdings of the monarch"*) the King NPC-020 holding `duchy_varfell` and `duchy_hafenmark`, which makes
    their dukes revocable through the realm seat."""
    w = POP.build_realm(0)
    if place:
        for rung in ("duchy_varfell", "duchy_hafenmark"):
            w.add_tenure(Tenure(f"t_in31_{rung}", "p_npc_020", rung, "hold", 0))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _exit_run(place=True):
    """NPC-020 revokes, by hand-built acts through the fold: the appointed Lord Steward through
    `off_duke_valorsmark` (non-judging), the elected Duke of Varfell and the `None` Duchess of Hafenmark
    through `off_npc_020`. `{office: (kinds, opened)}`."""
    w, d = _realm(place)
    assert {o: w.offices[o].conferral for o in (_STEWARD, _VARFELL, _HAFEN)} == {
        _STEWARD: "appointed", _VARFELL: "elected", _HAFEN: None}
    out = {o: _fold(w, d, _revoke(f"rv_in31_{o}", "p_npc_020", o, via))
           for o, via in ((_STEWARD, "off_duke_valorsmark"), (_VARFELL, "off_npc_020"),
                          (_HAFEN, "off_npc_020"))}
    return w, out


def test_in31_the_exit_on_the_built_realm(monkeypatch):
    w, out = _exit_run()
    assert all(kinds == ["tenure.closed"] for kinds, _ in out.values()), out
    assert out[_STEWARD][1] == {(BAN_KIND, "p_npc_009", "off_duke_valorsmark")}, out
    assert out[_VARFELL][1] == out[_HAFEN][1] == set(), out
    assert restrained(w, "p_npc_009", BAN_KIND)
    assert not restrained(w, "p_npc_052", BAN_KIND) and not restrained(w, "p_npc_050", BAN_KIND)
    assert len({frozenset(o) for _, o in out.values()}) > 1, "one outcome whatever the provenance"
    # CONTROL 1: without the placement, the dukes are not revocable at all.
    _, bare = _exit_run(place=False)
    assert bare[_VARFELL][0] == ["revoke.refused"] and bare[_HAFEN][0] == ["revoke.refused"], bare
    # CONTROL 2, THE PLAN'S FALSIFIER OBSERVED LIVE: the mapping's one cost removed, in place.
    monkeypatch.setitem(G.REVOCATION_DISPOSAL, "appointed", None)
    w2, flat = _exit_run()
    assert len({frozenset(o) for _, o in flat.values()}) == 1 and not restrained(w2, "p_npc_009", BAN_KIND)
