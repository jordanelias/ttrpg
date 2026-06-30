"""
Deterministic seeded regression oracle for the Valoria simulation reference.

WHY THIS EXISTS (ED-1053 / ecosystem review §3.2)
--------------------------------------------------
`sim/` is the 1:1 Python reference the GDScript Godot port is validated against, yet
it had ZERO tests and was never run in CI — a seeded campaign batch could silently
go degenerate (one faction ~87%, others 0%) and nothing would flag it, leaving the
port with no regression oracle. This pins a small, fast, fully deterministic batch so
that (a) the campaign engine stays runnable and reproducible, and (b) any future change
that perturbs balance output trips a visible, diff-able failure here.

WHAT IT PINS
------------
`mc_v18.run_batch(n=2, base_seed=0)` — two 50-season campaigns on fixed seeds [0, 1].
Runtime ≈ 5 s. The happy path does not touch any of sim's NotImplementedError stubs.

REGENERATING THE GOLDEN (only when a change is *intended* to move balance)
--------------------------------------------------------------------------
    python -c "from sim.mc_v18 import run_batch; r=run_batch(n=2, base_seed=0); \
print(r.n, r.win_share, r.all_winners, r.battles_mean)"
Then update GOLDEN below and say so in the commit. A surprise failure here means a
change altered simulation output — investigate before regenerating.
"""
import os
import sys

# Make the repo root importable so `import sim.*` resolves when pytest runs from anywhere.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from sim.mc_v18 import run_batch  # noqa: E402

# Golden batch, regenerated 2026-06-30 (deterministic; verified stable across repeat runs).
_SEED = 0
_N = 2
GOLDEN_WIN_SHARE = {'Crown': 50.0, 'Church': 50.0, 'Hafenmark': 0.0, 'Varfell': 0.0}
GOLDEN_WINNERS = {'Crown': 1, 'Church': 1}
GOLDEN_BATTLES_MEAN = 38.0


def test_mc_v18_batch_is_deterministic():
    """Same seed -> identical output. A non-deterministic reference cannot be a port oracle."""
    a = run_batch(n=_N, base_seed=_SEED)
    b = run_batch(n=_N, base_seed=_SEED)
    assert a.n == b.n
    assert a.win_share == b.win_share
    assert a.all_winners == b.all_winners
    assert a.battles_mean == b.battles_mean


def test_mc_v18_batch_matches_golden():
    """Pinned golden regression — a diff here means simulation output moved."""
    r = run_batch(n=_N, base_seed=_SEED)
    assert r.n == _N
    assert r.win_share == GOLDEN_WIN_SHARE, f"win_share drifted: {r.win_share}"
    assert r.all_winners == GOLDEN_WINNERS, f"all_winners drifted: {r.all_winners}"
    assert r.battles_mean == GOLDEN_BATTLES_MEAN, f"battles_mean drifted: {r.battles_mean}"


def test_mc_v18_win_share_is_well_formed():
    """Bounded smoke invariant: shares are a percentage distribution over the factions."""
    r = run_batch(n=_N, base_seed=_SEED)
    assert set(r.win_share) == set(GOLDEN_WIN_SHARE)
    assert all(0.0 <= v <= 100.0 for v in r.win_share.values())
    assert abs(sum(r.win_share.values()) - 100.0) < 1e-6
    assert r.battles_mean >= 0.0


if __name__ == '__main__':
    # Runnable without pytest.
    fns = [v for k, v in sorted(globals().items()) if k.startswith('test_') and callable(v)]
    p = f = 0
    for fn in fns:
        try:
            fn(); p += 1
        except AssertionError as e:
            f += 1; print(f"FAIL {fn.__name__}: {e}")
    print(f"{p} passed, {f} failed")
    sys.exit(1 if f else 0)
