"""`harness/soak.py`'s two grades (plan position IN-20, STORY-SOAK): flat cost per season, and
convergence of the act mix. Both graders are pure functions over plain data, so each test PLANTS the
failure it claims to catch and also runs a control that must pass -- a grader that fails everything
would satisfy a falsifier test alone.

Thresholds below are the TEST's own arguments to the grader, chosen only to separate a planted series
from a control; they are not engine values and pin nothing about the game.
"""

from __future__ import annotations

import argparse
import json

from ..harness import soak as S

COST_CEIL = 1.5
DRIFT_CEIL = 0.2
TOP_CEIL = 0.8

# a diverse, steady mix over three verbs
STEADY = {"tell": 5, "give": 3, "march": 2}


def test_flat_cost_passes_and_planted_growth_fails():
    flat = [3.0, 3.1, 2.9, 3.0, 3.05, 2.95, 3.0, 3.1]
    growing = [3.0 * (1.5 ** i) for i in range(8)]            # per-season cost growth, planted
    g_flat = S.grade_cost(flat, COST_CEIL)
    g_grow = S.grade_cost(growing, COST_CEIL)
    assert g_flat["grade"] == "PASS", g_flat                  # the control is not trivially failing
    assert g_grow["grade"] == "FAIL", g_grow                  # the planted growth is caught
    assert g_grow["ratio"] > COST_CEIL > g_flat["ratio"]


def test_cost_that_plateaued_inside_the_first_half_still_passes():
    # grew, then stopped: the grade asks whether cost is STILL growing
    plateau = [1.0, 4.0, 9.0, 9.0, 9.1, 8.9, 9.0, 9.0]
    assert S.grade_cost(plateau, COST_CEIL)["grade"] == "PASS"


def test_one_stalled_season_is_not_growth():
    spike = [3.0, 3.0, 3.0, 3.0, 3.0, 90.0, 3.0, 3.0]
    assert S.grade_cost(spike, COST_CEIL)["grade"] == "PASS"   # medians, not means


def test_cost_edge_cases_are_not_silent():
    assert S.grade_cost([1.0, 2.0, 3.0], COST_CEIL)["grade"] == "UNGRADED"
    zero_then_cost = S.grade_cost([0.0, 0.0, 1.0, 1.0], COST_CEIL)
    assert zero_then_cost["grade"] == "FAIL"                   # growth from nothing is unbounded
    assert S.grade_cost([0.0, 0.0, 0.0, 0.0], COST_CEIL)["grade"] == "PASS"


def test_convergent_mix_passes_and_planted_single_act_mix_fails():
    convergent = [dict(STEADY) for _ in range(8)]
    single = [{"tell": 10} for _ in range(8)]                  # one act, every season
    g_ok = S.grade_mix(convergent, DRIFT_CEIL, TOP_CEIL)
    g_single = S.grade_mix(single, DRIFT_CEIL, TOP_CEIL)
    assert g_ok["grade"] == "PASS", g_ok                      # the control passes
    assert g_single["grade"] == "FAIL", g_single               # the planted collapse is caught
    # it fails on COLLAPSE, not drift: a single-act mix holds perfectly still
    assert g_single["drift"] == 0.0
    assert g_single["top_share"] == 1.0 > TOP_CEIL
    assert any("collapsed" in r for r in g_single["reasons"])


def test_mix_that_is_still_moving_fails_on_drift():
    early = [{"tell": 5, "give": 5} for _ in range(4)]
    late_a = [{"tell": 5, "give": 5} for _ in range(2)]
    late_b = [{"march": 5, "give": 5} for _ in range(2)]       # the mix changes shape at the end
    g = S.grade_mix(early + late_a + late_b, DRIFT_CEIL, TOP_CEIL)
    assert g["grade"] == "FAIL" and g["drift"] > DRIFT_CEIL, g
    assert any("drift" in r for r in g["reasons"])
    # last block {march:10, give:10} against the block before {tell:10, give:10}: shares .5/.5 on
    # both sides, differing on two verbs by .5 each, so 0.5 * (.5 + .5) -- exact, and 1.0 if the
    # half-sum factor were dropped
    assert g["drift"] == 0.5


def test_mix_that_churned_early_and_settled_in_the_last_blocks_passes():
    churned = [{"march": 5, "give": 5} for _ in range(4)]
    g = S.grade_mix(churned + [dict(STEADY) for _ in range(4)], DRIFT_CEIL, TOP_CEIL)
    assert g["grade"] == "PASS" and g["drift"] == 0.0, g       # only the final two blocks are read


def test_mix_that_collapses_over_the_run_fails():
    diverse = [dict(STEADY) for _ in range(4)]
    collapsing = [{"tell": 10}, {"tell": 10}, {"tell": 10}, {"tell": 10}]
    assert S.grade_mix(diverse + collapsing, DRIFT_CEIL, TOP_CEIL)["grade"] == "FAIL"


def test_mix_that_stops_acting_fails_and_short_runs_are_ungraded():
    assert S.grade_mix([dict(STEADY)] * 4 + [{}] * 4, DRIFT_CEIL, TOP_CEIL)["grade"] == "FAIL"
    assert S.grade_mix([dict(STEADY)] * 3, DRIFT_CEIL, TOP_CEIL)["grade"] == "UNGRADED"
    # seven seasons would make blocks of ONE season: one season against one, which the grade refuses
    assert S.grade_mix([dict(STEADY)] * 7, DRIFT_CEIL, TOP_CEIL)["grade"] == "UNGRADED"
    assert S.grade_mix([dict(STEADY)] * 8, DRIFT_CEIL, TOP_CEIL)["grade"] == "PASS"


def _write_world(world_dir, costs, mixes):
    """The two files `soak._run_world` writes, with only the fields the grades read."""
    rows, acts = [], []
    for i, (c, m) in enumerate(zip(costs, mixes)):
        rows.append({"batch": i // 4, "season": i % 4, "wall_s": c})
        for verb, n in m.items():
            acts.extend({"batch": i // 4, "season": i % 4, "verb": verb} for _ in range(n))
    (world_dir / "seasons.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    (world_dir / "acts.jsonl").write_text("".join(json.dumps(r) + "\n" for r in acts))


def _args(**kw):
    base = {"cost_growth_ceiling": None, "mix_drift_ceiling": None,
            "mix_top_share_ceiling": None}
    base.update(kw)
    return argparse.Namespace(**base)


def test_grade_run_reads_a_written_world_and_names_a_missing_ceiling(tmp_path):
    flat = [3.0] * 8
    _write_world(tmp_path, flat, [dict(STEADY) for _ in range(8)])
    costs, mixes = S.load_series(tmp_path)
    assert costs == flat and mixes == [dict(STEADY)] * 8       # batches 0 and 1 stay in order

    cost, mix, lines = S.grade_run(tmp_path, _args(
        cost_growth_ceiling=COST_CEIL, mix_drift_ceiling=DRIFT_CEIL,
        mix_top_share_ceiling=TOP_CEIL))
    assert (cost["grade"], mix["grade"]) == ("PASS", "PASS")
    assert sum(1 for ln in lines if ln.startswith("  season ")) == 8   # one line per season
    assert any(ln.startswith("soak grade cost: PASS") for ln in lines)
    assert any(ln.startswith("soak grade act-mix convergence: PASS") for ln in lines)

    cost, mix, _ = S.grade_run(tmp_path, _args(mix_drift_ceiling=DRIFT_CEIL))
    assert cost["grade"] == "UNGRADED" and "--cost-growth-ceiling" in cost["why"]
    assert mix["grade"] == "UNGRADED" and "--mix-top-share-ceiling" in mix["why"]


def test_grade_run_fails_a_planted_world_end_to_end(tmp_path):
    _write_world(tmp_path, [3.0 * (1.5 ** i) for i in range(8)], [{"tell": 10}] * 8)
    cost, mix, _ = S.grade_run(tmp_path, _args(
        cost_growth_ceiling=COST_CEIL, mix_drift_ceiling=DRIFT_CEIL,
        mix_top_share_ceiling=TOP_CEIL))
    assert (cost["grade"], mix["grade"]) == ("FAIL", "FAIL")
