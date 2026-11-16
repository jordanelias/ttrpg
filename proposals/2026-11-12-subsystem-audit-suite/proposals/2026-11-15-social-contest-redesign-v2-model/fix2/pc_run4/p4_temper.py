from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
presser = only("press")


def quiet(v, me):
    return (only("rest") if any(o.move == "rest" for o in v.options) else smart)(v, me)


def broke_share(pp, rite, kw, n, seed, dec, DD=D):
    br = rst = nb = 0; rat = 0; endt = 0
    for i in range(n):
        inp, card, out, b = sit(pp, rite, M, (seed, i), D=DD, deciders=dec, **kw)
        bb = [x for x in out.beats if x.mover == "b"]
        br += any(x.broke for x in bb); nb += len(bb); rst += sum(x.move == "rest" for x in bb)
        c = dict(out.state.cond)["b"]; rat += c.rattles
        pb = next(p for p in inp.room if p.id == "b")
        endt += E.temper_of(pb, c, DD) >= DD["temper_break"]
    return br / n, rat / n, endt / n, rst / max(1, nb)


print(f"== P4.4-5/7 GRID: debate (turns 4), `a` presses every turn, b rests whenever he may; share of sittings b reaches the break (any broke beat) / mean rattles; n={N}")
print("   Grace->  " + "  ".join(f"G{g}       " for g in range(1, 8)))
grid = {}
for w in range(1, 8):
    row = []
    for g in range(1, 8):
        pp = copy.deepcopy(mp); pp["b"]["attributes"].update(will=w, grace=g)
        s, r, e, rs = broke_share(pp, "debate", dict(bench=BENCH, effort=3), N, "grid", {"a": presser, "b": quiet})
        grid[(w, g)] = (s, r, rs); row.append(f"{s:.2f}/{r:.1f}/{rs:.2f}")
    print(f"   Will {w}: " + "  ".join(row))
print("   (cell = share broke / mean rattles / share of b's beats that are rest)")

print("\n== W7 G7 under the harshest pressure: trial effort 4 (5 turns), a Presence-7 rung-5 judge (awe), `a` Will 7 Presence 7 presses every turn")
pp = copy.deepcopy(mp); pp["b"]["attributes"].update(will=7, grace=7); pp["a"]["attributes"].update(presence=7, will=7, attunement=7)
pp["j1"]["attributes"].update(presence=7); pp["j1"]["office"] = F.seat(5, "Crown", "major")
for rank in (1, 0):
    p2 = copy.deepcopy(pp); p2["b"]["rank"] = rank
    s, r, e, rs = broke_share(p2, "trial", dict(bench=("j1",), effort=4), 2 * N, "hi", {"a": presser, "b": quiet})
    print(f"  b rank {rank}: broke {s:.3f}, mean rattles {r:.2f}")
inp, card = host.build(p2, "trial", M, bench=("j1",), effort=4)
pb = next(p for p in inp.room if p.id == "b")
print("  temper of W7G7 by rattles 0..5:", [round(E.temper_of(pb, E.Cond(rattles=k), D), 2) for k in range(6)])

print("\n== P4.5-6 the menu at the break and after: b W3 G3 (broken at 1 rattle); views built by hand")
pp = copy.deepcopy(mp); pp["b"]["attributes"].update(will=3, grace=3)
inp, card = host.build(pp, "trial", M, bench=BENCH, effort=3)
st0 = E._start(inp); pb = next(p for p in inp.room if p.id == "b")
for k in (0, 1, 2):
    st = replace_cond = E.Sitting(tracks=st0.tracks, cond=tuple((i, E.Cond(rattles=k) if i == "b" else c) for i, c in st0.cond))
    v = build_view(inp, st, pb, draw(1, "v", "v"), 3)
    print(f"  rattles {k}: temper {E.temper_of(pb, E.Cond(rattles=k), D):.2f} broke={v.broke} moves on menu {Counter(o.move for o in v.options)}")
v = build_view(inp, st, pb, draw(1, "v", "v"), 1)
st_last = st
print(f"  rattles 2, last turn (turns_left 1): moves {Counter(o.move for o in v.options)}")
v = build_view(inp, st, pb, draw(1, "v", "v"), 0)
print(f"  rattles 2, turns_left 0: moves {Counter(o.move for o in v.options)}")
# reversibility: does rattles ever fall within a sitting? search every beat of many sittings
fell = 0; seen = 0
for i in range(300):
    inp2, card2, out2, b2 = sit(pp, "trial", M, ("rev", i), bench=BENCH, effort=4)
    prev = {}
    st = E._start(inp2)
    for x in out2.beats:
        pass
# rebuild cond trajectory by replaying the beats' `rattled` field
for i in range(300):
    inp2, card2, out2, b2 = sit(pp, "trial", M, ("rev", i), bench=BENCH, effort=4)
    r = Counter(); brk_then_not = 0; was = False
    for x in out2.beats:
        if x.mover == "b":
            if was and not x.broke: fell += 1
            was = was or x.broke; seen += x.broke
print(f"  within a sitting: b's beats marked broke {seen}; beats after a broke beat that are NOT broke {fell} (300 trials, effort 4)")
p3 = copy.deepcopy(pp); p3["b"]["rattled_ago"] = (0, 0, 0)
inp3, _ = host.build(p3, "trial", M, bench=BENCH, effort=3)
pb3 = next(p for p in inp3.room if p.id == "b"); st3 = E._start(inp3)
v3 = build_view(inp3, st3, pb3, draw(2, "v", "v"), 3)
print(f"  next sitting after three fresh rattles: strain carried {pb3.strain:.2f}, temper {E.temper_of(pb3, dict(st3.cond)['b'], D):.2f}, broke={v3.broke}, rest on menu={any(o.move=='rest' for o in v3.options)}")

print(f"\n== P4.6 what a broken man does, by temperament (trial, `a` presses every turn, b AUTOMATIC); share of b's BROKE beats by move; n={2*N}")
TEMP = (("hot proud W6 G1 grudge", dict(will=6, grace=1), dict(relationships={"a": -0.9}, pursuits={"p": 0.9}, convictions={"c": 1})),
        ("hot timid W1 G2", dict(will=1, grace=2), dict(pursuits={"p": 0.5}, convictions={"c": 3})),
        ("orator W2 G2 Pres7", dict(will=2, grace=2, presence=7), dict(pursuits={"p": 0.5})),
        ("flat W2 G2", dict(will=2, grace=2), {}),
        ("ordinary W4 G4", dict(will=4, grace=4), {}))
for lab, at, lay in TEMP:
    for tl, DD in (("shipped", D), ("temper terms off", host.dials(grain=0.0, grudge=0.0, pride=0.0))):
        pp = copy.deepcopy(mp); pp["b"]["attributes"].update(**at); pp["b"]["layers"] = lay
        mv = Counter(); mvc = Counter(); n = 0
        for i in range(2 * N):
            inp, card, out, b = sit(pp, "trial", M, ("tmp", i), bench=BENCH, effort=3, D=DD, deciders={"a": presser})
            for x in out.beats:
                if x.mover == "b":
                    (mv if x.broke else mvc)[x.move] += 1
        tot = sum(mv.values()) or 1; totc = sum(mvc.values()) or 1
        print(f"  {lab:24} [{tl:16}] broke beats {sum(mv.values()):5}: " + " ".join(f"{k} {mv[k]/tot:.2f}" for k in ("argue", "press", "concede", "rest"))
              + f" | composed beats {sum(mvc.values()):5}: " + " ".join(f"{k} {mvc[k]/totc:.2f}" for k in ("argue", "press", "concede", "rest")))

print(f"\n== P4 does provoking PAY, by temperament (trial; b automatic; `a`: press twice then best / best-argue only / automatic), rule on vs off; n={3*N}")
def p2then(v, me):
    return (only("press") if v.own.spoken < 2 else smart)(v, me)
for lab, at in (("W2 G2", dict(will=2, grace=2)), ("W3 G3", dict(will=3, grace=3)), ("W4 G4", dict(will=4, grace=4)),
                ("W6 G1 proud", dict(will=6, grace=1)), ("W1 G6", dict(will=1, grace=6)), ("W7 G7", dict(will=7, grace=7))):
    pp = copy.deepcopy(mp); pp["b"]["attributes"].update(**at); row = []
    for arm, DD in (("on", D), ("off", host.dials(temper_break=9.0))):
        r = {k: carried(pp, "trial", M, 3 * N, "pay", bench=BENCH, effort=3, D=DD, deciders=({"a": d} if d else None))
             for k, d in (("press2", p2then), ("argue", only("argue")), ("auto", None))}
        row.append(f"[{arm}] " + " ".join(f"{k} {v:.3f}" for k, v in r.items()))
    print(f"  {lab:12} " + " | ".join(row))

print(f"\n== A-136 composed NPC = view-only best chooser? count decisions where auto != smart, by temperament (trial, both auto), 300 sittings")
for lab, at in (("W4 G4", dict(will=4, grace=4)), ("W5 G5", dict(will=5, grace=5)), ("W3 G4", dict(will=3, grace=4)), ("W2 G2", dict(will=2, grace=2)), ("W6 G1", dict(will=6, grace=1))):
    pp = copy.deepcopy(mp); pp["a"]["attributes"].update(**at); pp["a"]["layers"] = dict(relationships={"b": -0.5}, pursuits={"p": 0.8}, convictions={"c": 2})
    same = diff = same0 = diff0 = 0
    def spy(v, me):
        global same, diff, same0, diff0
        a_, s_ = auto(v, me, D), smart(v, me)
        t = E.temper_of(me, v.own, D)
        if t == 0: same0 += a_ == s_; diff0 += a_ != s_
        else: same += a_ == s_; diff += a_ != s_
        return a_
    for i in range(300):
        sit(pp, "trial", M, ("spy", i), bench=BENCH, effort=3, deciders={"a": spy})
    print(f"  {lab}: temper 0 -> identical {same0}, differ {diff0}; temper > 0 -> identical {same}, differ {diff}")
