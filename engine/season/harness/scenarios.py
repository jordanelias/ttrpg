"""`harness.scenarios` -- ONE REGISTRY OF SCENARIOS AND ONE LOOP THAT RUNS ANY OF THEM (`IS-B2-CORE-01`, `IS-B3-GO-01`).

A *scenario* is a standalone playable setup of one subsystem: a world, never a code path. `SCENARIOS` is the
one mapping from a name to its row; `run` is the one season loop that plays a row; every later entry
(`headless --world`, `play_surface --scenario`, `harness.valley`, `field_scene`, `governance_spine play`,
`storybar --world`, the port gate's `scenario:` names) resolves its name here and keeps no list of its own.

    python -m engine.season.harness.scenarios <name> --seed S --seasons K [--person P] [--play | --script FILE] [--developer]

THE ROW (`Scenario`, frozen):
  * `build(seed) -> World`    -- the world. A builder imports the realm's from `boot/realm.py` and places a person through
                                 `boot/realm.py::place_person`, assigning no store directly. A scenario whose opening
                                 situation is made by acts folds them inside `build`; the row has no field for them.
  * `seat(w) -> str`          -- the default seated person (`--person` overrides it).
  * `ending(w, pid, seasons_left) -> str | None` -- a reader of the world: the ending's name, or `None` while the run goes on.
                                 `pid` is the seated person now bound (`None` once `carry_on` found his line extinct) and
                                 `seasons_left` the seasons `run` has yet to play.
  * `kinds`                   -- from each name `ending` can return to a member of `ENDING_KINDS`: whether it is a win, a
                                 loss or a draw for the seated person. The row refuses a value outside the tuple at
                                 construction; `run` refuses an ending whose name `kinds` does not hold. A reader's
                                 whole range cannot be known at construction, so the second half is checked where the
                                 name is returned (`tests/test_scenarios_runner.py`, over every registered row).
  * `verbs`                   -- the verb set the chooser draws from; `None` is `resolvable_verbs()`.
  * `role`                    -- the composition role the scenario exists to enter, for the integrated check.
  * `unreached`               -- composition roles (members of `engine.substrate.composition.ROLES`) whose entry count must
                                 read 0 on this world; `run` returns the counts, no reader is added.

THE LOOP (`run`) is `populated.run`'s: the chooser comes from `boot/chooser.py::chooser`, the seat is bound through
`play_surface.dispatching_chooser`, `SeasonDriver.season` is called with the fixtures' `contest_max_depth`, a dead seat is
re-bound between seasons by `play_surface.carry_on`, and the run stops when `ending` names one. With `pick=None` the seat
takes the shipped ranking whole (`decision/sheet.py::take_ranked`), which is the automated run by construction.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from typing import Callable, Mapping, Optional

from ...substrate import composition
from ..data import goals as goals_data
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.rosters import COVERT_KINDS, faction_prop_id
from ..decision.sheet import DevelopmentSheet, creation_sheet, development_space, seat as bind_seat, take_ranked
from ..boot.chooser import chooser
from ..boot.realm import place_person, seed_goals
from ..gaps import Forbidden
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import world_q
from ..state.attribution import live_cover
from ..state.carriers import Act, Claim, Office, Proposition, Rung, Tenure, generated_attributes
from ..state.ids import H, draw_factory
from ..state.world import World
from ..tests._flat_fold import flat_fold, flat_fold_fixtures      # the one place a world asks for the flat fold; `trail_world` is built at it
from . import probes as P
from .headless import build_world
from .play_surface import carry_on, dispatching_chooser

#: What an ending is for the seated person. The one closed tuple; a row's `kinds` values are members of it.
ENDING_KINDS = ("won", "lost", "drawn")


@dataclass(frozen=True, kw_only=True)
class Scenario:
    build: Callable[[int], World]
    seat: Callable[[World], str]
    ending: Callable[[World, Optional[str], int], Optional[str]]
    verbs: Optional[frozenset] = None
    role: Optional[str] = None
    kinds: Mapping[str, str] = field(default_factory=dict)
    unreached: frozenset = frozenset()

    def __post_init__(self):
        object.__setattr__(self, "kinds", dict(self.kinds))
        bad = {n: k for n, k in self.kinds.items() if k not in ENDING_KINDS}
        if bad:
            raise Forbidden(f"ending kinds {bad!r} are outside {ENDING_KINDS!r}", "harness/scenarios.py::Scenario",
                            needs=f"each kind one of {ENDING_KINDS!r}", law="IS-B3-GO-01 (1) -- the closed tuple")
        unknown = sorted(r for r in self.unreached if r not in composition.ROLES)
        if unknown:
            raise Forbidden(f"unreached names {unknown!r}, which are not composition roles", "harness/scenarios.py::Scenario",
                            needs="members of engine.substrate.composition.ROLES", law="IS-B3-GO-01 (2)")
        if self.role is not None and self.role not in composition.ROLES:
            raise Forbidden(f"role {self.role!r} is not a composition role", "harness/scenarios.py::Scenario",
                            needs="a member of engine.substrate.composition.ROLES", law="IS-B2-CORE-01 (1)")


def season_ending(w: World, pid: Optional[str], seasons_left: int) -> Optional[str]:
    """The `season` row's reader: `realm_ended` when `world_q.endings_reached(w)` is non-empty; `line_extinct` when the seat
    has no person (`carry_on` found no living tie); `time` when no season is left; else `None`. In that order."""
    if world_q.endings_reached(w):
        return "realm_ended"
    if pid is None:
        return "line_extinct"
    return "time" if seasons_left <= 0 else None


#: The one mapping from a scenario's name to its row; every lane registers its own in its batch. `season` is Carin's case
#: (`headless.build_world`) as a played scenario, seated on its first person in id order; the world is built to need no role.
#: `IS-B3-GO-02` (B34) splits `realm_ended` by the seat's side.
SCENARIOS: dict[str, Scenario] = {
    "season": Scenario(build=build_world, seat=lambda w: sorted(w.persons)[0], ending=season_ending,
                       kinds={"realm_ended": "drawn", "line_extinct": "lost", "time": "drawn"}),
}


def run(name: str, seed: int, seasons: int, pick: Optional[Callable[[DevelopmentSheet], list]] = None,
        host=None, person: Optional[str] = None) -> dict:
    """Play `SCENARIOS[name]` at `seed` for at most `seasons` seasons and stop at the first season whose end `ending`
    names one. `pick(sheet) -> indices` decides for the seated person (`person`, else the row's `seat`); `None` takes the
    shipped ranking whole. `host` is `SeasonDriver.season`'s own (`queries/inputs.py::PlayHost`).

    Returns `{ending, kind, tick, hash, entries, seasons, seat_deliberations, world}`: `ending` is the ending's name and
    `kind` its member of `ENDING_KINDS` (both `None` while the run goes on), `entries` CI-11's per-role entry counts
    (`harness/aperture.py::engines_entered`; `None` where it cannot count), `seasons` the number played and
    `seat_deliberations` how many times the seated space was asked. An ending whose name the row's `kinds` does not hold
    is REFUSED, not labelled."""
    from . import aperture                                     # lazy: aperture imports harness modules a row may import in turn
    row = SCENARIOS[name]
    w = row.build(seed)
    verbs = resolvable_verbs() if row.verbs is None else row.verbs
    pid = row.seat(w) if person is None else person
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")      # `boot/chooser.py::chooser`'s own mint and draw
    draw = draw_factory(w.world_seed, lambda: w.tick)
    asked = {"n": 0}

    def counted(sheet):
        asked["n"] += 1
        return (take_ranked if pick is None else pick)(sheet)
    space = development_space(w.fixtures, mint, counted, verbs=verbs, draw=draw)
    overrides = bind_seat(creation_sheet(w.persons.values()), pid, space)
    choose = dispatching_chooser(chooser(w, verbs=verbs), overrides)
    d = SeasonDriver(w)
    played = {"n": 0}

    def loop() -> Optional[str]:
        bound, last = carry_on(w, overrides, pid, (), lambda offer: offer[0])
        ended = row.ending(w, bound, seasons)
        while ended is None and played["n"] < seasons:
            d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"), host=host)
            played["n"] += 1
            if bound is not None:
                bound, last = carry_on(w, overrides, bound, last, lambda offer: offer[0])
            ended = row.ending(w, bound, seasons - played["n"])
        return ended

    ended, entries = aperture.engines_entered(loop)
    if ended is not None and ended not in row.kinds:
        raise Forbidden(f"scenario {name!r} ended {ended!r}, which its `kinds` {sorted(row.kinds)!r} does not hold",
                        "harness/scenarios.py::run", needs="a `kinds` entry beside every ending name the reader can return",
                        law="IS-B2-CORE-01 (1) -- every row states its `kinds` beside its endings")
    return {"ending": ended, "kind": None if ended is None else row.kinds[ended], "tick": w.tick,
            "hash": w.content_hash(), "entries": entries, "seasons": played["n"],
            "seat_deliberations": asked["n"], "world": w}


# ======================================================================================
# THE INQUIRY WORLDS (B11.70, `08_FI_03` §1): `trail_world`, moved here from `tests/test_fi03_trail.py` unchanged, and
# `inquiry_world`, the scenario built beside it. Neither is registered in `SCENARIOS` here (B11.76 registers `inquiry`).
# ======================================================================================
FAC = faction_prop_id("Valorsmark")
FORGER, INVESTIGATOR, ABOUT = "p_other", "p_high", "p_mid"
FORGE_ID = "fi03_forge"


def hear(w, holder, subject):
    """Put a firsthand claim ON `subject` in `holder`'s own ledger -- what `survey`'s cell asks
    (`own_ledger`, *the surveyor has heard of it*). An existence observation, a stem the reader
    already answers, so the planted belief means nothing beyond *I know this exists*."""
    kind = ("Proposition" if subject in w.propositions else "Person" if subject in w.persons
            else "Rung")
    p = w.persons[holder]
    p.ledger.append(Claim(f"c_{holder}_{subject}_{len(p.ledger)}", holder, subject,
                          f"exists:{kind}", 1, w.tick, "firsthand", 1, "own"))


def step(w, d, *acts):
    """RESOLVE then WITNESS one lap of `acts` through the driver; the Events reach `w.log` between the
    two, as `SeasonDriver.season` puts them there. Returns the Events."""
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


COVER = "rec:cv"


def conceal_forger(w, d):
    """The forger takes a cover (`conceal`, through the fold) and a tick passes: `anchor_of` now answers `COVER` for his
    acts. Asserted, so no test below reads an uncovered world as a covered one."""
    assert [e.kind for e in step(w, d, Act(id="cv", actor=FORGER, verb="conceal", payload={"subject": FORGER}))] == [
        "cover.assumed"]
    assert live_cover(w, FORGER) == COVER
    w.tick += 1


def trail_world(verb="forge", kind="record.forged", second=None, fixtures=None, covered=False):
    """THE WORLD, built through the fold to the moment the investigator holds the forged Record (tick 2).
    Returns `(w, d, rid)`. `verb`/`kind`: the tick-0 act that mints the Record and the one Event it must
    emit -- `forge` by default; step 3's structural control passes `survey` (`faction.surveyed`), which
    mints the same Record id (the id is the act's) into the same hand by the same body (`_mint_sheet`).
    `second`: an act id for a SECOND such act by the same man at tick 0 (its own Record, which stays in
    his hand; `second_record` reads it back) -- the C1 test's second forging. `fixtures`: the arm the
    world is built at (v9 SC-02 `22b` step 25's sweeps), else `tiny_world`'s default AT THE FIXED CEILING
    ARM. ⚠ `ceiling_per_pool` (CP-T01-06, shipped True) is swept OFF here: these tests draw until a band
    lands, and they test the trail's closure and deposits, which no arm moves. Examining a forged Record
    composes an obstacle above 2 for a pool-2 investigator, and the per-pool cap lets it stand (2.842 at
    pool 2, against the fixed 2.0), so the draw odds F / P / S / O read 74 / 19 / 7 / 0 % at the fixed
    arm and 90 / 8.05 / 1.95 / 0 % at the shipped one: a hand band (Success or better) is 1.95 % per
    act, and the 60-id sweep, being seeded, does not reach one.

    `covered` (B11.58): the forger `conceal`s first (a live `cover`, `COVER`) and forges a tick later, so the forging
    anchors on the alias (`anchor_of`)."""
    if fixtures is None:
        fixtures = DEFAULT_FIXTURES.sweep("ceiling_per_pool", False)
    w = flat_fold(P.tiny_world(fixtures))   # the builder owns the flat fold: test_odds_of and test_sc02_22b build this world too, unmarked or on their own
    w.propositions[FAC] = Proposition(FAC, "HOLDS", "Valorsmark", "is a faction of this world", True, 0)
    for pid in (INVESTIGATOR, ABOUT):
        w.add_tenure(Tenure(f"t_commit_{pid}", pid, FAC, "commit", since=0))
    d = SeasonDriver(w)
    hear(w, FORGER, ABOUT)
    if covered:
        conceal_forger(w, d)
    out = step(w, d, Act(id=FORGE_ID, actor=FORGER, verb=verb, payload={"subject": ABOUT}))
    assert [e.kind for e in out] == [kind], [e.kind for e in out]
    (rid,) = [c.subject for c in out[0].changes]
    if second is not None:
        out = step(w, d, Act(id=second, actor=FORGER, verb=verb, payload={"subject": ABOUT}))
        assert [e.kind for e in out] == [kind], [e.kind for e in out]
    w.tick += 1
    assert [e.kind for e in step(w, d, Act(id="fi03_move", actor=FORGER, verb="move",
                                           payload={"to": "S"}))] == ["travel.moved"]
    assert [e.kind for e in step(w, d, Act(id="fi03_give", actor=FORGER, verb="give",
                                           payload={"subject": rid, "to": INVESTIGATOR}))] == [
        "record.given"]
    assert world_q.hold_force(w, rid).subject == INVESTIGATOR
    w.tick += 1
    return w, d, rid


# THE INQUIRY SCENARIO'S CAST AND PLACES. Ids of this builder's own world (as `trail_world`'s are), never game vocabulary.
FORGE_PLACE, HAND_PLACE, TOWN = "Hf", "Hw", "Sq"       # the hearths the sheet is forged at and handed over at, and the settlement they are in
CASE_GOAL = "goal_scenario_inquiry"  # the investigator's one goal: the Proposition id and the `data/goals.py` row's id
INQUIRY_CAST = ("p_forger", "p_holder", "p_witness", "p_investigator", "p_bench_a", "p_bench_b")


def inquiry_goal():
    """THE INVESTIGATOR'S ONE GOAL (`08_FI_07` §1, R-44: *the case is a goal*), a `data/goals.py` row parsed through the
    loader's own `parse`: its `object:` is `deed_doers` over `rosters.yaml: covert_kinds` -- the doers his OWN ledger names of
    any covert deed, `person_q.deed_doers` -- so its referents are his suspects, empty until his ledger names someone.
    [ASSUMPTION; medium; Jordan to correct] a scenario goal is authored in the builder as `build_realm`'s ambitions are,
    not drawn; its lean (`justice`, `virtue`) is `goals.yaml`'s `goal_riskbreakers_prevent_corruption`'s."""
    (g,) = goals_data.parse({"goals": [{
        "id": CASE_GOAL, "org": {"faction": "Valorsmark"}, "text": "an inquirer learns who did the covert deed",
        # [canonical: engine/season/goals.yaml §goal_riskbreakers_prevent_corruption] the lean 0.6 / 0.4 is that row's, copied
        "object": {"kind": "deed_doers", "kinds": sorted(COVERT_KINDS)}, "pursuits": {"justice": 0.6, "virtue": 0.4},
        "source": "B11.70 -- `harness/scenarios.py::inquiry_goal`"}]})
    return g


def inquiry_world(seed: int = 0) -> World:
    """THE INQUIRY WORLD (`08_FI_03` §1, B11.70): one settlement (`TOWN`, under a duchy and the realm, with two hearths:
    `FORGE_PLACE`, `HAND_PLACE`), six persons placed through `boot/realm.py::place_person` -- `p_forger` (at the forging hearth),
    `p_holder` and `p_witness` (at the handover hearth), and the investigator and the bench's two members (in the settlement) --
    the investigator and the two bench members each holding a seat that may `open_case` (`remit:determine`, scoped to the
    settlement, so the three are the bench `world_q.judging_set` finds there).

    The opening situation is made by the acts, folded as `trail_world`'s are and none planted but the forger's hearing of his
    subject (`hear`, the faction's own sheet): he `forge`s a sheet where nobody else stands, `move`s to the handover hearth and
    `give`s it to the holder with the witness standing by -- so the witness was at the handover and not at the forging, and the
    investigator, who stands at neither, holds nothing of either. The premise is folded with the task draw off (a failed forging
    leaves no sheet); the world is returned at the arm it was built with. The holder's act on the sheet is his own, in the season
    (none is folded here). The investigator holds one goal (`inquiry_goal`), seeded by `boot/realm.py::seed_goals`; the row is
    planted for the reader (`data/goals.py::plant`). No claim of the investigator's names the forger or the sheet."""
    w = World(world_seed=seed)
    for rid, kind, under in (("Rl", "realm", None), ("Dc", "duchy", "Rl"), (TOWN, "settlement", "Dc"), (FORGE_PLACE, "hearth", TOWN),
                           (HAND_PLACE, "hearth", TOWN)):
        w.rungs[rid] = Rung(rid, kind)
        if under is not None:
            w.add_tenure(Tenure(f"t_{rid}_in", rid, under, "contain", 0))
    w.propositions[FAC] = Proposition(FAC, "HOLDS", "Valorsmark", "is a faction of this world", True, 0)
    here = {"p_forger": FORGE_PLACE, "p_holder": HAND_PLACE, "p_witness": HAND_PLACE}
    for pid in INQUIRY_CAST:
        place_person(w, pid, pid[2:].replace("_", " "), here.get(pid, TOWN),
                     attributes=generated_attributes(w.world_seed, pid, w.fixtures.get("generated_attribute_range")))
    for pid, post in (("p_investigator", "Inquirer"), ("p_bench_a", "Magistrate"), ("p_bench_b", "Magistrate")):
        oid = f"off_{pid[2:]}"
        w.offices[oid] = Office(oid, post, TOWN, ["determine"], scope_rung=TOWN, faction="Valorsmark")
        w.add_tenure(Tenure(f"t_hold_{pid}", pid, oid, "hold", 0))
    w.add_tenure(Tenure("t_commit_p_investigator", "p_investigator", FAC, "commit", 0))
    hear(w, "p_forger", FAC)
    goal = inquiry_goal()
    goals_data.plant((goal,))
    seed_goals(w, (goal,), {}, {}, complete=False)
    played, w.fixtures = w.fixtures, flat_fold_fixtures(w.fixtures)   # the PREMISE is folded with the task draw off (a forging that failed leaves no sheet); the world plays at its own arm
    try:
        d = SeasonDriver(w)
        (sheet,) = [e for e in step(w, d, Act(id=FORGE_ID, actor="p_forger", verb="forge", payload={"subject": FAC}))
                    if e.kind == "record.forged"]
        (rid,) = [c.subject for c in sheet.changes]
        w.tick += 1
        for n, to in enumerate((TOWN, HAND_PLACE)):
            assert [e.kind for e in step(w, d, Act(id=f"inq_move_{n}", actor="p_forger", verb="move", payload={"to": to}))] == ["travel.moved"]
        assert [e.kind for e in step(w, d, Act(id="inq_give", actor="p_forger", verb="give",
                                               payload={"subject": rid, "to": "p_holder"}))] == ["record.given"]
    finally:
        w.fixtures = played
    w.tick += 1
    return w


def _parse(argv) -> argparse.Namespace:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.scenarios", description=__doc__.split("\n\n")[0])
    ap.add_argument("name", help="a name in SCENARIOS")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--seasons", type=int, default=1)
    ap.add_argument("--person", help="the seated person's id (default: the row's `seat`)")
    how = ap.add_mutually_exclusive_group()
    how.add_argument("--play", action="store_true", help="read each pick from stdin: indices, blank takes the ranking whole")
    how.add_argument("--script", metavar="FILE", help="one line of indices per deliberation; once the file is spent the ranking is taken whole")
    ap.add_argument("--developer", action="store_true", help="also print the sheet's budget, decisiveness, pursuits and tenures")
    return ap.parse_args(argv)


def _picker(a: argparse.Namespace) -> Callable[[DevelopmentSheet], list]:
    lines = open(a.script).read().splitlines() if a.script else []
    state = {"lap": 0}

    def pick(sheet: DevelopmentSheet) -> list:
        state["lap"] += 1
        print(f"-- lap {state['lap']} · {sheet.person_id} · budget {sheet.budget}")
        if a.developer:
            print(f"   decisiveness {sheet.decisiveness:.3f} · pursuits {dict(sheet.pursuits)} · tenures {list(sheet.tenures)}")
        for i, c in enumerate(sheet.candidates):
            print(f"   [{i}] {c.verb} {c.subject if c.subject is not None else ''}".rstrip())
        if a.play:
            text = input("pick (indices, blank = take the ranking): ")
        else:
            text = lines[state["lap"] - 1] if state["lap"] <= len(lines) else ""
        chosen = [int(t) for t in text.replace(",", " ").split()] if text.strip() else list(take_ranked(sheet))
        print(f"   pick {chosen}")
        return chosen
    return pick


def main(argv=None) -> int:
    a = _parse(sys.argv[1:] if argv is None else argv)
    if a.name not in SCENARIOS:
        raise SystemExit(f"no scenario {a.name!r}; registered: {sorted(SCENARIOS) or 'none'}")
    r = run(a.name, a.seed, a.seasons, pick=_picker(a), person=a.person)
    print(f"{a.name} · seed {a.seed} · {r['seasons']} season(s) · tick {r['tick']} · ending {r['ending']} · kind {r['kind']}")
    print(f"CONTENT HASH: {r['hash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
