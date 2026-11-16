from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
OFF = host.dials(admit_step=0.0, contempt_step=0.0)
POL = (("rest", only("rest")), ("argue(best)", only("argue")), ("answer-only", answer_only),
       ("answer-else-best", answer_else_best), ("press", only("press")), ("auto", None))

print("== reproduce N p3:48/121 (seed 'sil', n=600, crown): accused b; `for` carried")
for lab, DD in (("shipped", D), ("rule off", OFF)):
    r = {k: carried(mp, "trial", M, 600, "sil", bench=BENCH, effort=3, D=DD, deciders=({"b": d} if d else None))
         for k, d in (("rest", only("rest")), ("argue", only("argue")), ("auto", None))}
    print(f"  [{lab}] " + ", ".join(f"{k} {v:.3f}" for k, v in r.items()))

print(f"\n== P4.1-3 CHARGED side (accused b, `against`), fresh seed, n={N}; lower `for` carried = better for him")
for venue, rite, kw in (("trial FORMAL(5)", "trial", dict(bench=BENCH)), ("arbitration PLAIN(4)", "arbitration", dict(bench=BENCH)),
                        ("inquisition SOLEMN(6)", "inquisition", dict(bench=("c1", "c2"))),
                        ("interrogation PLAIN(4)", "interrogation", dict(bench=BENCH))):
    for reg in ("crown", "theocracy", "commune"):
        try:
            inp, card = host.build(mp, rite, M, regime=reg, effort=3, **kw)
        except ValueError as e:
            print(f"  {venue:22} {reg:9} refused: {e}"); continue
        row = []
        for DD, tag in ((D, ""), (OFF, "off:")):
            for lab, d in POL if tag == "" else (("rest", only("rest")), ("auto", None)):
                p = carried(mp, rite, M, N, "p4c", regime=reg, effort=3, D=DD, deciders=({"b": d} if d else None), **kw)
                row.append(f"{tag}{lab} {p:.3f}")
        print(f"  {venue:22} {reg:9} silence={card.silence:8} std={card.standard} | " + " ".join(row))

print(f"\n== P4 UNCHARGED / bearer side (accuser a, `for`), other side automatic, n={N}; higher = better for him")
for venue, rite, kw in (("trial", "trial", dict(bench=BENCH)), ("debate", "debate", dict(bench=BENCH)),
                        ("questioning(bearer asks)", "questioning", {}), ("conversation", "conversation", {})):
    row = []
    for lab, d in POL:
        p = carried(mp, rite, M, N, "p4u", effort=3, deciders=({"a": d} if d else None), **kw)
        row.append(f"{lab} {p:.3f}")
    inp, card = host.build(mp, rite, M, effort=3, **kw)
    print(f"  {venue:26} silence={card.silence:8} odds(unmoved)={card.odds} | " + " ".join(row))

print(f"\n== mean track move per draw-move between FLAT people (trial, both automatic vs both argue), n={N}")
for lab, dec in (("both argue(best)", {"a": only("argue"), "b": only("argue")}), ("auto", None)):
    mv = defaultdict(list)
    for i in range(N):
        inp, card, out, b = sit(mp, "trial", M, ("mv", i), bench=BENCH, effort=3, deciders=dec)
        for x in out.beats:
            d = sum(dd for q, dd in x.moved if q == "j1") * (1 if x.side == "for" else -1)
            mv[(x.move, x.relation, x.evaded)].append(d)
    print(f"  [{lab}] " + "; ".join(f"{k}: n={len(v)} mean toward speaker {sum(v)/len(v):+.2f}" for k, v in sorted(mv.items())))

print(f"\n== PARTY-DECIDER silence (questioning: the questioned man b decides; conversation: b addressed decides), n={N}")
for rite, kw in (("questioning", {}), ("conversation", {})):
    inp, card = host.build(mp, rite, M, effort=3, **kw)
    row = []
    for DD, tag in ((D, ""), (OFF, "off:")):
        for lab, d in (("rest", only("rest")), ("argue", only("argue")), ("concede", only("concede")), ("auto", None)):
            p = carried(mp, rite, M, N, "p4d", effort=3, D=DD, deciders=({"b": d} if d else None), **kw)
            row.append(f"{tag}{lab} {p:.3f}")
    print(f"  {rite:12} silence={card.silence} decided_by={card.decided_by} | " + " ".join(row))

print("\n== the fold: contumacy and regard after a silent sitting (trial crown, accused rests; and commune)")
for reg in ("crown", "commune"):
    cont = reg_ = 0.0; n = 200
    for i in range(n):
        inp, card, out, b = sit(mp, "trial", M, ("fold", i), bench=BENCH, effort=3, regime=reg, deciders={"b": only("rest")})
        w = host.new_world(); host.fold(w, mp, inp, card, out, M)
        cont += sum(1 for c in w["ledgers"]["j1"] if c[0] == "contumacy"); reg_ += w["regard"].get(("j1", "b"), 0.0)
    print(f"  {reg}: contumacy claims in the judge's ledger per sitting {cont/n:.2f}; judge's regard for the silent man {reg_/n:+.3f}")
