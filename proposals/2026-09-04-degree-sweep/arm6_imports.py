"""ARM 6 -- WERE THE v2 SYSTEMS MARKED FOR IMPORT ACTUALLY IMPORTED?

⚠ JORDAN ASKED THIS DIRECTLY, 2026-09-04: *"It appears that the discovery system (and possibly
other systems) from v2 that were identified as valuable to import we're not?"*

Answered against the tree rather than against the PR bodies, because the PR bodies are what the
question is about. The prescription is `architecture/meta/HANDOFF_NEXT.md`
§2 -- which calls itself ***"this is the real backlog"*** -- crossed with #359's design-v2.
"""
from __future__ import annotations
from pathlib import Path
import yaml
from sweep_core import Log

_REPO = Path("/home/user/ttrpg")
VT = _REPO / "engine/season/verb_table.yaml"

# HANDOFF_NEXT.md §2, verbatim subjects. Each row: (id, what it is, what blocks, the probe).
ROWS = [
    ("2a", "a generic `release` verb (#358 §A.3 row 14)",
     "defect · betray · breaking a treaty · releasing a guarantee — AND a person cannot resign "
     "an office, a direct T-m violation", "verb"),
    ("2b", "`the six investigation acts` split into six rows with writes",
     "expose · Investigate — discovery is inert. #359's discovery model (a contest of capability "
     "against secrecy, EMITTING A DEGREE) is the shape", "six"),
    ("2c", "`determine` graded, `judging_set` as a Query",
     "vote — nothing is decided at a sitting", "determine"),
    ("2d", "a founding verb writing `Rung.exists` / `Site.exists`",
     "incorporation · building a holding — F.20: the world only decays", "founding"),
    ("2e", "⚠ NOT a `bargain` verb — the handoff says 'test composability FIRST … adding a verb "
           "is the LAST resort, not the first'. The prescribed deliverable is the COMPOSABILITY "
           "TEST (does `utter` a counter-OUGHT + `commit` already express it?)",
     "the third response at every tier", "composability"),
]


def run(log: Log) -> dict:
    log.rule("ARM 6 — the v2 systems marked for import, checked against the tree")
    log("SOURCE", "architecture/meta/HANDOFF_NEXT.md §2 — "
                  "'The five root causes that block #359's actions — ⚠ this is the real backlog'")
    log("SOURCE", "proposals/2026-09-03-governance-corpus-rebuild/03-design-v2.md §discovery — "
                  "'Discovery is a contest — the investigator's relevant capability against the "
                  "scheme's `secrecy` — emitting a `Degree` like everything else'")
    vt = yaml.safe_load(VT.read_text())
    rows = {str(r.get("verb")): r for r in vt["verbs"]}
    names = set(rows)
    out = {}
    for rid, what, blocks, probe in ROWS:
        if probe == "verb":
            # ⚠ A SUBSTRING MATCH ON A VERB NAME IS A WEAK PROBE and is labelled as one: it would
            # report ABSENT for a correct mechanism under another name. The CONCEPT was checked by
            # hand for 2a — `repudiate` closes only a `commit`, `revoke` needs a remit — so no
            # self-resignation path exists and ABSENT is right. The probe did not establish that.
            hit = sorted(x for x in names if "release" in x.lower())
            state = (f"PRESENT {hit}" if hit else
                     "ABSENT (name probe; concept checked by hand — `repudiate` closes only a "
                     "`commit` and `revoke` needs a remit, so no self-resignation path exists)")
        elif probe == "six":
            r = rows.get("the six investigation acts")
            state = ("NOT SPLIT — still ONE row: writes=%r contests=%r grade=%r"
                     % (r.get("writes"), r.get("contests"), r.get("grade"))) if r else "ABSENT"
        elif probe == "determine":
            # ⚠ THE PRESCRIPTION IS `judging_set` AS A QUERY IN `shape.py`, not a verb-table
            # grade, and an earlier draft probed only the grade. Both are checked now.
            r = rows.get("determine")
            try:
                import shape as _S
                js = hasattr(_S.Query, "judging_set") or "judging_set" in dir(_S)
            except Exception:
                js = None
            state = (("`determine` grade=%r contests=%r; `judging_set` as a Query in shape.py: %s"
                      % (r.get("grade"), r.get("contests"),
                         "PRESENT" if js else "ABSENT")) if r else "ABSENT")
        elif probe == "composability":
            # ⚠ SCORING THE ABSENCE OF A `bargain` VERB AS AN UNMET DELIVERABLE INVERTS THE
            # PRESCRIPTION, and an earlier draft did exactly that. The handoff deprecates adding
            # a verb. The honest verdict is NOT-TESTED: no artifact anywhere in the chain runs
            # the composability test, this sweep included. Found by the adversarial pass.
            has = sorted(x for x in names if "bargain" in x.lower())
            state = ("NOT TESTED — no `bargain` verb (which the handoff DEPRECATES adding) and "
                     "no composability test for `utter`+`commit` anywhere in the chain, this "
                     "sweep included") if not has else f"a verb was ADDED: {has} — the last resort taken first"
        else:
            prod = [v for v, rr in rows.items()
                    for w in (rr.get("writes") if isinstance(rr.get("writes"), list) else [])
                    if w in ("Rung.exists", "Site.exists")]
            state = f"PRESENT {prod}" if prod else "ABSENT — zero producers"
        if state.startswith("NOT TESTED"):
            done = None                       # neither delivered nor scored — see the note above
        else:
            done = (state.startswith("PRESENT") and "NOT SPLIT" not in state
                    and "grade='absent'" not in state)
        out[rid] = dict(what=what, blocks=blocks, state=state, delivered=done)
        log("ROW", f"{rid}  {what}")
        log("", f"     blocks : {blocks}")
        log("", f"     STATE  : {state}")
    n_done = sum(1 for v in out.values() if v.get("delivered") is True)
    n_untested = sum(1 for v in out.values() if v.get("delivered") is None)
    n_scored = len(ROWS) - n_untested
    log.rule("ARM 6 — verdict")
    log("COUNT", f"{n_done} of {n_scored} SCORABLE root-cause fixes are delivered; "
                 f"{n_untested} is NOT TESTED (2e, whose prescribed deliverable is a "
                 f"composability test nobody has run)",
        "⚠ an earlier draft reported '0 of 5' by counting 2e's missing `bargain` verb as an unmet "
        "deliverable. That inverts the handoff, which deprecates adding the verb. Corrected.")
    log("MEASURE", f"verbs declaring `contests:` : "
                   f"{[v for v, r in rows.items() if r.get('contests')]}",
        "one — and it is the combat verb, not a social one")
    log("VERDICT", "the v2 systems marked valuable were evaluated, ranked and prescribed — and "
                   "not built",
        "PRs #358, #361 and #362 all edited the meta-architecture PROSE. None touched "
        "`verb_table.yaml`: `git diff 2c0ea60..1e163ee -- .../verb_table.yaml` is empty. What "
        "landed in #362 was thirteen edits to a document; what did not land is every one of the "
        "five mechanisms the same handoff calls the real backlog.")
    log("CONSEQUENCE", "2b is the one Jordan named, and it is why investigation is degreeless",
        "the prescription was a discovery CONTEST emitting a Degree. Without it `the six "
        "investigation acts` stays one row with `writes: []`, so investigating and accusing "
        "cannot carry a degree of success no matter what the ladder does.")
    out["_n_delivered"] = n_done
    out["_n_scorable"] = n_scored
    out["_n_untested"] = n_untested
    out["_n_prescribed"] = len(ROWS)
    return out
