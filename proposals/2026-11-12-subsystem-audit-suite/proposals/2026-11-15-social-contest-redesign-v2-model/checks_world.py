"""v2 verification, part 2: the played game, the simulation, bearing, context, roles, power, the fold, the seasons.
PYTHONHASHSEED=0 python checks_world.py [n]"""
import sys, copy, math
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, build_view, Item, Choice
from scmodel.rng import draw
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
cast, T = F.cast(), F.TOLLS
D = host.dials()
FL = ("guildsmen", "toll_men", "clerk")
def H(t): print("\n== " + t)
def mat(rite, f="scholar", ag="bully"):
    return dict(T, parties={"for": f}) if rite in ("rally", "audience") else dict(T, parties={"for": f, "against": ag})
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))),
        ("trial", dict(bench=CB, floor=FL)), ("debate", dict(bench=CB, floor=("guildsmen",))),
        ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
def without(move):
    def f(view, me):
        os_ = [o for o in view.options if o.move != move] or list(view.options)
        o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
    return f

H("PLAYED: what he sees and chooses. Options on the first menu, per rite and side; decisions per sitting")
for rite, kw in ROWS:
    f = "orator" if rite == "rally" else "scholar"
    inp, card = host.build(cast, rite, mat(rite, f), effort=3, **kw)
    row = []
    for me in E.order(inp):
        v = build_view(inp, E._start(inp), me, draw(0, "v", rite), card.turns)
        row.append(f"{me.side}: {len(v.options)} ({', '.join(sorted({o.move for o in v.options}))})")
    print(f"  {rite:13} turns {card.turns} -> {card.turns} decisions each | " + " | ".join(row))
print("  skill: one side played by a view-only chooser, the other automatic; mean over five characters in the played seat (carried; n=%d each)" % (N // 2))
CH = ("orator", "scholar", "bully", "diplomat", "fox")
for rite, kw in ROWS:
    r = Counter()
    for f in CH:
        ag = "bully" if f != "bully" else "scholar"
        m = mat(rite, f, ag)
        for lab, dec in (("random", chooser("random")), ("automatic", None), ("best", smart)):
            r[lab] += rate(cast, rite, m, N // 2, "skill", deciders={f: dec} if dec else None, effort=3, **kw) / len(CH)
    n_ = len(CH) * (N // 2)
    print(f"   {rite:13} random {r['random']:.3f}  automatic (the man himself) {r['automatic']:.3f}  view-only best {r['best']:.3f}  (best-random {r['best']-r['random']:+.3f}, best-automatic {r['best']-r['automatic']:+.3f}; 2se {2*se(.4,n_)*1.41:.3f})")
pk = copy.deepcopy(F.mid_people()); pk["b"]["layers"] = dict(pursuits={"p": 0.95}, convictions={"c": 0}, relationships={"a": -0.5})
for lab, DD in (("shipped", D), ("control: read_blur 0 (everyone reads perfectly)", host.dials(read_blur=0.0))):
    r = {}
    for att in (1, 7):
        pk["a"]["attributes"]["attunement"] = att
        r[att] = rate(pk, "conversation", F.matter(), N * 2, "att", deciders={"a": smart, "b": chooser("rest")}, effort=3, D=DD)
    print(f"  a poor reader chooses worse only through the view: Attunement 1 -> {r[1]:.3f}, 7 -> {r[7]:.3f}, diff {r[7]-r[1]:+.3f} [{lab}]")
print("  every move on a menu is best somewhere: the view-only chooser with and without the option")
mpp = F.mid_people()
wk = copy.deepcopy(mpp); wk["b"]["attributes"].update(will=2, grace=2)
strong = copy.deepcopy(mpp); strong["a"]["attributes"].update(reason=7, presence=6); strong["a"]["rank"] = 3
able = copy.deepcopy(mpp)
for q in ("a", "b"): able[q]["attributes"].update(reason=6, grace=6, presence=5); able[q]["rank"] = 2
able["j1"]["layers"] = dict(pursuits={"p": 0.8}, convictions={"c": 4})
cold = copy.deepcopy(mpp); cold["crowd"]["layers"] = dict(pursuits={"p": 0.1}, convictions={"c": 1}, relationships={"a": -0.4})
def no_answer(view, me):
    os_ = [o for o in view.options if o.relation != "answers"] or list(view.options)
    o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
for lab, people, rite, who, mv, kw, inv in (
        ("rest: rally, a plain man before a cold crowd", cold, "rally", "a", "rest", dict(floor=("crowd",)), False),
        ("concede (descend): the accused against a strong accuser", strong, "trial", "b", "concede", dict(bench=BENCH), True),
        ("concede (accept): negotiation, the party addressed", mpp, "negotiation", "b", "concede", {}, False),
        ("answer: trial, two able advocates before a bench that can be moved", able, "trial", "b", "answers", dict(bench=BENCH), True),
        ("answer: negotiation, the same two", able, "negotiation", "b", "answers", {}, True)):
    m = dict(id="m", parties={"for": "a"}, bears={}) if rite == "rally" else F.matter()
    w_ = rate(people, rite, m, N, "menu", deciders={who: smart}, effort=4, **kw)
    wo = rate(people, rite, m, N, "menu", deciders={who: no_answer if mv == "answers" else without(mv)}, effort=4, **kw)
    if inv: w_, wo = 1 - w_, 1 - wo
    print(f"   {lab:58} with {w_:.3f}  without {wo:.3f}  ({w_-wo:+.3f})")
print("  leaks: the View's fields:", [f for f in E.View.__dataclass_fields__])
inp, card = host.build(cast, "trial", T, bench=CB, floor=FL, effort=3)
me = [p for p in inp.room if p.id == "scholar"][0]
vs = [build_view(inp, E._start(inp), me, draw(i, "leak", "t"), 3) for i in range(3000)]
def corr(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
fa = [dict(v.fit)["consequence"] for v in vs]; fb = [dict(v.fit)["authority"] for v in vs]; aa = [dict(v.aim)["consequence"] for v in vs]
dif = [x - y for x, y in zip(fa, fb)]
sdd = math.sqrt(sum((d - sum(dif) / len(dif)) ** 2 for d in dif) / len(dif))
print(f"  believed fit(consequence) vs fit(authority): corr of the noise {corr(fa, fb) - 0:+.3f} given accuracy shared; s.d. of the believed difference {sdd:.3f} (0 would leak the true difference; before: exactly 0); fit vs aim corr {corr(fa, aa):+.3f}")
resid = lambda xs, accs: [x for x in xs]
print(f"  the View holds no Present, no Beat.terms, no track: {not any(isinstance(getattr(vs[0], f), (E.Present, E.Beat)) for f in E.View.__dataclass_fields__)}; a mixed sitting (played `for`, automatic `against`) ran above in every rite")

H("SIMULATION: the automatic policy is the man. `for` in a trial against an ordinary respondent (400 sittings each)")
base = copy.deepcopy(cast); base["plain"] = F.P("plain"); base["plainr"] = F.P("plainr")
for who in ("orator", "scholar", "bully", "diplomat", "fox", "plain"):
    mv, gr, ins = Counter(), Counter(), 0.0; n = 0; car = 0
    m = dict(T, parties={"for": who, "against": "plainr"})
    for i in range(400):
        inp, card, out, b = sit(base, "trial", m, ("sim", i), bench=CB, floor=FL, effort=3)
        car += b[0] in CARRIED
        for x in out.beats:
            if x.mover == who:
                n += 1; mv[x.move] += 1; ins += x.insincere
                if x.ground: gr[x.ground] += 1
    print(f"  {who:9} press {mv['press']/n:.2f} argue {mv['argue']/n:.2f} rest {mv['rest']/n:.2f} concede {mv['concede']/n:.2f} | evidence {gr['evidence']/n:.2f} consequence {gr['consequence']/n:.2f} authority {gr['authority']/n:.2f} solidarity {gr['solidarity']/n:.2f} | insincere/beat {ins/n:.2f} | carried {car/400:.2f}")
print("  who prevails (carried as `for` against each other; trial before the bench / rally before the floor):")
names = ("orator", "scholar", "bully", "diplomat", "plain")
for rite, kw in (("trial", dict(bench=CB)), ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk")))):
    for a in names:
        if rite == "rally":
            print(f"   rally {a:9} {rate(base, 'rally', dict(T, parties={'for': a}), 400, 'rr', effort=3, **kw):.2f}", end=";")
        else:
            print(f"\n   trial {a:9} " + " ".join(f"{b[:4]} {rate(base, 'trial', dict(T, parties={'for': a, 'against': b}), 300, 'rr', effort=3, **kw):.2f}" for b in names if b != a), end="")
print()

H("BEARING: pursuits, convictions, ties (each with a flattened control)")
for who in ("orator", "bully", "scholar", "townsfolk"):
    st = host.bearing(cast[who], T, cast)
    print(f"  (a) {who:9} bearing of the toll matter (want, hold, bond) = {tuple(round(x, 2) for x in st)} -> stands {'for' if sum(st) > 0 else 'against'}, lean {D['lean_step']*sum(st)/3:+.2f}")
for lab, flat in (("shipped", ()), ("control: bearing flattened", ("bearing",))):
    r = {}
    for c_ in (0.1, 0.9):
        pp = copy.deepcopy(F.mid_people()); pp["b"]["layers"] = dict(pursuits={"p": c_})
        k = n = 0
        for i in range(N):
            inp, card, out, b = sit(pp, "conversation", F.matter(), ("bp", i), effort=1, flat=flat,
                                    deciders={"a": lambda v, me: Choice(*[(o.move, o.ground, o.item, o.relation) for o in v.options if o.move == "press" and o.ground == "consequence"][0]), "b": chooser("rest")})
            x = out.beats[0]; n += 1; k += x.rattled is not None
        r[c_] = k / n
    print(f"  (b) a press on what he wants: the pressed man's pursuit at 0.1 -> rattled {r[0.1]:.3f}; at 0.9 -> {r[0.9]:.3f} [{lab}]")
ral = dict(id="m", parties={"for": "a"}, bears={"faith": -1.0})
for lab, DD in (("shipped", D), ("control: ploy_step 0, grain_strain 0", host.dials(ploy_step=0.0, grain_strain=0.0))):
    r = {}
    for conv in (0, 5):
        pp = copy.deepcopy(F.mid_people()); pp["a"]["layers"] = dict(convictions={"faith": conv}) if conv else {}
        pp["crowd"]["attributes"]["attunement"] = 6
        ins = []; k = 0
        for i in range(N):
            inp, card, out, b = sit(pp, "rally", ral, ("ins", i), floor=("crowd",), effort=1, D=DD,
                                    deciders={"a": lambda v, me: Choice(*[(o.move, o.ground, o.item, o.relation) for o in v.options if o.ground == "authority"][0])})
            k += b[0] in CARRIED; ins.append(out.beats[0].insincere)
        r[conv] = (k / N, sum(ins) / N, dict(out.state.cond)["a"].strain)
    print(f"  (c) arguing from principle against the matter's bearing on his own conviction: no conviction carried {r[0][0]:.3f} (insincere {r[0][1]:.2f}); conviction 5 carried {r[5][0]:.3f} (insincere {r[5][1]:.2f}, strain after {r[5][2]:.2f}) [{lab}]")
for lab, flat in (("shipped", ()), ("control: bearing flattened", ("bearing",))):
    won, lost = [], []
    for i in range(300):
        w = host.new_world()
        TO = dict(T, parties={"for": "orator", "against": "bully"})
        inp, card, out, b = sit(cast, "trial", TO, ("pur", i), bench=CB, floor=FL, effort=3, flat=flat)
        pc = copy.deepcopy(cast)
        if flat:
            for p in pc.values(): p["layers"] = {}
        host.fold(w, pc, inp, card, out, TO)
        (won if b[0] in CARRIED else lost).append((w["pursuits"].get("orator", 0), w["pursuits"].get("bully", 0)))
    f = lambda xs, j: sum(x[j] for x in xs) / max(1, len(xs))
    print(f"  (d) the verdict moves what each wanted: the orator (trade 0.8) wins -> orator {f(won,0):+.2f}, bully {f(won,1):+.2f}; loses -> orator {f(lost,0):+.2f}, bully {f(lost,1):+.2f} [{lab}]")
for lab, flat in (("shipped", ()), ("control: bearing flattened", ("bearing",))):
    r = {}
    for j in ("judge2", "judge3"):
        r[j] = rate(cast, "audience", dict(T, parties={"for": "scholar", "against": "bully"}), N, "part", bench=(j,), effort=2, flat=flat)
    inp, card, out, b = sit(cast, "audience", dict(T, parties={"for": "scholar", "against": "bully"}), ("part", 0), bench=("judge2",), effort=2, flat=flat)
    w = host.new_world(); host.fold(w, cast, inp, card, out, T)
    seen = [c for c in w["ledgers"].get("scholar", []) if c[0] == "partial"]
    print(f"  (e) a decider tied to the respondent (judge2, the bully's client) carries {r['judge2']:.3f}; a neutral seat (judge3) {r['judge3']:.3f}; 'partial' claims the petitioner now holds: {seen[:1]} [{lab}]")
it = cast["scholar"]["items"][0]
inp, card = host.build(cast, "trial", T, bench=("judge",), floor=FL + ("judge2",), effort=3)
pr = {p.id: p for p in inp.room}
print(f"  (f) one record ({it.id}, weight {it.weight}, about the bully), credited by: the neutral judge {E.credit(pr['judge'], it):+.2f}; the bully's client judge2 {E.credit(pr['judge2'], it):+.2f}; the toll men (his friends) {E.credit(pr['toll_men'], it):+.2f}")
sm = Item("simony_letter", "record", 0.8, source="clerk", about="bishop")
p2 = copy.deepcopy(cast); p2["stranger"] = F.P("stranger")
inpx, _ = host.build(p2, "conversation", dict(id="x", parties={"for": "fox", "against": "scholar"}, bears={}), effort=1)
sc = [p for p in inpx.room if p.id == "scholar"][0]
inpy, _ = host.build(p2, "conversation", dict(id="x", parties={"for": "fox", "against": "stranger"}, bears={}), effort=1)
sr = [p for p in inpy.room if p.id == "stranger"][0]
print(f"  (g) a letter implicating the bishop: the bishop's client credits it {E.credit(sc, sm):+.2f} and a press with it aims {E.aim(sc, 'evidence', sm):+.2f} at him; a stranger credits it {E.credit(sr, sm):+.2f}, aim {E.aim(sr, 'evidence', sm):+.2f}")
for lab, flat in (("shipped", ()), ("control: bearing flattened", ("bearing",))):
    r = {}
    for need in (0.0, 0.9):
        pp = copy.deepcopy(cast); pp["diplomat"]["layers"]["needs"] = {"grain": need}
        mm = dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0})
        r[need] = rate(pp, "negotiation", mm, N, "need", effort=3, flat=flat, pred=lambda inp, card, out, b: out.ended == "yielded" and out.ended_by == "diplomat")
    print(f"  (h) a pressing need changes a concession: the diplomat accepts the grain terms {r[0.0]:.3f} with no need, {r[0.9]:.3f} with need 0.9 [{lab}]")

H("CONTEXT: the same matter and persons (trial of the toll matter; 600 sittings an arm)")
def arm(lab, **kw):
    try:
        inp, card = host.build(cast, "trial", T, bench=CB, floor=FL, effort=3, **kw)
    except ValueError as e:
        print(f"  {lab:34} REFUSED: {e}"); return
    r = rate(cast, "trial", T, 600, "ctx", bench=CB, floor=FL, effort=3, **kw)
    nb = sum(len(sit(cast, "trial", T, ("ctx", i), bench=CB, floor=FL, effort=3, **kw)[2].beats) for i in range(100)) / 100
    gw = {g: w for g, _, w in inp.grounds if w != 1.0}
    print(f"  {lab:34} standard {inp.rite.standard} lean {inp.rite.lean:+.1f} turns {inp.rite.turns} unrest {inp.rite.unrest} stakes {inp.rite.stakes} admits {len(inp.rite.admits)} era {gw or '-'} | beats {nb:.1f} carried {r:.3f}")
arm("crown, peace, plain era")
arm("theocracy", regime="theocracy")
arm("commune", regime="commune")
arm("famine", strife="famine")
arm("war", strife="war")
arm("age of faith", era="age_of_faith")
arm("mercantile age", era="mercantile")
arm("theocracy+famine+faith, FLATTENED", regime="theocracy", strife="famine", era="age_of_faith", flat=("context",))
for reg in ("crown", "theocracy", "commune"):
    print(f"  lawful under {reg}: {host.lawful(reg)}")
for lab, f in (("an office-holder (the bully, rung 2) as accuser", "bully"), ("a commoner (the clerk) as accuser", "clerk")):
    m = dict(T, parties={"for": f, "against": "scholar"})
    inp, card = host.build(cast, "trial", m, bench=CB, floor=FL, effort=3, arranger=f, rig=1.0)
    print(f"  {lab:48} power {host.power(cast[f]):.1f} tilt {card.tilt} turns {card.turns} room {[r[0] for r in card.room]} carried {rate(cast, 'trial', m, 600, 'off', bench=CB, floor=FL, effort=3, arranger=f, rig=1.0):.3f}")
for lab, bench in (("a partisan bench (judge2 presides alone)", ("judge2",)), ("a neutral bench (judge presides)", ("judge",))):
    print(f"  {lab:48} carried {rate(cast, 'trial', T, 600, 'pb', bench=bench, floor=FL, effort=3):.3f}; flattened {rate(cast, 'trial', T, 600, 'pb', bench=bench, floor=FL, effort=3, flat=('bearing',)):.3f}")

H("ROLES: one record, one reading")
st = []
for rite, kw, f, ag in (("trial", dict(bench=CB), "judge", "bully"), ("trial", dict(bench=CB), "scholar", "bully"), ("trial", dict(bench=CB, floor=("judge",)), "scholar", "bully")):
    m = dict(T, parties={"for": f, "against": ag})
    inp, _ = host.build(cast, rite, m, effort=3, **{k: tuple(x for x in v if x != f) if k == "bench" and f == "judge" else v for k, v in kw.items()})
    j = [p for p in inp.room if p.id == "judge"]
    if j: st.append((("speaks " + j[0].side) if j[0].side else ("judges" if j[0].decides else "attends"), j[0].care, tuple(round(x, 2) for x in j[0].stake)))
print(f"  (a) the judge as {st[0][0]} / {st[1][0]}: care {st[0][1]} / {st[1][1]} (equal: {st[0][1] == st[1][1]}); his stake differs only with the parties ({st[0][2]} / {st[1][2]})")
tw = copy.deepcopy(F.mid_people()); tw["j1"]["attributes"].update(reason=7, presence=2); tw["a"]["attributes"].update(reason=7, presence=2)
tw["a"]["office"] = tw["j1"]["office"]; tw["a"]["faction"] = tw["j1"]["faction"]
x1 = rate(tw, "trial", F.matter(f="a"), N, "swap", bench=("j1",), effort=3)
tw2 = copy.deepcopy(tw); tw2["a"], tw2["j1"] = dict(tw["j1"], id="a"), dict(tw["a"], id="j1")
x2 = rate(tw2, "trial", F.matter(f="a"), N, "swap", bench=("j1",), effort=3)
tw3 = copy.deepcopy(F.mid_people()); tw3["j1"]["attributes"].update(reason=7, presence=2)
x3 = rate(tw3, "trial", F.matter(f="a"), N, "swap", bench=("j1",), effort=3)
tw4 = copy.deepcopy(F.mid_people()); tw4["a"]["attributes"].update(reason=7, presence=2)
x4 = rate(tw4, "trial", F.matter(f="a"), N, "swap", bench=("j1",), effort=3)
print(f"  (b) two identical men swapped between advocate and judge: carried {x1:.3f} / {x2:.3f} (identical: {x1 == x2}); a Reason-7 man as the judge only {x3:.3f}, as the advocate only {x4:.3f}: the role's operands, not the person")
for lab, rel in (("no magnate in the gallery", None), ("a hostile magnate (power 4.5)", -0.9), ("a friendly magnate", 0.9)):
    pp = copy.deepcopy(F.mid_people())
    fl = ()
    if rel is not None:
        pp["mag"] = F.P("mag", office=F.seat(4, "Guild", "moderate"), layers=dict(relationships={"a": rel, "b": -rel})); fl = ("mag",)
    dr = rt = n = 0; car = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "trial", F.matter(), ("mag", i), bench=BENCH, floor=fl, effort=3)
        car += b[0] in CARRIED
        for x in out.beats:
            if x.mover == "a" and x.move == "argue": dr += x.drift; n += 1
        rt += dict(out.state.cond)["a"].rattles
    print(f"  (d) {lab:32} `for` mean drift per speech {dr/max(1,n):.3f}, rattles per sitting {rt/N:.3f}, carried {car/N:.3f}")
wc = vc = pw = 0
for i in range(400):
    inp, card, out, b = sit(cast, "trial", T, ("wit", i), bench=CB, floor=FL, effort=3)
    for x in out.beats:
        wc += x.voice != x.mover; pw += x.target == "clerk"
    vc += [p.side for p in inp.room if p.id == "clerk"][0] is None
print(f"  (e) the clerk is called from the floor in {wc} beats of 400 trials (he speaks his own testimony with his own dice); he is the one pressed next in {pw}; his role cell is unchanged after in {vc}/400")

H("POWER: who arranges, and what it costs (trial of the toll matter; the bully arranges against the scholar)")
def parm(lab, people, arranger, rig, flat=()):
    inp, card = host.build(people, "trial", T, bench=CB, floor=FL, effort=3, arranger=arranger, rig=rig, flat=flat)
    r = rate(people, "trial", T, 600, "pow", bench=CB, floor=FL, effort=3, arranger=arranger, rig=rig, flat=flat)
    w = host.new_world(); inp2, card2, out, b = sit(people, "trial", T, ("pow", 0), bench=CB, floor=FL, effort=3, arranger=arranger, rig=rig, flat=flat)
    host.fold(w, people, inp2, card2, out, T)
    pres = [p for p in inp.room if p.decides][0]
    print(f"  {lab:44} tilt {card.tilt:.2f} turns {card.turns} bench {card.decided_by} floor {len([x for x in card.room if x[1]=='attends'])} presiding lean {pres.lean:+.2f} | accuser carried {r:.3f} | legitimacy {w['legitimacy']} appeal {[d for d in w['docket'] if d[1]=='appeal']}")
parm("fair (rig 0)", cast, "bully", 0.0)
parm("a strong arranger, firm (rig 0.5)", cast, "bully", 0.5)
parm("a strong arranger, rigged (rig 1)", cast, "bully", 1.0)
eq = copy.deepcopy(cast); eq["scholar"]["office"] = F.seat(2, "Crown", "minor")
parm("two equals, rig 1", eq, "bully", 1.0)
wkp = copy.deepcopy(cast); wkp["bully"]["office"] = None; wkp["scholar"]["office"] = F.seat(4, "Church", "moderate")
parm("a weak arranger, rig 1", wkp, "bully", 1.0)
parm("rigged, power FLATTENED", cast, "bully", 1.0, flat=("power",))

H("THE FOLD: the disposal table, and two outcomes leaving two worlds (control: the proceeding is not held)")
SEVEN = (("heresy trial", "inquisition"), ("parliamentary debate", "debate"), ("private negotiation", "negotiation"), ("rallying a crowd", "rally"),
         ("interrogation for information", "questioning"), ("a trial", "trial"), ("the abridged form (tell)", "conversation"))
for name, rite in SEVEN:
    dsp = host.RITES[rite]["disposes"]
    print(f"  {name:30} ({rite}, disposes {dsp}): " + "; ".join(f"{b}: {'+'.join(w)}" for b, w in host.DISPOSAL[dsp].items()))
seen = {}
for i in range(200):
    inp, card, out, b = sit(cast, "trial", T, ("fold", i), bench=CB, floor=FL, effort=3)
    if b[0] not in seen:
        w = host.new_world(); band, writes = host.fold(w, cast, inp, card, out, T)
        seen[b[0]] = (w, writes)
empty = host.new_world()
for band in ("overwhelming", "success", "partial", "failure"):
    if band in seen:
        w, writes = seen[band]
        print(f"  trial {band:12} tenures {w['tenures']} offices {w['offices']} precedents {[p.id for p in w['precedents']]} docket {w['docket']} strife {w['strife']} | typed writes {len(writes)}: {sorted(set(x[0] for x in writes))}")
print(f"  control, not held: tenures {empty['tenures']} offices {empty['offices']} precedents {empty['precedents']} docket {empty['docket']} strife {empty['strife']}")

H("THREE SEASONS: a famine convenes a debate; its outcome moves the strife and a faction; a rigged trial returns as an appeal")
def season_run(seed, flat=()):
    people = copy.deepcopy(cast); world = host.new_world(); world["strife"]["famine"] = 1.0; log = []; wins = Counter()
    def hold(rite, m, **kw):
        nonlocal people
        strife = "famine" if world["strife"].get("famine", 0) > 0.6 else "peace"
        inp, card = host.build(people, rite, m, effort=3, strife=strife, flat=flat, **kw)
        out = proceed(inp, draw((seed, len(world["events"])), "act", rite))
        band, writes = host.fold(world, people, inp, card, out, m)
        won = band in CARRIED; f = m["parties"]["for"]; a = m["parties"].get("against")
        wins[f if won else (a or "nobody")] += 1
        for (x, y), v in world["regard"].items():                       # regard is read back as a relationship
            if x in people: people[x]["layers"].setdefault("relationships", {})[y] = max(-1, min(1, cast[x]["layers"].get("relationships", {}).get(y, 0.0) + v))
        for pid, rs in world["rattled"].items(): people[pid]["rattled_ago"] = tuple(rs)
        log.append(f"{rite}:{m['id']}[{strife}] {f} v {a}: {band}, {out.ended}" + (f", tilt {card.tilt}" if card.tilt else ""))
        return band
    for s in range(3):
        for pid in world["rattled"]: world["rattled"][pid] = [x + 1 for x in world["rattled"][pid]]
        if world["strife"].get("famine", 0) > 0.6:                      # the strife convenes: a motion to remit the tolls
            hold("debate", dict(T, id=f"remit_{s}", parties={"for": "orator", "against": "bully"}), bench=CB, floor=("guildsmen", "townsfolk"))
        hold("trial", dict(T, id=f"tolls_{s}", strife=None), bench=CB, floor=FL, arranger="bully", rig=1.0 if s == 0 else 0.0)
        for d in list(world["docket"]):
            if d[1] == "appeal":
                world["docket"].remove(d)
                hold("audience", dict(T, id=d[0], parties={"for": "scholar", "against": "bully"}, strife=None), bench=("bishop",) if False else ("judge",))
        hold("negotiation", dict(id=f"grain_{s}", parties={"for": "diplomat", "against": "bully"}, bears={"grain": 1.0, "tolls": -0.5}, strife="famine"))
    return world, people, log, wins
w, pe, log, wins = season_run(3)
for l in log: print("   " + l)
print(f"  after: famine {w['strife']['famine']:.2f} (began 1.00); standing {w['standing']}; legitimacy {w['legitimacy']}; tenures {w['tenures'][:4]}")
print(f"  earned grudges: scholar->bully {pe['scholar']['layers']['relationships'].get('bully', 0):+.2f} (began 0), bully->scholar {pe['bully']['layers']['relationships'].get('scholar'):+.2f} (began -0.70); strain carried in: bully {host.strain_carried(pe['bully'], D):.2f}, scholar {host.strain_carried(pe['scholar'], D):.2f}")
car = {0: [], 1: [], 2: []}; fam = []; ap = 0; st = []; after = {True: [], False: []}
for sd in range(80):
    w, pe, log, wins = season_run(sd)
    tr = [l for l in log if l.startswith("trial")]
    for k, l in enumerate(tr): car[k].append("success" in l or "overwhelming" in l)
    after[car[0][-1]].append(car[2][-1])
    fam.append(w["strife"]["famine"]); ap += any("appeal" in l for l in log); st.append(max(host.strain_carried(p, D) for p in pe.values()))
m_ = lambda xs: sum(xs) / max(1, len(xs))
print(f"  80 runs: the recurring trial carried in season 1 (rigged) {m_(car[0]):.2f}, season 2 {m_(car[1]):.2f}, season 3 {m_(car[2]):.2f}; season 3 carried after a season-1 win {m_(after[True]):.2f} (n={len(after[True])}), after a loss {m_(after[False]):.2f} (n={len(after[False])}): no snowball if these are close")
print(f"  famine after three seasons mean {m_(fam):.2f} range {min(fam):.2f}..{max(fam):.2f} (began 1.00); the rigged trial returned as an appeal in {ap}/80 runs; greatest strain carried by anyone {max(st):.2f} (bound 1.00)")
tot0 = Counter()
c0 = []
for sd in range(80): c0.append(any(("success" in l or "overwhelming" in l) for l in season_run(sd, flat=("bearing",))[2] if l.startswith("trial")))
print(f"  control (bearing flattened): a trial carried in some season in {m_(c0):.2f} of runs (shipped: {m_([a or b or c for a, b, c in zip(car[0], car[1], car[2])]):.2f})")
