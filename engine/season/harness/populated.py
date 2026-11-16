"""`harness.populated` — ONE WORLD, THE WHOLE CAST, AND MORE THAN ONE PLACE TO STAND.

WHAT THIS IS FOR, in Jordan's words (2026-09-13): *"I want to see as many persons as there are NPC
season loops for each world. If there are 87 loops, then I want 87 persons for each test run. I want
there to be multiple locations to inhabit."* And: *"each settlement has places/buildings. we need to
build these out for testing."*

WHAT IT REPLACES, AND WHY THE OLD SHAPE COULD NOT SHOW ANYTHING. `corpus_run.build_at` builds ONE
WORLD PER CASE and seats exactly three persons in it -- `p_a`, `p_b`, `p_c`, unnamed, all three in
the SAME rung, in all 89 runnable worlds. Measured 2026-09-13, and each of these is a fact about the
instrument rather than about the design:

  * all three persons act in every world (p_b 2182 acts · p_a 1935 · p_c 1911), so it is not that
    one NPC does everything -- the loops ARE concurrent within a world;
  * they are co-located at tick 0 and at the end of every run, and NOBODY'S containing rung ever
    changes, in any of the 89 worlds;
  * 0 of 4,870 acts name another person as their subject;
  * and the told channel (`ED-IN-0222`) deposits 8 second-hand claims in the whole corpus, because
    a witness who saw everything the teller saw cannot be told anything.

Three anonymous people standing in one room, 89 times over, is not a population, and every
measurement taken on it inherits that. `engine/season/requirements.yaml` names the gap `W27`
("a real cast") and it is the stated blocker on `R2` and `A3`.

WHERE THE PLACES COME FROM, AND WHICH HALF IS CANON.

  * `systems/settlements/valoria_geography_v30.yaml` -- CANON. 17 provinces, 37 settlements, each
    with a territory, a controller and a type. Read, never edited, never overridden here.
  * `engine/season/venues.yaml` -- AUTHORED FOR PLAY. The buildings inside a settlement, which
    canon does not name at all. Its header says so at length.

⚠ THE LADDER NEEDED NO NEW KIND AND THAT IS THE POINT. `rosters.yaml: rung_kinds` is
`person < hearth < community < settlement < territory < province < duchy < realm`. `community` and
`hearth` sat unused in every world this repo has ever built, which is precisely why everyone was in
one room: `build_at` seats a person directly in the settlement. A BUILDING is a `hearth`; a QUARTER
is a `community`. `contain_ascends` requires strict ascent and not adjacency (`state/world.py:220`),
so `realm -> province -> settlement -> community -> hearth -> person` is legal with `territory` and
`duchy` unused.

⚠ THE CAST IS THE CORPUS'S OWN, NOT A GENERATED ONE. Every case carries a `name:` -- "Carin Vedel",
not `p_a` -- and one person is seated per case. That is `W27`'s *"the cast comes from the case"*
read literally, and it is why this module authors no NPC: inventing a roster here would be the
fabrication `OI-05` is filed as a ruling to avoid (`ED-WR-0011`).

⚠ WHAT THIS DOES **NOT** DO. It does not grade the 143 cases -- `corpus_run` still owns that, and
its per-case worlds are what the `R1`/`R3`/`R4`/`R5` checks are computed over. This is a second
instrument beside it, not a replacement, and nothing here is wired into a gate yet. Read its output
as a measurement of what a populated world does, not as a claim that a case passes.

⚠ **AN ARC HAS NO CARRIER (`ED-IN-0225`, 2026-09-13): no type, no rung, no tenure kind, and the
carrier is not to be built.** The 97 ARC cases name SITUATIONS -- "The Unworked Clause",
"Vaynard's Wager" -- and what an arc IS in this world has no carrier. This module seats the NPC lane
only and builds no carrier for an arc.

`corpus_run`'s own bar reports the ARC lane as
*"ENDS = NOT-COMPUTABLE -- closed by W23 (contest results) + W26 (binding decisions) + W30 (the
predicates)"*. An arc CARRIER is on none of those three, so the ARC half of the bar was never
waiting on one -- the ARC cases keep being graded by `corpus_run` exactly as before.
"""

from __future__ import annotations

import sys
from collections import Counter

from ..boot.realm import build_realm
from ..queries.world_q import HUNGER_KIND, closed_uses, home_of as home_of_q, hunger, subsistence_draw, uncontrolled
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.world import World
from . import probes as P


def census(w: World) -> dict:
    """What was built, counted from the world rather than from the inputs."""
    kinds = Counter(r.kind for r in w.rungs.values())
    # §8: `world_q.home_of` owns "where is everyone"; this used to roll its own copy, and so did
    # three other sites (see that query's docstring).
    where = home_of_q(w)
    # ⚠ THE SUBSISTENCE ROWS ARE ITEM 3a's EXECUTION ARTIFACT, and they exist because the number
    # that mattered was invisible. Before the larder ladder, `build_realm(0)` after one season
    # held 4,810 units at the 37 settlements and 0 at the 211 hearths, while every person lived
    # in a hearth — so the draw ran at 0 rungs and the census reported a thriving economy nobody
    # could eat from. `stores_by_rung_kind` is where the food IS; `eaters_short` is who could not
    # reach it. Both are read from the world, never from the inputs.
    stores_by_kind: Counter = Counter()
    for r in w.rungs.values():
        for k, v in (r.stores or {}).items():
            stores_by_kind[r.kind] += v
    short = getattr(w, "_subsistence_shortfall", {})
    # REM-50: one walk of the larder ladder for every settlement's `hunger`, never one per call.
    next_draw = subsistence_draw(w)
    hunger_bands = Counter(hunger(w, r.id, next_draw)[0] for r in w.rungs.values() if r.kind == HUNGER_KIND)
    # `24f`: the cohorts are persons (S9.1), so `persons` counts them; these two rows separate them
    # from the cast, read off the world (`Person.is_cohort`) rather than off `cohorts.yaml`.
    cohorts = [p for p in w.persons.values() if p.is_cohort]
    return {"rungs": dict(kinds), "persons": len(w.persons), "sites": len(w.sites),
            "cohorts": len(cohorts), "cohort_weight": sum(p.weight for p in cohorts),
            "ties": getattr(w, "_tie_census", {}), "propositions": len(w.propositions),
            # v9 IN-68: what `seed_goals` minted, a report and never read by the loop. `orientation`
            # rows are loaded and counted and mint nothing; `dropped` is the cap's.
            **{(k if k == "goals" else f"goal_{k}"): getattr(w, "_goal_census", {}).get(k, 0)
               for k in ("goals", "orientation", "commits", "stance_rows", "dropped")},
            "distinct_buildings_inhabited": len(set(where.values())),
            "largest_building": max(Counter(where.values()).values()) if where else 0,
            "stores_by_rung_kind": dict(sorted(stores_by_kind.items())),
            "eaters_short": len(short),
            "unheld_for_want_of_a_head": len(getattr(w, "_unheld_for_want_of_a_head", [])),
            # `24h` P5: the revolt Query's only caller (r2 `05` §A.1.5 RULED (d),
            # `establishment_of`'s precedent). A report, not a rule: it feeds no decision and moves no hash.
            # Summed over REALM rungs: `terr_T16` is a root rung outside the realm (see `build_realm`), so
            # it is not counted.
            "uncontrolled_in_realm": sum(len(uncontrolled(w, r.id))
                                            for r in w.rungs.values() if r.kind == "realm"),
            # v9 IN-35: the Calamity's effect per territory (`world_q.closed_uses`, a Query over band
            # floors), its one reader -- `uncontrolled`'s precedent above: a report, not a rule. Each
            # territory with a Site below a floor, and how many such Sites it holds.
            "sites_below_a_floor_by_territory": {
                r: n for r in sorted(w.rungs) if w.rungs[r].kind == "territory"
                if (n := len(closed_uses(w, r)))},
            # REM-50: `world_q.hunger`'s only caller until CP-T10-05 -- `uncontrolled`'s precedent above: a
            # report, not a rule. Each settlement's band, from the NEXT draw; D = 0 counts as `fed`.
            "hunger_by_settlement": dict(sorted(hunger_bands.items()))}


def run(seasons: int = 1, seed: int = 0, cap: int | None = None, w: World | None = None) -> dict:
    """Build it and tick it. Returns the census plus what the season did.

    `w` takes a world ALREADY BUILT, for a caller that wants to report on the build before the
    season runs -- `main` below is the one, and without this it built the whole realm twice
    (~10s each) to print a census it then discarded.

    ⚠ `out["acts"]`, `out["actors"]` AND `out["act_subjects"]` READ `d.resolved`, THE FOLD SET, ON
    PURPOSE (REM-10 / HR-8): `harness/aperture.py`'s CONTROL line compares this `acts` with the
    measured arm's `len(d.resolved)`, and `harness/arms.py` reads `act_subjects` as its outcome
    metric. The ATTEMPT census (`corpus_run.attempts`, the act store) is a different, larger
    quantity; it does not replace this one."""
    w = build_realm(seed, cap) if w is None else w
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    for _ in range(seasons):
        d.season(ch, question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    out = census(w)
    out["acts"] = len(d.resolved)
    out["actors"] = len({a.actor for a in d.resolved})
    subj_rel = Counter()
    for a in d.resolved:
        s = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
        subj_rel["another person" if (s in w.persons and s != a.actor)
                 else "self" if s in w.persons else "not a person"] += 1
    out["act_subjects"] = dict(subj_rel)
    out["claim_sources"] = dict(Counter(c.source for p in w.persons.values() for c in p.ledger))
    return out


def creed_sweep(seasons: int = 2, seeds: tuple = (0, 1)) -> list:
    """`ED-IN-0229`'s instrument: does the faction creed change what people do, against a control?

    ⚠ **THE CONTROL ARM IS THE POINT AND IT IS BUILT BY REMOVING THE CAUSE, NOT BY EDITING THE
    RESULT.** `cast.faction_leader` is stubbed to `None` for the build, so every faction falls
    through `build_realm`'s own `template is None or lead_pid not in w.persons` branch to `HOLDS`,
    no creed is uttered and no stance row is written — the world this repository had before the
    ruling, produced by the same code path rather than by a second builder that could drift from
    it. Everything else (seed, cast, map, offices, holdings, wants) is identical between arms.

    ⚠ **AND IT SWEEPS `question_aggregation_rule`, WHICH IS WHY IT HAS TWO AXES INSTEAD OF ONE.**
    The creed's effect INVERTS across that fixture, and a single-arm run would have reported
    whichever sign the incumbent default happened to give. `H-54` owns the fixture; the reason the
    sign flips is the `q.id` tiebreak written out in `build_realm`'s membership block.

    Returns one row per (creed, rule, seed); `main --creed-sweep` prints them."""
    from ..data import cast as _cast
    rows = []
    for creed in (False, True):
        for rule in ("first", "all"):
            for seed in seeds:
                real = _cast.faction_leader
                if not creed:
                    _cast.faction_leader = lambda _f: None
                try:
                    w = build_realm(seed)
                finally:
                    _cast.faction_leader = real
                # ⚠ `.sweep()` RETURNS A NEW `Fixtures`; `_v[...] = rule` MUTATED THE SHARED ONE.
                # `World.__init__` stores `fixtures` BY REFERENCE and `build_realm` always passes
                # the module-level `DEFAULT_FIXTURES`, so writing through `_v` left the singleton
                # carrying the last arm's rule for the rest of the interpreter -- every later
                # `corpus_run`, `m1_acceptance` row and pytest test in that process silently
                # grading under `all` instead of the shipped `first`. A sweep that contaminates
                # the control is §0.1 pt 1's failure inside the instrument built to provide one.
                w.fixtures = w.fixtures.sweep("question_aggregation_rule", rule)
                out = run(seasons, seed, None, w=w)
                subj = out["act_subjects"]
                rows.append({
                    "creed": creed, "rule": rule, "seed": seed, "acts": out["acts"],
                    "other": subj.get("another person", 0), "self": subj.get("self", 0),
                    "not_a_person": subj.get("not a person", 0),
                    "told_by": out["claim_sources"].get("told_by", 0),
                    "stance_rows": sum(len(p.stance) for p in w.persons.values()),
                    "creeds": sum(1 for p in w.propositions.values()
                                  if p.id.startswith("fac_") and str(p.mood).upper() == "OUGHT"),
                })
    return rows


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--creed-sweep" in argv:
        argv.remove("--creed-sweep")
        n = int(argv[0]) if argv and argv[0].isdigit() else 2
        hdr = (f"{'creed':<6} {'rule':<6} {'seed':>4} {'acts':>6} {'other':>6} {'self':>6} "
               f"{'thing':>6} {'told':>5} {'stance':>7} {'creeds':>7}")
        print(f"THE CREED, AGAINST A CONTROL — {n} season(s) per arm (ED-IN-0229)")
        print(hdr); print("-" * len(hdr))
        for r in creed_sweep(n):
            print(f"{('yes' if r['creed'] else 'no'):<6} {r['rule']:<6} {r['seed']:>4} "
                  f"{r['acts']:>6} {r['other']:>6} {r['self']:>6} {r['not_a_person']:>6} "
                  f"{r['told_by']:>5} {r['stance_rows']:>7} {r['creeds']:>7}")
        return 0
    seasons = int(argv[0]) if argv and argv[0].isdigit() else 1
    cap = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else None
    w = build_realm(0, cap)
    c = census(w)
    print("THE POPULATED WORLD — one world, the canonical map, the corpus's own cast")
    print(f"  rungs by kind        {c['rungs']}")
    print(f"  persons              {c['persons']}   ({c['persons'] - c['cohorts']} one per season "
          f"loop; {c['cohorts']} cohort(s) of total weight {c['cohort_weight']}, `cohorts.yaml`)")
    print(f"  buildings inhabited  {c['distinct_buildings_inhabited']}"
          f"   (largest holds {c['largest_building']})")
    print(f"  sites                {c['sites']}")
    out = run(seasons, 0, cap, w=w)
    print(f"\n  after {seasons} season(s): {out['acts']} acts by {out['actors']} actors")
    print(f"  act subjects         {out['act_subjects']}")
    print(f"  claims by source     {out['claim_sources']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
