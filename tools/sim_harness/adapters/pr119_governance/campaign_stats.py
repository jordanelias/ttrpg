"""campaign_stats.py — standalone world-state statistics pass over
pr119_integrated_campaign.run_campaign().

The harness's own trace (via `--adapter pr119_integrated_campaign`) answers "what happened"
(a branch-count distribution over the 4 emergent outcomes). It does not capture per-trial
NUMERIC world state (final Pi, ledger tag composition, province Accord, which recall reason
fired) — TraceEvent only persists n/branch_counts, by design (see harness.py). This script
calls the SAME run_campaign() function directly (no duplicated simulation logic) in a plain
loop with its own seeded random.Random, so the numbers in designs/audit/2026-07-12-pr119-
harness-verification/README.md's "Interdependency & emergence" section are reproducible by
re-running this file, not hand-copied from a one-off session.

Usage:
    python3 -m tools.sim_harness.adapters.pr119_governance.campaign_stats [--n 500] [--seed 0]
"""
from __future__ import annotations

import argparse
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
    __package__ = "tools.sim_harness.adapters.pr119_governance"

from .pr119_integrated_campaign import IntegratedCampaignAdapter, run_campaign


def gather(n: int, seed: int, overrides: dict | None = None) -> dict:
    adapter = IntegratedCampaignAdapter()
    params, _provenance = adapter.resolve_params(resolver=None)  # no CanonResolver calls in this adapter
    if overrides:
        params = {**params, **overrides}
    rng = random.Random(seed)
    branch_counts: Counter = Counter()
    recall_reasons: Counter = Counter()
    final_pressures, seasons_survived, compact_counts, grudge_counts = [], [], [], []
    province_accords, guild_influences = [], []
    rescued = 0
    za_lapsed = 0
    seggio_entrenched = 0

    for _ in range(n):
        branch, stats = run_campaign(rng, params)
        branch_counts[branch] += 1
        if stats["recall_reason"]:
            recall_reasons[stats["recall_reason"]] += 1
        final_pressures.append(stats["final_pressure"])
        seasons_survived.append(stats["seasons_survived"])
        compact_counts.append(stats["compact_tag_count"])
        grudge_counts.append(stats["grudge_tag_count"])
        province_accords.append(stats["final_province_accord"])
        guild_influences.append(stats["guild_influence"])
        rescued += int(stats["rescued_by_corruption"])
        za_lapsed += int(stats["za_lapsed"])
        seggio_entrenched += int(stats["seggio_entrenched"])

    return {
        "n": n, "seed": seed,
        "branch_counts": dict(branch_counts),
        "recall_reasons": dict(recall_reasons),
        "rescue_rate": rescued / n,
        "za_lapse_rate": za_lapsed / n,
        "seggio_entrenchment_rate": seggio_entrenched / n,
        "mean_final_pressure": statistics.fmean(final_pressures),
        "mean_seasons_survived": statistics.fmean(seasons_survived),
        "mean_compact_tag_count": statistics.fmean(compact_counts),
        "mean_grudge_tag_count": statistics.fmean(grudge_counts),
        "mean_final_province_accord": statistics.fmean(
            [a for a in province_accords if a is not None]),
        "mean_guild_influence": statistics.fmean(guild_influences),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=500)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--p-comply", type=float, default=None,
                         help="override the shared per-season compliance rate "
                              "(default: the adapter's own 0.5, a test-scenario value)")
    parser.add_argument("--pa-demotion-streak", type=int, default=None,
                         help="override §1.0d's consecutive-miss demotion threshold "
                              "(default: the adapter's own 3, PROVISIONAL per §1.0d's text)")
    args = parser.parse_args(argv)
    overrides = {}
    if args.p_comply is not None:
        overrides["p_comply"] = args.p_comply
    if args.pa_demotion_streak is not None:
        overrides["pa_demotion_streak"] = args.pa_demotion_streak
    result = gather(args.n, args.seed, overrides or None)
    for k, v in result.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
