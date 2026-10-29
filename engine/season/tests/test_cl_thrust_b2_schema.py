"""CL-THRUST B2.1 / B2.2 (batch B10-05 landing) -- THE SCHEMA ONLY: the closed `thrust_axes` roster, the
optional `axis:` key on a goal row, and the top-level `goal_stages` list, all read by the ONE loader
`data/goals.py`. Nothing reads a stage yet (`current_stage` is B3.1), no row is authored, and no hash moves.

A loader that cannot refuse is absent (`CLAUDE.md` §0.1 pt 2). Every refusal the entry lists is PLANTED here,
each by ONE mutation of one valid base document, so the refusal is isolated from the others; the base loads
first (the control). Each plant must raise the loader's OWN refusal type (a `ShapeGap`, never the builder's
`SystemExit`), naming the row, and the loops assert that they ran (`assert checked >= N`).

Struck by the M20 ruling and NOT built: a stage `deadline` and the row keys `closing`, `successor` and `deal`.
They are planted below as refused keys, and absent from the carriers' fields.
"""
from __future__ import annotations

import copy
import dataclasses

import pytest
import yaml

from engine.season.data import files, goals, rosters
from engine.season.data.requires import WORLD_ONLY_STEMS, build_typed_requires
from engine.season.data.rosters import roster, roster_map
from engine.season.gaps import Forbidden, Unspecified

# Two pursuits a stage may weigh, named one per statement: the roster is owned by `references/descriptor_registry.yaml`
# (`tests/valoria/test_conviction_roster_single_owner.py` refuses two roster members in one container).
_PURSUIT_A = "honour"
_PURSUIT_B = "stability"

# The stage cells. `of: subject` is the grammar's own operand (`requires_operands` has no `referent`: the
# stage binds `subject := each referent` at read time, B3.1). `relation` `held_by` asks `held_by` and `existence`
# asks `exists`: stems a claim in a person's own ledger answers. (`own_ledger` asks `claim.held`, which no
# claim answers person-side -- WITNESS deposits none -- so the loader REFUSES it, planted below.)
_HELD = {"form": "relation", "of": "subject", "relation": "held_by"}
_EXISTS = {"form": "existence", "of": "subject", "kind": "Proposition"}


def _goal(gid, org, obj, **more):
    return {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_cl_thrust_b2_schema", **more}


def _stage(sid, term, cell, pursuits=None):
    return {"id": sid, "term": term, "predicate": copy.deepcopy(cell),
            "pursuits": {"honour": 1} if pursuits is None else pursuits}


def _base() -> dict:
    """A valid document: one orientation goal, three goals that mint a Proposition (two carrying an `axis:`,
    one a pole that is not among the ten), and two stage rows -- one for one goal, one for two goals, with a
    term repeated (non-decreasing is lawful) and a mixed cell."""
    return {
        "goals": [
            _goal("g_orient", {"faction": "Löwenritter"}, {"kind": "orientation"}),
            _goal("g_throne", {"faction": "Crown"}, {"kind": "seat_holders", "seats": ["off_king"]},
                  stance=1, axis="political_authority"),
            _goal("g_rung", {"faction": "Hafenmark"}, {"kind": "rung", "rung": "terr_T9"},
                  axis="uphold_church"),
            _goal("g_deeds", {"faction": "Varfell"}, {"kind": "deed_doers", "kinds": ["bond.formed"]}),
        ],
        "goal_stages": [
            {"id": "gs_throne", "for": ["g_throne"],
             "stages": [_stage("s1", "short", _HELD), _stage("s2", "long", _EXISTS)]},
            {"id": "gs_pair", "for": ["g_rung", "g_deeds"],
             "stages": [_stage("s1", "short", _HELD),
                        _stage("s2", "medium", {"all": [_HELD, _EXISTS]}),
                        _stage("s3", "medium", _EXISTS),
                        _stage("s4", "long", _HELD, {_PURSUIT_A: 0.5, _PURSUIT_B: 2})]},
        ],
    }


def _mut(mutate) -> dict:
    """`_base()` with `mutate(doc)` applied: the only edit made."""
    doc = _base()
    mutate(doc)
    return doc


def _row(doc, rid):
    return next(r for r in doc["goal_stages"] if r["id"] == rid)


def _stg(doc, rid, sid):
    return next(s for s in _row(doc, rid)["stages"] if s["id"] == sid)


def _goal_row(doc, gid):
    return next(r for r in doc["goals"] if r["id"] == gid)


def _set_goal(gid, key, value):
    return _mut(lambda d: _goal_row(d, gid).__setitem__(key, value))


def _set_row(rid, key, value):
    return _mut(lambda d: _row(d, rid).__setitem__(key, value))


def _drop_row(rid, key):
    return _mut(lambda d: _row(d, rid).pop(key))


def _set_stage(rid, sid, key, value):
    return _mut(lambda d: _stg(d, rid, sid).__setitem__(key, value))


def _drop_stage(rid, sid, key):
    return _mut(lambda d: _stg(d, rid, sid).pop(key))


def _set_terms(rid, *terms):
    """`_base()` with the terms of row `rid`'s stages, in order, replaced by `terms` (one per stage)."""
    def mutate(d):
        stages = _row(d, rid)["stages"]
        assert len(stages) == len(terms)
        for stage, term in zip(stages, terms):
            stage["term"] = term
    return _mut(mutate)


# ------------------------------------------------------------------------------ the control

def test_a_valid_hand_built_document_loads_and_each_goal_carries_its_row():
    got = {g.id: g for g in goals.parse(_base())}
    assert list(got) == [r["id"] for r in _base()["goals"]], "file order, one Goal per row"
    # the axes: a member of the ten, a pole that is not among them, and none
    assert got["g_throne"].axis == "political_authority" and got["g_rung"].axis == "uphold_church"
    assert got["g_orient"].axis is None and got["g_deeds"].axis is None
    # the stage rows: attached to every goal they are `for:`, shared, and absent elsewhere
    one, pair = got["g_throne"].stages, got["g_rung"].stages
    assert (one.id, one.for_goals) == ("gs_throne", ("g_throne",))
    assert (pair.id, pair.for_goals) == ("gs_pair", ("g_rung", "g_deeds"))
    assert got["g_deeds"].stages is pair, "one row, one object, however many goals it is for"
    assert got["g_orient"].stages is None, "a goal in no row has none"
    # ordered, with the authored ids, terms and pursuits
    assert [s.id for s in pair.stages] == ["s1", "s2", "s3", "s4"]
    terms = [s.term for s in pair.stages]    # not spelled as a list: three roster members in a body is a duplicate
    assert terms[0] == "short" and terms[1] == terms[2] == "medium" and terms[3] == "long"
    assert pair.stages[3].pursuits == {_PURSUIT_A: 0.5, _PURSUIT_B: 2}
    # the predicate IS the typed-requires builder's own product, not a second reading of the cell
    assert pair.stages[0].predicate == build_typed_requires("probe", _HELD)
    assert pair.stages[1].predicate == build_typed_requires("probe", {"all": [_HELD, _EXISTS]})


def test_a_missing_goal_stages_key_reads_as_empty_and_nothing_else_moves():
    """THE SHIPPED STATE: no `goal_stages` key and no `axis:`. An explicit `[]` is the same document."""
    bare = _base()
    del bare["goal_stages"]
    for row in bare["goals"]:
        row.pop("axis", None)
    explicit = copy.deepcopy(bare)
    explicit["goal_stages"] = []
    got = goals.parse(bare)
    assert got == goals.parse(explicit) and len(got) == 4
    assert all(g.axis is None and g.stages is None for g in got)


def test_the_shipped_goals_file_carries_no_axis_and_no_goal_stages_and_loads_unchanged(monkeypatch):
    raw = yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))
    assert "goal_stages" not in raw, "no stage is authored in this landing"
    assert not any("axis" in r for r in raw["goals"]), "no shipped row carries an axis"
    monkeypatch.setattr(goals, "_CACHE", None)
    loaded = goals.goals()
    checked = 0
    for g in loaded:
        assert g.axis is None and g.stages is None, g.id
        checked += 1
    assert checked == len(raw["goals"]) >= 9, checked


# ------------------------------------------------------------------------------ B2.1: the roster and `axis:`

def test_thrust_axes_is_a_closed_roster_whose_opposes_names_only_members():
    axes = roster("thrust_axes")
    assert rosters._ROSTERS["thrust_axes"]["open"] is False
    # one membership per assert: spelling the roster together would DUPLICATE it in a body
    # (`test_season_shape.py::test_jordan_no_definition_is_hardcoded_in_a_body`)
    assert "suppress_einhir_revival" in axes and "revive_einhir" in axes
    for pole in ("reveal_thread_truth", "uphold_church", "uphold_caste", "altonian_ascendancy"):
        assert pole in axes, f"{pole!r}, an opposite pole that is not among the ten, is a member too"
    opposes = roster_map("thrust_axes", "opposes")
    checked = 0
    for axis, pole in opposes.items():
        assert axis in axes and pole in axes, (axis, pole)
        checked += 1
    assert checked >= 6, checked
    assert opposes["suppress_einhir_revival"] == "revive_einhir"
    assert opposes["revive_einhir"] == "suppress_einhir_revival"


def test_every_rostered_axis_is_accepted_on_a_row_that_mints_a_proposition():
    checked = 0
    for axis in sorted(roster("thrust_axes")):
        got = goals.parse(_set_goal("g_deeds", "axis", axis))
        assert next(g for g in got if g.id == "g_deeds").axis == axis
        checked += 1
    assert checked == len(roster("thrust_axes")) >= 10, checked


def test_a_pole_the_opposes_map_pairs_that_is_no_member_is_refused_at_parse(monkeypatch):
    """The map is the roster's second half; a pole outside `values:` is an axis no row could carry."""
    planted = dict(roster_map("thrust_axes", "opposes"), purge_altonia="a_pole_nobody_listed")
    monkeypatch.setitem(rosters._ROSTERS["thrust_axes"], "opposes", planted)
    with pytest.raises(Unspecified) as red:
        goals.parse(_base())
    assert "a_pole_nobody_listed" in red.value.what and "thrust_axes" in red.value.where
    assert type(red.value) is Unspecified
    # the control: unplanted, the same document loads
    monkeypatch.undo()
    assert goals.parse(_base())


# (name, doc, refusal type, a fragment of `.what`, a fragment of `.where` naming the row)
_AXIS_PLANTS = [
    ("an axis off the roster", _set_goal("g_throne", "axis", "world_peace"), Unspecified, "world_peace",
     "g_throne"),
    ("an axis that is a list", _set_goal("g_throne", "axis", ["political_authority"]), Unspecified,
     "political_authority", "g_throne"),
    ("an axis that is null", _set_goal("g_throne", "axis", None), Unspecified, "None", "g_throne"),
    # THE PLANTED-FAILURE TARGET of B2.1: a member of the roster, on a row that mints nothing
    ("an axis on an orientation row", _set_goal("g_orient", "axis", "faction_standing"), Forbidden,
     "orientation", "g_orient"),
    ("a pole that is no member on an orientation row", _set_goal("g_orient", "axis", "uphold_caste"),
     Forbidden, "orientation", "g_orient"),
]


@pytest.mark.parametrize("name,doc,cls,fragment,named", _AXIS_PLANTS, ids=[p[0] for p in _AXIS_PLANTS])
def test_each_planted_axis_violation_is_refused_by_name(name, doc, cls, fragment, named):
    assert goals.parse(_base()), "the control: the base itself loads"
    with pytest.raises(cls) as red:
        goals.parse(doc)
    assert type(red.value) is cls, (name, type(red.value))
    assert fragment in red.value.what, (name, red.value.what)
    assert named in red.value.where, (name, red.value.where)


# ------------------------------------------------------------------------------ B2.2: the goal_stages rows

def _world_only_cells() -> dict:
    """Cells the typed-requires builder ACCEPTS and whose every stem only the world answers."""
    return {
        "with": {"form": "relation", "of": "subject", "relation": "with"},
        "audience": {"form": "relation", "of": "subject", "relation": "audience"},
        "own-state": {"form": "scalar_threshold", "of": "subject", "scalar": "thread_sensitivity",
                      "threshold_predicate": "thread_sensitivity.gate", "comparator": ">="},
        "mixed with a person-side stem": {"all": [_HELD, {"form": "relation", "of": "subject",
                                                            "relation": "with"}]},
    }


def _ledger_derived_cells() -> dict:
    """Cells the typed-requires builder ACCEPTS and that ask a `LEDGER_DERIVED_STEMS` stem (`claim.held`):
    no claim answers it person-side, so a stage over one could never be met (found at the B10-05 close)."""
    return {
        "own_ledger": {"form": "own_ledger", "of": "subject"},
        "mixed with a readable stem": {"all": [_HELD, {"form": "own_ledger", "of": "subject"}]},
    }


_BUILDER_REFUSED = {
    "a form off requires_forms": {"form": "eighth_form", "of": "subject"},
    "an operand outside requires_operands (there is no `referent`)": {"form": "own_ledger", "of": "referent"},
    "an operand outside the form's needs": {"form": "own_ledger", "of": "actor"},
    "a stem no reader dispatches on": {"form": "relation", "of": "subject", "relation": "no_such_stem"},
    "a cell that is no mapping": "yes",
    "an `all` of one clause": {"all": [_HELD]},
}

_PLANTS = [
    # --- the row itself
    ("goal_stages is a mapping", _mut(lambda d: d.__setitem__("goal_stages", {"gs": 1})), Unspecified,
     "not a list", "goal_stages"),
    ("goal_stages is null", _mut(lambda d: d.__setitem__("goal_stages", None)), Unspecified, "not a list",
     "goal_stages"),
    ("a row that is no mapping", _mut(lambda d: d["goal_stages"].append("gs_x")), Unspecified, "`id:`",
     "goal_stages"),
    ("a row with no id", _mut(lambda d: d["goal_stages"].append({"for": ["g_throne"], "stages": []})),
     Unspecified, "`id:`", "goal_stages"),
    ("a repeated row id", _mut(lambda d: d["goal_stages"].append(copy.deepcopy(_row(d, "gs_pair")))),
     Forbidden, "more than one row", "gs_pair"),
    # --- `for:`
    ("for: empty", _set_row("gs_throne", "for", []), Unspecified, "non-empty", "gs_throne"),
    ("for: absent", _drop_row("gs_throne", "for"), Unspecified, "non-empty", "gs_throne"),
    ("for: a bare string", _set_row("gs_throne", "for", "g_throne"), Unspecified, "non-empty", "gs_throne"),
    ("for: a non-goal", _set_row("gs_throne", "for", ["g_ghost"]), Unspecified, "g_ghost", "gs_throne"),
    ("for: a non-hashable id", _set_row("gs_throne", "for", [["g_throne"]]), Unspecified, "no goal",
     "gs_throne"),
    # THE PLANTED-FAILURE TARGET of B2.2: a goal that mints no Proposition
    ("for: an orientation goal", _set_row("gs_throne", "for", ["g_throne", "g_orient"]), Forbidden,
     "orientation", "gs_throne"),
    # the SECOND row in file order (`gs_pair`) is the one refused, and its message names the first claimer
    ("for: a goal a second row claims", _set_row("gs_throne", "for", ["g_throne", "g_deeds"]), Forbidden,
     "which row 'gs_throne' already claims", "gs_pair"),
    ("for: the same goal twice in one row", _set_row("gs_throne", "for", ["g_throne", "g_throne"]),
     Forbidden, "already claims", "gs_throne"),
    # --- `stages:`
    ("stages: absent", _drop_row("gs_throne", "stages"), Unspecified, "at least two", "gs_throne"),
    ("stages: one stage", _set_row("gs_throne", "stages", [_stage("s1", "short", _HELD)]), Unspecified,
     "at least two", "gs_throne"),
    ("stages: none", _set_row("gs_throne", "stages", []), Unspecified, "at least two", "gs_throne"),
    ("stages: a mapping", _set_row("gs_throne", "stages", {"s1": 1, "s2": 2}), Unspecified, "at least two",
     "gs_throne"),
    ("a stage that is no mapping", _mut(lambda d: _row(d, "gs_throne")["stages"].__setitem__(0, "s1")),
     Unspecified, "`id:`", "gs_throne"),
    ("a stage with no id", _mut(lambda d: _stg(d, "gs_throne", "s1").pop("id")), Unspecified, "`id:`",
     "gs_throne"),
    ("a repeated stage id", _mut(lambda d: _stg(d, "gs_throne", "s2").__setitem__("id", "s1")), Forbidden,
     "more than one stage", "gs_throne/s1"),
    # --- `term`
    ("a term off the roster", _set_stage("gs_throne", "s1", "term", "soon"), Unspecified, "soon",
     "gs_throne/s1"),
    ("a term that is a number", _set_stage("gs_throne", "s1", "term", 1), Unspecified, "term 1",
     "gs_throne/s1"),
    ("no term", _drop_stage("gs_throne", "s1", "term"), Unspecified, "term None", "gs_throne/s1"),
    ("terms that decrease", _set_stage("gs_pair", "s3", "term", "short"), Forbidden, "nearer",
     "gs_pair/s3"),
    ("terms that decrease from the far end", _set_terms("gs_throne", "long", "medium"), Forbidden, "nearer",
     "gs_throne/s2"),
    # --- `pursuits`
    ("no pursuits", _drop_stage("gs_throne", "s1", "pursuits"), Unspecified, "pursuits", "gs_throne/s1"),
    ("empty pursuits", _set_stage("gs_throne", "s1", "pursuits", {}), Unspecified, "pursuits",
     "gs_throne/s1"),
    ("an unknown pursuit", _set_stage("gs_throne", "s1", "pursuits", {"bloodlust": 1}), Unspecified,
     "bloodlust", "gs_throne/s1"),
    ("a pursuit weighing nothing", _set_stage("gs_throne", "s1", "pursuits", {"honour": 0}), Unspecified,
     "weighs", "gs_throne/s1"),
    ("a pursuit weight that is a bool", _set_stage("gs_throne", "s1", "pursuits", {"honour": True}),
     Unspecified, "weighs", "gs_throne/s1"),
    ("a pursuit weight that is inf", _set_stage("gs_throne", "s1", "pursuits", {"honour": float("inf")}),
     Unspecified, "weighs", "gs_throne/s1"),
    # --- `predicate`: absent, `none`
    ("no predicate", _drop_stage("gs_throne", "s1", "predicate"), Unspecified, "no requirement",
     "gs_throne/s1"),
    ("predicate: none", _set_stage("gs_throne", "s1", "predicate", "none"), Unspecified, "no requirement",
     "gs_throne/s1"),
    # --- the struck keys (M20) and any other key the schema does not read
    ("a stage `deadline`", _set_stage("gs_throne", "s1", "deadline", 3), Forbidden, "deadline",
     "gs_throne/s1"),
    ("a stage with a stray key", _set_stage("gs_throne", "s1", "note", "x"), Forbidden, "note",
     "gs_throne/s1"),
    ("a row `closing`", _set_row("gs_throne", "closing", {"form": "none"}), Forbidden, "closing",
     "gs_throne"),
    ("a row `successor`", _set_row("gs_throne", "successor", {"on_met": None}), Forbidden, "successor",
     "gs_throne"),
    ("a row `deal`", _set_row("gs_throne", "deal", {"weight": 1}), Forbidden, "deal", "gs_throne"),
]
_PLANTS += [(f"predicate: {name}", _set_stage("gs_throne", "s1", "predicate", cell), Unspecified,
             "typed-requires builder", "gs_throne/s1") for name, cell in _BUILDER_REFUSED.items()]
_PLANTS += [(f"predicate asks a world-only stem: {name}", _set_stage("gs_throne", "s1", "predicate", cell),
             Forbidden, "only the world answers", "gs_throne/s1") for name, cell in _world_only_cells().items()]
_PLANTS += [(f"predicate asks a ledger-derived stem: {name}", _set_stage("gs_throne", "s1", "predicate", cell),
             Forbidden, "no ledger claim answers", "gs_throne/s1") for name, cell in _ledger_derived_cells().items()]
_PLANTS += [("a top-level key beside goals and goal_stages (`ladders:`)",
             _mut(lambda d: d.__setitem__("ladders", copy.deepcopy(d["goal_stages"]))), Forbidden,
             "top-level key", "goals.yaml")]


def test_the_plants_ran_a_floor_of_refusals_and_each_is_unique():
    """The loop asserts that it asserted (`CLAUDE.md` §0.1 pt 2): every plant of both lists is refused with
    its own type, so a list that silently emptied (or a `pytest.raises` that never ran) cannot pass."""
    assert len(_PLANTS) >= 51 and len(_AXIS_PLANTS) >= 5, (len(_PLANTS), len(_AXIS_PLANTS))
    assert len({p[0] for p in _PLANTS}) == len(_PLANTS)
    assert len({p[0] for p in _AXIS_PLANTS}) == len(_AXIS_PLANTS)
    checked = 0
    for name, doc, cls, fragment, named in _AXIS_PLANTS + _PLANTS:
        with pytest.raises(cls) as red:
            goals.parse(doc)
        assert type(red.value) is cls and fragment in red.value.what and named in red.value.where, name
        checked += 1
    assert checked == len(_AXIS_PLANTS) + len(_PLANTS) >= 56, checked


@pytest.mark.parametrize("name,doc,cls,fragment,named", _PLANTS, ids=[p[0] for p in _PLANTS])
def test_each_planted_goal_stages_violation_is_refused_by_name(name, doc, cls, fragment, named):
    # the plant is ONE mutation of the base: the base itself loads (the control), so the refusal below
    # can only be the mutation's.
    assert goals.parse(_base())
    with pytest.raises(cls) as red:
        goals.parse(doc)
    assert type(red.value) is cls, (name, type(red.value))
    assert fragment in red.value.what, (name, red.value.what)
    assert named in red.value.where, (name, red.value.where)


def test_the_builders_systemexit_is_wrapped_into_the_loaders_own_refusal():
    """The builder raises `SystemExit` (it was written for `verb_table.yaml`'s import); the loader must hand
    a stage author a `ShapeGap` naming the stage, not kill the process. Asserted both ways, per cell."""
    checked = 0
    for name, cell in _BUILDER_REFUSED.items():
        with pytest.raises(SystemExit):
            build_typed_requires("probe", cell)
        with pytest.raises(Unspecified) as red:
            goals.parse(_set_stage("gs_throne", "s1", "predicate", cell))
        assert not isinstance(red.value, SystemExit) and "gs_throne/s1" in red.value.where, name
        checked += 1
    assert checked == len(_BUILDER_REFUSED) >= 6, checked


def test_the_world_only_plants_are_cells_the_builder_accepts_so_only_the_stem_refuses_them():
    """ISOLATION: a world-only plant that the builder also refused would pass the plants above for the
    wrong reason. Each builds, and its every stem is a `WORLD_ONLY_STEMS` member."""
    checked = 0
    for name, cell in _world_only_cells().items():
        req = build_typed_requires("probe", cell)
        assert req is not None, name
        stems = set(req.stems())
        if name == "mixed with a person-side stem":
            assert stems & WORLD_ONLY_STEMS and stems - WORLD_ONLY_STEMS, (name, stems)
        else:
            assert stems and stems <= WORLD_ONLY_STEMS, (name, stems)
        checked += 1
    assert checked == len(_world_only_cells()) >= 4, checked


def test_equal_terms_are_lawful_and_only_a_decrease_is_refused():
    """`gs_pair` repeats `medium`. The control that the decrease plants are not refusing equality."""
    got = next(g for g in goals.parse(_base()) if g.id == "g_rung")
    assert [s.term for s in got.stages.stages].count("medium") == 2


def test_the_struck_keys_are_not_built():
    """M20 struck the stage `deadline` and the row keys `closing`, `successor` and `deal`: no carrier field."""
    stage_fields = {f.name for f in dataclasses.fields(goals.Stage)}
    row_fields = {f.name for f in dataclasses.fields(goals.GoalStages)}
    checked = 0
    for struck, fields in (("deadline", stage_fields), ("closing", row_fields), ("successor", row_fields),
                           ("deal", row_fields)):
        assert struck not in fields, struck
        checked += 1
    assert checked == 4


# ------------------------------------------------------------------------------ through the file reader

def test_a_bad_stage_in_the_file_refuses_the_whole_file_and_caches_nothing(monkeypatch, tmp_path):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump(_set_stage("gs_throne", "s1", "term", "soon"), allow_unicode=True),
                    encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    with pytest.raises(Unspecified, match="gs_throne/s1"):
        goals.goals()
    assert goals._CACHE is None, "a refused file is not cached as if it had loaded (goals included)"


def test_a_good_file_with_stages_loads_through_the_reader_and_replaced_rows_carry_their_own(monkeypatch,
                                                                                         tmp_path):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump(_base(), allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    assert goals.goal("g_throne").stages.id == "gs_throne" and goals.goal("g_throne").axis == "political_authority"
    # the one cache: swapping the goals swaps the stage rows with them (`decision_spread.no_goals`)
    with goals.rows_replaced():
        assert goals.goals() == () and goals.goal("g_throne") is None
    assert goals.goal("g_throne").stages.id == "gs_throne"
