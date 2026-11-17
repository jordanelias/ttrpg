"""F14 the brute rule (stress lane A brute.py; A-144(6)). Grid: the judge's seat x his Grace; trial, one seat.
PREDICTION after: a mid judge of a mid seat is no brute; brute rises with the seat and falls with Grace; Grace 7 never;
the legitimacy a right ruling earns stays positive for an ordinary judge.  python -B f14_brute.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
m = mat()
H(f"F14 brute, and mean legitimacy / standing / compliance after one ruling (n={N} a cell)")
for lv in ("r2", "r3", "r4m", "r5M"):
    for g in (1, 2, 4, 5, 7):
        pp = {"a": F.P("a"), "b": F.P("b"), "j1": F.P("j1", office=office(lv, "Crown"), faction="Crown", grace=g)}
        L = S = C = 0.0; br = None
        for i in range(N):
            inp, card, out, b = sit(pp, "trial", m, ("br", i), bench=("j1",), effort=3)
            w = host.new_world(); host.fold(w, pp, inp, card, out, m)
            L += w["legitimacy"].get("Crown", 0.0); S += w["standing"].get("Crown", 0.0); C += w["compliance"].get("m", 1.0)
            br = host.reception(inp, [p for p in inp.room if p.id == "j1"][0])[0]
        print(f"  {lv:4} (power {host.power(pp['j1']):.0f}) Grace {g}: brute {br:.3f} legit {L/N:+.3f} standing {S/N:+.3f} compliance {C/N:.3f}", flush=True)
