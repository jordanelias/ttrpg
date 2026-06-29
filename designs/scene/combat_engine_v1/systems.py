"""Subsystem modules. Uniform contract: each is a pure function of (aggressor, defender, state, cfg[, rng]).
NO subsystem touches raw A/B — they receive Combatant objects in role. This isolates every mechanic for
unit-testing and makes the coupling explicit (the fix for the recurring inversion bugs)."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from math import exp, tanh
from config import HANDLE_RANK
import core
from combatant import WEAPONS, GEOMETRY

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
    _heft=core.heft_resp(w,cfg)   # WS-2 req4: continuous heft (binary mode -> {0,1}, byte-identical to wt=='heavy')
    pen=cfg['WEIGHT_PEN']*_heft+cfg['HANDS_COMMIT']*(w['hands']==2)*_heft
    pen=min(pen, cfg['MAX_TEMPO_PEN'])
    grip=getattr(c,'grip','normal')
    if grip=='choke':  pen += cfg['CHOKE_TEMPO_PEN']    # choked grip: a bit slower cadence (control/leverage gain elsewhere)
    elif grip=='lunge':pen += cfg['LUNGE_TEMPO_PEN']    # extended/lunge: slower to repeat (reach/commit gain elsewhere)
    t=cfg['BASE_TEMPO']+w['spd']*cfg['SPEED_K']+cfg['AGI_TEMPO_K']*(c.agi-4)-pen   # athleticism adds a LITTLE cadence (Jordan 2026-06-04); centred at agi 4 so default fighters & the mirror are unchanged
    t*=(1-cfg['TEMPO_FATIGUE_K']*fatigue)               # fatigue slows the rate of action
    t*=poise_factor(c, cfg)                            # DYNAMIC structure/balance: a kuzushi'd fighter acts slower (1.0 at full)
    return max(cfg['TEMPO_FLOOR'],t)
def close_tempo(c, cfg, fatigue=0.0):
    """Cadence IN THE CLOSE — conditional (fatigue/grip). A long two-handed pole (spear/staff) is SLOW to recover
    once a faster weapon is inside UNLESS it chokes up (grip adjustment to act in close quarters). Spread COMPRESSED
    toward the mean so action-frequency is a secondary edge, not the deciding axis (reach governs)."""
    t=weapon_tempo(c,cfg,fatigue)
    w=c.w; grip=getattr(c,'grip','normal')
    # a long pole (spear/staff: data flag `closes_poorly`) pays the closed penalty UNLESS it has choked up to fight
    # close (grip adjustment offsets it). Explicit weapon DATA, not an attribute-conjunction guess.
    if w.get('closes_poorly', False) and grip!='choke': t -= cfg['POLE_CLOSE_PENALTY']
    t=max(cfg['TEMPO_FLOOR'],t)
    return cfg['CLOSE_TEMPO_MEAN'] + (t-cfg['CLOSE_TEMPO_MEAN'])*cfg['CLOSE_TEMPO_COMPRESS']

# ---------- stamina ----------
def stamina_max(c): 
    import r8_parity_harness as r8; return r8.stamina_max(c.end,c.spirit)
def act_cost(c, commit, cfg):
    return (cfg['ACT_BASE']+cfg['ACT_WEIGHT']*core.heft_resp(c.w,cfg)+cfg['ACT_COMMIT']*commit)*cfg['COST_SCALE']   # WS-2 req4: continuous heft

# ---------- concentration (Focus+Spirit tracker) ----------
def conc_max(c, cfg):
    return cfg['CONC_FOCUS']*c.focus + cfg['CONC_SPIRIT']*c.spirit   # 3*Focus + 2*Spirit (Jordan 2026-06-04, canonical ED-902; corrects prior Cog-driven form)
def reading(c, cfg): return (2*c.cog + c.att)/3 + cfg['READ_HISTORY_K']*(c.history-3)   # cog primary, Att half, + relevant-History experience (Jordan 2026-06-03)
def reflex(c, cfg): return (cfg['REFLEX_AGI']*c.agi+cfg['REFLEX_ATT']*c.att)/(cfg['REFLEX_AGI']+cfg['REFLEX_ATT'])

# ---------- strength handling + endurance fatigue ----------
def str_demand(c, cfg):
    w=c.w; return cfg['D0']+cfg['D_LEN']*reach_base(c,cfg)+cfg['D_WT']*core.heft_resp(w,cfg)+cfg['D_HAND']*HANDLE_RANK[w['hand']]+cfg['D_2H']*(w['hands']==2)   # WS-2 req4: continuous heft
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
    """The IRRECOVERABILITY multiplier on the overcommit cost — the commitment=recovery axis made physical. To
    commit is to give up recovery; HOW MUCH depends on how hard the action is to terminate/retract: the weapon's
    static turning moment (mass*pob_frac — a forward-heavy mace 'wants to continue' and can't be stopped; a
    hand-balanced rapier retracts instantly, which is WHY a rapier can feint and a mace can't), plus footwork (a
    lunge extends the body = low recovery; a choke/gathered grip stays recoverable). 1.0 at the longsword
    reference; bounded below so it never flips sign. Pure."""
    w=c.w
    moment = w.get('mass',1.0)*w.get('pob_frac',0.15)            # static forward moment: heavy+forward = hard to stop
    mult = 1.0 + cfg['EXPOSE_MOMENT_K']*(moment - cfg['EXPOSE_MOMENT_REF'])
    grip=getattr(c,'grip','normal')
    if grip=='lunge':   mult += cfg['EXPOSE_LUNGE_K']            # extended body = committed, low recovery
    elif grip=='choke': mult -= cfg['EXPOSE_CHOKE_K']           # gathered in = more recoverable
    return max(0.3, mult)
def stance_stability(c, fat, cfg): return cfg['FOOT_STANCE_K']*(balance_eff(c,fat,cfg)-3)

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

# fail-fast: the three hand-maintained weapon dicts must stay key-synchronised (a missing GATE key -> KeyError at
# mode_sigma; a missing GEOMETRY key -> silent stale gap). Catch drift at import, not mid-fight.
assert set(GATE)>=set(WEAPONS), f"GATE missing weapons: {set(WEAPONS)-set(GATE)}"
assert set(GEOMETRY)>=set(WEAPONS), f"GEOMETRY missing weapons: {set(WEAPONS)-set(GEOMETRY)}"
def mode_sigma(mode, aggressor, defender, commit, choke, read_win, fat_d, cfg):
    """defender's δσ for a chosen defensive mode. Reading universal; +2 axis-specific. Skills bias per-axis."""
    rd=reading(defender,cfg)-reading(aggressor,cfg)
    rfx=reflex(defender,cfg); tech=defender.history+defender.skill('technique')
    ftw=balance_eff(defender,fat_d,cfg); strn=defender.strength
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
    _deep=max(0.0,min(1.0,commit-3.0))     # CONTINUOUS commit response: 0 at <=3, ramps to 1 at >=4 (no integer cliff)
    _shallow=max(0.0,min(1.0,3.0-commit))  # 0 at >=3, ramps to 1 at <=2
    if mode=='parry': sig-=0.25*_deep      # a deep commit is easier to parry (committed line); a shallow probe harder to catch
    if mode=='dodge': sig+=0.10*_deep-0.10*_shallow   # deep commit easier to void; a shallow feint harder to read for the dodge
    return (base+sig)*cap

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
HALFSWORD_FORM = {'longsword':'longsword_halfsword'}
HALFSWORD_BASE = {'longsword_halfsword':'longsword'}

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
    MODE the head actually fights in vs this armour (the cut->half-sword-thrust shift `coupling` models): a cut-and-
    thrust sword swings (easy) unarmoured but thrusts to gaps (hard) vs plate. Pure."""
    ah=aggressor.w['head']
    if ah=='point':                       legib=cfg['LEGIB_THRUST']      # always a thrust
    elif ah in ('straight_cut','curved_cut'): legib=cfg['LEGIB_SWING']   # pure cutters always swing
    elif ah=='blunt':                     legib=cfg['LEGIB_SWING']       # percussive arc, easy to read
    elif ah=='cut_thrust':
        # shifts to a controlled gap-thrust vs plate (hard to read), otherwise cuts (easy) — matches coupling's mode-shift
        legib=cfg['LEGIB_THRUST'] if opp_armor in ('medium','heavy') else cfg['LEGIB_SWING']
    else:                                 legib=1.0
    legib += cfg['LEGIB_COMMIT_K']*max(0,commit-3)
    if getattr(aggressor,'grip','normal')=='lunge': legib += cfg['LEGIB_LUNGE']
    return legib

# [UNUSED since WS-5 2026-06-28 — the feint is dissolved into the attack (wrapper no longer calls this; deception
#  is intrinsic to commit-depth + legibility + the read contest). Kept until a cleanup pass removes it + FEINT_*.]
def feint_eval(aggressor, defender, mental_fat_d, feint_streak, cfg, rng, TR):
    """Decide/resolve a feint. Pure (reads rng): returns dict {do, debuff, new_streak, beat_cost, stamina_cost}.
    A fooled defender's real-attack defence/read is degraded; a defender who READS it gains a small counter-edge.
    Capped at FEINT_MAX_STREAK; short phase; costs stamina. Wrapper applies the state changes."""
    do = (cfg['FEINT_ENABLE'] and feint_streak < cfg['FEINT_MAX_STREAK']
          and rng.random() < cfg['FEINT_P'] and aggressor.stamina>0)
    if not do:
        return dict(do=False, debuff=0.0, new_streak=0, beat_cost=0.0, stamina_cost=0.0)
    feint_q = (reading(aggressor,cfg)+aggressor.skill('technique'))*TR.eff_cw(aggressor, 'tempo')
    def_read = reading(defender,cfg)*TR.eff_cw(defender, 'visual')*TR.eff_cw(defender, 'precommit')*(1-0.4*mental_fat_d)
    read_feint = rng.random() < 1/(1+exp(-(def_read-feint_q)/2.0))
    debuff = -cfg['FEINT_PUNISH'] if read_feint else cfg['FEINT_DEBUFF']
    return dict(do=True, debuff=debuff, new_streak=feint_streak+1,
                beat_cost=cfg['FEINT_BEAT_COST'], stamina_cost=cfg['FEINT_STAMINA'])

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
