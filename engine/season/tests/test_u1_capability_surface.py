"""B04.02 -- THE SKILL DEFINITION BLOCK, ITS EXPORTER CHECK AND ITS LEAF READER; ONE KIND.

`references/descriptor_registry.yaml: capabilities` defines each skill once (kind, gloss, base attribute, opposed_by,
untrained, grows_by, scale). `tools/export_descriptors.py::_capability_roster` validates it and cooks it into
`engine/engine_params/descriptors.json`; `engine/substrate/descriptors.py::CAPABILITIES` is the one runtime reader.
The kind is closed at `skill` (A-98 (4)); `decision/sheet.py::describe` returns a skill's or an attribute's gloss.

Each refusal test plants the defect in the registry the exporter reads, in process, and observes the exporter refuse
it -- the shipped block is the control (`test_the_shipped_block_loads_the_four_skills`).
"""
from __future__ import annotations

import copy
import os
import sys

import pytest

from engine.substrate import descriptors

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import export_descriptors as ed  # noqa: E402

_REAL_LOAD = ed.ci_common.load_yaml


def _plant(monkeypatch, edit) -> None:
    """Make the exporter read the shipped registry after `edit(reg)` has changed it."""
    def planted(path, default=None):
        reg = copy.deepcopy(_REAL_LOAD(path, default=default))
        edit(reg)
        return reg
    monkeypatch.setattr(ed.ci_common, "load_yaml", planted)


def test_the_shipped_block_loads_the_four_skills():
    """The control: the shipped `[skill]` roster exports, and the leaf reads the four rows it moved."""
    out = ed.build()["capabilities"]
    assert len(out["rows"]) == 4 and "arms" in out["rows"] and "inquiry" in out["rows"]
    assert out["kinds"] == ["skill"]
    assert set(descriptors.CAPABILITIES) == set(out["rows"])
    row = descriptors.capability("arms")
    assert row.kind == "skill" and row.base == "attr.body.agility" and row.opposed_by is None
    assert (row.floor, row.ceiling) == (0, 7) and row.grows_by == ("train", "practice", "use")
    assert descriptors.capability("argue").opposed_by == "attr.spirit.will"
    with pytest.raises(ValueError, match="capabilities"):
        descriptors.capability("no_such_skill")


def test_deleting_the_block_refuses_the_load(monkeypatch):
    _plant(monkeypatch, lambda reg: reg.pop("capabilities"))
    with pytest.raises(SystemExit, match="capabilities"):
        ed.build()


def test_a_definition_row_with_no_gloss_is_refused_naming_it(monkeypatch):
    def empty_gloss(reg):
        reg["capabilities"]["rows"]["inquiry"]["gloss"] = ""
    _plant(monkeypatch, empty_gloss)
    with pytest.raises(SystemExit, match="inquiry.*gloss"):
        ed.build()


def test_an_attribute_with_no_gloss_is_refused_naming_it(monkeypatch):
    def empty_gloss(reg):
        reg["attributes"]["mind"][0]["gloss"] = ""
    _plant(monkeypatch, empty_gloss)
    with pytest.raises(SystemExit, match="attr.mind.focus.*gloss"):
        ed.build()


def test_a_capability_row_of_a_kind_other_than_skill_is_refused(monkeypatch):
    """`IS-B2-CHAR-05`: a leftover `aptitude` (or `trait`) row is refused; A-98 governs and the roster is `[skill]`."""
    def aptitude(reg):
        reg["capabilities"]["rows"]["arms"]["kind"] = "aptitude"
    _plant(monkeypatch, aptitude)
    with pytest.raises(SystemExit, match="arms.*kind"):
        ed.build()


def test_a_base_outside_the_ten_attributes_is_refused(monkeypatch):
    """CORE's falsifier: change `argue`'s `base` to a name outside the ten and the exporter refuses."""
    def off_roster(reg):
        reg["capabilities"]["rows"]["argue"]["base"] = "attr.social.bonds"
    _plant(monkeypatch, off_roster)
    with pytest.raises(SystemExit, match="argue.*base"):
        ed.build()


def test_an_opposed_by_outside_the_ten_attributes_is_refused(monkeypatch):
    def off_roster(reg):
        reg["capabilities"]["rows"]["argue"]["opposed_by"] = "attr.mind.nothing"
    _plant(monkeypatch, off_roster)
    with pytest.raises(SystemExit, match="argue.*opposed_by"):
        ed.build()


@pytest.mark.parametrize("field,value", [("untrained", "invented"), ("grows_by", ["train", "fixed"])])
def test_a_value_outside_its_closed_set_is_refused(monkeypatch, field, value):
    def outside(reg):
        reg["capabilities"]["rows"]["copying"][field] = value
    _plant(monkeypatch, outside)
    with pytest.raises(SystemExit, match=f"copying.*{field}"):
        ed.build()


@pytest.mark.parametrize("scale", [[3, 1], [0], "0-7", [0, 7.5]])
def test_a_scale_that_is_not_an_integer_pair_with_floor_at_most_ceiling_is_refused(monkeypatch, scale):
    def bad_scale(reg):
        reg["capabilities"]["rows"]["copying"]["scale"] = scale
    _plant(monkeypatch, bad_scale)
    with pytest.raises(SystemExit, match="copying.*scale"):
        ed.build()


def test_describe_returns_the_gloss():
    from engine.season.decision.sheet import describe
    assert describe("inquiry") == "Finds things out: from a record, a place or a watched person."
    assert describe("inquiry") == descriptors.capability("inquiry").gloss
    # an attribute's gloss, by key: the leaf's text and no World
    assert describe("attr.mind.focus") == descriptors.ATTRIBUTE_GLOSSES["attr.mind.focus"]
    assert all(descriptors.ATTRIBUTE_GLOSSES[k] for k in descriptors.ATTRIBUTES)
    with pytest.raises(ValueError):
        describe("no_such_key")
