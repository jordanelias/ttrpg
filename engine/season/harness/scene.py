"""`harness.scene` -- ONE MODULE'S SCENE INSTANCE, RUN ALONE FROM A SMALL WORLD (B34.15; `01_CORE_one_scene_contract` edit 4).

    python -m engine.season.harness.scene combat.fight --fixture fight_headless --seed 0

A *scene instance* is one module's playable form: one act's scene, staged from a small world, by the SAME entry the season's fold calls (the glossary's row
*scene instance*; Layer 1's `Scene`, what the budget counts, keeps its own sense). `play(role, fixture, ...)` is an instrument: it adds no rule, reads no file a
module does not already receive, and holds no loop of its own.

  * `apply=False` -- calls `seam.contest` (`seam/contest.py::contest`), NOT the provider, with the arguments `loop/resolve.py::_contest` passes, so the depth cap
    and the one ladder run: a result carries the degree `seam/ladder.py::degree_of` grades it at, and a world whose `max_depth` the fixture sets to 0 is refused
    with the seam's own typed `ContestError("max_depth reached")`. THE ACT IS RECORDED IN THE WORLD'S ACT STORE FIRST, as RESOLVE records it (`w.acts.append`), so the
    provider reads the same `combat_input` it reads in a season. NOT ASKED HERE (A-63): the counterparty's received-scene debit and the `engaged` clause; both
    belong to the fold, and the record names them under `not_asked`.
  * `apply=True` -- runs a ONE-ACT SEASON through `SeasonDriver.season`, the act being the one thing `choose` returns, so the fold's `writes_at(degree)` and
    emissions happen and the returned world carries the consequences (the counterparty's debit and the `engaged` clause included, once B28 lands them in the fold).

THE GENERATOR is the keyed stream `draw_factory(world_seed, tick)(actor, "roll:<prize>:<act id>")` -- the purpose `_contest` gives the act's own stream, so the
standalone call and the season's draw the same key for one act in one world at one tick (A-30: one draw per key, no recorder).

`decide` (the host's decider for `role`) is handed in as `PlayHost(persons={actor}, deciders={role: decide})`; with none, no host: AUTOMATED, as every season is.

A FIXTURE is a dict: `role` (a `composition.json` role), `build` (`seed -> World`), `act` (`id`, `actor`, `verb`, `payload`) and, optionally, `max_depth` (absent:
the world's own `contest_max_depth`, which a season passes, S39.3). `FIXTURES` holds the ones whose builders exist. Its caller: the gate command above and the
module lanes' standalone instructions (B20's field, B30's nesting); no other file imports it.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable, Optional

from ..data.verbs import VERB_TABLE
from ..loop.driver import SeasonDriver
from ..loop.sides import _contests_of, seat_named_by, sides_of
from ..queries.inputs import PlayHost
from ..seam import ContestError, ContestRefused, contest, degree_of
from ..seam.wrappers.sigma import arranged_by, topic_of
from ..state.carriers import Act, effort_of
from ..state.ids import draw_factory
from .carin import BAILIFF, CARIN, build_world as carin_world

#: THE FIXTURES, by name. `fight_headless` is the headless world (`carin.build_world`, Carin's three people) with an authored `fight` between its first two
#: persons: the `[ASSUMPTION]` of `01_CORE_one_scene_contract` edit 4. `duel` (`duel_scene.build`, `IS-PC-01` step 6) is NOT here: its builder was retired unbuilt
#: (`hole_register.yaml` H-580) and the name waits on the redesign.
FIXTURES: dict[str, dict] = {
    "fight_headless": dict(role="combat.fight", build=carin_world,
                           act=dict(id="scene_0", actor=CARIN, verb="fight", payload={"subject": BAILIFF})),
}

#: What an `apply=False` record says it did not ask (A-63; `28_CORE_scene_access_A` §2, §3): both are the fold's, so a standalone call without the fold omits them.
NOT_ASKED = ("the counterparty's received-scene debit", "the `engaged` clause (A-63)")


def _act(spec: dict) -> Act:
    return Act(id=spec["id"], actor=spec["actor"], verb=spec["verb"], payload=dict(spec.get("payload") or {}))


def _checked(role: str, fixture: dict) -> None:
    if fixture.get("role") != role:
        raise ValueError(f"fixture stages role {fixture.get('role')!r}, not {role!r}: a decider for {role!r} would never be asked")


def play(role: str, fixture: dict, *, seed: int = 0, decide: Optional[Callable] = None, apply: bool = False) -> dict:
    """One module's scene, alone. Returns a record: `role`, `seed`, `act`, `played` (a decider was handed in), `max_depth`, `status` (`RESOLVED`, a typed refusal's
    status, or `DEPTH-CAPPED`), `degree` (the one ladder's, `None` for a refusal), `result` (the provider's own return, `apply=False`) or `events` and `world`
    (`apply=True`), and `content_hash`. `apply=False` also carries `not_asked`."""
    _checked(role, fixture)
    w = fixture["build"](seed)
    act = _act(fixture["act"])
    host = None if decide is None else PlayHost(frozenset({act.actor}), deciders={role: decide})
    max_depth = fixture.get("max_depth", w.fixtures.get("contest_max_depth"))
    record: dict[str, Any] = dict(role=role, seed=seed, apply=apply, played=decide is not None, max_depth=max_depth,
                                  act=dict(id=act.id, actor=act.actor, verb=act.verb, payload=dict(act.payload)))
    driver = SeasonDriver(w)              # built in both modes: the registrar fills the module entries here, and a season needs the driver anyway
    if apply:
        _season(driver, act, max_depth, host)
        caused = [(e.kind, e.degree) for e in w.log if act.id in e.causes]
        graded = [d for _, d in caused if d is not None]
        return dict(record, status="FOLDED" if graded else "UNGRADED", degree=graded[-1] if graded else None, events=caused, world=w,
                    content_hash=w.content_hash())
    row = VERB_TABLE[act.verb]
    contests = _contests_of(act, row)
    if not contests:
        raise ValueError(f"verb {act.verb!r} contests no prize: there is no scene to stage")
    prize = contests[0]
    target = act.payload.get(row.opponent_operand())
    parties, subject, rung = sides_of(w, act, target, prize)
    w.acts.append(act)                    # RESOLVE records the act before it reaches the seam (`combat.py::_cause_act` reads it back)
    topic = topic_of(act, subject)
    arranger, rig = arranged_by(w, act, topic)
    rng = draw_factory(w.world_seed, lambda: w.tick)(act.actor, f"roll:{prize}:{act.id}")
    got = contest(w, rung=rung, prize=prize, claimants=parties, depth=0, max_depth=max_depth, causes=[act.id], verb=act.verb, subject=subject, rng=rng,
                  effort=effort_of(act), host=host, via=act.via, act=act, topic=topic, arranger=arranger, rig=rig, seat=seat_named_by(w, act, prize))
    record.update(not_asked=NOT_ASKED, prize=prize, content_hash=w.content_hash())
    if isinstance(got, ContestError):
        return dict(record, status="DEPTH-CAPPED", degree=None, refusal=got.reason, result=None)
    if isinstance(got, ContestRefused):
        return dict(record, status=got.status, degree=None, refusal=got.why, result=None)
    return dict(record, status=got["status"], degree=degree_of(got, subject, w.fixtures), result=got)


def _season(driver: Any, act: Act, max_depth: Optional[int], host: Optional[PlayHost]) -> None:
    """A ONE-ACT SEASON: `act` is what its actor's `choose` returns and every other person's `choose` returns nothing. The one loop, `SeasonDriver.season`."""
    def choose(p: Any, v: Any, s: Any, ask_budget: Callable[[], int]) -> list:
        return [act] if p.id == act.actor else []
    driver.season(choose, None, contest_max_depth=max_depth, host=host)


def _plain(record: dict) -> dict:
    """The record as the command prints it: the world and the module's trace stay in the process."""
    out = {k: v for k, v in record.items() if k != "world"}
    if isinstance(out.get("result"), dict):
        out["result"] = {k: v for k, v in out["result"].items() if k != "trace"}
    return out


def main(argv: Optional[list] = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.scene", description=__doc__.split("\n\n")[0])
    ap.add_argument("role", help="a module role the fixture stages (`combat.fight`)")
    ap.add_argument("--fixture", required=True, choices=sorted(FIXTURES), help="a name in FIXTURES")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--apply", action="store_true", help="run a one-act season (the fold's writes and emissions happen) instead of the seam's call alone")
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        record = play(a.role, FIXTURES[a.fixture], seed=a.seed, apply=a.apply)
    except ValueError as refused:
        raise SystemExit(str(refused))
    print(json.dumps(_plain(record), indent=1, sort_keys=True, default=repr))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
