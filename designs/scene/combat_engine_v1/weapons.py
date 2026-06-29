"""weapons.py — the WEAPONS DICTIONARY: each weapon as an AGGREGATE of physical primitives.

The data half of the weapon split (the derivation half is weapon_physics.py). A weapon is a bundle of primitives;
behaviour EMERGES upward through weapon_physics, never from a per-weapon behaviour table. This module owns ONLY the
primitive data + the build-time geometry bake; it imports nothing from the engine and is the single source every
consumer reads (today via `combatant.WEAPONS`, which re-exports this).

PRIMITIVE SCHEMA (per weapon):
  PHYSICAL   mass(kg) · head_len · grip_len (length-units) · pommel_kg · wclass{bladed,hafted_tip,hafted_block} ·
             hilt{compound,simple,none} · hands(1/2) · reach_adj
  GUARD      hand_guard(0-1 passive hand protection) · blade_guard(0-1 active blade-catch/wind utility)
  HEAD       head{point,cut_thrust,straight_cut,curved_cut,blunt} · clinch(grappling affinity)
  GEOMETRY   curvature · point_concentration · cross_section · edge_keenness · strike_concentration  (-> geo bake)
  LEGACY (retiring; derived in weapon_physics, kept until Phase-3 wiring): reach{long/short} · wt{light/heavy} ·
             spd · gap · percussion · pob_frac · closes_poorly · hand{Forgiving/Standard/Demanding}
"""

# canonical weapon axis-vectors (weapon_axes_v2 §5)
WEAPONS = {
 'rapier':   dict(reach='long', wt='light', hands=1, head='point',  spd=1.5, hand='Demanding', gap=0.40, head_len=3.2, grip_len=0.6, hand_guard=0.90, blade_guard=0.45, reach_adj=0.15, clinch=2, percussion=0, mass=1.3, pob_frac=0.1),
 'arming':   dict(reach='long', wt='light', hands=1, head='cut_thrust', spd=1.5, hand='Standard', gap=0.65, head_len=2.4, grip_len=0.8, hand_guard=0.40, blade_guard=0.55, reach_adj=-0.6, clinch=4, percussion=2, mass=1.2, pob_frac=0.12),
 'longsword':dict(reach='long', wt='heavy', hands=2, head='cut_thrust', spd=0.5, hand='Standard', gap=0.90, head_len=2.8, grip_len=1.6, hand_guard=0.45, blade_guard=0.85, reach_adj=-0.9, clinch=6, percussion=4, mass=1.4, pob_frac=0.14),
 'greatsword':dict(reach='long',wt='heavy', hands=2, head='straight_cut', spd=0.0, hand='Demanding', gap=0.70, head_len=3.6, grip_len=1.8, hand_guard=0.55, blade_guard=0.70, reach_adj=-0.05, clinch=3, percussion=3, mass=2.7, pob_frac=0.22),
 'sabre':    dict(reach='long', wt='light', hands=1, head='curved_cut', spd=2.0, hand='Standard', gap=0.40, head_len=2.6, grip_len=0.7, hand_guard=0.70, blade_guard=0.45, reach_adj=-0.1, clinch=3, percussion=1, mass=0.9, pob_frac=0.18),
 'dagger':   dict(reach='short',wt='light', hands=1, head='cut_thrust', spd=3.0, hand='Forgiving', gap=1.00, head_len=0.7, grip_len=0.4, hand_guard=0.30, blade_guard=0.40, clinch=10, percussion=1, mass=0.3, pob_frac=0.25),
 'paired_short':dict(reach='short',wt='light',hands=1,head='cut_thrust', spd=2.5, hand='Demanding', gap=0.65, head_len=1.4, grip_len=0.5, hand_guard=0.55, blade_guard=0.50, reach_adj=1.4, clinch=5, percussion=2, mass=0.7, pob_frac=0.22),
 'spear':    dict(reach='long', wt='light', hands=2, head='point',  spd=0.0, hand='Forgiving', gap=0.70, head_len=5.5, grip_len=1.2, hand_guard=0.10, blade_guard=0.20, clinch=2, percussion=1, closes_poorly=True, mass=2.0, pob_frac=0.42),
 'staff':    dict(reach='long', wt='light', hands=2, head='blunt',  spd=0.0, hand='Forgiving', gap=0.20, head_len=2.8, grip_len=2.8, hand_guard=0.15, blade_guard=0.30, reach_adj=0.5, clinch=3, percussion=4, closes_poorly=True, mass=1.5, pob_frac=0.05),
 'mace':     dict(reach='long', wt='heavy', hands=1, head='blunt',  spd=0.0, hand='Forgiving', gap=0.20, head_len=1.8, grip_len=0.7, hand_guard=0.45, blade_guard=0.30, reach_adj=-0.55, clinch=4, percussion=8, mass=1.2, pob_frac=0.6),
 'poleaxe':  dict(reach='long', wt='heavy', hands=2, head='blunt',  spd=-0.5,hand='Demanding', gap=0.85, head_len=2.2, grip_len=2.2, hand_guard=0.30, blade_guard=0.60, reach_adj=-0.05, clinch=5, percussion=8, mass=2.5, pob_frac=0.45),
 # half-sword: the SHORTENED longsword (mit dem kurzen Schwert) — one hand grips the blade. Auto-switched form.
 'longsword_halfsword':dict(reach='short', wt='heavy', hands=2, head='point', spd=-0.5, hand='Demanding', gap=1.00, head_len=1.4, grip_len=2.6, hand_guard=0.35, blade_guard=0.25, clinch=7, percussion=4, base='longsword', mass=1.4, pob_frac=0.12),
}

# ---- WEAPON GEOMETRY (build-time inputs to geometry.bake; see geometry.py) ----
GEOMETRY = {
  'rapier': dict(curvature=0.0, point_concentration=0.95, cross_section=0.4, edge_keenness=0.3, strike_concentration=0.0),
  'arming': dict(curvature=0.05, point_concentration=0.6, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
  'longsword': dict(curvature=0.0, point_concentration=0.8, cross_section=0.9, edge_keenness=0.8, strike_concentration=0.1),
  'greatsword': dict(curvature=0.0, point_concentration=0.62, cross_section=0.82, edge_keenness=0.8, strike_concentration=0.1),
  'sabre': dict(curvature=0.55, point_concentration=0.45, cross_section=0.5, edge_keenness=0.9, strike_concentration=0.0),
  'dagger': dict(curvature=0.0, point_concentration=0.95, cross_section=0.97, edge_keenness=0.8, strike_concentration=0.0),
  'paired_short': dict(curvature=0.05, point_concentration=0.65, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
  'spear': dict(curvature=0.0, point_concentration=0.78, cross_section=0.82, edge_keenness=0.4, strike_concentration=0.0),
  'staff': dict(curvature=0.0, point_concentration=0.05, cross_section=0.55, edge_keenness=0.0, strike_concentration=0.15),
  'mace': dict(curvature=0.0, point_concentration=0.02, cross_section=0.85, edge_keenness=0.0, strike_concentration=0.45),
  'poleaxe': dict(curvature=0.0, point_concentration=0.78, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.85),
  'longsword_halfsword': dict(curvature=0.0, point_concentration=0.85, cross_section=0.95, edge_keenness=0.5, strike_concentration=0.1),
}

# COMPOSITE-MASS primitives (weapon_physics §4, recovered 2026-06-22): the three primitives the {mass,head_len,
# grip_len} set lacked, so PoB DERIVES from an iron-on-wood mass model rather than being hand-set.
#   wclass — bladed (grip+blade+pommel) / hafted_tip (wood shaft + iron point) / hafted_block (haft + iron head).
#   hilt   — guard mass at the cross: compound (cup/swept ~0.30kg) / simple (cross ~0.12) / none.
#   pommel_kg — iron counterweight at the hand, back-solved from sourced specimen PoB (bladed weapons only).
COMPOSITE = {
 'rapier':   dict(wclass='bladed', hilt='compound', pommel_kg=0.348),
 'arming':   dict(wclass='bladed', hilt='simple',   pommel_kg=0.234),
 'longsword':dict(wclass='bladed', hilt='simple',   pommel_kg=0.140),
 'greatsword':dict(wclass='bladed', hilt='simple',  pommel_kg=0.548),
 'sabre':    dict(wclass='bladed', hilt='simple',   pommel_kg=0.195),
 'dagger':   dict(wclass='bladed', hilt='none',     pommel_kg=0.021),
 'paired_short':dict(wclass='bladed', hilt='none',  pommel_kg=0.202),
 'longsword_halfsword':dict(wclass='bladed', hilt='simple', pommel_kg=0.140),
 'spear':    dict(wclass='hafted_tip',   hilt='none', pommel_kg=0.0, is_poleaxe=False),
 'staff':    dict(wclass='hafted_tip',   hilt='none', pommel_kg=0.0, is_poleaxe=False),
 'poleaxe':  dict(wclass='hafted_tip',   hilt='none', pommel_kg=0.0, is_poleaxe=True),
 'mace':     dict(wclass='hafted_block', hilt='none', pommel_kg=0.0, is_poleaxe=False),
}

# Bake the precalculated coefficient surface ONCE at import (zero added runtime cost): geometry derives `gap`
# (and thrust/cut/perc_conc/halfsword for downstream wiring) from each weapon's geometry, overriding hand-set gap;
# then merge the composite-mass primitives into the dictionary.
import geometry as _geo
for _w, _params in GEOMETRY.items():
    if _w in WEAPONS:
        _b = _geo.bake(_params)
        WEAPONS[_w]['gap'] = _b['gap']
        WEAPONS[_w]['geo'] = _b   # full baked surface available to modules
for _w, _c in COMPOSITE.items():
    if _w in WEAPONS:
        WEAPONS[_w].update(_c)
