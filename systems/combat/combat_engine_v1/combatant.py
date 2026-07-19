"""Combatant — built ONCE at init; identity (which fighter) never changes. The wrapper passes a Combatant
to every subsystem as `aggressor` or `defender`; no subsystem ever sees raw 'A'/'B'. This is the structural
fix for the frame-mapping bug class: roles are objects, not positional/dict keys."""

# The weapons DICTIONARY + GEOMETRY live in weapons.py (the data layer); the DERIVATION in weapon_physics.py.
# Re-exported here so existing `from combatant import WEAPONS` call-sites keep working (the canonical home is weapons.py).
from weapons import WEAPONS, GEOMETRY, HALFSWORD_FORM, HALFSWORD_BASE  # noqa: F401  (data lives in weapons.py)

# ---- COMBAT-STATE KERNEL (relocated verbatim, ED-1085 container de-leak 2026-07-01) ----
# Previously imported from the FROZEN tests/sim/v32-combat-balance/ harness (r2_consequence_wounds /
# r5_strength_stamina via r8_parity_harness) through a sys.path hack that dragged numpy into the
# engine runtime. The live engine owns its state kernel (holonic doctrine §3); the frozen harness
# keeps its historical copies for its own archived runs. Formulas and constants are byte-identical
# to the r2/r5 originals; provenance tags carried over.

# WOUND_POOL_PENALTY removed 2026-07-08 (ED-PC-0005 ruling: wounds NEVER cut pools -1D; each wound
# adds a fractional Ob — combat = ED-1041's bilateral WOUND_ATK_OB/WOUND_DEF_OB in config.py, applied
# in systems.py). The dead pool_penalty() method (zero callers) was deleted in the same pass and
# derived_stats_v30 §4.1 was rewritten to the fractional-Ob model (reverses PP-716).
SPI_WI_W = 0.4               # [D-A noise, Jordan 2026-06-18: Spirit at low weight increases the Wound Interval -> reduces uniformity]
STR_HEALTH_W = 0.25          # [D-A noise, Jordan 2026-06-18: Strength at very low weight, proportional to Endurance, into Health -> reduces uniformity]
WOUND_INTERVAL_BASE = 4      # [D-A recalib, Jordan 2026-06-18: flat base lowered 6->4; 2 pts moved into Spirit/Strength terms, conserving avg Health=40]
MAXWOUNDS_DIV = 2            # [canonical: derived_stats_v30 §4.1 (floor(Endurance / 2))]
MAXWOUNDS_ADD = 1            # [canonical: derived_stats_v30 §4.1 (+1)]
MAXWOUNDS_CAP = 3            # [canonical: derived_stats_v30 §4.1 (Max Wounds capped at 3, PP-717)]
STAMINA_PER_END = 3          # [canonical: derived_stats §4.2 — proposed-canon replacement; End contribution to Stamina; replaces Endurance x5; sim-tunable]
STAMINA_PER_SPIRIT = 2       # [canonical: derived_stats §4.2 — proposed-canon replacement; Spirit contribution to Stamina (energy reserves); sim-tunable]


def max_wounds(end):
    """Max Wounds (derived_stats_v30 §4.1, authoritative): min(floor(End/2)+1, cap)."""
    return min(end // MAXWOUNDS_DIV + MAXWOUNDS_ADD, MAXWOUNDS_CAP)


def wound_interval(end, spirit=3):
    """Wound Interval (derived_stats_v30 §4.1): End + base + low-weight Spirit (D-A, Jordan 2026-06-18)."""
    return round(end + WOUND_INTERVAL_BASE + SPI_WI_W*spirit)


def health_full(end, spirit=3, strength=4):
    """Full Health (derived_stats_v30 §4.1): WI x (MaxWounds+1) + low-weight Strength*Endurance (D-A, Jordan 2026-06-18)."""
    return round(wound_interval(end, spirit) * (max_wounds(end) + 1) + STR_HEALTH_W*strength*end)


def stamina_max(end, spirit):
    """Recomposed Stamina reserve = f(End, Spirit). Replaces canonical Endurance x 5 (Jordan decision)."""
    return STAMINA_PER_END * int(round(end)) + STAMINA_PER_SPIRIT * int(round(spirit))


class WoundTracker:
    """The authoritative non-resetting wound-gate tracker (derived_stats_v30 §4.1).
    Health depletes; every WI of cumulative damage is a wound gate; a single hit larger than WI
    crosses multiple gates at once (the decisive strike). Felled at Health depletion (D-A reshape).
    Wounds add a fractional Ob per wound (combat: ED-1041 bilateral WOUND_ATK_OB/WOUND_DEF_OB in
    config.py/systems.py) — NEVER a -1D pool cut (Jordan ruling 2026-07-08, ED-PC-0005, which
    reversed PP-716's -1D and deleted the old pool_penalty() here). Persists between
    encounters (cleared only at session end, per canon)."""

    def __init__(self, end, equipment_health=0, spirit=3, strength=4):
        self.end = end; self.spirit = spirit; self.strength = strength
        self.wi = wound_interval(end, spirit)
        self.max_wounds = max_wounds(end)
        self.health_full = health_full(end, spirit, strength) + equipment_health
        self.cumulative_damage = 0

    @property
    def health_remaining(self):
        return max(0, self.health_full - self.cumulative_damage)

    @property
    def wounds(self):
        """Wounds accrued = floor(cumulative_damage / WI), capped at MW+1 (felled)."""
        return min(self.cumulative_damage // self.wi, self.max_wounds + 1)

    @property
    def felled(self):
        """Incapacitated at Health depletion (cumulative damage >= Health). Health carries a low-weight
        Strength buffer (D-A reshape, Jordan-ratified), so Strength now buys survivability; coincides with the
        old MW+1-wound rule when that buffer is zero. (The wound counter still caps at MW+1; wound
        impairment is applied as a fractional Ob via the ED-1041 channel, not a pool cut -- ED-PC-0005.)"""
        return self.cumulative_damage >= self.health_full

    def apply(self, damage):
        """Apply a strike's damage. Returns (new_wounds_inflicted, felled). A hit > WI inflicts
        multiple wounds at once -- the decisive blow crossing several gates."""
        before = self.wounds
        self.cumulative_damage += max(0, int(damage))
        inflicted = self.wounds - before
        return inflicted, self.felled


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
        self.sel_head=None                    # SELECTED use-mode head token for this exchange (systems.select_mode); None = use the native weapon head. Set per-beat by the wrapper (mirrors grip_position); routes into core.strike / adef_cap / legibility.
        self.sel_dmg=None                     # SELECTED damage-mode ('percussion'/'shear'/'puncture') for this exchange; read by systems.legibility (thrust hard / cut+percuss easy). None = head-inferred fallback.
        # ---- circumstance-degradation scaffold (I1, D11a, closing-distance redesign — designs/audit/2026-07-02-
        # scene-combat-closing-distance-redesign/) — all default to IDEAL so the added surface is byte-identical
        # until a later increment wires a live reader. ----
        self.sel_gap=None                     # SELECTED element's own geo['gap'] (systems.select_mode's widened 5-tuple, I2/D2b); None = native w['gap'] fallback. Canonical gap source for core.strike/adef_cap/the select_mode comparator (fixes M-02's object confusion).
        self.sel_perc=None                    # SELECTED element's own percussion (I2/D2b); None = native WP.percussion_authority(w) fallback. Canonical perc source for core.strike (fixes BLOCKER-2).
        self.sel_pc=None                      # SELECTED element's own point_concentration (I2/D2b, capstone M2 fix); None = native whole-weapon point_concentration fallback. Sources D2's cut_thrust Φ_grip blend (I2), D5's close_efficacy (I4), D4's swing-room legibility term (I5).
        self.sel_eff=None                     # SELECTED element's own derived cut/thrust magnitude (U2/ED-PC-0011); None = no scaling (core.coupling treats it as "at/above reference"). Scales core.coupling's 'cut' token DELIVERY only; inert for every other head.
        self.range_avail=1.0                  # CONTINUOUS swing-room available in [0,1] (I5/D4, systems.range_utilization); 1.0 = full room (ideal, identity). Reshapes commit_depth's Beta draw + the swing-room legibility term; never adds/reorders a draw.
        self.facing=0.0                       # CONTINUOUS facing state (I6/D6, systems.facing_target); 0.0 = neutral (identity). Feeds a lateral-void closing term + a small profile term in reach_sigma/legibility; keyed on stance/measure/grip only (C2), never weapon class.
        self.skills=skills or {}            # equippable per-axis skill biases (mastery-stack + set bonuses)
        self.equipped=equipped or []        # equipped tradition abilities (modulators over the substrate; default none)
        # ---- DERIVED CHARACTER FIGURES — the combatant is the HOST; core/systems CONSUME these, never recompute ----
        self.pool=max(5, history+6)                          # resolution pool (History)
        self.wt=WoundTracker(end, spirit=self.spirit, strength=self.strength)
        self.health_full=self.wt.health_full                 # total Health (End+Spirit+Str buffer)
        self.wound_interval=self.wt.wi                       # damage per wound-gate (WI)
        self.max_wounds=self.wt.max_wounds                   # wound-gate cap (felled beyond)
        self.stamina_max=stamina_max(end, self.spirit)       # max stamina from Endurance+Spirit (cfg-free)
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
