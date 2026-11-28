"""v12 B21d.04 (CR-90): THE CLOCK-MARKS INSTRUMENT -- `harness/clocks.py` reads, per seed, the FIRST season of each mark an arc runs through (each clock band
crossed, breakdown, the first claim, `declare`, civil war, the Church's `declare`, Church `rung.seized`) and whether parliament still determines a matter after
the first war. It reads the log and the world and writes nothing. The Events are planted on the built realm (seed 0) with their causing acts, as
`test_cr89_clocks.py` plants them; no season is run here, so a season is `emitted_at - t0 + 1` against the tick the reading starts at.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data.rosters import ENDING_HEAD, clocks
from engine.season.harness import clocks as K
from engine.season.harness.probes import apparatus_receipt
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act, Claim, Event, Proposition

CHURCH, CROWN = "fac_church_of_solmund", "fac_valorsmark"
CLERIC = "p_npc_004"            # a Church member at build (`faction_holding`)
KING = "p_npc_020"              # the Crown's head at build (`world_q.head`)
CHURCH_HEAD = "p_npc_021"       # the Church's head at build
ROW = K.determining_arrangement()


def _plant(w, n, kind, tick, actor=KING, verb="seize"):
    """Log one act-caused Event of `kind` at `tick`, as the fold would."""
    a = Act(f"a_cr90_{n}", actor, verb, payload={"subject": "terr_T1"})
    w.acts.append(a)
    e = Event(f"ev_cr90_{n}", kind, [], [a.id], tick)
    w.log.append(e)
    return e


def _sit(w, n, kind, tick):
    """One sitting of `ROW` that wrote one Event of `kind` (a determination when `kind` is `matter.determined`)."""
    a = Act(f"a_sit90_{n}", KING, "determine", payload={"subject": CLERIC})
    w.acts.append(a)
    e = Event(f"ev_sit90_{n}", kind, [], [a.id], tick, ending=((ENDING_HEAD, ROW, "full", "closed", None),))
    w.log.append(e)
    return e


def _hold(pid, e, w, n):
    """`pid` holds a claim of `e`, deposited as WITNESS deposits one (`test_cr89_clocks._hold`)."""
    cid = f"c_cr90_{n}"
    w.persons[pid].ledger.append(Claim(cid, pid, CLERIC, e.kind, True, e.emitted_at, "firsthand", 100, "own"))
    w.log.append(Event(f"ev_dep90_{n}", "claim.deposited", [apparatus_receipt(w, cid, "set", "Event", "claim_ledger")], [e.id], e.emitted_at))


def _arc(w):
    """A planted three-season arc from tick `t0 = w.tick`. Season 1: five Church seizures. Season 2: five more, two failed sittings of `ROW`, a claim to a
    territory, and a Crown `declare`. Season 3: a Church `declare`, then a determination of `ROW` (parliament still determines after the war), and five more
    Church seizures. Returns `(t0, {name: its events})`."""
    t0, n = w.tick, iter(range(1000))
    ev = {"seize1": [_plant(w, next(n), "rung.seized", t0, CLERIC) for _ in range(5)]}
    ev["seize2"] = [_plant(w, next(n), "rung.seized", t0 + 1, CLERIC) for _ in range(5)]
    ev["failed"] = [_sit(w, next(n), "matter.undetermined", t0 + 1) for _ in range(2)]
    w.propositions["claim:fac_valorsmark:terr_T1"] = Proposition("claim:fac_valorsmark:terr_T1", Q.CLAIM_MOOD, CROWN, "claims", "terr_T1", t0 + 1)
    ev["crown_war"] = [_plant(w, next(n), "war.declared", t0 + 1, KING, "declare")]
    ev["church_war"] = [_plant(w, next(n), "war.declared", t0 + 2, CLERIC, "declare")]
    ev["decided"] = [_sit(w, next(n), "matter.determined", t0 + 2)]
    ev["seize3"] = [_plant(w, next(n), "rung.seized", t0 + 2, CLERIC) for _ in range(5)]
    return t0, ev


def test_the_reader_moves_no_hash():
    """Reading a world with an arc planted on it leaves its content hash as it was, and the reading read something (a mark reached)."""
    w = build_realm(0)
    t0, _ = _arc(w)
    before = w.content_hash()
    r = K.read_world(w, t0, 3)
    assert sum(v is not None for v in r.marks.values()) >= 8, r.marks
    assert w.content_hash() == before, "the reader wrote to the world"
