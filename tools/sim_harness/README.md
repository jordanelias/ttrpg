# `tools/sim_harness/` — Gate-0 prototype

**Status: PROPOSED, ED-IN-0038.** Not wired into CI or local hooks. This is a proof of the
architecture described in
`designs/audit/2026-07-12-simulation-test-harness-methodology/simulation_test_harness_methodology_v1.md`
— read that doc first for the full methodology, the depth-tier rubric, the triage-flag taxonomy, and
the real rollout order (§8). This README is usage notes only.

**Revision note:** this package has been through six rounds of adversarial review and deliberate
stress-testing (not just one) — see the per-file docstrings for what changed and why in each; every
corrected claim states the failure it replaces, not just the new behavior, precisely because this note
itself went stale once already (round 1's note described only round 1's fix and was never updated
through rounds 2–5, which is a finding from round 6 in its own right). Headlines, roughly in order found:
(1) an uncaught exception from a stub subsystem crashed the whole run before any trace/registry write —
`Harness.run()` now catches it, and the shipped demo includes a synthetic `stub_probe` decision point
that exercises the path on every invocation, not just in theory; (2) two more rounds of stress-testing
found a same-day registry-id collision, a crash on missing/malformed `CURRENT.md` or
`module_contracts.yaml`, an invalid-tier value sailing through construction to crash deep inside a run,
and a triage-flag flood at scale (10,000 duplicate flags from one systematic classification bug); (3)
round 6 (max effort) found that **triage flags were never actually written into the persisted trace
file** — only printed to console and rolled up in the registry summary — plus an uncaught exception path
in `resolve_params()`/the provenance check, a `UnicodeDecodeError` gap in three separate `except OSError`
guards (fixed by extracting one shared `read_text_or_gap` helper), `--trials 0` silently skipping the
stub-capture demonstration entirely, and `DEGENERATE_DISTRIBUTION` misreporting a broken adapter's
garbage output as if it were a real, if skewed, distribution.

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
- `trace_logger.py` — per-event trace **and every triage flag** (deterministic JSON, matching
  `sim/substrate/keys.py`'s `KeyLog` serialization convention — but not its schema/validation, see the
  module docstring for the precise boundary) + a **live** (not backfilled) `references/audit_registry.jsonl`
  append. Both durable writes are guarded in `main()` — a disk-full or permissions failure prints a
  warning instead of discarding the console-visible summary of a run that already completed.
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

`--trials` must be positive: 0 (or negative) trials means every decision point's loop runs zero
iterations, so no stub/crash path ever fires — `Harness.run()` rejects this with `ValueError` rather than
silently producing a plausible-looking verdict for the wrong reason (found live: `--trials 0` reported
the same `PARTIAL` headline as a real run, but with zero `STUB_HIT` flags, for a completely different and
misleading reason).

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
row-label substring, or `None` — see "Provisional adapters" below), `resolve_params()` (returns
`(params, provenance)` — every param key needs a provenance entry: canon-verified, an explicit
"test-scenario, not canon-derived" note, or an explicit "PROVISIONAL: ..." note), `decision_points()`,
and `run_once()` (may raise `NotImplementedError` for a genuine stub branch — the harness catches it).

Then add **one import line** to `adapters/__init__.py` so `@register_adapter(...)` actually runs at
import time — that is the only file outside the adapter's own that needs touching. `harness.py` itself
never needs an edit to add an adapter; this is enforced by construction (the CLI's `--adapter` dispatch
reads `ADAPTER_REGISTRY`, not a hardcoded name), not just documented.

## Provisional adapters — testing pre-canonical mechanics

The Gate-0 demo (`dice_pool_demo.py`) only proves the harness against already-ratified canon
(`params/core.md`, via `verify_citation`). That's half the original ask — the other half was explicitly
"have it so that we can insert/swap in/plug in provisional test code" — and it was NOT concretely proven
by Gate-0: `canon_row` was a required `str` with no `None`-handling anywhere in `harness.py`, so an
adapter for a proposed-but-not-yet-ratified mechanic would have crashed on its first resolver call.

`canon_row: str | None = None` now has a real, first-class path (see `adapter.py`'s docstring for the
full reasoning). `contract_module` and `canon_row` are two **independent** nullable axes — don't conflate
them:

| | `contract_module` | `canon_row` |
|---|---|---|
| Answers | Is this bound to a `module_contracts.yaml` IN→resolver→OUT contract? | Is this bound to a live `CURRENT.md` canonical head at all? |
| `None` means | Genuinely cross-cutting substrate (e.g. dice math — canon-cited, but no module-contract row) | Deliberately testing provisional/pre-canonical work — a proposed mechanic, possibly with a filed `ED-<LANE>-NNNN`, that hasn't been ratified into a `CURRENT.md` row yet |

A provisional adapter (sketch, not a shipped file — write one when there's a real proposed mechanic to
test):

```python
@register_adapter("proposed_faction_bonus")
class ProposedFactionBonusAdapter(Adapter):
    contract_module = None       # or a real module_contracts.yaml key if one exists
    canon_row = None             # no CURRENT.md row yet — this is what makes it provisional
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver):
        params = {"proposed_bonus": 2}
        provenance = {
            "proposed_bonus": "PROVISIONAL: designs/audit/2026-xx-xx-some-proposal/, "
                               "ED-FA-9999 filed, not yet ratified",
        }
        return params, provenance

    def decision_points(self):
        return [DecisionPoint(
            name="proposed_check", default_tier=Tier.MINOR, branches=["pass", "fail"],
            justification="smoke-testing a proposed mechanic ahead of ratification",
        )]

    def run_once(self, rng, params, dp):
        ...
```

Every event this produces carries `canon_status: "provisional"` in the persisted trace (verified
adapters carry `"verified"`) — a reader or future tooling can never mistake a provisional run's numbers
for canon-verified ones just by scanning an empty `citations` list, which was ambiguous before this
field existed (a verified row citing zero docs and a provisional adapter with no row at all used to look
identical). The harness also logs an explicit `canon_binding` note (visible in the trace, distinct from
a silent skip) whenever `canon_row is None`.

Do not add a new top-level interface shape — if the `Adapter` protocol doesn't fit a subsystem, that's a
finding to raise against the design doc, not a reason to route around it.
