#!/usr/bin/env python3
import json, random, statistics as st, sys
from collections import Counter
import regimes as R
import predictions as PR

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
REG = ('BU', 'TD', 'TDR', 'HY')
CONDS = {
    'base': dict(),
    'noent': dict(entrench=0),
    'engine': dict(refuse=0.8),
    'small': dict(A=12, P=10, PR=4),
    'null': dict(A=8, P=8, PR=3),
}


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else 0.0


def agg(ms):
    out = {}
    keys = [k for k in ms[0] if k not in ('main_ref', 'sig_struct', 'sig_slot', 'tp', 'gap_cv')]
    for k in keys:
        out[k] = mean([m.get(k) for m in ms])
    out['injected_any'] = mean([1 if m['injected'] > 0 else 0 for m in ms])
    gv = [m['gap_cv'] for m in ms if m['gap_cv'] is not None]
    out['gap_cv_med'] = st.median(gv) if gv else float('nan')
    tps = [m['tp'] for m in ms if m['tp'] is not None]
    out['tp_std'] = st.pstdev(tps) if len(tps) > 1 else 0.0
    ds, dl = len(set(m['sig_struct'] for m in ms)), len(set(m['sig_slot'] for m in ms))
    out['R_oat'] = ds / dl if dl else 0.0
    out['n_struct'] = ds; out['n_slot'] = dl
    return out


def runset(regime, cfg, **kw):
    ms = []
    for seed in range(N):
        ev, _ = R.simulate(seed, regime, **cfg, **kw)
        ms.append(R.run_metrics(ev, T=cfg.get('T', R.T_DEF), shuf_rng=random.Random(seed + 999)))
    return ms


A = {}
for c, cfg in CONDS.items():
    A[c] = {r: agg(runset(r, cfg)) for r in REG}

# --- perturbation
A['pert'] = {}
for r in REG:
    vp, ap, apv, killed = [], [], [], 0
    for seed in range(N):
        ev, victim = R.simulate(seed, r, perturb_t=10)
        killed += 1 if victim is not None else 0
        v = 1 if sum(R.violations(ev, 10).values()) else 0
        ex = [e for e in R.executed(ev) if e['t'] >= 10]
        mr = R.main_ref(ex)
        arc = 1 if (mr and R.arc_test(ex, mr, 10, R.T_DEF)['all']) else 0
        vp.append(v); ap.append(arc); apv.append(1 if (arc and v) else 0)
    A['pert'][r] = dict(viol_post_any=mean(vp), arc_post=mean(ap), kill_applied=killed / N,
                        arc_post_viol_share=(sum(apv) / sum(ap)) if sum(ap) else 0.0)

# --- dose, ablations, control
A['dose'] = {}
for w in (0.0, 0.25, 0.5, 0.75, 1.0):
    A['dose'][w] = agg(runset('HY', {}, w=w))
A['abl'] = {'noocc': agg(runset('HY', {}, occ=False)), 'nolife': agg(runset('HY', {}, life=False)),
            'neither': agg(runset('HY', {}, occ=False, life=False))}
eq = 0
for seed in range(N):
    a, _ = R.simulate(seed, 'BU'); b, _ = R.simulate(seed, 'HY', w=0.0, occ=False, life=False)
    eq += 1 if R.log_hash(a) == R.log_hash(b) else 0
A['ctl'] = dict(equal=eq, n=N)

json.dump({str(k): v for k, v in A.items()}, open('results.json', 'w'), indent=1, default=str)

# ----------------------------------------------------------------------------- report
def row(cond, keys):
    print(f"{'':6}" + "".join(f"{k:>14}" for k in keys))
    for r in REG:
        print(f"{r:6}" + "".join(f"{A[cond][r][k]:14.3f}" for k in keys))

print(f"N={N} seeds/regime/condition, T={R.T_DEF}\n")
for title, keys in (("LEGIBILITY", ['leg_apparent', 'leg_grounded', 'why_linked', 'leg_grounded_raw']),
                    ("COHERENCY", ['thread_cont', 'chain_conn', 'viol_any', 'injected_any']),
                    ("ARC", ['arc_rise', 'arc_peak', 'arc_fall', 'arc_all', 'arc_null', 'arc_closed', 'arc_any3', 'dangling']),
                    ("BEATS/NODES", ['five_node', 'gap_cv_med', 'conv', 'dead', 'depth', 'n_sel', 'n_exec']),
                    ("DIVERSITY", ['R_oat', 'n_struct', 'n_slot', 'tp_std', 'peak_mag'])):
    print(f"== {title} (base)"); row('base', keys); print()
print("== PERTURBATION (kill at t=10)")
for r in REG:
    print(r, {k: round(v, 3) for k, v in A['pert'][r].items()})
print("\n== DOSE (HY, w_amb)")
for w in sorted(A['dose']):
    d = A['dose'][w]; print(w, {k: round(d[k], 3) for k in ('why_linked', 'arc_all', 'arc_null', 'arc_closed', 'thread_cont', 'leg_grounded')})
print("\n== ABLATION (HY)");
for n, d in A['abl'].items():
    print(n, {k: round(d[k], 3) for k in ('why_linked', 'arc_all', 'arc_closed', 'thread_cont', 'dead')})
print("HY full", {k: round(A['base']['HY'][k], 3) for k in ('why_linked', 'arc_all', 'arc_closed', 'thread_cont', 'dead')})
print("\n== CONDITION SWEEP (arc_all / arc_null / why_linked / leg_grounded)")
for c in CONDS:
    print(c, {r: tuple(round(A[c][r][k], 2) for k in ('arc_all', 'arc_null', 'why_linked', 'leg_grounded')) for r in REG})
print("\n== CONTROL", A['ctl'])
print("\n== PRE-REGISTERED PREDICTIONS")
npass = 0
for id, claim, fn in PR.P:
    ok, ev = fn(A); npass += ok
    print(f"[{'CONFIRMED' if ok else 'FALSIFIED'}] {id}: {claim}\n            {ev}")
print(f"\n{npass}/{len(PR.P)} confirmed")
