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