"""B01a.01 -- EVERY PERSON WITHOUT AUTHORED VALUES DRAWS ALL TEN ATTRIBUTES, UNIFORM ON `generated_attribute_range`, KEYED.

`state/carriers.py::generated_attributes(world_seed, pid, span)` is the one owner: one keyed draw per (person, attribute)
through `state/ids.py::draw_factory` (the clock argument is 0), so a sheet is a function of (seed, person id, attribute)
alone; an authored value replaces its own key only. `Fixtures generated_attribute_range` (H-856) is the setting: shipped
`(1, 6)`; `(2, 2)` is B01's flat seating at `pool_default` (the control); `None` is nothing generated.

The control proof (`(2, 2)` reproduces B01's close hashes) is read in process and recorded in the commit body, not kept
here (B02.01's rule).
"""
from __future__ import annotations

import pytest

from engine.substrate.descriptors import ATTRIBUTES

from ..data import cast
from ..gaps import Forbidden
from ..harness import populated
from ..harness.populated import build_realm
from ..state.carriers import generated_attributes
from ..state.ids import draw_factory

SHIPPED = (1, 6)


def _range_at(monkeypatch, value) -> None:
    """Sweep the setting for the life of one test, on the copy `build_realm` reads and the original."""
    from ..data.fixtures import DEFAULT_FIXTURES
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "generated_attribute_range", value)
    monkeypatch.setitem(populated.DEFAULT_FIXTURES._v, "generated_attribute_range", value)


def test_every_key_is_drawn_in_the_range_one_draw_per_key():
    lo, hi = SHIPPED
    checked = 0
    for pid in ("p_a", "p_b", "p_npc_001"):
        sheet = generated_attributes(7, pid, SHIPPED)
        assert list(sheet) == list(ATTRIBUTES) and len(sheet) == 10
        for key, value in sheet.items():
            assert lo <= value <= hi
            assert value == draw_factory(7, lambda: 0)(pid, f"attr.generated:{key}").randint(lo, hi)
            checked += 1
    assert checked == 30


def test_the_sheet_is_a_function_of_seed_person_and_key():
    checked = 0
    differing = 0
    for i in range(50):
        pid = f"p_x_{i:03d}"
        a, b = generated_attributes(0, pid, SHIPPED), generated_attributes(0, pid, SHIPPED)
        assert a == b
        differing += generated_attributes(1, pid, SHIPPED) != a
        checked += 1
    assert checked == 50
    assert differing >= 1, "two seeds drew the same sheet for fifty persons"


def test_a_realm_holds_every_value_of_the_range_on_every_key():
    w = build_realm(0)
    authored = cast.attributes_of(cast.row("NPC-001"))
    lo, hi = SHIPPED
    checked = 0
    for key in ATTRIBUTES:
        held = {p.attributes[key] for p in w.persons.values() if not (p.id == "p_npc_001" and key in authored)}
        for value in range(lo, hi + 1):
            assert value in held, (key, value)
            checked += 1
        assert held <= set(range(lo, hi + 1)), (key, held)
    assert checked == 60


def test_an_authored_value_overrides_its_key_only():
    w = build_realm(0)
    authored = cast.attributes_of(cast.row("NPC-001"))
    assert authored, "NPC-001 authors no attribute"
    drawn = generated_attributes(w.world_seed, "p_npc_001", w.fixtures.get("generated_attribute_range"))
    held = w.persons["p_npc_001"].attributes
    assert set(authored) < set(ATTRIBUTES), "the row must leave some key unauthored for this test to see the other half"
    for key in ATTRIBUTES:
        assert held[key] == (authored[key] if key in authored else drawn[key]), key


def test_the_sheet_does_not_read_pool_default(monkeypatch):
    from ..data.fixtures import DEFAULT_FIXTURES
    at_2 = {pid: dict(p.attributes) for pid, p in build_realm(0).persons.items()}
    monkeypatch.setitem(populated.DEFAULT_FIXTURES._v, "pool_default", 3)
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "pool_default", 3)
    at_3 = {pid: dict(p.attributes) for pid, p in build_realm(0).persons.items()}
    assert at_2 == at_3


def test_falsifier_a_realm_built_at_another_range_seats_that_range(monkeypatch):
    _range_at(monkeypatch, (3, 3))
    w = build_realm(0)
    authored = cast.attributes_of(cast.row("NPC-001"))
    checked = 0
    for p in w.persons.values():
        for key in ATTRIBUTES:
            if p.id == "p_npc_001" and key in authored:
                continue
            assert p.attributes[key] == 3, (p.id, key)
            checked += 1
    assert checked >= 10 * (len(w.persons) - 1)


def test_the_flat_range_is_lane_a_seating(monkeypatch):
    _range_at(monkeypatch, (2, 2))
    w = build_realm(0)
    pool_default = w.fixtures.get("pool_default")
    lane_a = {key: int(pool_default) for key in ATTRIBUTES}
    authored = cast.attributes_of(cast.row("NPC-001"))
    for p in w.persons.values():
        expected = {**lane_a, **(authored if p.id == "p_npc_001" else {})}
        assert p.attributes == expected, p.id


@pytest.mark.parametrize("bad", [(0, 6), (5, 4), (1, 8), (1.0, 6)])
def test_the_range_refuses_outside_the_scale(bad):
    with pytest.raises(Forbidden) as e:
        generated_attributes(0, "p_x", bad)
    assert "generated_attribute_range" in str(e.value)


# -- B01a.02: the in-play mint draws by the same owner -------------------------------------------------------------
def _place_that_holds_a_person(w) -> str:
    from ..state.world import rung_kind_ascends
    return next(r for r, rung in w.rungs.items() if rung_kind_ascends("person", rung.kind))


def test_a_person_individuated_in_play_holds_the_ten_drawn():
    from ..loop import census
    w = build_realm(0)
    pid = "p_minted_in_play"
    assert pid not in w.persons
    census._individuate(w, pid, _place_that_holds_a_person(w))
    expected = generated_attributes(w.world_seed, pid, w.fixtures.get("generated_attribute_range"))
    assert len(expected) == 10
    assert w.persons[pid].attributes == expected
    # the falsifier's second half: the sheet does not depend on the tick of the mint
    w.tick += 5
    census._individuate(w, "p_minted_later", _place_that_holds_a_person(w))
    assert w.persons["p_minted_later"].attributes == generated_attributes(
        w.world_seed, "p_minted_later", w.fixtures.get("generated_attribute_range"))


def test_with_nothing_generated_an_individuated_person_holds_none(monkeypatch):
    from ..loop import census
    _range_at(monkeypatch, None)
    w = build_realm(0)
    census._individuate(w, "p_minted_in_play", _place_that_holds_a_person(w))
    assert not w.persons["p_minted_in_play"].attributes


# -- B01a.03: the generic test cast, and the two pinned instruments' persons ----------------------------------------
def test_the_generic_cast_seats_every_empty_sheet_and_keeps_a_fixed_value():
    from ..harness.probes import tiny_world
    from ._generic_cast import seat_generic_cast
    fixed = {"p_low": {"attr.body.strength": 6}}
    w = seat_generic_cast(tiny_world(), fixed=fixed)
    span = w.fixtures.get("generated_attribute_range")
    checked = 0
    for pid, p in w.persons.items():
        assert list(p.attributes) == list(ATTRIBUTES) and len(p.attributes) == 10, pid
        drawn = generated_attributes(w.world_seed, pid, span)
        for key in ATTRIBUTES:
            want = 6 if (pid, key) == ("p_low", "attr.body.strength") else drawn[key]
            assert p.attributes[key] == want, (pid, key)
            checked += 1
    assert checked == 10 * len(w.persons)
    # two calls at one seed are equal; at another seed they differ
    again = seat_generic_cast(tiny_world(), fixed=fixed)
    other = seat_generic_cast(tiny_world(), seed=9, fixed=fixed)
    sheets = lambda x: {pid: dict(p.attributes) for pid, p in x.persons.items()}
    assert sheets(again) == sheets(w) and sheets(other) != sheets(w)
    # a key outside the ten refuses
    with pytest.raises(Exception):
        seat_generic_cast(tiny_world(), fixed={"p_low": {"attr.body.nonsense": 3}})


def test_a_corpus_case_person_holds_a_drawn_sheet():
    from ..harness import corpus_run
    from ..harness.run_cases import load_cases
    lo, hi = SHIPPED
    checked = 0
    for case in load_cases("NPC")[:8]:
        if str(case.get("scale")) not in corpus_run.RUNG_KINDS:
            continue
        w = corpus_run.build_at(case, 0)
        for pid, p in w.persons.items():
            assert list(p.attributes) == list(ATTRIBUTES), (case.get("id"), pid)
            assert all(lo <= v <= hi for v in p.attributes.values()), (case.get("id"), pid)
            checked += 1
    assert checked >= 5


def test_a_headless_person_holds_a_drawn_sheet():
    from ..harness import headless
    w = headless.build_world(0)
    assert len(w.persons) == 3
    for pid, p in w.persons.items():
        assert p.attributes == generated_attributes(w.world_seed, pid, w.fixtures.get("generated_attribute_range")), pid


# -- B01a.06: Spirit is its own attribute group, ten attributes ---------------------------------------------------
def test_the_roster_is_ten_keys_with_spirit_its_own_group():
    import tools.descriptor_registry as dr
    assert len(ATTRIBUTES) == 10
    assert "attr.spirit.will" in ATTRIBUTES and not any("threadsensitivity" in k for k in ATTRIBUTES)   # dropped, J-12
    assert "attr.mind.will" not in ATTRIBUTES
    # the registry's order: body, mind, spirit, social
    assert [k.split(".")[1] for k in ATTRIBUTES] == ["body"] * 3 + ["mind"] * 3 + ["spirit"] + ["social"] * 3
    reg = dr.load()
    assert dr.by_category(reg, "spirit") == ["attr.spirit.will"]
    assert dr.by_category(reg, "mind") == ["attr.mind.focus", "attr.mind.acuity", "attr.mind.perception"]
    assert dr.aggregate_members(reg, "agg.spirit") == ["attr.spirit.will"]
    assert "attr.mind.will" not in dr.aggregate_members(reg, "agg.mind")


def test_the_old_will_key_resolves_to_the_new_one():
    import tools.descriptor_registry as dr
    from engine.substrate import names as N
    from engine.substrate.descriptors import attribute_key
    assert attribute_key("attr.mind.will") == "attr.spirit.will"
    assert attribute_key("Will") == attribute_key("Spirit") == "attr.spirit.will"
    assert dr.resolve(dr.load(), "attr.mind.will")["key"] == "attr.spirit.will"
    assert N.canonical_for("attr.mind.will") == N.CANONICAL["attr.spirit.will"]


def test_a_sheet_holds_ten_keys_in_range():
    w = build_realm(0)
    lo, hi = SHIPPED
    authored = cast.attributes_of(cast.row("NPC-001"))
    checked = 0
    for p in w.persons.values():
        assert list(p.attributes) == list(ATTRIBUTES) and len(p.attributes) == 10, p.id
        for key, value in p.attributes.items():
            if p.id == "p_npc_001" and key in authored:
                continue
            assert lo <= value <= hi, (p.id, key)
            # each key is its own stream: no key draws from another key's
            assert value == draw_factory(w.world_seed, lambda: 0)(p.id, f"attr.generated:{key}").randint(lo, hi), (p.id, key)
            checked += 1
    assert checked >= 10 * (len(w.persons) - 1)
    assert "attr.mind.will" not in next(iter(w.persons.values())).attributes
