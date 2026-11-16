import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from collections import Counter
from sc2 import host, fixtures as F
from sc2.lab import sit, chooser
cast, T = F.cast(), F.TOLLS
CB = ("judge", "judge2", "judge3"); FL = ("guildsmen", "toll_men", "clerk")
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))), ("trial", dict(bench=CB, floor=FL)), ("debate", dict(bench=CB, floor=("guildsmen",))), ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
own = Counter(); unp = []
for rite, kw in ROWS:
    m = dict(T) if rite not in ("rally", "audience") else dict(T, parties={"for": "orator" if rite == "rally" else "scholar"})
    for i in range(300):
        dec = {} if i % 2 == 0 else {p: chooser("random", i) for p in cast}
        inp, card, out, b = sit(cast, rite, m, ("inv", i), effort=3, deciders=dec, **kw)
        for x in out.beats:
            if any(q == x.voice for q, _ in x.moved): own[(rite, x.move)] += 1
            if x.evaded and not any(d != 0 for _, d in x.moved):
                unp.append((rite, i, x.n, x.mover, x.move, x.relation, x.rattled, x.moved))
print("a speech moved its own speaker's track, by (rite, move):", dict(own))
print("evaded with no track moved:", unp)
