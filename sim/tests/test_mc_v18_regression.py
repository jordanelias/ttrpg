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

REGENERATED 2026-07-08 (ED-SC-0006, party-derivation bridge): the seed-1 campaign now
crosses the Stability Crisis trigger and its Emergency Council contest actually resolves
(previously every contest scene deferred — the kernel was reachable-in-code but
dead-in-campaign; see scene_dispatch._emergency_council_parties), consuming RNG draws
that used to never fire and moving this golden's win_share/all_winners/battles_mean.
This is the intended flip, not a regression — see test_mc_v18_resolves_at_least_one_contest
below.

REGENERATED 2026-07-08 (ED-FA-0008/0011/0012 — FA-lane mechanics into faction_action.py):
state-conditioned action mix (ED-FA-0011, retiring the fixed 30/35/20/15 M7_ASSUMPTION_SIX
vector), Muster as a fiscal-military purchase (ED-FA-0008: W-1 up front, pool = Mil + floor(W/2)),
the Terms-vs-Storm conquest fork (ED-FA-0012 a/b), and the Parliamentary-Censure fallback wired
into the faction-unique slot. faction_take_action is reachable from EVERY live campaign, so these
shift RNG consumption and moved this golden's win_share/all_winners/battles_mean — the expected,
intended move each pin below anticipates (a surprise here means output moved for a DIFFERENT
reason; investigate before regenerating).
"""
import os
import sys

# Make the repo root importable so `import sim.*` resolves when pytest runs from anywhere.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from sim.mc_v18 import run_batch, run_campaign  # noqa: E402

# Golden batch, regenerated 2026-07-08 (ED-FA-0008/0011/0012 — see module docstring; deterministic,
# verified stable across repeat runs). Prior ED-SC-0006 values were {Crown 50, Varfell 50} /
# {Crown 1, Varfell 1} / 30.0; the FA-lane action-mix + Muster + conquest-fork + Parliamentary
# fallback shifted campaign RNG and moved them here.
_SEED = 0
_N = 2
GOLDEN_WIN_SHARE = {'Crown': 0.0, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 100.0}
GOLDEN_WINNERS = {'Varfell': 2}
GOLDEN_BATTLES_MEAN = 35.0


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


def test_mc_v18_resolves_at_least_one_contest():
    """ED-SC-0006 (party-derivation bridge): across the golden batch, at least one Emergency
    Council contest must actually resolve — previously ALWAYS 0 (fable5_social_contest_audit_v1.md
    N-1: the promoted kernel was reachable in code but dead-in-campaign). This is what
    test_f7_named_zero_assertions_islands_unreachable (test_f7_smoke_oracle.py) predicted would
    trip; it happens to still read 0 for that particular seed-42/n=8 sample (Stability Crisis is
    seed-dependent and rare), so this seed-0 golden is the one that demonstrates the bridge live."""
    total = sum(run_campaign(seed=_SEED + i).scenes_resolved for i in range(_N))
    assert total > 0, f"no contest resolved across the seed-{_SEED} golden batch (got {total}) — the party-derivation bridge may have regressed"


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
