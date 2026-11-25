"""B11.74 (`19_LACUNA_conclusion_is_a_committed_assertion.md` R-19-03; FRES §7 (3)): A PROPOSITION CARRIES ITS SUPPORT.

`utter` commits a conclusion (a `concluded:<kind>` cell, B11.73's deposit to its maker) and the act carries `cites`, the claim ids and
Record ids the utterer cited; `_eff_utter` stores them as `Proposition.support`, and a cite he does not hold is refused before anything is
written. `HOLDS` is the mood a conclusion is uttered in. No computed act forms `utter` with a cite (typed `utter` is B25's), so these plant
the act and fold it through the real driver.
"""
from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Claim, Record, Tenure

UTTERER, OTHER = "p_low", "p_mid"
SUSPECT, VICTIM = "p_other", "p_king"
CELL = "concluded:person.died"
_CONTENT = {"terms": "prop_x", "to": (OTHER,), "from": UTTERER}


def _world():
    """A utterer who holds one claim of his own and one Record on a live `hold`; a second person holds a claim and a Record he does not."""
    w = P.tiny_world()
    w.persons[UTTERER].ledger.append(Claim("c_mine", UTTERER, VICTIM, "person.died", True, 0, "firsthand", 100, "own"))
    w.persons[OTHER].ledger.append(Claim("c_his", OTHER, VICTIM, "person.died", True, 0, "firsthand", 100, "own"))
    w.records["r_mine"] = Record("r_mine", "Hh", "petition", subject_matter=_CONTENT)
    w.records["r_his"] = Record("r_his", "Hh", "petition", subject_matter=_CONTENT)
    w.add_tenure(Tenure("t_hold_mine", UTTERER, "r_mine", "hold", since=0))
    w.add_tenure(Tenure("t_hold_his", OTHER, "r_his", "hold", since=0))
    return w


def _utter(w, aid: str, cites):
    """Fold one planted `utter` of the conclusion `(VICTIM, CELL, SUSPECT)` carrying `cites`; the Events the act caused."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    payload = {"proposition": f"prop_{aid}", "mood": "HOLDS", "subject": VICTIM, "predicate": CELL, "value": SUSPECT}
    if cites is not None:
        payload["cites"] = cites
    evs = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id=aid, actor=UTTERER, verb="utter", payload=payload)])
    return [e.kind for e in evs if e.causes and e.causes[0] == aid]


def test_a_conclusion_is_uttered_with_a_held_support():
    """A planted `utter` of the `concluded:` cell citing a claim and a Record he holds mints a Proposition whose `support` is exactly the cited
    ids, in the order cited; with no `cites` it is `()` (the control: the field is the act's, not a default made up). FALSIFIER: an effect that
    drops `cites` reads `()` on the first assert; one that stores the payload object reads a list, not a tuple, on the second."""
    w = _world()
    kinds = _utter(w, "u_held", ["c_mine", "r_mine"])
    assert "proposition.uttered" in kinds, kinds
    prop = w.propositions["prop_u_held"]
    assert prop.support == ("c_mine", "r_mine")
    assert isinstance(prop.support, tuple), "a Proposition is immutable: its support is a tuple, not the act's list"
    assert (prop.predicate, prop.value) == (CELL, SUSPECT)
    assert _utter(w, "u_bare", None) and w.propositions["prop_u_bare"].support == ()


def test_a_cite_the_utterer_does_not_hold_leaves_no_support():
    """A cite another person holds, and a cite nobody holds, each refuse the whole act at the fold: no Proposition, no `proposition.uttered`,
    no hold Tenure for the maker. The held-cite control in the same world is admitted, so the refusal observes the failure it excludes."""
    w = _world()
    for aid, cites in (("u_his_claim", ["c_mine", "c_his"]), ("u_his_record", ["r_his"]), ("u_nothing", ["c_nowhere"])):
        kinds = _utter(w, aid, cites)
        assert "act.refused" in kinds and "proposition.uttered" not in kinds, (aid, kinds)
        assert f"prop_{aid}" not in w.propositions, aid
        assert not [t for t in w.persons[UTTERER].tenures if t.object == f"prop_{aid}"], aid
    assert "proposition.uttered" in _utter(w, "u_control", ["c_mine"])
    assert w.propositions["prop_u_control"].support == ("c_mine",)
