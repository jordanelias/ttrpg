"""THE PLAY SURFACE'S DISPATCH SEAM — a `choose` that hands named persons to a callback and everyone
else to the chooser the caller already built. v9 PC-06 `S-1`.

    from engine.season.harness.play_surface import dispatching_chooser
    choose = dispatching_chooser(make_chooser(fx, mint, verbs, draw), {"p_carin": my_callback})
    driver.season(choose, None, contest_max_depth=...)

**This is the whole single-player hook, and it edits no engine file.** `SeasonDriver.season` already
RECEIVES its chooser (`loop/driver.py`, `season(self, choose, ...)`) and DELIBERATE calls it once per
person as `choose(p, v, s, ask_budget)` (`loop/deliberate.py`). So a client that wants to decide for
one person needs no engine change: it passes a `choose` that dispatches on `p.id`. That is all this
module is.

⚠ **THE CALLBACK SEES WHAT `choose` SEES AND NOTHING MORE.** It is called as
`callback(p, v, s, ask_budget, auto)`: the same four person-side arguments DELIBERATE passes (a
`Person`, a `View`, a `Sensation`, the budget QUERY), plus `auto`, the delegate chooser itself. No
`World` reaches it through this seam; what a callback closes over is the client's own, and no scan
reaches it (CONVENTION, `04:246`'s MECHANICAL path scan covers `make_chooser`, not a callback). `auto` is passed so a client can show
or replay what the shipped policy would have done; calling it is the caller's choice.

⚠ **THE SEAM ADDS NO RULE.** It does not validate what the callback returns: DELIBERATE already
refuses a return over the person's budget (S26.3), a scene over the interaction bound, and an Act
whose actor is not the person deciding (L1). Re-checking here would be a second owner of those
rules. Nor does it build the delegate: the caller constructs `auto` exactly as it would have passed
it to `season` (`headless.run`, `populated.run`), so with no overrides the run is the shipped run.

**THE LINE CONTINUES, OR ENDS (v10 CP-T02-06)** is `carry_on`, the client's re-bind on this same seam, below.

The control (no file of that name exists; the seam is covered by `test_g2_token.py`, `test_rem30_character_sheet.py` and
`test_rem31_grid_suspension.py`): a callback that returns `auto`'s own pick leaves
`World.content_hash()` equal to the plain run on the same seed; a planted deviation for one person
moves it.

THE TRANSCRIPT (B34.04, `proposals/11_GO_player_surface_contract_B.md` §8) -- ONE RUNNER FOR EVERY PLAYABLE SCENARIO:

    python -m engine.season.harness.play_surface --seed S --person P --seasons K [--scenario NAME]

seats `P` with `take_ranked` and prints, per deliberation, the `Situation` (the asked rows), the `Offer` (each row with its terms and odds,
then the withheld rows) and the pick; then, at his next deliberation and once more when the run ends, the `account` of what he has learned
since. `--scenario NAME` resolves through `scenarios.SCENARIOS` and the run is `scenarios.run` -- the runner has no season loop of its own;
with no `--scenario` the row is `life`, the realm as built. The line `content_hash <hash>` is the hash of the plain run on the same seed (the transcript reads and writes nothing); where the run ended on a realm ending it is followed by
`ENDING <name> <kind>`, the last line.

⚠ **A PLAYER-FACING PRESENTATION IS TRIGGERED BY AN `AccountRow` OF THE SEATED PERSON, NEVER BY A LOG EVENT.** The log is the whole world; his
ledger is what he is entitled to. A port that hangs a cutscene on `scar.taken` in the log shows the player a scar he has not heard of (GO-B §7).

⚠ THE FACTION LINE IS THE HOST'S, NOT HIS. Once a season the transcript prints the seated person's faction's `faction_q.standing` at the
realm rung, labelled resolver-side: the world's reading, never his belief (AX-2). It is not a row of the `Situation` or of the `account`
and is never handed to `decision/`; it defines no footprint, density or provinces reading of its own.
"""
from __future__ import annotations

import argparse
import sys
from typing import Any, Callable, MutableMapping, Mapping, Optional, Sequence

from ..data import goals as goals_data
from ..decision.choose import TERM_NAMES
from ..decision.options import seat_of
from ..decision.sheet import account, chronicle, creation_sheet, offer, situation
from ..gaps import Forbidden
from ..loop.driver import resolvable_verbs
from ..queries import faction_q, world_q
from ..queries.person_q import content_kind, content_said, deed_doer_claims, deed_doers, dossier
from ..queries.world_q import continuations
from ..state.carriers import interior_of
from ..state.ids import draw_factory

# `(p, v, s, ask_budget) -> list[Act | Scene]` — DELIBERATE's call, the delegate's shape.
Chooser = Callable[..., list]
# `(p, v, s, ask_budget, auto) -> list[Act | Scene]` — the same four arguments, plus the delegate.
Callback = Callable[..., list]


def dispatching_chooser(auto: Chooser, overrides: Mapping[str, Callback]) -> Chooser:
    """A `choose(p, v, s, ask_budget)` for `SeasonDriver.season`: person ids in `overrides` go to
    their callback as `callback(p, v, s, ask_budget, auto)`; every other person goes to `auto`.

    `overrides` is read at each call, not copied, so a client may add or remove a person between
    seasons. With an empty mapping the returned chooser is `auto` behind one dictionary lookup."""
    def choose(p: Any, v: Any, s: Any, ask_budget: Callable[[], int]) -> list:
        cb = overrides.get(p.id)
        if cb is None:
            return auto(p, v, s, ask_budget)
        return cb(p, v, s, ask_budget, auto)
    return choose


def carry_on(w: Any, overrides: MutableMapping[str, Callback], pid: str, last: Sequence,
             pick: Callable[[Sequence], Any]) -> tuple:
    """CP-T02-06, THE RE-BIND: called by the client BETWEEN SEASONS for the seated person `pid`, with `last`
    the reading it took the season before (`()` at the first call). Returns `(pid_now, reading)`: the person
    the callback is bound to (`None` once the line is extinct) and `world_q.continuations`' reading of him.

      * `pid` lives: the reading is refreshed and nothing is rebound. A season with no death is the shipped
        run (`overrides` is not touched).
      * `pid` is dead: the OFFER is `last` filtered to those still in `w.persons`, in the order the Query gave
        it, which is `rosters.yaml: continuation_ties` order. `pick(offer)` is the PLAYER's choice (a
        `Continuation` of the offer); `overrides[pid]` is moved to him. An empty offer is the line extinct,
        exactly as an empty last reading: the callback is dropped and `(None, ())` returned.

    ⚠ THE CLIENT HOLDS NO ROSTER: which persons may be chosen, and in what order, is `world_q.continuations`'
    answer (a game fact); this only filters it to the living and binds. A choice outside the offer is
    REFUSED, not coerced. [ASSUMPTION; medium; Jordan to correct; revert: bind to `offer[0]` without calling
    `pick`.] Writes nothing to the world; `overrides` is read at each call by `dispatching_chooser`, so the
    rebind is seen by the next season's DELIBERATE."""
    if pid in w.persons:
        return pid, continuations(w, w.persons[pid])
    offer = tuple(c for c in last if c.person in w.persons)
    if not offer:
        overrides.pop(pid, None)
        return None, ()
    chosen = pick(offer)
    if chosen not in offer:
        # REFUSED before anything moves: the callback stays bound to `pid`, so a caller that catches this and asks again
        # still has the player's binding to move
        raise Forbidden(f"{chosen!r} is not in the offer {list(offer)!r}", "harness/play_surface.py::carry_on",
                        needs="a member of the offer, in `continuation_ties` order",
                        law="CP-T02-06 -- the client binds to one of the living ties the Query offered, no other")
    callback = overrides.pop(pid, None)
    if callback is not None:
        overrides[chosen.person] = callback
    return chosen.person, continuations(w, w.persons[chosen.person])


def has_continuation(w: Any, pid: Optional[str]) -> bool:
    """THE TRANSCRIPT'S STOP TEST (B34.19, `U5a_CORE_owed_edits` §F rules 1-2): does the seated person `pid` have a living continuation, `world_q.continuations`' answer and no
    roster of this file's own? `False` for `None` (his line is extinct) and for a person the world no longer holds. The scenario rows that name a realm ending
    (`scenarios.season_ending`, `life_ending`) end the run on it only where this is `False`; with a continuation the run plays on and the ending stays in `endings_reached`.
    Reads `w`, writes nothing."""
    return pid in w.persons and bool(continuations(w, w.persons[pid]))


def holdings_of(w: Any) -> Callable[[str], tuple]:
    """THE HOST'S READER for `decision/sheet.py::creation_sheet(persons, holdings_of)` (B34.06): person id -> `((tenure kind, object id), ...)` of his own live
    Tenures, built here from `w.tenures` because `decision/` names no `World` and `OwnStateReader` answers one object's holder and enumerates nothing (as
    `military_menu.py` reads an army host-side). The pairs are the ones `Situation.holdings` shows, in the order held. Reads `w`, writes nothing."""
    held: dict = {}
    for t in w.tenures:
        if t.live:
            held.setdefault(t.subject, []).append((t.kind, t.object))
    return lambda pid: tuple(held.get(pid, ()))


def board(p: Any, fixtures: Any) -> list:
    """THE CASE BOARD: what `p` holds, laid out for a player to read (B11.77, `IS-B2-FI-04`, `08_FI_07` §3). A PRINT, NOT A READER: `person_q.dossier` is the one owner of what a row is and
    how it is weighed (`fixtures` is the `fx` it weighs under, as clause 4 does), and this groups nothing itself. A list of dicts, in order:

      * `{"kind": "claim", "row": DossierRow}` -- one per `dossier` row, a group's rows together;
      * `{"kind": "suspects", "goal", "doers", "by"}` -- one per goal of his that is a `deed_doers` case (a live `commit` Tenure on a goal row whose `object:` names one form of
        `rosters.yaml: goal_object_kinds.forms.deed_doers` and no `against`, which names another goal's referents and is a World read): `doers` is `person_q.deed_doers` over his own
        ledger, `by` the ids of the claims that name each; `()` and `{}` until his ledger names someone;
      * `{"kind": "document", "id", "of", "about"}` -- one per `dossier` row that is the content of a document on his live `hold`: its kind and what it says (`content_said`).

    Reads `p` alone: no World, no state written, no token."""
    out: list = [{"kind": "claim", "row": row} for row in dossier(p, None, fixtures)]
    for t in p.tenures:
        goal = goals_data.goal(t.object) if t.kind == "commit" and t.live else None
        if goal is not None and goal.object["kind"] == "deed_doers" and "against" not in goal.object:
            out.append({"kind": "suspects", "goal": goal.id, "doers": deed_doers(p.ledger, goal.object, p.id),
                        "by": deed_doer_claims(p.ledger, goal.object, p.id)})
    out += [{"kind": "document", "id": x["row"].record, "of": content_kind(x["row"].claim), "about": content_said(x["row"].claim)}
            for x in out if x["kind"] == "claim" and x["row"].record is not None]
    return out


# ---------------------------------------------------------------------------------------------------
# THE TRANSCRIPT (B34.04) -- printers of what `decision/sheet.py` reads, and the command that runs a scenario through `scenarios.run`.
# ---------------------------------------------------------------------------------------------------

def account_lines(p: Any, since: tuple, known: frozenset = frozenset()) -> list:
    """The `account` of `p` since `since` without the claims whose ids are in `known`, one line a row: the claim as he holds it, whether it echoes his own deed, who told him, and
    what changed. Reads `p`'s own ledger only."""
    out = []
    for r in (r for r in account(p, since) if r.claim.id not in known):
        c = r.claim
        via = f" told by {c.teller} ({c.hops} hops)" if getattr(c, "teller", None) else ""
        out.append(f"   learned {c.subject} · {c.predicate} = {str(c.value)} · {c.source} · when {c.when}.{c.lap}{via}"
                   + (" · his own deed" if r.own else "")
                   + (f" · before: {str(r.prior.value)}" if r.prior is not None else "")
                   + (" · nobody is named as the doer" if r.unattributed else ""))
    return out


def deliberation_lines(w: Any, sheet: Any, verbs: Optional[frozenset] = None) -> list:
    """The `Situation` and the `Offer` of the seated person at one deliberation, as printed lines. `sheet` is the `DevelopmentSheet` `development_space` hands `pick`
    (its `view` and `budget` are the deliberation's own); `w` is read only to find the person's own record (`w.persons[...]`) and the `fx` and `draw` the chooser was
    built with. The offer rows are the sheet's own order (`make_ranker`'s, the picked question's occasions first when he picked a later one, B34.16), so `[i]` is the
    index a pick names."""
    p = interior_of(w.persons[sheet.person_id], w.tick, w.fixtures.claim_decay())     # what the chooser ranked (`loop/deliberate.py`): a stored `Person` reads his claims unfaded
    v = sheet.view
    s = situation(p, v, lambda: sheet.budget)
    off = offer(p, v, w.fixtures, resolvable_verbs() if verbs is None else verbs, draw_factory(w.world_seed, lambda: w.tick), sheet.asked_index)
    lines = [f"   situation · body {s.body} · budget {s.budget} · holds {list(s.holdings)} · pursuits {dict(s.pursuits)} · stance {list(s.stance)}"]
    for a in s.asked:
        lines.append(f"   asked {a.question.id} · {a.question.source} · about {a.question.about}"
                     + (f" · his claim: {a.claim.predicate} = {str(a.claim.value)}" if a.claim is not None else "")
                     + (" · asked for" if a is s.asked[sheet.asked_index] and sheet.asked_index > 0 else ""))
    for i, r in enumerate(off.rows):
        c = r.candidate
        terms = " ".join(f"{n} {t:+.2f}" for n, t in zip(TERM_NAMES, r.terms))
        said = " ".join(f"{k}={x}" for k, x in sorted(c.operands.items()) if isinstance(x, str) and k != "via")      # the string operands: `to=` tells two rows of one verb and subject apart
        seat = seat_of(p, c)                                                                                          # and the seat the act is exercised through (`Act.via`)
        lines.append(f"   [{i}] " + " ".join(x for x in (c.verb, c.subject or "", said, f"through {seat}" if seat else "") if x)
                     + (f" · for {r.occasion}" if r.occasion else "") + f" · {terms}"
                     + (f" · believes {r.odds:.2f}" if r.odds is not None else "") + f" · cost {r.cost}")
    for x in off.withheld:
        lines.append(f"   withheld {x.verb} {x.subject if x.subject is not None else ''}".rstrip() + f" · unmet {x.unmet}")
    return lines


def faction_line(w: Any, pid: Optional[str]) -> Optional[str]:
    """THE HOST'S LINE (resolver-side, never his belief): where the faction `pid` coheres under stands at the realm rung, `faction_q.standing`'s record and no reading of
    this file's own. `None` for a person the world no longer holds or a world with no realm rung."""
    from .governance_spine import _top_rung            # lazy: governance_spine imports this module
    top = _top_rung(w)
    if top is None or pid not in w.persons:
        return None
    prop = world_q.faction_of(w, pid)
    if prop is None:
        return f"host (resolver-side, not his belief) · {pid} coheres under no single faction"
    s = faction_q.standing(w, prop, top)
    return (f"host (resolver-side, not his belief) · faction {prop}: footprint {len(s.footprint)} rungs, {s.present} of {s.persons} present, "
            f"largest holder's share {s.sovereign_share:.2f}, {len(s.provinces)} provinces")


def transcript(name: str, seed: int, seasons: int, person: Optional[str] = None, out: Callable[[str], None] = print,
               ask: Optional[Callable[[Any], int]] = None) -> dict:
    """Play `scenarios.SCENARIOS[name]` through `scenarios.run` with `person` seated on `take_ranked`, printing each deliberation (`deliberation_lines`), the pick, the
    `account` since his last deliberation, and once a season the host's faction line. `ask(situation) -> int` is his pick of one of the questions asked of him
    (`development_space`'s), the first where `None`. Prints `content_hash` and, last, `ENDING <name> <kind>` where the run ended on one (B34.20, `IS-B3-GO-02`: the kind is the row's `kinds`, from the seat's side; before it,
    his `chronicle` and his whole `account`, and nothing of the antecedents `endings_reached` computes, which stay host-side until `reveal`, B38).
    THE STOPS (B34.19, `U5a_CORE_owed_edits` §F): the run's own, read through `scenarios.run`'s `ending`: a reached realm ending stops it only where the seat has no continuation
    (`has_continuation`; with one the ending is recorded, printed as `realm ending reached`, and the run plays on); a dead seat with no continuation stops it (`line_extinct`),
    with one the line says `re-seated`; and `seasons` stops it. No reveal is printed (B38). Returns `scenarios.run`'s dict, with `recorded`, the realm endings reached. Nothing here writes the world: the readers are `decision/sheet.py`'s."""
    from . import scenarios as SC                      # lazy: scenarios imports this module
    from ..decision.sheet import take_ranked
    row = SC.SCENARIOS[name]
    built: list = []
    last: dict = {}                                    # person id -> the ids of the claims he held at his last deliberation
    state = {"n": 0, "tick": None, "seat": None}
    recorded: list = []                                # the realm endings reached while the run went on (`endings_reached`'s ids, in the order first seen)

    def note_endings(w: Any, pid: Optional[str]) -> None:
        for e in world_q.endings_reached(w):
            if e.ending not in recorded:
                recorded.append(e.ending)
                out(f"   realm ending reached: {e.ending}" + (" · he has a continuation" if has_continuation(w, pid) else " · he has none"))

    def host_line(pid: Optional[str]) -> None:
        text = faction_line(built[0], pid)
        if text is not None:
            out(f"   {text}")

    def learned(pid: Optional[str]) -> None:
        w = built[0]
        if pid in last and pid in w.persons:
            rows = account_lines(w.persons[pid], (), last[pid])
            out(f"   he has learned {len(rows)} thing(s) since his last deliberation")
            for line in rows:
                out(line)

    def pick(sheet):
        w = built[0]
        state["n"] += 1
        pid = sheet.person_id
        was = state["seat"] or (person if person is not None else row.seat(w))   # the one he was, where he never deliberated before dying
        if pid != was:
            out(f"-- re-seated: {was} is dead, the line continues under {pid}")
        out(f"-- deliberation {state['n']} · tick {w.tick} · {pid}")
        learned(pid)
        if state["tick"] != w.tick:
            host_line(pid)
            note_endings(w, pid)
            state["tick"] = w.tick
        for line in deliberation_lines(w, sheet, row.verbs):
            out(line)
        chosen = list(take_ranked(sheet))
        out(f"   pick {chosen}")
        # What he holds now is what he knew when he chose; the next `account` is the claims he holds then that he did not hold now. (A claim carries the stamp of the lap it
        # landed in, and WITNESS runs after DELIBERATE, so no `since` stamp read here can tell the lap just played from the ones before: the driver's `(tick, lap)` is a local, D-21.)
        last[pid] = frozenset(c.id for c in w.persons[pid].ledger)
        state["seat"] = pid
        return chosen

    r = SC.run(name, seed, seasons, pick=pick, person=person, on_build=built.append, ask=ask)
    w = built[0]
    note_endings(w, r["seat"])                         # an ending reached after his last deliberation is the one the run stopped on
    r["recorded"] = recorded
    if r["seat"] is not None and r["seat"] == state["seat"]:
        out("-- the run ended")
        learned(r["seat"])
        host_line(r["seat"])
    if r["ending"] is not None and r["seat"] in w.persons:      # AT AN ENDING (B34.20, `IS-B3-GO-02` (3)) his own chronicle and his whole account, and nothing of the world's truth
        held = w.persons[r["seat"]]
        c = chronicle(held, w.fixtures)
        out(f"-- the ending · {held.id} · chronicle {len(c.ledger)} claim(s) on {len(c.beliefs)} subject(s), {len(c.threads)} thread(s) · conviction {dict(c.conviction)}"
            f" · scar {dict(c.scar_pursuits)} · held {dict(c.scar_affiliations_held)} · history {dict(c.scar_affiliations_history)}")
        for line in account_lines(held, ()):
            out(line)
    out(f"{name} · seed {seed} · {r['seasons']} season(s) · tick {r['tick']} · seat {' > '.join(r['passed'])}")
    out(f"content_hash {r['hash']}")
    if r["ending"] is not None:                        # the last line, where the run ended on one (the batch gate reads it so)
        out(f"ENDING {r['ending']} {r['kind']}")
    return r


def _parse(argv: Sequence[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(prog="python -m engine.season.harness.play_surface", description=__doc__.split("\n\n")[0])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--person", help="the seated person's id (default: the scenario's own seat; the realm has none, so it prints its creation sheet)")
    ap.add_argument("--seasons", type=int, default=1)
    ap.add_argument("--question", type=int, default=0, help="which of the questions asked of him he answers (an index in attention order; 0, the default, is the shipped ranking)")
    ap.add_argument("--scenario", default="life", help="a name in `scenarios.SCENARIOS` (default `life`: the realm as built)")
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    a = _parse(sys.argv[1:] if argv is None else argv)
    from . import scenarios as SC                      # lazy: scenarios imports this module
    if a.scenario not in SC.SCENARIOS:
        raise SystemExit(f"no scenario {a.scenario!r}; registered: {sorted(SC.SCENARIOS)}")
    row = SC.SCENARIOS[a.scenario]
    if row.seat is None and a.person is None:          # no default seat: the creation sheet is the pick list, and the run does not start
        print(f"{a.scenario} has no default seat; pass --person with one of:")
        w = row.build(a.seed)
        for c in creation_sheet(w.persons.values(), holdings_of(w)):
            print(f"   {c.id} · {c.name} · holds {list(c.holdings)} · pursuits {dict(c.pursuits)}")
        return 2
    transcript(a.scenario, a.seed, a.seasons, a.person, ask=None if a.question == 0 else (lambda s: min(a.question, len(s.asked) - 1)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
