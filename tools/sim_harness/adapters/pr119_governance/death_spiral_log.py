"""death_spiral_log.py — an extensive, per-trial log that traces and flags every death-spiral
pattern this adapter cluster's two campaign engines (`pr119_integrated_campaign.run_campaign`
and `pr119_event_deck_engine.run_deck_campaign`) actually produce, each flag paired with a
cited, concrete proposed patch — not a general "this seems bad" note.

Built in direct response to the ask: "implement an extensive log that traces and flags all
death spirals explicitly complete with proposed patches/adjustments." Reuses both engines'
real return values (no duplicated simulation logic) rather than re-deriving detection from
scratch — a pattern here is a rule over the SAME stats dict the harness/campaign_stats.py
already produce, not a new simulation.

Five named patterns, each grounded in a specific finding from this session's own passes or the
governance-compendium research (designs/audit/2026-07-12-governance-compendium/):

  RECALL_CASCADE            2+ governor recalls in one trial.
  PI_RUNAWAY_SUSTAINED      final Pi >= 9 (pinned near the 0-10 ceiling).
  LEDGER_SCHEMA_CORRUPTION  1+ live Compact ledger tag (the confirmed §1.3a/TAG_KINDS bug).
  GRUDGE_ACCUMULATION       5+ live Grudge tags at trial end (outpacing their own ttl decay).
  PROSPERITY_COLLAPSE       the event-deck engine's own "ruined" terminal classification.

Each pattern's `patch` field cites a real doc, not an invented fix. Output: a JSONL log (one
line per FLAGGED trial x pattern) plus a summary table — both consumed by
designs/audit/2026-07-12-pr119-harness-verification/README.md's death-spiral section.

Usage:
    python3 -m tools.sim_harness.adapters.pr119_governance.death_spiral_log --n 300 --seed 0
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
    __package__ = "tools.sim_harness.adapters.pr119_governance"

from .pr119_event_deck_engine import EventDeckEngineAdapter, run_deck_campaign
from .pr119_integrated_campaign import IntegratedCampaignAdapter, run_campaign

_LOG_PATH = (Path(__file__).resolve().parents[4]
             / "designs" / "audit" / "2026-07-12-pr119-harness-verification"
             / "death_spiral_log.jsonl")


def _detect_integrated(stats: dict) -> list:
    flags = []
    if stats.get("final_pressure", 0) >= 9:
        flags.append(("PI_RUNAWAY_SUSTAINED",
                       f"final Pi={stats['final_pressure']:.2f}",
                       "PATCH: VEN-SE-5 Scuole Grandi Pi-valve (designs/audit/2026-07-12-"
                       "governance-compendium/44_standing_institutions.md) -- 'the stress "
                       "test's highest-value single tuning lever'; re-home as a Sponsor "
                       "sub-option draining Pi through the formula's existing generic "
                       "'-player releases' term, per its own consolidated disposition."))
    if stats.get("compact_tag_count", 0) >= 1:
        flags.append(("LEDGER_SCHEMA_CORRUPTION",
                       f"{stats['compact_tag_count']} live Compact tag(s), TAG_KINDS has no "
                       f"such kind",
                       "PATCH: governance_consolidation_v1.md §1 D3 -- model Compact as a "
                       "Debt subtype (ttl/recurs fields) rather than a 6th ledger family, or "
                       "deliberately extend sim/territory/ledger.py's TAG_KINDS -- either way, "
                       "before §1.3a ratifies (currently blocking)."))
    if stats.get("grudge_tag_count", 0) >= 5:
        flags.append(("GRUDGE_ACCUMULATION",
                       f"{stats['grudge_tag_count']} live Grudge tags outpacing ttl decay",
                       "PATCH: designs/audit/2026-07-12-settlement-season-stress-sim/"
                       "stress_test_synthesis_v1.md's own recommendation -- 'Grudge decay' as "
                       "one of three named substrate fixes (with survivable Appeal odds and a "
                       "defined Suspicion->Recall increment) for the Pattern A/E/G rank-ladder "
                       "death-spiral, which 44_standing_institutions.md confirms NO buildable "
                       "institution can reach."))
    if stats.get("recalled") and stats.get("recall_reason") == "g606":
        flags.append(("RECALL_CASCADE",
                       "terminal recall via G606 (cumulative, not streak-based)",
                       "PATCH: governance_consolidation_v1.md §1 D5 -- merge §1.0d Performance "
                       "Audit onto Goldenfurt's existing G606 suspicion/recall signal as a "
                       "modifier, not a parallel demotion cascade (the confirmed NERS MERGE); "
                       "this session's own 1500-trial run found G606 alone drives ~100% of "
                       "terminal recalls even when §1.0d is tuned lenient."))
    return flags


def _detect_deck(stats: dict) -> list:
    flags = []
    if stats.get("recalls", 0) >= 2:
        flags.append(("RECALL_CASCADE",
                       f"{stats['recalls']} governor recalls in {stats['seasons_survived']} "
                       f"seasons",
                       "PATCH: same as the integrated-campaign RECALL_CASCADE patch above "
                       "(governance_consolidation_v1.md §1 D5) -- both engines independently "
                       "confirm G606 as the dominant recall driver."))
    if stats.get("final_pressure", 0) >= 9:
        flags.append(("PI_RUNAWAY_SUSTAINED",
                       f"final Pi={stats['final_pressure']:.2f}",
                       "PATCH: same as the integrated-campaign PI_RUNAWAY_SUSTAINED patch "
                       "above (VEN-SE-5 Scuole Grandi)."))
    if stats.get("branch") == "ruined":
        flags.append(("PROSPERITY_COLLAPSE",
                       f"final Prosperity={stats['final_prosperity']}, "
                       f"Order={stats['final_order']}, Pi={stats['final_pressure']:.2f}",
                       "PATCH: designs/territory/governance_play_redesign_v1.md §1.3a's own "
                       "cited logic (Scott's extraction-invariance-detonates-revolt) argues "
                       "for a subsistence floor on Extract/Tax Directives against a declining "
                       "settlement; the real counter-lever is the Develop verb itself "
                       "(governance_play_redesign_v1.md §1.3), not yet built in sim/ -- this "
                       "adapter's own 'neglect decay' term is a stand-in for that missing "
                       "positive-feedback path, not a proposed fix in its own right."))
    return flags


def run_and_log(n: int, seed: int, deck_governance_skill: float = 0.35) -> dict:
    """deck_governance_skill defaults BELOW-average (0.35, not the adapter's own 0.5 default)
    deliberately: a death-spiral log run at a mediocre-governor regime is the honest test —
    logging only best-case runs would undercount every pattern here."""
    integrated_adapter = IntegratedCampaignAdapter()
    integrated_params, _ = integrated_adapter.resolve_params(resolver=None)
    deck_adapter = EventDeckEngineAdapter()
    deck_params, _ = deck_adapter.resolve_params(resolver=None)
    deck_params = {**deck_params, "governance_skill": deck_governance_skill}

    rng = random.Random(seed)
    _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    pattern_counts = Counter()
    engine_trial_counts = Counter()
    records = []

    for engine_name, run_fn, params in (
        ("integrated_campaign", run_campaign, integrated_params),
        ("event_deck_engine", run_deck_campaign, deck_params),
    ):
        for trial_idx in range(n):
            branch, stats = run_fn(rng, params)
            engine_trial_counts[engine_name] += 1
            detector = _detect_integrated if engine_name == "integrated_campaign" else _detect_deck
            for pattern, detail, patch in detector(stats):
                pattern_counts[(engine_name, pattern)] += 1
                records.append({
                    "engine": engine_name, "trial": trial_idx, "pattern": pattern,
                    "branch": branch, "detail": detail, "patch": patch,
                })

    with open(_LOG_PATH, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

    return {
        "n_per_engine": n, "seed": seed, "deck_governance_skill": deck_governance_skill,
        "log_path": str(_LOG_PATH),
        "engine_trial_counts": dict(engine_trial_counts),
        "pattern_counts": {f"{e}/{p}": c for (e, p), c in pattern_counts.items()},
        "total_flags": len(records),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=300)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--deck-governance-skill", type=float, default=0.35)
    args = parser.parse_args(argv)
    result = run_and_log(args.n, args.seed, args.deck_governance_skill)
    for k, v in result.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
