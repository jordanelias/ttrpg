"""A-143: content (Reason), framing (Attunement), delivery (Presence), conduct (Grace): four operands on one speech.
PYTHONHASHSEED=0 python checks_v6.py [n]"""
import sys, copy, math
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed
from scmodel.rng import draw
from checks_v3_helpers import force
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
ground = lambda g: force(lambda o: o.move == "argue" and o.ground == g)
mp = F.mid_people()
fp = copy.deepcopy(mp)
L = dict(pursuits={"grain": 0.9, "glory": 0.1, "coin": 0.3}, convictions={"faith": 5, "law": 1})
for q in ("b", "j1", "crowd"): fp[q]["layers"] = L
fm = dict(id="m", parties={"for": "a", "against": "b"}, bears={"grain": 1.0, "coin": 0.2, "glory": 0.2, "faith": 0.5, "law": 0.5})
VEN = (("a private exchange (the tell)", "conversation", dict(form="abridged"), fm), ("before a bench", "trial", dict(bench=("j1",), effort=2), fm), ("before a crowd", "rally", dict(floor=("crowd",), effort=2), dict(fm, parties={"for": "a"})))
OFF = {"reason": dict(relevance=0), "attunement": dict(read_blur=0.0), "presence": dict(heard_step=0.0), "grace": dict(esteem_step=0.0)}
print("== each attribute's own operand on the speech: carried at 1 -> 7, arguing consequence; and with its own operand off")
for attr in ("reason", "attunement", "presence", "grace"):
    row = []
    for lab, rite, kw, m in VEN:
        r = {}
        for arm, DD in (("on", host.dials(bias_step=0.0)), ("off", host.dials(bias_step=0.0, **OFF[attr]))):
            for x in (1, 7):
                pp = copy.deepcopy(fp); pp["a"]["attributes"][attr] = x
                r[(arm, x)] = rate(pp, rite, m, N, "v6", D=DD, deciders={"a": ground("consequence"), "b": chooser("rest")}, **kw)
        d1, d0 = r[("on", 7)] - r[("on", 1)], r[("off", 7)] - r[("off", 1)]
        row.append(f"{lab}: {r[('on',1)]:.3f}->{r[('on',7)]:.3f} ({d1:+.3f}); off {d0:+.3f}; the operand's own share {d1-d0:+.3f}")
    print(f"  {attr:10} " + " | ".join(row) + f"   (se of a difference {math.hypot(se(.35, N), se(.35, N)):.3f})")
print("== four strengths, the SAME argument (consequence) to the SAME listener (the hungry man), the same key: the beat record")
def first_frame(att, key):
    pp = copy.deepcopy(fp); pp["a"]["attributes"]["attunement"] = att
    inp, card = host.build(pp, "trial", fm, bench=("j1",), floor=("crowd",), effort=1, D=host.dials(bias_step=0.0))
    return proceed(inp, draw(("four", key), "act", "trial"), deciders={"a": ground("consequence"), "b": chooser("rest")}).beats[0].frame
KEY = next(k for k in range(50) if first_frame(1, k) != first_frame(7, k))
print(f"  (key {KEY}: the first of 0..49 on which a poor reader frames differently from a good one; he does so on {sum(first_frame(1, k) != first_frame(7, k) for k in range(50))} of 50)")
for lab, at in (("ordinary", {}), ("Reason 7", dict(reason=7)), ("Attunement 7", dict(attunement=7)), ("Attunement 1", dict(attunement=1)), ("Presence 7", dict(presence=7)), ("Grace 7", dict(grace=7))):
    pp = copy.deepcopy(fp); pp["a"]["attributes"].update(at); pp["b"]["attributes"]["grace"] = 5
    inp, card = host.build(pp, "trial", fm, bench=("j1",), floor=("crowd",), effort=1, D=host.dials(bias_step=0.0))
    out = proceed(inp, draw(("four", KEY), "act", "trial"), deciders={"a": ground("consequence"), "b": chooser("rest")})
    x = out.beats[0]
    print(f"  {lab:13} relevance {x.relevance:.2f} | framed on {x.frame:6} | heard {x.heard:.2f} | esteem {x.esteem:+.2f} | margin with the judge {x.margin:+.2f}")
