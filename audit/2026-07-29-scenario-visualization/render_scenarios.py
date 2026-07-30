"""render_scenarios.py — visualise all 20 honest-gauge scenarios, tick by tick, for visual audit.

WHY THIS EXISTS. The gauge reports a number per row (win%, casualty%, in-band or not). A number
cannot tell you *why* a row is out of band, and every diagnosis in the last two audits therefore
needed a bespoke probe — there are now 23 of them. This renders what the engine actually DOES in each
of the 20 history-grounded scenarios, on the same coordinate convention as the historical schematics
in `research/diagrams/mass_battle_formations/`, so engine geometry can be read against the
historical geometry panel-for-panel rather than argued about.

**Armies are built by the gauge's own builders.** `gauge_mb.make_unit` / `_envelop_army` /
`_refused_army` are imported and called with the row's own kwargs — this renders THE SCENARIO THE
GAUGE SCORES, not a lookalike. Re-deriving the deployment here is how a visualisation ends up
faithfully depicting something the engine never ran (and it is the same single-owner rule the rest
of this lane runs on).

**Tracked, not one-shot.** Every run writes `manifest.json` with a SHA-256 per scenario panel, so a
re-run after an engine change shows exactly which scenarios moved. That is the point: the images are
a regression surface, not decoration.

    python3 audit/2026-07-29-scenario-visualization/render_scenarios.py [--ticks 0,4,8,12,16,20]
    python3 -m playwright ... (see render_png.py for the headless-Chromium rasteriser)

Orientation matches the existing historical schematics exactly: **side B (blue) deploys at the top,
side A (red) advances upward**, one dot per cell, coloured by subunit, routed subunits faded.
"""
import argparse
import hashlib
import json
import math
import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, '..', '..'))
sys.path.insert(0, os.path.join(_REPO, 'tests', 'sim'))
sys.path.insert(0, _HERE)

import mass_battle.orchestration as orch          # noqa: E402
import gauge_mb as g                              # noqa: E402
import mass_battle.config as cfg                  # noqa: E402

# Same palettes as research/diagrams/mass_battle_formations/generate_comparison.py, so a reader can
# put the two side by side without re-learning the colour language.
A_COLORS = ['#cf4b52', '#e07a5f', '#d1a15f', '#b5556f', '#9e4b4b', '#c56b4a',
            '#b8455f', '#d98a5a', '#a85050', '#e0925f', '#bf5a52']
B_COLORS = ['#2f6fb0', '#3fa0a0', '#5b74c9', '#4f8f77', '#6f7fb5', '#4a86c8', '#3c7f95']

DEFAULT_TICKS = (0, 4, 8, 12, 16, 20)
SEED = 1_000_000          # gauge_mb.matchup's own seed_base — the first seed of every row


SCALE = os.environ.get('VIZ_SCALE', 'historical')   # 'historical' | 'gauge'


def scenarios():
    """The 20 rows, at the requested scale.

    'gauge'      — exactly what the honest gauge scores: tier-3 single-subunit bodies (25 cells,
                   400 troops). Kept because it is the CONTROL: it shows why the historical
                   comparison could not be made at that scale.
    'historical' — the same 20 matchups rebuilt from the precedent battles' real orders of battle
                   (see scaled_orders_of_battle.py): historical ratio, formation and subunit count,
                   scaled only as far as the engine's own ceilings force.
    """
    if SCALE == 'gauge':
        return [(r[0], r[1], r[2], r[3], r[4], r[5]) for r in
                (g.TESTS + (g.CAV_TESTS if cfg.PER_CELL else []))]
    import scaled_orders_of_battle as S
    return [(rid, label, fa, fb, {}, {}) for rid, label, fa, fb in S.SCALED]


def _build(spec, side):
    """Build one side using that row's OWN constructor — never a re-derivation."""
    shape, kw = spec
    if callable(shape):
        try:
            return shape(side, side, **kw)          # gauge_mb's _envelop_army/_refused_army
        except TypeError:
            return shape(side, **kw)                # scaled_orders_of_battle builders
    return g.make_unit(shape, 3, side, side, **kw)


def _cells(u):
    out = []
    for i, s in enumerate(u.subunits):
        pts = [(r, c) for (r, c) in s.cells_float()]
        out.append({'idx': i, 'shape': s.shape,
                    'instr': ','.join(getattr(s, 'instructions', ())) or '—',
                    'routed': bool(getattr(s, 'routed', False)),
                    'troops': round(sum(getattr(s, 'cell_troops', {}).values()), 1),
                    'pts': pts})
    return out


def snapshot(row, tick):
    """One deterministic snapshot. Rebuilt from the same seed each time — never advanced in place,
    so tick N is always 'N ticks from spawn' and never 'wherever the previous panel left off'."""
    _id, _label, sa, sb, ka, kb = row[0], row[1], row[2], row[3], row[4], row[5]
    random.seed(SEED)
    a = _build((sa, ka), 'A')
    b = _build((sb, kb), 'B')
    if tick > 0:
        orch.run_battle(a, b, max_turns=tick)
    return _cells(a), _cells(b), a, b


def _bounds(row, ticks):
    rs, cs = [], []
    for tk in ticks:
        ca, cb, _a, _b = snapshot(row, tk)
        for data in (ca, cb):
            for s in data:
                for (r, c) in s['pts']:
                    rs.append(r); cs.append(c)
    pad = 2.0
    if not rs:
        return (0, 1, 0, 1)
    return (min(rs) - pad, max(rs) + pad, min(cs) - pad, max(cs) + pad)


def panel(ca, cb, bounds, tick, w=250, h=250):
    rmin, rmax, cmin, cmax = bounds
    span = max(rmax - rmin, cmax - cmin, 1e-6)
    X = lambda c: (c - cmin) / span * (w - 20) + 10
    Y = lambda r: (r - rmin) / span * (h - 20) + 10
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
         f'aria-label="tick {tick}">']
    grid = []
    for c in range(math.ceil(cmin), int(cmax) + 1):
        grid.append(f'<line x1="{X(c):.1f}" y1="6" x2="{X(c):.1f}" y2="{h-6}"/>')
    for r in range(math.ceil(rmin), int(rmax) + 1):
        grid.append(f'<line x1="6" y1="{Y(r):.1f}" x2="{w-6}" y2="{Y(r):.1f}"/>')
    p.append(f'<g stroke="#8899aa" stroke-opacity="0.13" stroke-width="0.5">{"".join(grid)}</g>')
    for side, data in (('A', ca), ('B', cb)):
        pal = A_COLORS if side == 'A' else B_COLORS
        for s in data:
            col = pal[s['idx'] % len(pal)]
            op = 0.22 if s['routed'] else 0.95
            p.append(''.join(
                f'<circle cx="{X(c):.1f}" cy="{Y(r):.1f}" r="3.0" fill="{col}" '
                f'fill-opacity="{op}" stroke="#0a0d13" stroke-opacity="0.35" stroke-width="0.5"/>'
                for (r, c) in s['pts']))
    p.append(f'<text x="8" y="{h-6}" font-size="11" fill="#8899aa">t={tick}</text>')
    p.append('</svg>')
    return ''.join(p)


def render(ticks=DEFAULT_TICKS, out_dir=None):
    out_dir = out_dir or _HERE
    rows = scenarios()
    manifest = {'flags': {k: getattr(cfg, k) for k in
                          ('PER_CELL', 'FIELD_MOVEMENT', 'PC_NODE_COHESION', 'PC_CELL_MORALE',
                           'PC_CELL_DAMAGE', 'PC_OCTAGON_DMG', 'PC_STOCHASTIC_ROUT',
                           'PC_CLOSE_RANKS', 'PC_INTENT_RESOLUTION', 'PC_FRACTIONAL_POOL',
                           'PC_FRICTION_CEV', 'PC_YIELD_EMERGENT', 'PC_RESERVE_COMMIT',
                           'PC_FEIGNED_RETREAT', 'PC_TROOP_DENSITY_CAP')
                          if hasattr(cfg, k)},
                'ticks': list(ticks), 'seed': SEED, 'scale': SCALE, 'scenarios': {}}
    body = []
    for row in rows:
        rid, label = row[0], row[1]
        bounds = _bounds(row, ticks)
        panels = []
        end_state = None
        for tk in ticks:
            ca, cb, ua, ub = snapshot(row, tk)
            panels.append(panel(ca, cb, bounds, tk))
            end_state = {
                'a_hp_pct': round(100 * ua.hp / ua.hp_max, 1) if ua.hp_max else 0,
                'b_hp_pct': round(100 * ub.hp / ub.hp_max, 1) if ub.hp_max else 0,
                'a_routed': bool(ua.routed), 'b_routed': bool(ub.routed),
                'a_subunits': len(ua.subunits), 'b_subunits': len(ub.subunits),
                'a_troops': round(ua.hp, 1), 'b_troops': round(ub.hp, 1),
            }
        strip = ''.join(f'<div class="p">{s}</div>' for s in panels)
        # The hash covers the SVG geometry only — the caption carries counts that are already in
        # the manifest, so a caption reword cannot masquerade as a geometry change.
        digest = hashlib.sha256(''.join(panels).encode()).hexdigest()
        manifest['scenarios'][rid] = {'label': label, 'sha256': digest, 'end_state': end_state}
        body.append(
            f'<section id="{rid}"><h2>{rid} — {label}</h2>'
            f'<p class="meta">A: {end_state["a_subunits"]} subunit(s), {end_state["a_troops"]:.0f} troops '
            f'&middot; B: {end_state["b_subunits"]} subunit(s), {end_state["b_troops"]:.0f} troops '
            f'&middot; end t={ticks[-1]}: A {end_state["a_hp_pct"]}% hp'
            f'{" (ROUTED)" if end_state["a_routed"] else ""}, '
            f'B {end_state["b_hp_pct"]}% hp{" (ROUTED)" if end_state["b_routed"] else ""}'
            f'<br><span class="sha">geometry sha256 {digest[:16]}…</span></p>'
            f'<div class="strip">{strip}</div></section>')

    flags_txt = ' &middot; '.join(f'{k}={int(bool(v))}' for k, v in manifest['flags'].items())
    html = f'''<!doctype html><meta charset="utf-8"><title>Mass battle — 20 scenarios, tick by tick</title>
<style>
 body{{background:#0d1117;color:#c9d1d9;font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;margin:0;padding:24px}}
 h1{{font-size:20px;margin:0 0 4px}} h2{{font-size:15px;margin:26px 0 4px;color:#e6edf3}}
 .meta{{margin:0 0 8px;color:#8b949e;font-size:12px}} .sha{{color:#6e7681;font-family:ui-monospace,monospace}}
 .strip{{display:flex;gap:8px;flex-wrap:wrap}} .p{{background:#161b22;border:1px solid #21262d;border-radius:6px}}
 .legend{{color:#8b949e;font-size:12px;margin-bottom:16px}}
 .flags{{font-family:ui-monospace,monospace;font-size:11px;color:#8b949e;margin-bottom:18px;
        background:#161b22;border:1px solid #21262d;border-radius:6px;padding:8px 10px}}
</style>
<h1>Mass battle — all {len(rows)} scenarios ({SCALE} scale), tick by tick</h1>
<p class="legend">Side <b style="color:#cf4b52">A (red)</b> advances upward; side
<b style="color:#2f6fb0">B (blue)</b> deploys at the top. One dot per cell, coloured by subunit;
routed subunits faded. Same coordinate convention and palette as
<code>research/diagrams/mass_battle_formations/</code>, so panels compare directly against the
historical schematics. Armies are built by <code>gauge_mb</code>'s own constructors — this is the
scenario the gauge scores, not a lookalike. Seed {SEED}, deterministic.</p>
<div class="flags">{flags_txt}</div>
{''.join(body)}'''
    hp = os.path.join(out_dir, f'scenarios_{SCALE}.html')
    with open(hp, 'w', encoding='utf-8') as f:
        f.write(html)
    mp = os.path.join(out_dir, f'manifest_{SCALE}.json')
    with open(mp, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
    print(f"wrote {hp}\nwrote {mp}\nscenarios: {len(rows)}  ticks: {list(ticks)}")
    return manifest


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ticks', default=','.join(str(t) for t in DEFAULT_TICKS))
    ap.add_argument('--out-dir', default=None)
    a = ap.parse_args()
    render(tuple(int(x) for x in a.ticks.split(',')), a.out_dir)
