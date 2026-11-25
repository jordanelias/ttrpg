"""The one place a test folds a seat turnover at a writing band instead of drawing it.

B21.14 (BIND_C commit C3): `confer`, `revoke` and `succeed` contest the prize `a seat` (as `establish` has since B21.09), so the
seam's draw decides their band and a Failure writes nothing. A test whose question is the turnover's FOLD -- its admission, the
write gate, the effect, what it emits and who hears it -- and not the draw asks for `seat_at_success`: every act contesting `a seat`
is folded at Success through the real `_fold` (its own `_admits`, the gate, the effect), the shape B21.09 gave the founding's
helpers (`test_cr25_computed_establish._act`). Every other contest is drawn as shipped. A test whose question is the draw
(`test_vb_c_turnover.py::test_c3_confer_revoke_succeed_band_on_a_hand_built_world`, the realm pins) must NOT use this. Name the
fixture at the site; the reason is here.

B21.56 (BIND_D commit D3): `issue` contests `a standing` against its executor, and the band is written into the writ (`force`) and
picks its kind (`dispensation.ignored` at Failure). A test whose question is the writ's fold -- its clauses, the mint, the content,
who comes to hold or read it -- and not the draw asks for `writ_at_success`: every `issue` is folded at Success through the real
`_fold`. Keyed on the VERB, not the prize: `a standing` is also `tell`'s and `arrest`'s, which stay drawn. The draw's own test is
`test_vb_d_orders.py::test_d3_a_writ_is_minted_at_every_band_with_its_force`, which must NOT use it.
"""
import pytest

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.season.data.verbs import VERB_TABLE
from engine.season.loop.driver import SeasonDriver
from engine.season.seam import Resolution

SEAT = VERB_TABLE["confer"].contests          # the prize, read off the row (`a seat`), never spelt here
assert SEAT and VERB_TABLE["revoke"].contests == SEAT == VERB_TABLE["succeed"].contests, SEAT


@pytest.fixture
def seat_at_success(monkeypatch):
    drawn = SeasonDriver._contest

    def at_success(self, w, token, a, contests, contest_max_depth, host=None):
        if contests and contests[0] == SEAT:
            return self._fold(w, token, a, Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))
        return drawn(self, w, token, a, contests, contest_max_depth, host)

    monkeypatch.setattr(SeasonDriver, "_contest", at_success)


WRIT = "issue"
assert VERB_TABLE[WRIT].contests, WRIT


@pytest.fixture
def writ_at_success(monkeypatch):
    drawn = SeasonDriver._contest

    def at_success(self, w, token, a, contests, contest_max_depth, host=None):
        if a.verb == WRIT:
            return self._fold(w, token, a, Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))
        return drawn(self, w, token, a, contests, contest_max_depth, host)

    monkeypatch.setattr(SeasonDriver, "_contest", at_success)
