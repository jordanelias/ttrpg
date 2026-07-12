"""harness.py — Harness core: orchestrates one run of an Adapter, independent of any
subsystem-specific knowledge.

THIS IS A GATE-0 PROTOTYPE (design doc section 10): one demo adapter ships
(adapters/dice_pool_demo.py), not wired into CI, not a coverage claim over any
subsystem beyond the demo. See
designs/audit/2026-07-12-simulation-test-harness-methodology/simulation_test_harness_methodology_v1.md
for the full architecture, the depth-tier rubric, and the real rollout order.

Usage:
    python -m tools.sim_harness.harness --trials 300 --seed 1
    python -m tools.sim_harness.harness --no-registry   # skip the audit_registry.jsonl append
"""
from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from pathlib import Path

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    __package__ = "tools.sim_harness"

from .adapter import Adapter
from .canon_resolver import CanonGapError, CanonResolver
from .depth import DEPTH_TIERS, Tier
from .trace_logger import TraceEvent, TraceLogger
from .triage import TriageCategory

RESULTS_DIR = Path(__file__).resolve().parent / "results"


class Harness:
    def __init__(self, adapter: Adapter, *, seed: int = 0):
        self.adapter = adapter
        # valoria_dice.py's trial core calls the `random` module directly rather than
        # accepting an injected Random instance, so Gate-0 seeds globally for
        # reproducibility; a future adapter that takes an injected rng can ignore this.
        random.seed(seed)
        self.rng = random.Random(seed)
        self.resolver = CanonResolver()
        self.logger = TraceLogger(adapter.__class__.__name__, adapter.contract_module)

    def _check_contract_binding(self) -> None:
        """Gate-0's contract check is intentionally minimal: confirm the declared
        module (if any) exists in module_contracts.yaml and note its doc/status.
        Running the real A1-A12 closure checks (skills/valoria-module-adjudicator/
        scripts/contract_adjudicator.py) against the live corpus on every harness run
        is Wave 1 work (design doc section 4/7), not implemented here."""
        if self.adapter.contract_module is None:
            self.logger.events.append  # no-op; explicit opt-out, nothing to flag
            return
        try:
            import yaml  # already a repo dependency (tools/ci_* scripts use it)
        except ImportError:
            self.logger.triage.flag(
                "contract_binding", Tier.MAJOR, TriageCategory.UNCLASSIFIED,
                "PyYAML unavailable locally — contract binding not checked this run",
            )
            return
        contracts_path = Path(__file__).resolve().parents[2] / "references" / "module_contracts.yaml"
        data = yaml.safe_load(contracts_path.read_text(encoding="utf-8"))
        entries = {m["module"]: m for m in data.get("modules", [])}
        entry = entries.get(self.adapter.contract_module)
        if entry is None:
            self.logger.triage.flag(
                "contract_binding", Tier.MAJOR, TriageCategory.CONTRACT_VIOLATION,
                f"adapter declares contract_module={self.adapter.contract_module!r}, "
                f"not found in references/module_contracts.yaml",
            )
        elif not entry.get("doc"):
            self.logger.triage.flag(
                "contract_binding", Tier.MEDIUM, TriageCategory.CANON_GAP,
                f"module {self.adapter.contract_module!r} has doc: null in "
                f"module_contracts.yaml — this adapter's runs cannot be checked "
                f"against a canonical spec",
            )

    def run(self, trials_per_point: int = 200) -> TraceLogger:
        self._check_contract_binding()

        try:
            params = self.adapter.resolve_params(self.resolver)
            citations = self.resolver.resolve(self.adapter.canon_row)["doc_paths"]
        except CanonGapError as exc:
            self.logger.triage.flag(
                "resolve_params", Tier.MAJOR, TriageCategory.CANON_GAP, str(exc),
            )
            return self.logger

        for dp in self.adapter.decision_points():
            tier = dp.tier()
            policy = DEPTH_TIERS[tier]
            n = trials_per_point
            branch_counts: Counter = Counter()

            for _ in range(n):
                outcome = self.adapter.run_once(self.rng, params, dp)
                branch = outcome.detail.get("branch")
                if branch is not None:
                    if dp.branches and branch not in dp.branches:
                        self.logger.triage.flag(
                            dp.name, tier, TriageCategory.OUT_OF_RANGE,
                            f"outcome classified into branch {branch!r}, not declared "
                            f"in decision point's branches {dp.branches}",
                        )
                    branch_counts[branch] += 1
                if outcome.detail.get("stub_hit"):
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.STUB_HIT,
                        f"adapter reported a stub/unimplemented branch at {dp.name}",
                    )

            if n < policy.min_n:
                self.logger.triage.flag(
                    dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                    f"tier-{int(tier)} ({policy.label}) event sampled at n={n} < "
                    f"required min_n={policy.min_n} — no distribution claim without "
                    f"enough trials (per sim/tests/test_f7_smoke_oracle.py's lesson: "
                    f"no balance claim without an oracle + n >= 100)",
                )

            if policy.degenerate_threshold is not None and len(dp.branches) > 1 and n > 0:
                top_branch, top_count = branch_counts.most_common(1)[0] if branch_counts else (None, 0)
                if top_count / n >= policy.degenerate_threshold:
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                        f"{top_count}/{n} trials ({top_count / n:.1%}) collapsed into "
                        f"single branch {top_branch!r} at tier {int(tier)} "
                        f"({policy.label}) — exceeds the {policy.degenerate_threshold:.0%} "
                        f"threshold for this tier",
                    )

            self.logger.record(TraceEvent(
                event_id=dp.name, tier=int(tier), n=n,
                branch_counts=dict(branch_counts), citations=citations,
                contract_note=(f"contract_module={self.adapter.contract_module!r}"
                                if self.adapter.contract_module else "no module_contracts.yaml "
                                "row — cross-cutting substrate, deliberate opt-out"),
            ))

        return self.logger


def _build_adapter(name: str) -> Adapter:
    if name == "dice_pool_demo":
        from .adapters.dice_pool_demo import DicePoolAdapter
        return DicePoolAdapter()
    raise SystemExit(f"unknown adapter {name!r} — only dice_pool_demo ships in Gate-0")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Gate-0 simulation/test harness prototype")
    parser.add_argument("--adapter", default="dice_pool_demo",
                         help="adapter name under adapters/ (Gate-0: only dice_pool_demo)")
    parser.add_argument("--trials", type=int, default=200, help="trials per decision point")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--no-registry", action="store_true",
                         help="skip the audit_registry.jsonl append (dry run)")
    args = parser.parse_args(argv)

    adapter = _build_adapter(args.adapter)
    harness = Harness(adapter, seed=args.seed)
    logger = harness.run(trials_per_point=args.trials)

    trace_path = logger.write_trace(RESULTS_DIR)
    print(f"trace written: {trace_path}")
    print(f"events: {len(logger.events)}  triage flags: {len(logger.triage.flags)}")
    for f in logger.triage.flags:
        print(f"  [{f.category.value}] tier={f.tier} {f.event_id}: {f.detail}")
    verdict = logger.triage.verdict()
    print(f"verdict: {verdict}")

    if not args.no_registry:
        record = logger.append_registry_record(
            subsystem=adapter.registry_subsystem,
            scope=f"sim-harness Gate-0 run over {adapter.__class__.__name__} "
                  f"(n={args.trials}, seed={args.seed})",
            folder="designs/audit/2026-07-12-simulation-test-harness-methodology/",
        )
        print(f"audit_registry.jsonl appended: {record['id']}")

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
