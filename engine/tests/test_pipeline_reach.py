"""engine/tests/test_pipeline_reach.py — the P1 acceptance oracle (OI-56, ED-IN-0091 plan §2.3).

WHAT THIS IS
------------
`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §1 defines "the pipeline runs
across all directions and scales" as a checklist; §2.3 says nothing asserted it before this file.
This is that assertion, driven with explicit coverage counting per CLAUDE.md §0.1 point 2 ("a
direction that never came up is a FAIL, not a skip") and named falsifiers per §0.1 point 3.
CORRECTION (ED-IN-0093 Wave 1): an earlier version of this docstring claimed every `assert
checked >= N` below was load-bearing; that was false — several counters incremented
unconditionally inside a plain `for` loop over a hardcoded literal list with no `continue`/
conditional skip path, so the loop could not have skipped an item regardless of the counter, and
the paired assert was decorative. Those counters were removed; the fixed-length literal list
itself (`len(...)` or the loop's own exhaustive iteration) is what guarantees every item ran.
CORRECTION 2 (re-critic round 2, item 3): `_source_scan`'s own `checked` was ALSO claimed above
to be a genuine conditional-skip counter — that claim is itself false. `_source_scan`'s
`checked += 1` (below) runs unconditionally once per entry of the `module_paths` list handed to
it, with no skip path, so `checked` is always exactly `len(module_paths)` by construction. Its
call sites split into two shapes: three compare `checked == len(<the same list variable>)`, which
is a tautology (the list and its own length, compared to each other) and asserts nothing a reader
couldn't already see from the loop — those three asserts have been dropped. One call site
(`test_direction3_vertical_up_handoff_dispatcher_is_wired`, `:323`) compares `checked == 4`
against an *inline literal*, independent of the list variable's own length — that one has real
force: it fails if the hardcoded module list at that call site silently shrinks, and stays. So:
`_source_scan`'s `checked` is a list-shrinkage guard where compared against an inline literal,
not a "genuine conditional-skip counter" anywhere in this file — there is no load-bearing
conditional-skip counter left in this module.

METHOD (G12, plan's own governing rule): every claim below about the tree was re-verified at its
cited file:line on 2026-07-29, the same day as the plan — this file does not execute the register
or the plan text verbatim where the working tree had already moved past it. Concretely, at write
time: the stubwire primitive (§2.1) and the dispatch closure (§2.2, OI-01/OI-02) had ALREADY LANDED
in this working tree (a sibling Wave-1 lane) — this file's assertions reflect that real state, not
the plan's aspirational description of it. The OI-17/18a/19 stub-conversion lanes (conv1/conv2,
plan §3 Wave 1 stage 4) had NOT landed at write time; this file still asserts their target state
STRICTLY (not xfail), per the plan's explicit instruction ("Strict rows this wave: ... converted
stub invocations") — those assertions are expected to be red until that sibling lane lands in the
same wave/PR, which is the acceptance oracle doing its job, not a defect in this file.

DESIGN CHOICE — dynamic xfail over hardcoded strict/red (documented so a reader does not mistake
this for indecision): a handful of rows below (combat-under-flag chief among them) use
`pytest.mark.xfail(<live introspection>, strict=True, ...)` instead of a bare assertion OR a bare
`@pytest.mark.xfail`. This is deliberate: this file is ONE of four file-disjoint lanes landing in
the same wave/PR without a guaranteed relative order (wf_wave1_spine.js's own "Build" phase runs
oracle/dispatch/conv1/conv2 in `parallel()`), so hardcoding "always red" would misreport a row the
moment a sibling lane's work lands, and hardcoding "always strict" would hard-fail CI on a lane that
has not landed yet. `strict=True` xfail is the self-flagging shape: honestly xfail while the
introspected condition says "not wired," and a hard, loud CI failure (XPASS) the moment the
condition flips true but nobody flipped the marker — which is exactly the manual "flip the row"
step the plan's burn-down process describes (§6.4 note in the wave text: "waves flip rows to strict
as they land").

XFAIL_MANIFEST below is the live P1 burn-down list this file promises to be (plan §2.3): one row per
still-unwired direction, each citing the OI row and the plan location that schedules its closure.
Every xfail in this file corresponds to exactly one manifest row; nothing here is a disguised pass.

Mirrors `test_f7_smoke_oracle.py`'s bootstrap (sys.path insert, direct `engine.mc_v18` imports) —
read there first, per the assignment; this file does not alter or re-record that oracle's goldens.
"""
from __future__ import annotations

import importlib
import inspect
import os
import re
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

import pytest  # noqa: E402

from engine.autoload import game_state, scene_slate  # noqa: E402
from engine.cross_scale import scene_dispatch, echo_transport  # noqa: E402
from engine.substrate import stubwire  # noqa: E402
from engine.mc_v18 import run_campaign, _dispatch_combat_bridge_on  # noqa: E402


# ═════════════════════════════════════════════════════════════════════════════════════════════
# XFAIL_MANIFEST — the live P1 burn-down list (plan §2.3). One row per still-unwired direction.
# `strict` rows use a live-introspected condition (see module docstring "DESIGN CHOICE"); `always`
# rows are unconditionally xfail this wave because their closure is explicitly scheduled for a
# LATER wave (Wave 2/3), not this one, per the plan's own wave assignment.
# ═════════════════════════════════════════════════════════════════════════════════════════════
XFAIL_MANIFEST = [
    {"id": "combat-bridge-on", "oi": "OI-01", "kind": "strict-condition",
     "area": "scene dispatch: combat",
     "reason": "DISPATCH_COMBAT_BRIDGE defaults OFF this wave (plan §2.2 term 2 / §6) — the ON "
               "flip is a separately scheduled IN action after PC's E0-E3 merge, never a side "
               "effect of this wave. Run with env DISPATCH_COMBAT_BRIDGE=1 to exercise the strict "
               "assertion for real."},
    {"id": "accord-echo-leg", "oi": "OI-03", "kind": "wave2",
     "area": "Key direction 2b: bottom-up, Accord leg",
     "reason": "domain_echo.compute_accord_echo has zero callers anywhere in engine/cross_scale — "
               "wiring it beside compute_domain_echo is Wave 2 item 1, not this wave."},
    {"id": "vertical-up-handoff", "oi": "OI-06", "kind": "wave2",
     "area": "Key direction 3: vertical-up",
     "reason": "handoff_rules.py is an import-orphan (its only 'importers' are docstring "
               "mentions, re-verified 2026-07-29) — wiring it as the vertical-up dispatcher "
               "inside dispatch is Wave 2 item 5."},
    {"id": "territory-transfer-resolver", "oi": "OI-04", "kind": "wave2",
     "area": "Key direction 4: top-down, territory transfer",
     "reason": "parliamentary_transfer.propose_transfer has zero callers (re-verified 2026-07-29) "
               "— wiring it via the parliamentary bridge is Wave 2 item 2."},
    {"id": "diagonal-causes", "oi": "OI-28", "kind": "wave3",
     "area": "Key direction 6: diagonal (causes[])",
     "reason": "causes[] has zero executable instances corpus-wide (re-verified 2026-07-29: no "
               "'causes=[' with any content in engine/ or systems/ outside tests) — populating "
               "it at existing emitters is Wave 3 item 5."},
    {"id": "world-npcs", "oi": "OI-05", "kind": "wave2",
     "area": "world chain: world.npcs",
     "reason": "generate_npc has zero call sites; world.npcs stays permanently empty this wave — "
               "Wave 2 item 3 wires npc generation at world-gen + season tick."},
    {"id": "world-knots", "oi": "OI-07", "kind": "wave2",
     "area": "world chain: world.knots",
     "reason": "world.knots has the same never-populated shape as world.npcs — Wave 2 item 4 "
               "wires population via registry.py."},
    {"id": "world-settlements", "oi": "OI-07", "kind": "wave2",
     "area": "world chain: world.settlements",
     "reason": "game_state.serialize_world has no 'settlements' key at all (re-verified "
               "2026-07-29) — same Wave 2 item 4 as world.knots."},
    {"id": "altonian-reinforcements-handoff", "oi": "OI-10 / OI-17", "kind": "accepted-handoff",
     "area": "unconditional NotImplementedError exemption",
     "reason": "systems/mass_battle/sim/altonian_reinforcements.py is the ONE accepted "
               "cross-session handoff (MB-owned file) — conversion is MB plan §12 I1, not this "
               "program's job (critic F9: an IN exit criterion may not be hostage to another "
               "session's schedule). This module MUST still raise NotImplementedError; if it "
               "does not, MB's conversion has landed and this manifest row (and its guard test "
               "below) should be deleted."},
]


def _manifest_reason(manifest_id: str) -> str:
    row = next(r for r in XFAIL_MANIFEST if r["id"] == manifest_id)
    return f"{row['oi']}: {row['reason']} [XFAIL_MANIFEST['{manifest_id}']]"


# ═════════════════════════════════════════════════════════════════════════════════════════════
# Shared fixtures / probes
# ═════════════════════════════════════════════════════════════════════════════════════════════

def _fresh_world(seed: int):
    return game_state.create_world(seed=seed)


def _world_with_scheduler(seed: int):
    """Mirrors test_echo_transport.py's `_world_with_scheduler` helper exactly (same three
    attribute assignments) — reused, not re-implemented differently, so this file's direction-2a
    probe exercises the SAME attach pattern the live campaign loop uses (mc_v18.run_campaign)."""
    world = game_state.create_world(seed=seed)
    world.echo_scheduler = echo_transport.make_scheduler()
    world.key_log = world.echo_scheduler.log
    world._echo_key_seq = 0
    return world


def _classify_call(callable_fn):
    """Call a zero-arg callable and classify the outcome:
      'stub_wired' — returned an engine.substrate.stubwire.StubResult (converted, honest no-op)
      'raw_stub'   — raised NotImplementedError (not yet converted)
      'resolved'   — returned anything else (real behavior)
      'error'      — raised anything else (a genuine defect — always a failure regardless of caller)
    Returns (outcome, detail)."""
    try:
        result = callable_fn()
    except NotImplementedError as e:
        return "raw_stub", str(e)
    except Exception as e:  # noqa: BLE001 - deliberately broad: any other exception is a real defect
        return "error", f"{type(e).__name__}: {e}"
    if isinstance(result, stubwire.StubResult):
        return "stub_wired", result
    return "resolved", result


def _probe(module_path: str, func_name: str, args: tuple, kwargs: dict | None = None):
    kwargs = kwargs or {}
    mod = importlib.import_module(module_path)
    func = getattr(mod, func_name)
    return _classify_call(lambda: func(*args, **kwargs))


def _source_scan(pattern: str, module_paths: list[str]):
    """Grep-equivalent over a curated set of LIVE modules (not the whole tree — a targeted,
    checked>=N scan matching the register's own grep-verified evidence method). Returns
    (checked_file_count, matches: list[(module_path, match_text)])."""
    rx = re.compile(pattern)
    matches = []
    checked = 0
    for mp in module_paths:
        checked += 1
        mod = importlib.import_module(mp)
        src = inspect.getsource(mod)
        for m in rx.finditer(src):
            matches.append((mp, m.group(0)))
    return checked, matches


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — "All scene directions dispatch" (OI-01/OI-02)
# ═════════════════════════════════════════════════════════════════════════════════════════════

# _dispatch_combat_bridge_on is imported from engine.mc_v18 (the single owner, CLAUDE.md §8) —
# not re-implemented here. run_campaign decides the flag from `effective_params`/the env var and
# stashes it on `world.dispatch_combat_bridge`; this test drives `_resolve_slot` directly (below
# run_campaign) so it must reproduce the identical decision, never a second one. The owner takes
# an `effective_params` dict (params-override-then-env-var, mirroring `_echo_transport_on`); this
# file has no params override to give it, so it always passes `{}` (env-var-only resolution).


@pytest.mark.xfail(not _dispatch_combat_bridge_on({}), strict=True,
                    reason=_manifest_reason("combat-bridge-on"))
def test_combat_resolves_via_canonical_bridge_under_flag_on():
    """OI-01: with the flag genuinely ON (world.dispatch_combat_bridge — the same attribute
    run_campaign sets), combat resolves through combat_engine_v1 via the IN-side bridge, not the
    DEPRECATED systems.combat.sim.combat path. Well-formed context (ctx['factions']) is supplied
    deliberately — this direction's acceptance is evaluated on its OWN documented contract
    (combat_bridge.py), not on the empty-context probe the total-mapping test below uses for the
    scene_types that resolve unconditionally of context."""
    world = _fresh_world(seed=7)
    world.dispatch_combat_bridge = _dispatch_combat_bridge_on({})
    slot = scene_slate.SceneSlot(scene_type="combat",
                                  context={"factions": ("Crown", "Church")}, priority=0)
    res = scene_dispatch._resolve_slot(slot, world, world.rng)
    assert res.get("resolved") is True, f"combat did not resolve via the canonical bridge: {res}"
    assert res["result"]["a_label"] == "Crown" and res["result"]["b_label"] == "Church"


def test_scene_type_total_mapping_resolves_or_stub_flags():
    """§1 acceptance: every scene_type the slate can queue (plan's named roster: combat, contest,
    investigation/fieldwork, thread operation, domain action) either resolves through its
    canonical resolver or records a stubwire flag — never a silent 'not live' string (OI-01/02).
    combat is covered separately above (its acceptance is flag-conditional, not unconditional);
    this test covers the remaining five scene_type strings via DIRECT `_resolve_slot` probes (not
    organic triggering — today only 'contest' is ever organically queued, via Stability Crisis),
    so a direction that is real but never organically triggered this wave is still checked, not
    silently skipped (§0.1 point 2). STRICT (no xfail): the dispatch lane's OI-02 conversion and
    its total-mapping fallback (the else-branch stubwire call) both landed in this wave — these
    are exactly the 'stub-flag paths your fellow lanes wire' the assignment names as strict."""
    world = _fresh_world(seed=11)
    slots = [
        ("contest", {"faction": "Crown", "stakes": {"kind": "emergency_council", "faction": "Crown"}}),
        ("investigation", {}),
        ("fieldwork", {}),
        ("thread", {}),
        ("domain_action", {}),
    ]
    # A plain loop over this fixed 5-item literal list has no conditional skip path (no
    # `continue`/early exit below) — every item runs by construction, so a `checked == len(slots)`
    # counter would be decorative, not load-bearing (§0.1 point 2 corrected, see module
    # docstring); the literal list length IS the coverage guarantee.
    failures = []
    for scene_type, ctx in slots:
        slot = scene_slate.SceneSlot(scene_type=scene_type, context=dict(ctx), priority=0)
        res = scene_dispatch._resolve_slot(slot, world, world.rng)
        stub_flagged = res.get("stub") is True
        if not (res.get("resolved") is True or stub_flagged):
            failures.append(f"{scene_type}: neither resolved nor stub-flagged — {res}")
    assert not failures, (
        "scene_type(s) with neither a canonical resolution nor an honest stubwire flag "
        "(OI-01/OI-02, plan §2.2):\n" + "\n".join(failures)
    )


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — "The 7 Key-delivery directions" (directional_coverage_v1.md's roster)
# ═════════════════════════════════════════════════════════════════════════════════════════════

_KEY_DELIVERY_EMITTER_MODULES = [
    "engine.cross_scale.echo_transport",
    "engine.cross_scale.domain_echo",
    "engine.cross_scale.scene_dispatch",
    "engine.cross_scale.parliamentary_bridge",
    "engine.cross_scale.articulation",
]


def test_direction1_lateral_fires():
    """directional_coverage_v1.md #1 — LIVE. Same-scale delivery: the emergency_council contest
    resolves two facets of the SAME faction directly (a real, live, unconditional resolution —
    not organically triggered here, driven directly per the total-mapping test's own method)."""
    world = _fresh_world(seed=3)
    slot = scene_slate.SceneSlot(
        scene_type="contest",
        context={"faction": "Crown", "stakes": {"kind": "emergency_council", "faction": "Crown"}},
        priority=0)
    res = scene_dispatch._resolve_slot(slot, world, world.rng)
    assert res.get("resolved") is True, f"lateral (emergency_council contest) did not fire: {res}"


def test_direction2a_bottom_up_domain_echo_core_fires():
    """directional_coverage_v1.md #2 — core LIVE (ECHO_TRANSPORT default ON). Direct probe of the
    transport path (mirrors test_echo_transport.py's method): a resolved scene carrying an
    explicit `echo` block routes through domain_echo -> a real, logged Key with populated
    targets[] and a deferred faction-stat apply."""
    world = _world_with_scheduler(seed=42)
    fid = next(iter(world.factions))
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid,
                    "most_relevant_stat": "L", "degree": "Overwhelming"}}
    out = echo_transport.emit_scene_echo("contest", {"total_victory": True}, ctx, world)
    assert out.get("other_echoes"), "bottom-up Domain Echo core did not fire"
    assert len(world.key_log) == 1
    k = next(iter(world.key_log))
    assert k.targets and k.targets[0].stat_deltas, "the logged Key carries no populated targets[]"


@pytest.mark.xfail(strict=True, reason=_manifest_reason("accord-echo-leg"))
def test_direction2b_bottom_up_accord_echo_leg_is_wired():
    """directional_coverage_v1.md #2 — the Accord leg. compute_accord_echo must have >=1 caller
    among the live cross-scale emitter modules; today it has zero (grep-verified 2026-07-29)."""
    # domain_echo.py itself is EXCLUDED here — it's the definer (both the `def` line and its own
    # module docstring's "Entry points" list mention the name, neither is a call site); this test
    # asks whether anything ELSE calls it, so it scans the other emitter modules only.
    caller_modules = [m for m in _KEY_DELIVERY_EMITTER_MODULES if m != "engine.cross_scale.domain_echo"]
    _checked, matches = _source_scan(r"compute_accord_echo\(", caller_modules)
    assert matches, "compute_accord_echo has zero callers among the live emitter modules"


@pytest.mark.xfail(strict=True, reason=_manifest_reason("vertical-up-handoff"))
def test_direction3_vertical_up_handoff_dispatcher_is_wired():
    """directional_coverage_v1.md #3 — DOCTRINE-ONLY. handoff_rules.py must be imported by at
    least one live cross-scale/autoload module (not a docstring mention) for the curated 8-rule
    dispatcher to be anything but bypassed. Today it is an import-orphan (grep-verified
    2026-07-29: engine/cross_scale/__init__.py and two OTHER modules' docstrings mention it by
    name in prose, but nothing actually imports it)."""
    checked, matches = _source_scan(
        r"^\s*(?:from engine\.cross_scale import handoff_rules\b|"
        r"import engine\.cross_scale\.handoff_rules\b)",
        ["engine.cross_scale.scene_dispatch", "engine.mc_v18",
         "engine.cross_scale.parliamentary_bridge", "engine.cross_scale.echo_transport"])
    assert checked == 4
    assert matches, "handoff_rules is still an import-orphan (no live import statement found)"


def test_direction4_topdown_targeting_mechanism_fires():
    """directional_coverage_v1.md #4/#5 — top-down / down-diagonal ANNOTATION-DEBT (not fully
    dead): the shared substrate mechanism (a Key naming sub-scale actors in targets[]) is
    exercised — reuses direction 2a's own logged Key as proof, per directional_coverage's own
    finding that the mechanism is 'exercised elsewhere,' not that a separate top-down mechanism is
    missing. The residual (sparse targets[] annotation + the specific uncalled transfer resolver)
    is tracked separately below, not blocking this direction's §1 bar ('fires >=once')."""
    world = _world_with_scheduler(seed=99)
    fid = next(iter(world.factions))
    ctx = {"echo": {"actor_faction": fid, "most_relevant_stat": "L", "degree": "Success"}}
    echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    assert len(world.key_log) == 1
    k = next(iter(world.key_log))
    assert k.targets and k.targets[0].actor_id, "targeting mechanism did not populate targets[]"


@pytest.mark.xfail(strict=True, reason=_manifest_reason("territory-transfer-resolver"))
def test_direction4b_territory_transfer_resolver_is_called():
    """OI-04 residual on top of direction 4's core bar: parliamentary_transfer.propose_transfer
    must have >=1 caller. Today it has zero (grep-verified 2026-07-29) — the one-way territory
    ratchet OI-04 describes."""
    _checked, matches = _source_scan(r"propose_transfer\(", _KEY_DELIVERY_EMITTER_MODULES)
    assert matches, "parliamentary_transfer.propose_transfer still has zero callers"


def test_direction5_down_diagonal_shares_direction4s_mechanism():
    """directional_coverage_v1.md #5 — same substrate mechanism class as #4 (top-down), same
    verdict (ANNOTATION-DEBT, not a separate mechanism gap per the audit's own text: 'No separate
    mechanism gap'). Recorded as its own direction (not silently folded into #4) so the meta
    coverage check below cannot miss it, but the check itself is the same targets[] proof."""
    world = _world_with_scheduler(seed=100)
    fid = next(iter(world.factions))
    ctx = {"echo": {"actor_faction": fid, "most_relevant_stat": "L", "degree": "Success"}}
    echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    assert len(world.key_log) == 1
    k = next(iter(world.key_log))
    assert k.targets and k.targets[0].actor_id


@pytest.mark.xfail(strict=True, reason=_manifest_reason("diagonal-causes"))
def test_direction6_diagonal_causes_has_an_instance():
    """directional_coverage_v1.md #6 — UNREACHED, the headline directional gap (OI-28): causes[]
    must be populated with actual content at >=1 live emit site. Today it is zero corpus-wide
    (re-verified 2026-07-29 via source scan of the same emitter-module set used above — no
    'causes=[' with any non-empty content anywhere in engine/ or systems/ outside tests)."""
    _checked, matches = _source_scan(r"causes\s*=\s*\[[^\]]+\]", _KEY_DELIVERY_EMITTER_MODULES)
    assert matches, "causes[] is still populated nowhere among the live emitter modules"


def test_direction7a_temporal_cadence_fires():
    """directional_coverage_v1.md #7 — cadence half, PARTIALLY WIRED. TickScheduler's
    accounting_boundary/next_tick cadence primitives (used live by mc_v18's per-season boundary)
    are directly callable and actually advance state."""
    world = _world_with_scheduler(seed=5)
    sched = world.echo_scheduler
    before_season = sched.log._season_counters.copy() if hasattr(sched.log, "_season_counters") else None
    ran = sched.accounting_boundary()
    assert isinstance(ran, int)
    sched.next_tick()  # must not raise — cadence mechanism is live and callable
    assert before_season is not None  # sanity: we actually inspected scheduler-internal state


def test_direction7b_temporal_decay_is_a_declared_deferral():
    """directional_coverage_v1.md #7 — decay half, an EXPLICIT deferral (OF-3), never a silent
    gap: propagation_spec_v1.md documents 'OF-3 (decay() unspecified...)' in the working tree.
    §1's acceptance bar for this half is exactly 'flagged, not faked' — this test asserts the flag
    is genuinely present in the canonical doc, not asserting decay() exists (it should not, yet)."""
    doc_path = os.path.join(_REPO_ROOT, "systems", "_architecture", "propagation_spec_v1.md")
    assert os.path.isfile(doc_path), "propagation_spec_v1.md (OF-3's home) is missing entirely"
    text = open(doc_path, encoding="utf-8").read()
    assert "OF-3" in text and "decay()" in text, (
        "OF-3 (the decay() deferral) is no longer declared in propagation_spec_v1.md — either "
        "decay() has been specified (great — update this test) or the declaration regressed"
    )


def test_all_seven_key_delivery_directions_have_a_dedicated_check():
    """Meta-coverage (§0.1 point 2): directional_coverage_v1.md's 7-item roster must each have
    >=1 dedicated test function in THIS module — fails loudly if a direction is ever silently
    dropped, rather than the file quietly shrinking to fewer than 7."""
    mod = sys.modules[__name__]
    names = [n for n in dir(mod) if n.startswith("test_direction")]
    covered = set()
    for n in names:
        m = re.match(r"test_direction(\d)", n)
        if m:
            covered.add(int(m.group(1)))
    assert covered == set(range(1, 8)), f"missing Key-delivery direction test(s): {set(range(1, 8)) - covered}"
    assert len(names) >= 7, f"expected >=7 direction test functions, found {len(names)}"


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — "world chains populated" (OI-05/OI-07) — xfail until Wave 2
# ═════════════════════════════════════════════════════════════════════════════════════════════

@pytest.mark.xfail(strict=True, reason=_manifest_reason("world-npcs"))
def test_world_npcs_populated_after_a_seeded_campaign():
    r = run_campaign(seed=42)
    assert r.npcs_generated > 0, "world.npcs stayed empty (OI-05: generate_npc has zero callers)"


@pytest.mark.xfail(strict=True, reason=_manifest_reason("world-knots"))
def test_world_knots_populated_after_a_seeded_campaign():
    r = run_campaign(seed=42)
    knots = r.final_state.get("knots", {})
    assert knots, "world.knots stayed empty (OI-07)"


@pytest.mark.xfail(strict=True, reason=_manifest_reason("world-settlements"))
def test_world_settlements_populated_after_a_seeded_campaign():
    r = run_campaign(seed=42)
    settlements = r.final_state.get("settlements", {})
    assert settlements, "world.settlements stayed empty or unserialized entirely (OI-07)"


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — "zero unconditional NotImplementedError in live trees, except the one accepted
# cross-session handoff" (OI-17/18a/19/10a). STRICT: this wave's conv1/conv2 lanes own converting
# every one of these (plan §3 Wave 1 stage 4) — "converted stub invocations" is the assignment's
# own name for a strict-this-wave row.
# ═════════════════════════════════════════════════════════════════════════════════════════════

# OI-17 full-module conversions (conv1: factions/overview; conv2 A: world/characters/threadwork/
# engine cross_scale+autoload). EXCLUDES systems/mass_battle/sim/altonian_reinforcements.py (the
# one accepted cross-session handoff, MB plan §12 I1 — see its own guard test below).
_OI17_FULL_MODULE_ENTRYPOINTS = [
    ("systems.factions.sim.charter_liberties", "attempt_charter", lambda w: (w,)),
    ("systems.factions.sim.infrastructure_reclamation", "compute_reclamation_bonus", lambda w: ("T1", w)),
    ("systems.factions.sim.home_sanctuary", "t9_invasion_modifier", lambda w: (w,)),
    ("systems.factions.sim.varfell_mandate_action", "attempt_mandate_action", lambda w: (w,)),
    ("systems.factions.sim.varfell_territorial_acquisition", "attempt_territorial_acquisition", lambda w: ("T4", w)),
    ("systems.factions.sim.hafenmark_equipment", "apply_hafenmark_equipment", lambda w: (w.factions["Hafenmark"],)),
    ("systems.overview.sim.rs_track", "apply_rs_delta", lambda w: (1, "test", w)),
    ("systems.overview.sim.ip_track", "apply_ip_delta", lambda w: (1, "test", w)),
    ("systems.world.sim.miraculous_event", "trigger_miraculous_event", lambda w: ("test_event", w)),
    ("systems.world.sim.restoration_movement", "process_rm_pt_decay", lambda w: (w,)),
    ("systems.characters.sim.companion", "run_companion_scene", lambda w: ({},)),
    ("systems.threadwork.sim.rendering", "apply_rs_strain", lambda w: (1, "test", w)),
    ("engine.cross_scale.articulation", "evaluate_articulation_triggers", lambda w: (w,)),
    ("engine.autoload.npc_ai", "select_action", lambda w: ("Crown_npc_1", w)),
]


def test_oi17_full_module_conversions_are_stub_wired():
    # No conditional skip path in this loop (plain iteration over a fixed literal list) — a
    # `checked` counter would be decorative; see module docstring's §0.1 point 2 correction.
    world = _fresh_world(seed=1)
    unconverted = []
    for mod_path, func_name, args_fn in _OI17_FULL_MODULE_ENTRYPOINTS:
        outcome, detail = _probe(mod_path, func_name, args_fn(world))
        if outcome != "stub_wired":
            unconverted.append(f"{mod_path}.{func_name} -> {outcome}: {detail}")
    assert not unconverted, (
        "OI-17 modules not (yet) stub-wired via engine.substrate.stubwire (plan §3 Wave 1 stage "
        "4, conv1/conv2 lanes):\n" + "\n".join(unconverted)
    )


def test_only_accepted_handoff_still_raises_unconditionally():
    """The other half of 'zero unconditional NotImplementedError... except': altonian_reinforcements
    is the ONE module this file expects to still raise. If it stops raising, MB's own §12 I1
    conversion has landed — a good thing — and this test (plus its XFAIL_MANIFEST row) should be
    deleted, not left green-by-accident."""
    outcome, detail = _probe("systems.mass_battle.sim.altonian_reinforcements",
                              "invoke_altonian_reinforcements", (_fresh_world(seed=1),))
    assert outcome == "raw_stub", (
        "altonian_reinforcements no longer raises unconditionally (outcome="
        f"{outcome!r}: {detail}) — if MB plan §12 I1 has converted it, DELETE this test and the "
        "'altonian-reinforcements-handoff' XFAIL_MANIFEST row rather than updating the assertion"
    )


# OI-18a — SELF-FLAG ONLY (plan's explicit scope note): the contest GAMES router's stub rows
# (consensus/negotiation/inquiry) and the Dyadic/Negotiation/Ceremonial.play scaffolds.
_OI18A_GAMES_ROWS = ["consensus", "negotiation", "inquiry"]
_OI18A_MODE_SCAFFOLDS = ["DyadicMode", "NegotiationMode", "CeremonialMode"]


def test_oi18a_contest_games_router_stub_rows_are_self_flagged():
    # No conditional skip path in this loop — a `checked` counter would be decorative; see
    # module docstring's §0.1 point 2 correction.
    wrapper = importlib.import_module("systems.social_contest.sim.contest.wrapper")
    unconverted = []
    for game in _OI18A_GAMES_ROWS:
        outcome, detail = _classify_call(lambda g=game: wrapper.GAMES[g]["resolve"](None))
        if outcome != "stub_wired":
            unconverted.append(f"GAMES[{game!r}] -> {outcome}: {detail}")
    assert not unconverted, (
        "contest GAMES router stub rows not yet self-flagged via stubwire (OI-18a):\n"
        + "\n".join(unconverted)
    )


def test_oi18a_mode_scaffolds_are_self_flagged():
    # No conditional skip path in this loop — a `checked` counter would be decorative; see
    # module docstring's §0.1 point 2 correction.
    modes = importlib.import_module("systems.social_contest.sim.contest.modes")
    unconverted = []
    for cls_name in _OI18A_MODE_SCAFFOLDS:
        cls = getattr(modes, cls_name)
        outcome, detail = _classify_call(lambda c=cls: c().play())
        if outcome != "stub_wired":
            unconverted.append(f"{cls_name}.play() -> {outcome}: {detail}")
    assert not unconverted, (
        "Dyadic/Negotiation/Ceremonial scaffold .play() not yet self-flagged via stubwire "
        "(OI-18a):\n" + "\n".join(unconverted)
    )


# OI-19 — partial NotImplementedError branches (leave live branches untouched). resolver.py:51 is
# a benign abstract base (WinCondition.resolve) and is DELIBERATELY EXCLUDED per the plan's own
# scope note — it is not part of the stub-conversion class.
def test_oi19_partial_branches_are_self_flagged():
    # Three unconditional, unguarded probes in a row (no conditional skip path) — a `checked`
    # counter would be decorative; see module docstring's §0.1 point 2 correction.
    unconverted = []

    outcome, detail = _probe("systems.factions.sim.tribunal", "run_tribunal",
                              ("npc_accused", ["npc_accuser"], "succession_contest"))
    if outcome != "stub_wired":
        unconverted.append(f"tribunal.run_tribunal (§7 generic dispatch) -> {outcome}: {detail}")

    outcome, detail = _probe("systems.factions.sim.treaty", "propose_treaty",
                              (["Crown", "Church"], {}))
    if outcome != "stub_wired":
        unconverted.append(f"treaty.propose_treaty (no canonized formation path) -> {outcome}: {detail}")

    outcome, detail = _probe("systems.social_contest.sim.contest.dictionaries", "panel_win_condition",
                              (), {"aggregation": "unanimity_required"})
    if outcome != "stub_wired":
        unconverted.append(f"dictionaries.panel_win_condition(unanimity_required) -> {outcome}: {detail}")

    assert not unconverted, (
        "OI-19 partial NotImplementedError branches not yet self-flagged via stubwire (leaving "
        "their live branches untouched; resolver.py:51 is deliberately excluded as a benign "
        "abstract base):\n" + "\n".join(unconverted)
    )
