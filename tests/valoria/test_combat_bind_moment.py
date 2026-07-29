"""MASS/MOMENTUM IN THE BIND — channel 5 (ED-PC-0052).

DEFECT (verified red on the pre-fix tree): where weapons connect — parry, block, bind, wind — the
engine had **no mass, momentum or inertia term at all**. `bind_sigma = lev + catch + tac + strq +
spine + wound`, and the only physical lever among those is
`leverage() = grip_len - LEVER_HEAD_K*head_len`, which is **pure geometry**. Two weapons of identical
grip geometry and wildly different mass distribution bound identically.

Jordan, 2026-07-29: *"when it comes to parrying and blocking and binds and winds etc where weapons
connect with one another... the lighter the weapon is, the easier it is to move away due to momentum.
so while the rapier can react very quickly, wouldn't this make it a lot easier for an opponent with a
heavier weapon -- say a scimitar -- or some other cutting weapon indicate that they would have an
advantage in those weapon-to-weapon collision/reorienting scenarios due to weight/momentum/heft/
leverage?"*

THE VARIABLE IS THE MOMENT, NOT THE WEIGHT — and measuring first is what caught that. The rapier is
the HEAVIER weapon (1.37 kg against the scimitar's 0.95 and the shamshir's 0.77), so a mass-keyed term
would have moved the wrong way. What governs how cheaply a blade is displaced at the contact is the
moment about the hand: `at_grip(w, grip)['S_g']` reads rapier **0.1231** against scimitar **0.2199**
(1.8x). A rapier is heavy but hilt-and-pommel balanced — quick to move, and cheap for an opponent to
shove aside at the blade, which is Jordan's mechanism stated in the right variable.

IT IS A GENUINELY NEW PRIMITIVE, not a re-spelling of `leverage()`: measured across the 50-weapon
startable roster, **corr(leverage(), log S_g) = +0.109**. The demonstration is deliberately taken
WITHIN one weapon class rather than across two — a polearm-vs-sword pair would prove nothing, since of
course they differ. Among the ten one-handed swords of the civilian duel population the two measures
very nearly INVERT:

    falchion   leverage -0.0576   S_g 0.2415      <- worst lever arm, HIGHEST moment
    tsurugi    leverage +0.0110   S_g 0.1130      <- better lever arm, LOWEST moment

`leverage()` spans just 0.097 across those ten swords while their moments span 2.14x. A heavy chopping
falchion shoving a light tsurugi off the bind is the effect that was missing, and the lever-arm
primitive ranks it backwards. So the moment gets its own additive, ablatable term and is NOT multiplied
into `leverage()` (consolidation_v1 §2.3: one primitive per physical effect).

Note also what this explains: the rapier has the WORST `leverage()` of all ten (-0.0792) and the
second-lowest moment, so its bind dominance was coming from `catch` — its swept hilt, +0.197 against a
scimitar — with no physical counterweight anywhere.

FORM — a LOG-RATIO, `BIND_MOMENT_K * log(S_g_agg / S_g_def)`:
  - scale-free and sign-symmetric, so it cannot be gamed by the unit of moment and cannot invert;
  - it composes correctly with `bind_dominance_p = logistic(bind_sigma)` — an additive log-odds shift,
    exactly the shape ED-PC-0045 established when it replaced a multiplicative lever that AMPLIFIED a
    negative differential;
  - it compresses the polearm tail. A raw linear differential would hand a spear (S_g 1.3873) roughly
    ten times the arming sword's moment and an unbounded bind sigma; the log reads 2.4 instead of 10.5.

NO DOUBLE-COUNT with the speed cost. A heavier-at-the-contact weapon is slower to initiate a rebind or
a wind, and the engine already prices that elsewhere — `agility` is MoI^(-AGILITY_EXP), feeding tempo
and the defence affinities. This term prices only the *displacement resistance* half, which was absent.

FALSIFIERS — mutations run against these guards, each naming its target:
  - BIND_MOMENT_K = 0                       -> guards 2, 3 red (the term is inert / pre-fix state).
  - key the term on `mass` instead of S_g   -> guard 3 red (the rapier is the heavier weapon).
  - key it on a raw linear differential     -> guard 5 red (the polearm tail is not compressed).
  - fold it into `leverage()`               -> guard 6 red (leverage must stay pure geometry).
  - read derive()['static_moment'] instead of at_grip's S_g -> guard 7 red (grip-blind).
"""
import math
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S     # noqa: E402
import combatant as C          # noqa: E402
import tradition as TRAD       # noqa: E402  (the resolver's tradition service — NOT traditions.py)
import weapon_physics as WP    # noqa: E402
from config import CFG         # noqa: E402


def _bind(a_weapon, b_weapon, cfg=None):
    """One bind iteration's net sigma, aggressor `a_weapon` vs defender `b_weapon`."""
    return S.bind_sigma(C.Combatant('a', weapon=a_weapon), C.Combatant('b', weapon=b_weapon),
                        cfg or CFG, TRAD)


def _cfg_with(**over):
    d = dict(CFG)
    d.update(over)
    return d


def test_the_premise_the_rapier_is_the_heavier_weapon():
    """The pin that makes this batch's variable choice falsifiable. If the roster ever changes so the
    rapier is LIGHTER than the scimitar, the 'key on moment not mass' reasoning must be re-checked —
    it is only interesting because the naive variable points the other way."""
    assert C.WEAPONS['rapier']['mass'] > C.WEAPONS['scimitar']['mass'], (
        "the rapier is no longer heavier than the scimitar; this batch's central argument (mass would "
        "have moved the wrong way, moment moves the right way) needs re-deriving"
    )
    assert WP.at_grip(C.WEAPONS['rapier'], 0.0)['S_g'] < WP.at_grip(C.WEAPONS['scimitar'], 0.0)['S_g'], (
        "the rapier's grip-moment is no longer below the scimitar's — the mechanism's premise moved"
    )


def test_the_bind_responds_to_the_moment_differential():
    """GUARD 2 (the defect pin). The moment must contribute to the bind for a pairing that differs ONLY
    in moment-bearing terms.

    ⚠ REWRITTEN: the first version of this guard compared `scimitar vs arming` against
    `rapier vs arming` — two DIFFERENT pairings, so `catch`, `spine` and `tac` supplied a difference
    all by themselves and the guard PASSED at BIND_MOMENT_K = 0, i.e. it never observed the defect at
    all. Caught by running the declared pre-fix mutation. It now isolates the term by ablating it on
    the SAME pairing, which is the only form that can see this defect."""
    off = _cfg_with(BIND_MOMENT_K=0.0)
    for a, b in (('scimitar', 'rapier'), ('falchion', 'tsurugi'), ('arming', 'dagger')):
        live, ablated = _bind(a, b), _bind(a, b, off)
        assert abs(live - ablated) > 1e-9, (
            f"{a} vs {b}: the bind is identical with and without the moment term "
            f"({live:.6f} vs {ablated:.6f}) — there is no mass/momentum term in the bind. Mutation "
            "that produces this: BIND_MOMENT_K = 0 (which IS the pre-fix engine)."
        )


def test_the_heavier_at_the_contact_gains_in_the_bind():
    """GUARD 3 (Jordan's worked example, and the direction pin). A higher-moment cutter must gain
    against the rapier in the bind relative to the term being off.

    ALSO the mass-vs-moment discriminator: keying this on `mass` would move it the WRONG way, because
    the rapier is the heavier weapon."""
    off = _cfg_with(BIND_MOMENT_K=0.0)
    for cutter in ('scimitar', 'shamshir', 'sabre'):
        before = _bind(cutter, 'rapier', off)
        after = _bind(cutter, 'rapier')
        assert after > before + 1e-9, (
            f"{cutter} does not gain in the bind against the rapier once the moment term is live "
            f"({before:.6f} -> {after:.6f}). Mutations that produce this: BIND_MOMENT_K = 0, or "
            "keying the term on mass (the rapier is HEAVIER, so mass moves it backwards)."
        )


def test_the_term_is_ablatable():
    """GUARD 4 — its own ablatable primitive (the U9/U10 discipline: a lever must be switchable off to
    be measurable). Turning K off must remove the whole contribution and leave a finite bind."""
    off = _cfg_with(BIND_MOMENT_K=0.0)
    checked = 0
    for a, b in (('scimitar', 'rapier'), ('spear', 'dagger'), ('poleaxe', 'arming'),
                 ('shamshir', 'rapier'), ('dagger', 'spear')):
        live, ablated = _bind(a, b), _bind(a, b, off)
        assert math.isfinite(live) and math.isfinite(ablated)
        assert live != ablated, f"{a} vs {b}: the moment term contributes nothing at the live K"
        checked += 1
    assert checked == 5, f"only {checked} pairings exercised"


def test_the_moment_term_is_antisymmetric():
    """GUARD 4b — swapping the two sides must negate the term's contribution exactly. A bind
    advantage that does not reverse when the roles reverse is a sign bug of the ED-PC-0045 class."""
    off = _cfg_with(BIND_MOMENT_K=0.0)
    for a, b in (('scimitar', 'rapier'), ('spear', 'arming'), ('dagger', 'poleaxe')):
        fwd = _bind(a, b) - _bind(a, b, off)
        rev = _bind(b, a) - _bind(b, a, off)
        assert abs(fwd + rev) < 1e-12, (
            f"the moment contribution is not antisymmetric for {a}/{b}: {fwd:+.6f} vs {rev:+.6f}"
        )


def test_the_moment_edge_is_scale_invariant():
    """GUARD 5 — the real reason the form is a LOG-RATIO, and the one property that actually
    discriminates it from a linear differential: **dimensional coherence**. `S_g` is a moment and
    carries units; adding a bare DIFFERENCE of moments to a sigma is dimensionally incoherent, and its
    magnitude would depend on the unit chosen. A log-ratio is dimensionless, so scaling every moment in
    the roster by a constant must leave the bind edge EXACTLY unchanged.

    ⚠ REWRITTEN: this guard first asserted that the extreme spear/dagger mismatch stayed under
    `6*K` sigma, claiming a linear form would breach it. **That was false and the mutation proved it** —
    S_g differences are small in absolute terms (spear-dagger = 1.377), so the linear form contributes
    LESS here (0.413) than the log-ratio does (1.47), and the mutant passed. The log compresses relative
    to the RATIO spread (8.5x vs 14x across the roster), not absolutely. Scale-invariance is the
    property that is actually unique to the log form, and it cannot be satisfied by an epsilon."""
    a = C.Combatant('a', weapon='spear')
    b = C.Combatant('b', weapon='dagger')
    base = S.contact_moment_edge(a, b)
    ratio = (WP.at_grip(C.WEAPONS['spear'], 0.0)['S_g']
             / WP.at_grip(C.WEAPONS['dagger'], 0.0)['S_g'])
    assert ratio > 50, f"the spear/dagger moment ratio {ratio:.1f} is no longer the extreme case"
    assert base > 0.0, "the extreme case should still favour the spear"
    # scale BOTH sides' moments by 1000x by scaling the underlying masses; a dimensionless log-ratio
    # must not move at all, a linear differential moves by ~1000x.
    orig_a, orig_b = a.w['mass'], b.w['mass']
    parts_a = [dict(p) for p in a.w.get('parts', [])] if isinstance(a.w.get('parts'), list) else None
    try:
        for w in (a.w, b.w):
            w['mass'] = w['mass'] * 1000.0
            if isinstance(w.get('parts'), list):
                for pt in w['parts']:
                    if isinstance(pt, dict) and 'mass_kg' in pt:
                        pt['mass_kg'] *= 1000.0
        scaled = S.contact_moment_edge(a, b)
    finally:
        a.w['mass'], b.w['mass'] = orig_a, orig_b
        if parts_a is not None:
            a.w['parts'] = parts_a
    assert abs(scaled - base) < 1e-9, (
        f"scaling every moment by 1000x moved the bind edge {base:.6f} -> {scaled:.6f}. The term is "
        "not dimensionless — a bare difference of moments is being added to a sigma. Mutation that "
        "produces this: `return sa - sd` instead of `log(sa/sd)`."
    )


def test_leverage_stays_pure_geometry():
    """GUARD 6 — the one-primitive-per-effect pin (consolidation_v1 §2.3). `leverage()` is the lever
    ARM; the moment is a DIFFERENT physical fact. The new term must not have been folded into it, or
    the two can never be ablated apart. Verified by mass-independence."""
    c = C.Combatant('x', weapon='scimitar')
    before = S.leverage(c, CFG)
    original = c.w['mass']
    try:
        c.w['mass'] = original * 3.0
        after = S.leverage(c, CFG)
    finally:
        c.w['mass'] = original
    assert abs(after - before) < 1e-12, (
        f"leverage() moved when mass tripled ({before:.6f} -> {after:.6f}) — the moment has been "
        "folded into the lever-arm primitive instead of standing beside it."
    )


def test_choking_up_a_polearm_reduces_its_moment_advantage():
    """GUARD 7 — the emergent consequence, pinned deliberately. `S_g` is grip-aware (a spear's moment
    halves from 1.3873 to 0.6937 when choked up), so a crowded polearm loses part of its bind
    advantage. That is a real and desirable interaction with the closed-measure grip model, and pinning
    it means a future change that silently makes the term grip-blind fails here."""
    open_grip = C.Combatant('a', weapon='spear')
    open_grip.grip_position = 0.0
    choked = C.Combatant('a', weapon='spear')
    choked.grip_position = 1.0
    d = C.Combatant('b', weapon='arming')
    assert S.bind_sigma(open_grip, d, CFG, TRAD) > S.bind_sigma(choked, d, CFG, TRAD) + 1e-9, (
        "choking up a spear does not reduce its bind moment advantage — the term has become "
        "grip-blind (it must read at_grip(w, grip_position)['S_g'], not derive()['static_moment'])."
    )
