"""weapons.py — the WEAPONS DICTIONARY: each weapon ONE record, an aggregate of physical primitives.

The data half of the weapon split (the derivation half is weapon_physics.py). A weapon is a bundle of primitives;
behaviour EMERGES upward through weapon_physics, never from a per-weapon behaviour table. Each weapon is a SINGLE
record here — to add / remove / edit a weapon you touch exactly one entry. 53-weapon roster, morphology-rearch
Phase B (2026-07-02): every weapon's MASS DISTRIBUTION is now a positional sum over LOCATED, MATERIALED PARTS
(elements/guards/haft/pommel/butt — specimen-grounded, designs/audit/2026-07-02-morphology-rearch-phase0/), not a
whole-weapon lump at a wclass-centroid. weapon_physics.derive() sums them; see its STAGE-1 docstring.

RECORD SCHEMA (per weapon):
  PHYSICAL   mass(kg, = Σ part masses) · head_len · grip_len (length-units, UNIT_M=0.30m each) · hands(1/2) ·
             head{point,cut_thrust,straight_cut,curved_cut,blunt} (native/default combat mode — afforded_heads
             derives the full afforded SET) · clinch(grappling affinity) · hand_guard(0-1) · blade_guard(0-1) ·
             reach_adj
  COMPOSITE  wclass{bladed,hafted_tip,hafted_block} · hilt{compound,simple,none}
  PARTS      elements=[{x_m, mass_kg, extent_m, [edge_undulation]}] (the located striking element(s) — one for a
             plain blade/point/haft-tip, several for a composite head like the bec de corbin's hammer+beak+spike;
             comment names the physical part) · guards=[{x_m, mass_kg, extent_m, [dual_role_element]}] (located
             catching/hand-protecting hardware; a guard that is ALSO a striking element, e.g. the hook_sword's
             crescent, sets dual_role_element=True and carries mass_kg=0 here — its mass is counted once, via
             elements) · haft={x_m, mass_kg, extent_m} (grip for a bladed weapon; the full shaft for a hafted one)
             · pommel/butt={x_m, mass_kg} (omitted when absent). All positions in METRES, x=0 at the working hand,
             +toward the tip, −toward the butt (weapon_physics.derive()'s axis).
  GEOMETRY   geometry=dict(curvature, point_concentration, cross_section, edge_keenness, strike_concentration) -> bake
             (whole-weapon combat-shape primitives — the default every weapon reads unless it has mode_elements)
  MODES      mode_elements=[{head, geometry}] (Phase B2, 8 weapons only: poleaxe, bec_de_corbin, lucerne_hammer,
             ji, goedendag, guisarme, kama_yari, voulge) — the striking elements that afford GENUINELY DIFFERENT
             fight-modes (swing the hammer face vs thrust the spike), each with its own head token + per-element
             geometry, grounded against Phase 0 specimen research and independently adversarially verified. This
             is a PARALLEL view onto the mass-model `elements` (a composite can have multiple mass elements
             without multiple modes, e.g. flamberge's forte/tip/ricasso — one continuous edge, no mode_elements).
  LEGACY (derived in weapon_physics; live until the wt/spd/hand de-leak lands): reach{long/short} · wt{light/heavy} ·
             spd · hand{Forgiving/Standard/Demanding}.  `gap`/`geo` are DERIVED by the bake below.
"""

WEAPONS = {
 'rapier': dict(
   mass=1.368, head_len=3.2, grip_len=0.6, hands=1, head='point', clinch=2, hand_guard=0.9, blade_guard=0.45, reach_adj=0.15,
   wclass='bladed', hilt='compound',
   elements=[
     dict(x_m=0.48, mass_kg=0.62, extent_m=0.96),  # blade
    ],
   guards=[
     dict(x_m=0.02, mass_kg=0.3, extent_m=0.1),  # swept hilt (compound guard: knucklebow + multiple sweeping bars + ring/side-rings)
    ],
   haft=dict(x_m=-0.09, mass_kg=0.1, extent_m=0.18),
   pommel=dict(x_m=-0.18, mass_kg=0.348),
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.52, edge_keenness=0.3, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Demanding'),
 'arming': dict(
   mass=1.2, head_len=2.4, grip_len=0.8, hands=1, head='cut_thrust', clinch=4, hand_guard=0.4, blade_guard=0.55, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.36, mass_kg=0.78, extent_m=0.72),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.09, extent_m=0.16),  # straight cross/quillon guard
    ],
   haft=dict(x_m=-0.12, mass_kg=0.096, extent_m=0.24),
   pommel=dict(x_m=-0.24, mass_kg=0.234),
   geometry=dict(curvature=0.05, point_concentration=0.6, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Standard'),
 'longsword': dict(
   mass=1.408, head_len=2.8, grip_len=0.85, hands=2, head='cut_thrust', clinch=6, hand_guard=0.45, blade_guard=0.85,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.42, mass_kg=0.87, extent_m=0.84),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.12, extent_m=0.2),  # straight cross guard (occasionally slightly curved quillons)
    ],
   haft=dict(x_m=-0.1275, mass_kg=0.118, extent_m=0.255),
   pommel=dict(x_m=-0.255, mass_kg=0.3),
   geometry=dict(curvature=0.0, point_concentration=0.8, cross_section=0.9, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.5, hand='Standard'),
 'greatsword': dict(
   mass=2.751, head_len=4.2, grip_len=1.3, hands=2, head='straight_cut', clinch=3, hand_guard=0.55, blade_guard=0.7, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.63, mass_kg=1.75, extent_m=1.26),  # blade (with ricasso, often flanked by parrying lugs)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.19, extent_m=0.26),  # cross guard with recurved/S-shaped quillons
    ],
   haft=dict(x_m=-0.195, mass_kg=0.263, extent_m=0.39),
   pommel=dict(x_m=-0.39, mass_kg=0.548),
   geometry=dict(curvature=0.0, point_concentration=0.62, cross_section=0.82, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0.0, hand='Demanding'),
 'sabre': dict(
   mass=0.9, head_len=2.6, grip_len=0.7, hands=1, head='curved_cut', clinch=3, hand_guard=0.52, blade_guard=0.45, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.39, mass_kg=0.53, extent_m=0.78),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.095, extent_m=0.14),  # stirrup hilt: single iron knucklebow + quillon
    ],
   haft=dict(x_m=-0.105, mass_kg=0.08, extent_m=0.21),
   pommel=dict(x_m=-0.21, mass_kg=0.195),
   geometry=dict(curvature=0.42, point_concentration=0.45, cross_section=0.5, edge_keenness=0.9, strike_concentration=0.0),
   reach='long', wt='light', spd=2.0, hand='Standard'),
 'dagger': dict(
   mass=0.274, head_len=0.7, grip_len=0.4, hands=1, head='cut_thrust', clinch=10, hand_guard=0.3, blade_guard=0.4,
   wclass='bladed', hilt='none',
   elements=[
     dict(x_m=0.105, mass_kg=0.16, extent_m=0.21),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.025, extent_m=0.05),  # small cross guard / disc guard
    ],
   haft=dict(x_m=-0.06, mass_kg=0.068, extent_m=0.12),
   pommel=dict(x_m=-0.12, mass_kg=0.021),
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.84, edge_keenness=0.8, strike_concentration=0.0),
   reach='short', wt='light', spd=3.0, hand='Forgiving'),
 'paired_short': dict(
   mass=0.698, head_len=1.4, grip_len=0.5, hands=1, head='cut_thrust', clinch=5, hand_guard=0.55, blade_guard=0.5, reach_adj=-0.5,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.21, mass_kg=0.36, extent_m=0.42),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.075, extent_m=0.11),  # D-guard / simple knuckle-guard hilt
    ],
   haft=dict(x_m=-0.075, mass_kg=0.061, extent_m=0.15),
   pommel=dict(x_m=-0.15, mass_kg=0.202),
   geometry=dict(curvature=0.05, point_concentration=0.65, cross_section=0.72, edge_keenness=0.8, strike_concentration=0.0),
   reach='short', wt='light', spd=2.5, hand='Demanding'),
 'spear': dict(
   mass=2.004, head_len=5.5, grip_len=1.2, hands=2, head='point', clinch=2, hand_guard=0.1, blade_guard=0.2,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.51, mass_kg=0.4, extent_m=0.28),  # spearhead (leaf-shaped socketed point)
    ],
   haft=dict(x_m=0.645, mass_kg=1.354, extent_m=2.01),
   butt=dict(x_m=-0.36, mass_kg=0.25),
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.82, edge_keenness=0.4, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, hand='Forgiving'),
 'staff': dict(
   mass=1.478, head_len=2.8, grip_len=2.8, hands=2, head='blunt', clinch=3, hand_guard=0.15, blade_guard=0.3,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.84, mass_kg=0.0, extent_m=0.0),  # working tip (blunt, no metal fitting — bare wood end)
    ],
   haft=dict(x_m=0.0, mass_kg=1.478, extent_m=1.68),
   geometry=dict(curvature=0.0, point_concentration=0.05, cross_section=0.55, edge_keenness=0.0, strike_concentration=0.15),
   reach='long', wt='light', spd=0.0, hand='Forgiving'),
 'mace': dict(
   mass=1.2, head_len=1.8, grip_len=0.7, hands=1, head='blunt', clinch=4, hand_guard=0.18, blade_guard=0.3,
   wclass='hafted_block', hilt='none',
   elements=[
     dict(x_m=0.486, mass_kg=0.95, extent_m=0.14),  # flanged head (6-8 flanges, solid steel/iron block)
    ],
   haft=dict(x_m=0.165, mass_kg=0.25, extent_m=0.75),
   geometry=dict(curvature=0.0, point_concentration=0.02, cross_section=0.85, edge_keenness=0.0, strike_concentration=0.45),
   reach='short', wt='heavy', spd=0.0, hand='Forgiving'),
 'poleaxe': dict(
   mass=2.583, head_len=3.0, grip_len=3.0, hands=2, head='blunt', clinch=5, hand_guard=0.3, blade_guard=0.6, reach_adj=-0.05,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.85, mass_kg=0.55, extent_m=0.06),  # hammer face (front, blunt square/pyramidal-studded striking face)
     dict(x_m=0.85, mass_kg=0.35, extent_m=0.08),  # beak/fluke (rear-facing curved spike/hook, opposite the hammer)
     dict(x_m=1.02, mass_kg=0.28, extent_m=0.2),  # top spike (langet-mounted, forward-thrusting point above the hammer/beak)
    ],
   guards=[
     dict(x_m=0.6, mass_kg=0.12, extent_m=0.45),  # steel langets (metal straps reinforcing the haft below the head, incidental hand protection)
     dict(x_m=0.65, mass_kg=0.05, extent_m=0.1),  # small hand-guard disc/rondel below the head
    ],
   haft=dict(x_m=0.0, mass_kg=1.013, extent_m=1.8),
   butt=dict(x_m=-0.9, mass_kg=0.22),
   geometry=dict(curvature=0.0, point_concentration=0.78, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.85),
   mode_elements=[
     dict(head='blunt', geometry=dict(curvature=0.00, point_concentration=0.02, cross_section=0.85, edge_keenness=0.00, strike_concentration=0.75)),  # hammer face (front, blunt square/pyramidal-studded striking face)
     dict(head='point', geometry=dict(curvature=0.25, point_concentration=0.60, cross_section=0.80, edge_keenness=0.00, strike_concentration=0.00)),  # beak/fluke (rear-facing curved spike/hook, opposite the hammer)
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.85, cross_section=0.90, edge_keenness=0.00, strike_concentration=0.00)),  # top spike (langet-mounted, forward-thrusting point above the hammer/beak)
    ],
   reach='long', wt='heavy', spd=-0.5, hand='Demanding'),
 # half-sword: the SHORTENED longsword (mit dem kurzen Schwert) — one hand grips the blade. Auto-switched form.
 'longsword_halfsword': dict(
   mass=1.408, head_len=1.4, grip_len=2.6, hands=2, head='point', clinch=7, hand_guard=0.35, blade_guard=0.25,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.21, mass_kg=0.435, extent_m=0.42),  # blade tip segment (forward of the new working-hand point — the working point in half-sword grip)
    ],
   guards=[
     dict(x_m=-0.42, mass_kg=0.12, extent_m=0.2),  # cross guard (the SAME cross as the longsword record — now trailing BEHIND the working hand, inert as a guard in this grip, sitting within the "grip_len" span)
    ],
   haft=dict(x_m=-0.39, mass_kg=0.553, extent_m=0.78),
   pommel=dict(x_m=-0.675, mass_kg=0.3),
   geometry=dict(curvature=0.0, point_concentration=0.85, cross_section=0.95, edge_keenness=0.5, strike_concentration=0.1),
   reach='short', wt='heavy', spd=-0.5, hand='Demanding', base='longsword'),
 'yari': dict(
   mass=1.23, head_len=6.2067, grip_len=0.9603, hands=2, head='point', clinch=3, hand_guard=0.12, blade_guard=0.12,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.712, mass_kg=0.28, extent_m=0.3),  # main_point
    ],
   guards=[
     dict(x_m=1.412, mass_kg=0.0232, extent_m=0.02),  # habaki_collar
    ],
   haft=dict(x_m=0.787, mass_kg=0.9268, extent_m=2.1501),
   geometry=dict(curvature=0.0, point_concentration=0.88, cross_section=0.8, edge_keenness=0.32, strike_concentration=0.0),
   reach='long', wt='light', spd=0, hand='Demanding'),
 'kama_yari': dict(
   mass=1.4397, head_len=5.81, grip_len=0.857, hands=2, head='cut_thrust', clinch=6, hand_guard=0.12, blade_guard=0.75, reach_adj=-0.1,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.593, mass_kg=0.28, extent_m=0.3),  # main_point
     dict(x_m=1.36, mass_kg=0.085, extent_m=0.13),  # cross_blade_left
     dict(x_m=1.36, mass_kg=0.085, extent_m=0.13),  # cross_blade_right
    ],
   haft=dict(x_m=0.743, mass_kg=0.9897, extent_m=2.0001),
   geometry=dict(curvature=0.1, point_concentration=0.8, cross_section=0.78, edge_keenness=0.42, strike_concentration=0.0),
   mode_elements=[
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.85, cross_section=0.80, edge_keenness=0.32, strike_concentration=0.00)),  # main_point
     dict(head='curved_cut', geometry=dict(curvature=0.55, point_concentration=0.10, cross_section=0.45, edge_keenness=0.65, strike_concentration=0.00)),  # cross_blade_left
     dict(head='curved_cut', geometry=dict(curvature=0.55, point_concentration=0.10, cross_section=0.45, edge_keenness=0.65, strike_concentration=0.00)),  # cross_blade_right
    ],
   reach='long', wt='light', spd=0, hand='Demanding'),
 'dangpa': dict(
   mass=1.8392, head_len=6.4933, grip_len=1.1397, hands=2, head='point', clinch=2, hand_guard=0.05, blade_guard=0.55,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.823, mass_kg=0.32, extent_m=0.25),  # center_prong
     dict(x_m=1.71, mass_kg=0.115, extent_m=0.16),  # flank_tine_left
     dict(x_m=1.71, mass_kg=0.115, extent_m=0.16),  # flank_tine_right
    ],
   haft=dict(x_m=0.803, mass_kg=1.2892, extent_m=2.2899),
   geometry=dict(curvature=0.0, point_concentration=0.75, cross_section=0.78, edge_keenness=0.3, strike_concentration=0.0),
   reach='long', wt='light', spd=0, hand='Standard'),
 'bear_spear': dict(
   mass=2.3502, head_len=6.4167, grip_len=0.4163, hands=2, head='point', clinch=4, hand_guard=0.12, blade_guard=0.45, reach_adj=-0.1,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.75, mass_kg=0.46, extent_m=0.35),  # main_point
    ],
   guards=[
     dict(x_m=1.55, mass_kg=0.087, extent_m=0.22),  # crossbar_lug
    ],
   haft=dict(x_m=0.9001, mass_kg=1.8032, extent_m=2.0499),
   geometry=dict(curvature=0.0, point_concentration=0.55, cross_section=0.75, edge_keenness=0.5, strike_concentration=0.0),
   reach='long', wt='light', spd=0, hand='Standard'),
 'ranseur': dict(
   mass=2.1503, head_len=6.2733, grip_len=0.7267, hands=2, head='cut_thrust', clinch=6, hand_guard=0.12, blade_guard=0.65,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.672, mass_kg=0.48, extent_m=0.42),  # main_point
    ],
   guards=[
     dict(x_m=1.3, mass_kg=0.087, extent_m=0.16),  # wing_lug_left
     dict(x_m=1.3, mass_kg=0.087, extent_m=0.16),  # wing_lug_right
    ],
   haft=dict(x_m=0.832, mass_kg=1.4963, extent_m=2.1),
   geometry=dict(curvature=0.0, point_concentration=0.9, cross_section=0.85, edge_keenness=0.3, strike_concentration=0.15),
   reach='long', wt='light', spd=0, hand='Standard'),
 'spetum': dict(
   mass=1.8, head_len=5.8667, grip_len=1.4633, hands=2, head='cut_thrust', clinch=2, hand_guard=0.2, blade_guard=0.4,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.55, mass_kg=0.32, extent_m=0.42),  # central spear point (langet-socketed triangular blade)
     dict(x_m=1.02, mass_kg=0.03, extent_m=0.16),  # left side prong/wing (forward-curving flange)
     dict(x_m=1.02, mass_kg=0.03, extent_m=0.16),  # right side prong/wing (forward-curving flange)
    ],
   haft=dict(x_m=0.6605, mass_kg=1.42, extent_m=2.199),
   geometry=dict(curvature=0.0, point_concentration=0.72, cross_section=0.72, edge_keenness=0.55, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, hand='Standard'),
 'partisan': dict(
   mass=2.57, head_len=5.8817, grip_len=1.7883, hands=2, head='cut_thrust', clinch=3, hand_guard=0.15, blade_guard=0.6,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.45, mass_kg=0.82, extent_m=0.629),  # central ox-tongue blade (broad triangular/leaf main blade)
     dict(x_m=0.9, mass_kg=0.1, extent_m=0.2),  # left wing-lug (basal flange)
     dict(x_m=0.9, mass_kg=0.1, extent_m=0.2),  # right wing-lug (basal flange)
    ],
   haft=dict(x_m=0.614, mass_kg=1.55, extent_m=2.301),
   geometry=dict(curvature=0.0, point_concentration=0.5, cross_section=0.68, edge_keenness=0.7, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0.0, hand='Standard'),
 'naginata': dict(
   mass=1.35, head_len=3.6, grip_len=3.4, hands=2, head='cut_thrust', clinch=3, hand_guard=0.15, blade_guard=0.15,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.87, mass_kg=0.48, extent_m=0.42),  # nagasa (forged sword blade, saki-zori curved single edge)
    ],
   haft=dict(x_m=0.03, mass_kg=0.82, extent_m=2.1),
   butt=dict(x_m=-1.02, mass_kg=0.05),
   geometry=dict(curvature=0.5, point_concentration=0.45, cross_section=0.58, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, hand='Demanding'),
 'glaive': dict(
   mass=1.84, head_len=3.7333, grip_len=3.2667, hands=2, head='curved_cut', clinch=2, hand_guard=0.2, blade_guard=0.35,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.87, mass_kg=0.82, extent_m=0.5),  # leaf-shaped single-edge blade (socketed)
    ],
   haft=dict(x_m=0.07, mass_kg=1.02, extent_m=2.1),
   geometry=dict(curvature=0.22, point_concentration=0.4, cross_section=0.65, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='light', spd=0.0, hand='Standard'),
 'guandao': dict(
   mass=3.8, head_len=6.75, grip_len=1.25, hands=2, head='curved_cut', clinch=2, hand_guard=0.15, blade_guard=0.35,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.53, mass_kg=1.75, extent_m=0.99),  # main dao blade (deep reclining-moon crescent, single edge)
     dict(x_m=0.55, mass_kg=0.25, extent_m=0.12),  # rear spike/hook notch (spine feature at the blade's socket end)
    ],
   guards=[
     dict(x_m=0.05, mass_kg=0.05, extent_m=0.03),  # socket collar/washer
    ],
   haft=dict(x_m=0.825, mass_kg=1.55, extent_m=2.4),
   butt=dict(x_m=-0.375, mass_kg=0.2),
   geometry=dict(curvature=0.6, point_concentration=0.3, cross_section=0.78, edge_keenness=0.85, strike_concentration=0.15),
   reach='long', wt='heavy', spd=-0.5, hand='Demanding'),
 'podao': dict(
   mass=2.48, head_len=5.3233, grip_len=0.7433, hands=2, head='curved_cut', clinch=1, hand_guard=0.1, blade_guard=0.1,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.85, mass_kg=1.45, extent_m=1.494),  # dao_blade
    ],
   haft=dict(x_m=0.687, mass_kg=1.03, extent_m=1.82),
   geometry=dict(curvature=0.3, point_concentration=0.35, cross_section=0.6, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0, hand='Forgiving'),
 'fauchard': dict(
   mass=2.03, head_len=6.1717, grip_len=1.1617, hands=2, head='curved_cut', clinch=2, hand_guard=0.05, blade_guard=0.4,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.95, mass_kg=0.65, extent_m=1.803),  # fauchard_blade
     dict(x_m=0.55, mass_kg=0.08, extent_m=0.1),  # back_hook_spike
    ],
   haft=dict(x_m=0.7515, mass_kg=1.3, extent_m=2.2),
   geometry=dict(curvature=0.55, point_concentration=0.25, cross_section=0.55, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0, hand='Standard'),
 'bardiche': dict(
   mass=2.61, head_len=5.2933, grip_len=0.7067, hands=2, head='straight_cut', clinch=2, hand_guard=0.1, blade_guard=0.05, reach_adj=-0.1,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.85, mass_kg=1.75, extent_m=1.476),  # crescent_blade
    ],
   guards=[
     dict(x_m=0.05, mass_kg=0.06, extent_m=0.12),  # lower_socket_langet
    ],
   haft=dict(x_m=0.688, mass_kg=0.8, extent_m=1.8),
   geometry=dict(curvature=0.2, point_concentration=0.18, cross_section=0.55, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0, hand='Standard'),
 'sparr_axe': dict(
   mass=2.25, head_len=4.55, grip_len=0.45, hands=2, head='straight_cut', clinch=2, hand_guard=0.1, blade_guard=0.08, reach_adj=-0.15,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.75, mass_kg=1.15, extent_m=1.23),  # broad_axe_bit
    ],
   haft=dict(x_m=0.615, mass_kg=1.1, extent_m=1.5),
   geometry=dict(curvature=0.15, point_concentration=0.1, cross_section=0.6, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0, hand='Forgiving'),
 'voulge': dict(
   mass=2.18, head_len=6.1667, grip_len=0.5, hands=2, head='cut_thrust', clinch=4, hand_guard=0.2, blade_guard=0.35,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.1, mass_kg=0.85, extent_m=1.5),  # cleaver_blade
     dict(x_m=1.55, mass_kg=0.1, extent_m=0.14),  # thrusting_heel_spike
     dict(x_m=0.65, mass_kg=0.08, extent_m=0.08),  # rear_fluke
    ],
   haft=dict(x_m=0.85, mass_kg=1.15, extent_m=2.0),
   geometry=dict(curvature=0.1, point_concentration=0.55, cross_section=0.65, edge_keenness=0.8, strike_concentration=0.1),
   mode_elements=[
     dict(head='cut_thrust', geometry=dict(curvature=0.15, point_concentration=0.30, cross_section=0.65, edge_keenness=0.80, strike_concentration=0.00)),  # cleaver_blade
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.68, cross_section=0.78, edge_keenness=0.15, strike_concentration=0.00)),  # thrusting_heel_spike
    ],
   reach='long', wt='heavy', spd=0, hand='Standard'),
 'guisarme': dict(
   mass=1.8663, head_len=3.4557, grip_len=3.5443, hands=2, head='cut_thrust', clinch=2, hand_guard=0.15, blade_guard=0.35,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.6958, mass_kg=0.19, extent_m=0.32),  # hooked cutting blade
     dict(x_m=0.9867, mass_kg=0.06, extent_m=0.1),  # reverse thrusting spike
    ],
   haft=dict(x_m=-0.0133, mass_kg=1.4963, extent_m=2.1),
   butt=dict(x_m=-1.0633, mass_kg=0.12),
   geometry=dict(curvature=0.2, point_concentration=0.55, cross_section=0.68, edge_keenness=0.55, strike_concentration=0.0),
   mode_elements=[
     dict(head='cut_thrust', geometry=dict(curvature=0.35, point_concentration=0.30, cross_section=0.55, edge_keenness=0.60, strike_concentration=0.00)),  # hooked cutting blade
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.80, cross_section=0.85, edge_keenness=0.00, strike_concentration=0.00)),  # reverse thrusting spike
    ],
   reach='long', wt='light', spd=0.0, hand='Standard'),
 'ji': dict(
   mass=2.1, head_len=3.8483, grip_len=4.1517, hands=2, head='cut_thrust', clinch=3, hand_guard=0.25, blade_guard=0.75,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=1.0345, mass_kg=0.15, extent_m=0.24),  # straight spearhead (thrusting point)
     dict(x_m=0.7586, mass_kg=0.14, extent_m=0.22),  # perpendicular crescent (yueyadao) blade
    ],
   haft=dict(x_m=-0.0455, mass_kg=1.71, extent_m=2.4),
   butt=dict(x_m=-1.2455, mass_kg=0.1),
   geometry=dict(curvature=0.2, point_concentration=0.62, cross_section=0.72, edge_keenness=0.55, strike_concentration=0.0),
   mode_elements=[
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.75, cross_section=0.80, edge_keenness=0.40, strike_concentration=0.00)),  # straight spearhead (thrusting point)
     dict(head='curved_cut', geometry=dict(curvature=0.45, point_concentration=0.05, cross_section=0.62, edge_keenness=0.75, strike_concentration=0.05)),  # perpendicular crescent (yueyadao) blade
    ],
   reach='long', wt='light', spd=0.0, hand='Standard'),
 'bec_de_corbin': dict(
   mass=2.4534, head_len=2.8723, grip_len=3.1277, hands=2, head='blunt', clinch=8, hand_guard=0.3, blade_guard=0.15, reach_adj=-0.05,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.5478, mass_kg=0.22, extent_m=0.06),  # hammer face
     dict(x_m=0.587, mass_kg=0.26, extent_m=0.09),  # curved beak (bec de corbin)
     dict(x_m=0.8217, mass_kg=0.1, extent_m=0.08),  # top spike
    ],
   guards=[
     dict(x_m=0.0978, mass_kg=0.05, extent_m=0.09),  # rondel disc
     dict(x_m=0.3326, mass_kg=0.04, extent_m=0.25),  # langets
    ],
   haft=dict(x_m=-0.0383, mass_kg=1.5834, extent_m=1.8),
   butt=dict(x_m=-0.9383, mass_kg=0.2),
   geometry=dict(curvature=0.0, point_concentration=0.86, cross_section=0.9, edge_keenness=0.25, strike_concentration=0.8),
   mode_elements=[
     dict(head='blunt', geometry=dict(curvature=0.00, point_concentration=0.02, cross_section=0.88, edge_keenness=0.00, strike_concentration=0.50)),  # hammer face
     dict(head='point', geometry=dict(curvature=0.55, point_concentration=0.62, cross_section=0.75, edge_keenness=0.00, strike_concentration=0.00)),  # curved beak (bec de corbin)
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.88, cross_section=0.85, edge_keenness=0.00, strike_concentration=0.00)),  # top spike
    ],
   reach='long', wt='heavy', spd=-0.5, hand='Standard'),
 'lucerne_hammer': dict(
   mass=2.4834, head_len=2.8717, grip_len=3.1283, hands=2, head='blunt', clinch=7, hand_guard=0.05, blade_guard=0.15, reach_adj=-0.05,
   wclass='hafted_tip', hilt='none',
   elements=[
     dict(x_m=0.4825, mass_kg=0.2, extent_m=0.06),  # hammer face (4-tine fluke, striking side)
     dict(x_m=0.5938, mass_kg=0.35, extent_m=0.11),  # 3-4 tine fluke (rear beak)
     dict(x_m=0.8165, mass_kg=0.15, extent_m=0.09),  # top spike
    ],
   haft=dict(x_m=-0.0385, mass_kg=1.5834, extent_m=1.8),
   butt=dict(x_m=-0.9385, mass_kg=0.2),
   geometry=dict(curvature=0.0, point_concentration=0.8, cross_section=0.9, edge_keenness=0.2, strike_concentration=0.62),
   mode_elements=[
     dict(head='blunt', geometry=dict(curvature=0.00, point_concentration=0.02, cross_section=0.90, edge_keenness=0.00, strike_concentration=0.45)),  # hammer face (4-tine fluke, striking side)
     dict(head='blunt', geometry=dict(curvature=0.00, point_concentration=0.08, cross_section=0.90, edge_keenness=0.00, strike_concentration=0.62)),  # 3-4 tine fluke (rear beak)
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.80, cross_section=0.88, edge_keenness=0.00, strike_concentration=0.00)),  # top spike
    ],
   reach='long', wt='heavy', spd=-0.5, hand='Demanding'),
 'goedendag': dict(
   mass=1.796, head_len=3.3333, grip_len=0.6667, hands=2, head='blunt', clinch=4, hand_guard=0.1, blade_guard=0.15,
   wclass='hafted_block', hilt='none',
   elements=[
     dict(x_m=0.55, mass_kg=0.0, extent_m=0.9),  # tapering club body (extended wooden mass element)
     dict(x_m=0.85, mass_kg=0.46, extent_m=0.1),  # iron spike (tanged, thrusting point)
    ],
   haft=dict(x_m=0.4, mass_kg=1.336, extent_m=1.2),
   geometry=dict(curvature=0.0, point_concentration=0.25, cross_section=0.55, edge_keenness=0.1, strike_concentration=0.3),
   mode_elements=[
     dict(head='blunt', geometry=dict(curvature=0.00, point_concentration=0.03, cross_section=0.60, edge_keenness=0.00, strike_concentration=0.35)),  # tapering club body (extended wooden mass element)
     dict(head='point', geometry=dict(curvature=0.00, point_concentration=0.75, cross_section=0.88, edge_keenness=0.00, strike_concentration=0.00)),  # iron spike (tanged, thrusting point)
    ],
   reach='short', wt='heavy', spd=0.0, hand='Forgiving'),
 'katana': dict(
   mass=1.025, head_len=2.1467, grip_len=1.0863, hands=2, head='curved_cut', clinch=5, hand_guard=0.35, blade_guard=0.28,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.294, mass_kg=0.76, extent_m=0.7),  # blade (nagasa)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.1, extent_m=0.078),  # tsuba
    ],
   haft=dict(x_m=-0.163, mass_kg=0.14, extent_m=0.3259),
   pommel=dict(x_m=-0.3259, mass_kg=0.025),
   geometry=dict(curvature=0.2, point_concentration=0.6, cross_section=0.62, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Demanding'),
 'tachi': dict(
   mass=1.105, head_len=2.3933, grip_len=1.1397, hands=2, head='curved_cut', clinch=5, hand_guard=0.3, blade_guard=0.3, reach_adj=0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.328, mass_kg=0.82, extent_m=0.78),  # blade (nagasa)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.1, extent_m=0.078),  # tsuba
    ],
   haft=dict(x_m=-0.1709, mass_kg=0.16, extent_m=0.3419),
   pommel=dict(x_m=-0.3419, mass_kg=0.025),
   geometry=dict(curvature=0.35, point_concentration=0.5, cross_section=0.55, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='light', spd=1.0, hand='Demanding'),
 'odachi': dict(
   mass=2.075, head_len=3.72, grip_len=1.48, hands=2, head='cut_thrust', clinch=3, hand_guard=0.3, blade_guard=0.13, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.516, mass_kg=1.7, extent_m=1.2),  # blade (nagasa)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.115, extent_m=0.082),  # tsuba
    ],
   haft=dict(x_m=-0.222, mass_kg=0.23, extent_m=0.444),
   pommel=dict(x_m=-0.444, mass_kg=0.03),
   geometry=dict(curvature=0.2, point_concentration=0.55, cross_section=0.62, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='heavy', spd=0, hand='Demanding'),
 'tsurugi': dict(
   mass=0.605, head_len=2.1367, grip_len=0.7973, hands=1, head='cut_thrust', clinch=4, hand_guard=0.3, blade_guard=0.4,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.299, mass_kg=0.43, extent_m=0.684),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.065, extent_m=0.06),  # guard (simple cross/collar-type, pre-tsuba chokuto fitting)
    ],
   haft=dict(x_m=-0.1196, mass_kg=0.09, extent_m=0.2392),
   pommel=dict(x_m=-0.2392, mass_kg=0.02),
   geometry=dict(curvature=0.0, point_concentration=0.6, cross_section=0.68, edge_keenness=0.8, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Standard'),
 'changdao': dict(
   mass=1.475, head_len=3.9367, grip_len=2.5633, hands=2, head='cut_thrust', clinch=4, hand_guard=0.28, blade_guard=0.15, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.546, mass_kg=0.95, extent_m=1.27),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.095, extent_m=0.09),  # wenxu crossguard
    ],
   haft=dict(x_m=-0.3845, mass_kg=0.4, extent_m=0.769),
   pommel=dict(x_m=-0.769, mass_kg=0.03),
   geometry=dict(curvature=0.25, point_concentration=0.55, cross_section=0.7, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=-0.2, hand='Standard'),
 'nandao': dict(
   mass=1.24, head_len=2.726, grip_len=0.924, hands=2, head='curved_cut', clinch=2, hand_guard=0.25, blade_guard=0.05, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3828, mass_kg=0.95, extent_m=0.87),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.05, extent_m=0.05),  # S-shaped integrated guard
    ],
   haft=dict(x_m=-0.1386, mass_kg=0.09, extent_m=0.2772),
   pommel=dict(x_m=-0.2772, mass_kg=0.15),
   geometry=dict(curvature=0.3, point_concentration=0.35, cross_section=0.6, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='heavy', spd=1.2, hand='Standard'),
 'jian': dict(
   mass=0.835, head_len=2.35, grip_len=0.8, hands=1, head='cut_thrust', clinch=2, hand_guard=0.25, blade_guard=0.25, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.33, mass_kg=0.6, extent_m=0.75),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.035, extent_m=0.055),  # disc guard
    ],
   haft=dict(x_m=-0.12, mass_kg=0.1, extent_m=0.24),
   pommel=dict(x_m=-0.24, mass_kg=0.1),
   geometry=dict(curvature=0.0, point_concentration=0.7, cross_section=0.68, edge_keenness=0.75, strike_concentration=0.0),
   reach='long', wt='light', spd=1.8, hand='Demanding'),
 'scimitar': dict(
   mass=0.95, head_len=2.7073, grip_len=0.8427, hands=1, head='curved_cut', clinch=2, hand_guard=0.4, blade_guard=0.15, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3847, mass_kg=0.68, extent_m=0.855),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.06, extent_m=0.09),  # cross-guard with langets
    ],
   haft=dict(x_m=-0.1264, mass_kg=0.09, extent_m=0.2528),
   pommel=dict(x_m=-0.2528, mass_kg=0.12),
   geometry=dict(curvature=0.55, point_concentration=0.3, cross_section=0.55, edge_keenness=0.9, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Standard'),
 'pulwar': dict(
   mass=0.86, head_len=2.418, grip_len=0.832, hands=1, head='curved_cut', clinch=2, hand_guard=0.25, blade_guard=0.1, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3354, mass_kg=0.64, extent_m=0.78),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.05, extent_m=0.075),  # downturned quillon cross-guard with langets
    ],
   haft=dict(x_m=-0.1248, mass_kg=0.08, extent_m=0.2496),
   pommel=dict(x_m=-0.2496, mass_kg=0.09),
   geometry=dict(curvature=0.6, point_concentration=0.25, cross_section=0.5, edge_keenness=0.9, strike_concentration=0.0),
   reach='long', wt='light', spd=1.2, hand='Forgiving'),
 'shamshir': dict(
   mass=0.77, head_len=2.457, grip_len=0.893, hands=1, head='curved_cut', clinch=5, hand_guard=0.3, blade_guard=0.1, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3321, mass_kg=0.58, extent_m=0.81),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.04, extent_m=0.08),  # plain cross-guard
    ],
   haft=dict(x_m=-0.134, mass_kg=0.08, extent_m=0.2679),
   pommel=dict(x_m=-0.2679, mass_kg=0.07),
   geometry=dict(curvature=0.7, point_concentration=0.08, cross_section=0.42, edge_keenness=0.95, strike_concentration=0.0),
   reach='long', wt='light', spd=2.2, hand='Demanding'),
 'szabla': dict(
   mass=0.95, head_len=2.815, grip_len=0.685, hands=1, head='cut_thrust', clinch=4, hand_guard=0.5, blade_guard=0.3,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.42, mass_kg=0.52, extent_m=0.849),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.05, extent_m=0.12),  # knucklebow / cross-hilt with quillons
    ],
   haft=dict(x_m=-0.1027, mass_kg=0.17, extent_m=0.2055),
   pommel=dict(x_m=-0.2055, mass_kg=0.21),
   geometry=dict(curvature=0.3, point_concentration=0.6, cross_section=0.62, edge_keenness=0.9, strike_concentration=0.0),
   reach='long', wt='light', spd=2.0, hand='Demanding'),
 'cinquedea': dict(
   mass=0.8, head_len=1.2, grip_len=0.75, hands=1, head='cut_thrust', clinch=4, hand_guard=0.2, blade_guard=0.1, reach_adj=-0.4,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.135, mass_kg=0.4, extent_m=0.45),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.02, extent_m=0.09),  # simple curved guard-bar
    ],
   haft=dict(x_m=-0.1125, mass_kg=0.15, extent_m=0.225),
   pommel=dict(x_m=-0.225, mass_kg=0.23),
   geometry=dict(curvature=0.0, point_concentration=0.55, cross_section=0.8, edge_keenness=0.75, strike_concentration=0.0),
   reach='short', wt='light', spd=1.5, hand='Forgiving'),
 'flamberge': dict(
   mass=2.7001, head_len=4.0167, grip_len=1.4833, hands=2, head='cut_thrust', clinch=6, hand_guard=0.55, blade_guard=0.75, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3, mass_kg=0.8859, extent_m=0.75, edge_undulation=dict(amplitude_mm=15.0, period_mm=90.0)),  # blade (flame-ground section, forte-to-mid)
     dict(x_m=0.98, mass_kg=0.4641, extent_m=0.45),  # blade tip (plain distal section + Parierhaken zone)
     dict(x_m=0.0, mass_kg=0.1688, extent_m=0.18),  # ricasso (blunted forward gripping section)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.2953, extent_m=0.3),  # main cross-guard with quillons
     dict(x_m=0.75, mass_kg=0.1266, extent_m=0.1),  # Parierhaken (hooked side-lugs)
    ],
   haft=dict(x_m=-0.2225, mass_kg=0.297, extent_m=0.445),
   pommel=dict(x_m=-0.445, mass_kg=0.4624),
   geometry=dict(curvature=0.0, point_concentration=0.62, cross_section=0.82, edge_keenness=0.8, strike_concentration=0.1),
   reach='long', wt='heavy', spd=0, hand='Demanding'),
 'estoc': dict(
   mass=2.0, head_len=3.7483, grip_len=1.4817, hands=2, head='point', clinch=8, hand_guard=0.35, blade_guard=0.75, reach_adj=0.1,
   wclass='bladed', hilt='compound',
   elements=[
     dict(x_m=0.55, mass_kg=1.15, extent_m=1.149),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.18, extent_m=0.24),  # cruciform guard with long quillons
     dict(x_m=0.03, mass_kg=0.04, extent_m=0.05),  # finger rings / side rings
    ],
   haft=dict(x_m=-0.2223, mass_kg=0.18, extent_m=0.4445),
   pommel=dict(x_m=-0.4445, mass_kg=0.45),
   geometry=dict(curvature=0.0, point_concentration=0.9, cross_section=0.95, edge_keenness=0.05, strike_concentration=0.0),
   reach='long', wt='heavy', spd=-0.5, hand='Demanding'),
 # half-sword: the SHORTENED estoc (mit dem kurzen Schwert on an edgeless armoured thruster). Auto-switched form.
 'estoc_halfsword': dict(
   mass=2.0, head_len=1.3317, grip_len=3.8983, hands=2, head='point', clinch=9, hand_guard=0.25, blade_guard=0.5, reach_adj=0.1,
   wclass='bladed', hilt='compound',
   elements=[
     dict(x_m=0.2, mass_kg=0.4, extent_m=0.399),  # free blade tip (forward of the new hand-on-blade grip point)
    ],
   guards=[
     dict(x_m=-0.75, mass_kg=0.18, extent_m=0.24),  # cruciform guard with long quillons (now behind the working hand)
     dict(x_m=-0.72, mass_kg=0.04, extent_m=0.05),  # finger rings / side rings
    ],
   haft=dict(x_m=-0.385, mass_kg=0.93, extent_m=1.569),
   pommel=dict(x_m=-1.1695, mass_kg=0.45),
   geometry=dict(curvature=0.0, point_concentration=0.95, cross_section=0.95, edge_keenness=0.05, strike_concentration=0.0),
   reach='short', wt='heavy', spd=-0.5, hand='Demanding', base='estoc'),
 'falchion': dict(
   mass=1.0, head_len=2.8017, grip_len=0.6183, hands=1, head='straight_cut', clinch=4, hand_guard=0.45, blade_guard=0.4, reach_adj=-0.1,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.44, mass_kg=0.65, extent_m=0.801),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.07, extent_m=0.14),  # simple cross-guard with quillons (baseline archaeological quillon-hilted form)
    ],
   haft=dict(x_m=-0.0927, mass_kg=0.08, extent_m=0.1855),
   pommel=dict(x_m=-0.1855, mass_kg=0.2),
   geometry=dict(curvature=0.15, point_concentration=0.3, cross_section=0.65, edge_keenness=0.85, strike_concentration=0.0),
   reach='long', wt='light', spd=1.5, hand='Standard'),
 'rondel': dict(
   mass=0.35, head_len=0.8, grip_len=0.4, hands=1, head='point', clinch=9, hand_guard=0.55, blade_guard=0.12,
   wclass='bladed', hilt='none',
   elements=[
     dict(x_m=0.12, mass_kg=0.235, extent_m=0.24),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.045, extent_m=0.055),  # hand_guard_disc
    ],
   haft=dict(x_m=-0.06, mass_kg=0.05, extent_m=0.12),
   pommel=dict(x_m=-0.12, mass_kg=0.02),
   geometry=dict(curvature=0.0, point_concentration=0.97, cross_section=0.85, edge_keenness=0.05, strike_concentration=0.0),
   reach='short', wt='light', spd=3.0, hand='Standard'),
 'main_gauche': dict(
   mass=0.55, head_len=1.0, grip_len=0.45, hands=1, head='point', clinch=4, hand_guard=0.85, blade_guard=0.65, reach_adj=-0.2,
   wclass='bladed', hilt='compound',
   elements=[
     dict(x_m=0.15, mass_kg=0.24, extent_m=0.3),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.16, extent_m=0.14),  # quillon_and_ring_and_shell_complex
     dict(x_m=0.0, mass_kg=0.02, extent_m=0.05),  # side_ring
    ],
   haft=dict(x_m=-0.0675, mass_kg=0.09, extent_m=0.135),
   pommel=dict(x_m=-0.135, mass_kg=0.04),
   geometry=dict(curvature=0.0, point_concentration=0.7, cross_section=0.75, edge_keenness=0.3, strike_concentration=0.0),
   reach='short', wt='light', spd=1.5, hand='Demanding'),
 'stiletto': dict(
   mass=0.22, head_len=0.9, grip_len=0.35, hands=1, head='point', clinch=7, hand_guard=0.2, blade_guard=0.05,
   wclass='bladed', hilt='none',
   elements=[
     dict(x_m=0.135, mass_kg=0.155, extent_m=0.27),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.01, extent_m=0.03),  # collar_guard
    ],
   haft=dict(x_m=-0.0525, mass_kg=0.043, extent_m=0.105),
   pommel=dict(x_m=-0.105, mass_kg=0.012),
   geometry=dict(curvature=0.0, point_concentration=0.99, cross_section=0.9, edge_keenness=0.02, strike_concentration=0.0),
   reach='short', wt='light', spd=3.0, hand='Demanding'),
 'misericorde': dict(
   mass=0.28, head_len=1.0, grip_len=0.45, hands=1, head='point', clinch=7, hand_guard=0.15, blade_guard=0.03,
   wclass='bladed', hilt='none',
   elements=[
     dict(x_m=0.15, mass_kg=0.185, extent_m=0.3),  # blade
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.022, extent_m=0.045),  # hand_guard_disc
    ],
   haft=dict(x_m=-0.0675, mass_kg=0.055, extent_m=0.135),
   pommel=dict(x_m=-0.135, mass_kg=0.018),
   geometry=dict(curvature=0.0, point_concentration=0.96, cross_section=0.83, edge_keenness=0.1, strike_concentration=0.0),
   reach='short', wt='light', spd=3.0, hand='Forgiving'),
 'hook_sword': dict(
   mass=0.75, head_len=1.5, grip_len=0.5, hands=1, head='curved_cut', clinch=5, hand_guard=0.55, blade_guard=0.75, reach_adj=-0.3,
   wclass='bladed', hilt='compound',
   elements=[
     dict(x_m=0.225, mass_kg=0.38, extent_m=0.45),  # blade_with_hooked_tip
     dict(x_m=0.0, mass_kg=0.14, extent_m=0.183),  # crescent_hand_guard_striking_element
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.0, extent_m=0.183, dual_role_element=True),  # crescent_hand_guard_striking_element
    ],
   haft=dict(x_m=-0.075, mass_kg=0.18, extent_m=0.15),
   pommel=dict(x_m=-0.15, mass_kg=0.05),
   geometry=dict(curvature=0.22, point_concentration=0.55, cross_section=0.65, edge_keenness=0.6, strike_concentration=0.0),
   reach='short', wt='light', spd=2.5, hand='Demanding'),
}

# Bake the geometry coefficient surface ONCE at import (zero runtime cost): geometry derives `gap` (and
# thrust/cut/perc_conc/halfsword for downstream wiring) from each weapon's nested geometry.
import geometry as _geo
for _w, _rec in WEAPONS.items():
    _b = _geo.bake(_rec['geometry'])
    _rec['gap'] = _b['gap']
    _rec['geo'] = _b   # full baked surface available to modules

# Bake each MULTI-MODE composite's per-element combat geometry ONCE at import (morphology-rearch Phase B2:
# the located mass elements now have a parallel combat-geometry view for weapons whose parts afford genuinely
# different fight-modes — a bec de corbin's hammer face vs beak vs spike — grounded per-element against Phase 0
# geom_notes, see designs/audit/2026-07-02-morphology-rearch-phase0/. Single-mode weapons carry no
# `mode_elements` key; systems._mode_elements() already defaults them to the whole-weapon head+geo.
for _w, _rec in WEAPONS.items():
    for _me in _rec.get('mode_elements', ()):
        _me['geo'] = _geo.bake(_me.pop('geometry'))

# Bake the derive() mass-family statistics ONCE at import (honors the bake-once contract — derive() was
# recomputed many times per beat via agility/at_grip/defense_affinities/percussion_authority; the record's
# located parts are static, so the result is too). weapon_physics.derive returns the cached '_derived' when
# present; a record mutated after bake is OUT OF CONTRACT, exactly as it already is for the baked geo/gap
# above. Cycle-free: weapon_physics imports only math at module scope.
import weapon_physics as _wp
for _w, _rec in WEAPONS.items():
    _rec['_derived'] = _wp.derive(_rec)

# Back-compat view: GEOMETRY as a name-keyed map onto each record's nested geometry (consumers: the systems
# key-sync assert, weapon_physics docstring). The single source is WEAPONS[w]['geometry'].
GEOMETRY = {_w: _rec['geometry'] for _w, _rec in WEAPONS.items()}

# HALF-SWORD FORM mapping (weapon data): which base weapon switches to which shortened gripped-blade form. The
# inverse is DERIVED (not a second hand-maintained dict). Read by systems.halfsword_target + capabilities.
HALFSWORD_FORM = {'longsword': 'longsword_halfsword', 'estoc': 'estoc_halfsword'}
HALFSWORD_BASE = {_form: _base for _base, _form in HALFSWORD_FORM.items()}
