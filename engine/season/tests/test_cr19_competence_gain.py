"""v10 CR-19: `AX-7`'s competence reads Attunement (`H-200`) -- `competence_gain`, shipped at 0.

`decision/options.py::refracted_confidence` gains a swept `competence_gain` (`Fixtures`, `H-200`), whose factor
`competence(p, g)` is monotone in the receiver's Attunement (`Person.attributes`, CR-20), exactly 1 at the scale's
middle, and 1 for a receiver with no authored Attunement. IT SHIPS AT 0: the factor is in place and the flip to a
live gain is a later declared mover, because a person-side gain cannot separate a lie from a truth
(`ED-IN-0327`; `competence`'s docstring; left to CR-27's `lie` and CR-83's design). So the falsifier sets a live
gain IN THE TEST.

FALSIFIER: one told claim, one channel (`co_located`), two receivers at Attunement 2 and 6 hold it at DIFFERENT
confidence at a live gain. PLANTED FAILURE (run 2026-11-05): `* competence(p, competence_gain)` dropped from
`refracted_confidence` -- the two hold it equal and `test_two_receivers_..._differ` reddens (37 == 37). Restored.
CONTROL: at the shipped gain 0 they hold it equal, the shipped gain IS 0, and `build_realm(0)` at one season is
the same world, hash and ordered `(kind, id)` log, as with the factor made inert.
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..decision import options as OPT
from ..decision.options import COMPETENCE_ATTRIBUTE, COMPETENCE_MID, competence, refracted_confidence
from ..epistemic import observers_for
from ..harness import populated as POP
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries.person_q import said_of
from ..state.carriers import Act, Claim, Event
from ..state.ids import H
from .test_ax7_refraction import HELD_CONF, TELLER, _told

LOW, HIGH = "p_mid", "p_other"      # two hearers standing in `Hh`, so one channel (`co_located`) reaches both
LIVE = 0.5                          # a live competence gain, set in the test and never shipped


def _two_hear(competence_gain: float, attunement=(2, 6)):
    """`TELLER` tells `(Hh, stores:grain, 8)` at confidence 37; `LOW` and `HIGH` hear it by presence. Their
    Attunement is authored through `Person.attributes` (`attunement` is `(LOW, HIGH)`, `None` leaves it unauthored)."""
    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("competence_gain", competence_gain)
    for pid, a in zip((LOW, HIGH), attunement):
        if a is not None:
            w.persons[pid].attributes = {COMPETENCE_ATTRIBUTE: a}
    w.persons[TELLER].ledger.append(
        Claim("c_held", TELLER, "Hh", "stores:grain", 8, 0, "firsthand", HELD_CONF, "own"))
    act = Act(id="a_tell_cr19", actor=TELLER, verb="tell",
              payload={"subject": "Hh", "said": said_of(w.persons[TELLER].ledger, "Hh", w.fixtures)})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, TELLER, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    chans = dict(observers_for(w, ev, "all_five", list(w.persons)))
    assert chans.get(LOW) == chans.get(HIGH) == "co_located", f"the fixture moved: {chans}"
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    got = {}
    for pid in (LOW, HIGH):
        told = _told(w, pid)
        assert len(told) == 1 and told[0].value == 8, (pid, told)
        got[pid] = told[0].confidence
    return got


def test_the_gain_ships_at_the_control_zero():
    assert DEFAULT_FIXTURES.get("competence_gain") == 0.0


def test_two_receivers_of_one_told_claim_on_one_channel_hold_it_at_different_confidence_at_a_live_gain():
    got = _two_hear(LIVE)
    assert got[LOW] < got[HIGH] <= HELD_CONF, got      # Attunement 2 credits it less than 6 does
    assert got == {LOW: 25, HIGH: 37}, got             # 37 * (1 + .5 * (2 - 4) / 3) = 24.67 -> 25; 6 is capped at 1


def test_at_the_shipped_gain_zero_they_hold_it_equal():
    got = _two_hear(DEFAULT_FIXTURES.get("competence_gain"))
    assert got == {LOW: HELD_CONF, HIGH: HELD_CONF}, got


def test_a_receiver_with_no_authored_attunement_reads_one_at_a_live_gain():
    got = _two_hear(LIVE, attunement=(None, None))
    assert got == {LOW: HELD_CONF, HIGH: HELD_CONF}, got
    assert competence(P.tiny_world().persons[LOW], 1.0) == 1.0


def test_the_factor_is_one_at_the_scales_middle_and_monotone_in_attunement():
    p = P.tiny_world().persons[LOW]
    assert COMPETENCE_MID == 4
    seen = []
    for a in range(1, 8):
        p.attributes = {COMPETENCE_ATTRIBUTE: a}
        seen.append(competence(p, 1.0))
    assert seen[3] == 1.0, seen                                # Attunement 4
    assert seen == sorted(seen) and seen[0] < seen[3], seen    # monotone, and not flat
    assert seen[0] == 0.0, seen                                # the floor at gain 1
    p.attributes = {COMPETENCE_ATTRIBUTE: 2}
    assert [competence(p, 0.0)] == [1.0]                       # gain 0: 1 for everyone
    for bad in (-0.1, 1.5):
        with pytest.raises(ValueError):
            competence(p, bad)


def test_refracted_confidence_reads_the_factor_directly():
    c = Claim("c_x", LOW, "Hh", "stores:grain", 8, 0, "told_by", 60, "own")
    p = P.tiny_world().persons[LOW]
    p.attributes = {COMPETENCE_ATTRIBUTE: 2}
    assert refracted_confidence(p, c, "co_located", 0.5) == 60                          # competence_gain defaults to 0
    assert refracted_confidence(p, c, "co_located", 0.5, competence_gain=0.0) == 60
    assert refracted_confidence(p, c, "co_located", 0.5, competence_gain=LIVE) < 60


def test_the_realm_at_the_shipped_gain_is_the_realm_with_the_factor_inert(monkeypatch):
    """CONTROL on `build_realm(0)`, one season: the shipped world equals the world with `competence` made the
    constant 1 (the pre-CR-19 formula), by content hash and by the ordered `(kind, id)` event list. Latent in the
    realm because the cast authors no Attunement; a cast row that gains one moves a LIVE gain, not this."""
    def run(seed=0):
        w = POP.build_realm(seed)
        POP.run(seasons=1, seed=seed, w=w)
        return w.content_hash(), [(e.kind, e.id) for e in w.log]

    shipped = run()
    assert len(shipped[1]) > 1000, "a vacuous log would make the equality below say nothing"
    monkeypatch.setattr(OPT, "competence", lambda p, g: 1.0)
    inert = run()
    assert shipped == inert
