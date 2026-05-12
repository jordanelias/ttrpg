# SIM-MB-06 v11 -- per-cell octagon angle model

## Changes from v10
- Atom renamed to Subunit; Unit.atoms -> Unit.subunits
- Per-cell facing vector (cell_facing_vec): records raw (dr,dc) per cell.
- Per-cell octagon angle replaces centroid-to-centroid.
  octagon_angle(atk_centroid, def_pos, def_facing) -> GREEN/YELLOW/RED.
  [canonical: designs/provincial/mass_battle_v30.md §octagon]
  Uses attacker centroid to avoid equidistant non-determinism.
- halt_before_enemy: stub (disabled).
- GappedLine gap skip (-99) removed; gap effect is geometric.
- role_at_contact GL size table updated: {1:2,2:3,3:4,4:4}.
- Ranged melee penalty: unit_type='ranged' -> pool //= 2.

## Battery n=500
10/13 in-band (matches v10)
Open M: H5 RF vs HS 37.4pct; Open L: R1 Ranged 69.4pct (improved from 91pct)
