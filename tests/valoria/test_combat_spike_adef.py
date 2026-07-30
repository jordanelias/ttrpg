"""THE BLUNT-COMPOSITE SPIKE'S ARMOUR DEFEAT — E3a guards (M3/F3, ED-PC-0049).

DEFECT (verified red on the pre-fix tree): `config.py`'s `ADEF_POINT` carries the ED-1080 calibration
note *"set so the poleaxe spike adef ≈ its hammer."* PC-5 later introduced `thrust_authority` — a
point-to-hand LEVER de-rating whose grounding is that a reach-thrust delivered at full extension
cannot press a harness the way a short/half-sword thrust can — and applied it to every `point` head.
That silently halved the poleaxe's spike **after** the calibration it was set against:

    poleaxe @heavy   sel_head 'point'  sel_gap 0.8200   adef_cap 0.6013   vs ADEF_THRESHOLD 0.72
    armor_defeat_sigma = 1.7 * (0.6013 - 0.72) = -0.20  ->  PLATE SHIELDS AGAINST THE POLEAXE

on the very mode `select_mode` picks. It is a CATEGORY ERROR, and `core.adef_cap`'s own line-400
comment already states the correct principle in so many words: *"NOT applied to the blunt-puncture
beak (a poleaxe's spike authority is its percussion energy, already in puncture_pressure)."* That
exemption was written for the branch where a blunt-composite resolves its NATIVE blunt head — and
never reached the branch where `select_mode` commits it to the spike, which is precisely when the
spike is the thing being scored. A two-handed percussive blow driving a concentrated spike is not a
fencer's extended thrust; nothing about the lever de-rating applies to it.

THE GUARDS:
  1. `test_blunt_composite_spike_is_not_derated_by_the_reach_lever` — the MECHANISM invariant, and
     the one an epsilon cannot satisfy: for a NATIVE-BLUNT weapon, the selected-point armour-defeat
     capability must not be a function of `thrust_authority` at all. Asserted by varying
     `thrust_authority`'s output and requiring the result to be unmoved.
  2. `test_poleaxe_spike_clears_the_plate_threshold` — the CONSEQUENCE pin, at the live selected
     mode and the live selected gap (not a synthetic call): the mode `select_mode` actually picks
     must not leave plate shielding against the poleaxe.
  3. `test_spike_approaches_its_own_hammer` — the ED-1080 contract, pinned as a RATIO (>= 0.78) so
     it cannot be satisfied by an epsilon over the threshold, PLUS a dependence assertion that the
     percussion-puncture path is live. It is pinned at the parity this batch's surgical fix actually
     reaches, NOT at 1.0, because full parity is NOT reachable without re-anchoring `ADEF_POINT`
     roster-wide — a balance change this batch has no mandate for. See the module note below; the
     residual is escalated, not silently absorbed.
  4. `test_a_true_reach_thrust_is_still_derated` — the COMPLEMENTARY pin. The fix must not delete
     the PC-5 lever for the weapons it was actually grounded on. A spear/rapier reach-thrust must
     still be de-rated; only the blunt-composite spike is exempt.

BALANCE ESCALATED TO JORDAN, NOT DECIDED HERE (plan §11). After this fix the poleaxe spike reads
1.0200 against its own hammer's 1.3000 — 78%, up from 46%, clearing the 0.72 plate threshold with
margin, but NOT the parity `ADEF_POINT`'s comment claims. Closing the last 22% requires
ADEF_POINT >= ~1.53, which raises `armor_defeat_sigma` for EVERY selected-point weapon at every
armoured tier and trips the Godot export gate — the plan's own flagged candidate, explicitly marked
escalate-rather-than-take. A second input to that decision: the hammer reference itself is inflated
by E2a's disclosed saturation residue (poleaxe percussion pins at PERC_CAP, so the hammer reads
1.3000 where it read 1.2162 before), against which the spike is already at 84%. Both are the same
deferred Phase-C PERC_SCALE/PERC_EXP re-fit.

FALSIFIERS — mutations run against these guards, each naming its target:
  - restore `tauth` on the blunt-composite spike     -> guards 1, 2, 3 red.
  - exempt EVERY point head from `tauth`             -> guard 4 red (the PC-5 lever deleted).
  - drop the percussion-puncture term, keep gap only -> guard 3 red, via its DEPENDENCE assertion.
    It is NOT caught by the ratio floor: bare gap reaches 0.757, which cleared the 0.75 floor this
    file originally shipped. The mutation was run, it survived, and the guard was rewritten — see
    guard 3's docstring. This is the review-R-5 failure mode reappearing one level up: a pin that
    looks like it discriminates and does not.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S     # noqa: E402
import combatant as C          # noqa: E402
import core                    # noqa: E402
import weapon_physics as WP    # noqa: E402
from config import CFG         # noqa: E402

# The blunt-composite family: a native BLUNT head that also carries a concentrated spike/beak. These
# are the weapons the exemption must reach (the plan names the collateral three explicitly).
BLUNT_COMPOSITES = ('poleaxe', 'bec_de_corbin', 'lucerne_hammer', 'goedendag')


def _live_selection(name, tier):
    """The (head, gap) `armor_defeat_sigma` actually consumes — via select_mode, not a synthetic call."""
    dm, h, sg, sp, spc, se = S.select_mode(C.Combatant('x', weapon=name), tier, False, CFG)
    return h, sg


def test_blunt_composite_spike_is_not_derated_by_the_reach_lever():
    """GUARD 1 — the mechanism invariant. For a native-blunt weapon, selected-point armour-defeat
    capability must be INDEPENDENT of `thrust_authority`. Proved by moving that function's output
    and requiring the capability not to follow."""
    real = core.thrust_authority
    try:
        moved = {}
        for name in BLUNT_COMPOSITES:
            w = C.WEAPONS[name]
            core.thrust_authority = lambda hl: 1.0
            hi = core.adef_cap(w, CFG, head='point', gap=w['gap'])
            core.thrust_authority = lambda hl: 0.1
            lo = core.adef_cap(w, CFG, head='point', gap=w['gap'])
            if abs(hi - lo) > 1e-12:
                moved[name] = (hi, lo)
        assert not moved, (
            "a blunt-composite's spike is still scaled by the reach-thrust lever "
            f"(thrust_authority 1.0 vs 0.1 moves it): {moved}. A two-handed percussive blow driving "
            "a concentrated spike is not a fencer's extended thrust — core.adef_cap's own line-400 "
            "comment says the beak's authority IS its percussion energy. Mutation that produces "
            "this: restoring `tauth` on the native-blunt selected-point branch."
        )
    finally:
        core.thrust_authority = real


def test_poleaxe_spike_clears_the_plate_threshold():
    """GUARD 2 — the consequence, at the LIVE selected mode and gap. `select_mode` picks 'point' for
    the poleaxe at medium and heavy; on the pre-fix tree that mode read 0.6013 against a 0.72
    threshold, i.e. armor_defeat_sigma went NEGATIVE and plate shielded against a poleaxe."""
    thr = CFG['ADEF_THRESHOLD']['heavy']
    head, gap = _live_selection('poleaxe', 'heavy')
    assert head == 'point', (
        f"poleaxe no longer selects its spike at heavy (selects {head!r}) — this guard's premise "
        "moved and it no longer observes M3/F3."
    )
    cap = core.adef_cap(C.WEAPONS['poleaxe'], CFG, head=head, gap=gap)
    assert cap > thr, (
        f"poleaxe spike adef_cap {cap:.4f} <= ADEF_THRESHOLD['heavy'] {thr} — armor_defeat_sigma is "
        f"{CFG['ADEF_W']['heavy'] * (cap - thr):+.4f}, so plate SHIELDS against the poleaxe on the "
        "mode select_mode itself picks. Mutation that produces this: restoring `tauth` on the "
        "blunt-composite spike (pre-fix value 0.6013)."
    )


def test_spike_approaches_its_own_hammer():
    """GUARD 3 — the ED-1080 contract as a RATIO, per review R-5: 'spike ~ hammer', not merely
    'spike clears the threshold'. The weak form passes a fix that clears 0.72 while still
    contradicting the calibration it claims to restore.

    FLOOR IS 0.78, NOT 1.0 — and that is a disclosed shortfall, not a weak guard. Full parity needs
    ADEF_POINT re-anchored roster-wide (escalated; see the module docstring).

    ⚠ THE RATIO ALONE IS NOT ENOUGH, and this docstring said otherwise until the mutation was
    actually run. The claim was that a 0.75 floor would catch the drop-the-percussion-puncture-term
    mutant because bare gap reaches only 0.757. It does not: 0.757 >= 0.75, so that mutant PASSED.
    A floor tightened to just above it would be a 0.007-wide margin, i.e. brittle decoration. So the
    percussion path is pinned by a DEPENDENCE assertion instead — the spike's capability must
    respond to `puncture_pressure`, which the bare-gap form cannot do at any margin."""
    w = C.WEAPONS['poleaxe']
    head, gap = _live_selection('poleaxe', 'heavy')
    spike = core.adef_cap(w, CFG, head=head, gap=gap)
    hammer = core.adef_cap(w, CFG, head='blunt')
    ratio = spike / hammer
    assert ratio >= 0.78, (
        f"poleaxe spike {spike:.4f} is only {ratio:.1%} of its own hammer {hammer:.4f} — ED-1080's "
        "recorded calibration is 'spike adef ~ its hammer'. Pre-fix this ratio was 46%. Mutation "
        "that produces this: restoring `tauth` on the blunt-composite spike."
    )
    # the percussion-driven puncture path must be LIVE for the spike, not merely gap precision
    real_pp = WP.puncture_pressure
    try:
        WP.puncture_pressure = lambda ww, **kw: real_pp(ww, **kw) * 2.0
        boosted = core.adef_cap(w, CFG, head=head, gap=gap)
    finally:
        WP.puncture_pressure = real_pp
    assert boosted > spike + 1e-9, (
        f"doubling puncture_pressure does not move the poleaxe's spike capability ({spike:.4f} -> "
        f"{boosted:.4f}) — the spike is being scored on gap precision alone. A beak defeats plate by "
        "the percussion energy behind it. Mutation that produces this: dropping the "
        "percussion-puncture term from the native-blunt selected-point branch."
    )


def test_a_true_reach_thrust_is_still_derated():
    """GUARD 4 — the complementary pin. The exemption is scoped to blunt-composite spikes; the PC-5
    lever must survive for the weapons it was actually grounded on. A spear or rapier delivering a
    thrust at full extension is still de-rated. Without this, 'exempt every point head' passes."""
    real = core.thrust_authority
    try:
        for name in ('spear', 'rapier', 'yari'):
            w = C.WEAPONS[name]
            assert w['head'] != 'blunt', f"{name} is not a reach-thrust control any more"
            core.thrust_authority = lambda hl: 1.0
            hi = core.adef_cap(w, CFG, head='point', gap=w['gap'])
            core.thrust_authority = lambda hl: 0.1
            lo = core.adef_cap(w, CFG, head='point', gap=w['gap'])
            assert hi > lo + 1e-9, (
                f"{name}'s reach-thrust is no longer de-rated by thrust_authority — the PC-5 lever "
                "has been deleted rather than scoped. Mutation that produces this: exempting EVERY "
                "point head from tauth instead of only the native-blunt composite spike."
            )
    finally:
        core.thrust_authority = real
