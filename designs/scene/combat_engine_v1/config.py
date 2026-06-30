"""All tunable coefficients in ONE place (seeds). Class-C — calibrated against the harness, not canon."""
CFG = dict(
  # reach (continuous, derived from weapon vector)
  L0=4.0, LONG=2.0, HANDS2=0.8, HEADR=1.0, HEAD_REACH={'point':1.0,'straight_cut':0.5,'curved_cut':0.5,'cut_thrust':0.5,'blunt':0.0},
  REACH_DISADV_K=0.22, REACH_ADV_K=0.12, RESIDUAL_REACH_FRAC=0.3, FOOT_MEASURE_K=0.15,
  # reach as a standing per-exchange advantage (reference structure): keep most of the gap, weight it high
  # unarmoured and let it FALL with armour (the reach->clinch rotation). Tuned so reach governs A0 across the roster.
  REACH_FRAC=0.82,
  REACH_W={'none':0.62,'light':0.50,'medium':0.34,'heavy':0.20},
  # heavy-weapon viability: bound the stacked weight+2H tempo penalty so a poleaxe can act (not 7x slower)
  MAX_TEMPO_PEN=0.8, TEMPO_FLOOR=0.7, REOPEN_K=0.34, REOPEN_MAX=0.6, CLOSE_TEMPO_MEAN=1.5, CLOSE_TEMPO_COMPRESS=0.38,
  PUSH_AVAIL_P=0.22, PUSH_REOPEN_BONUS=0.18,
  # conditional tempo (correction 2): fatigue slows cadence; choke/lunge grips trade cadence for control/reach
  TEMPO_FATIGUE_K=0.25, CHOKE_TEMPO_PEN=0.4, LUNGE_TEMPO_PEN=0.6,
  # movement legibility (correction 4): swings/lunges easy to read (lateral, large); thrusts hard (in-line)
  LEGIB_SWING=1.25, LEGIB_THRUST=0.80, LEGIB_COMMIT_K=0.10, LEGIB_LUNGE=0.25,
  # lever-arm primitive: redirect/bind capacity from an EXPLICIT hand-to-contact lever arm = grip_len − LEVER_HEAD_K·head_len
  # (Phase-3 grounding fix: the prior grip/(grip+head) ratio let compact weapons out-bind long ones — dagger > spear).
  # Structure grounded; magnitudes [SIM-CALIBRATE] (fit the bind win-rate in the re-baseline). LEVER_REF = a 1H sword's net lever.
  LEVER_K=0.22, LEVER_HEAD_K=0.2, LEVER_REF=0.32, LEVER_2H=0.20,
  # displace-and-step-inside vs a committed thrust (needs leverage edge + winning the read)
  DISPLACE_LEV_GAP=0.15, DISPLACE_P=0.55, DISPLACE_PULLBACK_GRAZE=0.30, APPROACH_DISPLACE_K=0.7, APPROACH_DISPLACE_MAX=0.6,
  # (feint config removed 2026-06-29: the feint is dissolved into the attack — WS-5 — so FEINT_*/feint_eval are gone.)
  # hilt/guard primitive: blade_guard (cross/quillons/rings) catches the blade in the bind & enhances winding;
  # hand_guard protects the hand in the parry ("don't parry with your hands"). Modulated around a neutral cross.
  BIND_GUARD_K=0.55, PARRY_GUARD_K=0.45, WIND_GUARD_K=0.40, GUARD_NEUTRAL=0.45,
  ADEF_W={'none':0.0,'light':0.4,'medium':1.0,'heavy':1.7}, ADEF_BLUNT=1.3, ADEF_POINT=1.0, ADEF_CUT=-0.9,
  ADEF_THRESHOLD={'none':0.0,'light':0.70,'medium':0.45,'heavy':0.72},
  CLOSE_RATE_K=0.40, STOPHIT_CHANCE=0.75, STOPHIT_FULL_GAP=3.0,
  # tempo
  BASE_TEMPO=2.0, SPEED_K=0.6, AGI_TEMPO_K=0.03, WEIGHT_PEN=0.8, HANDS_COMMIT=0.5, POLE_CLOSE_PENALTY=1.2, ACT_THRESHOLD=2.5, BURST_MAX=4,   # AGI_TEMPO_K: athleticism adds a little cadence (Jordan 2026-06-04, centred at agi 4; 0.03 = modest). BURST_MAX: per-TURN burst ceiling 1-~4
  # stamina / recovery
  STAMINA_REF=18.0, RECOVERY_FRAC=0.5, COST_SCALE=0.5, ACT_BASE=2.0, ACT_WEIGHT=1.0, ACT_COMMIT=0.4, OOB=2,
  # WS-2 req4: continuous weapon morphology (weight=2.7kg, not weight="heavy"). HEFT_MODE binary|continuous.
  # continuous adds a WITHIN-CLASS mass term on top of the binary class anchor (so cross-class balance — which the
  # binary `wt` encodes as wieldiness, not raw kg — is preserved) -> a 2.7kg greatsword reads heavier than a 1.4kg
  # longsword at every heft site (tempo, stamina cost, str-demand, cut/thrust impact). HEFT_MODE='binary' is
  # byte-identical to pre-WS-2. One calibrated gain (HEFT_MASS_K), per the recovered WP-2 recommendation.
  HEFT_MODE='continuous', HEFT_MASS_K=0.15,   # K=0.15: greatsword(2.7kg) heft 1.20 vs longsword(1.4kg) 1.00 — clear within-class ordering at a roster shift ~= the N=300 noise floor. Raise toward 0.30 (poleaxe -8pp) only with a full re-sweep.
  # concentration (Focus+Spirit tracker; baseline-consistency + fatigue-resistance)
  CONC_SPIRIT=2.0, CONC_FOCUS=3.0, CONC_BASE_K=4.0, CONC_DRAIN_BOUT=3.0, CONC_DRAIN_LOSS=2.0, CONC_DRAIN_HIT=2.0,   # Concentration = 3*Focus + 2*Spirit (Jordan 2026-06-03; was 3*Foc+1*Spi)
  CONC_RECOVER_FRAC=0.4, FOCUS_MENTAL_K=0.5, FOCUS_CONSISTENCY_K=0.10, DISRUPT_K=0.7,
  # reading / tempo channels
  READ_K=0.5, REFLEX_AGI=2.0, REFLEX_ATT=1.0, INIT_K=0.045, COMMIT_SIGMA=0.18,
    WOUND_ATK_OB=0.15, WOUND_DEF_OB=0.25,   # ED-1041 wound obstacle (bilateral, tunable): +0.15 Ob attacking / +0.25 Ob defending per wound; supersedes the -1D aggressor-only pool penalty (ED-1021). Defender has no pool, so defence-impairment must be an Ob channel.
  READ_HISTORY_K=0.2, INIT_READING_K=0.03, INIT_HISTORY_K=0.02,   # reading=experience(History) term; initiative reading/History terms (Jordan 2026-06-03; Class-C)
  # defense modes
  PARRY_K=0.9, DODGE_K=0.9, WIND_K=0.9, CHOKE_BIND_K=0.30,
  # strength handling + endurance fatigue
  D0=1.0, D_LEN=0.35, D_WT=1.0, D_HAND=0.6, D_2H=0.4, HANDLE_K=0.10,
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
  EXPOSE_MOMENT_K=0.8, EXPOSE_MOMENT_REF=(1.4**1.5)*0.14, EXPOSE_LUNGE_K=0.4, EXPOSE_CHOKE_K=0.2,   # REF = the longsword anchor (mass**exp * pob), exact so longsword stays mult 1.0
  MOMENT_MASS_EXP=1.5, LUNGE_REF_MASS=1.4,
  # Grip/stance DERIVED from morphology (no closes_poorly flag): unwieldy-in-close = reach beyond CLOSE_REACH_REF
  # (spear/staff/greatsword/rapier/poleaxe); choke-up needs grip_len >= CHOKE_GRIP_MIN (poles + 2H, NOT a rapier).
  CLOSE_REACH_REF=6.5, CHOKE_GRIP_MIN=1.0, POLE_CLOSE_K=0.92, LUNGE_1H_BONUS=1.15, LUNGE_2H_FACTOR=0.7,
  # TEMPO is coupled to COMMITMENT+RECOVERY: a deep, hard-to-recover commit leaves you slower to re-ready for the
  # next action (extra readiness debt = K * (commit-2) * recoverability_factor). A feint costs no tempo.
  RECOVERY_TEMPO_K=0.15,
  # bind iteration weights (calibrated): technique/skill, tactile (Fuhlen), strength — moved out of bind_sigma inline
  BIND_TECH_K=0.06, BIND_TACTILE_K=0.04, BIND_STR_K=0.0156,
  # outcome-mapping probabilities (calibrated) — lifted from wrapper inline literals (single source)
  STOPHIT_NSIG_BASE=0.4, PARTIAL_DODGE_GRAZE=0.4, PARTIAL_PARRY_GRAZE=0.30, WIND_BIND_P=0.55,
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
  POISE_FLOOR=0.5, POISE_EFFECT_FLOOR=0.88, POISE_RECOVER=0.20, POISE_FOCUS_K=0.10,   # Focus speeds structure recovery (Jordan 2026-06-03; Class-C)
  POISE_BREAK_OVERCOMMIT=0.09, POISE_BREAK_BIND=0.05, POISE_BREAK_HIT=0.07, POISE_SOLID_HIT=8.0,
  # attacker bias: a small per-exchange edge to the aggressor (first-mover / Vor-holder) so under equal circumstances
  # the one who moves first is favoured — an EDGE, not determinism (defence still works); the mirror stays 50 because
  # the aggressor role alternates over a fight. Added to net_sigma.
  ATTACKER_BIAS=0.12,
  # single-time counter (a tier of the unified counter): UNIVERSAL but skill-gated. SELECTION is tempo-driven (how
  # often a fighter reaches for it); SUCCESS scales with training (history)+reflex — the untrained single-time counter
  # is a desperate-idiot move that mostly fails and is punished (eats the attack undefended, cedes the seized Vor).
  # The basic two-time riposte (on miss/neutralize) stays the universal, disadvantaged fallback. Abilities modulate later.
  COUNTER_SELECT_BASE=0.45, COUNTER_SUCCESS_BASE=0.50, COUNTER_TRAIN_K=0.10, COUNTER_REFLEX_K=0.05,
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
  COMMIT_BETA_BASE=1.2, COMMIT_BETA_K=0.6, LUNGE_COMMIT=4.0,   # LUNGE_COMMIT: a THRUST committed at/above this depth IS a lunge (the body extends — reach+commitment, low recovery, more readable)
  # WS-4/WS-5 imposition gate (section C EXPERIMENT, default OFF): a tradition imposes/refuses its PREFERRED node
  # (German imposes the bind; Italian/English/Spanish refuse it -> a counter/disengage). DECOUPLED from channel
  # magnitude (fixed rates). Turn on via the workbench to measure vs the keep-bias baseline; it SHIPS only if it
  # beats that baseline on legibility + vacuum-balance (section C), else it stays off.
  IMPOSITION_GATE=True, IMPOSE_BIND_BOOST=0.5, IMPOSE_REFUSE_P=0.5,   # ON by default (WS-4 dissolution): with the affinity budget it beats the keep-bias baseline on spread + none-fairness + qualitative differentiation (section C). Toggle off to compare.
  # 95% videogame cap: structural per-exchange floor so no matchup reads 100/0 (always an upset chance)
  UPSET_FLOOR=0.05,
)
HANDLE_RANK={'Forgiving':0,'Standard':1,'Demanding':2}
