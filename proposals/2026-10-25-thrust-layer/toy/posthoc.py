# POST-HOC (exploratory, run after v2): HYc arm, bootstrap CIs, director templating, sifting availability.
import random, regimes2 as R
from collections import Counter
N=300; T=R.T_DEF
def runs(reg, **kw):
    return [R.run_metrics(R.simulate(s,reg,**kw)[0], shuf_rng=random.Random(s+999)) for s in range(N)]
M={r:runs(r) for r in ('BU','TD','TDR','HY','HYc')}
rng=random.Random(7)
def boot(a,b,key,n=2000):
    xa=[m[key] for m in M[a] if m.get(key) is not None]; xb=[m[key] for m in M[b] if m.get(key) is not None]
    ds=sorted(sum(rng.choice(xa) for _ in xa)/len(xa)-sum(rng.choice(xb) for _ in xb)/len(xb) for _ in range(n))
    return sum(xa)/len(xa)-sum(xb)/len(xb), ds[int(.025*n)], ds[int(.975*n)]
print("regime means: arc_all arc_null arc_closed dangling why_linked five_node thread_cont dead")
for r in M:
    f=lambda k: sum(m[k] for m in M[r])/len(M[r])
    print(f"{r:4}", *[f"{f(k):.3f}" for k in ('arc_all','arc_null','arc_closed','dangling','why_linked','five_node','thread_cont','dead')])
print("\nbootstrap 95% CI of difference (A - B)")
for a,b,k in [('TD','BU','arc_all'),('TDR','BU','arc_all'),('HY','BU','arc_all'),('HYc','BU','arc_all'),('HYc','HY','arc_all'),('HYc','HY','arc_closed'),('HYc','HY','dangling'),('HY','BU','why_linked'),('HYc','BU','why_linked'),('TDR','BU','five_node'),('TD','BU','five_node'),('HYc','BU','five_node'),('HY','BU','thread_cont'),('HYc','BU','thread_cont')]:
    d,lo,hi=boot(a,b,k); print(f"{a:4}-{b:3} {k:12} {d:+.3f}  [{lo:+.3f},{hi:+.3f}]", "" if lo>0 or hi<0 else "  (CI spans 0)")
print("\narc_all - arc_null:", {r: round(sum(m['arc_all']-m['arc_null'] for m in M[r])/N,3) for r in M})
for r in ('TD','TDR'):
    sig=set(); slot=set()
    for seed in range(N):
        ev,_=R.simulate(seed,r)
        sig.add(tuple((e['verb'],round(e['delta'])) for e in ev if e['forced'] and e['delta']>0))
        slot.add(tuple((e['verb'],round(e['delta']),e['actor'],e['target']) for e in ev if e['forced'] and e['delta']>0))
    print(r,'forced-beat signatures: structural distinct',len(sig),'slot distinct',len(slot),'of',N,'runs')
def available(ex):
    mass=Counter()
    for e in ex: mass[e['thread']]+=e['delta']
    for th,_ in mass.most_common(6):
        if sum(1 for e in ex if e['thread']==th)<5: continue
        for lo in range(0,T-8+1):
            for hi in range(lo+8,T+1):
                if R.arc_test(ex,th,lo,hi)['all']: return 1
    return 0
print("\nSIFTING availability (any thread among top-6, any window >=8 seasons, satisfies the arc test)")
for reg in ('BU','TD','TDR','HY','HYc'):
    real=[];null=[]
    for seed in range(N):
        ex=R.executed(R.simulate(seed,reg)[0]); real.append(available(ex))
        rg=random.Random(seed+31); null.append(sum(available(R.shuffled(ex,rg)) for _ in range(2))/2)
    print(reg,'real %.3f  shuffled-null %.3f  diff %+.3f'%(sum(real)/N,sum(null)/N,(sum(real)-sum(null))/N))
