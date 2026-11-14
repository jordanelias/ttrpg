"""The corpus run's seasons cap: absent, the shipped clamp; present, a bound a gate can read at two
seasons a case (D-17). The cap is read off the case's own `temporal`, not off `seasons_for`."""
from __future__ import annotations

from engine.season.harness import corpus_run as C
from engine.season.harness import run_cases as R


def _cases():
    return [c for lane in ("NPC", "ARC") for c in R.load_cases(lane)]


def _shipped(case: dict) -> int:
    t = case.get("temporal")
    span = t.get("span_seasons") if isinstance(t, dict) else None
    if isinstance(span, int) and span > 0:
        return min(span, C.MAX_SEASONS)
    return C.DEFAULT_SEASONS


def test_with_no_cap_every_case_runs_the_shipped_clamp():
    checked = 0
    for c in _cases():
        assert C.seasons_for(c) == _shipped(c), c.get("id")
        checked += 1
    assert checked >= 100


def test_a_cap_of_two_bounds_every_case():
    checked, saw_long, saw_one = 0, False, False
    for c in _cases():
        got = C.seasons_for(c, 2)
        assert got <= 2, c.get("id")
        assert got == min(C.seasons_for(c), 2), c.get("id")
        t = c.get("temporal")
        span = t.get("span_seasons") if isinstance(t, dict) else None
        saw_long = saw_long or (isinstance(span, int) and span > 2)
        if span == 1:
            saw_one = True
            assert got == 1, c.get("id")
        checked += 1
    assert checked >= 100
    # the cap was exercised against a case it cuts, and a case it leaves alone
    assert saw_long and saw_one


def test_the_command_line_reads_the_cap():
    assert C.parse_argv(["0", "--seasons", "2"]) == ([0], 2)
    assert C.parse_argv(["--seasons", "2", "1"]) == ([1], 2)
    assert C.parse_argv(["0"]) == ([0], None)
    assert C.parse_argv([]) == ([], None)
