"""B05.02 at the seam -- `seam/wrappers/sigma.py::resolve` carries the REAL margin on the record and draws
nothing beyond the module's own roll, and `seam/ladder.py::degree_of` grades that margin once at the ladder.
(Re-pointed from CP-T01-04's `settled_margin`: no fraction of a margin is paid by a second draw any more; the
record keeps the key's name, `settled_margin`, and it is `net - ob`, unrounded.)

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * A WHOLE OR A FRACTIONAL OB DRAWS NOTHING BEYOND THE ROLL: after `resolve` the act's generator is in exactly
    the state the module's `roll` alone leaves it in (a second draw at a fractional Ob, as the fraction rule
    made, moves every hash behind it; this is the arm that sees it).
  * THE RECORD'S MARGIN IS REAL: `settled_margin == net - ob`, a float that is not rounded to a whole.
  * THE RECORD'S OWN FIELDS ARE UNCHANGED: `net`, `ob` and `pool` are the entry's (S27.4 and every reader
    of the pair see what they saw); only `settled_margin` is added.
  * `degree_of` GRADES THE MARGIN when the record carries one (against a zero obstacle) and the pair as before
    when it does not, and the two agree on a record the host wrote (the ladder quantises once).
  * THE DEALT DISTRIBUTION IS `odds_of`: 20,000 real `resolve` calls at a fractional Ob, graded by
    `degree_of`, agree with `odds_of` within three standard errors, and a fractional Ob deals a chance of its own.
"""
from __future__ import annotations

import random

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL

from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act
from ..data.verbs import VERB_TABLE
from .test_odds_of import _within_3se
from .test_sc01_obstacle_ceiling import _module

KEY = "copying"


def _world(opposition):
    """A speaker at pool 4 against a hearer whose score is `opposition`: the obstacle is score/2 (under the
    shipped ceiling of 2), so 3 gives 1.5 and 4 gives 2.0."""
    # B05.14: read on the form's score/2 ALONE: no difficulty (every level sized 0) and a hearer holding his resisting attribute at 0, so
    # the obstacle is `0.5 x score`. This file is about how the margin is carried at a whole and a fractional Ob, not about the terms
    # (`test_obstacle_form.py`'s).
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("difficulty_ob", {k: 0 for k in DEFAULT_FIXTURES.get("difficulty_ob")}))
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    # roster-exempt: TEST FIXTURE capabilities -- a speaker at pool 4 and a hearer scoring `opposition`.
    w.persons["p_low"].capability = {KEY: 4}
    w.persons["p_mid"].attributes = {VERB_TABLE["tell"].opposed_attribute: 0}
    w.persons["p_mid"].capability = {KEY: opposition}
    return w


def _resolve(w, rng):
    return sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid", rng=rng)


def _reference_state(w, seed):
    """The generator's state after the module's own roll alone."""
    inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid")
    rng = random.Random(seed)
    _module().roll(inp, rng)
    return rng.getstate()


def test_resolve_draws_nothing_beyond_the_roll_at_a_whole_or_a_fractional_ob():
    checked = 0
    for opposition, ob in ((4, 2.0), (3, 1.5)):
        w = _world(opposition)
        for seed in range(40):
            rng = random.Random(seed)
            out = _resolve(w, rng)
            assert out["status"] == "RESOLVED" and out["ob"] == ob and out["pool"] == 4, out
            assert rng.getstate() == _reference_state(w, seed), (ob, seed)
            checked += 1
    assert checked == 80


def test_the_records_margin_is_the_real_margin_not_a_whole():
    w = _world(3)                                     # Ob 1.5
    fractional = 0
    for seed in range(40):
        out = _resolve(w, random.Random(seed))
        assert out["settled_margin"] == out["net"] - out["ob"], out
        fractional += out["settled_margin"] != round(out["settled_margin"])
    assert fractional >= 30, fractional               # the margin is a real: a whole margin is the exception


def test_the_records_own_fields_are_the_entrys_and_only_one_is_added():
    w = _world(3)
    out = _resolve(w, random.Random(5))
    inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid")
    margin = _module().roll(inp, random.Random(5))
    assert (out["net"], out["ob"], out["pool"], out["terms"]) == (margin.net, margin.ob, inp.pool, margin.terms)
    # B05.14: AND `terms`, every term of the obstacle named on the record (`Margin.terms`, the entry's own; lane A's `ob_terms` is replaced)
    # B04.08: AND `fed_by`, the `social_roll` rows that fed the roll (`resolve`'s record, never an `Event` field, D-U1-06)
    assert set(out) == {"status", "module", "resolver", "pool", "net", "ob", "leverage", "settled_margin", "terms", "fed_by"}


def test_degree_of_grades_the_margin_when_present_and_the_pair_otherwise():
    pair = dict(status="RESOLVED", net=3.0, ob=1.5)           # net - ob = 1.5: Success on the pair
    assert ladder.degree_of(pair) == "Success"
    assert ladder.degree_of(dict(pair, settled_margin=0)) == "Partial"
    assert ladder.degree_of(dict(pair, settled_margin=-1)) == "Failure"
    assert ladder.degree_of(dict(pair, settled_margin=3)) == "Overwhelming"
    assert ladder.degree_of(dict(pair, settled_margin=0.9996)) == "Success"      # quantised once, at the ladder: 1000 milli
    assert ladder.degree_of(dict(pair, settled_margin=-0.0004)) == "Partial"     # -0.4 milli rounds to 0
    w = _world(3)
    for seed in range(40):                                    # the host's own record: both readings agree
        out = _resolve(w, random.Random(seed))
        assert ladder.degree_of(out) == ladder.degree_of({k: out[k] for k in ("status", "net", "ob")}), out


def test_the_dealt_distribution_is_odds_of_and_a_fractional_ob_deals_its_own_chance():
    w = _world(3)
    act = Act(id="a:p_low:p_mid", actor="p_low", verb="tell", payload={"to": "p_mid"})
    odds = sigma.odds_of(w, act)
    whole = sigma.odds_of(_world(4), act)                      # Ob 2.0
    assert odds is not None and whole is not None and odds != whole
    assert odds[0] < whole[0]                                  # Ob 1.5 is easier than Ob 2.0
    n = 20_000
    rng = random.Random(11)
    labels = {v: k for k, v in DEGREE_LABEL.items()}
    tally = [0, 0, 0, 0]
    for _ in range(n):
        tally[DEGREE_ORDINAL[labels[ladder.degree_of(_resolve(w, rng))]]] += 1
    _within_3se(odds, tally, n)
