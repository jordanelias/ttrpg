"""A seizure writes Territory.accord on the CONTINUOUS scale, not a canon tier (ED-FA-0037).

THE DEFECT THIS PINS. `systems/factions/sim/mass_seizure.py` computed `starting_accord`
as a canonical Accord TIER (an int, 0-4 in `ACCORD_MAP`'s domain) and then assigned it
straight into `Territory.accord`, which is the CONTINUOUS 1.0-7.0 field:

    t.accord = float(starting_accord)      # tier 2 -> 2.0

`ACCORD_MAP` is the tier->continuous table (`{0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}`) and
`engine/substrate/canon_buckets.canonical_accord` is its inverse. Reading a raw tier back
through the inverse loses tiers:

    canonical_accord(2.0) == 1   # wrote tier 2, reads back tier 1
    canonical_accord(3.0) == 1   # wrote tier 3, reads back tier 1  (TWO tiers)

`starting_accord` on a successful seizure is always 2 or 3 (`SEIZURE_ACCORD_FLOOR = 2`;
Overwhelming caps at 3), so EVERY seizure was corrupting the field — the two reachable
values are exactly the two worst cases.

The code flagged itself: ":Convert int accord to ACCORD_MAP-style continuous if needed;
for now, set directly". The sibling site had already done it correctly
(`parliamentary_transfer.py:346`, `terr.accord = ACCORD_MAP[accord_level]`).

REACHABILITY, stated honestly. `resolve_mass_seizure` has zero non-test callers, and a
default `create_world` has no Religious Buildings at all, so this never fired in a
campaign — the defect is LATENT, not live, and no golden moves. This file is the first
thing that has ever executed the function (CLAUDE.md §0.2).

FALSIFIER. `test_seized_accord_round_trips_to_its_tier` fails against the pre-fix tree
(`canonical_accord(2.0) == 1 != 2`) and passes after.
"""
from __future__ import annotations

import random

import pytest

from engine.autoload.game_state import ACCORD_MAP, create_world
from engine.substrate.canon_buckets import canonical_accord
from systems.factions.sim import mass_seizure as MS
from systems.settlements.sim import infrastructure as INFRA


def _world_with_a_seizable_church_territory():
    """A real world, minimally arranged so a seizure can actually resolve.

    Built through the public constructors (`create_world`, `build_infrastructure`)
    rather than by mocking the precondition helpers — a test that stubs
    `_has_church_building` would prove nothing about the write path.
    """
    w = create_world(seed=0)
    INFRA.reset_infrastructure(w)

    tid = sorted(w.territories)[0]
    t = w.territories[tid]
    # Church-owned => auto-Prominent under PP-534's Self-Control Rule.
    t.owner = "Church"
    # A Chapel is the Religious Building floor §3.2 asks for.
    INFRA.build_infrastructure(tid, INFRA.BUILDING_CHAPEL, w)

    assert MS._has_church_building(w, tid), "fixture: territory must carry a Religious Building"
    assert MS._church_is_prominent_for_seizure(w, tid), "fixture: Church must be Prominent"
    return w, tid


def _seize(w, seed):
    return MS.resolve_mass_seizure(w, rng=random.Random(seed))


def _first_successful_seizure(max_seeds=200):
    """Find a seed that actually seizes, and PROVE we found one.

    Per CLAUDE.md §0.1 pt 2: a loop that asserts conditionally must assert that it
    asserted. Without the final `pytest.fail`, a run where nothing ever seizes would
    report green while testing nothing.
    """
    for seed in range(max_seeds):
        w, tid = _world_with_a_seizable_church_territory()
        results = _seize(w, seed)
        seized = [r for r in results if r.seized]
        if seized:
            return w, results, seized, seed
    pytest.fail(
        f"no seizure succeeded in {max_seeds} seeds — the fixture no longer exercises "
        "the write path this test exists to pin"
    )


def test_the_fixture_actually_reaches_the_resolver():
    """Guard the guard: if the preconditions rot, every assertion below goes vacuous."""
    w, tid = _world_with_a_seizable_church_territory()
    results = _seize(w, 0)
    assert results, "resolve_mass_seizure returned nothing — preconditions not met"
    assert any(r.territory_id == tid for r in results)


def test_seized_accord_round_trips_to_its_tier():
    """THE FALSIFIER. Pre-fix: canonical_accord(2.0) == 1 != 2, and this fails."""
    w, _results, seized, _seed = _first_successful_seizure()

    for r in seized:
        written = w.territories[r.territory_id].accord
        assert written == ACCORD_MAP[r.starting_accord], (
            f"{r.territory_id}: accord written as {written}, expected "
            f"ACCORD_MAP[{r.starting_accord}] == {ACCORD_MAP[r.starting_accord]}"
        )
        assert canonical_accord(written) == r.starting_accord, (
            f"{r.territory_id}: wrote tier {r.starting_accord} but it reads back as "
            f"tier {canonical_accord(written)} — the tier was lost in the write"
        )


def test_written_accord_is_on_the_continuous_scale():
    """The field's domain is ACCORD_MAP's values, never its keys.

    A raw tier index is always < the smallest legal continuous value except for the
    degenerate tier-0 case, so this catches the class rather than the two instances.
    """
    _w, _results, seized, _seed = _first_successful_seizure()
    legal = set(ACCORD_MAP.values())

    for r in seized:
        written = _w.territories[r.territory_id].accord
        assert written in legal, (
            f"{r.territory_id}: accord {written} is not a canonical continuous value "
            f"({sorted(legal)}) — a tier index was probably written raw"
        )


def test_the_reachable_tiers_are_exactly_the_corrupting_ones():
    """Documents WHY this mattered: every value this site can produce was wrong.

    SEIZURE_ACCORD_FLOOR clamps success to >= 2 and Overwhelming caps at 3, so the
    reachable set is {2, 3} — and float(2)/float(3) both read back as tier 1.
    """
    assert MS.SEIZURE_ACCORD_FLOOR == 2
    for tier in (2, 3):
        assert canonical_accord(float(tier)) != tier, (
            f"tier {tier} written raw would round-trip correctly — the premise of "
            "ED-FA-0037 no longer holds and this test should be re-derived"
        )
        assert canonical_accord(ACCORD_MAP[tier]) == tier
