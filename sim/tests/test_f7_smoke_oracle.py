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
1. The n=8 seed-42 golden win-share {Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}.
   This is now the DEFAULT campaign with ECHO_TRANSPORT ratified ON (Jordan 2026-07-08) — the
   consequence spine is live (REPINNED 2026-07-08 for the merge of origin/main's parliamentary_bridge
   auto-resolve with this branch's FA-lane mechanics + play-out echo). Still small-n (NOT balance
   signal), but note the spine already ERODED the pre-spine {Varfell 87.5} artifact (retained under
   ECHO_TRANSPORT=0 in test_echo_transport.py). Do not tune to it.
2. scenes_resolved now FIRES (the spine is live — the named-zero flipped, the success signal
   the earlier revision predicted). insurgencies_formed / npcs_generated are STILL 0 — the
   insurgency pipeline and NPE remain built-but-unreachable islands (C-EMERGE-5/6) with no
   bridge yet; when they land these MUST become non-zero (the next success signal).
3. Hafenmark elimination lockout: the one-way 0-territory lockout MECHANISM is intact (0-territory
   factions never act again; the only restoration path, parliamentary_transfer, is never called).
   Hafenmark wins 1/8 here as a TRAJECTORY artifact of the merged RNG, not a comeback. KNOWN-TRACKED
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

# REPINNED 2026-07-08: merge of ED-SC-0002/0006/0007 auto-resolve (parliamentary_bridge.py,
# origin/main) with this branch's ED-SC-0007 play-out echo addition (scene_dispatch.py) +
# ED-FA-0008/0011/0012 faction-action mechanics + ED-SC-0007-item-2 Censure fallback — all of these
# consume campaign RNG, so goldens from either session alone are stale. This is the DEFAULT campaign
# with the consequence spine ON (ECHO_TRANSPORT ratified ON, Jordan 2026-07-08): the faction-scale §10
# vote (parliamentary_bridge, every season) + the personal emergency-council contest with its play-out
# echo (ED-SC-0006/0007 #96 + this branch). Still small-n (NOT balance signal) — a guard against silent
# drift, not a target. The pre-spine byte-exact oracle is retained under ECHO_TRANSPORT=0 in
# test_echo_transport.py. (deterministic; reproduced stable across repeat runs.)
GOLDEN_WIN_SHARE = {'Crown': 37.5, 'Church': 12.5, 'Hafenmark': 12.5, 'Varfell': 37.5}
GOLDEN_WINNERS = {'Crown': 3, 'Church': 1, 'Hafenmark': 1, 'Varfell': 3}
GOLDEN_BATTLES_MEAN = 30.2
GOLDEN_SCENES_RESOLVED = 383  # was 0 pre-spine — the §10 vote (+ occasional emergency council) resolves each season
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


def test_f7_scenes_live_insurgency_and_npe_still_islands():
    """The consequence spine is LIVE: scenes_resolved now FIRES.

    REPINNED 2026-07-08 (merge of both sessions): scenes_resolved is no longer 0 on seed-42. The
    faction-scale §10 Parliamentary vote (parliamentary_bridge, origin/main) resolves EVERY season,
    and the personal-scale Emergency Council contest resolves when the FA-lane action-mix/Muster/
    conquest-fork/Parliamentary changes (this branch) shift seed-42 RNG across Stability Crisis
    (383 scenes across the n=8 batch). Pinned here as the new golden — NOT re-asserted to 0.
    insurgencies_formed and npcs_generated remain built-but-unreachable islands (C-EMERGE-4/5),
    still guarded at 0; when the insurgency pipeline / NPE seeding land, those pins trip next and
    get updated the same way.
    """
    campaigns = _campaigns42()
    scenes = sum(r.scenes_resolved for r in campaigns)
    insurgencies = sum(r.insurgencies_formed for r in campaigns)
    npcs = sum(r.npcs_generated for r in campaigns)
    assert scenes == GOLDEN_SCENES_RESOLVED, f"scenes_resolved drifted ({scenes} vs {GOLDEN_SCENES_RESOLVED}) — the spine output moved; investigate before regenerating"
    assert insurgencies == 0, f"insurgencies_formed is no longer 0 ({insurgencies}) — the insurgency pipeline may be reachable; update the golden"
    assert npcs == 0, f"npcs_generated is no longer 0 ({npcs}) — generate_npc may have live call sites; update the golden"


def test_f7_hafenmark_elimination_lockout():
    """Hafenmark wins 1/8 on seed-42 (REPINNED 2026-07-08 for the two-session merge).

    The one-way 0-territory lockout MECHANISM is intact — no comeback path was added (ED-FA-0005
    remains open; parliamentary_transfer is still never called). Hafenmark's win here is a
    TRAJECTORY shift, not a comeback: the merged behaviour (the per-season §10 vote from
    parliamentary_bridge + the FA-lane action-mix/Muster/conquest-fork/Parliamentary fallback +
    the play-out echo) changed which factions survive to the 50-season horizon on these seeds, so
    Hafenmark simply avoids elimination in 1 of the 8 and wins on territory. Pinned as the new
    golden; a move here again means the merged RNG shifted — investigate before regenerating."""
    campaigns = _campaigns42()
    hafenmark_wins = sum(1 for r in campaigns if r.winner == 'Hafenmark')
    assert hafenmark_wins == 1, f"Hafenmark won {hafenmark_wins} != 1 — merged trajectory moved (or an ED-FA-0005 comeback path landed); investigate before regenerating"


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
