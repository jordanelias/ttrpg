"""THE battery for sc2 after the second fix pass: every figure the v2 design states.  PYTHONHASHSEED=0 python checks_v8.py [n]
Runs, in order: checks_v8_core (D1..D8, F-list, carriers, bearing, context, power, fold, types, invariants, settings),
checks_v8_a139, checks_v8_a141, checks_v8_a143, checks_v8_adj (A-144, A-145, A-146), then the fix pass's own probes
fix2/c1 (C1), c_form (C: formality, the silence cell), c2 and c2_n (C2), c3 and c3_grid (C3, D1, D3), c4 (C4), c5 (C5),
d2 (D2, B9: 3 and 12 seasons), b17 (B17), bitems (B1..B21, C, E, F)."""
import os, runpy, sys
n = sys.argv[1] if len(sys.argv) > 1 else "300"
start = sys.argv[2] if len(sys.argv) > 2 else None      # resume from a named probe (the model unchanged), appending
here = os.path.dirname(os.path.abspath(__file__))
for mod in ("checks_v8_core", "checks_v8_a139", "checks_v8_a141", "checks_v8_a143", "checks_v8_adj"):
    if start: break
    print(f"\n######## {mod}", flush=True); sys.argv = [mod + ".py", n]; runpy.run_module(mod, run_name="__main__")
sys.path.insert(0, os.path.join(here, "fix2"))
for f, args in (("c1", [n]), ("c_form", [n]), ("c2", [n]), ("c2_n", ["1500"]), ("c3", [n]), ("c3_grid", ["800"]), ("c4", [n]), ("c5", [n]),
                ("d2", ["100", "3"]), ("d2", ["30", "12"]), ("b17", [n]), ("bitems", [n]), ("fswap", ["600"]), ("reconcile", ["1200"])):
    if start and f != start: continue
    start = None
    print(f"\n######## fix2/{f}", flush=True); sys.argv = [f + ".py"] + args
    runpy.run_path(os.path.join(here, "fix2", f + ".py"), run_name="__main__")
