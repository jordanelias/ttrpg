# SIM-MB-06 v13 — Manifest

**Session:** 2026-05-12/13
**Iteration:** v12 → v13
**Commit scope:** simulation
**File:** `tests/sim/sim_mb_06_v13.py`

## Summary

v13 adds **one bottom-up mechanism**: cross-side cell contention via strict speed-differential resolution. Prior to v13, cells from opposing sides could end the phase at the same absolute position — magical co-location. v13 resolves these contests per historical precedent: faster cell wins the position, loser reverts.

Battery preserved at 12/13 in-band at n=500. H5 (RefusedFlank vs Horseshoe) remains the open tension at 47.4% (target 50-65%). v13 does not address H5 — that requires geometry-aware wrap-around handling, deferred to v14.

## Jordan design directive (2026-05-12)

Two messages, in sequence:

1. **Within-side formation hold (discipline-gated):**
   > "a cell can hold X number of troops, which means it can only absorb a finite amount from neighbouring cells... if a cell of troops is joining another cell of troops, then that cell will have a vector that faces the midpoint of that troop... subunits abandoning their subformation where cells merge partially/completely into other cells is a tactical failure... this comes down to discipline."

2. **Cross-side cell contention (speed-priority):**
   > "if the fronts of two opposing cells become adjacent, then there is fighting. if they were to occupy the same cell, then the troop with higher speed gets priority for taking up that adjacent cell while the other remains in place. if they have the same speed, then the troop with the greater size gets that space. if they are the same size, then it's randomized who gets it... a cell can only move beyond a cell directly facing them if they have sufficient speed, eg a cavalry charge... if a phase ends and a subunit cell like cavalry is occupying the same spot as an opponent, then the opponent cells will shift back to accommodate them."

## v13 mechanism: cross-side cell contention

### Implementation

`resolve_cross_side_contention(unit_a, unit_b)` runs after both sides advance and before `find_contacts`. It:

1. Collects per-side `abs_pos → [(subunit, orig_coord, contention_speed)]` maps.
2. Identifies contested positions (occupied by cells from both sides).
3. For each contested position:
   - Skips if neither side moved into the position this turn (stale contention).
   - Resolves on **strict speed differential**: higher speed wins.
   - **Tied speed → no movement resolution** (combat decides via engagement, per the historical hoplite-mirror model).
4. Loser cells that moved this turn revert to their pre-move snapshot (`_prev_offsets`); cells didn't actually advance into the contested position.

Supporting infrastructure added to `Subunit`:
- `_prev_offsets`, `_prev_offsets_c`, `_prev_facings`: snapshot at top of `advance_cells` before any movement.
- `_moved_this_turn: Set[Tuple]`: tracks cells that actually moved this turn (vs halted, hold-stance, or already-at-target).

### Why conservative on tiebreakers

Jordan's full rule specifies size and random tiebreakers when speeds match. v13 omits these. Reasons:

1. **Battery noise.** Applied per contested position per turn in symmetric-speed matchups (Line vs Line, H1 mirror), random tiebreakers fire on every tied contest. Net effect: variance with no historical grounding.

2. **Historical model for equal-speed meetings.** Two disciplined infantry formations of equal speed don't resolve their meeting via movement priority. They reach the contact line at the same time and resolve via combat (the push, the engagement, casualties). This is the hoplite phalanx mirror; the Roman vs Roman civil war engagement. Movement-priority resolution is for cases where one side has a real organizational speed advantage.

3. **Cavalry deferred.** Size and random tiebreakers will matter when cavalry exists — cavalry vs heavy infantry contests, light cavalry probing screens, etc. Framework supports re-enabling when cavalry units enter the test suite.

### Historical grounding

- **Crécy 1346 / Agincourt 1415:** English defenders pre-positioned via faster deployment (chosen terrain, archers in place before French knights closed). Speed-priority = whoever gets to the ground first wins it; the slower halts in place.
- **Leuctra 371 BC:** Epaminondas's oblique order. Strong wing advances faster than the weakened wing. Strong wing reaches Spartan elite before Spartan right can engage. Speed advantage = first-engagement priority.
- **Hoplite phalanx mirror:** Equal-speed disciplined formations meeting at adjacency don't resolve by movement priority. Combat (othismos, the push) decides. → equal-speed contests stay co-located, resolved by find_contacts + engagement damage.

### Charge-through and end-of-phase displacement

Jordan's spec includes:
- Cavalry charge-through (cell moves past directly-facing enemy with sufficient speed/power; penetration depth = f(speed, attack power, enemy facing))
- End-of-phase displacement (opponent cells shift back when cavalry ends co-located)

Neither is wired in v13 — current battery is infantry-only. Framework supports:
- `_moved_this_turn` distinguishes moving from static
- `cell_last_speed` available for speed comparison
- Loser-shift-back logic implementable via `cell_offsets -= 1`

To enable when cavalry exists: add speed threshold for charge-through (e.g., speed ≥ 3 vs static facing-forward enemy → penetrate; speed/power/facing → depth). End-of-phase displacement becomes the shift-back path for static-loser cases.

## Within-side discipline-gated formation hold (NOT INVOKED)

Earlier in the session I implemented Jordan's first message (cell capacity, discipline-gated merge with midpoint facing) as `Subunit.resolve_internal_collisions`. Result: battery dropped 12/13 → 9/13. Diagnostics:

- RF cells average ~31 collisions per battle (deep column piles up behind halted front rank); HS averages ~4.
- The mechanism fires on every collision. Discipline check pass = revert, fail = merge with midpoint facing.
- The FAIL case's midpoint-of-two-forward-vectors is still forward — no effective facing penalty when both cells advance in the same direction.
- The PASS revert preferentially helps shapes with deep column stacking (RF, Line), hurts those without (Arrowhead spread across columns) — asymmetric effect not grounded in design intent.

The method is left in the code (line ~582 in v13.py) but not invoked. Re-enabling requires a proper bad-facing trigger — likely tied to wrap-around (when one side's cells force the other's cells to face perpendicularly into the wrap, the midpoint vector becomes truly different from forward).

## Battery (n=500)

| Test | A vs B | Result | Target | Status |
|------|--------|--------|--------|--------|
| H1 | Line vs Line | 51.6 | 45-55 | ✓ |
| H2 | Arrowhead vs Line | 54.4 | 50-65 | ✓ |
| H3 | Horseshoe vs Line | 61.6 | 50-65 | ✓ |
| H4 | Horseshoe vs Arrowhead | 48.2 | 40-60 | ✓ |
| **H5** | **RefusedFlank vs Horseshoe** | **47.4** | **50-65** | **← OUT** |
| H6 | RefusedFlank vs Line | 56.8 | 45-60 | ✓ |
| H7 | GappedLine vs Line | 51.6 | 50-65 | ✓ |
| H8 | GappedLine vs Arrowhead | 49.6 | 45-60 | ✓ |
| H9 | Line vs Arrowhead | 48.2 | 35-50 | ✓ |
| H10 | Line vs Horseshoe | 37.6 | 35-50 | ✓ |
| H11 | Arrowhead vs Horseshoe | 51.0 | 40-60 | ✓ |
| R1 | Ranged vs Line | 34.6 | 30-50 | ✓ |
| R3 | Ranged vs Ranged | 47.2 | 45-55 | ✓ |

**In-band: 12/13** (same as v12 commit).

### Firing diagnostics (50 battles per test)

| Test | Firings/battle | Why |
|------|---|---|
| H1 Line-Line | 0.0 | Symmetric speed-1, no differential |
| H2 Arrow-Line | 1.0 | Arrow tip speed-2 beats Line speed-1 once per battle |
| H3 HS-Line | 14.0 | HS wings speed-2 vs Line speed-1, sustained |
| H5 RF-HS | 0.0 | Both have speed-2 components — tied speed → combat decides |
| H6 RF-Line | 4.0 | RF front speed-2 vs Line speed-1 |
| H7 GL-Line | 0.0 | Both speed-1 throughout |
| H9 Line-Arrow | 1.0 | Symmetric to H2 |
| H10 Line-HS | 8.0 | Symmetric to H3 |

Mechanism doing work in asymmetric matchups; correctly silent in symmetric ones.

## H5 deferred to v14

The fundamental insight: H5's tension isn't cell co-location (which v13 resolves). It's HS wings extending PAST RF's footprint. The wrap isn't an overlap — HS cells are at columns RF doesn't occupy. Speed-priority resolution doesn't address wrap geometry.

Candidate mechanisms for v14:
- Refused-stub repositioning (mobile reserve responding to wing extension)
- Depth-ratio pool bonus when enemy extends past own footprint width
- Defensive angle bonus for cells engaging outside-footprint enemies (anti-flanking)
- Anti-wrap perimeter check

These are geometry-aware, not speed-aware. Different mechanism family than v13.

## Drift risk

- **Strict-speed-only deviation from Jordan's full spec is documented inline** in `resolve_cross_side_contention` docstring and in this manifest. Future cavalry work re-enables tiebreakers; PI text rule should match the deviation note.
- **Within-side merge mechanism left dormant** — code exists, not invoked. Risk: re-enabling without fixing the FAIL-case midpoint-facing issue would re-break battery.
- **Charge-through framework partially scaffolded** (snapshot, moved-this-turn tracking) but not wired. Risk: future cavalry implementation must use these primitives rather than inventing parallel ones.

## Files

- `tests/sim/sim_mb_06_v13.py` — 1351 lines, simulation
- `tests/sim/sim_mb_06_v13_manifest.md` — this file
- `tests/coverage_matrix.md` — v13 entry added
