"""B, C, E and F items of the second fix pass not covered by the core batteries."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cast, T = F.cast(), F.TOLLS
ral = dict(id="m", parties={"for": "a"}, bears={})

H("B1 a matter with no accused / no opposition, and the refusals (each keyed)")
for rite, kw in (("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("audience", dict(bench=BENCH))):
    inp, card, out, b = sit(mp, rite, ral, ("os", 0), effort=3, **kw)
    print(f"  {rite} with nobody against: ran; ended {out.ended}, band {b[0]}, beats {[(x.move, x.relation) for x in out.beats]}; carried over {N} {carried(mp, rite, ral, N, 'os', effort=3, **kw):.3f}")
pp = copy.deepcopy(mp); pp["foe"] = F.P("foe", layers=dict(pursuits={"x": 0.8})); m1 = dict(ral, bears={"x": -1.0})
inp, card = host.build(pp, "trial", m1, bench=BENCH, floor=("crowd", "foe"), effort=3)
print(f"  D4 who comes to oppose: with a man on the floor whom the charge would cost, the room is {card.room}")
for lab, fn in (("one character", lambda: E.Input(inp.rite, "m", inp.room[:1], inp.grounds, D)),
                ("one person as both parties", lambda: host.build(mp, "trial", dict(M, parties={"for": "a", "against": "a"}), bench=BENCH)),
                ("an abridged act whose only decider is the speaker", lambda: host.build(mp, "rally", ral, bench=("a",), floor=("crowd",), form="abridged")),
                ("a cohort of weight 0", lambda: host.build(dict(mp, crowd=dict(mp["crowd"], weight=0)), "rally", ral, floor=("crowd",))),
                ("an unlawful rite", lambda: host.build(mp, "debate", M, bench=BENCH, regime="theocracy")),
                ("a bench rite with no seat of its authority", lambda: host.build(mp, "inquisition", M, bench=BENCH))):
    try: fn(); print(f"  NOT REFUSED: {lab}")
    except ValueError as e: print(f"  refused: {lab}: {e}")
inp, card = host.build(mp, "trial", M, form="abridged")
print(f"  an abridged trial needs no bench: close {card.close}, decided by {card.decided_by}")

H(f"B2 the lie's record: `hypocrite` claims written by a hearer of Attunement 2 / 4 / 7, and whether the lie carried (the tell, n={N})")
for att in (2, 4, 7):
    pp = copy.deepcopy(mp); pp["a"]["believes"] = {"m": -1.0}; pp["b"]["attributes"]["attunement"] = att
    car = hyp = hyp_car = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "conversation", M, ("lie", i), form="abridged")
        w = host.new_world(); host.fold(w, pp, inp, card, out, M)
        h = sum(1 for e in w["ledgers"].get("b", []) if e[0] == "hypocrite")
        c = b[0] in CARRIED; car += c; hyp += h > 0; hyp_car += (h > 0) and c
    print(f"  Attunement {att}: carried {car/N:.3f}; a `hypocrite` claim in {hyp/N:.3f} of tells; claims written where the lie still carried {hyp_car}")
pp = copy.deepcopy(mp); pp["a"]["layers"] = dict(pursuits={"x": 0.9})
inp, card = host.build(pp, "trial", dict(M, bears={"x": -1.0}), bench=BENCH)
a = inp.room[0]
print(f"  insincerity of arguing FOR a matter that costs him, believing it: consequence {E.insincerity(a, 'for', 'consequence', None):.2f}, authority {E.insincerity(a, 'for', 'authority', None):.2f} (was 0.90)")
pp = copy.deepcopy(mp); pp["a"]["believes"] = {"m": -0.8}
inp, card = host.build(pp, "trial", M, bench=BENCH)
print(f"  where a false item comes from: a man who knows the charge false holds {[(it.id, it.kind, it.sincere) for it in inp.room[0].items]}; an honest man {[it.id for it in host.build(mp, 'trial', M, bench=BENCH)[0].room[0].items]}")

H(f"B3 a ruling is received; a tell or a rally is not; nothing is minted from nothing (n={N})")
c = Counter()
for i in range(N):
    mr = dict(T, parties={"for": "orator"})
    inp, card, out, b = sit(cast, "rally", mr, ("rl", i), floor=("guildsmen", "toll_men", "townsfolk"), effort=3)
    w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, mr)
    c["failed"] += band == "failure"
    c["grievance"] += any(x[0] == "grievance" for x in wr); c["legitimacy"] += bool(w["legitimacy"]); c["reception"] += bool(w["reception"])
    c["regard 'how he ruled'"] += any(x[0].startswith("regard") and x[-1] == "how he ruled" for x in wr)
    c["famine created"] += "famine" in w["strife"]
print(f"  rallies: {dict(c)}")
c = Counter()
for i in range(N):
    inp, card, out, b = sit(mp, "conversation", M, ("tl", i), form="abridged", floor=("crowd",))
    w = host.new_world(); band, wr = host.fold(w, mp, inp, card, out, M)
    c["reception"] += bool(w["reception"]); c["legitimacy"] += bool(w["legitimacy"])
print(f"  tells: {dict(c)}")
w = host.new_world(); w["strife"]["famine"] = 1.0; moved = Counter()
for i in range(N // 4):
    inp, card, out, b = sit(cast, "debate", dict(T, id="remit"), ("fm", i), bench=CB, floor=("guildsmen",), effort=3)
    before = w["strife"]["famine"]; band, _ = host.fold(w, cast, inp, card, out, dict(T, id="remit")); moved[(band, round(w["strife"]["famine"] - before, 2))] += 1
print(f"  a famine moves only by what a sitting resolved (decree carried eases it; nothing raises it): {dict(moved)}; at the end {w['strife']['famine']:.2f}")

H(f"B4 questioning: what each band leaves in the world (the cast; n={N})")
ws = defaultdict(Counter)
for i in range(N):
    m = dict(T, id="who", parties={"for": "fox", "against": "bully"})
    inp, card, out, b = sit(cast, "questioning", m, ("q4", i), effort=3)
    w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, m)
    ws[band][tuple(sorted({x[0] for x in wr if x[0] not in ("case_file:stage", "strain_carried")}))] += 1
for band, cc in ws.items():
    print(f"  {band}: {dict(cc.most_common(2))}")

H("B6 a conflicted seat: recusal, a conflict that nets to zero, and the price of ruling his own way")
pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(pursuits={"x": 0.5}, clients=("b",))
m6 = dict(M, bears={"x": 1.0})
st6 = host.bearing(pp["j1"], m6, pp)
print(f"  j1's stake {tuple(round(x, 2) for x in st6)} -> conflict, lean {tuple(round(x, 2) for x in host.conflict(pp["j1"], m6, pp))} (opposite interests do not cancel)")
inp, card = host.build(pp, "trial", m6, bench=BENCH, effort=3)
print(f"  with other seats of the authority: recused {card.recused}, decided by {card.decided_by}")
inp, card = host.build(pp, "trial", m6, bench=("j1",), effort=3)
print(f"  alone on the bench: recused {card.recused}, decided by {card.decided_by}: he sits, and the room holds a `partial` claim")
pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(pursuits={"x": 0.9})
paid = Counter()
for i in range(N):
    inp, card, out, b = sit(pp, "trial", m6, ("b6", i), bench=("j1",), effort=3)
    w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, m6)
    paid[(band in CARRIED, any(x[0] == "partial_paid" for x in wr))] += 1
print(f"  a seat who wants the charge to carry (lean +): (carried, paid) {dict(paid)}")

H(f"B11 the NPC liar reads the judge as he believes him: share of the liar's beats that argue, before a judge of Attunement 1 / 7 (n={N})")
for la in (2, 4, 7):
    row = []
    for ja in (1, 7):
        pp = copy.deepcopy(mp); pp["a"]["believes"] = {"m": -1.0}; pp["a"]["attributes"]["attunement"] = la; pp["j1"]["attributes"]["attunement"] = ja
        mv = Counter(x.move for i in range(N // 2) for x in sit(pp, "trial", M, ("b11", i), bench=("j1",), effort=3)[2].beats if x.mover == "a")
        row.append(f"judge {ja}: argue {mv['argue']/max(1, sum(mv.values())):.2f}")
    print(f"  liar of Attunement {la}: " + "; ".join(row))

H("B14 Focus: drift continuous in the pull; its slope where distraction is the ordinary state")
print(f"  drift at pull 0 / 0.0001 / 0.5 with a hold of -1.0: {E.drift_of(0.0, -1.0):.4f} / {E.drift_of(0.0001, -1.0):.4f} / {E.drift_of(0.5, -1.0):.4f}")
def fsw(pp, rite, m, lab, n=N * 2, **kw):
    r = {}
    for x in (1, 7):
        q = copy.deepcopy(pp); q["a"]["attributes"]["focus"] = x; r[x] = carried(q, rite, m, n, "b14", **kw)
    print(f"  {lab:58s} Focus 1 -> 7: {r[1]:.3f} -> {r[7]:.3f} ({r[7]-r[1]:+.3f}, z {z(r[7], r[1], n):+.1f})")
fsw(mp, "trial", M, "a quiet trial (no pull)", bench=BENCH, effort=3, deciders={"a": only("argue")})
fsw(mp, "trial", M, "a trial in famine (unrest 0.75)", bench=BENCH, effort=3, strife="famine", deciders={"a": only("argue")})
fsw(mp, "trial", M, "a pressed man: the other side presses every turn", bench=BENCH, effort=3, deciders={"a": only("argue"), "b": only("press")})
hp = copy.deepcopy(mp); hp["crowd"]["layers"] = dict(relationships={"a": -0.8}); hp["crowd"]["attributes"]["attunement"] = 4
fsw(hp, "rally", ral, "a rally before a hostile crowd (heckled)", floor=("crowd",), effort=3)
fsw(mp, "trial", M, "a pressed man in a famine", bench=BENCH, effort=3, strife="famine", deciders={"a": only("argue"), "b": only("press")})

H("B15 / B16 Will at the rally and the tell; Attunement where listeners hold nothing; Grace above the occasion's standard")
for lab, rite, m, kw in (("the tell", "conversation", M, dict(form="abridged")), ("the rally", "rally", ral, dict(floor=("crowd",), effort=3))):
    r = {x: carried(dict(mp, a=dict(mp["a"], attributes=dict(mp["a"]["attributes"], will=x))), rite, m, N * 2, "b15", **kw) for x in (1, 7)}
    print(f"  Will 1 -> 7, {lab}: {r[1]:.3f} -> {r[7]:.3f}")
for lab, kw in (("a quiet tell (plain venue)", dict(form="abridged")), ("pressed every turn (conversation, plain)", dict(effort=3, deciders={"b": only("press"), "a": only("argue")}))):
    r = {x: carried(dict(mp, a=dict(mp["a"], attributes=dict(mp["a"]["attributes"], grace=x))), "conversation", M, N * 2, "b16", **kw) for x in (4, 5, 6, 7)}
    print(f"  Grace 4/5/6/7, {lab}: " + " / ".join(f"{r[x]:.3f}" for x in (4, 5, 6, 7)))

H("B19 one word, one thing; C the context acting on PLAY (choices), not only on who wins")
for k in ("interrogation", "examination", "tribunal", "inquisition_hearing"):
    rid, over = host.ALIASES[k]; print(f"  `{k}` is the {rid} structure {over or ''}")
inp, card = host.build(mp, "tribunal", M, bench=BENCH, effort=3)
print(f"  a tribunal is decided by {card.decided_by} ({card.close}, quorum {inp.rite.quorum})")
def shares(**kw):
    g = Counter(); mv = Counter()
    for i in range(N // 2):
        inp, card, out, b = sit(cast, "trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), ("ctx", i), bench=CB, floor=FL, effort=3, **kw)
        for x in out.beats:
            mv[x.move] += 1
            if x.move == "argue": g[x.ground] += 1
    t, tm = sum(g.values()), sum(mv.values())
    return "grounds " + " ".join(f"{k[:5]} {g[k]/t:.2f}" for k in ("evidence", "consequence", "authority", "solidarity")) + " | rest " + f"{mv['rest']/tm:.2f}"
for lab, kw in (("plain era", {}), ("age of faith", dict(era="age_of_faith")), ("mercantile", dict(era="mercantile")),
                ("crown", {}), ("theocracy", dict(regime="theocracy")), ("commune", dict(regime="commune"))):
    print(f"  {lab:14s} {shares(**kw)}")
ep = copy.deepcopy(mp); ep["b"]["layers"] = dict(pursuits={"p": 0.8}, convictions={"c": 4})
em = dict(M, bears={"p": 1.0, "c": 1.0})
for lab, era in (("plain", "plain"), ("age of faith", "age_of_faith"), ("mercantile", "mercantile")):
    g = Counter(x.ground for i in range(N // 2) for x in sit(ep, "conversation", em, ("era", i), effort=3, era=era)[2].beats if x.mover == "a" and x.move == "argue")
    t = sum(g.values()) or 1
    print(f"  C era on PLAY: a listener who wants and holds alike; the speaker's grounds in a {lab:12s} era: consequence {g['consequence']/t:.2f}, authority {g['authority']/t:.2f}")
pp = copy.deepcopy(mp)
for j in BENCH: pp[j]["faction"] = "Crown"
pp["a"]["faction"] = "Crown"
r = {lab: carried(pp if lab == "partisan" else mp, "trial", M, N * 2, "fac", bench=BENCH, effort=3) for lab in ("partisan", "no faction")}
print(f"  faction: the accuser shares the bench's faction {r['partisan']:.3f}; nobody's faction {r['no faction']:.3f} ({r['partisan']-r['no faction']:+.3f})")

H(f"N's strife figure, re-measured in N's own setup (the toll trial, the cast; n={N * 2})")
for lab, kw in (("crown/peace", {}), ("war", dict(strife="war")), ("famine", dict(strife="famine"))):
    print(f"  {lab:12s} {carried(cast, 'trial', T, N * 2, 'nN', bench=CB, floor=FL, effort=3, **kw):.3f}")

H("B21 a bystander at a tell: what he learns (a claim of what he heard), never a ruling")
inp, card, out, b = sit(mp, "trial", M, ("by", 0), form="abridged", floor=("crowd",))
w = host.new_world(); host.fold(w, mp, inp, card, out, M)
print(f"  a word in an open court (the abridged trial): room {card.room}; the crowd's ledger {w['ledgers'].get('crowd')}; its regard writes {[(k, round(v, 3)) for k, v in w['regard'].items() if k[0] == 'crowd']}; reception {w['reception']} (none: no ruling)")

H("E / F the draw count, determinism, the mirror")
print(f"  draws per exchange at G = 4 grounds: {E.DRAWS_PER_EXCHANGE(4)} (6G + 11, asserted in every exchange); one per drawn decider")
hs = set(); same = True
for i in range(50):
    o1 = sit(cast, "trial", T, ("det", i), bench=CB, floor=FL, effort=3)[2]; o2 = sit(cast, "trial", T, ("det", i), bench=CB, floor=FL, effort=3)[2]
    h1 = hashlib.sha256(repr((o1.beats, o1.verdicts, o1.state)).encode()).hexdigest(); same &= h1 == hashlib.sha256(repr((o2.beats, o2.verdicts, o2.state)).encode()).hexdigest(); hs.add(h1)
print(f"  50 seeds: {len(hs)} distinct hashes; the same seed twice gives the same hash: {same}")
sw_ = {}
for lab, a_side in (("a for", "for"), ("a against", "against")):
    pp = copy.deepcopy(mp)
    for k_ in host.ATTRS: pp["a"]["attributes"][k_] = 5; pp["b"]["attributes"][k_] = 3
    m_ = M if a_side == "for" else dict(M, parties={"for": "b", "against": "a"})
    p_ = carried(pp, "debate", m_, N * 2, "swap", bench=BENCH, effort=3)
    sw_[a_side] = p_ if a_side == "for" else 1 - p_
eq = carried(mp, "debate", M, N * 2, "swap", bench=BENCH, effort=3)
print(f"  the swap (debate, a all-5 against b all-3): a carries {sw_['for']:.3f} as the bearer and {sw_['against']:.3f} as the other side; gap {sw_['for'] - sw_['against']:+.3f} against the equals' bearer edge {2 * eq - 1:+.3f} (n={N * 2})")
for attr in ("reason", "presence", "grace", "will"):
    r = {}
    for ax, bx in ((7, 1), (1, 7)):
        pp = copy.deepcopy(mp); pp["a"]["attributes"][attr] = ax; pp["b"]["attributes"][attr] = bx
        r[(ax, bx)] = carried(pp, "conversation", M, N, "mir", effort=3)
    pq = copy.deepcopy(mp)
    for ax, bx in ((7, 1),):
        pq["a"]["attributes"][attr] = bx; pq["b"]["attributes"][attr] = ax
    print(f"  mirror ({attr}, conversation): a7 b1 {r[(7, 1)]:.3f}, a1 b7 {r[(1, 7)]:.3f}; the swing {r[(7, 1)] - r[(1, 7)]:+.3f}")

H(f"F no absurd all-1 side, no mandatory attribute (trial, all-mid opponent, automatic; n={N})")
for lab, lv in (("all 1 against all 4", 1), ("all 7 against all 4", 7)):
    pp = copy.deepcopy(mp)
    for k_ in host.ATTRS: pp["a"]["attributes"][k_] = lv
    print(f"  {lab}: `for` carried {carried(pp, 'trial', M, N, 'abs', bench=BENCH, effort=3):.3f} (equals {carried(mp, 'trial', M, N, 'abs', bench=BENCH, effort=3):.3f})")
row = []
for k_ in host.ATTRS:
    pp = copy.deepcopy(mp); pp["a"]["attributes"][k_] = 1
    row.append(f"{k_} 1: {carried(pp, 'trial', M, N, 'mand', bench=BENCH, effort=3):.3f}")
print("  one attribute at 1, the rest 4: " + "; ".join(row))
