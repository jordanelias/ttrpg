"""The one place a test asks for the flat fold: `task_draw_arm: off`.

With the arm on (B07.05) a converted task verb draws a band, and a Failure or Partial lands nothing or a fraction. A test
whose question is the verb's FOLD (what it writes, what it refuses, that the write EXECUTES) and not the draw runs the world
with the arm off, so the answer does not depend on which band a seed rolls. A test whose question is the draw
(`test_task_draw.py`, the realm pins) must NOT use this: it states the arm itself. Name the helper at the site; the reason is here.
"""
from engine.season.data.fixtures import Fixtures

ARM = "task_draw_arm"


def flat_fold_fixtures(fixtures: Fixtures) -> Fixtures:
    """`fixtures` with the task draw off. Reads the fixture first, so a renamed or mistyped arm fails here instead of
    sweeping nothing, and asserts the result reads `off` (a sweep that no-ops would leave the tests asking the draw)."""
    fixtures.get(ARM)
    flat = fixtures.sweep(ARM, "off")
    assert flat.get(ARM) == "off", flat.get(ARM)
    return flat


def flat_fold(w):
    """The world `w`, its fixtures swept to the flat fold; returns `w` for `tiny_world`-style chaining."""
    w.fixtures = flat_fold_fixtures(w.fixtures)
    return w
