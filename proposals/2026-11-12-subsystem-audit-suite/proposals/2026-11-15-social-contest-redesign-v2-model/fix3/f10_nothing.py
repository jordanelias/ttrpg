"""F10 a rig with nothing to tilt (stress lane B probe_rig, probe_fold): conversation, questioning, negotiation.
PREDICTION after: tilt 0, nobody named, no price; a rite with seats or watchers still tilts (control: trial).
python -B f10_nothing.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
H(f"F10 a (r5M) arranges against b (r2) at rig 1; n={N}")
pp = castB(pa="r5M", pb="r2", seat_fac="Parliament")
for row in ("conversation", "questioning", "negotiation", "trial"):
    k = paid = 0
    for rig in (0.0, 1.0):
        k = paid = 0
        for i in range(N):
            inp, card, out, b = sit(pp, row, mat(), ("nt", row, i), bench=BENCH, arranger="a", rig=rig, effort=2)
            w = host.new_world(); host.fold(w, pp, inp, card, out, mat())
            k += b[0] in CARRIED; paid += w["legitimacy"].get("Parliament", 0.0) < 0 and card.tilt > 0
        if rig == 0.0:
            p0 = k / N
    print(f"  {row:12} card at rig 1: tilt {card.tilt} arranged_by {card.arranged_by} | P(for) rig 0 {p0:.3f} rig 1 {k/N:.3f} (2se {2*se(p0,N)*1.41:.3f}) | priced {paid}/{N}")
