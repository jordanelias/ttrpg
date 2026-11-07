"""v11 CR-79 commit (1) -- THE CREDIT TERM AT WITNESS (`H-275`; `strife-00` §5, R14/A12).

`loop/witness.py::_credit` grades a told claim's confidence, after `_refract`, by
`1 + regime_gain * c`, `c` = `world_q.commensurate(hearer, teller)` in {-1, 0, +1}, clamped to
`[0, max(confidence_default, the uncredited value)]` and applied only when `regime_gain * c` is not 0.
`regime_gain` ships at the control 0 at commit (1).

Every world here is hand-built (`probes.tiny_world`, the told deposit driven as `test_ax7_refraction`
drives it). Each test that means the control sets `regime_gain` to 0 explicitly, and each test runs an
arm in which the term is live, so a test that cannot see the term cannot pass. The affiliation pairs
are `test_strife_flows::test_commensurate`'s, re-checked through `commensurate` before use.
"""

from __future__ import annotations

import math

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..decision.options import COMPETENCE_ATTRIBUTE
from ..epistemic import observers_for
from ..harness import populated as POP
from ..harness import probes as P
from ..loop import witness as WIT
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q as W
from ..queries.person_q import said_of
from ..state.carriers import Act, Claim, Event, Tenure
from ..state.ids import H
from .test_ax7_refraction import HELD_CONF, KNOTTED, NEAR, TELLER, _told

OTHER = "p_other"           # a second hearer standing in `Hh` with `NEAR`, so `co_located` reaches both
LIVE = 0.5                  # the value given (ED-IN-0316), set in the tests and not shipped at commit (1)
# Conviction maps, one affiliation each (pairs from `test_strife_flows::test_commensurate`):
# `NONE` holds no affiliation, so it reads 0 against anyone (an unrelated pair).
THREAD, INNER, ORTHO, NONE = {"thread_truth": 3}, {"inner_tradition": 3}, {"solmund_orthodoxy": 3}, {}
REALM_BASE_HASH = "600d8b27147478e158553552cc1409a5"   # `build_realm(0)`, after B11-S4 (PR #580)


def _tell(regime: float, refraction: float = 0.0, held: int = HELD_CONF, conviction=None,
          competence_gain: float = 0.0, attunement=None):
    """`TELLER` tells `(Hh, stores:grain, 8)` held firsthand at `held`; `NEAR` and `OTHER` hear it in the
    room (`co_located`, remove 0), `KNOTTED` through a knot (`witness_key`). `conviction` and `attunement`
    map a pid to its `Person.conviction` / Attunement. Returns `{hearer: told confidence}`."""
    w = P.tiny_world()
    w.fixtures = (w.fixtures.sweep("regime_gain", regime).sweep("refraction_gain", refraction)
                  .sweep("competence_gain", competence_gain))
    w.add_tenure(Tenure("t_knot_cr79", TELLER, KNOTTED, "knot", since=0))
    for pid, conv in (conviction or {}).items():
        w.persons[pid].conviction = dict(conv)
    for pid, a in (attunement or {}).items():
        w.persons[pid].attributes = {COMPETENCE_ATTRIBUTE: a}
    w.persons[TELLER].ledger.append(
        Claim("c_held", TELLER, "Hh", "stores:grain", 8, 0, "firsthand", held, "own"))
    act = Act(id="a_tell_cr79", actor=TELLER, verb="tell",
              payload={"subject": "Hh", "said": said_of(w.persons[TELLER].ledger, "Hh", w.fixtures)})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, TELLER, f"ev:news.told:{act.id}"), "news.told",
               [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    chans = dict(observers_for(w, ev, "all_five", list(w.persons)))
    assert (chans.get(NEAR), chans.get(OTHER), chans.get(KNOTTED)) == (
        "co_located", "co_located", "witness_key"), f"the fixture moved: {chans}"
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    got = {}
    for pid in (NEAR, OTHER, KNOTTED):
        told = _told(w, pid)
        assert len(told) == 1 and told[0].value == 8 and told[0].chain == (TELLER,), (pid, told)
        got[pid] = told[0].confidence
    return got


def _c(conviction: dict) -> dict:
    """`commensurate(hearer, TELLER)` for each hearer under `conviction`, read off a tiny world: the
    setup check that the pairs still mean what the test says."""
    w = P.tiny_world()
    for pid, conv in conviction.items():
        w.persons[pid].conviction = dict(conv)
    return {pid: W.commensurate(w, pid, TELLER) for pid in (NEAR, OTHER, KNOTTED)}


def revert_cr79(monkeypatch):
    """CR-79 OFF, in process: `regime_gain` at 0, the control. A test that pins a hash from before CR-79's flip to
    0.5 (a declared mover of the told deposit) calls this, so its pin reads the item it names alone."""
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "regime_gain", 0.0)


def test_the_gain_ships_at_the_value_given_and_zero_is_the_control():
    assert DEFAULT_FIXTURES.get("regime_gain") == 0.5      # ED-IN-0316, shipped at commit (2) on its guard


def test_a_commensurate_teller_is_credited_more_than_an_incommensurate_one_and_an_unrelated_one_not_at_all():
    """THE FALSIFIER, below the ceiling. One telling at 37, three hearers: `NEAR` commensurate with the
    teller (+1), `OTHER` incommensurate (-1), `KNOTTED` unrelated (0). Refraction off, so the uncredited
    deposit is the teller's own 37. At 0.5: 56 / 19 / 37; at the control every hearer holds 37.
    PLANTED FAILURE (run 2026-11-07): the told branch's `if regime: tc = _credit(...)` deleted -- RED
    (37, 37, 37 at 0.5). Restored, GREEN."""
    conv = {TELLER: THREAD, NEAR: INNER, OTHER: ORTHO, KNOTTED: NONE}
    assert _c(conv) == {NEAR: 1, OTHER: -1, KNOTTED: 0}
    assert _tell(0.0, conviction=conv) == {NEAR: 37, OTHER: 37, KNOTTED: 37}
    live = _tell(LIVE, conviction=conv)
    assert live == {NEAR: 56, OTHER: 19, KNOTTED: 37}, live
    assert live[NEAR] > live[KNOTTED] > live[OTHER]


def test_the_hearers_own_conviction_not_his_settlements_sets_the_sign():
    """THE DISSENTER (Fable F9). `NEAR` and `OTHER` stand in one hearth of one settlement; the teller and
    `OTHER` hold `solmund_orthodoxy`. `NEAR` holding `thread_truth` is credited at -1 by an orthodox
    teller though everyone round him is orthodox; change NOTHING but `NEAR`'s own conviction to the
    orthodoxy and he is credited at +1. `OTHER`'s deposit does not move between the two runs."""
    dissent = {TELLER: ORTHO, OTHER: ORTHO, NEAR: THREAD}
    conform = {TELLER: ORTHO, OTHER: ORTHO, NEAR: ORTHO}
    assert _c(dissent)[NEAR] == -1 and _c(conform)[NEAR] == 1 == _c(dissent)[OTHER]
    a, b = _tell(LIVE, conviction=dissent), _tell(LIVE, conviction=conform)
    assert (a[NEAR], b[NEAR]) == (19, 56), (a, b)
    assert a[OTHER] == b[OTHER] == 56


def test_a_claim_at_the_ceiling_is_not_raised_past_it():
    """THE CEILING: `max(confidence_default, the uncredited value)`. Told at `confidence_default` (100),
    a commensurate teller leaves it at 100; told ABOVE it (120), the ceiling is the uncredited value and
    +1 leaves it there, while -1 still halves it -- the clamp is a ceiling, not a freeze."""
    top = DEFAULT_FIXTURES.get("confidence_default")
    conv = {TELLER: THREAD, NEAR: INNER, OTHER: ORTHO}
    checked = 0
    for held, near, other in ((top, top, top // 2), (top + 20, top + 20, (top + 20) // 2),
                              (HELD_CONF, 56, 19)):
        got = _tell(LIVE, held=held, conviction=conv)
        assert (got[NEAR], got[OTHER]) == (near, other), (held, got)
        checked += 1
    assert checked == 3


def test_a_commensurate_credit_lands_at_or_above_an_unrelated_one_at_any_competence():
    """The ceiling never lowers a credit. Refraction live (competence is a refraction factor) and
    `competence_gain` 1.0, so Attunement 1..7 spans the competence factor's whole range (0 to 1); at each,
    and at a claim below and at the ceiling, `NEAR` (+1) holds at least what `OTHER` (0) holds, and more
    wherever the uncredited value is strictly between 0 and the ceiling."""
    conv = {TELLER: THREAD, NEAR: INNER, OTHER: NONE}
    assert _c(conv)[NEAR] == 1 and _c(conv)[OTHER] == 0
    top = DEFAULT_FIXTURES.get("confidence_default")
    checked = strict = 0
    for held in (HELD_CONF, top):
        for a in range(1, 8):
            got = _tell(LIVE, refraction=LIVE, held=held, conviction=conv, competence_gain=1.0,
                        attunement={NEAR: a, OTHER: a})
            assert got[NEAR] >= got[OTHER], (held, a, got)
            if 0 < got[OTHER] < top:
                assert got[NEAR] > got[OTHER], (held, a, got)
                strict += 1
            checked += 1
    assert checked == 14 and strict >= 5, (checked, strict)


def test_the_credit_applies_where_nothing_refracts():
    """THE DECOUPLING. At `refraction_gain` 0 and `regime_gain` 0.5 an incommensurate teller's claim told
    at 40 lands at 20: the credit term is not switched off with refraction. With refraction live as well,
    the knotted hearer's refracted copy is halved in turn: credit composes after `_refract`.
    PLANTED FAILURE (run 2026-11-07): the told branch's condition narrowed to `if regime and refracting`
    -- RED here (the claim stays at 40). Restored, GREEN."""
    conv = {TELLER: THREAD, OTHER: ORTHO, KNOTTED: ORTHO}
    assert _c(conv)[OTHER] == _c(conv)[KNOTTED] == -1
    assert _tell(LIVE, refraction=0.0, held=40, conviction=conv)[OTHER] == 20
    refracted = _tell(0.0, refraction=LIVE, conviction=conv)[KNOTTED]
    assert refracted < HELD_CONF, "refraction did not lower the knotted copy: this test sees no composition"
    assert _tell(LIVE, refraction=LIVE, conviction=conv)[KNOTTED] == int(refracted * 0.5 + 0.5)


@pytest.mark.parametrize("bad", [1.5, -0.1, math.nan])
def test_a_regime_gain_outside_zero_to_one_raises(bad):
    with pytest.raises(ValueError, match="regime_gain"):
        _tell(bad, conviction={TELLER: THREAD, NEAR: INNER})


def test_the_control_reads_nothing_and_deposits_what_a_bypass_deposits(monkeypatch):
    """THE CONTROL, at the told site. At `regime_gain` 0 neither `_credit` nor `commensurate` is reached
    (both replaced by a raise), and every hearer holds the teller's own 37 -- the deposit a WITNESS with
    the term bypassed makes (the live arm below, `_credit` replaced by the identity). The same raise
    FIRES at 0.5, so the probe can see a call it excludes."""
    conv = {TELLER: THREAD, NEAR: INNER, OTHER: ORTHO, KNOTTED: NONE}

    def _boom(*a, **k):
        raise AssertionError("reached at the control")
    with monkeypatch.context() as m:
        m.setattr(W, "commensurate", _boom)
        m.setattr(WIT, "_credit", _boom)
        control = _tell(0.0, conviction=conv)
        with pytest.raises(AssertionError, match="reached at the control"):
            _tell(LIVE, conviction=conv)
    with monkeypatch.context() as m:
        m.setattr(WIT, "_credit", lambda w, c, *a: c)
        bypass = _tell(LIVE, conviction=conv)
    assert control == bypass == {NEAR: HELD_CONF, OTHER: HELD_CONF, KNOTTED: HELD_CONF}


def test_the_realm_at_the_control_never_reaches_commensurate_and_its_build_hash_is_the_base(monkeypatch):
    """THE CONTROL, on the realm. `build_realm(0)` hashes to the base reading; one season at
    `regime_gain` 0 (set explicitly) runs with `commensurate` replaced by a raise, so no told deposit read
    a person's affiliations, and its after-hash equals a run with the told site's `_credit` bypassed. The
    seeded before/after hashes over seeds 0-2 against the unmodified base are the commit's scratch reading."""
    w = POP.build_realm(0)
    assert w.content_hash() == REALM_BASE_HASH
    w.fixtures = w.fixtures.sweep("regime_gain", 0.0)

    def _boom(*a, **k):
        raise AssertionError("commensurate read at the control")
    with monkeypatch.context() as m:
        m.setattr(W, "commensurate", _boom)
        POP.run(seasons=1, seed=0, w=w)
    w2 = POP.build_realm(0)
    w2.fixtures = w2.fixtures.sweep("regime_gain", 0.0)
    with monkeypatch.context() as m:
        m.setattr(WIT, "_credit", lambda w, c, *a: c)
        POP.run(seasons=1, seed=0, w=w2)
    assert w.content_hash() == w2.content_hash() != REALM_BASE_HASH
