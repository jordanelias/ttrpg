"""Branch-probability math for the Combat Workbench (WS-6) narrator + branch explorer.

Given the INPUTS the engine emits at each decision node (wrapper._emit events), reconstruct the
probability of each ALTERNATE branch — the "what else could have happened, and how likely" view that
turns an n=1 trace into something honest. The engine emits facts (the inputs a node consumed and the
sampled outcome); this module turns those inputs into the local distribution.

Single source of truth: every canonical value (the roll's mean and spread, the soft-cap, sigma_n, the
band edges) is IMPORTED from the dice engine (`engine.dice_engine.sigma_leverage`, which delegates to
`dice_engine`), never re-declared here — so a tuning change to the engine flows through automatically
and the sim-fabrication discipline holds by import. The frozen v32 harness is no longer read.
Degree banding is the owner ladder's: the Ob is the one the roll was banded at (the 'roll'/'stophit'
trace events carry it, `core.ob_from_defender` of the struck party), and the band odds are
`sigma_leverage.band_odds`, the Normal closed form of the one sampler `core.resolve` draws
(`roll_net_continuous`). PC-03 replaced a copy of the pre-ruling ladder at the retired fixed
`DECISIVE_OB`, which went stale silently at ED-PC-0058; its falsifier is
tests/valoria/test_combat_ob_from_defender_consumers.py (workbench bands vs `core.resolve` frequencies)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `engine.dice_engine` and `modules.combat` are packages
from engine.dice_engine import sigma_leverage as SL  # the dice owner: band_odds, soft_cap, sigma_n (numpy-free)


def degree_distribution(pool, net_sigma, ob):
    """P(fail / partial / success / overwhelming) for one resolution roll under the continuous engine.

    core.resolve draws net = roll_net(pool) + soft_cap(net_sigma) * sigma_n(pool), then bands it at `ob`.
    That boost is the mu-shift; the roll's mean and spread and the band edges are
    `SL.band_odds(pool, ob, boost)`'s, the closed form of the same sampler and ladder.
    `ob` is REQUIRED — the Ob the roll was banded at (the trace event's `ob`), never a default, for the
    same reason core.resolve requires it."""
    boost = SL.soft_cap(net_sigma) * SL.sigma_n(pool)      # core.resolve's own boost expression
    p_fail, p_part, p_succ, p_over = SL.band_odds(pool, ob, boost)   # owner order: DEGREE_ORDINAL
    d = {'fail': p_fail, 'partial': p_part, 'success': p_succ, 'overwhelming': p_over}
    return {k: max(0.0, round(v, 4)) for k, v in d.items()}


def outcome_distribution(degree, mode, cfg, exposure=0.0):
    """DEPTH-2: given a roll degree and the defender's mode, the {hit, bind, riposte, miss} distribution it leads
    to — computed from the engine's outcome-mapping rules (wrapper.py:173-198) + cfg. This is the "what does each
    roll outcome lead to" branch the explorer expands under the roll node (overcommit_exposure≈0 by default)."""
    neut = {'parry': cfg['NEUTRALIZE_PARRY'], 'dodge': cfg['NEUTRALIZE_DODGE'], 'wind': cfg['NEUTRALIZE_WIND']}[mode]
    out = {'hit': 0.0, 'bind': 0.0, 'riposte': 0.0, 'miss': 0.0}
    if degree == 'fail':
        rip = min(cfg['RIPOSTE_CAP'], cfg['RIPOSTE_ON_FAIL'] + exposure)
        out['riposte'], out['miss'] = rip, 1 - rip
    elif degree == 'partial':
        if mode == 'dodge':
            g = cfg['PARTIAL_DODGE_GRAZE']; out['hit'], out['miss'] = g, 1 - g
        elif mode == 'parry':
            g = cfg['PARTIAL_PARRY_GRAZE']; out['hit'], out['miss'] = g, 1 - g
        else:
            out['bind'] = 1.0
    elif degree == 'success':
        rip_p = min(cfg['RIPOSTE_CAP'], cfg['RIPOSTE_ON_NEUTRALIZE'] + exposure)
        rem = 1.0
        if mode == 'wind':
            out['bind'] = cfg['WIND_BIND_P']; rem = 1 - cfg['WIND_BIND_P']
        out['riposte'] += rem * neut * rip_p
        out['miss'] += rem * neut * (1 - rip_p)
        out['hit'] += rem * (1 - neut)
    else:  # overwhelming
        miss = max(0.0, neut - cfg['NEUTRALIZE_OVERWHELM_DROP'])
        out['miss'], out['hit'] = miss, 1 - miss
    return {k: round(v, 4) for k, v in out.items()}


def _beta_pdf(x, a, b):
    from math import gamma
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return x ** (a - 1.0) * (1.0 - x) ** (b - 1.0) / (gamma(a) * gamma(b) / gamma(a + b))


def beta_band_probs(a, b):
    """P(commit lands in each band) for the continuous draw commit = 2 + 3*Beta(a,b): feint (<=2.75) / light
    (2.75-3.5) / committed (3.5-4.25) / all-in (>=4.25). Deterministic numerical integration — no scipy."""
    import numpy as np
    xs = np.linspace(1e-4, 1 - 1e-4, 600)
    pdf = np.array([_beta_pdf(x, a, b) for x in xs])
    cdf = np.concatenate([[0.0], np.cumsum((pdf[1:] + pdf[:-1]) / 2 * np.diff(xs))])
    cdf = cdf / cdf[-1] if cdf[-1] > 0 else cdf
    F = lambda t: float(np.interp(t, xs, cdf))
    edges = [0.0, 0.25, 0.5, 0.75, 1.0]
    labels = ['feint', 'light', 'committed', 'all-in']
    return {labels[i]: round(F(edges[i + 1]) - F(edges[i]), 3) for i in range(4)}


def node_distribution(ev):
    """For a trace event, return {branch_label: probability} for the alternate branches at that node,
    or None if the node is not a probabilistic branch point. Used by the narrator and branch explorer."""
    k = ev.get('kind')
    if k == 'commit':
        return beta_band_probs(ev['beta_a'], ev['beta_b'])
    if k == 'read':
        p = ev['p_read_win']
        return {'defender reads (Vor flips)': round(p, 4), 'attacker hides it': round(1 - p, 4)}
    if k in ('roll', 'stophit'):
        return degree_distribution(ev['pool'], ev['net_sigma'], ev['ob'])
    if k == 'approach':
        p = ev['stophit_p']
        return {'longer stop-hits': round(p, 4), 'no stop-hit': round(1 - p, 4)}
    return None


if __name__ == '__main__':
    # smoke: a healthy pool with a small edge should be success-weighted; a big negative edge fail-weighted.
    # Ob 1.5 = core.ob_from_defender of a default-History (3) defender.
    print('pool 9, +0.4 sigma :', degree_distribution(9, 0.4, 1.5))
    print('pool 9, -0.8 sigma :', degree_distribution(9, -0.8, 1.5))
    print('pool 5,  0.0 sigma :', degree_distribution(5, 0.0, 1.5))
    d = degree_distribution(9, 0.4, 1.5)
    assert abs(sum(d.values()) - 1.0) < 0.02, d
    print('OK — degree distributions sum to ~1')
