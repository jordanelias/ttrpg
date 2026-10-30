"""v9 IN-33 (H-58), RESTORED at v10 REM-2B (checkpoints `ad2f930f`..`b5c4685d`): `exchange` ON ITS TWO COINED
OPERANDS, `return_kind` AND `return_amount`.

The row's cell is W3's own -- *both sides' stores cover their side of the exchange* -- as two
`scalar_threshold` conjuncts: `stores(from, kind) >= amount` (the actor's side, `transfer`'s cell)
and `stores(to, return_kind) >= return_amount` (the other side). `loop/effects_economy.py::
_eff_exchange` moves both sides with `_shift`. The person derives `return_kind` from the fixture
`default_return_kind` and `return_amount` from `default_transfer_amount` (`decision/options.py::
_derive_operand`; DECISION at `hole_register.yaml` H-58).

  (a) THE CLOSURE STILL BINDS: a cell naming an operand outside `requires_operands` refuses at load.
  (b) THE FOLD, ON A HAND-BUILT WORLD WHERE THE CAUSE IS CONTROLLED: both sides move, each kind is
      conserved; the controls (a kind nobody holds, a kind for itself, a rung with itself, a side
      short of stock) refuse and move nothing.
  (c) FORMATION: a Candidate carries the two new operands from the fixtures, and no other row's
      formation moves (the crowd-out control, by construction against the base row).
  (d) THE REALM HALF IS NOT HERE. v9 built `exchange`, measured it at 0 executions through the real
      chooser, and reverted it; REM-2B restores it WITHOUT requiring a realm execution (P9), so no test
      here asks the real chooser to execute one. The trajectory it moves is read at `aperture 4 0`
      (the commit body), not asserted.

MUTATIONS, run at the restore (the commit body): the roster's two names removed reddens (a) and (c);
`_eff_exchange`'s second `_shift` deleted reddens (b)'s conservation; the `kind == back` decline in
`decision/options.py::_operands` deleted reddens (c)'s like-for-like test.
"""
import dataclasses

import pytest

from engine.season.data import verbs as V
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.requires import REQUIRES_OPERANDS, build_typed_requires
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision.options import opening_set
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.state.carriers import Act, Claim, Question, View

VERB = "exchange"
MADE, REFUSED = "exchange.made", "exchange.refused"


# (a) THE CLOSURE ---------------------------------------------------------------------------------

def _two_sided(key, threshold):
    return {"all": [
        {"form": "scalar_threshold", "of": "from", "scalar": "stores", "key": "kind",
         "threshold": "amount"},
        {"form": "scalar_threshold", "of": "to", "scalar": "stores", "key": key,
         "threshold": threshold}]}


def test_in33_a_an_operand_outside_the_roster_still_refuses_at_load():
    """FALSIFIER (the plan's): an operand outside the closed roster -> the loader refuses. The two
    coined names load; an unlisted name in the same position does not."""
    assert {"return_kind", "return_amount"} <= set(REQUIRES_OPERANDS)
    req = build_typed_requires(VERB, _two_sided("return_kind", "return_amount"))
    assert req.operands() == ("from", "kind", "amount", "to", "return_kind", "return_amount")
    with pytest.raises(SystemExit, match="not in rosters.yaml's requires_operands"):
        build_typed_requires(VERB, _two_sided("counter_kind", "counter_amount"))


def test_in33_a_the_row_is_typed_on_both_sides_and_resolvable():
    row = VERB_TABLE[VERB]
    assert row.requires_typed is not None
    assert set(row.requires_typed.operands()) >= {"from", "kind", "amount", "to", "return_kind",
                                                   "return_amount"}
    assert not row.requires_decline_note and not row.effect_decline_note, "a stale decline note"
    assert VERB in resolvable_verbs()


# (b) THE FOLD, HAND-BUILT --------------------------------------------------------------------------

def _at_resolve(hh=None, s=None):
    """`tiny_world` at a RESOLVE barrier with the two larders set by hand AFTER MATTER ran, so no
    yield moves them under the act."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    w.rungs["Hh"].stores = dict(hh if hh is not None else {"grain": 8})
    w.rungs["S"].stores = dict(s if s is not None else {"grain": 40, "salt": 5})
    return w, d


def _fold(w, d, **over):
    payload = {"subject": "S", "from": "Hh", "to": "S", "kind": "grain", "amount": 2,
               "return_kind": "salt", "return_amount": 1, **over}
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="ex", actor="p_low", verb=VERB, payload=payload))
    return [e.kind for e in out]


def _stores(w):
    return {r: dict(w.rungs[r].stores) for r in ("Hh", "S")}


def test_in33_b_an_exchange_moves_both_sides_and_conserves_each_kind():
    w, d = _at_resolve()
    before = _stores(w)
    kinds = _fold(w, d)
    assert MADE in kinds and REFUSED not in kinds, kinds
    after = _stores(w)
    assert after["Hh"] == {"grain": 6, "salt": 1}, after
    assert after["S"] == {"grain": 42, "salt": 4}, after
    for k in ("grain", "salt"):
        assert (sum(s.get(k, 0) for s in before.values())
                == sum(s.get(k, 0) for s in after.values())), k


@pytest.mark.parametrize("why, over, hh, s", [
    ("the other side holds none of the kind it gives back (the `coin` control arm)",
     {"return_kind": "coin"}, None, None),
    ("a kind traded for itself", {"return_kind": "grain"}, None, None),
    ("a rung trading with itself", {"to": "Hh", "subject": "Hh"}, {"grain": 8, "salt": 5}, None),
    ("the actor's side is short", {"amount": 9}, None, None),
    ("the other side is short", {"return_amount": 6}, None, None),
    ("a side that is no rung", {"to": "p_mid", "subject": "p_mid"}, None, None),
])
def test_in33_b_the_controls_refuse_and_move_nothing(why, over, hh, s):
    w, d = _at_resolve(hh, s)
    before = _stores(w)
    kinds = _fold(w, d, **over)
    assert REFUSED in kinds and MADE not in kinds, (why, kinds)
    assert _stores(w) == before, why


# (c) FORMATION -----------------------------------------------------------------------------------

def _formed(w, pid, referents):
    q = Question("q:in33", "need", tuple(referents))
    return opening_set(w.persons[pid], View(pid, [], w.fixtures.get("view_k")), q, w.fixtures)


def _sig(cands):
    return sorted((c.verb, str(c.subject), sorted((k, str(v)) for k, v in c.operands.items()))
                  for c in cands)


def test_in33_c_a_candidate_carries_what_comes_back_from_the_fixtures():
    w = P.tiny_world()
    got = [c for c in _formed(w, "p_low", ("S",)) if c.verb == VERB]
    assert got, "no `exchange` formed on a rung referent"
    for c in got:
        assert c.operands["to"] == "S" and c.operands["from"] == "Hh", c.operands
        assert c.operands["return_kind"] == w.fixtures.get("default_return_kind")
        assert c.operands["return_amount"] == w.fixtures.get("default_transfer_amount")
        assert c.operands["return_kind"] != c.operands["kind"], c.operands


def test_in33_c_no_other_rows_formation_moves(monkeypatch):
    """THE CROWD-OUT CONTROL AT FORMATION: with `exchange`'s row as it was before IN-33 (untyped,
    forming on every referent with no operands), every Candidate of every OTHER row is identical,
    for every person over every rung and person referent."""
    w = P.tiny_world()
    refs = tuple(sorted(w.rungs)) + tuple(sorted(w.persons))
    now = {pid: _formed(w, pid, refs) for pid in w.persons}
    base_row = dataclasses.replace(VERB_TABLE[VERB], requires_typed=None)
    monkeypatch.setitem(V.VERB_TABLE, VERB, base_row)
    checked = 0
    for pid in w.persons:
        base = _formed(w, pid, refs)
        assert _sig(c for c in now[pid] if c.verb != VERB) == _sig(
            c for c in base if c.verb != VERB), pid
        checked += sum(c.verb == VERB for c in now[pid])
    assert checked >= len(w.persons), checked


def test_in33_c_a_question_naming_the_return_kind_forms_no_exchange():
    """The like-for-like decline: when the question names the kind that would come back (here a
    held `stores:<kind>` claim about the referent, `store_kind_of`), `kind` and `return_kind` are
    one kind and no `exchange` forms; `transfer` on the same question still forms (control)."""
    w = P.tiny_world()
    p = w.persons["p_low"]
    back = w.fixtures.get("default_return_kind")
    c = Claim(id="c_in33", holder="p_low", subject="S", predicate=f"stores:{back}", value=5,
              when=0, source="seen", confidence=1, visibility="own")
    p.ledger.append(c)
    q = Question("q:in33k", "claim_landed", ("S",), about="c_in33")
    got = opening_set(p, View("p_low", [], w.fixtures.get("view_k")), q, w.fixtures)
    assert not [x for x in got if x.verb == VERB], [x.operands for x in got if x.verb == VERB]
    assert [x for x in got if x.verb == "transfer" and x.operands["kind"] == back], "control"
