"""C4: the temper (A-136, A-146): no one born broken; it cools; logged once; composed = view-best; provoking pays by temperament."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
P = only("press")
def ppl(**b):
    pp = copy.deepcopy(mp); pp["b"]["attributes"].update(b); return pp

H(f"C4.1 the grid: debate, `a` presses every turn, b rests whenever he may: share broke / mean rattles / b's beats at zero rattles marked broke (n={N // 2})")
print("   Grace->  " + "  ".join(f"G{g:<13}" for g in (1, 2, 4, 7)))
for w in (1, 2, 4, 7):
    cells = []
    for g in (1, 2, 4, 7):
        br = rat = zero = 0
        for i in range(N // 2):
            inp, card, out, b = sit(ppl(will=w, grace=g), "debate", M, ("grid", w, g, i), bench=BENCH, effort=3,
                                    deciders={"a": P, "b": only("rest")})
            bb = [x for x in out.beats if x.mover == "b"]
            br += any(x.broke for x in bb)
            rat += sum(1 for x in out.beats if x.rattled == "b")
            rk = 0
            for x in out.beats:
                if x.mover == "b" and x.broke and rk == 0:
                    zero += 1
                if x.rattled == "b":
                    rk += 1
        cells.append(f"{br/(N//2):.2f}/{rat/(N//2):.1f}/{zero}")
    print(f"   Will {w}: " + "  ".join(f"{c:14s}" for c in cells))

H("C4.2 temper by rattles in a row and cooling (Will+Grace 3, 8, 14): temper after k quick rattles; then after each beat he makes")
for wg in ((1, 2), (4, 4), (7, 7)):
    pp = ppl(will=wg[0], grace=wg[1])
    me = E.Present("b", will=wg[0], grace=wg[1])
    seq, h = [], 0.0
    for k in range(4):
        seq.append(round(E.temper_of(me, E.Cond(heat=h), D), 2)); h = (h + 1.0)
    cool = [round(E.temper_of(me, E.Cond(heat=h * (1 - D["temper_cool"]) ** j), D), 2) for j in range(4)]
    print(f"   W{wg[0]} G{wg[1]}: by rattles 0..3 {seq}; after 3 rattles, then cooling at each of his beats {cool}")

H(f"C4.3 the record: 'lost his temper' claims per break per witness; zero-rattle breaks (trial, `a` presses every turn; n={N})")
claims = breaks = zero_b = 0
for i in range(N):
    pp = ppl(will=1, grace=2)
    inp, card, out, b = sit(pp, "trial", M, ("rec", i), bench=BENCH, effort=3, deciders={"a": P})
    w = host.new_world(); host.fold(w, pp, inp, card, out, M)
    breaks += any(x.broke for x in out.beats if x.mover == "b")
    claims += sum(1 for e in w["ledgers"].get("j1", []) if e[0] == "lost his temper")
    rk = 0
    for x in out.beats:
        if x.mover == "b" and x.broke and rk == 0: zero_b += 1
        if x.rattled == "b": rk += 1
print(f"   W1 G2: sittings with a break {breaks}; the judge's 'lost his temper' claims {claims} (one per break); beats broken at zero rattles {zero_b}")

H(f"C4.4 A-136: a composed NPC is the view-best chooser: decisions where auto != top-worth, by temper below / at the break (trial, both auto, n={N})")
for wg in ((4, 4), (2, 2), (1, 2), (6, 1)):
    same_c = diff_c = same_b = diff_b = 0
    def spy(view, me):
        global same_c, diff_c, same_b, diff_b
        a_, s_ = auto(view, me, D), smart(view, me)
        if me.id == "b":
            if view.broke:
                same_b += a_ == s_; diff_b += a_ != s_
            else:
                same_c += a_ == s_; diff_c += a_ != s_
        return a_
    for i in range(N):
        sit(ppl(will=wg[0], grace=wg[1]), "trial", M, ("cmp", i), bench=BENCH, effort=3, decide=spy)
    print(f"   W{wg[0]} G{wg[1]}: composed identical {same_c}, differ {diff_c}; broken identical {same_b}, differ {diff_b}")

H(f"C4.5 does provoking PAY, by temperament (trial; b automatic; `a`: his point, two presses, then best / argue only / automatic), rule on vs off (n={N})")
def press2(view, me):                          # puts his point first (the burden), then presses twice, then his best
    return P(view, me) if 1 <= view.own.spoken <= 2 else smart(view, me)
for lab, b in (("W2 G2", dict(will=2, grace=2)), ("W4 G4", {}), ("W6 G1 proud", dict(will=6, grace=1)), ("W7 G7", dict(will=7, grace=7))):
    row = []
    for tag, DD in (("on", D), ("off", host.dials(temper_break=99.0))):
        r = [carried(ppl(**b), "trial", M, N, "prov", bench=BENCH, effort=3, D=DD, deciders={"a": pol} if pol else None)
             for pol in (press2, only("argue"), None)]
        row.append(f"[{tag}] press2 {r[0]:.3f} argue {r[1]:.3f} auto {r[2]:.3f}")
    print(f"   {lab:12s} " + " | ".join(row))

H(f"C4.6 what a broken man does, by temperament (trial, `a` presses every turn, b automatic): share of b's broken beats by move (n={N})")
for lab, b in (("hot proud W6 G1", dict(will=6, grace=1)), ("hot timid W1 G2", dict(will=1, grace=2)), ("orator W2 G2 Pres7", dict(will=2, grace=2, presence=7)), ("ordinary W4 G4", {})):
    c = Counter(); cc = Counter()
    for i in range(N):
        inp, card, out, bb = sit(ppl(**b), "trial", M, ("brk", i), bench=BENCH, effort=3, deciders={"a": P})
        for x in out.beats:
            if x.mover == "b":
                (c if x.broke else cc)[x.move] += 1
    t, tc = sum(c.values()) or 1, sum(cc.values()) or 1
    print(f"   {lab:20s} broken beats {sum(c.values()):5d}: " + " ".join(f"{m} {c[m]/t:.2f}" for m in ("argue", "press", "concede", "rest"))
          + f" | composed beats {sum(cc.values()):5d}: " + " ".join(f"{m} {cc[m]/tc:.2f}" for m in ("argue", "press", "concede", "rest")))
