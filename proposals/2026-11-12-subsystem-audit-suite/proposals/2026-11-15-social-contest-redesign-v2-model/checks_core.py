"""v2 verification, part 1: D1..D8, the roles, the invariants, the transcripts.  PYTHONHASHSEED=0 python checks_core.py [n]"""
import sys, copy, math, hashlib
from collections import Counter
from sc2 import host, fixtures as F
from sc2.lab import *
from sc2.engine import proceed, closing_odds, MOVES, Choice
from scmodel.rng import draw
from scmodel import dice
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
mp, M = F.mid_people(), F.matter()
D, C = host.dials(), host.controls()
def H(t): print("\n== " + t)

H("D1 a bench verdict reads the sitting (trial, all-mid, effort 3; control arm: track_step 0)")
for lab, DD in (("shipped", D), ("control track_step=0", host.dials(track_step=0.0))):
    bins = {"<=-3": [0, 0], "(-3,0)": [0, 0], "[0,3)": [0, 0], ">=3": [0, 0]}
    tot = 0
    for i in range(N):
        inp, card, out, b = sit(mp, "trial", M, ("d1", i), bench=BENCH, effort=3, D=DD)
        t = dict(out.state.tracks)["j1"]
        k = "<=-3" if t <= -3 else "(-3,0)" if t < 0 else "[0,3)" if t < 3 else ">=3"
        bins[k][0] += 1; bins[k][1] += b[0] in CARRIED; tot += b[0] in CARRIED
    print(f"  {lab:22} carried {tot/N:.3f} | by the presiding seat's track: " + "  ".join(f"{k} n={v[0]} {v[1]/max(1,v[0]):.3f}" for k, v in bins.items()))
ex = rate(mp, "excommunication_deliberation", M, N, "d1x", bench=("c1", "c2", "c3"), effort=2)
print(f"  excommunication (declared, quorum 2, three church seats): carried {ex:.3f}  [before: 0/2000]")
r, s, z = sweep(mp, "trial", M, "a", "reason", n=N, bench=BENCH, effort=3)
print(f"  R11 trial arm: speaker Reason 1/4/7 -> carried {r}  slope {s:+.4f} z {z:+.1f}")

H("D2 the centre (abridged conversation = tell; equals, rank 1, routine)")
for lab, DD, diff in (("shipped", D, "routine"), ("controls", C, "routine"), ("shipped, routine set to 0.8", D, None)):
    cnt = Counter()
    for i in range(N * 2):
        if diff is None:
            saved = host.DIFFICULTY["routine"]; host.DIFFICULTY["routine"] = 0.8
        inp, card, out, b = sit(mp, "conversation", M, ("d2", i), form="abridged", D=DD)
        if diff is None: host.DIFFICULTY["routine"] = saved
        cnt[b[0]] += 1
    n2 = N * 2
    print(f"  {lab:28} fail {cnt['failure']/n2:.3f} partial {cnt['partial']/n2:.3f} carried {(cnt['success']+cnt['overwhelming'])/n2:.3f}   [A-79: .59/.16/.25; before: carried .53-.70]")
for rite, kw in (("conversation", {}), ("trial", dict(bench=BENCH)), ("rally", dict(floor=("crowd",)))):
    m = M if rite != "rally" else F.matter(ag=None)
    if rite == "rally": m = dict(id="m", parties={"for": "a"}, bears={})
    print(f"  full {rite:13} equals: carried {rate(mp, rite, m, N, 'd2f', effort=2, **kw):.3f}")
# control equality: the abridged margin IS the plain roll
ok = 0
for i in range(200):
    inp, card = host.build(mp, "conversation", M, form="abridged", D=C)
    out = proceed(inp, draw(("eq", i), "act", "conversation"))
    rng = draw(("eq", i), "act", "conversation")
    for _ in range(2 * 4 + 4): rng.normal()
    x = dice.SocialContestInput(pool=11.0, opposition=5.0, leverage=0.0, difficulty=0.5, obstacle_operands=(("manner", 0.0, 1.0),),
                                pool_default=2, pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
    m = dice.roll(x, rng)
    v = out.verdicts[0][1]
    ok += abs((v.net - v.ob) - (m.net - m.ob)) < 1e-9
print(f"  control equality: abridged margin == the one roll (dice.roll) on the same key: {ok}/200")

H("D3 the rattle economy")
def rattle_split(DD, lab):
    a = [0, 0]; b = [0, 0]
    for i in range(N):
        inp, card, out, bd = sit(mp, "trial", M, ("d3", i), bench=BENCH, effort=3, D=DD)
        rb = dict(out.state.cond)["b"].rattles; ra = dict(out.state.cond)["a"].rattles
        if rb > ra: a[0] += 1; a[1] += bd[0] in CARRIED
        elif ra > rb: b[0] += 1; b[1] += bd[0] in CARRIED
    print(f"  {lab:34} `for` carried when the respondent was rattled more: {a[1]/max(1,a[0]):.3f} (n={a[0]}); when `for` was: {b[1]/max(1,b[0]):.3f} (n={b[0]})")
rattle_split(D, "shipped")
OFF = host.dials(rattle_gain=0.0, show=0.0, rattle_pull=0.0, press_pull=0.0, wear=0.0)
wk = copy.deepcopy(mp); wk["b"]["attributes"].update(will=2, grace=2)
for lab, dec in (("opens with one press, then argues", "p1"), ("argues only", "argue"), ("presses only", "press")):
    def p1(view, me, _k=dec):
        return chooser("press" if (_k == "press" or (_k == "p1" and view.own.spoken == 0)) else "argue")(view, me)
    x1 = rate(wk, "trial", M, N, "d3c", bench=BENCH, effort=3, deciders={"a": p1, "b": chooser("argue")})
    x0 = rate(wk, "trial", M, N, "d3c", bench=BENCH, effort=3, deciders={"a": p1, "b": chooser("argue")}, D=OFF)
    print(f"  trial vs a Will-2 Grace-2 respondent, `for` {lab:36} carried {x1:.3f}; control (a rattle does nothing) {x0:.3f}")
for rite, lab in (("questioning", "questioned rite (only the questioner presses)"), ("conversation", "contest rite (both may press)")):
    print(f"  questioner carried, {lab}: {rate(mp, rite, M, N, 'd3q', effort=3):.3f}   [before: .26 questioned vs .34 contest: the script helped the accused]")
weak = copy.deepcopy(mp); weak["b"]["attributes"].update(will=2, grace=2)
cnt = Counter()
for i in range(N):
    inp, card, out, bd = sit(weak, "questioning", M, ("d3b", i), effort=3)
    cnt[(out.ended, dict(out.state.cond)["b"].rattles > 0)] += 1
print(f"  questioning a Will-2 Grace-2 man: ends {dict(cnt)}  (yielded while rattled = 'broken'; before: unreachable)")
print("  dominance: P(`for` carried), rows = `for` chooser, cols = `against` chooser (view-only choosers)")
kinds = ("auto", "smart", "argue", "press", "rest", "random"); BR = {}
for people, lab, rite, kw in ((mp, "all-mid", "conversation", {}), (weak, "vs Will-2 Grace-2", "conversation", {}), (mp, "all-mid", "debate", dict(bench=BENCH)), (mp, "all-mid", "trial", dict(bench=BENCH))):
    print(f"   {rite} {lab}:        " + " ".join(f"{k:>6}" for k in kinds))
    n3 = max(300, N // 4)
    for kf in kinds:
        row = []
        for ka in kinds:
            dec = {}
            if kf != "auto": dec["a"] = smart if kf == "smart" else chooser(kf)
            if ka != "auto": dec["b"] = smart if ka == "smart" else chooser(ka)
            row.append(rate(people, rite, M, n3, "dom", deciders=dec, effort=3, **kw)); BR[(kf, ka)] = row[-1]
        print(f"     for={kf:6} " + " ".join(f"{x:6.3f}" for x in row))

    print("       best reply to each column: " + ", ".join(f"{ka}<-{max(kinds, key=lambda kf: BR[(kf, ka)])}" for ka in kinds))
H("D4 strain carried does not ratchet (11 sittings, one rest between; the same pair)")
pp = copy.deepcopy(mp); hist = []
for k in range(11):
    pp["b"]["rattled_ago"] = tuple(s + 1 for s in pp["b"].get("rattled_ago", ()))        # one scene of rest
    inp, card = host.build(pp, "questioning", M, effort=3, deciders_none=None) if False else host.build(pp, "questioning", M, effort=3)
    hist.append(round(dict((p.id, p.strain) for p in inp.room)["b"], 2))
    out = proceed(inp, draw(("d4", k), "act", "q"), None, {"a": chooser("press")})
    pp["b"]["rattled_ago"] = pp["b"].get("rattled_ago", ()) + (0,) * dict(out.state.cond)["b"].rattles
print(f"  strain carried in at each sitting (pressed every exchange): {hist}   [before: 0 -> 5.8-9]")

H("D5 who opens (conversation, all-mid, effort 3)")
p1 = rate(mp, "conversation", M, N * 2, "d5", effort=3)
sw = copy.deepcopy(mp); 
r0 = host.RITES["conversation"]["bears"]; host.RITES["conversation"]["bears"] = "against"
p2 = rate(mp, "conversation", M, N * 2, "d5", effort=3); host.RITES["conversation"]["bears"] = r0
inp, card, out, b = sit(mp, "conversation", M, ("d5", 0), effort=3)
sp = Counter()
for i in range(300): sp.update(x.mover for x in sit(mp, "trial", M, ("d5", i), bench=BENCH, effort=3)[2].beats)
print(f"  speeches over 300 trials: {dict(sp)}; `for` opens: carried {p1:.3f}; `against` opens: {p2:.3f}; diff {p1-p2:+.3f} +- {2*se(p1, N*2):.3f}   [before: .433 vs .257]")

def ro(v, me):
    o = max(([o for o in v.options if o.relation == "raises"] or list(v.options)), key=lambda o: o.ev)
    return Choice(o.move, o.ground, o.item, o.relation)
q1 = rate(mp, "conversation", M, N * 2, "d5", effort=3, decide=ro)
host.RITES["conversation"]["bears"] = "against"; q2 = rate(mp, "conversation", M, N * 2, "d5", effort=3, decide=ro); host.RITES["conversation"]["bears"] = r0
print(f"  control (nobody may answer, both only raise): `for` opens {q1:.3f}; `against` opens {q2:.3f}; diff {q1-q2:+.3f}: what remains above is the initiative of raising against answering")

H("D6 the act's margin under consent (negotiation)")
bad = tot = 0
for i in range(N):
    inp, card, out, b = sit(mp, "negotiation", M, ("d6", i), effort=3)
    t = dict(out.state.tracks)["b"]
    if b[0] in CARRIED:
        tot += 1; bad += (t < 0 and out.ended != "yielded")
print(f"  graded Success or better: {tot}/{N}; of those with the other party's track against the actor: {bad}   [before: 198/2000]")

H("D7 a type is not a name")
ch = Counter()
for rite in ("trial", "debate", "inquisition"):
    for i in range(300):
        b1 = sit(mp, rite, M, ("d7", i), bench=BENCH if rite != "inquisition" else ("c1", "c2"), effort=3)[3][0]
        b2 = sit(mp, rite, M, ("d7", i), bench=BENCH if rite != "inquisition" else ("c1", "c2"), floor=("crowd",), effort=3)[3][0]
        ch[rite] += b1 != b2
print(f"  bench rows: sittings whose band changes when a crowd is on the floor: {dict(ch)} of 300   [before: 0 of 200 on every bench row; inquisition's floor is closed]")
cast = F.cast()
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))),
        ("trial", dict(bench=CB, floor=("guildsmen", "toll_men", "clerk"))), ("debate", dict(bench=CB, floor=("guildsmen",))),
        ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
print("  per rite (cast, effort 3, automatic): moves, relations, ends, mean beats, carried")
allmoves, allends = Counter(), Counter()
for rite, kw in ROWS:
    mv, rel, en = Counter(), Counter(), Counter(); nb = car = 0
    m = dict(F.TOLLS) if rite not in ("rally", "audience") else dict(F.TOLLS, parties={"for": "orator" if rite == "rally" else "scholar"})
    for i in range(400):
        inp, card, out, b = sit(cast, rite, m, ("rows", i), effort=3, **kw)
        for x in out.beats: mv[x.move] += 1; rel[x.relation] += 1
        en[out.ended] += 1; nb += len(out.beats); car += b[0] in CARRIED
    allmoves.update(mv); allends.update(en)
    print(f"   {rite:13} {dict(mv)} {dict(rel)} {dict(en)} beats {nb/400:.1f} carried {car/400:.2f}")
print(f"  every move occurs: {dict(allmoves)}; every end occurs: {dict(allends)}")
# every setting moves something
cast2 = copy.deepcopy(cast); cast2["bully"]["rattled_ago"] = (0, 1); cast2["scholar"]["layers"]["pursuits"]["tolls"] = 0.9
battery = [(cast2, r, (dict(F.TOLLS) if r not in ("rally", "audience") else dict(F.TOLLS, parties={"for": "orator" if r == "rally" else "scholar"})), kw) for r, kw in ROWS]
def digest(DD):
    h = hashlib.sha256()
    for people, rite, m, kw in battery:
        for i in range(25):
            inp, card, out, b = sit(people, rite, m, ("abl", i), effort=3, D=DD, arranger="bully" if rite == "trial" else None, rig=0.5 if rite == "trial" else 0.0, **kw)
            h.update(repr((b[0], round(b[1] or 0, 6), len(out.beats), out.ended)).encode())
    return h.hexdigest()
base = digest(D); dead = []
for k, v in host.SHIPPED.items():
    if k in ("pool_add", "pool_floor", "pool_default", "opposition_rate", "mid", "floor"): continue
    alt = None if isinstance(v, str) else (v * 2 if v else 1.0)
    if digest(host.dials(**{k: alt})) == base: dead.append(k)
print(f"  settings: {len(host.SHIPPED) - 6} of the proceeding's own; inert under perturbation over the battery: {dead or 'none'}   [before: 9 of 53]")

H("D8 the decider's three, each on one operand; lean; saturation")
ral = dict(id="m", parties={"for": "a"}, bears={})
force_auth = lambda v, me: Choice(*[(o.move, o.ground, o.item, o.relation) for o in v.options if o.ground == "authority"][0])
for attr, off in (("reason", dict(sense_step=0.0, involve=0.0, crowd_lean=0.0)), ("focus", dict(off_step=0.0)), ("attunement", dict(ploy_step=0.0))):
    pp = copy.deepcopy(mp)
    pp["a"]["attributes"].update(reason=6, presence=2, focus=1 if attr == "focus" else 4)   # a reasoned speaker (who wanders, for the Focus arm)
    mm = dict(ral)
    kw = dict(floor=("crowd",), effort=3, strife="famine" if attr == "focus" else "peace")
    if attr == "attunement":                                                  # ...arguing against his own conviction (a ploy)
        pp["a"]["layers"] = dict(convictions={"x": 5}); mm = dict(ral, bears={"x": -1.0}); kw["deciders"] = {"a": force_auth}
    r1, s1, z1 = sweep(pp, "rally", mm, "crowd", attr, n=N, **kw)
    r0, s0, z0 = sweep(pp, "rally", mm, "crowd", attr, n=N, D=host.dials(**off), **kw)
    print(f"  decider {attr:10} 1/4/7 -> carried { {k: round(v, 3) for k, v in r1.items()} } slope {s1:+.4f} z {z1:+.1f} | its own setting off: slope {s0:+.4f} (dead operand reads {'0: the gate cannot pass' if abs(s0) < 1e-12 else 'NON-ZERO'})")
from sc2.engine import Item
pp = copy.deepcopy(mp); pp["a"]["attributes"].update(reason=6, presence=2); pp["a"]["items"] = (Item("deed_of_gift", "record", 0.6),)
ev_only = lambda v, me: Choice(*[(o.move, o.ground, o.item, o.relation) for o in v.options if o.ground == "evidence"][0])
r3, s3, z3 = sweep(pp, "audience", dict(id="m", parties={"for": "a"}, bears={}), "j1", "reason", n=N, bench=("j1",), effort=2, deciders={"a": ev_only})
print(f"  Reason steers both ways: a petitioner arguing on the proof before one seat: the seat's Reason 1/4/7 -> { {k: round(v, 3) for k, v in r3.items()} } slope {s3:+.4f} z {z3:+.1f}")
pp = copy.deepcopy(mp); pp["a"]["attributes"].update(reason=2, presence=6)
r2, s2, z2 = sweep(pp, "rally", ral, "crowd", "reason", n=N, floor=("crowd",), effort=3)
print(f"  Reason steers both ways: a mannered speaker before the same decider: slope {s2:+.4f} z {z2:+.1f}")
for st in (-1.0, 0.0, 1.0):
    pp = copy.deepcopy(mp); pp["b"]["layers"] = dict(relationships={"a": st})
    tot = car = 0
    for i in range(N * 2):
        inp, card, out, b = sit(pp, "conversation", M, ("lean", i), effort=3)
        if 3.0 <= dict(out.state.tracks)["b"] < 5.0 and out.ended == "budget":
            tot += 1; car += b[0] in CARRIED
    print(f"  hearer's regard {st:+.0f}: sittings ending with his track in [3,5): {tot}; carried {car/max(1,tot):.3f}+-{se(car/max(1,tot), max(1,tot)):.3f}   [before: .27 hostile vs .80 friendly at the same track]")
inc = []
for t in (0, 3, 6, 9, 12):
    x = __import__("sc2.engine", fromlist=["x"]).close_input(host.build(mp, "trial", M, bench=BENCH)[0], t)
    mu, sd = __import__("sc2.engine", fromlist=["x"])._mean_margin(x)
    inc.append((t, round(1 - 0.5 * (1 + math.erf(((1.0 - mu) / sd) / math.sqrt(2))), 3)))
print(f"  no clamp: P(carried) by the decider's track {inc}   [before: one speech filled the track in 45-52% of openings]")
y = [0, 0, 0, 0]
for i in range(N):
    inp, card, out, b = sit(mp, "trial", M, ("yl", i), bench=BENCH, effort=3, deciders={"a": chooser("concede")})
    y[0] += b[0] in CARRIED
    inp, card, out, b = sit(mp, "trial", M, ("yl", i), bench=BENCH, effort=3)
    y[1] += b[0] in CARRIED
print(f"  sign of a concession: `for` conceding at every chance carries {y[0]/N:.3f} vs {y[1]/N:.3f} when he does not")

H("ROLES the speaker's six (slope of carried per point; z) at the abridged conversation and in full sittings")
rp = copy.deepcopy(mp)
for q, cr in (("b", dict(pursuits={"p": 0.9}, convictions={"c": 1})), ("j1", dict(pursuits={"p": 0.2}, convictions={"c": 5})), ("crowd", dict(pursuits={"p": 0.9}, convictions={"c": 1}))):
    rp[q]["layers"] = cr
mp_roles = rp
for scen, rite, kw, m in (("tell (abridged)", "conversation", dict(form="abridged"), M), ("conversation", "conversation", dict(effort=3), M),
                          ("trial", "trial", dict(bench=BENCH, effort=3, floor=("crowd",)), M), ("rally", "rally", dict(floor=("crowd",), effort=3), ral)):
    row = []
    for attr in host.ATTRS:
        r, s, z = sweep(mp_roles, rite, m, "a", attr, n=N, **kw)
        row.append(f"{attr[:4]} {s:+.3f}({z:+.0f})")
    print(f"  {scen:16} " + "  ".join(row))
r, s, z = sweep(mp, "conversation", M, "b", "will", n=N, form="abridged")
print(f"  the hearer's Will at the tell: slope {s:+.4f} z {z:+.1f}")

r, s, z = sweep(mp, "conversation", M, "a", "focus", n=N, form="abridged", strife="famine")
print(f"  the tell in a famine (unrest pulls): the speaker's Focus slope {s:+.4f} z {z:+.1f} (in a quiet room nothing pulls: 0 by construction)")
press_c = lambda v, me: Choice(*[(o.move, o.ground, o.item, o.relation) for o in v.options if o.move == "press" and o.ground == "consequence"][0])
rw = {}
for wl in (1, 4, 7):
    pp = copy.deepcopy(mp); pp["b"]["attributes"]["will"] = wl
    rw[wl] = rate(pp, "conversation", M, N, "wl", effort=1, deciders={"a": press_c, "b": chooser("rest")}, pred=lambda inp, card, out, b: out.beats[0].rattled is not None)
print(f"  Will: a pressed man is rattled at Will 1/4/7: {rw}")
rg = {}
for gl in (1, 4, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["grace"] = gl; pp["a"]["rattled_ago"] = ()
    tot = n_ = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "trial", M, ("gr", i), bench=BENCH, effort=3, deciders={"a": chooser("argue"), "b": chooser("press")})
        seen = False
        for x in out.beats:
            if x.rattled == "a": seen = True
            elif x.mover == "a" and seen: tot += x.margin; n_ += 1
    rg[gl] = round(tot / max(1, n_), 2)
print(f"  Grace: the mean margin of a man's speeches AFTER he has been rattled, at Grace 1/4/7 (formal venue): {rg}")

H("DETERMINISM, DRAW COUNTS, MIRROR")
a = [sit(cast, "trial", F.TOLLS, ("det", i), bench=CB, effort=3)[2] for i in range(50)]
b = [sit(cast, "trial", F.TOLLS, ("det", i), bench=CB, effort=3)[2] for i in range(50)]
print(f"  same key, same outcome: {sum(x == y for x, y in zip(a, b))}/50; draw counts asserted in proceed/_close on every run above")
tr = [dict(sit(mp, "conversation", M, ("mir", i), effort=3)[2].state.tracks)["b"] for i in range(N)]
print(f"  mirror: equals, mean track {sum(tr)/N:+.3f} +- {2*math.sqrt(sum(t*t for t in tr)/N/N):.3f} (0 = neither side favoured)")

H("R13 CONTINUITY and CARD invariants (every rite, cast, 300 sittings each, automatic and random choosers)")
viol = Counter(); nb = 0
for rite, kw in ROWS:
    m = dict(F.TOLLS) if rite not in ("rally", "audience") else dict(F.TOLLS, parties={"for": "orator" if rite == "rally" else "scholar"})
    for i in range(300):
        dec = {} if i % 2 else {p: chooser("random", i) for p in cast}
        inp, card, out, b = sit(cast, rite, m, ("inv", i), effort=3, deciders=dec, **kw)
        held = {p.id: {it.id for it in p.items} for p in inp.room}
        kinds = {it.id: it.kind for p in inp.room for it in p.items}
        closed, spoke = set(), Counter()
        for k, x in enumerate(out.beats):
            nb += 1
            viol["chain"] += x.n != k + 1
            viol["no point"] += x.move == "argue" and x.point is None
            viol["answers nothing"] += x.relation == "answers" and not any(p.id == x.point and p.side != x.side for p in out.state.points)
            viol["item not held"] += bool(x.item) and x.item not in held[x.mover]
            viol["item not admitted"] += bool(x.item) and kinds[x.item] not in card.admits
            viol["closed issue re-argued"] += x.issue in closed
            viol["move not on the card"] += x.move not in dict(card.moves)[x.side]
            viol["evasion unpriced"] += x.evaded and x.move == "argue" and not any(d != 0 for _, d in x.moved)
            if x.closed and not (out.ended == "yielded" and k == len(out.beats) - 1): closed.add(x.closed)
            spoke[x.mover] += 1
        viol["over the card's turns"] += any(v > card.turns for v in spoke.values())
        viol["deciders != card"] += tuple(i_ for i_, _ in out.verdicts) != tuple(sorted(card.decided_by, key=lambda q: [-p.precedence for p in inp.room if p.id == q] + [q]))
        viol["track != lean + beats"] += any(abs(dict(out.state.tracks)[p.id] - p.lean - sum(d for x in out.beats for q, d in x.moved if q == p.id)) > 1e-6 for p in inp.room if p.id in dict(out.state.tracks))
print(f"  beats checked {nb}; violations: {dict(viol)}")
