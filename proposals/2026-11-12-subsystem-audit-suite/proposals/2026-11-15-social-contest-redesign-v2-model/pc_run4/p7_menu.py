"""P7.2-4: the played View — options, dominance over the real menus, calibration, leak, skill expression."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cast, T = F.cast(), F.TOLLS
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("c1", "c2"))),
        ("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("rally", dict(floor=("crowd",))), ("audience", dict(bench=("j1",))))
mral = dict(id="m", parties={"for": "a"}, bears={})


def mat(rite):
    return mral if rite == "rally" else M


def side_won(inp, out, b, side):
    if inp.rite.close == "consent":
        win = b[0] == "success"
    else:
        win = b[0] in CARRIED
    return win if side == "for" else not win


print("== P7.2 options on the played View, first turn and over a sitting (mid people, effort 3): count by move")
for rite, kw in ROWS:
    for who, side in (("a", "for"), ("b", "against")):
        seen = Counter(); first = None; nviews = 0
        def spy(v, me):
            global first, nviews
            if first is None: first = Counter(o.move for o in v.options)
            seen.update(o.move for o in v.options); nviews += 1
            return smart(v, me)
        try:
            inp, card, out, b = sit(mp, rite, mat(rite), ("opt", 0), effort=3, deciders={who: spy}, **kw)
        except Exception as e:
            continue
        if nviews:
            print(f"  {rite:12} {side:7}: first menu {dict(first)} (total {sum(first.values())}); over {nviews} views mean {sum(seen.values())/nviews:.1f} options")

POLS = (("argue", only("argue")), ("press", only("press")), ("rest", only("rest")), ("concede", only("concede")),
        ("answer>best", answer_else_best), ("smart", smart), ("random", None), ("auto", "AUTO"))
OPP = (("opp auto", None), ("opp random", "R"))
print(f"\n== P7.3 DOMINANCE over the REAL menus: share the chooser's side wins, per policy (forced moves fall back to the best option when absent); n={N}")
best_count = Counter(); cells = 0
for rite, kw in ROWS:
    for who, other, side in (("a", "b", "for"), ("b", "a", "against")):
        try:
            host.build(mp, rite, mat(rite), effort=3, **kw)
        except Exception:
            continue
        inp0, card0 = host.build(mp, rite, mat(rite), effort=3, **kw)
        if not dict(inp0.rite.moves).get(side):
            continue
        avail = set(dict(inp0.rite.moves)[side])
        for olab, od in OPP:
            res = {}
            for plab, pd in POLS:
                if plab in ("argue", "press", "rest", "concede") and plab not in avail:
                    continue
                k = 0
                for i in range(N):
                    dec = {}
                    if pd == "AUTO": pass
                    elif pd is None: dec[who] = rnd(("dom", i))
                    else: dec[who] = pd
                    if od == "R" and any(p.id == other and p.side for p in inp0.room): dec[other] = rnd(("opp", i))
                    inp, card, out, b = sit(mp, rite, mat(rite), ("dom", rite, i), effort=3, deciders=dec or None, **kw)
                    k += side_won(inp, out, b, side)
                res[plab] = k / N
            top = max(res.values()); winners = [p for p, v in res.items() if v >= top - 2 * se(top, N) * 1.41]
            best = max(res, key=res.get); best_count[best] += 1; cells += 1
            print(f"  {rite:12} {side:7} {olab:10} " + " ".join(f"{p} {v:.3f}" for p, v in res.items()) + f"  | best {best}; within 2se: {winners}")
print(f"  cells {cells}; best policy count {dict(best_count)}")
