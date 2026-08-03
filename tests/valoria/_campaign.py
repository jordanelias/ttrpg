"""Shared seeded-campaign runner for the Key-emitter tests (ED-IN-0123).

WHY THIS EXISTS. `test_battle_concluded_key.py` and `test_public_governance_transfer_key.py` both
need the same three things from one seeded run — the `CampaignResult`, the `World` it mutated, and
a count of Keys emitted by type — and each had grown its own `campaign` fixture doing a subset.
`tools/build_test_register.py`'s duplicated-helper ratchet caught the second copy the moment it
landed (21 -> 22 duplicated helper names), which is the ratchet working: a helper needed twice
belongs in a shared module, not copied. Extracted here rather than renamed, because renaming would
have satisfied the counter while leaving the duplication.

Two things this owns that a caller should not re-derive:

  * **`VALORIA_STRICT_KEYS`.** The emitters deliberately swallow exceptions so telemetry can never
    take down a campaign turn — and a swallowed exception is exactly where a malformed payload
    would hide. Under the flag a `KeyValidationError` propagates, so a green run is evidence the
    payload validates against the registry rather than evidence that nothing was checked.
  * **Capturing the `World`.** `run_campaign` does not return it, so `create_world` is spied. Doing
    this ad hoc in each test file is how the two copies started.
"""
from __future__ import annotations

import collections
import os


def run(seed: int, *, seasons: int | None = None, strict_keys: bool = True):
    """Run one seeded campaign. Returns (result, world, keys_by_type).

    `seasons` overrides CAMPAIGN_SEASONS. Note that `run_campaign`'s own `max_seasons` argument is
    NOT the way to do this: it is shadowed by `effective_params.get('CAMPAIGN_SEASONS', ...)`, so
    passing max_seasons silently does nothing — a control that controls nothing.
    """
    from engine import mc_v18
    from engine.autoload import game_state
    from engine.substrate import keys as ks

    seen: collections.Counter = collections.Counter()
    real_emit = ks.TickScheduler.emit
    real_create = game_state.create_world
    captured: dict = {}

    def emit_spy(self, key, apply=None):
        seen[key.type] += 1
        return real_emit(self, key, apply)

    def create_spy(*a, **k):
        world = real_create(*a, **k)
        captured['world'] = world
        return world

    params = {'ECHO_TRANSPORT': True}
    if seasons is not None:
        params['CAMPAIGN_SEASONS'] = seasons

    ks.TickScheduler.emit = emit_spy
    game_state.create_world = create_spy
    if strict_keys:
        os.environ['VALORIA_STRICT_KEYS'] = '1'
    try:
        result = mc_v18.run_campaign(seed=seed, params=params)
    finally:
        ks.TickScheduler.emit = real_emit
        game_state.create_world = real_create
        if strict_keys:
            os.environ.pop('VALORIA_STRICT_KEYS', None)
    return result, captured.get('world'), seen


def initial_owners(seed: int) -> dict:
    """Territory ownership at t0. `create_world(seed)` is deterministic, so re-creating the world
    reproduces initial conditions without needing a snapshot taken mid-run."""
    from engine.autoload import game_state
    return owners_of(game_state.create_world(seed=seed))


def owners_of(world) -> dict:
    terrs = world.territories.values() if isinstance(world.territories, dict) else world.territories
    return {t.tid: t.owner for t in terrs}
