"""engine/tests/test_combat_bridge_seam.py — the OI-01 combat-bridge characterization test
(ED-IN-0091 plan §2.2/§3 Wave 1 stage 3, critic F2 term 1).

RULE, STATED PER §0's "state the falsifier" / the plan's seam terms (do not violate it here):
this file pins SHAPE ONLY — the bridge's result schema, its determinism under a fixed seed, and
the presence of the fields `_resolve_slot`'s combat branch actually reads off `resolve()`'s return
dict. It NEVER pins a damage value, a win rate, or any other balance quantity computed inside
`combat_engine_v1`. A PC-lane rebalance of the weapon/armour/tradition tables must not turn ANY
assertion in this file red; if one day it does, the assertion was written wrong (plan §0 "Seam
terms for the wrapper", term 1) — fix the test, don't chase the PC session.

Also covers, per the Wave 1 exit criteria: a byte-parity probe that DISPATCH_COMBAT_BRIDGE=OFF
(the default) leaves campaign output completely unchanged from the pre-bridge behaviour, and that
DISPATCH_COMBAT_BRIDGE=ON is *itself* a no-op on any currently-reachable campaign, because nothing
in the live loop yet queues a `combat` scene_type (verified 2026-07-29 — see combat_bridge.py's
module docstring). That second probe is a reachability guard, not a balance claim: it would trip
the moment some future wave adds a combat-scene trigger, which is the intended signal.
"""
from __future__ import annotations

import os
import random

import pytest

from engine.autoload import game_state
from engine.cross_scale import combat_bridge
from engine.mc_v18 import run_campaign, run_batch


# ── derive_parties: schema + context-derivation-gap behaviour (never an outcome) ────────────────

def _world_with_factions(mil_a=4.0, mil_b=6.0):
    w = game_state.create_world(seed=1)
    w.factions['Crown'].Mil = mil_a
    w.factions['Church'].Mil = mil_b
    return w


def test_derive_parties_returns_two_combatants_with_history_from_faction_mil():
    """Schema + derivation-rule check ONLY: `history` tracks the cited faction's own Mil stat
    (rounded, floored at 1, per combat_bridge.py's docstring) — never a downstream combat value."""
    w = _world_with_factions(mil_a=4.0, mil_b=6.0)
    parts = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w)
    assert parts is not None
    a, b = parts
    assert a.label == "Crown" and b.label == "Church"
    assert a.history == 4 and b.history == 6
    # constructor defaults are PC-owned; this test pins shape, never PC values. Every OTHER
    # field is left at Combatant.__init__'s own default (not invented by this bridge) — assert
    # only that the fields exist and are the expected TYPE, never their literal PC-tuned value,
    # so a PC-lane rebalance of those defaults cannot turn this bridge test red (module
    # docstring's "CHARACTERIZATION, NOT OUTCOME" rule).
    assert isinstance(a.weapon, str) and isinstance(a.armor, str) and isinstance(a.tradition, str)
    assert isinstance(a.strength, (int, float)) and isinstance(a.agi, (int, float)) and isinstance(a.end, (int, float))


def test_derive_parties_floors_at_one():
    w = _world_with_factions(mil_a=0.0, mil_b=-3.0)
    a, b = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w)
    assert a.history >= 1 and b.history >= 1


@pytest.mark.parametrize("ctx", [
    {},                                        # no 'factions' key at all
    {"factions": ("Crown",)},                  # too short
    {"factions": ("Crown", "Nonexistent")},     # unresolvable second faction
    {"factions": ("Nonexistent", "Church")},    # unresolvable first faction
])
def test_derive_parties_returns_none_on_context_derivation_gap(ctx):
    """A gap is flagged (None), never papered over with an invented actor."""
    w = _world_with_factions()
    assert combat_bridge.derive_parties(ctx, w) is None


# ── resolve(): result-dict SHAPE + determinism, never an outcome pin ─────────────────────────────

_EXPECTED_RESOLVE_KEYS = {"result", "winner", "a_label", "b_label", "a_history", "b_history"}


def test_resolve_result_schema_and_internal_consistency():
    """Shape only: the exact key set `_resolve_slot`'s combat branch stores into `out['result']`,
    typed correctly, and internally self-consistent with `fight()`'s own documented winner
    convention (result==1 => A won, result==-1 => B won, 0 => unresolved) — a LOGICAL contract on
    the bridge's own mapping, not a claim about which side wins. See
    `test_resolve_winner_mapping_observes_both_sides` below for the branch-coverage guard on the
    winner mapping itself (this test only checks ONE seed's internal consistency)."""
    w = _world_with_factions()
    a, b = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w)
    result = combat_bridge.resolve(a, b, random.Random(12345))
    assert set(result.keys()) == _EXPECTED_RESOLVE_KEYS
    assert result["result"] in (-1, 0, 1)
    assert result["a_label"] == "Crown" and result["b_label"] == "Church"
    assert result["a_history"] == a.history and result["b_history"] == b.history
    if result["result"] == 1:
        assert result["winner"] == "Crown"
    elif result["result"] == -1:
        assert result["winner"] == "Church"
    else:
        assert result["winner"] is None


def test_resolve_winner_mapping_observes_both_sides():
    """§0.1 point 2 ("an assertion must be able to observe the failure it excludes"): a single
    fixed-seed winner-mapping check only ever exercises whichever ONE branch that seed happens to
    land on. This test forces the OTHER branch too: two fixtures with opposite EXTREME Mil
    asymmetry (6 vs 1, then 1 vs 6, `derive_parties` -> `history`) plus a small seed sweep per
    fixture. PER-FIXTURE, not unioned (re-critic round 2, item 6): the docstring's promise is that
    the A-favoring fixture surfaces an A win and the B-favoring fixture a B win — a unioned
    `observed >= {'A','B'}` across both fixtures combined does not actually check that; it would
    stay green even if BOTH fixtures only ever produced, say, A wins (the sweep would still
    observe {'A'} from one fixture... but a union check specifically would also stay green if
    fixture A happened to yield a B win and fixture B happened to yield an A win — the wrong
    fixture producing the wrong side's win). So each fixture's own seed sweep is asserted against
    its OWN expected winner set. `checked >= 2` (mirroring the "assert checked >= N" pattern)
    attests the sweep genuinely ran. The 0/undecided branch is exercised if it happens to appear
    but is never required — extreme asymmetry makes it rare, not excluded. If a fixture
    empirically cannot produce its expected winner within this sweep, this test is meant to fail
    loudly (not have its assertion weakened to a union) — that failure is real signal that either
    the extreme-Mil derivation or the wrapper's win logic does not behave as documented."""
    fixtures = {
        "A": (_world_with_factions(mil_a=6.0, mil_b=1.0), "A"),
        "B": (_world_with_factions(mil_a=1.0, mil_b=6.0), "B"),
    }
    checked = 0
    for fixture_name, (w, expected_side) in fixtures.items():
        observed = set()
        for seed in range(8):
            a, b = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w)
            result = combat_bridge.resolve(a, b, random.Random(seed))
            checked += 1
            if result["result"] == 1:
                assert result["winner"] == result["a_label"]
                observed.add("A")
            elif result["result"] == -1:
                assert result["winner"] == result["b_label"]
                observed.add("B")
            else:
                assert result["winner"] is None
        assert expected_side in observed, (
            f"fixture {fixture_name!r} (mil_a={w.factions['Crown'].Mil}, "
            f"mil_b={w.factions['Church'].Mil}) never surfaced a {expected_side}-win across its "
            f"8-seed sweep; only observed {observed!r} — the extreme-Mil fixture did not produce "
            f"its expected winner")
    assert checked >= 2


def test_resolve_is_deterministic_under_a_fixed_seed():
    """Same seed -> byte-identical result dict. A non-deterministic bridge cannot be an oracle
    for anything downstream (mirrors test_f7_smoke_oracle.test_f7_determinism's method) — this
    compares two runs to EACH OTHER, never to a hand-pinned literal, so it carries no balance
    claim. `test_resolve_winner_mapping_observes_both_sides` above is what genuinely demonstrates
    the rng is threaded through (by observing divergent outcomes across a seed sweep); a separate
    "different seeds CAN diverge" test duplicated this schema check without asserting anything
    about divergence, so it was deleted rather than kept alongside."""
    w1 = _world_with_factions()
    w2 = _world_with_factions()
    a1, b1 = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w1)
    a2, b2 = combat_bridge.derive_parties({"factions": ("Crown", "Church")}, w2)
    r1 = combat_bridge.resolve(a1, b1, random.Random(999))
    r2 = combat_bridge.resolve(a2, b2, random.Random(999))
    assert r1 == r2


# ── flag-OFF byte-parity + flag-ON reachability no-op (Wave 1 exit criteria) ─────────────────────

def test_no_params_equals_explicit_flag_off():
    """Pins no-params ≡ explicit-OFF equivalence ONLY — it does NOT and cannot observe OFF-drift:
    both arms of this comparison run the exact same post-bridge dispatch code (the flag is read
    off `world`, defaulting False either way), so a regression that changed the OFF-path itself
    would move both sides identically and this test would stay green. (Renamed from
    `test_flag_off_is_the_default_and_byte_identical_to_no_params`, which claimed exactly that
    "byte identical to [true, pre-bridge] no params" property this test cannot demonstrate.)
    The TRUE OFF-parity instruments — the ones that actually pin PRE-bridge behaviour and would
    catch OFF-path drift — are the pre-existing pinned goldens that run in the same gate:
    `test_f7_smoke_oracle.py` (`GOLDEN_SCENES_RESOLVED=463` etc.), `test_mc_v18_regression.py`,
    and `test_echo_transport.py`."""
    assert os.environ.get('DISPATCH_COMBAT_BRIDGE') is None, (
        "DISPATCH_COMBAT_BRIDGE must not be set in the test environment for this probe to be valid")
    default = run_batch(n=3, base_seed=42)
    explicit_off = run_batch(n=3, base_seed=42, params={'DISPATCH_COMBAT_BRIDGE': 0})
    assert default.win_share == explicit_off.win_share
    assert default.all_winners == explicit_off.all_winners
    assert default.battles_mean == explicit_off.battles_mean


def test_flag_on_is_a_no_op_on_the_currently_reachable_campaign():
    """No live trigger queues a `combat` scene_type today (verified 2026-07-29 — see
    combat_bridge.py's module docstring), so flipping DISPATCH_COMBAT_BRIDGE ON must not move
    ANY campaign output: the combat branch is simply never entered either way. This is a
    reachability guard, not a balance claim — the moment a future wave adds a combat-scene
    trigger, THIS test is expected to fail, and that failure is the intended signal to write the
    ON-state acceptance instead of silently red-lining."""
    off = run_campaign(seed=42, params={'DISPATCH_COMBAT_BRIDGE': 0})
    on = run_campaign(seed=42, params={'DISPATCH_COMBAT_BRIDGE': 1})
    assert off.winner == on.winner
    assert off.season == on.season
    assert off.scenes_resolved == on.scenes_resolved
    assert off.stub_hits == on.stub_hits
    assert off.key_log_hash == on.key_log_hash
    assert off.keys_emitted == on.keys_emitted
