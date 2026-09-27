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

RETIRED 2026-09-27 (mc_v18-retirement plan M1): the `combat-bridge-on`, `world-npcs` and
`world-knots` XFAIL_MANIFEST rows and their tests are deleted along with the `engine.mc_v18`
import. `world-npcs`/`world-knots` duplicated `test_f7_smoke_oracle.py`'s own `npcs_generated==0`
golden and `test_world_population.py`'s honest-deferral guards (the latter kept, rewritten off
mc_v18 — see that file); `combat-bridge-on` exercised only mc_v18's own dormant dispatch branch
(env-var-gated, off by default, never run in a normal CI pass). None of the three had a live
trigger surface independent of the frozen module. `world-settlements` is deleted too, for the
same reason as its near-duplicate in `test_world_population.py`: settlements populate once, at
`create_world` time, and `run_campaign` never re-derives them, so the world-gen-time falsifier
(`test_settlements_populated_at_world_gen_matches_geography_source_exactly`, kept, in that other
file) already covers the live claim.
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
from engine.cross_scale import scene_dispatch  # noqa: E402
from engine.substrate import stubwire  # noqa: E402


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
#
# The combat-under-flag-ON probe that used to stand here (OI-01, `_dispatch_combat_bridge_on`
# imported from `engine.mc_v18`) is RETIRED 2026-09-27 — see module docstring. Combat is otherwise
# covered by `test_combat_bridge_seam.py`'s schema/determinism tests, which never touch mc_v18.


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
# §1 acceptance — "The 7 Key-delivery directions" RETIRED 2026-09-16 (ED-IN-0232).
#
# Eleven direction tests, a seven-direction roster check and three articulation-subscriber tests
# stood here — fifteen in all, every one of them exercising the Key bus: emit a Key, read the
# KeyLog, assert a `causes[]` id, count an emission per tick. Jordan: *"anything key-based gets
# retired"*. They are DELETED rather than re-pointed, because there is no bus to point them at.
#
# What that costs, said plainly: `directional_coverage_v1.md`'s claim that all seven delivery
# directions are exercised is no longer backed by anything in this tree, and the accord-echo leg's
# dormancy scan (`_scene_outcome_declared_by_a_live_producer`) went with them. The ten tests below
# are what survives, and none of them is about delivery — they cover the combat bridge, world
# population after a seeded campaign, and the stub-wiring census.
# ═════════════════════════════════════════════════════════════════════════════════════════════





























# §1 acceptance — "world chains populated" (OI-05/OI-07) RETIRED 2026-09-27 (mc_v18-retirement
# plan M1, see module docstring): world-npcs, world-knots and world-settlements each drove
# `engine.mc_v18.run_campaign` and are gone with that import. See module docstring for where each
# claim's live coverage now stands.

# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — articulation minimal bus subscriber (OI-08, plan §3 Wave 2 item 6). New this
# wave: no XFAIL_MANIFEST row (the subscriber is LIVE, not deferred) — same pattern as directions
# 1/2a/4/5 above (a dedicated strict reach test, no manifest bookkeeping needed for an already-
# wired direction).
# ═════════════════════════════════════════════════════════════════════════════════════════════







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
