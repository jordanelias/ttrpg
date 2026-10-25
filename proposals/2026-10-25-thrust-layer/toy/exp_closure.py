# POST-HOC, exploratory: does a threshold-forced, decider-closed moment (the corpus' dominant closure mode) produce arcs?
import random, regimes3 as R
N=300
def runs(reg, **kw): return [R.run_metrics(R.simulate(s,reg,**kw)[0], shuf_rng=random.Random(s+999)) for s in range(N)]
rng=random.Random(11)
def boot(A,B,key,n=2000):
    xa=[m[key] for m in A if m.get(key) is not None]; xb=[m[key] for m in B if m.get(key) is not None]
    ds=sorted(sum(rng.choice(xa) for _ in xa)/len(xa)-sum(rng.choice(xb) for _ in xb)/len(xb) for _ in range(n))
    return sum(xa)/len(xa)-sum(xb)/len(xb), ds[int(.025*n)], ds[int(.975*n)]
for cond,kw in (('base',{}),('engine(80% refusal)',dict(refuse=0.8))):
    M={r:runs(r,**kw) for r in ('BU','TDR','HY','HYd')}
    print("==",cond)
    print("regime  arc_all arc_null  closed dangling why_linked five_node injected_any")
    for r in M:
        f=lambda k: sum(m[k] for m in M[r])/N
        inj=sum(1 for m in M[r] if m['injected']>0)/N
        print(f"{r:5} {f('arc_all'):8.3f} {f('arc_null'):8.3f} {f('arc_closed'):7.3f} {f('dangling'):8.3f} {f('why_linked'):10.3f} {f('five_node'):9.3f} {inj:12.3f}")
    for a,b,k in (('HYd','BU','arc_all'),('HYd','HY','arc_all'),('HYd','HY','arc_closed'),('HYd','HY','dangling'),('TDR','HYd','arc_all'),('HYd','BU','five_node')):
        d,lo,hi=boot(M[a],M[b],k); print(f"  {a}-{b} {k:10} {d:+.3f} [{lo:+.3f},{hi:+.3f}]", "" if lo>0 or hi<0 else "(CI spans 0)")
    print("  HYd arc_all - arc_null:", round(sum(m['arc_all']-m['arc_null'] for m in M['HYd'])/N,3))
# how often did the machinery fire?
fired=0; asked=0
for s in range(N):
    ev,_=R.simulate(s,'HYd'); asked+=sum(1 for e in ev if e['verb']=='summon' and e['thread'] and e['thread'].startswith('T')); fired+=sum(1 for e in ev if e['verb']=='rule')
print("tribunals raised per run %.2f, ruled per run %.2f"%(asked/N,fired/N))
