"""P2.7: era x regime x strife -- lawful, admissible, at stake; does any outcome move?"""
import sys
from common import *
from sc2.engine import Item

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
pp = F.mid_people()
pp["a"]["attributes"].update(reason=6)
pp["a"]["items"] = (Item("old_ruling", "precedent", 0.9, source="a", about="b"),)
M = F.matter()
BENCH = ("j1", "j2", "j3", "c1", "c2", "c3")


def P(row, n=N, tag="", **kw):
    k = 0
    for i in range(n):
        inp, card, out, b = sit(pp, row, M, ("ctx", row, tag, i), bench=BENCH, floor=("crowd",), effort=3, **kw)
        k += b[0] in CARRIED
    return k / n, card


print("== lawful rites by regime:", {r: host.lawful(r) for r in host.REGIMES})
for reg in host.REGIMES:
    for row in ("debate", "inquisition"):
        try:
            host.build(pp, row, M, bench=BENCH, regime=reg); s = "built"
        except ValueError as e:
            s = f"REFUSED: {e}"
        print(f"   {row} under {reg}: {s}")

print(f"\n== trial, accuser holds a precedent (weight 0.9); P(for carried), n={N}; se ~{se(0.35,N):.3f}")
print(" regime | strife | era | silence | standard | admits precedent? | turns | stakes | P")
ref, _ = P("trial", tag="ref")
grid = {}
for reg in host.REGIMES:
    for strife in host.STRIFE:
        for era in host.ERAS:
            p, card = P("trial", tag=(reg, strife, era), regime=reg, strife=strife, era=era)
            grid[(reg, strife, era)] = p
            print(f"  {reg:9} | {strife:6} | {era:12} | {card.silence:7} | {card.standard} | {'precedent' in card.admits} | {card.turns} | "
                  f"{host.STRIFE[strife]['stakes']} | {p:.3f}{'  *' if abs(p-ref) > 2*math.hypot(se(p,N), se(ref,N)) else ''}")
print(f"  reference crown/peace/plain = {ref:.3f}; '*' = outside 2 se of reference")
import statistics as st
for axis, idx in (("regime", 0), ("strife", 1), ("era", 2)):
    lv = sorted({k[idx] for k in grid})
    print(f"  marginal by {axis}: " + ", ".join(f"{l} {st.mean(v for k, v in grid.items() if k[idx]==l):.3f}" for l in lv)
          + f" (each mean of {len(grid)//len(lv)} arms; se of a marginal ~{se(0.35, N*len(grid)//len(lv)):.3f})")

print("\n== control: context flattened (flat=('context',)) under theocracy/war/age_of_faith")
p, card = P("trial", tag="flat", regime="theocracy", strife="war", era="age_of_faith", flat=("context",))
print(f"  flattened {p:.3f} vs the same unflattened {grid[('theocracy','war','age_of_faith')]:.3f} vs reference {ref:.3f}")

print("\n== admissibility: accuser argues ONLY on evidence with his precedent; crown vs theocracy (drops precedent)")
from sc2.engine import Choice
def ev_only(view, me):
    os_ = [o for o in view.options if o.move == "argue" and o.item] or [o for o in view.options if o.move == "argue"]
    o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
for reg in ("crown", "theocracy"):
    k = 0; used = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "trial", M, ("adm", reg, i), bench=BENCH, floor=("crowd",), effort=3, regime=reg, deciders={"a": ev_only})
        k += b[0] in CARRIED; used += sum(1 for x in out.beats if x.item == "old_ruling")
    print(f"  {reg}: P {k/N:.3f}+-{se(k/N,N):.3f}; precedent cited {used/N:.2f} times/sitting")

print("\n== regime x power: a Church rung-3 accuser arranges (rig 1) against b (no office): tilt by regime")
pc = F.mid_people(); pc["a"]["office"] = F.seat(3, "Church"); pc["a"]["faction"] = "Church"
for reg in host.REGIMES:
    try:
        print(f"  {reg}: power(a) {host.power(pc['a'], reg)} tilt {host.build(pc, 'trial', M, bench=BENCH, arranger='a', rig=1.0, regime=reg)[1].tilt}")
    except ValueError as e:
        print(f"  {reg}: {e}")
