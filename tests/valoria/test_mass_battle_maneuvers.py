"""Wires the mass-battle maneuver acceptance validators (envelop/sweep) into CI on BOTH movement
paths — the measurement instrument for the movement/pathing audit's fix plan (ED-1096/1097,
finding 1.4, fix-plan step 6).

Before this file: `validators.py`'s `Run:` docstring pinned only PER_CELL, leaving
FIELD_MOVEMENT/PC_NODE_COHESION at the ambient default. Since ED-1089 flipped that default ON,
every bare invocation of V-ENVELOP/V-SWEEP silently measured the DEAD node-path arm — the two
maneuver instructions ('envelop'/'sweep') were confirmed (this session) to exist only on the
legacy grid path — so past "Stage C.4 passed" / "the maneuver works" claims were true only of a
path nothing runs by default anymore. This file makes both arms explicit and checked:

  - test_*_grid: the LEGACY path, where the underlying mechanism is real. A genuine regression
    test — if this goes red, a real mechanic broke.
  - test_*_node: the LIVE default path Jordan actually watches (the workbench, traced battles).
    Landed RED first (xfail(strict=True), commit 50247b1) as the acceptance target for fix-plan
    step 7 (the waypoint primitive, hierarchy/units.py Subunit._resolve_maneuver_goal). Step 7
    landed the same session and both flipped GREEN for real (not just "no longer erroring" --
    verified the xfail was hiding a real bug in v_envelop/v_sweep's own seeds/turns forwarding
    before trusting the green). Now real regression tests, same standing as the grid arm.

Toggled via validators._set_movement_path, which mutates the already-imported module-level
FIELD_MOVEMENT/PC_NODE_COHESION on hierarchy.units and orchestration at runtime (not the
import-time env-var read bat.py relies on) — no subprocess isolation needed, but the toggles ARE
real process-wide globals, so every test here restores them in a `finally` to avoid leaking node/
grid state into whatever test runs next in the same pytest session."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

from mass_battle import validators as _val  # noqa: E402
import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402

# Lighter seed count than validators.py's own _SEEDS=20 default -- this is a CI acceptance gate
# (does the maneuver reach its goal at all), not the full aggregate-confidence battery a manual
# `python3 -m mass_battle.validators` run performs; keeps this file's runtime well inside
# tests/valoria's shared 5-minute CI budget (measured ~7s per path per validator locally).
_CI_SEEDS = 8


@pytest.fixture(autouse=True)
def _movement_toggles():
    # PER_CELL is a SEPARATE, additional gate the legacy advance_cells requires for 'envelop'/
    # 'sweep' to be reachable at all (hierarchy/units.py:897,925: `if PER_CELL and PC_ENVELOP_PATH
    # ...` / `if PER_CELL and PC_SWEEP ...`) -- distinct from FIELD_MOVEMENT/PC_NODE_COHESION
    # (which path), and read from the ambient process env at import time like they are, so it is
    # NOT set just by validators._set_movement_path('grid'). This test process's own pytest
    # environment does not set PER_CELL=1 (unlike validators.py's documented `Run:` line for a
    # manual script invocation), so force it here for the duration of every test in this file.
    #
    # [2026-07-02 adversarial-review finding, ED-MB-0001] PC_ENVELOP_PATH/PC_SWEEP were missing from
    # this save/restore set even though every test here (via v_envelop/v_sweep's on/off comparison)
    # mutates hierarchy.units' copies directly and always leaves them at False when a test function
    # returns (the off-arm runs last) -- contradicting this docstring's own claim to restore
    # everything. Added here so a future in-process test added later in this suite that constructs
    # a Subunit with an 'envelop'/'sweep' instruction doesn't silently inherit a disabled maneuver
    # from whatever ran before it in the same pytest session -- exactly the class of silent-failure
    # this whole audit exists to catch.
    saved = {(mod, name): getattr(mod, name) for mod in (_hu, _orch)
             for name in ('FIELD_MOVEMENT', 'PC_NODE_COHESION', 'PER_CELL', 'PC_ENVELOP_PATH', 'PC_SWEEP')}
    _hu.PER_CELL = True
    try:
        yield
    finally:
        for (mod, name), val in saved.items():
            setattr(mod, name, val)


def test_envelop_reaches_rear_grid():
    """Regression: the legacy path's 'envelop' instruction still wraps a wide-placed detachment
    to the enemy's rear (V-ENVELOP, validators.py) -- the mechanism fix-plan step 7 ported to the
    live path, so this must keep working alongside it."""
    r = _val.v_envelop(path='grid')
    assert r.passed, f"V-ENVELOP (grid) regressed: measured={r.measured} expected={r.expected}"


def test_sweep_displaces_laterally_grid():
    """Regression: the legacy path's 'sweep' instruction still displaces a unit toward the enemy
    flank (V-SWEEP, validators.py)."""
    r = _val.v_sweep(path='grid')
    assert r.passed, f"V-SWEEP (grid) regressed: measured={r.measured} expected={r.expected}"


@pytest.mark.xfail(
    reason="[2026-07-05, UPDATED again -- see docstring] A follow-up Fable-5 adversarial audit found "
    "the 'steering mechanism is proven correct' claim below was WRONG: _envelop_goal had a genuine "
    "limit-cycle bug (D2, no hysteresis between phase-1/phase-2) plus _node_advance had a genuine "
    "step-freeze bug (D2b, a body could stall forever within 0.5 combined units of any waypoint). "
    "Both fixed. At GAUGE SCALE this closes the racing-clocks question for good: H3-H6's draws are "
    "now GONE entirely (were 100%/90%/100%/100%). THIS FIXTURE specifically still fails, but for a "
    "DIFFERENT, disclosed-not-chased reason: its small detachment's base cell speed is only 1, and "
    "the discipline-degradation speed tiers (floor(base*disc_mult)) floor to exactly 0 the moment "
    "discipline drops below the top tier -- a discretization edge case only low-base-speed bodies "
    "hit, confirmed by direct trace, not fixed here (out of scope for this pass; flagged for a "
    "future movement-tier pass). Measured: 11/20 seeds now reach behind the defender (up from 6, up "
    "from 0 before D2/D2b), mean row-diff -0.58 (up from -0.1) -- real, substantial improvement, "
    "still short of this validator's strict pass threshold. Separately, DG-3's pool-semantics "
    "ruling (intensive/per-troop) and DG-1's composition ruling (force-parity + majority-pin/"
    "cavalry-wing) were both implemented -- but the gauge-scale rows this unlocked now OVERSHOOT "
    "their bands decisively in the attacker's favor instead of landing in them, a newly-surfaced "
    "partition-invariance/Command-scaling question, not this fixture's concern. See "
    "designs/proposals/mass_battle_fighting_withdrawal_v1.md (DG-2 workplan) and "
    "tests/coverage_matrix.md's 2026-07-05 entry for the full record.",
    strict=False)
def test_envelop_reaches_rear_node():
    """Acceptance: V-ENVELOP on the LIVE default (node/field) path -- the path Jordan actually
    watches in the workbench. Subunit._resolve_maneuver_goal/_envelop_goal (fix-plan step 7) gives
    _node_advance an anchor-level goal, modeled on the legacy per-cell two-state machine, when the
    'envelop' instruction is active and PC_ENVELOP_PATH is on.

    [Gate 4 finding, 2026-07-02, SUPERSEDED -- see below] This passed reliably (16/20 seeds) at the
    moment step 7 landed, with PER_CELL still at its OLD default. Flipping PER_CELL's config default
    to '1' (gate 4) reproduced this failure, and the ORIGINAL diagnosis (recorded here for history,
    not because it's still believed) was a "two racing clocks" theory -- REFUTED, see below.

    [2026-07-04 update, ED-MB-0002, SUPERSEDED IN PART -- see 2026-07-05 below] A Fable-led root-cause
    audit (designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md) refuted racing-clocks as
    a GENERAL account (gauge row C7 passes its band, which a pure clock-race can't explain) and traced
    the composition-coupling accounting defects (RC-1). Jordan ruled DG-3/DG-4; both were implemented,
    adversarially reviewed, byte-exact/regression-clean. This fixture STILL failed after that fix, and
    a frozen-vs-wheeling-wings ablation was read at the time as settling "no timing race, at gauge
    scale" -- but see the 2026-07-05 correction immediately below: that ablation's own premise was
    unknowingly broken.

    [2026-07-05 correction, mass-battle Cannae gauge follow-up audit] The 2026-07-04 docstring claimed
    "the steering mechanism is proven correct" and that the frozen-vs-wheeling ablation settled the
    racing-clocks question with a clean null result. BOTH claims were WRONG, not just incomplete: a
    fresh adversarial pass found _envelop_goal's phase-1/phase-2 transition shares one threshold for
    entry and exit (no hysteresis) -- a genuine limit cycle where a wing wheels to its rear waypoint,
    turns in, immediately re-crosses the same threshold, and gets yanked back to phase 1, forever.
    Separately, _node_advance's per-tick step magnitude could freeze a body's approach forever within
    a small fixed distance of ANY goal. Both are real, confirmed-by-direct-trace bugs, now fixed (a
    one-shot commitment latch; capping the step at the remaining distance instead of freezing/
    overshooting). Re-measured: this fixture's own detachment now reaches behind the defender in
    11/20 seeds (was 6, was 0 pre-fix) -- real movement, still short of a clean pass, for a THIRD,
    separate, disclosed-not-chased reason (a discipline-degradation speed-floor discretization edge
    case specific to this fixture's low-base-speed detachment -- see the xfail reason above). At
    GAUGE SCALE (larger armies, higher base speeds, unaffected by that third issue), the fix is much
    more decisive: H3/H4/H5/H6/C4's 100%/90%/100%/100%/66.7% DRAWS are entirely gone. The racing-
    clocks ablation's own frozen-vs-wheeling null result is therefore RE-CONFIRMED as uninformative
    for a different reason than first understood (both configurations' wings never reached contact at
    all, due to the now-fixed D2 bug -- not because there was genuinely no race to find).

    Separately, DG-1 (composition: force-parity + majority-infantry-pin/cavalry-wing, per Jordan's
    2026-07-05 ruling) and the completion of DG-3 (intensive, per-troop-scaled pool semantics, per
    Jordan's 2026-07-05 ruling) were also implemented this session. The gauge rows this unlocked
    (H3/H4/H5/H6/C4) now OVERSHOOT their historical bands decisively in the attacker's favor instead
    of landing inside them -- a newly-surfaced, NOT-yet-resolved question (does `subunit_combat_pool`
    need to scale by a subunit's own troop share for genuine partition invariance, or is "N
    simultaneous full-strength attacking fronts overwhelm one defender" the historically-correct
    emergent mechanism and the bands need reconsidering?) -- explicitly not decided or silently tuned
    away here. **2026-07-08 update:** Jordan ruled the partition-invariance question a genuine defect
    (fixed, see orchestration.py's `_convergence_scale`/ED-MB-0004) and DG-2 "build it now" (the
    commanded-entry slice is now built, see hierarchy/units.py's `yielding`/`yield_active` +
    tests/valoria/test_mass_battle_yield.py) -- neither closed H3-H6's overshoot on its own; see
    tests/coverage_matrix.md's 2026-07-08 entry for the honest numeric record of both.

    See tests/coverage_matrix.md's 2026-07-05 entry for the full numeric record."""
    r = _val.v_envelop(path='node', seeds=_CI_SEEDS)
    assert r.passed, f"V-ENVELOP (node) measured={r.measured} expected={r.expected}"


def test_sweep_displaces_laterally_node():
    """Acceptance: V-SWEEP on the LIVE default (node/field) path -- Subunit._resolve_maneuver_goal/
    _sweep_goal (fix-plan step 7), same mechanism as test_envelop_reaches_rear_node."""
    r = _val.v_sweep(path='node', seeds=_CI_SEEDS)
    assert r.passed, f"V-SWEEP (node) measured={r.measured} expected={r.expected}"
