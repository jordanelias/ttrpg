"""Granularity probe: is the H3/H4 envelopment inversion a UNIT-GRANULARITY artifact?
Hypothesis: the defender Line is ONE monolithic 600-troop subunit, so flank/rear damage dilutes
across its whole HP pool and it never routs, while the envelop army's three 200-troop subunits rout
piecemeal. A defender split into N subunits should let its outer subunits rout + cascade -> envelop wins.
Run: python granularity_probe.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))
sys.path.insert(0, _SIM)
import gauge_mb as g            # noqa: E402
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW  # noqa: E402


def multi_line(name, faction, n_sub=6, total=600.0, conc=100.0, anchor=10, **unit_kw):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    per = total / n_sub
    cells_per = per / conc
    span = n_sub * cells_per
    c0 = anchor - span / 2.0
    specs = []
    for i in range(n_sub):
        col = int(round(c0 + (i + 0.5) * cells_per))
        specs.append({'shape': 'Line', 'troop_type': 'infantry',
                      'troops': per, 'concentration': conc,
                      'starting_position': (start_row, col)})
    return build_army(specs, name, faction, power=4, command=4, discipline=5, morale=6,
                      dr=1, stance=unit_kw.get('stance', 'balanced'), speed='Standard')


def run(n, defender_builder, label):
    A = B = draw = 0
    for s in range(n):
        random.seed(1_000_000 + s)
        ua = g._envelop_army('A', 'A')
        ub = defender_builder('B', 'B')
        r = g.resolve_battle(ua, ub, 'Line', 'Line', g.ANCHOR_MAP, kind='multi', max_battle_turns=20)
        w = r.get('winner', 'draw'); A += w == 'A'; B += w == 'B'; draw += w not in ('A', 'B')
    dec = A + B
    decA = 100.0 * A / dec if dec else 50.0
    print(f"  {label:34} envelop(A) {A:2}  line(B) {B:2}  draw {draw:2}   decA={decA:5.1f}%")


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"H3 Envelopment(A) vs Line(B), n={n}  (band decA 55-72)")
    run(n, lambda nm, fc: g.make_unit('Line', 3, nm, fc), 'monolithic Line (current)')
    for k in (3, 6, 9):
        run(n, lambda nm, fc, k=k: multi_line(nm, fc, n_sub=k), f'{k}-subunit Line')
