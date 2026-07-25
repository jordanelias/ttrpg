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


def _val_of(res):
    """Parse the row's decisive value out of the gauge's printed line (None if unparseable)."""
    raw = (res or {}).get('raw', '')
    parts = raw.split()
    if len(parts) < 5:
        return None
    try:
        return float(parts[-5])
    except ValueError:
        return None


def greedy_stack(rid, singles, n, band_lo, band_hi, depth=6):
    """[ED-MB-0041] Can COMBINED toggles reach the band when no single one can?

    Greedy hill-climb, not an exhaustive search: 2^33 is not enumerable, but a greedy stack answers
    the practical question — take the toggles that individually move the row furthest toward its band
    and apply them together, keeping each only if it improves. If a greedy stack of the strongest
    movers still cannot reach the band, the row is not a calibration problem. This can miss a
    combination that only works jointly (a non-monotone interaction), which is exactly why the result
    is reported as evidence rather than proof.
    """
    target = (band_lo + band_hi) / 2.0
    ranked = sorted((s for s in singles if s[1] is not None),
                    key=lambda s: abs(s[1] - target))
    over, cur = {}, None
    trail = []
    for name, _val in ranked[:depth * 3]:
        if '=' not in name:
            continue
        k, v = name.split('=', 1)
        if k in over:
            continue
        cand = dict(over); cand[k] = v
        res = run_row(rid, cand, n)
        got = _val_of(res)
        if got is None:
            continue
        if cur is None or abs(got - target) < abs(cur - target):
            over, cur = cand, got
            trail.append((name, got, bool(res.get('ok'))))
            if res.get('ok'):
                return over, cur, trail, True
        if len(over) >= depth:
            break
    return over, cur, trail, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=30)
    ap.add_argument('--rows', default='H4,H5,H6,H9,H10,R1,R3,C2,C4,C6')
    ap.add_argument('--out', default=None)
    ap.add_argument('--stack', action='store_true',
                    help='after the single-toggle sweep, greedily stack the strongest movers')
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

    # Bands, read from the gauge itself so this tool can never drift from the register it measures.
    sys.path.insert(0, SIM)
    import gauge_mb as _G
    bands = {t[0]: (t[-3], t[-2]) for t in (_G.TESTS + _G.CAV_TESTS)}

    results = {}
    for rid in args.rows.split(','):
        rid = rid.strip()
        hits, singles, verdicts = [], [], set()
        print(f'=== {rid} ({len(configs)} configs, n={args.n}) ===', flush=True)
        for name, over in configs:
            res = run_row(rid, over, args.n)
            if res.get('error'):
                print(f'  {name:32} ERROR {res["error"][:80]}', flush=True)
                continue
            raw = res.get('raw', '').rstrip()
            verdict = raw.split()[-1] if raw else '?'
            val = _val_of(res)
            singles.append((name, val))
            verdicts.add(verdict)
            mark = 'IN-BAND' if res.get('ok') else ''
            if res.get('ok'):
                hits.append(name)
            print(f'  {name:32} val={"?" if val is None else f"{val:.1f}":>6}  '
                  f'{verdict:<14} {mark}', flush=True)

        vals = [v for _n, v in singles if v is not None]
        lo, hi = bands.get(rid, (None, None))
        span = f'{min(vals):.1f}..{max(vals):.1f}' if vals else '?'
        print(f'  --> {rid}: {len(hits)} single config(s) reach band; '
              f'span across all singles = {span} (band {lo}-{hi})', flush=True)

        stacked = None
        if args.stack and not hits and lo is not None:
            over, cur, trail, ok = greedy_stack(rid, singles, args.n, lo, hi)
            stacked = {'config': over, 'val': cur, 'reached': ok,
                       'trail': [(t[0], t[1]) for t in trail]}
            print(f'  --> {rid} greedy stack: '
                  f'{"REACHED BAND" if ok else "still out"} at val={cur} with {over}', flush=True)
        results[rid] = {'singles_in_band': hits, 'span': span, 'band': [lo, hi],
                        'verdicts': sorted(verdicts), 'stacked': stacked}
        print('', flush=True)

    print('\n===== SUMMARY =====')
    for rid, r in results.items():
        if r['singles_in_band']:
            status = f'REACHABLE by a single toggle ({len(r["singles_in_band"])} of them)'
        elif r.get('stacked') and r['stacked']['reached']:
            status = f'REACHABLE only by stacking {r["stacked"]["config"]}'
        elif r['verdicts'] == ['UNRESOLVED']:
            # The win-split may sit inside the band and the row still fail: the gauge also requires a
            # DECISIVE result. An all-draw row is a missing resolution path, not a miscalibrated one --
            # reporting it as "span never enters band" would be simply wrong (50.0 is inside 42-58).
            status = (f'NOT REACHABLE — UNRESOLVED under every config (all draws); the win-split '
                      f'{r["span"]} is irrelevant while nothing resolves')
        else:
            status = (f'NOT REACHABLE — span {r["span"]} never enters band '
                      f'{r["band"][0]}-{r["band"][1]} (verdicts seen: {", ".join(r["verdicts"])})')
        print(f'  {rid:5} {status}')
    if args.out:
        with open(args.out, 'w') as f:
            json.dump(results, f, indent=2)


if __name__ == '__main__':
    main()
