"""Combatant — built ONCE at init; identity (which fighter) never changes. The wrapper passes a Combatant
to every subsystem as `aggressor` or `defender`; no subsystem ever sees raw 'A'/'B'. This is the structural
fix for the frame-mapping bug class: roles are objects, not positional/dict keys."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../tests/sim/v32-combat-balance'))
import r8_parity_harness as r8

# The weapons DICTIONARY + GEOMETRY live in weapons.py (the data layer); the DERIVATION in weapon_physics.py.
# Re-exported here so existing `from combatant import WEAPONS` call-sites keep working (the canonical home is weapons.py).
from weapons import WEAPONS, GEOMETRY, HALFSWORD_FORM, HALFSWORD_BASE  # noqa: F401  (data lives in weapons.py)


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
        self.grip_position=0.0               # CONTINUOUS grip-position in [0,1]: 0=as-issued (full reach), 1=gathered to the working balance (close control). Retires the choke/normal/lunge strings; derived per-beat by the wrapper from grip_target.
        self.lunge_depth=0.0                  # CONTINUOUS body-extension in [0,1] of an in-progress lunge (set at the attack; 0 = no lunge). Reads into recoverability_factor / weapon_tempo / legibility.
        self.skills=skills or {}            # equippable per-axis skill biases (mastery-stack + set bonuses)
        self.equipped=equipped or []        # equipped tradition abilities (modulators over the substrate; default none)
        # ---- DERIVED CHARACTER FIGURES — the combatant is the HOST; core/systems CONSUME these, never recompute ----
        self.pool=max(5, history+6)                          # resolution pool (History)
        self.wt=r8.WoundTracker(end, spirit=self.spirit, strength=self.strength)
        self.health_full=self.wt.health_full                 # total Health (End+Spirit+Str buffer)
        self.wound_interval=self.wt.wi                       # damage per wound-gate (WI)
        self.max_wounds=self.wt.max_wounds                   # wound-gate cap (felled beyond)
        self.stamina_max=r8.stamina_max(end, self.spirit)    # max stamina from Endurance+Spirit (cfg-free)
        self.conc_max=0.0                                    # max concentration (3*Focus+2*Spirit) — set in derive_stats(cfg)
        # ---- live state (reset/managed by the wrapper each bout) ----
        self.stamina=0.0
        self.conc=0.0
        self.ready=0.0
        self.initiative=0.0                  # the Vor/Nach state (signed; +ve = holds initiative). Reset/managed by wrapper.
        self.poise=1.0                   # kuzushi/balance (1.0=balanced, broken downward). Reset/managed by wrapper.
    # weapon vector accessors
    @property
    def w(self): return WEAPONS[self.weapon]
    @property
    def head(self): return WEAPONS[self.weapon]['head']
    # (.reach / .weight categorical accessors removed 2026-06-30 — dead vestigial; reach derives via
    #  systems.reach_base, heft via systems.wield_heft / core.heft_resp; no live consumer read these.)
    # ---- derived-figure host (the combatant computes its own; consumers import these, never recompute) ----
    def derive_stats(self, cfg):
        """Compute the cfg-dependent derived figures and store them on self (called once at bout reset). Keeps the
        derivation WITH the combatant so core/systems read c.conc_max etc. rather than calculating them."""
        self.conc_max = cfg['CONC_FOCUS']*self.focus + cfg['CONC_SPIRIT']*self.spirit   # 3F+2S (ED-902)
    @property
    def fatigue(self):
        """Current endurance fatigue in [0,1]: 0 fresh, ->1 spent. Derived from live stamina vs stamina_max."""
        return max(0.0, 1 - self.stamina/self.stamina_max) if self.stamina_max else 0.0
    @property
    def felled(self): return self.wt.felled
    def apply_wound(self, d):
        if d>0: self.wt.apply(d)
    def skill(self, axis): return self.skills.get(axis, 0.0)   # 0 = untrained; positive = trained bonus on that axis
