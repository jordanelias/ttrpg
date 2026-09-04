"""THE DEGREE SWEEP — corpus-wide runner. Emits every artifact under `runs/`.

Usage:  python sweep.py [seed]
"""
from __future__ import annotations
import collections, json, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sweep_core as K
from sweep_core import S, C, R, Log, LADDER_C, LADDER_D, KW
import arm0_census as A0
import arm1_admissibility as A1
import arm2_onramp as A2
import arm3_tree as A3
import arm4_margin as A4
import arm5_social as A5
import arm6_imports as A6
import arm7_flexibility as A7
import arm8_v30_benchmark as A8
import arm9_forking as A9
import arm10_throughlines as A10
import arm11_per_case as A11

OUT = Path(__file__).parent / "runs"
DEPTH = 3          # `CLAUDE.md` §0.1 pt 5 / G1: declared, not a bare literal.
DEPTH_WHY = ("Jordan's ask: 'explore at each decision point to a depth of three the degree of "
             "success'. Three consecutive contested folds in one carried-forward world.")


def runnable(lane: str) -> list:
    """⚠ `apply_rescale` FIRST, WHICH THE FIRST DRAFT OMITTED AND IT COST THREE CASES.
    `corpus_run.run_case` re-authors a case's `scale:` before testing it against `RUNG_KINDS`,
    so filtering on the raw `scale:` gave 27 NPC where the runner runs 30 — the sweep silently
    measured a smaller corpus than the instrument it is auditing. Caught by reconciling the
    sweep's case count against `corpus_run.py`'s own output rather than trusting either."""
    out = []
    for c in R.load_cases(lane):
        rc = C.apply_rescale(c)
        if str(rc.get("scale")) in set(S.RUNG_KINDS):
            out.append(rc)
    return out


def corpus_tree(log: Log, seed: int) -> dict:
    log.rule(f"ARM 3 — THE DEPTH-{DEPTH} DEGREE TREE, ACROSS THE WHOLE CORPUS")
    log("WHY", DEPTH_WHY)
    log("SETUP", f"branching factor = |ladder|; depth = {DEPTH}; "
                 f"so {len(LADDER_C)}^{DEPTH} = {len(LADDER_C)**DEPTH} paths on ladder C and "
                 f"{len(LADDER_D)}^{DEPTH} = {len(LADDER_D)**DEPTH} on ladder D, per case")
    log("SETUP", "a NODE is one contested act folded at one injected degree; the world carries "
                 "forward along a path and is forked by deepcopy at every branch")
    res = {"C": [], "D": []}
    t0 = time.time()
    for lane in ("NPC", "ARC"):
        for case in runnable(lane):
            for key, lad in (("C", LADDER_C), ("D", LADDER_D)):
                t = A3.tree(case, lad, DEPTH, log, seed)
                t["lane"] = lane
                t.pop("paths", None)          # per-path detail is emitted separately, not here
                res[key].append(t)
    log("TIMING", f"{sum(len(v) for v in res.values())} trees in {time.time()-t0:.1f}s")

    for key, name in (("C", "LADDER C — the canonical four"), ("D", "LADDER D — the declared three")):
        ts = res[key]
        n_paths = sum(t["n_paths"] for t in ts)
        n_alive = sum(t["n_alive"] for t in ts)
        depths = collections.Counter(t["reached_depth"] for t in ts)
        leaves = collections.Counter(t["distinct_leaves"] for t in ts)
        log.rule(f"ARM 3 RESULT — {name}")
        log("COUNT", f"{len(ts)} cases x {ts[0]['n_paths'] if ts else 0} paths = {n_paths} paths enumerated")
        log("COUNT", f"paths that survive all {DEPTH} nodes: {n_alive} "
                     f"({n_alive/n_paths*100 if n_paths else 0:.1f}%)")
        log("COUNT", f"deepest node reached, per case: {dict(sorted(depths.items()))}",
            "0 means the FIRST node refused, so every path is one node long and the other "
            f"{ts[0]['n_paths']-len(LADDER_C) if ts else 0}+ are never evaluated")
        log("COUNT", f"distinct leaf worlds per case: {dict(sorted(leaves.items()))}",
            "this is the discrimination measurement — if N surviving paths collapse to 1 leaf, "
            "the ladder produced N names for one future")
    return res


def main(seed: int = 0) -> int:
    OUT.mkdir(exist_ok=True)
    log = Log()
    log.rule("THE DEGREE SWEEP — degrees of success across the ARC and NPC corpus")
    log("SCOPE", f"cases: {len(R.load_cases('NPC'))} NPC + {len(R.load_cases('ARC'))} ARC = "
                 f"{len(R.load_cases('NPC'))+len(R.load_cases('ARC'))}, "
                 f"from all 11 case files in the PR chain",
        "the loader globs BOTH 2026-08-31-shape-tracer/cases and 2026-09-01-season-loop-tests/cases")
    log("SCOPE", f"runnable (scale is a rung kind): {len(runnable('NPC'))} NPC + "
                 f"{len(runnable('ARC'))} ARC")
    log("SEED", f"{seed} — the corpus arms are seeded and `R4` pins replay.",
        "⚠ NARROWED: an earlier version of this line claimed EVERY draw in the instrument was "
        "seeded. It was false of arm 5a, which drew from module-level `random` unseeded, and 5a "
        "is exactly the arm whose published distribution drifted between runs. 5a is seeded now; "
        "the claim is stated at the size it can carry.")

    out = {"seed": seed}
    out["arm0"] = A0.run(log, seed)
    out["arm1"] = A1.run(log)
    out["arm2"] = A2.run(log)
    out["arm2c"] = A2.run_2c(log)
    out["arm3"] = corpus_tree(log, seed)
    out["arm4a"] = A4.run_a(log)
    out["arm4b"] = A4.run_b(log)
    out["arm5a"] = A5.run_a(log)
    out["arm5b"] = A5.run_b(log)
    out["arm5d"] = A5.run_d(log)
    out["arm6"] = A6.run(log)
    out["arm7"] = A7.run(log, seed)
    out["arm8"] = A8.run(log)
    out["arm9"] = A9.run(log, seed)
    out["arm10"] = A10.run(log)
    out["arm11"] = A11.run(log)

    (OUT / "SWEEP_LOG.txt").write_text(log.text() + "\n")
    json.dump(out, open(OUT / "results.json", "w"), indent=1, default=str)
    print(log.text())
    print(f"\nwrote {OUT/'SWEEP_LOG.txt'} and {OUT/'results.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*(int(a) for a in sys.argv[1:])))
