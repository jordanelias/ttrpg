"""Test N's stated numbers on the same setup with this runner's own seeds: the toll trial (cast, bench of three
judges, floor of three, effort 3), accuser (scholar) carried; and the arranger-side rule for the accused."""
import sys
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
cast = F.cast(); T = F.TOLLS
CB = ("judge", "judge2", "judge3"); FL = ("guildsmen", "toll_men", "clerk")


def P(pp=cast, tag="", **kw):
    try:
        k = sum(sit(pp, "trial", T, ("rN", tag, i), bench=CB, floor=FL, effort=3, **kw)[3][0] in CARRIED for i in range(N))
        return k / N
    except ValueError:
        return None


claims = [("crown/peace", {}, 0.527), ("war", dict(strife="war"), 0.433), ("famine", dict(strife="famine"), 0.510),
          ("theocracy", dict(regime="theocracy"), 0.520), ("commune", dict(regime="commune"), 0.507),
          ("age of faith", dict(era="age_of_faith"), 0.507), ("mercantile", dict(era="mercantile"), 0.557),
          ("fair (bully arranges, rig 0)", dict(arranger="bully", rig=0.0), 0.527),
          ("firm (rig .5)", dict(arranger="bully", rig=0.5), 0.483), ("rigged (rig 1)", dict(arranger="bully", rig=1.0), 0.327),
          ("rigged, power flattened", dict(arranger="bully", rig=1.0, flat=("power",)), 0.577)]
print(f"n={N}; claim | N's figure | this run +- se | within 2 se (of the difference, N's se taken as ours)?")
for lab, kw, fig in claims:
    p = P(tag=lab, **kw)
    s2 = 2 * math.sqrt(2) * se(p, N)
    print(f"  {lab:30} {fig:.3f} | {p:.3f}+-{se(p,N):.3f} | {'yes' if abs(p-fig) <= s2 else 'NO'} (diff {p-fig:+.3f}, 2se {s2:.3f})")

print("\n== the accused arranges: does his tilt depend on whether he bears the accuser a grudge? (bully, rig 1)")
for rel in (-0.7, -0.1, 0.0, +0.3):
    pp = copy.deepcopy(cast); pp["bully"]["layers"]["relationships"]["scholar"] = rel
    inp, card = host.build(pp, "trial", T, bench=CB, floor=FL, effort=3, arranger="bully", rig=1.0)
    print(f"  bully's tie to the scholar {rel:+.1f}: card arranged_by {card.arranged_by} tilt {card.tilt} decided_by {card.decided_by} turns {card.turns} | accuser carried {P(pp, tag=('rel', rel), arranger='bully', rig=1.0):.3f}")

print("\n== reception, a rung-5 'moderate' judge (power 7), played, right/wrong by the fold's own test (N's table)")
from collections import defaultdict
M = F.matter()
for g in (7, 4, 1):
    pp = F.mid_people(); pp["a"]["faction"] = pp["b"]["faction"] = "Guild"
    pp["j1"] = F.P("j1", grace=g, faction="Crown", office=F.seat(5, "Crown", "moderate"))
    acc = defaultdict(list)
    for lean in ("a", "b"):
        pp["j1"]["layers"] = dict(relationships={lean: 1.0})
        for i in range(150):
            inp, card = host.build(pp, "trial", M, bench=("j1",), floor=("crowd",), effort=3)
            out = proceed(inp, draw(("r5", g, lean, i), "act", "trial"), None, None, {"j1": lambda jv: "for"})
            w = host.new_world(); host.fold(w, pp, inp, card, out, M)
            acc[w["reception"][0][2]].append((w["legitimacy"].get("Crown", 0), w["compliance"][0], w["appeal_weight"] if "appeal_weight" in w else 0, w["regard"].get(("crowd", "j1"), 0), w["standing"].get("Crown", 0)))
    for wrong, xs in sorted(acc.items()):
        print(f"  Grace {g} {'wrong' if wrong else 'right'} (n={len(xs)}): " + ", ".join(f"{sum(x[k] for x in xs)/len(xs):+.2f}" for k in range(5)))
