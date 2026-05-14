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
| settlement_management | settlement_mgmt_stress_01 (in progress) | manifest committed; modules 1–13 pending | — | — | 🟡 Mode G Session 1 — manifest |

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

---

## SIM-MB-06 v11 (per-cell octagon angle)

- IN-BAND (10/13) at n=500:
  H1 Line mirror, H2 Arrowhead/Line, H3 Horseshoe/Line, H4 Horseshoe/Arrowhead,
  H6 RefusedFlank/Line, H8 GappedLine/Arrowhead, H9 Line/Arrowhead,
  H10 Line/Horseshoe, H11 Arrowhead/Horseshoe, R3 Ranged mirror
- OUT-OF-BAND (3/13):
    M  H5 RefusedFlank/Horseshoe 37.4% (target 50-65%) — unchanged from v10
    H7 GappedLine/Line 51.6% n=500 (borderline; confirmed in-band at n=500)
    L  R1 Pure Ranged/Line 69.4% (target 30-50%) — improved from 91% in v10
- KEY CHANGES from v10:
  Atom renamed Subunit; per-cell facing vectors; per-cell octagon angle model
  (GREEN<45=0D, YELLOW 45-90=-1D, RED>=90=-2D); attacker centroid used (not
  nearest cell) to avoid equidistant non-determinism. GappedLine gap skip removed
  (geometric). Ranged melee penalty pool//=2.
- OPEN TENSIONS CARRIED FORWARD:
    M  H5 RF/HS — targeting issue (GL blocks converge; per-block targets needed)
    L  R1 Ranged — pool//2 insufficient; needs heavier penalty or volley rebalance

## SIM-MB-06 v11 (2026-05-12, EXPLORATORY)
- ARCHITECTURE EXTENSION on v10's bottom-up principle.
- CHANGES:
  - Atom -> Subunit rename (terminology alignment with Unit/Subunit/Cell)
  - Per-cell octagon angle: each cell carries raw movement vector facing.
    GREEN<45deg=0D, YELLOW 45-90deg=-1D, RED>=90deg=-2D.
    Replaces centroid-to-centroid; _per_cell_angle_mod averages per side.
  - Vector halt-at-contact: halt_before_enemy() post-movement pullback when
    cell at distance 0 or at distance 1 with enemy in REAR zone.
    target_r = er - fr (one step before enemy in facing direction).
  - GappedLine gap skip removed: -99 sentinel deleted, geometry is mechanism.
    role_at_contact half_w sizes corrected to match v10 equalized pattern.
  - Ranged melee penalty: unit_type='ranged' in contact -> pool //= 2.
- BATTERY RESULTS (n=500): 10/13 in-band, matching v10 count
  IN-BAND (10/13):
    H1 51.6%, H3 60.2%, H4 46.4%, H6 57.2%, H7 51.6%, H8 50.8%,
    H9 45.2%, H10 36.6%, H11 49.0%, R3 45.8%
  OUT-OF-BAND (2/13) + borderline:
    M (H5): RefusedFlank/Horseshoe 37.4% — persistent from v10
    L (R1): Ranged/Line 69.4% — improved from 91% but volley still dominant
    Borderline H2: Arrow/Line 49.8% (0.2% below 50% floor)
- TENSIONS CARRIED FORWARD:
  - M (H5): RF cannot develop angle advantage before HS wings wrap.
    Likely needs RF wing-pivot or refused-cell defensive bonus.
  - L (R1): pool//2 halves melee but volley dominates. v12 options:
    pool//3, reduce VOLLEY_MAX_RANGE, increase target DR vs ranged.
  - H7 borderline: both GL blocks target shared centroid -> convergence
    closes gap. Needs per-subunit targeting (each block targets section).
- DRIFT RISK: octagon_angle / cell_facing_vec is new code; needs Jordan review
  before promotion from EXPLORATORY. Pool sensitivity empirical.
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v12 (2026-05-12, EXPLORATORY)
- BOTTOM-UP TENSION RESOLUTION building on v11 architecture.
- DIRECTIVE: keep working bottom up, ensure historical precedent results respected top down.
- CHANGES (5 mechanisms, each with documented historical precedent):
  1. Column-local targeting: each cell maintains its starting column, steers toward
     target row at that column. Replaces centroid-attractor convergence pathologies.
     Historical: infantry held assigned files; lateral drift = breakdown signal.
     Effect: GappedLine gaps stay open, Horseshoe wings preserve wide footprint,
     Arrowhead wedge tip leads naturally (cells already at different columns).
  2. VOLLEY_MAX_RANGE 25 -> 8: ranged units close to within 8 cells before firing.
     Crécy/Agincourt: killing zones were the final 100 paces (~5 cells).
  3. Ranged melee penalty pool//2 -> pool//3: archers in close combat were marginal.
     Agincourt 1415, Crécy 1346: archers contributed little to melee phase.
  4. Volley HP scaling: 1 size loss = ceil(h_per_size/2) hp, not full h_per_size.
     Ranged size loss = arrows finding targets (many glance off armor/shields);
     melee size loss = decisive wounds. This change ALONE moved R1 from 69% -> 35%.
  5. RefusedFlank front-row speed 2: engaged front rank charges at battle pace
     ahead of deeper rows. Leuctra 371 BC oblique order: Theban front struck first.
     Whole-column speed 2 over-tunes vs Line (H6); front-row-only is the partial
     bonus that helps vs wide formations (HS) without dominating same-width (Line).
- BATTERY RESULTS (n=500): 12/13 in-band (up from v11's 10/13)
  IN-BAND (12/13):
    H1 51.6%, H2 54.4%, H3 59.4%, H4 52.2%, H6 57.4%, H7 51.6%,
    H8 49.6%, H9 48.2%, H10 39.8%, H11 48.4%, R1 34.6%, R3 47.2%
  BORDERLINE OUT (1/13):
    H5 RefusedFlank vs Horseshoe: 47.4% (target 50-65%, 2.6% below floor)
- TENSIONS RESOLVED FROM v11:
  - R1 (Ranged vs Line): 69.4% -> 34.6% (in band, was M tension)
  - H7 (GappedLine vs Line): 51.6% maintained (was borderline)
  - H2 (Arrowhead vs Line): 49.8% -> 54.4% (was borderline, now solidly in band)
- TENSIONS CARRIED FORWARD:
  - H5 (RF vs HS): only 2.6% below floor, but persistent. Mechanism candidates
    tried (didn't all-clean-fix):
    * whole-column speed 2: H5=56.8% ✓ but H6=64.8% (broke H6)
    * front-2-rows speed 2: H5=52.2% ✓ but H6=64.0% (broke H6)
    * front-row speed 2 (CHOSEN): H5=47.4% (still out), H6=57.4% ✓
    * engage_frac cap 1.0 -> 1.5: regressed H2/H7
  - Likely needs geometry-aware mechanism distinguishing wider-than-me vs
    same-width-as-me opponents. v13 candidate: refused-stub repositioning,
    depth-ratio pool bonus, anti-wrap defensive mechanism.
- DRIFT RISK: 5 mechanisms layered atop v11 architecture. Volley HP scaling
  (change 4) is a canonical-rule modification — needs Jordan review before
  promotion from EXPLORATORY. Column-local targeting alters movement model.
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v13 (2026-05-12/13, EXPLORATORY)
- CROSS-SIDE CELL CONTENTION building on v12.
- DIRECTIVE: historical precedent informs behaviour, bottom-up build, top-down confirm.
- CHANGES (1 bottom-up mechanism, historically grounded):
  Cross-side cell contention (resolve_cross_side_contention). After both sides
  advance, cells from opposing sides may occupy the same abs position
  (over-run). v13 resolves: faster cell wins position; loser cells that moved
  this turn revert to pre-move snapshot. Tied speed = no movement resolution
  (combat decides via engagement).
- HISTORICAL GROUNDING:
  * Crécy 1346 / Agincourt 1415: English defenders pre-positioned via faster
    deployment; French halt at disadvantage. Speed-priority = first to ground.
  * Leuctra 371 BC: oblique order — strong wing faster, reaches enemy first.
  * Hoplite mirror: equal-speed disciplined formations resolve via combat
    (othismos), not movement priority. → tied-speed contests stay co-located.
- DEVIATION FROM JORDAN FULL SPEC:
  Full Jordan rule: speed → size → random tiebreakers + cavalry charge-through
  + end-of-phase displacement. v13 implements STRICT SPEED ONLY. Size/random
  tiebreakers omitted: they produce battery noise per-position per-turn in
  symmetric matchups without modelling anything historical (equal infantry
  formations don't resolve by random; they resolve by combat). Charge-through
  and end-of-phase displacement deferred — no cavalry in battery; framework
  scaffolded (snapshot, _moved_this_turn tracking) for v14+ cavalry wiring.
- WITHIN-SIDE DISCIPLINE-GATED FORMATION HOLD: implemented as
  Subunit.resolve_internal_collisions but NOT INVOKED. Earlier attempt broke
  battery (12/13 → 9/13). Reason: midpoint-of-two-forward-vectors is still
  forward, so the FAIL case has no effective penalty; only PASS revert worked,
  preferentially helping deep-column shapes (RF, Line) and hurting Arrowhead.
  Method retained in code for v14+ when paired with proper bad-facing trigger
  (e.g., wrap-around forcing perpendicular facings).
- BATTERY RESULTS (n=500): 12/13 in-band (same as v12)
  IN-BAND (12/13):
    H1 51.6%, H2 54.4%, H3 61.6%, H4 48.2%, H6 56.8%, H7 51.6%,
    H8 49.6%, H9 48.2%, H10 37.6%, H11 51.0%, R1 34.6%, R3 47.2%
  BORDERLINE OUT (1/13):
    H5 RefusedFlank vs Horseshoe: 47.4% (target 50-65%, 2.6% below floor)
- MECHANISM FIRING DIAGNOSTICS (50 battles/test):
    H1 Line-Line: 0.0/battle (tied speed-1)
    H2 Arrow-Line: 1.0/battle (Arrow tip speed-2 vs Line speed-1)
    H3 HS-Line: 14.0/battle (HS wings speed-2 sustained vs Line)
    H5 RF-HS: 0.0/battle (both have speed-2 components, tied)
    H6 RF-Line: 4.0/battle (RF front speed-2 vs Line speed-1)
    H7 GL-Line: 0.0/battle (both speed-1)
    H10 Line-HS: 8.0/battle (symmetric to H3)
  Mechanism does substantive work in asymmetric matchups; correctly silent in
  symmetric ones per historical model.
- TENSIONS CARRIED FORWARD:
  - H5 (RF vs HS): unchanged at 47.4%. Fundamental insight: H5 is NOT a
    co-location problem (which v13 resolves). HS wings extend PAST RF's
    footprint — wrap-around at columns RF doesn't occupy. Speed-priority is
    the wrong tool for wrap geometry.
  - v14 candidates: refused-stub repositioning, depth-ratio pool bonus when
    enemy extends past own footprint, anti-flanking defensive bonus for cells
    engaging outside-footprint enemies. Geometry-aware, not speed-aware.
- DRIFT RISK: 1 new mechanism, conservative implementation. Documented
  deviation from Jordan spec in code docstring and manifest. Charge-through
  framework partially scaffolded — future wiring must use existing primitives.
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v14 (2026-05-13, EXPLORATORY)
- PHASE/TICK STRUCTURE wired into simulation.
- DIRECTIVE: lock phase = gallop-and-charge cycle; provide structural hooks
  for stamina, rally, reform, threadwork, morale, rout that subsequent cycles
  will populate.
- CHANGES (1 structural addition, zero combat-mechanic changes):
  TICKS_PER_PHASE = 6. New phase_boundary(unit_a, unit_b, phase_idx) fires
  every 6 ticks in run_battle, calling 6 empty hook stubs in canonical order:
  stamina_check, morale_check_phase, rout_resolution, rally_check,
  reform_check, threadwork_check. Return dict from run_battle now includes
  'phases' and 'tick_in_phase' fields (additive — existing callers unaffected).
- HISTORICAL GROUNDING:
  * Operational Studies Group: "three-hex charge would take about 5 minutes
    in real time" (1 hex trot + 2 hex gallop). + 1-2 ticks reform-to-position
    for cycle-charging = 6 ticks total per phase.
  * Wikipedia cavalry tactics: charge acceleration 400m in 2 min + gallop
    last 150m + impact + disengage; matches the 6-tick budget.
  * Hoplite phalanx exhaustion bound: ~10-15 minutes of sustained close
    combat before exhaustion forces rotation/breakdown. Same 6-tick frame
    transfers to infantry (ephodos → krousis → doratismos → othismos →
    pararrhexis).
- TICK BUDGET WITHIN A PHASE (cavalry calibration):
  Tick 1-2: approach/closing (infantry braces)
  Tick 3: impact (gallop hits line, decisive puncture/break moment)
  Tick 4-5: contact resolution (melee in place if not broken through)
  Tick 6: disengage/reform (exploit/rout/withdrawal)
- WHY STRUCTURE BEFORE MECHANISM:
  Depth-as-replacement design started this session was reverted on research.
  Historical evidence: depth's real role is stamina-replacement (rear ranks
  rotate forward to refresh exhausted front-rankers), not casualty-replacement.
  That needs the stamina_check hook to exist. Wiring phase structure first
  gives subsequent mechanism work clean landing points.
- BATTERY RESULTS (n=500): 12/13 in-band (unchanged from v13)
  IN-BAND (12/13):
    H1 51.6%, H2 54.4%, H3 61.6%, H4 48.2%, H6 56.8%, H7 51.6%,
    H8 49.6%, H9 48.2%, H10 37.6%, H11 51.0%, R1 34.6%, R3 47.2%
  BORDERLINE OUT (1/13):
    H5 RefusedFlank vs Horseshoe: 47.4% (target 50-65%, 2.6% below floor)
- CARRIED FORWARD TO LATER CYCLES:
  - Stamina mechanism on stamina_check hook (depletion per contact tick,
    depth permits rotation to refresh, low stamina degrades combat pool)
  - Morale-from-casualty-threshold on morale_check_phase + rout_resolution
    (real battles end at 5-15% casualties via rout, not 100% destruction —
    this is expected to be the structural fix for H5)
  - Rally on rally_check (degraded units attempt recovery)
  - Reform on reform_check (formation drift correction)
  - Threadwork on threadwork_check (narrative/agent threadwork at phase seams)
  - Cavalry charge cycle and cycle-charging — built into phase structure;
    wires once cavalry units exist in battery
- DRIFT RISK: zero combat-behavior change. Hooks are explicit no-ops with
  noqa markers. Return-dict additive only.
- NOT YET PROPAGATED to canonical mechanics. ED-814 remains canonical.

## SIM-MB-06 v14 AUDIT (2026-05-13)
- AUDIT cycle following v14 phase-structure commit.
- ARTIFACTS:
  * tests/sim/instrument_battle.py — reusable tick-by-tick instrumentation tool.
    Patches v14 sim with verbose logging; renders markdown per-tick record.
    Captures per-cell position/speed/facing/halted, volley pending, pre-pairs,
    target assignment, advance deltas, cross-side contention firings,
    post-movement contacts, full pool decomposition, dice result, per-unit
    deltas, ASCII grid snapshot.
  * tests/sim/audit_record_v14_h5.md — H5 RF vs HS seed 1000000 (outstanding
    tension; B wins T8, RF routed at hp=2/20).
  * tests/sim/audit_record_v14_h1.md — H1 Line vs Line seed 1000000 (control
    mirror; B wins this seed, near-symmetric 51.6% A-wins across 500 seeds).
  * tests/sim/audit_sim_mb_06_v14.md — consolidated audit + NERS analysis.
    Compared against literal pre-firearms history AND acclaimed-videogame
    precedents (Total War Medieval II / Three Kingdoms / Attila, Field of
    Glory II, Battle Brothers, Mount & Blade Bannerlord). Every existing
    mechanism + every proposed gap scored against project NERS criteria.
- TOP-LEVEL FINDINGS (5 divergences):
  1. Per-tick lethality ~5-10x too high (sim tick-scale = historical phase-scale)
  2. No rout-at-casualty-threshold; battles run to ~100% destruction
  3. No stamina/exhaustion (THE limiting factor historically; universal in genre)
  4. No rest/recovery between contact periods
  5. Front-row-faster-than-rear-rank infantry speed is historically backwards
- GAP REGISTER:
  G-1 stamina, G-2 rout-at-threshold — HIGH priority, full NERS pass, PAIRED
  G-4 formation cohesion, G-5 per-cell nearest-attacker angle — MEDIUM
  G-6 unit-pace speed (replace per-row) — MEDIUM-HIGH (strict NERS improvement)
  G-7 rally — MEDIUM, completes rout/rally arc
  G-3 per-tick lethality recalibration — defer; falls out of G-1+G-2
  G-8 reform after withdrawal — defer until G-1/G-2 wired
  G-9 threadwork — needs design clarification from Jordan
  G-10 sarissa multi-rank projection — defer; subsumed by stamina
  G-11 cavalry mechanism — HIGH priority; BLOCKED on battery scope
- NEXT CYCLE: G-1 + G-2 paired implementation on existing phase-boundary hooks.
  Expected: H5 -> 50-65% as RF rotation advantage manifests through stamina
  mechanism; HS routs first at morale threshold.


## settlement_mgmt_stress_01 — manifest committed
- Date: 2026-05-13
- Scope: general validation, full simulations across settlement_layer_v30
  + supporting canon (political hierarchy, fractional ownership, scale
  transitions, faction layer)
- Mode: G (Incremental Build Protocol) — 13 modules total
- Status: manifest + empty ledger committed; Module 1 (settlement
  primitives) begins next session
- Decisions locked-in (5 defaults — overridable before Module 1):
  Mode-13 order A→B→C→D→batch; companion scope = settlement-side only;
  Module 11 stresses both canon 3-mode + videogame collapse; pre-13
  prior-sim mining session; stop = no unfixed P1/P2 + 50 seeds clean +
  full coverage

## duel_architecture_stress_01 — design + stress test committed
- Date: 2026-05-13
- Scope: Architecture C duel composite stress (E5 stance + E7 yield + canonical combat)
- Mode: A + B + D — 12-hypothesis Monte Carlo (N=5000)
- Status: committed; findings pending Jordan ratification
- Findings: E7 works; End too dominant [P2]; defense unrewarded [P2]; feint never optimal [P2]

## sim_mb_06_v15 — G-1 stamina + G-2 rout committed
- Date: 2026-05-13
- Scope: mass combat simulation v14→v15
- Mode: G (Incremental Build Protocol) — single module (stamina + rout on existing phase-boundary hooks)
- Status: committed; battery 11/13 in-band (v14 at same seeds: 10/13)
- Changes: stamina drain 16/contact-tick, recovery 8/reserve-rank at phase boundary,
  pool penalty -1 die at exhaustion only, phase-boundary morale check for exhausted+damaged units
- Findings: H5 RF-vs-HS fixed (47.4→50.2%). H7 GL-vs-Line regressed (51.6→49.4%, structural).
  0% rout rate — G-3 lethality reduction prerequisite for meaningful rout.
  G-3 does NOT fall out of G-1+G-2 (contradicts audit prediction).

## sim_mb_06_v16 — G-3 continuous effective_size + lethality recalibration committed
- Date: 2026-05-13
- Scope: mass combat simulation v15→v16
- Mode: G (Incremental Build Protocol) — architectural change + lethality recalibration
- Status: committed
- Changes: continuous effective_size (float, not floored); LETHALITY_SCALE=0.10 for ~15%
  casualties per 3-phase engagement turn; casualty-percentage morale triggers at 30%/50%;
  max_turns default 18 (3-phase cap per engagement turn)
- Architecture: 4-level zoom (Peninsula → Territory → Battlefield → Scene).
  Sim models Battlefield level. Multi-turn battle: 5-8 turns × 3 phases per engagement.
  Per-unit 25×21 grid (not shared). Adjacent allies join at one depth.
- Findings: multi-turn rout at ~33% cumulative casualties after 2 turns.
  Winner casualties ~23%, loser ~33%. 100% rout rate.
  H5 RF wins 75.5% in multi-turn (above target — depth stacking).
  Per-turn battery not meaningful at max_turns=18 (most matchups draw).
  Winner/loser ratio 1.4x (historical 2-5x — needs pursuit/cascade).

## audit_sim_mb_06_v16 — formula validation + gap detection
- Date: 2026-05-13
- Scope: v16 audit (Mode A + Mode D)
- Status: committed
- Findings: 10 gaps (0 P1, 6 P2, 4 P3). Pool formula validated across boundary values.
  Phase-boundary morale check redundant with per-tick triggers (D-7).
  Multi-turn orchestrator is priority for v17 (D-1, D-9).
