"""CONCLUSIVE-FORM SET PIECES: the director authors the form (a best-of contest at a venue, decisive, lethal at the climax) and the
stakes of losing; the winner is the dice's and the principals' skill's.  Predictions registered BEFORE the first run (setpiece2_pred.sha)."""
import random, regimes7 as R
N = 300
def runs(reg, **kw): return [R.simulate(s, reg, **kw)[0] for s in range(N)]
def metrics(evs): return [R.run_metrics(ev, shuf_rng=random.Random(i + 999)) for i, ev in enumerate(evs)]
def mean(ms, k): return sum(m[k] for m in ms) / len(ms)
rng = random.Random(8)
def boot(A, B, k, n=2000):
    xa = [m[k] for m in A]; xb = [m[k] for m in B]
    ds = sorted(sum(rng.choice(xa) for _ in xa) / len(xa) - sum(rng.choice(xb) for _ in xb) / len(xb) for _ in range(n))
    return mean(A, k) - mean(B, k), ds[50], ds[1950]
def aminn(ms):
    d = [m['arc_all'] - m['arc_null'] for m in ms]
    bs = sorted(sum(rng.choice(d) for _ in d) / len(d) for _ in range(2000)); return sum(d) / len(d), bs[50], bs[1950]
REG = ('BU', 'TDR', 'TDSc', 'TDScf', 'HYg3c', 'HYg3d')
if __name__ == '__main__':
    base = {r: metrics(runs(r)) for r in REG}
    eng = {r: metrics(runs(r, refuse=0.8)) for r in REG}
    null = {r: metrics(runs(r, A=8, P=8, PR=3)) for r in ('BU', 'TDR', 'TDSc', 'TDScf')}
    win = {}
    for r in ('TDSc', 'HYg3c'):
        pw = n = 0
        for s in range(N):
            ev, _ = R.simulate(s, r); W = R.LAST
            c = [e for e in ev if e['verb'] == 'contest' and e['t'] >= 21]
            if c:
                n += 1; pw += (c[-1]['actor'] == W.dir['p'])
        win[r] = (pw / n, n)
    pert = {}
    for r in ('BU', 'TDR', 'TDSc', 'HYg3c'):
        vp = []; ap = []
        for s in range(N):
            ev, _ = R.simulate(s, r, perturb_t=10); vp.append(1 if sum(R.violations(ev, 10).values()) else 0)
        pert[r] = sum(vp) / N
    print("== base (N=300)")
    print("regime  arc_all arc_null  arc-null[CI]            closed dangling five_node why_linked thread_cont  inj  peak_mag")
    for r in REG:
        ms = base[r]; a = aminn(ms); inj = sum(1 for m in ms if m['injected'] > 0) / N
        print(f"{r:6} {mean(ms,'arc_all'):7.3f} {mean(ms,'arc_null'):8.3f}  {a[0]:+.3f} [{a[1]:+.3f},{a[2]:+.3f}] {mean(ms,'arc_closed'):6.3f} {mean(ms,'dangling'):8.3f} {mean(ms,'five_node'):9.3f} {mean(ms,'why_linked'):10.3f} {mean(ms,'thread_cont'):11.3f} {inj:5.2f} {mean(ms,'peak_mag'):8.2f}")
    print("\n== contrasts (diff, 95% CI)")
    for a, b, k in (('TDSc', 'BU', 'arc_all'), ('TDSc', 'TDR', 'arc_all'), ('TDSc', 'TDScf', 'arc_all'), ('TDSc', 'HYg3d', 'arc_all'), ('HYg3c', 'TDSc', 'arc_all'), ('HYg3c', 'TDSc', 'why_linked'), ('HYg3c', 'HYg3d', 'arc_all'), ('TDSc', 'TDR', 'five_node')):
        d, lo, hi = boot(base[a], base[b], k); print(f"  {a}-{b} {k:10} {d:+.3f} [{lo:+.3f},{hi:+.3f}]", "" if lo > 0 or hi < 0 else "(CI spans 0)")
    print("\n== 80% refusal")
    for r in REG:
        a = aminn(eng[r]); print(f"  {r:6} arc_all {mean(eng[r],'arc_all'):.3f}  arc-null {a[0]:+.3f} [{a[1]:+.3f},{a[2]:+.3f}]")
    print("\n== quiet world (A=8) main-thread peak magnitude:", {r: round(mean(null[r], 'peak_mag'), 2) for r in null})
    print("== P(protagonist wins the climax contest) [n runs with a climax]:", win)
    print("== violations after killing the protagonist at season 10:", pert)
    P = [
     ("C1", "Winner stays open: P(protagonist wins climax) in [0.25, 0.75] for TDSc", lambda: 0.25 <= win['TDSc'][0] <= 0.75),
     ("C2", "Ordering signal restored: arc_all - arc_null >= +0.05 for TDSc", lambda: aminn(base['TDSc'])[0] >= 0.05),
     ("C3", "Close to the forcing director: arc_all(TDSc) >= arc_all(TDR) - 0.10", lambda: mean(base['TDSc'], 'arc_all') >= mean(base['TDR'], 'arc_all') - 0.10),
     ("C4", "Complete beats: five_node(TDSc) >= 0.50", lambda: mean(base['TDSc'], 'five_node') >= 0.50),
     ("C5", "No standing motive: why_linked(TDSc) < 0.35", lambda: mean(base['TDSc'], 'why_linked') < 0.35),
     ("C6", "Form survives a refusing substrate: arc_all(TDSc) >= 0.50 at 80% refusal", lambda: mean(eng['TDSc'], 'arc_all') >= 0.50),
     ("C7", "Authored stakes fake intensity in a quiet world: peak_mag(TDSc) >= 2x BU", lambda: mean(null['TDSc'], 'peak_mag') >= 2 * mean(null['BU'], 'peak_mag')),
     ("C8", "Escalating stakes matter: arc_all(TDSc) >= arc_all(TDScf) + 0.05", lambda: mean(base['TDSc'], 'arc_all') >= mean(base['TDScf'], 'arc_all') + 0.05),
     ("C9", "No violations after killing the protagonist (TDSc, HYg3c)", lambda: pert['TDSc'] == 0 and pert['HYg3c'] == 0),
     ("C10", "Ladder + contest set pieces keep the 'why' (>= 0.55) and match TDSc on ordering signal (within 0.03)", lambda: mean(base['HYg3c'], 'why_linked') >= 0.55 and aminn(base['HYg3c'])[0] >= aminn(base['TDSc'])[0] - 0.03),
    ]
    print("\n== PREDICTIONS (registered before the first run)")
    ok = 0
    for id, claim, fn in P:
        v = bool(fn()); ok += v; print(f"[{'CONFIRMED' if v else 'FALSIFIED'}] {id}: {claim}")
    print(f"{ok}/{len(P)} confirmed")
