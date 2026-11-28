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
from engine.season.queries import person_q, world_q as Q
from engine.season.state.carriers import Act, Claim, Event, Proposition
from engine.season.state.ids import ROOT

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


def test_a_planted_log_reads_its_known_seasons():
    """The planted arc reads: Church Influence start 28 and cap 5 a season is 33, 38, 43, so `assertive` (40) is season 3 and `reach` (55) never; Turmoil
    (uncapped, range 10) is 5 after season 1, so `tension` (3) is season 1, and `crisis` (7) and `collapse` (9) are season 2; breakdown (Turmoil at crisis and
    two failed of the last three sittings) is season 2; the claim 2, `declare` 2, the Church's `declare` 3, Church `rung.seized` 1, parliament determines after
    the war. A head holding claims of the season-1 Events only believes Turmoil 5 and no more; one holding every claim believes what is true. Civil war is a
    live reading of the world, so it is read after each season: a stubbed step and reader read the first season it holds."""
    w = build_realm(0)
    t0, ev = _arc(w)
    held = {KING: [e for k in ("seize1", "seize2", "failed") for e in ev[k]], CHURCH_HEAD: ev["seize1"]}
    for i, (pid, events) in enumerate(held.items()):
        for j, e in enumerate(events):
            _hold(pid, e, w, 100 * i + j)
    r = K.read_world(w, t0, 3)
    want = {"church_influence:assertive": 3, "church_influence:reach": None, "turmoil:tension": 1, "turmoil:crisis": 2, "turmoil:collapse": 2,
            "breakdown": 2, "claim": 2, "declare": 2, "theocratic declare": 3, "church rung.seized": 1}
    assert {k: r.marks[k] for k in want} == want, r.marks
    assert r.parliament_after_war is True
    assert r.believed[CROWN]["turmoil:crisis"] == 2 and r.believed[CROWN]["breakdown"] == 2, r.believed[CROWN]
    assert r.believed[CHURCH]["turmoil:tension"] == 1 and r.believed[CHURCH]["turmoil:crisis"] is None, r.believed[CHURCH]
    assert r.believed[CHURCH]["breakdown"] is None
    # the seed's last two seasons shorten: the same log read at two seasons never reaches season 3's mark
    assert K.read_world(w, t0, 2).marks["theocratic declare"] is None
    # civil war: read after each season; the stubbed reader holds from season 2
    flags, steps = iter([False, True, True]), []
    first = K.observe(w, 0, 3, step=lambda k, s, w=None: steps.append(k), civil_now=lambda w: next(flags))
    assert (first, steps) == (2, [1, 1, 1])


def test_feeder_weights_zero_read_never_on_every_clock_mark(monkeypatch):
    """CONTROL: the same planted arc read with every feeder weight 0 (the rows `world_q.clock` and `person_q.believed_clock` read) reaches no band of any clock,
    true or believed, and so no breakdown; the shipped weights over the same log reach them (the arc above)."""
    from dataclasses import replace
    zero = {n: replace(r, feeders=tuple(replace(f, weight=0) for f in r.feeders)) for n, r in clocks().items()}
    w = build_realm(0)
    t0, ev = _arc(w)
    for j, e in enumerate(ev["seize1"] + ev["seize2"] + ev["failed"]):
        _hold(KING, e, w, j)
    shipped = K.read_world(w, t0, 3)
    assert shipped.marks["church_influence:assertive"] == 3 and shipped.believed[CROWN]["turmoil:crisis"] == 2, "control: the shipped weights reach no band"
    monkeypatch.setattr(Q, "clock_rows", lambda: zero)
    monkeypatch.setattr(person_q, "clocks", lambda: zero)
    r = K.read_world(w, t0, 3)
    bands = [k for k in r.marks if k.split(":")[0] in zero]
    assert len(bands) == 8 and all(r.marks[k] is None for k in bands + ["breakdown"]), r.marks
    assert all(v is None for b in r.believed.values() for k, v in b.items()), r.believed


def test_the_reader_moves_no_hash():
    """Reading a world with an arc planted on it leaves its content hash as it was, and the reading read something (a mark reached)."""
    w = build_realm(0)
    t0, _ = _arc(w)
    before = w.content_hash()
    r = K.read_world(w, t0, 3)
    assert sum(v is not None for v in r.marks.values()) >= 8, r.marks
    assert w.content_hash() == before, "the reader wrote to the world"
