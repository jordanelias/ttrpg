"""Fast diagnostic-core gauge probe (honest-gauge rebuild scaffolding).
Runs a small set of the most diagnostic rows, unbuffered, printing per-row as it goes."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gauge_mb as g
import mass_battle.config as c

def one(tid, label, sa, sb, ka, kb, mode='multi', n=20):
    r = g.matchup(sa, sb, ka, kb, mode, n=n)
    print(f"  {tid:4} {label[:34]:34} A%={r['a']:5.1f} B%={r['b']:5.1f} D%={r['d']:5.1f} decA={r['decA']:5.1f} t={r['t']:4.1f}", flush=True)
    return r

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    full = '--full' in sys.argv
    print(f"PER_CELL={c.PER_CELL} LANCH_DENSITY_REF={c.LANCHESTER_DENSITY_REF} CELL_CAP={c.CELL_CAP} K_LINEAR={c.K_LINEAR} n={n}", flush=True)
    if full:
        print("--- FULL gauge (multi), band in [] ---", flush=True)
        tests = g.TESTS + (g.CAV_TESTS if c.PER_CELL else [])
        for t in tests:
            tid, label, sa, sb, ka, kb, lo, hi, dexp, *rest = t
            metric = rest[0] if rest else 'decA'
            r = g.matchup(sa, sb, ka, kb, 'multi', n=n)
            val = r['a'] if metric == 'rawA' else r['decA']
            inband = lo <= val <= hi
            print(f"  {tid:4} {label[:32]:32} A%={r['a']:5.1f} B%={r['b']:5.1f} D%={r['d']:5.1f} {metric}={val:5.1f} band={lo}-{hi} {'OK' if inband else 'OUT'} t={r['t']:4.1f}", flush=True)
        print("--- done ---", flush=True)
    else:
        print("--- diagnostic core (multi) ---", flush=True)
        one('H1', 'Line vs Line (mirror)', 'Line', 'Line', {}, {}, n=n)
        one('H3', 'Envelopment vs Line', g._envelop_army, 'Line', {}, {}, n=n)
        one('H4', 'Envelop vs Arrowhead (Cannae)', g._envelop_army, 'Arrowhead', {}, {}, n=n)
        one('H10', 'Line vs Envelopment (rev H3)', 'Line', g._envelop_army, {}, {}, n=n)
        if c.PER_CELL:
            one('C4', 'Cav envelop vs Line', g._envelop_army, 'Line',
                {'pin_frac': 2/3, 'wing_troop_type': 'cavalry', 'wing_speed': 'Fast'}, {}, n=n)
        print("--- done ---", flush=True)
