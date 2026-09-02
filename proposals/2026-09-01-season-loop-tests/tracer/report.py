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
               "For each case: every `season_requires` row, what it DECLARES it rests on, the",
               "verdict, and the governing section. **Probe verdicts are HARD**",
               "(each is an execution).", "",
               "⚠ **ROUTING IS DECLARED, NOT MATCHED (`W10`).** The regex router is deleted. A row",
               "reaches a verdict only through an authored `exercises:` list in",
               "`cases/exercises/*.yaml`, bound to the row by the sha of its own need text — so a",
               "row that reaches the wrong answer is an authoring error somebody can argue with,",
               "not a pattern that fired on a common word. And every count the router published",
               "was a **floor**: an unmatched row fell silently to UNMAPPED, understating the",
               "corpus in the direction that flattered it.", "",
               "| verdict | means |", "|---|---|",
               "| `PASS` | every token the row declares resolved and is satisfied |",
               "| `ASSUMED` | resolved, but at least one rests on an **injected default nobody "
               "ratified**. Never a pass; it carries the case to DEGRADED |",
               "| `GAP` | a declared token named a real thing that is `absent`, unexecutable or "
               "gapping — a finding about the **shape** |",
               "| `UNMAPPED` | **nobody authored an `exercises:` for this row.** A fact about "
               "AUTHORING, which is fixable — never a pass |",
               "| `SOURCE-UNCLEAR` | the CASE SOURCE fails to say something; the source failing, "
               "not the shape |", ""]
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
          "",
          "## ⚠ THE ENFORCEMENT SPLIT — the single most important number in this ledger",
          "",
          f"**Of {sum(1 for v in pv.values() if v['verdict'] != 'PASS')} PROBES that did not "
          "pass, "
          f"{sum(1 for v in pv.values() if v['verdict'] != 'PASS' and v['by'] == 'construction')} "
          "were raised BY THE SHAPE ITSELF and "
          f"{sum(1 for v in pv.values() if v['verdict'] != 'PASS' and v['by'] == 'no-signature')} "
          "exist only because THERE IS NO SIGNATURE TO CALL.**",
          "",
          "> ⚠ **THIS COUNTS PROBES, NOT GAP EVENTS, and the two numbers differ.** "
          f"`results.json`'s `_trace_counts.GAP` is {TRACE.counts().get('GAP', 0)} — every gap "
          "RAISED during the run, including several inside one probe and several the corpus "
          "cases hit. This line counts probes whose VERDICT is not PASS: "
          f"{sum(1 for v in pv.values() if v['verdict'] != 'PASS')} of {len(pv)}. Both are "
          "honest counts of different populations, and `G10` forbids reporting either without "
          "its basis — which this file did until the `W5` adversarial pass read both.",
          "",
          "That is close to an even split, and it matters more than any case verdict. A refusal a",
          "gate enforces and a refusal that exists because nobody wrote the function are different",
          "guarantees, and §34 is explicit that *overstating this column is the failure mode*.",
          "",
          "**Why the distinction bites hardest at the port.** §47 concedes that [engine] GDScript",
          "has no module system and no visibility modifiers, so the guarantee there is",
          "*unreachable-by-name*, not *unwritable*. Every refusal in the `no-signature` half is one",
          "a contributor closes by simply writing the function — no gate fires, no test goes red,",
          "and the design's own §27.2 admission applies: *enforced by a person noticing*.",
          "",
          f"**And {sum(1 for v in pv.values() if v['verdict'] == 'PASS' and v['by'] != 'construction')} "
          f"of {sum(1 for v in pv.values() if v['verdict'] == 'PASS')} PASSes are not by construction",
          "either** — they are listed individually below and should be discounted accordingly. A",
          "`probe-model` PASS means the instrument supplied something the design does not.",
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
    # An undeclared row is NOT a pass and NOT a gap. It is the instrument admitting IT DID NOT
    # AIM. Under `W10` that admission is precise: NOBODY AUTHORED AN `exercises:` FOR THIS ROW.
    # Reporting the rows verbatim, clustered, is what makes the authoring backlog readable --
    # and what the corpus keeps asking for is itself a first-class finding about the surface.
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
        out = [f"# UNMAPPED — {kind}: the rows nobody has authored an `exercises:` for", "",
               "**An undeclared row is not a pass and not a gap. It is the instrument admitting it",
               "did not aim.** Under `W10` there is no regex to blame: a row lands here because no",
               "`cases/exercises/*.yaml` declares what it rests on. That is a fact about AUTHORING",
               "— fixable by writing one — rather than a pattern having missed, which was not.",
               "Every row is reproduced verbatim so the backlog can be worked from this file.", "",
               f"**{len(core)} `core` rows and {len(other)} non-core rows are undeclared.**", "",
               "## The vocabulary of the undeclared `core` rows", "",
               "Frequency over terms of five letters or more, stopwords removed. ⚠ **This is a",
               "reading aid for whoever authors the next overlay, and nothing computes a verdict",
               "from it** — a frequency table over prose is exactly the object `W10` deleted, and",
               "it is safe here only because it is printed and never read back.", "",
               "| term | count |", "|---|---|"]
        for w, n in terms.most_common(45):
            out.append(f"| {w} | {n} |")
        out += ["", "## Every undeclared `core` row, verbatim", ""]
        for cid, n in core:
            out.append(f"- **[{cid}]** {n}")
        out += ["", "## Every undeclared non-core row, verbatim", ""]
        for cid, n in other:
            out.append(f"- *[{cid}]* {n}")
        (RUNS / f"UNMAPPED_{kind}.md").write_text("\n".join(out))

    # THE DISCLOSURE S320 PROMISED AND REV 4 NEVER DELIVERED.
    import shape as _s
    used = sorted(_s.ASSUMPTIONS_USED)
    out = ["# THE INSTRUMENT'S OWN ASSUMPTIONS — what it had to supply to run at all", "",
           "**§42.2.1's inject-declare-name pattern, applied to SCHEMA ROWS rather than to",
           "numbers.** Without these the loop cannot complete one season, so refusing them would",
           "mean measuring nothing; asserting them silently would be the invention §42.3 names.",
           "", f"**{len(used)} of {len(_s.PARTITION_ASSUMED)} declared assumptions were actually",
           "exercised by this run.**", "", "| row | social | why | exercised |", "|---|---|---|---|"]
    for k, (social, why) in sorted(_s.PARTITION_ASSUMED.items()):
        out.append(f"| `({k[0]}, {k[1]})` | {social} | {why} | {'yes' if k in used else 'no'} |")
    out += ["", "## Harness fixtures — every number this instrument used", "",
            "| fixture | value | in chain? |", "|---|---|---|"]
    inchain = {"entrenchment_seasons": "yes — §15.2",
               "obstacle_refusal_multiple": "yes — §27.4"}
    for k, v in _s.DEFAULT_FIXTURES._v.items():
        out.append(f"| `{k}` | `{v}` | {inchain.get(k, 'no — a harness fixture')} |")
    (RUNS / "ASSUMPTIONS.md").write_text("\n".join(out))
    print(f"wrote UNMAPPED_NPC.md, UNMAPPED_ARC.md, ASSUMPTIONS.md ({len(used)} exercised)")



if __name__ == "__main__":
    import run_cases as R
    from trace_log import TRACE
    rep = R.main()
    (RUNS).mkdir(exist_ok=True)
    (RUNS / "results.json").write_text(json.dumps(rep, indent=1, default=str))
    (RUNS / "TRACE.txt").write_text(TRACE.dump_text())
    emit(rep, TRACE.rows)
