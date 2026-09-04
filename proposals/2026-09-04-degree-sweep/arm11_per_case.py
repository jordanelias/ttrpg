"""ARM 11 -- PER-CASE THROUGHLINES: what recurs INSIDE each arc/NPC, and what blocks it.

⚠ JORDAN, 2026-09-04: *"Identify throughlines/lessons/recurring issues within each arc/NPC too."*

Arm 10 ranks demand across the corpus. This profiles EACH of the 143 cases: which capability
families its own `season_requires` rows ask for, which of those the engine cannot supply, and
therefore what specifically fails for that case. Then it clusters the 143 profiles, because the
recurring pattern is not visible one case at a time -- it is visible when two dozen cases turn out
to want the same three things.

Emits `runs/CASE_PROFILES.md`: one row per case, so a reader can go to their arc directly.
"""
from __future__ import annotations
import collections, re
from pathlib import Path
import sweep_core as K
from sweep_core import S, C, R, Log
from arm10_throughlines import FAMILIES, STATUS, BLOCKED

OUT = Path(__file__).parent / "runs"


def profile_all() -> list:
    out = []
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            rc = C.apply_rescale(c)
            rows = c.get("season_requires") or []
            fams = collections.Counter(); core = collections.Counter()
            for r in rows:
                n = str(r.get("need", "")).lower()
                for fam, pat in FAMILIES.items():
                    if re.search(pat, n):
                        fams[fam] += 1
                        if r.get("hardness") == "core":
                            core[fam] += 1
            blocked = sorted([f for f in fams if STATUS.get(f, ("?",))[0] in BLOCKED],
                             key=lambda f: -core[f])
            blocked_core = sum(core[f] for f in blocked)
            t = c.get("temporal") or {}
            span = t.get("span_seasons") if isinstance(t, dict) else None
            out.append(dict(
                id=c["id"], lane=lane, scale=str(rc.get("scale")),
                runnable=str(rc.get("scale")) in set(S.RUNG_KINDS),
                name=str(c.get("name", ""))[:38],
                n_rows=len(rows),
                n_core=sum(1 for r in rows if r.get("hardness") == "core"),
                span=span if isinstance(span, int) else str(span or "unauthored"),
                families=dict(fams), core_by_family=dict(core),
                blocked=blocked, blocked_core=blocked_core,
                top_block=blocked[0] if blocked else None,
                signature=tuple(sorted(fams)),
            ))
    return out


def run(log: Log) -> dict:
    log.rule("ARM 11 — PER-CASE THROUGHLINES: the recurring issue inside each arc/NPC")
    P = profile_all()
    log("SCOPE", f"{len(P)} cases profiled against arm 10's thirteen families")

    # --- what blocks each case -------------------------------------------------
    log.rule("ARM 11a — the DOMINANT blocker per case")
    top = collections.Counter(p["top_block"] for p in P)
    for f, n in top.most_common():
        label = f or "— nothing blocked"
        log("BLOCKER", f"{str(label):24} is the dominant blocker for {n:3} of {len(P)} cases")
    clean = [p for p in P if not p["blocked"]]
    log("MEASURE", f"cases with NO blocked family: {len(clean)} of {len(P)}",
        f"e.g. {', '.join(p['id'] for p in clean[:8])}" if clean else "")

    # --- how many blocked CORE rows -------------------------------------------
    log.rule("ARM 11b — how deep the block goes, per case")
    depth = collections.Counter(min(p["blocked_core"], 6) for p in P)
    log("RESULT", f"blocked CORE rows per case (6+ bucketed): {dict(sorted(depth.items()))}",
        "a case with 0 blocked core rows can be run for what it is FOR; one with 4+ cannot be "
        "meaningfully attempted at all")
    worst = sorted(P, key=lambda p: -p["blocked_core"])[:10]
    for p in worst:
        log("WORST", f"{p['id']:20} {p['name']:38} {p['blocked_core']} blocked core rows · "
                     f"{', '.join(p['blocked'][:3])}")

    # --- the recurring SIGNATURES ---------------------------------------------
    log.rule("ARM 11c — the recurring signatures: cases that want the same things")
    sig = collections.Counter(p["signature"] for p in P)
    log("MEASURE", f"{len(sig)} distinct demand signatures across {len(P)} cases",
        "a low number would mean the corpus is repetitive; a high one, that it is diverse and "
        "every case is its own shape")
    for s, n in sig.most_common(6):
        if n < 2:
            continue
        log("CLUSTER", f"{n:3} cases share: {', '.join(s) if s else '(no family matched)'}")

    # --- PAIRS: which demands co-occur ----------------------------------------
    log.rule("ARM 11d — which demands travel together (the real throughlines)")
    pair = collections.Counter()
    for p in P:
        fs = sorted(p["families"])
        for i in range(len(fs)):
            for j in range(i + 1, len(fs)):
                pair[(fs[i], fs[j])] += 1
    for (a, b), n in pair.most_common(8):
        sa = STATUS.get(a, ("?",))[0]; sb = STATUS.get(b, ("?",))[0]
        both = (sa in BLOCKED) and (sb in BLOCKED)
        log("PAIR", f"{n:3} cases want BOTH {a} + {b}"
                    + ("   ⚠ BOTH BLOCKED" if both else f"   ({sa} / {sb})"))

    # --- lane and scale differences -------------------------------------------
    log.rule("ARM 11e — does the ARC lane want different things from the NPC lane?")
    for lane in ("NPC", "ARC"):
        ls = [p for p in P if p["lane"] == lane]
        fam = collections.Counter()
        for p in ls:
            for f in p["families"]:
                fam[f] += 1
        tot = len(ls)
        top3 = ", ".join(f"{f} {c/tot*100:.0f}%" for f, c in fam.most_common(4))
        blk = sum(1 for p in ls if p["blocked"])
        log("LANE", f"{lane} ({tot} cases): top demands — {top3}")
        log("", f"     cases with a blocked family: {blk} of {tot} ({blk/tot*100:.0f}%)")

    # --- the artifact ----------------------------------------------------------
    OUT.mkdir(exist_ok=True)
    lines = ["# Per-case throughlines — 143 ARC and NPC cases",
             "",
             "Generated by `arm11_per_case.py`. One row per case: what its own "
             "`season_requires` rows ask for, and which of those the engine cannot supply.",
             "",
             "`blocked core` counts the case's OWN `hardness: core` rows that land in a family "
             "arm 10 measured as SEVERED / ABSENT / INERT / BINARY.",
             "",
             "| case | lane | scale | runs? | span | rows | core | blocked core | dominant blocker | all blocked families |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for p in sorted(P, key=lambda p: (-p["blocked_core"], p["id"])):
        lines.append(f"| `{p['id']}` {p['name']} | {p['lane']} | {p['scale']} | "
                     f"{'yes' if p['runnable'] else 'NO'} | {p['span']} | {p['n_rows']} | "
                     f"{p['n_core']} | **{p['blocked_core']}** | "
                     f"{p['top_block'] or '—'} | {', '.join(p['blocked']) or '—'} |")
    (OUT / "CASE_PROFILES.md").write_text("\n".join(lines) + "\n")
    log("ARTIFACT", f"wrote runs/CASE_PROFILES.md — {len(P)} rows")
    return dict(n=len(P), dominant_blocker=dict(top),
                unblocked=[p["id"] for p in clean],
                blocked_core_hist=dict(depth), signatures=len(sig),
                worst=[(p["id"], p["blocked_core"]) for p in worst])
