"""`harness.obligee_report` -- M0e, THE OBLIGEE-REPORTS-TO-HIS-SEAT-HOLDER READER (v10 IN-18, G5's trigger).

It reads a finished world; it writes nothing, mints nothing and is read by nothing in the game, so it
moves no hash. It is an INSTRUMENT in the shape of `harness/storybar.py` and `harness/arc.py`: it
PRINTS a figure and grades nothing, and no test asserts what a realm run reads (rule V2: a reader,
never an assertion). The only assertions on it are on HAND-BUILT worlds, where the answer is known.

WHY IT EXISTS. G5 of the telling table (a duty to report: an obligee forms a `tell` to the seat holder)
was gated on a trigger, M0e > 0, which B-I read as 0 over four realm seasons (2026-10-13) with a scratch
counter that was never committed (`m0_telling.py`, the telling workplan's T0, retired with that plan).
No command in the tree printed it, so the reading could not be re-taken. This module is the command.

M0e, DEFINED HERE (the telling workplan's row said only *"per obligee, `inferred` claims about a
person"*; v10 IN-18 restates the trigger as *"an obligee reporting to the seat holder"*; this reader
counts both, headline first, so neither reading is lost):

  * AN OBLIGEE is the SUBJECT of an `oblige` Tenure on a seat in `w.offices` (the edge
    `world_q.establishment_of` reads, through `state/gate.py::sworn_to`'s rule: kind `oblige`, object
    the seat), LIVE AT THE TICK OF THE EVENT BEING READ: `since <= tick` and `until` unset or `> tick`.
    An imposed `oblige` (a sentence) counts as the same edge, as it does there.
  * THE SEAT HOLDER is the subject of a `hold` Tenure on that same seat, live at the same tick.
    `world_q.hold_force` answers only for NOW; a run's log spans ticks, so the window is read here, by
    the same `kind`/`object` test.
  * ⚠ SURVIVORS ONLY. `World.tenures` is the living persons' `Person.tenures`, and `remove_person`
    closes a dead person's edges and then drops him with them, so an obligee or a holder who died
    during the run is not in `w.tenures` at all: EVERY COUNT BELOW IS A LOWER BOUND whenever one did
    (seat-holders were 16 of the 20 deaths over seeds 0-4 at four seasons, CR-14's reading), and a 0 is
    a 0 over the survivors. Capturing the edges while the run goes changes what this reader is handed,
    not its arithmetic, and is not done here.
  * REPORTING, HEADLINE (`m0e`): an EXECUTED `tell` -- an Event of kind `news.told` whose causing act
    (`state/attribution.causing_act`) is a `tell` -- by an obligee, whose HEARER (the act's operand
    under the `tell` row's `counterparty:` column, read through `binding_from_act`, exactly as
    `loop/witness.py` reads it) is the holder of that obligee's seat. One count per (Event, seat).
  * REPORTING, ATTEMPTED (`attempted`): the same, over `news.told` AND `news.untold` Events (a refused
    or lost telling is still the obligee forming a `tell` to his holder).
  * REPORTING, HEARD (`told_by`): a `told_by` claim in the seat holder's ledger whose last chain hop
    (`Claim.teller`) is the obligee, deposited while both edges were live. It also counts a telling
    the holder overheard that was addressed to someone else; the ledger is capped, so it can fall
    below `m0e`.
  * THE TELLING WORKPLAN'S OWN M0e (`inferred_about_person`): the `inferred` claims (the obligee
    channel's source, `epistemic._ch_post_remit`) that an obligee holds ABOUT A PERSON. G5's marker
    site read that source, so it is the precondition the headline needs.

SOURCES: the trigger text is `workplans/valoria_master_workplan_v10_part4.md` IN-18 and the retired
telling workplan's §5 row G5 / §4 T0 M0e row (`git show 75acd96c^:workplans/2026-10-01-telling-workplan.md`).
Both are reference (`CLAUDE.md` §0.05); this module's code is the definition.

USAGE: `PYTHONHASHSEED=0 python -m engine.season.harness.obligee_report SEASONS SEED [SEED ...]`
builds `populated.build_realm(seed)`, runs `populated.run(SEASONS, seed, w=w)` once and prints the
reading. The tree is not touched.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import Optional

from ..data.requires import binding_from_act
from ..data.verbs import VERB_TABLE
from ..state.attribution import causing_act

TOLD = "news.told"
UNTOLD = "news.untold"
TOLD_BY = "told_by"
INFERRED = "inferred"


@dataclass
class ObligeeReading:
    m0e: int = 0                      # executed tells by an obligee to his seat's holder
    attempted: int = 0                # news.told + news.untold of the same
    told_by: int = 0                  # told_by claims in a holder's ledger, last hop an obligee
    inferred_about_person: int = 0    # inferred claims an obligee holds whose subject is a person
    obligee_edges: int = 0            # oblige Tenures on a seat in w.offices, of persons still in the world
    obligees: int = 0                 # distinct persons holding at least one such edge
    edges_with_holder: int = 0        # of those edges, how many had a holder at some tick they were live
    tells_by_obligees: int = 0        # executed tells by an obligee to anyone (the denominator)
    tells_all: int = 0                # executed tells in the log
    ticks: int = 0                    # how many distinct ticks the log spans
    by_pair: dict = field(default_factory=dict)   # (obligee, seat, holder) -> executed count
    attempted_by: dict = field(default_factory=dict)  # (kind, degree) -> count, over `attempted`
    edges_since: dict = field(default_factory=dict)   # Tenure.since -> oblige edges opened then

    def line(self) -> str:
        return (f"M0e={self.m0e} attempted={self.attempted} told_by={self.told_by} "
                f"inferred_about_person={self.inferred_about_person} | obligee_edges="
                f"{self.obligee_edges} obligees={self.obligees} edges_with_holder="
                f"{self.edges_with_holder} | tells_by_obligees={self.tells_by_obligees} "
                f"tells_all={self.tells_all} | ticks={self.ticks}")


def _live_at(t, tick: int) -> bool:
    return t.since <= tick and (t.until is None or tick < t.until)


def read_obligee_reports(w) -> ObligeeReading:
    """The reading over a world's whole log, and over the Tenures of the persons it still holds (see the
    module docstring for every definition and for what a death takes with it)."""
    out = ObligeeReading()
    counterparty = VERB_TABLE["tell"].counterparty
    seats = set(w.offices)
    obliges = [t for t in w.tenures if t.kind == "oblige" and t.object in seats
               and t.subject in w.persons]
    holds = [t for t in w.tenures if t.kind == "hold" and t.object in seats
             and t.subject in w.persons]
    out.obligee_edges = len(obliges)
    out.obligees = len({t.subject for t in obliges})
    for t in obliges:
        out.edges_since[t.since] = out.edges_since.get(t.since, 0) + 1
    out.edges_with_holder = sum(
        1 for t in obliges
        if any(h.object == t.object and (t.until is None or h.since < t.until)
               and (h.until is None or h.until > t.since) for h in holds))
    by_obligee: dict = {}
    for t in obliges:
        by_obligee.setdefault(t.subject, []).append(t)

    def holders(seat: str, tick: int) -> list:
        return [h.subject for h in holds if h.object == seat and _live_at(h, tick)]

    ticks = set()
    for e in w.log:
        ticks.add(e.emitted_at)
        if e.kind not in (TOLD, UNTOLD):
            continue
        a = causing_act(w, e)
        if a is None or a.verb != "tell":
            continue
        if e.kind == TOLD:
            out.tells_all += 1
        mine = [t for t in by_obligee.get(a.actor, ()) if _live_at(t, e.emitted_at)]
        if not mine:
            continue
        if e.kind == TOLD:
            out.tells_by_obligees += 1
        hearer = binding_from_act(a).get(counterparty)
        for seat in sorted({t.object for t in mine}):
            if hearer is not None and hearer in holders(seat, e.emitted_at):
                k = (e.kind, e.degree)
                out.attempted_by[k] = out.attempted_by.get(k, 0) + 1
                if e.kind == TOLD:
                    key = (a.actor, seat, hearer)
                    out.by_pair[key] = out.by_pair.get(key, 0) + 1
    out.attempted = sum(out.attempted_by.values())
    out.m0e = sum(out.by_pair.values())
    out.ticks = len(ticks)

    # HEARD: a told_by claim in a seat holder's ledger whose last hop is an obligee of that seat.
    for h in holds:
        for c in w.persons[h.subject].ledger:
            if c.source != TOLD_BY or not c.chain or not _live_at(h, c.when):
                continue
            if any(t.object == h.object and _live_at(t, c.when) for t in by_obligee.get(c.chain[-1], ())):
                out.told_by += 1
    # THE WORKPLAN'S OWN M0e: what an obligee holds `inferred` about a person.
    out.inferred_about_person = sum(
        1 for pid in by_obligee for c in w.persons[pid].ledger
        if c.source == INFERRED and c.subject in w.persons)
    return out


def main(argv: Optional[list] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 2:
        print(__doc__.split("USAGE:")[-1].strip())
        return 2
    from .populated import build_realm, run
    seasons = int(argv[0])
    for s in map(int, argv[1:]):
        w = build_realm(s)
        run(seasons, s, w=w)
        r = read_obligee_reports(w)
        print(f"seasons={seasons} seed={s} {r.line()}", flush=True)
        print(f"  by_pair={dict(sorted(r.by_pair.items()))} attempted_by="
              f"{dict(sorted(r.attempted_by.items(), key=str))} edges_since="
              f"{dict(sorted(r.edges_since.items()))} hash={w.content_hash()}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
