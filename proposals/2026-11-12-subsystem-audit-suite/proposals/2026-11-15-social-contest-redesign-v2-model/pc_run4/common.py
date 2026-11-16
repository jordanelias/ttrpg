"""pc_run4 helpers (premise runner 4). Read-only use of sc2; nothing here is part of the model."""
import sys, os, copy, math, random, hashlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter, defaultdict
from sc2 import host, fixtures as F, engine as E
from sc2.engine import proceed, Choice, build_view, auto
from sc2.lab import sit, rate, smart, chooser, se, CARRIED, BENCH, CB
from scmodel.rng import draw

mp, M = F.mid_people(), F.matter()
D = host.dials()


def force(pred):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)] or list(v.options)
        o = max(os_, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


only = lambda mv: force(lambda o: o.move == mv)
answer_only = force(lambda o: o.move == "argue" and o.relation == "answers")


def answer_else_best(v, me):
    """answer the standing point if one can, else the best perceived option (a 'responsive' human)."""
    a = [o for o in v.options if o.relation == "answers"]
    if a:
        o = max(a, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return smart(v, me)


def rnd(seed):
    def f(v, me):
        o = random.Random(f"{seed}|{v.n}|{v.mover}|{v.acc:.6f}").choice(v.options)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


def carried(people, rite, m, n, seed, **kw):
    k = 0
    for i in range(n):
        inp, card, out, b = sit(people, rite, m, (seed, i), **kw)
        k += b[0] in CARRIED
    return k / n


def fmt(p, n):
    return f"{p:.3f}±{2*se(p, n):.3f}"


def diff_z(p1, p2, n1, n2=None):
    n2 = n2 or n1
    s = math.hypot(se(p1, n1), se(p2, n2))
    return (p1 - p2) / s if s else 0.0
