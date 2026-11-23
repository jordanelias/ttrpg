"""v10 CR-20: the attribute carrier (`Person.attributes`), executed. Rewritten at B05.99 to the rule B05.09, B05.11, B05.14,
B05.16 and B05.25 landed (the pool is `pool_of(governing score + rank, ...)`; the opposition is the opponent's skill score plus
his opposing attribute; the skill row's `base:` and `opposed_by:` columns, `VOCATION_ATTRIBUTE` and `task_difficulty` are gone).

WHAT THIS PINS, and the falsifier of each:

  * POOLS AND OPPOSITION -- two persons holding 2 and 6 on `tell`'s two `governing:` attributes have governing scores 2.0 and
    6.0 and roll `pool_of(governing score + rank, addends, pool_add, pool_floor)` (`sigma.faculty`); opposite a roller they
    oppose with their skill score (`_opposition_of`, the untrained 2 here) plus their opposing attribute (`_opposing`: Will 2
    and 6; an unheld Will reads the scale's mid-point 4.0), which the module reads at `opposed_ob(.., opposition_rate)`.
    FALSIFIER: the attribute read planted away below, and the 6 rolls the untrained score's pool.
  * THE HELD KEY -- the rank ADDS to the governing score (never the larger of the two); the opposition's skill score is the held
    rank, never below the untrained score.
  * THE RETIRED COLUMNS ARE REFUSED -- a skill row carrying `base:` or `opposed_by:` (even naming one of the ten) is outside the
    exporter's row grammar; a verb naming a skill with no definition row is refused by the verb loader; a skill no verb names
    is reported (`verbs.skills_without_a_verb`), not refused.
  * THE CAST -- a legacy spelling resolves to its key; a key that is none of the ten, a value outside 1-7, a
    float and a double spelling refuse; no row and `stats: null` are `{}`.
  * NO PLAY-TIME WRITE -- no `write_matrix.yaml` row, so the gate refuses (`test_k3_thread_sensitivity.py` (e)).
"""
import functools
import importlib
import operator

import pytest

from engine.dice_engine.sigma_leverage import opposed_ob, pool_of
from engine.season.decision.sheet import creation_sheet
from engine.season.data import cast, files
from engine.season.data.matrix import matrix_row
from engine.season.data.verbs import VERB_CAPABILITY, VERB_TABLE, VOCATIONS, skills_without_a_verb
from engine.season.gaps import Forbidden, Unspecified
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.seam.wrappers import pool, sigma
from engine.season.state.gate import WriteClass
from engine.season.state.world import Step
from engine.substrate import composition, descriptors



def _roll_module():
    """The obstacle's owner, reached as the engine reaches it -- by the composition row's string, and LAZILY:
    `test_engine_does_not_import_systems.py` imports every engine file, this one included, and a module-level
    load would put `modules/` in its subprocess."""
    return importlib.import_module(composition.require("social_contest.roll").__module__)

TELL = "tell"                                   # draws on `copying`; governed by two attributes, resisted by Will
GOV = VERB_TABLE[TELL].governing                # (acuity, attunement)
WILL = VERB_TABLE[TELL].opposed_attribute
ATTR = GOV[0]
LOW, MID, HIGH = "p_low", "p_mid", "p_high"


def _w(**attrs):
    w = P.tiny_world()
    for pid, a in attrs.items():
        w.persons[pid].attributes = dict(a)
    return w


def _held(n):
    """A person holding `n` on both of `tell`'s governing attributes and on Will."""
    return {GOV[0]: n, GOV[1]: n, WILL: n}


def _pool(w, g, rank=0):
    """The pool rule at the world's fixtures, for a governing score `g` and a rank (no addend in a tiny world)."""
    return pool_of(g + rank, 0, w.fixtures.get("pool_add"), w.fixtures.get("pool_floor"))


# ======================================================================================
# THE FALSIFIER: governing scores 2 and 6, opposed at what the obstacle reads
# ======================================================================================

def test_pools_follow_the_governing_attributes_and_the_opposition_reads_the_opposing_attribute():
    assert len(GOV) == 2 and WILL == "attr.spirit.will"
    w = _w(**{LOW: _held(2), HIGH: _held(6)})
    assert [pool.governing_score(w, w.persons[p], TELL) for p in (LOW, MID, HIGH)] == [2.0, 2.0, 6.0]   # MID: the untrained 2
    assert w.fixtures.get("pool_add") == 6 and w.fixtures.get("pool_floor") == 5        # the shipped base and floor
    assert sigma.faculty(w, w.persons[LOW], TELL) == _pool(w, 2.0) == 8.0
    assert sigma.faculty(w, w.persons[HIGH], TELL) == _pool(w, 6.0) == 12.0
    assert sigma.faculty(w, w.persons[MID], TELL) == 8.0                                # nothing authored: the untrained score
    # the skill score alone is the same untrained 2 for all three (B05.11); the attribute is what parts them (A-137, B05.16)
    assert [sigma._opposition_of(w, p, TELL) for p in (LOW, MID, HIGH)] == [2.0, 2.0, 2.0]
    assert [sigma._opposing(w, p, TELL) for p in (LOW, MID, HIGH)] == [4.0, 6.0, 8.0]   # MID: the mid-point 4.0

    # What the module composes against a roller with nothing authored: even + difficulty + opposed_ob(opposition, rate).
    roller, SC_ROLL = MID, _roll_module()
    rate = w.fixtures.get("opposition_rate")
    obs = {}
    for subject, opposition in ((LOW, 4.0), (HIGH, 8.0)):
        inp = sigma.contest_input(w, [roller], verb=TELL, subject=subject)
        assert inp.opposition == opposition and inp.pool == 8.0
        ob, terms = SC_ROLL.obstacle(inp)
        named = dict(terms)
        assert named["opposition"] == opposed_ob(opposition, rate)
        assert named["difficulty"] == w.fixtures.get("difficulty_ob")[VERB_TABLE[TELL].difficulty]
        assert "ceiling" not in named, "the per-pool cap at pool 8 is above both obstacles"
        assert ob == functools.reduce(operator.add, (v for _, v in terms), 0.0)       # the terms fold to the obstacle
        obs[subject] = ob
    assert obs[HIGH] > obs[LOW]
    assert dict(SC_ROLL.obstacle(sigma.contest_input(w, [roller], verb=TELL, subject=HIGH))[1])["opposition"] \
        - dict(SC_ROLL.obstacle(sigma.contest_input(w, [roller], verb=TELL, subject=LOW))[1])["opposition"] \
        == opposed_ob(8.0, rate) - opposed_ob(4.0, rate)                               # Will 6 against Will 2, at the rate


def test_the_planted_failure_the_attribute_read_removed_rolls_the_untrained_pool(monkeypatch):
    """The assertion above can observe the failure it excludes: with the attribute read removed the 6 rolls the untrained 2's pool."""
    w = _w(**{HIGH: _held(6)})
    assert sigma.faculty(w, w.persons[HIGH], TELL) == 12.0
    monkeypatch.setattr(pool, "_held_attribute", lambda entity, attr: None)
    assert sigma.faculty(w, w.persons[HIGH], TELL) == _pool(w, 2.0) == 8.0 != 12.0


def test_a_verb_naming_no_skill_still_rolls_its_governing_attributes():
    """B05.25 replaced "a verb with no vocation ignores the attributes": every rolled verb names its governing attributes, so a
    verb naming no skill (`lie`, three attributes) rolls their mean at rank 0, and its opposition is the untrained score plus
    the opposing attribute. A brute verb (`transfer`) never rolls: it has no pool to ignore anything with."""
    lie = VERB_TABLE["lie"]
    assert VERB_CAPABILITY.get("lie") is None and len(lie.governing) == 3
    w = _w(**{HIGH: {a: 6 for a in lie.governing}})
    assert sigma.faculty(w, w.persons[HIGH], "lie") == _pool(w, 6.0) == 12.0
    assert sigma.faculty(w, w.persons[MID], "lie") == _pool(w, 2.0) == 8.0
    assert sigma._opposition_of(w, HIGH, "lie") == float(w.fixtures.get("pool_default"))   # no skill: the untrained score
    assert lie.opposed_attribute in lie.governing
    assert sigma._opposing(w, HIGH, "lie") == 2.0 + 6.0                                  # plus his opposing attribute, held at 6
    assert VERB_TABLE["transfer"].brute
    with pytest.raises(Forbidden):
        sigma.faculty(w, w.persons[HIGH], "transfer")


# ======================================================================================
# THE HELD KEY: practice adds to the governing score; the opposition's score is the held rank
# ======================================================================================

def test_the_rank_adds_to_the_governing_score_and_is_not_the_larger_of_the_two():
    key = VERB_CAPABILITY[TELL]
    w = _w(**{LOW: _held(3), MID: _held(2), HIGH: _held(6)})
    w.persons[LOW].capability = {key: 5}                  # practice above the attribute
    w.persons[MID].capability = {key: 1}                  # a held key below the attribute
    w.persons[HIGH].capability = {key: 4}
    assert sigma.faculty(w, w.persons[LOW], TELL) == _pool(w, 3.0, 5) == 14.0     # was the larger of the two, 5
    assert sigma.faculty(w, w.persons[MID], TELL) == _pool(w, 2.0, 1) == 9.0      # was 2
    assert sigma.faculty(w, w.persons[HIGH], TELL) == _pool(w, 6.0, 4) == 16.0    # was 6
    # the skill score is the held rank, never below the untrained 2; the attribute joins it in `_opposing`, not in the score
    assert [sigma._opposition_of(w, p, TELL) for p in (LOW, MID, HIGH)] == [5.0, 2.0, 4.0]
    assert [sigma._opposing(w, p, TELL) for p in (LOW, MID, HIGH)] == [8.0, 4.0, 10.0]


def test_a_held_key_alone_adds_to_the_untrained_governing_score():
    key = VERB_CAPABILITY[TELL]
    w = _w()
    w.persons[LOW].capability = {key: 4}
    assert sigma.faculty(w, w.persons[LOW], TELL) == _pool(w, 2.0, 4) == 12.0 and sigma._opposition_of(w, LOW, TELL) == 4.0
    # a held 0 is the untrained man's pool (B05.09: a held rank is never a loss), no longer a person under one die
    w.persons[MID].capability = {key: 0}
    assert sigma.faculty(w, w.persons[MID], TELL) == sigma.faculty(w, w.persons[HIGH], TELL) == 8.0


# ======================================================================================
# THE RETIRED COLUMNS ARE REFUSED; THE VERB TABLE IS CLOSED
# ======================================================================================

def test_the_retired_columns_are_refused_by_the_exporter_and_a_skill_with_no_row_by_the_verb_loader(monkeypatch):
    """B05.25 step 7 deleted a skill row's `base:` and `opposed_by:`: a row carrying either, even naming one of the ten, is outside
    the exporter's row grammar. A verb naming a skill with no definition row is the verb loader's refusal. (The retired
    "row for a non-vocation" refusal is gone: a skill no verb names is REPORTED, below.)"""
    import copy, os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
    import export_descriptors as ed
    real = ed.ci_common.load_yaml
    checked = 0
    for column in ("base", "opposed_by"):
        def planted(path, default=None, _column=column):
            reg = copy.deepcopy(real(path, default=default))
            reg["capabilities"]["rows"][sorted(reg["capabilities"]["rows"])[0]][_column] = ATTR    # one of the ten
            return reg
        monkeypatch.setattr(ed.ci_common, "load_yaml", planted)
        with pytest.raises(SystemExit, match=column):
            ed.build()
        checked += 1
    assert checked == 2
    monkeypatch.setattr(ed.ci_common, "load_yaml", real)
    assert ed.build()["capabilities"]["rows"]                       # the control: the shipped block exports
    from engine.season.tests.test_u1_capability_surface import _planted_verb_load, _row
    msg = _planted_verb_load(lambda doc: _row(doc, "argue").update(capability="no_such_skill"))
    assert msg is not None and "no_such_skill" in msg, msg


def test_a_skill_no_verb_names_is_reported_not_refused():
    assert skills_without_a_verb() == sorted(set(descriptors.CAPABILITIES) - set(VOCATIONS))


# ======================================================================================
# THE CAST'S `stats:`
# ======================================================================================

def test_a_legacy_spelling_resolves_to_its_key_and_a_range_reads_its_lower_bound():
    got = cast.attributes_of({"id": "X", "stats": {"cognition": 5, "focus": 5, "endurance": 4, "presence": "3–4"}})
    assert got == {"attr.mind.acuity": 5, "attr.mind.focus": 5, "attr.body.endurance": 4,
                   "attr.social.charisma": 3}
    # `social` is the category (`agg.social`), not an attribute: it refuses rather than guessing one of three
    with pytest.raises(Exception):
        cast.attributes_of({"id": "X", "stats": {"social": "3–4"}})
    assert cast.attributes_of({"id": "X", "stats": {"Reason": 2, "Spirit": 7, "attr.social.grace": 1}}) == {
        "attr.mind.acuity": 2, "attr.spirit.will": 7, "attr.social.grace": 1}


@pytest.mark.parametrize("stats", [
    {"luck": 3}, {"bonds": 3}, {"Bonds": 3},                       # none of the ten (Bonds is retired)
    {"focus": 0}, {"focus": 8}, {"focus": -1},                     # outside 1-7
    {"focus": 2.5}, {"focus": True}, {"focus": "3"}, {"focus": [3]}, {"focus": None},
    {"cognition": 3, "reason": 4},                                 # two spellings of one key
    [3], "five",
])
def test_an_unrostered_key_or_an_out_of_scale_value_refuses(stats):
    with pytest.raises(Unspecified):
        cast.attributes_of({"id": "X", "stats": stats})


def test_no_row_and_no_stats_are_absent_and_the_shipped_cast_parses():
    assert cast.attributes_of({}) == {} and cast.attributes_of({"id": "X"}) == {}
    assert cast.attributes_of({"id": "X", "stats": None}) == {}
    every = {cid: cast.attributes_of(r) for cid, r in cast.load().items()}
    assert len(every) == 46 and sum(bool(v) for v in every.values()) >= 1, "the registry read no value at all"
    assert every["NPC-001"] == {"attr.mind.acuity": 5, "attr.mind.focus": 5, "attr.body.endurance": 4,
                                "attr.social.attunement": 3, "attr.social.charisma": 3, "attr.social.grace": 3}
    assert all(set(v) <= set(descriptors.ATTRIBUTES) for v in every.values())


# ======================================================================================
# THE CARRIER IS WRITTEN AT BUILD ONLY
# ======================================================================================

def test_the_carrier_has_no_matrix_row_and_the_gate_refuses_a_write():
    with pytest.raises(Unspecified):
        matrix_row("Person", "attributes")
    w = _w(**{LOW: {ATTR: 2}})
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("attributes", mint_token(w, WriteClass.ACTS),
                lambda: setattr(w.persons[LOW], "attributes", {ATTR: 7}),
                record_kind="Person", fieldname="attributes", driver="Act")
    assert w.persons[LOW].attributes == {ATTR: 2}, "the refused write landed"


def test_the_creation_sheet_carries_the_attributes_as_a_read_only_copy():
    w = _w(**{HIGH: {ATTR: 6}})
    rows = {r.id: r for r in creation_sheet(w.persons.values())}
    assert dict(rows[HIGH].attributes) == {ATTR: 6} and dict(rows[LOW].attributes) == {}
    with pytest.raises(TypeError):
        rows[HIGH].attributes[ATTR] = 1
    assert w.persons[HIGH].attributes == {ATTR: 6}


# ======================================================================================
# THE REALM: the control arm ships, and the authored row is a measured mover when read
# ======================================================================================

def test_the_realm_reads_the_cast_stats_only_on_the_arm_that_is_switched_on():
    """`cast_attributes=False` (the control) leaves every person with no attribute; `True` (SHIPPED since B11 lane A)
    seats the sheet `state/carriers.py::generated_attributes` draws (B01a.01) on every person and the one row the
    registry authors (NPC-001, Edeyja) over it, key by key. The event-list and hash readings of the two arms are in
    `build_realm`'s docstring and the CR-20 and B11 lane A commit bodies."""
    from engine.season.boot.realm import build_realm
    from engine.season.state.carriers import generated_attributes
    off = build_realm(0, cast_attributes=False)
    assert not [p.id for p in off.persons.values() if p.attributes]
    on = build_realm(0)
    span = on.fixtures.get("generated_attribute_range")
    # BA1.99 re-point (BA1.01 authors `stats:` on 42 rows, not the one): every person's sheet is the drawn one with the row's authored
    # keys over it, key by key, and a person with no row or a row with no `stats:` holds the drawn sheet alone.
    checked, authored = 0, 0
    for pid, p in on.persons.items():
        drawn = generated_attributes(0, pid, span)
        row = cast.row(f"NPC-{pid[len('p_npc_'):]}") if pid.startswith("p_npc_") else None
        stated = cast.attributes_of(row) if row else {}
        assert p.attributes == {**drawn, **stated}, pid
        authored += bool(stated)
        checked += 1
    assert checked == len(on.persons) and checked > 1
    assert authored == 43, authored           # NPC-001 (before the batch) and the 42 BA1.01 states (NPC-001 not among them)


# ======================================================================================
# THE SETTER SCAN (04 PART D row 3, step 3: "a planted direct assignment is caught by the setter scan"): the gate
# refuses a gated write that NAMES the field, and nothing refuses a bare `p.attributes = ...`, so the build is the one
# place that may assign them. `test_k3_thread_sensitivity.py::test_k3_e_...` is the precedent (one field); CR-20 and
# CR-30 add two read-off fields to it. Added at the B10-10 close (layer-conformance, B3).
# ======================================================================================

def test_no_engine_source_outside_the_world_build_assigns_attributes_or_heritage():
    import ast
    import pathlib
    root = pathlib.Path(__file__).resolve().parents[1]
    build = files.REALM_PY
    fields = {"attributes", "heritage", "traits"}   # traits: B04.07, written at build only (04 §A.2 state/<carrier>)
    sites, scanned = [], 0
    for path in sorted(root.rglob("*.py")):
        if "tests" in path.relative_to(root).parts:
            continue
        scanned += 1
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            targets = (node.targets if isinstance(node, ast.Assign)
                       else [node.target] if isinstance(node, (ast.AugAssign, ast.AnnAssign)) else [])
            for t in targets:
                base = t.value if isinstance(t, ast.Subscript) else t          # `p.attributes[k] = v` too
                if isinstance(base, ast.Attribute) and base.attr in fields:
                    sites.append((path, node.lineno, base.attr))
            if (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "setattr"
                    and len(node.args) >= 2 and isinstance(node.args[1], ast.Constant)
                    and node.args[1].value in fields):
                sites.append((path, node.lineno, node.args[1].value))
    assert scanned > 50, f"scanned {scanned} files -- the walk did not reach the engine"
    outside = [s for s in sites if s[0] != build]
    assert not outside, f"assigned outside the world build: {outside}"
    assert {f for _, _, f in sites} == fields, f"the build no longer assigns both: {sites}"
