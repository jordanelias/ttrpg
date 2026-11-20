"""`harness.storybar` -- THE M2 INSTRUMENT: cross-person antecedent share and chain depth per season.

Plan position IN-19 (`STORY-BAR`). Over N seeded realms it prints, per season, how many acts had
ANOTHER PERSON'S act among their antecedents (the cross-person share) and the distribution of
cross-person chain depth, for each forcing arm, and whether the arms read equal. It grades nothing,
pins nothing and is wired into no gate: like `harness/aperture.py` it reports raw readings, never a
verdict (`harness/soak.py` now grades; this module does not). The prose that asked for it is
reference (`CLAUDE.md` §0.05); what this module computes is what the reading IS.

Entry point: `python -m engine.season.harness.storybar --base-seed S --n N --seasons K
--arms ARM ARM [--cap C] [--executed-only]`. Every numeric argument is required and none has a default (the same reason
`harness/soak.py` gives: this file is inside `tools/ci_sim_fabrication_check.py`'s blocking scope).
`--cap` is `build_realm`'s own parameter and defaults to its own `None`, the full realm.

`--base-seed S --seasons K --draw-seeds D D ...` (REM-15) replaces `--n`/`--arms`: one realm built from `S`,
deep-copied per draw seed, only the chooser's draw varied (`draw_seed_arm`, which states the two residues).

`--base-seed S [S ...] --seasons K --remove [PERSON] [--at SEASON LAP]` (the removal test, `removal_arm`):
one realm per seed, one person's choice suppressed at one lap, the others' acts that differ counted. With no
PERSON it takes `most_cited`'s and prints the name. Each seed's report ends on two verdict lines,
`R-01.c  others' acts differing: <n>  (replay <0>)` and `R-02.b  differing at a later (season, round): <m>`
(`removal_verdict`, which also says what each reading is expected to be). This is the only mode that takes
several seeds.

`--base-seed S [S ...] --seasons K --null-scenes` (`null_scenes`, IS-A-07, A-81): one realm per seed under the
shipped arm, and per seed, per season and pooled the count of acts that left no durable write, as `null_scenes
total=<n> null=<n> | <verb/class=n, ...>`. Report-only: it asserts no zero. Takes no `--n` or `--arms`;
`harness/aperture.py` prints the same reading as its NULL SCENES block. `null_scenes` owns the definitions of
a durable write and of a null scene.

THE READING (`read`, a pure function over the log and `SeasonDriver.act_of`, so a test can plant on
it). For each Event in the log its act is `act_of[e.id]`; an act's antecedents are, over every cause
`c` of every Event of that act:
  * `act_of[c]`, when `c` is an Event some OTHER act emitted -- an ANTECEDENT ACT, cross-person when
    its actor differs from this act's actor and own when it does not;
  * a WORLD EVENT, when `c` is an Event in the log that no act emitted (MATTER, CALENDAR);
  * nothing, when `c` is this act's own id (`loop/resolve.py::_act_events` stamps `[a.id] + occasion
    ids` on every Event an act emits, refusal or success (position IN-50) -- and an act is not its
    own antecedent) or `ROOT`.
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

THE COMPOSITION is `populated.run`'s (`build_realm`, `SeasonDriver`, `probes.chooser` over
`resolvable_verbs()`, the caller-passed `contest_max_depth`),
repeated here rather than called because `populated.run` exposes no per-season boundary in the log
-- the same reason `harness/soak.py` gives for keeping its own driver.

THE EXECUTED READING (CR-15, `--executed-only`; `read`'s `refused` argument). Beside the reading above,
never instead of it: the same cause graph with every REFUSED act and every edge into one cut, the
depth recomputed along what is left. An act is refused when `corpus_run.attempts` (the one owner of the
made/refused rule, over the act store) gives it a non-empty `refused` tuple, so a graded loss counts
as refused and is reported apart (`corpus_run.graded_losses`); `attribute`'s `made` is not the test (it
counts a graded loss as made). `executed_summary` is its own small summary, not `summarise`'s four
classes. Without the flag the CLI prints exactly what it printed before. It mints no carrier.

AN ARC HAS NO CARRIER (`ED-IN-0225`, 2026-09-13: no type, no rung, no tenure kind; the carrier is not
to be built): this reads the cause graph the loop already writes and mints no carrier, field, Event
kind or register row for an arc, story or thread.

THE ESTIMATES (`estimates`, v9 IN-23 CARRY-STABILITY), read after each season beside the reading above
and changing none of it: every person's own `queries/person_q.py::legitimacy` of every live seat-holder
(himself included -- a ruler can be wrong about his own standing, R7) and `stability` of every rung an
office sits on, vacant offices' included, at the realm's own `estimate_window_seasons` and `scar_weight_shift`. Each row is the
pairs read, their mean (the cross-person mean estimate), min, max and distinct values. Who holds which
seat is read off the World here, OUTSIDE the simulation: the observer may, and the person may not.
"""

from __future__ import annotations

import argparse
import copy
import os
import sys
from collections import Counter, defaultdict

from ..data.matrix import MATRIX, Step
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..data.verbs import opportunity_key
from ..queries.person_q import legitimacy, stability
from ..state.carriers import Receipt, subject_of
from ..state.gate import TENURE_CLOSED
from ..state.ids import ROOT
from .arc import _Records
from .corpus_run import attempts, graded_losses, refusal_sets, seats
from . import probes as P
from ..boot.realm import COHORT_PREFIX, build_realm

#: Every forcing setting this tree can run. `off` is the shipped loop; no `on` is built (see the
#: module docstring). A forcing position adds its own arm here.
ARMS = ("off",)

#: What `--remove` with no person names: the sentinel `main` swaps for `most_cited`'s person. Not a
#: person id of any realm (a person is `p_...`).
MOST_CITED = "<most-cited>"

#: The four antecedent classes, in precedence order (highest first).
CLASSES = ("cross", "own", "world", "none")


# ---------------------------------------------------------------------------------------------
# THE READING. Pure: the log, `act_of`, and where each season's Events begin in the log.
# ---------------------------------------------------------------------------------------------

def read(log, act_of: dict, bounds: list, refused=None) -> dict:
    """Classify every act in `act_of` and compute its cross-person chain depth.

    `bounds[s]` is the log index at which season `s`'s Events begin. Returns `{"acts": {act_id:
    {"actor", "season", "cls", "cross", "depth"}}, "unread": int}` with acts in first-logged order.

    `refused` (CR-15), a set of act ids, is `None` by default and then the return is EXACTLY the one
    above, no further key. When it is given the return gains `"executed"`: the same acts without the
    refused ones, each `{"actor", "season", "cross", "depth"}` with `cross` cut to antecedents that
    are also not refused and `depth` recomputed along those edges (`_executed_rows`). The default
    keys are computed first and untouched by it. `refused=frozenset()` is the executed path with
    nothing refused (it reads the default's `cross` and `depth`); `None` is the path without it."""
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

    depth = _depths(acts)
    for aid, row in acts.items():
        row["depth"] = depth[aid]
    out = {"acts": acts, "unread": unread}
    if refused is not None:
        out["executed"] = _executed_rows(acts, refused)
    return out


def _depths(acts: dict) -> dict:
    """`{act_id: depth}` along the `cross` edges of `acts` (rows with a `cross` list); explicit stack, a
    back-edge (never expected) contributes 0. An antecedent not in `acts` contributes 0 too."""
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
    return depth


def _executed_rows(acts: dict, refused) -> dict:
    """`read`'s `"executed"` value: the acts of `acts` NOT in `refused`, in the same order, each
    `{"actor", "season", "cross", "depth"}` with `cross` cut to antecedents also not in `refused` and
    `depth` recomputed along those edges by the same `_depths`. A refused act is not bridged over: an
    executed act whose only antecedent was refused stands at depth 1, whatever lay behind the refused
    act. No `cls`: with the cut `cross`, "own"/"world" would be guesses this reading cannot make."""
    rows = {aid: {"actor": r["actor"], "season": r["season"],
                  "cross": [b for b in r["cross"] if b not in refused]}
            for aid, r in acts.items() if aid not in refused}
    depth = _depths(rows)
    for aid, row in rows.items():
        row["depth"] = depth[aid]
    return rows


def summarise(acts) -> dict:
    """One reading over an iterable of act rows from `read`."""
    rows = list(acts)
    cls = Counter(r["cls"] for r in rows)
    dep = Counter(r["depth"] for r in rows)
    n = len(rows)
    return {"acts": n, "classes": {k: cls.get(k, 0) for k in CLASSES},
            "cross_share": (cls.get("cross", 0) / n) if n else 0.0,
            "depth": dict(sorted(dep.items())), "max_depth": max(dep, default=0)}


def per_season(acts, seasons: int) -> list:
    """`[(season_reading, cumulative_reading)]` for seasons `0..seasons-1`, over an iterable of act
    rows from `read`."""
    rows = list(acts)
    return [(summarise(r for r in rows if r["season"] == s),
             summarise(r for r in rows if r["season"] <= s)) for s in range(seasons)]


# ---------------------------------------------------------------------------------------------
# THE EXECUTED READING (CR-15). Beside the one above, never instead of it.
# ---------------------------------------------------------------------------------------------

def executed_items(acts: dict, executed: dict, refused, graded) -> list:
    """`[(default_row, executed_row_or_None, is_refused, is_graded_loss)]` per act of `read`'s `"acts"`,
    `executed` its `"executed"`. A plain list, so a season's slice or several seeds' rows pool by
    concatenation (act ids need not be unique across seeds)."""
    return [(r, executed.get(aid), aid in refused, aid in graded) for aid, r in acts.items()]


def executed_summary(items) -> dict:
    """The executed reading's own small summary over `executed_items`' tuples (NOT the four-class
    `summarise`): `acts` read; `executed` of them and, of those, `with_cross` having an executed cross
    antecedent and their `share`; `depth` the distribution along executed edges and `max_depth`;
    `refused`, `refused_deep` those at DEFAULT depth 2 or more, `graded` the graded losses among the
    refused; and, from the default reading, `deep` acts at cross-person depth 2 or more, `cross` acts
    classed cross and their `cross_share` (as `summarise` reads it)."""
    rows = list(items)
    ex = [e for _r, e, _ref, _g in rows if e is not None]
    dep = Counter(e["depth"] for e in ex)
    with_cross = sum(1 for e in ex if e["cross"])
    cross = sum(1 for r, _e, _ref, _g in rows if r["cls"] == "cross")
    return {"acts": len(rows), "executed": len(ex), "with_cross": with_cross,
            "share": (with_cross / len(ex)) if ex else 0.0,
            "depth": dict(sorted(dep.items())), "max_depth": max(dep, default=0),
            "refused": sum(1 for _r, _e, ref, _g in rows if ref),
            "refused_deep": sum(1 for r, _e, ref, _g in rows if ref and r["depth"] >= 2),
            "graded": sum(1 for _r, _e, ref, g in rows if ref and g),
            "deep": sum(1 for r, *_ in rows if r["depth"] >= 2), "cross": cross,
            "cross_share": (cross / len(rows)) if rows else 0.0}


def executed_per_season(items, seasons: int) -> list:
    """`[(season_reading, cumulative_reading)]` for seasons `0..seasons-1`, the executed counterpart
    of `per_season`, over `executed_items`' tuples."""
    rows = list(items)
    return [(executed_summary(i for i in rows if i[0]["season"] == s),
             executed_summary(i for i in rows if i[0]["season"] <= s)) for s in range(seasons)]


# ---------------------------------------------------------------------------------------------
# THE NULL SCENES READING (IS-A-07, A-81). Report-only; beside the reading above, never instead of it.
# ---------------------------------------------------------------------------------------------

#: The `(kind, field)` cell a claim deposit writes (`write_matrix.yaml`), and the one write the count
#: restricts to a holder who matters to the act.
CLAIM_CELL = ("Person", "claim_ledger")

#: The outcome classes of `null_scenes`, in print order. An act none of whose row's kinds is in the log
#: (`attempts` gives it neither `made` nor `refused`) is classed `neither` and counted, not dropped.
NULL_CLASSES = ("made", "refused", "graded_loss", "neither")


def _seat_holders(w, subject: str) -> frozenset:
    """Who an act's `subject` stands for: the person himself, or the live holders of the office it names
    (`corpus_run.seats`' inverse); nobody for anything else."""
    if subject in w.persons:
        return frozenset({subject})
    if subject in w.offices:
        return frozenset(pid for pid, oids in seats(w).items() if subject in oids)
    return frozenset()


def null_scenes(w, n: int, scope=None, rows=None, graded=None) -> dict:
    """`{"total": int, "null": Counter((verb, cls))}` over `corpus_run.attempts(w, n)`, the one owner of
    made and refused: how many acts there are, and which of them left no durable write.

    A *durable write* is a Receipt on a `write_matrix.yaml` cell whose `steps` include `RES` or `WIT`,
    other than the scene budget's own cell; a claim deposited in the actor's or a counterparty's ledger
    counts; a sighting in a bystander's ledger alone does not (the act must matter to someone in it).
    `[ASSUMPTION; medium; Jordan to correct; revert: any claim counts]`. A-62: the budget is a Query and
    writes no cell, so nothing is excluded for it; if a later build makes the debit a write, that cell is
    excluded by name here. A *null scene* is an act none of whose Events carries a durable write.

    An act's Events are those that name it in `causes[]` and, for a claim deposit, those caused by one of
    them (`loop/witness.py` gives a deposit the witnessed Event as its cause, not the act). A Receipt is
    read as the cell it wrote by `arc._Records.of`, the one reader of that, and a seat Receipt on a
    `tenure.closed` Event is skipped as `arc.read_arcs` skips it. The deposit's holder is read off the
    ledgers as the world ends, so a claim evicted from its ledger has no holder and does not count.
    The counterparty is `subject_of(act)` when it is a person, or the live holder of the office it names.

    `cls` is `graded_loss` where `corpus_run.graded_losses` has the act, else `refused` where the act has
    a refusal kind in the log (so a `march` that both declared and was refused is `refused`), else `made`,
    else `neither`.

    `scope`, `None` by default, is a predicate over an attempt of `attempts` (`(act, made, refused)`) that
    narrows WHICH acts are counted and changes nothing in what counts as a write [ASSUMPTION: the scope is
    an argument of this function, not a filter each caller writes -- basis: one owner of the count,
    CLAUDE.md §8; it adds no rule]. `rows` and `graded`, `None` by default, are `attempts(w, n)` and the ids
    of `graded_losses(w, n)` where a caller already holds them (`null_by_season` asks once per season over the
    same world); with `None` each is read here. Reads only."""
    records = _Records(w)
    named: dict = defaultdict(list)    # act id -> the Events naming it in `causes[]`
    by_event: dict = defaultdict(set)  # Event id -> the ids of the acts naming it
    events = list(w.log)
    for e in events:
        for c in e.causes:
            if w.acts.get(c) is not None:
                named[c].append(e)
                by_event[e.id].add(c)
    for e in events:
        if any(isinstance(r, Receipt) and (records.of(r, e)[0] == CLAIM_CELL) for r in e.changes):
            for c in e.causes:
                for aid in by_event.get(c, ()):
                    if aid not in by_event.get(e.id, ()):
                        named[aid].append(e)
    rows = attempts(w, n) if rows is None else rows
    graded = frozenset(a.id for a in graded_losses(w, n)) if graded is None else graded
    total, null = 0, Counter()
    for attempt in rows:
        a, made, refused = attempt
        if scope is not None and not scope(attempt):
            continue
        total += 1
        mine = {a.actor} | _seat_holders(w, subject_of(a))
        durable = False
        for e in named.get(a.id, ()):
            for r in e.changes:
                if not isinstance(r, Receipt) or (e.kind == TENURE_CLOSED and r.subject in w.offices):
                    continue
                pair, owner = records.of(r, e)
                row = MATRIX.get(pair)
                if row is None or not (Step.RESOLVE in row.steps or Step.WITNESS in row.steps):
                    continue
                if pair == CLAIM_CELL and owner not in mine:
                    continue
                durable = True
                break
            if durable:
                break
        if not durable:
            null[(a.verb, "graded_loss" if a.id in graded else "refused" if refused
                  else "made" if made else "neither")] += 1
    return {"total": total, "null": null}


def pool_null(readings) -> dict:
    """`null_scenes`' return summed over `readings`, an iterable of such returns (one per seed)."""
    out = {"total": 0, "null": Counter()}
    for r in readings:
        out["total"] += r["total"]
        out["null"].update(r["null"])
    return out


def null_line(r: dict) -> str:
    """`null_scenes total=<n> null=<n> | <verb/cls=n, ...>`, the largest count first, one owner of the
    line `--null-scenes` prints and `aperture`'s NULL SCENES block ends on."""
    parts = ", ".join(f"{v}/{c}={k}" for (v, c), k in sorted(r["null"].items(),
                                                           key=lambda kv: (-kv[1], kv[0])))
    return f"null_scenes total={r['total']} null={sum(r['null'].values())} | {parts or 'none'}"


def null_by_season(seed: int, seasons: int, cap=None) -> tuple:
    """`([season reading, ...], whole-run reading)` of `null_scenes` over one seeded realm run `seasons`
    seasons under the shipped arm. A season's reading is `null_scenes` with the `scope` of the acts the
    act store took in that season (the store is append-only, so the lengths at each season's end cut it)."""
    ends: list = []
    w, _d, _bounds = drive(seed, seasons, "off", cap, on_season=lambda w_, _s, _n: ends.append(len(w_.acts)))
    store, per, lo = tuple(w.acts), [], 0
    rows = attempts(w, seasons)
    graded = frozenset(a.id for a in graded_losses(w, seasons))
    for hi in ends:
        ids = frozenset(a.id for a in store[lo:hi])
        per.append(null_scenes(w, seasons, scope=lambda attempt, ids=ids: attempt[0].id in ids,
                               rows=rows, graded=graded))
        lo = hi
    return per, null_scenes(w, seasons, rows=rows, graded=graded)


def _spread(values) -> dict:
    vals = list(values)
    n = len(vals)
    return {"pairs": n, "mean": (sum(vals) / n) if n else 0.0,
            "min": min(vals, default=0), "max": max(vals, default=0), "distinct": len(set(vals))}


def estimates(w) -> dict:
    """`{"legitimacy": spread, "stability": spread}` over every (person, live seat-holder) and every
    (person, office rung) pair of `w` as it stands -- an office rung being any rung an Office sits on,
    vacant offices' included (`w.offices`, whether or not anyone holds the seat) -- each value one
    person's own estimate. Reads only."""
    window = w.fixtures.get("estimate_window_seasons")
    shift = w.fixtures.get("scar_weight_shift")
    holders = sorted(seats(w))
    rungs = sorted({o.rung for o in w.offices.values() if o.rung is not None})
    people = [w.persons[pid] for pid in sorted(w.persons)]
    return {"legitimacy": _spread(legitimacy(p, h, window, shift) for p in people for h in holders),
            "stability": _spread(stability(p, r, window) for p in people for r in rungs)}


# ---------------------------------------------------------------------------------------------
# ONE SEEDED REALM, ONE ARM.
# ---------------------------------------------------------------------------------------------

def drive(seed: int, seasons: int, arm: str, cap=None, on_season=None, world=None,
          draw_seed=None, wrap_chooser=None) -> tuple:
    """Build the realm, run `seasons` seasons under `arm`; return `(world, driver, bounds)`.

    `on_season(world, season summary, events logged this season)`, when given, is called after each
    season -- `harness/loops.py::observe` reads its per-season quantities through it.

    `world` and `draw_seed` are the `--draw-seeds` arm's two seams (`draw_seed_arm`) and both default
    to nothing, which is the shipped reading unchanged: `world`, when given, is a built World this
    call runs instead of building one (`seed` and `cap` are then unused); `draw_seed`, when given,
    replaces `w.world_seed` as the seed of the CHOOSER'S `draw_factory` and of nothing else -- the
    act-id mint below and every draw inside the driver keep `w.world_seed`.

    `wrap_chooser` is the removal test's seam (`removal_arm`), `None` by default, which is the shipped
    reading unchanged: `wrap_chooser(chooser) -> chooser` is applied once to the chooser before the
    first season. A wrapper must know which lap it is in, a fact only the driver holds (`SeasonDriver.
    lap`, a driver local by D-21), so when a wrapper is given the chooser it receives carries the
    driver as `.driver`; with `None` the chooser is handed to the loop untouched."""
    if arm not in ARMS:
        raise ValueError(f"forcing arm {arm!r} is not built; this tree runs {ARMS}")
    w = build_realm(seed, cap) if world is None else world
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs(), draw_seed=draw_seed)
    if wrap_chooser is not None:
        ch.driver = d
        ch = wrap_chooser(ch)
    bounds = []
    for _ in range(seasons):
        bounds.append(len(w.log))
        summary = d.season(ch, question=None,
                           contest_max_depth=w.fixtures.get("contest_max_depth"))
        if on_season is not None:
            on_season(w, summary, len(w.log) - bounds[-1])
    return w, d, bounds


def run_seed(seed: int, seasons: int, arm: str, cap=None, executed: bool = False) -> dict:
    """`drive`, then `read`; the result carries the resolved-act count and each season's
    `estimates` too.

    `executed` (CR-15), off by default, adds `"executed"` (`read`'s executed rows over
    `refusal_sets`) and `"items"` (`executed_items`); the default result is the same without them.

    ⚠ `resolved` IS `len(d.resolved)`, THE FOLD SET, AND KEEPS IT (REM-10 / HR-8): it is the count of
    acts that reached the fold, printed beside the act-store reading CR-15 adds, not instead of it.
    `corpus_run.attempts` counts what was ATTEMPTED (a contested act refused at admission included)."""
    per = []
    w, d, bounds = drive(seed, seasons, arm, cap, on_season=lambda w, _s, _n: per.append(estimates(w)))
    if executed:
        refused, graded = refusal_sets(w, len(bounds))
        out = read(w.log, d.act_of, bounds, refused)
        out["items"] = executed_items(out["acts"], out["executed"], refused, graded)
    else:
        out = read(w.log, d.act_of, bounds)
    out["resolved"] = len(d.resolved)
    out["estimates"] = per
    return out


def compare(arms, seeds, seasons: int, cap=None, executed: bool = False) -> list:
    """`[{"arm", "seeds": {seed: per_season}, "pooled": per_season}]`, one per arm in `arms` order.

    `executed` (CR-15) adds, beside each of those, `"executed_per_season"` and `"executed_total"` on a
    seed's entry and `"executed_pooled"` on the arm's, the `executed_per_season` / `executed_summary`
    readings; every default key is read as before, and the pooled comparison the CLI prints as
    EQUAL/DIFFER stays the default one."""
    out = []
    for arm in arms:
        by_seed, pooled_rows, pooled_items = {}, [], []
        for seed in seeds:
            r = run_seed(seed, seasons, arm, cap, executed)
            by_seed[seed] = {"per_season": per_season(r["acts"].values(), seasons),
                             "unread": r["unread"],
                             "resolved": r["resolved"],
                             "estimates": r["estimates"]}
            if executed:
                by_seed[seed]["executed_per_season"] = executed_per_season(r["items"], seasons)
                by_seed[seed]["executed_total"] = executed_summary(r["items"])
                pooled_items.extend(r["items"])
            pooled_rows.extend(r["acts"].values())
        res = {"arm": arm, "seeds": by_seed, "pooled": per_season(pooled_rows, seasons)}
        if executed:
            res["executed_pooled"] = executed_per_season(pooled_items, seasons)
        out.append(res)
    return out


# ---------------------------------------------------------------------------------------------
# THE `--draw-seeds` ARM: vary only the chooser's draw, on one built world.
# ---------------------------------------------------------------------------------------------

def chains(acts: dict, verbs: dict) -> Counter:
    """The multiset of verb-sequence chains from each FIRST ACT, over `read`'s `acts` and a
    `{act_id: verb}` map. A first act is one with no cross-person antecedent (class other than
    `cross`, depth 1); its chain is the verb sequence of the LONGEST path from it along cross-person
    edges taken forward (an act, then an act that names it as a cross-person antecedent), ties broken
    by the larger verb tuple. Keyed on verbs only, never an act id, so two runs that take the same
    verbs by different ids read as the same chain. Pure."""
    forward: dict = {aid: [] for aid in acts}
    for aid, row in acts.items():
        for b in row["cross"]:
            if b in forward:
                forward[b].append(aid)
    best: dict = {}
    # a consequent's depth is strictly greater than its antecedent's, so descending depth finishes
    # every consequent before the act it follows
    for aid in sorted(acts, key=lambda a: -acts[a]["depth"]):
        tail = max((best[c] for c in forward[aid]), key=lambda t: (len(t), t), default=())
        best[aid] = (verbs[aid],) + tail
    return Counter(best[aid] for aid, row in acts.items() if row["cls"] != "cross")


def fork(base):
    """A deep copy of `base` that is a world of its own. ⚠ A bare `copy.deepcopy(World)` is not one:
    `World.__init__` hands the log a LAMBDA, `lambda: self.acts.ids()`, and `deepcopy` shares a function
    object rather than copying it, so the copy's log would judge a cause against the ORIGINAL's act store
    (MEASURED: the first act-caused Event of a copied world's first season is refused as a cause that
    "resolves to nothing"). The bound `_on_logged` rebinds by itself. The one thunk is re-pointed here,
    from outside `state/` (a harness may not edit it), through the log's own `_act_ids` slot."""
    w = copy.deepcopy(base)
    w.log._act_ids = lambda: w.acts.ids()
    return w


def draw_seed_arm(base, seasons: int, draw_seeds) -> dict:
    """`--draw-seeds`: ONE built world `base`, deep-copied once per draw seed, each copy run
    `seasons` seasons with ONLY the chooser's `draw_factory` seeded by the draw seed
    (`drive(draw_seed=...)`). The question is how much of the cross-person chain structure the
    chooser's draw alone moves: the world, the act-id mint and `w.world_seed` are the same in every
    copy, and `base` itself is never run.

    Returns `{"base_hash_before", "base_hash_after", "fixtures": {"choice_temperature",
    "intent_disclosure"}, "runs": {draw_seed: {"start_hash", "acts", "depth", "chains"}}}`: `start_hash` is the copy's `content_hash()` before it runs (equal across
    copies and to `base_hash_before`); `base_hash_after` is `base`'s after every copy has run (a copy
    that shared state with `base` would move it); `depth` is `summarise`'s distribution over every
    act; `chains` is `chains`' multiset.

    TWO RESIDUES, so a difference is read as the chooser's draw on THIS arm and not as the whole of
    the world's stochasticity:
      1. EVERY DRAW OUTSIDE THE CHOOSER'S FACTORY STAYS KEYED TO `w.world_seed`: the contest draws
         and the weather draws read the world's seed, not the draw seed, so they are identical
         across draw seeds and are not varied here.
      2. `declare_intents` CONSUMES THE CHOOSER'S DRAW TOO (`decision/choose.py`: one draw keyed by
         the person and `intent:<act id>`), so a draw seed also moves which intents are declared;
         but that branch is INERT while `intent_disclosure` is 0.0 (its shipped value), so at that
         value the draw seed reaches the run only through the choice order. Under a fixture that
         raises `intent_disclosure` the arm varies both."""
    out = {"base_hash_before": base.content_hash(), "runs": {}}
    for ds in draw_seeds:
        w = fork(base)
        start = w.content_hash()
        w, d, bounds = drive(w.world_seed, seasons, "off", world=w, draw_seed=ds)
        r = read(w.log, d.act_of, bounds)
        out["runs"][ds] = {"start_hash": start, "acts": len(r["acts"]),
                           "depth": summarise(r["acts"].values())["depth"],
                           "chains": chains(r["acts"], {a.id: a.verb for a in d.act_of.values()})}
    out["base_hash_after"] = base.content_hash()
    # The two fixtures the residues below turn on, read AFTER the hash so the read cannot move it: the
    # arm records the values it ran at.
    out["fixtures"] = {k: base.fixtures.get(k) for k in ("choice_temperature", "intent_disclosure")}
    return out


def chain_difference(a: Counter, b: Counter) -> int:
    """How many chains the two multisets do not share: the sum over chains of `|count_a - count_b|`.
    Zero exactly when the multisets are equal."""
    return sum(abs(a.get(k, 0) - b.get(k, 0)) for k in set(a) | set(b))


# ---------------------------------------------------------------------------------------------
# THE `--remove` ARM: suppress one person's choice at one lap, on one built world.
# ---------------------------------------------------------------------------------------------

def _removing(who, when, stamps: dict, fired: list):
    """The `wrap_chooser` of `removal_arm`: a chooser that returns nothing for person `who` when
    `(tick, lap) == when`, and records, for every act any other call returns, the `(tick, lap)` it was
    chosen at (`stamps[id(act)] = (at, act)`; the act is kept so its `id()` is not reused). `who=None`
    removes nobody: the stamping alone, the replay control."""
    def wrap(chooser):
        d = chooser.driver

        def choose(p, v, s, ask_budget):
            at = (d.w.tick, d.lap)
            if who is not None and p.id == who and at == when:
                fired.append(at)
                return []
            out = chooser(p, v, s, ask_budget)
            for item in out:
                for a in getattr(item, "acts", (item,)):
                    stamps[id(a)] = (at, a)
            return out
        return choose
    return wrap


def _removal_run(base, seasons: int, who, when, draw_seed=None) -> tuple:
    """`(multiset, fired, end_hash)` of ONE copy of `base` run `seasons` seasons with `who`'s choice
    suppressed at `when`. The multiset is over EVERY person's attempted acts (the act store), keyed
    `(actor, tick, lap, verb, opportunity, "executed" | "refused")`, the tick and lap being those the
    act was CHOSEN at; a refusal is `corpus_run.attempts`' (the one owner of the made/refused rule).
    `fired` is how many times the wrapper suppressed a call: 0 means the removal never happened and the
    reading is a replay's, not a removal's."""
    stamps: dict = {}
    fired: list = []
    w = fork(base)
    w, _d, bounds = drive(w.world_seed, seasons, "off", world=w, draw_seed=draw_seed,
                          wrap_chooser=_removing(who, when, stamps, fired))
    read_ = Counter()
    for a, _made, refused in attempts(w, len(bounds)):
        (tick, lap), _a = stamps[id(a)]
        read_[(a.actor, tick, lap, a.verb, opportunity_key(a.verb, subject_of(a), a.payload),
               "refused" if refused else "executed")] += 1
    return read_, len(fired), w.content_hash()


def _others(acts: Counter, who) -> Counter:
    """`acts` without person `who`'s keys (`who=None`: all of them)."""
    return Counter({k: n for k, n in acts.items() if who is None or k[0] != who})


def removal_arm(base, seasons: int, who: str, when: tuple) -> dict:
    """THE REMOVAL TEST (CLAUDE.md §4: the word and its definition). *Suppress one person's choice at
    one lap and count how many of the other persons' acts differ from the unperturbed copy.*

    ONE built world `base`, deep-copied (`fork`, as `draw_seed_arm` does), run `seasons` seasons through
    `drive` with the chooser wrapped (`drive(wrap_chooser=...)`) to return no scene for person `who`
    at `(tick, lap) == when` -- `when` is `(season index, lap index)`, the tick and `SeasonDriver.lap`
    (named `lap` since the rename `PCR-4`; a lap is one pass of the season's scene budget).
    Returns the multiset of the OTHER persons' `(actor, tick, lap, verb, opportunity, executed |
    refused)`; `chain_difference` of two such multisets is the acts that differ. `who=None` removes
    nobody and returns every person's acts. `base` is never run, so it stays unmutated; every draw is
    keyed `H(seed, tick, subject, purpose)`, so removing one choice shifts no other person's draw."""
    return _others(_removal_run(base, seasons, who, when)[0], who)


def citation_counts(acts: dict) -> Counter:
    """`{person: n}` over `read`'s `acts`: `n` is how many (act, antecedent act) pairs name an act of that
    person as a CROSS-person antecedent of another person's act, i.e. the actor of the most antecedents
    of other persons' acts is the person whose acts others' acts most answer. Counted per antecedent
    ACT, as `read` classes them (a cause Event of the same act twice is one antecedent), not per cause
    Event [ASSUMPTION: the act is the unit `read` already uses; revert: count the cross causes]."""
    out: Counter = Counter()
    for row in acts.values():
        for b in row["cross"]:
            if b in acts:
                out[acts[b]["actor"]] += 1
    return out


def most_cited(base, seasons: int = 1) -> tuple:
    """`(person, n)`: the person who is the actor of the most `Event.causes` antecedents of OTHER persons'
    acts in the unperturbed copy of `base`'s first `seasons` season(s) (`citation_counts`), ties by the
    smallest person id. `(None, 0)` when no act has a cross-person antecedent. `base` is never run."""
    w, d, bounds = drive(base.world_seed, seasons, "off", world=fork(base))
    counts = citation_counts(read(w.log, d.act_of, bounds)["acts"])
    if not counts:
        return None, 0
    who = min(counts, key=lambda p: (-counts[p], p))
    return who, counts[who]


def removal_verdict(res: dict, when: tuple) -> dict:
    """The two readings `--remove` ends on, over `removal_report`'s result and the lap removed at:
    `n` the OTHER persons' acts differing in the `removed` arm (the removed person's own acts are cut
    from both sides by `_others`, so none counts), `m` those of them chosen at a LATER `(season, lap)`
    than `when` (the same lap's differences are the within-lap order's, not a consequence), and `replay`
    the `replay` arm's differing, the control that MUST read 0: a replay above 0 voids `n` and `m`.

    WHAT IS EXPECTED. `replay` exactly 0 and the unwrapped hash equal to the unperturbed one are the two
    controls that read zero. `removed` is expected ABOVE 0 for a person who forms a scene at `when`
    (`fired` 1), and exactly 0 where the unperturbed copy shows him forming none. The `cohort` arm is NOT
    a zero control: it removes one more person and reads that removal's own consequences, which is why
    it is printed apart and carries no expectation of 0; `draw-seed` re-draws everybody and is the
    floor a single removal is read beside."""
    arm = res["arms"]["removed"]
    return {"n": arm["differing"],
            "m": sum(v for k, v in arm["by_lap"].items() if tuple(k) > tuple(when)),
            "replay": res["arms"]["replay"]["differing"]}


def removal_report(base, seasons: int, who: str, when: tuple, cohort) -> dict:
    """What `--remove` prints: the unperturbed copy, then each arm against it.
    `{"base_hash_before", "base_hash_after", "unperturbed": (acts, end hash), "unwrapped_hash", "arms"}`.
    `unwrapped_hash` is the end hash of a copy run through `drive` with no wrapper: the control that the
    wrapper perturbs nothing (it must equal the unperturbed copy's, else every figure is void). `arms`
    maps, in print order, `replay` (nobody removed, MUST read 0), `removed` (`who`), `cohort` (the named
    cohort person's choice, a SECOND removal read beside the first: it is not a zero control, see
    `removal_verdict`) and `draw-seed` (every person's chooser draw
    re-seeded, `--draw-seeds`' arm: the floor) to `{"acts", "differing", "persons", "by_lap", "fired",
    "hash", "who"}`. `differing` is the multiset difference (as `chain_difference`) over the persons
    other than the one removed; `by_lap` counts it per `(tick, lap)` of the act."""
    before = base.content_hash()
    ref, _f, ref_hash = _removal_run(base, seasons, None, when)
    plain = drive(0, seasons, "off", world=fork(base))[0].content_hash()
    out = {"base_hash_before": before, "unperturbed": (sum(ref.values()), ref_hash),
           "unwrapped_hash": plain, "arms": {}}
    specs = (("replay", None, None), ("removed", who, None), ("cohort", cohort, None),
             ("draw-seed", None, base.world_seed + 1))
    for name, gone, ds in specs:
        got, fired, h = _removal_run(base, seasons, gone, when, draw_seed=ds)
        a, b = _others(ref, gone), _others(got, gone)
        diff = {k: abs(a.get(k, 0) - b.get(k, 0)) for k in set(a) | set(b) if a.get(k, 0) != b.get(k, 0)}
        by_lap = Counter()
        for k, n in diff.items():
            by_lap[(k[1], k[2])] += n
        out["arms"][name] = {"acts": sum(b.values()), "differing": sum(diff.values()),
                             "persons": len({k[0] for k in diff}), "by_lap": dict(sorted(by_lap.items())),
                             "fired": fired, "hash": h, "who": gone}
    out["base_hash_after"] = base.content_hash()
    return out


def _print_removal(base_seed: int, seasons: int, cap, when, res: dict) -> None:
    print(f"storybar --remove base-seed={base_seed} seasons={seasons} cap={cap} at={tuple(when)} "
          f"PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
    print(f"base world hash before={res['base_hash_before']} after={res['base_hash_after']} "
          f"({'unmutated' if res['base_hash_before'] == res['base_hash_after'] else 'MUTATED'})")
    n, h = res["unperturbed"]
    print(f"[unperturbed] acts={n} end_hash={h}")
    print(f"[control: drive with no wrapper] end_hash={res['unwrapped_hash']} "
          f"({'EQUAL' if res['unwrapped_hash'] == h else 'DIFFER'} to the unperturbed; DIFFER means "
          f"the wrapper perturbs the run and every figure below is void)")
    for name, r in res["arms"].items():
        who = f" {r['who']}" if r["who"] else ""
        removes = name in ("removed", "cohort")
        note = ("  NOT FIRED: the person was not asked at that lap; this is a replay's reading"
                if removes and not r["fired"] else "")
        print(f"[{name}{who}] differing={r['differing']} persons_affected={r['persons']} "
              f"fired={r['fired']} end_hash={r['hash']} "
              f"({'EQUAL' if r['hash'] == h else 'DIFFER'} to the unperturbed){note}")
        if r["by_lap"]:
            print("  by (season, lap): " + " ".join(f"{k}:{v}" for k, v in r["by_lap"].items()))
    v = removal_verdict(res, when)
    print(f"R-01.c  others' acts differing: {v['n']}  (replay {v['replay']})"
          f"{'' if v['replay'] == 0 else '  REPLAY NOT 0: every figure is void'}")
    print(f"R-02.b  differing at a later (season, round): {v['m']}")


def _print_draw_seeds(base_seed: int, seasons: int, cap, draw_seeds, res: dict) -> None:
    print(f"storybar --draw-seeds base-seed={base_seed} seasons={seasons} cap={cap} "
          f"draw-seeds={list(draw_seeds)} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
    print(f"base world hash before={res['base_hash_before']} after={res['base_hash_after']} "
          f"({'unmutated' if res['base_hash_before'] == res['base_hash_after'] else 'MUTATED'}) "
          f"ran at {res['fixtures']}")
    first = next(iter(res["runs"]), None)
    for ds, r in res["runs"].items():
        ch = r["chains"]
        longest = max((len(k) for k in ch), default=0)
        print(f"[draw {ds}] start_hash={r['start_hash']} acts={r['acts']} first_acts={sum(ch.values())} "
              f"depth={r['depth']} longest_chain={longest}")
        for k, n in sorted(ch.items(), key=lambda kv: (-len(kv[0]), kv[0])):
            if len(k) >= 2:
                print(f"  chain x{n}: {' > '.join(k)}")
        if ds != first:
            diff = chain_difference(res["runs"][first]["chains"], ch)
            same_depth = res["runs"][first]["depth"] == r["depth"]
            print(f"[draw {first} vs {ds}] chains {'EQUAL' if diff == 0 else 'DIFFER'} "
                  f"(differing={diff}); depth {'EQUAL' if same_depth else 'DIFFER'}")


# ---------------------------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------------------------

def _fmt(r: dict) -> str:
    c = r["classes"]
    return (f"acts={r['acts']} cross={c['cross']} own={c['own']} world={c['world']} "
            f"none={c['none']} cross_share={100 * r['cross_share']:.1f}% "
            f"depth={r['depth']} max_depth={r['max_depth']}")


def _fmt_exec(r: dict) -> str:
    return (f"acts={r['acts']} executed={r['executed']} with_exec_cross={r['with_cross']} "
            f"exec_share={100 * r['share']:.1f}% exec_depth={r['depth']} "
            f"refused={r['refused']} refused_depth>=2={r['refused_deep']} graded_losses={r['graded']} "
            f"| default: depth>=2={r['deep']} cross={r['cross']} "
            f"cross_share={100 * r['cross_share']:.1f}%")


def _fmt_est(e: dict) -> str:
    return "  ".join(f"{name} pairs={s['pairs']} mean={s['mean']:.3f} min={s['min']:.3f} "
                     f"max={s['max']:.3f} distinct={s['distinct']}" for name, s in e.items())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base-seed", type=int, nargs="+", required=True, metavar="S",
                    help="the realm's seed; with --remove several may be named and each is run in turn, "
                         "printing its own report; every other mode takes exactly one")
    ap.add_argument("--n", type=int, help="seeded realms per arm (required without --draw-seeds)")
    ap.add_argument("--seasons", type=int, required=True)
    ap.add_argument("--arms", nargs=2, choices=ARMS,
                    help=f"two forcing arms to compare; built: {', '.join(ARMS)} "
                         f"(required without --draw-seeds)")
    ap.add_argument("--cap", type=int, default=None,
                    help="build_realm's cast cap; omitted = build_realm's own None, the full realm")
    ap.add_argument("--executed-only", action="store_true",
                    help="beside each current line print the executed reading (acts none of whose "
                         "Events is a refusal kind, cross antecedents cut to executed acts, depth "
                         "recomputed along them), and one `executed seed=` total line per seed so "
                         "single-seed runs can be summed; the current lines print as without it. "
                         "Not with --draw-seeds")
    ap.add_argument("--draw-seeds", type=int, nargs="+", metavar="D",
                    help="instead of the arm comparison: build_realm(--base-seed) ONCE, deep-copy it "
                         "per draw seed D, and vary only the chooser's draw (see `draw_seed_arm` for "
                         "the two residues); prints the chain-depth distribution and the verb-chain "
                         "multiset per draw seed. Takes no --n or --arms")
    ap.add_argument("--remove", metavar="PERSON", nargs="?", const=MOST_CITED,
                    help="the removal test: suppress PERSON's choice at one lap (--at; the first when "
                         "omitted) on ONE built world, and count how many of the OTHER persons' acts "
                         "differ from the unperturbed copy. With no PERSON it takes the person who is "
                         "the actor of the most antecedents of other persons' acts in the unperturbed "
                         "copy's first season (ties by person id) and prints the name. Prints the "
                         "acts differing, the persons affected and the (season, lap) of each, beside "
                         "controls: replay (nobody removed, MUST read 0), a cohort's choice (a second "
                         "removal, expected above 0, not a zero control), and the chooser's draw "
                         "re-seeded for everybody (`--draw-seeds`' arm, the floor); it ends on two "
                         "lines, `R-01.c` (the others' acts differing, beside the replay) and "
                         "`R-02.b` (those at a later lap). Takes no --n or --arms; one arm is a "
                         "full copy of the run")
    ap.add_argument("--at", type=int, nargs=2, metavar=("SEASON", "LAP"),
                    help="with --remove: the (season index, lap index) whose choice is suppressed")
    ap.add_argument("--null-scenes", action="store_true",
                    help="instead of the arm comparison: run one realm per --base-seed under the shipped "
                         "arm and print, per seed and per season and pooled, how many acts left no "
                         "durable write (`null_scenes`, which owns the definition): `null_scenes "
                         "total=<n> null=<n> | <verb/class=n, ...>`. A reading, never a threshold. "
                         "Takes no --n, --arms, --draw-seeds, --remove or --executed-only; several "
                         "--base-seed values may be named")
    args = ap.parse_args(argv)

    if args.at is not None and args.remove is None:
        ap.error("--at belongs to --remove")
    if args.remove is None and not args.null_scenes and len(args.base_seed) != 1:
        ap.error("several --base-seed values belong to --remove and --null-scenes; every other mode "
                 "takes one")
    if args.null_scenes:
        if args.n is not None or args.arms is not None or args.draw_seeds is not None \
                or args.remove is not None or args.executed_only:
            ap.error("--null-scenes takes no --n, --arms, --draw-seeds, --remove or --executed-only")
        print(f"storybar --null-scenes base-seeds={args.base_seed} seasons={args.seasons} cap={args.cap} "
              f"PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
        got = {seed: null_by_season(seed, args.seasons, args.cap) for seed in args.base_seed}
        for seed, (per, whole) in got.items():
            for s, r in enumerate(per):
                print(f"[seed {seed}] season {s}: {null_line(r)}")
            print(f"[seed {seed}] all seasons: {null_line(whole)}")
        if len(got) > 1:
            for s in range(args.seasons):
                print(f"[pooled] season {s}: {null_line(pool_null(per[s] for per, _ in got.values()))}")
            print(f"[pooled] all seasons: {null_line(pool_null(whole for _, whole in got.values()))}")
        return 0
    if args.remove is not None:
        if args.n is not None or args.arms is not None or args.draw_seeds is not None \
                or args.executed_only:
            ap.error("--remove takes no --n, --arms, --draw-seeds or --executed-only")
        when = tuple(args.at) if args.at is not None else (0, 0)
        for seed in args.base_seed:
            base = build_realm(seed, args.cap)
            who = args.remove
            if who == MOST_CITED:
                who, cited = most_cited(base)
                if who is None:
                    ap.error(f"--base-seed {seed}: no act of the first season has a cross-person "
                             f"antecedent, so no person is the most cited; name one")
                print(f"storybar --remove names {who}: the actor of {cited} antecedents of other "
                      f"persons' acts in the unperturbed first season (base-seed={seed})")
            elif who not in base.persons:
                ap.error(f"--remove {who!r} is not a person of the realm built from --base-seed {seed}")
            cohort = next((p for p in sorted(base.persons)
                           if p.startswith(COHORT_PREFIX) and p != who), None)
            _print_removal(seed, args.seasons, args.cap, when,
                           removal_report(base, args.seasons, who, when, cohort))
        return 0

    base_seed = args.base_seed[0]

    if args.draw_seeds is not None:
        if args.n is not None or args.arms is not None:
            ap.error("--draw-seeds takes no --n or --arms")
        if args.executed_only:
            ap.error("--draw-seeds takes no --executed-only")
        if len(set(args.draw_seeds)) != len(args.draw_seeds):
            ap.error("--draw-seeds names a seed twice: the run is keyed by draw seed, so the repeat "
                     "would silently collapse into one")
        res = draw_seed_arm(build_realm(base_seed, args.cap), args.seasons, args.draw_seeds)
        _print_draw_seeds(base_seed, args.seasons, args.cap, args.draw_seeds, res)
        return 0
    missing = [f for f, v in (("--n", args.n), ("--arms", args.arms)) if v is None]
    if missing:
        ap.error(f"the following arguments are required: {', '.join(missing)}")

    seeds = list(range(base_seed, base_seed + args.n))
    res = compare(args.arms, seeds, args.seasons, args.cap, args.executed_only)
    print(f"storybar seeds={seeds[0]}..{seeds[-1]} seasons={args.seasons} arms={list(args.arms)} "
          f"cap={args.cap} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
    for i, arm_res in enumerate(res):
        arm = arm_res["arm"]
        for seed, sr in arm_res["seeds"].items():
            print(f"[arm {i}:{arm}] seed={seed} resolved={sr['resolved']} unread={sr['unread']}")
            for s, (this, cum) in enumerate(sr["per_season"]):
                print(f"  season {s}: {_fmt(this)}")
                print(f"  through {s}: {_fmt(cum)}")
                if args.executed_only:
                    ex_this, ex_cum = sr["executed_per_season"][s]
                    print(f"  executed season {s}: {_fmt_exec(ex_this)}")
                    print(f"  executed through {s}: {_fmt_exec(ex_cum)}")
                print(f"  estimates {s}: {_fmt_est(sr['estimates'][s])}")
            if args.executed_only:
                print(f"[arm {i}:{arm}] executed seed={seed} total: {_fmt_exec(sr['executed_total'])}")
        for s, (this, cum) in enumerate(arm_res["pooled"] if len(seeds) > 1 else ()):
            print(f"[arm {i}:{arm}] pooled season {s}: {_fmt(this)}")
            if args.executed_only:
                ex_this, ex_cum = arm_res["executed_pooled"][s]
                print(f"[arm {i}:{arm}] pooled executed season {s}: {_fmt_exec(ex_this)}")
            print(f"[arm {i}:{arm}] pooled through {s}: {_fmt(cum)}")
            if args.executed_only:
                print(f"[arm {i}:{arm}] pooled executed through {s}: {_fmt_exec(ex_cum)}")
    equal = res[0]["pooled"] == res[1]["pooled"]
    print(f"arms {args.arms[0]} vs {args.arms[1]}: "
          f"{'EQUAL' if equal else 'DIFFER'} on every pooled season reading")
    return 0


if __name__ == "__main__":
    sys.exit(main())
