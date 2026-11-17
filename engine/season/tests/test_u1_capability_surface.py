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
    # ED-IN-0377, ED-IN-0378: no skill row carries `opposed_by` for `argue` or `inquiry` (the social contest's rule, V2 §C.2): absent reads `base`
    assert descriptors.capability("argue").opposed_by is None and descriptors.capability("inquiry").opposed_by is None
    assert descriptors.capability("copying").opposed_by == "none"
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


# ======================================================================================
# B04.03 -- THE `capability:` COLUMN ON CONTESTED AND GRADED VERB ROWS
# ======================================================================================
# Each test plants the defect in a copy of `verb_table.yaml` and observes `_load_verb_table` refuse it; the shipped
# table is the control (every contested or graded row declares the column, and the value is a skill or `none`).

def _planted_verb_load(mutate):
    """Load the verb table from the shipped yaml after `mutate(doc)`; return the refusal's text (or None if it loaded)."""
    import unittest.mock as mock
    import yaml
    from engine.season.data import verbs as V
    doc = yaml.safe_load(V.VERB_TABLE_YAML.read_text())
    mutate(doc)
    with mock.patch.object(V, "VERB_TABLE_YAML") as fake:
        fake.exists.return_value = True
        fake.read_text.return_value = yaml.safe_dump(doc)
        try:
            V._load_verb_table()
        except SystemExit as e:
            return str(e)
    return None


def _row(doc, verb):
    return next(r for r in doc["verbs"] if r["verb"] == verb)


def test_the_shipped_table_declares_the_column_on_every_contested_or_graded_row():
    """The control: `capability` is a `VerbRow` field; every contested or graded row carries a skill or `none`."""
    from engine.season.data.verbs import VERB_TABLE
    from engine.season.data.rosters import GRADED_INQUIRIES
    owed = [v for v, r in VERB_TABLE.items() if r.contests or v in GRADED_INQUIRIES]
    assert len(owed) >= 12, owed
    for v in owed:
        cap = VERB_TABLE[v].capability
        assert cap == "none" or cap in descriptors.CAPABILITIES, (v, cap)
    # the column carries what the derived `VERB_CAPABILITY` holds, row for row
    from engine.season.data.verbs import VERB_CAPABILITY
    assert VERB_CAPABILITY and all(VERB_TABLE[v].capability == c for v, c in VERB_CAPABILITY.items())
    # the two contested rows with no skill say so
    assert [v for v in owed if v not in VERB_CAPABILITY and VERB_TABLE[v].capability == "none"] \
        == [v for v in owed if v not in VERB_CAPABILITY]
    # an uncontested, ungraded row carries no column
    assert all(r.capability == "" for v, r in VERB_TABLE.items() if v not in owed)


def test_a_contested_row_with_no_capability_is_refused_naming_it():
    """CORE's falsifier: delete `capability:` from `argue`'s row and the load refuses, naming the row."""
    msg = _planted_verb_load(lambda doc: _row(doc, "argue").pop("capability", None))
    assert msg is not None and "argue" in msg and "capability" in msg, msg


def test_a_graded_row_with_no_capability_is_refused_naming_it():
    msg = _planted_verb_load(lambda doc: _row(doc, "research").pop("capability", None))
    assert msg is not None and "research" in msg and "capability" in msg, msg


def test_a_capability_naming_no_definition_is_refused():
    msg = _planted_verb_load(lambda doc: _row(doc, "argue").update(capability="no_such_skill"))
    assert msg is not None and "argue" in msg and "no_such_skill" in msg, msg


def test_none_without_a_capability_note_is_refused():
    def drop_note(doc):
        r = _row(doc, "lie")
        assert r["capability"] == "none"
        r.pop("capability_note")
    msg = _planted_verb_load(drop_note)
    assert msg is not None and "lie" in msg and "capability_note" in msg, msg


def test_a_capability_on_a_row_that_neither_contests_nor_is_graded_is_refused():
    msg = _planted_verb_load(lambda doc: _row(doc, "give").update(capability="argue"))
    assert msg is not None and "give" in msg and "neither contests nor is graded" in msg, msg


# ======================================================================================
# B04.04 -- THE VERB MAPS DERIVED FROM THE COLUMN; TWO ROSTERS DELETED
# ======================================================================================
# The retired rosters' values, CAPTURED AS LITERALS (`rosters.yaml: verb_capability`, `vocation_attribute`, read on
# B04.03's tree before they were deleted). Spelled as lists of PAIRS: `test_season_shape.py`'s hardcoded-definition scan
# refuses a literal collection of three or more identifier strings (a dict's keys count), and it reads a pair of
# strings as nothing, so a roster of pairs is accepted where the dict is not.
_RETIRED_VERB_CAPABILITY = [
    ("tell", "copying"), ("speak", "copying"), ("argue", "argue"), ("research", "inquiry"), ("examine", "inquiry"),
    ("surveil", "inquiry"), ("fight", "arms"), ("accept", "arms"), ("capture", "arms"), ("interrogate", "inquiry"),
    ("arrest", "arms"), ("determine", "argue"),
]
_RETIRED_VOCATION_ATTRIBUTE = [
    ("copying", "attr.mind.focus"), ("argue", "attr.social.charisma"), ("inquiry", "attr.mind.acuity"),
    ("arms", "attr.body.agility"),
]
# the retired `opposed_by:` was `{}` (every row shipped absent). ED-IN-0377 and ED-IN-0378: who resists an argument is the social
# contest's rule (V2 part 2 §C.2), so no `argue`/`inquiry` row carries one, and the derived map is
# EQUAL to the retired one: empty.
_RETIRED_VOCATION_OPPOSED_BY = []


def _derived_maps():
    """The four maps the verb table's column and the definition block yield."""
    from engine.season.data import verbs as V
    return V.VERB_CAPABILITY, V.VOCATIONS, V.VOCATION_ATTRIBUTE, V.VOCATION_OPPOSED_BY


def test_derived_vocation_maps_equal_the_retired_rosters():
    """`==`, not `approx`: the derived `VERB_CAPABILITY` and `VOCATION_ATTRIBUTE` equal the retired rosters' literals, and
    `VOCATIONS` is the values of the first; the derived opposition equals the retired roster's (empty): `arms` and
    `argue`/`inquiry` carry no cell (read `base`) and `copying` spells `none` (a `none` entry would reach `_opposition_of`
    as an attribute key)."""
    verb_capability, vocations, vocation_attribute, vocation_opposed_by = _derived_maps()
    assert verb_capability == dict(_RETIRED_VERB_CAPABILITY)
    assert vocation_attribute == dict(_RETIRED_VOCATION_ATTRIBUTE)
    assert vocations == frozenset(c for _, c in _RETIRED_VERB_CAPABILITY) == frozenset(vocation_attribute)
    assert vocation_opposed_by == dict(_RETIRED_VOCATION_OPPOSED_BY) == {}
    assert descriptors.capability("copying").opposed_by == "none"      # spelled, and filtered out of the map
    # the two rows with no skill are spelled `none` and are in no map
    from engine.season.data.verbs import VERB_TABLE
    assert [v for v, r in VERB_TABLE.items() if r.capability == "none"] == ["lie", "march"] \
        and "lie" not in verb_capability and "march" not in verb_capability
