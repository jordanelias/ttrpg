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
from ..queries.world_q import commands
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


CROWN_SIX = {"off_guard_captain", "off_lord_steward", "off_lord_treasurer", "off_parliamentary_clerk", "off_royal_marshal", "off_spymaster"}
COUNCIL_SIX = {"off_legal_advisor_hm", "off_military_commander_hm", "off_commune_rep_hm",
               "off_senior_jarl_west", "off_skald_chief", "off_military_jarl"}
DUKES = {"off_duchess_hafenmark", "off_duke_varfell"}


def test_strippable_set_at_build_includes_six_council_seats():
    """G1 (B21.52). At build `strippable` is a superset of the Crown's six (through the duchy) and adds the six ducal council seats, each
    through its own duke's seat (`rung_above_same_faction`: the duke's seat is on the rung directly above the seat's territory anchor, in
    the seat's faction). FALSIFIER: a council whose body resolved to a faction other than its duke's. CONTROL: the Guild Comptroller
    (faction `Guilds`) is strippable by nobody, and `off_king` strips none of the twelve (the Crown's rule is unchanged)."""
    s = strippable(build_realm(0))
    assert {(DUCHY, seat) for seat in CROWN_SIX} <= s
    assert COUNCIL_SIX <= {seat for via, seat in s if via in DUKES}, COUNCIL_SIX - {seat for via, seat in s if via in DUKES}
    assert {via for via, seat in s if seat in COUNCIL_SIX} <= DUKES, "a council seat is strippable through a seat that is not its duke's"
    assert "off_guild_comptroller" not in {seat for _, seat in s}
    assert not any(via == THRONE and seat in CROWN_SIX | COUNCIL_SIX for via, seat in s)


def test_a_duke_commands_his_council_and_the_guild_comptroller_is_not_his():
    """B21.20's `commands` (ii) reads `may_revoke`, so anchoring the council one rung below the duchy puts the three Varfell holders (NPC-073,
    074, 082) and Hafenmark's three under their duke's `issue`. CONTROL: the Comptroller (a Guilds seat) is not the Duchess's man."""
    w = build_realm(0)
    for duke, seats in (("off_duke_varfell", ("off_senior_jarl_west", "off_skald_chief", "off_military_jarl")),
                        ("off_duchess_hafenmark", ("off_legal_advisor_hm", "off_military_commander_hm", "off_commune_rep_hm"))):
        for seat in seats:
            assert commands(w, _holder(w, duke), duke, _holder(w, seat)), (duke, seat)
    assert not commands(w, _holder(w, "off_duchess_hafenmark"), "off_duchess_hafenmark", _holder(w, "off_guild_comptroller"))


def _banned(w, who) -> bool:
    return any(t.kind == "ban" and t.subject == who and t.object == DUCHY and t.live for t in w.tenures)


def _dismissed(w, d, king, marshal, tag) -> bool:
    """The King's `revoke` of the Marshal through the duchy, tried until it lands (a Failure writes nothing); True where it left the ban
    (a Partial revocation unseats him without the disposal)."""
    for attempt in range(6):
        if "tenure.closed" in _resolve(w, d, Act(id=f"{tag}_rv_{attempt}", actor=king, verb="revoke", via=DUCHY,
                                                payload={"subject": MARSHAL})):
            break
    return _banned(w, marshal)


def test_dismiss_then_pardon_through_the_ducal_seat():
    """G3 (B21.53). The King dismisses the Marshal through `off_duke_valorsmark`, which opens the permanent ban on that seat, and the
    reappointment through the duchy is refused while it stands. The King then `pardon`s him through the SAME seat (undrawn until
    `14_VERBS_BINDING_B`): `ban.ended`, and the reappointment opens (a `confer` is drawn, so tried until it lands). FALSIFIER: the duchy
    without `determine` on its grant (the bench asks the grant and the object, not more): `pardon.refused` at every seed, the ban stands.
    Read as a count over seeds."""
    checked = pardoned = reappointed = 0
    for seed in range(8):
        w = build_realm(seed)
        d = SeasonDriver(w)
        king, marshal = _holder(w, THRONE), _holder(w, MARSHAL)
        if not _dismissed(w, d, king, marshal, f"fa_pardon_{seed}"):    # a Partial revocation (no ban) or no landing: nothing to pardon
            continue
        checked += 1
        assert _holder(w, MARSHAL) is None
        for attempt in range(6):                        # the ban is read in the effect, after the draw: a Failure is "resisted", not "refused"
            refused = _resolve(w, d, Act(id=f"fa_pardon_cf0_{seed}_{attempt}", actor=king, verb="confer", via=DUCHY,
                                         payload={"subject": MARSHAL, "office": MARSHAL, "to": marshal}))
            if refused != ["appointment.resisted"]:
                break
        assert refused == ["confer.refused"] and _holder(w, MARSHAL) is None, refused    # the ban bars the reappointment
        kinds = _resolve(w, d, Act(id=f"fa_pardon_{seed}", actor=king, verb="pardon", via=DUCHY, payload={"subject": marshal}))
        assert kinds == ["ban.ended"], kinds
        pardoned += 1
        assert not _banned(w, marshal)
        for attempt in range(6):
            kinds = _resolve(w, d, Act(id=f"fa_pardon_cf_{seed}_{attempt}", actor=king, verb="confer", via=DUCHY,
                                       payload={"subject": MARSHAL, "office": MARSHAL, "to": marshal}))
            assert "confer.refused" not in kinds, kinds
            if "tenure.opened" in kinds:
                assert _holder(w, MARSHAL) == marshal
                reappointed += 1
                break
    assert checked >= 3 and pardoned == checked and reappointed >= 1, (checked, pardoned, reappointed)


def test_pardon_through_off_king_still_refused():
    """G3's control (B21.53). A ban stands on the revoking seat; `pardon` through `off_king`, which is not the ban's object, closes nothing
    at any seed: the bench asks the grant AND the object. The ban stands."""
    checked = 0
    for seed in range(8):
        w = build_realm(seed)
        d = SeasonDriver(w)
        king, marshal = _holder(w, THRONE), _holder(w, MARSHAL)
        if not _dismissed(w, d, king, marshal, f"fa_pk_{seed}"):
            continue
        checked += 1
        assert _resolve(w, d, Act(id=f"fa_pk_{seed}", actor=king, verb="pardon", via=THRONE, payload={"subject": marshal})) \
            == ["pardon.refused"]
        assert _banned(w, marshal)
    assert checked >= 3, checked
