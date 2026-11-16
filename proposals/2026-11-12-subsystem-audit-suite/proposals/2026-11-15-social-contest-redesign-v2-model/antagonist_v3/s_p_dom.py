"""Dominance over the current menus: `for` (or the named side) plays a fixed strategy against the automatic other side. all-mid, effort 3, fresh process."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/snap")
from sc2 import host, fixtures as F
from sc2.lab import rate, se, BENCH, CARRIED
from sc2.engine import Choice
from checks_v3_helpers import force, only
mp, M = F.mid_people(), F.matter()
rite = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 800
who = "a"
kw = dict(trial=dict(bench=BENCH), debate=dict(bench=BENCH), audience=dict(bench=("j1",)), inquisition=dict(bench=("c1",)),
          rally=dict(floor=("crowd",))).get(rite, {})
m = dict(M, parties={"for": "a"}) if rite == "rally" else M
def answer_else_rest(v, me):
    a = [o for o in v.options if o.relation == "answers"]
    if a: o = max(a, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
    return only("rest")(v, me)
def press_then_argue(v, me):
    return (only("press") if v.own.spoken == 0 else only("argue"))(v, me)
strats = dict(auto=None, argue=only("argue"), press=only("press"), rest=only("rest"), concede=only("concede"),
              answer_else_rest=answer_else_rest, press_then_argue=press_then_argue)
pred = None
if rite == "negotiation":
    pred = lambda inp, card, out, b: b[0] == "success"
row = []
for k, d in strats.items():
    try:
        r = rate(mp, rite, m, n, "dom", pred=pred, effort=3, deciders=({who: d} if d else None), **kw)
    except Exception as e:
        r = float("nan")
    row.append(f"{k} {r:.3f}")
print(f"{rite:12} (for, vs automatic; n={n}, se~{se(.35, n):.3f}): " + " | ".join(row))
