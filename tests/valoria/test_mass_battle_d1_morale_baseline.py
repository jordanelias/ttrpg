"""d.1 — faction Stability sets a strategic unit's starting morale (ED-MB-0068).

WHY THIS EXISTS. Jordan ruled (ED-MB-0067) that faction Stability sets a unit's starting morale
when a battle is built from the strategic layer, superseding the untagged morale-starting-formula
sentence at `mass_battle_v30.md:230-231` ("General's Command + unit quality modifier") — NOT
PP-711, which is a DIFFERENT, live, already-implemented rule (the battle-boundary morale RESET,
`orchestration.py:reset_morale_between_battles`) unaffected by this change; see
`registers/editorial_ledger_mb.jsonl`'s ED-MB-0067, third correction row, for the full citation
history. `_faction_to_unit` previously hardcoded `morale=5, morale_start=5` with its own honest
`[canonical: inherited default — see GAP above]` comment — this is a NEW derivation, not an edit
to existing logic, so there is no prior test pinning the old flat-5 behaviour to update; this file
is the whole of its coverage.

SUBJECT, under CLAUDE.md §0.1 pt 5's load-bearing predicate: game math on the executable model
(a faction's Stability now decides the strength of the unit `_try_conquest` fields) and the
implementation of a Jordan ruling. Both halves of the predicate.
"""
from __future__ import annotations

import random

import pytest

from engine.autoload.game_state import Faction
from systems.mass_battle.sim import massbattle as MB


def test_two_factions_differing_only_in_stability_get_different_morale_starts():
    """(a) `Sta` 2.0 vs 6.0 -> `morale_start` 2 and 6 respectively, and morale == morale_start."""
    low = Faction(name='Low', Sta=2.0)
    high = Faction(name='High', Sta=6.0)

    u_low = MB._faction_to_unit(low)
    u_high = MB._faction_to_unit(high)

    assert u_low.morale_start == 2, f"Sta=2.0 should give morale_start 2, got {u_low.morale_start}"
    assert u_low.morale == u_low.morale_start, "morale and morale_start must agree at battle start"
    assert u_high.morale_start == 6, f"Sta=6.0 should give morale_start 6, got {u_high.morale_start}"
    assert u_high.morale == u_high.morale_start, "morale and morale_start must agree at battle start"
    # (F9) assert on what ROUT actually reads downstream, not only the constructor inputs: the
    # subunit's own `morale` field is left None (inherited), so `eff_morale`/`eff_morale_start`
    # fall through to the parent Unit's scalar (hierarchy/units.py's `_u().morale` fallback). A
    # future refactor that gives the subunit an explicit troop-type morale preset (e.g. via
    # `Subunit.of_type`) would silently stop reading the derived value while these two
    # constructor-level asserts kept passing — this closes that gap.
    assert u_low.subunits[0].eff_morale == 2, "subunit eff_morale did not inherit morale_start"
    assert u_low.subunits[0].eff_morale_start == 2, "subunit eff_morale_start did not inherit"


@pytest.mark.parametrize('sta, expected', [(0.0, 1), (7.0, 7)])
def test_boundary_stability_values_clamp_to_the_morale_ladder(sta, expected):
    """(b) `Sta=0.0` floors to morale_start 1 (canon's morale floor while a general is present,
    mass_battle_v30.md:254 — never 0, since rout fires at morale<=0). `Sta=7.0` is the confirmed
    ceiling (test_faction_stat_bounds.py: `Faction.Sta` floors at 0, ceilings at 7) and maps to
    morale_start 7 unchanged."""
    f = Faction(name='Probe', Sta=sta)
    unit = MB._faction_to_unit(f)
    assert unit.morale_start == expected, (
        f"Sta={sta} should give morale_start {expected}, got {unit.morale_start}")
    assert unit.morale == unit.morale_start


@pytest.mark.parametrize('sta, expected', [(3.5, 4), (4.5, 5), (5.5, 6), (2.5, 3)])
def test_half_boundary_rounding_is_symmetric_not_banker_rounded(sta, expected):
    """(b2, extending b) Python's bare `round()` is round-half-to-even (banker's rounding): `round(4.5) == 4` but
    `round(3.5) == 4` too, an undisclosed asymmetry with no game meaning. `Sta` reaches exact .5
    boundaries in ordinary play — a Govern Failure is exactly -5 granular = -0.5 Sta
    (`faction_action.py:490`, `MULTS['Sta']=10`) — so this is not a theoretical edge case.
    `_morale_start_from_stability` must round every .5 boundary the SAME way (half-up), so e.g.
    Sta 4.0 -> 4.5 (a positive nudge) and Sta 5.0 -> 4.5 (a Govern-failure nudge down) agree that
    4.5 rounds to 5, rather than one of them landing on 4 by parity accident."""
    f = Faction(name='Boundary', Sta=sta)
    unit = MB._faction_to_unit(f)
    assert unit.morale_start == expected, (
        f"Sta={sta} should round half-up to {expected}, got {unit.morale_start} "
        f"(bare round() would give {round(sta)} — check for banker's-rounding regression)")


def test_garrison_stub_keeps_the_pre_change_morale_of_five():
    """(c) `_GarrisonStub` (no strategic Faction backs an uncontrolled territory) resolves to the
    PRE-d.1 flat morale_start of 5, unchanged — so any golden movement this commit causes is
    attributable to real factions' Stability alone, not to a simultaneous garrison-stub change."""
    stub = MB._GarrisonStub(name='Uncontrolled', Mil=1.5)
    unit = MB._faction_to_unit(stub)
    assert unit.morale_start == 5, f"garrison stub morale_start moved, got {unit.morale_start}"
    assert unit.morale == 5, f"garrison stub morale moved, got {unit.morale}"


def test_resolve_mass_battle_is_still_deterministic_under_a_fixed_seed():
    """(d) Same-seed determinism must survive this change: `resolve_mass_battle` under a fixed
    seed returns byte-identical results across two runs. Follows massbattle.py's own
    `rngsource.using`/`world.rng` convention (massbattle.py:108-124 pre-edit, now further down
    the file) rather than a bare `random.seed()` call, since that convention is what makes the
    campaign's seeded goldens reproducible at all (rngsource.py's own module docstring)."""
    class _World:
        def __init__(self, seed):
            self.rng = random.Random(seed)

    def _run(seed):
        a = Faction(name='Attacker', Sta=5.0, Mil=4.0)
        b = Faction(name='Defender', Sta=3.0, Mil=3.0)
        world = _World(seed)
        return MB.resolve_mass_battle(a, b, terrain=None, world=world)

    r1 = _run(12345)
    r2 = _run(12345)

    assert r1 == r2, f"same-seed resolve_mass_battle diverged: {r1} vs {r2}"
    # the determinism claim would be vacuous if resolve_mass_battle silently no-op'd — confirm the
    # result actually carries the shape a real battle resolution produces (§0.1 pt 2: an assertion
    # must be able to observe the failure it excludes).
    assert set(r1) == {'attacker_wins', 'degree', 'attacker_size_pct', 'defender_size_pct'}
    assert r1['degree'] in ('Overwhelming', 'Success', 'Partial', 'Failure')


def test_morale_start_is_monotone_and_bounded_across_the_whole_stability_range():
    """(e) A sweep of every declared Stability value on its ladder (0..7, matching
    test_faction_stat_bounds.py's confirmed floor/ceiling), asserting the derivation is monotone
    non-decreasing and stays within the canon morale ladder [1, 7] throughout. Per CLAUDE.md
    §0.1 pt 2, a loop that asserts conditionally must also assert that it checked something."""
    checked = 0
    prev_morale = None
    for tenth in range(0, 71):
        sta = tenth / 10.0
        f = Faction(name='Sweep', Sta=sta)
        unit = MB._faction_to_unit(f)
        assert 1 <= unit.morale_start <= 7, (
            f"Sta={sta} produced out-of-ladder morale_start {unit.morale_start}")
        if prev_morale is not None:
            assert unit.morale_start >= prev_morale, (
                f"morale_start regressed as Sta rose to {sta}: {prev_morale} -> {unit.morale_start}")
        prev_morale = unit.morale_start
        checked += 1
    assert checked >= 71, f"the Stability sweep only checked {checked} values — it did not run"
