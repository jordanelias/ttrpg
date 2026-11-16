"""Shared helpers for the v2 checks: runners, policies, small statistics."""
import copy, math, random
from collections import Counter
from . import host, fixtures as F
from .engine import proceed, auto, Choice
from scmodel.rng import draw

CARRIED = ("success", "overwhelming")

def se(p, n): return math.sqrt(max(p * (1 - p), 1e-12) / n)

def sit(people, rite, matter, key, deciders=None, decide=None, **kw):
    inp, card = host.build(people, rite, matter, **kw)
    out = proceed(inp, draw(key, "act", rite), decide, deciders)
    return inp, card, out, host.act_band(inp, out)

def rate(people, rite, matter, n, seed="s", pred=None, **kw):
    pred = pred or (lambda inp, card, out, b: b[0] in CARRIED)
    k = sum(bool(pred(*sit(people, rite, matter, (seed, i), **kw))) for i in range(n))
    return k / n

def smart(view, me):                      # sees ONLY the view: takes the option of greatest believed worth
    o = max(view.options, key=lambda o: o.ev)
    return Choice(o.move, o.ground, o.item, o.relation)

def chooser(kind, seed=0):
    def f(view, me):
        os_ = view.options
        if kind == "random":
            o = random.Random(hash((seed, view.n, view.mover, round(view.acc, 6)))).choice(os_)
        else:
            pick = [o for o in os_ if o.move == kind] or [o for o in os_ if o.move == "argue"] or list(os_)
            o = max(pick, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f

def sweep(people, rite, matter, who, attr, n=1500, seed="sw", levels=(1, 4, 7), **kw):
    out = {}
    for x in levels:
        pp = copy.deepcopy(people)
        for w in (who if isinstance(who, (list, tuple)) else (who,)):
            pp[w]["attributes"][attr] = x
        out[x] = rate(pp, rite, matter, n, seed, **kw)
    s = (out[levels[-1]] - out[levels[0]]) / (levels[-1] - levels[0])
    sd = math.hypot(se(out[levels[0]], n), se(out[levels[-1]], n)) / (levels[-1] - levels[0])
    return out, s, (s / sd if sd else 0.0)

BENCH = ("j1", "j2", "j3")
CB = ("judge", "judge2", "judge3")


