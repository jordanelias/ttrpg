"""P2.2 'how long' and 'who must answer': turns by effort; a forced silence under each silence cell and regime."""
import sys
from collections import Counter
from common import *
from sc2.engine import Choice

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
pp = F.mid_people()
pp["a"]["attributes"].update(reason=6)
M = F.matter()
BENCH = ("j1", "j2", "j3", "c1", "c2", "c3")

print("== turns by effort (card.turns), crown/peace and war")
for row in host.RITES:
    t = [host.build(pp, row, M, bench=BENCH, floor=("crowd",), effort=e)[1].turns for e in (0, 1, 2, 3, 4)]
    tw = [host.build(pp, row, M, bench=BENCH, floor=("crowd",), effort=e, strife="war")[1].turns for e in (0, 1, 2, 3, 4)]
    print(f"  {row:13} effort0..4 {t}  war {tw}")


def only(move):
    def f(view, me):
        os_ = [o for o in view.options if o.move == move] or [o for o in view.options if o.move == "argue"]
        o = max(os_, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


print(f"\n== forced silence: `for` argues every turn, `against` RESTS every turn (n={N}, effort 3)")
print("   arm | silence cell | evaded beats/sitting | P(for carried) +- se | vs control arm with the rule off (contempt_step=admit_step=0)")
arms = [("trial crown", "trial", "crown"), ("trial theocracy", "trial", "theocracy"), ("trial commune", "trial", "commune"),
        ("inquisition crown", "inquisition", "crown"), ("inquisition theocracy", "inquisition", "theocracy"),
        ("questioning crown", "questioning", "crown"), ("debate crown", "debate", "crown"), ("negotiation crown", "negotiation", "crown")]
for lab, row, reg in arms:
    res = []
    for D in (host.dials(), host.dials(contempt_step=0.0, admit_step=0.0)):
        try:
            k = 0; ev = 0; sil = None; acc = 0
            for i in range(N):
                inp, card, out, b = sit(pp, row, M, ("sil", lab, i), bench=BENCH, floor=("crowd",), regime=reg, effort=3, D=D,
                                        deciders={"a": only("argue"), "b": only("rest")})
                k += b[0] in CARRIED; ev += sum(x.evaded for x in out.beats); sil = card.silence; acc += out.ended == "yielded"
            res.append((sil, ev / N, k / N))
        except ValueError as e:
            res.append(("REFUSED", 0, float("nan"))); break
    if res[0][0] == "REFUSED":
        print(f"  {lab:22} REFUSED"); continue
    (s, e, p), (_, e0, p0) = res
    print(f"  {lab:22} {s:8} evaded {e:.2f} | {p:.3f}+-{se(p,N):.3f} | rule off {p0:.3f} | diff {p-p0:+.3f} ({(p-p0)/max(1e-9, math.hypot(se(p,N), se(p0,N))):+.1f} se)")

print(f"\n== auto choosers: how often does a man rest/turn away while a point stands against him? (trial, n={N})")
ev = Counter(); rests = 0
for i in range(N):
    inp, card, out, b = sit(pp, "trial", M, ("auto", i), bench=BENCH, floor=("crowd",), effort=3)
    for x in out.beats:
        ev[(x.side, x.move, x.evaded)] += 1
print("  ", dict(ev))
