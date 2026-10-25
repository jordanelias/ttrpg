import random
from multiprocessing import Pool
import lookahead as L, regimes3 as R
def job(a):
    lam, seed = a
    ev, ctx = L.simulate_lb(seed, lam)
    M = R.run_metrics(ev, shuf_rng=random.Random(seed + 999))
    return lam, {k: M[k] for k in ('arc_all','arc_null','arc_closed','dangling','five_node','why_linked','depth','n_exec','injected','viol_any')} | dict(lev=ctx['lev'], chg=ctx['chg'], roll=ctx['roll'])
if __name__ == '__main__':
    seeds = range(120)
    with Pool(4) as p:
        out = p.map(job, [(l, s) for l in (0.0, 4.0) for s in seeds], chunksize=1)
    rng = random.Random(1)
    A = [m for l, m in out if l == 0.0]; B = [m for l, m in out if l == 4.0]
    n = len(A)
    def mean(ms, k): return sum(m[k] for m in ms) / len(ms)
    print("N =", n, "seeds per arm (0-39 overlap the earlier 40-seed sweep)")
    for k in ('arc_all','arc_null','arc_closed','dangling','five_node','why_linked','depth','n_exec'):
        xa = [m[k] for m in A]; xb = [m[k] for m in B]
        ds = sorted(sum(rng.choice(xb) for _ in xb)/n - sum(rng.choice(xa) for _ in xa)/n for _ in range(2000))
        print(f"{k:11} lam0 {mean(A,k):7.3f}  lam4 {mean(B,k):7.3f}  diff {mean(B,k)-mean(A,k):+7.3f} [{ds[50]:+.3f},{ds[1950]:+.3f}]")
    d = [m['arc_all'] - m['arc_null'] for m in B]; bs = sorted(sum(rng.choice(d) for _ in d)/n for _ in range(2000))
    print("lam4 arc_all - arc_null = %+.3f [%+.3f,%+.3f]" % (sum(d)/n, bs[50], bs[1950]))
    print("injected total:", sum(m['injected'] for m in B), "| violations rate:", mean(B,'viol_any'),
          "| changed/leveraged: %.3f" % (sum(m['chg'] for m in B)/sum(m['lev'] for m in B)),
          "| leveraged decisions per run: %.0f" % (sum(m['lev'] for m in B)/n), "| rollouts per run: %.0f" % (sum(m['roll'] for m in B)/n))
