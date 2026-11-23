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
from ..decision.sheet import DevelopmentSheet, creation_sheet, development_space, seat as bind_seat, take_ranked
from ..boot.chooser import chooser
from ..gaps import Forbidden
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.ids import H, draw_factory
from ..state.world import World
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
