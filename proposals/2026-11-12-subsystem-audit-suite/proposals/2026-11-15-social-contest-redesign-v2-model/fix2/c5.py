"""C5: each type's sitting reads as the proceeding it is named for (all-mid and the cast; automatic play)."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cast = F.cast()
T = F.TOLLS
SC = [("trial all-mid", mp, "trial", M, dict(bench=BENCH, floor=("crowd",), effort=3)),
      ("trial cast", cast, "trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), dict(bench=CB, floor=FL, effort=3)),
      ("debate all-mid", mp, "debate", M, dict(bench=BENCH, floor=("crowd",), effort=3)),
      ("debate cast", cast, "debate", dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), dict(bench=CB, floor=("guildsmen",), effort=3)),
      ("questioning all-mid", mp, "questioning", M, dict(effort=3)),
      ("questioning cast", cast, "questioning", dict(T, id="q", parties={"for": "fox", "against": "bully"}), dict(effort=3)),
      ("inquisition all-mid", mp, "inquisition", M, dict(bench=("c1", "c2", "c3"), effort=3)),
      ("negotiation cast", cast, "negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}), dict(effort=3))]
H(f"C5.1 who speaks: sittings in which a side never argues / says nothing at all; answers to points that no longer stand; standing points left unmarked (n={N})")
for lab, pp, rite, m, kw in SC:
    c = Counter()
    for i in range(N):
        inp, card, out, b = sit(pp, rite, m, ("c5", i), **kw)
        for s in ("for", "against"):
            bs = [x for x in out.beats if x.side == s]
            if not bs: continue
            c[s + " never argues"] += not any(x.move == "argue" for x in bs)
            c[s + " says nothing"] += all(x.move == "rest" for x in bs)
            c[s + " never raises"] += not any(x.relation == "raises" for x in bs)
        pts = {}
        st = None
        for x in out.beats:
            if x.relation == "answers":
                c["answers"] += 1
        c["left standing (marked)"] += sum(1 for x in out.beats if x.left is not None)
    print(f"  {lab:20s} " + "; ".join(f"{k} {v}" for k, v in sorted(c.items())))

H(f"C5.2 a conceded issue STAYS conceded and costs: the conceder's standing with those who decide, before and after his concession (trial cast, n={N})")
better = worse = 0
for i in range(N):
    inp, card, out, b = sit(cast, "trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), ("cc", i), bench=CB, floor=FL, effort=3)
    ds = [p.id for p in inp.room if p.decides]
    for x in out.beats:
        if x.move == "concede" and out.ended != "yielded":
            mv = sum(d for h, d in x.moved if h in ds) * SIGN[x.side]
            better += mv > 0; worse += mv < 0
print(f"  issue concessions that IMPROVED the conceder's standing {better}, that cost it {worse}")
H(f"C5.3 a declared close: verdicts where the band goes against the majority of seats (debate, n={N})")
against = tot = 0
for i in range(N):
    inp, card, out, b = sit(mp, "debate", M, ("dc", i), bench=BENCH, effort=3)
    ok = sum(1 for _, v in out.verdicts if v.net - v.ob >= 1)
    carried_ = b[0] in CARRIED
    tot += 1; against += carried_ != (ok >= 2)
print(f"  the band against the majority of seats in {against} of {tot}")
