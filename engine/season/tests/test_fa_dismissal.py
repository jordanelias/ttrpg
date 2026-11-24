"""B21.51 (`16_PESSIMIST_FA_A` edit 1): THE DUCHY OF VALORSMARK PASSES WITH THE THRONE.

The Crown's six council seats are strippable only through `off_duke_valorsmark` (`rung_above_same_faction`), and the King holds that
seat as a second hold. Before B21.51 the duchy had no `conferral` and no `successions` row, so a royal death left it vacant, the
heir's one `succeed` opened the throne alone, and every `revoke` of a council seat the new King made was refused. One home for
the lane's `strippable` helper: B21.52 and B21.53 add their arms here.
"""
from __future__ import annotations

from ..boot.realm import build_realm
from ..data.matrix import Step, WriteClass
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..state import gate as G
from ..state.carriers import Act
from .test_in61_heir_hears_vacancy import _holder

THRONE, TITLE, DUCHY, MARSHAL = "off_king", "off_heir", "off_duke_valorsmark", "off_royal_marshal"


def strippable(w) -> set:
    """Every `(via, seat)` such that whoever sits in `via` may close the live `hold` on `seat` (`state/gate.py::may_revoke`): the
    rule's own reading over the world, by seat, so a change of occupant leaves it where it was. `[ASSUMPTION: helper shape; the
    item creates it -- basis: the source's `pf1` was "grant-filtered", scratch not in the tree]`."""
    out = set()
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object in w.offices:
            for via in w.offices:
                who = _holder(w, via)
                if who and G.may_revoke(w, who, via, w.offices[t.object]):
                    out.add((via, t.object))
    return out


def _resolve(w, d, act):
    w.step = Step.RESOLVE
    w.frozen = False
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    return [e.kind for e in out]


def test_heir_holds_both_titles_after_one_succeed():
    """G2. The King dies holding the throne and the duchy; the heir's ONE `succeed` on the throne (drawn, as shipped) opens both, and the
    claim's Failure band opens neither. `strippable` after the claim equals its value at build (the duchy's six strips are back). The new
    King's `revoke` of the Marshal through the duchy is drawn: never refused at any seed, and it closes the hold at some. FALSIFIER: the
    duchy left vacant (`strippable` loses six, `revoke.refused`). CONTROL: the throne's own claim is `off_king`'s row, unchanged."""
    claimed = revoked = resisted = 0
    for seed in range(8):
        w = build_realm(seed)
        d = SeasonDriver(w)
        king, heir, marshal = _holder(w, THRONE), _holder(w, TITLE), _holder(w, MARSHAL)
        assert king and heir and marshal and _holder(w, DUCHY) == king, "fixture: the King no longer holds both seats"
        at_build = strippable(w)
        assert {(DUCHY, MARSHAL)} <= at_build
        w.step = Step.MATTER
        w._emitted_by_write = []
        _die(w, mint_token(w, WriteClass.MATTER), king)
        assert _holder(w, THRONE) is None and _holder(w, DUCHY) is None
        kinds = _resolve(w, d, Act(id=f"fa_diss_claim_{seed}", actor=heir, verb="succeed", payload={"subject": THRONE}))
        if "succession.claimed" not in kinds:           # a Failed claim (the draw) opens neither seat
            assert _holder(w, THRONE) is None and _holder(w, DUCHY) is None, kinds
            continue
        claimed += 1
        assert _holder(w, THRONE) == heir and _holder(w, DUCHY) == heir, "one claim did not open both seats"
        assert strippable(w) == at_build
        for attempt in range(6):                        # a Failed revoke writes nothing, so the same strip may be tried again
            kinds = _resolve(w, d, Act(id=f"fa_diss_revoke_{seed}_{attempt}", actor=heir, verb="revoke", via=DUCHY,
                                       payload={"subject": MARSHAL}))
            assert "revoke.refused" not in kinds, kinds
            if kinds == ["tenure.closed"]:
                revoked += 1
                assert _holder(w, MARSHAL) is None
                break
            assert kinds == ["revocation.resisted"] and _holder(w, MARSHAL) == marshal, kinds
            resisted += 1
    assert claimed >= 3, claimed
    assert revoked >= 1 and resisted >= 1, (claimed, revoked, resisted)
