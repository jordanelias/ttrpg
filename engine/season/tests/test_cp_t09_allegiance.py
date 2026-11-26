"""B21b.08 (CP-T09-01, AM-F-16): ALLEGIANCE FOLLOWS OPINION -- JOIN, LEAVE, SWITCH.

`world_q.joinable` filters `propositions_heard`'s output in `questions_for`: a rival creed passes only where `opinion_of` is above both
`world_q.INDIFFERENCE` and his opinion of his own faction. `world_q.leave_referents` carries a member's own faction on a question about a
person he regards on its behalf when his opinion of it is below `INDIFFERENCE`, so `release` forms on his `commit`. `world_q.creed_occasion` stamps
a person who has left a faction and holds a seat or land as a `Founder`, and `opening_set` offers him the creed `utter`.

All four drive the built realm, seed 0, tick 0 (Valorsmark, head `p_npc_020`; Varfell, head `p_npc_052`), forming through `opening_set` and folding
through the shipped `SeasonDriver.resolve`.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data import rosters as R
from engine.season.data.matrix import WriteClass
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act, Claim, Tenure

from .test_in53_vacancy_need import _formed

OWN, OWN_HEAD = "fac_valorsmark", "p_npc_020"
RIVAL, RIVAL_HEAD = "fac_varfell", "p_npc_052"


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


def _act(w, pid, cand, tag):
    p = w.persons[pid]
    return Act(tag, pid, cand.verb, payload=_payload_of(cand), via=seat_of(p, cand))


def _claim_about(pid, subject, cid):
    """A claim `pid` holds about `subject` (a person: admitted to his question by the person-side test), none of his own act."""
    return Claim(cid, pid, subject, "exists:Person", True, 0, "firsthand", 100, "own", 0)


def _members(w, fac, n, skip=()):
    return [m for m in Q.members(w, fac) if m not in skip][:n]


def _twin(w, src, dst):
    """`dst` equal to `src` in everything the opinion reads but a stance row: his pursuits, convictions, no stance, the same ledger."""
    s, t = w.persons[src], w.persons[dst]
    t.pursuits, t.conviction, t.stance, t.ledger = dict(s.pursuits), dict(s.conviction), [], list(s.ledger)


def _question_about(w, pid, subject):
    return next(q for q in Q.questions_for(w, w.persons[pid]) if q.about.startswith("c_about_"))


def test_a_member_reading_his_head_below_zero_forms_release():
    """Two Valorsmark members equal in pursuits, convictions and ledger; one holds a stance row (-5, 5) toward the head. His question about the head
    carries `fac_valorsmark` and `release` forms on it and folds (`commitment.ended`, he is no member); the other's carries neither."""
    w = build_realm(0)
    d = SeasonDriver(w)
    leaver, stayer = _members(w, OWN, 2, skip=(OWN_HEAD,))
    _twin(w, leaver, stayer)
    w.persons[leaver].stance = [(OWN_HEAD, -5, 5)]
    for pid in (leaver, stayer):
        w.persons[pid].ledger.append(_claim_about(pid, OWN_HEAD, f"c_about_{pid}"))
    assert Q.opinion_of(w, w.persons[leaver], OWN) < Q.INDIFFERENCE <= Q.opinion_of(w, w.persons[stayer], OWN), "fixture"

    q_leaver, q_stayer = _question_about(w, leaver, OWN_HEAD), _question_about(w, stayer, OWN_HEAD)
    assert OWN in q_leaver.referents and OWN not in q_stayer.referents, (q_leaver.referents, q_stayer.referents)
    (rel,) = [c for c in _formed(w, leaver, q_leaver) if c.verb == "release" and c.subject == OWN]
    assert [c for c in _formed(w, stayer, q_stayer) if c.verb == "release" and c.subject == OWN] == []
    assert "commitment.ended" in _fold(w, d, _act(w, leaver, rel, "a_leave"))
    assert leaver not in Q.members(w, OWN) and stayer in Q.members(w, OWN)


def _stranger(w, pid):
    """`pid`, a Valorsmark member, out of his faction and with a told claim naming Varfell's creed (a witnessed `utter` of it)."""
    for t in w.persons[pid].tenures:
        if t.kind == "commit" and t.live and t.object == OWN:
            t.until = w.tick
    w.persons[pid].ledger.append(Claim(f"c_told_{pid}", pid, RIVAL, "proposition.uttered", True, 0, "told", 100, "own", 0, doer=RIVAL_HEAD))
    assert Q.own_factions(w, w.persons[pid]) == () and RIVAL in Q.propositions_heard(w, w.persons[pid]), "fixture"


def _commit_on_rival(w, pid):
    q = Q.questions_for(w, w.persons[pid])[0]
    return [c for c in _formed(w, pid, q) if c.verb == "commit" and c.subject == RIVAL]


def test_a_stranger_favouring_varfell_forms_commit_and_joins():
    w = build_realm(0)
    d = SeasonDriver(w)
    (pid,) = _members(w, OWN, 1, skip=(OWN_HEAD,))
    _stranger(w, pid)
    w.persons[pid].stance = [(RIVAL_HEAD, 5, 5)]
    assert Q.opinion_of(w, w.persons[pid], RIVAL) > Q.INDIFFERENCE, "fixture"
    (cand,) = _commit_on_rival(w, pid)
    assert pid not in Q.members(w, RIVAL)
    # the filter is formation; admission is the fold's own answer (`admitted`, B21.63): Varfell's head utters one naming him and commits to it
    assert _fold(w, d, Act(id="a_adm", actor=RIVAL_HEAD, verb="utter", payload={"mood": "OUGHT", "subject": pid, "predicate": "is admitted to", "value": RIVAL}),
                 ) == ["proposition.uttered"]
    assert _fold(w, d, Act(id="a_adm_yes", actor=RIVAL_HEAD, verb="commit", payload={"subject": "prop:a_adm"})) == ["commitment.made"]
    assert Q.admission_stands(w, pid, RIVAL), "fixture"
    assert "commitment.made" in _fold(w, d, _act(w, pid, cand, "a_join"))
    assert pid in Q.members(w, RIVAL) and Q.faction_holding(w, pid) == RIVAL


def test_a_stranger_disliking_varfell_forms_no_commit():
    """The control of the join arm, and the one observation of the filter: with it dropped (`joinable` returning `heard`) this forms."""
    w = build_realm(0)
    (pid,) = _members(w, OWN, 1, skip=(OWN_HEAD,))
    _stranger(w, pid)
    w.persons[pid].stance = [(RIVAL_HEAD, -5, 5)]
    assert Q.opinion_of(w, w.persons[pid], RIVAL) < Q.INDIFFERENCE, "fixture"
    assert _commit_on_rival(w, pid) == []


def test_a_leaver_with_a_land_hold_is_offered_the_creed_utter():
    """A land-holding seat-holder who has released his faction is a `Founder` and forms the creed `utter` (the creed's mood and predicate on its
    payload); folded, the Proposition is a faction (`faction_props`). A man who has left and holds neither seat nor land is not offered it."""
    w = build_realm(0)
    d = SeasonDriver(w)
    land_holders = [pid for pid, p in sorted(w.persons.items())
                    if any(t.kind == "hold" and t.live and t.object in w.rungs and w.rungs[t.object].kind == "territory" for t in p.tenures)
                    and len(Q.own_factions(w, p)) == 1]
    assert land_holders, "fixture: no territory holder in the built realm"
    landless = next(m for m in Q.members(w, OWN) if not any(t.kind == "hold" and t.live for t in w.persons[m].tenures))
    for pid in (land_holders[0], landless):
        for t in w.persons[pid].tenures:
            if t.kind == "commit" and t.live and t.object in Q.faction_props(w):
                t.until = w.tick
    founder = land_holders[0]
    assert Q.creed_occasion(w, w.persons[founder]) and not Q.creed_occasion(w, w.persons[landless])

    q = Q.questions_for(w, w.persons[founder])[0]
    creeds = [c for c in _formed(w, founder, q) if c.verb == "utter" and c.subject == founder]
    assert [c.operands.get("predicate") for c in creeds] == [R.FACTION_CREED["predicate"]], creeds
    assert "proposition.uttered" in _fold(w, d, _act(w, founder, creeds[0], "a_found"))
    assert "prop:a_found" in Q.faction_props(w) and not Q.creed_occasion(w, w.persons[founder]), "a creed uttered is not offered twice"
    qs = Q.questions_for(w, w.persons[landless])
    assert qs and not any(c.verb == "utter" and c.operands.get("predicate") for c in _formed(w, landless, qs[0]))


# ---- B21b.10 (CP-T09-05, AM-F-14): LAND REWARDS THE SWORN -- `world_q.sworn_holdings`. Reward arm absent (BLOCKED on IN-08's `deed:rung.ceded` cell). ----

LORD, SWORN = "p_npc_020", "p_npc_050"      # the king (seats `off_king`, `off_duke_valorsmark`; six territories) and a man sworn to `off_king`


def _beside_the_lord(w):
    """The lord knows `SWORN` (a claim about him, so the question he answers is about him) and `SWORN` stands where he does (`give`'s `with`)."""
    for t in w.persons[SWORN].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_beside_lord", SWORN, Q.place_of(w, LORD), "contain", since=0))
    w.persons[LORD].ledger.append(_claim_about(LORD, SWORN, f"c_about_{LORD}"))


def _gives_of_land(w):
    q = _question_about(w, LORD, SWORN)
    return [c for c in _formed(w, LORD, q) if c.verb == "give" and c.subject in w.rungs]


def test_a_holder_with_a_sworn_man_beside_him_forms_give_of_his_territory():
    """The king, with `SWORN` live-obliged to `off_king` and standing beside him, answers a question about him: `give {subject: a territory he holds, to: SWORN}`
    forms, and folded the rung is `rung.ceded` and `SWORN` holds it."""
    w = build_realm(0)
    d = SeasonDriver(w)
    _beside_the_lord(w)
    assert SWORN in Q.establishment_of(w, "off_king"), "fixture"
    gives = [c for c in _gives_of_land(w) if c.operands.get("to") == SWORN]
    assert gives and {c.subject for c in gives} <= set(Q.holdings_of(w, LORD)), gives
    land = gives[0].subject
    assert "rung.ceded" in _fold(w, d, _act(w, LORD, gives[0], "a_grant"))
    assert Q.hold_force(w, land).subject == SWORN


def test_a_holder_with_no_obligee_forms_no_give_of_the_rung():
    """The control, one change from the arm above: `SWORN`'s `oblige` is closed, so he is nobody's sworn man and the same question forms no `give` of land."""
    w = build_realm(0)
    _beside_the_lord(w)
    for t in w.tenures:
        if t.kind == "oblige" and t.subject == SWORN and t.live:
            t.until = w.tick
    assert SWORN not in Q.establishment_of(w, "off_king") and Q.holdings_of(w, LORD), "fixture"
    assert _gives_of_land(w) == []
