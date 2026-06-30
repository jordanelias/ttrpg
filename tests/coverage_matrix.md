# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md
## Targeting extensions (2026-06-05)
- `target_delay_ticks`: countdown hold before first engagement — staggered waves / ambush release
- `target_condition='weakest'`: focus-fire on fewest-remaining-troops enemy subunit, re-evaluates each tick
- `target_condition='in_range:N'`: hold until enemy centroid within N cells — defensive trigger
- `order_target_idx`: direct subunit-to-subunit targeting by index (pre-existing; now documented)
- Backward-compatible: neutral defaults preserve byte-exact prior behaviour
- Stress-tested: 0 engine failures / 0 degenerate across 60 targeting-varied + 30 backward-compat trials

## PC_NODE_COHESION continuous-path fix (2026-06-05)
- _node_advance: `_node_pos[(orig_r,orig_c)]` → `setdefault(key, anchor)`
- Continuous-mode cells not present in _node_pos at spawn now seed from anchor (first-time default)
- Verified: 20-trial fuzz with PC_NODE_COHESION=1 → 0 engine failures

## Discipline-speed flooring fix (2026-06-05)
- advance_cells + _node_advance: actual_speed used math.floor(base_speed * disc_mult);
  base_speed=1 (standard infantry) with disc_mult=0.7 (discipline 3-4) floored to 0 -> unit frozen.
- When both sides had discipline <5 neither could move -> false draw at 100%/100% troops.
- Changed floor -> round: discipline now slows (disc 3-4 move at speed 1) rather than freezing.
- Validated: historical counters byte-identical (deepColumn 5/8, ShieldWall 8/8, command 8/8);
  disc-3 two-Line engages 5/5 (was frozen); fuzz draw_hold 20->12 (frozen draws resolved); 0 engfail/degen.
- NOTE: this resolves what was mis-flagged as "GappedLine/Horseshoe non-closing" - that was never
  shape-specific; single-subunit shapes close at every parameter. The non-close was this speed cliff.

## Discipline decoupled from movement speed (2026-06-05, supersedes d869461c floor->round)
- CANONICAL BASIS: mass_battle_v30.md L7 — PP-232 renames Cohesion->Discipline. Discipline IS cohesion.
  Canon ties discipline to: Power penalty (A.4 table), degradation under Size-loss asymmetry, Reform
  restoration, the H formula. params/mass_combat.md has ZERO discipline x movement coupling.
- disc_mult on actual_speed/step was engine-introduced with no canonical basis. Removed.
- actual_speed = base_speed + stance_mod (advance_cells); step = base + stance_mod (_node_advance).
- disc_mult RETAINED where canonical (it = cohesion): node cohesion factor k (L632), wheel rate kw (L624).
- Validated: counters byte-identical (deepColumn 5/8, ShieldWall 8/8, command 8/8); disc 3-7 all engage;
  fuzz(120) 0 engfail/0 degen; mirror(60) |aw-bw|=6 symmetric.
- The earlier floor->round (d869461c) patched a coupling that should not exist; this removes it.

## reform_check (regroup) wired + directed maneuver pathing (2026-06-05)
- reform_check (G-8 hook, was empty): a unit NOT in melee contact restores +1 discipline toward
  discipline_start each phase boundary. [canonical: mass_battle_v30.md L180 reform restoration;
  discipline=cohesion PP-232]. Engaged = any subunit pair within Chebyshev REFORM_ENGAGE_DIST(=1).
- Maneuver pathing: units no longer always path straight at nearest.
  - Subunit.maneuver ('envelop'|'surge') + maneuver_side ('left'|'right'|auto). Also derived from
    instructions tokens ('envelop'/'surge'/'breakthrough'), so the Flanker (envelop) template is now live.
  - _maneuver_target: stateless per-tick pather (no path state to corrupt).
    * envelop: go wide past the enemy's nearer flank (col +/- MANEUVER_ENVELOP_WIDE=4), then hook
      inward to its flank/rear once the front row is passed (two-phase, geometric).
    * surge: break the line and drive MANEUVER_SURGE_DEPTH(=5) rows past the enemy front, holding column.
  - advance_cells branches on maneuver; the DEFAULT path (column-local + overhang wheel) is the
    else-branch, byte-exact for maneuver=None.
- Constants in orchestration.py, inline-cited; class-B sim-tunable (Jordan-vetoable). config.py NOT
  touched (its 10 pre-existing uncited constants are a separate hygiene item).
- Targeting granularity CONFIRMED unit->subunit->cell: unit = matchup + unit stance/disc/cmd;
  subunit = target selection (order_target_idx / target_condition / delay) + maneuver; cell = each cell
  independently computes its target (column-local / wheel / maneuver) and moves (genuine per-cell).
- Validation: counters 5/8 8/8 8/8 unchanged; fuzz(120) 0 engfail/0 degen; reform unengaged 3->4
  capped at start, engaged unchanged; envelop hooks flank (deepest row 17 vs direct 16), surge breaks
  a weak line and drives through (deepest row 10 vs direct 16). Fabrication gate: all constants cited.

## reform_check CANON CORRECTION: PP-241 command gate added (2026-06-05, fixes 8ec085c0)
- 8ec085c0 implemented only the L180 '+1 if unengaged' clause; MISSED the L180-183 command gate.
- Canon (mass_battle_v30.md L180-183): discipline restores only if general's Command >= current
  Discipline + 1 AND Command >= 2 (PP-241); Command=1 general cannot restore at all; command caps
  the reformable discipline (a Cmd-4 general restores a unit only up to disc 4).
- Added gate. Validated: cmd5/d3->4, cmd4/d3->4, cmd4/d4 no-change, cmd2/d3 + cmd1 no-change.
  Counters 5/8 8/8 8/8 unchanged; fuzz(120) 0 fail. [SELF-AUTHORED catch: reform implemented from the
  one-line L180 summary, not the full L180-183 - corrected on canon read.]

## Build A -- atomized fixing-force flank (subunit-scale)  [committed cb8b5844]
- orchestration.py `_per_cell_angle_mod`: detached-flank term fires when a subunit is fixed
  frontally by a SEPARATE body (`_front_fixers`) and the attacker bears on its flank/rear;
  provably inert single-subunit (byte-exact counters 5/8, 8/8, 8/8). Toggle `PC_FIXING_FLANK`.
- validators.py: V-CANNAE (envelopment advantage; no seed worse, delta>0) + V-FIXING
  (pin-conditional; zero effect without a front-fixer). Emergent, public outputs only.
- robustness: fuzz(120) 0 engine-failures / 0 degenerate; mirror skew 2/48.
- scope: A is the angle disadvantage (modest); decisive collapse = B; reliable rear-reach = C
  (a detachment approaching directly into the rear/flank forms no contact pair today).

## Build B -- envelopment shock (reuses _charge_shock_sigma)  [committed c2134e16]
- orchestration.py: PC_ENVELOP_SHOCK (default ON) fires the calibrated _charge_shock_sigma on the
  fixed_by_other + flank/rear condition, as an elif to the charge-shock path (no double-count).
  Reuses the existing zone/brace/depth/shaken gating: a braced+deep+disciplined line resists
  (Waterloo square), a loose/shaken/shallow one shatters (Cannae). Byte-exact (inert single-subunit);
  fuzz(120) 0 fail / 0 degen.
- validators.py: V-SHOCK (B decisive vs a balanced line: A+B retains +0.030 over A alone, no seed
  worse) + V-BRACE (braced unit resists; B-marginal braced 0.004 < line 0.030). V-CANNAE/V-FIXING
  now isolate A (shock off).
- scope: envelopment now decisive vs a vulnerable line via frontal-mass spillover; a detachment
  reaching the rear directly (no contact pair today) remains build C.

## Build C -- envelop maneuver (around the flank to the rear)  [committed 40fe9845]
- orchestration.py: PC_ENVELOP_PATH (default ON); envelop clause in advance_cells cell_target, gated by
  the 'envelop' instruction -> inert for every existing scenario -> byte-exact (5/8,8/8,8/8; fuzz(120)
  0 fail/0 degen). Two-phase: pass wide of the flank (clearance >= enemy frontage), then turn in to the
  now-rear cells. Reuses the existing 2D steering + wheel.
- validators.py: V-ENVELOP -- with the maneuver the detachment reaches the rear region (mean row-offset
  ~0, behind in 7/20 seeds) vs straight advance (+3.9, 0/20). Reaching the rear enables the RED rear shock.
- scope: routes reliably to the rear region; full per-seed rear lodgment is combat-dependent.


## Reform (G-8) -- Discipline restoration (reform_check)  [committed 2026-06-06]
- orchestration.py: REFORM_CHECK_ENABLED (env, default OFF). Flag kept in-engine (not config.py) to
  avoid the sim_fabrication ledger drift on config's pre-existing constants. reform_check filled per
  canon (mass_battle_v30.md §A.5 / Phase Reform): an unengaged unit (find_contacts empty) gains +1
  Discipline toward discipline_start, gated by Command >= Discipline+1 AND Command >= 2 (Command-
  asymmetry, PP-241); a Command of one cannot restore. Default OFF => byte-exact (lanchester
  signature byte-identical vs the original `pass`; the 5 envelopment validators unchanged, PER_CELL=1).
- validators.py: V-REFORM -- 7/7 gating cases (unengaged-eligible restores +1 capped at start;
  cmd=1 / cmd<disc+1 / already-at-start / engaged / routed / flag-OFF all inert). Toggles the flag
  in-process (save/restore) so it cannot perturb the other goals. run_all 6/6 PASS.
- NOT implemented (canon Reform also does these; separate, morale/lifecycle-touching): +1 Morale
  recovery and sub-unit merge. [OPEN -- Jordan: cadence is per phase-boundary (bounded by start);
  canon Reform is once-per-turn (the Reform Phase) -- may rule once-per-turn.]
- scope: discipline restoration only; flag-gated opt-in pending a re-baseline decision.

## Build E -- atomized archer volley targeting (directed concentrated fire)  [committed 2026-06-06]
- PC_VOLLEY_TARGETING (default ON): an ordered archer (order_target_idx / 'weakest' in-range; else
  nearest) concentrates its volley casualties on the target subunit (percell.apply_to_subunit); unordered
  fire spreads by engaged density as before -- same totals, cell==hp preserved. No-order path byte-exact
  (counters 5/8,8/8,8/8; default-volley probe identical to committed; fuzz(120) 0/0).
- validators.py: V-ARCHER -- ordered fire concentrates ~31.5 more casualties on target, every seed; 7/7 PASS.
- prior volley was faction-level (targeting cosmetic); E concentrates the ordered portion, default
  unchanged (opt-in, Jordan-vetoable). percell.apply_to_subunit added to __all__. 'sweep' half deferred.

## Build E (lateral half) -- sweep maneuver (flank-ward lateral march)  [committed 2026-06-06]
- orchestration.py: PC_SWEEP (default ON). advance_cells gains a 'sweep' clause (after envelop): a subunit
  with the 'sweep' instruction picks a flank at UNIT level (its deploy column vs enemy centre) and all cells
  shift laterally toward it (uniform sign -> formation coheres), then turn in to engage the flank frontally.
  Distinct from envelop (around to REAR) and the wheel (overhang cells only). Gated on the 'sweep' instruction
  -> INERT for every existing scenario -> byte-exact (counters 5/8,8/8,8/8; fuzz(60) 0 fail/0 degen).
- validators.py: V-SWEEP -- a 'sweep' unit displaces ~3.0 columns laterally to a flank vs ~0.08 for straight
  column-local advance, every seed; concentrates on the enemy flank (frontage chewed down). run_all 8/8 PASS.
- [ASSUMPTION] 'sweep' semantics (lateral flank-ward march then frontal flank engagement) are a grounded
  editorial reading -- the original E item named 'sweep' without a spec; anchored to oblique order / flank
  march (Leuctra, Leuthen). Class-B, Jordan-vetoable. An earlier per-cell-flank attempt tore the unit toward
  both flanks (centroid cancelled); fixed by the unit-level flank decision.

## Build D -- pin / Anvil  [CLOSED done-by-A, Jordan ruling 2026-06-06]
- RULING (Jordan 2026-06-06, Variant 3): D is delivered by the existing pin (`pinned` facing gate,
  orchestration.py L1508-1519) + build A (fixed_by_other, L1526) -- a pinned/fixed cell cannot reface, so the
  flank/rear angle penalty lands. No separate D mechanic is built; the anvil function = pin + A.
- Investigation (subsumption, this session): the obvious pin wirings measure 0.0000. `pinned` is read in
  exactly one place (the facing-refusal gate). Stamina drain is already contact-proportional (L210-211), so a
  'pinned drains harder' debuff double-counts. The one distinct lever -- denying the held enemy its
  between-turn stamina recovery (BETWEEN_TURN_STAMINA_RECOVERY, L2133) -- is called only in
  run_multi_turn_battle / run_multi_unit_battle (L2200, L2555), never in run_battle (L1898, the validated
  path) -> provably inert there. A single-battle pin debuff would over-punish an already-penalized state
  (A flank + B shock + contact drain) -> fails NERS-N.
- status: CLOSED. No code change. (Variants 1 recovery-denial / 2 cohesion-debuff remain available on a
  future canonical decision; not pursued.)
| r1_sigma_resolution + r8_parity_harness | F4 μ-shift resolution (base Ob + net_boost; eff_ob DISPLAY-ONLY) | mirror 49.9/50.0 · str6v4 59.5/40.5 · hist7v4 61.7/38.2 · agi6v4 65.6/34.4 (N=3000) · atom MC≡p_success | ED-934 | 2026-06-12 |

## Smooth command-sigma combat pool + continuous discipline penalty (2026-06-15, ED-1013)
- CANONICAL BASIS: Jordan directive 2026-06-15 'smooth pools / fix discipline' (path 1 of documented fork).
- base_combat_pool COMMAND_SIGMA branch: flat 2*Command -> Command*(1 + hp/hp_max) -- 2*Command at full
  strength (size-decoupled, ED-899 preserved; cohesion is a FRACTION so per-capita effectiveness stays
  size-independent, Lanchester exponent ~1), degrading smoothly to Command at annihilation.
- discipline_penalty(): tiers {0,-1,-2} -> continuous -(5-disc)/2 clamped [-2,0] (same endpoints, no step).
- WHY: the flat pool left the discipline STEP as the sole pool-degradation term, which amplified a tiny
  latent contact-geometry asymmetry into a side-B mirror bias (H1 62/38, |A-B|=21.7pp). The smooth
  own-casualty degradation dilutes the discipline term -> mirror side-symmetric.
- VALIDATED: H1 Line-Line mirror n=120 A=53%/B=47% decisive, |A-B|=3.3pp (was 21.7); command decisive
  (cmd6-vs-2 -> 40-0); discipline decisive (disc5-vs-disc2 -> 20-0); mechanics_selftest clean.
- COVERAGE IMPACT (Jordan-accepted trade-off): smooth pool reduces FORMATION/charge decisiveness; the
  historical gauge tests/sim/gauge_mb.py (precedents_warfare.md bands) is now STALE and needs
  RE-CALIBRATION to the smooth engine (in-band dropped flat 3/6 -> smooth 1/6 on the 6-test subset).
  FLAGGED as a separate Jordan-canon follow-up.

## 2026-06-15 — Mass-battle gauge recalibration (ED-1014) [resolves the ED-1013 gauge-staleness flag]
- tests/sim/gauge_mb.py recalibrated bottom-up from historical precedent + peer-reviewed academic military
  analysis (grounding doc: references/historical/mass_battle_gauge_grounding.md). Bands set by HISTORY, the
  engine validated against them -- a fail FLAGS engine divergence, it does not lower the band.
- METRIC: raw-A% -> DECISIVE SPLIT decA=A/(A+B) (raw-A% failed symmetric mirrors purely on draw rate); the
  draw rate is validated separately (draw_exp). Near-parity high-draw is analytically expected (Hillestad 1995
  NRL 42(2); Taylor 1979/1983; Lanchester tie Armstrong&Sodergren 2015).
- VALIDATION (smooth engine, multi, n=120): 9/20 VALIDATED (mirrors; envelopment foot+mounted C4 93.8%, C7
  86.7%; command-decisive; maniples-absorb-wedge; misconception-corrected C1 45.7%). 6 DIVERGE-soft (subtle
  formation edges washed by the ED-1013 cohesion pool -- defensible per Biddle/Burkholder, below the v9 A.6
  modest edge). 3 DIVERGE-hard ENGINE-DEFECT FLAGS left FAILING: C2/C6 braced foot never beats cavalry (brace
  under-repels); C5 morale-shock inert (decA identical to C1). R1 ranged too-drawish open-field; R3 ranged
  mirror unresolvable; single-mode all-draws (18-tick cap).
- C1 REBASELINE 52-80 -> 35-55: the old band encoded the cavalry-beats-unprepared-infantry misconception
  (Burkholder 2007). Engine-defect flags (frontal cav shock/brace/morale flat) are future-work, not bands.
- Jordan directive 2026-06-15 (bottom-up recalibration, repeated); Jordan-vetoable.

## 2026-06-16 — Mass-battle gauge cavalry construction fix (ED-1015) [corrects the ED-1014 C2/C5/C6 "engine-defect" flags]
- RE-DIAGNOSIS (bottom-up, reading mass_battle/resolution.py + orchestration.py + config.py): the 3 ED-1014
  DIVERGE-hard cavalry flags (C2/C5/C6) were NOT engine defects -- they were GAUGE-CONSTRUCTION defects. The
  engine's brace-recoil (PC_CHARGE_RECOIL, calibrated vs Courtrai/Swiss/Waterloo) and shaken-shock
  (PC_SHOCK_SHAKEN_GAIN) are already grounded + WIRED; the gauge was not triggering them. Engine UNTOUCHED.
- FIX (gauge only): make_unit gains morale_start=None + instructions=() with byte-exact defaults (the 13 H/R
  rows + C1/C3/C4/C7 unchanged; H1 identical 52.8). C2/C6 defenders carry instructions=('brace',) ->
  _unit_braced fires the reciprocal recoil -> the braced wall REPELS. C5 is morale 2 of morale_start 6 ->
  genuinely shaken ("shaken" is RELATIVE, du Picq) -> shaken-amplifier + _morale_sigma fire.
- METRIC: C2/C6 judged on RAW cav-a LOW (band 0-30), draws expected (a repulse is a HOLD; decisive-split
  saturates at a tiny decisive n). Optional 10th tuple field metric='rawA' added (default 'decA').
- BANDS (history-grounded, Jordan-vetoable): C5 ceiling 90->98 (cavalry vs disordered foot is NEAR-TOTAL --
  Boddy 2015 dispersed 15,000; Hastings post-feint; the Phase-2 ceiling was set when the shock was inert);
  C7 ceiling 90->100 (encirclement of an immobile hold-stance line is annihilating -- Cannae; decA saturates
  to 100 when infantry is shut out).
- VALIDATION (multi, n=120; C5 re-checked n=240): cavalry block 7/7 -- C1 contested 45.7 OK, C2 REPELLED (raw
  cav-a 1.7), C3 mirror 43.7 OK, C4 envelop 93.8 OK, C5 shaken 95.6 (94.8@n=240) OK, C6 REPELLED 1.7, C7
  envelop 100.0 OK. Differentiation EMERGENT: braced-repulse ~2% != contested ~46% != shaken-shock ~95% !=
  envelopment ~94-100% (this validates the ED-1014 C1 rebaseline by differentiation). gauge_mb.py: 0 uncited
  constants, mechanics_selftest (True,[]).
- LATENT FLAG (out of scope, not triggered): the charge-recoil (orchestration ~L1647) does not zone-gate -> a
  flank/rear charge into a braced unit wrongly fires the recoil; C7 uses hold-only to avoid it. Fix candidate:
  gate on the frontal (GREEN) zone. The 6 formation soft-divergences (H2/H4/H5/H6/H7/H9) remain a separate residual.
- Jordan directive 2026-06-16 ('for 1/2/3 do everything you can to fix everything from a bottom-up emergent
  approach'); implemented by Claude, Jordan-vetoable.
- ED-1016 (per-subunit stat derivation, Jordan directive 2026-06-16; per-subunit pool option 1, "intensive
  attention to detail"): pushed power/discipline/morale/morale_start/dr onto Subunit (OPTIONAL; None inherits
  parent Unit via _unit back-ref), added per-subunit cohesion + subunit_combat_pool (SHARED command, per-subunit
  discipline+cohesion, shared stamina), repointed the engagement pool + Lanchester casualty power/dr +
  charge-shock/brace-recoil/morale sigma + Phase-2 volley (power/discipline/eff_size) to the contacting subunit's
  effective stats; Unit derives agg_power/discipline/morale/dr (troop-weighted) atop existing HP=Size=Sum(subunits).
  BYTE-EXACT verified vs a CLEAN pre-edit engine across melee/cavalry/brace/morale AND ranged/volley (exact states +
  win-rates identical) -- single-subunit fast-paths (cohesion->hp/hp_max, eff_size->effective_size) + None-inheritance
  guarantee the homogeneous historical battery is untouched. Mixed-unit differentiation demonstrated: cavalry subunit
  P6/D6 pool 8 vs infantry subunit P4/D4 pool 7, carried into the combat trace. Added make_mixed_unit gauge constructor
  (make_unit unchanged). V1 SCOPE: per-subunit combat morale uses the subunit's nominal value for overriding subunits;
  the eroding morale pool + rout + discipline degradation stay UNIT-level. Implemented by Claude, Jordan-vetoable.
- ED-1017 (per-subunit stamina, Jordan directive 2026-06-17; mirrors ED-1016): pushed stamina onto Subunit as OPTIONAL
  fields (stamina/stamina_max; None inherits parent Unit via _unit back-ref), added eff_stamina/eff_stamina_max +
  drain_stamina/recover_stamina (write routing: own-if-set else inherited Unit -> single-subunit reproduces the old
  Unit.stamina arithmetic) + agg_stamina (troop-weighted). Repointed per-subunit: subunit_combat_pool penalty
  (atom.eff_stamina), base_combat_pool (self.agg_stamina), the per-tick contact drain (each engaged subunit drains by its
  own cells-in-contact; reserves do not drain), phase-boundary recovery (stamina_check via new per-subunit _subunit_depth),
  between-turn recovery, and the exhaustion-pressure morale read. _fatigue_sigma UNCHANGED (its call site already passes the
  engaged subunit's contact columns -> already sub-unit-scoped; an atom param would be unused apparatus, NERS-E). BYTE-EXACT
  vs a CLEAN pre-edit engine across 9 matchups (melee mirror/asymmetric/envelopment, ranged/volley, cavalry charge/braced/
  envelopment/shaken) x 20 seeds in the resolving multi-turn mode -- identical state-vector digest. Rotation demonstrated:
  an engaged front subunit drains to 32/100 while a held reserve stays 100/100 (divergence impossible under shared
  Unit.stamina); the fresh reserve yields +1 combat-pool die over the exhausted front. make_mixed_unit extended for
  per-subunit stamina (make_unit unchanged). Grounding (references/historical/mass_battle_gauge_grounding.md §6): Sabin 2000
  JRS line relief / supporting troops; Zhmodikov 2000 Historia; du Picq Battle Studies; Clausewitz On War III.12. V1 SCOPE:
  per-subunit rout + eroding morale/discipline stay UNIT-level (deferred, Jordan-vetoable). Implemented by Claude, Jordan-vetoable.
- ED-1018 (troop-taxonomy stat home, Jordan directive 2026-06-17): wired the troop taxonomy onto the per-subunit stats
  (ED-1016/ED-1017). Added orchestration.TROOP_TYPE_STATS -- canonical per-type Power/Discipline/Morale presets transcribed from
  mass_battle_v30 B.2, keyed to the existing TROOP_TYPE_ROLES snake_case taxonomy (levy, light_infantry, heavy_infantry,
  cavalry, archers, crossbow, sling, artillery, knights_templar) -- plus orchestration.stats_for(troop_type) (case-insensitive
  accessor mirroring roles_for; fresh dict or None) and the constructor Subunit.of_type(troop_type, shape, tier,
  starting_position, **kw), which fills power/discipline/morale/morale_start from the preset unless the caller overrides;
  an unknown type fills nothing so fields stay None and inherit the parent Unit. PURELY ADDITIVE: nothing that does not call
  of_type changes, so the gauge constructors (make_unit/make_mixed_unit) are untouched and single-subunit units stay
  BYTE-EXACT (9-matchup x 20-seed multi-turn battery digest unchanged: fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  SCOPE: only the three unambiguous B.2 integers are mapped; dr (the Armour column -> a vs-Piercing DR scale at orch L413-417
  whose identity with Subunit.dr is unconfirmed) and stamina (the Endur column, no clean bridge to the 0-100 pool) are
  deliberately left to inherit and flagged, not guessed; unit_type (melee vs ranged) stays caller-controlled (a role, not a
  stat). Differentiation demonstrated: of_type reproduces every B.2 row exactly; the stats separate combat on both channels --
  pool via discipline (Levy 6 dice -> Cavalry/Knights Templar 8) and damage via the (1+Power) multiplier (Levy x2 -> Cavalry
  x6); caller overrides beat the preset; unknown types inherit the Unit. Grounding (references/historical/
  mass_battle_gauge_grounding.md §7): the canonical B.2 table itself (bottom-up); Sabin Lost Battles 2007 validated
  ancient-battle model rating units by type and quality, plus the settled heavy/light/missile distinction (top-down).
  Implemented by Claude, Jordan-vetoable.
- ED-1019 (per-subunit rout + eroding morale/discipline, Jordan directive 2026-06-17 + "Continue" confirm; completes
  the per-subunit lifecycle after ED-1016 stats / ED-1017 stamina): pushed rout, morale erosion, and discipline
  degradation from the Unit onto the Subunit so a section of the line breaks from its OWN casualties while a fresh
  sibling holds. (SUBUNIT_ROUT_FLOOR was a dead config stub -- defined/exported/never referenced; this is the
  per-subunit rout it pointed at.) New Subunit fields routed/broken/discipline_start; props/methods eff_discipline_start,
  erode_morale, degrade_discipline, restore_discipline (write-routed own-else-inherited-Unit -> single-subunit
  reproduces the old unit arithmetic); Unit methods derive_rout + cascade_morale_hit. Repointed per-subunit:
  morale_check_phase (each subunit erodes by its OWN cohesion + own stamina/discipline exhaustion), rout_resolution
  (each subunit routs at own eff_morale<=0, then derive_rout), discipline_check_phase (unit-loss asymmetry drives a
  per-subunit counter), reform_check (flag OFF), the run-loop rout trigger, the per-tick drain (routed subunit skipped),
  subunit_combat_pool (routed/broken subunit -> 0), and the multi-unit inter-unit cascade / flank-erosion morale hits
  (cascade_morale_hit hits the unit's inherited-default morale ONCE plus each own-morale subunit -> no double-count on
  homogeneous units). TWO CANON-STRUCTURE FORKS, Jordan-vetoable: (a) unit-rout DERIVED (agg morale 0 / all subunits
  routed / Command<=0; winner/pursuit/cascade keep keying on derived unit.routed -> spec's unit-level rout preserved);
  (b) NO intra-unit cascade added (A.12 cascade stays inter-unit per spec, though its "section of the line breaks"
  Cannae/Hastings rationale could justify intra-unit -- a canon-model change left for Jordan). NO mass_battle_v30 edit.
  BYTE-EXACT: 9-matchup x 20-seed multi-turn battery digest unchanged (fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  Per-subunit rout demonstrated: a 2-subunit unit (heavy front + levy rear) with the rear gutted to ~18% eroded the
  rear's morale to 0 over 2 phases (cohesion 0.18 -> -2/phase) while the front held at 5.0 (cohesion 1.0); rout_resolution
  routed the rear only (rear.routed=True, front.routed=False, UNIT.routed=False -- line held), rear pool -> 0 while front
  kept 7 dice; breaking the front too routed the unit (derive_rout). Single-subunit routs exactly at morale 0 as before.
  Grounding (references/historical/mass_battle_gauge_grounding.md S8): A.12 Cannae/Hastings sectional collapse; du Picq
  Battle Studies (panic is local, spreads from a break). Implemented by Claude, Jordan-vetoable.

- **ED-1020** (bugfix -- per-subunit broken-state scope; ED-1019 follow-up). Per-subunit stress testing
  (tests/sim/mass_battle/test_persubunit_stress.py) caught subunit_combat_pool flagging the WHOLE unit broken when
  ONE sub-unit hit Discipline 0, whose top gate then zeroed every healthy sibling's pool -- an unintended intra-unit
  break cascade contradicting the canonized A.4 ('siblings fight on') and A.12 inter-unit-only cascade. Fix: the
  Discipline-0 gate sets atom.broken and promotes to unit.broken only when ALL sub-units are broken; single-subunit is
  the lone sub-unit broken => unit.broken (byte-exact, digest unchanged). Re-test: broken levy 0 while healthy heavy
  sibling fights and unit not broken; all broken -> unit.broken. Stress battery all pass. Found + fixed by Claude
  during the ED-1018/1019 NERS audit; Jordan-vetoable.

- **ED-1021** (simulation -- D-A personal-combat wound model: Spirit->Wound Interval, Strength->Health, health-based felling).
  Jordan-ratified (2026-06-18): add Spirit to the Wound Interval at low weight (WI = round(End + 4 + 0.4*Spirit);
  flat base 6->4, the 2 points reallocated into the Spirit/Strength terms so avg Health stays 40) and Strength to
  Health proportional to Endurance (Health = round(WI*(MaxWounds+1) + 0.25*Strength*End)). Felling switched from the
  wound-COUNT rule (>= MW+1 wounds) to health-depletion (cumulative damage >= Health) because the count rule made the
  Strength->Health buffer a verified no-op on outcomes (str7-v-4 0.877 ~ mirror); health-based felling makes Strength
  buy survivability. Validated (np.default_rng, MB=50): equal average chars fall in ~5.2 hits (target 4-6); mirror 0.516;
  Spirit now matters spi7-v-4 0.50->0.81; Strength holds str7-v-4 ~0.88; noise Health 37/40/43 (str1/4/7), WI 8/9/11
  (spi1/3/7). r2 self-test 7/7 PASS (Health-40 fixture held; WI 10->9). Pre-existing ~50% multi-bout mutual-stall noted
  (baseline too, not caused here). Isolated to personal combat (WI/Health unused by mass-battle). Implemented by Claude,
  Jordan-vetoable. derived_stats_v30 §4.1 propagation follows.

- **ED-1022** (bugfix -- roll-input fidelity). discipline_check_phase drove every sub-unit's Discipline from the
  UNIT's cumulative loss + unit-level asymmetry, so a fresh reserve sub-unit cracked from siblings' casualties. Now each
  sub-unit degrades from its OWN (start_troops-cur_troops) loss; single-sub-unit uses the exact (hp_max-hp) expression
  (byte-exact, digest unchanged). Asymmetry baseline stays the opposing UNIT (no per-sub-unit opponent in 1v1). Verified:
  a gutted sub-unit degrades while a fresh reserve sibling (unit loss 2.0) does not. Regression S11.
- **ED-1023** (simulation -- of_type wiring). make_mixed_unit now builds each sub-unit via Subunit.of_type, so a canonical
  troop type draws its B.2 presets (ED-1018 consumed -- closes the Part-2 wiring gap); only caller-set stat keys forwarded
  so the preset fills the rest, non-canonical 'infantry' inherits, override wins. Additive (no callers; bat.py unaffected).
  Regression S12.

- **ED-1024** (editorial -- ruling). Morale is CONTINUOUS in play (Jordan): B.2 starting values integer, erosion
  continuous. No engine change -- Morale is already float throughout; only the turn-LOG rounds (round(.,3)), no int()
  coercion. Resolves the Mode-B audit flag.
- **ED-1025** (simulation -- campaign-boundary reset). New reset_morale_between_battles(unit): resets unit + per-subunit
  own Morale to start and clears routed/broken (rout is derived from Morale, so the flags must clear); Discipline persists
  (PP-712). Uncalled within a battle -> byte-exact (digest unchanged); the campaign layer calls it at the battle boundary.
  Regression S13.

- **ED-1026** (simulation -- sweep fidelity findings 1-2). Two formation paths now read per-subunit Discipline:
  advance_cells (movement formation-hold; run_battle passed unit.discipline -> atom.eff_discipline) and Unit.check_drift
  (formation drift; self.discipline -> a.eff_discipline). Byte-exact single-subunit (digest unchanged). A low-Discipline
  subunit now advances slower and drifts to Line independently of disciplined siblings. Regression S14 (drift) + S15 (advance).

- **ED-1027** (simulation -- sweep findings 3-6 closeout). (3) recalc_size now propagates rout to subunits on
  destruction; (4) the inter-unit cascade denominator uses agg_discipline (per-subunit troop-weighted, == unit when
  homogeneous); (6) between_turn_recovery recovers per-subunit Morale (inert at RECOVERY=0); (5) deleted dead
  discipline_penalty_volley. Byte-exact single-subunit (digest unchanged). Regression S16 + S17 + S18.

## 2026-06-20 — Formation-drift cell orphaning fix (ED-1032) [DIGEST CHANGE — first since the per-subunit gauge baseline]
- FINDING (diagnosed bottom-up vs orchestration.py + percell.py this session): on formation drift to Line (Unit.check_drift, L1368) cell_troops was not re-keyed to the new shape's pattern. ~42% of a drifted sub-unit's troops (157/376 in test) became spatially orphaned -- counted in HP (sum(cell_troops)==hp held, so strength/pool stayed correct) but invisible to iter_cells AND inert to front-cell casualty distribution (the orphaned wing never bled, held no frontage, could not be enveloped). Violates ED-907's "each cell inherits the best execution".
- FIX (orchestration.py check_drift): on drift, total=sum(cell_troops); shape="Line"; re-key cell_troops to _oriented(a)'s Line pattern with uniform per=total/len(new_ids), mirroring spawn (L629). Preserves total strength; restores the full cell complement.
- VALIDATION: test_persubunit_stress S1-S18 ALL PASS (no property regression); drifted unit final orphan=0.00 with HP preserved; no committed golden-digest test (digest asserted only by local bat.py).
- DIGEST CHANGE (intended, first since baseline): fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69 -> 1f8c05a9748d0b29c35a3acbd5e87d8f7112e159513cd3782af4f781a7cee05e. The fix deliberately alters drift-scenario outcomes (re-keyed casualties spread over the full Line, not the shared spine); IDENTICAL for any sub-unit that does not drift (reassignment is inside the drift branch). Jordan-approved adoption 2026-06-20.

## 2026-06-20 — base_combat_pool comment alignment + PP-683 framing (byte-exact; defect cleanup)
- orchestration.py base_combat_pool: the [canonical:] comment cited the legacy min(Size,Command)+Command; updated to the live Command*(1+cohesion) (ED-899/ED-1013), consistent with the now-propagated §A.4. Comment-only -> byte-exact (gauge digest 1f8c05a9 unchanged).
- PP-683 (encirclement -3 morale-cap removal) intentionally NOT wired: the engine delivers encirclement via PC_ENVELOP_SHOCK + Lanchester contact-overlap; a second cap-removal term double-counts and breaks H4 Cannae (same reason _envelopment_sigma is held dormant, NERS-N/E: no unneeded apparatus). The -3 cap (L314 min(loss,3.0)) stays in force; encirclement lethality is the shock + overlap. Doc PP-683 note added in the matching editorial commit.

## 2026-06-30 — Mass-battle bottom-up audit: provenance registry seed (ED-1043) [additive, data-only, byte-exact]
- ADDED `tests/sim/mass_battle/provenance.py`: a primitive-provenance registry SEED (the `Prov` schema +
  `PROVENANCE` rows for the 9 anti-pattern findings F1-F9 + the 3 grounded laws). Pure data record — it does
  NOT import or touch the engine, so the gauge digest is UNCHANGED (byte-exact). All `value` fields are stored
  as strings (a record of a constant, not a live constant), so it adds no mechanical literal to the engine.
- PURPOSE: machine-readable grounding tier per constant (derived / academic-law / historical / calibrated /
  ungrounded), enforcing the "no asserted value" bar. Seed counts: 3 academic-law, calibrated + ungrounded =
  the retirement worklist (target zero). Audit: `designs/audit/2026-06-30-massbattle-bottomup/`.
- NO regression test (data-only, no behavior); CI cross-check (provenance pass on ci_sim_fabrication_check)
  is roadmap Stage 0/5, not this pass.
