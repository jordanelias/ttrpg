# Perimeter target-points + face normals — engagement/approach geometry (Jordan ruling 2026-07-23)

**Status:** SPEC / PROPOSED (un-built). Captures Jordan's hand-drawn model (2026-07-23 image) as the
authoritative geometric backbone for targeting, approach/pathing, contact, and the octagon facing model.
Supersedes the crude **subunit-centroid** reference used in the ED-MB-0018 multi-side trigger (which
already moved to a coarse nearest-face model; this is the full version).

## The model (from the drawing)

A subunit is a lattice of troop **cells** (the primitive). Its **perimeter** is a closed polygon of
**faces** (the yellow edges). On that perimeter live **target points**, each carrying an outward **normal**:

- **Major target points** = the **midpoint of each perimeter face** (one per face). The normal is
  **perpendicular to the face** (points straight out).
- **Minor target points** = the **corners/vertices** where two faces meet. The normal is the **bisector**
  of the two adjacent face normals (diagonal, ~45° for a rectangle).

The normal at the targeted point **defines the required angle of approach**: an attacking subunit that
wants to *engage correctly* maneuvers so its **entire body is aligned along that normal** (square-on to
the face) **before contact** — it wants to be fully oriented on that line, not strike obliquely. An
attacker en route to a target point **can be intercepted** (a covering body reaches the approach lane
first).

**Pointed-formation exception:** where a face pair meets at a **sharp vertex (interior tip angle ≲ 60°)** —
the apex of an Arrowhead/Wedge, a cavalry rhomboid — the tip is a **point, not a flat face**. Its target
point is the vertex and its normal is the apex bisector; the two adjacent faces are steeply raked, so a
frontal approach to the tip and a "flank" approach to the raked side are nearly the same bearing. Handle
the tip as a single high-exposure vertex target rather than forcing it into the 4-face front/left/right/rear
scheme.

## Why the centroid was wrong (what this replaces)

Using the subunit **centroid** as the single reference mislabels both the side struck and the point
targeted: a **flank** attack should engage the **outermost side line** and a **rear** attack the
**backmost line**, not a point in the middle of the body. A wide, shallow line hit head-on had its own
corner cells read as oblique from the centroid (spurious flank/"extra side"), which is exactly the bug the
ED-MB-0018 adversarial review caught in the multi-side shock. The perimeter-face model fixes this by
construction: each face is a real edge of the footprint, and each attacker engages the **nearest face**
(or its corner), by that face's own geometry.

## How it maps onto the engine (integration plan)

The pieces already exist in cell-space; this is mostly a new geometry layer + a targeting/approach term,
not a rewrite:

1. **Perimeter extraction (new, pure function).** From an atom's oriented cells, compute the convex/ortho
   hull → faces → major target points (face mids) + minor target points (corners) + per-point outward
   normals. Cell-emergent (extremes of the footprint), so it stays bottom-up. For Line/Column this is the
   4-face rectangle already approximated in `_octagon_dmg_mod`'s `_nearest_face`; Arrowhead/GappedLine get
   their true raked/gapped faces; the tip exception applies to Arrowhead.
2. **Targeting (extends `assign_targets`, `core/contact.py`).** An attacking subunit selects a target
   **point** on the enemy perimeter (by order/role: `direct`→a named face, `weakest`→lowest-defended face,
   `rear`/`flank`→that face). Today targeting picks an enemy *subunit*; this refines it to a *face/point*.
3. **Approach alignment (extends the maneuver goals, `hierarchy/units.py`).** The steering goal becomes
   "reach the target point **along its normal**, body oriented on that line" — i.e. path to a standoff
   point offset from the target along +normal, then close. This replaces the hardcoded `_envelop_goal`
   waypoint `(rear_r, wide_c)` (the scripting-drift the cell-up audit flagged) with an **emergent** goal
   derived from the enemy's live perimeter geometry — the wrap falls out of "approach the rear face along
   its normal," it isn't choreographed.
4. **Interception (new, cheap).** Before an attacker reaches its target point, a friendly body whose own
   footprint/reach covers the approach lane engages it first (fixing force / screen). This is the missing
   half of envelopment timing (the covering cavalry that must be beaten before the rear is open).
5. **Octagon exposure (already cell-up; refine reference).** Damage stays per-defender-cell (each cell's
   own facing vs the local attacker), unchanged. What improves: the **approach-angle-vs-face-normal**
   becomes the clean signal for *how square-on* the hit is (a glancing vs perpendicular strike on the
   face), and the multi-side shock's face-set (ED-MB-0019) reads the real faces engaged.

## Relationship to what shipped

- **ED-MB-0018/0019 (octagon damage model):** the per-cell damage arc is unchanged and correct. The
  multi-side shock already moved from the centroid to a **nearest-perimeter-face** classification
  (ED-MB-0019) — a first, coarse instance of this model (4 axis-aligned faces, no minor/corner points, no
  tip exception, no approach-normal). This spec is the full version it should converge to.
- **ED-MB-0017 (pathing):** `_envelop_goal`/`_sweep_goal` are the hardcoded waypoint state machines the
  cell-up audit graded as scripting-drift; step 3 above **retires** them in favour of the emergent
  approach-along-normal goal. This is the single biggest fidelity+architecture win in the plan.

## Open questions for Jordan

- **Minor (corner) target points:** are corners genuinely lower-value than face-mids (a corner is exposed
  on two arcs but harder to bring mass against), or higher (a corner cell is flanked from two sides)? The
  drawing marks them *minor* — confirm they're **secondary** approach points (used when the major face is
  contested), not primary.
- **Tip threshold:** ≲60° interior angle for the point-not-face exception — confirm the cutoff.
- **"Fully aligned before contact":** how hard is the alignment requirement — a hard gate (must be within
  X° of the normal or the charge is disordered/penalised) or a soft bonus (more aligned → more of the body
  lands in the first shock)? This is the lever that makes approach *discipline* matter.
