"""ORDINARY-MEANING and INVERSION probes per speaker attribute."""
import sys, copy
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 800
CTL = lambda **o: host.MappingProxyType({**host.SHIPPED, **o})
def rate(pp, ctx, m, key, pred=None, **kw):
    pred = pred or (lambda inp, card, out, b: b[0] in CARRIED)
    return sum(bool(pred(*sit(pp, ctx, m, (key, i), **kw))) for i in range(n)) / n
def stats(pp, ctx, m, key, who="a", **kw):
    c = rt = br = yl = fr = nb = rs = 0
    for i in range(n):
        inp, card, out, b = sit(pp, ctx, m, (key, i), **kw)
        c += b[0] in CARRIED; yl += out.ended == "yielded" and out.ended_by == who
        for bt in out.beats:
            rt += bt.rattled == who
            if bt.mover == who: nb += 1; br += bt.broke; rs += bt.move == "rest"
    return c / n, rt / n, br / max(1, nb), yl / n, rs / max(1, nb)
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
print(f"n={n}")
# ---------------- FOCUS: heckler
print("FOCUS (speaker): a's Focus 1 vs 7")
hostile = F.matter(bears={"trade": -1.0})
def hostile_rally():
    pp = blank(); pp["crowd"]["layers"] = dict(pursuits={"trade": 0.9}); return pp
for lbl, ctx, mm, kw in (("rally, crowd hostile to a, heckle 1 (shipped)", "rally", hostile, {}),
                        ("rally, crowd hostile, heckle 0 (CONTROL)", "rally", hostile, dict(D=CTL(heckle=0.0))),
                        ("rally, crowd hostile, heckle 3", "rally", hostile, dict(D=CTL(heckle=3.0))),
                        ("rally, crowd friendly (no heat)", "rally", F.matter(bears={"trade": 1.0}), {}),
                        ("trial, b presses every turn", "trial", mat("blank"), dict(deciders={"b": forced("press")})),
                        ("trial, b presses every turn, press_pull=rattle_pull=0", "trial", mat("blank"), dict(deciders={"b": forced("press")}, D=CTL(press_pull=0.0, rattle_pull=0.0))),
                        ("trial famine (unrest .75)", "trial", mat("blank"), dict(strife="famine")),
                        ("tell famine (unrest .75)", "tell", mat("blank"), dict(strife="famine"))):
    r = {}
    for f in (1, 7):
        pp = hostile_rally() if ctx == "rally" else blank(); pp["a"]["attributes"]["focus"] = f
        r[f] = rate(pp, ctx, mm, ("omf", lbl), **kw)
    print(f"  {lbl:58} F1 {r[1]:.3f} F7 {r[7]:.3f} {d(r[1], r[7])}")
# ---------------- REASON: hostile listener, inversion re-test
print("REASON (speaker): a forced to argue on consequence; Reason 1/4/7")
for lbl, blay, bears in (("tell, matter HELPS listener b (b pursues trade .9, trade +1)", dict(pursuits={"trade": 0.9}), {"trade": 1.0}),
                         ("tell, matter HURTS listener b (b pursues tolls .9, tolls -1)", dict(pursuits={"tolls": 0.9}), {"tolls": -1.0}),
                         ("tell, matter hurts b strongly (tolls .9, conv law 5 bears -1)", dict(pursuits={"tolls": 0.9}, convictions={"law": 5}), {"tolls": -1.0, "law": -1.0})):
    for ctx in ("tell", "conversation"):
        r = {}
        for x in (1, 4, 7):
            pp = blank(); pp["b"]["layers"] = blay; pp["a"]["attributes"]["reason"] = x
            r[x] = rate(pp, ctx, F.matter(bears=bears), ("omr", lbl, ctx), deciders={"a": forced("argue")} if ctx == "tell" else {"a": lambda v, me: next(Choice(o.move, o.ground, o.item, o.relation) for o in sorted(v.options, key=lambda o: -o.ev) if o.move == "argue" and o.ground == "consequence")})
        print(f"  {ctx:12} {lbl:62} R1 {r[1]:.3f} R4 {r[4]:.3f} R7 {r[7]:.3f} {d(r[1], r[7])}")
print("  standing gap: trial, b holds office rung 5 (power ~6); a Reason 1/4/7; CONTROL gap_step=0")
for D in (None, CTL(gap_step=0.0)):
    r = {}
    for x in (1, 4, 7):
        pp = blank(); pp["b"]["office"] = F.seat(5, "Crown", "moderate"); pp["a"]["attributes"]["reason"] = x
        r[x] = rate(pp, "trial", mat("blank"), ("omg",), **({} if D is None else dict(D=D)))
    print(f"    {'shipped' if D is None else 'gap_step=0':10} R1 {r[1]:.3f} R4 {r[4]:.3f} R7 {r[7]:.3f} {d(r[1], r[7])}")
# ---------------- ATTUNEMENT: framing and gauge
print("ATTUNEMENT (speaker): listener b holds trade .8 (helped) and tolls .3 (hurt); tag a's best frame = trade")
def rich2():
    pp = blank(); pp["b"]["layers"] = dict(pursuits={"trade": 0.8, "tolls": 0.3}, convictions={"law": 2})
    pp["crowd"]["layers"] = dict(pursuits={"trade": 0.6, "grain": 0.6}); pp["j1"]["layers"] = dict(convictions={"law": 4}, pursuits={"order": 0.5}); return pp
m2 = F.matter(bears={"trade": 0.6, "tolls": -1.0, "law": 0.5, "grain": -0.5, "order": -0.5})
argcons = lambda v, me: next(Choice(o.move, o.ground, o.item, o.relation) for o in sorted(v.options, key=lambda o: -o.ev) if o.move == "argue" and o.ground == "consequence")
for ctx in ("tell", "conversation", "rally", "trial"):
    for D, lbl in ((None, "shipped"), (CTL(read_blur=0.0, bias_step=0.0), "CONTROL read_blur=0")):
        r = {}; hit = {}
        for x in (1, 4, 7):
            pp = rich2(); pp["a"]["attributes"]["attunement"] = x
            c = h = nb = 0
            for i in range(n):
                inp, card, out, b = sit(pp, ctx, m2, ("oma", ctx, lbl), deciders={"a": argcons}, **({} if D is None else dict(D=D)))
                c += b[0] in CARRIED
                for bt in out.beats:
                    if bt.mover == "a" and bt.frame is not None: nb += 1; h += bt.frame == "trade"
            r[x] = c / n; hit[x] = h / max(1, nb)
        print(f"  {ctx:12} {lbl:22} carried A1 {r[1]:.3f} A4 {r[4]:.3f} A7 {r[7]:.3f} {d(r[1], r[7])} | frame==listeners' best (trade): {hit[1]:.2f} {hit[4]:.2f} {hit[7]:.2f}")
print("  gauge: auto chooser (the NPC) in the trial, blank cast; CONTROL read_blur=bias_step=0")
for D, lbl in ((None, "shipped"), (CTL(read_blur=0.0, bias_step=0.0), "CONTROL")):
    r = {}
    for x in (1, 4, 7):
        pp = blank(); pp["a"]["attributes"]["attunement"] = x
        r[x] = rate(pp, "trial", mat("blank"), ("omgauge", lbl), **({} if D is None else dict(D=D)))
    print(f"    {lbl:10} A1 {r[1]:.3f} A4 {r[4]:.3f} A7 {r[7]:.3f} {d(r[1], r[7])}")
# ---------------- PRESENCE: crowd
print("PRESENCE (speaker): Presence 1 vs 7")
for lbl, ctx, kw in (("rally (crowd 30)", "rally", {}), ("rally, CONTROL heard_step=0", "rally", dict(D=CTL(heard_step=0.0))),
                     ("conversation (no crowd)", "conversation", {}), ("trial (crowd watching)", "trial", {}), ("tell", "tell", {})):
    r = {}
    for x in (1, 7):
        pp = blank(); pp["a"]["attributes"]["presence"] = x
        r[x] = rate(pp, ctx, mat("blank"), ("omp", lbl), **kw)
    print(f"  {lbl:40} P1 {r[1]:.3f} P7 {r[7]:.3f} {d(r[1], r[7])}")
# ---------------- GRACE: occasion standard
print("GRACE (speaker): venue standard plain 4 / formal 5 / solemn 6; Grace 1..7; b mid")
for lbl, ctx, rite in (("tell, conversation (plain)", "tell", None), ("tell, audience (formal)", None, "audience"), ("tell, inquisition (solemn)", None, "inquisition")):
    r = {}
    for x in range(1, 8):
        pp = blank(); pp["a"]["attributes"]["grace"] = x
        if ctx:
            r[x] = rate(pp, ctx, mat("blank"), ("omgr", lbl))
        else:
            c = 0
            for i in range(n):
                inp, card = host.build(pp, rite, mat("blank"), form="abridged", bench=("j1",) if rite == "audience" else ("c1",))
                from sc2.engine import proceed as PR
                out = PR(inp, draw(("omgr", lbl, i), "act", rite)); c += host.act_band(inp, out)[0] in CARRIED
            r[x] = c / n
    print(f"  {lbl:30} " + " ".join(f"G{x}:{r[x]:.3f}" for x in r))
# ---------------- WILL: rattled, gives up
print("WILL: the questioned man b (questioning; a presses every turn), b's Will 1/4/7")
for D, lbl in ((None, "shipped"), (CTL(temper_break=99.0, weary_step=0.0, awe_step=0.0), "CONTROL temper_break=99 weary=0 awe=0")):
    for x in (1, 4, 7):
        pp = blank(); pp["b"]["attributes"]["will"] = x
        c, rt, br, yl, rs = stats(pp, "questioning", mat("blank"), ("omw", lbl), who="b", deciders={"a": forced("press")}, **({} if D is None else dict(D=D)))
        print(f"  {lbl:38} Will {x}: questioner carried {c:.3f}  b rattled {rt:.2f}/sitting  b broke {br:.2f} of beats  b yielded {yl:.3f}  b rests {rs:.2f}")
print("WILL: trial, b presses a every turn; a's Will 1/4/7")
for x in (1, 4, 7):
    pp = blank(); pp["a"]["attributes"]["will"] = x
    c, rt, br, yl, rs = stats(pp, "trial", mat("blank"), ("omw2",), who="a", deciders={"b": forced("press")})
    print(f"  Will {x}: a carried {c:.3f}  a rattled {rt:.2f}  a broke {br:.2f}  a yielded {yl:.3f}  a rests {rs:.2f}")
