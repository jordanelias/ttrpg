"""v10 CR-20: the attribute carrier (`Person.attributes`), executed.

WHAT THIS PINS, and the falsifier of each:

  * POOLS AND OPPOSITION -- two persons holding 2 and 6 on a vocation's attribute and no held key roll
    pools 2 and 6 (`sigma.faculty`) and are opposed at 2.0 / 6.0 raw, which the obstacle halves to Ob 1 and 3
    and the CEILING then bounds (`modules/social_contest/roll.py::obstacle`, H-213: at the actor's pool of 2
    the per-pool cap is ~2.84, so the 6 reads below 3 -- asserted at what the module reads, not at 3).
    FALSIFIER: `faculty` ignoring the base is planted below and reads 2, not 6.
  * THE HELD KEY -- the pool is the larger of the base and the key a person holds (practice); the opposition
    the larger of the key and the attribute, never the fallback.
  * THE ROSTER IS CLOSED -- `vocation_attribute` refuses a vocation with no row, a row for a non-vocation and a
    value that is none of the ten.
  * THE CAST -- a legacy spelling resolves to its key; a key that is none of the ten, a value outside 1-7, a
    float and a double spelling refuse; no row and `stats: null` are `{}`.
  * NO PLAY-TIME WRITE -- no `write_matrix.yaml` row, so the gate refuses (`test_k3_thread_sensitivity.py` (e)).
"""
import importlib

import pytest

from engine.season.decision.sheet import creation_sheet
from engine.season.data import cast
from engine.season.data.matrix import matrix_row
from engine.season.data.rosters import (
    VERB_CAPABILITY, VOCATION_ATTRIBUTE, _load_vocation_attribute,
)
from engine.season.data.verbs import VOCATIONS
from engine.season.gaps import Unspecified
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.seam.wrappers import sigma
from engine.season.state.gate import WriteClass
from engine.season.state.world import Step
from engine.substrate import composition, descriptors



def _roll_module():
    """The obstacle's owner, reached as the engine reaches it -- by the composition row's string, and LAZILY:
    `test_engine_does_not_import_systems.py` imports every engine file, this one included, and a module-level
    load would put `modules/` in its subprocess."""
    return importlib.import_module(composition.require("social_contest.roll").__module__)

TELL = "tell"                                   # draws on `copying`
ATTR = VOCATION_ATTRIBUTE[VERB_CAPABILITY[TELL]]
LOW, MID, HIGH = "p_low", "p_mid", "p_high"


def _w(**attrs):
    w = P.tiny_world()
    for pid, a in attrs.items():
        w.persons[pid].attributes = dict(a)
    return w


# ======================================================================================
# THE FALSIFIER: pools 2 and 6, opposed at what the obstacle reads
# ======================================================================================

def test_pools_follow_the_vocation_attribute_and_the_opposition_reads_the_score():
    w = _w(**{LOW: {ATTR: 2}, HIGH: {ATTR: 6}})
    assert sigma.faculty(w, w.persons[LOW], TELL) == 2
    assert sigma.faculty(w, w.persons[HIGH], TELL) == 6
    assert sigma.faculty(w, w.persons[MID], TELL) == w.fixtures.get("pool_default")      # nothing authored
    assert sigma._opposition_of(w, LOW, TELL) == 2.0 and sigma._opposition_of(w, HIGH, TELL) == 6.0
    assert sigma._opposition_of(w, MID, TELL) is None                                    # never the fallback

    # What the module composes against a roller of pool 2 (the default): score/2, then the H-213 ceiling.
    roller, SC_ROLL = MID, _roll_module()
    low_ob = SC_ROLL.obstacle(sigma.contest_input(w, [roller], verb=TELL, subject=LOW))
    high_inp = sigma.contest_input(w, [roller], verb=TELL, subject=HIGH)
    high_ob = SC_ROLL.obstacle(high_inp)
    assert high_inp.opposition == 6.0 and high_inp.pool == w.fixtures.get("pool_default")
    assert low_ob == 1.0                                                  # 2 / 2: under any ceiling
    cap = SC_ROLL._chance_floor_cap(high_inp.pool, float(high_inp.obstacle_ceiling))
    assert 1.0 < cap < 3.0, "the plan's premise (Ob 3 reads) is false at this ceiling: the cap bites"
    assert high_ob == cap, "the ceiling is the obstacle a 6 reads against a pool of 2, not 3"


def test_the_planted_failure_faculty_ignoring_the_base_reads_two_and_not_six(monkeypatch):
    """The assertion above can observe the failure it excludes: with the attribute read removed the 6 rolls 2."""
    w = _w(**{HIGH: {ATTR: 6}})
    assert sigma.faculty(w, w.persons[HIGH], TELL) == 6
    monkeypatch.setattr(sigma, "_authored_attribute", lambda entity, verb: None)
    assert sigma.faculty(w, w.persons[HIGH], TELL) == w.fixtures.get("pool_default") != 6


def test_a_verb_with_no_vocation_ignores_the_attributes():
    w = _w(**{HIGH: {ATTR: 6}})
    assert VERB_CAPABILITY.get("determine") is None
    assert sigma.faculty(w, w.persons[HIGH], "determine") == w.fixtures.get("pool_default")
    assert sigma._opposition_of(w, HIGH, "determine") is None


# ======================================================================================
# THE HELD KEY: practice raises a pool, never lowers the base; the opposition is the larger score
# ======================================================================================

def test_the_pool_is_the_larger_of_the_base_and_the_held_key():
    key = VERB_CAPABILITY[TELL]
    w = _w(**{LOW: {ATTR: 3}, MID: {ATTR: 2}, HIGH: {ATTR: 6}})
    w.persons[LOW].capability = {key: 5}                  # practice above the attribute
    w.persons[MID].capability = {key: 1}                  # a held key below the attribute
    w.persons[HIGH].capability = {key: 4}
    assert sigma.faculty(w, w.persons[LOW], TELL) == 5
    assert sigma.faculty(w, w.persons[MID], TELL) == 2
    assert sigma.faculty(w, w.persons[HIGH], TELL) == 6
    assert [sigma._opposition_of(w, p, TELL) for p in (LOW, MID, HIGH)] == [5.0, 2.0, 6.0]


def test_a_held_key_alone_is_what_it_was_before_the_carrier():
    key = VERB_CAPABILITY[TELL]
    w = _w()
    w.persons[LOW].capability = {key: 4}
    assert sigma.faculty(w, w.persons[LOW], TELL) == 4 and sigma._opposition_of(w, LOW, TELL) == 4.0
    # a held key BELOW pool_default with no attribute stands alone: a held 0 is still a person under one die
    # (the plan's "larger of the key and the base" binds where an attribute is held; `test_odds_of.py` pins this)
    w.persons[MID].capability = {key: 0}
    assert sigma.faculty(w, w.persons[MID], TELL) == 0


# ======================================================================================
# THE ROSTER IS CLOSED BOTH WAYS
# ======================================================================================

def test_the_shipped_roster_covers_the_vocations_with_the_ten():
    assert set(VOCATION_ATTRIBUTE) == set(VOCATIONS) and VOCATIONS, "empty or open"
    assert set(VOCATION_ATTRIBUTE.values()) <= set(descriptors.ATTRIBUTES)


def test_the_loader_refuses_a_vocation_with_no_row_a_non_vocation_row_and_a_non_attribute():
    good = dict(VOCATION_ATTRIBUTE)
    voc = set(VOCATIONS)
    assert _load_vocation_attribute(good, voc) == good
    first = sorted(good)[0]
    with pytest.raises(Unspecified):
        _load_vocation_attribute({k: v for k, v in good.items() if k != first}, voc)      # no row for a vocation
    with pytest.raises(Unspecified):
        _load_vocation_attribute({**good, "dancing": "attr.body.agility"}, voc)           # a row for a non-vocation
    with pytest.raises(Unspecified):
        _load_vocation_attribute({**good, first: "attr.mind.nonsense"}, voc)              # none of the ten
    with pytest.raises(Unspecified):
        _load_vocation_attribute({**good, first: "attr.social.bonds"}, voc)               # retired, not one of the ten


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
        "attr.mind.acuity": 2, "attr.mind.will": 7, "attr.social.grace": 1}


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
    """`cast_attributes=False` (the shipped control) leaves every person with no attribute; `True` writes the
    one row the registry authors (NPC-001, Edeyja) and nobody else. The event-list and hash readings of the two
    arms are in `build_realm`'s docstring and the CR-20 commit body (the arm-off list equals the parent tree's)."""
    from engine.season.harness import populated as PO
    off = PO.build_realm(0)
    assert not [p.id for p in off.persons.values() if p.attributes]
    on = PO.build_realm(0, cast_attributes=True)
    assert [p.id for p in on.persons.values() if p.attributes] == ["p_npc_001"]
    assert on.persons["p_npc_001"].attributes == cast.attributes_of(cast.row("NPC-001"))
