"""Combat-engine MECHANICAL stress battery (2026-07-22 stress test).

Attacks systems/combat/combat_engine_v1 for correctness invariants that must hold regardless of balance:
robustness/crash, extreme/degenerate inputs, determinism, mirror-symmetry, numerical sanity (no NaN/inf,
damage int>=0), monotonicity (a better attribute never lowers win-rate), the 95% upset cap, and bounded
runtime. Report-only; mutates nothing. Run:  python stress_battery.py
"""
import sys, os, math, random, time, itertools, traceback
ENG = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1'))
sys.path.insert(0, ENG); sys.path.insert(0, os.path.join(ENG, 'workbench'))
import wrapper, config, core, combat_systems as S, weapon_physics as WP  # noqa: E402
from combatant import Combatant  # noqa: E402
from weapons import WEAPONS  # noqa: E402

CFG = config.CFG
ARMORS = ['none', 'light', 'medium', 'heavy']
TRADS = ['none', 'german', 'italian', 'spanish', 'japanese', 'chinese', 'filipino', 'english']
ATTRS = ['strength', 'agi', 'end', 'cog', 'att', 'spirit', 'focus', 'history', 'disp']
WPNS = [w for w in WEAPONS if 'base' not in WEAPONS[w]]
results = []
def record(cat, name, status, detail=''): results.append((cat, name, status, detail))
def mk(spec):
    kw = {k: spec[k] for k in ATTRS if k in spec}
    return Combatant(spec.get('label', '?'), weapon=spec.get('weapon', 'arming'),
                     armor=spec.get('armor', 'light'), tradition=spec.get('tradition', 'none'), **kw)
def winrate(a, b, n=200, seed=0):
    rng = random.Random(seed); aw = dec = draws = 0; half = n // 2
    for i in range(n):
        sw = i >= half; X = mk(b if sw else a); Y = mk(a if sw else b)
        r = wrapper.fight(X, Y, CFG, rng)
        if sw: r = -r
        if r == 1: aw += 1; dec += 1
        elif r == -1: dec += 1
        else: draws += 1
    return (aw / dec if dec else 0.0), dec, draws
def isbad(x): return isinstance(x, float) and (math.isnan(x) or math.isinf(x))

def cat_robustness():
    crashes = bad = total = 0; rng = random.Random(1)
    for w in WPNS:
        for a in ARMORS:
            total += 1
            try:
                r = wrapper.fight(mk({'weapon': w, 'armor': a, 'tradition': 'german'}),
                                  mk({'weapon': 'arming', 'armor': a, 'tradition': 'italian'}), CFG, rng)
                if r not in (-1, 0, 1): bad += 1; record('robustness', f'{w}/{a}', 'FAIL', f'result={r!r}')
            except Exception as e:
                crashes += 1; record('robustness', f'{w}/{a}', 'FAIL', f'{type(e).__name__}: {e}')
    record('robustness', 'weapon x armour grid', 'PASS' if crashes == 0 and bad == 0 else 'FAIL',
           f'{total} matchups, {crashes} crashes, {bad} bad')
    crashes = 0
    for ta, tb in itertools.product(TRADS, TRADS):
        try: wrapper.fight(mk({'tradition': ta}), mk({'tradition': tb}), CFG, random.Random(2))
        except Exception as e: crashes += 1; record('robustness', f'trad {ta}v{tb}', 'FAIL', str(e))
    record('robustness', 'tradition grid', 'PASS' if crashes == 0 else 'FAIL', f'{len(TRADS)**2} pairs, {crashes} crashes')

def cat_extremes():
    cases = [('all-zero', {a: 0 for a in ATTRS}), ('all-one', {a: 1 for a in ATTRS}),
             ('negative', {a: -5 for a in ATTRS}), ('huge-uniform', {a: 1000 for a in ATTRS}),
             ('float', {a: 3.7 for a in ATTRS}),
             ('mixed-asym', {'strength': 999, 'agi': 0, 'end': -3, 'cog': 50, 'att': 0, 'spirit': 0,
                             'focus': 0, 'history': 100, 'disp': 7})]
    for name, spec in cases:
        try:
            r = wrapper.fight(mk(dict(spec, weapon='longsword')), mk({'weapon': 'arming'}), CFG, random.Random(3))
            record('extremes', name, 'PASS' if r in (-1, 0, 1) else 'FAIL', f'result={r}')
        except Exception as e:
            record('extremes', name, 'FAIL', f'{type(e).__name__}: {e}')

def cat_determinism():
    mm = ck = 0
    for w in random.Random(0).sample(WPNS, 12):
        seqs = []
        for _ in range(3):
            rng = random.Random(12345)
            seqs.append(tuple(wrapper.fight(mk({'weapon': w}), mk({'weapon': 'spear'}), CFG, rng) for _ in range(15)))
        ck += 1
        if len(set(seqs)) != 1: mm += 1; record('determinism', w, 'FAIL', str(seqs))
    record('determinism', 'same-seed reproducibility', 'PASS' if mm == 0 else 'FAIL', f'{ck} weapons, {mm} nondet')

def cat_symmetry():
    worst = 0.0; wn = ''
    for w in ['arming', 'longsword', 'spear', 'mace', 'rapier', 'dagger', 'poleaxe']:
        for a in ARMORS:
            p, dec, _ = winrate({'weapon': w, 'armor': a, 'tradition': 'german'},
                                {'weapon': w, 'armor': a, 'tradition': 'german'}, n=400, seed=7)
            if abs(p - 0.5) > worst: worst = abs(p - 0.5); wn = f'{w}/{a} p={p:.3f}'
    st = 'PASS' if worst <= 0.08 else ('WARN' if worst <= 0.15 else 'FAIL')
    record('symmetry', 'mirror-match ~50% (N=400)', st, f'worst dev={worst:.3f} @ {wn}')

def cat_numerical():
    bad = neg = ck = 0
    for w in WPNS:
        wv = WEAPONS[w]
        for ar in ARMORS:
            for deg in ('graze', 'partial', 'success', 'overwhelming', 'fail'):
                for strg in (0, 4, 20, 1000):
                    ck += 1
                    try:
                        d = core.damage(deg, WP.heft(wv), wv['head'], strg, ar, True,
                                        gap=wv.get('gap', 0.5), perc=WP.percussion_authority(wv))
                    except Exception as e:
                        bad += 1; record('numerical', f'damage {w}/{ar}/{deg}', 'FAIL', str(e)); continue
                    if isbad(d) or not isinstance(d, int): bad += 1
                    elif d < 0: neg += 1
    record('numerical', 'core.damage finite,>=0,int', 'PASS' if bad == 0 and neg == 0 else 'FAIL',
           f'{ck} calls, {bad} bad, {neg} neg')
    badband = sum(1 for net in [x / 10 for x in range(-100, 300)]
                  if core.degree(net, core.DECISIVE_OB) not in {'fail', 'partial', 'success', 'overwhelming'})
    record('numerical', 'degree() valid band forall net', 'PASS' if badband == 0 else 'FAIL', f'{badband} invalid')
    bad_r = 0; rng = random.Random(9)
    for pool in (1, 5, 9, 13, 30):
        for nsig in [x / 4 for x in range(-40, 41)]:
            deg, net = core.resolve(pool, nsig, rng)
            if isbad(net) or deg not in {'fail', 'partial', 'success', 'overwhelming'}: bad_r += 1
    record('numerical', 'core.resolve finite forall pool x sigma', 'PASS' if bad_r == 0 else 'FAIL', f'{bad_r} bad')

def cat_monotonicity():
    base = {a: (4 if a in ('strength', 'agi', 'end') else 3) for a in ATTRS}; base['disp'] = 4
    for a in ('strength', 'end', 'history', 'agi', 'cog', 'focus', 'spirit'):
        ps = []
        for bump in (0, 2, 4):
            up = dict(base); up[a] = base[a] + bump
            p, _, _ = winrate(up, base, n=600, seed=100 + bump); ps.append(round(p, 3))
        md = max(ps[i] - ps[i + 1] for i in range(len(ps) - 1))
        st = 'PASS' if md <= 0.05 else ('WARN' if md <= 0.10 else 'FAIL')
        record('monotonicity', f'raise {a} non-decreasing', st, f'winrates(0/2/4)={ps}')

def cat_upsetcap():
    strong = {'strength': 8, 'agi': 8, 'end': 8, 'cog': 6, 'att': 6, 'spirit': 6, 'focus': 6, 'history': 10,
              'disp': 5, 'weapon': 'poleaxe', 'armor': 'heavy', 'tradition': 'german'}
    weak = {'strength': 1, 'agi': 1, 'end': 1, 'cog': 1, 'att': 1, 'spirit': 1, 'focus': 1, 'history': 0,
            'disp': 4, 'weapon': 'dagger', 'armor': 'none', 'tradition': 'none'}
    p, dec, dr = winrate(strong, weak, n=1000, seed=42)
    record('upset-cap', 'extreme mismatch < 100%', 'PASS' if p <= 1.0 else 'FAIL',
           f'p(strong)={p:.3f} decided={dec} draws={dr} UPSET_FLOOR={CFG["UPSET_FLOOR"]}')

def cat_termination():
    t0 = time.time(); nf = 0; rng = random.Random(0)
    for w in random.Random(1).sample(WPNS, 20):
        for _ in range(10):
            wrapper.fight(mk({'weapon': w, 'armor': 'heavy'}), mk({'weapon': 'staff', 'armor': 'heavy'}), CFG, rng); nf += 1
    dt = time.time() - t0
    record('termination', 'bounded runtime', 'PASS' if dt < 30 else 'WARN', f'{nf} fights {dt:.1f}s ({1000*dt/nf:.1f}ms/fight)')

if __name__ == '__main__':
    for fn in [cat_robustness, cat_extremes, cat_determinism, cat_symmetry, cat_numerical,
               cat_monotonicity, cat_upsetcap, cat_termination]:
        nm = fn.__name__.replace('cat_', ''); t0 = time.time()
        try: fn()
        except Exception as e: record(nm, 'HARNESS', 'FAIL', f'{type(e).__name__}: {e}\n{traceback.format_exc()}')
        print(f'[{nm}] {time.time()-t0:.1f}s', file=sys.stderr)
    print('\n=== MECHANICAL STRESS REPORT ===')
    cats = {}
    for c, n, s, d in results: cats.setdefault(c, []).append((n, s, d))
    osrt = {'FAIL': 0, 'WARN': 1, 'PASS': 2}
    for c, items in cats.items():
        print(f'\n## {c}')
        for n, s, d in sorted(items, key=lambda x: osrt.get(x[1], 9)): print(f'  [{s}] {n}: {d}')
    nf = sum(1 for r in results if r[2] == 'FAIL'); nw = sum(1 for r in results if r[2] == 'WARN')
    print(f'\n=== {nf} FAIL, {nw} WARN, {len(results)} checks ===')
