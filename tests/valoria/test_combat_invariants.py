"""Architecture-invariant guards for the scene-combat engine (the pre-merge re-audit found these missing).

The behavioural guards (test_combat_balance_guard) check the engine RESOLVES sanely; these lock the re-baseline's
HEADLINE ARCHITECTURE CLAIMS so they cannot silently regress — the exact failure class that let an earlier incomplete
de-leak land unnoticed (Gate-1 audit):

  · SINGLE-SOURCE   — core.p_auth (the duplicate percussion derivation) stays deleted; one WP source.
  · NO NAME-TABLE   — no weapon-NAME string literal appears in resolution code (poleaxe/mace/staff are primitive
                       bundles; behaviour EMERGES — the L0 primitive-law).
  · EMERGENT USE-MODE — select_mode reproduces every single-mode weapon's native head at every armour tier; exactly
                       one weapon (the poleaxe) changes its selected head with armour — and that falls out of primitives.
  · GAP-GAME        — the poleaxe affords + selects its spike vs plate; the mace/staff afford no point.

All static or tiny-seeded; deterministic.
"""
import ast
import os
import re
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, 'tests', 'sim', 'v32-combat-balance'))


def _mods():
    pytest.importorskip("numpy")
    import combatant as C
    import core
    import combat_systems as S
    import weapon_physics as WP
    from config import CFG
    return C, core, S, WP, CFG


# ── SINGLE-SOURCE ───────────────────────────────────────────────────────────────────────────────
def test_percussion_authority_single_source():
    """core.p_auth (the duplicate that read the hand-set pob_frac) was deleted and unified onto
    weapon_physics.percussion_authority — the invariant whose ABSENCE let the incomplete de-leak land. Guard: it stays
    gone, and both the damage path (core.strike) and the sigma path (systems.adef_cap) read the SAME WP authority."""
    C, core, S, WP, CFG = _mods()
    assert not hasattr(core, 'p_auth'), "core.p_auth resurrected — percussion authority is double-derived again"
    # the sigma path (adef_cap blunt branch) is defined in terms of WP.percussion_authority; confirm a mace's
    # blunt armour-defeat capability tracks the WP value (not a private re-derivation).
    mace = C.WEAPONS['mace']
    pa = WP.percussion_authority(mace)
    assert pa > 0
    # adef_cap blunt = max(ADEF_BLUNT*pa/REF, ADEF_POINT*puncture/REF); the concussion term must equal the WP source
    assert abs(CFG['ADEF_BLUNT'] * (pa / CFG['ADEF_PERC_REF'])) > 0
    assert S.adef_cap(mace, CFG, 'blunt') >= CFG['ADEF_BLUNT'] * (pa / CFG['ADEF_PERC_REF']) - 1e-9


# ── NO WEAPON-NAME TABLE IN RESOLUTION ────────────────────────────────────────────────────────────
def _string_literals_excluding_docstrings(path):
    """All string-constant literals in a module EXCEPT module/function/class docstrings. Comments are not in the AST,
    so they are naturally ignored — this catches only live code string literals."""
    tree = ast.parse(open(path, encoding='utf-8').read())
    doc_nodes = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, 'body', [])
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                doc_nodes.add(id(body[0].value))
    return [n.value for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in doc_nodes]


def test_no_weapon_name_literal_in_resolution():
    """poleaxe/mace/staff are bundles of primitives; the L0 primitive-law forbids a weapon-NAME conditional / per-weapon
    table in resolution. Scan the resolution modules for any weapon-name string LITERAL in live code (docstrings +
    comments allowed). A regression that hard-codes `if weapon=='poleaxe'` trips this."""
    C, core, S, WP, CFG = _mods()
    names = {n for n in C.WEAPONS if 'base' not in C.WEAPONS[n]}  # weapon names (exclude auto-switch forms)
    offenders = {}
    for mod in ('core.py', 'combat_systems.py', 'wrapper.py', 'contact.py'):   # I7b: contact.py joins the scanned resolution modules
        lits = _string_literals_excluding_docstrings(os.path.join(ENGINE, mod))
        hit = sorted({s for s in lits if s in names})
        if hit:
            offenders[mod] = hit
    assert not offenders, f"weapon-name literal(s) in resolution code (primitive-law break): {offenders}"


# ── EMERGENT USE-MODE SELECTION ───────────────────────────────────────────────────────────────────
def test_use_mode_selection_emerges_from_primitives():
    """select_mode must (a) reproduce every SINGLE-mode weapon's native head at every armour tier, and (b) leave
    exactly the weapons with a genuine multi-mode split (a real point-vs-blunt or point-vs-cut choice, not just an
    internal cut_thrust cut/gap-thrust re-weighting — that stays keyed on ONE token, see test_gap_thrust_...) as the
    ones whose SELECTED HEAD TOKEN changes with armour. Both fall out of the derived afforded_heads (no per-weapon
    list).
    [UPDATED, 2026-07-03, I2/I4/D2b/D5/R-7/JD-5 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
    plan_r1_RATIFIED.md] The R-7/M-02 object-confusion fix (I2) widens select_mode's greedy comparator to read each
    candidate head's OWN gap_precision/percussion (the winning mode_element's, via the widened afforded_heads
    5-tuple) instead of the whole-weapon w['gap']/percussion_authority(w) scalar. guisarme/voulge's point elements
    (thrusting spike / thrusting_heel_spike) carry a materially HIGHER gap_precision than their whole-weapon
    average — under the old whole-weapon-gap comparator this was invisible, so they never out-coupled their
    cut_thrust cleaver; under the corrected per-element gap they NOW correctly win the puncture path vs medium/
    heavy armour (exactly the reach-ladder gap-game mechanic bec_de_corbin/ji/kama_yari/lucerne_hammer already
    modelled). goedendag's point still never out-scores its blunt. I4/JD-5 then authors the deferred mode_elements
    for guandao (rear spike/hook notch) and fauchard (back-hook spike) — both DELIBERATELY REGENERATED here, not
    silently patched: verified via direct select_mode() sweep this pass that both flip curved_cut->point at
    light/medium/heavy (their point element's higher gap_precision wins as soon as any armour is present), none
    unchanged. hook_sword's authored blunt crescent (JD-5) never clears SELECT_EPS against any tier under the
    current [SIM-CALIBRATE] gains — a real but currently-inert affordance (same class as goedendag's point), so
    hook_sword does NOT become a changer. poleaxe is a [PHASE-C FLAG] — its own more-accurate, more-forward
    Phase-B mass distribution lifted its blunt percussion authority enough that it no longer switches to its
    spike vs heavy armour (weapon_physics.percussion_authority docstring; also test_gap_game_poleaxe_spikes_
    plate); left OUT of the expected set here until Phase C's engine-scale recalibration restores it, not
    silently included as if the current behaviour were correct.
    [PHASE-C FLAG, 2026-07-08, U1/ED-PC-0010] lucerne_hammer JOINS poleaxe's exclusion: U1's JD-1 PoB fix
    corrected its under-massed hammer/fluke/spike head (0.70->1.344kg, matching poleaxe's own physical scale
    — weapons.py) to land its PoB in the ratified poleaxe-class band (20-55cm), which as a direct consequence
    lifted its blunt percussion authority enough that it too no longer switches to its spike vs heavy armour —
    the SAME mechanism, corroborating rather than contradicting the poleaxe finding (both weapons share the
    same head_len/grip_len/composite-head shape). Moved out of `expected` below until the same Phase-C
    engine-scale recalibration restores it.
    [U2/ED-PC-0011, 2026-07-08 — the graded secondary-affordance checks (percussion/cut/point) re-enabled in
    element_afforded, plus the CUT_AUTH_REF magnitude-scaling fix] EXPANDS the changer set from 7 to 17,
    validated via a 13-agent agonist/antagonist adversarial Workflow (6 Sonnet producer/critic weapon-group
    pairs cross-examining each other's HEMA/physics grounding + 1 Opus final synthesis) rather than accepted
    on say-so. Ten NEW weapons join: greatsword/katana/tachi/nandao/glaive/podao/fauchard/hook_sword — all
    natively straight_cut/curved_cut two-handed OR one-handed blades that now afford a weak secondary
    half-sword-style thrust (point), switching to it once the material-resistance table's Williams-sourced
    puncture-beats-shear-vs-soft-armour asymmetry (and, vs plate, the situational gap game) out-couples their
    own edge's armour-degraded transmit — judged historically defensible (half-swording to the gaps is a
    well-attested PRIMARY technique against a harnessed opponent for every one of these classes, not just
    longswords) and accepted as genuine changers. tachi/nandao specifically switch to their OWN weak Mordhau/
    blunt option at 'heavy' rather than to their (comparatively weaker, 0.32/0.24) point — judged plausible
    given the two blades' own thrust geometry is the weakest of this group's.
    sabre/scimitar/falchion ALSO newly switch to a secondary point, and are included below because the engine
    genuinely does this today — but the adversarial pass FLAGGED this as a probable bug, not a validated finding
    (ED-PC-0012): these are historically dedicated slashing blades (scimitar's own point geometry, 0.16, is the
    lowest of any weapon in the roster) and the switch was traced to core.coupling's DELIVERY['point'] not
    scaling by the candidate's own thrust magnitude the way 'cut' now does — verified directly that scimitar/
    sabre/falchion/hook_sword's secondary point ALL score an IDENTICAL coupling at 'light' armour regardless of
    their 0.16-0.40 geometry spread (core._transmit's puncture gap-seeking term is floor-locked below the raw
    material transmission for any of these gap_precision values). A THRUST_AUTH_REF fix analogous to
    CUT_AUTH_REF is recommended but deliberately NOT implemented this pass (see ED-PC-0012's ledger entry) — it
    would also touch several of the newly-accepted two-handed cutters (tachi/nandao/glaive/podao all sit below
    the natural reference too) and needs its own roster-wide re-verification, not a third redesign-and-reverify
    cycle rushed through in the same session. hook_sword's own switch was judged MORE defensible than the other
    three one-handed cutters' (its point, 0.40, is measurably above-floor via its own gap_precision, the least
    mechanism-dominated of the four) and is accepted rather than flagged. When ED-PC-0012 lands, sabre/scimitar/
    falchion's entries below are expected to be removed (or their switch-tier to change) — this is a KNOWN,
    DOCUMENTED, load-bearing residual, not an oversight."""
    C, core, S, WP, CFG = _mods()
    tiers = ['none', 'light', 'medium', 'heavy']
    changers = []
    for n, rec in C.WEAPONS.items():
        if 'base' in rec:
            continue
        heads = {S.select_mode(C.Combatant('x', weapon=n), ar, False, CFG)[1] for ar in tiers}
        if len(heads) > 1:
            changers.append(n)
    # poleaxe + lucerne_hammer excluded — see [PHASE-C FLAG]s above.
    # [PC-5/ED-PC-0015, 2026-07-22] thrust_authority(head_len) scales the puncture GAP-PRESS term (core._transmit),
    # so select_mode's greedy comparator now weights each candidate point by its point-to-hand lever. TWO grounded
    # shifts in the changer set: +estoc/flamberge/changdao/odachi JOIN (stiff two-handed thrust-blades whose
    # short-enough-lever half-sword thrust now out-couples their edge vs mail/plate); -bec_de_corbin/voulge DROP
    # (their armour-defeat is a SWUNG beak/spike, not a static pommel-press — routed to their percussion path,
    # plate-defeat outcome preserved ~91%/63% at heavy).
    # [PC-4/ED-PC-0012, 2026-07-22 — RESOLVED] THRUST_AUTH_REF now scales DELIVERY['point'] by the SELECTED point's
    # own derived thrust magnitude (the 'cut'/CUT_AUTH_REF analog), removing the FLOOR-LOCKED artifact where a weak
    # incidental point on a slasher scored the same coupling as a real thruster. FOUR weapons DROP as changers (their
    # spurious armour-tier point-switch was the artifact, now correctly gone — they stay dedicated cutters at every
    # tier): sabre (point_eff 0.26), scimitar (0.16 — the roster's weakest), falchion (0.23), podao (0.24). The
    # remaining low-point two-handed cutters STAY changers on GROUNDED, geometry-earned grounds (verified this pass):
    # katana (0.44) keeps its thrust at light/medium and Mordhaus vs plate; tachi/nandao route to their own attested
    # Mordhau/blunt vs mail/plate (exactly the ED-anticipated shift); glaive keeps an earned mid-tier point. Every
    # NATIVE pointer (bear_spear 0.53, rapier, spear, estoc, yari, …) clamps to ratio 1.0 and is UNAFFECTED.
    # [ED-PC-0027, 2026-07-23 — T_vuln undefended-time model + mode-aware heft] select_mode's greedy comparator now
    # discounts each mode's coupling by its EXPOSURE (a committed swing leaves you open longer than a controlled
    # thrust, EXPOSE_SELECT_K), so in the 1v1 thrust-capable weapons prefer the point. This RE-SHAPES the changer set:
    #   - DROP kama_yari/guandao/fauchard/ji: they now thrust at EVERY tier (the point wins the exposure trade even
    #     unarmoured — grounded: their big pole-cut is exposing, the point is the dueling staple), so their selected
    #     head no longer CHANGES with armour → they are point-primary, not changers.
    #   - JOIN lucerne_hammer/goedendag: they now thrust at soft tiers but HAMMER vs mail/plate (their weak point
    #     can't gap-seek plate, so the resisted-but-heavy percussion wins there) → a genuine armour-conditional switch.
    # poleaxe is NO LONGER excluded here: it thrusts at every tier (see test_gap_game_poleaxe_thrusts_in_the_duel), so
    # its head does not change with armour → correctly absent from the changer set for a different reason than the old
    # [PHASE-C FLAG] (it is point-primary now, not blunt-locked).
    expected = ['greatsword', 'glaive', 'guisarme', 'lucerne_hammer', 'goedendag', 'katana', 'tachi',
                'odachi', 'changdao', 'nandao', 'flamberge', 'estoc', 'hook_sword']
    assert changers == expected, f"expected {expected} to change selected head with armour; got {changers}"


def test_afforded_heads_emerge_from_primitives():
    """Affordance emerges from geometry primitives: the poleaxe affords blunt+point (spike from point_concentration
    0.78); the mace/staff afford NO point (point_concentration 0.02/0.05 < the gate) — no weapon name involved."""
    C, core, S, WP, CFG = _mods()
    assert set(S.afforded_heads(C.WEAPONS['poleaxe'])) == {'blunt', 'point'}
    assert 'point' not in S.afforded_heads(C.WEAPONS['mace'])
    assert 'point' not in S.afforded_heads(C.WEAPONS['staff'])


def test_afforded_heads_emerge_from_phase_b2_mode_elements():
    """The morphology-rearch Phase B2 composites' per-element mode_elements affordances — each weapon's union
    over its own real striking elements, not a copy of another weapon's set.
    [U2/ED-PC-0011, 2026-07-08] ji/kama_yari gain a THIRD token, 'cut': each weapon's own POINT-tokened
    spearhead element carries a small incidental edge (ji=0.40, kama_yari=0.32 — a wing/blade-like flare near
    the socket, distinct from and much weaker than the weapon's own dedicated curved_cut blade, 0.99/0.88) that
    now clears the graded secondary-affordance floor (MODE_EDGE_MIN). Verified via the ED-PC-0011 adversarial
    Workflow this is genuine (not spurious) physics — comparable real yari/ji-class spearheads carried a real,
    if secondary, cutting capability near the socket — and that it NEVER wins selection at any armour tier or
    grip/room condition (curved_cut dominates at 'none', point dominates everywhere armour is present); its
    presence here is a real but currently-inert affordance, the same class as goedendag's own never-selected
    point. guisarme/voulge do NOT gain this token — each has only ONE point-family element (a genuine thrusting
    spike), not a separate incidental-edge source, and their own cut_thrust element already carries the ONLY
    edge each weapon has."""
    C, core, S, WP, CFG = _mods()
    assert set(S.afforded_heads(C.WEAPONS['bec_de_corbin'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['lucerne_hammer'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['goedendag'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['ji'])) == {'point', 'curved_cut', 'cut'}
    assert set(S.afforded_heads(C.WEAPONS['kama_yari'])) == {'point', 'curved_cut', 'cut'}
    assert set(S.afforded_heads(C.WEAPONS['guisarme'])) == {'cut_thrust', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['voulge'])) == {'cut_thrust', 'point'}


# ── GAP GAME ──────────────────────────────────────────────────────────────────────────────────────
def test_gap_game_poleaxe_thrusts_in_the_duel():
    """In the 1v1 the engine models, the poleaxe SELECTS its spike (puncture/point) at EVERY armour tier —
    RESOLVED 2026-07-23 (ED-PC-0027, the T_vuln undefended-time model + Jordan's historical grounding). The spike
    defeats plate at the reach-ladder gaps (gap_precision × GAP_EXPOSURE), AND the thrust is the poleaxe's dueling
    staple at all measures because its heavy SWING (the hammer/bec) leaves you open far longer than a controlled
    thrust — the T_vuln vulnerability window. Per Jordan (2026-07-23): the poleaxe's swing 'was a man-advantage
    move, used when they had opportunity to do so without being struck themselves' — i.e. group combat, NOT the
    1v1. So the OLD assertion 'unarmoured it does NOT spike' was a fiat encoding the videogame trope that a heavy
    weapon hammers soft targets; it is retired (like the sabre pure-cutter assertion). The hammer is not gone —
    it remains afforded and would win selection if its exposure window were covered (a group-combat model, future);
    it simply loses the 1v1 exposure trade. Emergent from gap_precision + T_vuln, no name conditional."""
    C, core, S, WP, CFG = _mods()
    for tier in ('none', 'light', 'medium', 'heavy'):
        dm, h = S.select_mode(C.Combatant('x', weapon='poleaxe'), tier, False, CFG)[:2]
        assert (dm, h) == ('puncture', 'point'), f"poleaxe should thrust (the 1v1 staple) vs {tier}; got {(dm, h)}"
    # the hammer is still AFFORDED (not removed) — it just loses the 1v1 exposure trade
    assert 'blunt' in S.afforded_heads(C.WEAPONS['poleaxe']), "the poleaxe's hammer face is still afforded"


# ── I2 CIRCUMSTANCE DEGRADATION (D1/D2/D2b/D5, 2026-07-03) ──────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_at_circumstance_is_l0_pure():
    """D1: at_circumstance takes only a weapon dict + scalar grip/room — no Combatant, no measure_gap. A structural
    guard against L0/L2 layer-discipline drift (the plan's own binding rule)."""
    import inspect
    C, core, S, WP, CFG = _mods()
    params = list(inspect.signature(WP.at_circumstance).parameters)
    assert params == ['w', 'grip', 'room'], params
    for p in params[1:]:
        assert 'combatant' not in p.lower() and 'measure_gap' not in p.lower()


def test_heft_percussion_ordering_at_ideal():
    """D2 falsifiable acceptance gate #1: spear < arming < longsword < greatsword at grip=0, greatsword not
    collapsed onto longsword.
    [PHASE-C FLAG, 2026-07-08, U1/ED-PC-0010] same finding as test_combat_heft.py::test_falsifiable_heft_
    ordering — U1's JD-1 PoB recalibration correctly lowers arming/longsword's heft numerator (moving their
    balance back toward the hand, per the ratified 1H band), which drops both below spear's own untouched
    numerator. Not a new defect — the SAME reach-class over-dominance already tracked in HANDOFF_PC.md
    ("SPEAR flat-dominance"). Deliberately left failing; see the other test's docstring for the full account."""
    C, core, S, WP, CFG = _mods()
    h = {n: WP.heft(C.WEAPONS[n]) for n in ('spear', 'arming', 'longsword', 'greatsword')}
    assert h['spear'] < h['arming'] < h['longsword'] < h['greatsword'], h


def test_thrust_protection_grip_invariant():
    """D2 gate #2: a point-selected strike is grip-INVARIANT (Phi_grip>=0.9, effectively 1.0) — bear_spear/spear/
    yari all select 'point' and must not collapse when fully gathered."""
    C, core, S, WP, CFG = _mods()
    for n in ('bear_spear', 'spear', 'yari'):
        c = C.Combatant('x', weapon=n)
        dm, h, sg, sp, spc, se = S.select_mode(c, 'none', True, CFG)
        assert h == 'point', f"{n} did not select point: {h}"
        phi = WP.phi_grip(C.WEAPONS[n], 1.0, h, spc)
        assert phi >= 0.9, f"{n} thrust-protection failed at full gather: {phi}"


def test_phi_grip_nan_guard_staff():
    """D2 gate #4: a centre-balanced staff (S_g(0)<=eps) never NaNs; Phi_grip stays finite (guarded to 1.0) at
    every grip position."""
    import math
    C, core, S, WP, CFG = _mods()
    w = C.WEAPONS['staff']
    for g in (0.0, 0.3, 0.7, 1.0):
        phi = WP.phi_grip(w, g, 'blunt', None)
        assert math.isfinite(phi), (g, phi)


def test_heft_percussion_byte_identical_at_grip_zero():
    """I2 gate #7: at grip=0/room=1.0, heft AND percussion are byte-identical to the pre-I2 ideal-circumstance
    value for the WHOLE roster (Phi==1 everywhere at open measure)."""
    C, core, S, WP, CFG = _mods()
    for n, w in C.WEAPONS.items():
        assert abs(WP.heft(w) - WP.heft(w, grip=0.0, sel_head=w['head'])) < 1e-9, n
        assert abs(WP.percussion_authority(w) - WP.percussion_authority(w, grip=0.0, room=1.0)) < 1e-9, n


def test_damage_retention_worst_case_material_lever():
    """D2/I2 gate #3: a gathered SWING's full-damage retention through core.damage (armour=none, success),
    WORST-CASE across STR 2/4/6/8, clears the plan's material-lever bar: guandao <=0.76, voulge/bardiche <=0.88
    (borderline, JD-1). The gate is about the SWING/CUT degradation (a broad arc loses power when you cannot fully
    extend). [ED-PC-0027: these weapons now SELECT the grip-invariant THRUST in the 1v1 (the T_vuln exposure trade),
    whose damage correctly does NOT degrade with grip — phi_grip('point')==1.0 — so the material lever is measured on
    each weapon's CUT head EXPLICITLY, the mode the gate governs; the thrust's grip-invariance is a separate, correct
    property tested elsewhere.]"""
    C, core, S, WP, CFG = _mods()

    def worst_retention(name, grip_star, cut_head):
        w = C.WEAPONS[name]
        eff, dm, gap, perc, spc, ref = S.afforded_heads(w)[cut_head]
        gap = gap if gap is not None else w['gap']
        perc = perc if perc is not None else WP.percussion_authority(w)
        worst = 0.0
        for STR in (2, 4, 6, 8):
            heft_open = core.heft_resp(w, CFG, grip=0.0, sel_head=cut_head, sel_pc=spc)
            heft_closed = core.heft_resp(w, CFG, grip=grip_star, sel_head=cut_head, sel_pc=spc)
            dmg_open = core.damage('success', heft_open, cut_head, STR, 'none', False, gap, perc)
            dmg_closed = core.damage('success', heft_closed, cut_head, STR, 'none', False, gap, perc)
            worst = max(worst, dmg_closed / dmg_open if dmg_open else 0.0)
        return worst

    assert worst_retention('guandao', 1.0, 'curved_cut') <= 0.76
    assert worst_retention('voulge', 1.0, 'cut_thrust') <= 0.88
    assert worst_retention('bardiche', 0.627, 'straight_cut') <= 0.88


def test_room_no_lever_falls_monotone_down():
    """C4 / D2b: percussion's room degradation is monotone-INCREASING in room (never monotone-down); a thrust
    stays at 0 percussion regardless of room (percussion is blunt-only by construction)."""
    C, core, S, WP, CFG = _mods()
    w = C.WEAPONS['mace']
    vals = [WP.percussion_authority(w, room=r) for r in (0.0, 0.25, 0.5, 0.75, 1.0)]
    assert all(vals[i] <= vals[i + 1] + 1e-9 for i in range(len(vals) - 1)), vals
    w2 = C.WEAPONS['rapier']
    assert all(WP.percussion_authority(w2, room=r) == 0.0 for r in (0.0, 0.5, 1.0))


def test_select_mode_open_measure_identity_single_mode_weapons():
    """I2 gate #5 (BLOCKER-2 + contract equivalence): at open measure (grip=0), select_mode's 5-tuple returns
    sel_gap==w['gap'], sel_perc==percussion_authority(w), sel_pc==the whole-weapon point_concentration for every
    SINGLE-MODE weapon (no mode_elements) — behaviour-preserving until intended."""
    C, core, S, WP, CFG = _mods()
    for n, w in C.WEAPONS.items():
        if 'base' in w or w.get('mode_elements'):
            continue
        c = C.Combatant('x', weapon=n)
        dm, h, sg, sp, spc, se = S.select_mode(c, 'none', False, CFG)
        assert sg == w['gap'], (n, sg, w['gap'])
        assert spc == w['geometry']['point_concentration'], (n, spc)
        if h == 'blunt':
            # sp is None for a weapon whose percussion authority is exactly 0 (e.g. staff — perfectly centre-
            # balanced, PoB_m==0, so the blunt token never clears SELECT_EPS and afforded_heads' degenerate
            # fallback fires); the native-fallback semantics still converge to the same value.
            resolved = sp if sp is not None else WP.percussion_authority(w)
            assert resolved == WP.percussion_authority(w), (n, sp)


def test_select_mode_sel_fields_track_swap_window():
    """I2 gate #5: within the closed exchange, every sel_* field resolves the SAME (post-swap) weapon/element —
    probes the longsword->longsword_halfsword swap window (M-02/R-7's object-confusion class)."""
    C, core, S, WP, CFG = _mods()
    c = C.Combatant('x', weapon='longsword_halfsword')
    dm, h, sg, sp, spc, se = S.select_mode(c, 'heavy', True, CFG)
    w = C.WEAPONS['longsword_halfsword']
    assert sg == w['gap'] or sg == w['geo']['gap']
    assert spc == w['geometry']['point_concentration']


# ── I3 GRIP-AWARE REACH + TWO-RECOMPUTE ER CONTRACT + JD-9 (D3, 2026-07-03) ──────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_reach_base_byte_identical_at_grip_zero():
    """D3 gate #2: Refresh #1 at grip=0 (no swap) reproduces today's frozen er EXACTLY (reach_base was grip-blind
    pre-I3, so grip=0 == today) — verified for the whole roster."""
    C, core, S, WP, CFG = _mods()
    for n, w in C.WEAPONS.items():
        c = C.Combatant('x', weapon=n)
        old = CFG['L0'] + CFG['REACH_GEOM_SCALE'] * (w['head_len'] + CFG['REACH_2H_K'] * w['grip_len'] * (w['hands'] == 2)) + w.get('reach_adj', 0.0)
        new = S.reach_base(c, CFG, grip=0.0)
        assert abs(old - new) < 1e-9, n


def test_reach_corrected_anchors_stay_above_l0():
    """D3 gate #6: a full choke reduces reach by exactly the forward geometry lost, and reach stays > L0 for every
    pole at max realistic choke, matching the plan's measured post-floor targets."""
    C, core, S, WP, CFG = _mods()
    targets = {'spear': 4.940, 'glaive': 5.465, 'poleaxe': 5.347, 'staff': 5.346, 'guisarme': 5.535}
    for n, target in targets.items():
        c = C.Combatant('x', weapon=n)
        r = S.reach_base(c, CFG, grip=1.0)
        assert abs(r - target) < 0.01, (n, r, target)
        assert r > CFG['L0'], n


def test_jd9_grip_target_converges_no_oscillation():
    """JD-9 (capstone finding M1): grip_target's drive term is fixed to grip=0.0, so it no longer depends on its
    own prior output — verified NON-OSCILLATING (in fact single-step) and matching the plan's own converged g*
    table exactly for every gathering pole."""
    C, core, S, WP, CFG = _mods()
    targets = {'spear': 0.865, 'yari': 1.0, 'glaive': 0.467, 'guisarme': 0.396, 'bardiche': 0.627}
    for n, target in targets.items():
        c = C.Combatant('x', weapon=n)
        g1 = S.grip_target(c, True, CFG)
        c.grip_position = g1
        g2 = S.grip_target(c, True, CFG)   # a second call, as if grip_position had been fed back — must NOT move
        assert g1 == g2, (n, g1, g2)
        assert abs(g1 - target) < 0.001, (n, g1, target)


def test_halfsword_form_reach_shorter_post_swap():
    """D3 gate #4: for a form-switching weapon, the post-swap reach reflects the SHORTER half-sword form —
    reach_base on longsword_halfsword < reach_base on longsword."""
    C, core, S, WP, CFG = _mods()
    c_full = C.Combatant('x', weapon='longsword')
    c_half = C.Combatant('x', weapon='longsword_halfsword')
    assert S.reach_base(c_half, CFG, grip=0.0) < S.reach_base(c_full, CFG, grip=0.0)


def test_engagement_reach_derivation_runs_clean():
    """Smoke test: a full engagement (grip-aware reach, the two-recompute er contract, JD-9 fixed-grip drive) runs
    to completion with no exception, for a gathering-pole matchup (the exact case JD-9 exists to fix)."""
    import random
    C, core, S, WP, CFG = _mods()
    import wrapper
    A = C.Combatant('A', weapon='spear')
    B = C.Combatant('B', weapon='arming')
    for seed in range(5):
        wrapper.fight(A, B, cfg=CFG, rng=random.Random(seed))


# ── I4 MODE/MEASURE COUPLING — CLOSE-EFFICACY (D5, 2026-07-03) ──────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_close_efficacy_identity_at_open_measure():
    """D5 gate: close_efficacy is EXACTLY 1.0 (not merely approximate) at open measure (closed=False) or when
    measure_gap is unset — the lever is inert until the fight is genuinely in the close."""
    C, core, S, WP, CFG = _mods()
    assert S.close_efficacy(0.0, None, 1.0, True) == 1.0
    assert S.close_efficacy(0.0, 0.0, 1.0, False) == 1.0
    assert S.close_efficacy(0.0, 6.5, 1.0, True) == 1.0


def test_close_efficacy_arc_vs_thrust_from_selected_element():
    """D5 gate #4: a low-per-element-pc cutter (guandao's cleaver, pc=0.30) degrades in the close, while a
    point-selected thrust barely does. bear_spear is the R-3 case: its WHOLE-WEAPON pc is a moderate 0.55
    (it has no authored mode_elements), which would wrongly degrade a pc-only formula — close_efficacy is gated
    on the SELECTED HEAD (head=='point' -> 1.0 unconditionally, mirroring D2's phi_grip thrust-protection), not
    pc alone, so bear_spear is correctly untouched despite its moderate whole-weapon pc."""
    C, core, S, WP, CFG = _mods()
    guandao_pc = C.WEAPONS['guandao']['mode_elements'][0]['geo']['point_concentration']
    assert S.close_efficacy(guandao_pc, 0.0, 1.0, True, head='curved_cut') < 0.9
    c = C.Combatant('x', weapon='bear_spear')
    dm, h, sg, sp, spc, se = S.select_mode(c, 'none', True, CFG, measure_gap=0.0)
    assert h == 'point'
    assert spc == C.WEAPONS['bear_spear']['geometry']['point_concentration'] == 0.55, "bear_spear has no mode_elements; its moderate whole-weapon pc is the R-3 trap"
    assert S.close_efficacy(spc, 0.0, 1.0, True, head=h) == 1.0, "gated on the SELECTED HEAD, not pc alone"


def test_close_efficacy_shifts_selection_in_tight_quarters():
    """D5: guandao's afforded point element (rear spike, I4/JD-5) out-couples its degraded cleaver once quarters
    are tight enough, even unarmoured — a real, measurable selection shift, not just a magnitude tweak. [ED-PC-0027:
    the T_vuln exposure layer (EXPOSE_SELECT_K) now ALSO prefers the thrust in OPEN measure (the guandao's big cut is
    exposing in a 1v1), which pre-empts and SUBSUMES this shift — the guandao thrusts at every measure. To isolate
    close_efficacy's OWN mechanism (the D5 gate this test governs), the exposure layer is disabled here (K=0); the
    two effects are complementary — close_efficacy discounts a broad arc in the close, exposure discounts it for its
    vulnerability window — and both point the same way.]"""
    C, core, S, WP, CFG = _mods()
    iso = dict(CFG); iso['EXPOSE_SELECT_K'] = 0.0   # isolate close_efficacy from the T_vuln exposure discount
    c = C.Combatant('x', weapon='guandao')
    h_open = S.select_mode(c, 'none', False, iso, measure_gap=None)[1]
    h_close = S.select_mode(c, 'none', True, iso, measure_gap=0.0)[1]
    assert h_open == 'curved_cut'
    assert h_close == 'point'


def test_sel_head_routes_to_reach_threat_and_approach_displace():
    """I4/D5: reach_threat's adef_cap call and approach_displace both now read the SELECTED head (sel_head),
    native fallback only when unset — verified they accept and use the override without raising."""
    C, core, S, WP, CFG = _mods()
    longer = C.Combatant('longer', weapon='poleaxe')
    shorter = C.Combatant('shorter', weapon='dagger')
    defender = C.Combatant('def', weapon='arming', armor='heavy')
    longer.sel_head = 'point'
    rt_point = S.reach_threat(longer, defender, CFG)
    longer.sel_head = 'blunt'
    rt_blunt = S.reach_threat(longer, defender, CFG)
    assert isinstance(rt_point, float) and isinstance(rt_blunt, float)
    longer.sel_head = 'point'
    d = S.approach_displace(shorter, longer, CFG)
    assert d >= 0.0


# ── I5 COMMIT/MEASURE COUPLING — SWING-ROOM (D4, 2026-07-03) ────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_range_utilization_identity():
    """D4/I5: range_utilization is EXACTLY 1.0 at open/roomy measure or when measure_gap is unset — the
    byte-identical default."""
    C, core, S, WP, CFG = _mods()
    assert S.range_utilization(None, None, CFG) == 1.0
    assert S.range_utilization(None, 100.0, CFG) == 1.0
    assert S.range_utilization(None, 0.0, CFG) == S.RANGE_AVAIL_FLOOR


def test_commit_depth_byte_identical_at_range_avail_one():
    """I5 gate #1: with range_avail forced 1.0 (the I1/I5 default), commit_depth reproduces the pre-I5 [2,5] draw
    EXACTLY — a single rng.betavariate draw, no reorder — verified by replaying the same seed through both the
    live function and the pre-I5 formula with the SAME (ba, bb) params."""
    C, core, S, WP, CFG = _mods()
    import random
    import tradition as TR
    agg = C.Combatant('agg', weapon='longsword'); agg.range_avail = 1.0
    dfd = C.Combatant('def', weapon='arming')
    rng = random.Random(11)
    commit, ba, bb, ln = S.commit_depth(agg, dfd, CFG, rng, TR)
    rng2 = random.Random(11)
    # replay commit_depth's own pre-draw computation (ln/wary/g/ba/bb are deterministic, not rng-consuming) then
    # the pre-I5 formula's SAME single draw
    old_commit = 2.0 + 3.0 * float(rng2.betavariate(ba, bb))
    assert commit == old_commit


def test_commit_depth_contracts_with_less_room():
    """D4 gate #2/#3: the commit distribution moves beyond noise as range_avail shrinks (interior-optimum-safe:
    a small loss of room near range_avail=1.0 does NOT immediately shallow commitment; only real crowding does),
    and never falls below the floored minimum span."""
    C, core, S, WP, CFG = _mods()
    assert S._commit_range_factor(0.9) == 1.0            # plateau near full room
    assert S._commit_range_factor(0.0) == S.RANGE_COMMIT_FLOOR
    assert 0.0 < S._commit_range_factor(0.4) < 1.0


def test_swing_room_legibility_zero_at_full_room():
    """D4/D5: the swing-room legibility term is exactly 0 at range_avail=1.0 (the I1/I5 default) — legibility()
    stays byte-identical to pre-I5 there."""
    C, core, S, WP, CFG = _mods()
    c = C.Combatant('x', weapon='greatsword')
    c.range_avail = 1.0
    legib_full = S.legibility(c, 3.0, CFG)
    c.range_avail = 0.3
    legib_cramped = S.legibility(c, 3.0, CFG)
    assert legib_cramped > legib_full, "less room -> a broad swing reads EASIER (higher legibility for the defender)"


def test_stophit_range_term_zero_at_full_room():
    """I5 gate #4: the approach stop-hit's commitment-depth term is exactly 0 at range_avail=1.0."""
    C, core, S, WP, CFG = _mods()
    longer = C.Combatant('longer', weapon='spear'); longer.range_avail = 1.0
    shorter = C.Combatant('shorter', weapon='dagger')
    base = S.stophit_sigma(longer, shorter, 2.0, CFG)
    longer.range_avail = 0.5
    cramped = S.stophit_sigma(longer, shorter, 2.0, CFG)
    assert base != cramped


# ── I6 FACING STATE + LATERAL-VOID CLOSING (D6, 2026-07-03) ─────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_facing_weapon_class_aware_at_shipped_k():
    """I6 gate #3 (C2 REVERSAL), now ACTIVE (U10/ED-PC-0022): FACING_REGIME_K is shipped >0, so the facing regime
    reads weapon class — a 1H weapon (profile, +) and a 2H weapon (square, −) at identical stance/grip now get
    DIFFERENT facing. This is the Jordan-resolved C2 reversal the U7 pin held at K=0; U10 activates it at a
    conservative K (C1 absolute direction still unresolved — see test_facing_near_neutral_small, which still holds)."""
    C, core, S, WP, CFG = _mods()
    assert CFG['FACING_REGIME_K'] > 0.0
    oneh = C.Combatant('a', weapon='sabre'); oneh.grip_position = 0.4       # 1H -> profile (+)
    twoh = C.Combatant('b', weapon='longsword'); twoh.grip_position = 0.4   # 2H -> square (−)
    assert S.facing_target(oneh, True, CFG) != S.facing_target(twoh, True, CFG)
    assert S.facing_target(oneh, False, CFG) != S.facing_target(twoh, False, CFG)


def test_facing_regime_separation():
    """U7/ED-PC-0020: the facing REGIME is wired (inert at K=0, live at K>0). facing_pref is signed by hands — a 1H
    weapon fights PROFILE (+), a 2H weapon SQUARES up (−) — and 'hands separates the twins' (a 1H vs 2H blade of the
    same reach face opposite regimes). Once FACING_REGIME_K>0, facing_target reads the weapon class (the C2 reversal)."""
    C, core, S, WP, CFG = _mods()
    assert WP.facing_pref(C.WEAPONS['sabre']) > 0 and WP.facing_pref(C.WEAPONS['arming']) > 0      # 1H -> profile (+)
    assert WP.facing_pref(C.WEAPONS['longsword']) < 0 and WP.facing_pref(C.WEAPONS['spear']) < 0   # 2H -> square (−)
    # hands separates twins: same head_len, opposite sign
    class _W(dict):
        pass
    w1h = {'hands': 1, 'head_len': 0.84}; w2h = {'hands': 2, 'head_len': 0.84}
    assert WP.facing_pref(w1h) == -WP.facing_pref(w2h) and WP.facing_pref(w1h) > 0
    # live at K>0: two weapons of different class now get different facing
    cfgk = dict(CFG, FACING_REGIME_K=0.6)
    c1 = C.Combatant('a', weapon='sabre'); c1.grip_position = 0.4      # 1H
    c2 = C.Combatant('b', weapon='longsword'); c2.grip_position = 0.4  # 2H
    assert S.facing_target(c1, True, cfgk) != S.facing_target(c2, True, cfgk)


def test_facing_near_neutral_small():
    """I6 gate #2: facing_target is a real but SMALL close contribution — never approaches a large fraction of the
    quantities it feeds into."""
    C, core, S, WP, CFG = _mods()
    c = C.Combatant('x', weapon='longsword'); c.grip_position = 1.0
    assert 0.0 < S.facing_target(c, True, CFG) < 0.15


def test_facing_neutral_byte_identical_to_i5():
    """I6 gate #1: with facing forced to neutral (0.0) for both roles, close_rate and reach_sigma reproduce their
    pre-I6 formulas EXACTLY."""
    C, core, S, WP, CFG = _mods()
    import tradition as TR
    agg = C.Combatant('agg', weapon='longsword'); agg.facing = 0.0
    dfd = C.Combatant('def', weapon='arming'); dfd.facing = 0.0
    er = {agg: 6.0, dfd: 5.0}
    rs = S.reach_sigma(agg, dfd, er, 0.0, 0.0, CFG, TR)
    gap = er[dfd] - er[agg]
    foot_meas = CFG['FOOT_MEASURE_K']*(S.balance_eff(dfd,0.0,CFG)*TR.eff_cw(dfd,'balance') - S.balance_eff(agg,0.0,CFG)*TR.eff_cw(agg,'balance'))
    meas_w = TR.eff_cw(dfd,'measure')/TR.eff_cw(agg,'measure')
    old_reach_edge = (gap*CFG['REACH_FRAC']+foot_meas)*meas_w
    assert rs == CFG['REACH_W'][dfd.armor]*old_reach_edge

    shorter = C.Combatant('s', weapon='dagger'); shorter.facing = 0.0
    cr = S.close_rate(shorter, 0.0, 0.2, 0.9, CFG)
    old_cr = CFG['CLOSE_RATE_K']*S.balance_eff(shorter,0.0,CFG)/3 * S.weapon_tempo(shorter,CFG,0.0)/2
    assert cr == old_cr*(1+0.2)*(2.0-0.9)


def test_facing_no_orient_deg_arc_thrust_gate():
    """I6 gate #4: no code path reads orient_deg for an arc-vs-thrust gate — facing_target and its consumers never
    reference orient_deg at all in R1 (ships as a pure stance/measure/grip signal; only a FUTURE weapon-shape
    promotion would key on orient_deg, and only as fore/aft)."""
    import inspect
    C, core, S, WP, CFG = _mods()
    src = inspect.getsource(S.facing_target) + inspect.getsource(S.close_rate) + inspect.getsource(S.reach_sigma)
    assert 'orient_deg' not in src


# ── I7a REAR-CLEARANCE CLOSE PENALTY (D7, 2026-07-03) ────────────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_rear_clearance_spear_less_than_guisarme():
    """I7a gate #1: rear_clearance(spear) < rear_clearance(guisarme) at open grip."""
    C, core, S, WP, CFG = _mods()
    assert WP.at_circumstance(C.WEAPONS['spear'], 0.0)['rear_clearance'] < WP.at_circumstance(C.WEAPONS['guisarme'], 0.0)['rear_clearance']


def test_rear_clearance_halfsword_forms_exceed_base():
    """I7a gate #1: both half-sword forms' rear_clearance exceeds their base form's (the trailing blade/pommel
    swings further behind the working hand once gripped mid-blade)."""
    C, core, S, WP, CFG = _mods()
    for base, half in (('longsword', 'longsword_halfsword'), ('estoc', 'estoc_halfsword')):
        rc_base = WP.at_circumstance(C.WEAPONS[base], 0.0)['rear_clearance']
        rc_half = WP.at_circumstance(C.WEAPONS[half], 0.0)['rear_clearance']
        assert rc_half > rc_base, (base, half, rc_base, rc_half)


def test_rear_clearance_from_parts_not_length_m():
    """I7a gate #2: rear_clearance is computed from _all_parts, never derive()['length_m'] — a code-level check
    that the two quantities genuinely differ for at least one half-sword composite (where they diverge, M-19)."""
    C, core, S, WP, CFG = _mods()
    w = C.WEAPONS['longsword_halfsword']
    rc = WP.at_circumstance(w, 0.0)['rear_clearance']
    length_m = WP.derive(w)['length_m']
    assert rc != length_m


def test_rear_clearance_monotone_non_decreasing():
    """I7a gate #3: rear_clearance(g) is monotone non-decreasing in grip for the WHOLE roster — gathering in
    never shortens what trails behind the hand."""
    C, core, S, WP, CFG = _mods()
    for n, w in C.WEAPONS.items():
        prev = None
        for g in (0.0, 0.25, 0.5, 0.75, 1.0):
            rc = WP.at_circumstance(w, g)['rear_clearance']
            if prev is not None:
                assert rc >= prev - 1e-9, (n, g, rc, prev)
            prev = rc


def test_rear_clearance_staff_changes_with_grip_despite_zero_u():
    """I7a gate #4 (M-20): the staff's rear_clearance changes with grip even though its inertia u stays 0
    (perfectly centre-balanced) — driven by geom_slide, decoupled from the CoM-clamped u."""
    C, core, S, WP, CFG = _mods()
    w = C.WEAPONS['staff']
    a0 = WP.at_circumstance(w, 0.0)
    a1 = WP.at_circumstance(w, 1.0)
    assert a0['u'] == 0.0 and a1['u'] == 0.0
    assert a1['rear_clearance'] > a0['rear_clearance']


def test_rear_clearance_penalty_moves_close_tempo_and_str_demand():
    """I7a gate #5: a live weapon (nonzero rear_clearance) reads a real close_tempo/str_demand penalty relative to
    a synthetic zero-rear-clearance ablation (patching REAR_CLEARANCE_*_K to 0 reproduces the pre-I7a values)."""
    C, core, S, WP, CFG = _mods()
    c = C.Combatant('x', weapon='guisarme'); c.grip_position = 0.5
    live_tempo = S.close_tempo(c, CFG)
    live_str = S.str_demand(c, CFG)
    old_tempo_k, old_str_k = S.REAR_CLEARANCE_TEMPO_K, S.REAR_CLEARANCE_STR_K
    try:
        S.REAR_CLEARANCE_TEMPO_K = 0.0
        S.REAR_CLEARANCE_STR_K = 0.0
        ablated_tempo = S.close_tempo(c, CFG)
        ablated_str = S.str_demand(c, CFG)
    finally:
        S.REAR_CLEARANCE_TEMPO_K, S.REAR_CLEARANCE_STR_K = old_tempo_k, old_str_k
    assert live_tempo != ablated_tempo
    assert live_str != ablated_str


# ── I7b CONTACT AXIS (D8/D9, M-11, 2026-07-03) ───────────────────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_contact_check_only_in_closed_exchange_tail():
    """I7b acceptance #1 (no grapple path from open measure): the contact.grab_available call sits
    textually AFTER the '----- CLOSED: tempo-gated exchange -----' marker — the Approach branch always
    `continue`s before this point, so it is structurally unreachable from open measure."""
    src = open(os.path.join(ENGINE, 'wrapper.py'), encoding='utf-8').read()
    closed_tail_start = src.index('----- CLOSED: tempo-gated exchange -----')
    contact_check = src.index('CT.grab_available(')
    assert contact_check > closed_tail_start


def test_opening_created_wired_at_all_three_precondition_sites():
    """D8: a unified opening_created flag is set at all three precondition sites (bind entry; the
    beaten-aside/slip-inside DISPLACE success; the deep-commit reopen section's 3 sub-clauses) — NOT
    three parallel grab checks each re-deriving their own opening. Reset once per beat."""
    src = open(os.path.join(ENGINE, 'wrapper.py'), encoding='utf-8').read()
    assert src.count('opening_created=False') == 1   # reset once per beat
    assert src.count('opening_created=True') == 5    # displace success + 3 reopen sub-clauses + bind entry


def test_contact_insertion_point_after_riposte_before_outcome_emit():
    """D8: ONE insertion point in the outcome tail, after hit/bind/riposte all resolve, before the
    'outcome' trace emit — not scattered across the three precondition sites."""
    src = open(os.path.join(ENGINE, 'wrapper.py'), encoding='utf-8').read()
    riposte_flip = src.index("aggressor, defender = defender, aggressor   # role flip")
    contact_check = src.index('CT.grab_available(')
    outcome_emit = src.index("_emit('outcome',")
    assert riposte_flip < contact_check < outcome_emit


# ── I8 STANDING ANTI-ORPHAN TEST (D11b, 2026-07-03) ──────────────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
CIRCUMSTANCE_FIELDS = ('grip_position', 'lunge_depth', 'sel_head', 'sel_dmg',
                       'sel_gap', 'sel_perc', 'sel_pc', 'range_avail', 'facing')


def test_every_circumstance_field_has_a_live_reader():
    """D11b: every per-beat circumstance field the wrapper writes onto a Combatant (the I1 scaffold's
    grip_position/lunge_depth/sel_head/sel_dmg/sel_gap/sel_perc/sel_pc/range_avail/facing) has AT LEAST
    ONE live reader in a consumer layer (core.py/systems.py/contact.py) — never just written by wrapper.py
    (L3, the mutator) and read nowhere. Catches an orphan window left open past its closing increment.
    Source-scans for either direct attribute access (`.field`) or the getattr(...,'field',...) fallback
    idiom core.strike/systems use for these optional fields."""
    consumers_src = "".join(open(os.path.join(ENGINE, mod), encoding='utf-8').read()
                             for mod in ('core.py', 'combat_systems.py', 'contact.py'))
    orphans = []
    for f in CIRCUMSTANCE_FIELDS:
        if not re.search(rf"\.{f}\b|'{f}'|\"{f}\"", consumers_src):
            orphans.append(f)
    assert not orphans, f"circumstance field(s) with NO reader in core.py/systems.py/contact.py: {orphans}"


# ── I8 ABLATION GATES (D11b/JD-1, 2026-07-03) — every lever must move outcomes beyond noise or be cut ──
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md, I8 acceptance #5.
# swing-Φ_grip is already gated by test_damage_retention_worst_case_material_lever (I2's worst-case-STR
# bar); range_avail by test_commit_depth_contracts_with_less_room / test_swing_room_legibility_zero_at_
# full_room (both already assert a nonzero, beyond-noise delta) / test_stophit_range_term_zero_at_full_
# room; rear_clearance by test_rear_clearance_penalty_moves_close_tempo_and_str_demand (I7a). The two
# levers below had no explicit ablation gate yet.
def test_phi_room_percussion_ablation_clears_noise_floor():
    """Percussion-Φ_room (D2b): a synthetic zero-degradation ablation (PERC_ROOM_FLOOR patched to 1.0, so
    phi_room_percussion is identically 1.0 regardless of room) is compared against the live floored
    degradation at a cramped room — the live lever must differ by more than a noise-floor 2%."""
    C, core, S, WP, CFG = _mods()
    w = C.WEAPONS['mace']
    live = WP.percussion_authority(w, room=0.3)
    old_floor = WP.PERC_ROOM_FLOOR
    try:
        WP.PERC_ROOM_FLOOR = 1.0
        ablated = WP.percussion_authority(w, room=0.3)
    finally:
        WP.PERC_ROOM_FLOOR = old_floor
    assert live != ablated
    assert abs(live - ablated) / ablated > 0.02, (live, ablated)


def test_facing_void_ablation_moves_close_rate_and_reach_sigma():
    """Facing void/profile terms (D6): a synthetic zero-gain ablation (the consumer-side FACING_VOID_GAIN
    in close_rate / FACING_PROFILE_K in reach_sigma patched to 0 — NOT facing_target's own FACING_VOID_K,
    which governs the producer, already gated by test_facing_near_neutral_small) is compared against the
    live terms at a real (nonzero, near-neutral) facing value — close_rate and reach_sigma must both move."""
    C, core, S, WP, CFG = _mods()
    import tradition as TR
    shorter = C.Combatant('s', weapon='dagger'); shorter.facing = 0.1
    agg = C.Combatant('agg', weapon='longsword'); agg.facing = 0.1
    dfd = C.Combatant('def', weapon='arming'); dfd.facing = -0.05
    er = {agg: 6.0, dfd: 5.0}
    live_cr = S.close_rate(shorter, 0.0, 0.2, 0.9, CFG)
    live_rs = S.reach_sigma(agg, dfd, er, 0.0, 0.0, CFG, TR)
    old_void_gain, old_profile_k = S.FACING_VOID_GAIN, S.FACING_PROFILE_K
    try:
        S.FACING_VOID_GAIN = 0.0; S.FACING_PROFILE_K = 0.0
        ablated_cr = S.close_rate(shorter, 0.0, 0.2, 0.9, CFG)
        ablated_rs = S.reach_sigma(agg, dfd, er, 0.0, 0.0, CFG, TR)
    finally:
        S.FACING_VOID_GAIN, S.FACING_PROFILE_K = old_void_gain, old_profile_k
    assert live_cr != ablated_cr
    assert live_rs != ablated_rs


def test_reach_class_beats_arming_not_inverted():
    """Reach vs a uniform arming-sword baseline — the GROUNDED, armour-CONDITIONAL ladder.
    [ORIGINAL, I8] guarded that reach (spear/yari/guisarme/poleaxe) never INVERTS into a loss at any armour tier
    — R2's grip/room/facing degradation must not zero the reach advantage.
    [REWRITTEN, PC-5/ED-PC-0015, 2026-07-22] The old blanket "reach beats arming at EVERY tier incl. heavy"
    encoded the pre-PC-5 UNIFORM-plate-defeat assumption (every point defeated plate at the gaps with equal
    authority — the flat ~85% reach dominance that the stress-test session flagged as G4 reach-over-dominance).
    thrust_authority(head_len) grounds it: a point pressed into a harness gap is a SHORT-LEVER pommel-backed act,
    so a long reach-thrust at full extension (spear head_len 1.65, yari 1.86) can no longer defeat plate the way a
    short one can. The reach advantage is now ARMOUR-CONDITIONAL — real vs flesh/cloth/mail, decaying to a loss vs
    plate for a PURE-POINT reach weapon, while a DEDICATED armour-defeating reach weapon (poleaxe: swung spike/
    hammer, percussion path, untouched by thrust_auth) still dominates plate. This test now asserts that grounded
    shape, NOT a blanket dominance. (Guards preserved: reach still dominates every NON-plate tier; nothing is
    annihilated to ~0 — a real zeroing bug still trips the floor.)"""
    import random
    import zlib
    import wrapper
    C, core, S, WP, CFG = _mods()
    share = {}
    for w in ('spear', 'yari', 'guisarme', 'poleaxe'):
        for armor in ('none', 'light', 'medium', 'heavy'):
            # crc32, not hash() — hash() is PYTHONHASHSEED-salted (non-reproducible run-to-run); see
            # workbench/balance.py's _seed() docstring for the same rationale.
            rng = random.Random(zlib.crc32(repr((w, armor)).encode()) % 9999)
            wins = dec = 0
            for i in range(60):
                swap = i >= 30
                A = C.Combatant('A', weapon=(w if not swap else 'arming'), armor=armor)
                B = C.Combatant('B', weapon=('arming' if not swap else w), armor=armor)
                r = wrapper.fight(A, B, CFG, rng)
                if swap: r = -r
                if r == 1: wins += 1; dec += 1
                elif r == -1: dec += 1
            assert dec > 0, (w, armor)
            share[(w, armor)] = wins / dec
    # (1) reach dominates every NON-plate tier for the DEDICATED reach weapons — the reach advantage vs flesh/cloth/mail
    #     is real. (spear/yari long point + poleaxe percussion; guisarme handled separately below.)
    #     [ED-PC-0027, 2026-07-23] the mode-aware heft correction (a thrust no longer carries the swing moment — the
    #     SPEAR flat-dominance root) reduced the spear/yari OFF-plate thrust damage toward the target band: they stay
    #     STRICTLY dominant at none/light (reach unresisted → ~0.70-0.78) but MEDIUM (mail) is now a genuine near-even
    #     contest (~0.50 true, n=60/cell SE~0.09 so the seed can land ~0.45), because mail resists the (now lighter)
    #     thrust while the reach edge persists — EXACTLY the guisarme (1b) situation, given the same near-even guard.
    #     The poleaxe (armour-defeating percussion + spike) stays strictly dominant at every off-plate tier.
    for armor in ('none', 'light', 'medium'):
        assert share[('poleaxe', armor)] > 0.5, f"poleaxe vs arming at {armor}: reach INVERTED off-plate ({share[('poleaxe', armor)]:.2f})"
    for w in ('spear', 'yari'):
        for armor in ('none', 'light'):
            assert share[(w, armor)] > 0.5, f"{w} vs arming at {armor}: reach INVERTED off-plate ({share[(w, armor)]:.2f})"
        assert share[(w, 'medium')] > 0.42, f"{w} vs arming at medium: reach ANNIHILATED ({share[(w, 'medium')]:.2f}) — expected a near-even contest (ED-PC-0027)"
    # (1b) [RE-BASELINED, U10/ED-PC-0022; TIGHTENED ED-PC-0023 per the adversarial review]. The guisarme (versatile
    #     mid-reach hooked polearm) keeps the STRICT >0.5 guard at none/light — the review confirmed it stays solidly
    #     dominant there (~0.68-0.78 at N>=300), so those tiers never needed loosening (my first re-baseline over-broadly
    #     relaxed all three). ONLY the MEDIUM tier is a genuine near-even contest (~0.51-0.53 true, n=60/cell → SE~0.09,
    #     so the hardcoded seed can land ~0.45): activating the edge_lines/choke legibility effects shaves the arming
    #     matchup there (arming's double edge reads harder; the 2H bill telegraphs when gathered — grounded). So medium
    #     gets a tight CONTEST band; none/light stay strict. A real zeroing bug still trips the medium floor.
    for armor in ('none', 'light'):
        assert share[('guisarme', armor)] > 0.5, f"guisarme vs arming at {armor}: reach INVERTED off-plate ({share[('guisarme', armor)]:.2f})"
    assert share[('guisarme', 'medium')] > 0.42, f"guisarme vs arming at medium: reach ANNIHILATED ({share[('guisarme', 'medium')]:.2f}) — expected a near-even contest"
    # (2) at HEAVY, the dedicated armour-defeating reach weapon still dominates (poleaxe's swung spike/hammer defeats plate).
    assert share[('poleaxe', 'heavy')] > 0.5, f"poleaxe vs arming at heavy should still defeat plate ({share[('poleaxe','heavy')]:.2f})"
    # (3) at HEAVY, a PURE-POINT reach weapon is correctly brought BELOW dominance (the grounded G4 correction — a long
    #     reach-thrust cannot press a point into a harness gap). [ED-PC-0027] the mode-aware heft correction dropped the
    #     spear/yari thrust heft (a thrust no longer carries the swing moment), so vs PLATE they are now a near-total
    #     STALEMATE LOSS (~0.05) — historically correct (a spear cannot defeat full plate; the arming can at least close
    #     and attempt the gaps). The old 0.10 floor was calibrated to the pre-correction inflated thrust; a genuine
    #     ZEROING bug (the reach lever going fully dead) is already caught by the STRICT >0.5 none/light assertions
    #     above, so here we assert only that plate correctly brings them below dominance.
    for w in ('spear', 'yari'):
        s = share[(w, 'heavy')]
        assert s < 0.5, f"{w} vs arming at heavy: plate should bring a pure-point reach weapon below dominance, got {s:.2f}"
    # (4) the versatile mid-reach cut_thrust polearm (guisarme) contests plate — neither lost nor runaway. [ED-PC-0027]
    #     it now SELECTS its gap-thrust (point) vs plate under the T_vuln exposure trade (its hooked bill thrusts to the
    #     gaps rather than swinging into a harness), so it contests strongly vs the plate-stalemate arming.
    #     [RE-BASELINED, ED-PC-0029, 2026-07-24] the ceiling rose 0.75->0.87 when `thrust_extension` was RETIRED (an
    #     adversarial physics/HEMA audit found that heft-penalty wrongly de-rated 2H gap-thrusts — the guisarme's plate
    #     bill among them — identically to a greatsword; thrust_authority(head_len) already grounds the long-reach-thrust-
    #     vs-plate decay, so thrust_extension was a spurious DOUBLE penalty). Removing it restored the guisarme's gap-
    #     thrust to its un-penalised strength: true ~0.83-0.85 (n=300). A 2H hooked bill that thrusts to the gaps SHOULD
    #     dominate a 1H arming sword that can barely mark plate — a favoured contest, still bounded below total dominance
    #     (the spear/yari pure-point stalemate-loss guard at (3) confirms plate is not free reach). CEILING 0.92 carries
    #     ~2·SE of n=60 sampling margin over the ~0.85 true value (this hardcoded-seed cell reads 0.80-0.89 across
    #     calibration; SE~0.06 on ~45 decided) — it is a runaway/inversion guard, not a fine balance assertion.
    assert 0.30 <= share[('guisarme', 'heavy')] <= 0.92, f"guisarme vs arming at heavy should contest ({share[('guisarme','heavy')]:.2f})"
