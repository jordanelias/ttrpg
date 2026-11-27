"""IN-48 (H-108 (b)), B21b.25 -- DELEGATION ON LAYER 1'S ROUTE: a regent is the holder of a SECOND SEAT.

`architecture/meta/04_CODE_ARCHITECTURE.md:354`: *"delegation = `establish` -> `confer` -> `revoke`"*. No tenure kind, carrier field or gate basis
is added; the build is one `rosters.yaml: revocation_bases` value, `same_rung_same_faction`, and its rule (`state/gate.py::seated_on_the_same_rung`
in `REVOCATION_RULES`), which licenses ANY other seat on the regent seat's rung, of its faction, whose grant carries `revoke`.

THE EXIT (judged by `harness/corpus_run.py`'s attribution rule (`attempts`, over the act store), a same-world control beside it): a regent's act through the conferred seat executes while
the principal's own hold stays live and is the same object, and the same act refuses once the regency ends -- by its term (T-n), by the
principal's `revoke` (T-o under the new value) or by the regent's `release` (T-m). THE FALSIFIER (H-108's): a delegate's act admitted after the
delegation ended, or a seat exercised by a person with no live `hold` on it.

What each test observes that no other does:
  1. `..._on_the_shipped_bases`: the READING that makes the value necessary (neither shipped basis admits a same-rung revoke), with the governor
     seat, which the same instrument admits, as its control. Green before the roster edit.
  2. `test_a_principal_dismisses_his_regent_early`: the value's admission, the cost (IN-31's ban) and the rule's four refusals.
  3. `test_a_rung_sibling_granting_revoke_also_dismisses_the_regent`: who the rule licenses (a sibling, not the conferrer) and the symmetric case.
  4. `test_the_regent_acts_via_his_seat_and_refuses_after_term_dismissal_and_release`: the lifecycle on the gate-and-fold, the principal's hold kept.
  5. `test_a_seat_is_exercised_only_by_its_holder`: a person with no hold, and a detained holder, act through no seat.
  6. `test_the_regent_commands_what_his_seat_commands`: A-22's classes asked of the regent's seat, not the principal's.
  7. `test_an_outside_seat_installs_a_governor_through_a_sworn_holder`: the installer reading ((5) row 9), no lever over the man installed.
  8. (retired at the batch close: shape (a), a founded governor over a holding, duplicated `test_cr25_computed_establish.py`; nothing in it read the new value.)
  9. `test_in48_exit_seeded_season`: the EXIT on `build_realm(0)`.
"""
from __future__ import annotations

import pytest

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import WriteClass
from engine.season.harness import probes as P
from engine.season.harness.corpus_run import attempts
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.queries.world_q import BAN_KIND
from engine.season.state import gate as G
from engine.season.state.carriers import Act, Office, Rung, Tenure
from engine.season.state.gate import may_fill, may_revoke

from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_g3_not_yours import _gov_world, _hold
from .test_in31_revocation_cost import _edges, _fold, _revoke

pytestmark = pytest.mark.usefixtures("seat_at_success")   # `confer`/`revoke`/`establish` are drawn; these tests read the gate and the fold, not the draw

VALUE = "same_rung_same_faction"
KING, VIA, REGENT, REGENT_SEAT = "p_king", "off_crown", "p_mid", "off_regent"
_RUNG_ABOVE = "rung_above_same_faction"


def _regent_seat(w, revocation=VALUE, remit=("confer", "revoke"), oid=REGENT_SEAT, faction="Crown", rung="R"):
    w.offices[oid] = Office(oid, "Regent", rung, list(remit), faction=faction, conferral="appointed", revocation=revocation)


def _confer(w, d, key="cf_regent", oid=REGENT_SEAT, to=REGENT, actor=KING, via=VIA, term=None):
    payload = {"subject": oid, "to": to, **({"term": term} if term is not None else {})}
    return _fold(w, d, Act(id=key, actor=actor, verb="confer", payload=payload, via=via))


def _regency(revocation=VALUE, remit=("confer", "revoke"), term=None):
    """`_gov_world` (`p_king` holds `off_crown` at the top rung, Crown) plus `off_regent` at the same rung, Crown, conferred on `p_mid` by the King."""
    w, d = _gov_world()
    _regent_seat(w, revocation, remit)
    kinds, _ = _confer(w, d, term=term)
    assert kinds == ["tenure.opened"], kinds
    return w, d


def _vacant(w, oid):
    """A vacant `appointed` seat at the settlement `S`: what a regent (or the King) may fill, which is the act the tests judge."""
    w.offices[oid] = Office(oid, "Reeve", "S", ["issue"], faction="Crown", conferral="appointed", revocation=_RUNG_ABOVE)


def _act_via(w, d, key, actor, via, oid, to="p_low"):
    """`actor` fills the vacant seat `oid` THROUGH `via` -- the act a regent exists to do. Returns `(kinds, opened)`."""
    _vacant(w, oid)
    return _fold(w, d, Act(id=key, actor=actor, verb="confer", payload={"subject": oid, "to": to}, via=via))


# ======================================================================================
# 1 -- THE MEASUREMENT: THE SHIPPED BASES CANNOT END A SAME-RUNG SEAT
# ======================================================================================

def test_a_principal_cannot_revoke_a_same_rung_seat_on_the_shipped_bases():
    """§10 (2). The King on `off_crown` (top rung) cannot revoke `off_regent` (same rung) under either shipped basis or none, through
    `may_revoke` and through the fold (`revoke.unauthorized`, the hold still live); the regent cannot strip the principal either. CONTROL, so the
    instrument can observe an admission: a governor seat at the rung BELOW, conferred the same way, reads True under both bases (the King holding D),
    and the fold closes its hold."""
    for basis in (_RUNG_ABOVE, "rung_above_in_holdings", None):
        w, d = _regency(revocation=basis)
        w.add_tenure(Tenure("t_king_holds_R", KING, "R", "hold", 0))        # `in_holdings` true on R: still no rung above R
        assert not may_revoke(w, KING, VIA, w.offices[REGENT_SEAT]), basis
        kinds, _ = _fold(w, d, _revoke(f"rv_{basis}", KING, REGENT_SEAT, VIA))
        assert kinds == ["revoke.unauthorized"] and _hold(w, REGENT_SEAT).live, (basis, kinds)
        assert not may_revoke(w, REGENT, REGENT_SEAT, w.offices[VIA]), "the regent strips the principal"
    for basis in (_RUNG_ABOVE, "rung_above_in_holdings"):
        w, d = _gov_world()
        w.add_tenure(Tenure("t_king_holds_D", KING, "D", "hold", 0))
        w.offices["off_gov"] = Office("off_gov", "Governor", "D", ["issue"], faction="Crown", conferral="appointed", revocation=basis)
        assert _confer(w, d, oid="off_gov", to="p_mid")[0] == ["tenure.opened"]
        assert may_revoke(w, KING, VIA, w.offices["off_gov"]), f"control: {basis} admits the governor"
        assert _fold(w, d, _revoke(f"rv_gov_{basis}", KING, "off_gov", VIA))[0] == ["tenure.closed"]
        assert _hold(w, "off_gov") is None


# ======================================================================================
# 2 -- THE EARLY DISMISSAL: THE ONE VALUE AND ITS RULE
# ======================================================================================

def test_a_principal_dismisses_his_regent_early():
    """§10 (3). With the regent seat declaring `same_rung_same_faction` the King's `revoke` through `off_crown` closes the regent's hold alone (the
    King's hold is the same object, live) and, the seat being `appointed`, opens IN-31's ban on him objected on the dismissing seat. The rule
    refuses a seat on another rung, a same-rung seat of another faction, and the seat itself. (CONTROL, the same world with `null`: refused, test 1.)"""
    w, d = _regency()
    king_hold = _hold(w, VIA)
    assert may_revoke(w, KING, VIA, w.offices[REGENT_SEAT])
    kinds, opened = _fold(w, d, _revoke("rv_regent", KING, REGENT_SEAT, VIA))
    assert kinds == ["tenure.closed"] and _hold(w, REGENT_SEAT) is None
    assert opened == {(BAN_KIND, REGENT, VIA)}, opened
    assert _hold(w, VIA) is king_hold and king_hold.live, "the dismissal closed the principal's hold"
    # the refusals, each a seat declaring the value judged from the same King's seat
    w, _ = _regency()
    w.offices["off_reeve"].revocation = VALUE                              # a seat at S, a rung BELOW the King's
    _regent_seat(w, oid="off_foreign_regent", faction="Hafenmark")         # same rung, another faction
    assert not may_revoke(w, KING, VIA, w.offices["off_reeve"])
    assert not may_revoke(w, KING, VIA, w.offices["off_foreign_regent"])
    assert not may_revoke(w, REGENT, REGENT_SEAT, w.offices[REGENT_SEAT]), "a holder stripping his own seat is `release`, not this"
    assert G.seated_on_the_same_rung(w, w.offices[VIA], w.offices[REGENT_SEAT])          # control: the same function admits the lawful pair


def test_a_rung_sibling_granting_revoke_also_dismisses_the_regent():
    """§10 (3), the sibling reach, pinned so it is visible: a SECOND same-rung, same-faction seat whose grant carries `revoke` strips the regent
    though it conferred nothing; the same seat without `revoke` passes the rule and is refused at eligibility (the fold). SYMMETRIC: a principal's
    seat declaring the value is strippable by its regent, and one declaring `null` is not."""
    w, d = _regency()
    _regent_seat(w, revocation=None, remit=("revoke",), oid="off_chancellor")
    _regent_seat(w, revocation=None, remit=("issue",), oid="off_marshal")
    w.add_tenure(Tenure("t_chan", "p_other", "off_chancellor", "hold", 0))      # seated after the row exists: the grant is stamped at seating
    w.add_tenure(Tenure("t_mar", "p_low", "off_marshal", "hold", 0))
    assert may_revoke(w, "p_other", "off_chancellor", w.offices[REGENT_SEAT]) and may_revoke(w, "p_low", "off_marshal", w.offices[REGENT_SEAT])
    kinds, _ = _fold(w, d, _revoke("rv_marshal", "p_low", REGENT_SEAT, "off_marshal"))
    assert kinds != ["tenure.closed"] and _hold(w, REGENT_SEAT) is not None, "a seat without `revoke` in its grant dismissed him"
    kinds, _ = _fold(w, d, _revoke("rv_chan", "p_other", REGENT_SEAT, "off_chancellor"))
    assert kinds == ["tenure.closed"] and _hold(w, REGENT_SEAT) is None, kinds
    # symmetric: the regent's seat over the principal's
    w, d = _regency()
    assert not may_revoke(w, REGENT, REGENT_SEAT, w.offices[VIA])                       # the principal's seat declares `_RUNG_ABOVE`
    w.offices[VIA].revocation = VALUE
    assert may_revoke(w, REGENT, REGENT_SEAT, w.offices[VIA]), "the rule is about seats: a declaring principal is as strippable as the regent"
    w.offices[VIA].revocation = None
    assert not may_revoke(w, REGENT, REGENT_SEAT, w.offices[VIA])


# ======================================================================================
# 3 -- THE REGENT'S LIFE: ACTS THROUGH HIS SEAT, AND ENDS THREE WAYS
# ======================================================================================

def test_the_regent_acts_via_his_seat_and_refuses_after_term_dismissal_and_release():
    """§10 (6), on the governance world, folded through the real fold. While the regency stands the regent's `confer` through `off_regent` opens a
    hold, and conferring it left the principal's hold live and the SAME object; the principal's own act through his seat is admitted. When the
    regency ends -- the term at MATTER (T-n), the principal's `revoke` (T-o), the regent's `release` (T-m) -- the same act opens nothing, and the
    principal's act through his seat is still admitted."""
    for end in ("term", "revoke", "release"):
        w, d = _regency(term=1 if end == "term" else None)
        king_hold = _hold(w, VIA)
        regent_hold = _hold(w, REGENT_SEAT)
        assert king_hold.live and (regent_hold.term is not None) == (end == "term")
        assert _act_via(w, d, f"rg_in_{end}", REGENT, REGENT_SEAT, f"off_r1_{end}")[0] == ["tenure.opened"], "the regent's act through his seat"
        assert _act_via(w, d, f"pr_in_{end}", KING, VIA, f"off_p1_{end}", to="p_other")[0] == ["tenure.opened"], "control: the principal's act"
        assert _hold(w, VIA) is king_hold and king_hold.live, "conferring a regency closed or replaced the principal's hold"
        if end == "term":
            w.tick = regent_hold.term.matures_at
            d.matter(mint_token(w, WriteClass.MATTER), [])
        elif end == "revoke":
            assert _fold(w, d, _revoke("rv_end", KING, REGENT_SEAT, VIA))[0] == ["tenure.closed"]
        else:
            assert _fold(w, d, Act(id="rel_end", actor=REGENT, verb="release", payload={"subject": REGENT_SEAT}))[0] == ["tenure.closed"]
        assert not regent_hold.live and _hold(w, REGENT_SEAT) is None, end
        kinds, opened = _act_via(w, d, f"rg_out_{end}", REGENT, REGENT_SEAT, f"off_r2_{end}")
        assert kinds != ["tenure.opened"] and _hold(w, f"off_r2_{end}") is None, (end, kinds, "the regent's act admitted after the regency ended")
        assert _act_via(w, d, f"pr_out_{end}", KING, VIA, f"off_p2_{end}", to="p_other")[0] == ["tenure.opened"], f"control: principal after {end}"


def test_a_seat_is_exercised_only_by_its_holder():
    """H-108's falsifier on this route: a person with no live `hold` on `off_regent` (the principal himself, a stranger) exercises nothing through it,
    and a regent in custody acts through no seat (A-23, `detain` suspends and does not vacate), until the `detain` is closed. CONTROL: the holder's
    act is admitted."""
    w, d = _regency()
    for who in (KING, "p_other"):
        kinds, _ = _act_via(w, d, f"x_{who}", who, REGENT_SEAT, f"off_x_{who}")
        assert kinds != ["tenure.opened"] and _hold(w, f"off_x_{who}") is None, (who, kinds)
    assert _act_via(w, d, "holder", REGENT, REGENT_SEAT, "off_x_holder")[0] == ["tenure.opened"], "control: the holder"
    jail = Tenure("t_regent_detained", REGENT, VIA, "detain", 0)
    w.add_tenure(jail)
    assert not G._seat_grants(w, REGENT, REGENT_SEAT, "confer") and _hold(w, REGENT_SEAT).live, "custody must suspend, not vacate"
    kinds, _ = _act_via(w, d, "jailed", REGENT, REGENT_SEAT, "off_x_jailed")
    assert kinds != ["tenure.opened"] and _hold(w, "off_x_jailed") is None, kinds
    jail.until = w.tick
    assert _act_via(w, d, "freed", REGENT, REGENT_SEAT, "off_x_freed")[0] == ["tenure.opened"], "control: the act once the detain is closed"


# ======================================================================================
# 4 -- A-22: WHOM THE REGENT COMMANDS
# ======================================================================================

def test_the_regent_commands_what_his_seat_commands():
    """§10 (4). `commands` is asked of the SEAT `via` names: the duke the regent's seat may revoke (class ii) and the unseated man on the same ground
    (class iii) are commanded through either seat; a man living in a second realm and sworn only to the principal's seat is commanded through
    `off_crown` and NOT through `off_regent` (class i: each seat's establishment is its own), until he swears to it."""
    w, _ = _regency(revocation=_RUNG_ABOVE)
    w.rungs["R2"] = Rung("R2", "realm")
    from engine.season.boot.realm import place_person
    place_person(w, "p_far", "a far man", "R2")
    w.add_tenure(Tenure("t_far_oath", "p_far", VIA, "oblige", 0))
    c = lambda via, who: world_q.commands(w, KING if via == VIA else REGENT, via, who)
    assert c(VIA, "p_high") and c(REGENT_SEAT, "p_high"), "class (ii): structural, one rung of one faction"
    assert c(VIA, "p_low") and c(REGENT_SEAT, "p_low"), "class (iii): the same ground"
    assert c(VIA, "p_far") and not c(REGENT_SEAT, "p_far"), "class (i): sworn to the principal's seat only"
    w.add_tenure(Tenure("t_far_oath_regent", "p_far", REGENT_SEAT, "oblige", 0))
    assert c(REGENT_SEAT, "p_far"), "control: the same man once sworn to the regent's seat"


# ======================================================================================
# 5 -- WHAT THE ROUTE DOES NOT DO, AND WHAT IT DOES ALREADY
# ======================================================================================

def test_an_outside_seat_installs_a_governor_through_a_sworn_holder():
    """§10 (5) row 9, the installer reading. `off_duke2` (D2, another duchy) cannot fill a governor seat at `D`; once the Duke of D swears to
    `off_duke2` (the oblige clause) it can, the fold opens the hold and the Duke KEEPS his seat -- and the installer has no lever over the man
    installed (the governor seat declares `null`). That is a governor installed from outside, not a puppet."""
    w, d = _gov_world()
    w.offices["off_dgov"] = Office("off_dgov", "Governor", "D", ["issue"], faction="Crown", conferral="appointed", revocation=None)
    assert not may_fill(w, "p_other", "off_duke2", w.offices["off_dgov"])
    w.add_tenure(Tenure("t_duke_oath", "p_high", "off_duke2", "oblige", 0))
    assert may_fill(w, "p_other", "off_duke2", w.offices["off_dgov"]), "control: the oath brings D into the seat's purview"
    duke_hold = _hold(w, "off_duke")
    kinds, _ = _confer(w, d, oid="off_dgov", to="p_mid", actor="p_other", via="off_duke2")
    assert kinds == ["tenure.opened"] and _hold(w, "off_dgov").subject == "p_mid"
    assert _hold(w, "off_duke") is duke_hold and duke_hold.live, "the Duke lost his seat"
    assert not may_revoke(w, "p_other", "off_duke2", w.offices["off_dgov"]), "the installer has a lever over the governor"


# ======================================================================================
# 6 -- THE EXIT, IN A SEEDED SEASON
# ======================================================================================

_REALM_RUNG, _REALM_KING, _REALM_VIA = "r_valoria", "p_npc_020", "off_king"
_REALM_REGENT, _REALM_REGENT_SEAT = "p_npc_088", "off_realm_regent_t"


def _no_act(p, v, s, ask_budget):
    return []


def _executed(w, d, act_id):
    """`corpus_run.attempts`, `attribute`'s own rule over the ACT STORE (a refused act may never reach the fold set `attribute` reads): did the act of
    this id execute (its row's `emits` kind is in the log), and was it refused?"""
    rows = {a.id: (made, refused) for a, made, refused in attempts(w, w.tick)}
    assert act_id in rows, f"{act_id} was never attempted"
    made, refused = rows[act_id]
    return bool(made) and not refused


def _exit_world(place_regent=True, end="term"):
    """`build_realm(0)`, a regent seat placed at build (same rung and faction as `off_king`, declaring the value) and a vacant `appointed` seat the
    regent's act fills; one season; the King's hand-built `confer` of the regent seat (a `term` payload for the term arm). Returns `(w, d)`."""
    w = build_realm(0)
    if place_regent:
        w.offices[_REALM_REGENT_SEAT] = Office(_REALM_REGENT_SEAT, "Regent", _REALM_RUNG, ["confer", "revoke"], faction=w.offices[_REALM_VIA].faction,
                                               conferral="appointed", revocation=VALUE)
    d = SeasonDriver(w)
    d.season(_no_act, question=None)
    if place_regent:
        payload = {"subject": _REALM_REGENT_SEAT, "to": _REALM_REGENT, **({"term": 1} if end == "term" else {})}
        kinds, _ = _fold(w, d, Act(id="cf_exit", actor=_REALM_KING, verb="confer", payload=payload, via=_REALM_VIA))
        assert kinds == ["tenure.opened"], kinds
    return w, d


def _regent_fills(w, d, key):
    w.offices[f"off_clerk_{key}"] = Office(f"off_clerk_{key}", "Clerk", "terr_T1", ["issue"], faction=w.offices[_REALM_VIA].faction,
                                           conferral="appointed", revocation=None)
    _fold(w, d, Act(id=key, actor=_REALM_REGENT, verb="confer", payload={"subject": f"off_clerk_{key}", "to": "p_npc_087"}, via=_REALM_REGENT_SEAT))
    return _executed(w, d, key)


def test_in48_exit_seeded_season():
    """§10 (6) EXIT on `build_realm(0)`: the regent's act through the conferred seat executes (`attempts`) while the King's hold is live and the
    same object, and after each of three endings the same act is refused. CONTROL, the same world with nobody holding the regent seat: the act is
    not executed `via` the seat -- the FALSIFIER (the EXIT passing with the seat removed would mean the act was admitted on another ground)."""
    for end in ("term", "revoke", "release"):
        w, d = _exit_world(end=end)
        king_hold = next(t for t in w.tenures if t.kind == "hold" and t.object == _REALM_VIA and t.live)
        regent_hold = next(t for t in w.tenures if t.kind == "hold" and t.object == _REALM_REGENT_SEAT and t.live)
        assert _regent_fills(w, d, f"in_{end}"), f"{end}: the regent's act through his seat did not execute"
        assert king_hold.live and next(t for t in w.tenures if t.kind == "hold" and t.object == _REALM_VIA and t.live) is king_hold
        if end == "term":
            while regent_hold.live:
                d.season(_no_act, question=None)
        elif end == "revoke":
            assert _fold(w, d, _revoke("rv_exit", _REALM_KING, _REALM_REGENT_SEAT, _REALM_VIA))[0] == ["tenure.closed"]
        else:
            assert _fold(w, d, Act(id="rel_exit", actor=_REALM_REGENT, verb="release", payload={"subject": _REALM_REGENT_SEAT}))[0] == ["tenure.closed"]
        assert not regent_hold.live
        assert not _regent_fills(w, d, f"out_{end}"), f"{end}: the regent's act admitted after the regency ended"
        assert king_hold.live
    w, d = _exit_world(place_regent=False)
    w.offices[_REALM_REGENT_SEAT] = Office(_REALM_REGENT_SEAT, "Regent", _REALM_RUNG, ["confer", "revoke"], faction=w.offices[_REALM_VIA].faction,
                                           conferral="appointed", revocation=VALUE)
    assert not _regent_fills(w, d, "control"), "control: an act through a seat nobody holds was executed"
