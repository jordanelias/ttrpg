# SIM-MB-06 v8 Module Manifest
# Iteration: v7 → v8 (tension F three-part resolution)
# Date: 2026-05-12

## ADDED IN v8

### F-i: Cell support stacking
Frontmost contact cells receive weighted contributions from non-contact
cells at greater depth. `effective_engage_frac = min(1.0, (contact + support_total) / atom_max_width)`.

Globals:
- SUPPORT_STACK_ENABLED = True
- SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}  (depth from contact)
- SUPPORT_WEIGHT_FLOOR = 0.3

New functions: `cells_to_orig_coords`, `support_engage_frac`

### F-ii: Puncture mechanism
Atoms with higher cell momentum (mean `cell_last_speed` at contact cells)
add a pool bonus proportional to the speed differential, capped at PUNCTURE_CAP.

Globals:
- PUNCTURE_ENABLED = True
- PUNCTURE_CAP = 3

`Atom` dataclass gains: `cell_last_speed: Dict[Tuple[int,int], int]`
(updated only when cell physically moves — persists through halt turns).

New function: `_momentum_speed(atom, contact_abs_cells)`

### F-iii: Cascading sub-phase resolution
Contacts sorted by attacker depth (foremost first); grouped into 1-row
depth buckets. Each sub-phase resolves its group, then rotates engaged
cells toward opponents (`_rotate_defender_facing`). Later sub-phases use
the rotated facings, granting FLANK/REAR bonuses to subsequently arriving rows.

Globals:
- CASCADING_ENABLED = True
- MAX_SUB_PHASES = 5

New functions: `_cell_facing_key`, `_rotate_defender_facing`,
`_init_dynamic_facings`, `_atom_avg_facing`, `_cascade_depth_key`,
`resolve_engagements_cascading`

## BATTERY RESULTS (sim_mb_06_v8_battery.py, n=80-120 per matchup)

| Test | Matchup | v7 | v8 | Target | Status |
|------|---------|----|----|--------|--------|
| T1 | Arrowhead vs Line T3 (KEY) | 0% | 45.8% | 40-60% | ✅ RESOLVED |
| T2 | Line mirror bias | ~50/50 | 56/41 | <±8pp | ✅ OK |
| T3 | Cannae (Horseshoe vs Arrow) | 62% | 48.0% | 40-65% | ✅ OK |
| T4 | Reversed Cannae | — | 44.0% | 35-60% | ✅ OK |
| T5 | Tier T2 Arrowhead vs Line | — | 56.2% | 40-60% | ✅ OK |
| T5 | Tier T3 Arrowhead vs Line | 0% | 46.2% | 40-60% | ✅ OK |
| T5 | Tier T4 Arrowhead vs Line | 0% | 42.5% | 40-60% | ⚠️ 55% draws, t=14.8 |
| T6 | Horseshoe vs Line T3 | 0% | 31.7% | 40-60% | ❌ OPEN |
| T7 | Lethality (Line mirror turns) | 9.7 | 9.8 | 3-6 | ❌ OPEN |

## OPEN TENSIONS (v8 → v9 candidates)

### Tension G: Horseshoe vs Line (T6, 31.7%, target 40-60%)
Horseshoe wings engage Line flanks at similar depth → support stacks
comparably. Horseshoe shape bonus (FLANK mod on engaged wings) did not
overcome Line width advantage. Needs investigation: Horseshoe pattern
geometry for support calculation, or dedicated shape-role modifier.

### Tension H: Lethality (T7, t=9.8, target 3-6)
Support stack doesn't affect Line-vs-Line engage_frac (was already ~1.0
in v7). Puncture gives no bonus when both sides advance at equal speed.
Likely requires a separate damage-floor or hp-scale fix independent of
engage_frac.

### Tension I: T4 draws (T5 tier sweep, 55% draws at T4, t=14.8)
High-tier units surviving to max_turns (15). Compound of lethality
problem. May resolve when T7 is fixed, or requires per-tier hp scaling.

## STATUS

EXPLORATORY. Tension F (T1 key metric) RESOLVED: Arrowhead vs Line T3
climbs from 0% → 45.8%. Tensions G (Horseshoe vs Line), H (lethality),
I (T4 draws) remain open.

ED-814 remains canonical mechanic. Atom architecture not yet ratified.
