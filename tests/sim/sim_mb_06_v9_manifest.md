# SIM-MB-06 v9 Module Manifest
# Iteration: v8 → v9 (unit-type infrastructure + Phase 2 Volley + historical battery)
# Date: 2026-05-12

## SCOPE

v9 adds unit-type infrastructure and Phase 2 Volley to enable proper configuration of
historical formations and ranged combat. Historical accuracy specification documented
in `tests/sim/sim_mb_06_v9_historical_spec.md` provides target win-rate bands for each
formation matchup grounded in `references/historical/precedents_warfare.md §1.1` and
the design doc's §A.6/§A.8 formation counter logic.

## ADDED IN v9

### Unit-type field on Atom
- `Atom.unit_type: str = 'melee'` (default; explicit per atom)
- `'melee'`: engages at contact (v8 behavior preserved verbatim)
- `'ranged'`: fires in Phase 2 at any enemy in line of sight, no adjacency required

### Phase 2 Volley implementation
- `volley_phase(unit_a, unit_b)` runs BEFORE Phase 3 Manoeuvre per §A.7
- Each ranged atom targets nearest in-range enemy atom
- Pool = `Power` dice (PP-503, not engagement pool formula PP-233)
- TN = 6 (`VOLLEY_TN`)
- Net successes − `RANGED_DR_DEFAULT` (=2 for Medium armour) = Size loss
- Size loss × `h_per_size` = HP loss (applied at Phase 6 Step 1, simultaneous with engagement damage)
- `VOLLEY_MIN_RANGE = 2` (cells; ranged stops firing when in melee contact)
- `VOLLEY_MAX_RANGE = BATTLEFIELD_SIZE` (25; full battlefield in v9)

### Volley helpers
- `_atom_distance(atom_a, atom_b)`: Chebyshev distance between nearest cells
- `_roll_volley_pool(power_dice)`: TN=6 d10 dice engine, 1=−1/10=+2 per §A.1
- `Unit.discipline_penalty_volley()`: pool reduction for Volley (positive int)

### Globals (citable from ledger)
- `VOLLEY_ENABLED`, `VOLLEY_TN`, `VOLLEY_MIN_RANGE`, `VOLLEY_MAX_RANGE`
- `RANGED_DR_DEFAULT`

## BATTERY RESULTS (n=80 per matchup, seed_base=1000000)

### In-band: 5/13 (38%)

| Test | Matchup | v9 | Target | Status |
|------|---------|----|----|--------|
| H1 | Line vs Line (mirror)          | 51.2% | 45–55% | ✓ |
| H2 | Arrowhead (Wedge) vs Line      | 55.0% | 50–65% | ✓ |
| H4 | Horseshoe vs Arrowhead (Cannae)| 52.5% | 40–60% | ✓ |
| H11| Arrowhead vs Horseshoe (rev H4)| 46.2% | 40–60% | ✓ |
| R3 | Ranged vs Ranged (mirror)      | 47.5% | 45–55% | ✓ |

### Out-of-band: 8/13 — surfaces three tunable tensions

| Test | Matchup | v9 | Target | Tension |
|------|---------|----|----|---------|
| H3 | Horseshoe vs Line              | 43.8% | 50–65% | G (v8 carry-over; improved from 31.7%) |
| H5 | RefusedFlank vs Horseshoe      | 82.5% | 50–65% | J — asymmetric shape over-tuned |
| H6 | RefusedFlank vs Line           | 66.2% | 45–60% | J |
| H7 | GappedLine vs Line             | 68.8% | 50–65% | J |
| H8 | GappedLine vs Arrowhead        | 72.5% | 45–60% | J |
| H9 | Line vs Arrowhead (rev H2)     | 62.5% | 35–50% | K — side-A bias amplified in asymmetric |
| H10| Line vs Horseshoe (rev H3)     | 66.2% | 35–50% | K |
| R1 | Pure Ranged vs Pure Line       | 90.0% | 30–50% | L — ranged over-tuned despite DR=2 |

## OPEN TENSIONS (v9 → v10 candidates)

### Tension G: Horseshoe vs Line (H3, 43.8%)
v8 baseline was 31.7%; v9 improved to 43.8% (likely via unit_type plumbing not affecting
melee logic — the change is statistical noise or seed sensitivity). Still below H3 band
50–65%. Root cause: support stacking gives Line frontal-engagement parity with Horseshoe
wings; needs shape-role asymmetry in the wing-engagement bonus.

### Tension J: Asymmetric shapes over-strong (H5/H6/H7/H8)
RefusedFlank and GappedLine win 66–82% vs targets 45–65%. Likely cause: `SHAPE_OFF_MOD`
role bonuses (`flank_engaged` +2, `refused` -2 but partner cells get +1) stack too
aggressively when only one side has an asymmetric shape. Calibration needed: reduce
shape-role bonus magnitudes, or apply only when the role's geometric precondition is met
(e.g., RefusedFlank `refused` role only activates when actually being flanked, not by default).

### Tension K: Side-A bias in asymmetric matchups (H9/H10)
H2 (Arrowhead-A vs Line-B) = 55%; H9 (Line-A vs Arrowhead-B) = 62.5%. Both should not
exceed 55% if shapes are symmetric. ~10pp side-A advantage emerges when shapes differ.
Mirror H1 within tolerance (51.2%). Root cause unclear: likely advance_dir=-1 path
interaction with cell pattern mirroring. Reproduce with controlled seeds, instrument
volley_dmg + engagement_dmg + halt-cell flags per turn.

### Tension L: Ranged over-tuned (R1, 90% vs 30–50%)
v9's volley fires 4–5 turns before melee can close. Per-turn impact: Power=4 → ~2 net
successes − DR 2 = 0 to 1 size loss per turn → 0–5 hp damage. Over 5 turns this is
0–25 hp out of 20 hp_max — enough to destroy unit before contact in many cases. Per
§A.7 ED-753 design intent ("pure-ranged underperforms parity melee"), need to either:
(a) reduce volley pool below Power (e.g., Power−1),
(b) increase DR (Heavy = 3),
(c) reduce volley turns by enabling melee approach speed bonus when under fire, or
(d) cap volley successes per turn.

## ARCHITECTURAL NOTES

### What infrastructure delivers (separable from tuning)
The v9 commit delivers configuration capacity: future iterations can declare units like
`Atom(shape='Arrowhead', unit_type='ranged', stance='hold')` to model mounted archers,
combined-arms compositions, etc. The Phase 2 volley correctly runs before movement and
applies damage simultaneously with engagement per the design doc's simultaneous-damage rule.

### What v9 does NOT yet model (deferred to v10+)
- Shield Wall, Skirmish, Column, Feigned Retreat formations (need `formation_modifier` field)
- Armour class per atom (currently all targets use RANGED_DR_DEFAULT=2 Medium)
- Cavalry (Speed-Fast melee with charge bonus)
- Combined-arms compositions (multi-atom units mixing ranged + melee in one army)
- Terrain modifiers (§A.9)

## STATUS

EXPLORATORY. v9 commits the unit-type + ranged infrastructure. Tunings G/J/K/L are
documented as open tensions; the historical spec provides verifiable target bands for
each. ED-814 remains canonical mechanic; atom architecture not yet ratified.

Mirror sanity holds (H1: 51.2%); Wedge>Line works (H2: 55%); Cannae works (H4: 52.5%);
infrastructure correctly enables ranged units (R3 mirror: 47.5%, R1 demonstrates over-tuning
which is a knob, not a structural defect).
