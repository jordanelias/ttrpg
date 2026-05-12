# SIM-MB-06 v12 — Manifest

session_id: bcae4a75c4bbc4b0
iteration: v11 -> v12
status: EXPLORATORY
base_commit: 304df9e (v11)
directive: keep working bottom up, ensure historical precedent results respected top down

## Module scope
Single module: mass_combat (engagement + movement + volley). Mode G compliant.

## Canonical references consulted (force_full)
- canon/02_canon_constraints.md, params/mass_combat.md
- designs/provincial/mass_battle_v30.md
- references/historical/precedents_warfare.md
- references/canonical_sources.yaml, skills/valoria-simulator/SKILL.md
- designs/architecture/complete_systems_reference.md
- designs/scene/derived_stats_v30.md, params/core.md

## v12 changes (5 bottom-up mechanisms, each historically anchored)

### 1. Column-local targeting (advance_cells)
Each cell's target = (target_centroid_row, my_starting_col). Replaces full
centroid-attractor. No lateral drift unless explicitly ordered.
Citation: infantry historically held assigned files; lateral drift = breakdown.
Effect: GappedLine gap stays open, HS wings preserve width, wedge tip leads.

### 2. VOLLEY_MAX_RANGE 25 -> 8
Initial deployment is 10 cells apart. Range 8 means 1-2 turns of approach
before volleys begin.
Citation: precedents_warfare.md — Crécy/Agincourt killing zones at final 100 paces.

### 3. Ranged melee penalty pool//2 -> pool//3
Archers in close combat: pool divided by 3 (was 2).
Citation: precedents_warfare.md — Agincourt/Crécy archer melee performance marginal.

### 4. Volley HP scaling ceil(h_per_size / 2)
1 size loss from volley = ceil(h_per_size/2) hp (was full h_per_size).
Bottom-up rationale: ranged size loss represents arrows finding targets in
formation; melee size loss represents decisive wounds. This is the single
biggest lever — moved R1 from 69% to 35%.

### 5. RefusedFlank front-row speed 2
Front rank (local_r=0, non-refused) advances at speed 2 like cavalry/wing.
Citation: precedents_warfare.md — Leuctra 371 BC oblique order, Theban front rank
charged at battle pace ahead of depth.

## Battery results (n=500): 12/13 in-band

| Test | Matchup | Target | v11 | v12 | Status |
|------|---------|--------|-----|-----|--------|
| H1   | Line mirror | 45-55% | 51.6% | 51.6% | OK |
| H2   | Arrowhead vs Line | 50-65% | 49.8% | 54.4% | OK (was borderline) |
| H3   | Horseshoe vs Line | 50-65% | 60.2% | 59.4% | OK |
| H4   | Horseshoe vs Arrowhead | 40-60% | 46.4% | 52.2% | OK |
| H5   | RefusedFlank vs Horseshoe | 50-65% | 37.4% | 47.4% | borderline OUT |
| H6   | RefusedFlank vs Line | 45-60% | 57.2% | 57.4% | OK |
| H7   | GappedLine vs Line | 50-65% | 51.6% | 51.6% | OK |
| H8   | GappedLine vs Arrowhead | 45-60% | 50.8% | 49.6% | OK |
| H9   | Line vs Arrowhead | 35-50% | 45.2% | 48.2% | OK |
| H10  | Line vs Horseshoe | 35-50% | 36.6% | 39.8% | OK |
| H11  | Arrowhead vs Horseshoe | 40-60% | 49.0% | 48.4% | OK |
| R1   | Ranged vs Line | 30-50% | 69.4% | 34.6% | OK (RESOLVED) |
| R3   | Ranged mirror | 45-55% | 45.8% | 47.2% | OK |

## Tensions carried forward

- **H5 (RF vs HS)**: 47.4%, only 2.6% below the 50% floor. Substantially improved
  from v11's 37.4% (10% gain) but not fully in band. The challenge: RF's deep
  column should beat HS's wider wing-wrap, but mechanisms that strengthen RF
  also help RF vs Line (H6) which is already in band. Need a geometry-aware
  mechanism that distinguishes wider-than-me from same-width opponents.
  v13 candidates:
  - Refused-stub repositioning closer to engaged column (defensive anchor)
  - Depth-ratio pool bonus when enemy extends past own footprint
  - Anti-wrap mechanism: cells engaging from outside enemy's column range
    have asymmetric angle penalties

## Mechanisms tried and reverted

- **Per-cell-nearest targeting** (each cell targets nearest enemy cell): caused
  pathological convergence — all GL cells converged on Arrowhead tip, broke
  6/13 tests. Column-local is the working compromise.
- **VOLLEY_MAX_RANGE=5**: broke R3 (ranged mirror couldn't reach at dist 10).
- **RANGED_DR_DEFAULT 2 -> 3**: overshot — R1 fell to 23% (under floor),
  R3 had 27% draws (units too tough).
- **engage_frac cap 1.0 -> 1.5**: regressed H2/H7/H10, didn't help H5 (cap
  benefits both sides similarly; H5 needs RF-specific advantage).
- **Whole-column speed 2 for RF**: H5 in band (56.8%) but H6 broken (64.8%).
- **Front-2-rows speed 2 for RF**: H5 in band (52.2%) but H6 broken (64.0%).

## Drift risk

5 layered mechanisms atop v11 architecture. Volley HP scaling (change 4) is a
canonical-rule modification per mass_battle_v30.md §A.7 PP-503 — needs Jordan
review before promotion from EXPLORATORY. Column-local targeting changes the
movement model fundamentally. Battery survives but new shapes / cavalry / tier
4 untested at this layered config.
