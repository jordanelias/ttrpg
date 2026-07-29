"""tests/valoria/test_handoff_dispatch_validity.py — OI-06 falsifier (ED-IN-0091 plan §3 Wave 2
item 5, register row OI-06).

OI-06: `handoff_rules.py` (the curated 8-rule cross-scale dispatcher, scale_transitions_v30.md §3)
was an import-orphan — its only "importers" were docstring mentions. This wires it as a VALIDITY
layer inside `engine/cross_scale/scene_dispatch.py`, at the one scale-transition dispatch already
reaches (Scene resolved -> handing outcome up to Faction scale, alongside the zoom_in_out calls).

What's pinned here, and why each is the falsifier for a specific claim (§0.1 point 3):
  - `handoff_rules` is a genuine live import of `scene_dispatch` (not a docstring mention) — the
    exact defect OI-06 named. `engine/tests/test_pipeline_reach.py`'s own
    `test_direction3_vertical_up_handoff_dispatcher_is_wired` (Oracle-owned, not edited here)
    checks the same fact via source-scan; this test checks it via direct introspection so this
    lane's own falsifier does not depend on that file's xfail-manifest state.
  - All 8 built §3 rules are exercised, DIRECTLY against `handoff_rules.apply_handoff` (dispatch
    itself can only reach ONE of the 8 today — Scene -> Faction, §3.4 — since scene_dispatch's
    scene_type vocabulary is narrower than handoff_rules' scale vocabulary; the other 7 are not
    reachable through any live dispatch path this wave. Recorded here, not glossed over.)
  - The invalid-pair path: a scale pair outside all 8 rules (and outside the §3.9 Fieldwork
    catch-all) makes `apply_handoff` return `valid=False`, and the OI-06 wrapper turns that into a
    VISIBLE `stubwire.StubResult` — never handoff_rules' own silent dict (handoff_rules.py:226-232,
    "No §3 rule defined").
  - §3.3 Personal -> Scene (Contest) is a canon-EMPTY heading held on the ED-IN-0049 fork (plan §5
    fork 11). `handoff_rules.py`'s own branch for that pair pre-empts the fork with placeholder
    procedure text; the OI-06 wrapper does not trust it and stub-flags the pair unconditionally,
    citing the fork — verified directly, since no live dispatch path derives this pair today.
  - Combat and contest — the only two scene_types dispatch derives a scale pair for — are
    exercised THROUGH `scene_dispatch._resolve_slot` and asserted behavior-neutral: no change to
    `resolved`/`result`, and the handoff layer's own flag never fires for them (both resolve to
    the always-valid §3.4 pair) — the plan's own "behavior-neutral for every currently-valid
    transition" exit term (item 5).
"""
from __future__ import annotations

import inspect
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.autoload import game_state, scene_slate  # noqa: E402
from engine.cross_scale import handoff_rules, scene_dispatch  # noqa: E402
from engine.substrate import stubwire  # noqa: E402


# ── scene_dispatch genuinely imports handoff_rules (not a docstring mention) ────────────────────

def test_scene_dispatch_carries_a_live_handoff_rules_import():
    src = inspect.getsource(scene_dispatch)
    assert "from engine.cross_scale import handoff_rules" in src.split("\n\n\n")[0] or \
           any(l.strip().startswith(("from engine.cross_scale import handoff_rules",
                                      "import engine.cross_scale.handoff_rules"))
               for l in src.splitlines()), (
        "scene_dispatch.py no longer carries a live handoff_rules import statement")
    # And it is actually bound to the real module object, not shadowed by a local of the same name.
    assert scene_dispatch.handoff_rules is handoff_rules


# ── all 8 built §3 rules, exercised directly (dispatch can only reach one of them) ──────────────

_ALL_EIGHT_PAIRS = [
    (handoff_rules.SCALE_PERSONAL, handoff_rules.SCALE_THREAD, handoff_rules.RULE_PERSONAL_TO_THREAD),
    (handoff_rules.SCALE_PERSONAL, handoff_rules.SCALE_FACTION, handoff_rules.RULE_PERSONAL_TO_FACTION),
    (handoff_rules.SCALE_PERSONAL, handoff_rules.SCALE_SCENE, handoff_rules.RULE_PERSONAL_TO_SCENE),
    (handoff_rules.SCALE_SCENE, handoff_rules.SCALE_FACTION, handoff_rules.RULE_SCENE_TO_FACTION),
    (handoff_rules.SCALE_THREAD, handoff_rules.SCALE_FACTION, handoff_rules.RULE_THREAD_TO_FACTION),
    (handoff_rules.SCALE_THREAD, handoff_rules.SCALE_MASS, handoff_rules.RULE_THREAD_TO_MASS),
    (handoff_rules.SCALE_MASS, handoff_rules.SCALE_PERSONAL, handoff_rules.RULE_MASS_TO_PERSONAL),
    (handoff_rules.SCALE_SCENE, handoff_rules.SCALE_MASS, handoff_rules.RULE_SCENE_TO_MASS),
]


def test_all_eight_built_rules_resolve_valid_directly():
    """Direct exercise (dispatch cannot reach 7 of these 8 today — recorded, not glossed: only
    (Scene, Faction) is derivable from any live scene_type, see
    `scene_dispatch._HANDOFF_SCALE_PAIR_BY_SCENE_TYPE`)."""
    assert len(_ALL_EIGHT_PAIRS) == 8
    for from_scale, to_scale, expected_rule_name in _ALL_EIGHT_PAIRS:
        result = handoff_rules.apply_handoff(from_scale, to_scale, {}, world=None)
        assert result.valid is True, f"{from_scale} -> {to_scale} unexpectedly invalid"
        assert result.rule_name == expected_rule_name


def test_scene_to_faction_is_the_one_pair_dispatch_derives():
    """The OI-06 scale-pair table dispatch actually uses — pinned so a future scene_type addition
    that silently changes this mapping is caught here, not discovered downstream."""
    assert scene_dispatch._HANDOFF_SCALE_PAIR_BY_SCENE_TYPE == {
        "combat": (handoff_rules.SCALE_SCENE, handoff_rules.SCALE_FACTION),
        "contest": (handoff_rules.SCALE_SCENE, handoff_rules.SCALE_FACTION),
    }


# ── invalid-pair path: a VISIBLE stubwire flag, never handoff_rules' own silent dict ────────────

def test_invalid_pair_is_flagged_by_handoff_rules_itself():
    """Baseline: confirm the pair this test uses really is one of handoff_rules' own invalid
    transitions (guards against the wrapper test below silently testing a pair that later becomes
    one of the 8 rules)."""
    result = handoff_rules.apply_handoff(handoff_rules.SCALE_FACTION, handoff_rules.SCALE_PERSONAL,
                                          {}, world=None)
    assert result.valid is False
    assert "No §3 rule defined" in result.notes[0]


def test_invalid_pair_wrapper_returns_a_visible_stubwire_flag():
    before = stubwire.invocations
    stub = scene_dispatch._handoff_validity_check_pair(
        handoff_rules.SCALE_FACTION, handoff_rules.SCALE_PERSONAL, {}, None)
    assert isinstance(stub, stubwire.StubResult)
    assert stub.stub is True
    assert stub.module == 'engine.cross_scale.scene_dispatch'
    assert "No §3 rule defined" in stub.reason
    # The counter genuinely moved — this is not a look-alike object, it is the single owner
    # (engine.substrate.stubwire) actually being invoked (CLAUDE.md §0.1 point 2).
    assert stubwire.invocations == before + 1


def test_valid_pair_wrapper_returns_none_no_stub_fires():
    before = stubwire.invocations
    result = scene_dispatch._handoff_validity_check_pair(
        handoff_rules.SCALE_SCENE, handoff_rules.SCALE_FACTION, {}, None)
    assert result is None
    assert stubwire.invocations == before


# ── §3.3 Personal -> Scene (Contest): held on the ED-IN-0049 fork, never trusted as content ─────

def test_personal_to_scene_fork_is_stub_flagged_not_trusted():
    """handoff_rules.py's own (Personal, Scene) branch returns valid=True with placeholder
    procedure text ("Open Contest scene per social_contest_v30") — confirmed here so the wrapper
    test below is provably testing an override, not a pair that was already invalid."""
    raw = handoff_rules.apply_handoff(handoff_rules.SCALE_PERSONAL, handoff_rules.SCALE_SCENE,
                                       {}, world=None)
    assert raw.valid is True  # handoff_rules itself does not gate this — the wrapper must.

    stub = scene_dispatch._handoff_validity_check_pair(
        handoff_rules.SCALE_PERSONAL, handoff_rules.SCALE_SCENE, {}, None)
    assert isinstance(stub, stubwire.StubResult)
    assert "ED-IN-0049" in stub.reason
    assert "fork" in stub.reason


# ── through dispatch: behavior-neutral for combat/contest (both derive the always-valid pair) ───

def _fresh_world(seed):
    return game_state.create_world(seed=seed)


def test_contest_dispatch_through_handoff_layer_is_behavior_neutral():
    world = _fresh_world(seed=3)
    slot = scene_slate.SceneSlot(
        scene_type="contest",
        context={"faction": "Crown", "stakes": {"kind": "emergency_council", "faction": "Crown"}},
        priority=0)
    before = stubwire.invocations
    res = scene_dispatch._resolve_slot(slot, world, world.rng)
    assert res.get("resolved") is True
    # The always-valid (Scene, Faction) pair never trips the stub layer — no golden-affecting
    # side effect, per the plan's "behavior-neutral for every currently-valid transition" term.
    assert "handoff_stub" not in res
    assert stubwire.invocations == before


def test_combat_dispatch_through_handoff_layer_is_behavior_neutral():
    world = _fresh_world(seed=7)
    world.dispatch_combat_bridge = True
    slot = scene_slate.SceneSlot(scene_type="combat",
                                  context={"factions": ("Crown", "Church")}, priority=0)
    before = stubwire.invocations
    res = scene_dispatch._resolve_slot(slot, world, world.rng)
    assert res.get("resolved") is True
    assert "handoff_stub" not in res
    assert stubwire.invocations == before


def test_scene_types_with_no_derivable_pair_are_untouched_by_the_handoff_layer():
    """fieldwork/investigation/the total-mapping stub all `return` before the handoff call site
    (see scene_dispatch._resolve_slot) — this pins that the handoff layer plays no role for them
    (OI-02's own stub-wire is the one that fires), and that `_handoff_validity_check` itself is
    a safe no-op default for a scene_type outside its lookup table."""
    world = _fresh_world(seed=11)
    assert scene_dispatch._handoff_validity_check("fieldwork", {}, world) is None
    assert scene_dispatch._handoff_validity_check("domain_action", {}, world) is None
