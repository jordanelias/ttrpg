"""EVERY CASE, EXECUTED — not graded.

`run_cases.py` GRADES the corpus: it reads each case's prose `need` rows, looks up the authored
declaration that says which verb / hole / probe answers each one, and reports PLAYABLE / DEGRADED /
BLOCKED / NOT-ASSESSED. That is a judgement about whether the engine COULD support a character.

This RUNS them. For every case it builds a world at the case's own declared `scale`, folds seasons
through the real resolver, and reports which verbs actually EXECUTED. Two different questions, and
until now only the first had an instrument.

⚠ JORDAN ASKED FOR THIS, 2026-09-02, AND THE ARGUMENT IS HIS: *"a larger surface introduces more
complexity, but given our goals, what solves one may solve another while providing more pushback as
to whether something is the RIGHT solve."* It is `CLAUDE.md` §0.1's "targeted-green is not
validation" applied at corpus scale — the milestone runs ONE hand-built world for ONE case, and a
world built to make a case pass encodes this session's model of that case, not the engine.

⚠ THE CASE COUNT IS NOT THE WORLD COUNT, AND REPORTING IT AS ONE WOULD BE A CONFOUND. `build_at`
derives a world from the case's `scale` AND NOTHING ELSE, because `scale` is the only structured
field the corpus carries — `temporal`, `who_acts`, `knowledge` and `ends_when` are free English,
143 distinct values out of 143. So two cases at the same scale get the SAME world, and 143 cases
collapse to THREE distinct worlds. "86 executed cases agree" is therefore worth nothing; "three
worlds spanning six rungs of the ladder agree" is the measurement, and this module prints the
second. §0.1 point 4 — a number without a control is not a measurement, in either direction.

⚠ AN UNREPRESENTABLE SCALE REFUSES; IT IS NOT MAPPED TO THE NEAREST RUNG. 57 of 143 cases declare
`scale: faction` or `scale: world`, and neither is in `rung_kinds`. Quietly folding `faction` onto
`settlement` would manufacture a pass for the largest single block of the corpus. §42.2's polarity
rule sends zero evidence to the verdict AGAINST the thing measured, so those cases come back
UNREPRESENTABLE with the scale named, and that count is the finding.
"""
from __future__ import annotations
import sys
from collections import Counter

import shape as S
import run_cases as R
import probes as P


def build_at(scale: str, seed: int = 0) -> S.World:
    """A world whose deepest rung is `scale`, with the whole containment chain above it.

    ⚠ THE CHAIN IS `rung_kinds`, NOT A HAND-PICKED SHAPE. `RUNG_KINDS` is ordered person -> realm
    and the containment tree is that order, so a case at `settlement` gets settlement inside
    territory inside province inside duchy inside realm — the tree the architecture says exists,
    rather than the two rungs the milestone fixture happens to carry."""
    w = S.World(seed, S.DEFAULT_FIXTURES)
    order = list(S.RUNG_KINDS)                       # person .. realm
    chain = order[order.index(scale):] if scale in order else []
    ids = {k: f"r_{k}" for k in chain}
    for k in chain:
        w.rungs[ids[k]] = S.Rung(ids[k], k)
    for lower, upper in zip(chain, chain[1:]):
        w.add_tenure(S.Tenure(f"t_{lower}_in_{upper}", ids[lower], ids[upper], "contain", 0))
    # One site per producing kind, on the deepest rung, so the matter economy has a source (`W8`).
    for n, kind in enumerate(sorted(S.SITE_YIELD)):
        if S.SITE_YIELD[kind]:
            w.sites[f"s_{kind}"] = S.Site(f"s_{kind}", ids[chain[0]], kind,
                                          condition=w.fixtures.get("condition_scale"))
    for n, pid in enumerate(("p_a", "p_b", "p_c")):
        w.persons[pid] = S.Person(pid, pid)
        w.add_tenure(S.Tenure(f"t_{pid}_in", pid, ids[chain[0]], "contain", 0))
    # A motive. Without one nothing forms a candidate at all — `headless.build_world` records why:
    # Q4 (a `commit` to an OUGHT) is the only question source a quiet season can answer.
    prop = S.Proposition("prop_x", "OUGHT", ids[chain[0]], "a standing ambition", True, 0)
    w.propositions[prop.id] = prop
    for pid in ("p_a", "p_b", "p_c"):
        w.add_tenure(S.Tenure(f"t_{pid}_commits", pid, prop.id, "commit", 0))
    for pid, ax in (("p_a", "Precedent"), ("p_b", "suspicion"), ("p_c", "self_preservation")):
        w.persons[pid].convictions = {ax: 0.9}
    return w


def run_case(case: dict, seasons: int = 2, seed: int = 0) -> dict:
    scale = str(case.get("scale"))
    if scale not in set(S.RUNG_KINDS):
        return dict(id=case["id"], scale=scale, status="UNREPRESENTABLE", verbs=[], acts=0,
                    why=f"`scale: {scale}` is not a rung kind; rung_kinds is {list(S.RUNG_KINDS)}")
    w = build_at(scale, seed)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    try:
        for _ in range(seasons):
            d.season(ch, question=None, subsistence=P.SUBSIST)
    except Exception as e:                            # an INSTRUMENT defect, reported as one
        return dict(id=case["id"], scale=scale, status="ERROR", verbs=[], acts=0,
                    why=f"{type(e).__name__}: {e}")
    acted = sorted({a.verb for a in getattr(d, "resolved", [])})
    return dict(id=case["id"], scale=scale, status="RAN" if acted else "NO-ACT",
                verbs=acted, acts=len(getattr(d, "resolved", [])), why="")


def main(seasons: int = 2, seed: int = 0) -> int:
    rows, by_status = [], Counter()
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            r = run_case(c, seasons, seed); r["lane"] = lane
            rows.append(r); by_status[r["status"]] += 1
    print(f"CORPUS RUN — {len(rows)} cases, {seasons} seasons, seed {seed}")
    for k, v in sorted(by_status.items()):
        print(f"  {k:16} {v}")
    un = Counter(r["scale"] for r in rows if r["status"] == "UNREPRESENTABLE")
    if un:
        print(f"  unrepresentable scales: {dict(un)}")
    ran = [r for r in rows if r["status"] == "RAN"]
    worlds = sorted({r["scale"] for r in ran})
    sigs = {tuple(r["verbs"]) for r in ran}
    print(f"\n  DISTINCT WORLDS   {len(worlds)}  {worlds}   <- the real N; cases at one scale are identical")
    print(f"  DISTINCT VERB SETS {len(sigs)} across those worlds")
    print(f"  acts per case      {sorted({r['acts'] for r in ran})}")
    ever = sorted({v for r in ran for v in r["verbs"]})
    never = sorted(set(S.VERB_TABLE) - set(ever))
    print(f"\nVERBS THAT EXECUTED ANYWHERE : {len(ever)} of {len(S.VERB_TABLE)} — {ever}")
    print(f"VERBS THAT NEVER EXECUTED    : {len(never)} — {never}")
    foldable = set(S.resolvable_verbs())
    print(f"\nWHERE THE 32 GO: {len(set(S.VERB_TABLE) - foldable)} have no predicate/effect at all · "
          f"{len(foldable - set(ever))} the fold CAN execute but nobody ever CHOOSES "
          f"({sorted(foldable - set(ever))}) · {len(ever)} actually happen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*(int(a) for a in sys.argv[1:])))
