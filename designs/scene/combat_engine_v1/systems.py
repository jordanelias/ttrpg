"""Subsystem modules. Uniform contract: each is a pure function of (aggressor, defender, state, cfg[, rng]).
NO subsystem touches raw A/B — they receive Combatant objects in role. This isolates every mechanic for
unit-testing and makes the coupling explicit (the fix for the recurring inversion bugs)."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from math import exp, tanh, sqrt
from config import HANDLE_RANK
import core
import weapon_physics as WP   # Phase-3b: derived L0 physics (percussion_authority/puncture_pressure/agility/reach) — cycle-free (WP imports only math at module scope)
from combatant import WEAPONS, GEOMETRY, HALFSWORD_FORM, HALFSWORD_BASE

# ---------- reach (continuous, derived) ----------
def reach_base(c, cfg):
    """Standing reach = body/arm offset (L0) + the weapon's forward extent DERIVED from geometry (Phase-3b: retires
    the categorical reach=='long' + HEAD_REACH[head] + the per-weapon reach_adj triple-duty). Forward extent =
    head_len (the blade/shaft forward of the lead hand) + a 2H rear-hand setback (REACH_2H_K*grip_len). So a
    CENTRE-gripped pole (staff, head_len≈grip_len) reaches LESS than a BUTT-gripped one (spear, head_len≫grip_len),
    and a long blade (greatsword) more than a short one — the grip-position insight, emergent. reach_adj is now a
    SMALL per-weapon residual, not the dominant term."""
    w=c.w
    geom = w['head_len'] + cfg['REACH_2H_K']*w['grip_len']*(w['hands']==2)
    return cfg['L0'] + cfg['REACH_GEOM_SCALE']*geom + w.get('reach_adj',0.0)

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
    reach (handled at the call site via grip state)."""
    w=c.w
    _heft=wield_heft(c,cfg)   # DERIVED g-aware MoI heft (Phase-3 Stage 2b): replaces the binary wt class on the COST path
    pen=cfg['WEIGHT_PEN']*_heft+cfg['HANDS_COMMIT']*(w['hands']==2)*_heft
    pen=min(pen, cfg['MAX_TEMPO_PEN'])
    pen += cfg['CHOKE_TEMPO_PEN']*getattr(c,'grip_position',0.0)   # gathering in trades cadence for close control — CONTINUOUS in grip_position (no choke string)
    pen += cfg['LUNGE_TEMPO_PEN']*getattr(c,'lunge_depth',0.0)     # an extended/lunged body is slower to repeat — CONTINUOUS in lunge_depth
    t=cfg['BASE_TEMPO']+w['spd']*cfg['SPEED_K']+cfg['AGI_TEMPO_K']*(c.agi-4)-pen   # athleticism adds a LITTLE cadence (Jordan 2026-06-04); centred at agi 4 so default fighters & the mirror are unchanged
    t*=(1-cfg['TEMPO_FATIGUE_K']*fatigue)               # fatigue slows the rate of action
    t*=poise_factor(c, cfg)                            # DYNAMIC structure/balance: a kuzushi'd fighter acts slower (1.0 at full)
    return max(cfg['TEMPO_FLOOR'],t)
def close_tempo(c, cfg, fatigue=0.0):
    """Cadence IN THE CLOSE — conditional (fatigue/grip). A long two-handed pole (spear/staff) is SLOW to recover
    once a faster weapon is inside UNLESS it chokes up (grip adjustment to act in close quarters). Spread COMPRESSED
    toward the mean so action-frequency is a secondary edge, not the deciding axis (reach governs)."""
    t=weapon_tempo(c,cfg,fatigue)
    # a weapon UNWIELDY in the close (DERIVED from reach — long business-end) is slow to recover once a handier
    # weapon is inside; GATHERING IN (grip_position) reduces the penalty in proportion (a fully-gathered pole pays
    # none). Pure morphology, CONTINUOUS in grip_position (no choke string, no closes_poorly flag).
    t -= cfg['POLE_CLOSE_K']*close_unwieldiness(c,cfg)*(1.0 - getattr(c,'grip_position',0.0))
    t=max(cfg['TEMPO_FLOOR'],t)
    return cfg['CLOSE_TEMPO_MEAN'] + (t-cfg['CLOSE_TEMPO_MEAN'])*cfg['CLOSE_TEMPO_COMPRESS']

# ---------- stamina ----------
def stamina_max(c):
    return c.stamina_max          # the combatant HOSTS its derived figures; thin accessor (back-compat)
def act_cost(c, commit, cfg):
    return (cfg['ACT_BASE']+cfg['ACT_WEIGHT']*wield_heft(c,cfg)+cfg['ACT_COMMIT']*commit)*cfg['COST_SCALE']   # DERIVED g-aware heft (Stage 2b)

# ---------- concentration (Focus+Spirit tracker) ----------
def conc_max(c, cfg):
    c.derive_stats(cfg); return c.conc_max   # the combatant HOSTS it (3F+2S, ED-902); thin accessor (back-compat)
def reading(c, cfg): return (2*c.cog + c.att)/3 + cfg['READ_HISTORY_K']*(c.history-3)   # cog primary, Att half, + relevant-History experience (Jordan 2026-06-03)
def reflex(c, cfg): return (cfg['REFLEX_AGI']*c.agi+cfg['REFLEX_ATT']*c.att)/(cfg['REFLEX_AGI']+cfg['REFLEX_ATT'])

# ---------- strength handling + endurance fatigue ----------
def str_demand(c, cfg):
    w=c.w; return cfg['D0']+cfg['D_LEN']*reach_base(c,cfg)+cfg['D_WT']*wield_heft(c,cfg)+cfg['D_HAND']*HANDLE_RANK[w['hand']]+cfg['D_2H']*(w['hands']==2)   # DERIVED g-aware heft (Stage 2b)
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
def recoverability_factor(c, cfg):
    """IRRECOVERABILITY multiplier on the overcommit cost — the commitment=recovery axis, made physical and
    GRIP-AWARE (Phase-3 Stage 2, grounded). Reads the DERIVED dynamics at the chosen grip-position (WP.at_grip):
      - SWING arrest: sqrt of the re-pivoted MoI (energy-limited Δt=Iω/τ), GATED by the forward static moment so a
        centre-balanced pole (a staff) is NOT mis-ranked as irrecoverable;
      - THRUST retract: the forward static moment alone (it retracts along the line);
      blended by point_concentration (CONTINUOUS head weight — a hand-balanced rapier retracts, a forward mace
      'wants to continue'; no head NAME); a MoI-aware 1H/2H force-couple control credit; and the body-extension
      (lunge) term — the lead, best-grounded axis (Silver true-times / Giganti). Normalized to a 2H cut-thrust
      anchor (recoverability 1.0; the mirror is symmetric). Bounded below. Pure. The sqrt(I)/parallel-axis/couple
      STRUCTURE is [ASSERTED — first-principles]; the gains are [FIAT/SIM-CALIBRATE]. See tasks/w811gujrg.output."""
    w=c.w
    g  = getattr(c, 'grip_position', 0.0)
    ld = getattr(c, 'lunge_depth', 0.0)
    a = WP.at_grip(w, g)
    I_g, S_g = max(1e-9, a['I_g']), a['S_g']
    I_ref, S_ref = cfg['REC_I_REF'], cfg['REC_S_REF']
    two = 1.0 if w['hands'] == 2 else 0.0
    pc = w['geometry']['point_concentration']                                  # CONTINUOUS thrust-ness (rapier .95, mace .02)
    # (A) MODE commitment — both dimensionless vs the anchor, then blended by geometry
    C_swing  = sqrt(I_g / I_ref) * (cfg['REC_S_FLOOR'] + (1 - cfg['REC_S_FLOOR']) * S_g / S_ref)
    C_thrust = cfg['REC_THRUST_BASE'] + cfg['EXPOSE_MOMENT_K'] * (S_g / S_ref - 1)
    C_mode   = pc * C_thrust + (1 - pc) * C_swing
    # (C) 1H/2H CONTROL via the force-couple, MoI-aware (anchor-normalized: the reference gives credit 1.0)
    tau     = (1 + cfg['REC_W2'] * two) * (1 + cfg['REC_K_COUPLE'] * w['grip_len'] * WP.UNIT_M * two)
    tau_ref = (1 + cfg['REC_W2'])      * (1 + cfg['REC_K_COUPLE'] * cfg['REC_GRIP_REF'] * WP.UNIT_M)
    arrest  = (tau / sqrt(I_g)) / (tau_ref / sqrt(I_ref))                       # >1 = more controllable than the anchor
    ctrl_credit = 1 - cfg['REC_CTRL_K'] * max(0.0, arrest - 1) * (1 - pc)       # a SWUNG weapon gains from 2H control; a thrust barely
    # (D) BODY-EXTENSION (lunge) — the lead axis; fires from the wrapper as lunge_depth
    lunge_mult = 1 + cfg['EXPOSE_LUNGE_K'] * ld * (w.get('mass', 1.0) / cfg['LUNGE_REF_MASS']) ** cfg['MOMENT_MASS_EXP']
    return max(cfg['RECOVER_FLOOR'], C_mode * ctrl_credit * lunge_mult)
def close_unwieldiness(c, cfg):
    """How poorly a weapon serves IN THE CLOSE — DERIVED from its reach (a long weapon's business end is past the
    fight at grappling distance and slow to bring back to bear). 0 for a short/handy weapon. No closes_poorly flag:
    pure morphology (reach = length + head + hands)."""
    return max(0.0, reach_base(c,cfg) - cfg['CLOSE_REACH_REF'])
def can_choke(c, cfg):
    """Can the fighter gather in (regrip toward the centre)? DERIVED from the grippable length — a long shaft/grip
    yes, a short hilt or a block-headed club no. Thin bool over WP.grip_choke_max (the continuous primitive)."""
    return WP.grip_choke_max(c.w) > 0.0
def grip_target(c, closed, cfg):
    """The CONTINUOUS grip-position g* in [0,1] the fighter adopts (The Approach — footwork & stance), fully DERIVED
    from morphology — replaces the discrete adopt_stance string ('choke' was g>0, 'normal' g=0). Once the measure is
    CLOSED, a fighter GATHERS IN (g>0) in proportion to how unwieldy the weapon is in the close (close_unwieldiness),
    bounded by how far it can regrip (WP.grip_choke_max): a pole gathers up the haft; a rapier (short hilt) cannot
    and just suffers. At open measure g=0 (full reach). Pure (returns g; the wrapper writes grip_position)."""
    if not closed:
        return 0.0
    drive = min(1.0, close_unwieldiness(c, cfg) / cfg['CHOKE_DRIVE_REF'])     # 0..1: the more unwieldy in the close, the more you gather
    return WP.grip_choke_max(c.w) * drive
def lunge_quality(c, cfg):
    """How well a weapon LUNGES (an extended-body thrust) — DERIVED, CONTINUOUS (Phase-3 Stage 2). A light, hand-
    balanced, point-concentrated weapon lunges well; the hard head-NAME gate ('point'/'cut_thrust') becomes the
    CONTINUOUS point_concentration weight (a blunt/cut head -> ~0, never an exact-0 category). Hand-balance is the
    DERIVED forward static moment (no hand-set pob_frac). Propensity in [0,1]; the wrapper rolls against it. Pure."""
    w=c.w
    pc      = w['geometry']['point_concentration']                                          # CONTINUOUS thrust-ness (was the head-name gate)
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
def mode_sigma(mode, aggressor, defender, commit, choke, read_win, fat_d, cfg):
    """defender's δσ for a chosen defensive mode. Reading universal; +2 axis-specific. Skills bias per-axis."""
    rd=reading(defender,cfg)-reading(aggressor,cfg)
    rfx=reflex(defender,cfg); tech=defender.history+defender.skill('technique')
    ftw=balance_eff(defender,fat_d,cfg); strn=defender.strength
    base=cfg['READ_K']*rd*(1.3 if read_win else 0.7)
    cap=WP.defense_affinities(defender.w)[mode]   # DERIVED from geometry+dynamics (retired the hand GATE table)
    if mode=='parry':
        sig=cfg['PARRY_K']*(0.45*(rfx-3)+0.45*(tech-3))/3 + defender.skill('parry')
        # "don't parry with your hands!": an unguarded weapon's parry exposes the hand -> penalised; a guarded one
        # parries confidently. Scales the parry around a neutral simple-cross guard.
        sig += cfg['PARRY_GUARD_K']*(defender.w['hand_guard']-cfg['GUARD_NEUTRAL'])
    elif mode=='dodge':
        sig=cfg['DODGE_K']*(0.30*(rfx-3)+0.70*(ftw-3))/3 + defender.skill('dodge')
    else:               # wind (in the bind): fore/thumb-rings "enhance winding"
        sig=cfg['WIND_K']*(0.45*(tech-3)+0.45*(strn-aggressor.strength))/3 + cfg['CHOKE_BIND_K']*choke + defender.skill('bind')
        sig += cfg['WIND_GUARD_K']*(defender.w['blade_guard']-cfg['GUARD_NEUTRAL'])
    _deep=max(0.0,min(1.0,commit-3.0))     # CONTINUOUS commit response: 0 at <=3, ramps to 1 at >=4 (no integer cliff)
    _shallow=max(0.0,min(1.0,3.0-commit))  # 0 at >=3, ramps to 1 at <=2
    if mode=='parry': sig-=0.25*_deep      # a deep commit is easier to parry (committed line); a shallow probe harder to catch
    if mode=='dodge': sig+=0.10*_deep-0.10*_shallow   # deep commit easier to void; a shallow feint harder to read for the dodge
    return (base+sig)*cap

def adef_cap(w, cfg, head=None):
    """The aggressor head's RAW armour-defeat CAPABILITY (head-based, armour-tier-independent): the best mode its head
    can deliver vs a harness. Consumed by armor_defeat_sigma (vs the per-tier threshold) AND reach_threat (the FIX-1
    deficit). Blunt = the BETTER of CONCUSSION (broad percussion authority — a mace dents the harness) or PUNCTURE (a
    concentrated beak/spike that pierces plate — the poleaxe queue); both DERIVED (Phase-3b retires hand-set
    `percussion`): concussion~percussion_authority, puncture~percussion_authority x strike_concentration (a broad
    mace face sc~0 -> no puncture; a spike sc high -> pierces). A wooden staff (low authority) does NEITHER. A
    cut-and-thrust sword takes the better of its cut or a half-sword gap-thrust; a point thrusts to gaps; a pure
    cutter collapses (ADEF_CUT).

    `head` (the SELECTED mode-head from select_mode) overrides w['head'] when the wielder has committed to a specific
    mode this exchange: a poleaxe whose select_mode chose 'point' (the spike) is scored on the spike's gap-thrust, not
    the better-of-blunt max. head=None keeps the native head (the per-head max over the weapon's intrinsic modes) — so
    every existing caller is byte-identical. percussion_authority now carries the §1 energy-credit (poleaxe 5.83 < mace
    7.45 — the poleaxe's plate edge is NOT concussion; see select_mode)."""
    head = head if head is not None else w['head']
    if head=='blunt':
        return max(cfg['ADEF_BLUNT']*(WP.percussion_authority(w)/cfg['ADEF_PERC_REF']),
                   cfg['ADEF_POINT']*(WP.puncture_pressure(w)/cfg['ADEF_PERC_REF']))
    if head=='point':      return cfg['ADEF_POINT']*w['gap']
    if head=='cut_thrust': return max(cfg['ADEF_CUT'], cfg['ADEF_POINT']*w['gap'])   # cut OR half-sword gap-thrust
    return cfg['ADEF_CUT']                                                            # straight/curved pure cut collapses

# ── primitive-emergent USE-MODE selection (the per-exchange technique choice) ───────────────────────────────────
# grounded_weapon_armour_usemode_model.md §3-4 (tasks wht7pkx1c / w4bekmb5e). There is NO per-weapon mode table:
# the AFFORDED modes + their effectiveness DERIVE from each weapon's existing geometry primitives, so poleaxe/mace/
# staff are just bundles of primitives, never a name-keyed list (the L0 primitive-law). The modes are the UNIVERSAL
# set {thrust, cut, percuss, puncture}; each maps to one of the engine's existing head TOKENS (so the downstream
# coupling/adef/legibility machinery is unchanged) and one DAMAGE mode. The wielder greedily SELECTS the afforded
# head whose resulting damage-coupling vs THIS armour is highest — generalizing the existing cut_thrust max() and the
# blunt max(concussion,puncture) from 2 modes to N. Pure.
SELECT_EPS = 0.05         # [DESIGN] affordance floor on a derived per-mode effectiveness: a mode is afforded iff its
                          #   derived effectiveness exceeds this (so a vanishing mode is not even a candidate). Small.
SELECT_PC_MIN = 0.10      # [DESIGN] raw point_concentration below which a head has NO thrusting point (a blunt FACE
                          #   that concentrates percussion but cannot pierce a gap): mace 0.02 -> no spike; poleaxe
                          #   0.78 / spear 0.78 -> a real point. Reads the raw primitive the design names, so the
                          #   mace-vs-poleaxe spike distinction EMERGES from morphology, not a weapon name.

def afforded_heads(w):
    """The set of head TOKENS this weapon can fight in, DERIVED from its geometry primitives (NOT a per-weapon list).
    Each maps token -> (derived effectiveness, damage_mode). A natively-versatile cut_thrust head stays ATOMIC (the
    engine's coupling/adef/legibility already resolve its cut<->gap-thrust internally) so its current behaviour is
    preserved exactly. A blunt head additionally affords the 'point' spike-thrust IFF it has a real piercing point
    (point_concentration > PC_MIN) — the poleaxe's beak emerges, the mace's flat face does not. Pure."""
    geo=w['geo']; head=w['head']; pc=geo['point_concentration']
    heads={}
    if head=='cut_thrust':                                            # versatile blade: keep atomic (internal max)
        heads['cut_thrust']=(max(geo['cut'], geo['gap']), 'shear_or_puncture')
    elif head in ('straight_cut','curved_cut','cut'):                # pure cutter
        if geo['cut']>SELECT_EPS: heads[head]=(geo['cut'], 'shear')
    elif head=='point':                                              # pure point
        if geo['gap']>SELECT_EPS and pc>SELECT_PC_MIN: heads['point']=(geo['gap'], 'puncture')
    elif head=='blunt':                                              # striking head
        if WP.percussion_authority(w)>SELECT_EPS: heads['blunt']=(WP.percussion_authority(w), 'percussion')
        if pc>SELECT_PC_MIN and geo['gap']>SELECT_EPS:               # a beak/spike: a real point ON a blunt haft
            heads['point']=(geo['gap'], 'puncture')
    if not heads:                                                    # degenerate fallback: never strip all modes
        heads[head]=(0.0, core.HEAD_MODE.get(head, 'shear'))
    return heads

_HEAD2DMG={'blunt':'percussion','point':'puncture','straight_cut':'shear','curved_cut':'shear','cut':'shear'}
def select_mode(c, defender_armor, closed, cfg):
    """PURE per-exchange use-mode selection. Derives the afforded head tokens from c.w's primitives (afforded_heads),
    then greedily SELECTS the one whose resulting damage-coupling vs defender_armor is highest — the effectiveness-vs-
    armour baseline the design §3 names ('exactly the existing coupling/adef_cap max(), generalized from 2 modes to
    N'). Reproduces every single-mode weapon's current head (rapier->point, sabre->curved_cut, arming/longsword/
    dagger->cut_thrust, mace/staff->blunt) and the poleaxe (the one weapon that affords >1 head: blunt+spike). NOTE
    [2026-06-30 finding]: under the grounded credited authority (poleaxe 5.83, a strong concussor) + the §2 RESIST
    table (plate.percussion .30 < plate.puncture .70, i.e. plate is modelled MORE vulnerable to concussion than to
    the spike), the greedy comparator selects the poleaxe's BLUNT mode at every armour tier — its concussion out-
    couples its spike vs plate (0.93 vs 0.44). The spike is AFFORDED and ready but not selected; flipping it would
    require re-tuning the frozen §2 RESIST / ADEF constants (out of scope). Returns (damage_mode, eff_head): eff_head
    is the head TOKEN routed downstream (core.strike/adef_cap/legibility), damage_mode the resolved 'percussion'/
    'shear'/'puncture'. The wrapper writes both onto the combatant (mutation stays wrapper-owned, like grip_position)."""
    w=c.w
    heads=afforded_heads(w)
    if len(heads)==1:                                                # single afforded mode: no choice (the common case)
        h=next(iter(heads))
    else:
        # greedy: the mode delivering the most damage-coupling THROUGH this armour (perc carries the blunt authority
        # so a high-authority hammer's through-plate transmit competes with a spike's gap-thrust on the same scale).
        h=max(heads, key=lambda hd: core.coupling(hd, defender_armor,
                  perc=WP.percussion_authority(w) if hd=='blunt' else core.PERC_AUTH_REF))
    if h=='cut_thrust':
        # atomic versatile head: the damage coupling already takes max(cut, half-sword gap-thrust) internally, so the
        # head token is unchanged. The REPORTED mode (legibility only) follows the documented armour-conditional shift
        # the engine has always modelled: a cut-thrust sword SWINGS (cuts) — reads easy — until it must half-sword-
        # thrust to the gaps vs a harness (medium/heavy), then reads hard. This reproduces the prior legibility exactly.
        dm = 'puncture' if defender_armor in ('medium','heavy') else 'shear'
    else:
        dm=_HEAD2DMG.get(h, core.HEAD_MODE.get(h,'shear'))
    return dm, h

def armor_defeat_sigma(aggressor, defender, cfg):
    """In armour, the weapon that CAN defeat the armour controls the exchange. Net-sigma adjustment for the aggressor
    vs the defender's armour: capability ABOVE the per-tier threshold = control (+); below = the armour SHIELDS (−).
    The threshold RISES with armour (monotonically harder). Zero unarmoured (ADEF_W['none']=0). Reads the aggressor's
    SELECTED mode-head (sel_head, set by the wrapper from select_mode) so the armour-defeat path scores the mode the
    wielder actually committed to; falls back to the native head when unset (byte-identical)."""
    a=cfg['ADEF_W'][defender.armor]
    if a==0.0: return 0.0
    return a*(adef_cap(aggressor.w, cfg, getattr(aggressor,'sel_head',None)) - cfg['ADEF_THRESHOLD'][defender.armor])

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
    deficit=max(0.0, cfg['ADEF_THRESHOLD'][defender.armor] - adef_cap(longer.w, cfg))
    return max(cfg['REACH_THREAT_FLOOR'], 1.0 - cfg['REACH_DECAY_K']*aw*deficit)

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

def impose_node(aggressor, defender, hit, bind, riposte, cfg, rng, TR):
    """WS-4/WS-5 imposition (section C, flag-gated): a tradition biases the exchange toward its PREFERRED node,
    DECOUPLED from channel magnitude (fixed normalized rates, not eff_cw — the repair the gate-reconciliation
    requires: the magnitude must not drive imposition). German (bind-seeker) imposes the crossing; the
    bind-refusers (Italian/English/Spanish counter/measure schools) slip a forming bind into a counter
    (cavazione/disengage). A landed hit is never re-routed. Pure (reads rng); returns (bind, riposte)."""
    if hit > 0:
        return bind, riposte
    pa = TR.preferred(aggressor.tradition); pd = TR.preferred(defender.tradition)
    if pa == 'bind' and not bind and rng.random() < cfg['IMPOSE_BIND_BOOST']:
        bind = True                                  # German forces the crossing onto an unwilling opponent
    if pd in ('counter', 'measure') and bind and rng.random() < cfg['IMPOSE_REFUSE_P']:
        bind = False; riposte = True                 # the refuser slips the bind into a single-time counter
    return bind, riposte


# weapons that have a half-sword form, and the form mapping (base <-> shortened)
# HALFSWORD_FORM / HALFSWORD_BASE are weapon DATA (single source in weapons.py, inverse derived); imported above.

def halfsword_target(c, closed, opp_armor):
    """PURE predicate: the weapon-form a half-sword-capable fighter SHOULD be in for the current range/armour
    (mit dem kurzen Schwert). Half-sword vs ARMOUR in the CLOSE (gap-thrust/leverage excel); full form at reach / vs
    unarmoured. Returns the target weapon string; the WRAPPER applies the mutation (mutation stays wrapper-owned).
    Weapons without a half-sword form return their current weapon unchanged."""
    base = HALFSWORD_BASE.get(c.weapon, c.weapon)
    if base not in HALFSWORD_FORM: return c.weapon
    want_half = closed and opp_armor in ('medium','heavy')
    return HALFSWORD_FORM[base] if want_half else base

# ============================================================================
# RESOLUTION-CONTRIBUTION MODULES (functional: pure, role-objects-in, contribution-out).
# The wrapper owns ALL state mutation; these never index raw A/B and never mutate combatants.
# Each takes Combatant OBJECTS by role (aggressor/defender or longer/shorter) so roles cannot invert inside them.
# ============================================================================

def reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR):
    """Standing measure-domain sigma the DEFENDER's reach imposes on the aggressor (proportional to gap, weighted
    high unarmoured, falling with armour). +ve lowers the attacker's net. Pure."""
    gap=er[defender]-er[aggressor]
    foot_meas=cfg['FOOT_MEASURE_K']*(balance_eff(defender,fat_d,cfg)*TR.eff_cw(defender, 'balance')
                                     - balance_eff(aggressor,fat_a,cfg)*TR.eff_cw(aggressor, 'balance'))
    meas_w = TR.eff_cw(defender, 'measure')/TR.eff_cw(aggressor, 'measure')
    reach_edge=(gap*cfg['REACH_FRAC']+foot_meas)*meas_w
    return cfg['REACH_W'][defender.armor]*reach_edge

def legibility(aggressor, commit, cfg, opp_armor='none'):
    """Read-legibility multiplier on the DEFENDER's visual read: a THRUST (in-line) is hard to read; a SWING/CUT
    (lateral arc) and a percussive BLUNT blow are easy; deeper commit/lunge = more readable. Legibility follows the
    MODE the wielder ACTUALLY fights in this exchange — the SELECTED damage-mode (sel_dmg, written by the wrapper from
    select_mode): puncture/thrust read HARD, shear/percuss read EASY. This is the one real use-mode wiring change (the
    fixed-head logic only ever inferred the mode from head+armour; now it reads the selected mode directly). Falls
    back to the prior head+armour inference when sel_dmg is unset, so it is byte-identical for every existing caller
    (a cut_thrust sword's sel_dmg is 'shear' unarmoured -> swing, 'puncture' vs plate -> thrust, matching coupling). Pure."""
    dm=getattr(aggressor,'sel_dmg',None)
    if dm is not None:
        legib = cfg['LEGIB_THRUST'] if dm=='puncture' else cfg['LEGIB_SWING']   # thrust hard; cut/percuss easy
    else:
        ah=aggressor.w['head']
        if ah=='point':                       legib=cfg['LEGIB_THRUST']      # always a thrust
        elif ah in ('straight_cut','curved_cut'): legib=cfg['LEGIB_SWING']   # pure cutters always swing
        elif ah=='blunt':                     legib=cfg['LEGIB_SWING']       # percussive arc, easy to read
        elif ah=='cut_thrust':
            # shifts to a controlled gap-thrust vs plate (hard to read), otherwise cuts (easy) — matches coupling's mode-shift
            legib=cfg['LEGIB_THRUST'] if opp_armor in ('medium','heavy') else cfg['LEGIB_SWING']
        else:                                 legib=1.0
    legib += cfg['LEGIB_COMMIT_K']*max(0,commit-3)
    legib += cfg['LEGIB_LUNGE']*getattr(aggressor,'lunge_depth',0.0)   # an extended/lunged body is more readable — CONTINUOUS in lunge_depth (no lunge string)
    return legib

def approach_displace(shorter, longer, cfg):
    """Lever-arm displacement-on-approach: a higher-leverage closer sets aside a THRUSTING longer weapon's point,
    suppressing its stop-hit and speeding the close. Returns a fraction in [0, APPROACH_DISPLACE_MAX]. Pure."""
    lever_edge = leverage(shorter,cfg) - leverage(longer,cfg)
    if longer.w['head']!='point' or lever_edge<=0: return 0.0
    rd=(reading(shorter,cfg)-reading(longer,cfg))
    return min(cfg['APPROACH_DISPLACE_MAX'], cfg['APPROACH_DISPLACE_K']*lever_edge*(1+0.1*rd))

def reopen_prob(longer, shorter, base_gap, fat_longer, push_avail, cfg, TR):
    """Probability the LONGER weapon regains distance given a created moment exists: reads to seize vs shorter's
    denial, executes with balance, scaled by armour; freed-hand shove adds a path. Pure (returns a probability).
    RR-02: takes the longer fighter's actual fatigue (was hardcoded 0). RR-03: normalises by REACH_W['none']."""
    id_read = reading(longer,cfg)*TR.eff_cw(longer, 'visual')
    deny_read = reading(shorter,cfg)*TR.eff_cw(shorter, 'visual')
    read_edge = 1/(1+exp(-(id_read-deny_read)/2.0))
    foot = balance_eff(longer,fat_longer,cfg)/3
    p=cfg['REOPEN_K']*base_gap*foot*read_edge*cfg['REACH_W'][shorter.armor]/cfg['REACH_W']['none']
    if push_avail: p += cfg['PUSH_REOPEN_BONUS']*foot
    return min(cfg['REOPEN_MAX'], p)

def bind_sigma(aggressor, defender, cfg, TR):
    """One bind iteration's net sigma: LEVERAGE (technique+skill + physical lever-arm) + BLADE-GUARD catch (the
    cross/quillons/rings that catch & control the opposing blade — a guardless pole binds poorly, a long cross
    excels) + TACTILE read (Fuhlen); Strength minor. +ve favours the aggressor winning the bind. Pure."""
    lev = ((aggressor.history+aggressor.skill('bind')) - (defender.history+defender.skill('bind')))*cfg['BIND_TECH_K'] \
          + (leverage(aggressor,cfg) - leverage(defender,cfg)) \
          * (TR.eff_cw(aggressor, 'leverage')/TR.eff_cw(defender, 'leverage'))
    catch = cfg['BIND_GUARD_K']*(aggressor.w['blade_guard'] - defender.w['blade_guard'])   # quillons/rings catch the blade
    tac = (reading(aggressor,cfg)*TR.eff_cw(aggressor, 'tactile')*TR.familiarity(aggressor.tradition,defender.tradition)
           - reading(defender,cfg)*TR.eff_cw(defender, 'tactile')*TR.familiarity(defender.tradition,aggressor.tradition))*cfg['BIND_TACTILE_K']
    strq = (aggressor.strength-defender.strength)*cfg['BIND_STR_K']
    wound = cfg['WOUND_DEF_OB']*defender.wt.wounds - cfg['WOUND_ATK_OB']*aggressor.wt.wounds   # ED-1041: wounds impair the bind too (defence ~1.6x), bind-aggressor/defender roles fixed through the loop
    return lev + catch + tac + strq + wound

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
    return (atk_sig - dsig - reach_pen + adef + init_edge + cfg['ATTACKER_BIAS']
            + cfg['WOUND_DEF_OB']*defender.wt.wounds - cfg['WOUND_ATK_OB']*aggressor.wt.wounds)

def commit_depth(aggressor, defender, cfg, rng, TR):
    """Draw the CONTINUOUS commitment depth in [2,5] (commitment-recovery is a spectrum, not four rungs). Disposition
    lean + WARINESS (vs an unread tradition the aggressor commits shallower) skew a Beta over the range; the 0.25
    param floor is the spread-floor (never collapses to a spike). Consumes one rng.beta draw (kept here so the
    wrapper sequences but owns no formula). Returns (commit, beta_a, beta_b, lean)."""
    ln=disp_lean(aggressor)
    wary=cfg['WARINESS_K']*(1-TR.familiarity(aggressor.tradition, defender.tradition))   # >=0, biases shallow
    g=cfg['COMMIT_BETA_K']*(cfg['DISP_COMMIT_K']*ln - wary)
    ba=max(0.25, cfg['COMMIT_BETA_BASE']*(1+g)); bb=max(0.25, cfg['COMMIT_BETA_BASE']*(1-g))
    commit=2.0+3.0*float(rng.beta(ba,bb))
    return commit, ba, bb, ln

def read_contest(aggressor, defender, commit, consistency_a, mental_fat_d, fat_d, cfg, rng, TR):
    """The defender's READ of the attack + the resulting mode selection. read_d (visual+precommit, familiarity-
    and legibility-scaled) vs read_a -> read_win (logistic). If the read wins, the defender picks the BEST mode;
    else it guesses. Consumes rng.random (the read) then rng.integers ONLY on a missed read — the same order as the
    inline version, so byte-identical. Pure resolution+selection logic moved out of the orchestrator. Returns a dict."""
    fam=TR.familiarity(defender.tradition, aggressor.tradition)
    legib=legibility(aggressor, commit, cfg, defender.armor)
    read_d=reading(defender,cfg)*TR.eff_cw(defender,'visual')*TR.eff_cw(defender,'precommit')*fam*legib*(1-cfg['MENTAL_FAT_READ_K']*mental_fat_d)
    read_a=reading(aggressor,cfg)*TR.eff_cw(aggressor,'visual')+consistency_a
    p_read=1/(1+exp(-(read_d-read_a)/1.0))
    read_win=rng.random() < p_read
    modes=['parry','dodge','wind']
    msig={m:mode_sigma(m,aggressor,defender,commit,0.0,read_win,fat_d,cfg) for m in modes}
    mode=max(msig,key=msig.get) if read_win else modes[rng.integers(3)]
    return dict(read_win=read_win, read_d=read_d, read_a=read_a, p_read=p_read, mode=mode, msig=msig)

def indes_steal_amount(defender, wind, commit, read_d, read_a, cfg, TR):
    """The Indes / sen-no-sen initiative-steal AMOUNT: a defender who out-read a deep commit steals the Vor, scaled
    by commit-depth x read-margin (bounded). Pure — the wrapper applies the clamp/mutation."""
    indes_scale=max(cfg['INDES_SCALE_FLOOR'], min(cfg['INDES_SCALE_CEIL'],
                    (1+cfg['INDES_COMMIT_K']*(commit-4))*(1+cfg['INDES_READ_K']*(read_d-read_a))))
    return cfg['INIT_STEAL_INDES']*init_steal_factor(defender, wind, TR)*indes_scale

def counter_select(defender, cfg, rng, TR):
    """Whether the defender reaches for the single-time counter (tempo-driven SELECTION; SUCCESS is gated later, a
    miss punished). Consumes one rng.random."""
    return rng.random() < cfg['COUNTER_SELECT_BASE']*TR.eff_cw(defender,'tempo')*max(0.0, 1-cfg['DISP_COUNTER_K']*disp_lean(defender))*TR.ability_factor(defender,'counter_select')

def overcommit_exposure(aggressor, commit, fat_a, cfg, TR):
    """The aggressor's exposure to the riposte from over-committing: commit-depth x irrecoverability, minus the
    anti-overcommit (balance) curb and trained discipline. Pure; floored at 0. The wrapper applies the loss."""
    return max(0.0, cfg['COMMIT_EXPOSE_K']*(commit-3)*recoverability_factor(aggressor,cfg)) - anti_overcommit(aggressor,fat_a,cfg) - TR.ability_bonus(aggressor,'anti_overcommit')

def clamp_initiative(x, cfg):
    """Hard bound on |initiative| (the CAP safeguard; paired with the wrapper's per-beat DECAY = the damper)."""
    return max(-cfg['INIT_CAP'], min(cfg['INIT_CAP'], x))

# ---------- initiative DIFFERENTIATION layer (per-tradition signature = channel weight x substrate mechanism) ----------
# A pure layer on top of the substrate: each tradition's signature initiative ability is just its existing channel
# weight multiplying the relevant substrate magnitude. No tradition-name branches; neutral tradition = 1.0 everywhere
# (so default fighters are unaffected and every invariant holds by construction).
def init_steal_factor(stealer, bind_active, TR):
    """WHO steals the Vor best. In a BIND (winding), the steal scales with tactile+leverage — German Fühlen /
    Stärke-Schwäche. In the OPEN, with tempo — Italian contratempo (the single-time counter). Neutral = 1.0."""
    if bind_active:
        return (TR.eff_cw(stealer, 'tactile') + TR.eff_cw(stealer, 'leverage'))/2
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
def stophit_sigma(longer, shorter, measure_gap, cfg):
    """The APPROACH-path stop-hit net-sigma (the longer weapon threatening across the closing gap). The analog of
    assemble_net_sigma for the approach: reach-disadvantage by gap + base + bilateral wound-Ob. Pure."""
    return (cfg['REACH_DISADV_K']*measure_gap + cfg['STOPHIT_NSIG_BASE']
            + cfg['WOUND_DEF_OB']*shorter.wt.wounds - cfg['WOUND_ATK_OB']*longer.wt.wounds)

def close_rate(shorter, ffat_shorter, displ, rt, cfg):
    """Measure-domain closing RATE for the shorter weapon walking in: athletic close-speed (balance x cadence),
    sped by displacing a thrusting point (displ) and by walking through an un-threatening reach (2.0-rt). Pure."""
    cr = cfg['CLOSE_RATE_K']*balance_eff(shorter,ffat_shorter,cfg)/3 * weapon_tempo(shorter,cfg,ffat_shorter)/2
    return cr*(1+displ)*(2.0-rt)

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
    return 1/(1+exp(-bsig))

def disrupt_resist_p(c, cfg):
    """Concentration disruption-resistance: P(the fighter completes a simultaneous strike despite being hit),
    logistic in Focus. Pure."""
    return 1/(1+exp(-cfg['DISRUPT_K']*(c.focus-3)))
