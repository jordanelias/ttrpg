"""The deontological gate on ONE scale (B10.22): the person's side of it is his axis's SHARE of his projected vector
(`options.refusal_tolerance`), on ±1 as an alignment cell is, so a refusal tracks the man and not the size of the table.

Read on the built realm with no season. The cells the realm ships are content (`16_PESSIMIST_CHAR_B`), so the refusal
half is read on PLANTED persons whose vectors and cells are set here, never on the shipped `forge` cell."""

from __future__ import annotations

import math

import pytest

from ..boot.chooser import chooser
from ..boot.realm import build_realm
from ..data import verbs as data_verbs
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import _ROSTERS, PURSUIT_AXES, refusable
from ..decision import choose as _choose
from ..decision import options as _options
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import subject_of
from .test_cr21_cells import _deontological_axis


@pytest.mark.parametrize("seed", (0, 1))
def test_share_not_projected_weight_is_the_tolerance(seed, monkeypatch):
    """Every cast tolerance is the axis's share of his projected vector and lies on ±1; and on planted persons a verb whose
    cell sits past the SHARE is refused while the raw weight would have said otherwise, in both directions."""
    w = build_realm(seed)
    axis = _deontological_axis()
    cast = [p for p in w.persons.values() if not p.is_cohort]
    assert len(cast) > 1
    for p in cast:
        v = _options.project(p)
        norm = math.sqrt(sum(x * x for x in v.values()))
        tol = _options.refusal_tolerance(p, axis)
        assert -1.0 <= tol <= 1.0, f"{p.id}: a tolerance of {tol:+.3f} lies off the cells' ±1 scale"
        assert tol == pytest.approx(v[axis] / norm if norm else 0.0, abs=1e-9)
    assert any(abs(_options.project(p)[axis]) < abs(_options.refusal_tolerance(p, axis)) for p in cast), (
        "no cast member's share differs from his raw weight, so the scale change observes nothing here")

    other = next(a for a in sorted(PURSUIT_AXES) if a != axis)
    mild, harsh = sorted(refusable(axis))[:2]
    monkeypatch.setitem(_ROSTERS["pursuit_axes"], "refusable", {axis: [mild, harsh]})
    monkeypatch.setattr(data_verbs, "ALIGNMENT", {axis: {mild: -0.5, harsh: 0.5}})
    p = cast[0]

    def planted(on_axis, off_axis):
        monkeypatch.setattr(data_verbs, "PURSUIT_PROJECTION", {"planted": {axis: on_axis, other: off_axis}})
        monkeypatch.setattr(p, "pursuits", {"planted": 1.0})
        tol = _options.refusal_tolerance(p, axis)
        return tol, {v for v in (mild, harsh) if _options.refuses(v, axis, tol)}

    # A man whose small vector points mostly down the axis: raw weight -0.2 (past `mild`'s -0.5 on the old scale: tolerated),
    # share -0.894 (below it: `mild` is past what he allows himself). `harsh` (+0.5) is past both.
    tol, refused = planted(-0.2, 0.1)
    assert tol == pytest.approx(-0.2 / math.hypot(0.2, 0.1))
    assert refused == {mild, harsh}
    # A man whose small vector lies wholly up the axis: raw weight +0.1 would refuse `harsh` (+0.5); his share is +1, so
    # nothing the cells reach lies past him.
    tol, refused = planted(0.1, 0.0)
    assert tol == pytest.approx(1.0)
    assert refused == set()


def test_scruple_is_zero_outside_the_set_and_positive_past_the_tolerance(monkeypatch):
    """B10.23: the refusal is a MARGIN. On planted cells a listed verb's scruple is how far its cell sits past the tolerance
    toward the refused pole (0.0 on the tolerated side), a verb outside the closed set has none however far its cell lies, and
    `refuses` is exactly `scruple > 0`."""
    build_realm(0)
    axis = _deontological_axis()
    mild, harsh = sorted(refusable(axis))[:2]
    outside = next(v for v in sorted(data_verbs.ALIGNMENT[axis]) if v not in refusable(axis))
    monkeypatch.setitem(_ROSTERS["pursuit_axes"], "refusable", {axis: [mild, harsh]})
    monkeypatch.setattr(data_verbs, "ALIGNMENT", {axis: {mild: -0.5, harsh: 0.5, outside: 0.9}})

    # tolerance +0.2: `harsh` lies 0.3 past it toward the refused pole, `mild` lies on the tolerated side, and `outside` lies
    # 0.7 past him but is not one of the certain actions
    assert _options.scruple(harsh, axis, 0.2) == pytest.approx(0.3)
    assert _options.scruple(mild, axis, 0.2) == 0.0
    assert _options.scruple(outside, axis, 0.2) == 0.0
    # tolerance -0.9: `mild` (-0.5) now lies 0.4 past it
    assert _options.scruple(mild, axis, -0.9) == pytest.approx(0.4)
    assert _options.scruple(outside, axis, -0.9) == 0.0
    checked = 0
    for tol in (-1.0, -0.9, -0.5, 0.0, 0.2, 0.5, 1.0):
        for v in (mild, harsh, outside):
            assert _options.refuses(v, axis, tol) == (_options.scruple(v, axis, tol) > 0.0)
            checked += 1
    assert checked == 21


def test_forgone_scores_exceed_released_lead(monkeypatch):
    """B10.24: armed, the gate strikes AFTER scoring and the Scene keeps what was given up. On a seed-0 realm season with a
    planted refusable verb (never the shipped cells), every Scene's `forgone` is exactly the struck candidates that out-scored
    the Scene's first act, each at its positive margin; the oracle is the score the chooser itself computed, recorded as it
    scored (the struck candidate's included), not read back off the carrier."""
    axis = _deontological_axis()
    planted = "create_record"             # the commonest act of the seed-0 season: a struck candidate that out-scores the lead is likely
    table = {a: dict(cells) for a, cells in data_verbs.ALIGNMENT.items()}
    table[axis][planted] = 0.9            # past every tolerance short of 0.9: refused by nearly every cast member
    w = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("refusal_axis", axis))
    monkeypatch.setattr(data_verbs, "ALIGNMENT", table)
    monkeypatch.setitem(_ROSTERS["pursuit_axes"], "refusable", {axis: [planted]})

    scored: list = []                     # (actor, verb, subject, score), in scoring order, cleared at each release
    inner_terms, inner_release = _choose.score_terms, _choose.release
    seen = {"scenes": 0, "forgone": 0, "struck_persons": 0}

    def spy_terms(p, c, fx, memo, odds=None, q=None):
        t = inner_terms(p, c, fx, memo, odds, q)
        scored.append((p.id, c.verb, c.subject or "", _choose.score_total(t)))
        return t

    def spy_release(p, ranked, n_scenes, fx, mint, q, draw=None):
        scenes = inner_release(p, ranked, n_scenes, fx, mint, q, draw)
        seg, scored[:] = dict(((v, s), sc) for _, v, s, sc in scored), []
        margin = _options.scruple(planted, axis, _options.refusal_tolerance(p, axis))
        seen["struck_persons"] += margin > 0
        for sc in scenes:
            lead = sc.acts[0]
            lead_score = seg[(lead.verb, subject_of(lead))]
            want = {(planted, s) for (v, s) in seg if v == planted and margin > 0 and seg[(v, s)] > lead_score}
            assert {(v, s) for v, s, _ in sc.forgone} == want, (p.id, lead.verb, sc.forgone, want)
            assert all(m == margin and m > 0 for _, _, m in sc.forgone)
            seen["scenes"] += 1
            seen["forgone"] += len(sc.forgone)
        return scenes

    monkeypatch.setattr(_choose, "score_terms", spy_terms)
    monkeypatch.setattr(_choose, "release", spy_release)
    d = SeasonDriver(w)
    d.season(chooser(w, verbs=resolvable_verbs()), question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert seen["struck_persons"] >= 1, "nobody's scruple struck the planted verb, so the gate observed nothing"
    assert seen["forgone"] >= 1, f"no Scene kept a struck candidate that out-scored its lead: {seen}"
    assert seen["scenes"] >= 10, "too few Scenes were checked for the equality to mean anything"
    stored = [sc for sc in w.acts.scenes() if sc.forgone]
    assert stored, "the Scenes RESOLVE stored carry no `forgone`"


def test_giving_way_to_a_scruple_is_an_event_the_fold_emits():
    """B10.24: where the Scene's `forgone` gives the act's own candidate a positive margin and the act resolves, the fold
    emits `scruple.overridden` beside the act's own kinds, caused by the act and graded by no band. An entry for another
    candidate, or at margin 0.0, or no entry, emits nothing."""
    from ..data.matrix import WriteClass
    from ..loop.driver import mint_token
    from ..state.carriers import Act, Scene
    from .test_in09_dispensation_answer import HOLDER, WRIT, _read_terms, _with_writ

    verb = "evade / defy"
    assert "scruple.overridden" in data_verbs.VERB_TABLE[verb].emits

    def fold(forgone, key):
        w, d = _with_writ()
        _read_terms(w, HOLDER)
        a = Act(id=key, actor=HOLDER, verb=verb, payload={"subject": WRIT})
        a.scene = f"sc_{key}"
        w.acts.add_scene(Scene(a.scene, HOLDER, [a], forgone=forgone))
        return a, d._fold(w, mint_token(w, WriteClass.ACTS), a)

    a, out = fold(((verb, WRIT, 0.4),), "gives_way")
    assert [e.kind for e in out] == ["compliance.withheld", "scruple.overridden"]
    assert out[1].degree is None and a.id in out[1].causes
    for forgone, key in (((), "no_entry"), (((verb, WRIT, 0.0),), "zero_margin"),
                         ((("construe", WRIT, 0.4),), "other_verb"), (((verb, "p_mid", 0.4),), "other_subject")):
        assert [e.kind for e in fold(forgone, key)[1]] == ["compliance.withheld"], key


def test_draw_strikes_some_not_all_at_margin_005_and_08():
    """B10.25: armed, with `scruple_temperature` 0.2, a candidate is struck with probability `1 - exp(-margin / T)` on the person's own draw
    keyed `scruple:<verb>:<subject>`. One planted person on one situation, 200 draws (the draw factory's seed is the only thing that varies):
    a candidate at margin 0.05 is struck in some and not all, one at margin 0.8 in most and not all. A candidate the draw leaves standing
    is kept in the Scene it leads (`Scene.forgone`) at its margin: the branch B10.24's threshold never reaches."""
    from ..state.ids import draw_factory
    from .test_governance_build import _h2_base, _h2_inject

    w, p, q, v, base, verbs = _h2_base()
    axis = _deontological_axis()
    light, heavy = verbs[:2]
    fx = w.fixtures.sweep("refusal_axis", axis).sweep("scruple_temperature", 0.2).sweep("choice_temperature", 0)
    # tolerance -0.4; the refusing pole is the negative one, so a cell lies past it by `cell - tolerance`: 0.05 and 0.8
    restore = _h2_inject(p, axis, -0.4, {light: -0.35, heavy: 0.4})
    struck = {c: 0 for c in sorted(base) if c[0] in (light, heavy)}
    standing = 0
    checked = 0
    try:
        assert _options.scruple(light, axis, -0.4) == pytest.approx(0.05) and _options.scruple(heavy, axis, -0.4) == pytest.approx(0.8)
        for seed in range(200):
            rank = _choose.make_ranker(fx, None, draw_factory(seed, lambda: 0))
            ranked = rank(p, v)
            formed = {(c.verb, c.subject): c for c in ranked}
            checked += 1
            for cand in struck:
                if cand not in formed:
                    struck[cand] += 1
                    continue
                kept = {(vb, s): m for vb, s, m in ranked.forgone_of(formed[cand], [formed[cand]])}
                assert kept[(cand[0], cand[1] or "")] == _options.scruple(cand[0], axis, -0.4), (seed, cand, kept)
                standing += 1
    finally:
        restore()
    assert checked >= 200 and standing >= 1 and len(struck) >= 2
    for cand, n in struck.items():
        if cand[0] == light:
            assert 0 < n < 200, (cand, n)            # a small margin usually gives way, and sometimes does not
        else:
            assert 100 < n < 200, (cand, n)          # a large one stops him in most draws and never certainly
