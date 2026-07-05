"""U0 — units honesty (ED-PC-0002; consolidation_v1.md §4, R3 unified sequence, first increment).

head_len/grip_len (and every derived grip/lever/reach threshold) converted from the 0.30 m
"length-unit" to HONEST METRES: weapons.py stored lengths ×0.30, weapon_physics.UNIT_M deleted,
per-length gains rescaled /0.30 (PERC_2H_ARC, LEVER_K, REACH_GEOM_SCALE), stored-length constants
×0.30 (PERC_GRIP_1H, GRIP_SHORT/GRIP_LONG, LEVER_REF, REC_GRIP_REF, GRAB_SHORT_REACH_M — renamed
from GRAB_SHORT_REACH_LU), wind's edge-length saturation 3.0 lu -> 0.90 m.

CONTRACT: byte-identical at 1e-9 against tests/valoria/r3_identity_golden.json — the OLD-vs-NEW
identity-sweep fixture built ONCE pre-edit on the post-#72 tree (the §4 process wrapper's
mechanism; later byte-identical increments reuse the same fixture). The fixture stores all
lengths in METRES (unit-invariant), so it compares directly on both sides of the conversion.
NEVER hand-edit the fixture; a deliberate re-baseline increment (U1/U2/U9) regenerates it with
recorded reasons.
"""
import json
import math
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

GOLDEN_PATH = os.path.join(os.path.dirname(__file__), 'r3_identity_golden.json')
TOL = 1e-9
GRIPS = (0.0, 0.25, 0.5, 0.75, 1.0)


def _mods():
    pytest.importorskip("numpy")
    import combatant as C
    import systems as S
    import weapon_physics as WP
    from config import CFG
    return C, S, WP, CFG


def _cmp(errs, name, path, old, new):
    if isinstance(old, bool) or isinstance(old, str):
        if old != new:
            errs.append((name, path, old, new))
        return
    if abs(old - new) > TOL:
        errs.append((name, path, old, new))


def test_units_refactor_byte_identical():
    """Every consumer-visible derived quantity — mass family, dynamics, circumstance bundle,
    percussion/heft, defence affinities, and the systems-level reach/tempo/leverage/recovery
    consumers — reproduces the pre-U0 golden at 1e-9, for the full 53-weapon roster."""
    C, S, WP, CFG = _mods()
    golden = json.load(open(GOLDEN_PATH, encoding='utf-8'))['weapons']
    assert set(golden) == set(C.WEAPONS), "fixture must cover the full roster exactly"
    errs = []
    for n, g in golden.items():
        w = C.WEAPONS[n]
        d = WP.derive(w)
        for k, v in g['derive'].items():
            _cmp(errs, n, f'derive.{k}', v, d[k])
        _cmp(errs, n, 'agility', g['agility'], WP.agility(w))
        _cmp(errs, n, 'energy_credit', g['energy_credit'], WP.energy_credit(w))
        _cmp(errs, n, 'handling', g['handling'], WP.handling(w))
        da = WP.defense_affinities(w)
        for k, v in g['defense_affinities'].items():
            _cmp(errs, n, f'defense_affinities.{k}', v, da[k])
        _cmp(errs, n, 'hand_guard_fn', g['hand_guard_fn'], WP.hand_guard(w))
        _cmp(errs, n, 'blade_guard_fn', g['blade_guard_fn'], WP.blade_guard(w))
        _cmp(errs, n, 'distraction', g['distraction'], WP.distraction(w))
        _cmp(errs, n, 'edge_vibration', g['edge_vibration'], WP.edge_vibration(w))
        _cmp(errs, n, 'grip_choke_max', g['grip_choke_max'], WP.grip_choke_max(w))
        _cmp(errs, n, 'grip_travel_max', g['grip_travel_max'], WP.grip_travel_max(w))
        _cmp(errs, n, 'armour_defeat_mode', g['armour_defeat_mode'], WP.armour_defeat_mode(w))
        _cmp(errs, n, 'baked_hand_guard', g['baked_hand_guard'], w['hand_guard'])
        _cmp(errs, n, 'baked_blade_guard', g['baked_blade_guard'], w['blade_guard'])
        _cmp(errs, n, 'gap', g['gap'], w['gap'])
        for rec in g['at_circumstance']:
            a = WP.at_circumstance(w, rec['grip'])
            for k in ('I_g', 'S_g', 'd_g', 'u', 'rear_clearance'):
                _cmp(errs, n, f'at_circumstance[{rec["grip"]}].{k}', rec[k], a[k])
            # geom_slide is stored in METRES in the fixture; post-U0 the live value IS metres
            _cmp(errs, n, f'at_circumstance[{rec["grip"]}].geom_slide_m',
                 rec['geom_slide_m'], a['geom_slide'])
        for i, gg in enumerate(GRIPS):
            _cmp(errs, n, f'grip_swing_ratio[{gg}]', g['grip_swing_ratio'][i], WP.grip_swing_ratio(w, gg))
            _cmp(errs, n, f'phi_grip_native[{gg}]', g['phi_grip_native'][i], WP.phi_grip(w, gg, w['head']))
            _cmp(errs, n, f'phi_grip_point[{gg}]', g['phi_grip_point'][i], WP.phi_grip(w, gg, 'point'))
            _cmp(errs, n, f'puncture_pressure[{gg}]', g['puncture_pressure'][i], WP.puncture_pressure(w, grip=gg))
            _cmp(errs, n, f'heft[{gg}]', g['heft'][i], WP.heft(w, grip=gg))
        for rec in g['percussion_authority']:
            _cmp(errs, n, f'percussion[{rec["grip"]},{rec["room"]}]', rec['v'],
                 WP.percussion_authority(w, grip=rec['grip'], room=rec['room']))
        _cmp(errs, n, 'heft_point_override', g['heft_point_override'],
             WP.heft(w, grip=0.5, sel_head='point', sel_pc=0.5))
        for gg in ('0.0', '0.5', '1.0'):
            c = C.Combatant('x', weapon=n)
            c.grip_position = float(gg)
            sg = g['systems'][gg]
            _cmp(errs, n, f'systems[{gg}].reach_base', sg['reach_base'], S.reach_base(c, CFG))
            _cmp(errs, n, f'systems[{gg}].wield_heft', sg['wield_heft'], S.wield_heft(c, CFG))
            _cmp(errs, n, f'systems[{gg}].weapon_tempo', sg['weapon_tempo'], S.weapon_tempo(c, CFG))
            _cmp(errs, n, f'systems[{gg}].close_tempo', sg['close_tempo'], S.close_tempo(c, CFG))
            _cmp(errs, n, f'systems[{gg}].str_demand', sg['str_demand'], S.str_demand(c, CFG))
            _cmp(errs, n, f'systems[{gg}].rear_clearance', sg['rear_clearance'], S.rear_clearance(c, CFG))
            _cmp(errs, n, f'systems[{gg}].close_unwieldiness', sg['close_unwieldiness'], S.close_unwieldiness(c, CFG))
            _cmp(errs, n, f'systems[{gg}].recoverability_factor', sg['recoverability_factor'], S.recoverability_factor(c, CFG))
        c = C.Combatant('x', weapon=n)
        c.lunge_depth = 0.4
        _cmp(errs, n, 'systems.lunged.recoverability_factor',
             g['systems']['lunged']['recoverability_factor'], S.recoverability_factor(c, CFG))
        _cmp(errs, n, 'systems.lunged.weapon_tempo',
             g['systems']['lunged']['weapon_tempo'], S.weapon_tempo(c, CFG))
        c2 = C.Combatant('x', weapon=n)
        _cmp(errs, n, 'systems.leverage', g['systems']['leverage'], S.leverage(c2, CFG))
        _cmp(errs, n, 'systems.lunge_quality', g['systems']['lunge_quality'], S.lunge_quality(c2, CFG))
        _cmp(errs, n, 'systems.grip_target_closed', g['systems']['grip_target_closed'], S.grip_target(c2, True, CFG))
        _cmp(errs, n, 'systems.can_choke', g['systems']['can_choke'], S.can_choke(c2, CFG))
        _cmp(errs, n, 'systems.grab_short_reach', g['systems']['grab_short_reach'],
             bool(w['head_len'] <= CFG['GRAB_SHORT_REACH_M']))
    assert not errs, f"{len(errs)} identity violations (first 10): {errs[:10]}"


def test_no_length_unit_indirection_remains():
    """The 0.30 m length-unit is fully retired: no UNIT_M symbol survives in the engine, and the
    two honest-metre spot anchors hold (rapier blade 0.96 m, spear forward shaft 1.65 m — the
    values weapon_physics' old UNIT_M comment length-validated as 1.14 m / 2.01 m TOTAL lengths)."""
    C, S, WP, CFG = _mods()
    assert not hasattr(WP, 'UNIT_M'), "weapon_physics.UNIT_M must be deleted, not kept as an alias"
    assert 'GRAB_SHORT_REACH_LU' not in CFG and 'GRAB_SHORT_REACH_M' in CFG
    r, s = C.WEAPONS['rapier'], C.WEAPONS['spear']
    assert math.isclose(r['head_len'] + r['grip_len'], 1.14, abs_tol=1e-9)   # rapier 1.14 m overall
    assert math.isclose(s['head_len'] + s['grip_len'], 2.01, abs_tol=1e-9)   # spear 2.01 m overall
