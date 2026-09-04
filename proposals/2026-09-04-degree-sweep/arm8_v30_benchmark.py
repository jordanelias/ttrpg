"""ARM 8 -- THE v30 COUNTERFACTUAL CORPUS AS A BENCHMARK.

⚠ JORDAN POINTED AT THIS, 2026-09-04: `tests/stress` at `v30-snapshot-2026-06-28`.

`tests/stress/emergent_arc_2026-04-17_batch8_counterfactual.md` is 916 lines of the EXACT
exploration this sweep was asked to mechanize, done by hand in 2026-04. Its stated method:

    "Each scenario identifies a major mechanical branch point from a prior scenario, takes the
     path NOT taken (ALTERNATE DEGREE, alternate NPC choice, alternate trigger), and traces the
     emergent consequences forward."

    Branch types used:
      DEGREE INVERSION   the roll succeeded where we assumed failure, or vice versa
      NPC CHOICE FORK    NPC took Option B where we assumed Option A
      TRIGGER TIMING     a clock or condition that fired differently
      PLAYER CHOICE FORK the player chose the path explicitly not modeled

So the corpus already declares what an alternative-outcome exploration IS, and it is a standard
this sweep can be measured against rather than a standard this sweep invents. That is the whole
value of this arm: arm 7 says how flexible the engine is on ITS OWN axis; this says how much of
the axis the DESIGN uses is reachable at all.

⚠ THE CLASSIFICATION BELOW IS A JUDGEMENT AND IS PRINTED WITH ITS EVIDENCE so a reader can
disagree per row. It is keyed on each scenario's own `ALTERNATE PATH:` line, quoted verbatim.
This arm reads the snapshot through `git show`; it edits nothing and the tag is not checked out.
"""
from __future__ import annotations
import re, subprocess
from sweep_core import Log

TAG = "v30-snapshot-2026-06-28"
DOC = "tests/stress/emergent_arc_2026-04-17_batch8_counterfactual.md"
REPO = "/home/user/ttrpg"

# The engine's reachability per branch type, each cited to the arm that measured it.
REACHABLE = {
    "DEGREE": (False, "arm 0: S39 fires 0 times in 5,376 decision firings; no corpus act "
                      "resolves at a degree"),
    "STATE": (True, "arm 7: state-threshold divergence is reachable — 8..29 distinct world "
                    "futures per case"),
    "CHOICE": (True, "arm 7: a substitution branch changes the acts, but arm 7c shows the budget "
                     "never binds, so the person never excludes anything on their own"),
}


def load() -> str:
    return subprocess.run(["git", "-C", REPO, "show", f"{TAG}:{DOC}"],
                          capture_output=True, text=True, check=True).stdout


def classify(alt: str) -> tuple:
    a = alt.lower()
    if re.search(r"\bfails?\b|\bsucceeds?\b|\bloses\b|\bd10 roll\b|\broll\b|degree|operation fails",
                 a):
        return "DEGREE", "names a roll outcome, a degree, or a contest won/lost"
    if re.search(r"\bplayer (distributes|uses|chooses)\b|no player|no pc expedition", a):
        return "CHOICE", "names an actor choosing a different option"
    return "STATE", "names a stored quantity, threshold or type differing"


def run(log: Log) -> dict:
    log.rule("ARM 8 — the v30 counterfactual corpus as a benchmark")
    log("SOURCE", f"{TAG}:{DOC} — 916 lines, 2026-04-17")
    log("METHOD", "quoted from the document: 'takes the path NOT taken (ALTERNATE DEGREE, "
                  "alternate NPC choice, alternate trigger), and traces the emergent "
                  "consequences forward'")
    try:
        t = load()
    except Exception as e:
        log("GAP", f"cannot read the snapshot: {type(e).__name__}: {e}")
        return {}
    rows = []
    for b in re.split(r"\n### ", t)[1:]:
        name = b.split("\n")[0].strip()
        m = re.search(r"ALTERNATE PATH:\s*(.*?)(?:\nQUESTION:|\n\n)", b, re.S)
        if not m:
            continue
        alt = " ".join(m.group(1).split())
        kind, why = classify(alt)
        rows.append(dict(scenario=name.split(":")[0], alt=alt, kind=kind, why=why))
    log("COUNT", f"{len(rows)} counterfactual scenarios parsed")
    for r in rows:
        log("BRANCH", f"{r['scenario']:10} [{r['kind']:6}] {r['alt'][:104]}")
        log("", f"           classified {r['kind']} because it {r['why']}")

    import collections
    by = collections.Counter(r["kind"] for r in rows)
    log.rule("ARM 8 — how much of the design's own branch axis can the engine reach?")
    tot = len(rows)
    unreach = 0
    for k, n in by.most_common():
        ok, cite = REACHABLE[k]
        if not ok:
            unreach += n
        log("AXIS", f"{k:7} {n:2} of {tot} scenarios ({n/tot*100:4.1f}%) — engine reach: "
                    f"{'YES' if ok else 'NO'}", cite)
    log("VERDICT", f"{unreach} of {tot} ({unreach/tot*100:.0f}%) of the corpus's OWN "
                   f"counterfactual branches are unreachable by the current engine",
        "the design's dominant way of generating an alternative future is to invert a roll. That "
        "is the one axis arm 0 measured at zero. Arm 7's flexibility number (mean 0.31) is "
        "therefore an upper bound reached WITHOUT the axis the design leans on hardest.")
    log("NOTE", "two of the DEGREE rows name subsystems that exist",
        "'Player LOSES the bilateral personal combat' is `personal_combat`, which "
        "`combat_seam` really does call (arm 2b) and which no verb routes to; 'Crown runs "
        "counter-intelligence (Intel vs Ob 2) and SUCCEEDS' is an investigation contest, which "
        "is HANDOFF_NEXT row 2b — the discovery model that was prescribed and not built (arm 6).")
    return dict(tag=TAG, doc=DOC, n=tot, by_kind=dict(by), unreachable=unreach,
                unreachable_pct=unreach / tot * 100 if tot else 0.0, rows=rows)
