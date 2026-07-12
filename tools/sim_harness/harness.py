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
from .canon_resolver import CanonGapError, CanonResolver, read_text_or_gap
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
        warns against.

        KNOWN, DELIBERATELY DEFERRED cost: this re-reads and re-parses the ~900-line
        module_contracts.yaml (~75ms) on every single call, with no cache — fine for
        Gate-0's single-shot CLI, but the design doc's own §8 rollout envisions many
        adapters run repeatedly across CI waves. Not fixed here: a process-lifetime
        cache is easy to add but risks subtle staleness if module_contracts.yaml
        changes between Harness constructions within one long-lived process, and
        nothing in this prototype's actual usage needs it yet — revisit when a real
        multi-adapter batch runner exists, with real usage patterns to design against.

        Never raises: a missing/unreadable/non-UTF-8 module_contracts.yaml converts
        to a MAJOR CANON_GAP flag, malformed YAML to the same, PyYAML being
        unavailable to a MAJOR UNCLASSIFIED flag, an unbound/undocumented module to
        CONTRACT_VIOLATION/CANON_GAP — this method always returns normally, it never
        propagates an exception to run()."""
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
        # This runs unconditionally, first, in Harness.run() — before even the
        # try/except around resolve_params(). read_text_or_gap (canon_resolver.py)
        # covers missing/unreadable/non-UTF-8; yaml.YAMLError covers malformed YAML
        # syntax. Neither covers YAML that parses successfully into the WRONG shape
        # (e.g. a top-level list instead of a mapping) — `(data or {}).get(...)`
        # guards the None-on-empty-file case but a non-empty list is truthy, so
        # `.get` on it would raise AttributeError; isinstance guards that too.
        try:
            text = read_text_or_gap(contracts_path, what="module_contracts.yaml")
            data = yaml.safe_load(text)
        except CanonGapError as exc:
            self.logger.triage.flag(
                "contract_binding", Tier.MAJOR, TriageCategory.CANON_GAP, str(exc),
            )
            return
        except yaml.YAMLError as exc:
            self.logger.triage.flag(
                "contract_binding", Tier.MAJOR, TriageCategory.CANON_GAP,
                f"cannot parse {contracts_path}: {exc}",
            )
            return
        if not isinstance(data, dict):
            self.logger.triage.flag(
                "contract_binding", Tier.MAJOR, TriageCategory.CANON_GAP,
                f"{contracts_path} parsed to {type(data).__name__}, expected a "
                f"mapping with a 'modules' key",
            )
            return
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
        # Rejected at the API boundary, not degraded into a flag: with
        # trials_per_point<=0 every per-decision-point trial loop below runs zero
        # iterations, so an adapter's stub/crash paths never fire and the run
        # reports a plausible-looking verdict for a completely different reason
        # than intended (e.g. this package's own shipped demo adapter always
        # raises NotImplementedError on trial 0 to demonstrate STUB_HIT capture —
        # at trials=0 that demonstration silently never happens, yet nothing
        # rejected the input). Found by deliberately running --trials 0.
        if trials_per_point <= 0:
            raise ValueError(
                f"trials_per_point must be positive, got {trials_per_point} — "
                f"a non-positive count means every decision point's trial loop "
                f"runs zero iterations, silently skipping stub/crash detection "
                f"and producing a misleading verdict for the wrong reason"
            )

        try:
            self._check_contract_binding()
            params, provenance = self.adapter.resolve_params(self.resolver)
            if self.adapter.canon_row is None:
                # Deliberate, explicit opt-out for an adapter testing provisional/
                # pre-canonical work — see Adapter.canon_row's docstring for the
                # distinction from contract_module=None. Logged, not silently
                # skipped, and citations stays [] rather than raising or being
                # left unset, so downstream code (TraceEvent) never has to guess
                # whether an empty citations list means "verified but the row
                # happened to cite nothing" or "never checked."
                self.logger.note(
                    "canon_binding",
                    "adapter declares canon_row=None — deliberate opt-out, "
                    "testing provisional/pre-canonical work with no CURRENT.md "
                    "row to verify against yet (see the adapter's own docstring "
                    "for the specific proposal/ED this run is validating)",
                )
                citations = []
            else:
                citations = self.resolver.resolve(self.adapter.canon_row)["doc_paths"]
            missing_provenance = sorted(set(params) - set(provenance))
            if missing_provenance:
                raise ValueError(
                    f"{self.adapter.__class__.__name__}.resolve_params() returned "
                    f"param(s) {missing_provenance} with no provenance entry — "
                    f"every value reaching a trial must be labeled canon-verified "
                    f"or an explicit non-canon test-scenario choice (adapter "
                    f"authoring bug, not a runtime gap — fix the adapter)"
                )
            orphaned_provenance = sorted(set(provenance) - set(params))
            if orphaned_provenance:
                self.logger.triage.flag(
                    "resolve_params", Tier.MINOR, TriageCategory.UNCLASSIFIED,
                    f"provenance declares key(s) {orphaned_provenance} not "
                    f"present in params — stale/orphaned entry (e.g. left over "
                    f"after a param was renamed), silently dropped otherwise; "
                    f"surfaced instead of hidden",
                )
        except CanonGapError as exc:
            self.logger.triage.flag(
                "resolve_params", Tier.MAJOR, TriageCategory.CANON_GAP, str(exc),
            )
            return self.logger
        except Exception as exc:  # noqa: BLE001 — deliberate, see comment below
            # This file has separately special-cased CanonGapError, OSError,
            # yaml.YAMLError, and a bespoke ValueError for missing provenance —
            # one at a time, across 5 rounds of adversarial review, each new
            # exception type discovered by stress-testing producing a new narrow
            # except clause. That's whack-a-mole, not a fix: the deeper guarantee
            # this method exists to make (design doc section 5 — "every run,
            # pass or fail, writes a trace + registry record") requires that NO
            # exception raised during setup, known type or not, can ever crash
            # the whole run uncaught. _check_contract_binding() already converts
            # its own known failure modes to flags internally and never raises;
            # this broad catch is the backstop for everything else, including
            # kinds of failure nobody has hit yet.
            self.logger.triage.flag(
                "run_setup", Tier.MAJOR, TriageCategory.UNCLASSIFIED,
                f"{exc.__class__.__name__} raised during harness setup (contract "
                f"binding / param resolution), before any trial ran: {exc}",
            )
            return self.logger

        for dp in self.adapter.decision_points():
            tier = dp.tier()
            policy = DEPTH_TIERS[tier]
            n = trials_per_point
            branch_counts: Counter = Counter()
            branches_set = set(dp.branches)  # O(1) membership vs. list, matters
            # once a decision point declares many branches (e.g. per-settlement/
            # per-faction adapters in later rollout waves) — found by stress-
            # testing branch-membership cost at thousands of declared branches.
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
                    branch_counts[branch] += 1
                if outcome.detail.get("stub_hit"):
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.STUB_HIT,
                        f"adapter reported a stub/unimplemented branch at {dp.name}",
                    )
                    stub_hit = True
                    # Break immediately, matching the two exception-based stub paths
                    # above — without this, an adapter that sets stub_hit=True every
                    # trial (instead of raising) would produce n duplicate STUB_HIT
                    # flags rather than one. Found alongside the OUT_OF_RANGE spam
                    # below by deliberately stress-testing a systematically
                    # misbehaving adapter at n=10,000.
                    break

            # OUT_OF_RANGE is flagged once per distinct invalid branch (with its
            # count), not once per trial: the first cut of this flagged inline
            # inside the loop above, so a single adapter classification bug at
            # n=10,000 produced 10,000 near-identical flags — real memory bloat and
            # unusable CLI output, found by deliberately stress-testing a
            # systematically-misclassifying adapter at scale.
            #
            # KNOWN LIMITATION (documented, not fixed here): when dp.branches is
            # empty by design (e.g. stub_probe, or a future non-bucketed decision
            # point), this whole OUT_OF_RANGE/completeness/degenerate-distribution
            # section is skipped entirely — any branch value an adapter's Outcome
            # sets in that case is silently tallied into the persisted trace's
            # branch_counts with zero validation. Not currently reachable via the
            # shipped dice_pool_demo adapter (stub_probe always raises before
            # returning an Outcome), and left open rather than force-fitting a
            # fix: it's genuinely ambiguous whether a future adapter intentionally
            # wants free-form, undeclared branch labels for some decision points,
            # or whether that should always be an error. Resolve this the next
            # time an adapter actually needs it, with real requirements in hand.
            if dp.branches:
                for bad_branch, count in branch_counts.items():
                    if bad_branch not in branches_set:
                        self.logger.triage.flag(
                            dp.name, tier, TriageCategory.OUT_OF_RANGE,
                            f"{count}/{n} trial(s) classified into branch "
                            f"{bad_branch!r}, not declared in decision point's "
                            f"branches {dp.branches}",
                        )

            actual_n = sum(branch_counts.values())
            # Branches not in branches_set are already loudly flagged above as
            # OUT_OF_RANGE with their own count — the degenerate-distribution
            # concentration check below must not ALSO count them as if they were
            # a legitimate (if skewed) sampled outcome, or a systematically
            # broken adapter that misclassifies nearly everything into one
            # undeclared value gets reported as "99% collapsed into a real
            # outcome" instead of "99% of trials produced no valid data at all"
            # — a misleading understatement of exactly how broken the run is.
            # Found by adversarial review with a reproducing adapter (99/100
            # trials into an undeclared branch produced a DEGENERATE_DISTRIBUTION
            # message naming that undeclared branch as the "collapsed" outcome).
            valid_branch_counts = (
                Counter({k: v for k, v in branch_counts.items() if k in branches_set})
                if dp.branches else branch_counts
            )
            valid_n = sum(valid_branch_counts.values())

            # dp.branches non-empty means this decision point DECLARED it classifies
            # trials into buckets — if it also ran n>0 trials without a stub/crash yet
            # produced fewer classified outcomes than trials run, the adapter is
            # silently failing to set Outcome.detail['branch'] on some or all trials.
            # Without this check that state reports verdict PASS with zero flags and
            # zero real data (actual_n=0 in the trace, but nothing reacts to it) —
            # exactly the "claims to verify, doesn't" failure this harness exists to
            # prevent, recurring one layer up from the registry-logging gap it was
            # built to fix. Found by adversarial review with a reproducing adapter.
            if not stub_hit and dp.branches and n > 0 and actual_n < n:
                self.logger.triage.flag(
                    dp.name, tier, TriageCategory.UNCLASSIFIED,
                    f"adapter completed {n} trial(s) but only classified {actual_n} "
                    f"into a declared branch — Outcome.detail['branch'] was unset "
                    f"for the remaining {n - actual_n}; sampled data is incomplete "
                    f"and should not be trusted",
                )

            if not stub_hit and n < policy.min_n:
                self.logger.triage.flag(
                    dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                    f"tier-{int(tier)} ({policy.label}) event sampled at n={n} < "
                    f"required min_n={policy.min_n} — no distribution claim without "
                    f"enough trials (per sim/tests/test_f7_smoke_oracle.py's lesson: "
                    f"no balance claim without an oracle + n >= 100)",
                )

            if (not stub_hit and policy.degenerate_threshold is not None
                    and len(dp.branches) > 1 and valid_n > 0):
                top_branch, top_count = valid_branch_counts.most_common(1)[0]
                if top_count / valid_n >= policy.degenerate_threshold:
                    self.logger.triage.flag(
                        dp.name, tier, TriageCategory.DEGENERATE_DISTRIBUTION,
                        f"{top_count}/{valid_n} valid trials ({top_count / valid_n:.1%}) "
                        f"collapsed into single branch {top_branch!r} at tier "
                        f"{int(tier)} ({policy.label}) — exceeds the "
                        f"{policy.degenerate_threshold:.0%} threshold for this tier",
                    )

            self.logger.record(TraceEvent(
                event_id=dp.name, tier=int(tier), n=actual_n,
                branch_counts=dict(branch_counts), citations=citations,
                justification=dp.justification,
                param_provenance={k: provenance[k] for k in params},
                canon_status="provisional" if self.adapter.canon_row is None else "verified",
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
    if args.trials <= 0:
        # Clean CLI rejection (argparse usage message, exit code 2, no traceback)
        # rather than letting Harness.run()'s own ValueError propagate as a raw
        # traceback through main() — Harness.run() still validates this too, for
        # direct (non-CLI) callers, but the CLI should fail like a CLI.
        parser.error(f"--trials must be positive, got {args.trials}")

    adapter = _build_adapter(args.adapter)
    harness = Harness(adapter, seed=args.seed)
    logger = harness.run(trials_per_point=args.trials)

    # Print the console summary FIRST, from data already held in memory, before
    # attempting either durable write below — write_trace()/append_registry_record()
    # can themselves fail (disk full, permissions, results/ existing as a plain
    # file instead of a directory), and neither call was previously guarded;
    # an uncaught failure there used to take the whole process down with a raw
    # traceback and lose even the console-visible summary of a run that had
    # already completed successfully. Found by adversarial review.
    n_events = sum(1 for e in logger.events if getattr(e, "kind", "event") == "event")
    print(f"events: {n_events}  triage flags: {len(logger.triage.flags)}")
    for f in logger.triage.flags:
        print(f"  [{f.category.value}] tier={f.tier} {f.event_id}: {f.detail}")
    verdict = logger.triage.verdict()
    print(f"verdict: {verdict}")

    try:
        trace_path = logger.write_trace(RESULTS_DIR)
        print(f"trace written: {trace_path}")
    except OSError as exc:
        print(f"WARNING: could not write trace file: {exc}", file=sys.stderr)

    if not args.no_registry:
        try:
            record = logger.append_registry_record(
                subsystem=adapter.registry_subsystem,
                scope=f"sim-harness Gate-0 run over {adapter.__class__.__name__} "
                      f"(n={args.trials}, seed={args.seed})",
                folder="designs/audit/2026-07-12-simulation-test-harness-methodology/",
            )
            print(f"audit_registry.jsonl appended: {record['id']}")
        except (OSError, ValueError) as exc:
            print(f"WARNING: could not append to audit_registry.jsonl: {exc}", file=sys.stderr)

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
