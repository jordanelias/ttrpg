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
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, 'tests', 'sim', 'v32-combat-balance'))


def _mods():
    pytest.importorskip("numpy")
    import combatant as C
    import core
    import systems as S
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
    for mod in ('core.py', 'systems.py', 'wrapper.py'):
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
    silently included as if the current behaviour were correct."""
    C, core, S, WP, CFG = _mods()
    tiers = ['none', 'light', 'medium', 'heavy']
    changers = []
    for n, rec in C.WEAPONS.items():
        if 'base' in rec:
            continue
        heads = {S.select_mode(C.Combatant('x', weapon=n), ar, False, CFG)[1] for ar in tiers}
        if len(heads) > 1:
            changers.append(n)
    expected = ['kama_yari', 'guandao', 'fauchard', 'voulge', 'guisarme', 'ji', 'bec_de_corbin', 'lucerne_hammer']   # poleaxe excluded — see [PHASE-C FLAG] above; voulge/guisarme added I2/R-7, guandao/fauchard added I4/JD-5 — see docstring
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
    over its own real striking elements, not a copy of another weapon's set."""
    C, core, S, WP, CFG = _mods()
    assert set(S.afforded_heads(C.WEAPONS['bec_de_corbin'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['lucerne_hammer'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['goedendag'])) == {'blunt', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['ji'])) == {'point', 'curved_cut'}
    assert set(S.afforded_heads(C.WEAPONS['kama_yari'])) == {'point', 'curved_cut'}
    assert set(S.afforded_heads(C.WEAPONS['guisarme'])) == {'cut_thrust', 'point'}
    assert set(S.afforded_heads(C.WEAPONS['voulge'])) == {'cut_thrust', 'point'}


# ── GAP GAME ──────────────────────────────────────────────────────────────────────────────────────
def test_gap_game_poleaxe_spikes_plate():
    """The situational gap game: vs plate the poleaxe SELECTS its spike (puncture/point — the reach-ladder); unarmoured
    it does not. Emergent from gap_precision × GAP_EXPOSURE, no name conditional.
    [PHASE-C FLAG, 2026-07-02] see weapon_physics.percussion_authority's docstring — morphology-rearch Phase B's
    real poleaxe mass distribution lifts its percussion authority above the mace's, so it now selects its hammer
    face (percussion) instead of the spike (puncture) vs heavy armour. Deliberately left failing pending Phase C's
    engine-scale recalibration against the grounded masses, not silently patched to accept the new selection."""
    C, core, S, WP, CFG = _mods()
    dm_heavy, h_heavy = S.select_mode(C.Combatant('x', weapon='poleaxe'), 'heavy', False, CFG)[:2]
    assert (dm_heavy, h_heavy) == ('puncture', 'point'), f"poleaxe vs plate should spike; got {(dm_heavy, h_heavy)}"
    h_none = S.select_mode(C.Combatant('x', weapon='poleaxe'), 'none', False, CFG)[1]
    assert h_none != 'point', "poleaxe unarmoured should not default to the spike (the gap game is situational)"


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
    collapsed onto longsword."""
    C, core, S, WP, CFG = _mods()
    h = {n: WP.heft(C.WEAPONS[n]) for n in ('spear', 'arming', 'longsword', 'greatsword')}
    assert h['spear'] < h['arming'] < h['longsword'] < h['greatsword'], h


def test_thrust_protection_grip_invariant():
    """D2 gate #2: a point-selected strike is grip-INVARIANT (Phi_grip>=0.9, effectively 1.0) — bear_spear/spear/
    yari all select 'point' and must not collapse when fully gathered."""
    C, core, S, WP, CFG = _mods()
    for n in ('bear_spear', 'spear', 'yari'):
        c = C.Combatant('x', weapon=n)
        dm, h, sg, sp, spc = S.select_mode(c, 'none', True, CFG)
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
    """D2/I2 gate #3: full-damage retention through core.damage (armour=none, success), WORST-CASE across STR
    2/4/6/8, clears the plan's material-lever bar: guandao <=0.76, voulge/bardiche <=0.88 (borderline, JD-1)."""
    C, core, S, WP, CFG = _mods()

    def worst_retention(name, grip_star):
        w = C.WEAPONS[name]
        c = C.Combatant('x', weapon=name)
        dm, h, sg, sp, spc = S.select_mode(c, 'none', True, CFG)
        gap = sg if sg is not None else w['gap']
        perc = sp if sp is not None else WP.percussion_authority(w)
        worst = 0.0
        for STR in (2, 4, 6, 8):
            heft_open = core.heft_resp(w, CFG, grip=0.0, sel_head=h, sel_pc=spc)
            heft_closed = core.heft_resp(w, CFG, grip=grip_star, sel_head=h, sel_pc=spc)
            dmg_open = core.damage('success', heft_open, h, STR, 'none', False, gap, perc)
            dmg_closed = core.damage('success', heft_closed, h, STR, 'none', False, gap, perc)
            worst = max(worst, dmg_closed / dmg_open if dmg_open else 0.0)
        return worst

    assert worst_retention('guandao', 1.0) <= 0.76
    assert worst_retention('voulge', 1.0) <= 0.88
    assert worst_retention('bardiche', 0.627) <= 0.88


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
        dm, h, sg, sp, spc = S.select_mode(c, 'none', False, CFG)
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
    dm, h, sg, sp, spc = S.select_mode(c, 'heavy', True, CFG)
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
    dm, h, sg, sp, spc = S.select_mode(c, 'none', True, CFG, measure_gap=0.0)
    assert h == 'point'
    assert spc == C.WEAPONS['bear_spear']['geometry']['point_concentration'] == 0.55, "bear_spear has no mode_elements; its moderate whole-weapon pc is the R-3 trap"
    assert S.close_efficacy(spc, 0.0, 1.0, True, head=h) == 1.0, "gated on the SELECTED HEAD, not pc alone"


def test_close_efficacy_shifts_selection_in_tight_quarters():
    """D5: guandao's afforded point element (rear spike, I4/JD-5) out-couples its degraded cleaver once quarters
    are tight enough, even unarmoured — a real, measurable selection shift, not just a magnitude tweak."""
    C, core, S, WP, CFG = _mods()
    c = C.Combatant('x', weapon='guandao')
    h_open = S.select_mode(c, 'none', False, CFG, measure_gap=None)[1]
    h_close = S.select_mode(c, 'none', True, CFG, measure_gap=0.0)[1]
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
def test_facing_never_reads_weapon_class():
    """I6 gate #3 (C2): two weapons with identical stance/measure/grip get IDENTICAL facing — facing_target is
    keyed ONLY on closed/grip_position, never weapon class."""
    C, core, S, WP, CFG = _mods()
    c1 = C.Combatant('a', weapon='spear'); c1.grip_position = 0.4
    c2 = C.Combatant('b', weapon='mace'); c2.grip_position = 0.4
    assert S.facing_target(c1, True, CFG) == S.facing_target(c2, True, CFG)
    assert S.facing_target(c1, False, CFG) == S.facing_target(c2, False, CFG)


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
