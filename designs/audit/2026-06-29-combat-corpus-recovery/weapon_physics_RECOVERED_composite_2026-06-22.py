"""
weapon_physics.py — primitive-derived weapon dynamics for combat_engine_v1.
PRELIMINARY / CALIBRATED (2026-06-22). Replaces the categorical `reach`/`wt` labels
(systems.reach_base/weapon_tempo/act_cost/str_demand, core.HEFT) with quantities
derived bottom-up from physical primitives and validated against sourced specimen PoB.

PRIMITIVES (per weapon): mass(kg), head_len, grip_len (engine length-units),
  pommel_kg (NEW — back-solved from sourced PoB; the primitive {mass,hl,gl} lacked),
  wclass in {bladed,hafted_tip,hafted_block}, hilt in {compound,simple,none}.
CONSTANTS are physically motivated; [SIM-CALIBRATE] marks the engine-scale mapping
gains that the proposal §9 re-baseline (mirror=50, tier spread, no-one-shot) must fit.
"""
import math

UNIT_M = 0.30            # length-unit -> m   [length-validated: rapier 1.14m, spear 2.01m]
RHO_WOOD = 700.0         # kg/m^3 ash/oak     [sourced §6]
RHO_IRON = 7860.0        # kg/m^3             [sourced §6]
D_HAFT = 0.040           # m haft diameter    [staff back-solve]
D_GRIP = 0.030           # m sword grip       [typical]
RHO_SWORD_GRIP = 900.0   # kg/m^3 wood scales + thin tang
GUARD = {'compound': 0.30, 'simple': 0.12, 'none': 0.0}   # hilt mass at cross (kg)
POLEAXE_BUTT = 0.22      # rear queue/spike counterweight (kg)
C_HEAD = {'bladed': 0.45, 'hafted_tip': 0.97, 'hafted_block': 0.88}  # head-mass centroid frac of head_len
_A_HAFT = math.pi*(D_HAFT/2)**2
_A_GRIP = math.pi*(D_GRIP/2)**2

# engine-scale mapping gains — [SIM-CALIBRATE] starting values, fit in re-baseline
K_REACH = 2.05           # reach contribution per metre of forward extent
K_HEFT  = 5.2            # non-blunt heft per unit MoI (caps at ~4)
K_TEMPO = 1.5            # tempo penalty per unit MoI
K_STRD  = 0.55           # str-demand per kg of static moment proxy

def derive(w):
    """w: dict with mass, head_len, grip_len, pommel_kg, wclass, hilt.
    Returns physical {PoB_m, m_head, MoI, static_moment, fwd_extent_m, length_m}."""
    hl, gl = w['head_len'], w['grip_len']
    m, cls = w['mass'], w['wclass']
    Lg, Lh = gl*UNIT_M, hl*UNIT_M
    Lt = Lg + Lh
    ch = C_HEAD[cls]
    if cls == 'bladed':
        m_grip = _A_GRIP*Lg*RHO_SWORD_GRIP
        m_pom = w.get('pommel_kg', 0.0)
        m_g = GUARD.get(w.get('hilt', 'none'), 0.0)
        m_head = m - m_grip - m_pom - m_g
        moment = m_head*(ch*Lh) - m_grip*(Lg/2) - m_pom*Lg
        moi = m_head*(ch*Lh)**2 + m_grip*(Lg/2)**2 + m_pom*(Lg**2)
    else:
        m_shaft = min(_A_HAFT*Lt*RHO_WOOD, m)
        m_iron = m - m_shaft
        butt = POLEAXE_BUTT if w.get('is_poleaxe') else 0.0
        m_iron = max(0.0, m_iron - butt)
        shaft_c = (Lt/2) - Lg
        moment = m_iron*(ch*Lh) + m_shaft*shaft_c - butt*Lg
        moi = m_iron*(ch*Lh)**2 + m_shaft*(shaft_c**2 + Lt**2/12) + butt*(Lg**2)
        m_head = m_iron
    PoB = moment/m
    return dict(PoB_m=PoB, PoB_cm=PoB*100, PoB_frac=PoB/Lt, m_head=m_head,
                MoI=moi, static_moment=m*PoB, fwd_extent_m=Lh, length_m=Lt)

# --- engine-scale replacements for the five categorical consumer sites ---
def reach_term(w, cfg):                       # replaces L0 + LONG*(reach=='long') + HEADR*HEAD_REACH[head]
    d = derive(w)
    return cfg['L0'] + K_REACH*d['fwd_extent_m'] + cfg['HANDS2']*(w['hands'] == 2) + w.get('reach_adj', 0.0)

def heft_term(w):                             # replaces HEFT={'light':0,'heavy':3} for non-blunt
    return max(0.0, min(4.0, K_HEFT*derive(w)['MoI']))

def tempo_penalty(w, cfg):                    # replaces WEIGHT_PEN*(wt=='heavy')
    return K_TEMPO*derive(w)['MoI']

def strdemand_term(w):                        # replaces D_WT*(wt=='heavy')
    return K_STRD*derive(w)['static_moment']

if __name__ == '__main__':
    import json
    cal = json.load(open('/home/claude/cb/weapon_calibrated_final.json'))
    POM = cal['pommel_kg']
    W = {
     'rapier':(3.2,0.6,1.3,'bladed','compound',1),'arming':(2.4,0.8,1.2,'bladed','simple',1),
     'longsword':(2.8,1.6,1.4,'bladed','simple',2),'greatsword':(3.6,1.8,2.7,'bladed','simple',2),
     'sabre':(2.6,0.7,0.9,'bladed','simple',1),'dagger':(0.7,0.4,0.3,'bladed','none',1),
     'paired_short':(1.4,0.5,0.7,'bladed','none',1),'longsword_halfsword':(1.4,2.6,1.4,'bladed','simple',2),
     'spear':(5.5,1.2,2.0,'hafted_tip','none',2),'staff':(2.8,2.8,1.5,'hafted_tip','none',2),
     'poleaxe':(2.2,2.2,2.5,'hafted_tip','none',2),'mace':(1.8,0.7,1.2,'hafted_block','none',1)}
    print(f"{'weapon':20s}{'PoB_cm':>7s}{'expect':>7s}{'dPoB':>6s}{'MoI':>6s}  SELFTEST")
    worst=0
    for n,(hl,gl,m,cls,hilt,H) in W.items():
        w=dict(head_len=hl,grip_len=gl,mass=m,wclass=cls,hilt=hilt,hands=H,
                pommel_kg=POM.get(n,0.0),is_poleaxe=(n=='poleaxe'))
        d=derive(w); exp=cal['derived'][n]['PoB_cm']; dd=abs(d['PoB_cm']-exp); worst=max(worst,dd)
        print(f"{n:20s}{d['PoB_cm']:7.1f}{exp:7.1f}{dd:6.2f}{d['MoI']:6.2f}")
    print(f"\nmax PoB deviation from calibration: {worst:.3f} cm  -> {'PASS' if worst<0.5 else 'FAIL'}")
