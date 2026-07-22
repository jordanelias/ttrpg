# Geometric contact + weapon-reach — de-gridding the field engine (proposal, 2026-07-22)

**Status: PROPOSED** (Jordan design, live). Captures the design that resolves the integer-collision /
"cells have no contact surface" problem surfaced during the ED-MB-0011 field-based stress test.

## Confirmed current state (traced, not assumed)

- **Cells already have a size.** `CELL_RADIUS = 0.5` (units.py:59-62, "per-cell physical-body radius,"
  = half the `COL_WIDTH = 1.0` lattice pitch). A cell is a disc of radius 0.5 → diameter 1.0.
- **The contact DECISION is already geometric float — no integer.** Live path `_find_contacts_standoff`
  (contact.py:291): `math.hypot(ar-br, ac-bc) <= standoff_from_reach(ra, rb)`, with
  `standoff = (CELL_RADIUS + reach_a) + (CELL_RADIUS + reach_b)` (units.py:65-68). Two short-reach cells
  engage at centre-distance ≤ 2.0. This is surface-to-surface + reach, exactly "do their bodies meet."
- **Integer collision survives in only two vestigial places that IGNORE that geometry:**
  1. **Contention** — `resolve_cross_side_contention` (contact.py:183-185): "same space" is
     `set(int(round)-keys) & set(int(round)-keys)` — *exact integer-cell equality*, not surface overlap.
     This is the key-collision: at `.1` two floats never share an integer key, so it would never fire.
  2. **Engaged-cell recording** (contact.py:292-293): `int(round)` cell-ids, consumed only for
     casualty **column** matching + `_lanchester_strength` frontage (`set(c for r,c)`).
- **Depth is NOT affected by the snap** (Stage-0 trace): `_formation_depth`/`_subunit_depth` read the
  static pattern; `_defender_depth`/`build_column_grid` read `col_grid` (legacy `cell_offsets_c`), keyed
  by column. No mechanic counts distinct *snapped rows*. So the earlier "depth-of-two collapse" is
  cosmetic in `cells()` output; the mechanically-live snap axis is **columns (frontage)**, via contention
  + recording.

## Proposal

### P1 — standardized cell size (formalize what exists)
Keep `CELL_RADIUS = 0.5` as the canonical nominal cell body radius (diameter 1.0 = one file pitch). Make
it the single source for every "do cells occupy the same/adjacent space" test (today only the contact
decision uses it; contention does not).

### P2 — per-WEAPON melee reach (replaces coarse troop-type reach for melee)
Each unit has a melee weapon with a reach, unless it is a pure ranged unit (and a ranged unit MAY also
carry a melee weapon). Melee reach (lattice units, added to `CELL_RADIUS` in `standoff`):

| weapon class | reach |
|---|---|
| non-pole melee (sword/axe/mace) | **0.1** |
| pole-weapon (spear/halberd/glaive) | **0.2** |
| pike | **0.3** |
| ranged | its projectile range (existing volley band) |

These are finer and weapon-based, vs today's troop-type `REACH_SHORT=0.5 / REACH_LONG=1.5`. Effect:
two non-pole melee cells engage at centre-distance ≤ `2·0.5 + 0.1 + 0.1 = 1.2` (vs 2.0 today); a pike
line reaches first (`2·0.5 + 0.3 + 0.3 = 1.6`) — the historical pike-vs-sword reach advantage emerges
from geometry, not a flat bonus.

### P3 — geometric contention (delete the integer collision)
Replace the exact integer-cell `contested = set(a_keys) & set(b_keys)` with **surface overlap on floats**:
two opposing cells contend for the same ground when `hypot(Δr, Δc) < 2·CELL_RADIUS` (their bodies
overlap). Movement priority (speed) then resolves who holds the ground — same rule as today, but the
"same space" predicate is geometric, so it works at any resolution (no integer key needed). This is the
change that lets positions be true floats without the key-collision failing silently.

### P4 — engaged-cell recording on the geometric set
The engaged-cell set (for casualty columns + Lanchester frontage) is recorded from the float-distance
contact already computed, at whatever column resolution is ratified (float file-bins, not `int(round)`).

## Trace / adversarial notes (to verify during implementation)
- **Frontage (Lanchester `set(c for r,c)`)**: finer column bins → potentially more distinct engaged
  columns → higher frontage → **balance shift** (DG-6-gated). Must A/B and disclose, not tune.
- **Contention firing**: geometric overlap must fire at least as often as the old integer collision, or
  movement-priority displacement changes. Adversarially verify contention still resolves (determinism).
- **Casualty conservation**: `cell==hp` must hold under the new recording (the Stage-0 probe showed the
  `.1` cells() variant already conserves — good sign).
- **Depth mechanics**: unaffected (read pattern/col_grid), so charge-absorption/stamina are stable — the
  change is isolated to contact/contention/frontage, which is the intended surface.
- **Reach values 0.1/0.2/0.3 vs CELL_RADIUS 0.5**: with CELL_RADIUS dominating, weapon reach is a small
  differentiator — confirm it is not swamped (i.e. that pike-vs-sword actually reaches first in practice).
- **Wired engine** (`systems/mass_battle/sim`): integer-grid throughout, no CELL_RADIUS/standoff — it
  cannot host this model without the same geometric-contact port; that is the reconciliation.

## Not yet executed
This is the design map. Implementation is staged (weapon-reach table → geometric contention → geometric
recording → verify + disclose gauge shift), each stage traced all-directions with an adversarial pass,
per the working method.
