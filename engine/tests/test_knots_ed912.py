"""The knots oracle draws only from a seeded generator (08_FI_04 §5)."""
from engine.dice_engine.draw import seeded
from types import SimpleNamespace

import pytest

from systems.fieldwork.sim import knots


def _actor():
    return SimpleNamespace(bonds=5, disposition=5, ts=40, spirit=3)


def test_form_knot_with_no_rng_raises():
    with pytest.raises(TypeError):
        knots.form_knot("a", "b", None, actor_a_obj=_actor(), actor_b_obj=_actor())


def test_a_knot_with_oneself_is_none():
    assert knots.form_knot("a", "a", None, actor_a_obj=_actor(), actor_b_obj=_actor(),
                           rng=seeded("0123456789abcdef")) is None
