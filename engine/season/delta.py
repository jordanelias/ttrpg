"""BEFORE-AND-AFTER, AS A COMMAND. `PLAN.md` guardrail `G11`.

⚠ THIS EXISTS BECAUSE THE SAME DEFECT SHIPPED TWICE. `W5` published "97 passed" (it was 98) and
`W17` published "gaps 69 -> 69 · zero probe flips · NPC and ARC unchanged" — three claims about a
BEFORE state that is not in the tree, with no command that produces any of them. An adversarial
pass could neither confirm nor refute them, which is the same as not having reported them.

`results.json` carries no verdict summary and no history, so the before-state has to come from
git. This reads a committed revision's artifact and the working tree's, and prints the deltas a
commit message is allowed to claim.

    python delta.py                # working tree vs HEAD
    python delta.py <rev>          # working tree vs <rev>

Every number a commit message on this lane states about probes, gaps, verdicts or trace counts
should be a line of this output, quoted rather than retyped.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

RESULTS = "engine/season/runs/results.json"
# ⚠ THE ARTIFACT MOVED AT ADOPTION (ED-IN-0202) AND THIS TOOL READS IT OUT OF HISTORY, so the
# path is rev-dependent: before the adoption commit it existed only under `proposals/`. Naming
# one path made `delta.py <any earlier rev>` a hard SystemExit — which is this lane's declared
# G11 carrier ("every number a commit message states should be a line of this output") going
# silent at the exact commit that needed it. Found by an adversarial pass on the conversion.
RESULTS_BEFORE_ADOPTION = "proposals/2026-09-01-season-loop-tests/runs/results.json"
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def at(rev: str) -> dict:
    tried = []
    for path in (RESULTS, RESULTS_BEFORE_ADOPTION):
        out = subprocess.run(["git", "show", f"{rev}:{path}"],
                             cwd=REPO, capture_output=True, text=True)
        if not out.returncode:
            return json.loads(out.stdout)
        tried.append(f"{path} ({out.stderr.strip()})")
    raise SystemExit(f"cannot read results.json at {rev}; tried " + " and ".join(tried))


def now() -> dict:
    return json.loads((REPO / RESULTS).read_text())


def _cases(d: dict, sec: str) -> Counter:
    v = d[sec]
    return Counter(c.get("verdict") for c in (v.values() if isinstance(v, dict) else v))


def report(old: dict, new: dict, rev: str) -> None:
    o = {k: v.get("verdict") for k, v in old["_probes"].items()}
    n = {k: v.get("verdict") for k, v in new["_probes"].items()}
    flips = [(k, o.get(k), n.get(k)) for k in sorted(set(o) | set(n)) if o.get(k) != n.get(k)]
    added = sorted(set(n) - set(o))
    print(f"DELTA  {rev} -> working tree")
    print(f"  probes           {len(o):4} -> {len(n):4}"
          + (f"   new: {added}" if added else ""))
    print(f"  gap events       {len(old['_gaps']):4} -> {len(new['_gaps']):4}"
          "     (_gaps: every gap RAISED, not probe verdicts)")
    for key in sorted(set(old["_trace_counts"]) | set(new["_trace_counts"])):
        a, b = old["_trace_counts"].get(key, 0), new["_trace_counts"].get(key, 0)
        if a != b:
            print(f"  trace {key:<12} {a:4} -> {b:4}")
    for label, fn in (("by=", lambda d: Counter(v.get("by") for v in d["_probes"].values())),
                      ("verdict", lambda d: Counter(v.get("verdict")
                                                    for v in d["_probes"].values()))):
        a, b = fn(old), fn(new)
        if a != b:
            print(f"  probe {label:<10} {dict(sorted(a.items()))}")
            print(f"  {'':16} -> {dict(sorted(b.items()))}")
    for sec in ("NPC", "ARC"):
        a, b = _cases(old, sec), _cases(new, sec)
        mark = "" if a == b else "   <-- MOVED"
        print(f"  {sec:<16} {dict(sorted(a.items()))}{mark}")
        if a != b:
            print(f"  {'':16} -> {dict(sorted(b.items()))}")
    print(f"  PROBE FLIPS      {len(flips)}"
          + ("" if flips else "   (none — a change that moves no verdict)"))
    for k, a, b in flips:
        print(f"    {k}: {a} -> {b}")


if __name__ == "__main__":
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    report(at(rev), now(), rev)
