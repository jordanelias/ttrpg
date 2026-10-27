"""REM-14 -- THE PREDICATE ROWS TRACE THE CLAUSE THEY REFUSED ON.

`loop/resolve.py` traces "<verb> by <actor>: precondition unmet" for ANY refused precondition, and a
predicate with several `return False` lines could not say which one decided. Each refusing branch of
`_req_release`, `_req_revoke`, `_req_dispatch`, `_req_convene` and `sides_of`'s non-marchable
`march` target now leaves one DECISION row (`chose="refuse"`) in the cluster-key form
`harness/report.py` groups by: `"<clause> -> <ids>"`.

Each test hand-builds the refusal, reads the rows the call appended to `TRACE`, and pairs it with a
CONTROL of the same act that is admitted and leaves no row (so the row is the refusal's, not
something every call writes). The predicate's answer is asserted unchanged (a bare `False`/`True`):
a predicate that returned a `Verdict` with observed reads would deposit claims and move the world
hash (`CLAUDE.md` §0.1).

MUTATION (run when this file was written): delete the `_refuse(...)` line of `_req_release`'s
ownership clause (making it `return False`) and `test_release_of_a_tenure_the_actor_does_not_own`
reds; delete the `TRACE.decision` call in `sides_of` and the march test reds.
"""

from __future__ import annotations

from ..harness import probes as P
from ..harness.populated import build_realm
from ..loop import predicates as _preds
from ..loop.sides import sides_of
from ..state.carriers import Act, Office, Rung
from ..trace_log import TRACE
from ..state.world import World


def _rows_of(call) -> tuple[object, list]:
    """`(call's answer, the DECISION rows it appended)`."""
    first = len(TRACE.rows)
    out = call()
    return out, [r for r in TRACE.rows[first:] if r.channel == "DECISION"]


def _clause(row) -> str:
    """The cluster key `harness/report.py` groups a DECISION row by."""
    return row.what.split(" -> ")[0]


def test_release_of_a_tenure_the_actor_does_not_own():
    w = P.tiny_world()
    tie = next(t for t in w.tenures if t.kind == "tie" and t.subject == "p_low" and t.live)
    # the tie is p_low's own: admitted, and nothing is written to the trace (the control)
    mine = Act(id="rel_ok", actor="p_low", verb="release", payload={"subject": tie.object})
    ok, rows = _rows_of(lambda: _preds._req_release(w, mine))
    assert ok is True and rows == [], rows
    # the same edge, released by a man who does not own it
    theirs = Act(id="rel_no", actor="p_mid", verb="release", payload={"subject": tie.object})
    out, rows = _rows_of(lambda: _preds._req_release(w, theirs))
    assert out is False
    assert len(rows) == 1, rows
    row = rows[0]
    assert row.detail["chose"] == "refuse"
    assert " -> " in row.what and row.what.endswith(f"p_mid toward {tie.object!r}"), row.what
    assert "does not own" in _clause(row), _clause(row)
    # and the no-subject clause is a different clause, so the two cannot be told apart by count alone
    out, rows = _rows_of(lambda: _preds._req_release(
        w, Act(id="rel_none", actor="p_low", verb="release", payload={})))
    assert out is False and [_clause(r) for r in rows] == ["a release names no subject"], rows


def test_revoke_names_the_clause_it_refused_on():
    """Three of `_req_revoke`'s four refusals, on `test_g3_not_yours.py`'s governance world. The
    fourth (a seat whose conferral basis has no revocation disposal) is reached only by a
    hand-mutated office -- `Office.__post_init__` refuses one -- and is not planted here."""
    from .test_g3_not_yours import _gov_world
    w, _ = _gov_world()
    rv = lambda via, office, actor="p_king": Act(
        id=f"rv_{via}_{office}", actor=actor, verb="revoke", payload={"office": office}, via=via)
    # control: the King revokes the duke through the seat above him -- admitted, no row
    ok, rows = _rows_of(lambda: _preds._req_revoke(w, rv("off_crown", "off_duke")))
    assert ok is True and rows == [], rows
    # (1) no such office
    out, rows = _rows_of(lambda: _preds._req_revoke(w, rv("off_crown", "off_nowhere")))
    assert out is False and [_clause(r) for r in rows] == [
        "a revoke names no office the world holds"], rows
    # (3) the seat exercised (`off_mayor`, below the duchy) has no authority over the duke's seat
    out, rows = _rows_of(lambda: _preds._req_revoke(w, rv("off_mayor", "off_duke")))
    assert out is False and [_clause(r) for r in rows] == [
        "a revoke the seat exercised has no revocation authority over the seat"], rows
    assert rows[0].what.endswith("p_king via 'off_mayor' on 'off_duke'"), rows[0].what
    # (4) authority holds, but the seat is vacant: nobody to strip
    w.offices["off_vacant"] = Office("off_vacant", "Duke", "D", ["issue"], faction="Crown",
                                     conferral="appointed", revocation="rung_above_same_faction")
    assert _preds.may_revoke(w, "p_king", "off_crown", w.offices["off_vacant"]), "fixture"
    out, rows = _rows_of(lambda: _preds._req_revoke(w, rv("off_crown", "off_vacant")))
    assert out is False and [_clause(r) for r in rows] == [
        "a revoke of a seat nobody holds"], rows
    assert all(r.detail["chose"] == "refuse" for r in rows)


def test_dispatch_names_no_person_the_world_holds():
    w = P.tiny_world()
    ok, rows = _rows_of(lambda: _preds._req_dispatch(
        w, Act(id="d_ok", actor="p_high", verb="dispatch", payload={"subject": "p_low"})))
    assert ok is True and rows == [], rows
    out, rows = _rows_of(lambda: _preds._req_dispatch(
        w, Act(id="d_no", actor="p_high", verb="dispatch", payload={"subject": "p_nobody"})))
    assert out is False and len(rows) == 1, rows
    assert _clause(rows[0]) == "a dispatch names no person the world holds"
    assert rows[0].what.endswith("p_high to 'p_nobody'") and rows[0].detail["chose"] == "refuse"


def test_convene_traces_both_of_its_refusals():
    w = World(world_seed=1)
    w.rungs["r_person"] = Rung("r_person", "person")
    w.rungs["r_settle"] = Rung("r_settle", "settlement")
    mk = lambda subject: Act(id="c", actor="x", verb="convene", payload={"subject": subject})
    ok, rows = _rows_of(lambda: _preds._req_convene(w, mk("r_settle")))
    assert ok is True and rows == [], rows
    out, rows = _rows_of(lambda: _preds._req_convene(w, mk("r_person")))
    assert out is False and [_clause(r) for r in rows] == [
        "a convene at a person-rung (an address, not a place)"], rows
    out, rows = _rows_of(lambda: _preds._req_convene(w, mk("r_nowhere")))
    assert out is False and [_clause(r) for r in rows] == [
        "a convene at a venue that is no rung the world holds"], rows


def test_march_at_a_non_marchable_target_traces_its_clause():
    """`sides_of`'s empty-claimants branch (answered later as `march.refused`). Control: a
    marchable settlement reaches the same function and traces nothing."""
    w = build_realm(0)
    a = Act(id="m1", actor="p_npc_033", verb="march", payload={"subject": "r_valoria"},
            via="off_npc_033")
    (sides, rows) = _rows_of(lambda: sides_of(w, a, "r_valoria", "a field"))
    assert sides[0] == [] and len(rows) == 1, rows
    assert _clause(rows[0]) == "a march at a target that is not a rung of a marchable kind"
    assert rows[0].what.endswith("p_npc_033 on 'r_valoria'") and rows[0].detail["chose"] == "refuse"
    ok = Act(id="m2", actor="p_npc_033", verb="march", payload={"subject": "set_s_002"},
             via="off_npc_033")
    (sides, rows) = _rows_of(lambda: sides_of(w, ok, "set_s_002", "a field"))
    assert sides[0] and rows == [], rows
