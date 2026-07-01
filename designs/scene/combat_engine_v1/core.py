"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Wraps canonical r1/r8/m1 so every subsystem resolves identically. No A/B knowledge here."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../tests/sim/v32-combat-balance'))
sys.path.insert(0, os.path.dirname(__file__))
from math import tanh
import r1_sigma_resolution as r1, r8_parity_harness as r8, m1_dice_sigma_core as m1
import weapon_physics as WP   # Phase-3 consolidation: percussion authority lives ONCE in WP (the credited derived value);
                              # core.strike reads WP.percussion_authority (the sigma path systems.adef_cap already does),
                              # retiring the duplicate core.p_auth that read the hand-set pob_frac. WP imports only math
                              # at module scope (cycle-free), so this import is safe.

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

# ---- damage (Impact x Coupling x Quality) — CONTINUOUS transmission, NO tanh saturation ----
# Adopts the ground-up linear damage model [damage_model.py / damage_model_design, Jordan 2026-05-30,
# ratified 2026-06-17]: damage = Impact x Coupling x Quality, NO cap/tanh, so head/strength/armour drive
# damage as a live gradient (the old tanh cap saturated everything to ~the cap and flattened the gradient).
#   Impact   = strength + heft; BLUNT heft is CONTINUOUS from percussion authority P_auth (perc carries it);
#              cut/thrust heft is weight-class (continuous-mass cut-impact deferred, plan #9).
#   Coupling = DELIVERY(head) x transmit(material-resistance-per-mode) x gap(coverage) — material/mode physics.
#   Quality  = degree factor.   Constants from damage_model (emergent-calibrated so an even Success ~= 1 WI).
HEFT={'light':0,'heavy':3}                                          # [damage_model — additive weight heft] (binary anchor)
HEFT_HEAVY=3.0                                                      # heavy-class cut/thrust heft (= HEFT['heavy'])
HEFT_REF_LIGHT=1.0; HEFT_REF_HEAVY=1.4                              # kg class-reference masses (longsword = heavy anchor)
def heft_resp(w, cfg):
    """WS-2 req4 — continuous weapon heft response (heft-units). The binary `wt` CLASS is the anchor (it encodes
    wieldiness/blade-presence, NOT raw kg — spear 2.0kg is 'light', mace 1.2kg 'heavy'), so cross-class balance is
    preserved; a WITHIN-CLASS mass term then makes a 2.7kg greatsword read heavier than a 1.4kg longsword at every
    heft site. HEFT_MODE='binary' returns exactly {heavy:1.0, light:0.0} — byte-identical to the pre-WS-2 booleans.
    One calibrated gain (HEFT_MASS_K), per the recovered WP-2 recommendation (not the MoI/pommel machinery)."""
    heavy = (w.get('wt') == 'heavy')
    if cfg.get('HEFT_MODE', 'binary') == 'binary':
        return 1.0 if heavy else 0.0
    base = 1.0 if heavy else 0.0
    ref = HEFT_REF_HEAVY if heavy else HEFT_REF_LIGHT
    return max(0.0, base + cfg.get('HEFT_MASS_K', 0.0) * (w.get('mass', ref) - ref))
QUAL={'graze':0.25,'partial':0.5,'success':1.0,'overwhelming':1.5}  # [damage_model QUALITY base; overwhelming = sigma-leverage tail floor]
OW_MAX=2.5; OW_Z=1.5          # [M-QUAL D-A: overwhelming quality saturates 1.5->OW_MAX by sigma-leverage severity]
DMG_SCALE=1.55                                                      # [damage_model — even Success ~= 1 WI; emergent-tunable]
HEAD_MODE={'blunt':'percussion','point':'puncture','cut_thrust':'shear','straight_cut':'shear','curved_cut':'shear','cut':'shear'}
DELIVERY={'blunt':1.6,'point':1.45,'cut_thrust':1.35,'straight_cut':1.5,'curved_cut':1.5,'cut':1.5}  # [damage_model head delivery]
# Material resistance per mode in [0,1] (resist; transmit = 1-resist). GROUNDED 2026-06-30 (Alan Williams, The Knight
# and the Blast Furnace, 2003) — designs/audit/2026-06-30-combat-grounding/. CHANGED 4 cells: cloth.shear .35->.45
# (a 16-30 layer jack sheds a ~60-130 J cut); cloth.puncture .15->.12 (a point stops at only ~50 J vs ~80 J cut — the
# documented cut>>point asymmetry); cloth.percussion .10->.12 (modest standalone blunt absorption); mail.shear .80->.85
# (cutting riveted mail is "functionally impossible," >130 J ceiling). Plate row + mail perc/punc KEEP (well-pinned).
# [CI — DESIGNER-SET/UNSOURCED: the cloth fractions are a designer normalisation of Williams' joules onto the 0-1 scale,
#  NOT a Williams figure.]  [PACKAGE: plate.percussion .30 is honest ONLY with the FIX-1b authority gate below — never
#  tune one without the other (ungated, an honest plate-vs-blunt resist is ~.55-.65).]  Assumes RIVETED mail + HARDENED
# ~2mm plate (butted mail / wrought iron are far weaker — not modelled).
RESIST={'none': {'percussion':0,   'shear':0,   'puncture':0},
        'cloth':{'percussion':.12, 'shear':.45, 'puncture':.12},
        'mail': {'percussion':.20, 'shear':.85, 'puncture':.45},
        'plate':{'percussion':.30, 'shear':.95, 'puncture':.70}}
TIER2MAT={'none':'none','light':'cloth','medium':'mail','heavy':'plate'}  # [armour_axes presets — tier->material]
COVERAGE_GAP={'full':0.15,'partial':0.5}                            # [damage_model — gap/bare-zone exposure]
# FIX-1b [FIAT — no melee-speed behind-plate data exists; ballistic BABT is the wrong regime, per Phase-3 grounding]:
# percussion transmitted through RIGID armour (mail/plate) scales with the blow's percussion AUTHORITY — a steel
# hammer (p_auth 8) overwhelms the armour's impact-spread; a wooden staff (p_auth ~4) is largely absorbed. The TRANSMIT
# term is LINEAR in (perc/PERC_AUTH_REF) (E=1.0, momentum-like). It COMPOUNDS with the pre-existing blunt heft
# (3·perc/8 in damage()), so the net blunt-vs-rigid damage scales ~perc² in authority — force and through-armour
# transmission are distinct physics, both authority-dependent (intended). Soft cloth absorbs by deformation
# (~authority-independent) so it is unscaled. perc=PERC_AUTH_REF = full transmission. Magnitude is FIAT. NOTE: FIX-1b
# is a damage-LETHALITY reduction only — it does NOT touch the sigma/reach/control path that drives the staff's
# vs-plate WIN-RATE (that is FIX-1's job); the staff-vs-arming heavy win-rate is ~flat under this change alone.
PERC_AUTH_REF=8.0; PERC_TRANSMIT_FLOOR=0.35
def _transmit(mode, mat, coverage, perc=PERC_AUTH_REF):
    t=1.0-RESIST[mat][mode]
    if mode=='puncture': return max(t, COVERAGE_GAP[coverage])      # thrust takes through-material OR the gap
    if mode=='percussion' and mat in ('mail','plate'):             # FIX-1b: rigid armour spreads blunt -> authority-scaled
        t*=max(PERC_TRANSMIT_FLOOR, min(1.0, perc/PERC_AUTH_REF))
    if mat!='none':
        g=COVERAGE_GAP[coverage]; return t*(1-g)+1.0*g             # some blows reach a bare zone
    return t
def coupling(head, armor, coverage='full', perc=PERC_AUTH_REF):
    """DELIVERY x transmit. cut_thrust is VERSATILE — takes the better of its edge (shear) or the half-sword thrust
    (puncture/gaps) at each armour level: a longsword half-swords vs plate instead of bouncing (restores the prior
    engine's max(cut,point) mode-shift; HEMA: you half-sword vs harness). [damage_model.coupling + cut_thrust versatility]
    `perc` (percussion authority) scales the blunt transmit vs rigid armour (FIX-1b); ignored for non-blunt heads."""
    mat=TIER2MAT[armor]
    if head=='cut_thrust':
        return max(DELIVERY['cut_thrust']*_transmit('shear',mat,coverage),
                   DELIVERY['point']*_transmit('puncture',mat,coverage))
    return DELIVERY.get(head,1.5)*_transmit(HEAD_MODE.get(head,'shear'),mat,coverage,perc)
def damage(deg, heft_units, weapon_head, strength, armor, close, gap=0.65, perc=8, q=None):
    """Linear: (strength+heft) x Coupling x Quality x DMG_SCALE — no tanh/cap. perc carries P_auth; blunt heft
    continuous from it. DMG_SCALE (above) is the single damage-scaling knob; the old tanh-cap scale/cap_end
    parameters were dead under the linear model and have been removed (with the config DAMAGE_SCALE/CAP_END
    entries they read). gap retained for signature compat — still vestigial here (per-weapon gap-skill folds
    into the 2b puncture work)."""
    if deg not in ('graze','success','overwhelming'): return 0
    heft = 3.0*(perc/8.0) if weapon_head=='blunt' else HEFT_HEAVY*heft_units   # WS-2: continuous cut/thrust heft (binary mode -> heft_units in {0,1} reproduces HEFT['light'/'heavy'])
    qf = q if q is not None else QUAL[deg]
    impact = strength + heft                                      # additive force (damage_model design: Str+Heft). M-STR commit 2a2c9f78 reverted per sim v33-mstr-impact (mstr_lin stalled low-Str+heavy).
    return max(0, int(round(impact * coupling(weapon_head, armor, perc=perc) * qf * DMG_SCALE)))   # FIX-1b: perc scales blunt transmit vs rigid armour

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
    head=getattr(attacker, 'sel_head', None) or attacker.head    # the SELECTED use-mode head (systems.select_mode, set by the wrapper); falls back to the native head
    return damage(deg, heft_resp(attacker.w, cfg), head, attacker.strength, defender.armor, close,
                  attacker.w['gap'], WP.percussion_authority(attacker.w), q=q)
