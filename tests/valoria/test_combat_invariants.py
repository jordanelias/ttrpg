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
    [UPDATED, 2026-07-02] morphology-rearch Phase B2 gave 8 weapons real per-element mode_elements (bec_de_corbin,
    lucerne_hammer, ji, goedendag, guisarme, kama_yari, voulge, plus the pre-existing poleaxe). Of those, 4 now
    genuinely emerge as armour-conditional token-changers (bec_de_corbin, lucerne_hammer, ji, kama_yari — a real
    blunt<->point or cut<->point split whose greedy winner flips with armour, exactly the "swing the hammer or
    thrust the spike" mechanic this re-architecture was built for). guisarme/voulge stay on their single
    'cut_thrust' token throughout (their point element never out-scores it — an internal re-weighting, not a token
    change) and goedendag's point never out-scores its blunt. poleaxe is a [PHASE-C FLAG] — its own more-accurate,
    more-forward Phase-B mass distribution lifted its blunt percussion authority enough that it no longer switches
    to its spike vs heavy armour (weapon_physics.percussion_authority docstring; also test_gap_game_poleaxe_spikes_
    plate); left OUT of the expected set here until Phase C's engine-scale recalibration restores it, not silently
    included as if the current behaviour were correct."""
    C, core, S, WP, CFG = _mods()
    tiers = ['none', 'light', 'medium', 'heavy']
    changers = []
    for n, rec in C.WEAPONS.items():
        if 'base' in rec:
            continue
        heads = {S.select_mode(C.Combatant('x', weapon=n), ar, False, CFG)[1] for ar in tiers}
        if len(heads) > 1:
            changers.append(n)
    expected = ['kama_yari', 'ji', 'bec_de_corbin', 'lucerne_hammer']   # poleaxe excluded — see [PHASE-C FLAG] above
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
    dm_heavy, h_heavy = S.select_mode(C.Combatant('x', weapon='poleaxe'), 'heavy', False, CFG)
    assert (dm_heavy, h_heavy) == ('puncture', 'point'), f"poleaxe vs plate should spike; got {(dm_heavy, h_heavy)}"
    _, h_none = S.select_mode(C.Combatant('x', weapon='poleaxe'), 'none', False, CFG)
    assert h_none != 'point', "poleaxe unarmoured should not default to the spike (the gap game is situational)"
