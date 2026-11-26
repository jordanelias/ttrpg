"""B24.34 (ARCS item 4, `12_ARCS_cited_evidence`): WHO HOLDS A RECORD CAN BE FOUND OUT.

A graded `research` of a Record deposits `(holder, holds, record)` to the finder at every finding band (`rosters.yaml: look_reads` `holds`, listed by
`finding_terms`), read off the live `hold` Tenure a Record's holder is (`queries/world_q.py::WorldReader.look`); a `Failure` deposits none. A hand-built world,
the act folded at a band the test names and then witnessed (`test_playable_inquiry._look`), so what lands is what the WITNESS barrier deposited.
"""
from __future__ import annotations

import pytest

from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries import world_q
from ..state.carriers import Act, Record, Tenure
from .test_playable_inquiry import _look

FINDER, HOLDER, NEXT = "p_low", "p_mid", "p_other"      # all three stand at `Hh`, where a `research` must be present
REC = "rec_b2434"
FOUND_BANDS = ("Overwhelming", "Success", "Partial")


def _world():
    """`tiny_world` where `p_mid` holds a petition (`REC`) and the finder, `p_low`, holds nothing."""
    w = P.tiny_world()
    w.records[REC] = Record(REC, "Hh", "petition", subject_matter={"terms": "prop_x", "to": (HOLDER, NEXT), "from": HOLDER})
    w.add_tenure(Tenure("t_hold_rec", HOLDER, REC, "hold", since=0))
    return w, SeasonDriver(w)


def _research(w, d, band, actor=FINDER):
    return _look(w, d, Act(id=f"a_research_{actor}_{band}", actor=actor, verb="research", payload={"subject": REC}), band)


def _holds(w, pid=FINDER):
    """`{(holder, record)}` of the `holds` claims `pid` holds."""
    return {(c.subject, c.value) for c in w.persons[pid].ledger if c.predicate == "holds"}


@pytest.mark.parametrize("band", FOUND_BANDS)
def test_an_inquiry_finds_who_holds_the_record(band):
    """A `research` that grades at a finding band leaves the finder a `holds` claim about the holder, at `Partial` too (ARCS: `Partial` or better).
    FALSIFIER: a deposit keyed to the wrong person, or one `finding_terms` withholds at a band, leaves the set short. CONTROL: the finder held none before."""
    w, d = _world()
    assert not _holds(w), "control: the finder holds no `holds` claim before the look"
    _research(w, d, band)
    assert _holds(w) == {(HOLDER, REC)}, (band, _holds(w))


def test_a_given_away_record_names_the_new_holder():
    """The holder gives the Record away (`give`, folded through the fold's own gate); the finder's look afterwards names the new holder and not the old.
    CONTROL: the same look before the gift names the old holder, so the claim is read off the live Tenure and not remembered."""
    w, d = _world()
    _research(w, d, "Success")
    assert _holds(w) == {(HOLDER, REC)}, "control: before the gift"
    given = _look(w, d, Act(id="a_give", actor=HOLDER, verb="give", payload={"subject": REC, "to": NEXT}), "Success")
    assert [e.kind for e in given] == ["record.given"], [e.kind for e in given]
    assert world_q.hold_force(w, REC).subject == NEXT
    w.persons[FINDER].ledger.clear()
    _research(w, d, "Success", actor=FINDER)
    assert _holds(w) == {(NEXT, REC)}, _holds(w)


def test_a_failed_inquiry_deposits_no_holds_claim():
    """At `Failure` (`finding.none`) the finder holds no `holds` claim. CONTROL: the same act at `Success` deposits one, so the empty set could have been full."""
    w, d = _world()
    out = _research(w, d, "Failure")
    assert [e.kind for e in out] == ["finding.none"], [e.kind for e in out]
    assert not _holds(w)
    w2, d2 = _world()
    _research(w2, d2, "Success")
    assert _holds(w2)


def test_a_holder_who_looks_at_what_he_holds_is_taught_no_claim_about_himself():
    """`p_mid` researches the Record he holds: his own look names him, and a look teaches a man no claim about himself. CONTROL: the look is no refusal and DID teach him
    something (the finding and what it read of the Record), so the empty `holds` set is the look's rule and not a look that did nothing."""
    w, d = _world()
    before = {c.id for c in w.persons[HOLDER].ledger}
    out = _research(w, d, "Success", actor=HOLDER)
    assert [e.kind for e in out] == ["finding.made"], [e.kind for e in out]
    taught = {c.predicate for c in w.persons[HOLDER].ledger if c.id not in before}
    assert "finding.made" in taught and "content:petition" in taught, taught
    assert not _holds(w, HOLDER), _holds(w, HOLDER)
