"""IN-19 -- `harness/storybar.py`, the M2 instrument. These tests pin the INSTRUMENT, never its
numbers (the same stance as `test_aperture.py`): what a season's cause graph reads is the
measurement and it moves whenever the game does.

The falsifier the plan names, observed rather than assumed:
  * a planted severed antecedent edge DROPS the cross-person share -- on a real seeded run, against
    an unplanted copy of the same log that must read identically (so the planting path alone moves
    nothing);
  * forcing off, the two arms read EQUAL -- `--arms off off` is the only comparison this tree can
    run, since no forcing source is built, and an unbuilt arm is refused rather than invented.
"""

from __future__ import annotations

import dataclasses
from types import SimpleNamespace as NS

import pytest

from ..harness import storybar as SB

SEED, SEASONS, CAP = 0, 2, 10


@pytest.fixture(scope="module")
def driven():
    return SB.drive(SEED, SEASONS, "off", CAP)


def _copy_log(log, act_of, sever_aid=None, sever_from=None):
    """A copy of the log with fresh Event objects (and `act_of` re-keyed onto them). When
    `sever_aid` is given, every cause of that act's Events that names an Event of act `sever_from`
    is removed -- one severed antecedent edge."""
    events, new_act_of = [], {}
    for e in log:
        a = act_of.get(e.id)
        causes = list(e.causes)
        if sever_aid is not None and a is not None and a.id == sever_aid:
            causes = [c for c in causes
                      if getattr(act_of.get(c), "id", None) != sever_from]
        e2 = dataclasses.replace(e, causes=causes)
        events.append(e2)
        if a is not None:
            new_act_of[e2.id] = a
    return events, new_act_of


def test_a_severed_antecedent_edge_drops_the_cross_person_share(driven):
    w, d, bounds = driven
    base = SB.read(w.log, d.act_of, bounds)
    # one act with exactly one cross-person antecedent act, so severing that edge must reclassify it
    target = next((aid for aid, r in base["acts"].items() if len(r["cross"]) == 1), None)
    assert target is not None, (
        "no act in the run has exactly one cross-person antecedent; the falsifier observed nothing")
    severed_from = base["acts"][target]["cross"][0]

    control_log, control_act_of = _copy_log(w.log, d.act_of)
    control = SB.read(control_log, control_act_of, bounds)
    base_ps = SB.per_season(base["acts"].values(), SEASONS)
    assert SB.per_season(control["acts"].values(), SEASONS) == base_ps, (
        "copying the log moved the reading; the planted arm below would not isolate the edge")

    planted_log, planted_act_of = _copy_log(w.log, d.act_of, target, severed_from)
    planted = SB.read(planted_log, planted_act_of, bounds)
    assert planted["acts"][target]["cls"] != "cross"
    planted_ps = SB.per_season(planted["acts"].values(), SEASONS)

    checked = 0
    season = base["acts"][target]["season"]
    for s in range(SEASONS):
        b_this, b_cum = base_ps[s]
        p_this, p_cum = planted_ps[s]
        if s >= season:
            assert p_cum["cross_share"] < b_cum["cross_share"], (s, b_cum, p_cum)
            assert p_cum["classes"]["cross"] == b_cum["classes"]["cross"] - 1
            checked += 1
        if s == season:
            assert p_this["cross_share"] < b_this["cross_share"], (s, b_this, p_this)
            checked += 1
    assert checked >= 2, f"the drop was asserted {checked} time(s); expected at least 2"


def test_forcing_off_the_two_arms_read_equal():
    res = SB.compare(("off", "off"), [SEED], 1, CAP)
    a, b = res[0]["pooled"], res[1]["pooled"]
    assert a[0][0]["acts"] > 0, "the arms read no acts; their equality would be vacuous"
    assert a == b
    assert res[0]["seeds"] == res[1]["seeds"]


def test_an_unbuilt_forcing_arm_is_refused_not_invented():
    assert SB.ARMS == ("off",)
    with pytest.raises(ValueError):
        SB.drive(SEED, 1, "on", CAP)


def test_depth_runs_along_cross_person_edges_only():
    """A hand-built graph: p1's act -> p2's act -> p3's act is depth 3; p3's own follow-up is
    classed `own` and stays depth 1; an act caused only by an actorless Event is `world`."""
    acts = {k: NS(id=k, actor=p) for k, p in
            (("a1", "p1"), ("a2", "p2"), ("a3", "p3"), ("a4", "p3"), ("a5", "p1"))}
    ev = lambda i, causes: NS(id=i, causes=causes)
    log = [ev("m0", []),                      # an actorless Event (MATTER)
           ev("e1", ["a1"]),
           ev("e2", ["a2", "e1"]),
           ev("e3", ["a3", "e2"]),
           ev("e4", ["a4", "e3"]),
           ev("e5", ["a5", "m0"])]
    act_of = {"e1": acts["a1"], "e2": acts["a2"], "e3": acts["a3"], "e4": acts["a4"],
              "e5": acts["a5"]}
    r = SB.read(log, act_of, [0])["acts"]
    assert {k: (v["cls"], v["depth"]) for k, v in r.items()} == {
        "a1": ("none", 1), "a2": ("cross", 2), "a3": ("cross", 3),
        "a4": ("own", 1), "a5": ("world", 1)}
