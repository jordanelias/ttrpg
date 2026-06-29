"""Branch-probability math for the Combat Workbench (WS-6) narrator + branch explorer.

Given the INPUTS the engine emits at each decision node (wrapper._emit events), reconstruct the
probability of each ALTERNATE branch — the "what else could have happened, and how likely" view that
turns an n=1 trace into something honest. The engine emits facts (the inputs a node consumed and the
sampled outcome); this module turns those inputs into the local distribution.

Single source of truth: every canonical value (per-die mean, sigma_n, the soft-cap, the decisive Ob,
the degree thresholds) is IMPORTED from the engine (core / m1), never re-declared here — so a tuning
change to the engine flows through automatically and the sim-fabrication discipline holds by import.
Degree banding mirrors core.degree() exactly (the ER-2 continuity-corrected k-0.5 thresholds)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from math import erf, sqrt, exp
import core                      # importing core also puts the r1/r8/m1 substrate dir on sys.path
import m1_dice_sigma_core as m1  # so this resolves without re-adding the path


def _phi(z):
    """Standard normal CDF via erf (no scipy dependency)."""
    return 0.5 * (1.0 + erf(z / sqrt(2.0)))


def degree_distribution(pool, net_sigma):
    """P(fail / partial / success / overwhelming) for one resolution roll under the continuous engine.

    core.resolve draws net ~ Normal(mean, sd) then bands it with core.degree(net, DECISIVE_OB):
        mean = mu_per_die * pool + soft_cap(net_sigma) * sigma_n(pool)
        sd   = sigma_n(pool) = 0.8 * sqrt(pool)
    Thresholds mirror core.degree (continuity-corrected): fail net<0.5; success net>=ob-0.5;
    overwhelming net>=max(2*ob-0.5, 2.5); partial otherwise."""
    ob = core.DECISIVE_OB
    mu = m1.PER_DIE[m1.TN_STANDARD][0]            # canonical per-die mean at TN7
    sd = float(m1.sigma_n(pool))                  # 0.8 * sqrt(pool)
    mean = mu * pool + float(m1.soft_cap(net_sigma)) * sd
    t_fail = 0.5
    t_succ = ob - 0.5
    t_over = max(2 * ob - 0.5, 2.5)
    F = lambda t: _phi((t - mean) / sd)
    p_fail = F(t_fail)
    p_part = F(t_succ) - F(t_fail)
    p_over = 1.0 - F(t_over)
    p_succ = F(t_over) - F(t_succ)
    d = {'fail': p_fail, 'partial': p_part, 'success': p_succ, 'overwhelming': p_over}
    return {k: max(0.0, round(v, 4)) for k, v in d.items()}


def read_win_p(read_d, read_a):
    """P(defender wins the read) = sigmoid(read_d - read_a) — the wrapper read contest (scale 1.0)."""
    return round(1.0 / (1.0 + exp(-(read_d - read_a) / 1.0)), 4)


def outcome_distribution(degree, mode, cfg, exposure=0.0):
    """DEPTH-2: given a roll degree and the defender's mode, the {hit, bind, riposte, miss} distribution it leads
    to — computed from the engine's outcome-mapping rules (wrapper.py:173-198) + cfg. This is the "what does each
    roll outcome lead to" branch the explorer expands under the roll node (overcommit_exposure≈0 by default)."""
    neut = {'parry': cfg['NEUTRALIZE_PARRY'], 'dodge': cfg['NEUTRALIZE_DODGE'], 'wind': cfg['NEUTRALIZE_WIND']}[mode]
    out = {'hit': 0.0, 'bind': 0.0, 'riposte': 0.0, 'miss': 0.0}
    if degree == 'fail':
        rip = min(0.95, cfg['RIPOSTE_ON_FAIL'] + exposure)
        out['riposte'], out['miss'] = rip, 1 - rip
    elif degree == 'partial':
        if mode == 'dodge':
            g = cfg['PARTIAL_DODGE_GRAZE']; out['hit'], out['miss'] = g, 1 - g
        elif mode == 'parry':
            g = cfg['PARTIAL_PARRY_GRAZE']; out['hit'], out['miss'] = g, 1 - g
        else:
            out['bind'] = 1.0
    elif degree == 'success':
        rip_p = min(0.95, cfg['RIPOSTE_ON_NEUTRALIZE'] + exposure)
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
    if k == 'roll':
        return degree_distribution(ev['pool'], ev['net_sigma'])
    if k == 'stophit':
        return degree_distribution(ev['pool'], ev['net_sigma'])
    if k == 'approach':
        p = ev['stophit_p']
        return {'longer stop-hits': round(p, 4), 'no stop-hit': round(1 - p, 4)}
    return None


if __name__ == '__main__':
    # smoke: a healthy pool with a small edge should be success-weighted; a big negative edge fail-weighted
    print('pool 9, +0.4 sigma :', degree_distribution(9, 0.4))
    print('pool 9, -0.8 sigma :', degree_distribution(9, -0.8))
    print('pool 5,  0.0 sigma :', degree_distribution(5, 0.0))
    d = degree_distribution(9, 0.4)
    assert abs(sum(d.values()) - 1.0) < 0.02, d
    print('OK — degree distributions sum to ~1')
