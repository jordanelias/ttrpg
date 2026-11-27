"""THE COMBAT ATTRIBUTE SPEC (PC-14) -- the one owner of which attributes a `Combatant` carries.

A leaf: imports only the standard library. Each entry holds COMBAT FACTS ONLY:

  key          : the engine's own attribute key (`c.agi`, `c.attrs['agi']`).
  default      : the value a fighter built without that attribute carries.
  neutral      : the centring value a formula subtracts (`c.agi - NEUTRAL['agi']`), present only where a direct
                 centring literal exists in the engine; `None` where none does.
  registry_key : the `references/descriptor_registry.yaml: attributes` key this attribute reads as, or `None`
                 where the registry names none. It is a POINTER, not a copy: the registry owns the scale, the
                 names, the aliases, the floor and the ceiling, and none of them is written here (a copied name or
                 bound would be a second owner).
  status       : `IN_FLUX` for every entry (Jordan, 2026-11-01: "ensure all attributes including history are
                 stored in such a way where they can be modified in future as they are currently in flux").

ADDING an attribute is one entry here: `Combatant` generates its property, the workbench factories and the typed
export (`tools/export_engine_params.py`, section `attributes`) read this tuple. RENAMING is the entry's `key` plus
its readers. RE-VALUING is `Combatant.set_attr` (or `c.<key> = v`), which re-derives every derived figure.

NOT delivered, and said so: re-centring the derived quantities stays formula constants anchored on the default
scale (`balance_eff - 3`, `reflex - 3`, `conc/5 - 3`, `Ob = MU_PER_DIE x score` since B15.03 (was `score/2`), `pool = score + 6`).

INTERIM HOMES. `disp` carries `registry_key: None`: this spec is its only home until the registry or the
season's carrier (`Person.attributes`, CR-20) names a key for it; that commit sets the entry's `registry_key` in
the same change. `att` is Perception (ED-IN-0347) and is the whole of the read (PC-18 (1)); Reason (`attr.mind.acuity`) has no combat
role, so an authored acuity does not reach a `Combatant`. (the revert marker is on `combat_systems.reading`).

NOT AN ATTRIBUTE: the party's SKILL SCORE for the verb that opened the fight (A-98: a skill score is not an attribute; `IS-PC-05`,
A-112). It is the skill table's number (`engine/season/seam/wrappers/pool.py::score`, passed in `PersonalCombatInput.scores`) and
lives on the `Combatant` as `c.score` (`combatant.py`), not here. It is read in exactly two places, the pool (`core.resolution_pool`,
with the party's `pool_addends`) and the Ob the opponent rolls against (`core.ob_from_defender`).
"""
from collections import namedtuple

IN_FLUX = 'IN_FLUX'

AttributeSpec = namedtuple('AttributeSpec', 'key default neutral registry_key status')

SPEC = (
    AttributeSpec('strength', 4, 4, 'attr.body.strength', IN_FLUX),   # neutral 4: PC-20 (4)'s arrest term centres on it
    AttributeSpec('agi', 4, 4, 'attr.body.agility', IN_FLUX),
    AttributeSpec('end', 4, None, 'attr.body.endurance', IN_FLUX),
    AttributeSpec('att', 3, None, 'attr.mind.perception', IN_FLUX),
    AttributeSpec('spirit', 3, 4, 'attr.spirit.will', IN_FLUX),   # neutral 4: B15.10's yield roll counts Spirit in whole steps from the 1-7 scale's mid-point (`wrapper._spirit_levels`), as Strength and Coordination centre on it
    AttributeSpec('focus', 3, 3, 'attr.mind.focus', IN_FLUX),
    AttributeSpec('disp', 4, 4, None, IN_FLUX),
)

# THE OTHER INPUT SLOTS (B18.02; the module declares what it can take, never who fills it). Same form as `SPEC`; the host
# fills a slot with a NUMBER and the module never takes the name of a skill, technique or tradition. The six slot families
# and where each is owned:
#   attr   -- `SPEC` above.                       temper -- `SPEC`'s `disp` row (so no tuple of its own).
#   pool   -- `PersonalCombatInput.scores` and `addends` (`core.resolution_pool`, `core.ob_from_defender`).
#   kit    -- `PersonalCombatInput.kits` (`Combatant`'s `weapon` and `armor`).
#   axis   -- `AXES`, below. Fed by `PersonalCombatInput.axes` ({axis: bonus}, `Combatant.skills`).
#   lever  -- `LEVERS`, below. Fed by `PersonalCombatInput.techniques` ({ability: level}, `Combatant.equipped`), which
#             `ability_primitives` turns into a lever's factor or bonus; no second field carries a lever value.
# `default` is the value the engine reads for a fighter who holds none, so an empty slot is today's fight. `neutral` is None
# (no centring literal) and `registry_key` None (no registry row names an axis or a lever yet; the row that does sets it in
# the same change, as `disp`'s will).
#
# AXES: the additive sigma bonus on a defence or contest, 0.0 untrained (`Combatant.skill`; read at
# `combat_systems.balance_eff`, `mode_sigma` and `bind_sigma`). `technique` and `grab` are read by the engine too
# but are WITHHELD from the slot family until a sweep shows them outside the interval (R-PC-43).
AXES = (
    AttributeSpec('balance', 0.0, None, None, IN_FLUX),
    AttributeSpec('parry', 0.0, None, None, IN_FLUX),
    AttributeSpec('dodge', 0.0, None, None, IN_FLUX),
    AttributeSpec('bind', 0.0, None, None, IN_FLUX),
)

# LEVERS: the named modulators `ability_primitives` reads. `default` 1.0 is a FACTOR (`ability_factor`, `*`; the
# product of learned abilities, 1.0 with none) and 0.0 a BONUS (`ability_bonus`, `+`; their sum). Only `counter_success` and
# `anti_overcommit` are read as bonuses.
LEVERS = (
    AttributeSpec('visual', 1.0, None, None, IN_FLUX),
    AttributeSpec('precommit', 1.0, None, None, IN_FLUX),
    AttributeSpec('tactile', 1.0, None, None, IN_FLUX),
    AttributeSpec('tempo', 1.0, None, None, IN_FLUX),
    AttributeSpec('balance', 1.0, None, None, IN_FLUX),
    AttributeSpec('measure', 1.0, None, None, IN_FLUX),
    AttributeSpec('leverage', 1.0, None, None, IN_FLUX),
    AttributeSpec('counter_select', 1.0, None, None, IN_FLUX),
    AttributeSpec('counter_success', 0.0, None, None, IN_FLUX),
    AttributeSpec('anti_overcommit', 0.0, None, None, IN_FLUX),
    AttributeSpec('edge_read', 1.0, None, None, IN_FLUX),
    AttributeSpec('spine_press', 1.0, None, None, IN_FLUX),
    AttributeSpec('edge_grab', 1.0, None, None, IN_FLUX),
    AttributeSpec('choke_control', 1.0, None, None, IN_FLUX),
    AttributeSpec('facing_regime', 1.0, None, None, IN_FLUX),
)

KEYS = tuple(s.key for s in SPEC)
DEFAULT = {s.key: s.default for s in SPEC}
NEUTRAL = {s.key: s.neutral for s in SPEC if s.neutral is not None}

assert len(set(KEYS)) == len(KEYS), f"attribute spec repeats a key: {KEYS}"
for _fam in (AXES, LEVERS):
    assert len({s.key for s in _fam}) == len(_fam), f"a slot tuple repeats a key: {[s.key for s in _fam]}"
