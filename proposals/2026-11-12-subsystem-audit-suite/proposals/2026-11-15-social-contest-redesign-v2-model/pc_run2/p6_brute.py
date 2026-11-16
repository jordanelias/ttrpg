"""P6.4-6: reception by the presiding judge's Grace x station x accuracy. A PLAYED judge rules for/against
(engine `rulings`); 'wrong' is the fold's own test (ruled against his own track, |track|>1). Accuser is Guild so the
judge's faction (Crown) legitimacy carries only the reception terms."""
import sys
from collections import defaultdict
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
M = F.matter()


def cast(rung, mod, grace, reason=4):
    pp = F.mid_people()
    pp["a"]["faction"] = "Guild"; pp["b"]["faction"] = "Guild"
    pp["j1"] = F.P("j1", grace=grace, reason=reason, faction="Crown", office=(F.seat(rung, "Crown", mod) if rung is not None else None))
    # give the judge a firm lean so 'wrong' is decidable: he is tied to a (start toward for) or to b
    return pp


def cell(rung, mod, grace, how, lean, reason=4, n=N):
    pp = cast(rung, mod, grace, reason)
    pp["j1"]["layers"] = dict(relationships={lean: 1.0})
    acc = defaultdict(list)
    for i in range(n):
        inp, card = host.build(pp, "trial", M, bench=("j1",), floor=("crowd",), effort=3)
        out = proceed(inp, draw(("br", rung, mod, grace, how, lean, reason, i), "act", "trial"), None, None, {"j1": lambda jv: how})
        w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, M)
        jid, rec, wrong = w["reception"][0]
        key = "wrong" if wrong else "right"
        acc[key].append((w["legitimacy"].get("Crown", 0.0), w["compliance"][0], w.get("appeal_weight", 0.0),
                         w["regard"].get(("crowd", "j1"), 0.0), w["standing"].get("Crown", 0.0), host.power(pp["j1"])))
    return acc


def mean(xs, k): return sum(x[k] for x in xs) / len(xs) if xs else float("nan")


print(f"n={N} per cell; trial; presiding j1 played; legitimacy(Crown), compliance, appeal weight, crowd->judge regard, Crown standing")
SKIP2x2 = len(sys.argv) > 2
print("== the 2x2 at a rung-4 'moderate' judge (power 6); verdict 'for' with the judge leaning to a = right, leaning to b = wrong")
for grace in (() if SKIP2x2 else (1, 7)):
    for lean, lab in (("a", "right?"), ("b", "wrong?")):
        acc = cell(4, "moderate", grace, "for", lean)
        for k, xs in acc.items():
            print(f"  Grace {grace} {lab:6} -> fold says {k:5} (n={len(xs):3}) power {mean(xs,5):.1f}: legit {mean(xs,0):+.3f} compliance {mean(xs,1):.2f} appeal {mean(xs,2):.2f} regard {mean(xs,3):+.3f} standing {mean(xs,4):+.3f}")

print("\n== sweep Grace 1..7 x station (no office / rung 1 / rung 4 moderate / rung 6 major), right and wrong; legitimacy(Crown) | regard")
for rung, mod in ((0, None), (1, None), (4, "moderate"), (6, "major")):
    row_r, row_w = [], []
    for g in range(1, 8):
        r = cell(rung, mod, g, "for", "a", n=60)["right"]
        wr = cell(rung, mod, g, "for", "b", n=60)["wrong"]
        row_r.append(f"{mean(r,0):+.2f}/{mean(r,3):+.2f}"); row_w.append(f"{mean(wr,0):+.2f}/{mean(wr,3):+.2f}")
    pw = host.power(cast(rung, mod, 4)["j1"])
    print(f"  station rung {rung} {mod or ''} (power {pw:.0f}) RIGHT: " + "  ".join(row_r))
    print(f"  {'':>27}  WRONG: " + "  ".join(row_w))

print("\n== does Reason substitute for Grace? rung 4 moderate, Grace 1, Reason 1 vs 7 (right verdict)")
for reason in (1, 7):
    r = cell(4, "moderate", 1, "for", "a", reason=reason, n=60)["right"]
    print(f"  Reason {reason}: legit {mean(r,0):+.3f} regard {mean(r,3):+.3f}")

print("\n== simulated (drawn) judge, not played: the reception terms apply to a drawn verdict too? Grace 1 vs 7, rung 4 moderate")
for g in (1, 7):
    pp = cast(4, "moderate", g); L = []; W = 0
    for i in range(200):
        inp, card, out, b = sit(pp, "trial", M, ("sim", g, i), bench=("j1",), floor=("crowd",), effort=3)
        w = host.new_world(); host.fold(w, pp, inp, card, out, M); L.append(w["legitimacy"].get("Crown", 0.0)); W += w["reception"][0][2]
    print(f"  Grace {g}: mean legit {sum(L)/len(L):+.3f}; share judged 'wrong' {W/200:.2f}")
