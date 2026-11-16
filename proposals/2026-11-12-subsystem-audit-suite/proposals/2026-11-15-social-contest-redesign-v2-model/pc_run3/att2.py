"""Attunement re-run (fixed seeding): frame == the perfect reader's frame for those addressed; carried. And the
adjudicator's Attunement under scripted speakers (a argues every turn, b rests) and under the NPC policy."""
import sys
from common import *
from sc2 import engine as E
n = int(sys.argv[1]) if len(sys.argv) > 1 else 800
CTL = lambda **o: host.MappingProxyType({**host.SHIPPED, **o})
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
def rich2():
    pp = blank(); pp["b"]["layers"] = dict(pursuits={"trade": 0.8, "tolls": 0.3}, convictions={"law": 2})
    pp["crowd"]["layers"] = dict(pursuits={"trade": 0.6, "grain": 0.6}); pp["j1"]["layers"] = dict(convictions={"law": 4}, pursuits={"order": 0.5, "trade": 0.4}); return pp
m2 = F.matter(bears={"trade": 0.6, "tolls": -1.0, "law": 0.5, "grain": -0.5, "order": -0.5})
argcons = lambda v, me: next(Choice(o.move, o.ground, o.item, o.relation) for o in sorted(v.options, key=lambda o: -o.ev) if o.move == "argue" and o.ground == "consequence")
print("SPEAKER ATTUNEMENT, a argues on consequence every turn (frame chosen from his reading); listeners hold several wants")
for ctx in ("tell", "conversation", "rally", "trial"):
    for D, lbl in ((None, "shipped"), (CTL(read_blur=0.0, bias_step=0.0), "CONTROL read_blur=0")):
        r = {}; hit = {}
        for x in (1, 4, 7):
            pp = rich2(); pp["a"]["attributes"]["attunement"] = x
            c = h = nb = 0
            for i in range(n):
                inp, card, out, b = sit(pp, ctx, m2, ("oma2", ctx, lbl, i), deciders={"a": argcons}, **({} if D is None else dict(D=D)))
                c += b[0] in CARRIED
                a = inp.room[0]; hs = [p for p in inp.room if p.decides and p.side != "for"] or E._hearers(inp, a, "for")
                best = E.frame(inp, hs, "for", "consequence")
                for bt in out.beats:
                    if bt.mover == "a" and bt.frame is not None: nb += 1; h += bt.frame == best
            r[x] = c / n; hit[x] = h / max(1, nb)
        print(f"  {ctx:12} {lbl:20} carried A1 {r[1]:.3f} A4 {r[4]:.3f} A7 {r[7]:.3f} {d(r[1], r[7])} | frame==true best: {hit[1]:.2f} {hit[4]:.2f} {hit[7]:.2f}")
print("ADJUDICATOR ATTUNEMENT (trial, judge j1 Attunement 1/4/7), scripted: a argues every turn, b rests")
for lbl, bel, rag, D in (("a strained liar", -1.0, (0, 0), None), ("a comfortable honest man", 1.0, (), None),
                         ("a HONEST but strained man (rattled twice before)", 1.0, (0, 0), None), ("a strained liar, CONTROL ploy_step 0", -1.0, (0, 0), CTL(ploy_step=0.0))):
    r = {}
    for ja in (1, 4, 7):
        pp = blank(); pp["a"]["believes"] = {"m": bel}; pp["a"]["rattled_ago"] = rag; pp["j1"]["attributes"]["attunement"] = ja
        r[ja] = sum(sit(pp, "trial", mat("blank"), ("aa", lbl, i), deciders={"a": forced("argue"), "b": forced("rest")}, **({} if D is None else dict(D=D)))[3][0] in CARRIED for i in range(n)) / n
    print(f"  {lbl:48} A1 {r[1]:.3f} A4 {r[4]:.3f} A7 {r[7]:.3f} {d(r[1], r[7])}")
print("  NPC policy: how often the liar argues at all (share of a's beats that are argue), judge A1 vs A7")
for ja in (1, 7):
    pp = blank(); pp["a"]["believes"] = {"m": -1.0}; pp["a"]["rattled_ago"] = (0, 0); pp["j1"]["attributes"]["attunement"] = ja
    ar = nb = 0
    for i in range(n):
        inp, card, out, b = sit(pp, "trial", mat("blank"), ("aan", i))
        for bt in out.beats:
            if bt.mover == "a": nb += 1; ar += bt.move == "argue"
    print(f"    judge A{ja}: liar argues in {ar/nb:.2f} of his beats")
print("AWE on a peer: a and judge both rung 5 Crown moderate? (a as a peer: same office)")
for aw in (2, 7):
    pp = blank(); pp["a"]["attributes"]["will"] = aw; pp["a"]["office"] = F.seat(5, "Crown", "moderate"); pp["j1"]["attributes"]["presence"] = 7; pp["j1"]["office"] = F.seat(5, "Crown", "moderate")
    inp, card = host.build(pp, "trial", mat("blank"), bench=("j1",), floor=("crowd",))
    a = next(p for p in inp.room if p.id == "a"); print(f"  a Will {aw} (power {a.power}): awe {E.awe(inp, a):.2f}")
