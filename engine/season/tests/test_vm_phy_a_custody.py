"""`14_VERBS_PHYSICAL_A` (custody and force) -- the gates of the audit's §1.7, §2.7, §3.7 and §4.7, one function each.
This file holds A4's (B14.27), A3's (B15), A1's (B29.01) and A2's (B29.02).

A4, THE REAL CHOOSER. `test_b11a_duel_reach.py` drives the chain through formed Candidates and hand-built acts and
reverts the whole of lane A at once; this test plants ONE grievance between two co-located persons and plays a season
through `harness.probes.chooser` (the game's own policy) and `SeasonDriver.season`: no act is built here. The chain is
bound to the two persons through the driver's own `act_of` (event id -> the act that made it), which the test keeps:
the challenge was issued by A, the accept was declared by B on that challenge's Record, and the scene's outcome
(`body.changed` / `duel.yielded`) is an event of that accept's own act. The instruments watch and change nothing,
except the stamp's own planted failure (`challenges_heard` returning `()` alone), which the second test plays through
a whole season.

LIMITS. (1) The world is `probes.tiny_world()`, not `build_realm` (the gate says "a seeded realm"): a stated
departure, because a realm has no fixed co-located pair to plant a dispute between. (2) Existence at measured seeds,
not a rate: at the tree of the B24 close merged with main the chain completes at seeds 14, 16, 22, 24, 25 of 14-25, and every one of those seeds has A issue the
challenge (seed 6 issues none there, nor 31: B24.27's citing variant added candidates to the chooser's draw); it was 8, 13, 20 of 0-20 before B24, and 0, 3, 5 of 0-5 before the
keyed stream, B06; seeds 4-7 attempt accept with no accept.declared following, most others attempt none); a hash-moving
change re-measures.
"""
from __future__ import annotations

import pytest

from ..data.rosters import CHALLENGE_KIND
from ..decision import assemble
from ..decision import options as O
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..seam.wrappers import combat as CW
from ..state.carriers import Claim, subject_of

A, B = "p_mid", "p_low"           # `tiny_world`: both stand at the hearth; A holds the grievance, B is its object
SEEDS = range(14, 26)             # measured on `tiny_world`; see LIMITS above. Was range(21) before B24 (seed 6 then issues no challenge), range(6) before it: under the keyed stream (B06) the chain completes at none of 0-5
#: How many of `SEEDS` the whole bound chain completes at, measured at the tree this floor was written on (14, 16, 22, 24, 25 of 14-25;
#: was 8, 13, 20 of 0-20 before B24, and 0, 3, 5 of 0-5 before B06's stream; the floor is unchanged).
FLOOR = 3


def _play(seed, monkeypatch):
    """One season of the planted world through the real chooser; returns the world, the driver (whose `act_of` binds an
    event to the act that made it), what the chooser returned in order (`(actor, verb)`, a diagnostic: the driver
    drops done acts and releases at most `per_lap` scenes, so this is what was OFFERED, not what was attempted) and
    the terms every fight was built under."""
    w = P.tiny_world()
    w.world_seed = seed
    me = w.persons[A]
    me.ledger.append(Claim("c_vm_phy_a_deed", A, B, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    me.pursuits = {"liberty": 1.0}                    # his own pursuits judge the deed against him: a dispute

    terms, offered = [], []
    real_input = CW.combat_input

    def spy_input(*a, **k):
        inp = real_input(*a, **k)
        terms.append(inp.terms)
        return inp
    monkeypatch.setattr(CW, "combat_input", spy_input)

    base = P.chooser(w, verbs=resolvable_verbs())

    def choose(p, v, s, ask_budget):
        scenes = base(p, v, s, ask_budget)
        offered.extend((a.actor, a.verb) for sc in scenes for a in sc.acts)
        return scenes
    d = SeasonDriver(w)
    d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, offered, terms


def _made(w, d, kind, verb, actor=None):
    """`(event, act)` for each logged event of `kind` whose act (by `act_of`) is `verb` by `actor` (any, when `None`)."""
    return [(e, d.act_of[e.id]) for e in w.log
            if e.kind == kind and e.id in d.act_of and d.act_of[e.id].verb == verb
            and (actor is None or d.act_of[e.id].actor == actor)]


def _formed(w, pid, verb):
    """`verb` Candidates in `pid`'s own opening set, on every question the world puts to him (the view is the
    size the real deliberation reads, `w.fixtures["view_k"]`)."""
    p = w.persons[pid]
    k_view = w.fixtures.get("view_k")
    return [c for q in world_q.questions_for(w, p)
            for c in O.opening_set(p, assemble(p, q, k_view), q, w.fixtures) if c.verb == verb]


def _accepts_formed(w, pid):
    return _formed(w, pid, "accept")


def test_accept_forms_on_a_heard_challenge(monkeypatch):
    """The audit §4.7 gate. Planted failure: `challenges_heard` returning `()` alone turns this red (see the next test,
    which plays it). Control: the challenged's opening set holds `accept` with the stamp and none without it."""
    checked = complete = 0
    for seed in SEEDS:
        with monkeypatch.context() as m:
            w, d, offered, terms = _play(seed, m)
            kinds = [e.kind for e in w.log]
            # the challenge came from A, the real chooser's pick
            issued = _made(w, d, "challenge.issued", "challenge", A)
            assert issued, (seed, kinds, offered)
            challenge = issued[0][1]
            accepted = _made(w, d, "accept.declared", "accept", B)
            if accepted:
                complete += 1
                ev, act = accepted[0]
                # B's accept is on that challenge's own Record, and it came after the challenge
                assert subject_of(act) == "rec:" + challenge.id, (seed, subject_of(act), challenge.id)
                assert w.records[subject_of(act)].kind == CHALLENGE_KIND, (seed, w.records[subject_of(act)].kind)
                log = list(w.log)
                assert log.index(issued[0][0]) < log.index(ev), (seed, kinds)
                # the scene it set off ended in one of the duel's typed outcomes, an event of THAT accept's own act
                ends = [e for e in log[log.index(ev):]
                        if e.kind in ("duel.yielded", "body.changed") and d.act_of.get(e.id) is act]
                assert ends, (seed, kinds, offered)
                # a challenge names no stakes, so the one fight was built under the roster's `accept` line, `blood`
                assert terms and set(terms) == {"blood"}, (seed, terms)   # every fight the scene built, not their number: the draw moves how many a seed plays
                # CONTROL: B's opening set has `accept` while the stamp stands, and none with the stamp's reader at `()`
                assert _accepts_formed(w, B), (seed, "the challenged holds an `accept` with the stamp")
                m.setattr(world_q, "challenges_heard", lambda w, p, named=None: ())
                assert world_q.questions_for(w, w.persons[B]), (seed, "B is asked something at all")
                assert _accepts_formed(w, B) == [], (seed, "without the stamp the challenged has no `accept`")
        checked += 1
    assert checked == len(SEEDS)
    assert complete >= FLOOR, (complete, FLOOR)


# ---------------------------------------------------------------------------------------------------------------------
# A3 (B15.07): A FELLING IS FOLLOWED BY THE MORTAL-WOUND DRAW, IN THE COMBAT MODULE (the audit §3.7's standing-rule gate).
# ---------------------------------------------------------------------------------------------------------------------
def _a3_scene(w, seed: int, aid: str = "a3"):
    """One fight between `A` and `B` on `w` at `world_seed = seed`: `(the module's CombatOutcome, the host's resolve dict)`, both on the
    record `combat_input` builds and the scene key `resolve` forms (`contest:the body:<aid>`), so the module's `mortal` is what the host maps."""
    from ..state.ids import draw_factory
    w.world_seed = seed
    entry, refusal = CW.entry_for(CW._PRIZE, CW._PROVIDER)
    assert entry is not None, refusal
    got = entry.fn(CW.combat_input(w, [A, B], "fight", cause=aid), draw_factory(w.world_seed, lambda: w.tick)(A, f"contest:{CW._PRIZE}:{aid}"))
    return got, CW.resolve(w, [A, B], [aid], CW._PRIZE, verb="fight")


def test_a3_a_felling_is_followed_by_a_drawn_death():
    """A felled party's fate is the mortal-wound draw's, drawn in the module (`fight.py::mortal_wound`) and only MAPPED by the host
    (`seam/wrappers/combat.py::_wound_state`): over 120 seeded fights at a reachable `mortal_wound_ob`, some felled parties die and some do
    not, and every host `wound_state` entry of a felled party is the module's `MortalResult` (`felled` = `mortal`, `wounds` as drawn).
    FALSIFIER: bypass the mortal roll (no `mortal` on the outcome, or the host not mapping it) and no felled party survives. CONTROL: the same
    seeds at the unreachable control (99.0) leave every felled party felled. SITE: the host adapter calls no sampler, no ladder and no
    uniform (an AST scan of `seam/wrappers/combat.py`): a planted wrapper-side draw computing `felled` is found here."""
    import ast
    import inspect
    from ..loop.driver import SeasonDriver
    w = P.tiny_world()
    SeasonDriver(w)                                              # registers the module entry the host resolves
    shipped = w.fixtures
    reading = {}
    for arm, ob in (("reachable", 2.0), ("control", 99.0)):
        w.fixtures = shipped.sweep("mortal_wound_ob", {c: ob for c in shipped.get("mortal_wound_ob")})
        felled = died = checked = 0
        for seed in range(120):
            got, res = _a3_scene(w, seed)
            assert res["status"] == "RESOLVED", res
            for pid, pw in got.wounds.items():
                st = res["wound_state"][pid]
                if not pw.felled:
                    assert pid not in got.mortal and st["felled"] is False and st["wounds"] == pw.wounds, (seed, pid, st)
                    continue
                m = got.mortal[pid]                          # a felled party is ALWAYS drawn for
                assert (st["felled"], st["wounds"]) == (m.mortal, m.wounds), (seed, pid, st, m)
                felled += 1
                died += m.mortal
            checked += 1
        assert checked == 120 and felled >= 40, (arm, checked, felled)
        reading[arm] = (felled, died)
    assert 0 < reading["reachable"][1] < reading["reachable"][0], f"a felling is neither always nor never a death: {reading}"
    assert reading["control"][1] == reading["control"][0], f"the unreachable control kills every felled party: {reading}"
    # THE SITE: the host forms the key and maps; it draws nothing and grades nothing.
    calls = {n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, "id", None)
             for n in ast.walk(ast.parse(inspect.getsource(CW))) if isinstance(n, ast.Call)}
    planted = calls & {"roll_net_continuous", "roll_net", "net_boost", "degree_from_net", "u", "random", "below", "mortal_wound"}
    assert not planted, f"seam/wrappers/combat.py draws or grades the mortal roll itself: {sorted(planted)}"


# ---------------------------------------------------------------------------------------------------------------------
# A3 (B15.08): `fight`'S TERMS FOLLOW ITS CONTEXT (`rosters.yaml: context_terms`, the Candidate's `context` payload key).
# ---------------------------------------------------------------------------------------------------------------------
def test_a3_fight_terms_follow_the_context(monkeypatch):
    """A `fight` formed on a context of violence carries it (`CONTEXT_KEY`, set by `opening_set`), and the scene the host resolves is fought under
    `context_terms`' line for it: a `crime` fight under `yield`, a `war` fight under `death`; a fight with no context (hand-built) keeps the engine's
    lethal default, and `accept` keeps `duel_terms`' line whatever its context. A `context_terms` key that is no context reader, a term that is no
    name, or a term outside the engine's closed set is REFUSED (`options._check_context_terms`, `verbs._load_context_terms` at import,
    `combat.duel_terms_of` before the call). FALSIFIER: `context_terms` emptied leaves the `crime` fight lethal."""
    from ..data import verbs as V
    from ..data.rosters import CONTEXT_KEY
    from ..gaps import Forbidden
    from ..state.carriers import Act, Question, View
    SeasonDriver(P.tiny_world())                                 # registers the module entry the host resolves
    seen = []
    real_input = CW.combat_input

    def spy(*a, **k):
        inp = real_input(*a, **k)
        seen.append(inp.terms)
        return inp
    monkeypatch.setattr(CW, "combat_input", spy)

    def fought_under(stamp, context):
        w = P.tiny_world()
        q = Question("q:a3", "need", (B,), B, classes=((B, stamp),))
        formed = [c for c in O.opening_set(w.persons[A], View(A, [], w.fixtures.get("view_k"), q), q, w.fixtures)
                  if c.verb == "fight" and c.subject == B]
        assert len(formed) == 1 and formed[0].operands[CONTEXT_KEY] == context, (stamp, formed)
        assert context in O.VIOLENCE_CONTEXT_READERS                     # the key's range is the readers' closed set
        act = w.acts.append(Act(id=f"a3_{context}", actor=A, verb="fight", payload={**formed[0].operands, "subject": B}))
        res = CW.resolve(w, [A, B], [act.id], CW._PRIZE, verb="fight")
        assert res["status"] == "RESOLVED", res
        return seen[-1]

    assert fought_under(V.DETAINEE_CLASS, "crime") == "yield"
    assert fought_under(V.ENEMY_CLASS, "war") == "death"
    w = P.tiny_world()
    assert real_input(w, [A, B], "fight").terms == "death", "a fight with no context keeps the engine's lethal default"
    assert real_input(w, [A, B], "accept", context="crime").terms == "blood", "`duel_terms` outranks the context"
    with monkeypatch.context() as m:
        m.setattr(CW, "CONTEXT_TERMS", {})
        assert fought_under(V.DETAINEE_CLASS, "crime") == "death", "FALSIFIER: `context_terms` emptied, the crime fight is lethal again"
    with monkeypatch.context() as m:
        m.setattr(CW, "CONTEXT_TERMS", {"crime": "mercy"})
        with pytest.raises(Forbidden):
            CW.duel_terms_of("fight", None, "crime")
    with pytest.raises(Forbidden):
        O._check_context_terms({"no_such_context": "yield"})
    with pytest.raises(Forbidden):
        V._load_context_terms({"crime": ""})
    assert V.CONTEXT_TERMS == {"war": "death", "crime": "yield", "defence": "yield"}


# ---------------------------------------------------------------------------------------------------------------------
# A1 (B29.01): `arrest` FORMS ON A WARRANT ADDRESSED TO THE OFFICER AND HEARD OF (the audit's §1.7 gate).
# ---------------------------------------------------------------------------------------------------------------------
ISSUER, COURT = "p_npc_020", "off_duke_valorsmark"     # `build_realm(0)`: a holder of `issue` and `determine`; its seat commands the two officers below
OFFICER, THIRD = "p_npc_036", "p_npc_035"              # holders of `dispatch` (`off_royal_marshal`, `off_guard_captain`) that `COURT` commands
PRISONER = "p_npc_075"                                 # an unseated man the court reaches (`may_determine`) and the marshal's seat reaches (`may_warrant`)


def _at_degree(degree, *verbs):
    """`SeasonDriver._contest` with the named verbs folded at `degree` (a `Degree`) through the real `_fold` (the shape of `_seat_at_success.writ_at_success`):
    a test whose question is the act's fold and not its draw. Every other verb is drawn as shipped."""
    from engine.dice_engine.dice_engine import DEGREE_LABEL
    from ..seam import Resolution
    drawn = SeasonDriver._contest

    def at_degree(self, w, token, a, contests, contest_max_depth, host=None):
        if a.verb in verbs:
            return self._fold(w, token, a, Resolution(DEGREE_LABEL[degree], {}))
        return drawn(self, w, token, a, contests, contest_max_depth, host)
    return at_degree


def _at_success(*verbs):
    from engine.dice_engine.dice_engine import Degree
    return _at_degree(Degree.SUCCESS, *verbs)


def _act_of(w, who, cand):
    """The one Act the real packer makes of the Candidate `cand` of `who` (no hand-built act: `pack_scenes`, the chooser's own packer), run now (`after` cleared)."""
    from ..decision.choose import pack_scenes
    from ..state.ids import H
    mint = lambda p, verb, subj: H(w.world_seed, w.tick, p, f"act:{verb}:{subj}")
    (act,) = [a for sc in pack_scenes(w.persons[who], [cand], 99, w.fixtures, mint) for a in sc.acts]
    act.after = None
    return act


def _warrant_world(to, monkeypatch):
    """`build_realm(0)` with the court's holder having ISSUED, through the real fold (`SeasonDriver.resolve`, then `witness`), a
    dispensation naming `PRISONER` and addressed `to`. PLANTED, and only these: the issuer knows the prisoner (the `terms` conjunct of
    `issue`), the officer and the third man stand where the issuer stands (the realm seats nobody beside the seat that commands him: the
    audit's "co-located with the issuer"), and `issue`'s own draw is folded at Success. Everything after this is the shipped game."""
    from ..boot.realm import build_realm
    from ..data.matrix import WriteClass
    from ..loop.driver import mint_token
    from ..state.carriers import Act, Tenure
    w = build_realm(0)
    d = SeasonDriver(w)
    here = world_q.place_of(w, ISSUER)
    for who in (OFFICER, THIRD):
        for t in w.tenures:
            if t.subject == who and t.kind == "contain" and t.until is None:
                t.until = w.tick
        w.add_tenure(Tenure(f"t_plant_at_court_{who}", who, here, "contain", since=w.tick))
    w.persons[ISSUER].ledger.append(Claim("c_vm_phy_a_knows", ISSUER, PRISONER, "exists:Person", 1, w.tick, "firsthand", 100, "own"))
    with monkeypatch.context() as m:
        m.setattr(SeasonDriver, "_contest", _at_success("issue"))
        out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="a_vm_phy_a_w", actor=ISSUER, verb="issue", via=COURT,
                                                            payload={"subject": PRISONER, "to": to})],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["dispensation.issued"], [e.kind for e in out]
    w.log.extend(out)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return w, d


def test_arrest_on_an_addressed_and_heard_warrant(monkeypatch):
    """The audit's §1.7 gate, A1. A court seat issues a dispensation naming a man, addressed to an officer who stood by; the officer holds
    no copy (the Record stays in the issuer's hand) and has only heard it. (1) His opening set, on the questions the world puts to him,
    holds `arrest` on that man and on no other. (2) The Candidate so formed, folded at Success (the draw pinned so a refusal is the
    write clause's and never a lost roll), is `arrest.made` and opens a `detain` on the prisoner. PLANTED FAILURE: `_eff_arrest` reading
    the held half alone (the pre-B29.01 reading) forms the act and the `write` clause refuses it, `arrest.refused`: this fails on that kind.
    (3) The custody is read downstream: the issuing seat's holder forms `interrogate` on the prisoner (`Detainee`). (4) One season through
    `SeasonDriver.season` and the shipped chooser, no hand-built act: any `arrest` the officer attempts ends `arrest.made` or
    `arrest.resisted`, never refused. (At the measured seeds 0-6 the chooser draws none, so this arm observes nothing there.)
    CONTROL: the same world with the warrant addressed to a third man forms no `arrest` for the officer, and does for that man."""
    from ..data.matrix import WriteClass
    from ..data.rosters import DETAIN_KIND
    from ..loop.driver import mint_token
    w, d = _warrant_world(OFFICER, monkeypatch)
    formed = _formed(w, OFFICER, "arrest")
    assert formed and {c.subject for c in formed} == {PRISONER}, formed
    act = _act_of(w, OFFICER, formed[0])
    with monkeypatch.context() as m:
        m.setattr(SeasonDriver, "_contest", _at_success("arrest"))
        out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    assert [e.kind for e in out] == ["arrest.made"], [e.kind for e in out]
    assert world_q.restrained(w, PRISONER, DETAIN_KIND)
    assert PRISONER in {c.subject for c in _formed(w, ISSUER, "interrogate")}
    w2, d2 = _warrant_world(OFFICER, monkeypatch)
    d2.season(P.chooser(w2, verbs=resolvable_verbs()), None, contest_max_depth=w2.fixtures.get("contest_max_depth"))
    assert set(e.kind for e in w2.log if e.id in d2.act_of and d2.act_of[e.id].verb == "arrest"
               and d2.act_of[e.id].actor == OFFICER) <= {"arrest.made", "arrest.resisted"}
    w3, _ = _warrant_world(THIRD, monkeypatch)
    assert _formed(w3, OFFICER, "arrest") == []
    assert {c.subject for c in _formed(w3, THIRD, "arrest")} == {PRISONER}


# ---------------------------------------------------------------------------------------------------------------------
# A2 (B29.02): `capture` FORMS ONLY ON A PERSON UNDER `war` OR `crime`, AND ITS CUSTODY GOES TO THE WARRANT'S COURT (the audit's §2.7 gate).
# ---------------------------------------------------------------------------------------------------------------------
def test_capture_after_a_resisted_arrest_goes_to_the_warrant_court(monkeypatch):
    """The audit's §2.7 gate, A2. §1.7's world, the officer's `arrest` folded at Failure through the real fold (the draw pinned, as the
    A1 test pins Success: a fixture pool of 0 dice leaves the roll to chance, and the question here is the fold's). (1) `arrest.resisted`
    opens no custody. (2) The same officer's next opening set holds `capture` on the man the warrant names and on no stranger (`rosters.yaml:
    violence_contexts`' `capture` line: the `crime` context). (3) A `capture` the real packer makes of that Candidate, its scene pinned to a
    yield by the man (`Untouched`, `surrender.by` = him), opens ONE `detain` to the seat that ISSUED the warrant (`COURT`), not to the seat the
    act is exercised through (`Act.via`, the officer's own). CONTROL: the same world with the warrant addressed to a third man forms no `capture`
    on the prisoner for the officer. PLANTED FAILURE: the `capture` line deleted from `violence_contexts` forms `capture` on strangers
    again (this test then fails on the stranger assertion); `_eff_capture` reading `a.via` alone (as before B29.02) fails (3)."""
    from ..data.matrix import Step, WriteClass
    from ..data.rosters import DETAIN_KIND
    from ..loop import resolve as R
    from ..loop.driver import mint_token
    from ..seam import Resolution
    from ..state.carriers import Tenure
    from engine.dice_engine.dice_engine import Degree
    w, d = _warrant_world(OFFICER, monkeypatch)
    (arrest,) = [c for c in _formed(w, OFFICER, "arrest") if c.subject == PRISONER][:1]
    with monkeypatch.context() as m:
        m.setattr(SeasonDriver, "_contest", _at_degree(Degree.FAILURE, "arrest"))
        out = d.resolve(mint_token(w, WriteClass.ACTS), [_act_of(w, OFFICER, arrest)], contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    assert [e.kind for e in out] == ["arrest.resisted"], [e.kind for e in out]
    assert not world_q.restrained(w, PRISONER, DETAIN_KIND)
    formed = _formed(w, OFFICER, "capture")
    assert formed and {c.subject for c in formed} == {PRISONER}, [(c.subject, c.operands) for c in formed]
    act = _act_of(w, OFFICER, formed[0])
    assert act.via is not None and act.via != COURT, (act.via, COURT)
    here = world_q.place_of(w, OFFICER)                      # PLANTED: a fight needs the man where the officer stands (`capture`'s `with` cell; `arrest` asks no presence)
    for t in w.tenures:
        if t.subject == PRISONER and t.kind == "contain" and t.until is None:
            t.until = w.tick
    w.add_tenure(Tenure("t_plant_at_officer_prisoner", PRISONER, here, "contain", since=w.tick))
    w.step, w.frozen = Step.RESOLVE, False
    scene = {"status": "RESOLVED", "surrender": {"by": PRISONER, "turn": 1, "accepted": True},
             "wound_state": {p: {"available": True, "felled": False, "wounds": 0, "max_wounds": 4, "health_remaining": 10, "health_full": 10}
                             for p in (OFFICER, PRISONER)}}
    out = R._fold(d, w, mint_token(w, WriteClass.ACTS), act, Resolution("Untouched", scene))
    w.log.extend(out)
    assert [e.kind for e in out] == ["person.captured"], [e.kind for e in out]
    (detain,) = [t for t in w.tenures if t.kind == DETAIN_KIND and t.subject == PRISONER and t.live]
    assert detain.object == COURT, (detain.object, act.via)
    w3, _ = _warrant_world(THIRD, monkeypatch)
    assert _formed(w3, OFFICER, "capture") == [], "CONTROL: no warrant to the officer, no `capture` on the man"
