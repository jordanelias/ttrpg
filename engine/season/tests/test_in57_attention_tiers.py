"""v9 IN-57 (RS-22, A-26) -- `world_q.attention_key`: the order a person answers his questions in is
a tiered read of his own state (0 a claim about an ambition's subject, 1 own tenure or seat purview,
2 a deed claim with nonzero valence under his pursuits, by -|valence|, 3 the standing `need`
question, 4 the rest -- and every claim whose `doer` is the asker, the echo of his own act),
`(order[source], q.id)` the final tiebreak.

What each test proves, and the failure it can observe:

  (a) `test_an_ambition_about_x_is_answered_before_a_hash_earlier_claim_about_y` -- the entry's
      first falsifier. A control asserts the OLD key would have answered Y first, so the test is
      not vacuous; reverting the key reddens it.
  (a2) `test_a_person_whose_only_question_is_need_answers_it` and
      `test_a_tier_1_claim_precedes_the_need_question` -- the `need` question is PLAN `W5`'s
      quiet-season fallback: answered when nothing salient landed, after a salient claim when one
      did. The entry's tier 0 (need first) reddens the second.
  (a3) `test_a_claim_recording_his_own_act_ranks_after_a_foreign_occasioned_claim` -- arm C's
      falsifier: a claim whose `doer` is the asker (his only tier-0 candidate) sorts after a
      foreign-occasioned tier-1 claim and the `need` question; a control asserts it is first with
      `doer` cleared. `test_witness_stamps_doer_exactly_on_the_holders_own_acts` is the stamp's
      own falsifier over a live season (disable the stamp and it reddens).
  (b) `test_the_five_tiers_order_against_the_old_key` -- one person holding a question in every
      tier, ids chosen so the old key orders them otherwise; tier 2 by -|valence|.
  (c) `test_the_same_question_keys_differently_for_two_persons_with_different_state` and
      `test_one_person_keys_alike_under_worlds_differing_only_outside_his_own_state` -- the entry's
      second falsifier. A key that reads the log, another person or the store's size reddens (c2).
  (d) `test_reach_composes_on_own_purview` -- the rule lives once: `reach` is `{p.id}` | the ladder
      | `own_purview`, over every realm person.
  (e) `test_seed_0_season_1_each_person_answers_a_tier_0_or_1_question_first_where_he_has_one` --
      the EXIT line under these tiers, over every `questions_for` call DELIBERATE receives in the
      first season of `build_realm(0)`; it asserts it asserted.
"""
from __future__ import annotations

import copy
import dataclasses

import pytest

from ..data import verbs as V
from ..data.pursuits import to_axes
from ..data.rosters import QUESTION_SOURCES
from ..harness import populated as POP
from ..loop import driver as DRV
from ..queries import world_q
from ..queries.person_q import deed_valence
from ..state.carriers import (Claim, Event, Person, Proposition, Question, StateChange,
                              Tenure)
from ..state.containment import home_of, parent_of
from ..state.attribution import causing_act
from ..state.ids import ROOT
from ..state.world import World

ORDER = {s: i for i, s in enumerate(QUESTION_SOURCES)}
PURSUITS = {"community": 3}
NEED_TIER = 3


def old_key(q: Question) -> tuple:
    """The key before IN-57 -- the control every ordering test compares against."""
    return (ORDER[q.source], q.id)


def _claim(cid, holder, subject, predicate="exists:Person", value=1):
    return Claim(cid, holder, subject, predicate, value, 0, "firsthand", 100, "own")


def _deed_kinds(pursuits) -> tuple:
    """Two deed kinds with nonzero valence under `pursuits`, the smaller |valence| first, read off
    the shipped alignment table rather than written here."""
    ax = to_axes(pursuits)
    scored = sorted((abs(deed_valence(ax, _claim("c", "p", "p", k, True))), k)
                    for k in sorted(V.DEED_KINDS))
    nonzero = [(v, k) for v, k in scored if v]
    assert len(nonzero) >= 2 and nonzero[0][0] < nonzero[-1][0]
    return nonzero[0][1], nonzero[-1][1]


def _world_with(p: Person, props=()) -> World:
    w = World(0)
    for pr in props:
        w.propositions[pr.id] = pr
    w.persons[p.id] = p
    return w


def _ambitious(pid="p_a") -> tuple:
    """A person committed to an OUGHT about `X`, and his world."""
    p = Person(pid, pid)
    p.tenures.append(Tenure(f"t_{pid}_o", pid, "o_x", "commit", 0))
    return p, _world_with(p, [Proposition("o_x", "OUGHT", "X", "X ought to be so", True, 0)])


def _admits_x(p: Person) -> None:
    """A claim about X reaches `p`'s questions only through `reach`; a `hold` on X puts it there.
    Tier 0 is tested before tier 1, so the claim still reads as the ambition's."""
    p.tenures.append(Tenure(f"t_{p.id}_x", p.id, "X", "hold", 0))


# ---------------------------------------------------------------------------
# (a), (a2), (b) -- the order
# ---------------------------------------------------------------------------

def test_an_ambition_about_x_is_answered_before_a_hash_earlier_claim_about_y():
    p, w = _ambitious()
    _admits_x(p)
    # Y is the person himself (reach's limb 1, no tier) and, second, one of his own tenure's
    # objects (tier 1): the claim about X answers first against either.
    p.tenures.append(Tenure("t_y", p.id, "Y", "hold", 0))
    p.ledger += [_claim("c_000", p.id, "Y"), _claim("c_001", p.id, p.id),
                 _claim("c_zzz", p.id, "X")]
    qs = world_q.questions_for(w, p)
    assert sorted(qs, key=old_key)[0].referents == ("Y",), "control: the old key answered Y first"
    assert qs[0].source == "claim_landed" and qs[0].referents == ("X",), [q.id for q in qs]


def test_a_person_whose_only_question_is_need_answers_it():
    p, w = _ambitious()
    qs = world_q.questions_for(w, p)
    assert [q.id for q in qs] == ["q:need:o_x"]
    # ... and a claim with no tier (about himself, no deed) stays behind it
    p.ledger.append(_claim("c_000", p.id, p.id))
    qs = world_q.questions_for(w, p)
    assert sorted(qs, key=old_key)[0].id == "q:claim:c_000", "control: the old key put it first"
    assert qs[0].id == "q:need:o_x", [q.id for q in qs]


def test_a_tier_1_claim_precedes_the_need_question():
    p, w = _ambitious()
    p.tenures.append(Tenure("t_obj", p.id, "obj_t", "hold", 0))
    p.ledger.append(_claim("c_3", p.id, "obj_t"))
    qs = world_q.questions_for(w, p)
    key = world_q.attention_key(w, p)
    assert [q.id for q in qs] == ["q:claim:c_3", "q:need:o_x"], [q.id for q in qs]
    assert [key(q)[0] for q in qs] == [1, NEED_TIER]


def _echo_world():
    """p_a: an ambition about X (whose claims reach him through a `hold` on X) and a tenure on Y.
    He holds a claim about X recording HIS OWN refused act (`doer` = p_a, as WITNESS stamps it) --
    his only tier-0 candidate -- and a claim about Y recording p_q's act. The own-act claim's id
    sorts first."""
    p, w = _ambitious()
    _admits_x(p)
    p.tenures.append(Tenure("t_y", p.id, "Y", "hold", 0))
    w.persons["p_q"] = Person("p_q", "p_q")
    own = _claim("c_000", p.id, "X", "release.refused", True)
    p.ledger += [dataclasses.replace(own, doer=p.id), _claim("c_zzz", p.id, "Y", "speech.made", True)]
    return p, w


def test_a_claim_recording_his_own_act_ranks_after_a_foreign_occasioned_claim():
    """C's falsifier: the echo of his own act is not news. Without `doer` the own-act claim about
    his ambition's subject is tier 0 and answered first (the control below); with it, the claim
    sorts with the rest, after the foreign-occasioned claim (tier 1) and the `need` question."""
    p, w = _echo_world()
    qs = world_q.questions_for(w, p)
    assert [q.about for q in qs] == ["c_zzz", "o_x", "c_000"], [q.id for q in qs]
    assert [world_q.attention_key(w, p)(q)[0] for q in qs] == [1, NEED_TIER, 4]
    p.ledger[-2] = dataclasses.replace(p.ledger[-2], doer=None)
    assert world_q.questions_for(w, p)[0].about == "c_000", (
        "control: without `doer` the own-act claim about X is tier 0 and first")


def test_another_persons_doer_is_not_the_screen():
    """The key compares `doer` with the ASKER: a claim stamped with someone else's id (which
    WITNESS never writes, asserted below on a live season) does not demote it."""
    p, w = _echo_world()
    p.ledger[-2] = dataclasses.replace(p.ledger[-2], doer="p_q")
    assert world_q.questions_for(w, p)[0].about == "c_000"


def test_the_five_tiers_order_against_the_old_key():
    p, w = _ambitious()
    _admits_x(p)
    p.pursuits = dict(PURSUITS)
    small, big = _deed_kinds(p.pursuits)
    p.tenures.append(Tenure("t_obj", p.id, "obj_t", "hold", 0))
    p.ledger += [
        _claim("c_0", p.id, p.id),                               # tier 4: about me, no deed
        _claim("c_1", p.id, p.id, small, True),                  # tier 2, small |valence|
        _claim("c_2", p.id, p.id, big, True),                    # tier 2, large |valence|
        _claim("c_3", p.id, "obj_t"),                            # tier 1: my own tenure's object
        _claim("c_4", p.id, "X"),                                # tier 0: my ambition's subject
    ]
    qs = world_q.questions_for(w, p)
    ids = [q.id for q in qs]
    assert [q.id for q in sorted(qs, key=old_key)] == [
        "q:claim:c_0", "q:claim:c_1", "q:claim:c_2", "q:claim:c_3", "q:claim:c_4", "q:need:o_x"]
    assert ids == ["q:claim:c_4", "q:claim:c_3", "q:claim:c_2", "q:claim:c_1", "q:need:o_x",
                   "q:claim:c_0"], ids
    key = world_q.attention_key(w, p)
    assert [key(q)[0] for q in qs] == [0, 1, 2, 2, NEED_TIER, 4]


def test_a_seat_purview_is_tier_1_and_the_ladder_above_home_is_not():
    """Limb 4 (the seat's rung and below) is tier 1; limb 3 (the ladder) is in `reach` but is no
    tier (`own_purview` is limbs 2 and 4 only)."""
    w = POP.build_realm(0)
    seated = [(p, t) for p in w.persons.values() for t in p.tenures
              if t.kind == "hold" and t.live and t.object in w.offices
              and w.offices[t.object].rung is not None]
    assert seated
    p, t = seated[0]
    rung = w.offices[t.object].rung
    key = world_q.attention_key(w, p)
    assert key(Question("q:claim:z", "claim_landed", (rung,), "z"))[0] == 1
    mine = world_q.own_purview(w, p)
    ladder, cur = [], home_of(w).get(p.id)
    while cur is not None and cur not in ladder:
        ladder.append(cur); cur = parent_of(w, cur)
    outside = [r for r in ladder if r not in mine]
    assert outside, "control: a rung on the ladder lies outside his purview"
    assert key(Question("q:claim:z", "claim_landed", (outside[-1],), "z"))[0] == 4


# ---------------------------------------------------------------------------
# (c) -- the key reads only the person's own state
# ---------------------------------------------------------------------------

PROBES = (
    Question("q:claim:c9", "claim_landed", ("X",), "c9"),
    Question("q:claim:c8", "claim_landed", ("obj_t",), "c8"),
    Question("q:claim:c7", "claim_landed", ("p_a",), "c7"),
    Question("q:claim:c6", "claim_landed", ("elsewhere",), "c6"),
    Question("q:need:o_x", "need", ("X",), "o_x"),
    Question("q:claim:c5", "claim_landed", ("X",), "c5"),   # his own act's echo: tier 4, not 0
)


def test_the_same_question_keys_differently_for_two_persons_with_different_state():
    a, w = _ambitious("p_a")
    b = Person("p_b", "p_b")
    w.persons[b.id] = b
    q = PROBES[0]                                                # a claim about X
    assert world_q.attention_key(w, a)(q) != world_q.attention_key(w, b)(q)
    assert world_q.attention_key(w, a)(q)[0] == 0 and world_q.attention_key(w, b)(q)[0] == 4
    b.tenures.append(Tenure("t_bx", b.id, "X", "hold", 0))      # B's own tenure on X: tier 1
    assert world_q.attention_key(w, b)(q)[0] == 1
    # tier 2 is read through the person's own pursuits: the same deed claim, two holders
    small, big = _deed_kinds(PURSUITS)
    c = _claim("c_d", "p_a", "elsewhere", big, True)
    a.pursuits = dict(PURSUITS)
    a.ledger.append(c); b.ledger.append(c)
    qd = Question("q:claim:c_d", "claim_landed", ("elsewhere",), "c_d")
    assert world_q.attention_key(w, a)(qd)[0] == 2 and world_q.attention_key(w, b)(qd)[0] == 4


def _other_state(w: World) -> World:
    """`w` changed ONLY outside p_a's own state: another person with an ambition about every probe
    referent, a seat and a ledger; an unrelated OUGHT; an Event in the log."""
    w2 = copy.deepcopy(w)
    w2.propositions["o_y"] = Proposition("o_y", "OUGHT", "elsewhere", "another ought", True, 0)
    q = Person("p_q", "p_q", pursuits={"family": 5})
    q.tenures += [Tenure("t_q1", "p_q", "o_y", "commit", 0),
                  Tenure("t_q2", "p_q", "obj_t", "hold", 0)]
    q.ledger += [_claim("c_q", "p_q", "X"), _claim("c9", "p_q", "X", "bond.formed", True)]
    w2.persons[q.id] = q
    w2.log.append(Event(id="e_other", kind="body.changed",
                        changes=[StateChange("p_q", "set", "MATTER", "f")],
                        causes=[ROOT], emitted_at=0))
    return w2


def test_one_person_keys_alike_under_worlds_differing_only_outside_his_own_state():
    p, w = _ambitious()
    p.pursuits = dict(PURSUITS)
    p.tenures.append(Tenure("t_obj", p.id, "obj_t", "hold", 0))
    p.ledger.append(_claim("c7", p.id, p.id, _deed_kinds(PURSUITS)[1], True))
    p.ledger.append(dataclasses.replace(_claim("c5", p.id, "X", "release.refused", True), doer=p.id))
    w2 = _other_state(w)
    p2 = w2.persons[p.id]
    assert len(w2.log) > len(w.log) and len(w2.persons) > len(w.persons)   # the worlds differ
    k1, k2 = world_q.attention_key(w, p), world_q.attention_key(w2, p2)
    tiers = {k1(q)[0] for q in PROBES}
    assert tiers == {0, 1, 2, NEED_TIER, 4}, tiers                # every tier is probed
    for q in PROBES:
        assert k1(q) == k2(q), q.id


# ---------------------------------------------------------------------------
# (d) -- one rule
# ---------------------------------------------------------------------------

def test_reach_composes_on_own_purview():
    w = POP.build_realm(0)
    checked = 0
    for p in w.persons.values():
        ladder, cur = set(), home_of(w).get(p.id)
        while cur is not None and cur not in ladder:
            ladder.add(cur); cur = parent_of(w, cur)
        assert world_q.reach(w, p) == {p.id} | ladder | world_q.own_purview(w, p), p.id
        checked += 1
    assert checked >= 50


# ---------------------------------------------------------------------------
# (e) -- the EXIT line: seed 0, season 1
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def season_1():
    """Every `questions_for` call DELIBERATE receives in `build_realm(0)`'s first season, with the
    tier of each question taken at the call (the key reads the state then)."""
    w = POP.build_realm(0)
    real, seen = DRV.questions_for, []

    def spy(w_, p, since=None):
        out = real(w_, p, since)
        key = world_q.attention_key(w_, p)
        seen.append((p.id, [key(q)[0] for q in out], [q.id for q in out],
                     [q.id for q in sorted(out, key=old_key)]))
        return out

    DRV.questions_for = spy
    try:
        POP.run(1, 0, w=w)
    finally:
        DRV.questions_for = real
    return seen, w


def test_witness_stamps_doer_exactly_on_the_holders_own_acts(season_1):
    """`Claim.doer` is set on a held claim IF AND ONLY IF the Event it records was caused by the
    holder's own act -- read here the long way, through the log (`claim.deposited` -> the recorded
    Event -> `causing_act`), which the key may not do and a test may. Never on a told copy, never
    anyone's id but the holder's; asserts it asserted (stamped and unstamped both populated)."""
    _, w = season_1
    dep, ev = {}, {}
    for e in w.log:
        ev[e.id] = e
        if e.kind == "claim.deposited":
            for c in e.changes:
                dep[c.subject] = [x for x in (e.causes or []) if x != ROOT]
    stamped = unstamped = 0
    for p in w.persons.values():
        for c in p.ledger:
            if c.id not in dep:
                continue
            own = any((a := causing_act(w, ev[x])) is not None and a.actor == p.id
                      for x in dep[c.id] if x in ev)
            assert c.doer in (None, p.id), (p.id, c)
            assert (c.doer == p.id) == own, (p.id, c.id, c.predicate, c.doer, own)
            if c.doer is not None:
                assert c.source != "told_by" and not c.chain, c
            stamped += c.doer is not None
            unstamped += c.doer is None
    # MEASURED at IN-57, `build_realm(0)`, one season: 1,652 of 5,238 held claims stamped.
    assert stamped >= 1000 and unstamped >= 1000, (stamped, unstamped)


def test_seed_0_season_1_each_person_answers_a_tier_0_or_1_question_first_where_he_has_one(
        season_1):
    checked = moved = 0
    for pid, tiers, ids, old_ids in season_1[0]:
        if not any(t <= 1 for t in tiers):
            continue
        checked += 1
        assert tiers[0] <= 1, (pid, list(zip(ids, tiers)))
        moved += ids[0] != old_ids[0]
    # MEASURED at IN-57 (with the own-act screen): 390 calls, 133 holding a tier-0/1 question, 80 of
    # those first questions moved against the old key; first-question tiers {0: 28, 1: 105, 2: 1,
    # 3 (need): 108, 4: 105}. Without the screen 299 calls held one: most were his own act's echo.
    assert checked >= 100, checked
    assert moved >= 1, "control: the tiered key changed no person's first question"
