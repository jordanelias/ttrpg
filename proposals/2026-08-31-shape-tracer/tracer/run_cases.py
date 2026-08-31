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

# The corpus is COMMITTED next to the runner. It used to be read from a session scratchpad,
# which meant the run was not reproducible by anyone but the session that made it — a read-only
# audit caught that `04_UNIFIED_SHAPE.md`'s own falsifier ("re-run the classification") was not
# executable from what was committed. An unreproducible measurement is a reading.
CASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cases")

# need-text -> probe. Ordered; first match wins. Keys are regexes over the lowercased need.
ROUTES: list[tuple[str, str]] = [
    # -- SPECIFIC person-scale patterns FIRST. Ordering is load-bearing: an earlier pass put the
    # -- generic world rules first and mis-routed "degrade his PERSONAL condition" to W1 (site
    # -- decay) and "maintenance labor" to A3 (substrate), turning two BLOCKED cases into false
    # -- PLAYABLEs. A greedy keyword is worse than no keyword.
    # -- EIGHTH WAVE. The King's first core need routed to A5 (spirals) on the word "compound";
    # -- it is an ACTION BUDGET, and Jordan's stated player model is ~5 scenes and so ~5 acts
    # -- per season. The shape gives exactly one. Triage is the whole game at high office.
    (r"address a subset|only .{0,30}(address|act on) .{0,20}(some|a subset|part)"
     r"|unaddressed .{0,20}compound|several independent, ongoing pressure|actions? per season"
     r"|limited .{0,30}per-season (budget|pool)|menu of distinct .{0,20}actions"
     r"|action economy|renewing per-season", "P36"),
    # -- SEVENTH WAVE routes. Ordering defect found when the expanded arc corpus landed: the
    # -- bare word "threshold" was routing 16 core needs onto W2 (band strobing), which is a
    # -- different mechanism entirely. Mis-routing did not flatter the shape here (W2 is also a
    # -- gap, so the cases stayed BLOCKED) but it ATTRIBUTED the block to the wrong cause, which
    # -- is how a change-list gets aimed at the wrong object. These run first.
    (r"hidden (personal )?(quantity|exposure|track)|silently accumulate|invisible until"
     r"|accumulat\w* (a )?hidden|without (his|her|their|the character.s) (own )?knowledge"
     r"|unaware .* accumulat|not visible to (him|her|them)self", "P34"),
    (r"contestable by an opposing|opposing actor.s action in the same|net effect"
     r"|push(ing)? .* in opposite|counter(ed|ing) by another actor", "P35"),
    (r"(cross|reach|pass)\w* (a |its |multiple |the )?(hard )?threshold\w*"
     r"|on (crossing|reaching) (a |its |the )?threshold|threshold[- ]triggered"
     r"|trigger\w* (an?|the) .* on (crossing|reaching)|use-threshold", "P26"),
    # -- ARC-driven routes, added after the arc lanes reported (sixth wave)
    # A13 is ambient SOCIAL drift. Keying it on the bare word "ambient" caught four rows about
    # an ambient WORLD-HEALTH or ENVIRONMENTAL quantity — which is matter, already lawful, and
    # already served (A3 passes: the substrate is a Site kind). Those four were inflating the
    # bill this test sends to Jordan. Key on the SUBJECT being social.
    (r"(ambient|background|drift\w*|erod\w+|passive)\b[^.]{0,80}(cultural|allegiance|loyalty|mood|opinion|sentiment|disposition|population|popular|social)"
     r"|(cultural|allegiance|loyalty|mood|sentiment|disposition)[^.]{0,60}(drift|erod|decay|sour|decline)"
     r"|absence of any faction|purely from the absence|from the absence of any", "A13"),
    (r"invisible to himself|nobody .* deciding|no actor triggers|spontaneous(ly)? .* (check|change)"
     r"|without any actor", "A14"),
    (r"held in reserve|once per arc|usable once|reserved resource|optimal .* window", "A15"),
    (r"procedural (stage|timetable)|advance .* on its own|regardless of whether .* acts"
     r"|fixed procedural", "A16"),
    # FOURTH greedy-keyword defect, found by the comparative audit: the bare word "enforce"
    # routed five needs here, including the King's "a policy he ENFORCES", which then read
    # as PASS. A17 is specifically WINNING vs ENFORCING as two events; require that shape.
    (r"(won|winning|victor\w*|ruling|contest|argument).{0,60}(separate|distinct|independent)"
     r"|implementation .* fail|enforc\w+ .{0,40}(separate|fail|its own)"
     r"|(separate|distinct) .{0,30}enforc", "A17"),
    (r"persist(ent|s)? .* after the (battle|scene)|outlives the scene that|lingering|carries into"
     r"|condition .* not automatically cleared", "A18"),
    (r"irreversib|no exit|permanently and irrecoverab|zero-point|can no longer choose", "A19"),
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
    (r"inaction|not acting|persist\w* .{0,40}without forcing a decision|deferr"
     r"|uncertainty is itself|persistence must itself count|rather than a null state"
     r"|erode from .{0,20}inaction|from (that |the )?(patron|leader|ruler).s inaction", "P19"),
    (r"diverge from what .* intended|carried out differently|acting in .* name .* diverge", "P20"),
    (r"more constrained by visibility|publicness|higher status .* cost|visible .* cost more"
     r"|lower-status .{0,40}would not|a cost that a (lower|higher)\b|status .{0,20}asymmetr", "P21"),
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
    # W1 is SITE decay. The bare word "condition" was catching "nine named conditions",
    # "the underlying situation", "a pre-existing condition" — the third greedy-keyword
    # defect of this build, and the reason case verdicts are now advisory-only (see §5).
    (r"disrepair|falls into (disrepair|ruin)|neglect(ed)? (site|place|building|harbour)"
     r"|(site|place|building|harbour|road|fort)\w* .{0,30}(decay|degrade|deteriorat)"
     r"|decay .{0,20}(site|place|building|infrastructure)|verb .* unavailable"
     r"|condition of (a|the) (site|place|building)", "W1"),
    (r"\bband\b|tipping point|equilibrium|maintain(ing)? .* against (decay|wear|entropy)"
     r"|oscillat|strobe|flap", "W2"),
    (r"nobody chose|no actor|world .* itself|weather|harvest|season(al)? change", "W3"),
    (r"off-?board|foreign power|altonia|empire|outside the peninsula|invasion", "W4"),
    (r"ends at a (sitting|meeting)|resolved at a|comes to a head at", "A1"),
    # A2 is a threshold FIRING AN OUTCOME with nobody deciding. Bare `counter` matched inside
    # "counter-productive"; bare `automatic` matched "not automatically a safe action". Both
    # inflate the corpus's single largest blocker, which is the number that prices Law 1's
    # refusal — so a loose regex here is the most expensive one in the file.
    (r"\bcounters?\b(?![-\w])|clock reach|threshold fires|when .{0,40} reaches"
     r"|(trigger|fire)\w* an? (automatic|unavoidable|immediate)"
     r"|automatic(ally)?,? (and )?(simultaneous|unavoidab|self-sustain|at the (direct|expense))"
     r"|must automatically", "A2"),
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
        core = [r for r in d["rows"] if r["hardness"] == "core"]
        core_unmapped = [r for r in core if r["verdict"] == "UNMAPPED"]
        # A case whose core needs mostly did not route was not tested. Calling it PLAYABLE is the
        # instrument flattering the shape by failing to aim at it — the exact direction §5 warns
        # about. BLOCKED still wins over NOT-ASSESSED: one executed core failure is a real result.
        verdicts[cid] = (
            "BLOCKED" if core_bad else
            "NOT-ASSESSED" if core and len(core_unmapped) * 2 >= len(core) else
            "DEGRADED" if any_bad else
            "PLAYABLE")

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
