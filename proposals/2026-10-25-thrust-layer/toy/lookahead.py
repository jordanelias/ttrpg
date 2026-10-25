"""Choice-level 'narrative leverage' with lookahead, on the toy world.

Actors choose by Plackett-Luce / Gumbel over candidate acts (as engine/season/decision/choose.py::_sample_order does:
order ~ softmax(score/tau), noise keyed by the candidate).  Narrative leverage adds, to each candidate's score, a shift of
lam * tau * soft_cap(z_c) where z_c is the candidate's lookahead value standardised over THAT ACTOR's candidates (the
mu-shift-in-sigma-units idea of sigma_leverage.py).  Resolution (dice) is never touched; no option is removed; no outcome is
written.  lam=0 is the control (same chooser, no shift).
Lookahead value V_c: M rollouts of H seasons of lam=0 dynamics from the post-act state, scored by a LOCAL proxy Q
(cross-person involvement, thread concentration, escalation) - deliberately not the evaluation metrics.
Only 'relevant' actors (participants of the current top-3 threads) are leveraged - the casting rule.
"""
import math, random, sys
from collections import Counter
import regimes3 as R
from regimes3 import W, clip

TAU = 0.15
M_MAX = 1.5
VI = {'harm': 1, 'claim': 2, 'aid': 3, 'move': 4, 'idle': 5}


def soft_cap(x):
    return M_MAX * math.tanh(x / M_MAX)


def clone(s):
    c = W.__new__(W)
    c.__dict__ = dict(s.__dict__)
    for n in ('place', 'skill', 'alive', 'holder', 'amb', 'amb_n'):
        setattr(c, n, list(getattr(s, n)))
    c.op = [r[:] for r in s.op]
    c.ev = list(s.ev)
    for n in ('last_ref', 'last_harm', 'hold_since', 'pending_occ', 'last_occ', 'adj'):
        setattr(c, n, dict(getattr(s, n)))
    c.ra = random.Random(); c.rd = random.Random()
    return c


def candidates(s, t, a):
    cs = []
    h = s.last_harm.get(a)
    if h and t - h[2] <= 2 and s.alive[h[1]]:
        if s.place[h[1]] == s.place[a]:
            cs.append(dict(verb='harm', b=h[1], k=None, u=1.2, motive=('reaction', h[0])))
        else:
            cs.append(dict(verb='move', q=s.place[h[1]], b=None, k=None, u=0.6))
    for k in range(s.PR):
        if s.pplace[k] == s.place[a] and s.holder[k] != a:
            cs.append(dict(verb='claim', b=None, k=k, u=0.3 + 0.2 * s.pval[k], motive=('opportunity', f"P{k}")))
    nb = s.near(a)
    for b in nb:
        if s.op[a][b] < -0.3:
            cs.append(dict(verb='harm', b=b, k=None, u=0.4 + 0.4 * (-s.op[a][b]), motive=('hostility', b)))
        elif s.op[a][b] > 0.4:
            cs.append(dict(verb='aid', b=b, k=None, u=0.2 + 0.2 * s.op[a][b], motive=('affinity', b)))
    cs.append(dict(verb='move', q=(s.place[a] + 1 + (a + t) % (s.P - 1)) % s.P, b=None, k=None, u=0.2))
    cs.append(dict(verb='idle', b=None, k=None, u=0.3))
    return cs


def apply(s, t, a, c):
    v = c['verb']
    if v == 'harm':
        s.do(t, a, 'harm', b=c['b'], motive=c.get('motive'))
    elif v == 'claim':
        s.do(t, a, 'claim', k=c['k'], motive=c.get('motive'))
    elif v == 'aid':
        s.do(t, a, 'aid', b=c['b'], motive=c.get('motive'))
    elif v == 'move':
        s.place[a] = c['q']


def gumbel(seed, t, a, c):
    key = ((((seed * 131 + t) * 131 + a) * 131 + VI[c['verb']]) * 17 + (c['b'] if c['b'] is not None else 0)) * 29 \
          + (c['k'] if c['k'] is not None else 0) * 7 + (c.get('q') if c.get('q') is not None else 0)
    u = random.Random(key).random() or 1e-12
    return -math.log(-math.log(u))


def step_season(s, t, seed, lam=0.0, ctx=None):
    for a in range(s.A):
        if s.alive[a] and s.skill[a] < s.base_skill[a]:
            s.skill[a] += 1
    order = [a for a in range(s.A) if s.alive[a]]
    s.ra.shuffle(order)
    top3, rel = None, set()
    if lam > 0 and ctx is not None:
        top3, rel = relevant(s)
    for a in order:
        if not s.alive[a]:
            continue
        cs = candidates(s, t, a)
        g = [gumbel(seed, t, a, c) for c in cs]
        base = [c['u'] / TAU + gi for c, gi in zip(cs, g)]
        choice = max(range(len(cs)), key=lambda i: base[i])
        if lam > 0 and ctx is not None and a in rel and len(cs) > 1:
            V = [lookahead(s, t, a, c, ctx, top3) for c in cs]
            mu = sum(V) / len(V); sd = (sum((x - mu) ** 2 for x in V) / len(V)) ** 0.5
            if sd > 1e-9:
                tilted = [base[i] + lam * soft_cap((V[i] - mu) / sd) for i in range(len(cs))]
                new = max(range(len(cs)), key=lambda i: tilted[i])
                ctx['lev'] += 1; ctx['chg'] += (new != choice)
                choice = new
        apply(s, t, a, cs[choice])


def relevant(s):
    mass = Counter()
    for e in s.ev:
        if e['delta'] > 0 and e.get('thread') and isinstance(e['actor'], int):
            mass[e['thread']] += e['delta']
    top3 = {th for th, _ in mass.most_common(3)}
    rel = set()
    for e in s.ev:
        if e.get('thread') in top3:
            for x in (e['actor'], e['target']):
                if isinstance(x, int) and s.alive[x]:
                    rel.add(x)
    return top3, rel


def lookahead(s, t, a, c, ctx, top3, M=4, H=2):
    tot = 0.0
    for m in range(M):
        ctx['roll'] += 1
        r = clone(s)
        r.ra = random.Random(ctx['seed'] * 977 + t * 31 + a * 7 + m + 1000 * VI[c['verb']])
        n0 = len(r.ev)
        apply(r, t, a, c)
        for h in range(1, H + 1):
            step_season(r, t + h, ctx['seed'] * 3 + 1, 0.0, None)
        new = r.ev[n0:]
        mine = {e['id'] for e in new if e['actor'] == a}
        desc = set(mine); others = set()
        for e in new:
            if e['actor'] != a and any(x in desc for x in e['causes']):
                desc.add(e['id'])
                if isinstance(e['actor'], int):
                    others.add(e['actor'])
        involve = min(3, len(others)) / 3
        touched = next((e['thread'] for e in new if e['actor'] == a and e.get('thread')), None)
        ex = [e for e in new if e['delta'] > 0 and e.get('thread') and isinstance(e['actor'], int)]
        tm = sum(e['delta'] for e in ex)
        conc = (sum(e['delta'] for e in ex if e['thread'] in top3 or e['thread'] == touched) / tm) if tm else 0.0
        esc = math.tanh(sum(e['delta'] for e in ex if e['thread'] == touched) / 6.0) if touched else 0.0
        tot += (involve + conc + esc) / 3
    return tot / M


def simulate_lb(seed, lam, T=24, A=24, P=6, PR=6, entrench=1, refuse=0.0):
    s = W(seed, A, P, PR, T, entrench, refuse)
    ctx = dict(seed=seed, lev=0, chg=0, roll=0)
    for t in range(T):
        step_season(s, t, seed, lam, ctx)
    return s.ev, ctx
