"""control: is the crown/peace/plain reference stable across seed tags? (explains a 3-se gap in p2_context)"""
from common import *
from sc2.engine import Item
pp = F.mid_people(); pp["a"]["attributes"].update(reason=6)
pp["a"]["items"] = (Item("old_ruling", "precedent", 0.9, source="a", about="b"),)
M = F.matter(); BENCH = ("j1", "j2", "j3", "c1", "c2", "c3")
for tag, kw in (("ref", {}), ("ref", dict(regime="crown", strife="peace", era="plain")), ("x1", {}), ("x2", {}), ("x3", {})):
    n = 400; k = sum(sit(pp, "trial", M, ("ctx", "trial", tag, i), bench=BENCH, floor=("crowd",), effort=3, **kw)[3][0] in CARRIED for i in range(n))
    print(tag, kw, k / n)
n = 3000; k = sum(sit(pp, "trial", M, ("big", i), bench=BENCH, floor=("crowd",), effort=3)[3][0] in CARRIED for i in range(n)); print("n=3000", k / n, se(k/n, n))
