"""ADJ GRACE: reception of a played presiding judge's verdict. accurate = rules the way his own track leans;
wrong = against it. Fold into a fresh world per sitting. Rung-5 Crown judge (moderate) and a rung-0 judge."""
import sys
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 300
m = mat("blank")
def ruling(kind):
    def f(jv):
        lean = "for" if jv.track > 0 else "against"
        return lean if kind == "accurate" else ("against" if lean == "for" else "for")
    return f
for rung, mod in ((5, "moderate"), (0, None)):
    print(f"judge rung {rung} {mod or ''}")
    for g in (1, 4, 7):
        for kind in ("accurate", "wrong"):
            L = C = A = R = 0.0; k = 0; wrongflag = 0; skipped = 0
            for i in range(n):
                pp = blank(); pp["j1"]["attributes"]["grace"] = g; pp["j1"]["office"] = F.seat(rung, "Crown", mod)
                inp, card, out, b = sit(pp, "trial", m, ("gr", i), rulings={"j1": ruling(kind)})
                tr = dict(out.state.tracks)["j1"]
                if abs(tr) <= 1.0:
                    skipped += 1; continue
                w = host.new_world(); host.fold(w, pp, inp, card, out, m)
                rec = w.get("reception", [])
                if not rec: continue
                k += 1; L += w["legitimacy"].get("Crown", 0.0); C += w["compliance"][-1]; A += w.get("appeal_weight", 0.0)
                R += sum(v for (x, y), v in w["regard"].items() if y == "j1") / max(1, sum(1 for (x, y) in w["regard"] if y == "j1"))
                wrongflag += rec[-1][2]
            print(f"  Grace {g} {kind:8}: n={k:3} (|track|<=1 skipped {skipped})  legitimacy {L/k:+.2f}  compliance {C/k:.2f}  appeal {A/k:.2f}  regard-for-judge {R/k:+.3f}  flagged-wrong {wrongflag/k:.2f}")
