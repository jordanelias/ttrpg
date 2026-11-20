"""P2 symmetry / opener: identical people, auto both sides. Measure final-track mirror, who speaks how often, and the
opener effect by flipping who opens (order patched to `rank` with precedence: same cycle rule, opener swapped).
    PYTHONHASHSEED=0 python lane3/p2_symmetry.py [n]"""
import math
import sys
from collections import Counter
from dataclasses import replace

from harness import proceed2, person, bench_people, scene_kw, CARRIED, P, dialmod, build_input, draw, degree

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4000


def go(row, opener, D, effort=2, attrsA=None, attrsB=None, presumes=None):
    people = {"a": person("a", attrsA, pursuits={"x": 0.6}, convictions={"faith": 2}),
              "b": person("b", attrsB, pursuits={"x": 0.6}, convictions={"faith": 2})}
    people.update(bench_people())
    inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=effort, **scene_kw(row))
    sp = list(inp.speakers)
    if opener is not None:
        prec = {"for": 2, "against": 1} if opener == "for" else {"for": 1, "against": 2}
        sp = [replace(S, precedence=prec[S.side]) for S in sp]
        inp = replace(inp, speakers=tuple(sp), type=replace(inp.type, order="rank"))
    if presumes:
        inp = replace(inp, type=replace(inp.type, presumes=presumes))
    c = Counter()
    trk = []
    spk = Counter()
    for t in range(n):
        out, es = proceed2(inp, draw(("p2", row, t), "a", "r"), {})
        m, veto = P.act_margin(out, inp.type, inp)
        b = None if m is None else degree(m)
        c["carry"] += b in CARRIED
        c["fail"] += b == "failure"
        trk.append(out.state.track)
        for x in out.exchanges:
            spk[x.mover] += 1
        if es is not None:
            c[out.ended + ":" + inp.speakers[es].side] += 1
        c["end:" + out.ended] += 1
    mt = sum(trk) / n
    sd = math.sqrt(sum((x - mt) ** 2 for x in trk) / (n - 1))
    pos = sum(x > 0.5 for x in trk) / n
    neg = sum(x < -0.5 for x in trk) / n
    cr = c["carry"] / n
    return dict(carry=cr, se=math.sqrt(cr * (1 - cr) / n), mean_track=mt, se_track=sd / math.sqrt(n), pos=pos,
                neg=neg, spk={k: v / n for k, v in spk.items()}, c=c)


for Dn, D in (("shipped", dialmod.shipped()), ("controls", dialmod.controls()), ("rd_shipped", dialmod.rd_shipped())):
    for row in ("conversation", "legal_trial", "arbitration", "negotiation"):
        for op in (None, "for", "against"):
            if op is None and row in ("legal_trial",):
                pass
            r = go(row, op, D)
            print(f"{Dn:10} {row:13} opener={str(op):8} carry={r['carry']:.3f}±{r['se']:.3f} "
                  f"track={r['mean_track']:+.3f}±{r['se_track']:.3f} P(track>.5)={r['pos']:.3f} P(<-.5)={r['neg']:.3f} "
                  f"speeches={ {k: round(v, 2) for k, v in r['spk'].items()} } "
                  f"ends={ {k: v for k, v in r['c'].items() if ':' in k} }")
    print()
# presumption effect at rd_shipped (only dial where presumes matters) on interrogation-like flips
D = dialmod.rd_shipped()
for row in ("legal_trial", "conversation"):
    for pr in ("none", "for", "against"):
        r = go(row, None, D, presumes=pr)
        print(f"rd_shipped presumes={pr:8} {row:13} carry={r['carry']:.3f}±{r['se']:.3f}")
D = dialmod.shipped()
for row in ("legal_trial", "conversation"):
    for pr in ("none", "for", "against"):
        r = go(row, None, D, presumes=pr)
        print(f"shipped    presumes={pr:8} {row:13} carry={r['carry']:.3f}±{r['se']:.3f}")
