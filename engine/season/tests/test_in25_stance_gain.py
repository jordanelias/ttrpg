"""v9 IN-25 (BOUND-STAKES, `workplans/valoria_master_workplan_v9_part5.md`) -- a gain on `score`'s
stance term: `decision/choose.py::stance_term` reads the term `stance_polarity` signs (IN-18 G2,
H-194) at `1 + g`, `g` the swept `Fixtures` arm `stance_gain` (H-202; control `0`, shipped).

THE FALSIFIER, executed and able to fail:
  * a planted person whose pursuits pull one candidate above another, holding stance toward the
    other's subject worth 0.6 of that pull: the control arm `0` keeps the pursuits' order, the arms
    `1` and `3` reverse it -- a `score` whose stance term carried no gain could not;
  * the same person holding NO stance is unmoved at `3`, so the reversal is the stance's;
  * `stance_term` at every polarity arm is the control's value times `1 + g` exactly, so the gain
    scales G2's SIGNED term and does not re-sign it.
The plan's hash half (*"the gain at 0 does not reproduce today's hash"*) is a realm reading,
recorded on H-202, not re-run here. Verbs are read off the loaded tables, not typed.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE, align
from ..decision import choose as CH
from ..decision.options import project
from ..state.carriers import Candidate, Person

_HI_SUBJECT, _LO_SUBJECT = "p_in25_a", "p_in25_b"
_ARMS = (0.0, 1.0, 3.0)


def _verbs(p: Person):
    """The highest- and lowest-pulling verbs for `p` under the bare pursuit dot, read off the table."""
    axis_w = project(p)
    pull = {v: sum(axis_w[ax] * align(v, ax) for ax in PURSUIT_AXES) for v in sorted(VERB_TABLE)}
    hi, lo = max(pull, key=pull.get), min(pull, key=pull.get)
    assert pull[hi] > pull[lo], "every verb pulls alike: no ranking to reverse"
    return hi, lo, pull[hi] - pull[lo]


def _ranking(g: float, share: float, monkeypatch) -> tuple:
    """`make_chooser`'s real ranking, temperature 0, `stance_polarity` shipped, `stance_gain == g`,
    for a person whose stance toward the low verb's subject is `share` of the pursuit gap."""
    p = Person(id="p_in25", name="p_in25")
    p.pursuits = dict(virtue=1.0)
    hi, lo, gap = _verbs(p)
    p.stance = [(_LO_SUBJECT, share * gap, 1.0)] if share else []
    cands = [Candidate(hi, _HI_SUBJECT), Candidate(lo, _LO_SUBJECT)]
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [c.verb for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    fx = DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("stance_gain", g)
    CH.make_chooser(fx, lambda *a: "act")(p, SimpleNamespace(question=object()),
                                         SimpleNamespace(subsistence=0), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"], hi, lo


def test_in25_the_gain_reverses_a_ranking_the_control_keeps(monkeypatch):
    """MUTATION (run 2026-10-09, IN-25): `stance_term`'s gain dropped (`return t` on every arm)
    reddens the arm-1 and arm-3 assertions. Restored, GREEN."""
    assert DEFAULT_FIXTURES.get("stance_gain") == 0, "the shipped arm moved: restate"
    checked = 0
    control, hi, lo = _ranking(0.0, 0.6, monkeypatch)
    assert control == [hi, lo], f"the control arm did not keep the pursuit dot's order: {control}"
    for g in (1.0, 3.0):
        armed, _, _ = _ranking(g, 0.6, monkeypatch)
        assert armed == [lo, hi], (
            f"stance worth 0.6 of the pursuit gap, gain {g}, left the order at {armed}: "
            "`score`'s stance term carries no gain")
        checked += 1
    assert checked >= 2


def test_in25_no_stance_is_unmoved_at_the_largest_arm(monkeypatch):
    armed, hi, lo = _ranking(3.0, 0.0, monkeypatch)
    assert armed == [hi, lo], f"the gain moved a person holding no stance: {armed}"


def test_in25_the_gain_scales_the_signed_term_on_every_polarity_arm():
    from ..decision.options import subject_is_opponent
    p = Person(id="p_in25", name="p_in25")
    p.stance = [("p_x", -1.0, 3.0)]                 # `_eff_march`'s grudge-row shape
    assert subject_is_opponent(VERB_TABLE["fight"]) and not subject_is_opponent(VERB_TABLE["tell"])
    checked = 0
    assert len(CH.STANCE_POLARITIES) >= 3, CH.STANCE_POLARITIES
    for polarity in CH.STANCE_POLARITIES:
        base = DEFAULT_FIXTURES.sweep("stance_polarity", polarity)
        for verb in ("fight", "tell"):
            c = Candidate(verb, "p_x")
            t0 = CH.stance_term(p, c, base)
            assert t0 != 0, f"{polarity}/{verb}: the planted grudge reads 0, nothing to scale"
            for g in _ARMS:
                assert CH.stance_term(p, c, base.sweep("stance_gain", g)) == (1.0 + g) * t0
                checked += 1
    # G2's sign survives the gain: `declared` still pulls `fight` on the disliked UP
    assert CH.stance_term(p, Candidate("fight", "p_x"),
                          DEFAULT_FIXTURES.sweep("stance_polarity", "declared")
                          .sweep("stance_gain", 3.0)) == 12.0
    assert checked == len(CH.STANCE_POLARITIES) * 2 * len(_ARMS)


@pytest.mark.parametrize("g", [-1.0, float("nan")])
def test_in25_a_negative_or_nan_gain_is_refused(g):
    with pytest.raises(ValueError, match="stance_gain"):
        CH.stance_term(Person(id="p", name="p"), Candidate("fight", "p_x"),
                       DEFAULT_FIXTURES.sweep("stance_gain", g))
