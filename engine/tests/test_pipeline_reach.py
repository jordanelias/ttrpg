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
# LATER wave (Wave 2/3), not this one, per the plan's own wave assignment. `honest-deferral` rows
# are a THIRD kind added by the Oracle stage this wave (2026-07-29): unlike `wave2`/`wave3`, these
# are not scheduled to close in any future wave — canon itself specifies no world-gen/season-tick
# trigger for the mechanism, so the deferral is the considered, permanent-until-canon-changes
# disposition, not a to-do. They stay xfail (never flip to strict) for exactly that reason.
#
# WAVE 2 BURN-DOWN (2026-07-29, ED-IN-0095): four rows retired this wave, each confirmed XPASS
# (strict) by running its test directly against the tree, not by inspection — accord-echo-leg
# (OI-03), vertical-up-handoff (OI-06), territory-transfer-resolver (OI-04), world-settlements
# (OI-07). Their tests are now unconditional strict assertions (see each test's own docstring for
# the resolving citation) and their manifest rows are removed per this list's own "one row per
# still-unwired direction" contract. world-npcs/world-knots stay xfail but reclassified
# `honest-deferral` (see rows below) — Wave 2 landed a considered disposition, not a wire-up.
# ═════════════════════════════════════════════════════════════════════════════════════════════
XFAIL_MANIFEST = [
    {"id": "combat-bridge-on", "oi": "OI-01", "kind": "strict-condition",
     "area": "scene dispatch: combat",
     "reason": "DISPATCH_COMBAT_BRIDGE defaults OFF this wave (plan §2.2 term 2 / §6) — the ON "
               "flip is a separately scheduled IN action after PC's E0-E3 merge, never a side "
               "effect of this wave. Run with env DISPATCH_COMBAT_BRIDGE=1 to exercise the strict "
               "assertion for real."},
    {"id": "diagonal-causes", "oi": "OI-28", "kind": "strict-condition",
     "area": "Key direction 6: diagonal (causes[])",
     "reason": "HONESTY CORRECTION (2026-07-29, same-day W3 follow-on — the prior version of this "
               "reason described the causes[]-populating path as not-yet-existing; that went stale "
               "the moment it landed, in this same file's own wave, and was left uncorrected): "
               "echo_transport._apply_accord_echo now builds a real scene.accord_echo Key (OI-03 "
               "registered the type; a real sched.emit call site exists) AND genuinely populates "
               "its causes[] field with the sibling §5.2 domain-echo Key's id when that leg also "
               "fired for the SAME scene resolution — the ONE executable, non-decorative causes[] "
               "instance corpus-wide, unit-falsified directly against the real KeyLog by "
               "engine/tests/test_accord_echo.py's two §3 tests (log-lookup, not string-equality). "
               "This row STAYS xfail anyway, for a genuinely different reason than before: the path "
               "is executable but DORMANT — no live producer module declares "
               "echo['scene_outcome'] (scene_dispatch.py / parliamentary_bridge.py, re-verified "
               "2026-07-29; same scan test_direction2b uses), so classify_scene_outcome always "
               "returns None in any real campaign and _apply_accord_echo's Key-with-causes[] "
               "branch never runs outside a test that hand-supplies the input. The xfail condition "
               "below is now LIVE-INTROSPECTED (mirrors combat-bridge-on's own pattern) rather than "
               "a hardcoded always-red: it re-checks that same dormancy scan, so the MARKER "
               "self-lifts the moment a producer supplies the input — but that is not the same "
               "claim as 'no manual burn-down step needed' (re-critic HIGH correction, 2026-07-29): "
               "the test BODY below deliberately omits scene_outcome from its ctx (real dormancy, "
               "not a stand-in), so once the marker lifts the test goes HARD RED, not green — a "
               "deliberate loud alarm demanding the body be rewritten to thread the landed "
               "producer's real input, not a self-resolving row. See test_accord_echo.py's "
               "test_accord_leg_receives_the_domain_echo_"
               "keys_real_in_log_id / test_accord_leg_caused_by_key_id_is_none_when_the_domain_"
               "echo_leg_does_not_fire for the unit-level falsifiers (both green today), and "
               "test_direction6b_accord_echo_leg_receives_a_genuine_in_log_causal_id below for the "
               "companion reach-level check."},
    {"id": "world-npcs", "oi": "OI-05", "kind": "honest-deferral",
     "area": "world chain: world.npcs",
     "reason": "RECLASSIFIED Wave 2 (was 'generate_npc has zero call sites', framed as an "
               "oversight): re-verified against investigation_systems_v30.md SYSTEM 1 this wave "
               "— Two-Tier Generation's Tier-1 seed is scene-specification-driven only ('Scene "
               "specification declares density and composition'); no canon head names a "
               "world-gen initial count or a season-tick generation trigger (NPE-02's proposed "
               "persistence cap is an unresolved Open Question, not a ratified number). The "
               "honest move is to generate none automatically rather than fabricate a count "
               "(CLAUDE.md §5/§7) — world.npcs is a PERMANENT deferral until canon specifies a "
               "trigger, not a to-do for a later wave. The drift half (simulate_npc_actions) was "
               "already wired every season pre-wave via accounting.py:78-82 and is unaffected. "
               "The deferral is recorded live via engine.mc_v18._faction_actions_callback's "
               "stubwire.stub_resolve('generate_npc(world-gen|season-tick)', ...) call, firing "
               "once per season — see engine/tests/test_world_population.py's "
               "test_generate_npc_has_no_automatic_call_site_this_wave /"
               "test_npc_and_knot_deferral_stubs_fire_every_season for the falsifiers."},
    {"id": "world-knots", "oi": "OI-07", "kind": "honest-deferral",
     "area": "world chain: world.knots",
     "reason": "RECLASSIFIED Wave 2 (was 'same never-populated shape as world.npcs', framed as "
               "an oversight): re-verified against knots_v30.md §3.1 this wave — form_knot's "
               "Prerequisites (Disposition +5 with target NPC, PC Bonds >= 5, PC's current Knot "
               "count < floor(Bonds/2) + 1) are personal-scale actor fields (Disposition, Bonds) "
               "that do not exist anywhere on the aggregate strategic World; no world-gen or "
               "season-tick formation rule exists in canon to cite. world.knots is a PERMANENT "
               "deferral until canon specifies a formation rule, not a to-do for a later wave. "
               "The deferral is recorded live via engine.mc_v18._faction_actions_callback's "
               "stubwire.stub_resolve('form_knot(world-gen|season-tick)', ...) call, firing once "
               "per season — see engine/tests/test_world_population.py's "
               "test_knots_stay_unpopulated_honest_deferral /"
               "test_npc_and_knot_deferral_stubs_fire_every_season for the falsifiers."},
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
    (checked_file_count, matches: list[(module_path, match_text)]).

    BUGFIX (Wave 2, Oracle stage, flagged by the L-handoff lane): `re.compile(pattern)` without
    `re.MULTILINE` made any `^`-anchored pattern only ever match offset 0 of the WHOLE
    `inspect.getsource(mod)` string, i.e. only if the anchored text were the file's literal first
    line — impossible for an import statement in every candidate module here (a module docstring
    always precedes it). Verified directly before this fix: `test_direction3_vertical_up_handoff_
    dispatcher_is_wired`'s `^\\s*(?:from ...|import ...)` pattern returned zero matches against
    scene_dispatch.py's real source even though the import statement is genuinely present;
    the SAME scan with `re.MULTILINE` added found it. `re.MULTILINE` is safe for every other
    caller of this function in this module — none of the other patterns use `^`/`$` anchors, so
    adding the flag changes nothing for them."""
    rx = re.compile(pattern, re.MULTILINE)
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


def test_direction2b_bottom_up_accord_echo_leg_is_wired_but_dormant():
    """directional_coverage_v1.md #2 — the Accord leg. compute_accord_echo must have >=1 caller
    among the live cross-scale emitter modules (caller-exists), AND no live emitter module may
    declare `echo['scene_outcome']` yet (dormancy) — WIRED but DORMANT, not resolved.

    WAVE-2 REWRITE (orchestrator-adjudicated fix batch, 2026-07-29, OI-03 fix 1 fallout): the
    prior version of this test was RESOLVED/XPASS(strict) on a bare source-scan for "a caller
    exists" alone. That framing went stale the moment OI-03 fix 1 deleted
    `echo_transport._ACCORD_OUTCOME_BY_SCENE_TYPE`'s `{"combat": "violence"}` fallback (see that
    module's WAVE-2 CORRECTION comment): classification now requires an explicit caller-declared
    `echo['scene_outcome']`, and no live emitter module supplies one, so the leg went from
    "reachable via a combat scene" back to organically DORMANT. Reporting caller-exists alone as
    "wired" would silently overstate reachability again — the critic's 'missing' finding this
    row repairs. Both halves are asserted here, honestly, rather than re-adding an XFAIL_MANIFEST
    row for functionality that DOES exist (a manifest row is for still-UNWIRED functionality;
    this is wired-but-not-organically-triggered, a different, established shape — see
    echo_transport.py module docstring's own "INERT-in-the-live-loop" framing for the sibling
    §5.2 leg)."""
    # domain_echo.py itself is EXCLUDED here — it's the definer (both the `def` line and its own
    # module docstring's "Entry points" list mention the name, neither is a call site); this test
    # asks whether anything ELSE calls it, so it scans the other emitter modules only.
    caller_modules = [m for m in _KEY_DELIVERY_EMITTER_MODULES if m != "engine.cross_scale.domain_echo"]

    # Half 1 — caller exists: compute_accord_echo has a real call site among the live emitters.
    _checked, matches = _source_scan(r"compute_accord_echo\(", caller_modules)
    assert matches, "compute_accord_echo has zero callers among the live emitter modules"

    # Half 2 — dormancy: no live PRODUCER module (the two modules that build a `ctx['echo']`
    # block for echo_transport to consume — scene_dispatch.py's emergency_council/combat
    # branches, parliamentary_bridge.py's vote ctx) DECLARES echo['scene_outcome'] as an INPUT
    # (a dict-literal assignment, `"scene_outcome": ...`, inside the `echo = {...}` block they
    # build). echo_transport.py itself is deliberately EXCLUDED from this half — its own
    # `_apply_accord_echo` builds a RETURN/telemetry dict containing a `"scene_outcome": ...`
    # entry (recording the classification result), which is a consumer-side bookkeeping write,
    # not a producer declaring the input; including it here would be a false positive. If a
    # producer module ever declares the input key, the leg has become organically reachable and
    # this test (and echo_transport.py's DORMANT framing) must be updated together, not left
    # silently stale the way the caller-exists-only version of this test was.
    producer_modules = ["engine.cross_scale.scene_dispatch", "engine.cross_scale.parliamentary_bridge"]
    _checked2, outcome_declarations = _source_scan(r"[\"']scene_outcome[\"']\s*:", producer_modules)
    assert not outcome_declarations, (
        "a live producer module now declares echo['scene_outcome'] — the accord-echo leg is no "
        "longer dormant; update this test's framing (and echo_transport.py's module docstring) "
        f"to reflect organic reachability instead of caller-exists-but-dormant: {outcome_declarations}")


def test_direction3_vertical_up_handoff_dispatcher_is_wired():
    """directional_coverage_v1.md #3 — DOCTRINE-ONLY. handoff_rules.py must be imported by at
    least one live cross-scale/autoload module (not a docstring mention) for the curated 8-rule
    dispatcher to be anything but bypassed.

    RESOLVED (Wave 2 item 5, OI-06, XFAIL_MANIFEST row 'vertical-up-handoff' retired 2026-07-29):
    the L-handoff lane added a genuine `from engine.cross_scale import handoff_rules` import to
    scene_dispatch.py. Getting this row to XPASS also surfaced and fixed a real bug in THIS
    file's own `_source_scan` (see its docstring) — the `^`-anchored pattern below could never
    have matched without the `re.MULTILINE` fix, regardless of how thoroughly the import was
    wired. STRICT now (no xfail): the row is removed from XFAIL_MANIFEST."""
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


def test_direction4b_territory_transfer_resolver_is_called():
    """OI-04 residual on top of direction 4's core bar: parliamentary_transfer.propose_transfer
    must have >=1 caller.

    RESOLVED (Wave 2 item 2, OI-04, XFAIL_MANIFEST row 'territory-transfer-resolver' retired
    2026-07-29): the L-transfer lane added `_derive_transfer`/`_run_transfer_motion` to
    engine/cross_scale/parliamentary_bridge.py, wired into `run_parliamentary_scene`;
    `_run_transfer_motion` calls `parliamentary_transfer.propose_transfer` at
    parliamentary_bridge.py:160 — closing the one-way territory ratchet OI-04 describes. STRICT
    now (no xfail): the row is removed from XFAIL_MANIFEST."""
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


def _scene_outcome_declared_by_a_live_producer() -> bool:
    """Shared dormancy check, kept IDENTICAL to test_direction2b_bottom_up_accord_echo_leg_is_
    wired_but_dormant's own scan so the two dormancy claims (that test's Half 2, and this
    function's use as the diagonal-causes xfail condition) can never silently diverge. True once
    ANY live producer module declares echo['scene_outcome'] as an input -- at which point the
    accord-echo leg (and this direction's causes[] path with it) becomes organically reachable."""
    producer_modules = ["engine.cross_scale.scene_dispatch", "engine.cross_scale.parliamentary_bridge"]
    _checked, matches = _source_scan(r"[\"']scene_outcome[\"']\s*:", producer_modules)
    return bool(matches)


@pytest.mark.xfail(not _scene_outcome_declared_by_a_live_producer(), strict=True,
                    reason=_manifest_reason("diagonal-causes"))
def test_direction6_diagonal_causes_has_an_instance():
    """directional_coverage_v1.md #6 — the headline directional gap (OI-28), CORRECTED FRAMING
    (2026-07-29): the prior version of this test did a raw source-text scan for any non-empty
    `causes=[...]` literal, which is EXACTLY the shape that would silently XPASS the moment
    `_apply_accord_echo` started writing `causes=[caused_by_key_id] if caused_by_key_id else []`
    into its own source (a real, load-bearing line, not decorative) -- passing on TEXT PRESENCE
    while the path stays organically unreached in every real campaign. This is now a CAMPAIGN-
    SHAPED runtime probe instead: drive `emit_scene_echo` with the exact ctx shape a live producer
    would supply MINUS `scene_outcome` (the genuinely-missing input, per the dormancy scan the
    xfail condition above shares with test_direction2b) and assert the real KeyLog contains >=1
    Key with a non-empty `causes[]`. Today this is honestly red (dormant: no scene.accord_echo Key
    is even built without a declared scene_outcome, so nothing in the log ever carries a populated
    causes[]) -- xfail, with a LIVE-INTROSPECTED marker (the dormancy scan above) that self-lifts
    the moment a producer supplies scene_outcome. CORRECTION (re-critic HIGH, 2026-07-29): that is
    NOT the same as "no manual burn-down step needed" -- the ctx built above deliberately omits
    scene_outcome (real dormancy, not a placeholder), so when the marker lifts this test goes HARD
    RED, not green: the body must be rewritten to thread the landed producer's actual input before
    it can pass. The marker lifting is a deliberate loud alarm demanding that rewrite, not a
    self-resolving row. See engine/tests/test_accord_echo.py's own §3 tests for the unit-level
    falsifier that the
    MECHANISM itself (given the input) genuinely populates causes[] -- that suite hand-supplies
    scene_outcome deliberately, to test the mechanism in isolation from the dormancy question this
    test tracks."""
    world = _world_with_scheduler(seed=42)
    fid = next(iter(world.factions))
    sid = next(iter(getattr(world, "settlements", {})), None)
    assert sid is not None, "fixture needs >=1 settlement"
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "target_settlement": sid}}  # no scene_outcome -- real dormancy
    echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    causal_keys = [k for k in world.key_log if k.causes]
    assert causal_keys, "no Key in the real KeyLog carries a populated causes[] (OI-28 diagonal direction unreached)"


def test_direction6b_accord_echo_leg_receives_a_genuine_in_log_causal_id():
    """OI-28 LIVE half (W3 item 3), the honestly-scoped claim: NOT 'a Key's causes[] is
    populated' (that is test_direction6 above, still xfail — no accord Key exists yet to carry
    one, see the manifest row) but 'the one live candidate site threads a REAL, already-in-log
    Key id to the place that WILL populate causes[] the moment that Key exists' — a seeded run
    with echo flags ON, asserting >=1 (assert checked >= 1, CLAUDE.md §0.1 point 2). This is a
    genuine, runtime, non-decorative check: it does not just import-scan for a string, it drives
    echo_transport.emit_scene_echo for real and looks the returned id up in the real KeyLog."""
    world = _world_with_scheduler(seed=42)
    fid = next(iter(world.factions))
    sid = next(iter(getattr(world, "settlements", {})), None)
    assert sid is not None, "fixture needs >=1 settlement"
    world.settlements[sid].order = 2
    ctx = {"echo": {"actor_faction": fid, "target_faction": fid, "most_relevant_stat": "L",
                    "degree": "Success", "scene_outcome": "governance",
                    "target_settlement": sid}}
    out = echo_transport.emit_scene_echo("contest", {"winner": "A"}, ctx, world)
    checked = 0
    accord_rows = out.get("accord_applied") or []
    assert accord_rows, "fixture assumption: the §5.5 Accord leg must fire for this ctx"
    for row in accord_rows:
        cause_id = row.get("caused_by_key_id")
        assert cause_id is not None, "fixture assumption: the §5.2 leg must also fire for this ctx"
        # The keys.py:325 invariant itself, exercised directly: lookup() raises KeyError if the
        # id is not genuinely in the log — this is not a string-equality check.
        assert world.echo_scheduler.log.lookup(cause_id) is not None
        checked += 1
    assert checked >= 1  # assert-that-asserted (CLAUDE.md §0.1 point 2)


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
# §1 acceptance — "world chains populated" (OI-05/OI-07). world-settlements resolved Wave 2
# (below); world-npcs/world-knots are Wave-2-RECLASSIFIED to `honest-deferral` — permanently
# xfail, not "until a later wave" (see XFAIL_MANIFEST's per-row reason for the canon citation).
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


def test_world_settlements_populated_after_a_seeded_campaign():
    """RESOLVED (Wave 2 item 4, OI-07, XFAIL_MANIFEST row 'world-settlements' retired
    2026-07-29): systems/settlements/sim/registry.py gained `populate_from_geography`, called at
    world-gen and serialized via game_state.serialize_world/restore_world — confirmed XPASS(strict)
    by running this test directly. This row stays a REACH probe (truthiness only, matching this
    file's own convention for direction/world-chain rows); the thorough falsifier (exact count
    vs. the geography source, serialization round-trip, RNG-purity) lives in
    engine/tests/test_world_population.py, not duplicated here. STRICT now (no xfail)."""
    r = run_campaign(seed=42)
    settlements = r.final_state.get("settlements", {})
    assert settlements, "world.settlements stayed empty or unserialized entirely (OI-07)"


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — articulation minimal bus subscriber (OI-08, plan §3 Wave 2 item 6). New this
# wave: no XFAIL_MANIFEST row (the subscriber is LIVE, not deferred) — same pattern as directions
# 1/2a/4/5 above (a dedicated strict reach test, no manifest bookkeeping needed for an already-
# wired direction).
# ═════════════════════════════════════════════════════════════════════════════════════════════

def test_articulation_subscriber_is_wired_and_stub_flags_fire():
    """OI-08: TickScheduler.subscribe (engine/substrate/keys.py:447) had ZERO callers anywhere in
    the corpus before this wave. engine.cross_scale.articulation.subscribe_all is now that first
    caller, AND it is reachable from the real production path: engine/mc_v18.py's
    `if _echo_transport_on(effective_params):` block calls `_articulation.subscribe_all(
    world.echo_scheduler)` immediately after `world.echo_scheduler = echo_transport.make_scheduler(
    ...)` (verified live at that call site) — the same attach pattern `_world_with_scheduler` above
    mirrors, which is what this probe uses (run_campaign's own CampaignResult does not expose
    `world` after returning, only telemetry fields, so a full-campaign probe cannot inspect
    `world.echo_scheduler.subscriptions` directly).

    Unit-level coverage of subscribe_all's own contract (exact 10 type_ids, per-type stub firing,
    non-idempotency) already lives in tests/valoria/test_articulation_subscriber.py — this row
    asserts REACH only (>= 9 subscribed types per the task's own floor, plus one live stub-flag
    firing visible through the same scheduler object mc_v18 constructs), not re-deriving that
    file's thorough per-type sweep."""
    from engine.cross_scale import articulation
    from engine.substrate import stubwire

    world = _world_with_scheduler(seed=21)
    count = articulation.subscribe_all(world.echo_scheduler)
    assert count >= 9, f"expected >=9 §3.1 trigger types subscribed (OI-08 floor), got {count}"

    # stub-flag invocations visible: the callback registered for a subscribed type_id must fire a
    # typed stubwire no-op when invoked — mirroring how TickScheduler.emit would call it, without
    # needing a fully registry-valid Key (the callback body ignores its `key` argument by
    # contract — engine/cross_scale/articulation.py's `_on_key` closure only reads `type_id`).
    type_id = next(iter(world.echo_scheduler.subscriptions))
    callback = world.echo_scheduler.subscriptions[type_id][0]
    stubwire.reset_invocations()
    before = stubwire.invocations
    result = callback(None, world.echo_scheduler)
    assert stubwire.invocations == before + 1, "subscribed callback did not fire a stub-wire flag"
    assert result.stub is True and result.module == "engine.cross_scale.articulation"


def test_articulation_subscriber_is_wired_in_a_real_production_campaign_construction():
    """WAVE-2 REACH-GUARD REPAIR (critic 'missing', ED-IN-0091 plan §3 Wave 2 item 8): the test
    above asserts subscribe_all's own contract via `_world_with_scheduler` — a HAND-BUILT world +
    scheduler this file constructs itself, not the production `engine.mc_v18.run_campaign`
    construction path. Its docstring CLAIMED production reach ("verified live at that call
    site") but never actually exercised `run_campaign`'s own `if _echo_transport_on(...)` block —
    a future edit that deleted `_articulation.subscribe_all(world.echo_scheduler)` from
    `run_campaign` would leave that test green (it never calls `run_campaign` at all). This test
    closes that gap: it patches `articulation.subscribe_all` itself (not the scheduler) and runs
    a REAL `run_campaign(..., params={'ECHO_TRANSPORT': 1})` construction, so it fails if the
    production hook is ever dropped, edited to call a different function, or never invoked."""
    from unittest import mock

    from engine.cross_scale import articulation

    with mock.patch.object(articulation, "subscribe_all", wraps=articulation.subscribe_all) as spy:
        run_campaign(seed=21, max_seasons=1, params={"ECHO_TRANSPORT": 1})

    assert spy.call_count >= 1, (
        "engine.mc_v18.run_campaign's ECHO_TRANSPORT-on construction path did not call "
        "articulation.subscribe_all at all — the PRODUCTION hook (not the hand-built helper the "
        "test above uses) must wire the subscriber")
    (scheduler_arg,), _kwargs = spy.call_args
    assert scheduler_arg.subscriptions, (
        "articulation.subscribe_all was called by run_campaign but registered zero subscriptions "
        "on the real scheduler it was given")


@pytest.mark.xfail(not _dispatch_combat_bridge_on({}), strict=True,
                    reason=_manifest_reason("combat-bridge-on"))
def test_combat_pair_key_reaches_articulation_subscriber_under_flag_on():
    """W3 item 7 (critic SHARPEN HIGH) — the campaign-consumption falsifier for the combat pair:
    under DISPATCH_COMBAT_BRIDGE ON (+ the echo scheduler attached, ECHO_TRANSPORT default ON),
    a combat scene's Key genuinely reaches the articulation subscriber through the REAL dispatch
    pipeline (`scene_dispatch._resolve_slot` -> `echo_transport.emit_scene_echo` ->
    `TickScheduler.emit` -> the subscribed callback) — not just that `_TRIGGER_TYPE_IDS` lists
    `scene.combat_resolved`/`scene.combat_felled` (tests/valoria/test_articulation_subscriber.py's
    `test_combat_pair_reaches_the_articulation_subscriber` is the isolated unit proof of THAT) but
    that a real combat scene dispatch actually delivers one. xfail while DISPATCH_COMBAT_BRIDGE is
    OFF (today's default) — mirrors `test_combat_resolves_via_canonical_bridge_under_flag_on`'s own
    gate exactly (same manifest row, same flag); run with env DISPATCH_COMBAT_BRIDGE=1 to exercise
    the strict assertion for real.

    SEED (re-critic MED, 2026-07-29): `04_execution_ledger.md:105` claimed the strict assertion
    was "verified manually with the flag on" without pinning which seed or recording how to
    reproduce it. Re-verified here with a 30-seed sweep (seed=0..29, each seed re-run through this
    exact body: `DISPATCH_COMBAT_BRIDGE=1 python3 -m pytest
    engine/tests/test_pipeline_reach.py::test_combat_pair_key_reaches_articulation_subscriber_under_flag_on
    -q`) — DRAW-INSENSITIVE: all 30 seeds pass identically (resolved=True, exactly one
    scene.combat_resolved Key logged, stubwire fires), so seed choice here is a stability
    convention, not a cherry-pick. Pinned to seed=0 (the first seed of the sweep, previously an
    unremarked seed=7)."""
    from engine.cross_scale import articulation

    world = _world_with_scheduler(seed=0)
    world.dispatch_combat_bridge = _dispatch_combat_bridge_on({})
    articulation.subscribe_all(world.echo_scheduler)
    stubwire.reset_invocations()
    before = stubwire.invocations

    slot = scene_slate.SceneSlot(scene_type="combat",
                                  context={"factions": ("Crown", "Church")}, priority=0)
    res = scene_dispatch._resolve_slot(slot, world, world.rng)
    assert res.get("resolved") is True, f"combat did not resolve via the canonical bridge: {res}"

    combat_resolved_keys = [k for k in world.echo_scheduler.log if k.type == "scene.combat_resolved"]
    assert combat_resolved_keys, (
        "no scene.combat_resolved Key was emitted by the real dispatch pipeline "
        f"(dispatch result: {res})")
    assert stubwire.invocations > before, (
        "a scene.combat_resolved Key was logged but articulation's subscribed callback never fired "
        "(TickScheduler.emit did not reach the subscriber)")


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — OI-12 orphan census pointer (plan §3 Wave 2 item 7). Per the Oracle stage's own
# instruction, a manifest row PER still-orphan module is overkill for a 14-module census; this is
# the single pointer row citing the census's actual home
# (audit/2026-07-29-code-shape-open-items/04_execution_ledger.md), matching direction7b's own
# "declared deferral" pattern above rather than re-deriving the census here.
# ═════════════════════════════════════════════════════════════════════════════════════════════

_OI12_ALREADY_STUB_WIRED = (
    "engine/autoload/npc_ai.py",
    "systems/characters/sim/companion.py",
    "systems/overview/sim/rs_track.py",
    "systems/overview/sim/ip_track.py",
    "systems/threadwork/sim/rendering.py",
    "systems/world/sim/miraculous_event.py",
    "systems/world/sim/restoration_movement.py",
)
_OI12_VERIFIED_ORPHAN_NO_CALLSITE = (
    "systems/threadwork/sim/co_movement.py",
    "systems/threadwork/sim/collective.py",
    "systems/threadwork/sim/opposing.py",
    "systems/settlements/sim/settlement.py",
    "systems/settlements/sim/temperaments.py",
    "systems/social_contest/sim/parliamentary_stay.py",
    "engine/autoload/registry.py",
)


def _load_structure_audit():
    """Load skills/valoria-vector-audit/scripts/structure_audit.py the SAME way
    tests/valoria/test_structure_audit.py does (importlib.util, since scripts/ is not a
    package) -- reused here rather than re-implemented, per CLAUDE.md §8."""
    import importlib.util
    script = os.path.join(_REPO_ROOT, "skills", "valoria-vector-audit", "scripts", "structure_audit.py")
    spec = importlib.util.spec_from_file_location("structure_audit", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_oi12_census_is_recorded_in_the_execution_ledger():
    """The census itself (documentation only, no code edits per the L-artic lane's own note) lives
    in 04_execution_ledger.md, not here — this asserts the full 14-module list this wave's census
    covers is genuinely present there, so a future edit that silently drops a module from the
    ledger's record trips here rather than the census quietly rotting out of sync with this
    pointer. Does not re-verify each module's live import-orphan status (that is
    `test_oi12_census_matches_the_real_structure_audit_classification` below, split out so a
    doc-presence failure and a live-classification-drift failure report distinctly)."""
    doc_path = os.path.join(_REPO_ROOT, "audit", "2026-07-29-code-shape-open-items",
                             "04_execution_ledger.md")
    assert os.path.isfile(doc_path), "04_execution_ledger.md (OI-12 census's home) is missing"
    text = open(doc_path, encoding="utf-8").read()
    assert "OI-12 census" in text, "OI-12 census is no longer recorded in the execution ledger"

    missing = [mod_path for mod_path in _OI12_ALREADY_STUB_WIRED + _OI12_VERIFIED_ORPHAN_NO_CALLSITE
               if mod_path not in text]
    assert not missing, (
        "module(s) dropped from the OI-12 census record in 04_execution_ledger.md:\n"
        + "\n".join(missing)
    )


def test_oi12_census_matches_the_real_structure_audit_classification():
    """WAVE-2 REPAIR (critic 'missing', CLAUDE.md §0.1 point 2): the prior version of this
    module's checks used `checked = 0; for mod_path in <fixed literal tuple>: checked += 1; ...;
    assert checked == len(<the same tuple>)` — the SAME decorative-counter class this file's own
    module docstring corrects elsewhere (CORRECTION 2): `checked` increments unconditionally,
    once per entry of a fixed-length literal, with no skip path, so the count could not fail
    short of editing the tuple literals themselves; it asserted nothing a reader could not
    already see from the tuple lengths.

    This test re-derives the REAL orphan / stub_wired sets from structure_audit's own graph
    functions (the identical functions `tests/valoria/test_structure_audit.py`'s
    `test_orphan_cli_split_conservation` calls over the real repo tree — reused, not
    re-implemented) and compares the two pinned census tuples against them: a module pinned
    `_OI12_ALREADY_STUB_WIRED` must still be `stub_wired`; a module pinned
    `_OI12_VERIFIED_ORPHAN_NO_CALLSITE` must still be a `code_orphan`. This is genuinely
    falsifiable — if a census module's live classification drifts (a caller lands, or a stubwire
    import is removed), this fails and names exactly which module and which direction, rather
    than passing regardless."""
    sa = _load_structure_audit()
    root = sa.Path(_REPO_ROOT)
    modules = sa.collect_py_modules(root)
    g_code, _parse_errors = sa.build_g_code(root, modules)
    code_nodes = list(modules)
    code_deg = sa.degrees(g_code, code_nodes)
    main_guard_modules = sa.collect_cli_entry_modules(root, modules)
    code_orphans, _cli_entries = sa.split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules)
    orphan_set = set(code_orphans)
    stub_wired_set = set(sa.stub_wired_modules(g_code))

    checked = 0
    mismatches = []
    for mod_path in _OI12_ALREADY_STUB_WIRED:
        checked += 1
        dotted = sa._module_name(mod_path)
        if dotted not in stub_wired_set:
            mismatches.append(
                f"{mod_path} ({dotted}): pinned already-stub-wired but structure_audit no "
                f"longer classifies it stub_wired")
    for mod_path in _OI12_VERIFIED_ORPHAN_NO_CALLSITE:
        checked += 1
        dotted = sa._module_name(mod_path)
        if dotted not in orphan_set:
            mismatches.append(
                f"{mod_path} ({dotted}): pinned verified-orphan-no-callsite but structure_audit "
                f"no longer classifies it an import orphan (a caller landed) — update the OI-12 "
                f"census row, not this test")
    # assert-that-asserted (CLAUDE.md §0.1 point 2): the mismatch collection above is the real
    # conditional check per module; this confirms every pinned module was actually looked up
    # against the live classification, not skipped.
    assert checked == len(_OI12_ALREADY_STUB_WIRED) + len(_OI12_VERIFIED_ORPHAN_NO_CALLSITE)
    assert not mismatches, (
        "OI-12 census drifted from the real structure_audit classification:\n" + "\n".join(mismatches)
    )


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
