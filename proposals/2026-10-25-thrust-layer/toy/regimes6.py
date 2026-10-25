#!/usr/bin/env python3
"""Toy world for logic-testing three narrative-emergence regimes.

BU   bottom-up: actors act on local drives only (reaction, opportunity, hostility, affinity, wander).
TD   top-down, SCRIPT: a director binds protagonist/antagonist/prize at t=0 and FORCES a five-beat schedule;
     no precondition checks (blind).
TDR  top-down, REPLAN: the same schedule, but the director re-reads state at each beat (re-picks the most
     hostile pair, relocates them) and still FORCES outcomes.  The strongest top-down: dynamic, state-reading.
HY   hybrid: actors carry standing referent-bound ambitions assigned by a tension graph (top-down at
     world-gen), with a lifecycle (fire / lapse -> successor by predicate), plus an occasion channel that
     raises declinable summonses.  No outcome is ever written by anything but an actor's act.

RNG STREAMS ARE SEPARATE (world / acts / ambition-assignment / director) so HY(w_amb=0, occasions off)
consumes the act stream exactly as BU does: that is the control (identical log hash).
Every metric is computed from the event log alone, regime-blind.
"""
import random, math, hashlib, json, statistics as st
from collections import defaultdict, Counter

T_DEF = 24
THETA = 6.0
BEAT_T = [3, 7, 12, 17, 21]
BEAT_I = [1, 2, 3, 5, 8]


def clip(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


class W:
    def __init__(s, seed, A, P, PR, T, entrench=1, refuse=0.0):
        s.rw = random.Random(seed * 7 + 1); s.ra = random.Random(seed * 7 + 2)
        s.rb = random.Random(seed * 7 + 3); s.rd = random.Random(seed * 7 + 4)
        s.A, s.P, s.PR, s.T = A, P, PR, T
        s.entrench, s.refuse = entrench, refuse
        s.death_p = 0.25
        s.terminal = False
        s.trib = False
        s.ladder = False
        s.eng = None
        s.engaged_flag = False
        s.sp_mode = False
        s.ladder_depth = 3
        s.deadline = 6
        s.cap = 2
        s.cycles = [0] * A
        s.adj = {}
        rw = s.rw
        s.place = [rw.randrange(P) for _ in range(A)]
        s.fac = [i % 4 for i in range(A)]
        s.skill = [rw.randint(1, 5) for _ in range(A)]
        s.base_skill = list(s.skill)
        s.alive = [True] * A
        s.op = [[0.0] * A for _ in range(A)]
        for i in range(A):
            for j in range(A):
                if i != j:
                    s.op[i][j] = clip((0.3 if s.fac[i] == s.fac[j] else -0.1) + rw.uniform(-0.5, 0.5))
        s.pplace = [rw.randrange(P) for _ in range(PR)]
        s.pval = [rw.choice([1, 2, 3]) for _ in range(PR)]
        s.holder = [None] * PR
        s.ev = []
        s.last_ref = {}
        s.last_harm = {}
        s.hold_since = {}
        s.amb = [None] * A
        s.amb_n = [0] * A
        s.pending_occ = {}
        s.last_occ = {}
        s.dir = None

    # ---------------------------------------------------------------- logging
    def log(s, t, actor, verb, target, ref, delta, causes, motive, grounded, forced=False, closing=False, snap=None):
        e = dict(id=len(s.ev), t=t, actor=actor, verb=verb, target=target, ref=ref, delta=delta,
                 causes=[c for c in causes if c is not None], motive=motive, grounded=grounded,
                 forced=forced, closing=closing)
        e.update(snap or {})
        s.ev.append(e)
        if ref is not None and verb not in ('summon', 'ambition_fired', 'ambition_lapsed'):
            s.last_ref[ref] = e['id']
        return e['id']

    # ---------------------------------------------------------------- grounding (decided from live state, before effects)
    def grounded(s, motive, a, b, k, t):
        if motive is None:
            return False
        m = motive[0]
        if m == 'reaction':
            h = s.last_harm.get(a)
            return bool(h and h[0] == motive[1] and t - h[2] <= 3 and h[1] == b)
        if m == 'ambition':
            am = s.amb[a]
            return bool(am and am['id'] == motive[1])
        if m == 'opportunity':
            return k is not None and s.place[a] == s.pplace[k]
        if m == 'hostility':
            return b is not None and s.op[a][b] < -0.3
        if m == 'affinity':
            return b is not None and s.op[a][b] > 0.4
        if m == 'occasion':
            return True
        if m == 'asserted':          # an author-supplied reason: grounded only if the actor's own state agrees
            if b is not None:
                return s.op[a][b] < -0.3
            if k is not None and s.holder[k] is not None and s.holder[k] != a:
                return s.op[a][s.holder[k]] < -0.3
            return False
        return False

    # ---------------------------------------------------------------- one act
    def do(s, t, a, verb, b=None, k=None, motive=None, forced=False, force_delta=None, kill=False, extra=()):
        if verb == 'claim':
            ref = f"P{k}"; tgt = s.holder[k]
            loc_ok = s.place[a] == s.pplace[k]
            tgt_alive = True if tgt is None else s.alive[tgt]
            gb = tgt
        else:
            ref = "D%d-%d" % (min(a, b), max(a, b)); tgt = b
            loc_ok = s.place[a] == s.place[b]; tgt_alive = s.alive[b]; gb = b
        snap = dict(actor_alive=s.alive[a], target_alive=tgt_alive, colocated=loc_ok)
        g = s.grounded(motive, a, gb, k, t)
        causes = [s.last_ref.get(ref)] + list(extra)
        po = s.pending_occ.pop(a, None)
        if po is not None:
            causes.append(po)
        eid = len(s.ev)
        roll = s.ra.randint(1, 6) + s.skill[a]
        refused = (s.refuse > 0 and not forced and s.ra.random() < s.refuse)
        if refused:
            roll = -99
        delta = 0.0; closing = False
        if verb == 'claim':
            diff = 5 + (s.skill[tgt] // 2 if tgt not in (None, a) else 0)
            if s.entrench and tgt not in (None, a):
                diff += min(3, (t - s.hold_since.get((tgt, k), t)) // 2)
            if forced or roll >= diff:
                prev = s.holder[k]
                s.holder[k] = a
                delta = float(force_delta if force_delta is not None else s.pval[k])
                if prev is not None and prev != a:
                    closing = True
                    s.op[prev][a] = clip(s.op[prev][a] - 0.5)
                    s.last_harm[prev] = (eid, a, t)
                s.hold_since[(a, k)] = t
        elif verb == 'harm':
            diff = 4 + s.skill[b] // 2
            if forced or roll >= diff:
                delta = float(force_delta) if force_delta is not None else 1.0
                before = s.skill[b]
                s.skill[b] = max(1, s.skill[b] - 1)
                died = kill or (before == 1 and s.ra.random() < s.death_p)
                if died:
                    s.alive[b] = False; closing = True
                    if force_delta is None:
                        delta = 3.0
                    for kk in range(s.PR):
                        if s.holder[kk] == b:
                            s.holder[kk] = None
                s.op[b][a] = clip(s.op[b][a] - 0.6)
                s.last_harm[b] = (eid, a, t)
            else:
                s.op[b][a] = clip(s.op[b][a] - 0.2)
        elif verb == 'aid':
            if forced or roll >= 4:
                delta = float(force_delta) if force_delta is not None else 0.5
                s.op[b][a] = clip(s.op[b][a] + 0.4); s.op[a][b] = clip(s.op[a][b] + 0.2)
        if verb == 'claim':
            thread = ("T%d-%d" % (min(a, tgt), max(a, tgt))) if tgt not in (None, a) else f"P{k}"
        else:
            thread = "T%d-%d" % (min(a, b), max(a, b))
        snap['thread'] = thread
        snap['engaged'] = s.engaged_flag
        e = s.eng
        if e and delta > 0 and e['t0'] <= t <= e['t1'] and e['mult'] > 1:
            other = tgt if verb == 'claim' else b
            if {a, other} == {e['p'], e['q']}:
                delta *= e['mult']
        s.log(t, a, verb, tgt if verb == 'claim' else b, ref, delta, causes, motive, g, forced, closing, snap)

    # ---------------------------------------------------------------- co-located others
    def near(s, a):
        return [x for x in range(s.A) if x != a and s.alive[x] and s.place[x] == s.place[a]]

    # ---------------------------------------------------------------- drives
    def choose(s, t, a, cfg):
        ra = s.ra
        e = s.eng
        if e and e['t0'] <= t <= e['t1'] and a in (e['p'], e['q']):
            o = e['q'] if a == e['p'] else e['p']
            if s.alive[o]:
                s.engage_act(t, a, o)
                return
        # 1 reaction
        h = s.last_harm.get(a)
        if h and t - h[2] <= 2 and s.alive[h[1]] and ra.random() < 0.6:
            if s.place[h[1]] == s.place[a]:
                s.do(t, a, 'harm', b=h[1], motive=('reaction', h[0]))
            else:
                s.place[a] = s.place[h[1]]
            return
        # 2 standing ambition (HY only; coin is not drawn at w=0 -> exact BU control)
        if cfg['amb'] and cfg['w'] > 0 and ra.random() < cfg['w']:
            am = s.amb[a]
            if am and s.ladder:
                if s.ladder_act(t, a):
                    return
            elif am:
                kind, r = am['kind'], am['ref']
                mo = ('ambition', am['id'])
                if kind == 'claim':
                    if s.holder[r] == a:
                        return
                    if s.place[a] == s.pplace[r]:
                        s.do(t, a, 'claim', k=r, motive=mo)
                    else:
                        s.place[a] = s.pplace[r]
                    return
                if kind in ('oppose', 'protect') and s.alive[r]:
                    if s.place[a] == s.place[r]:
                        s.do(t, a, 'harm' if kind == 'oppose' else 'aid', b=r, motive=mo)
                    else:
                        s.place[a] = s.place[r]
                    return
        # 3 local opportunity
        if ra.random() < 0.4:
            c = [k for k in range(s.PR) if s.pplace[k] == s.place[a] and s.holder[k] != a]
            if c:
                k = max(c, key=lambda q: s.pval[q])
                s.do(t, a, 'claim', k=k, motive=('opportunity', f"P{k}"))
                return
        nb = s.near(a)
        # 4 hostility
        if nb:
            b = min(nb, key=lambda x: s.op[a][x])
            if s.op[a][b] < -0.3 and ra.random() < 0.5:
                s.do(t, a, 'harm', b=b, motive=('hostility', b))
                return
            # 5 affinity
            b2 = max(nb, key=lambda x: s.op[a][x])
            if s.op[a][b2] > 0.4 and ra.random() < 0.3:
                s.do(t, a, 'aid', b=b2, motive=('affinity', b2))
                return
        # 6 wander
        if ra.random() < 0.25:
            s.place[a] = ra.randrange(s.P)

    # ---------------------------------------------------------------- ambitions (top-down tension graph + lifecycle)
    def new_amb(s, a, kind, ref, t):
        s.amb_n[a] += 1
        s.amb[a] = dict(id=f"A{a}.{s.amb_n[a]}", kind=kind, ref=ref, t0=t)
        if s.ladder:
            s.amb[a].update(ladder=s.build_ladder(kind, ref), idx=0, stage_t0=t)

    def build_ladder(s, kind, ref):
        d = s.ladder_depth
        if kind == 'claim':
            L = []
            if d >= 3: L += [('reach', s.pplace[ref]), ('ally', None)]
            if d >= 2: L += [('weaken', ref)]
            return L + [('hold', ref)]
        if kind == 'oppose':
            L = []
            if d >= 3: L += [('reach_p', ref)]
            if d >= 2: L += [('weaken_p', ref)]
            return L + [('defeat', ref)]
        return [('befriend', ref)]

    def stage_done(s, a, am, typ, arg, t):
        if typ == 'reach': return s.place[a] == arg
        if typ == 'reach_p': return (not s.alive[arg]) or s.place[a] == s.place[arg]
        if typ == 'ally': return any(x != a and s.alive[x] and s.op[x][a] >= 0.5 for x in range(s.A))
        if typ == 'weaken':
            h = s.holder[arg]
            return h is None or h == a or (not s.alive[h]) or s.skill[h] < s.base_skill[h]
        if typ == 'weaken_p': return (not s.alive[arg]) or s.skill[arg] < s.base_skill[arg]
        if typ == 'hold': return s.holder[arg] == a and s.hold_since.get((a, arg), 10**9) <= t - 2
        if typ == 'defeat':
            if not s.alive[arg]: return True
            return sum(1 for e in s.ev if e['actor'] == a and e.get('target') == arg and e['verb'] == 'harm' and e['delta'] > 0) >= 3
        if typ == 'befriend': return (not s.alive[arg]) or s.op[arg][a] >= 0.7
        return True

    def stage_act(s, t, a, am, typ, arg):
        mo = ('ambition', am['id'])
        if typ == 'reach':
            s.place[a] = arg; return True
        if typ == 'reach_p':
            s.place[a] = s.place[arg]; return True
        if typ == 'ally':
            nb = [x for x in s.near(a) if s.op[x][a] > -0.2]
            if nb:
                s.do(t, a, 'aid', b=max(nb, key=lambda x: s.op[x][a]), motive=mo); return True
            mates = [x for x in range(s.A) if x != a and s.alive[x] and s.fac[x] == s.fac[a]]
            if mates:
                s.place[a] = s.place[min(mates, key=lambda x: (s.place[x] != s.place[a], x))]; return True
            return False
        if typ in ('weaken', 'weaken_p', 'defeat'):
            tgt = s.holder[arg] if typ == 'weaken' else arg
            if tgt is None or tgt == a or not s.alive[tgt]: return False
            if s.place[a] == s.place[tgt]:
                s.do(t, a, 'harm', b=tgt, motive=mo)
            else:
                s.place[a] = s.place[tgt]
            return True
        if typ == 'hold':
            if s.holder[arg] == a: return True
            if s.place[a] == s.pplace[arg]:
                s.do(t, a, 'claim', k=arg, motive=mo)
            else:
                s.place[a] = s.pplace[arg]
            return True
        if typ == 'befriend':
            if not s.alive[arg]: return False
            if s.place[a] == s.place[arg]:
                s.do(t, a, 'aid', b=arg, motive=mo)
            else:
                s.place[a] = s.place[arg]
            return True
        return False

    def ladder_act(s, t, a):
        am = s.amb[a]
        guard = 0
        while am and am['idx'] < len(am['ladder']) and guard < 6:
            guard += 1
            typ, arg = am['ladder'][am['idx']]
            if s.stage_done(a, am, typ, arg, t):
                s.log(t, a, 'goal_met', None, None, 0.0, [], ('ambition', am['id']), True)
                am['idx'] += 1; am['stage_t0'] = t; continue
            if t - am['stage_t0'] > s.deadline:
                s.log(t, a, 'goal_failed', None, None, 0.0, [], ('ambition', am['id']), True)
                am['idx'] += 1; am['stage_t0'] = t; continue
            return s.stage_act(t, a, am, typ, arg)
        if am and am['idx'] >= len(am['ladder']):
            s.log(t, a, 'ambition_fired', None, None, 0.0, [], ('ambition', am['id']), True)
            s.cycles[a] += 1
            if s.cycles[a] >= s.cap:
                s.amb[a] = None
            else:
                c = [k for k in range(s.PR) if s.holder[k] != a]
                if c:
                    s.new_amb(a, 'claim', max(c, key=lambda q: s.pval[q]), t)
                else:
                    s.amb[a] = None
        return False

    def assign_ambitions(s):
        rb = s.rb
        for k in range(s.PR):
            facs = rb.sample(range(4), 2)
            for f in facs:
                pool = [a for a in range(s.A) if s.fac[a] == f and s.amb[a] is None]
                if pool:
                    s.new_amb(rb.choice(pool), 'claim', k, 0)
        for a in range(s.A):
            if s.amb[a] is None:
                if rb.random() < 0.5:
                    r = rb.choice([x for x in range(s.A) if s.fac[x] != s.fac[a]])
                    s.new_amb(a, 'oppose', r, 0)
                else:
                    r = rb.choice([x for x in range(s.A) if s.fac[x] == s.fac[a] and x != a])
                    s.new_amb(a, 'protect', r, 0)

    def lifecycle(s, t):
        for a in range(s.A):
            am = s.amb[a]
            if not am or not s.alive[a]:
                continue
            if am['kind'] == 'claim':
                if s.holder[am['ref']] == a and s.hold_since.get((a, am['ref']), 10**9) <= t - 2:
                    s.log(t, a, 'ambition_fired', None, f"P{am['ref']}", 0.0, [], ('ambition', am['id']), True)
                    if s.terminal:
                        s.amb[a] = None
                        continue
                    rivals = [x for x in range(s.A) if s.alive[x] and x != a]
                    if rivals:
                        s.new_amb(a, 'oppose', min(rivals, key=lambda x: s.op[a][x]), t)
            else:
                if not s.alive[am['ref']]:
                    s.log(t, a, 'ambition_lapsed', None, None, 0.0, [], ('ambition', am['id']), True)
                    if s.terminal:
                        s.amb[a] = None
                        continue
                    c = [k for k in range(s.PR) if s.holder[k] != a]
                    if c:
                        k = max(c, key=lambda q: s.pval[q])
                        s.new_amb(a, 'claim', k, t)
                    else:
                        rivals = [x for x in range(s.A) if s.alive[x] and x != a]
                        s.new_amb(a, 'oppose', min(rivals, key=lambda x: s.op[a][x]), t) if rivals else None

    def occasions(s, t):
        rd = s.rd
        pairs = []
        for a in range(s.A):
            am = s.amb[a]
            if not am or not s.alive[a]:
                continue
            if am['kind'] == 'oppose' and s.alive[am['ref']]:
                pairs.append((a, am['ref'], "D%d-%d" % (min(a, am['ref']), max(a, am['ref'])), s.place[am['ref']]))
            if am['kind'] == 'claim':
                for b in range(a + 1, s.A):
                    ab = s.amb[b]
                    if ab and ab['kind'] == 'claim' and ab['ref'] == am['ref'] and s.alive[b]:
                        pairs.append((a, b, f"P{am['ref']}", s.pplace[am['ref']]))
        for a, b, ref, dest in pairs:
            if s.place[a] == s.place[b]:
                continue
            le = s.last_ref.get(ref)
            if le is not None and t - s.ev[le]['t'] <= 4:
                continue
            if t - s.last_occ.get(ref, -99) <= 4:
                continue
            if rd.random() < 0.5:
                eid = s.log(t, None, 'summon', None, ref, 0.0, [], ('occasion',), True)
                s.last_occ[ref] = t
                for x in (a, b):
                    if rd.random() < 0.7:
                        s.place[x] = dest
                        s.pending_occ[x] = eid


    def tribunals(s, t, theta=None):
        theta = THETA if theta is None else theta
        """Threshold-forced moment: a pair thread whose cumulative intensity crosses theta raises a DECLINABLE
        tribunal; a decider ACTOR rules (the favoured party is the decider's own opinion). The crossing writes no outcome."""
        rd = s.rd
        cum = Counter()
        for e in s.ev:
            th = e.get('thread')
            if th and th.startswith('T') and e['delta'] > 0 and isinstance(e['actor'], int):
                cum[th] += e['delta']
        for th, c in cum.items():
            if c < theta or (th in s.adj and t - s.adj[th] <= 6):
                continue
            a, b = (int(x) for x in th[1:].split('-'))
            others = [x for x in range(s.A) if s.alive[x] and x not in (a, b)]
            if not (s.alive[a] and s.alive[b] and others):
                continue
            d = max(others, key=lambda x: (s.skill[x], -x))
            eid = s.log(t, None, 'summon', None, None, 0.0, [], ('occasion',), True, snap=dict(thread=th))
            s.adj[th] = t
            if all(rd.random() < 0.7 for _ in (a, b, d)):          # all three must accept
                f, l = (a, b) if s.op[d][a] >= s.op[d][b] else (b, a)
                for k in range(s.PR):
                    if s.holder[k] == l:
                        s.holder[k] = f; s.hold_since[(f, k)] = t
                s.op[a][b] = s.op[b][a] = 0.0
                s.op[l][d] = clip(s.op[l][d] - 0.3)
                s.log(t, d, 'rule', l, None, 5.0, [eid, s.last_ref.get("D%d-%d" % (min(a, b), max(a, b)))],
                      ('occasion', eid), True, closing=True,
                      snap=dict(thread=th, actor_alive=True, target_alive=True, colocated=True))


    def setpiece(s, t, i, mult_on):
        """A SET PIECE writes a SITUATION, never an outcome: the principals are relocated to one venue (a declared director
        write, delta 0) and, for the window, may only engage each other.  Who wins, and whether anyone dies, is theirs and the dice's."""
        d = s.dir
        alive = [a for a in range(s.A) if s.alive[a]]
        if len(alive) < 2:
            return
        if not (s.alive[d['p']] and s.alive[d['q']]):
            best = None
            for a in alive:
                for b in alive:
                    if a < b:
                        sc = s.op[a][b] + s.op[b][a]
                        if best is None or sc < best[0]:
                            best = (sc, a, b)
            _, a, b = best
            d['p'], d['q'] = (a, b) if s.skill[a] >= s.skill[b] else (b, a)
        p, q = d['p'], d['q']
        s.place[q] = s.place[p]
        s.log(t, None, 'relocate', None, None, 0.0, [], ('setpiece', i), True, forced=True,
              snap=dict(thread="T%d-%d" % (min(p, q), max(p, q))))
        dur = 2 if i == 4 else 1
        s.eng = dict(t0=t, t1=t + dur - 1, p=p, q=q, mult=(BEAT_I[i] if mult_on else 1))

    def engage_act(s, t, a, o):
        ra = s.ra
        s.place[a] = s.place[o]
        k = [kk for kk in range(s.PR) if s.pplace[kk] == s.place[a] and s.holder[kk] == o]      # contend over what the other principal holds
        op = s.op[a][o]
        r = ra.random()
        s.engaged_flag = True
        try:
            if op > 0.3 and r < 0.5:
                s.do(t, a, 'aid', b=o, motive=('affinity', o))
            elif k and r < 0.5:
                kk = max(k, key=lambda q: s.pval[q])
                s.do(t, a, 'claim', k=kk, motive=('opportunity', f"P{kk}"))
            else:
                s.do(t, a, 'harm', b=o, motive=('hostility', o))
        finally:
            s.engaged_flag = False

    # ---------------------------------------------------------------- directors
    def dir_init(s):
        rd = s.rd
        cand = [a for a in range(s.A) if s.skill[a] >= 3] or list(range(s.A))
        p = rd.choice(cand)
        q = rd.choice([x for x in range(s.A) if s.fac[x] != s.fac[p]])
        k = rd.randrange(s.PR)
        s.dir = dict(p=p, q=q, k=k)
        if not s.sp_mode:
            s.endow(0, p, k)

    def endow(s, t, p, k):
        # the director writes initial state: p holds prize k (declared as a forced event, delta 0)
        if k is not None and s.holder[k] != p:
            s.holder[k] = p; s.hold_since[(p, k)] = t
            s.log(t, p, 'endow', None, f"P{k}", 0.0, [], ('asserted', 'setup'), False, forced=True,
                  snap=dict(thread=f"P{k}"))

    def beat(s, t, i, replan):
        d = s.dir; intens = BEAT_I[i]
        if replan:
            alive = [a for a in range(s.A) if s.alive[a]]
            if not (s.alive[d['p']] and s.alive[d['q']]):
                best = None
                for a in alive:
                    for b in alive:
                        if a < b:
                            sc = s.op[a][b] + s.op[b][a]
                            if best is None or sc < best[0]:
                                best = (sc, a, b)
                _, a, b = best
                d['p'], d['q'] = (a, b) if s.skill[a] >= s.skill[b] else (b, a)
            s.place[d['q']] = s.place[d['p']]               # director relocates (declared, delta 0)
            here = [k for k in range(s.PR) if s.pplace[k] == s.place[d['p']]]
            d['k'] = here[0] if here else None
        p, q, k = d['p'], d['q'], d['k']
        if replan and k is not None and i in (0, 3):
            s.endow(t, p if i == 0 else q, k)
        if i == 0:
            if k is None:
                s.do(t, q, 'harm', b=p, motive=('hostility', p) if replan else ('asserted', 'plot'), forced=True, force_delta=intens)
            else:
                s.do(t, q, 'claim', k=k, motive=('opportunity', f"P{k}") if replan else ('asserted', 'plot'), forced=True, force_delta=intens)
        elif i in (1, 4):
            s.do(t, p, 'harm', b=q, motive=('hostility', q) if replan else ('asserted', 'plot'), forced=True,
                 force_delta=intens, kill=(i == 4))
        elif i == 2:
            s.do(t, q, 'harm', b=p, motive=('hostility', p) if replan else ('asserted', 'plot'), forced=True, force_delta=intens)
        elif i == 3:
            if k is None:
                s.do(t, p, 'harm', b=q, motive=('hostility', q) if replan else ('asserted', 'plot'), forced=True, force_delta=intens)
            else:
                s.do(t, p, 'claim', k=k, motive=('opportunity', f"P{k}") if replan else ('asserted', 'plot'), forced=True, force_delta=intens)

    # ---------------------------------------------------------------- perturbation (a player act)
    def leader(s, t):
        inv = Counter(); mass = Counter()
        for e in s.ev:
            if e['delta'] > 0 and e['ref']:
                mass[e['ref']] += e['delta']
        if not mass:
            return None
        top = mass.most_common(1)[0][0]
        for e in s.ev:
            if e['delta'] > 0 and e['ref'] == top:
                for x in (e['actor'], e['target']):
                    if isinstance(x, int) and s.alive[x]:
                        inv[x] += e['delta']
        return inv.most_common(1)[0][0] if inv else None

    def player_kill(s, t, regime):
        v = s.dir['p'] if regime in ('TD', 'TDR', 'TDS', 'TDSm') and s.alive[s.dir['p']] else s.leader(t)
        if v is None or not s.alive[v]:
            return None
        s.alive[v] = False
        for kk in range(s.PR):
            if s.holder[kk] == v:
                s.holder[kk] = None
        s.log(t, 'player', 'player_kill', v, None, 3.0, [], ('player',), True, closing=True,
              snap=dict(actor_alive=True, target_alive=True, colocated=True))
        return v


def simulate(seed, regime, A=24, P=6, PR=6, T=T_DEF, w=0.6, occ=True, life=True, perturb_t=None, entrench=1, refuse=0.0):
    s = W(seed, A, P, PR, T, entrench, refuse)
    cfg = dict(amb=(regime in ('HY', 'HYc', 'HYd', 'HYg1', 'HYg2', 'HYg3', 'HYg3d', 'HYg3s')), w=w)
    if regime in ('HYg1', 'HYg2', 'HYg3', 'HYg3d', 'HYg3s'):
        s.ladder = True; s.ladder_depth = 3 if regime in ('HYg3d', 'HYg3s') else int(regime[-1]); life = False
    if regime in ('HYc', 'HYd'):
        s.terminal = True
    if regime in ('HYd', 'HYg3d'):
        s.trib = True
    if regime in ('HY', 'HYc', 'HYd', 'HYg1', 'HYg2', 'HYg3', 'HYg3d', 'HYg3s'):
        s.assign_ambitions()
    if regime in ('TDS', 'TDSm', 'HYg3s'):
        s.sp_mode = True
    if regime in ('TD', 'TDR', 'TDS', 'TDSm', 'HYg3s'):
        s.dir_init()
    victim = None
    for t in range(T):
        for a in range(A):                      # wounds heal: one point per season toward base skill
            if s.alive[a] and s.skill[a] < s.base_skill[a]:
                s.skill[a] += 1
        if perturb_t is not None and t == perturb_t:
            victim = s.player_kill(t, regime)
        if regime in ('HY', 'HYc', 'HYd', 'HYg1', 'HYg2', 'HYg3', 'HYg3d', 'HYg3s'):
            if life:
                s.lifecycle(t)
            if occ:
                s.occasions(t)
            if s.trib:
                s.tribunals(t)
        if regime in ('TD', 'TDR') and t in BEAT_T:
            s.beat(t, BEAT_T.index(t), replan=(regime == 'TDR'))
        if regime in ('TDS', 'TDSm', 'HYg3s') and t in BEAT_T:
            s.setpiece(t, BEAT_T.index(t), mult_on=(regime == 'TDSm'))
        order = [a for a in range(A) if s.alive[a]]
        s.ra.shuffle(order)
        for a in order:
            if s.alive[a]:
                s.choose(t, a, cfg)
    global LAST
    LAST = s
    return s.ev, victim


# ======================================================================== metrics (log-only)
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
