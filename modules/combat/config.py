"""CFG holds the tunable coefficients of the resolution systems (seeds), Class-C — calibrated against the harness, not canon. It is NOT the only home of a constant: `core.py` holds the resolution/damage/armour constants and tables, `weapon_physics.py` the physical anchors (`PERC_*`, `GRIP_*`, `HEFT_REF`, ...), `combatant.py` the wound and stamina model, and `ability_primitives.py` and `traditions.py` the ability and tradition tables; `tools/export_engine_params.py` exports every one of those to its own section."""
CFG = dict(
  # reach (continuous, derived from weapon vector)
  L0=4.0,   # live reach_base anchor (reach is geometry-derived; head is a primitive, not a categorical reach table).

  REACH_DISADV_K=0.22, FOOT_MEASURE_K=0.15,   # reach advantage is carried by REACH_FRAC/REACH_W in systems.reach_sigma.
  # reach DERIVED from geometry.
  # reach_base = L0 + REACH_GEOM_SCALE*(head_len + REACH_2H_K*grip_len*[2H]) + reach_adj. SCALE [SIM-CALIBRATE] fit so
  # the spread maps onto the 4.5-7.8 band (spear longest, dagger shortest); a centre-gripped pole reaches less than
  # a butt-gripped one BY CONSTRUCTION (the grip insight).
  # U0 (ED-PC-0002): head_len/grip_len are METRES (0.635 reach-pt per 0.30 m). reach_adj stays a SMALL
  # per-weapon residual in reach-POINTS (the same unit as reach_base's output, added OUTSIDE the geometric
  # scale) — it is not a stored length and is deliberately NOT rescaled.
  REACH_GEOM_SCALE=0.635/0.30, REACH_2H_K=0.4,
  # reach as a standing per-exchange advantage (reference structure): keep most of the gap, weight it high
  # unarmoured and let it FALL with armour (the reach->clinch rotation). Tuned so reach governs A0 across the roster.
  REACH_FRAC=0.82,
  REACH_W={'none':0.62,'light':0.50,'medium':0.34,'heavy':0.20},
  # heavy-weapon viability: bound the stacked weight+2H tempo penalty so a poleaxe can act (not 7x slower)
  MAX_TEMPO_PEN=0.8, TEMPO_FLOOR=0.7, REOPEN_K=0.34, REOPEN_MAX=0.6, CLOSE_TEMPO_MEAN=1.5, CLOSE_TEMPO_COMPRESS=0.38,
  PUSH_AVAIL_P=0.22, PUSH_REOPEN_BONUS=0.18,
  # PROACTIVE FIGHTING WITHDRAWAL (ED-PC-0030): a reach weapon out-leveraged in the bind refuses it, breaks measure,
  # and re-presents its point at its dominant measure (Silver's staff/spear game) — the closed-phase lever for the
  # reach-weapon-loses-the-bind residual. VOLUNTARY (any beat, unlike the created-moment reopen) + read-contested;
  # a failed/read withdrawal is PURSUED (Nachreisen). systems.disengage_attempt_p / systems.disengage_clean_p gate it EMERGENTLY on the bind
  # leverage deficit (a bind-dominant poleaxe never triggers). [SIM-CALIBRATE] magnitudes; the structure is grounded.
  DISENGAGE_BASE_P=0.5, DISENGAGE_MAX=0.5, DISENGAGE_GAP_REF=3.0, DISENGAGE_LEV_SCALE=0.1, DISENGAGE_PURSUIT_NSIG=-0.3, PURSUIT_FOOT_K=0.15,
  # DISENGAGE_PURSUIT_NSIG is the BASE ANCHOR of systems.pursuit_sigma (catching a withdrawing opponent is hard),
  # not the whole resolution (ED-PC-0036).
  # PURSUIT_FOOT_K weights the footwork differential that decides the chase (Nachreisen = "travelling after"); scaled to
  # match FOOT_MEASURE_K, the engine's other footwork-into-sigma term. [SIM-CALIBRATE]
  # conditional tempo (correction 2): fatigue slows cadence; choke/lunge grips trade cadence for control/reach
  TEMPO_FATIGUE_K=0.25, CHOKE_TEMPO_PEN=0.4, LUNGE_TEMPO_PEN=0.6,
  # movement legibility (correction 4): swings/lunges easy to read (lateral, large); thrusts hard (in-line)
  LEGIB_SWING=1.25, LEGIB_THRUST=0.80, LEGIB_COMMIT_K=0.10, LEGIB_LUNGE=0.25,
  # a feathered/tasselled/ringed weapon's ornament motion adds visual clutter that
  # degrades the defender's read regardless of the attack's own mode legibility. [SIM-CALIBRATE] — the 3 roster
  # weapons with attested adornments (ranseur/guandao/jian) are period-documented as ceremonial-phase features,
  # so this is deliberately a SMALL knock, not a primary legibility axis. See weapon_physics.distraction().
  LEGIB_DISTRACT_K=0.15,
  # U3/ED-PC-0018 edges primitive — the three edge-effect channels (§2.3, one channel per physical fact), small
  # GROUNDED baselines (U10/ED-PC-0022). No lever robustly moves aggregate FIELD winrate — correct, because flat
  # physics cancels in a mirror-ish field. Efficacy BEYOND rote physics comes from
  # the TRADITION-MODULATION SURFACE: each lever is routed through ability_primitives.ability_factor(c, <channel>),
  # so a school that specializes in a lever amplifies it into a SITUATIONALLY-DECISIVE edge without distorting field
  # balance. Channels: edge_lines->'edge_read' (legibility), spine->'spine_press' (bind), grab_hazard->'edge_grab'
  # (contact). BASELINE MAGNITUDES [SIM-CALIBRATE] set so the physics is live but the field spread stays within the
  # ~±4pp harness noise floor; the invested ability multipliers (shinogi/ringen — the two morphology-lever abilities whose HEMA grounding held, ED-PC-0026) carry the decisive weight.
  #   LEGIB_EDGELINE_K: a double/false edge's return-cut ambiguity degrades the defender's read (weapon_physics.edge_lines
  #     -> legibility, same sign as LEGIB_DISTRACT_K); BIND_SPINE_K: a single edge's rigid spine wins the bind bearing-
  #     surface (weapon_physics.spine differential -> bind_sigma); GRAB_EDGE_K: a live edge self-injures an unskilled
  #     bare-hand grab (weapon_physics.grab_hazard -> contact.grab_sigma). See weapon_physics.py's U3 block + §2.3.
  LEGIB_EDGELINE_K=0.04,
  # U5/ED-PC-0019 polearm choke counterbalance: CHOKE_ACCURACY_K — a head-heavy pole choked up to counterbalance loses
  # fine precision -> reads easier (systems.choke_counterbalance -> legibility). U10/ED-PC-0022. This is
  # the SOLE choke-cost channel (the D2 force-invariant keeps the thrust force grip-invariant — see
  # weapon_physics.py). Modulated by ability_factor(c,'choke_control') (a
  # pole tradition gathers without telegraphing — mitigates; default 1.0). CHOKE_RC_REF — pole-class rear_clearance
  # reference the choke normalises by (poleaxe-class ~0.9).
  CHOKE_ACCURACY_K=0.03, CHOKE_RC_REF=0.9,
  # U7/ED-PC-0020 weapon-class-aware facing: FACING_REGIME_K — scales the signed facing regime (weapon_physics.facing_pref:
  # 1H profile / 2H square) multiplicatively in systems.facing_target, modulated by ability_factor(c,'facing_regime').
  # U10/ED-PC-0022, a CONSERVATIVE 0.12: the C2 REGIME (1H-profile vs 2H-square) is Jordan-resolved and
  # live (facing reads weapon class), but C1 (absolute polearm facing DIRECTION) stays unresolved, so facing must not
  # become load-bearing — the K stays modest and its consumers (FACING_VOID_K/FACING_PROFILE_K) stay small by design.
  FACING_REGIME_K=0.12,
  # lever-arm primitive: redirect/bind capacity from an EXPLICIT hand-to-contact lever arm = grip_len − LEVER_HEAD_K·head_len
  # Structure grounded; magnitudes [SIM-CALIBRATE] (fit the bind win-rate in the re-baseline). LEVER_REF = a 1H sword's net lever.
  # U0 (ED-PC-0002): lever lengths are METRES — LEVER_K is a per-metre gain, LEVER_REF a stored length;
  # LEVER_HEAD_K/LEVER_2H are dimensionless.
  LEVER_K=0.22/0.30, LEVER_HEAD_K=0.2, LEVER_REF=0.096, LEVER_2H=0.20,
  # displace-and-step-inside vs a committed thrust (needs leverage edge + winning the read)
  DISPLACE_LEV_GAP=0.15, DISPLACE_P=0.55, DISPLACE_PULLBACK_GRAZE=0.30, APPROACH_DISPLACE_K=0.7, APPROACH_DISPLACE_MAX=0.6,
  # hilt/guard primitive: blade_guard (cross/quillons/rings) catches the blade in the bind & enhances winding;
  # hand_guard protects the hand in the parry ("don't parry with your hands"). Modulated around a neutral cross.
  BIND_GUARD_K=0.55, PARRY_GUARD_K=0.45, WIND_GUARD_K=0.40, GUARD_NEUTRAL=0.45,
  ADEF_W={'none':0.0,'light':0.4,'medium':1.0,'heavy':1.7}, ADEF_BLUNT=1.3, ADEF_POINT=1.2, ADEF_CUT=-0.9,   # ADEF_POINT [SIM-CALIBRATE, reach-ladder frame; ED-1080]: the gap-thrust is a strong armour-defeater (the reliable armoured KILL — Le Jeu de la Hache / Harnischfechten), so a SELECTED spike's exchange-CONTROL (armor_defeat_sigma) now matches its DAMAGE — unifying the sigma path with the gap-game damage path (the adef-consistency lever). NOT parity with the hammer (ED-PC-0049): the spike ('point') reads ~0.78 of the hammer ('blunt') on the poleaxe record (grip 0) and still clears ADEF_THRESHOLD['heavy'] (0.72); nothing requires parity, and buying it (ADEF_POINT ~1.53) would re-baseline every selected point.
  ADEF_PERC_REF=8.0,   # [SIM-CALIBRATE] derived-percussion-authority reference (a steel hammer ~8) for blunt armour-defeat.
  # LOCKED TO weapon_physics.PERC_CAP (ED-PC-0042 rider I1b) — adef_cap's blunt branch divides a percussion_authority,
  # which is CLAMPED at PERC_CAP, by this seed, so it is not an independent tunable: it is the same scale top, and the
  # deferred Phase-C PERC_SCALE/PERC_EXP re-fit must move both. It is NOT bound by import, unlike core.PERC_AUTH_REF,
  # for two reasons: config.py is a deliberate zero-import seeds leaf (importing the physics module here inverts the
  # layering, data <- behaviour), and CFG is per-run OVERRIDABLE (workbench/presets.py deep-copies + overlays it,
  # tests write `dict(CFG, K=...)`), so an import-time binding would be a FALSE single-ownership any overlay silently
  # breaks. The equality is held instead by a guard:
  # tests/valoria/test_combat_invariants.py::test_percussion_anchor_has_one_owner. Change PERC_CAP, change this.
  # FIX-1 (reach-threat decay): a long weapon that CANNOT defeat the closer's armour loses its reach/approach edge —
  # the armoured man walks through a threat that can't hurt him. Derived from adef_cap vs the tier threshold; 0-effect
  # unarmoured by construction. REACH_DECAY_K [FIAT — designer-set; deliberately LOW to avoid triple-counting REACH_W
  # + ADEF_CUT, which already remove most cut-vs-plate reach value]. FLOOR keeps a residual (an armoured man still works to close).
  REACH_DECAY_K=0.35, REACH_THREAT_FLOOR=0.35,
  REPRESENT_DECAY_K=3.5, REPRESENT_FOOT_K=0.06,   # ED-PC-0033: represent_measure_p armour-fade — P(a reach weapon re-presents at open measure entering a fresh engagement) = exp(-DECAY_K·ADEF_W·armour_defeat_deficit)·footwork. DECAY_K steeper than reach_threat's REACH_DECAY (holding an armoured man off a whole engagement is harder than deterring one stop-hit); crowds a PURE POINT off plate while a gap-defeating reach weapon still presents. FOOT_K small — armour dominates, Agility only nudges (0 for a stat mirror). [SIM-CALIBRATE]
  ADEF_THRESHOLD={'none':0.0,'light':0.30,'medium':0.45,'heavy':0.72},   # MONOTONE (ED-1050, Jordan 2026-06-30): the armour-defeat threshold RISES with armour — a gambeson (light) is soft/easily defeated, mail (medium) harder, plate (heavy) hardest (systems.armor_defeat_sigma's docstring forbids an inversion). [SIM-CALIBRATE] values within the grounded monotone frame; validated (mirror-50, light matchups sane).
  # STRUCTURAL THRESHOLD SOFTENING (ED-PC-0037) — the two discontinuities the four-dimension audit found dominating
  # the whole balance surface, making win-rate nearly a STEP FUNCTION of which side of a line a weapon fell on.
  # INIT_TEMPO_K / READ_TEMPO_K: the ANTICIPATION half of "who acts first" (systems.tempo_pressure). Weapon cadence
  #   alone used to decide it, metronomically and therefore deterministically. These make the Vor (initiative) and the
  #   READ modulate how fast a fighter's next action comes to bear — you begin as your opponent begins because you
  #   anticipated them, and you keep dictating because you took the Vor. Both 0 restores cadence-only behaviour.
  #   Deliberately NOT noise: an unexplained random term would answer the right objection with the wrong mechanism.
  # CLOSE_GAP_REF / CLOSE_LATCH_BAND: the engagement-start closed latch is a probabilistic ramp across REF +- BAND
  #   instead of a hard step at REF (worth +9pp across 2 cm of reach). BAND 0 restores the step.
  # All [SIM-CALIBRATE]; the STRUCTURE (a threshold should not be a cliff; cadence proposes, the Vor and read dispose)
  # is the grounded part.
  INIT_TEMPO_K=0.30, READ_TEMPO_K=0.05, CLOSE_GAP_REF=0.3, CLOSE_LATCH_BAND=0.3,
  CLOSE_RATE_K=0.40, STOPHIT_CHANCE=0.75, STOPHIT_FULL_GAP=3.0, ARREST_K=0.12, ARREST_REACH_FLOOR=5.0,   # ARREST_K/ARREST_REACH_FLOOR (ED-PC-0029): a LANDED stop-thrust checks the closer's advance by the braced-weapon IMPULSE it transmits (systems.arrest_impulse = K·(reach−FLOOR)·braceability), netted against close_rate. This is an ARREST, not a wound — a braced point halts a charge whether or not it penetrates (boar-spear lugs: penetration≠arrest), so it reads reach+structure, never damage. FLOOR (~arm+dagger length) zeroes a dagger's arrest — nothing to brace against a charge at grappling distance. Armour enters ONCE, via reach_threat in the stop-hit's landing prob. Grounded in HEMA Nachreisen. [SIM-CALIBRATE]
  # tempo
  BASE_TEMPO=2.0, TEMPO_RECOVER_K=0.4, TEMPO_RECOVER_SHAPE=0.35, AGI_TEMPO_K=0.03, WEIGHT_PEN=0.8, HANDS_COMMIT=0.5, ACT_THRESHOLD=2.5, BURST_MAX=4,   # TEMPO_RECOVER_K/_SHAPE: scales systems._recovery_mode_commitment's grip-aware balance-recovery delta from the anchor (tanh-saturating — the raw commitment spans ~0.2 to ~68 across the roster). [SIM-CALIBRATE] both. AGI_TEMPO_K: athleticism adds a little cadence (Jordan 2026-06-04, centred at agi 4; 0.03 = modest). BURST_MAX: the per-round exchange cap (A-101: the 4-10 s band is an indicator of this cap, not a clock); 1-~4
  # stamina / recovery
  STAMINA_REF=18.0, RECOVERY_FRAC=0.5, COST_SCALE=0.5, ACT_BASE=2.0, ACT_WEIGHT=1.0, ACT_COMMIT=0.4, OOB=2,
  ARMOR_DEMAND={'none':0.0,'light':5/3,'medium':10/3,'heavy':5.0},   # PC-20 (3), AR-10 (adj §3.1 (8)): the Strength a harness demands, per tier, in Strength points (str_demand's unit). systems.act_cost charges max(0, demand - strength) at ACT_WEIGHT/D_WT stamina per point (handling_penalty's form, priced as a unit of weapon heft), so an armoured weak fighter tires faster than an unarmoured one and a fighter at or over the demand pays nothing. [SIM-CALIBRATE; ASSUMPTION; medium; Jordan to correct; revert: every tier 0.0, the control, which reproduces the PC-20 (2) tree.] RULE: an even ladder over the ordinal tiers (light TOP/3, medium 2TOP/3, heavy TOP; 'none' 0), TOP the middle grid member of the range over which (a) every armoured tier is a Strength job for some fighter on the 1-7 scale (light > 1: the weakest is short of a gambeson), (b) the strongest bears plate free (heavy <= 7: above it plate is a flat tax on everyone), and (c) ED-1040's observable (str-2 greatsword mirror draw rate, n=3000) and every matchup family's pooled draw rate (weapon n=1000/weapon vs arming, attribute n=3000, tradition n=500/pair; balance.winrate, PYTHONHASHSEED=0) stay inside their TOP=0 Wilson 95% intervals. The draw bound does NOT bite (the families fight at Strength 4 in light armour, which no TOP <= 7 makes short), so (a) and (b) bound the range (3, 7]; its midpoint 5 is a grid member and ships.
  # concentration (Focus+Spirit tracker; baseline-consistency + fatigue-resistance)
  CONC_SPIRIT=2.0, CONC_FOCUS=3.0, CONC_DRAIN_BOUT=3.0, CONC_DRAIN_LOSS=2.0, CONC_DRAIN_HIT=2.0,   # Concentration = 3*Focus + 2*Spirit (Jordan 2026-06-03)
  CONC_RECOVER_FRAC=0.4, FOCUS_MENTAL_K=0.5, FOCUS_CONSISTENCY_K=0.10,
  # reading / tempo channels
  READ_K=0.5, REFLEX_AGI=2.0, REFLEX_ATT=1.0, INIT_K=0.045, COMMIT_SIGMA=0.18,
    WOUND_ATK_OB=0.15, WOUND_DEF_OB=0.25,   # ED-1041 wound obstacle (bilateral, tunable): +0.15 Ob attacking / +0.25 Ob defending per wound; supersedes the -1D aggressor-only pool penalty (ED-1021). Defender has no pool, so defence-impairment must be an Ob channel.
  AGI_READ_K=0.2,   # PC-18 (2), ED-IN-0347: the attack's suddenness is Coordination — systems.read_contest's aggressor side adds AGI_READ_K*(agi-NEUTRAL['agi']) to his reading value, inside the visual factor (0 at agi 4: a default aggressor is unchanged at any K). [SIM-CALIBRATE] chosen on the workbench (balance.winrate, FINAL_TRIALS, Wilson z) over the grid 0, .05, .1, .15, .2, .3, .5 as the largest value at which both Coordination mirrors (agi 6 and agi 2) hold 50% inside their 95% interval, the defender's p_read strictly falls in the aggressor's agi 1..7, and the lever sign-safety probes stay live (att + K*(agi-4) must stay > 0 on the 1-7 scale, K < 1/3), and 0.3's agi-6 mirror read 48.2% [46.4, 49.98]. 0.0 ablates the term (the control). LIMIT: criterion (a) cannot observe K (a Coordination mirror of identical builds under the position-swapped winrate is 50% by construction) and (b) holds at every K > 0 (read_a is linear and increasing in agi), so the pick of 0.2 over 0.3 rests on (c) and one marginal interval: a structural choice, not a measurement. [ASSUMPTION; medium; Jordan to correct; revert: AGI_READ_K = 0.]
  LAPSE_K=0.05,   # PC-19, ED-IN-0347: Focus between the read and the response — systems.mode_sigma adds LAPSE_K*consistency(defender) before the mode's affinity cap. consistency() is FOCUS_CONSISTENCY_K*(conc/5-3), 0 at full reserve (3F+2S = 15), NEGATIVE once the reserve is drained, so K > 0 lowers a drained defender's response and leaves a fresh one's alone. [SIM-CALIBRATE] chosen on the workbench over the grid 0, .02, .05, .1, .15, .2, .3 as the middle grid member of the range (.02 to .1) over which (a) a drained defender's chosen-mode sigma falls monotonically and (b) no matchup family's pooled draw rate leaves its K=0 Wilson 95% interval. The term is small: FOCUS_CONSISTENCY_K is 0.1, so the whole range is about -0.015..+0.02, below what the draw arm can separate from noise, so this value is a grid member of a structural range and not a measurement; PC-22 retires this key into one Concentration function. [ASSUMPTION; medium; Jordan to correct; revert: LAPSE_K = 0.] 0.0 ablates the term (the control).
  INIT_READING_K=0.03,   # initiative reading term (Jordan 2026-06-03; Class-C)
  INIT_TEMPO_LEVER_K=0.03,   # PC-17 / ED-PC-0059: weight of the 'tempo' ability lever in systems.init_emphasis_sigma, ADDED as K*lever_log_edge(f_aggressor, f_defender) (exactly 0 at default builds). Set equal to INIT_READING_K, so one unit of log-tempo edge weighs what one point of reading difference does: a x1.5 generic at level 1 adds log(1.5)*K = 0.012 sigma, at level 8 about 0.097. [SIM-CALIBRATE]
  # defense modes
  PARRY_K=0.9, DODGE_K=0.9, WIND_K=0.9,   # A gathered grip does not aid the wind here (grip is the continuous grip_position); if wanted it must be DESIGNED against a double-count check vs systems.leverage (bind capacity) and CHOKE_ACCURACY_K (the choke cost, ED-PC-0026).
  # strength handling + endurance fatigue
  D0=1.0, D_LEN=0.35, D_WT=1.0, D_HAND=0.6, D_2H=0.4, HANDLE_K=0.10,
  D_MASS=0.45,   # PC-20 (2), AR-12 ("weight itself", beside "managing heft"): systems.str_demand adds D_MASS*mass (kg), so a heavier weapon of EQUAL inertia (wield_heft) handles worse for a fighter short of its demand; a fighter clear of it pays nothing. [SIM-CALIBRATE; ASSUMPTION; medium; Jordan to correct; revert: 0.0, the control, which reproduces the PC-20 (1) tree.] RULE: the middle grid member of the range over which (a) the exit holds and (b) ED-1040's observable (str-2 greatsword mirror draw rate, n=3000) and every matchup family's pooled draw rate (PC-19 (2)'s instrument: weapon n=1000/weapon vs arming, attribute n=3000, tradition n=500/pair; workbench balance.winrate, PYTHONHASHSEED=0) stay inside their D_MASS=0 Wilson 95% intervals, CAPPED at equal billing with the inertia term beside it (D_MASS*mean mass = D_WT*mean wield_heft over the workbench roster: 0.958), since the ruling puts weight BESIDE heft, not over it. The draw bound does NOT bite on the grid .1 .2 .3 .45 .6 .9 1.2, so the cap alone bounds the range (0, .958]; .45 is the grid member nearest its midpoint.
  FATIGUE_HANDLE_K=0.20, FATIGUE_FOOT_K=0.30, FOOT_COMMIT_DISC_K=0.06, FOOT_STANCE_K=0.05,
  # outcome-mapping (audit C-2: neutralize is a fixed per-mode shape, not dsig-scaled)
  NEUTRALIZE_PARRY=0.55, NEUTRALIZE_DODGE=0.62, NEUTRALIZE_WIND=0.50, NEUTRALIZE_OVERWHELM_DROP=0.45,
  RIPOSTE_ON_FAIL=0.32, COMMIT_EXPOSE_K=0.06,
  # COMMITMENT = (im)RECOVERABILITY (the physical axis): to commit IS to give up recovery, so the overcommit cost
  # scales with how hard the action is to terminate/retract — the weapon's static turning moment (mass*pob_frac:
  # a forward-heavy mace "wants to continue" and can't be stopped; a hand-balanced rapier retracts instantly,
  # which is WHY a rapier can feint and a mace can't) plus footwork (lunge = extended body = low recovery; choke
  # = gathered = recoverable). Weight is NON-LINEAR in recovery: the forward moment and the lunge cost scale as
  # mass**MOMENT_MASS_EXP, so a heavy weapon is disproportionately hard to arrest (a longsword lunge != a rapier
  # lunge). REF is the longsword anchor recomputed for the exponent (1.4**1.5 * 0.14 = 0.232) so it stays mult 1.0.
  EXPOSE_MOMENT_K=0.8, EXPOSE_LUNGE_K=0.4,
  MOMENT_MASS_EXP=1.5, LUNGE_REF_MASS=1.4,
  # ── T_vuln undefended-time / mode-exposure model (ED-PC-0027, 2026-07-23). The vulnerability window a fighter
  # carries while executing an attack (delivery+recovery), reusing _recovery_mode_commitment's swing-arrest/thrust-
  # retract core made mode-aware (sel_pc) + measure-amplified. EXPOSE_CLOSE_K: how much tight measure amplifies a
  # SWING's window (caught mid-arc; a thrust is measure-invariant). EXPOSE_SELECT_K: how much a mode's undefended
  # window discounts its damage-coupling in select_mode's greedy pick — so a fighter trades damage vs exposure and
  # the poleaxe's spike EMERGES vs plate (the hammer's long window outweighs its marginal damage edge) rather than
  # by fiat. Both [SIM-CALIBRATE] — structure from kinematics (self-consistent with _recovery_mode_commitment),
  # magnitudes to be cross-checked against HEMA-biomechanics mocap; EXPOSE_SELECT_K calibrated so the poleaxe flips
  # to its spike vs plate while single-mode weapons (which never reach the comparator) are untouched.
  EXPOSE_CLOSE_K=0.6, EXPOSE_SELECT_K=0.3,
  # ── recovery model: commitment=recovery, GRIP-AWARE, normalized to a 2H cut-thrust anchor.
  # recoverability_factor reads WP.at_grip(I_g,S_g) + point_concentration + hands at the chosen grip-position. The
  # STRUCTURE (sqrt(I) swing-arrest / parallel-axis / the 1H-2H force-couple) is [ASSERTED — first-principles;
  # validate vs motion-capture, NOT the engine's own config]; the anchor refs + gains are [SIM-CALIBRATE/FIAT].
  # Leads with body-extension (lunge), the best-grounded axis (Silver true-times / Giganti). See tasks/w811gujrg.output.
  REC_I_REF=0.139, REC_S_REF=0.212, REC_GRIP_REF=0.255,   # [SIM-CALIBRATE] anchor MoI / static-moment / grip_len in METRES (U0: 0.85 lu ×0.30 — ~1.4kg 2H cut-thrust blade) -> the scale-setter, recoverability 1.0
  ARREST_STR_K=0.05,   # PC-20 (4), AR-13 (Strength counterbalances heft): systems.recoverability_factor multiplies the WHOLE mode's irrecoverability by 1 - ARREST_STR_K*(strength - NEUTRAL['strength'])*wield_heft*(1 - pc) (no clamp of its own; RECOVER_FLOOR bounds the product; the term is scaled by the swung share (1 - pc) but the factor it scales multiplies the thrust component too at 0 < pc < 1), so a strong fighter arrests his own swing sooner (smaller overcommit_exposure, smaller tempo cost of a deep commit) and a weak one later, in proportion to the heft arrested; 0 at Strength 4. [SIM-CALIBRATE; ASSUMPTION; medium; Jordan to correct; revert: 0.0, the control, which reproduces the PC-20 (3) tree.] RULE: the middle grid member of the range over which (a) the factor stays above 0 for a Strength-7 fighter at the roster's heaviest wield_heft with no thrust share (guandao 3.116 at grip 0: ARREST_STR_K < 1/(3*3.116) = 0.107; above it Strength stops mattering at the top of the scale, a cliff), and (b) ED-1040's observable (str-2 greatsword mirror draw rate, n=3000) and every matchup family's pooled draw rate (weapon n=1000/weapon vs arming, attribute n=3000, tradition n=500/pair; balance.winrate, PYTHONHASHSEED=0) stay inside their ARREST_STR_K=0 Wilson 95% intervals. The draw bound does NOT bite on the grid .025 .05 .075 .1 (the weapon and tradition families fight at Strength 4, where the term is 0), so (a) alone bounds the range (0, .107); .05 is the grid member nearest its midpoint.
  REC_S_FLOOR=0.3, REC_THRUST_BASE=1.0, REC_W2=0.6, REC_K_COUPLE=0.9, REC_CTRL_K=0.3, RECOVER_FLOOR=0.3,   # [FIAT] swing static-moment floor / thrust anchor / 2H-couple gains / control-credit / lower bound
  CHOKE_DRIVE_REF=1.5, LUNGE_DEPTH_SCALE=4.0,   # [FIAT] close_unwieldiness to fully gather; commit over `lunge_commit` (the window's upper third, LUNGE_FRAC) for a full-depth lunge
  # WIELDING heft (tempo/stamina/strength COST) — DERIVED from the g-aware swing inertia (WP.at_grip I_g), a
  # COMPRESSED power-law (like agility) so the ~1000x MoI range maps to a sane spread; anchored at REC_I_REF so the
  # 2H cut-thrust reference ~= 1.0 (the old heavy heft). The half-
  # sword's tiny MoI reads LIGHT. The damage-impact path uses heft_resp. [SIM-CALIBRATE] exponent. EXP shared with agility (Cross/Fleisig handle-axis, [ASSERTED]).
  WIELD_HEFT_EXP=0.3,
  # Grip/stance DERIVED from morphology: a closing fighter GATHERS (grip_position 0->1) in proportion to how unwieldy
  # the weapon is in the close, bounded by WP.grip_choke_max (a rapier's short hilt cannot gather; a pole regrips up
  # the haft). Continuous grip_position + lunge_depth live on the Combatant. A dead exported key is guarded by
  # tests/valoria/test_combat_invariants.py::test_no_dead_exported_engine_params.
  # CLOSE_ENGAGE_M [ED-PC-0053]: the BODY-scale distance, in honest metres, at which a fight is CLOSED — chest-to-
  # chest out to about a forearm. This constant is a property of BODIES, not weapons, which is the whole
  # difference between a derivation and a gate. [SIM-CALIBRATE on the value; the SHAPE is grounded.]
  # CURVE_RECOVERY_K [channel 2, ED-PC-0054, 2026-07-29 — Jordan-grounded]: a curved blade does not WEDGE the way a
  # straight one can, so its swing arrests/extracts more cheaply — "faster recovery because the weapon isn't getting
  # stuck" and "greater manoeuvreability compared to a contemporary that is a purely straight edge", which are ONE
  # fact in this engine (recovery IS how soon you can act or redirect again). Discounts the C_swing branch of
  # systems._recovery_mode_commitment ONLY: a thrust retracts along its own line and has nothing to unstick.
  # SAFE BY CONSTRUCTION because `curvature` is dimensionless and bounded [0,1], so (1 - K*cv) is bounded in [1-K, 1]
  # — unlike this session's two earlier scaling terms, whose inputs were unbounded (S_g carries units; I_g spans
  # ~1000x). ⚠ ITS EFFECTIVE SIZE IS AMPLIFIED BY THE pc-CONFOUND: point_concentration anti-correlates with curvature
  # at -0.729, so curved weapons are already weighted into the swing branch where this applies ((1-pc) = 0.70..0.92
  # for the curved family). RE-MEASURE THIS TERM when channels 3-4 fix that tip data. [SIM-CALIBRATE; 0.0 ablates.]
  CURVE_RECOVERY_K=0.15,
  CLOSE_ENGAGE_M=0.45, POLE_CLOSE_K=0.92, LUNGE_1H_BONUS=1.15, LUNGE_2H_FACTOR=0.7,
  # TEMPO is coupled to COMMITMENT+RECOVERY: a deep, hard-to-recover commit leaves you slower to re-ready for the
  # next action (extra readiness debt = K * (commit-2) * recoverability_factor). A feint costs no tempo.
  RECOVERY_TEMPO_K=0.15,
  # bind iteration weights (calibrated): technique/skill, tactile (Fuhlen), strength — moved out of bind_sigma inline
  # BIND_MOMENT_K [channel 5, ED-PC-0052, 2026-07-29 — Jordan-grounded]: displacement resistance in the bind. Where
  # weapons CONNECT (parry/block/bind/wind), the side whose weapon carries more moment about the working hand is
  # harder to shove off the line. The bind's only other physical lever is systems.leverage(), which is pure GEOMETRY
  # (grip_len - LEVER_HEAD_K*head_len). Keyed on at_grip's S_g, NOT on mass:
  # the rapier is the HEAVIER weapon (1.37 kg vs the scimitar's 0.95) yet has the lower moment,
  # because its mass sits in hilt and pommel — so a mass-keyed term would move the wrong way. Applied as a LOG-RATIO
  # (see systems.bind_sigma) which is scale-free, antisymmetric, and compresses the polearm tail. An additive
  # log-odds shift, matching ED-PC-0045's ruling on how a bind lever must compose with logistic(bind_sigma).
  # [SIM-CALIBRATE] — own ablatable term, 0.0 ablates it.
  # PARRY_MOMENT_K / WIND_MOMENT_K [channel 5, ED-PC-0052]: the SAME displacement-resistance fact
  # (systems.contact_moment_edge, single owner) applied to the other two places weapons CONNECT. Jordan named
  # "parrying and blocking" FIRST, and the parry is the high-throughput contact: bind_sigma is evaluated ~1.2x per
  # fight, mode_sigma's parry branch on essentially every defended exchange, which is why a bind-only version of this
  # term was measured aggregate-INERT. Separate gains rather than one shared constant, exactly as the guard fact
  # already carries BIND_GUARD_K 0.55 / PARRY_GUARD_K 0.45 / WIND_GUARD_K 0.40. All [SIM-CALIBRATE]; 0.0 ablates.
  PARRY_MOMENT_K=0.30, WIND_MOMENT_K=0.30,
  BIND_MOMENT_K=0.30,
  BIND_TECH_K=0.06, BIND_TACTILE_K=0.04, BIND_STR_K=0.0156, BIND_SPINE_K=0.03,   # BIND_SPINE_K [U3/ED-PC-0018, U10/ED-PC-0022]: single-edge spine-press bearing surface (weapon_physics.spine differential), modulated by ability_factor 'spine_press' (shinogi; Winden was re-homed, ED-PC-0026). The strongest of the six levers per the U9 adversarial pass (robustly directional) — a small baseline here, decisive with the ability.
  # a wavy/flame-ground edge (weapon_physics.edge_vibration, 0 for a plain edge)
  # degrades the OPPONENT's tactile read in the bind and boosts the wielder's own initiative-steal there.
  # [SIM-CALIBRATE] — flamberge's 15mm amplitude is the only roster weapon that currently reads nonzero.
  BIND_VIBRATION_K=0.5,
  # outcome-mapping probabilities (calibrated) — lifted from wrapper inline literals (single source)
  STOPHIT_NSIG_BASE=0.4, TRUE_TIME_K=3.5, PARTIAL_DODGE_GRAZE=0.4, PARTIAL_PARRY_GRAZE=0.30, WIND_BIND_P=0.55,   # TRUE_TIME_K (ED-PC-0029): magnitude of Silver's true-time point-tempo edge (systems.true_time_edge) on the approach stop-hit — the light-point reach weapon's hand-speed advantage over a heavy-pointed closer. [SIM-CALIBRATE]. The mechanism is systems.true_time_edge, a tanh-saturating STANDING REACH differential, armour-faded to exactly 0 at plate — grounded in Silver's hand-before-foot, not in a head-inertia law (ED-PC-0029).
  RIPOSTE_ON_NEUTRALIZE=0.20, BIND_HIT_P=0.4,
  # mental-fatigue weights (calibrated): how much fatigue degrades the read vs the defence
  MENTAL_FAT_READ_K=0.4, MENTAL_FAT_DEF_K=0.3,
  # initiative substrate (the three-phase Vor/Nach/Indes ~ sen state; culture-neutral, differentiation layered on top).
  # A bounded sigma-edge for whoever holds the Vor (on attack AND defence). SAFEGUARDS: per-beat DECAY toward contested
  # (the damper — you hold the Vor only by continuing to threaten) + a hard CAP on |initiative| (the bound). Both are
  # required by the NERS audit for this positive-feedback state.
  INIT_SIGMA_K=0.16, INIT_SCALE=1.2,                     # the edge: INIT_SIGMA_K*tanh(rel_initiative/INIT_SCALE)
  INIT_DECAY=0.75, INIT_CAP=1.5,                         # damper (per beat) + hard bound
  INIT_GAIN_HIT=0.18, INIT_LOSS_WOUNDED=0.28,            # press the advantage / forced toward Nach by damage
  INIT_STEAL_INDES=0.36, INIT_LOSS_OVERCOMMIT=0.14,      # read-based steal (Indes/sen-no-sen) / overcommit bleeds grip
  # kuzushi / structure (dynamic balance): broken by overcommit / losing the bind / a solid blow; while broken it
  # degrades tempo AND defence; recovers each beat toward 1.0. This is the DYNAMIC tempo-vs-structure fix deferred
  # from the initiative build (replaces the rejected static balance->tempo coupling — structure is dynamic, balance
  # keeps its existing roles). Effect factor is 1.0 at full structure, so default/full-structure fighters are unaffected.
  POISE_FLOOR=0.40, POISE_EFFECT_FLOOR=0.72, POISE_RECOVER=0.20, POISE_FOCUS_K=0.10,   # Focus speeds structure recovery (Jordan 2026-06-03; Class-C). ED-PC-0031 (Jordan "strong strong poise break"): poise is DEEP so a stagger is decisive — FLOOR 0.40 (a hard concussion drives structure lower) + EFFECT_FLOOR 0.72 (a fully-staggered fighter acts/defends at 0.72x — the "wind knocked out" is real, not a ±12% nudge); the PC-5 plate-stalemate + lever-texture invariants are fitted against this pair.
  POISE_BREAK_OVERCOMMIT=0.09, POISE_BREAK_BIND=0.05, POISE_BREAK_HIT=0.07, POISE_SOLID_HIT=8.0,
  # PERCUSSION -> STAMINA (wind) + POISE (stagger) — ED-PC-0031 (Jordan). A landed blow delivers a concussive IMPULSE
  # DISTINCT from the wound: it drains the defender's STAMINA (wind knocked out / attrition) and BREAKS their POISE
  # (stagger). ARMOUR-GATED by physics: a BLUNT/percussion head transmits its impulse THROUGH the harness (mace/
  # warhammer/staff-butt concuss even when the plate holds — the anti-plate blunt path; Medieval Chronicles, tempered
  # by Devereaux's 'plate+padding soaks much'), scaled by percussion_authority × a per-tier absorption; a POINT/edge
  # transmits impulse only where it BITES — its load IS the wound d (a deflected point pings off plate ~0, preserving
  # the gap-specialist's plate close). [SIM-CALIBRATE] magnitudes; the blunt-vs-point transmission split is grounded.
  PERC_STAM_K=0.4, PERC_POISE_K=0.04, PERC_BLUNT_HEFT=2.2, PERC_POINT_FRAC=0.20,
  # ED-PC-0036: PERC_QUAL is the concussive-impulse quality ladder. It is DELIBERATELY NOT core.QUAL: core's ladder scales a
  # WOUND (0.25/0.5/1.0/1.5) whereas this scales transmitted IMPULSE, and a graze that barely breaks skin still
  # delivers real percussion (0.4 > core's 0.25) while an overwhelming blow concentrates more of the body's momentum
  # (1.6 > 1.5). Two ladders for one degree system is a smell, so the divergence is stated rather than left implicit.
  # PERC_STR_BASE/PERC_STR_K: the striker's mass-behind-the-blow term, = 0.5 + strength/4 (unchanged magnitudes).
  PERC_QUAL={'graze':0.4,'success':1.0,'overwhelming':1.6}, PERC_STR_BASE=0.5, PERC_STR_K=0.25,   # [SIM-CALIBRATE]
  PERC_BLUNT_TRANSMIT={'none':1.0,'light':0.85,'medium':0.7,'heavy':0.55},
  # single-time counter (a tier of the unified counter): UNIVERSAL but skill-gated. SELECTION is tempo-driven (how
  # often a fighter reaches for it); SUCCESS scales with reflex (CR-85, ED-IN-0330) — the untrained single-time counter
  # is a desperate-idiot move that mostly fails and is punished (eats the attack undefended, cedes the seized Vor).
  # The basic two-time riposte (on miss/neutralize) stays the universal, disadvantaged fallback. Abilities modulate later.
  COUNTER_SELECT_BASE=0.45, COUNTER_SUCCESS_BASE=0.50, COUNTER_REFLEX_K=0.05,
  # Indes flip refinement: the steal magnitude scales with commit-DEPTH (a deeper commit leaves more to exploit) and
  # read-MARGIN (how cleanly the defender out-read it). A deep commit read cleanly is a near-complete Vor flip; a
  # shallow/marginally-read one barely shifts it. Bounded [FLOOR,CEIL]x here, and further σ-bounded downstream by
  # initiative_sigma (tanh) — impactful, not auto-win. At commit4 + neutral margin the scale is ~1.0 (the prior flat value).
  INDES_COMMIT_K=0.4, INDES_READ_K=0.15, INDES_SCALE_FLOOR=0.5, INDES_SCALE_CEIL=2.0,
  # disposition (temperament, aggression axis; base param disp 1-7, 4=neutral, lean=(disp-4)/3). Orthogonal to tradition
  # (tradition=competence, disposition=propensity). THREE hooks: (1) COMMIT skew — aggressive leans deep (4,5), cautious
  # shallow (2,3); (2) COUNTER-selection tilt — cautious favours the single-time counter (reactive), aggressive presses
  # instead; (3) the INITIATIVE LEVER — aggressive drifts the Vor UP (pressing builds Vor), cautious DOWN (cedes it), so
  # BOTH poles cost: aggression risks overcommit (its deep commits raise existing exposure), caution bleeds the Vor. At
  # lean=0 every hook is a no-op (default fighters unchanged). Anchored to the German Vor/Nach doctrine (S2).
  DISP_COMMIT_K=0.8, DISP_COUNTER_K=0.5, DISP_INIT_K=0.10, WARINESS_K=1.5,   # WARINESS_K (WS-5): commit-caution vs an UNREAD tradition (familiarity<1 -> shallow bias), spread-floored; 0 = off
  # CONTINUOUS commitment (the commitment-recovery axis is a SPECTRUM, not 4 rungs): commit ~ 2 + 3*Beta(a,b),
  # with the disposition+wariness skew _k shaping the Beta (neutral a=b -> centred ~3.5; aggressive -> toward 5;
  # cautious/wary -> toward 2). Param floor 0.25 = the spread-floor. Replaces the old integer {2,3,4,5} draw.
  COMMIT_BETA_BASE=1.2, COMMIT_BETA_K=0.6, LUNGE_FRAC=2/3,   # LUNGE_FRAC: a THRUST committed at/above `S.lunge_commit` (this fraction of the beat's window, from its floor 2) IS a lunge (the body extends — reach+commitment, low recovery, more readable)
  # No imposition gate (Jordan, 2026-07-23, ED-PC-0023: top-down scripting that FORCED a tradition's preferred node
  # over the emergent bind/counter resolution — the antithesis of "each combatant resolves in a way that feels correct
  # to their style"). Tradition preference EMERGES from BUILD: a fighter binds more because they INVESTED in it (skill('bind') + a bind-friendly
  # weapon's wind affinity + learned binding abilities + disposition), all already live in mode_sigma/bind_sigma.
  # The tradition gates ACCESS to a technique kit; investment + skill drive efficacy.
  YIELD_HEALTH_FRAC=0.5,  # [ASSUMPTION; medium; Jordan to correct -- v9 PC-10a, RS-25.] Under the 'yield' duel term a fighter
  # yields once his Health falls to this fraction of full (`wrapper._terms_crossed`); 'blood' stops at the first wound
  # and 'death' is the lethal fight. Here, in CFG, so it crosses the exporter with every other tunable.
  # No matchup is certain: the chance a blow that would fell a fighter is TURNED (`wrapper.engagement`'s `_land`, B15.09).
  UPSET_FLOOR=0.05,   # [DESIGNER RULE — Jordan; deliberate, NOT an emergent mechanic. Tagged ED-PC-0036.]
  # One keyed draw at each felling (a sub-key of the fight's own Draw, "upset:<scene>:<round>", so it takes no position of the
  # fight's stream); with this probability the blow is turned (not applied: the tracker stays as it stood before it) and the would-be-felled fighter
  # lands the damage it carried back through the one damage site (`finalblow_riposte`), and the fight goes on from there. It MOVES THE TRACKERS: it is
  # a blow the trackers record, not an edit of the result -- the result is whatever the continued fight ends with, so a felled
  # fighter's win-rate is no longer clamped by a scoreboard flip but reached by the dice that follow. A blow that fells nobody draws nothing.

  # ── PC-15: thresholds lifted from wrapper.py / combat_systems.py literals (each was inline; values and meanings kept).
  # CLOSE_GAP_REF (above) is ALSO the one reach-gap threshold at the other three sites
  # (re-presentation gate, reopen, disengage): a reopened gap at or below it re-closes at the approach step, so "a gap worth
  # acting on" and the closed latch are one fact. DEEP_FRAC: where the DEEP tier begins, as a fraction of the commit window
  # `S.commit_depth` draws in this beat (`S.deep_commit` = 2 + DEEP_FRAC * the window's span: the lower edge of its upper third).
  # Deep gates the Indes steal, the displace-and-step-inside route and the shorter fighter's over-commit reopen moment; it is also
  # the anchor the Indes scale is centred on (scale 1.0 at the deep edge). A threshold on a drawn quantity is stated in the
  # quantity's live range: the keys this replaced (4.0, set when the window was [2, 5]) sat in the top 1.5% of the closed
  # window [2, ~4.03], about 1% of exchanges. At full room (range_avail >= RANGE_COMMIT_PEAK) the edge is exactly 4.0, as shipped.
  # LUNGE_FRAC stays its own key (a lunge is a different fact, though both read 2/3 today), and the ramp in systems.mode_sigma
  # (3 to 4) is a formula coefficient, not moved.
  # STAMINA_COLLAPSE: a fighter whose stamina is at or below this ends the burst. BEAT_BUDGET: the engagement's beat
  # ceiling (was soft*3 with soft=8). RIPOSTE_CAP: the ceiling on the riposte chance after the overcommit add-on.
  # CONTACT_*: the grapple branch effects, as multiples of the existing structure/initiative constants.
  DEEP_FRAC=2/3, STAMINA_COLLAPSE=-4, BEAT_BUDGET=24, RIPOSTE_CAP=0.95,
  CONTACT_DISARM_POISE_K=2.0, CONTACT_THROW_POISE_K=3.0, CONTACT_CONTROL_VOR_K=0.5,

  # ── contact axis (I7b, D8/D9): grab affinity derives from free-hand availability + LEVERAGE ONLY —
  # no hook-hardware term (JD-7 retraction: no primitive in the schema separates a pull-hook from a
  # bind-lug — orient_deg interleaves pulls and binds; see contact.py's docstring). GRAB_SHORT_REACH_M
  # (U0, ED-PC-0002: was GRAB_SHORT_REACH_LU=1.25 length-units; now 0.375 METRES — same threshold,
  # honest unit + honest name) is a PRIMITIVE threshold (head_len, metres), not a name check: it clears
  # the roster's dagger-class (head_len<=0.36) and excludes the next-shortest non-dagger record
  # (paired_short / half-sworded 2H forms, head_len>=0.399) — the open-contact exemption for a weapon
  # already functionally at grapple range. GRAB_STR_K >> GRAB_LEV_K*(leverage spread) so the grab reads
  # strength-dominant (a gross-motor contest), unlike bind_sigma's tactile/technique lead. [SIM-CALIBRATE] all.
  GRAB_SHORT_REACH_M=0.375, GRAB_STR_K=0.06, GRAB_LEV_K=0.5, GRAB_ESCAPE_P=0.25, GRAB_EDGE_K=0.07,   # GRAB_EDGE_K [U3/ED-PC-0018, U10/ED-PC-0022]: a live edge self-injures an unskilled bare-hand grab (weapon_physics.grab_hazard of the GRABBED weapon), mitigated by grab skill AND ability_factor 'edge_grab' (German Ringen am Schwert seizes a live blade safely — factor<1)

  # ── B14.08 (R-PC-18): the 18 constants that lived at module level in combat_systems.py, moved here unchanged so the
  # typed export carries them (CLAUDE.md §5); combat_systems reads every one through cfg[...]. Tags and meanings kept.
  # rear clearance (I7a, D7): close_tempo / str_demand penalty per metre of length trailing behind the working hand — the
  # counterweight that makes choking up a real tradeoff (Silver: the length behind the hands "will hinder him to strike,
  # thrust, ward, or go back"); the str_demand term is general handling difficulty, not close-scoped. [SIM-CALIBRATE]
  REAR_CLEARANCE_TEMPO_K=0.3, REAR_CLEARANCE_STR_K=0.15,
  # swing-room (I5, D4): range_avail floor (even the tightest melee retains some room); the range_avail fraction above which
  # the commit-window stays at its FULL upper bound (the C4 interior-optimum plateau — only real crowding shallows
  # commitment, never a monotone-from-the-start ramp); the floor on the commit-window contraction factor; the swing-room
  # legibility gain (weakly grounded — ships small, ablation-gated); the approach stop-hit's commitment-depth term (a
  # stop-hit thrown with full extension threatens more than one snapped into a cramped, rapidly-closing gap). [SIM-CALIBRATE]
  RANGE_AVAIL_FLOOR=0.3, RANGE_COMMIT_PEAK=0.85, RANGE_COMMIT_FLOOR=0.5, LEGIB_SWING_ROOM_K=0.3, STOPHIT_RANGE_K=0.3,
  # facing (I6, D6): lateral-void closing contribution and the close_rate multiplier [SIM-CALIBRATE]; the reach_sigma
  # profile term [FIAT — C1 unresolved]. Near-neutral by design: C1 (polearm facing direction) is unresolved.
  FACING_VOID_K=0.08, FACING_PROFILE_K=0.03, FACING_VOID_GAIN=0.15,
  # close-efficacy (I4, D5): the measure_gap scale the close-quarters ramp saturates over (unanchored to any other
  # reference, standing on its own calibration, ED-PC-0053) and the cap on f(measure_gap, range_avail). [SIM-CALIBRATE]
  CLOSE_EFF_GAP_REF=6.5, CLOSE_EFF_FLOOR=0.5,
  # graded secondary-affordance floors (U2/ED-PC-0008/0009, [DESIGN]): percussion, cut and thrust per-primitive floors a
  # mode must clear to be afforded regardless of its native head; SELECT_EPS is the affordance floor on a derived per-mode
  # effectiveness for each mode's OWN native-head branch (a vanishing mode is not even a candidate).
  MODE_PERC_MIN=0.5, MODE_EDGE_MIN=0.15, MODE_TIP_MIN=0.15, SELECT_EPS=0.05,
  # [DESIGN] TRUE_TIME_REF: reach-gap (reach-points) at which the true-time edge is ~tanh(1)=0.76 of its max (sets where
  # the hand-before-foot benefit saturates); ARREST_POB_REF: PoB_frac at/above which a weapon is too FRONT-HEAVY to brace
  # as a pole-jab (rear_balance ramps 1.0 at PoB_frac 0 down to 0 at the REF).
  TRUE_TIME_REF=1.5, ARREST_POB_REF=0.6,

  # ── B14.18 (U5b_PC_residue §1 item 2): the scale of the read's logistic in read_contest, p_read = logistic((read_d-read_a)/READ_SCALE);
  # was the literal 1.0 (byte-identical), now carried by the export so a sweep can fit it. [SIM-CALIBRATE]
  READ_SCALE=1.0,
)
