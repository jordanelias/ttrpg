"""ARM 0 -- THE REACHABILITY CENSUS. Which decision sites do the 143 cases actually reach?

This is the baseline every other arm is measured against, and it is the one number that settles
whether degrees are exercised today: if `S39` never fires, no case resolved a degree, and no
amount of reading the verb table can say otherwise.
"""
from __future__ import annotations
import collections
import sweep_core as K
from sweep_core import S, C, R, Log
from trace_log import TRACE


def run(log: Log, seed: int = 0) -> dict:
    log.rule("ARM 0 — REACHABILITY: what the 143 cases actually reach")
    sites = collections.Counter()
    site_cases = collections.defaultdict(set)
    chan = collections.Counter()
    statuses = collections.Counter()
    per_lane = collections.defaultdict(collections.Counter)
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            TRACE.rows.clear(); TRACE.case = c["id"]
            r = C.run_case(c, seed, lane)
            statuses[r["status"]] += 1
            per_lane[lane][r["status"]] += 1
            for x in TRACE.rows:
                chan[x.channel] += 1
                if x.channel == "DECISION":
                    sites[x.where] += 1
                    site_cases[x.where].add(c["id"])
    log("SCOPE", f"{sum(statuses.values())} cases run at seed {seed}")
    log("MEASURE", f"trace channel totals: {dict(chan)}")
    log("⚠ 2x", "EVERY COUNT ABOVE IS DOUBLE THE CORPUS, AND DELIBERATELY LEFT RAW.",
        "`corpus_run.run_case` folds the season TWICE — the measured run (:341) and the R4 "
        "determinism replay (:386-388) — and this census clears the trace once per case, so both "
        "are counted. Signature: `S24` reads 22 firings in 11 cases, i.e. 11 x 1 x 2. Halve for "
        "a per-corpus figure. Zero doubled is still zero, so the S39 result is unaffected — but "
        "the denominators are not per-corpus and saying so is cheaper than a second run. Found "
        "by the adversarial pass.")
    scales = collections.Counter()
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            rc = C.apply_rescale(c)
            if str(rc.get("scale")) not in set(S.RUNG_KINDS):
                scales[str(rc.get("scale"))] += 1
    log("MEASURE", f"UNREPRESENTABLE by scale: {dict(scales)} (total {sum(scales.values())})",
        "printed here because `corpus_run.main()` prints it and `sweep.py` never calls that — a "
        "number in the README's scope table had no instrument in the shipped run")
    log.rule("ARM 0a — every decision site the corpus reached")
    for w, n in sites.most_common():
        log("SITE", f"{w:14} {n:7} firings in {len(site_cases[w]):3} cases")
    log.rule("ARM 0b — the sites it did NOT reach")
    NEVER = {
        "S39": "the contest seam — where an act routes to a subsystem",
        "S39.3": "the contest depth cap",
        "S39.4": "the degree ladder's margin model",
        "S27.4": "the Ob/Pool budget refusal — the only other roll-shaped branch",
    }
    for w, what in NEVER.items():
        n = sites.get(w, 0)
        log("SITE", f"{w:14} {n:7} firings   — {what}",
            "NEVER REACHED" if n == 0 else "")
    total_dec = sum(sites.values())
    log("VERDICT", f"{sites.get('S39', 0)} of {total_dec} decision firings are the contest seam")
    log("⚠ WEAK", "THE S39 COUNT ALONE CANNOT CARRY THAT CONCLUSION, and an earlier draft rested "
                  "it there.",
        "`S39` as a `TRACE.decision` exists at ONE site (shape.py:4957), reached only after a "
        "personal-combat dispatch RETURNS RESOLVED; the other three S39 sites are raises. "
        "`S39.4` has no `TRACE.decision` at all — it is only the `where` of a raise — so its "
        "zero is vacuous and cannot observe the failure it excludes (§0.1 pt 2). And a contested "
        "act reaching `resolve()` would raise `Forbidden` at shape.py:4611 first, because "
        "`corpus_run` calls `season()` with no `contest_max_depth`. All three paths are raises "
        "and produce no DECISION row.")
    dg = statuses.get("DESIGN-GAP", 0); idf = statuses.get("INSTRUMENT-DEFECT", 0)
    log("VERDICT", f"the load-bearing evidence is the STATUS histogram: {dict(statuses)}",
        f"DESIGN-GAP={dg}, INSTRUMENT-DEFECT={idf}. `run_case` converts every `ShapeGap` and "
        f"`Forbidden` into one of those two statuses, so zero of both rules out the raise paths "
        f"the S39 counter cannot see. Together with `S39 == 0`: no contest was dispatched AND "
        f"none was attempted-and-refused. NOT ONE act in the corpus resolved at a degree.")
    return dict(sites=dict(sites), channels=dict(chan), statuses=dict(statuses),
                per_lane={k: dict(v) for k, v in per_lane.items()},
                total_decisions=total_dec, s39_firings=sites.get("S39", 0))
