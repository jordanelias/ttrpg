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

## Held for Jordan (nothing here ratifies on merge)

Per CLAUDE.md §2's ED-1094 exception, one item in the parent proposal is **held back loudly**: the
**decision policy** (precedence order among canon / historical precedent / physical factuality,
the operational test for "emergent", and the deliberate-fantasy exception clause). It is the one
artifact only Jordan can author, agents can only draft it for correction, and **merging this
pointer does not adopt any precedence order.** The scaffolding in this PR is deliberately inert
with respect to that decision — it measures and reports; it rules nothing.
