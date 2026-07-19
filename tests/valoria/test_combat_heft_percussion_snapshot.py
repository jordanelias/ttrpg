"""Per-weapon heft + percussion snapshot regression (D12c, I8, 2026-07-03) — designs/audit/2026-07-02-
scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md.

I2's acceptance #8 called for a full-roster heft AND percussion snapshot so a future re-anchor's effect is
VISIBLE (a diff against the golden values) rather than silently absorbed. The fixture
(golden_heft_percussion_snapshot.json) pins core.heft_resp(grip=0) and weapon_physics.percussion_authority
(grip=0, room=1 — the ideal circumstance) for every startable weapon (auto-switch FORMS excluded, matching
the convention in test_combat_heft.py / test_combat_capabilities.py).

LIFECYCLE: a deliberate re-anchor (a REC_I_REF/REC_S_REF/SWING_FLOOR retune, a new mass model, etc.) is
expected to move these numbers — regenerate the fixture and record the change reason in the commit (the
same discipline test_combat_element_parity.py uses), never patch a single weapon's row to make a failure
go away without recording why.
"""
import json
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules

import core  # noqa: E402
import weapon_physics as WP  # noqa: E402
from combatant import WEAPONS  # noqa: E402

GOLDEN = os.path.join(os.path.dirname(__file__), 'golden_heft_percussion_snapshot.json')
TOL = 1e-6
CFG = {}   # heft_resp doesn't read cfg (kept for call-site compatibility only — see test_combat_heft.py)

NAMES = [n for n, rec in WEAPONS.items() if 'base' not in rec]   # exclude auto-switched FORMS


def _golden():
    with open(GOLDEN, encoding='utf-8') as f:
        return json.load(f)


def test_fixture_covers_full_roster():
    """Every startable weapon is pinned; a new weapon must be added to the fixture DELIBERATELY."""
    golden = _golden()
    assert set(golden) == set(NAMES), (
        f"fixture/roster drift — missing from fixture: {set(NAMES) - set(golden)}; "
        f"stale in fixture: {set(golden) - set(NAMES)}")


def test_heft_snapshot_matches():
    golden = _golden()
    drift = {}
    for n in NAMES:
        h = core.heft_resp(WEAPONS[n], CFG, grip=0.0)
        if abs(h - golden[n]['heft']) > TOL:
            drift[n] = (h, golden[n]['heft'])
    assert not drift, f"heft_resp drift vs golden snapshot (live, golden): {drift}"


def test_percussion_snapshot_matches():
    golden = _golden()
    drift = {}
    for n in NAMES:
        p = WP.percussion_authority(WEAPONS[n], grip=0.0, room=1.0)
        if abs(p - golden[n]['percussion']) > TOL:
            drift[n] = (p, golden[n]['percussion'])
    assert not drift, f"percussion_authority drift vs golden snapshot (live, golden): {drift}"
