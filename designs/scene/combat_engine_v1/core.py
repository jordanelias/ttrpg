"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Wraps canonical r1/r8/m1 so every subsystem resolves identically. No A/B knowledge here."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../tests/sim/v32-combat-balance'))
from math import tanh
import r1_sigma_resolution as r1, r8_parity_harness as r8, m1_dice_sigma_core as m1
from math import sqrt as _sqrt

DECISIVE_OB = r8.DECISIVE_OB
TN = r8.TN_STANDARD

def resolution_pool(history): return r8.resolution_pool(history)
def effective_ob(pool, net_sigma): return r1.effective_ob(DECISIVE_OB, pool, net_sigma)
def roll_net(pool, rng): return r8.roll_net_continuous(pool, TN, rng=rng)
def degree(net, ob):
    """Band a CONTINUOUS net into a degree, with the ER-2 continuity correction applied (params/core.md
    §Continuous Engine, commit a3d3888 — landed in canon TEXT, never propagated to engine CODE until now).
    The continuous net approximates a sum of integer per-die effects, so each integer degree threshold k is
    read at the k-0.5 boundary; without it the continuous read ran 5-9pp LOW across the whole 5-13D combat
    band (NERS R+S fail, 2026-06-23 critique). Self-contained here (NOT routed through r1.degree_of_success)
    so the DISCRETE/TTRPG path r1 serves stays exactly net>=k. [AUDIT-FIX — re-sweep Class-C calibration.]"""
    if net < 0.5: return 'fail'                                   # discrete net <= 0
    if net >= 2*ob - 0.5 and net >= 2.5: return 'overwhelming'    # discrete net >= 2*ob AND net >= 3
    if net >= ob - 0.5: return 'success'                          # discrete net >= ob
    return 'partial'                                              # discrete 1 <= net < ob

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

# ---- damage (Impact x Coupling x Quality) — CONTINUOUS transmission, NO tanh saturation ----
# Adopts the ground-up linear damage model [damage_model.py / damage_model_design, Jordan 2026-05-30,
# ratified 2026-06-17]: damage = Impact x Coupling x Quality, NO cap/tanh, so head/strength/armour drive
# damage as a live gradient (the old tanh cap saturated everything to ~the cap and flattened the gradient).
#   Impact   = strength + heft; BLUNT heft is CONTINUOUS from percussion authority P_auth (perc carries it);
#              cut/thrust heft is weight-class (continuous-mass cut-impact deferred, plan #9).
#   Coupling = DELIVERY(head) x transmit(material-resistance-per-mode) x gap(coverage) — material/mode physics.
#   Quality  = degree factor.   Constants from damage_model (emergent-calibrated so an even Success ~= 1 WI).
HEFT={'light':0,'heavy':3}                                          # [damage_model — additive weight heft]
QUAL={'graze':0.25,'partial':0.5,'success':1.0,'overwhelming':1.5}  # [damage_model QUALITY base; overwhelming = sigma-leverage tail floor]
OW_MAX=2.5; OW_Z=1.5          # [M-QUAL D-A: overwhelming quality saturates 1.5->OW_MAX by sigma-leverage severity]
DMG_SCALE=1.55                                                      # [damage_model — even Success ~= 1 WI; emergent-tunable]
HEAD_MODE={'blunt':'percussion','point':'puncture','cut_thrust':'shear','straight_cut':'shear','curved_cut':'shear','cut':'shear'}
DELIVERY={'blunt':1.6,'point':1.45,'cut_thrust':1.35,'straight_cut':1.5,'curved_cut':1.5,'cut':1.5}  # [damage_model head delivery]
RESIST={'none': {'percussion':0,  'shear':0,  'puncture':0},        # [damage_model — material resistance per mode in [0,1]]
        'cloth':{'percussion':.10,'shear':.35,'puncture':.15},
        'mail': {'percussion':.20,'shear':.80,'puncture':.45},
        'plate':{'percussion':.30,'shear':.95,'puncture':.70}}
TIER2MAT={'none':'none','light':'cloth','medium':'mail','heavy':'plate'}  # [armour_axes presets — tier->material]
COVERAGE_GAP={'full':0.15,'partial':0.5}                            # [damage_model — gap/bare-zone exposure]
def _transmit(mode, mat, coverage):
    t=1.0-RESIST[mat][mode]
    if mode=='puncture': return max(t, COVERAGE_GAP[coverage])      # thrust takes through-material OR the gap
    if mat!='none':
        g=COVERAGE_GAP[coverage]; return t*(1-g)+1.0*g             # some blows reach a bare zone
    return t
def coupling(head, armor, coverage='full'):
    """DELIVERY x transmit. cut_thrust is VERSATILE — takes the better of its edge (shear) or the half-sword thrust
    (puncture/gaps) at each armour level: a longsword half-swords vs plate instead of bouncing (restores the prior
    engine's max(cut,point) mode-shift; HEMA: you half-sword vs harness). [damage_model.coupling + cut_thrust versatility]"""
    mat=TIER2MAT[armor]
    if head=='cut_thrust':
        return max(DELIVERY['cut_thrust']*_transmit('shear',mat,coverage),
                   DELIVERY['point']*_transmit('puncture',mat,coverage))
    return DELIVERY.get(head,1.5)*_transmit(HEAD_MODE.get(head,'shear'),mat,coverage)
def damage(deg, weapon_wt, weapon_head, strength, armor, close, gap=0.65, perc=8, q=None):
    """Linear: (strength+heft) x Coupling x Quality x DMG_SCALE — no tanh/cap. perc carries P_auth; blunt heft
    continuous from it. DMG_SCALE (above) is the single damage-scaling knob; the old tanh-cap scale/cap_end
    parameters were dead under the linear model and have been removed (with the config DAMAGE_SCALE/CAP_END
    entries they read). gap retained for signature compat — still vestigial here (per-weapon gap-skill folds
    into the 2b puncture work)."""
    if deg not in ('graze','success','overwhelming'): return 0
    heft = 3.0*(perc/8.0) if weapon_head=='blunt' else HEFT.get(weapon_wt,0)
    qf = q if q is not None else QUAL[deg]
    impact = strength + heft                                      # additive force (damage_model design: Str+Heft). M-STR commit 2a2c9f78 reverted per sim v33-mstr-impact (mstr_lin stalled low-Str+heavy).
    return max(0, int(round(impact * coupling(weapon_head, armor) * qf * DMG_SCALE)))

def strike(attacker, defender, deg, close, cfg, net=None, pool=None):
    """Role-object damage convenience: reads weight/head/strength/gap/percussion off the ATTACKER and armour off the
    DEFENDER, returning the int damage. Single call-site for every blow so the 9-arg positional surface (the
    transposition-bug class) exists in exactly one place. Takes role objects (never raw A/B), consistent with the
    subsystem contract. `cfg` is retained as the engine-config handle at this single damage chokepoint — no longer
    read here now that DMG_SCALE is the lone scaling constant, but it is the wiring point should a damage knob ever
    move into config."""
    q=None
    if net is not None and deg=='overwhelming':                  # M-QUAL: sigma-leverage tail (canonical sigma_n + tanh)
        z=max(0.0,(net-2*DECISIVE_OB)/m1.sigma_n(pool))          # severity beyond the overwhelming bar (net>=6)
        q=1.5+(OW_MAX-1.5)*tanh(z/OW_Z)
    return damage(deg, attacker.weight, attacker.head, attacker.strength, defender.armor, close,
                  attacker.w['gap'], p_auth(attacker.w), q=q)
