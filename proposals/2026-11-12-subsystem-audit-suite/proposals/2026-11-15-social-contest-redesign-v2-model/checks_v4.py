"""After Jordan's correction of A-139: only a one-character sitting is refused; a person may be a side AND decide.
PYTHONHASHSEED=0 python checks_v4.py [n]"""
import sys, copy
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, Choice
from scmodel.rng import draw
from checks_v3_helpers import force, only
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
mp, M = F.mid_people(), F.matter(); cast, T = F.cast(), F.TOLLS
def H(t): print("\n== " + t)
H("A-139 the invariant")
try: E.Input(host.build(mp, "trial", M, bench=BENCH)[0].rite, "m", (host.build(mp, "trial", M, bench=BENCH)[0].room[0],), host.build(mp, "trial", M, bench=BENCH)[0].grounds, host.dials()); print("  NOT REFUSED")
except ValueError as e: print(f"  refused: {e}")
for lab, rite, m, kw in (("an audience with a noble who speaks and then decides", "audience", dict(M, parties={"for": "a", "against": "j1"}), dict(bench=("j1",))),
                         ("an inquisitor who questions and judges", "inquisition", dict(M, parties={"for": "c1", "against": "b"}), dict(bench=("c1", "c2"))),
                         ("a questioned man who decides whether to give way", "questioning", M, {}),
                         ("a seat who speaks in debate and votes", "debate", dict(M, parties={"for": "j1", "against": "b"}), dict(bench=BENCH))):
    inp, card, out, b = sit(mp, rite, m, ("v4", 1), effort=3, **kw)
    both = [p.id for p in inp.room if p.side and p.decides]
    print(f"  {lab:52} both cells: {both}; adjudicators {card.decided_by}; verdicts {[i for i, _ in out.verdicts]}; band {b[0]}")
H("the three types re-decided on the merits (before = the consent version of the last pass)")
c = Counter(sit(mp, "conversation", M, ("cv", i), effort=3)[3][0] for i in range(N)); print(f"  conversation (close: the man addressed, a draw on him): bands {dict(c)}; carried {(c['success']+c['overwhelming'])/N:.3f}   [before: accepted or impasse, no band in 63%]")
for lab, dec in (("concedes at once", only("concede")), ("automatic", None), ("never concedes", force(lambda o: o.move != "concede"))):
    c = Counter(); ev = 0; nb = 0
    for i in range(N):
        inp, card, out, b = sit(mp, "questioning", M, ("q", i), effort=3, deciders=({"b": dec} if dec else None)); c[b[0] in CARRIED] += 1
        for x in out.beats:
            if x.mover == "b": nb += 1; ev += x.evaded
    print(f"  questioning, the questioned {lab:18} the questioner gets it {c[True]/N:.3f}; the questioned man's beats charged as evasion {ev}/{nb}   [before: 1.000 / 0.255 / 0.000; evasion could not fire]")
c = Counter(sit(mp, "negotiation", M, ("ng", i), effort=3)[3][0] for i in range(N)); print(f"  negotiation (consent, kept on the merits): {dict(c)}")
H("a party who decides is steered by his own stake, and the room reads it")
pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(pursuits={"tolls": 0.9}); m = dict(id="m", parties={"for": "a", "against": "j1"}, bears={"tolls": -1.0})
for lab, fl in (("shipped", ()), ("bearing flattened", ("bearing",))):
    r = rate(pp, "audience", m, N, "nb", bench=("j1",), floor=("j2",), effort=2, flat=fl)
    inp, card, out, b = sit(pp, "audience", m, ("nb", 0), bench=("j1",), floor=("j2",), effort=2, flat=fl); w = host.new_world(); host.fold(w, pp, inp, card, out, m)
    j = [p for p in inp.room if p.id == "j1"][0]
    print(f"  the noble (speaks against, decides; the plea would cost him his tolls) [{lab}]: start {j.start:+.2f}; petitioner carried {r:.3f}; `partial` claims an onlooker (j2) holds: {[c for c in w['ledgers'].get('j2', []) if c[0] == 'partial'][:1]}")
o = proceed(host.build(pp, "audience", m, bench=("j1",), floor=("j2",), effort=2)[0], draw(7, "a", "j"), rulings={"j1": lambda jv: "for" if jv.track < 0 else "against"})
print(f"  a played noble (a side AND the adjudicator) rules against his own mind: band {host.act_band(host.build(pp, 'audience', m, bench=('j1',), floor=('j2',), effort=2)[0], o)[0]}; departure from his own track returned {o.ruled or '(none: he ruled with his own mind)'}")
H("invariants over the eight rites (cast, effort 3; automatic and random choosers)")
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))), ("trial", dict(bench=CB, floor=("guildsmen", "toll_men", "clerk"))), ("debate", dict(bench=CB, floor=("guildsmen",))), ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
viol = Counter(); nb = 0; both = 0
for rite, kw in ROWS:
    m = dict(T) if rite != "rally" else dict(T, parties={"for": "orator"})
    if rite == "audience": m = dict(T, parties={"for": "scholar", "against": "judge"})
    if rite == "inquisition": m = dict(T, parties={"for": "bishop", "against": "orator"})
    bd = Counter(); en = Counter()
    for i in range(200):
        dec = {} if i % 2 == 0 else {p: chooser("random", i) for p in cast}
        inp, card, out, b = sit(cast, rite, m, ("inv", i), effort=3, deciders=dec, **kw)
        both += any(p.side and p.decides for p in inp.room)
        if i % 2 == 0: bd[b[0]] += 1; en[out.ended] += 1
        closed = set()
        for k, x in enumerate(out.beats):
            nb += 1
            viol["chain"] += x.n != k + 1; viol["no point"] += x.move == "argue" and x.point is None
            viol["closed issue re-argued"] += x.issue in closed; viol["move not on the card"] += x.move not in dict(card.moves)[x.side]
            viol["evasion unpriced"] += x.evaded and not x.rattled and not any(d != 0 for _, d in x.moved) and any(p.focus > 1 for p in inp.room if p.side != x.side); viol["a non-deciding speaker moved his own track"] += any(q == x.voice and not next(p for p in inp.room if p.id == q).decides for q, _ in x.moved)
            if x.closed and not (out.ended == "yielded" and k == len(out.beats) - 1): closed.add(x.closed)
        viol["one character"] += len({p.id for p in inp.room}) < 2
        viol["verdicts != the card's adjudicators"] += set(i_ for i_, _ in out.verdicts) != set(card.decided_by)
        viol["track != start + beats"] += any(abs(dict(out.state.tracks)[p.id] - p.start - sum(d for x in out.beats for q, d in x.moved if q == p.id)) > 1e-6 for p in inp.room)
    print(f"  {rite:12} bands {dict(bd)} ends {dict(en)}")
print(f"  beats {nb}; sittings in which someone held both cells {both}/1600; violations {dict(viol)}")
