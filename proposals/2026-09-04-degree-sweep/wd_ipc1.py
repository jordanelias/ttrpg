"""W-D supplement -- THE FIXTURE POINT `EXECUTION_PLAN.md` NAMED, RUN AND REPORTED.

The plan's W-D row asks for `DEFAULT_FIXTURES` and `interactions_per_scene=1`, "each with
observation_deposit on and off -- four arms". `H-117` had already measured that at
`interactions_per_scene=1` alone (scene_budget 5 x 1 = 5 slots) the budget BINDS but the in-budget
count `L` is 5, and `A9.MAX_ALT` probes only the top 3 alternatives -- so no probed alternative
lies outside the budget and every fork is INERT-BY-CONSTRUCTION. This runs it anyway rather than
citing that: a fixture point the plan named and the run skipped is not a measurement.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
from sweep_core import S

def fx(mode):
    return S.DEFAULT_FIXTURES.sweep("interactions_per_scene", 1).sweep(
        "observation_deposit_mode", mode)

if __name__ == "__main__":
    out = {}
    for mode in W.ARMS:
        rows, good = [], []
        import arm9_forking as A9
        f = fx(mode)
        for lane, c in W.CASES:
            r = A9.fork_case(c, W.SEED, W.SEASONS, fixtures=f)
            r["lane"] = lane
            rows.append(r)
        good = [r for r in rows if r.get("ok")]
        real = [x for r in good for x in r["forks"]
                if x.get("status") in ("DIVERGED", "RECONVERGED")]
        div = [x for x in real if not x["reconverged"]]
        # budget_binds at this point, over the deliberations actually recorded
        from sweep_core import Log
        log = Log()
        b = A9.budget_report(log, rows, f)
        out[mode] = dict(mode=mode, slots=5,
                         n_cases_ok=len(good), n_cases_failed=len(rows) - len(good),
                         probed=sum(r["n_forks"] for r in good),
                         no_live_window=sum(r["n_no_live_window"] for r in good),
                         inert=sum(r["n_inert"] for r in good),
                         genuine=len(real), diverged=len(div),
                         reconverged=len(real) - len(div),
                         reconvergence_rate=((len(real) - len(div)) / len(real)) if real else None,
                         budget=b, budget_log=log.text())
        print(mode, {k: v for k, v in out[mode].items() if k not in ("budget_log", "budget")})
        print(out[mode]["budget_log"])
    json.dump(out, open(Path(__file__).parent / "runs" / "wd_ipc1.json", "w"), indent=1,
              default=str)
    print("wrote runs/wd_ipc1.json")
