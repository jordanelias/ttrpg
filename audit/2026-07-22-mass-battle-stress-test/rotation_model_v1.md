# Rotation Model — two-tier troop rotation + recovery (Jordan directive, 2026-07-23)

Parse-back + build plan for Jordan's rotation directive, plus the foundational primitive landed
(ED-MB-0028). Companion to `honest_gauge_readout.md` (the scale/depth findings that motivate it) and
`fiat_register_v1.md`.

## The directive, parsed

> "(1) subunits are comprised of cells. as cells lose troops, unengaged troops from other cells try to
> fill them in to keep those engaged cells at their prescribed density. eventually the subunit cell
> coverage shrinks as troop minimums aren't met in a cell. this is the internal subunit version of
> rotating troops.
> (2) subunits, however, are troop types and carry morale and discipline and exhaustion. subunits can
> rotate with other subunits where there is a blended relational cell exchange over ticks where one
> subunit eventually disperses in a cascading rotate-by-cell mechanic so that the subunits basically
> aggregate/mix together then separate at cellular level so that you can rotate out a subunit.
> not all troop losses are necessarily deaths — abstractly it could be injuries or troops who may have
> been fleeing/withdrawing, so there needs to be some ability for a subunit to recover troop count to
> some degree to make this rotation explicit as worthwhile in addition to the full combat strength of
> the substituting unit."

Three coupled mechanics, bottom-up:

| # | Mechanic | Scope | What it models |
|---|----------|-------|----------------|
| **T1** | **Intra-subunit cell backfill + coverage shrink** | within one subunit | Engaged (front) cells stay at prescribed density by pulling troops forward from unengaged (rear) cells; when troop minimums can't be met, cell coverage shrinks. The *internal* rotation — ranks stepping up. |
| **T2** | **Inter-subunit rotation** | between two subunits of one army | A fresh subunit relieves a spent one at the front via a **blended relational cell exchange over ticks** — the two aggregate/mix at the cell level, then separate, so one rotates out. The manipular/*triplex acies* line relief. |
| **T3** | **Troop-count recovery** | one rotated-out subunit | Not all losses are deaths (injuries, stragglers, momentary flight). A subunit out of contact recovers *some* troop count, so rotating it out (and later back) is worthwhile beyond just fielding the fresh substitute. |

## State of the engine before this work

- **T1:** partial and *abstract only*. Depth already damps fatigue (`PC_DEPTH_ROTATE`) and rests genuine
  reserves (`update_stamina`), and `_pair_engaged_troops` weights the exchange by the actual troops in
  the engaged front cells — so front density already matters to combat. But casualties simply *deplete*
  the engaged front cells; there was **no literal backfill** (`PC_REFILL_FLOOR` is referenced in comments
  but never wired) and **no coverage shrink**. The reserve was a stamina abstraction, not literal troops
  stepping up.
- **T2:** absent. The Reserve rule (ED-MB-0023) is *bench-then-commit*, not a blended pass-through
  rotation. No cell-level mixing/relief exists.
- **T3:** absent. `run_battle` is explicit: "HP does NOT recover between turns (casualties are permanent
  within a battle)." Between-turn recovery restores stamina/morale, never troop count.

## What landed: T1 Phase 1a — `Subunit.close_ranks()` (ED-MB-0028)

The single-owner primitive the rest composes on. After casualties each tick (gated, simultaneous —
both units' casualties applied first), each subunit reflows its **living** troops front-rank-first
(`orig_r` ascending; r=0 = engaged edge) toward each cell's **spawn prescribed density** (`_cell_target`),
depleting the rear. Net: a **deep** formation holds full front-cell density — and thus full front combat
pool — until its depth is spent; a **shallow** one thins at the front immediately.

- **Conservation** exact (only casualties, applied elsewhere, reduce the total).
- **Relational, not absolute:** troops close toward the front rather than leaving sub-density holes
  ("troops will always be as close together as possible"). Emptied cells keep their key at 0.0 — every
  `iter_cells` consumer already gates on `troops>0`, so functional coverage shrinks from the rear
  **without** mutating the cell set this pass (literal cell dissolution + lateral close-up = Phase 1b).
- **Gated** `PC_CLOSE_RANKS` (default OFF → `cell_troops` untouched, byte-exact: bat.py 4 modes EXIT=0).
- **Verified:** front rank knocked to 16.7/cell → refilled to 100 from the rear (rear absorbs the loss),
  conservation 1250→1250. `tests/valoria/test_close_ranks.py` (7 tests).
- **Effect** (`close_ranks_probe.py`, equal troops+density, aspect varies): DEEP(3×4) vs SEMI(6×2)
  **81% → 94%** with close-ranks ON — the reserve now sustains the front literally, sharpening depth's
  value; mirror stays fair (both sides run it → no bias).

## Remaining build order (bottom-up, each gated + adversarially reviewed)

1. **T1 Phase 1b — literal coverage shrink + lateral close-up.** Dissolve sub-`CELL_FLOOR` cells, merge
   remnants into neighbours, and slide columns in when a whole column dies (the "shrink not holes"
   lifecycle, task #29). Higher blast radius (mutates the cell set mid-battle: facing vectors, node
   cohesion, col grid) → its own increment with a targeted regression.
2. **T2 — inter-subunit rotation.** A relief order that, over several ticks, blends two same-army
   subunits' cells at the shared boundary (cascading rotate-by-cell), transfers the front, then separates
   — the spent subunit rotates to the rear. Composes on T1's cell-reflow primitive.
3. **T3 — troop-count recovery.** A subunit out of contact recovers a bounded fraction of *non-death*
   losses over time (injuries/stragglers/rally), so the rotate-out→recover→rotate-in cycle is worthwhile.
   Interacts with the DG-2 yielding/rally work; must not let a unit heal back to full (cap to a fraction
   of losses, decaying).

**North star unchanged:** grounded emergent primitives, calibrated to independent history, never to the
gauge rows; every new mechanic gated OFF until measured and (where it changes canon-adjacent behavior)
ratified.
