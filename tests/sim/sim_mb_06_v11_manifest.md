# SIM-MB-06 v11 — Manifest

session_id: bcae4a75c4bbc4b0
iteration: v10 -> v11
status: EXPLORATORY
base_commit: cae8b39 (v10)

## Module scope
Single module: mass_combat. Mode G compliant.

## Canonical references (force_full)
- canon/02_canon_constraints.md, params/mass_combat.md
- designs/provincial/mass_battle_v30.md
- references/historical/precedents_warfare.md
- references/canonical_sources.yaml, skills/valoria-simulator/SKILL.md
- designs/architecture/complete_systems_reference.md
- designs/scene/derived_stats_v30.md, params/core.md

## v11 changes
1. Atom -> Subunit rename
2. Per-cell octagon angle: GREEN<45=0D, YELLOW 45-90=-1D, RED>=90=-2D
3. Vector halt-at-contact: halt_before_enemy() pulls cells back on over-run
4. GappedLine gap skip removed: geometric mechanism only
5. Ranged melee penalty: unit_type='ranged' in contact -> pool //= 2

## Battery (n=500): 10/13 in-band

| Test | Matchup | Target | Result |
|------|---------|--------|--------|
| H1 | Line mirror | 45-55 | 51.6 OK |
| H2 | Arrow vs Line | 50-65 | 49.8 borderline |
| H3 | HS vs Line | 50-65 | 60.2 OK |
| H4 | HS vs Arrow | 40-60 | 46.4 OK |
| H5 | RF vs HS | 50-65 | 37.4 OUT |
| H6 | RF vs Line | 45-60 | 57.2 OK |
| H7 | GL vs Line | 50-65 | 51.6 OK |
| H8 | GL vs Arrow | 45-60 | 50.8 OK |
| H9 | Line vs Arrow | 35-50 | 45.2 OK |
| H10 | Line vs HS | 35-50 | 36.6 OK |
| H11 | Arrow vs HS | 40-60 | 49.0 OK |
| R1 | Ranged vs Line | 30-50 | 69.4 OUT (was 91%) |
| R3 | Ranged mirror | 45-55 | 45.8 OK |

## Open tensions
- M (H5): RF vs HS 37.4%. Needs RF wing-pivot or defensive bonus.
- L (R1): Ranged vs Line 69.4% (improved from 91%). Volley still dominant.
- H7 borderline: GL blocks converge on shared centroid; needs per-subunit targeting.

## Drift risk
octagon_angle/cell_facing_vec is new code; needs Jordan review.
