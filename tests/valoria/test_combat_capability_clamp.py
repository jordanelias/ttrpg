"""CAPABILITY IS FLOORED AT ZERO BEFORE A DEFICIT IS TAKEN — M4 / F4, batch E1b (ED-PC-0046).

audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md §4 (E1b).

THE DEFECT. `combat_systems.adef_cap` (owned by `core.adef_cap`) returns a SIGNED number. For a weapon
whose only mode against a harness is a cut, it returns `ADEF_CUT = -0.9` — and that -0.9 is a
SIGMA-DOMAIN CONTROL PENALTY, calibrated for `armor_defeat_sigma`'s +/- scale. It is not a capability
magnitude, and there is no such thing as negative capability.

Two sigma-path sites fed it RAW into a capability DEFICIT:

    reach_threat        :  deficit = max(0, ADEF_THRESHOLD[armor] - cap)
    represent_measure_p :  deficit = max(0, ADEF_THRESHOLD[armor] - cap)

so a pure cutter's deficit at medium read `0.45 - (-0.9) = 1.35` instead of `0.45 - 0 = 0.45` — THREE
TIMES the true shortfall, and the reach-ladder charged the weapon twice for one fact: once as ADEF_CUT
inside `armor_defeat_sigma`, and again as a tripled deficit here.

`core.damage`'s penetration knee had ALREADY been fixed for exactly this, ED-PC-0039, whose comment
states the rule in full: *"'Cannot defeat the harness' is a floor at zero capability, not an unbounded
negative one."* That fix was applied to the knee ONLY. These two sites were left behind. This batch
finishes it.

RED-ON-MAIN, measured on 87856ea (2026-07-29) — the falsifiers, `bardiche` (raw adef_cap -0.9000) vs
an `arming` defender at `medium`:

    combat_systems.reach_threat          0.5275000000000001   ->  0.8425                (clamped)
    combat_systems.represent_measure_p   0.008870713909928251 ->  0.20700755268115265   (clamped, 23.3x)

The represent gate moves 23x rather than 1.6x because its response to the deficit is a STEEP `exp()`
(REPRESENT_DECAY_K 3.5) where the reach decay is shallow and linear (REACH_DECAY_K 0.35). Unclamped, a
bardiche was crowded off measure in 99.1% of fresh engagements against mail.

WHY THE ASSERTIONS ARE PREDICTIONS, NOT CONSTANTS (review R-11.3). "Assert the consumers agree" is an
implementation-consistency check with no stated failing form — it can ship green on broken code. So the
pins here recompute what each function MUST return with `max(0, cap)` substituted, from that function's
own surrounding terms, and compare. Two consequences, both deliberate:
  · a legitimate later recalibration of REACH_DECAY_K / REPRESENT_DECAY_K / ADEF_THRESHOLD / the
    select_mode comparator moves the prediction with the code, and this gate stays green;
  · removing the clamp moves the code AWAY from the prediction, and it goes red naming the site.
The tautology risk that buys is answered head-on: every pin ALSO asserts the function does not match
the UNCLAMPED prediction, by at least a stated separation. That inequality is the literal red-on-main
form, and a prediction helper that silently drifted into re-deriving the broken value would fail it.

THE SITE THAT MUST NOT BE "FIXED". `armor_defeat_sigma` LEGITIMATELY keeps the raw, signed cap, and the
plan says so explicitly. It IS the sigma domain — the term ADEF_CUT was calibrated for — and it is
signed on both sides by design (capability above the tier threshold = control, below = the armour
shields). Clamping it would delete the cutter's control penalty outright. Because "make the three call
sites consistent" is the single most likely wrong fix here, that non-clamp is PINNED, not narrated:
`test_armor_defeat_sigma_keeps_the_raw_signed_capability`.

MUTATION RECORD (§13.3 — a guard that has never failed is decoration). Run 2026-07-29, each mutation
applied to the working tree by file copy, `__pycache__` purged, and the mutant asserted present in the
source before running:
  M0  the unmodified tree (no clamp at either site)  -> 3 failed / 3 passed; both named pins and the
      class sweep, reporting the red values verbatim (0.5275000000000001 / 0.008870713909928251)
  M1  drop the clamp in `reach_threat` only          -> 2 failed / 4 passed; the reach pin and the
      class sweep, naming `combat_systems.reach_threat`; the represent and armor_defeat_sigma pins
      stayed GREEN, so the gate localises the site rather than merely noticing the file changed
  M2  drop the clamp in `represent_measure_p` only   -> 2 failed / 4 passed; the represent pin and the
      class sweep, naming `combat_systems.represent_measure_p`; the reach pin stayed GREEN
  M3  apply the clamp in `armor_defeat_sigma` too    -> 1 failed / 5 passed; the do-not-fix pin, which
      is the whole reason that pin exists (this is the plan's named wrong fix, not a hypothetical)
  M4  `abs(cap)` instead of `max(0, cap)` at both    -> 3 failed / 3 passed; the plausible-looking
      wrong way to "handle negativity", which would turn the worst cutter into the tier's best
      defeater
All four killed; none survived. The M1/M2 split is the load-bearing one: each names only its own site
and leaves the other three tests green, so the gate localises a regression instead of merely noticing
that the file changed.
"""
import math
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import Combatant, WEAPONS  # noqa: E402
from config import CFG  # noqa: E402

# The plan's canonical pair: a pure cutter (no point, no percussion worth the name) against mail.
CUTTER, DEFENDER, TIER = 'bardiche', 'arming', 'medium'

# Minimum separation between the clamped and unclamped predictions for a pin to count as observing
# anything. A pin whose two predictions coincide is watching nothing, and says so instead of passing.
MIN_SEPARATION = 1e-3


def _pair(weapon=CUTTER, armor=TIER):
    return Combatant('longer', weapon=weapon), Combatant('shorter', weapon=DEFENDER, armor=armor)


def _raw_cap_reach(longer):
    """The capability `reach_threat` reads, with reach_threat's own geometry."""
    return S.adef_cap(longer.w, CFG, head=getattr(longer, 'sel_head', None),
                      gap=getattr(longer, 'sel_gap', None),
                      grip=getattr(longer, 'grip_position', 0.0),
                      room=getattr(longer, 'range_avail', 1.0))


def _reach_prediction(longer, defender, clamp):
    """What `reach_threat` must return, recomputed from its OWN surrounding terms, with the capability
    either floored at zero (`clamp=True`, the correct rule) or read raw (`clamp=False`, the defect)."""
    aw = CFG['ADEF_W'][defender.armor]
    if aw == 0.0:
        return 1.0
    cap = _raw_cap_reach(longer)
    cap = max(0.0, cap) if clamp else cap
    deficit = max(0.0, CFG['ADEF_THRESHOLD'][defender.armor] - cap)
    return max(CFG['REACH_THREAT_FLOOR'], 1.0 - CFG['REACH_DECAY_K'] * aw * deficit)


def _represent_prediction(longer, shorter, clamp, measure_gap=None):
    """What `represent_measure_p` must return, recomputed from its OWN surrounding terms. The presenting
    mode is re-derived exactly as the function derives it (ED-PC-0034/0036: open-measure geometry, never
    a live sel_* read), so a recalibration of `select_mode` or of the decay constants moves this
    prediction WITH the code — only the capability floor is under test."""
    aw = CFG['ADEF_W'][shorter.armor]
    if aw <= CFG['ADEF_W'][S.V.TIER_LIGHT]:
        return 1.0
    room = S.range_utilization(longer, measure_gap, CFG)
    sel = S.select_mode(longer, shorter.armor, False, CFG, measure_gap=measure_gap, grip=0.0, room=room)
    cap = S.adef_cap(longer.w, CFG, head=sel.head, gap=sel.gap, grip=0.0, room=room)
    cap = max(0.0, cap) if clamp else cap
    deficit = max(0.0, CFG['ADEF_THRESHOLD'][shorter.armor] - cap)
    base = math.exp(-CFG['REPRESENT_DECAY_K'] * aw * deficit)
    foot = 1.0 + CFG['REPRESENT_FOOT_K'] * (longer.agi - shorter.agi)
    return max(0.0, min(1.0, base * foot))


def _negative_cap_weapons(armor=TIER):
    """The affected class, DERIVED not listed: every roster weapon whose raw armour-defeat capability
    against this tier is negative. 16 members on the current roster (bardiche, falchion, fauchard,
    glaive, greatsword, guandao, hook_sword, katana, nandao, podao, pulwar, sabre, scimitar, shamshir,
    sparr_axe, tachi). A new cutter joins the guard automatically; a re-signed ADEF_CUT empties it, and
    the anti-vacuity assertions below fail loudly rather than passing on an empty sweep."""
    out = []
    for w in sorted(WEAPONS):
        longer, _ = _pair(w, armor)
        if _raw_cap_reach(longer) < 0.0:
            out.append(w)
    return out


# ── the two clamped sites ─────────────────────────────────────────────────────────────────────────

def test_reach_threat_floors_capability_at_zero():
    longer, defender = _pair()
    raw = _raw_cap_reach(longer)
    assert raw < 0.0, (
        f"VACUOUS PIN: {CUTTER}'s raw adef_cap is {raw!r}, not negative — this pin cannot observe the "
        f"defect it exists for. Pick a pure cutter, or ADEF_CUT has been re-signed.")

    clamped = _reach_prediction(longer, defender, clamp=True)
    unclamped = _reach_prediction(longer, defender, clamp=False)
    assert clamped - unclamped > MIN_SEPARATION, (
        f"VACUOUS PIN: clamped and unclamped predictions for reach_threat coincide "
        f"({clamped!r} vs {unclamped!r}) — nothing is under test.")

    got = S.reach_threat(longer, defender, CFG)
    assert got == clamped, (
        f"combat_systems.reach_threat DOES NOT FLOOR CAPABILITY AT ZERO [ED-PC-0046]. "
        f"{CUTTER} vs {DEFENDER}@{TIER}: got {got!r}, clamped-cap prediction {clamped!r}. "
        f"Raw adef_cap is {raw!r} (ADEF_CUT is a sigma-domain control penalty, not a capability "
        f"magnitude); the deficit must be threshold - max(0, cap), never threshold - cap.")
    assert got != unclamped, (
        f"combat_systems.reach_threat still reads the RAW negative capability [ED-PC-0046]: "
        f"got {got!r}, which is exactly the UNCLAMPED prediction {unclamped!r}.")


def test_represent_measure_p_floors_capability_at_zero():
    longer, shorter = _pair()
    clamped = _represent_prediction(longer, shorter, clamp=True)
    unclamped = _represent_prediction(longer, shorter, clamp=False)
    assert clamped - unclamped > MIN_SEPARATION, (
        f"VACUOUS PIN: clamped and unclamped predictions for represent_measure_p coincide "
        f"({clamped!r} vs {unclamped!r}) — nothing is under test.")

    got = S.represent_measure_p(longer, shorter, CFG, TR)
    assert got == clamped, (
        f"combat_systems.represent_measure_p DOES NOT FLOOR CAPABILITY AT ZERO [ED-PC-0046]. "
        f"{CUTTER} vs {DEFENDER}@{TIER}: got {got!r}, clamped-cap prediction {clamped!r}. Its exp() "
        f"response is steep, so an unclamped deficit crowds a cutter off measure in ~99% of fresh "
        f"engagements; the deficit must be threshold - max(0, cap).")
    assert got != unclamped, (
        f"combat_systems.represent_measure_p still reads the RAW negative capability [ED-PC-0046]: "
        f"got {got!r}, which is exactly the UNCLAMPED prediction {unclamped!r}.")


def test_both_sigma_deficit_sites_clamp_for_the_whole_negative_capability_class():
    """The property, not two weapons. Every weapon whose raw capability is negative must read the
    clamped prediction at BOTH sites — so a fix applied to one site, or to one weapon's branch, fails
    here even if the two named pins above were somehow satisfied."""
    weapons = _negative_cap_weapons()
    assert len(weapons) >= 5, (
        f"VACUOUS SWEEP: only {len(weapons)} weapon(s) have a negative raw adef_cap at {TIER} "
        f"({weapons}). The class this clamp protects has essentially emptied — either the roster or "
        f"ADEF_CUT changed, and this guard is no longer watching what it claims to.")
    checked = 0
    for w in weapons:
        longer, shorter = _pair(w)
        r_clamped = _reach_prediction(longer, shorter, clamp=True)
        r_unclamped = _reach_prediction(longer, shorter, clamp=False)
        got_r = S.reach_threat(longer, shorter, CFG)
        assert got_r == r_clamped, (
            f"combat_systems.reach_threat unclamped for {w} vs {DEFENDER}@{TIER} [ED-PC-0046]: "
            f"got {got_r!r}, clamped {r_clamped!r}, unclamped {r_unclamped!r}.")

        p_clamped = _represent_prediction(longer, shorter, clamp=True)
        p_unclamped = _represent_prediction(longer, shorter, clamp=False)
        got_p = S.represent_measure_p(longer, shorter, CFG, TR)
        assert got_p == p_clamped, (
            f"combat_systems.represent_measure_p unclamped for {w} vs {DEFENDER}@{TIER} "
            f"[ED-PC-0046]: got {got_p!r}, clamped {p_clamped!r}, unclamped {p_unclamped!r}.")
        checked += 1
    assert checked == len(weapons) and checked >= 5, (
        f"the sweep asserted on only {checked} of {len(weapons)} weapons")


# ── the site that must NOT be clamped ─────────────────────────────────────────────────────────────

def test_armor_defeat_sigma_keeps_the_raw_signed_capability():
    """DO NOT "consistency-fix" this one. `armor_defeat_sigma` IS the sigma domain — the term ADEF_CUT
    was calibrated against — and it is signed on both sides by design. Clamping it at zero would delete
    the cutter's control penalty entirely (bardiche vs mail: -1.35 -> -0.45, a 0.9 sigma gift to every
    cutter in armour). Plan §4 E1b names this explicitly; this pin is what makes the prohibition
    enforceable instead of a comment someone reads after breaking it."""
    checked = 0
    for w in _negative_cap_weapons():
        longer, defender = _pair(w)
        aw = CFG['ADEF_W'][defender.armor]
        raw = _raw_cap_reach(longer)
        thr = CFG['ADEF_THRESHOLD'][defender.armor]
        raw_form = aw * (raw - thr)
        clamped_form = aw * (max(0.0, raw) - thr)
        assert raw_form < clamped_form - MIN_SEPARATION, (
            f"VACUOUS PIN: raw and clamped forms coincide for {w} ({raw_form!r} vs {clamped_form!r}).")
        got = S.armor_defeat_sigma(longer, defender, CFG)
        assert got == raw_form, (
            f"combat_systems.armor_defeat_sigma MUST KEEP THE RAW SIGNED CAPABILITY [ED-PC-0046] — it "
            f"is the sigma-domain term ADEF_CUT is calibrated for, NOT a capability deficit. {w} vs "
            f"{DEFENDER}@{TIER}: got {got!r}, raw-cap form {raw_form!r}, clamped form {clamped_form!r}. "
            f"If this went red because the max(0, cap) clamp was propagated here for consistency with "
            f"reach_threat/represent_measure_p, that is the wrong fix: revert it.")
        checked += 1
    assert checked >= 5, f"the do-not-clamp sweep asserted on only {checked} weapons"


# ── the clamp must be INERT where capability is already non-negative ──────────────────────────────

def test_clamp_is_inert_for_weapons_that_already_have_non_negative_capability():
    """The fix must be a floor, not a rescale: for every weapon whose raw capability is already >= 0,
    both sites must be byte-identical to the unclamped computation. This is the half of the change that
    carries no balance intent, and it is what bounds the blast radius to the cutter class."""
    checked = 0
    for w in sorted(WEAPONS):
        longer, shorter = _pair(w)
        if _raw_cap_reach(longer) < 0.0:
            continue
        assert S.reach_threat(longer, shorter, CFG) == _reach_prediction(longer, shorter, clamp=False), (
            f"combat_systems.reach_threat moved for {w}, whose capability was ALREADY non-negative "
            f"[ED-PC-0046] — the clamp is a floor at zero, not a rescale.")
        assert S.represent_measure_p(longer, shorter, CFG, TR) == _represent_prediction(
            longer, shorter, clamp=False), (
            f"combat_systems.represent_measure_p moved for {w}, whose capability was ALREADY "
            f"non-negative [ED-PC-0046] — the clamp is a floor at zero, not a rescale.")
        checked += 1
    assert checked >= 20, f"the inertness sweep asserted on only {checked} weapons"


def test_unarmoured_is_untouched_by_construction():
    """A0-safety: ADEF_W['none'] == 0 short-circuits both sites before any capability is read, so the
    clamp cannot reach unarmoured play. Asserted rather than assumed."""
    for w in _negative_cap_weapons():
        longer, shorter = _pair(w, armor='none')
        assert S.reach_threat(longer, shorter, CFG) == 1.0
        assert S.represent_measure_p(longer, shorter, CFG, TR) == 1.0
