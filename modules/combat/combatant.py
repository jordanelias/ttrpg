"""Combatant — built ONCE at init; identity (which fighter) never changes. The wrapper passes a Combatant
to every subsystem as `aggressor` or `defender`; no subsystem ever sees raw 'A'/'B'. This is the structural
fix for the frame-mapping bug class: roles are objects, not positional/dict keys."""

# The weapons DICTIONARY + GEOMETRY live in weapons.py (the data layer); the DERIVATION in weapon_physics.py.
# Re-exported here so existing `from combatant import WEAPONS` call-sites keep working (the canonical home is weapons.py).
from weapons import WEAPONS, GEOMETRY, HALFSWORD_FORM, HALFSWORD_BASE  # noqa: F401  (data lives in weapons.py)
import attributes as _A   # the attribute spec, the one owner of which attributes exist (PC-14)
from config import CFG    # conc_max's coefficients when rederive() is given no cfg

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
    reversed PP-716's -1D and deleted the old pool_penalty() here). Damage is held on the tracker
    and zeroed at the start of each fight (`wrapper.fight`)."""

    def __init__(self, end, equipment_health=0, spirit=3, strength=4):
        self.equipment_health = equipment_health
        self.rederive(end, spirit=spirit, strength=strength)
        self.cumulative_damage = 0

    def rederive(self, end, spirit=3, strength=4):
        """Recompute the maxima (WI, Max Wounds, full Health) from the attributes (PC-14). Touches NO damage:
        `cumulative_damage` is left as it stands: damage taken is never erased by an attribute edit. The maxima are
        recomputed, so `wounds`, `health_remaining` and `felled` are re-read against the kept damage (raising `end`
        can lift a felled fighter, lowering it can fell one). A fight's own start zeroes the damage, in `wrapper.fight`."""
        self.wi = wound_interval(end, spirit)
        self.max_wounds = max_wounds(end)
        self.health_full = health_full(end, spirit, strength) + self.equipment_health

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
    """THE ATTRIBUTES (PC-14): one storage, `self.attrs`, a dict keyed by `attributes.KEYS` (the spec is the one owner of
    which attributes exist and their defaults). Each key is also a generated property with a getter AND a setter
    (`c.history`, `c.history = 5`), so every read and assignment site keeps working; a setter is `set_attr`, which
    re-derives. `Combatant(label, attrs=None, **kw)`: `attrs` is a `{key: value}` dict, `**kw` takes the same keys as
    keywords (a key given both ways is a TypeError, as Python's own "multiple values" is); an unknown attribute name is
    a TypeError. `disp` is disposition / temperament, the aggression axis; lean = (disp - NEUTRAL['disp'])/3,
    orthogonal to tradition."""
    def __init__(self, label, attrs=None, weapon='arming', armor='light', skills=None, equipped=None, tradition='none',
                 **kw):
        given = dict(attrs or {})
        twice = sorted(set(given) & set(kw))
        if twice:
            raise TypeError(f"Combatant() got attribute(s) {twice} both in attrs and as keywords")
        given.update(kw)
        unknown = sorted(set(given) - set(_A.KEYS))
        if unknown:
            raise TypeError(f"Combatant() got unknown attribute(s) {unknown}; the attributes are {_A.KEYS} "
                            f"(modules/combat/attributes.py)")
        self.label=label
        self.attrs = {k: given.get(k, _A.DEFAULT[k]) for k in _A.KEYS}
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
        self.equipped=equipped or []        # LEARNED techniques (ability_primitives): a LIST of names (each level 1.0) OR a DICT {name: level} for graded levels-of-investment (level>=0; 0=untrained/inert). Efficacy emerges from the invested level, not tradition membership (ED-PC-0023). Default none.
        # ---- DERIVED CHARACTER FIGURES — the combatant is the HOST; core/systems CONSUME these, never recompute ----
        # (resolution pool is NOT hosted here: the live engine calls core.resolution_pool(history) directly, and a
        # second hardcoded `self.pool=max(5,history+6)` here was a dead re-implementation of that rule with ZERO
        # readers — removed ED-PC-0023 audit, §8 "every rule lives once". Any consumer needing the pool calls
        # core.resolution_pool.)
        a = self.attrs
        self.wt=WoundTracker(a['end'], spirit=a['spirit'], strength=a['strength'])
        # ---- live state (reset/managed by the wrapper each bout) ----
        self.stamina=0.0
        self.conc=0.0
        self._cfg=None                                       # the cfg of the last derivation (None: config.CFG)
        self.rederive()                                      # stamina_max (End+Spirit) and conc_max (3*Focus+2*Spirit)
        # ED-PC-0035: the dead `self.ready` attribute is GONE — it was written here and in wrapper._init_live but READ
        # nowhere; the live readiness state is the wrapper's LOCAL `ready={A:..,B:..}` dict. Carried state that resets
        # to no effect is worse than absent state: it reads as though the engine tracks it.
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
    def rederive(self, cfg=None):
        """THE ONE DERIVATION PATH (PC-14): every figure derived from `attrs`, re-computed from the current values.
        Rebuilds the wound tracker's maxima (WI, Max Wounds, full Health) IN PLACE, PRESERVING `cumulative_damage` --
        damage taken is never erased by setting an attribute (the maxima move, so `felled` and `health_remaining` are
        re-read against it); `wrapper.fight` zeroes the damage at its own start, because a fight begins unwounded. Sets `stamina_max` (cfg-free) and `conc_max` (3*Focus+2*Spirit, ED-902, from `cfg`), and
        clamps live Stamina and Concentration DOWN to the new maxima (never raises them). `cfg=None` re-uses the cfg
        of the last derivation, `config.CFG` until one is given. Writes no Health/WI/Max-Wounds mirror on the
        Combatant (PC-11 deleted those): the tracker owns them."""
        if cfg is not None:
            self._cfg = cfg
        cfg = self._cfg if self._cfg is not None else CFG
        a = self.attrs
        self.wt.rederive(a['end'], spirit=a['spirit'], strength=a['strength'])
        self.stamina_max = stamina_max(a['end'], a['spirit'])                       # max stamina from Endurance+Spirit
        self.conc_max = cfg['CONC_FOCUS']*a['focus'] + cfg['CONC_SPIRIT']*a['spirit']   # 3F+2S (ED-902)
        self.stamina = min(self.stamina, self.stamina_max)
        self.conc = min(self.conc, self.conc_max)

    def set_attr(self, key, value):
        """Re-value one attribute and re-derive (PC-14). An attribute the spec does not name is a TypeError."""
        if key not in self.attrs:
            raise TypeError(f"{key!r} is not a combat attribute; the attributes are {_A.KEYS} "
                            f"(modules/combat/attributes.py)")
        self.attrs[key] = value
        self.rederive()
    @property
    def felled(self): return self.wt.felled
    def apply_wound(self, d):
        if d>0: self.wt.apply(d)
    def skill(self, axis): return self.skills.get(axis, 0.0)   # 0 = untrained; positive = trained bonus on that axis


def _attribute_property(key):
    """`c.<key>` reads `c.attrs[key]`; `c.<key> = v` is `c.set_attr(key, v)` (it re-derives)."""
    return property(lambda self: self.attrs[key], lambda self, value: self.set_attr(key, value),
                    doc=f"combat attribute {key!r} (modules/combat/attributes.py)")


for _key in _A.KEYS:   # GENERATED from the spec: a new spec entry is a new property, with no edit here
    if hasattr(Combatant, _key):
        raise TypeError(f"attribute key {_key!r} collides with a Combatant member")
    setattr(Combatant, _key, _attribute_property(_key))
del _key
