"""F12 lawfulness by the row requested; admits once each (stress lane B static.py).
PREDICTION after: a church row on the debate rite sits under a theocracy; the polity's debates do not; under a commune
the church's and the polity's inquisitions do not; no kind admitted twice.  python -B f12_lawful.py"""
from common import *
mp, M = F.mid_people(), F.matter()
H("F12 which rows sit, by regime (refusals keyed)")
for rg in host.REGIMES:
    out = []
    for row in list(host.RITES) + list(host.ALIASES):
        bench = ("c1", "c2", "c3") if row in ("inquisition", "inquisition_hearing", "excommunication_deliberation") else BENCH
        r = attempt(lambda: host.build(mp, row, M, bench=bench, regime=rg, effort=2)[1].kind)
        if not r.startswith("ok"):
            out.append(f"{row} {r}")
    print(f"  {rg:9}: " + ("; ".join(out) or "every row sits"))
    dup = []
    for row in host.RITES:
        try:
            ad = list(host.build(mp, row, M, bench=BENCH + ("c1", "c2"), regime=rg, effort=2)[1].admits)
        except ValueError:
            continue
        dup += [(row, k) for k in sorted(set(ad)) if ad.count(k) > 1]
    print(f"  {rg:9}: kinds admitted twice: {dup or 'none'}")
