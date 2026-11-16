from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
A, R = only("argue"), only("rest")
H(f'C2.4 the party who decides, with and without a stake of his own: argue every turn vs rest (n={N})')
def staked(pp, who, s):
    pp = copy.deepcopy(pp); pp[who]["layers"] = dict(pursuits={"x": 0.8}); return pp
mx = lambda **kw: F.matter(bears={"x": -0.6}, **kw)     # the matter costs the decider what he wants
for lab, rite, m, kw, who in (("questioning b", "questioning", M, dict(effort=3), "b"),
                              ("audience noble j1", "audience", F.matter(ag="j1"), dict(bench=("j1",), effort=3), "j1"),
                              ("inquisition c1", "inquisition", F.matter(f="c1", ag="b"), dict(bench=("c1",), effort=3), "c1")):
    for tag, pp, mm in (("flat", mp, m), ("with a stake", staked(mp, who, 0.6), dict(m, bears={"x": (-0.6 if who != m["parties"]["for"] else 0.6)}))):
        r = {k: carried(pp, rite, mm, N, "c2n", deciders={who: pol}, **kw) for k, pol in (("argue", A), ("rest", R))}
        s = 1.0 if who == mm["parties"]["for"] else -1.0
        print(f"  {lab:20s} {tag:13s} argue {r['argue']:.3f} rest {r['rest']:.3f}  toward him {s*(r['argue']-r['rest']):+.3f} (z {s*z(r['argue'], r['rest'], N):+.1f})")
