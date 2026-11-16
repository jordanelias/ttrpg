"""pc_run3 premise-runner-3 probes: shared fixtures and runners. Read-only use of sc2."""
import sys, os, copy, math, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sc2 import host, fixtures as F
from sc2.engine import proceed, auto, Choice
from scmodel.rng import draw
CARRIED = ("success", "overwhelming")
ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")

def blank():
    return F.mid_people()

def rich():
    pp = F.mid_people()
    pp["a"]["layers"] = dict(pursuits={"trade": 0.6})
    pp["b"]["layers"] = dict(pursuits={"tolls": 0.6})
    for j in ("j1", "j2", "j3"):
        pp[j]["layers"] = dict(convictions={"law": 4}, pursuits={"order": 0.5})
    pp["crowd"]["layers"] = dict(pursuits={"trade": 0.5, "grain": 0.5}, convictions={"faith": 3})
    return pp

def mat(kind):
    if kind == "blank":
        return F.matter()
    return F.matter(bears={"trade": 1.0, "tolls": -1.0, "law": 0.5, "grain": -0.5, "order": -0.5, "faith": 0.0})

CTX = {
    "tell":         ("conversation", dict(form="abridged")),
    "conversation": ("conversation", dict()),
    "trial":        ("trial", dict(bench=("j1",), floor=("crowd",))),
    "rally":        ("rally", dict(floor=("crowd",))),
    "questioning":  ("questioning", dict()),
    "debate":       ("debate", dict(bench=("j1", "j2", "j3"), floor=("crowd",))),
}

def sit(people, ctx, matter, key, deciders=None, decide=None, rulings=None, **kw):
    rite, base = CTX[ctx]
    k = dict(base); k.update(kw)
    inp, card = host.build(people, rite, matter, **k)
    out = proceed(inp, draw(key, "act", rite), decide, deciders, rulings)
    return inp, card, out, host.act_band(inp, out)

def ols(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    res = sum((y - my - b * (x - mx)) ** 2 for x, y in zip(xs, ys))
    se = math.sqrt(res / (n - 2) / sxx)
    return b, se

def se(p, n): return math.sqrt(max(p * (1 - p), 1e-12) / n)

def forced(kind):
    def f(view, me):
        os_ = view.options
        pick = [o for o in os_ if o.move == kind] or [o for o in os_ if o.move == "argue"] or list(os_)
        o = max(pick, key=lambda o: (o.ev, o.ground or "", o.relation))
        return Choice(o.move, o.ground, o.item, o.relation)
    return f
