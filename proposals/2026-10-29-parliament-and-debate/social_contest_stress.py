"""Stress probe for the SOCIAL CONTEST subsystem, with an audit log (same JSONL shape as stress_probe.py).

Two things are stressed, and the log keeps them apart:
  MODULE  `modules/social_contest/roll.py` (the live, registered σ-leverage roll): `obstacle` and `roll`
          over `SocialContestInput` at and past the edges of every field.
  KERNEL  `systems/social_contest/sim/contest/` (evaluated, not adopted, per roll.py's SC-05 note):
          `build_contest` / `resolve_contest` / `mechanics_selftest`, every proceeding, adjudicator and
          policy, plus the kernel's own 151 tests and the module's tests.

NO CHOSEN COUNT. Nothing here fixes a number of trials. Each section samples until its slice of the
caller's --budget-s runs out and logs how many trials that was, so a reader sees the evidence
strength (n) beside every rate. The edge values come from the code's own constants where it has them
(OB_MIN, Standing.START, Stasis.LADDER, the PROCEEDINGS / POLICIES / CANONICAL_ADJUDICATORS keys) and
otherwise from the edges of the field's type (0, 1, negative, huge, None, NaN, inf); they are edges
to try, never a claim about the legal domain. Every anomaly is logged with the exact input and the
sampling seed that produced it, so it can be replayed.

Usage (repo root):  python proposals/2026-10-29-parliament-and-debate/social_contest_stress.py \\
                      --label sc --budget-s 1800 --log OUT.jsonl [--sections module,kernel,suites,props]
"""
import argparse, faulthandler, itertools, math, os, random, subprocess, sys, time, traceback
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from stress_probe import Log, git  # one owner of the audit-log shape

from engine.dice_engine.sigma_leverage import OB_MIN
from engine.season.queries.inputs import SocialContestInput, Margin
from modules.social_contest import roll as sc_roll
import systems.social_contest.sim.contest as sc
from systems.social_contest.sim.contest.contract import Panel, Adjudicator
from systems.social_contest.sim.contest.primitives import Stasis, Standing

INF, NAN = float('inf'), float('nan')


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def same(x, y):
    """Equality that treats NaN as equal to NaN (a reproduced NaN is reproducible, not a mismatch)."""
    return x == y or (isinstance(x, float) and isinstance(y, float) and x != x and y != y)


def finite_input(kw):
    return all(math.isfinite(v) for k, v in kw.items() if isinstance(v, float))


def sig(e):
    return f"{type(e).__name__}: {str(e).splitlines()[0][:140] if str(e) else ''}"


# ───────────────────────── MODULE ─────────────────────────
POOL = [-1, 0, 1, 2, 3, 10, 100, 10_000]
OPP = [None, -3.0, 0.0, 1.0, 2.0, 6.0, 20.0, 1e9, INF, NAN]
OBD = [-1.0, 0.0, 2.0, 5.0]
CEIL = [None, OB_MIN - 0.5, OB_MIN, 2.0, 5.0, 1e9]
LEV = [-100.0, -5.0, -1.0, 0.0, 1.0, 5.0, 100.0, NAN]
ROOM = [(0.0, 0.0, 0.0, 0.0), (1.0, 1.0, 0.0, 0.0), (1.0, -1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 1.0),
        (3.0, 10.0, 2.0, 2.0), (1.0, -50.0, 0.0, 0.0), (1.0, 1.0, 1.0, 1.0)]
FORG = [0.0, 1.0, -1.0, 50.0]


def module_section(log, label, seconds):
    deadline = time.time() + seconds
    rnd = random.Random(0)
    log.w('section_start', label=label, section='module.grid', seconds=seconds, sampling_seed=0)
    n = 0
    exc = Counter(); exc_ex = {}
    nonfinite = Counter(); nonfinite_ex = {}
    viol = Counter(); viol_ex = {}
    t_max = 0.0; t_max_in = None
    while time.time() < deadline:
        rg, gain, prf, step = rnd.choice(ROOM)
        kw = dict(pool=rnd.choice(POOL), opposition=rnd.choice(OPP), obstacle_default=rnd.choice(OBD),
                  obstacle_ceiling=rnd.choice(CEIL), obstacle_refusal_multiple=2.0, leverage=rnd.choice(LEV),
                  reception=rg, reception_gain=gain, proofs=prf, proof_step=step, forgery_quality=rnd.choice(FORG))
        inp = SocialContestInput(**kw)
        s = rnd.randrange(2 ** 31)
        n += 1
        before = random.getstate()
        t = time.time()
        try:
            m1 = sc_roll.roll(inp, random.Random(s))
            dt = time.time() - t
            if dt > t_max:
                t_max, t_max_in = dt, (kw, s)
            m2 = sc_roll.roll(inp, random.Random(s))
        except Exception as e:
            k = sig(e)
            exc[k] += 1
            exc_ex.setdefault(k, {'input': kw, 'seed': s})
            if finite_input(kw) and not (isinstance(e, ValueError) and 'below the Ob minimum' in str(e)):
                viol['undocumented_exception_on_finite_input'] += 1
                viol_ex.setdefault('undocumented_exception_on_finite_input', {'input': kw, 'seed': s, 'error': k})
            continue
        if random.getstate() != before:
            viol['global_random_consumed_with_rng_given'] += 1
            viol_ex.setdefault('global_random_consumed_with_rng_given', {'input': kw, 'seed': s})
        if not isinstance(m1, Margin):
            viol['not_a_margin'] += 1; viol_ex.setdefault('not_a_margin', {'input': kw})
        if not (same(m1.net, m2.net) and same(m1.ob, m2.ob)):
            viol['same_seed_different_result'] += 1
            viol_ex.setdefault('same_seed_different_result', {'input': kw, 'seed': s, 'a': (m1.net, m1.ob), 'b': (m2.net, m2.ob)})
        for nm, v in (('net', m1.net), ('ob', m1.ob)):
            if not math.isfinite(v):
                key = nm + ('_from_finite_input' if finite_input(kw) else '_from_nonfinite_input')
                nonfinite[key] += 1
                nonfinite_ex.setdefault(key, {'input': kw, 'seed': s, 'value': repr(v)})
        c = kw['obstacle_ceiling']
        if c is not None and c >= OB_MIN and math.isfinite(m1.ob) and m1.ob > c + 1e-9:
            viol['ob_above_ceiling'] += 1; viol_ex.setdefault('ob_above_ceiling', {'input': kw, 'ob': m1.ob})
    log.w('module_grid', label=label, trials=n, exceptions=dict(exc), exception_examples=exc_ex,
          nonfinite=dict(nonfinite), nonfinite_examples=nonfinite_ex, violations=dict(viol),
          violation_examples=viol_ex, slowest_call_s=round(t_max, 4), slowest_input=t_max_in)

    # rng=None path: does it consume the process-global stream?
    log.w('section_start', label=label, section='module.rng_none')
    inp = SocialContestInput(pool=3, opposition=None, obstacle_default=2.0, obstacle_ceiling=2.0,
                             obstacle_refusal_multiple=2.0, leverage=0.0)
    random.seed(12345); a = random.random()
    random.seed(12345); sc_roll.roll(inp, None); b = random.random()
    log.w('module_rng_none', label=label, global_stream_consumed=(a != b),
          note='True means roll(inp, rng=None) draws from the process-global random stream')


def module_stats(log, label, seconds):
    """Rates with confidence intervals; monotonicity in pool, leverage and opposition."""
    log.w('section_start', label=label, section='module.stats', seconds=seconds)
    base = dict(pool=3, opposition=None, obstacle_default=2.0, obstacle_ceiling=None,
                obstacle_refusal_multiple=2.0, leverage=0.0)
    axes = {'pool': [1, 2, 3, 4, 6, 8, 12, 20], 'leverage': [-2.0, -1.0, 0.0, 1.0, 2.0],
            'opposition': [0.0, 2.0, 4.0, 6.0, 8.0, 12.0]}
    per = seconds / sum(len(v) for v in axes.values())
    rows = {}
    for axis, vals in axes.items():
        series = []
        for v in vals:
            inp = SocialContestInput(**{**base, axis: v})
            rng = random.Random(hash((axis, v)) & 0xffffffff)
            k = n = 0
            end = time.time() + per
            while time.time() < end:
                for _ in range(200):
                    m = sc_roll.roll(inp, rng); n += 1; k += (m.net >= m.ob)
            lo, hi = wilson(k, n)
            series.append({'value': v, 'n': n, 'p_success': round(k / n, 5), 'ci95': [round(lo, 5), round(hi, 5)], 'ob': sc_roll.obstacle(inp)})
        rows[axis] = series
        flips = []
        sign = -1 if axis == 'opposition' else 1  # more opposition should not raise success
        for a, b in zip(series, series[1:]):
            d = sign * (b['p_success'] - a['p_success'])
            if d < 0 and (sign * (b['ci95'][0] - a['ci95'][1]) < 0) and (b['ci95'][1] < a['ci95'][0] if sign > 0 else b['ci95'][0] > a['ci95'][1]):
                flips.append((a['value'], b['value']))
        log.w('module_monotone', label=label, axis=axis, series=series, significant_violations=flips)


# ───────────────────────── KERNEL ─────────────────────────
FAC = [-1, 0, 1, 2, 3, 4, 6, 10, 100]
STAND = [-5.0, 0.0, Standing.START, 1e3]
WEIGHT = [0.0, 1.0, -1.0, 1e6]


def side(rnd):
    r = rnd.random()
    if r < 0.4:
        return rnd.choice(FAC)
    if r < 0.5:
        return float(rnd.choice(FAC)) + rnd.random()
    d = {'faculty': rnd.choice(FAC), 'standing_start': rnd.choice(STAND)}
    if rnd.random() < 0.6:
        d['evidence'] = [(rnd.choice(Stasis.LADDER), rnd.choice(WEIGHT)) for _ in range(rnd.choice([0, 1, 3, 12]))]
    return d


def band_side(band):
    b = str(band)
    if b == 'draw':
        return 'draw'
    if b[:1] in 'aA':
        return 'A'
    if b[:1] in 'bB':
        return 'B'
    return 'other'


def adjudicators(rnd):
    return [None] + list(sc.CANONICAL_ADJUDICATORS) + ['panel'] + [Panel(tuple(Adjudicator() for _ in range(k))) for k in (1, 2, 3, 9)]


def kernel_section(log, label, seconds):
    log.w('section_start', label=label, section='kernel.fuzz', seconds=seconds, sampling_seed=1,
          proceedings=sorted(sc.PROCEEDINGS), policies=sorted(sc.POLICIES), adjudicators=sorted(sc.CANONICAL_ADJUDICATORS))
    deadline = time.time() + seconds
    rnd = random.Random(1)
    procs = sorted(sc.PROCEEDINGS); pols = sorted(sc.POLICIES)
    adjs = adjudicators(rnd)
    n = 0
    exc = Counter(); exc_ex = {}
    bands = defaultdict(Counter)
    nondet = Counter(); nondet_ex = {}
    leak = Counter(); leak_ex = {}
    shape = Counter()
    times = []
    while time.time() < deadline:
        proc = rnd.choice(procs); pa = rnd.choice(pols); pb = rnd.choice(pols)
        sa, sb = side(rnd), side(rnd)
        adj = rnd.choice(adjs)
        # the tracker opt-in is honoured only by 'optional' proceedings (build_contest refuses it elsewhere, by design)
        ut = rnd.choice([None, True, False]) if sc.PROCEEDINGS[proc].get('tracker_mode') == 'optional' else None
        s = rnd.randrange(2 ** 31)
        spec = {'proc': proc, 'pa': pa, 'pb': pb, 'sa': sa, 'sb': sb, 'adj': repr(adj)[:80], 'use_tracker': ut, 'seed': s}
        n += 1
        out = []
        try:
            for rep in (1, 2):
                random.seed(s)
                c = sc.build_contest(sa, sb, venue=proc, adjudicator=adj, use_tracker=ut)
                st = random.getstate()
                t = time.time()
                r = sc.resolve_contest(c, policy_a=pa, policy_b=pb)
                times.append(time.time() - t)
                if rep == 1:
                    leak['advanced_global_stream' if random.getstate() != st else 'did_not_advance'] += 1
                out.append(r)
        except Exception as e:
            k = f"{proc}|{sig(e)}"
            exc[k] += 1
            exc_ex.setdefault(k, {**spec, 'trace': traceback.format_exc().splitlines()[-4:]})
            continue
        try:
            (band, reason), bout = out[0]
            shape['tuple_band_reason_bout'] += 1
        except Exception:
            shape['other:' + type(out[0]).__name__] += 1
            continue
        bands[proc][str(band)] += 1
        (b2, r2), _ = out[1]
        if (str(band), str(reason)) != (str(b2), str(r2)):
            nondet[proc] += 1
            nondet_ex.setdefault(proc, {**spec, 'first': (str(band), str(reason)), 'second': (str(b2), str(r2))})
    ts = sorted(times)
    log.w('kernel_fuzz', label=label, trials=n, exceptions=dict(exc), exception_examples=exc_ex,
          bands={k: dict(v) for k, v in bands.items()}, nondeterministic_under_reseed=dict(nondet),
          nondeterministic_examples=nondet_ex, global_stream=dict(leak), return_shapes=dict(shape),
          resolve_s={'n': len(ts), 'median': round(ts[len(ts) // 2], 5) if ts else None,
                     'p99': round(ts[int(len(ts) * .99)], 5) if ts else None, 'max': round(ts[-1], 5) if ts else None})


def kernel_api_edges(log, label):
    log.w('section_start', label=label, section='kernel.api_edges')
    res = {}

    def tryit(name, fn):
        try:
            r = fn()
            res[name] = {'ok': True, 'type': type(r).__name__, 'repr': repr(r)[:160]}
        except Exception as e:
            res[name] = {'ok': False, 'error': sig(e)}
    tryit('unknown_proceeding', lambda: sc.build_contest(4, 4, venue='nope'))
    tryit('unknown_adjudicator', lambda: sc.build_contest(4, 4, venue='formal_contest', adjudicator='nope'))
    tryit('bad_side_type', lambda: sc.build_contest('x', 4, venue='formal_contest'))
    tryit('none_side', lambda: sc.build_contest(None, 4, venue='formal_contest'))
    tryit('use_tracker_with_prebuilt_venue', lambda: sc.build_contest(4, 4, venue=sc.proceeding_venue('formal_contest'), use_tracker=True))
    tryit('empty_panel', lambda: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest', adjudicator=Panel(tuple()))))
    tryit('unknown_game', lambda: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest'), game='nope'))
    for g in ('consensus', 'negotiation', 'inquiry'):
        tryit(f'stub_game_{g}', lambda g=g: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest'), game=g))
    tryit('unknown_policy', lambda: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest'), policy_a='nope'))
    tryit('policy_returning_garbage', lambda: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest'), policy_a=lambda v: None))
    tryit('policy_raising', lambda: sc.resolve_contest(sc.build_contest(4, 4, venue='formal_contest'), policy_a=lambda v: 1 / 0))
    tryit('mechanics_selftest', lambda: sc.mechanics_selftest())
    log.w('kernel_api_edges', label=label, results=res)


def kernel_props(log, label, seconds):
    """Symmetry / position-bias and monotonicity in faculty, per proceeding, with n and CIs."""
    log.w('section_start', label=label, section='kernel.props', seconds=seconds)
    procs = sorted(sc.PROCEEDINGS)
    per = seconds / (len(procs) * 3)
    rows = []
    for proc in procs:
        def rate(sa, sb, pa='logos', pb='logos', secs=per):
            rnd = random.Random(hash((proc, repr(sa), repr(sb))) & 0xffffffff)
            c = Counter(); n = 0
            end = time.time() + secs
            while time.time() < end:
                for _ in range(20):
                    random.seed(rnd.randrange(2 ** 31))
                    try:
                        (band, _), _b = sc.resolve_contest(sc.build_contest(sa, sb, venue=proc), policy_a=pa, policy_b=pb)
                        c[band_side(band)] += 1
                    except Exception as e:
                        c['error:' + sig(e)] += 1
                    n += 1
            return c, n
        c1, n1 = rate(4, 4)                # equal sides
        c2, n2 = rate(1, 4); c3, n3 = rate(4, 1)  # weak A vs strong B, then swapped
        row = {'proceeding': proc,
               'equal': {'n': n1, **{k: v for k, v in c1.items()}, 'A_ci95': [round(x, 4) for x in wilson(c1['A'], max(1, c1['A'] + c1['B']))]},
               'weakA_vs_strongB': {'n': n2, **dict(c2)},
               'strongA_vs_weakB': {'n': n3, **dict(c3)}}
        # position bias: A's win share among decided equal contests should be 0.5
        d = c1['A'] + c1['B']
        row['equal']['position_bias_flag'] = bool(d and not (wilson(c1['A'], d)[0] <= 0.5 <= wilson(c1['A'], d)[1]))
        # monotone: the stronger side should win more often than the weaker, in both seats
        d3, d2 = c3['A'] + c3['B'], c2['A'] + c2['B']
        lo3, hi3 = wilson(c3['A'], d3); lo2, hi2 = wilson(c2['A'], d2)
        row['decided_share'] = {'equal': round(d / n1, 4), 'weakA_vs_strongB': round(d2 / n2, 4), 'strongA_vs_weakB': round(d3 / n3, 4)}
        if d3 and d2 and lo3 > 0.5 and hi2 < 0.5:
            row['stronger_wins_more_in_both_seats'] = True
        elif d3 and d2 and (hi3 < 0.5 or lo2 > 0.5):
            row['stronger_wins_more_in_both_seats'] = False
        else:
            row['stronger_wins_more_in_both_seats'] = 'inconclusive (too few decided contests)' 
        rows.append(row)
    log.w('kernel_props', label=label, rows=rows)


def run_suites(log, label):
    # engine/tests/test_contest_kernel.py is the pytest wrapper that runs the standalone _kernel_tests.py script
    for name, args in (('kernel_tests', ['engine/tests/test_contest_kernel.py']),
                       ('module_and_oblige_tests', ['engine/season/tests/test_social_contest_module.py',
                                                    'engine/season/tests/test_sc01_obstacle_ceiling.py'])):
        existing = [a for a in args if os.path.exists(os.path.join(ROOT, a))]
        if not existing:
            log.w('suite', label=label, name=name, skipped='no such file', files=args)
            continue
        env = {**os.environ, 'PYTHONUTF8': '1'}
        t = time.time()
        p = subprocess.run([sys.executable, '-m', 'pytest', *existing, '-q', '-p', 'no:cacheprovider'], cwd=ROOT,
                           capture_output=True, text=True, env=env)
        log.w('suite', label=label, name=name, files=existing, returncode=p.returncode,
              wall_s=round(time.time() - t, 1), tail=p.stdout.splitlines()[-12:], stderr_tail=p.stderr.splitlines()[-5:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True)
    ap.add_argument('--budget-s', type=float, required=True, dest='budget')
    ap.add_argument('--sections', default='suites,edges,module,kernel,props')
    ap.add_argument('--hang-s', type=float, default=None, help='dump tracebacks and exit if the run stalls this long')
    ap.add_argument('--log', required=True)
    a = ap.parse_args()
    log = Log(a.log)
    if a.hang_s:
        faulthandler.dump_traceback_later(a.hang_s, exit=True, file=open(a.log + '.hang.txt', 'w'))
    log.w('manifest', label=a.label, argv=sys.argv, head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'),
          dirty=git('status', '--porcelain')[:400], python=sys.version.split()[0], platform=sys.platform,
          pythonhashseed=os.environ.get('PYTHONHASHSEED'), ob_min=OB_MIN)
    secs = [s for s in a.sections.split(',') if s]
    timed = [s for s in secs if s in ('module', 'kernel', 'props')]
    weights = {'module': 2, 'kernel': 3, 'props': 3}  # module has two timed parts; shares are logged
    total_w = sum(weights[s] for s in timed) or 1
    share = {s: a.budget * weights[s] / total_w for s in timed}
    log.w('plan', label=a.label, budget_s=a.budget, shares_s=share, sections=secs)
    t0 = time.time()
    for s in secs:
        try:
            if s == 'suites': run_suites(log, a.label)
            elif s == 'edges': kernel_api_edges(log, a.label)
            elif s == 'module':
                module_section(log, a.label, share['module'] * 0.5); module_stats(log, a.label, share['module'] * 0.5)
            elif s == 'kernel': kernel_section(log, a.label, share['kernel'])
            elif s == 'props': kernel_props(log, a.label, share['props'])
        except Exception as e:
            log.w('error', label=a.label, section=s, type=type(e).__name__, message=str(e)[:400], traceback=traceback.format_exc())
    log.w('summary', label=a.label, wall_s=round(time.time() - t0, 1))


if __name__ == '__main__':
    main()
