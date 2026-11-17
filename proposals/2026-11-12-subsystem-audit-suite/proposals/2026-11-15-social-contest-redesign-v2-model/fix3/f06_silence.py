"""F6 silence under a commune (stress lane B probe_silence; A-145). Rows whose reply is `must`, all-mid, rig 0.
PREDICTION after: under a commune the cell is `refusal` (never free where an answer is owed) and its cost lower
than a crown's by the commune's standard; the accused who always rests carries more risk than an arguing one.
Control: the same Input with the cell forced to `refusal` at the crown's cost.  python -B f06_silence.py N"""
import dataclasses
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
H(f"F6 P(for carries), n={N}; seeds as lane B")
for row in ("trial", "tribunal", "arbitration", "questioning"):
    for rg in ("crown", "commune"):
        pp = castB()
        inp0, card = host.build(pp, row, mat(), bench=BENCH, floor=("crowd", "o1"), regime=rg, effort=2)
        line = []
        for pol, dec in (("auto", {}), ("b rests", {"b": only("rest")}), ("all rest", {"a": only("rest"), "b": only("rest")})):
            k = 0
            for i in range(N):
                out = proceed(inp0, draw(("si", row, rg, pol, i), "act", row), None, dec)
                k += host.act_band(inp0, out)[0] in CARRIED
            line.append(f"{pol} {k/N:.3f}")
        print(f"  {row:12} {rg:8} cell `{inp0.rite.silence}` | " + " | ".join(line) + f"  (2se~{2*se(0.3,N):.3f}) | card: {card.silence[:70]}", flush=True)
