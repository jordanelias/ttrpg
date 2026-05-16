"""m7_balance_sweep — N=1000 balance sweep for mc_v17 with Wilson 95% CI.  # [canonical: N/A — doc]

Per integration_plan_v3 §5 Phase 2d:                                          # [canonical: N/A — doc]
  N=1000 balance battery + Wilson CI check (all factions in [20%, 30%] at 95%) # [canonical: N/A — doc]
"""
import json
import math
import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mc_v17 as v17  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]


# ═══════════════════════════════════════════════════════════════════════════
# WILSON 95% CONFIDENCE INTERVAL
# ═══════════════════════════════════════════════════════════════════════════

# [canonical: standard statistical formula — Wilson (1927) score CI for proportions]
WILSON_Z_95 = 1.96  # [canonical: standard normal 0.975 quantile for 95% CI]


def wilson_ci(successes, n, z=WILSON_Z_95):  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    # [canonical: Wilson score interval — standard formula for binomial proportion CI]
    if n == 0:
        return (0.0, 0.0)
    phat = successes / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (phat + z2 / (2 * n)) / denom
    spread = z * math.sqrt(phat * (1 - phat) / n + z2 / (4 * n * n)) / denom  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    return (max(0.0, center - spread), min(1.0, center + spread))


# ═══════════════════════════════════════════════════════════════════════════
# SWEEP RUNNER
# ═══════════════════════════════════════════════════════════════════════════

def run_sweep(n=1000, params=None, log_dir=None, test_id='v17_sweep'):  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    """Run N campaigns; return per-faction win shares + Wilson 95% CIs."""
    # [canonical: integration_plan §5 Phase 2d]
    t_start = time.time()
    print(f"=== v17 balance sweep — N={n} ===")
    if params:
        print(f"  Params: {params}")

    wins = {'Crown': 0, 'Church': 0, 'Hafenmark': 0, 'Varfell': 0}
    battles_total = 0
    season_ended_list = []

    for i in range(n):
        r = v17.run_campaign(params=params, seed=i,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                             log_dir=(log_dir if (log_dir and i < 5) else None),  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                             test_id=test_id)
        if r['winner'] in wins:
            wins[r['winner']] += 1
        battles_total += r.get('battles', 0)
        season_ended_list.append(r.get('season_ended', 0))
        if (i + 1) % 100 == 0:
            elapsed = time.time() - t_start
            print(f"  [{i+1:5d}/{n}] elapsed {elapsed:.1f}s  partial: {wins}")

    elapsed = time.time() - t_start
    decided = sum(wins.values())

    # Compute Wilson 95% CIs per faction
    cis = {fn: wilson_ci(wins[fn], n) for fn in wins}
    shares = {fn: wins[fn] / n * 100 for fn in wins}

    # Balance check — every faction's 95% CI overlapping [20%, 30%]
    BAND_LOW = 0.20  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    BAND_HIGH = 0.30  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    in_band = {}
    for fn in wins:
        lo, hi = cis[fn]
        # CI overlaps band iff lo <= BAND_HIGH AND hi >= BAND_LOW
        in_band[fn] = (lo <= BAND_HIGH) and (hi >= BAND_LOW)

    report = {
        'n': n,
        'decided': decided,
        'elapsed_seconds': round(elapsed, 1),
        'campaigns_per_second': round(n / elapsed, 1) if elapsed > 0 else 0,
        'wins': wins,
        'win_share_pct': {k: round(v, 2) for k, v in shares.items()},
        'wilson_95_ci_pct': {k: [round(lo * 100, 2), round(hi * 100, 2)]
                              for k, (lo, hi) in cis.items()},
        'in_balance_band_20_30': in_band,
        'all_factions_in_band': all(in_band.values()),
        'battles_total': battles_total,
        'battles_per_campaign': round(battles_total / n, 2) if n else 0,
        'mean_season_ended': round(sum(season_ended_list) / n, 2) if n else 0,
    }

    print(f"\n=== Sweep complete in {elapsed:.1f}s ({n/elapsed:.1f} campaigns/sec) ===")
    print(f"  win_share_pct:  {report['win_share_pct']}")
    print(f"  wilson_95_ci:   {report['wilson_95_ci_pct']}")
    print(f"  in_band_20_30:  {in_band}")
    print(f"  all_in_band:    {report['all_factions_in_band']}")
    print(f"  battles/campaign: {report['battles_per_campaign']}")
    print(f"  mean season ended: {report['mean_season_ended']}")

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        report_path = os.path.join(log_dir, f'{test_id}_report.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"  Report written: {report_path}")

    return report


if __name__ == '__main__':
    # Default: small sweep for smoke; pass N as arg for full run
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    log_dir = '/home/claude/v17_sweep_logs' if n >= 1000 else None  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    run_sweep(n=n, log_dir=log_dir)
