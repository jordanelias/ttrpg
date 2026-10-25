import random, sys, json
from multiprocessing import Pool
import lookahead as L, regimes3 as R
SEEDS = range(40)
def job(args):
    lam, seed = args
    ev, ctx = L.simulate_lb(seed, lam)
    M = R.run_metrics(ev, shuf_rng=random.Random(seed + 999))
    M['lev'], M['chg'], M['roll'] = ctx['lev'], ctx['chg'], ctx['roll']
    M['sig_struct'] = M['sig_slot'] = None
    return lam, M
if __name__ == '__main__':
    lams = (0.0, 1.0, 2.0, 4.0)
    with Pool(3) as p:
        out = p.map(job, [(l, s) for l in lams for s in SEEDS], chunksize=1)
    keys = ('arc_all', 'arc_null', 'arc_closed', 'dangling', 'five_node', 'why_linked', 'thread_cont', 'chain_conn', 'depth', 'n_exec', 'viol_any')
    print("lam  " + " ".join(f"{k:>11}" for k in keys) + "   injected  changed/leveraged  rollouts/run")
    for l in lams:
        ms = [m for ll, m in out if ll == l]
        row = [sum(m[k] for m in ms) / len(ms) for k in keys]
        inj = sum(m['injected'] for m in ms)
        chg = sum(m['chg'] for m in ms) / max(1, sum(m['lev'] for m in ms))
        print(f"{l:<4} " + " ".join(f"{x:11.3f}" for x in row) + f"   {inj:8d}  {chg:16.3f}  {sum(m['roll'] for m in ms)/len(ms):12.0f}")
