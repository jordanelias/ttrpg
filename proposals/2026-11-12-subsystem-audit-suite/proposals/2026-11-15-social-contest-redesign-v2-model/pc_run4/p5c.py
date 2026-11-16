from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")

mt = dict(id="mt", parties={"for": "a", "against": "b"}, bears={"trade": 1.0, "tolls": -1.0, "law": 0.5})
men = {"merchant": F.P("merchant", layers=dict(pursuits={"trade": 0.9}, convictions={"law": 1}, relationships={"a": 0.4}))}
pp = copy.deepcopy(mp); pp.update(men)
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
