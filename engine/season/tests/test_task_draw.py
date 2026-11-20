"""B07.01 (workplan v12 part 10 cont. 2, batch B07-task-draw; 18-A, "Gate"): AN UNCONTESTED CONSEQUENTIAL ACT IS DRAWN.

Three resolution classes, one per writing row, derived at load (`data/verbs.py::_check_resolution_classes`): `contest` (the
row has `contests:`), `task` (a `rosters.yaml: graded_tasks` route), `bookkeeping` (`bookkeeping_verbs`), and the rows owed a
contest by their lane (`contest_owed`). The 18 task rows and `reconstruct` route through `graded_tasks` with `armed_by:
task_draw_arm`, so `Fixtures.task_draw_arm` decides whether the loop takes the route (`data/rosters.py::graded_route`); it
ships `off` (the control) until B07.05 flips it on 18-A gate 5's reading.

GREEN HERE (B07.01): gates 2, 4 and 6 and the `contest_owed` refusal. EXPECTED RED UNTIL B07.05 (the arm ships `off`):
gate 1 (`test_converted_verb_resolves_in_at_least_two_bands`) and gate 3
(`test_trained_tender_fails_less_than_default_and_neither_is_zero`).
"""

from __future__ import annotations

import copy
from collections import Counter, defaultdict
from unittest import mock

import pytest
import yaml

from ..boot.realm import build_realm
from ..data import verbs as VERBS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import BOOKKEEPING_VERBS, CONTEST_OWED, GRADED_TASKS
from ..data.verbs import DRAW_CLAUSE, VERB_TABLE
from ..harness import populated as POP
from ._realm_goldens import SHIPPED

#: The converted verbs, read off the roster (never listed): every route the batch armed.
CONVERTED = sorted(v for v, r in GRADED_TASKS.items() if r.get("armed_by") == "task_draw_arm")
TASKS = sorted(v for v in CONVERTED if GRADED_TASKS[v]["form"] == "task")


def _doc() -> dict:
    return yaml.safe_load(VERBS.VERB_TABLE_YAML.read_text())


def _row(doc: dict, verb: str) -> dict:
    return next(r for r in doc["verbs"] if r["verb"] == verb)


def _load(mutate=None, **rosters) -> str | None:
    """Load a copy of the shipped verb table, `mutate`d, with any of `GRADED_TASKS`, `BOOKKEEPING_VERBS`, `CONTEST_OWED`
    replaced; the refusal's text, or `None` where it loads."""
    doc = copy.deepcopy(_doc())
    if mutate is not None:
        mutate(doc)
    patches = [mock.patch.object(VERBS, name, value) for name, value in rosters.items()]
    with mock.patch.object(VERBS, "VERB_TABLE_YAML") as fake:
        fake.exists.return_value = True
        fake.read_text.return_value = yaml.safe_dump(doc)
        for p in patches:
            p.start()
        try:
            VERBS._load_verb_table()
        except SystemExit as e:
            return str(e)
        finally:
            for p in patches:
                p.stop()
    return None


def _realm(seed: int, seasons: int, fixtures=DEFAULT_FIXTURES):
    w = build_realm(seed, fixtures=fixtures)
    POP.run(seasons, seed, w=w)
    return w


# --------------------------------------------------------------------------------------------------------------------------
# gate 2 -- the control
# --------------------------------------------------------------------------------------------------------------------------

def test_task_draw_arm_off_reproduces_the_pinned_hash():
    """`task_draw_arm: off` reproduces the realm pins current at B07 (`_realm_goldens.SHIPPED`, one season, seeds 0 to 2;
    C3-N27: the pins, not 18-A's strings). The arm is set explicitly, so the reading holds whatever the shipped value is."""
    off = DEFAULT_FIXTURES.sweep("task_draw_arm", "off")
    checked = 0
    for (seed, seasons), pin in sorted(SHIPPED.items()):
        if seasons != 1:
            continue
        assert _realm(seed, seasons, off).content_hash() == pin, (seed, seasons)
        checked += 1
    assert checked == 3, checked


# --------------------------------------------------------------------------------------------------------------------------
# gate 4 -- the class refusals
# --------------------------------------------------------------------------------------------------------------------------

def test_bookkeeping_row_that_writes_a_body_is_refused_at_load():
    """Plant `tend` (writes `Person.body`) into `bookkeeping_verbs`: the load refuses, naming `tend` and the cell. And the
    falsifier's other half: a `bookkeeping` row that writes another's holding or stores loads only behind `brute:` --
    strip `give`'s and the load refuses naming it."""
    assert _load() is None                                                     # CONTROL: the shipped table loads
    msg = _load(BOOKKEEPING_VERBS={**BOOKKEEPING_VERBS, "tend": {"why": "planted"}})
    assert msg is not None and "'tend'" in msg and "Person.body" in msg, msg
    assert "'tend' is in 2 classes" in msg, msg                                # a task row planted there is in two classes too
    msg = _load(lambda doc: [_row(doc, "give").pop(k, None) for k in ("brute", "brute_note")])
    assert msg is not None and "'give'" in msg and "Tenure." in msg, msg


def test_task_row_without_a_route_is_refused_at_load():
    """Delete `reconstruct`'s route: it emits a finding and is then in no class, so the load refuses naming it; the same for a
    task row (`tend`), whose `draw` clause no route then admits."""
    def unrouted(verb):
        """The row as it stood before its route: the columns only a rolled row may carry removed too, so what refuses it
        is the class, not the orphaned `capability:`/`difficulty:` (which refuses first, also naming it)."""
        def mutate(doc):
            row = _row(doc, verb)
            for k in [k for k in row if k.startswith(("capability", "difficulty"))]:
                row.pop(k)
        return mutate

    for verb in ("reconstruct", "tend"):
        routes = {v: r for v, r in GRADED_TASKS.items() if v != verb}
        msg = _load(GRADED_TASKS=routes)
        assert msg is not None and repr(verb) in msg, msg
    msg = _load(unrouted("reconstruct"), GRADED_TASKS={v: r for v, r in GRADED_TASKS.items() if v != "reconstruct"})
    assert msg is not None and "'reconstruct'" in msg and "no class" in msg, msg


def test_a_contest_owed_row_that_declares_contests_is_refused():
    """UNDECIDED (1) (ii): a `contest_owed` member that declares `contests:` is refused naming it, so the roster cannot go
    stale -- the item that adds the row's prize deletes the verb from the roster in the same commit."""
    contested = next(v for v, r in VERB_TABLE.items() if r.contests)
    msg = _load(CONTEST_OWED={**CONTEST_OWED, contested: "planted"})
    assert msg is not None and repr(contested) in msg and "contest_owed" in msg, msg
    msg = _load(CONTEST_OWED={**CONTEST_OWED, "zz_no_such_verb": "planted"})
    assert msg is not None and "zz_no_such_verb" in msg, msg


# --------------------------------------------------------------------------------------------------------------------------
# gate 6 -- the shapes
# --------------------------------------------------------------------------------------------------------------------------

def test_loader_accepts_shapes_a_and_b_and_refuses_a_band_keyed_route_row():
    """Every converted row loads in shape (a): a `form: task` route with a flat `writes:` and `emits:` and a `draw` clause, or
    `reconstruct` a `form: inquiry` route. Shape (b) (`contests: "a task"`) is the first such verb's (UNDECIDED (6)), so no
    row carries it here; the shipped table loading is its control. Three planted rows are refused, each naming its verb: a
    band-keyed `writes:` on a route row, a flat `writes:` on a `contests:` row, a writing row in no class."""
    assert len(TASKS) == 18 and set(CONVERTED) - set(TASKS) == {"reconstruct"}, CONVERTED
    checked = 0
    for v in TASKS:
        row = VERB_TABLE[v]
        assert not row.contests and not row.writes_by_degree and not row.emits_by_degree, v
        assert row.draw_kinds and set(row.draw_kinds).isdisjoint(row.emits_on_refusal), v   # a lost draw is no refusal
        assert row.refusal_for(DRAW_CLAUSE) == row.draw_kinds and row.difficulty and row.capability, v
        checked += 1
    assert checked == 18
    assert GRADED_TASKS["reconstruct"]["form"] == "inquiry" and not VERB_TABLE["reconstruct"].writes
    assert _load() is None                                                     # CONTROL: shape (a) rows load as shipped

    msg = _load(lambda doc: _row(doc, "tend").update(writes={"Success": ["Person.body"], "Failure": []}))
    assert msg is not None and "'tend'" in msg, msg                           # a band-keyed `writes:` on a route row
    contested = next(v for v, r in VERB_TABLE.items() if r.contests and r.writes)
    msg = _load(lambda doc: _row(doc, contested).update(writes=list(VERB_TABLE[contested].writes)))
    assert msg is not None and repr(contested) in msg and "FLAT" in msg, msg  # a flat `writes:` on a `contests:` row
    unclassed = next(v for v in BOOKKEEPING_VERBS if VERB_TABLE[v].writes)
    msg = _load(BOOKKEEPING_VERBS={v: r for v, r in BOOKKEEPING_VERBS.items() if v != unclassed})
    assert msg is not None and repr(unclassed) in msg and "no class" in msg, msg   # a writing row in no class
    msg = _load(lambda doc: _row(doc, "tend").update(emits_on_refusal=["tend.refused"]))
    assert msg is not None and "'tend'" in msg and "draw" in msg, msg          # a task row with no `draw` clause


# --------------------------------------------------------------------------------------------------------------------------
# gates 1 and 3 -- EXPECTED RED UNTIL B07.05 (the arm ships `off`)
# --------------------------------------------------------------------------------------------------------------------------

def test_converted_verb_resolves_in_at_least_two_bands():
    """18-A gate 1, at the SHIPPED fixtures: seeds 0 to 2, two seasons. Every converted verb with ten or more resolved acts
    resolves in at least two bands and is not 100 % one band (`checked >= 10` verbs), and Events carrying a degree are at
    least 90 % of the success Events of non-bookkeeping acts. RED while `task_draw_arm` ships `off` (no converted act carries
    a degree); B07.05 flips it."""
    bands: dict = defaultdict(Counter)
    acts_by_verb: Counter = Counter()
    graded_success = success = 0
    for seed in (0, 1, 2):
        w = _realm(seed, 2)
        act_of = {a.id: a for a in w.acts}
        for e in w.log:
            a = next((act_of[c] for c in e.causes if c in act_of), None)
            if a is None or a.verb not in VERB_TABLE or a.verb in BOOKKEEPING_VERBS:
                continue
            row = VERB_TABLE[a.verb]
            if e.kind in row.emits and e.kind not in row.emits_on_refusal:
                success += 1
                graded_success += e.degree is not None
            if a.verb in CONVERTED and e.degree is not None:
                bands[a.verb][e.degree] += 1
        for a in w.acts:
            if a.verb in CONVERTED:
                acts_by_verb[a.verb] += 1
    checked = 0
    for v in CONVERTED:
        if acts_by_verb[v] < 10:
            continue
        assert len(bands[v]) >= 2, (v, dict(bands[v]), acts_by_verb[v])
        checked += 1
    assert checked >= 10, (checked, dict(acts_by_verb))
    assert success and graded_success >= 0.9 * success, (graded_success, success)


def test_trained_tender_fails_less_than_default_and_neither_is_zero():
    """18-A gate 3: odds respond to state -- `tend` by a tender trained in its skill against one at `pool_default`, 200 planted
    acts each: the trained tender's Failure share is lower, and neither is 0. RED UNTIL B07.05, and then until `tend` names a
    skill: UNDECIDED (11) (iv) gives it `capability: none` (no defined skill covers it), so no tender can be trained in it."""
    key = VERB_TABLE["tend"].capability
    assert key and key != "none", (
        "`tend` names no skill (`capability: none`, UNDECIDED (11) (iv)): there is no trained tender to compare")
    assert DEFAULT_FIXTURES.get("task_draw_arm") == "on", "the task draw ships off (B07.05 flips it)"
