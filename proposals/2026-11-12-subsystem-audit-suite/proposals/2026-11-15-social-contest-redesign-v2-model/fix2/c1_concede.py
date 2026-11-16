from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
cast = F.cast()
_menu = E.menu
for cs in (2.0, 1.0, 0.5):
    DD = host.dials(concede_step=cs)
    best = Counter(); conc = defaultdict(list)
    def spy(inp, st, mover, turns_left, frames=None, objects=None, acc=1.0):
        out = _menu(inp, st, mover, turns_left, frames, objects, acc)
        tr = _menu(inp, st, mover, turns_left, None, None, 1.0)[0]
        if tr:
            o = max(tr, key=lambda o: o[4]); best[o[0] if o[0] != "argue" else o[3]] += 1
        return out
    E.menu = spy
    for pp, m, kw in ((mp, M, dict(bench=BENCH)), (cast, dict(F.TOLLS, parties={"for": "scholar", "against": "diplomat"}), dict(bench=CB, floor=FL)),
                      (cast, dict(F.TOLLS, parties={"for": "bully", "against": "scholar"}), dict(bench=CB, floor=FL))):
        for i in range(N):
            inp, card, out, b = sit(pp, "trial", m, ("cc", i), effort=3, D=DD, **kw)
            conc[sum(1 for x in out.beats if x.move == "concede" and x.side == "against")].append(b[0] in CARRIED)
    E.menu = _menu
    tot = sum(best.values())
    print(f"concede_step {cs}: true-best " + " ".join(f"{k} {v/tot:.3f}" for k, v in best.most_common()),
          "| accuser carries by issues the accused conceded:", {k: (len(v), round(sum(v)/len(v), 3)) for k, v in sorted(conc.items())})
