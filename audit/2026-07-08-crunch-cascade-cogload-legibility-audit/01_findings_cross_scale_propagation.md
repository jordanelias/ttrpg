# Cross-Scale Propagation / Aggregation Architecture — Findings (adversarially verified)

**Canonical heads:** `designs/architecture/propagation_spec_v1.md` (CANONICAL, "TERMINATION-ONLY —
cross-tick convergence NOT proven") + `holonic_container_doctrine_v1.md` (CANONICAL).

This lane doesn't have player trackers; it audits the structural primitives (Key,
aggregate-up/distribute-down transforms, cascade-depth counters) that let state cascade between
scales — the place a badly-designed cascade would be structurally invisible to any single-
subsystem audit.

## 1. Structural primitive inventory

Key (universal event record, bidirectional); KEY_LOG/`on_key_emitted` (7-step pipeline, Step 4/5
amended and RATIFIED 2026-07-07); Aggregate-Up (Domain Echo — never writes an aggregate directly,
routes through a deferred settlement-locus write or a decaying Key-ledger modifier); Distribute-
Down (one Key, N-entry `targets[]`, not N re-entrant emissions — confirmed fan-out is not conflated
with cascade depth); `cascade_depth` (proven to terminate under caller-supplied caps with **no
default and no cited canonical source** — confirmed in code); `sub_step_index` (proven total
order, explicitly not a cascade-depth meter).

**Module-contract count, independently recounted and corrected:** `doc: null` — confirmed 10/27;
`[ASSUMPTION]`-grade resolver — confirmed 11/27 (both match CLAUDE.md's cited figures exactly).
**Correction:** the overlap between the two sets is **5 modules, not 4** (`npc_memory`,
`domain_actions`, `settlement_economy`, `faction_politics`, `scenario_authoring` all appear in
both lists), making the union **16/27 (~59%), not 17/27 (~63%)** as originally computed — a minor
arithmetic slip that doesn't touch the headline 10/27 and 11/27 figures.

## 2. Interaction chain map — three named cascade paths

- **Domain Echo (up):** scene → settlement-locus deferred write (at ACCOUNTING_BOUNDARY) →
  `AGGREGATE_s()` re-derives faction stat on next read. 3 hops, 1 tick.
- **peninsular_strain → npc_behavior/settlement (down):** one Key, many-entry `targets[]` for all
  affected territories — not one Key per territory. 8 of the down-seams (D.4) remain unclosed/
  unsequenced.
- **National-event-modifier down-half (D.5):** a faction's modifier emitted as a single Key whose
  `targets[]` also reaches N constituent settlements, closing into a re-derivation loop the next
  tick — **this is the exact cascade the D.6 double-count risk concerns.**

## 3. Cascade check — the core finding, confirmed verbatim throughout

The spec proves exactly two things and is explicit it proves no more: **Theorem A** (within any
single tick, cascade depth capped at 1-down+1-up) and **Theorem B** (within any single re-entrant
drain, depth strictly increases and is capped, so any one drain halts). **Neither theorem
addresses cross-tick recurrence** — the "inter-scale macro loop" is bounded only by the
campaign's outer season loop, not by proven decay/convergence. Every quote checked against the
source is exact and in-context: *"It can persist at bounded, non-decaying amplitude for the
entire campaign"* and *"the guarantee is TERMINATION-ONLY, not convergence. Do not oversell it."*
Magnitude **is** proven bounded (every hop individually capped) — the concrete risk is a
**persistent, non-damping oscillation**, not unbounded growth.

**`decay()` is entirely unspecified** — not just an unbacked constant but a load-bearing function
with zero cited form, no calibration, and no functional shape. Genuine convergence requires it to
be strictly contractive; until specified, the spec's own text says not to oversell the guarantee.

**D.6 double-count is the spec's own self-identified "confirmed driver of non-convergence,"
explicitly not resolved** — whether the down-targeted settlement `stat_deltas` are disjoint from
what `AGGREGATE_s()` reads is an open ruling with no default; getting it wrong means the same
scene outcome counts twice.

**ORD-3 self-contradiction, the single strongest and most independently re-verified finding in
this lane:** the propagation spec's own determinism proof depends on `compute_observers` being
order-preserving, but `key_substrate_v30.md`'s own reference pseudocode for `compute_observers`
literally returns a bare Python `set()` — the exact pattern the spec's own ORD-2 rule forbids. The
spec names this as a live violation in its own dependency and cannot fix it itself (out of its
authority). Confirmed by direct code inspection, verbatim.

**Cap constants (OF-CAP)** are confirmed in code to be caller-supplied required ints with no
hardcoded default — the termination guarantee holds only *given some cap*, not for any specific
validated one.

## 4. Cognitive load (engine/designer-facing)

A module author wiring a new subsystem into this architecture must reason about at least six
distinct rule families (ordering discipline, aggregate-up discipline, distribute-down discipline,
termination/re-entrancy mechanics, RNG threading, save/replay determinism preconditions) — a
substantial surface, and the spec is unusually honest that it is not yet fully self-consistent
(the ORD-3 contradiction above). The spec is legible for the specific cases it works through
(Domain Echo, peninsular_strain, national-event-modifier) and silent on the rest — a module
author for, say, `scene_timer` or `audit` (both `doc: null`) has no worked template to follow.
`engine_clock`'s `doc: null` is confirmed to be a pure editorial-bookkeeping gap (the spec already
supplies a complete worked entry for it; it's pending a separate ED to flip the flag), not a
content gap.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — D.6 double-count ruling absence.** Confirmed, HIGH PRIORITY per the spec's own text,
  still unresolved.
- **P1 — `decay()` is a load-bearing unknown with zero shape.** Confirmed; blocks any Godot-port
  claim that "the up/down loop settles."
- **P1 — ORD-3 self-contradiction in cited canon.** Confirmed as the strongest finding in this
  lane — a live, verbatim contradiction between two canonical docs' own claims about each other.
- **P2 — `causes[]` field overload** (runtime re-entrancy parent vs. authored provenance) — the
  spec itself flags this as low-severity residual ambiguity; confirmed genuine but minor.
- **P2 — Holonic doctrine's "wrapper" vocabulary is used consistently but not re-stated at the
  point of use** by the propagation spec (which speaks entirely in Keys/targets/transforms terms)
  — not drift, but requires the reader to infer the mapping.
- **P3 — ORD-4's module-global-queue issue is a straightforward code fix mislabeled as an open
  design flag** alongside genuinely hard questions (D.6, decay()) — risk of misprioritization, not
  of incorrectness.
- **P3 — `engine_clock`'s `doc: null` non-flip is a pure editorial-process gap**, not a content
  gap — CLAUDE.md's "~37% of contracts are not implementable specs" framing could be misread as
  implying engine_clock has no real spec, when it does.

## Recency check

The critic pass checked HANDOFF_IN.md and ledger entries through 2026-07-08 and found **no open
flag from this lane has since been resolved** — one adjacent item did land same-day (ED-IN-0028,
wiring an echo-transport seam described as "unwired" in the Social Contest lane's findings — see
that file), but it does not touch D.6, decay(), OF-CAP, RNG-MODEL-COLLISION, ORD-3, or ORD-4,
which all remain open exactly as described here.
