"""Route every case's `season_requires` rows onto probes, execute, and grade.

THE HONESTY RULES, inherited from the in-chain instrument (#351) because its own report
records what went wrong without them, and re-tightened here:

  1. **Probe verdicts are HARD; case verdicts are ADVISORY.** A probe is an execution. A case
     verdict is a keyword routing over prose, and keyword routing is crude.
  2. **A row that does not route is reported UNMAPPED, never passed.** Silence is not a pass.
  3. **A case more than half of whose `core` rows fail to route is NOT-ASSESSED**, not graded.
     Grading it DECLARED-PRESENT would be the instrument flattering the shape by failing to aim at it.
  4. **Every route matches on WORD BOUNDARIES with explicit negative guards.** #351's most
     expensive correction was a bare substring `ambient` catching ambient-MATERIAL rows (8 -> 3)
     and a bare `counter` matching inside "counter-productive" (10 -> 8). Both are guarded here.
  5. **A probe runs ONCE.** Its verdict is cached, so a case cannot change a probe's result.

A READING RULE for the corpus the loader (`load_cases`, `boot/realm.py`) hands this file: where a case file cites an archived fieldwork term, the parent `fieldwork_v30.md` is the reading of that term, and nothing is built from it without a new design (`08_FI_audit_addendum_B.md` F-FI-13, R-47).
"""

from __future__ import annotations

import re

from ..data.matrix import MATRIX
from ..data.verbs import VERB_TABLE
from ..loop.driver import resolvable_verbs
from ..data import files
from ..gaps import ShapeGap
from ..trace_log import TRACE
from . import exercises as EX
from . import probes as P
from ..boot.realm import CORPUS_DEFECTS, load_cases   # moved to `boot/` (B03c.01); the builder reads both


# ---------------------------------------------------------------------------
# THE ROUTER. (probe_id, regex, negative-guard regex or None)
# Word-boundary anchored. Ordered: the FIRST match wins, so specific precedes general.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# THE REGEX ROUTER IS GONE. `W10`.
#
# `ROUTES` through `ROUTES_5`, `COMPILED` and `route()` stood here -- FIVE ACCRETED TIERS, each
# added after measuring which `core` rows the previous tier missed. That accretion IS the defect:
# `PLAN.md` §7.4 records the SIXTH recurrence of the bare-token class, found while the plan was
# being written, and rules on it in terms -- *"the fix is NOT to add `threat`. Adding the word is
# what was done at recurrences two, three and four. The fix is `W10`: delete the router. A roster
# of words IS a specification, and nobody ratified this one."*
#
# ⚠ AND EVERY COUNT THE ROUTER PUBLISHED WAS A FLOOR. A row matching no pattern fell silently to
# UNMAPPED, so "the ARC refusal count" and every figure derived from routing understated the
# corpus in the direction that flattered it. A row with no `exercises:` is VISIBLY unauthored.
#
# Routing is `exercises.py` now: a per-row declaration, bound to the need text by sha, resolving
# to a verb, a hole id, a probe or an Event kind. NOT-ASSESSED means NOBODY AUTHORED ONE -- a fact
# about authoring, which is fixable -- rather than "the regex missed", which is not.
#
# Recoverable at `git log -S "ROUTES_5"` if the 973 declarations are ever wanted as a starting
# point. They are not: laundering the router's output into declarations would keep every one of
# its errors and make them look ratified.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# EXECUTION -- a probe runs ONCE; its verdict is cached.
# ---------------------------------------------------------------------------

_VERDICTS: dict[str, dict] = {}


def run_probe(pid: str) -> dict:
    if pid in _VERDICTS:
        return _VERDICTS[pid]
    spec = P.PROBES[pid]
    TRACE.case = f"probe:{pid}"
    try:
        msg = spec["fn"]()
        if isinstance(msg, str) and msg.strip() == "UNREACHABLE":
            # The probe expected the shape to REFUSE and it did not. That is never a PASS:
            # it is either a real finding (a refusal ARCHITECTURE.md states is not enforced)
            # or an instrument defect. Both flatter the shape, so both are reported.
            v = dict(id=pid, verdict="NOT-REFUSED", detail=(
                "the shape PERMITTED what this probe expected it to refuse; the refusal named at "
                f"{spec['section']} did not fire"), kind="NOT-REFUSED",
                section=spec["section"], title=spec["title"])
        else:
            v = dict(id=pid, verdict="PASS", detail=msg, kind=None,
                     section=spec["section"], title=spec["title"])
    except ShapeGap as g:
        v = dict(id=pid, verdict="GAP", detail=g.what, kind=g.kind,
                 section=g.where, title=spec["title"], needs=g.needs, law=g.law)
    except AssertionError as e:
        v = dict(id=pid, verdict="INSTRUMENT-ERROR", detail=f"assertion failed: {e!r}",
                 kind=None, section=spec["section"], title=spec["title"])
    except Exception as e:                                  # noqa: BLE001
        v = dict(id=pid, verdict="INSTRUMENT-ERROR", detail=f"{type(e).__name__}: {e}",
                 kind=None, section=spec["section"], title=spec["title"])
    v["by"] = spec["by"]
    v["tests"] = spec["tests"]
    _VERDICTS[pid] = v
    return v


# ---------------------------------------------------------------------------
# CASES
# ---------------------------------------------------------------------------



def _probe_view() -> dict:
    """Every probe's verdict, run once and cached by `run_probe`. Built lazily so a row that
    names no probe never triggers the corpus run."""
    from . import probes as _P
    return {pid: run_probe(pid) for pid in _P.PROBES}


OVERLAY = EX.load()

_REGISTER: dict = {}


def _register() -> dict:
    """`hole_register.yaml` by id. An `exercises:` may name a hole, and an `absent` one blocks the
    row that rests on it -- which is more honest than routing such a row to a probe that happens
    to raise for a different reason."""
    if not _REGISTER:
        from ..data.rosters import load_yaml
        path = files.HOLE_REGISTER_YAML
        for r in (load_yaml(path.read_text()) or {}).get("rows") or []:
            _REGISTER[r["id"]] = r
    return _REGISTER


def grade(case: dict) -> dict:
    rows = case.get("season_requires") or []
    routed, unmapped, unclear = [], [], []
    for r in rows:
        need = r.get("need", "")
        entry = dict(need=need, hardness=r.get("hardness", "important"), probe=None)
        # An `UNCLEAR:` row is the CASE SOURCE failing to say something, not the shape failing
        # to do it. Counting it as UNMAPPED conflates two different failures, and the in-chain
        # brief is explicit that an unclear source IS ITSELF DATA.
        if re.match(r"\s*UNCLEAR\b", need, re.I):
            unclear.append(entry)
            continue
        # DECLARED ROUTING (`W10`). No pattern touches `need`; the binding is an authored
        # `exercises:` keyed by the need's own sha, so a row reaching the wrong answer is an
        # authoring error somebody can argue with rather than a regex firing on a common word.
        decl = OVERLAY.get(case["id"], {}).get(EX.need_sha(need), {})
        tokens = list(decl.get("exercises") or [])
        entry["exercises"] = tokens
        if not tokens:
            unmapped.append(entry)              # NOBODY AUTHORED ONE -- a fact about authoring
            continue
        parts = [EX.resolve(t, probes=_probe_view(), verb_table=VERB_TABLE,
                            resolvable=resolvable_verbs(), register=_register(),
                            matrix=MATRIX)
                 for t in tokens]
        entry["resolved"] = parts
        # The row's verdict is the WORST of its declarations. A row resting on four things is
        # blocked if any one of them is missing, which is what "rests on" means.
        # ⚠ THREE OUTCOMES. A row every one of whose declarations RESTS ON AN INJECTED DEFAULT
        # is not a pass: `ASSUMED` carries into the case verdict as DEGRADED, never DECLARED-PRESENT.
        # Publishing those as PASS is what put seven false passes in the caselog.
        # ⚠ AN UNBOUND TOKEN IS AN AUTHORING ERROR, NOT A DESIGN FINDING, AND CONFLATING THEM
        # PUBLISHED THE SECOND WEARING THE FIRST'S CLOTHES. `resolve()` distinguishes them --
        # `bound=False` means the token NAMES NOTHING (`create_recrod`, `H-8`, a probe id with a
        # typo) -- and `grade` read only `ok`, so a mistyped token graded GAP, made its case
        # BLOCKED, and landed in `blockers` beside real holes. `report.py`'s own legend asserts the
        # opposite in the artifact: *"`GAP` | a declared token named a real thing"*. Nothing
        # enforced that sentence. It does now: an unbound token is INSTRUMENT-ERROR, it is
        # excluded from `blockers`, and its case cannot be graded at all.
        # Found by the `W10` adversarial pass.
        _unbound = [t for t, x in zip(tokens, parts) if not x.get("bound")]
        _ok = all(x["ok"] for x in parts)
        _assumed = any(x.get("assumed") for x in parts)
        entry["unbound"] = _unbound
        entry["verdict"] = dict(
            verdict="INSTRUMENT-ERROR" if _unbound
                    else "PASS" if _ok and not _assumed else "ASSUMED" if _ok else "GAP",
            detail=" · ".join(x["detail"] for x in parts),
            kind=None, section="", by="declared",
            title=need[:60], tests=need)
        entry["probe"] = next((x.get("probe") for x in parts if x.get("probe")), None)
        routed.append(entry)

    core = [r for r in rows if r.get("hardness") == "core"
            and not re.match(r"\s*UNCLEAR\b", r.get("need", ""), re.I)]
    core_unmapped = [u for u in unmapped if u["hardness"] == "core"]
    core_routed = [r for r in routed if r["hardness"] == "core"]
    core_blocked = [r for r in core_routed
                    if r["verdict"]["verdict"] in ("GAP", "NOT-REFUSED")]
    # A row whose declaration names nothing is a fact about the OVERLAY. It outranks every other
    # verdict because until it is fixed nothing the row says can be believed.
    broken = [r for r in routed if r["verdict"]["verdict"] == "INSTRUMENT-ERROR"]

    # HONESTY RULE 3: **a case with ANY unmapped `core` row may not be graded DECLARED-PRESENT.**
    #
    # ⚠ THE `more than half` CLAUSE THAT STOOD HERE IS DELETED, AS INERT. It read
    # `elif core and len(core_unmapped) * 2 > len(core): NOT-ASSESSED`, and it could never be the
    # deciding branch: its own predicate proves `core_unmapped` is non-empty, so the strict clause
    # two lines down returns the SAME verdict on every input that reaches it. It was meaningful
    # before the strict clause was added and has been dead ever since. Its guard
    # (`test_a_case_more_than_half_unrouted_on_core_is_not_assessed`) passed by deleting the rule
    # it named -- which is `CLAUDE.md` §0.1 pt 2 exactly: an assertion that cannot observe the
    # failure it excludes. Found by the `W10` adversarial pass.
    #
    # The strict clause was added after reading the first DECLARED-PRESENT list. Five of the twelve DECLARED-PRESENT verdicts in
    # the first run rested on one or two routed core rows with other core rows sitting
    # unmapped beside them -- one case reached DECLARED-PRESENT on a single distinct probe with three
    # rows unrouted. That is the instrument certifying a season it never aimed at, which is the
    # flattering direction and the one nobody notices.
    #
    # A blocker still outranks it: if a core row DID route and DID hit a gap, the case is
    # BLOCKED regardless of what else failed to route, because that is a fact about the shape
    # rather than about the aim.
    if broken:
        verdict = "INSTRUMENT-ERROR"
    elif core_blocked:
        verdict = "BLOCKED"
    elif not core_routed:
        # THE ZERO-CORE AND ZERO-DECLARED CASE. This is the only branch the strict clause below
        # cannot reach: a case with NO core rows at all has an empty `core_unmapped`, so nothing
        # else would stop it reaching DECLARED-PRESENT on its non-core rows alone.
        verdict = "NOT-ASSESSED"
    elif core_unmapped:
        verdict = "NOT-ASSESSED"
    # ⚠ `ASSUMED` LANDS HERE, WITH GAP. A row resting on an injected default nobody ratified is
    # a real dependency, and a case built entirely on such rows is DEGRADED — playable only if
    # the defaults happen to be right. Grading it DECLARED-PRESENT is the flattering direction, and it is
    # what seven rows did until the `W10` adversarial pass read the `detail` strings.
    elif any(r["verdict"]["verdict"] in ("GAP", "NOT-REFUSED", "ASSUMED") for r in routed):
        verdict = "DEGRADED"
    else:
        verdict = "DECLARED-PRESENT"

    return dict(
        id=case["id"], name=case.get("name", ""), scale=case.get("scale", ""),
        source=case.get("_source", ""), verdict=verdict,
        rows=len(rows), core=len(core), core_routed=len(core_routed),
        core_unmapped=len(core_unmapped), core_blocked=len(core_blocked),
        # ⚠ THE DECLARED TOKEN THAT FAILED, NOT A PROBE ID. Under the regex router a blocker was
        # always a probe, because a probe was the only thing a row could reach. A declared row
        # can rest on a verb the fold cannot execute or on an `absent` register row, and naming
        # THAT is the point of `W10`: `H-84` is a better answer than "P22 gapped".
        blockers=sorted({t for r in core_blocked
                         for t, x in zip(r.get("exercises") or [], r.get("resolved") or [])
                         if not x["ok"] and x.get("bound")}),
        unbound=sorted({t for r in broken for t in r.get("unbound") or ()}),
        routed=routed, unmapped=unmapped, unclear=len(unclear),
        ends_when=case.get("ends_when", ""),
    )


@TRACE.recording()      # `_gaps` and `_trace_counts` below are read off the trace this call keeps
def main(kinds=("NPC", "ARC")) -> dict:
    report: dict = {}
    for kind in kinds:
        cases = load_cases(kind)
        graded = []
        for c in cases:
            TRACE.case = c["id"]
            graded.append(grade(c))
        report[kind] = graded
    # every probe runs, even if no case routed onto it -- an unexercised probe is a finding.
    for pid in P.PROBES:
        run_probe(pid)
    report["_probes"] = _VERDICTS
    report["_gaps"] = TRACE.gaps
    report["_trace_counts"] = TRACE.counts()
    report["_corpus_defects"] = sorted(set(CORPUS_DEFECTS))
    return report




if __name__ == "__main__":
    # W15 -- ONE WRITER PER ARTIFACT. This entrypoint used to write `results.json` and
    # `TRACE.txt` itself, and `report.py` wrote them too from its own `main()` call. Two
    # writers over one artifact set meant whichever ran last won, and the committed markdown
    # went stale by one fix: FOUR ARC CASES WERE WRONG IN A MERGED PR because the caselogs
    # came from one run and `results.json` from another. `report.py` is now the SOLE emitter.
    # This entrypoint still RUNS the corpus -- it is the fastest way to see the tallies -- and
    # it writes nothing. `test_w15_the_run_cases_entrypoint_writes_nothing`, which ran this file as a
    # script and hashed `runs/` before and after, is retired: nothing enforces the refusal now.
    rep = main()
    for kind in ("NPC", "ARC"):
        rows = rep[kind]
        tally: dict[str, int] = {}
        for r in rows:
            tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        print(f"\n=== TEST {kind}: {len(rows)} cases ===")
        print("   " + " · ".join(f"{v} {k}" for k, v in sorted(tally.items())))
        blockers: dict[str, int] = {}
        for r in rows:
            for b in r["blockers"]:
                blockers[b] = blockers.get(b, 0) + 1
        print("   top core blockers: " + " · ".join(
            f"{k}({v})" for k, v in sorted(blockers.items(), key=lambda kv: -kv[1])[:10]))
        # ⚠ `routed` IS COUNTED, NOT SUBTRACTED. This line read `{rr-um} routed`, which folded
        # the `UNCLEAR:` rows into the routed count -- and under `W10` that is not a rounding
        # error: it published "15 routed" for the ARC lane, whose authored coverage is ZERO. All
        # fifteen were rows whose own SOURCE says it does not know. An unclear row is neither
        # routed nor unmapped; it is a third thing, and the flattering direction is to let it hide
        # inside the first. Found by the `W10` adversarial pass; `G11` is the rule it breaks.
        rr = sum(r["rows"] for r in rows)
        um = sum(len(r["unmapped"]) for r in rows)
        ro = sum(len(r["routed"]) for r in rows)
        uc = sum(r["unclear"] for r in rows)
        print(f"   {rr} season_requires rows = {ro} declared · {um} UNDECLARED · "
              f"{uc} UNCLEAR (the source's own admission)")
        assert ro + um + uc == rr, (ro, um, uc, rr)
    pv = rep["_probes"]
    tal: dict[str, int] = {}
    for v in pv.values():
        key = v["verdict"] if v["verdict"] != "GAP" else f"GAP:{v['kind']}"
        tal[key] = tal.get(key, 0) + 1
    print(f"\n=== PROBES: {len(pv)} ===")
    print("   " + " · ".join(f"{v} {k}" for k, v in sorted(tal.items())))
    print(f"\n=== TRACE: {TRACE.counts()}")
    print("\nWrote nothing under proposals/2026-09-01-season-loop-tests/. `report.py` is the\n"
          "sole emitter of runs/ (W15, guardrail G7). To regenerate the artifacts:\n"
          "    python report.py")
