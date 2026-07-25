"""[ED-MB-0041] Is 20/20 reachable by CONSTANTS at all? — a per-row reachability sweep.

The question this answers is not "which settings score best" but the prior one: **for each failing
gauge row, does ANY setting of the engine's toggles move it into its band?** A row that is invariant
to every toggle, or that cannot reach its band under any of them, is blocked by STRUCTURE — a missing
or broken mechanism — and no amount of constant-fitting will pass it. Distinguishing those two classes
is what stops a tuning pass from being an infinite search.

Method: one subprocess per (row, config) so `mass_battle.config` re-reads the environment cleanly
(every toggle is an import-time `os.environ.get`). Per-row, not per-battery, so the cost is tractable
and a row's own sensitivity is isolated from the others'.

Usage:
    python audit/2026-07-22-mass-battle-stress-test/reachability_sweep.py [--n 30] [--rows H4,H5,...]
"""
import argparse
import json
import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SIM = os.path.join(REPO, 'tests', 'sim')

# The gated PC_* booleans (12 of 33 default OFF) plus the load-bearing ones the flag audit flagged.
# Each entry is a single-toggle perturbation from the shipped default.
TOGGLES = [
    'PC_CELL_DAMAGE', 'PC_STOCHASTIC_ROUT', 'PC_FRICTION_CEV', 'PC_INTENT_RESOLUTION',
    'PC_FEIGNED_RETREAT', 'PC_YIELD_EMERGENT', 'PC_YIELD_RALLY', 'PC_YIELD_POCKET',
    'PC_CLOSE_RANKS', 'PC_RESERVE_COMMIT', 'PC_TROOP_DENSITY_CAP', 'PC_FRACTIONAL_POOL',
    'PC_WHEEL', 'PC_OCTAGON_DMG', 'PC_BRACE_ENABLED', 'PC_RECOIL_FRONTAL',
    'PC_RECOIL_CHARGER_GATE', 'PC_ENVELOP_PATH', 'PC_REFUSE', 'PC_ENVELOP_SHOCK',
    'PC_CONVERGENCE_NORM', 'PC_FACING_MODEL', 'PC_FACING_ATTENTION', 'PC_FACING_ROUT',
    'PC_DEPTH_ROTATE', 'PC_KITE_ENABLED', 'LANCHESTER_ENABLED', 'SIGMA_HEAD_ENABLED',
    'COMMAND_SIGMA_ENABLED', 'CASCADING_ENABLED', 'SUPPORT_STACK_ENABLED', 'PUNCTURE_ENABLED',
    'TIP_SUPPORT_ENABLED',
]

# A few magnitudes the audit named as live levers, swept at their extremes rather than fitted.
MAGNITUDES = {
    'PC_CHARGE_RECOIL': ['0', '3', '12', '24'],
    'SIGMA_PER_D': ['0.1', '0.4', '0.8'],
    'K_LINEAR': ['4', '8', '24'],
    'MULTI_SIDE_SHOCK': ['0.0', '0.25', '1.0'],
    'FACING_REACTION_TICKS': ['0', '1', '6'],
    'ENCIRCLEMENT_PENALTY': ['0', '4'],
}

WORKER = r'''
import os, sys, json
sys.path.insert(0, %r)
import gauge_mb as G
rid = os.environ['SWEEP_ROW']; n = int(os.environ['SWEEP_N'])
rows = [t for t in (G.TESTS + G.CAV_TESTS) if t[0] == rid]
if not rows:
    print(json.dumps({'error': 'row not found'})); raise SystemExit(0)
row = rows[0]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    G.run('multi', rows, n=n) if 'n' in G.run.__code__.co_varnames else G.run('multi', rows)
out = buf.getvalue()
line = [l for l in out.splitlines() if l.strip().startswith(rid)]
print(json.dumps({'raw': line[0] if line else '', 'ok': bool(line and line[0].rstrip().endswith('OK'))}))
''' % (SIM,)


def run_row(rid, env_over, n):
    env = dict(os.environ)
    env.update(env_over)
    env['SWEEP_ROW'] = rid
    env['SWEEP_N'] = str(n)
    try:
        r = subprocess.run([sys.executable, '-c', WORKER], cwd=REPO, env=env,
                           capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        return {'error': 'timeout'}
    try:
        return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception:
        return {'error': (r.stderr or r.stdout)[-400:]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=30)
    ap.add_argument('--rows', default='H4,H5,H6,H9,H10,R1,R3,C2,C4,C6')
    ap.add_argument('--out', default=None)
    args = ap.parse_args()

    configs = [('BASELINE', {})]
    for t in TOGGLES:
        cur = os.environ.get(t)
        # perturb both ways so a default-ON toggle is tested OFF and vice versa
        configs.append((f'{t}=0', {t: '0'}))
        configs.append((f'{t}=1', {t: '1'}))
    for k, vals in MAGNITUDES.items():
        for v in vals:
            configs.append((f'{k}={v}', {k: v}))

    results = {}
    for rid in args.rows.split(','):
        rid = rid.strip()
        hits = []
        print(f'=== {rid} ({len(configs)} configs, n={args.n}) ===', flush=True)
        for name, over in configs:
            res = run_row(rid, over, args.n)
            if res.get('error'):
                print(f'  {name:32} ERROR {res["error"][:80]}', flush=True)
                continue
            raw = res.get('raw', '').rstrip()
            verdict = raw.split()[-1] if raw else '?'
            val = raw.split()[-5] if len(raw.split()) >= 5 else '?'
            mark = 'IN-BAND' if res.get('ok') else ''
            if res.get('ok'):
                hits.append(name)
            print(f'  {name:32} val={val:>6}  {verdict:<14} {mark}', flush=True)
        results[rid] = hits
        print(f'  --> {rid}: {len(hits)} config(s) reach band'
              f'{"" if not hits else ": " + ", ".join(hits[:8])}\n', flush=True)

    print('\n===== SUMMARY =====')
    for rid, hits in results.items():
        status = 'REACHABLE' if hits else 'NOT REACHABLE by any single toggle/magnitude tested'
        print(f'  {rid:5} {status}')
    if args.out:
        with open(args.out, 'w') as f:
            json.dump(results, f, indent=2)


if __name__ == '__main__':
    main()
