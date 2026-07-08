"""
F7 smoke oracle — the "born guarded" campaign regression (ED-IN-0021 / OPT-3).

WHY THIS EXISTS (unaddressed-areas audit U-4 / C-EMERGE)
-------------------------------------------------------
The "~87% win-share degeneracy" that five docs cited as a balance fact was a SMALL-N
ARTIFACT: it traces to a single un-guarded `run_batch(8, base_seed=42)` that propagated
unchallenged. The lesson the audit drew: *no balance claim without an oracle + n >= 100.*
This is the second pinned golden (`base_seed=42`), complementing the seed-0 golden in
`test_mc_v18_regression.py`. It exists to guard the CURRENT (pre-transport) state so that
when the Key/echo transport layer and the LPS-1 oracle land, the change is LOUD here rather
than silent.

WHAT IT PINS — and why each assertion is a *guard*, not a target
----------------------------------------------------------------
1. The n=8 seed-42 golden win-share {Crown 12.5, Church 0, Hafenmark 0, Varfell 87.5}.
   This IS the historical artifact, pinned deliberately and labelled: it is NOT balance
   signal (n=8 is far too small; the audit's n=100 read is 56/36/7/1). Do not tune to it.
2. Named ZERO-assertions: scenes_resolved / insurgencies_formed / npcs_generated are all 0
   across the whole batch, because the contest kernel, insurgency pipeline, and NPE are
   built-but-unreachable islands (C-REACH / C-EMERGE-4/5/6). These MUST start firing when
   the derivation bridge + keying waves land — this test tripping is then the SUCCESS signal
   (update the golden and say so in the commit).
3. Hafenmark elimination lockout: Hafenmark never wins (0-territory factions never act
   again; the only restoration path, parliamentary_transfer, is never called). KNOWN-TRACKED
   via ED-FA-0005 (comeback path ruled to be authored). Trips when a comeback path lands.
4. VICTORY_THRESHOLD dead-param regression: the param moves NO outcome (C-EMERGE-8 / C-FA-9).
   Trips when the victory threshold is actually wired to a live gate.
5. Wall-time ceiling: keeps the reference fast and non-degrading.

REGENERATING THE GOLDEN (only when a change is *intended* to move output)
-------------------------------------------------------------------------
    python -c "from sim.mc_v18 import run_batch; print(run_batch(n=8, base_seed=42).win_share)"
A surprise failure means simulation output moved — investigate BEFORE regenerating. If the
move is the transport layer / oracle finally reaching a subsystem, that is the intended win;
update the pins and note it.
"""
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from sim.mc_v18 import run_campaign, run_batch  # noqa: E402

_SEED = 42
_N = 8
_FACTIONS = ['Crown', 'Church', 'Hafenmark', 'Varfell']

# Pinned 2026-07-07 (deterministic; reproduced stable across repeat runs).
GOLDEN_WIN_SHARE = {'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 87.5}
GOLDEN_WINNERS = {'Varfell': 7, 'Crown': 1}
GOLDEN_BATTLES_MEAN = 33.0
WALL_TIME_CEILING_S = 90.0  # n=8 runs ~16s; generous headroom for CI variance

_CACHE = {}


def _campaigns42():
    """Run the 8 seed-42 campaigns once; cache for reuse across assertions."""
    if 'c' not in _CACHE:
        t0 = time.time()
        _CACHE['c'] = [run_campaign(seed=_SEED + i) for i in range(_N)]
        _CACHE['wall'] = time.time() - t0
    return _CACHE['c']


def _win_share(campaigns):
    wins = {}
    for r in campaigns:
        if r.winner:
            wins[r.winner] = wins.get(r.winner, 0) + 1
    total = sum(wins.values()) or 1
    return {fn: round(wins.get(fn, 0) / total * 100, 1) for fn in _FACTIONS}, wins


def test_f7_determinism():
    """Same seed -> identical output. A non-deterministic reference cannot be an oracle."""
    a = run_batch(n=2, base_seed=_SEED)
    b = run_batch(n=2, base_seed=_SEED)
    assert a.win_share == b.win_share
    assert a.all_winners == b.all_winners
    assert a.battles_mean == b.battles_mean


def test_f7_golden_win_share():
    """The n=8 seed-42 artifact, pinned. NOT balance signal — a guard against silent drift."""
    share, winners = _win_share(_campaigns42())
    assert share == GOLDEN_WIN_SHARE, f"win_share drifted: {share}"
    assert winners == GOLDEN_WINNERS, f"winners drifted: {winners}"
    b = run_batch(n=_N, base_seed=_SEED)
    assert b.battles_mean == GOLDEN_BATTLES_MEAN, f"battles_mean drifted: {b.battles_mean}"


def test_f7_named_zero_assertions_islands_unreachable():
    """scenes_resolved / insurgencies_formed / npcs_generated are 0 — the islands never fire.

    When the derivation bridge (SC) + keying waves + NPE seeding land, these MUST become
    non-zero: this test tripping is the SUCCESS signal, not a regression. Update the pins then.
    """
    campaigns = _campaigns42()
    scenes = sum(r.scenes_resolved for r in campaigns)
    insurgencies = sum(r.insurgencies_formed for r in campaigns)
    npcs = sum(r.npcs_generated for r in campaigns)
    assert scenes == 0, f"scenes_resolved is no longer 0 ({scenes}) — the contest/scene bridge may have landed; update the golden"
    assert insurgencies == 0, f"insurgencies_formed is no longer 0 ({insurgencies}) — the insurgency pipeline may be reachable; update the golden"
    assert npcs == 0, f"npcs_generated is no longer 0 ({npcs}) — generate_npc may have live call sites; update the golden"


def test_f7_hafenmark_elimination_lockout():
    """Hafenmark never wins (one-way 0-territory lockout). KNOWN-TRACKED via ED-FA-0005."""
    campaigns = _campaigns42()
    hafenmark_wins = sum(1 for r in campaigns if r.winner == 'Hafenmark')
    assert hafenmark_wins == 0, f"Hafenmark won {hafenmark_wins} — a comeback path may have landed (ED-FA-0005); update the golden"


def test_f7_victory_threshold_is_a_dead_param():
    """VICTORY_THRESHOLD moves no outcome (C-EMERGE-8 / C-FA-9). Trips when wired to a live gate."""
    base = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 11}).win_share
    hi = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 999}).win_share
    lo = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 1}).win_share
    assert base == hi == lo, (
        f"VICTORY_THRESHOLD now moves outcomes (11->{base}, 999->{hi}, 1->{lo}) — "
        "the dead param may have been wired to a live victory gate; update this test"
    )


def test_f7_wall_time_ceiling():
    """The reference stays fast; guards against an accidental complexity blow-up."""
    _campaigns42()  # populates _CACHE['wall']
    assert _CACHE['wall'] < WALL_TIME_CEILING_S, (
        f"the {_N}-campaign seed-42 batch took {_CACHE['wall']:.1f}s "
        f"(> {WALL_TIME_CEILING_S}s ceiling)"
    )
