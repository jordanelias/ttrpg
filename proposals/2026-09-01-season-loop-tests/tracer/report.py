"""The TRACING report. Every decision made and every step performed, per test.

`trace_log.py` is the channel; this is the readable artifact it feeds. It emits four things,
and the separation between them is deliberate:

  1. THE DECISION REGISTER -- every branch the shape took that could have gone another way,
     with the alternatives it did not take. This is the row that exists because A DECISION
     NOBODY RECORDS IS A DECISION NOBODY CAN AUDIT.
  2. THE STEP SEQUENCE -- the loop as executed: six steps, four barriers, in order, with the
     write class of every write that crossed the gate.
  3. THE PER-CASE LOG -- for each NPC and each arc: every `season_requires` row, the probe it
     routed onto, the verdict, and the section of ARCHITECTURE.md that governs it.
  4. THE PROBE LEDGER -- all probes, their verdicts, and HOW each verdict was reached
     (`by=`), because a refusal the shape raised and a refusal that exists only as an absent
     signature are different evidence.

A probe executes ONCE and its verdict is cached, so a case cannot change a probe's result.
That is why the per-case log records ROUTING and the step sequence records EXECUTION: they are
different facts and conflating them would let a case appear to have run something it did not.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RUNS = ROOT / "runs"


def emit(rep: dict, trace_rows: list) -> None:
    RUNS.mkdir(exist_ok=True)

    # -- 1. THE DECISION REGISTER ------------------------------------------
    decisions = [r for r in trace_rows if r.channel == "DECISION"]
    reg: dict[tuple, dict] = {}
    for d in decisions:
        key = (d.what.split(" -> ")[0][:110], d.where)
        e = reg.setdefault(key, dict(n=0, chose=Counter(), alts=set()))
        e["n"] += 1
        e["chose"][d.detail.get("chose", "-")] += 1
        for a in d.detail.get("alternatives", []):
            e["alts"].add(a)
    lines = ["# THE DECISION REGISTER",
             "",
             "Every branch the shape took that could have gone another way, with the alternatives",
             "it did not take. A decision nobody records is a decision nobody can audit.",
             "",
             f"**{len(decisions)} decisions taken, {len(reg)} distinct.**", ""]
    for (what, where), e in sorted(reg.items(), key=lambda kv: -kv[1]["n"]):
        lines.append(f"### {what}  ·  `{where}`  ·  taken {e['n']}x")
        for c, n in e["chose"].most_common():
            lines.append(f"- **chose:** {c}  ({n}x)")
        for a in sorted(e["alts"]):
            lines.append(f"- *not taken:* {a}")
        lines.append("")
    (RUNS / "DECISIONS.md").write_text("\n".join(lines))

    # -- 2. THE STEP SEQUENCE ----------------------------------------------
    steps = [r for r in trace_rows if r.channel in ("STEP", "BARRIER")]
    writes = [r for r in trace_rows if r.channel == "WRITE"]
    wc = Counter((w.detail.get("write_class"), w.detail.get("step"),
                  w.detail.get("admitted")) for w in writes)
    seq = ["# THE STEP SEQUENCE", "",
           f"**{sum(1 for r in steps if r.channel=='STEP' and r.what.startswith('enter'))} step "
           f"entries · {sum(1 for r in steps if r.channel=='BARRIER')} barrier openings · "
           f"{len(writes)} writes through the gate.**", "",
           "## Writes, by class and step (S30's matrix, checked PER WRITE SITE)", "",
           "| write class | step | admitted | count |", "|---|---|---|---|"]
    for (cls, st, ok), n in sorted(wc.items(), key=lambda kv: -kv[1]):
        seq.append(f"| {cls} | {st} | {'yes' if ok else '**NO -- refused**'} | {n} |")
    seq += ["", "## The loop, as executed", "",
            "```", "CALENDAR  -- barrier 1 -- fires occasions and DECIDES NOTHING",
            "MATTER    -- barrier 2 -- THE WORLD FREEZES AT ITS END",
            "DELIBERATE-- a MAP, not a barrier -- pure, parallel, no World",
            "RESOLVE   -- barrier 3 -- the ONLY writing step for acts; an ORDERED FOLD",
            "WITNESS   -- barrier 4 -- THE JOIN; fan-out global, deposit per-person",
            "CENSUS    -- shares WITNESS's join", "```", ""]
    (RUNS / "STEPS.md").write_text("\n".join(seq))

    # -- 3. THE PER-CASE LOG -----------------------------------------------
    for kind, title in (("NPC", "TEST A — 46 unique NPCs"),
                        ("ARC", "TEST B — every unique arc")):
        rows = rep.get(kind) or []
        out = [f"# {title} — the per-case log", "",
               "For each case: every `season_requires` row, the probe it routed onto, the verdict,",
               "and the section of `ARCHITECTURE.md` that governs it. **Probe verdicts are HARD**",
               "(each is an execution); **case verdicts are ADVISORY** (routing is keyword-based",
               "over prose, and keyword routing is crude).", "",
               "`UNMAPPED` = no probe matched; the row is reported, never passed.",
               "`UNCLEAR` = the CASE SOURCE fails to say something; that is the source failing,",
               "not the shape.", ""]
        for c in rows:
            out.append(f"## {c['id']} — {c.get('name','')}  ·  **{c['verdict']}**")
            out.append(f"*{c.get('scale','')} · {c['rows']} rows, {c['core']} core · "
                       f"blockers: {', '.join(c['blockers']) or 'none'}*")
            if c.get("ends_when"):
                out.append(f"*ends when:* {c['ends_when']}")
            out.append("")
            out.append("| need | probe | verdict | § |")
            out.append("|---|---|---|---|")
            for r in c["routed"]:
                v = r["verdict"]
                mark = "PASS" if v["verdict"] == "PASS" else f"**{v.get('kind') or v['verdict']}**"
                need = r["need"].replace("|", "\\|")[:190]
                out.append(f"| {'**[core]** ' if r['hardness']=='core' else ''}{need} "
                           f"| `{r['probe']}` | {mark} | {v['section']} |")
            for r in c["unmapped"]:
                need = r["need"].replace("|", "\\|")[:190]
                out.append(f"| {'**[core]** ' if r['hardness']=='core' else ''}{need} "
                           f"| — | UNMAPPED | — |")
            if c.get("unclear"):
                out.append(f"| *({c['unclear']} row(s) marked `UNCLEAR:` by the case source)* "
                           "| — | SOURCE-UNCLEAR | — |")
            out.append("")
        (RUNS / f"CASELOG_{kind}.md").write_text("\n".join(out))

    # -- 4. THE PROBE LEDGER -----------------------------------------------
    pv = rep["_probes"]
    by = Counter(v["by"] for v in pv.values())
    pl = ["# THE PROBE LEDGER", "",
          f"**{len(pv)} probes.** Each is a real execution against `shape.py` that either",
          "completes or raises a typed gap.", "",
          "## How each verdict was reached", "",
          "`ARCHITECTURE.md` §34: *overstating the enforcement column is the failure mode.* §47:",
          "*a false claim of enforcement is worse than none, because it stops the next reader from",
          "checking.* So every probe declares its provenance:", "",
          "| `by=` | means | count |", "|---|---|---|",
          f"| `construction` | **the shape itself raised** — a gate, a law or a type stopped it. This is evidence | {by['construction']} |",
          f"| `no-signature` | nothing to call. The design supplies no function by which it could be attempted — which *is* the refusal, but **absence is not a guard** | {by['no-signature']} |",
          f"| `convention` | the shape permits it and only a reader stops it. §27.2 is the design's own example and says so out loud | {by['convention']} |",
          f"| `probe-model` | the probe supplies a model the design does not, to reach the question at all | {by['probe-model']} |",
          "", "## The probes", "",
          "| probe | verdict | by | § | what it tests |", "|---|---|---|---|---|"]
    order = {"GAP": 0, "NOT-REFUSED": 1, "INSTRUMENT-ERROR": 2, "PASS": 3}
    for pid, v in sorted(pv.items(), key=lambda kv: (order.get(kv[1]["verdict"], 9), kv[0])):
        mark = "PASS" if v["verdict"] == "PASS" else f"**{v.get('kind') or v['verdict']}**"
        pl.append(f"| `{pid}` | {mark} | {v['by']} | {v['section']} | {v['tests'][:130]} |")
    pl += ["", "## Every gap, with the law that produced it", ""]
    for pid, v in sorted(pv.items()):
        if v["verdict"] == "PASS":
            continue
        pl += [f"### `{pid}` — {v['title']}  ·  **{v.get('kind')}**  ·  `{v['section']}`  ·  by `{v['by']}`",
               f"**what:** {v['detail']}", ""]
        if v.get("needs"):
            pl.append(f"**needs:** {v['needs']}")
        if v.get("law"):
            pl.append(f"**law:** {v['law']}")
        pl.append("")
    (RUNS / "PROBES.md").write_text("\n".join(pl))
    print(f"wrote DECISIONS.md ({len(reg)} distinct), STEPS.md, "
          f"CASELOG_NPC.md, CASELOG_ARC.md, PROBES.md")

    # -- 5. THE UNMAPPED REGISTER ------------------------------------------
    # An unrouted row is NOT a pass and NOT a gap. It is the instrument admitting IT DID NOT
    # AIM. Reporting the rows verbatim, clustered, is more honest than tuning regexes until
    # the number looks good -- and what the corpus asks for that NO PROBE COVERS is itself a
    # first-class finding about the shape's surface.
    for kind in ("NPC", "ARC"):
        rows = rep.get(kind) or []
        core = [(c["id"], u["need"]) for c in rows for u in c["unmapped"]
                if u["hardness"] == "core"]
        other = [(c["id"], u["need"]) for c in rows for u in c["unmapped"]
                 if u["hardness"] != "core"]
        terms = Counter()
        stop = set("the a an of to and or in be is are must able for that this it its with on as "
                   "by not no from at into their they them one own such which what when who whom "
                   "than rather same only other another each any all some more most both either "
                   "must-be can may will would could should there here also even while whether "
                   "without within across between over under after before during through".split())
        for _, n in core:
            for w in n.lower().replace("-", " ").split():
                w = "".join(ch for ch in w if ch.isalpha())
                if len(w) >= 5 and w not in stop:
                    terms[w] += 1
        out = [f"# UNMAPPED — {kind}: what the corpus asked for that no probe covers", "",
               "**An unrouted row is not a pass and not a gap. It is the instrument admitting it",
               "did not aim.** Every row is reproduced verbatim so a reader can judge whether the",
               "miss is a routing failure (fixable) or a genuine absence of any surface to probe",
               "(a finding about the shape).", "",
               f"**{len(core)} `core` rows and {len(other)} non-core rows did not route.**", "",
               "## The vocabulary of the unrouted `core` rows", "",
               "Frequency over terms of five letters or more, stopwords removed. A term that is",
               "frequent here names a capability the corpus keeps asking for and the probe set has",
               "no execution for.", "",
               "| term | count |", "|---|---|"]
        for w, n in terms.most_common(45):
            out.append(f"| {w} | {n} |")
        out += ["", "## Every unrouted `core` row, verbatim", ""]
        for cid, n in core:
            out.append(f"- **[{cid}]** {n}")
        out += ["", "## Every unrouted non-core row, verbatim", ""]
        for cid, n in other:
            out.append(f"- *[{cid}]* {n}")
        (RUNS / f"UNMAPPED_{kind}.md").write_text("\n".join(out))

    print(f"wrote UNMAPPED_NPC.md, UNMAPPED_ARC.md")



if __name__ == "__main__":
    import run_cases as R
    from trace_log import TRACE
    rep = R.main()
    (RUNS).mkdir(exist_ok=True)
    (RUNS / "results.json").write_text(json.dumps(rep, indent=1, default=str))
    (RUNS / "TRACE.txt").write_text(TRACE.dump_text())
    emit(rep, TRACE.rows)
