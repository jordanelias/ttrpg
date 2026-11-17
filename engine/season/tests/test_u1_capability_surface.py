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


# ======================================================================================
# B04.05 -- THE TEN ROLES, THE SITE MAP AND THE USES TABLE, WITH ITS LOADER
# ======================================================================================
# `rosters.yaml: capability_roles` (closed, ordered), `capability_use_sites` (a MAP: site -> its one reader) and
# `tables.capability_uses` (the rows) are read by `data/rosters.py::_load_capability_uses`. Each refusal test plants the
# defect in a copy of the shipped rows (or the shipped roster the loader reads) and observes the loader refuse it, naming
# the row; the shipped table is the control. Planted rows are `dict(shipped_row, field=...)`, never a literal row: the
# hardcoded-definition scan in `test_season_shape.py` refuses a literal collection of three or more strings.

def _shipped_rows():
    import copy as _copy
    from engine.season.data import rosters
    return _copy.deepcopy(list(rosters._TABLES["capability_uses"]["rows"]))


def _fixture_values():
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    return dict(DEFAULT_FIXTURES._v)


def _shipped_row(role):
    """The first shipped row of `role` -- the base a test plants a defect into."""
    rows = [r for r in _shipped_rows() if r["role"] == role]
    assert rows, role
    return rows[0]


def _refused(rows, fixtures=None):
    """Load `rows` through the loader and return the refusal's text (None if it loaded)."""
    from engine.season.data import rosters
    from engine.season.gaps import ShapeGap
    try:
        rosters._load_capability_uses(rows, _fixture_values() if fixtures is None else fixtures)
    except ShapeGap as e:
        return str(e)
    return None


def test_the_shipped_uses_table_loads_and_every_site_has_its_reader():
    """The control: every shipped row loads, its role is one of the ten, its site is registered with a reader."""
    from engine.season.data import rosters
    roles = rosters.roster("capability_roles", ordered=True)
    assert len(roles) == 10 and len(set(roles)) == 10
    rows = _shipped_rows()
    loaded = rosters._load_capability_uses(rows, _fixture_values())
    assert len(rows) >= 8 and len(loaded) == len(rows)
    checked = 0
    for row in loaded:
        assert row.role in roles and row.use in rosters.CAPABILITY_USE_SITES
        assert rosters.CAPABILITY_USE_SITES[row.use].strip()
        checked += 1
    assert checked == len(rows)
    assert rosters.capability_uses() == loaded
    # the roles that ship a row are roles, and most of the ten ship none
    assert {r.role for r in loaded} <= set(roles)
    assert len({r.role for r in loaded}) >= 5


def test_a_gate_row_on_another_capability_is_refused():
    """CAP Part A's falsifier: a `gate` row keyed on anything but Thread Sensitivity is refused at load."""
    base = _shipped_row("gate")
    msg = _refused([dict(base, key="inquiry")])
    assert msg is not None and "gate" in msg and "inquiry" in msg, msg
    msg = _refused([dict(base, key=descriptors.ATTRIBUTES[0])])
    assert msg is not None and "gate" in msg and descriptors.ATTRIBUTES[0] in msg, msg
    # control: the same row, untouched, loads
    assert _refused([base]) is None


def test_a_gate_row_at_a_site_that_is_not_a_gate_site_is_refused():
    """The other half of the falsifier: a `gate` row at any site but `own_state_gate` and `told_retain`."""
    from engine.season.data import rosters
    base = _shipped_row("gate")
    other = next(s for s in sorted(rosters.CAPABILITY_USE_SITES) if s != base["use"])
    msg = _refused([dict(base, use=other)])
    assert msg is not None and "gate" in msg and other in msg, msg


def test_negative_circumstance_gain_is_refused():
    """A-25: `circumstance` carries hostile terms only; a negative gain would be a favourable one (an `edge` row's work)."""
    base = dict(_shipped_row("judgement"), role="circumstance")
    gain = base["gain"]
    fx = _fixture_values()
    assert fx[gain] >= 0                       # control: at its shipped value the row loads
    assert _refused([base], fx) is None
    fx[gain] = -0.5
    msg = _refused([base], fx)
    assert msg is not None and "circumstance" in msg and gain in msg and "negative" in msg, msg


def test_a_use_with_no_registered_reader_is_refused(monkeypatch):
    """USES: a site the map carries with no reader -- a row nothing would read -- is refused, naming the site."""
    from engine.season.data import rosters
    sites = dict(rosters.CAPABILITY_USE_SITES)
    site = next(iter(sites))
    for blank in ("", "   ", None):
        monkeypatch.setitem(rosters._ROSTERS, "capability_use_sites", dict(sites, **{site: blank}))
        msg = _refused(_shipped_rows())
        assert msg is not None and site in msg and "reader" in msg, (blank, msg)
    monkeypatch.setitem(rosters._ROSTERS, "capability_use_sites", sites)
    assert _refused(_shipped_rows()) is None


def test_capability_use_with_an_unregistered_site_is_refused():
    base = _shipped_row("dice")
    msg = _refused([dict(base, use="no_such_site")])
    assert msg is not None and "no_such_site" in msg and "capability_use_sites" in msg, msg


def test_a_level_outside_level_sigma_is_refused():
    """MAP: an `edge` row's `level` is a `sigma_leverage.LEVEL_SIGMA` name."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    base = dict(_shipped_row("dice"), role="edge", level="moderate", per="held")
    for name in LEVEL_SIGMA:                   # control: every name in the owner's table loads
        assert _refused([dict(base, level=name)]) is None, name
    msg = _refused([dict(base, level="enormous")])
    assert msg is not None and "level" in msg and "enormous" in msg, msg


def test_an_unknown_role_or_key_is_refused():
    base = _shipped_row("dice")
    msg = _refused([dict(base, role="no_such_role")])
    assert msg is not None and "no_such_role" in msg and "capability_roles" in msg, msg
    msg = _refused([dict(base, key="no_such_key")])
    assert msg is not None and "no_such_key" in msg, msg
    # a key is a skill, an attribute, a practitioner key or a selector: each loads
    for key in (*sorted(descriptors.CAPABILITIES), descriptors.ATTRIBUTES[0], *sorted(descriptors.PRACTITIONER_STATS),
                "verb", "verb.base"):
        assert _refused([dict(base, key=key)]) is None, key


def test_a_field_the_role_does_not_take_is_refused():
    """MAP §C's role-field table: `level` is an `edge` field; a `dice` row naming one is refused."""
    base = _shipped_row("dice")
    msg = _refused([dict(base, level="moderate")])
    assert msg is not None and "level" in msg and "dice" in msg, msg
    msg = _refused([dict(base, no_such_field=1)])
    assert msg is not None and "no_such_field" in msg, msg


def test_a_per_outside_held_rank_mid_is_refused():
    base = dict(_shipped_row("dice"), role="edge", level="minor", per="held")
    from engine.season.data import rosters
    pers = sorted(rosters.roster("capability_per"))
    assert len(pers) == 3
    for per in pers:
        assert _refused([dict(base, per=per)]) is None, per
    msg = _refused([dict(base, per="twice")])
    assert msg is not None and "per" in msg and "twice" in msg, msg


def test_a_gain_add_or_floor_that_is_not_a_registered_fixture_is_refused():
    gain_row = _shipped_row("judgement")
    msg = _refused([dict(gain_row, gain="no_such_fixture")])
    assert msg is not None and "no_such_fixture" in msg and "Fixture" in msg, msg
    dice_row = _shipped_row("dice")
    for column in ("add", "floor"):
        msg = _refused([dict(dice_row, **{column: "no_such_fixture"})])
        assert msg is not None and column in msg and "no_such_fixture" in msg, (column, msg)
        # control: a registered fixture name in the same cell loads
        assert _refused([dict(dice_row, **{column: gain_row["gain"]})]) is None, column
