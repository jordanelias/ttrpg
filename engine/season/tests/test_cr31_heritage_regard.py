"""v11 CR-31: the caste estimate, a heritage regard term (`queries/person_q.py::heritage_regard`, `regard`'s
third term, at `Fixtures heritage_gain`, `H-348`).

FALSIFIER (the plan's): two hearers with equal stance toward one teller and the same `seen` claim marking him
`southern_einhir`, one holding `einhir_restoration: 0` and one `5`, weight the same told claim differently at
`heritage_gain` 0.5 and identically at 0; a hearer holding no such `seen` claim weights it as at 0; a hearer with no
`einhir_restoration` key reads the term 0. PLANTED FAILURE: `conviction_stand` with its sign flipped reverses the
first pair's order (the test below observes the reversal).

THE POLARITY ARMS that read the term: at the shipped `stance_polarity` `declared`, and at `regard`, `stance_term`
reads `regard(p, subject, fx)`, which carries the term; `legacy` reads `stance_toward` and does not. The shipped
consumer of the told-claim weight is `decision/options.py::teller_weight`'s relation term.

THE CONTROL (`heritage_gain` 0 reproduces the pre-item tree's `build_realm(0)` hash) is measured with the
instrument and recorded in the CR-31 commit body, not asserted here: a hash is no pin (CLAUDE.md §0.1 pt 5).
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.season.data.cast import STANCE_MAX
from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.data.rosters import SEEN_PREDICATE
from engine.season.decision.choose import _stance_arm
from engine.season.decision.options import teller_weight
from engine.season.epistemic import Seen
from engine.season.queries import person_q
from engine.season.queries.person_q import conviction_stand, heritage_regard, regard
from engine.season.state.carriers import Claim, Person

SOUTH, ALT, NORTH = "southern_einhir", "altonian", "northern_einhir"
TELLER = "x"


def _fx(gain, **more):
    """Every other regard-bearing gain held at its control, so the term is the only thing that moves a weight."""
    fx = (DEFAULT_FIXTURES.sweep("heritage_gain", gain).sweep("judged_gain", 0.0).sweep("told_valence_gain", 0.0)
          .sweep("record_gain", 0.0))
    for k, v in more.items():
        fx = fx.sweep(k, v)
    return fx


def _seen(pid, who, marks, when=1, rnd=0, chain=(), n=[0]):
    n[0] += 1
    return Claim(f"c_seen_{n[0]}", pid, "Hh", SEEN_PREDICATE, Seen(stratum="speech", marks=marks, who=who),
                 when, "firsthand", 100, "own", round=rnd, chain=chain)


def _told():
    return Claim("c_told", "h", "Hh", "stores:grain", 0, 2, "told_by", 100, "own", chain=(TELLER,))


def _hearer(pid, conviction, marks=(SOUTH,), stance=None):
    p = Person(pid, conviction=conviction)
    if stance is not None:
        p.stance = [(TELLER, stance, 1)]
    if marks is not None:
        p.ledger.append(_seen(pid, TELLER, marks))
    return p


def _weight(p, gain):
    return teller_weight(p, _fx(gain))(_told())


# ======================================================================================
# THE FALSIFIER
# ======================================================================================

def test_two_hearers_equal_in_stance_weigh_a_told_claim_by_their_creed_at_half_and_alike_at_zero():
    restorer, rejecter = _hearer("h5", {"einhir_restoration": 5}, stance=1), _hearer("h0", {"einhir_restoration": 0},
                                                                                     stance=1)
    assert person_q.stance_toward(restorer, TELLER) == person_q.stance_toward(rejecter, TELLER) == 1
    live = (_weight(restorer, 0.5), _weight(rejecter, 0.5))
    assert live[0] > live[1], live                     # the restorationist credits a southern Einhir teller more
    assert _weight(restorer, 0.0) == _weight(rejecter, 0.0)


def test_a_hearer_who_never_saw_the_teller_marked_weighs_as_at_zero():
    for marks in (None, (), (NORTH,), ("pontiff",)):   # none held; nothing describable; engages no concern; no heritage
        p = _hearer("h0", {"einhir_restoration": 0}, marks=marks)
        assert _weight(p, 0.5) == _weight(p, 0.0), marks
        assert heritage_regard(p, TELLER, _fx(0.5)) == 0.0


def test_a_hearer_with_no_conviction_key_reads_zero_not_held():
    for conviction in ({}, {"solmund_orthodoxy": 5}):
        p = _hearer("h", conviction)
        assert heritage_regard(p, TELLER, _fx(1.0)) == 0.0
        assert _weight(p, 0.5) == _weight(p, 0.0)


def test_a_stored_zero_is_a_held_rejection_and_pulls_hardest():
    """Absent reads 0 and a stored 0 reads -1 -- the two cannot be told apart by anything but the key."""
    absent, zero, five = (_hearer("a", {}), _hearer("z", {"einhir_restoration": 0}),
                          _hearer("f", {"einhir_restoration": 5}))
    fx = _fx(1.0)
    assert heritage_regard(absent, TELLER, fx) == 0.0
    assert heritage_regard(zero, TELLER, fx) == -STANCE_MAX
    assert heritage_regard(five, TELLER, fx) == STANCE_MAX
    mid = [heritage_regard(_hearer("m", {"einhir_restoration": v}), TELLER, fx) for v in (2, 3)]
    assert mid[0] == -mid[1] and 0 < mid[1] < STANCE_MAX


def test_the_planted_failure_the_centring_sign_flipped_reverses_the_pair(monkeypatch):
    """The first assertion above can observe the failure it excludes."""
    restorer, rejecter = _hearer("h5", {"einhir_restoration": 5}), _hearer("h0", {"einhir_restoration": 0})
    assert _weight(restorer, 0.5) > _weight(rejecter, 0.5)
    real = person_q.conviction_stand
    monkeypatch.setattr(person_q, "conviction_stand", lambda p, a: -real(p, a))
    assert _weight(restorer, 0.5) < _weight(rejecter, 0.5)


# ======================================================================================
# THE READER
# ======================================================================================

def test_the_newest_own_untold_seen_claim_that_marks_a_heritage_is_the_belief():
    p = Person("h", conviction={"einhir_restoration": 5, "altonian_civics": 0})
    p.ledger.append(_seen("h", TELLER, (ALT,), when=1))
    p.ledger.append(_seen("h", TELLER, (SOUTH,), when=3))
    p.ledger.append(_seen("h", TELLER, (), when=5))                  # newer, but marks no heritage: not the belief
    p.ledger.append(_seen("h", "somebody_else", (ALT,), when=6))     # another person's mark
    p.ledger.append(_seen("h", TELLER, (ALT,), when=9, chain=("y",)))   # told, not seen
    fx = _fx(1.0)
    assert heritage_regard(p, TELLER, fx) == STANCE_MAX              # SOUTH (when 3) beats ALT (when 1)
    p.ledger.append(_seen("h", TELLER, (ALT,), when=3, rnd=1))       # same season, a later round
    assert heritage_regard(p, TELLER, fx) == -STANCE_MAX             # ALT engages `altonia`, which `h` rejects
    assert heritage_regard(p, "somebody_else", fx) == -STANCE_MAX


def test_the_term_is_in_regards_own_units_and_scales_with_the_gain():
    p = _hearer("h", {"einhir_restoration": 5})
    for gain in (0.5, 1.0, 2.0):
        assert heritage_regard(p, TELLER, _fx(gain)) == gain * STANCE_MAX
    assert regard(p, TELLER, _fx(0.0)) == 0.0 == person_q.stance_toward(p, TELLER)
    assert regard(p, TELLER, _fx(0.5)) == 0.5 * STANCE_MAX
    assert regard(p, TELLER) == 0.0                                  # no fixtures: the stored half exactly


@pytest.mark.parametrize("bad", [-0.1, float("nan")])
def test_a_negative_or_nan_gain_raises(bad):
    with pytest.raises(ValueError):
        heritage_regard(_hearer("h", {"einhir_restoration": 5}), TELLER, _fx(bad))


def test_the_term_reads_the_hearers_own_ledger_alone():
    """No World, and the teller need not exist anywhere: the only inputs are the hearer, an id, and the fixtures."""
    p = _hearer("h", {"einhir_restoration": 5})
    assert heritage_regard(p, TELLER, _fx(1.0)) == STANCE_MAX
    assert conviction_stand(p, "einhir_restoration") == 1.0 and conviction_stand(p, "altonian_civics") == 0.0


# ======================================================================================
# THE POLARITY ARMS
# ======================================================================================

def test_the_regard_and_declared_arms_read_the_term_and_legacy_does_not():
    p = _hearer("h", {"einhir_restoration": 5})
    cand = SimpleNamespace(verb="tell", subject=TELLER)
    for arm, reads in (("legacy", False), ("regard", True), ("declared", True)):
        fx = _fx(0.5, stance_polarity=arm)
        assert _stance_arm(p, cand, fx, None) == (0.5 * STANCE_MAX if reads else 0.0), arm
        assert _stance_arm(p, cand, _fx(0.0, stance_polarity=arm), None) == 0.0, arm
    assert DEFAULT_FIXTURES.get("stance_polarity") == "declared" and DEFAULT_FIXTURES.get("heritage_gain") == 0.5
