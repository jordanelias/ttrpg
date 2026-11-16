from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")

print("\n== P5.3/5 the same record credited by two hearers by tie to its SOURCE; an item that implicates a man's patron")
rec = E.Item("rec", "record", 0.7, source="clerk", about="bully")
pr = {}
for bj in ("judge", "judge2", "judge3"):
    inp, card = host.build(cast, "trial", T, bench=(bj,), floor=FL, effort=3)
    pr.update({p.id: p for p in inp.room})
for h in ("judge", "judge2", "judge3", "toll_men", "guildsmen", "clerk"):
    if h in pr:
        print(f"  credit({h:9}) = {E.credit(pr[h], rec):+.2f}  bonds to clerk {E._bond(pr[h], 'clerk'):+.2f}, to bully {E._bond(pr[h], 'bully'):+.2f}")
src = E.Item("rec2", "record", 0.7, source="clerk", about=None)
p2 = copy.deepcopy(cast); p2["judge3"]["layers"]["relationships"] = {"clerk": 0.8}
inp2, _ = host.build(p2, "trial", T, bench=("judge3",), floor=FL, effort=3); pr2 = {p.id: p for p in inp2.room}
print(f"  a source-only record (about nobody): judge3 neutral {E.credit(pr['judge3'], src):+.2f} vs judge3 a friend of the clerk {E.credit(pr2['judge3'], src):+.2f}")
print(f"  -> outcome: the scholar argues the ledger (about the bully) before judge (neutral) vs judge2 (the bully's client), scholar forced to argue on evidence; n={N}")
for bench in (("judge",), ("judge2",)):
    for fl in ((), ("bearing",)):
        p = carried(cast, "trial", dict(T, strife=None), N, "ev", bench=bench, effort=3, flat=fl,
                    deciders={"scholar": force(lambda o: o.move == "argue" and o.ground == "evidence")})
        print(f"     bench {bench[0]:7} [{'flat' if fl else 'shipped'}] carried {p:.3f}")

print(f"\n== P5.6 office, faction, regime, strife: SAME matter and persons, n={N}")
def arm(people, **kw):
    return carried(people, "trial", M, N, "ctx", bench=BENCH, effort=3, **kw)
base = arm(mp)
off = copy.deepcopy(mp); off["b"]["office"] = F.seat(4, "Crown", "moderate")
part = copy.deepcopy(mp); part["a"]["faction"] = "Crown"
for j in BENCH: part[j]["faction"] = "Crown"
rows = [("control (commoners, crown, peace)", arm(mp)),
        ("accused b holds office rung4+moderate", arm(off)), ("  same, power flattened", arm(off, flat=("power",))),
        ("accuser a shares the bench's faction", arm(part)), ("  same, bearing flattened", arm(part, flat=("bearing",))),
        ("regime theocracy", arm(mp, regime="theocracy")), ("regime commune", arm(mp, regime="commune")),
        ("strife war", arm(mp, strife="war")), ("strife famine", arm(mp, strife="famine")), ("strife schism", arm(mp, strife="schism")),
        ("era age_of_faith", arm(mp, era="age_of_faith")), ("era mercantile", arm(mp, era="mercantile")),
        ("theocracy+war+faith, context flattened", arm(mp, regime="theocracy", strife="war", era="age_of_faith", flat=("context",)))]
for lab, p in rows:
    print(f"  {lab:42} carried {p:.3f}  (vs control {p-base:+.3f}, z {diff_z(p, base, N):+.1f})")
print("  the same office-holder b under crown vs theocracy (Crown seat): power", host.power(off["b"], "crown"), "->", host.power(off["b"], "theocracy"))
print(f"  office-holder b under theocracy carried {arm(off, regime='theocracy'):.3f} vs crown {arm(off):.3f}")

print(f"\n== P5.7 a party who also decides: the noble (audience: a petitions, j1 is the other party AND the bench), n={2*N}")
mn = dict(id="m", parties={"for": "a", "against": "j1"}, bears={})
for lab, d in (("argues every turn", only("argue")), ("presses", only("press")), ("rests", only("rest")), ("auto", None)):
    p = carried(mp, "audience", mn, 2 * N, "nob", bench=("j1",), effort=3, deciders=({"j1": d} if d else None))
    print(f"  noble {lab:18} petitioner carried {p:.3f}")
mn2 = dict(mn, bears={"t": -1.0}); p2 = copy.deepcopy(mp); p2["j1"]["layers"] = dict(pursuits={"t": 0.9})
inp, card = host.build(p2, "audience", mn2, bench=("j1",), effort=3)
print(f"  a noble with a stake (the plea costs him): start {next(p for p in inp.room if p.id=='j1').start:+.2f}; carried {carried(p2, 'audience', mn2, 2*N, 'nob2', bench=('j1',), effort=3):.3f} vs flattened {carried(p2, 'audience', mn2, 2*N, 'nob2', bench=('j1',), effort=3, flat=('bearing',)):.3f}")

print("\n== P5.8 a one-character sitting")
def tryit(lab, fn):
    try:
        r = fn(); print(f"  NOT refused: {lab}: {r if not isinstance(r, tuple) else r[1].decided_by}")
    except Exception as e:
        print(f"  refused: {lab}: {type(e).__name__}: {e}")
tryit("conversation, a alone (no other party, no floor)", lambda: host.build(mp, "conversation", dict(id="m", parties={"for": "a"}, bears={})))
tryit("rally, a alone (empty floor)", lambda: host.build(mp, "rally", dict(id="m", parties={"for": "a"}, bears={})))
tryit("audience, a petitions a bench of himself", lambda: host.build(mp, "audience", dict(id="m", parties={"for": "j1"}, bears={}), bench=("j1",)))
tryit("trial a vs a", lambda: host.build(mp, "trial", dict(id="m", parties={"for": "a", "against": "a"}, bears={}), bench=BENCH))
tryit("module: Input with one id", lambda: E.Input(rite=host.build(mp, "trial", M, bench=BENCH)[0].rite, matter="m",
       room=(E.Present("a", side="for", decides=True),), grounds=(), dials=D))
tryit("trial, a for, b absent from matter (no against), bench j1", lambda: host.build(mp, "trial", dict(id="m", parties={"for": "a"}, bears={}), bench=("j1",)))

print("\n== P5 roles: one person (merchant) as speaker, judge and hearer reads the same bearing")
pp2 = copy.deepcopy(pp); pp2["merchant"]["office"] = F.seat(3, "Crown")
mtr = dict(mt, parties={"for": "a", "against": "b"})
r1 = host.build(pp2, "trial", dict(mt, parties={"for": "merchant", "against": "b"}), bench=BENCH)[0]
r2 = host.build(pp2, "trial", mtr, bench=("merchant",))[0]
r3 = host.build(pp2, "trial", mtr, bench=BENCH, floor=("merchant",))[0]
g = lambda inp: next(p for p in inp.room if p.id == "merchant")
for lab, inp in (("speaker", r1), ("judge", r2), ("hearer", r3)):
    p = g(inp); print(f"  as {lab:7}: side {p.side} decides {p.decides} stake {tuple(round(x,2) for x in p.stake)} care {p.care} power {p.power} start {p.start:+.2f}")
print("  (note: as the `for` speaker the matter's parties change, so bond differs by construction)")

print("\n== P5 a witness called from the audience (cast trial: the scholar's testimony is the clerk's; clerk on the floor)")
vc = pc = rg = 0; n = 300
for i in range(n):
    inp, card, out, b = sit(cast, "trial", T, ("wit", i), bench=CB, floor=FL, effort=3,
                            deciders={"scholar": force(lambda o: o.item == "clerk_saw_it" and o.move == "argue")})
    clerk_spoke = [x for x in out.beats if x.voice == "clerk"]
    vc += bool(clerk_spoke); pc += any(x.move == "press" and x.target == "clerk" for x in out.beats)
    w = host.new_world(); host.fold(w, cast, inp, card, out, T); rg += w["regard"].get(("bully", "clerk"), 0.0)
print(f"  sittings where the clerk spoke (voice) {vc}/{n}; where the bully then pressed the clerk {pc}/{n}; bully's regard for clerk {rg/n:+.3f}")

print(f"\n== P5.4 bigger n: the tied judge steers? (trial, mid, bench j1, `for`=a), n=4000")
for kind, lay in (("neutral", {}), ("client of b (tie .5)", dict(clients=("b",))), ("client+friend of b (tie 1)", dict(clients=("b",), relationships={"b": 1.0})), ("client+friend of a (tie 1)", dict(clients=("a",), relationships={"a": 1.0}))):
    p2 = copy.deepcopy(mp); p2["j1"]["layers"] = lay
    inp, card = host.build(p2, "trial", M, bench=("j1",), effort=3)
    j = next(p for p in inp.room if p.id == "j1")
    print(f"  {kind:28} start {j.start:+.2f} carried {carried(p2, 'trial', M, 4000, 'pj4', bench=('j1',), effort=3):.3f}")
