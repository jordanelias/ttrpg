"""CI-tier: the weapon-morphology affordance gates stay synced with the live engine (WS-2 / req 5).

capabilities.py declares the true hard gates (half-sword / gap-thrust / percussive-blow) as pure predicates.
These tests assert each predicate still matches the engine's actual physics, so the registry can never drift
from what the engine enforces.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import capabilities as C  # noqa: E402
import systems as S  # noqa: E402
import core  # noqa: E402
import contact as CT  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402

NAMES = [n for n in WEAPONS if 'base' not in WEAPONS[n]]   # exclude auto-switched FORMS (longsword_halfsword, estoc_halfsword, ...), never a named weapon


def test_halfsword_matches_engine_form_switch():
    for n in NAMES:
        c = Combatant('x', weapon=n)
        switches = S.halfsword_target(c, True, 'heavy') != n
        assert switches == C.allowed('halfsword', n), n


def test_gap_thrust_matches_puncture_path():
    for n in NAMES:
        head = WEAPONS[n]['head']
        puncture = (core.HEAD_MODE.get(head) == 'puncture') or head == 'cut_thrust' or 'point' in S.afforded_heads(WEAPONS[n])
        assert puncture == C.allowed('gap_thrust', n), n


def test_percussive_blow_matches_percussion_mode():
    for n in NAMES:
        head = WEAPONS[n]['head']
        percussion = core.HEAD_MODE.get(head) == 'percussion'
        assert percussion == C.allowed('percussive_blow', n), n


def test_table_covers_full_roster():
    tbl = C.capability_table()
    assert set(tbl) == set(NAMES)
    for n, row in tbl.items():
        assert set(row) == set(C.CAPABILITIES)


def test_pure_cutters_have_no_gates():
    """[UPDATED 2026-07-08, U2/ED-PC-0011/ED-PC-0012] Originally asserted greatsword/sabre have NO alternate-
    mode gates at all. The graded secondary-affordance checks (ED-PC-0011) gave both a real 'point' token, so
    the ORIGINAL premise ("pure cutter" = zero alt-mode capability) is now split into two different cases,
    validated via a 13-agent agonist/antagonist adversarial Workflow against HEMA/physics grounding:
    - greatsword's secondary thrust (half-sword-to-the-gaps) is REAL, historically well-attested capability —
      removed from this test entirely; it is no longer a "pure cutter" and correctly so (see
      test_use_mode_selection_emerges_from_primitives for its accepted changer status).
    - sabre's secondary thrust is a FLAGGED, NOT-YET-FIXED BUG (ED-PC-0012): its own point geometry is weak
      (0.26, and scimitar/falchion share the same class at 0.16/0.23) but core.coupling's DELIVERY['point']
      does not scale by it (unlike 'cut', fixed this session via CUT_AUTH_REF) — verified directly that
      sabre/scimitar/falchion/hook_sword's secondary point ALL score an IDENTICAL coupling at 'light' armour
      regardless of their wildly different geometry, a floor-locked artifact of core._transmit's puncture path,
      not earned capability. sabre is KEPT in this test, deliberately left failing (not silently patched or
      quietly dropped) until ED-PC-0012's THRUST_AUTH_REF fix lands and correctly suppresses this floor-locked
      credit — matching this suite's existing convention (test_gap_game_poleaxe_spikes_plate,
      test_falsifiable_heft_ordering) of a documented, intentionally-red assertion over a silently-adjusted one.
    """
    assert not any(C.capability_table()['sabre'].values()), (
        "sabre should have zero alt-mode gates (a dedicated slashing sabre has no genuine thrust/percussion "
        "capability) but currently shows gap_thrust=True — a KNOWN, FLAGGED bug (ED-PC-0012): core.coupling's "
        "DELIVERY['point'] doesn't scale by the candidate's own thrust magnitude, so sabre's weak (0.26) "
        "incidental point gets full credit. See this test's docstring."
    )


# ── I7b CONTACT AXIS (D8/D9, 2026-07-03) ───────────────────────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_open_contact_matches_grab_available_with_no_opening():
    """I7b acceptance #1: capabilities.open_contact matches contact.grab_available's own exemption
    predicate when there is NO prior opening (opening_created=False) — the only case where the
    exemption is discriminating (WITH an opening, every weapon-wielder is available)."""
    for n in NAMES:
        c = Combatant('x', weapon=n); opp = Combatant('y', weapon='arming')
        assert CT.grab_available(c, opp, False, CFG) == C.allowed('open_contact', n), n


def test_grab_unavailable_without_opening_for_non_exempt_weapon():
    """I7b acceptance #1: a non-exempt weapon-wielder (e.g. arming sword) has NO grab path without a
    prior opening — no grapple path from open measure."""
    c = Combatant('x', weapon='arming'); opp = Combatant('y', weapon='arming')
    assert CT.grab_available(c, opp, False, CFG) is False
    assert CT.grab_available(c, opp, True, CFG) is True


def test_grab_available_dagger_exempt_regardless_of_opening():
    """I7b acceptance #1: dagger-class (short head_len primitive) grabs open-contact — no opening needed."""
    c = Combatant('x', weapon='dagger'); opp = Combatant('y', weapon='arming')
    assert CT.grab_available(c, opp, False, CFG) is True
    assert CT.grab_available(c, opp, True, CFG) is True


class _StubActor:
    """Minimal stand-in exposing only the attributes contact.grab_sigma reads (.w, .strength) — used to
    prove it is blind to any extra 'hardware' keys a weapon dict might carry."""
    def __init__(self, w, strength):
        self.w = w; self.strength = strength


def test_grab_sigma_has_no_hook_hardware_term():
    """I7b acceptance #3 (D9/JD-7): grab_sigma reads ONLY strength + systems.leverage (grip_len/head_len/
    hands) — two weapon dicts identical on those fields but carrying different guard-type/hook-flavoured
    extra keys must produce an IDENTICAL grab_sigma (the retracted hook-hardware axis is inert here)."""
    base = dict(grip_len=0.8, head_len=2.4, hands=1)
    w_plain = dict(base, guard_type='none')
    w_hooked = dict(base, guard_type='lug', hook=True, hook_affordance=True)   # extraneous — must be ignored
    opp = _StubActor(dict(base), 4)
    ga = CT.grab_sigma(_StubActor(w_plain, 5), opp, CFG)
    gb = CT.grab_sigma(_StubActor(w_hooked, 5), opp, CFG)
    assert ga == gb


def test_grab_outcome_menu_reachable_across_seeds():
    """I7b acceptance #2: the branching grab_outcome menu (disarm/throw/pin/control/foot_pin/escape)
    is reachable across seeds — draw many times at a spread of dominance edges."""
    import random
    rng = random.Random(1)
    seen = set()
    for _ in range(4000):
        seen.add(CT.grab_outcome(rng.uniform(-1.5, 1.5), rng, CFG))
    assert seen == set(CT.GRAB_OUTCOMES)


def test_grab_outcome_does_not_touch_beats_counter():
    """I7b acceptance #5: grab_outcome's signature carries no `beats`/loop-state parameter, and is a pure
    (rng-only) resolution — a structural guard that it cannot re-enter the caller's bind inner loop."""
    import inspect
    params = list(inspect.signature(CT.grab_outcome).parameters)
    assert params == ['gsig', 'rng', 'cfg']


def test_clinch_field_deleted_from_every_weapon_record():
    """I7b acceptance #4 (D9): `clinch` is DELETED from every weapons.py record — a forced disposition,
    not retire-OR-residual. Grep-style: no live weapon dict carries the key."""
    for n in NAMES:
        assert 'clinch' not in WEAPONS[n], n


def test_no_pull_capable_or_hook_data_boolean_in_weapons():
    """I7b acceptance #7: no hand-authored pull_capable/hook data boolean exists anywhere in weapons.py —
    the explicit guard against the hollow D9/JD-7 workaround (invisible to the name-literal scanner)."""
    src = open(os.path.join(ENGINE, 'weapons.py'), encoding='utf-8').read()
    assert 'pull_capable' not in src
    assert 'hook_affordance' not in src
