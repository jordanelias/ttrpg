"""Drive the extracted a:NPC and b:ARCS cases against the shape, and report.

Each case carries `season_requires` rows written in SHAPE-NEUTRAL language by lanes that had not
read the shape. This runner maps each `need` onto a probe — a concrete execution against the shape —
and records the verdict.

An unmatched need is NOT skipped. It is reported as `UNMAPPED`, which means the probe set does not
yet cover a capability a real case demands. That is a finding about the instrument, and the honest
loop is: read the unmapped clusters, add probes, re-run.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import Counter

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from probes import PROBES, PROBE_DOC, run_all           # noqa: E402
from trace_log import TRACE                              # noqa: E402

CASE_DIR = ("/tmp/claude-0/-home-user-ttrpg/"
            "78360267-ece4-57b1-8568-be13abd76bad/scratchpad/cases")

# need-text -> probe. Ordered; first match wins. Keys are regexes over the lowercased need.
ROUTES: list[tuple[str, str]] = [
    # -- SPECIFIC person-scale patterns FIRST. Ordering is load-bearing: an earlier pass put the
    # -- generic world rules first and mis-routed "degrade his PERSONAL condition" to W1 (site
    # -- decay) and "maintenance labor" to A3 (substrate), turning two BLOCKED cases into false
    # -- PLAYABLEs. A greedy keyword is worse than no keyword.
    (r"(degrade|wear|erode|cost).{0,40}(personal|his|her|their) (condition|health|body)"
     r"|proximity|exposure to .* damage|standing next to", "P31"),
    (r"death .* (produce|buy|purchase|different)|sacrific|spending (his|her|their) life"
     r"|die .* (seal|complete|finish)", "P32"),
    (r"multi-week|work-in-progress|ongoing work|across (multiple )?seasons.{0,30}(task|labor|work)"
     r"|recurring, location-bound|standing condition|half-done|interrupted partway", "P30"),
    (r"persistent object|physical product|outlives the scene|artifact .* independent"
     r"|evidence object|copied text .* exist", "P28"),
    (r"possess|found with it|merely holding|holder .* consequence", "P29"),
    (r"two (independent )?(rank|standing|reputation)|parallel .* track|separate ladder"
     r"|covert reputation|private reputation", "P33"),
    (r"reassess.{0,30}(loyal|stage)|in stages|gradual(ly)? .* reassess|does not revert", "P18"),
    (r"inaction|not acting|persist .* without forcing a decision|deferr|uncertainty is itself", "P19"),
    (r"diverge from what .* intended|carried out differently|acting in .* name .* diverge", "P20"),
    (r"more constrained by visibility|publicness|higher status .* cost|visible .* cost more", "P21"),
    (r"private setting at no cost|confidential counsel|frank .* private|public(ly)? .* would cost", "P22"),
    (r"cannot be retried|cooldown|un-repeatable|fail(ed)?, cost .* standing", "P23"),
    (r"revocable by the collective|body that grants it|revoke .* authority it granted", "P24"),
    (r"silently underperform|undetectable without|divided loyalt.{0,40}(cause|underperf)", "P25"),
    (r"accumulated .* harm|threshold .* confrontation|patience .* limit", "P26"),
    (r"investment .* window|alignment .* lock|won by whichever|contested .* allegiance", "P27"),
    (r"no office|without an office|no post|postless|no institutional|holds no", "P1"),
    (r"petition|demand in front|put .* before|bring .* to (a )?(sitting|court|council)", "P2"),
    (r"covert|without .* know(ing)? who|conceal|anonym|unattributed|secret(ly)? act", "P3"),
    (r"conviction|belief change|moral|scar|crisis of|change what .* is|transform", "P4"),
    (r"false|wrong conclusion|mistaken|misremember|believe .* untrue|deceiv", "P5"),
    (r"forget|decay of memory|lose .* memory|no longer recall", "P6"),
    (r"disagree|differ(ent)? account|two witnesses|perspective|construal", "P7"),
    (r"inherit|survives .* death|passed to .* heir|generation", "P8"),
    (r"dispatch|order .* subordinate|direct .* officer|command .* person|refuse an order", "P9"),
    (r"custody|register|records? .* held|archive|keeper of", "P10"),
    (r"two masters|conflicting (obligation|loyalt)|dual loyal|divided loyal", "P11"),
    (r"ambition|goal .* progress|rival|obstruct|pursue .* over", "P12"),
    (r"faction .* exist|movement .* form|found a|commit to a cause", "F1"),
    (r"leader(ship)? change|depose|deposition|who leads|succession of a (faction|movement)", "F2"),
    (r"faction .* end|dissolv|collapse of a (faction|movement)|everyone leaves", "F3"),
    (r"claim .* (press|sovereign)|pretend|title to|legitimacy of a claim", "F4"),
    (r"confer|appoint|invest|revoke|remove from office|grant an office", "F5"),
    (r"sitting|council|parliament|assembly|vote|motion|convene|decide together", "F6"),
    (r"decay|condition|disrepair|neglect|verb .* unavailable|falls into", "W1"),
    (r"band|threshold|tipping|equilibrium|maintain(ing)? .* against", "W2"),
    (r"nobody chose|no actor|world .* itself|weather|harvest|season(al)? change", "W3"),
    (r"off-?board|foreign power|altonia|empire|outside the peninsula|invasion", "W4"),
    (r"ends at a (sitting|meeting)|resolved at a|comes to a head at", "A1"),
    (r"counter|clock reach|threshold fires|automatic(ally)?|when .* reaches", "A2"),
    (r"substrate|thread|seam|metaphysic|forgetting|calamity", "A3"),
    (r"caus(e|al)|provenance|trace back|why it happened|chain of", "A4"),
    (r"spiral|escalat|feedback|runaway|compound|vicious", "A5"),
    (r"expos|reveal|becomes public|scandal|discovered|comes to light", "A6"),
]

_COMPILED = [(re.compile(p), pid) for p, pid in ROUTES]


def route(need: str):
    n = need.lower()
    for rx, pid in _COMPILED:
        if rx.search(n):
            return pid
    return None


def _repairs(body: str):
    """Yield progressively more aggressive repairs of a possibly-truncated lane output.

    A lane's final assistant message can begin mid-entry (the model streamed a long YAML and the
    captured message is a tail) or end mid-entry. Dropping the file loses real cases, so trim to
    whole `- id:` entries instead. This never invents content — it only discards partial edges.
    """
    yield body
    starts = [m.start() for m in re.finditer(r"^- id:", body, re.M)]
    if not starts:
        return
    head = body[starts[0]:]
    yield head                                    # drop a truncated leading entry
    if len(starts) > 1:
        # also drop a truncated trailing entry
        tail_start = starts[-1] - starts[0]
        yield head[:tail_start]


def load_cases() -> list[dict]:
    cases = []
    for path in sorted(glob.glob(os.path.join(CASE_DIR, "*.yaml"))):
        raw = open(path).read()
        m = re.search(r"```(?:ya?ml)?\s*\n(.*?)```", raw, re.S)
        body = m.group(1) if m else raw
        data = None
        for attempt, text in enumerate(_repairs(body)):
            try:
                data = yaml.safe_load(text)
                if isinstance(data, list) and data:
                    if attempt:
                        print(f"  ~ {os.path.basename(path)}: recovered by repair #{attempt} "
                              f"(a lane's final message was truncated mid-entry)")
                    break
            except Exception:
                data = None
        if data is None:
            print(f"  ! {os.path.basename(path)}: unparseable even after repair")
            continue
        if not isinstance(data, list):
            print(f"  ! {os.path.basename(path)}: not a list")
            continue
        for c in data:
            if isinstance(c, dict) and c.get("id"):
                c["_lane"] = os.path.basename(path).replace(".yaml", "")
                cases.append(c)
    return cases


def main():
    print("== running probes against the shape ==")
    probe_results = run_all()
    pv = {k: v for k, (v, _) in probe_results.items()}
    print(Counter(pv.values()))

    cases = load_cases()
    print(f"\n== {len(cases)} cases loaded ==")
    if not cases:
        print("no cases yet")
        return

    per_case, unmapped, by_verdict = {}, [], Counter()
    need_rows = 0
    for c in cases:
        cid = c["id"]
        TRACE.start_case(f"{c['_lane']}:{cid}")
        rows = []
        for nr in (c.get("season_requires") or []):
            if not isinstance(nr, dict):
                continue
            need = str(nr.get("need", ""))
            need_rows += 1
            pid = route(need)
            if pid is None:
                unmapped.append((cid, need, nr.get("hardness", "?")))
                rows.append({"need": need, "probe": None, "verdict": "UNMAPPED",
                             "hardness": nr.get("hardness")})
                by_verdict["UNMAPPED"] += 1
            else:
                v = pv.get(pid, "?")
                rows.append({"need": need, "probe": pid, "verdict": v,
                             "hardness": nr.get("hardness")})
                by_verdict[v] += 1
        per_case[cid] = {
            "lane": c["_lane"], "name": c.get("name"), "scale": c.get("scale"),
            "one_line": c.get("one_line"), "ends_when": c.get("ends_when"),
            "who_acts": c.get("who_acts"), "rows": rows,
        }

    verdicts = {}
    for cid, d in per_case.items():
        core_bad = [r for r in d["rows"]
                    if r["hardness"] == "core"
                    and r["verdict"] not in ("PASS", "PARTIAL", "UNMAPPED")]
        any_bad = [r for r in d["rows"]
                   if r["verdict"] not in ("PASS", "PARTIAL", "UNMAPPED")]
        verdicts[cid] = ("BLOCKED" if core_bad else
                         "DEGRADED" if any_bad else "PLAYABLE")

    print("\n== case verdicts ==")
    print(Counter(verdicts.values()))

    out = {
        "probe_results": {k: {"verdict": v, "detail": d, "doc": PROBE_DOC[k]}
                          for k, (v, d) in probe_results.items()},
        "need_rows": need_rows,
        "need_verdicts": dict(by_verdict),
        "case_verdicts": verdicts,
        "cases": per_case,
        "unmapped": [{"case": c, "need": n, "hardness": h} for c, n, h in unmapped],
        "trace_summary": TRACE.summary(),
        "gaps": TRACE.gap_rows(),
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "..", "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    TRACE.dump(os.path.join(here, "..", "TRACE.txt"),
               os.path.join(here, "..", "gaps.json"))

    print(f"\nunmapped needs: {len(unmapped)}")
    for cid, need, h in unmapped[:25]:
        print(f"  [{h}] {cid}: {need[:96]}")


if __name__ == "__main__":
    main()
