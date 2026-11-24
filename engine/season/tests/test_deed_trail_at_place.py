"""B11.59 (CP-T06-01 with `16_PESSIMIST_FI_C` edits 1-2) -- A DEED THAT WRITES A PLACE, AN ALIAS OR A PERSON LEAVES A TRAIL.

`rosters.yaml: covert_kinds` names the deed kinds an inquiry can uncover for someone no witness channel admitted
(`epistemic.trail_of`). Three tests, each the FI_C gate's, over a hand-built world (a seeded run reaches none of them: the
`sabotage` row forms on no Site in the realm, and no graded inquiry forms on a killing):

  * `test_examine_finds_site_damaged` -- the SITE side, GREEN here: a saboteur damages a Site with nobody at its place, a
    second man `examine`s it and holds the deed. CP-T06-01's two-band reading is `test_fi03_trail.py`'s.
  * `test_bystander_holds_exists_person_zero` -- GREEN since B11.60: a witness of a killing holds the victim ended
    (`exists:Person` 0), not only `person.died`.
  * `test_surveil_at_the_place_of_a_killing_finds_the_deed_at_partial` -- EXPECTED RED UNTIL B11.63: the place side. `trail_of`
    reads the Events that wrote or were anchored on the inquiry's subject, and a place is neither for a killing.
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..loop.driver import SeasonDriver, mint_token
from ..seam.contest import Resolution
from ..state.carriers import Act
from ._scar_helpers import party_state
from .test_fi03_trail import HAND_BANDS, examine_at, sabotaged_site, step, tiny

pytestmark = pytest.mark.flat_fold

SABOTEUR, FINDER, WITNESS, KILLER, VICTIM = "p_other", "p_high", "p_low", "p_other", "p_mid"
# [JUSTIFIED: a test-fixture search bound, not a game value -- the act ids tried for a band; asserted reached]
SWEEP = 60


def held(w, pid, predicate):
    return {c.subject for c in w.persons[pid].ledger if c.predicate == predicate and c.value is True}


def test_examine_finds_site_damaged():
    """The saboteur's deed reaches the finder by no channel (control: he holds no `site.damaged` claim before the
    `examine`). At a band showing the hand he holds the deed under the saboteur and the Site, `inferred`."""
    w, _ = sabotaged_site()
    assert held(w, FINDER, "site.damaged") == set(), "the finder was admitted to the deed before any inquiry"
    for n in range(SWEEP):
        w, e = examine_at(n)
        if e.degree in HAND_BANDS:
            break
    else:
        raise AssertionError(f"{SWEEP} act ids drew no band showing the hand")
    assert held(w, FINDER, "site.damaged") == {SABOTEUR, "site_x"}, held(w, FINDER, "site.damaged")
    assert {c.source for c in w.persons[FINDER].ledger if c.predicate == "site.damaged"} == {"inferred"}


def killing():
    """The killer fells the victim at `Hh`, where the witness also stands (`tiny_world`'s hearth holds p_low, p_mid and
    p_other); a constructed `Felled` through the real fold, then the real WITNESS. Returns `(w, d)`; the finder stands at `S`."""
    w = tiny()
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    res = Resolution("Felled", {"wound_state": {VICTIM: party_state(felled=True, left=0), KILLER: party_state()}})
    out = d._fold(w, mint_token(w, WriteClass.ACTS), Act(id="kill", actor=KILLER, verb="fight", payload={"subject": VICTIM}), res)
    w.log.extend(out)
    assert VICTIM not in w.persons and "person.died" in [e.kind for e in out], "fixture: the victim did not die"
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return w, d


def test_bystander_holds_exists_person_zero():
    """B11.60. The witness stood in the room, holds the death, and holds the victim ended: `(victim,
    exists:Person, 0)` (the same cell the fold asks, R-02). He also holds `person.died`, asserted first so the red is the
    missing reading and not a fan that admitted nobody."""
    w, _ = killing()
    assert VICTIM in held(w, WITNESS, "person.died"), "the bystander was not admitted to the killing"
    ended = [c for c in w.persons[WITNESS].ledger if c.subject == VICTIM and c.predicate == "exists:Person"]
    assert [c.value for c in ended] == [0], ended


def test_surveil_at_the_place_of_a_killing_finds_the_deed_at_partial():
    """EXPECTED RED UNTIL B11.63. A man who was not in the room walks to `Hh` and `surveil`s it; at a Partial band he holds the
    victim dead (`finding_terms` Partial: the deed, not the hand), under the victim and not under the killer."""
    for n in range(SWEEP):
        w, d = killing()
        assert held(w, FINDER, "person.died") == set(), "the finder was admitted to the killing before any inquiry"
        assert [e.kind for e in step(w, d, Act(id="mv", actor=FINDER, verb="move", payload={"to": "Hh"}))] == ["travel.moved"]
        (e,) = step(w, d, Act(id=f"sv_{n}", actor=FINDER, verb="surveil", payload={"subject": "Hh"}))
        if e.degree == "Partial":
            break
    else:
        raise AssertionError(f"{SWEEP} act ids drew no Partial band")
    assert held(w, FINDER, "person.died") == {VICTIM}, held(w, FINDER, "person.died")
