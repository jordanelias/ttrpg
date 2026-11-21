"""B09.18 -- A PREDICATE NEVER RAISES, AND NAMES THE CLAUSE THAT REFUSED (step one).

Two claims, each executed and each able to fail:

  1. EVERY REFUSING BRANCH OF THE NINE REGISTERED PREDICATES NAMES ITS CLAUSE. An `ast` walk over the functions of
     `REQUIRES_PREDICATES` finds no `return False`: a refusal reads `return _refuse("<clause>", "<ids>")`, which
     leaves one DECISION row in `TRACE` (a trace row is not world state: the hash is unmoved). The walk asserts that
     it walked (`checked >= 9`), and a PLANTED bare branch is shown to be caught, so a walk that matched nothing
     cannot pass.
  2. A LIST OPERAND IS REFUSED, NOT RAISED. The fold calls `bool(pred(w, a))` with no catch, so a predicate that
     raises on a hand-built or client-returned act ends the season. Each predicate, on `{"subject": ["a", "b"]}`
     (and on the same list under `office` and `to`, the other operands the predicates read), answers `False`.
"""
from __future__ import annotations

import ast
import inspect
import textwrap

import pytest

from ..boot.realm import build_realm
from ..loop import predicates as PR
from ..state.carriers import Act, subject_of

_LIST = ["a", "b"]


def _bare_false_returns(fn) -> list:
    """The line numbers (within `fn`'s own source) of every `return False` in it."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    return [n.lineno for n in ast.walk(tree)
            if isinstance(n, ast.Return) and isinstance(n.value, ast.Constant) and n.value.value is False]


def test_every_refusing_branch_names_a_clause():
    checked = 0
    bare = {}
    for verb, fn in PR.REQUIRES_PREDICATES.items():
        checked += 1
        lines = _bare_false_returns(fn)
        if lines:
            bare[verb] = lines
    assert checked >= 9, f"the walk saw {checked} registered predicates; the population floor is nine"
    assert not bare, f"a refusing branch returns a bare False (use `_refuse(clause, ids)`): {bare}"


def test_a_planted_bare_branch_is_caught():
    """The walk can observe the failure it excludes: a predicate with one bare `return False` is reported."""
    def _planted(w, a):
        if a is None:
            return False
        return PR._refuse("planted", "x")

    assert len(_bare_false_returns(_planted)) == 1
    def _clean(w, a):
        return PR._refuse("planted", "x")
    assert _bare_false_returns(_clean) == []


def _acts(w):
    """A seated actor and the seat he exercises, so the predicates that ask `via` get past it."""
    hold = next(t for t in w.tenures if t.kind == "hold" and t.live and t.object in w.offices)
    actor, via = hold.subject, hold.object
    shapes = [{"subject": list(_LIST)},
              {"subject": list(_LIST), "office": list(_LIST), "to": list(_LIST)}]
    return [(actor, via, p) for p in shapes] + [(actor, None, p) for p in shapes]


def test_a_list_operand_is_refused_not_raised():
    w = build_realm(0)
    ran = 0
    for verb, fn in sorted(PR.REQUIRES_PREDICATES.items()):
        for actor, via, payload in _acts(w):
            act = Act(id=f"probe_{verb}", actor=actor, verb=verb, payload=payload, via=via)
            ok = fn(w, act)              # no catch: a raise fails the test, which is the claim
            ran += 1
            assert isinstance(ok, (bool, PR.Answer)) and not ok, (verb, payload, via, ok)   # a refusal, never a raise or a None
    assert ran >= 9 * 4, ran


def _refused_names(fn) -> list:
    """The literal first argument of every `_refuse_at(...)` call in `fn`: the clause name each refusing branch carries."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    return [n.args[0].value for n in ast.walk(tree)
            if isinstance(n, ast.Call) and n.args and isinstance(n.args[0], ast.Constant)
            and (getattr(n.func, "id", None) == "_refuse_at" or getattr(n.func, "attr", None) == "_refuse_at")]


def test_every_branch_names_a_declared_clause_and_every_declared_clause_has_a_branch():
    """B09.19: the names a branch carries and the names the decorator declares are one set (the decorator owns it). A branch
    naming a clause nobody declared, or a declared clause no branch refuses at, is the drift this walk reads. It asserts that
    it walked, and a planted undeclared branch is shown to be caught."""
    checked = 0
    for verb, fn in sorted(PR.REQUIRES_PREDICATES.items()):
        declared = getattr(fn, "clauses", ())
        if not declared:
            assert not _refused_names(fn), f"{verb!r} names clauses at its branches and declares none"
            continue
        used = _refused_names(fn)
        assert set(used) <= set(declared), (verb, sorted(set(used) - set(declared)))
        assert set(declared) <= set(used), (verb, sorted(set(declared) - set(used)))
        assert len(set(declared)) == len(declared), verb
        checked += 1
    assert checked == 4, f"the four naming predicates (confer, establish, oblige, succeed): saw {checked}"
    # the walk observes what it excludes
    def _planted(w, a):
        return PR._refuse_at("undeclared", "x")
    assert _refused_names(_planted) == ["undeclared"]
    assert "undeclared" not in PR.REQUIRES_PREDICATES["confer"].clauses


def test_a_predicate_refusing_at_a_name_it_did_not_declare_is_an_instrument_defect(monkeypatch):
    """The fold checks the clause a predicate answers against its own declaration, so a branch that drifted from the decorator
    fails loudly at the first act it refuses and is not silently read as a flat refusal."""
    from ..gaps import InstrumentDefect
    from .test_g3_not_yours import _gov_world

    def drifted(w, a):
        return PR.Answer(False, "bogus")
    drifted.clauses = ("declared",)
    monkeypatch.setitem(PR.REQUIRES_PREDICATES, "confer", drifted)
    w, d = _gov_world()
    with pytest.raises(InstrumentDefect):
        d.resolve(mint_token(w, WriteClass.ACTS),
                  [Act(id="c0", actor="p_other", verb="confer", payload={"office": "off_reeve", "to": "p_mid"},
                       via="off_duke2")], contest_max_depth=w.fixtures.get("contest_max_depth"))


def test_the_shared_read_returns_a_string_or_empty():
    """`subject_of` / `operand_of`: a non-string operand reads as `""`, a string as itself."""
    from ..state.carriers import operand_of
    mk = lambda payload: Act(id="x", actor="p", verb="v", payload=payload)
    assert subject_of(mk({"subject": _LIST})) == "" and subject_of(mk({"subject": "a"})) == "a"
    assert subject_of(mk({})) == "" and subject_of(mk({"subject": None})) == ""
    assert operand_of(mk({"office": _LIST}), "office") == ""
    assert operand_of(mk({"office": "o"}), "office") == "o"
    assert operand_of(mk("a string payload"), "to") == ""


# ======================================================================================
# B09.19 -- STEP TWO'S CHANNEL: THE REFUSED CLAUSE REACHES THE EVENT'S KIND
# ======================================================================================
# `requires_predicate(verb, clauses=...)` declares the clause names; a predicate answers `(ok, clause)`; `_admits` hands the
# clause to `row.refusal_for`. NO shipped row is keyed (the four authored rows are B21's), so each test PLANTS a keyed `confer`
# row in its own table, over kinds the roster already holds.

import dataclasses  # noqa: E402

from ..data.verbs import COUNTERPARTY_CLAUSE, ELIGIBILITY_CLAUSE, VERB_TABLE, WRITE_CLAUSE  # noqa: E402
from ..data.matrix import WriteClass  # noqa: E402
from ..gaps import Unspecified  # noqa: E402
from ..loop.driver import mint_token  # noqa: E402
from ..manifest import check_preconditions  # noqa: E402

_PURVIEW_KIND, _HELD_KIND, _DISPLACE_KIND = "case.unauthorized", "confer.refused", "issue.unauthorized"


def _keyed_confer(clause_kinds: dict):
    """`confer`'s shipped row, keyed: the three fold clauses it fails at (eligibility, write, counterparty), plus the predicate
    clauses `clause_kinds` names. The fold clauses keep the kind the flat row emitted, so only the predicate's clauses move."""
    row = VERB_TABLE["confer"]
    flat = row.emits_on_refusal
    by_clause = {ELIGIBILITY_CLAUSE: flat, WRITE_CLAUSE: flat, COUNTERPARTY_CLAUSE: flat,
                 **{c: (k,) for c, k in clause_kinds.items()}}
    union = tuple(dict.fromkeys(k for ks in by_clause.values() for k in ks))
    return dataclasses.replace(row, emits_on_refusal=union, refusals_by_clause=by_clause)


def test_a_keyed_predicate_row_emits_its_clauses_kind(monkeypatch):
    from .test_g3_not_yours import _gov_world
    declared = PR.REQUIRES_PREDICATES["confer"].clauses
    assert declared == ("office", "basis", "conferee", "purview", "held", "displacement"), declared
    kinds = {c: _HELD_KIND for c in declared}
    kinds.update(purview=_PURVIEW_KIND, displacement=_DISPLACE_KIND)
    keyed = _keyed_confer(kinds)
    assert keyed.precondition_evaluable(PR.REQUIRES_PREDICATES), "the planted row is not admitted: the fixture is wrong"

    def run(world, driver, aid, actor, via, to):
        out = driver.resolve(mint_token(world, WriteClass.ACTS),
                             [Act(id=aid, actor=actor, verb="confer", payload={"office": "off_reeve", "to": to}, via=via)],
                             contest_max_depth=world.fixtures.get("contest_max_depth"))
        world.log.extend(out)
        return out

    # the three arms on one world in order: PURVIEW (a duke of another duchy), then a legitimate conferral that seats the reeve,
    # then HELD (conferring the seat on its own holder) and DISPLACEMENT (the King, who has no revocation reach over the reeve)
    def arms(world, driver):
        got = {}
        got["purview"] = [e.kind for e in run(world, driver, "c0", "p_other", "off_duke2", "p_mid")]
        assert "tenure.opened" in [e.kind for e in run(world, driver, "c1", "p_high", "off_duke", "p_mid")]
        got["held"] = [e.kind for e in run(world, driver, "c2", "p_high", "off_duke", "p_mid")]
        got["displacement"] = [e.kind for e in run(world, driver, "c3", "p_king", "off_crown", "p_low")]
        return got

    w, d = _gov_world()
    flat = arms(w, d)
    assert flat == {c: ["confer.refused"] for c in ("purview", "held", "displacement")}, flat    # CONTROL: the shipped flat row

    w, d = _gov_world()
    monkeypatch.setitem(VERB_TABLE, "confer", keyed)
    got = arms(w, d)
    assert got == {"purview": [_PURVIEW_KIND], "held": [_HELD_KIND], "displacement": [_DISPLACE_KIND]}, got
    assert len({k for ks in got.values() for k in ks}) == 3, "two clauses emitted one kind on a keyed row"
    # the actor's ledger holds a claim keyed by the purview kind, so §F1 clause 4 can decline the same act next round
    refused = [e for e in w.log if e.kind == _PURVIEW_KIND]
    assert len(refused) == 1, refused
    d.witness(mint_token(w, WriteClass.INTERIOR), refused)
    assert any(c.predicate == _PURVIEW_KIND and c.subject == "p_other" for c in w.persons["p_other"].ledger), (
        [(c.predicate, c.subject) for c in w.persons["p_other"].ledger])


def test_a_keyed_predicate_row_with_unknown_keys_is_refused(monkeypatch):
    declared = PR.REQUIRES_PREDICATES["confer"].clauses
    ok = _keyed_confer({c: "confer.refused" for c in declared})
    assert ok.precondition_evaluable(PR.REQUIRES_PREDICATES), "control: the exact keys are admitted"
    checked = 0
    for what, names in (("an unknown key", (*declared, "bogus")),
                        ("a declared clause left unkeyed", declared[:-1]),
                        ("only unknown keys", ("bogus",))):
        row = _keyed_confer({c: "confer.refused" for c in names})
        assert not row.precondition_evaluable(PR.REQUIRES_PREDICATES), what
        # the construction-time sweep names the verb: a precondition nothing evaluates, with no decline note
        with pytest.raises(Unspecified) as refused:
            check_preconditions({**VERB_TABLE, "confer": row}, PR.REQUIRES_PREDICATES)
        assert "confer" in str(refused.value), what
        checked += 1
    assert checked == 3
    assert check_preconditions({**VERB_TABLE, "confer": ok}, PR.REQUIRES_PREDICATES), "control: the sweep was not empty"
