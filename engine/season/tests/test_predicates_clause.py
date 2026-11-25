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
    assert checked == 6, f"the six naming predicates (confer, establish, oblige, revoke, succeed, utter): saw {checked}"    # B21.82: `revoke` joins
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
    drifted.clauses = PR.REQUIRES_PREDICATES["confer"].clauses    # the shipped row is keyed (B21.80): its keys must still equal them
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
# clause to `row.refusal_for`. The four rows that take it are B21's, one commit each; B21.80's `confer` is the first shipped keyed
# row, so the first test reads it and the key-checking test PLANTS variants of it in its own table.

import dataclasses  # noqa: E402

from ..data.verbs import COUNTERPARTY_CLAUSE, ELIGIBILITY_CLAUSE, VERB_TABLE, WRITE_CLAUSE  # noqa: E402
from ..data.matrix import WriteClass  # noqa: E402
from ..gaps import Unspecified  # noqa: E402
from ..loop.driver import mint_token  # noqa: E402
from ..manifest import check_preconditions  # noqa: E402

_FLAT = ("confer.refused",)


def _keyed_confer(clause_kinds: dict):
    """`confer`'s row with its predicate clauses re-keyed to `clause_kinds` (planted: the shipped row has been keyed since B21.80,
    so a test that needs other keys or kinds builds its own). The fold clauses keep the one flat kind."""
    row = VERB_TABLE["confer"]
    by_clause = {ELIGIBILITY_CLAUSE: _FLAT, WRITE_CLAUSE: _FLAT, COUNTERPARTY_CLAUSE: _FLAT,
                 **{c: (k,) for c, k in clause_kinds.items()}}
    union = tuple(dict.fromkeys(k for ks in by_clause.values() for k in ks))
    return dataclasses.replace(row, emits_on_refusal=union, refusals_by_clause=by_clause)


def _flat_confer():
    """The row before B21.80: one kind for every refusal, as the control for what keying changes."""
    return dataclasses.replace(VERB_TABLE["confer"], emits_on_refusal=_FLAT, refusals_by_clause={})


def test_a_keyed_predicate_row_emits_its_clauses_kind(monkeypatch):
    """B21.80: THE SHIPPED `confer` ROW. A refusal at the purview clause, the held clause and the displacement clause emits
    three kinds, where the flat row (the control) emitted `confer.refused` for all three."""
    from .test_g3_not_yours import _gov_world
    declared = PR.REQUIRES_PREDICATES["confer"].clauses
    assert declared == ("office", "basis", "term", "conferee", "purview", "self_across_chains", "held", "displacement"), declared
    shipped = VERB_TABLE["confer"]
    assert shipped.refusals_by_clause, "the shipped confer row is flat: B21.80 keys it"
    assert shipped.precondition_evaluable(PR.REQUIRES_PREDICATES), "the shipped row's keys are not the predicate's clauses"
    kinds = [shipped.refusals_by_clause[c] for c in declared]
    assert all(len(k) == 1 for k in kinds) and len({k[0] for k in kinds}) == len(declared), (
        "two clauses of the predicate key one kind", kinds)

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
    monkeypatch.setitem(VERB_TABLE, "confer", _flat_confer())
    flat = arms(w, d)
    assert flat == {c: ["confer.refused"] for c in ("purview", "held", "displacement")}, flat    # CONTROL: the flat row

    monkeypatch.undo()
    w, d = _gov_world()
    got = arms(w, d)
    assert got == {"purview": ["confer.unauthorized"], "held": ["confer.held"],
                   "displacement": ["confer.displacement_unauthorized"]}, got
    assert len({k for ks in got.values() for k in ks}) == 3, "two clauses emitted one kind on a keyed row"
    # the actor's ledger holds a claim keyed by the purview kind, so §F1 clause 4 can decline the same act next round
    refused = [e for e in w.log if e.kind == "confer.unauthorized"]
    assert len(refused) == 1, refused
    d.witness(mint_token(w, WriteClass.INTERIOR), refused)
    assert any(c.predicate == "confer.unauthorized" and c.subject == "p_other" for c in w.persons["p_other"].ledger), (
        [(c.predicate, c.subject) for c in w.persons["p_other"].ledger])


def _flat_row(verb: str, kind: str):
    """A shipped row as it stood flat: one kind for every refusal (the control for what keying changes)."""
    return dataclasses.replace(VERB_TABLE[verb], emits_on_refusal=(kind,), refusals_by_clause={})


def test_a_refused_establish_says_which_clause_refused_in_its_kind(monkeypatch):
    """B21.81: THE SHIPPED `establish` ROW. Hand-built acts refused at `conferral basis`, `re-founding` and `reduction is
    revocation` emit three kinds where the flat row (the control) emitted `establish.refused` for all three, and the actor's
    ledger holds a claim keyed by each. (`rung held` is not reachable by a hand-built act: clause 1's `founds_over` refuses a
    rung the world does not hold first, as `office resolves`.)"""
    from .test_governance_build import _establish, _establish_world, _founding, _seat_reeve
    declared = PR.REQUIRES_PREDICATES["establish"].clauses
    assert declared == ("office resolves", "rung held", "conferral basis", "filler", "re-founding", "may fill",
                        "reduction is revocation"), declared
    shipped = VERB_TABLE["establish"]
    assert shipped.refusals_by_clause and shipped.precondition_evaluable(PR.REQUIRES_PREDICATES)
    kinds = [shipped.refusals_by_clause[c] for c in declared]
    assert all(len(k) == 1 for k in kinds) and len({k[0] for k in kinds}) == len(declared), (
        "two clauses of the predicate key one kind", kinds)

    def arms(world, driver):
        got = {}
        got["conferral basis"] = [e for e in _establish(world, driver, "e0", _founding(conferral=None))]
        _seat_reeve(world, ["confer", "issue", "dispatch"])      # a sitting holder whose grant is the three
        got["re-founding"] = [e for e in _establish(world, driver, "e1", _founding(post="Other"))]
        got["reduction is revocation"] = [e for e in _establish(world, driver, "e2",
                                                                 _founding(remit=["confer", "issue"]))]
        return got

    w, d = _establish_world()
    monkeypatch.setitem(VERB_TABLE, "establish", _flat_row("establish", "establish.refused"))
    flat = {c: [e.kind for e in es] for c, es in arms(w, d).items()}
    assert flat == {c: ["establish.refused"] for c in ("conferral basis", "re-founding", "reduction is revocation")}, flat
    monkeypatch.undo()
    w, d = _establish_world()
    got = arms(w, d)
    names = {c: [e.kind for e in es] for c, es in got.items()}
    assert names == {"conferral basis": ["establish.no_basis"], "re-founding": ["establish.refounding"],
                     "reduction is revocation": ["establish.reduces_grant"]}, names
    # the actor's ledger holds a claim keyed by each kind, so §F1 clause 4 can decline the same act next round
    for clause, events in got.items():
        w.log.extend(events)
        d.witness(mint_token(w, WriteClass.INTERIOR), events)
        assert any(c.predicate == names[clause][0] for c in w.persons["p_high"].ledger), (
            clause, [(c.predicate, c.subject) for c in w.persons["p_high"].ledger])


def test_a_refused_revoke_says_which_clause_refused_in_its_kind(monkeypatch):
    """B21.82: THE SHIPPED `revoke` ROW. Hand-built acts refused at `authority` (the mayor's seat has none over the duke) and at
    `held` (a seat nobody holds) emit two kinds where the flat row (the control) emitted `revoke.refused` for both, and the
    actor's ledger holds a claim keyed by each."""
    from .test_g3_not_yours import _SUCCESS, _gov_world
    declared = PR.REQUIRES_PREDICATES["revoke"].clauses
    assert declared == ("office", "disposal", "authority", "keeps", "held"), declared
    shipped = VERB_TABLE["revoke"]
    assert shipped.refusals_by_clause and shipped.precondition_evaluable(PR.REQUIRES_PREDICATES)
    kinds = [shipped.refusals_by_clause[c] for c in declared]
    assert all(len(k) == 1 for k in kinds) and len({k[0] for k in kinds}) == len(declared), (
        "two clauses of the predicate key one kind", kinds)

    def arms(world, driver):
        world.offices["off_duke"].remit_acts.append("revoke")       # the duke's seat revokes too (`remit:revoke`, eligibility)
        world._grant_remit(next(t for t in world.tenures if t.kind == "hold" and t.object == "off_duke"), force=True)
        got = {}
        for clause, actor, via, office in (("authority", "p_king", "off_mayor", "off_duke"),
                                           ("held", "p_high", "off_duke", "off_reeve")):
            act = Act(id=f"rv_{clause}", actor=actor, verb="revoke", payload={"office": office}, via=via)
            world.acts.append(act)
            got[clause] = driver._fold(world, mint_token(world, WriteClass.ACTS), act, _SUCCESS)
        return got

    w, d = _gov_world()
    monkeypatch.setitem(VERB_TABLE, "revoke", _flat_row("revoke", "revoke.refused"))
    flat = {c: [e.kind for e in es] for c, es in arms(w, d).items()}
    assert flat == {"authority": ["revoke.refused"], "held": ["revoke.refused"]}, flat       # CONTROL: the flat row
    monkeypatch.undo()
    w, d = _gov_world()
    got = arms(w, d)
    names = {c: [e.kind for e in es] for c, es in got.items()}
    assert names == {"authority": ["revoke.unauthorized"], "held": ["revoke.no_holder"]}, names
    actors = {"authority": "p_king", "held": "p_high"}
    for clause, events in got.items():
        w.log.extend(events)
        d.witness(mint_token(w, WriteClass.INTERIOR), events)
        assert any(c.predicate == names[clause][0] for c in w.persons[actors[clause]].ledger), (
            clause, [(c.predicate, c.subject) for c in w.persons[actors[clause]].ledger])


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
