"""Calibrate a matched-granularity Cannae composition for H3 (Envelop vs Line, band decA 55-72).
Enveloper compositions (force+density parity, GAUGE_TROOPS=600 @ GAUGE_CONC) vs a granular Line.
Run: python cannae_calib.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))
sys.path.insert(0, _SIM)
import gauge_mb as g            # noqa: E402
from mass_battle.engine import (build_army, build_envelopment,       # noqa: E402
                                 SIDE_A_START_ROW, SIDE_B_START_ROW)

CONC = 100.0
TOT = 600.0
ANCHOR = g.ANCHOR_MAP.get(('Line', 3), 10)


def granular_line(name, faction, n_sub=6, total=TOT, conc=CONC, **uk):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    per = total / n_sub
    cells_per = per / conc
    span = n_sub * cells_per
    c0 = ANCHOR - span / 2.0
    specs = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': per, 'concentration': conc,
              'starting_position': (start_row, int(round(c0 + (i + 0.5) * cells_per)))}
             for i in range(n_sub)]
    return build_army(specs, name, faction, power=4, command=4, discipline=5, morale=6,
                      dr=1, stance=uk.get('stance', 'balanced'), speed='Standard')


def cannae(name, faction, *, center_frac=1/3, n_center=2, inf_wings=True, cav_wings=True,
           conc=CONC, total=TOT, center_width=None):
    """Deep centre (n_center stacked subunits, narrow) + optional infantry flank wings +
    optional fast cavalry rear wings. Force+density parity."""
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    center_troops = total * center_frac
    rem = total - center_troops
    n_wing_pairs = (1 if inf_wings else 0) + (1 if cav_wings else 0)
    wing_troops = rem / (2 * n_wing_pairs) if n_wing_pairs else 0.0
    per_center = center_troops / n_center
    center = []
    for j in range(n_center):
        sp = {'shape': 'Line', 'troop_type': 'infantry', 'troops': per_center, 'concentration': conc,
              'starting_position': (start_row, ANCHOR + (j - (n_center - 1) / 2.0) * 1)}
        if center_width is not None:
            sp['width'] = center_width
        center.append(sp)
    wings = []
    if inf_wings:
        wings += [{'shape': 'Line', 'troop_type': 'infantry', 'troops': wing_troops, 'concentration': conc},
                  {'shape': 'Line', 'troop_type': 'infantry', 'troops': wing_troops, 'concentration': conc}]
    if cav_wings:
        wings += [{'shape': 'Line', 'troop_type': 'cavalry', 'troops': wing_troops, 'concentration': conc},
                  {'shape': 'Line', 'troop_type': 'cavalry', 'troops': wing_troops, 'concentration': conc}]
    return build_envelopment(center, wings, name, faction, speed='Fast' if cav_wings else 'Standard')


def run(n, builder_a, builder_b, label):
    A = B = draw = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        ua = builder_a('A', 'A'); ub = builder_b('B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=20)
        w = r.get('winner', 'draw'); A += w == 'A'; B += w == 'B'; draw += w not in ('A', 'B')
    dec = A + B
    decA = 100.0 * A / dec if dec else 50.0
    print(f"  {label:52} A {A:2} B {B:2} draw {draw:2}   decA={decA:5.1f}%")


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"H3 Envelop(A) vs Line(B), n={n}   band decA 55-72")
    for nl in (5, 6, 7):
        run(n, lambda nm, fc: g._envelop_army(nm, fc),
            lambda nm, fc, nl=nl: granular_line(nm, fc, n_sub=nl), f'thin-enveloper vs {nl}-line')
    print("  --- matched-granularity Cannae compositions vs 6-line ---")
    L6 = lambda nm, fc: granular_line(nm, fc, n_sub=6)
    run(n, lambda nm, fc: cannae(nm, fc, inf_wings=True, cav_wings=False), L6, 'centre+inf-wings (4 sub) vs 6-line')
    run(n, lambda nm, fc: cannae(nm, fc, inf_wings=True, cav_wings=True), L6, 'centre+inf+cav-wings (6 sub) vs 6-line')
    run(n, lambda nm, fc: cannae(nm, fc, center_frac=1/2, inf_wings=True, cav_wings=True), L6, 'fat-centre(1/2)+inf+cav vs 6-line')
    run(n, lambda nm, fc: cannae(nm, fc, center_frac=1/2, n_center=3, inf_wings=True, cav_wings=True), L6, 'deep-centre(1/2,3-stack)+inf+cav vs 6-line')


def granular_line_wd(name, faction, n_sub=6, total=TOT, conc=CONC, width=None, depth=None):
    """Granular line with explicit per-subunit width×depth (ranks)."""
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    per = total / n_sub
    cells_per = per / conc
    span = n_sub * max(1, (width or cells_per))
    c0 = ANCHOR - span / 2.0
    specs = []
    for i in range(n_sub):
        sp = {'shape': 'Line', 'troop_type': 'infantry', 'troops': per, 'concentration': conc,
              'starting_position': (start_row, int(round(c0 + (i + 0.5) * max(1, (width or cells_per)))))}
        if width is not None: sp['width'] = width
        if depth is not None: sp['depth'] = depth
        specs.append(sp)
    return build_army(specs, name, faction, power=4, command=4, discipline=5, morale=6,
                      dr=1, stance='balanced', speed='Standard')
