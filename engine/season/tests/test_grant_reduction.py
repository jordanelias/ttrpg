"""B21.69 (`IS-B3-FA-07`, A-105): A REDUCTION OF A SITTING HOLDER'S GRANT IS A REVOCATION, DRAWN AGAINST THE TWO FACTIONS' POWER.

One owner for every revocation: `revoke` (with its optional `keeps`, the acts the holder keeps) is the verb and the draw, the write gate's `T-o`
(`state/gate.py::tenure_write_basis`) is the basis for a re-stamp that drops an act, and `establish` refuses a re-stamp that narrows a sitting
grant. The roll's `faction_power` term (`faction_power_step`, shipped 0) prices the holder's faction against the host's (`faction_q.weight`).
The hand-built world is `test_g3_not_yours._gov_world`: `p_king` on `off_crown` above the duke `p_high` on `off_duke`.
"""
from __future__ import annotations

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.season.data.matrix import Step, WriteClass
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.seam import Resolution
from engine.season.state.carriers import Act, Tenure
from engine.season.state.gate import T_O, NotYours, tenure_write_basis

from .test_g3_not_yours import _gov_world, _hold
from .test_cr25_computed_establish import _act, _kinds, _seated_reeve, _world as _cr25_world
from .test_vb_c_turnover import KING, TARGET, VIA, _resolved

DUKE = "p_high"


def _duke_world():
    """`_gov_world`, with the duke's seat granting four acts (he holds the grant a re-stamp can cut)."""
    w, d = _gov_world()
    w.offices[TARGET].remit_acts = ["issue", "confer", "dispatch", "convene"]
    t = _hold(w, TARGET)
    w._grant_remit(t, force=True)
    assert t.granted_acts == ("issue", "confer", "dispatch", "convene"), t.granted_acts
    return w, d, t


def _restamp(w, t, grant, actor, via):
    """A bare gate write re-stamping `t`'s grant to `grant` (through `_grant_remit`, the one writer), as `actor` through `via`."""
    return w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: w._grant_remit(t, force=True, acts=grant),
                   record_kind="Tenure", fieldname="payload", driver="Act", actor=actor, via=via)


def test_a_gate_write_narrowing_a_sitting_grant_needs_a_revocation_basis():
    """A bare gate write that narrows a sitting `granted_acts` by an actor whose seat may FILL the duke's seat and may not REVOKE it (its basis
    declares none) is refused (`NotYours`; the basis is `None`); red before the clause, which admitted it as `CONFERRAL`. CONTROLS: the same seat
    WIDENING the grant is still admitted (`conferral`), and the narrowing under a basis the King's seat satisfies is `T-o`."""
    w, d, t = _duke_world()
    was = Tenure(t.id, t.subject, t.object, t.kind, t.since, t.until, degree=t.degree, payload=dict(t.payload), term=t.term)
    t.payload = {**t.payload, "remit_acts": ("issue", "confer")}
    assert tenure_write_basis(w, t, was, KING, VIA, frozenset()) == T_O, "the King's seat may revoke the duke's: a cut is `T-o`"
    w.offices[TARGET].revocation = None
    assert tenure_write_basis(w, t, was, KING, VIA, frozenset()) is None, "a cut by a seat that may fill and not revoke was admitted"
    t.payload = dict(was.payload)
    _restamp(w, t, ("issue", "confer", "dispatch", "convene", "revoke"), KING, VIA)          # CONTROL: a widening is the conferral basis's
    assert t.granted_acts == ("issue", "confer", "dispatch", "convene", "revoke"), t.granted_acts
    try:
        _restamp(w, t, ("issue",), KING, VIA)
    except NotYours:
        pass
    else:
        raise AssertionError("a bare cut by a seat that may not revoke was written")
    assert t.granted_acts == ("issue", "confer", "dispatch", "convene", "revoke"), "the refused cut was not put back"


def test_an_establish_that_narrows_a_sitting_grant_is_refused_and_a_revoke_with_keeps_carries_it():
    """`p_high` (the duke, via `off_duke`) over a reeve's seat his own seat may revoke (`rung_above_same_faction`) and fill: the `establish` that cuts
    the reeve's grant is refused even so (`establish.refused`, the grant as it was) -- it was admitted before, by `may_revoke`. CONTROLS: the same
    `establish` WIDENING executes; and the `revoke` carrying `keeps` cuts the grant through the real fold, the reeve still seated, no ban charged."""
    w, d = _cr25_world()
    payload = _seated_reeve(w, "rung_above_same_faction")
    w.offices["off_duke"].remit_acts.append("revoke")                    # the duke's seat revokes too (`remit:revoke`, eligibility)
    w._grant_remit(next(t for t in w.tenures if t.kind == "hold" and t.object == "off_duke"), force=True)
    [t] = [t for t in w.tenures if t.id == "t_reeve"]
    assert t.granted_acts == ("issue", "dispatch"), t.granted_acts
    assert _kinds(_act(w, d, "e_cut", "p_high", "off_duke", {**payload, "remit": ["issue"]})) == ["establish.reduces_grant"]      # B21.81: the `reduction is revocation` clause's kind
    assert t.granted_acts == ("issue", "dispatch"), "the refused cut re-stamped the grant"
    assert _kinds(_act(w, d, "e_add", "p_high", "off_duke", {**payload, "remit": ["issue", "dispatch", "convene"]})) \
        == ["remit.changed", "tenure.payload_set"], "the control widening did not execute"
    assert t.granted_acts == ("issue", "dispatch", "convene"), t.granted_acts
    rv = Act(id="rv_keeps", actor="p_high", verb="revoke", payload={"office": "off_reeve", "keeps": ["issue", "convene"]}, via="off_duke")
    assert _preds._req_revoke(w, rv)
    w.acts.append(rv)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), rv, Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))
    assert _kinds(out) == ["tenure.closed"], _kinds(out)
    assert t.live and t.granted_acts == ("issue", "convene"), (t.live, t.granted_acts)
    assert not [b for b in w.tenures if b.kind == "ban" and b.subject == "p_mid"], "a reduction charged the disposal"
    # `keeps` that names the whole grant (or more) cuts nothing: no write, `revoke.refused`; a `keeps` that is no list is refused at the precondition
    whole = Act(id="rv_whole", actor="p_high", verb="revoke", payload={"office": "off_reeve", "keeps": ["issue", "convene", "dispatch"]}, via="off_duke")
    w.acts.append(whole)
    assert _kinds(d._fold(w, mint_token(w, WriteClass.ACTS), whole, Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))) == ["revoke.refused"]
    assert t.granted_acts == ("issue", "convene")
    assert not _preds._req_revoke(w, Act(id="rv_bad", actor="p_high", verb="revoke", payload={"office": "off_reeve", "keeps": "issue"}, via="off_duke"))


def test_a_partial_establish_on_a_seated_office_never_cuts_the_sitting_grant():
    """B21 close: the Partial band narrows only a FOUNDING. The duke re-establishes the seated reeve's office (`issue`, `dispatch`) at Partial
    through the real fold: the same remit leaves the grant as it was (`establish.refused`, nothing moved) -- red before, when Partial cut the copy
    to its first half and the re-stamp wrote `("issue",)`, a revocation outside `revoke`; a WIDENING at Partial lands whole (before, the half
    copy equalled the grant and nothing moved)."""
    w, d = _cr25_world()
    payload = _seated_reeve(w, "rung_above_same_faction")
    [t] = [t for t in w.tenures if t.id == "t_reeve"]
    assert t.granted_acts == ("issue", "dispatch"), t.granted_acts

    def partial(aid, remit):
        act = Act(id=aid, actor="p_high", verb="establish", payload={**payload, "remit": remit}, via="off_duke")
        w.step = Step.RESOLVE
        w.acts.append(act)
        return _kinds(d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(DEGREE_LABEL[Degree.PARTIAL], {})))

    assert partial("e_same", ["issue", "dispatch"]) == ["establish.refused"]
    assert t.live and t.granted_acts == ("issue", "dispatch"), "a Partial establish cut the sitting grant"
    assert w.offices["off_reeve"].remit_acts == ["issue", "dispatch"], w.offices["off_reeve"].remit_acts
    assert partial("e_wide", ["issue", "dispatch", "convene"]) == ["remit.changed", "tenure.payload_set"]
    assert t.granted_acts == ("issue", "dispatch", "convene"), t.granted_acts


def _power_arm(seed: int, host_weight: int, holder_weight: int, same_faction: bool, step: float = 1):
    """`_gov_world` at world seed `seed`: the King (host, `off_crown`) and the duke each a member of a rostered faction, the duke of the King's own
    where `same_faction`; their `Person.weight` the members' weights (`faction_q.weight`); `faction_power_step` `step`. Returns `(world, driver)`."""
    w, d = _gov_world()
    w.world_seed = seed
    w.fixtures = w.fixtures.sweep("faction_power_step", step)
    w.offices[VIA].faction = "Valorsmark"                                 # the host seat's faction: a rostered one, as the commits name
    crown, other = "fac_valorsmark", "fac_varfell"
    w.add_tenure(Tenure("t_k_commit", KING, crown, "commit", 0))
    w.add_tenure(Tenure("t_d_commit", DUKE, crown if same_faction else other, "commit", 0))
    w.persons[KING].weight, w.persons[DUKE].weight = host_weight, holder_weight
    for p in (KING, DUKE):
        w.persons[p].attributes = {**(w.persons[p].attributes or {}), "attr.social.charisma": 3}
    return w, d


def _bands(host: int, holder: int, same: bool, step: float) -> list:
    """The band of the same reduction (`revoke` with `keeps`) at each of 200 world seeds."""
    out = []
    for seed in range(200):
        w, d = _power_arm(seed, host, holder, same, step)
        out.append(_resolved(w, d, Act(id=f"gp_{seed}", actor=KING, verb="revoke", via=VIA,
                                       payload={"office": TARGET, "keeps": ["issue"]}))[0])
    return out


def _share(bands: list) -> float:
    return sum(b != "Failure" for b in bands) / len(bands)


def test_a_foreign_holders_reduction_is_harder_against_a_stronger_faction():
    """200 seeds per arm of the same reduction, the duke's faction heavier than the King's and lighter: success shares (anything but Failure)
    strictly ordered, the heavier one lower. `faction_power_step` is 1 inside the test only (shipped 0: at 0 the shares cannot order).
    CONTROLS, same weights and seeds with the step at 0: only the stronger foreign holder's rolls move (the weaker foreign holder's and the
    SAME faction's, however heavy, are band for band what they were), and the stronger one's share falls."""
    stronger, weaker = _bands(1, 5, False, 1), _bands(5, 1, False, 1)
    checked = len(stronger) + len(weaker)
    assert checked >= 200, checked
    assert _share(stronger) < _share(weaker), (_share(stronger), _share(weaker))
    assert _share(stronger) < _share(_bands(1, 5, False, 0)), "the term did not make the stronger holder's seat harder"
    assert weaker == _bands(5, 1, False, 0), "a weaker foreign faction was priced"
    assert _bands(1, 5, True, 1) == _bands(1, 5, True, 0), "a holder of the host's own faction was priced"
