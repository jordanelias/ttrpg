"""F13 equal kin to both parties (stress lane A det P5, g_kin). Trial, bench j1 (rung 4) with j2 (rung 3) as backup.
PREDICTION after: kin (or patron/client) to both parties is a conflict like kin to one: j1 steps down for j2, or,
alone, is recorded partial; patronage written on either man's record counts. Control: no tie.  python -B f13_kin.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
m = mat()
def pp_(lay, client_rec=None):
    pp = {"a": F.P("a"), "b": F.P("b"), "j1": F.P("j1", office=F.seat(4, "Crown"), faction="Crown", layers=copy.deepcopy(lay)),
          "j2": F.P("j2", office=F.seat(3, "Crown"), faction="Crown")}
    if client_rec:
        pp[client_rec[0]]["layers"] = dict(patron="j1")
    return pp
H("F13 j1's conflict by tie pattern; recusal with a backup, the ledger when alone")
for lab, lay, crec in (("none", {}, None), ("kin of a", dict(kin=("a",)), None), ("kin of a and b", dict(kin=("a", "b")), None),
                       ("client of a, patron of b", dict(patron="a", clients=("b",)), None), ("rel +1 a and +1 b", dict(relationships={"a": 1.0, "b": 1.0}), None),
                       ("patron of a, written on a's record only", {}, ("a",))):
    pp = pp_(lay, crec)
    st = host.bearing(pp["j1"], m, pp)
    c = host.conflict(pp["j1"], m, pp) if ARM == "after" else host.conflict(st)
    card2 = host.build(pp, "trial", m, bench=("j1", "j2"), effort=3)[1]
    part = 0
    for i in range(50):
        inp, card, out, b = sit(pp, "trial", m, ("k", i), bench=("j1",), effort=3)
        w = host.new_world(); host.fold(w, pp, inp, card, out, m); part += any(x[0] == "partial" for L in w["ledgers"].values() for x in L)
    k = sum(sit(pp, "trial", m, ("kp", i), bench=("j1",), effort=3)[3][0] in CARRIED for i in range(N))
    print(f"  {lab:40} tie a {host.tie(pp['j1'], 'a', pp):+.1f} b {host.tie(pp['j1'], 'b', pp):+.1f} conflict {c[0]:.3f} lean {c[1]:+.3f} | with backup: decided {card2.decided_by} recused {card2.recused} | alone: partial on a ledger {part}/50, P(for) {pc(k, N)}")
