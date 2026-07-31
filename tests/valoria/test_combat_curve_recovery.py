"""CURVATURE -> RECOVERY / MANOEUVRABILITY — channel 2 (ED-PC-0054).

DEFECT (verified on the pre-fix tree): `curvature` had exactly ONE runtime consumer in the whole
engine — `arrest_impulse`, where it REDUCES braceability, i.e. a COST. Its only benefit was
`cut_factor` (damage), wired 2026-07-29 by ED-PC-0051. There was no recovery, tempo or manoeuvrability
consequence anywhere; grep for stuck/stick/extraction over the engine returns nothing.

Jordan, 2026-07-29, two statements that are ONE fact in this engine's vocabulary:
  - "it allows for faster recovery because the weapon isn't getting 'stuck' the same way a straightened
    weapon would"
  - "the curvature of a weapon allows it greater manoeuvreability compared to a contemporary that is a
    purely straight edge"
The engine expresses "how soon can you act or redirect again" through recovery -> tempo debt, so both
are served by ONE term. Two terms for one fact would be the double-count consolidation_v1 §2.3 forbids.

WHERE: `_recovery_mode_commitment`'s `C_swing` branch only. Swing-only because extraction is a CUTTING
problem: a thrust retracts along its own line and has nothing to unstick. `C_thrust` is untouched.

WHY THIS PATHWAY, stated because the previous batch failed on exactly this point: wrapper.py's
`ready[aggressor] -= RECOVERY_TEMPO_K*(commit-2.0)*recoverability_factor(...)` runs on EVERY committed
attack, where `bind_sigma` (ED-PC-0052) ran ~1.2x per fight and was measured aggregate-inert. Throughput
was checked BEFORE building this time.

WHY THE FORM IS SAFE, and this is the third scaling term this session so it is worth naming: `curvature`
is DIMENSIONLESS and bounded [0,1] by construction (geometry.py: "straight edge = 0 ... strongly curved
(shamshir) = 1"). So `1 - K*cv` is bounded in [1-K, 1] and cannot tail. The two earlier terms both
mis-scaled because their inputs were unbounded — `S_g` carries units (a linear bind differential was
dimensionally incoherent) and `I_g` spans ~1000x (a linear close-quarters multiplier read guandao 48.9).
Neither failure mode is reachable here.

THREE DISCLOSURES FROM THIS BATCH'S OWN ADVERSARIAL REVIEW, none incidental:

 1. THE pc-CONFOUND AMPLIFIES THIS TERM. `_recovery_mode_commitment` blends
    `pc*C_thrust + (1-pc)*C_swing`, and `point_concentration` anti-correlates with curvature at -0.729
    across 42 bladed weapons (the tip-data double-count in curvature_and_bind_model_v1.md §4). Curved
    weapons are therefore ALREADY weighted into the swing branch, which is exactly where this discount
    applies: measured (1-pc) = 0.70..0.92 for the curved family, so the effective discount is 70-92% of
    nominal. THIS TERM MUST BE RE-MEASURED when channels 3-4 correct that tip data, because its
    effective magnitude rides on a known-suspect correlation.
 2. ONE DISCOUNT BUYS THREE THINGS. `_recovery_mode_commitment` feeds (a) `recoverability_factor` ->
    tempo debt per committed attack, (b) the ED-PC-0027 `T_vuln` exposure window, and (c) `select_mode`
    via `EXPOSE_SELECT_K`. So a curved weapon gets faster recovery AND a shorter undefended window AND
    more cut-selection, all in the same direction. Physically coherent — a shorter recovery IS a shorter
    window — but ~3x more potent than its K suggests, which is why K is small.
 3. CURVATURE NOW HAS TWO BENEFITS AND ONE COST (damage via cut_factor, recovery here; braced stop-hits
    via arrest_impulse). Not a double-count — edge presentation, extraction and braceability are three
    distinct facts, which is how Jordan enumerated them — but the NET is no longer obviously negative,
    so test_curvature_net_is_not_a_runaway pins the aggregate.

GROUNDING: [ASSERTED — first-principles], matching recoverability_factor's own existing tag. The
draw-cut/slicing advantage is well attested; the specific EXTRACTION claim ("does not wedge, so the
arrest is cheaper") is physical reasoning, NOT treatise-sourced, and is not dressed up as more.

PRE-REGISTERED PREDICTION (written before the field was measured, per CLAUDE.md §0.1 #4 — the author
wanting a particular answer is the control that matters here): curved cutters gain +1 to +3 pp in the
civilian sidearm field, the rapier stays ~flat, curved battlefield polearms rise slightly. The measured
outcome is recorded in the ED-PC-0054 ledger entry whether or not it matched.

FALSIFIERS — mutations run against these guards, each naming its target:
  - CURVE_RECOVERY_K = 0                      -> guards 1, 3, 5 red (the pre-fix engine). NOT guard 2:
    that is the ZERO ANCHOR and correctly passes at K=0, which is what makes it a meaningful pin rather
    than a restatement of guard 1. An earlier draft of this list claimed "guards 1, 2"; the mutation
    run corrected it.
  - apply the discount to C_thrust too        -> guard 3 red (a thrust has nothing to unstick).
  - key it on something unbounded (I_g, S_g)  -> guards 2 AND 4 red (the bounded-input pin, plus the
    zero anchor, because an I_g-keyed term would credit straight blades too).
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S     # noqa: E402
import combatant as C          # noqa: E402
import geometry as G           # noqa: E402
from config import CFG         # noqa: E402


def _cfg_with(**over):
    d = dict(CFG)
    d.update(over)
    return d


def _curv(n):
    return G.bake(C.WEAPONS[n]['geometry'])['curvature']


def _startable():
    return {n: w for n, w in C.WEAPONS.items() if 'base' not in w}


def test_the_population_is_real():
    """Premise pin: curvature must still span a usable range AND be dimensionless/bounded — the
    property that makes this form safe (see the module docstring)."""
    cvs = [G.bake(w['geometry'])['curvature'] for w in _startable().values()]
    assert min(cvs) == 0.0, "no straight-edged weapon remains as the zero anchor"
    assert 0.5 < max(cvs) <= 1.0, f"curvature no longer spans a usable bounded range: max {max(cvs)}"


def test_a_curved_blade_recovers_faster_than_a_straight_one():
    """GUARD 1 (the defect pin, red on main). Curvature must reduce the swing-arrest commitment.
    Isolated by ablating the term on the SAME weapon — the mistake ED-PC-0052 made was comparing two
    different weapons, which lets unrelated terms supply the difference."""
    off = _cfg_with(CURVE_RECOVERY_K=0.0)
    checked = 0
    for n in ('shamshir', 'pulwar', 'scimitar', 'sabre', 'tachi', 'katana'):
        c = C.Combatant('x', weapon=n)
        live = S.recoverability_factor(c, CFG)
        ablated = S.recoverability_factor(c, off)
        assert live < ablated - 1e-12, (
            "%s (curvature %.2f) recovers no better with the curve term live (%.6f vs %.6f ablated). "
            "Mutation that produces this: CURVE_RECOVERY_K = 0, which IS the pre-fix engine."
            % (n, _curv(n), live, ablated))
        checked += 1
    assert checked == 6


def test_a_straight_blade_gains_nothing():
    """GUARD 2 — the zero anchor. A purely straight edge must be byte-identical to the pre-fix engine:
    this is a curvature BENEFIT, not a global recovery buff."""
    off = _cfg_with(CURVE_RECOVERY_K=0.0)
    for n in ('rapier', 'estoc', 'longsword', 'spear', 'dagger'):
        assert _curv(n) == 0.0, "%s is no longer straight — pick a different zero anchor" % n
        c = C.Combatant('x', weapon=n)
        assert S.recoverability_factor(c, CFG) == S.recoverability_factor(c, off), (
            "%s has curvature 0 yet its recovery moved — the term is not keyed on curvature." % n)


def test_only_the_swing_branch_is_discounted():
    """GUARD 3 — swing-only. Isolated by driving sel_pc to 1.0 (a pure thrust), where the blend is
    entirely C_thrust: the curve term must then be inert even for the most curved weapon."""
    off = _cfg_with(CURVE_RECOVERY_K=0.0)
    w = C.WEAPONS['shamshir']
    live_t = S._recovery_mode_commitment(w, 0.0, CFG, sel_pc=1.0)
    abl_t = S._recovery_mode_commitment(w, 0.0, off, sel_pc=1.0)
    assert live_t == abl_t, (
        "a PURE THRUST (sel_pc=1.0) on the most curved weapon still gets the curve recovery discount "
        "(%.6f vs %.6f). Mutation that produces this: applying it outside the C_swing branch."
        % (live_t, abl_t))
    live_s = S._recovery_mode_commitment(w, 0.0, CFG, sel_pc=0.0)
    abl_s = S._recovery_mode_commitment(w, 0.0, off, sel_pc=0.0)
    assert live_s < abl_s - 1e-12, (
        "a pure SWING on the most curved weapon is not discounted — the term is inert where it should "
        "be live.")


def test_the_discount_is_bounded_by_construction():
    """GUARD 4 — the pin that would have caught BOTH of this session's earlier mis-scaled terms. The
    factor must stay within [1-K, 1] for every weapon, which holds because curvature is dimensionless
    and bounded. Re-key this on an unbounded quantity and the band is breached."""
    off = _cfg_with(CURVE_RECOVERY_K=0.0)
    K = CFG['CURVE_RECOVERY_K']
    worst = 1.0
    for n in _startable():
        c = C.Combatant('x', weapon=n)
        a, b = S.recoverability_factor(c, CFG), S.recoverability_factor(c, off)
        if b > 1e-12:
            worst = min(worst, a / b)
    assert (1.0 - K) - 1e-9 <= worst <= 1.0, (
        "the worst-case recovery ratio %.6f escapes the [1-K, 1] = [%.3f, 1.0] band the bounded-"
        "curvature form guarantees. Mutation: keying the term on an unbounded input (I_g, S_g)."
        % (worst, 1 - K))


def test_curvature_net_is_not_a_runaway():
    """GUARD 5 — the aggregate pin from disclosure 3. Curvature now carries TWO benefits against ONE
    cost. Distinct facts, so not a double-count, but the net must stay bounded."""
    off = _cfg_with(CURVE_RECOVERY_K=0.0)
    sh = C.Combatant('x', weapon='shamshir')
    ratio = S.recoverability_factor(sh, CFG) / S.recoverability_factor(sh, off)
    assert 0.85 <= ratio < 1.0, (
        "the most curved weapon's recovery credit is %.4f of its un-credited value; outside [0.85, 1.0) "
        "this stops being a modest situational benefit. K is [SIM-CALIBRATE] but the ORDER is not."
        % ratio)
