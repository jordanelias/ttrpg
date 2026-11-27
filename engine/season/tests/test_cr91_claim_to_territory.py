"""B21b.13 (CR-91 (1), (2), (4); A-103): A CLAIM TO A TERRITORY, AS AN OCCASION AND AS CONTEXT.

A claim to a territory is a Proposition of mood `world_q.CLAIM_MOOD`, `claim:<faction>:<rung>`, minted by `utter` only on a ground of the closed roster
`rosters.yaml: casus_grounds` (`loop/predicates.py::_req_utter`, `world_q.casus_ground`); a held one is `declare`'s occasion (`world_q.claim_creeds`) and a war
declared on it has the claimed rungs for its target set (`world_q.war_fields`); never a gate on `march`. `faction_q.civil_war` reads a war between two factions
whose heads are both sworn to the sovereign's seat. All drive the built realm, seed 0, through the shipped `SeasonDriver.resolve`.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.loop.driver import SeasonDriver
from engine.season.queries import faction_q as FQ
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act

from ._dispatch_realm import realm_seating_dispatch
from .test_cp_t09_declare import _declare_candidates, _fold
from .test_march import _occupy, _seize_kinds

HAF, CROWN, VAR = "fac_hafenmark", "fac_valorsmark", "fac_varfell"
DUCHESS, DUCHY_SEAT = "p_npc_050", "off_duchess_hafenmark"      # Hafenmark's head, seated in a seat granting `dispatch` (CR-86: sworn to `off_king`)
TOWN = "set_s_016"                                              # a Hafenmark-held town the Crown can occupy unopposed (`test_march.py` exit (vi))
OTHER = "set_s_017"                                             # a second, seized beside it and never claimed: the plain war's wider target set


def _claim(pid, faction, rung, act_id="a_claim"):
    return Act(act_id, pid, "utter", payload={"mood": Q.CLAIM_MOOD, "subject": faction, "value": rung})


def _seized():
    """The built realm with `TOWN` occupied by the Crown and seized through `off_king` (`rung.seized` in the log), so Hafenmark holds ground (i) to it. The realm is
    `test_march.py`'s (`_dispatch_realm.realm_seating_dispatch`: the spymaster's seat granted `dispatch`, B21.03's named fixture edit), so the Crown can march."""
    w = realm_seating_dispatch(0)
    for n, town in enumerate((TOWN, OTHER)):
        _occupy(w, town, "p_npc_033", "off_spymaster", act_id=f"m{n}")
        assert _seize_kinds(w, town, act_id=f"z{n}") == ["rung.seized"] and Q.holder_faction_of(w, town) == CROWN
    return w


def test_a_planted_seizure_gives_the_loser_ground_and_his_claim_executes():
    """Ground (i): after the Crown seizes a Hafenmark town, Hafenmark's Duchess utters a claim to it: `proposition.uttered`, the claim minted under its own id
    (`claim:fac_hafenmark:set_s_016`, subject the faction, value the rung) and held by her. The control, the same claim before the seizure, is refused."""
    ctrl = build_realm(0)
    d = SeasonDriver(ctrl)
    assert [e.kind for e in _fold(ctrl, d, _claim(DUCHESS, HAF, TOWN))] == ["utter.refused"], "control failed -- a claim with no seizure behind it executed"
    w = _seized()
    d = SeasonDriver(w)
    assert Q.casus_ground(w, DUCHESS, HAF, TOWN) == "seized_from_faction"
    assert [e.kind for e in _fold(w, d, _claim(DUCHESS, HAF, TOWN))] == ["proposition.uttered"]
    cid = Q.claim_id(HAF, TOWN)
    c = w.propositions[cid]
    assert (c.mood, c.subject, c.value) == (Q.CLAIM_MOOD, HAF, TOWN)
    assert any(t.kind == "hold" and t.live and t.object == cid for t in w.persons[DUCHESS].tenures), "the claimant does not hold her claim"


def test_with_no_ground_the_claim_is_refused_naming_the_ground():
    """With no ground -- a Hafenmark claim to a Crown town nothing was ever taken from Hafenmark in -- the `utter` is refused (`utter.refused`), nothing is minted,
    and the predicate names the clause `ground`; a claim for a faction the utterer is not of is refused on `claimant`."""
    from engine.season.loop.predicates import _req_utter
    w = build_realm(0)
    d = SeasonDriver(w)
    crown_town = "set_s_002"
    assert Q.holder_faction_of(w, crown_town) == CROWN
    before = set(w.propositions)
    assert tuple(_req_utter(w, _claim(DUCHESS, HAF, crown_town))) == (False, "ground")
    assert tuple(_req_utter(w, _claim(DUCHESS, CROWN, crown_town))) == (False, "claimant")
    assert [e.kind for e in _fold(w, d, _claim(DUCHESS, HAF, crown_town))] == ["utter.refused"]
    assert set(w.propositions) == before, "a groundless claim minted a Proposition"


def test_a_held_claim_is_declares_occasion_and_its_target_set_is_the_claimed_rung():
    """CR-91 (2): the Crown has seized two Hafenmark towns and the Duchess claims one. Holding the claim she forms `declare` on the Crown's creed (the town's
    holder), which no other occasion offered her (the control, read before the claim). Folded, the war is live, and her seat's war target set is the claimed town
    alone, where the same war with no claim behind it offers both Crown towns her seat reaches."""
    w = _seized()
    d = SeasonDriver(w)
    assert _declare_candidates(w, DUCHESS, CROWN) == [], "control failed -- declare forms on the Crown with no claim held"
    _fold(w, d, _claim(DUCHESS, HAF, TOWN))
    assert Q.claim_creeds(w, w.persons[DUCHESS]) == (CROWN,)
    cand = _declare_candidates(w, DUCHESS, CROWN)
    assert cand, "a held claim raised no declare"
    out = _fold(w, d, Act("a_decl", DUCHESS, "declare", payload=_payload_of(cand[0]), via=seat_of(w.persons[DUCHESS], cand[0])))
    assert [e.kind for e in out] == ["war.declared"] and Q.at_war(w, HAF, CROWN)
    war = next(x for x in w.propositions.values() if x.mood == Q.WAR_MOOD)
    assert Q.claimed_rungs(w, war) == (TOWN,)
    assert Q.war_fields(w, w.persons[DUCHESS]) == (TOWN,)

    plain = _seized()                                   # the same war, declared with no claim uttered
    pd = SeasonDriver(plain)
    _fold(plain, pd, Act("a_decl", DUCHESS, "declare", payload={"subject": CROWN}, via=DUCHY_SEAT))
    assert Q.at_war(plain, HAF, CROWN)
    assert Q.war_fields(plain, plain.persons[DUCHESS]) == (TOWN, OTHER)


def test_civil_war_reads_true_only_for_two_factions_whose_heads_are_sworn_to_the_sovereign():
    """CR-91 (4): Hafenmark declares on Varfell -- both heads sworn to `off_king` (CR-86) -- and `civil_war` reads True both ways; before the declaration, and for
    Hafenmark's war on the sovereign's own faction (the King is sworn to no seat), it reads False; with the Duchess's oath released it reads False."""
    w = build_realm(0)
    d = SeasonDriver(w)
    assert FQ.civil_war(w, HAF, VAR) is False, "control failed -- a civil war with no war"
    _fold(w, d, Act("a_decl_var", DUCHESS, "declare", payload={"subject": VAR}, via=DUCHY_SEAT))
    assert Q.at_war(w, HAF, VAR)
    assert FQ.civil_war(w, HAF, VAR) is True and FQ.civil_war(w, VAR, HAF) is True
    _fold(w, d, Act("a_decl_crown", DUCHESS, "declare", payload={"subject": CROWN}, via=DUCHY_SEAT))
    assert Q.at_war(w, HAF, CROWN) and FQ.civil_war(w, HAF, CROWN) is False
    for t in w.persons[DUCHESS].tenures:
        if t.kind == "oblige" and t.live and t.object == "off_king":
            t.until = w.tick
    assert Q.at_war(w, HAF, VAR) and FQ.civil_war(w, HAF, VAR) is False, "a war whose one head is sworn to nobody read as civil"
