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


@pytest.mark.parametrize('stat', ['I', 'L', 'W', 'Sta', 'Mil'])
def test_every_declared_faction_stat_floors_at_zero(stat):
    """RULED 2026-08-23 by Jordan — TWO rulings that between them flattened this table.

      * "Influence can be 0." SUPERSEDES ED-IN-0029's floor of 1 (OPT-AV-14/D14, rationale "never
        fully vanishes institutionally"), which S5d had wired one day earlier.
      * "Legitimacy is a base." `fac.legitimacy` joins the registry, so `L` — which twenty of
        `adjust`'s 31 non-test call sites write, the majority of all traffic — clamps from the
        registry instead of falling back to the blanket 0.5.

    So all six declared faction stats now floor at 0. Before S5d every stat clamped at a blanket
    0.5, which was wrong in BOTH directions: above the ratified floor for four stats, below it for
    Influence. It is now one number, and it is the registry's."""
    assert _sunk(stat) == 0, f'{stat} should floor at 0, got {_sunk(stat)}'


def test_legitimacy_is_a_declared_base_descriptor():
    """The ruling itself, pinned at the registry rather than at the clamp — so a future edit that
    silently drops `fac.legitimacy` fails here with the ruling's name on it rather than as a
    mysterious golden move.

    ⚠ `fac.legitimacy` is NOT Mandate. Mandate remains the size-weighted derived aggregate of
    settlement L/PS (settlement_layer §1.8). The code field `Faction.L` has served as both at
    different times — `parliamentary_bridge` still comments "Mandate == Faction.L pre-LPS-1" — and
    that conflation is older than this ruling and is not resolved by it."""
    assert descriptors.faction_bounds('L') == (0, 7), (
        'L lost its registry bounds. Jordan ruled 2026-08-23 that Legitimacy IS a base descriptor; '
        'if that was reversed, say so here and restore the UNDECLARED fallback path.'
    )
    assert 'fac.legitimacy' in descriptors.FACTION_STATS
    assert descriptors.FACTION_FIELD_MAP['fac.legitimacy'] == 'L'
    assert len(descriptors.FACTION_STATS) == 6, (
        f'the faction roster is {len(descriptors.FACTION_STATS)} stats, expected 6 '
        f'(influence, legitimacy, wealth, military, intel, stability)'
    )


def test_the_undeclared_fallback_is_now_unreachable_for_faction_stats_but_kept():
    """`UNDECLARED_FLOOR`/`_CEILING` existed for `L` alone. With `L` declared, no faction stat
    reaches them — but they are NOT dead, and deleting them would be the wrong cleanup: `MULTS`
    carries `accord` and `pt`, which are Territory fields, and `echo_transport`'s dynamic write is
    gated on MULTS membership rather than on the registry. A caller can still pass a stat the
    registry knows nothing about."""
    assert Faction.UNDECLARED_FLOOR == 0.5 and Faction.UNDECLARED_CEILING == 7.0
    for stat in ('I', 'L', 'W', 'Sta', 'Mil'):
        assert descriptors.faction_bounds(stat) is not None, (
            f'{stat} fell back to the undeclared bounds — the registry should own every faction stat'
        )
    assert descriptors.faction_bounds('accord') is None, (
        'accord is a Territory field; if the registry now declares it as a FACTION stat, that is a '
        'roster change that needs saying out loud'
    )


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
