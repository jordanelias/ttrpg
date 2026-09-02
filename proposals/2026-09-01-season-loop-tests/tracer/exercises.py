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
    <kind>        an Event kind (`record.created`). Satisfied when SOME `emits:` COLUMN OF PART D
                  OR PART E DECLARES IT -- a static table lookup, NOT a run.

⚠ THE KIND TOKEN IS THE WEAKEST OF THE FOUR AND ITS OLD DESCRIPTION OVERSTATED IT. This line read
*"satisfied when the kind appears in a run"*, which is what a reader of `CASELOG_*.md` would take
a PASS on such a row to mean. It never was: `resolve` computes membership in the union of
`emits:`/`emits_on_refusal:` over the verb table and the write matrix, so `term.matured` passes
because some Part D row LISTS that kind, not because anything matured. The gap was on the side
that flatters the shape, which is the direction §42.2's polarity rule is about. **`W4` is the item
that closes it** -- it makes every MATTER write emit its declared kind, at which point a run-level
check has something to observe; today 25 of the 40 declared kinds are emitted by nothing (measured:
`python headless.py --case NPC-088 --seasons 2 --seed 0` against `shape.MATRIX`). The `detail`
string and the caselog now say "declared" rather than "emitted" so no reader has to know this.

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

from register import REG_ID_RE as REG_ID

HERE = Path(__file__).resolve().parent
OVERLAY = HERE.parent / "cases" / "exercises"


def need_sha(need: str) -> str:
    """The binding key: the whitespace-normalised need, sha256, first 12 hex. Normalised because
    the corpus wraps mid-sentence and a re-wrap is not a re-wording."""
    return hashlib.sha256(re.sub(r"\s+", " ", need).strip().encode()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# THE THREE THINGS THAT MAY BE DONE WITH A NEED'S TEXT, AND THERE ARE NO OTHERS.
#
# ⚠ THIS SECTION EXISTS BECAUSE THE GUARD NEEDED A BOUNDARY TO BE TOTAL AGAINST. `W10`'s claim is
# that NO VERDICT TURNS ON A NEED'S PROSE. A guard for that has to scan every module that can move
# a verdict -- including `report.py`, which is the sole emitter -- and `report.py` legitimately
# escapes a need for a markdown cell and tokenises one for a printed frequency table. With those
# operations written inline, the guard could only be made to pass by scoping it away from the file,
# and a filename roster is the same defect as a word roster (`G2`).
#
# So the operations get ONE OWNER each, named, here, next to the binding. `CLAUDE.md` §8: never
# re-implement a rule; build on the single-owner primitive. A reader auditing "what can this
# codebase do with a case's prose?" reads three functions instead of grepping for `.lower()`.
# ---------------------------------------------------------------------------

def need_display(need: str, width: int | None = None) -> str:
    """RENDER a need into a markdown table cell. Escapes the column separator and truncates.

    Deciding nothing is the whole point: this is the only way a need's text may reach an
    artifact, and it is a declared sanitizer so the taint check can tell rendering from routing."""
    out = need.replace("|", "\\|")
    return out[:width] if width else out


def need_terms(need: str, *, stop: set[str], min_len: int = 5) -> list[str]:
    """TOKENISE a need for the printed vocabulary table in `UNMAPPED_*.md`.

    ⚠ THIS IS THE ONE ROUTER-SHAPED OPERATION LEFT IN THE CODEBASE, AND IT IS SAFE ONLY BECAUSE
    ITS OUTPUT IS PRINTED AND NEVER READ BACK. It is given one owner, and named, precisely so that
    stays checkable: if a verdict ever starts depending on this function's output, the dependency
    is a call to a function whose docstring says it must not have one. `report.py` says the same
    thing to the reader of the artifact."""
    out = []
    for w in need.lower().replace("-", " ").split():
        w = "".join(ch for ch in w if ch.isalpha())
        if len(w) >= min_len and w not in stop:
            out.append(w)
    return out


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
            # ⚠ THE HUMAN-READABLE `need:` MUST AGREE WITH THE KEY IT SITS BESIDE. `load()` read
            # only `need_sha`, so the text a reviewer judges the declaration BY was bound to
            # nothing — the residue of the very paraphrase defect the sha was added to fix. A
            # reviewer reading a stale `need:` would be checking the declaration against the
            # wrong row.
            if row.get("need") and need_sha(row["need"]) != sha:
                raise SystemExit(
                    f"{f.name}: {cid}'s `need:` text hashes to {need_sha(row['need'])}, not the "
                    f"{sha} it is filed under -- the readable text and the binding disagree")
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


def orphan_cases(overlay: dict, cases: list) -> list:
    """Overlay files whose `case:` id matches NO case in the corpus at all.

    ⚠ `unbound` CANNOT SEE THESE, BY CONSTRUCTION. It is called once per lane, and an id from
    the other lane is legitimately absent from the lane being checked -- so it `continue`s past
    an id it does not recognise. A file naming a case that exists in NEITHER lane therefore
    passed BOTH checks: every row bound to nothing, silently, which is the exact defect
    `need_sha` was added to end one level down. Pass both lanes' cases here and the excuse is
    gone. Found by the `W10` adversarial pass."""
    known = {c["id"] for c in cases}
    return sorted(cid for cid in overlay if cid not in known)


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
    every = []
    for kind in ("NPC", "ARC"):
        cs = R.load_cases(kind)
        every += cs
        c = coverage(ov, cs)
        print(f"{kind}: {c['authored']}/{c['rows']} rows authored "
              f"({c['core_authored']}/{c['core']} core)")
        for cid, sha, need in unbound(ov, cs):
            print(f"  ⚠ UNBOUND {cid} {sha}: {need!r} matches no live row")
    for cid in orphan_cases(ov, every):
        print(f"  ⚠ ORPHAN FILE: `case: {cid}` exists in neither lane -- every row of that file "
              f"is bound to nothing")


# ---------------------------------------------------------------------------
# TOKEN RESOLUTION -- the declared path from a row to a verdict.
#
# ⚠ NO TOKEN IS MATCHED AGAINST THE NEED TEXT. That is the whole of `W10`: the binding is
# AUTHORED, so a row that reaches the wrong probe is an authoring error somebody can see and
# argue with, not a regex that fired on a common word. §7.4's sixth recurrence -- `threat` not
# being on a list, so two rows naming the same L3 refusal routed to nothing -- is unrepresentable
# here, because there is no list of words.
# ---------------------------------------------------------------------------

def classify(token: str) -> str:
    """Which of the four shapes a token is. Derived from the token, never from a roster of
    names: `probe:` is prefixed, a hole id matches `H-NN`, an Event kind carries a dot, and
    anything else is a verb -- which the resolver then checks against the table rather than
    assuming."""
    if token.startswith("probe:"):
        return "probe"
    # The id shape has ONE owner: `register.py`, which validates it. Re-deriving it here
    # made `H-100` classify as a hole and fail validation — CLAUDE.md §8, "never
    # re-implement a rule", one module apart.
    if re.fullmatch(REG_ID, token):
        return "hole"
    if "." in token:
        return "kind"
    return "verb"


def resolve(token: str, *, probes, verb_table, resolvable, register, matrix) -> dict:
    """One token -> `{ok, bound, kind, detail}`. `ok=False` is a GAP for the row that declares it.

    ⚠ `bound` AND `ok` ARE DIFFERENT QUESTIONS, and the binding guard needs the first.
    `bound=False` means THE TOKEN NAMES NOTHING -- no such probe, no such register row, no such
    verb -- which is an AUTHORING error: somebody typed an id that does not exist, and no verdict
    computed from it means anything. `ok=False` with `bound=True` is the opposite and is the
    instrument working: the token named a real thing and that thing is `absent`, unexecutable, or
    gapping. The guard used to tell them apart by MATCHING THREE OF THIS FUNCTION'S FOUR failure
    strings, so a token naming a nonexistent Event kind was unguarded and a reworded message would
    have silently disarmed the rest. `PLAN.md` `G3`: assert the PROPERTY, never the string.

    A HOLE token is the interesting case and the reason `exercises:` admits one at all: a row
    whose need rests on an `absent` register row is BLOCKED BY THE REGISTER, and saying so
    directly is more honest than routing it to a probe that happens to raise. `assumption` is
    admitted and reported -- the row runs on an injected default, which is a real dependency and
    not a blocker."""
    what = classify(token)
    if what == "probe":
        pid = token.split(":", 1)[1]
        if pid not in probes:
            return dict(ok=False, bound=False, kind=what, detail=f"no probe {pid!r} exists")
        v = probes[pid]
        return dict(ok=v["verdict"] == "PASS", bound=True, kind=what,
                    detail=f"{pid}: {v['verdict']}", probe=pid, verdict=v["verdict"])
    if what == "hole":
        row = register.get(token)
        if row is None:
            return dict(ok=False, bound=False, kind=what, detail=f"no register row {token}")
        g = row.get("grade")
        # ⚠ AN `assumption` IS NOT A PASS, AND TREATING IT AS ONE PUBLISHED SEVEN FALSE PASSES.
        # The first version was `ok = g not in ("absent",)`, so a row resting on an INJECTED
        # DEFAULT read as satisfied. The worked case: NPC-005's "full deniability as an
        # achievable outcome" declared `H-33`, whose default is TOTAL FAN-OUT -- the exact
        # NEGATION of the need -- and the caselog printed PASS while the row's own `from:` said
        # "there is no mechanism by which anyone could be excluded". `PLAN.md` `G1`: a fill off
        # the register is a red test, and an assumption rendered as a pass is that fill wearing a
        # verdict. §42.2's polarity rule says the same thing about evidence: an injected default
        # is not evidence the design does the thing.
        #
        # THREE STATES, NOT TWO. `absent` blocks; `assumption` is ASSUMED -- the row runs, on
        # something nobody ratified, and the case is DEGRADED rather than PLAYABLE; `ruled` and
        # `measured` pass. Found by the `W10` adversarial pass.
        if g == "absent":
            return dict(ok=False, bound=True, kind=what, detail=f"{token}: absent", grade=g)
        if g == "assumption":
            return dict(ok=True, assumed=True, bound=True, kind=what, grade=g,
                        detail=f"{token}: assumption -- rests on an injected default")
        return dict(ok=True, bound=True, kind=what, detail=f"{token}: {g}", grade=g)
    if what == "kind":
        # ⚠ THE UNION OVER BOTH TABLES, NOT A HARDCODED WORD. This read
        # `token in emitted or token == "term.matured"` -- A ONE-ELEMENT KIND LIST IN A PYTHON
        # BODY, added by hand, in the commit that DELETED the regex router for exactly that
        # habit and quoted the ruling against it in its own docstring. `PLAN.md` §8.2: "Do not
        # add another word to a router's roster." Jordan, 2026-09-02: "a kind list ... written as
        # a literal in a Python body is a defect, whatever else is true of it."
        #
        # And the primitive was already loaded. Part D's `emits:` column carries every MATTER
        # emission -- `term.matured`, `record.expired`, `condition.band_crossed`, `claim.decayed`
        # and thirty more -- so composing on `MATRIX` covers all of them and moves when the data
        # moves. The hand-added word covered one and would have produced a spurious blocker on
        # any of the rest. Found by the `W10` adversarial pass.
        #
        # AND THE DETAIL NOW AGREES WITH THE VERDICT. The old one computed `ok` with the special
        # case and the message without it, so `results.json` published
        # "term.matured: not in any emits:" beside a PASS -- the exact shape `G3` forbids.
        emitted = {k for r in verb_table.values() for k in (r.emits or ())}
        emitted |= {k for r in verb_table.values() for k in (r.emits_on_refusal or ())}
        emitted |= {k for r in matrix.values() for k in (r.emits or ())}
        # `bound` and `ok` COINCIDE HERE AND NOWHERE ELSE, deliberately: a kind that appears in
        # no `emits:` column names nothing at all, so its failure is an AUTHORING error rather
        # than a finding about the design. Every other shape can name something real and still
        # fail (`absent`, an unexecutable verb, a gapping probe), and conflating the two is what
        # let the binding guard check three of four branches.
        # ⚠ "declared", NOT "emitted". This is a STATIC TABLE LOOKUP and the word `emitted` told
        # every reader of the caselog it was a run. See the module docstring: `W4` is what turns
        # this into a claim about a run.
        return dict(ok=token in emitted, bound=token in emitted, kind=what,
                    detail=f"{token}: {'declared in an emits: column (static, not a run)' if token in emitted else 'on no emits: column'}")
    if token not in verb_table:
        return dict(ok=False, bound=False, kind="verb",
                    detail=f"{token!r} is on no verb-table row")
    if token not in resolvable:
        row = verb_table[token]
        missing = []
        if (row.requires or "").strip() not in ("—", "-", ""):
            missing.append("a `requires:` predicate")
        if row.writes:
            missing.append("an effect")
        return dict(ok=False, bound=True, kind="verb",
                    detail=f"{token!r} is on the table and the fold cannot execute it: needs "
                           + " and ".join(missing or ["an unknown half"]))
    return dict(ok=True, bound=True, kind="verb", detail=f"{token!r} executes")
