"""Route checks: (1) Will in conversation/questioning with staying power, temper and awe removed: which route carries
it? b scripted to argue only (no press) vs rest only. (2) Presence with its dice share removed (k = all Reason) and
heard_step 0. (3) Focus discontinuity: drift at pull 0 vs a hair of pull."""
import sys, copy
from common import *
from dataclasses import replace
from sc2.engine import proceed
from sc2 import engine as E
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
CTL = lambda **o: host.MappingProxyType({**host.SHIPPED, **o})
WCTL = CTL(weary_step=0.0, temper_break=99.0, awe_step=0.0)
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
print("(1) a's Will 1 vs 7, staying power/temper/awe OFF")
for ctx in ("conversation", "questioning"):
    for lbl, dec in (("b argues only (no press)", {"b": forced("argue")}), ("b rests only", {"b": forced("rest")}), ("b auto", {})):
        r = {}
        for x in (1, 7):
            pp = blank(); pp["a"]["attributes"]["will"] = x
            r[x] = sum(sit(pp, ctx, mat("blank"), ("rw", ctx, lbl, i), deciders=dec, D=WCTL)[3][0] in CARRIED for i in range(n)) / n
        print(f"  {ctx:12} {lbl:26} W1 {r[1]:.3f} W7 {r[7]:.3f} {d(r[1], r[7])}")
print("(2) a's Presence 1 vs 7 with heard_step 0 AND Reason's dice share forced to 10/10")
for ctx in ("tell", "conversation", "rally", "trial"):
    r = {}
    for x in (1, 7):
        pp = blank(); pp["a"]["attributes"]["presence"] = x; c = 0
        rite, base = CTX[ctx]
        for i in range(n):
            inp, card = host.build(pp, rite, mat("blank") if ctx != "rally" else mat("blank"), D=CTL(heard_step=0.0), **base)
            inp = replace(inp, grounds=tuple((g, 2.0, e) for g, _, e in inp.grounds))
            out = proceed(inp, draw(("rp", ctx, i), "act", rite)); c += host.act_band(inp, out)[0] in CARRIED
        r[x] = c / n
    print(f"  {ctx:12} P1 {r[1]:.3f} P7 {r[7]:.3f} {d(r[1], r[7])}")
print("(3) Focus: tell with listener stake s (mood -> heat -> pull); mean drift and carried at Focus 1 / 7")
for s in (0.0, 0.01, 0.3, 0.9):
    row = []
    for x in (1, 7):
        pp = blank(); pp["b"]["layers"] = dict(pursuits={"tolls": s}) if s else {}; pp["a"]["attributes"]["focus"] = x
        dr = c = 0; pulls = 0.0
        for i in range(n):
            inp, card, out, b = sit(pp, "tell", F.matter(bears={"tolls": -1.0}), ("fd", s, i))
            c += b[0] in CARRIED; dr += out.beats[0].drift
            if i == 0:
                st0 = E._start(inp); a = inp.room[0]; pulls = E._pull(inp, st0, a, dict(st0.cond)["a"])
        row.append(f"F{x}: pull {pulls:.4f} drift {dr/n:.3f} carried {c/n:.3f}")
    print(f"  b's stake from pursuit {s}: " + " | ".join(row))
