"""F19 a judge who holds by the law is not partial (audit of 2,400 transcripts). Trial and audience, one seat j1 with
a backup j2 for recusal; the matter bears law 0.5 and tolls -1. Judges: none; a conviction (law 4); a pursuit in the
matter (tolls 0.8); kin of the accuser. PREDICTION after: the conviction-only judge is never recused, recorded or
priced; the pursuit and kin judges still are.  python -B f19_partial.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
m = mat(bears={"law": 0.5, "tolls": -1.0})
H(f"F19 partiality by what the judge carries (n={N})")
for lab, lay in (("nothing", {}), ("a conviction: law 4", dict(convictions={"law": 4})), ("a pursuit: tolls 0.8", dict(pursuits={"tolls": 0.8})), ("kin of the accuser", dict(kin=("a",)))):
    for rite in ("trial", "audience"):
        pp = {"a": F.P("a"), "b": F.P("b"), "j1": F.P("j1", office=F.seat(4, "Crown"), faction="Crown", layers=copy.deepcopy(lay)), "j2": F.P("j2", office=F.seat(3, "Crown"), faction="Crown")}
        rec = host.build(pp, rite, m, bench=("j1", "j2"), effort=3)[1].recused
        led = paid = 0
        for i in range(N):
            inp, card, out, b = sit(pp, rite, m, ("pt", rite, i), bench=("j1",), effort=3)
            w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, m)
            led += any(x[0] == "partial" and x[1] == "j1" for L in w["ledgers"].values() for x in L); paid += any(x[0] == "partial_paid" for x in wr)
        print(f"  {lab:22} {rite:8}: with a backup, recused {rec or '-'} | alone: on a ledger {led/N:.2f}, priced {paid/N:.2f}")
