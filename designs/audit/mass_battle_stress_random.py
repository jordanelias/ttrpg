"""Robust randomized-subformation stress test for the mass_battle engine.

Each subunit independently has a 50% chance of a RANDOMIZED subformation (random shape
+ concentration); the other 50% is a standard Line. Units carry 1-3 such subunits.
Fuzzes the formation space and separates the two robustness questions:
  - construction-rejection (off-grid / invalid combo) = CORRECT input validation, not a defect
  - engine failure (exception/NaN/out-of-bounds/non-termination) during run_battle = the real defect
Plus a mirror-symmetry control (identical randomized formation both sides -> ~50/50, order-cancelled)
and a non-randomized historical-counter control (outcomes must stay precedent-plausible).

NON-INVASIVE: only constructs units + calls run_battle; never touches engine internals.
Requires PER_CELL=1.  Usage: python3 stress_random.py [n_trials=100] [mirror=24] [seed_base=9000]
"""
import sys, math, random, traceback
from mass_battle.engine import Subunit, Unit, run_battle
from mass_battle.mass_battle_stress import make_unit, _COL

SHAPES = ['Arrowhead', 'Column', 'GappedLine', 'Horseshoe', 'Line', 'RefusedFlank']
MAX_T = 180
SPREADS = {1: [0], 2: [-9, 9], 3: [-13, 0, 13]}

def random_spec(rng):
    """A reproducible random unit spec. Each subunit: 50% randomized subformation, else standard Line."""
    n = rng.choice([1, 1, 1, 2, 2, 3])
    subs = []
    for _ in range(n):
        if rng.random() < 0.5:                                  # 50% RANDOMIZED subformation
            subs.append((rng.choice(SHAPES), round(rng.uniform(60, 200), 1)))
        else:                                                   # standard
            subs.append(('Line', 120.0))
    return dict(n=n, subs=subs,
                troops_each=round(rng.uniform(1200, 3600) / (1 + 0.4 * (n - 1)), 1),
                ttype=('cavalry' if rng.random() < 0.15 else 'infantry'),
                stance=rng.choice(['balanced', 'balanced', 'balanced', 'hold']),
                command=rng.randint(3, 7), discipline=rng.randint(3, 7),
                brace=(rng.random() < 0.5), anchor=rng.randint(-10, 10))

def instantiate(spec, fac):
    """Build a Unit for faction fac from a spec (may raise ValueError if a formation is off-grid)."""
    ad = -1 if fac == 'A' else 1
    row = 34 if fac == 'A' else 15
    spreads = SPREADS[spec['n']]
    instr = ('brace', 'hold') if (spec['stance'] == 'hold' and spec['brace']) else ()
    speed = 'Fast' if spec['ttype'] == 'cavalry' else 'Standard'
    sus = [Subunit(shape=sh, troop_type=spec['ttype'], tier=4,
                   starting_position=(row, _COL + spec['anchor'] + spreads[i]), advance_dir=ad, unit_type='melee',
                   stance=spec['stance'], instructions=instr,
                   troops=spec['troops_each'], concentration=conc)
           for i, (sh, conc) in enumerate(spec['subs'])]
    return Unit(name=fac, faction=fac, power=4, command=spec['command'],
                discipline=spec['discipline'], discipline_start=5, morale=6, morale_start=6,
                subunits=sus, dr=1, stance=spec['stance'], speed=speed)

def validate(r, a, b):
    """Return list of degeneracy issues (empty = sane outcome) + the winner key."""
    iss = []
    w = r.get('winner')
    if w not in ('A', 'B', 'draw', None):
        iss.append(f"winner={w!r}")
    for nm, u in (('A', a), ('B', b)):
        hp = getattr(u, 'hp', None); hm = getattr(u, 'hp_max', 0)
        if hp is None or not hm:
            iss.append(f"{nm}:no-hp"); continue
        f = hp / hm
        if math.isnan(f) or math.isinf(f):
            iss.append(f"{nm}:hp-naninf")
        elif f < -1e-6 or f > 1 + 1e-6:
            iss.append(f"{nm}:hp-frac={f:.3f}")
        m = getattr(u, 'morale', 0.0)
        if math.isnan(m) or math.isinf(m):
            iss.append(f"{nm}:mor-naninf")
    return iss, (w if w in ('A', 'B', 'draw') else 'None')

def fuzz(n, seed_base):
    rej = engfail = degen = draw_hold = draw_bb = 0
    wins = {'A': 0, 'B': 0, 'draw': 0, 'None': 0}
    fail_ex, degen_ex = [], []
    for t in range(n):
        R = random.Random(seed_base + t)
        sA = random_spec(R); sB = random_spec(R)
        try:
            a = instantiate(sA, 'A'); b = instantiate(sB, 'B')
        except ValueError:
            rej += 1; continue
        try:
            r = run_battle(a, b, max_turns=MAX_T)
        except Exception as e:
            engfail += 1
            if len(fail_ex) < 6:
                fail_ex.append((type(e).__name__, str(e)[:140], traceback.format_exc().strip().splitlines()[-1]))
            continue
        iss, key = validate(r, a, b)
        if iss:
            degen += 1
            if len(degen_ex) < 6:
                degen_ex.append((iss, key, [su.shape for su in a.subunits], [su.shape for su in b.subunits]))
        wins[key] += 1
        if key in ('draw', 'None'):
            if sA['stance'] == 'hold' or sB['stance'] == 'hold': draw_hold += 1
            else: draw_bb += 1
    return dict(rej=rej, engfail=engfail, degen=degen, wins=wins, draw_hold=draw_hold,
                draw_bb=draw_bb, fail_ex=fail_ex, degen_ex=degen_ex)

def mirror(n, seed_base):
    """Identical randomized formation both sides, order-cancelled. Symmetric engine -> ~50/50."""
    aw = bw = dr = rej = 0
    for t in range(n):
        spec = random_spec(random.Random(seed_base + 50000 + t))
        try:
            a, b = instantiate(spec, 'A'), instantiate(spec, 'B')
            a2, b2 = instantiate(spec, 'A'), instantiate(spec, 'B')   # fresh for 2nd ordering (units mutate)
        except ValueError:
            rej += 1; continue
        w1 = run_battle(a, b, max_turns=MAX_T).get('winner')
        w2 = run_battle(b2, a2, max_turns=MAX_T).get('winner')        # swapped order
        for w, swap in ((w1, False), (w2, True)):
            if w in ('draw', None): dr += 1
            elif (w == 'A') != swap:  aw += 1
            else:                     bw += 1
    return dict(aw=aw, bw=bw, draw=dr, rej=rej)

def control(seed_base):
    """Non-randomized historical-counter sanity (precedent-plausibility intact)."""
    def rate(win, lose, N=4):
        w = 0
        for s in range(N):
            for order in (1, 2):
                random.seed(s + seed_base + order * 1000)
                if order == 1:
                    a = make_unit('A', **win); b = make_unit('B', **lose); want = 'A'
                else:
                    a = make_unit('A', **lose); b = make_unit('B', **win); want = 'B'
                if run_battle(a, b, max_turns=MAX_T).get('winner') == want: w += 1
        return w, 2 * N
    L = dict(shape='Line', troops=4000, concentration=120)
    out = {}
    out['deepColumn>thinLine'] = rate(dict(shape='Column', troops=4000, concentration=120), L)
    out['ShieldWall>Wedge'] = rate(dict(shape='Line', troops=4000, concentration=120, stance='hold',
                                         discipline=7, instructions=('brace', 'hold')),
                                    dict(shape='Arrowhead', troops=4000, concentration=120))
    out['command-dominates'] = rate(dict(shape='Line', troops=2000, concentration=120, command=7),
                                     dict(shape='Line', troops=6000, concentration=120, command=2))
    return out

if __name__ == '__main__':
    n_trials = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    n_mirror = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    seed_base = int(sys.argv[3]) if len(sys.argv) > 3 else 9000

    print(f"=== RANDOMIZED-SUBFORMATION STRESS  (fuzz={n_trials}, mirror={n_mirror}x2, PER_CELL=1) ===")
    f = fuzz(n_trials, seed_base)
    built = n_trials - f['rej']
    print(f"\n-- fuzz: {n_trials} trials --")
    print(f"  constructed & ran : {built}   (rejected at construction: {f['rej']} — input validation)")
    print(f"  ENGINE FAILURES   : {f['engfail']}   <- defect surface")
    print(f"  degenerate states : {f['degen']}   <- defect surface (NaN / hp out-of-range / bad winner)")
    print(f"  outcomes          : {f['wins']}")
    print(f"  draws: hold-standoff (correct, a holder won't advance) {f['draw_hold']} | both-balanced non-close {f['draw_bb']}")
    if f['fail_ex']:
        print("  engine-failure examples:")
        for nm, msg, last in f['fail_ex']:
            print(f"    {nm}: {msg}  | {last}")
    if f['degen_ex']:
        print("  degenerate examples:")
        for iss, key, sa, sb in f['degen_ex']:
            print(f"    {iss} winner={key}  A={sa} B={sb}")

    m = mirror(n_mirror, seed_base)
    tot = m['aw'] + m['bw'] + m['draw']
    skew = abs(m['aw'] - m['bw'])
    print(f"\n-- mirror symmetry (identical random formation both sides, order-cancelled) --")
    print(f"  A-side {m['aw']}  B-side {m['bw']}  draw {m['draw']}  (rej {m['rej']})  |skew|={skew}/{tot}")

    print(f"\n-- non-randomized historical-counter control --")
    for k, (w, N) in control(seed_base).items():
        print(f"  {k:22} {w}/{N} ({100*w//N}%)")

    verdict = "ROBUST" if (f['engfail'] == 0 and f['degen'] == 0) else "FAILURES PRESENT"
    print(f"\nVERDICT: {verdict} — engine_failures={f['engfail']} degenerate={f['degen']}")
