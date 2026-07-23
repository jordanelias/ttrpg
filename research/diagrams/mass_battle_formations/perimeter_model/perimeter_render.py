"""Render each engine formation with the perimeter target-point / normal model computed from its ACTUAL
footprint, to machine-vision-verify it matches Jordan's drawing (faces=yellow, major targets=big red at
face mids, minor targets=small red at corners, normals=blue, sharp tips flagged)."""
import sys, math
sys.path.insert(0, '/home/user/ttrpg/tests/sim')
from mass_battle.geometry import CELL_PATTERN_FN

def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def render_shape(name, cells, ox, oy, scale=26):
    # cells are (r,c); draw c->x, r->y
    svg = []
    cx = sum(c for r, c in cells)/len(cells); cy = sum(r for r, c in cells)/len(cells)
    X = lambda c: ox + (c - cx)*scale + 130
    Y = lambda r: oy + (r - cy)*scale + 130
    # cells (black)
    for r, c in cells:
        svg.append(f'<circle cx="{X(c):.1f}" cy="{Y(r):.1f}" r="7" fill="#111"/>')
    # hull in (c,r) space so x=c,y=r
    hpts = hull([(c, r) for r, c in cells])
    n = len(hpts)
    # faces (yellow edges) + major target points (big red at mid) + normals (blue)
    for i in range(n):
        a = hpts[i]; b = hpts[(i+1) % n]
        ax, ay = X(a[0]), Y(a[1]); bx, by = X(b[0]), Y(b[1])
        svg.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#f2d024" stroke-width="6" stroke-linecap="round"/>')
        mx, my = (ax+bx)/2, (ay+by)/2
        # outward normal: edge dir (dx,dy); normal candidates (-dy,dx)/(dy,-dx); pick the one pointing away from centroid
        dx, dy = bx-ax, by-ay; L = math.hypot(dx, dy) or 1
        nx, ny = -dy/L, dx/L
        ccx, ccy = X(cx), Y(cy)
        if (mx+nx - ccx)**2 + (my+ny - ccy)**2 < (mx - ccx)**2 + (my - ccy)**2:
            nx, ny = -nx, -ny
        svg.append(f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{mx+nx*38:.1f}" y2="{my+ny*38:.1f}" stroke="#2aa4f4" stroke-width="5" stroke-linecap="round"/>')
        svg.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="15" fill="#f0473c"/>')  # major target
    # minor target points (corners) + corner bisector normals + sharp-tip detection
    for i in range(n):
        p = hpts[i]; prev = hpts[(i-1) % n]; nxt = hpts[(i+1) % n]
        px, py = X(p[0]), Y(p[1])
        v1 = (X(prev[0])-px, Y(prev[1])-py); v2 = (X(nxt[0])-px, Y(nxt[1])-py)
        l1 = math.hypot(*v1) or 1; l2 = math.hypot(*v2) or 1
        ang = math.degrees(math.acos(max(-1, min(1, (v1[0]*v2[0]+v1[1]*v2[1])/(l1*l2)))))  # interior angle
        # outward bisector
        bx_, by_ = -(v1[0]/l1 + v2[0]/l2), -(v1[1]/l1 + v2[1]/l2)
        bl = math.hypot(bx_, by_) or 1; bx_, by_ = bx_/bl, by_/bl
        svg.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px+bx_*30:.1f}" y2="{py+by_*30:.1f}" stroke="#2aa4f4" stroke-width="4" stroke-linecap="round"/>')
        sharp = ang <= 60
        rr = 12 if sharp else 8
        col = '#ff8c00' if sharp else '#f0473c'
        svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rr}" fill="{col}"/>')  # minor target (orange if sharp tip)
    label = f'{name}  ({len(cells)} cells, {n}-face hull)'
    svg.append(f'<text x="{ox+130}" y="{oy+250}" fill="#111" font-size="16" font-family="sans-serif" text-anchor="middle">{label}</text>')
    return '\n'.join(svg)

shapes = [('Line', CELL_PATTERN_FN['Line'](3)),
          ('Arrowhead', CELL_PATTERN_FN['Arrowhead'](4)),
          ('Column', CELL_PATTERN_FN['Column'](3)),
          ('GappedLine', CELL_PATTERN_FN['GappedLine'](3))]
panels = []
for i, (nm, cells) in enumerate(shapes):
    panels.append(f'<g transform="translate({(i%2)*320},{(i//2)*300})">{render_shape(nm, cells, 0, 0)}</g>')
html = f'''<!doctype html><html><body style="margin:0;background:#fff">
<svg width="700" height="640" viewBox="0 0 700 640" xmlns="http://www.w3.org/2000/svg">
<rect width="700" height="640" fill="#fff"/>
{''.join(panels)}
</svg></body></html>'''
open('/tmp/claude-0/-home-user-ttrpg/b2d06a23-ce9e-5027-ada9-5bfd82a3aab4/scratchpad/perimeter_render.html','w').write(html)
print("wrote perimeter_render.html")
