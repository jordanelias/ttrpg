"""`harness.scenarios` -- ONE REGISTRY OF SCENARIOS AND ONE LOOP THAT RUNS ANY OF THEM (`IS-B2-CORE-01`, `IS-B3-GO-01`).

A *scenario* is a standalone playable setup of one subsystem: a world, never a code path. `SCENARIOS` is the
one mapping from a name to its row; `run` is the one season loop that plays a row; every later entry
(`headless --world`, `play_surface --scenario`, `harness.valley`, `field_scene`, `governance_spine play`,
`storybar --world`, the port gate's `scenario:` names) resolves its name here and keeps no list of its own.

    python -m engine.season.harness.scenarios <name> --seed S --seasons K [--person P] [--play | --script FILE] [--developer]

THE ROW (`Scenario`, frozen):
  * `build(seed) -> World`    -- the world. A builder places a person through `boot/realm.py::place_person`; the `season`
                                 world (`carin.build_world`, moved from `headless`) and `inquiry_world` assign their rungs, offices and
                                 propositions directly AT BUILD, before any season (the apparatus's precedent: the hand-built worlds of `tests/`). A scenario whose opening
                                 situation is made by acts folds them inside `build`; the row has no field for them.
  * `seat(w) -> str`          -- the default seated person (`--person` overrides it). `None` is a row with NO default seat (`life`): `run` refuses
                                 a call with no `person`, and the command line prints the creation sheet and exits.
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
  * `reading(w, pid) -> str`  -- the row's own figure for the summary line (B11.76): a computed read of the world at the run's end, stored
                                 nowhere. `None` prints none.
  * `answer(w, pid) -> str`   -- what the world holds that the seated person does not, printed only under `--developer` and only after the
                                 run has ended, never per lap (B11.76, A-49: nothing is revealed in play). `None` prints none.

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
from ..data.rosters import COVERT_KINDS, SEEN_PREDICATE, faction_prop_id
from ..data.verbs import CONCLUDED_STEM
from ..decision.sheet import DevelopmentSheet, creation_sheet, development_space, seat as bind_seat, take_ranked
from ..boot.chooser import chooser
from ..boot.realm import build_realm, place_person, seed_goals
from ..gaps import Forbidden
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import world_q
from ..state.attribution import actor_of, anchor_of, causing_act, event_by_id, live_cover
from ..state.carriers import Act, Claim, Office, Proposition, Question, Rung, Tenure, generated_attributes
from ..state.gate import DISPOSABLE_KINDS, UNDECLARED_DISPOSAL
from ..state.ids import H, draw_factory
from ..state.world import World
from .flat_fold import flat_fold, flat_fold_fixtures      # the one place a world asks for the flat fold; `trail_world` is built at it
from . import probes as P
from .carin import build_world
from .play_surface import board, carry_on, dispatching_chooser

#: What an ending is for the seated person. The one closed tuple; a row's `kinds` values are members of it.
ENDING_KINDS = ("won", "lost", "drawn")


@dataclass(frozen=True, kw_only=True)
class Scenario:
    build: Callable[[int], World]
    seat: Optional[Callable[[World], str]]
    ending: Callable[[World, Optional[str], int], Optional[str]]
    verbs: Optional[frozenset] = None
    role: Optional[str] = None
    kinds: Mapping[str, str] = field(default_factory=dict)
    unreached: frozenset = frozenset()
    reading: Optional[Callable[[World, Optional[str]], str]] = None
    answer: Optional[Callable[[World, Optional[str]], str]] = None

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
        host=None, person: Optional[str] = None, on_build: Optional[Callable[[World], None]] = None,
        tie: Optional[Callable[[tuple], object]] = None) -> dict:
    """Play `SCENARIOS[name]` at `seed` for at most `seasons` seasons and stop at the first season whose end `ending`
    names one. `pick(sheet) -> indices` decides for the seated person (`person`, else the row's `seat`); `None` takes the
    shipped ranking whole. `tie(offer) -> Continuation` decides, between seasons, whom the seat passes to when he is dead and
    `play_surface.carry_on` offers his living ties (B11.79, `IS-B2-CHAR-01` (3)); `None` takes the first, `carry_on`'s own
    recorded revert. `host` is `SeasonDriver.season`'s own (`queries/inputs.py::PlayHost`). `on_build(w)` is called once with
    the built world before any season: a client that prints beside `pick` (the command line's board) keeps it; it is handed the
    world itself and is a reader by agreement, as `pick` is.

    Returns `{ending, kind, tick, hash, entries, seasons, seat_deliberations, premise, seat, passed, world}`: `ending` is the ending's name and
    `kind` its member of `ENDING_KINDS` (both `None` while the run goes on), `entries` CI-11's per-role entry counts
    (`harness/aperture.py::engines_entered`; `None` where it cannot count), `seasons` the number played, `seat_deliberations` how many
    times the seated space was asked, `premise` the ids of the acts the build folded (the run's own are the others), `seat` the person
    bound at the end (`None` once his line is extinct) and `passed` the persons the seat has been, in order (the first is the one he
    began as). An ending whose name the row's `kinds` does not hold is REFUSED, not labelled. A row with no `seat` and no `person`
    is REFUSED before it is built."""
    from . import aperture                                     # lazy: aperture imports harness modules a row may import in turn
    row = SCENARIOS[name]
    if person is None and row.seat is None:
        raise Forbidden(f"scenario {name!r} has no default seat and no person was given", "harness/scenarios.py::run",
                        needs="`person`: a `CreationRow.id` of the built world", law="IS-B2-CHAR-01 (1) -- the seat comes from `--person`")
    w = row.build(seed)
    if on_build is not None:
        on_build(w)
    premise = frozenset(a.id for a in w.acts)
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
    played = {"n": 0, "seat": pid}
    passed = [pid]
    take = (lambda offer: offer[0]) if tie is None else tie

    def loop() -> Optional[str]:
        bound, last = carry_on(w, overrides, pid, (), take)
        ended = row.ending(w, bound, seasons)
        while ended is None and played["n"] < seasons:
            d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"), host=host)
            played["n"] += 1
            if bound is not None:
                bound, last = carry_on(w, overrides, bound, last, take)
                if bound is not None and bound != passed[-1]:
                    passed.append(bound)
            ended = row.ending(w, bound, seasons - played["n"])
        played["seat"] = bound
        return ended

    ended, entries = aperture.engines_entered(loop)
    if ended is not None and ended not in row.kinds:
        raise Forbidden(f"scenario {name!r} ended {ended!r}, which its `kinds` {sorted(row.kinds)!r} does not hold",
                        "harness/scenarios.py::run", needs="a `kinds` entry beside every ending name the reader can return",
                        law="IS-B2-CORE-01 (1) -- every row states its `kinds` beside its endings")
    return {"ending": ended, "kind": None if ended is None else row.kinds[ended], "tick": w.tick,
            "hash": w.content_hash(), "entries": entries, "seasons": played["n"],
            "seat_deliberations": asked["n"], "premise": premise, "seat": played["seat"], "passed": tuple(passed), "world": w}


# ======================================================================================
# THE INQUIRY WORLDS (B11.70, `08_FI_03` §1): `trail_world`, moved here from `tests/test_fi03_trail.py` unchanged, and
# `inquiry_world`, the scenario built beside it; `trail_world` is no row, `inquiry_world` is the `inquiry` row's builder (B11.76, below).
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
LEAN_GOAL = "goal_riskbreakers_prevent_corruption"   # the `goals.yaml` row whose lean (`pursuits:`) the investigator's goal takes
CASE_GOAL = "goal_scenario_inquiry"  # the investigator's one goal: the Proposition id and the `data/goals.py` row's id
INQUIRY_CAST = ("p_forger", "p_holder", "p_witness", "p_investigator", "p_bench_a", "p_bench_b")


def inquiry_goal():
    """THE INVESTIGATOR'S ONE GOAL (`08_FI_07` §1, R-44: *the case is a goal*), a `data/goals.py` row parsed through the
    loader's own `parse`: its `object:` is `deed_doers` over `rosters.yaml: covert_kinds` -- the doers his OWN ledger names of
    any covert deed, `person_q.deed_doers` -- so its referents are his suspects, empty until his ledger names someone.
    [ASSUMPTION; medium; Jordan to correct] a scenario goal is authored in the builder as `build_realm`'s ambitions are,
    not drawn; its lean is READ off `goals.yaml`'s `goal_riskbreakers_prevent_corruption` row (`LEAN_GOAL`), the covert-deed goal the realm already authors, never retyped."""
    (g,) = goals_data.parse({"goals": [{
        "id": CASE_GOAL, "org": {"faction": "Valorsmark"}, "text": "an inquirer learns who did the covert deed",
        "object": {"kind": "deed_doers", "kinds": sorted(COVERT_KINDS)}, "pursuits": dict(goals_data.goal(LEAN_GOAL).pursuits),
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
    assert w.tick == CASE_OPENS, (w.tick, CASE_OPENS)
    return w


# ======================================================================================
# THE INQUIRY ROW (B11.76, `08_FI_03` §5, `08_FI_07` §4): `inquiry` is registered in `SCENARIOS` -- builder `inquiry_world`, the Cut A verb
# set, the investigator seated, four endings read off the world by `inquiry_ending`, and a summary line that is computed and stored nowhere.
# ======================================================================================
INVESTIGATOR_SEAT, INQUIRY_FORGER = "p_investigator", "p_forger"       # the seated person; the one who did the premise's forging
CASE_OPENS = 2          # the tick `inquiry_world` returns at (asserted there): the premise's forging at 0, its handover at 1
COLD_SEASONS = 4        # [canonical: proposals/2026-11-12-subsystem-audit-suite/proposals/08_FI_03_playable-inquiry.md §5] "four seasons pass"
#: `08_FI_07` §2.0's Cut A verb set, with `examine` (B11.72) and `reconstruct` (B11.73) added as their items landed. The chooser draws from it for everyone.
CUT_A_VERBS = frozenset({"research", "surveil", "petition", "carry", "open_case", "tell", "lie", "give", "survey", "create_record", "forge",
                         "conceal", "utter", "commit", "move", "examine", "reconstruct"})
INQUIRY_KINDS = {"determined": "won", "fled": "lost", "rests": "drawn", "cold": "drawn"}


def disposed(w: World) -> list:
    """The persons under a live disposal edge (`state/gate.py::DISPOSABLE_KINDS`: `oblige` imposed by a determination, `detain`, `ban`) on a seat a member
    of the bench at `TOWN` holds (`world_q.judging_set`): a bench has ruled on each, `_eff_determine` opens the edge on the seat exercised."""
    bench = set(world_q.judging_set(w, TOWN))
    seats = {t.object for t in w.tenures if t.kind == "hold" and t.live and t.subject in bench}
    return [t.subject for t in w.tenures if t.live and t.object in seats and t.kind in DISPOSABLE_KINDS and t.subject in w.persons
            and (t.kind != UNDECLARED_DISPOSAL or t.imposed)]


def concluded(w: World, investigator: Optional[str]) -> list:
    """`[(the one it was done to, deed kind, what he concluded)]`: the `concluded:` claims in `investigator`'s own ledger (`loop/witness.py` deposits them at
    WITNESS, B11.73); the third term is the doer's id, or `True` where a Partial left the deed alone."""
    p = w.persons.get(investigator)
    return [] if p is None else [(c.subject, c.predicate.partition(":")[2], c.value) for c in p.ledger
                                 if str(c.predicate).startswith(f"{CONCLUDED_STEM}:")]


def inquiry_ending(w: World, investigator: Optional[str]) -> Optional[str]:
    """THE INQUIRY'S ENDING, the first true of (`08_FI_03` §5; computed, stored nowhere), or `None`:
      * `determined` -- a live disposal edge on the bench's seat names a person (`disposed`);
      * `fled`       -- the forger's place is outside `world_q.reach` of the investigator (the forger has no place at all once he leaves the world);
      * `rests`      -- the investigator holds a `concluded:` claim. The source's second clause, *"and his season budget is spent"*, is true at every reading
                        the runner takes (it reads an ending between seasons, once the season's budget is gone), so no budget is read here; its
                        alternative, *"a petition of his on the docket"* stands only *before FI_03 §3 lands*, and B11.73 has landed it;
      * `cold`       -- `COLD_SEASONS` seasons have passed since the case opened (`CASE_OPENS`).
    A dead investigator with no continuation (`investigator` is `None`, or no longer in the world) leaves `fled` and `rests` unread, and `cold`
    still reads, so the run ends rather than running to the cap seatless."""
    if disposed(w):
        return "determined"
    p = w.persons.get(investigator)
    if p is not None:
        if world_q.home_of(w).get(INQUIRY_FORGER) not in world_q.reach(w, p):
            return "fled"
        if concluded(w, investigator):
            return "rests"
    return "cold" if w.tick - CASE_OPENS >= COLD_SEASONS else None


def seen_at_inquiries(w: World, investigator: Optional[str]) -> int:
    """How many distinct persons hold a `seen` claim naming `investigator` at one of his inquiries (`08_FI_07` §4, R-46: in place of the archived Exposure
    meter): a `seen` claim whose `who` is he, whose originating Event (`world_q.occasioned_by`, the claim's deposit and the Event it is about) his act of an
    inquiry verb (`aperture.inquiry_verbs`) caused. A read over ledgers at the run's end; no chooser reads it and no field holds it."""
    from . import aperture
    verbs = frozenset(aperture.inquiry_verbs())
    seers = set()
    for pid, p in w.persons.items():
        if pid == investigator:
            continue
        for c in p.ledger:
            if c.predicate != SEEN_PREDICATE or getattr(c.value, "who", None) != investigator or pid in seers:
                continue
            for eid in world_q.occasioned_by(w, Question(f"q:seen:{c.id}", "claim_landed", (), c.id)):
                a = causing_act(w, event_by_id(w, eid))
                if a is not None and a.actor == investigator and a.verb in verbs:
                    seers.add(pid)
                    break
    return len(seers)


def named_and_actor(w: World, investigator: Optional[str]) -> Optional[tuple]:
    """`(named, actors, named_is_actor)`: who the run's conclusion or accusation names and who did the Event it is about, or `None` where nobody is named. A
    `concluded:` claim naming a hand is the investigator's conclusion about `(the one it was done to, the deed kind)`: the actors are those of the
    Events of that kind that name the one it was done to (`anchor_of`, or a change of the Event's); where he concluded a deed alone (a Partial) nobody is named. With no
    conclusion, a person under `disposed` is the accused, and the Event is the premise's forging (`FORGE_ID`)."""
    for to, kind, hand in concluded(w, investigator):
        if isinstance(hand, str):
            actors = sorted({actor_of(w, e) for e in w.log if e.kind == kind and to in ({anchor_of(w, e)} | {c.subject for c in e.changes})} - {None})
            return hand, actors, hand in actors
    accused = disposed(w)
    if accused:
        forging = w.acts.get(FORGE_ID)
        actors = [] if forging is None else [forging.actor]
        return accused[0], actors, accused[0] in actors
    return None


def inquiry_reading(w: World, investigator: Optional[str]) -> str:
    """The `inquiry` row's figure on the summary line: `seen_at_inquiries`."""
    return f"seen by {seen_at_inquiries(w, investigator)}"


def inquiry_answer(w: World, investigator: Optional[str]) -> str:
    """What `--developer` prints at the run's end and nowhere else: whether the person the run named is the Event's actor (`named_and_actor`)."""
    got = named_and_actor(w, investigator)
    return "DEVELOPER · nobody was named" if got is None else (
        f"DEVELOPER · named {got[0]} · the Event's actor {', '.join(got[1]) or 'unknown'} · named is the actor: {'yes' if got[2] else 'no'}")


SCENARIOS["inquiry"] = Scenario(build=inquiry_world, seat=lambda w: INVESTIGATOR_SEAT, ending=lambda w, pid, left: inquiry_ending(w, pid),
                                verbs=CUT_A_VERBS, kinds=INQUIRY_KINDS, reading=inquiry_reading, answer=inquiry_answer)


# ======================================================================================
# THE LIFE ROW (B11.79, `IS-B2-CHAR-01`): the realm as built, a person of it seated by `--person`, and four endings read off the world.
# ======================================================================================
LIFE_KINDS = {"fulfilled": "won", "line_extinct": "lost", "realm_ended": "drawn", "unfinished": "drawn"}


def met_ambitions(w: World, pid: Optional[str]) -> list:
    """The ids of the ambitions (`world_q.ambitions`) of `pid` that `world_q.aim_state` reads `met` for him, in the order he holds them; `[]` for a
    person the world no longer holds. A read of the world: it stores nothing."""
    p = w.persons.get(pid)
    return [] if p is None else [a for a in world_q.ambitions(w, p) if world_q.aim_state(w, p, w.propositions[a]) == "met"]


def life_ending(w: World, pid: Optional[str], seasons_left: int) -> Optional[str]:
    """THE LIFE'S ENDING, the first true of (`IS-B2-CHAR-01` (2); computed, stored nowhere, read by no chooser), or `None`:
      * `line_extinct` -- `pid` is `None`: `carry_on` found no living tie to carry the seat on (read first, since no ambition can be read of nobody);
      * `fulfilled`    -- one of his ambitions reads `met` (`met_ambitions`);
      * `realm_ended`  -- `world_q.endings_reached(w)` is non-empty;
      * `unfinished`   -- no season is left."""
    if pid is None:
        return "line_extinct"
    if met_ambitions(w, pid):
        return "fulfilled"
    if world_q.endings_reached(w):
        return "realm_ended"
    return "unfinished" if seasons_left <= 0 else None


def life_reading(w: World, pid: Optional[str]) -> str:
    """The `life` row's figure on the summary line: which ambition of the seat's is met, else `no ambition met`."""
    met = met_ambitions(w, pid)
    return f"met {', '.join(met)}" if met else "no ambition met"


#: `seat=None`: no default person; `--person` names one. [ASSUMPTION; medium; Jordan to correct] `realm_ended` is `drawn` for every seat; B34 splits it by the seat's side as `IS-B3-GO-02` states for `season`.
SCENARIOS["life"] = Scenario(build=build_realm, seat=None, ending=life_ending, kinds=LIFE_KINDS, reading=life_reading)


def board_lines(w: World, pid: str) -> list:
    """The board's lines for `pid`, printed before each lap's offered acts: `play_surface.board(w.persons[pid], w.fixtures)` rendered one line a row (a `dossier` row, the suspects
    line, a held document). A person the world no longer holds has no board. It prints what he holds and nothing of the world's truth (A-49): a claim's own fields, its support
    and the ids of his claims that disagree with it."""
    p = w.persons.get(pid)
    lines: list = []
    for x in [] if p is None else board(p, w.fixtures):
        if x["kind"] == "claim":
            row = x["row"]
            c = row.claim
            via = f" via {'>'.join(c.chain)}" if c.chain else ""
            lines.append(f"held {c.subject} · {c.predicate} = {str(c.value)[:48]} · {c.source}{via} · confidence {c.confidence} · when {c.when} · support {row.support:.2f}"
                         + (f" · against {', '.join(row.against)}" if row.against else ""))
        elif x["kind"] == "suspects":
            lines.append(f"suspects ({x['goal']}): " + ("; ".join(f"{d} on {', '.join(x['by'][d])}" for d in x["doers"]) or "nobody named yet"))
        else:
            lines.append(f"document {x['id']} · {x['of']} · {x['about']}")
    return lines


def _parse(argv) -> argparse.Namespace:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.scenarios", description=__doc__.split("\n\n")[0])
    ap.add_argument("name", help="a name in SCENARIOS")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--seasons", type=int, default=1)
    ap.add_argument("--person", help="the seated person's id (default: the row's `seat`; a row with none, `life`, prints the creation sheet and exits)")
    how = ap.add_mutually_exclusive_group()
    how.add_argument("--play", action="store_true", help="read each pick from stdin: indices, blank takes the ranking whole")
    how.add_argument("--script", metavar="FILE", help="one line of indices per deliberation (and one index per offer of ties, once the seat is dead); once the file is spent the ranking is taken whole and the first tie")
    ap.add_argument("--developer", action="store_true", help="also print the sheet's budget, decisiveness, pursuits and tenures")
    return ap.parse_args(argv)


def _picker(a: argparse.Namespace, world: Optional[Callable[[], World]] = None) -> Callable[[DevelopmentSheet], list]:
    """The command line's `pick`. `world()` returns the built world (`run`'s `on_build`): with it each lap prints `board_lines` for the seated person between its
    header and the offered acts; without it the lap prints no board (a caller that has no world). `pick.tie` is the `tie` for `run` (B11.79): when the seat is dead
    and `carry_on` offers his living ties, it prints them and takes the index the script's next line (or stdin, under `--play`) gives, blank the first."""
    lines = open(a.script).read().splitlines() if a.script else []
    state = {"lap": 0, "read": 0}

    def next_line(prompt: str) -> str:
        if a.play:
            return input(prompt)
        state["read"] += 1
        return lines[state["read"] - 1] if state["read"] <= len(lines) else ""

    def tie(offer: tuple):
        print(f"-- the seat is dead; {len(offer)} tie(s) carry his line on")
        for i, c in enumerate(offer):
            print(f"   [{i}] {c.person} · {c.tie}")
        text = next_line("carry on as (index, blank = the first): ").strip()
        at = int(text) if text else 0
        if not 0 <= at < len(offer):
            raise SystemExit(f"{at} is not in the offer 0..{len(offer) - 1}")
        print(f"   carry on as {offer[at].person}")
        return offer[at]

    def pick(sheet: DevelopmentSheet) -> list:
        state["lap"] += 1
        print(f"-- lap {state['lap']} · {sheet.person_id} · budget {sheet.budget}")
        if a.developer:
            print(f"   decisiveness {sheet.decisiveness:.3f} · pursuits {dict(sheet.pursuits)} · tenures {list(sheet.tenures)}")
        if world is not None:
            for line in board_lines(world(), sheet.person_id):
                print(f"   {line}")
        for i, c in enumerate(sheet.candidates):
            print(f"   [{i}] {c.verb} {c.subject if c.subject is not None else ''}".rstrip())
        text = next_line("pick (indices, blank = take the ranking): ")
        chosen = [int(t) for t in text.replace(",", " ").split()] if text.strip() else list(take_ranked(sheet))
        print(f"   pick {chosen}")
        return chosen
    pick.tie = tie
    return pick


def main(argv=None) -> int:
    a = _parse(sys.argv[1:] if argv is None else argv)
    if a.name not in SCENARIOS:
        raise SystemExit(f"no scenario {a.name!r}; registered: {sorted(SCENARIOS) or 'none'}")
    from . import aperture                                     # lazy, as `run`'s is
    row = SCENARIOS[a.name]
    if row.seat is None and a.person is None:                  # a row with no default seat: the creation sheet is the pick list, and the run does not start
        print(f"{a.name} has no default seat; pass --person with one of:")
        for c in creation_sheet(row.build(a.seed).persons.values()):
            print(f"   {c.id} · {c.name} · pursuits {dict(c.pursuits)}")
        return 2
    built: list = []
    pick = _picker(a, lambda: built[0])
    r = run(a.name, a.seed, a.seasons, pick=pick, person=a.person, on_build=built.append, tie=pick.tie)
    w, seat = r["world"], r["seat"]
    null, total = aperture.null_reading(w, scope=lambda attempt: attempt[0].id not in r["premise"])
    line = f"{a.name} · seed {a.seed} · {r['seasons']} season(s) · tick {r['tick']} · ending {r['ending']} · kind {r['kind']} · seat {' > '.join(r['passed'])}"
    if row.reading is not None:
        line += f" · {row.reading(w, seat)}"
    print(f"{line} · null scenes {null}/{total}")                  # THE SUMMARY LINE (`IS-B2-CORE-03` (2), `08_FI_07` §4): one line, computed from the world
    for text in aperture.inquiry_lines(w, seat):
        print(text)
    if a.developer and row.answer is not None:                     # the run has ended: no lap prints this (A-49)
        print(row.answer(w, seat))
    print(f"CONTENT HASH: {r['hash']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
