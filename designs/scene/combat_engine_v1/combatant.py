"""Combatant — built ONCE at init; identity (which fighter) never changes. The wrapper passes a Combatant
to every subsystem as `aggressor` or `defender`; no subsystem ever sees raw 'A'/'B'. This is the structural
fix for the frame-mapping bug class: roles are objects, not positional/dict keys."""
import sys; sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/v32')
import r8_parity_harness as r8

# canonical weapon axis-vectors (weapon_axes_v2 §5)
WEAPONS = {
 # gap = gap-thrust precision (0-1, reference §4). head_len / grip_len = lever-arm. NEW hilt/guard primitive:
 # hand_guard (0-1) = PASSIVE hand/forearm protection (bare tang 0 -> simple cross ~0.4 -> side-rings/knuckle ~0.6
 # -> swept/cup ~0.9): governs how safely the hand can be committed forward + parry without being hit.
 # blade_guard (0-1) = ACTIVE blade-catching/winding utility of the cross/quillons/rings (none on a guardless pole;
 # high on a long cross; fore/thumb-rings "enhance winding"): governs bind-catch + wind capability.
 'rapier':   dict(reach='long', wt='light', hands=1, head='point',  spd=1.5, hand='Demanding', gap=0.40, head_len=3.2, grip_len=0.6, hand_guard=0.90, blade_guard=0.45, reach_adj=0.15, clinch=2, percussion=0),
 'arming':   dict(reach='long', wt='light', hands=1, head='cut_thrust', spd=1.5, hand='Standard', gap=0.65, head_len=2.4, grip_len=0.8, hand_guard=0.40, blade_guard=0.55, reach_adj=-0.6, clinch=4, percussion=2),
 'longsword':dict(reach='long', wt='heavy', hands=2, head='cut_thrust', spd=0.5, hand='Standard', gap=0.90, head_len=2.8, grip_len=1.6, hand_guard=0.45, blade_guard=0.85, reach_adj=-0.9, clinch=6, percussion=4),
 'greatsword':dict(reach='long',wt='heavy', hands=2, head='straight_cut', spd=0.0, hand='Demanding', gap=0.70, head_len=3.6, grip_len=1.8, hand_guard=0.55, blade_guard=0.70, reach_adj=-0.05, clinch=3, percussion=3),
 'sabre':    dict(reach='long', wt='light', hands=1, head='curved_cut', spd=2.0, hand='Standard', gap=0.40, head_len=2.6, grip_len=0.7, hand_guard=0.70, blade_guard=0.45, reach_adj=-0.1, clinch=3, percussion=1),
 'dagger':   dict(reach='short',wt='light', hands=1, head='cut_thrust', spd=3.0, hand='Forgiving', gap=1.00, head_len=0.7, grip_len=0.4, hand_guard=0.30, blade_guard=0.40, clinch=10, percussion=1),
 'paired_short':dict(reach='short',wt='light',hands=1,head='cut_thrust', spd=2.5, hand='Demanding', gap=0.65, head_len=1.4, grip_len=0.5, hand_guard=0.55, blade_guard=0.50, reach_adj=1.4, clinch=5, percussion=2),
 'spear':    dict(reach='long', wt='light', hands=2, head='point',  spd=0.0, hand='Forgiving', gap=0.70, head_len=5.5, grip_len=1.2, hand_guard=0.10, blade_guard=0.20, clinch=2, percussion=1),
 'staff':    dict(reach='long', wt='light', hands=2, head='blunt',  spd=0.0, hand='Forgiving', gap=0.20, head_len=2.8, grip_len=2.8, hand_guard=0.15, blade_guard=0.30, reach_adj=0.5, clinch=3, percussion=4),
 'mace':     dict(reach='long', wt='heavy', hands=1, head='blunt',  spd=0.0, hand='Forgiving', gap=0.20, head_len=1.8, grip_len=0.7, hand_guard=0.45, blade_guard=0.30, reach_adj=-0.55, clinch=4, percussion=8),
 'poleaxe':  dict(reach='long', wt='heavy', hands=2, head='blunt',  spd=-0.5,hand='Demanding', gap=0.85, head_len=2.2, grip_len=2.2, hand_guard=0.30, blade_guard=0.60, reach_adj=-0.05, clinch=5, percussion=8),
 # half-sword: the SHORTENED longsword (mit dem kurzen Schwert) — one hand grips the blade. Auto-switched form (see
 # halfsword_switch): short reach, supreme gap-thrust + leverage for the bind/armour, but loses cutting & cadence.
 'longsword_halfsword':dict(reach='short', wt='heavy', hands=2, head='point', spd=-0.5, hand='Demanding', gap=1.00, head_len=1.4, grip_len=2.6, hand_guard=0.35, blade_guard=0.25, clinch=7, percussion=4, base='longsword'),
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

# Bake the precalculated coefficient surface ONCE at import (zero added runtime cost): geometry derives `gap`
# (and thrust/cut/perc_conc/halfsword for downstream wiring) from each weapon's geometry, overriding hand-set gap.
import geometry as _geo
for _w, _params in GEOMETRY.items():
    if _w in WEAPONS:
        _b = _geo.bake(_params)
        WEAPONS[_w]['gap'] = _b['gap']
        WEAPONS[_w]['geo'] = _b   # full baked surface available to modules


class Combatant:
    def __init__(self, label, strength=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3,
                 history=3, footwork=3, weapon='arming', armor='light', skills=None, tradition='none'):
        self.label=label
        self.strength=strength; self.agi=agi; self.end=end
        self.cog=cog; self.att=att; self.spirit=spirit; self.focus=focus
        self.history=history; self.footwork=footwork
        self.weapon=weapon; self.armor=armor
        self.tradition=tradition             # cognitive-mode profile (selection-weights over the substrate)
        self.grip='normal'                   # grip/stance state: normal | choke (close, leverage) | lunge (reach, commit)
        self.skills=skills or {}            # equippable per-axis skill biases (mastery-stack + set bonuses)
        # derived (canonical)
        self.pool=max(5, history+6)
        self.wt=r8.WoundTracker(end)
        self.health_full=self.wt.health_full
        # live state (reset/managed by wrapper)
        self.stamina=0.0; self.stamina_max=0.0
        self.conc=0.0; self.conc_max=0.0
        self.ready=0.0
    # weapon vector accessors
    @property
    def w(self): return WEAPONS[self.weapon]
    @property
    def reach(self): return WEAPONS[self.weapon]['reach']
    @property
    def head(self): return WEAPONS[self.weapon]['head']
    @property
    def weight(self): return WEAPONS[self.weapon]['wt']
    @property
    def felled(self): return self.wt.felled
    def apply_wound(self, d):
        if d>0: self.wt.apply(d)
    def skill(self, axis): return self.skills.get(axis, 0.0)   # 0 = untrained; positive = trained bonus on that axis
