"""Combatant — built ONCE at init; identity (which fighter) never changes. The wrapper passes a Combatant
to every subsystem as `aggressor` or `defender`; no subsystem ever sees raw 'A'/'B'. This is the structural
fix for the frame-mapping bug class: roles are objects, not positional/dict keys."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../tests/sim/v32-combat-balance'))
import r8_parity_harness as r8

# The weapons DICTIONARY + GEOMETRY live in weapons.py (the data layer); the DERIVATION in weapon_physics.py.
# Re-exported here so existing `from combatant import WEAPONS` call-sites keep working (the canonical home is weapons.py).
from weapons import WEAPONS, GEOMETRY, COMPOSITE  # noqa: F401


class Combatant:
    def __init__(self, label, strength=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3,
                 history=3, disp=4, weapon='arming', armor='light', skills=None, equipped=None, tradition='none'):
        self.label=label
        self.strength=strength; self.agi=agi; self.end=end
        self.cog=cog; self.att=att; self.spirit=spirit; self.focus=focus
        self.history=history
        self.disp=disp                       # disposition / temperament, aggression axis (1-7, 4=neutral); lean=(disp-4)/3, orthogonal to tradition
        self.weapon=weapon; self.armor=armor
        self.tradition=tradition             # cognitive-mode profile (selection-weights over the substrate)
        self.grip='normal'                   # grip/stance state: normal | choke (close, leverage) | lunge (reach, commit)
        self.skills=skills or {}            # equippable per-axis skill biases (mastery-stack + set bonuses)
        self.equipped=equipped or []        # equipped tradition abilities (modulators over the substrate; default none)
        # derived (canonical)
        self.pool=max(5, history+6)
        self.wt=r8.WoundTracker(end, spirit=self.spirit, strength=self.strength)
        self.health_full=self.wt.health_full
        # live state (reset/managed by wrapper)
        self.stamina=0.0; self.stamina_max=0.0
        self.conc=0.0; self.conc_max=0.0
        self.ready=0.0
        self.initiative=0.0                  # the Vor/Nach state (signed; +ve = holds initiative). Reset/managed by wrapper.
        self.poise=1.0                   # kuzushi/balance (1.0=balanced, broken downward). Reset/managed by wrapper.
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
