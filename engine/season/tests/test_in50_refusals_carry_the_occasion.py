"""IN-50 -- A REFUSED ACT CITES WHAT OCCASIONED IT, because `_act_events` is the one emission owner.

`loop/resolve.py::_fold`'s success return added `self._occasion_ids(w, a)` to `causes[]` and every
refusal return stamped `[a.id]` alone, so an act chosen from a scene another person's act-Event
occasioned dropped that edge the moment it was refused. The rule now lives once, in
`_act_events(self, w, a, kinds, ...)`, and the three refusals that built `Event` directly
go through it. This file is the counterfactual: each refusal route is driven with an occasion
present, and the same route with the append neutered fails (run once, 2026-10-09, IN-50: the
count is in the commit and in `engine/season/requirements.yaml` R-01's `measured:`).

What each test observes, and the control that stops it passing vacuously:

  1-4. THE FOUR REFUSAL ROUTES that did not append: `_survives`' `act.ineligible`; the S27.4
       `attempt.refused`; the contest branch's `_admits` refusal; `_refuse_party_gap`.
  5.   THE FOLD'S OWN REFUSAL (`_fold`'s `ev` through `_admits`) -- the route that already went
       through `_act_events` and so already named the occasion only on success.
  6.   THE NO-SCENE CONTROL: an act with no scene has no occasion and keeps `[a.id]` alone on every
       route -- and so does an act whose scene carries `occasion=None` or a `need` question -- so
       the append is not padding every `causes[]` (over-citation scores R3 for free).
  7.   `_act_events` ASKED DIRECTLY: the act then the occasion, and one independent list per Event.
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


def _over_attempt(w, act_id, **kw):
    """A `work` whose obstacle is past the refusal multiple of its pool: the S27.4 `attempt.refused`."""
    a = Act(id=act_id, actor=ACTOR, verb="work", **kw)
    a.obstacle, a.pool = w.fixtures.get("obstacle_refusal_multiple") * 10 + 1, 1
    return a


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
    a = _over_attempt(w, "a_over", scene=SCENE)
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
    # RE-PINNED AT v9 IN-13: an unheld settlement (`set_s_037`) now ARRIVES (`Unopposed`), so the
    # party gap is reached by H-149's route instead -- a HEARTH target musters an empty army
    # (`sides_of`: `claimants=[]`), `_contest`'s empty-`_parties` check (BEFORE the provider is
    # reached) answers PARTY-GAP and `_refuse_party_gap` emits
    # (test_march.py, `test_a_march_on_a_non_settlement_rung_refuses_h149_is_enforced`).
    a = Act(id="a_march", actor=ACTOR, verb="march", payload={"subject": "b_s_014_barracks"},
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
    over = _over_attempt(w, "a_bare_over")
    # A SCENE THAT EXISTS AND CARRIES NO OCCASION (`occasion=None`), and one whose occasion is a
    # `need` Question about the same claim the occasioned fixture's question names: `occasioned_by`
    # returns nothing for either, so the act keeps `[a.id]` -- the scene's presence alone adds nothing.
    d.scenes["sc_in50_none"] = Scene("sc_in50_none", ACTOR, [], occasion=None)
    d.scenes["sc_in50_need"] = Scene("sc_in50_need", ACTOR, [],
                                     occasion=Question("q_in50_need", "need", (), about="claim_in50"))
    no_occ = Act(id="a_no_occ", actor="p_removed", verb="work", scene="sc_in50_none")
    need = Act(id="a_need", actor="p_removed", verb="work", scene="sc_in50_need")
    checked = 0
    for a, out in ((bare, d._survives(w, bare)), (unknown, d._survives(w, unknown)),
                   (over, [e for e in _resolve(w, d, over) if e.kind == "attempt.refused"]),
                   (no_occ, d._survives(w, no_occ)), (need, d._survives(w, need))):
        assert out, a.id
        for e in out:
            assert e.causes == [a.id], f"{e.kind} cites {e.causes}: an act with no occasion got one"
            checked += 1
    assert checked >= 5


# -- 7 ---------------------------------------------------------------------------------------------
def test_in50_act_events_cites_the_act_then_the_occasion_one_list_per_event():
    w, d, occ = _world_with_occasion()
    a = Act(id="a_direct", actor=ACTOR, verb="work", scene=SCENE)
    # TWO DECLARED KINDS (`rosters.yaml: fold_kinds`): since SC-02 `23` the fold refuses a kind no
    # emission column declares (loader invariant 7), so the made-up `k.one`/`k.two` this used to pass
    # are refused -- `test_sc02_typed_ids_and_loader.py` plants exactly that.
    out = _act_events(d, w, a, ("act.refused", "act.ineligible"))
    assert [e.kind for e in out] == ["act.refused", "act.ineligible"]
    assert [e.causes for e in out] == [[a.id, occ]] * 2, [e.causes for e in out]
    assert out[0].causes is not out[1].causes, "two Events share one causes list"
    assert out[0].id == H(w.world_seed, w.tick, a.actor, f"act.refused:{a.id}"), "the id scheme moved"


# -- 8 ---------------------------------------------------------------------------------------------
def _play(case):
    case = C.apply_rescale(case)             # `run_case`'s own first step
    w = C.build_at(case, 0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(C.seasons_for(case)):
        d.season(ch, question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def _cross_person_refusals(w, d):
    """Refusals only: a kind on the row's `emits_on_refusal:` and NOT on its `emits:` (the test
    `loop/witness.py::_happened` applies), so a graded loss on both columns (`tell`'s
    `news.untold`) is not counted and restoring the occasion on the success path alone fails here."""
    n = 0
    for e in w.log:
        a = d.act_of.get(e.id)
        row = VERB_TABLE.get(a.verb) if a is not None else None
        if row is None:
            continue
        refusal = (set(row.emits_on_refusal or ()) | {"act.refused"}) - set(row.emits or ())
        if e.kind not in refusal:
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


# -- REM-13 ----------------------------------------------------------------------------------------
# `corpus_run`'s degrees BY VERB, the bands that differ, and the emission-only class. Planted worlds
# and planted rows only: no count of a corpus run is asserted (V2), so each reading is a reader that
# can be wrong and not a pin that can be re-recorded.

def _tell_and_research(n):
    """`tiny_world` with a `Record`, ONE `resolve` of a `tell` (to `p_mid`) and a `research`, both
    through `d.resolve`, so `d.act_of` holds both acts (a bare `_fold` leaves it empty). Act ids are
    swept by the caller until the seam draws the bands it needs."""
    from engine.season.state.carriers import Claim, Said
    from engine.season.tests.test_fi01_graded_inquiries import REC
    from engine.season.tests.test_fi01_graded_inquiries import _resolve as fi_resolve
    from engine.season.tests.test_fi01_graded_inquiries import _world as fi_world
    w, d = fi_world()
    w.persons["p_low"].ledger.append(Claim("c_rem13", "p_low", "Hh", "stores:grain", 8, 0,
                                           "firsthand", 37, "own"))
    fi_resolve(w, d,
               Act(id=f"a_rem13_tell_{n}", actor="p_low", verb="tell",
                   payload={"subject": "Hh", "to": "p_mid",
                            "said": Said("Hh", "stores:grain", 8, 37, ())}),
               Act(id=f"a_rem13_res_{n}", actor="p_low", verb="research", payload={"subject": REC}))
    return w, d


def _lost_tell_beside_a_found_research():
    """The planted two-verb world: `tell` graded Failure, `research` graded something else."""
    for n in range(120):
        w, d = _tell_and_research(n)
        bands = {e.kind: e.degree for e in w.log if e.degree}
        if bands.get("news.untold") == "Failure" and bands.get("finding.made") not in (None, "Failure"):
            return w, d
    raise AssertionError("120 act ids never drew a lost tell beside a found research")


def test_rem13_a_lost_tell_is_credited_to_tell_alone():
    """A `tell` that grades Failure beside a `research` that does not: `tell` carries the Failure and
    `research` carries none. The sum control is the same world's unkeyed total.

    MUTATION (run 2026-10-26, reverted): every degree credited to one verb (`verb = "tell"`) -- the
    `research` assertions red; the verb key dropped (`verb = NO_ACT`) -- the `tell` one reds."""
    w, d = _lost_tell_beside_a_found_research()
    by = C.degrees_by_verb(w.log, d.act_of)
    assert set(by) == {"tell", "research"}, by
    assert by["tell"] == {"Failure": 1}, by
    assert "Failure" not in by["research"] and sum(by["research"].values()) == 1, by
    # THE CONTROL: the per-verb totals sum to the old unkeyed total, degree by degree
    total = C.Counter(str(e.degree) for e in w.log if getattr(e, "degree", None))
    summed = C.Counter()
    for ds in by.values():
        summed.update(ds)
    assert summed == total and sum(total.values()) == 2, (summed, total)


def test_rem13_a_graded_event_whose_act_is_unknown_is_credited_to_no_act_not_dropped():
    """The sum control cannot fail by a drop: an Event the `act_of` map does not hold lands in
    `NO_ACT`, so the per-verb total still equals the unkeyed one."""
    w, d = _lost_tell_beside_a_found_research()
    by = C.degrees_by_verb(w.log, {})
    assert set(by) == {C.NO_ACT} and sum(by[C.NO_ACT].values()) == 2, by


def test_rem13_run_case_carries_the_per_verb_table_and_it_sums_to_the_total():
    """On a REAL `run_case`, for each of the two named corpus cases: `degrees_by_verb` sums to
    `degrees` degree by degree. `checked` guards against a loop that read nothing."""
    wanted = {"ARC-23", "NPC-090"}
    cases = [(lane, c) for lane in ("ARC", "NPC") for c in R.load_cases(lane) if c["id"] in wanted]
    assert {c["id"] for _, c in cases} == wanted, "a named corpus case is gone; re-pick the cases"
    checked = 0
    for lane, c in cases:
        row = C.run_case(c, 0, lane)
        assert "degrees_by_verb" in row, row.keys()
        summed = C.Counter()
        for ds in row["degrees_by_verb"].values():
            summed.update(ds)
        assert dict(summed) == row["degrees"], (c["id"], dict(summed), row["degrees"])
        checked += sum(summed.values())
    assert checked >= 1, "neither case completed a contest: the sum control was vacuous"


def _planted_row(**kw):
    import dataclasses
    base = VERB_TABLE["tell"]
    return dataclasses.replace(base, **kw)


def test_rem13_bands_that_differ_reads_true_for_a_planted_row_whose_bands_differ():
    """A planted contested row with two different `writes_at` bands prints True; the same row with
    every band alike prints False (so the reader can say both); an uncontested row is not listed."""
    differ = _planted_row(verb="zz_differ", writes_by_degree={
        "Success": ["Person.pursuits"], "Failure": []})
    alike = _planted_row(verb="zz_alike", writes_by_degree={"Success": [], "Failure": []})
    flat = _planted_row(verb="zz_flat", writes_by_degree={}, contests="", writes=())
    out = C.bands_that_differ({"zz_differ": differ, "zz_alike": alike, "zz_flat": flat})
    assert out == {"zz_differ": True, "zz_alike": False}, out
    # and over the real table: exactly the degree-keyed rows are listed, each a bool
    real = C.bands_that_differ()
    assert set(real) == {v for v, r in VERB_TABLE.items() if r.writes_by_degree}
    assert all(isinstance(x, bool) for x in real.values())


def test_rem13_emits_and_writes_nothing_tags_the_ruled_and_leaves_the_rest_untagged():
    """Planted rows: one emitting and writing nothing with a ruling -> `deposit-only by ruling`;
    one without a ruling -> `untagged`; a writing row, a row with an effect body, and a row emitting
    nothing are not listed."""
    quiet = dict(writes=(), writes_by_degree={}, contests="", emits=("x.made",), emits_by_degree={})
    rows = {
        "zz_ruled": _planted_row(verb="zz_ruled", **quiet),
        "zz_bare": _planted_row(verb="zz_bare", **quiet),
        "zz_writes": _planted_row(verb="zz_writes", **{**quiet, "writes": ("Person.pursuits",)}),
        "zz_effect": _planted_row(verb="zz_effect", **quiet),
        "zz_mute": _planted_row(verb="zz_mute", **{**quiet, "emits": ()}),
        "zz_bands": _planted_row(verb="zz_bands", writes=("Person.pursuits",), emits=("x.made",),
                                 contests="", emits_by_degree={},
                                 writes_by_degree={"Success": ["Person.pursuits"], "Failure": []}),
    }
    out = C.emits_and_writes_nothing(rows, effects={"zz_effect": object()},
                                     rulings={"zz_ruled": "planted"})
    assert out == {"zz_ruled": "deposit-only by ruling", "zz_bare": "untagged"}, out
    # the default rulings are the code's: `tell` and the graded inquiries, read from the roster
    assert C.deposit_only_rulings()["tell"] == "G1"
    assert set(C.deposit_only_rulings()) - {"tell"} == set(C.GRADED_INQUIRIES)
