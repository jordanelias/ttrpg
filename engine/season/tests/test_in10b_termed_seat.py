"""IN-10 (b) (#453 §7.2 `:1382`, §9.6 `:2071`) -- `confer` + `Tenure.term`: a seat-hold carrying a
term (regency, the term-limited seat), which opens, and MATURES at the MATTER barrier the term names
(`loop/matter.py`'s term branch, gate basis `T-n`), leaving the seat vacant.

The edits are `_eff_confer` and the row's `writes:` (`Tenure.term`); the term is the opening act's
declaration (`loop/effects_governance.py::_declared_term`, the payload's `term`, a length in seasons)
[ASSUMPTION; medium; Jordan to correct]. A computed `confer` declares none and opens an untermed hold.

  (1) the effect: a declared term rides the opened hold as `Term(tick + n, act)`; none declared, none
      carried; a malformed one raises (a caller defect);
  (2) THE EXIT, in seeded seasons through the real `SeasonDriver`: a termed conferral opens, matures
      at its tick under `T-n` citing the act that wound it, and the seat is left vacant -- the
      control, the same conferral untermed, still holds after the same seasons. FALSIFIER: a termed
      hold that never matures -> (b) not built.

MUTATION, run at the build: `term=_declared_term(w, a)` dropped from `_eff_confer` reddens (1) and (2).
"""
import pytest

from engine.season.data.verbs import VERB_TABLE
from engine.season.gaps import InstrumentDefect
from engine.season.harness import probes as P
from engine.season.loop.effects import EFFECTS
from engine.season.state.carriers import Act

from .test_g3_not_yours import _gov_world, _hold

SEAT, CONFERRER, VIA, CONFEREE = "off_reeve", "p_king", "off_crown", "p_mid"


def _act(term=None, key="cf_in10b"):
    payload = {"subject": SEAT, "to": CONFEREE}
    if term is not None:
        payload["term"] = term
    return Act(id=key, actor=CONFERRER, verb="confer", payload=payload, via=VIA)


def _opened(ch):
    return next(s.ref[1] for s in ch.subjects if s.earns == "tenure.opened")


# (1) ----------------------------------------------------------------------------------------------

def test_in10b_the_row_declares_the_term_it_writes():
    assert VERB_TABLE["confer"].writes == ("Tenure.until", "Tenure.since", "Tenure.term")


def test_in10b_a_declared_term_rides_the_opened_hold_and_none_otherwise():
    w, _ = _gov_world()
    t = _opened(EFFECTS["confer"](w, _act(term=2)))
    assert t.term is not None and (t.term.matures_at, t.term.declared_by) == (w.tick + 2, "cf_in10b")
    assert _opened(EFFECTS["confer"](w, _act())).term is None
    for bad in (0, -1, "2", 1.5, True):
        with pytest.raises(InstrumentDefect, match="positive whole number"):
            EFFECTS["confer"](w, _act(term=bad))


# (2) THE EXIT, IN SEEDED SEASONS -----------------------------------------------------------------

def _seasons(term, n=3):
    """`n` seasons of the governance world through `SeasonDriver.season`; the King confers `off_reeve`
    on `p_mid` (through `off_crown`) in the FIRST season only. Returns the world, the act's id and
    the seat's hold after the first season."""
    w, _ = _gov_world()
    start = w.tick
    acts = {}

    def choose(p, v, s, ask_budget):
        if p.id == CONFERRER and w.tick == start:
            a = P.Act_(w, p, "confer", via=VIA,
                       payload={"subject": SEAT, "to": CONFEREE,
                                **({"term": term} if term is not None else {})})
            acts["confer"] = a.id
            return [a]
        return []
    d = P._run_d(w, choose, n=1)
    first = _hold(w, SEAT)
    for _ in range(n - 1):
        d.season(choose, question=None, subsistence=P.SUBSIST)
    return w, acts["confer"], first


def test_in10b_a_termed_seat_opens_and_matures_and_the_untermed_control_does_not():
    w, aid, first = _seasons(term=1)
    assert first is not None and first.subject == CONFEREE, "the termed conferral did not open"
    assert first.term is not None and first.term.declared_by == aid
    assert not first.live and first.until == first.term.matures_at, (
        "a termed hold that never matures: (b) not built", first)
    assert _hold(w, SEAT) is None, "the seat is not left vacant"
    lapse = [e for e in w.log if e.kind == "tenure.closed" and e.causes == [aid]]
    assert lapse, "no MATTER closure cites the act that wound the term (AX-5)"
    # CONTROL: the same conferral, untermed, still holds after the same seasons.
    wc, _, firstc = _seasons(term=None)
    assert firstc is not None and firstc.term is None and firstc.live
    assert _hold(wc, SEAT) is firstc
