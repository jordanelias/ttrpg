"""`harness.storybar` -- THE M2 INSTRUMENT: cross-person antecedent share and chain depth per season.

Plan position IN-19 (`STORY-BAR`). Over N seeded realms it prints, per season, how many acts had
ANOTHER PERSON'S act among their antecedents (the cross-person share) and the distribution of
cross-person chain depth, for each forcing arm, and whether the arms read equal. It grades nothing,
pins nothing and is wired into no gate: like `harness/aperture.py` it reports raw readings, never a
verdict (`harness/soak.py` now grades; this module does not). The prose that asked for it is reference (`CLAUDE.md` §0.05); what this
module computes is what the reading IS.

Entry point: `python -m engine.season.harness.storybar --base-seed S --n N --seasons K
--arms ARM ARM [--cap C]`. Every numeric argument is required and none has a default (the same reason
`harness/soak.py` gives: this file is inside `tools/ci_sim_fabrication_check.py`'s blocking scope).
`--cap` is `build_realm`'s own parameter and defaults to its own `None`, the full realm.

THE READING (`read`, a pure function over the log and `SeasonDriver.act_of`, so a test can plant on
it). For each Event in the log its act is `act_of[e.id]`; an act's antecedents are, over every cause
`c` of every Event of that act:
  * `act_of[c]`, when `c` is an Event some OTHER act emitted -- an ANTECEDENT ACT, cross-person when
    its actor differs from this act's actor and own when it does not;
  * a WORLD EVENT, when `c` is an Event in the log that no act emitted (MATTER, CALENDAR);
  * nothing, when `c` is this act's own id (`loop/resolve.py` stamps `[a.id] + occasion ids` on a
    successful act's Events (`resolve.py:487`) and `[a.id]` alone on every refusal (position IN-50),
    so the cross-person share is a FLOOR of what the log can express until that repair lands:
    `resolve.py`'s refusal returns at `:73`, `:372`, `:448`, `:554`, `:577`, `:747`, `:777` and
    `:912` omit the occasion -- and an act is not its own antecedent) or `ROOT`.
  A cause that is none of these (an id the log admits but that is neither a logged Event nor this
  act's own id) is counted in `unread` rather than dropped silently.
Each act takes ONE class, by precedence `cross` > `own` > `world` > `none` [ASSUMPTION: the source
recipe classifies "by whether the antecedent's actor differs" and names the four classes but not the
order when an act has several kinds of antecedent; the cross-person share does not depend on it].
CHAIN DEPTH is along cross-person edges only: an act with no cross-person antecedent has depth 1, and
otherwise 1 + the largest depth among its cross-person antecedent acts. An act belongs to the season in
which its first Event entered the log; a season's row reads the acts first logged in it, and the
cumulative row every act logged up to and including it.

FORCING ARMS. `ARMS` holds every forcing setting this tree can run, and today that is ONE: `off`, the
shipped season loop with no outside forcing input. No forcing source is built yet (the `FORCE-*`
positions IN-21/34, IN-35, IN-36 build them), so there is no `on` arm and this module invents none.
The comparison already takes two arms so its control exists before its subject: `--arms off off` is
the forcing-off control, and the two arms must read equal. A forcing position adds its arm name here
and applies it to the freshly built World before the chooser is made, the idiom `harness/arms.py` and
`harness/soak.py` use for a fixture sweep.

THE COMPOSITION is `populated.run`'s (`build_realm`, `SeasonDriver`, `make_chooser` over
`resolvable_verbs()`, `draw_factory`, `probes.SUBSIST`, the caller-passed `contest_max_depth`),
repeated here rather than called because `populated.run` exposes no per-season boundary in the log
-- the same reason `harness/soak.py` gives for keeping its own driver.

ARCS ARE OUT OF SCOPE BY DECISION (`ED-IN-0225`): this reads the cause graph the loop already writes
and mints no carrier, field, Event kind or register row for an arc, story or thread.
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter

from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.ids import H, ROOT, draw_factory
from . import probes as P
from .populated import build_realm

#: Every forcing setting this tree can run. `off` is the shipped loop; no `on` is built (see the
#: module docstring). A forcing position adds its own arm here.
ARMS = ("off",)

#: The four antecedent classes, in precedence order (highest first).
CLASSES = ("cross", "own", "world", "none")


# ---------------------------------------------------------------------------------------------
# THE READING. Pure: the log, `act_of`, and where each season's Events begin in the log.
# ---------------------------------------------------------------------------------------------

def read(log, act_of: dict, bounds: list) -> dict:
    """Classify every act in `act_of` and compute its cross-person chain depth.

    `bounds[s]` is the log index at which season `s`'s Events begin. Returns `{"acts": {act_id:
    {"actor", "season", "cls", "cross", "depth"}}, "unread": int}` with acts in first-logged order."""
    events = list(log)
    event_ids = {e.id for e in events}
    # an act's Events, in log order, and the season of its first Event
    acts: dict = {}
    season = 0
    for i, e in enumerate(events):
        while season + 1 < len(bounds) and i >= bounds[season + 1]:
            season += 1
        a = act_of.get(e.id)
        if a is None:
            continue
        row = acts.get(a.id)
        if row is None:
            row = acts[a.id] = {"actor": a.actor, "season": season, "events": []}
        row["events"].append(e)

    unread = 0
    for aid, row in acts.items():
        cross, own, world = set(), set(), False
        for e in row["events"]:
            for c in e.causes:
                if c == aid or c == ROOT:
                    continue
                ant = act_of.get(c)
                if ant is not None:
                    if ant.id == aid:
                        continue                       # another Event of this same act
                    (cross if ant.actor != row["actor"] else own).add(ant.id)
                elif c in event_ids:
                    world = True
                else:
                    unread += 1
        row["cross"] = sorted(cross)
        row["cls"] = ("cross" if cross else "own" if own else "world" if world else "none")
        del row["events"]

    # depth along cross-person edges; explicit stack, a back-edge (never expected) contributes 0
    depth: dict = {}
    for root in acts:
        if root in depth:
            continue
        stack, on = [root], {root}
        while stack:
            top = stack[-1]
            pending = [b for b in acts[top]["cross"]
                       if b in acts and b not in depth and b not in on]
            if pending:
                stack.append(pending[0])
                on.add(pending[0])
                continue
            depth[top] = 1 + max((depth.get(b, 0) for b in acts[top]["cross"] if b in acts),
                                 default=0)
            stack.pop()
            on.discard(top)
    for aid, row in acts.items():
        row["depth"] = depth[aid]
    return {"acts": acts, "unread": unread}


def summarise(acts) -> dict:
    """One reading over an iterable of act rows from `read`."""
    rows = list(acts)
    cls = Counter(r["cls"] for r in rows)
    dep = Counter(r["depth"] for r in rows)
    n = len(rows)
    return {"acts": n, "classes": {k: cls.get(k, 0) for k in CLASSES},
            "cross_share": (cls.get("cross", 0) / n) if n else 0.0,
            "depth": dict(sorted(dep.items())), "max_depth": max(dep, default=0)}


def per_season(reading: dict, seasons: int) -> list:
    """`[(season_reading, cumulative_reading)]` for seasons `0..seasons-1`."""
    rows = list(reading["acts"].values())
    return [(summarise(r for r in rows if r["season"] == s),
             summarise(r for r in rows if r["season"] <= s)) for s in range(seasons)]


# ---------------------------------------------------------------------------------------------
# ONE SEEDED REALM, ONE ARM.
# ---------------------------------------------------------------------------------------------

def drive(seed: int, seasons: int, arm: str, cap=None) -> tuple:
    """Build the realm, run `seasons` seasons under `arm`; return `(world, driver, bounds)`."""
    if arm not in ARMS:
        raise ValueError(f"forcing arm {arm!r} is not built; this tree runs {ARMS}")
    w = build_realm(seed, cap)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    bounds = []
    for _ in range(seasons):
        bounds.append(len(w.log))
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, bounds


def run_seed(seed: int, seasons: int, arm: str, cap=None) -> dict:
    """`drive`, then `read`; the result carries `bounds` and the resolved-act count too."""
    w, d, bounds = drive(seed, seasons, arm, cap)
    out = read(w.log, d.act_of, bounds)
    out["bounds"] = bounds
    out["resolved"] = len(d.resolved)
    return out


def compare(arms, seeds, seasons: int, cap=None) -> dict:
    """`{arm_index: {"arm", "seeds": {seed: per_season}, "pooled": per_season}}` for each arm."""
    out = {}
    for i, arm in enumerate(arms):
        by_seed, pooled_rows = {}, []
        for seed in seeds:
            r = run_seed(seed, seasons, arm, cap)
            by_seed[seed] = {"per_season": per_season(r, seasons), "unread": r["unread"],
                             "resolved": r["resolved"]}
            pooled_rows.extend(r["acts"].values())
        out[i] = {"arm": arm, "seeds": by_seed,
                  "pooled": per_season({"acts": dict(enumerate(pooled_rows))}, seasons)}
    return out


# ---------------------------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------------------------

def _fmt(r: dict) -> str:
    c = r["classes"]
    return (f"acts={r['acts']} cross={c['cross']} own={c['own']} world={c['world']} "
            f"none={c['none']} cross_share={100 * r['cross_share']:.1f}% "
            f"depth={r['depth']} max_depth={r['max_depth']}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base-seed", type=int, required=True)
    ap.add_argument("--n", type=int, required=True, help="seeded realms per arm")
    ap.add_argument("--seasons", type=int, required=True)
    ap.add_argument("--arms", nargs=2, choices=ARMS, required=True,
                    help=f"two forcing arms to compare; built: {', '.join(ARMS)}")
    ap.add_argument("--cap", type=int, default=None,
                    help="build_realm's cast cap; omitted = build_realm's own None, the full realm")
    args = ap.parse_args(argv)

    seeds = list(range(args.base_seed, args.base_seed + args.n))
    res = compare(args.arms, seeds, args.seasons, args.cap)
    print(f"storybar seeds={seeds[0]}..{seeds[-1]} seasons={args.seasons} arms={list(args.arms)} "
          f"cap={args.cap} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
    for i in sorted(res):
        arm = res[i]["arm"]
        for seed, sr in res[i]["seeds"].items():
            print(f"[arm {i}:{arm}] seed={seed} resolved={sr['resolved']} unread={sr['unread']}")
            for s, (this, cum) in enumerate(sr["per_season"]):
                print(f"  season {s}: {_fmt(this)}")
                print(f"  through {s}: {_fmt(cum)}")
        for s, (this, cum) in enumerate(res[i]["pooled"] if len(seeds) > 1 else ()):
            print(f"[arm {i}:{arm}] pooled season {s}: {_fmt(this)}")
            print(f"[arm {i}:{arm}] pooled through {s}: {_fmt(cum)}")
    equal = res[0]["pooled"] == res[1]["pooled"]
    print(f"arms {args.arms[0]} vs {args.arms[1]}: "
          f"{'EQUAL' if equal else 'DIFFER'} on every pooled season reading")
    return 0


if __name__ == "__main__":
    sys.exit(main())
