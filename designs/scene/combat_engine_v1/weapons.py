"""weapons.py — the WEAPONS DICTIONARY: each weapon ONE record, an aggregate of physical primitives.

The data half of the weapon split (the derivation half is weapon_physics.py). A weapon is a bundle of primitives;
behaviour EMERGES upward through weapon_physics, never from a per-weapon behaviour table. Each weapon is a SINGLE
record here — to add / remove / edit a weapon you touch exactly one entry (previously the data was scattered across
three parallel name-keyed dicts; consolidated 2026-06-29 per the architecture audit).

RECORD SCHEMA (per weapon):
  PHYSICAL   mass(kg) · head_len · grip_len (length-units) · hands(1/2) · head{point,cut_thrust,straight_cut,
             curved_cut,blunt} · clinch(grappling affinity) · hand_guard(0-1) · blade_guard(0-1) · reach_adj
  COMPOSITE  wclass{bladed,hafted_tip,hafted_block} · hilt{compound,simple,none} · pommel_kg · butt_kg(rear counterweight, kg)
  GEOMETRY   geometry=dict(curvature, point_concentration, cross_section, edge_keenness, strike_concentration) -> bake
  LEGACY (derived in weapon_physics; live until the Phase-3 wiring): reach{long/short} · wt{light/heavy} · spd ·
             hand{Forgiving/Standard/Demanding}.  `gap`/`geo` are DERIVED by the bake below.
"""

WEAPONS = {
 'rapier': dict(
   mass=1.3, head_len=3.2, grip_len=0.6, hands=1, head='point', clinch=2, hand_guard=0.9, blade_guard=0.45, reach_adj=0.15,
   wclass='bladed', hilt='compound', pommel_kg=0.348,
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.52, edge_keenness=0.3, strike_concentration=0.0),   # PRIMITIVE-AUDIT [G,T1 Vienna]: cross_section 0.40->0.52 — period rapiers stiff (ricasso >=8.3mm vs replica 6.2mm), but not uniform (A1027 flexible) -> moderate
   reach='long', wt='light', spd=1.5, hand='Demanding'),
 'arming': dict(
   mass=1.2, head_len=2.4, grip_len=0.8, hands=1, head='cut_thrust', clinch=4, hand_guard=0.4, blade_guard=0.55, reach_adj=-0.1,   # PRIMITIVE-AUDIT [C]: reach_adj -0.6->-0.1 — arming ~= sabre (near-equal length, identical HEAD_REACH); was dropping it below the sabre
   wclass='bladed', hilt='simple', pommel_kg=0.234,
   geometry=dict(curvature=0.05, point_concentration=0.6, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Standard'),
 'longsword': dict(
   mass=1.4, head_len=2.8, grip_len=0.85, hands=2, head='cut_thrust', clinch=6, hand_guard=0.45, blade_guard=0.85, reach_adj=0.0,   # PRIMITIVE-AUDIT [G,T1/T2]: grip_len 1.6->0.85 (real grip ~25cm, not 48cm=greatsword hilt); reach_adj zeroed once reach went geometry-derived (was -0.9 categorical-scale debt)
   wclass='bladed', hilt='simple', pommel_kg=0.30,   # PRIMITIVE-AUDIT [G,T2]: pommel 0.14->0.30 (real wheel/pear pommels 0.2-0.4kg; 0.14 < arming 0.234 was backwards for a 2H weapon, a band-aid vs the phantom grip)
   geometry=dict(curvature=0.0, point_concentration=0.8, cross_section=0.9, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.5, hand='Standard'),
 'greatsword': dict(
   mass=2.7, head_len=4.2, grip_len=1.3, hands=2, head='straight_cut', clinch=3, hand_guard=0.55, blade_guard=0.7, reach_adj=-0.05,   # PRIMITIVE-AUDIT [G,T0+T2]: head_len/grip_len 3.6/1.8 (grip 0.33)->4.2/1.3 (grip-frac ~0.24); Zweihander/montante hilt fraction 0.17-0.25
   wclass='bladed', hilt='simple', pommel_kg=0.548,
   geometry=dict(curvature=0.0, point_concentration=0.62, cross_section=0.82, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.0, hand='Demanding'),
 'sabre': dict(
   mass=0.9, head_len=2.6, grip_len=0.7, hands=1, head='curved_cut', clinch=3, hand_guard=0.52, blade_guard=0.45, reach_adj=-0.1,   # PRIMITIVE-AUDIT [G, 1796-stirrup]: hand_guard 0.7->0.52 — a single knucklebow guards the knuckles only (~greatsword 0.55), not a cup hilt
   wclass='bladed', hilt='simple', pommel_kg=0.195,
   geometry=dict(curvature=0.42, point_concentration=0.45, cross_section=0.5, edge_keenness=0.9, strike_concentration=0.0),   # PRIMITIVE-AUDIT [G, LOW-CONF reconstruction]: curvature 0.55->0.42 (1796 < shamshir); inert at the halfsword gate, flag [NO SPECIMEN DATA]
   reach='long', wt='light', spd=2.0, hand='Standard'),
 'dagger': dict(
   mass=0.3, head_len=0.7, grip_len=0.4, hands=1, head='cut_thrust', clinch=10, hand_guard=0.3, blade_guard=0.4,
   wclass='bladed', hilt='none', pommel_kg=0.021,
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.84, edge_keenness=0.8, strike_concentration=0.0),   # PRIMITIVE-AUDIT [G]: cross_section 0.97->0.84 — 0.97 = edgeless-rondel rigidity, inconsistent with edge_keenness 0.8 (an edged war-dagger out-rigiditied the longsword)
   reach='short', wt='light', spd=3.0, hand='Forgiving'),
 'paired_short': dict(
   mass=0.7, head_len=1.4, grip_len=0.5, hands=1, head='cut_thrust', clinch=5, hand_guard=0.55, blade_guard=0.5, reach_adj=-0.5,   # PRIMITIVE-AUDIT [G]: reach_adj +1.4->-0.5 — fabricated reach (gave a 0.57m weapon arming-sword reach); dual-wield benefit belongs in tempo, not reach
   wclass='bladed', hilt='simple', pommel_kg=0.202,   # PRIMITIVE-AUDIT [G]: hilt none->simple — consistency with the attested D-guard (hand_guard 0.55); GUARD mass sits at the hand
   geometry=dict(curvature=0.05, point_concentration=0.65, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='short', wt='light', spd=2.5, hand='Demanding'),
 'spear': dict(
   mass=2.0, head_len=5.5, grip_len=1.2, hands=2, head='point', clinch=2, hand_guard=0.1, blade_guard=0.2,
   wclass='hafted_tip', hilt='none', pommel_kg=0.0, haft_d=0.035, butt_kg=0.25,   # SPEAR-BALANCE [Jordan A, 2026-06-30]: a war spear is butt-weighted (sauroter 0.25kg) on a ~35mm ash shaft -> a real 0.40kg head (40mm gave an impossible 0.23kg head); balances at the forward grip, retracts free when gripped at balance (grip-position model)
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.82, edge_keenness=0.4, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, hand='Forgiving'),
 'staff': dict(
   mass=1.5, head_len=2.8, grip_len=2.8, hands=2, head='blunt', clinch=3, hand_guard=0.15, blade_guard=0.3, reach_adj=0.0,   # PRIMITIVE-AUDIT [C]: reach_adj 0.5->0.0 — the blunt head-reach now lives in HEAD_REACH['blunt']=0.5 (shared), retiring this fudge
   wclass='hafted_tip', hilt='none', pommel_kg=0.0,
   geometry=dict(curvature=0.0, point_concentration=0.05, cross_section=0.55, edge_keenness=0.0, strike_concentration=0.15),
   reach='long', wt='light', spd=0.0, hand='Forgiving'),
 'mace': dict(
   mass=1.2, head_len=1.8, grip_len=0.7, hands=1, head='blunt', clinch=4, hand_guard=0.18, blade_guard=0.3, reach_adj=0.0,   # PRIMITIVE-AUDIT [G]: hand_guard 0.45->0.18 (a bare haft is below a cross-hilt); reach_adj cleared (was masking the 'long' tag)
   wclass='hafted_block', hilt='none', pommel_kg=0.0,
   geometry=dict(curvature=0.0, point_concentration=0.02, cross_section=0.85, edge_keenness=0.0, strike_concentration=0.45),
   reach='short', wt='heavy', spd=0.0, hand='Forgiving'),   # PRIMITIVE-AUDIT [G,T1 Wallace A978 51.8cm]: reach 'long'->'short' — a ~0.55m sidearm, not a reach weapon
 'poleaxe': dict(
   mass=2.5, head_len=3.0, grip_len=3.0, hands=2, head='blunt', clinch=5, hand_guard=0.3, blade_guard=0.6, reach_adj=-0.05,   # PRIMITIVE-AUDIT [G,T0/T2]: length 1.32->1.8m (keep the 50/50 centre-grip split); was shorter than every specimen (Art Institute 177.8cm, RA VII.1510 236.7cm)
   wclass='hafted_tip', hilt='none', pommel_kg=0.0, butt_kg=0.22,   # rear queue/spike counterweight (kg) — derive() reads it; the old is_poleaxe flag is gone
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.85),
   reach='long', wt='heavy', spd=-0.5, hand='Demanding'),
 # half-sword: the SHORTENED longsword (mit dem kurzen Schwert) — one hand grips the blade. Auto-switched form.
 'longsword_halfsword': dict(
   mass=1.4, head_len=1.4, grip_len=2.6, hands=2, head='point', clinch=7, hand_guard=0.35, blade_guard=0.25,
   wclass='bladed', hilt='simple', pommel_kg=0.14, gripped=True,   # HAND-ON-BLADE form: the held span is STEEL, not a wood grip (weapon_physics.derive reads `gripped`)
   geometry=dict(curvature=0.0, point_concentration=0.85, cross_section=0.95, edge_keenness=0.5, strike_concentration=0.1),
   reach='short', wt='heavy', spd=-0.5, hand='Demanding', base='longsword'),
}

# Bake the geometry coefficient surface ONCE at import (zero runtime cost): geometry derives `gap` (and
# thrust/cut/perc_conc/halfsword for downstream wiring) from each weapon's nested geometry.
import geometry as _geo
for _w, _rec in WEAPONS.items():
    _b = _geo.bake(_rec['geometry'])
    _rec['gap'] = _b['gap']
    _rec['geo'] = _b   # full baked surface available to modules

# Bake the derive() mass-family statistics ONCE at import (re-architecture 2026-07-02 Phase A: honors the
# bake-once contract — derive() was recomputed many times per beat via agility/at_grip/defense_affinities/
# percussion_authority; the record's located parts are static, so the result is too). weapon_physics.derive
# returns the cached '_derived' when present; a record mutated after bake is OUT OF CONTRACT, exactly as it
# already is for the baked geo/gap above. Cycle-free: weapon_physics imports only math at module scope.
import weapon_physics as _wp
for _w, _rec in WEAPONS.items():
    _rec['_derived'] = _wp.derive(_rec)

# Back-compat view: GEOMETRY as a name-keyed map onto each record's nested geometry (consumers: the systems
# key-sync assert, weapon_physics docstring). The single source is WEAPONS[w]['geometry'].
GEOMETRY = {_w: _rec['geometry'] for _w, _rec in WEAPONS.items()}

# HALF-SWORD FORM mapping (weapon data): which base weapon switches to which shortened gripped-blade form. The
# inverse is DERIVED (not a second hand-maintained dict). Read by systems.halfsword_target + capabilities.
HALFSWORD_FORM = {'longsword': 'longsword_halfsword'}
HALFSWORD_BASE = {_form: _base for _base, _form in HALFSWORD_FORM.items()}
