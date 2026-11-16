"""R2 role isolation: same seed, one fixed script for both sides (argue consequence/raises where on the menu, else
first argue, else first option), `a` differs in ONE attribute (lo vs hi). Count, over a's beats and b's beats, the
fraction where each operand field differs. Fields: drift(Focus) relevance(Reason) frame(Attunement) heard(Presence)
esteem(Grace) broke(temper) margin rattled evaded."""
import sys, copy
from common import *
FIELDS = ("drift", "relevance", "frame", "heard", "esteem", "broke", "margin", "rattled", "evaded")

def script(view, me):
    os_ = view.options
    pick = [o for o in os_ if o.move == "argue" and o.ground == "consequence" and o.relation == "raises"] \
        or [o for o in os_ if o.move == "argue"] or list(os_)
    o = pick[0]
    return Choice(o.move, o.ground, o.item, o.relation)

def presser(view, me):
    os_ = view.options
    pick = [o for o in os_ if o.move == "press" and o.ground == "consequence"] or [o for o in os_ if o.move == "argue" and o.ground == "consequence"] or list(os_)
    o = pick[0]
    return Choice(o.move, o.ground, o.item, o.relation)

n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
for fx in ("rich",):
    for ctx in CTX:
        for attr in ATTRS:
            for lo, hi in ((1, 7),):
                cnt = {("a", f): 0 for f in FIELDS}; cnt.update({("b", f): 0 for f in FIELDS}); na = nb = 0; desync = 0
                for i in range(n):
                    outs = []
                    for x in (lo, hi):
                        pp = rich() if fx == "rich" else blank(); pp["a"]["attributes"][attr] = x
                        dec = {"a": script, "b": presser}
                        inp, card, out, b = sit(pp, ctx, mat(fx), ("iso", i), deciders=dec)
                        outs.append(out)
                    A, B = outs
                    if len(A.beats) != len(B.beats) or any((p.mover, p.move) != (q.mover, q.move) for p, q in zip(A.beats, B.beats)):
                        desync += 1
                    for p, q in zip(A.beats, B.beats):
                        if (p.mover, p.move) != (q.mover, q.move):
                            break
                        who = "a" if p.mover == "a" else "b"
                        if who == "a": na += 1
                        else: nb += 1
                        for f in FIELDS:
                            u, v = getattr(p, f), getattr(q, f)
                            if (abs(u - v) > 1e-9) if isinstance(u, float) else (u != v):
                                cnt[(who, f)] += 1
                fa = " ".join(f"{f}:{cnt[('a', f)]/max(1,na):.2f}" for f in FIELDS if cnt[('a', f)])
                fb = " ".join(f"{f}:{cnt[('b', f)]/max(1,nb):.2f}" for f in FIELDS if cnt[('b', f)])
                print(f"{fx} {ctx:12} {attr:10} {lo}v{hi} a-beats {na:4} [{fa}] | b-beats {nb:4} [{fb}] desync {desync}/{n}")
