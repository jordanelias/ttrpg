"""B24p.06 -- the bearing reading and what a person carries in (V2 p2 §A.2 to §A.4, §G).

Every reader here is person-side: it reads the person's OWN interior and the operands the host passes, never `World`,
another person's ledger or a true attribute of anyone else. Hand-built people only; `test_sc_roles.py` is shared with
the exchange's and the roles' tests (B24p.07, .18): the last two tests below are the exchange's (a Focus role and a Reason role)."""
from __future__ import annotations

from ..data.affiliations import AFFILIATION_CEILING, AFFILIATIONS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import STANCE_MAX
from ..queries import person_q as PQ
from ..queries.inputs import Choice
from ..state.carriers import Claim, Person, interior_of
from .test_sc_proceeding_module import P, _dials, _inp, _key, _p, _rite, _sit

FX = DEFAULT_FIXTURES
FULL = (("x", 5, 5),)        # one stance row at the row type's bound: a relationship of +1


def _person(pid="p", **kw):
    return Person(id=pid, **kw)


def test_bearing_reads_only_his_own_interior():
    """A pursuit the matter helps reads `want` above 0, the same matter against it below 0; a man with nothing at stake
    reads `(0, 0, bond)`. Read from `interior_of(p)`, the record that carries nothing but his own state."""
    lover = interior_of(_person(pursuits={"wealth": 0.8}, stance=[("x", 2, 5)]), 0, 0)
    helps = PQ.bearing(lover, {"wealth": 1.0}, for_party="x", against_party="y")
    against = PQ.bearing(lover, {"wealth": -1.0}, for_party="x", against_party="y")
    bare = PQ.bearing(interior_of(_person(stance=[("x", 2, 5)]), 0, 0), {"wealth": 1.0}, for_party="x", against_party="y")
    assert helps[0] > 0 > against[0]
    assert bare[:2] == (0, 0) and bare[2] == 10 / STANCE_MAX and bare[2] == helps[2]
    # a held conviction reads as `hold`, over the roster's own ceiling, and never as `want`
    name = sorted(AFFILIATIONS)[0]
    held = interior_of(_person(conviction={name: AFFILIATION_CEILING}), 0, 0)
    got = PQ.bearing(held, {name: 1.0}, for_party="x", against_party="y")
    assert got == (0, 1.0, 0)


def test_conflict_on_both_sides_never_cancels():
    """Interests and ties on both sides are a conflict, never a cancellation (V2 p4 §K B6, §L 13); a shared faction is
    a tie, never partiality (§L R1); a conviction alone is not partiality (§L 19)."""
    # a pursuit the matter helps and an office duty it hurts: opposed, equal
    wants = _person(pursuits={"wealth": 0.5})
    c, lean = PQ.conflict(wants, {"wealth": 1.0}, for_party="x", against_party="y", duty=(("wealth", -0.5),))
    assert round(c, 2) == 0.33 and lean == 0.0
    # a tie as strong to one party as to the other
    both = _person(stance=[("x", 5, 5), ("y", 5, 5)])
    c, lean = PQ.conflict(both, {}, for_party="x", against_party="y")
    assert round(c, 2) == 0.33 and lean == 0.0
    # a conviction the matter bears on, alone: it moves how he hears (hold), it makes him no partial
    name = sorted(AFFILIATIONS)[0]
    law = _person(conviction={name: AFFILIATION_CEILING})
    assert PQ.bearing(law, {name: 1.0}, for_party="x", against_party="y")[1] == 1.0
    assert PQ.conflict(law, {name: 1.0}, for_party="x", against_party="y") == (0.0, 0.0)
    # a shared faction with one party moves the bond he hears by and is not partiality
    judge = _person()
    assert PQ.bearing(judge, {}, for_party="x", against_party="y", shares=("x",))[2] > 0
    assert PQ.conflict(judge, {}, for_party="x", against_party="y") == (0.0, 0.0)


def test_bearing_gives_a_party_a_stake_in_his_own_case():
    """A flat matter: each party's `mean(stake)` is `PARTY_STAKE` toward his own side; a non-party's is 0; `party=False`
    reads the matter without the floor; a stake already above the floor is not lowered."""
    def mean(stake):
        return sum(stake) / len(stake)

    flat = {}
    pro = mean(PQ.bearing(_person("x"), flat, for_party="x", against_party="y"))
    con = mean(PQ.bearing(_person("y"), flat, for_party="x", against_party="y"))
    out = mean(PQ.bearing(_person("z"), flat, for_party="x", against_party="y"))
    assert pro > 0 > con and out == 0                 # being a party is a stake, toward his own side
    assert abs(pro - PQ.PARTY_STAKE) < 1e-12 and abs(con + PQ.PARTY_STAKE) < 1e-12
    assert mean(PQ.bearing(_person("x"), flat, for_party="x", against_party="y", party=False)) == 0
    keen = PQ.bearing(_person("x", pursuits={"wealth": 1.0}), {"wealth": 1.0}, for_party="x", against_party="y")
    assert mean(keen) > PQ.PARTY_STAKE and keen[2] == 0


def test_a_false_item_is_his_own_word_or_nothing():
    """A man whose own ledger holds the matter false and who speaks for it gets one insincere `testimony` of his own;
    one whose ledger agrees gets none; so does one who holds nothing (a forged `Record` is a `[HOOK]`)."""
    def knows(value, pid="p"):
        return _person(pid, ledger=[Claim("c", pid, "m", "held_by:q", value, 0, "firsthand", 80, "own")])

    liar = PQ.false_items(knows(False), "m", "for", FX)
    assert len(liar) == 1 and liar[0].kind == "testimony" and liar[0].sincere is False
    assert liar[0].source == "p" and liar[0].about == "m" and 0 < liar[0].weight <= 1
    assert PQ.false_items(knows(False), "m", "against", FX) == ()
    assert PQ.false_items(knows(True), "m", "for", FX) == ()
    assert len(PQ.false_items(knows(True), "m", "against", FX)) == 1
    assert PQ.false_items(_person(), "m", "for", FX) == ()
    assert PQ.believes(knows(False), "m", FX) < 0 < PQ.believes(knows(True), "m", FX)


def test_strain_carried_fades_and_is_bounded():
    """Each rattle fades on its own clock and the k-th freshest counts half the one before: any number of rattles stays
    under 1.0 and each further scene lowers the load. Control: with no fade the load does not drop."""
    assert PQ.strain_carried((), FX) == 0
    assert PQ.strain_carried((0,) * 1000, FX) < 1.0
    assert PQ.strain_carried((2,), FX) < PQ.strain_carried((1,), FX) < PQ.strain_carried((0,), FX)
    still = FX.sweep("strain_fade", 0.0)
    assert PQ.strain_carried((9,), still) == PQ.strain_carried((0,), still)
    assert PQ.strain_carried((3, 0), FX) == PQ.strain_carried((0, 3), FX)


def _speak(inp, mover, keyed, ground="consequence"):
    return P.exchange(inp, _sit(inp), mover, Choice("argue", ground, None, None), _key("roles", keyed))[1]


def test_drift_is_continuous_in_the_pull():
    """FOCUS (R1, B14): what pulls a man off the point (the times' `unrest`) moves him only as far as his hold fails to carry it: no pull,
    no drift; a pull of 0.0001 a drift of at most 0.0001 even at Focus 1 (it once read 0.67); a real pull sometimes carries him."""
    seen = {}
    for pull in (0.0, 0.0001, 0.5):
        inp = _inp([_p("a", "for", focus=1.0), _p("b", "against"), _p("j", decides=True)], _rite(unrest=pull))
        drifts = [_speak(inp, inp.room[0], i).drift for i in range(60)]
        assert all(0.0 <= d <= pull for d in drifts), (pull, max(drifts))
        seen[pull] = sum(d > 0 for d in drifts)
    assert seen[0.0] == 0 and seen[0.5] > 5, seen


def test_a_party_who_decides_hears_his_own_case_by_his_own_reason():
    """REASON, C2: a party who decides is moved by his own speech, heard by HIMSELF: his own Reason validates it (a sounder speaker moves
    his own track further, the dice held equal), his own Will resists it, and the other side's Reason and Will, which he is not hearing
    through, change nothing on his track (his own Reason is 7, off the middle, so that a validation read from anyone else would show)."""
    def own_move(a_reason=7.0, a_will=4.0, b_reason=4.0, b_will=4.0):
        dials = _dials(DEFAULT_FIXTURES.sweep("fit_level", "strong"))
        grounds = (("consequence", 0.0, 1.0),)                # Reason's share of the dice 0: only Presence rolls, so Reason acts by validating
        inp = _inp([_p("a", "for", True, reason=a_reason, will=a_will), _p("b", "against", reason=b_reason, will=b_will)], dials=dials, grounds=grounds)
        return dict(_speak(inp, inp.room[0], 7).moved)

    base = own_move()
    assert "a" in base
    assert own_move(a_reason=7.0)["a"] > own_move(a_reason=1.0)["a"]
    assert own_move(a_will=7.0)["a"] < own_move(a_will=1.0)["a"]
    assert own_move(b_reason=7.0)["a"] == own_move(b_reason=1.0)["a"] == base["a"]
    assert own_move(b_will=7.0)["a"] == own_move(b_will=1.0)["a"] == base["a"]
