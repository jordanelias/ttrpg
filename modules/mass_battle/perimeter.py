"""Perimeter faces from the convex hull of a subunit's cell centres, with outward normals; read by
`units._envelop_goal`. Pure geometry (functions of the cell set only).
[Known limitation: a genuinely CONCAVE footprint (GappedLine's internal lane) is bridged by the hull.]
"""
import math
from dataclasses import dataclass
from typing import List, Sequence, Tuple

Point = Tuple[float, float]


@dataclass(frozen=True)
class Face:
    a: Point                  # one endpoint (hull vertex)
    b: Point                  # the other endpoint
    mid: Point                # face midpoint
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
