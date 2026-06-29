"""weapon_physics.py — the GEOMETRY-AND-PHYSICS layer: derive a weapon's combat dynamics from its PRIMITIVES.

The bottom-up half of the weapon split (the other half is the weapons DICTIONARY, combatant.WEAPONS). A weapon is
NOT a bundle of hand-authored aggregates (spd, wt, closes_poorly, HEFT class, GATE caps); it is a set of PHYSICAL
PRIMITIVES and EVERY combat quantity DERIVES here, once, as documented physics. Aggregate-based emergence: behaviour
rises from the primitives, never from a per-weapon table.

PRIMITIVES consumed (per weapon, from combatant.WEAPONS):
  mass(kg), head_len, grip_len (length-units, UNIT_M m each), pommel_kg, wclass{bladed,hafted_tip,hafted_block},
  hilt{compound,simple,none}, hands, hand_guard, blade_guard, reach_adj, head, + geometry geo{cut,thrust,perc_conc}
  and the raw geometry {cross_section, strike_concentration, ...} on combatant.GEOMETRY.

DERIVED (the single basis every consumer wires to):
  STAGE 1 composite mass -> PoB, m_head, MoI, static_moment   (recovered weapon_physics 2026-06-22, self-tested 0.05cm)
  STAGE 2 PoB+mass -> percussion authority, puncture pressure, armour-defeat mode   (recovered percussion_authority)
  STAGE 3 dynamics -> agility, authority(impact), reach, the {parry,dodge,wind} defence affinities
  STAGE 4 the five categorical->continuous consumer terms (reach_term/heft_term/tempo_penalty/strdemand_term)

CALIBRATION: the composite constants are physically sourced; the engine-scale K_* gains are [SIM-CALIBRATE] —
fit in the re-baseline (REARCHITECTURE_v1 Phase 3), not asserted. This module is BUILD-ONLY until Phase 3 wires
its outputs into the consumers; today nothing live reads STAGE 3/4 (the engine still uses the hand tables).
"""
import math

# ── composite-mass constants (sourced; recovered weapon_physics_calibration_2026-06-22) ──
UNIT_M = 0.30            # length-unit -> m   (length-validated: rapier 1.14m, spear 2.01m)
RHO_WOOD = 700.0        # kg/m^3 ash/oak
RHO_IRON = 7860.0       # kg/m^3
D_HAFT = 0.040          # m haft diameter (staff back-solve)
D_GRIP = 0.030          # m sword grip
RHO_SWORD_GRIP = 900.0  # kg/m^3 wood scales + thin tang
GUARD = {'compound': 0.30, 'simple': 0.12, 'none': 0.0}   # hilt mass at the cross (kg)
POLEAXE_BUTT = 0.22     # rear queue/spike counterweight (kg)
C_HEAD = {'bladed': 0.45, 'hafted_tip': 0.97, 'hafted_block': 0.88}  # head-mass centroid frac of head_len
_A_HAFT = math.pi * (D_HAFT / 2) ** 2
_A_GRIP = math.pi * (D_GRIP / 2) ** 2

# ── percussion authority (recovered percussion_authority.py) ──
PERC_SCALE = 9.5
PERC_EXP = 0.30
PERC_CAP = 8.0
HEAVY_BLUNT_THRESHOLD = 6.0

# ── engine-scale mapping gains — [SIM-CALIBRATE] starting values, fit in the Phase-3 re-baseline ──
K_REACH = 2.05; K_HEFT = 5.2; K_TEMPO = 1.5; K_STRD = 0.55
MOI_AGILITY_K = 6.0     # agility = 1/(1+MOI_AGILITY_K*MoI); scales physical MoI (kg.m^2) into a useful 0..1 spread


# ════════════════════ STAGE 1 — composite mass -> balance & inertia ════════════════════
def derive(w):
    """Composite iron-on-wood mass model -> {PoB, m_head, MoI, static_moment, ...}. PoB is DERIVED, not hand-set.
    Pure; consumes the primitive set {mass, head_len, grip_len, pommel_kg, wclass, hilt}."""
    hl, gl = w['head_len'], w['grip_len']
    m, cls = w['mass'], w.get('wclass', 'bladed')
    Lg, Lh = gl * UNIT_M, hl * UNIT_M
    Lt = Lg + Lh
    ch = C_HEAD[cls]
    if cls == 'bladed':
        m_grip = _A_GRIP * Lg * RHO_SWORD_GRIP
        m_pom = w.get('pommel_kg', 0.0)
        m_g = GUARD.get(w.get('hilt', 'none'), 0.0)
        m_head = m - m_grip - m_pom - m_g
        moment = m_head * (ch * Lh) - m_grip * (Lg / 2) - m_pom * Lg
        moi = m_head * (ch * Lh) ** 2 + m_grip * (Lg / 2) ** 2 + m_pom * (Lg ** 2)
    else:
        m_shaft = min(_A_HAFT * Lt * RHO_WOOD, m)
        butt = POLEAXE_BUTT if w.get('is_poleaxe') else 0.0
        m_iron = max(0.0, m - m_shaft - butt)
        shaft_c = (Lt / 2) - Lg
        moment = m_iron * (ch * Lh) + m_shaft * shaft_c - butt * Lg
        moi = m_iron * (ch * Lh) ** 2 + m_shaft * (shaft_c ** 2 + Lt ** 2 / 12) + butt * (Lg ** 2)
        m_head = m_iron
    PoB = moment / m
    return dict(PoB_m=PoB, PoB_cm=PoB * 100, PoB_frac=PoB / Lt, m_head=m_head,
                MoI=moi, static_moment=m * PoB, fwd_extent_m=Lh, length_m=Lt)


# ════════════════════ STAGE 2 — percussion / puncture authority ════════════════════
def percussion_authority(w):
    """Blunt swing authority from mass + balance (the L's cancel: p ~ sqrt(mass)*pob_frac). Saturating; 0 for a
    non-blunt head. Reproduces the validated anchors mace=8, poleaxe=8, staff=4."""
    if w['head'] != 'blunt':
        return 0.0
    pob = derive(w)['PoB_frac']
    return min(PERC_CAP, PERC_SCALE * (math.sqrt(max(0.0, w['mass'])) * pob) ** PERC_EXP)


def puncture_pressure(w):
    """Concentrated-blunt pierce: same authority delivered through a beak/pick (strike_concentration) -> pressure
    that defeats plate; a broad face -> 0 (concussion, not puncture)."""
    sc = w.get('geo', {}).get('strike_concentration', w.get('strike_concentration', 0.0))
    return percussion_authority(w) * sc


def armour_defeat_mode(w):
    """Route the armour-defeat path by head shape (the physics the live single blunt row flattens)."""
    head = w['head']
    if head == 'blunt':
        sc = w.get('geo', {}).get('perc_conc', 0.0)
        return 'puncture' if sc >= 0.75 else 'concussion'
    if head in ('point', 'cut_thrust'):
        return 'gap-thrust'
    return 'cut'


# ════════════════════ STAGE 3 — dynamics: agility, authority, reach, defence affinities ════════════════════
def agility(w):
    """Speed/handiness: a high-MoI weapon is slow to bring to bear. In (0,1]; light hand-balanced ~1."""
    return 1.0 / (1.0 + MOI_AGILITY_K * derive(w)['MoI'])


def authority(w):
    """Impact authority (cut/thrust/blunt): forward momentum sqrt(mass)*forwardness. Head-specific delivery stays
    in core.coupling; this is the raw force the heft term reads."""
    pob = derive(w)['PoB_frac']
    return (w['mass'] ** 0.5) * (0.30 + pob)


def reach(w):
    """Effective forward reach + 2H extension (replaces reach=='long' + HEAD_REACH[head])."""
    return w['head_len'] + (0.8 if w['hands'] == 2 else 0.0) + w.get('reach_adj', 0.0)


def defense_affinities(w):
    """The {parry, dodge, wind} affinities the hand GATE table encodes — DERIVED from geometry + dynamics.
    wind: meet+dominate the bind — blade-catching guard x rigidity x bind-leverage x edge-length.
    dodge: void with footwork — lightness (agility) x one-handedness.
    parry: deflect safely — a guarded hand commits the parry; a handy weapon parries fast."""
    d = derive(w)
    cross_section = w.get('geo', {}).get('cross_section', w.get('cross_section', 0.6))
    rigidity = 0.30 + 0.70 * cross_section
    ag = agility(w)
    lever_norm = d['MoI'] / (1.0 / MOI_AGILITY_K + d['MoI'])      # bind-leverage in (0,1): heavy/forward dominates
    onehand = 1.0 if w['hands'] == 1 else 0.78
    wind = w.get('blade_guard', 0.4) * rigidity * (0.45 + 0.55 * lever_norm) * (0.7 + 0.3 * min(1.0, w['head_len'] / 3.0))
    dodge = ag * onehand
    parry = (0.45 + 0.55 * w.get('hand_guard', 0.4)) * (0.55 + 0.45 * min(1.0, ag / 0.6))

    def _band(x, lo, hi):                                         # into the old GATE's ~[0.4,1.0] band
        return round(0.4 + 0.6 * max(0.0, min(1.0, (x - lo) / (hi - lo))), 2)
    return dict(parry=_band(parry, 0.55, 1.0), dodge=_band(dodge, 0.2, 0.95), wind=_band(wind, 0.05, 0.45))


# ════════════════════ STAGE 4 — the five categorical->continuous consumer terms (Phase-3 wiring) ════════════════════
def reach_term(w, cfg):
    return cfg['L0'] + K_REACH * (derive(w)['fwd_extent_m']) + cfg['HANDS2'] * (w['hands'] == 2) + w.get('reach_adj', 0.0)


def heft_term(w):
    return max(0.0, min(4.0, K_HEFT * derive(w)['MoI']))


def tempo_penalty(w):
    return K_TEMPO * derive(w)['MoI']


def strdemand_term(w):
    return K_STRD * derive(w)['static_moment']


if __name__ == '__main__':
    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    from combatant import WEAPONS

    print("STAGE 1 — composite PoB vs the (retiring) hand-set pob_frac [does the iron-on-wood model reproduce it?]:")
    print(f"{'weapon':12} {'PoB_cm':>7} {'PoB_frac':>9} {'hand_pob':>9} {'dpob':>6} {'MoI':>7} {'m_head':>7}")
    worst = 0.0
    for n, w in WEAPONS.items():
        d = derive(w); hp = w.get('pob_frac', 0.0); dd = abs(d['PoB_frac'] - hp); worst = max(worst, dd)
        print(f"  {n:10} {d['PoB_cm']:7.1f} {d['PoB_frac']:9.3f} {hp:9.3f} {dd:6.3f} {d['MoI']:7.3f} {d['m_head']:7.3f}")
    print(f"  max |PoB_frac - hand pob_frac| = {worst:.3f}\n")

    print("STAGE 2/3 — derived authority/agility/reach + percussion + defence affinities:")
    print(f"{'weapon':12} {'auth':>5} {'agil':>5} {'reach':>6} {'perc':>5} {'mode':>10} {'parry/dodge/wind':>18}")
    for n, w in WEAPONS.items():
        a = defense_affinities(w)
        print(f"  {n:10} {authority(w):5.2f} {agility(w):5.2f} {reach(w):6.2f} {percussion_authority(w):5.2f} "
              f"{armour_defeat_mode(w):>10}   {a['parry']:.2f}/{a['dodge']:.2f}/{a['wind']:.2f}")
