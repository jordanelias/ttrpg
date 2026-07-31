# Pointer — M1 program scaffolding (IN lane)

**target:** this file — the program has no separate `proposals/` doc, deliberately. Writing one
would have pushed `proposals.open` 20 → 21 and **regressed this program's own scope ceiling on the
commit that introduced it.** The ratchet caught its author first; obeying it rather than raising
the ceiling is the whole point, and the pointer already carries the scope, so a second document
would also have duplicated it (CLAUDE.md §8, every rule lives once).
**lane:** IN (cross-cutting: governance + dashboard + acceptance gating) · **ED:** ED-IN-0112 (ledger `open`, `needs_jordan: true` — the decision policy is Jordan's to author)
**liveness:** LIVE — the active scaffolding program for M1 ("one playable season")
**scope:** the scope ratchet `tools/scope_ratchet.py` + `registers/scope_baseline.yaml`; the season
acceptance gate `tools/m1_acceptance.py`; the dashboard program panel in `tools/dashboard_data.py`
(`build_program`) and `dashboard/index.html` (`renderProgram`); the pytest pins
`tests/valoria/test_scope_ratchet.py`. Downstream, and NOT yet claimed by this pointer because
they are unbuilt: the decision policy document, the derivation engine, and the season loop itself.

> ⚠️ **Claims two shared surfaces.** `tools/dashboard_data.py` and `dashboard/index.html` are
> edited by any session that adds a card. This program adds exactly one section (`program`) and one
> renderer (`renderProgram`) and touches nothing else in either file — a concurrent card addition
> should merge cleanly, but sequence if the other change restructures `build_all()`.

> ⚠️ **Deliberately NOT claiming `registers/review_baseline.yaml`.** The scope ratchet is a
> SEPARATE instrument from the technical-debt ratchet, with its own baseline file, because scope
> growth is not a quality regression and `review_core`'s signals cannot see it. Do not merge the
> two registers without an explicit ruling — the split is the design, not an oversight.

## What this program is for

M1 has sat at **0 of 7 junctures** while the corpus grew. Nothing in the repository surfaced that
fact as a *program* signal: every existing card describes the state of the corpus, none answers
"is the goal moving?". This program adds the missing surface and the missing stopping rule, and
defines "fully simulatable season" as five falsifiable rows so the phrase cannot expand without
someone noticing.

## Ratified 2026-07-31 (PR #277)

**RATIFIED on merge** per ED-1094: the scope ratchet + its raise guard + the G13 activity control,
the season acceptance gate, the dashboard program panel, `valoria_local.py --ci`, and the `-n auto`
shipping-gate parallelisation (387s -> 180.7s in CI, 2.15x, collection byte-identical).

**Wired, not merely built.** An adversarial critic found the ratchet had no executing caller except
the test suite — an inert instrument. It is now a **report-only** row in `tools/valoria_local.py`'s
check table (which runs pre-commit *and* in CI's `generation-consistency-check`) and is registered in
`references/ci_checks_registry.yaml`. Deliberately **not** a new CI job: the repo has 34, and adding
a 35th to report one number would be the defect the instrument exists to measure.

## Still held for Jordan — carried forward as ED-IN-0113

The **decision policy** never ratified and does not ratify here: the precedence order among canon /
historical precedent / physical factuality, the operational test for "emergent", and the
deliberate-fantasy exception clause. A **134-ruling precedent mine** is attached to ED-IN-0113 and
shows **mechanical** canon is demonstrably subordinate to measured, physically-grounded engine
behaviour (ED-899 / ED-900 / ED-901 / ED-PC-0005) — but whether **metaphysical** canon shares that
tier is **unestablished**, and inventing it would be the fabrication `NO DEFAULT` forbids. Five
unfixed adversarial findings ride the same entry.
