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
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import shape as S                                                     # noqa: E402
from trace_log import TRACE                                           # noqa: E402

CASE = "NPC-088"

# The three people #353 §13.1's worked case needs, and no more. `carin` makes the copies; `bailiff`
# is the person a copy can reach, so that a claim landing in SOMEONE ELSE'S ledger produces THEIR
# Q2 question -- which is the link check 2 walks. `warden` holds the rung.
CARIN, BAILIFF, WARDEN = "p_carin", "p_bailiff", "p_warden"


def build_world(seed: int = 0, fixtures: "S.Fixtures" = None) -> S.World:
    """Carin's world. Fixtures default to `DEFAULT_FIXTURES`, unmodified, so check 3's claim --
    that every number read resolves to a register `site:` -- is about the registered defaults and
    not about a set tuned for this run.

    ⚠ `fixtures` IS A PARAMETER BECAUSE THE FIRST VERSION BUILT THE WORLD FROM `DEFAULT_FIXTURES`
    AND THEN RAN IT ON WHATEVER WAS SWEPT. The site's starting `condition` came from the unswept
    default while the band floors and the wear came from the swept one, so a `condition_scale`
    sweep silently compared a site at 1000 against floors scaled to 10000 -- a confounded arm,
    which duly reported a "finding" that was the confound. Found while writing the sweep itself;
    §0.1 point 1 is the general form of it."""
    w = S.World(seed, fixtures or S.DEFAULT_FIXTURES)
    w.rungs["hearth_ostvik"] = S.Rung("hearth_ostvik", "hearth")
    w.rungs["ostvik"] = S.Rung("ostvik", "settlement")
    w.sites["scriptorium"] = S.Site("scriptorium", "hearth_ostvik", "body",
                                    condition=w.fixtures.get("condition_scale"))

    for pid, name in ((CARIN, "Carin Vedel"), (BAILIFF, "Uwe the bailiff"),
                      (WARDEN, "the warden")):
        w.persons[pid] = S.Person(pid, name)
    w.add_tenure(S.Tenure("t_carin_in", CARIN, "hearth_ostvik", "contain", since=0))
    w.add_tenure(S.Tenure("t_bailiff_in", BAILIFF, "hearth_ostvik", "contain", since=0))
    w.add_tenure(S.Tenure("t_warden_in", WARDEN, "ostvik", "contain", since=0))
    w.add_tenure(S.Tenure("t_hearth_in", "hearth_ostvik", "ostvik", "contain", since=0))

    # ⚠ HER MOTIVE IS A `commit` TO AN OUGHT PROPOSITION, WHICH IS Q4 -- the source `PLAN.md` `W5`
    # added and V2 §F1 omitted. Without it "an NPC with a standing ambition and a quiet season
    # forms no candidates at all", and Carin IS that NPC: nothing is due, nobody has told her
    # anything, and her subsistence has not moved. Q4 is the only reason she acts.
    prop = S.Proposition("prop_einhir", "OUGHT", "einhir_texts",
                         "the Einhir texts should survive", True, 0)
    w.propositions[prop.id] = prop
    w.add_tenure(S.Tenure("t_carin_commits", CARIN, prop.id, "commit", since=0))

    # Convictions read PERSON-SIDE ONLY, scored against `rosters.yaml`'s alignment table. These
    # are hers; nothing else in the loop reads them.
    # ⚠ THESE ARE WORLD DATA, NOT A DEFINITION, and the distinction is the one `rosters.yaml`
    # states: a roster or a table is a definition the GAME resolves from; a person's conviction
    # weight is a fact about that person, like their name. It is nonetheless load-bearing on the
    # result and saying so is owed — `Precedent: 0.9` against the alignment table's
    # `Precedent -> create_record: 0.9` is what puts `create_record` first in her ranking every
    # season, and therefore what starts the causal chain check 2 measures. A different Carin
    # produces a different season, which is the point of her having convictions at all.
    w.persons[CARIN].convictions = {"Precedent": 0.9, "self_preservation": 0.3}
    w.persons[BAILIFF].convictions = {"suspicion": 0.8, "Precedent": 0.4}
    w.persons[WARDEN].convictions = {"Precedent": 0.6}
    return w


def subsistence(p: S.Person, w: S.World) -> int:
    """The injected formula §42.2.1 requires. No in-chain document supplies one and S10.4 makes
    MatterKind an OPEN registry, so summing kinds as if fungible is a model choice this instrument
    may not make on the design's behalf. A person is at the scale unless a store says otherwise."""
    return w.fixtures.get("condition_scale")


def run(seasons: int = 2, seed: int = 0) -> dict:
    """Run Carin's season(s) and return the artifact. NOTHING HERE CHOOSES AN ACT."""
    w = build_world(seed)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    out = []
    for _ in range(seasons):
        # ⚠ NARROWED TO WHAT THE FOLD CAN EXECUTE, AND THE NARROWING IS COMPUTED, NOT AUTHORED.
        # `resolvable_verbs()` asks the fold which verbs it can carry through RESOLVE -- a verb
        # needs both a `requires:` predicate and, if it writes, an effect. Without this the season
        # HALTS on the first verb whose precondition is prose (`comply`: "a claim of the
        # dispensation's terms is in the actor's own ledger"), which is a true finding about the
        # specification and a different one from whether her season runs.
        #
        # ⚠ THIS IS THE HONEST CEILING ON ARTIFACT 2 AND IT IS REPORTED RATHER THAN HIDDEN:
        # Carin chooses from the resolvable subset, not from all 32. Which verbs those are moves
        # with `verb_table.yaml`, `REQUIRES_PREDICATES` and `EFFECTS`, so the number below is a
        # measurement of the specification's completeness, not a setting.
        # `H-87`: the contest depth cap is the CALLER's to supply (S39.3 refuses a default), and
        # artifact 2 never had to decide until Part E's `contests:` column became real and the
        # seam started firing on `kill / wound`.
        out.append(d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                            None, subsistence,
                            contest_max_depth=w.fixtures.get("contest_max_depth")))
    return dict(seasons=out, hash=w.content_hash(), world=w,
                events=len(w.log), acts=sum(s["acts"] for s in out),
                resolvable=len(S.resolvable_verbs()), verbs=len(S.VERB_TABLE))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--case", default=CASE)
    ap.add_argument("--seasons", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--log", action="store_true", help="print the Event log with its causes[]")
    a = ap.parse_args()
    if a.case != CASE:
        raise SystemExit(f"this artifact is {CASE}; `PLAN.md` §6.1 names the second case as "
                         "NPC-033 if she fails for a reason about her own rows")
    r = run(a.seasons, a.seed)
    print(f"{a.case} · {a.seasons} season(s) · seed {a.seed}")
    for n, s in enumerate(r["seasons"]):
        print(f"  season {n}: acts={s['acts']} events={s['events']} deposits={s['deposits']}")
    if a.log:
        for e in r["world"].log:
            print(f"    {e.kind:22} {e.subject:12} causes={e.causes}")
    print(f"  verbs the fold can execute: {r['resolvable']} of {r['verbs']}")
    print(f"CONTENT HASH: {r['hash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
