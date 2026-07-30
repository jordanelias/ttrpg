"""NATIVE EDGE QUALITY MUST BE CONSUMED — A7a channel 1 (M6, ED-PC-0051).

DEFECT (verified red on the pre-fix tree): `core.coupling` scales a cut by its derived edge quality
ONLY for the bare `'cut'` token — and core.py's own comment records that this token "is NEVER a
weapon's own native head" (it is the incidental-edge token a rapier or a mace picks up). The two
NATIVE cut heads, `curved_cut` (12 weapons) and `straight_cut` (4), were never scaled at all. 16
weapons — 31% of the roster — coupled identically regardless of their edge.

It is worse than an omission, because the scaling that DOES exist could not grade them either. The
native cut-eff population runs 0.710 (hook_sword) to 1.330 (shamshir), entirely ABOVE
`CUT_AUTH_REF = 0.70`, so `min(1.0, eff/CUT_AUTH_REF)` is identically **1.000** for all 16. The
defect register's own proposed fix was that expression, and it is provably a NO-OP.

MEASURED CONSEQUENCE, which is what makes this the top balance defect rather than a tidy-up: the four
keenest edges in the game were four of the five worst performers in the only context they exist for.
Against the civilian sidearm field (the settlement-legal 1H non-blunt roster, per Jordan's carry
ruling of 2026-07-29): shamshir eff 1.330 -> 41.5%, pulwar 1.240 -> 35.5% (last), sabre 1.180 ->
38.2%, scimitar 1.220 -> 47.9%, against rapier (a POINT) at 80.6%.

THE FORM, and why it is not the register's sketch (Jordan, 2026-07-29):
  - "cutters need to be excellent in contexts where they can CUT ie unarmoured and light armour"
  - "the curve extends the amount of cutting edge with which to do damage"
The second is ALREADY derived — `geometry.cut_factor = edge_keenness * (1 + 0.45*tanh(2*curvature))`
adds up to +45% for curvature — and was simply discarded downstream. So this batch does not invent a
quantity; it CONSUMES one the geometry layer already computes. The first is why the benefit is
material-gated: a superior edge pays off in proportion to how much the target yields to an edge,
which is the already-owned `_transmit('shear', mat)` normalised to its unarmoured value
(none 1.000 / cloth 0.618 / mail 0.277 / plate 0.193). A POOR edge, by contrast, is poor everywhere.

Anchored on the KATANA, whose derived cut_factor is exactly 1.00 — a canonical attested single-edged
cutter, following this module's own precedent of anchoring a reference on a named weapon
(CUT_AUTH_REF <- hook_sword, THRUST_AUTH_REF <- bear_spear, PERC_AUTH_REF_SOFT <- weakest hammer).

SCOPE — this is channel 1 of THREE effects Jordan grounded on 2026-07-29. The other two are specified
and deliberately NOT built here (one concern per batch):
  (2) a curved blade recovers faster because it does not get stuck — currently NO consumer anywhere.
  (3) a curved thrust also cuts, because the thrust axis is not perpendicular to the swing axis —
      currently INVERTED, `thrust_factor` reads shamshir 0.03 and geometry.py documents that as
      "correctly collapse toward 0". Also complicates `cut_thrust_arm`'s binary shear-OR-puncture
      max(), which ED-PC-0050 has just built the heft split on.

FALSIFIERS — mutations run against these guards, each naming its target:
  - revert to `min(1.0, eff/CUT_AUTH_REF)` for native heads -> guards 1 and 2 red (the no-op).
  - make the benefit unconditional on material               -> guard 3 red.
  - make the PENALTY material-gated too                      -> guard 4 red.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combatant as C          # noqa: E402
import core                    # noqa: E402
import vocabulary as V         # noqa: E402

NATIVE_CUT_HEADS = ('curved_cut', 'straight_cut')


def _native_cutters():
    return {n: w for n, w in C.WEAPONS.items()
            if 'base' not in w and w.get('head') in NATIVE_CUT_HEADS}


def test_the_population_is_real_and_sits_above_the_incidental_reference():
    """The premise pin. If the native cut-eff population ever straddles CUT_AUTH_REF, the 'the old
    expression is a no-op' finding stops being true and this file's reasoning must be revisited."""
    effs = [w['geo']['cut'] for w in _native_cutters().values()]
    assert len(effs) >= 15, f"native-cutter population collapsed to {len(effs)}"
    assert min(effs) > core.CUT_AUTH_REF, (
        f"the native cut-eff population now dips below CUT_AUTH_REF ({min(effs)} <= "
        f"{core.CUT_AUTH_REF}); the no-op finding this batch rests on no longer holds as stated."
    )


def test_native_edge_quality_changes_coupling():
    """GUARD 1 (the defect pin, red on main). Two native cutters with different edges must not couple
    identically. On main every one of the 16 read the same multiplier, 1.000."""
    for tier in ('none', 'light'):
        keen = core.coupling('curved_cut', tier, eff=1.330)
        dull = core.coupling('curved_cut', tier, eff=0.710)
        assert keen > dull + 1e-9, (
            f"a shamshir's edge (1.330) couples the same as a hook_sword's (0.710) at {tier}: "
            f"{keen:.6f} vs {dull:.6f}. Mutation that produces this: scaling native cut heads by "
            "min(1.0, eff/CUT_AUTH_REF), whose population is entirely above the reference so the "
            "expression is identically 1.0."
        )


def test_the_grading_is_monotone_across_the_whole_native_population():
    """GUARD 2 — the ordering must hold across the real roster, not just at two hand-picked points,
    with a counted-assertion floor so the loop cannot pass vacuously."""
    rows = sorted((w['geo']['cut'], n) for n, w in _native_cutters().items())
    checked = 0
    for (e_lo, n_lo), (e_hi, n_hi) in zip(rows, rows[1:]):
        if e_hi <= e_lo + 1e-12:
            continue
        c_lo = core.coupling(C.WEAPONS[n_lo]['head'], 'none', eff=e_lo)
        c_hi = core.coupling(C.WEAPONS[n_hi]['head'], 'none', eff=e_hi)
        checked += 1
        assert c_hi > c_lo + 1e-12, (
            f"{n_hi} (eff {e_hi}) does not out-couple {n_lo} (eff {e_lo}) unarmoured: "
            f"{c_hi:.6f} vs {c_lo:.6f}"
        )
    assert checked >= 10, f"only {checked} ordered pairs exercised — the loop asserted almost nothing"


def test_a_superior_edge_pays_off_only_where_the_target_can_be_cut():
    """GUARD 3 (Jordan's constraint, 2026-07-29: 'excellent in contexts where they can CUT ie
    unarmoured and light armour'). The keen-vs-dull ADVANTAGE must shrink as the target stops
    yielding to an edge — a razor edge is no help against plate."""
    def advantage(tier):
        keen = core.coupling('curved_cut', tier, eff=1.330)
        ref = core.coupling('curved_cut', tier, eff=1.000)   # the katana reference
        return keen / ref
    adv = {t: advantage(t) for t in ('none', 'light', 'medium', 'heavy')}
    assert adv['none'] > adv['light'] > adv['medium'] > adv['heavy'], (
        f"the keen-edge advantage is not material-conditioned: {adv}. Mutation that produces this: "
        "applying the benefit unconditionally instead of gating it on shear yield."
    )
    # The plate bound is DERIVED FROM THE RESIST TABLE, not chosen. Shear yield falls 1.000 -> 0.193
    # from none to plate, so a benefit gated once on shear yield must shrink by that same factor;
    # allowing 1.5x slack for the ratio's own arithmetic gives 0.29. This replaces an absolute
    # `< 1.02` threshold the first draft of this file asserted, which was invented rather than
    # derived and which the linear gate legitimately fails (it measures 1.064). Recorded rather than
    # quietly relaxed: the form is right, the original threshold was mine and was wrong.
    slack = 1.5 * core._shear_yield('plate')
    assert (adv['heavy'] - 1.0) <= (adv['none'] - 1.0) * slack, (
        f"the plate advantage {adv['heavy']:.4f} is not gated down from the unarmoured "
        f"{adv['none']:.4f} by the resist table's own shear-yield factor: {adv}. Mutation that "
        "produces this: applying the benefit unconditionally."
    )
    assert adv['none'] > 1.20, (
        f"a superior edge buys only {adv['none']:.3f}x unarmoured, where it should be at its best. {adv}"
    )


def test_a_poor_edge_is_poor_everywhere():
    """GUARD 4 — the complementary pin, and the asymmetry is deliberate. A keen edge's BENEFIT is
    gated on the target yielding; a poor edge's PENALTY is not. A badly-edged weapon does not become
    a good cutter just because the target is unarmoured."""
    for tier in ('none', 'light', 'medium', 'heavy'):
        poor = core.coupling('curved_cut', tier, eff=0.710)
        ref = core.coupling('curved_cut', tier, eff=1.000)
        assert poor < ref - 1e-9, (
            f"a poor edge (0.710) is not penalised vs the katana reference at {tier}: "
            f"{poor:.6f} vs {ref:.6f}. Mutation that produces this: gating the penalty on material "
            "the way the benefit is gated."
        )


def test_the_incidental_cut_token_is_untouched():
    """The bare 'cut' token keeps its OWN reference and its own cap — that scaling is correct and is
    not this batch's concern. Its population (an incidental edge on a point or blunt weapon) runs
    0.02-0.50, genuinely below CUT_AUTH_REF, so min(1.0, eff/0.70) grades it properly."""
    lo = core.coupling('cut', 'none', eff=0.02)
    hi = core.coupling('cut', 'none', eff=0.50)
    assert lo < hi, "the incidental-cut token's own grading broke"
    capped_a = core.coupling('cut', 'none', eff=1.20)
    capped_b = core.coupling('cut', 'none', eff=1.30)
    assert abs(capped_a - capped_b) < 1e-12, (
        "the bare 'cut' token's cap at 1.0 was removed; this batch must not change that token"
    )
