"""fix2 helpers: the second fix pass's probes (adapted from pc_run1..4 to the current sc2 API)."""
import sys, os, copy, math, random, hashlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter, defaultdict
from sc2 import host, fixtures as F, engine as E
from sc2.engine import proceed, Choice, build_view, auto, SIGN
from sc2.lab import sit, rate, smart, chooser, se, CARRIED, BENCH, CB
from scmodel.rng import draw

mp, M = F.mid_people(), F.matter()
D = host.dials()
FL = ("guildsmen", "toll_men", "clerk")


def force(pred, fallback="best"):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)]
        if not os_:
            os_ = list(v.options)
        o = max(os_, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


only = lambda mv: force(lambda o: o.move == mv)
raise_only = force(lambda o: o.move == "argue" and o.relation == "raises")
answer_only = force(lambda o: o.move == "argue" and o.relation == "answers")


def answer_else(kind):
    """answer the standing point if he can, else `kind` (argue = his best argument, rest)."""
    def f(v, me):
        a = [o for o in v.options if o.relation == "answers"]
        if a:
            o = max(a, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
        return (only(kind))(v, me)
    return f


def carried(people, rite, m, n, seed, **kw):
    return sum(sit(people, rite, m, (seed, i), **kw)[3][0] in CARRIED for i in range(n)) / n


def z(p1, p2, n1, n2=None):
    n2 = n2 or n1
    s = math.hypot(se(p1, n1), se(p2, n2))
    return (p1 - p2) / s if s else 0.0


def H(t):
    print("\n== " + t, flush=True)
