"""A-141: Attunement is the gauge of the perceived worth of a contestant's choices.  PYTHONHASHSEED=0 python checks_v5.py [n]"""
import sys, copy, math
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, build_view, menu, Choice
from scmodel.rng import draw
N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
mp, M = F.mid_people(), F.matter()
pk = copy.deepcopy(mp)
pk["b"]["layers"] = dict(pursuits={"p": 0.95}, convictions={"c": 0}, relationships={"a": -0.6}); pk["b"]["attributes"].update(will=6)
pk["j1"]["layers"] = dict(pursuits={"p": 0.1}, convictions={"c": 5}, relationships={"a": 0.5})
D = host.dials(); TRUE = host.dials(read_blur=0.0, bias_step=0.0)
def H(t): print("\n== " + t)
def corr(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b); return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
H("(a) the VALUE of Attunement: the same people and menu; the chooser takes his perceived-best option; carried")
for rite, kw, m in (("trial", dict(bench=("j1",)), M), ("conversation", {}, M), ("audience", dict(bench=("j1",)), dict(id="m", parties={"for": "a"}, bears={})), ("tell (abridged)", dict(form="abridged"), M)):
    row = []
    for lab, DD in (("shipped", D), ("control: perceived = true", TRUE)):
        r = {}
        for att in (1, 4, 7):
            pp = copy.deepcopy(pk); pp["a"]["attributes"]["attunement"] = att
            r[att] = rate(pp, rite.split()[0] if rite != "tell (abridged)" else "conversation", m, N, "att", effort=3 if "form" not in kw else 0, D=DD, deciders={"a": smart}, **kw)
        d = r[7] - r[1]; row.append(f"{lab}: 1/4/7 = {r[1]:.3f}/{r[4]:.3f}/{r[7]:.3f}, 7-1 {d:+.3f} (se {math.hypot(se(r[1], N), se(r[7], N)):.3f})")
    print(f"  {rite:16} " + " | ".join(row))
H("(b) calibration: correlation of perceived with true worth over the options of first-turn menus, by Attunement")
for att in (1, 4, 7):
    pp = copy.deepcopy(pk); pp["a"]["attributes"]["attunement"] = att; pe, tr, err = [], [], []
    for i in range(400):
        inp, card = host.build(pp, "trial", M, bench=("j1",), effort=3); st = E._start(inp); me = inp.room[0]
        v = build_view(inp, st, me, draw(("cal", i), "v", "t"), 4); t = menu(inp, st, me, 4)[0]
        for o, x in zip(v.options, t):
            if o.move in ("argue", "press"): pe.append(o.ev); tr.append(x[4]); err.append(o.ev - x[4])
    print(f"  Attunement {att}: corr {corr(pe, tr):+.2f}; mean error {sum(err)/len(err):+.2f}; s.d. of error {math.sqrt(sum(e*e for e in err)/len(err)):.2f}")
H("(c) the bias is a character (Attunement 2; trial; share of his beats)")
for lab, bias, att in (("an optimist", 1.0, 2), ("no bias", 0.0, 2), ("a pessimist", -1.0, 2), ("an optimist who reads well (Attunement 7)", 1.0, 7), ("a pessimist who reads well", -1.0, 7)):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att; pp["a"]["bias"] = bias; mv = Counter(); car = 0
    for i in range(N // 2):
        inp, card, out, b = sit(pp, "trial", M, ("bias", i), bench=BENCH, effort=3); car += b[0] in CARRIED
        mv.update(x.move for x in out.beats if x.mover == "a")
    n = sum(mv.values())
    print(f"  {lab:42} argue {mv['argue']/n:.2f} press {mv['press']/n:.2f} rest {mv['rest']/n:.2f} concede {mv['concede']/n:.2f} | carried {car/(N//2):.3f}")
H("(e) no leak")
inp, card = host.build(pk, "trial", M, bench=("j1",), effort=3); me = inp.room[0]; st = E._start(inp)
vs = [build_view(inp, st, me, draw(i, "leak", "t"), 4) for i in range(3000)]; low = [v for v in vs if v.acc < 0.3]
e = lambda v, k: v.options[k].ev
kk = {(o.move, o.ground): k for k, o in enumerate(vs[0].options) if o.relation in ("raises", "presses")}
print(f"  View fields {list(E.View.__dataclass_fields__)}")
print(f"  poor readers (n={len(low)}): correlation of the errors of two options: argue consequence vs argue authority {corr([e(v, kk[('argue','consequence')]) for v in low], [e(v, kk[('argue','authority')]) for v in low]):+.3f}; argue vs press on one ground {corr([e(v, kk[('argue','consequence')]) for v in low], [e(v, kk[('press','consequence')]) for v in low]):+.3f}; an option vs the mood {corr([e(v, kk[('argue','consequence')]) for v in low], [v.mood for v in low]):+.3f}")

H("A-142 FRAMING: the frame is picked from his believed reading and lands on the listener's true interior")
from sc2.engine import frame, landing
fp = copy.deepcopy(mp)
fp["b"]["layers"] = dict(pursuits={"grain": 0.9, "glory": 0.1, "coin": 0.3}, convictions={"faith": 5, "law": 1})
fp["j1"]["layers"] = dict(pursuits={"coin": 0.9, "grain": 0.1}, convictions={"law": 5, "faith": 1})
fm = dict(id="m", parties={"for": "a", "against": "b"}, bears={"grain": 1.0, "coin": 1.0, "glory": 1.0, "faith": 1.0, "law": 1.0})
def framing(DD, att, rite="conversation", kw={}):
    pp = copy.deepcopy(fp); pp["a"]["attributes"]["attunement"] = att; hit = n = 0; fits = []
    for i in range(N // 2):
        inp, card, out, b = sit(pp, rite, fm, ("fr", i), effort=3, D=DD, deciders={"a": ground("consequence"), "b": chooser("rest")}, **kw)
        L = [p for p in inp.room if (p.decides and p.side != "for")] or [p for p in inp.room if p.side != "for"]
        best = frame(inp, L, "for", "consequence")
        for x in out.beats:
            if x.mover == "a" and x.frame: n += 1; hit += x.frame == best; fits.append(sum(h.weight * landing(h, "for", 0, x.frame) for h in L) / sum(h.weight for h in L))
    return hit / n, sum(fits) / len(fits)
from checks_v3_helpers import force
ground = lambda g: force(lambda o: o.move == "argue" and o.ground == g)
for lab, DD in (("shipped", D), ("control: a perfect reading (read_blur 0)", host.dials(read_blur=0.0)), ("control: no reading (read_blur 40)", host.dials(read_blur=40.0))):
    r = {att: framing(DD, att) for att in (1, 4, 7)}
    c1 = {att: rate(dict(copy.deepcopy(fp), a=dict(fp["a"], attributes=dict(fp["a"]["attributes"], attunement=att))), "conversation", fm, N, "frc", effort=3, D=host.dials(**dict(DD, bias_step=0.0)), deciders={"a": ground("consequence"), "b": chooser("rest")}) for att in (1, 7)}
    print(f"  [{lab}] frame is the listener's true best at Attunement 1/4/7: {r[1][0]:.2f}/{r[4][0]:.2f}/{r[7][0]:.2f}; realised fit {r[1][1]:+.2f}/{r[4][1]:+.2f}/{r[7][1]:+.2f}; carried (arguing consequence throughout) 1 -> 7: {c1[1]:.3f} -> {c1[7]:.3f} ({c1[7]-c1[1]:+.3f}, se {math.hypot(se(c1[1], N), se(c1[7], N)):.3f})")
inpb, _ = host.build(fp, "conversation", fm); inpj, _ = host.build(fp, "audience", dict(fm, parties={"for": "a"}), bench=("j1",))
B_ = [p for p in inpb.room if p.id == "b"]; J_ = [p for p in inpj.room if p.id == "j1"]
print(f"  the same reason (consequence) to two listeners: framed on `{frame(inpb, B_, 'for', 'consequence')}` for the hungry man (lands {landing(B_[0], 'for', 0, 'grain'):+.2f}) and on `{frame(inpj, J_, 'for', 'consequence')}` for the money-minded seat (lands {landing(J_[0], 'for', 0, 'coin'):+.2f}); the wrong way round they land {landing(B_[0], 'for', 0, 'coin'):+.2f} and {landing(J_[0], 'for', 0, 'grain'):+.2f}; a frame he does not hold at all {landing(B_[0], 'for', 0, 'office'):+.2f}")
cast, T = F.cast(), F.TOLLS
for lab, fl in (("the guild alone", ("guildsmen",)), ("the guild and the toll men", ("guildsmen", "toll_men")), ("guild, toll men, townsfolk", ("guildsmen", "toll_men", "townsfolk"))):
    inp, _ = host.build(cast, "rally", dict(T, parties={"for": "orator"}), floor=fl); L = [p for p in inp.room if p.decides]
    fr = frame(inp, L, "for", "consequence")
    print(f"  a split room dilutes: rally to {lab:28} framed on `{fr}`: mean landing {sum(h.weight * landing(h, 'for', 0, fr) for h in L) / sum(h.weight for h in L):+.2f}; by body {[(h.id, round(landing(h, 'for', 0, fr), 2)) for h in L]}")
print("  no leak: `frame` is called with his accuracy and his own normals; the View shows the frame chosen and its perceived worth, never a listener's weights")
