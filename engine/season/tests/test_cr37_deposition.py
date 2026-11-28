"""v11 CR-37 -- B21c.05: THE THRONE MAY BE STRIPPED BY THE HOLY SEE'S CONCURRENCE WITH A CARRIED MOTION (M8, A2-14, the deposition half of
§1b-3; `depose` is closed, answered by `revoke`).

A seat whose `revocation:` is `joint_concurrence` (`rosters.yaml: revocation_bases`; `off_king`'s row) is stripped by a `revoke` through a
seat of a body named in `rosters.yaml: concurring_bodies` (the Holy See) -- the gate's rule (`state/gate.py::REVOCATION_RULES`) -- whose
actor HOLDS a live `resolution` naming the seat (`terms`) and its current holder (`to`), made by a determination through a seat other than
the revoking `via` (the record conjunct, `_req_revoke` and again `_eff_revoke`, read by `loop/predicates.py::confirming_resolutions`, the
one reader CR-36 landed; the gate reads no Record, K-52). The `revoke` is drawn on its contested row as B21.14 made it: no second
resolution and no branch on the basis in the effect. No ban opens (`REVOCATION_DISPOSAL["inheritance"]` is None); the throne falls vacant
and goes by IN-61's claim. REACH 0 in the realm: no computed docket item names an arrangement (H-80) and no computed `give` delivers a
resolution (H-229), so every route here is hand-built.

THE WORLD is `test_cr36_nomination.py`'s court (`probes.tiny_world`: R > D > S > Hh) with these seats, `off_king`, `off_duke_valorsmark` and
`off_confessor` taking `conferral`, `revocation` and `body` from their SHIPPED `offices.yaml` rows (`data/rosters.py::OFFICES_SEATS`), so the
data row is what is exercised:
  * `off_king` (the throne, held by p_king) and `off_duke_valorsmark` (his duchy, held by him too);
  * `off_heir` (the title `rosters.yaml: successions` names for the throne, held by p_mid);
  * `off_regent` (Crown, remit `determine`, held by p_high): the motion's maker, a seat of the interim bench (CR-38);
  * `off_confessor` (body Holy See, held by p_other) given the realm's reach so it may sit a motion itself (arm (v));
  * `off_chancellor` (Crown, remit `revoke`, held by p_low): a revoking seat of no concurring body (arm (iii)).
The motion is a petition naming `off_king`, docketed under `parliamentary_debate` with the King as its matter. The hand-built `give` (H-229's
residue) moves the resolution's `hold` by hand: the delivery is not under test.
"""
from __future__ import annotations

import pytest

from ..data.rosters import OFFICES_SEATS
from ..loop.effects_information import _docket_item
from ..state.carriers import Act, Record, Tenure
from ._gov_fixtures import give_by_hand as _give_by_hand, holders as _holders, seat, vacate
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_u7_remit import JUDGE, OPENS, _fold, _kinds, _world

CROWN = "Valorsmark"
THRONE, DUCHY, TITLE, CONFESSOR = "off_king", "off_duke_valorsmark", "off_heir", "off_confessor"
REGENT_SEAT, CHANCELLOR = "off_regent", "off_chancellor"
KING, HEIR, REGENT, HOLY, OTHER = "p_king", "p_mid", "p_high", "p_other", "p_low"
PETITION, ROW = "pet_deposition", "parliamentary_debate"
SEEDS = range(40)
STRIPS = ("Overwhelming", "Success", "Partial")


def _shipped(sid):
    row, = [r for r in OFFICES_SEATS if r["id"] == sid]
    return row


def _shipped_terms(sid):
    """The seat's `conferral`, `revocation` and `body` as its shipped `offices.yaml` row declares them."""
    row = _shipped(sid)
    return {"conferral": row.get("conferral"), "revocation": row.get("revocation"), "body": row.get("body")}


def _court(**fx):
    w, d = _world(**fx)
    vacate(w, "off_duke")
    seat(w, THRONE, "King", "R", ["issue", "determine", "confer", "revoke", "convene"], KING, faction=CROWN, **_shipped_terms(THRONE))
    seat(w, DUCHY, "Duke", "D", ["issue", "determine", "confer", "revoke", "convene"], KING, faction=CROWN, **_shipped_terms(DUCHY))
    seat(w, TITLE, "Heir", "R", ["issue"], HEIR, faction=CROWN)
    w.offices[TITLE].conferral = "appointed"
    seat(w, REGENT_SEAT, "Dicastery", "R", ["issue", "determine"], REGENT, faction=CROWN)
    seat(w, CONFESSOR, "Confessor", "R", ["issue", "determine", "confer", "revoke", "convene"], HOLY, **_shipped_terms(CONFESSOR))
    seat(w, CHANCELLOR, "Chancellor", "R", ["issue", "revoke"], OTHER, faction=CROWN)
    w.records[PETITION] = Record(PETITION, "R", "petition", subject_matter={"terms": THRONE, "to": None, "from": "R"})
    w.add_tenure(Tenure("t_pet_deposition", OTHER, PETITION, "hold", since=0))
    w.docket.append(_docket_item(KING, ROW, PETITION))
    return w, d


def _determine(key, actor=REGENT, via=REGENT_SEAT):
    return Act(id=key, actor=actor, verb="determine", via=via, payload={"subject": KING})


def _revoke(key, actor=HOLY, via=CONFESSOR, seat=THRONE):
    return Act(id=key, actor=actor, verb="revoke", via=via, payload={"office": seat})


def _resolutions(w):
    return [rid for rid, r in w.records.items() if r.kind == "resolution"]


def _bans_on(w, who):
    return [t for t in w.tenures if t.kind == "ban" and t.live and t.subject == who]


def _opening(actor=REGENT, via=REGENT_SEAT, **fx):
    """The first act id at which the motion carries, over act ids until the draw opens (shipped draws unless `fx`)."""
    for s in SEEDS:
        w, d = _court(**fx)
        if _fold(w, d, _determine(f"mo{s}", actor, via))[0].degree in OPENS:
            return f"mo{s}"
    raise AssertionError("no act id carried the motion")


def _carried(actor=REGENT, via=REGENT_SEAT, key=None, **fx):
    """A court whose motion carried at act id `key` (else `_opening`'s), the resolution in the motion-maker's hand. The world is rebuilt."""
    w, d = _court(**fx)
    out = _fold(w, d, _determine(key or _opening(actor, via, **fx), actor, via))
    assert out[0].degree in OPENS, _kinds(out)
    rid, = _resolutions(w)
    return w, d, rid


# --- THE ROUTE EXECUTES, READ BY BAND ---------------------------------------------------------------------------------------------------

def test_carried_motion_and_concurrence_strip_the_throne_by_band():
    """EXIT: a carried motion (a `resolution` naming `off_king` and the King, made through the Regent's seat, held by the Confessor after a
    hand-built `give`) and the Confessor's `revoke` through his seat, drawn over forty act ids at the shipped draws: at Overwhelming, Success
    or Partial the throne-hold closes, no ban opens, the King's `off_duke_valorsmark` hold stays live and the heir's `succeed` is admitted
    (IN-61); at Failure `revocation.resisted` and the King keeps the throne. Never refused: the refusal arms are below."""
    checked, bands, claimed = 0, {}, 0
    key = _opening()
    for s in SEEDS:
        w, d, rid = _carried(key=key)      # the same carried motion each time (the first act id that opens); the world is rebuilt, never copied
        assert w.records[rid].subject_matter == {"terms": THRONE, "to": [KING]}
        _give_by_hand(w, rid, HOLY)
        out = _fold(w, d, _revoke(f"rv{s}"))
        kinds, band = _kinds(out), out[0].degree
        assert not any(k.startswith("revoke.") for k in kinds), (s, kinds)
        checked += 1
        bands[band] = bands.get(band, 0) + 1
        assert _holders(w, DUCHY) == [KING], (s, band)
        assert _bans_on(w, KING) == [], (s, band)
        if band in STRIPS:
            assert kinds == ["tenure.closed"] and _holders(w, THRONE) == [], (s, kinds)
            got = _kinds(_fold(w, d, Act(id=f"sc{s}", actor=HEIR, verb="succeed", payload={"subject": THRONE})))
            assert "succession.refused" not in got, (s, got)
            if _holders(w, THRONE) == [HEIR]:
                claimed += 1
        else:
            assert band == "Failure" and kinds == ["revocation.resisted"] and _holders(w, THRONE) == [KING], (s, band, kinds)
    assert checked >= 40
    assert sum(bands.get(b, 0) for b in STRIPS) >= 1 and claimed >= 1, (bands, claimed)


# --- THE REFUSALS: AT THE PRECONDITION OR THE GATE, NEVER A DRAW ------------------------------------------------------------------------

def _arm(arm):
    """A carried motion (a strong judge) delivered to the revoker, then one change per arm. Returns the world, its driver and the act."""
    w, d, rid = _carried(**JUDGE)
    actor, via = HOLY, CONFESSOR
    if arm == "ii_none_held":
        _give_by_hand(w, rid, HEIR)
    elif arm == "iii_not_a_concurring_body":
        _give_by_hand(w, rid, OTHER)
        actor, via = OTHER, CHANCELLOR
    else:
        _give_by_hand(w, rid, HOLY)
    if arm == "iv_former_king":
        assert "release.refused" not in _kinds(_fold(w, d, Act(id="rel", actor=KING, verb="release", payload={"subject": THRONE})))
        assert _holders(w, THRONE) == []
        _fold(w, d, Act(id="claim", actor=HEIR, verb="succeed", payload={"subject": THRONE}))
        assert _holders(w, THRONE) == [HEIR], "fixture: the heir did not take the throne"
    return w, d, _revoke(f"r_{arm}", actor, via)


@pytest.mark.usefixtures("seat_at_success")
@pytest.mark.parametrize("arm,kind", [("ii_none_held", "revoke.no_resolution"),
                                      ("iii_not_a_concurring_body", "revoke.unauthorized"),
                                      ("iv_former_king", "revoke.no_resolution")])
def test_deposition_refusals(arm, kind):
    """(ii) the Confessor holds no resolution (it went elsewhere) -> refused at the record conjunct; (iii) the resolution held by a revoker
    whose seat is of no `concurring_bodies` body -> refused at the gate's rule (`authority`); (iv) the resolution names a former King (the
    throne passed to the heir) -> refused at the holder clause. The throne's holder is unchanged in each. CONTROL (one clause away): the
    `control` arm -- the Regent's resolution in the Confessor's hand against the King who holds the throne -- strips it."""
    w, d, act = _arm("control")
    assert _kinds(_fold(w, d, act)) == ["tenure.closed"] and _holders(w, THRONE) == []
    w, d, act = _arm(arm)
    before = _holders(w, THRONE)
    assert _kinds(_fold(w, d, act)) == [kind], arm
    assert _holders(w, THRONE) == before and before, arm


@pytest.mark.usefixtures("seat_at_success")
def test_a_planted_single_signer_is_refused():
    """M8's gate arm, arm (v): ONE BODY CANNOT BOTH CARRY THE MOTION AND CONCUR. A resolution minted through `off_confessor` itself, held by
    the Confessor, and his `revoke` through the same seat -> refused (the two-seat clause). And a resolution PLANTED by hand (no logged act
    made it, so no creating seat is readable) -> refused. The King keeps the throne in both."""
    w, d, rid = _carried(actor=HOLY, via=CONFESSOR, **JUDGE)
    assert w.records[rid].subject_matter == {"terms": THRONE, "to": [KING]}
    assert _kinds(_fold(w, d, _revoke("r_single"))) == ["revoke.no_resolution"]
    assert _holders(w, THRONE) == [KING]
    w, d = _court(**JUDGE)
    w.records["res_planted"] = Record("res_planted", "R", "resolution", subject_matter={"terms": THRONE, "to": [KING]})
    w.add_tenure(Tenure("t_planted", HOLY, "res_planted", "hold", since=0))
    assert _kinds(_fold(w, d, _revoke("r_planted"))) == ["revoke.no_resolution"]
    assert _holders(w, THRONE) == [KING]


def test_the_concurring_seat_does_not_command_the_king():
    """A-22 class (ii) IS DISMISSAL WITHOUT A MOTION: the Confessor's seat may close the throne-hold at the gate (`may_revoke`, the write
    basis, kept) but strips it only with a carried motion (`CONCURRED_BASES`), so he does not command the King (`world_q.commands`, through
    `state/gate.py::may_dismiss`). CONTROL (one basis away): a seat on a non-concurred basis (`same_rung_same_faction` on the heir's title)
    is commanded by the seat that may revoke it."""
    from ..queries import world_q
    from ..state.gate import may_revoke
    w, _ = _court()
    assert may_revoke(w, HOLY, CONFESSOR, w.offices[THRONE])
    assert not world_q.commands(w, HOLY, CONFESSOR, KING)
    w.offices[TITLE].revocation = "same_rung_same_faction"
    assert world_q.commands(w, KING, THRONE, HEIR)


@pytest.mark.usefixtures("seat_at_success")
def test_no_route_reaches_the_confessor():
    """A-36: THE CONFESSOR LEAVES ONLY BY DEATH OR RESIGNATION. The shipped `off_confessor` row does not declare `joint_concurrence`; a
    carried motion naming `off_confessor` and its holder, held by a second Holy See seat, and that seat's `revoke` of the Confessor's seat
    -> refused at the seat's basis (`authority`), and the Confessor keeps his seat."""
    assert _shipped(CONFESSOR)["revocation"] != "joint_concurrence"
    assert _shipped(THRONE)["revocation"] == "joint_concurrence"
    w, d = _court(**JUDGE)
    seat(w, "off_see_vicar", "Vicar of the See", "R", ["issue", "revoke"], OTHER, body=w.offices[CONFESSOR].body)
    w.records["pet_conf"] = Record("pet_conf", "R", "petition", subject_matter={"terms": CONFESSOR, "to": None, "from": "R"})
    w.add_tenure(Tenure("t_pet_conf", OTHER, "pet_conf", "hold", since=0))
    w.docket[:] = [_docket_item(HOLY, ROW, "pet_conf")]
    out = _fold(w, d, Act(id="mo_conf", actor=REGENT, verb="determine", via=REGENT_SEAT, payload={"subject": HOLY}))
    assert out[0].degree in OPENS, _kinds(out)
    rid, = _resolutions(w)
    assert w.records[rid].subject_matter == {"terms": CONFESSOR, "to": [HOLY]}
    _give_by_hand(w, rid, OTHER)
    assert _kinds(_fold(w, d, _revoke("r_conf", OTHER, "off_see_vicar", CONFESSOR))) == ["revoke.unauthorized"]
    assert _holders(w, CONFESSOR) == [HOLY]
