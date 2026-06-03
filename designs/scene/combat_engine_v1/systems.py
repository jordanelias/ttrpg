"""Subsystem modules. Uniform contract: each is a pure function of (aggressor, defender, state, cfg[, rng]).
NO subsystem touches raw A/B — they receive Combatant objects in role. This isolates every mechanic for
unit-testing and makes the coupling explicit (the fix for the recurring inversion bugs)."""
import sys; sys.path.insert(0,'/home/claude/combat_engine')
from math import exp
from config import HANDLE_RANK
import core
from combatant import WEAPONS

# ---------- reach (continuous, derived) ----------
def reach_base(c, cfg):
    w=c.w
    return (cfg['L0']+cfg['LONG']*(w['reach']=='long')+cfg['HANDS2']*(w['hands']==2)
            +cfg['HEADR']*cfg['HEAD_REACH'][w['head']] + w.get('reach_adj',0.0))

# ---------- tempo ----------
def weapon_tempo(c, cfg, fatigue=0.0):
    """General cadence — CONDITIONAL on grip/stance/fatigue (correction 2), not a static weapon property. Heavy
    weapons are slower but NOT tempo-dead (penalty bounded). Fatigue reduces cadence (a tiring fighter acts less
    often). A choked grip trades cadence for close-quarters control; a lunge/extended grip trades repeat-speed for
    reach (handled at the call site via grip state)."""
    w=c.w
    pen=cfg['WEIGHT_PEN']*(w['wt']=='heavy')+cfg['HANDS_COMMIT']*(w['hands']==2 and w['wt']=='heavy')
    pen=min(pen, cfg['MAX_TEMPO_PEN'])
    grip=getattr(c,'grip','normal')
    if grip=='choke':  pen += cfg['CHOKE_TEMPO_PEN']    # choked grip: a bit slower cadence (control/leverage gain elsewhere)
    elif grip=='lunge':pen += cfg['LUNGE_TEMPO_PEN']    # extended/lunge: slower to repeat (reach/commit gain elsewhere)
    t=cfg['BASE_TEMPO']+w['spd']*cfg['SPEED_K']-pen
    t*=(1-cfg['TEMPO_FATIGUE_K']*fatigue)               # fatigue slows the rate of action
    return max(cfg['TEMPO_FLOOR'],t)
def close_tempo(c, cfg, fatigue=0.0):
    """Cadence IN THE CLOSE — conditional (fatigue/grip). A long two-handed pole (spear/staff) is SLOW to recover
    once a faster weapon is inside UNLESS it chokes up (grip adjustment to act in close quarters). Spread COMPRESSED
    toward the mean so action-frequency is a secondary edge, not the deciding axis (reach governs)."""
    t=weapon_tempo(c,cfg,fatigue)
    w=c.w; grip=getattr(c,'grip','normal')
    is_long_pole = (w['hands']==2 and w['reach']=='long' and w['spd']<=0.0 and w['wt']=='light')  # spear, staff
    # a long pole pays the closed penalty UNLESS it has choked up to fight close (grip adjustment offsets it)
    if is_long_pole and grip!='choke': t -= cfg['POLE_CLOSE_PENALTY']
    t=max(cfg['TEMPO_FLOOR'],t)
    return cfg['CLOSE_TEMPO_MEAN'] + (t-cfg['CLOSE_TEMPO_MEAN'])*cfg['CLOSE_TEMPO_COMPRESS']

# ---------- stamina ----------
def stamina_max(c): 
    import r8_parity_harness as r8; return r8.stamina_max(c.end,c.spirit)
def act_cost(c, commit, cfg):
    return (cfg['ACT_BASE']+cfg['ACT_WEIGHT']*(c.weight=='heavy')+cfg['ACT_COMMIT']*commit)*cfg['COST_SCALE']

# ---------- concentration (Focus+Spirit tracker) ----------
def conc_max(c, cfg):
    return cfg['CONC_BASE_K']*(cfg['CONC_FOCUS']*c.focus+cfg['CONC_SPIRIT']*c.spirit)/(cfg['CONC_FOCUS']+cfg['CONC_SPIRIT'])
def reading(c): return (c.cog+c.att)/2
def reflex(c, cfg): return (cfg['REFLEX_AGI']*c.agi+cfg['REFLEX_ATT']*c.att)/(cfg['REFLEX_AGI']+cfg['REFLEX_ATT'])

# ---------- strength handling + endurance fatigue ----------
def str_demand(c, cfg):
    w=c.w; return cfg['D0']+cfg['D_LEN']*reach_base(c,cfg)+cfg['D_WT']*(w['wt']=='heavy')+cfg['D_HAND']*HANDLE_RANK[w['hand']]+cfg['D_2H']*(w['hands']==2)
def handling_penalty(c, fat, cfg):
    deficit=max(0.0, str_demand(c,cfg)-c.strength)
    return cfg['HANDLE_K']*deficit + cfg['FATIGUE_HANDLE_K']*fat
def footwork_eff(c, fat, cfg):
    return (c.footwork + c.skill('footwork'))*(1-cfg['FATIGUE_FOOT_K']*fat)
def anti_overcommit(c, fat, cfg): return cfg['FOOT_COMMIT_DISC_K']*(footwork_eff(c,fat,cfg)-3)
def stance_stability(c, fat, cfg): return cfg['FOOT_STANCE_K']*(footwork_eff(c,fat,cfg)-3)

# ---------- defense modes (parry/dodge/wind) ----------
GATE={
 'rapier':{'parry':1.0,'dodge':0.8,'wind':0.4},'arming':{'parry':0.9,'dodge':0.8,'wind':0.7},
 'longsword':{'parry':0.9,'dodge':0.7,'wind':1.0},'greatsword':{'parry':0.7,'dodge':0.6,'wind':0.9},
 'sabre':{'parry':0.9,'dodge':0.9,'wind':0.6},'dagger':{'parry':0.6,'dodge':0.9,'wind':0.5},
 'paired_short':{'parry':1.0,'dodge':0.9,'wind':0.4},'spear':{'parry':0.8,'dodge':0.9,'wind':0.8},
 'staff':{'parry':0.9,'dodge':0.8,'wind':0.8},'mace':{'parry':0.7,'dodge':0.7,'wind':0.7},
 'poleaxe':{'parry':0.8,'dodge':0.5,'wind':1.0},
 'longsword_halfsword':{'parry':1.0,'dodge':0.5,'wind':1.0},
}
def mode_sigma(mode, aggressor, defender, commit, choke, read_win, fat_d, cfg):
    """defender's δσ for a chosen defensive mode. Reading universal; +2 axis-specific. Skills bias per-axis."""
    rd=reading(defender)-reading(aggressor)
    rfx=reflex(defender,cfg); tech=defender.history+defender.skill('technique')
    ftw=footwork_eff(defender,fat_d,cfg); strn=defender.strength
    base=cfg['READ_K']*rd*(1.3 if read_win else 0.7)
    cap=GATE[defender.weapon][mode]
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
    if mode=='parry' and commit>=4: sig-=0.25
    if mode=='dodge' and commit>=4: sig+=0.10
    if mode=='dodge' and commit<=2: sig-=0.10
    return (base+sig)*cap

def armor_defeat_bonus(c, defender, cfg):
    """Slow heavy weapons (poleaxe/mace) land FEW but armour-DEFEATING blows. Within the 3-exchange bout cap they
    can't out-volume, so each blow that lands on heavy armour gets an impact bonus reflecting its plate-defeating
    momentum (the war-hammer/poleaxe role). Scales with the defender's armour weight and the weapon's slowness."""
    w=c.w
    is_slow_heavy = (w['wt']=='heavy' and w['head']=='blunt' and w['spd']<=0.0)   # mace, poleaxe
    if not is_slow_heavy: return 0.0
    armor_factor={'none':0.0,'light':0.3,'medium':0.7,'heavy':1.0}[defender.armor]
    return cfg['SLOW_WEAPON_IMPACT_K']*armor_factor

def armor_defeat_sigma(aggressor, defender, cfg):
    """In armour, the weapon that CAN defeat the armour controls the exchange (reference 'lethality-in-state' term,
    and the reach->armour-defeat rotation). Returns a net-sigma adjustment for the aggressor vs the defender's armour:
    blunt/percussion and gap-thrust gain; pure cut COLLAPSES as armour rises. Zero unarmoured."""
    a=cfg['ADEF_W'][defender.armor]
    if a==0.0: return 0.0
    head=aggressor.w['head']
    # capability = the BEST mode available to this head vs armour. A cut-and-thrust sword may CUT or half-sword to a
    # gap-thrust POINT; it uses whichever is more effective — so a defender taking MORE armour never flips the
    # attacker into a suddenly-stronger mode (removes the light->medium cliff). Pure cutters cut; points thrust.
    if head=='blunt':
        # blunt armour-defeat scales with PERCUSSION AUTHORITY (§4): a steel hammer/beak (mace/poleaxe, perc 8)
        # defeats plate; a wooden quarterstaff (perc 4) does not — wood transmits little through plate. Reference =
        # perc 8 (full credit); lower percussion weapons get proportionally less armour-defeat.
        cap=cfg['ADEF_BLUNT']*(aggressor.w.get('percussion',8)/8.0)
    elif head=='point':
        cap=cfg['ADEF_POINT']*aggressor.w['gap']
    elif head=='cut_thrust':
        cut_cap=cfg['ADEF_CUT']
        point_cap=cfg['ADEF_POINT']*aggressor.w['gap']     # half-sword gap-thrust (precision-scaled)
        cap=max(cut_cap, point_cap)                         # take the better of cut vs half-sword at THIS armour level
    else:                                                   # straight/curved pure cut
        cap=cfg['ADEF_CUT']
    # RELATIVE to a per-state threshold: capability above the bar = control (+); below = the defender's armour
    # SHIELDS against you (−). The threshold RISES with armour, so more armour is monotonically harder to defeat.
    return a*(cap - cfg['ADEF_THRESHOLD'][defender.armor])

def leverage(c, cfg):
    """Lever-arm primitive: capacity to redirect/bind/displace another weapon, from grip BEHIND the contact vs head
    AHEAD of it (mechanical advantage). Long grip + compact head (poleaxe/longsword/staff) = high; long head/point on
    short grip (spear) or tiny weapon (dagger) = low. Two hands add control. Nominal scale ~ -1..+1 around a sword."""
    w=c.w
    ratio = w['grip_len']/(w['grip_len']+w['head_len'])      # fraction of the weapon that is grip (lever behind hand)
    lev = cfg['LEVER_K']*(ratio - cfg['LEVER_REF'])           # vs a reference sword ratio
    if w['hands']==2: lev += cfg['LEVER_2H']                  # two hands = more control over the lever
    return lev

# weapons that have a half-sword form, and the form mapping (base <-> shortened)
HALFSWORD_FORM = {'longsword':'longsword_halfsword'}
HALFSWORD_BASE = {'longsword_halfsword':'longsword'}

def halfsword_switch(c, closed, opp_armor, cfg):
    """Auto-switch a half-sword-capable weapon between its normal and shortened forms by distance/technique
    (mit dem kurzen Schwert). Half-sword is chosen when CLOSED and/or facing ARMOUR (its gap-thrust + leverage
    excel there); normal form is resumed at reach / vs the unarmoured at distance. Reversible; only toggles `weapon`.
    Returns True if half-sword form is now active."""
    base = HALFSWORD_BASE.get(c.weapon, c.weapon)
    if base not in HALFSWORD_FORM: return c.weapon.endswith('_halfsword')
    want_half = closed and opp_armor in ('medium','heavy')   # half-sword's purpose: gap-thrust/leverage vs armour in the close
    if not closed: want_half=False                           # at reach, keep the full-length cutting form
    c.weapon = HALFSWORD_FORM[base] if want_half else base
    return want_half

# ============================================================================
# RESOLUTION-CONTRIBUTION MODULES (functional: pure, role-objects-in, contribution-out).
# The wrapper owns ALL state mutation; these never index raw A/B and never mutate combatants.
# Each takes Combatant OBJECTS by role (aggressor/defender or longer/shorter) so roles cannot invert inside them.
# ============================================================================

def reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR):
    """Standing measure-domain sigma the DEFENDER's reach imposes on the aggressor (proportional to gap, weighted
    high unarmoured, falling with armour). +ve lowers the attacker's net. Pure."""
    gap=er[defender]-er[aggressor]
    foot_meas=cfg['FOOT_MEASURE_K']*(footwork_eff(defender,fat_d,cfg)*TR.channel_weight(defender.tradition,'footwork')
                                     - footwork_eff(aggressor,fat_a,cfg)*TR.channel_weight(aggressor.tradition,'footwork'))
    meas_w = TR.channel_weight(defender.tradition,'measure')/TR.channel_weight(aggressor.tradition,'measure')
    reach_edge=(gap*cfg['REACH_FRAC']+foot_meas)*meas_w
    return cfg['REACH_W'][defender.armor]*reach_edge

def legibility(aggressor, commit, cfg):
    """Read-legibility multiplier on the DEFENDER's visual read of the aggressor's attack: swings/lunges easy
    (lateral, large), thrusts hard (in-line); deeper commit/lunge = more readable. Pure."""
    ah=aggressor.w['head']
    if ah in ('straight_cut','curved_cut'): legib=cfg['LEGIB_SWING']
    elif ah=='point':                       legib=cfg['LEGIB_THRUST']
    elif ah=='blunt':                        legib=cfg['LEGIB_SWING']
    else:                                    legib=1.0
    legib += cfg['LEGIB_COMMIT_K']*max(0,commit-3)
    if getattr(aggressor,'grip','normal')=='lunge': legib += cfg['LEGIB_LUNGE']
    return legib

def feint_eval(aggressor, defender, mental_fat_d, feint_streak, cfg, rng, TR):
    """Decide/resolve a feint. Pure (reads rng): returns dict {do, debuff, new_streak, beat_cost, stamina_cost}.
    A fooled defender's real-attack defence/read is degraded; a defender who READS it gains a small counter-edge.
    Capped at FEINT_MAX_STREAK; short phase; costs stamina. Wrapper applies the state changes."""
    do = (cfg['FEINT_ENABLE'] and feint_streak < cfg['FEINT_MAX_STREAK']
          and rng.random() < cfg['FEINT_P'] and aggressor.stamina>0)
    if not do:
        return dict(do=False, debuff=0.0, new_streak=0, beat_cost=0.0, stamina_cost=0.0)
    feint_q = (reading(aggressor)+aggressor.skill('technique'))*TR.channel_weight(aggressor.tradition,'tempo')
    def_read = reading(defender)*TR.channel_weight(defender.tradition,'visual')*(1-0.4*mental_fat_d)
    read_feint = rng.random() < 1/(1+exp(-(def_read-feint_q)/2.0))
    debuff = -cfg['FEINT_PUNISH'] if read_feint else cfg['FEINT_DEBUFF']
    return dict(do=True, debuff=debuff, new_streak=feint_streak+1,
                beat_cost=cfg['FEINT_BEAT_COST'], stamina_cost=cfg['FEINT_STAMINA'])

def approach_displace(shorter, longer, cfg):
    """Lever-arm displacement-on-approach: a higher-leverage closer sets aside a THRUSTING longer weapon's point,
    suppressing its stop-hit and speeding the close. Returns a fraction in [0, APPROACH_DISPLACE_MAX]. Pure."""
    lever_edge = leverage(shorter,cfg) - leverage(longer,cfg)
    if longer.w['head']!='point' or lever_edge<=0: return 0.0
    rd=(reading(shorter)-reading(longer))
    return min(cfg['APPROACH_DISPLACE_MAX'], cfg['APPROACH_DISPLACE_K']*lever_edge*(1+0.1*rd))

def reopen_prob(longer, shorter, base_gap, push_avail, cfg, TR):
    """Probability the LONGER weapon regains distance given a created moment exists: reads to seize vs shorter's
    denial, executes with footwork, scaled by armour; freed-hand shove adds a path. Pure (returns a probability)."""
    id_read = reading(longer)*TR.channel_weight(longer.tradition,'visual')
    deny_read = reading(shorter)*TR.channel_weight(shorter.tradition,'visual')
    read_edge = 1/(1+exp(-(id_read-deny_read)/2.0))
    foot = footwork_eff(longer,0,cfg)/3
    p=cfg['REOPEN_K']*base_gap*foot*read_edge*cfg['REACH_W'][shorter.armor]/0.62
    if push_avail: p += cfg['PUSH_REOPEN_BONUS']*foot
    return min(cfg['REOPEN_MAX'], p)

def bind_sigma(aggressor, defender, cfg, TR):
    """One bind iteration's net sigma: LEVERAGE (technique+skill + physical lever-arm) + BLADE-GUARD catch (the
    cross/quillons/rings that catch & control the opposing blade — a guardless pole binds poorly, a long cross
    excels) + TACTILE read (Fuhlen); Strength minor. +ve favours the aggressor winning the bind. Pure."""
    lev = ((aggressor.history+aggressor.skill('bind')) - (defender.history+defender.skill('bind')))*0.06 \
          + (leverage(aggressor,cfg) - leverage(defender,cfg)) \
          * (TR.channel_weight(aggressor.tradition,'leverage')/TR.channel_weight(defender.tradition,'leverage'))
    catch = cfg['BIND_GUARD_K']*(aggressor.w['blade_guard'] - defender.w['blade_guard'])   # quillons/rings catch the blade
    tac = (reading(aggressor)*TR.channel_weight(aggressor.tradition,'tactile')*TR.familiarity(aggressor.tradition,defender.tradition)
           - reading(defender)*TR.channel_weight(defender.tradition,'tactile')*TR.familiarity(defender.tradition,aggressor.tradition))*0.04
    strq = (aggressor.strength-defender.strength)*0.0156
    return lev + catch + tac + strq
