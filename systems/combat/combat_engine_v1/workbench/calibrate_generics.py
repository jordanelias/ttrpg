"""Calibration of the PC-17 GENERIC lever abilities (ED-PC-0059, item 7): the driver and its analysis in one file.

It is MEASURED-BY for the numbers in ED-PC-0059's calibration block. It reads the engine through build_levers.build()
(which forwards **kw, so `equipped` reaches the Combatant; balance._mk is NOT used) and wrapper.fight. Observation is
non-invasive: wrapper._TRACE (the engine's own seam) for `outcome` and `wound` events, and two pass-through wrappers
(read_contest, bind_sigma) that call the original and return its value untouched, drawing no rng. Every subject is built
tradition='none' with known_traditions=(the teaching tradition,), equipped={generic: level}; the opponent is the same
weapon and armour, plain; position-swapped; one random.Random(seed) per cell, seed = crc32(repr(cell key)) % 100000.
A first run whose visual/precommit K-zero control did not null (the module-level LEGIB_SWING_ROOM_K is not in CFG) is
why that control zeroes it too. This is a CALIBRATION instrument for provisional generics: re-run it now that CR-85
has replaced `history` with `faculty` and deleted its five sigma terms (the plan's PC-17 RE-BASE), and read its limits in ED-PC-0059 before quoting a number.

Usage (the repo root is derived from this file's location):
  python -u calibrate_generics.py OUTFILE [--n N] [--workers W] [--phase main|ctl|all] [--levels 1,2,4,8] [--levers a,b]
  python -u calibrate_generics.py --cell LEVER TIER LEVEL KIND N      # re-derive ONE cell, prints its JSON
  python calibrate_generics.py --analyze OUTFILE                      # controls, table and verdicts from a run's file
About 12 minutes on 4 cores for the whole grid at n=10000.
"""
import sys, os, json, math, random, zlib, time, argparse

LEVERS = ('visual', 'precommit', 'tactile', 'tempo', 'balance', 'edge_read', 'choke_control')
STEMS = ('keen_eye', 'reading_intent', 'blade_feel', 'timing', 'footing', 'hidden_return', 'quiet_gather')
TIERS = ('basic', 'practiced', 'refined')
# weapon / armour each lever is read on (the site must be live: edge_read needs a double edge, choke_control a pole)
BUILD = {
    'visual': ('arming', 'light'), 'precommit': ('arming', 'light'), 'tactile': ('longsword', 'light'),
    'tempo': ('arming', 'light'), 'balance': ('arming', 'none'), 'edge_read': ('longsword', 'light'),
    'choke_control': ('poleaxe', 'light'),
}
# the lever's CFG K's, zeroed by the (b) control (None = no K exists for this lever; the substitute is stated)
KZERO = {
    'visual': dict(LEGIB_SWING=0.0, LEGIB_THRUST=0.0, LEGIB_COMMIT_K=0.0, LEGIB_LUNGE=0.0, LEGIB_EDGELINE_K=0.0,
                   CHOKE_ACCURACY_K=0.0),   # no K of its own: zero the legibility the defender's read multiplies
    'precommit': dict(LEGIB_SWING=0.0, LEGIB_THRUST=0.0, LEGIB_COMMIT_K=0.0, LEGIB_LUNGE=0.0, LEGIB_EDGELINE_K=0.0,
                      CHOKE_ACCURACY_K=0.0),
    'tactile': dict(BIND_TACTILE_K=0.0),
    'tempo': dict(INIT_TEMPO_LEVER_K=0.0),
    'balance': dict(FOOT_MEASURE_K=0.0, PURSUIT_FOOT_K=0.0),
    'edge_read': dict(LEGIB_EDGELINE_K=0.0),
    'choke_control': dict(CHOKE_ACCURACY_K=0.0),
}


def teaching_tradition(lever, tier_idx, trads):
    # Latin square (ability_primitives): tradition t gets (lever (t+k) mod 7, tier k) => t = (lever_idx - k) mod 7
    return trads[(LEVERS.index(lever) - tier_idx) % 7]


def setup(repo):
    sys.path.insert(0, os.path.join(repo, 'systems/combat/combat_engine_v1/workbench'))
    sys.path.insert(0, os.path.join(repo, 'modules/combat'))
    global BL, wrapper, S, CFG, AP, TRADS
    import build_levers as BL
    import wrapper, combat_systems as S
    from config import CFG
    import ability_primitives as AP
    import traditions
    TRADS = tuple(t for t in traditions.TRADITIONS if t != 'none')
    return TRADS


def cell_seed(key):
    return zlib.crc32(repr(key).encode()) % 100000   # build_levers._seed's function, widened (9999 buckets collide across 126 cells x2)


def run_cell(repo, lever, tier_idx, level, kind, n):
    """kind: 'main' (K live), 'k0' (the lever's K zeroed), 'mirror' (equipped on BOTH sides). level 0 = unequipped-effect twin."""
    trads = setup(repo)
    stem = STEMS[LEVERS.index(lever)]
    name = f'{stem}_{TIERS[tier_idx]}'
    assert AP.ABILITIES[name]['lever'] == lever
    trad = teaching_tradition(lever, tier_idx, trads)
    assert AP.ABILITIES[name]['tradition'] == trad, (name, trad, AP.ABILITIES[name]['tradition'])
    weapon, armor = BUILD[lever]
    cfg = dict(CFG)
    if kind in ('k0', 'k0b'):
        cfg.update(KZERO[lever])
    if kind == 'k0b':
        cfg.update(READ_TEMPO_K=0.0)   # tempo only: ALSO zero the cadence site, to separate it from the init-sigma site
    _room = S.LEGIB_SWING_ROOM_K
    if kind == 'k0' and lever in ('visual', 'precommit'):
        S.LEGIB_SWING_ROOM_K = 0.0     # a module-level (not CFG) legibility term; the first run left it live and the control was NOT null
    subj_spec = dict(label='S', weapon=weapon, armor=armor, tradition='none',
                     equipped={name: float(level)}, known_traditions=(trad,))
    opp_spec = dict(label='O', weapon=weapon, armor=armor, tradition='none')
    if kind == 'mirror':
        opp_spec = dict(opp_spec, equipped={name: float(level)}, known_traditions=(trad,))
    seed = cell_seed((lever, name, level, kind))
    rng = random.Random(seed)

    # --- observation (pass-through; no rng, no state) ---
    rec = {}
    orig_rc, orig_bs = S.read_contest, S.bind_sigma

    def rc(aggressor, defender, commit, consistency_a, mental_fat_d, fat_d, cfg_, rng_, TR):
        out = orig_rc(aggressor, defender, commit, consistency_a, mental_fat_d, fat_d, cfg_, rng_, TR)
        cb = S.choke_counterbalance(aggressor, cfg_)
        rec['reads'].append((aggressor.label, defender.label, out['p_read'], cb > 0.0))
        return out

    def bs(aggressor, defender, cfg_, TR):
        v = orig_bs(aggressor, defender, cfg_, TR)
        rec['binds'].append((aggressor.label, v))
        return v

    def trace(ev):
        k = ev['kind']
        if k == 'outcome':
            rec['exch'].append((ev['aggressor'], bool(ev['bind'])))
        elif k == 'wound':
            rec['wounds'].append((ev['by'], ev['damage']))
        elif k == 'roll':
            rec['rolls'].append((ev['aggressor'], ev['net_sigma']))

    S.read_contest, S.bind_sigma, wrapper._TRACE = rc, bs, trace
    fights = []
    wins = {1: 0, -1: 0, 0: 0}
    try:
        half = n // 2
        for i in range(n):
            swap = i >= half            # position swap: first half S is A, second half S is B
            rec.update(reads=[], binds=[], exch=[], wounds=[], rolls=[])
            Sc, Oc = BL.build(subj_spec), BL.build(opp_spec)
            X, Y = (Oc, Sc) if swap else (Sc, Oc)
            r = wrapper.fight(X, Y, cfg, rng)
            r = -r if swap else r       # r from S's point of view
            wins[r] += 1
            f = {}
            for who, other in (('S', 'O'), ('O', 'S')):
                rd = [p for a, d, p, _ in rec['reads'] if d == who]
                ra = [p for a, d, p, _ in rec['reads'] if a == who]
                ra_cb = [p for a, d, p, cb in rec['reads'] if a == who and cb]
                bd = [(1 / (1 + math.exp(-v)) if a == who else 1 - 1 / (1 + math.exp(-v))) for a, v in rec['binds']]
                ex_s = sum(1 for a, _ in rec['exch'] if a == who)
                dmg_s = sum(d for b, d in rec['wounds'] if b == who)
                dmg_o = sum(d for b, d in rec['wounds'] if b == other)
                ns = [v for a, v in rec['rolls'] if a == who]
                f[who] = dict(ns_sum=sum(ns), ns_n=len(ns), rd_sum=sum(rd), rd_n=len(rd), ra_sum=sum(ra), ra_n=len(ra),
                              racb_sum=sum(ra_cb), racb_n=len(ra_cb), bd_sum=sum(bd), bd_n=len(bd),
                              ex_s=ex_s, ex_n=len(rec['exch']), dmg_s=dmg_s, dmg_tot=dmg_s + dmg_o)
            fights.append(f)
    finally:
        S.read_contest, S.bind_sigma, wrapper._TRACE = orig_rc, orig_bs, None
        S.LEGIB_SWING_ROOM_K = _room
    return dict(lever=lever, name=name, tradition=trad, tier=TIERS[tier_idx], level=level, kind=kind, n=n,
                seed=seed, weapon=weapon, armor=armor, wins=wins, fights=fights)


# --- metrics: (numerator key, denominator key, sign) per lever; sign +1 = higher is the lever's benefit ---
METRIC = {
    'visual': ('rd_sum', 'rd_n', +1, "P(read) as defender (mean p_read_win)"),
    'precommit': ('rd_sum', 'rd_n', +1, "P(read) as defender (mean p_read_win)"),
    'tactile': ('bd_sum', 'bd_n', +1, "P(subject dominates bind) (mean logistic(bind_sigma))"),
    'tempo': ('ex_s', 'ex_n', +1, "share of exchanges the subject initiates"),
    'balance': ('dmg_s', 'dmg_tot', +1, "subject share of wound damage dealt"),
    'edge_read': ('ra_sum', 'ra_n', -1, "opponent P(read) vs subject's attacks (benefit = lower)"),
    'choke_control': ('racb_sum', 'racb_n', -1, "opponent P(read) vs subject's attacks, grip>0 events (benefit = lower)"),
}


def ratio(fights, who, num, den):
    """Cluster (per-fight) ratio estimator p = sum k / sum m; Wilson interval at n_eff = p(1-p)/Var(p) so that
    within-fight correlation is not mistaken for independent events. Returns (p, lo, hi, n_eff, m_total)."""
    K = [f[who][num] for f in fights]
    M = [f[who][den] for f in fights]
    sm = sum(M)
    if sm == 0:
        return (float('nan'),) * 4 + (0,)
    p = sum(K) / sm
    nf = len(fights)
    var = sum((k - p * m) ** 2 for k, m in zip(K, M)) * nf / (nf - 1) / sm ** 2
    neff = min(sm, p * (1 - p) / var) if var > 0 and 0 < p < 1 else sm   # never more precise than sm independent Bernoulli events
    z = 1.96
    d = 1 + z * z / neff
    c = (p + z * z / (2 * neff)) / d
    h = z * math.sqrt(p * (1 - p) / neff + z * z / (4 * neff * neff)) / d
    return p, max(0.0, c - h), min(1.0, c + h), neff, sm


def newcombe(a, b):
    """Newcombe hybrid-score CI for p_a - p_b from the two Wilson intervals. a, b = (p, lo, hi, ...)"""
    d = a[0] - b[0]
    return d, d - math.sqrt((a[0] - a[1]) ** 2 + (b[2] - b[0]) ** 2), d + math.sqrt((a[2] - a[0]) ** 2 + (b[0] - b[1]) ** 2)


def wilson_wins(w):
    dec = w[1] + w[-1]
    p = w[1] / dec if dec else float('nan')
    z = 1.96
    d = 1 + z * z / dec
    c = (p + z * z / (2 * dec)) / d
    h = z * math.sqrt(p * (1 - p) / dec + z * z / (4 * dec * dec)) / d
    return p, c - h, c + h


def summarize(cell):
    lever = cell['lever']
    num, den, sign, _ = METRIC[lever]
    out = dict(lever=lever, name=cell['name'], tradition=cell['tradition'], tier=cell['tier'], level=cell['level'],
               kind=cell['kind'], n=cell['n'], seed=cell['seed'], weapon=cell['weapon'], armor=cell['armor'])
    out['S'] = ratio(cell['fights'], 'S', num, den)
    out['O'] = ratio(cell['fights'], 'O', num, den)
    out['win'] = wilson_wins(cell['wins'])
    out['decided'] = cell['wins'][1] + cell['wins'][-1]
    K = [f['S']['ns_sum'] for f in cell['fights']]; M = [f['S']['ns_n'] for f in cell['fights']]
    sm = sum(M); mu = sum(K) / sm; nf = len(K)
    out['S_ns'] = (mu, math.sqrt(sum((k - mu * m) ** 2 for k, m in zip(K, M)) * nf / (nf - 1)) / sm)   # mean attack net_sigma, cluster SE
    for key in ('rd', 'ra', 'racb', 'bd'):    # secondary raw readings, for context
        out['S_' + key] = ratio(cell['fights'], 'S', key + '_sum', key + '_n')[0]
    return out


def _job(args):
    repo, lever, tier_idx, level, kind, n = args
    t0 = time.time()
    c = run_cell(repo, lever, tier_idx, level, kind, n)
    s = summarize(c)
    s['secs'] = round(time.time() - t0, 1)
    return s


def analyze(RES):
    """Read the results file written by the run mode and print the controls, the per-generic table and the verdicts.
    Print controls + per-generic table + verdicts. Pre-declared rules (set before the n=10000 run was read):
      effect(L) = sign * (rate(L) - rate(L0 pooled over the 3 tier-replicates)), in percentage points; CI = Newcombe hybrid
      score over the two cluster-adjusted Wilson intervals (cal.ratio). sign=+1 where higher is the benefit, -1 for edge_read, choke_control.
      MONOTONE  : no pair i<j of {0,1,2,4,8} with sign*(rate_j - rate_i) significantly negative (Newcombe upper bound < 0).
      WRONG SIGN: effect(8) significantly negative.
      CLIFF     : an interval (a->b) whose logit step exceeds 2.5x the step expected from the overall 0->8 logit slope, at z>2
                  (logit SE from the Wilson half-width by the delta method). Saturation (rate pinned >=0.99 or <=0.01) is NOT a cliff;
                  it is flagged "pins".
      DETECTABLE: effect(8) CI excludes 0.
      TIER SPREAD visible at level L if (refined - basic) effect CI excludes 0 in the expected order; REVERSED if significant the other way.
      PASS = monotone and no wrong sign and no cliff and detectable at L8.   INCONCLUSIVE = otherwise clean but undetectable at L8.
    """
    LEVERS = ('visual', 'precommit', 'tactile', 'tempo', 'balance', 'edge_read', 'choke_control')
    TIERS = ('basic', 'practiced', 'refined')
    LV = (1.0, 2.0, 4.0, 8.0)
    SIGN = {'visual': 1, 'precommit': 1, 'tactile': 1, 'tempo': 1, 'balance': 1, 'edge_read': -1, 'choke_control': -1}
    Z = 1.96
    cells = {}
    for l in open(RES):
        r = json.loads(l); cells[(r['lever'], r['tier'], r['level'], r['kind'])] = r


    def wil(p, neff):
        d = 1 + Z * Z / neff; c = (p + Z * Z / (2 * neff)) / d
        h = Z * math.sqrt(p * (1 - p) / neff + Z * Z / (4 * neff * neff)) / d
        return (p, max(0, c - h), min(1, c + h), neff)


    def pooled(cs):
        m = sum(c['S'][4] for c in cs); p = sum(c['S'][0] * c['S'][4] for c in cs) / m
        ne = sum(c['S'][3] for c in cs)
        return wil(p, ne) + (m,)


    def diff(a, b):
        d = a[0] - b[0]
        return d, d - math.sqrt((a[0] - a[1]) ** 2 + (b[2] - b[0]) ** 2), d + math.sqrt((a[2] - a[0]) ** 2 + (b[0] - b[1]) ** 2)


    def orient(sg, t):
        d, lo, hi = t
        return (d, lo, hi) if sg > 0 else (-d, -hi, -lo)


    def lg(p):
        p = min(max(p, 1e-4), 1 - 1e-4); return math.log(p / (1 - p))


    def lse(c):   # SE of logit from the Wilson half-width
        p = min(max(c[0], 1e-4), 1 - 1e-4)
        return max((c[2] - c[1]) / (2 * Z), 1e-6) / (p * (1 - p))


    def fmt(t, sg=1):
        d, lo, hi = t; return f"{100*d:+.2f} [{100*lo:+.2f},{100*hi:+.2f}]"


    report = []
    verdicts = {}
    for lv in LEVERS:
        sg = SIGN[lv]
        l0 = [cells[(lv, t, 0.0, 'main')] for t in TIERS]
        base = pooled(l0)
        reps = [c['S'] for c in l0]
        zmax = 0
        for i in range(3):
            for j in range(i + 1, 3):
                d, lo, hi = diff(reps[i], reps[j]); zmax = max(zmax, abs(d) / (((hi - lo) / (2 * Z)) or 1e-9))
        report.append(f"\n### {lv}   base(L0, pooled 3 replicates)={base[0]:.4f} [{base[1]:.4f},{base[2]:.4f}] events={base[4]}  replicate max|z|={zmax:.2f}")
        # controls
        ctl = []
        c8m = cells[(lv, 'refined', 8.0, 'main')]
        ctl.append(('main   refined L8 - L0pooled', orient(sg, diff(c8m['S'], base))))
        for kd in ('k0', 'k0b'):
            a, b = cells.get((lv, 'refined', 0.0, kd)), cells.get((lv, 'refined', 8.0, kd))
            if a and b:
                ctl.append((f'{kd}     refined L8 - L0 (K zeroed)', orient(sg, diff(b['S'], a['S']))))
        for L in (0.0, 4.0, 8.0):
            m = cells.get((lv, 'refined', L, 'mirror'))
            if m:
                ctl.append((f'mirror L{int(L)} S - O (both equipped)', diff(m['S'], m['O'])))
        for nm, t in ctl:
            report.append(f"   ctl {nm:<40} {fmt(t)} pp")
        if lv == 'tempo':
            for kd in ('main', 'k0', 'k0b'):
                a, b = cells.get((lv, 'refined', 0.0, kd)), cells.get((lv, 'refined', 8.0, kd))
                if a and b and 'S_ns' in a:
                    d = b['S_ns'][0] - a['S_ns'][0]; se = math.hypot(a['S_ns'][1], b['S_ns'][1])
                    report.append(f"   ctl tempo mean attack net_sigma ({kd}) refined L8 - L0: {d:+.4f} sigma (SE {se:.4f}, z={d/se:+.1f})")
        # table
        effs = {}
        for t in TIERS:
            seq = {0.0: base}
            for L in LV:
                seq[L] = cells[(lv, t, L, 'main')]['S']
            e = {L: orient(sg, diff(seq[L], base)) for L in LV}
            effs[t] = (seq, e)
            name = cells[(lv, t, 8.0, 'main')]['name']; trad = cells[(lv, t, 8.0, 'main')]['tradition']
            # monotone
            pts = [0.0] + list(LV); mono = True; viol = []
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    d = orient(sg, diff(seq[pts[j]], seq[pts[i]]))
                    if d[2] < 0:
                        mono = False; viol.append(f"{int(pts[i])}->{int(pts[j])}")
            wrong = e[8.0][2] < 0
            det = e[8.0][1] > 0
            # cliff
            s = orient(sg, (lg(seq[8.0][0]) - lg(seq[0.0][0]), 0, 0))[0] / 8
            cliff = []
            for a_, b_ in ((0.0, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0)):
                step = sg * (lg(seq[b_][0]) - lg(seq[a_][0])); exp_ = s * (b_ - a_)
                se = math.hypot(lse(seq[a_]), lse(seq[b_]))
                if s > 0 and step > 2.5 * exp_ and (step - 2.5 * exp_) / se > 2:
                    cliff.append(f"{int(a_)}->{int(b_)}")
            pins = [int(L) for L in LV if seq[L][0] >= 0.99 or seq[L][0] <= 0.01]
            verdicts[(lv, t)] = dict(mono=mono, viol=viol, wrong=wrong, det=det, cliff=cliff, pins=pins, name=name, trad=trad, e=e, seq=seq)
        # tier spread
        spread = {}
        for L in LV:
            d = orient(sg, diff(effs['refined'][0][L], effs['basic'][0][L]))
            spread[L] = 'visible' if d[1] > 0 else ('REVERSED' if d[2] < 0 else 'not-detectable')
        for t in TIERS:
            v = verdicts[(lv, t)]; v['spread'] = spread
            ok = v['mono'] and not v['wrong'] and not v['cliff'] and v['det']
            v['verdict'] = 'PASS' if ok else ('INCONCLUSIVE' if (v['mono'] and not v['wrong'] and not v['cliff']) else 'FAIL')
            report.append(f"  {v['name']:<20}{v['trad']:<9}" + "  ".join(f"L{int(L)} {fmt(v['e'][L])}" for L in LV)
                          + f"  | mono={'Y' if v['mono'] else 'N ' + ','.join(v['viol'])} cliff={','.join(v['cliff']) or 'none'} pins={v['pins'] or '-'} -> {v['verdict']}")
        report.append(f"  tier spread refined-basic by level: {spread}")
    print("\n".join(report))
    json.dump({f"{k[0]}|{k[1]}": {kk: vv for kk, vv in v.items() if kk in ('mono', 'viol', 'wrong', 'det', 'cliff', 'pins', 'verdict', 'name', 'trad', 'spread')} for k, v in verdicts.items()}, open(RES + '.verdicts.json', 'w'), default=str)


REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('out', nargs='?')
    ap.add_argument('--n', type=int, default=2000)
    ap.add_argument('--workers', type=int, default=3)
    ap.add_argument('--phase', default='all')
    ap.add_argument('--levels', default='1,2,4,8')
    ap.add_argument('--levers', default=','.join(LEVERS))
    ap.add_argument('--cell', nargs=5, metavar=('LEVER', 'TIER', 'LEVEL', 'KIND', 'N'))
    ap.add_argument('--analyze', metavar='OUTFILE')
    a = ap.parse_args()
    if a.analyze:
        analyze(a.analyze)
        sys.exit(0)
    if a.cell:
        lever, tier, level, kind, n = a.cell
        s = _job((REPO, lever, TIERS.index(tier), float(level), kind, int(n)))
        print(json.dumps(s))
        sys.exit(0)
    if not a.out:
        ap.error('OUTFILE is required for a run')
    levels = [float(x) for x in a.levels.split(',')]
    levers = a.levers.split(',')
    jobs = []
    for lv in levers:
        for t in range(3):
            if a.phase in ('main', 'all'):
                jobs.append((REPO, lv, t, 0.0, 'main', a.n))
                for L in levels:
                    jobs.append((REPO, lv, t, L, 'main', a.n))
        if a.phase in ('ctl', 'all'):
            if lv == 'tempo':
                jobs += [(REPO, lv, 2, 0.0, 'k0b', a.n), (REPO, lv, 2, 8.0, 'k0b', a.n)]
            jobs += [(REPO, lv, 2, 0.0, 'k0', a.n), (REPO, lv, 2, 8.0, 'k0', a.n),
                     (REPO, lv, 2, 8.0, 'mirror', a.n), (REPO, lv, 2, 4.0, 'mirror', a.n),
                     (REPO, lv, 2, 0.0, 'mirror', a.n)]
    from multiprocessing import Pool
    done = 0
    with Pool(a.workers) as pool, open(a.out, 'a') as fh:
        for s in pool.imap_unordered(_job, jobs):
            fh.write(json.dumps(s) + '\n'); fh.flush()
            done += 1
            print(f"[{done}/{len(jobs)}] {s['name']} L{s['level']} {s['kind']} S={s['S'][0]:.4f} secs={s['secs']}", flush=True)
    print('EXIT 0', flush=True)
