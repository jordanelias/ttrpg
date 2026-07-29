"""
engine/tests/test_parliamentary_transfer_bridge.py — OI-04 Territory Transfer motion oracle

Guards `engine.cross_scale.parliamentary_bridge._derive_transfer` / `_run_transfer_motion` — the
THIRD Parliamentary motion path wired 2026-07-29 (ED-IN-0091 plan §3 Wave 2, 07-14 Tier-1 #2 /
GAP-A1). Before this, `systems.factions.sim.parliamentary_transfer.propose_transfer` had zero
callers, so a faction's lost territory was a one-way ratchet (test_f7_smoke_oracle.py's
`test_f7_hafenmark_elimination_lockout` documented exactly this: "the only restoration path,
parliamentary_transfer, is never called... Trips when a comeback path lands").

Scope: this file falsifies the NEW derivation/wiring in isolation. It does NOT touch or re-record
any IN-family campaign golden (test_f7_smoke_oracle.py / test_mc_v18_regression.py /
test_parliamentary_bridge.py's flag-ON pins / test_echo_transport.py's flag-ON pins) — those move
because this wiring now consumes extra `world.rng` draws whenever the auto-CB qualifies, and their
re-record is the World lane's declared job (wf_wave2_seams.js header correction / plan §3 Wave 2
phase 2), not this lane's (file-ownership table: "L-transfer ->
engine/cross_scale/parliamentary_bridge.py + systems/factions/sim/*"; golden test files are WORLD's).
"""
import os
import sys
import random

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.autoload import game_state
from engine.cross_scale import parliamentary_bridge as pb
from engine.cross_scale import echo_transport
from systems.factions.sim import parliamentary_transfer


def _scheduled_world(seed):
    """A fresh world with the echo scheduler attached (ECHO_TRANSPORT on shape) — the state
    run_parliamentary_scene requires to do anything at all."""
    w = game_state.create_world(seed=seed)
    w.echo_scheduler = echo_transport.make_scheduler()
    w.key_log = w.echo_scheduler.log
    w._echo_key_seq = 0
    return w


# ── _derive_transfer: no fabrication, canon-cited derivation ──────────────────────────────────

def test_derive_transfer_none_when_crown_at_starting_territory_count():
    """Crown starts at exactly 6 territories (game_state.STARTING_OWNER); the auto-CB requires
    STRICTLY fewer than PARL_CROWN_RESTORATION_TERRITORY_MAX (6, parliamentary_transfer.py §3), so
    a fresh world derives no transfer candidate at all — 'no behaviour change when no CB qualifies'
    (plan §3 Wave 2 item 1)."""
    w = game_state.create_world(seed=42)
    assert len(w.factions['Crown'].territories) == 6
    assert pb._derive_transfer(w) is None


def test_derive_transfer_none_for_non_crown_factions_with_no_ledger():
    """No faction other than Crown has ANY CB source without a populated `world.casus_belli`
    ledger (parliamentary_transfer.py's own [ASSUMPTION] banner) — confirms this derivation reads
    that fact rather than inventing eligibility for Church/Hafenmark/Varfell."""
    w = game_state.create_world(seed=0)
    # Even if Church/Hafenmark/Varfell are territorially weak, they have no CB source at all.
    for name in ('Church', 'Hafenmark', 'Varfell'):
        assert parliamentary_transfer._available_cb(name, 'Crown', w) == []


def test_derive_transfer_finds_crown_restoration_cb_and_picks_largest_holder():
    """Once Crown drops under 6 territories, the auto-CB qualifies (crown_constitutional_restoration
    -> 'adversarial' only per parliamentary_transfer.py's own _MODE_CB table). Target selection is
    NOT canon-determined (no site in parliamentary_transfer_v30.md §1-4 names one), so the [SEED]
    default (largest current non-Crown holder, ties by name) is pinned here as a KNOWN-ANSWER case,
    not asserted as canon."""
    w = game_state.create_world(seed=42)
    w.factions['Crown'].territories = w.factions['Crown'].territories[:5]  # drop to 5, below 6
    # Known starting holdings at seed-agnostic STARTING_OWNER: Church=1 (T9, floor-protected),
    # Hafenmark=4 (T7,T8,T10,T17), Varfell=4 (T4,T11,T12,T13) -> tie broken by holder name asc
    # ('Hafenmark' < 'Varfell'); within Hafenmark the alphabetically-first territory id is 'T10'.
    result = pb._derive_transfer(w)
    assert result == ('Crown', 'T10', 'adversarial')


def test_derive_transfer_never_targets_last_territory_protected_holder():
    """Church holds a single territory (T9) at world creation — the §1.3 last-territory floor
    means _derive_transfer must never propose Church as a holder, matching the block
    propose_transfer itself would apply anyway (this derivation mirrors, not re-implements, that
    gate)."""
    w = game_state.create_world(seed=42)
    w.factions['Crown'].territories = w.factions['Crown'].territories[:5]
    result = pb._derive_transfer(w)
    assert result is not None
    _, target_territory, _ = result
    assert target_territory not in w.factions['Church'].territories


# ── _run_transfer_motion / run_parliamentary_scene: no-op when no CB qualifies ─────────────────

def test_run_transfer_motion_is_noop_without_qualifying_cb():
    w = _scheduled_world(seed=42)
    assert pb._run_transfer_motion(w, w.rng) is None


def test_run_parliamentary_scene_carries_transfer_key_and_is_none_when_no_cb():
    """The bridge's return dict always carries a 'transfer' key (present on both the resolved and
    unresolved-vote branches, per the OI-04 docstring), None when no CB qualifies."""
    w = _scheduled_world(seed=42)
    out = pb.run_parliamentary_scene(w, w.rng)
    assert 'transfer' in out
    assert out['transfer'] is None


# ── Falsifier (plan §3 Wave 2 item 3): a Success actually moves the territory ──────────────────

def test_transfer_regain_actually_happens_bounded_search():
    """Direct unit-level falsifier (canon: `assert checked >= 1`, CLAUDE.md §0.1 point 2): construct
    a world where the auto-CB qualifies, then search a bounded range of RNG seeds for a
    Success/Overwhelming outcome and assert BOTH halves of 'the territory list changes hands' —
    Faction.territories (what propose_transfer's own §1.2 table names) AND Territory.owner (what
    engine/autoload/victory.py + engine/mc_v18.py's fallback winner scoring actually read — the
    [bugfix] this task shipped alongside the wiring, since a 'regain' invisible to victory scoring
    is not a regain)."""
    checked = 0
    transferred_seen = 0
    for seed in range(300):
        w = _scheduled_world(seed=1)  # fixed world shape; only the roll rng varies
        w.factions['Crown'].territories = w.factions['Crown'].territories[:5]
        rng = random.Random(seed)
        out = pb.run_parliamentary_scene(w, rng)
        tr = out.get('transfer')
        checked += 1
        if tr is None:
            continue
        assert tr['initiator'] == 'Crown'
        assert tr['cb_used'] == 'crown_constitutional_restoration'
        if tr['status'] == 'transferred':
            transferred_seen += 1
            target = tr['target_territory']
            assert target in w.factions['Crown'].territories, \
                "propose_transfer reported 'transferred' but Faction.territories was not updated"
            assert w.territories[target].owner == 'Crown', \
                "propose_transfer reported 'transferred' but Territory.owner was not updated"
            break
    assert checked >= 1, "the bounded search never even ran the derivation — falsifier is vacuous"
    assert transferred_seen >= 1, \
        f"no Success/Overwhelming transfer observed across {checked} seeded attempts — regain path unreachable"


def test_transfer_failure_does_not_move_territory():
    """The negative control for the falsifier above: a Failure/Partial outcome must NOT move the
    territory (propose_transfer §1.2) — searched the same bounded way."""
    checked = 0
    failure_seen = 0
    for seed in range(300):
        w = _scheduled_world(seed=1)
        w.factions['Crown'].territories = w.factions['Crown'].territories[:5]
        rng = random.Random(seed)
        before = set(w.factions['Hafenmark'].territories)
        out = pb.run_parliamentary_scene(w, rng)
        tr = out.get('transfer')
        checked += 1
        if tr is None:
            continue
        if tr['status'] in ('failed', 'partial'):
            failure_seen += 1
            assert set(w.factions['Hafenmark'].territories) == before, \
                "a non-transferred outcome moved the holder's territory list"
            break
    assert checked >= 1
    assert failure_seen >= 1, f"no Failure/Partial outcome observed across {checked} seeded attempts"


# ── golden_status control: the pinned F7/regression seeds are documented, not asserted here ────

def test_ecs_flag_off_bridge_stays_byte_exact_no_op():
    """ECHO_TRANSPORT off (no echo_scheduler) — the bridge (and therefore the transfer motion
    inside it) never runs at all, matching the byte-exact contract test_echo_transport.py already
    pins for the flag-OFF path."""
    w = game_state.create_world(seed=0)
    assert pb.run_parliamentary_scene(w, w.rng) == {"resolved": False, "reason": "ECHO_TRANSPORT off"}


# ── Wave-2 canon gate: §1.1 Frequency (1/arc/faction) + Cost (CB consumption on attempt) ────────

def test_propose_transfer_blocks_a_second_attempt_in_the_same_arc():
    """parliamentary_transfer_v30.md §1.1 (:27 Frequency): once an initiator has attempted
    Parliamentary Transfer this arc, a second attempt in the SAME arc is blocked at the
    declaration stage -- no CB consumed, no roll made (checked via world.rng state parity)."""
    w = game_state.create_world(seed=42)
    w.factions['Crown'].territories = w.factions['Crown'].territories[:5]  # qualifies the auto-CB
    r1 = parliamentary_transfer.propose_transfer('Crown', 'T10', 'adversarial', w, rng=w.rng)
    assert r1.status != 'invalid', f"first attempt should be a real (non-invalid) attempt: {r1}"
    assert w.factions['Crown'].parl_transfer_used_this_arc is True, (
        "an attempt (CB qualified, roll made) must set the arc-used flag")

    rng_state_before = w.rng.getstate()
    r2 = parliamentary_transfer.propose_transfer('Crown', 'T10', 'adversarial', w, rng=w.rng)
    assert r2.status == 'blocked'
    assert any('§1.1 Frequency' in n for n in r2.notes), f"expected a §1.1 Frequency note, got: {r2.notes}"
    assert w.rng.getstate() == rng_state_before, "a gated-out attempt must not consume world.rng"


def test_reset_arc_clears_the_frequency_gate():
    """Faction.reset_arc() (game_state.py, called by season_manager.advance_season on an arc
    boundary) clears parl_transfer_used_this_arc, mirroring council_used_this_arc's own reset."""
    w = game_state.create_world(seed=42)
    w.factions['Crown'].parl_transfer_used_this_arc = True
    w.factions['Crown'].reset_arc()
    assert w.factions['Crown'].parl_transfer_used_this_arc is False


def test_derive_transfer_excludes_an_arc_gated_initiator():
    """The bridge's derivation (not just propose_transfer's own gate) must exclude an
    already-arc-gated initiator, so a gated-out season never even proposes a doomed-to-block
    motion (plan requirement: 'a gated-out season is byte-identical to today')."""
    w = game_state.create_world(seed=42)
    w.factions['Crown'].territories = w.factions['Crown'].territories[:5]
    assert pb._derive_transfer(w) is not None, "fixture assumption: Crown should qualify pre-gate"
    w.factions['Crown'].parl_transfer_used_this_arc = True
    assert pb._derive_transfer(w) is None, (
        "an arc-gated initiator must be excluded from candidate derivation, not merely blocked "
        "once selected")


def test_gated_out_season_matches_no_qualifying_cb_season_byte_for_byte():
    """The falsifier for 'a gated-out season is byte-identical to today': with the ONLY
    qualifying initiator (Crown) already arc-gated, run_parliamentary_scene's transfer leg must
    behave EXACTLY like a season where no CB qualifies at all -- same return shape, same
    zero-rng-draw contract."""
    w_gated = _scheduled_world(seed=1)
    w_gated.factions['Crown'].territories = w_gated.factions['Crown'].territories[:5]
    w_gated.factions['Crown'].parl_transfer_used_this_arc = True

    w_no_cb = _scheduled_world(seed=1)  # Crown at starting 6 territories -- no CB qualifies either

    rng_gated = random.Random(7)
    rng_no_cb = random.Random(7)
    transfer_gated = pb._run_transfer_motion(w_gated, rng_gated)
    transfer_no_cb = pb._run_transfer_motion(w_no_cb, rng_no_cb)

    assert transfer_gated is None and transfer_no_cb is None
    assert rng_gated.getstate() == rng_no_cb.getstate(), (
        "a gated-out season must consume exactly as many world.rng draws as a no-qualifying-CB "
        "season (zero) -- not byte-identical otherwise")


if __name__ == '__main__':
    fns = [v for k, v in sorted(globals().items()) if k.startswith('test_') and callable(v)]
    p = f = 0
    for fn in fns:
        try:
            fn(); p += 1
        except AssertionError as e:
            f += 1; print(f"FAIL {fn.__name__}: {e}")
    print(f"{p} passed, {f} failed")
    sys.exit(1 if f else 0)
