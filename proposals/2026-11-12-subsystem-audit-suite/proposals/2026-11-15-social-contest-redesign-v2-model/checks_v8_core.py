"""v8 core: every figure of the reconciliation, re-measured on the model after the second fix pass (run through checks_v8.py)."""
import sys, copy, math, hashlib
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, build_view, Item, Choice, p_carried
from scmodel.rng import draw
from scmodel import dice
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
mp, M = F.mid_people(), F.matter()
cast, T = F.cast(), F.TOLLS
D, C = host.dials(), host.controls()
FL = ("guildsmen", "toll_men", "clerk")
def H(t): print("\n== " + t)
def force(pred):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)] or list(v.options)
        o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
    return f
only = lambda mv: force(lambda o: o.move == mv)
ground = lambda g: force(lambda o: o.move == "argue" and o.ground == g)
def sw(people, rite, m, who, attr, lv=(1, 7), n=N, **kw):
    r = {}
    for x in lv:
        pp = copy.deepcopy(people); pp[who]["attributes"][attr] = x
        r[x] = rate(pp, rite, m, n, "sw", **kw)
    d = r[lv[1]] - r[lv[0]]
    return f"{r[lv[0]]:.3f}->{r[lv[1]]:.3f} ({d:+.3f}, z {d / math.hypot(se(r[lv[0]], n), se(r[lv[1]], n)):+.1f})"

H("D1 bench reads the sitting (trial, all-mid, effort 3)")
for lab, DD in (("shipped", D), ("control track_step 0", host.dials(track_step=0.0))):
    bins = Counter(); car = Counter()
    for i in range(N):
        inp, card, out, b = sit(mp, "trial", M, ("d1", i), bench=BENCH, effort=3, D=DD)
        t = dict(out.state.tracks)["j1"]; k = "<=-3" if t <= -3 else "<0" if t < 0 else "<3" if t < 3 else ">=3"
        bins[k] += 1; car[k] += b[0] in CARRIED
    print(f"  {lab:22} " + "  ".join(f"{k} n={bins[k]} {car[k]/max(1,bins[k]):.3f}" for k in ("<=-3", "<0", "<3", ">=3")))
print(f"  excommunication (declared, quorum 2): carried {rate(mp, 'excommunication_deliberation', M, N, 'x', bench=('c1','c2','c3'), effort=2):.3f}")

H("D2 the centre (the tell, equals rank 1)")
def tell(DD, diff=None):
    if diff is not None: old = host.DIFFICULTY["routine"]; host.DIFFICULTY["routine"] = diff
    c = Counter(sit(mp, "conversation", M, ("d2", i), form="abridged", D=DD)[3][0] for i in range(N * 3))
    if diff is not None: host.DIFFICULTY["routine"] = old
    n = N * 3; return f"fail {c['failure']/n:.3f} half {c['partial']/n:.3f} carried {(c['success']+c['overwhelming'])/n:.3f}"
print(f"  v2 shipped, routine 0.5: {tell(D)} | at controls: {tell(C)} | routine 0.8: {tell(D, 0.8)}")
plain = Counter()
for i in range(N * 3):
    x = dice.SocialContestInput(pool=11.0, opposition=1.0, leverage=0.0, difficulty=0.5, obstacle_operands=(), pool_default=2, pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
    plain[dice.degree(dice.roll(x, draw(("pl", i), "a", "t")))] += 1
n = N * 3
print(f"  the PLAN's plain roll (B05.25 pool, skill-score-only opposition): fail {plain['failure']/n:.3f} half {plain['partial']/n:.3f} carried {(plain['success']+plain['overwhelming'])/n:.3f}  [A-79: .59/.16/.25]")
ok = 0
for i in range(200):
    inp, card = host.build(mp, "conversation", M, form="abridged", D=C); out = proceed(inp, draw(("eq", i), "act", "conversation"))
    rng = draw(("eq", i), "act", "conversation"); [rng.normal() for _ in range(E.DRAWS_PER_EXCHANGE(4) - 1)]
    x = dice.SocialContestInput(pool=11.0, opposition=5.0, leverage=0.0, difficulty=0.5, obstacle_operands=(), pool_default=2, pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
    m = dice.roll(x, rng); v = out.verdicts[0][1]; ok += abs((v.net - v.ob) - (m.net - m.ob)) < 1e-9
print(f"  at control the abridged margin == the one roll under A-137's rule (opposition = Will + rank): {ok}/200")

H("D3 / F2 the rattle and the concession")
wk = copy.deepcopy(mp); wk["b"]["attributes"].update(will=2, grace=2)
def p1(view, me): return (only("press") if view.own.spoken == 0 else only("argue"))(view, me)
OFF = host.dials(rattle_gain=0.0, show=0.0, rattle_pull=0.0, press_pull=0.0, wear=0.0)
for lab, dec in (("one press then argue", p1), ("argue only", only("argue")), ("press every turn", only("press"))):
    print(f"  trial vs a Will-2 Grace-2 respondent who plays AUTOMATICALLY, `for` {lab:22} carried {rate(wk, 'trial', M, N, 'd3', bench=BENCH, effort=3, deciders={'a': dec}):.3f}; a rattle that does nothing {rate(wk, 'trial', M, N, 'd3', bench=BENCH, effort=3, deciders={'a': dec}, D=OFF):.3f}")
def yielded_to(rite, who, kw, people=mp):
    return {lab: rate(people, rite, M, N, "f2", effort=3, deciders=({who: dec} if dec else None), **kw) for lab, dec in (("concedes at once", only("concede")), ("automatic", None), ("never concedes", force(lambda o: o.move != "concede")))}
print(f"  questioning: the questioner gets what he asks (the questioned man's accept) when the questioned: {yielded_to('questioning', 'b', {})}")
print(f"  trial: `for` carried when the ACCUSED: {yielded_to('trial', 'b', dict(bench=BENCH))}  (conceding walks the ladder: fact, definition, justification, then the matter)")
print(f"  trial: `for` carried when the ACCUSER: {yielded_to('trial', 'a', dict(bench=BENCH))}; debate, the mover: {yielded_to('debate', 'a', dict(bench=BENCH))}")
full = [0, 0]
for i in range(N):
    inp, card, out, b = sit(mp, "trial", M, ("conf", i), bench=BENCH, effort=4, deciders={"b": only("concede")})
    if out.ended == "yielded": full[0] += 1; full[1] += b[0] in CARRIED
print(f"  a full confession (the accused concedes the last rung): convicted {full[1]}/{full[0]} = {full[1]/max(1,full[0]):.3f} (the close is still the bench's draw: A-14)")

H("D5 / D6")
p1_ = rate(mp, "trial", M, N * 2, "d5", bench=BENCH, effort=3); host.RITES["trial"]["bears"] = "against"
p2_ = rate(mp, "trial", M, N * 2, "d5", bench=BENCH, effort=3); host.RITES["trial"]["bears"] = "for"
print(f"  trial, `for` opens {p1_:.3f}; `against` opens {p2_:.3f}; diff {p1_-p2_:+.3f} +- {2*se(p1_, N*2)*1.41:.3f}")
c = Counter()
for i in range(N):
    inp, card, out, b = sit(mp, "negotiation", M, ("d6", i), effort=3); c[(b[0], out.ended)] += 1
print(f"  negotiation (consent): {dict(c)}: Success only where the party addressed accepted")

H("F7 speaking at a formal venue (trial, all-mid, `for` chooser against the automatic other side)")
print("  " + "; ".join(f"{k}: {rate(mp, 'trial', M, N * 2, 'f7', bench=BENCH, effort=3, deciders=({'a': d} if d else None)):.3f}" for k, d in (("argue every turn", only("argue")), ("automatic", None), ("rest every turn", only("rest")))))

H("F8 the judge's own three in a FULL TRIAL, each with the sign the ruling gives, and with its setting off")
rec = Item("deed", "record", 0.9)
def f8(lab, attr, prep, kw, off):
    pp = copy.deepcopy(mp); prep(pp)
    print(f"  judge's {attr:10} {lab:58} {sw(pp, 'trial', M, 'j1', attr, bench=('j1',), effort=3, **kw)} | setting off {sw(pp, 'trial', M, 'j1', attr, bench=('j1',), effort=3, D=host.dials(**off), **kw)}")
def good_case(pp): pp["a"]["items"] = (rec,); pp["a"]["attributes"].update(reason=6)
f8("`for` is sound but plain (Reason 7, Grace 2), the other polished (Reason 1, Grace 7): up", "reason", lambda pp: (pp["a"]["attributes"].update(reason=7, grace=2), pp["b"]["attributes"].update(reason=1, grace=7)), dict(deciders={"a": only("argue"), "b": only("argue")}), dict(sense_step=0.0))
f8("the other way round: down", "reason", lambda pp: (pp["b"]["attributes"].update(reason=7, grace=2), pp["a"]["attributes"].update(reason=1, grace=7)), dict(deciders={"a": only("argue"), "b": only("argue")}), dict(sense_step=0.0))
f8("`for` wanders (Focus 1, a famine): down", "focus", lambda pp: pp["a"]["attributes"].update(focus=1), dict(strife="famine", deciders={"a": only("argue"), "b": only("rest")}), dict(off_step=0.0))
f8("the OTHER side wanders (both argue; the bearer must put his case): up", "focus", lambda pp: pp["b"]["attributes"].update(focus=1), dict(strife="famine", deciders={"a": only("argue"), "b": only("argue")}), dict(off_step=0.0))
f8("`for` argues what he knows to be false: down", "attunement", lambda pp: pp["a"].update(believes={"m": -1.0}), dict(deciders={"a": only("argue"), "b": only("rest")}), dict(ploy_step=0.0))
f8("the OTHER side argues what he knows false (both argue): up", "attunement", lambda pp: pp["b"].update(believes={"m": 1.0}), dict(deciders={"a": only("argue"), "b": only("argue")}), dict(ploy_step=0.0))

H("ROLES the speaker's six, and the restored carriers (carried at attribute 1 -> 7)")
ral = dict(id="m", parties={"for": "a"}, bears={})
rp = copy.deepcopy(mp)
for q, cr in (("b", dict(pursuits={"p": 0.9}, convictions={"c": 1})), ("j1", dict(pursuits={"p": 0.2}, convictions={"c": 5})), ("crowd", dict(pursuits={"p": 0.9}, convictions={"c": 1}))): rp[q]["layers"] = cr
for scen, rite, m, kw in (("tell", "conversation", M, dict(form="abridged")), ("trial", "trial", M, dict(bench=BENCH, effort=3, floor=("crowd",))), ("rally", "rally", ral, dict(floor=("crowd",), effort=3))):
    print(f"  {scen:6} " + " | ".join(f"{a[:4]} {sw(rp, rite, m, 'a', a, **kw)}" for a in host.ATTRS))
big = copy.deepcopy(mp); big["b"]["office"] = F.seat(4, "Crown", "moderate")
for lab, DD in (("shipped", D), ("gap_step 0", host.dials(gap_step=0.0))):
    print(f"  Reason accounts for the other side's circumstances: vs a power-{host.power(big['b']):.1f} respondent, `for` at Presence-dice only (solidarity ground, k=0): Reason {sw(big, 'conversation', M, 'a', 'reason', form='abridged', D=DD, deciders={'a': ground('solidarity')})} [{lab}]")
for lab, DD in (("shipped", D), ("heard_step 0", host.dials(heard_step=0.0))):
    print(f"  Presence, the share heard: before a crowd, arguing on the proof (k high): Presence {sw(dict(mp, a=dict(mp['a'], items=(rec,))), 'trial', M, 'a', 'presence', bench=BENCH, floor=('crowd',), effort=3, D=DD, deciders={'a': ground('evidence'), 'b': only('rest')})} [{lab}]")
for lab, DD in (("shipped", D), ("weary_step 0", host.dials(weary_step=0.0))):
    print(f"  Will, staying power: arguing all five turns of a trial, nobody pressing: Will {sw(mp, 'trial', M, 'a', 'will', bench=BENCH, effort=4, D=DD, deciders={'a': only('argue'), 'b': only('rest')})} [{lab}]")
for lab, DD in (("shipped", D), ("esteem_step 0", host.dials(esteem_step=0.0))):
    print(f"  Grace, esteem in the room: trial against an ordinary man: Grace {sw(mp, 'trial', M, 'a', 'grace', bench=BENCH, effort=3, D=DD)} [{lab}]")
for att in (1, 7):
    xs, ys = [], []
    for i in range(400):
        pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att; st = ((i % 9) - 4) / 4.0
        pp["b"]["layers"] = dict(pursuits={"t": 1.0}); inp, card = host.build(pp, "trial", dict(M, bears={"t": st}), bench=BENCH)
        v = build_view(inp, E._start(inp), inp.room[0], draw(("int", i), "v", "t"), 3); xs.append(v.intent); ys.append(st / 3)
    mx, my = sum(xs) / 400, sum(ys) / 400
    print(f"  Attunement reads intent: corr(believed stake of the man opposite, his true stake) at Attunement {att}: {sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys)):+.2f}")
for lean in (0.3, -0.3):
    old = host.RITES["audience"]["reason_lean"]; host.RITES["audience"]["reason_lean"] = lean; r = {}
    for nm, at in (("scholar-like (Reason 7, Presence 2)", dict(reason=7, presence=2)), ("orator-like (Presence 7, Reason 2)", dict(presence=7, reason=2))):
        pp = copy.deepcopy(mp); pp["a"]["attributes"].update(at); r[nm] = rate(pp, "audience", ral, N, "ven", bench=("j1",), effort=2, deciders={"a": ground("consequence")})
    host.RITES["audience"]["reason_lean"] = old
    print(f"  R11 the venue arm: the same ground (consequence) before one seat, venue lean {lean:+.1f}: {r}")

H("F1 / B-3 the view")
inp, card = host.build(cast, "trial", T, bench=CB, floor=FL, effort=3)
st0 = E._start(inp); me = inp.room[0]
st1, _, _, _ = E.exchange(inp, st0, inp.room[1], Choice("argue", "consequence", None, "raises"), draw(1, "x", "y"))
vs = [build_view(inp, st1, me, draw(i, "leak", "t"), 3) for i in range(3000)]
def corr(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
low = [v for v in vs if v.acc < 0.3]
kk = {(o.move, o.ground): k for k, o in enumerate(vs[0].options) if o.relation in ("raises", "presses")}
e_ = lambda v, k: v.options[k].ev
print(f"  poor readers (acc < 0.3, n={len(low)}): correlation of the errors of two perceived numbers: argue consequence, argue authority {corr([e_(v, kk[('argue','consequence')]) for v in low], [e_(v, kk[('argue','authority')]) for v in low]):+.3f}; an option, the mood {corr([e_(v, kk[('argue','consequence')]) for v in low], [v.mood for v in low]):+.3f}; mood, their point {corr([v.mood for v in low], [v.live_theirs[3] for v in low]):+.3f}; intent, mood {corr([v.intent for v in low], [v.mood for v in low]):+.3f}")
print(f"  View fields: {list(E.View.__dataclass_fields__)}")
dl = car = 0
for i in range(N * 2):
    inp, card, out, b = sit(mp, "trial", M, ("odds", i), bench=BENCH, effort=3, decide=only("rest")); car += b[0] in CARRIED
print(f"  F3 card odds {card.odds} vs delivered with both sides silent {car/(N*2):.3f}; consent: card odds {host.build(mp, 'negotiation', M)[1].odds}, band when both rest: {sit(mp, 'negotiation', M, 0, decide=only('rest'))[3][0]}; abridged: card odds {host.build(mp, 'conversation', M, form='abridged')[1].odds} (the option's own chance is shown)")
land = pl = 0
for i in range(N * 2):
    inp, card = host.build(mp, "conversation", M, form="abridged"); rng = draw(("ab", i), "a", "t")
    v = build_view(inp, E._start(inp), inp.room[0], rng, 1); pl += v.options[0].p
    out = proceed(inp, draw(("ab", i), "a", "t")); land += out.beats[0].margin >= 0
print(f"  abridged: the menu's believed chance to land (mean) {pl/(N*2):.3f} vs delivered {land/(N*2):.3f}")

H("F4 resume, F5 refusals, the nemo rule")
inp1, card1 = host.build(mp, "trial", M, bench=BENCH, effort=1); o1 = proceed(inp1, draw(1, "a", "r"), decide=only("argue"))
inp2, card2 = host.build(mp, "trial", M, bench=BENCH, effort=3, state=o1.state); o2 = proceed(inp2, draw(2, "a", "r"), decide=only("argue"))
print(f"  first sitting {card1.turns} turns each -> spoken {[(i, c.spoken) for i, c in o1.state.cond if c.spoken]}; resumed under {card2.turns} turns: {len(o2.beats)} more beats, spoken {[(i, c.spoken) for i, c in o2.state.cond if c.spoken]}; beats continue at n={o2.beats[0].n}")
def refused(lab, fn):
    try: fn(); print(f"  NOT REFUSED: {lab}")
    except ValueError as e: print(f"  refused: {lab}: {e}")
oy = proceed(host.build(mp, "trial", M, bench=BENCH, effort=3)[0], draw(3, "a", "r"), deciders={"a": only("concede")})
refused("resuming a sitting that ended yielded", lambda: host.build(mp, "trial", M, bench=BENCH, state=oy.state))
refused("a rally with nobody on the floor", lambda: host.build(mp, "rally", ral))
refused("an abridged rally with nobody addressed", lambda: host.build(mp, "rally", ral, form="abridged"))
refused("a cohort of weight 0", lambda: host.build(dict(mp, crowd=dict(mp["crowd"], weight=0)), "rally", ral, floor=("crowd",)))
refused("a sitting with one character", lambda: E.Input(inp1.rite, "m", inp1.room[:1], inp1.grounds, D))
o = proceed(*[host.build(mp, "trial", M, bench=BENCH, effort=3)[0]], draw(5, "a", "j"), rulings={"j1": lambda jv: "against" if jv.track > 0 else "for"})
print(f"  a played judge: sees JudgeView{tuple(E.JudgeView.__dataclass_fields__)}; chooses for / against / leave it to the draw; ruling against his own track {dict(o.state.tracks)['j1']:+.2f} is returned as a departure {o.ruled} (the fold deposits it as a claim)")

H("A-136 the NPC's temper (one seat played by the view-only best chooser against the SAME man automatic; other side automatic)")
def man(will, grace, rel, care_):
    pp = copy.deepcopy(mp); pp["a"]["attributes"].update(will=will, grace=grace); pp["a"]["layers"] = dict(relationships={"b": rel}, pursuits={"p": care_[0]}, convictions={"c": care_[1]}); return pp
for lab, pp in (("flat, composed (Will 4, Grace 4)", mp), ("cool (Will 6, Grace 7, a grudge)", man(6, 7, -0.9, (0.9, 1))), ("hot and proud (Will 6, Grace 1, a grudge)", man(6, 1, -0.9, (0.9, 1))), ("hot and timid (Will 1, Grace 2)", man(1, 2, 0.0, (0.5, 3)))):
    row = []
    for rite, kw in (("trial", dict(bench=BENCH)), ("inquisition", dict(bench=("c1", "c2"))), ("debate", dict(bench=BENCH))):
        a_ = rate(pp, rite, M, N * 2, "tm", effort=3, **kw); s_ = rate(pp, rite, M, N * 2, "tm", effort=3, deciders={"a": smart}, **kw)
        mv = Counter(x.move for i in range(150) for x in sit(pp, rite, M, ("tm", i), effort=3, **kw)[2].beats if x.mover == "a")
        row.append(f"{rite}: auto {a_:.3f} best {s_:.3f} ({s_-a_:+.3f}) press share {mv['press']/max(1,sum(mv.values())):.2f} concede {mv['concede']/max(1,sum(mv.values())):.2f}")
    print(f"  {lab:42} " + " | ".join(row))
print(f"  (2 s.e. of a difference at n={N*2}: {2*se(.35, N*2)*1.41:.3f}); control temper off (grain, grudge, pride 0): the automatic policy IS the best chooser by construction")
base = copy.deepcopy(cast); base["plainr"] = F.P("plainr")
for lab, DD in (("shipped", D), ("temper off", host.dials(grain=0.0, grudge=0.0, pride=0.0))):
    row = []
    for who in ("orator", "scholar", "bully", "diplomat", "fox"):
        mv, gr, n = Counter(), Counter(), 0
        for i in range(200):
            for x in sit(base, "trial", dict(T, parties={"for": who, "against": "plainr"}), ("sim", i), bench=CB, floor=FL, effort=3, D=DD)[2].beats:
                if x.mover == who: n += 1; mv[x.move] += 1; gr[x.ground] += 1
        row.append(f"{who}: press {mv['press']/n:.2f} proof {gr['evidence']/n:.2f} fellowship {gr['solidarity']/n:.2f} concede {mv['concede']/n:.2f}")
    print(f"  the man in a trial [{lab}]: " + " | ".join(row))

H("BEARING (B-5 fit reads the matter; R12 sincerity; ties), each with a control")
inp, card = host.build(cast, "rally", dict(T, parties={"for": "orator"}), floor=("guildsmen", "toll_men", "townsfolk"))
pr = {p.id: p for p in inp.room}
print(f"  a consequence argument FOR remitting the tolls fits: guildsmen {E.fit(pr['guildsmen'], pr['orator'], 'for', 'consequence', None):+.2f}, toll men {E.fit(pr['toll_men'], pr['orator'], 'for', 'consequence', None):+.2f}, townsfolk {E.fit(pr['townsfolk'], pr['orator'], 'for', 'consequence', None):+.2f}; flattened: {E.fit(host.build(cast, 'rally', dict(T, parties={'for': 'orator'}), floor=('toll_men',), flat=('bearing',))[0].room[1], pr['orator'], 'for', 'consequence', None):+.2f}")
for lab, fl in (("shipped", ()), ("flattened", ("bearing",))):
    r = {}
    for c_ in (0.1, 0.9):
        pp = copy.deepcopy(mp); pp["b"]["layers"] = dict(pursuits={"p": c_})
        r[c_] = rate(pp, "conversation", M, N, "bp", effort=1, flat=fl, deciders={"a": force(lambda o: o.move == "press" and o.ground == "consequence"), "b": only("rest")}, pred=lambda inp, card, out, b: out.beats[0].rattled is not None)
        r[("on", c_)] = rate(pp, "conversation", dict(M, bears={"p": -1.0}), N, "bp", effort=1, flat=fl, deciders={"a": force(lambda o: o.move == "press" and o.ground == "consequence"), "b": only("rest")}, pred=lambda inp, card, out, b: out.beats[0].rattled is not None)
    print(f"  B7 a press on what he wants: rattled {r[0.1]:.3f} at pursuit 0.1, {r[0.9]:.3f} at 0.9 when the matter does not touch it; {r[('on', 0.1)]:.3f}, {r[('on', 0.9)]:.3f} when it does [{lab}]")
lie = Item("false_report", "rumour", 0.8, source="a", sincere=False)
for lab, DD in (("shipped", D), ("ploy_step 0", host.dials(ploy_step=0.0, grain_strain=0.0))):
    pa = copy.deepcopy(mp); pa["crowd"]["attributes"]["attunement"] = 6
    hon = rate(pa, "rally", ral, N, "lie", floor=("crowd",), effort=1)
    pb = copy.deepcopy(pa); pb["a"]["believes"] = {"m": -1.0}
    hon = rate(pa, "rally", ral, N, "lie", floor=("crowd",), effort=1, deciders={"a": only("argue")})
    self_serving = rate(pb, "rally", ral, N, "lie", floor=("crowd",), effort=1, D=DD, deciders={"a": only("argue")})
    pc = copy.deepcopy(pa); pc["a"]["items"] = (lie,); host.RITES["rally"]["admits"] += ("rumour",) if "rumour" not in host.RITES["rally"]["admits"] else ()
    forged = rate(pc, "rally", ral, N, "lie", floor=("crowd",), effort=1, D=DD, deciders={"a": ground("evidence")})
    print(f"  before an attuned crowd: an honest plea {hon:.3f}; a SELF-SERVING lie (it helps him and he knows it false) {self_serving:.3f}; an argument on a claim he knows false {forged:.3f} [{lab}]")
fz = copy.deepcopy(mp); fz["a"]["items"] = (Item("forged_writ", "record", 0.9, about="b", sincere=False),); fz["j1"]["attributes"]["attunement"] = 7
for lab, DD in (("shipped", D), ("ploy_step 0", host.dials(ploy_step=0.0))):
    print(f"  a press made with a forged writ before an attuned judge: `for` carried {rate(fz, 'trial', M, N, 'fz', bench=('j1',), effort=2, D=DD, deciders={'a': force(lambda o: o.move == 'press' and o.ground == 'evidence'), 'b': only('rest')}):.3f} [{lab}]")
for lab, fl in (("shipped", ()), ("flattened", ("bearing",))):
    r = {j: rate(cast, "audience", dict(T, parties={"for": "scholar", "against": "bully"}), N, "part", bench=(j,), effort=2, flat=fl) for j in ("judge2", "judge3")}
    it = cast["scholar"]["items"][0]; pr = {p.id: p for p in host.build(cast, "trial", T, bench=("judge",), floor=FL + ("judge2",), flat=fl)[0].room}
    nd = {}
    for need in (0.0, 0.9):
        pp = copy.deepcopy(cast); pp["diplomat"]["layers"]["needs"] = {"grain": need}
        nd[need] = rate(pp, "negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0}), N, "need", effort=3, flat=fl)
    print(f"  [{lab}] petition before the respondent's client {r['judge2']:.3f}, a neutral seat {r['judge3']:.3f} | the ledger credited: neutral judge {E.credit(pr['judge'], it):+.2f}, the respondent's client {E.credit(pr['judge2'], it):+.2f} | the diplomat accepts with need 0 / 0.9: {nd[0.0]:.3f} / {nd[0.9]:.3f}")

H("CONTEXT and POWER (toll trial; `for` carried)")
def arm(**kw):
    try: return f"{rate(cast, 'trial', T, N, 'ctx', bench=CB, floor=FL, effort=3, **kw):.3f}"
    except ValueError as e: return "refused"
print("  " + "; ".join(f"{k} {arm(**kw)}" for k, kw in (("crown/peace", {}), ("theocracy", dict(regime="theocracy")), ("commune", dict(regime="commune")), ("famine", dict(strife="famine")), ("war", dict(strife="war")), ("age of faith", dict(era="age_of_faith")), ("mercantile", dict(era="mercantile")), ("all three FLATTENED", dict(regime="theocracy", strife="famine", era="age_of_faith", flat=("context",))))))
for lab, kw in (("fair", dict(arranger="bully", rig=0.0)), ("firm", dict(arranger="bully", rig=0.5)), ("rigged", dict(arranger="bully", rig=1.0)), ("rigged, power flattened", dict(arranger="bully", rig=1.0, flat=("power",)))):
    inp, card, out, b = sit(cast, "trial", T, ("pw", 0), bench=CB, floor=FL, effort=3, **kw); w = host.new_world(); host.fold(w, cast, inp, card, out, T)
    print(f"  {lab:24} tilt {card.tilt:.2f} turns {card.turns} bench {card.decided_by} floor {sum(1 for x in card.room if x[1]=='attends')} | accuser carried {arm(**kw)} | legitimacy {w['legitimacy']} appeal weight {w['appeal_weight']} price {host.rig_price(card.tilt):.3f}")

H("F6 the fold performs every write; regard moves both ways; three seasons")
up = dn = 0; ops = Counter()
for i in range(300):
    inp, card, out, b = sit(cast, "conversation", dict(T, parties={"for": "orator", "against": "diplomat"}), ("f6", i), effort=3); w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, T)
    up += sum(1 for x in wr if x[0] == "regard+"); dn += sum(1 for x in wr if x[0] == "regard-"); ops.update(x[0] for x in wr)
print(f"  300 conversations: regard writes up {up}, down {dn}; write kinds {dict(ops)}")
ops = Counter(); bands = Counter()
for i in range(300):
    inp, card, out, b = sit(cast, "trial", T, ("f6t", i), bench=CB, floor=FL, effort=3); w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, T); ops.update(x[0] for x in wr); bands[band] += 1
print(f"  300 trials: bands {dict(bands)}; write kinds {dict(ops)}")
print("  (three seasons: the season driver sc2/acts.py, run in fix2/d2.py)")

H("TYPES in play, typical outcomes, and the invariants (the cast, effort 3; half automatic, half random choosers)")
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))), ("trial", dict(bench=CB, floor=FL)), ("debate", dict(bench=CB, floor=("guildsmen",))), ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
viol = Counter(); nb = 0; allm = Counter(); alle = Counter()
for rite, kw in ROWS:
    m = dict(T) if rite not in ("rally", "audience") else dict(T, parties={"for": "orator" if rite == "rally" else "scholar"})
    mv, rel_, en, bd = Counter(), Counter(), Counter(), Counter(); nbt = 0
    for i in range(300):
        dec = {} if i % 2 == 0 else {p: chooser("random", i) for p in cast}
        inp, card, out, b = sit(cast, rite, m, ("inv", i), effort=3, deciders=dec, **kw)
        if i % 2 == 0:
            for x in out.beats: mv[x.move] += 1; rel_[x.relation] += 1
            en[out.ended] += 1; bd[b[0]] += 1; nbt += len(out.beats)
        held = {p.id: {it.id for it in p.items} for p in inp.room}; kinds = {it.id: it.kind for p in inp.room for it in p.items}; closed, spoke = set(), Counter()
        for k, x in enumerate(out.beats):
            nb += 1
            viol["chain"] += x.n != k + 1; viol["no point"] += x.move == "argue" and x.point is None
            viol["answers nothing"] += x.relation == "answers" and not any(p.id == x.point and p.side != x.side for p in out.state.points)
            viol["item not held"] += bool(x.item) and x.item not in held[x.mover]; viol["item not admitted"] += bool(x.item) and kinds[x.item] not in card.admits
            viol["closed issue re-argued"] += x.issue in closed; viol["move not on the card"] += x.move not in dict(card.moves)[x.side]
            viol["evasion unpriced"] += x.evaded and not x.rattled and not any(d != 0 for _, d in x.moved) and any(p.focus > 1 for p in inp.room if p.side != x.side); viol["a non-deciding speaker moved his own track"] += any(q == x.voice and not next(p for p in inp.room if p.id == q).decides for q, _ in x.moved)
            if x.closed and not (out.ended == "yielded" and k == len(out.beats) - 1): closed.add(x.closed)
            spoke[x.mover] += 1
        viol["over the card's turns"] += any(v > card.turns for v in spoke.values())
        viol["verdicts != the card's adjudicators"] += set(i_ for i_, _ in out.verdicts) != set(card.decided_by)
        viol["track != start + beats"] += any(abs(dict(out.state.tracks)[p.id] - p.start - sum(d for x in out.beats for q, d in x.moved if q == p.id)) > 1e-6 for p in inp.room)
        viol["consent with a verdict"] += card.close == "consent" and bool(out.verdicts)
    allm.update(mv); alle.update(en)
    print(f"  {rite:12} moves {dict(mv)} | answers {rel_['answers']} raises {rel_['raises']} | ends {dict(en)} | beats {nbt/150:.1f} | bands {dict(bd)}")
print(f"  every move {dict(allm)}; every end {dict(alle)}")
print(f"  beats checked {nb}; violations {dict(viol)}")
def digest(DD):
    h = hashlib.sha256(); c2 = copy.deepcopy(cast); c2["bully"]["rattled_ago"] = (0, 1); c2["scholar"]["believes"] = {"tolls": -0.5}
    for rite, kw in ROWS:
        m = dict(T) if rite not in ("rally", "audience") else dict(T, parties={"for": "orator" if rite == "rally" else "scholar"})
        for i in range(20):
            inp, card, out, b = sit(c2, rite, m, ("abl", i), effort=4, D=DD, arranger="bully" if rite == "trial" else None, rig=0.5 if rite == "trial" else 0.0, **kw)
            h.update(repr((b[0], round(b[1] or 0, 6), len(out.beats), out.ended)).encode())
    return h.hexdigest()
base = digest(D); own = [k for k in host.SHIPPED if k not in ("pool_add", "pool_floor", "pool_default", "opposition_rate", "mid", "floor", "ceiling")]
dead = [k for k in own if digest(host.dials(**{k: (None if isinstance(host.SHIPPED[k], str) else (host.SHIPPED[k] * 2 if host.SHIPPED[k] else 1.0))})) == base]
print(f"  settings: {len(own)}; inert under perturbation over the battery: {dead or 'none'}")
