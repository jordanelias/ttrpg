"""ARTIFACT 2 — ONE NPC SEASON, END TO END. `PLAN.md` Part 6, work item `W9`.

    python headless.py --case NPC-088 --seasons 2 --seed 0

> ### THE TESTED VERSION RAN ZERO CASES END TO END. ONE IS AN INFINITE IMPROVEMENT OVER ZERO, AND
> ### IT IS THE ONLY NUMBER THAT WOULD PROVE ANY OF THIS.

`PLAN.md` §6.1 chose NPC-088, Carin Vedel, a copyist with no institutional position, on four
grounds: #353 §13.1 already narrates her season as the worked lawful case; her only routed blocker
is `P22`, which Part D rules; her needs exercise the largest number of ruled rows (a Record with
ACT-DECLARED stages, MATTER maturation, a `hold` on a Record, `(Person, exists)` as an ending);
and she needs no sitting, no contest and no dispensation -- the three places a default is still
being injected. **Her season tests the loop rather than the defaults.**

⚠ WHAT THIS FILE IS NOT. It is not a scenario author. Every act Carin takes is chosen by
`make_chooser` -- §F2's policy, scoring her own convictions against the alignment table -- from an
option set `opening_set` COMPUTES from `verb_table.yaml`. There is no roster, no `effect` lambda
and no branch on her name anywhere below. What this file supplies is a WORLD: the people, the
rung, the site and the question sources #353 §13.1 describes. If a season of hers is uninteresting
that is a finding about Parts D-F, not something to fix here by scripting her.

The six checks of `PLAN.md` §6.3 are executed by
`test_tracer_is_honest.py::test_w9_*`, which import `build_world` and `run` from here. Check 2 --
a causal chain of at least four Events walking from her own act -- is the one that cannot be faked,
and check 3 -- every fixture read resolving to a `site:` on `hole_register.yaml` -- is `V2` §G's
central claim made falsifiable.
"""
from __future__ import annotations

import argparse

from ..data.verbs import VERB_TABLE
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.attribution import anchor_of
from ..trace_log import TRACE
from . import probes as P

CASE = "NPC-088"

# The three people #353 §13.1's worked case needs, and the world that holds them, are `carin.py`'s (a leaf `scenarios.py` reads too); re-bound here for every importer.
from .carin import BAILIFF, CARIN, WARDEN, build_world  # noqa: E402,F401


def run(seasons: int = 2, seed: int = 0) -> dict:
    """Run Carin's season(s) and return the artifact. NOTHING HERE CHOOSES AN ACT."""
    w = build_world(seed)
    d = SeasonDriver(w)
    out = []
    for _ in range(seasons):
        # ⚠ NARROWED TO WHAT THE FOLD CAN EXECUTE, AND THE NARROWING IS COMPUTED, NOT AUTHORED.
        # `resolvable_verbs()` asks the fold which verbs it can carry through RESOLVE -- a verb
        # needs both a `requires:` predicate and, if it writes, an effect. Without this the season
        # HALTS on the first verb whose precondition is prose (`comply`, `evade / defy`, `construe` and
        # `exchange` were the examples until v9 IN-09 and IN-33 typed their cells, restored at v10
        # REM-2B; `tie / knot` is the row still left out, for want of an effect; `succeed` has had one since v10 IN-61), which
        # is a true finding about the specification and a different one from whether her season runs.
        #
        # ⚠ THIS IS THE HONEST CEILING ON ARTIFACT 2 AND IT IS REPORTED RATHER THAN HIDDEN:
        # Carin chooses from the resolvable subset, not from all 32. Which verbs those are moves
        # with `verb_table.yaml`, `REQUIRES_PREDICATES`, `requires_typed:` and `EFFECTS`, so the
        # number below is a measurement of the specification's completeness, not a setting.
        # ⚠ `requires_typed:` JOINED THAT LIST IN `W-A` and this comment did not say so until the
        # adversarial pass read it: `resolvable_verbs` now admits a verb whose precondition is a
        # TYPED CELL as well as one carrying a hand-written predicate.
        # `H-87`: the contest depth cap is the CALLER's to supply (S39.3 refuses a default), and
        # artifact 2 never had to decide until Part E's `contests:` column became real and the
        # seam started firing on `kill / wound`.
        out.append(d.season(P.chooser(w, verbs=resolvable_verbs()),
                            None,
                            contest_max_depth=w.fixtures.get("contest_max_depth")))
    return dict(seasons=out, hash=w.content_hash(), world=w,
                events=len(w.log), acts=sum(s["acts"] for s in out),
                resolvable=len(resolvable_verbs()), verbs=len(VERB_TABLE))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--case", default=CASE)
    ap.add_argument("--seasons", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--log", action="store_true", help="print the Event log with its causes[]")
    ap.add_argument("--world", help="a name in `harness/scenarios.py::SCENARIOS`; plays it with that registry's `run` instead of Carin's case")
    how = ap.add_mutually_exclusive_group()
    how.add_argument("--auto", action="store_true", help="with --world: every decider in a sitting is the engine's (the default; named so a command line says which)")
    how.add_argument("--play", nargs="?", const="", metavar="ID", help="with --world: the person ID (default: the row's seat) makes his own moves in a sitting, one option index a line from "
                                                                         "stdin (blank: the first); every other decider and every act of the season is the engine's")
    a = ap.parse_args()
    if a.world is None and (a.auto or a.play is not None):
        raise SystemExit("--auto and --play are modes of a scenario: name one with --world")
    if a.world is not None:
        from . import scenarios                    # lazy: the registry is the one owner of names, this file keeps no list
        if a.world not in scenarios.SCENARIOS:
            raise SystemExit(f"no scenario {a.world!r}; registered: {sorted(scenarios.SCENARIOS) or 'none'}")
        who = None
        if a.play is not None:
            row = scenarios.SCENARIOS[a.world]
            who = a.play or (None if row.seat is None else row.seat(row.build(a.seed)))
            if who is None:
                raise SystemExit(f"{a.world} has no default seat: --play takes a person id")
        r = scenarios.run(a.world, a.seed, a.seasons, host=None if who is None else scenarios.played_host(who), person=who)
        print(f"{a.world} · {r['seasons']} season(s) · seed {a.seed} · tick {r['tick']} · ending {r['ending']} · kind {r['kind']}")
        print(f"CONTENT HASH: {r['hash']}")
        return 0
    if a.case != CASE:
        raise SystemExit(f"this artifact is {CASE}; `PLAN.md` §6.5 (was §6.1 before the 2026-09-02 rewrite) names the second case as "
                         "NPC-033 if she fails for a reason about her own rows")
    r = run(a.seasons, a.seed)
    print(f"{a.case} · {a.seasons} season(s) · seed {a.seed}")
    for n, s in enumerate(r["seasons"]):
        # `rounds=` (the lap count, its key kept) since `U2`: a ticked season and a one-pass one are indistinguishable in this
        # line without it. See `SeasonDriver.season`'s return for why no Event carries a lap.
        print(f"  season {n}: rounds={s['rounds']} acts={s['acts']} events={s['events']} "
              f"deposits={s['deposits']}")
    if a.log:
        # G1b: `Event.subject` is gone; `anchor_of` is what it was -- the actor where one acted,
        # the written thing otherwise -- and `-` where nothing says (an `anchor_of` of `None`).
        w = r["world"]
        for e in w.log:
            print(f"    {e.kind:22} {anchor_of(w, e) or '-':12} causes={e.causes}")
    print(f"  verbs the fold can execute: {r['resolvable']} of {r['verbs']}")
    print(f"CONTENT HASH: {r['hash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
