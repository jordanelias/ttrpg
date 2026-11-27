"""`harness.scene` -- ONE MODULE'S SCENE INSTANCE, RUN ALONE FROM A SMALL WORLD (B34.15; `01_CORE_one_scene_contract` edit 4).

    python -m engine.season.harness.scene combat.fight --fixture fight_headless --seed 0
    python -m engine.season.harness.scene social_contest.roll --fixture roll --seed 0 [--effort N] [--verb V] [--apply]    # B34.17, `IS-DICE-01`

`play` stages ONE SCENE INSTANCE, ALONE (the glossary's row *scene instance*; ED-IN-0303): one act's scene, from a small world, by the SAME entry the season's fold
calls, with no season around it. `play(role, fixture, ...)` is an instrument: it adds no rule, reads no file a
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

A ROLE WITH A PRINTER (`PRINTERS`: `social_contest.roll`) adds `roll` to the record: the pool and its parts, each obstacle term and their sum, the levels, the exact and the
believed odds, the draw's key and the dealt band; with `apply=True` the record also carries `wrote`, what the band's act left in the world.

`decide` (the host's decider for `role`) is handed in as `PlayHost(persons={actor}, deciders={role: decide})`; with none, no host: AUTOMATED, as every season is.

A FIXTURE is a dict: `role` (a `composition.json` role), `build` (`seed -> World`), `act` (`id`, `actor`, `verb`, `payload`) and, optionally, `max_depth` (absent:
the world's own `contest_max_depth`, which a season passes, S39.3). `FIXTURES` holds the ones whose builders exist. Its caller: the gate command above and the
module lanes' standalone instructions (B20's field, B30's nesting); `tests/test_scene_contract.py` imports it, and so does its own command line.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable, Optional

from engine.dice_engine.fmath import ltr_sum
from engine.dice_engine.sigma_leverage import record_odds

from ..data.verbs import VERB_TABLE
from ..loop.driver import SeasonDriver
from ..loop.sides import _contests_of, seat_named_by, sides_of
from ..queries.inputs import PlayHost
from ..seam import ContestError, ContestRefused, contest, degree_of
from ..seam.wrappers.pool import addends_of, governing_score, pool_pair, rank
from ..seam.wrappers.sigma import arranged_by, odds_of, topic_of
from ..state.carriers import EFFORT, Act, Event, Office, Record, Tenure, effort_of
from ..state.ids import draw_factory
from . import storybar
from .carin import BAILIFF, CARIN, WARDEN, build_world as carin_world
from .pairs import BANDS
from .probes import about

#: THE FIXTURES, by name. `fight_headless` is the headless world (`carin.build_world`, Carin's three people) with an authored `fight` between its first two
#: persons: the `[ASSUMPTION]` of `01_CORE_one_scene_contract` edit 4. `duel` (`duel_scene.build`, `IS-PC-01` step 6) is NOT here: its builder was retired unbuilt
#: (`hole_register.yaml` H-580) and the name waits on the redesign.
#:
#: `roll` (B34.17, `IS-DICE-01`) stages the social roll on `fight_headless`'s world (`carin.build_world`, called, not copied). SUBSTITUTION, said once: the entry builds it on
#: `duel_scene.build(seed)`, which does not exist (H-580); its own basis is *the duel's world is reused: two persons who differ and a witness*, and Carin's world is that
#: kind of world (three persons drawn per seed; Carin and the bailiff share a hearth). THE VERB IS `arrest`, chosen at landing from the rows of `verb_table.yaml` the social roll
#: deals (a contested prize whose provider is `social_contest` and no `proceeds:`: arrest, confer, establish, issue, revoke, succeed): of these, `arrest` is the one whose row
#: names a skill (`capability: arms`), which the entry's step 1 adds a score in, and its band cells differ (three bands open a `detain` edge and `Failure` writes nothing;
#: `arrest.made` / `arrest.resisted`). It is eligible only through a seat and effective only on a warrant, so the world is given the two seats and the one warrant it names.
ROLL_VERB, ROLL_SEAT = "arrest", "off_watch"
ROLL_SKILL_SCORES = {CARIN: 2, BAILIFF: 3}       # AUTHORED: each fighter's `arms` rank (the skill `ROLL_VERB`'s row names), added to the drawn attributes


def _roll_world(seed: int) -> Any:
    """`carin.build_world(seed)` plus what an `arrest` needs: an `arms` rank on each of the two persons; Carin seated at the watch (`off_watch`, which grants `dispatch`); the
    warden seated at the bench (`off_bench`, which sits over Ostvik) and the warrant it issued naming the bailiff, held by Carin (its creating act and Event planted, as
    `issuing_seat` reads them: the issuing seat is the bench, whose holder could close the custody)."""
    w = carin_world(seed)
    row = VERB_TABLE[ROLL_VERB]
    for pid, rank_held in ROLL_SKILL_SCORES.items():
        w.persons[pid].capability = {row.capability: rank_held}
    w.offices[ROLL_SEAT] = Office(ROLL_SEAT, "Watch", "ostvik", ["dispatch"], faction="Crown")
    w.offices["off_bench"] = Office("off_bench", "Bench", "ostvik", ["issue", "determine"], scope_rung="ostvik", faction="Crown")
    w.add_tenure(Tenure("t_carin_watch", CARIN, ROLL_SEAT, "hold", since=0))
    w.add_tenure(Tenure("t_warden_bench", WARDEN, "off_bench", "hold", since=0))
    w.records["rec_warrant"] = Record("rec_warrant", "ostvik", "dispensation", subject_matter=dict(terms=BAILIFF, to=CARIN, at=None, force=None))
    w.add_tenure(Tenure("t_warrant", CARIN, "rec_warrant", "hold", since=0))
    w.acts.append(Act(id="a_warrant", actor=WARDEN, verb="issue", via="off_bench", payload={"subject": BAILIFF, "to": CARIN}))
    w.log.append(Event("e_warrant", "dispensation.issued", [about(w, "rec_warrant")], ["a_warrant"], 0))
    return w


FIXTURES: dict[str, dict] = {
    "fight_headless": dict(role="combat.fight", build=carin_world,
                           act=dict(id="scene_0", actor=CARIN, verb="fight", payload={"subject": BAILIFF})),
    "roll": dict(role="social_contest.roll", build=_roll_world,
                 act=dict(id="scene_0", actor=CARIN, verb=ROLL_VERB, via=ROLL_SEAT, payload={"subject": BAILIFF})),
}

#: THE FOUR BANDS' NAMES, in the one ladder's order (`pairs.BANDS`, its one owner): the keys of a printed odds table.
BAND_ORDER = BANDS

#: What an `apply=False` record says it did not ask (A-63; `28_CORE_scene_access_A` §2, §3): both are the fold's, so a standalone call without the fold omits them.
NOT_ASKED = ("the counterparty's received-scene debit", "the `engaged` clause (A-63)")


def _act(spec: dict) -> Act:
    return Act(id=spec["id"], actor=spec["actor"], verb=spec["verb"], via=spec.get("via"), payload=dict(spec.get("payload") or {}))


def staged(fixture: dict, *, verb: Optional[str] = None, effort: Optional[int] = None) -> dict:
    """`fixture` with its act's verb and its act's effort replaced where given (`main`'s `--verb` and `--effort`): the one place either is set on a fixture. A verb the table
    lacks is refused here, naming it."""
    if verb is not None and verb not in VERB_TABLE:
        raise ValueError(f"verb {verb!r} is no row of verb_table.yaml")
    act = dict(fixture["act"])
    if verb is not None:
        act["verb"] = verb
    if effort is not None:
        act["payload"] = {**(act.get("payload") or {}), EFFORT: effort}
    return {**fixture, "act": act}


def _checked(role: str, fixture: dict) -> None:
    if fixture.get("role") != role:
        raise ValueError(f"fixture stages role {fixture.get('role')!r}, not {role!r}: a decider for {role!r} would never be asked")


def play(role: str, fixture: dict, *, seed: int = 0, decide: Optional[Callable] = None, apply: bool = False) -> dict:
    """One scene instance, staged alone. Returns a record: `role`, `seed`, `act`, `played` (a decider was handed in; True is where the role's entry accepts one, not `social_contest.roll`'s plain-roll path, which never
    calls it), `max_depth`, `status` (`RESOLVED`, a typed refusal's status, `DEPTH-CAPPED`, or at `apply=True` `FOLDED` / `UNGRADED`), `degree` (the one ladder's, `None` for a refusal), `result` (the provider's own return, `apply=False`) or `events` and `world`
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
        # THE ROLL THE FOLD DEALS IS THE STANDALONE CALL'S (one key, one world, one tick: `test_apply_false_goes_through_seam_contest`), so a printer's record is read off
        # a twin world's `apply=False` call, and the season runs on `w`.
        alone = play(role, fixture, seed=seed, decide=decide) if role in PRINTERS else {}
        printed = {"roll": alone["roll"]} if "roll" in alone else {}
        _season(driver, act, max_depth, host)
        caused = [(e.kind, e.degree) for e in w.log if act.id in e.causes]
        graded = [d for _, d in caused if d is not None]
        return dict(record, **printed, status="FOLDED" if graded else "UNGRADED", degree=graded[-1] if graded else None, events=caused, wrote=_wrote(w, act),
                    world=w, content_hash=w.content_hash())
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
    purpose = f"roll:{prize}:{act.id}"
    rng = draw_factory(w.world_seed, lambda: w.tick)(act.actor, purpose)
    drawn_from = dict(actor=act.actor, purpose=purpose, seed=w.world_seed, tick=w.tick, key=rng.key)       # read before the draw: a `Draw` counts what it deals
    got = contest(w, rung=rung, prize=prize, claimants=parties, depth=0, max_depth=max_depth, causes=[act.id], verb=act.verb, subject=subject, rng=rng,
                  effort=effort_of(act), host=host, via=act.via, act=act, topic=topic, arranger=arranger, rig=rig, seat=seat_named_by(w, act, prize))
    record.update(not_asked=NOT_ASKED, prize=prize, content_hash=w.content_hash())
    if isinstance(got, ContestError):
        return dict(record, status="DEPTH-CAPPED", degree=None, refusal=got.reason, result=None)
    if isinstance(got, ContestRefused):
        return dict(record, status=got.status, degree=None, refusal=got.why, result=None)
    degree = degree_of(got, target, w.fixtures)          # the season's own `_target` (`loop/resolve.py`): the act's opponent operand
    printed = {"roll": PRINTERS[role](w, act, drawn_from, got, degree)} if role in PRINTERS and "terms" in got else {}      # a party gap has no terms to print
    return dict(record, **printed, status=got["status"], degree=degree, result=got)


def _season(driver: Any, act: Act, max_depth: Optional[int], host: Optional[PlayHost]) -> None:
    """A ONE-ACT SEASON: `act` is what its actor's `choose` returns, ONCE (a season has several laps and the driver stamps a fresh id on an act each lap it is returned: handed
    out every lap, the act would be played again and the record would read the last play's), and every other person's `choose` returns nothing. The one loop, `SeasonDriver.season`."""
    handed: list = []
    def choose(p: Any, v: Any, s: Any, ask_budget: Callable[[], int]) -> list:
        if p.id != act.actor or handed:
            return []
        handed.append(act.id)
        return [act]
    driver.season(choose, None, contest_max_depth=max_depth, host=host)


def _wrote(w: Any, act: Act) -> dict:
    """WHAT THE ACT'S BAND WROTE, after a season: `changes` -- the `(subject, field)` of every change on the Events that name the act in `causes[]`; `deposited` -- the
    `claim.deposited` Events those Events caused (what witnesses were given); `durable` -- whether the act is NOT a null scene by `storybar.null_scenes`' own rule (a durable
    write other than the scene budget, which is the driver's and writes no cell, A-62)."""
    mine = [e for e in w.log if act.id in e.causes]
    ids = {e.id for e in mine}
    null = storybar.null_scenes(w, 1, scope=lambda attempt: attempt[0].id == act.id)
    return dict(changes=[(c.subject, c.field) for e in mine for c in e.changes],
                deposited=sum(1 for e in w.log if e.kind == "claim.deposited" and ids & set(e.causes)),
                durable=null["total"] == 1 and not null["null"])


def _roll_record(w: Any, act: Act, drawn_from: dict, got: dict, degree: Optional[str]) -> dict:
    """THE SOCIAL ROLL'S PRINTED RECORD (`IS-DICE-01`), read off the call's own return and the owners of each quantity, and adding no rule:
      * `pool` -- the pool and its parts (`pool.py`: the skill score `rank`, the attribute base `governing_score`, the registered addends, the `social_roll` row's base and
        floor), the actor's governing attributes and the opposing one;
      * `obstacle` -- every term by name (`Margin.terms`), their sum (accumulated left to right, as `roll.py::obstacle` does) and the obstacle `ob`;
      * `levels` -- the named levels in force: each `advantage_sources` member's count for and against the roller (attributes enter as the pool's base, wounds and a seat's
        modifier as levels) and the leverage they make;
      * `exact` -- the four bands' odds, `sigma_leverage.record_odds` (`band_odds` at the roll's own boost) over the call's pool, obstacle and leverage, `None` for a refusal;
      * `believed` -- the actor's own believed odds, `odds_of(w, act, believer=<actor>)`: `None` where a factor is unknown to him;
      * `draw` -- the key the roll drew on; `dealt` -- the band the one ladder gave it."""
    actor, row = w.persons[act.actor], VERB_TABLE[act.verb]
    base, floor = pool_pair(w.fixtures)
    parts = dict(skill=rank(actor, act.verb), governing=governing_score(w, actor, act.verb), addends=addends_of(w, actor, act.verb), base=base, floor=floor)
    attributes = {name: actor.attributes.get(name) for name in row.governing}
    target = w.persons.get(act.payload.get(row.opponent_operand()))
    if row.opposed_attribute is not None and target is not None:
        attributes[f"opposing {row.opposed_attribute}"] = target.attributes.get(row.opposed_attribute)
    terms = [(name, value) for name, value in got["terms"]]
    exact = record_odds(got["pool"], got["ob"], got["leverage"]) if got["status"] == "RESOLVED" else None
    believed = odds_of(w, act, believer=actor)
    return dict(pool=dict(pool=got["pool"], parts=parts, attributes=attributes),
                obstacle=dict(terms=terms, sum=ltr_sum(value for _, value in terms), ob=got["ob"]),
                levels=dict(by_source=[tuple(level) for level in got["levels"]], leverage=got.get("leverage")),
                exact=None if exact is None else dict(zip(BAND_ORDER, exact)),
                believed=None if believed is None else dict(zip(BAND_ORDER, believed)),
                draw=drawn_from, dealt=degree)


#: A MODULE ROLE'S PRINTER: `(w, act, drawn_from, got, degree) -> the record's `roll``. The roles whose scene prints more than the seam's return.
PRINTERS: dict[str, Callable] = {"social_contest.roll": _roll_record}


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
    ap.add_argument("--verb", default=None, help="stage this verb (a row of verb_table.yaml) in place of the fixture's act's own")
    ap.add_argument("--effort", type=int, default=None, help="the act's effort (extra scene slots, CP-T01-05): each brings one `effort_level` for the roller")
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        record = play(a.role, staged(FIXTURES[a.fixture], verb=a.verb, effort=a.effort), seed=a.seed, apply=a.apply)
    except ValueError as refused:
        raise SystemExit(str(refused))
    print(json.dumps(_plain(record), indent=1, sort_keys=True, default=repr))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
