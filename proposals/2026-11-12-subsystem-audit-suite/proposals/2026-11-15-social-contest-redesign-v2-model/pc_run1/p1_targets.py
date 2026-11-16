"""N's stated run targets for P1 that a fixture can reach: D1 buckets, D6 negotiation ends, track invariant."""
from collections import Counter
from common import *
mp = F.mid_people(); M = F.matter(); BENCH = ("j1", "j2", "j3")
def buckets(D, n=900, people=mp, m=M, kw=dict(bench=BENCH, effort=3, floor=("crowd",))):
    b = {k: [0, 0] for k in ("<=-3", "<0", "<3", ">=3")}
    for i in range(n):
        inp, card, out, band = run(people, "trial", m, ("pc1-d1", i), D=D, **kw)
        j = next(p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides)
        t = dict(out.state.tracks)[j]
        k = "<=-3" if t <= -3 else "<0" if t < 0 else "<3" if t < 3 else ">=3"
        b[k][0] += 1; b[k][1] += band[0] in CARRIED
    return {k: (v[0], round(v[1] / v[0], 3) if v[0] else None) for k, v in b.items()}
print("D1 all-mid trial, shipped:", buckets(host.dials()))
print("D1 all-mid trial, track_step 0:", buckets(host.dials(track_step=0.0)))
cast = F.cast(); m, kw = scenes()["trial"]
print("D1 cast trial, shipped:", buckets(host.dials(), 900, cast, m, kw))
c = Counter()
for i in range(900):
    inp, card, out, band = run(mp, "negotiation", M, ("pc1-d6", i), effort=3)
    c[band[0]] += 1
print("D6 all-mid negotiation (n=900):", dict(c))
viol = 0; nb = 0
for rite, (m, kw) in scenes().items():
    for i in range(200):
        inp, card, out, band = run(cast, rite, m, ("inv", i), **kw)
        T = {p.id: p.start for p in inp.room}
        for b in out.beats:
            nb += 1
            for hid, d in b.moved:
                T[hid] += d
        viol += any(abs(T[k] - v) > 1e-9 for k, v in out.state.tracks)
print(f"track == start + beats' moves: violations {viol} sittings, over {nb} beats")
