"""All tunable coefficients in ONE place (seeds). Class-C — calibrated against the harness, not canon."""
CFG = dict(
  # core
  DAMAGE_SCALE=4.0, CAP_END=4,
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
  # lever-arm primitive: redirect/bind capacity from grip-vs-head length (LEVER_REF ~ a one-hand sword's grip ratio)
  LEVER_K=2.2, LEVER_REF=0.30, LEVER_2H=0.20,
  # displace-and-step-inside vs a committed thrust (needs leverage edge + winning the read)
  DISPLACE_LEV_GAP=0.15, DISPLACE_P=0.55, DISPLACE_PULLBACK_GRAZE=0.30, APPROACH_DISPLACE_K=0.7, APPROACH_DISPLACE_MAX=0.6,
  # feinting: a non-existent action that degrades a FOOLED defender's real-attack defence/read; capped at 3 in a row,
  # short phase, costs stamina, readable (a defender who reads it gains a small counter-edge). Tuned not-overpowered.
  FEINT_ENABLE=True, FEINT_P=0.30, FEINT_MAX_STREAK=3, FEINT_BEAT_COST=0.3, FEINT_STAMINA=1.0,
  FEINT_DEBUFF=0.30, FEINT_PUNISH=0.12,
  # hilt/guard primitive: blade_guard (cross/quillons/rings) catches the blade in the bind & enhances winding;
  # hand_guard protects the hand in the parry ("don't parry with your hands"). Modulated around a neutral cross.
  BIND_GUARD_K=0.55, PARRY_GUARD_K=0.45, WIND_GUARD_K=0.40, GUARD_NEUTRAL=0.45,
  ADEF_W={'none':0.0,'light':0.4,'medium':1.0,'heavy':1.7}, ADEF_BLUNT=1.3, ADEF_POINT=1.0, ADEF_CUT=-0.9,
  ADEF_THRESHOLD={'none':0.0,'light':0.70,'medium':0.45,'heavy':0.72},
  CLOSE_RATE_K=0.40, STOPHIT_CHANCE=0.75, STOPHIT_FULL_GAP=3.0,
  # tempo
  BASE_TEMPO=2.0, SPEED_K=0.6, WEIGHT_PEN=0.8, HANDS_COMMIT=0.5, POLE_CLOSE_PENALTY=1.2, ACT_THRESHOLD=2.5, MAX_EXCHANGES_PER_BOUT=3,
  # stamina / recovery
  STAMINA_REF=18.0, RECOVERY_FRAC=0.5, COST_SCALE=0.5, ACT_BASE=2.0, ACT_WEIGHT=1.0, ACT_COMMIT=0.4, OOB=2,
  # concentration (Focus+Spirit tracker; baseline-consistency + fatigue-resistance)
  CONC_FOCUS=3.0, CONC_SPIRIT=1.0, CONC_BASE_K=4.0, CONC_DRAIN_BOUT=3.0, CONC_DRAIN_LOSS=2.0, CONC_DRAIN_HIT=2.0,
  CONC_RECOVER_FRAC=0.4, FOCUS_MENTAL_K=0.5, FOCUS_CONSISTENCY_K=0.10, DISRUPT_K=0.7,
  # reading / tempo channels
  READ_K=0.5, REFLEX_AGI=2.0, REFLEX_ATT=1.0, INIT_K=0.045, COMMIT_SIGMA=0.18,
  # defense modes
  PARRY_K=0.9, DODGE_K=0.9, WIND_K=0.9, CHOKE_BIND_K=0.30,
  # strength handling + endurance fatigue
  D0=1.0, D_LEN=0.35, D_WT=1.0, D_HAND=0.6, D_2H=0.4, HANDLE_K=0.10,
  FATIGUE_HANDLE_K=0.20, FATIGUE_FOOT_K=0.30, FOOT_COMMIT_DISC_K=0.06, FOOT_STANCE_K=0.05,
  # outcome-mapping (audit C-2: neutralize is a fixed per-mode shape, not dsig-scaled)
  NEUTRALIZE_PARRY=0.55, NEUTRALIZE_DODGE=0.62, NEUTRALIZE_WIND=0.50, NEUTRALIZE_OVERWHELM_DROP=0.45,
  RIPOSTE_ON_FAIL=0.32, COMMIT_EXPOSE_K=0.06,
  # bind iteration weights (calibrated): technique/skill, tactile (Fuhlen), strength — moved out of bind_sigma inline
  BIND_TECH_K=0.06, BIND_TACTILE_K=0.04, BIND_STR_K=0.0156,
  # outcome-mapping probabilities (calibrated) — lifted from wrapper inline literals (single source)
  STOPHIT_NSIG_BASE=0.4, PARTIAL_DODGE_GRAZE=0.4, PARTIAL_PARRY_GRAZE=0.30, WIND_BIND_P=0.55,
  RIPOSTE_ON_NEUTRALIZE=0.20, BIND_HIT_P=0.4, SEPARATION_P=0.03,
  # mental-fatigue weights (calibrated): how much fatigue degrades the read vs the defence
  MENTAL_FAT_READ_K=0.4, MENTAL_FAT_DEF_K=0.3,
  # 95% videogame cap: structural per-exchange floor so no matchup reads 100/0 (always an upset chance)
  UPSET_FLOOR=0.05,
)
HANDLE_RANK={'Forgiving':0,'Standard':1,'Demanding':2}
