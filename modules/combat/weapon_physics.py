"""weapon_physics.py — the GEOMETRY-AND-PHYSICS layer: derive a weapon's combat dynamics from its PRIMITIVES.

The bottom-up half of the weapon split (the other half is the weapons DICTIONARY, combatant.WEAPONS). A weapon is
NOT a bundle of hand-authored aggregates (spd, wt, closes_poorly, HEFT class, GATE caps); it is a set of PHYSICAL
PRIMITIVES and EVERY combat quantity DERIVES here, once, as documented physics. Aggregate-based emergence: behaviour
rises from the primitives, never from a per-weapon table.

PRIMITIVES consumed (per weapon: a weapons.WEAPONS record, whose schema is weapons.py's header):
  mass(kg), head_len, grip_len (METRES — U0 units honesty, ED-PC-0002), wclass{bladed,hafted_tip,hafted_block},
  hilt{compound,simple,none}, hands, head, the located parts elements/guards/haft/pommel/butt, adornments, and the fields
  weapons.py bakes onto the record: geo{cut,thrust,perc_conc,cross_section,strike_concentration,...}, hand_guard,
  blade_guard, _derived.

DERIVED (the intended single basis; wiring is PARTIAL — see WIRING STATUS):
  STAGE 1 composite mass -> PoB, m_head, MoI, static_moment   (recovered weapon_physics 2026-06-22, self-tested 0.05cm)
  STAGE 2 PoB+mass -> percussion authority, puncture pressure, armour-defeat mode   (recovered percussion_authority)
  STAGE 3 dynamics -> agility, the {parry,dodge,wind} defence affinities

WIRING STATUS:
  · LIVE consumers (read by systems.py / core): derive(), agility(), defense_affinities(),
    percussion_authority(), puncture_pressure(), at_grip(), grip_choke_max().
  · DIAGNOSTIC-ONLY (called by no resolution code): armour_defeat_mode().
  percussion_authority lives ONCE in this module, read by core.strike. Reach and heft are derived by the live
  systems.* derivations (reach_base/wield_heft).

CALIBRATION: the composite constants are physically sourced; the engine-scale K_* gains are [SIM-CALIBRATE] —
fit in the re-baseline, not asserted.
"""
import math

from engine.dice_engine.fmath import ltr_sum
from . import vocabulary as V  # the engine's token ALPHABET, owned once (ED-PC-0042). A zero-import leaf, so this
                         # module -- which CANNOT import core (core imports IT: `import weapon_physics as WP`) -- still reaches the
                         # same head/mode/hilt tokens core's tables are keyed by, with no cycle.


# A float sum here goes through `fmath.ltr_sum`, the one accumulation rule (its docstring says why: CR-01).
# ── composite-mass constants (sourced; recovered weapon_physics_calibration_2026-06-22) ──
# head_len/grip_len/the GRIP_*/LEVER_*/PERC_GRIP_1H/REC_GRIP_REF/GRAB_SHORT_REACH thresholds are all HONEST
# METRES (ED-PC-0002).
RHO_WOOD = 700.0        # kg/m^3 ash/oak
D_HAFT = 0.040          # m haft diameter (staff back-solve)
D_GRIP = 0.030          # m sword grip
RHO_SWORD_GRIP = 900.0  # kg/m^3 wood scales + thin tang
GUARD = {V.HILT_COMPOUND: 0.30, V.HILT_SIMPLE: 0.12, V.HILT_NONE: 0.0}   # hilt mass at the cross (kg)
C_HEAD = {'bladed': 0.45, 'hafted_tip': 0.97, 'hafted_block': 0.88}  # head-mass centroid frac of head_len
_A_GRIP = math.pi * (D_GRIP / 2) ** 2

# ── percussion authority (recovered percussion_authority.py) ──
PERC_SCALE = 9.5
PERC_EXP = 0.30
PERC_CAP = 8.0          # the "steel-hammer reference" ceiling = the top of the canonical 0-8 percussion-authority
                        # scale (recovered percussion_authority.py:61). SINGLE OWNER of that anchor (ED-PC-0042
                        # rider I1b). This one is the PRIMITIVE (the clamp that CREATES the
                        # scale); core.PERC_AUTH_REF, core.damage()'s blunt `perc/8.0` + its `perc=8` default, and
                        # config.CFG['ADEF_PERC_REF'] are DENOMINATORS normalising an authority value against the
                        # scale top, so they must move WITH it. The two core sites bind from here; the CFG seed
                        # cannot (config.py is a zero-import leaf and CFG is per-run overridable — see the note
                        # there) and is held equal by
                        # tests/valoria/test_combat_invariants.py::test_percussion_anchor_has_one_owner.
                        # A re-fit of PERC_SCALE/PERC_EXP (see percussion_authority's docstring) changes the
                        # scale here, once.
# Armour-defeat is continuous: core.adef_cap scales percussion_authority against ADEF_PERC_REF.

# ── concussion energy-credit (2H grip + arc/haft-length) — GROUNDED biomechanics ──
# designs/audit/2026-06-30-combat-grounding/grounded_weapon_armour_usemode_model.md §1 (task wpwi3b9qf,
# adversarially fact-checked). A two-handed grip raises the EFFECTIVE MASS behind the blow (not tip speed), and a
# longer haft adds a little more but saturates (you lose ω as ~I^-0.28). The credit multiplies INSIDE the
# (sqrt(mass)*PoB_frac)**PERC_EXP authority term, so it compounds at the authority exponent, not linearly.
PERC_2H_HANDS = 0.25    # GROUNDED: measured 2H/1H force ratio ~=1.25 (Oh et al. 2022 within-subject crossover, S1;
                        #   corroborated IASTM compact-tool 1.24-1.28). So 1 + PERC_2H_HANDS = R_F = 1.25 per extra hand.
PERC_2H_ARC = 0.04 / 0.30   # [SIM-CALIBRATE band 0.02-0.06 per old length-unit = 0.0667-0.20 per METRE]: bat-MOI
                        #   rate penalty / haft-length swing-weight gain (Nathan 2003 constant-power regime, S1;
                        #   capped at the Cross-Nathan swing-weight optimum). Rescaled /0.30 at U0 (grip_len is
                        #   now metres) — same physical gain, honest unit.
PERC_GRIP_1H = 0.21     # m — the 1H reference grip_len (= the mace's grip_len): the arc credit accrues only for
                        #   haft LONGER than a one-handed grip. GROUNDED as the 1H anchor (the mace is the 1H percussor).

def energy_credit(w):
    """The 2H/arc energy multiplier on percussion authority (grounded §1). (1 + A_HANDS*(hands-1)) for the extra
    hand's effective-mass credit, times (1 + B_ARC*max(0, grip_len - 1H_ref)) for the saturating haft-length gain.
    A 1H weapon at the reference grip credits 1.0 (no change). Pure; consumes only {hands, grip_len}."""
    return (1.0 + PERC_2H_HANDS * (w['hands'] - 1)) * (1.0 + PERC_2H_ARC * max(0.0, w['grip_len'] - PERC_GRIP_1H))

# ── engine-scale mapping gains — [SIM-CALIBRATE] starting values, fit in the Phase-3 re-baseline ──
MOI_AGILITY_K = 6.0     # LIVE [SIM-CALIBRATE]: the bind-leverage normaliser in defense_affinities.wind (reaches the
                        # engine via systems.mode_sigma's 'wind' cap).
# agility power law: EXPONENT is GROUNDED (Cross & Nathan 2009 / Fleisig 2002, handle-axis,
# mass-independent, n≈0.20–0.28); the ANCHOR is [SIM-CALIBRATE] (sets where agility≈1).
AGILITY_EXP = 0.25      # grounded exponent (band 0.20–0.28)
# [SIM-CALIBRATE] anchor MoI: set JUST BELOW the lightest weapon's swing inertia (~0.9× the dagger's MoI 0.0024) so
# AGILITY_REF/MoI ≤ 1 for the WHOLE roster — nothing pins to the min(1.0) cap, which is an inert safety guard (an
# anchor above the light weapons' MoI would flat-top them all to agility 1.0 and ERASE the emergent light-weapon
# dodge/parry ordering). Agility ∈ (0,1] emerges strictly from MoI (dagger highest → spear lowest). The dodge/parry
# _band spread (renormalised below to the compressed range) is calibrated against this anchor.
AGILITY_REF = 0.00215
# Reach comes from systems.reach_base (grip-aware); this module has no reach function.


# ════════════════════ STAGE 1 — located-part mass model -> balance & inertia ════════════════════
# A weapon's balance/inertia is the SUM over LOCATED PARTS about the working-hand
# axis — moment=Σ mᵢ·xᵢ, MoI=Σ mᵢ·(xᵢ² + extentᵢ²/12), m_total=Σ mᵢ, PoB=moment/m_total. Every physical part
# (head elements, guards, haft/grip, pommel, butt) is a
# named located mass in the roster record (w['elements']/['guards']/['haft']/['pommel']/['butt']), sourced from
# specimen/typology physical facts, not a formula split by
# weapon-class centroid. A compound head's mass is the sum of its located elements, not one point at wclass's
# centroid — the bec de corbin's hammer/beak/spike each carry their own measured mass and position. The
# single-C_HEAD-centroid fallback path is LIVE ONLY for a record with no explicit `elements` (a synthetic record;
# none in the roster).
def _head_elements(w):
    """Phase-A fallback: no explicit `elements` → one synthetic element at the old C_HEAD centroid (pos_frac)
    carrying the whole head-mass residual (mass_share 1.0). Not exercised by any current roster weapon."""
    els = w.get('elements')
    if els:
        return els
    return [dict(pos_frac=C_HEAD[w.get('wclass', 'bladed')], mass_share=1.0)]

def _all_parts(w):
    """The weapon's full located-mass part list: head elements + guards + haft/grip + pommel + butt,
    each as (mass_kg, x_m, extent_m) about the working-hand axis (x=0, +toward tip, −toward butt — the SAME
    axis convention the specimen data was collected under). A guard flagged `dual_role_element` is also a head element (e.g.
    the hook_sword's crescent, which both catches AND strikes) — its mass is carried by the element entry only,
    so it is excluded here to avoid double-counting. Empty when the record carries no explicit parts (the
    single-element fallback below covers that case). Pure."""
    parts = []
    for e in w.get('elements', ()):
        parts.append((e['mass_kg'], e['x_m'], e.get('extent_m', 0.0)))
    for g in w.get('guards', ()):
        if not g.get('dual_role_element'):
            parts.append((g['mass_kg'], g['x_m'], g.get('extent_m', 0.0)))
    haft = w.get('haft')
    if haft:
        parts.append((haft['mass_kg'], haft['x_m'], haft.get('extent_m', 0.0)))
    pommel = w.get('pommel')
    if pommel:
        parts.append((pommel['mass_kg'], pommel['x_m'], 0.0))
    butt = w.get('butt')
    if butt:
        parts.append((butt['mass_kg'], butt['x_m'], 0.0))
    return parts

def derive(w):
    """Located-part mass model -> {PoB, m_head, MoI, static_moment, ...}. PoB DERIVED. Pure. Roster weapons
    carry a part list (elements/guards/haft/pommel/butt); derive() is a positional sum over it —
    no per-weapon-class formula. Records without explicit parts fall back to the C_HEAD-centroid
    reproduction (not exercised by the live roster). Roster records carry a bake-once
    '_derived' cache (weapons.py import loop) — mutation after bake is out of contract, same as the baked
    geo/gap; synthetic dicts without the key compute fresh."""
    cached = w.get('_derived')
    if cached is not None:
        return cached
    Lh, Lg = w['head_len'], w['grip_len']   # metres (U0 units honesty — no unit conversion)
    Lt = Lh + Lg
    parts = _all_parts(w)
    if parts:
        m_total = ltr_sum(p[0] for p in parts)
        moment = ltr_sum(p[0] * p[1] for p in parts)
        moi = ltr_sum(p[0] * (p[1] ** 2 + p[2] ** 2 / 12.0) for p in parts)
        PoB = moment / m_total
        m_head = ltr_sum(e['mass_kg'] for e in w.get('elements', ()))
        return dict(PoB_m=PoB, PoB_cm=PoB * 100, PoB_frac=PoB / Lt, m_head=m_head,
                    MoI=moi, static_moment=moment, fwd_extent_m=Lh, length_m=Lt)
    # ── fallback (not exercised by the live roster) ──
    m, cls = w['mass'], w.get('wclass', 'bladed')
    if w.get('gripped'):
        # HAND-ON-BLADE (half-sword) lumped-rod special case for a synthetic record; the
        # live roster's half-sword forms (longsword_halfsword/estoc_halfsword) carry a shifted-origin part list
        # instead, which gives the same physics without the uniform-rod approximation.
        ch = C_HEAD[cls]
        m_lin = m / Lt
        m_fwd = m_lin * Lh
        c_fwd = ch * Lh
        moment = m_fwd * c_fwd
        moi = m_fwd * c_fwd ** 2 + m_fwd * Lh ** 2 / 12.0
        PoB = moment / m
        return dict(PoB_m=PoB, PoB_cm=PoB * 100, PoB_frac=PoB / Lt, m_head=m_fwd,
                    MoI=moi, static_moment=m * PoB, fwd_extent_m=Lh, length_m=Lt)
    fparts = []  # (mass, x_from_working_hand, rod_length)
    if cls == 'bladed':
        m_grip = _A_GRIP * Lg * RHO_SWORD_GRIP
        m_pom = w.get('pommel_kg', 0.0)
        m_g = GUARD.get(w.get('hilt', V.HILT_NONE), 0.0)
        head_mass = m - m_grip - m_pom - m_g
        fparts.append((m_grip, -Lg / 2, 0.0))
        fparts.append((m_pom, -Lg, 0.0))
        fparts.append((m_g, 0.0, 0.0))
    else:
        a_haft = math.pi * (w.get('haft_d', D_HAFT) / 2) ** 2
        m_shaft = min(a_haft * Lt * RHO_WOOD, m)
        butt = w.get('butt_kg', 0.0)
        head_mass = max(0.0, m - m_shaft - butt)
        fparts.append((m_shaft, (Lt / 2) - Lg, Lt))
        fparts.append((butt, -Lg, 0.0))
    m_head = 0.0
    for e in _head_elements(w):
        me = e['mass_share'] * head_mass
        fparts.append((me, e['pos_frac'] * Lh, e.get('rod_L', 0.0)))
        m_head += me
    m_total = ltr_sum(p[0] for p in fparts)
    moment = ltr_sum(p[0] * p[1] for p in fparts)
    moi = ltr_sum(p[0] * (p[1] ** 2 + p[2] ** 2 / 12.0) for p in fparts)
    PoB = moment / m_total
    return dict(PoB_m=PoB, PoB_cm=PoB * 100, PoB_frac=PoB / Lt, m_head=m_head,
                MoI=moi, static_moment=moment, fwd_extent_m=Lh, length_m=Lt)


# ════════════════════ STAGE 2 — percussion / puncture authority ════════════════════
# ── circumstance degradation (I2, D2/D2b) — mode-split, thrust-protected, floored, NaN-guarded Phi_grip; a
# SEPARATE floored Phi_room for percussion only (Phi_room is CUT from the heft path — JD-1(d), R-8: a monotone
# heft-room multiply violates C4).
SWING_FLOOR = 0.5      # [SIM-CALIBRATE] floor on the swing-fraction degradation (a fully-gathered swing never drops below half its open-measure authority)
# phi_grip('point') is grip-INVARIANT UNCONDITIONALLY (no constant; the D2 grip-invariant-thrust gate, phi>=0.9 at
# full gather): a rigid shaft transmits axial compression independent of hand position, so choking up a pole does
# NOT reduce the force of an axial thrust. What choking up costs is CONTROL (a shortened rear lever lets the point
# be beaten off-line, and the gathered posture telegraphs): a legibility/accuracy effect whose home is
# systems.choke_counterbalance -> CHOKE_ACCURACY_K (U5/ED-PC-0019, U10/ED-PC-0022).
PERC_ROOM_FLOOR = 0.5  # [SIM-CALIBRATE] floor on percussion's room degradation (identity at room=1.0/r*; monotone-down FORBIDDEN, C4)

def grip_swing_ratio(w, grip):
    """rho(g) = S_g(g)/S_g(0), the swing-moment retention at grip g relative to open measure. NaN-GUARDED: rho:=1.0
    when S_g(0)<=eps (a centre-balanced staff, S_g near-zero at every grip — closes the biomech BLOCKER-class NaN
    finding, D2). rho(0)==1.0 always, by construction. Pure."""
    S0 = at_circumstance(w, 0.0)['S_g']
    if S0 <= 1e-9:
        return 1.0
    return at_circumstance(w, grip)['S_g'] / S0

def phi_grip(w, grip, sel_head, sel_pc=None):
    """The circumstance-degraded impact multiplier (D2) — mode-split on the SELECTED element's strike mode, never a
    whole-weapon point_concentration blend (R-3: whole-weapon pc bands overlap in the wrong order, e.g. bear_spear
    pc=0.55 < greatsword pc=0.62). A `point`-headed strike is grip-INVARIANT (Phi_thrust==1.0 — axial thrust mass
    is delivered independent of hand position on a rigid shaft, `[ASSERTED — rigid-body first principles]`).
    Every OTHER head (cut_thrust/straight_cut/curved_cut/cut/blunt) degrades its swing fraction by a FLOORED
    S_g-ratio (Phi_swing, SWING_FLOOR `[SIM-CALIBRATE]`), THEN blends by the SELECTED element's OWN
    point_concentration (`sel_pc`, sourced from c.sel_pc — D2b/I2; None falls back to the native whole-weapon
    point_concentration): Phi_grip = pc_sel*1.0 + (1-pc_sel)*Phi_swing — the within-mode thrust-ness a pure cutter
    still carries (guandao pc=0.30) as well as a genuinely versatile cut_thrust blade (JD-8: spetum
    retains its swing degradation weighted by its own low pc). At grip=0, rho(0)==1.0 always, so Phi_swing==1.0
    and the blend collapses to 1.0 for EVERY head. Pure."""
    if sel_head == V.HEAD_POINT:
        return 1.0   # D2 gate: an axial point thrust's TRANSMISSION is grip-invariant — a rigid shaft carries axial compression from the hands to the point independent of WHERE on the shaft it is gripped (`[ASSERTED — rigid-body transmission only]`). The force is human-GENERATED (choking up shortens the rear body-lever available to drive the thrust), a real grip-dependent cost (ED-PC-0026). That cost is not zero; it is booked ELSEWHERE as a CONTROL/authority cost — systems.choke_counterbalance -> CHOKE_ACCURACY_K (the legibility/control channel) and thrust_authority(head_len) (the gap-press lever) — NOT as a phi_grip force term. So this 1.0 is the transmission invariant, not a claim of zero total cost.
    rho = grip_swing_ratio(w, grip)
    phi_swing = SWING_FLOOR + (1.0 - SWING_FLOOR) * rho
    pc = sel_pc if sel_pc is not None else w['geo']['point_concentration']   # whole-weapon fallback off the BAKED surface (geometry.bake passes the raw primitives through so `geo` is the single read path — ED-PC-0042/I3)
    return pc * 1.0 + (1.0 - pc) * phi_swing

def phi_room_percussion(room):
    """Percussion's room degradation (D2b) — floored, monotone-increasing to the room=1.0 (r*) identity peak; a
    monotone-DOWN shape is FORBIDDEN (C4: force-vs-distance is non-monotone, no lever collapses linearly/
    quadratically with lost room). Stays on the percussion path only (unlike heft — Phi_room is CUT there,
    JD-1(d)); reaches the armour-defeat sigma path via adef_cap/puncture_pressure/reach_threat, so it is not
    cosmetic. `[SIM-CALIBRATE]`. Pure."""
    r = max(0.0, min(1.0, room))
    return PERC_ROOM_FLOOR + (1.0 - PERC_ROOM_FLOOR) * r

def hilt_assembly_mass(w):
    """The guard+pommel+integral-grip-material mass — the part that becomes the striking HEAD when a bladed
    weapon is reversed (Mordhau/Mordschlag: HEMA sources describe both hands moving onto the blade near the
    ricasso/tip, with the guard+pommel assembly projecting out as an improvised mace head — see
    reversed_grip_percussion's docstring for sourcing). Pure sum over the weapon's own located parts, no name
    check. 0.0 for a weapon with no guard/pommel/haft record (e.g. a synthetic test dict)."""
    guard_m = ltr_sum(g['mass_kg'] for g in w.get('guards', ()) if not g.get('dual_role_element'))
    pommel_m = w.get('pommel', {}).get('mass_kg', 0.0)
    haft_m = w.get('haft', {}).get('mass_kg', 0.0)
    return guard_m + pommel_m + haft_m


REVERSED_GRIP_EFFICIENCY = 0.25   # [FIAT, HEMA-grounded direction, ED-PC-0009, 2026-07-08] no treatise or
                    #   biomechanical study gives a precise force reading for a Mordhau/reversed-grip strike, but
                    #   every source consulted agrees on the QUALITATIVE magnitude: a documented, historically-
                    #   attested supplementary technique used specifically because the edge/point had failed
                    #   against armour, NOT the wielder's preferred or most powerful option — explicitly weaker
                    #   than a dedicated mace/warhammer, "far less injurious" against rigid plate (retains real
                    #   concussive threat against mail/padding/an exposed head). 0.25 is a deliberately
                    #   conservative discount on the raw located-part percussion_element_authority computation
                    #   (which, unmodified, would put every two-handed sword's hilt assembly within ~15-30% of a
                    #   dedicated mace/poleaxe's OWN authority — physically defensible on raw mass alone, but
                    #   contradicting the "clearly secondary, far less injurious" historical framing every source
                    #   agreed on). [SIM-CALIBRATE]: open to playtesting: percussion_authority's own PERC_EXP=0.30
                    #   power-law cannot express "structurally weak" from input magnitude alone (verified: even a
                    #   pommel-only mass at a near-zero lever arm still saturates toward ~2-3/8 before this
                    #   discount, because a fractional exponent compresses ANY nonzero input toward the upper
                    #   band) — this explicit multiplier is the honest alternative to either leaving Mordhau
                    #   mace-strength (wrong, JD-4's original finding) or hand-fudging PERC_SCALE/PERC_EXP
                    #   themselves (which would distort every dedicated blunt weapon's own calibration).

def reversed_grip_percussion(w, grip=0.0, room=1.0):
    """A bladed, two-handed weapon's Mordhau/Mordschlag percussion option — the pommel/crossguard strike used
    (per Liechtenauer-tradition half-swording; Wikipedia "Mordhau (weaponry)"; Malevus "Mordhau: The Murder
    Stroke Technique") when cuts and thrusts fail against rigid armour: both hands move onto the blade and the
    guard+pommel assembly, now projecting outward, is swung like an improvised mace. GROUNDED SHAPE: reuses
    percussion_element_authority's existing per-element form — the SAME physics already applied to a lucerne_
    hammer's rear fluke or a bec_de_corbin's beak (a located mass at its own position, not a whole-weapon
    lump) — with hilt_assembly_mass(w) as the striking mass and the weapon's own grip_len as the lever arm (the
    guard+pommel's natural reach beyond a rear hand choked up near the crossguard, per the HEMA grip
    description: "one hand towards the tip...the other towards the crossguard"). Then applies
    REVERSED_GRIP_EFFICIENCY (see its own docstring) so the result reads as the documented supplementary,
    clearly-weaker-than-dedicated-blunt-weapons option rather than mace-parity. Restricted to hands==2 bladed
    weapons — HEMA's Mordhau is attested for longswords/greatswords/two-handers with enough spare blade length
    to grip past; a one-handed sword or dagger has no comparable technique in the sourced material. 0.0
    otherwise, or if the weapon carries no guard/pommel mass at all. `grip`/`room` pass through to
    percussion_element_authority's own Phi_grip/Phi_room degradation (D2b) — room (how much space there is to
    swing) applies exactly as it would to a dedicated blunt strike; grip (the PRIMARY blade's own choke state)
    is threaded too since percussion_element_authority already reads it uniformly, though its physical bearing
    on an already-reversed grip is a secondary effect at most. Pure."""
    if w.get('wclass') != 'bladed' or w.get('hands') != 2:
        return 0.0
    hilt_m = hilt_assembly_mass(w)
    if hilt_m <= 1e-9:
        return 0.0
    return percussion_element_authority(w, hilt_m, w['grip_len'], grip=grip, room=room) * REVERSED_GRIP_EFFICIENCY


# ════════ THE SHARED STRIKE-POINT LEVER (ED-PC-0047, E2a — SINGLE OWNER, consumed by E2b) ════════
STRIKE_HAND_LEVER = 0.12   # m — the SHORTEST lever any weapon-delivered blow can have: a strike landed AT the
                    #   working-hand axis (x=0) is still delivered by the hand/hilt assembly projecting about one
                    #   hand-breadth (0.10-0.12 m, anthropometric hand breadth incl. the fist's grip diameter) past
                    #   the grip axis, swung on the arm. GROUNDED as a geometric floor, not a fitted constant: it
                    #   exists so a striking element MOUNTED at the hand (a hook_sword's guard crescent, a pommel,
                    #   a hand-guard punch) derives a real lever instead of zero. [SIM-CALIBRATE] magnitude.

def delivered_strike(w):
    """(m_strike, x_strike, m_total) — the located mass on the STRIKING side of the working hand and its centroid.

    THE PHYSICAL POINT (ED-PC-0047 / M1): mass BEHIND the hands is counterweight you carry, not authority you
    cancel. `derive()['PoB_frac']` is the centre of balance of the WHOLE weapon about the hand, so a rear butt-cap
    or a symmetric haft SUBTRACTS from it — and a centre-gripped staff cancels to exactly 0.0 regardless of mass,
    which is the defect this function exists to remove. Only the forward (x>0) mass is delivered into the blow;
    the rear mass is neutral, never negative.

    Distributed parts (`extent_m`, e.g. a staff's haft lumped at its centroid with a 1.68 m extent) are split
    UNIFORMLY at the hand, so the forward half of a centre-gripped haft counts with its own centroid — the
    physical picture that a centre-gripped staff strikes with a tip half the haft away from the leading hand.
    Reads the same located-part list as `derive()` (`_all_parts`), so the two cannot disagree about the weapon.

    FALLBACK (no located parts — a synthetic dict; not exercised by the weapon roster, every member of which
    carries a part list): the whole mass, at the derived balance point, clamped forward. Pure."""
    m_f = 0.0
    s_f = 0.0
    m_total = 0.0
    for (m, x, extent) in _all_parts(w):
        m_total += m
        if extent <= 1e-12:
            if x > 0.0:
                m_f += m
                s_f += m * x
            continue
        lo, hi = x - extent / 2.0, x + extent / 2.0
        if hi <= 0.0:
            continue          # wholly behind the hand — counterweight, contributes nothing (never negative)
        if lo >= 0.0:
            m_f += m
            s_f += m * x
            continue
        m_fwd = m * (hi / extent)              # uniform-density split at the hand
        m_f += m_fwd
        s_f += m_fwd * (hi / 2.0)              # centroid of the forward portion
    if m_total <= 1e-12:                       # no located parts: Phase-A fallback
        d = derive(w)
        return max(0.0, w.get('mass', 0.0)), max(0.0, d['PoB_m']), max(1e-12, w.get('mass', 0.0))
    if m_f <= 1e-12:
        return 0.0, 0.0, m_total
    return m_f, s_f / m_f, m_total


def strike_point_lever(w, m_strike, x_strike):
    """**THE strike-point lever — the SINGLE OWNER of the percussion lever form, shared by E2a and E2b.**

        lambda(m, x) = m * (STRIKE_HAND_LEVER + |x|) / (m_total * (STRIKE_HAND_LEVER + Lt))

    Read it as: **the fraction of the weapon's MAXIMUM swing moment that this strike delivers** — the maximum
    being the whole weapon's mass presented at its own tip, which is why `lambda(m_total, Lt) == 1.0` exactly.
    It generalises `derive()['PoB_frac']`: `lambda(m_total, PoB_m)` at a zero hand-floor IS `PoB_frac` for every
    weapon whose balance point sits at or ahead of the hand: the SAME quantity re-pointed from "the whole mass at
    the centre of balance" to "the delivered mass at the strike point".
    [ED-PC-0048] It is not a STRICT generalisation: `lambda` takes `|x|`, so the three roster weapons whose PoB sits
    BEHIND the hand (estoc_halfsword, longsword_halfsword, cinquedea) map to the POSITIVE lever rather than the
    negative `PoB_frac`. No behaviour depends on it — all three are non-blunt heads, so they route to
    `reversed_grip_percussion` and never reach this line.

    TWO scales share it, because they are the same defect (a lever that can be exactly 0):
      · E2a (M1): PoB_frac is a CoM offset, so a rear counterweight cancels it — staff 0.0. Fixed by measuring
        the moment of the DELIVERED mass (`delivered_strike`), which no counterweight can cancel.
      · E2b (M9, ED-PC-0048): `percussion_element_authority`'s `|x| / Lt` zeroed any element mounted at x=0.
        Fixed by STRIKE_HAND_LEVER: a blow landed at the hand still swings on the hand/hilt's own lever. It routes
        through THIS function, as `sqrt(elem_mass) * strike_point_lever(w, delivered_strike(w)[2], elem_x)`.
        ⚠ **NOTE THE FIRST ARGUMENT.** This function divides its mass argument by the weapon's total, so passing
        `elem_mass` puts mass in at power 1.5 (dropping percussion 19-37% on every weapon). The element's own mass
        belongs in `sqrt()`; the lever is geometric, which is exactly what this function returns when handed the
        delivered mass (R-11.4).
      · NOT `|x| / Lt` and NOT `PoB_frac`. If a third lever form ever appears in this module, one of them is wrong.

    Symmetric in the sign of x (a rear-facing fluke swings on |x| like any other located element). Monotone
    non-decreasing in both arguments. In [0, 1] for any strike the weapon can actually present. Pure."""
    Lt = derive(w)['length_m']
    if Lt <= 1e-12:
        return 0.0
    m_total = delivered_strike(w)[2]
    if m_total <= 1e-12:
        return 0.0
    return (max(0.0, m_strike) * (STRIKE_HAND_LEVER + abs(x_strike))) / (m_total * (STRIKE_HAND_LEVER + Lt))


def percussion_authority(w, grip=0.0, room=1.0, sel_head=None, sel_pc=None):
    """Blunt swing authority from the DELIVERED mass and its STRIKE-POINT LEVER (p ~ sqrt(m_strike)*lambda),
    times the GROUNDED 2H/arc energy_credit (§1) folded INSIDE the authority term. Saturating.
    [ED-PC-0047, E2a] The lever is `strike_point_lever` (see that function — the single owner E2b consumes too)
    against `delivered_strike`'s forward mass, not `derive()['PoB_frac']` (the whole weapon's centre of balance about
    the hand, which a rear counterweight would SUBTRACT from and which is exactly 0 for a centre-gripped haft): the
    staff derives a real perc_auth / puncture / adef_cap / percussion_stagger.
    NON-BLUNT HEADS (U2/ED-PC-0008/0009): a non-blunt head routes to reversed_grip_percussion(w) (see its own
    docstring), the historically-grounded Mordhau/pommel-strike option, correctly weak (roughly 1.4-1.8 on this 0-8
    scale for a two-handed sword vs a dedicated mace's 8.0/poleaxe's ~7.5; a whole-weapon-formula reuse would put
    swords at mace-parity, ED-PC-0008). 0.0 for a one-handed/short bladed weapon or a hafted weapon whose native
    head genuinely isn't blunt (no comparable technique is attested in the sourced material).
    [ED-PC-0047] HONEST LIMIT: the blunt-native family reads mace = poleaxe = goedendag at PERC_CAP > lucerne > bec >
    staff (5.6, the family's weakest percussor). The poleaxe family COMPRESSES against PERC_CAP, and the staff's ~4
    intent is unreachable while the mace is pinned at PERC_CAP: at PERC_EXP=0.30 an authority RATIO of 0.5 demands an
    INPUT ratio of 0.5^(1/0.30) = 0.099. That is a PERC_SCALE/PERC_EXP re-fit question (see PERC_CAP's ownership
    note), not a lever question; test_gap_game_poleaxe_thrusts_in_the_duel and test_use_mode_selection_emerges_from_
    primitives' poleaxe-switches finding await that re-fit.
    CIRCUMSTANCE-DEGRADED (I2, D2b): grip/room-threaded via the SAME mode-split Phi_grip as heft (JD-4: percussion
    is grip-aware too, avoiding the M-08 blunt/cut asymmetry) PLUS a floored Phi_room (D2b — percussion keeps it,
    heft does not). `sel_head` overrides w['head'] for the affordance gate (None = native). At grip=0/room=1.0 both
    Phi terms are 1.0 for a BLUNT-headed weapon."""
    head = sel_head if sel_head is not None else w['head']
    if head != V.HEAD_BLUNT:
        return reversed_grip_percussion(w, grip=grip, room=room)
    m_strike, x_strike, _ = delivered_strike(w)
    lever = strike_point_lever(w, m_strike, x_strike)
    base = min(PERC_CAP, PERC_SCALE * (math.sqrt(m_strike) * lever * energy_credit(w)) ** PERC_EXP)
    return base * phi_grip(w, grip, V.HEAD_BLUNT, sel_pc) * phi_room_percussion(room)


def puncture_pressure(w, grip=0.0, room=1.0, sel_head=None, sel_pc=None):
    """Concentrated-blunt pierce: same authority delivered through a beak/pick (strike_concentration) -> pressure
    that defeats plate; a broad face -> 0 (concussion, not puncture). Grip/room-threaded through percussion_
    authority (I2/D2b) — byte-identical at grip=0/room=1.0."""
    sc = w.get('geo', {}).get('strike_concentration', 0.0)   # raw primitive, passed through by geometry.bake (geo is complete)
    return percussion_authority(w, grip=grip, room=room, sel_head=sel_head, sel_pc=sel_pc) * sc


def percussion_element_authority(w, elem_mass, elem_x, grip=0.0, room=1.0):
    """Per-element application of the percussion_authority FORM (I2, D2b — a per-element percussion_authority
    variant, NOT `at_circumstance`, which returns {I_g,S_g,d_g,u,...} and computes no percussion value at all). Uses
    THIS striking element's own mass_kg + its x_m as the moment-arm FRACTION of the weapon's total length (the
    per-element analogue of percussion_authority's whole-weapon sqrt(mass)*PoB_frac), with the whole-weapon
    `energy_credit` (a 2H/arc credit is a property of how the WHOLE weapon is gripped, not of one striking element).
    Distinguishes multi-blunt composites (lucerne_hammer's hammer face vs its rear 3-4 tine fluke). Degraded by the
    SAME grip/room Phi as the whole-weapon percussion_authority (D2/D2b) — a property of the grip/room circumstance,
    not of which element is striking. Pure.
    [ED-PC-0048, E2b] The lever is routed through `strike_point_lever`, the single owner, so the weapon and element
    scales carry one lever form (review R-11.4). It is never exactly zero: an element mounted AT the hand (hook_sword's
    crescent, `mode_elements[1]`, 0.140 kg at x = +0.000 m, JD-5) still has an arm's lever via STRIKE_HAND_LEVER, so
    any guard-mounted striking element can be afforded and selected.
    ⚠ CALLED WITH THE DELIVERED MASS, NOT `elem_mass` — load-bearing. `strike_point_lever`'s first argument is a mass
    it divides by the weapon's total, so passing `elem_mass` would double-count the striking mass (power 1.5). The
    element's own mass belongs in `sqrt()`; the LEVER is geometric. Passing `delivered_strike(w)[2]` makes
    `strike_point_lever` reduce exactly to `(STRIKE_HAND_LEVER + |x|) / (STRIKE_HAND_LEVER + Lt)` — the same single
    owner, the same form, no third lever, and no mass term where none belongs.
    ⚠ MAGNITUDE RESIDUE: a 0.140 kg hand-mounted crescent reads 4.132 on a 0-8 scale where a 1.2 kg mace reads 8.0;
    that is the PERC_EXP=0.30 low-mass compression (a PERC_SCALE/PERC_EXP re-fit question), not a lever question.
    See tests/valoria/test_combat_element_reachability.py."""
    m_total = delivered_strike(w)[2]
    lever = strike_point_lever(w, m_total, elem_x)     # == (STRIKE_HAND_LEVER + |x|) / (STRIKE_HAND_LEVER + Lt)
    base = min(PERC_CAP, PERC_SCALE * (math.sqrt(max(0.0, elem_mass)) * lever * energy_credit(w)) ** PERC_EXP)
    return base * phi_grip(w, grip, V.HEAD_BLUNT, None) * phi_room_percussion(room)


def armour_defeat_mode(w):
    """Route the armour-defeat path by head shape (the physics the live single blunt row flattens)."""
    head = w['head']
    if head == V.HEAD_BLUNT:
        sc = w.get('geo', {}).get('perc_conc', 0.0)
        return V.ADEF_MODE_PUNCTURE if sc >= 0.75 else V.ADEF_MODE_CONCUSSION
    if head in V.THRUST_FAMILY_HEADS:
        return V.ADEF_MODE_GAP_THRUST
    return V.ADEF_MODE_CUT


# ════════════════════ STAGE 3 — dynamics: agility, authority, reach, defence affinities ════════════════════
def agility(w):
    """Speed/handiness from swing inertia. GROUNDED SHAPE — a constant-exponent POWER LAW about the grip axis:
    agility ∝ MoI^(−AGILITY_EXP), EXP≈0.25 (Cross & Nathan 2009 / Fleisig 2002 — handle-axis bat/racket/golf swing
    studies, mass-independent, exponent 0.20–0.28). Anchored at AGILITY_REF (set just BELOW the lightest weapon's
    MoI), so the whole roster sits at agility ≤ 1 and the spread EMERGES strictly from MoI: dagger highest (~0.97) →
    spear lowest (~0.18). The exponent is grounded; AGILITY_REF is [SIM-CALIBRATE]. In (0,1].
    AGILITY_REF/MoI ≤ 1 for EVERY weapon, so the min(1.0,…) NEVER binds — it is an inert safety guard. The consumers
    (defense_affinities' dodge _band window + the parry agility-pivot) are renormalised to this agility range.
    I1, D11a: reads at_grip(w,0.0)['I_g'] (the SAME grip-adjusted MoI wield_heft/_recovery_mode_commitment/
    recoverability_factor read), at grip=0; at_grip(w,0)['I_g'] reconstructs derive(w)['MoI'] to within float
    round-trip noise."""
    return min(1.0, (AGILITY_REF / max(1e-6, at_grip(w, 0.0)['I_g'])) ** AGILITY_EXP)


def defense_affinities(w):
    """The {parry, dodge, wind} affinities the hand GATE table encodes — DERIVED from geometry + dynamics.
    wind: meet+dominate the bind — blade-catching guard x rigidity x bind-leverage x edge-length.
    dodge: void with footwork — lightness (agility) x one-handedness.
    parry: deflect safely — a guarded hand commits the parry; a handy weapon parries fast.
    MIGRATED (I1, D11a): lever_norm reads at_grip(w,0.0)['I_g'] instead of derive(w)['MoI'] directly — the SAME
    grip-adjusted MoI source agility()/wield_heft/_recovery_mode_commitment/recoverability_factor all read."""
    I_g0 = at_grip(w, 0.0)['I_g']
    cross_section = w.get('geo', {}).get('cross_section', 0.6)   # raw primitive via geometry.bake (geo is complete)
    rigidity = 0.30 + 0.70 * cross_section
    ag = agility(w)
    lever_norm = I_g0 / (1.0 / MOI_AGILITY_K + I_g0)              # bind-leverage in (0,1): heavy/forward dominates
    onehand = 1.0 if w['hands'] == 1 else 0.78
    wind = w.get('blade_guard', 0.4) * rigidity * (0.45 + 0.55 * lever_norm) * (0.7 + 0.3 * min(1.0, w['head_len'] / 0.90))   # 0.90 m = the old 3.0-lu edge-length saturation (U0)
    dodge = ag * onehand
    # AGILITY-PIVOT: agility() is anchored below the lightest MoI (capless), so its live range is compressed (a handy
    # 1H sword reads ag≈0.4); the parry saturation pivot is set to that range.
    # [SIM-CALIBRATE 0.39]
    parry = (0.45 + 0.55 * w.get('hand_guard', 0.4)) * (0.55 + 0.45 * min(1.0, ag / 0.39))

    def _band(x, lo, hi):                                         # remap into the ~[0.4,1.0] affinity band
        return round(0.4 + 0.6 * max(0.0, min(1.0, (x - lo) / (hi - lo))), 2)
    # DODGE _band window is set to the capless-agility range so the dodge spread runs dagger 1.0 > paired > sabre >
    # arming > … > heavies at the 0.4 floor rather than flat-topping at 1.0. [SIM-CALIBRATE 0.19,0.54]
    return dict(parry=_band(parry, 0.55, 1.0), dodge=_band(dodge, 0.19, 0.54), wind=_band(wind, 0.05, 0.45))


# ════════════════════ STAGE 3a — LOCATED-GUARD CATCH: hand_guard / blade_guard, DERIVED (morphology-rearch Phase B4) ═══
# The plan's aggregation-operator discipline: catch is a SATURATING SUM over a weapon's located `guards` (physical
# extent, x_m position) — not a placeless hand-authored 0-1 scalar. Two DIFFERENT physical questions share the same
# guards list: hand_guard asks "does hardware sit AT the working hand, shielding it from a sliding cut" (a guard far
# out on the head does nothing for your own grip — proximity-weighted); blade_guard asks "does the weapon have a
# catching/binding surface at all, wherever the bind lands" (a wing-lug or reverse hook two feet up a polearm still
# catches an opposing blade in the bind just fine — position-independent). A `dual_role_element` guard (a hook,
# prong, tine, or fluke that is ALSO a striking element, e.g. the guisarme's hook or the dangpa's flanking tines —
# Phase 0 documents these explicitly as catching/binding hardware, not decoration) contributes to catch exactly like
# dedicated hardware (a cross-guard, a tsuba); its mass is already counted once via `elements` (mass_kg=0 here).
GUARD_HAND_SCALE = 0.25  # [SIM-CALIBRATE] metres — proximity half-life-ish decay for hand-guard relevance; a guard at
                          #   this distance from the working hand counts ~37% toward hand_guard, negligibly beyond ~3x it.
HILT_CATCH_MULT = {V.HILT_COMPOUND: 3.0, V.HILT_SIMPLE: 1.0, V.HILT_NONE: 1.0}  # [SIM-CALIBRATE] a compound hilt (basket/swept/
                          #   rings) covers far more than its own bar-length extent suggests; a plain cross or a
                          #   hafted weapon's incidental catch-hardware does not get this multiplier.
GUARD_HAND_K = 3.0       # [SIM-CALIBRATE] fit against the pre-Phase-B4 authored hand_guard ladder (rough — Phase C
                          #   recalibrates against the balance harness, not this static-table fit)
GUARD_BLADE_K = 2.0      # [SIM-CALIBRATE] ditto, blade_guard ladder

def _guard_catch_raw(w, proximity):
    """Σ guard extent, each guard's contribution optionally decayed by distance from the working hand (x=0).
    proximity=False -> position-independent (blade_guard's bind-catch); proximity=True -> exp(-|x|/GUARD_HAND_SCALE)
    weighted (hand_guard's own-hand coverage). Pure."""
    total = 0.0
    for g in w.get('guards', ()):
        wgt = math.exp(-abs(g['x_m']) / GUARD_HAND_SCALE) if proximity else 1.0
        total += g['extent_m'] * wgt
    return total

def hand_guard(w):
    """Own-hand protection, DERIVED: a saturating function of guard hardware AT the working hand (proximity-
    weighted), scaled by hilt complexity (a swept/basket hilt covers the hand far more than a plain cross of the
    same bar length). In [0,1). A bare haft (spear, staff, mace — no guards) -> 0. Pure."""
    hm = HILT_CATCH_MULT.get(w.get('hilt', V.HILT_NONE), 1.0)
    return math.tanh(GUARD_HAND_K * hm * _guard_catch_raw(w, proximity=True))

def blade_guard(w):
    """Bind-catch capability, DERIVED: a saturating function of ALL located catching surfaces (guards AND
    dual-role catching elements — hooks/prongs/tines/lugs), position-independent (a bind can land anywhere along
    a long polearm's reach, not just at the hand), scaled by hilt complexity. In [0,1). Pure."""
    hm = HILT_CATCH_MULT.get(w.get('hilt', V.HILT_NONE), 1.0)
    return math.tanh(GUARD_BLADE_K * hm * _guard_catch_raw(w, proximity=False))


# ════════════════════ STAGE 3c — DISTRACTION: adornment motion degrades the defender's read (Phase B5) ════════════
# "a feather and ring distract eyes which makes it harder to read intent" (the design brief this re-architecture
# was built for). A weapon's `adornments` — a tassel, streamer, or plume attested for its type (Phase 0 physical
# facts) — adds visual clutter near the striking motion. Empty adornments (the overwhelming majority of the
# roster) -> distraction()==0 -> legibility() is unaffected.
DISTRACT_K = 2.0  # [SIM-CALIBRATE] saturating-sum gain on Σ count·extent_m; the 3 roster examples (ranseur/guandao/
                   #   jian tassels, each a single ~0.15-0.35m attachment) are ALL period-documented as a
                   #   ceremonial-phase feature, not a primary combat design element — deliberately kept small.

def distraction(w):
    """Saturating sum over the weapon's adornments (count × extent, position-independent — any motion near the
    weapon draws the eye). In [0,1); 0 for the (typical) weapon with no adornments field. Pure."""
    total = ltr_sum(a.get('count', 1) * a.get('extent_m', 0.0) for a in w.get('adornments', ()))
    return math.tanh(DISTRACT_K * total)


# ════════════════════ STAGE 3d — EDGE VIBRATION: a wavy/serrated edge degrades the OPPONENT's tactile read (Phase B5) ═
# "a wavy/serrated/irregular blade can cause vibrations for opponent... which would affect the effectiveness of
# riposting/winding" (the design brief). The vibration is felt by whoever is BOUND AGAINST the irregular edge — the
# wielder is used to their own weapon's feel, the opponent is not — so this degrades the OPPONENT's tactile read in
# a bind, not the wielder's own. Only flamberge currently carries edge_undulation (amplitude/period on its flame-
# ground element); every other weapon's elements default amplitude_mm=0 -> edge_vibration()==0 -> identity.
VIBRATION_K = 0.04  # [SIM-CALIBRATE] per mm of edge-undulation amplitude; flamberge's 15mm amplitude -> ~0.45, a
                     #   real but not dominant tactile disruption (bind_sigma's tac term is one of five summands).

def facing_pref(w):
    """U7/ED-PC-0020 — a weapon's preferred FACING REGIME, signed in [-1, 1]: a ONE-handed fighter keeps the off-side
    back and fights bladed/PROFILE (+, a narrower target, more voiding); a TWO-handed weapon commits both hands and
    must SQUARE UP to bring it on line (−, more profile presented). Emergent from `hands` (the regime is nearly
    categorical there — 'hands separates the twins': a 1H vs 2H version of the same blade face opposite regimes),
    with a mild reach saturation (a longer weapon commits its regime harder). No weapon name. Pure. Wired multiplicative
    into systems.facing_target (FACING_REGIME_K, K=0 -> inert/byte-identical until the U9 recalibration)."""
    sign = 1.0 if w['hands'] == 1 else -1.0
    return sign * (0.85 + 0.15 * math.tanh(2.0 * w['head_len']))

def edge_vibration(w):
    """The weapon's peak edge-undulation intensity — the MAX amplitude across its located elements (the most
    extreme undulating segment dominates the tactile signature felt by an opponent bound against it). In [0,1);
    0 for the (typical) plain-edged weapon. Pure."""
    amp = max((e.get('edge_undulation', {}).get('amplitude_mm', 0.0) for e in w.get('elements', ())), default=0.0)
    return math.tanh(VIBRATION_K * amp)


# ════════════════════ U3 — EDGE-COUNT PRIMITIVE: per-element edges={sides∈{0,1,2}, false_edge_frac} (ED-PC-0018) ═
# consolidation_v1.md §2.1-2.3. `elements[].edges` is a physical/attested blade fact (double vs single vs edgeless;
# a clipped false/back edge), landed as data like edge_undulation/adornments. It wires ONE channel per physical fact
# (§2.3, no double-counts): a double/false edge buys read-difficulty (edge_lines -> systems.legibility) + grab-resist
# (grab_hazard -> contact.grab_sigma); a single edge buys the spine-press bearing surface (spine -> systems.bind_sigma).
# Every reader is pure, iterates only elements that carry an `edges` key (a blunt/edgeless element has none), returns
# 0 for a weapon with no edges data (BYTE-IDENTICAL until the data + the K=0-gated downstream constants land — U9
# flips the constants). No weapon name — emergent from the per-element data.

def _blade_edges(w):
    """Yield each striking element's edges descriptor {sides, false_edge_frac} — only elements that carry one (a
    blunt/edgeless element with no `edges` key is skipped). Pure helper."""
    for e in w.get('elements', ()):
        ed = e.get('edges')
        if ed is not None:
            yield ed

def edge_lines(w):
    """Cut-line entropy — a double or false/back edge affords off-line and RETURN cuts, so the wielder's intent reads
    HARDER (the mechanical payload of a back-swing cut IS the unreadable return line; §2.3, JD-5). Per blade element:
    a double edge (sides==2) contributes the full return-line ambiguity (1.0); a single edge with a sharpened false
    edge contributes its false_edge_frac; a plain single or an edgeless element contributes 0. Weapon value = MAX over
    its blade elements (the most ambiguous edge dominates the read). In [0,1]; 0 for a plain-single/edgeless weapon.
    Pure — wired into systems.legibility (LEGIB_EDGELINE_K, K=0 until U9)."""
    def _el(ed):
        s = ed.get('sides', 1)
        if s == 2: return 1.0
        if s == 1: return ed.get('false_edge_frac', 0.0)
        return 0.0
    return max((_el(ed) for ed in _blade_edges(w)), default=0.0)

def spine(w):
    """Spine as bearing surface — a SINGLE edge leaves a rigid non-cutting back (a spine) to press/bind against the
    opposing blade (hand-high spine-press, Fühlen/winden); a double edge has no spine, an edgeless needle none worth
    pressing. Continuous: (sides==1)·(1−false_edge_frac) per element — a longer false/back edge eats the plain spine.
    Weapon value = MAX over blade elements. In [0,1]; 0 for a double-edged or edgeless weapon. Pure — wired into
    systems.bind_sigma (BIND_SPINE_K, K=0 until U9)."""
    def _el(ed):
        return (1.0 - ed.get('false_edge_frac', 0.0)) if ed.get('sides', 1) == 1 else 0.0
    return max((_el(ed) for ed in _blade_edges(w)), default=0.0)

def grab_hazard(w):
    """Grab hazard — a LIVE double edge resists being seized bare-handed (an unskilled/ill-timed grab self-injures); a
    plain single edge is half-hazardous (the spine is safe to grab); an edgeless element is safe. Per element:
    (sides + (sides==1)·false_edge_frac)/2 -> 0 edgeless, 0.5 plain single, up to ~0.6 clipped single, 1.0 double.
    Weapon value = MAX over blade elements. In [0,1]; 0 for an edgeless weapon. Pure — wired into contact.grab_sigma
    (GRAB_EDGE_K, K=0 until U9)."""
    def _el(ed):
        s = ed.get('sides', 1)
        return (s + (ed.get('false_edge_frac', 0.0) if s == 1 else 0.0)) / 2.0
    return max((_el(ed) for ed in _blade_edges(w)), default=0.0)


# ════════════════════ STAGE 3e — HEFT / HANDLING: derived off the per-part mass model (Phase B6) ════════════════
# Heft (impact force is a static moment) and handling (control demand is a balance/guard composite) are DIFFERENT
# physical quantities that share one mass model as their common source — grounded in the same data, not literally
# the same scalar (reusing wield_heft's own MoI-based swing-inertia formula for the IMPACT path would violate the
# falsifiable spear<arming<longsword<greatsword ordering: a spear's swing-inertia about the working hand is LARGE
# even though its striking mass is small, which is exactly the COST/IMPACT distinction wield_heft's own docstring
# draws).
HEFT_REF = 0.09609384729140724  # [ANCHOR, RE-DERIVED U1/ED-PC-0010, 2026-07-08] the 2H cut-thrust reference's
                    #   (longsword) own m_head*PoB_frac, so heft(longsword)==1.0 exactly (longsword's PoB is
                    #   weapons.py's). Rescales heft() for every weapon uniformly; DMG_SCALE's ~3.0 class magnitude
                    #   at this SAME anchor weapon is unaffected by a uniform rescale. The thrust lever is
                    #   THRUST_POB below (ED-PC-0027).
THRUST_POB = 0.16   # [SIM-CALIBRATE] the PoB-DECOUPLED effective lever for a THRUST's axial impact (ED-PC-0027,
                    # Jordan-ruled). A thrust delivers momentum ALONG THE LINE — its penetrating impact scales with
                    # the STRIKING MASS at the business end (m_head) but is INDEPENDENT of the weapon's forward
                    # balance (PoB_frac), unlike a swing (whose impact IS the forward-balance moment): the spear is
                    # very forward-balanced (PoB_frac 0.344) yet light-headed, so its thrust must not read hefty. The
                    # falsifiable ordering spear<arming<longsword<greatsword holds. Value ~ a hand-neutral balance
                    # (the controlled posture a thrust is delivered from), well below the forward swing PoBs
                    # (0.08-0.34). Total mass is not used (the long light shaft does not add to point impact).

# The "polearm out-thrusts a 2H sword at range" intent (Jordan review 2026-07-24) lives in the REACH/ARREST exchange
# during the approach (systems.arrest_impulse), not in a raw-heft penalty; THRUST_POB is the thrust-heft model.

def _arm_lever(d, head, sel_arm):
    """The base lever `heft` multiplies by the striking mass: the axial thrust lever for the puncture arm, the swing
    moment (floored forward-balance) for the shear arm, token-keyed when no arm is resolved. See `heft`."""
    if sel_arm == V.MODE_PUNCTURE:
        return THRUST_POB
    if sel_arm == V.MODE_SHEAR:
        return max(0.0, d['PoB_frac'])
    return THRUST_POB if head == V.HEAD_POINT else max(0.0, d['PoB_frac'])

def heft_by_arm(w, grip=0.0, sel_head=None, sel_pc=None):
    """(shear, puncture) heft of one weapon at one grip, with `phi_grip` evaluated ONCE: each value is exactly
    `heft(w, grip, sel_head, sel_pc, sel_arm=<that arm>)` (same expression, same order, same `phi`), for a caller that
    needs both arms (core.cut_thrust_impacts, core.strike) without paying the grip circumstance twice. Pure."""
    d = derive(w)
    head = sel_head if sel_head is not None else w['head']
    phi = phi_grip(w, grip, head, sel_pc)
    return tuple(((d['m_head'] * _arm_lever(d, head, a)) / HEFT_REF) * phi for a in (V.MODE_SHEAR, V.MODE_PUNCTURE))

def heft(w, grip=0.0, sel_head=None, sel_pc=None, sel_arm=None):
    """Impact heft — the weapon's striking mass × how forward-balanced it is (a heavy, forward-loaded head hits
    harder than a light, hand-balanced one), normalised so the 2H cut-thrust anchor (longsword) reads 1.0. PoB_frac
    is floored at 0 before use: a HAND-ON-BLADE grip (longsword_halfsword/estoc_halfsword) has its centre of mass
    BEHIND the working hand for CONTROL purposes (weapon_physics.derive's STAGE-1 docstring), but the strike itself
    still delivers real forward force — a negative "lever" would wrongly read as negative impact, not merely
    reduced. Read ONLY by the cut/thrust/point damage path (core.heft_resp); a BLUNT head's impact force already
    derives independently from percussion_authority. FALSIFIABLE ACCEPTANCE (verified at authoring time): spear <
    arming < longsword < greatsword, greatsword not collapsed onto longsword.
    CIRCUMSTANCE-DEGRADED (I2, D2): grip enters ONLY through the mode-split, thrust-protected, floored, NaN-guarded
    phi_grip multiplier — NEVER through a room term (Phi_room is explicitly CUT from the heft path, JD-1(d): a
    monotone heft-room multiply violates C4). `sel_head` is the SELECTED use-mode head (None = native
    w['head']); `sel_pc` is the selected element's own point_concentration (None = native whole-weapon
    point_concentration). At grip=0 phi_grip(w,0,...)==1.0 always, by construction — see phi_grip. Pure."""
    d = derive(w)
    head = sel_head if sel_head is not None else w['head']
    # MODE-SPLIT (ED-PC-0027): a SWING's impact is the forward-balance moment (m_head*PoB_frac); a THRUST's is axial,
    # PoB-DECOUPLED (m_head*THRUST_POB) — see THRUST_POB. phi_grip already grip-splits (point->1.0); this splits the
    # BASE lever too, so a forward-balanced light-headed weapon (spear) does not over-credit its thrust.
    # [ED-PC-0050, E3b] SPLIT ON THE RESOLVED ARM, NOT THE TOKEN. `cut_thrust` is ONE token whose arm is resolved
    # separately, in core.cut_thrust_arm — so a cut_thrust weapon that resolves the PUNCTURE arm is paid the thrust
    # lever, not the SWING moment. `sel_arm` is 'shear' | 'puncture' | None; None keeps the token-keyed behaviour
    # (pinned by test_arm_defaults_are_byte_identical).
    # Arm tokens come from vocabulary (V.MODE_PUNCTURE / V.MODE_SHEAR) — the alphabet has one owner (E0/ED-PC-0042).
    lever = _arm_lever(d, head, sel_arm)
    base = (d['m_head'] * lever) / HEFT_REF
    return base * phi_grip(w, grip, head, sel_pc)

HANDLING_POB_K = 1.00    # [SIM-CALIBRATE] PoB_frac contribution (forward-loaded balance demands more correction)
HANDLING_GUARD_K = 0.50  # [SIM-CALIBRATE] hand_guard REDUCES demand (a guarded grip is more forgiving to hold)

def handling(w):
    """Physical control-demand GAP — DERIVED from PoB_frac (forward-loaded balance demands more correction) and
    hand_guard (reduces demand — a guarded grip is more forgiving to hold); PHYSICAL ONLY. Scoped narrowly to
    the two NEW physical facts the retired `hand` category didn't already have a dedicated term for elsewhere —
    systems.str_demand ALREADY carries MoI (via wield_heft) and 2H (its own D_2H term) as separate summands, so
    this does not re-derive them (no double-count). The retired `hand` category (Forgiving/Standard/Demanding)
    was NOT purely physical — it encoded a weapon-TRADITION's skill-ceiling (a spear reads 'Forgiving' for its
    simple point-and-thrust technique despite a high PoB_frac; a rapier reads 'Demanding' for its sophisticated
    fencing system despite a guarded hilt) — verified at authoring time to have no meaningful correlation with
    PoB_frac/hand_guard across the roster, confirming the old category was skill-driven, not control-driven. That
    skill-ceiling axis is EXPLICITLY NOT reconstructed here (plan decision 4/6): it relocates to the future
    fighter/tradition competence layer. str_demand's resulting shift for skill-driven weapons is the accepted
    interim (decision 6). Non-negative. Pure."""
    d = derive(w)
    return max(0.0, HANDLING_POB_K * d['PoB_frac'] - HANDLING_GUARD_K * w.get('hand_guard', 0.0))


# ════════════════════ STAGE 3b — GRIP-POSITION: continuous hand-slide (retires the choke/normal/lunge strings) ════════════════════
# Grip is MORPHOLOGY, not a named state. Where the working hand sits on the shaft is a CONTINUOUS choice, bounded by
# the weapon's own geometry: a long shaft/grip slides (butt<->centre), a short hilt cannot. "Choke" = grip-position
# toward the centre, EMERGENT from grip_len — never a category. reach / MoI / close-capability / recovery all derive
# from g. (Grounded: the parallel-axis re-pivot. [FIAT]: the GRIP_* bounds, calibrated to the old CHOKE_GRIP_MIN.)
GRIP_SHORT = 0.30       # [FIAT] m (= the old 1.0-lu CHOKE_GRIP_MIN) grippable length at/below which the hand cannot gather forward (short hilt)
GRIP_LONG = 0.90        # [FIAT] m (= the old 3.0 lu) grippable length at which the full gather range is available
GRIP_MIN_WORKING = 0.30 # [FIAT] m of weapon kept ahead of the working hand (you must still have a weapon out front — already metres pre-U0)

def _gather_len(w):
    """Grippable length along the weapon, in metres — how far a hand can travel along it. A TIPPED pole's forward
    shaft is itself grippable (you regrip up the haft toward balance — the spear gathering to a short staff); a
    block-headed club or a hilted weapon offers only its grip (you cannot grip up a mace's head). Name-free: wclass
    selects which length primitives are grippable."""
    return w['grip_len'] + (w['head_len'] if w.get('wclass') == 'hafted_tip' else 0.0)

def grip_travel_max(w):
    """Forward hand-slide available, in metres = the grippable length less the minimum weapon kept out front."""
    return max(0.0, _gather_len(w) - GRIP_MIN_WORKING)

def grip_choke_max(w):
    """Regrip freedom in [0,1], DERIVED from the grippable length: a short hilt or a block-headed club -> 0 (cannot
    gather in), a long shaft -> 1. EMERGENT from morphology — never a weapon name or a 'can_choke' flag."""
    L = _gather_len(w)
    return max(0.0, min(1.0, (L - GRIP_SHORT) / (GRIP_LONG - GRIP_SHORT)))

def _geom_slide_max(w):
    """The MAXIMUM geometric forward hand-offset, in METRES, floored so the forward head extent kept ahead of the
    working hand never drops below GRIP_MIN_WORKING (M-04, D1): min(grip_travel_max(w), head_len - GRIP_MIN_WORKING).
    A pure geometric bound — decoupled from the CoM-clamped inertia slide u, so a centre-balanced staff's
    reach/rear-clearance still change with grip though its u==0 (M-20)."""
    return min(grip_travel_max(w), w['head_len'] - GRIP_MIN_WORKING)

def at_circumstance(w, grip=0.0, room=1.0):
    """Re-derive the working-pivot dynamics at grip-position `grip` in [0,1] (0 = held as issued; 1 = gathered to
    the working BALANCE — the hand slides forward toward the CoM, stopping AT it, since the CoM is the inertia
    minimum; you gather for control, you do not slide past it). The lunge/extension (reach side) is a BODY term
    handled in recoverability, not a hand-slide. EXACT parallel-axis off the LEAD-HAND axis (the axis derive()
    already uses). Returns {I_g, S_g, d_g, u, rear_clearance, geom_slide}. GROUNDED (parallel-axis theorem); the
    gather REACH is morphology-bounded ([FIAT] GRIP_*). A POLE regrips up the whole haft toward balance (the spear
    gathers to a short staff); a HILT slides within its grip only, gated by grip_len (a short hilt cannot gather —
    its half-sword form, not a slide, is its mid-blade grip).
    L0 CIRCUMSTANCE BUNDLE (I2, D1): two members beyond {I_g,S_g,d_g,u}, both PURE weapon+scalar functions (no
    Combatant — L0 purity, a structural test asserts this): `rear_clearance` — length trailing behind the working
    hand, from LOCATED parts (`_all_parts`, never `derive()['length_m']` — M-19: the full length is wrong for exactly
    the half-sword composites this is for), gathered-in via the geometric slide (below), NOT the CoM-bounded inertia
    slide `u` — a fighter's hand genuinely moves forward by `geom_slide` regardless of whether that motion buys
    any inertia benefit, and the rear overhang is a direct geometric consequence of THAT motion (M-20: a centre-
    balanced staff's `u` is clamped to 0 since it is already at the inertial optimum, but its rear_clearance must
    still lengthen as the grip slides forward — I7a's own acceptance gate). `geom_slide` — a geometric forward
    hand-offset (metres), FLOORED and decoupled from the CoM-bounded inertia slide `u` (M-04/M-20); scaled by the
    SAME `grip` fraction as `u`. `room` is accepted for the L0 bundle's consumers (D4/I5's swing-room
    term) but is UNUSED here — no member of THIS bundle degrades with room (that lever lives in commit_depth/
    legibility/percussion, never in the static kinematics)."""
    d = derive(w)
    m, PoB, I0 = w['mass'], d['PoB_m'], d['MoI']
    I_cm = max(0.0, I0 - m * PoB ** 2)                          # back out CoM inertia (same axis => valid, >=0)
    u_max = grip_choke_max(w) * max(0.0, min(PoB, grip_travel_max(w)))   # gather TOWARD the CoM, gated by regrip freedom; never past the inertia minimum
    gf = max(0.0, min(1.0, grip))
    u = gf * u_max                                              # forward hand-slide (m)
    d_g = PoB - u                                               # CoM-to-working-hand distance after the slide
    geom_slide = gf * max(0.0, _geom_slide_max(w))
    rear_clearance = -min((x - extent / 2.0) for (_mass, x, extent) in _all_parts(w)) + geom_slide
    return dict(I_g=I_cm + m * d_g ** 2,                        # MINIMUM (= I_cm) when u reaches the CoM
                S_g=m * abs(d_g), d_g=d_g, u=u,
                rear_clearance=rear_clearance, geom_slide=geom_slide)

def at_grip(w, g):
    """Thin alias onto at_circumstance's original {I_g,S_g,d_g,u} members (D1, I2). New code should call
    at_circumstance directly."""
    a = at_circumstance(w, g, 1.0)
    return dict(I_g=a['I_g'], S_g=a['S_g'], d_g=a['d_g'], u=a['u'])
