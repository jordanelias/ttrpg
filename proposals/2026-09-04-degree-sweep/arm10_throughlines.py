"""ARM 10 -- WHAT THE 143 CASES ASK FOR, RANKED, AGAINST WHAT THE ENGINE SUPPLIES.

⚠ JORDAN, 2026-09-04: *"What are the throughlines/patterns/commonalities amongst the suite of
tests for each NPC or arc?"* and, before it, *"What is the takeaway, though? Just running
everything isn't enough to discuss what needs extending, fixing, etc."*

This arm is the answer to both, and it is the only arm that produces a WORK LIST rather than a
measurement. Every other arm asks "does X work". This asks "how many cases care".

METHOD, stated so it can be disagreed with. Each case carries `season_requires:` rows -- prose
statements of a mechanical capability the case needs. 972 rows across 143 cases. Each row is
matched against thirteen keyword families; a row may match more than one. The families are the
recurring demands, not a taxonomy anyone authored, and the regexes are printed with the counts so
a reader can re-cut them.

⚠ THIS IS A KEYWORD SCAN OVER PROSE AND IT IS NOT A PARSE. It will miss a row that phrases a
demand unusually and will over-count one that uses a family word incidentally. It is reported as
a ranking of PRESSURE, not as a census. The engine-status column beside it is measured by the
other arms and cited to them.
"""
from __future__ import annotations
import collections, re
import sweep_core as K
from sweep_core import S, C, R, Log

FAMILIES = {
    "accumulator/clock":      r"accumulat|counter|clock|tick|per period|each season|per season|increment",
    "belief/knowledge":       r"\bknow\b|knowledge|believe|unaware|hidden|secret|invisible|discover|learn",
    "threshold crossing":     r"threshold|crosses|reaches a (set|certain) level|tips|at or below|at or above",
    "roll/contest":           r"\broll\b|contest|opposed|check against|succeed or fail|failable|attempt.*fail",
    "observability":          r"observ|visible|trackable|players must be able to see|detect",
    "relationship/loyalty":   r"loyalt|trust|relationship|standing with|opinion of|affection",
    "investigation":          r"investigat|evidence|corrobor|uncover|fieldwork|inquiry|witness",
    "memory/persistence":     r"remember|memory|persist|carry (over|forward)|later period|previously",
    "social/speech":          r"persuad|argue|accus|testimon|rumour|rumor|tell|speak|convince|reputation",
    "irreversibility":        r"cannot be (undone|reversed)|never decrease|irrevers|no way to.*decrease|permanent",
    "DEGREE/partial outcome": r"partial|degree|margin|overwhelm|narrowly|barely|extent of success|how well",
    "third-party substitute": r"another actor|third party|someone else|a different (actor|faction)|step in",
    "resource depletion":     r"deplet|exhaust|unaffordab|run out|falls low|cost.*resource",
}

# Engine status per family, each cited to the arm that measured it. NOT asserted from reading.
STATUS = {
    "belief/knowledge": ("SEVERED",
        "arm 9d — claims are deposited (4,800 measured) and `belief_contradicts` cannot read any "
        "of them: the predicate vocabularies are disjoint and no claim is falsy"),
    "roll/contest": ("ABSENT",
        "arm 0 — the contest seam is never reached; zero DESIGN-GAP and zero INSTRUMENT-DEFECT "
        "confirm none was attempted-and-refused either"),
    "DEGREE/partial outcome": ("ABSENT",
        "arms 0 and 5b — no act resolves at a degree; 12 of 12 interpersonal verbs carry no "
        "degree column"),
    "investigation": ("INERT",
        "arm 5b/6 — `the six investigation acts` is ONE row with `writes: []` and no `contests:`; "
        "the split into six degree-emitting rows is HANDOFF_NEXT row 2b, prescribed and unbuilt. "
        "The subsystem side is a stub too: social_contest's `inquiry` game is STUB"),
    "third-party substitute": ("BLOCKED BY belief/knowledge",
        "arm 9 — a third party taking over requires the world to be readable by deliberation, "
        "which is the severed edge above"),
    "social/speech": ("BINARY",
        "arm 5b — `speak`, `tell`, `refract`, `comply`, `evade / defy` write no state and carry "
        "no degree; the act emits and nothing follows from how well it went"),
    "accumulator/clock": ("PARTIAL",
        "arm 0 — `S24` (a Date coming due) fires in 11 of 143 cases; `Rung.stores` exists and "
        "moves. The mechanism is present and thinly exercised"),
    "threshold crossing": ("PARTIAL",
        "`band_floors` / `body_band_penalty` exist and `combat_seam` reads them; arm 7 shows "
        "state-threshold divergence is reachable"),
    "observability": ("PRESENT",
        "the View/Query side column exists and is enforced person-side"),
    "relationship/loyalty": ("THIN",
        "`convictions` and `stance_toward` are consumed by the chooser, but `align` is sparse "
        "with `default_cell: 0.0`, so only 2..7 of 22 candidates carry a nonzero score and the "
        "rest tie and sort alphabetically"),
    "memory/persistence": ("PRESENT",
        "the append-only log and the per-person ledger both persist across seasons"),
    "irreversibility": ("PRESENT",
        "`Proposition` is a frozen dataclass; `Tenure.until` closes and does not reopen"),
    "resource depletion": ("PRESENT",
        "`Rung.stores` is written by `transfer`/`levy`/`exchange` behind a `stores >= amount` "
        "precondition"),
}

BLOCKED = {"SEVERED", "ABSENT", "INERT", "BLOCKED BY belief/knowledge", "BINARY"}


def run(log: Log) -> dict:
    log.rule("ARM 10 — THROUGHLINES: what the 143 cases ask for, and what the engine supplies")
    rows = []
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            for r in (c.get("season_requires") or []):
                rows.append((lane, c["id"], r.get("hardness", "?"), str(r.get("need", ""))))
    cases = {cid for _, cid, _, _ in rows}
    hard = collections.Counter(h for _, _, h, _ in rows)
    log("SCOPE", f"{len(rows)} `season_requires` rows across {len(cases)} cases "
                 f"(mean {len(rows)/len(cases):.1f} per case)")
    log("SCOPE", f"hardness: {dict(hard)}",
        "`core` is the case's own word for a requirement without which the case is not the case")
    log("METHOD", "thirteen keyword families over the `need:` prose; a row may match more than "
                  "one. A SCAN, not a parse — a ranking of pressure, not a census.")

    fam_rows = collections.Counter(); fam_core = collections.Counter()
    fam_cases = collections.defaultdict(set)
    for lane, cid, h, need in rows:
        n = need.lower()
        for fam, pat in FAMILIES.items():
            if re.search(pat, n):
                fam_rows[fam] += 1
                fam_cases[fam].add(cid)
                if h == "core":
                    fam_core[fam] += 1

    log.rule("ARM 10a — the demand, ranked by how many CASES need it")
    out = {}
    for fam, _ in sorted(fam_cases.items(), key=lambda kv: -len(kv[1])):
        st, why = STATUS.get(fam, ("?", ""))
        out[fam] = dict(rows=fam_rows[fam], core_rows=fam_core[fam],
                        cases=len(fam_cases[fam]), status=st, why=why)
        log("DEMAND", f"{fam:24} {len(fam_cases[fam]):3} cases · {fam_rows[fam]:4} rows "
                      f"({fam_core[fam]:3} core) · ENGINE: {st}")

    log.rule("ARM 10b — THE WORK LIST: demand the engine cannot meet, ranked")
    blocked = [(f, d) for f, d in out.items() if d["status"] in BLOCKED]
    blocked.sort(key=lambda kv: -kv[1]["cases"])
    n_cases_blocked = len(set().union(*[fam_cases[f] for f, _ in blocked])) if blocked else 0
    for f, d in blocked:
        log("FIX", f"{f:24} wanted by {d['cases']:3} of {len(cases)} cases "
                   f"({d['core_rows']} core rows) — {d['status']}")
        log("", f"     {d['why']}")
    log("MEASURE", f"cases touching at least one blocked family: {n_cases_blocked} of {len(cases)} "
                   f"({n_cases_blocked/len(cases)*100:.0f}%)")

    log.rule("ARM 10c — THE TAKEAWAY, and it is one bug in three places")
    for line, why in [
        ("the loop is OPEN. Acts happen, the world changes, and nothing that happened can alter "
         "what anyone decides next.",
         "arm 9: 2,403 forks, every one changing the act and the log, none changing the next "
         "three decisions"),
        ("EDGE 1 — belief -> decision. SEVERED, and it is the bottleneck.",
         "`belief_contradicts` needs `predicate in PERSON_PREDICATES AND value is False`. The "
         "corpus deposits `travel.blocked value=True` and ten others; the vocabularies are "
         "disjoint and nothing is falsy. `H-72`/`F.24`/`H-94` register it. Fix this FIRST — "
         "every other fix is inert without it, because a consequence that cannot reach a "
         "decision is a log line."),
        ("EDGE 2 — outcome -> magnitude. ABSENT.",
         "one contested verb, not foldable; 3 of 4 declared prizes claimed by no verb; 12 of 12 "
         "interpersonal verbs degreeless. HANDOFF_NEXT row 2b is the built form for "
         "investigation. Worth doing SECOND: a degree is a magnitude on an edge that must exist "
         "first."),
        ("EDGE 3 — world -> belief. PRESENT AND CARRYING THE WRONG PAYLOAD.",
         "WITNESS deposits 339,804 claims, so the channel works. But they carry event-kind "
         "predicates (`speech.made`, `travel.blocked`) — descriptions of what happened — rather "
         "than propositions that could contradict a requirement. This is the cheapest of the "
         "three and may be the shortest path to closing edge 1."),
    ]:
        log("TAKEAWAY", line, why)
    log("⚠ THE ONE WORTH ACTING ON", "the design's OWN worked example is one type mismatch from "
                                      "running.",
        "`opening_set`'s docstring: 'a person who *wrongly* believes the granary full still forms "
        "the Candidate, acts, and gets `transfer.refused` from the fold. That is T3 and L2 "
        "working.' The fold DOES deposit that refusal. `belief_contradicts` cannot read it — "
        "wrong predicate namespace, and recorded `value=True` ('it is true that this was "
        "refused') where the reader wants False. The feedback loop this design describes is "
        "already deposited and already unread.")
    return dict(n_rows=len(rows), n_cases=len(cases), hardness=dict(hard),
                families=out, blocked=[f for f, _ in blocked],
                cases_touching_blocked=n_cases_blocked)
