# `tools/sim_harness/` — Gate-0 prototype

**Status: PROPOSED, ED-IN-0038.** Not wired into CI or local hooks. This is a proof of the
architecture described in
`designs/audit/2026-07-12-simulation-test-harness-methodology/simulation_test_harness_methodology_v1.md`
— read that doc first for the full methodology, the depth-tier rubric, the triage-flag taxonomy, and
the real rollout order (§8). This README is usage notes only.

## What ships here

- `canon_resolver.py` — resolves a subsystem's live canonical head from `CURRENT.md`, never fabricates.
- `depth.py` — the 1 (minor) / 2 (medium) / 3 (major) tier policy: minimum trial count and
  degenerate-distribution threshold per tier.
- `triage.py` — the mandatory triage-flag taxonomy and verdict rule (a flag can never be silently
  swallowed into a PASS).
- `adapter.py` — the `Adapter` protocol every subsystem's "test module" implements. The harness core
  has zero subsystem-specific knowledge; only an adapter does.
- `trace_logger.py` — per-event trace + a **live** (not backfilled) `references/audit_registry.jsonl`
  append, via the existing `tools/audit_registry.append_record`.
- `harness.py` — orchestrator + CLI.
- `adapters/dice_pool_demo.py` — the one adapter that ships in Gate-0, wrapping
  `skills/valoria-dice-model/valoria_dice.py`. Chosen deliberately as the simplest, lowest-risk demo —
  see its docstring. It also surfaces a real finding: dice-pool resolution has **no row of its own** in
  `references/module_contracts.yaml` (confirmed by grep across all 27 module names) — genuinely
  cross-cutting substrate, not a gap in this prototype.

## Run it

```
python3 -m tools.sim_harness.harness --trials 200 --seed 0
python3 -m tools.sim_harness.harness --trials 10 --seed 0 --no-registry   # forces a DEGENERATE_DISTRIBUTION flag (n too low)
```

`--no-registry` skips the `audit_registry.jsonl` append (use for local experimentation). Trace files
write to `results/` (gitignored, same convention as `sim/results/`).

## What this is not

- Not a coverage claim over any subsystem beyond the one demo adapter.
- Not wired into CI — see the design doc §7 for the proposed report-only → blocking ratchet.
- Not a replacement for `sim/tests/`'s deterministic regression goldens, `contract_adjudicator.py`'s
  fixture suite, or `combat_sim.py`. It's built to absorb the latter two as adapters in later waves
  (§6/§8 of the design doc), not to compete with any of them.

## Adding a new adapter

Implement `Adapter` (see `adapter.py`'s docstrings and `adapters/dice_pool_demo.py` as the worked
example): declare `contract_module` (a real `references/module_contracts.yaml` key, or `None` with a
one-line justification if the subsystem is genuinely cross-cutting), `canon_row` (a `CURRENT.md` bold
row-label substring), `resolve_params()`, `decision_points()`, and `run_once()`. Do not add a new
top-level interface shape — if the `Adapter` protocol doesn't fit a subsystem, that's a finding to raise
against this doc, not a reason to route around it.
