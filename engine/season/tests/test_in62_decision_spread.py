"""v9 IN-62 -- ONE OWNER OF THE SCORE'S TERMS, AND THE READING THAT ATTRIBUTES A DECISION TO ONE OF THEM.

`decision/choose.py::score_terms(p, c, fx, memo) -> (pursuit, stance, urgency)` owns the formula and
`make_chooser`'s `score` adds its three terms; `harness/decision_spread.py::attribute_top` says which
term decided a top. Five claims, each executed and each able to fail:

  1. `score(c) == sum(score_terms(...))` for EVERY candidate a seeded realm season forms (observed
     through `_sample_order`, the one place `make_chooser` hands the scores on), and the loop asserts
     that it asserted;
  2. two hand-built persons with one question and different pursuits pick different tops, attributed
     `pursuit`. MUTATION (run 2026-10-15): `score_terms` returning pursuit 0 reddens it -- the tops
     collapse onto one candidate and the attribution reads `tiebreak`;
  3. the attribution can say "no state decided": persons with nothing separating their candidates read
     `draw` / `tiebreak`, never `pursuit`; under `--null` (H-66 `uniform`) every realm top is
     `draw` / `tiebreak` while the shipped alignment reads `pursuit` for some (so the assertion is
     one that could fail);
  4. the pair that differs only in pursuits scores identically, candidate by candidate, under
     `--control`, and differently before it;
  5. `attribute_top`'s top is the REAL chooser's top (the ordering is repeated in the harness, so it is
     pinned here).
The plan's hash half (*`build_realm(0)` two-season hash EQUAL to the base*) is a realm reading recorded
at the commit, not pinned here: a pinned hash would be a golden, and the first reading IS the baseline.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.substrate.descriptors import PURSUITS

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..harness import decision_spread as DS
from ..harness.populated import build_realm
from ..state.carriers import Candidate, Person
from ..state.ids import draw_factory

_FX0 = DEFAULT_FIXTURES.sweep("choice_temperature", 0)        # no sampler: the score alone orders
_SUBJECT = "p_in62_x"


def _person(pid: str, **pursuits) -> Person:
    p = Person(id=pid, name=pid)
    p.pursuits = dict(pursuits)
    return p


def _cands(*verbs) -> list:
    return [Candidate(v, _SUBJECT) for v in verbs]


def _opposed_pair():
    """Two single-pursuit persons and two verbs whose pull on them runs OPPOSITE ways by a clear
    margin, found by scanning the loaded tables (nothing typed). Returns (pursuit a, pursuit b, verb va, verb vb)."""
    # the oracle is the DATA owners (`to_axes`, `align`), not `score_terms`: a mutated `score_terms`
    # must move the attribution under test, not the scan that picks the pair.
    verbs = sorted(VERB_TABLE)
    pull: dict = {}
    for name in PURSUITS:
        axes = to_axes({name: 1.0})
        for v in verbs:
            pull[(name, v)] = sum(axes[ax] * V.align(v, ax) for ax in PURSUIT_AXES)
    for a in PURSUITS:
        for b in PURSUITS:
            for i, va in enumerate(verbs):
                for vb in verbs[i + 1:]:
                    da, db = pull[(a, va)] - pull[(a, vb)], pull[(b, va)] - pull[(b, vb)]
                    if da > 0.05 and db < -0.05:
                        return a, b, va, vb
    raise AssertionError("no two pursuits pull two verbs opposite ways: the tables moved under this test")


def test_in62_two_persons_one_question_different_pursuits_pick_different_tops_by_pursuit():
    """THE FALSIFIER. MUTATION (run 2026-10-15): `score_terms` returning `(0.0, stance, u)` reddens it:
    both persons then tie on every candidate, share one top, and read `tiebreak`."""
    a, b, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    pa, pb = _person("p_in62_a", **{a: 1.0}), _person("p_in62_b", **{b: 1.0})
    ra = DS.attribute_top(pa, cands, _FX0)
    rb = DS.attribute_top(pb, cands, _FX0)
    assert ra["top"].verb != rb["top"].verb, (
        f"{a} vs {b} on ({va}, {vb}) picked {ra['top'].verb} and {rb['top'].verb}: nothing separated them")
    assert ra["decider"] == "pursuit" and rb["decider"] == "pursuit", (ra["decider"], rb["decider"])


def test_in62_persons_with_nothing_separating_their_candidates_are_never_attributed_to_pursuit():
    """Identical EMPTY state: no pursuit, no stance. At temperature 0 the verb's spelling orders the
    tie (`tiebreak`); at the shipped temperature the draw does (`draw`). Never `pursuit`."""
    a, b, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    draw = draw_factory(0, lambda: 0)
    checked = 0
    for i in range(6):
        p = _person(f"p_in62_empty_{i}")
        r0 = DS.attribute_top(p, cands, _FX0)
        assert r0["decider"] == "tiebreak", r0["decider"]
        r1 = DS.attribute_top(p, cands, DEFAULT_FIXTURES, draw)
        assert r1["decider"] == "draw", r1["decider"]
        checked += 2
    assert checked >= 12


_FX_TAU = DEFAULT_FIXTURES.sweep("choice_temperature", 0.1)


class _Fixed:
    """A planted draw stream: `random()` returns one number."""
    def __init__(self, u: float):
        self.u = u

    def random(self) -> float:
        return self.u


def _planted(favoured_verb: str):
    """A draw that gives `favoured_verb`'s candidate the largest Gumbel noise and every other the smallest
    (u -> 1 gives g ~ +27, u -> 0 gives g ~ -3), so the sampler's top is `favoured_verb` whatever the score."""
    return lambda pid, purpose: _Fixed(1 - 1e-12 if f"choice:{favoured_verb}:" in purpose else 1e-12)


def test_rem12_a_two_candidate_tie_at_tau_point_one_reads_tie_and_the_decider_stays_draw():
    """The `draw` label's first half. FALSIFIER: swapping the `tie` and `outvoted` classifications inside
    `attribute_top` reddens this and the next test. Identical EMPTY state: both candidates score alike."""
    _, _, va, vb = _opposed_pair()
    draw = draw_factory(0, lambda: 0)
    r = DS.attribute_top(_person("p_rem12_tie"), _cands(va, vb), _FX_TAU, draw)
    assert abs(r["margin"]) <= DS.EPS, "the premise failed: the two candidates did not tie"
    assert r["draw_kind"] == "tie", r["draw_kind"]
    assert r["decider"] == "draw", r["decider"]
    # CONTROL: at tau 0 the same tie is ordered by the spelling, not the draw -- no draw kind at all
    r0 = DS.attribute_top(_person("p_rem12_tie"), _cands(va, vb), _FX0)
    assert (r0["draw_kind"], r0["decider"]) == (None, "tiebreak"), (r0["draw_kind"], r0["decider"])


def test_rem12_a_strict_top_the_planted_draw_reverses_reads_outvoted_and_the_decider_stays_draw():
    """The `draw` label's second half. The person holds one pursuit, so one candidate leads on score; the
    planted draw hands the other candidate the sampler's top. A draw that agrees with the leader reads
    `None` and a term, so the assertion could fail."""
    a, _, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    p = _person("p_rem12_out", **{a: 1.0})
    strict = DS.attribute_top(p, cands, _FX0)["top"].verb          # the score alone: the leader
    other = vb if strict == va else va
    r = DS.attribute_top(p, cands, _FX_TAU, _planted(other))
    assert r["margin"] > DS.EPS, "the premise failed: no strict score top"
    assert r["top"].verb == other != strict, "the planted draw did not reverse the leader"
    assert r["draw_kind"] == "outvoted", r["draw_kind"]
    assert r["decider"] == "draw", r["decider"]
    # CONTROL: the same person, a draw favouring the leader -> not the draw's top; a term decided it
    ok = DS.attribute_top(p, cands, _FX_TAU, _planted(strict))
    assert ok["top"].verb == strict and ok["draw_kind"] is None and ok["decider"] == "pursuit", (
        ok["top"].verb, ok["draw_kind"], ok["decider"])


def test_rem12_field_zero_sets_urgency_aside_and_is_false_for_a_person_who_holds_a_vector():
    a, _, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    empty = DS.attribute_top(_person("p_rem12_fz"), cands, _FX0, subsistence=3.0)
    assert empty["field_zero"] is True
    assert any(t[2] != 0 for t in empty["terms"]), "urgency was 0: the setting-aside was not exercised"
    held = DS.attribute_top(_person("p_rem12_fz2", **{a: 1.0}), cands, _FX0)
    assert held["field_zero"] is False


def test_in62_identical_nonzero_pursuits_pick_one_top_and_the_attribution_is_pursuit():
    """The other half of "attributed to the state that decided": two persons holding the SAME pursuit
    are decided by it, and by the same candidate."""
    a, _, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    r1 = DS.attribute_top(_person("p_in62_s1", **{a: 1.0}), cands, _FX0)
    r2 = DS.attribute_top(_person("p_in62_s2", **{a: 1.0}), cands, _FX0)
    assert (r1["top"].verb, r1["decider"]) == (r2["top"].verb, r2["decider"]) == (r1["top"].verb, "pursuit")


def test_in62_the_pair_that_differs_only_in_pursuits_ties_under_control():
    a, b, va, vb = _opposed_pair()
    cands = _cands(va, vb)
    pa, pb = _person("p_in62_a", **{a: 1.0}), _person("p_in62_b", **{b: 1.0})
    before = (DS.attribute_top(pa, cands, _FX0), DS.attribute_top(pb, cands, _FX0))
    assert before[0]["scores"] != before[1]["scores"], "the pair did not differ before the control"
    mean = DS.apply_control(SimpleNamespace(persons={pa.id: pa, pb.id: pb}))
    assert mean and pa.pursuits == pb.pursuits == mean and pa.pursuits is not pb.pursuits
    ra, rb = DS.attribute_top(pa, cands, _FX0), DS.attribute_top(pb, cands, _FX0)
    assert ra["scores"] == rb["scores"] and ra["terms"] == rb["terms"], "control left the pair apart"
    assert ra["top"].verb == rb["top"].verb


def test_in62_the_harness_top_is_the_real_choosers_top(monkeypatch):
    """`attribute_top` repeats the chooser's ORDERING; this pins its top to `make_chooser`'s own, at the
    shipped temperature and a real draw, over persons whose pursuits differ."""
    verbs = sorted(VERB_TABLE)[:8]
    cands = _cands(*verbs)
    seen: dict = {}
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = list(ranked)
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    draw = draw_factory(0, lambda: 0)
    chooser = CH.make_chooser(DEFAULT_FIXTURES, lambda *a: "act", draw=draw)
    checked = 0
    for i, name in enumerate(PURSUITS):
        p = _person(f"p_in62_c{i}", **{name: 1.0, PURSUITS[(i + 3) % len(PURSUITS)]: 0.5})
        seen.clear()
        chooser(p, SimpleNamespace(question=object()), SimpleNamespace(subsistence=0), lambda: 1)
        assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
        r = DS.attribute_top(p, cands, DEFAULT_FIXTURES, draw)
        assert r["top"] is seen["ranked"][0], (p.id, r["top"].verb, seen["ranked"][0].verb)
        checked += 1
    assert checked == len(PURSUITS) >= 15


def test_in62_a_memo_without_the_hoisted_factors_is_refused():
    p = _person("p_in62_m", **{PURSUITS[0]: 1.0})
    with pytest.raises(ValueError, match="deliberation_memo"):
        CH.score_terms(p, Candidate(sorted(VERB_TABLE)[0], _SUBJECT), _FX0, {})


@pytest.fixture(scope="module")
def season_pairs():
    """One seeded realm season through the real chooser, recording for every candidate it ranked the
    chooser's own `score(c)` (seen at `_sample_order`) beside the `score_terms` it came from."""
    mp = pytest.MonkeyPatch()
    pending: list = []
    pairs: list = []
    real_terms, real_order = CH.score_terms, CH._sample_order

    def terms_spy(p, c, fx, memo):
        t = real_terms(p, c, fx, memo)
        pending.append((id(c), t))
        return t

    def order_spy(ranked, score, p, fx, draw):
        by_id = dict(pending)
        pending.clear()
        for c in ranked:
            pairs.append((score(c), by_id[id(c)]))
        return real_order(ranked, score, p, fx, draw)
    mp.setattr(CH, "score_terms", terms_spy)
    mp.setattr(CH, "_sample_order", order_spy)
    try:
        w = build_realm(0)
        DS.play_season(w, 1)
    finally:
        mp.undo()
    return pairs


def test_in62_score_is_the_sum_of_score_terms_for_every_candidate_a_season_forms(season_pairs):
    checked = 0
    for score, (pursuit, stance, urgency) in season_pairs:
        assert score == pursuit + stance + urgency, (score, pursuit, stance, urgency)
        checked += 1
    assert checked >= 1000, f"a seeded realm season formed only {checked} candidates"
    assert any(t[0] != 0 for _, t in season_pairs), "no pursuit term was nonzero: the sum proved nothing"


def test_in62_under_the_null_every_realm_top_is_draw_or_tiebreak_and_the_shipped_reading_is_not():
    shipped = DS.read_decisions(build_realm(0))
    with DS.null_alignment():
        null = DS.read_decisions(build_realm(0))
    assert DS.alignment_at("uniform") != V.ALIGNMENT, "the null outlived its reading"
    seen_null, checked = set(), 0
    for row in null["rows"]:
        seen_null |= set(row["deciders"])
        checked += sum(row["deciders"].values())
    assert checked >= 400, checked
    assert seen_null <= {"draw", "tiebreak"}, f"under the null a top was attributed to {seen_null}"
    assert any("pursuit" in k for row in shipped["rows"] for k in row["deciders"]), (
        "the shipped reading attributed no top to pursuit: the null assertion could not have failed")


def test_in62_arm_0_holds_one_vector_one_conviction_and_reads_no_goals_file():
    """The control the close review found leaking: every holder of a vector holds the SAME vector and the
    SAME conviction (the score projects `crisis_weights`, which scales `doctrine` by conviction), a person
    who holds no vector keeps holding none, and `no_goals()` makes the goals FILE read empty for the
    reading and restores it."""
    from ..data import goals as goals_data
    w = build_realm(0, goals=False)
    before = {pid: bool(p.pursuits) for pid, p in w.persons.items()}
    DS.apply_control(w)
    holders = [p for p in w.persons.values() if before[p.id]]
    assert len(holders) >= 46 and any(not v for v in before.values()), "control: cast hold vectors, cohorts none"
    assert len({tuple(sorted(p.pursuits.items())) for p in holders}) == 1
    assert len({tuple(sorted(p.conviction.items())) for p in holders}) == 1
    assert all(not p.pursuits for pid, p in w.persons.items() if not before[pid])
    assert goals_data.goals(), "control: the shipped file carries goals"
    with_goals = goals_data.expected("faction", "Crown")
    with DS.no_goals():
        assert goals_data.goals() == ()
        assert goals_data.expected("faction", "Crown") != with_goals, (
            "the creed's expected vector still sums the file's goal pursuits under the control")
    assert goals_data.goals(), "no_goals() did not restore the cache"
