"""engine/substrate/stubwire.py — the single owner of "explicitly-flagged not-built".

The ONE new P1 primitive of the Connective-Tissue & Compliance Orchestration Plan
(`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §2.1, ED-IN-0091,
2026-07-29). Every OI-17-class stub (a `NotImplementedError` standing in for design-gated
behavior) converts to a call here instead of raising or fabricating a value. This makes
"explicitly not built" a single, greppable, typed shape rather than N different silent
`"not live"` strings or unconditional raises scattered across the tree — composed on by
`structure_audit.py` (the `stub_wired` node attribute) and `review_core.py` (the
`stubs.count` ratchet signal) without a second registry (CLAUDE.md §8 "every rule lives
once"; §0.1 point 5 "one owner for the operation, every site routed through it").

Contract (frozen, per the plan's §2.1 pin — do not widen without updating the plan):
  - `StubResult` — a frozen dataclass `{module, io_contract, reason, stub: True}`. `stub` is
    not caller-settable: every `StubResult` this module can produce carries `stub=True` by
    construction, so a caller cannot accidentally fabricate a "resolved" stub result.
  - `stub_resolve(module, io_contract, *, reason) -> StubResult` — the sole constructor.
    Callers treat the return value as a typed no-op: no invented numbers, no invented state
    change (§0.1 "No fabrication" / CLAUDE.md §7). `reason` is free-text provenance for why
    the call site is stubbed (cite the design-gate, e.g. an OI-nn / ED-nnnn row) — this module
    does not validate that string; the caller owns its own provenance discipline.
  - `invocations` — a module-level counter, incremented once per `stub_resolve` call. The
    season loop folds it into campaign telemetry (`engine/mc_v18.py` `CampaignResult.stub_hits`,
    the same pattern as the existing F7 `npcs_generated` counter — see that module's docstring).
  - `reset_invocations()` — test-only helper so `tests/valoria/test_stubwire.py` (and any other
    suite) can assert an exact per-test invocation delta without cross-test leakage. Not called
    by any production path.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class StubResult:
    """A typed no-op returned in place of real behavior. `stub` is always True — it is not a
    constructor parameter (init=False) so no call site can construct a StubResult claiming to
    be anything other than what it is."""

    module: str
    io_contract: str
    reason: str
    stub: bool = field(default=True, init=False)


# Module-level invocation counter (§2.1: "the season loop folds it into campaign telemetry").
# Process-lifetime cumulative; callers wanting a per-run delta snapshot `invocations` before and
# after (see engine/mc_v18.py's stub_hits wiring) rather than this module resetting itself —
# resetting on every call would make the counter useless for the ratchet signal in
# tools/review_core.py, which reads a fresh subprocess's cumulative count.
invocations: int = 0


def stub_resolve(module: str, io_contract: str, *, reason: str) -> StubResult:
    """The sole constructor for a stub-wired call site's return value.

    `module` — the dotted module name of the caller (self-identifying, not inferred — no stack
    inspection: explicit is the single-owner discipline CLAUDE.md §0 asks for).
    `io_contract` — the declared I/O contract the stub stands in for (e.g. a `module_contracts.yaml`
    entry name or a short shape description), so a caller of the stub can see what real shape it
    is deferring, not just that it deferred.
    `reason` — why this call site is stubbed (cite the design-gate: an OI-nn row, an ED-<LANE>-NNNN,
    or an accepted cross-session handoff item per the plan's §1 acceptance criteria).
    """
    global invocations
    invocations += 1
    return StubResult(module=module, io_contract=io_contract, reason=reason)


def reset_invocations() -> None:
    """Test-only: zero the module-level counter. Never called from a production code path —
    the counter is process-cumulative by design (see `invocations`' docstring)."""
    global invocations
    invocations = 0
