"""IN-08 6f (`workplans/valoria_master_workplan_v9_part5.md`) -- `score` is the derived `confliction`
Query's caller (ID-13): `make_chooser` reads the pursuit dot at `1 / (1 + k * confliction(p))`, `k`
the swept `Fixtures` arm `confliction_weight` (H-188; control `0`, shipped).

THE FALSIFIER, executed and able to fail:
  * a planted person holding two INCOMPATIBLE affiliations at full intensity, at a non-zero arm,
    ranks a candidate pair the other way round from the control arm -- a `score` that never read
    `confliction` could not flip it;
  * the control arm `0` gives the ranking the pursuit dot gives on its own;
  * the same person holding a COMPATIBLE pair (confliction 0) at the same non-zero arm is unmoved --
    so the flip is the strain's, not the arm's alone.
The pairs and verbs are read from the loaded tables, not typed, so no roster name is copied here.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE, align
from ..decision import choose as CH
from ..decision.options import project
from ..queries.person_q import confliction
from ..state.carriers import Candidate, Person
from engine.substrate.descriptors import AFFILIATION_CEILING

from ._scar_helpers import compatible_pairs, incompatible_pairs

_HI_SUBJECT, _LO_SUBJECT = "p_h6f_a", "p_h6f_b"


def _pairs():
    bad, good = incompatible_pairs(), compatible_pairs()
    assert bad, "no incompatible pair is loaded: the confliction term has nothing to read"
    assert good, "no compatible pair is loaded: the control below has no subject"
    return bad[0], good[0]


def _verbs(p: Person):
    """The highest- and lowest-pulling verbs for `p` under the bare pursuit dot, read off the table."""
    axis_w = project(p)
    pull = {v: sum(axis_w[ax] * align(v, ax) for ax in PURSUIT_AXES) for v in sorted(VERB_TABLE)}
    hi, lo = max(pull, key=pull.get), min(pull, key=pull.get)
    assert pull[hi] > pull[lo], "every verb pulls alike: no ranking to flip"
    return hi, lo, pull[hi] - pull[lo]


def _person(pair) -> Person:
    p = Person(id="p_h6f", name="p_h6f")
    p.pursuits = dict(virtue=1.0)
    p.conviction = {a: AFFILIATION_CEILING for a in pair}
    return p


def _ranking(p: Person, k: float, monkeypatch) -> list:
    hi, lo, gap = _verbs(p)
    # the regard the low verb's subject carries makes up 3/4 of the pursuit gap: at the bare dot the
    # high verb still wins; once the dot is damped below 3/4 of itself, regard wins.
    p.stance = [(_LO_SUBJECT, 0.75 * gap, 1.0)]
    cands = [Candidate(hi, _HI_SUBJECT), Candidate(lo, _LO_SUBJECT)]
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [c.verb for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    # `stance_gain` (H-202) at its CONTROL 0, explicitly: the 3/4 share above is calibrated against
    # §F2's stance weight 1, and the gain ships live (Jordan, 2026-10-09), which would double the
    # stance term and flip the control arm by the stance's weight rather than by the strain's.
    fx = (DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("stance_gain", 0.0)
          .sweep("confliction_weight", k))
    choose = CH.make_chooser(fx, lambda *a: "act")
    choose(p, SimpleNamespace(question=object()), SimpleNamespace(subsistence=0), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"], hi, lo


def test_6f_strain_flips_a_ranking_the_control_keeps(monkeypatch):
    bad, _ = _pairs()
    p = _person(bad)
    assert confliction(p) == AFFILIATION_CEILING, "the planted pair is not in strain"
    control, hi, lo = _ranking(p, 0, monkeypatch)
    assert control == [hi, lo], f"the control arm did not keep the pursuit dot's order: {control}"
    armed, _, _ = _ranking(p, 1.0, monkeypatch)
    assert armed == [lo, hi], (
        f"two incompatible affiliations at full intensity, arm 1, left the order at {armed}: "
        "`score` does not read `confliction`")


def test_6f_a_compatible_pair_at_the_same_arm_is_unmoved(monkeypatch):
    _, good = _pairs()
    p = _person(good)
    assert confliction(p) == 0
    armed, hi, lo = _ranking(p, 1.0, monkeypatch)
    assert armed == [hi, lo], f"the arm moved a person in no strain: {armed}"


def test_6f_a_negative_arm_is_refused(monkeypatch):
    bad, _ = _pairs()
    with pytest.raises(ValueError, match="confliction_weight"):
        _ranking(_person(bad), -1.0, monkeypatch)
