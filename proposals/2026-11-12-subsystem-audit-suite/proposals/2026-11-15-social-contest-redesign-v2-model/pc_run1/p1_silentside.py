"""Share of sittings in which a side never argues (no raise, no answer); and the 'declared' close vs the judges' majority."""
from collections import Counter
from common import *
cast = F.cast(); n = 400
for rite, (m, kw) in scenes().items():
    c = Counter()
    for i in range(n):
        inp, card, out, band = run(cast, rite, m, ("ss", i), **kw)
        for side in ("for", "against"):
            if any(p.side == side and dict(inp.rite.moves).get(side) for p in inp.room):
                c[side + " speaks"] += 1
                c[side + " never argues"] += not any(b.side == side and b.move == "argue" for b in out.beats)
                c[side + " never speaks a word (all rests)"] += all(b.move == "rest" for b in out.beats if b.side == side)
        if rite == "debate":
            maj = sum((v.net - v.ob) >= 1 for _, v in out.verdicts) >= 2
            c["majority of 3 for carried"] += maj
            c["  ...but band not carried"] += maj and band[0] not in CARRIED
            c["band carried, majority not"] += (band[0] in CARRIED) and not maj
    print(rite, {k: f"{v}/{n}" for k, v in c.items()})
