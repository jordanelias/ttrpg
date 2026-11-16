"""reproduce N's stated figures for P4/P5/P7 with N's own setups and seeds (the producer's checks were read for setup only)."""
from common import *
cast, T = F.cast(), F.TOLLS
def quiet(v, me): return (only("rest") if any(o.move == "rest" for o in v.options) else smart)(v, me)
def provoke(v, me): return (only("press") if v.own.spoken < 2 else only("argue"))(v, me)
print("A-146 (N p3:122; n=600 seed prov): low 0.84 / 0.565 vs 0.425; ordinary 0.16 / 0.257 vs 0.223; high 0 / 0.093 both")
for lab, wl, gr in (("low", 2, 2), ("ordinary", 4, 4), ("high", 7, 7)):
    pp = copy.deepcopy(mp); pp["b"]["attributes"].update(will=wl, grace=gr); row = []
    for arm, DD in (("on", D), ("off", host.dials(temper_break=9.0))):
        car = brk = nb = 0
        for i in range(600):
            inp, card, out, b = sit(pp, "debate", M, ("prov", i), bench=BENCH, effort=3, D=DD, deciders={"a": provoke, "b": quiet})
            car += b[0] in CARRIED
            for x in out.beats:
                if x.mover == "b": nb += 1; brk += x.broke
        row.append(f"[{arm}] carried {car/600:.3f} broke {brk/nb:.2f}")
    print(f"  {lab:9} " + " ".join(row))
wk = copy.deepcopy(mp); wk["b"]["attributes"].update(will=2, grace=2)
def p1(view, me): return (only("press") if view.own.spoken == 0 else only("argue"))(view, me)
OFF = host.dials(rattle_gain=0.0, show=0.0, rattle_pull=0.0, press_pull=0.0, wear=0.0)
print("D3 (N p3:41; n=300 seed d3): 0.530/0.463/0.507; control 0.480/0.463/0.363")
print("  " + " ".join(f"{lab} {rate(wk, 'trial', M, 300, 'd3', bench=BENCH, effort=3, deciders={'a': d}):.3f}/{rate(wk, 'trial', M, 300, 'd3', bench=BENCH, effort=3, deciders={'a': d}, D=OFF):.3f}" for lab, d in (("press-then-argue", p1), ("argue", only("argue")), ("press-every", only("press")))))
print("F7 uncharged (N p3:48; n=600 seed f7): argue 0.243, rest 0.300, auto 0.353")
print("  " + " ".join(f"{k} {rate(mp, 'trial', M, 600, 'f7', bench=BENCH, effort=3, deciders=({'a': d} if d else None)):.3f}" for k, d in (("argue", only("argue")), ("auto", None), ("rest", only("rest")))))
print("  same, seed 'crit' (the critic's rows):", " ".join(f"{k} {rate(mp, 'trial', M, 600, 'crit', bench=BENCH, effort=3, deciders=({'a': d} if d else None)):.3f}" for k, d in (("argue", only("argue")), ("rest", only("rest")), ("auto", None))))
print("partial judge (N p3:137; n=300 seed part): judge2 0.490, judge3 0.590; flattened 0.637/0.623")
for fl in ((), ("bearing",)):
    print("  ", fl, {j: rate(cast, "audience", dict(T, parties={"for": "scholar", "against": "bully"}), 300, "part", bench=(j,), effort=2, flat=fl) for j in ("judge2", "judge3")})
pk = copy.deepcopy(mp)
pk["b"]["layers"] = dict(pursuits={"p": 0.95}, convictions={"c": 0}, relationships={"a": -0.6}); pk["b"]["attributes"].update(will=6)
pk["j1"]["layers"] = dict(pursuits={"p": 0.1}, convictions={"c": 5}, relationships={"a": 0.5})
print("gauge (N p3:108; trial bench j1, smart chooser, seed att): 0.327/0.360/0.440 at Attunement 1/4/7")
for n in (300, 2000):
    r = {}
    for att in (1, 4, 7):
        pp = copy.deepcopy(pk); pp["a"]["attributes"]["attunement"] = att
        r[att] = rate(pp, "trial", M, n, "att", effort=3, bench=("j1",), deciders={"a": smart})
    print(f"  n={n}: {r}")
print("party-decider rows (N p3:124; n=600 seed pd): conv 0.355/0.312; quest 0.402/0.367; noble 0.248/0.273; control 0.485/0.408")
for lab, rite, who, kw, m in (("conversation", "conversation", "b", {}, M), ("questioning", "questioning", "b", {}, M), ("noble", "audience", "j1", dict(bench=("j1",)), dict(M, parties={"for": "a", "against": "j1"})), ("control trial", "trial", "b", dict(bench=BENCH), M)):
    r = {k: rate(mp, rite, m, 600, "pd", effort=3, deciders={who: d}, **kw) for k, d in (("argues", only("argue")), ("rests", only("rest")))}
    print(f"  {lab:14} argues {r['argues']:.3f} rests {r['rests']:.3f}")
