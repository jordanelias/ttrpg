"""B21b.11 (CP-T09-02 (a), AM-F-10, AM-F-11): `declare` -- THE ROW, AND THE WAR ONLY A DECLARATION OPENS.

`declare` is a seated muster-holder's act (`remit:dispatch`, `march`'s and `raze`'s eligibility): through the one mint `_eff_utter` makes it writes the WAR
Proposition (subject the seat's faction, value the target) and the declarer's own `commit` to it in one write. `world_q.at_war` asks, beside B21's `may_wage`,
that the Proposition's creating Event's causing act is a `declare`. All three drive the built realm, seed 0, forming through `opening_set` and folding through
the shipped `SeasonDriver.resolve`.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data.rosters import SEEN_PREDICATE
from engine.season.epistemic import Seen
from engine.season.data.matrix import WriteClass
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q as Q
from engine.season.state import gate
from engine.season.state.carriers import Act, Claim

from .test_in53_vacancy_need import _formed

OWN, TARGET = "fac_valorsmark", "fac_guilds"


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _declarer(w, told=True):
    """A Valorsmark member holding a seat whose grant carries `dispatch`, read off `Tenure.granted_acts` and not by `gate.may_wage`; and (`told`) told of the
    target's creed, so the creed is a Proposition his own ledger names (`propositions_heard`) and `declare` forms on it."""
    pid = next(p for p in sorted(w.persons)
               if p in Q.members(w, OWN)
               and any(t.kind == "hold" and t.live and t.object in w.offices and gate.MUSTER_ACT in t.granted_acts
                       and gate.seat_faction(w, t.object) == OWN for t in w.persons[p].tenures))
    if told:
        w.persons[pid].ledger.append(Claim(f"c_told_{pid}", pid, TARGET, "proposition.uttered", True, 0, "told", 100, "own", 0, doer="p_npc_052"))
    return pid


def _declare_candidates(w, pid, target):
    q = Q.questions_for(w, w.persons[pid])[0]
    return [c for c in _formed(w, pid, q) if c.verb == "declare" and c.subject == target]


def test_a_seated_muster_holder_declares_and_the_war_is_live():
    """A computed `declare` forms on the target's creed, folds (`war.declared`, no `proposition.uttered`), mints a WAR Proposition between the two factions
    with the declarer's own live `commit`, and `at_war` reads True both ways; the control reads False first. Witnessed, `war.declared` reaches a person who is
    not where the act was done (the realm reach of a `binding_decision` kind)."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    assert Q.at_war(w, OWN, TARGET) is False, "control failed -- a war before any declaration"
    cand = _declare_candidates(w, pid, TARGET)[0]
    out = _fold(w, d, Act("a_decl", pid, "declare", payload=_payload_of(cand), via=seat_of(w.persons[pid], cand)))
    assert [e.kind for e in out] == ["war.declared"], [e.kind for e in out]
    war = [p for p in w.propositions.values() if p.mood == Q.WAR_MOOD]
    assert len(war) == 1 and (war[0].subject, war[0].value) == (OWN, TARGET)
    assert any(t.kind == "commit" and t.object == war[0].id and t.live for t in w.persons[pid].tenures), "the declarer's own commit"
    assert Q.at_war(w, OWN, TARGET) is True and Q.at_war(w, TARGET, OWN) is True
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    here = Q.place_of(w, pid)
    far = [p for p in sorted(w.persons) if p != pid and Q.place_of(w, p) != here
           and any(c.predicate == "war.declared" for c in w.persons[p].ledger)]
    assert far, "no one away from the declarer holds the declaration"


def test_an_utter_of_mood_war_plus_a_commit_is_no_war():
    """THE S2 CONTROL: the same WAR Proposition minted by a plain `utter` and committed to by a seated muster-holder through the real fold is no war --
    `at_war` asks that the creating Event's causing act is a `declare`. The control: the identical chain minted by `declare` is."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    kinds = [e.kind for e in _fold(w, d, Act("a_utt", pid, "utter", payload={"mood": "WAR", "subject": OWN, "value": TARGET}))]
    assert kinds == ["proposition.uttered"], kinds
    kinds = [e.kind for e in _fold(w, d, Act("a_utt_commit", pid, "commit", payload={"subject": "prop:a_utt"}))]
    assert kinds == ["commitment.made"], kinds
    assert Q.at_war(w, OWN, TARGET) is False and Q.at_war(w, TARGET, OWN) is False
    cand = _declare_candidates(w, pid, TARGET)[0]
    _fold(w, d, Act("a_decl", pid, "declare", payload=_payload_of(cand), via=seat_of(w.persons[pid], cand)))
    assert Q.at_war(w, OWN, TARGET) is True


def test_declare_on_his_own_faction_is_refused():
    """`declare.refused`, nothing minted and no commit opened, for the declarer's own faction and for a target that is no rostered faction's Proposition."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    seat = next(t.object for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object in w.offices
                and gate.MUSTER_ACT in t.granted_acts and gate.seat_faction(w, t.object) == OWN)
    before = (len(w.propositions), sum(1 for t in w.tenures if t.kind == "commit"))
    refused = 0
    for n, target in enumerate((OWN, "prop:no_faction")):
        if target not in w.propositions:
            w.propositions[target] = type(w.propositions[OWN])(target, "OUGHT", pid, "a cause", True, 0)
            before = (before[0] + 1, before[1])
        kinds = [e.kind for e in _fold(w, d, Act(f"a_decl_{n}", pid, "declare", payload={"subject": target}, via=seat))]
        assert kinds == ["declare.refused"], (target, kinds)
        refused += 1
    assert refused == 2
    assert (len(w.propositions), sum(1 for t in w.tenures if t.kind == "commit")) == before
    assert Q.at_war(w, OWN, OWN) is False


# --- B21b.12 (CP-T09-02 (b), (c), (d)): THE WAR'S OCCASION, ITS TARGET SET, AND RALLYING --------------------

def _declare(w, d, pid, target=TARGET):
    cand = _declare_candidates(w, pid, target)[0]
    return _fold(w, d, Act(f"a_decl_{pid}", pid, "declare", payload=_payload_of(cand), via=seat_of(w.persons[pid], cand)))


def _wound(w, pid, doer_faction, n):
    """`pid` holds the firsthand claim of one of his own faction's men wounded (`body.changed`) with the `seen.who` pairing naming a member of `doer_faction`: the
    deed `opinion_referents` reads. Returns the doer."""
    victim = [m for m in Q.members(w, OWN) if m != pid][n]       # one victim a wound: two sightings of one man pair no doer (IN-58)
    doer = Q.members(w, doer_faction)[0]
    w.persons[pid].ledger += [
        Claim(f"c_wound_{n}", pid, victim, Q.WOUND_KIND, True, 0, "firsthand", 100, "own", 0, doer=doer),
        Claim(f"c_wound_seen_{n}", pid, victim, SEEN_PREDICATE, Seen(stratum="contested_physical", marks=(), who=doer), 0, "firsthand", 100, "own", 0)]
    return doer


def test_a_wound_by_a_disliked_faction_forms_declare():
    """(b): a seated muster-holder (the declarer, told of no creed) holding the firsthand claim of his man WOUNDED by a member of a faction he reads below
    indifference forms `declare` on that faction's creed, which nothing told him of; the control reads the same man wounded by a faction he favours and forms
    none. Folded, the war is live both ways and a person away from the declarer holds the `war.declared` claim at WITNESS."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w, told=False)
    me = w.persons[pid]
    assert Q.opinion_of(w, me, TARGET) < 0 <= Q.opinion_of(w, me, "fac_varfell"), "the pair is not the one the falsifier needs"
    assert _declare_candidates(w, pid, TARGET) == [], "control failed -- declare forms on an untold creed with no wound"
    _wound(w, pid, "fac_varfell", 0)
    assert _declare_candidates(w, pid, "fac_varfell") == [] and _declare_candidates(w, pid, TARGET) == [], "a wound by a favoured faction raised a creed"
    doer = _wound(w, pid, TARGET, 1)
    assert Q.opinion_referents(w, me, next(c for c in me.ledger if c.id == "c_wound_1"))[0] == doer, "the wound is not one he judges"
    assert _declare_candidates(w, pid, TARGET), "the wound raised no declare"
    out = _declare(w, d, pid)
    assert [e.kind for e in out] == ["war.declared"], [e.kind for e in out]
    assert Q.at_war(w, OWN, TARGET) and Q.at_war(w, TARGET, OWN)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    here = Q.place_of(w, pid)
    assert [p for p in sorted(w.persons) if p != pid and Q.place_of(w, p) != here
            and any(c.predicate == "war.declared" for c in w.persons[p].ledger)], "no one away from the declarer holds the declaration"


def _walk(w, pid):
    """`pid`'s questions' `march` candidates, subject -> the Candidate."""
    return {c.subject: c for q in Q.questions_for(w, w.persons[pid]) for c in _formed(w, pid, q) if c.verb == "march"}


def test_a_live_war_offers_an_enemy_town_the_ledger_never_named():
    """(c): the declarer's seat reaches settlements Hafenmark holds that his ledger never named. With no war none is a `march` target; with the war live `march` forms
    on every one; with every committer released (`at_war` False) the term withdraws."""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w, told=True)
    foe = "fac_hafenmark"
    towns = sorted(r.id for r in w.rungs.values() if r.kind == "settlement" and Q.holder_faction_of(w, r.id) == foe
                   and any(gate.purview_reaches(w, w.offices[t.object], r.id) for t in w.persons[pid].tenures
                           if t.kind == "hold" and t.live and t.object in w.offices and gate.MUSTER_ACT in t.granted_acts))
    named = Q.ledger_names(w.persons[pid].ledger)
    assert towns and not (set(towns) & named), "the fixture needs enemy towns his ledger never named"
    assert not (set(towns) & set(_walk(w, pid))), "control failed -- a march forms on an enemy town in peacetime"
    seat = next(t.object for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object in w.offices
                and gate.MUSTER_ACT in t.granted_acts and gate.seat_faction(w, t.object) == OWN)
    out = _fold(w, d, Act("a_decl_foe", pid, "declare", payload={"subject": foe}, via=seat))       # he reads Hafenmark above 0: no occasion forms it, the war is the fixture
    assert [e.kind for e in out] == ["war.declared"] and Q.at_war(w, OWN, foe)
    assert set(towns) <= set(Q.war_fields(w, w.persons[pid])), "the war offered not every town the seat reaches"
    assert set(towns) <= set(_walk(w, pid)), "no march forms on an enemy town"
    war = next(x.id for x in w.propositions.values() if x.mood == Q.WAR_MOOD)
    _fold(w, d, Act("a_peace", pid, "release", payload={"subject": war}))
    assert not Q.at_war(w, OWN, foe)
    assert Q.war_fields(w, w.persons[pid]) == () and not (set(towns) & set(_walk(w, pid))), "the town is still offered with every committer released"


def test_a_member_of_either_side_rallies_and_his_commit_does_not_keep_the_war():
    """(d): once a war is declared and witnessed, a person of either party who holds the `war.declared` claim forms `commit` to the war (through
    `propositions_heard`: the claim's subject is the WAR Proposition, so no stamp of its own is needed). Folded, the defender's commit is no war kept alive: the declarer releases and `at_war` reads False with the defender's commit still live
    (he sits in no muster seat, `may_wage`). [ASSUMPTION: names]"""
    w = build_realm(0)
    d = SeasonDriver(w)
    pid = _declarer(w)
    out = _declare(w, d, pid)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    war = next(x.id for x in w.propositions.values() if x.mood == Q.WAR_MOOD)

    def commit_on_war(p):
        return [c for q in Q.questions_for(w, w.persons[p]) for c in _formed(w, p, q) if c.verb == "commit" and c.subject == war]
    seatless = lambda p: not any(t.kind == "hold" and t.live and gate.MUSTER_ACT in t.granted_acts for t in w.persons[p].tenures)
    holders = [p for p in sorted(w.persons) if p != pid and any(c.predicate == "war.declared" for c in w.persons[p].ledger)]
    defender = next(p for p in holders if Q.faction_holding(w, p) == TARGET and seatless(p))
    ally = next(p for p in holders if Q.faction_holding(w, p) == OWN and seatless(p))
    assert commit_on_war(defender) and commit_on_war(ally), "a member of a party is not rallied"
    c = commit_on_war(defender)[0]
    kinds = [e.kind for e in _fold(w, d, Act("a_rally", defender, "commit", payload=_payload_of(c)))]
    assert kinds == ["commitment.made"], kinds
    assert Q.at_war(w, OWN, TARGET)
    _fold(w, d, Act("a_peace", pid, "release", payload={"subject": war}))
    assert any(t.kind == "commit" and t.object == war and t.live and t.subject == defender for t in w.tenures), "the rally was released with the declarer"
    assert not Q.at_war(w, OWN, TARGET), "a rallying commit kept the war alive"


# --- B21b.14 (CP-T09-03, AM-F-12): ALLIANCE AND PEACE ARE ACTS ON THE WAR -------------------------------------
# The Crown (Valorsmark) declares on Hafenmark; its King mints a `covenant` on the WAR Proposition, `give`s it and the addressee's own `commit` (alliance) or
# `release` (peace) answers it, through `terms_sourced`. Real formation, real fold, WITNESS's content deposit; hand-built only in who holds the seat.

FOE = "fac_hafenmark"


def _war(w, d, faction, foe):
    """A seated muster-holder of `faction` (the first, who is also the maker of the covenants below) declares on `foe`; returns (declarer, war id)."""
    pid = _seated(w, faction)
    seat = next(t.object for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object in w.offices
                and gate.MUSTER_ACT in t.granted_acts and gate.seat_faction(w, t.object) == faction)
    assert [e.kind for e in _fold(w, d, Act("a_decl_war", pid, "declare", payload={"subject": foe}, via=seat))] == ["war.declared"]
    return pid, next(x.id for x in w.propositions.values() if x.mood == Q.WAR_MOOD)


def _crown_war(w, d):
    """The Crown (Valorsmark) declares on Hafenmark."""
    return _war(w, d, OWN, FOE)


def _hand_over(w, d, maker, war, to):
    """`maker` mints a `covenant` on the war through the seat he holds that grants `issue`, stands `to` where he stands and `give`s the instrument; WITNESS deposits
    its content. Returns the dispensation's id."""
    seat = next(t.object for t in w.persons[maker].tenures if t.kind == "hold" and t.live and t.object in w.offices and "issue" in t.granted_acts)
    here = [t.object for t in w.persons[maker].tenures if t.live and t.kind in ("contain", "reside")]
    for t in w.persons[to].tenures:
        if t.live and t.kind in ("contain", "reside"):
            t.object = here[0]
    rec = f"rec:cv_{to}"
    assert [e.kind for e in _fold(w, d, Act(f"cv_{to}", maker, "covenant", via=seat, payload={"subject": war, "to": to}))] == ["covenant.offered"]
    gave = _fold(w, d, Act(f"cvg_{to}", maker, "give", payload={"subject": rec, "to": to}))
    assert [e.kind for e in gave] == ["record.given"], [e.kind for e in gave]
    d.witness(mint_token(w, WriteClass.INTERIOR), gave)
    return rec


def _verbs_on(w, pid, war):
    """Every verb `pid`'s own deliberation forms on the war Proposition."""
    return {c.verb for q in Q.questions_for(w, w.persons[pid]) for c in _formed(w, pid, q) if c.subject == war}


def _seated(w, faction, exclude=()):
    return next(p for p in sorted(w.persons) if p not in exclude and p in Q.members(w, faction)
                and any(t.kind == "hold" and t.live and t.object in w.offices and gate.MUSTER_ACT in t.granted_acts
                        and gate.seat_faction(w, t.object) == faction for t in w.persons[p].tenures))


def test_an_ally_holding_the_crowns_covenant_on_w_commits_and_is_offered_enemy_towns():
    """(1): a seat-holder of a third faction holding a covenant on W minted by a party's seat forms `commit` to W, folds it, and is then at war on the maker's
    side: `side_in` reads the issuing seat's faction and CP-T09-02 (c) offers him the enemy's towns his purview reaches. The fixture is the one the realm's seats
    allow (only the King's seat reaches another faction's towns): Hafenmark declares on Varfell, its Duchess's covenant goes to the King. CONTROL: before the
    instrument, and holding it without accepting, neither; and his own `commit` to W without the instrument reads no side."""
    third, enemy = OWN, "fac_varfell"
    w = build_realm(0)
    d = SeasonDriver(w)
    duchess, war = _war(w, d, FOE, enemy)
    ally = _seated(w, third)
    assert Q.side_in(w, w.persons[ally], war) is None and Q.war_fields(w, w.persons[ally]) == (), "control failed -- a side before any instrument"
    assert Q.side_in(w, w.persons[duchess], war) == FOE, "the declarer is the war's subject"
    _hand_over(w, d, duchess, war, ally)
    assert Q.side_in(w, w.persons[ally], war) == FOE, "the instrument names the maker's seat's faction"
    assert Q.war_fields(w, w.persons[ally]) == (), "holding the instrument without accepting it is no alliance"
    cands = [c for q in Q.questions_for(w, w.persons[ally]) for c in _formed(w, ally, q) if c.verb == "commit" and c.subject == war]
    assert cands, "the addressee formed no commit on W from the held dispensation"
    assert [e.kind for e in _fold(w, d, Act("a_ally", ally, "commit", payload=_payload_of(cands[0])))] == ["commitment.made"]
    towns = Q.war_fields(w, w.persons[ally])
    assert towns and all(Q.holder_faction_of(w, r) == enemy for r in towns), towns
    # CONTROL: the same commit without the instrument -- a third party who rallied by hearsay has no side, and no town.
    w2 = build_realm(0)
    d2 = SeasonDriver(w2)
    _, war2 = _war(w2, d2, FOE, enemy)
    ally2 = _seated(w2, third)
    _fold(w2, d2, Act("a_ally2", ally2, "commit", payload={"subject": war2}))
    assert Q.side_in(w2, w2.persons[ally2], war2) is None and Q.war_fields(w2, w2.persons[ally2]) == ()


def test_a_peace_covenant_held_by_an_enemy_committer_forms_release():
    """(2): a seated Hafenmark committer to W holding the Crown's covenant on W forms `release` on W; folded, his edge closes (`commitment.ended`), and with the
    declarer's own release as well no committer is left and `at_war` reads False. His side is his own faction's (`side_in`), the covenant notwithstanding."""
    w = build_realm(0)
    d = SeasonDriver(w)
    king, war = _crown_war(w, d)
    foe = _seated(w, FOE)
    _fold(w, d, Act("a_foe_commit", foe, "commit", payload={"subject": war}))
    assert Q.at_war(w, OWN, FOE) and Q.side_in(w, w.persons[foe], war) == FOE
    _hand_over(w, d, king, war, foe)
    assert Q.side_in(w, w.persons[foe], war) == FOE, "an enemy committer's side is his own"
    cands = [c for q in Q.questions_for(w, w.persons[foe]) for c in _formed(w, foe, q) if c.verb == "release" and c.subject == war]
    assert cands, "the enemy committer formed no release on W"
    kinds = [e.kind for e in _fold(w, d, Act("a_foe_release", foe, "release", payload=_payload_of(cands[0])))]
    assert "commitment.ended" in kinds, kinds
    assert not any(t.kind == "commit" and t.object == war and t.live for t in w.persons[foe].tenures)
    assert Q.at_war(w, OWN, FOE), "the declarer's own commit still keeps the war"
    _fold(w, d, Act("a_king_release", king, "release", payload={"subject": war}))
    assert not Q.at_war(w, OWN, FOE) and not Q.at_war(w, FOE, OWN), "every committer released, the war stands"


def test_one_instrument_offers_release_and_commit_and_records_which():
    """(3) [ASSUMPTION: names]: a peace covenant offers an enemy member whichever of the two edges his own state allows -- `release` to the one who holds a
    `commit` to W (`held_edge_declines` spares him a second edge), `commit` to the one who holds none -- and never both to one man. Recorded, not prevented:
    a `commit` formed from a peace offer is an escalation CP-T09-02's stopping reading counts."""
    w = build_realm(0)
    d = SeasonDriver(w)
    king, war = _crown_war(w, d)
    committed = _seated(w, FOE)
    uncommitted = _seated(w, FOE, exclude=(committed,))
    _fold(w, d, Act("a_foe_commit", committed, "commit", payload={"subject": war}))
    for who in (committed, uncommitted):
        _hand_over(w, d, king, war, who)
    got = {who: _verbs_on(w, who, war) & {"commit", "release"} for who in (committed, uncommitted)}
    assert got == {committed: {"release"}, uncommitted: {"commit"}}, got
