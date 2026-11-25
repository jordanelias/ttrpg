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
"""
from __future__ import annotations

from typing import Any, Callable, MutableMapping, Mapping, Sequence

from ..data import goals as goals_data
from ..gaps import Forbidden
from ..queries.person_q import content_kind, content_said, deed_doer_claims, deed_doers, dossier
from ..queries.world_q import continuations

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
