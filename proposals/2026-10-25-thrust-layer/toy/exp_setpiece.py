"""SET-PIECE DIRECTOR: writes a situation (relocation of the principals + an engagement window, optionally a stake multiplier),
never an outcome.  Predictions registered BEFORE the first run (sha256 in setpiece_pred.sha).  Post hoc to v2; exploratory."""
import random, regimes6 as R
N = 300
def runs(reg, **kw): return [R.simulate(s, reg, **kw)[0] for s in range(N)]
def metrics(evs): return [R.run_metrics(ev, shuf_rng=random.Random(i + 999)) for i, ev in enumerate(evs)]
def mean(ms, k): return sum(m[k] for m in ms) / len(ms)
rng = random.Random(4)
def boot(A, B, k, n=2000):
    xa = [m[k] for m in A]; xb = [m[k] for m in B]
    ds = sorted(sum(rng.choice(xa) for _ in xa) / len(xa) - sum(rng.choice(xb) for _ in xb) / len(xb) for _ in range(n))
    return mean(A, k) - mean(B, k), ds[50 if n == 2000 else int(.025 * n)], ds[1950 if n == 2000 else int(.975 * n)]
def aminn(ms):
    d = [m['arc_all'] - m['arc_null'] for m in ms]
    bs = sorted(sum(rng.choice(d) for _ in d) / len(d) for _ in range(2000)); return sum(d) / len(d), bs[50], bs[1950]
REG = ('BU', 'TDR', 'TDS', 'TDSm', 'HYg3d', 'HYg3s')
if __name__ == '__main__':
    base_ev = {r: runs(r) for r in REG}
    base = {r: metrics(base_ev[r]) for r in REG}
    eng = {r: metrics(runs(r, refuse=0.8)) for r in REG}
    null = {r: metrics(runs(r, A=8, P=8, PR=3)) for r in ('BU', 'TDR', 'TDS', 'TDSm')}
    # outcome openness: who is dead at the end, protagonist vs antagonist (set-piece directors)
    openness = {}
    for r in ('TDR', 'TDS', 'TDSm'):
        pk = ak = nk = 0
        for s in range(N):
            R.simulate(s, r); W = R.LAST; d = W.dir
            pa, qa = W.alive[d['p']], W.alive[d['q']]
            pk += (not pa and qa); ak += (pa and not qa); nk += (pa and qa)
        openness[r] = (pk / N, ak / N, nk / N)
    pert = {}
    for r in ('BU', 'TDR', 'TDS', 'TDSm'):
        vp = []
        for s in range(N):
            ev, _ = R.simulate(s, r, perturb_t=10); vp.append(1 if sum(R.violations(ev, 10).values()) else 0)
        pert[r] = sum(vp) / N
    print("== base (N=300)")
    print("regime  arc_all arc_null  arc-null[CI]            closed dangling five_node why_linked thread_cont  inj dir_writes engaged_in_sel peak_mag")
    for r in REG:
        ms = base[r]; a = aminn(ms)
        inj = sum(1 for m in ms if m['injected'] > 0) / N
        eis = sum(1 for ev in base_ev[r] for e in R.select(ev) if e.get('engaged')) / max(1, sum(len(R.select(ev)) for ev in base_ev[r]))
        print(f"{r:6} {mean(ms,'arc_all'):7.3f} {mean(ms,'arc_null'):8.3f}  {a[0]:+.3f} [{a[1]:+.3f},{a[2]:+.3f}] {mean(ms,'arc_closed'):6.3f} {mean(ms,'dangling'):8.3f} {mean(ms,'five_node'):9.3f} {mean(ms,'why_linked'):10.3f} {mean(ms,'thread_cont'):11.3f} {inj:5.2f} {mean(ms,'director_writes'):9.1f} {eis:14.3f} {mean(ms,'peak_mag'):8.2f}")
    print("\n== contrasts (diff, 95% CI)")
    for a, b, k in (('TDS', 'BU', 'arc_all'), ('TDSm', 'TDS', 'arc_all'), ('TDR', 'TDS', 'arc_all'), ('TDR', 'TDS', 'five_node'), ('HYg3s', 'HYg3d', 'arc_all'), ('HYg3s', 'TDS', 'arc_all'), ('HYg3s', 'HYg3d', 'why_linked'), ('TDS', 'HYg3d', 'arc_all')):
        d, lo, hi = boot(base[a], base[b], k); print(f"  {a}-{b} {k:10} {d:+.3f} [{lo:+.3f},{hi:+.3f}]", "" if lo > 0 or hi < 0 else "(CI spans 0)")
    print("\n== 80% refusal")
    for r in REG:
        a = aminn(eng[r]); print(f"  {r:6} arc_all {mean(eng[r],'arc_all'):.3f}  arc-null {a[0]:+.3f} [{a[1]:+.3f},{a[2]:+.3f}]")
    print("\n== quiet world (A=8): main-thread peak magnitude", {r: round(mean(null[r], 'peak_mag'), 2) for r in null})
    print("\n== outcome openness at end of run (P(protagonist dead only), P(antagonist dead only), P(both alive)):", {r: tuple(round(x, 2) for x in v) for r, v in openness.items()})
    print("\n== violations after killing the protagonist at season 10:", {r: round(v, 2) for r, v in pert.items()})
    # predictions
    ctx = dict(base=base, eng=eng, null=null, open=openness, pert=pert)
    P = [
     ("S1", "Outcomes stay open under TDS: P(protagonist dead only) >= 0.10, P(antagonist dead only) >= 0.10, P(both alive) >= 0.25",
      lambda: openness['TDS'][0] >= 0.10 and openness['TDS'][1] >= 0.10 and openness['TDS'][2] >= 0.25),
     ("S2", "TDS keeps an ordering signal: arc_all - arc_null >= +0.03 for TDS",
      lambda: aminn(base['TDS'])[0] >= 0.03),
     ("S3", "Open outcomes cost arcs: arc_all(TDS) <= arc_all(TDR) - 0.10",
      lambda: mean(base['TDS'], 'arc_all') <= mean(base['TDR'], 'arc_all') - 0.10),
     ("S4", "Open outcomes cost beats: five_node(TDS) <= five_node(TDR) - 0.20",
      lambda: mean(base['TDS'], 'five_node') <= mean(base['TDR'], 'five_node') - 0.20),
     ("S5", "No forced outcome and no constraint violation in any set-piece arm, perturbed or not",
      lambda: all(sum(1 for m in base[r] if m['injected'] > 0) == 0 and mean(base[r], 'viol_any') == 0 for r in ('TDS', 'TDSm', 'HYg3s')) and pert['TDS'] == 0 and pert['TDSm'] == 0),
     ("S6", "The stake multiplier buys arcs but fakes intensity: arc_all(TDSm) >= arc_all(TDS) + 0.05 AND quiet-world peak_mag(TDSm) >= 2x BU while TDS < 1.5x BU",
      lambda: mean(base['TDSm'], 'arc_all') >= mean(base['TDS'], 'arc_all') + 0.05 and mean(null['TDSm'], 'peak_mag') >= 2 * mean(null['BU'], 'peak_mag') and mean(null['TDS'], 'peak_mag') < 1.5 * mean(null['BU'], 'peak_mag')),
     ("S7", "Under 80% refusal the TDS arc gain over BU is at most half its base gain (set pieces still need the dice)",
      lambda: (mean(eng['TDS'], 'arc_all') - mean(eng['BU'], 'arc_all')) <= 0.5 * (mean(base['TDS'], 'arc_all') - mean(base['BU'], 'arc_all'))),
     ("S8", "Set pieces add no standing motive: why_linked(TDS) < 0.35",
      lambda: mean(base['TDS'], 'why_linked') < 0.35),
     ("S9", "Ladder + set pieces beats set pieces alone on the ordering signal and keeps the 'why': arc-null(HYg3s) > arc-null(TDS) and why_linked(HYg3s) >= 0.55",
      lambda: aminn(base['HYg3s'])[0] > aminn(base['TDS'])[0] and mean(base['HYg3s'], 'why_linked') >= 0.55),
    ]
    print("\n== PREDICTIONS (registered before the first run)")
    ok = 0
    for id, claim, fn in P:
        v = bool(fn()); ok += v; print(f"[{'CONFIRMED' if v else 'FALSIFIED'}] {id}: {claim}")
    print(f"{ok}/{len(P)} confirmed")
