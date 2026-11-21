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
            assert ok is False, (verb, payload, via, ok)
    assert ran >= 9 * 4, ran


def test_the_shared_read_returns_a_string_or_empty():
    """`subject_of` / `operand_of`: a non-string operand reads as `""`, a string as itself."""
    from ..state.carriers import operand_of
    mk = lambda payload: Act(id="x", actor="p", verb="v", payload=payload)
    assert subject_of(mk({"subject": _LIST})) == "" and subject_of(mk({"subject": "a"})) == "a"
    assert subject_of(mk({})) == "" and subject_of(mk({"subject": None})) == ""
    assert operand_of(mk({"office": _LIST}), "office") == ""
    assert operand_of(mk({"office": "o"}), "office") == "o"
    assert operand_of(mk("a string payload"), "to") == ""
