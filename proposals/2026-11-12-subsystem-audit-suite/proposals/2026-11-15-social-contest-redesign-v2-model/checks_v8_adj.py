"""A-144: the adjudicator's five: validation, relevance filter, perception, intimidation, reception."""
import sys, copy, math
from types import SimpleNamespace
from collections import Counter
from sc2 import host, fixtures as F, engine as E
from sc2.lab import *
from sc2.engine import proceed, Item
from scmodel.rng import draw
from checks_v3_helpers import force, only
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
ground = lambda g: force(lambda o: o.move == "argue" and o.ground == g)
mp = F.mid_people()
L = dict(pursuits={"grain": 0.9}, convictions={"law": 4})
M = dict(id="m", parties={"for": "a", "against": "b"}, bears={"grain": 1.0, "law": 0.5})
D = host.dials(bias_step=0.0)
def base():
    pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(L); return pp
def sw(pp, attr, lv=(1, 7), who="j1", n=N, **kw):
    r = {}
    for x in lv:
        q = copy.deepcopy(pp); q[who]["attributes"][attr] = x; r[x] = rate(q, "trial", M, n, "adj", bench=("j1",), effort=3, **kw)
    d = r[lv[1]] - r[lv[0]]; return f"{r[lv[0]]:.3f} -> {r[lv[1]]:.3f} ({d:+.3f}, z {d / math.hypot(se(r[lv[0]], n), se(r[lv[1]], n)):+.1f})"
print("\n== A-144 A. the judge's REASON validates: `for` is plain but sound (Reason 7, Grace 2), `against` polished but unsound (Reason 1, Grace 7); both argue consequence; `for` carried")
pp = base(); pp["a"]["attributes"].update(reason=7, grace=2); pp["b"]["attributes"].update(reason=1, grace=7)
dec = {"a": ground("consequence"), "b": ground("consequence")}
print(f"  judge's Reason 1 -> 7: {sw(pp, 'reason', deciders=dec, D=D)} | control sense_step 0 (he cannot tell): {sw(pp, 'reason', deciders=dec, D=host.dials(bias_step=0.0, sense_step=0.0))}")
print("== B. the judge's FOCUS filters: the same merits (`for` argues), with and without noise (the other side only presses; `for` is Focus 1 in a famine)")
pq = base(); 
print(f"  no noise (the other side rests, peace): judge's Focus 1 -> 7: {sw(pq, 'focus', deciders={'a': only('argue'), 'b': only('rest')}, D=D)}")
pn = base(); pn["a"]["attributes"].update(will=2)
TH = host.dials(bias_step=0.0, off_step=0.0)
print(f"  B12 the theatre filter (restored): a rattle's room move by the judge's Focus (the other side presses a Will-2 `for`; his wandering not counted): {sw(pn, 'focus', deciders={'a': only('argue'), 'b': only('press')}, D=TH)}")
print(f"  B10 the judge's ATTUNEMENT reads a rattled man's discomfort for what it is (the same arm; `for` honest): {sw(pn, 'attunement', deciders={'a': only('argue'), 'b': only('press')}, D=TH)} | control comfort_step 0: {sw(pn, 'attunement', deciders={'a': only('argue'), 'b': only('press')}, D=host.dials(bias_step=0.0, off_step=0.0, comfort_step=0.0))}")
pnl = copy.deepcopy(pn); pnl["a"]["believes"] = {"m": -1.0}
print(f"  ... and a rattled LIAR's as guilt (`for` knows his case false; ploy deduction off to isolate it): {sw(pnl, 'attunement', deciders={'a': only('argue'), 'b': only('press')}, D=host.dials(bias_step=0.0, off_step=0.0, ploy_step=0.0))}")
pw = base(); pw["a"]["attributes"].update(focus=1)
print(f"  `for` wanders (Focus 1, famine): {sw(pw, 'focus', deciders={'a': only('argue'), 'b': only('rest')}, D=D, strife='famine')} | control off_step 0: {sw(pw, 'focus', deciders={'a': only('argue'), 'b': only('rest')}, D=host.dials(bias_step=0.0, off_step=0.0), strife='famine')}")
print("== C. the judge's ATTUNEMENT perceives the participant: `for` carried")
pl = base(); pl["a"]["believes"] = {"m": -1.0}; pl["a"]["rattled_ago"] = (0, 0)
ph = base()
psh = base(); psh["a"]["rattled_ago"] = (0, 0)
for lab, q in (("a strained liar (knows it false; carries two fresh rattles)", pl), ("a comfortable honest man", ph), ("B10 a strained HONEST man (two fresh rattles)", psh)):
    print(f"  {lab:58} judge's Attunement 1 -> 7: {sw(q, 'attunement', deciders={'a': only('argue'), 'b': only('rest')}, D=D)} | control ploy_step 0: {sw(q, 'attunement', deciders={'a': only('argue'), 'b': only('rest')}, D=host.dials(bias_step=0.0, ploy_step=0.0))}")
o = proceed(host.build(pl, "trial", M, bench=("j1",), effort=2)[0], draw(1, "a", "c"), rulings={"j1": lambda jv: (print(f"  a played judge of Attunement {jv and 4} is shown tells {jv.tells}") or None)})
print("== D. the judge's PRESENCE and STATION intimidate: the petitioner's carried at an audience; his View.awe")
for lab, wl, jp, off, DD in (("a Will-2 petitioner before a Presence-7 judge of rung 5", 2, 7, 5, D), ("a Will-7 peer (rung 5) before the same judge", 7, 7, 5, D), ("the Will-2 petitioner, the judge's Presence and office FLATTENED", 2, 4, None, D), ("the Will-2 petitioner, awe_step 0", 2, 7, 5, host.dials(bias_step=0.0, awe_step=0.0))):
    pp = base(); pp["a"]["attributes"]["will"] = wl; pp["j1"]["attributes"]["presence"] = jp
    pp["j1"]["office"] = F.seat(off, "Crown", "moderate") if off else None
    if off is None: pp["j1"]["office"] = F.seat(0, "Crown")
    if wl == 7: pp["a"]["office"] = F.seat(5, "Crown", "moderate")
    m = dict(M, parties={"for": "a"})
    inp, card = host.build(pp, "audience", m, bench=("j1",), effort=2, D=DD)
    v = E.build_view(inp, E._start(inp), inp.room[0], draw(0, "v", "a"), 2)
    print(f"  {lab:66} awe {v.awe:.2f}; audience carried {rate(pp, 'audience', m, N, 'awe', bench=('j1',), effort=2, D=DD, deciders={'a': ground('consequence')}):.3f}; in a trial where the other side presses him: rattles a sitting {sum(dict(sit(pp, 'trial', M, ('aw', i), bench=('j1',), effort=3, D=DD, deciders={'a': only('argue'), 'b': only('press')})[2].state.cond)['a'].rattles for i in range(N))/N:.2f}, carried {rate(pp, 'trial', M, N, 'aw', bench=('j1',), effort=3, D=DD, deciders={'a': only('argue'), 'b': only('press')}):.3f}")
pg = base(); pg["a"]["attributes"]["will"] = 2
for g in ("j2", "j3"): pg[g]["office"] = None
print(f"  the venue: the same Will-2 man before a gallery of commoner peers who decide (a rally): awe {E.build_view(host.build(pg, 'rally', dict(M, parties={'for': 'a'}), floor=('j2', 'j3'))[0], E._start(host.build(pg, 'rally', dict(M, parties={'for': 'a'}), floor=('j2', 'j3'))[0]), host.build(pg, 'rally', dict(M, parties={'for': 'a'}), floor=('j2', 'j3'))[0].room[0], draw(0, 'v', 'a'), 2).awe:.2f}")
print("== E. the judge's GRACE is how his verdict is RECEIVED: (accurate, wrong) x (gracious, brutish); a rung-5 judge; means over sittings")
def recep(grace, wrong, DD=D, played=True, n=N):
    pp = base(); pp["j1"]["attributes"]["grace"] = grace; pp["j1"]["office"] = F.seat(5, "Crown", "moderate"); pp["j2"]["office"] = F.seat(1, "Crown")
    acc = Counter(); k = 0
    for i in range(n):
        inp, card = host.build(pp, "trial", M, bench=("j1",), floor=("j2", "crowd"), effort=3, D=DD)
        rule = (lambda jv: ("against" if jv.track > 0 else "for")) if wrong else (lambda jv: ("for" if jv.track > 0 else "against"))
        out = proceed(inp, draw(("rc", i), "act", "trial"), rulings={"j1": rule} if played else None)
        w = host.new_world(); host.fold(w, pp, inp, card, out, M)
        if not w["reception"] or w["reception"][-1][2] != wrong: continue     # B5: wrong = against the merits as the record shows them
        k += 1
        acc["legitimacy"] += w["legitimacy"].get("Crown", 0.0); acc["compliance"] += w["compliance"].get("m", 0.0)
        acc["appeal"] += w["appeal_weight"].get("m", 0.0)
        acc["regard"] += w["regard"].get(("crowd", "j1"), 0.0); acc["standing"] += w["standing"].get("Crown", 0.0)
    k = max(1, k)
    return f"n={k}: legitimacy {acc['legitimacy']/k:+.2f}, compliance {acc['compliance']/k:.2f}, appeal weight {acc['appeal']/k:.2f}, the crowd's regard for him {acc['regard']/k:+.2f}, his faction's standing {acc['standing']/k:+.2f}"
for gl, g in (("gracious (Grace 7)", 7), ("brutish (Grace 1)", 1)):
    for wl, wr in (("accurate", False), ("wrong", True)):
        print(f"  {wl:8} x {gl:18} played judge: {recep(g, wr)}")
print(f"  accurate x brutish, a SIMULATED judge (his own draw): {recep(1, False, played=False)}")
print("  B5 how far station binds (A-144(6)): brute by the judge's Grace (rows) and station (power, columns):")
for g in (1, 4, 7):
    print("    Grace " + str(g) + ": " + "  ".join(f"power {pw}: brute {host.reception(SimpleNamespace(dials=host.dials()), SimpleNamespace(power=pw, grace=g))[0]:.2f}" for pw in (0, 3, 5, 7, 9)))
print(f"  control, Grace flattened to 4 (accurate): {recep(4, False)}; (wrong): {recep(4, True)}")

print("== the critic's rows: `for` chooser against the automatic other side; and a party who decides arguing against resting")
mpp = F.mid_people(); MM = F.matter()
for rite, kw, m in (("trial", dict(bench=BENCH), MM), ("debate", dict(bench=BENCH), MM), ("rally", dict(floor=("crowd",)), dict(id="m", parties={"for": "a"}, bears={}))):
    print(f"  {rite}: " + "; ".join(f"{k} {rate(mpp, rite, m, N * 2, 'crit', effort=3, deciders=({'a': d} if d else None), **kw):.3f}" for k, d in (("argue every turn", only("argue")), ("rest every turn", only("rest")), ("automatic", None))))
mv = Counter(x.move for i in range(200) for x in sit(mpp, "debate", MM, ("dm", i), bench=BENCH, effort=3)[2].beats)
print(f"  debate, all-mid, automatic: moves {dict(mv)}")
for lab, rite, who, kw, m in (("conversation: the man addressed", "conversation", "b", {}, MM), ("questioning: the questioned man", "questioning", "b", {}, MM), ("audience: the noble who is the other party", "audience", "j1", dict(bench=("j1",)), dict(MM, parties={"for": "a", "against": "j1"})), ("control: the accused in a trial (not a decider)", "trial", "b", dict(bench=BENCH), MM)):
    r = {k: rate(mpp, rite, m, N * 2, "pd", effort=3, deciders={who: d}, **kw) for k, d in (("argues", only("argue")), ("rests", only("rest")))}
    print(f"  {lab:46} `for` carried when he argues every turn {r['argues']:.3f}, rests {r['rests']:.3f} ({r['argues']-r['rests']:+.3f})")
for lab, sgn in (("the matter helps the listener", 1.0), ("the matter hurts him", -1.0)):
    r = {}
    for x in (1, 4, 7):
        pp = copy.deepcopy(mpp); pp["a"]["attributes"]["reason"] = x; pp["b"]["layers"] = dict(pursuits={"t": 0.9})
        r[x] = rate(pp, "conversation", dict(MM, bears={"t": sgn}), N * 2, "rs", form="abridged", deciders={"a": ground("consequence")})
    print(f"  relevance is magnitude, not sign: the tell on consequence, {lab}: Reason 1/4/7 = {r[1]:.3f}/{r[4]:.3f}/{r[7]:.3f}")
def refused(lab, fn):
    try: fn(); print(f"  NOT REFUSED: {lab}")
    except (ValueError, KeyError) as e: print(f"  refused: {lab}: {type(e).__name__}: {e}")
refused("one person as both parties", lambda: host.build(mpp, "trial", dict(MM, parties={"for": "a", "against": "a"}), bench=BENCH))
refused("an abridged act whose only decider is the speaker", lambda: host.build(mpp, "rally", dict(id="m", parties={"for": "a"}, bears={}), bench=("a",), floor=("crowd",), form="abridged"))
inp, card = host.build(mpp, "trial", MM, bench=BENCH, floor=("crowd",)); me = inp.room[0]
import statistics
for gl in (1, 4, 7):
    pp = copy.deepcopy(mpp); pp["b"]["attributes"]["grace"] = gl; pp["a"]["attributes"]["attunement"] = 2
    i2, _ = host.build(pp, "trial", MM, bench=BENCH); es = [E.build_view(i2, E._start(i2), i2.room[0], draw(k, "l", "e"), 3).esteem for k in range(300)]
    print(f"  leak: a poor reader's View.esteem against an opponent of Grace {gl}: mean {statistics.mean(es):+.2f}, s.d. {statistics.pstdev(es):.2f} (true {E.esteem(i2, E._start(i2), i2.room[0]):+.2f})")

print("== A-145 SILENCE: the same matter and persons (trial, all-mid); `for` carried when the accused ...")
for reg in ("crown", "theocracy", "commune"):
    row = []
    for lab, DD in (("shipped", host.dials()), ("silence rule off", host.dials(admit_step=0.0, contempt_step=0.0))):
        r = {k: rate(mpp, "trial", MM, N * 2, "sil", bench=BENCH, effort=3, regime=reg, D=DD, deciders=({"b": d} if d else None)) for k, d in (("rests every turn", only("rest")), ("argues every turn", only("argue")), ("automatic", None))}
        row.append(f"[{lab}] rests {r['rests every turn']:.3f}, argues {r['argues every turn']:.3f}, automatic {r['automatic']:.3f}")
    print(f"  {reg:9} (silence: {host.build(mpp, 'trial', MM, bench=BENCH, regime=reg)[1].silence}) " + " | ".join(row))
inp, card, out, b = sit(mpp, "trial", MM, ("sil", 0), bench=BENCH, effort=3, deciders={"b": only("rest")}); w = host.new_world(); host.fold(w, mpp, inp, card, out, MM)
print(f"  recorded: contumacy claims the judge holds {sum(1 for c_ in w['ledgers']['j1'] if c_[0] == 'contumacy')}; the judge's regard for the silent man {w['regard'].get(('j1', 'b'), 0):+.2f}")
print(f"  a rally (nothing to answer): rest costs tempo only: card.silence = {host.build(mpp, 'rally', dict(id='m', parties={'for': 'a'}, bears={}), floor=('crowd',))[1].silence}")
r = {k: rate(mpp, "questioning", MM, N * 2, "silq", effort=3, deciders={"b": d}) for k, d in (("silent", only("rest")), ("answers", only("argue")))}
print(f"  a party who decides and stays silent (the questioned man): the questioner gets it {r['silent']:.3f} when he is silent, {r['answers']:.3f} when he answers")

print("== A-146 a broken temper cannot hold its tongue: a debate; `for` puts a point, presses twice, then argues; the other man rests whenever he may")
def quiet(v, me): return (only("rest") if any(o.move == "rest" for o in v.options) else smart)(v, me)
def provoke(v, me): return (only("press") if 1 <= v.own.spoken <= 2 else only("argue"))(v, me)   # puts his point, then presses twice
for lab, wl, gr in (("ordinary (Will 4, Grace 4)", 4, 4), ("low (Will 2, Grace 2)", 2, 2), ("high (Will 7, Grace 7)", 7, 7)):
    pp = copy.deepcopy(mpp); pp["b"]["attributes"].update(will=wl, grace=gr); row = []
    for arm, DD in (("rule on", host.dials()), ("rule off", host.dials(temper_break=9.0))):
        car = brk = rst = nb = 0
        for i in range(N * 2):
            inp, card, out, b = sit(pp, "debate", MM, ("prov", i), bench=BENCH, effort=3, D=DD, deciders={"a": provoke, "b": quiet})
            car += b[0] in CARRIED
            for x in out.beats:
                if x.mover == "b": nb += 1; brk += x.broke; rst += x.move == "rest"
        row.append(f"[{arm}] provoker carried {car/(N*2):.3f}; his beats made with temper broken {brk/nb:.2f}; rested {rst/nb:.2f}")
    print(f"  the provoked man {lab:26} " + " | ".join(row) + f"   (2 s.e. of a difference {2*math.hypot(se(.3, N*2), se(.3, N*2)):.3f})")
