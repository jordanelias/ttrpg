"""CL-THRUST B3.2 (batch B10-09 close two landing) -- R2: a person's `goal_stages` stage adds its referents to the
question he answers THROUGH THE CLASSED STAMPER, and its `pursuits` join the salience target as a goal's own do.

THE BUILD (`world_q.stage_referents`, `open_stages`, and `attention_key`'s `salience`): `current_stage` (B3.1, the person's
own ledger) keys an open stage by a referent of the ambition; `stage_referents` hands those referents, through the SAME
class test a question's own referents meet (`_of_stamped_class`), to `questions_for`'s `_stamped` as the last term of the
splice, so they ride `out[0]` as classed referents whether or not the ambition's `need` question sorts first (it is tier 3).
NOT BUILT: R3' (the pulse) and the stage `deadline` (struck by M20). NO LADDER IS AUTHORED IN `goals.yaml`: the ladder below is
authored here only, through the one seam the B2/B3.1 tests use (`goals.rows_replaced(goals.parse(doc))`).

What each test proves, and the failure that would redden it:

  (a) A STAGE REFERENT RIDES THE QUESTION HE ANSWERS, AS ITS CLASS: out[0] is a claim question about something else
      (the `need` question is tier 3) and carries `(p_a, "Person")`; the same world with no ladder does not. PLANTED
      FAILURE: `stage_referents` stubbed to `()` reddens it (`test_a_stubbed_term_..._reddens_the_stamp`).
  (b) BELIEF, NOT TRUTH: the person whose own ledger holds every stage's claim has no open stage and no stamp; one who
      lacks them has it. `open_stages` reads `current_stage`, person-side.
  (c) THE CLASS TEST IS THE QUESTION'S OWN: a stage referent that no row declares a class for is not stamped.
  (d) THE STAGE'S PURSUITS JOIN THE SALIENCE TARGET: the `need` question's salience moves with the stage's pursuits (and by
      the amount the goal's own pursuits would move it), and does not move with no ladder.
  (e) EQUAL AT EMPTY DATA (TL §3.3 control (a), here `goal_stages: []`): over the seed-0 realm `stage_referents` is `()` for
      every person and `questions_for` is equal with the shipped goals and with the same goals carrying `goal_stages: []`.
      The whole-world hash control is the pins in `test_season_weather.py` / `test_go07_canonical_digest.py`, unmoved.
  (f) THE LADDER REACHES THE SHIPPED REALM, NON-VACUOUSLY: one authored ladder on two shipped `seat_holders` goals, seed 0,
      one season; the stage-referent hit rate is asserted above 0 (its definition is `_hit_rate`'s).
"""
from __future__ import annotations

import copy
from collections import Counter

import pytest
import yaml

from ..data import files, goals
from ..data.requires import binding_of, evaluate
from ..decision import make_chooser, opening_set
from ..harness import populated
from ..harness.corpus_run import attempts
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Claim, Person, Proposition, Tenure
from ..state.ids import H, draw_factory
from ..state.world import World

SEAT = "off_king"
OWN = "thing_own"             # an object of his own live `hold`: a claim about it is a tier-1 question
THRONE = "g_throne"
OTHER = "g_other"                 # a second seat goal, no stage row: the control ambition
S1 = {"form": "existence", "of": "subject", "kind": "Person"}
S2 = {"form": "relation", "of": "subject", "relation": "held_by"}


def _goal(gid, org, obj, **more):
    return {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_cl_thrust_b32", **more}


def _stage(sid, term, cell, pursuits=None):
    return {"id": sid, "term": term, "predicate": copy.deepcopy(cell),
            "pursuits": {"honour": 1} if pursuits is None else pursuits}


def _doc(*, with_row=True, pursuits=None) -> dict:
    doc = {"goals": [_goal(THRONE, {"faction": "Crown"}, {"kind": "seat_holders", "seats": [SEAT]}, stance=1),
                     _goal(OTHER, {"faction": "Hafenmark"}, {"kind": "rung", "rung": "terr_T9"})]}
    if with_row:
        doc["goal_stages"] = [{"id": "gs_throne", "for": [THRONE],
                               "stages": [_stage("s1", "short", S1, pursuits), _stage("s2", "long", S2, pursuits)]}]
    return doc


@pytest.fixture
def staged():
    with goals.rows_replaced(goals.parse(_doc())):
        yield


@pytest.fixture
def unstaged():
    with goals.rows_replaced(goals.parse(_doc(with_row=False))):
        yield


def _claim(cid, holder, subject, predicate, value=True, when=0) -> Claim:
    return Claim(cid, holder, subject, predicate, value, when, "firsthand", 100, "own")


def _world(ledger, holders=("p_a",), pursuits=None):
    """`p_o` is committed to the OUGHT `THRONE`, holds `ledger`, and holds `OWN` (so a claim about it is a
    tier-1 question, which sorts ahead of his tier-3 `need` question); `holders` sit on the throne's seat."""
    w = World(0)
    w.propositions[THRONE] = Proposition(THRONE, "OUGHT", "subj_" + THRONE, f"{THRONE} ought", True, 0)
    for pid in dict.fromkeys(list(holders) + ["p_o"]):
        w.persons[pid] = Person(pid, pid)
    for i, h in enumerate(holders):
        w.persons[h].tenures.append(Tenure(f"t_hold_{h}", h, SEAT, "hold", i))
    o = w.persons["p_o"]
    o.tenures.append(Tenure("t_commit_p_o", "p_o", THRONE, "commit", 0))
    o.tenures.append(Tenure("t_hold_own", "p_o", OWN, "hold", 0))
    o.ledger = list(ledger) + [_claim("c_own_seat", "p_o", OWN, "office.changed")]
    if pursuits:
        o.pursuits = dict(pursuits)
    return w


def _answered(w):
    return world_q.questions_for(w, w.persons["p_o"])


def _classed(q) -> set:
    return set(q.classes)


# ---------------------------------------------------------------------------------------------------
# (a) a stage referent rides the question he answers, as its class
# ---------------------------------------------------------------------------------------------------

def test_a_stage_referent_rides_the_question_he_answers_as_a_classed_referent(staged):
    w = _world([])
    qs = _answered(w)
    assert [q.source for q in qs][0] == "claim_landed" and qs[1].source == "need", \
        "the own-seat claim (tier 1) sorts ahead of the need question (tier 3): the case this term exists for"
    assert qs[1].referents == ("p_a",), "the need question's plain referents already name the holder"
    assert ("p_a", "Person") in _classed(qs[0]), "and the stage referent is stamped on the question he answers"
    assert "p_a" not in qs[0].referents, "stamped as a class, the plain referents untouched"
    assert world_q.stage_referents(w, w.persons["p_o"]) == ("p_a",)


def test_with_no_ladder_the_same_world_stamps_no_stage_referent(unstaged):
    w = _world([])
    qs = _answered(w)
    assert qs[0].source == "claim_landed"
    assert ("p_a", "Person") not in _classed(qs[0]) and world_q.stage_referents(w, w.persons["p_o"]) == ()


def test_a_stubbed_term_reads_no_stamp_and_the_new_test_reddens(staged, monkeypatch):
    """THE PLANTED FAILURE: the term stubbed to return nothing. The (a) assertion then fails -- run here as the
    inverse (the stamp is absent), so the failure is OBSERVED in the suite and not only by hand."""
    monkeypatch.setattr(world_q, "stage_referents", lambda w, p, ambs=None: ())
    qs = _answered(_world([]))
    assert ("p_a", "Person") not in _classed(qs[0])


# ---------------------------------------------------------------------------------------------------
# (b) belief, not truth
# ---------------------------------------------------------------------------------------------------

def _passing(referent="p_a", pid="p_o"):
    return [_claim("c_s1", pid, referent, "exists:Person"), _claim("c_s2", pid, referent, f"held_by:{pid}")]


def test_a_person_whose_own_ledger_passes_every_stage_has_no_open_stage_and_no_stamp(staged):
    w = _world(_passing())
    assert world_q.current_stage(w, w.persons["p_o"], THRONE) is None
    assert world_q.stage_referents(w, w.persons["p_o"]) == ()
    assert ("p_a", "Person") not in _classed(_answered(w)[0])


def test_a_person_who_has_passed_the_first_stage_only_is_still_stamped_on_the_second(staged):
    w = _world(_passing()[:1])
    assert {r: s.id for r, s in world_q.open_stages(w, w.persons["p_o"], THRONE).items()} == {"p_a": "s2"}
    assert ("p_a", "Person") in _classed(_answered(w)[0])


# ---------------------------------------------------------------------------------------------------
# (c) the class test is the question's own
# ---------------------------------------------------------------------------------------------------

def test_a_stage_referent_no_row_declares_a_class_for_is_not_stamped(staged):
    """A referent whose collection no verb row declares (`World.class_of` is `None`: an id the world does not hold) is
    dropped by the one class test `own_referents_of_class` uses, so no unclassed id reaches a classed verb."""
    w = _world([], holders=("p_a",))
    assert world_q._of_stamped_class(w, ("p_a", "p_nobody")) == ("p_a",)
    assert world_q.own_referents_of_class(w, world_q.Question("q:x", "need", ("p_a", "p_nobody"), "x")) == ("p_a",)


# ---------------------------------------------------------------------------------------------------
# (d) the stage's pursuits join the salience target
# ---------------------------------------------------------------------------------------------------

def _need_salience(w) -> float:
    p = w.persons["p_o"]
    key = world_q.attention_key(w, p)
    need = next(q for q in _answered(w) if q.source == "need")
    return -key(need)[1]


def test_the_stage_pursuits_join_the_salience_target_as_the_goals_own_do():
    """`p_o` points at honour; the goal weighs stability only. A stage weighing honour pulls the target toward him, so
    the salience of the need question rises with the ladder, and does not with no ladder (the control)."""
    mine = {"honour": 1}
    with goals.rows_replaced(goals.parse(_doc(with_row=False))):
        base = _need_salience(_world([], pursuits=mine))
    with goals.rows_replaced(goals.parse(_doc(pursuits={"honour": 3}))):
        lifted = _need_salience(_world([], pursuits=mine))
    with goals.rows_replaced(goals.parse(_doc(pursuits={"stability": 3}))):
        same_axis = _need_salience(_world([], pursuits=mine))
    assert lifted > base, (lifted, base)
    assert same_axis <= base, "a stage weighing what he does not point at does not raise it (the control, other way)"
    with goals.rows_replaced(goals.parse(_doc(pursuits={"honour": 3}))):
        done = _need_salience(_world(_passing(), pursuits=mine))
    assert done == base, "a stage he has passed weighs nothing"


# ---------------------------------------------------------------------------------------------------
# (e) equal at empty data
# ---------------------------------------------------------------------------------------------------

def test_with_goal_stages_empty_the_realm_stamps_nothing_and_its_questions_are_equal():
    raw = yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))
    assert "goal_stages" not in raw
    w = populated.build_realm(0)
    shipped = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    explicit = copy.deepcopy(raw)
    explicit["goal_stages"] = []
    with goals.rows_replaced(goals.parse(explicit)):
        again = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    committed = [p for p in w.persons.values() if world_q.ambitions(w, p)]
    assert len(committed) >= 40, "the loop must have looked at the committed persons"
    assert all(world_q.stage_referents(w, p) == () for p in w.persons.values())
    assert shipped == again


# ---------------------------------------------------------------------------------------------------
# (f) the ladder reaches the shipped realm; the stage-referent hit rate
# ---------------------------------------------------------------------------------------------------

LADDER_GOALS = ["goal_crown_peninsular_sovereignty", "goal_church_suppress_restoration"]


def authored_realm_doc() -> dict:
    """The shipped goals plus ONE authored ladder, in the doc only (never in `goals.yaml`): a stage a person's own claims
    must answer on the referent (a Person exists, in his ledger) and then one that asks he hold it."""
    doc = yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))
    doc["goal_stages"] = [{"id": "gs_b32_test", "for": list(LADDER_GOALS),
                           "stages": [_stage("s1", "short", S1), _stage("s2", "long", S2, {"honour": 1, "stability": 1})]}]
    return doc


def _open_refs(w, p) -> tuple:
    """The referents of `p`'s open stages that `stage_referents` would stamp, read from `open_stages` and NOT through
    `stage_referents`, so the measurement still names them when a control stubs the term."""
    out: list = []
    for pid in world_q.ambitions(w, p):
        out.extend(r for r in world_q.open_stages(w, p, pid) if r not in out)
    return world_q._of_stamped_class(w, tuple(out))


def stage_run(w, seasons: int) -> dict:
    """`populated.run`'s construction (`harness/populated.py::run`), the chooser WATCHED and never steered.

    STAGE-REFERENT HIT RATE (TL §8 B0.2's definition, adapted: R3' is not built, so no `need` question is PROMOTED; the
    unit here is a DELIBERATION in which the question the person was handed carries one of his open-stage referents).
    Of those deliberations (`stage`): `formed` = a candidate formed whose subject is a stage referent; `hit` = formed AND an
    act by that person naming a stage referent as its subject executed (`corpus_run.attempts`: a made kind, not a refusal;
    matched by (actor, subject), so a later season's act counts for an earlier deliberation: stated, not corrected)."""
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    deliberations = 0
    seen: list = []                           # (pid, stage referents, formed)

    def watched(p, v, s, ask_budget):
        nonlocal deliberations
        deliberations += 1
        q = getattr(v, "question", None)
        refs = set(_open_refs(w, p))
        if refs and q is not None and refs & (set(q.referents) | {o for o, _ in q.classes}):
            cands = opening_set(p, v, q, w.fixtures)
            seen.append((p.id, frozenset(refs), any(c.subject in refs for c in cands)))
        return real(p, v, s, ask_budget)

    for _ in range(seasons):
        d.season(watched, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    made, refused = Counter(), Counter()
    for a, ok, no in attempts(w, seasons):
        subj = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
        for key, bucket in ((ok, made), (no, refused)):
            if key:
                bucket[(a.actor, subj)] += 1
    hit = sum(1 for pid, refs, formed in seen if formed and any(made[(pid, r)] for r in refs))
    return {"deliberations": deliberations, "stage": len(seen), "formed": sum(1 for *_, f in seen if f), "hit": hit,
            "made": made, "refused": refused, "told": sum(1 for e in w.log if e.kind == "news.told"),
            "hash": w.content_hash()}


@pytest.fixture(scope="module")
def ladder_run():
    with goals.rows_replaced(goals.parse(authored_realm_doc())):
        w = populated.build_realm(0)
        yield stage_run(w, 1)


def test_the_authored_ladder_reaches_the_realm_and_its_stage_referent_hit_rate_is_above_zero(ladder_run):
    r = ladder_run
    assert r["stage"] >= 1, "some deliberation was handed a question carrying a stage referent: the stamp reaches"
    assert r["formed"] >= 1, "and a candidate formed on one"
    assert r["hit"] > 0, ("hit rate 0 on the authored ladder: the stamper does not reach an executed act "
                          f"(stage {r['stage']}, formed {r['formed']}, refusals {dict(r['refused'])})")
    print(f"\nstage-referent hit rate: {r['hit']}/{r['stage']} stage deliberations "
          f"({r['formed']} formed a candidate), over {r['deliberations']} deliberations; refusals {dict(r['refused'])}")
