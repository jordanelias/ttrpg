import itertools
from fractions import Fraction as F

# per-die success distribution: 0 succ w.p. 6/10, 1 succ w.p. 3/10, 2 succ w.p. 1/10
die = {0: F(6,10), 1: F(3,10), 2: F(1,10)}

def pool_dist(n):
    dist = {0: F(1)}
    for _ in range(n):
        newdist = {}
        for s, p in dist.items():
            for ds, dp in die.items():
                newdist[s+ds] = newdist.get(s+ds, F(0)) + p*dp
        dist = newdist
    return dist

def mean_var(dist):
    mean = sum(F(k)*p for k,p in dist.items())
    var = sum(F(k)*F(k)*p for k,p in dist.items()) - mean*mean
    return mean, var

for n in [3,4,5,6,7,8,9,10,11,12,13,14]:
    d = pool_dist(n)
    m,v = mean_var(d)
    print(n, "mean=%.3f"%m, "sd=%.3f"%(float(v)**0.5))

print()
print("=== Full distribution for pool sizes 4,6,8,10,12 ===")
for n in [4,6,8,10,12]:
    d = pool_dist(n)
    print(f"--- pool {n} ---")
    for s in sorted(d):
        if d[s] > F(1,100000):
            print(f"  successes={s:2d}  p={float(d[s]):.4f}")

print()
print("=== Obstacle-roll: P(margin band) for pool N vs obstacle O ===")
def band(m):
    if m <= -2: return "Disaster"
    if m == -1: return "Failure"
    if m == 0: return "Costed Success"
    if m in (1,2): return "Clean Success"
    return "Overwhelming"

for n,o in [(4,2),(6,3),(8,4),(10,5),(12,6),(6,2),(6,5),(8,2),(8,7),(14,7)]:
    d = pool_dist(n)
    bandp = {}
    for s,p in d.items():
        m = s-o
        b = band(m)
        bandp[b] = bandp.get(b, F(0)) + p
    print(f"pool={n:2d} obstacle={o:2d}  " + "  ".join(f"{b}={float(p)*100:.1f}%" for b,p in bandp.items()))

print()
print("=== Opposed contest: P(A wins by band) pool A vs pool B ===")
def opposed_bands(nA, nB):
    dA = pool_dist(nA)
    dB = pool_dist(nB)
    bandp = {}
    for sa,pa in dA.items():
        for sb,pb in dB.items():
            m = sa-sb
            b = band(m)
            bandp[b] = bandp.get(b, F(0)) + pa*pb
    return bandp

for nA,nB in [(8,8),(10,8),(10,6),(12,6),(12,4),(14,4),(6,6),(8,4)]:
    bp = opposed_bands(nA,nB)
    total_Awin = sum(p for b,p in bp.items() if b in ("Clean Success","Overwhelming"))
    print(f"A={nA:2d} vs B={nB:2d}: " + "  ".join(f"{b}={float(p)*100:.1f}%" for b,p in bp.items()))

print()
print("=== extremes: max-competence vs trivial obstacle (Disaster still reachable?) ===")
for n,o in [(14,2),(16,2),(20,3)]:
    d = pool_dist(n)
    bandp = {}
    for s,p in d.items():
        m = s-o
        b = band(m)
        bandp[b] = bandp.get(b, F(0)) + p
    print(f"pool={n:2d} obstacle={o:2d}  " + "  ".join(f"{b}={float(p)*100:.2f}%" for b,p in bandp.items()))

print()
print("=== extremes: min competence vs hard obstacle (Overwhelming still reachable?) ===")
for n,o in [(3,6),(3,8),(4,9)]:
    d = pool_dist(n)
    bandp = {}
    for s,p in d.items():
        m = s-o
        b = band(m)
        bandp[b] = bandp.get(b, F(0)) + p
    print(f"pool={n:2d} obstacle={o:2d}  " + "  ".join(f"{b}={float(p)*100:.3f}%" for b,p in bandp.items()))
