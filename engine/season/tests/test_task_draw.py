"""B07.01 (workplan v12 part 10 cont. 2, batch B07-task-draw; 18-A, "Gate"): AN UNCONTESTED CONSEQUENTIAL ACT IS DRAWN.

Three resolution classes, one per writing row, derived at load (`data/verbs.py::_check_resolution_classes`): `contest` (the
row has `contests:`), `task` (a `rosters.yaml: graded_tasks` route), `bookkeeping` (`bookkeeping_verbs`), and the rows owed a
contest by their lane (`contest_owed`). The 18 task rows and `reconstruct` route through `graded_tasks` with `armed_by:
task_draw_arm`, so `Fixtures.task_draw_arm` decides whether the loop takes the route (`data/rosters.py::graded_route`); it
shipped `off` (the control) until B07.05 flipped it `on` on 18-A gate 5's reading; gate 2 still reads the control `off`.
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
        is the class, not the orphaned `capability:`/`difficulty:` (which refuses first, also naming it), nor a band-keyed
        `emits:` no route grades (B07.05 keyed `reconstruct`'s: flattened to the band an undrawn act reads)."""
        from ..data.rosters import UNROUTED_BAND

        def mutate(doc):
            row = _row(doc, verb)
            for k in [k for k in row if k.startswith(("capability", "difficulty"))]:
                row.pop(k)
            if isinstance(row.get("emits"), dict):
                row["emits"] = row["emits"][UNROUTED_BAND]
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
# gates 1 and 3 -- the arm `on` (B07.05)
# --------------------------------------------------------------------------------------------------------------------------

def gate1_counts(w) -> dict:
    """18-A gate 1's reading of one run world: "counts each Event carrying a `degree` by the verb of the act in its `causes`".
    `bands[verb][band]` counts those Events for a converted verb; `resolved[verb]` its RESOLVED acts, the acts whose Events carry
    a `degree` (UNDECIDED (12) (ii): a row refused before any draw is no resolved act); `success` the success Events of
    non-bookkeeping acts (a kind the row emits, not a refusal kind), `graded_success` those carrying a degree. A `contest_owed`
    row's success Events are counted apart (`owed_success`), outside the share: its degree is its owning lane's contest.
    [ASSUMPTION: the 90 % share's denominator leaves out `contest_owed` rows -- basis: UNDECIDED (1) (owed to the lane named,
    each owner deletes its verb from the roster as it adds `contests:`, so the row then joins the count) and UNDECIDED (4)'s
    precedent ("their gate is their own batch's"); read as written the share is 722 of 827 at seeds 0-2, every ungraded Event
    an owed row's.]"""
    bands: dict = defaultdict(Counter)
    resolved_ids: dict = defaultdict(set)
    graded_success = success = owed_success = refusals_checked = 0
    verb_success: Counter = Counter()
    banded_refusals: list = []
    act_of = {a.id: a for a in w.acts}
    for e in w.log:
        a = next((act_of[c] for c in e.causes if c in act_of), None)
        if a is None or a.verb not in VERB_TABLE or a.verb in BOOKKEEPING_VERBS:
            continue
        row = VERB_TABLE[a.verb]
        if a.verb in CONTEST_OWED:
            owed_success += e.kind in row.emits and e.kind not in row.emits_on_refusal
        elif e.kind in row.emits and e.kind not in row.emits_on_refusal:
            success += 1
            graded_success += e.degree is not None
        if a.verb in TASKS and e.kind in row.emits_on_refusal and e.kind not in row.emits:
            refusals_checked += 1                    # B07.10: a task act's refusal is no outcome and carries no band
            if e.degree is not None:
                banded_refusals.append((a.verb, e.kind, e.degree))
        if a.verb in CONVERTED and e.kind in row.emits and e.kind not in row.emits_on_refusal:
            verb_success[a.verb] += 1
        if a.verb in CONVERTED and e.degree is not None:
            bands[a.verb][e.degree] += 1
            resolved_ids[a.verb].add(a.id)
    return {"bands": {v: dict(c) for v, c in bands.items()}, "resolved": {v: len(s) for v, s in resolved_ids.items()},
            "success": success, "graded_success": graded_success, "owed_success": owed_success,
            "verb_success": dict(verb_success), "refusals_checked": refusals_checked, "banded_refusals": banded_refusals}


#: UNDECIDED (4)'s nine converted verbs refused or unexecuted before B07, built out by B12c, B22, B23 and B26 (a literal: the
#: test reads no prose). A converted verb with ten or more resolved acts and no success Event is `unbuilt`, and must be one.
UNBUILT_OK = {"train", "recruit", "work", "restore", "build", "found", "raze", "sabotage", "marshal"}


def gate1_verdict(per_seed: list) -> tuple:
    """`(failures, checked, totals)` over the seeds' `gate1_counts`: a failure is a converted verb with ten or more resolved
    acts that resolves in fewer than two bands or is 100 % one band. B07.10 (UNDECIDED (4)): one with ten or more resolved acts
    and zero success Events in the run is not built out, reported in the totals as `unbuilt` and neither failed nor checked."""
    bands: dict = defaultdict(Counter)
    resolved: Counter = Counter()
    verb_success: Counter = Counter()
    refusals_checked, banded_refusals = 0, []
    success = graded_success = owed_success = 0
    for c in per_seed:
        for v, b in c["bands"].items():
            bands[v].update(b)
        resolved.update(c["resolved"])
        verb_success.update(c["verb_success"])
        refusals_checked += c["refusals_checked"]
        banded_refusals += c["banded_refusals"]
        success += c["success"]
        graded_success += c["graded_success"]
        owed_success += c["owed_success"]
    failures, checked, unbuilt = [], 0, []
    for v in CONVERTED:
        if resolved[v] < 10:
            continue
        if not verb_success[v]:
            unbuilt.append(v)
            continue
        n = sum(bands[v].values())
        if len(bands[v]) < 2 or max(bands[v].values()) == n:
            failures.append((v, dict(bands[v]), resolved[v]))
        checked += 1
    return failures, checked, {"resolved": dict(resolved), "success": success, "graded_success": graded_success,
                               "owed_success": owed_success, "unbuilt": sorted(unbuilt), "verb_success": dict(verb_success),
                               "refusals_checked": refusals_checked, "banded_refusals": banded_refusals}


#: The number of converted verbs gate 1 must have examined (a non-vacuity floor, CLAUDE.md section 0.1 pt 2: the loop asserted something).
#: 18-A's text said ten; ten was reached only because `raze`'s REFUSALS carried a band and counted as resolved acts (premise-check F1,
#: UNDECIDED (13)). With a refusal carrying no band, nine verbs reach ten resolved acts at seeds 0 to 2, two seasons (reconstruct, tend,
#: forge, conceal, move, survey, migrate, train, carry: read @ B07.10), `carry` at exactly ten, so the floor is the honest count (UNDECIDED (14)).
#: [ASSUMPTION; medium; Jordan ruled 9, 2026-11-20; revert: 10 once a tenth verb is built out and reaches ten resolved acts at these fixtures]
GATE1_VERBS_FLOOR = 9


def test_converted_verb_resolves_in_at_least_two_bands():
    """18-A gate 1, at the SHIPPED fixtures: seeds 0 to 2, two seasons. Every converted verb with ten or more RESOLVED acts
    (acts whose Events carry a `degree`, UNDECIDED (12) (ii)) resolves in at least two bands and is not 100 % one band
    (`checked >= GATE1_VERBS_FLOOR` verbs), and Events carrying a degree are at least 90 % of the success Events of non-bookkeeping acts
    (a `contest_owed` row's left out, `gate1_counts`); no task row's refusal Event carries a degree (B07.10). RED with `task_draw_arm` `off` (no converted act carries a degree)."""
    failures, checked, t = gate1_verdict([gate1_counts(_realm(seed, 2)) for seed in (0, 1, 2)])
    assert not failures, failures
    assert checked >= GATE1_VERBS_FLOOR, (checked, t["resolved"])
    assert set(t["unbuilt"]) <= UNBUILT_OK, t["unbuilt"]                        # B07.10: not built out, not failed
    assert t["refusals_checked"] >= 1, t["refusals_checked"]                   # B07.10: a task refusal carries no band
    assert not t["banded_refusals"], t["banded_refusals"]
    assert t["success"] and t["graded_success"] >= 0.9 * t["success"], (t["graded_success"], t["success"])


def test_a_refused_task_act_carries_no_band():  # [ASSUMPTION: test name]
    """B07.10 (UNDECIDED (13) (i)): a drawn `tend` act on a patient already at his ceiling is drawn, then its write declines. A
    refusal is a precondition failed, never an outcome (04 section C.4): every Event is `tend.refused` with no degree, or
    `tend.failed` (the `draw` clause, an outcome) at `Failure`. 200 planted acts, each its own keyed draw. FALSIFIER:
    `_refusal_degree` returning `degree` stamps the band on the refusal and this fails."""
    from dataclasses import replace

    from .test_in10_record_operands import _resolve
    from .test_in12_step9 import PATIENT, _tend_acts, _world

    on = DEFAULT_FIXTURES.sweep("task_draw_arm", "on")
    w, d = _world(on)
    ceiling = w.fixtures.get("condition_scale")
    (act,) = _tend_acts(w)
    refused = failed = 0
    for i in range(200):
        w.persons[PATIENT].body = ceiling
        for e in _resolve(w, d, replace(act, id=f"{act.id}#{i}")):
            if e.kind == "tend.refused":
                assert e.degree is None, (i, e.degree)
                refused += 1
            else:
                assert e.kind == "tend.failed" and e.degree == "Failure", (i, e.kind, e.degree)
                failed += 1
    assert refused >= 1 and failed >= 1, (refused, failed)


#: The skill gate 3 plants on `tend` for its own duration (UNDECIDED (12) (i)): any of the five registered skills; `tend` ships
#: `capability: none` (a sixth skill moves the arm-off hashes; the skill is the `tend` lane's, B12c).
#: [ASSUMPTION: `inquiry`, one the hearth's two persons hold none of -- basis: UNDECIDED (12) (i) names no member of the five.]
PLANTED_SKILL = "inquiry"


def test_trained_tender_fails_less_than_default_and_neither_is_zero(rank_trained=3):
    """18-A gate 3, as UNDECIDED (12) (i) reads it: the odds respond to the pool the one rule reads. `tend` names no skill as
    shipped, so the test PLANTS one for its own duration (`tend`'s row `capability:` and `VERB_CAPABILITY`, the map `pool.py`
    reads, both monkeypatched to `PLANTED_SKILL`), with the arm `on` in the world's fixtures: a tender holding it at 3 against
    the same tender untrained (his score `pool_default`, D-U1-11j), 200 planted `tend` acts each -- the trained tender's
    Failure share is lower, and neither is 0. FALSIFIER: `rank_trained=0` (the plant reads nothing) fails the assertion."""
    from dataclasses import replace

    from .test_in10_record_operands import _resolve
    from .test_in12_step9 import PATIENT, TENDER, _tend_acts, _world

    assert VERB_TABLE["tend"].capability == "none" and "tend" not in VERBS.VERB_CAPABILITY   # CONTROL: shipped, no skill
    key = PLANTED_SKILL
    on = DEFAULT_FIXTURES.sweep("task_draw_arm", "on")

    def failure_share(rank) -> float:
        w, d = _world(on)
        assert key not in (w.persons[PATIENT].capability or {}) and key not in (w.persons[TENDER].capability or {})
        if rank is not None:
            w.persons[TENDER].capability = {**(w.persons[TENDER].capability or {}), key: rank}
        low = w.fixtures.get("condition_scale") * 2 // 5
        (act,) = _tend_acts(w)
        bands: Counter = Counter()
        for i in range(200):                     # 200 planted acts, each its own id and so its own keyed draw
            w.persons[PATIENT].body = low
            graded = [e.degree for e in _resolve(w, d, replace(act, id=f"{act.id}#{i}")) if e.degree is not None]
            assert len(graded) == 1, graded      # each act was drawn, and reports one band
            bands[graded[0]] += 1
        assert sum(bands.values()) == 200, bands
        return bands["Failure"] / 200

    with mock.patch.dict(VERB_TABLE, {"tend": replace(VERB_TABLE["tend"], capability=key)}), \
            mock.patch.dict(VERBS.VERB_CAPABILITY, {"tend": key}):
        trained, untrained = failure_share(rank_trained), failure_share(None)
    assert 0 < trained < untrained and untrained > 0, (trained, untrained)


# --------------------------------------------------------------------------------------------------------------------------
# B07.02 -- each magnitude and quality effect reads the band through one fraction
# --------------------------------------------------------------------------------------------------------------------------

def test_no_effect_names_a_band():
    """18-A edit 5, the falsifier: no `loop/effects_*.py` carries a string literal that is a band, so an effect reads the band
    only through `task_share` / `forge_quality_at` (`data/rosters.py`). `ast`, so a comment or a docstring does not count."""
    import ast
    from pathlib import Path

    from ..data.rosters import DEGREE_BANDS
    files = sorted((Path(__file__).resolve().parent.parent / "loop").glob("effects_*.py"))
    assert len(files) >= 4, files
    named = [(f.name, n.lineno, n.value) for f in files for n in ast.walk(ast.parse(f.read_text()))
             if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in DEGREE_BANDS]
    assert not named, named


def test_the_band_scales_each_magnitude_through_one_share():
    """`task_share` is the one table: a flat act (`None`) is share 1 and every band reads the `task_fraction` roster; the effects
    that scale a magnitude (`tend`, `_rise`) land the share of it, and with no band the whole -- the control the realm hash rests on."""
    from fractions import Fraction

    from ..data.rosters import DEGREE_BANDS, FORGE_QUALITY, TASK_FRACTION, forge_quality_at, task_share
    from ..loop.effects_economy import _rise
    from ..loop.effects_shared import EFFECTS
    from ..seam.contest import Resolution
    from .test_in12_step9 import PATIENT, _tend_acts, _world

    assert task_share(None) == 1 and set(TASK_FRACTION) == set(DEGREE_BANDS)
    assert {task_share(b) for b in DEGREE_BANDS} == set(TASK_FRACTION.values()) and Fraction(1, 2) in TASK_FRACTION.values()
    checked = 0
    for band, share in TASK_FRACTION.items():
        w, _d = _world()
        scale = w.fixtures.get("condition_scale")
        low = scale * 2 // 5
        w.persons[PATIENT].body = low
        (act,) = _tend_acts(w)
        EFFECTS["tend"](w, act, Resolution(band, {})).apply()
        assert w.persons[PATIENT].body == low + (scale - low) * share.numerator // share.denominator, (band, share)
        checked += 1
    assert checked == len(DEGREE_BANDS)
    # the flat act: no `res` is the whole headroom, `Failure` none, `Partial` strictly between
    w, _d = _world()
    site = next(s for s in w.sites.values() if s.condition < w.fixtures.get("condition_scale"))
    whole, half, none = _rise(w, site), _rise(w, site, Resolution("Partial", {})), _rise(w, site, Resolution("Failure", {}))
    assert whole > 0 and none == 0 and 0 < half < whole and _rise(w, site, Resolution("Success", {})) == whole, (whole, half, none)
    # the quality table: the unrouted act reads Success's row, Failure makes no document
    assert forge_quality_at(None) == FORGE_QUALITY["Success"] and forge_quality_at("Failure") is None
