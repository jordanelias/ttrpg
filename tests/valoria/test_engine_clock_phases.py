"""The tick's three phases happen in the right order, in the right module (ED-IN-0199).

WHAT THIS PINS, AND WHY IT IS NOT APPARATUS-GUARDING-APPARATUS.
`propagation_spec_v1.md` §O.1 makes engine_clock the owner of SEASON_TICK -> ACTION ->
ACCOUNTING_BOUNDARY. Until this commit that module did not exist, and the scheduler's two
phase calls lived at the tail of `mc_v18._faction_actions_callback` — inside the ACTION
phase's own body:

    _sched.accounting_boundary()   # mc_v18.py:168 at 3d04568
    _sched.next_tick()             # mc_v18.py:169

`next_tick()` sets `_phase = _PHASE_ACTION`. Running it there meant the scheduler was in the
ACTION phase for the whole of `run_accounting`, and `keys.py:_emit_at_depth` defers an
`apply` precisely when `_phase == _PHASE_ACTION`. So an accounting-phase emission carrying a
settlement effect would have been queued to the NEXT season's boundary — a silent one-tick
lag on every accounting-phase deferred apply.

CLAUDE.md §0.1 pt 5's predicate admits this guard: the artifact is the tick's phase ordering,
which is load-bearing on the game (it decides when a settlement effect lands) and on the port
(Godot re-implements this loop). It is not a test of a checker.

REACHABILITY, STATED HONESTLY. `systems/overview/sim/accounting.py` emits no Keys today, so
the defect is LATENT and the re-siting moved no campaign output — five seeded campaigns and
both pinned batches were byte-identical including `key_log_hash` (recorded in the commit). The
point of moving it while inert is that the first accounting-phase emitter to land would
otherwise have inherited the bug, and its symptom reads as a balance question, not a phase bug.

THE FALSIFIER is `test_accounting_runs_inside_the_accounting_phase`. Against the pre-move tree
it fails: the scheduler is in ACTION when accounting's body runs. The other tests here pin the
things a naive "fix" would break instead — the boundary drains BEFORE accounting rather than
after, the tick counter spans both phases, and the flag-off path still runs.
"""
from __future__ import annotations

import pytest

from engine.autoload import engine_clock
from engine.autoload.game_state import create_world
from engine.cross_scale import echo_transport
from engine.substrate import composition, keys as K
from systems.overview.sim import accounting as accounting_module


ACTION = K._PHASE_ACTION
ACCOUNTING = K._PHASE_ACCOUNTING


@pytest.fixture
def world():
    w = create_world(seed=0)
    w.echo_scheduler = echo_transport.make_scheduler()
    w.key_log = w.echo_scheduler.log
    return w


@pytest.fixture
def spy_accounting(monkeypatch):
    """Observe the scheduler's phase from INSIDE accounting's body.

    `composition.require` memoises per role, so replacing the module attribute is not
    enough on its own — the cache entry has to go too, and be restored, or a later test
    in the same process would keep the spy. `monkeypatch.setitem`/`delitem` handle the
    restore; the explicit pop covers the case where nothing had resolved the role yet.
    """
    calls = []

    def _spy(w):
        calls.append(w.echo_scheduler._phase)
        return accounting_module.run_accounting(w)

    composition._CACHE.pop('accounting', None)
    monkeypatch.setitem(composition._CACHE, 'accounting', _spy)
    yield calls
    composition._CACHE.pop('accounting', None)


# ── The falsifier ─────────────────────────────────────────────────────────────────────

def test_accounting_runs_inside_the_accounting_phase(world, spy_accounting):
    """THE FALSIFIER. Pre-move this observes ACTION, because next_tick() had already run."""
    engine_clock.run_tick(world, action_callback=lambda w: None)

    assert spy_accounting == [ACCOUNTING], (
        f"accounting's body ran with the scheduler in {spy_accounting} — it must run inside "
        "ACCOUNTING_BOUNDARY, or every deferred apply it emits slips a tick"
    )


def test_accounting_runs_exactly_once_per_tick(world, spy_accounting):
    """One tick, one accounting pass.

    ⚠ THE JUSTIFICATION THIS TEST FIRST CARRIED WAS FALSE, and is corrected rather than
    quietly reworded: it claimed to be the §0.1-pt-2 non-vacuity guard for the falsifier
    above, on the reasoning that a spy which never fired would leave that test "vacuous on an
    empty list". It would not — `assert [] == [ACCOUNTING]` FAILS. The falsifier is already
    non-vacuous by construction, and a guard that cannot fail for the reason it states is
    worse than no guard.

    What this DOES catch is a real defect the falsifier cannot see: accounting running twice.
    `run_tick` resolves the role and calls it once; a future edit that also left a call in
    `season.run_season`, or re-added one to the action body, would double-apply a whole
    accounting pass while the phase assertion above stayed green.
    """
    engine_clock.run_tick(world, action_callback=lambda w: None)
    assert spy_accounting == [ACCOUNTING], (
        f"accounting ran {len(spy_accounting)} time(s) this tick, expected exactly 1"
    )


# ── Ordering around the boundary ──────────────────────────────────────────────────────

def _payload_free_type(registry) -> str:
    """The first registered Key type that demands no payload fields.

    Chosen from the registry rather than hard-coded so this test does not become a second,
    silently-drifting copy of the type roster; sorted so the choice is deterministic across
    runs and workers.
    """
    for type_id in sorted(registry.types):
        if not (registry.require(type_id).get("required_payload_fields") or []):
            return type_id
    raise AssertionError("every Key type now requires payload fields — pick one and fill it")


def _emit_with_deferred_apply(world, landed):
    """Emit one Key carrying an `apply`, the OF-7 shape the boundary exists to drain."""
    sched = world.echo_scheduler
    type_id = _payload_free_type(sched.log.registry)
    key = K.Key(
        id="ed-in-0199-probe",
        type=type_id,
        emitted_at=K.EmittedAt(season_index=world.season),
        targets=[K.Target(actor_id="probe", role="subject")],
    )
    sched.emit(key, apply=lambda _k: landed.append(world.echo_scheduler._phase))


def test_a_deferred_apply_lands_before_accounting_not_after(world, spy_accounting):
    """The boundary DRAINS, then accounting runs — not the other way round.

    A plausible wrong fix is to call `accounting_boundary()` after `run_accounting`, which
    would also put accounting in the ACCOUNTING phase and pass the falsifier above. It would
    mean accounting reads settlement state the tick's own echoes have not been applied to yet.
    """
    landed = []
    engine_clock.run_tick(
        world,
        action_callback=lambda w: _emit_with_deferred_apply(w, landed),
    )
    assert landed, "the deferred apply never ran — the boundary did not drain"
    assert landed == [ACCOUNTING], "the apply must run at the boundary, in ACCOUNTING phase"
    assert spy_accounting == [ACCOUNTING]


def test_the_action_phase_body_leaves_the_phase_alone(world):
    """mc_v18's real action callback must not touch the clock any more.

    Behavioural rather than a grep: if `next_tick()` or `accounting_boundary()` were
    re-added to the ACTION body, the phase observed on return would not be ACTION.
    """
    from engine import mc_v18

    observed = []

    def _callback(w):
        mc_v18._faction_actions_callback(w)
        observed.append(w.echo_scheduler._phase)

    engine_clock.run_tick(world, action_callback=_callback)

    assert observed == [ACTION], (
        f"the ACTION body left the scheduler in {observed} — the clock calls belong in "
        "engine_clock.run_tick, not in the phase body"
    )


def test_the_tick_closes_back_into_action(world):
    """`next_tick()` runs LAST, so the next tick starts clean and in ACTION."""
    engine_clock.run_tick(world, action_callback=lambda w: None)
    sched = world.echo_scheduler
    assert sched._phase == ACTION
    assert sched._emitted_this_tick == 0


def test_the_emission_counter_spans_both_phases(world):
    """§4.1: "Level B's cap applies tick-wide, both phases."

    Pre-move, `next_tick()` reset the counter before accounting, so accounting's emissions
    started a fresh budget every season and the tick-wide cap could be exceeded silently.
    Here the count is still rising when accounting begins.
    """
    seen = {}

    def _spy(w):
        seen['at_accounting'] = w.echo_scheduler._emitted_this_tick

    composition._CACHE['accounting'] = _spy
    try:
        engine_clock.run_tick(
            world,
            action_callback=lambda w: _emit_with_deferred_apply(w, []),
        )
    finally:
        composition._CACHE.pop('accounting', None)

    assert seen['at_accounting'] == 1, (
        "the tick's emission count was reset before accounting — the tick-wide cap is not "
        "tick-wide any more"
    )


# ── The flag-off path ─────────────────────────────────────────────────────────────────

def test_a_world_without_a_scheduler_still_ticks():
    """ECHO_TRANSPORT off: no `world.echo_scheduler` attribute at all, and that is legal."""
    w = create_world(seed=0)
    assert engine_clock.scheduler_of(w) is None

    before = w.season
    result = engine_clock.run_tick(w, action_callback=lambda _w: None)

    assert w.season == before + 1
    assert result.season == w.season


def test_run_tick_advances_the_season_exactly_once():
    """engine_clock is "the only module that may advance the season counter" (§O.1)."""
    w = create_world(seed=0)
    start = w.season
    for _ in range(3):
        engine_clock.run_tick(w)
    assert w.season == start + 3
