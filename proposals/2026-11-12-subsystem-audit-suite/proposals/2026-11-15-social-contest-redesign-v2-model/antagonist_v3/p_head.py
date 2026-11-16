"""Reconciled v2: every changed claim, with its control.  PYTHONHASHSEED=0 python checks_v3.py [n]"""
import sys, copy, math, hashlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+"/..")
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, build_view, Item, Choice, p_carried
from scmodel.rng import draw
from scmodel import dice
N = 20
mp, M = F.mid_people(), F.matter()
cast, T = F.cast(), F.TOLLS
D, C = host.dials(), host.controls()
FL = ("guildsmen", "toll_men", "clerk")
def H(t): print("\n== " + t)
def force(pred):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)] or list(v.options)
        o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
    return f
only = lambda mv: force(lambda o: o.move == mv)
ground = lambda g: force(lambda o: o.move == "argue" and o.ground == g)
def sw(people, rite, m, who, attr, lv=(1, 7), n=N, **kw):
    r = {}
    for x in lv:
        pp = copy.deepcopy(people); pp[who]["attributes"][attr] = x
        r[x] = rate(pp, rite, m, n, "sw", **kw)
    d = r[lv[1]] - r[lv[0]]
    return f"{r[lv[0]]:.3f}->{r[lv[1]]:.3f} ({d:+.3f}, z {d / math.hypot(se(r[lv[0]], n), se(r[lv[1]], n)):+.1f})"

H("D1 bench reads the sitting (trial, all-mid, effort 3)")
for lab, DD in (("shipped", D), ("control track_step 0", host.dials(track_step=0.0))):
    bins = Counter(); car = Counter()
    for i in range(N):
        inp, card, out, b = sit(mp, "trial", M, ("d1", i), bench=BENCH, effort=3, D=DD)
        t = dict(out.state.tracks)["j1"]; k = "<=-3" if t <= -3 else "<0" if t < 0 else "<3" if t < 3 else ">=3"
        bins[k] += 1; car[k] += b[0] in CARRIED
    print(f"  {lab:22} " + "  ".join(f"{k} n={bins[k]} {car[k]/max(1,bins[k]):.3f}" for k in ("<=-3", "<0", "<3", ">=3")))
print(f"  excommunication (declared, quorum 2): carried {rate(mp, 'excommunication_deliberation', M, N, 'x', bench=('c1','c2','c3'), effort=2):.3f}")

H("D2 the centre (the tell, equals rank 1)")
def tell(DD, diff=None):
    if diff is not None: old = host.DIFFICULTY["routine"]; host.DIFFICULTY["routine"] = diff
    c = Counter(sit(mp, "conversation", M, ("d2", i), form="abridged", D=DD)[3][0] for i in range(N * 3))
    if diff is not None: host.DIFFICULTY["routine"] = old
    n = N * 3; return f"fail {c['failure']/n:.3f} half {c['partial']/n:.3f} carried {(c['success']+c['overwhelming'])/n:.3f}"
print(f"  v2 shipped, routine 0.5: {tell(D)} | at controls: {tell(C)} | routine 0.8: {tell(D, 0.8)}")
plain = Counter()
for i in range(N * 3):
    x = dice.SocialContestInput(pool=11.0, opposition=1.0, leverage=0.0, difficulty=0.5, obstacle_operands=(), pool_default=2, pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
    plain[dice.degree(dice.roll(x, draw(("pl", i), "a", "t")))] += 1
n = N * 3
print(f"  the PLAN's plain roll (B05.25 pool, skill-score-only opposition): fail {plain['failure']/n:.3f} half {plain['partial']/n:.3f} carried {(plain['success']+plain['overwhelming'])/n:.3f}  [A-79: .59/.16/.25]")
ok = 0
for i in range(200):
    inp, card = host.build(mp, "conversation", M, form="abridged", D=C); out = proceed(inp, draw(("eq", i), "act", "conversation"))
    rng = draw(("eq", i), "act", "conversation"); [rng.normal() for _ in range(2 * 4 + 7)]
    x = dice.SocialContestInput(pool=11.0, opposition=5.0, leverage=0.0, difficulty=0.5, obstacle_operands=(), pool_default=2, pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
    m = dice.roll(x, rng); v = out.verdicts[0][1]; ok += abs((v.net - v.ob) - (m.net - m.ob)) < 1e-9
print(f"  at control the abridged margin == the one roll under A-137's rule (opposition = Will + rank): {ok}/200")

H("D3 / F2 the rattle and the concession")
wk = copy.deepcopy(mp); wk["b"]["attributes"].update(will=2, grace=2)
def p1(view, me): return (only("press") if view.own.spoken == 0 else only("argue"))(view, me)
OFF = host.dials(rattle_gain=0.0, show=0.0, rattle_pull=0.0, press_pull=0.0, wear=0.0)
for lab, dec in (("one press then argue", p1), ("argue only", only("argue")), ("press every turn", only("press"))):
    print(f"  trial vs a Will-2 Grace-2 respondent who plays AUTOMATICALLY, `for` {lab:22} carried {rate(wk, 'trial', M, N, 'd3', bench=BENCH, effort=3, deciders={'a': dec}):.3f}; a rattle that does nothing {rate(wk, 'trial', M, N, 'd3', bench=BENCH, effort=3, deciders={'a': dec}, D=OFF):.3f}")
def yielded_to(rite, who, kw, people=mp):
    return {lab: rate(people, rite, M, N, "f2", effort=3, deciders=({who: dec} if dec else None), **kw) for lab, dec in (("concedes at once", only("concede")), ("automatic", None), ("never concedes", force(lambda o: o.move != "concede")))}
print(f"  questioning: the questioner gets what he asks (the questioned man's accept) when the questioned: {yielded_to('questioning', 'b', {})}")
print(f"  trial: `for` carried when the ACCUSED: {yielded_to('trial', 'b', dict(bench=BENCH))}  (conceding walks the ladder: fact, definition, justification, then the matter)")
print(f"  trial: `for` carried when the ACCUSER: {yielded_to('trial', 'a', dict(bench=BENCH))}; debate, the mover: {yielded_to('debate', 'a', dict(bench=BENCH))}")
full = [0, 0]
for i in range(N):
    inp, card, out, b = sit(mp, "trial", M, ("conf", i), bench=BENCH, effort=4, deciders={"b": only("concede")})
    if out.ended == "yielded": full[0] += 1; full[1] += b[0] in CARRIED
print(f"  a full confession (the accused concedes the last rung): convicted {full[1]}/{full[0]} = {full[1]/max(1,full[0]):.3f} (the close is still the bench's draw: A-14)")

H("D5 / D6")
p1_ = rate(mp, "trial", M, N * 2, "d5", bench=BENCH, effort=3); host.RITES["trial"]["bears"] = "against"
p2_ = rate(mp, "trial", M, N * 2, "d5", bench=BENCH, effort=3); host.RITES["trial"]["bears"] = "for"
print(f"  trial, `for` opens {p1_:.3f}; `against` opens {p2_:.3f}; diff {p1_-p2_:+.3f} +- {2*se(p1_, N*2)*1.41:.3f}")
c = Counter()
for i in range(N):
    inp, card, out, b = sit(mp, "negotiation", M, ("d6", i), effort=3); c[(b[0], out.ended)] += 1
print(f"  negotiation (consent): {dict(c)}: Success only where the party addressed accepted")


print("after", round(rate(mp, "trial", M, 300, "f7", bench=BENCH, effort=3, deciders={"a": only("argue")}), 3))
