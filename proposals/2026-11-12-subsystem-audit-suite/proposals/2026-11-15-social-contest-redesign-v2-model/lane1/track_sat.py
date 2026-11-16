"""Track clamp: share of first exchanges whose clipped margin alone fills the track (|track| = track_clip after one
speech), all-mid shipped, and the RD dial set's decider Focus (strike_level minor) under the bench-pool control.
usage: PYTHONHASHSEED=0 python lane1/track_sat.py [n]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people, sweep
from scmodel import dials, host
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
for dn, D in (("shipped", dials.shipped()), ("controls", dials.controls())):
    for scen in ("private_full", "bench_full", "crowd_full"):
        full = 0; m = []
        for i in range(N):
            inp, out, band = sitting(scen, base_people(), D, ("sat", i))
            x = out.exchanges[0]; m.append(x.margin)
            full += x.margin >= 3.0
        mu = sum(m) / N
        print(f"{dn:8} {scen:12} first speech margin mean {mu:+.2f}; share filling the track alone {full/N:.3f}±{math.sqrt(full/N*(1-full/N)/N):.3f}")
host._judging = lambda p, D: host._base_pool(D)
for dn, D in (("shipped", dials.shipped()), ("rd (strike_level minor)", dials.rd_shipped())):
    r = sweep("bench_full", "dec", "focus", n=1500, D=D)
    print(f"bench pool=8 control, {dn}: decider Focus slope {r['slope']:+.4f} se {r['se']:.4f}")
