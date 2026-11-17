"""F3 the rig's sympathy on a deciding seat (stress lane B probe_paired, common seeds).
PREDICTION after: the presiding seat starts at presume_step x tilt (1.97 at tilt 0.99), as the sympathy_step 0 arm
did before; the arranger's gain rig 0 -> 1 rises to the sympathy-0 arm's.  python -B f03_sympathy.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
H(f"F3 arranger a (r5M) vs b (r2), Parliament seats; paired seeds; n={N}")
for row in ("trial", "audience", "examination", "inquisition", "arbitration"):
    for arm, over in (("shipped", {}), ("sympathy0", dict(sympathy_step=0.0))):
        D = host.dials(**over); pp = castB(pa="r5M", pb="r2", seat_fac="Parliament"); ps = []; st = None
        for rig in (0.0, 1.0):
            k = 0
            for i in range(N):
                inp, card, out, b = sit(pp, row, mat(), ("pa", row, i), bench=BENCH + ("c1", "c2", "c3"), floor=("crowd", "o1"), arranger="a", rig=rig, effort=2, D=D)
                k += b[0] in CARRIED
            ps.append(k / N); st = {p.id: round(p.start, 2) for p in inp.room if p.decides}
        print(f"  {row:12} {arm:9} rig0 {ps[0]:.3f} rig1 {ps[1]:.3f} gain {ps[1]-ps[0]:+.3f} (2se {2*math.hypot(se(ps[0],N),se(ps[1],N)):.3f}); seats' start at rig 1 {st}", flush=True)
