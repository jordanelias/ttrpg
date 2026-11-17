"""F9 packing against the quorum (stress lane B probe_rig2; lane A det P8: one seat running a quorum-2 debate).
PREDICTION after: a packed declared bench keeps at least its quorum; the rig moves P(the arranger's side) toward the
arranger whichever side arranges (before: the direction was set by the bench's size, not the arranger); a bench
offered fewer seats than its quorum is refused `short_bench`.  python -B f09_quorum.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
H(f"F9 arranger r5M vs r2, Parliament parties; P(for), n={N}")
for row in ("tribunal", "debate"):
    for who in ("a", "b"):
        pp = castB(pa="r5M", pb="r2", seat_fac="Parliament") if who == "a" else castB(pa="r2", pb="r5M", seat_fac="Parliament")
        line = []
        for rig in (0.0, 0.5, 1.0):
            inp, card = host.build(pp, row, mat(), bench=BENCH, arranger=who, rig=rig, effort=2)
            k = sum(sit(pp, row, mat(), ("q", row, who, rig, i), bench=BENCH, arranger=who, rig=rig, effort=2)[3][0] in CARRIED for i in range(N))
            line.append(f"rig {rig}: seats {len(card.decided_by)} quorum {inp.rite.quorum} P(for) {pc(k, N)}")
        print(f"  {row:8} arranger {who}: " + " | ".join(line), flush=True)
mp, M = F.mid_people(), F.matter()
for row in ("debate", "tribunal"):
    print(f"  {row} offered one seat:", attempt(lambda: host.build(mp, row, M, bench=("j1",))[1].decided_by))
