"""`harness.clocks` -- THE FIRST SEASON OF EACH MARK AN ARC RUNS THROUGH, PER SEED (v12 B21d.04, CR-90).

An INSTRUMENT, like `harness/strife.py`: it reads the log and the world and writes nothing, so it moves no hash. Per seed it reads the FIRST season (1 is the
first season run) in which each mark holds, or `never`:

    each clock band crossed   the TRUE fold (`world_q.clock`, the log's Events up to that season) and each head's BELIEVED fold (`person_q.believed_clock`, the
                              Events he holds a claim of, up to that season; his ledger as it ends, so a claim evicted since reads as never heard). The heads are
                              the persons `world_q.head` answers for, one per faction that has one. CARRIER
    breakdown                 true: the Turmoil crisis band and `breakdown_sittings` of the last `breakdown_window` sittings of the determining arrangement
                              (`world_q.sittings_failed`'s count, `queries/clock.py::sittings_failed_of`, to that season); believed: `person_q.believed_breakdown`
                              per head. CARRIER
    claim                     the first `claim:<faction>:<rung>` Proposition (`world_q.CLAIM_MOOD`) uttered, by its `Proposition.when`. CARRIER
    civil war                 `faction_q.civil_war` of the two factions of a live WAR Proposition. A LIVE READING OF THE WORLD, so it is read after each season
                              (`observe`), never from the end state. CARRIER
    declare                   the first `war.declared` Event (`declare`'s emitted kind). EVENT KIND, no carrier holds "a war was ever declared": `world_q.at_war` is
                              the war's presence now
    theocratic declare        the first `war.declared` whose causing act's actor belongs to the Church faction. EVENT KIND, the Church read as the one faction the
                              `church_influence` row's feeders name (`rosters.yaml: tables.clocks`), never a name here. A theocratic WAR Proposition is minted by
                              nothing before B21d.06 (`world_q._church_under_theocratic_war`)
    Church rung.seized        the first `rung.seized` Event whose causing act's actor belongs to that faction. EVENT KIND
    parliament                whether a `matter.determined` Event whose proceeding held `determining_arrangement()` follows (in the log's order) the first
                              `war.declared`; `None` for no war. EVENT KIND

BREAKDOWN'S ARRANGEMENT is `parliamentary_debate`, which `arrangements.yaml` carries (`bench_basis: determine`); a tree without it reads the first arrangement whose
bench's basis is `determine`. Pooled, a mark's share is the seeds reaching it by each season, with the first seasons' spread (min..max).

`--arm NAME[,NAME...]` names the trigger switches (`Fixtures` fields) thrown ON for the run; the default is none, every trigger off. [ASSUMPTION; medium; Jordan to
correct; revert: delete the flag.] The switches (`ci_*_on`, `turmoil_*_on`, `nation_functions_on`) are B21d.06's; a name with no `Fixtures` field is refused, naming
it, before anything runs, and a field that is no switch (not a bool) is refused likewise.

    python -m engine.season.harness.clocks <seasons> <seed> [seed ...] [--arm NAME[,NAME...]]
"""
from __future__ import annotations

import sys
from typing import Callable, NamedTuple, Optional

from ..boot.realm import build_realm
from ..data.arrangements import ARRANGEMENTS
from ..data.rosters import clocks
from ..data.verbs import DISPOSAL_EVENTS
from ..gaps import Ungraded
from ..queries import faction_q, person_q, world_q
from ..queries.clock import sittings_failed_of
from . import populated

PREFERRED_ARRANGEMENT = "parliamentary_debate"
WAR_KIND, SEIZED_KIND = "war.declared", "rung.seized"
NEVER = "never"
SINGLE_MARKS = ("breakdown", "claim", "declare", "civil war", "theocratic declare", "church rung.seized")


def determining_arrangement() -> str:
    """THE ARRANGEMENT BREAKDOWN COUNTS SITTINGS OF: `parliamentary_debate` where `arrangements.yaml` carries it, else the first row whose bench's basis is
    `determine` (a sitting that can determine)."""
    if PREFERRED_ARRANGEMENT in ARRANGEMENTS:
        return PREFERRED_ARRANGEMENT
    return next(i for i, r in ARRANGEMENTS.items() if r["bench_basis"] == "determine")


def church_faction() -> Optional[str]:
    """The faction the `church_influence` row's feeders name as an actor's faction -- the one the clock row calls the Church, read from the row and named nowhere here."""
    named = {f.actor_faction for f in clocks()["church_influence"].feeders} - {None}
    return next(iter(named), None)


def heads(w) -> dict:
    """`{faction Proposition id: its head}` for each faction `world_q.head` answers for."""
    return {f: h for f in sorted(world_q.faction_props(w)) if (h := world_q.head(w, f)) is not None}


def band_marks() -> list:
    """`"<clock>:<band>"` for each band of each clock row, in the roster's order."""
    return [f"{name}:{b.name}" for name, row in clocks().items() for b in row.bands]


class Reading(NamedTuple):
    """ONE WORLD'S READING. `marks`: `{mark: first season or None}` of the true marks; `believed`: `{faction: {mark: first season or None}}` for each head (the band
    marks and `breakdown`); `ends`: `{clock: (true value, {faction: his believed value})}` at the last season; `parliament_after_war`: `None` (no war), `True` or `False`."""
    marks: dict
    believed: dict
    ends: dict
    parliament_after_war: Optional[bool]


def _first(ticks, holds) -> Optional[int]:
    """The first season (1-based) of `ticks` at which `holds(tick)` is true, else `None`."""
    return next((i + 1 for i, t in enumerate(ticks) if holds(t)), None)


def _season(tick: int, t0: int, seasons: int) -> Optional[int]:
    return tick - t0 + 1 if 0 <= tick - t0 < seasons else None


def _earliest(ticks, t0: int, seasons: int) -> Optional[int]:
    seen = [s for t in ticks if (s := _season(t, t0, seasons)) is not None]
    return min(seen) if seen else None


def read_world(w, t0: int, seasons: int, civil: Optional[int] = None) -> Reading:
    """READ `w`, whose reading began at tick `t0` and ran `seasons` seasons, for every mark. `civil` is the first season a civil war held (`observe`), which only the
    world after each season can say. Writes nothing."""
    ticks = range(t0, t0 + seasons)
    fx, arr = w.fixtures, determining_arrangement()
    clock_rows = clocks()
    at = lambda band: fx.get(band.at)
    marks: dict = {}
    for name, row in clock_rows.items():
        for b in row.bands:
            marks[f"{name}:{b.name}"] = _first(ticks, lambda t, n=name, b=b: world_q.clock(w, n, t) >= at(b))
    clock_name, crisis_name = person_q.BREAKDOWN_BAND
    crisis = at(next(b for b in clock_rows[clock_name].bands if b.name == crisis_name))
    sittings = world_q.sitting_events(w, w.log)
    window, need = fx.get("breakdown_window"), fx.get("breakdown_sittings")
    marks["breakdown"] = _first(ticks, lambda t: world_q.clock(w, clock_name, t) >= crisis
                                and sittings_failed_of([s for s in sittings if s.tick <= t], arr, window) >= need)
    claims = [c.when for pid, c in w.propositions.items() if c.mood == world_q.CLAIM_MOOD and pid.startswith("claim:")]
    marks["claim"] = _earliest(claims, t0, seasons)
    wars = [e for e in w.log if e.kind == WAR_KIND]
    church = church_faction()
    marks["declare"] = _earliest((e.emitted_at for e in wars), t0, seasons)
    marks["theocratic declare"] = _earliest((ce.tick for ce in world_q.clock_events(w, wars) if ce.actor_faction == church), t0, seasons)
    seized = [e for e in w.log if e.kind == SEIZED_KIND]
    marks["church rung.seized"] = _earliest((ce.tick for ce in world_q.clock_events(w, seized) if ce.actor_faction == church), t0, seasons)
    marks["civil war"] = civil
    # the believed folds: each head's, over the Events he holds a claim of that were emitted by that season
    of_clock, of_sitting = world_q.clock_events_by_claim(w), world_q.sitting_events_by_claim(w)
    believed, ends = {}, {n: (world_q.clock(w, n, ticks[-1]), {}) for n in clock_rows}
    for faction, pid in heads(w).items():
        p, got = w.persons[pid], {}
        for name, row in clock_rows.items():
            for b in row.bands:
                got[f"{name}:{b.name}"] = _first(ticks, lambda t, n=name, b=b: person_q.believed_clock(
                    p, n, {c: e for c, e in of_clock.items() if e.tick <= t}) >= at(b))
            ends[name][1][faction] = person_q.believed_clock(p, name, {c: e for c, e in of_clock.items() if e.tick <= ticks[-1]})
        got["breakdown"] = _first(ticks, lambda t: person_q.believed_breakdown(
            p, arr, {c: e for c, e in of_clock.items() if e.tick <= t}, {c: e for c, e in of_sitting.items() if e.tick <= t}, fx))
        believed[faction] = got
    after = None
    if wars:
        war_id, seen_war = wars[0].id, False        # the log's own order: a determination after the war's Event
        after = False
        for e in w.log:
            seen_war = seen_war or e.id == war_id
            after = after or (seen_war and e.kind == DISPOSAL_EVENTS["determine"] and world_q.ending_arrangement(e) == arr)
    return Reading(marks, believed, ends, after)


def civil_war_now(w) -> bool:
    """IS ANY LIVE WAR A CIVIL WAR (`faction_q.civil_war`) -- the pair of factions of each WAR Proposition, asked of the world as it stands."""
    return any(faction_q.civil_war(w, p.subject, p.value) for p in list(w.propositions.values()) if p.mood == world_q.WAR_MOOD)


def observe(w, seed: int, seasons: int, step: Callable = populated.run, civil_now: Callable = civil_war_now) -> Optional[int]:
    """RUN `seasons` seasons of `w` ONE AT A TIME (`step(1, seed, w=w)`, `populated.run` -- its own driver per call reads the same as one call over all of them) and
    return the first season after which `civil_now(w)` held, else `None`. The one reading the end state cannot give."""
    first = None
    for k in range(1, seasons + 1):
        step(1, seed, w=w)
        if first is None and civil_now(w):
            first = k
    return first


def _arm(w, names) -> None:
    """Throw each named switch ON for `w`. A name with no `Fixtures` field, or a field that is no switch, raises `SystemExit` naming it."""
    for n in names:
        try:
            cur = w.fixtures.get(n)
        except Ungraded:
            raise SystemExit(f"--arm {n}: no `Fixtures` field of that name. The trigger switches (`ci_*_on`, `turmoil_*_on`, `nation_functions_on`) are "
                             f"added by B21d.06; until a field exists the only arm is the default, every trigger off.")
        if not isinstance(cur, bool):
            raise SystemExit(f"--arm {n}: `Fixtures {n}` is {cur!r}, not a switch (a bool).")
        w.fixtures = w.fixtures.sweep(n, True)


def measure(seasons: int, seeds: tuple, arm: tuple = ()) -> dict:
    """Build, run and read each seed (`{seed: Reading}`). `arm` names the switches on."""
    out = {}
    for s in seeds:
        w = build_realm(s)
        _arm(w, arm)
        t0 = w.tick
        civil = observe(w, s, seasons)
        out[s] = read_world(w, t0, seasons, civil)
    return {"seasons": seasons, "seeds": tuple(seeds), "arm": tuple(arm), "readings": out}


def _fmt(season) -> str:
    return NEVER if season is None else str(season)


def _believed_any(r: Reading) -> dict:
    """`{mark: the earliest season any head believes it}` for the band marks and `breakdown`."""
    keys = band_marks() + ["breakdown"]
    return {k: min((b[k] for b in r.believed.values() if b[k] is not None), default=None) for k in keys}


def _seed_block(seed: int, r: Reading, seasons: int) -> list:
    out = [f"seed {seed}   (first season of each mark, 1 to {seasons}, or {NEVER})"]
    for name, row in clocks().items():
        true, held = r.ends[name]
        out.append(f"  {name:<16} true: " + ", ".join(f"{b.name} {_fmt(r.marks[f'{name}:{b.name}'])}" for b in row.bands)
                   + f"   end {true:g}; heads believe {min(held.values(), default=0):g}..{max(held.values(), default=0):g}")
    reach = {f: b for f, b in r.believed.items() if any(v is not None for v in b.values())}
    for f, b in reach.items():
        out.append(f"    head of {f} believes: " + ", ".join(f"{k} {_fmt(v)}" for k, v in b.items() if v is not None))
    if not reach:
        out.append(f"    no head believes any band or a breakdown ({len(r.believed)} heads read)")
    out.append("  " + "; ".join(f"{m} {_fmt(r.marks[m])}" for m in SINGLE_MARKS))
    par = {None: "no war, so not asked", True: "yes", False: "no"}[r.parliament_after_war]
    out.append(f"  parliament still determines a matter after the first war: {par}")
    return out


def _pooled(m: dict) -> list:
    seeds, seasons, rs = m["seeds"], m["seasons"], m["readings"]
    rows = [(k, [rs[s].marks[k] for s in seeds]) for k in band_marks() + list(SINGLE_MARKS)]
    rows += [(f"{k} (a head believes)", [_believed_any(rs[s])[k] for s in seeds]) for k in band_marks() + ["breakdown"]]
    out = [f"POOLED over seeds {list(seeds)}: the share of seeds reaching each mark by season 1..{seasons}, and the first seasons' spread"]
    for k, firsts in rows:
        got = [f for f in firsts if f is not None]
        by = "  ".join(f"{n} {sum(1 for f in got if f <= n)}/{len(seeds)}" for n in range(1, seasons + 1))
        out.append(f"  {k:<40} by season: {by}   spread {min(got)}..{max(got)}" if got else f"  {k:<40} by season: {by}   spread {NEVER}")
    war = [rs[s].parliament_after_war for s in seeds if rs[s].parliament_after_war is not None]
    out.append(f"  parliament determines after the first war: {sum(war)}/{len(war)} of the seeds with a war")
    return out


def report(m: dict) -> str:
    arm = ", ".join(m["arm"]) + " on" if m["arm"] else "none (every trigger off)"
    out = [f"clock marks: {m['seasons']} seasons, seeds {list(m['seeds'])}, arm: {arm}",
           f"breakdown counts sittings of: {determining_arrangement()}; believed folds: each faction's `world_q.head`", ""]
    for s in m["seeds"]:
        out += _seed_block(s, m["readings"][s], m["seasons"]) + [""]
    return "\n".join(out + _pooled(m))


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    arm: list = []
    while "--arm" in a:
        i = a.index("--arm")
        if i + 1 >= len(a):
            print("usage: --arm needs a name")
            return 2
        arm += [x for x in a[i + 1].split(",") if x]
        del a[i:i + 2]
    if len(a) < 2:
        print("usage: python -m engine.season.harness.clocks <seasons> <seed> [seed ...] [--arm NAME[,NAME...]]")
        return 2
    print(report(measure(int(a[0]), tuple(int(x) for x in a[1:]), tuple(arm))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
