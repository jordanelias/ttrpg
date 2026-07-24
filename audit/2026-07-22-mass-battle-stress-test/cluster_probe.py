"""Envelop-cluster measurement with matched 3-command (tripartite: wing-centre-wing) defenders.
Both sides at constant density (GAUGE_CONC), force parity (GAUGE_TROOPS). The enveloper is already a
3-body composition; this matches the plain-Line/Arrowhead opponents to 3 commands. Reports decA vs band.
Run: python cluster_probe.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW
CONC = g.GAUGE_CONC; TOT = g.GAUGE_TROOPS

def tri_line(name, faction, shape='Line', total=TOT, conc=CONC, **uk):
    """A shape as a 3-command line (wing/centre/wing) at constant density, centred on the shape's anchor."""
    tier = 3
    anchor = g.ANCHOR_MAP.get((shape, tier), 10)
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    per = total / 3.0
    cells_per = per / conc
    specs = [{'shape': shape, 'troop_type': uk.get('troop_type','infantry'), 'troops': per, 'concentration': conc,
              'unit_type': uk.get('unit_type','melee'), 'stance': uk.get('stance','balanced'),
              'instructions': tuple(uk.get('instructions', ())),
              'starting_position': (start_row, int(round(anchor + (k-1)*cells_per)))}
             for k in range(3)]
    return build_army(specs, name, faction, power=uk.get('power',4), command=4,
                      discipline=uk.get('discipline',5), morale=uk.get('morale',6),
                      morale_start=uk.get('morale_start', None),
                      dr=1, stance=uk.get('stance','balanced'), speed=uk.get('speed','Standard'))

def run(n, ba, bb, tid, lo, hi, metric='decA'):
    A=B=d=0
    for s in range(n):
        random.seed(1_000_000+s)
        ua=ba('A','A'); ub=bb('B','B')
        r=g.resolve_battle(ua,ub,'Line','Line',g.ANCHOR_MAP,kind='multi',max_battle_turns=20)
        w=r.get('winner','draw'); A+=w=='A'; B+=w=='B'; d+=w not in('A','B')
    dec=A+B
    val = 100.0*A/(A+B+d) if metric=='rawA' else (100.0*A/dec if dec else 50.0)
    ok = lo<=val<=hi
    print(f"  {tid:5} {ba.__doc__ or '':2} A {A:2} B {B:2} draw {d:2}  {metric}={val:5.1f}  band {lo}-{hi}  {'OK' if ok else 'MISS'}")

ENV = lambda nm,fc: g._envelop_army(nm,fc)
REF = lambda nm,fc: g._refused_army(nm,fc)
if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 20
    print(f"Envelop cluster, matched 3-command defenders, n={n}")
    run(n, ENV, lambda nm,fc: tri_line(nm,fc,'Line'), 'H3', 55,72)
    run(n, ENV, lambda nm,fc: tri_line(nm,fc,'Arrowhead'), 'H4', 45,62)
    run(n, REF, lambda nm,fc: tri_line(nm,fc,'Line'), 'H6', 48,60)
    run(n, lambda nm,fc: tri_line(nm,fc,'Line'), ENV, 'H10', 28,45)
    run(n, lambda nm,fc: tri_line(nm,fc,'Arrowhead'), ENV, 'H11', 38,55)
    run(n, REF, ENV, 'H5', 48,62)
    print("  --- regression checks (should stay ~mid-band) ---")
    run(n, lambda nm,fc: tri_line(nm,fc,'Line'), lambda nm,fc: tri_line(nm,fc,'Line'), 'H1', 42,58)
    run(n, lambda nm,fc: tri_line(nm,fc,'Arrowhead'), lambda nm,fc: tri_line(nm,fc,'Line'), 'H2', 48,62)
