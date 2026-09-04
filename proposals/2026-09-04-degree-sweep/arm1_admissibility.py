"""ARM 1 -- ADMISSIBILITY. Hand every token of both ladders to the only degree-keyed verb
and record, per token, exactly what the shape does.

⚠ THIS IS THE ARM THAT CANNOT BE SATISFIED BY WRITING. `VerbRow.writes_at` / `emits_at` either
return a branch or raise a typed gap; the sweep reports the return value or the exception, and
there is no third thing for it to say.
"""
from __future__ import annotations
import sweep_core as K
from sweep_core import S, KW, LADDER_C, LADDER_D, Log


# ⚠ `BaseException`, NOT `Exception`, AND THAT IS ITSELF THE FIRST FINDING.
# `VerbRow.writes_at` / `emits_at` raise `SystemExit`, which does NOT derive from `Exception`.
# A probe written with the ordinary `except Exception` -- which is what `corpus_run.run_case`
# uses, in both its clauses -- does not catch it. This one catches `BaseException` so the sweep
# can REPORT the refusal instead of dying of it, and records which base class was involved so
# the distinction is in the data rather than only in this comment.
def probe_token(row, degree):
    """One token against one verb row. Returns (writes, emits, verdict, detail)."""
    try:
        w = row.writes_at(degree)
    except BaseException as e:
        base = "Exception" if isinstance(e, Exception) else "BaseException-ONLY"
        return None, None, "REFUSED", f"{type(e).__name__} [{base}]: {e}"
    try:
        em = row.emits_at(degree)
    except BaseException as e:
        base = "Exception" if isinstance(e, Exception) else "BaseException-ONLY"
        return w, None, "HALF-ADMITTED", f"writes ok; emits raised {type(e).__name__} [{base}]: {e}"
    return w, em, "ADMITTED", ""


def run(log: Log) -> dict:
    log.rule("ARM 1 — ADMISSIBILITY: does the system accept the degrees Jordan named?")
    log("SETUP", f"contested verbs in the table: {list(K.contested_verbs())}",
        "a verb routes to the degree seam only if it declares `contests:`. There is exactly one.")
    row = S.VERB_TABLE[KW]
    log("SETUP", f"{KW!r} declares contests={row.contests!r}",
        f"so its prize routes to `{S.roster_map('contest_subsystems','prizes').get(row.contests)}`")
    log("SETUP", f"declared degree branches: {sorted(row.writes_by_degree)}",
        "these are the ONLY tokens `writes_at` can select; an unlisted one raises by design "
        "(shape.py: 'an unlisted degree RAISES rather than falling back to the union')")

    out = {"C": {}, "D": {}, "none": {}}

    log.rule("ARM 1a — LADDER C, the canonical four (dice_engine.degree_from_net)")
    log("WHY", K.LADDER_C_WHY)
    for d in LADDER_C:
        w, em, verdict, detail = probe_token(row, d)
        out["C"][d] = dict(verdict=verdict, writes=list(w or []), emits=list(em or []), detail=detail)
        log("INJECT", f"degree={d!r} -> writes_at({d!r})")
        log("RESULT", f"{verdict}" + (f" — {detail}" if detail else f" writes={list(w or [])} emits={list(em or [])}"))

    log.rule("ARM 1b — LADDER D, the declared three (verb_table.yaml `kill / wound`)")
    log("WHY", K.LADDER_D_WHY)
    for d in LADDER_D:
        w, em, verdict, detail = probe_token(row, d)
        out["D"][d] = dict(verdict=verdict, writes=list(w or []), emits=list(em or []), detail=detail)
        log("INJECT", f"degree={d!r} -> writes_at({d!r})")
        log("RESULT", f"{verdict} writes={list(w or [])} emits={list(em or [])}",
            "these are STATE PATHS the fold would write, and they differ per token — so the "
            "declared ladder does carry mechanical consequence, unlike the canonical one above")

    log.rule("ARM 1c — THE CONTROL: a contested verb folded with NO degree at all")
    w, em, verdict, detail = probe_token(row, None)
    out["none"]["<None>"] = dict(verdict=verdict, detail=detail)
    log("INJECT", "degree=None")
    log("RESULT", f"{verdict} — {detail}",
        "the control matters: if a missing degree silently returned the union, every result "
        "above would be indistinguishable from a system with no ladder at all")

    log.rule("ARM 1d — AN UNCONTESTED VERB, the second control")
    for v in ("speak", "work"):
        r2 = S.VERB_TABLE[v]
        w, em, verdict, detail = probe_token(r2, "Overwhelming")
        out.setdefault("uncontested", {})[v] = dict(verdict=verdict, writes=list(w or []))
        log("INJECT", f"verb={v!r} (declares no `contests:`) degree='Overwhelming'")
        log("RESULT", f"{verdict} writes={list(w or [])}",
            "an uncontested verb IGNORES the degree and returns its flat tuple — so passing a "
            "degree to an ordinary verb is silently a no-op, which is the third response class")
    return out
