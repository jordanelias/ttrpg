"""Perimeter target-point / face-normal geometry (Jordan ruling 2026-07-23, see
audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md).

A subunit is a lattice of 1x1 troop cells. Its perimeter carries TARGET POINTS an attacker aims at,
each with an outward NORMAL that defines the required angle of approach (the attacker wants its body
aligned along the normal — square-on to the face — before contact):

  * MAJOR target points = the MIDPOINT of each perimeter face; normal perpendicular to the face.
  * MINOR target points = the CORNERS (hull vertices); normal along the corner bisector.
  * A sharp vertex (interior angle <= SHARP_TIP_DEG, the Arrowhead/Wedge apex) is flagged `sharp`
    — the pointed-formation exception (a point, not a flat face).

This is a PURE-GEOMETRY primitive (functions of the cell set only) — the behavioural wiring
(approach-along-normal pathing, the alignment gate, interception) is a separate, Jordan-gated step.
The faces come from the convex hull of the cell centres, which gives clean straight AND diagonal
faces (a Line's 4 edges, an Arrowhead's 2 raked sides + base) and matches Jordan's hand-drawing.
[Known limitation: a genuinely CONCAVE footprint (GappedLine's internal lane) is bridged by the hull;
concave/internal-face handling is a documented follow-up — see the spec.]
"""
import math
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

# interior vertex angle <= this -> a sharp tip (point, not a flat face)
SHARP_TIP_DEG = 60.0   # [canonical: perimeter_targeting_geometry_v1.md — Jordan 2026-07-23: "where the angle is like 60 or less" is the pointed-formation tip exception]

Point = Tuple[float, float]


@dataclass(frozen=True)
class TargetPoint:
    kind: str                 # 'major' (face midpoint) | 'minor' (corner vertex)
    pos: Point                # (r, c) on the perimeter
    normal: Tuple[float, float]  # outward unit normal = the required approach direction
    sharp: bool = False       # True only for a minor point at a sharp vertex (<= SHARP_TIP_DEG)


@dataclass(frozen=True)
class Face:
    a: Point                  # one endpoint (hull vertex)
    b: Point                  # the other endpoint
    mid: Point                # face midpoint (the major target point)
    normal: Tuple[float, float]  # outward unit normal


def _convex_hull(points: Sequence[Point]) -> List[Point]:
    """Counter-clockwise convex hull (Andrew's monotone chain). Deterministic; ties dropped."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts

    def cross(o: Point, a: Point, b: Point) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower: List[Point] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: List[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def _unit(v: Tuple[float, float]) -> Tuple[float, float]:
    m = math.hypot(v[0], v[1]) or 1.0
    return (v[0] / m, v[1] / m)


def _centroid(cells: Sequence[Point]) -> Point:
    n = len(cells)
    return (sum(r for r, _c in cells) / n, sum(c for _r, c in cells) / n)


def perimeter_faces(cells: Sequence[Point]) -> List[Face]:
    """The perimeter faces (convex-hull edges) with outward-pointing normals. Empty for < 3 cells
    (a point/line has no enclosed face)."""
    cells = list(cells)
    if len(cells) < 3:
        return []
    hull = _convex_hull(cells)
    if len(hull) < 3:
        return []
    cen = _centroid(cells)
    faces: List[Face] = []
    n = len(hull)
    for i in range(n):
        a = hull[i]
        b = hull[(i + 1) % n]
        mid = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
        # candidate normal perpendicular to the edge; flip to point AWAY from the centroid (outward)
        edge = (b[0] - a[0], b[1] - a[1])
        nrm = _unit((-edge[1], edge[0]))
        if (mid[0] + nrm[0] - cen[0]) ** 2 + (mid[1] + nrm[1] - cen[1]) ** 2 \
                < (mid[0] - cen[0]) ** 2 + (mid[1] - cen[1]) ** 2:
            nrm = (-nrm[0], -nrm[1])
        faces.append(Face(a=a, b=b, mid=mid, normal=nrm))
    return faces


def _vertex_interior_angle(prev: Point, p: Point, nxt: Point) -> float:
    """Interior angle (degrees) at hull vertex p between edges p->prev and p->nxt."""
    v1 = (prev[0] - p[0], prev[1] - p[1])
    v2 = (nxt[0] - p[0], nxt[1] - p[1])
    m1 = math.hypot(*v1) or 1.0
    m2 = math.hypot(*v2) or 1.0
    cos_a = max(-1.0, min(1.0, (v1[0] * v2[0] + v1[1] * v2[1]) / (m1 * m2)))
    return math.degrees(math.acos(cos_a))


def target_points(cells: Sequence[Point], sharp_tip_deg: float = SHARP_TIP_DEG) -> List[TargetPoint]:
    """All perimeter target points: one MAJOR per face (midpoint) + one MINOR per corner (vertex),
    each with its outward approach-normal. Corners with interior angle <= sharp_tip_deg are flagged
    `sharp` (the pointed-formation exception). Degenerate footprints (< 3 cells) return a single
    major point at the centroid facing an arbitrary axis, so callers always get a target."""
    cells = list(cells)
    if len(cells) < 3:
        cen = _centroid(cells) if cells else (0.0, 0.0)
        return [TargetPoint(kind='major', pos=cen, normal=(0.0, 1.0))]
    hull = _convex_hull(cells)
    cen = _centroid(cells)
    out: List[TargetPoint] = []
    # majors: face midpoints
    for f in perimeter_faces(cells):
        out.append(TargetPoint(kind='major', pos=f.mid, normal=f.normal))
    # minors: hull vertices, normal = outward corner bisector, sharp if the interior angle is acute
    n = len(hull)
    for i in range(n):
        p = hull[i]
        prev = hull[(i - 1) % n]
        nxt = hull[(i + 1) % n]
        ang = _vertex_interior_angle(prev, p, nxt)
        b1 = _unit((prev[0] - p[0], prev[1] - p[1]))
        b2 = _unit((nxt[0] - p[0], nxt[1] - p[1]))
        bis = (-(b1[0] + b2[0]), -(b1[1] + b2[1]))       # outward = away from both edges
        if math.hypot(*bis) < 1e-9:  # [canonical: epsilon: float magnitude guard] straight (degenerate) vertex -> use edge normal
            bis = _unit((-(nxt[1] - p[1]), nxt[0] - p[0]))
        nrm = _unit(bis)
        if (p[0] + nrm[0] - cen[0]) ** 2 + (p[1] + nrm[1] - cen[1]) ** 2 \
                > (p[0] - cen[0]) ** 2 + (p[1] - cen[1]) ** 2:
            pass                                          # already points outward
        else:
            nrm = (-nrm[0], -nrm[1])
        out.append(TargetPoint(kind='minor', pos=p, normal=nrm, sharp=(ang <= sharp_tip_deg)))
    return out


def nearest_target(cells: Sequence[Point], attacker: Point,
                   majors_only: bool = True) -> Optional[TargetPoint]:
    """The target point on `cells`'s perimeter nearest `attacker` — the face (or corner) an attacking
    body engages. Majors (faces) are the primary engagement points; minors are secondary (majors_only
    default). Returns None for an empty cell set."""
    tps = [t for t in target_points(cells) if (t.kind == 'major' or not majors_only)]
    if not tps:
        return None
    return min(tps, key=lambda t: (t.pos[0] - attacker[0]) ** 2 + (t.pos[1] - attacker[1]) ** 2)


def approach_alignment(cells: Sequence[Point], attacker: Point,
                       attacker_heading: Tuple[float, float]) -> float:
    """How square-on an attacker approaching its nearest face is: the cosine of the angle between the
    attacker's heading and the INWARD face normal (1.0 = perfectly aligned / square-on; 0 = grazing;
    < 0 = approaching from behind the face). This is the signal a future alignment gate/bonus consumes
    — the primitive only reports it; the hard-gate-vs-soft-bonus policy is Jordan-gated."""
    t = nearest_target(cells, attacker, majors_only=True)
    if t is None:
        return 0.0
    inward = (-t.normal[0], -t.normal[1])
    h = _unit(attacker_heading)
    return h[0] * inward[0] + h[1] * inward[1]
