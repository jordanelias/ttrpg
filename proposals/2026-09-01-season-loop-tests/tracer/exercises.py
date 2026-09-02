"""DECLARED ROUTING — `W10`. The `exercises:` overlay, and the only path from a case row to a
verdict now that the regex router is gone.

> `PLAN.md` `W10`: *"Every `season_requires` row gains `exercises: [<verb> | <contract §> |
> <H-id>]`, authored with the row. Delete `ROUTES*` and `COMPILED` from `run_cases.py`;
> `route_precision.py` retires with them. **NOT-ASSESSED then means 'nobody authored an
> `exercises:`'** — a fact about authoring, which is fixable — instead of 'the regex missed',
> which is not."*

⚠ WHY THE ROUTER HAD TO GO RATHER THAN GROW. `PLAN.md` §7.4 records the SIXTH recurrence of the
bare-token class, found while the plan was being written: `EMG-C2` and `NSC-09` both name an
"institutional threat value", both are the same L3 refusal, and both routed to NOTHING because
`threat` was not on a list. Its verdict is the one this file implements: *"the fix is NOT to add
`threat`. Adding the word is what was done at recurrences two, three and four. The fix is `W10`:
delete the router. A roster of words IS a specification, and nobody ratified this one."*

⚠ AND THE COUNT THE ROUTER PUBLISHED WAS A FLOOR, NOT A TOTAL. Rows that matched no pattern fell
silently to UNMAPPED, so every figure derived from routing understated the corpus in the direction
that flattered it. Declared routing cannot do that: a row with no `exercises:` is VISIBLY
unauthored.

WHAT A TOKEN MAY BE, and what each resolves to:

    <verb>        a row of `verb_table.yaml`. Resolves by asking the fold whether it can EXECUTE
                  it -- both a `requires:` predicate and, if it writes, an effect. A declared verb
                  the fold cannot run is a GAP for that row, and it names which half is missing.
    H-NN          a row of `hole_register.yaml`. `absent` is a blocker; `assumption` is a
                  dependency on an injected default; `ruled`/`measured` are satisfied.
    probe:PID     a probe. Runs it and takes its verdict. This is the ONLY token that reaches a
                  probe, and it is authored per row rather than matched.
    <kind>        an Event kind (`record.created`). Satisfied when the kind appears in a run.

BINDING IS BY THE NEED TEXT, NOT BY POSITION. Each entry carries `need_sha`, the first 12 hex of
the sha256 of the whitespace-normalised need. If a case row is reworded the binding FAILS LOUDLY
rather than silently annotating a different row -- which is the defect the `W9` adversarial pass
found in the NPC-088 overlay, where nothing tied the file to the corpus at all.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
OVERLAY = HERE.parent / "cases" / "exercises"


def need_sha(need: str) -> str:
    """The binding key: the whitespace-normalised need, sha256, first 12 hex. Normalised because
    the corpus wraps mid-sentence and a re-wrap is not a re-wording."""
    return hashlib.sha256(re.sub(r"\s+", " ", need).strip().encode()).hexdigest()[:12]


def load() -> dict:
    """Every overlay file, as `{case_id: {need_sha: entry}}`. Raises on a duplicate binding, so
    two files cannot annotate one row with different answers."""
    out: dict = {}
    for f in sorted(OVERLAY.glob("*.yaml")):
        doc = yaml.safe_load(f.read_text()) or {}
        cid = doc.get("case")
        if not cid:
            raise SystemExit(f"{f.name}: no `case:` key")
        bucket = out.setdefault(cid, {})
        for row in doc.get("rows") or []:
            sha = row.get("need_sha")
            if not sha:
                raise SystemExit(f"{f.name}: a row has no `need_sha` -- the binding would be "
                                 "positional, which is what W9's pass found wrong with the "
                                 "first overlay")
            if sha in bucket:
                raise SystemExit(f"{f.name}: duplicate binding for {sha} in {cid}")
            bucket[sha] = row
    return out


def unbound(overlay: dict, cases: list) -> list:
    """Overlay entries whose `need_sha` matches no row of their case. A reworded corpus row
    orphans its annotation, and this is what makes that LOUD rather than silent."""
    by_id = {c["id"]: c for c in cases}
    bad = []
    for cid, rows in overlay.items():
        case = by_id.get(cid)
        if case is None:
            continue                      # a case from the other lane; checked when that lane runs
        live = {need_sha(r.get("need", "")) for r in (case.get("season_requires") or [])}
        for sha, row in rows.items():
            if sha not in live:
                bad.append((cid, sha, str(row.get("need", ""))[:60]))
    return bad


def coverage(overlay: dict, cases: list) -> dict:
    """How much of a lane is authored. A number this instrument publishes, so it ships with the
    command that produces it: `python exercises.py`."""
    rows = core = have = core_have = 0
    for c in cases:
        bucket = overlay.get(c["id"], {})
        for r in (c.get("season_requires") or []):
            need = r.get("need", "")
            if re.match(r"\s*UNCLEAR\b", need, re.I):
                continue
            rows += 1
            is_core = r.get("hardness") == "core"
            core += is_core
            if bucket.get(need_sha(need), {}).get("exercises"):
                have += 1
                core_have += is_core
    return dict(rows=rows, authored=have, core=core, core_authored=core_have)


if __name__ == "__main__":
    import run_cases as R
    ov = load()
    for kind in ("NPC", "ARC"):
        cs = R.load_cases(kind)
        c = coverage(ov, cs)
        print(f"{kind}: {c['authored']}/{c['rows']} rows authored "
              f"({c['core_authored']}/{c['core']} core)")
        for cid, sha, need in unbound(ov, cs):
            print(f"  ⚠ UNBOUND {cid} {sha}: {need!r} matches no live row")


# ---------------------------------------------------------------------------
# TOKEN RESOLUTION -- the declared path from a row to a verdict.
#
# ⚠ NO TOKEN IS MATCHED AGAINST THE NEED TEXT. That is the whole of `W10`: the binding is
# AUTHORED, so a row that reaches the wrong probe is an authoring error somebody can see and
# argue with, not a regex that fired on a common word. §7.4's sixth recurrence -- `threat` not
# being on a list, so two rows naming the same L3 refusal routed to nothing -- is unrepresentable
# here, because there is no list of words.
# ---------------------------------------------------------------------------

TOKEN_KINDS = ("probe", "verb", "hole", "kind")


def classify(token: str) -> str:
    """Which of the four shapes a token is. Derived from the token, never from a roster of
    names: `probe:` is prefixed, a hole id matches `H-NN`, an Event kind carries a dot, and
    anything else is a verb -- which the resolver then checks against the table rather than
    assuming."""
    if token.startswith("probe:"):
        return "probe"
    if re.fullmatch(r"H-\d+", token):
        return "hole"
    if "." in token:
        return "kind"
    return "verb"


def resolve(token: str, *, probes, verb_table, resolvable, register) -> dict:
    """One token -> `{ok, kind, detail}`. `ok=False` is a GAP for the row that declares it.

    A HOLE token is the interesting case and the reason `exercises:` admits one at all: a row
    whose need rests on an `absent` register row is BLOCKED BY THE REGISTER, and saying so
    directly is more honest than routing it to a probe that happens to raise. `assumption` is
    admitted and reported -- the row runs on an injected default, which is a real dependency and
    not a blocker."""
    what = classify(token)
    if what == "probe":
        pid = token.split(":", 1)[1]
        if pid not in probes:
            return dict(ok=False, kind=what, detail=f"no probe {pid!r} exists")
        v = probes[pid]
        return dict(ok=v["verdict"] == "PASS", kind=what,
                    detail=f"{pid}: {v['verdict']}", probe=pid, verdict=v["verdict"])
    if what == "hole":
        row = register.get(token)
        if row is None:
            return dict(ok=False, kind=what, detail=f"no register row {token}")
        g = row.get("grade")
        return dict(ok=g not in ("absent",), kind=what, detail=f"{token}: {g}", grade=g)
    if what == "kind":
        emitted = {k for r in verb_table.values() for k in (r.emits or ())}
        emitted |= {k for r in verb_table.values() for k in (r.emits_on_refusal or ())}
        # MATTER's own emissions are not in the verb table; the register carries them as rows.
        return dict(ok=token in emitted or token == "term.matured", kind=what,
                    detail=f"{token}: {'emitted' if token in emitted else 'not in any emits:'}")
    if token not in verb_table:
        return dict(ok=False, kind="verb", detail=f"{token!r} is on no verb-table row")
    if token not in resolvable:
        row = verb_table[token]
        missing = []
        if (row.requires or "").strip() not in ("—", "-", ""):
            missing.append("a `requires:` predicate")
        if row.writes:
            missing.append("an effect")
        return dict(ok=False, kind="verb",
                    detail=f"{token!r} is on the table and the fold cannot execute it: needs "
                           + " and ".join(missing or ["an unknown half"]))
    return dict(ok=True, kind="verb", detail=f"{token!r} executes")
