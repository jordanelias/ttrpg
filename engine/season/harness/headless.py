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

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.convictions import conviction as _conv
from ..data.verbs import VERB_TABLE
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import Person, Proposition, Rung, Site, Tenure
from ..state.ids import H, draw_factory
from ..state.world import World
from ..trace_log import TRACE

CASE = "NPC-088"

# The three people #353 §13.1's worked case needs, and no more. `carin` makes the copies; `bailiff`
# is the person a copy can reach, so that a claim landing in SOMEONE ELSE'S ledger produces THEIR
# Q2 question -- which is the link check 2 walks. `warden` holds the rung.
CARIN, BAILIFF, WARDEN = "p_carin", "p_bailiff", "p_warden"


def build_world(seed: int = 0, fixtures: "S.Fixtures" = None) -> World:
    """Carin's world. Fixtures default to `DEFAULT_FIXTURES`, unmodified, so check 3's claim --
    that every number read resolves to a register `site:` -- is about the registered defaults and
    not about a set tuned for this run.

    ⚠ `fixtures` IS A PARAMETER BECAUSE THE FIRST VERSION BUILT THE WORLD FROM `DEFAULT_FIXTURES`
    AND THEN RAN IT ON WHATEVER WAS SWEPT. The site's starting `condition` came from the unswept
    default while the band floors and the wear came from the swept one, so a `condition_scale`
    sweep silently compared a site at 1000 against floors scaled to 10000 -- a confounded arm,
    which duly reported a "finding" that was the confound. Found while writing the sweep itself;
    §0.1 point 1 is the general form of it."""
    w = World(seed, fixtures or DEFAULT_FIXTURES)
    w.rungs["hearth_ostvik"] = Rung("hearth_ostvik", "hearth")
    w.rungs["ostvik"] = Rung("ostvik", "settlement")
    w.sites["scriptorium"] = Site("scriptorium", "hearth_ostvik", "body",
                                    condition=w.fixtures.get("condition_scale"))

    for pid, name in ((CARIN, "Carin Vedel"), (BAILIFF, "Uwe the bailiff"),
                      (WARDEN, "the warden")):
        w.persons[pid] = Person(pid, name)
    w.add_tenure(Tenure("t_carin_in", CARIN, "hearth_ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_bailiff_in", BAILIFF, "hearth_ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_warden_in", WARDEN, "ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_hearth_in", "hearth_ostvik", "ostvik", "contain", since=0))

    # ⚠ HER MOTIVE IS A `commit` TO AN OUGHT PROPOSITION, WHICH IS Q4 -- the source `PLAN.md` `W5`
    # added and V2 §F1 omitted. Without it "an NPC with a standing ambition and a quiet season
    # forms no candidates at all", and Carin IS that NPC: nothing is due, nobody has told her
    # anything, and her subsistence has not moved. Q4 is the only reason she acts.
    prop = Proposition("prop_einhir", "OUGHT", "einhir_texts",
                         "the Einhir texts should survive", True, 0)
    w.propositions[prop.id] = prop
    w.add_tenure(Tenure("t_carin_commits", CARIN, prop.id, "commit", since=0))

    # Convictions read PERSON-SIDE ONLY, scored against `rosters.yaml`'s alignment table. These
    # are hers; nothing else in the loop reads them.
    # ⚠ THESE ARE WORLD DATA, NOT A DEFINITION, and the distinction is the one `rosters.yaml`
    # states: a roster or a table is a definition the GAME resolves from; a person's conviction
    # weight is a fact about that person, like their name. It is nonetheless load-bearing on the
    # result and saying so is owed — `Precedent: 0.9` against the alignment table's
    # `Precedent -> create_record: 0.9` is what puts `create_record` first in her ranking every
    # season, and therefore what starts the causal chain check 2 measures. A different Carin
    # produces a different season, which is the point of her having convictions at all.
    # ⚠ `U3`: THESE ARE CONVICTIONS NOW, AND TWO OF THE OLD THREE NAMES WERE NEVER CONVICTIONS.
    # The line read `{"Precedent": 0.9, "self_preservation": 0.3}` / `{"suspicion": 0.8, ...}` /
    # `{"Precedent": 0.6}` — `Precedent` IS one of the thirteen and survives unchanged, while
    # `self_preservation` and `suspicion` were ad-hoc scalars the old four-name roster carried and
    # are not things a person can believe. They are replaced by the conviction each was standing
    # in for, at the same weight, so the three people keep the characters the docstring above
    # describes:
    #   * `self_preservation` -> `Utility`  — "effectiveness, results, instrumental judgment"
    #     (`conviction_taxonomy_v30.md` §2). The old cells priced it as caution about exposure and
    #     cost, which is the instrumental reading.
    #   * `suspicion`        -> `Order`     — "procedural correctness, rule-following". The old
    #     `suspicion` block's own cells were `open_case: 0.9` and `surveil: 0.9`, i.e. the reach
    #     for the institution and the reach without it; the bailiff is the procedural one.
    # ⚠ THIS IS A SUBSTITUTION AND IT IS DECLARED AS ONE. Nothing in canon maps the three retired
    # names onto the thirteen; the mapping above is argued from the old cells' own reasons and is
    # this harness's choice, not a reading of `conviction_axis_matrix_v30.md`. `H-46` stays open.
    # ⚠⚠ **EACH NAME IS LOOKED UP IN THE OWNER RATHER THAN TYPED, AND THE GUARD THAT FORCED THIS
    # IS RIGHT EVEN THOUGH ITS FIRST READING OF THESE LINES WAS NOT.**
    # `tests/valoria/test_conviction_roster_single_owner.py` fails on any literal holding TWO OR
    # MORE canonical conviction names, because three incompatible rosters once shipped at the same
    # time and silently disabled ED-912 §6.1's Conviction Scar. `{"Precedent": 0.9, "Utility": 0.3}`
    # is two canonical names in one dict, so it read as a roster fragment — and the distinction
    # between a ROSTER (an enumeration that can drift out of step with the owner) and a REFERENCE
    # (a choice of one member) is not one an AST scan can draw.
    # `_conv` draws it by CONSTRUCTION rather than by argument: one name per call, each checked
    # against `CONVICTIONS`, which IS `engine.substrate.descriptors.CONVICTIONS` — the same object,
    # not a copy. A rename in `references/descriptor_registry.yaml` now raises here by name instead
    # of silently seeding a conviction nobody holds, which is strictly more than the literals did.
    # [JUSTIFIED: these five weights are AUTHORED CHARACTER, not a mechanical constant -- #353 §14 types convictions as "weights over the closed 13 | 1-3 primary + distributed" and supplies no magnitudes. Carin at Precedent 0.9 is what the docstring above explains starts her causal chain; the rest are her, the bailiff and the warden being three different people. `H-46` is the row and it is open]
    w.persons[CARIN].convictions = {_conv("Precedent"): 0.9, _conv("Utility"): 0.3}
    # [JUSTIFIED: as the line above -- authored character under `H-46`, not a mechanical constant. The bailiff is procedural-first (Order 0.8) and the warden holds one conviction weakly, which is what makes the three people three]
    w.persons[BAILIFF].convictions = {_conv("Order"): 0.8, _conv("Precedent"): 0.4}
    # [JUSTIFIED: as above -- one conviction, held weakly; the warden is the least opinionated of the three by design]
    w.persons[WARDEN].convictions = {_conv("Precedent"): 0.6}
    return w


def subsistence(p: Person, w: World) -> int:
    """The injected formula §42.2.1 requires. No in-chain document supplies one and S10.4 makes
    MatterKind an OPEN registry, so summing kinds as if fungible is a model choice this instrument
    may not make on the design's behalf. A person is at the scale unless a store says otherwise."""
    return w.fixtures.get("condition_scale")


def run(seasons: int = 2, seed: int = 0) -> dict:
    """Run Carin's season(s) and return the artifact. NOTHING HERE CHOOSES AN ACT."""
    w = build_world(seed)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
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
        # with `verb_table.yaml`, `REQUIRES_PREDICATES`, `requires_typed:` and `EFFECTS`, so the
        # number below is a measurement of the specification's completeness, not a setting.
        # ⚠ `requires_typed:` JOINED THAT LIST IN `W-A` and this comment did not say so until the
        # adversarial pass read it: `resolvable_verbs` now admits a verb whose precondition is a
        # TYPED CELL as well as one carrying a hand-written predicate.
        # `H-87`: the contest depth cap is the CALLER's to supply (S39.3 refuses a default), and
        # artifact 2 never had to decide until Part E's `contests:` column became real and the
        # seam started firing on `kill / wound`.
        out.append(d.season(make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                                         draw=draw_factory(w.world_seed, lambda: w.tick)),
                            None, subsistence,
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
    a = ap.parse_args()
    if a.case != CASE:
        raise SystemExit(f"this artifact is {CASE}; `PLAN.md` §6.5 (was §6.1 before the 2026-09-02 rewrite) names the second case as "
                         "NPC-033 if she fails for a reason about her own rows")
    r = run(a.seasons, a.seed)
    print(f"{a.case} · {a.seasons} season(s) · seed {a.seed}")
    for n, s in enumerate(r["seasons"]):
        # `rounds` since `U2`: a ticked season and a one-pass one are indistinguishable in this
        # line without it. See `SeasonDriver.season`'s return for why no Event carries a round.
        print(f"  season {n}: rounds={s['rounds']} acts={s['acts']} events={s['events']} "
              f"deposits={s['deposits']}")
    if a.log:
        for e in r["world"].log:
            print(f"    {e.kind:22} {e.subject:12} causes={e.causes}")
    print(f"  verbs the fold can execute: {r['resolvable']} of {r['verbs']}")
    print(f"CONTENT HASH: {r['hash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
