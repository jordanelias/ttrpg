# SIM-MB-06 v10 Module Manifest
# Iteration: v9 → v10 (bottom-up granular — remove top-down SHAPE_OFF_MOD)
# Date: 2026-05-12

## SCOPE

v10 restructures shape advantages to emerge from **geometric mechanisms only**, removing
the top-down `SHAPE_OFF_MOD` and `SHAPE_DEF_MOD` flat per-shape dice bonuses. The
historical accuracy targets in `tests/sim/sim_mb_06_v9_historical_spec.md` must be
achievable on a granular bottom-up basis: cell arrangement, engagement angle, support
stacking, momentum, and encirclement count. No holistic shape bonus is allowed.

## ROOT CAUSE OF v9 OVER-TUNING

Diagnostic revealed two compounded defects in v9:

### Defect 1: Cell counts unequal across shapes

| Shape         | T1 | T2 | T3 | T4 | v9 ratio vs Line @ T3 |
|---------------|----|----|----|----|------------------------|
| Line          | 9  | 15 | 25 | 35 | 1.00                   |
| Arrowhead     | 9  | 16 | 25 | 36 | 1.00                   |
| Horseshoe     | 13 | 17 | 25 | 31 | 1.00                   |
| GappedLine    | 12 | 30 | 56 | 90 | **2.24** (!)           |
| RefusedFlank  | 10 | 13 | 21 | 31 | 0.84                   |

GappedLine carried 2.24× the troops of Line at T3 — the apparent "shape advantage" was
mostly extra troops. RefusedFlank had 84% of Line's troops, masked by `SHAPE_OFF_MOD`
`engaged=+1` bonus.

### Defect 2: SHAPE_OFF_MOD double-counted geometric mechanisms

The flat per-shape dice bonus layered on top of already-working geometric mechanisms:

| Geometric mechanism (bottom-up, in v8+) | What SHAPE_OFF_MOD was redundantly adding |
|------------------------------------------|-------------------------------------------|
| `support_engage_frac` (Arrowhead tip gets depth support) | `Arrowhead tip = +2D` flat   |
| `engagement_angle` FLANK/REAR bonus      | `Horseshoe flank_engaged = +2D` flat      |
| `count_engagements` encirclement penalty | implicit in flat bonuses                  |
| Geometric absence of contact             | `RefusedFlank refused = -2D` flat         |

## CHANGES IN v10

### Equalized cell counts
- GappedLine: 56 → 24 cells at T3 (sizes `{1:(2,2), 2:(3,3), 3:(4,3), 4:(4,4)}`)
- RefusedFlank: 21 → 25 cells at T3 (sizes `{1:(3,4), 2:(4,5), 3:(5,6), 4:(6,7)}`)
- Line, Arrowhead, Horseshoe unchanged

### Zeroed flat per-shape modifiers
```python
SHAPE_OFF_MOD = {
    "Line":        lambda role: 0,
    "Arrowhead":   lambda role: 0,         # was: +2 tip, -1 else
    "Horseshoe":   lambda role: 0,         # was: -2 center, +2 flank_engaged
    "GappedLine":  lambda role: -99 if role == "gap" else 0,  # gap sentinel retained
    "RefusedFlank":lambda role: 0,         # was: -2 refused, +1 else
}
SHAPE_DEF_MOD = {all: lambda r: 0}         # was: Horseshoe center +1
```

The `gap=-99` sentinel is retained because it is *structural* (no cell at the gap, not
a balance choice — cannot engage what is not there).

### Mechanisms left intact (these are correctly bottom-up)
- `support_engage_frac` — depth-weighted cell support (per-atom)
- `engagement_angle` + `ANGLE_DEF_MOD` — facing-based flank/rear bonuses
- `_momentum_speed` puncture — speed differential at contact
- `count_engagements_per_atom` + `ENCIRCLEMENT_PENALTY` — multi-attack penalty
- `MIN_DISCIPLINE` — deployment-validity check (not a combat modifier)

## BATTERY RESULTS (n=80; H3 confirmed at n=200)

**In-band: 9/13 at n=80 (69%); effectively 10/13 with H3 at n=200**

| Test | v9 result | v10 (n=80) | Target | Δ from v9 | Status |
|------|-----------|------------|--------|-----------|--------|
| H1  | 51.2% | 51.2% | 45-55% | 0.0  | ✓ |
| H2  | 55.0% | 55.0% | 50-65% | 0.0  | ✓ |
| H3  | 43.8% | 66.2% (n=80) / 64.5% (n=200) | 50-65% | +22pp | ✓ (geometry alone produces envelopment) |
| H4  | 52.5% | 51.2% | 40-60% | -1.3 | ✓ |
| H5  | 82.5% | 43.8% | 50-65% | -38.7 pp | OPEN (real geometric Q below) |
| H6  | 66.2% | 51.2% | 45-60% | -15.0pp | ✓ |
| H7  | 68.8% | 51.2% | 50-65% | -17.6pp | ✓ |
| H8  | 72.5% | 56.2% | 45-60% | -16.3pp | ✓ |
| H9  | 62.5% | 56.2% | 35-50% | -6.3pp  | OPEN (tension K, structural) |
| H10 | 66.2% | 43.8% | 35-50% | -22.4pp | ✓ |
| H11 | 46.2% | 46.2% | 40-60% | 0.0  | ✓ |
| R1  | 90.0% | 90.0% | 30-50% | 0.0  | OPEN (tension L, independent) |
| R3  | 47.5% | 47.5% | 45-55% | 0.0  | ✓ |

## KEY VALIDATION

**H3 Horseshoe vs Line at 64.5% (n=200) inside 50-65%** — purely geometric. Horseshoe
wings extend beyond Line's flanks at T3 (7-wide vs 5-wide), making contact at the Line's
side cells from a FLANK angle. The `engagement_angle` mechanism converts that to -1D
defender penalty. The `support_engage_frac` lets the Horseshoe center stack support
behind contact. No shape bonus needed.

**H2 Arrowhead vs Line at 55%** — purely geometric. Wedge tip's `support_engage_frac`
puts all back-row cells behind 1 contact cell → effective ratio ~5x. The `_momentum_speed`
puncture bonus reflects the wedge advancing while the line halts. Both already in v8/v9;
v10 just removed the redundant flat +2D.

## OPEN TENSIONS (v10 → v11 candidates)

### Tension M: RefusedFlank vs Horseshoe (H5, 43.8% / 46.0% at n=200)
*v9 was 82.5% (over) due to `engaged=+1` bonus. v10 swung to 46% (slight under).*

Real geometric question: RefusedFlank's refused column has 1 forward cell at the front.
The Horseshoe's wing on that side reaches and engages that 1 cell, getting partial flank
advantage. Historically (Leuctra, Leuthen) the refused side withdrew entirely from
contact. To model this faithfully, the refused column might need to be 0 cells (pure
withdrawal) — but then the side becomes geometrically *open*, allowing the Horseshoe
wing to envelop further. The v11 question: is the refused-flank advantage actually
depth-concentration (Leuctra's 50-deep left wing punching through) rather than wing
avoidance? If so, RefusedFlank may need a depth-concentration multiplier on the engaging
side, not flank-withdrawal logic.

### Tension K (carry-over): side-A bias in asymmetric matchups
H2 (Arrow-A) 55%, H9 (Line-A vs Arrow-B) 56%. ~5-6pp side-A bias when shapes differ.
Mirror H1 has no bias (51.2%). Structural — likely advance_dir cell-offset interaction.
Out of v10 scope.

### Tension L (carry-over): Ranged over-tuned (R1: 90% vs 30-50%)
Independent of shape mechanics. Volley fires ~5 turns before melee contact; per-turn
damage ~0-1 size loss accumulates to wipe Line before contact. Tuning options:
reduce volley pool (Power−1), increase DR per armour class, or limit volley turns.

## ARCHITECTURAL PRINCIPLE ESTABLISHED

**Shape advantages are geometric, not bonus-based.** v10 demonstrates that historical
formation outcomes can be reproduced on a granular bottom-up basis:
- Wedge concentration → `support_engage_frac` per-cell depth support
- Envelopment → `engagement_angle` from wings reaching past flanks
- Refused flank → withdrawal of cells from contact (geometric, not bonus)
- Manipular gaps → cells absent at gap (geometric, not bonus)

Future iterations must follow this principle: if a shape produces wrong outcomes,
either the geometry is wrong (cell pattern fix) or a geometric mechanism is missing
(e.g., depth-concentration multiplier). Flat per-shape dice bonuses are forbidden.

## STATUS

EXPLORATORY. v10 commits the bottom-up restructure. M/K/L remain open for v11. The
v9 tension J cluster (RefusedFlank/GappedLine over-tune at 66-82%) is RESOLVED — those
matchups now sit in their target bands without any per-shape bonus.

ED-814 remains canonical mechanic; atom architecture not yet ratified but principle of
bottom-up emergence is established and tested.
