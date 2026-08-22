"""ED-IN-0029's per-stat floors, wired into `Faction.adjust` at plan S5d (2026-08-22).

WHY THIS FILE EXISTS AT ALL — it was missing, and an adversarial pass said so. S5d shipped a
behaviour change on the live campaign path whose entire evidence was an unrun oracle script and a
set of moved goldens. A golden says "something moved"; it never says "Influence now floors at 1".
§0.1 pt 3: a result claim carries, in the same commit, the specific test that would have shown it
wrong. This is that test.

SUBJECT, under §0.1 pt 5: the clamp on faction stats in the live campaign loop — game math, and the
implementation of a Jordan-ratified canon decision (ED-IN-0029, 2026-07-08). Both halves of the
predicate, like `test_faction_obstacle_conventions.py`.

WHAT THE CANON SAYS: Influence floors at 1 — an institution's influence never fully vanishes —
while Wealth, Military, Stability and Intel float at 0. Everything ceilings at 7.
"""
from __future__ import annotations

import pytest

from engine.autoload.game_state import Faction, MULTS
from engine.substrate import descriptors


def _sunk(stat, start=3.0):
    """A faction with `stat` driven as far down as `adjust` will allow."""
    f = Faction(name='probe', L=start, Sta=start, W=start, I=start, Mil=start)
    f.adjust(stat, -1000 * MULTS[stat])
    return getattr(f, stat)


def _raised(stat, start=3.0):
    f = Faction(name='probe', L=start, Sta=start, W=start, I=start, Mil=start)
    f.adjust(stat, 1000 * MULTS[stat])
    return getattr(f, stat)


def test_influence_floors_at_one_not_at_the_old_blanket_half():
    """The floor ED-IN-0029 actually changed the meaning of. Before S5d this returned 0.5."""
    assert _sunk('I') == 1, (
        'Influence no longer floors at 1. ED-IN-0029 (ratified 2026-07-08) floors it there because '
        'an institution never fully loses influence; 0.5 would be the pre-S5d blanket floor '
        'returning.'
    )


@pytest.mark.parametrize('stat', ['W', 'Sta', 'Mil'])
def test_the_other_declared_stats_float_to_zero(stat):
    """Before S5d these clamped at 0.5, which is ABOVE the ratified floor — the blanket was wrong in
    both directions, not merely conservative."""
    assert _sunk(stat) == 0, f'{stat} should floor at 0 per ED-IN-0029, got {_sunk(stat)}'


def test_legitimacy_keeps_the_undeclared_fallback_because_Q1_is_open():
    """`L` is the one Faction field the registry declares nothing for, and whether Legitimacy is a
    base descriptor or derived like Mandate is Q1, Jordan's open ruling. `adjust` therefore falls
    back to the pre-S5d bounds for it. Twenty of the 31 non-test call sites adjust `L`, so this is
    the majority of traffic and it is deliberately unchanged: giving it a floor here would be
    authoring canon inside a wiring commit.

    When Q1 is ruled, this test is the work-list entry."""
    assert descriptors.faction_bounds('L') is None, (
        'the registry now declares bounds for L — if Q1 was ruled, wire it and rewrite this test'
    )
    assert _sunk('L') == Faction.UNDECLARED_FLOOR == 0.5
    assert _raised('L') == Faction.UNDECLARED_CEILING == 7.0


@pytest.mark.parametrize('stat', ['I', 'W', 'Sta', 'Mil', 'L'])
def test_every_stat_still_ceilings_at_seven(stat):
    """ED-IN-0029 moved floors, not ceilings. A ceiling change would be a balance change nobody
    ratified, and it would be invisible in a floor-focused review."""
    assert _raised(stat) == 7


def test_adjust_actually_consults_the_registry_rather_than_hardcoding_the_same_numbers():
    """§0.1 pt 2 — the tests above pass equally if someone hardcodes `1` and `0` in `adjust`, which
    is the same defect the S1 commit found in `assert_faction_roster_is_covered`: an assertion
    observing a layer BELOW the one it excludes. This drives the value from the REGISTRY side and
    asserts the clamp follows, so the wiring itself is what is under test."""
    original = descriptors.FACTION_STATS['fac.wealth']
    descriptors.FACTION_STATS['fac.wealth'] = dict(original, floor=4)
    try:
        assert _sunk('W') == 4, (
            'adjust did not follow a changed registry floor — it is not reading faction_bounds(), '
            'it is hardcoding numbers that happen to match ED-IN-0029 today.'
        )
    finally:
        descriptors.FACTION_STATS['fac.wealth'] = original
    assert _sunk('W') == 0, 'the fixture did not restore the registry'


def test_intel_has_a_declared_floor_that_no_code_path_can_reach():
    """The honest half of S5d, pinned so it is not quietly forgotten or quietly "fixed" by inventing
    a multiplier. `fac.intel` is a ratified faction stat with a registry floor of 0, and `MULTS`
    carries no `intel` key — so `adjust('intel', …)` raises before any bound is consulted. Wiring it
    needs a canon multiplier nobody has stated.

    If this test starts failing because `MULTS['intel']` exists, that is a canon value arriving:
    check it was ratified, then delete this test and add `intel` to the parametrized floors above."""
    assert descriptors.faction_bounds('intel') == (0, 7)
    assert 'intel' not in MULTS
    with pytest.raises(KeyError):
        Faction(name='probe').adjust('intel', -10)


def test_no_caller_overrides_the_bounds():
    """The `floor`/`ceiling` parameters survive with no live caller. If one appears, the registry has
    stopped being the single owner of these numbers and this test should fail loudly rather than
    the override sitting unnoticed in one subsystem."""
    import ast
    import pathlib

    repo = pathlib.Path(__file__).resolve().parents[2]
    overriders = []
    scanned = 0
    for path in list(repo.glob('engine/**/*.py')) + list(repo.glob('systems/**/*.py')):
        rel = path.relative_to(repo).as_posix()
        if '__pycache__' in rel or '/tests/' in rel:
            continue
        scanned += 1
        try:
            tree = ast.parse(path.read_text(encoding='utf-8'))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and node.func.attr == 'adjust'):
                if len(node.args) > 2 or any(k.arg in ('floor', 'ceiling') for k in node.keywords):
                    overriders.append(f'{rel}:{node.lineno}')
    assert scanned > 50, f'the walk only scanned {scanned} files — it is broken, not clean'
    assert not overriders, (
        'call site(s) override the registry bounds: ' + ', '.join(overriders) + '. That is how a '
        'stat quietly acquires two floors. If a locally-canonical bound is genuinely needed, say so '
        'in the plan and record it here.'
    )
