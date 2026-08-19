"""Property tests against engine/autoload/dice_engine.py — an INDIVIDUAL engine, ahead of the
full season loop (return_to_game_queue.yaml S2 action 3; tools/m1_acceptance.py's
`row_invariant_violations` names this exact move: "properties can be authored against
individual engines TODAY, ahead of the loop").

WHAT THIS IS AND IS NOT. This is a BEGINNING, not the M1 acceptance row itself. Row 5
("N seeds, zero invariant violations") measures invariants over a full season KeyLog; this file
measures two much narrower, fully-specified invariants of the dice primitive alone, seeded and
swept across many trials. It does not touch engine.mc_v18 and does not change
row_invariant_violations()'s reported `state` (still `blocked`, correctly).

WHY NO HYPOTHESIS. The `hypothesis` package is not a dependency anywhere in this tree (grep
tests/valoria for it: zero hits before this file) and CI's `unit-tests` job installs only
`pyyaml pytest numpy pytest-xdist` (.github/workflows/valoria-ci.yml). Adding a new third-party
import to a blocking-gate test file without also adding it to that install step would collect-
error the whole `unit-tests` job -- out of scope for S2 (CLAUDE.md's "do not widen the step").
So these are hand-rolled seeded sweeps: the property-testing METHODOLOGY (many pseudo-random
inputs, one invariant, one seed for reproducibility) without the extra dependency.

Each property is checked against an INDEPENDENTLY DERIVED oracle (the documented formula/rule,
re-typed from the docstring below it, not a call into the function's own internals) -- an
assertion that merely re-ran the code under test would not be able to observe the failure it
excludes (CLAUDE.md §0.1 point 2).
"""
import os
import random
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, REPO_ROOT)

from engine.autoload import dice_engine as de  # noqa: E402

N_TRIALS = 500
SWEEP_SEED = 20260819  # same fixed-seed convention as tools/m1_acceptance.py's M1_PROBE_SEED


# ── Property 1: roll_pool's Pool Minimum + Die Rule bounds (dice_engine.py:80-84, PP-246) ───────
#
#   "Pool minimum 1D" (params/core.md §Pool Minimum) -> effective_pool = max(1, pool_size).
#   "1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes" (Die Rule, PP-246) -> each die
#   contributes a value in {-1, 0, 1, 2}, so net is bounded by
#   [-1 * effective_pool, 2 * effective_pool] regardless of the actual rolls.

def test_roll_pool_respects_pool_minimum_and_die_rule_bounds_property():
    rng_seeder = random.Random(SWEEP_SEED)
    checked = 0
    for _ in range(N_TRIALS):
        pool_size = rng_seeder.randint(-10, 200)  # includes <= 0 to exercise the minimum clamp
        tn = rng_seeder.choice([6, 7, 8])
        trial_rng = random.Random(rng_seeder.randint(0, 2**32 - 1))

        result = de.roll_pool(pool_size, tn=tn, rng=trial_rng)

        expected_effective = max(1, pool_size)
        assert result.pool_size == expected_effective, (
            f'pool_size={pool_size}: Pool Minimum violated, got {result.pool_size}'
        )
        assert len(result.rolls) == expected_effective, (
            f'pool_size={pool_size}: rolled {len(result.rolls)} dice, expected {expected_effective}'
        )
        assert all(1 <= face <= 10 for face in result.rolls), (
            f'pool_size={pool_size}: a d10 face outside [1,10]: {result.rolls}'
        )
        lo, hi = -1 * expected_effective, 2 * expected_effective
        assert lo <= result.net <= hi, (
            f'pool_size={pool_size}: net={result.net} outside Die Rule bounds [{lo}, {hi}] '
            f'for {expected_effective} dice (rolls={result.rolls})'
        )
        checked += 1
    # §0.1 point 2: a loop that asserts conditionally must assert that it asserted.
    assert checked == N_TRIALS


def test_roll_pool_is_deterministic_given_an_identically_seeded_rng():
    """A narrower, individual-engine echo of row_determinism's shape (same seed -> same
    result) -- exercised here at the dice-pool level, not the season level."""
    for trial_seed in (1, 2, 3, 424242, SWEEP_SEED):
        r1 = de.roll_pool(12, tn=7, rng=random.Random(trial_seed))
        r2 = de.roll_pool(12, tn=7, rng=random.Random(trial_seed))
        assert r1.rolls == r2.rolls
        assert r1.net == r2.net


# ── Property 2: degree_from_net's margin ladder (dice_engine.py:104-129, Jordan ruling 2026-08-14)
#
#   margin = net - ob
#   margin >= 3        -> OVERWHELMING
#   margin >= 1         -> SUCCESS
#   0 <= margin < 1     -> PARTIAL
#   margin < 0          -> FAILURE
#
# Independently re-derived here (not calling degree_from_net to compute its own oracle) so a
# regression in the ladder's boundary logic is something this test CAN observe, per §0.1 point 2.

def _expected_degree(net, ob):
    margin = net - ob
    if margin >= 3:
        return de.Degree.OVERWHELMING
    if margin >= 1:
        return de.Degree.SUCCESS
    if margin >= 0:
        return de.Degree.PARTIAL
    return de.Degree.FAILURE


def test_degree_from_net_matches_the_documented_margin_formula_property():
    rng = random.Random(SWEEP_SEED)
    checked = 0
    for _ in range(N_TRIALS):
        # Both operands may be fractional (docstring: "Both operands may be fractional").
        # Range chosen to land on/near every band boundary (margin in roughly [-6, 9]) rather
        # than drift toward the interior only, since boundaries are exactly where a ladder bug
        # hides (§0.1 point 2's "an assertion must be able to observe the failure it excludes").
        net = round(rng.uniform(-10, 15), 3)
        ob = round(rng.uniform(-5, 12), 3)

        expected = _expected_degree(net, ob)
        actual = de.degree_from_net(net, ob)
        assert actual == expected, (
            f'net={net}, ob={ob}, margin={net - ob}: expected {expected}, got {actual}'
        )
        checked += 1
    assert checked == N_TRIALS


def test_degree_from_net_boundary_values_exactly():
    """Example-based edges at the exact band transitions -- the seeded sweep above lands near
    these only probabilistically; this pins them exactly."""
    assert de.degree_from_net(net=3, ob=0) == de.Degree.OVERWHELMING   # margin == 3
    assert de.degree_from_net(net=2.999, ob=0) == de.Degree.SUCCESS    # just under 3
    assert de.degree_from_net(net=1, ob=0) == de.Degree.SUCCESS        # margin == 1
    assert de.degree_from_net(net=0.999, ob=0) == de.Degree.PARTIAL    # just under 1
    assert de.degree_from_net(net=0, ob=0) == de.Degree.PARTIAL        # margin == 0
    assert de.degree_from_net(net=-0.001, ob=0) == de.Degree.FAILURE   # just under 0


def test_degree_from_net_is_total_over_the_sweep_and_never_raises():
    """A ladder with a gap would raise (falling through an if/elif chain to an implicit None)
    or return something outside the four-member enum -- neither is caught by the formula-match
    test above if the gap happens to coincide with a value the sweep never hits, so this checks
    totality directly: every result is one of the four Degree members, never None."""
    rng = random.Random(SWEEP_SEED + 1)
    for _ in range(N_TRIALS):
        net = rng.uniform(-20, 20)
        ob = rng.uniform(-20, 20)
        result = de.degree_from_net(net, ob)
        assert result in (de.Degree.OVERWHELMING, de.Degree.SUCCESS,
                          de.Degree.PARTIAL, de.Degree.FAILURE), (net, ob, result)
