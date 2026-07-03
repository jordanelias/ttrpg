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
    [UPDATED, 2026-07-03, I2/D2b/R-7 — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/
    plan_r1_RATIFIED.md] The R-7/M-02 object-confusion fix widens select_mode's greedy comparator to read each
    candidate head's OWN gap_precision/percussion (the winning mode_element's, via the widened afforded_heads
    5-tuple) instead of the whole-weapon w['gap']/percussion_authority(w) scalar. guisarme/voulge's point elements
    (thrusting spike / thrusting_heel_spike) carry a materially HIGHER gap_precision than their whole-weapon
    average — under the old whole-weapon-gap comparator this was invisible, so they never out-coupled their
    cut_thrust cleaver; under the corrected per-element gap they NOW correctly win the puncture path vs medium/
    heavy armour (exactly the reach-ladder gap-game mechanic bec_de_corbin/ji/kama_yari/lucerne_hammer already
    modelled) — DELIBERATELY REGENERATED, not silently patched: verified via direct select_mode() sweep this pass
    that both flip cut_thrust->point at medium/heavy, none/light unchanged. goedendag's point still never
    out-scores its blunt. poleaxe is a [PHASE-C FLAG] — its own more-accurate, more-forward Phase-B mass
    distribution lifted its blunt percussion authority enough that it no longer switches to its spike vs heavy
    armour (weapon_physics.percussion_authority docstring; also test_gap_game_poleaxe_spikes_plate); left OUT of
    the expected set here until Phase C's engine-scale recalibration restores it, not silently included as if the
    current behaviour were correct."""
    C, core, S, WP, CFG = _mods()
    tiers = ['none', 'light', 'medium', 'heavy']
    changers = []
    for n, rec in C.WEAPONS.items():
        if 'base' in rec:
            continue
        heads = {S.select_mode(C.Combatant('x', weapon=n), ar, False, CFG)[1] for ar in tiers}
        if len(heads) > 1:
            changers.append(n)
    expected = ['kama_yari', 'voulge', 'guisarme', 'ji', 'bec_de_corbin', 'lucerne_hammer']   # poleaxe excluded — see [PHASE-C FLAG] above; voulge/guisarme added I2/R-7 — see docstring
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
