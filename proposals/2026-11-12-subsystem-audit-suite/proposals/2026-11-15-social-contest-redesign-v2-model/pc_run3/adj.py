"""Adjudicator-side operands (A-144). Blank cast; trial before bench j1 unless stated. auto NPC choosers."""
import sys, copy
from common import *
from sc2 import engine as E
n = int(sys.argv[1]) if len(sys.argv) > 1 else 600
def rate(pp, ctx, m, key, pred=None, **kw):
    pred = pred or (lambda inp, card, out, b: b[0] in CARRIED)
    return sum(bool(pred(*sit(pp, ctx, m, (key, i), **kw))) for i in range(n)) / n
def line(lbl, vals):
    ps = [vals[x] for x in sorted(vals)]
    print(f"  {lbl:58} " + " ".join(f"{x}:{vals[x]:.3f}" for x in sorted(vals)) + f"  (d={ps[-1]-ps[0]:+.3f}, se_d={math.hypot(se(ps[0],n),se(ps[-1],n)):.3f})")
CTL = lambda **o: host.MappingProxyType({**host.SHIPPED, **o})
LV = (1, 4, 7)
m = mat("blank")
print(f"n={n} per cell")
print("A1 ADJ REASON: a sound-but-plain (R7 G2) vs b polished-unsound (R1 G7); judge j1 Reason sweep; P(for carried)")
for ctx in ("trial", "conversation", "debate"):
    for lbl, ar, ag, br, bg, D in (("sound a vs polished b", 7, 2, 1, 7, None), ("polished a vs sound b", 1, 7, 7, 2, None),
                                   ("sound a vs polished b, CONTROL relevance=0 esteem_step=0", 7, 2, 1, 7, CTL(relevance=0, esteem_step=0.0)),
                                   ("equal mid parties (null)", 4, 4, 4, 4, None)):
        v = {}
        for jr in LV:
            pp = blank(); pp["a"]["attributes"].update(reason=ar, grace=ag); pp["b"]["attributes"].update(reason=br, grace=bg)
            for j in ("j1", "j2", "j3"): pp[j]["attributes"]["reason"] = jr
            pp["b"]["attributes"]["reason"] = br
            if ctx == "conversation": pp["b"]["attributes"]["reason"] = br  # b is the decider here: judge = b (party)
            kw = {} if D is None else dict(D=D)
            v[jr] = rate(pp, ctx, m, ("a1", ctx, lbl), **kw)
        line(f"{ctx}: {lbl}", v)
print("A2 ADJ FOCUS: judge Focus sweep")
for lbl, setup, kw in (
        ("off-point: a Focus1 vs b Focus7, famine", lambda pp: (pp["a"]["attributes"].update(focus=1), pp["b"]["attributes"].update(focus=7)), dict(strife="famine")),
        ("off-point mirrored: a Focus7 vs b Focus1, famine", lambda pp: (pp["a"]["attributes"].update(focus=7), pp["b"]["attributes"].update(focus=1)), dict(strife="famine")),
        ("theatre: b presses every turn, a argues (peace)", lambda pp: None, dict(deciders={"b": forced("press"), "a": forced("argue")})),
        ("theatre: a presses every turn, b argues (peace)", lambda pp: None, dict(deciders={"a": forced("press"), "b": forced("argue")})),
        ("theatre a presses, CONTROL rattle_gain=0 rebound=0", lambda pp: None, dict(deciders={"a": forced("press"), "b": forced("argue")}, D=CTL(rattle_gain=0.0, rebound=0.0))),
        ("both argue only (null)", lambda pp: None, dict(deciders={"a": forced("argue"), "b": forced("argue")}))):
    v = {}
    for jf in LV:
        pp = blank(); setup(pp)
        pp["j1"]["attributes"]["focus"] = jf
        v[jf] = rate(pp, "trial", m, ("a2", lbl), **kw)
    line(lbl, v)
print("A3 ADJ ATTUNEMENT: judge Attunement sweep; a's insincerity via believes; strain via rattled_ago")
for lbl, bel, rag, D in (("a strained liar (believes -1, rattled_ago 0,0)", -1.0, (0, 0), None),
                         ("a comfortable honest (believes +1)", 1.0, (), None),
                         ("a honest but strained (believes +1, rattled_ago 0,0)", 1.0, (0, 0), None),
                         ("a strained liar, CONTROL ploy_step=0", -1.0, (0, 0), CTL(ploy_step=0.0))):
    v = {}
    for ja in LV:
        pp = blank(); pp["a"]["believes"] = {"m": bel}; pp["a"]["rattled_ago"] = rag
        pp["j1"]["attributes"]["attunement"] = ja
        kw = {} if D is None else dict(D=D)
        v[ja] = rate(pp, "trial", m, ("a3", lbl), **kw)
    line(lbl, v)
print("A4 ADJ PRESENCE+OFFICE: awe on a; a's rattles/sitting; P(for carried). b mid.")
def awe_stats(pp, ctx, key, **kw):
    aw = rt = car = 0.0
    for i in range(n):
        inp, card, out, b = sit(pp, ctx, m, (key, i), **kw)
        a = next(p for p in inp.room if p.id == "a"); bb = next(p for p in inp.room if p.id == "b")
        aw += E.awe(inp, a); rt += sum(1 for bt in out.beats if bt.rattled == "a"); car += b[0] in CARRIED
    return aw / n, rt / n, car / n
for jp, rung, mod in ((7, 5, "moderate"), (4, 3, None), (1, 0, None)):
    for aw_ in (1, 2, 4, 7):
        pp = blank(); pp["a"]["attributes"]["will"] = aw_
        pp["j1"]["attributes"]["presence"] = jp; pp["j1"]["office"] = F.seat(rung, "Crown", mod)
        a_, r_, c_ = awe_stats(pp, "trial", ("a4", jp, rung, aw_))
        print(f"  judge Presence {jp} rung {rung} {mod or '':8}  a Will {aw_}: awe {a_:.2f}  a rattled {r_:.2f}/sitting  P(a carried) {c_:.3f}")
pp = blank(); pp["a"]["attributes"]["will"] = 2; pp["j1"]["attributes"]["presence"] = 7; pp["j1"]["office"] = F.seat(5, "Crown", "moderate")
a_, r_, c_ = awe_stats(pp, "trial", ("a4c",), D=CTL(awe_step=0.0))
print(f"  CONTROL awe_step=0, judge P7 rung5, a Will 2: awe {a_:.2f} rattled {r_:.2f} P {c_:.3f}")
print("  commoner deciders (conversation, b decides): b Presence sweep, a Will 2")
for bp in (1, 4, 7):
    pp = blank(); pp["a"]["attributes"]["will"] = 2; pp["b"]["attributes"]["presence"] = bp
    a_, r_, c_ = awe_stats(pp, "conversation", ("a4b", bp))
    print(f"    b(decider) Presence {bp}: awe on a {a_:.2f}  rattled {r_:.2f}  P(a carried) {c_:.3f}")
