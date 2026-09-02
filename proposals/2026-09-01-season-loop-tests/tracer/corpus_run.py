"""EVERY CASE, EXECUTED — not graded, and not merely attempted.

`run_cases.py` GRADES the corpus: it reads each case's prose `need` rows, looks up the authored
declaration naming which verb / hole / probe answers each one, and reports PLAYABLE / DEGRADED /
BLOCKED / NOT-ASSESSED. That is a judgement about whether the engine COULD support a character.

This RUNS them. Jordan asked for it, 2026-09-02: *"shouldn't we consider running all NPCs and all
arcs in our test runs? a larger surface introduces more complexity, but given our goals, what
solves one may solve another while providing more pushback as to whether something is the RIGHT
solve."* It is `CLAUDE.md` §0.1's *"targeted-green is not validation"* at corpus scale.

⚠ REV 2. THE FIRST VERSION MEASURED A QUANTITY ITS OWN FIXTURE HAD ALREADY FIXED, and its
adversarial pass overturned the headline. Three defects, all of them the same shape — an instrument
that could only return the answer it returned:

  1. **IT COUNTED ATTEMPTS AND CALLED THEM EXECUTIONS.** It read `driver.resolved`, and
     `self.resolved.append(a)` is the FIRST statement of `_fold` — before `_eligible`, before the
     `requires` predicate, before the wrote-nothing refusal. `shape.py` says so in terms: *"record
     which acts REACHED RESOLVE"*. Every "verb that executed" was a verb that was tried. Execution
     is now read from the EVENT LOG through Part E's own `emits:` / `emits_on_refusal:` columns,
     which is the design's own statement of what success looks like.
  2. **EVERY WORLD WAS THE SAME WORLD PERSON-SIDE.** It hung persons, the Proposition, the
     convictions and the sites all on `chain[0]`, so `scale` varied only the count of rungs ABOVE
     the actors — and `View.__slots__` is `(holder, claim_ids, question)` with `__getattr__`
     raising, so L2 closes the only channel by which a rung could reach a verb choice. *"One verb
     set across three worlds"* was therefore entailed by a ruled refusal plus an identical fixture,
     before anything ran. That is not a finding about the ladder.
  3. **A PERSON IS ALSO A RUNG AND THIS FIXTURE FORGOT IT.** `tiny_world` gives every person a
     `person`-kind Rung under the same id; `build_at` did not, so `_req_move`'s `w.rungs.get(
     a.actor)` was `None` and `move` was refused in every world in the corpus — while being
     reported as one of the seven verbs that "executed".

⚠ AND `scale` IS NOT THE CORPUS'S ONLY STRUCTURED FIELD, WHICH IS WHAT MADE REV 1's CEILING
ARGUMENT WRONG IN THE REVERSE DIRECTION. `temporal` is a mapping with declared sub-keys and **57 of
143 cases carry an integer `temporal.span_seasons`** (1..16), which rev 1 ignored while hardcoding
2. And `cases/ENDINGS_CLASSIFIED.yaml` already classifies endings into DECIDER/ROLL/THRESHOLD/
NEVER/UNCLEAR with a boolean `forced_by_threshold`. Both are read here. So the number of distinct
worlds is a property of what the BUILDER reads, never a ceiling the corpus imposes.

⚠ AN UNREPRESENTABLE SCALE STILL REFUSES rather than being folded onto the nearest rung: §42.2's
polarity rule sends zero evidence to the verdict AGAINST the thing measured, and mapping `faction`
onto `settlement` would manufacture a pass for the largest single block of the corpus.
"""
from __future__ import annotations
import sys
from collections import Counter
from pathlib import Path

import shape as S
import run_cases as R
import probes as P

# `CLAUDE.md` §0.1 pt 5 / `G1`: declared here with its reason, not a bare literal in a body.
MAX_SEASONS = 6          # the corpus asks for up to 16; the flood (`W6`) makes that unaffordable
DEFAULT_SEASONS = 2      # for the 86 cases whose `span_seasons` is prose ("ongoing")

_ENDINGS = Path(__file__).resolve().parents[2] / "2026-08-31-shape-tracer" / "cases" / "ENDINGS_CLASSIFIED.yaml"


def endings() -> dict:
    """`cases/ENDINGS_CLASSIFIED.yaml`, keyed by case id. Its own header calls the 19 of 50 rows
    carrying `forced_by_threshold` *"load-bearing on the whole proposal"*, and rev 1 did not read
    it — so a deadline that the corpus says forces the ending reached no world."""
    if not _ENDINGS.exists():
        return {}
    d = S.load_yaml(_ENDINGS.read_text())
    rows = d.get("cases") if isinstance(d, dict) else d
    return {r["id"]: r for r in (rows or []) if isinstance(r, dict) and r.get("id")}


ENDINGS = endings()


def seasons_for(case: dict) -> int:
    """The case's own `temporal.span_seasons` where it is an integer, clamped to `MAX_SEASONS`."""
    t = case.get("temporal")
    n = t.get("span_seasons") if isinstance(t, dict) else None
    return min(int(n), MAX_SEASONS) if isinstance(n, int) and n > 0 else DEFAULT_SEASONS


def build_at(case: dict, seed: int = 0) -> S.World:
    """A world for THIS case: the containment chain down to its `scale`, three people who are
    themselves `person` rungs, a site per producing kind, a motive, and — where the corpus says the
    ending is forced by a threshold — a Date coming due, which is `questions_for`'s Q1.

    ⚠ THE CONVICTIONS ARE SEEDED FROM THE CASE ID, over the `conviction_axes` ROSTER. Rev 1 wrote
    three axis names and the weight `0.9` as literals, which is a fill off the register (`G1`) and,
    worse, was the ENTIRE ranking function — `stance` is empty in these worlds and §F2's `urgency`
    term has no `c` in it, so the conviction axis alone orders every candidate. Identical
    convictions therefore forced identical rankings in every world. Seeding from the id makes them
    differ per case, reproducibly, and takes the axis names from the roster rather than a body."""
    scale = str(case.get("scale"))
    w = S.World(seed, S.DEFAULT_FIXTURES)
    order = list(S.RUNG_KINDS)
    chain = order[order.index(scale):] if scale in order else []
    ids = {k: f"r_{k}" for k in chain}
    for k in chain:
        w.rungs[ids[k]] = S.Rung(ids[k], k)
    for lower, upper in zip(chain, chain[1:]):
        w.add_tenure(S.Tenure(f"t_{lower}_in_{upper}", ids[lower], ids[upper], "contain", 0))
    for kind in sorted(S.SITE_YIELD):
        if S.SITE_YIELD[kind]:
            w.sites[f"s_{kind}"] = S.Site(f"s_{kind}", ids[chain[0]], kind,
                                          condition=w.fixtures.get("condition_scale"))
    axes = sorted(S.CONVICTION_AXES)
    for n, pid in enumerate(("p_a", "p_b", "p_c")):
        w.persons[pid] = S.Person(pid, pid)
        # ⚠ A PERSON IS THE BOTTOM RUNG OF THE LADDER, and `tiny_world` models it that way. Without
        # this, `_req_move`'s `w.rungs.get(a.actor)` is None and `move` is refused everywhere.
        w.rungs[pid] = S.Rung(pid, "person")
        w.add_tenure(S.Tenure(f"t_{pid}_in", pid, ids[chain[0]], "contain", 0))
        pick = int(S.H(seed, 0, str(case.get("id")), f"axis:{pid}"), 16) % len(axes)
        w.persons[pid].convictions = {axes[pick]: 0.9}
    prop = S.Proposition("prop_x", "OUGHT", ids[chain[0]], "a standing ambition", True, 0)
    w.propositions[prop.id] = prop
    for pid in ("p_a", "p_b", "p_c"):
        w.add_tenure(S.Tenure(f"t_{pid}_commits", pid, prop.id, "commit", 0))
    if (ENDINGS.get(str(case.get("id"))) or {}).get("forced_by_threshold"):
        # Q1: a Date coming due, with a DocketItem naming a matter. The corpus says this case's
        # ending is forced by a threshold; a world with no deadline cannot represent that at all.
        w.dates["d_forced"] = {"id": "d_forced", "venue": ids[chain[0]], "due_at": 1,
                               "holder": None, "fired": False}
        w.docket.append({"date": "d_forced", "matter": prop.id})
    return w


# ===========================================================================
# `W18` -- THE RUN DEFINITION, AS AN INSTRUMENT (`PLAN.md` §6.1, §6.2)
#
# `run_cases.py` GRADES; this RUNS. The difference is the whole of `PLAN.md` Part 4B: the first
# item set optimised for a grading count that rose while zero cases ran.
#
# ⚠ A CHECK THIS CANNOT COMPUTE REPORTS `NOT-COMPUTABLE` AND NAMES THE ITEM THAT CLOSES IT. It
# does NOT score. `R2` needs authored `exercises:` rows and a real cast (`W27`); `A2`'s DECIDER and
# ROLL predicates need mechanisms `W26` and `W23` build; `A3` needs the case's own cast (`W27`).
# A number that cannot fail is not a measurement (§0.1 pt 2), and it flatters toward progress every
# time -- which this chain has now found in its own work six times.
# ===========================================================================

NOT_COMPUTABLE = {
    "R2": "W10-core (author the rows) + W27 (a real cast)",
    "A2": "W23 (contest results) + W26 (binding decisions) + W30 (the predicates)",
    "A3": "W27 (the cast comes from the case)",
}


def _register_sites() -> str:
    """Every `site:` on the register, as one string -- `R5`'s haystack.

    ⚠ THE SAME READING `W9` CHECK 3 USES, not a second one (§8). That check asserts the milestone
    run's fixture reads all resolve; this asks the same question per case."""
    import register as REG
    return " ".join(str(r.get("site") or "") for r in REG.load()["rows"])


def _r3_propagates(w, driver) -> bool:
    """`R3`: is there an **Act by another person** whose `causes[]` walks back to an act of a
    different person?

    ⚠ THE FIRST WORDING OF THIS CHECK SAID *AN EVENT* AND WAS SATISFIABLE 711 TIMES OVER ON DAY
    ONE. Every `claim.deposited` Event has a cause whose `subject` differs from its own -- that is
    what a witness deposit IS -- so an Event-level test scores every completing case immediately,
    and the instrument built to say zero would have opened by saying twenty-seven. Measured: 711 of
    711 deposits pass the loose reading; 0 Events have a cause that is an ACT by a different person.

    ⚠ AND IT MUST GO THROUGH `causes[] -> Act.actor`, BECAUSE THE EVENT HAS NO ACTOR BY RULING.
    #353 §19.3 puts `actor` among the three fields the Event does NOT carry; `driver.resolved` is
    the only surface that knows who acted, which is also what `H-82`'s `log u resolved` integrity
    check is for."""
    acts = list(getattr(driver, "resolved", []))
    if len(acts) < 2:
        return False
    # Event id -> the ACTOR of the act that emitted it, by the fold's own id derivation
    # (`H(seed, tick, actor, f"{kind}:{act.id}")`), which is the same route execution attribution
    # uses. One index, built once -- the first draft of this nested four loops and was O(n^4).
    emitter: dict = {}
    for a in acts:
        row = S.VERB_TABLE.get(a.verb)
        if row is None:
            continue
        for k in tuple(row.emits or ()) + tuple(row.emits_on_refusal or ()):
            for t in range(w.tick + 2):
                emitter[S.H(w.world_seed, t, a.actor, f"{k}:{a.id}")] = a.actor
    for e in w.log:
        mine = emitter.get(e.id)
        if mine is None:
            continue
        for c in (e.causes or []):
            theirs = emitter.get(c)
            if theirs is not None and theirs != mine:
                return True
    return False


def _span_status(case: dict) -> str:
    """`A1`: an integer `span_seasons` is run in full; a prose span REFUSES rather than defaulting.

    ⚠ REFUSES, NOT DEFAULTS. `MAX_SEASONS` clamps 3 arcs the corpus asks for at 8/10/16, and a
    silent default would report a 2-season run as an arc that ran its span. `W29` lifts the clamp;
    `W28` authors the prose spans."""
    t = case.get("temporal")
    n = t.get("span_seasons") if isinstance(t, dict) else None
    if not isinstance(n, int) or n <= 0:
        return "SPAN-UNAUTHORED"
    return "CLAMPED" if n > MAX_SEASONS else "OK"


def run_case(case: dict, seed: int = 0, lane: str = "NPC") -> dict:
    scale, cid = str(case.get("scale")), case["id"]
    if scale not in set(S.RUNG_KINDS):
        return dict(id=cid, scale=scale, status="UNREPRESENTABLE", executed=[], refused=[],
                    seasons=0, why=f"`scale: {scale}` is not a rung kind", checks={})
    n = seasons_for(case)
    w = build_at(case, seed)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    try:
        for _ in range(n):
            d.season(ch, question=None, subsistence=P.SUBSIST)
    except S.InstrumentDefect as e:
        # ⚠ THE TWO BUCKETS ARE SHAPE'S OWN, NOT A SECOND TAXONOMY (§8). `shape.py` states why the
        # split matters: a call-site bug landing in the design column *"corrupts the measurement in
        # the direction that flatters it"*. Rev 1 merged them and labelled the merged bucket
        # "an INSTRUMENT defect", which mis-attributes every design gap the fold can raise.
        return dict(id=cid, scale=scale, status="INSTRUMENT-DEFECT", executed=[], refused=[],
                    seasons=n, why=f"{type(e).__name__}: {e}", checks={"R1": False})
    except (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer) as e:
        return dict(id=cid, scale=scale, status="DESIGN-GAP", executed=[], refused=[],
                    seasons=n, why=f"{type(e).__name__}: {e}", checks={"R1": False})
    # EXECUTION, ATTRIBUTED TO THE ACT — not to any verb that shares an emission kind.
    #
    # ⚠ THE KIND ALONE IS NOT AN ATTRIBUTION, AND READING IT AS ONE PUT A FALSE POSITIVE IN THE
    # PUBLISHED SET. `forge` and `create_record` BOTH emit `record.created` (and `confer` and
    # `revoke` both emit `tenure.closed`), so a scan over `{e.kind for e in w.log}` credited
    # `forge` with every record `create_record` made — while `forge` has no predicate and no
    # effect and cannot execute at all. Caught by cross-checking the executed set against the
    # predicate/effect tables: a verb the fold cannot execute appeared among the verbs that did.
    #
    # The fold derives every emission's id as `H(seed, tick, actor, f"{kind}:{act.id}")`
    # (`shape.py`, `_fold.ev`), so attribution is EXACT and reuses the design's own id scheme
    # rather than adding a second rule for the same question (§8). The act id is unique, so a
    # match at any tick is a genuine match for that act.
    ids = {e.id for e in w.log}
    ok_v, no_v = set(), set()
    for a in getattr(d, "resolved", []):
        row = S.VERB_TABLE.get(a.verb)
        if row is None:
            continue
        for t in range(n + 1):
            for k in (row.emits or ()):
                if S.H(w.world_seed, t, a.actor, f"{k}:{a.id}") in ids:
                    ok_v.add(a.verb)
            for k in (row.emits_on_refusal or ()):
                if S.H(w.world_seed, t, a.actor, f"{k}:{a.id}") in ids:
                    no_v.add(a.verb)
    ok, no = sorted(ok_v), sorted(no_v)
    # ---- `W18`: §6.1's R1/R3/R4/R5 and §6.2's A1, computed. R2/A2/A3 are NOT-COMPUTABLE.
    before = dict(S.DEFAULT_FIXTURES.reads)
    w2 = build_at(case, seed)
    d2 = S.SeasonDriver(w2)
    mint2 = lambda pid, verb, subj: S.H(w2.world_seed, w2.tick, pid, f"act:{verb}:{subj}")
    ch2 = S.make_chooser(w2.fixtures, mint2, verbs=S.resolvable_verbs())
    try:
        for _ in range(n):
            d2.season(ch2, question=None, subsistence=P.SUBSIST)
        r4 = w2.content_hash() == w.content_hash()
    except Exception:
        r4 = False
    read = [k for k, c in w.fixtures.reads.items() if c > before.get(k, 0)]
    sites = _register_sites()
    checks = {
        "R1": True,
        "R3": _r3_propagates(w, d),
        "R4": r4,
        "R5": all(k in sites for k in read) if read else None,
        "A1": _span_status(case),
    }
    # §6.1's statuses. `RUNS` needs R2, which is NOT-COMPUTABLE — so a case that passes everything
    # computable is `RUNS-UNDECLARED`, which is the honest name for it and exists because the first
    # draft had no status a case could occupy today.
    core = checks["R1"] and checks["R4"] and (checks["R5"] is not False)
    if not core:
        status = "HALTS"
    elif lane == "ARC" and checks["A1"] == "SPAN-UNAUTHORED":
        status = "SPAN-UNAUTHORED"
    elif checks["R3"]:
        status = "RUNS-UNDECLARED"
    else:
        status = "RUNS-ALONE-UNDECLARED" if ok else "NO-EXECUTION"
    return dict(id=cid, scale=scale, status=status, executed=ok, refused=no, seasons=n,
                why="", checks=checks)


def planted_control(seed: int = 0) -> tuple:
    """`W18`'s CONTROL, and the only clause of its proof that demonstrates sensitivity.

    ⚠ PRINTING ZERO WHERE ZERO IS ENTAILED IS NOT A CONTROL (§0.1 pt 4). The first draft called it
    one. This plants a second person's Act caused by the first person's act and asserts `R3` flips
    false -> true; without it the instrument has shown only that it can print a number.

    Returns `(before, after)`."""
    case = next(c for c in R.load_cases("NPC") if str(c.get("scale")) in set(S.RUNG_KINDS))
    w = build_at(case, seed)
    d = S.SeasonDriver(w)
    before = _r3_propagates(w, d)
    # Two acts, two actors, the second caused by the first. Hand-built: the point is to prove the
    # DETECTOR works, not that the loop produces one -- the loop producing one is `W24`/`W25`.
    a1 = S.Act(id="ctl_a", actor="p_a", verb="speak")
    a2 = S.Act(id="ctl_b", actor="p_b", verb="speak")
    d.resolved.extend([a1, a2])
    k = S.VERB_TABLE["speak"].emits[0]
    e1 = S.Event(S.H(w.world_seed, 0, "p_a", f"{k}:{a1.id}"), k, "p_a", [], [S.ROOT], 0)
    e2 = S.Event(S.H(w.world_seed, 0, "p_b", f"{k}:{a2.id}"), k, "p_b", [], [e1.id], 0)
    w.log.extend([e1, e2])
    return before, _r3_propagates(w, d)


def main(seed: int = 0) -> int:
    rows = []
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            r = run_case(c, seed, lane); r["lane"] = lane; rows.append(r)
    by = Counter(r["status"] for r in rows)
    print(f"CORPUS RUN — {len(rows)} cases, seed {seed}, seasons from `temporal.span_seasons`")
    for k, v in sorted(by.items()):
        print(f"  {k:18} {v}")
    un = Counter(r["scale"] for r in rows if r["status"] == "UNREPRESENTABLE")
    if un:
        print(f"  unrepresentable scales: {dict(un)}")
    # ⚠ THE DISCRIMINATION MEASUREMENT, which is what explains a single executed set across many
    # different worlds. §F2 ranks candidates by `Σ conviction[axis] · alignment(verb, axis)`, and
    # `alignment` is SPARSE with `default_cell: 0.0` — so a person's convictions separate only the
    # handful of (verb, axis) pairs the table actually carries. Every other candidate scores
    # identically and `sorted(..., key=(-score, c.verb, c.subject))` breaks the tie ALPHABETICALLY
    # BY VERB NAME. Reported rather than inferred, because "the worlds agree" is worthless without
    # saying WHY they agree (`H-97`).
    sep = []
    for c in R.load_cases("NPC") + R.load_cases("ARC"):
        if str(c.get("scale")) not in set(S.RUNG_KINDS):
            continue
        w2 = build_at(c, seed); w2.step = S.Step.DELIBERATE
        pr = w2.persons["p_a"]
        qs = S.questions_for(w2, pr)
        vw = S.Query.assemble(pr, qs[0] if qs else None, w2.fixtures.get("view_k"))
        cd = S.Query.opening_set(pr, vw, qs[0]) if qs else []
        nz = sum(1 for x in cd if any(float(pr.convictions.get(a, 0.0)) * S.align(x.verb, a)
                                      for a in S.CONVICTION_AXES))
        sep.append((nz, len(cd)))
    if sep:
        tot = sep[0][1]
        print(f"\n  RANKING DISCRIMINATION   {min(n for n, _ in sep)}..{max(n for n, _ in sep)} of "
              f"{tot} candidates carry a nonzero conviction score; the rest TIE and are ordered "
              f"alphabetically by verb name")
    # ⚠ A CASE THAT EXECUTED, WHATEVER ITS BAR STATUS. `W18` renamed the statuses (`RAN` became
    # `RUNS-UNDECLARED` / `RUNS-ALONE-UNDECLARED`), and this filter still named the old ones — so
    # the verb counts went to 0 of 32 the moment the bar landed, silently, because an empty set has
    # no obvious tell. Keyed on `checks["R1"]` now, which is the property meant all along: the run
    # completed. Caught by reading the output rather than by a test, which is the honest account.
    live = [r for r in rows if r.get("checks", {}).get("R1") is True]
    sigs = {tuple(r["executed"]) for r in live}
    print(f"\n  DISTINCT WORLDS RUN      {len(live)} (scales {sorted({r['scale'] for r in live})}, "
          f"season counts {sorted({r['seasons'] for r in live})})")
    print(f"  DISTINCT EXECUTED SETS   {len(sigs)}")
    ever = sorted({v for r in live for v in r["executed"]})
    tried = sorted({v for r in live for v in r["refused"]})
    foldable = set(S.resolvable_verbs())
    print(f"\nVERBS THAT EXECUTED : {len(ever)} of {len(S.VERB_TABLE)} — {ever}")
    print(f"VERBS ONLY REFUSED  : {len(set(tried) - set(ever))} — {sorted(set(tried) - set(ever))}")
    print(f"\nWHERE THE {len(S.VERB_TABLE)} GO: {len(set(S.VERB_TABLE) - foldable)} have no "
          f"predicate/effect · {len(foldable - set(ever) - set(tried))} foldable but never even "
          f"attempted ({sorted(foldable - set(ever) - set(tried))}) · "
          f"{len(set(tried) - set(ever))} attempted and always refused · {len(ever)} executed")

    # ---- `W18`: THE BAR, per lane (`PLAN.md` §6.1 / §6.2) --------------------
    print("\n" + "=" * 72)
    print("THE BAR — `PLAN.md` Part 6.  Two counts, one per lane, NEVER averaged (`G10`):")
    print("  the NPC number counts PROPAGATION; the ARC number counts ENDINGS.")
    for lane in ("NPC", "ARC"):
        ls = [r for r in rows if r["lane"] == lane]
        st = Counter(r["status"] for r in ls)
        headline = "RUNS" if lane == "NPC" else "ENDS"
        print(f"\n  {lane}  ({len(ls)} cases)     ** {headline} = {st.get(headline, 0)} **")
        for k, v in sorted(st.items(), key=lambda kv: -kv[1]):
            print(f"     {k:24} {v}")
        live = [r for r in ls if r["checks"]]
        for c in ("R1", "R3", "R4", "R5"):
            n = sum(1 for r in live if r["checks"].get(c) is True)
            print(f"     check {c}: {n} of {len(live)} pass")
    b, a = planted_control(seed)
    print(f"\n  CONTROL — planted cross-person edge: R3 {b} -> {a}  "
          f"{'(the detector works)' if (not b and a) else '⚠ THE CONTROL DID NOT FIRE'}")
    print("\n  NOT-COMPUTABLE — reported, never scored:")
    for k, why in NOT_COMPUTABLE.items():
        print(f"     {k}: closed by {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*(int(a) for a in sys.argv[1:])))
