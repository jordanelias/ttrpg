"""P7.2/4/6/7: calibration of the shown odds, leak probes, skill expression, mixed sittings, equivalence."""
from common import *
import statistics as S
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600

# in-memory wrapper (the M2 files are not edited): remember the (inp, st, mover, turns_left) each View was built from
_orig_bv = E.build_view
LAST = {}
def _bv(inp, st, mover, rng, turns_left):
    v = _orig_bv(inp, st, mover, rng, turns_left)
    LAST[mover.id] = (inp, st, mover, turns_left, v)
    return v
E.build_view = _bv
import sc2.engine as EE
EE.build_view = _bv


def true_menu(me_id):
    inp, st, mover, tl, v = LAST[me_id]
    frames = {o.ground: o.frame for o in v.options if o.move == "argue"}
    G = [g for g, _, _ in inp.grounds]
    fr = {g: frames.get(g) for g in G}
    out, T, P, Sx = E.menu(inp, st, mover, tl, fr)
    return {(m, g, it, rel): (ev, p) for m, g, it, rel, ev, p, f in out}


print(f"== P7.2 CALIBRATION of the shown chance on each option (a random chooser for `a`; b automatic; trial+debate+conversation; mid people, a's Attunement 1/4/7)")
for att in (1, 4, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att
    bins = defaultdict(lambda: [0, 0]); errs_ev = []; errs_p = []; tbins = defaultdict(lambda: [0, 0])
    rec = []
    def spy(v, me):
        o = random.Random(f"cal|{v.n}|{v.acc:.6f}").choice(v.options)
        tm = true_menu(me.id); tev, tp = tm[(o.move, o.ground, o.item, o.relation)]
        errs_ev.append(o.ev - tev)
        if o.p is not None: errs_p.append(o.p - tp)
        rec.append((o, tp))
        return Choice(o.move, o.ground, o.item, o.relation)
    n_ = 0
    for rite, kw in (("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("conversation", {})):
        for i in range(N):
            rec.clear()
            inp, card, out, b = sit(pp, rite, M, ("cal", att, rite, i), effort=3, deciders={"a": spy}, **kw)
            mine = [x for x in out.beats if x.mover == "a"]
            for (o, tp), x in zip(rec, mine):
                if o.p is None: continue
                hit = (x.margin >= 0) if o.move == "argue" else (x.rattled is not None)
                k = min(9, int(o.p * 10)); bins[k][0] += 1; bins[k][1] += hit; n_ += 1
                k2 = min(9, int(tp * 10)); tbins[k2][0] += 1; tbins[k2][1] += hit
    print(f"  Attunement {att}: shown ev - true ev mean {S.mean(errs_ev):+.3f} sd {S.pstdev(errs_ev):.3f}; shown p - true p mean {S.mean(errs_p):+.3f} sd {S.pstdev(errs_p):.3f}; options scored {n_}")
    print("     shown-p bin: " + " ".join(f"{k/10:.1f}:{v[1]/v[0]:.2f}(n{v[0]})" for k, v in sorted(bins.items()) if v[0] >= 20))
    print("     true-p  bin: " + " ".join(f"{k/10:.1f}:{v[1]/v[0]:.2f}(n{v[0]})" for k, v in sorted(tbins.items()) if v[0] >= 20))

print(f"\n== P7.2 the View's believed odds (last view of `a`) against the delivered verdict (trial, mid; a smart; b automatic), n={2*N}")
for att in (1, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att
    bins = defaultdict(lambda: [0, 0])
    for i in range(2 * N):
        inp, card, out, b = sit(pp, "trial", M, ("odds", att, i), bench=BENCH, effort=3, deciders={"a": smart})
        v = LAST["a"][4]; k = min(9, int(v.odds * 10)); bins[k][0] += 1; bins[k][1] += b[0] in CARRIED
    print(f"  Attunement {att}: " + " ".join(f"{k/10:.1f}:{v[1]/v[0]:.2f}(n{v[0]})" for k, v in sorted(bins.items()) if v[0] >= 15))

print(f"\n== P7.2 LEAK / BEAT-THE-MODEL probes (trial, mid), n={2*N}")
def oracle(v, me):
    tm = true_menu(me.id)
    o = max(v.options, key=lambda o: tm[(o.move, o.ground, o.item, o.relation)][0])
    return Choice(o.move, o.ground, o.item, o.relation)
def debias(v, me):
    adj = lambda o: o.ev - (1 - v.acc) * D["bias_step"] * me.bias * (1.0 if o.move in ("argue", "press") else 0.0)
    o = max(v.options, key=adj)
    return Choice(o.move, o.ground, o.item, o.relation)
for lab, att, bias in (("Att 2, unbiased", 2, 0.0), ("Att 2, pessimist (bias -1)", 2, -1.0), ("Att 2, optimist (bias +1)", 2, 1.0), ("Att 6, unbiased", 6, 0.0)):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att; pp["a"]["bias"] = bias
    r = {k: carried(pp, "trial", M, 2 * N, "leak", bench=BENCH, effort=3, deciders=({"a": d} if d else None))
         for k, d in (("random", rnd("lk")), ("auto", None), ("smart(view)", smart), ("debiased(view+own bias)", debias), ("oracle(true ev)", oracle))}
    print(f"  {lab:28} " + " ".join(f"{k} {v:.3f}" for k, v in r.items()))
pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = 1
for gl in (1, 7):
    p2 = copy.deepcopy(pp); p2["b"]["attributes"]["grace"] = gl
    es = []; ws = []
    for i in range(300):
        inp, card, out, b = sit(p2, "trial", M, ("lk2", gl, i), bench=BENCH, effort=3, deciders={"a": smart})
        v = LAST["a"][4]; es.append(v.esteem)
    inp, card = host.build(p2, "trial", M, bench=BENCH)
    print(f"  Attunement-1 viewer's View.esteem vs an opponent of Grace {gl}: mean {S.mean(es):+.2f} sd {S.pstdev(es):.2f} (true at start {E.esteem(inp, E._start(inp), inp.room[0]):+.2f})")

print(f"\n== P7.4 SKILL: `a` random vs automatic vs view-best vs answer-else-best, by rite and Attunement, b automatic, n={N}")
for rite, kw in (("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("questioning", {}), ("conversation", {}), ("negotiation", {}), ("audience", dict(bench=("j1",)))):
    for att in (1, 4, 7):
        pp = copy.deepcopy(mp); pp["a"]["attributes"]["attunement"] = att
        pred = (lambda inp, card, out, b: b[0] == "success") if rite == "negotiation" else None
        r = {}
        for k, d in (("random", rnd("sk")), ("auto", None), ("smart", smart), ("answer>best", answer_else_best)):
            r[k] = rate(pp, rite, M, N, "sk", pred=pred, effort=3, deciders=({"a": d} if d else None), **kw)
        print(f"  {rite:12} Att {att}: " + " ".join(f"{k} {v:.3f}" for k, v in r.items()))

print("\n== P7.6 temperament: two NPCs, different traits, same state -> different choices? (trial, `for` = each, first 3 beats' moves, 300 sittings)")
for lab, at, lay in (("flat", {}, {}), ("hot proud grudge", dict(will=6, grace=1), dict(relationships={"b": -0.9})), ("timid", dict(will=1, grace=2), {}), ("cool scholar", dict(reason=7, will=6, grace=6), dict(convictions={"c": 5}))):
    pp = copy.deepcopy(mp); pp["a"]["attributes"].update(**at); pp["a"]["layers"] = lay
    mv = Counter()
    for i in range(300):
        inp, card, out, b = sit(pp, "trial", M, ("t6", i), bench=BENCH, effort=3)
        mv.update(x.move for x in out.beats if x.mover == "a")
    t = sum(mv.values()); print(f"  {lab:18} " + " ".join(f"{k} {mv[k]/t:.2f}" for k in ("argue", "press", "concede", "rest")))

print("\n== P7.7 same rules both ways: a played seat whose callback IS the automatic policy reproduces the all-automatic sitting")
same = 0
for i in range(300):
    a1 = sit(mp, "trial", M, ("eq", i), bench=BENCH, effort=3)[2]
    a2 = sit(mp, "trial", M, ("eq", i), bench=BENCH, effort=3, deciders={"a": lambda v, me: auto(v, me, D), "b": lambda v, me: auto(v, me, D)})[2]
    same += a1 == a2
print(f"  identical outcomes {same}/300")
h = lambda o: hashlib.sha256(repr(o).encode()).hexdigest()[:12]
o1 = sit(F.cast(), "trial", F.TOLLS, ("det", 1), bench=CB, floor=("guildsmen", "toll_men", "clerk"), effort=3)[2]
o2 = sit(F.cast(), "trial", F.TOLLS, ("det", 1), bench=CB, floor=("guildsmen", "toll_men", "clerk"), effort=3)[2]
print(f"  determinism: same seed twice {h(o1)} {h(o2)}")
o = sit(mp, "trial", M, ("mix", 3), bench=BENCH, effort=3, deciders={"a": smart})
print(f"  a mixed sitting (a played by a view-only callback, b automatic, three drawn judges): ended {o[2].ended}, beats {len(o[2].beats)}, band {o[3][0]}")
o = proceed(host.build(mp, "trial", M, bench=BENCH, effort=3)[0], draw(9, "a", "j"), rulings={"j1": lambda jv: "for"})
print(f"  a played judge in the same sitting: verdicts {[(d, round(m.net - m.ob, 2)) for d, m in o.verdicts]}, departures returned {o.ruled}")
