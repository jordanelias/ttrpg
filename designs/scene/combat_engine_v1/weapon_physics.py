"""weapon_physics.py — the GEOMETRY-AND-PHYSICS layer: derive a weapon's combat dynamics from its PRIMITIVES.

The bottom-up half of the weapon split (the other half is the weapons DICTIONARY, combatant.WEAPONS). A weapon is
NOT a bundle of hand-authored aggregates (spd, wt, closes_poorly, HEFT class, GATE caps); it is a set of PHYSICAL
PRIMITIVES and EVERY combat quantity DERIVES here, once, as documented physics. Aggregate-based emergence: behaviour
rises from the primitives, never from a per-weapon table.

PRIMITIVES consumed (per weapon, from combatant.WEAPONS):
  mass(kg), head_len, grip_len (length-units, UNIT_M m each), pommel_kg, wclass{bladed,hafted_tip,hafted_block},
  hilt{compound,simple,none}, hands, hand_guard, blade_guard, reach_adj, head, + geometry geo{cut,thrust,perc_conc}
  and the raw geometry {cross_section, strike_concentration, ...} on combatant.GEOMETRY.

DERIVED (the intended single basis; wiring is PARTIAL — see WIRING STATUS):
  STAGE 1 composite mass -> PoB, m_head, MoI, static_moment   (recovered weapon_physics 2026-06-22, self-tested 0.05cm)
  STAGE 2 PoB+mass -> percussion authority, puncture pressure, armour-defeat mode   (recovered percussion_authority)
  STAGE 3 dynamics -> agility, authority(impact), reach, the {parry,dodge,wind} defence affinities

WIRING STATUS (2026-06-30, Gate-1 audit — SUPERSEDES the prior "BUILD-ONLY; nothing live reads STAGE 3/4" claim,
which is now FALSE):
  · LIVE consumers (read by systems.py / core via Phase-3 wiring): derive(), agility(), defense_affinities(),
    percussion_authority(), puncture_pressure(), at_grip(), grip_choke_max().
  · NOT YET WIRED — the live engine derives these in PARALLEL elsewhere (the open single-source debt): reach()
    [live path = systems.reach_base], authority() and armour_defeat_mode() [diagnostic-only]. Consolidating the
    parallel derivations onto this module is the deferred single-source RE-BASELINE (Gate-1 finding; it changes
    balance numbers, so it is Jordan-gated — the percussion-authority split core.p_auth vs WP.percussion_authority,
    which read DIFFERENT inputs (hand-set pob_frac vs derived PoB_frac), is the sharpest case).
  · The STAGE-4 consumer-term helpers (reach_term/heft_term/tempo_penalty/strdemand_term) were DELETED 2026-06-30 —
    a dead alternative-wiring the live systems.* derivations (reach_base/wield_heft) superseded.

CALIBRATION: the composite constants are physically sourced; the engine-scale K_* gains are [SIM-CALIBRATE] —
fit in the re-baseline (REARCHITECTURE_v1 Phase 3), not asserted.
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
C_HEAD = {'bladed': 0.45, 'hafted_tip': 0.97, 'hafted_block': 0.88}  # head-mass centroid frac of head_len
_A_HAFT = math.pi * (D_HAFT / 2) ** 2
_A_GRIP = math.pi * (D_GRIP / 2) ** 2

# ── percussion authority (recovered percussion_authority.py) ──
PERC_SCALE = 9.5
PERC_EXP = 0.30
PERC_CAP = 8.0
HEAVY_BLUNT_THRESHOLD = 6.0

# ── concussion energy-credit (2H grip + arc/haft-length) — GROUNDED biomechanics ──
# designs/audit/2026-06-30-combat-grounding/grounded_weapon_armour_usemode_model.md §1 (task wpwi3b9qf,
# adversarially fact-checked). A two-handed grip raises the EFFECTIVE MASS behind the blow (not tip speed), and a
# longer haft adds a little more but saturates (you lose ω as ~I^-0.28). The credit multiplies INSIDE the
# (sqrt(mass)*PoB_frac)**PERC_EXP authority term, so it compounds at the authority exponent, not linearly.
PERC_2H_HANDS = 0.25    # GROUNDED: measured 2H/1H force ratio ~=1.25 (Oh et al. 2022 within-subject crossover, S1;
                        #   corroborated IASTM compact-tool 1.24-1.28). So 1 + PERC_2H_HANDS = R_F = 1.25 per extra hand.
PERC_2H_ARC = 0.04      # [SIM-CALIBRATE band 0.02-0.06]: bat-MOI rate penalty / haft-length swing-weight gain
                        #   (Nathan 2003 constant-power regime, S1; capped at the Cross-Nathan swing-weight optimum).
PERC_GRIP_1H = 0.7      # the 1H reference grip_len (= the mace's grip_len): the arc credit accrues only for haft
                        #   LONGER than a one-handed grip. GROUNDED as the 1H anchor (the mace is the 1H percussor).

def energy_credit(w):
    """The 2H/arc energy multiplier on percussion authority (grounded §1). (1 + A_HANDS*(hands-1)) for the extra
    hand's effective-mass credit, times (1 + B_ARC*max(0, grip_len - 1H_ref)) for the saturating haft-length gain.
    A 1H weapon at the reference grip credits 1.0 (no change). Pure; consumes only {hands, grip_len}."""
    return (1.0 + PERC_2H_HANDS * (w['hands'] - 1)) * (1.0 + PERC_2H_ARC * max(0.0, w['grip_len'] - PERC_GRIP_1H))

# ── engine-scale mapping gains — [SIM-CALIBRATE] starting values, fit in the Phase-3 re-baseline ──
MOI_AGILITY_K = 6.0     # LIVE [SIM-CALIBRATE]: the bind-leverage normaliser in defense_affinities.wind (reaches the
                        # engine via systems.mode_sigma's 'wind' cap). The agility POWER LAW below replaced this
                        # rational form FOR AGILITY only; this constant is still load-bearing here — NOT dead.
                        # (The dead STAGE-4 gains K_REACH/K_HEFT/K_TEMPO/K_STRD were removed with STAGE-4, 2026-06-30.)
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
        a_haft = math.pi * (w.get('haft_d', D_HAFT) / 2) ** 2    # per-weapon shaft cross-section: a spear shaft (~35mm) is thinner than the staff/poleaxe-calibrated D_HAFT (40mm)
        m_shaft = min(a_haft * Lt * RHO_WOOD, m)
        butt = w.get('butt_kg', 0.0)            # rear queue/spike counterweight (kg); generalises the retired is_poleaxe flag — ANY rear-weighted haft counterweights for free
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
    """Blunt swing authority from mass + balance (the L's cancel: p ~ sqrt(mass)*pob_frac), times the GROUNDED 2H/arc
    energy_credit (§1) folded INSIDE the authority term. Saturating; 0 for a non-blunt head (an edge/point delivers
    no percussion — the edge-no-percuss caveat is THIS gate, emergent). Grounded anchors (2026-06-30 re-baseline,
    credited): mace 7.45 > poleaxe 5.83 > staff 2.52 — the poleaxe sits BELOW the mace in pure concussion (correct:
    its plate primacy is the beak/spike puncture mode, NOT concussion — see puncture_pressure + systems.select_mode)."""
    if w['head'] != 'blunt':
        return 0.0
    pob = derive(w)['PoB_frac']
    return min(PERC_CAP, PERC_SCALE * (math.sqrt(max(0.0, w['mass'])) * pob * energy_credit(w)) ** PERC_EXP)


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


# ════════════════════ STAGE 3b — GRIP-POSITION: continuous hand-slide (retires the choke/normal/lunge strings) ════════════════════
# Grip is MORPHOLOGY, not a named state. Where the working hand sits on the shaft is a CONTINUOUS choice, bounded by
# the weapon's own geometry: a long shaft/grip slides (butt<->centre), a short hilt cannot. "Choke" = grip-position
# toward the centre, EMERGENT from grip_len — never a category. reach / MoI / close-capability / recovery all derive
# from g. (Grounded: the parallel-axis re-pivot. [FIAT]: the GRIP_* bounds, calibrated to the old CHOKE_GRIP_MIN.)
GRIP_SHORT = 1.0        # [FIAT, = old CHOKE_GRIP_MIN] grip_len at/below which the hand cannot gather forward (short hilt)
GRIP_LONG = 3.0         # [FIAT] grip_len at which the full gather range is available
GRIP_MIN_WORKING = 0.30 # [FIAT] m of weapon kept ahead of the working hand (you must still have a weapon out front)

def _gather_len(w):
    """Grippable length along the weapon, in metres — how far a hand can travel along it. A TIPPED pole's forward
    shaft is itself grippable (you regrip up the haft toward balance — the spear gathering to a short staff); a
    block-headed club or a hilted weapon offers only its grip (you cannot grip up a mace's head). Name-free: wclass
    selects which length primitives are grippable."""
    L = w['grip_len'] + (w['head_len'] if w.get('wclass') == 'hafted_tip' else 0.0)
    return L * UNIT_M

def grip_travel_max(w):
    """Forward hand-slide available, in metres = the grippable length less the minimum weapon kept out front."""
    return max(0.0, _gather_len(w) - GRIP_MIN_WORKING)

def grip_choke_max(w):
    """Regrip freedom in [0,1], DERIVED from the grippable length: a short hilt or a block-headed club -> 0 (cannot
    gather in), a long shaft -> 1. EMERGENT from morphology — never a weapon name or a 'can_choke' flag."""
    Lu = _gather_len(w) / UNIT_M
    return max(0.0, min(1.0, (Lu - GRIP_SHORT) / (GRIP_LONG - GRIP_SHORT)))

def at_grip(w, g):
    """Re-derive the working-pivot dynamics at grip-position g ∈ [0,1] (0 = held as issued; 1 = gathered to the
    working BALANCE — the hand slides forward toward the CoM, stopping AT it, since the CoM is the inertia minimum;
    you gather for control, you do not slide past it). The lunge/extension (reach side) is a BODY term handled in
    recoverability, not a hand-slide. EXACT parallel-axis off the LEAD-HAND axis (the axis derive() already uses).
    Returns {I_g, S_g, d_g, u}. GROUNDED (parallel-axis theorem); the gather REACH is morphology-bounded ([FIAT] GRIP_*).
    A POLE regrips up the whole haft toward balance (the spear gathers to a short staff); a HILT slides within its
    grip only, gated by grip_len (a short hilt cannot gather — its half-sword form, not a slide, is its mid-blade grip)."""
    d = derive(w)
    m, PoB, I0 = w['mass'], d['PoB_m'], d['MoI']
    I_cm = max(0.0, I0 - m * PoB ** 2)                          # back out CoM inertia (same axis => valid, >=0)
    u_max = grip_choke_max(w) * max(0.0, min(PoB, grip_travel_max(w)))   # gather TOWARD the CoM, gated by regrip freedom; never past the inertia minimum
    u = max(0.0, min(1.0, g)) * u_max                          # forward hand-slide (m)
    d_g = PoB - u                                              # CoM-to-working-hand distance after the slide
    return dict(I_g=I_cm + m * d_g ** 2,                       # MINIMUM (= I_cm) when u reaches the CoM
                S_g=m * abs(d_g), d_g=d_g, u=u)


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
