"""P2.1/P2.2 and the merged rows: does each type play by its own cells? (auto choosers, mid cast, n per row)"""
import sys
from collections import Counter
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
pp = F.mid_people()
M = F.matter()
BENCH = ("j1", "j2", "j3", "c1", "c2", "c3")
ROWS = list(host.RITES) + list(host.ALIASES)
print(f"n={N} per row; mid cast; bench {BENCH} filtered by the rite's authority; floor ('crowd',)")
print("row | close | decided_by | turns | silence | moves(for/against) | reply | beats/sitting | for: arg/prs/rst/cnc | against: arg/prs/rst/cnc | evaded/sitting | ended | bands | P(for carried)")
for row in ROWS:
    try:
        inp, card = host.build(pp, row, M, bench=BENCH, floor=("crowd",))
    except ValueError as e:
        print(f"{row}: REFUSED {e}"); continue
    mv = {"for": Counter(), "against": Counter()}; ends = Counter(); bands = Counter(); nb = 0; ev = 0
    for i in range(N):
        inp, card, out, b = sit(pp, row, M, (row, i), bench=BENCH, floor=("crowd",))
        nb += len(out.beats); ev += sum(x.evaded for x in out.beats)
        for x in out.beats:
            mv[x.side][x.move] += 1
        ends[out.ended] += 1; bands[b[0]] += 1
    f = lambda c: "/".join(str(c[k]) for k in ("argue", "press", "rest", "concede"))
    car = (bands["success"] + bands["overwhelming"]) / N
    print(f"{row} | {card.close} | {card.decided_by} | {card.turns} | {card.silence} | {dict(card.moves)} | {dict(card.reply)} | "
          f"{nb/N:.2f} | {f(mv['for'])} | {f(mv['against'])} | {ev/N:.2f} | {dict(ends)} | {dict(bands)} | {car:.3f}±{se(car,N):.3f}")
