"""B04.02 -- THE SKILL DEFINITION BLOCK, ITS EXPORTER CHECK AND ITS LEAF READER; ONE KIND.

`references/descriptor_registry.yaml: capabilities` defines each skill once (kind, gloss, base attribute, opposed_by,
untrained, grows_by, scale). `tools/export_descriptors.py::_capability_roster` validates it and cooks it into
`engine/engine_params/descriptors.json`; `engine/substrate/descriptors.py::CAPABILITIES` is the one runtime reader.
The kind is closed at `skill` (A-98 (4)); `decision/sheet.py::describe` returns a skill's or an attribute's gloss.

Each refusal test plants the defect in the registry the exporter reads, in process, and observes the exporter refuse
it -- the shipped block is the control (`test_the_shipped_block_loads_the_five_skills`).
"""
from __future__ import annotations

import copy
import os
import sys

import pytest

from engine.substrate import descriptors

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import export_descriptors as ed  # noqa: E402
from engine.dice_engine import draw as keyed_draw

_REAL_LOAD = ed.ci_common.load_yaml


def _plant(monkeypatch, edit) -> None:
    """Make the exporter read the shipped registry after `edit(reg)` has changed it."""
    def planted(path, default=None):
        reg = copy.deepcopy(_REAL_LOAD(path, default=default))
        edit(reg)
        return reg
    monkeypatch.setattr(ed.ci_common, "load_yaml", planted)


def test_the_shipped_block_loads_the_six_skills():
    """The control: the shipped `[skill]` roster exports, and the leaf reads its six rows (the four B04.02 moved, B04.18's `law` and B15.07's `healing`)."""
    out = ed.build()["capabilities"]
    assert len(out["rows"]) == 6 and {"arms", "inquiry", "healing"} <= set(out["rows"])
    assert out["kinds"] == ["skill"]
    assert set(descriptors.CAPABILITIES) == set(out["rows"])
    row = descriptors.capability("arms")
    assert row.kind == "skill"
    assert (row.floor, row.ceiling) == (0, 7) and row.grows_by == ("train", "practice", "use")
    # B05.25 step 7 (B05.99 rewrite): a skill row carries no `base:` and no `opposed_by:` any more -- the verb row names its
    # `governing:` and `opposed_attribute:` -- so no row's carrier has either field (was: `arms` base agility, `copying` `none`)
    assert all(not hasattr(r, "base") and not hasattr(r, "opposed_by") for r in descriptors.CAPABILITIES.values())
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
    from engine.season.data.rosters import GRADED_TASKS
    owed = [v for v, r in VERB_TABLE.items() if r.contests or v in GRADED_TASKS]
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


def test_the_shipped_uses_table_loads_and_every_site_is_registered():
    """The control: every shipped row loads, its role is one of the ten, its site is registered with a non-blank site string.
    (The string says where the reader is, or that none reads it yet -- `fight` and `kit`; this test does not check a reader exists.)"""
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


def test_a_judgement_row_its_reader_cannot_read_is_refused():
    """Phase 2 (`/code-review`): `_judgement_factor` reads the actor's own `attributes` at the row's key, so a `judgement` row
    keyed on a skill, or on `side: subject`, would load and read nothing. Each is refused naming the row."""
    base = _shipped_row("judgement")
    assert _refused([base]) is None                                    # control: the shipped row loads
    skill = sorted(descriptors.CAPABILITIES)[0]
    msg = _refused([dict(base, key=skill)])
    assert msg is not None and "judgement" in msg and skill in msg, msg
    msg = _refused([dict(base, side="subject")])
    assert msg is not None and "judgement" in msg, msg


def test_a_row_its_sites_reader_does_not_read_is_refused():
    """B04 Phase 3: the `social_roll` reader reads a `dice` row at `key: verb, side: actor` and an `opposes` row at `key: verb,
    side: subject`, one of each, and the gate's reader reads the actor's own value (`rosters.yaml: capability_site_reads`). A row
    that differs would load, change nothing the roll does, and be reported by `fed_by` as if it had. Each is refused, naming the
    row; the shipped rows are the control."""
    dice, opposes, gate = _shipped_row("dice"), _shipped_row("opposes"), _shipped_row("gate")
    for row in (dice, opposes, gate):
        assert _refused([row]) is None, row                                   # control: each shipped row loads
    msg = _refused([dict(dice, key=descriptors.ATTRIBUTES[0])])
    assert msg is not None and "dice" in msg and "key" in msg, msg           # a dice row keyed off `verb`
    msg = _refused([dict(dice, side="subject")])
    assert msg is not None and "dice" in msg and "side" in msg, msg          # a dice row on the other side
    msg = _refused([dict(opposes, side="actor")])
    assert msg is not None and "opposes" in msg and "side" in msg, msg
    msg = _refused([dice, dict(dice)])
    assert msg is not None and "second" in msg and "dice" in msg, msg        # a second dice row is reported and never read
    msg = _refused([dict(gate, side="subject")])
    assert msg is not None and "gate" in msg and "side" in msg, msg


def test_the_believed_roll_reads_the_same_terms_as_the_dealt_one(monkeypatch):
    """B04 Phase 3: `believed_input` (the chooser's `View.odds`) and `_read_social_roll` (the dealt roll) ask `_social_rows` which
    terms the table gives the roll. With the `opposes` row deleted the dealt roll reads no opposition, so the believed record
    carries none either and is no longer `None` (unknown) for want of a claim about the subject; with the `dice` row deleted both
    deal a pool of 0. FALSIFIER: a believer who still reads an opposition the table no longer gives."""
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.harness import probes as P
    from engine.season.seam.wrappers import sigma
    from engine.season.seam.wrappers import pool
    p = P.tiny_world().persons["p_low"]
    kw = dict(pool=3, person_subject=True)
    # B05.99 rewrite (B05.62 ships `believed_prior: ordinary`): a believer holding no claim of the subject no longer reads
    # `None` but the ORDINARY person's opposition (the untrained score + the attribute mid-point); the claim kept is the table's
    ordinary = pool.untrained(DEFAULT_FIXTURES) + pool.attribute_midpoint()
    # control: the shipped table gives the roll an opposition, and the believer reads it at the prior
    assert sigma.believed_input(p, "arrest", "p_mid", DEFAULT_FIXTURES, **kw).opposition == ordinary
    _rebound(monkeypatch, lambda rows: rows.__delitem__(next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "opposes")))
    inp = sigma.believed_input(p, "arrest", "p_mid", DEFAULT_FIXTURES, **kw)
    assert inp is not None and inp.opposition is None and inp.pool == 3
    _rebound(monkeypatch, lambda rows: rows.__delitem__(next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "dice")))
    assert sigma.believed_input(p, "arrest", "p_mid", DEFAULT_FIXTURES, **kw).opposition == ordinary   # `opposes` is back
    assert sigma._read_social_roll(P.tiny_world(), ["p_low", "p_mid"], verb="arrest", subject="p_mid")[0].pool == 0


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


def test_a_use_site_with_a_blank_site_string_is_refused(monkeypatch):
    """USES: a site the map carries with a blank site string (it names no reader and says none reads it) is refused, naming the
    site. The loader checks the string is non-blank, not that the reader it names exists."""
    from engine.season.data import rosters
    sites = dict(rosters.CAPABILITY_USE_SITES)
    site = next(iter(sites))
    for blank in ("", "   ", None):
        monkeypatch.setitem(rosters._ROSTERS, "capability_use_sites", dict(sites, **{site: blank}))
        msg = _refused(_shipped_rows())
        assert msg is not None and site in msg and "blank site string" in msg, (blank, msg)
    monkeypatch.setitem(rosters._ROSTERS, "capability_use_sites", sites)
    assert _refused(_shipped_rows()) is None


def test_an_unregistered_fixture_is_refused_by_the_load_all_hook_before_play(monkeypatch):
    """F21: `rosters.py` cannot name the Fixture registry (an import cycle), so `data/fixtures.py::load`, which `data.load_all()`
    calls on every driver construction, runs the Fixture checks: a `gain` that is no registered Fixture refuses there, naming
    the row. The control is the shipped table, which passes the same hook."""
    import copy
    from engine.season.data import fixtures, rosters
    from engine.season.gaps import ShapeGap
    fixtures.load()                                                      # control
    rows = copy.deepcopy(list(rosters._TABLES["capability_uses"]["rows"]))
    next(r for r in rows if r["role"] == "judgement")["gain"] = "no_such_fixture"
    monkeypatch.setitem(rosters._TABLES, "capability_uses", dict(rosters._TABLES["capability_uses"], rows=rows))
    with pytest.raises(ShapeGap, match="no_such_fixture"):
        fixtures.load()


def test_a_reader_spelling_an_unregistered_site_is_refused_at_import():
    """F17: each Python literal that names a site binds it through `rosters.require_use_site`, so a renamed site refuses
    rather than reading no capability. The control is the three shipped literals (each is a registered site)."""
    from engine.season.data import rosters
    from engine.season.decision.options import TOLD_CLAIM_CREDIT
    from engine.season.gaps import Unspecified
    from engine.season.queries.person_q import OWN_STATE_GATE
    from engine.season.seam.wrappers.sigma import SOCIAL_ROLL_SITE
    for literal in (TOLD_CLAIM_CREDIT, OWN_STATE_GATE, SOCIAL_ROLL_SITE):
        assert rosters.require_use_site(literal) == literal and literal in rosters.CAPABILITY_USE_SITES
    with pytest.raises(Unspecified, match="renamed_site"):
        rosters.require_use_site("renamed_site")


def test_capability_use_with_an_unregistered_site_is_refused():
    base = _shipped_row("dice")
    msg = _refused([dict(base, use="no_such_site")])
    assert msg is not None and "no_such_site" in msg and "capability_use_sites" in msg, msg


def test_a_row_missing_its_roles_required_field_is_refused():
    """F11: a `judgement` or `gate` row with no `gain`, and an `edge` row with no `level`, is refused at load, naming the row
    and the field. The control is the shipped row of each role, which loads."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    edge = _trait_use("edge", per="held", level=sorted(LEVEL_SIGMA)[0])      # no shipped row is an `edge`: plant one
    for role, need in (("judgement", "gain"), ("gate", "gain"), ("edge", "level")):
        row = edge if role == "edge" else _shipped_row(role)
        assert _refused([row]) is None, role                          # control: the row carries it
        planted = dict(row)
        del planted[need]
        msg = _refused([planted])
        assert msg is not None and need in msg and role in msg and row["use"] in msg, (role, msg)


def test_a_level_outside_level_sigma_is_refused():
    """MAP: an `edge` row's `level` is a `sigma_leverage.LEVEL_SIGMA` name."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    base = dict({k: v for k, v in _shipped_row("dice").items() if k not in ("add", "floor")}, role="edge", level="moderate", per="held")
    for name in LEVEL_SIGMA:                   # control: every name in the owner's table loads
        assert _refused([dict(base, level=name)]) is None, name
    msg = _refused([dict(base, level="enormous")])
    assert msg is not None and "level" in msg and "enormous" in msg, msg


def test_an_unknown_role_or_key_is_refused():
    base = next(r for r in _shipped_rows() if r["role"] == "dice" and r["use"] == "fight")     # a site no reader pins to one key
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
    base = dict({k: v for k, v in _shipped_row("dice").items() if k not in ("add", "floor")}, role="edge", level="minor", per="held")
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


# ---------------------------------------------------------------------------------------------------------------------
# B04.06 -- THE DECISION LAYER READS THE TABLE. `decision/options.py::competence` reads its key from the `told_claim_credit`
# row (through `_judgement_factor`), and `queries/person_q.py::OwnStateReader` reads the Thread gate's key and its threshold
# fixture from the `own_state_gate` row. The rebound table is the one the readers then see.
# ---------------------------------------------------------------------------------------------------------------------

def _rebound(monkeypatch, edit):
    """Make `capability_uses()` return the shipped rows after `edit(rows)` has changed them, loaded by the real loader."""
    from engine.season.data import rosters
    rows = _shipped_rows()
    edit(rows)
    monkeypatch.setattr(rosters, "_CAPABILITY_USES", rosters._load_capability_uses(rows, _fixture_values()))


def _hearer(**held):
    """A hand-built hearer holding the named attributes (`held`: `{attribute name: score}`), nothing else authored."""
    from engine.season.harness import probes as P
    p = P.tiny_world().persons["p_mid"]
    p.attributes = {descriptors.attribute_key(name): score for name, score in held.items()}
    return p


def _credit(p, gain=0.5):
    """The confidence `p` credits a told claim held at 60, on one channel, at the competence gain `gain`."""
    from engine.season.decision.options import refracted_confidence
    from engine.season.state.carriers import Claim
    c = Claim("c_x", "p_other", "Hh", "stores:grain", 8, 0, "told_by", 60, "own")
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    return refracted_confidence(p, c, "co_located", 0.5, fx=DEFAULT_FIXTURES.sweep("competence_gain", gain))


def test_repointing_told_claim_credit_moves_the_factor_with_no_decision_edit(monkeypatch):
    """USES' falsifier: re-point the `told_claim_credit` row at Perception in a rebound table and a hand-built hearer's
    refracted confidence follows Perception and ignores Attunement, with no edit under `decision/`."""
    low_attunement = dict(Attunement=2, Perception=6)
    low_perception = dict(Attunement=6, Perception=2)
    # control: the shipped row reads Attunement
    assert _credit(_hearer(**low_attunement)) < 60 and _credit(_hearer(**low_perception)) == 60

    def to_perception(rows):
        row = next(r for r in rows if r["use"] == "told_claim_credit")
        row["key"] = descriptors.attribute_key("Perception")
    _rebound(monkeypatch, to_perception)
    assert _credit(_hearer(**low_attunement)) == 60, "Attunement still moves the credit after the row was re-pointed"
    assert _credit(_hearer(**low_perception)) < 60, "Perception does not move the credit the re-pointed row names"


def test_a_use_with_no_row_reads_no_capability(monkeypatch):
    """`told_claim_credit` with no row is a factor of exactly 1 (a hearer who would be discounted is not), never a default."""
    from engine.season.queries import person_q
    low = _hearer(Attunement=2)
    assert _credit(low) < 60
    _rebound(monkeypatch, lambda rows: rows.__delitem__(next(i for i, r in enumerate(rows) if r["use"] == "told_claim_credit")))
    assert _credit(low) == 60
    gate = next(r for r in _shipped_rows() if r["role"] == "gate")["use"]
    _rebound(monkeypatch, lambda rows: rows.__delitem__(next(i for i, r in enumerate(rows) if r["use"] == gate)))
    ts = _hearer()
    ts.thread_sensitivity = 99
    reader = person_q.OwnStateReader(ts, _Fx())
    assert reader.read(ts.id, "thread_sensitivity") is person_q.UNKNOWN


class _Fx:
    """The Fixtures read the gate needs, as a bare `.get`."""
    def get(self, name):
        from engine.season.data.fixtures import DEFAULT_FIXTURES
        return DEFAULT_FIXTURES.get(name)


def test_the_own_state_reader_reads_its_threshold_fixture_and_its_key_from_the_gate_row(monkeypatch):
    """The gate's threshold is the row's `gain` fixture and its value is the row's key's held value: swapping the fixture
    name in the row moves the answer with no edit under `queries/`."""
    from engine.season.queries import person_q
    row = next(r for r in _shipped_rows() if r["role"] == "gate")
    p = _hearer()
    gate = _Fx().get(row["gain"])
    # the reader's two stems come from the same row
    p.thread_sensitivity = gate
    reader = person_q.OwnStateReader(p, _Fx())
    assert reader.read(p.id, "thread_sensitivity") == gate and reader.read(p.id, "thread_sensitivity.gate") == gate
    other = next(n for n in _fixture_values() if n != row["gain"] and isinstance(_fixture_values()[n], (int, float))
                 and _fixture_values()[n] != gate)
    _rebound(monkeypatch, lambda rows: next(r for r in rows if r["role"] == "gate").update(gain=other))
    assert reader.read(p.id, "thread_sensitivity.gate") == _Fx().get(other)


def test_the_substrate_forms_and_scale_of():
    """`about_mid` is 1 at the mid-point and linear about it; `scale_of` returns
    the attribute scale and a practitioner stat's bounds, and refuses a key with neither."""
    lo, hi = descriptors.ATTRIBUTE_FLOOR, descriptors.ATTRIBUTE_CEILING
    mid = (lo + hi) / 2
    assert descriptors.about_mid(mid, lo, hi, 1.0) == 1.0 and descriptors.about_mid(lo, lo, hi, 1.0) == 0.0
    assert descriptors.about_mid(hi, lo, hi, 0.5) == 1.5 and descriptors.about_mid(lo, lo, hi, 0.0) == 1.0
    assert descriptors.scale_of(descriptors.ATTRIBUTES[0]) == (lo, hi)
    assert descriptors.scale_of(next(iter(descriptors.PRACTITIONER_STATS)))[0] == 0
    with pytest.raises(ValueError, match="scale"):
        descriptors.scale_of("no_such_key")


# ======================================================================================
# B04.07 -- THE TRAIT ROSTER: HOME, EXPORTER, READER, HOLDING, USES  (U1 §2a steps 1-5; A-107)
# ======================================================================================
# `descriptor_registry.yaml: traits` defines each trait once; `export_descriptors.py::_trait_roster` validates it;
# `descriptors.TRAITS` reads it; `data/cast.py::traits_of` maps a cast row's `resonant_style:` through it into
# `Person.traits` (a frozenset, never `Person.capability`); `_load_capability_uses` accepts a trait key only at
# role `edge` with `per: held`. The shipped roster is the control in each test.

_TRAIT_IDS = ("moved_by_evidence", "moved_by_consequence", "moved_by_authority", "moved_by_solidarity")


def test_the_shipped_trait_roster_exports_and_the_leaf_reads_it():
    """The control: four traits, one `resonant_style` value each; `trait(id)` names the roster on a miss."""
    out = ed.build()["traits"]
    assert tuple(out["rows"]) == _TRAIT_IDS and out["scale"] == [0, 1]
    assert set(descriptors.TRAITS) == set(_TRAIT_IDS)
    assert {r.seated_by for r in descriptors.TRAITS.values()} == {"evidence", "consequence", "authority", "solidarity"}
    row = descriptors.trait("moved_by_evidence")
    assert row.id == "moved_by_evidence" and row.seated_by == "evidence" and row.gloss.strip()
    with pytest.raises(ValueError, match="traits"):
        descriptors.trait("no_such_trait")


def test_a_trait_id_that_is_also_a_skill_is_refused(monkeypatch):
    """One id, one roster: a trait row named for a skill is refused at the exporter, naming both."""
    def collide(reg):
        reg["traits"]["rows"]["arms"] = dict(reg["traits"]["rows"]["moved_by_evidence"])
        del reg["traits"]["rows"]["moved_by_evidence"]
    _plant(monkeypatch, collide)
    with pytest.raises(SystemExit, match="arms") as e:
        ed.build()
    assert "capabilities" in str(e.value)


def test_a_trait_row_that_breaks_the_schema_is_refused_naming_it(monkeypatch):
    """The other refusals of §2a step 2: an empty gloss, a `scale` other than [0, 1], a `seated_by` used twice."""
    def empty(reg):
        reg["traits"]["rows"]["moved_by_authority"]["gloss"] = " "
    _plant(monkeypatch, empty)
    with pytest.raises(SystemExit, match="moved_by_authority"):
        ed.build()
    monkeypatch.setattr(ed.ci_common, "load_yaml", _REAL_LOAD)
    _plant(monkeypatch, lambda reg: reg["traits"].update(scale=[0, 2]))
    with pytest.raises(SystemExit, match="scale"):
        ed.build()
    monkeypatch.setattr(ed.ci_common, "load_yaml", _REAL_LOAD)
    _plant(monkeypatch, lambda reg: reg["traits"]["rows"]["moved_by_solidarity"].update(seated_by="evidence"))
    with pytest.raises(SystemExit, match="evidence"):
        ed.build()
    monkeypatch.setattr(ed.ci_common, "load_yaml", _REAL_LOAD)
    _plant(monkeypatch, lambda reg: reg.pop("traits"))
    with pytest.raises(SystemExit, match="traits"):
        ed.build()


def test_a_row_key_outside_the_row_grammar_is_refused_naming_the_row(monkeypatch):
    """F18: a stray key on a skill row (a `lapses_by:` that A-106 removed, a typo of `grows_by`) and on a trait row is refused by
    the exporter, naming the row and the key; the shipped registry is the control (it builds)."""
    assert ed.build()["capabilities"]["rows"]
    for stray in ("lapses_by", "grows_bye"):
        monkeypatch.setattr(ed.ci_common, "load_yaml", _REAL_LOAD)
        _plant(monkeypatch, lambda reg, s=stray: reg["capabilities"]["rows"]["arms"].update({s: [1]}))
        with pytest.raises(SystemExit, match=f"capabilities.rows.arms.*{stray}"):
            ed.build()
        monkeypatch.setattr(ed.ci_common, "load_yaml", _REAL_LOAD)
        _plant(monkeypatch, lambda reg, s=stray: reg["traits"]["rows"]["moved_by_evidence"].update({s: 1}))
        with pytest.raises(SystemExit, match=f"traits.rows.moved_by_evidence.*{stray}"):
            ed.build()


def _trait_use(role="edge", key="moved_by_evidence", **cols):
    """A planted uses row at the `judgement` row's site, re-roled and re-keyed, then `cols` over it."""
    from engine.season.data import rosters
    base = _shipped_row("judgement")
    row = {"use": base["use"], "role": role, "key": key}
    if "side" in rosters._capability_role_fields(rosters.roster("capability_roles", ordered=True))[role]:
        row["side"] = "actor"                            # only where the role takes it: the refusal tested is the key's
    row.update(cols)
    assert row["use"] in rosters.CAPABILITY_USE_SITES
    return row


def test_a_trait_key_at_role_edge_with_per_held_loads():
    """The one place a trait key is accepted (U1 §2a step 5): the control for the refusals below."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    assert _refused([_trait_use("edge", per="held", level=sorted(LEVEL_SIGMA)[0])]) is None


def test_a_trait_key_outside_role_edge_is_refused():
    """A trait key at any role but `edge` is refused naming the row and the key; the roles are the whole closed set."""
    from engine.season.data import rosters
    refused = 0
    for role in rosters.roster("capability_roles", ordered=True):
        if role == "edge":
            continue
        msg = _refused([_trait_use(role)])
        assert msg is not None and "moved_by_evidence" in msg and "`edge`" in msg, (role, msg)
        refused += 1
    assert refused == 9


def test_a_dice_use_of_a_trait_is_refused():
    """MAP §G "Tests"; the falsifier of U1 §2a: a `dice` row keyed on a trait must not load."""
    msg = _refused([_trait_use("dice")])
    assert msg is not None and "moved_by_evidence" in msg and "dice" in msg and "`edge`" in msg, msg


def test_a_trait_key_with_per_other_than_held_is_refused():
    for per in ("rank", "mid"):
        msg = _refused([_trait_use("edge", per=per)])
        assert msg is not None and "moved_by_evidence" in msg and "held" in msg, (per, msg)
    msg = _refused([_trait_use("edge")])                 # no `per` at all is not `held` either
    assert msg is not None and "held" in msg, msg


def test_a_key_in_neither_roster_is_still_refused():
    msg = _refused([_trait_use("edge", key="moved_by_nobody", per="held")])
    assert msg is not None and "moved_by_nobody" in msg, msg


def test_an_unknown_resonant_style_is_refused():
    """`traits_of` refuses a `resonant_style` value no trait row seats, naming the row; absent or null holds none."""
    from engine.season.data import cast
    from engine.season.gaps import ShapeGap
    with pytest.raises(ShapeGap, match="Vengeance") as e:
        cast.traits_of({"id": "NPC-X", "resonant_style": "Vengeance"})
    assert "NPC-X" in str(e.value)
    assert cast.traits_of({"id": "NPC-X"}) == frozenset() == cast.traits_of({"resonant_style": None}) == cast.traits_of({})
    assert cast.traits_of({"resonant_style": "Evidence"}) == frozenset({"moved_by_evidence"})
    assert cast.traits_of({"resonant_style": "solidarity"}) == frozenset({"moved_by_solidarity"})


def test_a_trait_never_enters_person_capability():
    """On the shipped world: every cast row carrying `resonant_style:` seats exactly one trait on its person, a row
    without one seats none, `Person.traits` is a frozenset of defined trait ids, and no trait id is in any
    `Person.capability`. (The falsifier of §2a: a cast row's trait found in `Person.capability`.)"""
    from engine.season.boot.realm import build_realm, _slug
    from engine.season.data import cast
    w = build_realm(0)
    seen = styled = 0
    for cid, row in sorted(cast.load().items()):
        p = w.persons.get(f"p_{_slug(cid)}")
        if p is None:
            continue
        assert isinstance(p.traits, frozenset)
        if row.get("resonant_style"):
            assert len(p.traits) == 1 and p.traits <= set(descriptors.TRAITS), (cid, p.traits)
            styled += 1
        else:
            assert p.traits == frozenset(), (cid, p.traits)
        seen += 1
    assert styled == 18 and seen >= 46
    assert not any(set(p.capability) & set(descriptors.TRAITS) for p in w.persons.values())
    assert sum(1 for p in w.persons.values() if p.traits) == styled


# ---------------------------------------------------------------------------------------------------------------------
# B04.08 -- THE ROLL'S RECORD NAMES THE ROWS THAT FED IT (CAP A6 `fed_by`; MAP §G edit 6; D-U1-06: no `Event` field)
# ---------------------------------------------------------------------------------------------------------------------
def _arrest_roll(fixtures=None):
    """A hand-built `arrest` (a contested verb that stays on the single roll; the influence verbs' record is the social
    contest's V2 `Beat`, ED-IN-0378) resolved through the provider: `p_low` arrests `p_mid` on prize `a standing`."""
    import random
    from engine.season.harness import probes as P
    from engine.season.loop.driver import SeasonDriver
    from engine.season.seam.wrappers import sigma
    w = P.tiny_world(fixtures) if fixtures is not None else P.tiny_world()
    SeasonDriver(w)    # registers the module entry the prize row names
    return sigma.resolve(w, ["p_low", "p_mid"], ["c"], "a standing", verb="arrest", subject="p_mid", rng=keyed_draw.seeded(keyed_draw.H2("test_u1_capability_surface", 3)))


def test_fed_by_on_an_arrest_lists_its_dice_and_opposes_rows():
    """The record's `fed_by` is the `social_roll` rows that contributed, in table order: `==` on the `(use, role)` pairs,
    and the row's own `(key, side)` beside them; a value read and a contribution for each (the opposition halved by the
    module: `terms`'s own `opposition` entry, `Margin.terms`). The control is the table itself: the tuple is read off `capability_uses()`."""
    from engine.season.data import rosters
    out = _arrest_roll()
    assert out["status"] == "RESOLVED"
    assert tuple((f[0], f[1]) for f in out["fed_by"]) == (("social_roll", "dice"), ("social_roll", "opposes"))
    assert tuple((f[0], f[1], f[2], f[3]) for f in out["fed_by"]) == tuple(
        (r.use, r.role, r.key, r.side) for r in rosters.capability_uses() if r.use == "social_roll")
    dice, opposes = out["fed_by"]
    # INDEPENDENT of the record: the same actor and verb read through the pool owner and the opposition owner directly.
    from engine.season.harness import probes as P
    from engine.season.seam.wrappers import pool, sigma
    w = P.tiny_world()
    # B05 close: the `dice` value is the pool's own base (B05.25: the governing score plus the rank), not `score` (`max(pool_default, rank)`)
    assert dice[4] == pool.governing_score(w, w.persons["p_low"], "arrest") + pool.rank(w.persons["p_low"], "arrest")
    assert dice[5] == pool.faculty(w, w.persons["p_low"], "arrest") == out["pool"]
    # B05.14 (A-137; B05.99 re-pin): the `opposes` row's value is the opposition operand, his skill score PLUS his opposing
    # attribute (`_opposing`; the mid-point where unheld, B05.16), was the skill score alone (`_opposition_of`)
    assert opposes[4] is not None and opposes[4] == sigma._opposing(w, "p_mid", "arrest") != sigma._opposition_of(w, "p_mid", "arrest")
    assert opposes[5] == dict(out["terms"])["opposition"] and opposes[5] > 0      # B05.14: `Margin.terms` replaces `ob_terms`


def test_fed_by_follows_the_table_rows_in_table_order(monkeypatch):
    """FALSIFIER: a `fed_by` that names a row the roll did not read, or omits one it did, or fixes its own order. Swap the
    two `social_roll` rows in a rebound table: the record lists them in the table's order, and drops a deleted row."""
    def swap(rows):
        i = next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "dice")
        rows[i], rows[i + 1] = rows[i + 1], rows[i]
    _rebound(monkeypatch, swap)
    assert tuple((f[0], f[1]) for f in _arrest_roll()["fed_by"]) == (("social_roll", "opposes"), ("social_roll", "dice"))
    _rebound(monkeypatch, lambda rows: rows.__delitem__(next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "opposes")))
    out = _arrest_roll()
    assert tuple((f[0], f[1]) for f in out["fed_by"]) == (("social_roll", "dice"),)
    # THE PLAN'S FALSIFIER: a fed_by that omits a row the roll read. With the `opposes` row deleted the roll reads no
    # opposition, so nobody is opposite and the module's `opposition` term is the stand-in `opposed_ob(pool_default)` (a roll that read a
    # person anyway would carry his score and attribute), and the fed_by lists no `opposes` row to contribute it (above).
    from engine.dice_engine.sigma_leverage import opposed_ob
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    # B05.99 re-pin (B05.23 ships `opposition_rate` MU_PER_DIE): was 0.5 x pool_default
    assert dict(out["terms"])["opposition"] == opposed_ob(DEFAULT_FIXTURES.get("pool_default"), DEFAULT_FIXTURES.get("opposition_rate"))


def test_a_refused_roll_carries_fed_by_too():
    """S27.4's refusal returns the same record shape: `fed_by` is on the `REFUSED` dict as on the `RESOLVED` one."""
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    out = _arrest_roll(DEFAULT_FIXTURES.sweep("obstacle_refusal_multiple", 0))
    assert out["status"] == "REFUSED"
    assert tuple((f[0], f[1]) for f in out["fed_by"]) == (("social_roll", "dice"), ("social_roll", "opposes"))


# --- B04.14: one Endurance default in a fight -------------------------------------------------------------------

def test_party_end_default_is_the_combat_exports(monkeypatch):
    """`party_end` of a person who authors no Endurance, with no body bands, is the combat module's own default for
    `end` as `engine/engine_params/combat_engine_v1.json: sections.attributes.end.default` exports it -- read off
    `combat_kit`, not off the wrapper. FALSIFIER: patch the wrapper's one module-level read to 5 and the answer reads 5
    (a literal `4` in `party_end` would ignore the patch)."""
    from engine.season.harness import probes as P
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.seam.wrappers import combat
    from engine.substrate import combat_kit
    exported = combat_kit.END_DEFAULT       # the artifact's one reader (a second open of the path fails the bridge test)
    w = P.tiny_world()
    person = next(iter(w.persons.values()))
    person.attributes.pop(combat._END_KEY, None)
    assert combat.party_end(person, DEFAULT_FIXTURES) == exported
    monkeypatch.setattr(combat, "_END_DEFAULT", 5)
    assert combat.party_end(person, DEFAULT_FIXTURES) == 5


# ---------------------------------------------------------------------------------------------------------------------
# B04.15 -- A RANK NEVER PASSES ITS ROW'S CEILING. `loop/effects_combat.py::raised_capability` reads the ceiling of
# `descriptors.capability(key)` (the row's `scale`), the one place a rank is raised by `train` and by `_grown` alike.
# ---------------------------------------------------------------------------------------------------------------------

def _holder(**held):
    """A hand-built person holding the named skills at the named ranks (`held`: `{skill: rank}`), nothing else changed."""
    from engine.season.harness import probes as P
    p = P.tiny_world().persons["p_mid"]
    p.capability = dict(held)
    return p


def test_a_rank_at_its_ceiling_is_not_raised():
    """FALSIFIER: a rank of 8 reachable by `train` or `_grown`. At the row's ceiling `raised_capability` returns `None`; one below
    it, it returns the rank raised by one whole point, the other keys kept; a key not held is MINTED at 1 (B05.09, CORE Edit 9;
    B05.99 rewrite: it answered `None` under the retired never-minted rule)."""
    from engine.season.loop.effects_combat import raised_capability
    ceiling = descriptors.capability("arms").ceiling
    assert ceiling == 7
    assert raised_capability(_holder(arms=ceiling), "arms") is None
    assert raised_capability(_holder(arms=ceiling - 1, inquiry=2), "arms") == {"arms": ceiling, "inquiry": 2}
    assert raised_capability(_holder(inquiry=2), "arms") == {"arms": 1, "inquiry": 2}


# ---------------------------------------------------------------------------------------------------------------------
# B04.09 -- A CAST ROW MAY AUTHOR SKILL SCORES (CAP A7; CORE Edit 5). `data/cast.py::capabilities_of` is the one reader;
# the builder merges it over the lifepath expansion; the case overlay's `cast: capability:` is checked through it.
# The shipped registry authors no row, so each test plants the row it reads.

def test_a_cast_capability_naming_no_definition_is_refused():
    """FALSIFIER: a row naming an undefined skill that builds. `capabilities_of` refuses it naming the row and the roster;
    the overlay check refuses it through the same function (a defined skill no verb draws on is no longer refused there)."""
    from engine.season.data import cast
    from engine.season.gaps import ShapeGap
    with pytest.raises(ShapeGap, match="no_such_skill") as e:
        cast.capabilities_of({"id": "NPC-X", "capabilities": {"arms": 3, "no_such_skill": 2}})
    assert "NPC-X" in str(e.value) and "arms" in str(e.value)
    # a trait is no skill
    with pytest.raises(ShapeGap, match="moved_by_evidence"):
        cast.capabilities_of({"id": "NPC-X", "capabilities": {"moved_by_evidence": 1}})
    # a non-mapping refuses
    with pytest.raises(ShapeGap):
        cast.capabilities_of({"id": "NPC-X", "capabilities": ["arms"]})
    # the control: the shipped four load, and absence is `{}`
    assert cast.capabilities_of({"id": "NPC-X", "capabilities": {"arms": 3, "copying": 0}}) == {"arms": 3, "copying": 0}
    assert cast.capabilities_of({"id": "NPC-X"}) == {} == cast.capabilities_of({"capabilities": None}) == cast.capabilities_of({})
    from engine.season.harness import corpus_run
    with pytest.raises(SystemExit, match="no_such_skill"):
        corpus_run._check_capability("case", "Who", {"who": "Who", "capability": {"no_such_skill": 2}})
    corpus_run._check_capability("case", "Who", {"who": "Who", "capability": {"arms": 2}})


def test_a_cast_capability_above_its_scale_is_refused():
    """FALSIFIER: a rank above the row's ceiling that builds. The scale is the definition row's own `floor`..`ceiling`, read
    from `descriptors.CAPABILITIES`, never a number typed here; a bool, a fraction and a numeric string refuse as `attributes_of`'s do."""
    from engine.season.data import cast
    from engine.season.gaps import ShapeGap
    row = descriptors.CAPABILITIES["arms"]
    r = lambda v: {"id": "NPC-X", "capabilities": {"arms": v}}
    assert cast.capabilities_of(r(row.floor)) == {"arms": row.floor}
    assert cast.capabilities_of(r(row.ceiling)) == {"arms": row.ceiling}
    for bad in (row.ceiling + 1, row.floor - 1, True, 2.5, "3", None):
        with pytest.raises(ShapeGap, match="arms"):
            cast.capabilities_of(r(bad))
    from engine.season.harness import corpus_run
    with pytest.raises(SystemExit, match="whole number"):
        corpus_run._check_capability("case", "Who", {"who": "Who", "capability": {"arms": row.ceiling + 1}})


def test_an_authored_capability_wins_over_the_lifepath(monkeypatch):
    """On a built realm: a row whose lifepath holds `inquiry` at `pool_default` and which authors `capabilities: {inquiry: 5,
    arms: 4}` is built holding exactly that (the authored value wins, and a key the lifepath does not hold is added); a row
    with the lifepath alone is built as before (the control); a row with neither holds nothing."""
    from engine.season.boot.realm import build_realm
    from engine.season.data import cast
    from engine.season.data.rosters import LIFEPATH_TEMPLATES
    rows = {cid: dict(r) for cid, r in cast.load().items()}
    lifepath = next(k for k, v in LIFEPATH_TEMPLATES.items() if "inquiry" in v)
    both, only_path, neither = "NPC-087", "NPC-084", "NPC-086"
    assert not any(rows[c].get("lifepath") or rows[c].get("capabilities") for c in (both, only_path, neither))
    rows[both].update(lifepath=lifepath, capabilities={"inquiry": 5, "arms": 4})
    rows[only_path]["lifepath"] = lifepath
    monkeypatch.setattr(cast, "_CACHE", rows)
    w = build_realm(0)
    default = w.fixtures.get("pool_default")
    assert default != 5
    assert w.persons["p_npc_087"].capability == {"inquiry": 5, "arms": 4}
    assert w.persons["p_npc_084"].capability == {"inquiry": default}
    assert w.persons["p_npc_086"].capability == {}


# ---------------------------------------------------------------------------------------------------------------------
# B04.10 -- `rank_at_least` AS A `when` KEY (CAP A7; DEF Edit 2). The closed `when` roster is `rosters.yaml:
# capability_when_keys`; the loader refuses a key outside it and a `rank_at_least` it cannot read; `rosters.when_holds` is the
# one comparison, which the `edge` reader (B05) calls. No row ships, so each test plants the rows it reads. The tests read the
# SELECTED ROWS from the comparison, not a roll: the arm that turns levels into sigma lands in B05.
# ---------------------------------------------------------------------------------------------------------------------

def _rank_rows(**when_for_second):
    """Two `edge` rows on one skill at one site -- the first unconditioned, the second under the planted `when`."""
    first = dict(use="social_roll", role="edge", key="inquiry", side="actor", per="rank", level="minor")
    second = dict(first, level="strong", when=dict(when_for_second))
    return [first, second]


def test_rank_at_least_selects_a_second_use_row():
    """FALSIFIER: "(d)'s two holders read alike". With a second row under `rank_at_least: 3`, a holder at skill rank 2 and one at
    rank 3 select different rows, read as the level names (`==`, not `approx`); a person who holds no rank in the skill reads
    as rank 0 and selects the unconditioned row alone; and the row with no `when` holds for everyone."""
    from engine.season.data import rosters
    loaded = rosters._load_capability_uses(_rank_rows(rank_at_least=3), _fixture_values())
    assert [r.when for r in loaded] == [None, {"rank_at_least": 3}]
    levels = lambda holder: [r.level for r in loaded if rosters.when_holds(r, holder)]
    assert levels(_holder(inquiry=2)) == ["minor"]
    assert levels(_holder(inquiry=3)) == ["minor", "strong"]
    assert levels(_holder(inquiry=7)) == ["minor", "strong"]
    assert levels(_holder()) == ["minor"] and levels(_holder(arms=7)) == ["minor"]
    assert levels(_holder(inquiry=2)) != levels(_holder(inquiry=3))


def test_a_rank_at_least_the_loader_cannot_read_is_refused():
    """`rank_at_least` is a closed `when` key that names a skill rank on the row's scale: an unknown `when` key, a key that is no
    skill (an attribute, a trait), a bool, a fraction or a numeric string, a rank outside the scale, and a `gate` row (which takes
    no `when`: A-11) each refuse naming the row; the control rows load."""
    from engine.season.data import rosters
    ceiling = descriptors.capability("inquiry").ceiling
    assert rosters.roster("capability_when_keys") == frozenset({"rank_at_least"})
    assert _refused(_rank_rows(rank_at_least=ceiling)) is None and _refused(_rank_rows(rank_at_least=1)) is None
    msg = _refused(_rank_rows(sunset=3))
    assert msg is not None and "sunset" in msg and "when" in msg, msg
    for bad in (True, 2.5, "3", None, 0, ceiling + 1):
        msg = _refused(_rank_rows(rank_at_least=bad))
        assert msg is not None and "rank_at_least" in msg, (bad, msg)
    for key in (descriptors.attribute_key("Attunement"), "moved_by_evidence"):
        rows = _rank_rows(rank_at_least=3)
        rows[1]["key"] = key
        if key in descriptors.TRAITS:
            rows[1].update(per="held")
        msg = _refused(rows)
        assert msg is not None and "rank_at_least" in msg and key in msg, (key, msg)
    gate = dict(_shipped_row("gate"), when={"rank_at_least": 3})
    msg = _refused([gate])
    assert msg is not None and "when" in msg, msg


# ---------------------------------------------------------------------------------------------------------------------
# B04.11 -- A BUNDLE MAY GRANT A SKILL AT A RANK (CAP A7; DEF Edit 3). An entry of `lifepath_templates: holds:` is a bare id
# (held at `pool_default`, as ever) or `{<id>: <rank>}`, the rank checked against that skill's own `floor`..`ceiling`
# (`descriptors.CAPABILITIES`). `rosters._load_lifepaths` checks it; `cast.capability_of` expands it. No shipped
# entry is a mapping, so each test plants the cells it reads.
# ---------------------------------------------------------------------------------------------------------------------

def _bundle_cells(lifepath, holds):
    """The shipped `lifepath_templates` table with `lifepath`'s `holds:` replaced by `holds`."""
    from engine.season.data import rosters
    cells = {k: dict(v) for k, v in rosters.table("lifepath_templates").items()}
    cells[lifepath]["holds"] = holds
    return cells


def _load_bundles(cells):
    """What the module does at import over `cells`: the id table and the rank table, from the one loader."""
    from engine.season.data import rosters
    return rosters._load_lifepaths(cells, rosters.LIFEPATHS, frozenset(descriptors.CAPABILITIES))


def test_a_bundle_rank_above_its_scale_is_refused():
    """FALSIFIER: a `{id: 8}` entry that loads. The scale is the skill row's own `floor`..`ceiling`, never a number typed
    here; a bool, a fraction, a numeric string, a two-key mapping and an undefined id refuse too, naming the lifepath."""
    from engine.season.gaps import ShapeGap
    row = descriptors.CAPABILITIES["inquiry"]
    lp = "3-CR2"
    for ok in (row.floor, row.ceiling):                                    # the controls: both ends of the scale load
        ids, ranks = _load_bundles(_bundle_cells(lp, [{"inquiry": ok}]))
        assert ids[lp] == ("inquiry",) and ranks[lp] == {"inquiry": ok}
    for bad in (row.ceiling + 1, row.floor - 1, True, 2.5, "3", None):
        with pytest.raises(ShapeGap, match=lp):
            _load_bundles(_bundle_cells(lp, [{"inquiry": bad}]))
    for bad_entry in ({"inquiry": 2, "arms": 2}, {}, {"no_such_skill": 2}, 3):
        with pytest.raises(ShapeGap, match=lp):
            _load_bundles(_bundle_cells(lp, [bad_entry]))
    with pytest.raises(ShapeGap, match=lp):                                # one skill granted twice, bare and ranked
        _load_bundles(_bundle_cells(lp, ["inquiry", {"inquiry": 3}]))


def test_a_bare_bundle_id_keeps_the_untrained_value(monkeypatch):
    """FALSIFIER: a bare id read as anything but `pool_default`. A bundle of one bare id and one ranked entry expands (through
    `capability_of`) to the bare id at `pool_default` and the ranked one at its rank; the shipped table, every entry a bare id,
    expands each key to `pool_default` and carries no rank."""
    from engine.season.data import cast, rosters
    assert all(not r for r in rosters.LIFEPATH_RANKS.values())
    lp = "3-CH5"
    assert rosters.LIFEPATH_TEMPLATES[lp] == ("inquiry",)
    assert cast.capability_of({"id": "X", "lifepath": lp}, 2) == {"inquiry": 2}
    assert cast.capability_of({"id": "X", "lifepath": lp}, 5) == {"inquiry": 5}
    ids, ranks = _load_bundles(_bundle_cells(lp, ["inquiry", {"arms": 4}]))
    monkeypatch.setattr(cast, "LIFEPATH_TEMPLATES", ids)
    monkeypatch.setattr(cast, "LIFEPATH_RANKS", ranks)
    for default in (2, 5):
        assert cast.capability_of({"id": "X", "lifepath": lp}, default) == {"inquiry": default, "arms": 4}


# B04.12 -- THE CAST ROW'S UNREAD KEYS: READ, REMOVED OR LISTED (CAP A7; DEF Edit 4). `data/cast.py` refuses, when it reads the
# registry, a row carrying a key that is neither declared by the registry's own `schema:` block (`row_keys`) nor listed as unread (`UNREAD_KEYS`).

def _registry_with(tmp_path, monkeypatch, **extra_keys):
    """Point the cast loader at a one-row registry carrying `extra_keys`, with the cache cleared (restored at teardown)."""
    import yaml
    from engine.season.data import cast
    row = {"id": "NPC-X", "first_name": "A", "last_name": None, "faction": "Crown", "role": "r", "status": "canonical",
           **extra_keys}
    path = tmp_path / "npc_registry.yaml"
    shipped = cast.load_yaml(cast.NPC_REGISTRY_YAML.read_text(encoding="utf-8"))
    path.write_text(yaml.safe_dump({"schema": shipped["schema"], "characters": [row]}), encoding="utf-8")
    monkeypatch.setattr(cast, "NPC_REGISTRY_YAML", path)
    monkeypatch.setattr(cast, "_CACHE", None)
    return cast


def test_a_cast_row_key_neither_read_nor_unread_listed_is_refused(tmp_path, monkeypatch):
    """FALSIFIER: a row carrying a key nothing reads and nothing declares unread that builds. The three keys DEF Edit 4 deletes
    refuse (a deleted key that comes back is a key that invites a reader), a typo refuses, and each refusal names the row and the
    key; the controls are a read key (`resonant_style`), the two listed-unread keys, and the shipped registry (every key it
    carries is in one of the two sets, and the three deleted keys are gone from both of its levels)."""
    from engine.season.gaps import Unspecified
    for bad in ("arc_trajectory", "cultural_label", "self_other_initial", "resonant_stlye"):
        cast = _registry_with(tmp_path, monkeypatch, **{bad: "x"})
        with pytest.raises(Unspecified, match=bad) as e:
            cast.row("NPC-X")
        assert "NPC-X" in str(e.value)
    cast = _registry_with(tmp_path, monkeypatch, resonant_style="Evidence", certainty=2, coherence=9)
    assert cast.row("NPC-X")["certainty"] == 2
    assert {"certainty", "coherence", "first_name", "birthplace", "notes"} <= set(cast.UNREAD_KEYS)
    assert not set(cast.UNREAD_KEYS) & cast.row_keys(cast.load_yaml(cast.NPC_REGISTRY_YAML.read_text(encoding="utf-8")))   # one list
    monkeypatch.setattr(cast, "NPC_REGISTRY_YAML", cast.files.NPC_REGISTRY_YAML)
    monkeypatch.setattr(cast, "_CACHE", None)
    rows = cast.load()
    assert len(rows) >= 40
    carried = {k for r in rows.values() for k in r}
    shipped = cast.load_yaml(cast.NPC_REGISTRY_YAML.read_text(encoding="utf-8"))
    assert carried <= cast.row_keys(shipped) | set(cast.UNREAD_KEYS)
    assert not cast.row_keys(shipped) & {"arc_trajectory", "cultural_label", "self_other_initial"}
    with pytest.raises(Unspecified, match="schema"):                  # a registry that declares no keys is refused, not waved through
        cast.row_keys({"characters": []})
    assert {"certainty", "coherence"} <= carried                       # the listed keys are still authored, so the list is not vacuous
    assert not carried & {"arc_trajectory", "cultural_label", "self_other_initial"}
    assert not {k for r in rows.values() for k in (r.get("convictions") or {})} & {"cultural_label", "self_other_initial"}


def test_a_convictions_group_that_holds_no_list_is_refused():
    """B04 Phase 3: the two keys B04.12 deleted sat inside `convictions:` as scalars, and `pursuits_of` used to skip a group that
    held no list, so either would have loaded again. A scalar group is refused, naming the person and the group; a shipped row
    (the control) still reads."""
    from engine.season.data import cast
    from engine.season.gaps import Unspecified
    cid, shipped = next(iter(sorted(cast.load().items())))
    assert cast.pursuits_of(shipped)                                          # control
    for bad in ("cultural_label", "self_other_initial"):
        row = dict(shipped, convictions=dict(shipped["convictions"], **{bad: "x"}))
        with pytest.raises(Unspecified, match=bad):
            cast.pursuits_of(row)


# B04.13 -- THE DEVELOPMENT SHEET SHOWS THE PERSON (CAP A8; CORE Edit 6, DEF Edit 5). `decision/sheet.py::DevelopmentSheet` gains
# `attributes`, `thread_sensitivity`, `heritage` and `tenures`: the person's own state, copies only, no derived pool stored.

def _sheet_of(person_id: str, mutate=None):
    """Build the realm at seed 0, seat `person_id` at the development space, run the season until the first sheet is shown, and
    return it with what the stored Person held when it was shown (`mutate(w)` plants state first). The season stops at that
    first pick: nothing after it is read (accretion pass, B04's close)."""
    from engine.season.boot.realm import build_realm
    from engine.season.decision import make_chooser
    from engine.season.decision.sheet import creation_sheet, development_space, seat
    from engine.season.harness.play_surface import dispatching_chooser
    from engine.season.loop.driver import SeasonDriver, resolvable_verbs
    from engine.season.state.ids import H, draw_factory
    w = build_realm(0)
    if mutate is not None:
        mutate(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    seen: list = []

    class _Shown(Exception):
        pass

    def pick(sheet):
        q = w.persons[person_id]
        seen.append((sheet, {"thread_sensitivity": q.thread_sensitivity, "attributes": dict(q.attributes),
                             "tenures": tuple((t.kind, t.object) for t in q.tenures if t.until is None)}))
        raise _Shown
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw)
    space = development_space(w.fixtures, mint, pick, verbs=resolvable_verbs(), draw=draw)
    choose = dispatching_chooser(auto, seat(creation_sheet(w.persons.values()), person_id, space))
    try:
        SeasonDriver(w).season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    except _Shown:
        pass
    assert seen, f"{person_id} was never shown a sheet; the test observed nothing"
    return seen[0]


def test_development_sheet_shows_thread_sensitivity_heritage_and_tenures():
    """`p_npc_001` reads Thread Sensitivity 75 (DEF Edit 5 (c); her registry row's `ts: 75-80`). The sheet carries her attributes (a
    frozen copy, as `CreationRow` does), her heritage, and her live tenures as `(kind, object)` pairs in the order held; a closed
    tenure is not shown. FALSIFIER: a sheet field that reads a value not the person's own, or a live object a pick could write
    through. The controls are the stored person's own fields, equal to the sheet's, and the planted closed tenure that is absent."""
    from engine.season.state.carriers import Tenure

    def plant(w):
        p = w.persons["p_npc_001"]
        p.tenures.append(Tenure("t_b0413_open", p.id, "o_b0413_a", "hold", 0))
        p.tenures.append(Tenure("t_b0413_shut", p.id, "o_b0413_b", "commit", 0, until=0))
        p.heritage = "altonian"
    sheet, held = _sheet_of("p_npc_001", plant)
    assert sheet.thread_sensitivity == 75 == held["thread_sensitivity"]
    assert sheet.heritage == "altonian"
    assert dict(sheet.attributes) == held["attributes"] and len(sheet.attributes) == 10
    assert sheet.tenures == held["tenures"]
    assert ("hold", "o_b0413_a") in sheet.tenures and all(o != "o_b0413_b" for _, o in sheet.tenures)
    assert all(isinstance(e, tuple) and len(e) == 2 for e in sheet.tenures)
    with pytest.raises(TypeError):
        sheet.attributes["attr.mind.acuity"] = 9               # a copy, read-only
    assert not hasattr(sheet, "pool"), "a derived pool is stored on the sheet; the play surface asks View.odds"
