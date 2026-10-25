"""Hierarchical ambition: overall thrust (ambition) decomposed into a LADDER of short/medium goals ending in the long goal.
Predictions below were written BEFORE this script was first run (sha256 in ladder_pred.sha).  Exploratory, post hoc to v2."""
import random, regimes5 as R
N = 300
PRED = [
 ("H1", "Ladder gives closure/escalation: arc_all(HYg3) >= arc_all(HY) + 0.10 with the bootstrap CI excluding 0",
  lambda c: c['d']('HYg3','HY','arc_all')[1] > 0 and c['d']('HYg3','HY','arc_all')[0] >= 0.10),
 ("H2", "Depth dose: arc_all(HYg1) <= arc_all(HYg2) + 0.02 and arc_all(HYg2) <= arc_all(HYg3) + 0.02",
  lambda c: c['m']('HYg1','arc_all') <= c['m']('HYg2','arc_all')+0.02 and c['m']('HYg2','arc_all') <= c['m']('HYg3','arc_all')+0.02),
 ("H3", "No injection and no constraint violations in any ladder arm",
  lambda c: all(c['m'](r,'injected_any')==0 and c['m'](r,'viol_any')==0 for r in ('HYg1','HYg2','HYg3'))),
 ("H4", "Ordering signal beyond chance: arc_all - arc_null for HYg3 >= +0.05",
  lambda c: c['m']('HYg3','arc_all')-c['m']('HYg3','arc_null') >= 0.05),
 ("H5", "Motive depth preserved: why_linked(HYg3) >= 0.70",
  lambda c: c['m']('HYg3','why_linked') >= 0.70),
 ("H6", "Refusal-heavy substrate (80%): the HYg3-BU arc gain is smaller than at base",
  lambda c: c['e']('HYg3','BU','arc_all')[0] < c['d']('HYg3','BU','arc_all')[0]),
 ("H7", "Complete beats: five_node(HYg3) >= five_node(HY) + 0.15",
  lambda c: c['m']('HYg3','five_node') >= c['m']('HY','five_node')+0.15),
]
if __name__ == '__main__':
    import sys
    REG = ('BU','TDR','HY','HYd','HYg1','HYg2','HYg3')
    def runs(reg, **kw): return [R.run_metrics(R.simulate(s,reg,**kw)[0], shuf_rng=random.Random(s+999)) for s in range(N)]
    base = {r: runs(r) for r in REG}
    eng = {r: runs(r, refuse=0.8) for r in REG}
    rng = random.Random(5)
    def mean(ms,k):
        xs=[m[k] for m in ms if m.get(k) is not None]; return sum(xs)/len(xs)
    def boot(S,a,b,k,n=2000):
        xa=[m[k] for m in S[a]]; xb=[m[k] for m in S[b]]
        ds=sorted(sum(rng.choice(xa) for _ in xa)/len(xa)-sum(rng.choice(xb) for _ in xb)/len(xb) for _ in range(n))
        return (sum(xa)/len(xa)-sum(xb)/len(xb), ds[int(.025*n)], ds[int(.975*n)])
    ctx = dict(m=lambda r,k: (sum(1 for m in base[r] if m['injected']>0)/N) if k=='injected_any' else mean(base[r],k),
               d=lambda a,b,k: (lambda t:(t[0],t[1],t[2]))(boot(base,a,b,k)) if False else (lambda t:(t[0],t[1]))(boot(base,a,b,k)),
               e=lambda a,b,k: (lambda t:(t[0],t[1]))(boot(eng,a,b,k)))
    for name,S in (('base',base),('engine (80% refusal)',eng)):
        print('==',name)
        print('regime   arc_all arc_null  closed dangling why_linked five_node thread_cont  n_exec  fired/goal_met n/a')
        for r in REG:
            f=lambda k: mean(S[r],k)
            print(f"{r:6} {f('arc_all'):8.3f} {f('arc_null'):8.3f} {f('arc_closed'):7.3f} {f('dangling'):8.3f} {f('why_linked'):10.3f} {f('five_node'):9.3f} {f('thread_cont'):11.3f} {f('n_exec'):7.0f}")
        for a,b,k in (('HYg3','BU','arc_all'),('HYg3','HY','arc_all'),('HYg3','HY','arc_closed'),('HYg3','HY','five_node'),('HYg3','HYd','arc_all'),('TDR','HYg3','arc_all'),('HYg2','HY','arc_all'),('HYg1','HY','arc_all')):
            d,lo,hi=boot(S,a,b,k); print(f"  {a}-{b} {k:10} {d:+.3f} [{lo:+.3f},{hi:+.3f}]", "" if lo>0 or hi<0 else "(CI spans 0)")
        print("  arc_all - arc_null:", {r: round(sum(m['arc_all']-m['arc_null'] for m in S[r])/N,3) for r in REG})
    print("\n== PREDICTIONS (pre-registered before the first run)")
    ok=0
    for id,claim,fn in PRED:
        try: v=bool(fn(ctx))
        except Exception as ex: v=False; claim+=f" [check error {ex}]"
        ok+=v; print(f"[{'CONFIRMED' if v else 'FALSIFIED'}] {id}: {claim}")
    print(f"{ok}/{len(PRED)} confirmed")
