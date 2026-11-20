from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
H(f"C the venue's formality and the `silence` cell on silence's cost: the accused rests every turn vs answers; `for` carried (n={N})")
for lab, rite, reg, kw in (("trial (formal 5, refusal)", "trial", "crown", dict(bench=BENCH)), ("arbitration (plain 4, refusal)", "arbitration", "crown", dict(bench=BENCH)),
                           ("trial under theocracy (6, admits)", "trial", "theocracy", dict(bench=BENCH)), ("trial under commune (4, free)", "trial", "commune", dict(bench=BENCH))):
    r = {k: carried(mp, rite, M, N, "frm", effort=3, regime=reg, deciders={"b": pol}, **kw) for k, pol in (("rest", only("rest")), ("answer", answer_else("rest")))}
    print(f"  {lab:36s} rests {r['rest']:.3f}  answers {r['answer']:.3f}  silence costs him {r['rest'] - r['answer']:+.3f}")
