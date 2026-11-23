"""B10.04 -- regard read as a share of the stance bound, times `Fixtures stance_scale`
(`decision/choose.py::stance_term`; `U5a_CHAR_owed_amendments` §2).

`stance_scale` ships at its control, `STANCE_MAX`: the term is today's exactly (the realm hash is the control, recorded in
the commit). The test below observes what the sweep (0.2, 0.4, 0.8) is for: a man's loyalty to one person makes an act done
against him rare in his choices, and not impossible.

FALSIFIER: no draw takes the act against him at any swept value (the gap is out of the draw's reach), or more than half
do (the relationship no longer restrains).
"""
from __future__ import annotations

import random

from ..data.pursuits import pursuit
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision.options import opening_set, subject_is_opponent
from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Question, View
from ._scar_helpers import scars, wounded

A, B = "p_mid", "p_low"          # `probes.tiny_world`: both at the hearth `Hh`
DRAWS = 200
SWEPT = (0.2, 0.4, 0.8)


def _takes_the_act_against_him(v: float) -> tuple[int, int]:
    """`(takes, checked)` over `DRAWS` draws of one deliberation: `A`, with an authored stance of 10 toward `B`, answers one
    question about `B`; `takes` counts the draws whose first pick is an act the verb row treats as against its subject
    (`subject_is_opponent`, the sign `_stance_arm` reads under the shipped `declared` arm)."""
    w = P.tiny_world()
    p, fx = w.persons[A], w.fixtures.sweep("stance_scale", v)
    p.stance.append((B, 2, 5))                              # valence 2 x weight 5 = 10
    # [JUSTIFIED: the pull of his own pursuits toward the act against B -- `speak` is the one opponent row this question forms, and
    # its alignment is small on every axis, so a negative weight on `stewardship` (humble: speak -0.4 on `grandiose_humble`) is the
    # only plant that makes it his pursuits' top; one fixed value across the sweep, not tuned per swept value]
    p.pursuits = {pursuit("stewardship"): -2.0}
    q = Question("q:regard-unit", "need", (B,), B)
    cands = opening_set(p, View(A, [], fx.get("view_k"), q), q, fx)
    memo = CH.deliberation_memo(p, fx)
    scores = {id(c): CH.score_total(CH.score_terms(p, c, fx, memo, None)) for c in cands}
    ranked = CH.score_order(cands, scores)
    takes = checked = 0
    for s in range(DRAWS):
        def draw(pid, purpose, s=s):
            return random.Random(f"{s}|{pid}|{purpose}")
        top = CH._sample_order(ranked, lambda c: scores[id(c)], p, fx, draw)[0]
        checked += 1
        takes += subject_is_opponent(VERB_TABLE[top.verb]) and top.subject == B
    return takes, checked


def test_a_strong_loyalty_makes_acting_against_rare_not_impossible():
    got = {}
    for v in SWEPT:
        takes, checked = _takes_the_act_against_him(v)
        assert checked >= DRAWS, v
        assert takes < DRAWS / 2, f"at {v} {takes} of {checked}: the relationship no longer restrains"
        got[v] = takes
    assert max(got.values()) > 0, f"0 of {DRAWS} at every swept value: the gap is out of the draw's reach, {got}"
    assert got[0.2] >= got[0.4] >= got[0.8], f"a larger scale must not restrain less: {got}"



def test_stance_term_is_clamped():
    """B10.10 (H-471): twenty grudges of weight 5 against one person (H-339's hand-set rows) sum to -100 in stance units; through
    `stance_term` at `stance_gain` 1 the term reads +-200 unclamped and +-50 (2 x `STANCE_MAX`) with `stance_clamp` on, under every
    polarity arm. A sum inside the bound (five grudges, -25) reads the same either way."""
    from ..data.cast import STANCE_MAX
    from ..state.carriers import Candidate
    w = P.tiny_world()
    p = w.persons[A]
    cand = Candidate("speak", B)
    got = {}
    for rows in (20, 5):
        p.stance = [(B, -1, 5)] * rows
        for arm in ("legacy", "regard", "declared"):
            for clamp in (False, True):
                fx = w.fixtures.sweep("stance_polarity", arm).sweep("stance_gain", 1.0).sweep("stance_clamp", clamp)
                got[rows, arm, clamp] = abs(CH.stance_term(p, cand, fx))
    assert all(got[20, arm, False] == 2 * 100 for arm in ("legacy", "regard", "declared")), got
    assert all(got[20, arm, True] == 2 * STANCE_MAX for arm in ("legacy", "regard", "declared")), got
    assert all(got[5, arm, c] == 2 * 25 for arm in ("legacy", "regard", "declared") for c in (False, True)), got


def _five_sights(cap):
    """`scars` after ONE driver folds the same violating act (`fight`, which violates every pursuit below) five times in one season
    with everyone an observer (`fan_out_mode: total`), each person holding `stability` 0.2 and `justice` 0.5."""
    w = P.tiny_world()
    w.step = Step.RESOLVE
    w.fixtures = w.fixtures.sweep("scar_season_cap", cap).sweep("fan_out_mode", "total")
    for p in w.persons.values():
        p.pursuits = {pursuit("stability"): 0.2, pursuit("justice"): 0.5}
    d = SeasonDriver(w)
    for i in range(5):
        d._fold(w, mint_token(w, WriteClass.ACTS), Act(id=f"cap{i}", actor="p_low", verb="fight", payload={"subject": "p_mid"}), wounded())
    return scars(w)


def test_a_capped_witness_holds_one_count_for_five_sights():
    """B10.06 (H-465): the same violating act seen five times in one season is five counts per element uncapped and one at the
    cap -- per element at `element`, and at `person` one count in all, on the element he holds most violated (`justice`, 0.5)."""
    got = {cap: _five_sights(cap) for cap in (None, "element", "person")}
    assert got[None] and all(c == {pursuit("justice"): 5, pursuit("stability"): 5} for c in got[None].values()), got[None]
    assert got["element"].keys() == got[None].keys() and all(
        c == {pursuit("justice"): 1, pursuit("stability"): 1} for c in got["element"].values()), got["element"]
    assert got["person"].keys() == got[None].keys() and all(
        c == {pursuit("justice"): 1} for c in got["person"].values()), got["person"]


# ---------------------------------------------------------------------------------------------------
# B10.09 (H-470): regard's judged and told halves counted in stance steps (`person_q.deed_steps`, `regard`'s arm `stance`).
# ---------------------------------------------------------------------------------------------------

KIND = "commitment.ended"        # an unpaired deed kind with a nonzero row on the deontological axis (`data/verbs.py::align_kind`)


def _saw(weight, n, unit, *, told=False):
    """`(regard, gain)` of a holder whose one pursuit, `honour`, weighs `weight`, who holds `n` claims that `B` did a deed of `KIND`
    (firsthand, or told when `told`), at `Fixtures regard_unit` `unit`, and the gain that half is read at; no stance row, so the
    figure is the deeds' half alone."""
    from ..state.carriers import Claim
    from ..queries.person_q import regard
    w = P.tiny_world()
    fx = w.fixtures.sweep("regard_unit", unit)
    p = w.persons[A]
    p.pursuits = {pursuit("honour"): weight}
    p.stance = []
    p.ledger = [Claim(f"c_ru{i}", A, B, KIND, True, 0, "told" if told else "firsthand", 100, "own",
                      chain=(("p_other",) if told else ())) for i in range(n)]
    return regard(p, B, fx), float(fx.get("told_valence_gain" if told else "judged_gain"))


def test_one_deed_is_at_most_one_step_at_arm_stance():
    """B10.09 (H-470): two holders with opposite pursuits who each saw one deed hold regards of opposite sign, of size at most the
    gain (one step times `judged_gain`) at `stance`, and of the raw size (past it, at a pursuit weight of 3) at `raw`. The told
    half is bound the same way by `told_valence_gain`."""
    for told in (False, True):
        mine, gain = _saw(3.0, 1, "stance", told=told)
        theirs, _ = _saw(-3.0, 1, "stance", told=told)
        assert mine < 0 < theirs and abs(mine) <= gain and abs(theirs) <= gain, (told, mine, theirs, gain)
        assert abs(mine) == abs(theirs) > 0, (told, mine, theirs)           # a cosine is the same size either side of the axis
        raw_mine, _ = _saw(3.0, 1, "raw", told=told)
        raw_theirs, _ = _saw(-3.0, 1, "raw", told=told)
        assert raw_mine < 0 < raw_theirs and abs(raw_mine) > gain and abs(raw_theirs) > gain, (told, raw_mine, raw_theirs, gain)


def test_six_deeds_outweigh_a_loyalty_row_of_weight_two():
    """B10.09 (H-470): a holder who saw six such deeds holds a regard that outweighs a loyalty row of weight 2 (one step, weight 2:
    +2) at `stance`, where one deed does not; at `raw` ONE deed of a holder whose pursuit weighs 10 already does, which is the
    unit the arm replaces."""
    loyalty = 1 * 2
    one, _ = _saw(10.0, 1, "stance")
    six, _ = _saw(10.0, 6, "stance")
    assert one + loyalty > 0 > six + loyalty, (one, six)
    raw_one, _ = _saw(10.0, 1, "raw")
    assert raw_one + loyalty < 0, raw_one


def test_sabotage_on_a_hated_person_scores_positive_with_the_cell(monkeypatch):
    """B10.11 (H-337): at stance -25 the term for `sabotage` on the hated person is negative before a `regard_sign` cell (`sabotage` is
    no act contested against its subject, so the row's default sign is +1 and a grudge lowers it) and positive once the cell `-1` is
    planted in this test's own copy of the table (never in `verb_table.yaml`); a cell `0` reads nothing, and `+1` is the default."""
    from dataclasses import replace
    from ..state.carriers import Candidate
    w = P.tiny_world()
    p = w.persons[A]
    p.stance = [(B, -1, 5)] * 5                                                  # -25 toward B
    fx = w.fixtures.sweep("stance_polarity", "declared")
    cand = Candidate("sabotage", B)
    before = CH.stance_term(p, cand, fx)
    got = {}
    for sign in (-1, 0, 1):
        monkeypatch.setattr(CH, "VERB_TABLE", {**VERB_TABLE, "sabotage": replace(VERB_TABLE["sabotage"], regard_sign=sign)})
        got[sign] = CH.stance_term(p, cand, fx)
    assert before < 0 < got[-1], (before, got)
    assert got[0] == 0 and got[1] == before, (before, got)
