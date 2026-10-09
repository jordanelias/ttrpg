"""IN-50 -- A REFUSED ACT CITES WHAT OCCASIONED IT, because `_act_events` is the one emission owner.

`loop/resolve.py::_fold`'s success return added `self._occasion_ids(w, a)` to `causes[]` and every
refusal return stamped `[a.id]` alone, so an act chosen from a scene another person's act-Event
occasioned dropped that edge the moment it was refused. The rule now lives once, in
`_act_events(self, w, a, kinds, causes, ...)`, and the three refusals that built `Event` directly
go through it. This file is the counterfactual: each refusal route is driven with an occasion
present, and the same route with the append neutered fails (run once, 2026-10-09, IN-50: the
count is in the commit and in `engine/season/requirements.yaml` R-01's `measured:`).

What each test observes, and the control that stops it passing vacuously:

  1-4. THE FOUR REFUSAL ROUTES that did not append: `_survives`' `act.ineligible`; the S27.4
       `attempt.refused`; the contest branch's `_admits` refusal; `_party_gap_refusal`.
  5.   THE FOLD'S OWN REFUSAL (`_fold`'s `ev` through `_admits`) -- the route that already went
       through `_act_events` and so already named the occasion only on success.
  6.   THE NO-SCENE CONTROL: an act with no scene has no occasion and keeps `[a.id]` alone on every
       route, so the append is not padding every `causes[]` (over-citation scores R3 for free).
  7.   `_act_events` ASKED DIRECTLY: order, de-duplication, the caller's list unmutated, and one
       independent list per Event.
  8.   A REAL RUN over two corpus cases: refusals in a played-out case carry an edge to ANOTHER
       person's act-Event, and `_r3_propagates` reads True.
"""

from engine.season.data.matrix import Step, WriteClass
from engine.season.decision import make_chooser
from engine.season.harness import corpus_run as C
from engine.season.harness import run_cases as R
from engine.season.harness.populated import build_realm
from engine.season.data.verbs import VERB_TABLE
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.loop.resolve import _act_events
from engine.season.state.carriers import Act, Event, Question, Scene, StateChange
from engine.season.state.ids import H, ROOT, draw_factory

ACTOR = "p_npc_033"          # Crown, seated in `build_realm(0)` (test_march.py's attacker)
SCENE = "sc_in50"


def _world_with_occasion(scene_actor=ACTOR):
    """`build_realm(0)`, a driver, and ONE real occasion: an origin Event in the log, a
    `claim.deposited` Event about it, a `claim_landed` Question naming the deposit's claim, and a
    Scene carrying that Question -- so `occasioned_by` returns exactly `[origin.id]`, by the
    production route and not by a stub."""
    w = build_realm(0)
    d = SeasonDriver(w)
    origin = Event("ev_in50_origin", "speech.made", [], [ROOT], w.tick)
    deposit = Event("ev_in50_deposit", "claim.deposited",
                    [StateChange("claim_in50", "set", "Act")], [origin.id], w.tick)
    w.log.append(origin)
    w.log.append(deposit)
    q = Question("q_in50", "claim_landed", (), about="claim_in50")
    d.scenes[SCENE] = Scene(SCENE, scene_actor, [], occasion=q)
    return w, d, origin.id


def _resolve(w, d, act, depth=2):
    w.step = Step.RESOLVE
    w.frozen = False
    return d.resolve(mint_token(w, WriteClass.ACTS), [act], depth)


def _check_route(events, act, occasion, kinds):
    """Every Event the route emitted names the act FIRST and then the occasion, once each."""
    assert events, "the route emitted nothing; the fixture no longer reaches it"
    assert {e.kind for e in events} <= set(kinds), (kinds, [e.kind for e in events])
    for e in events:
        assert e.causes == [act.id, occasion], (
            f"{e.kind} cites {e.causes}; a refused act chosen from an occasioned scene must cite "
            f"[its own id, the occasion {occasion}]")


# -- 1 ---------------------------------------------------------------------------------------------
def test_in50_route_1_act_ineligible_cites_the_occasion():
    w, d, occ = _world_with_occasion()
    a = Act(id="a_gone", actor="p_removed", verb="work", scene=SCENE)
    assert a.actor not in w.persons
    out = d._survives(w, a)
    _check_route(out, a, occ, ("act.ineligible",))


# -- 2 ---------------------------------------------------------------------------------------------
def test_in50_route_2_attempt_refused_cites_the_occasion():
    w, d, occ = _world_with_occasion()
    a = Act(id="a_over", actor=ACTOR, verb="work", scene=SCENE)
    a.obstacle, a.pool = w.fixtures.get("obstacle_refusal_multiple") * 10 + 1, 1
    out = _resolve(w, d, a)
    _check_route([e for e in out if e.kind == "attempt.refused"], a, occ, ("attempt.refused",))


# -- 3 ---------------------------------------------------------------------------------------------
def test_in50_route_3_the_contest_branchs_admits_refusal_cites_the_occasion():
    w, d, occ = _world_with_occasion()
    # `fight` contests "the body" and its precondition is `the subject is a living person`; a
    # subject who is no person is refused by `_admits` BEFORE the seam, at the contest branch.
    a = Act(id="a_fight", actor=ACTOR, verb="fight", payload={"subject": "no_such_person"},
            scene=SCENE)
    out = _resolve(w, d, a)
    assert not any(e.kind == "person.died" for e in out), "the fight ran; this is not a refusal"
    _check_route(out, a, occ, {e.kind for e in out})
    assert all(e.kind.endswith(".refused") for e in out), [e.kind for e in out]


# -- 4 ---------------------------------------------------------------------------------------------
def test_in50_route_4_party_gap_refusal_cites_the_occasion():
    w, d, occ = _world_with_occasion()
    # `set_s_037` is `build_realm(0)`'s one settlement with no held ancestor: `sides_of` returns
    # `subject=None`, the wrapper reports PARTY-GAP and `_party_gap_refusal` emits (test_march.py).
    a = Act(id="a_march", actor=ACTOR, verb="march", payload={"subject": "set_s_037"},
            via="off_npc_033", scene=SCENE)
    # `march` defers its contest to ENCOUNTER (test_march.py `_fold_one`), which is where it refuses.
    out = _resolve(w, d, a)
    out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, 2)
    refused = [e for e in out if e.kind == "march.refused"]
    _check_route(refused, a, occ, ("march.refused",))


# -- 5 ---------------------------------------------------------------------------------------------
def test_in50_route_5_the_folds_own_refusal_cites_the_occasion():
    w, d, occ = _world_with_occasion()
    # `issue` is eligible only through `remit:issue`; a person who exercises no seat is refused by
    # `_admits` inside `_fold`, whose `ev` is `_act_events` with the verdict bound.
    a = Act(id="a_issue", actor=ACTOR, verb="issue", payload={}, scene=SCENE)
    out = _resolve(w, d, a)
    refusals = [e for e in out if e.kind.endswith((".refused", ".unauthorized", ".ineligible"))]
    _check_route(refusals, a, occ, {e.kind for e in refusals})


# -- 6 ---------------------------------------------------------------------------------------------
def test_in50_control_an_act_with_no_scene_keeps_its_own_id_alone():
    w, d, _occ = _world_with_occasion()
    bare = Act(id="a_bare", actor="p_removed", verb="work")                  # no scene at all
    unknown = Act(id="a_unknown", actor="p_removed", verb="work", scene="sc_nowhere")
    over = Act(id="a_bare_over", actor=ACTOR, verb="work")
    over.obstacle, over.pool = w.fixtures.get("obstacle_refusal_multiple") * 10 + 1, 1
    checked = 0
    for a, out in ((bare, d._survives(w, bare)), (unknown, d._survives(w, unknown)),
                   (over, [e for e in _resolve(w, d, over) if e.kind == "attempt.refused"])):
        assert out, a.id
        for e in out:
            assert e.causes == [a.id], f"{e.kind} cites {e.causes}: an act with no occasion got one"
            checked += 1
    assert checked >= 3


# -- 7 ---------------------------------------------------------------------------------------------
def test_in50_act_events_appends_dedupes_and_leaves_the_callers_list_alone():
    w, d, occ = _world_with_occasion()
    a = Act(id="a_direct", actor=ACTOR, verb="work", scene=SCENE)
    given = [a.id, occ, a.id]                       # the occasion already present, the act twice
    out = _act_events(d, w, a, ("k.one", "k.two"), given)
    assert given == [a.id, occ, a.id], "the caller's causes list was mutated"
    assert [e.kind for e in out] == ["k.one", "k.two"]
    assert [e.causes for e in out] == [[a.id, occ]] * 2, [e.causes for e in out]
    assert out[0].causes is not out[1].causes, "two Events share one causes list"
    assert out[0].id == H(w.world_seed, w.tick, a.actor, f"k.one:{a.id}"), "the id scheme moved"
    again = _act_events(d, w, a, ("k.one",), [a.id])
    assert again[0].causes == [a.id, occ], "the occasion was not appended to a bare [a.id]"


# -- 8 ---------------------------------------------------------------------------------------------
def _play(case):
    case = C.apply_rescale(case)             # `run_case`'s own first step
    w = C.build_at(case, 0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(C.seasons_for(case)):
        d.season(ch, question=None, subsistence=C.P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def _cross_person_refusals(w, d):
    n = 0
    for e in w.log:
        a = d.act_of.get(e.id)
        row = VERB_TABLE.get(a.verb) if a is not None else None
        if row is None or e.kind not in (set(row.emits_on_refusal or ()) | {"act.refused"}):
            continue
        n += any(d.act_of.get(c) is not None and d.act_of[c].actor != a.actor
                 for c in e.causes if c != a.id)
    return n


def test_in50_real_run_refusals_cite_another_persons_act_and_r3_holds():
    wanted = {"ARC-23", "NPC-090"}
    cases = [c for lane in ("ARC", "NPC") for c in R.load_cases(lane) if c["id"] in wanted]
    assert {c["id"] for c in cases} == wanted, "a named corpus case is gone; re-pick the cases"
    total = 0
    for case in cases:
        w, d = _play(case)
        seen = _cross_person_refusals(w, d)
        assert seen >= 1, (f"{case['id']}: no refusal cites another person's act-Event -- "
                           "refused acts are dropping their occasion again")
        assert C._r3_propagates(w, d), f"{case['id']}: R3 reads False"
        total += seen
    assert total >= 2
