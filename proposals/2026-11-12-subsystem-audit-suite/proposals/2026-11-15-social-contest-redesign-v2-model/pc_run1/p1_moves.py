"""P1.5/P1.7/P1.8: what a beat does to the deciders, by move and relation; concessions and the verdict; one-sided edge."""
import sys
from collections import defaultdict, Counter
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cast, mp = F.cast(), F.mid_people()
BENCH = ("j1", "j2", "j3")
worlds = {"all-mid trial": (mp, "trial", F.matter(), dict(bench=BENCH, effort=3, floor=("crowd",))),
          "all-mid debate": (mp, "debate", F.matter(), dict(bench=BENCH, effort=3, floor=("crowd",)))}
for k, (m, kw) in scenes().items():
    worlds["cast " + k] = (cast, k, m, kw)

for name, (pp, rite, m, kw) in worlds.items():
    acc = defaultdict(list)
    conc = defaultdict(list)
    for i in range(N):
        inp, card, out, b = run(pp, rite, m, ("mv", i), **kw)
        ds = {p.id for p in inp.room if p.decides}
        for be in out.beats:
            sg = SIGN[be.side]
            seen = {}
            for hid, d in be.moved:
                if hid in ds:
                    seen[hid] = seen.get(hid, 0.0) + d
            if seen:
                acc[(be.move, be.relation, "evaded" if be.evaded else "")].append(sg * sum(seen.values()) / len(seen))
        if inp.rite.concede == "descends":
            cs = [be for be in out.beats if be.move == "concede" and be.side == "against"]
            conc[len(cs)].append(b[0] in CARRIED)
    print(f"\n== {name} (n={N} sittings): mean move at the deciders toward the speaker's side, per beat")
    for k in sorted(acc, key=lambda k: -len(acc[k])):
        v = acc[k]
        print(f"   {k[0]:8s} {k[1]:9s} {k[2]:7s} n={len(v):5d} mean {sum(v)/len(v):+.3f}  share>0 {sum(x > 0 for x in v)/len(v):.2f}")
    if conc:
        print("   P(accuser carries) by how many issues the ACCUSED conceded:",
              {k: (len(v), round(sum(v) / len(v), 3)) for k, v in sorted(conc.items())})

print("\n== one-sided matters (no 'against' party)")
for rite, kw in (("trial", dict(bench=BENCH, effort=3, floor=("crowd",))), ("debate", dict(bench=BENCH, effort=3, floor=("crowd",))),
                 ("questioning", dict(effort=3)), ("conversation", dict(effort=3, floor=("crowd",))), ("audience", dict(bench=BENCH, effort=3))):
    try:
        inp, card, out, b = run(mp, rite, dict(id="m", parties={"for": "a"}, bears={}), ("os", 0), **kw)
        print(f"   {rite}: ran; ended {out.ended}, band {b[0]}, beats {[(x.move, x.relation) for x in out.beats]}")
    except Exception as e:
        print(f"   {rite}: {type(e).__name__}: {e!r}")
