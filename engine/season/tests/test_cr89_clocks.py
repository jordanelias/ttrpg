"""v12 B21d.02 (CR-89 commit (1); ED-IN-0343, ED-IN-0345): THE TWO CLOCKS AS ROWS AND ONE FOLD OF THE LOG.

A clock is a row of `rosters.yaml: tables.clocks` (loaded by `data/rosters.py::clocks`) plus one pure fold,
`queries/clock.py::clock_fold`. Nothing stores it: the STORE is `w.log`. `world_q.clock(w, name, tick)` folds the log's
Events, each attributed to its causing act's actor and his faction at the Event's tick (an Event no act caused is not
counted); `person_q.believed_clock(p, name, of_claim)` folds the same attributed Events, only those `p` holds a claim of,
each Event once however many of his claims report it (`ED-IN-0322`). The Events are planted on the built realm (seed 0)
with their causing acts, as the fold would log them; nothing here runs a season.
"""
from __future__ import annotations

from dataclasses import replace

from engine.season.boot.realm import build_realm
from engine.season.data.rosters import ENDING_HEAD, clocks
from engine.season.harness.probes import apparatus_receipt
from engine.season.queries import world_q as Q
from engine.season.queries.clock import ClockEvent, clock_fold
from engine.season.queries.person_q import believed_breakdown, believed_clock, believed_sittings_failed
from engine.season.state.carriers import Act, Claim, Event
from engine.season.state.ids import ROOT

CI, TURMOIL = "church_influence", "turmoil"
CHURCH, CROWN = "fac_church_of_solmund", "fac_valorsmark"
CLERIC = "p_npc_004"            # a Church member at build (`faction_holding`)
KING = "p_npc_020"              # the Crown's holder of `terr_T1` .. `terr_T14` at build
HEARER = "p_npc_034"            # the person whose ledger the believed fold reads


def _plant(w, n, kind, actor=CLERIC, verb="seize", subject="terr_T1", changed=(), tick=None, act=True):
    """Log one Event of `kind` as the fold would: its causing act (when `act`) in the act store and in `causes`, each id of
    `changed` a gate receipt on it. Returns the Event."""
    tick = w.tick if tick is None else tick
    causes = []
    if act:
        a = Act(f"a_cr89_{n}", actor, verb, payload={"subject": subject})
        w.acts.append(a)
        causes = [a.id]
    else:
        causes = [ROOT]
    e = Event(f"ev_cr89_{n}", kind, [apparatus_receipt(w, c, "set", "Act", "until") for c in changed], causes, tick)
    w.log.append(e)
    return e


def _hold(pid, e, w, n):
    """`pid` holds a claim of `e`, deposited as WITNESS deposits one: the event-kind claim in his ledger and the
    `claim.deposited` Event naming it, caused by `e` (`loop/witness.py::_deposit`)."""
    cid = f"c_cr89_{n}"
    w.persons[pid].ledger.append(Claim(cid, pid, CLERIC, e.kind, True, e.emitted_at, "firsthand", 100, "own"))
    w.log.append(Event(f"ev_dep_cr89_{n}", "claim.deposited", [apparatus_receipt(w, cid, "set", "Event", "claim_ledger")],
                       [e.id], e.emitted_at))


def test_a_hand_built_log_folds_to_its_known_value_and_clamps_at_cap_and_range():
    """Hand-built attributed Events folded by the shipped rows: three Church seizures in season 0 read CI start + 3; seven in
    one season read start + the season cap (5), not + 7; Turmoil fed eleven seizures across seasons reads its range's top (10)
    and stops; a season of determinations lowers it from there by exactly their count."""
    rows = clocks()
    ci, tu = rows[CI], rows[TURMOIL]
    seize = lambda t: ClockEvent(f"e{t}", t, "rung.seized", CHURCH, frozenset())
    assert clock_fold([], ci) == ci.start == 28 and clock_fold([], tu) == tu.start == 0
    assert clock_fold([seize(0)] * 3, ci) == 31
    assert clock_fold([seize(0)] * 7, ci) == 28 + ci.season_cap == 33, "the season cap did not bind"
    assert clock_fold([seize(0)] * 7 + [seize(1)] * 7, ci) == 38, "the cap is per season"
    assert clock_fold([seize(t // 4) for t in range(11)], tu) == 10, "Turmoil passed its range"
    determined = [ClockEvent(f"d{i}", 3, "matter.determined", CROWN, frozenset()) for i in range(2)]
    assert clock_fold([seize(t // 4) for t in range(11)] + determined, tu) == 8, "the clamp was not applied season by season"


def test_one_planted_church_rung_seized_raises_ci_and_turmoil_by_one_weight_once():
    """One `rung.seized` whose causing act is a Church member's, taking a Crown holder's territory: CI and Turmoil each move by
    one feeder weight (1), read twice the same; the CI feeder against the Church does not fire (the closed hold was the
    King's), and the same seizure taken FROM the Church reads CI at start (+1 -1) with Turmoil still +1."""
    w = build_realm(0)
    ci0, tu0 = Q.clock(w, CI), Q.clock(w, TURMOIL)
    assert (ci0, tu0) == (28, 0), (ci0, tu0)
    _plant(w, 1, "rung.seized", changed=("t_hold_terr_T1",))
    assert (Q.clock(w, CI), Q.clock(w, TURMOIL)) == (ci0 + 1, tu0 + 1)
    assert (Q.clock(w, CI), Q.clock(w, TURMOIL)) == (ci0 + 1, tu0 + 1), "a second read moved the clock: something was stored"
    v = build_realm(0)
    church_hold = next(t for t in v.tenures if t.kind == "hold" and t.live and Q.faction_holding(v, t.subject) == CHURCH)
    _plant(v, 2, "rung.seized", actor=KING, subject=church_hold.object, changed=(church_hold.id,))
    assert (Q.clock(v, CI), Q.clock(v, TURMOIL)) == (ci0 - 1, tu0 + 1), "the seizure from the Church did not lower CI"


def test_a_person_holding_claims_of_half_the_events_believes_half():
    """Four Church seizures in the log; `HEARER` holds claims of two of them, one of the two by two claims. The world reads
    Turmoil 4; he believes 2 -- each Event once, and none he holds no claim of."""
    w = build_realm(0)
    evs = [_plant(w, i, "rung.seized", changed=()) for i in range(4)]
    _hold(HEARER, evs[0], w, 0)
    _hold(HEARER, evs[1], w, 1)
    _hold(HEARER, evs[1], w, 2)
    assert Q.clock(w, TURMOIL) == 4
    of_claim = Q.clock_events_by_claim(w)
    assert believed_clock(w.persons[HEARER], TURMOIL, of_claim) == 2
    assert believed_clock(w.persons[HEARER], CI, of_claim) == 30
    assert believed_clock(w.persons[KING], TURMOIL, of_claim) == 0, "a man holding no claim believes the start"


def test_an_event_with_no_causing_act_is_not_counted():
    """A feeder-kind Event (`rung.seized`) whose causes name no act moves neither clock; the same Event with its act does."""
    w = build_realm(0)
    _plant(w, 1, "rung.seized", act=False)
    assert (Q.clock(w, CI), Q.clock(w, TURMOIL)) == (28, 0), "an Event no act caused was counted"
    _plant(w, 2, "rung.seized")
    assert (Q.clock(w, CI), Q.clock(w, TURMOIL)) == (29, 1), "control failed -- the act-caused Event was not counted either"


def test_every_weight_zero_reproduces_the_start_values():
    """CONTROL: the shipped rows with every feeder weight 0, folded over a planted log of every feeder kind each row names
    (each Event act-caused, by a Church member against the Crown and by the King against the Church), read the start values;
    the shipped weights over the same log do not."""
    w = build_realm(0)
    church_hold = next(t for t in w.tenures if t.kind == "hold" and t.live and Q.faction_holding(w, t.subject) == CHURCH)
    n = 0
    for row in clocks().values():
        for f in row.feeders:
            _plant(w, n, f.kind, changed=("t_hold_terr_T1",))
            _plant(w, n + 1, f.kind, actor=KING, subject=church_hold.object, changed=(church_hold.id,))
            n += 2
    events = Q.clock_events(w, w.log)
    assert len(events) == n >= 20, len(events)
    for name, row in clocks().items():
        zero = replace(row, feeders=tuple(replace(f, weight=0) for f in row.feeders))
        assert clock_fold(events, zero) == row.start, name
    assert (clock_fold(events, clocks()[CI]), clock_fold(events, clocks()[TURMOIL])) != (28, 0), "the log moves no clock at the shipped weights"


# v12 B21d.03 (CR-89 commit (2); ED-IN-0341): THE BREAKING POINT. A sitting is one act a proceeding resolved, written on every Event the act emits
# (`Event.ending`'s head names the arrangement, `loop/resolve.py::_proceeding_ending`); it disposes nothing when none of its Events is the
# determination (`data/verbs.py::DISPOSAL_EVENTS["determine"]`). `world_q.sittings_failed` counts those among an arrangement's last `window` sittings
# in the log; `person_q.believed_sittings_failed` the same over the sittings `p` holds a claim of; `person_q.believed_breakdown` is the conjunction.
ROW = "parliamentary_debate"


def _sit(w, n, kinds, arrangement=ROW, tick=None):
    """Log ONE SITTING of `arrangement` as the fold writes one: an act (`determine` by the King) and one Event per kind of `kinds`, each caused by the
    act and carrying the proceeding's head (`ENDING_HEAD`, the arrangement). Returns the Events."""
    tick = w.tick if tick is None else tick
    a = Act(f"a_sit_{n}", KING, "determine", payload={"subject": HEARER})
    w.acts.append(a)
    head = ((ENDING_HEAD, arrangement, "full", "closed", None),)
    out = [Event(f"ev_sit_{n}_{k}", k, [], [a.id], tick, ending=head) for k in kinds]
    w.log.extend(out)
    return out


def test_three_planted_sittings_that_dispose_nothing_read_three_and_one_determination_makes_two():
    """Three sittings of one arrangement, each ending `matter.undetermined`, read 3 of the last 3; a `matter.determined` in the second sitting makes it
    2; a sitting of another arrangement and an Event with no proceeding move neither; a fourth sitting that determined pushes the first out of the window
    (1). The person twin: `HEARER` holding claims of sittings 1 and 3 believes 2, of 1 only believes 1, and a man holding none believes 0."""
    w = build_realm(0)
    assert Q.sittings_failed(w, ROW, 3) == 0, "a built realm with no sitting read a failed one"
    s1, s2, s3 = (_sit(w, i, ["matter.undetermined"]) for i in range(3))
    _sit(w, 9, ["matter.undetermined"], arrangement="council_of_state")
    _plant(w, 9, "matter.undetermined")                       # act-caused, but no proceeding wrote it: no sitting
    assert Q.sittings_failed(w, ROW, 3) == 3
    w.log.append(Event("ev_sit_1_det", "matter.determined", [], list(s2[0].causes), w.tick, ending=s2[0].ending))
    assert Q.sittings_failed(w, ROW, 3) == 2, "a determination in the sitting did not dispose of it"
    assert Q.sittings_failed(w, "council_of_state", 3) == 1
    _sit(w, 4, ["matter.determined"], tick=w.tick + 1)
    assert Q.sittings_failed(w, ROW, 3) == 1, "the window did not drop the oldest sitting"
    assert Q.sittings_failed(w, ROW, 4) == 2
    _hold(HEARER, s1[0], w, 10)
    _hold(HEARER, s3[0], w, 11)
    _hold(CLERIC, s1[0], w, 12)
    of_claim = Q.sitting_events_by_claim(w)
    assert believed_sittings_failed(w.persons[HEARER], ROW, 3, of_claim) == 2
    assert believed_sittings_failed(w.persons[CLERIC], ROW, 3, of_claim) == 1
    assert believed_sittings_failed(w.persons[KING], ROW, 3, of_claim) == 0, "a man holding no claim believes a failed sitting"


def test_breakdown_needs_both_believed_turmoil_and_failed_sittings():
    """Believed breakdown is believed Turmoil at the crisis band (7) AND two failed sittings of the last three he knows of. The failed sittings'
    `matter.undetermined` feed Turmoil too (one log). `HEARER`: 5 seizures + 2 failed sittings = Turmoil 7, 2 failed -> broken. `CLERIC`: 7 seizures + 1
    failed sitting = Turmoil 8, 1 failed -> not. `KING`: 4 seizures + 2 failed sittings = Turmoil 6, 2 failed -> not. Nothing is stored: the world reads
    the same before and after asking."""
    w = build_realm(0)
    fx = w.fixtures
    assert (fx.get("breakdown_sittings"), fx.get("breakdown_window"), fx.get("turmoil_crisis")) == (2, 3, 7)
    seized = [_plant(w, 100 + i, "rung.seized") for i in range(7)]
    failed = [_sit(w, 200 + i, ["matter.undetermined"])[0] for i in range(2)]
    n = iter(range(300, 400))
    for pid, seen in ((HEARER, seized[:5] + failed), (CLERIC, seized + failed[:1]), (KING, seized[:4] + failed)):
        for e in seen:
            _hold(pid, e, w, next(n))
    of_clock, of_sitting = Q.clock_events_by_claim(w), Q.sitting_events_by_claim(w)
    read = {pid: (believed_clock(w.persons[pid], TURMOIL, of_clock), believed_sittings_failed(w.persons[pid], ROW, 3, of_sitting))
            for pid in (HEARER, CLERIC, KING)}
    assert read == {HEARER: (7, 2), CLERIC: (8, 1), KING: (6, 2)}, read
    before = w.content_hash()
    broken = {pid: believed_breakdown(w.persons[pid], ROW, of_clock, of_sitting, fx) for pid in (HEARER, CLERIC, KING)}
    assert broken == {HEARER: True, CLERIC: False, KING: False}, broken
    assert w.content_hash() == before, "asking for breakdown wrote something"
