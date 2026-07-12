# `tools/sim_harness/` — Gate-0 prototype

**Status: PROPOSED, ED-IN-0038.** Not wired into CI or local hooks. This is a proof of the
architecture described in
`designs/audit/2026-07-12-simulation-test-harness-methodology/simulation_test_harness_methodology_v1.md`
— read that doc first for the full methodology, the depth-tier rubric, the triage-flag taxonomy, and
the real rollout order (§8). This README is usage notes only.

**Revision note:** this package went through an adversarial review pass (8 independent finder angles)
that found several real defects in the first cut, then a fix pass that closed all of them — see the
per-file docstrings for what changed and why (each corrected claim states the failure it replaces, not
just the new behavior). The most important one: an uncaught exception from a stub subsystem used to
crash the whole run before any trace or registry entry was written; `Harness.run()` now catches it and
reports a `STUB_HIT`/`UNCLASSIFIED` triage flag instead, and the shipped demo adapter includes a
synthetic decision point (`stub_probe`) that deliberately exercises this path so the fix has a real,
working, always-run example rather than only a claim about it.

## What ships here

- `canon_resolver.py` — resolves a subsystem's live canonical head from `CURRENT.md` (reusing
  `tools/currency_consistency_check.py`'s existing path parser rather than a second one), and can
  `verify_citation()` that one specific asserted string is still literally present in a cited doc before
  a caller trusts it. Never fabricates.
- `depth.py` — the 1 (minor) / 2 (medium) / 3 (major) tier policy. Every `DecisionPoint` must declare a
  non-empty `justification` (enforced at construction, not just documented) and that justification is
  carried into the trace.
- `triage.py` — the mandatory triage-flag taxonomy and verdict rule (a flag can never be silently
  swallowed into a PASS).
- `adapter.py` — the `Adapter` protocol every subsystem's "test module" implements, plus the
  `@register_adapter("name")` decorator + `ADAPTER_REGISTRY` that makes adding one a single-file,
  single-import operation — the harness core never hardcodes an adapter name.
- `trace_logger.py` — per-event trace (deterministic JSON, matching `sim/substrate/keys.py`'s `KeyLog`
  serialization convention — but not its schema/validation, see the module docstring for the precise
  boundary) + a **live** (not backfilled) `references/audit_registry.jsonl` append.
- `harness.py` — orchestrator + CLI. Catches `NotImplementedError` (and any other exception) raised by
  an adapter's `run_once()` and converts it to a triage flag instead of crashing; reseeds deterministically
  per trial (via `hashlib`, not Python's salted builtin `hash()` — see `_run_one_trial`'s docstring for
  why that distinction matters) so `--seed N` is reproducible across separate process runs, not just
  within one.
- `adapters/dice_pool_demo.py` — the one adapter that ships in Gate-0, wrapping
  `skills/valoria-dice-model/valoria_dice.py`'s **public** API (`roll_pool`, `classify_outcome` — added
  to that module so this package no longer depends on its underscore-prefixed internals). Chosen
  deliberately as the simplest, lowest-risk demo. Distinguishes canon-verified parameters (TN, Ob — real
  `params/core.md` table values, checked live via `verify_citation`) from declared test-scenario values
  (pool size, which is character-build-dependent and has no single fixed canonical value) — every
  parameter carries a provenance string, and `Harness.run()` raises if any doesn't. Also surfaces a real
  finding: dice-pool resolution has **no row of its own** in `references/module_contracts.yaml` (grepped
  across all 27 module names) — genuinely cross-cutting substrate, not a gap in this prototype.

## Run it

```
python3 -m tools.sim_harness.harness --trials 200 --seed 0
python3 -m tools.sim_harness.harness --trials 10 --seed 0 --no-registry   # forces DEGENERATE_DISTRIBUTION on the two real events
python3 -m tools.sim_harness.harness --adapter bogus --no-registry        # lists real available adapter names instead of a bare crash
```

The shipped adapter's `verdict` is **PARTIAL by default**, not PASS — its `stub_probe` decision point
deliberately raises `NotImplementedError` every run, by design, so the STUB_HIT path is exercised on
every invocation rather than only when someone thinks to test it. That is the intended, honest signal
for a harness whose real purpose is testing incomplete work: a subsystem with a real stub in it should
report PARTIAL, not a false PASS.

`--no-registry` skips the `audit_registry.jsonl` append (use for local experimentation). Trace files
write to `results/` (gitignored, same convention as `sim/results/`).

## What this is not

- Not a coverage claim over any subsystem beyond the one demo adapter.
- Not wired into CI — see the design doc §7 for the proposed report-only → blocking ratchet.
- Not a replacement for `sim/tests/`'s deterministic regression goldens, `contract_adjudicator.py`'s
  fixture suite, or `combat_sim.py`. It's built to absorb the latter two as adapters in later waves
  (§6/§8 of the design doc), not to compete with any of them.
- Not a mechanical guarantee that a declared tier (minor/medium/major) is the *correct* one — `depth.py`
  enforces that every tier choice is justified (non-empty, recorded), not that the justification is
  good. Catching a self-serving tier downgrade is still a review-time responsibility. Said plainly here
  because the first cut of this code implied otherwise without actually enforcing it.

## Adding a new adapter

Implement `Adapter` (see `adapter.py`'s docstrings and `adapters/dice_pool_demo.py` as the worked
example): declare `contract_module` (a real `references/module_contracts.yaml` key, or `None` with a
one-line justification if the subsystem is genuinely cross-cutting), `canon_row` (a `CURRENT.md` bold
row-label substring), `resolve_params()` (returns `(params, provenance)` — every param key needs a
provenance entry, canon-verified or an explicit "test-scenario, not canon-derived" note), `decision_points()`,
and `run_once()` (may raise `NotImplementedError` for a genuine stub branch — the harness catches it).

Then add **one import line** to `adapters/__init__.py` so `@register_adapter(...)` actually runs at
import time — that is the only file outside the adapter's own that needs touching. `harness.py` itself
never needs an edit to add an adapter; this is enforced by construction (the CLI's `--adapter` dispatch
reads `ADAPTER_REGISTRY`, not a hardcoded name), not just documented.

Do not add a new top-level interface shape — if the `Adapter` protocol doesn't fit a subsystem, that's a
finding to raise against the design doc, not a reason to route around it.
