"""The balance oracle's arms still construct, and they still differ (ED-SC-0032).

WHY THIS EXISTS, and why it is not apparatus-guarding-apparatus. `tools/balance_oracle.py` is the
n>=100 campaign balance instrument CLAUDE.md §7 names, and ED-SC-0031 cited its `--n 120` run as
THE control licensing six golden re-pins. It is deliberately NOT a CI gate — 240 campaigns take
~13 minutes and a gate that slow gets skipped. The consequence is that nothing executes it, so it
has no freshness relationship to the code it measures.

That consequence bit within one commit. ED-SC-0032 moved `degree` and `OVERWHELM_SIGMA` out of
`engine/autoload/sigma_leverage.py` into the subsystem that owns them, and the oracle's live arm
read both off the engine. `python3 tools/balance_oracle.py` raised AttributeError on its first
arm — the instrument that produced the previous commit's control, disabled by that commit's own
successor, found by an adversarial pass rather than by anything automated.

CLAUDE.md §0.1 point 5 admits this guard: the defective artifact is load-bearing on a JORDAN
DECISION and on the game — its output is what a golden re-pin is justified by, and a broken arm
either raises (loud) or, worse, silently produces two identical arms and a meaningless z. The
guard is cheap by construction: it constructs and undoes the arms and bands a handful of values.
It runs NO campaigns, so it costs milliseconds and can never become the slow gate the oracle
deliberately is not.

FALSIFIER: `test_the_pre_ruling_arm_actually_changes_the_ladder` fails if an arm stops reaching
the contest's degree path — which is exactly what a moved binding does, and what would have made
a reported balance result worthless.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))


@pytest.fixture(scope="module")
def oracle():
    """Load the tool by path — it is a script, not an importable package member."""
    spec = importlib.util.spec_from_file_location(
        "_balance_oracle_probe", REPO / "tools" / "balance_oracle.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_every_arm_constructs_and_undoes(oracle):
    """The failure this file exists for: an arm whose symbols moved raises on setup."""
    assert len(oracle.ARMS) == 2, f"expected exactly two arms, got {sorted(oracle.ARMS)}"
    for name, setup in oracle.ARMS.items():
        undo = setup()
        assert callable(undo), f"arm {name!r} returned a non-callable undo"
        undo()


def test_the_pre_ruling_arm_actually_changes_the_ladder(oracle):
    """THE FALSIFIER. Two arms that band identically are a fake control, not a null result.

    `degree(3, 3)` is the cell Jordan's 2026-08-14 ruling moved — Success under the retired
    private ladder, Partial under the owner's. If the arm no longer reaches the contest's path,
    this reads 1 in both arms and fails.
    """
    from systems.social_contest.sim.contest import degree_extension as CD
    from systems.social_contest.sim.contest import resolver as R

    baseline = CD.degree(3, 3)
    undo = oracle.ARMS['private_ladder']()
    try:
        patched_adapter = CD.degree(3, 3)
        patched_ladder = R.degree_from_net(3, 3)
    finally:
        undo()

    assert baseline == 1, f"the owner's ladder bands degree(3,3) as {baseline}, expected Partial"
    assert patched_adapter == 2, (
        "the private_ladder arm did not change the contest adapter's answer — the arm has lost "
        "its grip on the degree path and any balance result from it would be fake")
    assert patched_ladder.value == "success", (
        "the private_ladder arm did not change the LIVE resolver binding — `resolver._reception` "
        "would still run the owner's ladder in both arms")
    assert CD.degree(3, 3) == baseline, "the arm's undo did not restore the owner's ladder"


def test_the_owner_arm_is_a_true_no_op(oracle):
    """The control arm must change nothing at all, or the comparison has two treatments."""
    from systems.social_contest.sim.contest import degree_extension as CD
    from systems.social_contest.sim.contest import resolver as R

    before = ([CD.degree(n, 2, p) for n in range(0, 9) for p in (None, 2, 8, 20)],
              R.degree_from_net)
    undo = oracle.ARMS['owner_ladder']()
    try:
        during = ([CD.degree(n, 2, p) for n in range(0, 9) for p in (None, 2, 8, 20)],
                  R.degree_from_net)
    finally:
        undo()
    assert during == before


def test_the_retired_pair_definitions_still_import(oracle):
    """The retired comparisons are kept as the record of what the old behaviour WAS.

    They are the only surviving statement of three superseded mechanics, so a rename that breaks
    them silently deletes that record. Constructing them is enough to prove the symbols resolve.
    """
    for attr in ('_ARMS_POOL', '_ARMS_FLOOR', '_ARMS_BOUNDS'):
        retired = getattr(oracle, attr)
        assert len(retired) == 2, f"{attr} should keep both arms of its pair"
        for setup in retired.values():
            setup()()
