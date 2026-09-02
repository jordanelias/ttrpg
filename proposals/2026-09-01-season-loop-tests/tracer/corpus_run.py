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


def run_case(case: dict, seed: int = 0) -> dict:
    scale, cid = str(case.get("scale")), case["id"]
    if scale not in set(S.RUNG_KINDS):
        return dict(id=cid, scale=scale, status="UNREPRESENTABLE", executed=[], refused=[],
                    seasons=0, why=f"`scale: {scale}` is not a rung kind")
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
                    seasons=n, why=f"{type(e).__name__}: {e}")
    except (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer) as e:
        return dict(id=cid, scale=scale, status="DESIGN-GAP", executed=[], refused=[],
                    seasons=n, why=f"{type(e).__name__}: {e}")
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
    return dict(id=cid, scale=scale, status="RAN" if ok else "NO-EXECUTION",
                executed=ok, refused=no, seasons=n, why="")


def main(seed: int = 0) -> int:
    rows = []
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            r = run_case(c, seed); r["lane"] = lane; rows.append(r)
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
    live = [r for r in rows if r["status"] in ("RAN", "NO-EXECUTION")]
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*(int(a) for a in sys.argv[1:])))
