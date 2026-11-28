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


def _hold(pid, e, w, n, found=None):
    """`pid` holds a claim of `e`, deposited as WITNESS deposits one: the event-kind claim in his ledger and the
    `claim.deposited` Event naming it, caused by `e` (`loop/witness.py::_deposit`); `found`: the finding Event's id; as a FINDING deposits it (ED-FI-0002,
    `_deposit(..., also=(f.id,))`), an earlier Event first (the finding) and the uncovered Event `e` second."""
    cid = f"c_cr89_{n}"
    w.persons[pid].ledger.append(Claim(cid, pid, CLERIC, e.kind, True, e.emitted_at, "firsthand", 100, "own"))
    w.log.append(Event(f"ev_dep_cr89_{n}", "claim.deposited", [apparatus_receipt(w, cid, "set", "Event", "claim_ledger")],
                       [found, e.id] if found else [e.id], e.emitted_at))


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
    """Four Church seizures in the log; `HEARER` holds claims of two of them, one of the two by two claims, and of a third as a FOUND claim
    (the finding Event caused the deposit first, the seizure second). The world reads Turmoil 4; he believes 3 -- each Event once, a found
    claim counted, and none he holds no claim of."""
    w = build_realm(0)
    evs = [_plant(w, i, "rung.seized", changed=()) for i in range(4)]
    _hold(HEARER, evs[0], w, 0)
    _hold(HEARER, evs[1], w, 1)
    _hold(HEARER, evs[1], w, 2)
    _hold(HEARER, evs[2], w, 3, found=_plant(w, 9, "claim.deposited", act=False, changed=()).id)
    assert Q.clock(w, TURMOIL) == 4
    of_claim = Q.clock_events_by_claim(w)
    assert believed_clock(w.persons[HEARER], TURMOIL, of_claim) == 3
    assert believed_clock(w.persons[HEARER], CI, of_claim) == 31
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


# v12 B21d.06 (CR-89 commit (3); A-47, A-103): EACH BAND'S TRIGGER, ONE `Fixtures` SWITCH EACH, SHIPPED OFF. On, a trigger reads the band off the person's OWN
# believed fold, never the true clock, through a term that already exists; off, it reads nothing. The beliefs are planted as B21d.02's tests plant them: act-caused
# feeder Events and the claims WITNESS would deposit of them. `office.established` by a Church member feeds CI alone (at most 5 a season, the cap); `march.declared`
# feeds Turmoil alone (uncapped). Nothing here runs a season.
import pytest

from engine.season.data import goals as goals_data
from engine.season.data.fixtures import CLOCK_TRIGGERS, DEFAULT_FIXTURES
from engine.season.decision.choose import deliberation_memo, score_terms, stance_term
from engine.season.decision.options import seat_of
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.data.matrix import WriteClass
from engine.season.seam.wrappers import sigma
from engine.season.state.carriers import Candidate, Question
from engine.dice_engine.fmath import ltr_sum
from engine.season.data.pursuits import _AXES

from .test_in53_vacancy_need import _formed

REALM = "r_valoria"             # the realm's rung, where `nation_functions` convenes
_N = iter(range(10_000, 99_999))


def _fx(*on):
    fx = DEFAULT_FIXTURES
    for name in on:
        fx = fx.sweep(name, True)
    return fx


def _believe(w, pid, name, value):
    """Make `pid` believe the clock `name` at `value` from its start, by act-caused feeder Events he holds a claim of: CI by `office.established` of a Church member,
    five a season (the cap), Turmoil by `march.declared`, all in one season."""
    start = clocks()[name].start
    kind = "office.established" if name == CI else "march.declared"
    for i in range(int(value - start)):
        n = next(_N)
        e = _plant(w, n, kind, verb="establish", tick=(i // 5 if name == CI else 0))
        _hold(pid, e, w, n)


def _break_down(w, pid):
    """`pid` believes breakdown: Turmoil at the crisis band (5 marches + 2 failed sittings' `matter.undetermined`) and two failed sittings of `ROW`."""
    for e in [_plant(w, n, "march.declared") for n in [next(_N) for _ in range(5)]] + [_sit(w, next(_N), ["matter.undetermined"])[0] for _ in range(2)]:
        _hold(pid, e, w, next(_N))


def _head(w, faction):
    return Q.head(w, faction)


def _check_ci_pursuit_gain_on():
    """CI >= assertive: a Church member's `seize` scores more in the `pursuit` term by the row read as aligned one step on every axis he weighs
    (`damp * Σ|axis_w|`, his term's own unit); a non-Church man's does not move."""
    read = {}
    for on in (False, True):
        for pid in (CLERIC, KING):
            w = build_realm(0, fixtures=_fx(*(["ci_pursuit_gain_on"] if on else [])))
            _believe(w, pid, CI, 40)
            me, q = w.persons[pid], Q.questions_for(w, w.persons[pid])[0]
            memo = deliberation_memo(me, w.fixtures)
            unit = memo[("damp",)] * ltr_sum(abs(memo[("axis_w",)][ax]) for ax in _AXES)
            read[(on, pid)] = (score_terms(me, Candidate("seize", "terr_T1"), w.fixtures, memo, None, q)[0], unit)
    assert read[(True, CLERIC)][1] > 0
    assert read[(True, CLERIC)][0] == read[(False, CLERIC)][0] + read[(True, CLERIC)][1], read
    assert read[(True, KING)][0] == read[(False, KING)][0], "a man not of the Church gained"


def _check_ci_mu_shift_on():
    """CI >= reach: the Church member's social roll against the King takes one more named level FOR him (a larger `leverage`, the mu-shift) and the
    obstacle's terms are untouched (never an Ob reduction)."""
    read = {}
    for on in (False, True):
        w = build_realm(0, fixtures=_fx(*(["ci_mu_shift_on"] if on else [])))
        _believe(w, CLERIC, CI, 55)
        inp = sigma.contest_input(w, [CLERIC], verb="arrest", subject=KING)
        read[on] = (inp.leverage, inp.obstacle_operands)
    assert read[True][0] > read[False][0], read
    assert read[True][1] == read[False][1], "the obstacle moved: the trigger is an Ob term"


def _check_ci_theocratic_occasion_on():
    """CI >= mass seizure: the Church head's head question carries the Crown's creed and is mandatory; off, it is not marked."""
    read = {}
    for on in (False, True):
        w = build_realm(0, fixtures=_fx(*(["ci_theocratic_occasion_on"] if on else [])))
        head = _head(w, CHURCH)
        _believe(w, head, CI, 60)
        q = Q.questions_for(w, w.persons[head])[0]
        read[on] = (q.mandatory, (CROWN, "Proposition") in q.classes)
    assert read == {False: (False, False), True: (True, True)}, read


def _check_ci_church_decline_on():
    """CI >= ascendant (two bands, dominant and ascendant): the King's `fight` on a Church officer his ledger names loses two valence steps in the `stance`
    term; the Church member's own `fight` on him does not move (he is of the Church)."""
    read = {}
    for on in (False, True):
        for pid, subject in ((KING, CLERIC), (HEARER, CLERIC)):
            w = build_realm(0, fixtures=_fx(*(["ci_church_decline_on"] if on else [])))
            _believe(w, pid, CI, 80)
            me, q = w.persons[pid], Q.questions_for(w, w.persons[pid])[0]
            read[(on, pid)] = stance_term(me, Candidate("fight", subject), w.fixtures, {}, q)
    assert read[(True, KING)] == read[(False, KING)] - 2.0, read
    assert read[(True, HEARER)] == read[(False, HEARER)], "a Church member was weighed against his own Church"


def _check_turmoil_violence_relief_on():
    """Turmoil >= tension (one band of three): on a violent row whose stance term is a RESTRAINT (negative: he regards the man), the term is relieved by one
    third; a grudge's pull (positive) is CR-87's bound, untouched."""
    read = {}
    for on in (False, True):
        w = build_realm(0, fixtures=_fx(*(["turmoil_violence_relief_on"] if on else [])))
        _believe(w, KING, TURMOIL, 3)
        me, q = w.persons[KING], Q.questions_for(w, w.persons[KING])[0]
        read[on] = {s: stance_term(me, Candidate("fight", s), w.fixtures, {}, q) for s in sorted(w.persons) if s != KING}
    restrained = [s for s, t in read[False].items() if t < 0]
    pulled = [s for s, t in read[False].items() if t > 0]
    assert restrained, "no subject the King is restrained from -- the check observes nothing"
    assert all(read[True][s] == read[False][s] * (1.0 - 1 / 3) for s in restrained), [(s, read[False][s], read[True][s]) for s in restrained]
    assert all(read[True][s] == read[False][s] for s in pulled)


def _check_turmoil_vassal_war_on():
    """Believed breakdown: a vassal head's (Hafenmark's) head question carries the Crown's creed and is mandatory; the King, believing the same, is no vassal."""
    read = {}
    for on in (False, True):
        for faction in ("fac_hafenmark", CROWN, CHURCH):
            w = build_realm(0, fixtures=_fx(*(["turmoil_vassal_war_on"] if on else [])))
            head = _head(w, faction)
            _break_down(w, head)
            q = Q.questions_for(w, w.persons[head])[0]
            read[(on, faction)] = (q.mandatory, (CROWN, "Proposition") in q.classes)
    assert read[(True, "fac_hafenmark")] == (True, True) and not read[(False, "fac_hafenmark")][0], read
    assert not read[(True, CROWN)][0] and not read[(False, CROWN)][0], "the sovereign's head was occasioned against his own creed"
    assert not read[(True, CHURCH)][0], "a head sworn to no seat of the sovereign's faction is no vassal"


def _check_nation_functions_on():
    """Every head seat's holder holds a live commit to a `nation_functions` goal with the switch on (seeded at build); none with it off."""
    read = {}
    for on in (False, True):
        w = build_realm(0, fixtures=_fx(*(["nation_functions_on"] if on else [])))
        heads = {f: h for f in sorted(Q.faction_props(w)) if (h := Q.head(w, f)) is not None}
        read[on] = {h: sorted(t.object for t in w.persons[h].tenures if t.kind == "commit" and t.live
                              and (g := goals_data.goal(t.object)) is not None and g.switch == "nation_functions_on") for h in heads.values()}
    assert all(v == [] for v in read[False].values()), read[False]
    assert len(read[True]) >= 6 and all(len(v) == 1 for v in read[True].values()), read[True]


_CHECKS = {"ci_pursuit_gain_on": _check_ci_pursuit_gain_on, "ci_mu_shift_on": _check_ci_mu_shift_on,
           "ci_theocratic_occasion_on": _check_ci_theocratic_occasion_on, "ci_church_decline_on": _check_ci_church_decline_on,
           "turmoil_violence_relief_on": _check_turmoil_violence_relief_on, "turmoil_vassal_war_on": _check_turmoil_vassal_war_on,
           "nation_functions_on": _check_nation_functions_on}


@pytest.mark.parametrize("switch", CLOCK_TRIGGERS)
def test_switch_moves_its_term_only_when_on(switch):
    """Each switch, planted at its band: its term moves with the switch on and reads as it did with it off (`test_<switch>_moves_its_term_only_when_on`, the
    seven made one parametrised test: one shape, a check each). Every switch ships off."""
    assert DEFAULT_FIXTURES.get(switch) is False, f"{switch} does not ship off"
    _CHECKS[switch]()


def test_two_heads_at_war_convene_at_believed_turmoil_three_only_with_the_row_on():
    """Hafenmark's head declares war on the Crown (the shipped fold); both heads then believe Turmoil 3. With `nation_functions_on` both form `convene` at the
    realm's rung; with it off neither does; with it on at believed Turmoil 2 neither does (the row's question is raised at the tension band)."""
    read = {}
    for on, turmoil in ((False, 3), (True, 3), (True, 2)):
        w = build_realm(0, fixtures=_fx(*(["nation_functions_on"] if on else [])))
        d = SeasonDriver(w)
        duchess, king = _head(w, "fac_hafenmark"), _head(w, CROWN)
        q = Question("q:need:war", "need", (CROWN,), CROWN, classes=((CROWN, "Proposition"),))
        cand = next(c for c in _formed(w, duchess, q) if c.verb == "declare" and c.subject == CROWN)
        out = d.resolve(mint_token(w, WriteClass.ACTS), [Act("a_war", duchess, "declare", payload={"subject": CROWN}, via=seat_of(w.persons[duchess], cand))],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        w.log.extend(out)
        assert Q.at_war(w, "fac_hafenmark", CROWN), "the planted war is not live"
        for pid in (duchess, king):
            _believe(w, pid, TURMOIL, turmoil)
        read[(on, turmoil)] = {pid: any(c.verb == "convene" and c.subject == REALM for c in _formed(w, pid, Q.questions_for(w, w.persons[pid])[0]))
                               for pid in (duchess, king)}
    assert read[(True, 3)] == {pid: True for pid in read[(True, 3)]}, read
    assert not any(read[(False, 3)].values()), read
    assert not any(read[(True, 2)].values()), read


def test_a_declare_trigger_opens_a_mandatory_question_and_decides_nothing():
    """A-47: at believed breakdown with `turmoil_vassal_war_on`, the vassal head's head question is the off-arm question marked mandatory with the Crown's creed
    stamped -- nothing else about it moves; `declare` on the creed is one candidate among others he forms; forming it wrote nothing (the hash), executed no
    `declare` (no `war.declared`, no WAR Proposition)."""
    slate = {}
    for on in (False, True):
        w = build_realm(0, fixtures=_fx(*(["turmoil_vassal_war_on"] if on else [])))
        head = _head(w, "fac_hafenmark")
        _break_down(w, head)
        before, logged = w.content_hash(), len(w.log)
        qs = Q.questions_for(w, w.persons[head])
        assert w.content_hash() == before and len(w.log) == logged, "forming the question wrote something"
        assert not any(p.mood == Q.WAR_MOOD for p in w.propositions.values()) and not any(e.kind == "war.declared" for e in w.log)
        slate[on] = (qs, _formed(w, head, qs[0]))
    (off_q, off_c), (on_q, on_c) = slate[False], slate[True]
    assert on_q[0].mandatory and not off_q[0].mandatory
    assert on_q[0].id == off_q[0].id and on_q[0].referents == off_q[0].referents, "the trigger chose another question"
    assert set(on_q[0].classes) - set(off_q[0].classes) <= {(CROWN, "Proposition")}, "the trigger stamped more than the creed"
    assert (CROWN, "Proposition") in on_q[0].classes
    assert any(c.verb == "declare" and c.subject == CROWN for c in on_c), "the occasion formed no declare"
    assert len({(c.verb, c.subject) for c in on_c}) > 1, "the declare is his only act: the trigger decided it"
