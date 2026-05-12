# Valoria Simulation Coverage Matrix
## Last updated: 2026-05-11 | SIM-MB-05A/B/C (Phase 2 complete)

| System | Last Sim | Scenarios | Findings | P1 Open | Status |
|--------|----------|-----------|----------|---------|--------|
| mass_combat (engagement) | SIM-MB-05A | Line vs Line + matrix | F-G lethality at 3.95t target met | — | ✓ ED-811 validated |
| mass_combat (volley) | SIM-MB-05C | TN6 vs TN7 composition sweep | F-I ranged dominance partial fix | ED-822 | ⚠ TN7 partial fix; ED-825 secondary measure |
| mass_combat (composition grid) | SIM-MB-05A | 5 shapes × 4 comps | — | — | ✓ ED-814 distribution validated |
| mass_combat (shapes) | SIM-MB-05A/B/C | 5×5 matrix + 4 H-variants | F-A,B,C all resolved; H-2 selected | — | ✓ ED-816 fully calibrated |
| mass_combat (drift cascade) | SIM-MB-05C | direct vs tiered alternatives | direct-to-Line selected over tiered | — | ✓ ED-817 validated |
| mass_combat (Discipline) | SIM-MB-05A | shape min-Disc tests | — | — | ✓ ED-815 reframing holds |
| mass_combat (combined attack) | SIM-MB-05A/C | vs 5 shapes; 3v1 test harness | F-D undercalibrated; F-J Fibonacci aggressive | ED-823 | ⚠ test harness needs rebuild |
| mass_combat (Horseshoe trigger) | SIM-MB-05C | 4 H-variants × 4 opponents | H-2 positional selected (54% mean) | — | ✓ ED-821 resolved → ED-816 |
| mass_combat (rally) | SIM-MB-04 | isolation | — | — | ✓ ED-802 formula verified |
| mass_combat (withdrawal) | SIM-MB-04 | conceptual | — | ED-813 | Phase 1 fix in workplan |
| mass_combat (stability) | SIM-MB-04 | S1,S2 | — | — | ✓ ED-808 correct |
| mass_combat (grid map) | SIM-MB-04 | 8x5 grid | — | — | Prototype validated |
| combat (personal) | SIM-MB-03 | — | — | — | See prior sims |
| social_contest | sim_d06 | — | — | — | See prior sims |
| thread | sim_thread_batch_08 | — | — | — | See prior sims |
| strategic | sim_bg_ff_01 | — | — | — | See prior sims |

## SIM-MB-05A/B/C Summary
- Date: 2026-05-11
- Scope: Phase 2 shape mechanics validation + exhaustive branch exploration
- Trials: 6000+ across three batteries
- EDs validated and closed: 811, 812, 814, 815, 816, 817, 821
- EDs raised and open: 822 (Volley TN partial fix; secondary measure as ED-825), 823 (combined attack calibration)
- Lethality: 3.95t mean, 0/600 one-turn kills
- Shape matrix: produces strategic rock-paper-scissors with Horseshoe H-2 trigger
- Volley TN7: partial fix for composition imbalance (+8pp pure-melee competitiveness)


## SIM-MB-06 v5 Summary (exploratory)
- Date: 2026-05-11 → 2026-05-12 (Jordan-directed iteration v1→v5)
- Scope: atom architecture exploration — composite units, per-cell movement,
  25×25 battlefield w/ 5-cell buffer, side-mirrored patterns
- Status: EXPLORATORY. Three open design tensions before promotion to canonical:
  - Cannae envelopment failure (wings advance straight, do not curve in) — B-ii pending
  - Composite-vs-uniform balance (Bii pool over-penalizes small atoms) — C-i/ii pending
  - Arrowhead tip isolation (no support requirement) — E pending
- Mirror rule: Side B patterns flip vertically `(r,c) → (max_r−r, c)`;
  cell roles/speeds keyed by ORIGINAL pattern coords (preserve role across mirror)
- 25×25 battlefield expansion (from 21×21): 5-cell buffer per side enables flank arcs
- Visualization: tests/sim/sim_mb_06_v5_visual.html (8 sections incl. correction §8)
- NOT YET propagated to canonical mechanics — ED-814 (composition grid) remains
  the canonical formulation. This atom model would supersede ED-814 if ratified.


## SIM-MB-06 v6 Summary (exploratory, continued)
- Date: 2026-05-12
- Scope: bug hunt + architectural addition + Phase C pool formula
- Critical fix: halt-cell bug (Side B halted wrong cells due to mirror not applied)
  - Caused 80/20 Side A bias in mirror matches
  - Fix in run_battle: halt logic uses oriented_pattern() throughout
  - Verified: bias collapsed to ~52/48 at n=200 (within noise)
- Architectural addition: per-cell facing + engagement angle (Jordan request)
  - cell_facing(advance_dir) → (dr, dc) unit vector for each cell's front face
  - engagement_angle classifies FRONT / FLANK / REAR per cosine of approach
  - ANGLE_DEF_MOD = {FRONT: 0, FLANK: -1, REAR: -2} on defender pool
  - Side effect: Cannae now works at 62% naturally — B-ii may be obsoleted
- Phase C pool formula: C-ii validated (composite normalizes 5% → 38.3%)
- Remaining tensions:
  - E (tip support) — Arrowhead vs Line 0%, tip dies isolated
  - Horseshoe vs Line 0% — separate investigation needed
  - Lethality 9.7 turns vs 3-6 target — atoms under-damaging
- NOT YET PROPAGATED to canonical mechanics.


## SIM-MB-06 v7 Summary (exploratory, Phase E)
- Date: 2026-05-12
- Scope: tip support constraint (Phase E) + tension F discovery
- Tip support mechanic: fast cells (speed > min in atom) cannot advance
  more than TIP_SUPPORT_GAP offsets past slowest non-zero-speed cell.
  Affects Arrowhead only currently (tip 2, base 1).
- Defaults: ENABLED=True, GAP=2 (no behavioral change for current tests)
- Validated behavior at X=1:
  - Arrowhead vs Horseshoe: 17% → 63% (tip stays supported, wedge holds)
  - Cannae inverts: 65% → 33% (no longer self-isolating)
  - Arrowhead T2 vs Line T2: 4% → 34%
- DID NOT resolve Arrowhead T3/T4 vs Line — structural pool formula issue
- New tension F documented: pool formula penalizes narrow attackers,
  wedge cannot concentrate force. Four resolution options queued (F-i..F-iv).

## Next simulation priorities
1. **SIM-MB-06**: rebuild 3v1 combined attack test harness; validate ED-823 Fibonacci recalibration options
2. **Composition balance secondary measure**: test melee_pct Ob bonus / Volley pool cap / DR scaling (ED-825 candidate)
3. **Workplan Phase 3-6**: propagate ED-811..820 to mass_battle_v30.md and params files
4. **Then A3 SCHISM**: archetype 3 testing per parent workplan

## Handoff 2026-05-12
- tests/sim/sim_mb_06_handoff_2026-05-12.md — v7→v8 handoff doc with tension F design (cell-support stacking + puncture momentum + cascading sub-phase resolution with facing rotation)

## SIM-MB-06 v8 Summary (exploratory, tension F resolved)
- Date: 2026-05-12
- Scope: tension F three-part resolution — F-i support stack + F-ii puncture + F-iii cascade
- F-i: cell support stacking — non-contact cells at depth contribute weighted engage_frac
  (depth 1→1.0, depth 2→0.7, depth 3→0.5, floor 0.3); Arrowhead tip stack caps at 1.0
- F-ii: puncture — speed differential at contact → pool bonus (cap +3D per Jordan handoff)
  cell_last_speed tracked per orig-coord in Atom dataclass
- F-iii: cascading sub-phases — contacts sorted by attacker depth, resolved in groups;
  defender cells rotate facing after each sub-phase, enabling FLANK bonuses on later rows
- Battery results (n=80-120 per matchup):
  T1 Arrowhead T3 vs Line T3:       0% → 45.8% ✓ TENSION F RESOLVED (target 40-60%)
  T2 Line mirror bias:               6pp ✓ (< ±8pp)
  T3 Cannae (Horseshoe vs Arrow):    48.0% ✓ (was 62%, target 40-65%)
  T4 Reversed Cannae:                44.0% ✓
  T5 Tier sweep T2/T3/T4:            56.2 / 46.2 / 42.5% ✓ (T4: 55% draws, t=14.8)
  T6 Horseshoe vs Line T3:           31.7% ← OPEN (target 40-60%, was 0%)
  T7 Lethality (mean turns):         9.8 ← OPEN (target 3-6, unchanged)
- Open tensions:
  G: Horseshoe vs Line (31.7%) — support stack helped but short of target; shape geometry issue
  H: Lethality (t=9.8) — Line mirror → equal momentum, no puncture differential; hp-scale fix needed
  I: T4 draws (55%) — compound of H; resolves when H resolved
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v9 Summary (exploratory, unit types + ranged)
- Date: 2026-05-12
- Scope: unit_type infrastructure (melee/ranged) + Phase 2 Volley + historical-precedent battery
- ADDED:
  - Atom.unit_type field ('melee' default | 'ranged')
  - volley_phase(): Phase 2 ranged fire at line-of-sight distance (not adjacency)
  - VOLLEY_TN=6, VOLLEY_MIN_RANGE=2 (no fire when adjacent), VOLLEY_MAX_RANGE=battlefield
  - RANGED_DR_DEFAULT=2 (Medium armour vs Piercing per params/mass_combat.md)
  - Unit.discipline_penalty_volley() — pool reduction for ranged
  - Historical accuracy spec: tests/sim/sim_mb_06_v9_historical_spec.md (H1-H11 + R1-R3 bands)
- BATTERY (n=80, 13 matchups vs historical-precedent target bands):
  IN-BAND (5/13):
    H1  Line vs Line mirror:               51.2%  (target 45-55%)
    H2  Arrowhead (Wedge) vs Line:         55.0%  (target 50-65%) — design counter holds
    H4  Horseshoe vs Arrowhead (Cannae):   52.5%  (target 40-60%) — v8 tension F still resolved
    H11 Arrowhead vs Horseshoe (rev H4):   46.2%  (target 40-60%)
    R3  Ranged vs Ranged mirror sanity:    47.5%  (target 45-55%)
  OUT-OF-BAND (8/13) — surfaces 4 tunable tensions:
    G  H3 Horseshoe vs Line:               43.8% (target 50-65%) — improved from v8's 31.7%, still under
    J  H5 RefusedFlank vs Horseshoe:       82.5% (target 50-65%) — asymmetric shape over-tuned
    J  H6 RefusedFlank vs Line:            66.2% (target 45-60%)
    J  H7 GappedLine vs Line:              68.8% (target 50-65%)
    J  H8 GappedLine vs Arrowhead:         72.5% (target 45-60%)
    K  H9 Line vs Arrowhead (rev H2):      62.5% (target 35-50%) — side-A bias amplified
    K  H10 Line vs Horseshoe (rev H3):     66.2% (target 35-50%)
    L  R1 Pure Ranged vs Pure Line:        90.0% (target 30-50%) — ranged over-tuned despite DR=2
- INFRASTRUCTURE DELIVERED:
  Unit configuration now enables future formation modeling (Shield Wall, Skirmish via
  formation_modifier, cavalry via Speed-Fast melee, combined-arms via multi-atom units).
  Phase 2 Volley correctly runs before movement; damage applies simultaneously with engagement.
- OPEN TENSIONS for v10:
  G/J/K/L documented in tests/sim/sim_mb_06_v9_manifest.md
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v10 Summary (exploratory, bottom-up shape advantages)
- Date: 2026-05-12
- Scope: remove top-down SHAPE_OFF_MOD; equalize cell counts; let geometric mechanisms produce historical results
- DIAGNOSTIC ROOT CAUSE of v9 over-tuning:
  - GappedLine T3 had 56 cells vs Line's 25 (2.24x troops) — "shape advantage" was extra troops
  - RefusedFlank T3 had 21 cells (84% of Line) — flat +1D bonus masked the deficit
  - SHAPE_OFF_MOD double-counted geometric mechanisms (support_engage_frac, engagement_angle)
- CHANGES:
  - Equalized cell counts: GappedLine 56->24, RefusedFlank 21->25 at T3
  - SHAPE_OFF_MOD = {all: 0} (gap=-99 retained as structural sentinel only)
  - SHAPE_DEF_MOD = {all: 0}
  - MIN_DISCIPLINE retained (deployment-validity, not combat modifier)
- MECHANISMS that remain (correctly bottom-up):
  - support_engage_frac — depth-weighted cell support per atom
  - engagement_angle + ANGLE_DEF_MOD — facing-based flank/rear bonus
  - _momentum_speed puncture — speed differential at contact
  - count_engagements_per_atom + ENCIRCLEMENT_PENALTY — multi-attack penalty
- BATTERY RESULTS (in-band 9/13 at n=80; H3 confirmed 64.5% at n=200):
  IN-BAND (10/13 effective):
    H1 mirror 51.2% / H2 Wedge 55% / H3 Envelopment 64.5% (n=200) / H4 Cannae 51.2%
    H6 RF/Line 51.2% / H7 GL/Line 51.2% / H8 GL/Arrow 56.2% / H10 rev H3 43.8% / H11 rev H4
    R3 ranged mirror 47.5%
  OUT-OF-BAND (3/13):
    M  H5 RefusedFlank/Horseshoe 43.8% (was 82.5%) — real geometric Q for v11
    K  H9 Line/Arrowhead 56.2% — side-A bias structural (carry-over)
    L  R1 Pure Ranged/Line 90% — independent Phase 2 frequency (carry-over)
- TENSION J (asymmetric over-tune cluster) RESOLVED:
  H5/H6/H7/H8 dropped from 66-82% to 44-56%; H9/H10 from 62-66% to 43-56%.
  All driven by SHAPE_OFF_MOD removal and cell-count equalization.
- ARCHITECTURAL PRINCIPLE ESTABLISHED:
  Shape advantages emerge from cell arrangement (geometry) + already-present mechanisms.
  No flat per-shape dice bonuses. If wrong outcome, either fix geometry or add a real
  geometric mechanism. Forbidden: re-introducing top-down balance fudge.
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.
