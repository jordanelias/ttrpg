"""v9 PC-06 K-3 (`H-85`) -- `thread_read`'s typed cell over the Thread Sensitivity carrier.

The design (`proposals/2026-10-07-unplugged-systems-replug.md` §3.3, re-reviewed at the B-S opener):
a per-person whole number on `Person`, set once at world build from the cast's authored `ts:` by
`data/cast.py::thread_sensitivity_of`, never written in play; read by `thread_read`'s
`scalar_threshold` cell `of: actor` over the stem `thread_sensitivity`, against the second read
`thread_sensitivity.gate` (`Fixtures thread_sensitivity_gate`). Both stems are answered by
`queries/person_q.py::OwnStateReader`, which the fold's `WorldReader` delegates to and the person's
own formation (`decision/options.py::opening_set`) asks.

THE FALSIFIERS, one section each:
  (a) the stem reads the carrier: an actor at 30 executes, at 29 is refused, with no value is refused
      -- at the fold, at the reader, and in the person's own formation;
  (b) the threshold is the fixture's: sweep it and the same person's verdict flips;
  (c) the parse rule on every authored shape, and a refusal on any other;
  (d) `thread_read` has left the no-predicate set, asked of its owner (`resolvable_verbs()`);
  (e) nothing writes the carrier in play: no `write_matrix.yaml` row, the gate refuses a write, and
      no engine source outside the world build assigns it.
"""
from __future__ import annotations

import ast
import pathlib

import pytest

from ..data import cast
from ..data.matrix import matrix_row
from ..data.requires import OWN_STATE_STEMS, UNKNOWN, WORLD_ONLY_STEMS, binding_of, evaluate
from ..data.verbs import VERB_TABLE
from ..decision.options import opening_set
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import REQUIRES_PREDICATES, SeasonDriver, mint_token, resolvable_verbs
from ..queries.person_q import LedgerReader, OwnStateReader
from ..queries.world_q import WorldReader
from ..state.carriers import Question, View
from ..state.gate import WriteClass
from ..state.world import Step

VERB = "thread_read"
ACTOR = "p_low"
#: The shipped gate, read from the fixture rather than typed: the test is about the cell, not the 30.
GATE = P.DEFAULT_FIXTURES.get("thread_sensitivity_gate")


def _world(ts, fixtures=None):
    w = P.tiny_world(fixtures) if fixtures is not None else P.tiny_world()
    w.persons[ACTOR].thread_sensitivity = ts
    return w


def _fold_kinds(w, key: str = "") -> list:
    """`ACTOR` attempts one `thread_read` through the real fold; the kinds its act caused."""
    d = P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, VERB, key=key, payload={"subject": "Hh"})]
                                        if p.id == ACTOR else []))
    ids = {a.id for a in d.resolved if a.verb == VERB}
    assert ids, "the hand-built act never reached RESOLVE -- this asserts nothing about the gate"
    return [e.kind for e in w.log if (e.causes or [None])[0] in ids]


def _formed(w, fx=None) -> bool:
    p = w.persons[ACTOR]
    q = Question("q:k3", "need", ("Hh",))
    cands = opening_set(p, View(ACTOR, [], w.fixtures.get("view_k")), q, fx or w.fixtures)
    return any(c.verb == VERB for c in cands)


# ======================================================================================
# (a) THE STEM READS THE CARRIER
# ======================================================================================

def test_k3_a_the_gate_reads_the_actors_own_carrier_at_the_fold_the_reader_and_formation():
    cell = VERB_TABLE[VERB].requires_typed
    assert cell is not None, "`thread_read` carries no typed cell"
    want = {GATE: True, GATE - 1: False, None: UNKNOWN}
    checked = 0
    for ts, verdict in want.items():
        w = _world(ts)
        # the fold's reader, through the one evaluator
        got = evaluate(cell, WorldReader(w, ACTOR), binding_of(ACTOR, {})).value
        assert got is verdict, (ts, got)
        # the person's own formation: only a person his own reading admits forms the Candidate
        assert _formed(w) is (verdict is True), (ts, "formation disagrees with the gate")
        # the fold, end to end
        kinds = _fold_kinds(w)
        if verdict is True:
            assert "finding.made" in kinds and "finding.none" not in kinds, (ts, kinds)
        else:
            assert "finding.none" in kinds and "finding.made" not in kinds, (ts, kinds)
        checked += 1
    assert checked == 3


def test_k3_a_a_person_reads_nobody_elses_sensitivity_and_no_ledger_answers_it():
    """`OwnStateReader` answers the stem only of its own person; a ledger never does (the stems are
    `WORLD_ONLY_STEMS`), so no told or seen number can stand in for the one on the person."""
    w = _world(GATE + 10)
    other = w.persons["p_mid"]
    assert OwnStateReader(other, w.fixtures).read(ACTOR, "thread_sensitivity") is UNKNOWN
    assert OwnStateReader(w.persons[ACTOR], w.fixtures).read(ACTOR, "thread_sensitivity") == GATE + 10
    assert OWN_STATE_STEMS <= WORLD_ONLY_STEMS
    from ..state.carriers import Claim
    lie = Claim("c_lie", ACTOR, ACTOR, "thread_sensitivity", 99, 0, "firsthand", 100, "own")
    assert LedgerReader([lie]).read(ACTOR, "thread_sensitivity") is UNKNOWN, (
        "a ledger answered a sensitivity -- a told number would decide the gate")
    # a subject that is no person has no sensitivity, and the fold refuses rather than raising
    assert WorldReader(w, ACTOR).read("Hh", "thread_sensitivity") is UNKNOWN
    # AT THE FOLD TOO: the fold's reader is built on its own actor, so a cell naming ANOTHER person
    # reads UNKNOWN even where that person carries a value, and the actor's own reading is unchanged
    other.thread_sensitivity = GATE + 20
    assert WorldReader(w, ACTOR).read("p_mid", "thread_sensitivity") is UNKNOWN, (
        "the fold read another person's sensitivity")
    assert WorldReader(w, ACTOR).read(ACTOR, "thread_sensitivity") == GATE + 10
    assert WorldReader(w, "p_mid").read("p_mid", "thread_sensitivity") == GATE + 20


# ======================================================================================
# (b) THE THRESHOLD IS THE FIXTURE'S
# ======================================================================================

def test_k3_b_sweeping_the_gate_fixture_flips_the_same_persons_verdict():
    ts = GATE - 1
    control = _fold_kinds(_world(ts))
    assert "finding.none" in control and "finding.made" not in control, (
        f"the control: {ts} is not refused at the shipped gate: {control}")
    lower = P.DEFAULT_FIXTURES.sweep("thread_sensitivity_gate", ts)
    w = _world(ts, lower)
    assert _formed(w) is True, "the swept gate did not reach the person's own formation"
    assert "finding.made" in _fold_kinds(w), "the swept gate did not reach the fold"
    # the control point 0: every AUTHORED value passes, and an unauthored one still refuses
    zero = P.DEFAULT_FIXTURES.sweep("thread_sensitivity_gate", 0)
    assert "finding.made" in _fold_kinds(_world(0, zero))
    w0 = _world(None, zero)
    assert _formed(w0) is False and "finding.none" in _fold_kinds(w0), (
        "a person with no authored sensitivity passed a gate at 0 -- `None` read as 0")


# ======================================================================================
# (c) THE PARSE RULE
# ======================================================================================

@pytest.mark.parametrize("raw, want", [
    (35, 35), (0, 0), (None, None),
    ("75–80", 75), ("75-80", 75), ("75 — 80", 75),     # a range reads as its lower bound
    ("~50", 50), ("~ 50", 50),                                    # an approximate value as its number
])
def test_k3_c_the_authored_shapes_parse(raw, want):
    assert cast.thread_sensitivity_of({"id": "X", "ts": raw}) == want


@pytest.mark.parametrize("raw", ["high", "30", "", -5, True, 2.5, [30]])
def test_k3_c_any_other_shape_refuses_rather_than_guessing(raw):
    with pytest.raises(Unspecified):
        cast.thread_sensitivity_of({"id": "X", "ts": raw})


def test_k3_c_no_row_and_no_key_are_no_value_and_the_registry_reads_as_authored():
    assert cast.thread_sensitivity_of({}) is None
    assert cast.thread_sensitivity_of({"id": "X"}) is None
    # the registry's own rows: the two non-numeric shapes, a bare number, a `null # [GAP]`
    assert [cast.thread_sensitivity_of(cast.row(c)) for c in ("NPC-001", "NPC-002", "NPC-005", "NPC-006")] \
        == [75, 50, 35, None]
    every = {cid: cast.thread_sensitivity_of(r) for cid, r in cast.load().items()}
    assert sum(v is not None for v in every.values()) >= 1, "the registry read no value at all"


# ======================================================================================
# (d) `thread_read` HAS LEFT THE NO-PREDICATE SET
# ======================================================================================

def _authored_cell() -> dict:
    """`thread_read`'s `requires_typed:` exactly as `verb_table.yaml` authors it, read off the file
    rather than retyped here, so the mixed cell below is built on the shipped one."""
    import yaml
    doc = yaml.safe_load((pathlib.Path(__file__).resolve().parents[1] / "verb_table.yaml")
                         .read_text(encoding="utf-8"))
    rows = [r for r in doc["verbs"] if r.get("verb") == VERB]
    assert len(rows) == 1, f"{len(rows)} `{VERB}` rows in verb_table.yaml"
    return rows[0]["requires_typed"]


def test_k3_c_a_cell_mixing_an_own_state_stem_with_any_other_is_refused_at_load():
    """The person's own reading decides whether the row forms at all (`opening_set`), so a conjunct
    `OwnStateReader` cannot answer would read UNKNOWN and silently decline the verb for everybody.
    `build_typed_requires` refuses the mix at load. CONTROL: the shipped cell alone builds."""
    from ..data.requires import build_typed_requires
    own = _authored_cell()
    assert set(build_typed_requires("x", own).stems()) == OWN_STATE_STEMS, "the control did not build"
    mixed = {"all": [own, {"form": "existence", "of": "subject", "kind": "Person"}]}
    with pytest.raises(SystemExit, match=r"asks own-state stem\(s\)"):
        build_typed_requires("x", mixed)


def test_k3_d_thread_read_is_resolvable_and_its_precondition_evaluable():
    row = VERB_TABLE[VERB]
    assert row.precondition_evaluable(REQUIRES_PREDICATES), "the fold cannot evaluate its precondition"
    assert VERB in resolvable_verbs(), "`thread_read` is still in the no-predicate set"
    assert not getattr(row, "requires_decline_note", None), "a decline note on an evaluable row"
    assert set(row.requires_typed.stems()) == OWN_STATE_STEMS
    assert "actor" in row.requires_typed.operands(), "the gate is not read of the actor"


# ======================================================================================
# (e) NOTHING WRITES THE CARRIER IN PLAY
# ======================================================================================

def test_k3_e_the_carrier_has_no_matrix_row_and_the_gate_refuses_a_write():
    with pytest.raises(Unspecified):
        matrix_row("Person", "thread_sensitivity")
    w = _world(GATE)
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("thread_sensitivity", mint_token(w, WriteClass.ACTS),
                lambda: setattr(w.persons[ACTOR], "thread_sensitivity", 99),
                record_kind="Person", fieldname="thread_sensitivity", driver="Act")
    assert w.persons[ACTOR].thread_sensitivity == GATE, "the refused write landed"


#: The one place the engine assigns the carrier: the world build. A season step that wrote it would
#: make the gate a thing play can move, which the design forbids.
_BUILD = pathlib.Path(__file__).resolve().parents[1] / "harness" / "populated.py"


def test_k3_e_no_engine_source_outside_the_world_build_assigns_the_carrier():
    root = pathlib.Path(__file__).resolve().parents[1]
    sites, scanned = [], 0
    for path in sorted(root.rglob("*.py")):
        if "tests" in path.relative_to(root).parts:
            continue
        scanned += 1
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            targets = (node.targets if isinstance(node, ast.Assign)
                       else [node.target] if isinstance(node, (ast.AugAssign, ast.AnnAssign)) else [])
            for t in targets:
                if isinstance(t, ast.Attribute) and t.attr == "thread_sensitivity":
                    sites.append((path, node.lineno))
            if (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "setattr"
                    and len(node.args) >= 2 and isinstance(node.args[1], ast.Constant)
                    and node.args[1].value == "thread_sensitivity"):
                sites.append((path, node.lineno))
    assert scanned > 50, f"scanned {scanned} files -- the walk did not reach the engine"
    assert [p for p, _ in sites] == [_BUILD], f"the carrier is assigned at {sites}"


def test_k3_e_a_season_leaves_every_carrier_as_built():
    w = _world(GATE)
    w.persons["p_mid"].thread_sensitivity = GATE - 1
    before = {pid: p.thread_sensitivity for pid, p in w.persons.items()}
    P._run_d(w, lambda p, v, s, b: [P.Act_(w, p, VERB, payload={"subject": "Hh"})])
    assert {pid: p.thread_sensitivity for pid, p in w.persons.items() if pid in before} == before
    assert SeasonDriver  # imported for the fold the runs above drive
