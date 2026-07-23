"""compare_formations.py — engine output vs historical schematic, side by side.

For each canonical army formation (double envelopment / oblique-refused / battle line) render:
  LEFT  = a SCHEMATIC drawn from the historical geometry (research synthesis; sources in
          research/diagrams/mass_battle_formations/SOURCES.md) — labelled, with movement arrows;
  RIGHT = the SIM output from the (fixed, ED-MB-0017) engine, cells coloured by subunit, tick-by-tick.
Self-contained HTML (inline SVG). Deterministic seeds.
"""
import os, sys, math, random
_HERE=os.path.dirname(os.path.abspath(__file__))
_REPO=os.path.abspath(os.path.join(_HERE,'..','..','..'))
sys.path.insert(0, os.path.join(_REPO,'tests','sim'))
import mass_battle.orchestration as orch
from mass_battle.engine import build_unit, build_army, build_envelopment, build_refused_flank
from mass_battle import validators as val
val._set_movement_path('node')

A_COLORS = ['#cf4b52', '#e07a5f', '#d1a15f', '#b5556f', '#9e4b4b', '#c56b4a', '#b8455f', '#d98a5a', '#a85050', '#e0925f', '#bf5a52']
B_COLORS = ['#2f6fb0', '#3fa0a0', '#5b74c9', '#4f8f77', '#6f7fb5']

def _cells(u):
    out = []
    for i, s in enumerate(u.subunits):
        pts = [(r, c) for (r, c) in s.cells_float()]
        out.append((i, s.shape, ','.join(s.instructions) or '—', getattr(s, 'routed', False), pts))
    return out

def snap(fa, fb, seed, tick):
    random.seed(seed)
    a, b = fa(), fb()
    if tick > 0:
        orch.run_battle(a, b, max_turns=tick)
    return _cells(a), _cells(b)

def _bounds(fa, fb, seed, ticks):
    rs, cs = [], []
    for tk in ticks:
        a, b = snap(fa, fb, seed, tk)
        for data in (a, b):
            for (_i, _s, _in, _rt, pts) in data:
                for (r, c) in pts:
                    rs.append(r); cs.append(c)
    pad = 1.5
    return (min(rs)-pad, max(rs)+pad, min(cs)-pad, max(cs)+pad) if rs else (0,1,0,1)

def sim_panel(a, b, bounds, w=188, h=188):
    rmin, rmax, cmin, cmax = bounds
    span = max(rmax-rmin, cmax-cmin, 1e-6)
    X = lambda c: (c-cmin)/span*(w-16)+8
    Y = lambda r: (r-rmin)/span*(h-16)+8
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">']
    g = []
    for c in range(math.ceil(cmin), int(cmax)+1): g.append(f'<line x1="{X(c):.1f}" y1="5" x2="{X(c):.1f}" y2="{h-5}"/>')
    for r in range(math.ceil(rmin), int(rmax)+1): g.append(f'<line x1="5" y1="{Y(r):.1f}" x2="{w-5}" y2="{Y(r):.1f}"/>')
    p.append(f'<g stroke="currentColor" stroke-opacity="0.09" stroke-width="0.5">{"".join(g)}</g>')
    for side, data in (('A', a), ('B', b)):
        pal = A_COLORS if side == 'A' else B_COLORS
        for (i, shape, instr, routed, pts) in data:
            col = pal[i % len(pal)]; op = 0.28 if routed else 1.0
            p.append(''.join(f'<circle cx="{X(c):.1f}" cy="{Y(r):.1f}" r="2.7" fill="{col}" fill-opacity="{op}" stroke="#0a0d13" stroke-opacity="0.3" stroke-width="0.5"/>' for (r, c) in pts))
    p.append('</svg>')
    return ''.join(p)

# ── historical schematics (drawn from the research geometry) ──
def schematic(kind, w=188, h=188):
    """A labelled block+arrow schematic on the SAME orientation as the sim (enemy at the TOP of the
    panel, our army advancing UP the panel; row=vertical, col=horizontal)."""
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" font-family="ui-sans-serif,system-ui">']
    p.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="none"/>')
    A = '#cf4b52'; B = '#2f6fb0'; ink = 'currentColor'
    def blk(x, y, bw, bh, fill, label='', op=1.0):
        p.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="2" fill="{fill}" fill-opacity="{op}"/>')
        if label: p.append(f'<text x="{x+bw/2:.0f}" y="{y+bh/2+3:.0f}" font-size="8" fill="#fff" text-anchor="middle">{label}</text>')
    def arr(x1, y1, x2, y2, dash=''):
        p.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{ink}" stroke-width="1.4" stroke-opacity="0.75" marker-end="url(#ah)" {dash}/>')
    p.append('<defs><marker id="ah" markerWidth="7" markerHeight="7" refX="5.5" refY="2.6" orient="auto"><path d="M0,0 L6,2.6 L0,5.2 Z" fill="currentColor" fill-opacity="0.8"/></marker></defs>')
    # enemy line at top (all schematics)
    blk(44, 14, 100, 12, B, 'enemy', 0.9)
    if kind == 'cannae':
        # center bowed FORWARD (convex, toward enemy = up), African columns on BOTH flanks, cavalry wings
        blk(74, 96, 40, 16, A, 'center', 0.95)                 # center block
        p.append('<path d="M74,96 Q94,82 114,96" fill="none" stroke="#fff" stroke-opacity="0.5" stroke-width="1"/>')  # convex apex hint
        blk(40, 108, 20, 30, '#9e4b4b', 'Afr', 0.95)           # left African column (deeper)
        blk(128, 108, 20, 30, '#9e4b4b', 'Afr', 0.95)          # right African column
        blk(20, 120, 16, 12, '#7a3b52', 'cav', 0.9)            # left cavalry
        blk(152, 120, 16, 12, '#7a3b52', 'cav', 0.9)           # right cavalry
        # movement: center withdraws (down), wings wheel INWARD (mirror), cavalry rides around to rear
        arr(94, 96, 94, 118)                                    # center gives ground (down)
        arr(50, 120, 74, 108)                                   # left Afr wheels IN-right
        arr(138, 120, 114, 108)                                 # right Afr wheels IN-left (mirror)
        arr(28, 118, 60, 20, 'stroke-dasharray="3 2"')          # left cav ride-around to enemy rear
        arr(160, 118, 128, 20, 'stroke-dasharray="3 2"')        # right cav ride-around (mirror)
    elif kind == 'refused':
        # oblique: strong LEFT forward (deep), refused RIGHT echeloned BACK
        blk(40, 74, 28, 44, A, 'strong', 0.95)                 # strong deep column, forward
        blk(104, 116, 44, 16, A, 'refused', 0.55)              # refused wing, echeloned back + right
        arr(54, 74, 54, 40)                                     # strong advances obliquely up
        p.append('<text x="126" y="150" font-size="8" fill="currentColor" opacity="0.7" text-anchor="middle">held back (echelon)</text>')
    elif kind == 'line':
        # triplex acies: 3-line checkerboard with gaps
        for k, (yy, lab) in enumerate([(96,'hastati'),(118,'principes'),(140,'triarii')]):
            off = 0 if k % 2 == 0 else 15
            for j in range(4):
                blk(40 + off + j*30, yy, 16, 14, A, '', 0.95 - k*0.12)
            p.append(f'<text x="150" y="{yy+10}" font-size="7.5" fill="currentColor" opacity="0.65">{lab}</text>')
        arr(94, 92, 94, 40)                                     # line advances
    p.append('</svg>')
    return ''.join(p)

# ── formations to compare ──
def _line3(fac): return build_unit('Line', 3, fac, fac, 25, troop_type='infantry')
def _def(fac): return build_army([{'shape':'Line','troops':1000,'concentration':50}], fac, fac, anchor_col=25)
def _env(fac): return build_envelopment([{'shape':'Line','troops':600,'concentration':50}],[{'shape':'Line','troops':500,'concentration':50,'troop_type':'cavalry','speed':'Fast'},{'shape':'Line','troops':500,'concentration':50,'troop_type':'cavalry','speed':'Fast'}], fac, fac)
def _ref(fac): return build_refused_flank([{'shape':'Line','troops':900,'concentration':50}],[{'shape':'Line','troops':600,'concentration':50}], fac, fac)
def _armyN(n): return lambda fac: build_army([{'shape':'Line','troops':400,'concentration':50} for _ in range(n)], fac, fac, anchor_col=25)

ROWS = [
    ('Double envelopment (Cannae)', 'cannae', lambda: _env('A'), lambda: _def('B'),
     'Cavalry wings (fast, 3x infantry) straddle the centre on BOTH flanks and wheel OPPOSITE senses, wrapping behind the enemy by ~t6-8 (a mirror). Enveloping units MUST be fast or they arrive piecemeal.'),
    ('Oblique / refused flank (Leuctra)', 'refused', lambda: _ref('A'), lambda: _def('B'),
     'Strong wing leads at the FRONT; the refused wing sits ECHELONED BACK, out of contact, until pressed. No overlap.'),
    ('Battle line — 3 subunits', 'line', lambda: _armyN(3)('A'), lambda: _def('B'),
     'Subunits spaced across a frontage centred on the anchor, none overlapping.'),
    ('Battle line — 7 subunits', 'line', lambda: _armyN(7)('A'), lambda: _armyN(7)('B'),
     'Same, denser: 7 subunits, still centred and non-overlapping.'),
    ('Battle line — 11 subunits (cap)', 'line', lambda: _armyN(11)('A'), lambda: _armyN(11)('B'),
     'The videogame cap: 11 subunits, centred, no overlap.'),
]

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else 'compare.html'
    ticks = [0, 4, 8, 12]
    css = """
    :root{--bg:#0d1119;--panel:#151c28;--p2:#101722;--line:#26313f;--ink:#e6ebf2;--mut:#8a94a6;--brass:#c9a35f;--grid:#aeb9c9}
    @media (prefers-color-scheme:light){:root{--bg:#ece7db;--panel:#f6f2e9;--p2:#efe9dc;--line:#d8d1c1;--ink:#20262f;--mut:#6f6a5c;--brass:#9a7434;--grid:#3a3630}}
    :root[data-theme=light]{--bg:#ece7db;--panel:#f6f2e9;--p2:#efe9dc;--line:#d8d1c1;--ink:#20262f;--mut:#6f6a5c;--brass:#9a7434;--grid:#3a3630}
    :root[data-theme=dark]{--bg:#0d1119;--panel:#151c28;--p2:#101722;--line:#26313f;--ink:#e6ebf2;--mut:#8a94a6;--brass:#c9a35f;--grid:#aeb9c9}
    *{box-sizing:border-box}body{background:var(--bg);color:var(--ink);margin:0;padding:30px 24px 54px;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;line-height:1.5}
    .wrap{max-width:1180px;margin:0 auto}.eyebrow{font:600 11px/1 ui-monospace,Menlo,monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--brass);margin:0 0 9px}
    h1{font-size:25px;font-weight:680;letter-spacing:-.02em;margin:0 0 8px;text-wrap:balance}.lede{color:var(--mut);max-width:70ch;margin:0 0 26px;font-size:14px}
    .row{margin:0 0 20px;padding:16px 18px;background:var(--panel);border:1px solid var(--line);border-radius:12px}
    .rh{display:flex;align-items:baseline;gap:10px;margin-bottom:4px}.rn{font:600 12px/1 ui-monospace,Menlo,monospace;color:var(--brass);border:1px solid var(--line);border-radius:5px;padding:4px 7px}
    .rt{font-size:15.5px;font-weight:620}.note{color:var(--mut);font-size:12.5px;margin:2px 0 12px;max-width:80ch}
    .cols{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start}
    .col{color:var(--grid)}.lab{font:600 10.5px/1 ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin:0 0 7px}
    .strip{display:flex;gap:9px;flex-wrap:wrap}.frame svg{display:block;background:var(--p2);border:1px solid var(--line);border-radius:7px}
    .tk{font:600 10px/1 ui-monospace,Menlo,monospace;color:var(--mut);text-align:center;margin-top:5px}
    .sch svg{display:block;background:var(--p2);border:1px solid var(--line);border-radius:7px}
    .vs{align-self:center;font:600 12px ui-monospace,Menlo,monospace;color:var(--mut)}
    """
    html = [f'<title>Formations — engine vs history</title><style>{css}</style>',
            '<div class="wrap"><p class="eyebrow">Mass-battle engine · deployment &amp; pathing audit (ED-MB-0017)</p>',
            '<h1>Army formations: engine vs historical geometry</h1>',
            '<p class="lede">Left: a schematic drawn from the historical geometry (sources in '
            'research/diagrams/mass_battle_formations/SOURCES.md). Right: the fixed engine’s output — each '
            'dot a cell, coloured by subunit, snapped at ticks 0/4/8/12 (enemy deploys at the top; our '
            'army advances upward). The prior engine deployed all subunits in a rightward column (overlap; '
            'both envelopment wings on one side; refused wing level with the line) — now fixed.</p>']
    for idx, (title, kind, fa, fb, note) in enumerate(ROWS):
        seed = 200 + idx
        bounds = _bounds(fa, fb, seed, ticks)
        html.append(f'<div class="row"><div class="rh"><span class="rn">{idx+1:02d}</span><span class="rt">{title}</span></div>')
        html.append(f'<div class="note">{note}</div><div class="cols">')
        html.append(f'<div class="col sch"><div class="lab">History (schematic)</div><div class="frame">{schematic(kind)}</div></div>')
        html.append('<div class="vs">vs</div>')
        html.append('<div class="col"><div class="lab">Engine (sim)</div><div class="strip">')
        for tk in ticks:
            a, b = snap(fa, fb, seed, tk)
            html.append(f'<div><div class="frame">{sim_panel(a, b, bounds)}</div><div class="tk">t{tk:02d}</div></div>')
        html.append('</div></div></div></div>')
    html.append('</div>')
    open(out, 'w').write('\n'.join(html))
    print('wrote', out)

if __name__ == '__main__':
    main()
