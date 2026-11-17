"""v10 CR-96 (AR-44): the OPTIONAL `opposed_by:` per skill definition row (B04.04: `descriptor_registry.yaml: capabilities`,
derived into `data/verbs.py::VOCATION_OPPOSED_BY`), executed.

WHAT THIS PINS, and the falsifier of each:

  * THE COLUMN IS READ -- a hand-built row `opposed_by: attr.spirit.will` makes a party holding Spirit 6 and the
    verb's own attribute 2 oppose at 6.0 (the obstacle halves it to 3), and the row without it at 2.0 (Ob 1).
    FALSIFIER: the column ignored is planted below and reads 2.0 with the row present.
  * THE POOL IS NOT MOVED -- the column is the opposition's only; `faculty` still starts from the row's own attribute.
  * THE SHIPPED MAP IS ABSENT ON EVERY ROW (ED-IN-0377: who resists an argument is the social contest's rule, V2 §C.2, not a skill-row column) -- so `_opposing_attribute` reads exactly what `_authored_attribute`
    does, for every verb and every person: the control for the hash (the realm hash is recorded in the commit body).
  * AN `opposed_by` OUTSIDE THE TEN IS REFUSED BY THE EXPORTER (`tools/export_descriptors.py::_capability_roster`).
"""
import importlib

import pytest

from engine.season.data.verbs import (   # TASK_DIFFICULTY: B11 lane A
    TASK_DIFFICULTY, VERB_CAPABILITY, VOCATION_ATTRIBUTE, VOCATION_OPPOSED_BY,
)
from engine.season.harness import probes as P
from engine.season.seam.wrappers import pool, sigma
from engine.substrate import composition, descriptors

TELL = "tell"                                   # draws on `copying`
VOC = VERB_CAPABILITY[TELL]
OWN = VOCATION_ATTRIBUTE[VOC]
SPIRIT = "attr.spirit.will"
ROLLER, HOLDER = "p_high", "p_low"


def _roll_module():
    """The obstacle's owner, reached by the composition row's string and lazily (as `test_cr20_attributes.py`)."""
    return importlib.import_module(composition.require("social_contest.roll").__module__)


def _w():
    """HOLDER: the verb's own attribute 2, Spirit 6. ROLLER: the own attribute 7, so the pool is 7 and the
    H-213 ceiling is clear of 3 (the opposition is read and halved, not capped)."""
    w = P.tiny_world()
    w.persons[HOLDER].attributes = {OWN: 2, SPIRIT: 6}
    w.persons[ROLLER].attributes = {OWN: 7}
    return w


def _obstacle(w):
    return _roll_module().obstacle(sigma.contest_input(w, [ROLLER], verb=TELL, subject=HOLDER))


def test_the_shipped_roster_is_absent_on_every_row_and_reads_the_row_own_attribute():
    assert VOCATION_OPPOSED_BY == {}, "a shipped row names an opposing attribute: CR-95's, not this position's"
    w = _w()
    checked = 0
    for verb in sorted(VERB_CAPABILITY) + ["determine"]:
        for pid in (HOLDER, ROLLER, "p_mid"):
            assert pool._opposing_attribute(w.persons[pid], verb) == pool._authored_attribute(w.persons[pid], verb)
            checked += 1
    assert checked >= 10


def test_a_row_with_opposed_by_spirit_opposes_at_the_spirit_and_the_row_without_it_at_the_own(monkeypatch):
    w = _w()
    # B11 lane A (rebased in B01.02): on the shipped `task` arm the obstacle is the task's difficulty (`tell`'s,
    # `rosters.yaml: task_difficulty`) plus the opposing score halved; was 1.0 and 3.0, the score halved alone (the
    # control arm, `obstacle_model: stand_in`, still reads them, below).
    d = TASK_DIFFICULTY[TELL]
    assert sigma._opposition_of(w, HOLDER, TELL) == 2.0 and _obstacle(w) == d + 1.0       # the row without it
    monkeypatch.setattr(pool, "VOCATION_OPPOSED_BY", {VOC: SPIRIT})
    assert sigma._opposition_of(w, HOLDER, TELL) == 6.0                                    # Spirit 6, not the own 2
    ob = _obstacle(w)
    assert ob == d + 3.0, f"Spirit 6 halves to 3, on the task's {d}; read {ob}"           # not capped: the roller's pool is 7
    w.fixtures = w.fixtures.sweep("obstacle_model", "stand_in")
    assert _obstacle(w) == 3.0                                                             # the control: the score halved alone


def test_the_column_replaces_the_own_attribute_and_is_not_the_larger_of_the_two(monkeypatch):
    """The own attribute 9 above Spirit 6: `opposed_by` REPLACES it, so the opposition reads 6.0, not the larger 9.0."""
    w = _w()
    w.persons[HOLDER].attributes = {OWN: 9, SPIRIT: 6}
    assert sigma._opposition_of(w, HOLDER, TELL) == 9.0                                    # the row without it: the own
    monkeypatch.setattr(pool, "VOCATION_OPPOSED_BY", {VOC: SPIRIT})
    assert sigma._opposition_of(w, HOLDER, TELL) == 6.0


def test_the_column_moves_the_opposition_and_not_the_pool(monkeypatch):
    w = _w()
    before = sigma.faculty(w, w.persons[HOLDER], TELL)
    monkeypatch.setattr(pool, "VOCATION_OPPOSED_BY", {VOC: SPIRIT})
    assert sigma.faculty(w, w.persons[HOLDER], TELL) == before == 2                        # the pool is still the own
    # B11 lane A (rebased in B01.02): on the shipped `task` arm a person holding the own attribute and no Spirit opposes
    # with `pool.score`'s fallback, `pool_default`, read on the OPPOSING attribute (so not his own 7); `None` (the
    # module's stand-in) on the control arm. Was `is None` on every arm.
    assert sigma._opposition_of(w, ROLLER, TELL) == float(w.fixtures.get("pool_default"))
    w.fixtures = w.fixtures.sweep("obstacle_model", "stand_in")
    assert sigma._opposition_of(w, ROLLER, TELL) is None                                   # the control: never the fallback


def test_the_planted_failure_the_column_ignored_reads_two_with_the_row_present(monkeypatch):
    """The 6.0 above can observe the failure it excludes: with `opposed_by` ignored, the row present reads 2.0."""
    w = _w()
    monkeypatch.setattr(pool, "VOCATION_OPPOSED_BY", {VOC: SPIRIT})
    assert sigma._opposition_of(w, HOLDER, TELL) == 6.0
    monkeypatch.setattr(pool, "_opposing_attribute", pool._authored_attribute)             # the column ignored
    monkeypatch.setattr(sigma, "_opposing_attribute", pool._authored_attribute)
    assert sigma._opposition_of(w, HOLDER, TELL) == 2.0 != 6.0


def test_the_held_key_still_competes_with_the_opposing_attribute(monkeypatch):
    w = _w()
    w.persons[HOLDER].capability = {VOC: 4}
    monkeypatch.setattr(pool, "VOCATION_OPPOSED_BY", {VOC: SPIRIT})
    assert sigma._opposition_of(w, HOLDER, TELL) == 6.0                                    # the larger of key 4 and Spirit 6
    w.persons[HOLDER].capability = {VOC: 9}
    assert sigma._opposition_of(w, HOLDER, TELL) == 9.0


def test_the_exporter_refuses_an_opposed_by_outside_the_ten(monkeypatch):
    """The retired loader's refusals at their new owner. Gone with their subject: "a row for a non-vocation" (a skill no verb
    names is reported, `verbs.skills_without_a_verb`, not refused)."""
    import copy, os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
    import export_descriptors as ed
    real = ed.ci_common.load_yaml
    assert SPIRIT in descriptors.ATTRIBUTES
    for bad in ("attr.mind.nonsense", "attr.social.bonds", ""):                  # none of the ten; retired; empty
        def planted(path, default=None, _bad=bad):
            reg = copy.deepcopy(real(path, default=default))
            reg["capabilities"]["rows"]["argue"]["opposed_by"] = _bad
            return reg
        monkeypatch.setattr(ed.ci_common, "load_yaml", planted)
        with pytest.raises(SystemExit, match="argue.*opposed_by"):
            ed.build()
    def spirit(path, default=None):
        reg = copy.deepcopy(real(path, default=default))
        reg["capabilities"]["rows"]["argue"]["opposed_by"] = SPIRIT
        return reg
    monkeypatch.setattr(ed.ci_common, "load_yaml", spirit)                       # the control: a valid opposition exports
    assert ed.build()["capabilities"]["rows"]["argue"]["opposed_by"] == SPIRIT
