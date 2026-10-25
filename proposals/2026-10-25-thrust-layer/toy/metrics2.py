def executed(ev):
    return [e for e in ev if e['delta'] > 0 and e.get('thread') and isinstance(e['actor'], int)]


def select(ev, B=12, top=3):
    ex = executed(ev)
    mass = Counter()
    for e in ex:
        mass[e['thread']] += e['delta']
    keep = {r for r, _ in mass.most_common(top)}
    c = [e for e in ex if e['thread'] in keep]
    if len(c) > B:
        c = sorted(c, key=lambda e: (-e['delta'], e['t']))[:B]
    return sorted(c, key=lambda e: (e['t'], e['id']))


def main_thread(ex):
    m = Counter()
    for e in ex:
        m[e['thread']] += e['delta']
    return m.most_common(1)[0][0] if m else None


def ranks(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]:
            j += 1
        for q in range(i, j + 1):
            r[o[q]] = (i + j) / 2
        i = j + 1
    return r


def spearman(x, y):
    if len(x) < 3:
        return 0.0
    rx, ry = ranks(x), ranks(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else 0.0


def arc_test(ex, th, lo, hi, peak_hi=0.92, strict_close=False):
    """Three-act test on one thread over seasons [lo, hi): interior peak, rise before it, fall + closure after it.
    The peak is the CENTRE of the smoothed maximum plateau (a single spike smooths to a three-wide plateau)."""
    n = hi - lo
    I = [0.0] * n
    for e in ex:
        if e['thread'] == th and lo <= e['t'] < hi:
            I[e['t'] - lo] += e['delta']
    if sum(I) == 0:
        return dict(rise=False, peak=False, fall=False, all=False, closed=False, tp=None)
    S = [sum(I[max(0, i - 1):i + 2]) / len(I[max(0, i - 1):i + 2]) for i in range(n)]
    mx = max(S); plateau = [i for i in range(n) if abs(S[i] - mx) < 1e-9]
    tp = plateau[len(plateau) // 2]
    peak = 0.2 * n <= tp <= peak_hi * n
    rise = tp >= 3 and spearman(list(range(tp + 1)), S[:tp + 1]) >= 0.5
    post = S[tp + 1:]
    cut = (lambda t: t > tp) if strict_close else (lambda t: t >= tp)
    closed = any(e['thread'] == th and e['closing'] and cut(e['t'] - lo) and e['t'] < hi for e in ex)
    fall = len(post) >= 2 and (sum(post) / len(post)) <= 0.6 * S[tp] and closed
    return dict(rise=rise, peak=peak, fall=fall, all=(rise and peak and fall), closed=closed, tp=tp + lo)


def shuffled(ex, rng):
    ts = [e['t'] for e in ex]; rng.shuffle(ts)
    return [dict(e, t=t) for e, t in zip(ex, ts)]


def violations(ev, t_lo=0):
    v = Counter()
    for e in ev:
        if e['t'] < t_lo or not isinstance(e['actor'], int) or 'actor_alive' not in e:
            continue
        if not e['actor_alive']:
            v['dead_actor'] += 1
        if not e['target_alive']:
            v['dead_target'] += 1
        if not e['colocated']:
            v['not_colocated'] += 1
        for c in e['causes']:
            if c >= e['id'] or ev[c]['t'] > e['t']:
                v['bad_cause'] += 1
    return v


def graph_stats(ev):
    ex = executed(ev)
    cited = Counter()
    for e in ev:
        for c in e['causes']:
            cited[c] += 1
    conv = sum(1 for e in ex if len({ev[c]['actor'] for c in e['causes'] if isinstance(ev[c]['actor'], int)}) >= 2)
    dead = sum(1 for e in ex if cited[e['id']] == 0 and not e['closing'])
    depth = {}
    for e in ev:
        d = 1
        for c in e['causes']:
            if ev[c]['actor'] != e['actor']:
                d = max(d, 1 + depth.get(c, 1))
        depth[e['id']] = d
    return dict(n=len(ex), conv=conv / len(ex) if ex else 0, dead=dead / len(ex) if ex else 0,
                depth=max(depth.values()) if depth else 0)


def five_node(sel, th):
    """setup (first beat) < turn < climax (a beat in the thread's peak season) < resolution (a closing beat at/after it)."""
    bt = sorted([e for e in sel if e['thread'] == th], key=lambda e: e['t'])
    if len(bt) < 4:
        return False
    by = Counter()
    for e in bt:
        by[e['t']] += e['delta']
    tp = max(by, key=lambda t: (by[t], -t))
    setup = bt[0]
    turn = [e for e in bt if setup['t'] < e['t'] < tp]
    res = [e for e in bt if e['closing'] and e['t'] >= tp]
    return bool(turn and res and setup['t'] < tp)


def cv_gaps(sel, th):
    ts = sorted(set(e['t'] for e in sel if e['thread'] == th))
    g = [b - a for a, b in zip(ts, ts[1:])]
    if len(g) < 2:
        return None
    m = sum(g) / len(g)
    return (sum((x - m) ** 2 for x in g) / len(g)) ** 0.5 / m


BURN = 4
VARIANTS = {'p92_relax_b4': (0.92, False, 4), 'p92_relax_b0': (0.92, False, 0),
            'p85_strict_b4': (0.85, True, 4), 'p85_strict_b0': (0.85, True, 0)}


def run_metrics(ev, T=T_DEF, shuf_rng=None, t_lo=0):
    ex = executed(ev)
    sel = select(ev)
    M = {}
    # --- LEGIBILITY (the repo's triad: what is at stake / who acts and why / what changed)
    M['leg_apparent'] = sum(1 for e in sel if e['thread'] and e['delta'] > 0 and e['motive']) / len(sel) if sel else 0
    M['leg_grounded'] = sum(1 for e in sel if e['grounded']) / len(sel) if sel else 0
    selset = {e['id'] for e in sel}
    def linked(e):
        m = e['motive']
        return bool(m) and (m[0] == 'ambition' or (m[0] == 'reaction' and m[1] in selset))
    M['why_linked'] = sum(1 for e in sel if linked(e)) / len(sel) if sel else 0
    M['leg_grounded_raw'] = sum(1 for e in ex if e['grounded']) / len(ex) if ex else 0
    forced = [e for e in ex if e['forced']]
    M['forced_in_sel'] = sum(1 for e in sel if e['forced']) / len(sel) if sel else 0
    M['grounded_forced'] = (sum(1 for e in forced if e['grounded']) / len(forced)) if forced else float('nan')
    M['injected'] = sum(1 for e in ev if e['forced'] and e['delta'] > 0)
    M['director_writes'] = sum(1 for e in ev if e['forced'])
    # --- COHERENCY
    last = {}; cont = 0
    for i, e in enumerate(sel):
        if i > 0 and e['thread'] in last and e['t'] - last[e['thread']] <= 6:
            cont += 1
        last[e['thread']] = e['t']
    M['thread_cont'] = cont / (len(sel) - 1) if len(sel) > 1 else 0
    cc = 0; selids = [e['id'] for e in sel]
    for i, e in enumerate(sel[1:], 1):
        hops = set(e['causes']); frontier = set(e['causes'])
        for _ in range(2):
            frontier = {c2 for c in frontier for c2 in ev[c]['causes']}; hops |= frontier
        if hops & set(selids[:i]) or any(x['thread'] == e['thread'] for x in sel[:i]):
            cc += 1
    M['chain_conn'] = cc / (len(sel) - 1) if len(sel) > 1 else 0
    v = violations(ev, t_lo)
    M['viol'] = sum(v.values()); M['viol_any'] = 1 if M['viol'] else 0
    # --- ARC (observer-picked main thread, regime-blind), primary variant + sensitivity grid
    mass = Counter()
    for e in ex:
        mass[e['thread']] += e['delta']
    for name, (hi, strict, burn) in VARIANTS.items():
        exw = [e for e in ex if e['t'] >= burn]
        mt = main_thread(exw)
        a = arc_test(exw, mt, burn, T, hi, strict) if mt else dict(all=False)
        M['arc_' + name] = 1 if a['all'] else 0
        if shuf_rng is not None and exw:
            accs = []
            for _ in range(3):
                sx = shuffled(exw, shuf_rng); m2 = main_thread(sx)
                accs.append(1 if m2 and arc_test(sx, m2, burn, T, hi, strict)['all'] else 0)
            M['null_' + name] = sum(accs) / 3
    exw = [e for e in ex if e['t'] >= BURN]
    mt = main_thread(exw)
    M['main_thread'] = mt
    if mt:
        a = arc_test(exw, mt, BURN, T)
        for k in ('rise', 'peak', 'fall', 'closed'):
            M['arc_' + k] = 1 if a[k] else 0
        M['tp'] = a['tp']
        M['peak_mag'] = max(sum(e['delta'] for e in exw if e['thread'] == mt and e['t'] == t) for t in range(BURN, T))
        M['dangling'] = 1 if sum(e['delta'] for e in exw if e['thread'] == mt and e['t'] >= T - 2) >= 0.5 * M['peak_mag'] else 0
    else:
        for k in ('rise', 'peak', 'fall', 'closed'):
            M['arc_' + k] = 0
        M['tp'] = None; M['peak_mag'] = 0; M['dangling'] = 0
    M['arc_all'] = M['arc_p92_relax_b4']; M['arc_null'] = M.get('null_p92_relax_b4', 0)
    M['arc_any3'] = 1 if any(arc_test([e for e in ex if e['t'] >= BURN], r, BURN, T)['all']
                              for r, _ in Counter({e['thread']: e['delta'] for e in exw}).items()
                              if False) else 0
    top3 = Counter()
    for e in exw:
        top3[e['thread']] += e['delta']
    M['arc_any3'] = 1 if any(arc_test(exw, r, BURN, T)['all'] for r, _ in top3.most_common(3)) else 0
    # --- the DIRECTOR'S OWN thread (best case for a top-down regime): arc over the full window
    fc = Counter(e['thread'] for e in ev if e['forced'] and e['delta'] > 0)
    if fc:
        dt = fc.most_common(1)[0][0]
        da = arc_test(ex, dt, 0, T)
        M['arc_dir'] = 1 if da['all'] else 0
        M['dir_is_main'] = 1 if dt == mt else 0
        M['dir_mass_rank'] = 1 + sum(1 for r, m in mass.items() if m > mass[dt])
    else:
        M['arc_dir'] = None; M['dir_is_main'] = None; M['dir_mass_rank'] = None
    # --- BEATS / NODES
    M['five_node'] = 1 if mt and five_node(sel, mt) else 0
    M['gap_cv'] = cv_gaps(sel, mt) if mt else None
    g = graph_stats(ev)
    M.update(dict(conv=g['conv'], dead=g['dead'], depth=g['depth'], n_exec=g['n'], n_sel=len(sel)))
    if mt:
        th = [e for e in ex if e['thread'] == mt][:5]
        M['sig_struct'] = tuple((e['verb'], round(e['delta'])) for e in th)
        M['sig_slot'] = tuple((e['verb'], round(e['delta']), e['actor'], e['target']) for e in th)
    else:
        M['sig_struct'] = M['sig_slot'] = ()
    return M


def log_hash(ev):
    return hashlib.sha1(json.dumps([(e['t'], e['actor'], e['verb'], e['target'], e['ref'], e['delta']) for e in ev]).encode()).hexdigest()
