"""CP-T01-04 at the seam -- `seam/wrappers/sigma.py::resolve` settles the margin's fraction with the act's
own uniform, and `seam/ladder.py::degree_of` grades the settled margin.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * A WHOLE-OB ROLL KEEPS ITS STREAM: after `resolve` the act's generator is in exactly the state the
    module's `roll` alone leaves it in -- no uniform was drawn (an unconditional draw moves every
    whole-Ob hash; this is the arm that sees it). The record is the identity there: `settled_margin ==
    net - ob`.
  * A FRACTIONAL OB DRAWS EXACTLY ONE UNIFORM, the act's own: the generator ends one `random()` later,
    and the settled margin is `floor(net - ob)` plus one when that uniform is under the fraction.
  * THE RECORD'S OWN FIELDS ARE UNCHANGED: `net`, `ob` and `pool` are the entry's (S27.4 and every reader
    of the pair see what they saw); only `settled_margin` is added.
  * `degree_of` GRADES THE SETTLED MARGIN when the record carries one (against a zero obstacle) and the
    pair as before when it does not.
  * THE DEALT DISTRIBUTION IS `odds_of`: 20,000 real `resolve` calls at a fractional Ob, graded by
    `degree_of`, agree with `odds_of` within three standard errors, and differ from the integer
    collapse a fractional Ob had before (Ob 1.5 dealt exactly Ob 2's odds).
"""
from __future__ import annotations

import math
import random

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL

from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act
from .test_odds_of import _within_3se
from .test_sc01_obstacle_ceiling import _module

KEY = "copying"


def _world(opposition):
    """A speaker at pool 4 against a hearer whose score is `opposition`: the obstacle is score/2 (under the
    shipped ceiling of 2), so 3 gives 1.5 and 4 gives 2.0."""
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    # roster-exempt: TEST FIXTURE capabilities -- a speaker at pool 4 and a hearer scoring `opposition`.
    w.persons["p_low"].capability = {KEY: 4}
    w.persons["p_mid"].capability = {KEY: opposition}
    return w


def _resolve(w, rng):
    return sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid", rng=rng)


def _reference_state(w, seed, extra_draws):
    """The generator's state after the module's own roll, then `extra_draws` uniforms."""
    inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid")
    rng = random.Random(seed)
    _module().roll(inp, rng)
    for _ in range(extra_draws):
        rng.random()
    return rng.getstate()


def test_a_whole_ob_roll_draws_nothing_and_is_the_identity():
    w = _world(4)                                     # Ob 2.0
    checked = 0
    for seed in range(40):
        rng = random.Random(seed)
        out = _resolve(w, rng)
        assert out["status"] == "RESOLVED" and out["ob"] == 2.0, out
        assert rng.getstate() == _reference_state(w, seed, 0), seed
        assert out["settled_margin"] == out["net"] - out["ob"] and isinstance(out["settled_margin"], int)
        checked += 1
    assert checked == 40


def test_a_fractional_ob_draws_exactly_one_uniform_and_settles_by_it():
    w = _world(3)                                     # Ob 1.5
    paid = unpaid = 0
    for seed in range(60):
        rng = random.Random(seed)
        out = _resolve(w, rng)
        assert out["ob"] == 1.5 and out["pool"] == 4, out
        assert rng.getstate() == _reference_state(w, seed, 1), seed          # one uniform, the act's own
        ref = random.Random(seed)
        _module().roll(sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid"), ref)
        u = ref.random()
        floor = math.floor(out["net"] - out["ob"])
        assert out["settled_margin"] == floor + (1 if u < 0.5 else 0), (seed, out, u)
        paid += u < 0.5
        unpaid += u >= 0.5
    assert paid > 10 and unpaid > 10, (paid, unpaid)         # both arms of the draw were observed


def test_the_records_own_fields_are_the_entrys_and_only_one_is_added():
    w = _world(3)
    out = _resolve(w, random.Random(5))
    inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid")
    margin = _module().roll(inp, random.Random(5))
    assert (out["net"], out["ob"], out["pool"]) == (margin.net, margin.ob, inp.pool)
    assert set(out) == {"status", "module", "resolver", "pool", "net", "ob", "leverage", "settled_margin"}


def test_degree_of_grades_the_settled_margin_when_present_and_the_pair_otherwise():
    pair = dict(status="RESOLVED", net=3.0, ob=1.5)           # net - ob = 1.5: Success on the pair
    assert ladder.degree_of(pair) == "Success"
    assert ladder.degree_of(dict(pair, settled_margin=0)) == "Partial"
    assert ladder.degree_of(dict(pair, settled_margin=-1)) == "Failure"
    assert ladder.degree_of(dict(pair, settled_margin=3)) == "Overwhelming"


def test_the_dealt_distribution_is_odds_of_and_a_fraction_of_a_step_is_worth_its_fraction():
    w = _world(3)
    act = Act(id="a:p_low:p_mid", actor="p_low", verb="tell", payload={"to": "p_mid"})
    odds = sigma.odds_of(w, act)
    whole = sigma.odds_of(_world(4), act)                      # Ob 2.0
    assert odds is not None and whole is not None and odds != whole
    assert odds[0] < whole[0]                                  # Ob 1.5 is easier than Ob 2.0 at last
    n = 20_000
    rng = random.Random(11)
    labels = {v: k for k, v in DEGREE_LABEL.items()}
    tally = [0, 0, 0, 0]
    for _ in range(n):
        tally[DEGREE_ORDINAL[labels[ladder.degree_of(_resolve(w, rng))]]] += 1
    _within_3se(odds, tally, n)
