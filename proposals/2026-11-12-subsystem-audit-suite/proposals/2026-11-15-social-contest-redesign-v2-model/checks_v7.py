"""THE battery for the current sc2: every figure the v2 design states.  PYTHONHASHSEED=0 python checks_v7.py [n]
Runs, in order: checks_v7_core (D1..D8, F1..F8, carriers, bearing, context, power, fold, seasons, types, invariants),
checks_v4 (A-139), checks_v5 (A-141, A-142), checks_v6 (A-143), checks_v7_adj (A-144)."""
import runpy, sys
n = sys.argv[1] if len(sys.argv) > 1 else "400"
for mod in ("checks_v7_core", "checks_v4", "checks_v5", "checks_v6", "checks_v7_adj"):
    print(f"\n######## {mod}"); sys.argv = [mod + ".py", n]; runpy.run_module(mod, run_name="__main__")
