"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Wraps canonical r1/r8/m1 so every subsystem resolves identically. No A/B knowledge here."""
import sys; sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/v32')
from math import tanh
import r1_sigma_resolution as r1, r8_parity_harness as r8

DECISIVE_OB = r8.DECISIVE_OB
TN = r8.TN_STANDARD

def resolution_pool(history): return r8.resolution_pool(history)
def effective_ob(pool, net_sigma): return r1.effective_ob(DECISIVE_OB, pool, net_sigma)
def roll_net(pool, rng): return r8.roll_net_continuous(pool, TN, rng=rng)
def degree(net, ob):
    d = r1.degree_of_success(net, ob)
    return 'fail' if d=='failure' else d

# ---- damage (D1: Impact x Coupling x Quality), armour mitigation by head-mode x armour-type ----
HEFT={'light':4,'heavy':6}
QUAL={'partial':0.6,'graze':0.35,'success':1.0,'overwhelming':1.5}
RESIST={'none':{'blunt':0,'point':0,'cut':0},
        'light':{'blunt':.10,'point':.15,'cut':.35},
        'medium':{'blunt':.20,'point':.45,'cut':.80},
        'heavy':{'blunt':.30,'point':.70,'cut':.95}}
DELIVERY={'blunt':1.6,'point':1.45,'cut':1.35}
def head_mode(head, armor='none'):
    if head=='blunt': return 'blunt'
    if head=='point': return 'point'
    # MODE-SHIFT (reference): cut-and-thrust swords half-sword/rondel-thrust to gaps in armour -> fight as 'point';
    # pure cutters (straight_cut, curved_cut) CANNOT mode-shift and stay 'cut' (collapse vs plate).
    if head=='cut_thrust':
        return 'point' if armor in ('medium','heavy') else 'cut'
    return 'cut'   # straight_cut, curved_cut — no mode-shift
def _mode_transmit(mode, armor, close, gap):
    """Transmit fraction for a single resolved mode (blunt/point/cut) vs an armour state."""
    if mode=='point':
        if armor in ('medium','heavy'):
            gap_transmit = (cfg_gap_a(armor) + cfg_gap_b(armor)*gap) if close else 0.12*gap
            return gap_transmit*DELIVERY['point']        # plate body dead; value is the gap-find only
        t = max(1.0-RESIST[armor]['point'], 0.5*gap if close else 0.15*gap)
        return t*DELIVERY['point']
    t = 1.0-RESIST[armor][mode]
    return t*DELIVERY[mode]
def coupling(head, armor, close, gap=0.65):
    """Damage transmit. A cut-and-thrust head uses its BEST mode (cut vs half-sword point) at each armour level, so a
    defender taking more armour never flips the attacker to a suddenly-better transmit (removes the light->medium
    cliff). Pure cutters cannot half-sword and stay 'cut' (collapse vs plate)."""
    if head=='blunt':  return _mode_transmit('blunt', armor, close, gap)
    if head=='point':  return _mode_transmit('point', armor, close, gap)
    if head=='cut_thrust':
        return max(_mode_transmit('cut', armor, close, gap), _mode_transmit('point', armor, close, gap))
    return _mode_transmit('cut', armor, close, gap)      # straight_cut, curved_cut — no mode-shift
def cfg_gap_a(armor): return {'medium':0.10,'heavy':0.06}[armor]   # baseline gap-find transmit (low)
def cfg_gap_b(armor): return {'medium':0.40,'heavy':0.40}[armor]   # precision payoff: high-gap points reach gaps
def damage(deg, weapon_wt, weapon_head, strength, armor, close, scale, cap_end, gap=0.65):
    if deg not in ('graze','success','overwhelming'): return 0
    imp=HEFT[weapon_wt]+min(max((strength-3)//2,-1),2)
    cap=1.2*(cap_end+6)
    return int(round(QUAL[deg]*cap*tanh(imp*coupling(weapon_head,armor,close,gap)*scale/cap)))
