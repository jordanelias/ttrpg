"""Subsystem modules. Uniform contract: each is a pure function of (aggressor, defender, state, cfg[, rng]).
NO subsystem touches raw A/B — they receive Combatant objects in role. This isolates every mechanic for
unit-testing and makes the coupling explicit (the fix for the recurring inversion bugs)."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from collections import namedtuple   # ED-PC-0042 (I3): the sel_* bundle's two record shapes — HeadOption / ModeSelection, defined below
from math import tanh, sqrt, exp, log   # logistic single-sourced in core.logistic (ED-PC-0025); exp used by represent_measure_p's armour-fade; log by lever_log_edge (ED-PC-0045)
import core
import vocabulary as V   # the token ALPHABET, owned once (ED-PC-0042); core's tables are keyed by it
import weapon_physics as WP   # Phase-3b: derived L0 physics (percussion_authority/puncture_pressure/agility/reach) — cycle-free (WP imports only math + the zero-import `vocabulary` leaf at module scope)
import ability_primitives as ABIL   # U10/ED-PC-0022: the tradition-modulation surface for the morphology levers. ability_factor(c,channel)==1.0 by default (no equipped ability -> byte-identical), so the TR-less lever sites (legibility/facing_target) can reach it without threading TR. Cycle-free (ability_primitives imports only traditions).
from combatant import WEAPONS, GEOMETRY, HALFSWORD_FORM, HALFSWORD_BASE

# ---------- ability-lever composition (SINGLE OWNER — M5/F5, ED-PC-0045) ----------
def lever_log_edge(own_factor, opponent_factor):
    """The SIGN-SAFE way to compose two opposed multiplicative ability factors into a sigma term.

    THE DEFECT THIS REPLACES (M5/F5): the two contested-channel sites used to multiply a SIGNED
    physical differential by the RATIO `eff_cw(own)/eff_cw(opp)` — and a factor > 1 AMPLIFIES a
    negative difference, so investing in a technique made its owner WORSE exactly when they were
    behind on the differential it multiplied. `leverage()` is signed (14 of the 53-entry WEAPONS
    roster are negative, measured 2026-07-29; the plan's "14 of 51" counts balance.py's roster, which
    excludes the two half-sword forms — same 14 weapons either way) and
    the measure `gap` is signed by construction, so this was live, not a corner case.

    THE FORM: modulate the WIN PROBABILITY, which is positive by construction, rather than the signed
    differential. In log-odds space that is a pure ADDITIVE shift, `log(own) - log(opp)`, so the
    owner's odds are multiplied by `own/opp` REGARDLESS of the sign of the physical differential —
    exactly the contract in the customization proposal's §5.1 rule 5. For the bind this is exact:
    `bind_dominance_p(s) = core.logistic(s)`, so a level-1 Stärke-Schwäche (1.20) multiplies the
    owner's odds of dominating the bind by exactly 1.20. In the measure channel the same shift rides
    the monotone sigma->outcome map (the resolver shifts a roll, not a log-odds), so it raises the
    owner's win probability monotonically without being literally an odds multiplier there.

    Strictly increasing in `own_factor`, strictly decreasing in `opponent_factor`, on every input —
    that monotonicity IS the sign-safety property, and `tests/valoria/test_combat_lever_sign_safety.py`
    asserts it for every '*'-op ability in `ability_primitives.ABILITIES`, equipping each on the
    DISADVANTAGED side. Exactly 0.0 (not approximately) when both factors are 1.0, which is every
    default build — that is what makes E1a byte-identical at defaults rather than merely close.
    Both arguments come from `ability_factor`, which clamps to [ABIL_FACTOR_FLOOR, ABIL_FACTOR_CEIL],
    so `log` is always finite and never sees 0. Pure.

    NOT the alternatives, both rejected with measurements (plan §4 E1a / review R-4): scaling each
    side's OWN signed contribution recreates the defect on the 14 negative-leverage weapons, and
    clamping `leverage` at 0 inside `bind_sigma` would change DEFAULT-build behaviour."""
    return log(own_factor) - log(opponent_factor)

# ---------- reach (continuous, derived) ----------
def reach_base(c, cfg, grip=None):
    """Standing reach = body/arm offset (L0) + the weapon's forward extent DERIVED from geometry (Phase-3b: retires
    the categorical reach=='long' + HEAD_REACH[head] + the per-weapon reach_adj triple-duty). Forward extent =
    head_len (the blade/shaft forward of the lead hand) + a 2H rear-hand setback (REACH_2H_K*grip_len). So a
    CENTRE-gripped pole (staff, head_len≈grip_len) reaches LESS than a BUTT-gripped one (spear, head_len≫grip_len),
    and a long blade (greatsword) more than a short one — the grip-position insight, emergent. reach_adj is now a
    SMALL per-weapon residual, not the dominant term.
    GRIP-AWARE (I3, D3, 2026-07-03 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
    plan_r1_RATIFIED.md): the forward extent is reduced by the FLOORED geometric slide (WP.at_circumstance's
    `geom_slide`, D1) at the given grip — a gathered-up pole reaches less. `grip=None` (the default) reads the
    combatant's LIVE `c.grip_position`; an explicit override is used ONLY by grip_target's own drive input
    (JD-9 — see close_unwieldiness/grip_target) to break the grip<->reach feedback loop D3 would otherwise close.
    At grip=0 this is byte-identical to the pre-I3 return for every weapon (geom_slide(w,0)==0 always)."""
    return cfg['L0'] + cfg['REACH_GEOM_SCALE']*forward_extent(c, cfg, grip) + c.w.get('reach_adj',0.0)


def forward_extent(c, cfg, grip=None):
    """SINGLE OWNER of the weapon's forward extent in METRES — how far its business end sits ahead of the working
    hand: the blade/shaft forward of the lead hand, MINUS the floored geometric slide at the current grip (gathering
    in shortens it), PLUS a 2H rear-hand setback. Carries the whole "shaft length + hand position on shaft" fact.
    Extracted 2026-07-29 (ED-PC-0053) because `close_unwieldiness` now needs the same quantity, and the engine's own
    invariant is that a rule lives ONCE (CLAUDE.md §8). reach_base scales it into reach-points and adds the body
    offset L0; close_unwieldiness compares it against the body's close measure. They cannot disagree about how far
    forward a weapon reaches, because there is only one derivation. Pure."""
    w = c.w
    g = getattr(c, 'grip_position', 0.0) if grip is None else grip
    geom_slide = WP.at_circumstance(w, g, 1.0)['geom_slide']
    return (w['head_len'] - geom_slide) + cfg['REACH_2H_K']*w['grip_len']*(w['hands']==2)

# ---------- wielding heft (DERIVED, g-aware — the COST of swinging; replaces the binary wt class) ----------
def wield_heft(c, cfg):
    """Wielding heft (the tempo/stamina/strength COST of bringing a weapon to bear) — DERIVED from the g-aware swing
    inertia at the chosen grip (WP.at_grip I_g), a COMPRESSED power-law so the ~1000x MoI range across the roster
    maps to a sane heft spread. Anchored so the 2H cut-thrust reference reads ~1.0 (the old heavy-class heft). The
    half-sword form's tiny MoI now reads LIGHT (was binary wt='heavy' -> fixes the longsword-vs-plate collapse at
    root); a GATHERED pole (lower I_g) is lighter to wield. Replaces core.heft_resp on the COST path only (the
    damage-impact path keeps heft_resp pending the wt de-leak). Pure."""
    I_g = WP.at_grip(c.w, getattr(c, 'grip_position', 0.0))['I_g']
    return (max(1e-6, I_g) / cfg['REC_I_REF']) ** cfg['WIELD_HEFT_EXP']

# ---------- tempo ----------
def weapon_tempo(c, cfg, fatigue=0.0):
    """General cadence — CONDITIONAL on grip/stance/fatigue (correction 2), not a static weapon property. Heavy
    weapons are slower but NOT tempo-dead (penalty bounded). Fatigue reduces cadence (a tiring fighter acts less
    often). A choked grip trades cadence for close-quarters control; a lunge/extended grip trades repeat-speed for
    reach (handled at the call site via grip state). BALANCE-RECOVERY (morphology-rearch Phase B6, corrected):
    how readily a fighter regains a ready position after a swing/thrust is NOT a static weapon-geometry ratio —
    it is the SAME grip-aware physics recoverability_factor models (point of balance, head mass, and how the
    weapon is HELD, via _recovery_mode_commitment's swing-arrest/thrust-retract blend at the CURRENT grip-
    position), replacing the retired per-weapon `spd` scalar. A weapon that commits MORE than the anchor
    (>1.0) recovers slower -> costs cadence; one that commits less recovers faster -> gains a little."""
    w=c.w
    g=getattr(c,'grip_position',0.0)
    _heft=wield_heft(c,cfg)   # DERIVED g-aware MoI heft (Phase-3 Stage 2b): replaces the binary wt class on the COST path
    pen=cfg['WEIGHT_PEN']*_heft+cfg['HANDS_COMMIT']*(w['hands']==2)*_heft
    # KNOWN BROKEN-LOGIC (ED-PC-0023 audit, FLAGGED not fixed here): this hard min() FLAT-TOPS 38/53 weapons (every
    # raw pen>0.8 — a rapier at 0.831 and a spear at 2.878 read the IDENTICAL 0.80) to one value, erasing the tempo
    # ordering. The fix is a surgical saturation of only the over-cap tail (min(pen,MAXP)+K*tanh(max(0,pen-MAXP)),
    # arming/sub-cap byte-identical), but it changes 38 weapons' weapon_tempo/close_tempo and so requires a DELIBERATE
    # regeneration of tests/valoria/r3_identity_golden.json (no generator exists — must be hand-reproduced) per that
    # fixture's re-baseline protocol — out of scope for this fiat-fix batch. See u10_activation_v1.md §7 (deferred).
    pen=min(pen, cfg['MAX_TEMPO_PEN'])
    pen += cfg['CHOKE_TEMPO_PEN']*g   # gathering in trades cadence for close control — CONTINUOUS in grip_position (no choke string)
    pen += cfg['LUNGE_TEMPO_PEN']*getattr(c,'lunge_depth',0.0)     # an extended/lunged body is slower to repeat — CONTINUOUS in lunge_depth
    pen += cfg['TEMPO_RECOVER_K']*tanh(cfg['TEMPO_RECOVER_SHAPE']*(_recovery_mode_commitment(w,g,cfg)-1.0))   # balance-recovery, relative to the 2H cut-thrust anchor's neutral commitment=1.0; tanh-SATURATING (raw commitment spans ~0.2 to ~68 across the roster — a long pole's swing-arrest MoI at grip 0 is enormous — so a linear term would either flatten short weapons or blow the long ones straight to the floor; the tanh keeps the common 0.2-3 range well-differentiated while bounding the extreme-polearm tail)
    t=cfg['BASE_TEMPO']+cfg['AGI_TEMPO_K']*(c.agi-4)-pen   # athleticism adds a LITTLE cadence (Jordan 2026-06-04); centred at agi 4 so default fighters & the mirror are unchanged
    t*=(1-cfg['TEMPO_FATIGUE_K']*fatigue)               # fatigue slows the rate of action
    t*=poise_factor(c, cfg)                            # DYNAMIC structure/balance: a kuzushi'd fighter acts slower (1.0 at full)
    return max(cfg['TEMPO_FLOOR'],t)
REAR_CLEARANCE_TEMPO_K = 0.3   # [SIM-CALIBRATE] close_tempo penalty per metre of rear clearance (I7a, D7) — the
                               #   counterweight that makes choking up a real tradeoff (Silver: the length behind
                               #   the hands "will hinder him to strike, thrust, ward, or go back").
REAR_CLEARANCE_STR_K = 0.15    # [SIM-CALIBRATE] str_demand penalty per metre of rear clearance (I7a, D7) —
                               #   general handling difficulty, not close-scoped (unlike the tempo term above).

def rear_clearance(c, cfg):
    """The length trailing behind the working hand AT THE COMBATANT'S CURRENT GRIP (I7a, D7 — designs/audit/
    2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md; consumes D1/I2's at_circumstance,
    unread until now). Pure."""
    return WP.at_circumstance(c.w, getattr(c,'grip_position',0.0))['rear_clearance']

def choke_counterbalance(c, cfg):
    """U5/ED-PC-0019 — how much a head-heavy pole is CHOKED UP to counterbalance its forward mass this beat: the live
    grip_position (0 at the open measure, ->1 gathered to the working balance) weighted by how much shaft TRAILS the
    hand to counterbalance (rear_clearance, normalised by a pole-class reference). A compact one-hander (low
    rear_clearance) barely counterbalances; a poleaxe/staff (high rear_clearance) does so strongly. The COST of that
    control — a gathered pole telegraphs and loses fine precision — routes to the accuracy/legibility channel
    (CHOKE_ACCURACY_K), which is now the SOLE choke-cost channel: the thrust-side cost was re-homed here from
    weapon_physics.phi_grip (U10/ED-PC-0022 retired CHOKE_THRUST_K — it was mis-parked against the D2 force-invariant).
    Half-sword forms are EXEMPT: their
    grip is the blade-grip (a different mechanic), and the derived short-lever form reads ~0 here anyway — an explicit
    base-form guard makes that exact. In [0,1]; 0 at grip=0. Reuses the rear-clearance delta (no new primitive). Pure."""
    if 'base' in c.w:                                   # a *_halfsword form — not a pole choke-counterbalance
        return 0.0
    grip = getattr(c, 'grip_position', 0.0)
    if grip <= 0.0:
        return 0.0
    return min(1.0, grip * (rear_clearance(c, cfg) / cfg['CHOKE_RC_REF']))

def close_tempo(c, cfg, fatigue=0.0):
    """Cadence IN THE CLOSE — conditional (fatigue/grip). A long two-handed pole (spear/staff) is SLOW to recover
    once a faster weapon is inside UNLESS it chokes up (grip adjustment to act in close quarters). Spread COMPRESSED
    toward the mean so action-frequency is a secondary edge, not the deciding axis (reach governs).
    I7a/D7: gathering in also LENGTHENS what trails behind the hand — a real close-quarters footwork penalty
    that makes choking up a genuine tradeoff against the reach it buys (D3), not a free lunch."""
    t=weapon_tempo(c,cfg,fatigue)
    # a weapon UNWIELDY in the close (DERIVED from reach — long business-end) is slow to recover once a handier
    # weapon is inside; GATHERING IN (grip_position) reduces the penalty in proportion (a fully-gathered pole pays
    # none). Pure morphology, CONTINUOUS in grip_position (no choke string, no closes_poorly flag).
    t -= cfg['POLE_CLOSE_K']*close_unwieldiness(c,cfg)*(1.0 - getattr(c,'grip_position',0.0))
    t -= REAR_CLEARANCE_TEMPO_K*rear_clearance(c,cfg)
    t=max(cfg['TEMPO_FLOOR'],t)
    return cfg['CLOSE_TEMPO_MEAN'] + (t-cfg['CLOSE_TEMPO_MEAN'])*cfg['CLOSE_TEMPO_COMPRESS']

# ---------- stamina ----------
# ED-PC-0035: the `stamina_max(c)` back-compat accessor is REMOVED (zero callers; read c.stamina_max directly —
# the combatant hosts its own derived figures).
def act_cost(c, commit, cfg):
    return (cfg['ACT_BASE']+cfg['ACT_WEIGHT']*wield_heft(c,cfg)+cfg['ACT_COMMIT']*commit)*cfg['COST_SCALE']   # DERIVED g-aware heft (Stage 2b)

# ---------- concentration (Focus+Spirit tracker) ----------
# ED-PC-0035: the `conc_max(c,cfg)` back-compat accessor is REMOVED (zero callers; call c.derive_stats(cfg) and read
# c.conc_max — the combatant hosts it, 3F+2S, ED-902).
def reading(c, cfg): return (2*c.cog + c.att)/3 + cfg['READ_HISTORY_K']*(c.history-3)   # cog primary, Att half, + relevant-History experience (Jordan 2026-06-03)
def reflex(c, cfg): return (cfg['REFLEX_AGI']*c.agi+cfg['REFLEX_ATT']*c.att)/(cfg['REFLEX_AGI']+cfg['REFLEX_ATT'])

# ---------- strength handling + endurance fatigue ----------
def str_demand(c, cfg):
    w=c.w; return (cfg['D0']+cfg['D_LEN']*reach_base(c,cfg)+cfg['D_WT']*wield_heft(c,cfg)+cfg['D_HAND']*WP.handling(w)
                    +cfg['D_2H']*(w['hands']==2)+REAR_CLEARANCE_STR_K*rear_clearance(c,cfg))   # DERIVED g-aware heft (Stage 2b); D_HAND now reads morphology-rearch Phase B6's PoB_frac/hand_guard handling() gap, not the retired Forgiving/Standard/Demanding category. I7a/D7: general handling difficulty from what trails behind the hand.
def handling_penalty(c, fat, cfg):
    deficit=max(0.0, str_demand(c,cfg)-c.strength)
    return cfg['HANDLE_K']*deficit + cfg['FATIGUE_HANDLE_K']*fat
def disp_lean(c):
    """Disposition lean on the aggression axis: (disp-4)/3 in [-1,1]; +ve aggressive, -ve cautious, 0 = neutral (default)."""
    return (c.disp-4)/3.0
def balance_eff(c, fat, cfg):
    # BALANCE is NOT a stat (Jordan): it is GOVERNED BY AGILITY, modulated by CURRENT poise (kuzushi context); ability
    # modulation (Destreza compás etc.) arrives with the channel-wiring pass. The `agi-1` aligns Agility's neutral (4)
    # to the engine's balance-neutral (3), so a default fighter's substrate is unchanged. Still 1.0× at full poise.
    return (0.5*c.agi + 0.5*c.strength - 1 + c.skill('balance'))*(1-cfg['FATIGUE_FOOT_K']*fat) * poise_factor(c, cfg)   # ½Agi + ½Str (Jordan 2026-06-03), re-centred so Agi=Str=4 stays neutral 3
def anti_overcommit(c, fat, cfg): return cfg['FOOT_COMMIT_DISC_K']*(balance_eff(c,fat,cfg)-3)

def _recovery_mode_commitment(w, g, cfg, sel_pc=None, room=1.0):
    """The mode-blended balance-recovery commitment at grip-position g — the shared physical core BOTH
    recoverability_factor and weapon_tempo's own balance-recovery term read: SWING arrest (sqrt of the re-
    pivoted MoI, GATED by the forward static moment so a centre-balanced pole is not mis-ranked as
    irrecoverable) vs THRUST retract (the forward static moment alone — it retracts along the line), blended by
    point_concentration (a hand-balanced rapier retracts; a forward mace 'wants to continue'). Reads point of
    balance, head mass, AND how the weapon is held (all folded into WP.at_grip's I_g/S_g at THIS g) — the three
    facts a weapon's balance-recovery genuinely depends on. Dimensionless vs the 2H cut-thrust anchor (1.0 =
    neutral). Extracted so weapon_tempo can reuse this core WITHOUT recoverability_factor's own 1H/2H-control-
    credit and lunge terms, which weapon_tempo already applies as its own separate, differently-scoped cadence
    penalties (re-applying them here would double-count). Pure.

    MODE-AWARE + MEASURE-AMPLIFIED (ED-PC-0027, the T_vuln undefended-time model): this core doubles as the
    SELECTED-MODE vulnerability window a fighter carries while executing an attack (delivery + recovery), driven by
    two args that DEFAULT to the byte-identical prior behaviour:
      · `sel_pc` — the point_concentration of the SELECTED use-mode (None -> whole-weapon pc). A poleaxe that chose
        its spike (sel_pc high) retracts on-line like a thrust (low commitment); one that chose its hammer (sel_pc
        low) carries the full swing-arc commitment. So *choosing* the thrust genuinely lowers the window — the mode
        asymmetry the whole-weapon pc could not see.
      · `room` — the swing-arc's available measure (1.0 = full, default). A swing in TIGHT measure is caught mid-arc
        (cannot develop or arrest cleanly) so its commitment RISES (EXPOSE_CLOSE_K); a thrust retracts along the line
        regardless, so the C_thrust branch is measure-INVARIANT (the same rigid-body reasoning as close_efficacy's
        point->1.0). Grounding: Silver's 'times' (the thrust is the shortest, safest line) + 'closer = less able to
        swing'. room=1.0 -> no amplification -> byte-identical."""
    a = WP.at_grip(w, g)
    I_g, S_g = max(1e-9, a['I_g']), a['S_g']
    I_ref, S_ref = cfg['REC_I_REF'], cfg['REC_S_REF']
    pc = sel_pc if sel_pc is not None else w['geo']['point_concentration']   # SELECTED-mode thrust-ness (fallback: whole-weapon, read off the BAKED surface — see geometry.bake's raw passthrough)
    close = 1.0 + cfg['EXPOSE_CLOSE_K'] * (1.0 - max(0.0, min(1.0, room)))         # tighter room -> a swing is caught mid-arc; thrust invariant
    C_swing  = sqrt(I_g / I_ref) * (cfg['REC_S_FLOOR'] + (1 - cfg['REC_S_FLOOR']) * S_g / S_ref) * close
    C_thrust = cfg['REC_THRUST_BASE'] + cfg['EXPOSE_MOMENT_K'] * (S_g / S_ref - 1)
    return pc * C_thrust + (1 - pc) * C_swing

def recoverability_factor(c, cfg):
    """IRRECOVERABILITY multiplier on the overcommit cost — the commitment=recovery axis, made physical and
    GRIP-AWARE (Phase-3 Stage 2, grounded). Layers a MoI-aware 1H/2H force-couple control credit and the body-
    extension (lunge) term — the lead, best-grounded axis (Silver true-times / Giganti) — on top of
    _recovery_mode_commitment's shared swing-arrest/thrust-retract core. Normalized to a 2H cut-thrust anchor
    (recoverability 1.0; the mirror is symmetric). Bounded below. Pure. The sqrt(I)/parallel-axis/couple
    STRUCTURE is [ASSERTED — first-principles]; the gains are [FIAT/SIM-CALIBRATE]. See tasks/w811gujrg.output."""
    w=c.w
    g  = getattr(c, 'grip_position', 0.0)
    ld = getattr(c, 'lunge_depth', 0.0)
    I_g = max(1e-9, WP.at_grip(w, g)['I_g'])
    I_ref = cfg['REC_I_REF']
    two = 1.0 if w['hands'] == 2 else 0.0
    sel_pc = getattr(c, 'sel_pc', None)                                        # SELECTED-mode thrust-ness (ED-PC-0027: T_vuln is mode-aware)
    pc = sel_pc if sel_pc is not None else w['geo']['point_concentration']   # fallback: whole-weapon (single-mode weapons: sel_pc==whole-weapon pc, byte-identical)
    room = getattr(c, 'range_avail', 1.0)                                      # tight measure amplifies a SWING's window (a thrust is measure-invariant)
    C_mode = _recovery_mode_commitment(w, g, cfg, sel_pc=sel_pc, room=room)
    # (C) 1H/2H CONTROL via the force-couple, MoI-aware (anchor-normalized: the reference gives credit 1.0)
    tau     = (1 + cfg['REC_W2'] * two) * (1 + cfg['REC_K_COUPLE'] * w['grip_len'] * two)               # grip_len in metres (U0)
    tau_ref = (1 + cfg['REC_W2'])      * (1 + cfg['REC_K_COUPLE'] * cfg['REC_GRIP_REF'])               # REC_GRIP_REF in metres (U0)
    arrest  = (tau / sqrt(I_g)) / (tau_ref / sqrt(I_ref))                       # >1 = more controllable than the anchor
    ctrl_credit = 1 - cfg['REC_CTRL_K'] * max(0.0, arrest - 1) * (1 - pc)       # a SWUNG weapon gains from 2H control; a thrust barely
    # (D) BODY-EXTENSION (lunge) — the lead axis; fires from the wrapper as lunge_depth
    lunge_mult = 1 + cfg['EXPOSE_LUNGE_K'] * ld * (w.get('mass', 1.0) / cfg['LUNGE_REF_MASS']) ** cfg['MOMENT_MASS_EXP']
    return max(cfg['RECOVER_FLOOR'], C_mode * ctrl_credit * lunge_mult)
def close_unwieldiness(c, cfg, grip=None):
    """How poorly a weapon serves IN THE CLOSE: the OVERHANG, in metres, of its business end past the distance at
    which a fight is closed. 0 for a weapon shorter than that measure (a dagger is at home in the close).
    [ED-PC-0053, 2026-07-29 — Jordan: "you can't do a full thrust or swing one foot away holding a rapier"]
    THIS WAS A FIAT GATE UNTIL 2026-07-29, despite this docstring already claiming "pure morphology". It read
    `max(0, reach_base(c) - CLOSE_REACH_REF)` with CLOSE_REACH_REF=6.5 — but reach_base is
    `L0 + REACH_GEOM_SCALE*forward_extent + reach_adj` and **L0=4.0 is the fighter's own arm**, so the threshold
    implied `(6.5-4.0)/2.1167 = 1.18 m of weapon forward extent` before a weapon was unwieldy in the close AT ALL.
    A close/grapple happens around 0.45 m, so the gate was ~3x too permissive and, being a threshold, produced a
    CLIFF: **every one-handed sword in the roster paid exactly 0.0000** (dagger 0.21 m, arming 0.72, rapier 0.96,
    longsword 0.94 — all free; only estoc/spear/guandao crossed it). Since reach has FOUR benefit channels
    (measure, approach stop-hit, true-time edge, arrest impulse) and this was its only cost, **length was a free
    attribute for anything sword-length** — measured as the shared root cause of the rapier's civilian dominance
    (79% vs a 47% field; -25 pp of it ablates to reach) and the tracked off-plate spear dominance.
    NOW DERIVED, continuous from zero, in honest metres: `max(0, forward_extent(grip) - CLOSE_ENGAGE_M)`.
    `CLOSE_ENGAGE_M` is a property of BODIES, not of weapons — that is the whole difference between a derivation and
    a gate. `forward_extent` is the single owner shared with reach_base, and is grip-aware, so gathering in genuinely
    reduces the cost ("hand position on shaft").
    ⚠ MASS / POINT-OF-BALANCE / HEAD-WEIGHT ARE DELIBERATELY ABSENT, though they are equally real inputs to "how
    unwieldy is this": they are ALREADY charged, with a compressed power law, by `wield_heft`
    ((I_g/REC_I_REF)**WIELD_HEFT_EXP, "the tempo/stamina/strength COST of bringing a weapon to bear"), and the same
    grip-adjusted I_g is read again by `agility`, `recoverability_factor` and `_recovery_mode_commitment`. A factor
    here would be the FIFTH charge on one fact (§2.3's double-count rule), and it was measured unusable raw anyway:
    I_g spans ~1000x across the roster, so a linear inertia multiplier reads guandao 48.9 against its 2.10.
    MAGNITUDE: the metre-valued form lands the polearms near their old reach-unit values (spear 1.344 vs 1.297,
    guandao 1.725 vs 2.104), so POLE_CLOSE_K and CHOKE_DRIVE_REF need no re-anchoring — which is what keeps the
    guisarme@heavy floor (the failure that reverted the prior attempt at this) out of danger. The real change is that
    swords move 0 -> 0.27..0.51. `grip` forwards to forward_extent (I3, D3, JD-9); grip_target passes an explicit
    0.0 for its OWN drive input. Pure."""
    return max(0.0, forward_extent(c, cfg, grip) - cfg['CLOSE_ENGAGE_M'])
def can_choke(c, cfg):
    """Can the fighter gather in (regrip toward the centre)? DERIVED from the grippable length — a long shaft/grip
    yes, a short hilt or a block-headed club no. Thin bool over WP.grip_choke_max (the continuous primitive)."""
    return WP.grip_choke_max(c.w) > 0.0
def grip_target(c, closed, cfg):
    """The CONTINUOUS grip-position g* in [0,1] the fighter adopts (The Approach — footwork & stance), fully DERIVED
    from morphology — replaces the discrete adopt_stance string ('choke' was g>0, 'normal' g=0). Once the measure is
    CLOSED, a fighter GATHERS IN (g>0) in proportion to how unwieldy the weapon is in the close (close_unwieldiness),
    bounded by how far it can regrip (WP.grip_choke_max): a pole gathers up the haft; a rapier (short hilt) cannot
    and just suffers. At open measure g=0 (full reach). Pure (returns g; the wrapper writes grip_position).
    JD-9 FIXED-GRIP DRIVE INPUT (I3, D3, capstone finding M1, 2026-07-03 — designs/audit/2026-07-02-scene-combat-
    closing-distance-redesign/plan_r1_RATIFIED.md): once D3 makes reach_base grip-aware, this function's OWN drive
    term would otherwise read close_unwieldiness at the CURRENT grip_position — but grip_position THIS beat is
    exactly what this function is computing, closing a per-beat feedback loop (grip_position(n) depends on
    reach_base(grip_position(n-1)), the prior beat's own output) that iterates to a HARD, PERMANENT 2-cycle for
    every gathering pole (verified: spear flips 0<->0.865 every beat, forever). The drive term is pinned to
    grip=0.0 (open-measure reach) — a dedicated fixed-grip read used ONLY here; reach_base stays grip-aware for
    every OTHER consumer (str_demand/slip_inside/reach_sigma/close_tempo/reopen — the actual point of D3)."""
    if not closed:
        return 0.0
    drive = min(1.0, close_unwieldiness(c, cfg, grip=0.0) / cfg['CHOKE_DRIVE_REF'])     # 0..1: the more unwieldy in the close, the more you gather; FIXED grip=0.0 input (JD-9)
    return WP.grip_choke_max(c.w) * drive
def lunge_quality(c, cfg):
    """How well a weapon LUNGES (an extended-body thrust) — DERIVED, CONTINUOUS (Phase-3 Stage 2). A light, hand-
    balanced, point-concentrated weapon lunges well; the hard head-NAME gate ('point'/'cut_thrust') becomes the
    CONTINUOUS point_concentration weight (a blunt/cut head -> ~0, never an exact-0 category). Hand-balance is the
    DERIVED forward static moment (no hand-set pob_frac). Propensity in [0,1]; the wrapper rolls against it. Pure."""
    w=c.w
    pc      = w['geo']['point_concentration']                                               # CONTINUOUS thrust-ness (was the head-name gate)
    light   = (cfg['LUNGE_REF_MASS']/max(0.2,w.get('mass',1.0)))**cfg['MOMENT_MASS_EXP']    # NON-LINEAR lightness
    handbal = max(0.0, 1.0 - WP.derive(w)['PoB_frac'])                                       # DERIVED hand-balance (forward-balanced = poor lunge recovery)
    onehand = cfg['LUNGE_1H_BONUS'] if w['hands']==1 else cfg['LUNGE_2H_FACTOR']            # the classical lunge is one-handed
    return max(0.0, min(1.0, pc*light*handbal*onehand))
def stance_stability(c, fat, cfg): return cfg['FOOT_STANCE_K']*(balance_eff(c,fat,cfg)-3)

# ---------- defense modes (parry/dodge/wind) — DERIVED, no per-weapon table ----------
# The hand-authored per-weapon GATE parry/dodge/wind table is RETIRED (the worst primitive-law leak: defence
# behaviour authored per weapon name in engine code). The {parry,dodge,wind} caps now DERIVE from geometry + dynamics
# via WP.defense_affinities: parry from hand_guard x agility (a guarded, handy weapon parries fast); dodge from
# agility x one-handedness (light + free hand voids); wind from blade_guard x rigidity(cross_section) x bind-leverage
# (MoI) x edge-length. So a rapier's parry-1.0 EMERGES from its hand_guard, a poleaxe's wind from its blade-leverage.
assert set(GEOMETRY)>=set(WEAPONS), f"GEOMETRY missing weapons: {set(WEAPONS)-set(GEOMETRY)}"
def mode_sigma(mode, aggressor, defender, commit, read_win, fat_d, cfg):
    """defender's δσ for a chosen defensive mode. Reading universal; +2 axis-specific. Skills bias per-axis."""
    rd=reading(defender,cfg)-reading(aggressor,cfg)
    rfx=reflex(defender,cfg); tech=defender.history+defender.skill('technique')
    ftw=balance_eff(defender,fat_d,cfg); strn=defender.strength
    base=cfg['READ_K']*rd*(1.3 if read_win else 0.7)
    cap=WP.defense_affinities(defender.w)[mode]   # DERIVED from geometry+dynamics (retired the hand GATE table)
    if mode==V.DEF_PARRY:
        sig=cfg['PARRY_K']*(0.45*(rfx-3)+0.45*(tech-3))/3 + defender.skill(V.DEF_PARRY)
        # "don't parry with your hands!": an unguarded weapon's parry exposes the hand -> penalised; a guarded one
        # parries confidently. Scales the parry around a neutral simple-cross guard.
        sig += cfg['PARRY_GUARD_K']*(defender.w['hand_guard']-cfg['GUARD_NEUTRAL'])
        # [channel 5 / ED-PC-0052] DISPLACEMENT RESISTANCE. A parry is a weapon-to-weapon collision: a blade with more
        # moment about the hand is harder to beat aside, a hand-balanced one is cheap to displace. Same single-owner
        # fact as the bind (contact_moment_edge), its OWN gain — mirroring how the guard fact already carries three
        # gains (BIND_GUARD_K 0.55 / PARRY_GUARD_K 0.45 / WIND_GUARD_K 0.40) rather than one shared constant.
        sig += cfg['PARRY_MOMENT_K']*contact_moment_edge(defender, aggressor)
    elif mode==V.DEF_DODGE:
        sig=cfg['DODGE_K']*(0.30*(rfx-3)+0.70*(ftw-3))/3 + defender.skill(V.DEF_DODGE)
    else:               # wind (in the bind): fore/thumb-rings "enhance winding"
        sig=cfg['WIND_K']*(0.45*(tech-3)+0.45*(strn-aggressor.strength))/3 + defender.skill('bind')   # ED-PC-0035: the `+ CHOKE_BIND_K*choke` term is GONE — `choke` was hardcoded 0.0 by the only caller, so it was a structural zero (see config.py)
        sig += cfg['WIND_GUARD_K']*(defender.w['blade_guard']-cfg['GUARD_NEUTRAL'])
        sig += cfg['WIND_MOMENT_K']*contact_moment_edge(defender, aggressor)   # [channel 5] winding is in the bind — weapon on weapon, so the same moment fact applies (own gain)
    _deep=max(0.0,min(1.0,commit-3.0))     # CONTINUOUS commit response: 0 at <=3, ramps to 1 at >=4 (no integer cliff)
    _shallow=max(0.0,min(1.0,3.0-commit))  # 0 at >=3, ramps to 1 at <=2
    if mode==V.DEF_PARRY: sig-=0.25*_deep      # a deep commit is easier to parry (committed line); a shallow probe harder to catch
    if mode==V.DEF_DODGE: sig+=0.10*_deep-0.10*_shallow   # deep commit easier to void; a shallow feint harder to read for the dodge
    return (base+sig)*cap

def adef_cap(w, cfg, head=None, gap=None, grip=0.0, room=1.0):
    """Armour-defeat CAPABILITY — see core.adef_cap, which now OWNS this rule.
    [ED-PC-0038] Relocated to core so the DAMAGE path can consult the same capability the sigma path does. They had
    disagreed: a partisan (adef_cap 0.176, the worst on the board vs plate's 0.72 threshold) was landing 11 damage
    through a harness while a spear with BETTER capability (0.288) landed 3, because damage keyed on head mass and
    capability keyed on gap access. Duplicating the formula in core would have broken the repo's own "every rule
    lives once" invariant, so it moved and this delegates. Signature and results are unchanged."""
    return core.adef_cap(w, cfg, head=head, gap=gap, grip=grip, room=room)

def close_efficacy(pc, measure_gap, range_avail=1.0, closed=False, head=None):
    """The close-efficacy factor (D5): 1 - (1-pc)*f(measure_gap, range_avail). `pc` is the CANDIDATE element's own
    point_concentration (a pure-point element, pc~1, is barely touched; a broad-arc cutter, pc~0, is degraded up
    to the floor). `head=='point'` is grip-INVARIANT (returns 1.0 unconditionally) — the SAME rigid-body reasoning
    D2's phi_grip already applies to thrust-protection (R-3: a whole-weapon pc scalar does not cleanly separate
    arc-vs-thrust — bear_spear's whole-weapon pc is a moderate 0.55 despite being a pure-point weapon with NO
    authored mode_elements, so pc alone would wrongly degrade it; gating on the SELECTED head, not just pc,
    closes the same R-3 gap here). f is EXACTLY 0 — not approximate — at open measure (closed=False), when
    measure_gap is unknown (None, the default for any caller that hasn't wired a real measure — preserves
    byte-identical behaviour for every pre-I4 call site), or when measure_gap>=CLOSE_EFF_GAP_REF, so the lever is
    inert until the fight is genuinely in the close AND a real measure is threaded; f rises toward CLOSE_EFF_FLOOR
    as measure_gap shrinks toward 0 OR range_avail shrinks toward 0 (whichever is more constraining — either
    being crowded-in or having no swing room degrades a broad arc). Pure."""
    if head == V.HEAD_POINT:
        return 1.0
    if not closed or measure_gap is None:
        return 1.0
    gap_term = max(0.0, 1.0 - measure_gap / CLOSE_EFF_GAP_REF)
    room_term = max(0.0, 1.0 - range_avail)
    f = CLOSE_EFF_FLOOR * max(gap_term, room_term)
    return 1.0 - (1.0 - pc) * f

# ── swing-room (I5, D4, 2026-07-03 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
# plan_r1_RATIFIED.md): the AVAILABLE room to develop a swing this beat, derived from how close the exchange is.
# Two non-monotone-safe consumers, both reaching a channel int(round) cannot erase (C4 — never a heft multiply):
# commit_depth's Beta upper-support contraction and a swing-room legibility term (weighted by (1-sel_pc), a
# thrust unaffected). Never adds/reorders an rng draw.
RANGE_AVAIL_FLOOR = 0.3    # [SIM-CALIBRATE] floor on range_avail itself — even the tightest melee retains some room.
RANGE_COMMIT_PEAK = 0.85   # [SIM-CALIBRATE] range_avail fraction above which the commit-window stays at its FULL
                           #   upper bound (the C4 interior-optimum plateau: a little lost room doesn't shallow
                           #   commitment; only real crowding does — never a monotone-from-the-start ramp).
RANGE_COMMIT_FLOOR = 0.5   # [SIM-CALIBRATE] floor on the commit-window contraction factor.
LEGIB_SWING_ROOM_K = 0.3   # [SIM-CALIBRATE] swing-room legibility gain — weakly grounded (the brief flags the
                           #   absence of a treatise passage for cut-arc truncation); ships small, ablation-gated.
STOPHIT_RANGE_K = 0.3      # [SIM-CALIBRATE] the approach stop-hit's commitment-depth term (I5 gate #4) — a
                           #   stop-hit thrown with full extension threatens more than one snapped into a
                           #   cramped, rapidly-closing gap.

# ── facing (I6, D6, 2026-07-03 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
# plan_r1_RATIFIED.md): per-beat Combatant state, near-neutral (register-SOUND — no repair needed, a scaffolding
# increment). Keyed ONLY on stance/measure/grip (C2 — NEVER weapon class); ships small because C1 (polearm
# facing direction) is UNRESOLVED, so this must not become load-bearing. Two consumers: a lateral-void
# contribution into closing (Fiore fol. 39r) and a small profile term in reach_sigma (`[FIAT — C1]`).
FACING_VOID_K = 0.08       # [SIM-CALIBRATE] small lateral-void closing contribution.
FACING_PROFILE_K = 0.03    # [FIAT — C1 unresolved] small profile term in reach_sigma.
FACING_VOID_GAIN = 0.15    # [SIM-CALIBRATE] how much facing speeds the close (close_rate multiplier).

def facing_target(c, closed, cfg):
    """The per-beat facing state (I6, D6) — stance (closed/not) × grip_position × the U7 weapon-class facing REGIME
    (weapon_physics.facing_pref: a 1H fighter angles PROFILE, a 2H weapon SQUARES up). [U7/ED-PC-0020] the regime term
    is multiplicative and K=0-gated (FACING_REGIME_K), so at landing the multiplier is exactly 1.0 — byte-identical,
    and the C2 property (two weapons, same stance/grip → identical facing) still holds NUMERICALLY at K=0; the U9
    recalibration flips FACING_REGIME_K, at which point facing becomes weapon-class-aware (the C2 reversal, Jordan-
    resolved). Ships near-neutral (C1 polearm facing DIRECTION still unresolved). Pure (returns facing; wrapper writes c.facing)."""
    base = FACING_VOID_K * (1.0 if closed else 0.5)
    base = base * (0.5 + 0.5 * getattr(c, 'grip_position', 0.0))
    return base * (1.0 + cfg['FACING_REGIME_K'] * WP.facing_pref(c.w) * ABIL.ability_factor(c, 'facing_regime'))   # U7/ED-PC-0020 -> ACTIVATED U10/ED-PC-0022: weapon-class facing regime (1H profile / 2H square) is now LIVE (facing reads weapon class — the Jordan-resolved C2 reversal), AMPLIFIED by 'facing_regime' (Italian single-time profile guardia; factor 1.0 default). Conservative K (C1 direction still unresolved).

def range_utilization(c, measure_gap, cfg):
    """The AVAILABLE swing-room this beat, in [0,1], derived from how close the exchange is (measure_gap). 1.0 at
    open/roomy measure (measure_gap>=CLOSE_EFF_GAP_REF) or when measure_gap is unknown (None — preserves
    byte-identical behaviour for any caller that hasn't wired a real measure); floored (never truly zero — some
    minimal room always exists in melee) as measure_gap vanishes. Feeds c.range_avail (I1 scaffold; the wrapper
    writes it once per beat, pre-swap — range_avail is measure-derived, not form-derived, so it needs no
    post-swap refresh the way er/sel_* do). Pure."""
    if measure_gap is None:
        return 1.0
    return RANGE_AVAIL_FLOOR + (1.0 - RANGE_AVAIL_FLOOR) * max(0.0, min(1.0, measure_gap / CLOSE_EFF_GAP_REF))

def _commit_range_factor(range_avail):
    """The commit-window's Beta upper-support contraction factor (D4) — an interior-optimum-SAFE plateau: stays at
    1.0 (today's full [2,5] window) for range_avail>=RANGE_COMMIT_PEAK, so range_avail=1.0 (the I1/I5 default) is
    byte-identical; only degrades once room genuinely vanishes below the peak, floored. Never monotone from the
    very first unit of lost room (C4)."""
    r = max(0.0, min(1.0, range_avail))
    if r >= RANGE_COMMIT_PEAK:
        return 1.0
    return RANGE_COMMIT_FLOOR + (1.0 - RANGE_COMMIT_FLOOR) * (r / RANGE_COMMIT_PEAK)

# SELECT_PC_MIN RETIRED (morphology-rearch Phase B3, 2026-07-02). It was a magnitude THRESHOLD on point_concentration
# standing in for a fact the engine didn't yet have: whether a blunt haft's assembly HAS a real thrusting point at
# all (mace 0.02 -> no; poleaxe 0.78, modeled as ONE whole-weapon blunt token -> yes, smuggled in via this same
# token). Phase B2 gave every point-capable composite (poleaxe, bec_de_corbin, lucerne_hammer, ji, goedendag,
# guisarme, kama_yari, voulge) its own EXPLICIT point-tokened mode_element — the fact is now data, not inferred
# from a magnitude gate. "Affords a point iff it HAS a point-element" (the plan's own phrasing): a 'point' token in
# element_afforded now needs only geo['gap']>SELECT_EPS, same as every other mode. Verified byte-identical for the
# WHOLE roster at retirement time — no point-headed weapon without mode_elements had point_concentration<=0.10, and
# no blunt-headed weapon without mode_elements had point_concentration>0.10 (i.e. nothing was relying on either
# side of the old gate), so this changes no weapon's affordance, only how the affordance is DERIVED.

def _mode_elements(w):
    """The weapon's MODE-ELEMENTS — the located striking elements whose geometry affords fight-modes. Morphology-
    rearch Phase B2 (2026-07-02) populated real multi-element `mode_elements` lists for the 8 weapons whose parts
    afford genuinely different fight-modes (bec de corbin = hammer/blunt + beak/point + spike/point, each with its
    own per-element geometry grounded against Phase 0 specimen research — see designs/audit/2026-07-02-morphology-
    rearch-phase0/). A weapon with no explicit `mode_elements` (everything else — including composites whose extra
    mass elements are a mass-model subdivision only, e.g. flamberge's forte/tip/ricasso, or catching hardware like
    a partisan's wing-lugs) synthesizes ONE element carrying its own whole-weapon head token + baked geo, so the
    element-union below is the weapon's existing single-mode behaviour unchanged. Mirrors weapon_physics.
    _head_elements on the mass side. Pure."""
    els = w.get('mode_elements')
    if els:
        return els
    return [dict(head=w['head'], geo=w['geo'])]

def _element_mass_x(w, el):
    """The mass+position of a mode_element's SOURCE mass element, via its D0 `element_ref` (an explicit index into
    w['elements'], NOT list order — I0). Returns (mass_kg, x_m). Falls back to (0.0, 0.0) for the synthesized
    single-element case (_mode_elements' whole-weapon default, no element_ref) — never read (percussion_element_
    authority is only called on a real `element_ref`; the whole-weapon path uses WP.percussion_authority(w)
    directly)."""
    ref = el.get('element_ref')
    if ref is None:
        return 0.0, 0.0
    e = w['elements'][ref]
    return e['mass_kg'], e['x_m']

MODE_PERC_MIN = 0.5       # [DESIGN, U2/ED-PC-0009, 2026-07-08] per-primitive percussion-affordance floor for the
                          #   graded secondary blunt check (weapon_physics.percussion_authority's non-blunt branch,
                          #   the Mordhau/reversed-grip option). Set well below the ~1.4-1.8 range every eligible
                          #   two-handed sword reads (see reversed_grip_percussion) and well above 0 (one-handed
                          #   swords and daggers, which the function gates to exactly 0 — no comparable technique
                          #   is attested for them in the sourced material).
# ── close-efficacy (I4, D5, 2026-07-03 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
# plan_r1_RATIFIED.md): a broad arc-requiring swing (low per-element point_concentration) collapses in tight
# quarters; a point-selected thrust barely degrades (half-swording is the norm in the close). [SIM-CALIBRATE
# throughout — the brief flags the absence of a treatise passage for cut-arc truncation; ships small and
# ablation-gated, not load-bearing, per D4].
CLOSE_EFF_GAP_REF = 6.5   # [SIM-CALIBRATE] the measure_gap scale the close-quarters ramp saturates over. NOTE this
                          #   used to be justified as "shares CLOSE_REACH_REF's magnitude — the same 'how close is
                          #   close' reference". That justification is RETIRED with CLOSE_REACH_REF itself
                          #   (ED-PC-0053): the shared value was a coincidence of two different scales, not a shared
                          #   fact — this one is a measure_gap scale, that one was a reach_base threshold including
                          #   the body offset L0. This constant is now unanchored and stands on its own calibration;
                          #   it is a candidate for the same fiat-to-derived treatment.
CLOSE_EFF_FLOOR = 0.5     # [SIM-CALIBRATE] cap on f(measure_gap, range_avail): even the tightest quarters/least
                          #   room never fully collapses a broad element's affordance.

MODE_EDGE_MIN = 0.15      # [DESIGN, U2/ED-PC-0008, 2026-07-08] per-primitive cut-affordance floor for the GRADED,
                          #   head-independent secondary check (a weapon whose native head ISN'T a cut category
                          #   can still afford an incidental cut if its own geo['cut'] clears this). Consolidation_
                          #   v1.md §2.3 already assumed this exact value: "sides==0 => ek<=0.1 < MODE_EDGE_MIN
                          #   ~=0.15" (the roster's own edgeless-consistency invariant, V14). Verified against the
                          #   full roster post-geometry.cut_factor's floor drop: mace/staff read 0.0, the needle
                          #   class (stiletto/estoc/rondel, ek<=0.1) reads 0.02-0.05, comfortably below; rapier
                          #   (ek=0.30) reads 0.30, comfortably above.
MODE_TIP_MIN = 0.15       # [DESIGN, U2/ED-PC-0009, 2026-07-08] per-primitive thrust-affordance floor, the JD-9
                          #   resolution. Matched to MODE_EDGE_MIN for a clean, symmetric pair. Verified against
                          #   the full roster post-geometry.thrust_factor's floor drop: mace (0.02) and staff
                          #   (0.04) read comfortably below; every weapon test_greatsword_katana_sabre_afford_
                          #   thrust names reads 0.26+ (sabre, the lowest of the three); the heavily-curved-slasher
                          #   family (shamshir/pulwar/scimitar) correctly collapses toward the floor too (curvature
                          #   offsets the point off the hand-target line — HEMA: these are cutting-primary blades).
SELECT_EPS = 0.05         # [DESIGN] affordance floor on a derived per-mode effectiveness: a mode is afforded iff its
                          #   derived effectiveness exceeds this (so a vanishing mode is not even a candidate). Small.
                          #   Still used for each mode's OWN native-head branch below (unchanged from pre-U2).

# ── THE MODE-SELECTION RECORDS — ONE canonical field order each (ED-PC-0042 / I3) ────────────────────────────────
# The `sel_*` bundle used to be a BARE POSITIONAL TUPLE that widened three times as the model grew (element_afforded
# emitted 5 fields, or 7 for cut_thrust; afforded_heads normalised to 8; select_mode returned 6 in a DIFFERENT order),
# so every consumer carried its own index arithmetic plus width guards (`heads[hd][6] if len(heads[hd])>6 else None`)
# and ED-PC-0037.1 had to APPEND the per-arm magnitudes AFTER `element_ref` rather than beside the other magnitudes,
# because inserting a field would have silently transposed every reader. That is precisely the positional fragility
# `core.strike` was made a KEYWORD chokepoint to eliminate ("the 9-arg positional surface — the transposition-bug
# class — exists in exactly one place"), re-grown one field at a time. Naming the fields restores that idiom on the
# selection side: the order is declared HERE, once, and read by NAME everywhere downstream.
#
# `namedtuple`, deliberately, not a dataclass/dict: a HeadOption IS a tuple, so indexing, slicing, iteration, `len`,
# `list(...)`, `==` against a plain tuple and JSON array-encoding are all unchanged — golden_element_parity.json's
# `select_mode` rows (compared as `list(...) == <json list>`), the `[:2]`/`[1]`/`[:6]` callers in tests, and
# workbench/catalogue.py's `isinstance(r, tuple)` branch keep working byte-for-byte.
#
# ⚠ THE TWO ORDERS DIFFER, and that asymmetry is exactly why they are named. HeadOption leads with `eff`, ModeSelection
# leads with `dm`; `element_ref`/`eff_cut`/`eff_thrust` exist only on HeadOption. ModeSelection's order is PINNED by
# golden_element_parity.json and by ~15 six-way unpacks in tests — do not reorder it; add to the END if it must grow.
HeadOption = namedtuple('HeadOption', 'eff dm gap perc pc element_ref eff_cut eff_thrust',
                        defaults=(None, None, None))   # element_ref: filled by afforded_heads (the element's identity, not the element's own knowledge); eff_cut/eff_thrust: the ELEMENT-LOCAL per-arm magnitudes, cut_thrust only (ED-PC-0037.1)

def element_afforded(el, w, grip=0.0, room=1.0):
    """The afforded head TOKENS of ONE striking element — the per-element scope of the whole-weapon branch logic.
    Morphology-rearch Phase B3 (2026-07-02): a 'point' token affords iff geo['gap']>SELECT_EPS, same floor as
    every other mode — no separate point_concentration THRESHOLD (SELECT_PC_MIN, retired above). Being tokened
    'point' at all (a B2 authoring judgment call, grounded per-element) is now the affordance signal; the old
    threshold stood in for that fact before composites had explicit point-elements. The 'blunt' branch no longer
    smuggles in a secondary point-affordance from its OWN point_concentration — every weapon that needs a blunt-
    plus-point split (poleaxe, bec_de_corbin, lucerne_hammer, goedendag, guisarme's cousin-shape) now expresses it
    as a SEPARATE point-tokened mode_element (B2), not a magnitude reading on the blunt token.
    WIDENED RETURN (I2, D2b, R-7 + capstone M2, 2026-07-03 — designs/audit/2026-07-02-scene-combat-closing-
    distance-redesign/): each token now maps to a 5-tuple `(eff, dm, gap, perc, pc)` — the winning element's OWN
    baked `geo['gap']`/`geo['point_concentration']` (never the whole-weapon scalar, R-3/M-02) and its PERCUSSION
    (a per-element application of the percussion_authority FORM via `_element_mass_x`'s D0 `element_ref` mass
    lookup — closes the `[PHASE-B6 PENDING]` precision gap: a lucerne_hammer's two blunt elements now read their
    OWN mass+position, not the same whole-weapon value). Both `perc` and the blunt token's `eff` are grip/room-
    degraded (the SAME mode-split Phi as D2's heft, JD-4); every other token's `eff`/`gap` stay the STATIC
    per-element primitives (gap/cut do not degrade with grip in R1 — only the swing-moment-bearing quantities
    do). SHAPE (ED-PC-0042/I3): every token maps to a `HeadOption` record (defined above this function) — the
    same eight named fields for every branch, so no consumer has to know a per-branch width. `element_ref` is left
    None here (the element does not know its own index) and filled by the caller, afforded_heads.
    GRADED, HEAD-INDEPENDENT SECONDARY AFFORDANCES (U2/ED-PC-0008/0009, 2026-07-08): the native-head branch
    below is UNCHANGED (same tokens, same thresholds, same DELIVERY-multiplier identity — cut_thrust's atomic
    combo now compares cut against geo['thrust'] instead of geo['gap'], the JD-9 "wire geo['thrust']" fix,
    keeping gap itself threaded separately for the armour-gap math). AFTER it runs, three independent checks
    (one per physical family: edge, tip, blunt) ask "does this element's OWN geometry clear the graded floor,
    regardless of what its native head already claimed?" and ADD a token if so — geometry, not the `head`
    label, gates every mode; a weapon's `head` only decides which TOKEN NAME a mode's own native family uses
    (preserving the existing DELIVERY-multiplier routing for cut_thrust/straight_cut/curved_cut/point). A
    generic 'cut'/'point' token is used when the geometry supports a mode the native head's OWN family didn't
    already claim (e.g. rapier, head='point', can ALSO afford a weak edge; greatsword, head='straight_cut',
    can ALSO afford a thrust) — never overwrites a native token, only fills a gap via dict.setdefault."""
    geo=el['geo']; head=el['head']
    gap=geo['gap']; pc=geo['point_concentration']
    heads={}
    if head==V.HEAD_CUT_THRUST:                                       # versatile blade: keep atomic (internal max)
        # [ED-PC-0037.1] carry the ELEMENT's OWN cut/thrust alongside the blended max. The blend stays in `eff`
        # because sel_eff's downstream contract expects it; `eff_cut`/`eff_thrust` are the per-arm truth, so the
        # versatility contest can be scored on the element that is actually being swung rather than on the
        # whole-weapon bake (a guisarme's BILL is cut 0.76 / thrust 0.19; the weapon scalar says 0.64 / 0.41,
        # which credits a hook with a point it does not have — the M-02 object confusion this docstring forbids).
        heads[V.HEAD_CUT_THRUST]=HeadOption(max(geo['cut'], geo['thrust']), 'shear_or_puncture', gap, None, pc,
                                            eff_cut=geo['cut'], eff_thrust=geo['thrust'])
    elif head in V.PURE_CUT_HEADS:                                   # pure cutter
        if geo['cut']>SELECT_EPS: heads[head]=HeadOption(geo['cut'], V.MODE_SHEAR, gap, None, pc)
    elif head==V.HEAD_POINT:                                         # a real point (element-tokened, not inferred)
        if geo['gap']>SELECT_EPS: heads[V.HEAD_POINT]=HeadOption(geo['gap'], V.MODE_PUNCTURE, gap, None, pc)
    elif head==V.HEAD_BLUNT:                                         # striking head
        ref = el.get('element_ref')
        em, ex = _element_mass_x(w, el) if ref is not None else (0.0, 0.0)
        if em > 1e-9:                                                 # a real located mass element (D0 element_ref)
            pa=WP.percussion_element_authority(w, em, ex, grip=grip, room=room)
        else:                                                         # no element_ref, OR a zero-mass geometric marker
            pa=WP.percussion_authority(w, grip=grip, room=room)       # (e.g. goedendag's club-body element carries
                                                                        # its striking mass on the haft record, not
                                                                        # itself) — whole-weapon fallback, unchanged
        if pa>SELECT_EPS: heads[V.HEAD_BLUNT]=HeadOption(pa, V.MODE_PERCUSSION, gap, pa, pc)

    # ── graded secondary affordances (U2/ED-PC-0011, 2026-07-08) ──
    # Both checks were tried earlier this session and reverted pending fixes now landed:
    #   - percussion: core.coupling's DELIVERY['blunt']=1.6 previously ignored percussion MAGNITUDE against
    #     cloth/none (only mail/plate got the authority-scaled transmit), so a weak candidate incorrectly won
    #     selection against unarmoured targets. FIXED in core.py (the mat-restriction dropped, byte-identical
    #     for mace/poleaxe — verified: their perc sits at/near PERC_AUTH_REF so the scaling clamps to 1.0 at
    #     every tier). With that fix, a weak percussion candidate now correctly LOSES to a weapon's own cut/
    #     thrust against soft targets and only wins where the edge/point genuinely can't help — exactly the
    #     HEMA framing (Mordhau as a response to armour defeating the edge, not a general preference).
    #   - cut/point: re-validated against the roster (see ED-PC-0011) — the previously-blocking bear_spear
    #     case (head='point', an authored real edge on a "bear spear" — historically many boar/bear spears
    #     carried genuine wing/blade-like heads for a following cut, not pure thrusters) is a CORRECT emergent
    #     result, not a regression: test_thrust_protection_grip_invariant's premise (spear-class weapons always
    #     select 'point') was narrowed to the two weapons that still hold (spear, yari — genuinely point-only
    #     geometry) rather than silently preserved by suppressing bear_spear's own authored edge.
    if head != V.HEAD_BLUNT:
        pa_secondary = WP.percussion_authority(w, grip=grip, room=room, sel_head=head, sel_pc=pc)
        if pa_secondary>MODE_PERC_MIN:
            heads.setdefault(V.HEAD_BLUNT, HeadOption(pa_secondary, V.MODE_PERCUSSION, gap, pa_secondary, pc))
    if head not in V.CUT_FAMILY_HEADS and geo['cut']>MODE_EDGE_MIN:
        heads.setdefault(V.HEAD_CUT, HeadOption(geo['cut'], V.MODE_SHEAR, gap, None, pc))
    if head not in V.THRUST_FAMILY_HEADS and geo['thrust']>MODE_TIP_MIN:
        heads.setdefault(V.HEAD_POINT, HeadOption(geo['thrust'], V.MODE_PUNCTURE, gap, None, pc))
    return heads

def afforded_heads(w, grip=0.0, room=1.0):
    """The set of head TOKENS this weapon can fight in — the UNION over its mode-elements of each element's
    afforded tokens (best effectiveness per token). Element-union structure so a multi-element head (bec de
    corbin, lucerne_hammer, ji, goedendag, guisarme, kama_yari, voulge, poleaxe) affords each of its elements'
    modes; a single-mode weapon's synthesized one-element list reproduces its prior whole-weapon behaviour
    unchanged. Each token maps to a `HeadOption` record (eff, dm, gap, perc, pc, element_ref, eff_cut, eff_thrust
    — defined above element_afforded, ED-PC-0042/I3) — WIDENED I2/D2b (R-7 + capstone M2): the winning element's own
    gap/perc/pc + its identity, so select_mode can emit them (sel_gap/sel_perc/sel_pc); ED-PC-0037.1 added the
    element-local per-arm magnitudes. No per-weapon list, no name/kind branching (the L0 primitive-law). Pure."""
    heads={}
    for el in _mode_elements(w):
        for tok,opt in element_afforded(el, w, grip=grip, room=room).items():
            # the element knows its own magnitudes; only the CALLER knows which element it was, so element_ref is the
            # one field filled here (`_replace`, not a re-spelled tuple — nothing can transpose in a keyword copy).
            if tok not in heads or opt.eff>heads[tok].eff:
                heads[tok]=opt._replace(element_ref=el.get('element_ref'))
    if not heads:                                                    # degenerate fallback: never strip all modes
        h=w['head']
        heads[h]=HeadOption(0.0, core.HEAD_MODE.get(h, V.MODE_SHEAR), w['gap'], None, w['geo']['point_concentration'])
    return heads

def selected_arm_magnitudes(c, head, grip=None, room=None):
    """The ELEMENT-LOCAL (cut, thrust) magnitudes of the currently-selected head — (None, None) for any head with no
    two-armed contest. [ED-PC-0037.1] core.strike needs these to grade a cut-and-thrust blow on the element actually
    being swung. It cannot read them from select_mode's return (that tuple's 6-wide shape is depended on by the
    wrapper, the goldens and a dozen tests) and it cannot import this module (core is imported BY it — a cycle), so
    the wrapper writes them onto the combatant alongside the other sel_* fields, exactly as it does for sel_gap/
    sel_perc/sel_pc. Without this, core.strike fell back to the WHOLE-WEAPON bake and re-created the object confusion
    at the damage path even after select_mode was fixed: a guisarme's bill (element 0.76/0.19) was being damaged as
    though it carried the weapon's 0.41 thrust. Pure."""
    h = afforded_heads(c.w, grip=(getattr(c, 'grip_position', 0.0) if grip is None else grip),
                       room=(getattr(c, 'range_avail', 1.0) if room is None else room)).get(head)
    return (h.eff_cut, h.eff_thrust) if h is not None else (None, None)

# select_mode's OUTBOUND record — the six fields the wrapper writes onto the combatant as sel_dmg/sel_head/sel_gap/
# sel_perc/sel_pc/sel_eff, in that order. PINNED (see HeadOption's note): golden_element_parity.json stores these rows
# and ~15 tests unpack them six-wide. Field names match the combatant's sel_* fields minus the prefix, so the wrapper's
# assignment is readable as a pairing rather than a positional coincidence.
ModeSelection = namedtuple('ModeSelection', 'dm head gap perc pc eff')

def select_mode(c, defender_armor, closed, cfg, measure_gap=None, grip=None, room=None):
    """PURE per-exchange use-mode selection. Derives the afforded head tokens from c.w's primitives (afforded_heads),
    then greedily SELECTS the one whose resulting damage-coupling vs defender_armor is highest — the effectiveness-vs-
    armour baseline the design §3 names ('exactly the existing coupling/adef_cap max(), generalized from 2 modes to
    N'). Reproduces every single-mode weapon's current head (rapier->point, sabre->curved_cut, arming/longsword/
    dagger->cut_thrust, mace/staff->blunt) and the poleaxe (the one weapon that affords >1 head: blunt+spike). SITUATIONAL
    GAP GAME [2026-06-30]: the greedy comparator threads the SELECTED element's own derived gap_precision into the
    puncture path (core.coupling gap_prec=), so it SEES the gap-thrust's real GAP-SEEKING effectiveness vs the armour.
    The poleaxe now SELECTS its spike vs plate (the reach-ladder — the historically-correct armoured kill: thrust to
    the visor/armpit/groin), because its stiff concentrated point (gap 0.78) out-couples its own hammer at the gaps;
    a rondel-type (gap 0.84) selects the spike even harder; a mace (blunt-only, no afforded point) still hammers; a
    staff (weak point, weak authority) stays weak. All EMERGENT from the derived gap_precision — no weapon name.
    WIDENED RETURN (I2, D2b, R-7 + capstone M2; extended to 6 by U2/ED-PC-0011): `(dm, h, sel_gap, sel_perc, sel_pc,
    sel_eff)` — the four extra fields default to the whole-weapon w['gap']/WP.percussion_authority(w)/whole-weapon
    point_concentration/0.0 for a single-mode weapon (behaviour-preserving until intended; verified at I2's
    acceptance gate #5). Threads `c.grip_position`/`c.range_avail` (default 0.0/1.0 — I1 scaffold) into
    afforded_heads so the SELECTION itself (not just the eventual damage) reflects the wielder's current
    circumstance. `eff_head` is the head TOKEN routed downstream (core.strike/adef_cap/legibility), damage_mode
    the resolved 'percussion'/'shear'/'puncture'. `sel_eff` is the winning element's own derived cut/thrust
    magnitude — read by core.strike (as sel_eff) to scale core.coupling's 'cut' token DELIVERY (see CUT_AUTH_REF);
    inert for every other head. The six are returned as the named `ModeSelection` record (defined just above —
    ED-PC-0042/I3; it IS a tuple, so every existing positional caller is unchanged). The wrapper writes all six onto
    the combatant at BOTH call sites (mutation stays wrapper-owned).
    CLOSE-EFFICACY (I4, D5): `measure_gap` (None default — behaviour-preserving for every caller that hasn't wired
    a real measure) now genuinely reaches the comparator via close_efficacy, weighted by each CANDIDATE's own
    point_concentration — a broad arc-requiring swing collapses in tight quarters; a point-selected thrust barely
    degrades. `closed`/`measure_gap`/`range_avail` were previously received (`closed`) and ignored."""
    w=c.w
    # `grip`/`room` follow reach_base's JD-9 override idiom: None (the default, and every wrapper call) reads the
    # combatant's LIVE circumstance; an explicit value pins the geometry for a HYPOTHETICAL evaluation that must not
    # depend on live state (represent_measure_p asks "what would this weapon present at OPEN measure?" — ED-PC-0034).
    grip=getattr(c,'grip_position',0.0) if grip is None else grip
    room=getattr(c,'range_avail',1.0) if room is None else room
    heads=afforded_heads(w, grip=grip, room=room)
    if len(heads)==1:                                                # single afforded mode: no choice (the common case)
        h=next(iter(heads))
    else:
        # greedy: the mode delivering the most damage-coupling THROUGH this armour, weighted by close-efficacy (D5:
        # a broad arc that cannot fully develop in the close is discounted, a thrust barely) AND discounted by its
        # UNDEFENDED-TIME (T_vuln, ED-PC-0027). perc carries the blunt authority, gap_prec the thrust's GAP-SEEKING
        # plate-defeat. The T_vuln safety factor 1/(1+EXPOSE_SELECT_K*max(0,exposure-1)) prices the vulnerability window
        # of each mode: a heavy committed SWING (low sel_pc, large swing-arc MoI) leaves you open far longer than a
        # controlled THRUST (high sel_pc, retracts on-line) — so a fighter trades damage vs exposure and, in the 1v1
        # (no ally to cover a swing — Jordan 2026-07-23: the poleaxe's swing was a man-advantage move, the THRUST its
        # dueling staple), thrust-capable weapons prefer the point EMERGENTLY (the poleaxe spikes at every tier), while
        # a pure cutter with no real point keeps cutting. A mode with exposure<=1 (a clean thrust) is undiscounted.
        h=max(heads, key=lambda hd: core.coupling(hd, defender_armor,
                  perc=heads[hd].perc if heads[hd].perc is not None else core.PERC_AUTH_REF, gap_prec=heads[hd].gap,
                  eff=heads[hd].eff, thrust_auth=core.thrust_authority(w['head_len']),
                  eff_cut=heads[hd].eff_cut, eff_thrust=heads[hd].eff_thrust)
              * close_efficacy(heads[hd].pc, measure_gap, room, closed, head=hd)
              / (1.0 + cfg['EXPOSE_SELECT_K'] * max(0.0, _recovery_mode_commitment(w, grip, cfg, sel_pc=heads[hd].pc, room=room) - 1.0)))
    if h==V.HEAD_CUT_THRUST:
        # atomic versatile head: the damage coupling already takes max(cut, half-sword gap-thrust) internally, so the
        # head token is unchanged. The REPORTED mode (legibility only) follows the documented armour-conditional shift
        # the engine has always modelled: a cut-thrust sword SWINGS (cuts) — reads easy — until it must half-sword-
        # thrust to the gaps vs a harness (medium/heavy), then reads hard. This reproduces the prior legibility exactly.
        # [ED-PC-0036] The label is READ FROM the coupling contest itself (core.cut_thrust_arm, its single owner), so
        # damage and reported mode cannot diverge. This used to be an independent armour rule ('shear' at none/light,
        # else 'puncture') that contradicted what coupling actually paid — the thrust arm won at EVERY tier, so a
        # cut-and-thrust sword was damaged as a thrust and READ as a swing, with legibility (thrust HARD 0.80, swing
        # EASY 1.25) scoring a mode the fighter never performed. Deriving it also captures cases no armour rule can
        # express: a poor-edged weapon (spetum, eff 0.63 < CUT_AUTH_REF) correctly prefers its point even unarmoured.
        dm = core.cut_thrust_arm(core.TIER2MAT[defender_armor], 'full', heads[h].gap,
                                 heads[h].eff_cut, heads[h].eff_thrust, core.thrust_authority(w['head_len']))[1]
    else:
        dm=core.HEAD_MODE.get(h, V.MODE_SHEAR)
    sel = heads[h]   # the WINNING option's own record; the transposition below is deliberate and lives in exactly one place
    return ModeSelection(dm=dm, head=h, gap=sel.gap, perc=sel.perc, pc=sel.pc, eff=sel.eff)

def armor_defeat_sigma(aggressor, defender, cfg):
    """In armour, the weapon that CAN defeat the armour controls the exchange. Net-sigma adjustment for the aggressor
    vs the defender's armour: capability ABOVE the per-tier threshold = control (+); below = the armour SHIELDS (−).
    The threshold RISES with armour (monotonically harder). Zero unarmoured (ADEF_W['none']=0). Reads the aggressor's
    SELECTED mode-head (sel_head, set by the wrapper from select_mode) so the armour-defeat path scores the mode the
    wielder actually committed to; falls back to the native head when unset (byte-identical). CIRCUMSTANCE-DEGRADED
    (I2, D2b): also threads sel_gap/grip_position/range_avail so this resolves the SAME grip/gap as core.strike."""
    a=cfg['ADEF_W'][defender.armor]
    if a==0.0: return 0.0
    cap=adef_cap(aggressor.w, cfg, getattr(aggressor,'sel_head',None), gap=getattr(aggressor,'sel_gap',None),
                 grip=getattr(aggressor,'grip_position',0.0), room=getattr(aggressor,'range_avail',1.0))
    # [ED-PC-0046] THIS SITE DELIBERATELY KEEPS THE RAW, SIGNED cap — do not "consistency-fix" it to match the
    # max(0, cap) clamp in reach_threat/represent_measure_p (or core.damage's knee, ED-PC-0039). Those three take a
    # capability DEFICIT, where a negative cap is a category error: ADEF_CUT = -0.9 is a sigma-domain CONTROL
    # PENALTY, not a capability magnitude. THIS function IS the sigma domain — it is the term ADEF_CUT was
    # calibrated for, and it is signed on both sides by design (capability above threshold = control, below =
    # the armour shields). Clamping here would delete the cutter's control penalty entirely.
    return a*(cap - cfg['ADEF_THRESHOLD'][defender.armor])

def reach_threat(longer, defender, cfg):
    """FIX-1 — the factor by which a LONGER weapon's structural-reach advantage DECAYS when it CANNOT defeat the
    defender's armour: a head that can't threaten the harness can't hold a closing armoured man off — he walks
    through the reach (the differential reference's 'armour forces the fight down the reach-ladder'). DERIVED from
    the armour-defeat capability vs the tier threshold; A0-SAFE BY CONSTRUCTION (ADEF_W['none']=0 -> factor 1.0, so
    unarmoured reach is untouched with no special-case). A weapon that CAN defeat the tier (mace/poleaxe/dagger-gap)
    clears the threshold -> deficit 0 -> factor 1. Returns a factor in [REACH_THREAT_FLOOR, 1]. REACH_DECAY_K is
    [FIAT — designer-set; tightened to avoid triple-counting REACH_W + ADEF_CUT]."""
    aw=cfg['ADEF_W'][defender.armor]
    if aw==0.0: return 1.0
    cap=adef_cap(longer.w, cfg, head=getattr(longer,'sel_head',None), gap=getattr(longer,'sel_gap',None),
                 grip=getattr(longer,'grip_position',0.0), room=getattr(longer,'range_avail',1.0))
    # CLAMP THE CAPABILITY AT 0 BEFORE TAKING THE DEFICIT [ED-PC-0046] — the same fix core.damage's penetration knee
    # already carries (ED-PC-0039), which was applied there ONLY and left the two sigma-path deficits unclamped.
    # adef_cap returns a NEGATIVE number for a pure cutter (ADEF_CUT = -0.9), and that -0.9 is a sigma-domain CONTROL
    # PENALTY calibrated for armor_defeat_sigma's +/- scale, NOT a capability magnitude. Read raw it tripled the
    # bardiche's medium deficit (0.45 -> 1.35) and decayed its reach threat 0.843 -> 0.5275 — the reach-ladder was
    # punishing a cutter twice for the same fact, once as ADEF_CUT in armor_defeat_sigma and again here. "Cannot
    # defeat the harness" is a floor at ZERO capability, not an unbounded negative one; the grading of HOW badly a
    # cut fails against a harness is ADEF_CUT's job in the sigma path, not this decay's.
    deficit=max(0.0, cfg['ADEF_THRESHOLD'][defender.armor] - max(0.0, cap))
    return max(cfg['REACH_THREAT_FLOOR'], 1.0 - cfg['REACH_DECAY_K']*aw*deficit)

def represent_measure_p(longer, shorter, cfg, TR, measure_gap=None):
    """P(a reach weapon RE-PRESENTS its point at open measure entering a fresh engagement, rather than being crowded to
    grips). A new engagement (turn) nominally opens at measure — the fighters have broken and reset — but a reach weapon
    only KEEPS that measure if the (re-)closing opponent still RESPECTS the point. An armoured closer who does not fear a
    point that cannot defeat his harness crowds in and STAYS glued, so the reach weapon never recovers its distance and
    the fight stays close (where the shorter, bind-dominant weapon decides it). The fade shares reach_threat's grounded
    structure — the armour-defeat DEFICIT (how far the weapon's realised armour-defeat capability falls short of the
    tier threshold) weighted by the armour's substance (ADEF_W) — but a STEEPER exp() response, because holding a
    determined armoured man at the point over a whole engagement is a harder ask than merely deterring one stop-hit
    (reach_threat, which is deliberately shallow to avoid triple-counting, floors at 0.35 — too generous to CROWD a
    pure point off plate). So:
      • UNARMOURED (ADEF_W 0) -> 1.0: the reach weapon always re-presents — reach dominates off-plate, as it must.
      • LIGHT (gambeson, low ADEF_W) -> ~1.0 even for a non-'defeating' point: soft armour still respects a thrust, so
        crowding barely happens (the reach edge survives — light-tier reach invariants hold).
      • PLATE (heavy ADEF_W) -> collapses for a PURE POINT (spear/yari, large deficit) so it is crowded almost every
        engagement (a spear cannot keep a determined plate-armoured man at its point — the honest physics), while a
        gap-defeating reach weapon (poleaxe spike ~clears the tier; guisarme bill smaller deficit) still re-presents
        often enough to bring its plate-defeat to bear. This is the emergent discriminator the equal per-hit damage
        could not provide: at plate, spear and guisarme wound alike per hit, but the guisarme EARNS more presentations.
    Lifted mildly by the wielder's FOOTWORK (Agility differential) — nimble feet break and re-make measure — bounded so
    armour, not stats, dominates the gate (0 for a stat mirror). Reuses adef_cap (single owner of armour-defeat) on the
    PRESENTING mode this derives itself (below). REPRESENT_DECAY_K / REPRESENT_FOOT_K [SIM-CALIBRATE]. Pure."""
    aw = cfg['ADEF_W'][shorter.armor]
    if aw <= cfg['ADEF_W'][V.TIER_LIGHT]:
        return 1.0   # CROWDING IS A HARD-ARMOUR PHENOMENON: soft gambeson (and bare) still respects a thrust, so a reach
                     # weapon is never crowded off measure through it (reach survives at none/light — the light-tier reach
                     # dominance the invariants require). Only mail/plate let a closer fearlessly crowd the point. Returning
                     # exactly 1.0 (not ~0.99) also means the wrapper consumes NO rng draw here, so the gate is inert on the
                     # RNG stream at light — where the tradition-lever texture regression runs.
    # PRESENTING MODE (ED-PC-0034 bugfix). Derive — purely, here — the mode this weapon WOULD present at OPEN measure,
    # instead of reading the live sel_*/grip state. This gate is evaluated at ENGAGEMENT START, outside the per-beat loop
    # that refreshes sel_*, so the live fields still carry the PRIOR engagement's closed-phase selection (or, on the very
    # first engagement, nothing — so adef_cap fell back to the bare NATIVE head). Measured consequence: a multi-mode
    # weapon whose native head is a CUTTER read as maximally crowded on engagement 1 and differently later — katana
    # 0.000 -> 0.274, guisarme 0.092 -> 0.236, hook_sword 0.000 -> 0.425 for the identical matchup. That is the same
    # state-carryover defect class ED-PC-0033 fixed for grip_position, reintroduced one call up. A weapon is gated on
    # the point it would actually present, so the geometry is the OPEN-measure one explicitly: grip 0.0 (full extension,
    # nothing gathered) and room 1.0 (open measure) — path-independent by construction, never a stale read.
    # [ED-PC-0036, adversarial-review correction] The geometry is the engine's HONEST opening geometry, not a
    # counterfactual. grip=0.0 is right — a fresh engagement opens at full extension, nothing gathered — but the first
    # revision also pinned room=1.0, which the engine never occupies at this moment: the wrapper's own beat-1 room is
    # range_utilization(measure_gap) = FLOOR + (1-FLOOR)*min(1, gap/CLOSE_EFF_GAP_REF), i.e. ~0.43-0.66 in every cell
    # where this gate is live (room=1.0 would need a reach differential >= CLOSE_EFF_GAP_REF, which no matchup has).
    # That pin was not inert: at guisarme-vs-arming/medium it made select_mode grade the BILL'S CUT (cut_thrust) rather
    # than the point, dropping the gate 1.0 -> 0.413 and the matchup ~4pp — against the gate's own fiction, which is
    # whether the closer still respects the POINT. Deriving room from measure_gap keeps full path-independence (it is a
    # pure function of a local, never of carried state) AND makes the measure_gap parameter genuinely load-bearing.
    room = range_utilization(longer, measure_gap, cfg)
    sel = select_mode(longer, shorter.armor, False, cfg, measure_gap=measure_gap, grip=0.0, room=room)
    cap = adef_cap(longer.w, cfg, head=sel.head, gap=sel.gap, grip=0.0, room=room)
    # CLAMP THE CAPABILITY AT 0 BEFORE TAKING THE DEFICIT [ED-PC-0046] — same rule, same reason as reach_threat above
    # and core.damage's knee (ED-PC-0039): a raw negative adef_cap is ADEF_CUT's sigma-domain control penalty, not a
    # capability magnitude. Unclamped, the STEEPER exp() response here amplified the error far harder than the linear
    # reach decay does: bardiche vs arming at medium read 0.0089 — a pure cutter crowded off measure 99.1% of
    # engagements — against 0.207 clamped, a 23x move on the gate.
    deficit = max(0.0, cfg['ADEF_THRESHOLD'][shorter.armor] - max(0.0, cap))
    base = exp(-cfg['REPRESENT_DECAY_K'] * aw * deficit)
    foot = 1.0 + cfg['REPRESENT_FOOT_K']*(longer.agi - shorter.agi)   # footwork differential; 0 for a stat mirror
    return max(0.0, min(1.0, base*foot))

def leverage(c, cfg):
    """Lever-arm primitive: capacity to redirect/bind/displace another weapon. EXPLICIT hand-to-contact lever arm
    (Phase-3 grounding fix): the ABSOLUTE lever behind the controlling hand (grip_len) minus a fraction of the load
    AHEAD of the contact (head_len). A long-gripped pole (poleaxe/staff/half-sword) commands high leverage; a COMPACT
    weapon does NOT score spuriously high — the prior grip/(grip+head) RATIO rewarded short heads and let a dagger
    out-bind a spear (the verified HEMA inversion: dagger 0.140 > spear -0.066). Two hands add control. Nominal scale
    ~ -0.1..+0.6 around a sword. LEVER_HEAD_K/LEVER_REF/LEVER_2H are [SIM-CALIBRATE] (the lever-arm STRUCTURE is
    grounded; the magnitudes fit the bind win-rate in the re-baseline)."""
    w=c.w
    lever = w['grip_len'] - cfg['LEVER_HEAD_K']*w['head_len']   # absolute lever behind the hand minus the load ahead
    lev = cfg['LEVER_K']*(lever - cfg['LEVER_REF'])             # vs a reference one-hand sword's net lever
    if w['hands']==2: lev += cfg['LEVER_2H']                    # two hands = more control over the lever
    return lev

# ED-PC-0035: `impose_node` (the retired imposition-gate no-op stub) and its call-site guard are DELETED — the
# follow-up ED-PC-0023 explicitly owed. The ruling stands in the ledger; a no-op that still appears in the
# resolution path only invites someone to 'reconnect' it.


# weapons that have a half-sword form, and the form mapping (base <-> shortened)
# HALFSWORD_FORM / HALFSWORD_BASE are weapon DATA (single source in weapons.py, inverse derived); imported above.

def affords_halfsword(w):
    """EMERGENT half-sword affordance (P3/JD-3, ED-PC-0014): does the weapon offer a safe forward gripping zone
    (a `grippable` element — ricasso / attested gauntleted hand-on-blade) AND a blade that can present a controlled
    gap-thrust when gripped (`geo['halfsword']` = geometry.can_halfsword_thrust(curvature, point_concentration))?
    Both are physical/attested facts on the record, so the capability EMERGES rather than being name-whitelisted —
    this de-vestigialises `geo['halfsword']` (was computed by geometry.bake but read nowhere) and retires
    `HALFSWORD_FORM`/`HALFSWORD_BASE` AS BEHAVIOUR GATES (they remain only the base<->form NAME data below). On the
    un-extended roster the derived set was exactly {longsword, estoc}; marking a further attested ricasso
    grippable=True is the JD-3 roster-expansion decision.
    [ED-PC-0035 correction] That set is STALE: ED-PC-0016 marked greatsword and flamberge grippable too, so the
    derived set is now {longsword, greatsword, flamberge, estoc} — FOUR weapons. What still limits the auto-SWITCH to
    two is `HALFSWORD_FORM` (whose two entries the ED-PC-0016 auto-switch decision deliberately HELD), which means
    that name table is currently doing exactly the behaviour-gating this docstring says it no longer does. Tracked as
    a live inconsistency, not silently reworded: giving greatsword/odachi real half-sword forms is the Batch-6 roster
    item (they presently lose EVERY decided plate fight — an arming sword beats a greatsword at plate)."""
    return (any(e.get('grippable') for e in w.get('elements', ()))
            and bool(w.get('geo', {}).get('halfsword', False)))

def halfsword_target(c, closed, opp_armor):
    """PURE predicate: the weapon-form a half-sword-capable fighter SHOULD be in for the current range/armour
    (mit dem kurzen Schwert). Half-sword vs ARMOUR in the CLOSE (gap-thrust/leverage excel); full form at reach / vs
    unarmoured. Returns the target weapon string; the WRAPPER applies the mutation (mutation stays wrapper-owned).
    The CAPABILITY gate is now the emergent `affords_halfsword` (ED-PC-0014), not `base in HALFSWORD_FORM`; the
    HALFSWORD_FORM/HALFSWORD_BASE dicts survive only as the base<->form NAME mapping (the shifted-origin form
    records remain data). Weapons that do not afford the half-sword (or lack a form record) are unchanged."""
    base = HALFSWORD_BASE.get(c.weapon, c.weapon)
    form = HALFSWORD_FORM.get(base)
    want_half = closed and opp_armor in V.RIGID_TIERS and affords_halfsword(WEAPONS[base])
    return form if (want_half and form) else base

# ============================================================================
# RESOLUTION-CONTRIBUTION MODULES (functional: pure, role-objects-in, contribution-out).
# The wrapper owns ALL state mutation; these never index raw A/B and never mutate combatants.
# Each takes Combatant OBJECTS by role (aggressor/defender or longer/shorter) so roles cannot invert inside them.
# ============================================================================

def reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR):
    """Standing measure-domain sigma the DEFENDER's reach imposes on the aggressor (proportional to gap, weighted
    high unarmoured, falling with armour). +ve lowers the attacker's net. I6/D6: a small facing PROFILE term
    (`[FIAT — C1]`) — a defender presenting more profile (higher facing) is a slightly HARDER standing target (a narrower
    presentation, more voiding — matching weapon_physics.facing_pref's own "+ = 1H profile = narrower target" convention).
    [ED-PC-0035 correction: this line previously said "easier", which INVERTED the implemented direction — `profile` is
    ADDED to reach_pen and assemble_net_sigma SUBTRACTS reach_pen, so raising the defender's facing lowers the attacker's
    net. A future "fix" trusting the old prose would have silently flipped a live signed term.];
    exactly 0 at neutral facing (0.0, the pre-I6 default). Pure."""
    gap=er[defender]-er[aggressor]
    foot_meas=cfg['FOOT_MEASURE_K']*(balance_eff(defender,fat_d,cfg)*TR.eff_cw(defender, 'balance')
                                     - balance_eff(aggressor,fat_a,cfg)*TR.eff_cw(aggressor, 'balance'))
    meas_edge = lever_log_edge(TR.eff_cw(defender, 'measure'), TR.eff_cw(aggressor, 'measure'))   # M5/F5 ED-PC-0045: was `*= eff_cw(def)/eff_cw(agg)`, which AMPLIFIED a negative gap — a defender who invested in Misura while OUT-REACHED got a WORSE measure sigma (-1.374648 -> -1.5808452 at level 1). Now an ADDITIVE log-odds shift on the measure contest: monotone in each side's own factor whatever the sign of the gap. Kept INSIDE the REACH_W armour weighting, exactly like the differential it accompanies, so the measure channel's ability surface fades with armour as the channel itself does.
    reach_edge=(gap*cfg['REACH_FRAC']+foot_meas) + meas_edge
    profile = FACING_PROFILE_K*(getattr(defender,'facing',0.0) - getattr(aggressor,'facing',0.0))
    return cfg['REACH_W'][defender.armor]*reach_edge + profile

def legibility(aggressor, commit, cfg, opp_armor=V.TIER_NONE):
    """Read-legibility multiplier on the DEFENDER's visual read: a THRUST (in-line) is hard to read; a SWING/CUT
    (lateral arc) and a percussive BLUNT blow are easy; deeper commit/lunge = more readable. Legibility follows the
    MODE the wielder ACTUALLY fights in this exchange — the SELECTED damage-mode (sel_dmg, written by the wrapper from
    select_mode): puncture/thrust read HARD, shear/percuss read EASY. This is the one real use-mode wiring change (the
    fixed-head logic only ever inferred the mode from head+armour; now it reads the selected mode directly). Falls
    back to the prior head+armour inference when sel_dmg is unset, so it is byte-identical for every existing caller
    (a cut_thrust sword's sel_dmg is 'shear' unarmoured -> swing, 'puncture' vs plate -> thrust, matching coupling). Pure."""
    dm=getattr(aggressor,'sel_dmg',None)
    if dm is not None:
        legib = cfg['LEGIB_THRUST'] if dm==V.MODE_PUNCTURE else cfg['LEGIB_SWING']   # thrust hard; cut/percuss easy
    else:
        ah=aggressor.w['head']
        if ah==V.HEAD_POINT:                  legib=cfg['LEGIB_THRUST']      # always a thrust
        elif ah in (V.HEAD_STRAIGHT_CUT, V.HEAD_CURVED_CUT): legib=cfg['LEGIB_SWING']   # pure cutters always swing
        elif ah==V.HEAD_BLUNT:                legib=cfg['LEGIB_SWING']       # percussive arc, easy to read
        elif ah==V.HEAD_CUT_THRUST:
            # shifts to a controlled gap-thrust vs plate (hard to read), otherwise cuts (easy) — matches coupling's mode-shift
            legib=cfg['LEGIB_THRUST'] if opp_armor in V.RIGID_TIERS else cfg['LEGIB_SWING']
        else:                                 legib=1.0
    legib += cfg['LEGIB_COMMIT_K']*max(0,commit-3)
    legib += cfg['LEGIB_LUNGE']*getattr(aggressor,'lunge_depth',0.0)   # an extended/lunged body is more readable — CONTINUOUS in lunge_depth (no lunge string)
    legib -= cfg['LEGIB_DISTRACT_K']*WP.distraction(aggressor.w)   # morphology-rearch Phase B5: a feathered/tasselled weapon's ornament motion degrades the read — DERIVED, 0 for the (typical) unadorned weapon
    legib -= cfg['LEGIB_EDGELINE_K']*WP.edge_lines(aggressor.w)*ABIL.ability_factor(aggressor, 'edge_read')   # U3/ED-PC-0018 -> ACTIVATED U10/ED-PC-0022: a double/false edge's return-cut ambiguity degrades the read (same sign as distraction), AMPLIFIED by a tradition that weaponizes the false edge (Zwerchhau, 'edge_read'; factor 1.0 default). 0 for a plain-single/edgeless weapon.
    legib += cfg['CHOKE_ACCURACY_K']*choke_counterbalance(aggressor, cfg)*ABIL.ability_factor(aggressor, 'choke_control')   # U5/ED-PC-0019 -> ACTIVATED U10/ED-PC-0022: a head-heavy pole CHOKED UP to counterbalance telegraphs / loses fine precision AND loses point control (the RE-HOMED choke-thrust cost) -> reads EASIER (more legible). Mitigated by 'choke_control' (a pole tradition gathers without telegraphing; factor 1.0 default). 0 at grip=0 / for a compact weapon / a half-sword form.
    # SWING-ROOM LEGIBILITY (I5, D4/D5): a broad swing that cannot fully develop in cramped quarters is MORE
    # constrained and reads EASIER — weighted by the SELECTED element's own (1-pc_sel) (a thrust, pc_sel~1, is
    # unaffected) and by how little room is left (1-range_avail). Exactly 0 at range_avail=1.0 (the I1/I5
    # default) — the greatsword's "needs swing room" cramped-quarters cure routes through here + the commit-
    # window above, never a heft multiply (C4).
    range_avail=getattr(aggressor,'range_avail',1.0)
    pc_sel=getattr(aggressor,'sel_pc',None); pc_sel=pc_sel if pc_sel is not None else aggressor.w['geo']['point_concentration']
    legib += LEGIB_SWING_ROOM_K*(1.0-range_avail)*(1.0-pc_sel)
    return legib

def approach_displace(shorter, longer, cfg):
    """Lever-arm displacement-on-approach: a higher-leverage closer sets aside a THRUSTING longer weapon's point,
    suppressing its stop-hit and speeding the close. Returns a fraction in [0, APPROACH_DISPLACE_MAX]. Pure.
    I4/D5: reads the longer weapon's SELECTED head (sel_head, set every beat regardless of closed — the wrapper
    runs select_mode during the approach too), native fallback only when unset."""
    lever_edge = leverage(shorter,cfg) - leverage(longer,cfg)
    longer_head = getattr(longer,'sel_head',None) or longer.w['head']
    if longer_head!=V.HEAD_POINT or lever_edge<=0: return 0.0
    rd=(reading(shorter,cfg)-reading(longer,cfg))
    return min(cfg['APPROACH_DISPLACE_MAX'], cfg['APPROACH_DISPLACE_K']*lever_edge*(1+0.1*rd))

def reopen_prob(longer, shorter, base_gap, fat_longer, push_avail, cfg, TR):
    """Probability the LONGER weapon regains distance given a created moment exists: reads to seize vs shorter's
    denial, executes with balance, scaled by armour; freed-hand shove adds a path. Pure (returns a probability).
    RR-02: takes the longer fighter's actual fatigue (was hardcoded 0). RR-03: normalises by REACH_W['none']."""
    id_read = reading(longer,cfg)*TR.eff_cw(longer, 'visual')
    deny_read = reading(shorter,cfg)*TR.eff_cw(shorter, 'visual')
    read_edge = core.logistic((id_read-deny_read)/2.0)
    foot = balance_eff(longer,fat_longer,cfg)/3
    p=cfg['REOPEN_K']*base_gap*foot*read_edge*cfg['REACH_W'][shorter.armor]/cfg['REACH_W'][V.TIER_NONE]
    if push_avail: p += cfg['PUSH_REOPEN_BONUS']*foot
    return min(cfg['REOPEN_MAX'], p)

def disengage_attempt_p(longer, shorter, base_gap, fat_longer, cfg):
    """PROACTIVE fighting withdrawal (ED-PC-0030) — the rate at which a reach weapon closed into a bind it LOSES
    ATTEMPTS to refuse it: break measure with footwork and re-present its point at the measure where it dominates
    (HEMA: the spear/quarterstaff's whole game is the measure; Silver's staff keeps the swordsman at the weapon's
    length — you do NOT stand and bind when out-matched in it). Distinct from reopen_prob (which needs a created
    moment): a VOLUNTARY attempt any beat. This returns only the ATTEMPT INCLINATION; the READ CONTEST that decides
    a clean break vs a pursued (Nachreisen) withdrawal is resolved at the call site — so when this is 0 (e.g. faded
    at plate) NO attempt is made and there is NO pursuit. EMERGENT gate (no weapon names): only worth withdrawing
    when OUT-LEVERAGED in the bind — bind_deficit ramps to 1 when leverage(shorter) exceeds leverage(longer) (a
    light spear out-bound by a rigid estoc), ~0 when the longer weapon DOMINATES the bind (a poleaxe over a rondel
    stays and wins). Scales with footwork and the reach gap re-opened into. ARMOUR-FADE (same doctrine as
    true_time_edge): keeping distance only PAYS if the reach weapon can THREATEN the closer at range; vs a harness
    it cannot defeat, re-opening just cedes the close (the plated closer walks back in), so it fades to 0 as the
    closer's armour rises — at plate the reach weapon must ENGAGE the armour (gap-thrust/wrestle), not keep
    distance. Keyed on ADEF_W[closer]. Pure (the call site ANDs reach_threat too)."""
    bind_deficit = core.logistic((leverage(shorter, cfg) - leverage(longer, cfg)) / cfg['DISENGAGE_LEV_SCALE'])
    foot = balance_eff(longer, fat_longer, cfg)/3
    fade = max(0.0, 1.0 - cfg['ADEF_W'][shorter.armor]/cfg['ADEF_W'][V.TIER_HEAVY])
    p = cfg['DISENGAGE_BASE_P'] * bind_deficit * foot * fade * min(1.0, base_gap/cfg['DISENGAGE_GAP_REF'])
    return min(cfg['DISENGAGE_MAX'], p)

def disengage_clean_p(longer, shorter, cfg, TR):
    """Given a withdrawal is ATTEMPTED, the probability it is a CLEAN break (the withdrawer out-reads the closer's
    pursuit) rather than READ-and-pursued (Nachreisen). The read contest: the withdrawer's reading vs the closer's,
    each through their visual channel. Pure (returns a probability in (0,1))."""
    return core.logistic((reading(longer,cfg)*TR.eff_cw(longer,'visual') - reading(shorter,cfg)*TR.eff_cw(shorter,'visual'))/2.0)

def contact_moment_edge(a, b):
    """DISPLACEMENT RESISTANCE in the bind — the log-ratio of the two sides' grip-moments. SINGLE OWNER of the
    mass-in-the-bind question (ED-PC-0052, channel 5; Jordan-grounded 2026-07-29: "the lighter the weapon is, the
    easier it is to move away due to momentum... a heavier weapon would have an advantage in those weapon-to-weapon
    collision/reorienting scenarios").

    Until this function existed the bind had NO mass, momentum or inertia term anywhere: `bind_sigma` was
    lev + catch + tac + strq + spine + wound, and the only physical lever among those, `leverage()`, is pure
    GEOMETRY. Two swords of similar grip geometry and 2.14x different moment bound identically — and among the ten
    one-handed civilian swords the two measures very nearly INVERT (falchion, worst lever arm at -0.0576, carries the
    HIGHEST moment at 0.2415; tsurugi, better lever arm at +0.0110, the lowest at 0.1130). A heavy chopping falchion
    shoving a light tsurugi off the bind is the effect that was missing, and the lever-arm primitive ranked it
    backwards.

    READS at_grip(w, grip_position)['S_g'], the GRIP-ADJUSTED static moment — NOT `mass`, and NOT
    derive()['static_moment']:
      · not mass, because the naive variable points the WRONG WAY. The rapier is the heavier weapon (1.37 kg vs the
        scimitar's 0.95, the shamshir's 0.77) yet the cheaper to displace, because its mass sits in hilt and pommel.
        What resists being shoved aside is the moment about the hand, not the weight in it.
      · grip-adjusted, so choking up a polearm REDUCES its advantage (a spear's moment halves, 1.3873 -> 0.6937) —
        a real interaction with the closed-measure grip model, pinned by its own guard.

    LOG-RATIO, not a linear differential: scale-free (immune to the unit of moment), exactly antisymmetric (swapping
    the sides negates it, so it cannot produce the ED-PC-0045 sign pathology), an additive log-odds shift into
    bind_dominance_p = logistic(bind_sigma) as that ruling requires, and it compresses the polearm tail — a spear
    against a dagger is a 136x raw moment ratio that a linear form would turn into an unbounded sigma; the log reads
    ~4.9 before the [SIM-CALIBRATE] K.

    NO DOUBLE-COUNT with the speed cost: a heavier-at-the-contact weapon is also SLOWER to initiate a rebind or wind,
    and the engine already prices that through `agility` (MoI^-AGILITY_EXP) feeding tempo and defense_affinities. This
    term prices only the displacement-resistance half, which had no owner. Pure."""
    sa = WP.at_grip(a.w, getattr(a, 'grip_position', 0.0))['S_g']
    sb = WP.at_grip(b.w, getattr(b, 'grip_position', 0.0))['S_g']
    if sa <= 1e-12 or sb <= 1e-12:      # a synthetic/degenerate record — no moment edge either way
        return 0.0
    return log(sa/sb)


def bind_sigma(aggressor, defender, cfg, TR):
    """One bind iteration's net sigma: LEVERAGE (technique+skill + physical lever-arm) + BLADE-GUARD catch (the
    cross/quillons/rings that catch & control the opposing blade — a guardless pole binds poorly, a long cross
    excels) + TACTILE read (Fuhlen, degraded by the OPPONENT's edge vibration — morphology-rearch Phase B5: a
    wavy/flame-ground edge is felt as unfamiliar noise by whoever is bound against it, not its own wielder);
    Strength minor. +ve favours the aggressor winning the bind. Pure."""
    lev = ((aggressor.history+aggressor.skill('bind')) - (defender.history+defender.skill('bind')))*cfg['BIND_TECH_K'] \
          + (leverage(aggressor,cfg) - leverage(defender,cfg)) \
          + lever_log_edge(TR.eff_cw(aggressor, 'leverage'), TR.eff_cw(defender, 'leverage'))   # M5/F5 ED-PC-0045: was `* eff_cw(agg)/eff_cw(def)`, which AMPLIFIED a negative lever-arm differential — a dagger specialist in Stärke-Schwäche bound a poleaxe WORSE than an untrained twin (-1.05624 -> -1.19040). Now an ADDITIVE log-odds shift: since bind_dominance_p is logistic(bind_sigma), this multiplies the owner's ODDS of dominating the bind by exactly its ability factor, whatever the sign of the physical differential — and unlike the old ratio it is not inert when the two lever-arms are EQUAL (every mirror matchup), where a trained binder should still win.
    catch = cfg['BIND_GUARD_K']*(aggressor.w['blade_guard'] - defender.w['blade_guard'])   # quillons/rings catch the blade
    agg_read = reading(aggressor,cfg)*TR.eff_cw(aggressor, 'tactile')*TR.familiarity(aggressor.tradition,defender.tradition) \
               * (1 - cfg['BIND_VIBRATION_K']*WP.edge_vibration(defender.w))   # the DEFENDER's wavy edge disrupts the aggressor's read
    def_read = reading(defender,cfg)*TR.eff_cw(defender, 'tactile')*TR.familiarity(defender.tradition,aggressor.tradition) \
               * (1 - cfg['BIND_VIBRATION_K']*WP.edge_vibration(aggressor.w))   # the AGGRESSOR's wavy edge disrupts the defender's read
    tac = (agg_read - def_read)*cfg['BIND_TACTILE_K']
    strq = (aggressor.strength-defender.strength)*cfg['BIND_STR_K']
    spine = cfg['BIND_SPINE_K']*(WP.spine(aggressor.w)*TR.eff_cw(aggressor,'spine_press') - WP.spine(defender.w)*TR.eff_cw(defender,'spine_press'))   # U3/ED-PC-0018 -> ACTIVATED U10/ED-PC-0022: a single-edge rigid SPINE presses/binds the opposing blade (hand-high spine-press) — a separate physical fact from the lever-arm in `lev`, kept its own ablatable primitive (not multiplied into leverage — §2.3). Each side is AMPLIFIED by its own 'spine_press' ability (Japanese SHINOGI — the ability wired here; factor 1.0 default), so a bind specialist makes the spine decisive. [comment corrected 2026-07-23 ED-PC-0026: was "German Winden", a stale ref to the retired winden ability — winden is a DOUBLE-edged longsword technique, physically inert on this single-edge-only lever, which is why it was retagged to shinogi.] 0 for a double-edged/edgeless weapon.
    wound = cfg['WOUND_DEF_OB']*defender.wt.wounds - cfg['WOUND_ATK_OB']*aggressor.wt.wounds   # ED-1041: wounds impair the bind too (defence ~1.6x), bind-aggressor/defender roles fixed through the loop
    moment = cfg['BIND_MOMENT_K']*contact_moment_edge(aggressor, defender)   # channel 5 / ED-PC-0052: DISPLACEMENT RESISTANCE — the mass-moment half of the bind, absent until 2026-07-29 (see bind_moment_edge). A separate physical fact from `lev`'s lever ARM, so it is its own ablatable term and is NOT multiplied into leverage() (consolidation_v1 §2.3).
    return lev + catch + tac + strq + spine + wound + moment

# ---------- initiative substrate (three-phase Vor / Nach / Indes ~ sen; culture-neutral) ----------
# Pre-contact seizure CUT 2026-06-05 (Jordan; verified inert): seizure_score + initiative_seize removed. The
# pre-contact Vor contest gave a small initial edge (INIT_SEIZE_K 0.45*tanh) washed out by per-beat dynamics
# (INIT_GAIN_HIT 0.18/hit, decay, steals); ablation ~0 outcome impact. The ongoing initiative system
# (initiative_sigma + hit-gains/steals/decay) is retained and load-bearing.

def initiative_sigma(aggressor, defender, cfg):
    """The bounded sigma-edge the initiative state confers on whoever holds the Vor, on BOTH attack and defence.
    = INIT_SIGMA_K*tanh((aggressor.initiative - defender.initiative)/INIT_SCALE). Decoupled from the per-beat
    aggressor role: a DEFENDER holding the Vor produces a NEGATIVE term against the acting aggressor — realising
    'hold the Vor while defending'. Pure, tanh-bounded (cannot exceed INIT_SIGMA_K)."""
    return cfg['INIT_SIGMA_K']*tanh((aggressor.initiative - defender.initiative)/cfg['INIT_SCALE'])

# ---------- net-σ ASSEMBLY (moved out of the wrapper: the orchestrator sequences, the systems layer does the math) ----------
def defence_sigma(defender, mode_msig, mental_fat_d, fat_d, cfg):
    """The defender's δσ for the chosen mode: its mode_sigma (mental-fatigue-scaled) - handling + stance stability. Pure."""
    return mode_msig*(1-cfg['MENTAL_FAT_DEF_K']*mental_fat_d) - handling_penalty(defender,fat_d,cfg) + stance_stability(defender,fat_d,cfg)

def attack_sigma(aggressor, commit, init, oob, fat_a, consistency_a, cfg):
    """The aggressor's raw attack σ: commit-depth power + initiative emphasis - out-of-stamina penalty - handling + consistency. Pure."""
    return cfg['COMMIT_SIGMA']*(commit-3) + init - oob*0.5 - handling_penalty(aggressor,fat_a,cfg) + consistency_a

def assemble_net_sigma(atk_sig, dsig, reach_pen, adef, init_edge, aggressor, defender, cfg):
    """The net σ the core resolves against: attack - defence - reach + armour-defeat + Vor-edge + attacker-bias +
    bilateral wound-Ob. Pure; the wrapper SEQUENCES the contributions, this owns the arithmetic. Mirror stays 50."""
    # [ED-PC-0037] The flat `+ cfg['ATTACKER_BIAS']` (0.12 sigma on EVERY closed exchange) is GONE. It was untagged,
    # unledgered fiat that DUPLICATED the initiative/Vor system — two independently-calibrated mechanisms for the same
    # first-mover physics, the "every rule lives once" violation this repo forbids — and the 2026-06-28 critique
    # (W-08/W-10) had already recommended removal. Its own mirror-fairness defence ("the aggressor role alternates")
    # held only at fight aggregate: inside a burst (BURST_MAX=4) one fighter could hold the role for four consecutive
    # exchanges and bank the full bias each time. Removal was DEFERRED from batch 3 to here deliberately, because it
    # compounded with the deterministic first-actor monopoly — deleting it then would have been tuning against a moving
    # target. With that monopoly fixed (arbitrary cadence phase + tempo_pressure) removal measures small and clean:
    # mirrors hold at 0.50 and matchups move <=0.01, apart from katana/mace which were the biggest beneficiaries of
    # banking the bias behind a tempo edge. First-mover advantage now lives ONLY in the Vor, where it is earned.
    return (atk_sig - dsig - reach_pen + adef + init_edge
            + cfg['WOUND_DEF_OB']*defender.wt.wounds - cfg['WOUND_ATK_OB']*aggressor.wt.wounds)

def commit_depth(aggressor, defender, cfg, rng, TR):
    """Draw the CONTINUOUS commitment depth in [2,5] (commitment-recovery is a spectrum, not four rungs). Disposition
    lean + WARINESS (vs an unread tradition the aggressor commits shallower) skew a Beta over the range; the 0.25
    param floor is the spread-floor (never collapses to a spike). Consumes one rng.betavariate draw (kept here so the
    wrapper sequences but owns no formula). Returns (commit, beta_a, beta_b, lean).
    SWING-ROOM (I5, D4): the Beta's UPPER SUPPORT is contracted by range_avail's _commit_range_factor (a swing you
    cannot fully develop commits shallower) — reshapes the Beta PARAMS/window only, never adds or reorders the
    single draw (seeded determinism). At range_avail>=RANGE_COMMIT_PEAK (the I1/I5 default, 1.0) this is
    byte-identical to the pre-I5 [2,5] window."""
    ln=disp_lean(aggressor)
    wary=cfg['WARINESS_K']*(1-TR.familiarity(aggressor.tradition, defender.tradition))   # >=0, biases shallow
    g=cfg['COMMIT_BETA_K']*(cfg['DISP_COMMIT_K']*ln - wary)
    ba=max(0.25, cfg['COMMIT_BETA_BASE']*(1+g)); bb=max(0.25, cfg['COMMIT_BETA_BASE']*(1-g))
    span=3.0*_commit_range_factor(getattr(aggressor,'range_avail',1.0))
    commit=2.0+span*float(rng.betavariate(ba,bb))   # stdlib Beta draw (ED-1085 numpy de-leak; same distribution)
    return commit, ba, bb, ln

def read_contest(aggressor, defender, commit, consistency_a, mental_fat_d, fat_d, cfg, rng, TR):
    """The defender's READ of the attack + the resulting mode selection. read_d (visual+precommit, familiarity-
    and legibility-scaled) vs read_a -> read_win (logistic). If the read wins, the defender picks the BEST mode;
    else it guesses. Consumes rng.random (the read) then rng.randrange ONLY on a missed read — the same order as the
    inline version, so byte-identical. Pure resolution+selection logic moved out of the orchestrator. Returns a dict."""
    fam=TR.familiarity(defender.tradition, aggressor.tradition)
    legib=legibility(aggressor, commit, cfg, defender.armor)
    read_d=reading(defender,cfg)*TR.eff_cw(defender,'visual')*TR.eff_cw(defender,'precommit')*fam*legib*(1-cfg['MENTAL_FAT_READ_K']*mental_fat_d)
    read_a=reading(aggressor,cfg)*TR.eff_cw(aggressor,'visual')+consistency_a
    p_read=core.logistic((read_d-read_a)/1.0)
    read_win=rng.random() < p_read
    modes=list(V.DEFENCE_MODES)   # ORDERED: modes[rng.randrange(3)] below makes the sequence part of the RNG contract
    msig={m:mode_sigma(m,aggressor,defender,commit,read_win,fat_d,cfg) for m in modes}
    mode=max(msig,key=msig.get) if read_win else modes[rng.randrange(3)]   # stdlib uniform int (ED-1085)
    return dict(read_win=read_win, read_d=read_d, read_a=read_a, p_read=p_read, mode=mode, msig=msig)

def indes_steal_amount(defender, wind, commit, read_d, read_a, cfg, TR):
    """The Indes / sen-no-sen initiative-steal AMOUNT: a defender who out-read a deep commit steals the Vor, scaled
    by commit-depth x read-margin (bounded). Pure — the wrapper applies the clamp/mutation."""
    indes_scale=max(cfg['INDES_SCALE_FLOOR'], min(cfg['INDES_SCALE_CEIL'],
                    (1+cfg['INDES_COMMIT_K']*(commit-4))*(1+cfg['INDES_READ_K']*(read_d-read_a))))
    return cfg['INIT_STEAL_INDES']*init_steal_factor(defender, wind, cfg, TR)*indes_scale

def counter_select(defender, cfg, rng, TR):
    """Whether the defender reaches for the single-time counter (tempo-driven SELECTION; SUCCESS is gated later, a
    miss punished). Consumes one rng.random."""
    return rng.random() < cfg['COUNTER_SELECT_BASE']*TR.eff_cw(defender,'tempo')*max(0.0, 1-cfg['DISP_COUNTER_K']*disp_lean(defender))*TR.ability_factor(defender,'counter_select')

def overcommit_exposure(aggressor, commit, fat_a, cfg, TR):
    """The aggressor's exposure to the riposte from over-committing: commit-depth x irrecoverability, minus the
    anti-overcommit (balance) curb and trained discipline. Pure; floored at 0 (ED-PC-0034 fix: the floor now wraps the
    WHOLE expression, not just the commit term — previously a balanced/disciplined fighter at shallow commit returned a
    NEGATIVE exposure, e.g. -0.37 for an agile true_times fighter at commit 2. The wrapper guards its initiative/poise
    loss with `if >0`, but fed the un-floored value straight into RIPOSTE_ON_FAIL/ON_NEUTRALIZE, so negative exposure
    silently pushed the defender's riposte chance BELOW its configured base — a mechanic the docstring said could not
    exist. Not over-committing means you are not EXTRA exposed; it does not make you harder to riposte than the base
    contemplates, and anti-overcommit is a MITIGATION of exposure, not a bonus that can invert it). The wrapper applies
    the loss."""
    return max(0.0, cfg['COMMIT_EXPOSE_K']*(commit-3)*recoverability_factor(aggressor,cfg)
                    - anti_overcommit(aggressor,fat_a,cfg) - TR.ability_bonus(aggressor,'anti_overcommit'))

def clamp_initiative(x, cfg):
    """Hard bound on |initiative| (the CAP safeguard; paired with the wrapper's per-beat DECAY = the damper)."""
    return max(-cfg['INIT_CAP'], min(cfg['INIT_CAP'], x))

# ---------- initiative DIFFERENTIATION layer (per-tradition signature = channel weight x substrate mechanism) ----------
# A pure layer on top of the substrate: each tradition's signature initiative ability is just its existing channel
# weight multiplying the relevant substrate magnitude. No tradition-name branches; neutral tradition = 1.0 everywhere
# (so default fighters are unaffected and every invariant holds by construction).
def init_steal_factor(stealer, bind_active, cfg, TR):
    """WHO steals the Vor best. In a BIND (winding), the steal scales with tactile+leverage — German Fühlen /
    Stärke-Schwäche, boosted by the stealer's OWN edge vibration (morphology-rearch Phase B5: a wavy/flame-ground
    edge disrupts whoever is bound against it, giving the wielder an easier read to exploit — 0 for the typical
    plain-edged weapon, identity). In the OPEN, with tempo — Italian contratempo (the single-time counter).
    Neutral = 1.0."""
    if bind_active:
        return (TR.eff_cw(stealer, 'tactile') + TR.eff_cw(stealer, 'leverage'))/2 \
               * (1 + cfg['BIND_VIBRATION_K']*WP.edge_vibration(stealer.w))
    return TR.eff_cw(stealer, 'tempo')

def init_hold_decay(holder, cfg, TR):
    """Geometric HOLD (Spanish destreza): high measure slows the per-beat decay, so the Vor is held longer. Returns
    this fighter's effective decay multiplier (neutral measure = base INIT_DECAY)."""
    m = TR.eff_cw(holder, 'measure')
    return 1 - (1 - cfg['INIT_DECAY'])/m

def init_overcommit_loss(aggressor, exposure, cfg, TR):
    """True-times discipline (English; also Italian/Japanese tempo): tempo-disciplined fighters lose less grip on the
    Vor from their own commitment. Returns the initiative loss magnitude (neutral tempo = base)."""
    return cfg['INIT_LOSS_OVERCOMMIT'] * exposure / TR.eff_cw(aggressor, 'tempo')

# ---------- kuzushi / structure (dynamic balance) ----------
def poise_factor(c, cfg):
    """Maps current structure [POISE_FLOOR,1] to a [POISE_EFFECT_FLOOR,1] multiplier on tempo and defence: a
    broken-balance (kuzushi'd) fighter acts and defends worse. At full structure (1.0) returns 1.0 (no effect), so
    full-structure fighters are unaffected. Pure."""
    s=max(cfg['POISE_FLOOR'], min(1.0, c.poise))
    return cfg['POISE_EFFECT_FLOOR'] + (1-cfg['POISE_EFFECT_FLOOR'])*(s-cfg['POISE_FLOOR'])/(1-cfg['POISE_FLOOR'])

def clamp_poise(x, cfg):
    """Bound structure to [POISE_FLOOR, 1.0]."""
    return max(cfg['POISE_FLOOR'], min(1.0, x))

def percussion_stagger(striker, victim, wound, deg, cfg):
    """The concussive LOAD a landed blow delivers to the VICTIM, DISTINCT from the wound (ED-PC-0031, Jordan) —
    drained as STAMINA (wind knocked out / attrition) and broken as POISE (a strong stagger). ARMOUR-GATED by
    physics: a BLUNT/percussion head transmits its impulse THROUGH the harness (a mace/warhammer/staff-butt concusses
    even when the plate holds — the anti-plate blunt path; Medieval Chronicles, tempered by Devereaux's 'plate+
    padding soaks much'), scaled by the head's percussion_authority × a per-tier absorption (PERC_BLUNT_TRANSMIT); a
    POINT/edge transmits impulse only where it BITES — its load IS the wound (a deflected point pings off plate → ~0,
    so a gap-specialist can still close a non-piercing reach weapon at plate). This is why a STAFF (m_head≈0, wound
    ≈0) is still effective — its concussive impulse winds and staggers without drawing blood. Returns (stamina_drain,
    poise_break), both ≥ 0. Pure (the wrapper applies them to the victim's stamina/poise).
    ⚠ [ED-PC-0047 / E2a, 2026-07-29] The staff sentence above was FALSE FOR A YEAR of engine time and this docstring
    was the only place that said otherwise: `weapon_physics.percussion_authority` used the whole-weapon centre-of-
    balance offset as its lever, so a centre-gripped haft derived EXACTLY 0.0 authority and this function returned
    (0.0, 0.0) for the staff — the worked example of ED-PC-0031's headline mechanic delivered no wind and no stagger
    at all. Fixed at the lever (`weapon_physics.strike_point_lever`); the staff now derives 5.6290 and staggers at
    ~70% of a mace's. The claim above is now measured, not asserted:
    tests/valoria/test_combat_strike_point_lever.py::test_staff_stagger_is_a_real_fraction_of_the_maces pins it
    THROUGH this function with a constructed wound, so it cannot silently revert to a docstring again."""
    if deg not in ('graze', 'success', 'overwhelming'):
        return 0.0, 0.0
    head = getattr(striker, 'sel_head', None) or striker.head
    if head == V.HEAD_BLUNT:
        qf = cfg['PERC_QUAL'][deg]
        grip = getattr(striker, 'grip_position', 0.0)
        # SELECTED-ELEMENT percussion (ED-PC-0036 fix): read the striker's sel_perc — the percussion authority of the
        # element select_mode actually chose — with the whole-weapon value only as the native fallback, exactly as
        # core.strike does. This closes a bypass of the sel_* SINGLE-SOURCE contract that core.strike's docstring
        # declares canonical ("a composite routed to a blunt sub-element is damaged on THAT element's percussion"):
        # percussion_stagger was landing on the WHOLE-WEAPON value, so a lucerne_hammer's rear fluke and its hammer
        # face delivered identical stagger. That is the object-confusion bug class (M-02) the architecture exists to
        # prevent, re-opened by ED-PC-0031 — which post-dates the doctrine it broke.
        perc = getattr(striker, 'sel_perc', None)
        perc = perc if perc is not None else WP.percussion_authority(striker.w, grip=grip)
        load = ((cfg['PERC_STR_BASE'] + cfg['PERC_STR_K']*striker.strength) * cfg['PERC_BLUNT_HEFT']
                * perc * cfg['PERC_BLUNT_TRANSMIT'][victim.armor] * qf)
    else:
        # a THRUST/CUT delivers its energy as the WOUND (penetration), only a FRACTION as concussion/wind — a stab
        # winds far less than a mace-blow of the same lethality (the energy went into the hole, not the body's inertia).
        # PERC_POINT_FRAC keeps the concussion path a BLUNT specialty. And a point/cut winds via FLESH contact: vs a
        # harness it CANNOT defeat it glances/deflects and delivers ~0 concussion (unlike a blunt head, which drives
        # its impulse THROUGH the plate), so the point-wind FADES with the victim's armour (same ADEF doctrine) — this
        # keeps a plate STALEMATE a stalemate (two swords that can't defeat each other's plate don't wind each other
        # to a decision) and stops a weak plate-poke from over-draining a gap-specialist's wind at range.
        fade = max(0.0, 1.0 - cfg['ADEF_W'][victim.armor]/cfg['ADEF_W'][V.TIER_HEAVY])
        load = cfg['PERC_POINT_FRAC'] * float(max(0, wound)) * fade
    return cfg['PERC_STAM_K']*load, cfg['PERC_POISE_K']*load

# ============================================================================
# WRAPPER DE-LEAK (Phase-3 tail — completes the Phase-2 invariant "the wrapper computes NO sigma of its own").
# The Phase-2 pass moved the CLOSED-exchange net-sigma + commit + read into pure systems.*; these are the
# remaining inline sigma/formula ASSEMBLIES the pass missed (the APPROACH path especially). Each is a pure
# function lifted VERBATIM from the wrapper so the extraction is byte-identical. SCOPE DISCIPLINE: only genuine
# sigma/formula assemblies are lifted; LEGITIMATE L3 orchestration is left in the wrapper — composing a gate
# roll from a config scalar + already-derived systems outputs (stophit_p, the neutralize mode-pick, the
# RIPOSTE_ON_* gate, the bind-entry steal multiply) is the orchestrator sequencing pre-derived values, not
# assembling a formula of its own (per the Gate-1 audit's adversarial ruling on those sites).
# ============================================================================
# ── TRUE TIME (George Silver) — the hand is swifter than the foot ────────────────────────────────────────────────
# "The time of the hand being swifter than the time of the foot, overtakes him with blow or thrust in the arm, hand,
# head, face and body" (Silver, Paradoxes of Defence). The longer weapon completes a THRUST (a hand action) in the
# tempo the closer needs to move body-mass (a foot action) into its own measure; the further the point reaches BEYOND
# the closer's reach, the more of that hand-before-foot window it owns. So the true-time edge is the STANDING REACH
# ADVANTAGE (reach_longer − reach_shorter) — Silver's "time of the hand vs time of the foot" IS a measure/distance
# statement. An earlier head-inertia form (point re-presentation ∝ 1/m_head^0.25) was RETIRED after an adversarial
# audit: the cited sporting-implement law (Cross & Nathan 2009) is about MoI, and by the honest inertia — MoI for a
# swing, total mass for the axial slide — the polearm is NOT faster (a long lever's MoI is large; the spear is not
# lighter than an estoc); m_head was the one proxy that happened to give the doctrinal answer, and it spuriously
# credited a short closer's light point with "answering" a thrust it was still stepping into reach of. Reach is the
# honest quantity, and it makes the spear-vs-estoc edge small (they are nearly the same length) — the real reason
# that residual exists. This is why a perfect-length polearm out-fights a heavy two-hand sword AT REACH (Jordan
# 2026-07-24) yet only modestly out-fights a near-length one.
TRUE_TIME_REF = 1.5    # [DESIGN] reach-gap (reach-points) at which the true-time edge is ~tanh(1)=0.76 of its max —
                       #   sets where the hand-before-foot benefit saturates (a ~1.5 gap already buys most of it)
def true_time_edge(longer, shorter, cfg):
    """Silver's TRUE TIME as a net-sigma edge on the approach stop-hit: the longer weapon strikes in the tempo of a
    hand-action while the closer must move body-mass into measure, so its stop-hit dominates in proportion to its
    STANDING REACH ADVANTAGE = K·(reach_base(longer) − reach_base(shorter)), clamped ≥0 (the longer weapon by
    definition has the reach; a short closer's own quickness does not answer a thrust it is still closing into range
    of — the mechanism's own doctrine, and the fix to an audit finding that the prior head-inertia form over-buffed
    daggers-as-closers). ARMOUR-FADE: Silver's doctrine is UNARMOURED (backsword/rapier-era, out of harness) — vs a
    harness the game is armour-DEFEAT (gap/percussion), not reach-tempo, so the edge fades to 0 as the closer's
    armour rises (keyed on ADEF_W[closer]); the plate regime stays an armour-defeat contest owned by reach_threat +
    arrest_impulse. Composes with them (a distinct, structural-reach channel from stophit_sigma's dynamic
    REACH_DISADV_K·measure_gap gap term). SATURATING: the hand-before-foot benefit has a CEILING — a 3 m reach edge
    does not confer three times the tempo of a 1 m edge (past a step or two the closer is out of time either way),
    so the gap passes through tanh(·/TRUE_TIME_REF) and TRUE_TIME_K is the MAX sigma. A LINEAR form let a huge gap
    (spear 7.8 vs dagger 4.4 → 3.4) run to a degenerate ~60σ that shut the closer out entirely (the dagger never
    reached Contact); the tanh keeps the common 0.5–2 m gaps well-differentiated while bounding the tail. Pure."""
    fade = max(0.0, 1.0 - cfg['ADEF_W'][shorter.armor]/cfg['ADEF_W'][V.TIER_HEAVY])
    gap = max(0.0, reach_base(longer, cfg) - reach_base(shorter, cfg))
    return cfg['TRUE_TIME_K'] * fade * tanh(gap / TRUE_TIME_REF)

def stophit_sigma(longer, shorter, measure_gap, cfg):
    """The APPROACH-path stop-hit net-sigma (the longer weapon threatening across the closing gap). The analog of
    assemble_net_sigma for the approach: reach-disadvantage by gap + base + bilateral wound-Ob + Silver's true-time
    point-tempo edge (true_time_edge — the light-point reach weapon's hand-speed advantage). I5/D4: gains a
    commitment-depth term — a stop-hit thrown with full room to extend threatens more than one snapped off into a
    rapidly-closing, cramped gap, the SAME range_avail the closed exchange's commit-window reads (I5's gate #4).
    Exactly 0 at range_avail=1.0 (the I1/I5 default). Pure."""
    range_avail=getattr(longer,'range_avail',1.0)
    return (cfg['REACH_DISADV_K']*measure_gap + cfg['STOPHIT_NSIG_BASE']
            + cfg['WOUND_DEF_OB']*shorter.wt.wounds - cfg['WOUND_ATK_OB']*longer.wt.wounds
            + STOPHIT_RANGE_K*(range_avail-1.0)
            + true_time_edge(longer, shorter, cfg))

def tempo_pressure(c, opp, cfg, TR):
    """ANTICIPATION — how much sooner a fighter brings their next action to bear than raw weapon cadence implies.
    Multiplies the per-beat readiness accumulation (the wrapper applies it). Pure.

    [ED-PC-0037, F16] Who acts first was previously decided by weapon cadence ALONE, accumulated metronomically, so
    the marginally faster weapon crossed ACT_THRESHOLD first every single time: a jian's +1.5% close-tempo edge over an
    arming sword bought it a 2:1 action economy (679 vs 342 closed rolls / 150 fights), and cloning an arming sword to
    step its mass 1.18 -> 1.20 kg flipped the win-rate 57% <-> 42% on a cadence delta of 0.0002. That is a weapon
    STATISTIC deciding the fight's most important question.

    It is the wrong question to answer with cadence, and equally wrong to answer with noise. In the fight this engine
    models, who moves first is decided by the VOR and the READ — you begin as your opponent begins because you
    anticipated them, and you keep the initiative because you took it. Both quantities are already first-class here:
      • `initiative` — the Vor. It is not static: it decays per beat (init_hold_decay, tradition-held), drifts with
        disposition, and is STOLEN on hits and in the bind (init_steal_factor). A fighter who has been dictating the
        exchange gets to keep dictating it — earned, not owned.
      • `reading` — cog/attention/experience. Anticipating the opponent's commitment is precisely what lets you act
        into it rather than after it. (The feint is not a separate action here — WS-5 dissolved it into the attack's
        commit-depth and legibility — so its influence arrives through the read, which is where it belongs.)
    Floored at 0 so a badly out-read fighter stalls rather than accumulating backwards. Both K's [SIM-CALIBRATE].
    [HONESTY CORRECTION, ED-PC-0037.1] Measure this before believing it. An adversarial ablation (both K's -> 0,
    20 weapons x 4 tiers, n=400/cell) found the aggregate outcome effect to be -0.06pp +- 0.27 (z=-0.23), with no
    cell exceeding |z|=2.5 — i.e. currently OUTCOME-INVISIBLE. Worse, the READ term is identically ZERO in any
    same-stats fight, because reading() and eff_cw depend only on stats and tradition — and same-stats is exactly
    the weapon-balance surface the ED-PC-0037 entry cited as its result. So this function does NOT carry the
    first-actor fix: the operative mechanism is the uniform cadence-phase draw at engagement start, which breaks
    the lockstep by itself. This is a correctly-signed, correctly-grounded hook (a Vor-holder does act sooner:
    tp 1.6 vs 0.4 at the clamp) that will matter once builds diverge in stats/Vor, and it belongs here rather
    than as noise — but describing it as the answer to 'what happened to anticipating' oversold it, and the
    honest statement is that the anticipation channel exists and is currently near-silent at default builds."""
    return max(0.0, 1.0 + cfg['INIT_TEMPO_K']*(c.initiative - opp.initiative)
                        + cfg['READ_TEMPO_K']*(reading(c, cfg)*TR.eff_cw(c, 'tempo')
                                               - reading(opp, cfg)*TR.eff_cw(opp, 'tempo')))

def pursuit_sigma(pursuer, withdrawer, fat_p, fat_w, cfg, TR):
    """The NACHREISEN pursuit net-sigma — the closer striking a reach weapon that is turning out of the bind to break
    measure (ED-PC-0030's read-lost branch). Modelled on stophit_sigma, the engine's other opportunistic-strike sigma.
    [ED-PC-0036] This REPLACES a flat cfg['DISENGAGE_PURSUIT_NSIG'] passed straight to core.resolve: that shortcut let
    the single most violent branch in the closed phase bypass the ENTIRE sigma-assembly — no armour, no wounds, no
    attribute of the withdrawer at all, so every fighter pair in this branch resolved identically and the pursuer
    contributed only History (the pool). The mechanism ED-PC-0030 grounded is the attempt/clean/pursued STRUCTURE; the
    flat resolution was grounded nowhere. Terms, each already canonical elsewhere:
      • the base anchor — catching a withdrawing opponent is HARD (negative), the one part the old constant had right;
      • bilateral wound-Ob, on the same sign convention as every other sigma (a wounded target is easier, a wounded
        striker is worse) — its absence here was a silent inconsistency;
      • armour-defeat (armor_defeat_sigma) — you cannot punish a withdrawal you cannot pierce. A spear pursuing a
        plated man reads deeply negative; a poleaxe barely suffers. Exactly 0 unarmoured, so open-measure duels keep
        the old character;
      • a FOOTWORK differential — Nachreisen is literally "travelling after": catching the break is a feet contest, so
        the pursuer's balance/footwork against the withdrawer's is what decides whether the strike lands in the gap.
    Pure; the wrapper rolls it."""
    return (cfg['DISENGAGE_PURSUIT_NSIG']
            + cfg['WOUND_DEF_OB']*withdrawer.wt.wounds - cfg['WOUND_ATK_OB']*pursuer.wt.wounds
            + armor_defeat_sigma(pursuer, withdrawer, cfg)
            + cfg['PURSUIT_FOOT_K']*(balance_eff(pursuer, fat_p, cfg)*TR.eff_cw(pursuer, 'balance')
                                     - balance_eff(withdrawer, fat_w, cfg)*TR.eff_cw(withdrawer, 'balance')))

def close_rate(shorter, ffat_shorter, displ, rt, cfg):
    """Measure-domain closing RATE for the shorter weapon walking in: athletic close-speed (balance x cadence),
    sped by displacing a thrusting point (displ) and by walking through an un-threatening reach (2.0-rt). I6/D6:
    a small lateral-void contribution (Fiore fol. 39r) — angling off-line aids the close; exactly 0 at neutral
    facing (0.0, the pre-I6 default). Pure."""
    cr = cfg['CLOSE_RATE_K']*balance_eff(shorter,ffat_shorter,cfg)/3 * weapon_tempo(shorter,cfg,ffat_shorter)/2
    cr *= (1.0 + FACING_VOID_GAIN*getattr(shorter,'facing',0.0))
    return cr*(1+displ)*(2.0-rt)

ARREST_POB_REF = 0.6   # [DESIGN] PoB_frac at/above which a weapon is too FRONT-HEAVY to brace as a pole-jab (the
                       #   rear/centre-balanced staff/spear braces a charge; a front-heavy glaive/guandao cannot be
                       #   set butt-planted). rear_balance ramps 1.0 (PoB_frac 0, staff) -> 0 (PoB_frac >= REF).
                       #   0.5->0.6 (audit #4): a boar/bear-spear (PoB~0.53, the docstring's own braced-charge exemplar)
                       #   keeps a residual jab path rather than reading as a worse arrester than a sword.
def arrest_impulse(longer, cfg):
    """The IMPULSE a braced stop-thrust transmits to a CHARGING body during the approach, opposing the close (HEMA:
    the longer weapon 'sets' against the step-in / Nachreisen). Physically an ARREST — momentum checked, NOT a wound:
    a braced point halts (or drives back) a charge whether or not it penetrates (boar-spear lugs exist precisely
    because penetration != arrest; a fable audit corrected the earlier recoil = K*damage model, which wrongly crowned
    big CUTTERS — a swing does not stop a closing body — and stranded the staff). So this reads ONLY the weapon's
    reach + braceable structure, never damage:
      • reach beyond a body-length FLOOR — a long weapon meets the charge with leverage; a DAGGER (reach < floor) can
        arrest nothing (there is no charge to arrest at grappling distance) -> 0 by construction.
      • brace = the better of a THRUST point (buckling-discounted by cross_section — a whippy rapier blade buckles
        under the axial load and transmits little) OR a rigid straight REAR/centre-balanced POLE-jab (the staff path:
        no point needed — a braced quarterstaff stops you cold; killed for front-heavy or curved swingers).
    Armour is NOT read here (a plated man run onto a braced spear is still halted) — armour enters the approach ONLY
    via reach_threat (rt) in the stop-hit's landing probability, so it is counted ONCE, not thrice. ARREST_K /
    ARREST_REACH_FLOOR are [SIM-CALIBRATE]; the structure (reach x braceability, cutter/dagger-excluded) is grounded.
    Pure."""
    w = longer.w
    geo = w['geo']
    pob = WP.derive(w)['PoB_frac']
    cs, cv, th = geo['cross_section'], geo['curvature'], geo['thrust']
    rear_balance = max(0.0, min(1.0, 1.0 - pob/ARREST_POB_REF))   # CLAMPED to [0,1] (audit #4): a shifted-origin half-
                                                                 #   sword form has PoB_frac<0 (mass behind the working
                                                                 #   hand) which must not read as >1 super-braceable
    brace = max(th*cs,                       # thrust point, buckling(cross_section)-discounted (whippy rapier loses)
                cs*(1.0-cv)*rear_balance)    # rigid straight rear/centre-balanced pole-jab (staff; no point required)
    return cfg['ARREST_K'] * max(0.0, reach_base(longer, cfg) - cfg['ARREST_REACH_FLOOR']) * brace

def approach_step(measure_gap, base_gap, close_rate, recoil):
    """Net measure-domain movement for one approach beat: the closer's ADVANCE (close_rate) minus the stop-thrust's
    ARREST (recoil), clamped to [0, base_gap]. A penetrating/braced stop that arrests more than the closer advances
    nets them BACKWARD (driven out); one that does not, nets them still forward (they walk in). Single owner of the
    approach arithmetic (the wrapper is an orchestrator — no formula there, per the file's own convention). Pure."""
    return min(base_gap, max(0.0, measure_gap - close_rate + recoil))

def init_emphasis_sigma(aggressor, defender, cfg, TR):
    """Initiative/tempo EMPHASIS sigma fed into attack_sigma: tempo(Agi) + reading(Cog/Att) + experience(History),
    re-weighted by the aggressor's tempo channel. Pure (the formula the wrapper used to assemble inline)."""
    return (cfg['INIT_K']*(aggressor.agi-defender.agi)
            + cfg['INIT_READING_K']*(reading(aggressor,cfg)-reading(defender,cfg))
            + cfg['INIT_HISTORY_K']*(aggressor.history-defender.history))*TR.eff_cw(aggressor,'tempo')

def consistency(c, cfg):
    """Baseline-consistency sigma term from the Concentration tracker (3F+2S, depletes), centred at 3. Pure."""
    return cfg['FOCUS_CONSISTENCY_K']*(c.conc/5.0 - 3)

def mental_fatigue(c, fat, cfg):
    """Mental-fatigue scalar: endurance fatigue degraded by Concentration reserve (focus protects the read/technique
    under fatigue). cfrac is the fighter's current Concentration fraction. Pure."""
    cfrac = c.conc/max(1, c.conc_max)
    return fat*(1-cfg['FOCUS_MENTAL_K']*max(0, min(1, cfrac)))

def poise_regen(c, cfg):
    """Per-beat structure (kuzushi) regathering toward 1.0, Focus-accelerated. Returns the new poise PRE-clamp (the
    wrapper applies clamp_poise + the mutation). Pure."""
    return c.poise + cfg['POISE_RECOVER']*(1+cfg['POISE_FOCUS_K']*(c.focus-3))*(1-c.poise)

def counter_success_prob(defender, cfg, TR):
    """Single-time-counter SUCCESS probability (bounded): base + training(History) + reflex + the counter ability.
    The untrained counter mostly fails; abilities modulate it upward. Pure — the wrapper rolls rng against it."""
    succ = (cfg['COUNTER_SUCCESS_BASE'] + cfg['COUNTER_TRAIN_K']*(defender.history-3)
            + cfg['COUNTER_REFLEX_K']*(reflex(defender,cfg)-3) + TR.ability_bonus(defender,'counter_success'))
    return max(0.05, min(0.92, succ))

def bind_dominance_p(bsig):
    """Logistic of the bind net-sigma: P(aggressor dominates this bind iteration). Pure."""
    return core.logistic(bsig)

def disrupt_resist_p(c, cfg):
    """Concentration disruption-resistance: P(the fighter completes a simultaneous strike despite being hit),
    logistic in Focus. Pure."""
    return core.logistic(cfg['DISRUPT_K']*(c.focus-3))
