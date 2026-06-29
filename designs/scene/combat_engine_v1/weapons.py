"""weapons.py — the WEAPONS DICTIONARY: each weapon ONE record, an aggregate of physical primitives.

The data half of the weapon split (the derivation half is weapon_physics.py). A weapon is a bundle of primitives;
behaviour EMERGES upward through weapon_physics, never from a per-weapon behaviour table. Each weapon is a SINGLE
record here — to add / remove / edit a weapon you touch exactly one entry (previously the data was scattered across
three parallel name-keyed dicts; consolidated 2026-06-29 per the architecture audit).

RECORD SCHEMA (per weapon):
  PHYSICAL   mass(kg) · head_len · grip_len (length-units) · hands(1/2) · head{point,cut_thrust,straight_cut,
             curved_cut,blunt} · clinch(grappling affinity) · hand_guard(0-1) · blade_guard(0-1) · reach_adj
  COMPOSITE  wclass{bladed,hafted_tip,hafted_block} · hilt{compound,simple,none} · pommel_kg · is_poleaxe
  GEOMETRY   geometry=dict(curvature, point_concentration, cross_section, edge_keenness, strike_concentration) -> bake
  LEGACY (derived in weapon_physics; live until the Phase-3 wiring): reach{long/short} · wt{light/heavy} · spd ·
             percussion · pob_frac · hand{Forgiving/Standard/Demanding}.  `gap`/`geo` are DERIVED by the bake below.
"""

WEAPONS = {
 'rapier': dict(
   mass=1.3, head_len=3.2, grip_len=0.6, hands=1, head='point', clinch=2, hand_guard=0.9, blade_guard=0.45, reach_adj=0.15,
   wclass='bladed', hilt='compound', pommel_kg=0.348,
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.4, edge_keenness=0.3, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, percussion=0, pob_frac=0.1, hand='Demanding'),
 'arming': dict(
   mass=1.2, head_len=2.4, grip_len=0.8, hands=1, head='cut_thrust', clinch=4, hand_guard=0.4, blade_guard=0.55, reach_adj=-0.6,
   wclass='bladed', hilt='simple', pommel_kg=0.234,
   geometry=dict(curvature=0.05, point_concentration=0.6, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, percussion=2, pob_frac=0.12, hand='Standard'),
 'longsword': dict(
   mass=1.4, head_len=2.8, grip_len=1.6, hands=2, head='cut_thrust', clinch=6, hand_guard=0.45, blade_guard=0.85, reach_adj=-0.9,
   wclass='bladed', hilt='simple', pommel_kg=0.14,
   geometry=dict(curvature=0.0, point_concentration=0.8, cross_section=0.9, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.5, percussion=4, pob_frac=0.14, hand='Standard'),
 'greatsword': dict(
   mass=2.7, head_len=3.6, grip_len=1.8, hands=2, head='straight_cut', clinch=3, hand_guard=0.55, blade_guard=0.7, reach_adj=-0.05,
   wclass='bladed', hilt='simple', pommel_kg=0.548,
   geometry=dict(curvature=0.0, point_concentration=0.62, cross_section=0.82, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.0, percussion=3, pob_frac=0.22, hand='Demanding'),
 'sabre': dict(
   mass=0.9, head_len=2.6, grip_len=0.7, hands=1, head='curved_cut', clinch=3, hand_guard=0.7, blade_guard=0.45, reach_adj=-0.1,
   wclass='bladed', hilt='simple', pommel_kg=0.195,
   geometry=dict(curvature=0.55, point_concentration=0.45, cross_section=0.5, edge_keenness=0.9, strike_concentration=0.0),
   reach='long', wt='light', spd=2.0, percussion=1, pob_frac=0.18, hand='Standard'),
 'dagger': dict(
   mass=0.3, head_len=0.7, grip_len=0.4, hands=1, head='cut_thrust', clinch=10, hand_guard=0.3, blade_guard=0.4,
   wclass='bladed', hilt='none', pommel_kg=0.021,
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.97, edge_keenness=0.8, strike_concentration=0.0),
   reach='short', wt='light', spd=3.0, percussion=1, pob_frac=0.25, hand='Forgiving'),
 'paired_short': dict(
   mass=0.7, head_len=1.4, grip_len=0.5, hands=1, head='cut_thrust', clinch=5, hand_guard=0.55, blade_guard=0.5, reach_adj=1.4,
   wclass='bladed', hilt='none', pommel_kg=0.202,
   geometry=dict(curvature=0.05, point_concentration=0.65, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='short', wt='light', spd=2.5, percussion=2, pob_frac=0.22, hand='Demanding'),
 'spear': dict(
   mass=2.0, head_len=5.5, grip_len=1.2, hands=2, head='point', clinch=2, hand_guard=0.1, blade_guard=0.2,
   wclass='hafted_tip', hilt='none', pommel_kg=0.0, is_poleaxe=False,
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.82, edge_keenness=0.4, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, percussion=1, pob_frac=0.42, hand='Forgiving'),
 'staff': dict(
   mass=1.5, head_len=2.8, grip_len=2.8, hands=2, head='blunt', clinch=3, hand_guard=0.15, blade_guard=0.3, reach_adj=0.5,
   wclass='hafted_tip', hilt='none', pommel_kg=0.0, is_poleaxe=False,
   geometry=dict(curvature=0.0, point_concentration=0.05, cross_section=0.55, edge_keenness=0.0, strike_concentration=0.15),
   reach='long', wt='light', spd=0.0, percussion=4, pob_frac=0.05, hand='Forgiving'),
 'mace': dict(
   mass=1.2, head_len=1.8, grip_len=0.7, hands=1, head='blunt', clinch=4, hand_guard=0.45, blade_guard=0.3, reach_adj=-0.55,
   wclass='hafted_block', hilt='none', pommel_kg=0.0, is_poleaxe=False,
   geometry=dict(curvature=0.0, point_concentration=0.02, cross_section=0.85, edge_keenness=0.0, strike_concentration=0.45),
   reach='long', wt='heavy', spd=0.0, percussion=8, pob_frac=0.6, hand='Forgiving'),
 'poleaxe': dict(
   mass=2.5, head_len=2.2, grip_len=2.2, hands=2, head='blunt', clinch=5, hand_guard=0.3, blade_guard=0.6, reach_adj=-0.05,
   wclass='hafted_tip', hilt='none', pommel_kg=0.0, is_poleaxe=True,
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.85),
   reach='long', wt='heavy', spd=-0.5, percussion=8, pob_frac=0.45, hand='Demanding'),
 # half-sword: the SHORTENED longsword (mit dem kurzen Schwert) — one hand grips the blade. Auto-switched form.
 'longsword_halfsword': dict(
   mass=1.4, head_len=1.4, grip_len=2.6, hands=2, head='point', clinch=7, hand_guard=0.35, blade_guard=0.25,
   wclass='bladed', hilt='simple', pommel_kg=0.14,
   geometry=dict(curvature=0.0, point_concentration=0.85, cross_section=0.95, edge_keenness=0.5, strike_concentration=0.1),
   reach='short', wt='heavy', spd=-0.5, percussion=4, pob_frac=0.12, hand='Demanding', base='longsword'),
}

# Bake the geometry coefficient surface ONCE at import (zero runtime cost): geometry derives `gap` (and
# thrust/cut/perc_conc/halfsword for downstream wiring) from each weapon's nested geometry.
import geometry as _geo
for _w, _rec in WEAPONS.items():
    _b = _geo.bake(_rec['geometry'])
    _rec['gap'] = _b['gap']
    _rec['geo'] = _b   # full baked surface available to modules

# Back-compat view: GEOMETRY as a name-keyed map onto each record's nested geometry (consumers: the systems
# key-sync assert, weapon_physics docstring). The single source is WEAPONS[w]['geometry'].
GEOMETRY = {_w: _rec['geometry'] for _w, _rec in WEAPONS.items()}
