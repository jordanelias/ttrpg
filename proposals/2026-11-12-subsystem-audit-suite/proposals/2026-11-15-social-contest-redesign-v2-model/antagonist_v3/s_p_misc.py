import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/snap")
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import sit, rate, CARRIED, se, BENCH
from checks_v3_helpers import force, only
from scmodel.rng import draw
mp, M = F.mid_people(), F.matter()
def z(a, b, n): return (a - b) / math.hypot(se(a, n), se(b, n))
which = sys.argv[1]
if which == "f7":
    n = 1600
    for seed in ("f7b", "f7c"):
        a = rate(mp, "trial", M, n, seed, bench=BENCH, effort=3, deciders={"a": only("argue")})
        r = rate(mp, "trial", M, n, seed, bench=BENCH, effort=3, deciders={"a": only("rest")})
        au = rate(mp, "trial", M, n, seed, bench=BENCH, effort=3)
        print(f"F7 seed {seed} n={n}: argue every turn {a:.3f}  rest every turn {r:.3f}  auto {au:.3f}  rest-argue {r-a:+.3f} z {z(r,a,n):+.1f}")
    # with perceived == true (read_blur 0, bias 0): is it the noisy choice among argue options?
    D0 = host.dials(read_blur=0.0, bias_step=0.0)
    a = rate(mp, "trial", M, n, "f7b", bench=BENCH, effort=3, deciders={"a": only("argue")}, D=D0)
    r = rate(mp, "trial", M, n, "f7b", bench=BENCH, effort=3, deciders={"a": only("rest")}, D=D0)
    print(f"F7 perceived=true: argue {a:.3f} rest {r:.3f} diff {r-a:+.3f} z {z(r,a,n):+.1f}")
if which == "rally":
    ral = dict(id="m", parties={"for": "a"}, bears={})
    rp = copy.deepcopy(mp)
    for q, cr in (("b", dict(pursuits={"p": 0.9}, convictions={"c": 1})), ("j1", dict(pursuits={"p": 0.2}, convictions={"c": 5})), ("crowd", dict(pursuits={"p": 0.9}, convictions={"c": 1}))): rp[q]["layers"] = cr
    n = 1200
    for attr in ("grace", "reason"):
        r = {}
        for x in (1, 7):
            pp = copy.deepcopy(rp); pp["a"]["attributes"][attr] = x
            r[x] = rate(pp, "rally", ral, n, "rg", floor=("crowd",), effort=3)
        print(f"rally {attr} 1->7: {r[1]:.3f}->{r[7]:.3f} ({r[7]-r[1]:+.3f}, z {z(r[7], r[1], n):+.1f}) n={n}")
    # the rally ends: does the speaker rest at once?
    for x in (1, 7):
        pp = copy.deepcopy(rp); pp["a"]["attributes"]["grace"] = x
        c = Counter(); nb = 0
        for i in range(300):
            inp, card, out, b = sit(pp, "rally", ral, ("rg", i), floor=("crowd",), effort=3)
            c[out.ended] += 1; nb += len(out.beats)
        print(f"  grace {x}: ends {dict(c)} beats/sitting {nb/300:.2f}")
if which == "noble":
    pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(pursuits={"tolls": 0.9}); m = dict(id="m", parties={"for": "a", "against": "j1"}, bears={"tolls": -1.0})
    n = 3000
    r = {fl: rate(pp, "audience", m, n, "nb2", bench=("j1",), floor=("j2",), effort=2, flat=fl) for fl in ((), ("bearing",))}
    print(f"noble steer n={n}: shipped {r[()]:.3f} flattened {r[('bearing',)]:.3f} diff {r[()]-r[('bearing',)]:+.3f} z {z(r[()], r[('bearing',)], n):+.1f}")
    # the same partial seat as a NON-party bench seat (a third man)
    pp2 = copy.deepcopy(pp); m2 = dict(id="m", parties={"for": "a", "against": "b"}, bears={"tolls": -1.0})
    r2 = {fl: rate(pp2, "audience", m2, n, "nb2", bench=("j1",), floor=("j2",), effort=2, flat=fl) for fl in ((), ("bearing",))}
    print(f"same seat, not a party: shipped {r2[()]:.3f} flattened {r2[('bearing',)]:.3f} diff {r2[()]-r2[('bearing',)]:+.3f}")
if which == "reason_sign":
    # Reason's relevance multiplies the matter's bearing: does a high-Reason speaker do WORSE where the matter hurts the listener?
    n = 1500
    for bear, lab in ((1.0, "the matter helps the listener"), (-1.0, "the matter hurts the listener")):
        r = {}
        for x in (1, 4, 7):
            pp = copy.deepcopy(mp); pp["a"]["attributes"]["reason"] = x; pp["b"]["layers"] = dict(pursuits={"t": 0.9})
            r[x] = rate(pp, "conversation", dict(M, bears={"t": bear}), n, "rs", form="abridged", deciders={"a": force(lambda o: o.move == "argue" and o.ground == "consequence")})
        print(f"tell, arguing consequence, {lab}: Reason 1/4/7 carried {r[1]:.3f}/{r[4]:.3f}/{r[7]:.3f}  (7-1 {r[7]-r[1]:+.3f}, z {z(r[7], r[1], n):+.1f})")
    inp, card = host.build(dict(mp, b=dict(mp["b"], layers=dict(pursuits={"t": 0.9}))), "conversation", dict(M, bears={"t": -1.0}), form="abridged")
    h = [p for p in inp.room if p.id == "b"][0]
    print("  landing at relevance 0 / 1 / 2:", [round(E.landing(h, "for", 0, "t", rl), 2) for rl in (0.0, 1.0, 2.0)])
if which == "leak":
    # (1) esteem on the view recovers the opponent's TRUE Grace; (2) the rest option's raw ev reveals whether their point truly stands
    ok = tot = 0
    for g in (1, 2, 3, 4):
        pp = copy.deepcopy(mp); pp["b"]["attributes"]["grace"] = g
        inp, card = host.build(pp, "trial", M, bench=BENCH, effort=3)
        st = E._start(inp); me = inp.room[0]
        v = E.build_view(inp, st, me, draw(g, "lk", "t"), 3)
        short_me = max(0.0, inp.rite.standard - me.grace)
        g_rec = inp.rite.standard - (v.esteem + short_me)
        print(f"  opponent's true Grace {g}: recovered from View.esteem {g_rec:.2f}")
    # rest ev
    inp, card = host.build(mp, "trial", M, bench=BENCH, effort=3); st0 = E._start(inp)
    agree = n = 0
    for i in range(400):
        st1, *_ = E.exchange(inp, st0, inp.room[0], E.Choice("argue", "consequence", None, "raises"), draw(("x", i), "x", "y"))
        me = inp.room[1]
        v = E.build_view(inp, st1, me, draw(("lv", i), "v", "t"), 3)
        P = next(p for p in st1.points if p.id == dict(st1.live)["for"])
        truly = E._stands(P) > 0
        rest = [o for o in v.options if o.move == "rest"][0].ev
        if v.acc < 0.3:
            n += 1; agree += (rest < 0) == truly
            seen = v.live_theirs[3] > 0; tot += seen == truly
    print(f"  poor readers n={n}: rest ev sign agrees with the TRUE 'their point stands' {agree}/{n}; the perceived point strength's sign agrees {tot}/{n}")
if which == "det":
    # determinism, draw counts, termination over random choosers, symmetry
    import hashlib
    cast, T = F.cast(), F.TOLLS
    def h(seed):
        x = hashlib.sha256()
        for rite, kw in (("trial", dict(bench=("judge", "judge2", "judge3"))), ("conversation", {}), ("questioning", {}), ("audience", dict(bench=("judge",)))):
            m = dict(T) if rite != "audience" else dict(T, parties={"for": "scholar", "against": "judge"})
            for i in range(30):
                inp, card, out, b = sit(cast, rite, m, (seed, i), effort=4, **kw)
                x.update(repr([(bb.n, bb.move, bb.margin, bb.frame, bb.relevance, bb.heard, bb.esteem) for bb in out.beats] + [b[0]]).encode())
        return x.hexdigest()[:16]
    print("  determinism:", h("d"), h("d"))
