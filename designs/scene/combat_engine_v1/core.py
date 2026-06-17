"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Wraps canonical r1/r8/m1 so every subsystem resolves identically. No A/B knowledge here."""
import sys; sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/v32')
from math import tanh
import r1_sigma_resolution as r1, r8_parity_harness as r8, m1_dice_sigma_core as m1
from math import sqrt as _sqrt

DECISIVE_OB = r8.DECISIVE_OB
TN = r8.TN_STANDARD

def resolution_pool(history): return r8.resolution_pool(history)
def effective_ob(pool, net_sigma): return r1.effective_ob(DECISIVE_OB, pool, net_sigma)
def roll_net(pool, rng): return r8.roll_net_continuous(pool, TN, rng=rng)
def degree(net, ob):
    d = r1.degree_of_success(net, ob)
    return 'fail' if d=='failure' else d

def resolve(pool, net_sigma, rng):
    """Canonical mu-shift resolution (sigma_leverage_handoff §1): base Ob fixed at DECISIVE_OB; the sigma-leverage
    boosts the ROLL (boost = eff_sigma*sigma_N = soft_cap(net_sigma)*sigma_n(pool)), it does NOT shift the Ob.
    r1.effective_ob is display-only per its own docstring; resolving via the floored Ob-shift distorted the degree
    bands (overwhelming trivialised by the Ob-floor). Returns (deg, net)."""
    net = roll_net(pool, rng) + m1.soft_cap(net_sigma) * m1.sigma_n(pool)
    return degree(net, DECISIVE_OB), net

def p_auth(w):
    """Derived percussion authority: min(8, 9.5*(sqrt(mass)*pob_frac)**0.30). Replaces the hand-set per-weapon
    'percussion'; pob_frac & mass were dead weapon inputs and this is their consumer (combat_residuals_pob_f5 §2).
    Read only in core's blunt branch, so non-blunt heads are unaffected (their hand-set percussion was dead data)."""
    return min(8.0, 9.5 * (_sqrt(max(0.0, w.get('mass', 1.0))) * w.get('pob_frac', 0.15)) ** 0.30)

# ---- damage (D1: Impact x Coupling x Quality), armour mitigation by head-mode x armour-type ----
HEFT={'light':4,'heavy':6}
QUAL={'partial':0.6,'graze':0.35,'success':1.0,'overwhelming':1.5}
RESIST={'none':{'blunt':0,'point':0,'cut':0},
        'light':{'blunt':.10,'point':.18,'cut':.60},
        'medium':{'blunt':.20,'point':.45,'cut':.80},
        'heavy':{'blunt':.30,'point':.70,'cut':.95}}
DELIVERY={'blunt':1.6,'point':1.45,'cut':1.35}
def _mode_transmit(mode, armor, close, gap, perc=8):
    """Transmit fraction for a single resolved mode (blunt/point/cut) vs an armour state. Blunt scales with PERCUSSION
    authority (a wooden staff transmits little through plate; a steel hammer transmits fully)."""
    if mode=='point':
        if armor in ('medium','heavy'):
            gap_transmit = (cfg_gap_a(armor) + cfg_gap_b(armor)*gap) if close else 0.12*gap
            return gap_transmit*DELIVERY['point']        # plate body dead; value is the gap-find only
        t = max(1.0-RESIST[armor]['point'], 0.5*gap if close else 0.15*gap)
        return t*DELIVERY['point']
    t = 1.0-RESIST[armor][mode]
    if mode=='blunt': t *= (perc/8.0)                    # percussion authority (perc 8 = steel-hammer reference)
    return t*DELIVERY[mode]
def coupling(head, armor, close, gap=0.65, perc=8):
    """Damage transmit. A cut-and-thrust head uses its BEST mode (cut vs half-sword point) at each armour level, so a
    defender taking more armour never flips the attacker to a suddenly-better transmit (removes the light->medium
    cliff). Pure cutters cannot half-sword and stay 'cut' (collapse vs plate). Blunt scales with percussion."""
    if head=='blunt':  return _mode_transmit('blunt', armor, close, gap, perc)
    if head=='point':  return _mode_transmit('point', armor, close, gap, perc)
    if head=='cut_thrust':
        return max(_mode_transmit('cut', armor, close, gap, perc), _mode_transmit('point', armor, close, gap, perc))
    return _mode_transmit('cut', armor, close, gap, perc)      # straight_cut, curved_cut — no mode-shift
def cfg_gap_a(armor): return {'medium':0.10,'heavy':0.06}[armor]   # baseline gap-find transmit (low)
def cfg_gap_b(armor): return {'medium':0.40,'heavy':0.40}[armor]   # precision payoff: high-gap points reach gaps
def damage(deg, weapon_wt, weapon_head, strength, armor, close, scale, cap_end, gap=0.65, perc=8):
    if deg not in ('graze','success','overwhelming'): return 0
    imp=HEFT[weapon_wt]+min(max((strength-3)//2,-1),2)
    cap=1.2*(cap_end+6)
    return int(round(QUAL[deg]*cap*tanh(imp*coupling(weapon_head,armor,close,gap,perc)*scale/cap)))

def strike(attacker, defender, deg, close, cfg):
    """Role-object damage convenience: reads weight/head/strength/gap/percussion off the ATTACKER and armour off the
    DEFENDER, returning the int damage. Single call-site for every blow so the 11-arg positional surface (the
    transposition-bug class) exists in exactly one place. Takes role objects (never raw A/B), consistent with the
    subsystem contract."""
    return damage(deg, attacker.weight, attacker.head, attacker.strength, defender.armor, close,
                  cfg['DAMAGE_SCALE'], cfg['CAP_END'], attacker.w['gap'], p_auth(attacker.w))
