"""F17 the three items decided, not changed, re-measured on the fixed model (stress lane A crowd2, lane B probe_era,
lane C controls K1). A8: a 30-head bloc allied with a party, by rite (the bloc decides only in a rally); B10: the
consequence share argued, by era; C7: the respondent's always-argue against the automatic chooser.
python -B f17_decided.py N"""
from common import *
from sc2.lab import rate
N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
H(f"A8 a 30-head Guild bloc, matter.factions Guild +-1; P(for), n={N}")
for rite, bench, m0 in (("trial", ("j1",), mat()), ("debate", ("j1", "j2", "j3"), mat()), ("rally", (), dict(id="m", parties={"for": "a"}, bears={}))):
    row = []
    for lab, fs, fl in (("no floor", None, ()), ("neutral", {}, ("bloc",)), ("+1 for a", {"Guild": 1.0}, ("bloc",)), ("-1 for b", {"Guild": -1.0}, ("bloc",))):
        if rite == "rally" and not fl:
            continue
        pp = {"a": F.P("a"), "b": F.P("b"), "bloc": F.P("bloc", faction="Guild", weight=30)}
        for j in ("j1", "j2", "j3"): pp[j] = F.P(j, office=F.seat(3, "Crown"))
        m = dict(m0, factions=fs or {})
        k = sum(sit(pp, rite, m, ("c2", i), bench=bench, floor=fl, effort=3)[3][0] in CARRIED for i in range(N))
        row.append(f"{lab} {pc(k, N)}")
    print(f"  {rite:7}: " + " | ".join(row), flush=True)
H(f"B10 a conversation: the share of arguments on consequence, by era (n={N}, common seeds)")
pp = castB()
for j in ("j1", "j2", "j3", "c1", "c2", "c3"): pp[j]["layers"] = dict(convictions={"law": 4})
pp["crowd"]["layers"] = dict(pursuits={"trade": 0.6}); pp["a"]["layers"] = dict(pursuits={"trade": 0.8})
m = mat(bears={"law": 0.5, "trade": 0.5})
for er in host.ERAS:
    gs = Counter(); k = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "conversation", m, ("er", "conversation", i), bench=BENCH, floor=("crowd", "o1"), effort=2, era=er)
        k += b[0] in CARRIED; gs.update(x.ground for x in out.beats if x.move == "argue")
    print(f"  {er:12} P(for) {pc(k, N)} consequence share {gs['consequence']/max(1,sum(gs.values())):.3f} (of {sum(gs.values())})", flush=True)
H(f"C7 the respondent: automatic vs always-argue (P respondent wins), n={N}")
mp, M = F.mid_people(), F.matter()
for rite, kw in (("conversation", {}), ("questioning", {}), ("trial", dict(bench=("j1",)))):
    r = {lab: rate(mp, rite, M, N, "k1", effort=3, deciders=dec, pred=lambda inp, card, out, b: b[0] == "failure", **kw)
         for lab, dec in (("auto", None), ("argue", {"b": only("argue")}))}
    print(f"  {rite:12} auto {r['auto']:.3f} argue {r['argue']:.3f} diff {r['argue']-r['auto']:+.3f} (2se {2*math.hypot(se(r['auto'],N), se(r['argue'],N)):.3f})", flush=True)
