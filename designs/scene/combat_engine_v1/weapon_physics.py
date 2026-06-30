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
MOI_AGILITY_K = 6.0     # (legacy rational form; superseded by the power law below — kept until the wiring deletes it)
# agility power law (Phase-3 grounding): EXPONENT is GROUNDED (Cross & Nathan 2009 / Fleisig 2002, handle-axis,
# mass-independent, n≈0.20–0.28); the ANCHOR is [SIM-CALIBRATE] (sets where agility≈1). Replaces 1/(1+K·MoI).
AGILITY_EXP = 0.25      # grounded exponent (band 0.20–0.28)
AGILITY_REF = 0.088     # [SIM-CALIBRATE] anchor MoI (a handy arming sword) where agility≈1.0; fit in the re-baseline
# 2H reach comes from the HANDLE/rear-hand setback (HEMA measure-grammar), not hand-count — grip-proportional, not flat
K_GRIP_REACH = 0.4      # [SIM-CALIBRATE band 0.3–0.5] rear-hand setback fraction of grip_len for a 2H weapon
# [WIRING HAZARD — Phase-3b] weapon_physics.reach() spans ~0.7–6.0 (head_len-based); the LIVE systems.reach_base it
# replaces spans ~4.5–7.8 (L0=4.0-based). CLOSE_REACH_REF=6.5 + close_unwieldiness assume the 4.5–7.8 band, so wiring
# reach() in UNSCALED zeroes the long-weapon close penalty (spear 5.98 < 6.5). Wire via an affine remap, or re-tune
# CLOSE_REACH_REF/reach_adj/the gap-normalisation together in the same pass. Do NOT wire reach() raw.


# ════════════════════ STAGE 1 — composite mass -> balance & inertia ════════════════════
def derive(w):
    """Composite iron-on-wood mass model -> {PoB, m_head, MoI, static_moment, ...}. PoB is DERIVED, not hand-set.
    Pure; consumes the primitive set {mass, head_len, grip_len, pommel_kg, wclass, hilt}."""
    hl, gl = w['head_len'], w['grip_len']
    m, cls = w['mass'], w.get('wclass', 'bladed')
    Lg, Lh = gl * UNIT_M, hl * UNIT_M
    Lt = Lg + Lh
    ch = C_HEAD[cls]
    if w.get('gripped'):
        # HAND-ON-BLADE form (half-sword): the held span (grip_len) is STEEL — the gripped lower blade — NOT a
        # low-density wood grip. The standard bladed branch mis-reads grip_len as wood and yields a NON-PHYSICAL
        # negative PoB (recovered defect: longsword_halfsword derived PoB = -12.9 cm, MoI 0.184 > the full form's
        # 0.169). LUMPED model: the forward WORKING segment (head_len ahead of the forward hand) is approximated as
        # the steel fraction of the bar ahead of the hand; the pommel + rear grip are neglected in the swing inertia
        # (two-handed point work braced by the rear hand, not a free swing). The long grip behind feeds leverage
        # (systems.leverage). The forward end is light -> small +PoB and LOW swing-MoI (high close control). Build-only
        # (nothing live reads STAGE-1 derive() for the half-sword yet); the lumped approximation is calibration-grade,
        # not exact. Pure.
        m_lin = m / Lt                                  # ~uniform steel mass per unit length (you grip the blade)
        m_fwd = m_lin * Lh                              # steel forward of the working hand — loads the point
        c_fwd = ch * Lh                                 # centroid of the forward working segment ahead of the hand
        moment = m_fwd * c_fwd                          # forward moment of the light working end
        moi = m_fwd * c_fwd ** 2 + m_fwd * Lh ** 2 / 12.0   # working-segment swing inertia about the hand (low)
        m_head = m_fwd
        PoB = moment / m
        return dict(PoB_m=PoB, PoB_cm=PoB * 100, PoB_frac=PoB / Lt, m_head=m_head,
                    MoI=moi, static_moment=m * PoB, fwd_extent_m=Lh, length_m=Lt)
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
    sc = w.get('geo', {}).get('strike_concentration', 0.0)   # raw primitive, passed through by geometry.bake (geo is complete)
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
    """Speed/handiness from swing inertia. GROUNDED SHAPE — a constant-exponent POWER LAW about the grip axis:
    agility ∝ MoI^(−AGILITY_EXP), EXP≈0.25 (Cross & Nathan 2009 / Fleisig 2002 — handle-axis bat/racket/golf swing
    studies, mass-independent, exponent 0.20–0.28). Replaces the prior 1/(1+K·MoI), whose LOCAL exponent climbed
    0.1→0.9 across the roster and over-penalised heavy weapons ~2× (greatsword 0.22 vs the power-law ~0.6). Anchored
    at AGILITY_REF (a handy arming sword's MoI) where agility≈1, capped at 1.0 for lighter weapons. The exponent is
    grounded; AGILITY_REF is [SIM-CALIBRATE] (sets the spread, fit in the Phase-3 re-baseline). In (0,1].
    [FIAT/WIRING-HAZARD] Below AGILITY_REF the literature fit (Cross & Nathan, sampled MoI≈0.2–0.6) is EXTRAPOLATED
    and the min(1.0,…) CLAMP is a FIAT cap, not grounded — it collapses the whole light-weapon spread (dagger 0.002,
    arming 0.088, half-sword 0.025 all pin to 1.0), erasing the dagger>paired>sabre tempo ordering. MUST be resolved
    when agility is wired live in Phase-3b (re-anchor AGILITY_REF at/below the lightest MoI, or drop the cap and
    renormalise the consumer to (0,k]) — the power law itself is correct uncapped."""
    return min(1.0, (AGILITY_REF / max(1e-6, derive(w)['MoI'])) ** AGILITY_EXP)


def authority(w):
    """Impact authority (cut/thrust/blunt): forward momentum sqrt(mass)*forwardness. Head-specific delivery stays
    in core.coupling; this is the raw force the heft term reads."""
    pob = derive(w)['PoB_frac']
    return (w['mass'] ** 0.5) * (0.30 + pob)


def reach(w):
    """Effective forward reach (replaces the categorical reach=='long' + HEAD_REACH[head]). GROUNDED REVISION
    (HEMA measure-grammar): a two-handed weapon's extra reach comes from the HANDLE LENGTH / rear-hand setback, NOT
    from hand-count — a longsword thrusts as far as a rapier because of its longer grip, and a one-handed extension
    reaches equal-or-farther. So the prior flat `+0.8 if 2H` is replaced by K_GRIP_REACH·grip_len for 2H weapons.
    reach_adj is the per-weapon [SIM-CALIBRATE] correction (git eb5535eb tuned it to A0–A3 sim error; it is the
    dominant per-weapon term and is flagged NOT grounded). The standing arm+lunge offset lives in L0 (the consumer)."""
    twohand = K_GRIP_REACH * w['grip_len'] if w['hands'] == 2 else 0.0
    return w['head_len'] + twohand + w.get('reach_adj', 0.0)


def defense_affinities(w):
    """The {parry, dodge, wind} affinities the hand GATE table encodes — DERIVED from geometry + dynamics.
    wind: meet+dominate the bind — blade-catching guard x rigidity x bind-leverage x edge-length.
    dodge: void with footwork — lightness (agility) x one-handedness.
    parry: deflect safely — a guarded hand commits the parry; a handy weapon parries fast."""
    d = derive(w)
    cross_section = w.get('geo', {}).get('cross_section', 0.6)   # raw primitive via geometry.bake (geo is complete)
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
