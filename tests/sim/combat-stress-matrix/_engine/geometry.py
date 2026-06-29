"""
geometry.py — weapon GEOMETRY -> combat-coefficient derivation (pure, build-time).

Rationale (Jordan 2026-06-02): the head categories ('point'/'cut_thrust'/'curved_cut'/'blunt') and the hand-set
`gap` (gap-thrust precision) are categorical PROXIES for what is really geometry. This module derives those
coefficients from physical geometric parameters so curved-vs-straight edges, point-vs-broad force concentration, and
blade rigidity are modelled from first principles rather than assigned by hand.

ENGINEERING CONTRACT (no runtime cost): these are pure functions. `bake(params)` precomputes a weapon's combat
coefficients ONCE at build time (the "precalculated surface"); the engine/sim reads the baked values. Adding
geometric granularity therefore adds build-time work only — zero added runtime calculation.

CALIBRATION DISCIPLINE: the derived coefficients are calibrated to REPRODUCE the already-validated §4-grounded
values (so the emergent tier-list we validated top-down is preserved), then the continuous geometry refines on top.

Geometric parameters (all 0..1 unless noted):
  curvature           straight edge = 0 ... strongly curved (shamshir) = 1
  point_concentration broad/spatulate tip = 0 ... needle/bodkin point = 1   (force concentration F/A)
  cross_section       whippy/thin (loses thrust vs hard plate) = 0 ... rigid thick diamond (estoc) = 1
  edge_keenness       blunt = 0 ... razor = 1                                (flesh-cutting)
  strike_concentration   broad face (mace flat / staff end) = 0 ... beak/pick = 1   (percussion focus; blunt heads)
  head_len, grip_len  relative lengths (already used by the lever-arm module)
"""
from math import tanh

# ---- derivations (pure) ----

def gap_precision(point_concentration, cross_section):
    """Gap-thrust precision: a thrust finds plate gaps in proportion to FORCE CONCENTRATION (a fine point) AND
    RIGIDITY (a stiff section keeps the point on line into hard plate; a whippy blade deflects/binds). Both required —
    a fine point on a whippy blade (rapier) loses authority vs plate; a fine point on a rigid section (estoc, rondel)
    keeps it. Rigidity is the dominant gate vs hard plate, so it enters with a steep weight. Reproduces validated `gap`."""
    conc = 0.25 + 0.75*point_concentration
    rigid = cross_section**1.15           # whippy sections lose plate-thrust authority (steep but not extreme)
    return round(min(1.0, conc * (0.30 + 0.70*rigid)), 2)

def thrust_factor(point_concentration, cross_section, curvature):
    """Thrust effectiveness: rises with point concentration + rigidity, FALLS with curvature (a curved blade's point
    is offset from the hand-target line, so the thrust is less direct/alignable)."""
    base = (0.35 + 0.65*point_concentration) * (0.55 + 0.45*cross_section)
    return round(max(0.0, base*(1.0 - 0.6*curvature)), 2)

def cut_factor(curvature, edge_keenness):
    """Cut effectiveness: a keen edge cuts; CURVATURE adds slicing/draw-cut (contact point translates along the edge,
    presenting a more acute effective angle). Diminishing returns on curvature."""
    return round((0.45 + 0.55*edge_keenness) * (1.0 + 0.45*tanh(2.0*curvature)), 2)

def percussion_concentration(strike_concentration):
    """For blunt heads: a concentrated striking surface (beak/pick) focuses force to defeat plate; a broad face
    (mace flat, staff end) spreads it. Multiplies the §4 percussion AUTHORITY (mass) handled elsewhere."""
    return round(0.55 + 0.45*strike_concentration, 2)

def can_halfsword_thrust(curvature, point_concentration):
    """Whether a sword can shift to a controlled gap-thrust (half-sword) in armour: needs a reasonably straight blade
    and a usable point. A strongly curved blade (sabre) cannot present a controlled thrust; a straight one can."""
    return curvature <= 0.35 and point_concentration >= 0.35

def bake(params):
    """Precompute the combat-coefficient surface for one weapon from its geometry. Build-time only; the engine reads
    the returned dict. Returns the derived {gap, thrust, cut, perc_conc, halfsword} coefficients."""
    cv = params.get('curvature', 0.0)
    pc = params.get('point_concentration', 0.0)
    cs = params.get('cross_section', 0.5)
    ek = params.get('edge_keenness', 0.0)
    sc = params.get('strike_concentration', 0.0)
    return dict(
        gap            = gap_precision(pc, cs),
        thrust         = thrust_factor(pc, cs, cv),
        cut            = cut_factor(cv, ek),
        perc_conc      = percussion_concentration(sc),
        halfsword      = can_halfsword_thrust(cv, pc),
    )
