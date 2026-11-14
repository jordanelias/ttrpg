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
