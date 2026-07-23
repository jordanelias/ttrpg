"""All tunable coefficients in ONE place (seeds). Class-C — calibrated against the harness, not canon."""
CFG = dict(
  # reach (continuous, derived from weapon vector)
  L0=4.0,   # live reach_base anchor. (HANDS2 removed 2026-06-30 with the dead WP.reach_term; LONG/HEADR/HEAD_REACH retired Phase-3b — reach is geometry-derived; head is a primitive, not a categorical reach table.)

  REACH_DISADV_K=0.22, REACH_ADV_K=0.12, RESIDUAL_REACH_FRAC=0.3, FOOT_MEASURE_K=0.15,
  # Phase-3b: reach DERIVED from geometry (retires categorical reach=='long' + HEAD_REACH + the reach_adj triple-duty).
  # reach_base = L0 + REACH_GEOM_SCALE*(head_len + REACH_2H_K*grip_len*[2H]) + reach_adj. SCALE [SIM-CALIBRATE] fit so
  # the spread maps onto the old 4.5-7.8 band (spear longest, dagger shortest); a centre-gripped pole reaches less than
  # a butt-gripped one BY CONSTRUCTION (the grip insight). LONG/HEADR/HEAD_REACH retired here; L0 stays.
  # U0 (ED-PC-0002): head_len/grip_len are now METRES, so the scale absorbs the old 0.30 m length-unit
  # (0.635 reach-pt/lu -> 0.635/0.30 reach-pt/m — same physical scale, honest unit). reach_adj stays a SMALL
  # per-weapon residual in reach-POINTS (the same unit as reach_base's output, added OUTSIDE the geometric
  # scale) — it is not a stored length and is deliberately NOT rescaled (byte-identity would break otherwise).
  REACH_GEOM_SCALE=0.635/0.30, REACH_2H_K=0.4,
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
  # morphology-rearch Phase B5: a feathered/tasselled/ringed weapon's ornament motion adds visual clutter that
  # degrades the defender's read regardless of the attack's own mode legibility. [SIM-CALIBRATE] — the 3 roster
  # weapons with attested adornments (ranseur/guandao/jian) are period-documented as ceremonial-phase features,
  # so this is deliberately a SMALL knock, not a primary legibility axis. See weapon_physics.distraction().
  LEGIB_DISTRACT_K=0.15,
  # U3/ED-PC-0018 edges primitive — the three edge-effect channels (§2.3, one channel per physical fact). ACTIVATED
  # (U10/ED-PC-0022, 2026-07-23) to small GROUNDED baselines (were all K=0 until U9). The U9 capstone found no lever
  # robustly moves aggregate FIELD winrate — correct, because flat physics cancels in a mirror-ish field; that is not
  # evidence the physics is inert (the live_not_dead tests prove it responds). Efficacy BEYOND rote physics comes from
  # the TRADITION-MODULATION SURFACE: each lever is now routed through ability_primitives.ability_factor(c, <channel>),
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
  # fine precision -> reads easier (systems.choke_counterbalance -> legibility). ACTIVATED (U10/ED-PC-0022). This is now
  # the SOLE choke-cost channel: the thrust-side CHOKE_THRUST was RE-HOMED here (it was mis-parked against the D2 force-
  # invariant — see weapon_physics.py's retired-CHOKE_THRUST note). Modulated by ability_factor(c,'choke_control') (a
  # pole tradition gathers without telegraphing — mitigates; default 1.0). CHOKE_RC_REF — pole-class rear_clearance
  # reference the choke normalises by (poleaxe-class ~0.9).
  CHOKE_ACCURACY_K=0.03, CHOKE_RC_REF=0.9,
  # U7/ED-PC-0020 weapon-class-aware facing: FACING_REGIME_K — scales the signed facing regime (weapon_physics.facing_pref:
  # 1H profile / 2H square) multiplicatively in systems.facing_target, modulated by ability_factor(c,'facing_regime').
  # ACTIVATED (U10/ED-PC-0022) at a CONSERVATIVE 0.12: the C2 REGIME (1H-profile vs 2H-square) is Jordan-resolved and now
  # live (facing reads weapon class), but C1 (absolute polearm facing DIRECTION) stays unresolved, so facing must not
  # become load-bearing — the K stays modest and its consumers (FACING_VOID_K/FACING_PROFILE_K) stay small by design.
  FACING_REGIME_K=0.12,
  # lever-arm primitive: redirect/bind capacity from an EXPLICIT hand-to-contact lever arm = grip_len − LEVER_HEAD_K·head_len
  # (Phase-3 grounding fix: the prior grip/(grip+head) ratio let compact weapons out-bind long ones — dagger > spear).
  # Structure grounded; magnitudes [SIM-CALIBRATE] (fit the bind win-rate in the re-baseline). LEVER_REF = a 1H sword's net lever.
  # U0 (ED-PC-0002): lever lengths now METRES — LEVER_K rescaled /0.30 (per-metre gain), LEVER_REF ×0.30
  # (a stored length); LEVER_HEAD_K/LEVER_2H dimensionless, unchanged. Byte-identical.
  LEVER_K=0.22/0.30, LEVER_HEAD_K=0.2, LEVER_REF=0.096, LEVER_2H=0.20,
  # displace-and-step-inside vs a committed thrust (needs leverage edge + winning the read)
  DISPLACE_LEV_GAP=0.15, DISPLACE_P=0.55, DISPLACE_PULLBACK_GRAZE=0.30, APPROACH_DISPLACE_K=0.7, APPROACH_DISPLACE_MAX=0.6,
  # (feint config removed 2026-06-29: the feint is dissolved into the attack — WS-5 — so FEINT_*/feint_eval are gone.)
  # hilt/guard primitive: blade_guard (cross/quillons/rings) catches the blade in the bind & enhances winding;
  # hand_guard protects the hand in the parry ("don't parry with your hands"). Modulated around a neutral cross.
  BIND_GUARD_K=0.55, PARRY_GUARD_K=0.45, WIND_GUARD_K=0.40, GUARD_NEUTRAL=0.45,
  ADEF_W={'none':0.0,'light':0.4,'medium':1.0,'heavy':1.7}, ADEF_BLUNT=1.3, ADEF_POINT=1.2, ADEF_CUT=-0.9,   # ADEF_POINT 1.0->1.2 [SIM-CALIBRATE, reach-ladder frame; ED-1080]: the gap-thrust is a strong armour-defeater (the reliable armoured KILL — Le Jeu de la Hache / Harnischfechten), so a SELECTED spike's exchange-CONTROL (armor_defeat_sigma) now matches its DAMAGE — unifying the sigma path with the gap-game damage path (the adef-consistency lever). Set so the poleaxe spike adef ~= its hammer.
  ADEF_PERC_REF=8.0,   # [SIM-CALIBRATE] derived-percussion-authority reference (a steel hammer ~8) for blunt armour-defeat (Phase-3b)
  # FIX-1 (reach-threat decay): a long weapon that CANNOT defeat the closer's armour loses its reach/approach edge —
  # the armoured man walks through a threat that can't hurt him. Derived from adef_cap vs the tier threshold; 0-effect
  # unarmoured by construction. REACH_DECAY_K [FIAT — designer-set; deliberately LOW to avoid triple-counting REACH_W
  # + ADEF_CUT, which already remove most cut-vs-plate reach value]. FLOOR keeps a residual (an armoured man still works to close).
  REACH_DECAY_K=0.35, REACH_THREAT_FLOOR=0.35,
  ADEF_THRESHOLD={'none':0.0,'light':0.30,'medium':0.45,'heavy':0.72},   # MONOTONE (ED-1050 resolved, Jordan 2026-06-30): the armour-defeat threshold RISES with armour — a gambeson (light) is soft/easily defeated, mail (medium) harder, plate (heavy) hardest. light 0.70->0.30 fixes the backwards inversion (light>medium) that systems.armor_defeat_sigma's docstring forbids; medium/heavy KEPT (calibrated). Re-swept in canon + re-exported to combat_config.gd (retiring the port's private [AUDIT-FIX], CLAUDE.md §6). [SIM-CALIBRATE] values within the grounded monotone frame; validated (mirror-50, light matchups sane).
  CLOSE_RATE_K=0.40, STOPHIT_CHANCE=0.75, STOPHIT_FULL_GAP=3.0,
  # tempo
  BASE_TEMPO=2.0, TEMPO_RECOVER_K=0.4, TEMPO_RECOVER_SHAPE=0.35, AGI_TEMPO_K=0.03, WEIGHT_PEN=0.8, HANDS_COMMIT=0.5, POLE_CLOSE_PENALTY=1.2, ACT_THRESHOLD=2.5, BURST_MAX=4,   # SPEED_K RETIRED, replaced by TEMPO_RECOVER_K/_SHAPE (morphology-rearch Phase B6 correction, 2026-07-02): scales systems._recovery_mode_commitment's grip-aware balance-recovery delta from the anchor (tanh-saturating — the raw commitment spans ~0.2 to ~68 across the roster), replacing the retired per-weapon `spd` scalar. [SIM-CALIBRATE] both. AGI_TEMPO_K: athleticism adds a little cadence (Jordan 2026-06-04, centred at agi 4; 0.03 = modest). BURST_MAX: per-TURN burst ceiling 1-~4
  # stamina / recovery
  STAMINA_REF=18.0, RECOVERY_FRAC=0.5, COST_SCALE=0.5, ACT_BASE=2.0, ACT_WEIGHT=1.0, ACT_COMMIT=0.4, OOB=2,
  # WS-2 req4 heft: HEFT_MODE/HEFT_MASS_K RETIRED (morphology-rearch Phase B6, 2026-07-02) — core.heft_resp now
  # reads weapon_physics.heft() unconditionally (mass x forward-balance, real per-part data); there is no fiat
  # binary/continuous toggle left to select between.
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
  # ── recovery model (Phase-3 Stage 2): commitment=recovery, GRIP-AWARE, normalized to a 2H cut-thrust anchor.
  # recoverability_factor reads WP.at_grip(I_g,S_g) + point_concentration + hands at the chosen grip-position. The
  # STRUCTURE (sqrt(I) swing-arrest / parallel-axis / the 1H-2H force-couple) is [ASSERTED — first-principles;
  # validate vs motion-capture, NOT the engine's own config]; the anchor refs + gains are [SIM-CALIBRATE/FIAT].
  # Leads with body-extension (lunge), the best-grounded axis (Silver true-times / Giganti). See tasks/w811gujrg.output.
  REC_I_REF=0.139, REC_S_REF=0.212, REC_GRIP_REF=0.255,   # [SIM-CALIBRATE] anchor MoI / static-moment / grip_len in METRES (U0: 0.85 lu ×0.30 — ~1.4kg 2H cut-thrust blade) -> the scale-setter, recoverability 1.0
  REC_S_FLOOR=0.3, REC_THRUST_BASE=1.0, REC_W2=0.6, REC_K_COUPLE=0.9, REC_CTRL_K=0.3, RECOVER_FLOOR=0.3,   # [FIAT] swing static-moment floor / thrust anchor / 2H-couple gains / control-credit / lower bound
  CHOKE_DRIVE_REF=1.5, LUNGE_DEPTH_SCALE=4.0,   # [FIAT] close_unwieldiness to fully gather; commit over LUNGE_COMMIT for a full-depth lunge
  # WIELDING heft (tempo/stamina/strength COST) — DERIVED from the g-aware swing inertia (WP.at_grip I_g), a
  # COMPRESSED power-law (like agility) so the ~1000x MoI range maps to a sane spread; anchored at REC_I_REF so the
  # 2H cut-thrust reference ~= 1.0 (the old heavy heft). Retires the binary wt class for the COST path; the half-
  # sword's tiny MoI now reads LIGHT (fixes longsword-vs-plate at root). The damage-impact path keeps heft_resp (a
  # separate wt de-leak). [SIM-CALIBRATE] exponent. EXP shared with agility (Cross/Fleisig handle-axis, [ASSERTED]).
  WIELD_HEFT_EXP=0.3,
  # Grip/stance DERIVED from morphology: a closing fighter GATHERS (grip_position 0->1) in proportion to how unwieldy
  # the weapon is in the close, bounded by WP.grip_choke_max (a rapier's short hilt cannot gather; a pole regrips up
  # the haft). 'choke'/'normal'/'lunge' strings are RETIRED -> continuous grip_position + lunge_depth on the Combatant.
  CLOSE_REACH_REF=6.5, CHOKE_GRIP_MIN=1.0, POLE_CLOSE_K=0.92, LUNGE_1H_BONUS=1.15, LUNGE_2H_FACTOR=0.7,
  # TEMPO is coupled to COMMITMENT+RECOVERY: a deep, hard-to-recover commit leaves you slower to re-ready for the
  # next action (extra readiness debt = K * (commit-2) * recoverability_factor). A feint costs no tempo.
  RECOVERY_TEMPO_K=0.15,
  # bind iteration weights (calibrated): technique/skill, tactile (Fuhlen), strength — moved out of bind_sigma inline
  BIND_TECH_K=0.06, BIND_TACTILE_K=0.04, BIND_STR_K=0.0156, BIND_SPINE_K=0.03,   # BIND_SPINE_K [U3/ED-PC-0018 -> ACTIVATED U10/ED-PC-0022]: single-edge spine-press bearing surface (weapon_physics.spine differential), modulated by ability_factor 'spine_press' (German Winden). The strongest of the six levers per the U9 adversarial pass (robustly directional) — a small baseline here, decisive with the ability.
  # morphology-rearch Phase B5: a wavy/flame-ground edge (weapon_physics.edge_vibration, 0 for a plain edge)
  # degrades the OPPONENT's tactile read in the bind and boosts the wielder's own initiative-steal there.
  # [SIM-CALIBRATE] — flamberge's 15mm amplitude is the only roster weapon that currently reads nonzero.
  BIND_VIBRATION_K=0.5,
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
  IMPOSITION_GATE=False,   # RETIRED FIAT (Jordan design ruling 2026-07-23, ED-PC-0023): impose_node FORCED a tradition's preferred node (German impose-the-bind / Italian-etc refuse-it) via a label-keyed coin-flip that OVERRODE the emergent bind/counter resolution — top-down scripting (§0), the antithesis of "each combatant resolves in a way that feels correct to their style". Turned OFF: tradition-preference now EMERGES from BUILD — a fighter binds more because they INVESTED in it (skill('bind') + a bind-friendly weapon's wind affinity + learned binding abilities + disposition), all already live in mode_sigma/bind_sigma. The tradition gates ACCESS to a technique kit; investment + skill drive efficacy (the ability system's own target model). IMPOSE_BIND_BOOST/IMPOSE_REFUSE_P deleted with the fiat. (PREFERRED in traditions.py is now vestigial — kept as metadata pending a future EMERGENT selection-bias, never again a forced override.)
  # 95% videogame cap: structural per-exchange floor so no matchup reads 100/0 (always an upset chance)
  UPSET_FLOOR=0.05,
  # ── contact axis (I7b, D8/D9): grab affinity derives from free-hand availability + LEVERAGE ONLY —
  # no hook-hardware term (JD-7 retraction: no primitive in the schema separates a pull-hook from a
  # bind-lug — orient_deg interleaves pulls and binds; see contact.py's docstring). GRAB_SHORT_REACH_M
  # (U0, ED-PC-0002: was GRAB_SHORT_REACH_LU=1.25 length-units; now 0.375 METRES — same threshold,
  # honest unit + honest name) is a PRIMITIVE threshold (head_len, metres), not a name check: it clears
  # the roster's dagger-class (head_len<=0.36) and excludes the next-shortest non-dagger record
  # (paired_short / half-sworded 2H forms, head_len>=0.399) — the open-contact exemption for a weapon
  # already functionally at grapple range. GRAB_STR_K >> GRAB_LEV_K*(leverage spread) so the grab reads
  # strength-dominant (a gross-motor contest), unlike bind_sigma's tactile/technique lead. [SIM-CALIBRATE] all.
  GRAB_SHORT_REACH_M=0.375, GRAB_STR_K=0.06, GRAB_LEV_K=0.5, GRAB_ESCAPE_P=0.25, GRAB_EDGE_K=0.07,   # GRAB_EDGE_K [U3/ED-PC-0018 -> ACTIVATED U10/ED-PC-0022]: a live edge self-injures an unskilled bare-hand grab (weapon_physics.grab_hazard of the GRABBED weapon), mitigated by grab skill AND ability_factor 'edge_grab' (German Ringen am Schwert seizes a live blade safely — factor<1)
)
# HANDLE_RANK RETIRED (morphology-rearch Phase B6, 2026-07-02) — systems.str_demand now reads weapon_physics.
# handling() (PoB_frac/hand_guard, real per-part data); the Forgiving/Standard/Demanding category is gone.
