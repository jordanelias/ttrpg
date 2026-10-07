---
description: Establish currency before touching the tree — which head is canonical, and what is pending.
---

CLAUDE.md §1's priority order, as commands. Run this **before the first edit**.

1. **`CURRENT.md`** — the index of the live canonical head per subsystem, and the authority
   whenever you are unsure a doc is current. Its stamp: `grep -n '_Last reconciled' CURRENT.md`.

2. **`HANDOFF.md` and your lane's file.** Nothing reads these automatically.
   `sed -n '1,60p' HANDOFF.md` then `registers/handoffs/HANDOFF_<LANE>.md` for your lane
   (`MB PC FI SC FA WR IN GO SE`). Root `HANDOFF.md` carries only cross-cutting items.

3. **The subsystem head and its `## Status:` line** — resolve the head through `CURRENT.md`, never
   by a filename suffix.

4. **Verify the pins rather than trusting them by eye.** `python tools/freshness_gate.py` computes
   each doc's local git blob OID against the `canonical_sha__*` pins in
   `references/canonical_sources.yaml`. Blocking in CI, report-only locally.

5. **Where the milestone actually stands**, if that is the question — the only reading §0.2
   accepts:
   - `python tools/m1_acceptance.py --summary` (its "all junctures execute" row is DOC-DERIVED —
     bookkeeping, not evidence)
   - `python -m engine.season.harness.register --requirements` — THE NINE

**Ignore for currency:** `README.md`. There is nothing to resume from. An old path resolves through
`references/restructure_ledger.md` via `python tools/pathres.py` — but for "is this exact file
retired", ask `load_alias_map()` for an exact row: `pathres.resolve()` matches directory
prefixes and returns FORKED for any invented filename under a forked directory.

**Do not** read `.designs/` or `.audit/` as authority (§0.05, §1).
