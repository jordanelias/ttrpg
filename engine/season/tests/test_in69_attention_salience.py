"""v9 IN-69 (`workplans/valoria_master_workplan_v9_part5.md`, ED-IN-0293 (10), RS-22) -- WHICH AMBITION A
PERSON ANSWERS FIRST: `world_q.attention_key` orders WITHIN a tier by SALIENCE, descending, never across
tiers. Salience is the cosine (`data/pursuits.py::alignment`, the one owner `cast.loyalty` also calls)
of the person's pursuits against what the ambition's organization expects: an org goal ->
`expected(org) + goal.pursuits`, the faction creed -> `expected(faction)`, his own want -> 0.

What each test proves, and the failure it can observe:

  (a) `test_one_owner_...` -- `cast.loyalty` and the key return the same cosine for one (person,
      template) pair. MUTATION (run): `loyalty` re-deriving the cosine with a different projection, or
      the key a different weight vector, reddens it.
  (b) `test_two_persons_..._order_the_same_two_goals_differently` -- the entry's first falsifier, over
      the `need` question AND the tier-0 claim. A PLANTED KEY READING `q.id` FIRST fails the
      "differently" assertion (`test_a_planted_key_reading_the_id_first_is_caught`); the control
      asserts the old `(source, id)` key orders the two persons alike.
  (c) `test_a_member_pointing_with_the_creed_...` / `..._against_...` -- the head-vs-faction
      reconciliation: with the creed he answers it first, against it his own want. The control is the
      old key (creed after the want by id for both).
  (d) `test_the_key_reads_nothing_outside_his_own_state` -- IN-57's falsifier shape, for salience.
  (e) `test_salience_never_lifts_a_question_across_a_tier` -- a tier-1 claim precedes the most
      salient `need`; a tier-0 claim precedes it too.
  (f) `test_expected_...` -- `data/goals.py::expected`: template + the org's goals, orientation goals
      included; a body takes its faction's.
  (g) `test_the_shipped_goals_file_gives_a_want_and_a_creed_only` -- with the shipped (empty) file the
      only salience is the creed's; every other ambition reads 0.
"""
from __future__ import annotations

import copy

import pytest
import yaml

from engine.substrate.descriptors import AFFILIATION_CONCERNS

from ..data import cast, goals
from ..data.affiliations import AFFILIATION_CEILING
from ..data.pursuits import alignment
from ..data.rosters import PURSUITS, ROLE_TEMPLATE_OF, faction_prop_id
from ..data.verbs import ROLE_TEMPLATE_PURSUITS
from ..queries import person_q, world_q
from ..state.carriers import Claim, Person, Proposition, Question, Tenure
from ..state.world import World

FAC = "Löwenritter"
TEMPLATE_WEIGHTS = ROLE_TEMPLATE_PURSUITS[ROLE_TEMPLATE_OF[FAC]]
FID = faction_prop_id(FAC)
DEVOUT = {AFFILIATION_CONCERNS["church"][0]: AFFILIATION_CEILING}   # religious_intensity 1.0: crisis_weights == pursuits


def _opposed_pair():
    """Two single pursuits whose projections point opposite ways, read off the shipped matrix."""
    for a in PURSUITS:
        for b in PURSUITS:
            c = alignment({a: 1.0}, {b: 1.0})
            if c is not None and c < -0.5:
                return a, b
    raise AssertionError("the shipped projection holds no opposed pair of pursuits")


A, B = _opposed_pair()


def _plant(monkeypatch, tmp_path, *rows):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    return goals.goals()


def _goal_row(gid, case, pursuits, org=None, obj=None):
    return {"id": gid, "org": org or {"faction": FAC}, "text": f"{gid}, as a predicate",
            "object": obj or {"kind": "person", "case": case}, "pursuits": pursuits, "source": "test_in69"}


def _person(pid, pursuits, ambitions=(), holds=()):
    p = Person(pid, pid)
    p.pursuits = dict(pursuits)
    p.conviction = dict(DEVOUT)
    for i, o in enumerate(ambitions):
        p.tenures.append(Tenure(f"t_{pid}_c{i}", pid, o, "commit", 0))
    for i, o in enumerate(holds):
        p.tenures.append(Tenure(f"t_{pid}_h{i}", pid, o, "hold", 0))
    return p


def _goal_world(monkeypatch, tmp_path, ga_weight=50.0):
    """Two goals of Löwenritter, `g_a` leaning on pursuit A and `g_b` on B (opposed), about two persons;
    and two members, `p_a` (pursuits A) and `p_b` (pursuits B), each committed to both."""
    _plant(monkeypatch, tmp_path,
           _goal_row("g_a", "NPC-020", {A: ga_weight}), _goal_row("g_b", "NPC-033", {B: ga_weight}))
    w = World(0)
    w.propositions["g_a"] = Proposition("g_a", "OUGHT", "p_x", "g_a, as a predicate", FAC, 0)
    w.propositions["g_b"] = Proposition("g_b", "OUGHT", "p_y", "g_b, as a predicate", FAC, 0)
    pa = _person("p_a", {A: 1.0}, ("g_a", "g_b"), holds=("p_x", "p_y"))
    pb = _person("p_b", {B: 1.0}, ("g_a", "g_b"), holds=("p_x", "p_y"))
    for p in (pa, pb):
        w.persons[p.id] = p
        # claims about each goal's person, ids chosen so the OLD key orders about-p_x first
        p.ledger += [Claim("c_1", p.id, "p_x", "exists:Person", 1, 0, "firsthand", 100, "own"),
                     Claim("c_2", p.id, "p_y", "exists:Person", 1, 0, "firsthand", 100, "own")]
    return w, pa, pb


def _order(w, p):
    return [q.id for q in world_q.questions_for(w, p)]


def _differ(order_fn, w, pa, pb) -> bool:
    return order_fn(w, pa) != order_fn(w, pb)


def _old_order(w, p):
    qs = world_q.questions_for(w, p)
    src = {s: i for i, s in enumerate(world_q.QUESTION_SOURCES)}
    return [q.id for q in sorted(qs, key=lambda q: (src[q.source], q.id))]


# ---------------------------------------------------------------------------------------------------
# (a) one owner of the cosine
# ---------------------------------------------------------------------------------------------------

def test_one_owner_cast_loyalty_and_the_key_return_the_same_cosine(monkeypatch, tmp_path):
    """For one (person, template) pair, the key's salience IS the cosine `loyalty` maps onto 0..100.
    Over an EMPTY goals file: the faction expects its template alone (v9 FA-05's rows add to it)."""
    _plant(monkeypatch, tmp_path)
    row = cast.row("NPC-033")
    pursuits = cast.pursuits_of(row)
    p = _person("p_n", pursuits, (FID,))
    w = World(0)
    w.propositions[FID] = Proposition(FID, "OUGHT", "p_lead", "carries the creed of", FAC, 0,
                                      scope=ROLE_TEMPLATE_OF[FAC])
    w.persons["p_n"] = p
    need = Question(f"q:need:{FID}", "need", ("p_lead",), FID)
    salience = -world_q.attention_key(w, p, [FID])(need)[1]
    cosine = alignment(pursuits, TEMPLATE_WEIGHTS)
    assert cosine is not None and salience == cosine, (salience, cosine)
    assert cast.loyalty(row, FAC) == round(cast.LOYALTY_INDIFFERENT * (salience + 1))
    assert cast.loyalty(row, FAC) != cast.LOYALTY_INDIFFERENT, "the control must not be at indifference"


def test_alignment_is_none_for_a_zero_side_and_symmetric():
    assert alignment({}, TEMPLATE_WEIGHTS) is None and alignment(TEMPLATE_WEIGHTS, {}) is None
    assert alignment({A: 1.0}, {B: 2.0}) == alignment({B: 2.0}, {A: 1.0})
    assert alignment({A: 3.0}, {A: 1.0}) == pytest.approx(1.0)


# ---------------------------------------------------------------------------------------------------
# (b) two persons, two goals, two orders
# ---------------------------------------------------------------------------------------------------

def test_two_persons_with_different_pursuits_order_the_same_two_goals_differently(monkeypatch, tmp_path):
    w, pa, pb = _goal_world(monkeypatch, tmp_path)
    assert _old_order(w, pa) == _old_order(w, pb), "control: the old key orders the two alike"
    oa, ob = _order(w, pa), _order(w, pb)
    # tier 0 (claims about the goals' persons) first, then the `need` questions: each by salience
    assert oa == ["q:claim:c_1", "q:claim:c_2", "q:need:g_a", "q:need:g_b"], oa
    assert ob == ["q:claim:c_2", "q:claim:c_1", "q:need:g_b", "q:need:g_a"], ob


def test_a_planted_key_reading_the_id_first_is_caught(monkeypatch, tmp_path):
    """The falsifier's own mutation: a key that reads `q.id` first orders the two persons alike, so the
    'differently' assertion above, run over it, fails."""
    w, pa, pb = _goal_world(monkeypatch, tmp_path)

    def planted_order(w_, p):
        return [q.id for q in sorted(world_q.questions_for(w_, p), key=lambda q: (q.id,))]

    assert _differ(_order, w, pa, pb)
    assert not _differ(planted_order, w, pa, pb), "a key reading q.id first cannot tell the two persons apart"


# ---------------------------------------------------------------------------------------------------
# (c) the head-vs-faction reconciliation: with the creed, the creed; against it, his own want
# ---------------------------------------------------------------------------------------------------

def _creed_world(pursuits):
    """A member of Löwenritter committed to his faction's creed and to a want of his own whose id sorts
    BEFORE the creed's, so the old key answers the want first for everyone."""
    w = World(0)
    w.propositions[FID] = Proposition(FID, "OUGHT", "p_lead", "carries the creed of", FAC, 0,
                                      scope=ROLE_TEMPLATE_OF[FAC])
    w.propositions["a_want"] = Proposition("a_want", "OUGHT", "p_w", "a want", True, 0)
    p = _person("p_m", pursuits, (FID, "a_want"))
    w.persons["p_m"] = p
    return w, p


def _most_and_least_aligned():
    scored = sorted((alignment({n: 1.0}, TEMPLATE_WEIGHTS), n) for n in PURSUITS
                    if alignment({n: 1.0}, TEMPLATE_WEIGHTS) is not None)
    assert scored[0][0] < 0 < scored[-1][0], "the template must have a pursuit against and one with it"
    return scored[-1][1], scored[0][1]


def test_a_member_pointing_with_the_creed_answers_it_first():
    with_, _ = _most_and_least_aligned()
    w, p = _creed_world({with_: 1.0})
    assert _old_order(w, p)[0] == "q:need:a_want", "control: the old key answers the want first"
    assert _order(w, p)[0] == f"q:need:{FID}"


def test_a_member_pointing_against_the_creed_answers_his_own_want_first():
    _, against = _most_and_least_aligned()
    w, p = _creed_world({against: 1.0})
    assert _order(w, p) == ["q:need:a_want", f"q:need:{FID}"]
    # ... and the want's salience is indifference, the creed's is below it
    key = world_q.attention_key(w, p)
    assert -key(world_q.questions_for(w, p)[0])[1] == 0.0
    assert key(Question(f"q:need:{FID}", "need", ("p_lead",), FID))[1] > 0.0


# ---------------------------------------------------------------------------------------------------
# (d) nothing outside his own state
# ---------------------------------------------------------------------------------------------------

def test_the_key_reads_nothing_outside_his_own_state(monkeypatch, tmp_path):
    w, pa, _ = _goal_world(monkeypatch, tmp_path)
    w2 = copy.deepcopy(w)
    for i in range(6):                      # a crowd he is not part of, committed to his goals
        w2.persons[f"p_z{i}"] = _person(f"p_z{i}", {A: 9.0}, ("g_a",))
    w2.propositions["x"] = Proposition("x", "OUGHT", "p_q", "elsewhere", True, 0)
    p2 = w2.persons["p_a"]
    k1, k2 = world_q.attention_key(w, pa), world_q.attention_key(w2, p2)
    qs = world_q.questions_for(w, pa)
    assert len(qs) == 4
    assert [k1(q) for q in qs] == [k2(q) for q in world_q.questions_for(w2, p2)]


# ---------------------------------------------------------------------------------------------------
# (e) within a tier, never across
# ---------------------------------------------------------------------------------------------------

def test_salience_never_lifts_a_question_across_a_tier(monkeypatch, tmp_path):
    w, pa, _ = _goal_world(monkeypatch, tmp_path)
    key = world_q.attention_key(w, pa)
    claim = Question("q:claim:c_2", "claim_landed", ("p_y",), "c_2")      # tier 0, against his lean
    need = Question("q:need:g_a", "need", ("p_x",), "g_a")                # tier 3, his best-fitting goal
    assert key(need)[1] < 0 < key(claim)[1], "the need is the more salient, the claim's goal fits him badly"
    assert key(claim)[0] == 0 and key(need)[0] == 3
    assert sorted([need, claim], key=key)[0] is claim
    # a tier-1 claim (about his own tenure's object, not an aim) precedes the most salient need as well
    pa.tenures.append(Tenure("t_obj", pa.id, "obj_t", "hold", 0))
    key = world_q.attention_key(w, pa)                                    # own_purview is read at build
    tier1 = Question("q:claim:c_3", "claim_landed", ("obj_t",), "c_3")
    assert key(tier1)[0] == 1 and sorted([need, tier1], key=key)[0] is tier1


# ---------------------------------------------------------------------------------------------------
# (f) expected(org)
# ---------------------------------------------------------------------------------------------------

def test_expected_is_the_template_plus_the_orgs_goals_orientation_included(monkeypatch, tmp_path):
    body = next(b for b, f in goals.BODY_FACTION.items() if f == FAC)
    _plant(monkeypatch, tmp_path,
           _goal_row("g_o", None, {A: 2.0}, obj={"kind": "orientation"}),
           _goal_row("g_p", "NPC-020", {A: 1.0, B: 4.0}),
           _goal_row("g_body", "NPC-020", {B: 7.0}, org={"body": body}))
    fac = goals.expected("faction", FAC)
    assert fac[A] == pytest.approx(TEMPLATE_WEIGHTS.get(A, 0.0) + 3.0)
    assert fac[B] == pytest.approx(TEMPLATE_WEIGHTS.get(B, 0.0) + 4.0)
    bod = goals.expected("body", body)           # a body takes its faction's template, plus ITS goals only
    assert bod[B] == pytest.approx(TEMPLATE_WEIGHTS.get(B, 0.0) + 7.0)
    assert bod[A] == pytest.approx(TEMPLATE_WEIGHTS.get(A, 0.0))
    assert goals.org_faction("body", body) == FAC and goals.org_faction("faction", FAC) == FAC


# ---------------------------------------------------------------------------------------------------
# (g) the shipped goals file
# ---------------------------------------------------------------------------------------------------

def test_an_empty_goals_file_gives_a_want_and_a_creed_only(monkeypatch, tmp_path):
    assert _plant(monkeypatch, tmp_path) == (), "control: the planted goals file is empty"
    with_, against = _most_and_least_aligned()
    w, p = _creed_world({with_: 1.0})
    key = world_q.attention_key(w, p)
    sal = {q.about: -key(q)[1] for q in world_q.questions_for(w, p)}
    assert sal["a_want"] == 0.0 and sal[FID] > 0.0
    assert goals.expected("faction", FAC) == pytest.approx(TEMPLATE_WEIGHTS)
