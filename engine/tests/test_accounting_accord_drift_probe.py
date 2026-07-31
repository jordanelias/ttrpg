"""
engine/tests/test_accounting_accord_drift_probe.py — province-Accord drift PROBE oracle
(W3 Handoff item 2, ED-IN-0091 plan §3 Wave 3, 2026-07-29).

`systems.overview.sim.accounting.run_accounting` gained a REPORT-ONLY step comparing, per
province, `registry.province_accord` (the settlement-Order aggregate) against the live
`Territory.accord` field (converted to the same canonical-index space via
`game_state.canonical_accord`) and recording any divergence into additive campaign telemetry
(`world.accord_drift_probe_hits`, mirroring `engine.substrate.stubwire`'s `stub_hits` pattern).
It NEVER writes either compared value — the write-model reconciliation itself is the SE lane's
own OI-37 workstream, out of scope here (see `_probe_province_accord_drift`'s docstring).

Falsifiers pinned here:
  1. A forced settlement.order/Territory.accord divergence surfaces a nonzero probe value
     (assert checked >= 1, CLAUDE.md §0.1 point 2) — the probe genuinely detects, not just exists.
  2. No divergence anywhere leaves the probe absent/zero — not a fabricated always-on counter.
  3. The probe writes NEITHER `Settlement.order` NOR `Territory.accord` — byte-exact before/after,
     both via the isolated probe function directly and via the full `run_accounting` pass.
  4. No settlements / no territories -> the probe stays absent (0), never raises.
  5. `engine.mc_v18.run_campaign`'s `CampaignResult.accord_drift_probe_hits` surfaces the same
     per-campaign value `world.accord_drift_probe_hits` carries — the field actually reaches
     campaign telemetry, not just `world`.
"""
from engine.autoload import game_state
from engine.mc_v18 import run_campaign
from systems.overview.sim import accounting
from systems.settlements.sim import registry as settlement_registry


def _first_province_with_members(world):
    for tid, territory in world.territories.items():
        members = settlement_registry.province_members(tid, world)
        if members:
            return tid, territory, members
    return None, None, None


# ── 1. Genuine detection: a forced divergence surfaces a nonzero probe value ─────────────────

def test_a_forced_settlement_order_divergence_surfaces_a_nonzero_drift_probe_value():
    world = game_state.create_world(seed=42)
    tid, territory, members = _first_province_with_members(world)
    assert tid is not None, "fixture needs >=1 province with >=1 settlement"

    target_canonical = game_state.canonical_accord(territory.accord)
    # Force EVERY member to the same value, deliberately at the opposite end of the 0-5 range
    # from the territory's own canonical bucket -- floor(mean) of N copies of V is exactly V, so
    # this is a controlled, guaranteed-diverging fixture, not an incidental one.
    diverging_order = 0 if target_canonical >= 3 else 5
    checked = 0
    for m in members:
        m.order = diverging_order
        checked += 1
    assert checked >= 1
    assert settlement_registry.province_accord(tid, world) != target_canonical, (
        "fixture assumption: the forced order must genuinely diverge from the territory's "
        "canonical Accord bucket")

    assert not hasattr(world, "accord_drift_probe_hits") or world.accord_drift_probe_hits == 0
    accounting.run_accounting(world)
    assert getattr(world, "accord_drift_probe_hits", 0) >= 1, (
        "a genuine settlement/territory Accord divergence must surface a nonzero probe value")


# ── 2. Honesty: no divergence anywhere -> the probe stays absent/zero ────────────────────────

def test_no_divergence_anywhere_leaves_the_probe_absent_or_zero():
    world = game_state.create_world(seed=42)
    checked = 0
    for tid, territory in world.territories.items():
        members = settlement_registry.province_members(tid, world)
        if not members:
            continue
        target = game_state.canonical_accord(territory.accord)
        for m in members:
            m.order = target  # mean of N copies of `target` floors to exactly `target`
        checked += 1
    assert checked >= 1, "fixture needs >=1 province with settlements to make this claim mean anything"

    accounting.run_accounting(world)
    assert getattr(world, "accord_drift_probe_hits", 0) == 0, (
        "the probe must not fabricate a divergence when every province genuinely agrees")


# ── 3. Never writes either compared value ─────────────────────────────────────────────────────

def test_probe_function_writes_neither_settlement_order_nor_territory_accord():
    world = game_state.create_world(seed=42)
    orders_before = {sid: s.order for sid, s in world.settlements.items()}
    accords_before = {tid: t.accord for tid, t in world.territories.items()}

    accounting._probe_province_accord_drift(world)

    checked = 0
    for sid, s in world.settlements.items():
        assert s.order == orders_before[sid], f"settlement {sid}.order moved: probe must not write"
        checked += 1
    for tid, t in world.territories.items():
        assert t.accord == accords_before[tid], f"territory {tid}.accord moved: probe must not write"
        checked += 1
    assert checked >= 2


def test_full_run_accounting_pass_also_writes_neither_value():
    """The probe runs as step 6 of run_accounting -- confirm the composed pass (CI/MS/insurgency/
    NPE steps included) still leaves both compared fields untouched, not just the isolated
    function above (a regression in call ORDER could otherwise let an earlier step move one of
    these fields and mask a probe defect)."""
    world = game_state.create_world(seed=7)
    orders_before = {sid: s.order for sid, s in world.settlements.items()}
    accords_before = {tid: t.accord for tid, t in world.territories.items()}

    accounting.run_accounting(world)

    checked = 0
    for sid, s in world.settlements.items():
        assert s.order == orders_before[sid], f"settlement {sid}.order moved during run_accounting"
        checked += 1
    for tid, t in world.territories.items():
        assert t.accord == accords_before[tid], f"territory {tid}.accord moved during run_accounting"
        checked += 1
    assert checked >= 2


# ── 4. Edge cases: no settlements / no territories -> stays absent, never raises ─────────────

def test_no_settlements_leaves_the_probe_absent():
    world = game_state.create_world(seed=42)
    world.settlements = {}
    accounting._probe_province_accord_drift(world)  # must not raise
    assert getattr(world, "accord_drift_probe_hits", 0) == 0


def test_no_territories_leaves_the_probe_absent():
    world = game_state.create_world(seed=42)
    world.territories = {}
    accounting._probe_province_accord_drift(world)  # must not raise
    assert getattr(world, "accord_drift_probe_hits", 0) == 0


# ── 5. The value reaches CampaignResult, not just `world` ────────────────────────────────────

def test_campaign_result_surfaces_the_same_drift_probe_value_world_carries():
    """Drives a REAL run_campaign() (not a hand-built world) far enough for run_accounting to
    fire at least once, and confirms CampaignResult.accord_drift_probe_hits reaches campaign
    telemetry rather than being silently dropped at the World/CampaignResult boundary."""
    result = run_campaign(seed=42, max_seasons=2)
    assert isinstance(result.accord_drift_probe_hits, int)
    # CORRECTED 2026-07-30 (ED-IN-0098), found by tools/ci_vacuous_assertion_check.py [S1].
    # The previous line was `assert ... >= 0`, whose own comment ("never negative -- an
    # additive-only counter") conceded it could not fail — so this test's stated purpose,
    # "confirms the value reaches CampaignResult rather than being silently dropped at the
    # World/CampaignResult boundary", was asserted by the isinstance() line alone and the
    # boundary itself was never checked. A silent drop would leave BOTH sides at 0 and pass.
    # What actually falsifies the claim is AGREEMENT ACROSS the boundary, so assert that.
    # MEASURED: CampaignResult exposes no `.world` handle (checked — hasattr is False), so a
    # cross-boundary equality assertion would be permanently dead code. The strongest claim that
    # can actually FAIL here is that the counter arrived non-zero: the docstring's own premise is
    # that accounting fires "at least once" over 2 seasons, so 0 means either it never ran or the
    # value was dropped between World and CampaignResult — the exact defect this test guards.
    # Live value at seed=42/max_seasons=2 is 461, so the margin is not marginal.
    assert result.accord_drift_probe_hits > 0, (
        'accounting was expected to fire at least once in 2 seasons, so 0 drift-probe hits means '
        'the probe never incremented or never reached CampaignResult')
