"""F7 the card's odds against the close (stress lane B probe_card, lane C K2). Every speaker rests; a r5M arranges vs
b r2, Parliament seats. PREDICTION after: the card's odds within 2 s.e. of delivered in every row, rig 0 and 1, bench,
declared and hearers alike. Before: declared rows overstated, the rig ignored.  python -B f07_card.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
def rest(view, me):
    os_ = [o for o in view.options if o.move == "rest"] or list(view.options)
    o = os_[0]; return Choice(o.move, o.ground, o.item, o.relation)
H(f"F7 card odds vs delivered when nobody speaks; n={N}; seeds ('cd',row,rg,sf,i)")
mis = tot = 0; worst = 0.0
for row in ("trial", "tribunal", "audience", "debate", "inquisition", "examination", "arbitration", "rally", "questioning", "conversation"):
    for rg in ("crown", "theocracy", "commune"):
        for sf in ("peace", "war"):
            for rig in (0.0, 1.0):
                pp = castB(pa="r5M", pb="r2", seat_fac="Parliament")
                kw = dict(bench=BENCH + ("c1", "c2", "c3"), floor=("crowd", "o1"), regime=rg, strife=sf, arranger="a", rig=rig, effort=2)
                try:
                    inp, card = host.build(pp, row, mat(), **kw)
                except ValueError:
                    continue
                k = sum(host.act_band(inp, proceed(inp, draw(("cd", row, rg, sf, i), "act", row), rest))[0] in CARRIED for i in range(N))
                p = k / N; s2 = 2 * math.sqrt(max(card.odds * (1 - card.odds), 1e-4) / N)
                bad = abs(p - card.odds) > s2; mis += bad; tot += 1; worst = max(worst, abs(p - card.odds))
                if bad or (rg == "crown" and sf == "peace"):
                    print(f"  {row:13} {rg:9} {sf:6} rig{rig}: card {card.odds:.3f} delivered {p:.3f} (2se {s2:.3f}) close {card.close} seats {len(card.decided_by)}{'  <-- outside 2 s.e.' if bad else ''}", flush=True)
print(f"  cells {tot}; outside 2 s.e. {mis} (expected about {0.05*tot:.0f} by chance); largest gap {worst:.3f}")
