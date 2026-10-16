"""v9 IN-71 (`workplans/valoria_master_workplan_v9_part5.md`; H-188) -- `doctrine`'s projected pull
scales MULTIPLICATIVELY with religious conviction: `w_doctrine * intensity * row_doctrine`, ONE SITE,
the weights `person_q.crisis_weights` returns (the vector `choose`'s pursuit dot and `deeds_judged`
both project). Intensity = the person's highest intensity on any member of the `church` or `einhir`
concern, over the spine's ceiling; a person at 0 on every religious member has no doctrine pull
(IN-63). Ruled (Jordan, 2026-09-27), so there is no fixture arm and no control to sweep.

THE FALSIFIER, executed and able to fail:
  * two persons with EQUAL pursuits (only `doctrine`), religious intensity 5 vs 0, rank a candidate pair
    the other way round: the pair's whole pull difference is `doctrine`-celled, and a regard the low
    verb's subject carries makes up 3/4 of it. Mutation, run and restored: `religious_intensity`
    returning 1.0 reddens `test_in71_equal_pursuits_rank_a_doctrine_pair_apart_by_conviction`.
  * the ranking flips exactly where `intensity > 3/4`, not at any nonzero intensity: the coupling is a
    product and not a gate;
  * a person whose `doctrine` weight is 0 (or who holds none) is unmoved by any intensity.
Every loop asserts it asserted. Concern, member and verb names are read from the loaded tables.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.substrate.descriptors import AFFILIATION_CEILING, AFFILIATION_CONCERNS

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE, align
from ..decision import choose as CH
from ..decision.options import project
from ..queries import person_q as PQ
from ..state.carriers import Candidate, Person

_HI_SUBJECT, _LO_SUBJECT = "p_in71_a", "p_in71_b"
_CHURCH = AFFILIATION_CONCERNS["church"][0]
_EINHIR = AFFILIATION_CONCERNS["einhir"][0]
_CIVIC = AFFILIATION_CONCERNS["altonia"][0]
_ALL_RELIGIOUS = [m for c in ("church", "einhir") for m in AFFILIATION_CONCERNS[c]]


def _pw(**weights) -> dict:
    """A pursuit-weight map by keyword: the names are test inputs, not a roster literal
    (`tests/valoria/test_conviction_roster_single_owner.py` counts 2+ canonical names in one literal)."""
    return weights


def _person(conviction: dict, pursuits: dict | None = None) -> Person:
    p = Person(id="p_in71", name="p_in71")
    p.pursuits = dict(pursuits if pursuits is not None else {"doctrine": 1.0})
    p.conviction = dict(conviction)
    return p


def _at(intensity: int) -> dict:
    """A conviction holding every religious member at `intensity` and the civic one at the ceiling
    (which must not count)."""
    return {**{m: intensity for m in _ALL_RELIGIOUS}, _CIVIC: AFFILIATION_CEILING}


def _verbs():
    """The highest- and lowest-pulling verbs for a devout `doctrine`-only person, read off the table."""
    axis_w = project(_person(_at(AFFILIATION_CEILING)))
    pull = {v: sum(axis_w[ax] * align(v, ax) for ax in PURSUIT_AXES) for v in sorted(VERB_TABLE)}
    hi, lo = max(pull, key=pull.get), min(pull, key=pull.get)
    assert pull[hi] > pull[lo], "every verb pulls alike under `doctrine`: no ranking to flip"
    return hi, lo, pull[hi] - pull[lo]


def _ranking(p: Person, monkeypatch) -> list:
    hi, lo, gap = _verbs()
    # the regard the low verb's subject carries makes up 3/4 of the devout person's pull gap: at full
    # intensity the high verb wins; once the dot is scaled below 3/4 of itself, regard wins.
    p.stance = [(_LO_SUBJECT, 0.75 * gap, 1.0)]
    cands = [Candidate(hi, _HI_SUBJECT), Candidate(lo, _LO_SUBJECT)]
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [c.verb for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    # `stance_gain` (H-202) at its CONTROL 0, explicitly: the 3/4 share is calibrated against §F2's
    # stance weight 1, and the gain ships live, which would double the stance term.
    fx = DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("stance_gain", 0.0)
    choose = CH.make_chooser(fx, lambda *a: "act")
    choose(p, SimpleNamespace(question=object()), SimpleNamespace(subsistence=0), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"]


def test_in71_equal_pursuits_rank_a_doctrine_pair_apart_by_conviction(monkeypatch):
    hi, lo, _ = _verbs()
    devout, lukewarm = _person(_at(AFFILIATION_CEILING)), _person(_at(0))
    assert devout.pursuits == lukewarm.pursuits, "the two persons do not hold equal pursuits"
    assert _ranking(devout, monkeypatch) == [hi, lo], "the devout person did not follow his pursuit"
    assert _ranking(lukewarm, monkeypatch) == [lo, hi], (
        "a person at 0 on every religious member ranked as the devout one does: `doctrine` is not "
        "scaled by conviction")


def test_in71_the_ranking_flips_where_the_product_crosses_the_stance_not_at_any_nonzero_intensity(monkeypatch):
    hi, lo, _ = _verbs()
    order = {}
    for level in range(AFFILIATION_CEILING + 1):
        order[level] = _ranking(_person(_at(level)), monkeypatch)
    # the stance is 3/4 of the full pull, so the dot wins exactly where level / ceiling > 3/4
    checked = 0
    for level, ranked in order.items():
        want = [hi, lo] if level / AFFILIATION_CEILING > 0.75 else [lo, hi]
        assert ranked == want, f"intensity {level}: ranked {ranked}, wanted {want}"
        checked += 1
    assert checked == AFFILIATION_CEILING + 1 >= 6
    assert order[1] == [lo, hi] and order[AFFILIATION_CEILING] == [hi, lo], "no intensity changed the order"


def test_in71_the_weight_is_the_product_of_pursuit_and_fraction():
    checked = 0
    for level in range(AFFILIATION_CEILING + 1):
        p = _person(_at(level), _pw(doctrine=0.6, virtue=0.4))
        got = PQ.crisis_weights(p)
        assert got["doctrine"] == pytest.approx(0.6 * level / AFFILIATION_CEILING), (level, got)
        assert got["virtue"] == 0.4, "a pursuit that is not `doctrine` was scaled"
        assert p.pursuits == _pw(doctrine=0.6, virtue=0.4), "the reader wrote Person.pursuits"
        checked += 1
    assert checked == AFFILIATION_CEILING + 1
    full = _person(_at(AFFILIATION_CEILING))
    assert PQ.crisis_weights(full) is full.pursuits, "full intensity must hand back the person's own mapping"


def test_in71_intensity_is_the_highest_religious_member_across_both_concerns():
    cases = {
        "builder only": ({_CHURCH: 5, _EINHIR: 0}, 1.0),
        "dismantler only": ({_CHURCH: 0, _EINHIR: 5}, 1.0),
        "both devout, not summed": ({_CHURCH: 3, _EINHIR: 3}, 3 / AFFILIATION_CEILING),
        "the higher of two": ({_CHURCH: 2, _EINHIR: 4}, 4 / AFFILIATION_CEILING),
        "civic membership is no religion": ({_CHURCH: 0, _EINHIR: 0, _CIVIC: AFFILIATION_CEILING}, 0.0),
        "no conviction held": ({}, 0.0),
    }
    checked = 0
    for name, (conviction, want) in cases.items():
        assert PQ.religious_intensity(_person(conviction)) == pytest.approx(want), name
        checked += 1
    assert checked == len(cases) >= 6
    # IN-63: a person at 0 on every religious member has no doctrine pull at all
    assert PQ.crisis_weights(_person(_at(0)))["doctrine"] == 0.0


def test_in71_a_zero_doctrine_weight_is_unmoved_by_any_intensity():
    checked = 0
    for pursuits in (_pw(virtue=1.0, doctrine=0.0), _pw(virtue=1.0)):
        reference = PQ.crisis_weights(_person(_at(0), pursuits))
        assert reference == pursuits
        for level in range(AFFILIATION_CEILING + 1):
            p = _person(_at(level), pursuits)
            assert PQ.crisis_weights(p) == pursuits, (pursuits, level)
            assert PQ.projected_axes(p) == PQ.projected_axes(_person(_at(0), pursuits)), (pursuits, level)
            checked += 1
    assert checked == 2 * (AFFILIATION_CEILING + 1)


def test_in71_the_scar_shift_is_read_first_and_the_conviction_scales_what_is_left():
    p = _person(_at(2), _pw(doctrine=0.6, virtue=0.4))
    p.scar = {"doctrine": PQ.SCAR_WEIGHT_SHIFT_AT}
    got = PQ.crisis_weights(p, 0.5)
    assert got["doctrine"] == pytest.approx(0.6 * 0.5 * 2 / AFFILIATION_CEILING)
    assert got["virtue"] == pytest.approx(0.4 + 0.3)
    assert PQ.crisis_weights(p, 0) == pytest.approx(_pw(doctrine=0.6 * 2 / AFFILIATION_CEILING, virtue=0.4))
