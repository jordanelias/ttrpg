"""C1: speaking between equals; silence; the burden; the dominance matrix over the real menus per rite."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
cast = F.cast()

H(f"C1.1 the CHARGED side (accused b) under each regime; `for` carried, lower is better for him (all-mid, n={N})")
for rite, reg in (("trial", "crown"), ("trial", "theocracy"), ("trial", "commune"), ("inquisition", "crown"), ("examination", "crown")):
    bench = ("c1", "c2", "c3") if rite == "inquisition" else BENCH
    row = {}
    for lab, pol in (("rest", only("rest")), ("answer-else-rest", answer_else("rest")), ("answer-else-argue", answer_else("argue")),
                     ("argue", only("argue")), ("press", only("press")), ("auto", None)):
        dd = {"b": pol} if pol else None
        row[lab] = carried(mp, rite, M, N, "c1a", bench=bench, effort=3, regime=reg, deciders=dd)
    print(f"  {rite:12s} {reg:9s} " + "  ".join(f"{k} {v:.3f}" for k, v in row.items())
          + f"  | rest - answer-else-rest {row['rest'] - row['answer-else-rest']:+.3f} (z {z(row['rest'], row['answer-else-rest'], N):+.1f})")

H(f"C1.2 the BEARER (a) against an automatic opponent; `for` carried, higher is better for him (n={N})")
for rite, kw in (("trial", dict(bench=BENCH)), ("inquisition", dict(bench=("c1", "c2", "c3"))), ("questioning", {}),
                 ("debate", dict(bench=BENCH)), ("conversation", {}), ("audience", dict(bench=BENCH))):
    row = {}
    for lab, pol in (("rest", only("rest")), ("argue", only("argue")), ("answer-else-argue", answer_else("argue")),
                     ("press", only("press")), ("auto", None)):
        row[lab] = carried(mp, rite, M, N, "c1b", effort=3, deciders={"a": pol} if pol else None, **kw)
    print(f"  {rite:12s} " + "  ".join(f"{k} {v:.3f}" for k, v in row.items()))

H(f"C1.3 nobody speaks (both rest every turn): `for` carried (n={N}); the card's `unargued`")
for rite, kw in (("trial", dict(bench=BENCH)), ("inquisition", dict(bench=("c1", "c2", "c3"))), ("questioning", {}), ("debate", dict(bench=BENCH))):
    inp, card = host.build(mp, rite, M, effort=3, **kw)
    r = carried(mp, rite, M, N, "c1c", effort=3, decide=only("rest"), **kw)
    print(f"  {rite:12s} {r:.3f}   card: unargued = {card.unargued!r}; odds before an unmoved bench {card.odds}")

H(f"C1.4 mean move at those who decide, toward the speaker, per beat kind (all-mid, automatic, n={N} sittings)")
for name, rite, kw in (("trial", "trial", dict(bench=BENCH, floor=("crowd",))), ("debate", "debate", dict(bench=BENCH, floor=("crowd",))),
                       ("questioning", "questioning", {})):
    acc = defaultdict(list)
    for i in range(N):
        inp, card, out, b = sit(mp, rite, M, ("mv", i), effort=3, **kw)
        ds = {p.id for p in inp.room if p.decides}
        for be in out.beats:
            seen = [d for h, d in be.moved if h in ds]
            if seen:
                acc[(be.move, be.relation, "evaded" if be.evaded else "")].append(SIGN[be.side] * sum(seen) / len(seen))
    print(f"  {name}: " + "; ".join(f"{k[0]}/{k[1]}{('/' + k[2]) if k[2] else ''} n={len(v)} {sum(v)/len(v):+.2f}"
                                   for k, v in sorted(acc.items(), key=lambda kv: -len(kv[1]))))

H("C1.5 the dominance matrix: share of decision points where each option kind has the greatest TRUE worth (automatic sittings)")
_menu = E.menu
best = defaultdict(Counter)
cur = {"rite": None}
def spy(inp, st, mover, turns_left, frames=None, objects=None, acc=1.0):
    out = _menu(inp, st, mover, turns_left, frames, objects, acc)
    tr = _menu(inp, st, mover, turns_left, None, None, 1.0)[0]
    if tr:
        o = max(tr, key=lambda o: o[4])
        best[cur["rite"]][(o[0] if o[0] != "argue" else o[3])] += 1
    return out
E.menu = spy
scenes = [("trial", mp, M, dict(bench=BENCH, floor=("crowd",))), ("trial", cast, dict(F.TOLLS, parties={"for": "scholar", "against": "diplomat"}), dict(bench=CB, floor=FL)),
          ("debate", mp, M, dict(bench=BENCH)), ("debate", cast, dict(F.TOLLS, id="remit", parties={"for": "orator", "against": "diplomat"}), dict(bench=CB, floor=("guildsmen",))),
          ("questioning", mp, M, {}), ("questioning", cast, dict(F.TOLLS, id="q", parties={"for": "fox", "against": "bully"}), {}),
          ("inquisition", mp, M, dict(bench=("c1", "c2", "c3"))), ("conversation", mp, M, {}), ("negotiation", mp, M, {}),
          ("negotiation", cast, dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}), {}),
          ("audience", mp, M, dict(bench=BENCH)), ("rally", cast, dict(F.TOLLS, parties={"for": "orator"}), dict(floor=("guildsmen", "toll_men", "townsfolk")))]
for rite, pp, m, kw in scenes:
    cur["rite"] = rite
    for i in range(N // 3):
        sit(pp, rite, m, ("dom", i), effort=3, **kw)
E.menu = _menu
for rite, c in best.items():
    tot = sum(c.values())
    print(f"  {rite:12s} " + "  ".join(f"{k} {v / tot:.2f}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])) + f"  (n={tot})")
