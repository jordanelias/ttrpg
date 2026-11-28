"""Hand-built governance scaffolding the seat tests share (B21c: `test_cr32_ladders`, `test_cr34_declared_disposal`, `test_cr35_election`,
`test_cr36_nomination`, `test_cr37_deposition`). A helper, no tests: each function writes or reads the world exactly as the copies it
replaced did, so no assertion moves with it.
"""
from __future__ import annotations

from engine.season.state.carriers import Office, Proposition, Tenure


def seat(w, sid, post, rung, remit, holder, tenure=None, **office):
    """Build Office `sid` (scope `rung`; `office` its other fields) and, where `holder` is not `None`, his live `hold` on it (`tenure` its id,
    else `t_seat_<sid>`)."""
    off = Office(sid, post, rung, list(remit), **office)
    off.scope_rung = rung
    w.offices[sid] = off
    if holder is not None:
        w.add_tenure(Tenure(tenure or f"t_seat_{sid}", holder, sid, "hold", since=0))


def vacate(w, sid):
    """End every `hold` on `sid` at tick 0 (the tiny world's Duke's seat, cleared before a test builds its own seats)."""
    for t in list(w.tenures):
        if t.kind == "hold" and t.object == sid:
            t.until = 0


def holders(w, obj):
    """The subjects of the live `hold`s on `obj`, in store order."""
    return [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == obj]


def give_by_hand(w, rid, to):
    """H-229's residue: the resolution's one live `hold` closes and the receiver's opens -- `give`'s two edges, written by hand."""
    held, = [t for t in w.tenures if t.kind == "hold" and t.live and t.object == rid]
    held.until = w.tick
    w.add_tenure(Tenure(f"t_given_{rid}_{to}", to, rid, "hold", since=w.tick))


def commit(w, who, obj, key=None, until=None):
    """`who`'s `commit` to `obj` from tick 0 (`key` its id, else `cm_<who>_<obj>`)."""
    w.add_tenure(Tenure(key or f"cm_{who}_{obj}", who, obj, "commit", since=0, until=until))


def ought(w, who, pid, subject, predicate, mood="OUGHT", until=None, key=None):
    """`who` commits to Proposition `pid` (minted as `mood` about `subject` naming `predicate`, true, if absent)."""
    if pid not in w.propositions:
        w.propositions[pid] = Proposition(pid, mood, subject, predicate, True, 0)
    commit(w, who, pid, key=key, until=until)
