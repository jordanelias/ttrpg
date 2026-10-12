"""`rung_above_in_holdings` -- JORDAN, 2026-10-12: a duchy's title can be stripped only where the duchy
is a HOLDING of the monarch (*"it's not ONLY based on hierarchy of rungs, but also where it is placed
in holdings"*); a duchy that is nobody's holding has a head who is the highest authority and resigns.

THE FALSIFIER (§0.1 pt 3): a King seated on the rung above a Duke's duchy, who does NOT hold that
duchy, may not strip the Duke; the same King once the duchy is one of his holdings, may. The MUTATION
is the `in_holdings` conjunct deleted from `state/gate.py::seated_on_the_rung_above_in_holdings` -- the
first test goes red on it (run, recorded in the commit's receipt).

THE CONTROLS, each of which the rule must not move: the structure (a seat NOT on the rung above that
holds the duchy still cannot strip), whose holdings (another person's hold is not the actor's), a live
hold (a closed one is not a holding), and the OTHER basis (`rung_above_same_faction` is unchanged, and
differs from this one on exactly the faction clause, which this basis does not ask).

NOT HERE: the realm contains no holding of a duchy (measured in the last test), so no computed
`revoke` strips a Duke in `build_realm(0)`; that is content (R-05), not this rule.
"""
from ..harness import probes as P
from ..harness.populated import build_realm
from ..loop import predicates as _preds
from ..state.carriers import Act, Office, Person, Tenure
from ..state.gate import may_revoke
from ..loop.predicates import in_holdings

_HOLDINGS, _FACTION = "rung_above_in_holdings", "rung_above_same_faction"
_GRANTS = ["issue", "confer", "revoke"]
DUKE = "off_duke"            # tiny_world's Duke of D, a Crown seat held by `p_high`


def _world(basis=_HOLDINGS, king_faction="Crown"):
    """`tiny_world` (R ⊃ D ⊃ S ⊃ Hh), plus `p_king` on `off_crown` (a King at R, the rung directly
    above D) and `p_mayor` on `off_mayor` (a Mayor at S, NOT the rung above D)."""
    w = P.tiny_world()
    w.offices[DUKE].revocation = basis
    for pid, oid, post, rung, fac in (("p_king", "off_crown", "King", "R", king_faction),
                                      ("p_mayor", "off_mayor", "Mayor", "S", "Crown")):
        w.persons[pid] = Person(pid, pid)
        w.offices[oid] = Office(oid, post, rung, list(_GRANTS), faction=fac,
                                conferral="appointed", revocation=None)
        w.add_tenure(Tenure(f"t_{oid}", pid, oid, "hold", 0))
    return w


def _hold(w, pid, rung="D", until=None):
    w.add_tenure(Tenure(f"h_{pid}_{rung}", pid, rung, "hold", 0, until))


def _may(w, pid="p_king", via="off_crown"):
    return may_revoke(w, pid, via, w.offices[DUKE])


def test_a_king_strips_a_duke_only_where_the_duchy_is_his_holding():
    w = _world()
    assert not in_holdings(w, "p_king", "D")
    assert _may(w) is False, "the rung above alone stripped a Duke whose duchy is nobody's holding"
    _hold(w, "p_king")
    assert in_holdings(w, "p_king", "D")
    assert _may(w) is True


def test_the_faction_clause_is_not_asked_by_the_holdings_basis_and_is_by_the_other():
    w = _world(king_faction="Hafenmark")
    _hold(w, "p_king")
    assert _may(w) is True                                    # a holding is strippable whatever its faction
    w.offices[DUKE].revocation = _FACTION
    assert _may(w) is False                                    # the old basis still asks it, unchanged


def test_the_holdings_basis_still_needs_the_seat_on_the_rung_above():
    w = _world()
    _hold(w, "p_mayor")                                        # holds D, but sits at S, below it
    assert in_holdings(w, "p_mayor", "D")
    assert _may(w, "p_mayor", "off_mayor") is False
    _hold(w, "p_king")
    assert _may(w) is True                                     # the control: the King, same holdings


def test_the_holding_must_be_the_actors_own_and_live():
    w = _world()
    _hold(w, "p_mayor")                                        # somebody else holds D
    assert _may(w) is False
    _hold(w, "p_king", until=0)                                # a closed hold is no holding
    assert not in_holdings(w, "p_king", "D") and _may(w) is False


def test_the_fold_admits_what_the_gate_does():
    """`_req_revoke` asks the same predicate with the `office` operand a hand-built act carries."""
    w = _world()
    act = Act(id="a1", actor="p_king", verb="revoke", via="off_crown",
              payload={"subject": DUKE, "office": DUKE})
    assert not _preds._req_revoke(w, act)
    _hold(w, "p_king")
    assert _preds._req_revoke(w, act)


def test_as_built_no_duchy_is_anyones_holding_so_no_duke_is_strippable():
    """The measured premise of the plan's 'content is a choice' line, counted (§0.1 pt 2): the two duchy
    heads declare this basis and `in_holdings` is False for every person over every duchy rung."""
    w = build_realm(0)
    heads = [o for o in w.offices.values() if o.revocation == _HOLDINGS]
    assert sorted(o.post for o in heads) == ["Duchess", "Duke"], heads
    duchies = [r for r in w.rungs if r.startswith("duchy")]
    checked = 0
    for pid in w.persons:
        for rid in duchies:
            checked += 1
            assert not in_holdings(w, pid, rid), (pid, rid)
    assert checked == len(w.persons) * len(duchies) and checked > 0
