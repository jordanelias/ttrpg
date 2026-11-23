"""B21.13 (`14_VERBS_BINDING_C` commit C2 with `06_FA_decree_binds` edit 5): `revoke` READS ITS SEAT FROM `subject`.

A COMPUTED `revoke` names its seat on `subject` (the classed Office referent of the question it was formed from) and
carries no `office` key; `confer` already read the seat that way (`loop/predicates.py::office_named_by`), `revoke` did not,
so every computed `revoke` was refused at its first clause. One function per gate of BIND_C's C2..C4 lives here; B21.14
adds C3's. The hand-built world is `test_g3_not_yours._gov_world` (`p_king` on `off_crown`, above `off_duke`, held by `p_high`).

B21.14 (BIND_C commit C3): `confer`, `revoke` and `succeed` are DRAWN -- each contests the prize `a seat` on the social roll,
opposed by the live holder of the seat the act names (`rosters.yaml`'s `a seat` row, `opposed_by: holder`; `loop/sides.py`), and
its band decides what it writes. `test_c3_confer_revoke_succeed_band_on_a_hand_built_world` folds one of each, through the real
driver, on a world with one vacancy (`off_reeve`), one holder to revoke (`p_high` on `off_duke`) and one vacant inherited seat
(`off_king`, whose `successions` title `off_heir` `p_mid` holds), across 40 world seeds. FALSIFIER: the roll pinned to Success, the
band count collapses to one (read once, not kept). CONTROL: `rank_step` 0 and `provisional_term` at control (a Partial seat opens
untermed, as at Success); `test_in31_revocation_cost.py`, the ruled disposal at O/S, green.
"""
from __future__ import annotations

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.season.data.matrix import Step, WriteClass
from engine.season.decision.options import opening_set
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.seam import Resolution
from engine.season.seam.wrappers.sigma import HeardAct, audience_of
from engine.season.state.carriers import Act, Office, Tenure, View

from .test_g3_not_yours import _gov_world, _hold

KING, VIA, TARGET = "p_king", "off_crown", "off_duke"


def _fold(w, d, act: Act) -> list:
    """Fold ONE act at Success through the real `_fold` (its `_admits`, the gate, the effect); the event kinds. B21.14: `revoke` is
    DRAWN, and this test reads its admission and effect, not its draw (B21.09's precedent, `test_cr25_computed_establish._act`); the
    draw is `test_c3_confer_revoke_succeed_band_on_a_hand_built_world`'s, and the roll is reached below through the real `resolve`."""
    w.step = Step.RESOLVE
    w.acts.append(act)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))
    w.log.extend(out)
    return [e.kind for e in out]


def test_c2_a_computed_revoke_reaches_the_roll():
    """A `revoke` whose `subject` names the seat and whose payload carries no `office` is admitted and its effect closes
    the holder's `hold`. CONTROL: a hand-built act carrying `payload['office']` reads the same seat (`office` wins), and
    one naming no seat on either key is still refused."""
    w0, d0 = _gov_world()                       # B21.14: the computed act reaches the roll -- its Event carries a band
    band, kinds, _ = _resolved(w0, d0, Act(id="rv_roll", actor=KING, verb="revoke", payload={"subject": TARGET}, via=VIA))
    assert band is not None and kinds in (["tenure.closed"], ["revocation.resisted"]), (band, kinds)
    w, d = _gov_world()
    assert _hold(w, TARGET) is not None, "fixture: the duke holds his seat"
    computed = Act(id="rv_computed", actor=KING, verb="revoke", payload={"subject": TARGET}, via=VIA)
    assert "office" not in computed.payload
    assert _preds._req_revoke(w, computed), "a computed revoke is refused at its precondition"
    assert _fold(w, d, computed) == ["tenure.closed"]
    assert _hold(w, TARGET) is None, "the effect did not close the holder's hold"

    w2, d2 = _gov_world()
    handbuilt = Act(id="rv_hand", actor=KING, verb="revoke", payload={"office": TARGET}, via=VIA)
    assert _preds._req_revoke(w2, handbuilt)
    assert _fold(w2, d2, handbuilt) == ["tenure.closed"] and _hold(w2, TARGET) is None

    w3, d3 = _gov_world()                       # `office` wins where both are present
    both = Act(id="rv_both", actor=KING, verb="revoke", payload={"office": TARGET, "subject": "off_nowhere"}, via=VIA)
    assert _preds.office_named_by(both) == TARGET
    assert _fold(w3, d3, both) == ["tenure.closed"] and _hold(w3, TARGET) is None

    w4, _ = _gov_world()
    assert not _preds._req_revoke(w4, Act(id="rv_none", actor=KING, verb="revoke", payload={}, via=VIA))


THRONE, TITLE, HEIR, CONFEREE, VACANCY = "off_king", "off_heir", "p_mid", "p_low", "off_reeve"
PRESENCE = "attr.social.charisma"           # the three rows' one governing attribute (`verb_table.yaml`)


def _c3_world(seed: int):
    """`_gov_world` at world seed `seed`, plus the vacant inherited seat: `off_king` (`inheritance`, the `successions` row's seat),
    unheld, and its title `off_heir`, held by `p_mid`. The king and the heir hold Presence 3, so each band carries several of the
    40 draws."""
    w, d = _gov_world()
    w.world_seed = seed
    w.offices[THRONE] = Office(THRONE, "King", "R", ["confer", "revoke"], faction="Crown", conferral="inheritance")
    w.offices[TITLE] = Office(TITLE, "Heir", "R", [], faction="Crown", conferral="appointed",
                              revocation="rung_above_same_faction")
    w.add_tenure(Tenure("t_c3_heir", HEIR, TITLE, "hold", 0))
    for p in (KING, HEIR):
        w.persons[p].attributes = {**(w.persons[p].attributes or {}), PRESENCE: 3}
    return w, d


def _resolved(w, d, act: Act):
    """Fold ONE act through the shipped `SeasonDriver.resolve` (the seam's draw decides the band); `(band, kinds, events)`."""
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out[0].degree, [e.kind for e in out], out


def _heard(w, d, events, who) -> bool:
    """WITNESS the Events (A-81: a Failure band's durable write is the claim it deposits); does every person in `who` hold one?"""
    d.witness(mint_token(w, WriteClass.INTERIOR), list(events))
    kind = events[0].kind
    return all(any(c.predicate == kind for c in w.persons[p].ledger) for p in who)


def _forms(w, pid, verb) -> list:
    """The seats `pid` forms `verb` on, over the questions the world hands him (`questions_for`'s classed referents)."""
    p = w.persons[pid]
    return sorted({c.subject for q in world_q.questions_for(w, p)
                   for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures) if c.verb == verb})


def test_c3_confer_revoke_succeed_band_on_a_hand_built_world():
    bands: dict = {"confer": {}, "revoke": {}, "succeed": {}}
    checked = 0
    for seed in range(40):
        w, d = _c3_world(seed)
        body = set(audience_of(w, HeardAct(KING, VIA, world_q.place_of(w, KING)), "seat_body"))
        assert body, "fixture: the conferring seat's body hears nobody"

        # CONFER: the vacancy, on the conferee -- nobody holds it, so nobody stands opposite
        band, kinds, out = _resolved(w, d, Act(id=f"c3_confer_{seed}", actor=KING, verb="confer", via=VIA,
                                               payload={"subject": VACANCY, "to": CONFEREE}))
        bands["confer"][band] = bands["confer"].get(band, 0) + 1
        if band == "Failure":
            assert kinds == ["appointment.resisted"] and _hold(w, VACANCY) is None, kinds
            assert _heard(w, d, out, body | {CONFEREE}), "the resisted appointment is no remembered deed"
            assert VACANCY in _forms(w, KING, "confer"), "the Failed conferral does not re-form"
        else:
            assert kinds == ["tenure.opened"], (band, kinds)
            h = _hold(w, VACANCY)
            assert h is not None and h.subject == CONFEREE and h.term is None, (band, h)   # control: a Partial opens untermed

        # REVOKE: the duke, opposed by himself (the seat's live holder)
        band, kinds, out = _resolved(w, d, Act(id=f"c3_revoke_{seed}", actor=KING, verb="revoke", via=VIA,
                                               payload={"subject": TARGET}))
        bands["revoke"][band] = bands["revoke"].get(band, 0) + 1
        bans = [t for t in w.tenures if t.kind == "ban" and t.subject == "p_high" and t.live]
        if band == "Failure":
            assert kinds == ["revocation.resisted"], kinds
            assert _hold(w, TARGET) is not None and _hold(w, TARGET).subject == "p_high" and not bans, "the holder lost his seat"
            assert _heard(w, d, out, body | {"p_high"}), "the withstood revocation is no remembered deed"
            assert TARGET in _forms(w, KING, "revoke"), "the Failed revocation does not re-form"   # his own ledger now names the seat
        else:
            assert kinds == ["tenure.closed"] and _hold(w, TARGET) is None, (band, kinds)
            # the ruled disposal (`appointed` -> a ban) at O/S; a Partial unseats without it
            assert len(bans) == (0 if band == "Partial" else 1), (band, bans)

        # SUCCEED: the heir claims the vacant throne by his title -- nobody holds it, so nobody stands opposite
        band, kinds, out = _resolved(w, d, Act(id=f"c3_succeed_{seed}", actor=HEIR, verb="succeed", payload={"subject": THRONE}))
        bands["succeed"][band] = bands["succeed"].get(band, 0) + 1
        if band == "Failure":
            assert kinds == ["succession.contested"] and _hold(w, THRONE) is None, kinds
            assert _hold(w, TITLE) is not None and _hold(w, TITLE).subject == HEIR, "the Failed claim laid the title down"
            assert _heard(w, d, out, {HEIR}), "the contested claim is no remembered deed"
            assert THRONE in _forms(w, HEIR, "succeed"), "the Failed claim does not re-form"
        else:
            assert set(kinds) == {"succession.claimed", "tenure.closed"}, (band, kinds)
            h = _hold(w, THRONE)
            assert h is not None and h.subject == HEIR and h.term is None and _hold(w, TITLE) is None, (band, h)
        checked += 1
    assert checked >= 40, checked
    four = {"Overwhelming", "Success", "Partial", "Failure"}
    assert set(bands["confer"]) == four and set(bands["succeed"]) == four, bands
    assert bands["revoke"].get("Failure", 0) > 0, bands
