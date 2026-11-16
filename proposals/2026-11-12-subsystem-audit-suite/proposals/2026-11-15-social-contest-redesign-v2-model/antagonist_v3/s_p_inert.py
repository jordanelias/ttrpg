"""Is a party-and-decider's OWN speech (and the evasion charged on him) inert to the outcome? Same keys, fixed draw counts."""
import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/snap")
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import sit, CARRIED, se, BENCH
from checks_v3_helpers import force, only
N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
mp, M = F.mid_people(), F.matter()
def row(lab, rite, m, who, kw):
    res = {}
    same = 0
    outs = {}
    for pol, dec in (("auto", None), ("argue", only("argue")), ("rest", only("rest"))):
        car = 0; o = []
        for i in range(N):
            inp, card, out, b = sit(mp, rite, m, ("inert", i), effort=3, deciders=({who: dec} if dec else None), **kw)
            car += b[0] in CARRIED; o.append((b[0], round(b[1] or 0, 9)))
        res[pol] = car / N; outs[pol] = o
    # evs the view shows him for arguing (mean of best argue ev at turn 1)
    inp, card = host.build(mp, rite, m, effort=3, **kw)
    me = [p for p in inp.room if p.id == who][0]
    print(f"  {lab:46} carried auto {res['auto']:.3f} | {who} argues every turn {res['argue']:.3f} | {who} rests every turn {res['rest']:.3f}  (se {se(.35, N):.3f}); decides={me.decides} side={me.side}")
print("== a party who decides: does his own arguing change the verdict? (all-mid, effort 3)")
row("conversation: the man addressed (b)", "conversation", M, "b", {})
row("questioning: the questioned man (b)", "questioning", M, "b", {})
row("audience: the noble who is the other party (j1)", "audience", dict(M, parties={"for": "a", "against": "j1"}), "j1", dict(bench=("j1",)))
row("inquisition: the inquisitor who judges (c1)", "inquisition", dict(M, parties={"for": "c1", "against": "b"}), "c1", dict(bench=("c1", "c2")))
row("control, trial: the accused (b), not a decider", "trial", M, "b", dict(bench=BENCH))
# the view's worth for his arguing, against the outcome
print("== what the view tells the party-decider his argument is worth (turn 1, perfect reader acc irrelevant: TRUE menu ev)")
for lab, rite, m, who, kw in (("questioning b", "questioning", M, "b", {}), ("conversation b", "conversation", M, "b", {}), ("inquisition c1", "inquisition", dict(M, parties={"for": "c1", "against": "b"}), "c1", dict(bench=("c1", "c2")))):
    inp, card = host.build(mp, rite, m, effort=3, **kw); st = E._start(inp); me = [p for p in inp.room if p.id == who][0]
    true, *_ = E.menu(inp, st, me, 3)
    print(f"  {lab:16} " + "; ".join(f"{mv}/{g}/{rel} ev {ev:+.2f}" for mv, g, it, rel, ev, p, fr in true if mv == 'argue')[:300])
# evasion charged on the questioned man: whose track moves?
print("== evasion charged on the questioned man: whose tracks move")
cnt = Counter()
for i in range(400):
    inp, card, out, b = sit(mp, "questioning", M, ("ev", i), effort=3, deciders={"b": force(lambda o: o.move != "concede")})
    dec = {p.id for p in inp.room if p.decides}
    for x in out.beats:
        if x.evaded and x.mover == "b":
            cnt["evasions"] += 1; cnt["moved a decider"] += any(q in dec and d != 0 for q, d in x.moved)
print(" ", dict(cnt))
