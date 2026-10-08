"""PC-03 (ED-PC-0058 critique): the three readers of the per-defender Ob that ED-PC-0058 left behind.

`core.resolve` bands a roll at `core.ob_from_defender(defender)` (History / 2) on the owner ladder
(`engine.dice_engine.dice_engine.degree_from_net`, migrated at PC-02). Three things downstream of that
change kept reading the retired fixed `core.DECISIVE_OB = 3`:

 1. `workbench/probabilities.py` banded every displayed distribution at `DECISIVE_OB` on the pre-ruling
    ladder. Its two trace inputs (the wrapper's 'roll' / 'stophit' events) carried no `ob`, so it could
    not do otherwise. Falsifier: the workbench's band probabilities for a defender whose History is NOT
    the default, against `core.resolve`'s observed band frequencies over N seeds. On the pre-PC-03 tree
    they differ far beyond sampling noise; after it they agree.
 2. `core.strike`'s overwhelming-hit quality measured its severity tail `z` from `net - 2*DECISIVE_OB`,
    i.e. from a fixed net of 6, while the band it qualifies starts at the owner's bar for THIS defender's
    Ob. So q sat clamped at the tail floor for every overwhelming net between the bar and 6 (26% of
    overwhelming hits over 1,200 fights, measured at PC-03), and the tail's start moved with nothing the
    ladder reads. The workplan's "likely fix" `2*ob` is the PRE-ruling ladder's bar (`net >= 2*Ob`),
    which the 2026-08-14 ruling RULED OUT (`degree_from_net`'s docstring); it would start the tail
    below the bar for ob < 3 and clamp again above it for ob > 3. The fix reads the bar off the owner.
 3. Observation only (no physics change): does History enter the net sigma exactly once? It does not —
    see `test_history_enters_the_roll_through_exactly_one_channel`, xfailed with the measured numbers.
"""
import math
import os
import random
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, 'workbench'))

import combatant as C          # noqa: E402
import combat_systems as S     # noqa: E402
import core                    # noqa: E402
import tradition as TR         # noqa: E402
import wrapper                 # noqa: E402
from config import CFG         # noqa: E402
import probabilities as P      # noqa: E402
from engine.dice_engine import dice_engine as DE          # noqa: E402
from engine.dice_engine import sigma_leverage as SL       # noqa: E402

BANDS = ('fail', 'partial', 'success', 'overwhelming')
DEFAULT_HISTORY = C.Combatant('probe').history


# ── finding 1: the workbench's distributions against the resolver's frequencies ──────────────────

def _observed(pool, net_sigma, ob, n):
    counts = dict.fromkeys(BANDS, 0)
    for seed in range(n):
        deg, _ = core.resolve(pool, net_sigma, random.Random(seed), ob)
        counts[deg] += 1
    return {k: v / n for k, v in counts.items()}


def test_workbench_band_probabilities_match_resolve_for_a_non_default_history_defender():
    """The workbench's 'roll' node distribution (fed the event the wrapper emits) against `core.resolve`
    over N seeds, for a defender at History 5 (Ob 2.5, not the default's 1.5). Tolerance: 5 binomial
    standard errors per band, plus the 4-dp rounding the workbench applies."""
    defender = C.Combatant('D', history=5)
    assert defender.history != DEFAULT_HISTORY
    ob = core.ob_from_defender(defender)
    pool = core.resolution_pool(DEFAULT_HISTORY)
    n = 20_000
    checked, misses = 0, []
    for net_sigma in (-0.5, 0.0, 0.6):
        ev = {'kind': 'roll', 'pool': pool, 'net_sigma': net_sigma, 'ob': ob, 'degree': 'success'}
        want = P.node_distribution(ev)
        got = _observed(pool, net_sigma, ob, n)
        assert set(want) == set(BANDS)
        for band in BANDS:
            p = got[band]
            tol = 5.0 * math.sqrt(max(p * (1 - p), 1.0 / n) / n) + 5e-4
            checked += 1
            if abs(want[band] - p) > tol:
                misses.append(f'net_sigma={net_sigma} {band}: workbench {want[band]:.4f} vs resolve {p:.4f} (tol {tol:.4f})')
    assert checked == 12, checked
    assert not misses, 'workbench bands diverge from core.resolve:\n  ' + '\n  '.join(misses)


def test_trace_events_carry_the_ob_their_roll_was_banded_at():
    """Every 'roll' and 'stophit' event names the Ob the roll was banded at, and it is the STRUCK party's
    `ob_from_defender` — the input finding 1's distribution needs and could not get before PC-03."""
    rolls = stophits = 0
    # spear vs dagger supplies the stop-hits (it rarely closes); longsword vs arming the exchanges
    for weapon_a, weapon_b in (('spear', 'dagger'), ('longsword', 'arming')):
        for seed in range(20):
            events = []
            A = C.Combatant('A', weapon=weapon_a, history=5)
            B = C.Combatant('B', weapon=weapon_b, history=2)
            wrapper._TRACE = events.append
            try:
                wrapper.fight(A, B, rng=random.Random(seed))
            finally:
                wrapper._TRACE = None
            r, s = _check_events(events, {'A': A, 'B': B})
            rolls += r
            stophits += s
    assert rolls >= 50 and stophits >= 1, (rolls, stophits)


def _check_events(events, who):
    rolls = stophits = 0
    for ev in events:
        if ev['kind'] == 'roll':
            struck = who['B' if ev['aggressor'] == 'A' else 'A']
            rolls += 1
        elif ev['kind'] == 'stophit':
            struck = who[ev['shorter']]
            stophits += 1
        else:
            continue
        assert 'ob' in ev, f"{ev['kind']} event carries no ob: {ev}"
        assert ev['ob'] == core.ob_from_defender(struck), ev
    return rolls, stophits


# ── finding 2: the overwhelming-hit severity tail starts at the owner's bar ───────────────────────

def _owner_overwhelming_bar(ob):
    """The smallest float the OWNER ladder reads as Overwhelming at `ob` — a test-local bisection, kept
    independent of core's own helper so it can check that helper rather than restate it."""
    lo, hi = ob - 64.0, ob + 64.0
    while True:
        mid = (lo + hi) / 2
        if mid <= lo or mid >= hi:
            return hi
        if DE.degree_from_net(mid, ob) is DE.Degree.OVERWHELMING:
            hi = mid
        else:
            lo = mid


def _quality_at(net, pool, defender, monkeypatch):
    seen = {}
    real = core.damage

    def spy(*a, **kw):
        seen['q'] = kw.get('q')
        return real(*a, **kw)
    monkeypatch.setattr(core, 'damage', spy)
    core.strike(C.Combatant('A', weapon='longsword'), defender, 'overwhelming', CFG, net=net, pool=pool)
    monkeypatch.setattr(core, 'damage', real)
    return seen['q']


@pytest.mark.parametrize('history', [2, 3, 5, 6, 8])
def test_overwhelming_quality_tail_is_measured_from_the_owner_bar(history, monkeypatch):
    """At the bar, q is the tail floor (`QUAL['overwhelming']`); past it, z is exactly the distance past the
    bar in sigma_n units. On the pre-PC-03 tree the tail started at net 6 for every defender, so at every
    History but 6 the first assertion past the bar fails (or, for History 8, the floor is not at the bar)."""
    defender = C.Combatant('D', history=history)
    ob = core.ob_from_defender(defender)
    pool = core.resolution_pool(DEFAULT_HISTORY)
    bar = _owner_overwhelming_bar(ob)
    assert DE.degree_from_net(bar, ob) is DE.Degree.OVERWHELMING
    assert DE.degree_from_net(math.nextafter(bar, -math.inf), ob) is DE.Degree.SUCCESS
    assert _quality_at(bar, pool, defender, monkeypatch) == core.QUAL['overwhelming']
    for delta in (0.25, 1.0, 2.5):
        z = ((bar + delta) - bar) / SL.sigma_n(pool)
        want = 1.5 + (core.OW_MAX - 1.5) * math.tanh(z / core.OW_Z)
        assert _quality_at(bar + delta, pool, defender, monkeypatch) == want, (history, delta)


def test_band_floor_reads_the_owner_edges():
    """`core.band_floor` is the one place combat reads a band EDGE (the workbench's thresholds and strike's
    tail start). Each edge is the exact float where the owner ladder changes band."""
    checked = 0
    for ob in (0.5, 1.0, 1.5, 2.5, 3.0, 4.25):
        for band in BANDS[1:]:
            edge = core.band_floor(band, ob)
            below = core.degree(math.nextafter(edge, -math.inf), ob)
            assert BANDS.index(core.degree(edge, ob)) >= BANDS.index(band) > BANDS.index(below), (ob, band, edge)
            checked += 1
        assert core.band_floor('overwhelming', ob) == _owner_overwhelming_bar(ob)
    assert checked == 18


# ── finding 3: observation, not a ruling ──────────────────────────────────────────────────────────

def _defender_side_sigma(aggressor, defender, mode):
    """The net-sigma terms of one exchange that read the defender's History, assembled through the same
    `combat_systems` owners the wrapper sequences (`wrapper.engagement`, the net-sigma assembly): the
    initiative emphasis (into attack_sigma) and the defence sigma for `mode` (mode_sigma -> defence_sigma).
    Fatigue 0, read won, commit 3. `combat_systems.py` reads `.history` at four sites (reading, mode_sigma's
    `tech`, init_emphasis_sigma, the bind and counter rolls); the last two are other rolls."""
    init = S.init_emphasis_sigma(aggressor, defender, CFG, TR)
    msig = S.mode_sigma(mode, aggressor, defender, 3.0, True, 0.0, CFG)
    dsig = S.defence_sigma(defender, msig, 0.0, 0.0, CFG)
    return init - dsig


@pytest.mark.xfail(strict=True, reason=(
    'PC-03 finding 3, OBSERVED NOT RULED: the defender\'s History reaches the main roll through TWO channels — '
    'the Ob (`core.ob_from_defender` = History/2) AND the net sigma (`mode_sigma`\'s `tech` term for parry/wind, '
    '`reading()`\'s READ_HISTORY_K term, `init_emphasis_sigma`\'s INIT_HISTORY_K term). Whether that is a '
    'double-count is a design question; no physics was changed. strict=True: if History is ever routed '
    'through one channel this XPASSes and fails, so the record cannot go stale.'))
def test_history_enters_the_roll_through_exactly_one_channel():
    aggressor = C.Combatant('A')
    lo, hi = C.Combatant('D3', history=3), C.Combatant('D5', history=5)
    for c in (aggressor, lo, hi):
        wrapper._init_live(c, CFG)
    channels = {'ob': core.ob_from_defender(hi) - core.ob_from_defender(lo)}
    for mode in ('parry', 'dodge', 'wind'):
        channels[f'net_sigma[{mode}]'] = (_defender_side_sigma(aggressor, hi, mode)
                                          - _defender_side_sigma(aggressor, lo, mode))
    assert len(channels) == 4
    # each mode is a separate exchange; the claim is per exchange: Ob plus that mode's sigma
    for mode in ('parry', 'dodge', 'wind'):
        live = [k for k in ('ob', f'net_sigma[{mode}]') if abs(channels[k]) > 1e-12]
        assert len(live) == 1, f'History +2 moves {live}: {channels}'
