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
import hashlib
import random
import sys
from collections import Counter
from pathlib import Path

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    __package__ = "tools.sim_harness"

from . import adapters as _adapters_pkg  # noqa: F401  (import triggers @register_adapter on every shipped adapter)
from .adapter import ADAPTER_REGISTRY, Adapter
from .canon_resolver import CanonGapError, CanonResolver
from .depth import DEPTH_TIERS, Tier
from .trace_logger import TraceEvent, TraceLogger
from .triage import TriageCategory

RESULTS_DIR = Path(__file__).resolve().parent / "results"


class Harness:
    def __init__(self, adapter: Adapter, *, seed: int = 0):
        self.adapter = adapter
        self._seed = seed
        self.resolver = CanonResolver()
        self.logger = TraceLogger(adapter.__class__.__name__, adapter.contract_module)

    def _check_contract_binding(self) -> None:
        """Gate-0's contract check is intentionally minimal: confirm the declared
        module (if any) exists in module_contracts.yaml and note its doc/status.
        Running the real A1-A12 closure checks (skills/valoria-module-adjudicator/
        scripts/contract_adjudicator.py) against the live corpus on every harness run
        is Wave 1 work (design doc section 4/7), not implemented here — deliberately
        not duplicated here; adjudicator.py's checks need a registry_path this
        generic harness has no natural value for, and re-implementing A1-A12 by hand
        would be exactly the kind of second, drifting parser CLAUDE.md section 8
        warns against."""
        if self.adapter.contract_module is None:
            self.logger.note(
                "contract_binding",
                "adapter declares contract_module=None — deliberate opt-out for "
                "cross-cutting substrate with no references/module_contracts.yaml "
                "row of its own (see the adapter's own docstring for why)",
            )
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
        entries = {m.get("module"): m for m in data.get("modules", []) if m.get("module")}
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

    def _run_one_trial(self, dp, params, trial_idx: int):
        """Reseed deterministically per trial (base seed, event name, trial index)
        so reproducibility does not depend on constructor-time global state alone —
        a second Harness built later in the same process cannot silently perturb an
        earlier one's sequence, since every trial re-establishes its own seed
        immediately before running.

        Uses hashlib, not Python's builtin hash(): str/tuple hashing is
        PYTHONHASHSEED-salted per process by default (a deliberate CPython security
        feature), so hash((seed, dp.name, trial_idx)) silently produces a DIFFERENT
        derived seed on every process run — the exact opposite of the determinism
        this method exists to guarantee. Caught by re-running the same --seed twice
        and diffing trace content_hash before trusting this method."""
        digest = hashlib.sha256(f"{self._seed}:{dp.name}:{trial_idx}".encode()).digest()
        derived_seed = int.from_bytes(digest[:8], "big")
        random.seed(derived_seed)
        rng = random.Random(derived_seed)
        return self.adapter.run_once(rng, params, dp)

    def run(self, trials_per_point: int = 200) -> TraceLogger:
        self._check_contract_binding()

        try:
            params, provenance = self.adapter.resolve_params(self.resolver)
            citations = self.resolver.resolve(self.adapter.canon_row)["doc_paths"]
        except CanonGapError as exc:
            self.logger.triage.flag(
                "resolve_params", Tier.MAJOR, TriageCategory.CANON_GAP, str(exc),
            )
            return self.logger

        missing_provenance = sorted(set(params) - set(provenance))
        if missing_provenance:
            raise ValueError(
                f"{self.adapter.__class__.__name__}.resolve_params() returned "
                f"param(s) {missing_provenance} with no provenance entry — every "
                f"value reaching a trial must be labeled canon-verified or an "
                f"explicit non-canon test-scenario choice (adapter authoring bug, "
                f"not a runtime gap — fix the adapter)"
            )

        for dp in self.adapter.decision_points():
            tier = dp.tier()
            policy = DEPTH_TIERS[tier]
            n = trials_per_point
            branch_counts: Counter = Counter()
            stub_hit = False

            for trial_idx in range(n):
                try:
                    outcome = self._run_one_trial(dp, params, trial_idx)
                except NotImplementedError as exc:
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.STUB_HIT,
                        f"adapter's resolver raised NotImplementedError on trial "
                        f"{trial_idx}/{n} — genuine stub/unimplemented branch: {exc}",
                    )
                    stub_hit = True
                    break
                except Exception as exc:  # noqa: BLE001 — deliberate: a crashing
                    # adapter must still produce a trace + registry record instead
                    # of taking the whole harness process down with it (this is the
                    # exact "claims to log, doesn't" failure mode one layer down
                    # that the design doc's own section 5 promise depends on not
                    # happening).
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.UNCLASSIFIED,
                        f"adapter raised {exc.__class__.__name__} on trial "
                        f"{trial_idx}/{n}, not caught by the adapter itself: {exc}",
                    )
                    stub_hit = True
                    break

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
                    stub_hit = True

            actual_n = sum(branch_counts.values())

            if not stub_hit and n < policy.min_n:
                self.logger.triage.flag(
                    dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                    f"tier-{int(tier)} ({policy.label}) event sampled at n={n} < "
                    f"required min_n={policy.min_n} — no distribution claim without "
                    f"enough trials (per sim/tests/test_f7_smoke_oracle.py's lesson: "
                    f"no balance claim without an oracle + n >= 100)",
                )

            if (not stub_hit and policy.degenerate_threshold is not None
                    and len(dp.branches) > 1 and actual_n > 0):
                top_branch, top_count = branch_counts.most_common(1)[0]
                if top_count / actual_n >= policy.degenerate_threshold:
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                        f"{top_count}/{actual_n} trials ({top_count / actual_n:.1%}) "
                        f"collapsed into single branch {top_branch!r} at tier "
                        f"{int(tier)} ({policy.label}) — exceeds the "
                        f"{policy.degenerate_threshold:.0%} threshold for this tier",
                    )

            self.logger.record(TraceEvent(
                event_id=dp.name, tier=int(tier), n=actual_n,
                branch_counts=dict(branch_counts), citations=citations,
                justification=dp.justification,
                param_provenance={k: provenance[k] for k in params},
                contract_note=(f"contract_module={self.adapter.contract_module!r}"
                                if self.adapter.contract_module else "no module_contracts.yaml "
                                "row — cross-cutting substrate, deliberate opt-out"),
            ))

        return self.logger


def _build_adapter(name: str) -> Adapter:
    cls = ADAPTER_REGISTRY.get(name)
    if cls is None:
        raise SystemExit(
            f"unknown adapter {name!r} — available: {sorted(ADAPTER_REGISTRY)}"
        )
    return cls()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Gate-0 simulation/test harness prototype")
    parser.add_argument("--adapter", default="dice_pool_demo",
                         help=f"adapter name (available: {sorted(ADAPTER_REGISTRY)})")
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
    n_events = sum(1 for e in logger.events if getattr(e, "kind", "event") == "event")
    print(f"events: {n_events}  triage flags: {len(logger.triage.flags)}")
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
